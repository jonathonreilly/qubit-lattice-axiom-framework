"""K2c-C (PREREG.md): kernels on a saved pool under a selectable crossing weight (default hard = X3's measure):
PG (no fermion), W, O (Neuberger), SH (Shamir overlap = L_s->inf), DWF_4, DWF_8 (PV-subtracted, transfer formula, checked vs
dense 5D ratio on 3 points, < 1e-10 required), and bare D5_4, D5_8 (dense; open pools only).
usage: python3 k2c_dwf.py POOL.npz [WEIGHT]"""
import numpy as np, sys, time
from k2c_lib import *

name = sys.argv[1]; weight = sys.argv[2] if len(sys.argv) > 2 else 'hard'; t00 = time.time()
d = np.load(name); torus = '_torus_' in name; T = d['ux'].shape[1]
G = Geom(2, T, torus, 1 if torus else -1); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U)
qlo, qhi, q3 = (((6, 4), (8, 6), (10, 8)) if torus else ((16, None), (32, None), (48, None)))
dense = not torus
OPS = ['PG', 'W', 'O', 'SH', 'DWF_4', 'DWF_8'] + (['D5_4', 'D5_8'] if dense else [])
Fs, Bs = G.crossing_mats()
print(f"# K2c-C pool {name}: Lx={G.Lx} Lt={G.Lt} torus={torus} k={k} weight={weight} quad lo={qlo} hi={qhi} third={q3}; "
      f"max bulk |plaquette| {max(max_bulk(G, u) for u in U):.4f} (margin limit {DB})", flush=True)
# formula check vs dense 5D ratio, and SH formula vs direct SH, on 3 points of entry (0, 1)
ph, w = nodes(G, U[0], U[1], DELTA, 4, weight, 4 if torus else None); Db = D_batch(G, G.D0(U[0], U[1]), Fs, Bs, ph[:3])
f, _ = dwf_formula_logs(G, Db, [4, 8, 'inf'])
chk = max(np.abs(f[Ls] - logdet_op(G, Db, 'D5PV', Ls)[0]).max() for Ls in (4, 8)); chk2 = np.abs(f['inf'] - logdet_op(G, Db, 'SH')[0]).max()
print(f"formula vs dense D5PV (L_s=4,8): max|d logdet| {chk:.1e}; formula(inf) vs direct SH {chk2:.1e}", flush=True)
if chk > 1e-10: OPS = [o for o in OPS if not o.startswith('DWF')]; print("FORMULA CHECK FAILED: DWF columns dropped")


def point_all(Db):
    out = {}; gaps = []
    out['PG'] = np.zeros(Db.shape[0], complex)
    out['W'], _ = logdet_op(G, Db, 'W')
    out['O'], g1 = logdet_op(G, Db, 'O'); gaps.append(np.nanmin(g1))
    fo, g2 = dwf_formula_logs(G, Db, [4, 8, 'inf']); gaps.append(np.nanmin(g2))
    out['SH'] = fo['inf']; out['DWF_4'] = fo[4]; out['DWF_8'] = fo[8]
    if dense:
        for Ls in (4, 8): out[f'D5_{Ls}'], _ = logdet_op(G, Db, 'D5', Ls)
    return out, min(gaps)


def entries(n, nw, pairs):
    L = {op: {} for op in OPS}; gm = np.inf
    for (a, b) in pairs:
        ph, w = nodes(G, U[a], U[b], DELTA, n, weight, nw)
        if len(w) == 0 or w.sum() <= 0:
            for op in OPS: L[op][(a, b)] = -np.inf + 0j
            continue
        D0 = G.D0(U[a], U[b]); acc = {op: [] for op in OPS}
        ck = max(1, 4096 // (8 * G.N)) if dense else 32
        for c in range(0, len(w), ck):
            o, g = point_all(D_batch(G, D0, Fs, Bs, ph[c:c+ck])); gm = min(gm, g)
            for op in OPS: acc[op].append(o[op])
        for op in OPS:
            l = np.concatenate(acc[op]); lm = l.real.max(); L[op][(a, b)] = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
    return L, gm


def to_Z(Ld):
    Lm = np.full((k, k), -np.inf + 0j)
    for (a, b), v in Ld.items():
        Lm[a, b] = v; Lm[b, a] = np.conj(v)
    for a in range(k): Lm[a, a] = Lm[a, a].real
    return normalized(Lm)


allp = [(a, b) for a in range(k) for b in range(a, k)]
Llo, glo = entries(qlo[0], qlo[1], allp); Lhi, ghi = entries(qhi[0], qhi[1], allp)
rs = np.random.default_rng(99); sub = set()
while len(sub) < min(12, k * (k - 1) // 2):
    a_ = int(rs.integers(k)); b_ = int(rs.integers(k))
    if a_ != b_: sub.add((min(a_, b_), max(a_, b_)))
L3, g3 = entries(q3[0], q3[1], sorted(sub) + [(i, i) for i in range(k)])
print(f"min|eig H| over all points (H_W and H_T): {min(glo, ghi, g3):.3f}  [{time.time()-t00:.0f}s]", flush=True)
for op in OPS:
    Zl = to_Z(Llo[op]); Zh = to_Z(Lhi[op]); q = np.abs(Zh - Zl).max()
    dd = np.array([L3[op][(i, i)].real for i in range(k)]); qq3 = 0.0
    for (a, b) in sub:
        z = np.exp(L3[op][(a, b)] - 0.5 * (dd[a] + dd[b])) if np.isfinite(L3[op][(a, b)].real) else 0.0
        qq3 = max(qq3, abs(z - Zh[a, b]))
    E = k * max(q, qq3) + 1e-13; a, b, ev = lam(Zh)
    print(f"{op:6s}: lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} q3 {qq3:.1e} E {E:.1e} certified-negative {a < -10*E} PSD-within-error {a > -10*E}"
          f" | lowest eigs {np.array2string(ev[:3], precision=3)}", flush=True)
print(f"done [{time.time()-t00:.0f}s]")
