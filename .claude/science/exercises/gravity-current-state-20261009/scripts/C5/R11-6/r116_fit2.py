"""R11-6 fits: (i) registered dense S4 observables T_B, T_H (full r range 3..96, as registered; floor flags L=240 vs 320);
(ii) secondary: large-r components restricted to the operator-dominated range r >= 80."""
import numpy as np, re, sys
from r116_fit import compare, parse
def dense_blocks(fn):
    blocks = []; cur = None; P = None
    for line in open(fn):
        m = re.match(r'L=(\d+) K=(\d+) P=([-\d.]+)', line)
        if m: P = float(m.group(3)); continue
        m = re.search(r'(dimer|gauss) r=\s*([\d.]+)\s+T_B=([\d.eE+-]+)\s+T_H=([\d.eE+-]+).*U_B=\|\|\(B-1\)psi\|\|=([\d.eE+-]+)\s+U_H=\|\|\(H_S-H_BT\)psi\|\|=([\d.eE+-]+).*?=([\d.eE+-]+)$', line.strip())
        if m:
            key = (P, m.group(1))
            if cur is None or cur[0] != key: cur = [key, []]; blocks.append(cur)
            cur[1].append([float(m.group(i)) for i in range(2, 8)])
    return {b[0]: np.array(b[1]) for b in blocks}
out = []
def pr(s): print(s); out.append(s)
D = {}
for fn in sys.argv[1:]:
    if '_s4_' in fn: D[fn] = dense_blocks(fn)
for fn, bl in D.items():
    for key, a in bl.items():
        r = a[:, 0]
        for j, name in ((1, 'T_B'), (2, 'T_H')):
            d, v, p, c, b = compare(r, a[:, j])
            pr('%s P=%+.1f %s %s (registered, r=%.0f..%.0f, n=%d): dAICc(W-S)=%+.2f -> %s | values %s | max ||(B_a^T B_a-1)psi|| = %.1e'
               % (fn, key[0], key[1], name, r[0], r[-1], len(r), d, v, ' '.join('%.2e' % x for x in a[:, j]), a[:, 5].max()))
# floor flags: L=240 vs L=320 at P=0.4 dimer
k240 = [f for f in D if 'L240' in f]; k320 = [f for f in D if 'L320' in f]
if k240 and k320:
    a2 = D[k240[0]].get((0.4, 'dimer')); a3 = D[k320[0]].get((0.4, 'dimer'))
    if a2 is not None and a3 is not None:
        for j, name in ((1, 'T_B'), (2, 'T_H')):
            rel = np.abs(a3[:, j] - a2[:, j])/a3[:, j]
            flag = rel > 0.30
            pr('floor/discretization flags %s (L=240 vs 320, >30%%): %s ; rel changes %s' % (name, ' '.join('r=%.1f' % x for x in a3[flag, 0]) or 'none', ' '.join('%.2f' % x for x in rel)))
            ok = ~flag
            if ok.sum() >= 5:
                d, v, p, c, b = compare(a3[ok, 0], a3[ok, j]); pr('   secondary fit on unflagged points (n=%d): dAICc=%+.2f -> %s' % (ok.sum(), d, v))
            else: pr('   secondary fit: fewer than 5 unflagged points')
for fn in [f for f in sys.argv[1:] if '_tails_' in f]:
    r, T = parse(fn); r = np.array(r); T = np.array(T); s = r >= 80
    d, v, p, c, b = compare(r[s], T[s])
    pr('%s operator range r>=80 (n=%d): dAICc(W-S)=%+.2f -> %s | power p=%.2f | beta=%.2f' % (fn, s.sum(), d, v, p, b))
open('r116_fit2.out', 'w').write('\n'.join(out) + '\n')
