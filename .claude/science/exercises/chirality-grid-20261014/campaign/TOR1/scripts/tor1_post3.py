"""TOR-1 final kernel table (F3 registered estimator + F7 follow-up estimator) on pool P2."""
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
def norm(L): d = L.diagonal().real; return np.exp(L - 0.5 * (d[:, None] + d[None, :]))
def sub_norm(L):
    d = L.diagonal().real; Z = np.full(L.shape, np.nan + 0j); m = ~np.isnan(L.real)
    for a, b in zip(*np.where(m)):
        if not (np.isnan(d[a]) or np.isnan(d[b])): Z[a, b] = np.exp(L[a, b] - 0.5 * (d[a] + d[b]))
    return Z
def lev(n, nw, mode):
    out = {}
    for ops in (cheap, ['chi']):
        x = load(n, nw, ops, mode)
        if x: out.update(x)
    return out
A, B, Bp, C, Cf = lev(2, 8, 'upper'), lev(2, 12, 'upper'), lev(2, 16, 'upper'), lev(3, 8, 'sub122'), lev(3, 8, 'fix00')
herm = load(2, 8, ['chi'], 'rev112'); out = {}
for op in ['chi'] + cheap:
    if op not in A: continue
    ZA = norm(full(A[op])); k = len(ZA)
    h = 0.0
    if op == 'chi' and herm is not None:
        LA = full(A[op]); d = LA.diagonal().real; Lr = herm['chi']
        for a in range(k):
            for b in range(k):
                if not np.isnan(Lr[a, b].real):
                    h = max(h, abs(np.exp(Lr[a, b] - 0.5 * (d[a] + d[b])) - np.conj(np.exp(LA[b, a] - 0.5 * (d[a] + d[b])))))
    def qplane(Cd):
        if op not in Cd: return np.nan
        ZC = sub_norm(Cd[op]); m = ~np.isnan(ZC.real); return np.abs(ZC - ZA)[m].max()
    qp = np.nanmax([qplane(C), qplane(Cf)]) if (op in C or op in Cf) else np.nan
    rows = []
    if op in B:
        ZB = norm(full(B[op])); qB = np.abs(ZB - ZA).max(); E3 = k * np.nanmax([qB, qp, h, 0]) + 1e-13
        ev = np.linalg.eigvalsh(0.5 * (ZB + ZB.conj().T)); rows.append(('F3 (kernel B=(2,12))', ev, qB, E3, ZB))
    if op in Bp and op in B:
        ZBp = norm(full(Bp[op])); qBp = np.abs(ZBp - ZB).max(); E7 = k * np.nanmax([qBp, qp, h, 0]) + 1e-13
        ev = np.linalg.eigvalsh(0.5 * (ZBp + ZBp.conj().T)); rows.append(("F7 (kernel B'=(2,16))", ev, qBp, E7, ZBp))
    for (nm, ev, qpo, E, Z) in rows:
        comp = not np.isnan(qp)
        print(f"{op:4s} {nm:22s}: lam_min {ev[0]:+.5e} lam_2 {ev[1]:+.3e} max {ev[-1]:.4f} min/max {ev[0]/ev[-1]:+.3e} | q_poly {qpo:.2e} q_plane {qp:.2e} h {h:.1e} | E {E:.2e} "
              f"| plane-estimate present {comp} | conv-negative {comp and ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E}", flush=True)
        out[(op, nm[:2])] = (ev[0], E, Z)
for tag in ('F3', 'F7'):
    if ('chi', tag) in out and ('mod', tag) in out:
        Zc, Zm = out[('chi', tag)][2], out[('mod', tag)][2]; Hc = 0.5 * (Zc + Zc.conj().T)
        w, V = np.linalg.eigh(0.5 * (Zm + Zm.T)); v = V[:, 0]; wc, Vc = np.linalg.eigh(Hc)
        print(f"PHASE {tag}: max|Zn_chi - Zn_mod| {np.abs(Zc - Zm).max():.3e}; max|Im Zn_chi| {np.abs(Zc.imag).max():.3e}; lam_min chi - mod {wc[0] - w[0]:+.3e}; "
              f"first-order {np.real(v @ (Hc - Zm) @ v):+.3e}; |<v_mod|v_chi>| {abs(np.vdot(v, Vc[:, 0])):.6f}; chi/O lam ratio {wc[0]/out[('O', tag)][0]:.2f}" if ('O', tag) in out else "")
        np.save(f"{P}_TOR1_Zchi_{tag}.npy", Zc); np.save(f"{P}_TOR1_Zmod_{tag}.npy", Zm)
