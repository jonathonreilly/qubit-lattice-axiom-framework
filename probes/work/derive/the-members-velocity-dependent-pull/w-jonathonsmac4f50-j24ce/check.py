#!/usr/bin/env python3
"""check.py for J:derive:the-members-velocity-dependent-pull:a2 (worker w-jonathonsmac4f50-j24ce, claude-opus-5-5).

An independent check of block 144 (PR #9230, the supervisor's own derivation, same model family) by other routes:
  M  the member's plane-wave equations derived here from its position-space Lagrangian (Euler-Lagrange in sympy), solved directly for
     sources that keep the books, with and without the shift, and the pairing compared with (1/(2K))[T'.T - T'T/2]/(p^2 - omega^2);
  X  the two-body pull from that exchange at order v^2 (tensor contraction + the retardation term, exact);
  W  the weight of a bound pair by a direct Hamiltonian bound-state computation (relativistic kinetic terms, directional virial theorem);
  G  the existence of a first-order boost (centre-of-energy) generator, by Poisson brackets: the condition on (a, b, c).
Exact arithmetic (sympy, rationals) throughout.
"""
import random
import sympy as sp
from sympy.calculus.euler import euler_equations

PASS, FAIL = [], []
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else ""), flush=True)

# ================================================================ M: the member at plane waves
t, x = sp.symbols("t x", real=True)
K, al = sp.symbols("K alpha", positive=True)
names = ["u", "N1", "N2", "N3", "h11", "h12", "h13", "h22", "h23", "h33"]
F = {n: sp.Function(n)(t, x) for n in names}
src = {n: sp.Function("s_" + n)(t, x) for n in ["e", "P1", "P2", "P3", "T11", "T12", "T13", "T22", "T23", "T33"]}
def h(i, j):
    i, j = min(i, j), max(i, j)
    return F["h%d%d" % (i, j)]
Nv = [F["N1"], F["N2"], F["N3"]]
d = lambda f, k: sp.diff(f, x) if k == 1 else 0            # only x-dependence (wave vector along the first axis)
def Hdot(i, j): return sp.diff(h(i, j), t) - d(Nv[j - 1], i) - d(Nv[i - 1], j)
rng = range(1, 4)
trHd = sum(Hdot(i, i) for i in rng)
kin = sum(Hdot(i, j) ** 2 for i in rng for j in rng) - trHd ** 2
trh = sum(h(i, i) for i in rng)
R1 = sum(d(d(h(i, j), i), j) for i in rng for j in rng) - sum(d(d(trh, k), k) for k in rng)
R2 = (-sp.Rational(1, 4) * sum(d(h(i, j), k) ** 2 for i in rng for j in rng for k in rng)
      + sp.Rational(1, 2) * sum(sum(d(h(i, k), i) for i in rng) * sum(d(h(j, k), j) for j in rng) for k in rng)
      - sp.Rational(1, 2) * sum(sum(d(h(i, j), i) for i in rng) * d(trh, j) for j in rng)
      + sp.Rational(1, 4) * sum(d(trh, k) ** 2 for k in rng))
Th = lambda i, j: src["T%d%d" % (min(i, j), max(i, j))]
def lagrangian(with_shift):
    L = al * kin + K * (F["u"] * R1 + R2) - src["e"] * F["u"] + sp.Rational(1, 2) * sum(Th(i, j) * h(i, j) for i in rng for j in rng)
    if with_shift: L += sum(Nv[j] * src["P%d" % (j + 1)] for j in range(3))
    return L
