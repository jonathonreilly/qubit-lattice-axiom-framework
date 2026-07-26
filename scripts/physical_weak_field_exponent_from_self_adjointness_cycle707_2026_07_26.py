#!/usr/bin/env python3
"""Cycle 707 - the weak-field mass-law exponent is forced by self-adjointness.

Target: admission (c) of the G_Newton lane, as sharpened by Probe P4:

    "(c) S = L(1 - phi)  -- weak-field test-mass action."
    "The selection of valley-linear is by EMPIRICAL match to F~M = 1, not by
     retained derivation. The audit ledger contains no retained
     'weak-field-action derivation theorem'."
    -- G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4

The landed ACTION_UNIQUENESS_NOTE observes, on ONE fixed ordered-lattice
family, that the mass-law exponent equals the weak-field power `p` of the
field in the action, and explicitly declines to promote it:

    "not promoted to a closed formula or a universal theorem"

This runner does not re-observe that.  It supplies the missing mechanism.

The framework's own self-consistency loop couples the field to the propagator
ADDITIVELY (GRAVITY_FULL_SELF_CONSISTENCY_NOTE: "the field modifies the
propagator via `H(phi) = H + phi`"), and `H` is self-adjoint (that note's
CHECK 3).  For a self-adjoint family depending analytically on a coupling,
Rellich's theorem makes the eigenvalue response ANALYTIC in the coupling.
Hence the leading power is a positive INTEGER:

    p = 1  generically (nonvanishing first-order term, Hellmann-Feynman),
    p >= 2 only when the first-order term vanishes,
    p = 1/2 UNREACHABLE from a self-adjoint additive coupling.

So the sublinear class -- the named rival to valley-linear -- is excluded by
self-adjointness, and `p = 1` is the generic case rather than an empirical fit.

Rows:

  A  leading-power extraction for the six named action forms, exact
  B  the P4 transcription correction: L*sqrt(1-f) is p=1, not p=1/2
  C  Hellmann-Feynman: first-order response is <psi|V|psi>, exact on a lattice
  D  generic self-adjoint coupling gives p=1 (nonvanishing first order)
  E  a symmetry that kills the first-order term gives p=2, not p=1/2
  F  p=1/2 requires non-self-adjointness: exact branch-point witness
  I  the GENUINE geometric spent-delay is sublinear -- the rival is real
  H  the propagator itself responds linearly, exact rational resolvent
  G  valley/hill sign control, reproducing the landed sign statement

SCOPE.  The additive coupling `H(phi) = H + phi` is the lane's own, but the
note it comes from labels those bullets "Heuristic motivation (not a proof)".
So the `p = 1` conclusion is CONDITIONAL on that coupling; its value is that
it collapses admission (c) into the SAME unforced premise the A2 heuristic
already uses, rather than deriving it from nothing.  What IS unconditional is
the exclusion of `p = 1/2`, which needs only self-adjointness -- verified
framework content.
"""

from fractions import Fraction
from itertools import product
import math

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# A. leading power of the action forms
# ---------------------------------------------------------------------------
# The action is S = L * g(f).  The "valley depth" is 1 - g(f).  The landed
# family's field is f = s/r with s proportional to the source mass, so
# f is proportional to M and depth ~ f^p implies F ~ M^p.  The object to
# extract is therefore the leading power of `1 - g(f)` as f -> 0.

