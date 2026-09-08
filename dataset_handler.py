"""
AgriVision-CNN - Dataset Handler
Practice/reference implementation for DKA3223.
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms


def load_dataset():
    """Download/load CIFAR-10 and return the training dataset."""
    transform = transforms.ToTensor()

    dataset = datasets.CIFAR10(
        root="./data",
        train=True,
        download=True,
        transform=transform
    )
    return dataset


def show_samples(dataset, number_of_images=3):
    """Display the first three images with their labels."""
    class_names = dataset.classes

    fig, axes = plt.subplots(1, number_of_images, figsize=(10, 3))

    for i in range(number_of_images):
        image, label = dataset[i]

        # Convert CHW tensor -> HWC NumPy array for Matplotlib.
        image_np = np.transpose(image.numpy(), (1, 2, 0))

        axes[i].imshow(image_np)
        axes[i].set_title(class_names[label])
        axes[i].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dataset = load_dataset()
    show_samples(dataset, 3)
