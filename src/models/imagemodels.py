from typing import Tuple
import gin
import torch
from torch import nn


@gin.configurable
class NeuralNetwork(nn.Module):
    def __init__(self, num_classes: int, units1: int, units2: int) -> None:
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, units1),
            nn.ReLU(),
            nn.Linear(units1, units2),
            nn.ReLU(),
            nn.Linear(units2, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

@gin.configurable
class CNN(nn.Module):
    def __init__(self, num_classes: int) -> None:
        super().__init__()

        self.convolutions = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.convolutions(x)
        logits = self.dense(x)
        return logits


@gin.configurable
class CNNNet(nn.Module):
    '''
    CNN voor Experimenten
    '''

    def __init__(self, layer1: int, layer2: int, hidden: int, num_classes: int) -> None:
        super().__init__()

        self.convolutions = nn.Sequential(
            nn.Conv2d(1, layer1, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(layer1, layer2, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)  # Output: 32 * 5 * 5
        )

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(layer2*5*5, hidden),
            nn.ReLU(),
            nn.Linear(hidden, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.convolutions(x)
        logits = self.dense(x)
        return logits
