"""t10: palindromic signed cycle XYZZYX (Strang blocks): symmetry (dressing+shift), spectrum symmetry,
zero/pi quasienergy states away from K* vs angle."""
import numpy as np, itertools
from vcyc import layers_U
import t5_sym as T5        # reuses rots, P_of, lams, axis_perm_parity (prints its own results first)
pi = np.pi
rng = np.random.default_rng(10)
def blk(a, phi): return [(a, 0, phi / 2), (a, 1, phi), (a, 0, phi / 2)]
def pal18(phi): return blk(0, phi) + blk(1, phi) + blk(2, phi) + blk(2, phi) + blk(1, phi) + blk(0, phi)
lay = pal18(0.3)
print("---- t10 ----")
Ksr = rng.uniform(-pi, pi, (3, 3))
shifts = [lay[r:] + lay[:r] for r in range(len(lay))]
okl = []
for M in T5.rots:
    P = T5.P_of(M)
    A = np.einsum("ij,njk,lk->nil", P, layers_U(Ksr, lay, True), P)
    B_all = [layers_U(Ksr @ M.T, sl, True) for sl in shifts]
    best = min(np.abs(A - L @ B @ L).max() for B in B_all for L in T5.lams)
    perm = [int(np.nonzero(M[:, i])[0][0]) for i in range(3)]
    okl.append((best < 1e-10, perm))
print("palindrome-18 signed: rotations symmetric up to dressing+shift:", sum(o for o, _ in okl), "of 24;",
      "axis permutations realized:", sorted({tuple(p) for o, p in okl if o}))
Ks = rng.uniform(-pi, pi, (100, 3))
ph0 = np.sort(np.angle(np.linalg.eigvals(layers_U(Ks, lay, True))), axis=1)
dev = max(np.abs(np.sort(np.angle(np.linalg.eigvals(layers_U(Ks @ M.T, lay, True))), axis=1) - ph0).max() for M in T5.rots)
print(f"palindrome-18 signed: spectrum invariant under all 24 rotations of K: max dev {dev:.1e}")
N = 24
g = np.arange(N) * 2 * pi / N - pi
KK = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
Kst = np.array([pi, pi, pi])
dist = np.linalg.norm(((KK - Kst) + pi) % (2 * pi) - pi, axis=1)
for phi in [0.1, 0.2, 0.3, 0.35, 0.4, 0.45]:
    L0 = pal18(phi)
    ref = np.exp(1j * np.angle(np.linalg.eigvals(layers_U(Kst[None], L0, True)[0])[0]))
    ph = np.angle(np.linalg.eigvals(layers_U(KK, L0, True)) * np.conj(ref))
    f0 = np.abs(ph).min(1)[dist > 0.6].min(); fpi = (pi - np.abs(ph)).min()
    print(f"palindrome phi={phi:.2f}: min |qe| away from K* = {f0:.4f}; min distance to qe pi = {fpi:.4f}; "
          f"max |qe| = {np.abs(ph).max():.4f}")
