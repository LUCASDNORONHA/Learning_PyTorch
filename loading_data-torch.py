import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

# Carregando o conjunto de dados MNIST
training_data = datasets.MNIST(root='.', train=False, download=True, transform=ToTensor())
test_data = datasets.MNIST(root=".", train=False, download=True, transform=ToTensor())

# Imprimindo os primeiro indice do conjunto de dados
print('-'*50)
print(training_data[0])
print('-'*50)

# representando os dados em forma de imagem
figure = plt.figure(figsize=(8, 8))
cols, rows = 5, 5

for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1, )). item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.axis('off')
    plt.imshow(img.squeeze(), cmap='gray')
plt.show()

# Imprimindo as classes
print(training_data.classes)

# Dividindo os dados

loaded_train = DataLoader(training_data, batch_size=64, shuffle=True)
loaded_test = DataLoader(test_data, batch_size=64, shuffle=True)