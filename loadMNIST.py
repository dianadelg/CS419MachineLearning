import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from mnist_cnn import MNIST_CNN

model = MNIST_CNN()
torch.load('mnist_cnn_model.pth')
model.eval()