#!/usr/bin/env python3
"""First-order cubic completion of the member (alpha = K/4, beta = -alpha, with the shift), leading order in the spacing.
J:derive:the-members-cubic-completion-in-the-scalar-sector:a2

Solves delta0 V3 + delta1 S2 = 0 exactly over Q for all local cubic vertices V3 with two derivatives (T-even,
at most one time derivative per field) and all local first-order deformations delta1 (one derivative), and
quotients by local field redefinitions phi -> phi + F(phi, phi) (which also absorb delta0-exact delta1).
Symbols: d_j -> k_j, d_t -> w (formal exponential plane waves; integration by parts <-> k1 + k2 + k3 = 0).

A  the landed member (block 144 T1 form) is gauge invariant; the comparator's quadratic part equals it
B  scalar sector, rotation-invariant: 4 classes; the comparator's vertex is one; none is strictly invariant
C  full configurations, rotation-invariant: exactly 1 class, the comparator's (validation of the machinery)
D  scalar sector, cubic-symmetric (hyperoctahedral tensors, general momenta): still 4 classes, spanned by B's
E  full configurations, cubic-symmetric (general momenta): exactly 1 class, the comparator's   [long run]
"""
import itertools, sys, time
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

I3 = sp.eye(3)
w1, w2, zeta, chi = sp.symbols('w1 w2 zeta chi')
RANK = dict(n=0, N=1, h=2, zeta=0, xi=1)
PAR = dict(n=1, N=-1, h=1, zeta=-1, xi=1)          # time-reversal parities
KINDS = ('n', 'N', 'h')
HSYM = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

