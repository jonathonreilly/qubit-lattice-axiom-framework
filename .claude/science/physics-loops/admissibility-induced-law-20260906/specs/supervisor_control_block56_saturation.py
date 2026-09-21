"""Block 56 control (supervisor-run; floating point; evidence, not proof): the exact static law of the simplest clock law in large boxes.

Inside a box with walls at the ambient rate (phi = 1):  ((1 - A) + (gamma/12) M) phi = 0,  A the average over the six neighbours, M the bare
rest energies of bodies at rest.  Reported: (a) one body: phi_0, its ledger m phi_0 and its energy in the field m phi_0^2 against 1/(1 + x);
(b) balls of radius R whose clocks are stopped (phi = 0 on the ball, the limit of large bare energies): the ledger against 8 pi R/gamma, in boxes of
growing side; (c) the rate outside a stopped ball against 1 - R_eff/r; (d) a pair of heavy bodies: the defect of the ledger by separation against
its weak-field value (gamma/6) m_1 m_2 g(r)."""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import cg, spsolve

NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def solve_box(side, masses, gamma, stopped=None, exact=True):
    """phi on the box; `masses` site -> bare energy; `stopped` a set of sites held at phi = 0."""
    stopped = stopped or set()
    free = np.ones((side,) * 3, bool)
    free[0, :, :] = free[-1, :, :] = free[:, 0, :] = free[:, -1, :] = free[:, :, 0] = free[:, :, -1] = False
    for s in stopped:
        free[s] = False
    idx = -np.ones((side,) * 3, int)
    idx[free] = np.arange(free.sum())
    sites = np.argwhere(free)
    rows, cols, vals = [np.arange(len(sites))], [np.arange(len(sites))], [np.ones(len(sites))]
    b = np.zeros(len(sites))
    for d in NEIGH:
        nb = sites + np.array(d)
        j = idx[nb[:, 0], nb[:, 1], nb[:, 2]]
        inside = j >= 0
        rows.append(np.arange(len(sites))[inside]); cols.append(j[inside]); vals.append(-np.ones(inside.sum()) / 6)
        wall = ~inside & ~np.array([tuple(q) in stopped for q in nb]) if stopped else ~inside
        b[wall] += 1.0 / 6
    diag_extra = np.zeros(len(sites))
    for s, m in masses.items():
        diag_extra[idx[s]] = gamma / 12 * m
    a = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(sites),) * 2).tocsr()
    a = a + coo_matrix((diag_extra, (np.arange(len(sites)), np.arange(len(sites)))), shape=a.shape).tocsr()
    sol = spsolve(a.tocsc(), b) if exact else cg(a, b, rtol=1e-11, maxiter=20000)[0]
    phi = np.ones((side,) * 3)
    phi[free] = sol
    for s in stopped:
        phi[s] = 0.0
    return phi


def wall_flux(phi):
    """sum over bonds from the walls into the interior of (1 - phi): six times the total charge of (1 - A) phi."""
    return sum((1 - phi[1, :, :]).sum() + (1 - phi[-2, :, :]).sum() for phi in (phi, phi.transpose(1, 0, 2), phi.transpose(2, 1, 0)))


