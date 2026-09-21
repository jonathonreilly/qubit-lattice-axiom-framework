"""Block 58 refuting pass (supervisor-run; machinery disjoint from the runner: floating-point dense solves, random arrangements, higher harmonic
weights, a non-linear solve of the record's bare energy with no closed form).
W1  twenty random amplitudes at rest in a 9^3 box: the record's bare energy found by ROOT-FINDING on the ledger (not by the closed form) agrees
    with E/(1 - (gamma/12) g_y E); the wall flux is unchanged by the event.
W2  the flux identity with harmonic weights beyond a coordinate: x^2 - y^2, xyz, x^2 + y^2 - 2 z^2: sum over wall bonds (1 - phi) h = 6 sum q h;
    so the walls see every harmonic moment, and the quadrupole jumps too.
W3  which density holds the centre: mean dipole jump over odds proportional to |chi|^2 (probability), |chi|^2 phi (charge), |chi|^2 phi^2
    (energy), for random amplitudes: zero only for the charge density.
W4  the ledger is a concave function of the vector of bare energies (random pairs), and on a box a record at the site of largest potential needs
    more bare energy than the amplitude had."""
import sys

import numpy as np
from scipy.optimize import brentq

results = []
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
SIDE, GAMMA = 9, 0.8
INTERIOR = [(x, y, z) for x in range(1, SIDE - 1) for y in range(1, SIDE - 1) for z in range(1, SIDE - 1)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
N = len(INTERIOR)
BASE = np.zeros((N, N)); RHS = np.zeros(N)
for s, i in INDEX.items():
    BASE[i, i] = 1
    for d in NEIGH:
        t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
        if t in INDEX:
            BASE[i, INDEX[t]] -= 1 / 6
        else:
            RHS[i] += 1 / 6
GREEN = np.linalg.inv(BASE)
COORD = np.array(INTERIOR, float)


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def rates(mvec):
    return np.linalg.solve(BASE + GAMMA / 12 * np.diag(mvec), RHS)


def wall_sum(phi, h):
    tot = 0.0
    for x in range(SIDE):
        for y in range(SIDE):
            for z in range(SIDE):
                if (x, y, z) in INDEX:
                    continue
                for d in NEIGH:
                    t = (x + d[0], y + d[1], z + d[2])
                    if t in INDEX:
                        tot += (1 - phi[INDEX[t]]) * h(x, y, z)
    return tot


rng = np.random.default_rng(58)


def random_amplitude(k):
    sites = rng.choice(N, k, replace=False)
    wts = rng.dirichlet(np.ones(k))
    m = float(rng.uniform(1, 6))
    mvec = np.zeros(N); mvec[sites] = m * wts
    return sites, wts, m, mvec


# ------------------------------------------------------------------------------------------------ W1
worst_formula, worst_flux = 0.0, 0.0
for _ in range(20):
    sites, wts, m, mvec = random_amplitude(int(rng.integers(3, 12)))
    phi = rates(mvec)
    ledger = float(mvec @ phi)
    y = int(rng.choice(sites))
    after = lambda mp: (lambda v: mp * rates(v)[y])(np.eye(N)[y] * mp) - ledger
    m_rec = brentq(after, 1e-9, 1e6)
    closed = ledger / (1 - GAMMA / 12 * GREEN[y, y] * ledger)
    worst_formula = max(worst_formula, abs(m_rec / closed - 1))
    phi2 = rates(np.eye(N)[y] * m_rec)
    worst_flux = max(worst_flux, abs(wall_sum(phi2, lambda *a: 1.0) - wall_sum(phi, lambda *a: 1.0)))
report("W1", worst_formula < 1e-9 and worst_flux < 1e-8, f"twenty random amplitudes: the bare energy of the record that keeps the ledger, found by root-finding, agrees with the closed form to {worst_formula:.1e}; the total wall flux changes by at most {worst_flux:.1e}")

# ------------------------------------------------------------------------------------------------ W2
sites, wts, m, mvec = random_amplitude(8)
phi = rates(mvec)
q = GAMMA / 12 * mvec * phi
harmonics = {"x": lambda x, y, z: x, "x^2 - y^2": lambda x, y, z: x * x - y * y, "x y z": lambda x, y, z: x * y * z, "x^2 + y^2 - 2 z^2": lambda x, y, z: x * x + y * y - 2 * z * z, "x^2 (not harmonic)": lambda x, y, z: x * x}
defects = {}
for name, h in harmonics.items():
    lhs = wall_sum(phi, h)
    rhs = 6 * sum(q[i] * h(*INTERIOR[i]) for i in range(N))
    defects[name] = abs(lhs - rhs) / max(1e-12, abs(rhs))
ok = all(v < 1e-10 for k, v in defects.items() if "not" not in k) and defects["x^2 (not harmonic)"] > 1e-3
report("W2", ok, "sum over wall bonds (1 - phi) h = 6 sum q h: relative defects " + ", ".join(f"{k}: {v:.1e}" for k, v in defects.items()) + ": every harmonic moment of the charges is seen at the walls; a weight that is not harmonic is not")

# ------------------------------------------------------------------------------------------------ W3
means = {"probability": [], "charge": [], "energy": []}
for _ in range(30):
    sites, wts, m, mvec = random_amplitude(int(rng.integers(4, 12)))
    phi = rates(mvec)
    qv = mvec * phi
    xbar = (qv[:, None] * COORD).sum(0) / qv.sum()
    dens = {"probability": mvec, "charge": mvec * phi, "energy": mvec * phi ** 2}
    for k, dv in dens.items():
        centre = (dv[:, None] * COORD).sum(0) / dv.sum()
        means[k].append(np.linalg.norm(centre - xbar))
report("W3", max(means["charge"]) < 1e-12 and min(means["probability"]) > 1e-6 and min(means["energy"]) > 1e-6,
       f"thirty random amplitudes: distance between the mean site of formation and the centre the walls see: odds by probability {np.mean(means['probability']):.2e} (smallest {min(means['probability']):.1e}), by charge {max(means['charge']):.1e}, by energy {np.mean(means['energy']):.2e} (smallest {min(means['energy']):.1e}) sites: only the charge density |chi|^2 phi holds the centre")

# ------------------------------------------------------------------------------------------------ W4
concave = True
for _ in range(200):
    a = rng.uniform(0, 5, N) * (rng.random(N) < 0.05)
    b = rng.uniform(0, 5, N) * (rng.random(N) < 0.05)
    la, lb, lm = a @ rates(a), b @ rates(b), ((a + b) / 2) @ rates((a + b) / 2)
    concave = concave and lm >= (la + lb) / 2 - 1e-12
more = True
ymax = int(np.argmax(np.diag(GREEN)))
for _ in range(20):
    sites, wts, m, mvec = random_amplitude(int(rng.integers(3, 10)))
    ledger = float(mvec @ rates(mvec))
    more = more and ledger / (1 - GAMMA / 12 * GREEN[ymax, ymax] * ledger) >= m
report("W4", concave and more, "the ledger is midpoint-concave in the vector of bare energies for 200 random pairs; a record at the site of largest potential needs at least the amplitude's bare energy in 20 random cases")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
