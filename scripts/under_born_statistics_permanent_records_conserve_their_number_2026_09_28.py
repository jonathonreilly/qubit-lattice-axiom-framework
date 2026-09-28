#!/usr/bin/env python3
"""Under Born statistics, records that are never destroyed conserve their number.

Setting: a finite lattice; a record configuration says which sites hold a
record; a wave psi over configurations evolves by a Hermitian H; the records'
actual configuration follows any stochastic law that is equivariant (its
configuration distribution is |psi_t|^2 at every time). Bell's minimal jump law
max(0, J_yx)/P(x) is one such law.

Theorem (proved in the note):
  (i) If records are never destroyed, for every initial psi, then H commutes
      with the record number N.
  (ii) For a single state over all time (finite system): if its records are
      never destroyed, its Born count distribution is constant in time.
  (iii) Conversely, if [H, N] = 0 then Bell's law never changes N, and a site
      gains a record only when a record arrives through a nonzero matrix
      element of H (from a neighbour, for a nearest-neighbour H).

Checks:
A. The proof's key step: for H with hopping and local formation terms,
   X_n = i[H, Pi_{N>=n}] is traceless and indefinite; evolving its most
   negative eigenvector for a short time lowers P(N >= n), so an equivariant
   law must destroy records in that state.
B. Converse: for number-conserving hopping, Bell's rates between
   configurations of different N vanish and the count distribution of a random
   state is constant in time.
C. Formation from nothing: hard-core records on a ring of 8 with hopping and
   a local formation term g sigma^x, starting with no records. The mean count
   rises, but P(N >= 1) falls again at t ~ 1.5, and at late times Bell's
   destruction flux is comparable to its creation flux.
D. Arrival: a Bell trajectory under number-conserving nearest-neighbour
   hopping; every gain of a record at a site coincides with a neighbour's loss
   (the record arrived).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import numpy as np
from scipy.linalg import eigh, expm

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


L = 8; DIM = 2 ** L
CONF = np.array(list(itertools.product((0, 1), repeat=L)))
NREC = CONF.sum(1)
IDX = {tuple(c): i for i, c in enumerate(CONF)}


def hamiltonian(hop, g, rng=None):
    H = np.zeros((DIM, DIM), complex)
    for i, c in enumerate(CONF):
        for x in range(L):
            y = (x + 1) % L
            if c[x] != c[y]:
                d = c.copy(); d[x], d[y] = c[y], c[x]
                amp = hop if rng is None else hop * (1 + 0.3 * rng.normal())
                H[IDX[tuple(d)], i] += -amp
            if g:
                d = c.copy(); d[x] = 1 - c[x]; H[IDX[tuple(d)], i] += g
    return (H + H.conj().T) / 2 if rng is not None else H


def bell_currents(psi, H):
    return 2 * np.imag(np.conj(psi)[:, None] * H * psi[None, :])  # J[y, x]: flow x -> y


# ---------------------------------------------------------------- A the key step
H = hamiltonian(1.0, 0.4)
rows = []
for n in (1, 2, 4):
    Pi = np.diag((NREC >= n).astype(float))
    X = 1j * (H @ Pi - Pi @ H)
    ev, vec = np.linalg.eigh(X)
    psi = vec[:, 0]
    dt = 1e-3
    p0 = np.real(psi.conj() @ Pi @ psi); p1 = np.real((expm(-1j * H * dt) @ psi).conj() @ Pi @ (expm(-1j * H * dt) @ psi))
    rows.append((n, abs(np.trace(X)), ev[0], ev[-1], (p1 - p0) / dt))
check("A: i[H, Pi_{N>=n}] is traceless and indefinite, so some state loses records at once (an equivariant law must destroy them)",
      all(tr < 1e-12 and lo < -0.1 and hi > 0.1 and rate < -0.1 for _, tr, lo, hi, rate in rows),
      "; ".join(f"n={n}: trace {tr:.0e}, eigenvalues [{lo:.3f}, {hi:.3f}], dP/dt of the worst state {rate:.3f}" for n, tr, lo, hi, rate in rows))

# ---------------------------------------------------------------- B converse
rng = np.random.default_rng(1)
Hc = hamiltonian(1.0, 0.0, rng)
psi = rng.normal(size=DIM) + 1j * rng.normal(size=DIM); psi /= np.linalg.norm(psi)
J = bell_currents(psi, Hc)
cross = np.max(np.abs(J[NREC[:, None] != NREC[None, :]]))
w, V = eigh(Hc)
counts = []
for t in (0.0, 1.0, 5.0, 20.0):
    pt = np.abs(V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))) ** 2
    counts.append(np.array([pt[NREC == k].sum() for k in range(L + 1)]))
drift = max(np.max(np.abs(c - counts[0])) for c in counts)
check("B: with number-conserving hopping, Bell's rates never change the record number and the count distribution is constant",
      cross < 1e-14 and drift < 1e-12, f"largest current between different counts {cross:.1e}; count-distribution drift {drift:.1e}")

# ---------------------------------------------------------------- C formation from nothing
w, V = eigh(H)
psi0 = np.zeros(DIM, complex); psi0[0] = 1
ts = np.linspace(0, 60, 3001)
PN1 = []; mean = []; cre = des = 0.0
for t in ts:
    ps = V @ (np.exp(-1j * w * t) * (V.conj().T @ psi0)); p = np.abs(ps) ** 2
    PN1.append(p[NREC >= 1].sum()); mean.append(p @ NREC)
    if t > 30:
        Jt = bell_currents(ps, H)
        cre += np.sum(np.maximum(0, Jt)[NREC[:, None] > NREC[None, :]]); des += np.sum(np.maximum(0, Jt)[NREC[:, None] < NREC[None, :]])
PN1 = np.array(PN1); drop = np.diff(PN1)
first = ts[1 + np.argmax(drop < -1e-6)]
check("C: records formed from nothing by a local formation term are destroyed again: P(N >= 1) falls, and late destruction flux is comparable to creation flux",
      drop.min() < -1e-3 and 0.5 < cre / des < 2 and max(mean) > 1,
      f"mean count at t = 1, 2, 4: {[round(mean[int(t / 0.02)], 3) for t in (1, 2, 4)]}; P(N>=1) first falls at t = {first:.2f}; "
      f"late creation/destruction flux ratio {cre / des:.2f}")

# ---------------------------------------------------------------- D arrival
rngD = np.random.default_rng(4)
psi = rngD.normal(size=DIM) + 1j * rngD.normal(size=DIM); psi /= np.linalg.norm(psi)
w, V = eigh(Hc)
state = rngD.choice(DIM, p=np.abs(psi) ** 2)
dt = 0.005; gains = arrivals = 0
for step in range(4000):
    ps = V @ (np.exp(-1j * w * step * dt) * (V.conj().T @ psi))
    P = np.abs(ps) ** 2
    Jt = bell_currents(ps, Hc)[:, state]
    rates = np.maximum(0, Jt) / max(P[state], 1e-300)
    u = rngD.random()
    cum = np.cumsum(rates * dt)
    if u < cum[-1]:
        new = int(np.searchsorted(cum, u))
        old_c, new_c = CONF[state], CONF[new]
        gained = np.where((new_c == 1) & (old_c == 0))[0]; lost = np.where((new_c == 0) & (old_c == 1))[0]
        for x in gained:
            gains += 1
            arrivals += any(((x - y) % L) in (1, L - 1) for y in lost)
        state = new
check("D: under number-conserving nearest-neighbour hopping, every gain of a record at a site is an arrival from a neighbour",
      gains > 20 and arrivals == gains, f"{gains} gains, {arrivals} from a neighbour that lost its record in the same jump")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
