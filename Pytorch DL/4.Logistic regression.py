#数据集的加载
# import torchvision
#
# train_set = torchvision.datasets.MNIST(root='classification dataset', train=True,  download=True)
# test_set = torchvision.datasets.MNIST(root='classification dataset', train=False, download=True)

#导入神经网络模板
#
# import torch
# import torch.nn as nn
# from torch import optim
# import torch.nn.functional as F
#
# x_data = torch.Tensor([[1.0], [2.0], [3.0]])  # 需要是2D张量，形状：[样本数, 特征数]
# y_data = torch.Tensor([[0], [0], [1]])
#
# class LogisticRegressionModel(nn.Module):  #把线性模型构造成一个类，继承自nn.Module（nn中的一个基类）
#     def __init__(self):
#         super(LogisticRegressionModel,self).__init__()
#         #由Linear构造linear对象(实例化）
#         self.linear = torch.nn.Linear(1,1)  #这里的Linear也是继承自Module的，可以进行反向传播
#         #正向传播
#     def forward(self, x):
#         y_pred = F.sigmoid(self.linear(x) )#由于Module中有__call__方法，可以让让Module的实例像函数一样可调用。所以linear可以被调用
#         return y_pred
# model = LogisticRegressionModel()
# #逻辑回归的损失函数
# criterion = torch.nn.BCELoss(reduction="sum")
# optimizer = optim.SGD(model.parameters(), lr=0.01)
#
# for epoch in range(500):
#     y_pred = model(x_data)
#     loss = criterion(y_pred,y_data)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#     print(f'Epoch {epoch}, Loss: {loss:.4f}')
# print('w=',model.linear.weight.item())
# print('b=',model.linear.bias.item())
#
# x_test = torch.Tensor([4.0])
# y_test = model(x_test)
# print('y_pred=',y_test.data)

#多维输入的情况
# import torch
# import torch.nn as nn
# from torch import optim
# import torch.nn.functional as F
# import numpy as np
# xy = np.loadtxt('diabetes.csv.gz', delimiter=',', dtype=np.float32)
# x_data = torch.from_numpy(xy[:,:-1])
# y_data = torch.from_numpy(xy[:, -1].reshape(-1, 1)).float()#中括号表示拿出来是个矩阵而非向量
#
# class LogisticRegressionModel_mul_dim(nn.Module):  #把线性模型构造成一个类，继承自nn.Module（nn中的一个基类）
#     def __init__(self):
#         super(LogisticRegressionModel_mul_dim,self).__init__()
#         #由Linear构造linear对象(实例化）
#         self.linear1 = torch.nn.Linear(8,6)
#         self.linear2 = torch.nn.Linear(6,4)
#         self.linear3 = torch.nn.Linear(4,1)#这里的Linear也是继承自Module的，可以进行反向传播
#         self.sigmoid = torch.nn.Sigmoid()
#         #正向传播
#     def forward(self, x):
#         x = self.sigmoid(self.linear1(x))
#         x = self.sigmoid(self.linear2(x))
#         x = self.sigmoid(self.linear3(x))#由于Module中有__call__方法，可以让让Module的实例像函数一样可调用。所以linear可以被调用
#
#         return x
# model = LogisticRegressionModel_mul_dim()
#
# criterion = torch.nn.BCELoss(reduction="sum")
# optimizer = optim.SGD(model.parameters(), lr=0.01)
#
# for epoch in range(1000):
#     #前馈
#     y_pred = model(x_data)
#     loss = criterion(y_pred,y_data)
#     print(f'Epoch {epoch}, Loss: {loss:.4f}')
#     #反向传播
#     optimizer.zero_grad()
#     loss.backward()
#     #更新
#     optimizer.step()
# x_test = torch.Tensor([[-0.882353,-0.145729,0.0819672,-0.414141,0,-0.207153,-0.766866,-0.666667]])
#     # 这是一个包含 8 个特征的列表，作为 Tensor 的第一行（第 1 个样本）
#
# y_test = model(x_test)
# print('y_pred=',y_test.data)

# ##  mini-batch处理多维输入的逻辑回归
#step1 准备数据集
import torch
import numpy as np
import torch.nn as nn
from torch import optim
from torch.utils.data import Dataset,DataLoader #Dataset是抽象类，无法实例化，只能被继承
#Dataloader将dataset (shuffle后)封装成大小为batch_size的iteriation个batch

class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]  #xy是n行9列，所以shape[0]是样本数量n
        self.x_data = torch.from_numpy(xy[:, :-1])
        self.y_data = torch.from_numpy(xy[:, -1].reshape(-1, 1)).float()
    def __len__(self):
        return self.len
    def __getitem__(self, idx):
        return self.x_data[idx],self.y_data[idx]

dataset = DiabetesDataset('diabetes.csv.gz')
train_loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)
#num_workers是选择读取数据时用多少的GPU并行多线程

#step2 设计模型
class Model(nn.Module):  # 把线性模型构造成一个类，继承自nn.Module（nn中的一个基类）
    def __init__(self):
        super(Model, self).__init__()
        # 由Linear构造linear对象(实例化）
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)  # 这里的Linear也是继承自Module的，可以进行反向传播
        self.sigmoid = torch.nn.Sigmoid()
        # 正向传播
    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))  # 由于Module中有__call__方法，可以让让Module的实例像函数一样可调用。所以linear可以被调用
        return x
model = Model()

#step3 损失函数和优化器
criterion = torch.nn.BCELoss(reduction="sum")
optimizer = optim.SGD(model.parameters(), lr=0.01)

#step4 训练过程
if __name__ == '__main__':
    for epoch in range(50):
        for i,(X,Y) in enumerate(train_loader,0): #enumerate  是获得迭代次数
            y_pred = model(X)
            loss = criterion(y_pred, Y)
            print(f'Epoch {epoch}, Loss: {loss:.4f}')
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    #step5 测试集  这里的测试集代码要与第一个for循环对齐！！！！！
    print("--- 训练完成，开始测试集预测！ ---")
    x_test = torch.Tensor([-0.882353,-0.145729,0.0819672,-0.414141,0,-0.207153,-0.766866,-0.666667])
    y_test = model(x_test)
    print('y_test_pred=',y_test.data)