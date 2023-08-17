# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 05:19:33 2023

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Read the stock market dataset
data = pd.read_csv("file:///C:/Users/Dell/Downloads/stock_market_data.csv")  # Replace "your_stock_data.csv" with the actual filename

# Convert the 'datetime' column to a pandas datetime object
data['datetime'] = pd.to_datetime(data['datetime'])

# Set the 'datetime' column as the index
data.set_index('datetime', inplace=True)

# Plot stock market data using Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x=data.index, y='close', label='Close Price')
sns.lineplot(data=data, x=data.index, y='open', label='Open Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Market Analysis')
plt.legend()
plt.grid(True)
plt.show()

# Train the ARIMA model
p, d, q = 7, 0, 6
model = ARIMA(data['close'], order=(p, d, q))
results = model.fit()

# Forecast stock prices for the next year (365 days)
forecast_steps = 365
forecast = results.forecast(steps=forecast_steps)

# Calculate the average open and close prices for the next year
average_open_price = forecast.mean()
average_closing_price = forecast.iloc[-1]

# Determine if opening and closing prices have increased
last_actual_open = data['open'].iloc[-1]
last_actual_close = data['close'].iloc[-1]
increase_open = last_actual_open < average_open_price
increase_close = last_actual_close < average_closing_price

increase_open_str = "increased" if increase_open else "not increased"
increase_close_str = "increased" if increase_close else "not increased"

print(f"\nAverage Open Price for 2024: {average_open_price:.2f} ({increase_open_str})")
print(f"Average Closing Price for 2024: {average_closing_price:.2f} ({increase_close_str})")

# Evaluate the accuracy of the ARIMA model using Mean Squared Error (MSE)
actual_data = data['close'].iloc[-forecast_steps:]
mse = mean_squared_error(actual_data, forecast)
accuracy = 1 - (mse / actual_data.var())
print(f"\nModel Accuracy (R-squared): {accuracy:.2f}")

# Bar chart plots for opening and closing prices
plt.figure(figsize=(12, 6))
plt.bar(["Actual Open", "Forecasted Open"], [last_actual_open, average_open_price], color=['blue', 'green'])
plt.xlabel('Price Type')
plt.ylabel('Price')
plt.title('Actual vs. Forecasted Open Prices')
plt.grid(True)
plt.show()
print("Suggestions: Comparing actual and forecasted opening prices provides insight into potential market fluctuations. Consider these trends when planning budgets for purchasing stock products, as price changes can impact initial investments.")
plt.figure(figsize=(12, 6))
plt.bar(["Actual Close", "Forecasted Close"], [last_actual_close, average_closing_price], color=['blue', 'green'])
plt.xlabel('Price Type')
plt.ylabel('Price')
plt.title('Actual vs. Forecasted Closing Prices')
plt.grid(True)
plt.show()
print("Suggestions: Analyze the differences between actual and forecasted closing prices. This can help in estimating potential gains or losses when selling stock products. Adjusting selling strategies based on these trends could optimize earnings.")
# Histogram plots for actual and forecasted closing prices
plt.figure(figsize=(12, 6))
plt.hist(actual_data, bins=30, color='blue', alpha=0.7, label='Actual Closing Prices')
plt.hist(forecast, bins=30, color='green', alpha=0.7, label='Forecasted Closing Prices')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.title('Histogram of Actual vs. Forecasted Closing Prices')
plt.legend()
plt.grid(True)
plt.show()
print("Suggestions: Use the histogram to assess the distribution of actual and forecasted closing prices. This understanding can guide decisions about setting prices for stock products to align with market trends while maintaining profitability.")
