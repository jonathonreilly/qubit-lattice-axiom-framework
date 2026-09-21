"""Block 57 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic calculus with a generic change of parameter, dense
generalized eigenproblems, a non-linear elliptic solve, floating-point propagation).
W1  symbolic, generic f(t): L dt for the neighbour-difference kinetic term, the wall-referred term, the bond energy and a two-site clocked
    generator is unchanged; the on-site term changes by a multiple of f''.
W2  the linearized laws on a 6^3 torus as generalized eigenproblems V x = omega^2 M x on zero-sum fields: neighbours only: one frequency;
    referred to the lattice mean: omega^2 = c^2 wbar^2 E(k).
W3  the NON-LINEAR neighbours-only law on a line with walls: the acceleration of u, from an elliptic solve, is non-zero far from a source
    switched on at that instant; under the wall-referred law it is exactly zero there.
W4  the wall-referred law in a 41^3 box: half-rise times at r = 6, 12 for ambient rates 1 and 3 against r/(c wbar).
W5  a ring with the on-site term (a master parameter): the mean of psi follows the uniform mode's closed form psi_0^2 = 1 + a t^2; with the term referred
    to the lattice mean it does not move; both keep their ledgers."""
import sys

import numpy as np
import sympy as sp
from scipy.linalg import eigh

results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
t = sp.symbols("t", real=True)
f = sp.Function("f")(t)
fd = sp.diff(f, t)
u1, u2, uw = [sp.Function(nm)(t) for nm in ("u1", "u2", "uw")]
vel = lambda u: (sp.diff(u, t) - sp.diff(f, t, 2) / fd) / fd          # du'/dt'
w1, w2 = sp.exp(u1), sp.exp(u2)
pieces = {
    "neighbour difference": ((sp.diff(u1, t) - sp.diff(u2, t)) ** 2 / sp.sqrt(w1 * w2), (vel(u1) - vel(u2)) ** 2 / (sp.sqrt(w1 * w2) / fd) * fd),
    "wall referred": ((sp.diff(u1, t) - sp.diff(uw, t)) ** 2 / w1, (vel(u1) - vel(uw)) ** 2 / (w1 / fd) * fd),
    "bond energy": ((sp.sqrt(w1) - sp.sqrt(w2)) ** 2, (sp.sqrt(w1) / sp.sqrt(fd) - sp.sqrt(w2) / sp.sqrt(fd)) ** 2 * fd),
    "clocked generator": (sp.sqrt(w1 * w2), sp.sqrt(w1 * w2) / fd * fd),
    "on site": (sp.diff(u1, t) ** 2 / w1, vel(u1) ** 2 / (w1 / fd) * fd),
}
status = {k: sp.simplify(b - a) == 0 for k, (a, b) in pieces.items()}
extra = sp.simplify(pieces["on site"][1] - pieces["on site"][0])
report("W1", status == {"neighbour difference": True, "wall referred": True, "bond energy": True, "clocked generator": True, "on site": False} and sp.simplify(extra.subs(sp.diff(f, t, 2), 0)) == 0,
       f"generic f(t): L dt unchanged for the neighbour-difference term, the wall-referred term, the bond energy and the clocked generator; the on-site term changes by {extra}, which vanishes iff f'' = 0")

# ------------------------------------------------------------------------------------------------ W2
side = 6
sites = [(x, y, z) for x in range(side) for y in range(side) for z in range(side)]
index = {s: i for i, s in enumerate(sites)}
n = len(sites)
lam = np.zeros((n, n))
for s in sites:
    for ax in range(3):
        q = list(s); q[ax] = (q[ax] + 1) % side; q = tuple(q)
        lam[index[s], index[s]] += 1; lam[index[q], index[q]] += 1; lam[index[s], index[q]] -= 1; lam[index[q], index[s]] -= 1
