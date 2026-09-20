static-against-lightcone-kernel, independent run 2 of 2
worker w-jonathonsmac4f50-j4b4c (claude-opus-5), unit C-static-against-lightcone-kernel-a2

The comparator is the sphere static law (weight e^{beta s.s'}, heat bath on 16^3, probes/lib/block29_kernel.py).
The formation law is the light-cone reading on the 3+1 event lattice: n = 7 predecessors, symbol
phi(k) = (1 + 2 sum_j cos k_j)/7 (probes/lib/formation_levelplane.py, mode "3s sphere").
Overlap disclosure: the factor 14 - E below is the same one that appears in my runs of C:two-pin-interaction-linear:a2
and C:linear-kernel-3plus1:a2; the matching, the drift measurement and the frame algebra are new here.

(1) THE TWO KERNELS ARE THE SAME FUNCTION OF E (exact, sympy, general k)
  1 - phi(k)      = E(k)/7                      E(k) = 2 sum_j (1 - cos k_j), in [0, 12]
  1 - |phi(k)|^2  = E(k)(14 - E(k))/49
  (7/2)(1 - |phi(k)|^2)/E(k) = 1 - E(k)/14
  In static units the light-cone kernel is therefore the static kernel times 1 - E/14: equal as E -> 0, 6/7 at
  E = 2, 1/7 at the zone corner. Verified on the whole L = 16 grid to 3.3e-16.

(2) SPIN-WAVE MATCHING (exact condition, solved to 1e-12)
  S_static ~ 1/(beta_s E),  S_form ~ sigma^2/(1 - |phi|^2) = (7 sigma^2/2)/E / (1 - E/14),  sigma^2 = A(7 beta_f)/(7 beta_f)
  equal amplitudes as k -> 0  <=>  sigma^2 = 2/(7 beta_s)  <=>  beta_s = 2 beta_f / A(7 beta_f)
  beta_s=1.00 -> stiffness-matched beta_f=0.234045 (sigma^2=0.285714, residual +2.22e-16)
  beta_s=1.50 -> stiffness-matched beta_f=0.558895 (sigma^2=0.190476, residual +0.00e+00)
  beta_s=2.00 -> stiffness-matched beta_f=0.827350 (sigma^2=0.142857, residual +0.00e+00)
  beta_s=3.00 -> stiffness-matched beta_f=1.340097 (sigma^2=0.095238, residual -4.44e-16)
  Matching the long-wave amplitude and matching the magnetization are different requests: at these couplings the
  light-cone law is much less magnetized, and the first two are at or below its ordering threshold on this box.
  at the stiffness-matched coupling beta_f=0.2340 the light-cone law gives |m|=0.0162, against m_static=0.6885 at beta_s=1.00
  at the stiffness-matched coupling beta_f=0.5589 the light-cone law gives |m|=0.2364, against m_static=0.8164 at beta_s=1.50
  at the stiffness-matched coupling beta_f=0.8274 the light-cone law gives |m|=0.6971, against m_static=0.8684 at beta_s=2.00
  at the stiffness-matched coupling beta_f=1.3401 the light-cone law gives |m|=0.8379, against m_static=0.9153 at beta_s=3.00
  Conversely, at the magnetization-matched couplings of section 3 the formation law's k -> 0 amplitude is
  0.510, 0.552, 0.560, 0.568 of the static law's (7 sigma^2 beta_s/2).

(3) MAGNETIZATION MATCHED BY BISECTION (10 steps on [0.55, 4], same seed and length as the measured run)
  beta_s=1.00: matched beta_f=0.8061, |m|_form=0.6848 vs m_static=0.6885 (difference -0.0037, within 0.01: True); the stiffness-matched coupling would be beta_f=0.2340
  beta_s=1.50: matched beta_f=1.1969, |m|_form=0.8145 vs m_static=0.8164 (difference -0.0019, within 0.01: True); the stiffness-matched coupling would be beta_f=0.5589
  beta_s=2.00: matched beta_f=1.6281, |m|_form=0.8704 vs m_static=0.8684 (difference +0.0020, within 0.01: True); the stiffness-matched coupling would be beta_f=0.8274
  beta_s=3.00: matched beta_f=2.4906, |m|_form=0.9187 vs m_static=0.9153 (difference +0.0034, within 0.01: True); the stiffness-matched coupling would be beta_f=1.3401

(4) THE STATIC COMPARATOR, probes/lib/block29_kernel.py 16 3000 500 1.0 1.5 2.0 3.0
  sphere static law, L=16, sweeps=3000 (thermalisation 500); k = 2 pi n/L along e_1; E(k) = 2(1 - cos k)
    beta=1.00: m = 0.6885, m^2 = 0.4740, (m^2/3)^2 = 0.0250   (3s)
      n  beta E(k) S_perp(k): 0.805 0.929 0.920 0.943 0.926 0.933 0.927 0.899
      T(r) r=0..8: 0.2215 0.0657 0.0261 0.0123 0.0060 0.0026 0.0008 -0.0001 -0.0004
    beta=1.50: m = 0.8164, m^2 = 0.6664, (m^2/3)^2 = 0.0493   (3s)
      n  beta E(k) S_perp(k): 0.895 0.873 0.967 0.939 0.950 0.945 0.924 0.979
      T(r) r=0..8: 0.1513 0.0456 0.0184 0.0090 0.0047 0.0023 0.0009 0.0001 -0.0001
    beta=2.00: m = 0.8684, m^2 = 0.7541, (m^2/3)^2 = 0.0632   (3s)
      n  beta E(k) S_perp(k): 0.940 0.981 0.956 0.990 0.948 0.977 0.937 1.005
      T(r) r=0..8: 0.1148 0.0345 0.0138 0.0066 0.0033 0.0015 0.0005 0.0001 -0.0001
    beta=3.00: m = 0.9153, m^2 = 0.8378, (m^2/3)^2 = 0.0780   (3s)
      n  beta E(k) S_perp(k): 0.958 0.985 0.981 0.960 0.946 0.994 0.946 0.975
      T(r) r=0..8: 0.0776 0.0234 0.0094 0.0045 0.0022 0.0010 0.0003 -0.0001 -0.0002

(5) THE FORMATION LAW AT THE MATCHED COUPLINGS, probes/lib/formation_levelplane.py 3s sphere <beta_f> 16 6000 2000 7
  beta_s=1.00 | dim=3 (event lattice Z^4) menu=sphere beta=0.8061 L=16 T=6000 T0=2000 seed=7; predecessors n=7; sigma^2=0.145818
  beta_s=1.00 | |k| in [0.3,0.6): 0.7793 (n=18)
  beta_s=1.00 | |k| in [0.6,1.0): 0.7914 (n=62)
  beta_s=1.00 | |k| in [1.0,1.5): 0.8474 (n=170)
  beta_s=1.00 | |k| in [1.5,2.2): 0.8873 (n=488)
  beta_s=1.00 | |k| in [2.2,3.2): 0.9215 (n=1535)
  beta_s=1.00 | |k| in [3.2,6.0): 0.9214 (n=1822)
  beta_s=1.00 | SUMMARY: dim=3 menu=sphere beta=0.8061 L=16 T=6000 plateau_|m|=0.6849 lowk_ratio=0.7793 seconds=3
  beta_s=1.50 | dim=3 (event lattice Z^4) menu=sphere beta=1.1969 L=16 T=6000 T0=2000 seed=7; predecessors n=7; sigma^2=0.105110
  beta_s=1.50 | |k| in [0.3,0.6): 0.8959 (n=18)
  beta_s=1.50 | |k| in [0.6,1.0): 0.8770 (n=62)
  beta_s=1.50 | |k| in [1.0,1.5): 0.9034 (n=170)
  beta_s=1.50 | |k| in [1.5,2.2): 0.9125 (n=488)
  beta_s=1.50 | |k| in [2.2,3.2): 0.9241 (n=1535)
  beta_s=1.50 | |k| in [3.2,6.0): 0.9238 (n=1822)
  beta_s=1.50 | SUMMARY: dim=3 menu=sphere beta=1.1969 L=16 T=6000 plateau_|m|=0.8145 lowk_ratio=0.8959 seconds=3
  beta_s=2.00 | dim=3 (event lattice Z^4) menu=sphere beta=1.6281 L=16 T=6000 T0=2000 seed=7; predecessors n=7; sigma^2=0.080046
  beta_s=2.00 | |k| in [0.3,0.6): 0.9402 (n=18)
  beta_s=2.00 | |k| in [0.6,1.0): 0.9131 (n=62)
  beta_s=2.00 | |k| in [1.0,1.5): 0.9328 (n=170)
  beta_s=2.00 | |k| in [1.5,2.2): 0.9343 (n=488)
  beta_s=2.00 | |k| in [2.2,3.2): 0.9397 (n=1535)
  beta_s=2.00 | |k| in [3.2,6.0): 0.9393 (n=1822)
  beta_s=2.00 | SUMMARY: dim=3 menu=sphere beta=1.6281 L=16 T=6000 plateau_|m|=0.8704 lowk_ratio=0.9402 seconds=3
  beta_s=3.00 | dim=3 (event lattice Z^4) menu=sphere beta=2.4906 L=16 T=6000 T0=2000 seed=7; predecessors n=7; sigma^2=0.054069
  beta_s=3.00 | |k| in [0.3,0.6): 0.9742 (n=18)
  beta_s=3.00 | |k| in [0.6,1.0): 0.9430 (n=62)
  beta_s=3.00 | |k| in [1.0,1.5): 0.9592 (n=170)
  beta_s=3.00 | |k| in [1.5,2.2): 0.9567 (n=488)
  beta_s=3.00 | |k| in [2.2,3.2): 0.9588 (n=1535)
  beta_s=3.00 | |k| in [3.2,6.0): 0.9583 (n=1822)
  beta_s=3.00 | SUMMARY: dim=3 menu=sphere beta=2.4906 L=16 T=6000 plateau_|m|=0.9187 lowk_ratio=0.9742 seconds=3

(6) SHELL BY SHELL, SAME SHELLS AND THE SAME TRANSVERSE FRAME FOR BOTH LAWS
  R_static   = beta_s E(k) S_static(k)                (1 in static spin-wave theory; <= 1 by the infrared bound)
  R_form     = S_form(k)(1 - |phi|^2)/sigma^2         (1 in the linear gain-one theory, sigma^2 = A(7 beta_f)/(7 beta_f))
  R_form_eff = the same against the noise the law actually injects, <A(kappa)/kappa> at kappa = beta_f |S(x)|
  Errors are standard errors over 4 measurement blocks. Parseval holds to 6 decimals in every run, and my
  R_static reproduces block29_kernel.py's printed axis line digit for digit (same seed and sweeps).
  beta_s=1.00 m=0.6885 | beta_f=0.8061 |m|=0.6848 (difference -0.0036) | sigma^2=0.145824 sigma^2_eff=0.179438 (ratio 1.2305), <|S|>/7=0.7640
  beta_s=1.00 Parseval check: static sum_k S/N = 0.221527 vs <|s_perp|^2>/2 = 0.221527; formation 0.222679 vs 0.222678
  beta_s=1.00 k->0 amplitude ratio S_form/S_static = 7 sigma^2 beta_s/2 = 0.5104
  beta_s=1.00 direction drift over the measured levels: <cos^2 theta> = 0.2612 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.6306
  beta_s=1.00 measured fixed/instantaneous ratio by shell: 0.6599 0.6948 0.7324 0.7689 0.7971 0.7977  | predicted 0.6306, largest deviation 0.1672
  beta_s=1.50 m=0.8167 | beta_f=1.1969 |m|=0.8145 (difference -0.0022) | sigma^2=0.105112 sigma^2_eff=0.119821 (ratio 1.1399), <|S|>/7=0.8606
  beta_s=1.50 Parseval check: static sum_k S/N = 0.151106 vs <|s_perp|^2>/2 = 0.151106; formation 0.152435 vs 0.152435
  beta_s=1.50 k->0 amplitude ratio S_form/S_static = 7 sigma^2 beta_s/2 = 0.5518
  beta_s=1.50 direction drift over the measured levels: <cos^2 theta> = 0.5929 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.7965
  beta_s=1.50 measured fixed/instantaneous ratio by shell: 0.8062 0.8143 0.8254 0.8368 0.8466 0.8470  | predicted 0.7965, largest deviation 0.0506
  beta_s=2.00 m=0.8685 | beta_f=1.6281 |m|=0.8704 (difference +0.0020) | sigma^2=0.080044 sigma^2_eff=0.087899 (ratio 1.0981), <|S|>/7=0.9026
  beta_s=2.00 Parseval check: static sum_k S/N = 0.114755 vs <|s_perp|^2>/2 = 0.114755; formation 0.113268 vs 0.113268
  beta_s=2.00 k->0 amplitude ratio S_form/S_static = 7 sigma^2 beta_s/2 = 0.5603
  beta_s=2.00 direction drift over the measured levels: <cos^2 theta> = 0.7189 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.8595
  beta_s=2.00 measured fixed/instantaneous ratio by shell: 0.8649 0.8678 0.8728 0.8781 0.8828 0.8830  | predicted 0.8595, largest deviation 0.0236
  beta_s=3.00 m=0.9155 | beta_f=2.4906 |m|=0.9187 (difference +0.0032) | sigma^2=0.054068 sigma^2_eff=0.057396 (ratio 1.0615), <|S|>/7=0.9389
  beta_s=3.00 Parseval check: static sum_k S/N = 0.077483 vs <|s_perp|^2>/2 = 0.077483; formation 0.074820 vs 0.074820
  beta_s=3.00 k->0 amplitude ratio S_form/S_static = 7 sigma^2 beta_s/2 = 0.5677
  beta_s=3.00 direction drift over the measured levels: <cos^2 theta> = 0.8249 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.9125
  beta_s=3.00 measured fixed/instantaneous ratio by shell: 0.9151 0.9157 0.9176 0.9195 0.9213 0.9214  | predicted 0.9125, largest deviation 0.0089
    beta_s=1.00 |k| in [0.3,0.6) n=  18: R_static=0.8946+-0.0075  R_form=1.1650+-0.0037  R_form_eff=0.9467  (driver's fixed frame 0.7688)  R_form-R_static=+0.2704
    beta_s=1.00 |k| in [0.6,1.0) n=  62: R_static=0.9220+-0.0010  R_form=1.1294+-0.0041  R_form_eff=0.9178  (driver's fixed frame 0.7848)  R_form-R_static=+0.2074
    beta_s=1.00 |k| in [1.0,1.5) n= 170: R_static=0.9241+-0.0020  R_form=1.1491+-0.0043  R_form_eff=0.9339  (driver's fixed frame 0.8417)  R_form-R_static=+0.2250
    beta_s=1.00 |k| in [1.5,2.2) n= 488: R_static=0.9300+-0.0007  R_form=1.1477+-0.0004  R_form_eff=0.9327  (driver's fixed frame 0.8825)  R_form-R_static=+0.2176
    beta_s=1.00 |k| in [2.2,3.2) n=1535: R_static=0.9342+-0.0005  R_form=1.1508+-0.0005  R_form_eff=0.9352  (driver's fixed frame 0.9173)  R_form-R_static=+0.2166
    beta_s=1.00 |k| in [3.2,6.0) n=1822: R_static=0.9391+-0.0006  R_form=1.1496+-0.0003  R_form_eff=0.9343  (driver's fixed frame 0.9171)  R_form-R_static=+0.2105
    beta_s=1.50 |k| in [0.3,0.6) n=  18: R_static=0.9292+-0.0047  R_form=1.1113+-0.0040  R_form_eff=0.9749  (driver's fixed frame 0.8959)  R_form-R_static=+0.1821
    beta_s=1.50 |k| in [0.6,1.0) n=  62: R_static=0.9483+-0.0020  R_form=1.0769+-0.0049  R_form_eff=0.9447  (driver's fixed frame 0.8770)  R_form-R_static=+0.1286
    beta_s=1.50 |k| in [1.0,1.5) n= 170: R_static=0.9479+-0.0025  R_form=1.0945+-0.0039  R_form_eff=0.9602  (driver's fixed frame 0.9034)  R_form-R_static=+0.1466
    beta_s=1.50 |k| in [1.5,2.2) n= 488: R_static=0.9511+-0.0008  R_form=1.0904+-0.0002  R_form_eff=0.9565  (driver's fixed frame 0.9125)  R_form-R_static=+0.1393
    beta_s=1.50 |k| in [2.2,3.2) n=1535: R_static=0.9528+-0.0004  R_form=1.0915+-0.0004  R_form_eff=0.9575  (driver's fixed frame 0.9241)  R_form-R_static=+0.1387
    beta_s=1.50 |k| in [3.2,6.0) n=1822: R_static=0.9553+-0.0006  R_form=1.0906+-0.0003  R_form_eff=0.9567  (driver's fixed frame 0.9238)  R_form-R_static=+0.1354
    beta_s=2.00 |k| in [0.3,0.6) n=  18: R_static=0.9441+-0.0049  R_form=1.0871+-0.0046  R_form_eff=0.9900  (driver's fixed frame 0.9402)  R_form-R_static=+0.1430
    beta_s=2.00 |k| in [0.6,1.0) n=  62: R_static=0.9621+-0.0022  R_form=1.0522+-0.0051  R_form_eff=0.9582  (driver's fixed frame 0.9131)  R_form-R_static=+0.0901
    beta_s=2.00 |k| in [1.0,1.5) n= 170: R_static=0.9608+-0.0027  R_form=1.0687+-0.0038  R_form_eff=0.9732  (driver's fixed frame 0.9328)  R_form-R_static=+0.1079
    beta_s=2.00 |k| in [1.5,2.2) n= 488: R_static=0.9632+-0.0009  R_form=1.0640+-0.0002  R_form_eff=0.9689  (driver's fixed frame 0.9343)  R_form-R_static=+0.1008
    beta_s=2.00 |k| in [2.2,3.2) n=1535: R_static=0.9642+-0.0004  R_form=1.0645+-0.0004  R_form_eff=0.9694  (driver's fixed frame 0.9397)  R_form-R_static=+0.1003
    beta_s=2.00 |k| in [3.2,6.0) n=1822: R_static=0.9658+-0.0005  R_form=1.0638+-0.0003  R_form_eff=0.9687  (driver's fixed frame 0.9393)  R_form-R_static=+0.0980
    beta_s=3.00 |k| in [0.3,0.6) n=  18: R_static=0.9593+-0.0055  R_form=1.0645+-0.0052  R_form_eff=1.0028  (driver's fixed frame 0.9742)  R_form-R_static=+0.1052
    beta_s=3.00 |k| in [0.6,1.0) n=  62: R_static=0.9753+-0.0023  R_form=1.0298+-0.0052  R_form_eff=0.9701  (driver's fixed frame 0.9430)  R_form-R_static=+0.0544
    beta_s=3.00 |k| in [1.0,1.5) n= 170: R_static=0.9736+-0.0028  R_form=1.0454+-0.0037  R_form_eff=0.9848  (driver's fixed frame 0.9592)  R_form-R_static=+0.0717
    beta_s=3.00 |k| in [1.5,2.2) n= 488: R_static=0.9755+-0.0009  R_form=1.0405+-0.0002  R_form_eff=0.9802  (driver's fixed frame 0.9567)  R_form-R_static=+0.0650
    beta_s=3.00 |k| in [2.2,3.2) n=1535: R_static=0.9760+-0.0004  R_form=1.0408+-0.0004  R_form_eff=0.9804  (driver's fixed frame 0.9588)  R_form-R_static=+0.0648
    beta_s=3.00 |k| in [3.2,6.0) n=1822: R_static=0.9770+-0.0005  R_form=1.0401+-0.0003  R_form_eff=0.9798  (driver's fixed frame 0.9583)  R_form-R_static=+0.0631
    beta_s=1.00 axis k=(2 pi n/L,0,0) n=1..8 R_static: 0.805 0.929 0.920 0.943 0.926 0.933 0.928 0.899
    beta_s=1.00 axis k=(2 pi n/L,0,0) n=1..8 R_form  : 1.233 1.107 1.170 1.193 1.165 1.163 1.141 1.149
    beta_s=1.50 axis k=(2 pi n/L,0,0) n=1..8 R_static: 0.847 0.962 0.942 0.967 0.943 0.954 0.954 0.906
    beta_s=1.50 axis k=(2 pi n/L,0,0) n=1..8 R_form  : 1.167 1.056 1.116 1.141 1.105 1.108 1.083 1.093
    beta_s=2.00 axis k=(2 pi n/L,0,0) n=1..8 R_static: 0.854 0.978 0.957 0.980 0.955 0.968 0.970 0.917
    beta_s=2.00 axis k=(2 pi n/L,0,0) n=1..8 R_form  : 1.143 1.033 1.089 1.115 1.079 1.082 1.056 1.067
    beta_s=3.00 axis k=(2 pi n/L,0,0) n=1..8 R_static: 0.865 0.993 0.972 0.993 0.967 0.979 0.984 0.925
    beta_s=3.00 axis k=(2 pi n/L,0,0) n=1..8 R_form  : 1.120 1.012 1.064 1.092 1.056 1.058 1.032 1.044

(7) WHY THE FORMATION RATIO SITS ABOVE 1
  sigma^2 = A(7 beta_f)/(7 beta_f) is the noise of a vMF draw at concentration 7 beta_f, i.e. with the seven
  predecessors exactly aligned. The law draws at kappa = beta_f |S(x)| with <|S|>/7 = 0.764, 0.861, 0.903, 0.939
  at the four couplings, and A(kappa)/kappa is decreasing, so the injected noise is 1.231, 1.140, 1.098, 1.062
  times sigma^2. Dividing by that instead moves the lowest-shell ratio 1.165 -> 0.947, 1.111 -> 0.975,
  1.087 -> 0.990, 1.065 -> 1.003: closer to 1 in 7 of the 8 low-k shells and below 1 in 7 of 8.

(8) THE TWO DRIVERS DO NOT USE THE SAME TRANSVERSE FRAME (measured)
  block29_kernel.py projects on the instantaneous magnetization; formation_levelplane.py projects on the initial
  direction e0. For fluctuations transverse to a direction at angle theta from e0, a fixed axis t perpendicular
  to e0 sees variance sigma_T^2 (1 - (t.m)^2), so the two fixed axes together give sigma_T^2 (1 + cos^2 theta)/2.
  On the light-cone plane the direction random-walks away from e0 during the measurement window:
  beta_s=1.00 direction drift over the measured levels: <cos^2 theta> = 0.2612 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.6306
  beta_s=1.00 measured fixed/instantaneous ratio by shell: 0.6599 0.6948 0.7324 0.7689 0.7971 0.7977  | predicted 0.6306, largest deviation 0.1672
  beta_s=1.50 direction drift over the measured levels: <cos^2 theta> = 0.5929 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.7965
  beta_s=1.50 measured fixed/instantaneous ratio by shell: 0.8062 0.8143 0.8254 0.8368 0.8466 0.8470  | predicted 0.7965, largest deviation 0.0506
  beta_s=2.00 direction drift over the measured levels: <cos^2 theta> = 0.7189 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.8595
  beta_s=2.00 measured fixed/instantaneous ratio by shell: 0.8649 0.8678 0.8728 0.8781 0.8828 0.8830  | predicted 0.8595, largest deviation 0.0236
  beta_s=3.00 direction drift over the measured levels: <cos^2 theta> = 0.8249 -> predicted fixed/instantaneous frame bias (1+<cos^2>)/2 = 0.9125
  beta_s=3.00 measured fixed/instantaneous ratio by shell: 0.9151 0.9157 0.9176 0.9195 0.9213 0.9214  | predicted 0.9125, largest deviation 0.0089
  The small-fluctuation prediction matches the measured fixed/instantaneous ratio to 0.029 in the lowest shell at
  every coupling and to 0.009 across all shells at beta_s = 3; it degrades at large |k| and large drift.
  Consequence: the ratio printed by formation_levelplane.py is biased low by this factor - 0.63 at beta_f = 0.81
  on this box - and is not on the same footing as block29_kernel.py's. In its own frame the formation ratio comes
  out below 1 (0.769, 0.896, 0.940, 0.974 in the lowest shell), the same side as the static law; in the common
  frame it comes out above 1.

(9) HIT
  N4 low-k shells (|k| < 1.0) examined: 8; with the two corrections of opposite sign at more than 3 block errors each: 8
  N4   opposite sign: beta_s=1.00 |k| in [0.3,0.6): static 0.8946+-0.0075 (below 1), formation 1.1650+-0.0037 (above 1)
  N4   opposite sign: beta_s=1.00 |k| in [0.6,1.0): static 0.9220+-0.0010 (below 1), formation 1.1294+-0.0041 (above 1)
  N4   opposite sign: beta_s=1.50 |k| in [0.3,0.6): static 0.9292+-0.0047 (below 1), formation 1.1113+-0.0040 (above 1)
  N4   opposite sign: beta_s=1.50 |k| in [0.6,1.0): static 0.9483+-0.0020 (below 1), formation 1.0769+-0.0049 (above 1)
  N4   opposite sign: beta_s=2.00 |k| in [0.3,0.6): static 0.9441+-0.0049 (below 1), formation 1.0871+-0.0046 (above 1)
  N4   opposite sign: beta_s=2.00 |k| in [0.6,1.0): static 0.9621+-0.0022 (below 1), formation 1.0522+-0.0051 (above 1)
  N4   opposite sign: beta_s=3.00 |k| in [0.3,0.6): static 0.9593+-0.0055 (below 1), formation 1.0645+-0.0052 (above 1)
  N4   opposite sign: beta_s=3.00 |k| in [0.6,1.0): static 0.9753+-0.0023 (below 1), formation 1.0298+-0.0052 (above 1)
  N4 replacing sigma^2 by the injected noise moves the low-k formation ratio closer to 1 in 7 of 8 shells and puts it below 1 in 7 of 8
  N4 frame-bias prediction (1+<cos^2 theta>)/2, which is the small-fluctuation form: it matches the measured fixed/instantaneous ratio to 0.0294 in the lowest shell at every coupling and to 0.1672 over all shells, the deviation growing with |k| and with the drift (0.0089 over all shells at beta_s=3)
  SUMMARY: 1-|phi|^2 = E(14-E)/49 exactly (the light-cone kernel is the static one times 1-E/14); at |m| matched within 0.01 the low-k shells give R_static below 1 and R_form above 1 in 8 of 8 cases, e.g. beta_s=1.0 |k| in [0.3,0.6): 0.895+-0.007 against 1.165+-0.004 (0.947 against the injected noise), in 118s
  HIT: the two corrections do NOT have the same sign at small k. At magnetization matched within 0.01, beta_s E(k) S_static(k) sits below 1 (the infrared bound) while S_form(k)(1-|phi|^2)/sigma^2 sits above 1 in 8 of 8 low-k shells, each by more than three block errors; the formation excess is the calibration constant, since sigma^2 = A(7 beta_f)/(7 beta_f) assumes aligned predecessors while the law injects <A(kappa)/kappa> at kappa = beta_f |S| < 7 beta_f, and the ratio against that injected noise moves back towards 1 (see R_form_eff).

  The contradiction is with the expectation as stated - both ratios close to 1 with corrections of the same sign -
  and is a statement about those two named quantities. The kernels themselves agree exactly up to 1 - E/14
  (section 1). Numbers, not a verdict on the physics.