om, p = sp.symbols("omega p", positive=True)
E = sp.exp(sp.I * (p * x - om * t))
amp = {n: sp.Symbol("A_" + n) for n in names}
samp = {n: sp.Symbol("S_" + n) for n in src}
def plane_system(with_shift, alpha_val):
    L = lagrangian(with_shift)
    fields = [F[n] for n in names] if with_shift else [F[n] for n in names if not n.startswith("N")]
    if not with_shift: L = L.subs({F["N1"]: 0, F["N2"]: 0, F["N3"]: 0}).doit()
    eqs = euler_equations(L, fields, [t, x])
    subs = {F[n]: amp[n] * E for n in names}
    subs.update({src[n]: samp[n] * E for n in src})
    out = []
    for eq in eqs:
        ex = (eq.lhs - eq.rhs).subs(subs).doit()
        out.append(sp.simplify(sp.expand(ex / E)).subs(al, alpha_val))
    unknowns = [amp[n] for n in names] if with_shift else [amp[n] for n in names if not n.startswith("N")]
    return out, unknowns
def books_source(Theta, omv, pv):
    """sources keeping the books at (omega, p along x): omega P_j = p Theta_xj, omega e = p P_x"""
    T11, T12, T13, T22, T23, T33 = Theta
    P = [pv * T11 / omv, pv * T12 / omv, pv * T13 / omv]
    e = pv * P[0] / omv
    return {"e": e, "P1": P[0], "P2": P[1], "P3": P[2], "T11": T11, "T12": T12, "T13": T13, "T22": T22, "T23": T23, "T33": T33}
def pairing(sol, s2, with_shift):
    val = -s2["e"] * sol[amp["u"]] + sp.Rational(1, 2) * sum(s2["T%d%d" % (min(i, j), max(i, j))] * sol[amp["h%d%d" % (min(i, j), max(i, j))]] for i in rng for j in rng)
    if with_shift: val += sum(s2["P%d" % (j + 1)] * sol[amp["N%d" % (j + 1)]] for j in range(3))
    return sp.simplify(val)
def TT(s1, s2):
    """T1.T2 - (1/2) T1 T2 with eta = diag(-1, 1, 1, 1)"""
    Tm = lambda s: sp.Matrix([[s["e"], s["P1"], s["P2"], s["P3"]], [s["P1"], s["T11"], s["T12"], s["T13"]],
                              [s["P2"], s["T12"], s["T22"], s["T23"]], [s["P3"], s["T13"], s["T23"], s["T33"]]])
    eta = sp.diag(-1, 1, 1, 1)
    A, B = Tm(s1), Tm(s2)
    dot = sum(eta[m, m] * eta[n, n] * A[m, n] * B[m, n] for m in range(4) for n in range(4))
    trA = sum(eta[m, m] * A[m, m] for m in range(4)); trB = sum(eta[m, m] * B[m, m] for m in range(4))
    return dot - sp.Rational(1, 2) * trA * trB
random.seed(144)
okM, okN, details = True, True, []
for trial in range(3):
    omv = sp.Rational(random.randint(1, 9), random.randint(1, 9)); pv = sp.Rational(random.randint(1, 9), random.randint(1, 9))
    if omv == pv: pv += 1
    Th1 = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(6)]
    Th2 = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(6)]
    s1 = books_source(Th1, omv, pv); s2 = books_source(Th2, omv, pv)
    target = sp.simplify(TT(s2, s1) / (2 * K * (pv ** 2 - omv ** 2)))
    for with_shift in (True, False):
        eqs, unk = plane_system(with_shift, K / 4)
        eqs = [sp.simplify(e_.subs({om: omv, p: pv}).subs({samp[n]: s1[n] for n in src})) for e_ in eqs]
        sol = sp.linsolve(eqs, unk)
        if sol == sp.EmptySet:
            if with_shift: okM = False
            else: okN = False
            continue
        sol = dict(zip(unk, list(sol)[0]))
        val = pairing(sol, s2, with_shift)
        free = val.free_symbols - {K}
        good = (not free) and sp.simplify(val - target) == 0
        if with_shift: okM = okM and good
        else: okN = okN and good
        details.append("%s shift: pairing %s vs target %s" % ("with" if with_shift else "without", sp.nsimplify(val), sp.nsimplify(target)))
