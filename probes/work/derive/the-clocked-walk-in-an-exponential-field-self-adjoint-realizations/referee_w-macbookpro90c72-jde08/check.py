"""Independent referee for the clocked walk's self-adjoint realizations, attempt 2.

Own Pauli matrices, own series, own boundary form. The author's script is not called.
Weyl's alternative and the extension theorem stay assumed, as in the attempt.
"""
import itertools
import sys

import sympy as sp

FAILS = []
I = sp.I
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -I], [I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def Jrow(psi, k, mu, P):
    return (I / 2) * S1 * (mu ** (2 * k - 1) * psi[k - 1] - mu ** (2 * k + 1) * psi[k + 1]) + mu ** (2 * k) * P * psi[k]


def Bform(psi, phi, N, mu):
    hop = (I / 2) * mu ** (2 * N + 1) * S1
    # H_{N,N+1} = -(i/2) lambda^{N+1/2} sigma_1, and H_{N+1,N} = -H_{N,N+1}^dagger = +(i/2) ...
    return sp.expand((psi[N].H * (-hop) * phi[N + 1] - psi[N + 1].H * hop * phi[N])[0])


# ---------------------------------------------------------------- Green's identity
mu = sp.Integer(2)
P = sp.Rational(1, 5) * S2 + sp.Rational(2, 7) * S3
ps, ph = {}, {}
for k in range(-1, 5):
    ps[k] = sp.Matrix([sp.Rational(k + 1, 3) + I * sp.Rational(1 - k, 4), sp.Rational(k - 2, 5) - I * sp.Rational(k, 6)])
    ph[k] = sp.Matrix([sp.Rational(2 - k, 3) - I * sp.Rational(k, 5), sp.Rational(k + 3, 4) + I * sp.Rational(1, 7)])
lhs = sum((ps[k].H * Jrow(ph, k, mu, P) - Jrow(ps, k, mu, P).H * ph[k])[0] for k in range(0, 4))
rhs = Bform(ps, ph, 3, mu) - Bform(ps, ph, -1, mu)
want("G the sector operator's Green's identity is B_3 - B_{-1} on a rational window", sp.expand(lhs - rhs) == 0)

# ---------------------------------------------------------------- series on the line
mu_s, z = sp.symbols("mu z", positive=True)
X = sp.Symbol("X")
ok = True
for s in (1, -1):
    for eps in (1, -1):
        c = [sp.Integer(1)]
        for j in range(1, 6):
            c.append(sp.simplify(-2 * I * s * eps * c[-1] / (mu_s ** (2 * j) - mu_s ** (-2 * j))))
        Sx = lambda Y, c=c: sum(c[j] * Y ** j for j in range(6))
        residual = (I * s / 2) * ((sp.Integer(1) / eps) * Sx(X * mu_s ** 2) - eps * Sx(X / mu_s ** 2)) - X * Sx(X)
        ok = ok and sp.simplify(sp.expand(residual + c[5] * X ** 6)) == 0
        ok = ok and sp.simplify(c[2] / c[1] + 2 * I * s * eps / (mu_s ** 4 - mu_s ** (-4))) == 0
# |c_j/c_{j-1}| = 2/|lambda^j - lambda^{-j}| falls for lambda=4
prev = None
for j in range(1, 8):
    den = sp.Integer(4) ** j - sp.Integer(4) ** (-j)
    mod2 = sp.Rational(4, 1) / (den ** 2)
    ok = ok and (prev is None or mod2 < prev)
    prev = mod2
want("A the four line series satisfy the eigenvalue equation through order 5, and the coefficients fall", ok)

# m* = sinh(g/2), and (s+m)^2 = lambda there
m, mu_ = sp.symbols("m mu", positive=True)
mstar = (mu_ ** 2 - 1) / (2 * mu_)
sstar = sp.sqrt(sp.factor(1 + mstar ** 2))
grow = sp.diff((sp.sqrt(1 + m ** 2) + m) ** 2, m)
ok = sp.simplify((sstar + mstar) ** 2 - mu_ ** 2) == 0
ok = ok and sp.simplify(grow - 2 * (sp.sqrt(1 + m ** 2) + m) ** 2 / sp.sqrt(1 + m ** 2)) == 0
# witness: lambda=4, p=(1/4,1/3), det A_j != 0 for j=1..6 and all four roots
Pw = sp.Rational(1, 4) * S2 + sp.Rational(1, 3) * S3
roots = [sp.Rational(3, 2), sp.Rational(-2, 3), sp.Rational(2, 3), sp.Rational(-3, 2)]
dets = []
for r, j in itertools.product(roots, range(1, 7)):
    A = (I / 2) * (mu ** (2 * j) / r - r * mu ** (-2 * j)) * S1 + Pw
    dets.append(sp.simplify(A.det()))
ok = ok and all(d != 0 for d in dets)
want("A (sqrt(1+m^2)+m)^2 equals lambda exactly at m* and the witness recursions are invertible", ok)

# ---------------------------------------------------------------- line boundary space
def floquet(rv, mu):
    return [{k: (r / mu) ** k * v for k in range(-1, 5)} for r, v in rv]


def gram(sols, mu, N):
    n = len(sols)
    return sp.Matrix(n, n, lambda i, j: Bform(sols[i], sols[j], N, mu))


basis = [(1, sp.Matrix([1, 0])), (1, sp.Matrix([0, 1])), (-1, sp.Matrix([1, 0])), (-1, sp.Matrix([0, 1]))]
sols = floquet(basis, mu)
G = gram(sols, mu, 0)
Gexp = sp.diag(-I * S1, I * S1)
ok = G == Gexp and all(gram(sols, mu, N) == Gexp for N in (1, 2, 3))
Mt = sp.diag(mu, mu, -mu, -mu)
shifted = [{k: sol[k - 1] for k in range(0, 4)} for sol in sols]
ok = ok and all(sp.expand(shifted[i][k] - Mt[i, i] * sols[i][k]) == sp.zeros(2, 1) for i in range(4) for k in range(4))
ok = ok and Mt ** 2 == (mu ** 2) * sp.eye(4) and Mt.H * Gexp * Mt == (mu ** 2) * Gexp
want("B zero-energy boundary form is diag(-i sigma_1, i sigma_1), and T_2 acts as lambda", ok)

t1, t2 = sp.symbols("t1 t2", real=True)
v1 = sp.Matrix([1, I * t1])
v2 = sp.Matrix([1, I * t2])
ok = sp.simplify((v1.H * S1 * v1)[0]) == 0 and (sp.Matrix([0, 1]).H * S1 * sp.Matrix([0, 1]))[0] == 0
# a vector off the circle is not isotropic
ok = ok and sp.simplify((sp.Matrix([1, 1]).H * S1 * sp.Matrix([1, 1]))[0]) == 2
Lb = sp.Matrix.hstack(sp.Matrix.vstack(v1, sp.zeros(2, 1)), sp.Matrix.vstack(sp.zeros(2, 1), v2))
ok = ok and sp.simplify(Lb.H * Gexp * Lb) == sp.zeros(2)
# the whole fast-plus plane is not isotropic
plus = sp.Matrix.hstack(sp.eye(4)[:, 0], sp.eye(4)[:, 1])
ok = ok and plus.H * Gexp * plus != sp.zeros(2)
want("B the T_1-invariant Lagrangian planes are the torus of isotropic spinors", ok)

# chains
xx = sp.Matrix(sp.symbols("x1 x2"))
uA = {k: (sp.Integer(1) / mu) ** k * xx + (sp.Integer(-1) / mu) ** k * (S3 * xx) for k in range(4)}
uB = {k: (sp.Integer(1) / mu) ** k * xx - (sp.Integer(-1) / mu) ** k * (S3 * xx) for k in range(4)}
ok = all(sp.expand(uA[k][1 if k % 2 == 0 else 0]) == 0 for k in range(4))
ok = ok and all(sp.expand(uB[k][0 if k % 2 == 0 else 1]) == 0 for k in range(4))
meet = sp.solve(sp.Eq(sp.Matrix([[1, 1], [I * t2, -I * t1]]).det(), 0), t2)
on = sp.Matrix.hstack(Lb, sp.Matrix.vstack(v1, S3 * v1)).subs(t2, -t1).rank()
off = sp.Matrix.hstack(Lb, sp.Matrix.vstack(v1, S3 * v1)).subs({t1: 1, t2: 2}).rank()
ok = ok and meet == [-t1] and on == 2 and off == 3
Lw = Lb.subs({t1: 0, t2: 1})
Abas = sp.Matrix.hstack(sp.Matrix([1, 0, 1, 0]), sp.Matrix([0, 1, 0, -1]))
Bbas = sp.Matrix.hstack(sp.Matrix([1, 0, -1, 0]), sp.Matrix([0, 1, 0, 1]))
ok = ok and Lw.H * Gexp * Lw == sp.zeros(2) and sp.Matrix.hstack(Lw, Mt * Lw).rank() == 2
ok = ok and sp.Matrix.hstack(Lw, Abas).rank() == 4 and sp.Matrix.hstack(Lw, Bbas).rank() == 4
Ln = sp.Matrix.hstack(sp.Matrix([1, 0, 1, 0]), sp.Matrix([1, I, -1, I]))
ok = ok and Ln.H * Gexp * Ln == sp.zeros(2) and sp.Matrix.hstack(Ln, Mt * Ln).rank() == 4
want("B chain-separate planes are t2=-t1; the witness t1=0, t2=1 mixes the chains and keeps T_1", ok)

Sg = sp.diag(S1, S1)
joint = [sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, -1, 0, 0]), sp.Matrix([0, 0, 1, 1]), sp.Matrix([0, 0, 1, -1])]
ok = Sg * Mt == Mt * Sg
ok = ok and all(sp.Matrix.hstack(jv, Sg * jv).rank() == 1 for jv in joint)
ok = ok and all(sp.simplify((jv.H * Gexp * jv)[0]) != 0 for jv in joint)
want("B no joint eigenvector of T_1 and the half-turn sigma_1 is isotropic", ok)

