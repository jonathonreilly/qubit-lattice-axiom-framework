"""R9-7 common: kinematics, plateaus, and the 24 time orderings of the O(go^2 gi^2) X self-energy graph
(X sunset X -> Y A B with the Y line dressed by the inner quartet Y -> U C D, inner cluster = Phi of mass M).

Feynman-orientation lines: Y1: oa->i1 (k_Y), Phi: i1->i2 (k_Y, mass M, 3 fermions), Y2: i2->ob (k_Y),
A, B: oa->ob (k_A, k_B); external X_in absorbed at oa, X_out emitted at ob; k_Y + k_A + k_B = p.
Outer monomial types (each with h.c.):
  'dec' X -> Y A B          (toy N)        'vac' 0 -> X Y A B   (toy N)
  '22'  X Y -> A B          (new crossing) '31'  Y -> X A B     (new reverse decay)
Inner types: decay Y <-> UCD (weight sqrt h_i for fermions) and vacuum 0 <-> Y UCD."""
import itertools
import numpy as np
np.seterr(all='ignore')

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
    e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def plateau(x, x1, x2):
    return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))

def Fpl(s, L1, L2):
    if L1 is None:              # local limit: F == 1
        return np.ones_like(np.asarray(s, float))
    return plateau(np.sqrt(np.maximum(s, 0.0)), L1, L2)

def s2(E1, k1, E2, k2):
    return (E1 + E2)**2 - (k1 + k2)**2

def hfac(E, W, C=1.0):
    return (W*(1 + 2*C) - E)/(W + E)

VERT = ('oa', 'ob', 'i1', 'i2')
LINES = {'Y1': ('oa', 'i1', 1), 'Phi': ('i1', 'i2', 3), 'Y2': ('i2', 'ob', 1), 'A': ('oa', 'ob', 1), 'B': ('oa', 'ob', 1)}
TOYN_TYPES = {'dec', 'vac'}

def orderings():
    """list of dicts: perm, outer types at oa/ob, inner decay flags, present-lines per interval, fermion sign."""
    out = []
    for perm in itertools.permutations(VERT):
        t = {v: i for i, v in enumerate(perm)}
        oa_Ycre = t['i1'] > t['oa']; oa_ABcre = t['ob'] > t['oa']
        oa = {(True, True): 'dec', (False, False): 'vac', (False, True): '22', (True, False): '31'}[(oa_Ycre, oa_ABcre)]
        ob_Yann = t['i2'] < t['ob']; ob_ABann = t['oa'] < t['ob']
        ob = {(True, True): 'dec', (False, False): 'vac', (False, True): '22', (True, False): '31'}[(ob_Yann, ob_ABann)]
        i1_dec = (t['oa'] < t['i1']) == (t['i2'] > t['i1'])
        i2_dec = (t['ob'] > t['i2']) == (t['i1'] < t['i2'])
        nback = sum(nf for (a, b, nf) in LINES.values() if t[b] < t[a])
        pres = []
        for j in range(3):
            ls = [ln for ln, (a, b, nf) in LINES.items() if min(t[a], t[b]) <= j < max(t[a], t[b])]
            if j < t['oa']: ls.append('Xin')
            if j >= t['ob']: ls.append('Xout')
            pres.append(tuple(ls))
        out.append(dict(perm=perm, oa=oa, ob=ob, i1_dec=i1_dec, i2_dec=i2_dec, nback=nback, pres=pres,
                        toyN=(oa in TOYN_TYPES and ob in TOYN_TYPES)))
    return out

ORD = orderings()

if __name__ == '__main__':
    for o in ORD:
        print(o['perm'], o['oa'], o['ob'], 'i1dec' if o['i1_dec'] else 'i1vac', 'i2dec' if o['i2_dec'] else 'i2vac',
              'nback', o['nback'], 'toyN' if o['toyN'] else 'NEW', o['pres'])
    print('toy N orderings:', sum(o['toyN'] for o in ORD), ' total', len(ORD))
