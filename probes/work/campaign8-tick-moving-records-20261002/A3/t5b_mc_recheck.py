"""Re-check the SEQ-AVG Monte Carlo for the product start with fresh seeds (same rule)."""
import itertools
import numpy as np
import t5_two_records as m
from common import mh_split, mc_trajectories, chi2_check, tv

for seed in (1, 2, 3):
    m.rng = np.random.default_rng(99)          # same gates as the main run
    e = np.zeros(m.nc, complex); e[m.confs.index((0, 4))] = 1.0
    Psi = e.copy(); P = np.abs(Psi) ** 2
    T_list, P_list = [], [P.copy()]
    for t in range(m.TICKS):
        bonds = m.bondsA if t % 2 == 0 else m.bondsB
        gates = m.layer_gates(bonds)
        U = np.eye(m.nc, dtype=complex)
        for G in gates:
            U = G @ U
        Ts = [m.seq_rule(Psi, gates, list(o))[0] for o in itertools.permutations(range(4))]
        T_list.append(sum(Ts) / len(Ts))
        Psi = U @ Psi; P = np.abs(Psi) ** 2; P_list.append(P.copy())
    r = np.random.default_rng(1000 + seed)
    Mm = 300_000
    X0 = r.choice(m.nc, size=Mm, p=P_list[0])
    hists = mc_trajectories(T_list, X0, r)
    ps = [chi2_check(h, Pt, Mm)[2] for h, Pt in zip(hists, P_list)]
    tvs = [tv(h / Mm, Pt) for h, Pt in zip(hists, P_list)]
    print(f"seed {seed}: M={Mm}, min p = {min(ps):.3g} at tick {int(np.argmin(ps))}, max TV = {max(tvs):.4f}")
