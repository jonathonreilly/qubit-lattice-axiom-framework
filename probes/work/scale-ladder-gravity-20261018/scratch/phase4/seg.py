# segment-midpoint coupling: S_int = sum_seg eps_seg * [ (c L~)_seg evaluated at the segment midpoint ]
import contextlib, io, itertools
with contextlib.redirect_stdout(io.StringIO()):
    from common import *
    from ward import grad_fwd, grad_cell, shell_kt, stress_c, n1, n2
R0, D, ls = segment_readings(Dc, np.zeros(4)); Wt = np.diag(1 / ls ** 2); Lt = np.linalg.pinv(Wt @ D) @ Wt   # 10 x 24
assert np.allclose(Lt @ R0, strain_metric(Dc, np.zeros(4)))
E = np.eye(4); pairs = list(itertools.combinations(range(4), 2))
MID = [0.5 * E[m] for m in range(4)] + [0.5 * (E[m] + E[n]) for (m, n) in pairs for _ in (0, 1)] + [0.5 * np.ones(4)] * 8
def place(q, mid, mode):
    """symbol moving a cell-centred (u/2) density to the segment midpoint"""
    if mode == 'phase': return np.exp(1j * q @ (mid - 0.5))
    # local: average of the cell-centred density over the cells whose centres surround the midpoint
    fr = [nu for nu in range(4) if abs(mid[nu] - round(mid[nu])) < 1e-9]          # integer coordinates of the midpoint
    tot = 0
    for sg in itertools.product([-0.5, 0.5], repeat=len(fr)):
        c = mid.copy()
        for nu, s in zip(fr, sg): c[nu] += s
        tot += np.exp(1j * q @ (c - 0.5))
    return tot / 2 ** len(fr)
for mode in ('cell (old)', 'phase', 'local'):
    for sgn in ((+1, -1) if mode != 'cell (old)' else (+1,)):
        prev = None; line = []
        for s in (0.2, 0.1, 0.05, 0.025):
            k1 = shell_kt(s * n1, grad_cell); k2 = shell_kt(0.7 * s * n2, grad_cell); q = k2 - k1
            c = stress_c(grad_cell(-k1), grad_cell(k2)); beta = c @ Lt                    # per-segment coupling
            if mode != 'cell (old)': beta = beta * np.array([place(sgn * q, m, mode) for m in MID])
            Rq = segment_readings(Dc, -q)[0]; WG = Rq @ Dc.gauge(-q)[:, :4]              # 24 x 4 segment strains of site displacements
            r = np.linalg.norm(beta @ WG) / (np.linalg.norm(beta) * np.linalg.norm(WG)); line.append(r)
        print(f"{mode:10s} sign {sgn:+d}: Ward ratio " + ", ".join(f"{x:.2e}" for x in line) + "  halving factors " + ", ".join(f"{line[i]/line[i+1]:.2f}" for i in range(3)))
