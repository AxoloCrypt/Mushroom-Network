from tensorflow import keras
import numpy as np
import pandas as pd

train_df = pd.read_csv('../datasets/training.csv')
train_df.pop('Unnamed: 0')
print(train_df.head())

np.random.shuffle(train_df.values)

train_df_x = train_df.copy()
train_df_y = train_df_x.pop('class')

print(train_df_x.head())

model = keras.Sequential([
    keras.layers.Dense(24, input_shape=(23,), activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy()])

x = np.column_stack((train_df_x, train_df_y))

model.fit(x, train_df['class'].values, batch_size=23, epochs=10)

test_df = pd.read_csv('../datasets/testing.csv')
test_df.pop('Unnamed: 0')

test_df_x = test_df.copy()
test_df_y = test_df_x.pop('class')

test_x = np.column_stack((test_df_x, test_df_y))

print("#### EVALUATION ####")
model.evaluate(test_x, test_df['class'].values)
