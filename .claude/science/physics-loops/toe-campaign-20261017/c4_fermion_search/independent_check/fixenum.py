"""Backtracking enumeration of star strings fixed (labels mod sign) by a rotation g and
commuting with every translate of every O-image of themselves.
usage: enum.py soldered|unsoldered  gnames..."""
import sys, time, pickle, itertools, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
sold = sys.argv[1] == 'soldered'
SP, ROT, SG = tables(sold)
GM = {'C2z': np.array([[-1,0,0],[0,-1,0],[0,0,1]]), 'C2xy': np.array([[0,1,0],[1,0,0],[0,0,-1]]),
      'C4z': np.array([[0,-1,0],[1,0,0],[0,0,1]]), 'C3': np.array([[0,0,1],[1,0,0],[0,1,0]])}
def ridx(M): return [r for r, R in enumerate(O) if (R == M).all()][0]
SPinv = np.zeros_like(SP)
for r in range(24):
    for i in range(7): SPinv[r, SP[r, i]] = i
# constraints: (R,t) -> list of pairs (i, k, r): COMM[S_i, ROT[r][S_k]] with k = R^-1 j
CONS = []
for r in range(24):
    for t, pr in OVL.items():
        CONS.append([(i, int(SPinv[r, j])) for i, j in pr])

def enumerate_fixed(gname):
    g = ridx(GM[gname]); t0 = time.time()
    # powers of g
    pw = [None]; M = np.eye(3, dtype=int)
    H = []
    while True:
        M = M.dot(GM[gname]); H.append(ridx(M))
        if (M == np.eye(3, dtype=int)).all(): break
    # site orbits under <g>
    seen = set(); var = []   # (rep, [(site, r_power mapping rep->site)])
    for i in range(7):
        if i in seen: continue
        orb = {}
        for r in [ridx(np.eye(3, dtype=int))] + H:
            j = int(SP[r, i])
            if j not in orb: orb[j] = r
        seen |= set(orb); var.append((i, orb))
    # domains: codes at rep fixed by its stabilizer in <g>
    doms = []
    for i, orb in var:
        stab = [r for r in H if SP[r, i] == i]
        doms.append([c for c in range(64) if all(ROT[r, c] == c for r in stab)])
    site2var = {}
    for v, (i, orb) in enumerate(var):
        for j in orb: site2var[j] = v
    # each constraint is checked at the depth of its last variable
    bydepth = [[] for _ in var]
    for pr in CONS:
        if not pr: continue
        d = max(max(site2var[i], site2var[k]) for i, k in [(a, b) for a, b in pr])
        bydepth[d].append(pr)
    # rotation index for each constraint pair is needed: rebuild with r
    bydepth = [[] for _ in var]; ci = 0
    for r in range(24):
        for t, pr in OVL.items():
            ps = [(i, int(SPinv[r, j])) for i, j in pr]
            if ps:
                d = max(max(site2var[i], site2var[k]) for i, k in ps)
                bydepth[d].append((r, ps))
    out = []; S = [0]*7; nodes = [0]
    def rec(d):
        if d == len(var):
            out.append(tuple(S)); return
        i, orb = var[d]
        for c in doms[d]:
            for j, r in orb.items(): S[j] = ROT[r, c]
            nodes[0] += 1
            ok = True
            for r, ps in bydepth[d]:
                s = 0
                for a, b in ps: s ^= COMM[S[a], ROT[r, S[b]]]
                if s: ok = False; break
            if ok: rec(d + 1)
    rec(0)
    # verify fixedness and self-commutation directly with the 21-label core on all results
    gm = GM[gname]
    for S7 in out:
        assert act(gm, to21(S7), sold)[1] == to21(S7)
    print(gname, 'vars', [len(o) for _, o in var], 'domains', [len(x) for x in doms],
          'search space', int(np.prod([len(x) for x in doms])), 'nodes', nodes[0], 'found', len(out),
          'time %.1fs' % (time.time() - t0)); sys.stdout.flush()
    return out

if __name__ == '__main__':
    res = {}
    for gname in sys.argv[2:]:
        res[gname] = enumerate_fixed(gname)
    pickle.dump(res, open(W + 'fixed_%s_%s.pkl' % (sys.argv[1], '_'.join(sys.argv[2:])), 'wb'))
