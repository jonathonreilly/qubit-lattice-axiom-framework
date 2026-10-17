import sys, re, ast, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
exec(open('framed.py').read().split("cands = [()]")[0])
O = c1.O
def rot_gen(g, M):
    out = {}
    for p, labs in g.items():
        for a, l in enumerate(labs):
            if not l: continue
            v = tuple(int(x) for x in M @ np.array(p)); d = M @ np.array(E[a])
            b = int(np.nonzero(d)[0][0]); s = int(d[b])
            site = v if s == 1 else tuple(v[i] - (1 if i == b else 0) for i in range(3))
            out.setdefault(site, [0,0,0]); out[site][b] = l
    return {p: tuple(v) for p, v in out.items()}
def rows(gens, L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a; R = []
    for v in itertools.product(range(L), repeat=3):
        for g in gens:
            x = np.zeros(2*n, np.uint8)
            for p, labs in g.items():
                for a, l in enumerate(labs):
                    if not l: continue
                    q = idx([v[i] + p[i] for i in range(3)], a)
                    if l in (1, 2): x[q] ^= 1
                    if l in (2, 3): x[n + q] ^= 1
            R.append(x)
    return np.array(R)
def rank(M): return c1.f2_rank_and_null(M)[0]
def same(g1, g2, L=4):
    A, B = rows(g1, L), rows(g2, L); ra, rb = rank(A), rank(B)
    return ra == rb == rank(np.concatenate([A, B]))
fermions = [ast.literal_eval(m.group(1)) for m in (re.match(r'FERMION (\[.*\]) \(', l) for l in open('framed.log')) if m]
for S in fermions:
    gens = [A] + [plaq(c, S) for c in range(3)]
    stab = sum(1 for M in O if same(gens, [rot_gen(g, M) for g in gens]))
    print('framing', S, '| stabilizer order in O:', stab, '| orbit size:', 24 // stab, flush=True)