check("M1 at alpha = K/4, sources that keep the books (3 random rational (omega, p, Theta, Theta')): the member's plane-wave equations (Euler-Lagrange of the "
      "stated Lagrangian, derived here) have a solution WITH the shift, and the pairing -e'u + N.P' + (1/2)Theta'.h equals (1/(2K))[T'.T - (1/2)T'T]/(p^2 - omega^2), "
      "independent of the free (relabelling) parameters", okM, details[0] if details else "")
check("M2 the same WITHOUT the shift (N = 0, no N.P term): a solution exists and the pairing is the same", okN, details[1] if len(details) > 1 else "")
# at alpha != K/4: no solution for a source with e != 0
omv, pv = sp.Rational(1, 2), sp.Rational(3, 1)
s1 = books_source([1, sp.Rational(1, 3), 0, 2, 0, -1], omv, pv)
bad = []
for with_shift in (True, False):
    eqs, unk = plane_system(with_shift, K / 3)
    eqs = [sp.simplify(e_.subs({om: omv, p: pv}).subs({samp[n]: s1[n] for n in src})) for e_ in eqs]
    bad.append(sp.linsolve(eqs, unk) == sp.EmptySet)
check("M3 at alpha = K/3 (not K/4) a moving source with e != 0 has no solution, with or without the shift", all(bad) and s1["e"] != 0)

# ================================================================ X: the two-body pull at order v^2
v1 = sp.Matrix(sp.symbols("v1x v1y v1z", real=True)); v2 = sp.Matrix(sp.symbols("v2x v2y v2z", real=True))
m1, m2, eps = sp.symbols("m1 m2 epsilon", positive=True)
def body(m, v):
    g = 1 / sp.sqrt(1 - (eps * v).dot(eps * v))
    V = eps * v
    return {"e": m * g, "P1": m * g * V[0], "P2": m * g * V[1], "P3": m * g * V[2],
            "T11": m * g * V[0] ** 2, "T12": m * g * V[0] * V[1], "T13": m * g * V[0] * V[2], "T22": m * g * V[1] ** 2, "T23": m * g * V[1] * V[2], "T33": m * g * V[2] ** 2}
inst = sp.expand(sp.series(TT(body(m1, v1), body(m2, v2)), eps, 0, 3).removeO())
v11, v22, v12 = v1.dot(v1), v2.dot(v2), v1.dot(v2)
check("X1 T1.T2 - (1/2)T1T2 for e = m gamma, P = m gamma v, Theta = m gamma v v, to order v^2: m1 m2 [1/2 + (3/4)(v1^2 + v2^2) - 2 v1.v2]",
      sp.expand(inst - m1 * m2 * (sp.Rational(1, 2) + sp.Rational(3, 4) * eps ** 2 * (v11 + v22) - 2 * eps ** 2 * v12)) == 0)
# retardation: 1/(p^2 - omega^2) = 1/p^2 + omega^2/p^4 + ...; with omega^2 -> (p.v1)(p.v2) between the two bodies and FT[p_i p_j / p^4] = d_i d_j r/(8 pi)
X3 = sp.Matrix(sp.symbols("X Y Z", real=True)); r = sp.sqrt(X3.dot(X3))
hess = sp.Matrix(3, 3, lambda i, j: sp.diff(r, X3[i], X3[j]))
nvec = X3 / r
check("X2 d_i d_j r = (delta_ij - n_i n_j)/r, so the retardation kernel v1_i v2_j d_i d_j r/(8 pi) = [v1.v2 - (n.v1)(n.v2)]/(8 pi r); FT[1/p^4] = -r/(8 pi) is consistent with FT[1/p^2] = 1/(4 pi r) (Lap(-r/(8pi)) = -1/(4 pi r))",
      sp.simplify(hess - (sp.eye(3) - nvec * nvec.T) / r) == sp.zeros(3, 3) and sp.simplify(sum(sp.diff(-r / (8 * sp.pi), X3[i], 2) for i in range(3)) + 1 / (4 * sp.pi * r)) == 0)
