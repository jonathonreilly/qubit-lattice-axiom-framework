"""K2 part 2c: naive / staggered fermion on Z^4 (Euclidean).

Naive Dirac: S = sum psibar [sum_mu g_mu D_mu + m] psi, D_mu symmetric difference (symbol i sin k).
Claims checked:
 (1) exact pseudo-rotation L_w = sum w_{rs} x_r F_s + Sigma_w with
       F_s = two-step symmetric difference (symbol i/2 sin 2k_s),
       Sigma_w = -1/4 sum_ab w_ab g_a g_b S_a S_b   (S = neighbour average, symbol cos k)
     commutes with the Dirac operator exactly:  [Dirac, L_w] = 0   (real space, open box).
 (2) under spin diagonalisation psi = Gamma(x) chi, Gamma(x)=g1^x1 g2^x2 g3^x3 g4^x4, every shift
     used by F and Sigma maps to a scalar phase -> L_w acts on ONE staggered component.
 (3) Killing closure: [L_w, F_r] has symbol  w_{rs} f_s cos 2k_r  (f = sin2k/2), not a translation
     mod EOM: certificate on the complex shell sum sin^2 k = -m^2.
 (4) on-shell symmetric-stress criterion (Gordon): v g_mu u = (sin k_mu / m) v u on the shell.
"""
import numpy as np, itertools
rng = np.random.default_rng(5)
# Euclidean Hermitian gamma matrices
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
g = [np.kron(s1, s) for s in (s1, s2, s3)] + [np.kron(s2, I2)]
for a in range(4):
    for b in range(4):
        assert np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(4))
D = 4
def sh(F, mu, n):  # F shape (4, L,L,L,L) spinor first
    return np.roll(F, -n, axis=mu + 1)
def Dsym(F, mu): return 0.5 * (sh(F, mu, 1) - sh(F, mu, -1))
def Savg(F, mu): return 0.5 * (sh(F, mu, 1) + sh(F, mu, -1))
def F2(F, mu): return 0.25 * (sh(F, mu, 2) - sh(F, mu, -2))
def gmul(G, F): return np.einsum('ij,j...->i...', G, F)
def dirac(F, m): return sum(gmul(g[mu], Dsym(F, mu)) for mu in range(D)) + m * F
n = 14
X = np.indices((n,) * D).astype(float)
def Lw(F, w, sign):
    out = np.zeros_like(F)
    for r in range(D):
        for s_ in range(D):
            if w[r, s_] != 0:
                out += w[r, s_] * X[r][None] * F2(F, s_)
    for a in range(D):
        for b in range(D):
            if w[a, b] != 0:
                out += sign * (-0.25) * w[a, b] * gmul(g[a] @ g[b], Savg(Savg(F, a), b))
    return out
print("== (1) exact pseudo-rotation of the naive Dirac operator (open box, compact support) ==")
for (a, b) in [(3, 0), (0, 1), (2, 3)]:
    w = np.zeros((D, D)); w[a, b] = 1; w[b, a] = -1
    for sign in (+1, -1):
        worst = 0.0
        for m in (0.0, 0.5):
            psi = np.zeros((4,) + (n,) * D, complex)
            psi[(slice(None),) + (slice(4, -4),) * D] = rng.integers(-5, 6, size=(4,) + (n - 8,) * D)
            comm = dirac(Lw(psi, w, sign), m) - Lw(dirac(psi, m), w, sign)
            worst = max(worst, np.abs(comm).max())
        print(f"plane ({a},{b}) spin-term sign {sign:+d}: max |[Dirac, L_w] psi| = {worst:.3e}")
print("(the sign that gives 0 is the exact symmetry; delta psi = L psi, delta psibar = -psibar L)")

print("\n== (2) spin diagonalisation: shifts used by L map to scalar phases ==")
def Gam(x):
    M = np.eye(4, dtype=complex)
    for mu in range(D):
        M = M @ np.linalg.matrix_power(g[mu], int(x[mu]) % 2)
    return M
