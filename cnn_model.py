import torch.nn as nn


# AI Code Assistant Prompt:
# 1. Create a modular PyTorch CNN for the AgriVision-CNN image classification project.
# 2. Use at least two convolutional layers with ReLU and pooling for feature extraction.
# 3. Improve the basic CNN using Batch Normalization, Dropout and Adaptive Pooling.
# 4. Make the model suitable for CIFAR-10 with 10 output classes and easy to explain.


class AgriVisionCNN(nn.Module):

    def __init__(self, num_classes=10):
        super().__init__()

        self.features = nn.Sequential(

            # Convolution Block 1
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2),

            # Convolution Block 2
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            # Convolution Block 3
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),

            # Reduce feature map size
            nn.AdaptiveAvgPool2d((1, 1))
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.3),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x