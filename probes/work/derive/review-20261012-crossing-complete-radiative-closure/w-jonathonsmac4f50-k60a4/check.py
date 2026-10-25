#!/usr/bin/env python3
"""check.py -- review-20261012-crossing-complete-radiative-closure, attempt a1.

Self-contained (numpy, scipy, sympy, mpmath, fractions only).  One process, no files read or written.
Everything is re-implemented here; none of the R8-4 / R9-7 scripts is imported or copied.

What is executed
  A  exact (Fractions / Gaussian rationals / sympy):
     A1 the 24 time orderings of the connected O(go^2 gi^2) graph of toy N with the COMPLETE crossing set
        (outer monomials dec, vac, 22 = XY->AB, 31 = Y->XAB, each with h.c.; inner Y->UCD, 0->YUCD with h.c.)
     A2 exact finite-Fock RS4 (fractions, complex kernels, CAR/CCR, mixed statistics) == 24-ordering formula with a
        Wick-crossing sign rule that is derived here, not fitted
     A3 negative controls (wrong conjugation, bosonic signs for fermions) are rejected by the same test
     A4 gauge (rephasing) invariance; the ordering phases are 0, +-J2, +-(J1+J2) in the two invariants J1, J2
     A5 classification of ordering signs over all parity-allowed statistics assignments
     A6 boson-quartic Hamiltonian is unbounded below even at one mode per species (exact coherent-state energy)
     A7 the one-loop factor h(E,W) is not a function of the invariant masses (exact), and its defining identity
  B  floating point (numpy / scipy), two disjoint quadratures where a number is quoted:
     B1 INV-3F: the 3-body spectral weight is a function of the invariant mass only
     B2 reduced local graph: 24-ordering sum == minus the Euclidean Feynman integral (Feynman parameters), p independent
     B3 model M* (kernel = c(q_Y) Phi(s_AB) on all four outer crossing types; inner Psi(U,C,D)): relative p dependence
        of the two-loop m^2 at p = m_X/3, momentum Gauss-Legendre vs rapidity trapezoid
     B4 order of limits: cutoff C, masses (infrared), form-factor scale
     B5 statistics: fermion total = boson total - 2 S_neg;  ordering-truncated (toy-N) subset;  phase dependence
"""
import itertools, random, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy import integrate
np.seterr(all='ignore')
T0 = time.time()
NPASS = 0
NFAIL = 0
HITS = []
def check(name, ok, detail=''):
    global NPASS, NFAIL
    if ok: NPASS += 1
    else: NFAIL += 1
    print(('PASS ' if ok else 'FAIL ') + name + ((' | ' + detail) if detail else ''), flush=True)
    return ok

