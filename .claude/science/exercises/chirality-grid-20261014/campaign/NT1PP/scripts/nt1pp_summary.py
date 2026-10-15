"""NT-1'' consolidated tables (W0 = 0.3, Lt 8, Lx 4..24) from saved npz/npy; writes nt1pp_summary.npz. usage: python3 nt1pp_summary.py"""
import numpy as np
Ls = np.arange(4, 26, 2); rows = {}
for L in Ls:
    z = np.load(f'e2_Lx{L}_Lt8_W0.3.npz'); e = np.load(f'e2edge_Lx{L}_Lt8_W0.3.npy')
    for k, v in (('tau_central_11112', float(z['11112_tq_m'])), ('JQ_central_11112', abs(z['11112_rowsK'][3])),
                 ('tau_edge_11112', e[0, 0]), ('hbar_edge_11112', np.abs(z['11112_hb'][[0, -1]]).max()),
                 ('Abar_edgerow_11112', abs(z['11112_Arow'][0])), ('mbar_central_11112', np.abs(z['11112_mb'][3]).max()),
                 ('LxP_L1', L * float(z['L1_tq_m'])), ('Lx_hbar_edge_L1', L * np.abs(z['L1_hb'][[0, -1]]).max())):
        rows.setdefault(k, []).append(v)
print("Lx: " + " ".join(f"{L:9d}" for L in Ls))
for k, v in rows.items():
    v = np.array(v); print(f"{k:20s}: " + " ".join(f"{x:9.3e}" for x in v))
    if 'L1' not in k:
        r = 0.5 * np.log(v[:-1] / v[1:]); print(f"{'  local rate':20s}: " + " ".join(f"{x:9.3f}" for x in r))
        print(f"{'  rate*Lx_mid':20s}: " + " ".join(f"{x*(L+1):9.2f}" for x, L in zip(r, Ls[:-1])))
np.savez('nt1pp_summary.npz', Lx=Ls, **{k: np.array(v) for k, v in rows.items()})
