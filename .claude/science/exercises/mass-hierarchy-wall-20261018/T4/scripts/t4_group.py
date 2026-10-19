"""T-F3 task 1-2: residual elements, bilinear irreps, cross operators allowed by G, symmetry checks,
and Michel stationarity / non-stationarity of the joint F3 point."""
import itertools, numpy as np
from t4_core import *
import t4_inv as TI
rng = np.random.default_rng(11)
print("|B3| =", len(B3))
print("g_l  (C3[111] through a site) =", G_L.tolist())
print("g_nu (C2[110] o T(e3), axis through (0,0,1/2)) =", G_NU.tolist(), "; site-centred C2[110] ->", G_NU_SITE.tolist())
H = close([G_L, G_NU]); Hs = close([G_L, G_NU_SITE])
def commutant(gs):
    C = sum(np.kron(g, g) for g in gs) / len(gs); return int(round(np.trace(C)))
print(f"<g_l, g_nu>: order {len(H)}, contains -1: {any(np.allclose(h,-np.eye(3)) for h in H)}, commutant dim on triplet {commutant(H)} (1 = irreducible)")
print(f"<g_l, site C2[110]>: order {len(Hs)}, commutant dim {commutant(Hs)}")
print("  => a G-covariant map from ONE state to both mass matrices, generic coefficients, gives each sector the state's stabilizer;")
print("     requiring both residuals forces the stabilizer to contain <g_l,g_nu>, irreducible -> Schur -> degenerate masses.")
# ---- bilinear irreps ----
def rep_on(proj):
    basis = []
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3)); E[i, j] = 1; basis.append(proj(E).ravel())
    U, S, Vt = np.linalg.svd(np.array(basis)); r = int((S > 1e-10).sum()); Vb = Vt[:r]
    return [Vb @ np.array([act(g, v.reshape(3, 3)).ravel() for v in Vb]).T for g in B3], r
chars = {}
for nm, pr in PROJ.items():
    R, r = rep_on(pr)
    com = sum(np.kron(A, A) for A in R) / len(R)
    chars[nm] = np.array([np.trace(A) for A in R])
    print(f"irrep {nm}: dim {r}, commutant {int(round(np.trace(com)))} (1=irreducible); g_l-fixed dim {fixed_dim(G_L, nm)[0]}, g_nu-fixed dim {fixed_dim(G_NU, nm)[0]}")
names = list(PROJ)
G = np.array([[chars[a] @ chars[b] / len(B3) for b in names] for a in names])
print("character inner products (identity => four inequivalent irreps, each multiplicity 1 in 3x3):\n", G.round(6))
print("Dirac  rho(x)rho = A1+E+3M+3M' ; Majorana S^2 rho = A1+E+3M  (3M' is antisymmetric)  -> Majorana irreps are a subset of Dirac irreps")
print("T(1,1,1) image:", rep_tr((1, 1, 1)).diagonal().tolist(), "-> acts trivially on every bilinear (s_i s_j = 1)")
# ---- which components each residual keeps ----
# C3-fixed Dirac matrices: span{I, C+C^2, C-C^2}; g_nu-fixed symmetric: [[A,B,D],[B,A,-D],[D,-D,F]]
C = G_L.astype(float)
for nm in names:
    K = PROJ[nm](C); print(f"  projection of C onto {nm}: nonzero = {np.linalg.norm(K) > 1e-12}")
# ---- lemma: charged leptons need 3M (sym) and 3M' (antisym) at the C3 point ----
worst = 0
for _ in range(200000):
    a, b = rng.normal(size=2) + 1j * rng.normal(size=2)
    M = a * np.eye(3) + b * (C - C.T)                          # A1 + 3M'(1,1,1) only
    lam = np.linalg.eigvals(M); m0 = abs(a); m12 = sorted(abs(l) for l in lam if abs(l - a) > 1e-12)
    if len(m12) == 2: worst = max(worst, (m12[1] - m12[0]) / (2 * m0))
