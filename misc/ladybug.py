# Ladybug and the Clock
import random
import pandas as pd

def run():
    position = 12
    visited = {position}

    while len(visited) < 12:
        step = random.choice([1, -1])
        position = (position + step - 1) % 12 + 1
        visited.add(position)

    return position

N = 500_000
results = [run() for _ in range(N)]

# Show probability
print("Ladybug probabilities:")
for i in range(1, 12):
    print(f"{i}: {results.count(i)/len(results)*100:.2f}%")

# -------------------------------
# Run Simulation
# -------------------------------

# Build a DataFrame
df = pd.DataFrame(results, columns=["final_position"])

# Compute probabilities
probs = df["final_position"].value_counts(normalize=True).sort_index() * 100

print("Empirical probabilities of final positions with Pandas:")
print(probs.round(2).to_string())