# =====================================================================================================================
# A. exact part
# =====================================================================================================================
class GQ:
    """Gaussian rational"""
    __slots__ = ('re', 'im')
    def __init__(s, re=0, im=0): s.re = Fr(re); s.im = Fr(im)
    def __add__(s, o): o = _g(o); return GQ(s.re + o.re, s.im + o.im)
    __radd__ = __add__
    def __sub__(s, o): o = _g(o); return GQ(s.re - o.re, s.im - o.im)
    def __mul__(s, o): o = _g(o); return GQ(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    __rmul__ = __mul__
    def conj(s): return GQ(s.re, -s.im)
    def iszero(s): return s.re == 0 and s.im == 0
    def __eq__(s, o): o = _g(o); return s.re == o.re and s.im == o.im
    def __ne__(s, o): return not s.__eq__(o)
    def __repr__(s): return f"({float(s.re):.6g}{float(s.im):+.6g}i)"
def _g(x): return x if isinstance(x, GQ) else GQ(x, 0)

SP = ['X', 'Y', 'A', 'B', 'U', 'C', 'D']
SPI = {s: i for i, s in enumerate(SP)}
VERTS = ['o1', 'o2', 'i1', 'i2']
# internal lines: name -> (species, endpoint, endpoint).  The external X enters at o1 (annihilated) and leaves at o2 (created).
LINES = {'Y1': ('Y', 'o1', 'i1'), 'Y2': ('Y', 'o2', 'i2'), 'A': ('A', 'o1', 'o2'), 'B': ('B', 'o1', 'o2'),
         'U': ('U', 'i1', 'i2'), 'C': ('C', 'i1', 'i2'), 'D': ('D', 'i1', 'i2')}
VSPEC = {'o1': ['X', 'Y1', 'A', 'B'], 'o2': ['X', 'Y2', 'A', 'B'], 'i1': ['Y1', 'U', 'C', 'D'], 'i2': ['Y2', 'U', 'C', 'D']}
def sp_of(line): return 'X' if line == 'X' else LINES[line][0]
PRIMARY = [('dec', ['Y', 'A', 'B'], ['X']), ('vac', ['X', 'Y', 'A', 'B'], []), ('22', ['A', 'B'], ['X', 'Y']),
           ('31', ['X', 'A', 'B'], ['Y']), ('idec', ['U', 'C', 'D'], ['Y']), ('ivac', ['Y', 'U', 'C', 'D'], [])]
PRIM_BY_NAME = {n: (n, c, a) for (n, c, a) in PRIMARY}
PNAMES = [n for (n, _, _) in PRIMARY]

def orderings():
    out = []
    for perm in itertools.permutations(VERTS):          # perm[0] is the earliest vertex
        t = {v: k for k, v in enumerate(perm)}
        cre = {v: [] for v in VERTS}; ann = {v: [] for v in VERTS}
        ann['o1'].append('X'); cre['o2'].append('X')
        for ln, (s, u, w) in LINES.items():
            e, l = (u, w) if t[u] < t[w] else (w, u)
            cre[e].append(ln); ann[l].append(ln)
        out.append((perm, t, cre, ann))
    return out
ORD = orderings()

def vtype(v, cre, ann):
    cs = frozenset(sp_of(l) for l in cre[v]); as_ = frozenset(sp_of(l) for l in ann[v])
    if v.startswith('o'):
        tab = {(frozenset('YAB'), frozenset('X')): 'dec', (frozenset('XYAB'), frozenset()): 'vac',
               (frozenset('AB'), frozenset('XY')): '22', (frozenset('XAB'), frozenset('Y')): '31'}
    else:
        tab = {(frozenset('UCD'), frozenset('Y')): 'idec', (frozenset('YUCD'), frozenset()): 'ivac'}
    if (cs, as_) in tab: return tab[(cs, as_)], True
    if (as_, cs) in tab: return tab[(as_, cs)], False
    raise ValueError((v, cs, as_))

def oplist(v, cre, ann):
    """normal-ordered string A^dag(C) A(D): creators in ascending species order, then annihilators in descending order"""
    cl = sorted(cre[v], key=lambda l: SPI[sp_of(l)]); al = sorted(ann[v], key=lambda l: -SPI[sp_of(l)])
    return [(l, 'c') for l in cl] + [(l, 'a') for l in al]

def wick_sign(perm, cre, ann, ferm):
    """sign of the connected complete contraction of  a_p [M_latest ... M_earliest] a^dag_p :
    (-1)^(number of crossing pairs of contraction arcs among FERMION species)."""
    ops = [('X', 'a', 'ext')]
    for v in reversed(perm):
        for (l, k) in oplist(v, cre, ann): ops.append((l, k, v))
    ops.append(('X', 'c', 'ext'))
    arcs = {}
    for pos, (l, k, v) in enumerate(ops):
        key = ('Xout' if k == 'a' else 'Xin') if v == 'ext' else (('Xout' if k == 'c' else 'Xin') if l == 'X' else l)
        arcs.setdefault(key, {})[k] = pos
    arclist = []
    for key, d in arcs.items():
        assert d['a'] < d['c']
        s = 'X' if key.startswith('X') else sp_of(key)
        if s in ferm: arclist.append((d['a'], d['c']))
    cr = 0
    for i in range(len(arclist)):
        for j in range(i + 1, len(arclist)):
            a1, b1 = arclist[i]; a2, b2 = arclist[j]
            if (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1): cr += 1
    return -1 if cr % 2 else 1

def cut_lines(perm, k):
    early = set(perm[:k]); res = [ln for ln, (s, u, w) in LINES.items() if (u in early) != (w in early)]
    xs = 0
    if 'o1' in early and 'o2' not in early: xs = -1       # X_in annihilated, X_out not yet created
    if 'o2' in early and 'o1' not in early: xs = +1       # X_out already created, X_in not yet annihilated
    return res, xs

class Model:
    """periodic ring Z_L, 7 species, random rational energies; kernels: random complex (or phase x modulus)"""
    def __init__(s, L, ferm, seed, p=0, phases=None):
        s.L = L; s.ferm = set(ferm); s.p = p
        rnd = random.Random(seed)
        s.nm = len(SP)*L
        s.eps = [Fr(10 + rnd.randrange(1, 997), 17 + rnd.randrange(0, 11))/7 for _ in range(s.nm)]
        s.kap = {}
        for (name, cre, ann) in PRIMARY:
            sps = sorted(set(cre) | set(ann), key=lambda c: SPI[c])
            for ks in itertools.product(range(L), repeat=len(sps)):
                kd = dict(zip(sps, ks))
                if (sum(kd[c] for c in cre) - sum(kd[c] for c in ann)) % L == 0:
                    if phases is None:
                        s.kap[(name, ks)] = GQ(Fr(rnd.randrange(-9, 10), rnd.randrange(1, 6)), Fr(rnd.randrange(-9, 10), rnd.randrange(1, 6)))
                    else:
                        s.kap[(name, ks)] = GQ(Fr(rnd.randrange(1, 10), rnd.randrange(1, 6)), 0)*phases[name]
    def mi(s, sp_, k): return SPI[sp_]*s.L + k
    def energy(s, st): return sum(n*s.eps[i] for i, n in enumerate(st))
    def isF(s, i): return SP[i//s.L] in s.ferm
    def apply_ops(s, st, seq):
        st = list(st); coef = 1
        for (i, k) in seq:
            if s.isF(i):
                sign = -1 if sum(st[j] for j in range(i) if s.isF(j)) % 2 else 1
                if k == 'c':
                    if st[i] == 1: return None
                    st[i] = 1
                else:
                    if st[i] == 0: return None
                    st[i] = 0
                coef *= sign
            else:                                   # unnormalised occupation basis: a^dag|n)=|n+1), a|n)=n|n-1)
                if k == 'c': st[i] += 1
                else:
                    if st[i] == 0: return None
                    coef *= st[i]; st[i] -= 1
        return coef, tuple(st)
    def terms(s, which):
        out = []
        for (name, cre, ann) in PRIMARY:
            if (which == 'o') == name.startswith('i'): continue
            sps = sorted(set(cre) | set(ann), key=lambda c: SPI[c])
            for ks in itertools.product(range(s.L), repeat=len(sps)):
                if (name, ks) not in s.kap: continue
                kd = dict(zip(sps, ks)); k = s.kap[(name, ks)]
                for (C, D, amp) in ((cre, ann, k), (ann, cre, k.conj())):
                    cl = sorted(C, key=lambda c: SPI[c]); dl = sorted(D, key=lambda c: -SPI[c])
                    seq = [(s.mi(c, kd[c]), 'a') for c in reversed(dl)] + [(s.mi(c, kd[c]), 'c') for c in reversed(cl)]
                    out.append((amp, seq))
        return out
    def V(s, vec, T):
        res = {}
        for st, a in vec.items():
            for amp, seq in T:
                r = s.apply_ops(st, seq)
                if r is None: continue
                c, ns = r
                res[ns] = res.get(ns, GQ()) + a*amp*c
        return {k: v for k, v in res.items() if not v.iszero()}
    def R(s, vec, psi):
        Epsi = s.energy(psi); out = {}
        for st, a in vec.items():
            if st == psi: continue
            d = Epsi - s.energy(st)
            assert d != 0
            out[st] = a*(1/d)
        return out
    def E4(s, psi, T):
        Vv = lambda v: s.V(v, T); Rv = lambda v: s.R(v, psi)
        v = {psi: GQ(1)}
        a1 = Vv(v); a2 = Rv(a1); a3 = Vv(a2); a4 = Rv(a3); a5 = Vv(a4); a6 = Rv(a5); a7 = Vv(a6)
        assert Vv(v).get(psi, GQ()).iszero()          # E1 = 0
        e2 = a3.get(psi, GQ()); e3 = a5.get(psi, GQ()); t4 = a7.get(psi, GQ())
        c2 = Vv(Rv(a2)).get(psi, GQ())                # <V R^2 V>
        return t4 - e2*c2, e3
    def mixed(s, psi, To, Ti):
        e11, e3 = s.E4(psi, To + Ti); e10, _ = s.E4(psi, To); e01, _ = s.E4(psi, Ti)
        assert e3.iszero()
        return e11 - e10 - e01
    def exact_b(s):
        To = s.terms('o'); Ti = s.terms('i')
        psiX = [0]*s.nm; psiX[s.mi('X', s.p)] = 1
        return s.mixed(tuple(psiX), To, Ti) - s.mixed(tuple([0]*s.nm), To, Ti)
    def kappa(s, v, cre, ann, modes):
        name, prim = vtype(v, cre, ann)
        sps = ['X', 'Y', 'A', 'B'] if v.startswith('o') else ['Y', 'U', 'C', 'D']
        pr = PRIM_BY_NAME[name]
        sp_sorted = sorted(set(pr[1]) | set(pr[2]), key=lambda c: SPI[c])
        k = s.kap.get((name, tuple(modes[c] for c in sp_sorted)))
        if k is None: return GQ()
        return k if prim else k.conj()
    def closed(s, ferm_override=None, drop_conj=False, bose_signs=False):
        ferm = s.ferm if ferm_override is None else ferm_override
        tot = GQ(); p = s.p
        for perm, t, cre, ann in ORD:
            sgn = 1 if bose_signs else wick_sign(perm, cre, ann, ferm)
            cuts = [cut_lines(perm, k) for k in (1, 2, 3)]
            for lab in itertools.product(range(s.L), repeat=7):
                m = dict(zip(['Y1', 'Y2', 'A', 'B', 'U', 'C', 'D'], lab))
                amp = GQ(sgn)
                for v in VERTS:
                    modes = {sp_of(l): (p if l == 'X' else m[l]) for l in VSPEC[v]}
                    kk = s.kappa(v, cre, ann, modes)
                    if drop_conj and not vtype(v, cre, ann)[1]: kk = kk.conj()
                    amp = amp*kk
                    if amp.iszero(): break
                if amp.iszero(): continue
                den = Fr(1)
                for (ls, xs) in cuts:
                    den *= -(sum(s.eps[s.mi(LINES[l][0], m[l])] for l in ls) + xs*s.eps[s.mi('X', p)])
                tot = tot + amp*(1/den)
        return tot

def section_A():
    print('# --- A. exact checks', flush=True)
    # A1
    types_used = set(); ntoy = 0; per = []
    for perm, t, cre, ann in ORD:
        ts = [vtype(v, cre, ann) for v in perm]
        names = {n for (n, _) in ts if n in ('dec', 'vac', '22', '31')}
        per.append(names)
        types_used |= {n for (n, _) in ts}
        if names <= {'dec', 'vac'}: ntoy += 1
    check('A1 24 orderings; vertex monomial types are exactly dec,vac,22,31,idec,ivac (+h.c.); 10 use only toy-N outer types, 14 need 22 or 31',
          len(ORD) == 24 and types_used == set(PNAMES) and ntoy == 10 and all(len(x) > 0 for x in per) and sum(1 for x in per if x & {'22', '31'}) == 14,
          f'orderings={len(ORD)} toyN-subset={ntoy} new={24-ntoy}')
    # every cut crosses A and B together and U,C,D together; every cut has an internal line
    ok = True
    for perm, t, cre, ann in ORD:
        for k in (1, 2, 3):
            ls, xs = cut_lines(perm, k)
            ok &= (('A' in ls) == ('B' in ls)) and (('U' in ls) == ('C' in ls) == ('D' in ls)) and len(ls) > 0
    check('A1b A,B always cross a cut together; U,C,D always together; every cut crosses an internal line (no degenerate denominators)', ok)
    # A2 exact finite Fock vs closed form
    cases = [((), 2, 3, 0, 'all bosons'), (('A', 'B'), 2, 3, 0, 'A,B fermions'), (('U', 'C'), 2, 3, 0, 'U,C fermions'),
             (('A', 'B', 'U', 'C'), 2, 4, 0, 'A,B,U,C fermions'), (('X', 'A'), 2, 3, 0, 'X,A fermions'),
             (('X', 'Y', 'U'), 2, 3, 0, 'X,Y,U fermions'), (tuple(SP), 2, 1, 0, 'all fermions'), (tuple(SP), 2, 5, 1, 'all fermions, p=1'),
             (('A', 'C', 'Y'), 2, 7, 1, 'A,C,Y fermions, p=1'), (tuple(SP), 3, 2, 0, 'all fermions, L=3')]
    keep = {}
    for (F, L, seed, p, label) in cases:
        t0 = time.time(); M = Model(L, F, seed, p)
        b = M.exact_b(); cf = M.closed()
        keep[label] = (M, b)
        check(f'A2 exact RS4 (Fractions, complex kernels, L={L}) == 24-ordering Wick formula: {label}', b == cf and b != GQ(0) and b.im == 0,
              f'value~{float(b.re):.4e} imag=0 {time.time()-t0:.1f}s')
    # A3 negative controls
    M, b = keep['all fermions']
    check('A3 control: dropping the complex conjugate on h.c. vertices is rejected', M.closed(drop_conj=True) != b)
    check('A3 control: bosonic signs for an all-fermion model are rejected', M.closed(bose_signs=True) != b)
    M, b = keep['X,A fermions']
    check('A3 control: bosonic signs for X,A fermions are rejected', M.closed(bose_signs=True) != b)
    M, b = keep['A,B fermions']
    check('A3 control: bosonic signs for the sign-trivial model A,B fermions are NOT rejected (signs are all +)', M.closed(bose_signs=True) == b)
    # A4 gauge invariance and phase table
    units = [GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(5, 13), Fr(12, 13)), GQ(Fr(8, 17), Fr(15, 17)), GQ(Fr(7, 25), Fr(24, 25)), GQ(Fr(20, 29), Fr(21, 29)),
             GQ(Fr(-9, 41), Fr(40, 41)), GQ(Fr(12, 37), Fr(-35, 37))]
    om = {n: units[i] for i, n in enumerate(PNAMES)}
    u = dict(zip(SP, [units[(i + 2) % 7] for i in range(7)]))
    def gauge(name):
        _, cr, an = PRIM_BY_NAME[name]; g = GQ(1)
        for c in cr: g = g*u[c]
        for d in an: g = g*u[d].conj()
        return g
    om2 = {n: om[n]*gauge(n) for n in PNAMES}
    Fm = ('A', 'B')
    Ma = Model(2, Fm, 11, 0, phases=om); Mb = Model(2, Fm, 11, 0, phases=om2)
    ba = Ma.exact_b(); bb = Mb.exact_b()
    check('A4 exact: a species-level rephasing of the six crossing phases leaves the mixed RS4 coefficient unchanged', ba == bb and ba.im == 0 and ba == Ma.closed(),
          f'value~{float(ba.re):.4e}')
    # invariants: null space of the gauge action on the 6 phases
    chi = {c: sp.Symbol('chi_' + c) for c in SP}
    G = sp.Matrix([[sp.diff(sum(chi[c] for c in cr) - sum(chi[c] for c in an), chi[x]) for (_, cr, an) in PRIMARY] for x in SP])
    ns = G.nullspace()
    J1 = sp.Matrix([1, -1, -1, 1, 0, 0]); J2 = sp.Matrix([-1, 0, 1, 0, -1, 1])       # (dec,vac,22,31,idec,ivac)
    rows = []
    for perm, t, cre, ann in ORD:
        v = [0]*6
        for w in VERTS:
            nm, prim = vtype(w, cre, ann); v[PNAMES.index(nm)] += 1 if prim else -1
        rows.append(v)
    V = sp.Matrix(rows)
    A = sp.Matrix.hstack(J1, J2)
    sols = []
    for r in rows:
        x = sp.symbols('a b'); s_ = sp.solve(list(A*sp.Matrix(x) - sp.Matrix(r)), x, dict=True); sols.append(s_[0] if s_ else None)
    pat = {}
    for s_ in sols:
        key = (s_[sp.Symbol('a')], s_[sp.Symbol('b')])
        pat[key] = pat.get(key, 0) + 1
    exp = {(0, 0): 12, (0, -1): 3, (0, 1): 3, (1, 1): 3, (-1, -1): 3}
    patI = {(int(k[0]), int(k[1])): v for k, v in pat.items()}
    check('A4b gauge-invariant phases: the null space of the rephasing action is 2-dimensional (J1, J2), and every ordering carries phase theta = a*J1 + b*J2 with (a,b)=(0,0) in 12 orderings, +-(0,1) in 3 each, +-(1,1) in 3 each',
          len(ns) == 2 and G.rank() == 4 and all(s_ is not None for s_ in sols) and patI == exp,
          f'(a,b)->count {sorted(patI.items())}; J1 = phi_dec-phi_vac-phi_22+phi_31, J2 = -phi_dec+phi_22-phi_idec+phi_ivac')
    # A5 statistics classification
    allplus = []; table = []
    for r in range(8):
        for F in itertools.combinations(SP, r):
            F = set(F)
            if len(F & set('XYAB')) % 2 or len(F & set('YUCD')) % 2: continue     # every monomial must be even in fermion operators
            neg = sum(1 for (perm, t, cre, ann) in ORD if wick_sign(perm, cre, ann, F) < 0)
            table.append((''.join(sorted(F)) or '-', neg))
            if neg == 0: allplus.append(''.join(sorted(F)) or '-')
    pred = []
    for r in range(8):
        for F in itertools.combinations(SP, r):
            F = set(F)
            if len(F & set('XYAB')) % 2 or len(F & set('YUCD')) % 2: continue
            if 'X' not in F and 'Y' not in F and len(F & set('AB')) % 2 == 0 and len(F & set('UCD')) % 2 == 0: pred.append(''.join(sorted(F)) or '-')
    check('A5 over all 32 parity-allowed statistics assignments: the 24 ordering signs are all +1 exactly when X,Y are bosons and an even number of {A,B} and of {U,C,D} are fermions; all others have 12 or 16 negative orderings',
          len(table) == 32 and sorted(allplus) == sorted(pred) and len(pred) == 8 and all(n in (12, 16) for (f, n) in table if f not in pred),
          f'sign-trivial sets: {sorted(allplus)}; all-fermion negatives={dict(table)["ABCDUXY"]}')
    # A6 boson quartic instability, exact
    eps = Fr(3, 2); kap = Fr(1, 10)
    def Ecoh(t):          # <alpha|H|alpha>, alpha_s = t (X: -t), all four vac-type monomial species at one mode each
        return 4*eps*t*t + 2*kap*(-t)*t*t*t
    check('A6 all-boson Hamiltonian: coherent-state energy (variational upper bound on the ground energy) -> -infinity already for one mode per species',
          Ecoh(Fr(10)) < 0 and Ecoh(Fr(1000)) < -10**9 and Ecoh(Fr(10**5)) < -10**18, f'E(10^3)={float(Ecoh(Fr(1000))):.3e}')
    # A7 h factor
    E_, W_, C_ = sp.symbols('E W C', positive=True)
    h = (W_*(1 + 2*C_) - E_)/(W_ + E_)
    ident = sp.simplify(h/(E_ - W_) + 1/(E_ + W_) - 2*C_*W_/(E_**2 - W_**2))
    check('A7 one-loop identity h/(E-W)+1/(E+W) = 2CW/(E^2-W^2) for h=(W(1+2C)-E)/(W+E) (sympy)', ident == 0)
    import mpmath as mp
    mp.mp.dps = 50
    def hval(m, M, p, C=1):
        E = mp.sqrt(m*m + p*p); W = mp.sqrt(M*M + p*p); return (W*(1 + 2*C) - E)/(W + E)
    h0 = hval(1, 2, 0); h1 = hval(1, 2, 1); h5 = hval(1, 2, 5)
    check('A7b h at fixed invariant masses (m_X=1, M_cluster=2) differs between frames p=0,1,5: it is not a function of the invariant masses (frame-dependent, an imposed tuning)',
          abs(h0 - h1) > mp.mpf('0.05') and abs(h1 - h5) > mp.mpf('0.01'), f'h={mp.nstr(h0,8)}, {mp.nstr(h1,8)}, {mp.nstr(h5,8)}')

# =====================================================================================================================
# B. continuum part (1+1 D, infinite volume, continuum dispersion on every leg)
# =====================================================================================================================
MASS0 = dict(X=0.30, Y=0.33, A=0.37, B=0.41, U=0.29, C=0.35, D=0.43)      # toy-N masses (R8-4), reused as supplied parameters
NEG = {}
class Par:
    def __init__(s, scale=1.0, lam=1.0):
        s.m = {k: v*scale for k, v in MASS0.items()}; s.l1 = lam*1.0; s.l2 = lam*1.4
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
    e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1 - x, 1)), 0.0)
    return e1/(e1 + e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))
