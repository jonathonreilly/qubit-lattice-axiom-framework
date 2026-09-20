meanfield-threshold-by-dimension, independent run 2 of 2
worker w-jonathonsmac4f50-jdf97 (claude-opus-5), unit C-meanfield-threshold-by-dimension-a2

Where memory should appear, by dimension, in the two simplest approximations, for the sphere formation law with
n predecessors: n = d + 1 for the backward neighbourhood, n = 2d + 1 for the light cone.
Overlap disclosure: the identity 1 - |phi|^2 = E(14-E)/49 is the one I proved in C:static-against-lightcone-kernel:a2
and C:linear-kernel-3plus1:a2; everything else here is new.

(1) MEAN FIELD (exact)
  A(k) = coth k - 1/k = -k**7/4725 + 2*k**5/945 - k**3/45 + k/3 + O(k^8)
  mean field m' = A(n beta m): the slope at m = 0 is n beta/3, so a positive fixed point appears at n beta = 3
  A(k) = k/3 - k^3/45 + ...: coefficients 1/3 and -1/45
  so m = A(x m) with x = n beta has the positive root m^2 = 45(x/3 - 1)/x^3 to this order : True
  threshold table (exact):  d | backward n=d+1, beta_c=3/n | light-cone n=2d+1, beta_c=3/n
    d=1: backward n=2 beta_c=3/2 = 1.500000 | light-cone n=3 beta_c=1 = 1.000000
    d=2: backward n=3 beta_c=1 = 1.000000 | light-cone n=5 beta_c=3/5 = 0.600000
    d=3: backward n=4 beta_c=3/4 = 0.750000 | light-cone n=7 beta_c=3/7 = 0.428571
    d=4: backward n=5 beta_c=3/5 = 0.600000 | light-cone n=9 beta_c=1/3 = 0.333333
  The transition is continuous: m^2 = 45(n beta/3 - 1)/(n beta)^3 just above threshold.

(2) WHAT FIXES THE TWO PLANE RETURN SUMS (exact identities, sympy, general k)
  light-cone d=3 (n=7): 1 - |phi|^2 = E(14-E)/49 : True
  hence 1/(1-|phi|^2) = (7/2)(1/E + 1/(14-E)), so G_3 = (7/2)(<1/E> + <1/(14-E)>),
  where <1/E> = W/6 with W the simple-cubic Watson integral and <1/(14-E)> is a smooth average
  backward d=3 (n=4): 1 - |phi|^2 = (3/4)(1 - lambda), lambda the symbol of the uniform walk on the twelve
  vectors +-e_j, +-(e_i - e_j) : True
  so the backward walk is that face-centred-cubic walk held with probability 1/4, and G_3^bw = (4/3) G_FCC(0)
  Watson integral W = sqrt(6)/(32 pi^3) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24) = 1.5163860591519780182
  so <1/E> = W/6 = 0.25273100985866300303 (block 22 pinned 3<1/E> between 75/100 and 76/100 by exact terms)

(3) A RIGOROUS BRACKET FOR THE LIGHT-CONE G_3 (exact rational moments)
  1/(14-E) = (1/14) sum_j (E/14)^j with E/14 <= 6/7, so exact rational moments give a rigorous bracket:
    0.140931488 <= <1/(14-E)> <= 0.140931488  (J=200 terms, tail 1.75e-14)
  with block 22's rigorous 1/4 < <1/E> < 19/75 this gives
    1.368260 < G_3 light-cone < 1.379927
  and with the Watson value for <1/E>, G_3 light-cone = 1.377818743
  The bracket's width comes entirely from block 22's pin on <1/E>; the smooth part is exact to 1e-14.

