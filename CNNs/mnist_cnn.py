#Dependencies
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torchvision.datasets as datasets
import torchvision.transforms as transforms #PyTorch

#Checks for CUDA usage
def get_variable(input):
    x = Variable(input)
    if torch.cuda.is_available():
        x = x.cuda()
    return x

#Generates the MNIST Dataset
def generate_dataset():

    #Load MNIST Training Set
    train_sets = datasets.MNIST(root='./MNIST', train=True,
    transform=transforms.ToTensor(), download=True)

    #Load MNIST Test Set
    test_sets = datasets.MNIST (root='./MNIST', train=False,
    transform=transforms.ToTensor(), download=True)
    return train_sets, test_sets

#Establishes CNN class
class MNIST_CNN(nn.Module):

    def __init__(self):
        super(MNIST_CNN, self).__init__()

        #Define convoluted layers
        self.conv1 = nn.Conv2d(1, 10, kernel_size = 5)   
        self.conv2 = nn.Conv2d(10, 20, kernel_size = 5) 
        self.conv2_drop = nn.Dropout2d()

        #Define fully connected linear layers
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10) #output = 10 because 0-9

    # All dimensions except the batch dimension
    def num_flat_features(self, s):
        size = s.size()[1:]  
        num_features = 1
        for x in size:
            num_features *= x
        return num_features

    #Feedforward the layers
    def forward(self, s):

        #Convoluted
        s = F.relu(F.max_pool2d(self.conv1(s),2))
        s = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(s)), 2))

        #Reshapes the tensor
        s = s.view(-1, self.num_flat_features(s))

        #Fully connected linear
        s = F.relu(self.fc1(s))
        s = F.dropout(s, training = self.training)
        s = self.fc2(s)
        return F.log_softmax(s, dim = 1) #softmax

#Main function
def main():

    #Define training data information
    epoch_times = 20
    learning_rate = 0.0001
    batch_size = 32

    #Instantiate CNN
    mnist_cnn = MNIST_CNN()

    #Checks for CUDA on system
    if torch.cuda.is_available():
        mnist_cnn = mnist_cnn.cuda()

    #Fefining both the loss function, and the optimizer
    loss_func = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(mnist_cnn.parameters(), lr=learning_rate)

    #Generate the MNIST dataset for train and test
    train_sets, test_sets = generate_dataset()

    #Load the data for both train and test
    train_loader = torch.utils.data.DataLoader(dataset=train_sets,
    batch_size=batch_size, shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=test_sets,
    batch_size=10, shuffle=True)

    #Actually training the data
    for epoch in range(epoch_times):
        sum_train_loss = 0
        sum_validation_loss = 0
        
        #gets images and labels and tests 
        mnist_cnn.train()
        for images, labels in train_loader:
            images = get_variable(images)
            labels = get_variable(labels)
            outputs = mnist_cnn(images)
            train_loss = loss_func(outputs, labels)
            sum_train_loss += train_loss.data
            optimizer.zero_grad()
            train_loss.backward()
            optimizer.step()
      
        #Evaluates CNN by epoch, loss, etc.
        mnist_cnn.eval()
        for images, labels in test_loader:
            images = get_variable(images)
            labels = get_variable(labels)
            outputs = mnist_cnn(images)
            validation_loss = loss_func(outputs, labels)
            sum_validation_loss += validation_loss.data
        print('Epoch [%d/%d], TrainLoss: %.4f ValidationLoss: %.4f'
              % (epoch + 1, epoch_times, sum_train_loss, sum_validation_loss))

    #Evaluates CNN of #wrong, right, precision, etc.
    mnist_cnn.eval()
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = get_variable(images)
        labels = get_variable(labels)
        outputs = mnist_cnn(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels.data).sum()

    print('Total: %d, Correct: %d Wrong: %d' % (total, correct, total - correct))
    print('precision: %.4f %%' % (100 * float(correct) / float(total)))

    #saves the model
    torch.save(mnist_cnn, 'mnist_cnn_model.pth')

if __name__ == "__main__":
    main()
