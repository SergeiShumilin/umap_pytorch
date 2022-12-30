import torch
import torch.nn as nn

class conv(nn.Module):
    def __init__(self, n_components):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(
                in_channels=1, out_channels=64, kernel_size=3, stride=2, padding=1,
            ),
            nn.Conv2d(
                in_channels=64, out_channels=128, kernel_size=3, stride=2, padding=1,
            ),
            nn.Flatten(),
            nn.Linear(6272, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, n_components)
        ).cuda()
    def __forward__(self, X):
        return self.encoder(X)