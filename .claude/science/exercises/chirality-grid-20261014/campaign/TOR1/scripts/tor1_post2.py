"""TOR-1 kernel post-processing for F3 (pool P2): kernel = level B (2,12); E = k max(q_poly, q_plane, h) + 1e-13."""
import numpy as np
P = 'pool_TOR1_srch_Lt4_k6_s3201'; cheap = ['mod', 'O', 'vec0', 'W', 'PG']
def load(n, nw, ops, mode):
    try: z = np.load(f"{P}_L{n}_{nw}_{'-'.join(ops)}_{mode}.npz")
    except FileNotFoundError: return None
    return {op: z[op] for op in ops}
def full(L):
    F = L.copy(); k = len(F)
    for a in range(k):
        for b in range(a):
            if np.isnan(F[a, b].real) and not np.isnan(F[b, a].real): F[a, b] = np.conj(F[b, a])
    return F
def norm(L):
    d = L.diagonal().real; return np.exp(L - 0.5 * (d[:, None] + d[None, :]))
lev = {}
for key, n, nw, mode in (('A', 2, 8, 'upper'), ('B', 2, 12, 'upper'), ('C', 3, 8, 'sub122')):
    lev[key] = {**(load(n, nw, cheap, mode) or {}), **(load(n, nw, ['chi'], mode) or {})}
herm = load(2, 8, ['chi'], 'rev112'); res = {}
for op in ['chi'] + cheap:
    if op not in lev['A']: continue
    LA = full(lev['A'][op]); ZA = norm(LA); k = len(ZA)
    dimA = np.abs(np.angle(np.exp(1j * LA.diagonal().imag))).max()
    ZB = norm(full(lev['B'][op])) if op in lev['B'] else None
    q_poly = np.abs(ZB - ZA).max() if ZB is not None else np.nan
    q_plane = np.nan
    if op in lev['C']:
        LC = lev['C'][op]; ZC = norm(np.where(np.isnan(LC.real), 0, LC)); m = ~np.isnan(LC.real)
        q_plane = np.abs(ZC - ZA)[m].max()
    h = 0.0
    if op == 'chi' and herm is not None:
        Lr = herm['chi']; d = LA.diagonal().real
        for a in range(k):
            for b in range(k):
                if not np.isnan(Lr[a, b].real):
                    h = max(h, abs(np.exp(Lr[a, b] - 0.5 * (d[a] + d[b])) - np.conj(np.exp(LA[b, a] - 0.5 * (d[a] + d[b])))))
    E = k * np.nanmax([q_poly, q_plane, h, 0.0]) + 1e-13
    Zr = ZB if ZB is not None else ZA
    evA = np.linalg.eigvalsh(0.5 * (ZA + ZA.conj().T)); ev = np.linalg.eigvalsh(0.5 * (Zr + Zr.conj().T))
    complete = not (np.isnan(q_poly) or np.isnan(q_plane))
    res[op] = (ev[0], E, Zr)
    print(f"{op:4s}: A lam_min {evA[0]:+.5e} | B lam_min {ev[0]:+.5e} lam_2 {ev[1]:+.3e} max {ev[-1]:.4f} min/max {ev[0]/ev[-1]:+.3e} | q_poly {q_poly:.2e} q_plane {q_plane:.2e} h {h:.1e} "
          f"| E {E:.2e} | estimator complete {complete} | conv-negative {complete and ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E} | max|Im ln diag A| {dimA:.1e}", flush=True)
if 'chi' in res and 'mod' in res:
    Zc, Zm = res['chi'][2], res['mod'][2]
    w, V = np.linalg.eigh(0.5 * (Zm + Zm.T)); v = V[:, 0]; Hc = 0.5 * (Zc + Zc.conj().T)
    wc, Vc = np.linalg.eigh(Hc)
    print(f"PHASE: max|Zn_chi - Zn_mod| {np.abs(Zc - Zm).max():.3e}; max|Im Zn_chi| {np.abs(Zc.imag).max():.3e}; lam_min chi - mod {res['chi'][0]-res['mod'][0]:+.3e}; "
          f"first-order v_mod^T(H_chi - Z_mod)v_mod {np.real(v @ (Hc - Zm) @ v):+.3e}; |<v_mod|v_chi>| {abs(np.vdot(v, Vc[:, 0])):.5f}")
    np.save(P + '_TOR1_Zchi_B.npy', Zc); np.save(P + '_TOR1_Zmod_B.npy', Zm)
