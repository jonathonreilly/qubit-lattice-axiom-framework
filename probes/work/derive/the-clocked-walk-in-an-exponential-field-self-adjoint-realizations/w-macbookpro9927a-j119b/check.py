#!/usr/bin/env python3
"""The clocked walk in an exponential clock field, self-adjoint realizations: checks for ATTEMPT.md (attempt 2 of 2),
worker w-macbookpro9927a-j119b (claude-opus-5-5).

Objects (block 54 as landed on main, c3f8c47a58): (T psi)(x) = psi(x - 1), D = (i/2)(T - T^dag), the 3D walk H = sum_j sigma_j D_j,
the clocked walk H_w = W^(1/2) H W^(1/2) with w = lambda^(x1), lambda = mu^2 > 1. Across the gradient a plane wave gives the sector
operator (J psi)(n) = (i/2) sigma_1 [lambda^(n-1/2) psi(n-1) - lambda^(n+1/2) psi(n+1)] + lambda^n (p2 sigma_2 + p3 sigma_3) psi(n),
(p2, p3) = (sin k2, sin k3); p = 0 is block 108's line walk. Everything below is exact (sympy, Gaussian rationals); no floating point.
"""
from __future__ import annotations

import json
import subprocess
import time

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R_ = sp.Rational
I = sp.I
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -I], [I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
E2 = sp.eye(2)

NOTES = [
    ("b54", "c3f8c47a58", "docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_"
     "TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["Define (T_e psi)(x)=psi(x-e), D_j=(i/2)(T_j-T_j^dagger), and H=sum_e A_e T_e",
      "Conditional on a well-defined realization with the required intertwining relation, one could infer U(t)T_a=T_a U(lambda_a t); "
      "this note does not establish such a realization."]),
    ("b108", "305272de6f", "docs/ADMISSIBILITY_RULE_IN_AN_EXPONENTIAL_CLOCK_FIELD_THE_WALKS_DYNAMICS_NEEDS_A_BOUNDARY_CONDITION_AT_THE_"
     "FAST_CLOCK_END_BOUNDED_THEOREM_NOTE_2026-09-23.md",
     ["Chain A is `{(up, even x), (down, odd x)}` and chain B is `{(up, odd x), (down, even x)}`",
      "the shift by one carries chain A's solutions onto chain B's, so exactly the realizations whose chain-B condition is the image "
      "of the chain-A condition keep U(t) T_a = T_a U(lambda^a t) for every a"]),
    ("b109", "888d7ca821", "docs/ADMISSIBILITY_RULE_IN_THREE_DIMENSIONS_THE_CLOCKED_WALK_NEEDS_A_FAST_END_CONDITION_EXACTLY_IN_THE_"
     "SECTORS_WITH_SMALL_TRANSVERSE_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-23.md",
     ["its solutions are exactly psi(n) = (r/sqrt(lambda))^n v with r - 1/r = +-2m, m = |(sin k2, sin k3)|",
      "deficiency indices (2,2) for m < m* and (0,0) for m > m*"]),
]
TASK_Q = ["(b) classify the chain-MIXING realizations on the line and decide which of them keep the identity for every translation",
          "whether a single choice can serve all sectors with m < sinh(g/2) consistently with the lattice's rotations about x1",
          "HIT: (b) or (c) exact, or a counterexample to blocks 108-109."]
TASK_ID = "J:derive:the-clocked-walk-in-an-exponential-field-self-adjoint-realizations:a2"


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == TASK_ID), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, "block 54 as landed (c3f8c47a58), blocks 108 and 109 (PR heads) and the task quoted verbatim (9 lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ---------------------------------------------------------------- the sector operator and its boundary form
def Jrow(psi, k, mu, P):
    """(J psi)(k) for the sector operator; psi: dict k -> 2x1 Matrix; lambda = mu^2."""
    return (I / 2) * S1 * (mu ** (2 * k - 1) * psi[k - 1] - mu ** (2 * k + 1) * psi[k + 1]) + mu ** (2 * k) * P * psi[k]


