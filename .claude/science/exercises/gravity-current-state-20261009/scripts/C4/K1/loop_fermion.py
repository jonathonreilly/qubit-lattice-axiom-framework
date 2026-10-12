"""K1 step 2: one-loop induced quadratic action of a symmetric tensor h on Z^4 (xi = 1) from naive/staggered
fermions with the link-averaged vielbein coupling (W(B4)-covariant, Euclidean).

Coupling (stated):  S_f = sum_x { sum_mu 1/2 [ psibar(x) gamma_a E_a^mu(x+mu/2) psi(x+mu) - psibar(x+mu) gamma_a E_a^mu(x+mu/2) psi(x) ]
                                   + m psibar(x) psi(x) },
  E = (1+hbar)^(-1/2) = 1 - hbar/2 + 3 hbar^2/8 + ..., hbar(x+mu/2) = [h(x) + h(x+mu)]/2 (h site-placed, all 10 comps),
  psi densitized (no sqrt g / ln det g measure terms).  Momentum-space vertex: gamma_a i sin(P_mu) cos(q_mu/2) dE_a^mu(q).
Gamma = -Tr ln K.  For h(x) = H cos(q.x):  Gamma_2/V = 1/4 int_p tr[S(p) V S(p+q) V] + seagull,
  tr[S V_A S' V_B] = -(1/(Da Db)) [ (m^2 + a.b) u_A.u_B - (a.u_A)(b.u_B) - (a.u_B)(b.u_A) ],
  u_A,a = sum_mu (H_A)_{a mu} sin(p_mu + q_mu/2) cos(q_mu/2),  a = sin p, b = sin(p+q),
  seagull = -(3/4) I1 sum_mu cos^2(q_mu/2) (H^2)_{mu mu},  I1 = int sin^2 p_1 / D.
Decomposition: Gamma_2/V = 1/2 [ sum_k cM_k M_k(H) + sum_j c_j K_j(H,H;q) ] + O(q^4)  (action density convention).
Normalisation: one NAIVE 4D fermion = 16 Dirac tastes; per 4D staggered field = naive/4 (stated proxy).
Integration: periodic midpoint rule on an L^4 grid (exponentially convergent for m>0; L-convergence checked).
Usage: python loop_fermion.py m L1 [L2 ...]
"""
import numpy as np, sys, time, json
D4 = 4
pairs = [(m, n) for m in range(D4) for n in range(m, D4)]
def sym(v):
    h = np.zeros((D4, D4))
    for k, (m, n) in enumerate(pairs):
        h[m, n] = h[n, m] = v[k]
    return h
EA = [sym(np.eye(10)[k]) for k in range(10)]
fd = np.load("forms_data.npz"); MF = fd["M"]; KF = fd["K"]
names = ["F1", "F2", "F3", "F4", "A1", "A2", "A3", "A4", "A6"]

