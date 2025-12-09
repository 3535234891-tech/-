import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import torch

x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

w = torch.tensor([1.0]) #这里的w不是普通的python数字，而是tensor，普通的python数字无法调用后向传播的backward()方法
w.requires_grad_(True)  #默认的tensor不会保留计算的梯度，这一步是记录所有的梯度
#定义前向传播，用前向传播去计算损失函数
def forward(x):
    return w * x  #这里x原本是python数字，但是与tensor型的w相乘，会遵循广播机制也变成tensor型
#计算损失函数
def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y)**2  #同理，y也被x传染成tensor型了，


print("predict (before training)", 4, forward(4).item()) #forward(4).item()会返回tensorforward(4)对应的python数字

# 训练循环
for epoch in range(100):
    for x, y in zip(x_data, y_data):    #利用随机梯度下降
        l = loss(x, y)  # l也变成了tensor型     每调用一次loss，就动态的构建了一次计算图

        # 反向传播
        l.backward()

        # 打印梯度
        print('\tgrad:', x, y, w.grad.item()) #这里由于上一步的反向传播产生了梯度存储在了w.grad中，再利用item转化成了python数字输出

        # 更新权重
        w.data = w.data - 0.01 * w.grad  # 如果直接对w更新权重，会变成新的tensor，丢失梯度跟踪

        # 清零梯度
        w.grad.data.zero_()  #把tensor类型的w中的梯度数据全部清零

    # 打印进度（修正：应该是l.item()）
    print("progress:", epoch, l.item())

print("predict (after training)", 4, forward(4).item())


#神经网络实战

from torch.utils.data import Dataset
import os
import pandas as pd
import numpy as np
import torch

class iris_dataloader(Dataset): #继承父类Dataset，具体实现子类时必须实现下面三个方法
    def __init__(self, data_path): #用于初始化数据集，建立数据集的初始状态，为后续访问做准备
        self.data_path = data_path

        assert os.path.exists(self.data_path),"dataset does not exist"
        #使用pandas的read_csv函数读取CSV文件，得到的数据类型是pandas库独有的DataFrame类型 names=[0,1,2,3,4]表示给数据集的5列分别命名为0,1,2,3,4
        df = pd.read_csv(self.data_path,name = [0,1,2,3,4])
        #创建字典，将字符串标签映射为数字  使用map函数将第4列（标签列）的字符串转换为数字
        d = {"Tris-sector":0,"Tris-versicolor":1,"Tris-virgincia":2}
        df[4] = df[4].map(d)

        data = df.iloc[:,0:3]  #iloc[:, 0:4]表示：所有行，第0到第3列 前4列
        label = df.iloc[:,4:]  #选择第4列作为标签数据（花的种类） 从列索引

        data = (data - np.mean(data)) / np.std(data)  #Z值化，目的是使数据均值为0，标准差为1，加速模型收敛
        self.data = torch.from_numpy(np.array(data,dtype="float32")) #np.array(data, dtype='float32')：将pandas DataFrame转换为numpy数组，指定float32类型
        self.label = torch.from_numpy(np.array(label, dtype="int64")) #torch.from_numpy()：将numpy数组转换为PyTorch张量

        self.data_num = len(label)  #用标签数量表述数据集的大小
        print('当前数据集的大小：',self.data_num)
    def __len__(self):
        return self.data_num

    def __getitem__(self, idx): #提供按索引访问数据的能力
        self.data = list(self.data)
        self.label = list(self.label)
        return self.data[idx], self.label[idx]

#nn.Module构建神经网络模型
import os
import sys
from torch.utils.data import DataLoader
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.optim as optim
from data_loader import iris_dataloader

#初始化神经网络

class NN(nn.Module):
    def __init__(self,in_dim,hidden_dim1,hidden_dim2,out_dim,):
        super(NN, self).__init__()
        self.layer1 = nn.Linear(in_dim,hidden_dim1)
        self.layer2 = nn.Linear(hidden_dim1,hidden_dim2)
        self.layer3 = nn.Linear(hidden_dim2,out_dim)
#前向传播
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
#定义计算环境 三目运算如果if返回true表示gpu环境，false对应cpu
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")#判断cpu环境还是gpu环境
#训练集，验证集和测试集