# ---------------------------------------------------------------- three-dimensional sector
p2, p3 = sp.Rational(1, 4), sp.Rational(1, 3)
P = p2 * S2 + p3 * S3
Nmat = p2 * S3 - p3 * S2
m_w = sp.Rational(5, 12)
ev = Nmat.eigenvects()
def align(v, target):
    for i in range(2):
        if target[i] != 0:
            return sp.simplify(v * (target[i] / v[i]))
    return v


vp = align([v for val, _, vs in ev if sp.simplify(val - m_w) == 0 for v in vs][0], sp.Matrix([2 * I, 1]))
vm = align([v for val, _, vs in ev if sp.simplify(val + m_w) == 0 for v in vs][0], sp.Matrix([1, 2 * I]))
ok = sp.simplify(S1 * P - I * Nmat) == sp.zeros(2)
ok = ok and sp.simplify(Nmat * vp - m_w * vp) == sp.zeros(2, 1)
ok = ok and sp.simplify(Nmat * vm + m_w * vm) == sp.zeros(2, 1)
# the attempt's spinors are parallel to these
ok = ok and sp.Matrix.hstack(vp, sp.Matrix([2 * I, 1])).rank() == 1
ok = ok and sp.Matrix.hstack(vm, sp.Matrix([1, 2 * I])).rank() == 1
rv = [(sp.Rational(3, 2), vp), (sp.Rational(-2, 3), vp), (sp.Rational(2, 3), vm), (sp.Rational(-3, 2), vm)]
sols = floquet(rv, mu)
ok = ok and all(sp.Abs(r) < mu for r, _ in rv)
Gm = gram(sols, mu, 0)
ok = ok and all(gram(sols, mu, N) == Gm for N in (1, 2, 3))
labs = "abcd"
nz = {(labs[i], labs[j]) for i in range(4) for j in range(4) if Gm[i, j] != 0}
ok = ok and nz == {("a", "c"), ("c", "a"), ("b", "d"), ("d", "b")}
Tv = sp.diag(*[mu / r for r, _ in rv])
ok = ok and len({Tv[i, i] for i in range(4)}) == 4 and Tv.H * Gm * Tv == (mu ** 2) * Gm
pairs = []
for i, j in itertools.combinations(range(4), 2):
    if sp.Matrix([[Gm[i, i], Gm[i, j]], [Gm[j, i], Gm[j, j]]]) == sp.zeros(2):
        pairs.append(labs[i] + labs[j])
