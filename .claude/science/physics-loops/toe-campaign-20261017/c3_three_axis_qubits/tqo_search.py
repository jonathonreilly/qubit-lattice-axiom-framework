"""Among compatible orbit unions, find rules with trivial single-site commutant (TQO-1 candidates),
minimal by inclusion, then test 3D mobility with Singular Ext^3 (module_tool)."""
import sys, pickle, itertools, subprocess, time
import numpy as np
from module_tool import singular_script
ACTION, FACTION = sys.argv[1], sys.argv[2]
MAXK = int(sys.argv[3]) if len(sys.argv) > 3 else 2
d = pickle.load(open(f'orb3_{ACTION}_{FACTION}.pkl', 'rb'))
reps, elems, adj = d['reps'], d['elems'], d['adj']
n = len(reps)
def dec(a): return [((int(a) >> (4*i)) & 15) for i in range(7)]
def sp1(a, b): return int(a != 0 and b != 0 and a != b)
def anti(l1, l2): return sp1(l1 >> 2, l2 >> 2) ^ sp1(l1 & 3, l2 & 3)
labels = [set(l for e in elems[k] for l in dec(e)) - {0} for k in range(n)]
def commutant(labs): return frozenset(p for p in range(1, 16) if all(not anti(p, l) for l in labs))
comm1 = [commutant(labels[k]) for k in range(n)]
print('orbits', n, 'single orbits with trivial commutant', sum(1 for c in comm1 if not c), flush=True)
cands = [(k,) for k in range(n) if not comm1[k]]
if MAXK >= 2:
    for i in range(n):
        if not comm1[i]: continue
    for i in range(n):
        for j in adj[i]:
            if j <= i: continue
            if not comm1[i] or not comm1[j]: continue   # minimal: neither alone suffices
            if not (comm1[i] & comm1[j]): cands.append((i, j))
print('minimal candidate unions (size <= %d):' % MAXK, len(cands), flush=True)
pickle.dump(cands, open(f'tqo_cands_{ACTION}_{FACTION}.pkl', 'wb'))
STAR = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def gens_of(c):
    gs = []
    for k in c:
        for e in elems[k]:
            l = dec(e); gs.append({STAR[i]: (l[i] >> 2, l[i] & 3) for i in range(7) if l[i]})
    return gs
R = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/runsing.sh'
LIM = int(sys.argv[4]) if len(sys.argv) > 4 else 50
res = []
for c in cands[:LIM]:
    open('tmp_tqo.sing', 'w').write(singular_script(gens_of(c), 2, 'c'))
    t0 = time.time()
    out = subprocess.run([R, 'tmp_tqo.sing'], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=600).stdout
    mob = out.split('3D-mobile charge exists)?')[1].split()[0] if '3D-mobile' in out else '?'
    L = 'IXYZ'
    print(c, [len(elems[k]) for k in c], 'mobile3D =', mob, f'{time.time()-t0:.1f}s', '|', ' / '.join(' '.join(L[x>>2]+L[x&3] for x in dec(elems[k][0])) for k in c), flush=True)
    res.append((c, mob))
pickle.dump(res, open(f'tqo_res_{ACTION}_{FACTION}.pkl', 'wb'))
