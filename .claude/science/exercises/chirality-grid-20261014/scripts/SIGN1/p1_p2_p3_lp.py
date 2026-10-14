"""SIGN-1 P1 (which Majorana time reversals exist), P2 (LP over all on-site HS decompositions), P3 (any Spin(10) quartic).
See ../PREREG.md.  Usage: python p1_p2_p3_lp.py   (one process, < 0.2 GB)
"""
import numpy as np, itertools, sys, time, resource
from scipy.optimize import linprog
import scipy.sparse as sp
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import *

t0 = time.time()
def P(*a):
    print(*a); sys.stdout.flush()
def mem():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20  # MB on macOS (bytes)
rng = np.random.default_rng(20261014)

# ============================================================== P1
P("=== P1(a): filter parity (f(k+Pi) relates hw1 to hw2) ===")
fNN = lambda k: (1 - np.cos(k).sum()) / 2
def fF1(k):
    s2 = np.sin(np.asarray(k) / 2) ** 2; c2 = np.cos(np.asarray(k) / 2) ** 2
    return 1 - (s2[0] * c2[1] * c2[2] + s2[1] * c2[0] * c2[2] + s2[2] * c2[0] * c2[1])
for nm, f in (("f_NN", fNN), ("f_F1", fF1)):
    k1 = np.array([np.pi, 0, 0]); k2 = k1 + np.pi
    fe = (f(k1) + f(k2)) / 2; fo = (f(k1) - f(k2)) / 2
    P(f"  {nm}: f(hw1)={f(k1):+.3f}, f(hw1+Pi)=f(hw2)={f(k2):+.3f} -> even-offset part at hw1 {fe:+.3f}, odd-offset part {fo:+.3f} (both nonzero)")

P("=== P1(b): uniform MTRs of the walker (flavour 4x4 problem on (tau, sigma)) ===")
# two sites, two spins: bond operator  psi_1^dag sigma_a psi_2 / (2i) + h.c.  -> Majorana K; extract flavour block
Wf = []
for a, sg in enumerate((X.astype(complex), SY, Z.astype(complex))):
    h = np.zeros((4, 4), complex)          # modes (site, s): m = site*2 + s
    h[0:2, 2:4] = sg / (2j); h[2:4, 0:2] = (sg / (2j)).conj().T
    K = density_K(h)                       # 8x8 Majorana, ordering tau*4 + site*2 + s
    a_ = (-2j * K).real                    # K = (i/2) a  ->  a real antisym
    assert np.allclose((-2j * K).imag, 0)
    idx1 = [t * 4 + 0 * 2 + s for t in range(2) for s in range(2)]
    idx2 = [t * 4 + 1 * 2 + s for t in range(2) for s in range(2)]
    Wf.append(a_[np.ix_(idx1, idx2)])     # flavour matrix multiplying the (antisymmetric) site-1/site-2 kernel
for a in range(3):
    P(f"  W_{'xyz'[a]} (tau,sigma) symmetric? {np.allclose(Wf[a], Wf[a].T)}")
J4 = realify(np.array([[1j]]))  # 2x2 complex structure on one mode's (g1,g2)
J4 = np.kron(J4, np.eye(2))     # ordering tau*2 + s
for sign, nm in ((+1, "anticommuting (uniform Theta)"), (-1, "commuting (staggered Theta)")):
    A = np.vstack([np.kron(W, np.eye(4)) + sign * np.kron(np.eye(4), W.T) for W in Wf])
    u, s, vt = np.linalg.svd(A)
    sol = [v.reshape(4, 4) for v in vt[-(s < 1e-10).sum():]] if (s < 1e-10).any() else []
    rel = ["anticommutes with J" if np.allclose(O @ J4, -J4 @ O) else ("commutes with J" if np.allclose(O @ J4, J4 @ O) else "mixed")
           for O in sol]
    P(f"  O {nm}: solution dimension {len(sol)}; each solution {set(rel)}")
P("  -> uniform MTR anticommutes with the complex structure J: Theta is number-conserving (psi -> M psi);")
P("     staggered MTR commutes with J: particle-hole type; excluded by the filter's even+odd offsets (P1(a)).")

