# stock_analysis_bot

An advanced stock analysis bot that leverages AI agents to provide comprehensive stock analysis and investment recommendations.

## Features

- Multi-agent system for in-depth stock analysis
- Real-time stock data fetching using yfinance
- Technical analysis
- Financial statement analysis
- Market sentiment and news analysis
- AI-powered investment recommendations
- Telegram bot interface

## Requirements & Setup

1. Python 3.6+

2. Install required libraries:

```python
python3 -m pip install -U -r requirements.txt
```

3. Set up environment variables:

- Create a `.env` file in the project root
- Add the needed variables like:

```bash
GROQ_API_KEY='your_groq_api_key'
TELEGRAM_TOKEN='your_telegram_bot_token'
ANTHROPIC_API_KEY='your_anthropic_api_key'
```

## Usage

1. Run the main script:

```python
python3 main.py
```

1. Interact with the bot via Telegram:

- Start a chat with your bot on Telegram
- Use the `/start` command to begin
- Ask about any company stock (e.g., "AAPL" for Apple Inc.)

## Components

- **Agents**: Researcher, Technical Analyst, Financial Analyst, Hedge Fund Manager
- **Tools**: Stock News, Stock Price, Income Statement, Balance Sheet, Insider Transactions
- **Tasks**: Research, Technical Analysis, Financial Analysis, Investment Recommendation

## How it works

1. User sends a stock ticker to the Telegram bot
2. The bot initiates a crew of AI agents to analyze the stock
3. Agents perform their specialized tasks using various tools and LLMs
4. The Hedge Fund Manager synthesizes all information to provide an investment ecommendation
5. The bot sends the comprehensive analysis back to the user via Telegram

## Disclaimer

This bot is for educational and research purposes only. Always consult with a qualified financial advisor before making investment decisions.

## Example input and output

- Using Claude-3.5-sonnet as the base LLM

> AMD

```
Investment Recommendation for AMD Stock: MODERATE BUY

Rationale:
After careful consideration of the comprehensive research, technical analysis, and financial reports provided, I recommend a MODERATE BUY for AMD's stock. This recommendation is based on several key factors:

1. Strong Market Position and Growth Potential:
AMD has demonstrated robust revenue growth, reporting $22.68 billion for the fiscal year 2023. The company's significant investment in research and development ($5.872 billion in 2023) indicates a strong commitment to innovation and maintaining its competitive edge in the semiconductor industry. This positions AMD well to capitalize on growing markets, particularly in AI and data center applications.

2. Positive Analyst Sentiment:
Wall Street analysts generally have a bullish outlook on AMD stock. The Average Brokerage Recommendation (ABR) of 1.36 on a scale of 1 to 5 (1 being Strong Buy) is highly favorable, with 29 out of 36 analysts giving a Strong Buy recommendation. This positive sentiment reflects confidence in AMD's future prospects.

3. Technical Strength:
The technical analysis reveals a strong upward trend in AMD's stock price, with a significant gain of approximately 13.7% from June 17, 2024, to July 16, 2024. The stock is trading above its short-term moving averages, indicating strong bullish momentum. The recent consolidation near all-time highs suggests potential for further upside.

4. Solid Financial Position:
AMD maintains a strong liquidity position with $5.773 billion in cash, cash equivalents, and short-term investments as of December 31, 2023. This provides the company with financial flexibility to invest in growth opportunities and navigate potential market challenges.

5. Competitive Position in AI and Data Center Markets:
AMD's position in the AI chip market and its performance in data center segments are significant focus areas for investors. The company's ability to compete effectively with Intel and NVIDIA in these high-growth sectors presents substantial opportunities for future growth.

Risks and Considerations:
1. Earnings Estimate Revisions:
Despite positive analyst recommendations, AMD currently has a Zacks Rank #4 (Sell), and the Zacks Consensus Estimate for the current year has declined 0.3% over the past month. This discrepancy suggests some caution may be warranted.

2. Profitability Concerns:
AMD's net profit margin of 3.77% for 2023 is relatively low, indicating room for improvement in cost management and operational efficiency. Investors should monitor the company's ability to translate strong revenue into improved bottom-line results.

3. Competitive Pressures:
Increased competition in the AI chip market, especially from Intel and NVIDIA, poses a significant risk. AMD's ability to maintain its market share and technological edge will be crucial for long-term success.

4. Market Volatility:
The semiconductor industry is subject to cyclical trends and macroeconomic factors. Potential slowdowns in PC and gaming markets could affect AMD's consumer segment, while factors such as inflation and interest rates may impact overall tech sector performance.

Investment Strategy and Time Horizon:
For long-term investors (3-5 years), AMD presents an attractive opportunity given its strong market position and growth potential in AI and data center markets. The company's solid financial position and commitment to R&D support a positive long-term outlook.

For medium-term investors (1-2 years), a moderate buy stance is appropriate, with a focus on accumulating shares during potential pullbacks to support levels identified in the technical analysis (e.g., $170-$175 range).

Short-term traders should exercise caution due to potential volatility around the upcoming earnings report on July 30, 2024. They may consider entries on pullbacks to support levels with tight stop-losses.

Conclusion:
AMD's strong market position, positive analyst sentiment, technical strength, and growth potential in key markets support a MODERATE BUY recommendation. However, investors should remain mindful of the risks, including profitability concerns and intense competition. Regular reassessment of the investment thesis is advised, particularly following the upcoming earnings report and in light of evolving market conditions in the semiconductor industry.
```
