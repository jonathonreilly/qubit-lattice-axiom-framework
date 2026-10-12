"""R8-4 D-check: (i) are the frame-fixed cutoffs (leg cutoff, total-momentum cutoff on X and Y) inactive on the
support used by toy N's mixed coefficient?  (ii) rerun the mixed coefficient with widened cutoffs."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import r84_toyN_cont as D
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
grid = np.linspace(-2.6, 2.6, 121); h = grid[1] - grid[0]
for p in [0.0, 0.1, 0.2, 0.3, 0.4, 0.6]:
    mk = 0.0; mi = 0.0
    for sg in (1, -1):
        e, k, ps, w = D.cluster(sg*p, ('Y', 'A', 'B'), grid, h)
        mk = max(mk, np.max(np.abs(np.concatenate(k))))
        for kY in np.unique(k[0]):
            e2, k2, ps2, w2 = D.cluster(kY, ('U', 'C', 'D'), grid, h)
            if len(ps2): mi = max(mi, np.max(np.abs(np.concatenate(k2))))
    kYmax = max(np.max(np.abs(D.cluster(sg*p, ('Y','A','B'), grid, h)[1][0])) for sg in (1, -1))
    pr(f'p={p:.2f}: max |leg| outer {mk:.3f}; max |k_Y| {kYmax:.3f} (totc plateau {D.P["C1"]}); max |leg| inner {mi:.3f} (leg plateau {D.P["A1"]})')
D.P.update(dict(A1=2.45, A2=2.9, C1=1.9, C2=2.3))
rows, yrows = D.run(121, K=3.0)
pr(f'# widened cutoffs {D.P}')
r0 = rows[0]
for r in rows:
    pr(f'  p={r[0]:.2f}  m2_1={r[1]:+.10e}  mix={r[4]:+.10e}   rel.dev: 1loop {(r[1]-r0[1])/abs(r0[1]):+.2e}  mix {(r[4]-r0[4])/abs(r0[4]):+.2e}')
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(OUT) + '\n')