worst = 0.0
for x in itertools.product(range(2), repeat=D):
    x = np.array(x)
    for a in range(D):
        for b in range(D):
            if a == b: continue
            for sa in (1, -1):
                for sb in (1, -1):
                    y = x.copy(); y[a] += sa; y[b] += sb
                    M = np.linalg.inv(Gam(x)) @ g[a] @ g[b] @ Gam(y)
                    worst = max(worst, np.abs(M - M[0, 0] * np.eye(4)).max())
    for mu in range(D):
        for s_ in (2, -2):
            y = x.copy(); y[mu] += s_
            M = np.linalg.inv(Gam(x)) @ Gam(y)
            worst = max(worst, np.abs(M - M[0, 0] * np.eye(4)).max())
print("max deviation from scalar phase over all parity classes, diagonal and two-step shifts:", worst)
print("=> F (two-step) and Sigma (diagonal shifts x gamma_a gamma_b) act within one staggered component:")
print("   the staggered fermion inherits exact pseudo-translations and pseudo-rotations.")

print("\n== (3) Killing closure for the fermion ==")
# [L_w, F_r]: V . grad f_r with V_r = sum_s w_rs f_s, f = sin(2k)/2  ->  w_rs f_s cos 2k_r
def shell(m2, N):
    pts = []
    while len(pts) < N:
        kj = rng.normal(size=3) * 0.7 + 1j * rng.normal(size=3) * 0.3
        target = -m2 - np.sum(np.sin(kj) ** 2)        # sin^2 k4 = target
        k4 = np.arcsin(np.sqrt(target + 0j))
        k = np.concatenate([kj, [k4]])
        if abs(np.sum(np.sin(k) ** 2) + m2) < 1e-10: pts.append(k)
    return np.array(pts)
for m2 in (0.25, 1.0):
    P = shell(m2, 400); rels = []
    for (a, b) in [(3, 0), (0, 1)]:
        w = np.zeros((D, D)); w[a, b] = 1; w[b, a] = -1
        for r in range(D):
            R = np.array([sum(w[r, s_] * 0.5 * np.sin(2 * k[s_]) for s_ in range(D)) * np.cos(2 * k[r]) for k in P])
            B = np.array([[0.5 * np.sin(2 * k[s_]) for s_ in range(D)] for k in P])
            if np.linalg.norm(R) < 1e-12: continue
            c, *_ = np.linalg.lstsq(B, R, rcond=None)
            rels.append(np.linalg.norm(B @ c - R) / np.linalg.norm(R))
    print(f"m2={m2}: best translation fit of [L_w, F_r] on the shell: relative residual min/max = {min(rels):.3f}/{max(rels):.3f}")

print("\n== (4) Gordon identity on the complex shell (symmetric-stress criterion) ==")
worst = 0.0
for k in shell(0.49, 20):
    m = 0.7
    Dk = 1j * sum(g[mu] * np.sin(k[mu]) for mu in range(D)) + m * np.eye(4)
    U, S, Vh = np.linalg.svd(Dk)
    u = Vh.conj().T[:, -1]             # right null
    v = U[:, -1].conj()                # left null: v Dk = 0
    vu = v @ u
    for mu in range(D):
        lhs = v @ g[mu] @ u
        rhs = -1j * np.sin(k[mu]) / m * vu   # from v{i g_mu, Dk}u = 0
        worst = max(worst, abs(lhs - rhs) / max(abs(vu), 1e-12))
print("max |v g_mu u - (-i sin k_mu / m) v u| / |v u| =", f"{worst:.2e}")
print("=> zero-momentum on-shell current of translation f: ~ (v dD/dk_mu u) f_nu ~ sin k_mu cos k_mu f_nu;")
print("   symmetric in (mu,nu) iff f_nu ~ sin 2k_nu: the staggered two-step pseudo-momentum (L1's spectrum).")
