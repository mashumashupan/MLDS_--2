import torch
from torchvision import datasets, transforms

def load_data(download=True):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    trainset = datasets.CIFAR100(root='./data', train=True,
                                 download=download, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                              shuffle=True, num_workers=2)

    testset = datasets.CIFAR100(root='./data', train=False,
                                download=download, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                             shuffle=False, num_workers=2)
    
    return trainloader, testloader

def download_data():
    datasets.CIFAR100(root='./data', train=True, download=True)
    datasets.CIFAR100(root='./data', train=False, download=True)