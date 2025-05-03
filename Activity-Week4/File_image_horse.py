import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load CIFAR-10 dataset
(x_train, y_train), (_, _) = tf.keras.datasets.cifar10.load_data()

# Define class names
class_names = ["Airplane", "Automobile", "Bird", "Cat",
               "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]

# Find an index of a horse image
horse_class_index = 7  # The index for "Horse"
horse_indices = np.where(y_train == horse_class_index)[0]
random_horse_index = np.random.choice(horse_indices)

# Show the horse image
plt.figure(figsize=(2, 2))
plt.imshow(x_train[random_horse_index])
plt.title("Horse")
plt.axis("off")
plt.show()
