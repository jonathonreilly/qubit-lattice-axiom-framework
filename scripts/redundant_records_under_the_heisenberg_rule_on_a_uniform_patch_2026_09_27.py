#!/usr/bin/env python3
"""Redundant records under the dynamics clause's Heisenberg rule on a uniform 4x4 patch.

Question (pre-registered by the viability map's foundations lens): if records
are not primitive but emerge as facts copied redundantly into the surroundings
(option A, "quantum Darwinism"; reference only: Zurek 2009, Riedel and Zurek
2010), does a single site of a uniform lattice under a nearest-neighbour
unitary rule become such a record?

Setting: 16 spin-1/2 sites on a 4x4 open patch, H = sum over nearest-neighbour
bonds of sx.sx + sy.sy + sz.sz (the Heisenberg rule of the dynamics-clause
lane, as a comparator). Site 0 (a corner) starts in (|0> + |1>)/sqrt 2; the
other 15 start in a product state: either all |0>, or independent random pure
states (seed 7). The state is evolved exactly (Krylov exponential), no large
matrix is ever built.

Measures, with H(S) the entropy of site 0 in bits:
  I(S:F) averaged over random environment fragments F of size f;
  redundancy R_0.1 = 15 / f_min, with f_min the smallest f where the average
  I(S:F) >= 0.9 H(S);
  predictability sieve: H(S) at time t for site 0 started in a z, x or y
  eigenstate (the most stable basis has the lowest entropy).

Pre-registered criteria: success if R_0.1 >= 3 over a window of times with a
stable sieve winner; failure if R_0.1 < 2 at all times, or the sieve winner is
not stable; otherwise inconclusive.

Checks:
A. Random product environment: R_0.1 < 2 at every time t = 1, 2, 4 (failure).
B. Random product environment: the site is close to maximally mixed and the
   sieve has no winner (z, x, y entropies within 0.1 bit of each other).
C. Random product environment: I(S:F) stays below 0.1 H(S) for every fragment
   up to 4 of the 15 sites, and passes H(S) only from 8 sites (the Page-curve
   shape: the bit is available only from more than half of the surroundings).
D. All-|0> environment: the site barely decoheres (H(S) < 0.25 bit at every
   time); the flipped spin leaves as a single magnon, so there is no bit at
   the site to be recorded (the redundancy is not defined when H(S) is ~0).

Prints one line per check and `TOTAL: PASS=N FAIL=M`. Runtime about 6 minutes.
"""
import numpy as np
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex)
Lx = Ly = 4; n = 16
idx = lambda x, y: x * Ly + y
BONDS = [(idx(x, y), idx(x + dx, y + dy)) for x in range(Lx) for y in range(Ly)
         for dx, dy in ((1, 0), (0, 1)) if x + dx < Lx and y + dy < Ly]


def apply_h(psi):
    T = np.asarray(psi, complex).reshape([2] * n); out = np.zeros_like(T)
    for i, j in BONDS:
        for S in (SX, SY, SZ):
            X = np.moveaxis(np.tensordot(S, T, axes=([1], [i])), 0, i)
            X = np.moveaxis(np.tensordot(S, X, axes=([1], [j])), 0, j)
            out += X
    return out.reshape(-1)


H = spla.LinearOperator((2 ** n, 2 ** n), matvec=apply_h, rmatvec=apply_h, dtype=complex)


def evolve(psi0, t):
    return spla.expm_multiply(-1j * H, psi0, start=0, stop=t, num=2, endpoint=True, traceA=0.0)[-1]


def entropy(psi, A):
    B = [i for i in range(n) if i not in A]
    X = A if len(A) <= len(B) else B
    T = psi.reshape([2] * n); rest = [i for i in range(n) if i not in X]
    M = np.transpose(T, X + rest).reshape(2 ** len(X), -1)
    w = np.linalg.eigvalsh(M @ M.conj().T); w = w[w > 1e-14]
    return float(-np.sum(w * np.log2(w)))


def info_curve(psi, rng, samples=6):
    env = list(range(1, n)); hs = entropy(psi, [0]); out = []
    for f in range(1, n):
        vals = []
        for _ in range(samples if f < n - 1 else 1):
            F = sorted(rng.choice(env, size=f, replace=False).tolist())
            vals.append(hs + entropy(psi, F) - entropy(psi, [0] + F))
        out.append(float(np.mean(vals)))
    return hs, out


