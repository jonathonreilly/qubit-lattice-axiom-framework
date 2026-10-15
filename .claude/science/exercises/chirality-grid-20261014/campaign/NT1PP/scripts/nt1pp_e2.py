"""NT-1'' E2 (PREREG section 5): deterministic F = 0, uniform Wilson line W0 background; Lx-scaling of the finite-volume (Q) part.
usage: python3 nt1pp_e2.py Lx T W0      (runs 11112 and L1; one process per Lx)"""
import sys, time
import numpy as np
from nt1pp_common import *

Lx, T, W0 = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); t00 = time.time()
S = Strip(Lx, T); A = uniformW(S, W0); Lt = S.Lt
ys = [S.key[('x', 0, 0)], S.key[('t', 0, 0)]]
chunk = 1 if S.N >= 192 else 2
save = {}
for model in ('11112', 'L1'):
    MS = Measure(S, model, Ns=8)
    b = MS.ray(A, 8)
    kQ = b['kQ'][0]; kQt = kQ[S.tl]                        # (Lt-1, Lx) t-link Q-current, x-flat by construction
    Ab = b['Abar'][0].reshape(Lt, Lx); Arow = Ab.mean(1); Axdev = np.abs(Ab - Arow[:, None]).max()
    mb = b['mbar'][0].reshape(Lt - 1, Lx); hb = b['hbar'][0].reshape(Lt, Lx)
    rowsK = kQt.mean(1)                                    # transported charge per unit x at each row (= K_i / Lx)
    cen = T - 1                                            # row index of the crossing t-links (t = 0)
    edge_rows = [0, Lt - 1]; cen_rows = [T - 1, T]
    resp, g2, ok2 = fd_response(MS, A, ys, chunk=chunk)
    tq_m, tq_s = tail_stat(S, resp['kQ'], ys); tk_m, tk_s = tail_stat(S, resp['kbb'], ys)
    print(f"Lx={Lx:2d} Lt={Lt} W0={W0} {model:5s} gmin {min(b['gmin'], g2):.3f} idx {b['idx_ok'] and ok2} | "
          f"J_Q(central row) {abs(rowsK[cen]):.3e} max|kQ| {np.abs(kQ).max():.3e} | tau_kQ(s*) {tq_m:.3e} tau_kQ(Lx/2) {tq_s:.3e} "
          f"tau_kbb(s*) {tk_m:.3e} | Abar rows: edge {np.abs(Arow[edge_rows]).max():.3e} central {np.abs(Arow[cen_rows]).max():.3e} "
          f"(x-dev {Axdev:.1e}) | |mbar| edge {np.abs(mb[[0, -1]]).max():.3e} central {np.abs(mb[T - 1]).max():.3e} | "
          f"|hbar| edge {np.abs(hb[edge_rows]).max():.3e} central {np.abs(hb[cen_rows]).max():.3e} [{time.time()-t00:.0f}s]", flush=True)
    print(f"   Abar row profile (t=-{T-1}..{T}): " + " ".join(f"{v:+.2e}" for v in Arow))
    print(f"   Q t-link current per row        : " + " ".join(f"{v:+.2e}" for v in rowsK))
    save[model] = dict(Arow=Arow, rowsK=rowsK, mb=mb, hb=hb, tq_m=tq_m, tq_s=tq_s, tk_m=tk_m,
                       respQ=np.array([resp['kQ'][y] for y in ys]), respK=np.array([resp['kbb'][y] for y in ys]))
np.savez(f"e2_Lx{Lx}_Lt{Lt}_W{W0}.npz", **{f"{m}_{k}": v for m, d in save.items() for k, v in d.items()})
