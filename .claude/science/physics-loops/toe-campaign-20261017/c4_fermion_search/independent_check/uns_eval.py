"""Claim (3): evaluate the 1233 maximal commuting sets of the unsoldered C4/C3 class."""
import sys, pickle, time
from collections import Counter
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from sitecore import *
from signs import elim_masked, solve, star_to_torus
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
orbs = pickle.load(open(W + 'uns_orbs.pkl', 'rb')); cl = pickle.load(open(W + 'uns_cliques.pkl', 'rb'))
rows = []
for n, c in enumerate(cl):
    signed = [(1, to21(T)) for u in c for T in orbs[u][1]]
    basis, bad = local_basis(signed)
    items = [(to_op(T, s, 5), 1 << j) for j, u in enumerate(c) for s, T in [(1, to21(T)) for T in orbs[u][1]]]
    piv, eqs = elim_masked(items, 375)
    ok = solve(eqs, len(c))[0]
    rec = {'clique': c, 'basis': basis, 'local_bad_asbuilt': len(bad) > 0, 'resignable': ok}
    for L in (4, 6):
        d, b = torus_dim(basis, L); rec['d%d' % L] = d; rec['bad%d' % L] = len(b)
        if ok:
            tit = [(star_to_torus(op, L, (a, bb, e)), m) for op, m in piv for a in range(L) for bb in range(L) for e in range(L)]
            _, teqs = elim_masked(tit, 3*L**3); ok = ok and solve(eqs + teqs, len(c))[0]
    rec['valid'] = ok
    rows.append(rec)
    if n % 100 == 0: print(n, '%.0fs' % (time.time() - t0)); sys.stdout.flush()
pickle.dump(rows, open(W + 'uns_eval.pkl', 'wb'))
val = [r for r in rows if r['valid']]
print('maximal sets', len(rows), 'valid (some signing, no -1 locally & L=4,6)', len(val),
      'valid with all-+ signs', sum(1 for r in rows if not r['local_bad_asbuilt'] and r['bad4'] == 0 and r['bad6'] == 0))
eq = [r for r in val if r['d4'] == r['d6'] and r['d4'] > 0]
print('valid with equal nonzero log2dim at L=4,6:', len(eq), Counter(r['d4'] for r in eq))
print('valid (d4,d6) histogram', sorted(Counter((r['d4'], r['d6']) for r in val).items()))
print('all (d4,d6,valid) histogram', sorted(Counter((r['d4'], r['d6'], r['valid']) for r in rows).items()))
print('time %.1fs' % (time.time() - t0))
