# Questions

1. The following output is a snippet of the test results as well as the final time it took to train. I performed training on the Jetson Xavier NX and saw a slight improvement from the TX2, averaging 30 minutes an epoch.

```
Epoch: [99] completed, elapsed time 290.357 seconds
Test: [  0/142]	Time  0.577 ( 0.577)	Loss 2.2236e+00 (2.2236e+00)	Acc@1  37.50 ( 37.50)	Acc@5  75.00 ( 75.00)
Test: [ 10/142]	Time  0.123 ( 0.138)	Loss 5.0504e-01 (1.2579e+00)	Acc@1  87.50 ( 62.50)	Acc@5 100.00 ( 90.91)
Test: [ 20/142]	Time  0.087 ( 0.117)	Loss 1.3757e+00 (1.2355e+00)	Acc@1  62.50 ( 61.90)	Acc@5  87.50 ( 89.88)
Test: [ 30/142]	Time  0.060 ( 0.108)	Loss 6.4295e-01 (1.1881e+00)	Acc@1  62.50 ( 62.90)	Acc@5 100.00 ( 90.32)
Test: [ 40/142]	Time  0.065 ( 0.103)	Loss 2.3092e+00 (1.2768e+00)	Acc@1  25.00 ( 61.28)	Acc@5  75.00 ( 88.11)
Test: [ 50/142]	Time  0.065 ( 0.097)	Loss 1.4572e+00 (1.1329e+00)	Acc@1  75.00 ( 65.93)	Acc@5  75.00 ( 89.22)
Test: [ 60/142]	Time  0.062 ( 0.095)	Loss 6.0141e-02 (1.0516e+00)	Acc@1 100.00 ( 69.26)	Acc@5 100.00 ( 89.96)
Test: [ 70/142]	Time  0.061 ( 0.093)	Loss 8.5178e-02 (1.2057e+00)	Acc@1 100.00 ( 65.67)	Acc@5 100.00 ( 87.50)
Test: [ 80/142]	Time  0.063 ( 0.091)	Loss 3.6315e+00 (1.2580e+00)	Acc@1   0.00 ( 65.12)	Acc@5  37.50 ( 87.35)
Test: [ 90/142]	Time  0.073 ( 0.090)	Loss 1.1020e+00 (1.2746e+00)	Acc@1  62.50 ( 64.15)	Acc@5 100.00 ( 87.50)
Test: [100/142]	Time  0.089 ( 0.089)	Loss 1.5995e+00 (1.2845e+00)	Acc@1  37.50 ( 63.24)	Acc@5  87.50 ( 87.87)
Test: [110/142]	Time  0.064 ( 0.088)	Loss 2.6558e+00 (1.2957e+00)	Acc@1  25.00 ( 62.84)	Acc@5  75.00 ( 88.06)
Test: [120/142]	Time  0.062 ( 0.088)	Loss 2.2382e+00 (1.3276e+00)	Acc@1  37.50 ( 62.50)	Acc@5  87.50 ( 88.02)
Test: [130/142]	Time  0.067 ( 0.088)	Loss 2.1551e+00 (1.3819e+00)	Acc@1  37.50 ( 60.50)	Acc@5  62.50 ( 87.50)
Test: [140/142]	Time  0.097 ( 0.088)	Loss 3.7781e+00 (1.3942e+00)	Acc@1   0.00 ( 60.28)	Acc@5  87.50 ( 87.77)
 * Acc@1 60.352 Acc@5 87.841
saved checkpoint to:  plants/checkpoint.pth.tar

real	524m51.785s
user	511m45.420s
sys	29m21.384s

```
2. Unfortunately I didn't get a chance to train with larger batch sizes, and the following outputs will be used later in a class lab.

```
nvidia@nvidia-desktop:~/w251_projects/week13hw/jetson-inference/python/training/classification/plants$ ll
total 175000
drwxr-xr-x 2 nvidia nvidia     4096 Jul 25 11:44 ./
drwxr-xr-x 4 nvidia nvidia     4096 Jul 25 11:44 ../
-rw-r--r-- 1 nvidia nvidia 89594265 Jul 25 20:10 checkpoint.pth.tar
-rw-r--r-- 1 nvidia nvidia 89594267 Jul 25 20:05 model_best.pth.tar
```
