#!/usr/bin/env python3
# h2_55_b — contraction identity; gauge-rotation expansion; colour factors; IR cancellation core; lattice non-flatness;
# xi^2 vertex antisymmetry. Criteria: h2_55_b_criteria.md (written, and its B1-F corrected, before this script).
import itertools
import sympy as sp
I = sp.I
results = []; controls = []
def gate(name, ok, detail=''):
    results.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
def control(name, fired, detail=''):
    controls.append(bool(fired)); print(f"{'FIRES' if fired else 'DOES-NOT-FIRE'}  {name}  {detail}")
def comm(X, Y): return X*Y - Y*X
def is_zero_mat(Mx): return all(sp.expand(e) == 0 for e in Mx)

# ---------------- B1: contraction identity at the jet level (su(2)) ----------------
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
T2 = [-I*s1/2, -I*s2/2, -I*s3/2]
c, al0 = sp.symbols('c alpha0')
R4 = range(4)
b  = [[sp.Symbol(f'b_{a}_{m}') for m in R4] for a in range(3)]
b1 = [[[sp.Symbol(f'b1_{a}_{m}_{n}') for n in R4] for m in R4] for a in range(3)]
b2 = {}
for a in range(3):
    for m in R4:
        for n in R4:
            for r in range(n, 4):
                b2[(a, m, n, r)] = sp.Symbol(f'b2_{a}_{m}_{n}{r}')
def B(m):            return sum((b[a][m]*T2[a] for a in range(3)), sp.zeros(2))
def dB(n, m):        return sum((b1[a][m][n]*T2[a] for a in range(3)), sp.zeros(2))          # d_n B_m
def ddB(r, n, m):    return sum((b2[(a, m, min(n, r), max(n, r))]*T2[a] for a in range(3)), sp.zeros(2))  # d_r d_n B_m
def G(cc, m, n, cG=None):
    k = cc if cG is None else cG
    return dB(m, n) - dB(n, m) + k*comm(B(m), B(n))
def dG(cc, r, m, n, cG=None):
    k = cc if cG is None else cG
    return ddB(r, m, n) - ddB(r, n, m) + k*(comm(dB(r, m), B(n)) + comm(B(m), dB(r, n)))
def Phi(cc, m, cG=None):
    out = sp.zeros(2)
    for n in R4:
        out += dG(cc, n, n, m, cG) + cc*comm(B(n), G(cc, n, m, cG))
    divB = sum((dB(n, n) for n in R4), sp.zeros(2))
    out += al0*(sum((ddB(m, n, n) for n in R4), sp.zeros(2)) + cc*comm(B(m), divB))
    return out
def E(cc):
    return sp.expand(sum((-2*(G(cc, m, n)*G(cc, m, n)).trace()/4 for m in R4 for n in R4), 0))
scale = {}
for a in range(3):
    for m in R4:
        scale[b[a][m]] = c*b[a][m]
        for n in R4: scale[b1[a][m][n]] = c*b1[a][m][n]
for k_, v_ in b2.items(): scale[v_] = c*v_
ok11 = all(is_zero_mat(G(1, m, n).subs(scale, simultaneous=True) - c*G(c, m, n)) for m in R4 for n in R4)
gate('B1.1 G^(1)(cB) = c G^(c)(B)', ok11)
ok12 = all(is_zero_mat(Phi(1, m).subs(scale, simultaneous=True) - c*Phi(c, m)) for m in R4)
gate('B1.2 Phi^(1)(cB) = c Phi^(c)(B) (alpha0 symbolic)', ok12)
E1 = E(1); Ec = E(c)
ok13 = sp.expand(E1.subs(scale, simultaneous=True) - c**2*Ec) == 0
gate('B1.3 E^(1)(cB) = c^2 E^(c)(B)', ok13)
G0syms = set().union(*[G(0, m, n).free_symbols for m in R4 for n in R4])
b1syms = {b1[a][m][n] for a in range(3) for m in R4 for n in R4}
E0 = sp.expand(E(0))
quad = all(sum(sp.degree(term, x) for x in E0.free_symbols) == 2 for term in sp.Add.make_args(E0))
gate('B1.4 c=0: G is abelian dB (only first jets), E is quadratic in first jets', G0syms <= b1syms and E0.free_symbols <= b1syms and quad)
# control B1-F (corrected before the script): commutator in G without c, covariant derivative with c
okF = all(is_zero_mat(Phi(1, m, cG=1).subs(scale, simultaneous=True) - c*Phi(c, m, cG=1)) for m in R4)
control('B1-F G built without c (D keeps c): scaling identity fails', not okF)