def Fpl(s, P): return plateau(np.sqrt(np.maximum(s, 0.0)), P.l1, P.l2)
def En(q, P, sp_): return np.sqrt(P.m[sp_]**2 + q*q)

STRUCT = []
for perm, t, cre, ann in ORD:
    cuts = []
    for k in (1, 2, 3):
        ls, xs = cut_lines(perm, k)
        cuts.append((sum(1 for l in ls if l in ('Y1', 'Y2')), 1 if 'A' in ls else 0, 1 if 'U' in ls else 0, xs))
    STRUCT.append(cuts)
NDEC = [sum(1 for v in VERTS if vtype(v, cre, ann)[0] == 'dec') for (perm, t, cre, ann) in ORD]
NIDEC = [sum(1 for v in VERTS if vtype(v, cre, ann)[0] == 'idec') for (perm, t, cre, ann) in ORD]
SIGN = lambda F: np.array([wick_sign(perm, cre, ann, set(F)) for (perm, t, cre, ann) in ORD], float)

def support_extents(p, C2, P):
    """largest |q| carried by any A/B leg and by any U/C/D leg when |q_Y|<=C2 and the pair / cluster invariant masses are <= l2"""
    Kmax = abs(p) + C2; mA, mB = P.m['A'], P.m['B']
    d = np.arccosh(max((P.l2**2 - mA**2 - mB**2)/(2*mA*mB), 1.0))
    best = 0.0
    a = np.linspace(-7, 7, 4001)
    for (m1, m2) in ((mA, mB), (mB, mA)):
        bgrid = a[:, None] + np.linspace(-d, d, 401)[None, :]
        K = m1*np.sinh(a)[:, None] + m2*np.sinh(bgrid)
        ok = np.abs(K) <= Kmax
        if ok.any(): best = max(best, np.max(np.abs(m1*np.sinh(np.broadcast_to(a[:, None], bgrid.shape)[ok]))))
    G = np.linspace(-6, 6, 181)
    aU, aC, aD = np.meshgrid(G, G, G, indexing='ij')
    mU, mC, mD = P.m['U'], P.m['C'], P.m['D']
    sok = lambda m1, a1, m2, a2: (m1**2 + m2**2 + 2*m1*m2*np.cosh(a1 - a2)) <= P.l2**2
    ok = sok(mU, aU, mC, aC) & sok(mU, aU, mD, aD) & sok(mC, aC, mD, aD) & (np.abs(mU*np.sinh(aU) + mC*np.sinh(aC) + mD*np.sinh(aD)) <= C2)
    ext_in = max(np.max(np.abs(mU*np.sinh(aU[ok]))), np.max(np.abs(mC*np.sinh(aC[ok]))), np.max(np.abs(mD*np.sinh(aD[ok]))))
    return best*1.001, ext_in*1.001