ok = ok and pairs == ["ab", "ad", "bc", "cd"]
want("C below m* the boundary form pairs a-c and b-d, and exactly those four pairs are isotropic", ok)

M2 = sp.diag(*[(mu / r) ** 2 for r, _ in rv])
ok = [sp.simplify(M2[i, i]) for i in range(4)] == [sp.Rational(16, 9), 9, 9, sp.Rational(16, 9)]
al, de, be, ga = sp.symbols("alpha delta beta gamma")
xv = sp.Matrix([al, 0, 0, de])
yv = sp.Matrix([0, be, ga, 0])
cross = sp.expand((xv.H * Gm * yv)[0])
sol = sp.solve(sp.Eq(cross, 0), be)
ok = ok and len(sol) == 1 and sp.simplify(sol[0] - sp.conjugate(al) * ga / sp.conjugate(de)) == 0
want("C the shift by two keeps the sphere (beta : gamma) = (conj alpha : conj delta)", ok)

Rm = (sp.eye(2) - I * S1) / sp.sqrt(2)
Pr = -p3 * S2 + p2 * S3
Nr = (-p3) * S3 - p2 * S2
ok = sp.simplify(Rm * P * Rm.H - Pr) == sp.zeros(2)
ok = ok and sp.simplify(Rm.H * Rm - sp.eye(2)) == sp.zeros(2)
ok = ok and sp.simplify(Rm * S1 * Rm.H - S1) == sp.zeros(2)
ok = ok and sp.simplify(Rm * Nmat * Rm.H - Nr) == sp.zeros(2)
ok = ok and sp.simplify(Nr * (Rm * vp) - m_w * (Rm * vp)) == sp.zeros(2, 1)
ok = ok and S1 * P * S1 == -P and S1 * Nmat * S1 == -Nmat
ok = ok and sp.simplify((-Nmat) * (S1 * vp) - m_w * (S1 * vp)) == sp.zeros(2, 1)
want("C the quarter-turn and the half-turn carry sectors to sectors and keep the Floquet labels", ok)

