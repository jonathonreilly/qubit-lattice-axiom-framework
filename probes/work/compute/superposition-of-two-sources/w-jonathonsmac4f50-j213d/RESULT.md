superposition-of-two-sources, independent run 2 of 2
worker w-jonathonsmac4f50-j213d (claude-opus-5), unit C-superposition-of-two-sources-a2

SETUP
  probes/lib/formation_response.py, copied beside run.py, with a second source at d e1.
  Light-cone past (dim 3s, n = 7), L = 32, T = 2000, T0 = 800, seed 1, aligned start.
  Ten copies share every random number: no field; A (+h at the origin); B(d, sign) (sign*h at d e1); AB(d, sign).
  delta_X(x) = mean over 800 < t <= 2000 of (s_X - s_0).t1, spatial mean removed.
  S = delta_A + delta_B,  N = delta_AB - delta_A - delta_B.
  beta = 3, 6; d = 4, 8; both signs; h = 0.5, 2 (the task) and 8, 32 (added to locate the failure).

LARGEST max|N|/max|S| over beta, d and sign
  h = 0.5 : 0.0002
  h = 2   : 0.0033
  h = 8   : 0.0325
  h = 32  : 0.0853

BY CASE: beta h d sign | max|N|/max|S| | ||N||/||S|| | the two half-windows
  3 0.5 4 + | 0.0002 | 0.0001 | 0.0001 0.0003      6 0.5 4 + | 0.0001 | 0.0000 | 0.0001 0.0001
  3 0.5 4 - | 0.0002 | 0.0003 | 0.0003 0.0002      6 0.5 4 - | 0.0001 | 0.0001 | 0.0001 0.0001
  3 0.5 8 + | 0.0002 | 0.0001 | 0.0001 0.0003      6 0.5 8 + | 0.0001 | 0.0000 | 0.0000 0.0001
  3 0.5 8 - | 0.0001 | 0.0001 | 0.0001 0.0001      6 0.5 8 - | 0.0000 | 0.0000 | 0.0000 0.0000
  3 2   4 + | 0.0032 | 0.0020 | 0.0028 0.0036      6 2   4 + | 0.0008 | 0.0005 | 0.0007 0.0009
  3 2   4 - | 0.0033 | 0.0024 | 0.0033 0.0033      6 2   4 - | 0.0009 | 0.0006 | 0.0009 0.0008
  3 2   8 + | 0.0020 | 0.0012 | 0.0015 0.0026      6 2   8 + | 0.0006 | 0.0003 | 0.0004 0.0007
  3 2   8 - | 0.0010 | 0.0007 | 0.0011 0.0010      6 2   8 - | 0.0002 | 0.0001 | 0.0003 0.0002
  3 8   4 + | 0.0314 | 0.0224 | 0.0288 0.0339      6 8   4 + | 0.0114 | 0.0079 | 0.0103 0.0124
  3 8   4 - | 0.0325 | 0.0259 | 0.0307 0.0342      6 8   4 - | 0.0113 | 0.0087 | 0.0108 0.0118
  3 8   8 + | 0.0159 | 0.0112 | 0.0132 0.0187      6 8   8 + | 0.0060 | 0.0040 | 0.0049 0.0071
  3 8   8 - | 0.0144 | 0.0108 | 0.0126 0.0162      6 8   8 - | 0.0048 | 0.0036 | 0.0044 0.0053
  3 32  4 + | 0.0753 | 0.0521 | 0.0710 0.0797      6 32  4 + | 0.0572 | 0.0405 | 0.0530 0.0615
  3 32  4 - | 0.0853 | 0.0663 | 0.0802 0.0904      6 32  4 - | 0.0630 | 0.0501 | 0.0587 0.0674
  3 32  8 + | 0.0377 | 0.0261 | 0.0314 0.0440      6 32  8 + | 0.0287 | 0.0203 | 0.0243 0.0331
  3 32  8 - | 0.0404 | 0.0277 | 0.0341 0.0467      6 32  8 - | 0.0291 | 0.0213 | 0.0249 0.0332

PROFILES (beta = 3, d = 4, same sign; x: S/N)
  h = 0.5, along e1:
    -4: +0.00273/+0.000000   -2: +0.00699/+0.000000   0: +0.04249/+0.000006
     2: +0.01178/+0.000001    4: +0.04275/-0.000008   6: +0.00694/-0.000001   8: +0.00273/-0.000001
  h = 0.5, perpendicular through the midpoint (x2):
     0: +0.01178/+0.000001    1: +0.00949/+0.000001   2: +0.00690/+0.000000
     4: +0.00356/-0.000000    8: +0.00098/-0.000000
  h = 2, along e1:
    -4: +0.01083/-0.000018   -2: +0.02772/-0.000048   0: +0.16883/-0.000335
     2: +0.04668/-0.000073    4: +0.16851/-0.000541   6: +0.02742/-0.000070   8: +0.01078/-0.000027
  h = 2, perpendicular through the midpoint (x2):
     0: +0.04668/-0.000073    1: +0.03757/-0.000062   2: +0.02734/-0.000042
     4: +0.01408/-0.000024    8: +0.00387/-0.000007
  N has the opposite sign to S at h = 2: the two sources together give slightly less than their sum.

SINGLE SOURCE, delta_A at the source site (saturation of one source)
  beta = 3:  h = 0.5: 0.040305   h = 2: 0.160193   h = 8: 0.539562   h = 32: 0.926958
             4h would give 0.161220 at h = 2 (0.64 % low), 0.644880 at h = 8 (16 % low), 2.16 at h = 32
  beta = 6:  h = 0.5: 0.020311   h = 2: 0.081188   h = 8: 0.309426   h = 32: 0.772631

READING
  At h = 0.5 the sources add: the defect is at most 0.02 % of the summed field, far inside the task's 2 %.
  At h = 2 the defect is still at most 0.33 %, which is the task's expectation of "visible saturation at h = 2" not met.
    The single-source response at h = 2 is only 0.64 % below four times its h = 0.5 value, so one source is barely saturated there either.
  Additivity first breaks the 2 % line at h = 8 (3.25 % at beta = 3, d = 4), and reaches 8.5 % at h = 32.
  The defect is larger at the smaller separation d = 4 than at d = 8, and larger at beta = 3 than at beta = 6, in every case.
  The sign of the second source does not matter much: same and opposite signs give the same defect to within 10 %.
  The two half-windows of the time average agree to within about 20 % of the defect, so these are not noise.
