"""K1 step 2c: one-loop induced quadratic action of h from the noncompact U(1) photon on Z^4 (xi = 1),
corner-metric coupling (K-num H4):  S = sum_{x,s} (1/64) T^{mu nu rho sigma}(g_c) F^s_{mu nu} F^s_{rho sigma},
T = sqrt(g) g^{mu rho} g^{nu sigma},  corner metric g_c(x,s): diag h_kk(x), offdiag h_kl(x + (s_k e_k + s_l e_l)/2),
F^s_{mu nu} on the corner plaquette centred at x + (s_mu e_mu + s_nu e_nu)/2.  Feynman-type h-INDEPENDENT gauge fixing
(exact: S is U(1) invariant for every h, so Z[h] is GF independent; G = 1/shat^2).
Gamma = 1/2 Tr ln K;  h = H cos(q.x):
  Gamma_2/V = -1/2 int tr[G(p) V^T G(p+q) V] + 1/2 int tr[G(p) K2(p)],
  V_A(p+q,p) = 1/4 sum_{I,J} Tas1_A[I,J] Phi_{A,I,J}(p) r_J(p+q) r_I(p)^T  (real),
  Phi = prod_alpha cos(w_alpha/2),  w = p 1_I - (p+q) 1_J + q 1_A(offdiag)   [corner average done analytically],
  K2^{AB}(p) = 1/2 * 1/4 sum_{IJ} T2as_{AB}[I,J] * 1/2 sum_pm prod_alpha cos((p(1_I - 1_J) pm q(1_A - 1_B))_alpha / 2) r_J r_I^T.
Usage: python loop_photon.py L1 [L2 ...]
"""
import numpy as np, sys, time, json, itertools
pairs10 = [(m, n) for m in range(4) for n in range(m, 4)]
def sym(v):
    h = np.zeros((4, 4))
    for k, (m, n) in enumerate(pairs10):
        h[m, n] = h[n, m] = v[k]
    return h
EA = [sym(np.eye(10)[k]) for k in range(10)]
indA = [np.array([1.0 if (m != n and a in (m, n)) else 0.0 for a in range(4)]) for (m, n) in pairs10]
P6 = [(m, n) for m in range(4) for n in range(m + 1, 4)]
ind6 = [np.array([1.0 if a in I else 0.0 for a in range(4)]) for I in P6]
def Tfull(g):
    gi = np.linalg.inv(g); sg = np.sqrt(np.linalg.det(g))
    return sg * np.einsum('mr,ns->mnrs', gi, gi)
def asym(T):
    return np.array([[T[m, n, r, s] - T[n, m, r, s] - T[m, n, s, r] + T[n, m, s, r] for (r, s) in P6] for (m, n) in P6])
d = np.eye(4)
def T1(H):
    return 0.5 * np.trace(H) * np.einsum('mr,ns->mnrs', d, d) - np.einsum('mr,ns->mnrs', H, d) - np.einsum('mr,ns->mnrs', d, H)
def T2(H, K):   # symmetric bilinear, T2(H,H) = second-order part
    def q(h):
        return ((np.trace(h) ** 2) / 8 - np.sum(h * h) / 4) * np.einsum('mr,ns->mnrs', d, d) \
            - 0.5 * np.trace(h) * (np.einsum('mr,ns->mnrs', h, d) + np.einsum('mr,ns->mnrs', d, h)) \
            + np.einsum('mr,ns->mnrs', h @ h, d) + np.einsum('mr,ns->mnrs', d, h @ h) + np.einsum('mr,ns->mnrs', h, h)
    return 0.25 * (q(H + K) - q(H - K))
# self-check of T1, T2 against the exact T(1+eps h)
rng = np.random.default_rng(5); hh = sym(rng.normal(size=10)); e = 1e-3
T0 = Tfull(d)
fd1 = (Tfull(d + e * hh) - Tfull(d - e * hh)) / (2 * e)
fd2 = (Tfull(d + e * hh) + Tfull(d - e * hh) - 2 * T0) / (2 * e * e)
assert np.abs(fd1 - T1(hh)).max() < 1e-4 and np.abs(fd2 - T2(hh, hh)).max() < 1e-3, (np.abs(fd1 - T1(hh)).max(), np.abs(fd2 - T2(hh, hh)).max())
TAS1 = [asym(T1(E)) for E in EA]
TAS2 = [[asym(T2(EA[A], EA[B])) for B in range(10)] for A in range(10)]

