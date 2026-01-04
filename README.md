# Stock Price Simulation Using Monte Carlo Methods

## Project Overview
This project explores how stock prices would evolve over time using simulations. 
By modelling daily percentage changes and with the concepts of compounding, the project aims to demonstrate how random changes can lead to a wide range of possible outcomes.

The project contains two related simulations:
1. A single stock price path simulation, which illustrates how a possible price path changes over time.
2. A Monte Carlo simulation, which runs many independent price paths to analyze the distributions of possible final prices.

The main goal of this project is to understand and demonstrate the effects of randomness, compounding, and uncertainty in financial markets, whilst also utilizing concepts of mathematical modeling and programming.

## Modeling Approach

The stock price begins at an initial price of $100 a day. Each day, the price would change by a random percentage between 1% to +1%. The new price is then calculated using the formula:
 New Price = Previous Price x (1 + Daily Return)

This formula demonstrates compounding, which is a key feature of real stock price behavior.

### Why Simulation?

Stock prices are often influenced by many unpredictable factors. Rather than attempting to predict the final price, the simulation would allow us to explore a range of possible outcomes and to analyze their properties.

### Simulation Parameters
- Initial price: $100
- Time horizon: 100 days
- Daily return: uniformly distributed between -1% and +1%
- Monte Carlo simulations: 1,000 independent price paths
- Tools used: Python, NumPy, Matplotlib

## Results

### Single Stock Price Path
A single simulated stock price path over 100 days was generated to illustrate how prices evolve day-to-day under randomness. This plot highlights how even small daily fluctuations can lead to noticeable divergence over time.

Saved as: `plots/single_price_path.png`

### Monte Carlo Simulation
A Monte Carlo simulation consisting of 1,000 independent price paths was run over a 100-day period. The final prices from the simulations were collected and analysed.

Key statistics:
- **Mean final price:** 109.809  
- **5th percentile (worst 5% outcome):** 44.253  
- **95th percentile (best 5% outcome):** 174.109  

The histogram of final prices shows a *skewed distribution*, despite the daily returns being symmetric. This asymmetry arises due to the effect of compounding. The effect of compounding on large positive returns can compound more strongly than equivalent losses.

Saved as: `plots/final_price_distribution.png`

## Interpretation
Although the daily returns are between -1% and +1%, the distribution of the final prices becomes asymmetric over time. The upper tail of the distribution is longer, which puts the mean above its initial price.

I believe this demonstrates an important concept in the field of quantitative finance: *compounding transforms symmetric randomness into asymmetric outcomes*.

The use of percentiles provides a useful and insightful way to quantify risk:
1. The 5th percentile indicates a low-end outcome. It is an outcome that occurs in 5% of cases.
2. The 95th percentile shows strong gains that are certainly possible but rare.

## Limitations
This model is intentionally simple. It does not capture:

- Real-world distributions
- Market trends or jumps
- Correlations between assets
- Transaction costs or trading strategies

These limitations suggest areas for future improvements, which may help create more realistic models.

## Project Journal
A detailed day-by-day record of the development process is available in `journal.md`.

This includes:
- The planning and learning resources for the completion of this project
- Implementation decisions
- Challenges encountered
- Interpretation of results achieved

## Future extensions
Possible next steps include:
- Using normal distribution to model and extract results
- Calibrating parameters using real stock data
- Comparing outcomes across different time horizons

## Author
This project was completed as an independent learning exercise to improve my skills in simulation, programming, and quantitative reasoning.