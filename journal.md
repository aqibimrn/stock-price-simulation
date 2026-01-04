DAY 1
=====

Well, welcome to my journal for creating a Stock Price Simulation. I got an idea of this project after I decided I wanted to do a project where I could combine math and coding, and stock prices are a good example of real-world data that changes over time.

I honestly do not know how to do this, but I would like to do this project on Python. Upon research, I found this website (https://www.tutorialspoint.com/numpy/numpy\_matplotlib.htm) and learnt I would need to use the NumPy and Matplotlib. I will for now polish up on my python skills.

DAY 2
=====

Right now, I am planning on creating a stimulation Single Stock Path Simulation, which would simulate one stock price path over 100 days, using one random daily change per day. I would be using a for loop for this and it would generate a random daily change (between -1% to 1%). Each day builds on the previous day, which would result in compounding, just like real stock prices. This code would simulate one stock price path over 100 days, using one random daily change per day.

Day 3
=====

I have now fully familiarized myself with all the features of Matplotlib so I can also plot a graph of my findings.

I have created a plan and created a test program which ran with success. I saved the output as a file and recorded the 5th and 95th percentiles & the mean, which were as follows:
5th percentile (worst 5% outcome): 96.814
95th percentile (best 5% outcome): 103.885
Mean: 100.559

The mean tells us that the process is roughly fair / unbiased and that there is no strong upward or downward drift.

The 5th percentile tells us that in 95% of cases, the final price is above $96.81, and that there is a 5% chance of losing more than about 3.2% (96.82 - 100).

The 95th percentile tells us that big gains are possible but rare, and that there’s only a 5% chance of gaining more than about 3.9% (103.89 - 100).

In simple words, after 100 days, the stock usually ends between $96.8 and $103.9, with an average outcome slightly above $100.

DAY 4
=====

Next, I attempted to create a Monte Carlo simulation to model the distribution of possible final stock prices over a 100-day period using random daily percentage changes. 1,000 independant price path simulations were run over a 100-day period, where the stock price changed by a random percentage between -1% and +1% each day.

I then analyzed the results by calculating their mean and the 5th and 95th percentiles and plotting a histogram of the outcomes. This process helped me to realize how even such small daily changes can lead to a big distribution of the final prices and demonstrated the usefulness of Monte Carlo methods of modeling uncertainity.

A challange I encountered was choosing a model for daily price changes, since the assumptions made about randomness directly affect the realism of the simulation. Eventually, I decided to use a daily change between -1% to +1%, as it is quite interesting to see how even smaller daily changes can lead to big distributions of the prices!

I recorded the mean, 5th and 95th percentiles as below:
5th percentile (worst 5% outcome): 44.253
95th percentile (best 5% outcome): 174.109
Mean: 109.809

I can observe that unlike the single-stock-price-path simulation, the Monte Carlo simulation produces a highly skewed distribution. This is evident from the asymmetry between the distance from the starting price of 100 to the 5th percentile and from 100 to the 95th percentile (where the distance from 100 to 95th percentile is greater!).

Although the daily returns are symmetric, the effect of compounding causes the distribution of final prices to become asymmetric. As a result, the upper tail of the distribution pulls the mean upward, causing the mean final price to be significantly higher than the starting price.