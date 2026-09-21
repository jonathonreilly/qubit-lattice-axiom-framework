"""Block 58 control (supervisor-run; floating point; evidence, not proof): a spread amplitude at rest is replaced by one record.

Block 56's exact static law in a 41^3 box with walls at the ambient rate: ((1 - A) + (gamma/12) M) phi = 0.  Before: M = diag(m |chi_x|^2) for a
two-lump amplitude; after: one record at y whose bare energy keeps the ledger (note T1).
(a) the ledger, the bare energy of the record, the total wall flux and its first moments, before and after, at weak and at strong coupling;
(b) the same event under block 57's wall-referred law at weak field: the change of the field at distance r, by time."""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def solve(side, masses, gamma):
    free = np.ones((side,) * 3, bool)
    free[0] = free[-1] = False; free[:, 0] = free[:, -1] = False; free[:, :, 0] = free[:, :, -1] = False
    idx = -np.ones((side,) * 3, int); idx[free] = np.arange(free.sum())
    sites = np.argwhere(free)
    rows, cols, vals, b = [np.arange(len(sites))], [np.arange(len(sites))], [1 + gamma / 12 * masses[free]], np.zeros(len(sites))
    for d in NEIGH:
        nb = sites + np.array(d)
        j = idx[nb[:, 0], nb[:, 1], nb[:, 2]]
        ins = j >= 0
        rows.append(np.arange(len(sites))[ins]); cols.append(j[ins]); vals.append(-np.ones(ins.sum()) / 6); b[~ins] += 1 / 6
    a = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(sites),) * 2).tocsc()
    phi = np.ones((side,) * 3); phi[free] = spsolve(a, b)
    return phi


def wall_moments(phi, side):
    """total flux sum (1 - phi_inside) over wall bonds, and its first moments with the wall site's coordinates."""
    g = np.indices((side,) * 3).astype(float)
    tot, mom = 0.0, np.zeros(3)
    for ax in range(3):
        for wall, inner in ((0, 1), (side - 1, side - 2)):
            sl_w = [slice(1, -1)] * 3; sl_w[ax] = wall
            sl_i = [slice(1, -1)] * 3; sl_i[ax] = inner
            f = 1 - phi[tuple(sl_i)]
            tot += f.sum()
            for j in range(3):
                mom[j] += (f * g[j][tuple(sl_w)]).sum()
    return tot, mom


if __name__ == "__main__":
    side = 41
    c = side // 2
    g = np.indices((side,) * 3).astype(float)
    dens = np.exp(-((g[0] - c + 3) ** 2 + (g[1] - c) ** 2 + (g[2] - c) ** 2) / (2 * 2.0 ** 2)) + 0.4 * np.exp(-((g[0] - c - 5) ** 2 + (g[1] - c - 2) ** 2 + (g[2] - c) ** 2) / (2 * 1.5 ** 2))
    dens[[0, -1]] = 0; dens[:, [0, -1]] = 0; dens[:, :, [0, -1]] = 0
    dens /= dens.sum()
    for gamma, m in ((0.05, 6.0), (1.0, 6.0)):
        mass = m * dens
        phi = solve(side, mass, gamma)
        ledger = (mass * phi).sum()
        q = gamma / 12 * mass * phi
        xbar = np.array([(q * g[j]).sum() for j in range(3)]) / q.sum()
        pbar = np.array([(dens * g[j]).sum() for j in range(3)])
        ebar = np.array([(mass * phi ** 2 * g[j]).sum() for j in range(3)]) / (mass * phi ** 2).sum()
        tot0, mom0 = wall_moments(phi, side)
        print(f"gamma = {gamma}, bare energy {m}: ledger {ledger:.6f}; (2/gamma) x wall flux {2 / gamma * tot0:.6f}; centres relative to the box centre: charge-weighted {np.round(xbar - c, 4)}, probability {np.round(pbar - c, 4)}, energy-weighted {np.round(ebar - c, 4)}; lowest phi {phi.min():.4f}")
        print(f"    first moments of the wall flux / 6 = {np.round(mom0 / 6, 6)} against the dipole sum q x = {np.round([(q * g[j]).sum() for j in range(3)], 6)}")
        for y in ((c - 3, c, c), (c + 5, c + 2, c), (c, c + 4, c - 3)):
            probe = np.zeros((side,) * 3); probe[y] = 1e-7
            gfun = (1 - solve(side, probe, gamma)) * 12 / (gamma * 1e-7)
            gy = gfun[y]
            if gamma / 12 * gy * ledger >= 1:
                print(f"    record at {np.array(y) - c}: the ledger exceeds what this site can show ({12 / (gamma * gy):.4f}); no single record keeps it")
                continue
            m_rec = ledger / (1 - gamma / 12 * gy * ledger)
            after = np.zeros((side,) * 3); after[y] = m_rec
            phi2 = solve(side, after, gamma)
            tot1, mom1 = wall_moments(phi2, side)
            dp = gamma / 12 * ledger * (np.array(y) - xbar)
            print(f"    record at {np.array(y) - c}: bare energy {m_rec:.5f}; ledger after {m_rec * phi2[y]:.6f}; wall flux changed by {tot1 - tot0:+.1e}; first moments / 6 jumped by {np.round((mom1 - mom0) / 6, 6)} against Q (y - Xbar) = {np.round(dp, 6)}")
    # (b) the event under the wall-referred wave law at weak field: source changes from spread to point at t = 0 with the monopole kept
    print("(b) wall-referred law at weak field (c = 1, ambient rate 1), 61^3 box: the change of u at distance r along an axis after the event, by time")
    side = 61
    c = side // 2
    g = np.indices((side,) * 3).astype(float)
    spread = np.exp(-((g[0] - c + 2) ** 2 + (g[1] - c) ** 2 + (g[2] - c) ** 2) / (2 * 2.0 ** 2)); spread /= spread.sum()
    point = np.zeros((side,) * 3); point[c + 2, c, c] = 1.0
    ds = point - spread                                                        # change of the source: zero monopole, a dipole and more
    wall = np.ones((side,) * 3, bool); wall[1:-1, 1:-1, 1:-1] = False
    h = 0.25
    up = np.zeros((side,) * 3); u = np.zeros((side,) * 3)
    marks = {8: [], 16: [], 24: []}
    times = []
    for n in range(int(34 / h)):
        lap = -6 * u
        for ax in range(3):
            lap += np.roll(u, 1, ax) + np.roll(u, -1, ax)
        new = 2 * u - up + h * h * (lap - ds); new[wall] = 0
        up, u = u, new
        times.append((n + 1) * h)
        for r in marks:
            marks[r].append(u[c + 2 + r, c, c])
    for r, tr in marks.items():
        tr = np.array(tr)
        final = tr[-1]
        first = times[int(np.argmax(np.abs(tr) > 0.02 * np.abs(tr).max()))]
        print(f"    r = {r:2d}: change below 2 per cent of its largest value until t = {first:.2f} (r/(c wbar) = {r}); value at t = 34: {final:+.3e}")
