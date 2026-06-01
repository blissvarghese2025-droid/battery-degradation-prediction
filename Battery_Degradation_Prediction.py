# %%
%pip install scikit-learn


# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from sklearn.linear_model import LinearRegression

df = pd.read_csv("Battery_dataset.csv")

print(df.head())

print("\nColumns in dataset:\n")
print(df.columns)

X = df[["cycle"]]

y = df["BCt"]

model = LinearRegression()

model.fit(X,y)

future_cycles = np.array([250,300,350,400,450])

future_cycles_reshaped = future_cycles.reshape(-1,1)

predicted_capacity = model.predict(future_cycles_reshaped)

print("\nPredicted Future Battery Capacity:\n")

for cycle, capacity in zip(future_cycles, predicted_capacity):

    print(f"Cycle {cycle}: {capacity:4f}")


plt.figure(figsize=(10,6))

plt.scatter(
    X,
    y,
    s = 15,
    alpha = 0.5,
    label = "Actual Battery Capacity"
)

plt.plot(
    X,
    model.predict(X),
    color ="red",
    linewidth = 1,
    label = "Predicted Degradation Trend"
)      

plt.scatter(
    future_cycles,
    predicted_capacity,
    label = "Future capacity Prediction"
)


plt.xlabel("Cycle count")

plt.ylabel("Battery Capacity(BCt)")

plt.title("Battery Degradation Prediction")

plt.legend()

plt.grid(True)

plt.savefig("battery_degradation_prediction.png")

plt.show()


# %%



