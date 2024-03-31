import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.keras import layers, losses
final = pd.read_excel(r"C:\Users\Yihuai Cai\Desktop\最终.xlsx")
label = final['类型']
encoder = LabelEncoder()
encoder.fit(label)
encoded_Y = encoder.transform(label)
dummy_y = to_categorical(encoded_Y)
X = final.drop(columns=['总含量'])
# X=np.array(X)
print(X.shape)

dummy_y

X

X = X.drop(columns=['文物采样点','纹饰','类型','颜色'])
X

X=np.array(X)
X = X.astype('float64')
label = np.array(label)
train_features, val_test_features, train_labels, val_test_labels = train_test_split(X, dummy_y, test_size = 0.3,
                                                                           shuffle=True, random_state = 42)
X_val, X_test, Y_val, Y_test = train_test_split(val_test_features, val_test_labels, test_size=0.5, shuffle=True, random_state=42)


def create_model(data):
    model = tf.keras.Sequential([
      layers.Dense(data.shape[1], activation='relu'),
      layers.Dense(30, activation='relu'),
      layers.Dense(30, activation='relu'),
      layers.Dense(60, activation='relu'),
      layers.Dense(60, activation='relu'),
      layers.Dense(2, activation="softmax")
  ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

train_features = np.array(train_features)
model1 = create_model(train_features)

# Define the Keras TensorBoard callback.
from datetime import datetime
from tensorflow.keras.callbacks import ModelCheckpoint
logdir="logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
mcp_save = ModelCheckpoint('output/bestmodel.tf', save_best_only=True, monitor='val_loss', mode='min')

history=model1.fit(
    train_features, train_labels,
     validation_data=(X_val, Y_val),
    verbose=1,batch_size=7, epochs=50,callbacks=[tensorboard_callback, mcp_save])

#plot loss
import matplotlib.pyplot as plt
def plot_loss(history):
    plt.plot(history.history['loss'], label='Train_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 1])
    plt.xlabel('Epoch')
    plt.ylabel('Error [Diabetes]')
    plt.legend()
    plt.grid(True)

plot_loss(history)


#plot accuracy
def plot_loss(history):
    plt.plot(history.history['accuracy'], label='Train_accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.ylim([0, 1])
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy [Diabetes]')
    plt.legend()
    plt.grid(True)
plot_loss(history)

#测试测试集

prediction = np.around(model1.predict(X_test))
print(prediction)

# Use the forest's predict method on the test data
predictions = model1.predict(X_test)
# Calculate mean absolute errors
score = model1.evaluate(X_test, Y_test,verbose=1)

# Compare Prediction
print("Train acc: " , model1.evaluate(train_features, train_labels))
print("Test acc: ", model1.evaluate(X_test, Y_test))