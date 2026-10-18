"""TOR-1 kernel post-processing (PREREG F2): normalised Hermitian kernels, lambda_min, E = k max(q_plane, q_poly, h) + 1e-13."""
import sys, glob
import numpy as np
P = 'pool_TOR1_Lt4_k6_s3101'
def load(n, nw, ops, mode='upper'):
    fn = f"{P}_L{n}_{nw}_{'-'.join(ops)}_{mode}.npz"
    try: z = np.load(fn)
    except FileNotFoundError: return None
    return {op: z[op] for op in ops}
def full(L):
    k = L.shape[0]; F = L.copy()
    for a in range(k):
        for b in range(a):
            if np.isnan(F[a, b].real): F[a, b] = np.conj(F[b, a])
    return F
def norm(L):
    d = L.diagonal().real
    return np.exp(L - 0.5 * (d[:, None] + d[None, :])), np.abs(np.angle(np.exp(1j * L.diagonal().imag))).max()
cheap = ['mod', 'O', 'vec0', 'W', 'PG']
lv = {}
for (n, nw) in ((2, 4), (2, 6), (3, 4)):
    c = load(n, nw, cheap); x = load(n, nw, ['chi'])
    lv[(n, nw)] = {**(c or {}), **(x or {})}
herm = load(2, 4, ['chi'], 'rev112')
res = {}
for op in ['chi'] + cheap:
    Z = {}; dimx = {}
    for key, d in lv.items():
        if op in d: Z[key], dimx[key] = norm(full(d[op]))
    if (2, 4) not in Z: continue
    k = Z[(2, 4)].shape[0]
    hi = (3, 4) if (3, 4) in Z else (2, 4)
    q_plane = np.abs(Z[(3, 4)] - Z[(2, 4)]).max() if (3, 4) in Z else np.nan
    q_poly = np.abs(Z[(2, 6)] - Z[(2, 4)]).max() if (2, 6) in Z else np.nan
    h = 0.0
    if op == 'chi' and herm is not None:
        Lr = herm['chi']; L4 = lv[(2, 4)]['chi']; d = L4.diagonal().real
        for a in range(k):
            for b in range(k):
                if not np.isnan(Lr[a, b].real):
                    zr = np.exp(Lr[a, b] - 0.5 * (d[a] + d[b])); zf = np.conj(np.exp(L4[b, a] - 0.5 * (d[a] + d[b])))
                    h = max(h, abs(zr - zf))
    E = k * np.nanmax([q_plane, q_poly, h, 0.0]) + 1e-13
    for key in sorted(Z):
        ev = np.linalg.eigvalsh(0.5 * (Z[key] + Z[key].conj().T))
        tag = ' <- HIGH' if key == hi else ''
        print(f"{op:4s} level {key}: lam_min {ev[0]:+.5e} lam_2 {ev[1]:+.4e} max {ev[-1]:.4f} min/max {ev[0]/ev[-1]:+.3e}  max|Im ln diag| {dimx[key]:.1e}{tag}")
    ev = np.linalg.eigvalsh(0.5 * (Z[hi] + Z[hi].conj().T)); res[op] = (ev[0], E, Z[hi])
    print(f"{op:4s} SUMMARY: HIGH {hi} lam_min {ev[0]:+.5e} | q_plane {q_plane:.2e} q_poly {q_poly:.2e} h {h:.1e} | E {E:.2e} | conv-negative {ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E}", flush=True)
if 'chi' in res and 'mod' in res:
    Zc, Zm = res['chi'][2], res['mod'][2]
    print(f"PHASE: max|Zn_chi - Zn_mod| {np.abs(Zc - Zm).max():.3e}; max|Im Zn_chi| {np.abs(Zc.imag).max():.3e}; lam_min chi - mod {res['chi'][0] - res['mod'][0]:+.3e}")
    w, V = np.linalg.eigh(0.5 * (Zm + Zm.T)); v = V[:, 0]
    print(f"first-order shift v_mod^T (Z_chi - Z_mod) v_mod = {np.real(np.conj(v) @ (0.5*(Zc + Zc.conj().T) - Zm) @ v):+.3e}")
    np.save(P + '_TOR1_Zchi.npy', Zc); np.save(P + '_TOR1_Zmod.npy', Zm)
