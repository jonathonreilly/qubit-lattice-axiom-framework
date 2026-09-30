"""Kill check on T42: does second-order generation from P-even licensed terms produce a P-odd operator?
Abelian U(1) model.  H1 = star-pair term sum_v sum_{l<m in star(v)} E_l^out E_m^out  (licensed, proper-covariant sum, P-even),
H2 = sum_P cos(P) (licensed plaquette).  C = i[H1,H2] (leading, symmetrised).  Test: is C invariant under the improper coset?
Also with a P-odd licensed input added (abelian degree-6 star) to show what it takes.
Reuses the atom/group action of the attacker's parity.py (definitions only)."""
import re, itertools
from itertools import product
from collections import defaultdict
src = open('parity.py').read()
head = src.split("o = (0, 0, 0)")[0]
exec(head)      # defines n, unit, add, sub, GROUP, PROPER, IMPROPER, gatom, canon, ...

def plaq_atoms(b, mu, nu):
    # returns list of (link atom, s) with P = sum s*theta
    return [(('E', b, mu), +1), (('E', add(b, unit(mu)), nu), +1), (('E', add(b, unit(nu)), mu), -1), (('E', b, nu), -1)]

W = 2   # window: vertices/plaquette bases in [-W,W]^3
verts = list(product(range(-W, W + 1), repeat=3))
def star_arms(v):
    arms = []
    for mu in range(3):
        arms.append((('E', v, mu), +1))                    # outgoing +mu
        arms.append((('E', sub(v, unit(mu)), mu), -1))     # incoming: E_out = -E_link
    return arms

# operator = dict{(tuple(sorted E atoms), trig) : coeff}, trig = None or ('S'|'C', base, (mu,nu))
def opmul_E_trig(Eatoms, coeff, trig):
    return (tuple(sorted(Eatoms)), trig), coeff

H1 = defaultdict(complex)
for v in verts:
    arms = star_arms(v)
    for (a1, s1), (a2, s2) in itertools.combinations(arms, 2):
        H1[(tuple(sorted([a1, a2])), None)] += s1 * s2
H2 = {}
for b in verts:
    for mu in range(3):
        for nu in range(mu + 1, 3):
            H2[((), ('C', b, (mu, nu)))] = 1.0

def commutator_i(A, B):
    """i[A,B] for A polynomial in E (no trig), B a sum of cos(P): [E_l, cos P] = i s_l sin P  => i*[E_l E_m, cos P] = i*(E_m*i s_l sinP + E_l*i s_m sinP) = -(...)"""
    out = defaultdict(complex)
    for (Es, _), ca in A.items():
        for (_, trig), cb in B.items():
            _, base, (mu, nu) = trig
            pl = {a: s for a, s in plaq_atoms(base, mu, nu)}
            for i, e in enumerate(Es):
                if e in pl:
                    rest = tuple(sorted(Es[:i] + Es[i + 1:]))
                    # [E_e, cosP] = i s sinP ; commutator of product = rest * that
                    out[(rest, ('S', base, (mu, nu)))] += 1j * (1j * pl[e]) * ca * cb   # i * [., .] = i*(i s) = -s
    return {k: v for k, v in out.items() if abs(v) > 1e-12}

def act(g, op):
    out = defaultdict(complex)
    for (Es, trig), c in op.items():
        cc = c; im = []
        for a in Es:
            a2, s = gatom(g, a); cc *= s; im.append(a2)
        if trig is not None:
            a2, s = gatom(g, trig); cc *= s; im.append(a2)
        # translation-quotient: shift so min base is origin for the whole monomial (window-invariant comparison)
        bases = [a[1] for a in im]
        mn = tuple(min(b[i] for b in bases) for i in range(3))
        Es2 = tuple(sorted((a[0], sub(a[1], mn), a[2]) for a in im if a[0] == 'E'))
        tr2 = None
        for a in im:
            if a[0] in 'SC': tr2 = (a[0], sub(a[1], mn), a[2])
        out[(Es2, tr2)] += cc
    return out

def normalise(op):
    """translation-quotient normal form of an operator given in the window"""
    out = defaultdict(complex)
    for (Es, trig), c in op.items():
        atoms = list(Es) + ([trig] if trig else [])
        bases = [a[1] for a in atoms]
        mn = tuple(min(b[i] for b in bases) for i in range(3))
        Es2 = tuple(sorted((a[0], sub(a[1], mn), a[2]) for a in Es))
        tr2 = (trig[0], sub(trig[1], mn), trig[2]) if trig else None
        out[(Es2, tr2)] += c
    return out

def rel_diff(A, B):
    keys = set(A) | set(B)
    return {k: A.get(k, 0) - B.get(k, 0) for k in keys if abs(A.get(k, 0) - B.get(k, 0)) > 1e-9}

C = commutator_i(H1, H2)
Cn = dict(normalise(C))
print("generated operator i[H_star-pair, H_plaq]: number of translation-classes of monomials (window-weighted):", len(Cn))
# restrict to monomials whose E-atoms and plaquette lie deep inside the window to avoid edge effects: use a class-count comparison
def interior_only(op, margin=1):
    out = {}
    for (Es, trig), c in op.items():
        pass
    return op
# Use total weight per translation class, but the window boundary breaks reflection invariance of the *window* only through
# missing partners; to avoid it evaluate reflection on the windowed operator directly and compare only classes with full weight.
maxw = max(abs(v) for v in Cn.values())
full = {k: v for k, v in Cn.items() if abs(abs(v) - maxw) < 1e-9}
print("classes at full (interior) weight:", len(full), " max weight", maxw)
# improper images
diffs = 0
for g in IMPROPER[:6]:
    Rn = dict(normalise(act(g, C)))
    d = rel_diff({k: Cn[k] for k in full}, {k: Rn.get(k, 0) for k in full})
    diffs += len(d)
    print("improper element", g[:2], ": classes differing from original among interior classes:", len(d))
print("=> P-odd content of the second-order generated operator (interior):", "NONE" if diffs == 0 else "present")
# does the generated operator contain the marginal E_z sin(P_xy) with equal-weight (non-gradient) class?
marg = [k for k in full if len(k[0]) == 1 and k[1] is not None]
print("interior classes of the form E * sin(P) (one E, one sin P):", len(marg))
# Are all of them gradient-type i.e. does the sum of coefficients over each y/x/z-mirror-related class vanish?
# reflect each class by the parity element -1 (inversion) and by a mirror y->-y
mir = [g for g in IMPROPER if g[0] == (0, 1, 2) and g[1] == (1, -1, 1)][0]
Cm = dict(normalise(act(mir, C)))
sym = {k: Cn[k] - Cm.get(k, 0) for k in marg}
print("E*sinP classes: max |C - R_y C|:", max(abs(v) for v in sym.values()) if sym else None, " max |C|:", max(abs(Cn[k]) for k in marg))
