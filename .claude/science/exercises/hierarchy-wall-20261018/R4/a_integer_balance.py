"""Route A tests: an integer extent N fixed by a self-consistency balance.

a1: random exponential sums F(N) = sum_j c_j N^p_j exp(-k_j N); verify the
    proved bound N* <= [ln((J-1)R^2) + p_max ln N*]/Delta and record the
    largest k_light * N* reachable with O(1) inputs.
a2: 1D Wilson-Dirac ring with a kink/antikink mass profile at separation N.
    Measure the decay rate of the zero-mode splitting m(N) and of the Dirac-sea
    energy E(N) - E(inf); report the ratio and whether E(N) has any
    stationary point (an intrinsic selected N).
"""
import numpy as np
from scipy.optimize import brentq

rng = np.random.default_rng(20261018)
LSTAR = 38.4

print("== a1: exponential-sum zeros vs the bound ==")
viol = 0
best = []
for trial in range(6000):
    J = rng.integers(2, 6)
    R = float(rng.choice([2.0, 3.0, 10.0]))
    k = np.sort(rng.uniform(0.1, 3.0, J))
    # enforce distinct leading rate with gap; record Delta
    Delta = k[1] - k[0]
    if Delta < 1e-3:
        continue
    mag = np.exp(rng.uniform(-np.log(R), np.log(R), J))
    sgn = rng.choice([-1.0, 1.0], J)
    sgn[0] = -np.sign(sgn[1]) if sgn[1] != 0 else -1.0  # allow a sign change
    c = mag * sgn
    p = rng.integers(0, 3, J) if trial % 2 else np.zeros(J, dtype=int)
    # scaled by exp(k_1 N): same zeros, no underflow
    F = lambda N: np.sum(c * N ** p * np.exp(-(k - k[0]) * N))
    grid = np.linspace(1.0, 400.0, 4000)
    vals = (c[:, None] * grid[None, :] ** p[:, None] * np.exp(-(k - k[0])[:, None] * grid[None, :])).sum(0)
    roots = []
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            try:
                roots.append(brentq(F, grid[i], grid[i + 1]))
            except ValueError:
                pass
    if not roots:
        continue
    Ns = max(roots)
    pmax = p.max()
    bound = (np.log((J - 1) * R ** 2) + pmax * np.log(max(Ns, 1.0))) / Delta
    if Ns > bound * (1 + 1e-9):
        viol += 1
    # light-mode rate: any rate in the sum (spectral); worst case k_max
    best.append((k.max() * Ns, Delta / k.max(), R, J, int(pmax), Ns))
best.sort(reverse=True)
print(f"bound violations: {viol}  (instances with a zero: {len(best)})")
print("largest k_max*N* found (k_max N*, Delta/k_max, R, J, p_max, N*):")
for row in best[:5]:
    print("  " + ", ".join(f"{x:.3g}" for x in row))
o1 = [b for b in best if b[1] >= 0.2 and b[2] <= 10]
print(f"O(1) class (Delta/k_max >= 0.2, R <= 10): max k_max*N* = {max(b[0] for b in o1):.2f}"
      f"  vs L* = {LSTAR}")
print("required Delta/kappa for L* (J=2, p=0): R=3 ->",
      f"{np.log(9)/LSTAR:.3f}", " R=10 ->", f"{np.log(100)/LSTAR:.3f}")
print("required multiplicity n = kappa/Delta: R=3 ->", f"{LSTAR/np.log(9):.1f}",
      " R=10 ->", f"{LSTAR/np.log(100):.1f}",
      " R^2 = 1/alpha_LM (=11.0) ->", f"{LSTAR/np.log(11.0):.1f}")

print()
print("== a2: Wilson-Dirac kink/antikink ring ==")
def ring_spectrum(L, N, M0, r=1.0):
    # h(k) = sin k sx + (M + r(1-cos k)) sz  in real space, 2 components/site
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    H = np.zeros((2 * L, 2 * L), dtype=complex)
    Mx = np.full(L, M0)
    Mx[:N] = -M0
    hop = (-0.5j) * sx - 0.5 * r * sz  # x -> x+1 block
    for x in range(L):
        H[2*x:2*x+2, 2*x:2*x+2] = (Mx[x] + r) * sz
        y = (x + 1) % L
        H[2*x:2*x+2, 2*y:2*y+2] = hop
        H[2*y:2*y+2, 2*x:2*x+2] = hop.conj().T
    return np.linalg.eigvalsh(H)

for M0 in (0.3, 0.6):
    L = 320
    Ns = np.arange(4, 41, 2)
    msplit, Esea = [], []
    for N in Ns:
        ev = ring_spectrum(L, int(N), M0)
        msplit.append(np.min(np.abs(ev)))
        Esea.append(ev[ev < 0].sum())
    msplit = np.array(msplit); Esea = np.array(Esea)
    Einf = ring_spectrum(L, L // 2, M0)
    Einf = Einf[Einf < 0].sum()
    dE = Esea - Einf
    sel = Ns >= 10
    km = -np.polyfit(Ns[sel], np.log(msplit[sel]), 1)[0]
    # E(N) = a + b N + exponential: the Wilson term makes the bulk energy of
    # +M0 and -M0 differ (linear 'pressure' b). Remove it by second differences.
    d2 = Esea[2:] - 2 * Esea[1:-1] + Esea[:-2]
    N2 = Ns[1:-1]
    good = (N2 >= 10) & (np.abs(d2) > 1e-12)
    kE = -np.polyfit(N2[good], np.log(np.abs(d2[good])), 1)[0] / 1.0
    bpress = np.polyfit(Ns[Ns >= 30], Esea[Ns >= 30], 1)[0]
    # analytic zero-mode decay inside the -M0 region for r = 1: |1 - M0| per site
    # (Wilson-Dirac zero mode: psi_{x+1} = (1 - M0) psi_x)
    kz = -np.log(abs(1 - M0))
    dEdN = np.diff(Esea)
    stationary = np.any(np.sign(dEdN[1:]) != np.sign(dEdN[:-1]))
    print(f"   linear pressure dE/dN (bulk energy difference of -M0 vs +M0) = {bpress:.4e}")
    print(f"M0={M0}: rate of m(N) = {km:.4f}, rate of E''(N) = {kE:.4f}, "
          f"ratio = {kE/km:.3f}, analytic -ln|1-M0| = {kz:.4f}")
    print(f"   sign of dE/dN over N=4..40: {sorted(set(np.sign(dEdN).astype(int)))}; "
          f"stationary point in fermion sector alone: {bool(stationary)}")
    print(f"   m(N=40)/M0 = {msplit[-1]/M0:.3e}")