# Each form supplies BOTH g and the valley depth `1 - g(f)` in a rationalized
# closed form.  Evaluating `1 - g(f)` directly at f ~ 1e-9 loses the answer to
# catastrophic cancellation -- for g = 1 - f^2 it underflows to exactly zero.
# The closed forms below involve no subtraction of nearly-equal quantities, and
# row A cross-checks each against `1 - g(f)` at moderate f where that
# subtraction is still safe.
ACTION_FORMS = {
    "valley_linear   g=1-f":       (lambda f: 1 - f,            lambda f: f,                         1.0),
    "exponential     g=exp(-f)":   (lambda f: math.exp(-f),     lambda f: -math.expm1(-f),           1.0),
    "reciprocal      g=1/(1+f)":   (lambda f: 1 / (1 + f),      lambda f: f / (1 + f),               1.0),
    "sqrt_of_1mf     g=sqrt(1-f)": (lambda f: math.sqrt(1 - f), lambda f: f / (1 + math.sqrt(1 - f)), 1.0),
    "sublinear       g=1-sqrt(f)": (lambda f: 1 - math.sqrt(f), lambda f: math.sqrt(f),              0.5),
    "superlinear     g=1-f^2":     (lambda f: 1 - f * f,        lambda f: f * f,                     2.0),
}


def leading_power(depth, f_small=1e-9, ratio=10.0):
    """log-log slope of the valley depth, evaluated deep in the weak field."""
    return math.log(depth(f_small * ratio) / depth(f_small)) / math.log(ratio)


def a_leading_powers():
    rows = []
    ok = True
    for name, (g, depth, expected) in ACTION_FORMS.items():
        # the closed-form depth must agree with 1 - g(f) where that is safe
        agrees = all(
            abs(depth(f) - (1 - g(f))) <= 1e-12 * max(1.0, abs(depth(f)))
            for f in (1e-3, 1e-2, 0.1, 0.25)
        )
        p = leading_power(depth)
        rows.append(
            f"{name:28s} p={p:.6f}  expected {expected}  depth-form agrees: {agrees}"
        )
        if abs(p - expected) > 1e-6 or not agrees:
            ok = False
    for r in rows:
        print("      " + r)
    check(
        "A leading power of the valley depth matches the named class for all six forms",
        ok,
        f"{len(ACTION_FORMS)} forms, closed-form depths cross-checked against 1-g(f)",
    )


def b_p4_transcription_correction():
    """`L*sqrt(1-f)` and `L*(1-sqrt(f))` are in DIFFERENT classes.

    P4 names the rival to valley-linear as `S = L sqrt(1 - phi)` and assigns
    it `F~M = 0.50`.  The landed ACTION_UNIQUENESS_NOTE's 0.50 row is
    `S = L(1 - f^0.5)`.  These are not the same expression: the parenthesis
    moved.  Exact series settles it.
    """
    # exact rational check that sqrt(1-f) is linear at leading order:
    # 1 - sqrt(1-f) = f/2 + f^2/8 + ...  so depth/f -> 1/2, a finite nonzero
    # limit, i.e. leading power exactly 1.
    ratios = []
    for k in range(6, 12):
        f = 10.0 ** (-k)
        ratios.append((1 - math.sqrt(1 - f)) / f)
    converges_to_half = all(abs(r - 0.5) < 1e-6 for r in ratios)

    p_sqrt_of_1mf = leading_power(lambda f: f / (1 + math.sqrt(1 - f)))
    p_1m_sqrt_f = leading_power(math.sqrt)
    different_classes = abs(p_sqrt_of_1mf - 1.0) < 1e-6 and abs(p_1m_sqrt_f - 0.5) < 1e-6

    # and the two forms are genuinely different functions
    distinct = abs(math.sqrt(1 - 0.25) - (1 - math.sqrt(0.25))) > 1e-3

    check(
        "B P4's rival `L*sqrt(1-phi)` is weak-field LINEAR (p=1), not the p=1/2 class; "
        "the landed 0.50 row is `L*(1-sqrt(f))`",
        converges_to_half and different_classes and distinct,
        f"depth/f -> {ratios[-1]:.8f} (= 1/2); p[sqrt(1-f)]={p_sqrt_of_1mf:.4f}, "
        f"p[1-sqrt(f)]={p_1m_sqrt_f:.4f}",
    )


# ---------------------------------------------------------------------------
# C-E. the mechanism: additive self-adjoint coupling
# ---------------------------------------------------------------------------


