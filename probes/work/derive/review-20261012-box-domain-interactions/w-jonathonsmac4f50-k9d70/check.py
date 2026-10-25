#!/usr/bin/env python3
"""
check.py for J:derive:review-20261012-box-domain-interactions:a1
Interacting box-domain construction (two-body Bakamjian-Thomas box law on Z^d):
full Poincare list, common core, no-invariant-box / non-essential-self-adjointness obstruction,
explicit finite-rapidity range, d=3 requirements, pairwise-lift (three-body) leftover.

Self-contained: numpy, scipy, sympy, mpmath, fractions only.  No file is written.
Every finite claim is exact (sympy / Fractions) or high precision (mpmath, 60 digits);
the two floating-point items (fibre-infimum search, random orbit sampling) are labelled.

NOT claimed here: a precision lattice closure of the interacting d=2 algebra on a grid.
The chart-level and fibre-level checks below are identities of the chart / abstract fibre
algebra, not that closure.
"""
import sys, time, itertools, random, subprocess, os, hashlib
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import minimize

T0 = time.time()
NPASS = 0
NFAIL = 0
def rec(name, ok, detail=''):
    global NPASS, NFAIL
    if ok: NPASS += 1
    else: NFAIL += 1
    print(('PASS ' if ok else 'FAIL ') + name + ((' | ' + detail) if detail else ''), flush=True)

I = sp.I

# ---------------------------------------------------------------------------------------------
# 0. optional: verify source hashes if the read-only source checkout is present
# ---------------------------------------------------------------------------------------------
SRC_REPO = '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt'
SRC_COMMIT = '02b443faa6d9a2331fb04d648c578c6b85e1900a'
SRC_DIR = '.claude/science/exercises/gravity-current-state-20261009/'
SRC_OBJECTS = [
    ('agents/C5_R7-1_report.md', '0c88e3ea3c3f219f9f55421e7ff381032005be434ac065d750890bebcbf29929'),
    ('agents/C5_R7-1_referee_verdict.md', '4f6236c4a58a9a783a668efa291aa8cea69a9241e10464cdccb64fecd44961de'),
    ('agents/C5_R8-1_report.md', '067b6d7cfdc5ce72c38535629faeb0af42386fe43f3782d11c025e715f3516a0'),
    ('agents/C5_R8-1_referee_verdict.md', '55250319687b8a9f57a7f93a74c7a9b019caef09cb306521c80df6a941062205'),
    ('scripts/C5/R8-1/r81_common.py', '13295e0696e6c0851d7127fcd5e8a4e411b84a16cd454ac16c91cfd86e7747b0'),
    ('scripts/C5/R8-1/r81_d2_lattice_algebra.py', '3ba4f59edd5e3c33de3f7cde97fffb1e233fa9d2923af01c50db32857b84b050'),
]
if os.path.isdir(SRC_REPO):
    for path, h in SRC_OBJECTS:
        try:
            data = subprocess.run(['git', '-C', SRC_REPO, 'show', SRC_COMMIT + ':' + SRC_DIR + path],
                                  capture_output=True, check=True).stdout
            rec('source hash %s' % path.split('/')[-1], hashlib.sha256(data).hexdigest() == h)
        except Exception as e:
            print('# source hash check for %s skipped (%s)' % (path, type(e).__name__))
else:
    print('# source checkout absent: source-hash checks skipped (hashes are recorded in RECOVERY_STATUS.json)')

# ---------------------------------------------------------------------------------------------
# 1. Bookkeeping: the full 2+1 Poincare list has 15 pairs; the R8-1 d=2 runners test 11
# ---------------------------------------------------------------------------------------------
gens2 = ['H', 'Px', 'Py', 'J', 'Kx', 'Ky']
all_pairs = set(frozenset(p) for p in itertools.combinations(gens2, 2))
# r81_d2_lattice_algebra.py:146-156 (and the chart runner) list exactly these eleven:
listed = [('Kx', 'Px'), ('Kx', 'Py'), ('Ky', 'Py'), ('Kx', 'H'), ('Ky', 'H'), ('Kx', 'Ky'),
          ('J', 'Kx'), ('J', 'Ky'), ('J', 'Px'), ('J', 'H'), ('Px', 'H')]
listed_set = set(frozenset(p) for p in listed)
omitted = all_pairs - listed_set
rec('Poincare(2+1) has C(6,2)=15 commutator pairs; runner lists 11 distinct', len(all_pairs) == 15 and len(listed_set) == 11)
rec('omitted by the d=2 runners: [Ky,Px],[J,Py],[Py,H],[Px,Py] (4)',
    omitted == set(frozenset(p) for p in [('Ky', 'Px'), ('J', 'Py'), ('Py', 'H'), ('Px', 'Py')]))
gens3 = ['H'] + ['P%d' % i for i in (1, 2, 3)] + ['J%d' % i for i in (1, 2, 3)] + ['K%d' % i for i in (1, 2, 3)]
rec('Poincare(3+1) has C(10,2)=45 commutator pairs', len(list(itertools.combinations(gens3, 2))) == 45)

# ---------------------------------------------------------------------------------------------
# 2. Exact fibre algebra on plane waves:  generators on functions of P with (M,S) -> (mu, spin)
#    H = sqrt(mu^2+P^2), K_a = 1/2{H, i d_a} + alpha*(P x S)_a/(mu+H),  J = X x P + S
#    Coefficients are rational in (P, H, mu); reduce modulo H^2 = mu^2 + P^2.
# ---------------------------------------------------------------------------------------------
def fibre_algebra(d, Smats, alpha=1, sgn=1, kind='BT'):
    n = Smats[0].shape[0]
    mu, H = sp.symbols('mu H', positive=True)
    P = sp.symbols('P1:%d' % (d + 1), real=True)
    a = sp.symbols('a1:%d' % (d + 1))
    def D(G, i):   # derivative of coefficient G(P,H) times exp(a.P), H' = P/H
        return G.applyfunc(lambda e: sp.diff(e, P[i]) + sp.diff(e, H) * P[i] / H + a[i] * e)
    def X(G, i): return I * D(G, i)
    def Hop(G): return H * G
    def Pop(i): return lambda G: P[i] * G
    def Jop(i):
        if d == 2:
            return lambda G: I * (P[1] * D(G, 0) - P[0] * D(G, 1)) + Smats[0] * G
        b, c = (i + 1) % 3, (i + 2) % 3
        return lambda G: I * (P[c] * D(G, b) - P[b] * D(G, c)) + Smats[i] * G
    def Kop(i):
        def f(G):
            t = (H * X(G, i) + X(H * G, i)) / 2
            if d == 2:
                s = Smats[0] * G
                pxs = P[1] * s if i == 0 else -P[0] * s
            else:
                b, c = (i + 1) % 3, (i + 2) % 3
                pxs = P[b] * (Smats[c] * G) - P[c] * (Smats[b] * G)
            spt = alpha * sgn * pxs / (mu + H)
            return (-t + spt) if kind == 'printed' else (t + spt)
        return f
    g = {'H': Hop}
    for i in range(d): g['P%d' % (i + 1)] = Pop(i)
    if d == 2:
        g['J'] = Jop(0)
    else:
        for i in range(3): g['J%d' % (i + 1)] = Jop(i)
    for i in range(d): g['K%d' % (i + 1)] = Kop(i)
    return g, (mu, H, P, a, n)

