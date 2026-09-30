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
for v in [(0,0,0)]:
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
print("per-unit-cell density of i[H_starpair, H_plaq]: translation classes:", len(Cn))
tot = 0
for g in IMPROPER:
    Rn = dict(normalise(act(g, C)))
    d = rel_diff(Cn, Rn)
    tot += len(d)
print("improper elements checked:", len(IMPROPER), " total differing classes over all:", tot)
print("=> second-order generated operator from P-even licensed inputs is P-even" if tot == 0 else "=> P-odd content present")
# is the marginal pseudoscalar E_z sin(P_xy) (one E along the axis normal to the plaquette, no gradient) present?
# Its class representative: E on link (b, normal) with plaquette base b'... check coefficients of classes 'E_normal * sinP' summed over the mirror pair
marg = {k: v for k, v in Cn.items() if len(k[0]) == 1 and k[1] is not None and k[0][0][2] == (3 - k[1][2][0] - k[1][2][1])}
print("classes E_normal * sin(P): ", len(marg), " coefficients:", {k: v for k, v in list(marg.items())[:6]})
print("sum of coefficients over these classes (the non-gradient E.B coefficient):", sum(marg.values()))
print()
for k, v in sorted(Cn.items(), key=lambda kv: str(kv[0])):
    print(v, k)
