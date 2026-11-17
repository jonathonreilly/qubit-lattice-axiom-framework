"""GUIDE run for row 1085 (gap-descent-sign-2), task 1. Refutes or guides only; discharges no proof step.
Box: one transverse plaquette (square of four transverse sites), n = 2 or 3 layers, SU(2).
Large-t (kinetic time) second-order data:
  P_0 M P_0 on ker N (class functions of the layer plaquettes), its top eigenpairs (lambda_i, phi_i),
  l_i = ||P_1 M phi_i||^2 / lambda_i^2, P_1 = level N = 3/2 (two vertical spin-1/2 edges in one layer gap).
  n_i(t) = (3/2) e^(-3t/2) l_i + ...; sign of n_1 - n_0 at large t = sign of l_1 - l_0.
Formulas: library/gap-descent-sign-2.md step 3.1. Coefficients tested by gram_test.py.
Usage: python3 tplaq.py NLAYERS A D [betaT ...]   A = number of characters per layer in ker N, D = number of loop spins.
Caller sets one BLAS thread."""
import sys, math, json, os
import numpy as np
from scipy.special import ive
from functools import lru_cache

def lf(n): return math.lgamma(n + 1)
def tri(a, b, c): return 0.5 * (lf((a+b-c)//2) + lf((a-b+c)//2) + lf((-a+b+c)//2) - lf((a+b+c)//2 + 1))
def ok(a, b, c): return (a+b+c) % 2 == 0 and abs(a-b) <= c <= a+b
@lru_cache(maxsize=None)
def sixj(a, b, c, d, e, f):  # doubled args, Racah formula (copied from row 1081's su2box.py)
    if not (ok(a,b,c) and ok(a,e,f) and ok(d,b,f) and ok(d,e,c)): return 0.0
    pre = tri(a,b,c) + tri(a,e,f) + tri(d,b,f) + tri(d,e,c)
    t1, t2, t3, t4 = (a+b+c)//2, (a+e+f)//2, (d+b+f)//2, (d+e+c)//2
    s1, s2, s3 = (a+b+d+e)//2, (b+c+e+f)//2, (a+c+d+f)//2
    tot = 0.0
    for z in range(max(t1,t2,t3,t4), min(s1,s2,s3)+1):
        tot += (-1)**z * math.exp(pre + lf(z+1) - lf(z-t1) - lf(z-t2) - lf(z-t3) - lf(z-t4) - lf(s1-z) - lf(s2-z) - lf(s3-z))
    return tot

def setup(A, D):
    big = A + D
    # C_d on dims 1..big2 (index = dim - 1 = doubled spin)
    big2 = big + D
    C = np.zeros((D, big2, big2))
    for d in range(D):
        for a in range(big2):
            for ap in range(big2):
                if ok(a, d, ap): C[d, ap, a] = 1.0
    PJ = [(J, J + s) for J in range(D) for s in (-1, 1) if 0 <= J + s < D]      # (J_I, J_II) doubled
    PP = [(j, j + s) for j in range(big2 + D) for s in (-1, 1) if 0 <= j + s < big2 + D]   # (j, j') doubled
    R = np.zeros((len(PJ), len(PP), big))
    for q, (JI, JII) in enumerate(PJ):
        for p, (j, jp) in enumerate(PP):
            for b in range(big):
                v = sixj(j, jp, 1, JII, JI, b)
                if v != 0.0: R[q, p, b] = math.sqrt(2.0 * (j+1) * (jp+1)) * v * v
    return dict(A=A, D=D, big=big, big2=big2, C=C, PJ=PJ, PP=PP, R=R)

def uvec(beta, n):  # u_d = I_d(beta)/I_1(beta), d = 1..n
    d = np.arange(1, n + 1, dtype=float)
    return ive(d, beta) / ive(1, beta)

def ET(betaT, n):   # multiplication by exp(betaT (x - 1)) on characters of dims 1..n
    if betaT == 0.0: return np.eye(n)
    d = np.arange(1, n + 1)
    return ive(np.abs(d[:, None] - d[None, :]), betaT) - ive(d[:, None] + d[None, :], betaT)

def run(S, nl, bM, bT):
    A, D, big, big2, C, PJ, PP, R = (S[k] for k in ('A', 'D', 'big', 'big2', 'C', 'PJ', 'PP', 'R'))
    u = uvec(bM, big2 + D)
    E = ET(bT, big2)
    X = np.array([C[d] @ E for d in range(D)])        # multiplication by chi_d exp(bT x), big2 x big2
    Xc = X[:, :A, :A]
    u4 = u[:D]**4
    k0 = u[:A]**2                                     # sqrt of a_a^4
    if nl == 2:
        M0 = np.einsum('d,dxa,dyb->xyab', u4, Xc, Xc)
        kk = k0[:, None] * k0[None, :]
        M0 = (kk[:, :, None, None] * M0 * kk[None, None, :, :]).reshape(A*A, A*A)
    else:
        Y = np.array([[(C[d] @ C[e] @ E)[:A, :A] for e in range(D)] for d in range(D)])
        M0 = np.einsum('d,e,dxa,deyb,ezc->xyzabc', u4, u4, Xc, Y, Xc, optimize=True)
        kk = k0[:, None, None] * k0[None, :, None] * k0[None, None, :]
        M0 = (kk[:, :, :, None, None, None] * M0 * kk[None, None, None, :, :, :]).reshape(A**3, A**3)
    asym = np.abs(M0 - M0.T).max()
    M0 = 0.5 * (M0 + M0.T)
    w, V = np.linalg.eigh(M0)
    NE = int(os.environ.get('NEIG', '3'))
    lam = w[::-1][:max(4, NE)]
    out = dict(lam=[float(x) for x in lam], asym=float(asym), l=[], parity=[], tail=[], cpar=[])
    sgn = (-1.0)**np.arange(A)
    upp = np.array([[u[j], u[jp]] for (j, jp) in PP])   # u at dims j+1, jp+1 (index = doubled spin)
    for i in range(NE):
        phi = V[:, -1 - i]
        if nl == 2:
            g = (phi.reshape(A, A) * kk)
            out['cpar'].append(float(np.einsum('ab,a,b->', phi.reshape(A, A)**2, sgn, sgn)))
            out['parity'].append(float(np.sum(phi.reshape(A, A) * phi.reshape(A, A).T)))
            out['tail'].append(float(np.sum(phi.reshape(A, A)[A-2:, :]**2) + np.sum(phi.reshape(A, A)[:, A-2:]**2)))
            G = E[:big, :A] @ g @ E[:big, :A].T
        else:
            g = (phi.reshape(A, A, A) * kk)
            out['cpar'].append(float(np.einsum('abc,a,b,c->', phi.reshape(A, A, A)**2, sgn, sgn, sgn)))
            out['parity'].append(float(np.sum(phi.reshape(A, A, A) * phi.reshape(A, A, A).transpose(2, 1, 0))))
            t3 = phi.reshape(A, A, A)
            out['tail'].append(float(np.sum(t3[A-2:]**2) + np.sum(t3[:, A-2:]**2) + np.sum(t3[:, :, A-2:]**2)))
            # multiply by exp(bT x) on layer 1 and by Z_23 exp(bT (x_2 + x_3)) on layers 2, 3
            G = np.einsum('e,xa,eyb,ezc,abc->xyz', u4, E[:big, :A], X[:, :big, :A], X[:, :big2, :A], g, optimize=True)
        tot = 0.0
        for (nI, nII, mult) in ((1, 3, 4), (2, 2, 2)):
            wq = np.array([(JI+1) * (JII+1) * u[JI]**nI * u[JII]**nII for (JI, JII) in PJ])
            kf = upp[:, 0]**nI * upp[:, 1]**nII
            if nl == 2:
                amp = np.einsum('q,qka,ab,qjb->kj', wq, R, G, R, optimize=True)
                tot += mult * float(np.sum(kf[:, None] * kf[None, :] * amp**2))
            else:
                amp = np.einsum('q,qka,abc,qjb->kjc', wq, R, G, R, optimize=True)
                kc = u[:big2]**4
                tot += 2 * mult * float(np.sum(kf[:, None, None] * kf[None, :, None] * kc[None, None, :] * amp**2))
        out['l'].append(tot / lam[i]**2)
    return out

if __name__ == '__main__':
    nl, A, D = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    bTs = [float(x) for x in sys.argv[4:]] or [0.0, 0.1, 0.3]
    S = setup(A, D)
    BMS = [float(x) for x in os.environ.get('BMS', '0.5,1,1.5,2,2.4,3,4,5,6,8,10,12,16').split(',')]
    tag = os.environ.get('TAG', '')
    print(f"# layers {nl} A {A} D {D}  dim ker-N block {A**nl}")
    print("bM bT  lam1/lam0 lam2/lam1  par1 par2  l0 l1 l2  l1-l0  l2-l0  tail0 tail1  cpar0 cpar1 cpar2")
    res = {}
    for bT in bTs:
        for bM in BMS:
            o = run(S, nl, bM, bT)
            lam, l = o['lam'], o['l']
            print(f"{bM:4.1f} {bT:4.2f}  {lam[1]/lam[0]:.6e} {lam[2]/lam[1]:.6f}  {o['parity'][1]:+.2f} {o['parity'][2]:+.2f}  "
                  f"{l[0]:.6e} {l[1]:.6e} {l[2]:.6e}  {l[1]-l[0]:+.6e} {l[2]-l[0]:+.6e}  {o['tail'][0]:.1e} {o['tail'][1]:.1e}  {o['cpar'][0]:+.3f} {o['cpar'][1]:+.3f} {o['cpar'][2]:+.3f}", flush=True)
            res[f"{bM},{bT}"] = o
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(res, open(os.path.join(here, f"out_tplaq_n{nl}_A{A}_D{D}{tag}.json"), "w"))
