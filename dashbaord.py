import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib

# Simulate IMU data (acceleration, gyroscope) as input for the LSTM
# Normally you'd use real data from the wearable
time_steps = 50
features = 6  # 3-axis acceleration + 3-axis gyroscope

# Generate dummy dataset
X = np.random.rand(1000, time_steps, features)
y = np.random.randint(0, 2, 1000)  # Binary classification: 0 = normal, 1 = fatigue

# Normalize input data
scaler = MinMaxScaler()
X_flat = X.reshape(-1, features)
X_scaled = scaler.fit_transform(X_flat).reshape(-1, time_steps, features)

# Define LSTM model
model = Sequential([
    LSTM(64, input_shape=(time_steps, features)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_scaled, y, epochs=5, batch_size=32, verbose=0)

# Save model and scaler
model_path = "/mnt/data/AI_Wearable_Tech_Startup_Kit/LSTM_Model/fatigue_detector_lstm.h5"
scaler_path = "/mnt/data/AI_Wearable_Tech_Startup_Kit/LSTM_Model/scaler.save"

model.save(model_path)
joblib.dump(scaler, scaler_path)

model_path, scaler_path
