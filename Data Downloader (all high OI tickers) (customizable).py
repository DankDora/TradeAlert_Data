#! python3
# Data Downloader.py --  This calls the Data & Parser classes and
			#	 downloads all data for all HIGH OI tickers from .txt
						
import tradealertdownloaderclass as datadl

import sys
import os
import re
# ~ Data("XLU").update("intra_volume", amount = 0)
import time
# "Update()" class method inputs:
# ~ def update(self, chart, date = closestTradingDate(), amount = 1):






with open(r"C:\Users\lorig\Desktop\PythonCode\Projects, Exercises, Programs\Trade Alert Journey\high_OI_tickers.txt") as f:
	lines = f.readlines()

#try to use (.*)? to make it not-greedy so it takes first found
tickerRegex = re.compile(r"'([.A-Za-z]*)', ")

tickersList = tickerRegex.findall(lines[0])
print(len(tickersList))

# ~ print(tickersList)


# ~ for ticker in tickersList:
	# ~ if ticker == 

while(1):
	counter = 0
	try:
		for ticker in tickersList:
			# ~ ## ~ ticker = "NXTG"
			datadl.Data(ticker).update(chart = "intra_volume", amount = 0) 
			
	except (IndexError):
		
		print("IndexError...trying again")
		time.sleep(5)
		continue

	except (TypeError):
		print("TypeError...trying again")
		time.sleep(5)
		continue
