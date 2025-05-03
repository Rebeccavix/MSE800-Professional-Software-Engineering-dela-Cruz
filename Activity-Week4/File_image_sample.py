import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Define class names
class_names = ["Airplane", "Automobile", "Bird", "Cat",
               "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]

# Function to show an image


def show_image(index):
    plt.figure(figsize=(2, 2))
    plt.imshow(x_train[index])
    plt.title(class_names[y_train[index][0]])
    plt.axis("off")
    plt.show()


# Show a random image
random_index = np.random.randint(0, len(x_train))
show_image(random_index)