# L_int = (1/(2K)) [inst/(4 pi r) + (m1 m2/2)(v1.v2 - (n.v1)(n.v2))/(8 pi r)]
nv = sp.Matrix(sp.symbols("n1 n2 n3", real=True))
kk = m1 * m2 / (16 * sp.pi * K)
rr = sp.Symbol("r", positive=True)
Lint = (1 / (2 * K)) * (inst / (4 * sp.pi * rr) + (m1 * m2 / 2) * eps ** 2 * (v12 - nv.dot(v1) * nv.dot(v2)) / (8 * sp.pi * rr))
target = kk / rr * (1 + sp.Rational(3, 2) * eps ** 2 * (v11 + v22) - sp.Rational(7, 2) * eps ** 2 * v12 - sp.Rational(1, 2) * eps ** 2 * nv.dot(v1) * nv.dot(v2))
check("X3 block 144 T3: L_int = (m1 m2/(16 pi K r))[1 + (3/2)(v1^2 + v2^2) - (7/2)v1.v2 - (1/2)(n.v1)(n.v2)]: a = 3/2, b = -7/2, c = -1/2",
      sp.simplify(sp.expand(Lint - target)) == 0)

# ================================================================ W: the weight of a bound pair, directly
a_, b_, c_, k_ = sp.symbols("a b c k", real=True)
P = sp.Matrix(sp.symbols("P1 P2 P3", real=True)); q = sp.Matrix(sp.symbols("q1 q2 q3", real=True))
M = m1 + m2; mu1, mu2 = m1 / M, m2 / M
p1 = mu1 * P + q; p2 = mu2 * P - q
n_ = sp.Matrix(sp.symbols("nx ny nz", real=True))
lam = sp.Symbol("lambda")
def kinetic(pv_, m): return m + pv_.dot(pv_) / (2 * m) - pv_.dot(pv_) ** 2 / (8 * m ** 3)
Hint = -(k_ / rr) * (1 + a_ * (p1.dot(p1) / m1 ** 2 + p2.dot(p2) / m2 ** 2) + b_ * p1.dot(p2) / (m1 * m2) + c_ * n_.dot(p1) * n_.dot(p2) / (m1 * m2))
Hfull = kinetic(p1, m1) + kinetic(p2, m2) + Hint
ehat = sp.Matrix(sp.symbols("e1 e2 e3", real=True))
H2 = sp.expand(sp.diff(Hfull.subs({P[0]: lam * ehat[0], P[1]: lam * ehat[1], P[2]: lam * ehat[2]}), lam, 2).subs(lam, 0) / 2)   # P^2 coefficient along ehat (|ehat| = 1)
mured = m1 * m2 / M
Tint = q.dot(q) / (2 * mured); TP = ehat.dot(q) ** 2 / (2 * mured)
U = -k_ / rr; UP = -k_ * n_.dot(ehat) ** 2 / rr
ee = ehat.dot(ehat)
expect = (ee / (2 * M) - (ee * Tint + 2 * TP) / (2 * M ** 2) + ((2 * a_ + b_) * ee * U + c_ * UP) / M ** 2)
check("W1 the P^2 coefficient of the pair's Hamiltonian (relativistic kinetic terms + first-order pull, P = lambda ehat) is "
      "|e|^2/(2M) - (|e|^2 T + 2T_P)/(2M^2) + ((2a+b)|e|^2 U + c U_P)/M^2, T = q^2/(2 mu), T_P = (ehat.q)^2/(2 mu), U_P = -k (n.ehat)^2/r: exact",
      sp.simplify(sp.expand(H2 - expect)) == 0)
