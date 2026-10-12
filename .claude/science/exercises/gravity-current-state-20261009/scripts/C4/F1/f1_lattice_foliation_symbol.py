"""F1 (lane RF): the lattice VS/N-type tensor theory with the lapse demoted from gauge multiplier
to a field (non-projectable, khronometric-type), on Z^3 lattice symbols.

Setting (supplied, a test setting; nothing here is derived from the axioms):
  canonical symmetric h_ij, E_ij (6+6 slots); midpoint placement => continuum symbols with
  k -> qh = 2 sin(k/2) (09-14 note convention).
  Vector constraint G = qh_i E_ij = 0 kept EXACT (first class); its gauge h -> qh_(i xi_j) quotiented.
  Scalar constraint S DROPPED as a gauge constraint; lapse n becomes an auxiliary field:
    H = 1/2 E.K.E + (g/2) h:R(h) + g_n n S(h) + 1/2 D(qh) n^2 + n rho
    K = kA1 P_A1 + kE P_E + kT2 P_T2  (cubic: 3 kinetic numbers; isotropic DeWitt: kE=kT2=J, kA1=J(1-3c))
    D(qh) = -2 a qh^2 + mu_n            (a <-> khronometric alpha; mu_n = lapse mass, forbidden by
                                          time reparametrization, allowed otherwise)
  GR normalisation: g = 1/2, g_n = 1, J = 2 (c_T = 1), c = 1/2 (lambda = 1).
Checks:
  (A) TT: omega^2 = J g qh^2; cubic anisotropy kE != kT2 splits TT speeds by direction.
  (B) scalar (khronon): omega^2 = J (1-2c) (g_n^2/a - g) qh^2  == GSS c_S^2 with beta = 0,
      alpha = a, c = lambda/(3 lambda - 1), lambda = 1 + gamma.
  (C) static source: Newtonian 1/k^2 with G_N ~ 1/(g_n^2/g - a), PPN gamma = g_n/(2g);
      lapse mass mu_n != 0 -> n*k^2 -> 0 (no 1/r).
  (D) projectable limit (no n(x)): omega^2 = -(1-2c) J g qh^2 (RN L3 check).
"""
import numpy as np
np.set_printoptions(precision=6, suppress=True)

# basis of Sym^2(R^3): orthonormal under A:B
def sym_basis():
    B = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; B.append(M)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); B.append(M)
    return B
BAS = sym_basis()
def vec(M): return np.array([np.sum(M * b) for b in BAS])
def mat(v): return sum(v[a] * BAS[a] for a in range(6))

eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items():
    eps[i, j, k] = s

def R_op(q):
    """Linearised incompatibility R_ij = eps_iab eps_jcd d_a d_c h_bd, d -> i q (so d d -> -q q),
    overall sign chosen so that h_TT:R(h_TT) = +q^2 |h_TT|^2 (09-14 note)."""
    M = np.zeros((6, 6))
    for b in range(6):
        h = BAS[b]
        R = np.einsum('iab,jcd,a,c,bd->ij', eps, eps, q, q, h)
        M[:, b] = vec(R)
    return M  # sign fixed below by test

def S_vec(q):
    """S(h) = Delta tr h - d_i d_j h_ij -> -q^2 tr h + q_i q_j h_ij ; returns row vector s with S = s.h"""
    s = np.zeros(6)
    for b in range(6):
        h = BAS[b]
        s[b] = -q @ q * np.trace(h) + q @ h @ q
    return s

def gauge_dirs(q):
    G = []
    for j in range(3):
        xi = np.zeros(3); xi[j] = 1
        M = 0.5 * (np.outer(q, xi) + np.outer(xi, q))
        G.append(vec(M))
    return np.array(G).T  # 6x3

def K_op(kA1, kE, kT2):
    PA1 = np.zeros((6, 6)); PE = np.zeros((6, 6)); PT2 = np.zeros((6, 6))
    tr = np.array([1, 1, 1, 0, 0, 0]) / np.sqrt(3)
    PA1 = np.outer(tr, tr)
    Pdiag = np.diag([1, 1, 1, 0, 0, 0]).astype(float)
    PE = Pdiag - PA1
    PT2 = np.diag([0, 0, 0, 1, 1, 1]).astype(float)
    return kA1 * PA1 + kE * PE + kT2 * PT2

def transverse_basis(q):
    """orthonormal basis (6x3) of {h : q_i h_ij = 0} = orthogonal complement of gauge dirs."""
    G = gauge_dirs(q)
    U, s, Vt = np.linalg.svd(G, full_matrices=True)
    return U[:, 3:]

def spectrum(k, J=2.0, c=0.5, aniso=0.0, g=0.5, g_n=1.0, a=None, mu_n=0.0, projectable=False):
    q = 2 * np.sin(np.asarray(k, float) / 2)
    qq = q @ q
    R = R_op(q)
    # fix sign: TT test
    T = transverse_basis(q)
    kA1, kE, kT2 = J * (1 - 3 * c), J, J * (1 + aniso)
    K = K_op(kA1, kE, kT2)
    V = g * R
    if not projectable:
        s = S_vec(q)
        D = -2 * a * qq + mu_n
        V = V - (g_n ** 2) * np.outer(s, s) / D
    KT = T.T @ K @ T
    VT = T.T @ V @ T
    w2 = np.linalg.eigvals(KT @ VT)
    return np.sort(w2.real) / qq, q

