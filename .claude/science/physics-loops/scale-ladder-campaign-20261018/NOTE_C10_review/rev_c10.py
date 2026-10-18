#!/usr/bin/env python3
"""Reviewer checks for the C10 lane note (fresh-context, same model family). Exact sympy; imports nothing from the runner.
R1  common-zero basis change: c'(m,n) = mu_m mu_n c(m,n)/mu_{m+n}, so Lambda'_n = mu_0 Lambda_n (ratios kept, (S) kept);
    the checker's 'Lambda_n unchanged' holds only when mu_0 = 1.  Position-space computation, L = 6, forward Delta.
R2  the disclosed post-hoc A1-U witness change: with X_4 = 3 the point has n_3 = 0 (not in U); with X_4 = 8 it is in U.
R3  P4b rational class by a different route: u-variables with g = 1 + Delta u written out (no chain rule), and radical
    membership of every coefficient kappa via Groebner(eqs + [1 - t kappa]) = [1] (instead of sympy.solve).
"""
import itertools, sympy as sp
from sympy import QQ
PASS = FAIL = 0
def check(n, ok, det=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {det}", flush=True)

# ---------------- R1
L = 6
om = sp.exp(2 * sp.pi * sp.I / L)
D = sp.zeros(L, L)
for x in range(L):
    D[x, (x + 1) % L] += 1; D[x, x] -= 1                    # forward difference
s = lambda x, y, z: D[x, y] * (z == x) - D[y, x] * (z == y)  # L4 Poisson form at g = 1 (zeroth-order constants)
mu = {0: sp.Rational(3, 2), 1: sp.Rational(-1, 3), 2: sp.Rational(1, 5), 5: sp.Rational(2, 7)}
M = sp.Matrix(L, L, lambda x, a: mu.get((a - x) % L, 0))     # C'_x = sum_a mu(a - x) C_a
Mi = M.inv()
sp_ = {}
for x in range(L):
    for y in range(L):
        for w_ in range(L):
            sp_[x, y, w_] = sp.nsimplify(sum(M[x, a] * M[y, b] * s(a, b, z) * Mi[z, w_]
                                            for a in range(L) for b in range(L) for z in range(L) if s(a, b, z) != 0))
cbar = lambda m, n, S: sp.simplify(sp.expand(sum(om**(m * x + n * y) * S(x, y, 0) for x in range(L) for y in range(L))))
mu0 = sum(mu.values())
mu_hat = lambda n: sp.simplify(sum(v * om**(-n * r) for r, v in mu.items()))
ok = True; okfull = True
for n in range(L):
    Lam = cbar(0, n, s); Lamp = cbar(0, n, lambda x, y, z: sp_[x, y, z])
    ok &= sp.simplify(Lamp - mu0 * Lam) == 0
for m in range(L):
    for n in range(L):
        c = cbar(m, n, s); cp = cbar(m, n, lambda x, y, z: sp_[x, y, z])
        okfull &= sp.simplify(cp * mu_hat((m + n) % L) - mu_hat(m) * mu_hat(n) * c) == 0
check("R1 common-zero basis change, L=6 forward: Lambda'_n = mu_0 Lambda_n for all n", ok, f"mu_0 = {mu0}")
check("R1b c'(m,n) = mu_m mu_n c(m,n)/mu_{m+n} for all (m,n); so (S) and every ratio Lambda_n/Lambda_1 are kept", okfull)
check("R1c the unscaled claim 'Lambda_n unchanged' fails here (mu_0 != 1)",
      sp.simplify(cbar(0, 1, lambda x, y, z: sp_[x, y, z]) - cbar(0, 1, s)) != 0)

# ---------------- R2
L = 5
f = sp.symbols("f0:5"); p = sp.symbols("p0:5"); X = sp.symbols("X0:5"); P = sp.symbols("P0:5")
Dc = sp.zeros(L, L)
for x in range(L):
    Dc[x, (x + 1) % L] += sp.Rational(1, 2); Dc[x, (x - 1) % L] -= sp.Rational(1, 2)
Dv = lambda v, i: sum(Dc[i, j] * v[j] for j in range(L))
# on l = k = 0: pi = -Delta X, P = Delta phi (hand solution); m = 2 Delta(phi - X), n = -2 Delta(phi + X)
for X4, want in ((3, False), (8, True)):
    vals = dict(zip(list(f) + list(X), [3, -1, 4, 1, -5, 9, 2, -6, 5, X4]))
    mv = [sp.sympify(2 * Dv([f[j] - X[j] for j in range(L)], i)).subs(vals) for i in range(L)]
    nv = [sp.sympify(-2 * Dv([f[j] + X[j] for j in range(L)], i)).subs(vals) for i in range(L)]
    # cross-check the hand solution against the definitions l, k, m, n
    a = [p[i] + Dv(f, i) for i in range(L)]; b = [p[i] - Dv(f, i) for i in range(L)]
    be = [P[i] - Dv(X, i) for i in range(L)]; ga = [P[i] + Dv(X, i) for i in range(L)]
    sol = {p[i]: -Dv(X, i) for i in range(L)}; sol.update({P[i]: Dv(f, i) for i in range(L)})
    okdef = all(sp.expand((a[i] - be[i]).subs(sol)) == 0 and sp.expand((b[i] + ga[i]).subs(sol)) == 0 for i in range(L))
    okdef &= all(sp.expand((a[i] + be[i]).subs(sol) - 2 * Dv([f[j] - X[j] for j in range(L)], i)) == 0 for i in range(L))
    okdef &= all(sp.expand((b[i] - ga[i]).subs(sol) + 2 * Dv([f[j] + X[j] for j in range(L)], i)) == 0 for i in range(L))
    inU = all(v != 0 for v in mv + nv)
    check(f"R2 A1-U witness with X_4 = {X4}: in U = {inU} (expected {want})", okdef and inU == want, f"m={mv}, n={nv}")

# ---------------- R3
def rational_class(Ra, Rg):
    span = 2 * Ra + Rg + 4
    L = 2 * span + 3
    Dd = lambda i, j: sp.Rational(1, 2) if (j - i) % L == 1 else (-sp.Rational(1, 2) if (j - i) % L == L - 1 else 0)
    a = sp.symbols(f"a0:{L}"); u = sp.symbols(f"u0:{L}")
    g = [1 + (u[(i + 1) % L] - u[(i - 1) % L]) / 2 for i in range(L)]
    pairs = [(r, s_) for r in range(-Ra, Ra + 1) for s_ in range(r, Ra + 1)]
    kap = {(r, s_, t): sp.Symbol(f"K{r+5}_{s_+5}_{t+5}") for (r, s_) in pairs for t in range(-Rg, Rg + 1)}
    h = lambda x: sum(v * a[(x + r) % L] * a[(x + s_) % L] / g[(x + t) % L] for (r, s_, t), v in kap.items())
    pa = lambda F, G: sum(2 * Dd(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dd(i, j) != 0)
    eqs = set()
    h0 = h(0)
    for y in range(1, span + 1):
        hy = h(y)
        Fy = sp.diff(h0, u[y]) - sp.diff(hy, u[0]) + pa(h0, hy)
        num = sp.expand(sp.fraction(sp.together(Fy))[0])
        if num == 0: continue
        gens = [v for v in list(a) + list(u) if num.has(v)]
        eqs.update(sp.expand(c) for c in sp.Poly(num, *gens).coeffs())
    eqs.discard(0)
    t = sp.Symbol("t")
    unk = list(kap.values())
    allzero = all(list(sp.groebner(list(eqs) + [1 - t * k], *(unk + [t]), order="grevlex", domain=QQ).exprs) == [1] for k in unk)
    return allzero, len(unk), len(eqs)
for Ra, Rg in [(1, 0), (1, 1)]:
    ok, nu, ne = rational_class(Ra, Rg)
    check(f"R3 rational class h = sum k a a/g_(x+t), Ra={Ra}, Rg={Rg}, explicit u: every kappa in the radical (only h = 0 flat)",
          ok, f"({nu} unknowns, {ne} eqs)")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
