# HW 11 Reinforcement Learning with OpenGym

[![Lunar Lander Episode 510](./episode510.gif)](https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/episode510.mp4)


### Questions

#### 1. 
I trained the Lunar Lander model with the following parameters, leaving only num_epochs unchanged:

``` python
        self.density_first_layer = 250
        self.density_second_layer = 150
        self.num_epochs = 1
        self.batch_size = 128
        self.epsilon_min = 0.001
```

#### 2. 
I did run a test with `num_epochs` set to 100 but noticed the lunar window tended to lag between episodes. Instead I upped the batch size to 128 since the DNQ model was so small compared to a CNN network. I also played around with the epsilon decay and variables but wasn't able to get anything to train successfully.

#### 3. 
I did a test run with epsilon decay set to `0.95` and found that epsilon decay'd way too early to allow a successful training run. I also did many early test runs with the first two density layers set to smaller numbers like 32 and 16: since I didn't have the access to add additional layers I tested with the much larger sizes above and got better results. 

#### 4. 
Increasing the density layers to the values above made the most significant improvements and resulting in one of my test runs where only one of the scores was below 200.

Test Run 1
```
Starting Testing of the trained model...
0 : Episode || Reward:  238.51966391842765
1 : Episode || Reward:  228.00250656780176
2 : Episode || Reward:  219.58694892437637
3 : Episode || Reward:  257.40652369869036
4 : Episode || Reward:  222.070951235245
5 : Episode || Reward:  190.65793831752185
6 : Episode || Reward:  222.8140212313104
7 : Episode || Reward:  246.58024951216473
8 : Episode || Reward:  257.677800330818
9 : Episode || Reward:  249.7977519578318
10 : Episode || Reward:  215.1399199933074
Traceback (most recent call last):
  File "agent_lunar_lander.py", line 260, in <module>
    skvideo.io.vwrite(fname, np.array(frames))
MemoryError: Unable to allocate 2.40 GiB for an array with shape (3581, 400, 600, 3) and data type uint8

real 383m13.032s
user 0m5.320s
sys 0m0.420s
```

Test Run 2
```
Starting Testing of the trained model...
0 : Episode || Reward:  133.44152217542523
1 : Episode || Reward:  245.29862174984757
2 : Episode || Reward:  274.61848178509615
3 : Episode || Reward:  218.86257367673488
4 : Episode || Reward:  279.37500387347893
5 : Episode || Reward:  155.8961783294013
6 : Episode || Reward:  258.3949193748402
7 : Episode || Reward:  279.7479515078428
8 : Episode || Reward:  125.63343165554276
9 : Episode || Reward:  243.332481682972
10 : Episode || Reward:  266.7110500050317
11 : Episode || Reward:  300.59553419804877
12 : Episode || Reward:  249.29861897960492
13 : Episode || Reward:  273.6310911430463
14 : Episode || Reward:  267.57906667701036
15 : Episode || Reward:  221.97518070217205

real 536m9.104s
user 0m5.984s
sys 0m14.612s
```
#### 5. 

I
#### 6. 

I
#### 7. 
I

### Videos:

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/episode0.mp4

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/episode200.mp4

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/episode510.mp4

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/testing_run0.mp4

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/LunarLander/testing_run10.mp4
