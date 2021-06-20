# Steps to change
# 1. Generate these points using this web site :
# https://www.keene.edu/campus/maps/tool/
# For every loop, close the loop and put it under one array --> points = [ [..,..], [...,...] ]
# create around 90-150 click per path

# 2. upload demo_routes.py and mqtt_clients to linux_devices host, path /fortipoc/mqtt
# Subagios-MacBook-Pro:~ subagioteguh$ cd Dropbox/Fortinet/SourceCode/ruparupa/iot-demo/singapore-demo/
# Subagios-MacBook-Pro:singapore-demo subagioteguh$ scp -P 10106 demo_routes.py root@34.101.251.202:/fortipoc/mqtt
#root@34.101.251.202's password:
# demo_routes.py                                                                                           100%   26KB 385.6KB/s   00:00
#Subagios-MacBook-Pro:singapore-demo subagioteguh$ scp -P 10106 mqtt_client.py root@34.101.251.202:/fortipoc/mqtt
#root@34.101.251.202's password:
#mqtt_client.py                                                                                          100% 2898    91.7KB/s   00:00
#Subagios-MacBook-Pro:singapore-demo subagioteguh$

# 3. SSH to linuxdevices, killall python3
# 4. Rerun ./start_clients
# 5. check ps ux -> all python3 should run again

# if the bicycle running in a blank map, may be something is wrong with the mqtt_client.py, make sure it is updated !

{
  "coordinates": [
    [
      [
        103.8353254,
        1.3002293
      ],
      [
        103.8352073,
        1.3002508
      ],
      [
        103.8350464,
        1.3002722
      ],
      [
        103.8348962,
        1.3002079
      ],
      [
        103.8347889,
        1.3000685
      ],
      [
        103.8345958,
        1.2999397
      ],
      [
        103.8344241,
        1.2998539
      ],
      [
        103.8342417,
        1.2998003
      ],
      [
        103.8339735,
        1.2998325
      ],
      [
        103.8339199,
        1.2995536
      ],
      [
        103.8339092,
        1.299264
      ],
      [
        103.8339306,
        1.2989208
      ],
      [
        103.833877,
        1.2986848
      ],
      [
        103.8338126,
        1.2983523
      ],
      [
        103.8337268,
        1.2981485
      ],
      [
        103.8336517,
        1.2978696
      ],
      [
        103.8335658,
        1.2976873
      ],
      [
        103.8335229,
        1.2973655
      ],
      [
        103.833598,
        1.2971188
      ],
      [
        103.8335551,
        1.2968721
      ],
      [
        103.8335229,
        1.2966361
      ],
      [
        103.8335122,
        1.2964216
      ],
      [
        103.8335873,
        1.2962821
      ],
      [
        103.8337804,
        1.2962178
      ],
      [
        103.833995,
        1.2961427
      ],
      [
        103.8342096,
        1.2961427
      ],
      [
        103.8343598,
        1.2961213
      ],
      [
        103.8344778,
        1.2961105
      ],
      [
        103.834628,
        1.2960783
      ],
      [
        103.8347567,
        1.2960569
      ],
      [
        103.8349177,
        1.2960462
      ],
      [
        103.8351322,
        1.2960247
      ],
      [
        103.8352824,
        1.2960033
      ],
      [
        103.8354434,
        1.2959711
      ],
      [
        103.8357974,
        1.2959389
      ],
      [
        103.8359905,
        1.2959175
      ],
      [
        103.8359691,
        1.2960783
      ],
      [
        103.8359154,
        1.2962285
      ],
      [
        103.8358833,
        1.296443
      ],
      [
        103.8358296,
        1.2966576
      ],
      [
        103.8357652,
        1.2968828
      ],
      [
        103.8357009,
        1.2970866
      ],
      [
        103.8356365,
        1.2972797
      ],
      [
        103.8355721,
        1.2975693
      ],
      [
        103.8354863,
        1.2979447
      ],
      [
        103.8356043,
        1.2979983
      ],
      [
        103.8357331,
        1.2978696
      ],
      [
        103.835894,
        1.2977945
      ],
      [
        103.8360764,
        1.2977516
      ],
      [
        103.8362588,
        1.2976444
      ],
      [
        103.8366128,
        1.2976122
      ],
      [
        103.8368059,
        1.29758
      ],
      [
        103.8369561,
        1.2975049
      ],
      [
        103.8370634,
        1.2973118
      ],
      [
        103.8371063,
        1.2971402
      ],
      [
        103.8372029,
        1.2967541
      ],
      [
        103.8372566,
        1.2965074
      ],
      [
        103.8372029,
        1.29625
      ],
      [
        103.8371922,
        1.2959282
      ],
      [
        103.8373317,
        1.2960033
      ],
      [
        103.8374282,
        1.2962071
      ],
      [
        103.8375462,
        1.2964001
      ],
      [
        103.8376535,
        1.2965717
      ],
      [
        103.8378359,
        1.2968077
      ],
      [
        103.8380612,
        1.2970544
      ],
      [
        103.8382114,
        1.2972797
      ],
      [
        103.8383509,
        1.2975049
      ],
      [
        103.8384904,
        1.2977087
      ],
      [
        103.8386298,
        1.2978482
      ],
      [
        103.83878,
        1.2980198
      ],
      [
        103.838941,
        1.2982772
      ],
      [
        103.8391019,
        1.2984703
      ],
      [
        103.8392843,
        1.2986633
      ],
      [
        103.839413,
        1.2988886
      ],
      [
        103.839413,
        1.2991246
      ],
      [
        103.8392736,
        1.2992318
      ],
      [
        103.8390375,
        1.2992854
      ],
      [
        103.8387264,
        1.2993284
      ],
      [
        103.8384689,
        1.2994249
      ],
      [
        103.8381256,
        1.2994892
      ],
      [
        103.8378037,
        1.2995321
      ],
      [
        103.8374389,
        1.2996287
      ],
      [
        103.8370956,
        1.2997038
      ],
      [
        103.8368059,
        1.2997788
      ],
      [
        103.8364733,
        1.2998647
      ],
      [
        103.8359691,
        1.2999934
      ],
      [
        103.8353254,
        1.3002293
      ]
    ]
  ],
  "type": "Polygon"
}
# singtel to left bottom