class Setup:
    def __init__(self, fields, sym, momenta):
        self.fields, self.sym = fields, sym
        if momenta == 'plane':
            a, b, c = sp.symbols('a b c'); self.MOM = [a, b, c]
            self.KV = [sp.Matrix([a, 0, 0]), sp.Matrix([b, c, 0]), sp.Matrix([-a - b, -c, 0])]
        else:
            A = sp.symbols('a1:4'); B = sp.symbols('b1:4'); self.MOM = list(A) + list(B)
            self.KV = [sp.Matrix(A), sp.Matrix(B), -sp.Matrix(A) - sp.Matrix(B)]
        self.WV = [w1, w2, -w1 - w2]
        self.XI = sp.Matrix(sp.symbols('xi0:3'))
        self.F = []
        for s in range(3):
            if fields == 'scalar':
                n, B_, p, E = sp.symbols(f'n{s+1} B{s+1} p{s+1} E{s+1}')
                k = self.KV[s]
                self.F.append(dict(n=n, N=k*B_, h=2*p*I3 + 2*k*k.T*E, syms=[n, B_, p, E], pot=(n, B_, p, E)))
            else:
                n = sp.Symbol(f'n{s+1}'); N = sp.Matrix(sp.symbols(f'N{s+1}_0:3')); hs = sp.symbols(f'h{s+1}_0:6')
                h = sp.Matrix(3, 3, lambda i, j: hs[HSYM.index((min(i, j), max(i, j)))])
                self.F.append(dict(n=n, N=N, h=h, syms=[n] + list(N) + list(hs)))
        extra = [zeta, chi] if fields == 'scalar' else [zeta] + list(self.XI)
        self.GENS = self.MOM + [w1, w2] + extra + [x for f in self.F for x in f['syms']]

    # ---- index structures: pairings (rotation) or even blocks (hyperoctahedral) ----
    def structures(self, pos):
        pos = list(pos)
        if not pos: yield []; return
        p0, rest = pos[0], pos[1:]
        sizes = [1] if self.sym == 'iso' else range(1, len(rest) + 1, 2)
        for size in sizes:
            for comb in itertools.combinations(rest, size):
                left = [x for x in rest if x not in comb]
                for m in self.structures(left): yield [(p0,) + comb] + m
    @staticmethod
    def contract(factors, blocks, nfree=0, free_vals=()):
        R = sum(r for r, _ in factors); tot = R + nfree; expr = 0
        for vals in itertools.product(range(3), repeat=len(blocks)):
            assign = [None]*tot; ok = True
            for i in range(nfree): assign[R + i] = free_vals[i]
            for blk, v in zip(blocks, vals):
                for x in blk:
                    if assign[x] is not None and assign[x] != v: ok = False
                    assign[x] = v
            if not ok: continue
            term = 1; p = 0
            for r, f in factors:
                term *= f(tuple(assign[p:p + r])); p += r
                if term == 0: break
            expr += term
        return expr

    # ---- the member's quadratic action: cross term L2(X+Y)-L2(X)-L2(Y) = E(Y).X ----
    @staticmethod
    def cross(X, Y):
        def Hd(F): return F['w']*F['h'] - F['k']*F['N'].T - F['N']*F['k'].T
        def R1(F): return (F['k'].T*F['h']*F['k'])[0] - (F['k'].T*F['k'])[0]*F['h'].trace()
        HX, HY = Hd(X), Hd(Y)
        kin = sp.Rational(1, 2)*((HX*HY).trace() - HX.trace()*HY.trace())
        nr = X['n']*R1(Y) + Y['n']*R1(X)
        kx, ky, hx, hy = X['k'], Y['k'], X['h'], Y['h']; kk = (kx.T*ky)[0]
        r2 = (-sp.Rational(1, 2)*kk*(hx*hy).trace() + ((hx*kx).T*(hy*ky))[0]
              - sp.Rational(1, 2)*(((hx*kx).T*ky)[0]*hy.trace() + ((hy*ky).T*kx)[0]*hx.trace())
              + sp.Rational(1, 2)*kk*hx.trace()*hy.trace())
        return sp.expand(kin + nr + r2)
    def fobj(self, s):
        F = self.F[s]; return dict(n=F['n'], N=F['N'], h=F['h'], k=self.KV[s], w=self.WV[s])

    def factor(self, kind, slot, tau, s):
        r = RANK[kind]; F = self.F[slot]; k = self.KV[slot]; wv = self.WV[slot] if tau else 1
        base = {'n': lambda i: F['n'], 'N': lambda i: F['N'][i[0]], 'h': lambda i: F['h'][i[0], i[1]]}[kind]
        def f(idx):
            v = base(idx[:r])*wv
            for m in range(s): v *= k[idx[r + m]]
            return v
        return (r + s, f)
    def eps(self, kind, tau, s):
        k = self.KV[0]; wv = self.WV[0] if tau else 1
        if kind == 'zeta': return (s, lambda idx: zeta*wv*sp.Mul(*[k[i] for i in idx]))
        xi = (k*chi) if self.fields == 'scalar' else self.XI
        return (1 + s, lambda idx: xi[idx[0]]*wv*sp.Mul(*[k[i] for i in idx[1:]]))
    def delta0_slot1(self, expr):
        k, w = self.KV[0], self.WV[0]; F = self.F[0]
        if self.fields == 'scalar':
            n, B_, p, E = F['pot']
            sub = {n: w*zeta, B_: w*chi - zeta, p: 0, E: chi}
        else:
            Nn = w*self.XI - k*zeta; hn = k*self.XI.T + self.XI*k.T
            sub = {F['n']: w*zeta}
            for i in range(3): sub[F['N'][i]] = Nn[i]
            for (i, j), sy in zip(HSYM, F['syms'][4:]): sub[sy] = hn[i, j]
        return sp.expand(expr.subs(sub, simultaneous=True))

    # ---- enumerations ----
    def v3(self):
        out = []
        for kinds in itertools.combinations_with_replacement(KINDS, 3):
            for der in itertools.product([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)], repeat=3):
                if sum(t + s for t, s in der) != 2: continue
                if (sum(t for t, _ in der) + kinds.count('N')) % 2: continue
                R = sum(RANK[k] + s for k, (t, s) in zip(kinds, der))
                if R % 2: continue
                for m in self.structures(range(R)): out.append((kinds, der, tuple(m)))
        return out
    def v3_symbol(self, mono):
        kinds, der, m = mono; tot = 0
        for perm in itertools.permutations(range(3)):
            tot += self.contract([self.factor(k, perm[j], t, s) for j, (k, (t, s)) in enumerate(zip(kinds, der))], list(m))
        return sp.expand(tot)
    def out_field(self, facs, m, ok, k, w):
        ro = RANK[ok]; comp = {fv: self.contract(facs, list(m), nfree=ro, free_vals=fv) for fv in itertools.product(range(3), repeat=ro)}
        X = dict(n=0, N=sp.zeros(3, 1), h=sp.zeros(3), k=k, w=w)
        if ok == 'n': X['n'] = comp[()]
        elif ok == 'N': X['N'] = sp.Matrix([comp[(i,)] for i in range(3)])
        else: X['h'] = sp.Matrix(3, 3, lambda i, j: (comp[(i, j)] + comp[(j, i)])/2)
        return X
    def d1(self):
        out = []
        for ek in ('zeta', 'xi'):
            for fk in KINDS:
                for where in ('eps', 'phi'):
                    for tau, s in ((1, 0), (0, 1)):
                        for ok in KINDS:
                            if PAR[ok] != PAR[ek]*PAR[fk]*(-1)**tau: continue
                            R = RANK[ek] + RANK[fk] + s + RANK[ok]
                            if R % 2: continue
                            for m in self.structures(range(R)): out.append((ek, fk, where, tau, s, ok, tuple(m)))
        return out
    def d1_symbol(self, mono):
        ek, fk, where, tau, s, ok, m = mono; tot = 0
        for ps, es in ((1, 2), (2, 1)):
            te, se = (tau, s) if where == 'eps' else (0, 0)
            tp, sp_ = (tau, s) if where == 'phi' else (0, 0)
            X = self.out_field([self.eps(ek, te, se), self.factor(fk, ps, tp, sp_)], m, ok, self.KV[0] + self.KV[ps], self.WV[0] + self.WV[ps])
            tot += self.cross(X, self.fobj(es))
        return sp.expand(tot)
    def fr(self):
        out = []
        for k1, k2 in itertools.combinations_with_replacement(KINDS, 2):
            for ok in KINDS:
                if PAR[ok] != PAR[k1]*PAR[k2]: continue
                R = RANK[k1] + RANK[k2] + RANK[ok]
                if R % 2: continue
                for m in self.structures(range(R)): out.append((k1, k2, ok, tuple(m)))
        return out
    def fr_symbol(self, mono):
        k1, k2, ok, m = mono; tot = 0
        for e in range(3):
            s1, s2 = [x for x in range(3) if x != e]
            for u, v in ((s1, s2), (s2, s1)):
                X = self.out_field([self.factor(k1, u, 0, 0), self.factor(k2, v, 0, 0)], m, ok, self.KV[u] + self.KV[v], self.WV[u] + self.WV[v])
                tot += self.cross(X, self.fobj(e))
        return sp.expand(tot)

    # ---- the comparator: third-order part of N sqrt(g)(K K - K^2 + R) ----
    def comparator(self, part='all'):
        KV, WV = self.KV, self.WV
        class Mm:
            def __init__(s, d=None): s.d = {k: v for k, v in (d or {}).items() if v != 0}
            def __add__(s, o):
                o = o if isinstance(o, Mm) else Mm({(0, 0, 0): sp.sympify(o)}); d = dict(s.d)
                for k, v in o.d.items(): d[k] = d.get(k, 0) + v
                return Mm(d)
            __radd__ = __add__
            def __neg__(s): return Mm({k: -v for k, v in s.d.items()})
            def __sub__(s, o): return s + (-(o if isinstance(o, Mm) else Mm({(0, 0, 0): sp.sympify(o)})))
            def __mul__(s, o):
                if not isinstance(o, Mm): return Mm({k: v*o for k, v in s.d.items()})
                d = {}
                for k1, v1 in s.d.items():
                    for k2, v2 in o.d.items():
                        k = tuple(x + y for x, y in zip(k1, k2))
                        if max(k) > 1: continue
                        d[k] = d.get(k, 0) + v1*v2
                return Mm(d)
            __rmul__ = __mul__
            def dx(s, i): return Mm({k: v*sum(e*KV[q][i] for q, e in enumerate(k)) for k, v in s.d.items()})
            def dt(s): return Mm({k: v*sum(e*WV[q] for q, e in enumerate(k)) for k, v in s.d.items()})
        one = Mm({(0, 0, 0): 1}); Z = Mm()
        def mk(s, v): e = [0, 0, 0]; e[s] = 1; return Mm({tuple(e): v})
        n = Z; Nv = [Z]*3; h = [[Z]*3 for _ in range(3)]
        for s in range(3):
            F = self.F[s]; n = n + mk(s, F['n'])
            for i in range(3):
                Nv[i] = Nv[i] + mk(s, F['N'][i])
                for j in range(3): h[i][j] = h[i][j] + mk(s, F['h'][i, j])
        hh = [[sum((h[i][k]*h[k][j] for k in range(3)), Z) for j in range(3)] for i in range(3)]
        gi = [[(one if i == j else Z) - h[i][j] + hh[i][j] for j in range(3)] for i in range(3)]
        trh = h[0][0] + h[1][1] + h[2][2]; trhh = hh[0][0] + hh[1][1] + hh[2][2]
        hhh = sum((hh[i][k]*h[k][i] for i in range(3) for k in range(3)), Z)
        sqg = one + trh*sp.Rational(1, 2) + trh*trh*sp.Rational(1, 8) - trhh*sp.Rational(1, 4) + trh*trh*trh*sp.Rational(1, 48) - trh*trhh*sp.Rational(1, 8) + hhh*sp.Rational(1, 6)
        dg = [[[h[i][j].dx(l) for l in range(3)] for j in range(3)] for i in range(3)]
        G = [[[sum((gi[k][l]*(dg[l][j][i] + dg[l][i][j] - dg[i][j][l]) for l in range(3)), Z)*sp.Rational(1, 2) for j in range(3)] for i in range(3)] for k in range(3)]
        Ric = [[sum((G[k][i][j].dx(k) - G[k][i][k].dx(j) for k in range(3)), Z) + sum((G[k][k][l]*G[l][i][j] - G[k][j][l]*G[l][i][k] for k in range(3) for l in range(3)), Z) for j in range(3)] for i in range(3)]
        R = sum((gi[i][j]*Ric[i][j] for i in range(3) for j in range(3)), Z)
        DN = [[Nv[j].dx(i) - sum((G[k][i][j]*Nv[k] for k in range(3)), Z) for j in range(3)] for i in range(3)]
        Kl = [[(h[i][j].dt() - DN[i][j] - DN[j][i])*(one - n + n*n)*sp.Rational(1, 2) for j in range(3)] for i in range(3)]
        Ku = [[sum((gi[i][k]*gi[j][l]*Kl[k][l] for k in range(3) for l in range(3)), Z) for j in range(3)] for i in range(3)]
        KK = sum((Kl[i][j]*Ku[i][j] for i in range(3) for j in range(3)), Z)
        Kt = sum((gi[i][j]*Kl[i][j] for i in range(3) for j in range(3)), Z)
        if part == 'all': L = (one + n)*sqg*(KK - Kt*Kt + R)
        elif part == 'R': L = sqg*R                      # the lengths' curvature, lapse one
        elif part == 'nR': L = n*sqg*R                   # the lapse times the curvature
        elif part == 'kin': L = (one + n)*sqg*(KK - Kt*Kt)   # the kinetic part with its 1/N
        return L

    def mat(self, exprs):
        polys = [sp.Poly(e, *self.GENS).as_dict() if e != 0 else {} for e in exprs]
        keys = sorted({k for p in polys for k in p}); idx = {k: i for i, k in enumerate(keys)}
        rows = [[QQ(0)]*len(exprs) for _ in keys]
        for j, p in enumerate(polys):
            for k, v in p.items(): r = sp.Rational(v); rows[idx[k]][j] = QQ(r.p, r.q)
        return DomainMatrix(rows, (len(keys), len(exprs)), QQ)
    def rank(self, e): return self.mat(e).rank() if e else 0

    def classify(self, vfilter=None):
        V = self.v3()
        if vfilter: V = [m for m in V if vfilter(m)]
        Vs = [self.v3_symbol(m) for m in V]
        Ds = [self.d1_symbol(m) for m in self.d1()]
        Fs = [self.fr_symbol(m) for m in self.fr()]
        _, piv = self.mat(Vs).rref(); Vb = [Vs[i] for i in piv]
        _, pf = self.mat(Fs).rref(); Fb = [Fs[i] for i in pf]
        ns = self.mat([self.delta0_slot1(s) for s in Vb] + Ds).nullspace().to_Matrix()
        sol = []
        for r in range(ns.rows):
            cv = ns.row(r)[:len(Vb)]
            if any(x != 0 for x in cv): sol.append(sp.expand(sum(cv[i]*Vb[i] for i in range(len(Vb)) if cv[i] != 0)))
        r_sol = self.rank(sol); r_both = self.rank(sol + Fb)
        return dict(nV=len(V), indepV=len(Vb), consistent=r_sol, redef=len(Fb), union=r_both, classes=r_both - len(Fb), sol=sol, Fb=Fb, V=V)

