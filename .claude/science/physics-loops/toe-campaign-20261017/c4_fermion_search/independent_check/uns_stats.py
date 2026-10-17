import sys, pickle, time
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
from stats2 import mobile_signs
from mob4 import ext_test
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
rows = pickle.load(open(W + 'uns_eval.pkl', 'rb'))
eq = [r for r in rows if r['valid'] and r['d4'] == r['d6'] and r['d4'] > 0]
def gdict(S):
    return {(POS[i], a): (LX[S[3*i+a]], LZ[S[3*i+a]]) for i in range(7) for a in range(3) if S[3*i+a]}
summary = []
for n, r in enumerate(eq):
    gens = [gdict(S) for s, S in r['basis']]
    a = mobile_signs(gens, 3, ((2,0,0),(0,2,0),(0,0,2)), r=2)
    b = mobile_signs(gens, 3, ((2,0,0),(0,2,0),(0,0,2)), r=3)
    c = mobile_signs(gens, 3, ((4,0,0),(0,4,0),(0,0,4)), r=2)
    d = mobile_signs(gens, 3, ((-2,0,0),(0,-2,0),(0,0,-2)), r=2)
    ext = ext_test('uns_eq%d' % n, [from21(S) for s, S in r['basis']]).split('|')
    ext3 = [x for x in ext if 'Ext^3 localized' in x][0].strip()
    line = (n, 'orbits', len(r['clique']), 'k', len(gens), 'movable dims', a[0], 'mobile dim', a[1],
            'signs r2', sorted(a[2].values()), 'r3 same', a[2] == b[2], '4e same', a[2] == c[2], '-2e same', a[2] == d[2], ext3)
    print(line, '%.0fs' % (time.time() - t0)); sys.stdout.flush()
    summary.append((a[1], tuple(sorted(set(a[2].values()))), a[2] == b[2] == c[2] == d[2], 'isZero=0' in ext3))
from collections import Counter
print(Counter(summary))