def Bform(psi, phi, N, mu):
    """Christoffel-Darboux boundary term between N and N + 1: psi(N)^+ H_{N,N+1} phi(N+1) - psi(N+1)^+ H_{N+1,N} phi(N)."""
    Hup = -(I / 2) * mu ** (2 * N + 1) * S1
    Hdn = (I / 2) * mu ** (2 * N + 1) * S1
    return sp.expand((psi[N].H * Hup * phi[N + 1] - psi[N + 1].H * Hdn * phi[N])[0])


def family_g() -> None:
    # Green's identity on a window, exact, with generic Gaussian-rational sequences and a transverse term
    mu = R_(2)
    P = R_(1, 4) * S2 + R_(1, 3) * S3
    import random
    rnd = random.Random(7)
    ps = {k: sp.Matrix([R_(rnd.randint(-9, 9), rnd.randint(1, 5)) + I * R_(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(2)])
          for k in range(-2, 6)}
    ph = {k: sp.Matrix([R_(rnd.randint(-9, 9), rnd.randint(1, 5)) + I * R_(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(2)])
          for k in range(-2, 6)}
    lhs = sum((ps[k].H * Jrow(ph, k, mu, P) - Jrow(ps, k, mu, P).H * ph[k])[0] for k in range(0, 4))
    rhs = Bform(ps, ph, 3, mu) - Bform(ps, ph, -1, mu)
    ok = sp.simplify(sp.expand(lhs - rhs)) == 0
    check("G", ok, "sum_{n=0}^{3} [psi^+(J phi) - (J psi)^+ phi] = B_3 - B_{-1}, B_N = psi(N)^+ H_{N,N+1} phi(N+1) - psi(N+1)^+ H_{N+1,N} "
          "phi(N), exact on random Gaussian-rational sequences with lambda = 4, (p2, p3) = (1/4, 1/3): the boundary form sits at the ends")


# ---------------------------------------------------------------- (a) explicit solutions at every energy
def family_a() -> None:
    mu, z = sp.symbols("mu z", positive=True)
    X = sp.Symbol("X")                          # X = z mu^(-2n)
    ok = True
    for s in (1, -1):                           # sigma_1 = s sector of the line walk
        for eps in (1, -1):                     # f(n) ~ (eps/mu)^n at the fast end
            Jt = 5
            c = [sp.Integer(1)]
            for j in range(1, Jt + 1):
                c.append(sp.simplify(-2 * I * s * eps * c[-1] / (mu ** (2 * j) - mu ** (-2 * j))))
            Sx = lambda Y: sum(c[j] * Y ** j for j in range(Jt + 1))
            # (i s/2)(lambda^(n-1/2) f(n-1) - lambda^(n+1/2) f(n+1)) - z f(n), divided by (eps/mu)^n mu^(2n)
            lhs = (I * s / 2) * ((1 / eps) * Sx(X * mu ** 2) - eps * Sx(X / mu ** 2)) - X * Sx(X)
            ok &= sp.simplify(sp.expand(lhs + c[Jt] * X ** (Jt + 1))) == 0
            ratio = sp.simplify(c[2] / c[1])
            ok &= sp.simplify(ratio + 2 * I * s * eps / (mu ** 4 - mu ** -4)) == 0
    # 3D sectors: the coefficient recursion A_j c_j = c_{j-1}, A_j = (i/2)(lambda^j/r - r lambda^-j) sigma_1 + P, is solvable for
    # every j >= 1 exactly when no root r lambda^-j is a Floquet root; below m* no ratio reaches lambda
    muv = R_(2)
    P = R_(1, 4) * S2 + R_(1, 3) * S3
    roots = [R_(3, 2), R_(-2, 3), R_(2, 3), R_(-3, 2)]
    dets = [(I / 2 * (muv ** (2 * j) / r - r * muv ** (-2 * j)) * S1 + P).det() for r in roots for j in range(1, 7)]
    okd = all(dd != 0 for dd in dets)
    m, mu_ = sp.symbols("m mu", positive=True)
    mstar = (mu_ ** 2 - 1) / (2 * mu_)                      # (lambda - 1)/(2 sqrt(lambda)) with lambda = mu^2
    s_star = sp.sqrt(sp.factor(1 + mstar ** 2))
    # (sqrt(1 + m^2) + m)^2 is increasing in m and equals lambda exactly at m = m*, so it is below lambda iff m < m*
    eqpt = sp.simplify((s_star + mstar) ** 2 - mu_ ** 2) == 0 and \
        sp.simplify(sp.diff((sp.sqrt(1 + m ** 2) + m) ** 2, m) - 2 * (sp.sqrt(1 + m ** 2) + m) ** 2 / sp.sqrt(1 + m ** 2)) == 0
    check("A", ok and okd and eqpt,
          "for every complex z the line walk has four explicit solutions f(n) = (eps/mu)^n v_s sum_j c_j (z lambda^-n)^j, "
          "c_j = -2 i s eps c_{j-1}/(lambda^j - lambda^-j) (identity exact to order 5 with symbolic z, lambda; the coefficients fall "
          "like lambda^(-j^2/2), so the series is entire), each ~ (+-lambda^(-1/2))^n at the fast end: all square-summable there for "
          "every z; in a 3D sector the same recursion A_j c_j = c_{j-1} is solvable (det A_j != 0 checked for j = 1..6 at lambda = 4, "
          "(p2, p3) = (1/4, 1/3)) because (sqrt(1+m^2) + m)^2 < lambda exactly when m < m*")


# ---------------------------------------------------------------- (b) the line: realizations and translations
def floquet(P, mu, rv):
    """zero-energy Floquet solutions psi(n) = (r/mu)^n v on n = -1..3 (dict), checking [(i/2)(1/r - r) sigma_1 + P] v = 0."""
    out = []
    for r, v in rv:
        assert ((I / 2) * (1 / r - r) * S1 + P) * v == sp.zeros(2, 1)
        out.append({k: (r / mu) ** k * v for k in range(-1, 5)})
    return out


def gram(sols, mu, N=0):
    return sp.Matrix(len(sols), len(sols), lambda i, j: Bform(sols[i], sols[j], N, mu))


def family_b() -> None:
    mu = R_(2)
    P0 = sp.zeros(2, 2)
    basis = [(1, sp.Matrix([1, 0])), (1, sp.Matrix([0, 1])), (-1, sp.Matrix([1, 0])), (-1, sp.Matrix([0, 1]))]
    sols = floquet(P0, mu, basis)
    Gm = gram(sols, mu)
    Gexp = sp.diag(-I * S1, I * S1)
    ok1 = Gm == Gexp and all(gram(sols, mu, N) == Gexp for N in (1, 2, 3))
    # T_1 acts on (r/mu)^n v by mu/r: M = mu diag(1, 1, -1, -1); M^2 = lambda
    Mt = sp.diag(mu, mu, -mu, -mu)
    shifted = [{k: sol[k - 1] for k in range(0, 5)} for sol in sols]
    ok2 = all(sp.simplify(shifted[i][k] - Mt[i, i] * sols[i][k]) == sp.zeros(2, 1) for i in range(4) for k in range(0, 5))
    ok2 &= Mt ** 2 == mu ** 2 * sp.eye(4)
    # conformal: G(Mx, My) = lambda G(x, y)
    ok2 &= (Mt.H * Gexp * Mt) == mu ** 2 * Gexp
    # the isotropic circle in E_+ (and E_-): v = (1, i t) or (0, 1)
    t1, t2 = sp.symbols("t1 t2", real=True)
    v1 = sp.Matrix([1, I * t1])
    v2 = sp.Matrix([1, I * t2])
    ok3 = sp.simplify((v1.H * S1 * v1)[0]) == 0 and (sp.Matrix([0, 1]).H * S1 * sp.Matrix([0, 1]))[0] == 0
    # E_+ is not isotropic; L(v1, v2) = span(v1 in E_+, v2 in E_-) is Lagrangian for every t1, t2
    Lb = sp.Matrix.hstack(sp.Matrix.vstack(v1, sp.zeros(2, 1)), sp.Matrix.vstack(sp.zeros(2, 1), v2))
    ok3 &= sp.simplify(Lb.H * Gexp * Lb) == sp.zeros(2, 2) and (sp.Matrix.hstack(sp.eye(4)[:, 0], sp.eye(4)[:, 1]).H * Gexp *
                                                          sp.Matrix.hstack(sp.eye(4)[:, 0], sp.eye(4)[:, 1])) != sp.zeros(2, 2)
    # chains: the solution x (+) sigma_3 x is supported on (up, even), (down, odd): chain A; x (+) -sigma_3 x on chain B
    x1, x2 = sp.symbols("x1 x2")
    xx = sp.Matrix([x1, x2])
    uA = {k: (R_(1) / mu) ** k * xx + (R_(-1) / mu) ** k * (S3 * xx) for k in range(0, 4)}
    uB = {k: (R_(1) / mu) ** k * xx + (R_(-1) / mu) ** k * (-S3 * xx) for k in range(0, 4)}
    ok4 = all(sp.expand(uA[k][1 if k % 2 == 0 else 0]) == 0 for k in range(4)) and \
        all(sp.expand(uB[k][0 if k % 2 == 0 else 1]) == 0 for k in range(4))
    # L(v1, v2) meets chain A iff v2 is parallel to sigma_3 v1, i.e. t2 = -t1 (then it is chain-separate)
    meetA = sp.solve(sp.Eq((sp.Matrix([[1, 1], [I * t2, -I * t1]])).det(), 0), t2)
    rk_on = sp.Matrix.hstack(Lb, sp.Matrix.vstack(v1, S3 * v1)).subs(t2, -t1).rank()
    rk_off = sp.Matrix.hstack(Lb, sp.Matrix.vstack(v1, S3 * v1)).subs({t1: 1, t2: 2}).rank()
    ok4 &= meetA == [-t1] and rk_on == 2 and rk_off == 3
    # every Lagrangian plane is invariant under T_2 (M^2 is scalar); a chain-mixing, T_1-invariant witness: t1 = 0, t2 = 1
    Lw = Lb.subs({t1: 0, t2: 1})
    ok5 = (Lw.H * Gexp * Lw) == sp.zeros(2, 2) and sp.Matrix.hstack(Lw, Mt * Lw).rank() == 2
    Abas = sp.Matrix.hstack(*[sp.Matrix.vstack(e, S3 * e) for e in (sp.Matrix([1, 0]), sp.Matrix([0, 1]))])
    Bbas = sp.Matrix.hstack(*[sp.Matrix.vstack(e, -S3 * e) for e in (sp.Matrix([1, 0]), sp.Matrix([0, 1]))])
    ok5 &= sp.Matrix.hstack(Lw, Abas).rank() == 4 and sp.Matrix.hstack(Lw, Bbas).rank() == 4     # meets neither chain
    # a chain-separate but non-invariant realization (block 108's torus off its circle): A with x = (1, 0), B with y = (1, i)
    Ln = sp.Matrix.hstack(sp.Matrix.vstack(sp.Matrix([1, 0]), S3 * sp.Matrix([1, 0])),
                          sp.Matrix.vstack(sp.Matrix([1, I]), -S3 * sp.Matrix([1, I])))
    ok5 &= (Ln.H * Gexp * Ln) == sp.zeros(2, 2) and sp.Matrix.hstack(Ln, Mt * Ln).rank() > 2
    # the content's half-turn about the line, sigma_1 (it commutes with the line walk), acts as sigma_1 (+) sigma_1 and commutes
    # with M: an invariant plane of both is spanned by joint eigenvectors (1, +-1) (x) E_+-, none of which is isotropic
    Sg = sp.diag(S1, S1)
    ok6 = Sg * Mt == Mt * Sg
    joint = [sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, -1, 0, 0]), sp.Matrix([0, 0, 1, 1]), sp.Matrix([0, 0, 1, -1])]
    ok6 &= all((jv.H * Gexp * jv)[0] != 0 for jv in joint) and all(sp.Matrix.hstack(jv, Sg * jv).rank() == 1 for jv in joint)
    # sigma_1 commutes with the line walk: J at p = 0 contains sigma_1 only
    check("B", ok1 and ok2 and ok3 and ok4 and ok5 and ok6,
          "line, lambda = 4: the four zero-energy solutions (+-1/mu)^n v give the boundary form G = diag(-i sigma_1, +i sigma_1) "
          "(constant in N); T_1 = mu diag(1,1,-1,-1), T_2 = lambda (scalar), G(T_1 x, T_1 y) = lambda G(x, y); realizations = "
          "Lagrangian planes; the T_1-invariant ones are exactly L(v1, v2) = span(v1 (x) E_+, v2 (x) E_-) with v1, v2 on the isotropic "
          "circle (1, it): a torus; chain A = {(x, sigma_3 x)}, chain B = {(x, -sigma_3 x)}; L(v1, v2) is chain-separate iff "
          "t2 = -t1 (block 108's circle), chain-mixing otherwise (witness t1 = 0, t2 = 1); a chain-separate plane off that circle is "
          "not invariant; no plane is invariant under both T_1 and the half-turn sigma_1")