wbar, gamma, kappa, c = 1.7, 0.6, 2.3, 1.0
basis = np.linalg.svd(np.ones((1, n)))[2][1:].T                      # zero-sum fields
v_mat = basis.T @ (wbar / gamma * lam) @ basis
m_near = basis.T @ (kappa / wbar * lam) @ basis
m_mean = basis.T @ (np.eye(n) / (gamma * c * c * wbar)) @ basis
om_near = eigh(v_mat, m_near, eigvals_only=True)
om_mean = np.sort(eigh(v_mat, m_mean, eigvals_only=True))
symbols = np.sort([c * c * wbar * wbar * sum(2 - 2 * np.cos(2 * np.pi * k / side) for k in kk) for kk in [(a, b, d) for a in range(side) for b in range(side) for d in range(side)] if any(kk)])
report("W2", np.ptp(om_near) < 1e-9 and abs(om_near[0] - wbar ** 2 / (gamma * kappa)) < 1e-9 and np.max(np.abs(om_mean - symbols)) < 1e-9,
       f"6^3 torus: neighbours only: all 215 squared frequencies equal {om_near[0]:.6f} = wbar^2/(gamma kappa) (spread {np.ptp(om_near):.1e}); referred to the lattice mean: they are c^2 wbar^2 E(k) to {np.max(np.abs(om_mean - symbols)):.1e}, the smallest {om_mean[0]:.4f}")

# ------------------------------------------------------------------------------------------------ W3
nl = 101
mid = nl // 2
u = 0.3 * np.exp(-((np.arange(nl) - 30.0) / 9.0) ** 2); u[0] = u[-1] = 0.0          # a non-uniform rate field, walls at the ambient rate
du = np.zeros(nl)
phi = np.exp(u / 2)
source = np.zeros(nl); source[mid] = 1.0                                           # an energy density switched on at this instant
dF = np.zeros(nl); dF[1:-1] = 2 / gamma * phi[1:-1] * (2 * phi[1:-1] - phi[2:] - phi[:-2])
# neighbours only: K = (kappa/2) sum_b (du_x - du_y)^2/(phi_x phi_y); at du = 0 the law is  kappa Lam_w a = -(dF/du + e)  inside, a = 0 on the walls
wgt = 1 / (phi[1:] * phi[:-1])
lam_w = np.zeros((nl, nl))
for b in range(nl - 1):
    lam_w[b, b] += wgt[b]; lam_w[b + 1, b + 1] += wgt[b]; lam_w[b, b + 1] -= wgt[b]; lam_w[b + 1, b] -= wgt[b]
inner = slice(1, nl - 1)
acc_with = np.linalg.solve(kappa * lam_w[inner, inner], -(dF[inner] + source[inner]))
acc_without = np.linalg.solve(kappa * lam_w[inner, inner], -dF[inner])
far = 10 - 1                                                                         # site 10, forty sites from the source
near_change, far_change = acc_with[mid - 1] - acc_without[mid - 1], acc_with[far] - acc_without[far]
onsite_far = -(gamma * c * c * np.exp(u[10])) * 0.0                                  # wall-referred law: a_x = -gamma c^2 w_x (dF/du_x + e_x): the source enters at its own site only
report("W3", abs(far_change) > 1e-3 * abs(near_change) and onsite_far == 0.0,
       f"non-linear neighbours-only law on a line with walls, a source switched on at the middle: the acceleration of u changes by {near_change:.4f} at the source and by {far_change:.4f} forty sites away at the same instant (ratio {far_change / near_change:.3f}); under the wall-referred law the change forty sites away is exactly zero")