def reduce_zero(expr, mu, H, P):
    num = sp.numer(sp.together(sp.expand(expr)))
    if num == 0: return True
    rel = H ** 2 - mu ** 2 - sum(p ** 2 for p in P)
    return sp.expand(sp.rem(sp.expand(num), rel, H)) == 0

def comm(A, B, G): return A(B(G)) - B(A(G))

def table(d):
    T = {}
    if d == 2:
        names = ['H', 'P1', 'P2', 'J', 'K1', 'K2']
        T[('J', 'P1')] = {'P2': I}; T[('J', 'P2')] = {'P1': -I}
        T[('J', 'K1')] = {'K2': I}; T[('J', 'K2')] = {'K1': -I}
        T[('K1', 'P1')] = {'H': I}; T[('K2', 'P2')] = {'H': I}
        T[('K1', 'H')] = {'P1': I}; T[('K2', 'H')] = {'P2': I}
        T[('K1', 'K2')] = {'J': -I}
    else:
        names = ['H', 'P1', 'P2', 'P3', 'J1', 'J2', 'J3', 'K1', 'K2', 'K3']
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    e = sp.LeviCivita(a, b, c)
                    if e == 0: continue
                    T.setdefault(('J%d' % (a + 1), 'J%d' % (b + 1)), {})['J%d' % (c + 1)] = I * e
                    T.setdefault(('J%d' % (a + 1), 'P%d' % (b + 1)), {})['P%d' % (c + 1)] = I * e
                    T.setdefault(('J%d' % (a + 1), 'K%d' % (b + 1)), {})['K%d' % (c + 1)] = I * e
                    T.setdefault(('K%d' % (a + 1), 'K%d' % (b + 1)), {})['J%d' % (c + 1)] = -I * e
        for a in range(3):
            T[('K%d' % (a + 1), 'P%d' % (a + 1))] = {'H': I}
            T[('K%d' % (a + 1), 'H')] = {'P%d' % (a + 1): I}
    return names, T

def failing_pairs(d, Smats, **kw):
    names, T = table(d)
    gens, (mu, H, P, a, n) = fibre_algebra(d, Smats, **kw)
    v = sp.Matrix(sp.symbols('v1:%d' % (n + 1)))
    bad = []; tot = 0
    for A, B in itertools.combinations(names, 2):
        c = T.get((A, B))
        if c is None:
            c2 = T.get((B, A)); c = {k: -x for k, x in c2.items()} if c2 else {}
        res = comm(gens[A], gens[B], v)
        for C, coef in c.items(): res = res - coef * gens[C](v)
        tot += 1
        if not all(reduce_zero(e, mu, H, P) for e in res): bad.append((A, B))
    return tot, bad

def spin_matrices(j):
    j = sp.nsimplify(j); dim = int(2 * j + 1)
    ms = [j - k for k in range(dim)]
    Jz = sp.diag(*ms)
    Jp = sp.zeros(dim, dim)
    for k in range(1, dim):
        m_ = ms[k]
        Jp[k - 1, k] = sp.sqrt(j * (j + 1) - m_ * (m_ + 1))
    Jm = Jp.T
    return [(Jp + Jm) / 2, (Jp - Jm) / (2 * I), Jz]

s_sym = sp.Symbol('s', real=True)
S2 = [sp.Matrix([[s_sym]])]
tot, bad = failing_pairs(2, S2)
rec('d=2 fibre algebra: all 15 commutators close exactly (symbolic mu, spin s)', tot == 15 and not bad, 'bad=%s' % bad)
for lab, kw in [('printed boost sign (R7-1)', dict(kind='printed')),
                ('spin coefficient alpha=2', dict(alpha=2)),
                ('spin coefficient alpha=0 (no spin term)', dict(alpha=0)),
                ('spin term sign flipped', dict(sgn=-1))]:
    tot, bad = failing_pairs(2, S2, **kw)
    expected = ({('H', 'K1'), ('H', 'K2'), ('P1', 'K1'), ('P2', 'K2'), ('K1', 'K2')} if 'printed' in lab
                else {('K1', 'K2')})
    rec('d=2 control [%s] fails exactly %s' % (lab, sorted(expected)), set(bad) == expected, 'fails=%s' % bad)
# exact residual of [K1,K2]+iJ in the spin coefficient
al = sp.Symbol('alpha')
gens, (mu_, H_, P_, a_, n_) = fibre_algebra(2, S2, alpha=al)
v1 = sp.Matrix([sp.Symbol('v')])
res = (comm(gens['K1'], gens['K2'], v1) + I * gens['J'](v1))[0] - I * (1 - al) * s_sym * v1[0]
rec('d=2: [Kx,Ky]+iJ = i(1-alpha) s exactly (alpha enters only here)', reduce_zero(res, mu_, H_, P_))

for lab, j in [('1/2', sp.Rational(1, 2)), ('1', 1), ('2', 2)]:
    tot, bad = failing_pairs(3, spin_matrices(j))
    rec('d=3 fibre algebra spin %s: all 45 commutators close exactly' % lab, tot == 45 and not bad, 'bad=%s' % bad)
tot, bad = failing_pairs(3, spin_matrices(1), sgn=-1)
rec('d=3 control: spin-term sign flipped fails exactly the three [Ka,Kb]', set(bad) == {('K1', 'K2'), ('K1', 'K3'), ('K2', 'K3')})
tot, bad = failing_pairs(3, spin_matrices(1), alpha=0)
rec('d=3 control: no spin term fails exactly the three [Ka,Kb]', set(bad) == {('K1', 'K2'), ('K1', 'K3'), ('K2', 'K3')})

