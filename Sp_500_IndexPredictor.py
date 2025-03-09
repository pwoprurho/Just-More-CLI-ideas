import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("sp500_index.csv", parse_dates=["Date"], index_col="Date")
data = df["S&P500"].values.reshape(-1, 1)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

def create_sequences(data, seq_length):
    xs = []
    ys = []
    for i in range(len(data) - seq_length - 1):
        x = data[i:(i + seq_length)]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

seq_length = 60
X, Y = create_sequences(scaled_data, seq_length)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.3, shuffle= False)

model = Sequential()
model.add(LSTM(50, return_sequences=True,input_shape=(X_train.shape[1], 1)))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X_train, Y_train, epochs=5, batch_size=32)

predictor = model.predict(X_test)
predictor = scaler.inverse_transform(predictor)
Y_test = scaler.inverse_transform(Y_test)

mse = mean_squared_error(Y_test, predictor)
mae = mean_absolute_error(Y_test, predictor)
r2 = r2_score(Y_test, predictor)

print(f"mean squared error is {mse}")
print(f"meam absolute error is {mae}")
print(f"r2 score is {r2}")
print(df.info())