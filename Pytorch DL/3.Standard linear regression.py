import os
import torch
import torch.nn as nn
from torch import optim

x_data = torch.tensor([[1.0], [2.0], [3.0]])  # 需要是2D张量，形状：[样本数, 特征数]
y_data = torch.tensor([[2.0], [4.0], [6.0]])

class LinearModel(nn.Module):  #把线性模型构造成一个类，继承自nn.Module（nn中的一个基类）
    def __init__(self):
        super(LinearModel,self).__init__()
        #由Linear构造linear对象(实例化）
        self.linear = torch.nn.Linear(1,1)  #这里的Linear也是继承自Module的，可以进行反向传播
        #正向传播
    def forward(self, x):
        y_pred = self.linear(x) #由于Module中有__call__方法，可以让让Module的实例像函数一样可调用。所以linear可以被调用
        return y_pred

model = LinearModel()  #同样的model也是可调用的对象

criterion = nn.MSELoss(reduction='sum')   #损失函数实例化
optimizer = optim.SGD(model.parameters(), lr=0.01)   #优化器 会初始化权重w并更新梯度
#model.parameters()  成员parameters检查父类Module中的所有成员，如果有权重
#训练过程

for epoch in range(100):

    y_pred = model(x_data)
    loss = criterion(y_pred,y_data)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch}, Loss: {loss:.4f}')
print('w=',model.linear.weight.item())
print('b=',model.linear.bias.item())

x_test = torch.Tensor([4.0])
y_test = model(x_test)
print('y_pred=',y_test.data)

