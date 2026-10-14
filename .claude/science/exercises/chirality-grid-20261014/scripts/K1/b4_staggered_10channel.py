"""K1 test B4 (see ../PREREG.md): mean-field susceptibility of the 10-vector pairing channel at every corner
momentum Q, with BdG coherence factors.  Nambu spinor Psi_k = (psi_k, psi_{Q-k}^dag^T); per flavour component
(the 16-flavour matrix M with M^dag M = 1 factors out).  Pairing term Delta phi(k) psi_k^T (i sigma_y) psi_{Q-k} + h.c.
with phi(k) = f(k) f(Q-k).  E_0(Delta) = sum_k sum_{negative BdG eigenvalues} / 2; chi = -E_0''(0)."""
import numpy as np, itertools
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
isy = 1j * sy
def f_F1(p):
    s2 = np.sin(p / 2) ** 2; c2 = np.cos(p / 2) ** 2
    return 1 - (s2[0] * c2[1] * c2[2] + s2[1] * c2[0] * c2[2] + s2[2] * c2[0] * c2[1])
def f_NN(p): return (1 - np.cos(p[0]) - np.cos(p[1]) - np.cos(p[2])) / 2
def f_one(p): return np.ones_like(p[0])
filters = {"control f=1": f_one, "X2 f_F1": f_F1, "X2 f_NN": f_NN}
def hk(p):  # p: (3, n) -> (n, 2, 2)
    s = np.sin(p)
    return s[0][:, None, None] * sx + s[1][:, None, None] * sy + s[2][:, None, None] * sz
N = 40
k1 = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
K = np.stack(np.meshgrid(k1, k1, k1, indexing="ij")).reshape(3, -1)
def E0(f, Q, D):
    Qv = np.pi * np.array(Q, float)[:, None]
    p2 = Qv - K
    h1 = hk(K); h2 = hk(p2)
    phi = f(K) * f(p2)
    n = K.shape[1]
    H = np.zeros((n, 4, 4), complex)
    H[:, :2, :2] = h1
    H[:, 2:, 2:] = -np.transpose(h2, (0, 2, 1))
    A = D * phi[:, None, None] * isy
    H[:, :2, 2:] = A
    H[:, 2:, :2] = np.conj(np.transpose(A, (0, 2, 1)))
    ev = np.linalg.eigvalsh(H)
    return 0.5 * ev[ev < 0].sum() / n
corners = list(itertools.product((0, 1), repeat=3))
d = 2e-3
chi = {}
for name, f in filters.items():
    for Q in corners:
        chi[(name, Q)] = -(E0(f, Q, d) + E0(f, Q, -d) - 2 * E0(f, Q, 0.0)) / d ** 2
c0 = chi[("control f=1", (0, 0, 0))]
P(f"B4: grid N = {N} (midpoint), chi normalised to chi_control(Q=0) = {c0:.5f}")
for name in filters:
    row = {Q: round(chi[(name, Q)] / c0, 4) for Q in corners}
    best = max(row, key=row.get)
    P(f"  {name}: chi(Q)/chi_control(0) = {row}")
    P(f"     argmax Q = {best} (hw{sum(best)}), max ratio = {row[best]:.4f}")
# consistency with B1 (I[f] ratios at Q = 0): B1 gave I[F1]/I[1] = 0.3083, I[NN]/I[1] = 1.1455
P(f"  consistency: chi_F1(0)/chi_ctl(0) = {chi[('X2 f_F1',(0,0,0))]/c0:.4f} (B1: {0.28076/0.91066:.4f}); "
  f"chi_NN(0)/chi_ctl(0) = {chi[('X2 f_NN',(0,0,0))]/c0:.4f} (B1: {1.04312/0.91066:.4f})")
open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
