"""Supervisor control for block 104: a clump of records under two clocks on a 24^3 torus at (3,1,2), c0 = 1/2.
(1) the rule's own clock (block 50): u = -log pi_x (pi_x the product of the record's pair weights c*omega; 1 elsewhere);
(2) block 53's clock: (1 - A)u = log(kappa) (n - nbar), log kappa = -gamma E_rec/6 with gamma E_rec = 0.6 (illustrative).
Prints u and r*u(r) along an axis from the clump, the pull -grad u on a test packet, and the sources' totals.
Then samples block 39's law with vacancies (Kawasaki exchanges, weight prod over adjacent record pairs of c*omega) at
densities 0.05 and 0.2 and reports the mean of the rule-clock source log kappa_x = u_x - avg_neighbours u at records,
at empty sites, and over all sites (zero exactly)."""
import numpy as np

rng = np.random.default_rng(3)
L = 24
E6 = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
pair = {"equal": 1.5, "opposite": 0.5, "orthogonal": 1.0}


def w_pair(a, b):
    if a == b:
        return 1.5
    if (E6[a] == -E6[b]).all():
        return 0.5
    return 1.0


def rule_clock_u(occ):
    u = np.zeros((L, L, L))
    for x, a in occ.items():
        lp = 0.0
        for e in E6:
            y = tuple((np.array(x) + e) % L)
            if y in occ:
                lp += np.log(w_pair(a, occ[y]))
        u[x] = -lp
    return u


def avg6(f):
    return sum(np.roll(f, s, axis=ax) for ax in range(3) for s in (1, -1)) / 6


# a compact clump: 27 records on a 3x3x3 block at the centre, contents drawn to favour alignment (illustrative)
c = L // 2
occ = {}
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            occ[(c + i, c + j, c + k)] = int(rng.choice(6, p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))
u1 = rule_clock_u(occ)
s1 = u1 - avg6(u1)
n = np.zeros((L, L, L))
for x in occ:
    n[x] = 1
lk = -0.1
src = lk * (n - n.mean())
k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
sym = 1 - (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
sym[0, 0, 0] = 1
uh = np.fft.fftn(src) / sym
uh[0, 0, 0] = 0
u2 = np.real(np.fft.ifftn(uh))
print(f"rule's clock: total source {s1.sum():+.2e}; field nonzero at {np.count_nonzero(np.abs(u1) > 1e-15)} sites (all inside the clump); records' mean source {np.mean([s1[x] for x in occ]):+.4f}")
print(f"block 53's clock: total source {src.sum():+.2e} after the mean is removed; monopole n log kappa = {len(occ) * lk:+.2f}")
print(" r   u_rule      u_53       r*u_53     pull_rule   pull_53 (x-component of -grad u at the test site)")
for r in range(2, 11):
    x = (c + r, c, c)
    gx1 = -(u1[(c + r + 1) % L, c, c] - u1[c + r - 1, c, c]) / 2
    gx2 = -(u2[(c + r + 1) % L, c, c] - u2[c + r - 1, c, c]) / 2
    print(f"{r:2d}  {u1[x]:+.3e}  {u2[x]:+.4e}  {r * u2[x]:+.4f}   {gx1:+.2e}   {gx2:+.3e}")

# block 39's law with vacancies at (3,1,2), c0: Kawasaki moves of records to empty neighbours and content redraws
def sample(density, sweeps=400):
    N = int(density * L ** 3)
    sites = rng.choice(L ** 3, N, replace=False)
    occ = {tuple(np.unravel_index(s, (L, L, L))): int(rng.integers(6)) for s in sites}
    keys = list(occ)

    def local(x, a, occ):
        lw = 0.0
        for e in E6:
            y = tuple((np.array(x) + e) % L)
            if y in occ:
                lw += np.log(w_pair(a, occ[y]))
        return lw
    for sw in range(sweeps):
        for _ in range(N):
            x = keys[rng.integers(len(keys))]
            a = occ[x]
            if rng.random() < 0.5:
                b = int(rng.integers(6))
                d = local(x, b, occ) - local(x, a, occ)
                if np.log(rng.random()) < d:
                    occ[x] = b
            else:
                y = tuple((np.array(x) + E6[rng.integers(6)]) % L)
                if y in occ:
                    continue
                del occ[x]
                d = local(y, a, occ) - local(x, a, occ)
                if np.log(rng.random()) < d:
                    occ[y] = a
                    keys[keys.index(x)] = y
                else:
                    occ[x] = a
    return occ


for dens in (0.05, 0.2):
    oc = sample(dens)
    u = rule_clock_u(oc)
    s = u - avg6(u)
    rec = np.zeros((L, L, L), bool)
    for x in oc:
        rec[x] = True
    print(f"block 39's law at density {dens}: mean source at records {s[rec].mean():+.4f}, at empty sites {s[~rec].mean():+.5f}, total over all sites {s.sum():+.1e}; mean u at records {u[rec].mean():+.4f}")