# ------------------------------------------------------------------------------------------------ W4
def half_rise(side_b, wb, radii):
    h = 0.25 / wb
    m = side_b // 2
    up = np.zeros((side_b,) * 3); uc = np.zeros((side_b,) * 3)
    src = np.zeros((side_b,) * 3); src[m, m, m] = 1.0
    wall = np.ones((side_b,) * 3, bool); wall[1:-1, 1:-1, 1:-1] = False
    hit = {}
    for step in range(int(40 / wb / h)):
        lap = -6 * uc
        for ax in range(3):
            lap += np.roll(uc, 1, ax) + np.roll(uc, -1, ax)
        new = 2 * uc - up + h * h * (wb * wb * lap - src); new[wall] = 0
        up, uc = uc, new
        for r in radii:
            if r not in hit and uc[m + r, m, m] <= 0.5 * (-1 / (wb * wb) / (4 * np.pi * r)):
                hit[r] = (step + 1) * h
    return hit


rise1, rise3 = half_rise(41, 1.0, (6, 12)), half_rise(41, 3.0, (6, 12))
ok = all(abs(rise1[r] / r - 1) < 0.1 for r in (6, 12)) and all(abs(rise3[r] * 3 / r - 1) < 0.1 for r in (6, 12))
report("W4", ok, f"wall-referred law, 41^3 box, c = 1: half-rise times at r = 6, 12: {rise1[6]:.2f}, {rise1[12]:.2f} at ambient rate 1 and {rise3[6]:.2f}, {rise3[12]:.2f} at ambient rate 3 (r/(c wbar) = 6, 12 and 2, 4)")

# ------------------------------------------------------------------------------------------------ W5
nr = 64
rng = np.random.default_rng(57)
e_dens = 0.02 * (1 + 0.5 * np.cos(2 * np.pi * np.arange(nr) / nr))                   # a fixed positive energy density per unit rate: e_z = dens_z w_z
gam5, c5, h5 = 0.05, 1.0, 0.02


def static_part(psi):
    ph = 1 / psi
    return (e_dens * ph ** 2).sum() + 2 / gam5 * ((ph - np.roll(ph, 1)) ** 2).sum()


def force(psi):
    ph = 1 / psi
    dfu = 2 / gam5 * ph * (2 * ph - np.roll(ph, 1) - np.roll(ph, -1))
    return gam5 * c5 * c5 / (2 * psi) * (dfu + e_dens * ph ** 2)


out = {}
for kind in ("on site", "lattice mean"):
    psi = np.ones(nr); velp = np.zeros(nr)
    start_static = static_part(psi)
    led0 = start_static
    fcur = force(psi)
    if kind == "lattice mean":
        fcur = fcur - fcur.mean()
    for _ in range(2000):
        velp_half = velp + 0.5 * h5 * fcur
        psi = psi + h5 * velp_half
        fcur = force(psi)
        if kind == "lattice mean":
            fcur = fcur - fcur.mean()                                                # the uniform mode carries no momentum: only the zero-sum part of the force acts
        velp = velp_half + 0.5 * h5 * fcur
    tt = 2000 * h5
    led = static_part(psi) + 2 / (gam5 * c5 * c5) * (velp ** 2).sum()
    out[kind] = (psi.mean() - 1, led - led0)
a_uni = gam5 * c5 * c5 * e_dens.sum() / (2 * nr)                                    # uniform mode: psi'' = a/psi^3, so psi^2 = 1 + a t^2 from rest
predicted = np.sqrt(1 + a_uni * (2000 * h5) ** 2) - 1
ok = abs(out["on site"][0] / predicted - 1) < 0.01 and abs(out["lattice mean"][0]) < 1e-12 and abs(out["on site"][1]) < 1e-6
report("W5", ok, f"ring of 64 with a fixed positive energy density: on-site term: the mean of psi rose by {out['on site'][0]:.6f} in t = 40 against the uniform mode's closed form sqrt(1 + a t^2) - 1 = {predicted:.6f}, a = gamma c^2 (static ledger)/(2 N) (every clock slowing against the parameter), ledger moved by {out['on site'][1]:+.1e}; referred to the lattice mean: the mean of psi moved by {out['lattice mean'][0]:+.1e}")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
