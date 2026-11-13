# GUIDE only: end-to-end check of the bookkeeping of Theorem 3.3 in an abelian analogue.
# Z_N gauge theory (N even) on an Lx x Ly spatial torus, electric basis = divergence-free edge charges,
# parametrized by plaquette heights h (mod N, overcounted N times) and windings (mx, my).
# K = prod_e w[q_e];  M = sum_p cos(theta_p) shifts h_p by +-1 with matrix element 1/2.
# Exact (S1):  (1/a) F_sigma''(0) = sum_{j in sigma} sum_{p,+-} (1/4) sum_{k=0}^{a-1} w(j')^k w(j)^{a-k} / sum_{j in sigma} w(j)^a
# Prediction (dominant classes):  odd minus all = (2 Lx) * sum_c pi_c D_c ,  lines in direction x, 2 neighbours per edge in 2D.
import numpy as np, itertools, sys
def run(N, Lx, Ly, w, a):
    V = Lx*Ly
    # enumerate heights and windings
    grids = np.indices((N,)*V).reshape(V, -1).astype(np.int8)       # shape (V, N^V)
    h = grids.reshape(Lx, Ly, -1)                                    # h[x,y,state]
    ns = h.shape[-1]
    res = {}
    v = lambda x: (1+x)/(1-x)
    tot = {'odd':[0.0,0.0], 'all':[0.0,0.0]}
    for mx in range(N):
        for my in range(N):
            # edge charges
            qh = np.empty((Lx,Ly,ns), dtype=np.int8); qv = np.empty((Lx,Ly,ns), dtype=np.int8)
            for x in range(Lx):
                for y in range(Ly):
                    qh[x,y] = (h[x,y] - h[x,(y-1)%Ly] + (mx if y==0 else 0)) % N
                    qv[x,y] = (h[(x-1)%Lx,y] - h[x,y] + (my if x==0 else 0)) % N
            logw = np.zeros(ns)
            lw = np.log(w)
            for x in range(Lx):
                for y in range(Ly):
                    logw += lw[qh[x,y]] + lw[qv[x,y]]
            wj = np.exp(logw)
            Zs = np.sum(wj**a)
            num = 0.0
            for x in range(Lx):
                for y in range(Ly):
                    edges = [(qh[x,y], +1), (qh[x,(y+1)%Ly], -1), (qv[x,y], -1), (qv[(x+1)%Lx,y], +1)]
                    for sgn in (+1,-1):
                        ratio = np.ones(ns)
                        for (q, s) in edges:
                            ratio *= w[(q + sgn*s) % N] / w[q]
                        wp = wj*ratio
                        # sum_{k=0}^{a-1} wp^k wj^{a-k}
                        # sum_{k=0}^{a-1} wp^k wj^{a-k} = wj^a (1 - x^a)/(1 - x), x = ratio
                        x_ = ratio
                        geo = np.where(np.abs(x_-1.0) < 1e-12, float(a), (1.0 - x_**a)/np.where(np.abs(x_-1.0) < 1e-12, 1.0, (1.0 - x_)))
                        num += 0.25*np.sum(wj**a * geo)
            for key in (('odd','all') if mx % 2 == 1 else ('all',)):
                tot[key][0] += num; tot[key][1] += Zs
    E_odd = tot['odd'][0]/tot['odd'][1]; E_all = tot['all'][0]/tot['all'][1]
    return E_odd, E_all
def predict(N, Lx, Ly, w, a, odd_charges):
    v = lambda x: (1+x)/(1-x)
    D = {}; W = {}
    for c in odd_charges:   # representative charges up to sign
        xp = w[(c+1)%N]/w[c]*w[1]**3; xm = w[(c-1)%N]/w[c]*w[1]**3
        D[c] = 0.25*v(xp) + 0.25*v(xm) - 0.5*v(w[1]**4)
        mult = 1 if (2*c) % N == 0 else 2
        W[c] = mult*w[c]**(a*Lx)
    tot = sum(W.values())
    return 2*Lx*sum(W[c]/tot*D[c] for c in odd_charges), D, {c: W[c]/tot for c in odd_charges}
N = 6; a = 14
import sys
for (Lx, Ly) in [tuple(int(c) for c in arg.split('x')) for arg in sys.argv[1:]]:
    for label, w3 in (("unboosted", 0.0018), ("boosted w3=0.485", 0.485), ("boosted w3=0.60", 0.60)):
        w = np.array([1.0, 0.48, 0.17, w3, 0.17, 0.48])
        E_odd, E_all = run(N, Lx, Ly, w, a)
        pred, D, pi = predict(N, Lx, Ly, w, a, [1,3])
        print(f"Z6 {Lx}x{Ly} a={a} {label:18s}: exact odd-minus-all {E_odd-E_all:+.5f}   predicted {pred:+.5f}   (D1={D[1]:+.5f}, D3={D[3]:+.5f}, pi1={pi[1]:.3f}, pi3={pi[3]:.3f})")