# ---------------------------------------------------------------- (c) three dimensions, sector by sector
def family_c() -> None:
    mu = R_(2)                                              # lambda = 4, m* = (lambda - 1)/(2 sqrt lambda) = 3/4
    p2, p3 = R_(1, 4), R_(1, 3)                             # m = 5/12, sqrt(1 + m^2) = 13/12
    P = p2 * S2 + p3 * S3
    N_ = p2 * S3 - p3 * S2                                  # sigma_1 P = i N
    vp, vm = sp.Matrix([2 * I, 1]), sp.Matrix([1, 2 * I])   # N v = +-m v
    ok0 = N_ * vp == R_(5, 12) * vp and N_ * vm == -R_(5, 12) * vm and S1 * P == I * N_
    lab = ["a", "b", "c", "d"]
    rv = [(R_(3, 2), vp), (R_(-2, 3), vp), (R_(2, 3), vm), (R_(-3, 2), vm)]
    sols = floquet(P, mu, rv)
    ok0 &= all(abs(r) / mu < 1 for r, _ in rv)              # all four square-summable at the fast end: m = 5/12 < 3/4
    Gm = gram(sols, mu)
    ok1 = all(gram(sols, mu, N) == Gm for N in (1, 2, 3))
    nz = {(lab[i], lab[j]) for i in range(4) for j in range(4) if Gm[i, j] != 0}
    ok1 &= nz == {("a", "c"), ("c", "a"), ("b", "d"), ("d", "b")}
    Mt = sp.diag(*[mu / r for r, _ in rv])                  # T_1 on (r/mu)^n v is mu/r
    ok1 &= len(set(Mt[i, i] for i in range(4))) == 4 and (Mt.H * Gm * Mt) == mu ** 2 * Gm
    inv_lag = []
    for i in range(4):
        for j in range(i + 1, 4):
            sub = sp.Matrix([[Gm[i, i], Gm[i, j]], [Gm[j, i], Gm[j, j]]])
            if sub == sp.zeros(2, 2):
                inv_lag.append(lab[i] + lab[j])
    ok2 = inv_lag == ["ab", "ad", "bc", "cd"]
    # T_2 = M^2 has eigenspaces F1 = span(a, d) (16/9) and F2 = span(b, c) (9); the (1,1) T_2-invariant planes
    # span(alpha a + delta d, beta b + gamma c) are Lagrangian iff (beta : gamma) = (conj alpha : conj delta): a sphere CP^1
    M2 = Mt ** 2
    ok3 = [M2[i, i] for i in range(4)] == [R_(16, 9), 9, 9, R_(16, 9)]
    al, de = sp.symbols("alpha delta")
    be, ga = sp.symbols("beta gamma")
    xv = sp.Matrix([al, 0, 0, de])
    yv = sp.Matrix([0, be, ga, 0])
    cross = sp.expand((xv.H * Gm * yv)[0])
    sol = sp.solve(sp.Eq(cross, 0), be)
    ok3 &= len(sol) == 1 and sp.simplify(sol[0] - sp.conjugate(al) * ga / sp.conjugate(de)) == 0
    # rotations about x1: R = exp(-i pi sigma_1/4) sends the sector (p2, p3) to (-p3, p2) with N -> N', labels kept;
    # the half-turn sigma_1 sends (p2, p3) to (-p2, -p3), labels kept
    Rm = (E2 - I * S1) / sp.sqrt(2)
    Pr = -p3 * S2 + p2 * S3
    Nr = p2 * S3 - (-p3) * S2
    Nr = (-p3) * S3 - p2 * S2
    ok4 = sp.simplify(Rm * P * Rm.H - Pr) == sp.zeros(2, 2) and sp.simplify(Rm * S1 * Rm.H - S1) == sp.zeros(2, 2)
    ok4 &= sp.simplify(Rm * N_ * Rm.H - Nr) == sp.zeros(2, 2)
    ok4 &= sp.simplify(Nr * (Rm * vp) - R_(5, 12) * (Rm * vp)) == sp.zeros(2, 1)
    ok4 &= S1 * P * S1 == -P and S1 * N_ * S1 == -N_ and (-N_) * (S1 * vp) == R_(5, 12) * (S1 * vp)
    # m = 0 sectors (k2, k3 in {0, pi}): the half-turn fixes them and acts as sigma_1; family B shows no T_1-invariant plane is kept
    # direction dependence: as m -> 0 along p ~ (cos b, sin b), a -> (v+, r = +1), b -> (v+, -1), c -> (v-, +1), d -> (v-, -1)
    def limits(nv):
        ev = nv.eigenvects()
        vpl = [v for val, mult, vs in ev if val == 1 for v in vs][0]
        vmi = [v for val, mult, vs in ev if val == -1 for v in vs][0]
        E = lambda v, eps: sp.Matrix.vstack(v, sp.zeros(2, 1)) if eps == 1 else sp.Matrix.vstack(sp.zeros(2, 1), v)
        return {"bc": sp.Matrix.hstack(E(vpl, -1), E(vmi, 1)), "ad": sp.Matrix.hstack(E(vpl, 1), E(vmi, -1)),
                "ab": sp.Matrix.hstack(E(vpl, 1), E(vpl, -1)), "cd": sp.Matrix.hstack(E(vmi, 1), E(vmi, -1))}
    L0 = limits(S3)                                          # p ~ (1, 0): N/m = sigma_3
    L90 = limits(-S2)                                        # p ~ (0, 1): N/m = -sigma_2
    Gl = sp.diag(-I * S1, I * S1)
    ok5 = all(sp.Matrix.hstack(L0[k], L90[k]).rank() > 2 for k in L0)
    ok5 &= all(sp.simplify(L0[k].H * Gl * L0[k]) == sp.zeros(2, 2) and sp.simplify(L90[k].H * Gl * L90[k]) == sp.zeros(2, 2) for k in L0)
    # for every m > 0: the four roots are distinct, and r_i r_j = 1 exactly for the pairs a-c and b-d (so only these pair in G)
    mm = sp.Symbol("m", positive=True)
    ss = sp.sqrt(1 + mm ** 2)
    rs = {"a": mm + ss, "b": mm - ss, "c": ss - mm, "d": -mm - ss}
    prod_one = {(x, y) for x in "abcd" for y in "abcd" if x < y and sp.simplify(rs[x] * rs[y] - 1) == 0}
    distinct = all(sp.simplify(rs[x] - rs[y]) != 0 for x in "abcd" for y in "abcd" if x < y)
    squares = all(sp.solve(sp.Eq(rs[x] ** 2, 1), mm) == [] for x in "abcd")
    ok6 = prod_one == {("a", "c"), ("b", "d")} and distinct and squares
    check("C", ok0 and ok1 and ok2 and ok3 and ok4 and ok5 and ok6,
          "3D sector lambda = 4, (p2, p3) = (1/4, 1/3), m = 5/12 < m* = 3/4: Floquet roots r = 3/2, -2/3 (N = +m, v = (2i, 1)), "
          "2/3, -3/2 (N = -m, v = (1, 2i)); the boundary form pairs only a-c and b-d; T_1 = diag(4/3, -3, 3, -4/3), four distinct "
          "values: exactly four realizations keep U(t)T_a = T_aU(lambda^a t) for every x1-shift, the isotropic pairs ab, ad, bc, cd; "
          "T_2 keeps only F1 = ad, F2 = bc and a sphere span(alpha a + delta d, conj(alpha) b + conj(delta) c); the rotation "
          "exp(-i pi sigma_1/4) and the half-turn sigma_1 carry sectors to sectors keeping the labels; as m -> 0 each of the four "
          "choices tends to a plane that depends on the direction of (sin k2, sin k3) (0 and 90 degrees differ, both Lagrangian); for every "
          "m > 0 the roots m + s, m - s, s - m, -m - s (s = sqrt(1 + m^2)) are distinct, none squares to 1, and r_i r_j = 1 only for "
          "a-c and b-d")