# 2b. the Kato-Rellich route in the chart: 1/2{H,X} = H^(1/2) X H^(1/2) exactly (fibre, d=1)
Pp, mu1 = sp.symbols('P mu', positive=True)
fP = sp.Function('f')(Pp)
Hh = sp.sqrt(mu1 ** 2 + Pp ** 2)
lhs = (Hh * I * sp.diff(fP, Pp) + I * sp.diff(Hh * fP, Pp)) / 2
rhs = sp.sqrt(Hh) * I * sp.diff(sp.sqrt(Hh) * fP, Pp)
rec('chart fibre: 1/2{H,i d_P} = H^(1/2) (i d_P) H^(1/2) exactly (so [A,[A,X]]=0, A=H^(1/2))', sp.simplify(lhs - rhs) == 0)

# ---------------------------------------------------------------------------------------------
# 3. Chart identities at 60 digits (no grid, no finite differences):
#    lattice free generators (box law s(k)=k), in (P,k1) coordinates, == BT free generators in the
#    canonical chart (P,q) with half-density U; d=2 and d=3.  Also the lattice-native S and X_NW.
# ---------------------------------------------------------------------------------------------
mp.mp.dps = 60
MASS = mp.mpf('0.5')
II = mp.mpc(0, 1)

def make_chart(d):
    def vdot(a, b): return sum(x * y for x, y in zip(a, b))
    def eps(k): return mp.sqrt(MASS ** 2 + vdot(k, k))
    def chart_to_k(P, q):
        w = mp.sqrt(MASS ** 2 + vdot(q, q)); M0 = 2 * w; H0 = mp.sqrt(M0 ** 2 + vdot(P, P))
        c = vdot(P, q) / (M0 * (H0 + M0)) + w / M0
        return [q[i] + P[i] * c for i in range(d)]
    def k_to_chart(P, k1):
        k2 = [P[i] - k1[i] for i in range(d)]
        e1, e2 = eps(k1), eps(k2); H0 = e1 + e2; M0 = mp.sqrt(H0 ** 2 - vdot(P, P))
        c = vdot(P, k1) / (M0 * (H0 + M0)) - e1 / M0
        return [k1[i] + P[i] * c for i in range(d)]
    return vdot, eps, chart_to_k, k_to_chart

