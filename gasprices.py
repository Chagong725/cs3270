from collections import defaultdict
from datetime import datetime

prices_by_year = defaultdict(lambda: defaultdict(list))

with open('gas_prices.txt', 'r') as f:
    for line in f:
        date_str, price_str = line.strip().split(':')        
        date = datetime.strptime(date_str, '%m-%d-%Y')
        price = float(price_str)
        prices_by_year[date.year][date.month].append(price)

for year in sorted(prices_by_year.keys()):
    yearly_prices = [price for month in prices_by_year[year].values() for price in month]
    print(f'{year}:')
    print(f'    Low: ${min(yearly_prices):.2f}, Avg: ${sum(yearly_prices)/len(yearly_prices):.2f}, High: ${max(yearly_prices):.2f}')
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October','November','December']
    
    for i, month in enumerate(months, start=1):
      if i in prices_by_year[year]:
          monthly_avg_price = sum(prices_by_year[year][i]) / len(prices_by_year[year][i])
          print(f'    {month}   ${monthly_avg_price:.2f}')