def report(label, S, R, full_expect):
    Lc = S.comparator(); Vc = sp.expand(Lc.d.get((1, 1, 1), 0))
    cons = S.rank(R['sol'] + [Vc]) == R['consistent']
    nontriv = S.rank(R['Fb'] + [Vc]) > R['redef']
    inv = []
    if R['sol']:
        nsi = S.mat([S.delta0_slot1(v) for v in R['sol']]).nullspace().to_Matrix()
        inv = [sp.expand(sum(nsi[r, i]*R['sol'][i] for i in range(len(R['sol'])))) for r in range(nsi.rows)]
    ninv = S.rank(inv + R['Fb']) - R['redef']
    print(f"   {label}: vertices {R['nV']} -> {R['indepV']} independent; consistent {R['consistent']}; redefinitions {R['redef']} (all consistent: {R['union'] == R['consistent']}); classes {R['classes']}; strictly invariant classes {ninv}; {time.time()-T0:.0f}s", flush=True)
    check(f"{label}: redefinitions lie in the consistent space", R['union'] == R['consistent'])
    check(f"{label}: the comparator's cubic vertex is consistent and nontrivial", cons and nontriv)
    check(f"{label}: number of classes = {full_expect}", R['classes'] == full_expect, f"{R['classes']}")
    check(f"{label}: no strictly gauge-invariant class", ninv == 0)
    return Vc

