"""GUIDE check of the one-link forms of the SU(2) loop equations (Section 1).

The loop equations are identities of the one-link conditional law, density
prop. to exp(beta * sum_p x_p) with x_p = (1/2) tr(U B_p), six fixed staples B_p.
Criteria written before the run (each must hold within 5 standard errors):
 L1 (multiplicity 1):  E[W (3 + beta h)] = beta * sum_p (1/2) tr(B_p A^-1),
     W = (1/2) tr(U A), h = sum_p x_p.
 L2 (multiplicity 2, same direction):
     E[W2 (8 + 2 beta h)] = beta * sum_p E[(1/2)tr(B_p^-1 A1 U A2) + (1/2)tr(U A1 B_p^-1 A2)]
                            - 4 (1/2) tr(A1 A2^-1),   W2 = (1/2) tr(U A1 U A2).
 L1' (U(1) on the maximal torus, control of the coefficient 1 vs 3):
     E[cos(th+al) (1 + beta h)] = beta * sum_p cos(al - b_p),  h = sum_p cos(th + b_p).
Monte Carlo with Haar sampling and exponential weights; pure Python; < 50 MB.
"""
import math, random
random.seed(20261112)

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qinv(a): return (a[0], -a[1], -a[2], -a[3])
def haar():
    while True:
        v = [random.gauss(0, 1) for _ in range(4)]
        n = math.sqrt(sum(x*x for x in v))
        if n > 1e-12: return tuple(x/n for x in v)
def htr(a): return a[0]   # (1/2) tr of the SU(2) matrix of a unit quaternion

def check(beta, N):
    B = [haar() for _ in range(6)]; A = haar(); A1 = haar(); A2 = haar()
    Bi = [qinv(b) for b in B]
    rhs1 = beta * sum(htr(qmul(b, qinv(A))) for b in B)
    o = htr(qmul(A1, qinv(A2)))
    ws = []; L1s = []; L2s = []; L0s = []
    for _ in range(N):
        U = haar()
        h = sum(htr(qmul(U, b)) for b in B)
        ws.append(math.exp(beta*h))
        W = htr(qmul(U, A))
        L1s.append(W*(3 + beta*h) - rhs1)
        L0s.append(W*(1 + beta*h) - rhs1)
        UA1 = qmul(U, A1)
        W2 = htr(qmul(UA1, qmul(U, A2)))
        r2 = sum(htr(qmul(bi, qmul(A1, qmul(U, A2)))) + htr(qmul(UA1, qmul(bi, A2))) for bi in Bi)
        L2s.append(W2*(8 + 2*beta*h) - beta*r2 + 4*o)
    sw = sum(ws)
    res = []
    for L in (L1s, L2s, L0s):
        m = sum(w*l for w, l in zip(ws, L))/sw
        se = math.sqrt(sum((w*(l - m))**2 for w, l in zip(ws, L)))/sw
        res.append((m, se))
    return res

def check_u1(beta, N):
    b = [random.uniform(0, 2*math.pi) for _ in range(6)]; al = random.uniform(0, 2*math.pi)
    rhs = beta*sum(math.cos(al - bp) for bp in b)
    ws = []; Ls = []; Ls3 = []
    for _ in range(N):
        th = random.uniform(0, 2*math.pi)
        h = sum(math.cos(th + bp) for bp in b)
        ws.append(math.exp(beta*h))
        Ls.append(math.cos(th + al)*(1 + beta*h) - rhs)
        Ls3.append(math.cos(th + al)*(3 + beta*h) - rhs)
    sw = sum(ws); res = []
    for L in (Ls, Ls3):
        m = sum(w*l for w, l in zip(ws, L))/sw
        se = math.sqrt(sum((w*(l - m))**2 for w, l in zip(ws, L)))/sw
        res.append((m, se))
    return res

for beta in (0.3, 1.0, 2.0):
    (m1, e1), (m2, e2), (m0, e0) = check(beta, 800000)
    print("SU(2) beta=%.1f  L1 residual %.5f +- %.5f (%.1f se)   L2 residual %.5f +- %.5f (%.1f se)"
          % (beta, m1, e1, abs(m1)/e1, m2, e2, abs(m2)/e2))
    print("SU(2) beta=%.1f  control with coefficient 1 in place of 3 (wrong on purpose): %.5f +- %.5f (%.1f se)" % (beta, m0, e0, abs(m0)/e0))
    (u1, f1), (u3, f3) = check_u1(beta, 200000)
    print("U(1)  beta=%.1f  coefficient 1: residual %.5f +- %.5f (%.1f se);  coefficient 3 (wrong on purpose): %.5f +- %.5f (%.1f se)"
          % (beta, u1, f1, abs(u1)/f1, u3, f3, abs(u3)/f3))