def chart_identity(d, seed, sgnK=1):
    vdot, eps, chart_to_k, k_to_chart = make_chart(d)
    rnd = random.Random(seed)
    P0 = [mp.mpf(rnd.uniform(-.5, .5)) for _ in range(d)]
    q0 = [mp.mpf(rnd.uniform(-.7, .7)) for _ in range(d)]
    k10 = chart_to_k(P0, q0)
    cc = [mp.mpc(rnd.uniform(-1, 1), rnd.uniform(-1, 1)) for _ in range(12)]
    def Psi(*x):
        P = x[:d]; q = x[d:]
        ph = sum(cc[i] * P[i] for i in range(d)) + sum(cc[3 + i] * q[i] for i in range(d)) + cc[6] * P[0] * q[-1] + cc[7] * vdot(P, P)
        pol = 1 + cc[8] * q[0] + cc[9] * q[-1] + cc[10] * q[0] * q[1] + cc[11] * P[0] * q[1]
        return mp.exp(ph) * pol
    def Jq(P, k1):
        k2 = [P[i] - k1[i] for i in range(d)]
        e1, e2 = eps(k1), eps(k2); H0 = e1 + e2; q = k_to_chart(P, k1)
        w = mp.sqrt(MASS ** 2 + vdot(q, q)); return w * H0 / (2 * e1 * e2)
    def psi(*x):
        P = list(x[:d]); k1 = list(x[d:])
        return Psi(*P, *k_to_chart(P, k1)) * mp.sqrt(Jq(P, k1))
    x0 = tuple(P0) + tuple(k10)
    def dd(f, x, var):
        o = [0] * (2 * d); o[var] = 1
        return mp.diff(f, tuple(x), tuple(o))
    def X1(f, a): return lambda *x: II * (dd(f, x, d + a) + dd(f, x, a))
    def X2(f, a): return lambda *x: II * dd(f, x, a)
    def mulf(g, f): return lambda *x: g(*x) * f(*x)
    def e1f(*x): return eps(list(x[d:]))
    def e2f(*x): return eps([x[i] - x[d + i] for i in range(d)])
    def H0f(*x): return e1f(*x) + e2f(*x)
    def M0f(*x): return mp.sqrt(H0f(*x) ** 2 - vdot(x[:d], x[:d]))
    def Pf(a): return lambda *x: x[a]
    def k1f(a): return lambda *x: x[d + a]
    def k2f(a): return lambda *x: x[a] - x[d + a]
    def anti(g, Xop, f, a): return lambda *x: (g(*x) * Xop(f, a)(*x) + Xop(mulf(g, f), a)(*x)) / 2
    def K0(f, a):
        A = anti(e1f, X1, f, a); B = anti(e2f, X2, f, a)
        return lambda *x: A(*x) + B(*x)
    def J0(f, a=None):
        if d == 2:
            def r(*x):
                s = 0
                for (Xo, kf) in ((X1, k1f), (X2, k2f)):
                    s += Xo(mulf(kf(1), f), 0)(*x) - Xo(mulf(kf(0), f), 1)(*x)
                return s
            return r
        b, c = (a + 1) % 3, (a + 2) % 3
        def r(*x):
            s = 0
            for (Xo, kf) in ((X1, k1f), (X2, k2f)):
                s += Xo(mulf(kf(c), f), b)(*x) - Xo(mulf(kf(b), f), c)(*x)
            return s
        return r
    def XE(f, a):
        g1 = lambda *x: e1f(*x) / H0f(*x); g2 = lambda *x: e2f(*x) / H0f(*x)
        A = anti(g1, X1, f, a); B = anti(g2, X2, f, a)
        return lambda *x: A(*x) + B(*x)
    def XcrossP(f, a=None):
        if d == 2:
            return lambda *x: XE(mulf(Pf(1), f), 0)(*x) - XE(mulf(Pf(0), f), 1)(*x)
        b, c = (a + 1) % 3, (a + 2) % 3
        return lambda *x: XE(mulf(Pf(c), f), b)(*x) - XE(mulf(Pf(b), f), c)(*x)
    def Sdef(f, a=None):   # R8-1 section 3.2 lattice-native spin (d=2); the same expression in d=3
        J = J0(f, a); XP = XcrossP(f, a)
        return lambda *x: H0f(*x) / M0f(*x) * (J(*x) - XP(*x))
    def PdotJ(f):
        Js = [J0(f, a) for a in range(3)]
        return lambda *x: sum(x[a] * Js[a](*x) for a in range(3))
    def Scorr(f, a):   # d=3 corrected lattice-native S:  S_def - P (P.J0)/(M0 (H0+M0))
        Sd = Sdef(f, a); pj = PdotJ(f)
        return lambda *x: Sd(*x) - x[a] * pj(*x) / (M0f(*x) * (H0f(*x) + M0f(*x)))
    def PxS(f):
        if d == 2:
            Sf = Sdef(f)
            return [lambda *x: x[1] * Sf(*x), lambda *x: -x[0] * Sf(*x)]
        Sf = [Sdef(f, a) for a in range(3)]
        out = []
        for a in range(3):
            b, c = (a + 1) % 3, (a + 2) % 3
            out.append((lambda b, c: (lambda *x: x[b] * Sf[c](*x) - x[c] * Sf[b](*x)))(b, c))
        return out
    def XNW(f, a):
        pxs = PxS(f)[a]
        g = lambda *x: 1 / (H0f(*x) * (M0f(*x) + H0f(*x)))
        xe = XE(f, a)
        return lambda *x: xe(*x) - g(*x) * pxs(*x)
    # chart side
    def Hc(*x): return mp.sqrt(4 * (MASS ** 2 + vdot(x[d:], x[d:])) + vdot(x[:d], x[:d]))
    def M0c(*x): return 2 * mp.sqrt(MASS ** 2 + vdot(x[d:], x[d:]))
    def ddc(f, x, var):
        o = [0] * (2 * d); o[var] = 1
        return mp.diff(f, tuple(x), tuple(o))
    def Xc(f, a): return lambda *x: II * ddc(f, x, a)
    def Sc(f, a=None):
        if d == 2:
            return lambda *x: -II * (x[d] * ddc(f, x, d + 1) - x[d + 1] * ddc(f, x, d))
        b, c = (a + 1) % 3, (a + 2) % 3
        return lambda *x: -II * (x[d + b] * ddc(f, x, d + c) - x[d + c] * ddc(f, x, d + b))
    def Kc(f, a):
        Hf = mulf(Hc, f)
        A = lambda *x: (Hc(*x) * Xc(f, a)(*x) + Xc(Hf, a)(*x)) / 2
        if d == 2:
            Sf = Sc(f); pxs = [lambda *x: x[1] * Sf(*x), lambda *x: -x[0] * Sf(*x)][a]
        else:
            Sf = [Sc(f, t) for t in range(3)]; b, c = (a + 1) % 3, (a + 2) % 3
            pxs = lambda *x: x[b] * Sf[c](*x) - x[c] * Sf[b](*x)
        return lambda *x: A(*x) + sgnK * pxs(*x) / (M0c(*x) + Hc(*x))
    def Jc(f, a=None):
        if d == 2:
            return lambda *x: II * (x[1] * ddc(f, x, 0) - x[0] * ddc(f, x, 1)) + Sc(f)(*x)
        b, c = (a + 1) % 3, (a + 2) % 3
        return lambda *x: II * (x[c] * ddc(f, x, b) - x[b] * ddc(f, x, c)) + Sc(f, a)(*x)
    Pp_ = x0[:d]; qq = k_to_chart(list(Pp_), list(k10))
    xc = tuple(Pp_) + tuple(qq); sj = mp.sqrt(Jq(list(Pp_), list(k10)))
    res = {}
    def cmp(name, lat, chart):
        a = lat(*x0); b = chart(*xc) * sj
        res[name] = abs(a - b) / abs(b)
    for a in range(d): cmp('K0_%d' % a, K0(psi, a), Kc(Psi, a))
    if d == 2: cmp('J0', J0(psi), Jc(Psi))
    else:
        for a in range(3): cmp('J0_%d' % a, J0(psi, a), Jc(Psi, a))
    if d == 2: cmp('S_def', Sdef(psi), Sc(Psi))
    else:
        for a in range(3): cmp('S_corr_%d' % a, Scorr(psi, a), Sc(Psi, a))
        for a in range(3): cmp('S_def_%d(uncorrected)' % a, Sdef(psi, a), Sc(Psi, a))
    for a in range(d): cmp('XNW_%d' % a, XNW(psi, a), Xc(Psi, a))
    # round trip and Jacobian
    q_back = k_to_chart(P0, chart_to_k(P0, q0))
    res['roundtrip'] = max(abs(q_back[i] - q0[i]) for i in range(d))
    J = mp.matrix(d, d)
    for a in range(d):
        for b in range(d):
            o = [0] * d; o[b] = 1
            J[a, b] = mp.diff(lambda *k: k_to_chart(P0, list(k))[a], tuple(k10), tuple(o))
    res['jacobian'] = abs(mp.det(J) - Jq(P0, k10)) / abs(Jq(P0, k10))
    return res

for d in (2, 3):
    worst = 0
    worst_unc = 0
    names_ok = True
    for seed in (1, 2, 3):
        r = chart_identity(d, seed)
        for k, v in r.items():
            if 'uncorrected' in k: worst_unc = max(worst_unc, v); continue
            worst = max(worst, v)
    rec('d=%d chart identity (60 digits, 3 random points): K0, J0, X_NW, S, Jacobian, round trip; worst rel. diff < 1e-45' % d,
        worst < mp.mpf('1e-45'), 'worst=%s' % mp.nstr(worst, 3))
    if d == 3:
        rec('d=3: R8-1 section 3.2 S-formula S=(H0/M0)(J0-X_E x P) used unmodified is NOT the chart S (differs at O(1e-2))',
            worst_unc > mp.mpf('1e-3'), 'worst=%s' % mp.nstr(worst_unc, 3))
        rec('d=3: corrected lattice-native S = (H0/M0)(J0-X_E x P) - P (P.J0)/(M0 (H0+M0)) equals chart S (inside the 1e-45 line above)', True)
# controls: wrong spin sign in K0 chart formula
r = chart_identity(3, 2, sgnK=-1)
rec('d=3 control: spin term of opposite sign breaks K0 (rel diff > 1e-3)', max(r['K0_0'], r['K0_1'], r['K0_2']) > mp.mpf('1e-3'),
    'K0 diffs=%s' % [mp.nstr(r['K0_%d' % a], 3) for a in range(3)])

# ---------------------------------------------------------------------------------------------
# 4. Domain lemma: explicit leg-margin inequality for the common core
# ---------------------------------------------------------------------------------------------
def leg_bound(m, kappa, Pi):
    return kappa + Pi * (Fraction(1, 2) + Pi * kappa / (8 * m * m))
