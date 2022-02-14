# %python run.py --model TextCNN
```
Loading data...
Vocab size: 4762
180000it [00:03, 53634.09it/s]
10000it [00:00, 27481.99it/s]
10000it [00:00, 28616.15it/s]
Time usage: 0:00:04
<bound method Module.parameters of Model(
  (embedding): Embedding(4762, 300)
  (convs): ModuleList(
    (0): Conv2d(1, 256, kernel_size=(2, 300), stride=(1, 1))
    (1): Conv2d(1, 256, kernel_size=(3, 300), stride=(1, 1))
    (2): Conv2d(1, 256, kernel_size=(4, 300), stride=(1, 1))
  )
  (dropout): Dropout(p=0.5, inplace=False)
  (fc): Linear(in_features=768, out_features=10, bias=True)
)>
Epoch [1/20]
Iter:      0,  Train Loss:   2.3,  Train Acc:  8.59%,  Val Loss:   2.7,  Val Acc: 17.20%,  Time: 0:00:06 *
Iter:    100,  Train Loss:  0.75,  Train Acc: 72.66%,  Val Loss:  0.69,  Val Acc: 78.24%,  Time: 0:07:28 *
Iter:    200,  Train Loss:  0.72,  Train Acc: 78.91%,  Val Loss:  0.55,  Val Acc: 83.16%,  Time: 0:14:50 *
Iter:    300,  Train Loss:  0.46,  Train Acc: 85.16%,  Val Loss:  0.49,  Val Acc: 84.68%,  Time: 0:22:13 *
Iter:    400,  Train Loss:  0.72,  Train Acc: 78.91%,  Val Loss:  0.47,  Val Acc: 85.47%,  Time: 0:29:35 *
Iter:    500,  Train Loss:  0.35,  Train Acc: 90.62%,  Val Loss:  0.44,  Val Acc: 86.25%,  Time: 0:36:57 *
Iter:    600,  Train Loss:  0.52,  Train Acc: 85.16%,  Val Loss:  0.42,  Val Acc: 86.87%,  Time: 0:44:20 *
Iter:    700,  Train Loss:  0.46,  Train Acc: 84.38%,  Val Loss:   0.4,  Val Acc: 87.42%,  Time: 0:51:42 *
Iter:    800,  Train Loss:  0.49,  Train Acc: 85.94%,  Val Loss:  0.39,  Val Acc: 87.66%,  Time: 0:59:04 *
Iter:    900,  Train Loss:  0.44,  Train Acc: 86.72%,  Val Loss:  0.39,  Val Acc: 88.09%,  Time: 1:06:27 *
Iter:   1000,  Train Loss:  0.32,  Train Acc: 90.62%,  Val Loss:  0.39,  Val Acc: 88.03%,  Time: 1:13:49 
Iter:   1100,  Train Loss:   0.4,  Train Acc: 88.28%,  Val Loss:  0.38,  Val Acc: 88.19%,  Time: 1:21:11 *
Iter:   1200,  Train Loss:  0.41,  Train Acc: 85.16%,  Val Loss:  0.37,  Val Acc: 88.95%,  Time: 1:28:34 *
Iter:   1300,  Train Loss:   0.4,  Train Acc: 85.94%,  Val Loss:  0.36,  Val Acc: 88.93%,  Time: 1:35:56 *
Iter:   1400,  Train Loss:  0.46,  Train Acc: 86.72%,  Val Loss:  0.36,  Val Acc: 88.96%,  Time: 1:43:18 *
Epoch [2/20]
Iter:   1500,  Train Loss:  0.39,  Train Acc: 87.50%,  Val Loss:  0.35,  Val Acc: 89.11%,  Time: 1:50:38 *
Iter:   1600,  Train Loss:  0.32,  Train Acc: 89.06%,  Val Loss:  0.35,  Val Acc: 88.93%,  Time: 1:58:01 
Iter:   1700,  Train Loss:  0.33,  Train Acc: 88.28%,  Val Loss:  0.35,  Val Acc: 89.09%,  Time: 2:05:23 
Iter:   1800,  Train Loss:  0.29,  Train Acc: 89.84%,  Val Loss:  0.35,  Val Acc: 88.94%,  Time: 2:12:45 *
Iter:   1900,  Train Loss:  0.37,  Train Acc: 85.94%,  Val Loss:  0.34,  Val Acc: 89.32%,  Time: 2:20:08 *
Iter:   2000,  Train Loss:  0.35,  Train Acc: 89.06%,  Val Loss:  0.34,  Val Acc: 89.47%,  Time: 2:27:30 *
Iter:   2100,  Train Loss:  0.42,  Train Acc: 88.28%,  Val Loss:  0.34,  Val Acc: 89.67%,  Time: 2:34:52 *
Iter:   2200,  Train Loss:  0.33,  Train Acc: 89.06%,  Val Loss:  0.34,  Val Acc: 89.46%,  Time: 2:42:14 
Iter:   2300,  Train Loss:  0.36,  Train Acc: 92.97%,  Val Loss:  0.34,  Val Acc: 89.63%,  Time: 2:49:37 
Iter:   2400,  Train Loss:  0.32,  Train Acc: 88.28%,  Val Loss:  0.35,  Val Acc: 89.50%,  Time: 2:56:59 
Iter:   2500,  Train Loss:  0.18,  Train Acc: 93.75%,  Val Loss:  0.33,  Val Acc: 90.06%,  Time: 3:04:21 *
Iter:   2600,  Train Loss:  0.32,  Train Acc: 92.19%,  Val Loss:  0.33,  Val Acc: 90.23%,  Time: 3:11:44 *
Iter:   2700,  Train Loss:  0.26,  Train Acc: 88.28%,  Val Loss:  0.33,  Val Acc: 89.79%,  Time: 3:19:06 
Iter:   2800,  Train Loss:  0.32,  Train Acc: 91.41%,  Val Loss:  0.33,  Val Acc: 89.76%,  Time: 3:26:29 
Epoch [3/20]
Iter:   2900,  Train Loss:  0.36,  Train Acc: 88.28%,  Val Loss:  0.33,  Val Acc: 89.84%,  Time: 3:33:49 
Iter:   3000,  Train Loss:  0.22,  Train Acc: 94.53%,  Val Loss:  0.33,  Val Acc: 89.82%,  Time: 3:41:11 *
Iter:   3100,  Train Loss:  0.27,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 89.71%,  Time: 3:48:34 
Iter:   3200,  Train Loss:  0.39,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 89.85%,  Time: 3:55:56 
Iter:   3300,  Train Loss:  0.35,  Train Acc: 87.50%,  Val Loss:  0.32,  Val Acc: 90.05%,  Time: 4:03:19 *
Iter:   3400,  Train Loss:  0.31,  Train Acc: 89.84%,  Val Loss:  0.33,  Val Acc: 90.04%,  Time: 4:10:41 
Iter:   3500,  Train Loss:  0.18,  Train Acc: 95.31%,  Val Loss:  0.33,  Val Acc: 90.12%,  Time: 4:18:04 
Iter:   3600,  Train Loss:  0.19,  Train Acc: 96.09%,  Val Loss:  0.33,  Val Acc: 89.98%,  Time: 4:25:26 
Iter:   3700,  Train Loss:  0.38,  Train Acc: 87.50%,  Val Loss:  0.32,  Val Acc: 90.31%,  Time: 4:32:48 
Iter:   3800,  Train Loss:  0.32,  Train Acc: 88.28%,  Val Loss:  0.33,  Val Acc: 90.24%,  Time: 4:40:11 
Iter:   3900,  Train Loss:  0.33,  Train Acc: 85.94%,  Val Loss:  0.33,  Val Acc: 89.97%,  Time: 4:47:33 
Iter:   4000,  Train Loss:  0.22,  Train Acc: 93.75%,  Val Loss:  0.33,  Val Acc: 90.26%,  Time: 4:54:56 
Iter:   4100,  Train Loss:  0.18,  Train Acc: 92.97%,  Val Loss:  0.33,  Val Acc: 90.11%,  Time: 5:02:18 
Iter:   4200,  Train Loss:   0.3,  Train Acc: 92.19%,  Val Loss:  0.33,  Val Acc: 89.88%,  Time: 5:09:40 
Epoch [4/20]
Iter:   4300,  Train Loss:  0.24,  Train Acc: 91.41%,  Val Loss:  0.33,  Val Acc: 89.62%,  Time: 5:17:01 
No optimization for a long time, auto-stopping...
Test Loss:  0.31,  Test Acc: 90.61%
Precision, Recall and F1-Score...
               precision    recall  f1-score   support

      finance     0.9280    0.8770    0.9018      1000
       realty     0.9067    0.9430    0.9245      1000
       stocks     0.8595    0.8500    0.8547      1000
    education     0.9561    0.9580    0.9570      1000
      science     0.8364    0.8740    0.8548      1000
      society     0.8991    0.9090    0.9040      1000
     politics     0.9086    0.8550    0.8810      1000
       sports     0.9405    0.9640    0.9521      1000
         game     0.9164    0.9100    0.9132      1000
entertainment     0.9128    0.9210    0.9169      1000

     accuracy                         0.9061     10000
    macro avg     0.9064    0.9061    0.9060     10000
 weighted avg     0.9064    0.9061    0.9060     10000

Confusion Matrix...
[[877  19  61   2  15   7   7   7   2   3]
 [ 10 943   8   0   7  10   7   2   4   9]
 [ 38  25 850   4  41   2  26   4   8   2]
 [  0   2   1 958   9   7   6   3   1  13]
 [  0   7  25   4 874  17  16   4  37  16]
 [  5  23   2  15   9 909  17   4   3  13]
 [  9  12  31   8  26  40 855   9   1   9]
 [  1   1   3   1   3   8   2 964   4  13]
 [  2   1   7   3  48   3   3  13 910  10]
 [  3   7   1   7  13   8   2  15  23 921]]
Time usage: 0:00:01
```