def rvec(sh):
    R = np.zeros((6, 4) + sh.shape[1:])
    for I, (m, n) in enumerate(P6):
        R[I, n] += sh[m]; R[I, m] -= sh[n]
    return R

def bilinear(q, L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    P1, P2, P3 = np.meshgrid(k, k, k, indexing="ij")
    rest = [P1.ravel(), P2.ravel(), P3.ravel()]
    B = np.zeros((10, 10)); Sg = np.zeros((10, 10))
    for p0 in k:
        p = np.array([np.full(rest[0].shape, p0)] + rest)
        pq = p + q[:, None]
        sh = 2 * np.sin(p / 2); shq = 2 * np.sin(pq / 2)
        s2 = (sh * sh).sum(0); s2q = (shq * shq).sum(0)
        R = rvec(sh); Rq = rvec(shq)
        V = np.zeros((10, 4, 4, p.shape[1]))
        for A in range(10):
            for I in range(6):
                for J in range(6):
                    c = TAS1[A][I, J]
                    if c == 0.0:
                        continue
                    w = p * ind6[I][:, None] - pq * ind6[J][:, None] + q[:, None] * indA[A][:, None]
                    Phi = np.prod(np.cos(w / 2), axis=0)
                    V[A] += 0.25 * c * np.einsum('bN,aN,N->baN', Rq[J], R[I], Phi)
        wgt = 1.0 / (s2 * s2q)
        B += -0.5 * np.einsum('AbaN,BbaN,N->AB', V, V, wgt, optimize=True)
        # seagull: 1/2 int tr[G K2],  tr K2 = sum r_J . r_I * coeff
        RR = np.einsum('IaN,JaN->IJN', R, R)
        for A in range(10):
            for Bb in range(A, 10):
                tot = 0.0
                for I in range(6):
                    for J in range(6):
                        c = TAS2[A][Bb][I, J]
                        if c == 0.0:
                            continue
                        dI = ind6[I] - ind6[J]; dA = indA[A] - indA[Bb]
                        Psi = 0.5 * (np.prod(np.cos((p * dI[:, None] + q[:, None] * dA[:, None]) / 2), axis=0)
                                     + np.prod(np.cos((p * dI[:, None] - q[:, None] * dA[:, None]) / 2), axis=0))
                        tot += np.sum(c * Psi * RR[I, J] / s2)
                val = 0.5 * 2 * 0.25 * 0.5 * tot   # 1/2 Tr[G K2], K2 = 2*(1/64)*16*avg_s, 1/2 from <cos^2>
                Sg[A, Bb] += val; 
                if Bb != A: Sg[Bb, A] += val
    N = L ** 4
    return (B + Sg) / N, B / N, Sg / N

if __name__ == "__main__":
    fd = np.load("forms_data.npz"); MF = fd["M"]; KF = fd["K"]
    names = ["F1", "F2", "F3", "F4", "A1", "A2", "A3", "A4", "A6"]
    nvecs = [np.array(v, float) for v in ((1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1), (2, 1, 0, 0), (2, 1, 1, 0))]
    out = {}
    for L in [int(x) for x in sys.argv[1:]]:
        t0 = time.time()
        B0 = bilinear(np.zeros(4), L)[0]
        A = np.array([0.5 * M.ravel() for M in MF]).T
        cM, *_ = np.linalg.lstsq(A, B0.ravel(), rcond=None)
        rows = []; rhs = []
        for n in nvecs:
            u = 2 * np.pi / L * n
            dd = [bilinear(k * u, L)[0] - B0 for k in (1, 2, 3)]
            A2 = 1.5 * dd[0] - 0.15 * dd[1] + dd[2] / 90.0
            rows.append(np.array([0.5 * np.einsum('ABab,a,b->AB', KF[j], u, u).ravel() for j in range(9)]).T)
            rhs.append(A2.ravel())
        Am = np.vstack(rows); y = np.concatenate(rhs)
        cK, *_ = np.linalg.lstsq(Am, y, rcond=None)
        rK = np.linalg.norm(Am @ cK - y) / np.linalg.norm(y)
        print(f"photon L={L} [{time.time()-t0:.0f}s]: masses (cM1,cM2,cM3) = {cM[0]:+.7f} {cM[1]:+.7f} {cM[2]:+.7f}", flush=True)
        print("  kinetic c_j: " + "  ".join(f"{nm}={c:+.4e}" for nm, c in zip(names, cK)) + f"   fit resid {rK:.1e}", flush=True)
        out[L] = dict(cM=cM.tolist(), cK=cK.tolist(), rK=rK)
    json.dump(out, open("loop_photon.json", "w"), indent=1)
