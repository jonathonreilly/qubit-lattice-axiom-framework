"""O-closure of the fixed self-commuting strings; strings / orbits / sign-consistent orbits.
usage: orbits.py soldered|unsoldered g1 g2 ..."""
import sys, pickle, time
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
mode = sys.argv[1]; gs = sys.argv[2:]
sold = mode == 'soldered'
SP, ROT, SG = tables(sold)
res = pickle.load(open(W + 'fixed_%s_C2z_C2xy_C4z_C3.pkl' % mode, 'rb'))
base = set(s for g in gs for s in res[g])
idS = (0,)*7
def signed_orbit(S):
    d = {}
    for r in range(24):
        T = [0]*7; sg = 1
        for i in range(7):
            T[SP[r, i]] = ROT[r, S[i]]; sg *= SG[r, S[i]]
        T = tuple(T)
        if T in d and d[T] != sg: return d, False
        d[T] = sg
    return d, True
allS = set(); orbs = []; ncons = 0
for S in sorted(base):
    if S in allS: continue
    d, ok = signed_orbit(S)
    allS |= set(d); orbs.append((S, d, ok)); ncons += ok
# check the O-closed set is still self-commuting (it must be, by O-invariance)
print(mode, gs, 'base fixed strings', len(base), 'O-closure strings', len(allS),
      '(excluding identity: %d)' % (len(allS) - (idS in allS)), 'orbits', len(orbs),
      'sign-consistent', ncons, 'incl identity orbit', idS in allS, '%.1fs' % (time.time() - t0))
pickle.dump(orbs, open(W + 'orbs_%s_%s.pkl' % (mode, '_'.join(gs)), 'wb'))