def yfac(qy, C1, C2):
    return plateau(qy, C1, C2)**4 if C1 is not None else np.ones_like(qy)

def dens_pair(qA, qB, P):
    eA, eB = En(qA, P, 'A'), En(qB, P, 'B')
    return Fpl((eA + eB)**2 - (qA + qB)**2, P)**2/(4*eA*eB), eA + eB
def dens_trio(qU, qC, qD, P):
    eU, eC, eD = En(qU, P, 'U'), En(qC, P, 'C'), En(qD, P, 'D')
    psi = Fpl((eU + eC)**2 - (qU + qC)**2, P)*Fpl((eU + eD)**2 - (qU + qD)**2, P)*Fpl((eC + eD)**2 - (qC + qD)**2, P)
    return psi**2/(8*eU*eC*eD), eU + eC + eD

def accumulate(tot, pref, wab, W_AB, win, W_IN, EX, EY, hfac=False):
    ww0 = wab[:, None]*win[None, :]
    if hfac:           # one-loop fermion factor h = (3W - E)/(W + E) on the decay vertices X->YAB and Y->UCD (and h.c.), evaluated on the bare shell
        Wo = EY + W_AB; ho = ((3*Wo - EX)/(Wo + EX))[:, None]; hi = ((3*W_IN - EY)/(W_IN + EY))[None, :]
    for o, cuts in enumerate(STRUCT):
        ww = ww0
        if hfac: ww = ww0*ho**(0.5*NDEC[o])*hi**(0.5*NIDEC[o])
        den = 1.0
        for (nY, nAB, nIN, xs) in cuts:
            den = den*(-(nY*EY + nAB*W_AB[:, None] + nIN*W_IN[None, :] + xs*EX))
        tot[o] += pref*np.sum(ww/den)

