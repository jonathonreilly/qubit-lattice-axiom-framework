"""K1 step 2b: one-loop O(q^0) induced masses and tadpole of h from the noncompact U(1) photon on Z^4 (xi = 1),
corner-metric coupling (K-num's H4 photon coupling):  S = sum_{x,s} (1/64) sqrt(g) g^{mu rho} g^{nu sigma} F^s_{mu nu} F^s_{rho sigma},
corner plaquettes centred at x + (s_mu e_mu + s_nu e_nu)/2; for constant h every corner metric is g = 1 + h.
Constant g:  M(p) ∝ sum_{I,J: mu<nu, rho<sigma} 2 sqrt(g) (g^{mu rho} g^{nu sigma} - g^{mu sigma} g^{nu rho}) C_IJ(p) r_I r_J^T,
  r_{mu nu, a} = shat_mu delta_{nu a} - shat_nu delta_{mu a},  C_IJ = prod_{alpha in {mu,nu} xor {rho,sigma}} cos(p_alpha/2).
F_gamma(g) = 1/2 int_p ln det'_{shat-perp} M_g(p)  (U(1) gauge orbit / FP factors are h-independent; exact for this action).
Masses from the Hessian (Richardson in eps), tadpole from the first derivative.  Weyl check: constant conformal g leaves F unchanged.
Usage: python photon_q0.py L1 [L2 ...]
"""
import numpy as np, sys, time, json, itertools
pairs10 = [(m, n) for m in range(4) for n in range(m, 4)]
def sym(v):
    h = np.zeros((4, 4))
    for k, (m, n) in enumerate(pairs10):
        h[m, n] = h[n, m] = v[k]
    return h
P6 = [(m, n) for m in range(4) for n in range(m + 1, 4)]
def Fgamma(hv, L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    g = np.eye(4) + sym(hv); gi = np.linalg.inv(g); sg = np.sqrt(np.linalg.det(g))
    Gm = np.array([[2 * sg * (gi[m, r] * gi[n, s] - gi[m, s] * gi[n, r]) for (r, s) in P6] for (m, n) in P6])  # 6x6
    P1, P2, P3 = np.meshgrid(k, k, k, indexing="ij")
    rest = [P1.ravel(), P2.ravel(), P3.ravel()]
    tot = 0.0
    for p0 in k:
        p = [np.full(rest[0].shape, p0)] + rest
        sh = np.array([2 * np.sin(x / 2) for x in p]); co = np.array([np.cos(x / 2) for x in p])
        Nn = sh.shape[1]
        R = np.zeros((6, 4, Nn))
        for I, (m, n) in enumerate(P6):
            R[I, n] += sh[m]; R[I, m] -= sh[n]
        M = np.zeros((4, 4, Nn))
        for I, (m, n) in enumerate(P6):
            for J, (r, s) in enumerate(P6):
                if Gm[I, J] == 0.0:
                    continue
                sd = set((m, n)) ^ set((r, s))
                C = np.ones(Nn)
                for a in sd:
                    C = C * co[a]
                M += Gm[I, J] * np.einsum('aN,bN,N->abN', R[I], R[J], C)
        nh = sh / np.sqrt((sh * sh).sum(0))
        M = M + np.einsum('aN,bN->abN', nh, nh)          # det(M + n n^T) = det'(M) since M n = 0
        sgn, ld = np.linalg.slogdet(np.moveaxis(M, 2, 0))
        assert np.all(sgn > 0)
        tot += ld.sum()
    return 0.5 * tot / L ** 4

if __name__ == "__main__":
    out = {}
    for L in [int(x) for x in sys.argv[1:]]:
        t0 = time.time()
        F0 = Fgamma(np.zeros(10), L)
        def Q(v, e):
            return (Fgamma(e * v, L) + Fgamma(-e * v, L) - 2 * F0) / (2 * e * e)
        def QR(v):
            e = 4e-3
            return (4 * Q(v, e) - Q(v, 2 * e)) / 3
        v00 = np.zeros(10); v00[0] = 1
        v01 = np.zeros(10); v01[1] = 1
        vdm = np.zeros(10); vdm[0] = 1; vdm[pairs10.index((1, 1))] = -1
        vid = np.zeros(10); vid[[pairs10.index((i, i)) for i in range(4)]] = 1
        q00, q01, qdm, qid = QR(v00), QR(v01), QR(vdm), QR(vid)
        c1 = qdm / 2; c3 = q00 - c1; c2 = q01 / 2
        tad = (Fgamma(1e-3 * vid, L) - Fgamma(-1e-3 * vid, L)) / 2e-3 / 4
        # check: Q(identity) = 4 c1 + 16 c3 should vanish (Weyl)
        print(f"photon L={L} [{time.time()-t0:.0f}s]: masses (cM1,cM2,cM3) = {c1:+.9f} {c2:+.9f} {c3:+.9f};"
              f" tadpole = {tad:+.2e}; Weyl checks: Q(1) = {qid:+.2e}, 4c1+16c3 = {4*c1+16*c3:+.2e}", flush=True)
        out[L] = dict(c=[c1, c2, c3], tad=tad, Qid=qid)
    json.dump(out, open("photon_q0.json", "w"), indent=1)
