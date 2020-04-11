import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from fashionMNIST_cnn import simpleNet

model = simpleNet()
model.load_state_dict(torch.load('fashionMNIST_cnn_model.pth'))
model.eval()