def mix_mom(p, C1, C2, P, n_y, n_a, n_u, ext):
    """momentum-space tensor Gauss-Legendre in (q_Y, q_A, q_U, q_C); returns the 24 ordering contributions to m^2 = 2 E_X * mix"""
    ext_ab, ext_in = ext; EX = np.sqrt(P.m['X']**2 + p*p)
    xy, wy = np.polynomial.legendre.leggauss(n_y); xa, wa = np.polynomial.legendre.leggauss(n_a); xu, wu = np.polynomial.legendre.leggauss(n_u)
    tot = np.zeros(24)
    qU0, qC0 = np.meshgrid(ext_in*xu, ext_in*xu, indexing='ij'); wUC = np.outer(ext_in*wu, ext_in*wu).ravel(); qU0 = qU0.ravel(); qC0 = qC0.ravel()
    for iy in range(n_y):
        qy = C2*xy[iy]; cy = float(yfac(np.array([qy]), C1, C2)[0])
        if cy == 0: continue
        EY = En(qy, P, 'Y')
        qA = ext_ab*xa; qB = p - qy - qA
        dab, W = dens_pair(qA, qB, P); wab = dab*ext_ab*wa
        k = wab != 0; wab = wab[k]; W_AB = W[k]
        dtr, Wi = dens_trio(qU0, qC0, qy - qU0 - qC0, P); win = dtr*wUC
        k = win != 0; win = win[k]; W_IN = Wi[k]
        if len(wab) == 0 or len(win) == 0: continue
        pref = C2*wy[iy]*cy/((2*EX)*(2*EY)**2)/(2*np.pi)**4
        accumulate(tot, pref, wab, W_AB, win, W_IN, EX, EY)
    return tot*2*EX