print(f"A1+3M' only (e = trivial character): max over 2e5 draws of (m_heavy - m_mid)/(2 m_e) = {worst:.6f} (proved <= 1); data need {(ML[2]-ML[1])/(2*ML[0]):.0f}")
M = 0.3 * np.eye(3) + 0.7 * (C + C.T); print("A1+3M only: singular values", np.linalg.svd(M)[1].round(6), "(mu-tau degenerate)")
# ---- representative joint F3 point (data-fit) ----
th = THETA0
Ml = Ml0(rng.uniform(0, 2 * np.pi, 3), False); Mn = Mnu0(th, 0.4, nu_masses(1e-3), rng.uniform(0, 2 * np.pi, 3))
U, _, _ = pmns(Ml, Mn); print("check unperturbed:", {k: round(v, 5) for k, v in obs(U).items()})
print("  g_l-invariance of M_l:", np.allclose(act(G_L, Ml), Ml), "; g_nu-invariance of M_nu:", np.allclose(act(G_NU, Mn), Mn),
      "; M_l g_nu-inv:", np.allclose(act(G_NU, Ml), Ml), "; M_nu g_l-inv:", np.allclose(act(G_L, Mn), Mn))
# linear cross insertions: does phi_nu's content leak into M_l and phi_l's into M_nu?
for nm in ['E', '3M']:
    K = PROJ[nm](Mn); print(f"  phi_nu has {nm} component: {np.linalg.norm(K)/np.linalg.norm(Mn):.3f}; that component is g_l-invariant: {np.allclose(act(G_L,K),K)}")
K = pM(Ml); print(f"  phi_l has 3M component: {np.linalg.norm(K)/np.linalg.norm(Ml):.3f}; g_nu-invariant: {np.allclose(act(G_NU,K),K)}")
# ---- invariant ring ----
invs, bideg = TI.invariants(4)
from collections import Counter
cnt = Counter(bideg)
print("\nG-invariant polynomials in (mR,mI,nR,nI | DR,DI,pR,pI), orbit-sum basis, counts by (deg_l, deg_nu):")
for d in range(1, 5):
    row = {k: v for k, v in sorted(cnt.items()) if sum(k) == d}; print(f"  degree {d}: {row}")
cross = [k for k, b in enumerate(bideg) if b[0] > 0 and b[1] > 0]
z2 = [k for k in cross if bideg[k][0] % 2 == 0 and bideg[k][1] % 2 == 0]
print(f"  cross-sector invariants (deg<=4): {len(cross)}; even in each sector (survive Z2xZ2 shaping): {len(z2)}")
# U(1)xU(1)-invariant combinations of cross invariants (numerical nullspace), per bidegree
Zs = rng.normal(size=(1500, TI.NV)); Zr = TI.u1_rotate(Zs, rng.uniform(0, 6.3, 1500), 0) ; Zr2 = TI.u1_rotate(Zs, 0, rng.uniform(0, 6.3, 1500))
u1_basis = {}
for b in sorted(set(bideg[k] for k in cross)):
    ks = [k for k in cross if bideg[k] == b]
    A = np.vstack([TI.inv_values([invs[k] for k in ks], Zr) - TI.inv_values([invs[k] for k in ks], Zs),
                   TI.inv_values([invs[k] for k in ks], Zr2) - TI.inv_values([invs[k] for k in ks], Zs)])
    U_, S_, Vt_ = np.linalg.svd(A, full_matrices=False); null = Vt_[np.sum(S_ > 1e-8 * S_[0]):] if len(S_) else Vt_
    u1_basis[b] = (ks, null)
    print(f"  bidegree {b}: {len(ks)} invariants, U(1)xU(1)-invariant combinations: {null.shape[0]}")
# ---- Michel: within-sector stationarity and cross-term non-stationarity at the joint F3 point ----
z0 = TI.zfrom(Ml - pA1(Ml), Mn); z0[TI.IL] /= np.linalg.norm(z0[TI.IL]); z0[TI.IN] /= np.linalg.norm(z0[TI.IN])
A_l = TI.rep24(G_L); A_n = TI.rep24(G_NU)
def fixproj(A, idx):
    P = np.zeros((TI.NV, TI.NV)); Asub = A[np.ix_(idx, idx)]; k = order(G_L if A is A_l else G_NU)
    Pf = sum(np.linalg.matrix_power(Asub, j) for j in range(k)) / k; P[np.ix_(idx, idx)] = Pf; return P
