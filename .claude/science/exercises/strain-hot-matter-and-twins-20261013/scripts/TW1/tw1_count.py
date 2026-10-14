"""TW-1 (b), (d): reality type of each SM Weyl field per gauge factor, and exact staggered-count matching.

Building blocks in continuous time (tw1_alg.out):
  complex staggered field in irrep R  -> 2 Dirac in R  = 2 R + 2 Rbar   (left-handed Weyl multiset)
  reduced (Majorana) field in REAL irrep R0 -> 2 R0 (Weyl); exists only for real R0 (Schur, tw1_alg item 3)
A Weyl content W is realizable with NO surplus iff, for every irrep R appearing:
  complex type (R != Rbar): mult(R) = mult(Rbar) and mult(R) even;
  pseudo-real: mult(R) = 0 mod 4  (only complex fields; R = Rbar so each gives 4 R);
  real: mult(R) even (reduced fields; a complex field gives 4 R).
Reality type per factor: SU(3): 1 real, 3/3bar complex; SU(2): 1 real, 2 pseudo-real; U(1): q = 0 real, q != 0 complex;
product type: complex if any factor complex, else real/pseudo by the product of Frobenius-Schur indicators.
Left-handed frame, hypercharge Y with Q = T3 + Y (SM: Q (3,2,1/6), u^c (3b,1,-2/3), d^c (3b,1,1/3), L (1,2,-1/2), e^c (1,1,1), nu^c (1,1,0)).
"""
from fractions import Fraction as Fr
from collections import Counter

FS3 = {'1': 1, '3': 0, '3b': 0}
CONJ3 = {'1': '1', '3': '3b', '3b': '3'}
FS2 = {1: 1, 2: -1}
GEN = [('Q', '3', 2, Fr(1, 6), 1), ('u^c', '3b', 1, Fr(-2, 3), 1), ('d^c', '3b', 1, Fr(1, 3), 1),
       ('L', '1', 2, Fr(-1, 2), 1), ('e^c', '1', 1, Fr(1), 1)]
NUR = ('nu^c', '1', 1, Fr(0), 1)


def fs(rep, factors):
    c, d, y = rep
    ind = 1
    if 'SU3' in factors: ind *= FS3[c]
    if 'SU2' in factors: ind *= FS2[d]
    if 'U1' in factors: ind *= (1 if y == 0 else 0)
    return ind


def conj(rep):
    c, d, y = rep
    return (CONJ3[c], d, -y)


def project(rep, factors):
    c, d, y = rep
    return (c if 'SU3' in factors else '1', d if 'SU2' in factors else 1, y if 'U1' in factors else Fr(0))


def content(fields, factors, expand=True):
    """multiset of irreps of the chosen factor group; a factor not kept splits its rep into dim-many singlet copies."""
    W = Counter()
    for nm, c, d, y, m in fields:
        mult = m
        if 'SU3' not in factors: mult *= (1 if c == '1' else 3)
        if 'SU2' not in factors: mult *= d
        W[project((c, d, y), factors)] += mult
    return W


def match(W, factors):
    bad = []
    for R, m in W.items():
        t = fs(R, factors)
        if t == 0:
            if W.get(conj(R), 0) != m or m % 2: bad.append((R, m, 'complex: mult(R)=%d, mult(Rbar)=%d' % (m, W.get(conj(R), 0))))
        elif t == -1:
            if m % 4: bad.append((R, m, 'pseudo-real: mult %d not = 0 mod 4' % m))
        else:
            if m % 2: bad.append((R, m, 'real: mult %d odd' % m))
    return bad


def name(R):
    c, d, y = R
    return '(%s,%d,%s)' % (c, d, y)