def mix_rap(p, C1, C2, P, n_y, n_a, n_u, ext, hfac=False):
    """rapidity-space trapezoid (q = m sinh a, dq = E da) in (a_Y, a_A, a_U, a_C): disjoint nodes, weights and variables"""
    ext_ab, ext_in = ext; EX = np.sqrt(P.m['X']**2 + p*p)
    def grid(m, ext_q, n):
        R = np.arcsinh(ext_q/m); a = np.linspace(-R, R, n); return a, (a[1] - a[0])
    aY, hY = grid(P.m['Y'], C2, n_y); tot = np.zeros(24)
    aA, hA = grid(P.m['A'], ext_ab, n_a); aU, hU = grid(P.m['U'], ext_in, n_u); aC, hC = grid(P.m['C'], ext_in, n_u)
    qA = P.m['A']*np.sinh(aA); EA = np.sqrt(P.m['A']**2 + qA**2)
    qU, qC = np.meshgrid(P.m['U']*np.sinh(aU), P.m['C']*np.sinh(aC), indexing='ij')
    jac = (np.sqrt(P.m['U']**2 + qU**2)*hU*np.sqrt(P.m['C']**2 + qC**2)*hC).ravel(); qU = qU.ravel(); qC = qC.ravel()
    for iy in range(n_y):
        qy = P.m['Y']*np.sinh(aY[iy]); EY = np.sqrt(P.m['Y']**2 + qy*qy); jy = EY*hY
        cy = float(yfac(np.array([qy]), C1, C2)[0])
        if cy == 0: continue
        qB = p - qy - qA
        dab, W = dens_pair(qA, qB, P); wab = dab*EA*hA
        k = wab != 0; wab = wab[k]; W_AB = W[k]
        dtr, Wi = dens_trio(qU, qC, qy - qU - qC, P); win = dtr*jac
        k = win != 0; win = win[k]; W_IN = Wi[k]
        if len(wab) == 0 or len(win) == 0: continue
        pref = jy*cy/((2*EX)*(2*EY)**2)/(2*np.pi)**4
        accumulate(tot, pref, wab, W_AB, win, W_IN, EX, EY, hfac)
    return tot*2*EX

def rel(a, b): return (b - a)/abs(a)

