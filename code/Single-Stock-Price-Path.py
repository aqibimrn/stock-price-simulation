# import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

# declare variables
num_days = 100          # number of days to simulate
price = 100             # initial stock price
prices = [price]        # list to store stock price over time


# function to interpret percentiles
def percentiles(prices):
    # convert list to NumPy array for numerical operations
    final_prices_array = np.array(prices)

    # calculate 5th and 95th percentiles
    p5 = np.percentile(final_prices_array, 5)
    p95 = np.percentile(final_prices_array, 95)

    # print percentile values
    print("5th percentile: ", p5, ". 95th percentile: ", p95)


# function to compute the mean
def mean(prices):
    # calculate average stock price
    avg = sum(prices) / len(prices)
    print("Mean:", avg)


# simulate a single stock price path
for day in range(num_days):
    # generate a random daily return between -1% and +1%
    change = np.random.uniform(-0.01, 0.01)

    # update stock price
    price = price * (1 + change)

    # store daily price
    prices.append(price)


# calculate statistics on the price path
percentiles(prices)
mean(prices)

# plot stock price path
plt.plot(prices)

# add labels and title
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Single Stock Price Path")

# show plot
plt.show()
