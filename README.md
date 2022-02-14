## Pytorch 对抗训练 + 中文文本分类 

## 介绍
基于Pytorch实现的中文文本分类器与对抗训练功能（即插即用）。模型和对抗训练容易调用与调试。

数据以字为单位输入模型，预训练词向量使用 [搜狗新闻 Word+Character 300d](https://github.com/Embedding/Chinese-Word-Vectors)，[点这里下载](https://pan.baidu.com/s/14k-9jsspp43ZhMxqPmsWMQ)  

## Enviroment
python 3.7  
pytorch 1.1  
tqdm  
sklearn  
tensorboardX

## 代码结构
```
adversarial: FGSM, FREE, PGD 类定义，攻击，还原功能
models: 模型定义及模型参数配置
run.py: 程序运行Main()
train_eval.py：初始化网络，模型实际训练，测试，评估
utils.py: 数据集处理
```

## 模型和数据集
分类器和数据实现基于（https://github.com/649453932/Chinese-Text-Classification-Pytorch）

### 分类器
TextCNN，TextRNN，FastText，TextRCNN，BiLSTM_Attention, DPCNN, Transformer

### 对抗训练
FGSM, PGD, FREE

### 数据集介绍
[THUCNews](http://thuctc.thunlp.org/)中抽取了20万条新闻标题，已上传至github，文本长度在20到30之间。一共10个类别，每类2万条。

类别：财经、房产、股票、教育、科技、社会、时政、体育、游戏、娱乐。

数据集划分：

数据集|数据量
--|--
训练集|18万
验证集|1万
测试集|1万


### 更换自己的数据集
 - 如果用字，按照我数据集的格式来格式化你的数据。  
 - 如果用词，提前分好词，词之间用空格隔开，`python run.py --model TextCNN --word True`  
 - 使用预训练词向量：utils.py的main函数可以提取词表对应的预训练词向量。  

## 训练效果
模型|PRECISION|RECALL|F1|Time|备注
--|--|--|--|--|--
TextCNN|0.9064|0.9061|0.9060|5:17:01|Baseline *note: this training is done under different GPU
TextCNN+FGSM|0.9085|0.9078|0.9079|1:10:42|Training with FGSM
TextCNN+PGD|0.9170|0.9169|0.9168|3:24:00|Training with PGD
TextCNN+FREE|0.9094|0.9086|0.9088|2:45:00|Training with FREE

### 参数
TextCNN超参数在每个实验中保持一致。详情见TextCNN.py class Config

## 使用说明
```
# 训练并测试(无对抗训练)：
# TextCNN
python run.py --model TextCNN

# 训练并测试(对有抗训练)：
# TextCNN + FGSM
python run.py --model TextCNN --adversarial FGSM

# TextCNN + PGD
python run.py --model TextCNN --adversarial PGD

# TextCNN + FREE
python run.py --model TextCNN --adversarial FREE
```

## Reference
[1] Convolutional Neural Networks for Sentence Classification  
[2] Recurrent Neural Network for Text Classification with Multi-Task Learning  
[3] Attention-Based Bidirectional Long Short-Term Memory Networks for Relation Classification  
[4] Recurrent Convolutional Neural Networks for Text Classification  
[5] Bag of Tricks for Efficient Text Classification  
[6] Deep Pyramid Convolutional Neural Networks for Text Categorization  
[7] Attention Is All You Need
[8] Fast is better than free: Revisiting adversarial training
[9] https://github.com/locuslab/fast_adversarial 
[10] https://github.com/649453932/Chinese-Text-Classification-Pytorch


