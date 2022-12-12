def parse_input(arg):
    res = arg.split('\n\n')
    res = [x.split() for x in res]
    res = [[int(x) for x in y] for y in res]
    return res

def main():
    parsed = parse_input(day_input())
    result1 = [sum(x) for x in parsed]
    print(max(result1))

    result2 = sorted(result1, reverse=True)
    result2 = result2[:3]
    print(sum(result2))


def day_input_test():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def day_input():
    return"""4323
4004
4070
1780
5899
1912
2796
5743
3008
1703
4870
5048
2485
1204

30180

33734
19662

2402
4395
2703
1562
2407
3393
4311
1314
2729
2225
4420
4136
2867
1032
2095

7366
3496
6177
1426
4750
2655
3194
4240
4024
3510
2606
2335

1524
17720
23749

2549
1945
3392
4965
5601
4725
1462
1470
2988
5339
1620
6098
4447
5115
4102

2729
4836
10723
6705
2278
3290
2735
1813

10285
2302
6970
10710
8791
5575
9765
2167

1081
6290
3701
2457
9551
9625
3870
8433
5653

5647
2342
5549
2861
4081
3166
1902
3217
3255
4353
1752
2491
3271
4239
5744

14082

24855
23123
18215

9650
5995
11848
1258
10354
5948
9052

5347
7820
4620
4217
2686
7163
4911
8538
6851
8342

6323
3157
6939
3400
5297
6815
1476
2440
5816
6400
4198
2356

6537
2596
5678
7605
1882
4329
7488
6548
3687
2827
1461

4933
4880
1169
4190
5993
5452
5131
3310
5996
2670
1972
4666
3296
3978
4119

1372
2160
1268
3378
5672
2384
2772
2513
3534
1372
4691
4311
3016
5941
5035

3644
2169
5597
1874
1841
1794
2331
4907
1607
3104
1893
2026
4297
4078

7561
8745
10249
2438
4872
5647
7849
6634

21402
34212

2268
2107
3715
6236
3881
6741
6475
2999
4231
3936
4840

2318
5735
19378
7775

1848
12168

3324
5284
6502
5135
2887
5849
4107
1065
1236
1572
5308
2337
5741
1705

4445
3494
4890
3522
3456
3218
7020
3640
4653
4794
6003
4552

13971
2866
14359
1749
2761

8963
2088
6758
16065
4613

8406
3200
4467
5892
6549
6360
7789
1592
5334
5007

9335
9406
12089
10628
8080
1841
6973

7553
10626
8661
1747
4561
10772

3487
2524
2696
4140
4367
2367
6005
2465
2360
3447
1242
6378
4295

23471
14744
19137

15284
10987
1491
17669

2182
5750
7466
1965
1274
5648
7230
6127
7768
5246
2758

7451
6614
6538
6789

7381
6243
3806
4838
5163
2962
6748
1982
1049
5178
6590
3739

1598
4645
5128
3838
4383
2742
1654
2272
5518
1599
2948

6939
6508
4072
2196
3589
1905
2221
6003
6090
3612
1791
5525
4015

27936

1695
5271
5888
3809
4023
4690

4147
14521
18575
11452

2886
3542
4260
5414
4207
6920
3285
4103
2480
5378
5062
2587
1473

6375
5824
2640
1315
8095
1743
3695
7109

5281
2346
4972
4967
6804
1448
9301
1234

52340

5369
5911
3839
6600
4474
1724
3595
3585
3513
7336
2277
4851

7017
12732
9304
12136
6256
12880

3559
2147
4293
1481
4349
5624
3611
5194
4575
1662
6141
5599
1199
5901

29966
20696

3317
4398
1493
1730
2417
1597
5310
5163
4484
5160
1890
5695
4027
4393

13693
6774
7495
9515
9103
12116

10203
26377

6056
5189
3946
3696
4086
6017
7008
5212
2740
7433
3303
6170

6140
3588
5969
3308
3063
4591
6575

1803
8431
1340
5409
12106
5774

6812
6740
1025
7512
9778
7297
9872
4269

7012
1225
6654
4828
4791
1514
4144
5631
6230
2530
6276
2142

5884
5873
5068
5132
3739
4874
2798
2461
6577
4926
4343
1450

68707

4992
3372
5660
7139
5052
6115
1749
2810
7021
5529
5782
4395

1953
4377
6438
1987
5046
3732
4600
5665
5882
1974
6009
3727
1134

6339
5628
7716
2740
8091
3185
3877
2099
2812

1352
1928
2815
7509
1311
6981
4396
4094
3827
2278
2727

2249
4138
3251
3581
4657
2234
2070
1525
2206
3512
5139
3792
6039
5885

5939
1603
6497
4450
4937
1762
1301
4543
6872
4967
1365
5738
2504

22837
10301
13380

3714
1854

2320
6723
2994
3402
4840
4613
3460
4068
6575
4539
2139
1206
3238

1974
11341
4645
12073
2637

3876
2380
7305
1130
6134
7401
3911
7322
6264
3299
5164
1688

5399
3485
6861
4543
10367
10255

4451
2902
6043
4384
4023
3587
2836
5649
4765
2051
1471
2365
1038
2452

11226
13152
4749
9547

5099
2983
12118
9251
12847
9391

23810
22967
13264

8898
11599
3103
6687
5592
3559

14152
2647
9210

4675
5105
3400
2991
1688
5839
4746
6007
5103
4212
3419
4335
1974
2035
2263

3266
1208
4104
5092
1816
4339
4732
1746
2569
5600
2329
1035
4238
6095
5008

17154
20316
25661

1199

1285
6497
3073
1862
6437
2001
3807
3519
2338
6727
1258
3402
4825

6970
8106
9383
12577

10963
5485
10936
12139
8948
10772
11053

24569
16515
12189

4741
3247
4106
1423
2540
2549
10404
6570

10768
23116
9838

3655
3142
3835
3542
7419
5830
3956
7272
1539
7260
3636
4308

1949
5477
3960
1215
2389
5869
5677
2235
4273
6776
5490
5299
4913

3272
2331
4138
2958
4780
5427
5949
2894
3669
4201
3000
3387
1227
5110
1990

7239
18190
17161
16971

3742
2960
3810
2564
1972
5363
1675
2370
4486
5243
4833
6036
1590
6058

4374
3018
4827
4061
2097
4819
2646
6851
3864
1289
3366
3328
2929

16680
6361
9020
14141

12541
12672
12624

5794
7699
10020
9455
1716
2567
8294
1179

8733
6078
10818
2697
10768
5266
5211

9435
7619
3382
14870
2752

5089
1720
1836
6485
6459
4323
5068
5987
2588
6906
6899
4500

6132
4466
5913
1613
5151
3915
4656
3483
2387
1811
6147
5757
6699

4541
1357
5762
1877
2240
4025
5053
1079
6121
8030
5597

2463
2185
2126
4766
2069
4302
2072
5028
1581
2359
1914
4554
3730
4141
1625

5440
7109
6947
4241
7812
7923
9238
6317
4657

8064
5655
8309
5404
4639
8986
2719
3403
2541

6183
5137
7918
7159
3194
3628
5371
1554
3641
5394
6931

11367
16399
9440
3911

7952
5780
9026
1500
3848
8218
9643
6783

1841
5956
1547
5079
6979
7912
2992
6197
8715

31416
13515

5752
6402
5541
2444
2944
3826
6410
6654
6195
3130
1380
6102
5668

3732
5016
1813
5901
2438
1416
8290
5437
2402
7254

31293
6165

24947

10582
24078
25144

11476
12288
4678
4895
16179

2580
6573
13083
5326
5067

30550

14659
2596
9144
17320

3546
14239
16336
15317
5453

3977
4131
1046
6956
5174
10004
8796
7734

3761
4088
2898
6563
1891
3269
1152
4755
3098
5713
4203
2498
2648

21485
22269

1620
1960
2738
2963
1404
1649
7600
1930
3740
5450
7719

3500
7419
4550
3240
4553
2453
1545
7036
6217
1822
7939

17049
12540
17626

3626
10619
10814
4500
3733
9168
5404

3069
6699
2440
5847
2373
4696
6403
3330
6840
5094
7211

1378
7603
2366
7951
9178
4302
3611
4883

6816
4009
6047
1044
1252
2401
6354
4211
5248
2811
1746
2959

2576
5322
4474
5253
3873
6448
1624
1986
1986
2540
2250
5397
4203
5733

1853
5903
5337
1648
7813
8378
5571
5351
6403

6127
5397
2123
1893
4920
6195
5524
6428
4728
3850
4327
2792
2969
2220

1591
4847
2415
1107
1986
3466
6095
7735
4027
2370
7637

3856
11292
2699
14112
3518

5427
2633
6628
2393
3645
2730
6007
3798
1715
2521
5221
5755
6318

5191
4058
3958
1219
1664
2551
3534
6406
5722
4383
2105
6376
1774
6175

14330
9855
17946

3386
4396
3669
1958
3971
1358
5917
6026
4452
1188
3052
2668
1651
5408
4088

5749
2369
2628
4214
1375
3109
2788
6028
4984
3822
4667
6093
3474

1556
6494
3916
5611
4326
6483
2510
6131
3110
2554
1847
5859
2238

1047
11827
3359
8841
11232
5803
9220

5555
6553
3903
3149
5458
10593
8455
10770

10630
7727
6683
4610
7987
7038
9909
4599

4637
1682
4114
4940
2386
3909
3110
1393

6153
4700
5461
7641
2153
5363

63414

4467
1956
5073
1822
9426
3549
6866
4901
9317

19947
11533
16836
18062

7143
5185
13258
3803

5299
2684
2610
3416
1783
5055
2894
1164
4200
4558
4380
3465
3395

4672
2427
6915
2155
3306
4559
2674
2230
6649
7296
3433

2191
4437
4644
6313
1187
1602
6811
1299
1541
4973
2073
2231
4216

4893
8788
5585
10703
9517
6913
1333

11440
25326
18092

10121
6807
4589
6972
5842
8278
6672
4871

13690
7766
7778
12899
3329
4407

7659
15344
17263
13394

6028
9037
2459
8859
6934
5789
5622
5893
8267

10362

5313
5005
6354
3387
2019
4933
4843
1508
4066
1121
5027
2157
2712
5325

35049

2068
2489
2968
3176
2835
1518
5949
1106
1685
1485
3896
4946

5681
7841
5218
5573
2042
5725
6117
3882
5360
1299
3584

6516
2684
6887
1375
4296
7171
7693
4603
8239

7661
8996
3419
4736
5552
7873
8297
4376

5516
3278
2425
3308
7722
5739
5177
6738
9194

13795
12863
8108
9938
2374
12314

4931
6334
6636
6256
1945
8716
7054
2035
6715
2180

21075
7049
23573

6985
9970
9153
10475
4568
6395
5514
2117

4115
2844
1399
3535
4606
1103
1443
5323
4760
3992
5580
1494
3193
5242
4359

5161
4143
7753
3973
4318
5862

1093
1436
1444
4439
1387
2114
4263
5738
4607
5261
4509
1389
4886
4671
1154

13316
14156
1452
11726
4234

8647
7076
1481
1740
6584
4276
1502
1675
4012
7089

8636
8325
8445
4384
4778
8110
10100
3155

19339
8585
5973
9399

1783
15809
1729

3964
1092
5948
8653
2149
3494
7388
7876
9334

1211
4258
1428
1096
3758
1416
5969
5451
4933
1057
1399
5513
3655
3350
1564

4917
3980
5441
1532
5716
2371
1617
3153
1022
1540
3450
2297
1505
5188
2649

2683
2317
5457
9576
8251
8707
1755
7220

4412
10875
10547
6061
6221
2062
9465

3382
5259
3723
3240
5556
4985
4318
5831
2944
1993
2127
4208
3354

6909
7400
4076
3987
1663
7575
7573
8001
1510
3691

7569
9266
1750
4823
6919
5647
2972
8801
8260

3683
5566
8718
4320
7857
2501
1559
8947

2798
4808
3952
5628
2242
1378
4920
10266

1457
7199
1838
5849
6482
4068
7236
1668
2691

15285
10046
11923

1030
2698
3211
7630
4617
3383
1296
7816
6360
7323
3514

17686
34956

7398
2970
5451
1272
1456
6877
2549
4228
5946
6077
6451
6957

4599
2727
2828
3147
1487
2387
5140
5558
6931

4933
6113
2104
6548
5215
5627
6464
3672
6387
3110
1809
2780
1446

5186
1672
2253
3198
2294
2995
5943
3154
3667
5065
2833
4049
2298
5234
2856

3558
2069
2723
3908
6045
2393
4610
1637
4515
3961
1013
1420
3111
1729

17556
18719
8542
7803

1261
4761
5767
4098
3474
6178
6008
8514
1956

7007
4158
2967
7673
5076
7086
1105
7095
5155
5637
2208

4953
5303
5460
5146
2388
2298
1295
6414
6323
4793
5755
3878
1985
2872

7697
4701
1005
6777
1763
5264
6781
6600
1924
1746
6696

3932
3387
4831
5621
5502
1486
6377
6891
5189
6879
2991
2986
3450

2929
2641
2704
2693
6820
3719
1908
2612
6381
3258
1002
5008

7366
34310

2798
5125
8729
4928
1009
6350
7994
2082
6524
6253

1723
1469
2474
4565
1985
3861
5804
3481
4338
3580
2814
2346
1635
4627

13779
15932
16875
2148

8405
11181
7324
10246
11640
9061
2999

2635
1534
1223
1013
4713
5928
5200
4605
4520
1525
6818
4778
3059

3802
2391
8430
10838
5125
3233
11733

47671

11952
2923
3109
4817
4190
3666
11952

8561
7214
4010
7247
7555
7647
3618
8425

2971
3620
5747
7010
5404
2331
2841
8718
2043
5788

2245
4763
6360
5985
2177
6117
7552
1784
4680
2854

6924
1946
5473
3555
1298
1934
10754
8047

9028
1819
2994
5197
8253
9841

6533
1279
4728
3839
1054
2440
2416
2840
4875

5537
5579
6856
4320
3616
2177
6398
3270
2763
1654
3765
3727
3373

6348
1050
4641
4267
5765
7125
2146
2032
5863
3712
6506
5430

5288
7292
9531
7158
11662

8798
8981
9789
16908

5016
13660
8515
5994

4023
6670
6553
4764
1253
3340
5925
1400
2684
5796
1678
3324

5489
1836
19472
11219

1799
4055
7191
3511
9603
3607
4621
8520
8535

2786
4514
3546
6248
1984
3742
2448
2319
3698
1658
3949
6408
3281
3804

7413
3530
8579
19575

13921
5842
12657
1413
9693
2867

1456
4298
1496
6437
4283
2442
3605
5482
6000
3628
2020
2812
2219
3000

7965
3790
9640
10772
9856
7923
10390

6009
2604
8201
11341
7748
6987

60028

7101
5285
9589
11810
11534
4085
1902

2519
9496
2703

3854
5685
3541
3317
2262
5910
3642
3461
5759
3899
1461
2692
6095
4992
3739

9302
4237
7146
11412
9320
9865
11517"""