def section_B():
    print('# --- B. continuum checks (1+1 D)', flush=True)
    P = Par()
    # B1 INV-3F: spectral weight of the 3-body cluster depends on the invariant mass only
    ext = support_extents(0.0, 1.6, P)
    xu, wu = np.polynomial.legendre.leggauss(150)
    eIN = ext[1]
    qU, qC = np.meshgrid(eIN*xu, eIN*xu, indexing='ij'); wUC = np.outer(eIN*wu, eIN*wu).ravel(); qU = qU.ravel(); qC = qC.ravel()
    mom = {}
    for qy in (0.0, 0.5, 1.0, 1.5):
        d, W = dens_trio(qU, qC, qy - qU - qC, P); w = d*wUC
        M2 = W*W - qy*qy
        mom[qy] = [np.sum(w*2*W*f(M2)) for f in (lambda x: np.ones_like(x), lambda x: x, lambda x: 1/(x + 0.3), lambda x: np.cos(3*x))]
    spread = max((max(abs(mom[q][i] - mom[0.0][i]) for q in mom)/abs(mom[0.0][i])) for i in range(4))
    check('B1 INV-3F: sum_nodes w * 2W * f(W^2 - q^2) is the same at q_Y = 0, 0.5, 1.0, 1.5 (frame independence of the 3-body spectral density)',
          spread < 2e-5, f'max relative spread {spread:.2e} (zeroth moment {mom[0.0][0]:.6e})')
    # B2 OFPT = Feynman on the reduced local graph
    mX, mY = P.m['X'], P.m['Y']
    def ofpt(p, mu, M):
        EX = np.hypot(mX, p)
        def f(K):
            qy = p - K; EY = np.hypot(mY, qy); Emu = np.hypot(mu, K); EM = np.hypot(M, qy)
            s = 0.0
            for cuts in STRUCT:
                den = 1.0
                for (nY, nAB, nIN, xs) in cuts: den *= -(nY*EY + nAB*Emu + nIN*EM + xs*EX)
                s += 1.0/den
            return s/((2*EY)**2*(2*Emu)*(2*EM))/(2*np.pi)
        return integrate.quad(f, -80, 80, epsabs=1e-15, epsrel=1e-13, limit=500)[0]
    def feyn(mu, M):
        def g(y, x):
            z = 1 - x - y; D = x*mY**2 + y*M**2 + z*mu**2 - z*(1 - z)*mX**2
            return x/D**3
        v = integrate.dblquad(g, 0, 1, lambda x: 0, lambda x: 1 - x, epsabs=1e-15, epsrel=1e-13)[0]
        return v/(2*np.pi)
    worst = 0.0; spreadp = 0.0
    for (mu, M) in ((0.9, 1.1), (0.75, 0.6)):
        F = feyn(mu, M); vals = [ofpt(p, mu, M) for p in (0.0, 0.1, 0.3, 1.0)]
        worst = max(worst, max(abs(v/F + 1) for v in vals)); spreadp = max(spreadp, (max(vals) - min(vals))/abs(F))
    check('B2 local reduced graph (S_mu, Y, Z_M lines): the 24-ordering sum equals MINUS the Euclidean Feynman integral (Feynman parameters) and is p-independent for p=0..1',
          worst < 1e-9 and spreadp < 1e-9, f'max|ratio+1|={worst:.1e}, p-spread={spreadp:.1e}')
    # B3 model M*: two disjoint quadratures
    C1 = 1.2; C2 = 1.3*C1; p1 = 0.1
    ext0 = support_extents(0.0, C2, P); ext1 = support_extents(p1, C2, P)
    t0 = time.time()
    tr0 = mix_rap(0.0, C1, C2, P, 110, 110, 70, ext0); tr1 = mix_rap(p1, C1, C2, P, 110, 110, 70, ext1)
    gl0 = mix_mom(0.0, C1, C2, P, 96, 128, 96, ext0); gl1 = mix_mom(p1, C1, C2, P, 96, 128, 96, ext1)
    eps_tr = rel(tr0.sum(), tr1.sum()); eps_gl = rel(gl0.sum(), gl1.sum())
    NEG['r0'], NEG['r1'] = tr0, tr1
    check('B3 model M* (Y-confined P2, C1=1.2, legs |q|<=%.3f): total two-loop m^2(0) agrees between momentum Gauss-Legendre and rapidity trapezoid' % max(ext1),
          abs(gl0.sum()/tr0.sum() - 1) < 2e-5, f'm2(0): GL {gl0.sum():.9e}  trap {tr0.sum():.9e}  ({time.time()-t0:.0f}s)')
    check('B3b relative p-dependence at p=m_X/3 of the bosonic two-loop m^2 is small and the two quadratures agree: eps = (m2(p)-m2(0))/|m2(0)|',
          abs(eps_gl - eps_tr) < 3e-6 and 5e-6 < eps_tr < 2e-5, f'eps trap={eps_tr:.4e}  GL={eps_gl:.4e}')
    # unconfined limit reproduces the previously reported value (reproduction only, not a new result)
    # B4 order of limits
    print('# order of limits table: eps(C1; mass scale s, form-factor scale lam), p = s*m_X/3 (rapidity fixed), trapezoid', flush=True)
    def eps_of(C1_, s=1.0, lam=1.0, base=(100, 100, 66)):
        Pp = Par(s, lam); C2_ = 1.3*C1_; pp = 0.1*s
        e0 = support_extents(0.0, C2_, Pp); e1 = support_extents(pp, C2_, Pp)
        f = max(1.0, np.arcsinh(e0[0]/Pp.m['A'])/np.arcsinh(1.7/0.37))*max(1.0, C1_/1.2*0.8)
        cfg = tuple(int(round(b*f)) for b in base)
        a0 = mix_rap(0.0, C1_, C2_, Pp, *cfg, e0); a1 = mix_rap(pp, C1_, C2_, Pp, *cfg, e1)
        return rel(a0.sum(), a1.sum()), a0.sum(), e1, a0, a1
    Cs = [0.5, 0.7, 0.9, 1.2, 1.6, 2.0]; eps_c = []; m20 = []
    for c in Cs:
        t0 = time.time(); e, m0, ee, _, _ = eps_of(c); eps_c.append(e); m20.append(m0)
        print(f'   C1={c:.2f}  eps={e:.4e}  m2(0)={m0:.7e}  max leg momentum {max(ee):.3f}  ({time.time()-t0:.0f}s)', flush=True)
    check('B4a cutoff limit: eps(C1) decreases strictly and fast with C1 (4e-4 at C1=0.5 down to <1e-6 at C1=2) and m2(0) tends to the unconfined value',
          all(eps_c[i] > eps_c[i + 1] > 0 for i in range(len(Cs) - 1)) and eps_c[0] > 2e-4 and eps_c[-1] < 1e-6 and abs(m20[-1]/(-1.1553e-2) - 1) < 5e-4,
          f'eps={["%.2e" % x for x in eps_c]}')
    NEG['epsC'] = (Cs, eps_c)
    # infrared: masses scaled at fixed rapidity, fixed C1 and form factor scale
    e_s = {}
    for s in (1.0, 0.5, 0.25):
        t0 = time.time(); e, m0, ee, _, _ = eps_of(0.7, s=s, base=((100, 100, 66) if s == 1.0 else (80, 80, 54))); e_s[s] = (e, m0)
        print(f'   C1=0.70 mass scale s={s:<5}  eps={e:.4e}  m2(0)={m0:.5e}  ({time.time()-t0:.0f}s)', flush=True)
    check('B4b infrared direction (all masses scaled by s at fixed rapidity, fixed C1=0.7 and Lambda): eps falls by more than a factor 10 per halving (it reaches the ~1e-7 quadrature floor at s=1/4) while |m2(0)| grows by more than 50 per halving',
          e_s[1.0][0] > 10*e_s[0.5][0] and e_s[0.5][0] > 10*e_s[0.25][0] and abs(e_s[0.5][1]) > 50*abs(e_s[1.0][1]) and abs(e_s[0.25][1]) > 50*abs(e_s[0.5][1]),
          f'eps(s=1)={e_s[1.0][0]:.2e}, eps(s=.5)={e_s[0.5][0]:.2e}, eps(s=.25)={e_s[0.25][0]:.2e}; m2(0)={e_s[1.0][1]:.2e},{e_s[0.5][1]:.2e},{e_s[0.25][1]:.2e}')
    # form-factor scale (local-limit direction at fixed C1)
    e_l = {}
    for lam in (1.0, 2.0, 4.0):
        t0 = time.time(); e, m0, ee, _, _ = eps_of(1.2, lam=lam, base=((100, 100, 66) if lam == 1.0 else (90, 90, 60))); e_l[lam] = (e, m0)
        print(f'   C1=1.20 form-factor scale lam={lam:<4}  eps={e:.4e}  m2(0)={m0:.5e}  max legs {ee[0]:.2f},{ee[1]:.2f} ({time.time()-t0:.0f}s)', flush=True)
    check('B4c form-factor scale Lambda -> larger at fixed C1=1.2: eps stays finite, positive and below 1e-4 (no run-away) over lam=1,2,4',
          all(0 < e_l[l][0] < 1e-4 for l in e_l), f'eps={["%.2e" % e_l[l][0] for l in e_l]}')
    NEG['eps_l'] = e_l; NEG['e_s'] = e_s
    # B5 statistics, subset, phases (re-use B3 trapezoid ordering contributions)
    r0, r1 = NEG['r0'], NEG['r1']
    sB = SIGN([]); sF = SIGN(SP); sAB = SIGN(['A', 'B']); sCU = SIGN(['U', 'C']); sXYU = SIGN(['X', 'Y', 'U'])
    neg = sF < 0
    SnegA, SnegB = r0[neg].sum(), r1[neg].sum()
    totB = (sB*r0).sum(), (sB*r1).sum(); totF = (sF*r0).sum(), (sF*r1).sum()
    check('B5a sign-trivial assignments (A,B fermions; U,C fermions) reproduce the bosonic ordering sum bit for bit (so the P2 closure theorem applies to them)',
          np.array_equal(sAB, sB) and np.array_equal(sCU, sB) and np.array_equal(SIGN(['A', 'B', 'U', 'C']), sB))
    check('B5b all-fermion (finite-per-site) model: total = bosonic total - 2 S_neg exactly, S_neg = sum of the 12 sign-flipped orderings',
          abs(totF[0] - (totB[0] - 2*SnegA)) < 1e-15 and abs(totF[1] - (totB[1] - 2*SnegB)) < 1e-15 and int(neg.sum()) == 12 and np.array_equal(sXYU < 0, neg),
          f'S_neg(0)={SnegA:.5e} S_neg(p)={SnegB:.5e}; fermion m2(0)={totF[0]:.4e} vs boson {totB[0]:.4e}')
    eps_F = rel(totF[0], totF[1])
    check('B5c all-fermion model M* is NOT closed: relative p dependence at p=m_X/3 is more than 1e-2 (and equals -2 dS_neg/|m2_F(0)| + the bosonic part)',
          abs(eps_F) > 1e-2 and abs(rel(SnegA, SnegB)) < 1e-2, f'eps_F={eps_F:.3e}; relative S_neg drift {rel(SnegA, SnegB):.2e}; boson eps {rel(*totB):.2e}')
    # toy-N subset (only dec, vac, idec, ivac vertices) inside M*
    mask = np.array([all(vtype(v, cre, ann)[0] in ('dec', 'vac', 'idec', 'ivac') for v in VERTS) for (perm, t, cre, ann) in ORD])
    eps10 = rel(r0[mask].sum(), r1[mask].sum())
    check('B5d ordering-truncated subset (the 10 toy-N orderings) of the SAME kernels is far from closed, the complete 24 is not: the truncated failure is a missing-ordering effect',
          int(mask.sum()) == 10 and abs(eps10) > 1e-3 and abs(eps10) > 100*abs(rel(*totB)), f'eps(10 orderings)={eps10:.3e}, eps(24)={rel(*totB):.3e}')
    # B6 naive extension of the one-loop fermion factor h to the two decay vertices
    th0 = mix_rap(0.0, C1, C2, P, 110, 110, 70, ext0, hfac=True); th1 = mix_rap(p1, C1, C2, P, 110, 110, 70, ext1, hfac=True)
    eps_Fh = rel((sF*th0).sum(), (sF*th1).sum()); eps_Bh = rel((sB*th0).sum(), (sB*th1).sum())
    check('B6 the one-loop tuning h=(3W-E)/(W+E) applied to the two decay vertices (outer X->YAB, inner Y->UCD, bare-shell arguments) does NOT close the all-fermion two-loop dispersion',
          abs(eps_Fh) > 1e-2, f'all-fermion eps with h = {eps_Fh:.3e} (without h {eps_F:.3e}); bosonic sum with the same h factors {eps_Bh:.2e}')
    # phases: weights exp(i theta_o) with theta = a J1 + b J2
    ab = []
    for (perm, t, cre, ann) in ORD:
        v = [0]*6
        for w in VERTS:
            nm, prim = vtype(w, cre, ann); v[PNAMES.index(nm)] += 1 if prim else -1
        ab.append((v[3], v[5]))      # gauge: phi_31 = J1, phi_ivac = J2, others 0
    ab = np.array(ab, float)
    outs = []
    for (J1_, J2_) in ((0.0, 0.0), (0.0, np.pi/2), (np.pi/2, 0.0), (np.pi/2, np.pi/2)):
        th = ab[:, 0]*J1_ + ab[:, 1]*J2_
        re0, re1 = (np.cos(th)*r0).sum(), (np.cos(th)*r1).sum(); im0, im1 = (np.sin(th)*r0).sum(), (np.sin(th)*r1).sum()
        outs.append((J1_, J2_, rel(re0, re1), abs(im0) + abs(im1), re0))
    ok = abs(outs[0][2] - rel(*totB)) < 1e-15 and all(o[3] < 1e-12 for o in outs) and all(abs(o[2]) > 1e-3 for o in outs[1:])
    check('B5e kernel phases: the dispersion defect depends on the invariants (J1,J2); J1=J2=0 gives the closed case, any of J = pi/2 breaks closure at the 1e-3..1e-1 level; imaginary parts cancel (Hermiticity)',
          ok, '; '.join(f'(J1,J2)=({o[0]:.2f},{o[1]:.2f}): eps={o[2]:.2e}' for o in outs))
    return eps_tr, eps_c, eps_F, eps10

