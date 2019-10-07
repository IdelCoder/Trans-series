# Trans-series
本仓库代码是毕业论文《基于实体聚合与正例约束的知识库链接预测研究》的代码。部分算法以及基本框架参考了[**thunlp/TensorFlow-TransX**](https://github.com/thunlp/TensorFlow-TransX),以及[**thunlp/KB2E**](https://github.com/thunlp/KB2E)
## 链接预测
以TransE为例，执行./TransE/transE.py文件
* 在执行前，设置标志位，进行训练
```
class Config(object):
  def __init__(self):
    ...
    self.testFlag = False
    self.loadFromData = False
    ...
```
* 执行后，设置标志位，进行测试
```
class Config(object):
  def __init__(self):
    ...
    self.testFlag = True
    self.loadFromData = True
    ...
```
* PTransE的实现在另一个仓库中[**IdelCoder/PTransE-ag**](https://github.com/IdelCoder/PTransE-ag)。那个仓库中会有使用说明。
## 三元组分类
在./TransE/transE.py中，有三元组分类的示例
* 在执行前，设置标志位，进行训练
```
class Config(object):
  def __init__(self):
    ...
    self.testFlag = False
    self.loadFromData = False
    self.tripleClassification = True
    ...
```
* 执行后，设置标志位，用于验证三元组分类
```
class Config(object):
  def __init__(self):
    ...
    self.testFlag = True
    self.loadFromData = True
    self.tripleClassification = True
    ...
```
## 数据说明
* ./data/wn11和./data/fb13是处理过的数据，用来训练模型。./data/test是用来验证和测试的数据
* ./data/mappingdegree.py用来生成TransM的关系权重。./data/sparse.py用于TranSparse
