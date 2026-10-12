"""R4-1 (E): prefactor P = rms relative deviation / l^3 (geometric mean over l >= 6, l >= 2L) per kernel family, vs kernel scale L."""
import numpy as np
for fn in ('r41_C_results.npy', 'r41_D_results.npy'):
    res = np.load(fn, allow_pickle=True).item()
    print(f"--- {fn}")
    rows = []
    for k, o in res.items():
        L = float(k.split('L=')[1]) if 'L=' in k else 1.0
        sel = (o[:, 0] >= 6) & (o[:, 0] >= 2*L)
        if sel.sum() < 2: continue
        P = np.exp(np.mean(np.log(o[sel, 2]/o[sel, 0]**3)))
        sl = np.polyfit(np.log(o[sel, 0]), np.log(o[sel, 2]), 1)[0] if sel.sum() >= 3 else np.nan
        rows.append((k, L, P, sl, int(sel.sum())))
        print(f"{k:28s} L={L:4.1f}  P = rmsdev/l^3 = {P:.3e}   slope = {sl:+.2f}  (n_l = {int(sel.sum())})")
    for fam in ('smooth-f', 'smooth-g', 'flat', 'exp-cubic'):
        r = [(L, P) for k, L, P, s, n in rows if k.startswith(fam)]
        if len(r) >= 3:
            Ls, Ps = np.array(r).T
            print(f"   family {fam}: d ln P / d ln L = {np.polyfit(np.log(Ls), np.log(Ps), 1)[0]:+.2f}  over L = {Ls.min()}..{Ls.max()}")
