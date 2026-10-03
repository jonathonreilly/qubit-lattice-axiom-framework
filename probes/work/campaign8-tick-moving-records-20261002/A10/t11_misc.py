"""t11: (1) closed Pauli-string form of the signed cycle; (2) angle-staggering mass is taste-universal;
(3) R1 (cut every tick, Born jump odds) record motion is a persistent random walk (diffusive)."""
import numpy as np
from scipy.linalg import expm
from vcyc import layers_U, plain6, strang9
pi = np.pi
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Yp = np.array([[0, -1j], [1j, 0]]); Zp = np.diag([1., -1.])
def k3(z, y, x): return np.kron(z, np.kron(y, x))       # factor order (z, y, x); x = least significant bit
def D(axis, par, K, signed):
    h = X if par == 0 else (np.cos(K[axis]) * X + np.sin(K[axis]) * Yp)
    if axis == 0: return k3(I2, I2, h)
    if axis == 1: return k3(I2, h, Zp if signed else I2)
    return k3(h, Zp if signed else I2, Zp if signed else I2)
def closed(K, lay, signed):
    U = np.eye(8, dtype=complex)
    for (a, p, th) in lay:
        U = np.exp(1j * th) * expm(-1j * th * D(a, p, K, signed)) @ U
    return U
rng = np.random.default_rng(11)
err = 0.0
for t in range(50):
    K = rng.uniform(-pi, pi, 3)
    for lay, sg in [(plain6(0.7), False), (plain6(0.7), True), (strang9(0.5), True)]:
        err = max(err, np.abs(closed(K, lay, sg) - layers_U(K[None], lay, sg)[0]).max())
print(f"(1) closed Pauli-string form vs layer builder: {err:.1e}")

# (2) mass from angle staggering on x only: Strang block x_e(te/2) x_o(to) x_e(te/2)
te, to, th = 0.5, 0.42, 0.46
lay = [(0, 0, te / 2), (0, 1, to), (0, 0, te / 2)] + [(a, p, ang) for a in (1, 2) for (p, ang) in ((0, th / 2), (1, th), (0, th / 2))]
U = layers_U(np.array([[pi, pi, pi]]), lay, True)[0]
ph = np.angle(np.linalg.eigvals(U) * np.exp(-1j * (te + to + 4 * th)))
print(f"(2) K* relative eigenphases with te-to={te-to:.2f} on x: {np.round(np.sort(ph), 6)}")

# (3) R1: record cut every tick, jump to the current partner with odds sin^2 th (1D, cycling e/o)
def r1_var(th, ncyc, N=4001):
    p = np.sin(th) ** 2
    P = np.zeros(N); P[N // 2] = 1.0          # start on an even site (N//2 even)
    x = np.arange(N) - N // 2
    out = []
    for c in range(ncyc):
        for par in (0, 1):
            Q = (1 - p) * P
            # partner of site i in parity layer par: i+1 if (i-par) even else i-1
            idx = np.arange(N)
            right = ((idx - par) % 2 == 0)
            Q[1:][right[:-1]] += p * P[:-1][right[:-1]]
            Q[:-1][~right[1:]] += p * P[1:][~right[1:]]
            P = Q
        out.append((P * x ** 2).sum())
    return np.array(out)
for th in (0.6, pi / 4, pi / 2):
    v = r1_var(th, 400)
    n = np.arange(1, 401)
    print(f"(3) R1 th={th:.3f}: <x^2>/n at n=100,400: {v[99]/100:.3f}, {v[399]/400:.3f};  <x^2>/n^2 at 400: {v[399]/400**2:.4f}")
