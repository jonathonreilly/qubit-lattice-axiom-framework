#!/usr/bin/env python3
"""s2: finite-range walks (n = 2, 3, 4).  For each walk:
  * exact-grid W3 (Lemma Q of C5: N >= 6r+1 is exact), two grids;
  * certified decomposition of levels eps = 0 and pi into boxes;
  * Theorem L check: sum of box Chern numbers = -W3 = 0;
  * if the level is clean (only degenerate band touchings), the nodal chiralities at that
    level and their sum (Corollary NN: must be 0), plus velocity matrix and tilt.
Walks: shift-coin products Q, the D'Ariano-Perinotti BCC Weyl QCA, the C7 two-qubit
O-covariant Clifford walk (b_gold, which has massless pi-modes), a C4z-covariant coin
deformation of it that splits its Dirac nodes, and generic coupled n = 3, 4 walks.
"""
import sys
import numpy as np
import lib5b as L
import walks5b as WK

C = L.Checker()
I2 = np.eye(2)
KZ = np.kron(np.diag([1.0, -1.0]), L.SZ)          # tau3 sigma3 = -alpha_z : commutes with 1 (x) D(R_z)
SZs = np.kron(I2, L.SZ)                              # 1 (x) sigma3 = spin Sigma_z (axial b-field) : commutes with 1 (x) D(R_z)
cases = [
    WK.Q_product((1, 1, 1)),
    WK.dariano_perinotti_weyl(),
    WK.Q_product((2, 1, 1)),
    WK.c7_walk(WK.B_GOLD, 'C7-gold (O-covariant n=4)'),
    WK.conj_coin(WK.c7_walk(WK.B_GOLD, 'g'), SZs, 0.3, 'C7-gold deformed by axial coin exp(0.15i Sigma_z) (C4z-covariant)'),
    WK.coupled([WK.Q_product((1, 1, 1)), WK.phase_const(2.0)], 0.15, 11, 'n3: C(Q + e^{-2i})'),
    WK.coupled([WK.Q_product((1, 1, 1)), WK.Q_product((2, 1, 1))], 0.12, 12, 'n4: C(Q111 + Q211)'),
    WK.coupled([WK.Q_product((1, 1, 1)), L.lmul(L.lconst(-np.eye(2)), WK.Q_product((1, 1, 1)))], 0.12, 13, 'n4: C(Q + (-Q))'),
    WK.conj_coin(WK.c7_walk(WK.B_GOLD, 'g'), KZ, 0.3, 'C7-gold deformed by exp(0.15i tau3 sigma3) = vector-potential coin (C4z-covariant)'),
]
sel = [int(i) for i in sys.argv[1].split(',')] if len(sys.argv) > 1 else range(len(cases))

# C4z covariance of the deformed C7 walk (declared on-site action 1 (x) exp(-i pi sigma3/4))
from scipy.linalg import expm
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Dz = np.kron(I2, expm(-0.25j*np.pi*L.SZ))
Kt = np.random.default_rng(3).uniform(0, 2*np.pi, (200, 3))

summary = []
for i in sel:
    W = cases[i]
    print(f'=== [{i}] {W.name}  (n={W.n}, range r={W.range}, #hops={len(W.c)}, L={W.L:.3f})', flush=True)
    un = np.abs(W(Kt) @ np.conj(np.swapaxes(W(Kt), -1, -2)) - np.eye(W.n)).max()
    C.check(f'[{i}] unitary at 200 random k (err {un:.1e})', un < 1e-12)
    if i in (3, 4, 8):
        cov = np.abs(W(Kt @ Rz.T) - Dz @ W(Kt) @ Dz.conj().T).max()
        C.check(f'[{i}] C4z covariance U(Rk) = D U(k) D^dag (err {cov:.1e})', cov < 1e-12)
    r = W.range
    w1 = L.w3_grid(W, 6*r + 2); w2 = L.w3_grid(W, 6*r + 5, 0.37)
    print(f'  exact-grid W3: N={6*r+2}: {w1.real:+.2e}, N={6*r+5}: {w2.real:+.2e}')
    C.check(f'[{i}] exact-grid W3 = 0 (Theorem K)', abs(w1) < 1e-8 and abs(w2) < 1e-8, 'exact-grid certificate')
    det = np.linalg.det(W(Kt)); print(f'  det U range over samples: |det-det0| max {np.abs(det - det[0]).max():.1e}')
    for eps in (0.0, np.pi):
        res = L.analyze_level(W, eps, N0=32, depth=4, M=24)
        boxes = res['boxes']
        print(f'  level eps={eps:.4f}: bad cells {res["nbad"]}, components {res["ncomp"]}, decomposed={res["clean"]} {res["reason"]}')
        if not res['clean']:
            summary.append((W.name, eps, 'sheets/undecomposed', None, None))
            print('  (level not decomposable into isolated boxes: Fermi sheet(s); Theorem L still applies, not testable by boxes)')
            continue
        s = sum(round(b['ch']) for b in boxes)
        C.check(f'[{i}] eps={eps:.3f}: box Chern numbers integer, mesh-stable', all(abs(b['ch'] - round(b['ch'])) < 1e-9 and abs(b['ch'] - b['ch2']) < 1e-9 for b in boxes))
        C.check(f'[{i}] eps={eps:.3f}: Theorem L: sum Ch(P_<) = -W3 = 0 (got {s:+d})', s == 0)
        npock = sum(b['pocket'] for b in boxes)
        nod = [q for b in boxes for q in b['nodes']]
        clean = npock == 0
        weyl = [q for q in nod if q['gap_others'] > 1e-3]
        multi = [q for q in nod if q['gap_others'] <= 1e-3]
        print(f'  boxes {len(boxes)}, pocket boxes {npock}, Weyl (2-fold) nodes {len(weyl)}, >2-fold touchings {len(multi)}')
        for b in boxes:
            for q in b['nodes']:
                tag = 'Weyl' if q['gap_others'] > 1e-3 else 'multi'
                chs = f'{q["chi"]:+d}' if tag == 'Weyl' else 'n/a (>2-fold; 2-band linearization meaningless)'
                print(f'    {tag} node k={np.round(q["k"], 6)} chi={chs} tilt={np.round(q["tilt"], 4)} '
                      f'|v| sing.vals={np.round(np.linalg.svd(q["v"], compute_uv=False), 4)} box Ch={round(b["ch"]):+d}')
        if clean and not multi:
            chis = [q['chi'] for q in weyl]
            C.check(f'[{i}] eps={eps:.3f}: clean level with only Weyl nodes: sum chi = 0 (got {sum(chis):+d}, {len(chis)} nodes)', sum(chis) == 0)
            C.check(f'[{i}] eps={eps:.3f}: per box Ch = sum chi in box (Lemma S)', all(round(b['ch']) == sum(q['chi'] for q in b['nodes']) for b in boxes))
        summary.append((W.name, eps, 'clean' if clean else 'pockets', len(nod), s))
print('\nSUMMARY (walk, level, structure, #degenerate touchings, sum box Ch):')
for row in summary:
    print('  ', row)
C.total()