{
  "coordinates": [
    [
      [
        103.8394774,
        1.2991782
      ],
      [
        103.8395626,
        1.2991857
      ],
      [
        103.8396377,
        1.2992126
      ],
      [
        103.8396967,
        1.2992233
      ],
      [
        103.839761,
        1.2992287
      ],
      [
        103.8398361,
        1.2992447
      ],
      [
        103.839922,
        1.2992555
      ],
      [
        103.8400078,
        1.2992555
      ],
      [
        103.8401312,
        1.2992769
      ],
      [
        103.8402117,
        1.2992823
      ],
      [
        103.8403082,
        1.2993037
      ],
      [
        103.8403887,
        1.2993198
      ],
      [
        103.8405013,
        1.2993198
      ],
      [
        103.8405925,
        1.2993198
      ],
      [
        103.840673,
        1.2993037
      ],
      [
        103.8407696,
        1.299293
      ],
      [
        103.8408339,
        1.2992769
      ],
      [
        103.8409251,
        1.2992447
      ],
      [
        103.841011,
        1.2992233
      ],
      [
        103.8410914,
        1.2991857
      ],
      [
        103.8411719,
        1.2991428
      ],
      [
        103.8412738,
        1.2990892
      ],
      [
        103.8413489,
        1.2990356
      ],
      [
        103.8413596,
        1.2989712
      ],
      [
        103.8413328,
        1.2988908
      ],
      [
        103.841306,
        1.2988425
      ],
      [
        103.8412899,
        1.2987621
      ],
      [
        103.8412577,
        1.2986763
      ],
      [
        103.8412523,
        1.2986012
      ],
      [
        103.8412148,
        1.2985368
      ],
      [
        103.8412041,
        1.2984456
      ],
      [
        103.8411826,
        1.2983706
      ],
      [
        103.8411451,
        1.2982901
      ],
      [
        103.8411182,
        1.2981989
      ],
      [
        103.8410914,
        1.2981078
      ],
      [
        103.8410861,
        1.2979952
      ],
      [
        103.8410646,
        1.2979254
      ],
      [
        103.8410431,
        1.2978396
      ],
      [
        103.8410163,
        1.2977592
      ],
      [
        103.8409841,
        1.2976626
      ],
      [
        103.8409627,
        1.2975661
      ],
      [
        103.8409358,
        1.2974535
      ],
      [
        103.8409037,
        1.2973409
      ],
      [
        103.8408876,
        1.2972497
      ],
      [
        103.8408447,
        1.2971371
      ],
      [
        103.8408286,
        1.2970352
      ],
      [
        103.8408017,
        1.2969333
      ],
      [
        103.8407588,
        1.2968528
      ],
      [
        103.8407374,
        1.2967563
      ],
      [
        103.8407213,
        1.2966437
      ],
      [
        103.8406945,
        1.2965203
      ],
      [
        103.8406462,
        1.2964291
      ],
      [
        103.8406193,
        1.2963487
      ],
      [
        103.8405872,
        1.2962629
      ],
      [
        103.8405603,
        1.2961127
      ],
      [
        103.8405081,
        1.2960107
      ],
      [
        103.8405725,
        1.2959786
      ],
      [
        103.840653,
        1.2959732
      ],
      [
        103.8407388,
        1.2959678
      ],
      [
        103.8408354,
        1.2959517
      ],
      [
        103.8409427,
        1.2959303
      ],
      [
        103.841007,
        1.2958928
      ],
      [
        103.8410875,
        1.2958445
      ],
      [
        103.8411572,
        1.2957962
      ],
      [
        103.841227,
        1.2957426
      ],
      [
        103.8412806,
        1.2956782
      ],
      [
        103.8413611,
        1.2956192
      ],
      [
        103.8414308,
        1.2955442
      ],
      [
        103.8414684,
        1.2954423
      ],
      [
        103.8415113,
        1.2953511
      ],
      [
        103.8416293,
        1.2952331
      ],
      [
        103.8416454,
        1.2951741
      ],
      [
        103.8417259,
        1.2950079
      ],
      [
        103.8417902,
        1.2949274
      ],
      [
        103.8418975,
        1.2947558
      ],
      [
        103.8419673,
        1.2945627
      ],
      [
        103.8420906,
        1.2945466
      ],
      [
        103.8421658,
        1.2946378
      ],
      [
        103.8421765,
        1.2947504
      ],
      [
        103.8421389,
        1.2948201
      ],
      [
        103.8421014,
        1.294906
      ],
      [
        103.8420692,
        1.294981
      ],
      [
        103.8420263,
        1.2951151
      ],
      [
        103.8419834,
        1.2952277
      ],
      [
        103.8419404,
        1.2953672
      ],
      [
        103.8419029,
        1.2954905
      ],
      [
        103.8419343,
        1.295542
      ],
      [
        103.84187,
        1.2957029
      ],
      [
        103.8417948,
        1.2958746
      ],
      [
        103.8417948,
        1.2960462
      ],
      [
        103.8417519,
        1.2962178
      ],
      [
        103.8416446,
        1.2964216
      ],
      [
        103.8416232,
        1.2966039
      ],
      [
        103.8417412,
        1.2967648
      ],
      [
        103.8418485,
        1.2968935
      ],
      [
        103.8420416,
        1.2969472
      ],
      [
        103.8421918,
        1.2969793
      ],
      [
        103.8423527,
        1.2969472
      ],
      [
        103.84246,
        1.2971081
      ],
      [
        103.842503,
        1.2972904
      ],
      [
        103.8425244,
        1.2975156
      ],
      [
        103.8425673,
        1.2976444
      ],
      [
        103.8426746,
        1.2977516
      ],
      [
        103.8427712,
        1.2976015
      ],
      [
        103.8428248,
        1.2973977
      ],
      [
        103.8428892,
        1.2971939
      ],
      [
        103.8430072,
        1.2970544
      ],
      [
        103.8431145,
        1.2968399
      ],
      [
        103.8432325,
        1.2966361
      ],
      [
        103.8434471,
        1.2965396
      ],
      [
        103.843608,
        1.2964859
      ],
      [
        103.8438119,
        1.2964323
      ],
      [
        103.8439513,
        1.2964538
      ],
      [
        103.8439835,
        1.2966361
      ],
      [
        103.8439621,
        1.2968614
      ],
      [
        103.8439513,
        1.2970544
      ],
      [
        103.8439192,
        1.2972582
      ],
      [
        103.843887,
        1.2974191
      ],
      [
        103.843887,
        1.2976122
      ],
      [
        103.8438655,
        1.2977838
      ],
      [
        103.8438655,
        1.2979876
      ],
      [
        103.8438011,
        1.2982236
      ],
      [
        103.8437475,
        1.2983845
      ],
      [
        103.8437582,
        1.2985346
      ],
      [
        103.843726,
        1.2986741
      ],
      [
        103.8437153,
        1.2988135
      ],
      [
        103.8436295,
        1.2988993
      ],
      [
        103.8435007,
        1.2990066
      ],
      [
        103.8433505,
        1.2991138
      ],
      [
        103.8432647,
        1.2991889
      ],
      [
        103.8430394,
        1.2993069
      ],
      [
        103.8428892,
        1.2993713
      ],
      [
        103.842621,
        1.2994785
      ],
      [
        103.8424064,
        1.2996072
      ],
      [
        103.8421811,
        1.2996609
      ],
      [
        103.8419772,
        1.2997038
      ],
      [
        103.8417412,
        1.2997359
      ],
      [
        103.8416554,
        1.2998539
      ],
      [
        103.8417305,
        1.2999826
      ],
      [
        103.8417948,
        1.3001328
      ],
      [
        103.8418807,
        1.300283
      ],
      [
        103.841709,
        1.3003473
      ],
      [
        103.8415695,
        1.3003902
      ],
      [
        103.8414086,
        1.3004546
      ],
      [
        103.8412048,
        1.3004975
      ],
      [
        103.8410438,
        1.3005404
      ],
      [
        103.8408614,
        1.3006048
      ],
      [
        103.840679,
        1.3006477
      ],
      [
        103.8405718,
        1.3005082
      ],
      [
        103.840443,
        1.3004224
      ],
      [
        103.8403357,
        1.3002937
      ],
      [
        103.8402392,
        1.300165
      ],
      [
        103.8401426,
        1.3000148
      ],
      [
        103.8399924,
        1.2999076
      ],
      [
        103.8399066,
        1.2997574
      ],
      [
        103.83981,
        1.2996287
      ],
      [
        103.8396705,
        1.2994678
      ],
      [
        103.8395954,
        1.2993284
      ],
      [
        103.8394774,
        1.2991782
      ]
    ]
  ],
  "type": "Polygon"
}
# singtel to right up

