# GUIDE only. Family 2P: W(a;b,c,d) = sum_X exp(a E_X) (1-e^{-a m_X})^{-n_X bcd},
# E_X = f_X bcd - D_X (bc+cd+bd). Works with logs.
import math
fA, fB = 0.0, 1.0
DA = math.log(2.0); DB = DA + 21.0      # b* = 3*21/1 = 63
mA, mB = 2.0, 1.0
nA = nB = 1
def F(a, m): return -math.log1p(-math.exp(-a*m))
def logterms(a, b, c, d):
    V = b*c*d; A = b*c + c*d + b*d
    return (a*(fA*V - DA*A) + nA*V*F(a, mA), a*(fA*V - DA*A)), (a*(fB*V - DB*A) + nB*V*F(a, mB), a*(fB*V - DB*A))
def lse(x, y):
    M = max(x, y); return M + math.log(math.exp(x-M) + math.exp(y-M))
def logW(a, b, c, d):
    (tA, _), (tB, _) = logterms(a, b, c, d); return lse(tA, tB)
def g(a, b, c, d):
    # stable: g = th_vac + log1p(exp(e_oth - e_vac + th_oth - th_vac))
    (tA, eA), (tB, eB) = logterms(a, b, c, d)
    V = b*c*d
    thA, thB = nA*V*F(a, mA), nB*V*F(a, mB)
    if eA > eB: return thA + math.log1p(math.exp((eB - eA) + thB - thA))
    return thB + math.log1p(math.exp((eA - eB) + thA - thB))
def vac(a, b, c, d):
    (_, eA), (_, eB) = logterms(a, b, c, d); return 'A' if eA > eB else 'B'
a0, b0, k = 20, 40, 3
B = 4*k**6
s0 = math.expm1(g(a0, b0, b0, b0))
print("seed s0 = %.3e, threshold 1/B = %.3e, promised gap >= %.4f, m_B = %.2f" % (s0, 1/B, math.log(1/(B*s0))/a0, mB))
boxes = [(b0,b0,b0), (2*b0,b0,b0), (2*b0,2*b0,b0), (2*b0,2*b0,2*b0)]
prev = None
for bx in boxes:
    gg = g(a0, *bx)
    print(bx, "vac", vac(a0, *bx), "g = %.3e" % gg, "" if prev is None else "ratio %.3e" % (gg/prev))
    prev = gg
# FW2 on a grid (super-multiplicativity in b), and bounded defect
worst = 1e9; worst_up = -1e9
for a in (1, 2, 3, 20):
    for c in (1, 2, 40):
        for d in (1, 3, 40):
            for b1 in range(1, 70, 7):
                for b2 in range(1, 70, 5):
                    dlt = logW(a, b1+b2, c, d) - logW(a, b1, c, d) - logW(a, b2, c, d)
                    worst = min(worst, dlt); worst_up = max(worst_up, dlt/(a*c*d))
print("min FW2 defect (must be >= 0): %.4f ; max defect/(a c d) (must be <= D_B = %.3f): %.4f" % (worst, DB, worst_up))
