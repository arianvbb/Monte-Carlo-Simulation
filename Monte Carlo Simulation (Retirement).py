import numpy as np
import matplotlib.pyplot as plt


# Colleting data and setting values
initial_amount = float(input("Enter the initial investment amount: "))
annual_contribution = float(input("Enter the annual contribution amount: "))
years = int(input("Enter the amount of years until retirement: "))
goal = int(input("What's your desired amount to have by retirement?: "))
portfolio_value = initial_amount
last_year_crash = False
mc_sims = 250 # Number of simulations

all_simulations = []

# Running desired number of simulations
for m in range(0, mc_sims):
    simulation_path = []
    portfolio_value = initial_amount
    last_year_crash = False

    # Running each individual simulation accounting for market crashes, growth and yearly contributions.
    for t in range(0,years + 1):

        if last_year_crash == True:
            crash_prob = 0.25
            if np.random.rand() < crash_prob:
                rate = np.random.normal(-30, 20)
                portfolio_value = portfolio_value + annual_contribution
                portfolio_value = portfolio_value * (1 + rate / 100)
                last_year_crash = True
                simulation_path.append(portfolio_value)
            else:
                rate = np.random.normal(7, 12)
                portfolio_value = portfolio_value + annual_contribution
                portfolio_value = portfolio_value * (1 + rate / 100)
                last_year_crash = False
                simulation_path.append(portfolio_value)
            
        else:
            crash_prob = 0.07
            if np.random.rand() < crash_prob:
                rate = np.random.normal(-30, 20)
                portfolio_value = portfolio_value + annual_contribution
                portfolio_value = portfolio_value * (1 + rate / 100)
                last_year_crash = True
                simulation_path.append(portfolio_value)
            else:
                rate = np.random.normal(7, 12)
                portfolio_value = portfolio_value + annual_contribution
                portfolio_value = portfolio_value * (1 + rate / 100)
                last_year_crash = False
                simulation_path.append(portfolio_value)
    all_simulations.append(simulation_path)
    final_values = [sim[-1] for sim in all_simulations] # Indexing final net worth in each simulation
    reached_goal = sum(1 for value in final_values if value >= goal) # Finding the sum of each value higher than our original goal set by the user.


# For each simulation making them transperent and setting a color then plotting and printing the % chance of reaching the set goal with the annual contributions.
for simulation in all_simulations:
    plt.plot(simulation, alpha=0.3, color='blue')
plt.xlabel('Years')
plt.ylabel('Portfolio Value')
plt.axhline(goal, color = 'r')
print((reached_goal/mc_sims) * 100, "%")
plt.show()

#PS: The data for expected annual return and standard deviation was gathered from an online search and aren't meant to be treated as hard fact.