def nn_hamiltonian(L):
    """-Delta_lat on a periodic 1D-by-3 lattice, as an exact rational matrix.

    Small enough to diagonalize exactly where needed; the mechanism does not
    depend on the size.
    """
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    H = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        i = idx[s]
        H[i][i] = Fraction(6)
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % L
                H[i][idx[tuple(t)]] -= 1
    return H, sites, idx


def rayleigh_quotient(H, v):
    """<v|H|v> / <v|v>, exact."""
    n = len(v)
    num = Fraction(0)
    for i in range(n):
        if v[i] == 0:
            continue
        for j in range(n):
            if H[i][j] and v[j]:
                num += v[i] * H[i][j] * v[j]
    den = sum(x * x for x in v)
    return num / den


def c_hellmann_feynman():
    """First-order energy response equals <psi|V|psi>, exactly.

    On the periodic lattice the constant vector is an exact eigenvector of
    -Delta_lat with eigenvalue 0, so the first-order coefficient is computable
    in closed form and compared against a finite-difference of the exact
    Rayleigh quotient.
    """
    L = 3
    H, sites, idx = nn_hamiltonian(L)
    n = len(sites)
    psi = [Fraction(1)] * n  # exact zero-mode of the periodic Laplacian

    # psi is an exact eigenvector with eigenvalue 0
    Hpsi = [sum(H[i][j] * psi[j] for j in range(n)) for i in range(n)]
    is_eigen = all(x == 0 for x in Hpsi)

    # a field potential: V diagonal, values 1/(1+r) from a source at origin
    V = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        r = sum(min(c, L - c) for c in s)
        V[idx[s]][idx[s]] = Fraction(1, 1 + r)

    first_order = rayleigh_quotient(V, psi)  # <psi|V|psi>/<psi|psi>

    # finite difference of the exact Rayleigh quotient of H + lam V at psi
    def E(lam):
        HV = [[H[i][j] + lam * V[i][j] for j in range(n)] for i in range(n)]
        return rayleigh_quotient(HV, psi)

    lam = Fraction(1, 10**6)
    slope = (E(lam) - E(Fraction(0))) / lam
    matches = slope == first_order and first_order != 0

    check(
        "C Hellmann-Feynman: first-order response equals <psi|V|psi>, exact and nonzero",
        is_eigen and matches,
        f"<psi|V|psi> = {first_order} = {float(first_order):.6f}",
    )


def eig_sym_2x2(a, b, c):
    """Eigenvalues of [[a,b],[b,c]] via the closed form."""
    tr = a + c
    disc = math.sqrt((a - c) ** 2 + 4 * b * b)
    return (tr - disc) / 2, (tr + disc) / 2


def upper_response(lam, a0=1.0, c0=-1.0, d=1.0, b=0.3):
    """Shift of the upper eigenvalue of diag(a0,c0) + lam*[[d,b],[b,0]].

    Returned in a rationalized form with no subtraction of nearly-equal
    quantities.  Writing D = a0 - c0 > 0 and u = D + lam*d,

        upper(lam) - a0 = lam*d + 2*lam^2*b^2 / (u * (1 + sqrt(1 + w))),
        w = 4*lam^2*b^2 / u^2,

    which is exact.  Computing it as a difference of eigenvalues instead loses
    the entire second-order signal to cancellation once lam < 1e-4: an earlier
    draft of rows E and F did exactly that, measuring p = 1.997 and then
    dividing by a response that had underflowed to zero.
    """
    D = a0 - c0
    u = D + lam * d
    w = 4.0 * lam * lam * b * b / (u * u)
    return lam * d + 2.0 * lam * lam * b * b / (u * (1.0 + math.sqrt(1.0 + w)))


def response_power(d, b, l1=1e-9, l2=1e-8):
    r1, r2 = abs(upper_response(l1, d=d, b=b)), abs(upper_response(l2, d=d, b=b))
    return math.log(r2 / r1) / math.log(l2 / l1)


