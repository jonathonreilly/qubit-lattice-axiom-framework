"""A9 task 3 illustration: 'records form where energy is' for one excitation (supplied toy).

1D ring of N qubits. Vacuum = all sites in the same possibility |u> (a quiet ferromagnetic
vacuum). Change = Heisenberg ferromagnet H = J sum_bonds P_singlet (frustration-free;
the vacuum has zero energy), run for time tau per tick, keeping locked possibilities.
Formation effect at an unrecorded site x (SU(2)-covariant, relational, linear):
    F_x = c * sum_{y in N(x)} P_singlet(x, y)        (local excitation energy, c = 1/3)
  variant A: bonds to recorded neighbours count (their locked content is a classical condition)
  variant B: only bonds to unrecorded neighbours count
Menu at a forming site: {u, d}. Instrument: Kraus P_k sqrt(F_x); no record: sqrt(1 - F_x).
Schedule: three passes per tick over the sublattices x = 0, 1, 2 (mod 3); windows within a
pass are disjoint, so their instruments commute.

One flipped possibility (a magnon) stays one magnon until it is recorded ('d' locked).
In the one-magnon sector P_singlet(x,y) = |a><a| with a = (e_x - e_y)/sqrt2, so F_x measures
the local gradient (kinetic) energy |psi_x - psi_y|^2 / 2.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(20261003)
N, J, TAU, C = 30, 1.0, 0.5, 1.0 / 3.0
UNL, UP, DN = 0, 1, 2


def psd_sqrt(a):
    lam, w = np.linalg.eigh((a + a.conj().T) / 2)
    return (w * np.sqrt(np.clip(lam, 0, None))) @ w.conj().T


def window_mats(left, right, variant):
    """3x3 matrices on (x-1, x, x+1) for an unrecorded x with neighbour states left/right."""
    M = np.zeros((3, 3), complex)
    for j, st in ((0, left), (2, right)):
        if st == UNL:
            a = np.zeros(3); a[1] = 1 / np.sqrt(2); a[j] = -1 / np.sqrt(2)
            M += C * np.outer(a, a)
        elif st == UP and variant == "A":
            M[1, 1] += C * 0.5
    return psd_sqrt(M), psd_sqrt(np.eye(3) - M)


MATS = {(v, l, r): window_mats(l, r, v) for v in "AB" for l in (UNL, UP) for r in (UNL, UP)}


def change(status):
    H = np.zeros((N, N), complex)
    for x in range(N):
        y = (x + 1) % N
        sx, sy = status[x], status[y]
        if sx == UNL and sy == UNL:
            H[x, x] += J / 2; H[y, y] += J / 2; H[x, y] -= J / 2; H[y, x] -= J / 2
        elif sx == UNL and sy == UP:
            H[x, x] += J / 2
        elif sy == UNL and sx == UP:
            H[y, y] += J / 2
    return expm(-1j * TAU * H)


def total_chance(psi, status, variant):
    tot = 0.0
    for x in range(N):
        if status[x] != UNL:
            continue
        sF, _ = MATS[(variant, status[(x - 1) % N], status[(x + 1) % N])]
        w = psi[[(x - 1) % N, x, (x + 1) % N]]
        tot += np.linalg.norm(sF @ w) ** 2
    return tot


def run(psi0, variant, tmax=6000):
    psi = psi0.astype(complex).copy()
    status = np.zeros(N, int)
    U = change(status)
    t_first, t_mag, ups, mag_site = None, None, [], None
    halo = 0
    quiet = 0
    for t in range(tmax):
        if mag_site is None:
            if total_chance(psi, status, variant) < 1e-7:
                quiet += 1
                if quiet >= 100:   # stationary zero-energy (dark) state reached: no record will form
                    return t_first, None, len(ups), 0, [], True
            else:
                quiet = 0
            psi = U @ psi
            for r in range(3):
                xs = [x for x in range(r, N, 3) if status[x] == UNL]
                if not xs:
                    continue
                a_list, p_list = [], []
                for x in xs:
                    sF, _ = MATS[(variant, status[(x - 1) % N], status[(x + 1) % N])]
                    a = sF @ psi[[(x - 1) % N, x, (x + 1) % N]]
                    a_list.append(a); p_list.append(np.vdot(a, a).real)
                p = np.array(p_list)
                u = rng.uniform()
                cum = np.cumsum(p)
                if u < cum[-1]:  # one window forms (at most one: one magnon)
                    i = int(np.searchsorted(cum, u))
                    x, a = xs[i], a_list[i]
                    t_first = t if t_first is None else t_first
                    if rng.uniform() < abs(a[1]) ** 2 / p[i]:      # locks d: the magnon is recorded
                        status[x] = DN; mag_site = x; t_mag = t; psi[:] = 0
                        break
                    a = a.copy(); a[1] = 0                            # locks u: a vacuum-content record
                    psi[:] = 0; psi[[(x - 1) % N, x, (x + 1) % N]] = a / np.linalg.norm(a)
                    status[x] = UP; ups.append(x)
                    U = change(status)
                else:  # no record in this pass: Lueders no-record update on every window
                    new = psi.copy()
                    for x in xs:
                        _, s1 = MATS[(variant, status[(x - 1) % N], status[(x + 1) % N])]
                        idx = [(x - 1) % N, x, (x + 1) % N]
                        # windows of one pass are disjoint, so apply each to the current vector
                        new[idx] = s1 @ new[idx]
                    psi = new / np.linalg.norm(new)
        else:
            if variant == "B":
                break
            nbrs = [(mag_site - 1) % N, (mag_site + 1) % N]
            open_n = [y for y in nbrs if status[y] == UNL]
            if not open_n:
                break
            for y in open_n:   # vacuum next to a recorded 'd': F = c/2 <u|.|u>, locks u
                if rng.uniform() < C / 2:
                    status[y] = UP; halo += 1
    dist = [min((x - mag_site) % N, (mag_site - x) % N) for x in ups] if mag_site is not None else []
    return t_first, t_mag, len(ups), halo, dist, False


# exact checks
vac = np.zeros(N)
print(f"vacuum: total formation chance per tick = {total_chance(vac, np.zeros(N, int), 'A'):.1e} (exact 0)")
uni = np.ones(N) / np.sqrt(N)
st0 = np.zeros(N, int)
U0 = change(st0)
psi = uni.astype(complex)
mx = 0.0
for _ in range(200):
    psi = U0 @ psi
    mx = max(mx, total_chance(psi, st0, "A"))
print(f"uniform magnon (a globally rotated vacuum), 200 ticks: max total chance = {mx:.1e} (exact 0)")
for n in (1, 3, 7, 15):
    k = 2 * np.pi * n / N
    pw = np.exp(1j * k * np.arange(N)) / np.sqrt(N)
    print(f"plane wave k={k:.3f}: total chance = {total_chance(pw, st0, 'A'):.6f}, 2c(1-cos k) = {2*C*(1-np.cos(k)):.6f}")

# trajectories
import sys
NTR = int(sys.argv[2]) if len(sys.argv) > 2 else 300
VARIANTS = sys.argv[1] if len(sys.argv) > 1 else "AB"
x0 = N // 2
for variant in VARIANTS:
    for label, psi0 in (("magnon on one site", np.eye(N)[x0]),
                        *[(f"packet k={k:.2f}", (lambda k: (lambda v: v / np.linalg.norm(v))(
                            np.exp(1j * k * np.arange(N) - (np.arange(N) - x0) ** 2 / (2 * 3.0 ** 2))))(k))
                          for k in (0.3, 1.2, 2.4)]):
        E0 = total_chance(psi0, st0, variant) / (2 * C)
        dark = abs(np.vdot(uni, psi0)) ** 2
        res = [run(psi0, variant) for _ in range(NTR)]
        tf = np.array([r[0] for r in res if r[0] is not None]); tm = np.array([r[1] for r in res if r[1] is not None])
        ups = np.array([r[2] for r in res]); halo = np.array([r[3] for r in res])
        d = np.concatenate([r[4] for r in res]) if any(len(r[4]) for r in res) else np.array([np.nan])
        stuck = sum(r[5] for r in res)
        frac_up = (ups.sum() + halo.sum()) / (ups.sum() + halo.sum() + len(tm))
        print(f"[{variant}] {label:18s} E0/J={E0:.3f}: first record at tick {tf.mean():6.2f}+-{tf.std()/np.sqrt(len(tf)):.2f}; "
              f"magnon recorded in {len(tm)}/{NTR} (mean tick {tm.mean():6.1f}), never recorded {stuck} "
              f"(variant-A prediction from the uniform-state weight: {dark*NTR:.1f}); "
              f"u-records before {ups.mean():.2f}, halo {halo.mean():.2f}; vacuum-content share {frac_up:.2f}; "
              f"|u-record - magnon record| median {np.nanmedian(d):.1f}, max {np.nanmax(d):.0f}")