def redundancy(hs, cur, delta=0.1):
    fmin = next((f for f, v in enumerate(cur, 1) if v >= (1 - delta) * hs), None)
    return (n - 1) / fmin


rng_env = np.random.default_rng(7)
RANDOM_ENV = [None] + [(lambda v: v / np.linalg.norm(v))(rng_env.normal(size=2) + 1j * rng_env.normal(size=2)) for _ in range(1, n)]


def product(site0, kind):
    st = np.array(site0, complex)
    for i in range(1, n):
        st = np.kron(st, np.array([1, 0], complex) if kind == 'up' else RANDOM_ENV[i])
    return st


SIEVE = {'z': [1, 0], 'x': [1 / np.sqrt(2), 1 / np.sqrt(2)], 'y': [1 / np.sqrt(2), 1j / np.sqrt(2)]}
rng = np.random.default_rng(11)
rows = {}
for kind in ('random', 'up'):
    psi0 = product(np.array([1, 1]) / np.sqrt(2), kind)
    for t in (1, 2, 4):
        ps = evolve(psi0, t)
        hs, cur = info_curve(ps, rng)
        sieve = {b: entropy(evolve(product(np.array(v, complex), kind), t), [0]) for b, v in SIEVE.items()}
        rows[(kind, t)] = (hs, cur, redundancy(hs, cur) if hs > 1e-6 else float('nan'), sieve)
        print(f"  {kind:6s} t={t}: H(S)={hs:.3f}  R_0.1={rows[(kind, t)][2]:.2f}  "
              f"I/H at f=1,2,4,8,15: {[round(cur[f - 1] / max(hs, 1e-12), 2) for f in (1, 2, 4, 8, 15)]}  "
              f"sieve {{{', '.join(f'{b}: {s:.3f}' for b, s in sieve.items())}}}", flush=True)

R = [rows[('random', t)][2] for t in (1, 2, 4)]
check("A: random product surroundings: the redundancy stays below 2 at every time (the pre-registered failure)",
      all(r < 2 for r in R), f"R_0.1 at t = 1, 2, 4: {[round(r, 2) for r in R]}")
spread = [max(rows[('random', t)][3].values()) - min(rows[('random', t)][3].values()) for t in (1, 2, 4)]
hsr = [rows[('random', t)][0] for t in (1, 2, 4)]
check("B: random product surroundings: the site is close to maximally mixed and the sieve picks no basis",
      all(h > 0.8 for h in hsr) and all(s < 0.1 for s in spread),
      f"H(S) {[round(h, 3) for h in hsr]}; sieve spread {[round(s, 3) for s in spread]} bit")
page = [(max(rows[('random', t)][1][f - 1] for f in (1, 2, 3, 4)) / rows[('random', t)][0],
         rows[('random', t)][1][7] / rows[('random', t)][0]) for t in (1, 2, 4)]
check("C: random product surroundings: fragments of up to 4 sites hold under 10% of the bit, 8 sites hold more than all of it "
      "(Page-curve shape: only more than half of the surroundings knows)",
      all(small < 0.1 and big > 1.0 for small, big in page), f"(max I/H for f<=4, I/H at f=8): {[(round(a, 3), round(b, 2)) for a, b in page]}")
hsu = [rows[('up', t)][0] for t in (1, 2, 4)]
check("D: all-|0> surroundings: the site barely decoheres (the flipped spin leaves as one magnon)",
      all(h < 0.25 for h in hsu), f"H(S) at t = 1, 2, 4: {[round(h, 3) for h in hsu]} bit")
print('per_element: reduced density matrices and entropies are computed exactly from the 16-site state vector (no sampling of the state).')
print('per_site: the system is one corner site; its entropy and the predictability sieve (z, x, y) are computed at t = 1, 2, 4.')
print('per_mode: checked and not executed - the test is posed in the site basis; no mode-resolved redundancy is computed.')
print('per_block: mutual information with random environment fragments of every size 1..15 (6 samples each) gives the redundancy curve.')
print('lattice_wide: checked and not executed - one 4x4 patch with the Heisenberg rule only; the trend with size and other rules are not tested.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
