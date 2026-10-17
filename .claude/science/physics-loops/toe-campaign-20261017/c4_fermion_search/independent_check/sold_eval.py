"""Claim (2) set evaluation: -1 in group (as signed, and for any re-signing of orbits), torus log2 dims, 3D mobility."""
import sys, pickle, time
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from sitecore import *
from signs import elim_masked, solve, star_to_torus
from mob4 import ext_test
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
D = pickle.load(open(W + 'sold_sets.pkl', 'rb')); orbs, isG, cl = D['orbs'], D['isG'], D['cliques']
for k, c in enumerate(sorted(cl, key=len)):
    signed = [(s, to21(T)) for u in c for T, s in orbs[u][1].items()]
    basis, bad = local_basis(signed)
    res = [len(c), 'members', len(signed), 'localrank', len(basis), 'local -1 (orbit signs as built)', len(bad) > 0]
    # can any choice of per-orbit signs avoid -1 (locally / on tori)?
    items = [(to_op(to21(T), s, 5), 1 << j) for j, u in enumerate(c) for T, s in orbs[u][1].items()]
    piv, eqs = elim_masked(items, 375)
    okl, _ = solve(eqs, len(c)); res += ['re-signable locally', okl]
    for L in (4, 6):
        d, b = torus_dim(basis, L)
        n = 3*L**3
        tit = [(star_to_torus(op, L, (a, bb, e)), m) for op, m in piv for a in range(L) for bb in range(L) for e in range(L)]
        _, teqs = elim_masked(tit, n); okt, _ = solve(eqs + teqs, len(c))
        res += ['L%d log2dim' % L, d, '-1rels', len(b), 'resignable', okt]
    print(res, '%.1fs' % (time.time() - t0)); sys.stdout.flush()
    if len(c) == 3:
        print('   ', ext_test('sold_set%d' % k, [from21(S) for _, S in basis]))
