# https://www.youtube.com/watch?v=-59bKxwir5Q

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())



from crewai import Agent, Task, Crew
from crewai_tools import tool, ScrapeWebsiteTool

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import yfinance as yf

#*-----------------Tools-----------------*#

@tool("Stock News")
def stock_news(ticker):
    """
    Useful to get news about a stock.
    The input should be a ticker, for example AAPL, NET.
    """
    ticker = yf.Ticker(ticker)
    return ticker.news

scrape_tool = ScrapeWebsiteTool()

@tool("Stock Price")
def stock_price(ticker):
    """
    Useful to get stock price data.
    The input should be a ticker, for example AAPL, NET.
    """
    ticker = yf.Ticker(ticker)
    return ticker.history(period = "1mo")

@tool("Income statement")
def income_stmt(ticker):
    """
    Useful to get the income statement of a company.
    The input to this tool should be a ticker, for example AAPL, NET.
    """
    ticker = yf.Ticker(ticker)
    income_statement = ticker.income_stmt
    
    # Example of checking if the DataFrame is empty
    if income_statement.empty:
        return "No income statement data available."
    
    return income_statement

@tool("Balance Sheet")
def balance_sheet(ticker):
    """
    Useful to get the balance sheet of a company.
    The input to this tool should be a ticker, for example AAPL, NET.
    """
    ticker = yf.Ticker(ticker)
    return ticker.balance_sheet

@tool("Insider Transactions")
def insider_transactions(ticker):
    """
    Useful to get insider transactions of a stock.
    The input to this tool should be a ticker, for example AAPL, NET.
    """
    ticker = yf.Ticker(ticker)
    return ticker.insider_transactions


#*-----------------Agents-----------------*#

researcher = Agent(
    role = "Researcher",
    goal = """
        Gather and interpret vast amounts of data to
        provide a comprehensive overview ofthe sentiment
        and news surrounding a stock.
    """,
    backstory = """
        You're skilled in gathering and interpreting data
        from various sources. You read each data source
        carefully and extract the most important information.
        Your insights are crucial for making informed
        investment decisions.
    """,
    tools = [
        scrape_tool,
        stock_news
    ],
    verbose = True,
)
technical_analyst = Agent(
    role = "Technical Analyst",
    goal = """
        Analyze the movements of a stock and provide
        insights on trends, entry points, resistance and
        support levels.
    """,
    backstory = """
        An expert in technical analysis, you're known
        for your ability to predict stock prices.
        You provide valuable insights to your customers.
    """,
    tools = [
        stock_price
    ],
    verbose = True,
)
financial_analyst = Agent(
    role = "Financial Analyst",
    goal = """
        Use financial statements, insider trading data
        and other metrics to evaluate a stock's financial
        health and performance.
    """,
    backstory = """
        You're a very experienced investment advisor
        that looks at a company's financial health,
        market sentiment, and qualitative data to
        make informed recommendations.
    """,
    tools = [
        income_stmt,
        balance_sheet,
        insider_transactions
    ],
    verbose = True,
)
hedge_fund_manager = Agent(
    role = "Hedge Fund Manager",
    goal = """
        Manage a portfolio of stocks and make investment
        decisions to maximize returns using insights
        from financial analysts and researchers.
    """,
    backstory = """
        You're a seasoned hedge fund manager with a proven
        track record of making profitable investments.
        You always impress your clients.
    """,
    verbose = True,
)


#*-----------------Tasks-----------------*#

research = Task(
    description = """
        Gather and analyze the latest news and
        market sentiment surrounding
        {company}'s stock. Provide a summary
        of the news and any notable shifts in sentiment.
    """,
    agent = researcher,
    expected_output = """
        Your final answer MUST be a detailed
        summary of the news and market
        sentiment surrounding the stock.
    """,
)
technical_analysis = Task(
    description = """
        Conduct a technical analysis of the {company}
        stock price movements and identify
        key support and resistance levels chart patterns.
    """,
    agent = technical_analyst,
    expected_output = """
        Your final answer MUST be a report
        with potential entry points, price targets
        and any other relevant information.
    """,
)
financial_analysis = Task(
    description = """
        Analyze the {company}'s financial statements,
        balance sheet, insider trading data
        and other metrics to evaluate {company}'s
        financial health and performance.
    """,
    agent = financial_analyst,
    expected_output = """
        Your final answer MUST be a report with
        an overview of {company}'s
        revenue, earnings, cash flow, and
        other key financial metrics.
    """,
)
investment_recommendation = Task(
    description = """
        Based on the research, technical analysis, and
        financial analysis reports, provide a detailed
        investment recommendation for {company} stock.
    """,
    agent = hedge_fund_manager,
    expected_output = """
        Your final answer MUST be a detailed
        recommendation to BUY, SELL or HOLD the stock.
        Provide a detailed rationale for your recommendation.
    """,
    context = [
        research,
        technical_analysis,
        financial_analysis,
    ],
    output_file = "investment_recommendation.md",
)



#*-----------------Crew-----------------*#

class StockQA:
    def __init__(self):
        self.crew = Crew(
            tasks=[
                research,
                technical_analysis,
                financial_analysis,
                investment_recommendation
            ],
            agents=[
                researcher,
                technical_analyst,
                financial_analyst,
                hedge_fund_manager
            ],
            verbose=2,
        )

    def get_result(self, query):
        result = self.crew.kickoff(
            inputs={
                "company": query
            }
        )
        return result


#*-----------------Telegram Bot-----------------*#

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Ask me about company stock.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    stock_qa = StockQA()
    response = stock_qa.get_result(query)
    await update.message.reply_text(response)

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