{
  "coordinates": [
    [
      [
        103.8381117,
        1.2975523
      ],
      [
        103.83827,
        1.2975953
      ],
      [
        103.8382968,
        1.2976436
      ],
      [
        103.8383505,
        1.2977026
      ],
      [
        103.8384148,
        1.2977616
      ],
      [
        103.8384578,
        1.2978152
      ],
      [
        103.8385221,
        1.2978796
      ],
      [
        103.8385704,
        1.2979332
      ],
      [
        103.8386187,
        1.2979761
      ],
      [
        103.838667,
        1.2980244
      ],
      [
        103.8387152,
        1.2980834
      ],
      [
        103.8387582,
        1.298137
      ],
      [
        103.8388333,
        1.2982228
      ],
      [
        103.8388708,
        1.2982711
      ],
      [
        103.8389245,
        1.2983408
      ],
      [
        103.8389566,
        1.2983944
      ],
      [
        103.8390103,
        1.2984534
      ],
      [
        103.8390586,
        1.2985178
      ],
      [
        103.8391069,
        1.2985607
      ],
      [
        103.8391605,
        1.2986143
      ],
      [
        103.8392249,
        1.2986572
      ],
      [
        103.8392731,
        1.2987216
      ],
      [
        103.8393322,
        1.2988288
      ],
      [
        103.839418,
        1.2989093
      ],
      [
        103.839477,
        1.2989844
      ],
      [
        103.8395306,
        1.299038
      ],
      [
        103.8395896,
        1.2991077
      ],
      [
        103.8396379,
        1.2991882
      ],
      [
        103.8396969,
        1.2992793
      ],
      [
        103.8397667,
        1.2993491
      ],
      [
        103.8398203,
        1.2994134
      ],
      [
        103.8398793,
        1.2994885
      ],
      [
        103.8399222,
        1.2995475
      ],
      [
        103.8399759,
        1.2996279
      ],
      [
        103.8400134,
        1.2996762
      ],
      [
        103.8400778,
        1.299762
      ],
      [
        103.8401315,
        1.2998049
      ],
      [
        103.8401744,
        1.2998585
      ],
      [
        103.840228,
        1.2999122
      ],
      [
        103.8402709,
        1.2999819
      ],
      [
        103.8403192,
        1.3000462
      ],
      [
        103.8403836,
        1.3001321
      ],
      [
        103.8404372,
        1.3002018
      ],
      [
        103.8404855,
        1.3002876
      ],
      [
        103.8405606,
        1.300368
      ],
      [
        103.8406143,
        1.300427
      ],
      [
        103.8406411,
        1.3005128
      ],
      [
        103.8406303,
        1.3005986
      ],
      [
        103.8405767,
        1.300663
      ],
      [
        103.8404855,
        1.3007005
      ],
      [
        103.8403836,
        1.3007327
      ],
      [
        103.8402763,
        1.3007595
      ],
      [
        103.8401583,
        1.3007917
      ],
      [
        103.8400724,
        1.3008185
      ],
      [
        103.8399544,
        1.3008507
      ],
      [
        103.8398364,
        1.3008775
      ],
      [
        103.8397103,
        1.3009096
      ],
      [
        103.8395923,
        1.3009525
      ],
      [
        103.8394314,
        1.300974
      ],
      [
        103.8392597,
        1.3009311
      ],
      [
        103.8390452,
        1.3012099
      ],
      [
        103.8389271,
        1.3012743
      ],
      [
        103.8387447,
        1.3013386
      ],
      [
        103.8386375,
        1.3014137
      ],
      [
        103.8385194,
        1.3014781
      ],
      [
        103.83838,
        1.3015317
      ],
      [
        103.8382298,
        1.3015853
      ],
      [
        103.8381439,
        1.3016604
      ],
      [
        103.8379294,
        1.3017141
      ],
      [
        103.8377577,
        1.3017999
      ],
      [
        103.837586,
        1.3018428
      ],
      [
        103.837468,
        1.3017355
      ],
      [
        103.8373285,
        1.3016497
      ],
      [
        103.8372642,
        1.3015961
      ],
      [
        103.8371676,
        1.3014995
      ],
      [
        103.8370603,
        1.3013923
      ],
      [
        103.836953,
        1.301285
      ],
      [
        103.8368457,
        1.3011778
      ],
      [
        103.8367277,
        1.3010705
      ],
      [
        103.8366312,
        1.3009418
      ],
      [
        103.8365239,
        1.3007916
      ],
      [
        103.8364273,
        1.3007165
      ],
      [
        103.8363093,
        1.3005985
      ],
      [
        103.8361591,
        1.3004698
      ],
      [
        103.8360518,
        1.3003626
      ],
      [
        103.8358801,
        1.3002339
      ],
      [
        103.8359767,
        1.3001051
      ],
      [
        103.8361806,
        1.3000837
      ],
      [
        103.8363093,
        1.3000301
      ],
      [
        103.836438,
        1.299955
      ],
      [
        103.8365668,
        1.2999014
      ],
      [
        103.8367492,
        1.299837
      ],
      [
        103.8370067,
        1.2998155
      ],
      [
        103.8371998,
        1.2997512
      ],
      [
        103.8373929,
        1.2996439
      ],
      [
        103.8374573,
        1.2994401
      ],
      [
        103.8375217,
        1.2992685
      ],
      [
        103.8375753,
        1.2990862
      ],
      [
        103.8376182,
        1.2988716
      ],
      [
        103.8377148,
        1.2986679
      ],
      [
        103.8377792,
        1.2984962
      ],
      [
        103.8378221,
        1.2982817
      ],
      [
        103.8378864,
        1.2980886
      ],
      [
        103.8379294,
        1.2979063
      ],
      [
        103.8380152,
        1.297724
      ],
      [
        103.8381117,
        1.2975523
      ]
    ]
  ],
  "type": "Polygon"
}

