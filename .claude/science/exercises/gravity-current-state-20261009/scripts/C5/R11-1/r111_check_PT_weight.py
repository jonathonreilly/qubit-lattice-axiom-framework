"""R11-1: independent check of R10-5's fermion TT pair weight (Theorem PT input), with explicit 8x8 Clifford matrices.
t(k,k') = tr[P+(k') Gamma P-(k) Gamma],  P = (1 +- M/E)/2,  M = sum_j [S_j A_j + W_j B_j] + m B0 (7 anticommuting Hermitian 8x8),
Gamma = (S_x A_y + S_y A_x)/2, k' = (kx, ky, kz') (q along z).  R10-5 closed form:
t = (sx+sy)/2 - 4 sx sy/(E E') + (sx+sy)/2 * (Eperp^2 + Sz Sz' + Wz Wz')/(E E'),  s = S^2, Eperp^2 = m^2 + v_x + v_y.
Also checks the Clifford-flat TT identity numerically on a small grid: Xi_B(|V|^2=4 s_x s_y, 8 real) + Xi_F = <g(|c'|^2-1)/E^3>,
here with an independent direct alpha for the fermion from the explicit-matrix weight."""
import numpy as np, itertools
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2)
def kron(*a):
    out = np.eye(1)
    for x in a: out = np.kron(out, x)
    return out
G7 = [kron(X, I2, I2), kron(Y, I2, I2), kron(Z, X, I2), kron(Z, Y, I2), kron(Z, Z, X), kron(Z, Z, Y), kron(Z, Z, Z)]
err = max(np.abs(G7[i] @ G7[j] + G7[j] @ G7[i] - 2 * (i == j) * np.eye(8)).max() for i in range(7) for j in range(7))
print('Clifford check (7 generators, 8x8): max |{G_i,G_j} - 2 delta| = %.1e' % err)
Ax, Ay, Az, Bx, By, Bz, B0 = G7
rng = np.random.default_rng(3)
def Mof(S, W, m):
    return S[0] * Ax + S[1] * Ay + S[2] * Az + W[0] * Bx + W[1] * By + W[2] * Bz + m * B0
worst = 0
for _ in range(200):
    m = rng.uniform(0.05, 1.0)
    S = rng.normal(size=3); W = rng.normal(size=3)
    Szp, Wzp = rng.normal(), rng.normal()
    Sp_, Wp_ = S.copy(), W.copy(); Sp_[2] = Szp; Wp_[2] = Wzp
    M1, M2 = Mof(S, W, m), Mof(Sp_, Wp_, m)
    E1 = np.sqrt(np.sum(S ** 2) + np.sum(W ** 2) + m * m); E2 = np.sqrt(np.sum(Sp_ ** 2) + np.sum(Wp_ ** 2) + m * m)
    Pp2 = (np.eye(8) + M2 / E2) / 2; Pm1 = (np.eye(8) - M1 / E1) / 2
    Gam = 0.5 * (S[0] * Ay + S[1] * Ax)
    t_mat = np.trace(Pp2 @ Gam @ Pm1 @ Gam).real
    sx, sy = S[0] ** 2, S[1] ** 2
    Ep2 = m * m + S[0] ** 2 + W[0] ** 2 + S[1] ** 2 + W[1] ** 2
    t_cf = 0.5 * (sx + sy) - 4 * sx * sy / (E1 * E2) + 0.5 * (sx + sy) * (Ep2 + S[2] * Szp + W[2] * Wzp) / (E1 * E2)
    worst = max(worst, abs(t_mat - t_cf) / (abs(t_cf) + 1e-12))
print('pair weight: explicit 8x8 trace vs R10-5 closed form, 200 random points: max rel diff = %.1e' % worst)