(4) THE PLANE RETURN SUMS G_d (FFT-grid averaging, Richardson in 1/L)
  G_d = <1/(1-|phi|^2)> over the grid without the zero mode; Richardson assumes G_L = G_inf - c/L
  d=3 light-cone n=7: L=48:1.361354 L=64:1.365471 L=96:1.369587 L=128:1.371645 L=192:1.373703 L=256:1.374732
  d=3 light-cone n=7: Richardson (96,192) = 1.377819, (128,256) = 1.377819, difference 4.88e-08
  d=3 backward n=4: L=48:1.762474 L=64:1.770077 L=96:1.777679 L=128:1.781480 L=192:1.785280 L=256:1.787181
  d=3 backward n=4: Richardson (96,192) = 1.792882, (128,256) = 1.792882, difference 1.71e-07
  light-cone against A2/A3: 1.377819 vs 1.377819 (difference 3.57e-08)
  backward against the FCC constant 1.3446610: (4/3)*1.3446610 = 1.792881 vs 1.792882 (difference 3.69e-07)
  d=2 light-cone n=5: L=64:2.2566 L=128:2.5325 L=256:2.8083 L=512:3.0841 | successive differences 0.2759, 0.2758, 0.2758 (constant differences = log L growth)
  d=2 backward n=3: L=64:3.7921 L=128:4.3654 L=256:4.9386 L=512:5.5119 | successive differences 0.5733, 0.5732, 0.5732 (constant differences = log L growth)
  d=1 light-cone n=3: L=64:8.4272 L=128:16.4301 L=256:32.4315 L=512:64.4323 | ratios 1.9497, 1.9739, 1.9867 (2 = linear in L)
  d=1 backward n=2: L=64:21.3281 L=128:42.6641 L=256:85.3320 L=512:170.6660 | ratios 2.0004, 2.0001, 2.0000 (2 = linear in L)
  Two independent Richardson pairs agree to 5e-8 and 2e-7, the light-cone value agrees with the closed form of
  section 2 to 4e-8, and the backward value agrees with the published face-centred-cubic constant to 4e-7.
  d = 2 diverges logarithmically (equal successive differences under doubling) and d = 1 linearly (ratios 2),
  so there is no plateau to predict below three space dimensions.

(5) SPIN-WAVE PLATEAU 1 - sigma^2 G AGAINST THE EXECUTED SCANS
  sigma^2 = A(n beta)/(n beta); G_L is the same average on the box that was run, G_inf the extrapolated value.
  d=2 light-cone n=5 beta=2.0 L=256: executed |m|=0.6929 | spin wave 1-sigma^2 G_L=0.7473 (relative 7.8%), G_inf=nan | mean field 0.8873 | sigma^2=0.090000 G_L=2.8083  [X:formation-lightcone-sphere]
  d=3 backward n=4 beta=1.0 L=32: executed |m|=0.0155 | spin wave 1-sigma^2 G_L=0.6721 (relative 4236.1%), G_inf=0.6635 | mean field 0.5998 | sigma^2=0.187668 G_L=1.7473  [X:formation-3plus1-sphere-memory]
  d=3 backward n=4 beta=2.0 L=48: executed |m|=0.7366 | spin wave 1-sigma^2 G_L=0.8072 (relative 9.6%), G_inf=0.8039 | mean field 0.8536 | sigma^2=0.109375 G_L=1.7625  [X:formation-3plus1-seeds]
  d=3 backward n=4 beta=2.0 L=64: executed |m|=0.7354 | spin wave 1-sigma^2 G_L=0.8064 (relative 9.7%), G_inf=0.8039 | mean field 0.8536 | sigma^2=0.109375 G_L=1.7701  [X:formation-3plus1-finite-size]
  d=3 backward n=4 beta=24.0 L=64: executed |m|=0.9814 | spin wave 1-sigma^2 G_L=0.9818 (relative 0.0%), G_inf=0.9815 | mean field 0.9895 | sigma^2=0.010308 G_L=1.7701  [X:formation-3plus1-kernel]
  d=3 light-cone n=7 beta=0.4 L=64: executed |m|=0.0029 | spin wave 1-sigma^2 G_L=0.6829 (relative 23447.6%), G_inf=0.6800 | mean field 0.0000 | sigma^2=0.232243 G_L=1.3655  [X:formation-lightcone-sphere]
  d=3 light-cone n=7 beta=0.6 L=32: executed |m|=0.4146 | spin wave 1-sigma^2 G_L=0.7544 (relative 82.0%), G_inf=0.7499 | mean field 0.6345 | sigma^2=0.181513 G_L=1.3531  [X:formation-lightcone-sphere]
  d=3 light-cone n=7 beta=2.0 L=48: executed |m|=0.8946 | spin wave 1-sigma^2 G_L=0.9097 (relative 1.7%), G_inf=0.9086 | mean field 0.9226 | sigma^2=0.066327 G_L=1.3614  [X:formation-3plus1-seeds]
  the task's stated coupling: my own runs at beta = 6 on a 32^3 plane, T = 2000
  backward n=4 beta=6 L=32: executed |m| = 0.9237 vs spin wave 1 - sigma^2 G_L = 0.9302 (0.70%), mean field 0.9564, sigma^2 = 0.039931, G_L = 1.7473, G_inf gives 0.9284
  light-cone n=7 beta=6 L=32: executed |m| = 0.9669 vs spin wave 1 - sigma^2 G_L = 0.9685 (0.17%), mean field 0.9756, sigma^2 = 0.023243, G_L = 1.3531, G_inf gives 0.9680
  At beta = 24 the prediction is 0.04 percent from the executed plateau, at beta = 6 it is 0.70 percent
  (backward) and 0.17 percent (light cone); the executed backward value at beta = 6, 0.9237, matches the 0.92
  quoted in the task. At beta = 2 the error is about 10 percent (backward) and 1.7 percent (light cone), and near
  the threshold the linear theory is meaningless (it predicts 0.68 where the executed plateau is at the 0.003
  finite-size floor).