print('(b) reality type per factor (FS indicator: +1 real, -1 pseudo-real, 0 complex), LH Weyl frame')
print('  %-6s %-5s %-5s %-8s | %-8s %-8s %-8s | G_SM' % ('field', 'SU3', 'SU2', 'Y', 'SU3', 'SU2', 'U1_Y'))
tp = {1: 'real', -1: 'pseudo', 0: 'complex'}
for nm, c, d, y, m in GEN + [NUR]:
    R = (c, d, y)
    print('  %-6s %-5s %-5d %-8s | %-8s %-8s %-8s | %s' % (nm, c, d, y, tp[FS3[c]], tp[FS2[d]], tp[1 if y == 0 else 0],
                                                       tp[fs(R, ('SU3', 'SU2', 'U1'))]))
print('  embeddings (comparator, Slansky 1981): SU(5) 5bar, 10 complex; SO(10) 16 complex (Spin(10) spinor, 10 = 2 mod 8);'
      ' Pati-Salam (4,2,1), (4bar,1,2) complex (SU(4) 4 complex); 16 + 16bar real.')

print('\n(d) exact staggered-count matching (no surplus), per gauge group and content')
groups = [('G_SM', ('SU3', 'SU2', 'U1')), ('SU3 x SU2', ('SU3', 'SU2')), ('SU3 only', ('SU3',)), ('SU2 only', ('SU2',)),
          ('U1_Y only', ('U1',))]
contents = [('1 gen, no nu_R', GEN, 1), ('1 gen + nu_R', GEN + [NUR], 1), ('3 gen, no nu_R', GEN, 3), ('3 gen + 3 nu_R', GEN + [NUR], 3),
            ('2 gen + 2 nu_R', GEN + [NUR], 2), ('4 gen + 4 nu_R', GEN + [NUR], 4)]
for gname, fac in groups:
    for cname, flds, ng in contents:
        W = content([(a, b, c, d, m*ng) for a, b, c, d, m in flds], fac)
        bad = match(W, fac)
        print('  %-10s %-16s : %s' % (gname, cname, 'MATCH' if not bad else 'fails: ' + '; '.join('%s %s' % (name(R), why) for R, m, why in bad[:3])))
# SM + mirror
for gname, fac in groups[:1]:
    for ng in (1, 2, 3):
        flds = [(a, b, c, d, m*ng) for a, b, c, d, m in GEN + [NUR]]
        W = content(flds, fac)
        Wm = Counter({conj(R): m for R, m in W.items()})
        bad = match(W + Wm, fac)
        print('  %-10s %d gen + nu_R + %d mirror gen: %s' % (gname, ng, ng, 'MATCH' if not bad else 'fails: ' + '; '.join('%s %s' % (name(R), why) for R, m, why in bad[:2])))

# unbroken SU(3) x U(1)_em, LH Weyl: Q_em = T3 + Y
print('\n  unbroken SU(3)_c x U(1)_em (the gauge content the C5 root actually builds: vector U(1) + colour C_F)')
EM = []
for nm, c, d, y, m in GEN + [NUR]:
    if d == 2:
        EM += [(nm + '+', c, 1, y + Fr(1, 2), m), (nm + '-', c, 1, y - Fr(1, 2), m)]
    else:
        EM.append((nm, c, 1, y, m))
for cname, extra, ng in (('1 gen, no nu_R', False, 1), ('1 gen + nu_R', True, 1), ('2 gen + 2 nu_R', True, 2), ('3 gen + 3 nu_R', True, 3), ('3 gen, no nu_R', False, 3)):
    flds = [(a, b, c, d, m*ng) for a, b, c, d, m in EM if extra or a != 'nu^c']
    W = content(flds, ('SU3', 'U1'))
    bad = match(W, ('SU3', 'U1'))
    neutral = W.get(('1', 1, Fr(0)), 0)
    print('  %-16s : %s ; neutral Weyl (nu_L, nu^c) = %d -> reduced fields %s' % (cname, 'MATCH' if not bad else 'fails: ' + '; '.join('%s %s' % (name(R), why) for R, m, why in bad[:2]),
          neutral, ('%d' % (neutral//2)) if neutral % 2 == 0 else '%.1f (odd)' % (neutral/2)))