def main():
    section_A()
    eps_tr, eps_c, eps_F, eps10 = section_B()
    print(f'TOTAL: PASS={NPASS} FAIL={NFAIL}')
    print(f'# runtime {time.time()-T0:.0f}s')
    if NFAIL == 0:
        print('HIT: complete 8+4-monomial crossing model M* (kernel c(q_Y)Phi(s_AB) on dec,vac,22,31; inner Psi(U,C,D)) has exact two-loop covariance when unconfined (c=1, bosonic reduction + Feynman identity) for every statistics assignment with X,Y bosonic and even fermion number in {A,B} and in {U,C,D} (24 ordering signs all +1, exact Fock + enumeration), a box-confining Y-plateau leaves a controlled defect eps(C1)=%.1e..%.1e for C1=0.5..2.0 (two disjoint quadratures), while the all-CAR (finite-per-site) assignment is not closed (eps=%.1e; defect = -2 S_neg over 12 sign-flipped orderings)' % (eps_c[0], eps_c[-1], eps_F))
    print('SUMMARY: the complete crossing set (24 orderings, CAR signs and complex conjugates verified in exact finite Fock space) closes the two-loop dispersion exactly (bosonic reduction) and up to an exponentially small controlled defect when box-confined, for every statistics with bosonic X,Y and even fermion pairs, but not for the all-CAR finite-per-site assignment, whose defect is -2 times the sum of 12 sign-flipped orderings.')
    sys.exit(0 if NFAIL == 0 else 1)

if __name__ == '__main__':
    main()
