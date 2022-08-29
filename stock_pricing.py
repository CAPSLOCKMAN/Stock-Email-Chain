# Obtains individual stock price per input
# and continuous until user [q]uits

import yfinance as yf


while True:

	user_input = input("Stock Ticker Symbol or [Q]uit: ").upper()

	if user_input == "Q":
		quit()

	elif user_input != "Q":
		#stock_info = yf.Ticker(f'{user_input}').info
		stock_info = yf.Ticker(user_input).info

		print(f'\n{user_input} is currently at {stock_info["regularMarketPrice"]}.\n')



## Alert or email me when a certain
## stock reaches a specific 
## price point