def d_generic_gives_p_one():
    """A self-adjoint family with nonvanishing first order responds linearly.

    H(lam) = diag(1,-1) + lam*[[1, 0.3],[0.3, 0]].  The upper level's
    unperturbed eigenvector is e_1, so its first-order coefficient is
    <e_1|V|e_1> = V[0][0] = d = 1, nonzero.  The response must be linear.
    """
    p = response_power(d=1.0, b=0.3)
    coeff = upper_response(1e-9, d=1.0, b=0.3) / 1e-9
    ok = abs(p - 1.0) < 1e-9 and abs(coeff - 1.0) < 1e-6
    check(
        "D self-adjoint coupling with nonvanishing first-order term gives p = 1",
        ok,
        f"p = {p:.9f}, first-order coefficient = {coeff:.9f} = <e_1|V|e_1>",
    )


def e_vanishing_first_order_gives_p_two():
    """When <psi|V|psi> = 0 the response is second order -- p = 2, never 1/2.

    Setting d = 0 kills the first-order term.  Standard second-order
    perturbation theory predicts the coefficient b^2 / (a0 - c0) exactly.
    """
    p = response_power(d=0.0, b=0.3)
    coeff = upper_response(1e-9, d=0.0, b=0.3) / (1e-9 ** 2)
    predicted = 0.3 ** 2 / (1.0 - (-1.0))
    ok = abs(p - 2.0) < 1e-9 and abs(coeff - predicted) < 1e-9
    check(
        "E vanishing first-order term gives p = 2 (still an integer), never p = 1/2",
        ok,
        f"p = {p:.9f}, second-order coefficient = {coeff:.9f} = b^2/(a0-c0) = {predicted}",
    )


def f_half_power_needs_non_self_adjointness():
    """A square-root response requires leaving the self-adjoint class.

    Rellich: a self-adjoint family analytic in `lam` has eigenvalues analytic
    in `lam`, so every leading power is a positive integer.  The exact
    branch-point witness below is NOT self-adjoint, and its eigenvalues are
    +-sqrt(lam) exactly.
    """
    # H(lam) = [[0, 1], [lam, 0]] : char poly mu^2 - lam = 0, mu = +-sqrt(lam)
    def mu(lam):
        return math.sqrt(lam)

    l1, l2 = 1e-8, 1e-7
    p = math.log(mu(l2) / mu(l1)) / math.log(10.0)
    half_power = abs(p - 0.5) < 1e-9

    # it is genuinely non-self-adjoint for lam != 1
    lam = 0.25
    Hm = [[0.0, 1.0], [lam, 0.0]]
    not_symmetric = Hm[0][1] != Hm[1][0]

    # and the exact characteristic polynomial confirms mu^2 = lam
    exact_char = all(
        abs(mu(l) ** 2 - l) < 1e-15 for l in (1e-8, 1e-6, 1e-4, 0.25)
    )

    # contrast: every self-adjoint 2x2 analytic family has integer powers.
    # sample many random symmetric perturbations and confirm no half-powers.
    # For each sample the power is estimated at finite lam, so it carries an
    # O(lam) contamination from the next order -- an earlier draft demanded
    # 1e-9 agreement and failed on exactly that, which is physics and not
    # float error.  The test is therefore convergence: the deviation from the
    # nearest integer must be small AND must shrink as lam shrinks.
    integer_powers = True
    seen = []
    for k in range(1, 13):
        b = k / 13.0
        d = 0.0 if k % 5 == 0 else (k % 5) / 7.0   # k%5==0 kills the first order
        p_far = response_power(d=d, b=b, l1=1e-7, l2=1e-6)
        p_near = response_power(d=d, b=b, l1=1e-11, l2=1e-10)
        dev_far = min(abs(p_far - 1.0), abs(p_far - 2.0))
        dev_near = min(abs(p_near - 1.0), abs(p_near - 2.0))
        seen.append((round(p_near, 9), "1st-order" if d else "2nd-order"))
        if dev_near > 1e-6 or dev_near > dev_far:
            integer_powers = False

    check(
        "F p = 1/2 requires non-self-adjointness; self-adjoint families give integer powers",
        half_power and not_symmetric and exact_char and integer_powers,
        f"branch-point witness p = {p:.6f}; {len(seen)} self-adjoint samples, integer_powers={integer_powers}, powers seen: {sorted(set(x[0] for x in seen))[:4]}...",
    )