mpar = Fraction(1, 2)
bound_spec = leg_bound(mpar, Fraction(4, 5), Fraction(3, 5))
bound_dir = leg_bound(mpar, Fraction(1), Fraction(1))
B_FLAT = Fraction(13, 5)   # s(k)=k for |k_a| <= B = 2.6 in the R8-1 box law (r81_common.py BoxLaw: ratio sstep((B2-|k|)/(B2-B)) = 1)
rec('leg bound (spectrum-run params m=1/2,kappa=4/5,Pi1=3/5) = 1.244 < 2.6 (exact rationals)', bound_spec == Fraction(311, 250) and bound_spec < B_FLAT, str(bound_spec))
rec('leg bound (direct-run params kappa=1,Pi1=1) = 2 < 2.6 (exact rationals)', bound_dir == 2 and bound_dir < B_FLAT)
# brute-force sup check with the exact inverse chart at 40 digits (d=2 and d=3), boundary-heavy sampling
mp.mp.dps = 40
def sup_leg(d, kappa, Pi, ntr=400, seed=5):
    vdot, eps, chart_to_k, k_to_chart = make_chart(d)
    rnd = random.Random(seed); best = mp.mpf(0)
    for t in range(ntr):
        def rv(r):
            v = [rnd.gauss(0, 1) for _ in range(d)]; nrm = sum(x * x for x in v) ** .5
            return [mp.mpf(r) * mp.mpf(x / nrm) for x in v]
        rp = Pi if t % 2 == 0 else Pi * rnd.random()
        rq = kappa if t % 3 != 0 else kappa * rnd.random()
        P = rv(rp); q = rv(rq)
        k1 = chart_to_k(P, q); k2 = [P[i] - k1[i] for i in range(d)]
        best = max(best, mp.sqrt(vdot(k1, k1)), mp.sqrt(vdot(k2, k2)))
    return best
for d in (2, 3):
    sup = sup_leg(d, 0.8, 0.6)
    rec('d=%d: sampled sup |k_leg| over |P|<=0.6,|q|<=0.8 is below the proved bound 1.244' % d, sup <= mp.mpf(float(bound_spec)), 'sup=%s' % mp.nstr(sup, 6))
# capacity: largest internal mass allowed by the leg condition for given (Pi1, b)
Pi1 = Fraction(3, 5); bflat = B_FLAT
kap_max = (bflat - Pi1 / 2) / (1 + Pi1 * Pi1 / (8 * mpar * mpar))
mu_max = 2 * sp.sqrt(sp.Rational(kap_max.numerator, kap_max.denominator) ** 2 + sp.Rational(1, 4))
rec('leg-capacity: Sigma may contain internal masses up to mu_max = 2 sqrt(m^2+kappa_max^2) = %s for Pi1=0.6, b=2.6' % sp.N(mu_max, 5),
    abs(float(mu_max) - 4.0245) < 2e-3, 'kappa_max=%s' % kap_max)
rec('no umklapp on the core: |P|<Pi1<pi so k1+k2 = P as real vectors', float(Pi1) < np.pi)
mp.mp.dps = 60

# ---------------------------------------------------------------------------------------------
# 5. Obstruction trio (fibre, d=1 exact; d=2 explicit deficiency vector)
# ---------------------------------------------------------------------------------------------
th, mu_s, th1 = sp.symbols('theta mu theta1', positive=True)
gth = sp.Function('g')
Pq = sp.Symbol('P', real=True)
Hq = sp.sqrt(mu_s ** 2 + Pq ** 2)
# unitary map f(P) = g(theta(P))/sqrt(H), theta = asinh(P/mu):  K f = i H f' + (i/2) H' f  == i g'(theta)/sqrt(H)
f_expr = gth(sp.asinh(Pq / mu_s)) / sp.sqrt(Hq)
Kf = I * Hq * sp.diff(f_expr, Pq) + I * sp.diff(Hq, Pq) * f_expr / 2
target = I * sp.Subs(sp.Derivative(gth(th), th), th, sp.asinh(Pq / mu_s)).doit() / sp.sqrt(Hq)
rec('d=1 fibre: boost K = 1/2{H,i d_P} is unitarily i d/d(theta), P = mu sinh(theta) (exact)', sp.simplify(Kf - target) == 0)
# deficiency vectors e^{-theta}, e^{+theta} of K* on L2(-theta1, theta1); test against a compactly supported bump
bump = (th1 ** 2 - th ** 2) ** 3
ok = True
for sgn_, u in ((-1, sp.exp(-th)), (+1, sp.exp(th))):
    # K*u = i u' ; defining relation <K f,u> = <f,K*u> for f in C_c^infty(-theta1,theta1): int conj(i f') u = int conj(f) i u'
    lhs_ = sp.integrate(sp.expand((-I) * sp.diff(bump, th) * u), (th, -th1, th1))
    rhs_ = sp.integrate(sp.expand(bump * I * sp.diff(u, th)), (th, -th1, th1))
    ok = ok and sp.simplify(lhs_ - rhs_) == 0 and sp.simplify(I * sp.diff(u, th) - sgn_ * I * u) == 0
rec('d=1: K*u = -+i u has L2 solutions e^{-+theta} on (-theta1,theta1): deficiency indices (1,1) per fibre, K|core not essentially self-adjoint', ok)
# boundary form non-zero (symmetric not self-adjoint)
u = sp.exp(th)
Ku = I * sp.diff(u, th)
bform = sp.simplify(sp.integrate(sp.conjugate(Ku) * u, (th, -th1, th1)) - sp.integrate(sp.conjugate(u) * Ku, (th, -th1, th1)))
rec('d=1: <K*u,u>-<u,K*u> = -2i*sinh(2 theta1)/1 != 0 for u=e^{theta}, so K* is not symmetric and the closure of K|core is not self-adjoint', sp.simplify(bform + 2 * I * sp.sinh(2 * th1)) == 0)
# d=2: formal deficiency solution on a chord (spin term included)
Px, Py = sp.symbols('Px Py', real=True)
mu2, s2 = sp.symbols('mu s', positive=True)
H2 = sp.sqrt(mu2 ** 2 + Px ** 2 + Py ** 2)
Phi = sp.Function('Phi')(Px, Py); phi = sp.Function('varphi')(Py)
Vp = Py * s2 / (mu2 + H2)
theta_x = sp.asinh(Px / sp.sqrt(mu2 ** 2 + Py ** 2))
for sg in (+1, -1):   # (K_x + sg*i) u = 0
    u2 = phi * H2 ** sp.Rational(-1, 2) * sp.exp(-sg * theta_x + I * Phi)
    Kx_u = I * H2 * sp.diff(u2, Px) + I * sp.diff(H2, Px) * u2 / 2 + Vp * u2
    expr = (Kx_u + sg * I * u2)
    expr = expr.subs(sp.Derivative(Phi, Px), Vp / H2).doit()
    ok2 = sp.simplify(expr / u2) == 0
    rec('d=2 fibre: K_x (with spin term) has the formal solution u=varphi(Py) H^(-1/2) exp(%s theta_x + i Phi) of (K_x %s i)u=0 on each chord (nonzero, square-integrable on the disk for bounded varphi)' % ('-' if sg == 1 else '+', '+' if sg == 1 else '-'), ok2)
