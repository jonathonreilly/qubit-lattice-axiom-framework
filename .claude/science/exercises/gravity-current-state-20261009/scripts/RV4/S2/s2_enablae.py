"""S2 (b): E∇E-compatible class.  The shift source must be the energy current (G3/C1): total momentum = total energy current,
so the one-particle symbol is p = omega grad omega = grad(Omega/2),  Omega = omega^2 = M^2 + 2 Phi(k).
=> p is NOT free: p = grad Phi, and the dispersion changes with it.  Phi = sum_q b_q (1 - C_q(k)), C_q = cubic-orbit average of cos(q.k),
range max|q_i| <= 4;  normalisation Hess Phi(0) = I  <=>  sum_q b_q |q|^2/d = 1.
   mu_E  = -< (Phi_x^2 - Phi_y^2)(Phi_xx - Phi_yy) / (8 omega) >
   mu_T2 = -< Phi_x Phi_y Phi_xy / (2 omega) >
   mu_tr = -< |grad Phi|^2 Lap Phi / (8 omega) >
Costs reported: doublers (min of Phi/Phi_NN off the origin), quartic Lorentz-violating coefficients (alpha, beta) of Phi,
C3 averaged anomaly <Hess Phi> - I (= -I for every periodic Phi), max group velocity at M=0."""
import numpy as np, itertools, time
from scipy.optimize import minimize, fsolve
from s2_core import grid
rng = np.random.default_rng(7)

def orbits(d, r):
    return [q for q in itertools.combinations_with_replacement(range(r, -1, -1), d) if any(q)]

def phi_derivs(d, K, qs):
    """per orbit q: (1-C_q), grad, hessian (as lists) on grid K."""
    out = []
    for q in qs:
        perms = set(itertools.permutations(q))
        F = 0; G = [0]*d; Hs = [[0]*d for _ in range(d)]
        for pq in perms:
            c = [np.cos(pq[i]*K[i]) for i in range(d)]; s = [np.sin(pq[i]*K[i]) for i in range(d)]
            prod = np.prod(c, axis=0)
            F = F + prod
            for i in range(d):
                gi = -pq[i]*s[i]*np.prod([c[j] for j in range(d) if j != i], axis=0)
                G[i] = G[i] + gi
                for j in range(d):
                    if i == j:
                        Hs[i][j] = Hs[i][j] - pq[i]**2*prod
                    else:
                        Hs[i][j] = Hs[i][j] + pq[i]*pq[j]*s[i]*s[j]*np.prod([c[l] for l in range(d) if l not in (i, j)], axis=0)
        npm = len(perms)
        # 1 - C : value 1 - F/npm ; derivatives of -C
        out.append((1 - F/npm, [-g/npm for g in G], [[-h/npm for h in row] for row in Hs]))
    return out

class Model:
    def __init__(self, d, L, r):
        self.d = d; self.K = grid(d, L); self.qs = orbits(d, r)
        self.B = phi_derivs(d, self.K, self.qs)
        self.norm = np.array([sum(x*x for x in q)/d for q in self.qs], float)
    def fields(self, b):
        d = self.d
        Phi = sum(bi*B[0] for bi, B in zip(b, self.B))
        G = [sum(bi*B[1][i] for bi, B in zip(b, self.B)) for i in range(d)]
        Hs = [[sum(bi*B[2][i][j] for bi, B in zip(b, self.B)) for j in range(d)] for i in range(d)]
        return Phi, G, Hs
    def mus(self, b, M):
        Phi, G, Hs = self.fields(b)
        w = np.sqrt(np.maximum(M*M + 2*Phi, 1e-300))
        mE = -np.mean((G[0]**2 - G[1]**2)*(Hs[0][0] - Hs[1][1])/(8*w))
        mT = -np.mean(G[0]*G[1]*Hs[0][1]/(2*w))
        mtr = -np.mean(sum(g*g for g in G)*sum(Hs[i][i] for i in range(self.d))/(8*w))
        return mE, mT, mtr
    def costs(self, b):
        d = self.d; Phi, G, Hs = self.fields(b)
        PhiNN = sum(1 - np.cos(k) for k in self.K)
        ratio = Phi/PhiNN
        # quartic coefficients from Taylor of each orbit: 1 - C_q = sum_i <q_i^2> k_i^2/2 - [<q_i^4> k_i^4/24 + <q_i^2 q_j^2> k_i^2 k_j^2/4 (i<j)] + ...
        al = 0.0; be = 0.0
        for bi, q in zip(b, self.qs):
            P = list(set(itertools.permutations(q)))
            al += -bi*np.mean([p[0]**4 for p in P])/24
            be += -bi*np.mean([p[0]**2*p[1]**2 for p in P])/4
        hav = np.mean(Hs[0][0])
        vg = np.sqrt(sum(g*g for g in G)/np.maximum(2*Phi, 1e-30))   # |grad omega| at M=0 = |grad Phi|/sqrt(2 Phi)
        return dict(min_ratio=ratio.min(), alpha=al, beta=be, C3_avg_anom=hav-1.0, vmax=vg.max())