def grid(L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    return k

def bilinear(q, L, m, chunk_axis=True):
    """10x10 matrix B with Gamma_2/V = v^T B v for H = sum v_A E_A (per naive fermion)."""
    k = grid(L)
    B = np.zeros((10, 10)); I1 = 0.0
    cq = np.cos(q / 2)
    P1, P2, P3 = np.meshgrid(k, k, k, indexing="ij")
    rest = [P1.ravel(), P2.ravel(), P3.ravel()]
    for p0 in k:
        p = [np.full(rest[0].shape, p0)] + rest
        a = np.array([np.sin(x) for x in p])                       # 4,N
        b = np.array([np.sin(x + q[i]) for i, x in enumerate(p)])
        sP = np.array([np.sin(x + q[i] / 2) * cq[i] for i, x in enumerate(p)])   # sin(P_mu) cos(q_mu/2)
        Da = (a * a).sum(0) + m * m; Db = (b * b).sum(0) + m * m
        I1 += np.sum(a[0] ** 2 / Da)
        # u_A,a = sum_mu (E_A)_{a mu} sP_mu
        U = np.einsum('Aam,mN->AaN', np.array(EA), sP, optimize=True)  # 10,4,N
        au = np.einsum('aN,AaN->AN', a, U); bu = np.einsum('aN,AaN->AN', b, U)
        w = 1.0 / (Da * Db)
        ab = (a * b).sum(0)
        uu = np.einsum('AaN,BaN,N->AB', U, U, w * (m * m + ab), optimize=True)
        cross = np.einsum('AN,BN,N->AB', au, bu, w, optimize=True)
        B += -(uu - cross - cross.T)
    N = L ** 4
    B *= 0.25 / N
    I1 /= N
    # seagull
    S = np.zeros((10, 10))
    for A in range(10):
        for Bi in range(10):
            S[A, Bi] = sum(cq[mu] ** 2 * 0.5 * ((EA[A] @ EA[Bi])[mu, mu] + (EA[Bi] @ EA[A])[mu, mu]) for mu in range(4))
    B += -(0.75) * I1 * S
    return B, I1

def Fconst(hv, L, m):
    """constant-metric free energy per volume, per naive fermion: F = -2 int ln(sbar g^-1 sbar + m^2), g = 1+h"""
    k = grid(L)
    gi = np.linalg.inv(np.eye(4) + sym(hv))
    P1, P2, P3 = np.meshgrid(k, k, k, indexing="ij")
    rest = [np.sin(P1.ravel()), np.sin(P2.ravel()), np.sin(P3.ravel())]
    tot = 0.0
    for p0 in k:
        a = np.array([np.full(rest[0].shape, np.sin(p0))] + rest)
        X = np.einsum('aN,ab,bN->N', a, gi, a, optimize=True)
        tot += np.sum(np.log(X + m * m))
    return -2 * tot / L ** 4

def fit_masses(B0):
    # B0 = 1/2 sum cM_k M_k
    A = np.array([0.5 * M.ravel() for M in MF]).T
    c, res, *_ = np.linalg.lstsq(A, B0.ravel(), rcond=None)
    return c, np.linalg.norm(A @ c - B0.ravel()) / np.linalg.norm(B0)

def fit_kin(B2s, dirs):
    rows = []; rhs = []
    for B2, n in zip(B2s, dirs):
        Kn = np.array([0.5 * np.einsum('ABab,a,b->AB', KF[j], n, n).ravel() for j in range(9)]).T
        rows.append(Kn); rhs.append(B2.ravel())
    A = np.vstack(rows); y = np.concatenate(rhs)
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return c, np.linalg.norm(A @ c - y) / np.linalg.norm(y)

if __name__ == "__main__":
    m = float(sys.argv[1]); Ls = [int(x) for x in sys.argv[2:]]
    # on-grid momenta q = (2 pi / L) k n  (k = 1,2,3): finite-volume aliasing phases cancel in B(q) - B(0)
    nvecs = [np.array(v, float) for v in ((1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1), (2, 1, 0, 0), (2, 1, 1, 0))]
    results = {}
    for L in Ls:
        t0 = time.time()
        B0, I1 = bilinear(np.zeros(4), L, m)
        cM, rM = fit_masses(B0)
        B2s = []; dirs = []
        for n in nvecs:
            u = 2 * np.pi / L * n
            d = [bilinear(k * u, L, m)[0] - B0 for k in (1, 2, 3)]
            # d_k = k^2 A + k^4 B + k^6 C  -> A (coefficient of u u)
            A = 1.5 * d[0] - 0.15 * d[1] + d[2] / 90.0   # first row of inverse Vandermonde [k^2,k^4,k^6], k=1,2,3
            B2s.append(A); dirs.append(u)
        cK, rK = fit_kin(B2s, dirs)
        tad = 2 * I1
        Lam = 2 * tad
        cMnet = cM + np.array([Lam / 4, Lam / 4, -Lam / 8])
        print(f"m={m} L={L}  [{time.time()-t0:.0f}s]  per NAIVE fermion (/16 per Dirac taste, /4 per 4D staggered field)")
        print(f"  tadpole t (Gamma_1/V = t tr h) = {tad:+.9f}")
        print(f"  masses (cM1,cM2,cM3) = {cM[0]:+.9f} {cM[1]:+.9f} {cM[2]:+.9f}   fit resid {rM:.1e}")
        print(f"  net masses after CC cancellation  = {cMnet[0]:+.9f} {cMnet[1]:+.9f} {cMnet[2]:+.9f}")
        print("  kinetic c_j: " + "  ".join(f"{nm}={c:+.4e}" for nm, c in zip(names, cK)) + f"   fit resid {rK:.1e}")
        results[L] = dict(tad=tad, cM=cM.tolist(), cMnet=cMnet.tolist(), cK=cK.tolist(), rM=rM, rK=rK)
        sys.stdout.flush()
    # constant-metric cross-check of the mass block (independent formula), at the largest L
    L = Ls[-1]
    F0 = Fconst(np.zeros(10), L, m)
    def Q(v, eps):
        return (Fconst(eps * v, L, m) + Fconst(-eps * v, L, m) - 2 * F0) / (2 * eps ** 2)
    def QR(v):
        e = 2e-3
        return (4 * Q(v, e) - Q(v, 2 * e)) / 3
    v00 = np.zeros(10); v00[0] = 1                          # h_00 = 1
    v01 = np.zeros(10); v01[1] = 1                          # h_01 = h_10 = 1
    vdm = np.zeros(10); vdm[0] = 1; vdm[pairs.index((1, 1))] = -1
    q00, q01, qdm = QR(v00), QR(v01), QR(vdm)
    c1 = qdm / 2; c3 = q00 - c1; c2 = q01 / 2
    vid = np.zeros(10); vid[[pairs.index((i, i)) for i in range(4)]] = 1
    tadc = (Fconst(1e-4 * vid, L, m) - Fconst(-1e-4 * vid, L, m)) / (2e-4) / 4
    print(f"  constant-metric check (L={L}): masses from F(g) Hessian = {c1:+.8f} {c2:+.8f} {c3:+.8f}; tadpole {tadc:+.8f}")
    results["const_check"] = dict(L=L, c=[c1, c2, c3], tad=tadc)
    json.dump(results, open(f"loop_fermion_m{m}.json", "w"), indent=1)