def describe(mono):
    kinds, der, blocks = mono
    lab = {}
    for bi, blk in enumerate(blocks):
        for x in blk: lab[x] = 'ijklmnop'[bi]
    out = []; pos = 0
    for k, (t, s) in zip(kinds, der):
        r = RANK[k]
        idx = ''.join(lab[pos + q] for q in range(r)); dix = ''.join(lab[pos + r + q] for q in range(s)); pos += r + s
        out.append(('dt ' if t else '') + ''.join(f'd{x} ' for x in dix) + {'n': 'n', 'N': f'N{idx}', 'h': f'h{idx}'}[k])
    return ' * '.join(out)
VN = [(-2, 'n * dj hii * dk hjk'), (1, 'n * dj hii * dj hkk'), (1, 'n * di hij * dk hjk')]          # n |d_i h_ij - d_j tr h|^2
VH = [(3, 'hii * hjj * dl dl hkk'), (-4, 'hii * hjj * dk dl hkl'), (-10, 'hii * hjk * dl dl hjk'), (12, 'hii * hjk * dk dl hjl'),
      (-3, 'hij * hij * dl dl hkk'), (4, 'hij * hij * dk dl hkl'), (12, 'hij * hik * dl dl hjk'), (-14, 'hij * hik * dk dl hjl')]