def b_from_free(x, norm, j0):
    b = np.zeros(len(norm)); free = [i for i in range(len(norm)) if i != j0]
    b[free] = x; b[j0] = (1 - norm[free] @ x)/norm[j0]; return b

import sys
CFG = [(2, 96, 4), (3, 32, 3)]
for d, L, r in CFG:
    t0 = time.time()
    Mo = Model(d, L, r); qs = Mo.qs; j0 = qs.index((1,)+(0,)*(d-1))
    bNN = np.zeros(len(qs)); bNN[j0] = d            # Phi_NN = sum(1-cos k_i) = d(1-C_(1,0..))
    print(f"\n========== d={d} range<={r}: {len(qs)} cubic orbits, L={L} ({time.time()-t0:.1f}s) ==========")
    for M in [1.0, 0.3]:
        print(f"  NN (p=sin k) M={M}: mu_E,mu_T2,mu_tr = " + " ".join(f"{x:+.6e}" for x in Mo.mus(bNN, M)))
    # named: body-diagonal (E-protected) and its costs
    jd = qs.index((1,)*d); bD = np.zeros(len(qs)); bD[jd] = 1/Mo.norm[jd]
    print(f"  body-diagonal Phi (J_E = 1): mus(M=1) = " + " ".join(f"{x:+.4e}" for x in Mo.mus(bD, 1.0)) + f"  costs {Mo.costs(bD)}")
    xNN = np.delete(bNN, j0)
    sols = {}
    for M in [1.0, 0.3]:
        FM = Mo.mus(bNN, M)[0]
        cons = [{'type': 'eq', 'fun': lambda x, M=M: np.array(Mo.mus(b_from_free(x, Mo.norm, j0), M)[:2])/FM},
                {'type': 'ineq', 'fun': lambda x: Mo.costs(b_from_free(x, Mo.norm, j0))['min_ratio'] - 0.2}]
        best = None
        for s in range(4 if d == 2 else 2):
            x0 = xNN + (0.05*s)*rng.standard_normal(len(xNN))
            rr = minimize(lambda x: np.sum((x-xNN)**2), x0, constraints=cons, method='SLSQP', options={'maxiter': 300 if d == 2 else 80, 'ftol': 1e-14})
            v = np.abs(cons[0]['fun'](rr.x)).max()
            if v < 1e-9 and cons[1]['fun'](rr.x) > -1e-9 and (best is None or rr.fun < best.fun): best = rr
        if best is None: print(f"  M={M}: no doubler-free common zero found"); continue
        b = b_from_free(best.x, Mo.norm, j0); sols[M] = b
        print(f"  common zero at M={M} (doubler-free, Phi>=0.2 Phi_NN): |b-b_NN|={np.sqrt(best.fun):.4f}  ({time.time()-t0:.0f}s)")
        print("     largest b:", sorted([(round(b[i], 4), qs[i]) for i in range(len(qs))], key=lambda z: -abs(z[0]))[:6])
        for M2 in [0.1, 0.3, 1.0, 3.0]:
            m3 = Mo.mus(b, M2); ref = Mo.mus(bNN, M2)[0]
            print(f"     M={M2}: mu_E={m3[0]:+.4e} mu_T2={m3[1]:+.4e} mu_tr={m3[2]:+.4e}   (NN mu_E {ref:+.4e})")
        print(f"     costs: {Mo.costs(b)}   [NN: {Mo.costs(bNN)}]")
        np.save(f"s2_enablae_zero_d{d}_M{M}.npy", b)
    # all-mass attempt: minimise normalised residual over a mass set, report floor and the IR condition (alpha, beta)
    Ms = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]
    FMs = {M: Mo.mus(bNN, M)[0] for M in Ms}
    def resid(x):
        b = b_from_free(x, Mo.norm, j0)
        return sum((np.array(Mo.mus(b, M)[:2])/FMs[M])@(np.array(Mo.mus(b, M)[:2])/FMs[M]) for M in Ms)
    cons = [{'type': 'ineq', 'fun': lambda x: Mo.costs(b_from_free(x, Mo.norm, j0))['min_ratio'] - 0.2}]
    best = None
    starts = [np.delete(sols[M], j0) for M in sols][:1] if d == 2 else []
    for x0 in starts:
        rr = minimize(resid, x0, constraints=cons, method='SLSQP', options={'maxiter': 120, 'ftol': 1e-20})
        if best is None or rr.fun < best.fun: best = rr
    b = b_from_free(best.x, Mo.norm, j0)
    print(f"  ALL-MASS attempt over {len(Ms)} masses: min sum (mu/F_NN)^2 = {best.fun:.3e}  (NN: {resid(xNN):.3e}; {len(Ms)*2} conditions, {len(xNN)} free)  ({time.time()-t0:.0f}s)")
    for M2 in [0.05, 0.4, 1.2, 4.0]:
        m3 = Mo.mus(b, M2); ref = Mo.mus(bNN, M2)[0]
        print(f"     off-set M={M2}: mu_E/F={m3[0]/ref:+.3e} mu_T2/F={m3[1]/ref:+.3e}")
    print(f"     costs: {Mo.costs(b)}")