P("=== P1(c): Theta_V = (i sigma_y x V) K, V^T N^a* V = s_a N^a ===")
Vs = {1: np.eye(16), 5: G9[0] @ G9[1] @ G9[2] @ G9[3], 3: G9[0] @ G9[1]}
for k, V in Vs.items():
    s_list = []
    for Na in N10:
        T = V.T @ Na.conj() @ V
        s = np.vdot(Na.ravel(), T.ravel()).real / np.vdot(Na.ravel(), Na.ravel()).real
        assert np.allclose(T, s * Na)
        s_list.append(int(round(s)))
    sym = "symmetric" if np.allclose(V, V.T) else ("antisymmetric" if np.allclose(V, -V.T) else "?")
    M = np.kron(E, V); O = antireal(M.astype(complex))
    P(f"  k={k}: V {sym}, Theta^2 = {'-1' if np.allclose(O @ O, -np.eye(64)) else ('+1' if np.allclose(O @ O, np.eye(64)) else '?')}, "
      f"parities s_a = {s_list} (#(-1) = {s_list.count(-1)})")
# no V with uniform parity: check that conj rep is inequivalent (character test on a generic element)
gens = spin10_gens()
T = sum(rng.normal() * t for t in gens.values()); g = np.linalg.matrix_power(np.eye(16) + T / 64, 64)
P(f"  16 vs 16bar: tr g = {np.trace(g):.4f}, tr g* = {np.trace(g.conj()):.4f} (unequal -> no antiunitary commutes with Spin(10))")

# ============================================================== P2 setup
Kb = vertex_B()
n = 64
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]; NP = len(pairs)
pid = -np.ones((n, n), int)
for p, (i, j) in enumerate(pairs): pid[i, j] = p
def vec_to_mat(v):
    a = np.zeros((n, n)); iu = np.triu_indices(n, 1)
    a[iu] = v / np.sqrt(2); return a - a.T
def mats_to_vec(As):  # (b,64,64) -> (b, NP)
    iu = np.triu_indices(n, 1); return As[:, iu[0], iu[1]] * np.sqrt(2)

# samples
S = 6000
quads = np.array(sorted({tuple(sorted(rng.choice(n, 4, replace=False))) for _ in range(S + 500)}))[:S]
def pp(a, b): return pid[np.minimum(a, b), np.maximum(a, b)]
i_, j_, k_, l_ = quads.T
PIDX = [pid[i_, j_], pid[k_, l_], pid[i_, k_], pid[j_, l_], pid[i_, l_], pid[j_, k_]]
q1 = sum(alt_s(-Kb[a].conj(), Kb[a], quads) for a in range(10))
q2 = sum(2 * alt_s(Kb[a], Kb[a], quads).real for a in range(10))   # BB + h.c. = 2 Re
assert np.abs(q1.imag).max() < 1e-12
q1 = q1.real; q2 = q2.real
P(f"\nsamples: {len(quads)} quadruples; |q1|_1 = {np.abs(q1).sum():.3f}, |q2|_1 = {np.abs(q2).sum():.3f}")

def generators(k):
    su2 = [realify(np.kron(0.5j * s, np.eye(16))) for s in (X.astype(complex), SY, Z.astype(complex))]
    if k == 1: K1, K2 = [], [g for (a, b), g in gens.items() if b < 9]
    elif k == 5:
        A = {0, 1, 2, 3, 9}
        K1 = [g for (a, b), g in gens.items() if a in A and b in A]
        K2 = [g for (a, b), g in gens.items() if a not in A and b not in A]
    elif k == 3:
        A = {0, 1, 9}
        K1 = [g for (a, b), g in gens.items() if a in A and b in A]
        K2 = [g for (a, b), g in gens.items() if a not in A and b not in A]
    K1 = [realify(np.kron(np.eye(2), t)) for t in K1]; K2 = [realify(np.kron(np.eye(2), t)) for t in K2]
    outside = [realify(np.kron(np.eye(2), t)) for (a, b), t in gens.items()
               if not ((k == 1 and b < 9) or (k != 1 and ((a in A and b in A) or (a not in A and b not in A))))]
    return su2, K1, K2, outside

def signed_perm_action(R):
    """Ad_R(a) = R^T a R on pair basis, R a signed permutation: returns (perm, sign)."""
    perm = np.zeros(NP, int); sgn = np.zeros(NP)
    for p, (i, j) in enumerate(pairs):
        a = np.zeros((n, n)); a[i, j] = 1; a[j, i] = -1
        b = R.T @ a @ R
        ii, jj = np.nonzero(np.triu(np.abs(b) > 0.5, 1))
        assert len(ii) == 1
        perm[p] = pid[ii[0], jj[0]]; sgn[p] = b[ii[0], jj[0]]
    return perm, sgn

