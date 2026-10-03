"""Structure of the rho=3 near-unitary covariant walk:
shell weights of A_v, values at the 8 TRIM, axis behaviour, and the effective
generator H_eff = i log W (Fourier shell weights) to test whether the walk is a
truncation of exp(-i H) with a short-range covariant H."""
import itertools
import numpy as np

mats = np.load('rho3_Amats.npy')
vecs = np.load('rho3_vecs.npy')
I2 = np.eye(2)
shell = np.max(np.abs(vecs), axis=1)
w = np.einsum('vab,vab->v', mats.conj(), mats).real
print("A_v weight by sup-norm shell:", {int(s): f"{w[shell == s].sum():.3e}" for s in range(4)})
l1 = np.sum(np.abs(vecs), axis=1)
print("A_v weight by l1 shell:", {int(s): f"{w[l1 == s].sum():.3e}" for s in range(10) if w[l1 == s].sum() > 0})


def W(k):
    return np.einsum('v,vab->ab', np.exp(-1j * vecs @ k), mats)


ph = None
print("W at the 8 TRIM (as multiple of identity):")
for K in itertools.product([0, np.pi], repeat=3):
    M = W(np.array(K))
    print("  ", tuple(int(round(x / np.pi)) for x in K), np.round(M[0, 0], 6), " offdiag", f"{abs(M[0,1]):.1e}", " diag diff", f"{abs(M[0,0]-M[1,1]):.1e}")
phase0 = W(np.zeros(3))[0, 0]
# axis: W(t,0,0) / phase0 = exp(-i m t sigma_x)?
for t in [0.3, 0.7, 1.1]:
    M = W(np.array([t, 0, 0])) / phase0
    ev = np.angle(np.linalg.eigvals(M))
    print(f"  axis t={t}: eigen-phases/t = {np.round(np.sort(ev) / t, 4)}")
for t in [0.3, 0.7]:
    M = W(np.array([t, t, t])) / phase0
    ev = np.angle(np.linalg.eigvals(M))
    print(f"  body-diag t={t}: eigen-phases/t = {np.round(np.sort(ev) / t, 4)}")
# effective generator on a grid
n = 24
g = np.arange(n) * 2 * np.pi / n
H = np.zeros((n, n, n, 2, 2), complex)
minabs = 10
for i, j, l in itertools.product(range(n), repeat=3):
    k = np.array([g[i], g[j], g[l]])
    M = W(k) / phase0
    ev, V = np.linalg.eig(M)
    minabs = min(minabs, np.min(np.abs(ev + 1)))
    H[i, j, l] = V @ np.diag(1j * np.log(ev)) @ np.linalg.inv(V)
print(f"min |eigenvalue + 1| on grid: {minabs:.3e}  (log branch safe if not ~0)")
Hv = np.fft.fftn(H, axes=(0, 1, 2)) / n ** 3  # coefficient of exp(-i k.v) at index v
sh = {}
for a, b, c in itertools.product(range(n), repeat=3):
    v = np.array([a, b, c])
    v = np.where(v > n // 2, v - n, v)
    s = int(np.max(np.abs(v)))
    sh[s] = sh.get(s, 0) + float(np.sum(np.abs(Hv[a, b, c]) ** 2))
print("H_eff weight by sup-norm shell:", {s: f"{sh[s]:.2e}" for s in sorted(sh) if s <= 6})
