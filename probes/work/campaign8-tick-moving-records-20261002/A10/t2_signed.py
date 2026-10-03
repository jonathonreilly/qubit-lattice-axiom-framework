"""t2: signed (Kogut-Susskind sign) cycle.  Clifford structure, nodes, cone shape."""
import numpy as np, itertools
from cyc import cycle, layer

rng = np.random.default_rng(2)
pi = np.pi

def Dop(K, a, par, signed=True):
    th = 0.3
    L = layer(K, a, par, th, signed) * np.exp(-1j * th)
    return (L - np.cos(th) * np.eye(8)) / (-1j * np.sin(th))

# (a) D^2 = 1, D hermitian, {D_a, D_b} = 0 for different axes (signed); [D_a, D_b] = 0 (plain)
ea = eb = ec = 0.0
for t in range(100):
    K = rng.uniform(-pi, pi, 3)
    Ds = {(a, p): Dop(K, a, p, True) for a in range(3) for p in (0, 1)}
    Dp = {(a, p): Dop(K, a, p, False) for a in range(3) for p in (0, 1)}
    for k1, D1 in Ds.items():
        ea = max(ea, np.abs(D1 @ D1 - np.eye(8)).max(), np.abs(D1 - D1.conj().T).max())
        for k2, D2 in Ds.items():
            if k1[0] != k2[0]:
                eb = max(eb, np.abs(D1 @ D2 + D2 @ D1).max())
                ec = max(ec, np.abs(Dp[k1] @ Dp[k2] - Dp[k2] @ Dp[k1]).max())
print(f"(a) D^2=1, hermitian: {ea:.1e};  signed: max|{{D_a,D_b}}| = {eb:.1e};  plain: max|[D_a,D_b]| = {ec:.1e}")

# (b) Hamiltonian (Trotter) limit H = sum D : E = +-2 sqrt(sum cos^2(K_a/2)), each 4-fold
eh = 0.0
for t in range(100):
    K = rng.uniform(-pi, pi, 3)
    H = sum(Dop(K, a, p) for a in range(3) for p in (0, 1))
    E = np.sort(np.linalg.eigvalsh(H))
    e0 = 2 * np.sqrt(np.sum(np.cos(K / 2) ** 2))
    eh = max(eh, np.abs(E - np.array([-e0] * 4 + [e0] * 4)).max())
print(f"(b) sum of D's: spectrum +-2 sqrt(sum cos^2(K/2)) 4-fold each, max dev {eh:.1e}")

# (c) Floquet signed cycle: K* = (pi,pi,pi); degeneracy and cone slopes in many directions
Ks = np.array([pi, pi, pi])
for th in [0.05, pi / 8, pi / 4, 3 * pi / 8, 0.49 * pi]:
    U0 = cycle(Ks, th, signed=True)
    deg = np.abs(U0 - np.exp(6j * th) * np.eye(8)).max()
    d = 1e-5
    sl = []
    for n in [np.array([1., 0, 0]), np.array([0, 1., 0]), np.array([0, 0, 1.]),
              np.array([1., 1, 0]), np.array([1., 1, 1]), np.array([1., -1, 1])] + [rng.normal(size=3) for _ in range(6)]:
        n = n / np.linalg.norm(n)
        ph = np.sort(np.angle(np.linalg.eigvals(cycle(Ks + d * n, th, signed=True)) * np.exp(-6j * th))) / d
        sl.append(ph)
    sl = np.array(sl)
    print(f"(c) th={th:.4f}: |U(K*)-e^(6i th)|={deg:.1e}; slopes (rows=directions):")
    print("    min/max |slope| over bands+dirs:", f"{np.abs(sl).min():.6f} {np.abs(sl).max():.6f}",
          "  theta=", f"{th:.6f}", " sin(th)=", f"{np.sin(th):.6f}")
    print("    axis   :", np.round(sl[0], 6))
    print("    diag111:", np.round(sl[4], 6))
