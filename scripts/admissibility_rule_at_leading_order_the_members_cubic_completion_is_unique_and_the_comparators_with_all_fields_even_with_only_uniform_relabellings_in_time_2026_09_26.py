#!/usr/bin/env python3
"""Exact checks: at leading order in the spacing the member's first-order cubic completion is unique and is the comparator's
once all fields are kept, even with relabellings in time only for uniform clock profiles - within the member at alpha = K/4,
beta = -alpha with the bond shift (blocks 62, 101, 124, 136 and 144 as landed): delta0 V3 + delta1 S2 = 0 over local cubic
two-derivative T-even vertices, modulo local field redefinitions (a harvest of probe #9283's machinery and counts, with the
supervisor's variants for the readings of relabellings in time; not adopted).

A (the member): invariance of the quadratic member under both relabellings; the comparator's quadratic part equals it.
B (scalar sector, both relabellings): 4 classes; V_n and V_h consistent there; the comparator's vertex among them.
C (all fields, both relabellings): 1 class, the comparator's; V_n and V_h not consistent.
D (the readings): all fields with relabellings in time only at zero spatial momentum: 1 class; with none: 5; scalar sector: 5 and 8.
Exact rational arithmetic (sympy, domain matrices over Q); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_AT_LEADING_ORDER_THE_MEMBERS_CUBIC_COMPLETION_IS_UNIQUE_AND_THE_COMPARATORS_WITH_ALL_FIELDS_EVEN_WITH_ONLY_UNIFORM_RELABELLINGS_IN_TIME_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "time_relabelling_forged": "A",
    "scalar_count_forged": "B",
    "full_count_forged": "C",
    "uniform_variant_count_forged": "D",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()

# ============================================================================================ probe #9283's machinery (ported)
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

def _unused_report(label, S, R, full_expect):
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



class SetupNoTime(Setup):
    """Only spatial relabellings are required of the completion."""
    def delta0_slot1(self, expr):
        k, w = self.KV[0], self.WV[0]; F = self.F[0]
        if self.fields == 'scalar':
            n, B_, p, E = F['pot']
            sub = {n: 0, B_: w*chi, p: 0, E: chi}
        else:
            Nn = w*self.XI; hn = k*self.XI.T + self.XI*k.T
            sub = {F['n']: 0}
            for i in range(3): sub[F['N'][i]] = Nn[i]
            for (i, j), sy in zip(HSYM, F['syms'][4:]): sub[sy] = hn[i, j]
        return sp.expand(expr.subs(sub, simultaneous=True))
    def d1(self):
        return [m for m in super().d1() if m[0] == 'xi']


class SetupUniform(Setup):
    """Relabellings in time required only for spatially uniform profiles (zero spatial momentum)."""
    def _zeta_at_zero(self, expr):
        expr = sp.expand(expr)
        zpart = sp.expand(expr.coeff(zeta, 1)) * zeta
        rest = sp.expand(expr - zpart)
        return sp.expand(rest + zpart.subs(self.MOM[0], 0))
    def delta0_slot1(self, expr):
        return self._zeta_at_zero(super().delta0_slot1(expr))
    def d1_symbol(self, mono):
        s = super().d1_symbol(mono)
        return self._zeta_at_zero(s) if mono[0] == 'zeta' else s


def comparator_vertex(S):
    return sp.expand(S.comparator().d.get((1, 1, 1), 0))


def class_report(S, R):
    Vc = comparator_vertex(S)
    cons = S.rank(R['sol'] + [Vc]) == R['consistent']
    nontriv = S.rank(R['Fb'] + [Vc]) > R['redef']
    return Vc, cons, nontriv


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its relabellings and the comparator are supplied; the memo does not define a time metric)")
    S = Setup('full', 'iso', 'plane')
    k = sp.Matrix(sp.symbols('q1:4')); w = sp.Symbol('om'); ys = sp.symbols('y0:10')
    Y = dict(n=ys[0], N=sp.Matrix(ys[1:4]), h=sp.Matrix(3, 3, lambda i, j: ys[4 + HSYM.index((min(i, j), max(i, j)))]), k=-k, w=-w)
    xi_ = sp.Matrix(sp.symbols('x1:4')); z = sp.Symbol('z')
    lap = 2 if mut("time_relabelling_forged") else 1
    inv_t = S.cross(dict(n=lap*w*z, N=-k*z, h=sp.zeros(3), k=k, w=w), Y) == 0
    inv_s = S.cross(dict(n=0, N=w*xi_, h=k*xi_.T + xi_*k.T, k=k, w=w), Y) == 0
    Lc = S.comparator()
    a_, b_, c_ = S.MOM
    sub = {b_: -a_, c_: 0, w2: -w1}
    q12 = sp.expand(Lc.d.get((1, 1, 0), 0))
    same = sp.expand(q12.subs(sub) - S.cross(S.fobj(0), S.fobj(1)).subs(sub)) == 0
    checks.check("A3", inv_t and inv_s and same, "the quadratic member S2 is invariant under relabellings in time (dn = zeta-dot, dN = -grad zeta) and in space (dh = d xi + d xi^T, dN = xi-dot) for every field component, and equals the quadratic part of N sqrt(g)(K K - K^2 + R) on all ten components")


# ============================================================================================ family B
def family_b(checks: Checks):
    S = Setup('scalar', 'iso', 'plane'); R = S.classify()
    Vc, cons, nontriv = class_report(S, R)
    expect = 3 if mut("scalar_count_forged") else 4
    checks.check("B1", R['classes'] == expect and R['union'] == R['consistent'] and cons and nontriv,
                 f"scalar sector, both relabellings, rotation-invariant: {R['indepV']} independent vertices, consistent space {R['consistent']}, redefinitions {R['redef']}: {R['classes']} classes; the comparator's vertex is consistent and nontrivial ({time.time() - T0:.0f}s)")
    Vn = vertex(S, R, VN); Vh = vertex(S, R, VH)
    both = all(S.rank(R['sol'] + [v]) == R['consistent'] and S.rank(R['Fb'] + [v]) > R['redef'] for v in (Vn, Vh))
    indep = S.rank(R['Fb'] + [Vc, Vn, Vh]) - R['redef'] == 3
    checks.check("B2", both and indep, "in the scalar sector V_n = n |d_i h_ij - d_j tr h|^2 and an eight-term static lengths-only cubic V_h are consistent and nontrivial, and independent of the comparator's class")


# ============================================================================================ family C
def family_c(checks: Checks):
    S = Setup('full', 'iso', 'plane'); R = S.classify()
    Vc, cons, nontriv = class_report(S, R)
    expect = 2 if mut("full_count_forged") else 1
    Vn = vertex(S, R, VN); Vh = vertex(S, R, VH)
    art = S.rank(R['sol'] + [Vn]) > R['consistent'] and S.rank(R['sol'] + [Vh]) > R['consistent']
    checks.check("C1", R['classes'] == expect and R['union'] == R['consistent'] and cons and nontriv,
                 f"all fields, both relabellings, rotation-invariant: {R['indepV']} independent vertices, consistent space {R['consistent']}, redefinitions {R['redef']}: {R['classes']} class, the comparator's ({time.time() - T0:.0f}s)")
    checks.check("C2", art, "V_n and V_h are not consistent once all fields are kept: the scalar sector's extra classes are artefacts of the restriction")


# ============================================================================================ family D
def family_d(checks: Checks):
    out = {}
    for label, cls, fields in (("full, uniform", SetupUniform, 'full'), ("full, none", SetupNoTime, 'full'),
                               ("scalar, uniform", SetupUniform, 'scalar'), ("scalar, none", SetupNoTime, 'scalar')):
        S = cls(fields, 'iso', 'plane'); R = S.classify()
        Vc, cons, _ = class_report(S, R)
        out[label] = (R['classes'], cons, R['union'] == R['consistent'])
    expect_u = 5 if mut("uniform_variant_count_forged") else 1
    checks.check("D1", out["full, uniform"][0] == expect_u and out["full, uniform"][1] and out["full, uniform"][2],
                 f"all fields, relabellings in time required only at zero spatial momentum (uniform clock profiles): {out['full, uniform'][0]} class, the comparator's")
    checks.check("D2", out["full, none"][0] == 5 and out["full, none"][1],
                 f"all fields, no relabellings in time: {out['full, none'][0]} classes, the comparator's among them")
    checks.check("D3", out["scalar, uniform"][0] == 5 and out["scalar, none"][0] == 8,
                 f"scalar sector: {out['scalar, uniform'][0]} classes with uniform relabellings in time only, {out['scalar, none'][0]} with none ({time.time() - T0:.0f}s)")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 101, 124, 136 and 144 as landed on main (the member, its lapse and shift, its two relabellings and its quadratic action at the closing values); it reports the member's first-order cubic completion at leading order in the spacing; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at one class."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Gupta", "Kraichnan", "Feynman", "Boulware", "Wald", "Fierz", "Pauli",
                   "Arnowitt", "Misner", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Schur", "Fermi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 — one class with all fields", "## Theorem T1 — one class with all fields (after Deser)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - invariance of the quadratic member under both relabellings for every field component",
    "per_site: executed - the enumeration of cubic two-derivative T-even vertices and one-derivative deformations, rotation-invariant",
    "per_mode: executed - the consistent space and the redefinition quotient over Q, scalar sector and all fields",
    "per_block: executed - the readings: relabellings in time at zero spatial momentum only, and none",
    "lattice_wide: checked and not executed - the cubic-symmetric vertex classes (probe #9283's runs D and E), and the exact lattice lift at range 1-2",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: the member at alpha = K/4, beta = -alpha with the shift, leading order in the spacing; first-order cubic completions modulo field redefinitions: all fields with both relabellings 1 class (the comparator's), with relabellings in time only for uniform profiles 1, with none 5; scalar sector 4, 5 and 8; harvest of #9283 (unrefereed, same family) with supervisor variants; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