if __name__ == "__main__":
    gamma, side = 1.0, 41
    c = side // 2
    print(f"(a) one body at the centre of a {side}^3 box, gamma = {gamma}")
    g0 = None
    for m in (0.1, 1.0, 8.0, 30.0, 1e3, 1e6):
        phi = solve_box(side, {(c, c, c): m}, gamma)
        p0 = phi[c, c, c]
        g0 = g0 or (1 / p0 - 1) * 12 / (gamma * m)
        x = gamma / 12 * g0 * m
        print(f"    m = {m:>9g}: x = {x:10.4f}; phi_0 = {p0:.6f} against 1/(1 + x) = {1 / (1 + x):.6f}; ledger m phi_0 = {m * p0:.5f} (bound {12 / (gamma * g0):.5f}); energy in the field m phi_0^2 = {m * p0 * p0:.5f} (peak 3/(gamma g_0) = {3 / (gamma * g0):.5f} at x = 1); ledger from the wall flux {2 / gamma * wall_flux(phi) / 1:.5f}")
    print(f"    the box's g_0 = {g0:.5f}; on the infinite lattice 1.51639")
    print("(b) stopped balls (phi = 0 on every site within R of the centre): ledger = (2/gamma) x wall flux, by box side, with a linear extrapolation in 1/side, against 8 pi R/gamma")
    table = {}
    for side_b in (41, 61, 81):
        cb = side_b // 2
        for radius in (2, 4, 6):
            ball = {(cb + x, cb + y, cb + z) for x in range(-radius, radius + 1) for y in range(-radius, radius + 1) for z in range(-radius, radius + 1) if x * x + y * y + z * z <= radius * radius}
            phi = solve_box(side_b, {}, gamma, stopped=ball, exact=False)
            table[(radius, side_b)] = 2 / gamma * wall_flux(phi)
            if side_b == 81 and radius == 6:
                prof = [(r, 1 - phi[cb + r, cb, cb]) for r in (8, 12, 18, 24)]
    for radius in (2, 4, 6):
        l61, l81 = table[(radius, 61)], table[(radius, 81)]
        free = l81 - (l61 - l81) / (1 / 61 - 1 / 81) * (1 / 81)
        print(f"    R = {radius}: {table[(radius, 41)]:8.3f}, {l61:8.3f}, {l81:8.3f} in boxes of side 41, 61, 81; extrapolated {free:8.3f} = {free / (8 * np.pi * radius / gamma):.3f} of 8 pi R/gamma; per site of the ball the extrapolated ledger is {free / sum(1 for x in range(-radius, radius + 1) for y in range(-radius, radius + 1) for z in range(-radius, radius + 1) if x * x + y * y + z * z <= radius * radius):.3f} (one site alone: {12 / (gamma * 1.51639):.3f})")
    (r1, v1), (r4, v4) = prof[0], prof[3]
    a_fit = (v1 - v4) / (1 / r1 - 1 / r4)
    b_fit = a_fit / r1 - v1
    print("(c) outside the stopped ball of radius 6 in the 81^3 box, along an axis: 1 - phi = a/r - b fitted at r = 8 and 24, read at 12 and 18")
    print(f"    a = {a_fit:.3f}, b = {b_fit:.4f}; " + "; ".join(f"r = {r}: 1 - phi = {v:.4f}, fit {a_fit / r - b_fit:.4f}" for r, v in prof[1:3]) + f"; gamma x ledger/(8 pi) = {gamma * table[(6, 81)] / (8 * np.pi):.3f}")
    print("(d) a pair of bodies with bare energy 20 each (x = 2.5 alone) on the axis of the 41^3 box: the defect of the ledger against its weak-field value (gamma/6) m^2 g and against (gamma/6) (m phi)^2 g with phi of one body alone")
    m = 20.0
    for sep in (2, 4, 8, 12):
        s1, s2 = (c - sep // 2, c, c), (c + sep - sep // 2, c, c)
        phi = solve_box(side, {s1: m, s2: m}, gamma)
        pair = m * (phi[s1] + phi[s2])
        p1 = solve_box(side, {s1: m}, gamma)[s1]; p2 = solve_box(side, {s2: m}, gamma)[s2]
        probe = solve_box(side, {s1: 1e-6}, gamma)
        g12 = (1 - probe[s2]) * 12 / (gamma * 1e-6)
        print(f"    separation {sep:2d}: ledger of the pair {pair:.5f}; members alone {m * (p1 + p2):.5f}; defect {m * (p1 + p2) - pair:.5f}; (gamma/6) m^2 g = {gamma / 6 * m * m * g12:.5f}; (gamma/6) (m phi_1)(m phi_2) g = {gamma / 6 * m * p1 * m * p2 * g12:.5f}")