# no invariant box: boost orbit of any P reaches |P|=Pi1 in finite rapidity (closed form), for every mu
rap = lambda Pv, muv, Pi: float(np.arcsinh(Pi / muv) + np.arcsinh(Pv / muv))
rec('d=1: exit rapidity from |P|<Pi1 is finite for every P, mu (asinh(Pi1/mu)+asinh(P/mu)): no boost-invariant bounded momentum box',
    all(np.isfinite(rap(Pv, mv, 0.6)) for Pv in (-0.5, 0, 0.5) for mv in (0.3, 0.85, 3.0)))
# bounded-H ceiling (elementary): <psi_eta,H psi_eta> <= ||H|| versus <H>cosh(eta)+<P>sinh(eta)
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0 / np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0 / np.where(x < 1, 1 - x, 1)), 0.0)
    return e1 / (e1 + e2)
def wrap(k): return -(((-k) + np.pi) % (2 * np.pi) - np.pi)
def s_box(k, B=2.6, B2=3.0):
    k = wrap(k); r = sstep((B2 - np.abs(k)) / (B2 - B)); return r * k + (1 - r) * np.sin(k)
kk = np.linspace(-np.pi, np.pi, 200001)
eps_max = float(np.max(np.sqrt(0.25 + s_box(kk) ** 2)))
Hmax_free = 2 * eps_max
eta_ceiling = float(np.arccosh(Hmax_free / 0.85))
rec('bounded-H ceiling: R8-1 box law has max H0 = 2*max eps = %.4f, so a rest state of mass 0.85 can follow the continuum boost energy only up to eta <= %.3f (free-part bound; ||W|| would add to Hmax)' % (Hmax_free, eta_ceiling),
    Hmax_free > 5 and eta_ceiling > 2)

# ---------------------------------------------------------------------------------------------
# 6. Explicit finite-rapidity range  eta*(rho,mu) = asinh(Pi1/mu) - asinh(rho/mu)   (any d)
#    Boost of (H,P) along unit n, rapidity s:  H' = H cosh s - P.n sinh s ; |Phi|^2 = H'^2 - mu^2
# ---------------------------------------------------------------------------------------------
rng = np.random.default_rng(11)
def exit_rapidity(Pvec, n, mu, Pi):
    # first s>0 with |Phi_s(P)| = Pi, via closed form (P_par decreases): s = asinh(Ppar/mperp) + asinh(sqrt(Pi^2-Pperp^2)/mperp)
    Ppar = float(Pvec @ n); Pperp2 = float(Pvec @ Pvec - Ppar ** 2)
    mperp = np.sqrt(mu * mu + Pperp2)
    return np.arcsinh(Ppar / mperp) + np.arcsinh(np.sqrt(max(Pi * Pi - Pperp2, 0.0)) / mperp)
def phi_norm(Pvec, n, mu, s):
    H = np.sqrt(mu * mu + Pvec @ Pvec); Hp = H * np.cosh(s) - (Pvec @ n) * np.sinh(s)
    return np.sqrt(max(Hp * Hp - mu * mu, 0.0))
allok = True; worst_gap = 1e9
for d in (2, 3):
    for mu in (0.6, 0.85, 2.0):
        for rho in (0.1, 0.25, 0.4):
            Pi = 0.6
            etastar = np.arcsinh(Pi / mu) - np.arcsinh(rho / mu)
            for t in range(400):
                n = rng.normal(size=d); n /= np.linalg.norm(n)
                v = rng.normal(size=d); v /= np.linalg.norm(v); Pv = v * rho * rng.random() ** (1 / d)
                se = exit_rapidity(Pv, n, mu, Pi)
                # consistency: |Phi| equals Pi at se and is < Pi just before
                good = abs(phi_norm(Pv, n, mu, se) - Pi) < 1e-9 and phi_norm(Pv, n, mu, max(se - 1e-6, 0)) < Pi + 1e-9
                allok = allok and good and se >= etastar - 1e-12
                worst_gap = min(worst_gap, se - etastar)
            # attained at P = -rho n
            n = np.zeros(d); n[0] = 1.0
            se = exit_rapidity(-rho * n, n, mu, Pi)
            allok = allok and abs(se - etastar) < 1e-12
rec('exit rapidity >= eta*(rho,mu)=asinh(Pi1/mu)-asinh(rho/mu) for all sampled P in the rho-ball and boost directions (d=2,3), with equality at P=-rho n [floating-point sampling, 9x400x2 cases]',
    allok, 'min(exit-eta*)=%.2e' % worst_gap)
mp.mp.dps = 40
mu_, rho_, Pi_ = mp.mpf('0.85'), mp.mpf('0.25'), mp.mpf('0.6')
etas = mp.asinh(Pi_ / mu_) - mp.asinh(rho_ / mu_)
Hh0 = mp.sqrt(mu_ ** 2 + rho_ ** 2)
Hp = Hh0 * mp.cosh(etas) + rho_ * mp.sinh(etas)   # P = -rho n, boost: H' = H cosh s - P.n sinh s
rec('eta*(0.25;0.85;Pi1=0.6) = %s reproduces R8-1 d=1 value 0.367 (their rounded number: asinh(0.6/0.85)-asinh(0.25/0.85)); orbit hits |P|=Pi1 exactly (40 digits)' % mp.nstr(etas, 6),
    abs(mp.sqrt(Hp ** 2 - mu_ ** 2) - Pi_) < mp.mpf('1e-35') and abs(etas - mp.mpf('0.3670')) < mp.mpf('0.0035'))
mp.mp.dps = 60

# ---------------------------------------------------------------------------------------------
# 7. Ordered-pair 1/2 normalisation, exact: N=2 and N=3 sectors on 4 modes (Jordan-Wigner, Fractions)
# ---------------------------------------------------------------------------------------------
NM = 4
def apply_ad(i, state):
    if state[i]: return 0, None
    sgn = (-1) ** sum(state[:i]); s = list(state); s[i] = 1
    return sgn, tuple(s)
def apply_a(i, state):
    if not state[i]: return 0, None
    sgn = (-1) ** sum(state[:i]); s = list(state); s[i] = 0
    return sgn, tuple(s)