(6) WHERE THE THRESHOLD ACTUALLY IS
  threshold sweep on a 32^3 level plane, T = 2500 from an aligned start; the finite-size floor is about 0.02
  backward n=4 beta=0.75: plateau |m| = 0.0084 (mean field 0.0408)
  backward n=4 beta=0.90: plateau |m| = 0.0110 (mean field 0.5020)
  backward n=4 beta=1.10: plateau |m| = 0.0252 (mean field 0.6631)
  backward n=4 beta=1.30: plateau |m| = 0.4627 (mean field 0.7416)
  backward n=4 beta=1.50: plateau |m| = 0.6022 (mean field 0.7889)
  backward n=4: executed threshold between 1.1 and 1.3; mean field says 3/4 = 0.7500
  light-cone n=7 beta=0.43: plateau |m| = 0.0104 (mean field 0.0757)
  light-cone n=7 beta=0.48: plateau |m| = 0.0131 (mean field 0.4097)
  light-cone n=7 beta=0.52: plateau |m| = 0.0252 (mean field 0.5143)
  light-cone n=7 beta=0.56: plateau |m| = 0.2201 (mean field 0.5838)
  light-cone n=7 beta=0.60: plateau |m| = 0.4144 (mean field 0.6345)
  light-cone n=7: executed threshold between 0.52 and 0.56; mean field says 3/7 = 0.4286
  mean field below the executed bracket for both neighbourhoods: True

(7) VERDICT ON THE TASK'S EXPECTATIONS
  Mean field underestimates the threshold: 3/4 = 0.75 against an executed bracket (1.1, 1.3) for the backward
  neighbourhood, and 3/7 = 0.4286 against (0.52, 0.56) for the light cone - a factor 1.6 and 1.25 low.
  The spin-wave plateau is accurate to a few percent at beta >= 6: the worst of the three high-coupling points
  is 0.70 percent.
  N2/N3 high-coupling check: beta=24.0 L=64: executed 0.9814 vs spin wave 0.9818 (0.04%); beta=6.0 L=32: executed 0.9237 vs spin wave 0.9302 (0.70%); beta=6.0 L=32: executed 0.9669 vs spin wave 0.9685 (0.17%)
  SUMMARY: mean-field threshold is 3/n exactly (0.75 backward, 3/7 light-cone in d=3) and the executed brackets are (1.1,1.3) and (0.52,0.56), so mean field underestimates: True; G_3 = 1.792882 backward (= (4/3)G_FCC) and 1.377819 light-cone (= (7/2)(W/6 + <1/(14-E)>)), and the spin-wave plateau at beta >= 6 is within 0.70% of the executed value; 83s
  No HIT: both stated expectations hold. Numbers, not a verdict on the physics.