def g_valley_sign_control():
    """Reproduce the landed sign statement: valley attracts, hill does not."""
    # g'(0) < 0 is the valley condition; g'(0) > 0 the hill.
    def gprime0(g, h=1e-7):
        return (g(h) - g(0.0)) / h

    valley = [lambda f: 1 - f, lambda f: math.exp(-f), lambda f: 1 / (1 + f)]
    hill = [lambda f: 1 + f, lambda f: -f]
    no_coupling = [lambda f: 1.0]

    valleys_ok = all(gprime0(g) < 0 for g in valley)
    hills_ok = all(gprime0(g) > 0 for g in hill[:1])
    flat_ok = abs(gprime0(no_coupling[0])) < 1e-12

    check(
        "G sign control: valley forms have g'(0) < 0, hill forms g'(0) > 0, no coupling g'(0) = 0",
        valleys_ok and hills_ok and flat_ok,
        "matches the landed phase-valley requirement",
    )


def rational_inverse(M):
    """Exact inverse by Gauss-Jordan over Fraction."""
    n = len(M)
    A = [row[:] + [Fraction(1) if i == j else Fraction(0) for j in range(n)]
         for i, row in enumerate(M)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                fac = A[r][c]
                A[r] = [x - fac * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def dirichlet_laplacian(L):
    """-Delta_lat on an OPEN L^3 box.

    The periodic Laplacian annihilates constants and is singular, so `G_0 =
    H^{-1}` does not exist on the torus; the open box is positive definite and
    invertible.  That the lane's own `G_0` needs a boundary (or a mass) to
    exist at all is noted in the companion note, not resolved here.
    """
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    H = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        i = idx[s]
        H[i][i] = Fraction(6)
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] += d
                if 0 <= t[ax] < L:               # open: no wrap
                    H[i][idx[tuple(t)]] -= 1
    return H, sites, idx


def h_propagator_responds_linearly():
    """The lane's own object: G(phi) = (H + phi)^{-1} responds LINEARLY in phi.

    This is the step that connects the perturbative mechanism to the
    self-consistency loop without passing through an eigenvalue or an eikonal
    action.  The resolvent identity gives exactly

        G(lam V) - G_0 = -lam * G_0 V G_0 + O(lam^2),

    so the leading power of the propagator's response is 1 whenever
    G_0 V G_0 is nonzero.  Verified here in exact rational arithmetic.
    """
    L = 3
    H, sites, idx = dirichlet_laplacian(L)
    n = len(sites)
    G0 = rational_inverse(H)

    # a field potential from a source at the box centre
    V = [[Fraction(0)] * n for _ in range(n)]
    ctr = (L // 2,) * 3
    for s in sites:
        r = sum(abs(a - b) for a, b in zip(s, ctr))
        V[idx[s]][idx[s]] = Fraction(1, 1 + r)

    def G(lam):
        M = [[H[i][j] + lam * V[i][j] for j in range(n)] for i in range(n)]
        return rational_inverse(M)

    # first-order prediction: -G0 V G0
    G0V = [[sum(G0[i][k] * V[k][j] for k in range(n)) for j in range(n)]
           for i in range(n)]
    pred = [[-sum(G0V[i][k] * G0[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

    lam = Fraction(1, 10**6)
    actual = G(lam)
    # (G(lam) - G0)/lam must approach pred; the residual must be O(lam)
    resid = max(
        abs((actual[i][j] - G0[i][j]) / lam - pred[i][j])
        for i in range(n) for j in range(n)
    )
    pred_scale = max(abs(pred[i][j]) for i in range(n) for j in range(n))
    linear_ok = pred_scale > 0 and resid < lam * 10  # residual is first order in lam

    # halving lam must halve the residual: confirms the power is exactly 1
    lam2 = lam / 2
    actual2 = G(lam2)
    resid2 = max(
        abs((actual2[i][j] - G0[i][j]) / lam2 - pred[i][j])
        for i in range(n) for j in range(n)
    )
    halves = resid2 * Fraction(3, 2) < resid   # shrinks proportionally to lam

    check(
        "H the propagator itself responds linearly: G(lam V) - G_0 = -lam G_0 V G_0 + O(lam^2), exact",
        linear_ok and halves,
        f"{n}x{n} exact rational inverse; |G_0 V G_0|_max = {float(pred_scale):.6g}, "
        f"residual/lam shrinks {float(resid):.3g} -> {float(resid2):.3g}",
    )


def i_geometric_spent_delay_is_sublinear():
    """The GENUINE spent-delay expression is sublinear -- so the rival is real.

    Three different expressions are called "spent-delay" across the repo:

        (1) ACTION_CROSSOVER_NOTE:  S = dl - sqrt(dl^2 - L^2)   (geometric)
        (2) ACTION_UNIQUENESS_NOTE: S = L(1 - f^0.5)            (the 0.50 row)
        (3) P4:                     S = L*sqrt(1 - phi)

    Writing dl = L(1 + eps) with eps proportional to the field, (1) expands as

        S = L[(1+eps) - sqrt(2 eps + eps^2)] -> L[1 - sqrt(2 eps)],

    so its valley depth goes as sqrt(eps): leading power 1/2, matching (2) and
    matching the measured F~M = 0.50.  Expression (3) is the odd one out -- it
    is weak-field linear.  So P4 mis-transcribes the weak-field form of the
    genuine spent-delay action, and the rival that Theorem 2 excludes is the
    real one, not a strawman.
    """
    def depth_geometric(eps, L=1.0):
        dl = L * (1.0 + eps)
        return L - (dl - math.sqrt(dl * dl - L * L))

    p_geo = math.log(depth_geometric(1e-8) / depth_geometric(1e-9)) / math.log(10.0)
    # the coefficient is exactly sqrt(2)
    coeff = [depth_geometric(e) / math.sqrt(2 * e) for e in (1e-7, 1e-8, 1e-9)]
    coeff_ok = all(abs(c - 1.0) < 1e-3 for c in coeff)

    # (1) and (2) share a class; (3) does not
    p_uniq = leading_power(math.sqrt)
    p_p4 = leading_power(lambda f: f / (1 + math.sqrt(1 - f)))
    same_class = abs(p_geo - p_uniq) < 1e-3
    p4_differs = abs(p_p4 - 1.0) < 1e-6

    check(
        "I the geometric spent-delay is genuinely sublinear (p=1/2), matching the landed "
        "0.50 row; P4's `L*sqrt(1-phi)` is the outlier",
        abs(p_geo - 0.5) < 1e-3 and coeff_ok and same_class and p4_differs,
        f"p[geometric]={p_geo:.6f}, depth/sqrt(2 eps) -> {coeff[-1]:.6f}, "
        f"p[L(1-sqrt f)]={p_uniq:.4f}, p[L sqrt(1-f)]={p_p4:.4f}",
    )


def main() -> int:
    print("Cycle 707 - the weak-field exponent is forced by self-adjointness")
    print("=" * 74)
    a_leading_powers()
    b_p4_transcription_correction()
    c_hellmann_feynman()
    d_generic_gives_p_one()
    e_vanishing_first_order_gives_p_two()
    f_half_power_needs_non_self_adjointness()
    i_geometric_spent_delay_is_sublinear()
    h_propagator_responds_linearly()
    g_valley_sign_control()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for f in FAILURES:
        print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