Pl = fixproj(A_l, TI.IL); Pn = fixproj(A_n, TI.IN); Pfix = Pl + Pn; Pbr = np.eye(TI.NV) - Pfix
print(f"\njoint F3 point: in Fix(g_l)+Fix(g_nu): {np.allclose(Pfix@z0, z0)}; dim Fix_l = {round(np.trace(Pl))}, dim Fix_nu = {round(np.trace(Pn))}")
stab = [g for g, A in zip(B3, TI.REPS) if np.allclose(A @ z0, z0)]
print(f"stabilizer of the joint point in B3: order {len(stab)} (2 = only +-1)")
def brgrad(ks):
    out = []
    for k in ks:
        g = TI.Poly([invs[k]], [1.0]).grad(z0); out.append(np.linalg.norm(Pbr @ g))
    return np.array(out)
pure_l = [k for k, b in enumerate(bideg) if b[1] == 0]; pure_n = [k for k, b in enumerate(bideg) if b[0] == 0]
print(f"max breaking-gradient over pure-l invariants: {brgrad(pure_l).max():.2e}; pure-nu: {brgrad(pure_n).max():.2e}  (Michel: 0)")
gx = brgrad(cross)
for lab, ks in [("all cross", cross), ("Z2xZ2-even cross", z2)]:
    gg = brgrad(ks); print(f"{lab}: {np.sum(gg > 1e-10)}/{len(ks)} have nonzero breaking gradient at the joint point; median |grad_br| {np.median(gg[gg>1e-10]):.3f}")
nz_u1 = 0; tot_u1 = 0
for b, (ks, null) in u1_basis.items():
    for v in null:
        g = sum(c * TI.Poly([invs[k]], [1.0]).grad(z0) for c, k in zip(v, ks)); tot_u1 += 1; nz_u1 += np.linalg.norm(Pbr @ g) > 1e-10
print(f"U(1)xU(1)-invariant cross combinations: {nz_u1}/{tot_u1} have nonzero breaking gradient")
# lowest-degree examples
low = min((sum(bideg[k]), k) for k in cross if gx[cross.index(k)] > 1e-10)
names24 = [f"{f[0]}{i}" for f in TI.FIELDS for i in range(3)]
k = low[1]; print(f"lowest-degree misaligning cross invariant: degree {low[0]}, bidegree {bideg[k]}:",
              " + ".join(f"{c:+.3g}*" + "*".join(names24[v] for v in m) for m, c in list(invs[k].items())[:6]))
ex = [k for k in z2 if sum(bideg[k]) == 4 and gx[cross.index(k)] > 1e-10][0]
print("example Z2xZ2-even (shaping-proof) misaligning quartic:", " + ".join(f"{c:+.3g}*" + "*".join(names24[v] for v in m) for m, c in list(invs[ex].items())[:6]), "...")
# explicit hand example: sum_k |m_k|^2 |p_k|^2 (U(1)xU(1) and Z2xZ2 invariant; B3-invariant, not O(3)-invariant)
def handI(z):
    m = z[0:3] + 1j * z[3:6]; p = z[18:21] + 1j * z[21:24]; return np.sum(np.abs(m) ** 2 * np.abs(p) ** 2)
inv_ok = all(abs(handI(A @ zz) - handI(zz)) < 1e-12 for A in TI.REPS for zz in rng.normal(size=(3, TI.NV)))
eps = 1e-6; gh = np.array([(handI(z0 + eps * e) - handI(z0 - eps * e)) / (2 * eps) for e in np.eye(TI.NV)])
print(f"hand invariant sum_k |m_k|^2|p_k|^2: B3-invariant {inv_ok}; |breaking gradient| at joint point = {np.linalg.norm(Pbr@gh):.4f}")
np.save('t4_z0.npy', z0)
