#线性模型穷举法寻找Loss最优的权重w
import numpy as np
import matplotlib.pyplot as plt #导入用于数组计算和绘图的包

# x_data = [1.0,2.0,3.0]
# y_data = [2.0,4.0,6.0]

# def forward(x):
#     return x*w  #python中函数可以访问全局变量，因此函数被调用时，Python在全局作用域中寻找w
#
# def loss(x,y):
#     y_hat = forward(x)
#     return (y-y_hat)**2
#
# w_list = []
# mse_list = []
#
# for w in np.arange(0.0,4.1,0.1):
#     print('w=',w)
#     l_sum = 0
#     for x_val,y_val in zip(x_data,y_data):  #zip() 函数用于将多个可迭代对象（如列表）"打包"成元组序列。
#         # 示例
#         # names = ['Alice', 'Bob', 'Charlie']
#         # ages = [25, 30, 35]
#         #
#         # zipped = zip(names, ages)
#         # print(list(zipped))
#         # 输出: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
#         y_hat_val = forward(x_val)
#         loss_val = loss(x_val,y_val)
#         l_sum += loss_val
#         print('\t',x_val,y_val,y_hat_val,loss_val)
#     print('MSE=',l_sum/len(x_data))
#     w_list.append(w)
#     mse_list.append(l_sum/len(x_data))
# plt.plot(w_list,mse_list)
# plt.xlabel('w')
# plt.ylabel('Loss')
# plt.show()

#2.梯度下降算法找w(只能找到局部最优，很难找到全局最优）
x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

w = 1.0  #初始化w

def forward(x):
    return x*w
#计算w=1时的成本函数cost
def cost(xs,ys):
    cost = 0
    for x,y in zip(xs,ys):
        y_hat = forward(x)
        cost += (y-y_hat)**2
    return cost/len(xs)

#梯度函数
def gradient(xs,ys):
    grad = 0
    for x,y in zip(xs,ys):
        grad += 2*x*(x*w-y)  #这里梯度下降并行计算是指在计算每个样本的梯度时用的w都是同一个w，不会造成计算前面样本的梯度会影响后面样本的梯度计算
    return grad/len(xs)
#选择学习率为0.01的梯度下降算法去训练100次，并输出每次训练后对应的成本函数
print('Predict(before training):',4,forward(4))
epoch_list = []
cost_list = []
for epoch in range(100):
    cost_val = cost(x_data,y_data)
    grad_val = gradient(x_data,y_data)
    w -= 0.01*grad_val
    epoch_list.append(epoch)
    cost_list.append(cost_val)
    print('Epoch:',epoch,'w=',w,'loss=',cost_val)
print('Predict(after training):',4,forward(4))
plt.plot(epoch_list,cost_list)
plt.title('train loss')
plt.xlabel('epoch')
plt.ylabel('cost')
plt.show()

#随机梯度下降，即从全部样本组成的成本函数cost function中随机取出一个样本的损失函数loss，用它去寻找最佳的权重w
#其实就是靠随机噪声的运气去逃离局部最优达到全局最优，多运行几次SGD可能就能找到全局最优点了
x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

w = 1.0  #初始化w

def forward(x):
    return x*w
#计算w=1时的损失函数loss
def loss(x,y):
    y_hat = forward(x)
    loss = (y-y_hat)**2
    return loss

#梯度函数
def gradient(x,y):
    grad = 2*x*(x*w-y)
    return grad
#选择学习率为0.01的梯度下降算法去训练100次，并输出每次训练后对应的成本函数
print('Predict(before training):',4,forward(4))
epoch_list = []
l_list = []
for epoch in range(100):
    for x,y in zip(x_data,y_data):#这里没有随机选择一个样本，而是对每个样本的梯度都进行了更新是为了说明SGD的并行性差，前一个样本更新的梯度会对后面样本梯度更新时造成影响
        grad = gradient(x,y)
        w -= 0.01*grad
        print('\tgrad:',x,y,grad)
        l = loss(x,y)
    print('progress:',epoch,'w=',w,'loss=',l)
print('Predict(after training):',4,forward(4))

#注意到梯度下降时计算每一点的梯度互不影响，但是在随机梯度下降时前面样本更新的w会对后面样本的w产生印象
#梯度下降由于可以并行，时间更快，但是随机梯度下降性能更高，折中产生了mini-batch
#也就是在大数据集时，梯度下降的优点并行计算时间快，但是很难逃离局部最优，用SGD计算时间长，但是容易逃离局部最优达到全局最优，因此分成很多小部分（batch）
#对每一个小部分由于样本量大幅减少，因此对每个batch用使用GD的思想计算平均梯度，同时把每个batch当作all batches中的一个随机样本用SGD一样频繁更新权重

import numpy as np

# 数据准备
X = np.array([[1], [2], [3], [4], [5]])  # 5个样本
y = np.array([[2], [4], [6], [8], [10]])
w = 1.0  # 初始权重
learning_rate = 0.01
batch_size = 2  # 小批量大小


def forward(x):
    return x * w


def loss(y_pred, y_true):
    return (y_pred - y_true) ** 2


def gradient(x, y_true):
    y_pred = forward(x)
    return 2 * x * (y_pred - y_true)


# Mini-batch 训练过程
num_epochs = 100
n_samples = len(X)

for epoch in range(num_epochs):
    # 随机打乱数据
    indices = np.random.permutation(n_samples)
    X_shuffled = X[indices]
    y_shuffled = y[indices]

    total_loss = 0

    # 按batch处理
    for i in range(0, n_samples, batch_size):
        # 获取当前batch
        X_batch = X_shuffled[i:i + batch_size]
        y_batch = y_shuffled[i:i + batch_size]

        # 计算batch的平均梯度
        batch_grad = 0
        batch_loss = 0

        for x, y_true in zip(X_batch, y_batch):
            grad = gradient(x, y_true)
            batch_grad += grad
            batch_loss += loss(forward(x), y_true)

        # 平均梯度
        avg_grad = batch_grad / len(X_batch)
        avg_loss = batch_loss / len(X_batch)
        total_loss += avg_loss

        # 更新权重
        w = w - learning_rate * avg_grad

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {total_loss / (n_samples / batch_size):.4f}')