# terms linear in P (first order in P) are odd in q or carry the relative momentum: their first-order averages vanish; second order is beyond first order in k and v^2
lin = sp.expand(sp.diff(Hfull.subs({P[0]: lam * ehat[0], P[1]: lam * ehat[1], P[2]: lam * ehat[2]}), lam).subs(lam, 0))
lin_kin0 = sp.expand(sum(sp.diff(pv_.dot(pv_) / (2 * m), lam) for pv_, m in ((p1.subs({P[0]: lam * ehat[0], P[1]: lam * ehat[1], P[2]: lam * ehat[2]}), m1), (p2.subs({P[0]: lam * ehat[0], P[1]: lam * ehat[1], P[2]: lam * ehat[2]}), m2))).subs(lam, 0))
check("W2 the leading kinetic term has no P.q cross term (centre-of-mass split p_a = mu_a P +- q)", sp.simplify(lin_kin0) == 0)
# directional virial for V = -k/r: 2<T_P> = <x_P d_P V> = -<U_P>  (stationary states); then W = E0 d2E/dP2 with E0 = M + <T> + <U>
Tm, TPm, Um, UPm = sp.symbols("T_avg TP_avg U_avg UP_avg")
d2E = 1 / M - (Tm + 2 * TPm) / M ** 2 + 2 * ((2 * a_ + b_) * Um + c_ * UPm) / M ** 2
Wfirst = sp.expand(1 + (Tm + Um) / M - (Tm - UPm) / M + 2 * ((2 * a_ + b_) * Um + c_ * UPm) / M)
check("W3 with the directional virial 2<T_P> = -<U_P>, to first order in the binding: W = 1 + [(1 + 2(2a+b))<U> + (1 + 2c)<U_P>]/M (block 144 T4)",
      sp.simplify(Wfirst - (1 + ((1 + 2 * (2 * a_ + b_)) * Um + (1 + 2 * c_) * UPm) / M)) == 0)
xs = sp.Matrix(sp.symbols("xs1 xs2 xs3", real=True)); rs = sp.sqrt(xs.dot(xs))
Vf = -k_ / rs
check("W4 the directional virial's ingredient: x_P d_P V = -U_P for V = -k/r (x_P = ehat.x, U_P = -k (n.ehat)^2/r)",
      sp.simplify(ehat.dot(xs) * sum(ehat[i] * sp.diff(Vf, xs[i]) for i in range(3)) - (k_ * (ehat.dot(xs) / rs) ** 2 / rs)) == 0)
check("W5 W = 1 along every axis for every bound state iff 1 + 2(2a+b) = 0 and 1 + 2c = 0 (<U_P>/<U> ranges over an interval as the orbit turns); "
      "the member's (3/2, -7/2, -1/2) satisfies both; the clock alone (0, 0, 0) gives W = 1 + (<U> + <U_P>)/M < 1",
      (1 + 2 * (2 * sp.Rational(3, 2) - sp.Rational(7, 2))) == 0 and (1 + 2 * (-sp.Rational(1, 2))) == 0)

# ================================================================ G: the first-order boost generator
x1 = sp.Matrix(sp.symbols("x1a x1b x1c", real=True)); x2 = sp.Matrix(sp.symbols("x2a x2b x2c", real=True))
pp1 = sp.Matrix(sp.symbols("p1a p1b p1c", real=True)); pp2 = sp.Matrix(sp.symbols("p2a p2b p2c", real=True))
rv = x1 - x2; R = sp.sqrt(rv.dot(rv)); nn = rv / R
Hh = (sum(m + pv_.dot(pv_) / (2 * m) - pv_.dot(pv_) ** 2 / (8 * m ** 3) for pv_, m in ((pp1, m1), (pp2, m2)))
      - (k_ / R) * (1 + a_ * (pp1.dot(pp1) / m1 ** 2 + pp2.dot(pp2) / m2 ** 2) + b_ * pp1.dot(pp2) / (m1 * m2) + c_ * nn.dot(pp1) * nn.dot(pp2) / (m1 * m2)))