def vertex(S, R, terms):
    tot = 0
    for coef, d in terms:
        hits = [m for m in R['V'] if describe(m) == d]
        assert hits, d
        tot += coef*S.v3_symbol(hits[0])
    return sp.expand(tot)

print("== A  the member and the comparator's quadratic part")
S = Setup('full', 'iso', 'plane')
k = sp.Matrix(sp.symbols('q1:4')); w = sp.Symbol('om'); ys = sp.symbols('y0:10')
Y = dict(n=ys[0], N=sp.Matrix(ys[1:4]), h=sp.Matrix(3, 3, lambda i, j: ys[4 + HSYM.index((min(i, j), max(i, j)))]), k=-k, w=-w)
xi_ = sp.Matrix(sp.symbols('x1:4')); z = sp.Symbol('z')
check("A1 member invariant under relabelling in time (du = zeta-dot, dN = -grad zeta) for every field", S.cross(dict(n=w*z, N=-k*z, h=sp.zeros(3), k=k, w=w), Y) == 0)
check("A2 member invariant under spatial relabelling (dh = d xi + d xi^T, dN = xi-dot) for every field", S.cross(dict(n=0, N=w*xi_, h=k*xi_.T + xi_*k.T, k=k, w=w), Y) == 0)
Lc = S.comparator()
a_, b_, c_ = S.MOM
sub = {b_: -a_, c_: 0, w2: -w1}
q12 = sp.expand(Lc.d.get((1, 1, 0), 0))
check("A3 quadratic part of N sqrt(g)(K K - K^2 + R) equals the member (block 144 T1), all ten field components",
      sp.expand(q12.subs(sub) - S.cross(S.fobj(0), S.fobj(1)).subs(sub)) == 0)