# --- sign test of R
q = 2 * np.sin(np.array([0, 0, 0.3]) / 2)
R = R_op(q)
hTT = vec(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / np.sqrt(2))
val = hTT @ R @ hTT
print(f"sign test: h_TT:R(h_TT) / q^2 = {val/(q@q):+.6f}  (should be +1)")
SIGN = np.sign(val)
_R = R_op
def R_op(q):  # noqa: F811
    return SIGN * _R(q)
# gauge invariance checks
for kk in [np.array([0.3, 0.1, -0.2]), np.array([1.1, 2.0, 0.4])]:
    qv = 2 * np.sin(kk / 2)
    Gd = gauge_dirs(qv)
    print(f"gauge invariance k={kk}: |R G| = {np.abs(R_op(qv) @ Gd).max():.1e}, |S G| = {np.abs(S_vec(qv) @ Gd).max():.1e}")

print("\n(A)+(B) spectra omega^2/qh^2 on the transverse quotient (GR normalisation g=1/2, g_n=1, J=2)")
def gss_cs2(alpha, gamma, beta=0.0):
    return (2 - alpha) * (gamma + beta) / (alpha * (1 - beta) * (2 + 3 * gamma + beta))
for (alpha, gamma) in [(0.1, 0.05), (1e-3, 0.01), (0.5, 0.2), (1e-6, 0.01)]:
    lam = 1 + gamma
    c = lam / (3 * lam - 1)
    for k in [np.array([0, 0, 0.05]), np.array([0.03, 0.04, 0.02]), np.array([0.9, 0.4, 1.3])]:
        w, q = spectrum(k, J=2.0, c=c, g=0.5, g_n=1.0, a=alpha)
        print(f"  alpha={alpha:.0e} gamma={gamma}: k={k}: omega^2/qh^2 = {w}  ; GSS c_S^2 = {gss_cs2(alpha, gamma):.6f}, c_T^2 = 1")

print("\n(A') cubic kinetic anisotropy kT2 = kE(1+aniso): TT speeds^2 by direction (alpha=0.1,gamma=0.05)")
lam = 1.05; c = lam / (3 * lam - 1)
for aniso in [0.0, 1e-3]:
    for d in [[0, 0, 1], [1, 1, 0], [1, 1, 1], [0.3, 0.7, 0.2]]:
        k = 1e-3 * np.array(d, float) / np.linalg.norm(d)
        w, q = spectrum(k, J=2.0, c=c, aniso=aniso, g=0.5, g_n=1.0, a=0.1)
        print(f"  aniso={aniso:.0e} dir={d}: omega^2/qh^2 = {w}")

print("\n(D) projectable limit (lapse n(t) only): omega^2/qh^2, expect TT = J g = 1, scalar = -(1-2c) J g")
for gamma in [0.05, -0.1]:
    lam = 1 + gamma; c = lam / (3 * lam - 1)
    w, q = spectrum(np.array([0.01, 0.02, 0.03]), J=2.0, c=c, g=0.5, projectable=True)
    print(f"  lambda={lam}: c={c:.4f}: {w}; -(1-2c)Jg = {-(1-2*c)*2*0.5:+.6f}")

print("\n(C) static response to a point source rho (k -> 0): n(k) k^2 and PPN gamma = Psi/Phi")
def static(k, g=0.5, g_n=1.0, a=0.1, mu_n=0.0):
    """Extremise E = (g/2) h.R.h + g_n n S.h + 1/2 D n^2 + n*rho over transverse h (gauge fixed) and n."""
    q = 2 * np.sin(np.asarray(k, float) / 2); qq = q @ q
    T = transverse_basis(q)
    R = R_op(q); s = S_vec(q)
    D = -2 * a * qq + mu_n
    # variables x = (h_T (3), n); E = 1/2 x.M.x + b.x
    M = np.zeros((4, 4))
    M[:3, :3] = g * T.T @ R @ T
    M[:3, 3] = M[3, :3] = g_n * (s @ T)
    M[3, 3] = D
    b = np.zeros(4); b[3] = 1.0  # rho = 1
    x = -np.linalg.solve(M, b)
    h = T @ x[:3]; n = x[3]
    H = mat(h)
    # Psi from the transverse trace: h_perp = sigma P, Psi = -sigma/2; sigma = tr(h)/2 (h transverse, TT part zero)
    sigma = np.trace(H) / 2
    Psi = -sigma / 2
    return n * qq, Psi / n
for (g_n, a, mu) in [(1.0, 0.1, 0.0), (1.0, 1e-6, 0.0), (1.02, 0.1, 0.0), (1.0, 0.1, 1e-4), (1.0, 0.1, 1e-2)]:
    rows = []
    for kk in [1e-1, 1e-2, 1e-3]:
        nk2, gam = static(np.array([0, 0.6, 0.8]) * kk, g_n=g_n, a=a, mu_n=mu)
        rows.append(f"|k|={kk:.0e}: n k^2={nk2:+.5f}, gamma={gam:.5f}")
    pred = -1 / (2 * (g_n ** 2 / 0.5 - a))
    print(f"  g_n={g_n}, alpha={a:.0e}, mu_n={mu:.0e}:  " + " | ".join(rows) + f"   [pred n k^2 = {pred:+.5f}, gamma = g_n/(2g) = {g_n:.3f}]")