# %python run.py --model TextCNN --adversarial FGSM
```
Loading data...
Vocab size: 4762
180000it [00:02, 62270.22it/s]
10000it [00:00, 67685.54it/s]
10000it [00:00, 66740.14it/s]
Time usage: 0:00:03
<bound method Module.parameters of Model(
  (embedding): Embedding(4762, 300)
  (convs): ModuleList(
    (0): Conv2d(1, 256, kernel_size=(2, 300), stride=(1, 1))
    (1): Conv2d(1, 256, kernel_size=(3, 300), stride=(1, 1))
    (2): Conv2d(1, 256, kernel_size=(4, 300), stride=(1, 1))
  )
  (dropout): Dropout(p=0.5, inplace=False)
  (fc): Linear(in_features=768, out_features=10, bias=True)
)>
Epoch [1/20]
Iter:      0,  Train Loss:   2.3,  Train Acc:  7.03%,  Val Loss:   2.7,  Val Acc: 10.78%,  Time: 0:00:16 *
Iter:    100,  Train Loss:  0.76,  Train Acc: 75.00%,  Val Loss:  0.67,  Val Acc: 78.64%,  Time: 0:02:10 *
Iter:    200,  Train Loss:  0.66,  Train Acc: 78.12%,  Val Loss:  0.54,  Val Acc: 83.63%,  Time: 0:04:02 *
Iter:    300,  Train Loss:  0.49,  Train Acc: 83.59%,  Val Loss:  0.48,  Val Acc: 84.86%,  Time: 0:06:15 *
Iter:    400,  Train Loss:  0.66,  Train Acc: 79.69%,  Val Loss:  0.46,  Val Acc: 85.97%,  Time: 0:08:20 *
Iter:    500,  Train Loss:  0.35,  Train Acc: 87.50%,  Val Loss:  0.42,  Val Acc: 86.96%,  Time: 0:10:29 *
Iter:    600,  Train Loss:  0.53,  Train Acc: 85.94%,  Val Loss:  0.41,  Val Acc: 87.02%,  Time: 0:12:44 *
Iter:    700,  Train Loss:  0.46,  Train Acc: 82.81%,  Val Loss:  0.39,  Val Acc: 87.89%,  Time: 0:14:55 *
Iter:    800,  Train Loss:  0.41,  Train Acc: 88.28%,  Val Loss:  0.38,  Val Acc: 88.56%,  Time: 0:16:51 *
Iter:    900,  Train Loss:   0.4,  Train Acc: 89.06%,  Val Loss:  0.37,  Val Acc: 88.80%,  Time: 0:18:48 *
Iter:   1000,  Train Loss:   0.3,  Train Acc: 89.84%,  Val Loss:  0.38,  Val Acc: 88.45%,  Time: 0:20:41 
Iter:   1100,  Train Loss:  0.41,  Train Acc: 91.41%,  Val Loss:  0.38,  Val Acc: 88.25%,  Time: 0:22:45 
Iter:   1200,  Train Loss:  0.32,  Train Acc: 89.84%,  Val Loss:  0.35,  Val Acc: 89.48%,  Time: 0:24:38 *
Iter:   1300,  Train Loss:  0.41,  Train Acc: 86.72%,  Val Loss:  0.35,  Val Acc: 89.31%,  Time: 0:26:35 *
Iter:   1400,  Train Loss:  0.47,  Train Acc: 83.59%,  Val Loss:  0.35,  Val Acc: 89.21%,  Time: 0:28:18 *
Epoch [2/20]
Iter:   1500,  Train Loss:  0.35,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 89.23%,  Time: 0:30:05 *
Iter:   1600,  Train Loss:  0.27,  Train Acc: 92.19%,  Val Loss:  0.34,  Val Acc: 89.56%,  Time: 0:31:57 *
Iter:   1700,  Train Loss:  0.35,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 89.84%,  Time: 0:33:41 *
Iter:   1800,  Train Loss:  0.31,  Train Acc: 92.97%,  Val Loss:  0.35,  Val Acc: 89.36%,  Time: 0:35:25 
Iter:   1900,  Train Loss:  0.38,  Train Acc: 91.41%,  Val Loss:  0.33,  Val Acc: 89.86%,  Time: 0:37:07 *
Iter:   2000,  Train Loss:  0.26,  Train Acc: 89.06%,  Val Loss:  0.34,  Val Acc: 89.51%,  Time: 0:38:48 
Iter:   2100,  Train Loss:   0.4,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 89.75%,  Time: 0:40:29 
Iter:   2200,  Train Loss:  0.27,  Train Acc: 89.84%,  Val Loss:  0.33,  Val Acc: 89.48%,  Time: 0:42:09 
Iter:   2300,  Train Loss:  0.29,  Train Acc: 92.97%,  Val Loss:  0.33,  Val Acc: 89.77%,  Time: 0:43:50 *
Iter:   2400,  Train Loss:  0.24,  Train Acc: 92.97%,  Val Loss:  0.33,  Val Acc: 89.91%,  Time: 0:45:32 *
Iter:   2500,  Train Loss:  0.17,  Train Acc: 95.31%,  Val Loss:  0.32,  Val Acc: 90.25%,  Time: 0:47:12 *
Iter:   2600,  Train Loss:  0.35,  Train Acc: 88.28%,  Val Loss:  0.32,  Val Acc: 90.35%,  Time: 0:48:53 *
Iter:   2700,  Train Loss:  0.26,  Train Acc: 89.84%,  Val Loss:  0.32,  Val Acc: 90.04%,  Time: 0:50:33 
Iter:   2800,  Train Loss:  0.36,  Train Acc: 89.06%,  Val Loss:  0.32,  Val Acc: 90.09%,  Time: 0:52:15 
Epoch [3/20]
Iter:   2900,  Train Loss:  0.33,  Train Acc: 89.06%,  Val Loss:  0.32,  Val Acc: 90.34%,  Time: 0:53:54 *
Iter:   3000,  Train Loss:  0.21,  Train Acc: 95.31%,  Val Loss:  0.32,  Val Acc: 90.03%,  Time: 0:55:35 
Iter:   3100,  Train Loss:  0.23,  Train Acc: 93.75%,  Val Loss:  0.33,  Val Acc: 89.95%,  Time: 0:57:16 
Iter:   3200,  Train Loss:  0.32,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 90.14%,  Time: 0:58:57 
Iter:   3300,  Train Loss:  0.26,  Train Acc: 89.84%,  Val Loss:  0.32,  Val Acc: 90.00%,  Time: 1:00:38 
Iter:   3400,  Train Loss:  0.24,  Train Acc: 92.19%,  Val Loss:  0.32,  Val Acc: 90.30%,  Time: 1:02:18 
Iter:   3500,  Train Loss:  0.17,  Train Acc: 95.31%,  Val Loss:  0.33,  Val Acc: 89.94%,  Time: 1:03:59 
Iter:   3600,  Train Loss:  0.13,  Train Acc: 96.88%,  Val Loss:  0.32,  Val Acc: 90.15%,  Time: 1:05:40 
Iter:   3700,  Train Loss:  0.29,  Train Acc: 87.50%,  Val Loss:  0.32,  Val Acc: 90.25%,  Time: 1:07:22 
Iter:   3800,  Train Loss:  0.27,  Train Acc: 89.06%,  Val Loss:  0.33,  Val Acc: 90.21%,  Time: 1:09:02 
Iter:   3900,  Train Loss:  0.29,  Train Acc: 87.50%,  Val Loss:  0.32,  Val Acc: 90.31%,  Time: 1:10:42 
No optimization for a long time, auto-stopping...
Test Loss:   0.3,  Test Acc: 90.78%
Precision, Recall and F1-Score...
               precision    recall  f1-score   support

      finance     0.9340    0.8630    0.8971      1000
       realty     0.9320    0.9180    0.9249      1000
       stocks     0.8547    0.8650    0.8598      1000
    education     0.9586    0.9500    0.9543      1000
      science     0.8531    0.8710    0.8619      1000
      society     0.8717    0.9240    0.8971      1000
     politics     0.9095    0.8840    0.8966      1000
       sports     0.9457    0.9570    0.9513      1000
         game     0.9252    0.9150    0.9201      1000
entertainment     0.9004    0.9310    0.9154      1000

     accuracy                         0.9078     10000
    macro avg     0.9085    0.9078    0.9079     10000
 weighted avg     0.9085    0.9078    0.9079     10000

Confusion Matrix...
[[863  16  61   5  11  15  12   9   3   5]
 [ 10 918  18   1   9  16   8   4   3  13]
 [ 39  17 865   2  33   4  27   4   6   3]
 [  0   2   1 950   6  17   6   4   1  13]
 [  1   6  28   5 871  17  14   3  33  22]
 [  3  16   3  14  13 924  16   0   3   8]
 [  5   4  25   4  19  40 884   5   2  12]
 [  1   1   2   1   5  11   2 957   4  16]
 [  1   0   7   4  43   7   2  10 915  11]
 [  1   5   2   5  11   9   1  16  19 931]]
Time usage: 0:00:14
```

