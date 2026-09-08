import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from cnn_model import AgriVisionCNN


# ============================================================
# AGRIVISION-CNN : TRAINING CONFIGURATION
# ============================================================

LEARNING_RATE = 0.001
EPOCHS = 3
BATCH_SIZE = 32


def load_training_data():

    transform = transforms.ToTensor()

    dataset = datasets.CIFAR10(
        root="./data",
        train=True,
        download=True,
        transform=transform
    )

    # Use a manageable subset for local practical testing.
    dataset = torch.utils.data.Subset(
        dataset,
        range(5000)
    )

    data_loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    return data_loader


def train_model():

    # Select GPU if available, otherwise use CPU.
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print("=" * 55)
    print("           AGRIVISION-CNN TRAINING")
    print("=" * 55)
    print(f"Device        : {device}")
    print(f"Learning Rate : {LEARNING_RATE}")
    print(f"Epochs        : {EPOCHS}")
    print(f"Batch Size    : {BATCH_SIZE}")
    print("-" * 55)

    train_loader = load_training_data()

    model = AgriVisionCNN(num_classes=10)
    model = model.to(device)

    # Loss function
    criterion = nn.CrossEntropyLoss()

    # Optimizer
    optimizer = optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE
    )

    # Control structure for storing loss history.
    loss_history = []

    # ========================================================
    # TRAINING LOOP
    # ========================================================

    for epoch in range(EPOCHS):

        model.train()

        total_loss = 0.0

        for images, labels in train_loader:

            images = images.to(device)
            labels = labels.to(device)

            # -------------------------------
            # 1. FORWARD PROPAGATION
            # -------------------------------
            outputs = model(images)

            # -------------------------------
            # 2. LOSS CALCULATION
            # -------------------------------
            loss = criterion(outputs, labels)

            # -------------------------------
            # 3. BACKWARD PROPAGATION
            # -------------------------------
            optimizer.zero_grad()
            loss.backward()

            # -------------------------------
            # 4. UPDATE MODEL PARAMETERS
            # -------------------------------
            optimizer.step()

            total_loss += loss.item()

        epoch_loss = total_loss / len(train_loader)

        loss_history.append(epoch_loss)

        print(
            f"Epoch [{epoch + 1}/{EPOCHS}] "
            f"| Loss: {epoch_loss:.4f}"
        )

    print("-" * 55)
    print("Training completed successfully.")
    print("=" * 55)

    return loss_history


if __name__ == "__main__":
    train_model()