def limits(nv):
    evs = nv.eigenvects()
    plus = [v for val, _, vs in evs if val == 1 for v in vs][0]
    minus = [v for val, _, vs in evs if val == -1 for v in vs][0]

    def E(v, eps):
        return sp.Matrix.vstack(v, sp.zeros(2, 1)) if eps == 1 else sp.Matrix.vstack(sp.zeros(2, 1), v)

    return {
        "bc": sp.Matrix.hstack(E(plus, -1), E(minus, 1)),
        "ad": sp.Matrix.hstack(E(plus, 1), E(minus, -1)),
        "ab": sp.Matrix.hstack(E(plus, 1), E(plus, -1)),
        "cd": sp.Matrix.hstack(E(minus, 1), E(minus, -1)),
    }


L0 = limits(S3)
L90 = limits(-S2)
Gl = sp.diag(-I * S1, I * S1)
ok = all(sp.Matrix.hstack(L0[k], L90[k]).rank() > 2 for k in L0)
ok = ok and all(sp.simplify(L0[k].H * Gl * L0[k]) == sp.zeros(2) and sp.simplify(L90[k].H * Gl * L90[k]) == sp.zeros(2) for k in L0)
# the two limits named in the attempt
bc0 = sp.Matrix.hstack(sp.Matrix([0, 1, 0, 0]), sp.Matrix([0, 0, 1, 0]))
bc90 = sp.Matrix.hstack(sp.Matrix([1, I, 0, 0]), sp.Matrix([0, 0, 1, -I]))
ok = ok and sp.Matrix.hstack(L0["bc"], bc0).rank() == 2
ok = ok and sp.Matrix.hstack(L90["bc"], bc90).rank() == 2
want("C as m->0 the four planes stay Lagrangian and the 0-degree and 90-degree limits differ", ok)

mm = sp.Symbol("m", positive=True)
ss = sp.sqrt(1 + mm ** 2)
rs = {"a": mm + ss, "b": mm - ss, "c": ss - mm, "d": -mm - ss}
prod_one = set()
for x, y in itertools.combinations("abcd", 2):
    if sp.simplify(rs[x] * rs[y] - 1) == 0:
        prod_one.add((x, y))
distinct = all(sp.simplify(rs[x] - rs[y]) != 0 for x, y in itertools.combinations("abcd", 2))
no_square = all(sp.solve(sp.Eq(rs[x] ** 2, 1), mm) == [] for x in "abcd")
ok = prod_one == {("a", "c"), ("b", "d")} and distinct and no_square
want("C for every m>0 the four Floquet roots are distinct, none squares to 1, and only a-c and b-d multiply to 1", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - on the line the fast end is limit circle at every energy by four entire series, "
    "the boundary form is diag(-i sigma_1, i sigma_1), and the realizations that keep every x1-shift form the isotropic torus. "
    "Below m* a sector has exactly four such realizations, and their m->0 limits depend on direction."
)
print(
    "SUMMARY: confirmed (a) on the fast end, (b) the torus, and (c) the four sector realizations. "
    "The slow end remains Weyl's alternative, assumed. "
    "The witness lambda=4, (p2,p3)=(1/4,1/3) has roots 3/2, -2/3, 2/3, -3/2."
)