# %python run.py --model TextCNN --adversarial PGD
```
Loading data...
Vocab size: 4762
180000it [00:03, 46928.92it/s]
10000it [00:00, 64075.87it/s]
10000it [00:00, 60260.22it/s]
Time usage: 0:00:04
<bound method Module.parameters of Model(
  (embedding): Embedding(4762, 300)
  (convs): ModuleList(
    (0): Conv2d(1, 256, kernel_size=(2, 300), stride=(1, 1))
    (1): Conv2d(1, 256, kernel_size=(3, 300), stride=(1, 1))
    (2): Conv2d(1, 256, kernel_size=(4, 300), stride=(1, 1))
  )
  (dropout): Dropout(p=0.5, inplace=False)
  (fc): Linear(in_features=768, out_features=10, bias=True)
)>
Epoch [1/20]
Iter:      0,  Train Loss:   2.3,  Train Acc: 12.50%,  Val Loss:   2.7,  Val Acc: 10.05%,  Time: 0:00:17 *
Iter:    100,  Train Loss:  0.71,  Train Acc: 75.78%,  Val Loss:  0.68,  Val Acc: 78.88%,  Time: 0:03:35 *
Iter:    200,  Train Loss:  0.69,  Train Acc: 73.44%,  Val Loss:  0.54,  Val Acc: 83.62%,  Time: 0:07:00 *
Iter:    300,  Train Loss:  0.41,  Train Acc: 88.28%,  Val Loss:  0.49,  Val Acc: 84.71%,  Time: 0:10:13 *
Iter:    400,  Train Loss:  0.73,  Train Acc: 79.69%,  Val Loss:  0.46,  Val Acc: 85.87%,  Time: 0:13:39 *
Iter:    500,  Train Loss:  0.38,  Train Acc: 89.06%,  Val Loss:  0.42,  Val Acc: 86.84%,  Time: 0:16:56 *
Iter:    600,  Train Loss:  0.47,  Train Acc: 84.38%,  Val Loss:  0.42,  Val Acc: 86.96%,  Time: 0:20:22 *
Iter:    700,  Train Loss:  0.44,  Train Acc: 88.28%,  Val Loss:  0.39,  Val Acc: 87.63%,  Time: 0:23:34 *
Iter:    800,  Train Loss:  0.37,  Train Acc: 89.84%,  Val Loss:  0.38,  Val Acc: 88.30%,  Time: 0:26:45 *
Iter:    900,  Train Loss:  0.43,  Train Acc: 87.50%,  Val Loss:  0.38,  Val Acc: 88.53%,  Time: 0:29:57 *
Iter:   1000,  Train Loss:   0.3,  Train Acc: 89.84%,  Val Loss:  0.37,  Val Acc: 88.47%,  Time: 0:33:09 *
Iter:   1100,  Train Loss:  0.41,  Train Acc: 89.06%,  Val Loss:  0.37,  Val Acc: 88.74%,  Time: 0:36:18 *
Iter:   1200,  Train Loss:  0.36,  Train Acc: 88.28%,  Val Loss:  0.36,  Val Acc: 89.34%,  Time: 0:39:30 *
Iter:   1300,  Train Loss:  0.41,  Train Acc: 85.16%,  Val Loss:  0.36,  Val Acc: 88.92%,  Time: 0:43:01 *
Iter:   1400,  Train Loss:   0.5,  Train Acc: 85.16%,  Val Loss:  0.35,  Val Acc: 89.17%,  Time: 0:46:38 *
Epoch [2/20]
Iter:   1500,  Train Loss:  0.43,  Train Acc: 89.06%,  Val Loss:  0.34,  Val Acc: 89.43%,  Time: 0:50:02 *
Iter:   1600,  Train Loss:   0.3,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 89.37%,  Time: 0:53:35 
Iter:   1700,  Train Loss:  0.38,  Train Acc: 87.50%,  Val Loss:  0.33,  Val Acc: 89.72%,  Time: 0:56:45 *
Iter:   1800,  Train Loss:  0.32,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 89.29%,  Time: 0:59:56 
Iter:   1900,  Train Loss:  0.33,  Train Acc: 87.50%,  Val Loss:  0.33,  Val Acc: 89.85%,  Time: 1:03:08 *
Iter:   2000,  Train Loss:  0.34,  Train Acc: 86.72%,  Val Loss:  0.33,  Val Acc: 89.58%,  Time: 1:06:19 
Iter:   2100,  Train Loss:   0.4,  Train Acc: 87.50%,  Val Loss:  0.33,  Val Acc: 89.95%,  Time: 1:09:31 *
Iter:   2200,  Train Loss:   0.3,  Train Acc: 91.41%,  Val Loss:  0.33,  Val Acc: 89.72%,  Time: 1:12:42 
Iter:   2300,  Train Loss:  0.26,  Train Acc: 94.53%,  Val Loss:  0.32,  Val Acc: 90.03%,  Time: 1:15:54 *
Iter:   2400,  Train Loss:  0.25,  Train Acc: 93.75%,  Val Loss:  0.33,  Val Acc: 89.84%,  Time: 1:19:04 
Iter:   2500,  Train Loss:  0.17,  Train Acc: 93.75%,  Val Loss:  0.32,  Val Acc: 90.39%,  Time: 1:22:17 *
Iter:   2600,  Train Loss:  0.35,  Train Acc: 87.50%,  Val Loss:  0.31,  Val Acc: 90.32%,  Time: 1:25:30 *
Iter:   2700,  Train Loss:  0.26,  Train Acc: 90.62%,  Val Loss:  0.32,  Val Acc: 90.15%,  Time: 1:28:42 
Iter:   2800,  Train Loss:  0.37,  Train Acc: 87.50%,  Val Loss:  0.31,  Val Acc: 90.30%,  Time: 1:31:54 *
Epoch [3/20]
Iter:   2900,  Train Loss:  0.35,  Train Acc: 87.50%,  Val Loss:  0.31,  Val Acc: 90.37%,  Time: 1:35:05 *
Iter:   3000,  Train Loss:  0.23,  Train Acc: 93.75%,  Val Loss:  0.31,  Val Acc: 90.20%,  Time: 1:38:16 
Iter:   3100,  Train Loss:  0.24,  Train Acc: 92.19%,  Val Loss:  0.32,  Val Acc: 90.27%,  Time: 1:41:31 
Iter:   3200,  Train Loss:  0.39,  Train Acc: 89.84%,  Val Loss:  0.32,  Val Acc: 90.07%,  Time: 1:44:45 
Iter:   3300,  Train Loss:  0.34,  Train Acc: 88.28%,  Val Loss:  0.31,  Val Acc: 90.45%,  Time: 1:47:56 *
Iter:   3400,  Train Loss:  0.25,  Train Acc: 93.75%,  Val Loss:  0.32,  Val Acc: 90.50%,  Time: 1:51:06 
Iter:   3500,  Train Loss:  0.15,  Train Acc: 93.75%,  Val Loss:  0.31,  Val Acc: 90.27%,  Time: 1:54:17 *
Iter:   3600,  Train Loss:  0.16,  Train Acc: 95.31%,  Val Loss:  0.31,  Val Acc: 90.35%,  Time: 1:57:41 *
Iter:   3700,  Train Loss:  0.33,  Train Acc: 87.50%,  Val Loss:  0.31,  Val Acc: 90.49%,  Time: 2:00:54 
Iter:   3800,  Train Loss:  0.35,  Train Acc: 87.50%,  Val Loss:  0.31,  Val Acc: 90.44%,  Time: 2:04:11 
Iter:   3900,  Train Loss:  0.28,  Train Acc: 89.06%,  Val Loss:  0.31,  Val Acc: 90.44%,  Time: 2:07:24 
Iter:   4000,  Train Loss:  0.28,  Train Acc: 89.84%,  Val Loss:  0.32,  Val Acc: 90.42%,  Time: 2:10:39 
Iter:   4100,  Train Loss:  0.22,  Train Acc: 91.41%,  Val Loss:  0.31,  Val Acc: 90.57%,  Time: 2:13:58 
Iter:   4200,  Train Loss:  0.24,  Train Acc: 91.41%,  Val Loss:  0.31,  Val Acc: 90.52%,  Time: 2:17:11 
Epoch [4/20]
Iter:   4300,  Train Loss:  0.15,  Train Acc: 94.53%,  Val Loss:  0.31,  Val Acc: 90.17%,  Time: 2:20:23 
Iter:   4400,  Train Loss:  0.12,  Train Acc: 97.66%,  Val Loss:   0.3,  Val Acc: 90.77%,  Time: 2:23:49 *
Iter:   4500,  Train Loss:  0.31,  Train Acc: 89.84%,  Val Loss:  0.31,  Val Acc: 90.57%,  Time: 2:27:28 
Iter:   4600,  Train Loss:  0.17,  Train Acc: 95.31%,  Val Loss:  0.31,  Val Acc: 90.49%,  Time: 2:30:47 
Iter:   4700,  Train Loss:  0.31,  Train Acc: 88.28%,  Val Loss:  0.31,  Val Acc: 90.61%,  Time: 2:34:01 
Iter:   4800,  Train Loss:  0.16,  Train Acc: 95.31%,  Val Loss:   0.3,  Val Acc: 90.77%,  Time: 2:37:19 *
Iter:   4900,  Train Loss:   0.2,  Train Acc: 94.53%,  Val Loss:  0.31,  Val Acc: 90.78%,  Time: 2:40:43 
Iter:   5000,  Train Loss:  0.19,  Train Acc: 92.19%,  Val Loss:  0.31,  Val Acc: 90.56%,  Time: 2:44:16 
Iter:   5100,  Train Loss:  0.17,  Train Acc: 94.53%,  Val Loss:  0.31,  Val Acc: 90.67%,  Time: 2:47:43 
Iter:   5200,  Train Loss:  0.31,  Train Acc: 91.41%,  Val Loss:   0.3,  Val Acc: 90.88%,  Time: 2:51:21 *
Iter:   5300,  Train Loss:   0.2,  Train Acc: 91.41%,  Val Loss:  0.31,  Val Acc: 90.70%,  Time: 2:54:36 
Iter:   5400,  Train Loss:  0.35,  Train Acc: 91.41%,  Val Loss:  0.31,  Val Acc: 90.63%,  Time: 2:57:46 
Iter:   5500,  Train Loss:  0.21,  Train Acc: 92.97%,  Val Loss:  0.31,  Val Acc: 90.79%,  Time: 3:00:56 
Iter:   5600,  Train Loss:  0.14,  Train Acc: 95.31%,  Val Loss:  0.31,  Val Acc: 90.61%,  Time: 3:04:08 
Epoch [5/20]
Iter:   5700,  Train Loss:  0.24,  Train Acc: 92.19%,  Val Loss:  0.31,  Val Acc: 90.44%,  Time: 3:07:17 
Iter:   5800,  Train Loss:  0.17,  Train Acc: 96.09%,  Val Loss:  0.31,  Val Acc: 90.78%,  Time: 3:10:26 
Iter:   5900,  Train Loss:  0.16,  Train Acc: 95.31%,  Val Loss:  0.31,  Val Acc: 90.77%,  Time: 3:13:37 
Iter:   6000,  Train Loss:  0.19,  Train Acc: 94.53%,  Val Loss:  0.31,  Val Acc: 90.58%,  Time: 3:16:50 
Iter:   6100,  Train Loss:  0.24,  Train Acc: 90.62%,  Val Loss:  0.31,  Val Acc: 90.80%,  Time: 3:20:10 
Iter:   6200,  Train Loss:   0.1,  Train Acc: 96.09%,  Val Loss:  0.32,  Val Acc: 90.41%,  Time: 3:24:00 
No optimization for a long time, auto-stopping...
Test Loss:  0.28,  Test Acc: 91.69%
Precision, Recall and F1-Score...
               precision    recall  f1-score   support

      finance     0.9293    0.8940    0.9113      1000
       realty     0.9413    0.9300    0.9356      1000
       stocks     0.8798    0.8560    0.8677      1000
    education     0.9518    0.9480    0.9499      1000
      science     0.8702    0.8850    0.8775      1000
      society     0.8947    0.9260    0.9101      1000
     politics     0.9030    0.9030    0.9030      1000
       sports     0.9378    0.9650    0.9512      1000
         game     0.9361    0.9230    0.9295      1000
entertainment     0.9260    0.9390    0.9325      1000

     accuracy                         0.9169     10000
    macro avg     0.9170    0.9169    0.9168     10000
 weighted avg     0.9170    0.9169    0.9168     10000

Confusion Matrix...
[[894  11  49   3   9  11  11   7   3   2]
 [ 11 930  14   3   5  15   6   6   4   6]
 [ 42  20 856   3  38   2  30   2   5   2]
 [  1   3   1 948   3  18   7   7   2  10]
 [  2   2  22   7 885  15  18   5  29  15]
 [  1  12   3  16   8 926  18   5   3   8]
 [  7   5  21  11  15  28 903   3   0   7]
 [  2   1   1   0   3   7   3 965   5  13]
 [  0   0   6   2  37   6   2  12 923  12]
 [  2   4   0   3  14   7   2  17  12 939]]
Time usage: 0:00:15
```