def casimir_on(basis_mats, gl):
    out = np.zeros_like(basis_mats)
    for g in gl:
        c1 = np.einsum("ij,bjk->bik", g, basis_mats) - basis_mats @ g
        out += np.einsum("ij,bjk->bik", g, c1) - c1 @ g
    return out

RZ = realify(1j * np.eye(32))
results = {}
for k in (1, 5, 3):
    tk = time.time()
    V = Vs[k]; O = antireal(np.kron(E, V).astype(complex))
    su2, K1, K2, outside = generators(k)
    for g in su2 + K1 + K2:
        assert np.allclose(g @ O, O @ g), "symmetry generator does not commute with Theta"
    assert np.allclose(RZ @ O, -O @ RZ)
    # Q invariance under O (Theta) and RZ: check on the sample through q-values of transformed K's
    for R, nm in ((O, "Theta"), (RZ, "Z4")):
        Kt = [R.T @ Kk @ R for Kk in Kb]
        if nm == "Theta": Kt = [Kk.conj() for Kk in Kt]   # antilinear
        q1t = sum(alt_s(-Kt[a].conj(), Kt[a], quads) for a in range(10)).real
        q2t = sum(2 * alt_s(Kt[a], Kt[a], quads).real for a in range(10))
        assert np.allclose(q1t, q1) and np.allclose(q2t, q2), f"Q not {nm}-invariant"
    pZ, sZ = signed_perm_action(RZ); pO, sO = signed_perm_action(O)
    # sector bases from orbits
    seen = np.zeros(NP, bool); sectors = {(s1, s2): [] for s1 in (1, -1) for s2 in (1, -1)}
    for p in range(NP):
        if seen[p]: continue
        orb = {p}; frontier = [p]
        while frontier:
            q = frontier.pop()
            for nq in (pZ[q], pO[q]):
                if nq not in orb: orb.add(nq); frontier.append(nq)
        for q in orb: seen[q] = True
        orb = sorted(orb)
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = {}
                # group elements: e, Z, O, ZO acting on e_p
                for useZ in (0, 1):
                    for useO in (0, 1):
                        q, sg = p, 1.0
                        if useZ: sg *= sZ[q]; q = pZ[q]
                        if useO: sg *= sO[q]; q = pO[q]
                        ch = (s1 if useZ else 1) * (s2 if useO else 1)
                        v[q] = v.get(q, 0.0) + ch * sg / 4
                v = {q: c for q, c in v.items() if abs(c) > 1e-12}
                if v:
                    nrm = np.sqrt(sum(c * c for c in v.values()))
                    sectors[(s1, s2)].append({q: c / nrm for q, c in v.items()})
    clusters = []
    for key, vecs in sectors.items():
        d = len(vecs)
        B = np.zeros((NP, d))
        for c, v in enumerate(vecs):
            for q, val in v.items(): B[q, c] = val
        # orthonormalise (orbit vectors from different p in the same orbit can coincide up to sign)
        u, s, vt = np.linalg.svd(B, full_matrices=False); B = u[:, s > 1e-8]; d = B.shape[1]
        Cs = [np.zeros((d, d)) for _ in range(3)]
        for st in range(0, d, 96):
            mats = np.array([vec_to_mat(B[:, c]) for c in range(st, min(d, st + 96))])
            for ci, gl in enumerate((su2, K1, K2)):
                if gl:
                    Cs[ci][:, st:st + mats.shape[0]] = B.T @ mats_to_vec(casimir_on(mats, gl)).T
            del mats
        Xm = Cs[0] + np.sqrt(2) * Cs[1] + (np.pi / 3) * Cs[2]
        assert np.allclose(Xm, Xm.T, atol=1e-9)
        w, U = np.linalg.eigh(Xm)
        order = np.argsort(w); w = w[order]; U = U[:, order]
        start = 0
        for e in range(1, d + 1):
            if e == d or abs(w[e] - w[start]) > 1e-6 * max(1, abs(w[start])):
                cols = U[:, start:e]
                cas = tuple(round(float(np.trace(cols.T @ C @ cols) / cols.shape[1]), 6) for C in Cs)
                clusters.append(dict(sector=key, dim=e - start, cas=cas, Vfull=B @ cols))
                start = e
    dims = sorted([c["dim"] for c in clusters])
    P(f"\n=== P2 k={k}: {len(clusters)} joint eigenspaces of (Casimirs, Z4, Theta) on Lambda^2; dims {dims}; total {sum(dims)}")
    # A_rho on samples
    A = np.zeros((len(quads), len(clusters)))
    for c, cl in enumerate(clusters):
        Vf = cl["Vfull"]
        for st in range(0, len(quads), 1500):
            sl = slice(st, st + 1500)
            A[sl, c] = ((Vf[PIDX[0][sl]] * Vf[PIDX[1][sl]]).sum(1) - (Vf[PIDX[2][sl]] * Vf[PIDX[3][sl]]).sum(1)
                        + (Vf[PIDX[4][sl]] * Vf[PIDX[5][sl]]).sum(1))
    M = -0.25 * A
    even = np.array([cl["sector"][1] == -1 for cl in clusters])   # Ad_Theta = -1  <=> Theta-even bilinears
    P(f"  Theta-even irreps (attractive/real field allowed): {even.sum()}  dims {[cl['dim'] for cl, e in zip(clusters, even) if e]}")
    P(f"  Theta-odd  irreps (repulsive/imag field allowed):  {(~even).sum()}  dims {[cl['dim'] for cl, e in zip(clusters, even) if not e]}")
    rk = np.linalg.matrix_rank(M, tol=1e-9); P(f"  rank of the 4-form images on the sample: {rk}")
    # consistency: unconstrained fit of q1, q2
    for nm, qq in (("q1 (sum B^dag B)", q1), ("q2 (sum BB + h.c.)", q2)):
        g, *_ = np.linalg.lstsq(M, qq, rcond=None)
        P(f"  unconstrained fit of {nm}: relative residual {np.linalg.norm(M @ g - qq) / np.linalg.norm(qq):.2e}")
    # LP scan over angles
    bounds = [(None, 0) if e else (0, None) for e in even]
    nS = len(quads); nr = len(clusters)
    feas = []
    for th in np.arange(72) * 5.0:
        lam1, lam2 = np.cos(np.radians(th)), np.sin(np.radians(th))
        c = lam1 * q1 + lam2 * q2
        # L1 residual LP: min sum(sp+sm) s.t. M g + sp - sm = c
        cost = np.concatenate([np.zeros(nr), np.ones(2 * nS)])
        Aeq = sp.hstack([sp.csr_matrix(M), sp.identity(nS, format="csr"), -sp.identity(nS, format="csr")], format="csr")
        res = linprog(cost, A_eq=Aeq, b_eq=c, bounds=bounds + [(0, None)] * (2 * nS), method="highs")
        rel = res.fun / np.abs(c).sum()
        feas.append((th, lam1, lam2, rel, res.x[:nr] if rel < 1e-7 else None))
    P("  angle(deg) lam1 lam2  min L1 residual / |q|_1   (0 => an on-site Theta-compatible decomposition exists)")
    for th, l1, l2, rel, gx in feas:
        if th % 15 == 0 or rel < 1e-7:
            P(f"   {th:5.0f}  {l1:+.3f} {l2:+.3f}   {rel:.3e}" + ("   FEASIBLE" if rel < 1e-7 else ""))
    fe = [f for f in feas if f[3] < 1e-7]
    P(f"  feasible angles: {[f[0] for f in fe]}")
    # Farkas certificate for the pure 10-channel X2 points with lambda2 != 0 (example: 45 deg)
    for th in (45.0, 135.0, 90.0, 270.0):
        lam1, lam2 = np.cos(np.radians(th)), np.sin(np.radians(th)); c = lam1 * q1 + lam2 * q2
        # y: (M^T y)_odd >= 0, (M^T y)_even <= 0, y.c = -1, minimise |y|_1  (y = yp - ym)
        Aub = []; bub = []
        for r in range(nr):
            row = M[:, r]
            if even[r]: Aub.append(np.concatenate([row, -row])); bub.append(0.0)      # M^T y <= 0
            else: Aub.append(np.concatenate([-row, row])); bub.append(0.0)            # -M^T y <= 0
        res = linprog(np.ones(2 * nS), A_ub=np.array(Aub), b_ub=bub, A_eq=np.concatenate([c, -c])[None, :], b_eq=[-1.0],
                      bounds=[(0, None)] * (2 * nS), method="highs")
        if res.status == 0:
            y = res.x[:nS] - res.x[nS:]; mty = M.T @ y
            viol = max(np.maximum(mty[even], 0).max(initial=0), np.maximum(-mty[~even], 0).max(initial=0))
            P(f"  Farkas certificate at {th:.0f} deg: y.c = {y @ c:+.6f}, max sign violation {viol:.1e}, |y|_1 = {np.abs(y).sum():.3f}, "
              f"support {np.sum(np.abs(y) > 1e-12)} components")
            np.save(f"farkas_k{k}_th{int(th)}.npy", np.vstack([np.pad(quads.T, ((0, 0), (0, 0))), y[None, :]]))
        else:
            P(f"  Farkas LP at {th:.0f} deg: status {res.status} (no certificate => feasible)")
    # ---------------- P3: any Spin(10)-invariant quartic in the cone with Delta F = 4 content?
    # derivative constraints D_z q(g) = 0 for z in spin(10) outside K; Delta F = 4 detector D_n q
    S3 = 2000
    def deriv_matrix(zlist):
        rows = []
        for z in zlist:
            Dz = np.zeros((S3, nr))
            for c, cl in enumerate(clusters):
                Vf = cl["Vfull"]; d = Vf.shape[1]
                Xc = np.zeros_like(Vf)
                for st in range(0, d, 128):
                    mats = np.array([vec_to_mat(Vf[:, cc]) for cc in range(st, min(d, st + 128))])
                    Xc[:, st:st + mats.shape[0]] = mats_to_vec(mats @ z - np.einsum("ij,bjk->bik", z, mats)).T
                for st in range(0, S3, 1000):
                    sl = slice(st, st + 1000)
                    t = 0
                    for (pa, pb), sgn in (((0, 1), 1), ((2, 3), -1), ((4, 5), 1)):
                        t = t + sgn * ((Xc[PIDX[pa][sl]] * Vf[PIDX[pb][sl]]).sum(1) + (Vf[PIDX[pa][sl]] * Xc[PIDX[pb][sl]]).sum(1))
                    Dz[sl, c] = t
            rows.append(-0.25 * Dz)
        return np.vstack(rows)
    Dout = deriv_matrix(outside)
    Dn = deriv_matrix([RZ])          # U(1)_F generator (realify(i 1))
    # sanity: q1 is Spin(10) and U(1) invariant, q2 Spin(10)-invariant but not U(1)
    g1, *_ = np.linalg.lstsq(M, q1, rcond=None); g2, *_ = np.linalg.lstsq(M, q2, rcond=None)
    P(f"  P3 sanity: |D_spin10 q1| = {np.abs(Dout @ g1).max():.1e}, |D_spin10 q2| = {np.abs(Dout @ g2).max():.1e}, "
      f"|D_n q1| = {np.abs(Dn @ g1).max():.1e}, |D_n q2| = {np.abs(Dn @ g2).max():.2e}")
    # LP: g in sign cone, |g| <= 1, Dout g = 0; maximise / minimise r.(Dn g) for random r
    nz = Dout.shape[0]
    best = 0.0
    for trial in range(6):
        r = rng.normal(size=Dn.shape[0])
        obj = Dn.T @ r
        for sgn in (1, -1):
            res = linprog(-sgn * obj, A_eq=Dout, b_eq=np.zeros(nz),
                          bounds=[(-1, 0) if e else (0, 1) for e in even], method="highs")
            best = max(best, abs(res.fun))
    gq2 = g2 / np.abs(g2).max()
    ref = max(abs((Dn @ gq2) @ rng.normal(size=Dn.shape[0])) for _ in range(6))
    P(f"  P3: max |r.(D_n q)| over Spin(10)-invariant sign-cone elements (|g|<=1): {best:.2e}; "
      f"same functional on the X2 BB term (|g|<=1, sign cone ignored): {ref:.2e}")
    results[k] = dict(clusters=len(clusters), feasible=[f[0] for f in fe], p3=best)
    P(f"  k={k} done in {time.time() - tk:.0f}s, peak RSS {mem():.0f} MB")
    del clusters, A, M, Dout, Dn

P("\nSUMMARY", {k: (v["clusters"], v["feasible"], f"{v['p3']:.1e}") for k, v in results.items()})
P(f"total {time.time() - t0:.0f}s, peak RSS {mem():.0f} MB")
