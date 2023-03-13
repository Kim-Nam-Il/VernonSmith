import random
import numpy as np

# Define the parameters of the market
n_participants = 50
fundamental_value = 100
initial_price = 110
cash_per_participant = 1000

# Initialize the market
prices = [initial_price]
cash = [cash_per_participant for i in range(n_participants)]

# Run the market for 50 time steps
for t in range(50):
    # Determine the average price
    avg_price = np.mean(prices)

    # Determine the demand and supply for the asset
    demand = 0
    supply = 0
    for i in range(n_participants):
        # Determine the participant's buying or selling behavior
        if cash[i] >= prices[-1]:
            behavior = random.choice(['buy', 'sell'])
        else:
            behavior = 'sell'

        # Update the participant's cash and behavior based on the current price
        if behavior == 'buy':
            cash[i] -= prices[-1]
            demand += 1
        elif behavior == 'sell':
            cash[i] += prices[-1]
            supply += 1

    # Determine the new price based on the demand and supply
    new_price = fundamental_value + (demand - supply) * 0.1

    # Update the market with the new price
    prices.append(new_price)

# Print the final price and the total cash held by the participants
print("Final price:", prices[-1])
print("Total cash held:", sum(cash))