def fock_W(W, c, state):
    out = {}
    for a in range(NM):
        for b in range(NM):
            for a2 in range(NM):
                for b2 in range(NM):
                    w = W[a2][b2][a][b]
                    if w == 0: continue
                    # c * W[a'b';ab] a+_{a'} a+_{b'} a_b a_a |state>
                    sg1, s1 = apply_a(a, state)
                    if not sg1: continue
                    sg2, s2_ = apply_a(b, s1)
                    if not sg2: continue
                    sg3, s3 = apply_ad(b2, s2_)
                    if not sg3: continue
                    sg4, s4 = apply_ad(a2, s3)
                    if not sg4: continue
                    out[s4] = out.get(s4, 0) + c * w * sg1 * sg2 * sg3 * sg4
    return out
def basis(N): return [tuple(1 if i in comb else 0 for i in range(NM)) for comb in itertools.combinations(range(NM), N)]
def occ(state): return [i for i, x in enumerate(state) if x]
def perm_sign(p):
    p = list(p); sg = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; sg = -sg
    return sg
def first_quantised(W, N, bra, ket):
    # <T'| sum_{x<y} W^{(xy)} |T> / N!, T = sum_sigma sgn(sigma) delta  (unnormalised antisymmetric tensor of the Fock state)
    ob, ok_ = occ(bra), occ(ket); tot = Fraction(0)
    from math import factorial
    for sb in itertools.permutations(range(N)):
        for sk in itertools.permutations(range(N)):
            sgn = perm_sign(sb) * perm_sign(sk)
            ib = [ob[i] for i in sb]; ik = [ok_[i] for i in sk]
            for x, y in itertools.combinations(range(N), 2):
                if all(ib[z] == ik[z] for z in range(N) if z not in (x, y)):
                    tot += sgn * W[ib[x]][ib[y]][ik[x]][ik[y]]
    return tot / factorial(N)
def rand_W(rnd, kind):
    W = [[[[Fraction(0)] * NM for _ in range(NM)] for _ in range(NM)] for _ in range(NM)]
    raw = {}
    for idx in itertools.product(range(NM), repeat=4):
        raw[idx] = Fraction(rnd.randint(-9, 9), rnd.randint(1, 5))
    for (a2, b2, a, b) in itertools.product(range(NM), repeat=4):
        # exchange symmetric + hermitian-real symmetrisation
        terms = [raw[(a2, b2, a, b)], raw[(b2, a2, b, a)], raw[(a, b, a2, b2)], raw[(b, a, b2, a2)]]
        w = sum(terms) / 4
        if kind == 'odd':   # odd in each pair of indices (like the p-wave kernel)
            w = (raw[(a2, b2, a, b)] - raw[(b2, a2, a, b)] - raw[(a2, b2, b, a)] + raw[(b2, a2, b, a)])
            w2 = (raw[(a, b, a2, b2)] - raw[(b, a, a2, b2)] - raw[(a, b, b2, a2)] + raw[(b, a, b2, a2)])
            w = (w + w2) / 8
        W[a2][b2][a][b] = w
    return W
rnd = random.Random(7)
Wg = rand_W(rnd, 'sym')
for N in (2, 3):
    st = basis(N)
    okh = True; ok4 = False
    for bra in st:
        for ket in st:
            fq = first_quantised(Wg, N, bra, ket)
            f_half = fock_W(Wg, Fraction(1, 2), ket).get(bra, Fraction(0))
            f_quart = fock_W(Wg, Fraction(1, 4), ket).get(bra, Fraction(0))
            okh = okh and (f_half == fq)
            if f_quart != fq: ok4 = True
    rec('N=%d sector: Fock prefactor 1/2 reproduces sum_{x<y} W^{(xy)} exactly (all %d x %d matrix elements, Fractions)' % (N, len(st), len(st)), okh)
    rec('N=%d sector: Fock prefactor 1/4 does NOT (mismatch present)' % N, ok4)
Wo = rand_W(rnd, 'odd')
st = basis(2); ok_odd = True
for bra in st:
    for ket in st:
        i2, j2 = occ(bra); i1, j1 = occ(ket)
        ok_odd = ok_odd and (fock_W(Wo, Fraction(1, 2), ket).get(bra, Fraction(0)) == 2 * Wo[i2][j2][i1][j1])
rec('odd kernel: Fock(1/2) matrix element on normalised pair states = 2 W(k\',k) (the source of the earlier referee\'s spurious factor 2), exact', ok_odd)

# ---------------------------------------------------------------------------------------------
# 8. Three bodies, d=1, pairwise lift: exact leftover and an infimum-mass obstruction in a solvable model
#    model: pair mass shift  W_ij = sqrt(H0ij^2 + a) - H0ij  (multiplication operator; pair closure holds exactly)
# ---------------------------------------------------------------------------------------------
p = sp.symbols('p1:4', real=True); a_s = sp.Symbol('a', positive=True)
c_ = sp.symbols('c1:4'); b_ = sp.symbols('b1:4')
eps_ = [sp.sqrt(1 + x ** 2) for x in p]
f0 = sp.exp(sum(c_[i] * p[i] for i in range(3))) * (1 + b_[0] * p[0] + b_[1] * p[1] ** 2 + b_[2] * p[0] * p[2])
pairs = [(0, 1), (0, 2), (1, 2)]
def H0p(i, j): return eps_[i] + eps_[j]
def Wp(i, j): return sp.sqrt(H0p(i, j) ** 2 + a_s) - H0p(i, j)
def Xop(i, j, g):
    return sum(I * ((eps_[x] / H0p(i, j)) * sp.diff(g, p[x]) + sp.diff((eps_[x] / H0p(i, j)) * g, p[x])) / 2 for x in (i, j))
def K0op(g, idx=(0, 1, 2)): return sum(I * (eps_[x] * sp.diff(g, p[x]) + sp.diff(eps_[x] * g, p[x])) / 2 for x in idx)
def uvec(i, j, g): return sum(eps_[x] / H0p(i, j) * sp.diff(g, p[x]) for x in (i, j))
def Kpair(i, j, g): return K0op(g, (i, j)) + (Wp(i, j) * Xop(i, j, g) + Xop(i, j, Wp(i, j) * g)) / 2
def Hpair(i, j, g): return (H0p(i, j) + Wp(i, j)) * g
vals = {p[0]: sp.Rational(3, 10), p[1]: sp.Rational(-7, 10), p[2]: sp.Rational(11, 10), a_s: sp.Rational(1, 2),
        c_[0]: sp.Rational(1, 3), c_[1]: sp.Rational(-1, 5), c_[2]: sp.Rational(2, 7),
        b_[0]: sp.Rational(1, 3), b_[1]: sp.Rational(1, 2), b_[2]: sp.Rational(-1, 4)}
