import torch
import torch.nn as nn
import torch.nn.functional as F
import data_loader

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 100)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 学習済みモデルのロード
net = Net()
net.load_state_dict(torch.load('trained_model.pth'))
net.eval()

def predict(image_array):
    with torch.no_grad():
        output = net(torch.tensor(image_array).float())
        _, predicted = torch.max(output.data, 1)
        score = torch.softmax(output, dim=1)[0, predicted].item()
        
    return predicted.item(), score