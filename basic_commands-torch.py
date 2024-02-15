import torch
import numpy as np

# Instaciando um tensor de um array
ndarray = np.array([0, 1, 2])
t = torch.from_numpy(ndarray)

print('-'*50)
print(t)

# Imprimindo os atributos do tensor
print('-'*50)
print(t.shape)
print(t.dtype)
print(t.device)
print('-'*50)

# Intanciando um tensor de um lista
t = torch.tensor([0, 1, 2])
print(t)
print('-'*50) 

# Tensor pode ser multidimensional
ndarray = np.array([[0, 1, 2], [3, 4, 5]])
t = torch.from_numpy(ndarray)
print(t)
print('-'*50) 


# Criando um tensor a partir de outro tensor
new_t = torch.rand_like(t, dtype=torch.float)
print(new_t)
print('-'*50) 

# Criando um um tensor com o um shape predefinido por mim
my_shape = (3, 3)
rand_t = torch.rand(my_shape)
print(rand_t)
print('-'*50)

# Fatiamento de um tensor
zeros_tensor = torch.zeros((2, 3))
print(zeros_tensor)
print('-'*50)

# acessando um índice de um tensor pela coluna ou linha
print(zeros_tensor[1])
print(zeros_tensor[:, 0])
print('-'*50)

# Transposição de um tensor
transposed = zeros_tensor.T
print(transposed)
print('-'*50)

# Multiplição entre tensores
ones_tensor = torch.ones(3, 3)
product = torch.matmul(zeros_tensor, ones_tensor)
print(product)
print('-'*50)