def ev(e, dps=40): return sp.N(e.subs(vals), dps)
res_pair = Kpair(0, 1, Hpair(0, 1, f0)) - Hpair(0, 1, Kpair(0, 1, f0)) - I * (p[0] + p[1]) * f0
rec('model: two-body pair closure [K_ij,H_ij]=iP_ij holds (residual at 40 digits)', abs(ev(res_pair)) < 1e-30, 'resid=%s' % sp.N(abs(ev(res_pair)), 3))
def K3(g): return K0op(g) + sum((Wp(i, j) * Xop(i, j, g) + Xop(i, j, Wp(i, j) * g)) / 2 for i, j in pairs)
def H3(g): return (sum(eps_) + sum(Wp(i, j) for i, j in pairs)) * g
res3 = K3(H3(f0)) - H3(K3(f0)) - I * sum(p) * f0
Cf = I * sum(Wp(i, j) * uvec(i, j, Wp(k, l)) for (i, j) in pairs for (k, l) in pairs if (i, j) != (k, l)) * f0
rec('3-body pairwise lift: [K,H]-iP = sum_{(ij)!=(kl)} i W_ij u_ij(W_kl) exactly (derivation in ATTEMPT step 10; residual at 40 digits)',
    abs(ev(res3 - Cf)) < 1e-30, 'diff=%s' % sp.N(abs(ev(res3 - Cf)), 3))
rec('3-body pairwise lift: the leftover is nonzero (|C f| = %s > 1e-3)' % sp.N(abs(ev(Cf)), 5), abs(ev(Cf)) > 1e-3)
# small-a scaling of the leftover: C ~ a^2
def Cval(aval):
    vv = dict(vals); vv[a_s] = aval
    return abs(sp.N(Cf.subs(vv), 30))
r1, r2 = Cval(sp.Rational(1, 100)), Cval(sp.Rational(1, 200))
rec('leftover scales as a^2 at small a (ratio C(a)/C(a/2) -> 4: got %s)' % sp.N(r1 / r2, 6), abs(float(r1 / r2) - 4.0) < 0.1)
# infimum of the 3-body fibre mass depends on P => no K at all (Lorentz-invariant spectrum requires P-independence)
def M3(p1, p2, P, a):
    pp = [p1, p2, P - p1 - p2]; e = [np.sqrt(1 + x * x) for x in pp]
    Hh_ = sum(e)
    for (i, j) in pairs:
        h = e[i] + e[j]; Hh_ += np.sqrt(h * h + a) - h
    return np.sqrt(max(Hh_ * Hh_ - P * P, 0.0))
def Mmin(P, a, starts=24):
    r_ = np.random.default_rng(0); best = 1e9
    for t in range(starts):
        x0 = r_.uniform(-3, 3, 2)
        r = minimize(lambda x: M3(x[0], x[1], P, a), x0, method='Nelder-Mead', options=dict(xatol=1e-11, fatol=1e-13, maxiter=3000))
        best = min(best, r.fun)
    return best
m0 = Mmin(0.0, 1.0); m2 = Mmin(2.0, 1.0); m4 = Mmin(4.0, 1.0)
exact0 = 3 + 3 * (np.sqrt(5.0) - 2)
rec('solvable model (m=1,a=1): inf of 3-body mass at P=0 is 3+3(sqrt5-2)=%.8f (global search agrees)' % exact0, abs(m0 - exact0) < 1e-8, 'search=%.8f' % m0)
rec('solvable model: inf mass at P=2 is %.8f and at P=4 is %.8f, below the P=0 value by > 1e-3: no K generating a (local) unitary boost group across a P-interval containing 0 and 2 can exist for the pairwise H (a Lie-algebra-only K on a smaller domain is NOT excluded by this) [floating-point global search]' % (m2, m4),
    (m0 - m2 > 1e-3) and (m0 - m4 > 1e-2))

# ---------------------------------------------------------------------------------------------
# 9. d=3 requirement: rotation-invariant p-wave kernel commutes with the internal angular momentum
# ---------------------------------------------------------------------------------------------
for d in (2, 3):
    q = sp.symbols('q1:%d' % (d + 1), real=True); qp = sp.symbols('r1:%d' % (d + 1), real=True)
    bfun = sp.Function('b')
    kern = sum(q[i] * qp[i] for i in range(d)) * bfun(sum(x * x for x in q)) * bfun(sum(x * x for x in qp))   # sum_a g_a(q) g_a(q')
    comps = [(0, 1)] if d == 2 else [(0, 1), (1, 2), (2, 0)]
    ok = True
    for (i, j) in comps:
        Lk = (q[i] * sp.diff(kern, q[j]) - q[j] * sp.diff(kern, q[i])) + (qp[i] * sp.diff(kern, qp[j]) - qp[j] * sp.diff(kern, qp[i]))
        ok = ok and sp.simplify(Lk) == 0
    rec('d=%d: kernel sum_a g_a(q)g_a(q\'), g_a = q_a b(|q|^2) is rotation invariant, so [S,V]=0 and [S,M]=0 (exact)' % d, ok)
    oddk = sp.simplify(kern.subs({x: -x for x in q}, simultaneous=True) + kern) == 0
    rec('d=%d: p-wave kernel is odd under q -> -q (fermionic channel)' % d, oddk)

print('# runtime %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (NPASS, NFAIL))
if NFAIL == 0:
    print('HIT: scoped new results on the R8-1 two-body box law: all 15 (d=2) and 45 (d=3) Poincare commutators close exactly on the fibre algebra with the repaired spin term (R8-1 tested 11 of 15), the direct d=3 analogue of the lattice-native spin needs a helicity correction, the core boost is not essentially self-adjoint (deficiency (1,1) per fibre; no boost-invariant box), eta*(rho,mu)=asinh(Pi1/mu)-asinh(rho/mu) in closed form, and the pairwise three-body lift leaves exactly C=sum i W_ij u_ij(W_kl) with a P-dependent infimum mass in a solvable model.')
print('SUMMARY: Exact fibre-level 15/45-commutator closure, 60-digit chart identities (d=2,3) with a d=3 spin correction, the no-invariant-box and non-essential-self-adjointness obstruction, a closed-form finite-rapidity range, and an exact pairwise three-body leftover; it is not a precision lattice closure of the interacting d=2 algebra.')
sys.exit(0 if NFAIL == 0 else 1)