# ---------------- B2: gauge-rotation expansion (non-commutative) ----------------
lam, D, A = sp.symbols('lambda D A', commutative=False)
NMAX = 5
Om = sum((c**n*lam**n/sp.factorial(n) for n in range(NMAX)), sp.Integer(0))
Omi = sum(((-c)**n*lam**n/sp.factorial(n) for n in range(NMAX)), sp.Integer(0))
dOm = sum((c**n/sp.factorial(n)*sum((lam**i*D*lam**(n-1-i) for i in range(n)), sp.Integer(0)) for n in range(1, NMAX)), sp.Integer(0))
def by_c_degree(expr, maxdeg):
    expr = sp.expand(expr); out = {k: sp.Integer(0) for k in range(-1, maxdeg+1)}
    for term in sp.Add.make_args(expr):
        deg = 0; rest = []
        for f in sp.Mul.make_args(term):
            if f == c: deg += 1
            elif f.is_Pow and f.base == c: deg += int(f.exp)
            else: rest.append(f)
        if deg <= maxdeg: out[deg] += sp.Mul(*rest)
    return {k: sp.expand(v) for k, v in out.items()}
X = by_c_degree(dOm*Omi, 3)
C1 = lambda P_, Q_: P_*Q_ - Q_*P_
exp1 = D; exp2 = sp.Rational(1,2)*C1(lam, D); exp3 = sp.Rational(1,6)*C1(lam, C1(lam, D))
gate('B2.1 (dOmega)Omega^-1 = cD + c^2/2 [l,D] + c^3/6 [l,[l,D]]', X[0] == 0 and sp.expand(X[1]-exp1) == 0 and sp.expand(X[2]-exp2) == 0 and sp.expand(X[3]-exp3) == 0)
AOm = sp.expand(Om*(A + D)*Omi - (dOm*Omi)/c)
Y = by_c_degree(AOm, 2)
y0 = A; y1 = C1(lam, A) + sp.Rational(1,2)*C1(lam, D); y2 = sp.Rational(1,2)*C1(lam, C1(lam, A)) + sp.Rational(1,3)*C1(lam, C1(lam, D))
gate('B2.2 A^Omega coefficients c^0, c^1, c^2', sp.expand(Y[0]-y0) == 0 and sp.expand(Y[1]-y1) == 0 and sp.expand(Y[2]-y2) == 0, f'c^2 coeff = {sp.factor(Y[2]) if False else Y[2]}')
wrong = sp.Rational(1,2)*C1(lam, C1(lam, A)) + sp.Rational(1,2)*C1(lam, C1(lam, D))
control('B2-F "1/2 [l,[l,D]]" refuted by the series', sp.expand(Y[2]-wrong) != 0)

# ---------------- B3: colour factors ----------------
def gellmann():
    L = [sp.zeros(3) for _ in range(8)]
    L[0][0,1] = L[0][1,0] = 1
    L[1][0,1] = -I; L[1][1,0] = I
    L[2][0,0] = 1; L[2][1,1] = -1
    L[3][0,2] = L[3][2,0] = 1
    L[4][0,2] = -I; L[4][2,0] = I
    L[5][1,2] = L[5][2,1] = 1
    L[6][1,2] = -I; L[6][2,1] = I
    L[7][0,0] = L[7][1,1] = 1/sp.sqrt(3); L[7][2,2] = -2/sp.sqrt(3)
    return L
def fconst(Ts):
    n = len(Ts)
    return {(a, b_, d_): sp.nsimplify(sp.simplify(comm(Ts[a], Ts[b_]).multiply(Ts[d_]).trace()/(Ts[d_]*Ts[d_]).trace()))
            for a in range(n) for b_ in range(n) for d_ in range(n)}
def colour_checks(Ts, N):
    n = len(Ts)
    tr_ok = all(sp.simplify((Ts[a]*Ts[b_]).trace() - (-sp.Rational(1,2) if a == b_ else 0)) == 0 for a in range(n) for b_ in range(n))
    f = fconst(Ts)
    cas = all(sp.simplify(sum(f[(a, b_, d_)]*f[(d_, b_, e)] for b_ in range(n) for d_ in range(n)) - (-N if a == e else 0)) == 0 for a in range(n) for e in range(n))
    tot = sp.simplify(sum(f[k]**2 for k in f))
    return tr_ok, cas, tot, f
T3 = [-I*Lm/2 for Lm in gellmann()]
r2 = colour_checks(T2, 2); r3 = colour_checks(T3, 3)
gate('B3.1 tr T^a T^b = -delta/2 (SU(2), SU(3))', r2[0] and r3[0])
gate('B3.2 sum_bd f^abd f^dbe = -N delta (N = 2, 3)', r2[1] and r3[1])
gate('B3.3 sum f^2 = N(N^2-1) (6, 24)', r2[2] == 6 and r3[2] == 24, f'{r2[2]}, {r3[2]}')
T3bad = [-I*Lm for Lm in gellmann()]
fb = fconst(T3bad)
casb = sp.simplify(sum(fb[(0, b_, d_)]*fb[(d_, b_, 0)] for b_ in range(8) for d_ in range(8)))
control('B3-F generators -i lambda^a (no 1/2): sum f f = -4N delta, gate B3.2 fails', casb == -12 and casb != -3, f'(a=e=1) value {casb}')