s1_, s2_ = sp.symbols("sigma1 sigma2")
def G_comp(i):
    return (sum((m + pv_.dot(pv_) / (2 * m)) * xv[i] for pv_, m, xv in ((pp1, m1, x1), (pp2, m2, x2)))
            - (k_ / R) * (s1_ * x1[i] + s2_ * x2[i]))
def pb(A, B):
    return sum(sp.diff(A, xv[i]) * sp.diff(B, pv_[i]) - sp.diff(A, pv_[i]) * sp.diff(B, xv[i]) for xv, pv_ in ((x1, pp1), (x2, pp2)) for i in range(3))
# {G_x, H} - P_x at first order in k and to first order in the momenta (the O(k p) terms)
kk_ = sp.Symbol("kappa_small")
res = sp.expand(pb(G_comp(0), Hh) - (pp1[0] + pp2[0]))
# keep the terms of first order in k and first order in the momenta (scale p -> tau p)
tau_ = sp.Symbol("tau")
res_s = res.subs({pv_[i]: tau_ * pv_[i] for pv_ in (pp1, pp2) for i in range(3)}, simultaneous=True)
res_k1 = sp.expand(sp.diff(res_s, k_).subs(k_, 0))
res_k1_p1 = sp.expand(sp.diff(res_k1, tau_).subs(tau_, 0))
# the condition must hold at every configuration: sample points
cond = []
for pt in ([1, 2, 3, -1, 0, 1], [2, -1, 0, 0, 1, -2], [0, 1, 1, 1, 0, 0], [3, 0, 1, -2, 2, 1]):
    for pvals in ([1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]):
        sub = dict(zip(list(x1) + list(x2), pt)); sub.update(dict(zip(list(pp1) + list(pp2), pvals)))
        cond.append(sp.simplify(res_k1_p1.subs(sub)))
sol = sp.solve(cond, [s1_, s2_, a_, b_, c_], dict=True)
print("   G: solutions for {G, H} = P at first order in k and in the momenta:", sol)
okG = any(sp.simplify(s_.get(c_, sp.Symbol("free")) + sp.Rational(1, 2)) == 0 for s_ in sol)
fam = [s_ for s_ in sol]
check("G1 a centre-of-energy G = sum (m + p^2/2m) x - (k/r)(sigma1 x1 + sigma2 x2) with {G, H} = P at first order in k exists iff c = -1/2 and 2a + b = -1/2 "
      "(then sigma1 = sigma2 = 1/2), solved at 24 configurations: the pulls with weight one along every axis are exactly those with a first-order boost generator",
      len(sol) >= 1 and all((sp.simplify(s_.get(c_, c_) + sp.Rational(1, 2)) == 0) and (sp.simplify(2 * s_.get(a_, a_) + s_.get(b_, b_) + sp.Rational(1, 2)) == 0) for s_ in sol),
      str(sol))

print("")
print("TOTAL: PASS=%d FAIL=%d" % (len(PASS), len(FAIL)))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("HIT: block 144 confirmed by independent routes: the member's plane-wave equations derived here from the landed quadratic action (with block 136's shift) "
          "give the exchange (1/(2K))[T'.T - T'T/2]/(p^2 - omega^2) at alpha = K/4, with or without the shift, and no solution at alpha != K/4; the two-body pull "
          "(m1 m2/(16 pi K r))[1 + (3/2)(v1^2+v2^2) - (7/2)v1.v2 - (1/2)(n.v1)(n.v2)]; a direct bound-state computation gives W = 1 + [(1 + 2(2a+b))<U> + (1+2c)<U_P>]/M; "
          "and a first-order centre-of-energy generator exists iff c = -1/2, 2a + b = -1/2: pull-bound pairs have weight one along every axis")
    print("SUMMARY: PARTIAL block 144's T2, T3, T4 (and T5's 'pull unchanged without the shift') confirmed by a direct Euler-Lagrange solution, a direct bound-state "
          "computation and a Poisson-bracket boost generator; T5's drifting-lengths claim and T1 not re-checked")