print("== B  scalar sector, rotation-invariant (planar momenta, WLOG by rotation invariance)")
SB = Setup('scalar', 'iso', 'plane'); RB = SB.classify()
report("B scalar/iso", SB, RB, 4)
print("   sectors (classes realisable with the listed vertices only):")
for lab, flt in (("no shift factor", lambda m: 'N' not in m[0]), ("no lapse factor", lambda m: 'n' not in m[0]),
                 ("lengths only", lambda m: set(m[0]) <= {'h'}), ("no time derivative", lambda m: sum(t for t, _ in m[1]) == 0)):
    R_ = SB.classify(flt); print(f"     {lab}: consistent {R_['consistent']}, classes {R_['union'] - RB['redef']}", flush=True)
R_h = SB.classify(lambda m: set(m[0]) <= {'h'})
check("B5 a static lengths-only class exists in the scalar sector (not the comparator, which needs the lapse)", R_h['union'] - RB['redef'] >= 1)
VcB = sp.expand(SB.comparator().d.get((1, 1, 1), 0)); VnB = vertex(SB, RB, VN); VhB = vertex(SB, RB, VH)
for lab, v in (("V_n = n |d_i h_ij - d_j tr h|^2", VnB), ("V_h (eight-term static lengths-only cubic)", VhB)):
    check(f"B6 {lab}: consistent and nontrivial in the scalar sector",
          SB.rank(RB['sol'] + [v]) == RB['consistent'] and SB.rank(RB['Fb'] + [v]) > RB['redef'])
check("B7 comparator, V_n and V_h are independent classes", SB.rank(RB['Fb'] + [VcB, VnB, VhB]) - RB['redef'] == 3)
p_, E_ = SB.F[0]['pot'][2], SB.F[0]['pot'][3]
vB = sp.expand(SB.KV[0]*0)
k0 = SB.KV[0]; h0 = SB.F[0]['h']
vvec = sp.expand(h0*k0 - k0*h0.trace())
check("B8 on scalar configurations d_i h_ij - d_j tr h = -4 d_j psi (psi = p): invariant under longitudinal relabellings only",
      sp.simplify(vvec + 4*k0*p_) == sp.zeros(3, 1))

print("== C  full configurations, rotation-invariant (validation: known uniqueness of the comparator's vertex)")
SC = Setup('full', 'iso', 'plane'); RC = SC.classify()
report("C full/iso", SC, RC, 1)
VnC = vertex(SC, RC, VN); VhC = vertex(SC, RC, VH)
check("C5 V_n and V_h are not consistent once all configurations are allowed (scalar-sector artefacts)",
      SC.rank(RC['sol'] + [VnC]) > RC['consistent'] and SC.rank(RC['sol'] + [VhC]) > RC['consistent'])

print("== D  scalar sector, cubic-symmetric (general momenta)")
SD = Setup('scalar', 'cubic', 'general'); RD = SD.classify()
report("D scalar/cubic", SD, RD, 4)
RDi = SD.classify(lambda m: all(len(b) == 2 for b in m[2]))
check("D5 the rotation-invariant classes span the cubic-symmetric classes (anisotropy adds none)",
      SD.rank(RDi['sol'] + RD['Fb']) - RD['redef'] == RD['classes'], f"{SD.rank(RDi['sol'] + RD['Fb']) - RD['redef']}")

if '--skip-E' not in sys.argv:
    print("== E  full configurations, cubic-symmetric (general momenta) [long]")
    SE = Setup('full', 'cubic', 'general'); RE = SE.classify()
    report("E full/cubic", SE, RE, 1)

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PARTIAL (exact, leading order in the spacing): the scalar-sector first-order problem has 4 classes modulo local "
          "field redefinitions (rotation-invariant or cubic-symmetric alike), one of them the comparator's; none is strictly invariant; "
          "the unrestricted problem has exactly 1 (the comparator's). So the pre-registered 'one-dimensional continuum part' cannot "
          "hold in the scalar sector even for the comparator; exact lattice lift (range 1-2) not computed")
    print("HIT scalar-sector restriction is not selective: 4 first-order classes (comparator + 3) vs 1 in the full sector, exact over Q")