# ---------------- B4: IR cancellation core ----------------
pv = sp.symbols('q1:5', real=True)  # here: the momentum p (named q-symbols to avoid clash)
p2 = sum(x**2 for x in pv)
contr = sp.simplify(sum((p2*(1 if i == j else 0) - pv[i]*pv[j])*((1 if i == j else 0) - pv[i]*pv[j]/p2) for i in R4 for j in R4))
gate('B4.1 (p^2 d - pp):(d - pp/p^2) = 3 p^2', sp.simplify(contr - 3*p2) == 0, f'{contr}')
ok4 = True; badsum = []
for (N, rr) in ((2, r2), (3, r3)):
    first = rr[2]/(N**2 - 1)                                  # sum f^2 / (N^2-1) = N
    f = rr[3]; n = N**2 - 1
    cas00 = sp.simplify(sum(f[(0, b_, d_)]*f[(d_, b_, 0)] for b_ in range(n) for d_ in range(n)))  # = -N
    second = 2*sp.Rational(1,2)*cas00
    ok4 = ok4 and sp.simplify(first - N) == 0 and sp.simplify(second + N) == 0 and sp.simplify(first + second) == 0
    badsum.append(sp.simplify(first + 2*1*cas00))
gate('B4.2 IR: first/tree = N, second/tree = -N, sum 0 (N=2,3)', ok4)
control('B4-F coefficient 1 for [l,[l,A_T]] gives sum -N != 0', all(x != 0 for x in badsum), f'{badsum}')

# ---------------- B5: lattice non-flatness (NOBS core) ----------------
Xs, Ys = sp.symbols('X Y')
gate('B5.0 abelian plaquette sum of corner differences = 0', sp.expand((Xs-0) + ((Xs+Ys)-Xs) + (Ys-(Xs+Ys)) + (0-Ys)) == 0)
a_, b_ = sp.symbols('a b', real=True)
def expi(theta, sig): return sp.cos(theta)*sp.eye(2) + I*sp.sin(theta)*sig   # exp(i theta sig), sig^2 = 1
Pm = expi(a_, s1)*expi(b_, s2)*expi(-a_, s1)*expi(-b_, s2)
val = sp.simplify(sp.expand(2 - Pm.trace()))
v_pi4 = sp.simplify(val.subs({a_: sp.pi/4, b_: sp.pi/4}))
gate('B5.1 2 - tr P not identically 0; value at a=b=pi/4 nonzero', val != 0 and v_pi4 != 0, f'2-trP = {sp.factor(sp.trigsimp(val))}; at pi/4: {v_pi4}')
Pc = expi(a_, s1)*expi(b_, s1)*expi(-a_, s1)*expi(-b_, s1)
valc = sp.simplify(sp.expand(2 - Pc.trace()))
control('B5-F commuting X, Y: 2 - tr P = 0 (flat)', valc == 0, f'{valc}')

# ---------------- B6: xi^2 vertex antisymmetry ----------------
qv = sp.symbols('k1:5', real=True); pp = sp.symbols('l1:5', real=True)   # q -> k, p -> l
ok61 = all(sp.expand(qv[m]*(pp[n]-qv[n]) - (pp[m]-qv[m])*qv[n] - (qv[m]*pp[n] - pp[m]*qv[n])) == 0 for m in R4 for n in R4)
gate('B6.1 q_m(p-q)_n - (p-q)_m q_n = q_m p_n - p_m q_n', ok61)
lhs = sp.expand(sum((qv[m]*pp[n] - pp[m]*qv[n])**2 for m in R4 for n in R4))
rhs = sp.expand(2*(sum(x**2 for x in qv)*sum(x**2 for x in pp) - sum(qv[i]*pp[i] for i in R4)**2))
gate('B6.2 sum (q_m p_n - p_m q_n)^2 = 2(q^2 p^2 - (q.p)^2)', sp.expand(lhs - rhs) == 0)
quadpart = sp.expand(qv[0]*(pp[1]-qv[1])).coeff(qv[0]*qv[1])
control('B6-F unsymmetrised vertex keeps -q_m q_n', quadpart == -1, f'coeff of q0 q1 = {quadpart}')

print(f"gates: {sum(results)}/{len(results)} pass; controls: {sum(controls)}/{len(controls)} fire")
print('VERDICT:', 'PASS' if all(results) and all(controls) else 'FAIL')
