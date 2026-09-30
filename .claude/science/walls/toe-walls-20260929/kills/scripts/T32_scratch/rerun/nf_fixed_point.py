"""Own two-loop check (independent of T30's script): SU(3) with n massless Dirac flavours.
dalpha/dln(mu) = -alpha^2/(2 pi) [ b0 + b1 alpha/(4 pi) ],  b0 = 11 - 2n/3,  b1 = 102 - 38 n/3.
Two-loop zero alpha* = -4 pi b0/b1 exists for 8.05 < n < 16.5 (b1 < 0, b0 > 0).
Repo bare coupling: alpha_bare = 1/(4 pi) = 0.0796 (g = 1); alpha_LM = 0.0907 (ALPHA_S_DERIVED_NOTE).
Reading: alpha* well below O(1) => the flow stops at a perturbative fixed point: conformal, no confinement, no gap.
alpha* near/above O(1) (~0.8, the ladder estimate of the chiral-breaking coupling is a RECALLED number) => walking/confining.
"""
import math
ab = 1/(4*math.pi)
print("alpha_bare = %.4f" % ab)
for n in (4, 6, 8, 10, 11, 12, 13, 14, 15, 16):
    b0 = 11 - 2*n/3; b1 = 102 - 38*n/3
    if b1 < 0 and b0 > 0:
        a = -4*math.pi*b0/b1
        side = "flows DOWN to alpha*" if ab > a else "flows UP toward alpha*"
        print("n=%2d  b0=%6.3f b1=%8.3f  alpha*=%.4f  (%s)" % (n, b0, b1, a, side))
    else:
        print("n=%2d  b0=%6.3f b1=%8.3f  no two-loop zero: alpha grows monotonically into the IR (confining scale exists)" % (n, b0, b1))