def main() -> None:
    t0 = time.time()
    family_q()
    family_g()
    family_a()
    family_b()
    family_c()
    print("\n".join(OUT))
    print(f"families Q G A B C (all exact): {len(OUT) - len(FAILS)}/{len(OUT)} ok, {time.time() - t0:.0f} s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PARTIAL (a) the line walk's solutions at every energy are entire series, all square-summable at the fast end, "
          "giving (2,2) with a bounded slow end; (b) T_2 acts on the boundary space as the scalar lambda, so every realization keeps "
          "the even-shift identity, and the T_1-invariant ones form a torus containing block 108's circle, none kept by the half-turn "
          "sigma_1; (c) sectors 0 < m < m* have exactly four T_1-invariant realizations, rotation-covariant, each with a "
          "direction-dependent limit at m = 0")
    print("HIT: for block 108's line walk every self-adjoint realization, chain-mixing ones included, keeps U(t)T_2 = "
          "T_2U(lambda^2 t); those keeping U(t)T_a = T_aU(lambda^a t) for every a are exactly span(v1 at r = +1, v2 at r = -1), v1 and "
          "v2 on the isotropic circle (1, it): a torus whose chain-separate part (t2 = -t1) is block 108's circle; in block 109's 3D "
          "sectors with 0 < m < m* exactly four realizations keep the identity for every x1-shift (the isotropic pairs of the Floquet "
          "solutions); the half-turn about x1 fixes the four m = 0 sectors and keeps none of their torus, and each of the four choices "
          "has a direction-dependent limit at m = 0, so no choice continuous in (k2, k3) or covariant under the half-turn serves every "
          "sector with m < sinh(g/2)")


if __name__ == "__main__":
    main()