# singtel - orchard road

{
  "coordinates": [
    [
      [
        103.838248,
        1.2975974
      ],
      [
        103.83816,
        1.2974668
      ],
      [
        103.8381064,
        1.2973595
      ],
      [
        103.8380635,
        1.2971986
      ],
      [
        103.8379884,
        1.297027
      ],
      [
        103.8379025,
        1.2968661
      ],
      [
        103.8377631,
        1.2967052
      ],
      [
        103.837688,
        1.2965443
      ],
      [
        103.8375485,
        1.2964049
      ],
      [
        103.8374412,
        1.2962547
      ],
      [
        103.8373768,
        1.2960831
      ],
      [
        103.8374305,
        1.2958364
      ],
      [
        103.8374948,
        1.2956434
      ],
      [
        103.8375592,
        1.2954503
      ],
      [
        103.8376236,
        1.2953001
      ],
      [
        103.8376021,
        1.29515
      ],
      [
        103.8375699,
        1.2950641
      ],
      [
        103.8375699,
        1.2949354
      ],
      [
        103.8374948,
        1.2946995
      ],
      [
        103.8374412,
        1.2944957
      ],
      [
        103.8373768,
        1.2943562
      ],
      [
        103.8372803,
        1.2942275
      ],
      [
        103.8372695,
        1.2940452
      ],
      [
        103.8372159,
        1.2939272
      ],
      [
        103.8371301,
        1.2937556
      ],
      [
        103.8370979,
        1.2935947
      ],
      [
        103.8370871,
        1.2934767
      ],
      [
        103.8370657,
        1.2932729
      ],
      [
        103.8370871,
        1.293112
      ],
      [
        103.8371193,
        1.2929404
      ],
      [
        103.8371837,
        1.292758
      ],
      [
        103.8372588,
        1.2925971
      ],
      [
        103.8373554,
        1.2924362
      ],
      [
        103.8375056,
        1.2922432
      ],
      [
        103.8376343,
        1.2920823
      ],
      [
        103.8377631,
        1.2920394
      ],
      [
        103.8378918,
        1.291975
      ],
      [
        103.8380635,
        1.2919536
      ],
      [
        103.8381815,
        1.2918678
      ],
      [
        103.8384068,
        1.2918463
      ],
      [
        103.8385248,
        1.2916211
      ],
      [
        103.8386536,
        1.2914602
      ],
      [
        103.8387716,
        1.2912778
      ],
      [
        103.8388145,
        1.2911491
      ],
      [
        103.839072,
        1.2911598
      ],
      [
        103.8391793,
        1.291192
      ],
      [
        103.8393402,
        1.2912242
      ],
      [
        103.8395226,
        1.2912564
      ],
      [
        103.8396621,
        1.2913315
      ],
      [
        103.8397908,
        1.2915031
      ],
      [
        103.8399839,
        1.291546
      ],
      [
        103.8401127,
        1.291664
      ],
      [
        103.8402414,
        1.2917391
      ],
      [
        103.8403273,
        1.2918463
      ],
      [
        103.8404453,
        1.2918999
      ],
      [
        103.8406062,
        1.2920179
      ],
      [
        103.8406706,
        1.2921681
      ],
      [
        103.840574,
        1.2922754
      ],
      [
        103.8404131,
        1.2924792
      ],
      [
        103.8403058,
        1.2925864
      ],
      [
        103.8402092,
        1.2927151
      ],
      [
        103.8401019,
        1.2928117
      ],
      [
        103.8399732,
        1.2929618
      ],
      [
        103.839823,
        1.2930798
      ],
      [
        103.8396943,
        1.2931871
      ],
      [
        103.8395011,
        1.2933801
      ],
      [
        103.8394582,
        1.293541
      ],
      [
        103.8395762,
        1.2935732
      ],
      [
        103.8396728,
        1.2935518
      ],
      [
        103.8397694,
        1.293466
      ],
      [
        103.8398766,
        1.2933587
      ],
      [
        103.8399947,
        1.2932729
      ],
      [
        103.8401449,
        1.2931442
      ],
      [
        103.8402736,
        1.2930584
      ],
      [
        103.840456,
        1.2928867
      ],
      [
        103.8406277,
        1.292758
      ],
      [
        103.8407671,
        1.29264
      ],
      [
        103.8409603,
        1.2925113
      ],
      [
        103.8410997,
        1.2925221
      ],
      [
        103.8411641,
        1.2926079
      ],
      [
        103.8412392,
        1.2927688
      ],
      [
        103.841325,
        1.2928867
      ],
      [
        103.8414109,
        1.292994
      ],
      [
        103.8414752,
        1.2931549
      ],
      [
        103.8415933,
        1.2932836
      ],
      [
        103.8417005,
        1.293466
      ],
      [
        103.8418078,
        1.2935839
      ],
      [
        103.8419151,
        1.2937019
      ],
      [
        103.8419795,
        1.2937985
      ],
      [
        103.8420567,
        1.2939399
      ],
      [
        103.8421425,
        1.2941007
      ],
      [
        103.8421104,
        1.2943045
      ],
      [
        103.8420353,
        1.2944654
      ],
      [
        103.8419602,
        1.2946049
      ],
      [
        103.841885,
        1.2947979
      ],
      [
        103.8418099,
        1.2949267
      ],
      [
        103.8417134,
        1.2950875
      ],
      [
        103.8416168,
        1.2952484
      ],
      [
        103.841531,
        1.2953771
      ],
      [
        103.841413,
        1.295538
      ],
      [
        103.8412628,
        1.2956668
      ],
      [
        103.8411126,
        1.2958491
      ],
      [
        103.8409195,
        1.2958813
      ],
      [
        103.8407692,
        1.2959456
      ],
      [
        103.8405654,
        1.2960636
      ],
      [
        103.840619,
        1.2962352
      ],
      [
        103.8406727,
        1.2963639
      ],
      [
        103.8407478,
        1.2966106
      ],
      [
        103.8408229,
        1.2968359
      ],
      [
        103.8408551,
        1.2970826
      ],
      [
        103.8407156,
        1.2971791
      ],
      [
        103.8406083,
        1.2971362
      ],
      [
        103.8404688,
        1.2970933
      ],
      [
        103.840265,
        1.2970933
      ],
      [
        103.8401041,
        1.2970826
      ],
      [
        103.8399431,
        1.2971148
      ],
      [
        103.8397929,
        1.2971577
      ],
      [
        103.8396856,
        1.2971899
      ],
      [
        103.839514,
        1.2972971
      ],
      [
        103.8393852,
        1.2973507
      ],
      [
        103.8392028,
        1.2974473
      ],
      [
        103.8390741,
        1.2975331
      ],
      [
        103.8389561,
        1.2975974
      ],
      [
        103.8387951,
        1.2976833
      ],
      [
        103.8386557,
        1.2977798
      ],
      [
        103.8384947,
        1.2978441
      ],
      [
        103.8383553,
        1.2977262
      ],
      [
        103.838248,
        1.2975974
      ]
    ]
  ],
  "type": "Polygon"
}
# singtel bottom right

