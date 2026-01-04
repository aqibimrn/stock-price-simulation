# import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

# declare variables
num_days = 100              # number of days in each simulation
num_simulations = 1000      # total number of Monte Carlo simulations
price = 100                 # initial stock price
final_prices = [price]      # list to store final prices from each simulation


# function to interpret percentiles
def percentiles(prices):
    # convert list to NumPy array for numerical operations
    final_prices_array = np.array(prices)

    # calculate 5th and 95th percentiles
    p5 = np.percentile(final_prices_array, 5)
    p95 = np.percentile(final_prices_array, 95)

    # print percentile values
    print("5th percentile: ", p5, ". 95th percentile: ", p95)
    return [p5, p95]

# function to compute the mean
def mean(prices):
    # calculate average final price
    avg = sum(prices) / len(prices)
    print("Mean:", avg)


# Monte Carlo simulation of stock prices
for sim in range(num_simulations):
    # simulate price movement over num_days

    for day in range(num_days):
        # generate a random daily return between -1% and +1%
        change = np.random.uniform(-0.01, 0.01)
        price = price * (1 + change)

    # store the final price after 100 days
    final_prices.append(price)

# calculate statistics on outcomes
percentile_store = []
percentile_store = percentiles(final_prices)
mean(final_prices)

# plot histogram of results
plt.hist(final_prices, bins=50, alpha=0.7, color='blue')

# plot percentile lines
plt.axvline(percentile_store[0], color='red', linestyle='dashed', label='5th percentile')
plt.axvline(percentile_store[1], color='green', linestyle='dashed', label='95th percentile')

# add labels and title
plt.xlabel("Final Price")
plt.ylabel("Frequency")
plt.title("Distribution of Final Stock Prices")

# show legend and plot
plt.legend()
plt.show()