# %python run.py --model TextCNN --adversarial FREE
```
Loading data...
Vocab size: 4762
180000it [00:03, 59397.90it/s]
10000it [00:00, 63570.00it/s]
10000it [00:00, 60858.81it/s]
Time usage: 0:00:03
<bound method Module.parameters of Model(
  (embedding): Embedding(4762, 300)
  (convs): ModuleList(
    (0): Conv2d(1, 256, kernel_size=(2, 300), stride=(1, 1))
    (1): Conv2d(1, 256, kernel_size=(3, 300), stride=(1, 1))
    (2): Conv2d(1, 256, kernel_size=(4, 300), stride=(1, 1))
  )
  (dropout): Dropout(p=0.5, inplace=False)
  (fc): Linear(in_features=768, out_features=10, bias=True)
)>
Epoch [1/20]
Iter:      0,  Train Loss:   2.1,  Train Acc: 18.75%,  Val Loss:   2.3,  Val Acc: 26.24%,  Time: 0:00:16 *
Iter:    100,  Train Loss:  0.58,  Train Acc: 81.25%,  Val Loss:  0.59,  Val Acc: 81.67%,  Time: 0:03:10 *
Iter:    200,  Train Loss:   0.6,  Train Acc: 80.47%,  Val Loss:  0.52,  Val Acc: 84.13%,  Time: 0:06:00 *
Iter:    300,  Train Loss:  0.53,  Train Acc: 82.81%,  Val Loss:   0.5,  Val Acc: 84.60%,  Time: 0:08:35 *
Iter:    400,  Train Loss:  0.73,  Train Acc: 75.78%,  Val Loss:  0.48,  Val Acc: 85.10%,  Time: 0:11:12 *
Iter:    500,  Train Loss:  0.39,  Train Acc: 89.84%,  Val Loss:  0.44,  Val Acc: 86.57%,  Time: 0:13:57 *
Iter:    600,  Train Loss:  0.51,  Train Acc: 84.38%,  Val Loss:  0.43,  Val Acc: 87.15%,  Time: 0:16:56 *
Iter:    700,  Train Loss:  0.59,  Train Acc: 78.12%,  Val Loss:  0.42,  Val Acc: 87.07%,  Time: 0:19:37 *
Iter:    800,  Train Loss:  0.42,  Train Acc: 85.16%,  Val Loss:  0.41,  Val Acc: 87.32%,  Time: 0:22:15 *
Iter:    900,  Train Loss:  0.45,  Train Acc: 85.94%,  Val Loss:  0.41,  Val Acc: 87.69%,  Time: 0:24:51 
Iter:   1000,  Train Loss:  0.26,  Train Acc: 90.62%,  Val Loss:  0.39,  Val Acc: 88.11%,  Time: 0:27:26 *
Iter:   1100,  Train Loss:  0.35,  Train Acc: 89.06%,  Val Loss:  0.39,  Val Acc: 88.00%,  Time: 0:30:03 
Iter:   1200,  Train Loss:  0.38,  Train Acc: 85.94%,  Val Loss:   0.4,  Val Acc: 87.91%,  Time: 0:32:52 
Iter:   1300,  Train Loss:  0.52,  Train Acc: 85.16%,  Val Loss:  0.38,  Val Acc: 88.29%,  Time: 0:35:33 *
Iter:   1400,  Train Loss:  0.48,  Train Acc: 84.38%,  Val Loss:  0.38,  Val Acc: 88.36%,  Time: 0:38:30 
Epoch [2/20]
Iter:   1500,  Train Loss:  0.48,  Train Acc: 84.38%,  Val Loss:  0.39,  Val Acc: 87.92%,  Time: 0:41:47 
Iter:   1600,  Train Loss:  0.28,  Train Acc: 91.41%,  Val Loss:  0.37,  Val Acc: 88.81%,  Time: 0:45:04 *
Iter:   1700,  Train Loss:  0.34,  Train Acc: 89.84%,  Val Loss:  0.36,  Val Acc: 89.29%,  Time: 0:48:10 *
Iter:   1800,  Train Loss:  0.31,  Train Acc: 90.62%,  Val Loss:  0.36,  Val Acc: 89.20%,  Time: 0:51:20 
Iter:   1900,  Train Loss:  0.43,  Train Acc: 87.50%,  Val Loss:  0.36,  Val Acc: 89.30%,  Time: 0:54:24 *
Iter:   2000,  Train Loss:  0.41,  Train Acc: 86.72%,  Val Loss:  0.36,  Val Acc: 89.18%,  Time: 0:57:33 
Iter:   2100,  Train Loss:  0.36,  Train Acc: 86.72%,  Val Loss:  0.35,  Val Acc: 89.43%,  Time: 1:00:37 *
Iter:   2200,  Train Loss:  0.36,  Train Acc: 86.72%,  Val Loss:  0.37,  Val Acc: 89.06%,  Time: 1:03:50 
Iter:   2300,  Train Loss:  0.27,  Train Acc: 92.19%,  Val Loss:  0.35,  Val Acc: 89.31%,  Time: 1:06:57 
Iter:   2400,  Train Loss:  0.25,  Train Acc: 90.62%,  Val Loss:  0.36,  Val Acc: 89.30%,  Time: 1:09:53 
Iter:   2500,  Train Loss:  0.26,  Train Acc: 91.41%,  Val Loss:  0.36,  Val Acc: 89.23%,  Time: 1:12:32 
Iter:   2600,  Train Loss:  0.38,  Train Acc: 87.50%,  Val Loss:  0.36,  Val Acc: 89.20%,  Time: 1:15:14 
Iter:   2700,  Train Loss:  0.28,  Train Acc: 89.06%,  Val Loss:  0.35,  Val Acc: 89.74%,  Time: 1:18:21 *
Iter:   2800,  Train Loss:  0.34,  Train Acc: 87.50%,  Val Loss:  0.34,  Val Acc: 89.59%,  Time: 1:21:05 *
Epoch [3/20]
Iter:   2900,  Train Loss:  0.43,  Train Acc: 85.94%,  Val Loss:  0.34,  Val Acc: 89.93%,  Time: 1:24:17 *
Iter:   3000,  Train Loss:  0.32,  Train Acc: 88.28%,  Val Loss:  0.34,  Val Acc: 89.74%,  Time: 1:27:29 
Iter:   3100,  Train Loss:  0.36,  Train Acc: 92.19%,  Val Loss:  0.34,  Val Acc: 90.14%,  Time: 1:30:45 *
Iter:   3200,  Train Loss:  0.47,  Train Acc: 87.50%,  Val Loss:  0.34,  Val Acc: 89.76%,  Time: 1:33:56 
Iter:   3300,  Train Loss:  0.24,  Train Acc: 92.19%,  Val Loss:  0.33,  Val Acc: 90.09%,  Time: 1:37:07 *
Iter:   3400,  Train Loss:  0.25,  Train Acc: 90.62%,  Val Loss:  0.34,  Val Acc: 89.92%,  Time: 1:40:25 
Iter:   3500,  Train Loss:  0.21,  Train Acc: 91.41%,  Val Loss:  0.34,  Val Acc: 90.13%,  Time: 1:43:29 
Iter:   3600,  Train Loss:  0.24,  Train Acc: 92.97%,  Val Loss:  0.34,  Val Acc: 90.04%,  Time: 1:46:34 
Iter:   3700,  Train Loss:  0.28,  Train Acc: 89.06%,  Val Loss:  0.34,  Val Acc: 89.94%,  Time: 1:49:38 
Iter:   3800,  Train Loss:  0.38,  Train Acc: 86.72%,  Val Loss:  0.35,  Val Acc: 89.74%,  Time: 1:52:14 
Iter:   3900,  Train Loss:  0.36,  Train Acc: 88.28%,  Val Loss:  0.35,  Val Acc: 89.69%,  Time: 1:55:00 
Iter:   4000,  Train Loss:  0.26,  Train Acc: 90.62%,  Val Loss:  0.34,  Val Acc: 90.32%,  Time: 1:57:40 
Iter:   4100,  Train Loss:  0.29,  Train Acc: 86.72%,  Val Loss:  0.33,  Val Acc: 90.33%,  Time: 2:00:28 
Iter:   4200,  Train Loss:  0.38,  Train Acc: 85.16%,  Val Loss:  0.33,  Val Acc: 90.26%,  Time: 2:03:18 
Epoch [4/20]
Iter:   4300,  Train Loss:  0.34,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 90.32%,  Time: 2:06:22 *
Iter:   4400,  Train Loss:  0.19,  Train Acc: 92.97%,  Val Loss:  0.33,  Val Acc: 90.48%,  Time: 2:09:32 
Iter:   4500,  Train Loss:  0.43,  Train Acc: 90.62%,  Val Loss:  0.32,  Val Acc: 90.76%,  Time: 2:12:38 *
Iter:   4600,  Train Loss:  0.28,  Train Acc: 91.41%,  Val Loss:  0.33,  Val Acc: 90.34%,  Time: 2:15:45 
Iter:   4700,  Train Loss:  0.31,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 90.25%,  Time: 2:18:42 
Iter:   4800,  Train Loss:   0.3,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 90.31%,  Time: 2:23:47 
Iter:   4900,  Train Loss:  0.22,  Train Acc: 93.75%,  Val Loss:  0.33,  Val Acc: 90.37%,  Time: 2:28:17 
Iter:   5000,  Train Loss:  0.36,  Train Acc: 92.19%,  Val Loss:  0.35,  Val Acc: 90.01%,  Time: 2:31:48 
Iter:   5100,  Train Loss:  0.26,  Train Acc: 90.62%,  Val Loss:  0.33,  Val Acc: 90.48%,  Time: 2:34:44 
Iter:   5200,  Train Loss:  0.27,  Train Acc: 88.28%,  Val Loss:  0.33,  Val Acc: 90.80%,  Time: 2:37:15 
Iter:   5300,  Train Loss:   0.2,  Train Acc: 92.97%,  Val Loss:  0.35,  Val Acc: 90.52%,  Time: 2:39:48 
Iter:   5400,  Train Loss:  0.32,  Train Acc: 89.84%,  Val Loss:  0.34,  Val Acc: 90.33%,  Time: 2:42:22 
Iter:   5500,  Train Loss:  0.29,  Train Acc: 89.06%,  Val Loss:  0.33,  Val Acc: 90.58%,  Time: 2:44:58 
No optimization for a long time, auto-stopping...
Test Loss:  0.31,  Test Acc: 90.86%
Precision, Recall and F1-Score...
               precision    recall  f1-score   support

      finance     0.9234    0.8800    0.9012      1000
       realty     0.9312    0.9340    0.9326      1000
       stocks     0.8314    0.8630    0.8469      1000
    education     0.9586    0.9490    0.9538      1000
      science     0.8559    0.8790    0.8673      1000
      society     0.8916    0.9050    0.8983      1000
     politics     0.8857    0.8910    0.8883      1000
       sports     0.9517    0.9450    0.9483      1000
         game     0.9484    0.9000    0.9236      1000
entertainment     0.9162    0.9400    0.9279      1000

     accuracy                         0.9086     10000
    macro avg     0.9094    0.9086    0.9088     10000
 weighted avg     0.9094    0.9086    0.9088     10000

Confusion Matrix...
[[880  12  66   2   9  11  10   4   3   3]
 [ 10 934  16   1   5  16   4   3   1  10]
 [ 43  23 863   2  33   4  24   3   2   3]
 [  2   1   4 949   4  13  13   4   1   9]
 [  2   5  34   5 879  16  21   2  24  12]
 [  4  16   2  17  13 905  25   4   2  12]
 [  8   4  36   7  15  30 891   2   1   6]
 [  1   2   7   1   9   6   8 945   1  20]
 [  2   0   9   4  50   8   3  13 900  11]
 [  1   6   1   2  10   6   7  13  14 940]]
Time usage: 0:00:14
···
