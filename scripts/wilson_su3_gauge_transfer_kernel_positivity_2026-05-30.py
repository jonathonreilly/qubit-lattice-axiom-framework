#!/usr/bin/env python3
"""Audit-companion runner for WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY.

Establishes the GAUGE HALF (H1) of the interacting-SU(3) reflection-positivity
program: the Wilson single-(temporal-)link weight

    w(U) = exp( (beta / N_c) Re Tr U )                        (N_c = 3)

is a positive-definite class function on SU(3), equivalently its character
(Peter-Weyl / Fourier) coefficients

    c_lambda(beta) = integral_{SU(3)} w(U) conj(chi_lambda(U)) dU

are non-negative for every irrep lambda and every beta >= 0, equivalently the
Wilson gauge transfer kernel

    K(U, U') = exp( -beta ( 1 - Re Tr(U' U^dag) / N_c ) ) = e^{-beta} * w(U' U^dag)

is positive semidefinite (PSD) as a Gram kernel on SU(3) configurations.

The load-bearing, non-circular fact is that SU(3) tensor-product
(Clebsch-Gordan / Littlewood-Richardson) multiplicities are NON-NEGATIVE
INTEGERS, so (chi_3 + chi_3bar)^n expands with non-negative coefficients in the
character basis, and exp(.) of (beta>=0) times it inherits non-negative
coefficients term by term:

    c_lambda(beta)
      = sum_{n>=0} (1/n!) (beta/(2 N_c))^n
            * [ multiplicity of chi_lambda in (chi_3 + chi_3bar)^n ]  >= 0.

Checks (exact rational arithmetic where possible; Haar-MC with honest error
bands only where an integral over SU(3) is genuinely required):

  C0: torus self-consistency.  The exact trace-polynomial character formulas
      for the low SU(3) irreps agree with the Weyl character formula on
      generic (non-degenerate) torus points.

  C1: CG non-negativity engine (EXACT).  Decompose products of low SU(3)
      characters (3x3bar, 3x3, 3barx3bar, 8x3, 3x8, 6x3bar, ...) in the
      character basis using exact rational linear algebra in the
      (Tr U, Tr U^dag) polynomial ring.  Every multiplicity N^nu_{lam mu} is
      a NON-NEGATIVE INTEGER and matches the textbook decomposition.

  C2: positive expansion of (chi_3 + chi_3bar)^n (EXACT).  For n = 1..6 the
      class function (chi_3 + chi_3bar)^n has NON-NEGATIVE INTEGER character
      coefficients, hence each term of the exp-series for w is a non-negative
      combination of characters (beta >= 0).

  C3: c_lambda(beta) >= 0 for the low irreps over a beta grid, by Haar-MC.
      Reports the single smallest c_lambda found and its honest 1-sigma
      Monte-Carlo band; passes iff c_lambda > -k * SEM (k = 5).

  C4: transfer-kernel Gram PSD.  K(U_i, U_j) = w(U_j U_i^dag) is PSD on
      Haar-sampled SU(3) configs (min eigenvalue >= -tol).  The RP kernel
      exp(-beta(1 - Re Tr(U'U^dag)/N_c)) shares the same Gram spectrum up to
      the positive scalar e^{-beta}, so PSD transfers.

  C5: NON-TRIVIALITY control.  A deformed weight w~ = w - eps*chi_8 with a
      deliberately negative octet coefficient yields (a) a strictly negative
      c_8 and (b) a NON-PSD Gram with a strictly negative eigenvalue.  The
      PSD / c_lambda>=0 tests therefore have teeth.

Single deterministic seed (np.random.default_rng).  numpy + stdlib only.
Prints `SCORECARD PASS=N FAIL=0`.

Scope: GAUGE HALF ONLY.  No fermion determinant, no mixed OS transfer
representation (H2), no full interacting RP.
"""

from fractions import Fraction

import numpy as np

N_C = 3

# ---------------------------------------------------------------------------
# Low SU(3) irreps as highest-weight Dynkin labels (p, q),
#   dim = (p+1)(q+1)(p+q+2)/2.
# ---------------------------------------------------------------------------
IRREPS = {
    (0, 0): 1,    # trivial 1
    (1, 0): 3,    # fundamental 3
    (0, 1): 3,    # antifundamental 3bar
    (1, 1): 8,    # adjoint 8
    (2, 0): 6,    # 6
    (0, 2): 6,    # 6bar
    (3, 0): 10,   # 10
    (0, 3): 10,   # 10bar
    (2, 1): 15,   # 15
    (1, 2): 15,   # 15bar
}


def dim_irrep(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ===========================================================================
# Exact character algebra in the (t, tbar) = (Tr U, Tr U^dag) polynomial ring.
#
# A class function on SU(3) is, on the maximal torus, a Laurent polynomial in
# the eigenvalues that is symmetric and SU(3)-reduced; in terms of the two
# basic invariants t = Tr U (= e1) and tbar = Tr U^dag (= e2, since det U = 1)
# every low character is a POLYNOMIAL in (t, tbar).  We represent a class
# function as a dict { (i, j) : coeff } meaning sum coeff * t^i * tbar^j, with
# exact Fraction coefficients.
#
# The low SU(3) characters (verified against the Weyl character formula in C0):
#   chi_1     = 1
#   chi_3     = t
#   chi_3bar  = tbar
#   chi_8     = t*tbar - 1
#   chi_6     = t^2 - tbar
#   chi_6bar  = tbar^2 - t
#   chi_10    = t^3 - 2 t tbar + 1
#   chi_10bar = tbar^3 - 2 tbar t + 1
#   chi_15    = t^2 tbar - t - tbar^2            (Schur s_(3,1,0), reduced)
#   chi_15bar = tbar^2 t - tbar - t^2
# (chi_15 / chi_15bar verified by Jacobi-Trudi + Weyl in C0.)
# ===========================================================================
def _padd(a, b, scale=Fraction(1)):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + scale * v
    return {k: v for k, v in out.items() if v != 0}


def _pmul(a, b):
    out = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            k = (i1 + i2, j1 + j2)
            out[k] = out.get(k, Fraction(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


# Character polynomials in (t, tbar) with exact Fraction coefficients.
CHAR_POLY = {
    (0, 0): {(0, 0): Fraction(1)},
    (1, 0): {(1, 0): Fraction(1)},
    (0, 1): {(0, 1): Fraction(1)},
    (1, 1): {(1, 1): Fraction(1), (0, 0): Fraction(-1)},
    (2, 0): {(2, 0): Fraction(1), (0, 1): Fraction(-1)},
    (0, 2): {(0, 2): Fraction(1), (1, 0): Fraction(-1)},
    (3, 0): {(3, 0): Fraction(1), (1, 1): Fraction(-2), (0, 0): Fraction(1)},
    (0, 3): {(0, 3): Fraction(1), (1, 1): Fraction(-2), (0, 0): Fraction(1)},
    (2, 1): {(2, 1): Fraction(1), (1, 0): Fraction(-1), (0, 2): Fraction(-1)},
    (1, 2): {(1, 2): Fraction(1), (0, 1): Fraction(-1), (2, 0): Fraction(-1)},
}


def decompose_in_characters(poly, basis_labels):
    """Express a (t,tbar)-polynomial as an integer combination of characters.

    Greedy peeling by leading monomial: each character chi_{p,q} has a unique
    'top' monomial t^? tbar^? not shared (as a top) by lower-degree characters,
    so we can solve triangularly.  Returns dict {label: Fraction coeff} and the
    residual (should be empty).  Exact arithmetic.

    We order candidate characters by total monomial degree descending and, for
    each, identify its top monomial (highest i+j, ties by i) and subtract the
    multiple needed to cancel that monomial in the running remainder."""
    # Build (label, poly, top-monomial) and sort by descending top-degree.
    def topmon(p):
        # highest total degree, tie-break by larger i
        return max(p.keys(), key=lambda ij: (ij[0] + ij[1], ij[0]))

    cand = []
    for lab in basis_labels:
        cp = CHAR_POLY[lab]
        cand.append((lab, cp, topmon(cp)))
    # Sort so that we peel highest-degree characters first.
    cand.sort(key=lambda x: (x[2][0] + x[2][1], x[2][0]), reverse=True)

    rem = dict(poly)
    coeffs = {}
    for lab, cp, tm in cand:
        cur = rem.get(tm, Fraction(0))
        if cur == 0:
            coeffs[lab] = Fraction(0)
            continue
        lead = cp[tm]
        mult = cur / lead
        coeffs[lab] = mult
        rem = _padd(rem, cp, scale=-mult)
    return coeffs, rem


def check_weyl_consistency():
    """C0: trace-polynomial characters agree with the Weyl character formula
    on generic torus points (where the alternant ratio is well conditioned)."""
    rng = np.random.default_rng(101)

    def alternant(z, exps):
        M = np.array([[z[i] ** exps[j] for j in range(3)] for i in range(3)],
                     dtype=complex)
        return np.linalg.det(M)

    def weyl_char(p, q, z):
        return alternant(z, (p + q + 2, q + 1, 0)) / alternant(z, (2, 1, 0))

    ok = True
    maxerr = 0.0
    for _ in range(40):
        # Generic torus point with distinct eigenvalues.
        a, b = rng.uniform(0.2, 1.7), rng.uniform(2.2, 3.4)
        th = np.array([a, b, -a - b])
        z = np.exp(1j * th)
        if abs(alternant(z, (2, 1, 0))) < 1e-3:
            continue
        t = z.sum()
        tb = np.conj(t)
        for lab, cp in CHAR_POLY.items():
            val_poly = sum(complex(v) * (t ** i) * (tb ** j)
                           for (i, j), v in cp.items())
            val_weyl = weyl_char(*lab, z)
            err = abs(val_poly - val_weyl)
            maxerr = max(maxerr, err)
            if err > 1e-7:
                ok = False
    return ok, maxerr


def check_cg_nonnegativity():
    """C1: SU(3) tensor-product multiplicities N^nu_{lam mu} are NON-NEGATIVE
    INTEGERS (exact rational decomposition) and match textbook values."""
    basis = list(IRREPS.keys())
    # Textbook low SU(3) tensor products (only listing irreps inside our basis;
    # products whose full decomposition stays inside the basis also have their
    # dimension sum checked).
    cases = {
        ((1, 0), (0, 1)): {(1, 1): 1, (0, 0): 1},          # 3 x 3bar = 8 + 1
        ((1, 0), (1, 0)): {(2, 0): 1, (0, 1): 1},          # 3 x 3 = 6 + 3bar
        ((0, 1), (0, 1)): {(0, 2): 1, (1, 0): 1},          # 3bar x 3bar = 6bar + 3
        ((1, 1), (1, 0)): {(2, 1): 1, (0, 2): 1, (1, 0): 1},   # 8 x 3 = 15 + 6bar + 3
        ((1, 0), (1, 1)): {(2, 1): 1, (0, 2): 1, (1, 0): 1},   # 3 x 8 = 15 + 6bar + 3
        ((2, 0), (0, 1)): {(2, 1): 1, (1, 0): 1},          # 6 x 3bar = 15 + 3
    }
    ok = True
    min_mult = None
    max_resid = 0.0
    details = []
    for (lam, mu), want in cases.items():
        prod = _pmul(CHAR_POLY[lam], CHAR_POLY[mu])
        coeffs, rem = decompose_in_characters(prod, basis)
        # residual must be empty (full decomposition lands inside basis)
        resid = sum(abs(float(v)) for v in rem.values())
        max_resid = max(max_resid, resid)
        for lab, c in coeffs.items():
            if c.denominator != 1:
                ok = False  # not an integer
            iv = int(c)
            if min_mult is None or iv < min_mult:
                min_mult = iv
            if iv < 0:
                ok = False
            target = want.get(lab, 0)
            if iv != target:
                ok = False
                details.append((lam, mu, lab, iv, target))
        # dimension consistency: sum d_nu * N == d_lam * d_mu
        lhs = dim_irrep(*lam) * dim_irrep(*mu)
        rhs = sum(dim_irrep(*lab) * int(c) for lab, c in coeffs.items())
        if lhs != rhs:
            ok = False
            details.append(("dim", lam, mu, lhs, rhs))
        if resid > 1e-9:
            ok = False
    return ok, (min_mult if min_mult is not None else 0), max_resid, details


def check_positive_power_expansion():
    """C2: (chi_3 + chi_3bar)^n has NON-NEGATIVE INTEGER character coefficients
    for n = 1..6 (exact), so every term of the exp-series for w is a
    non-negative combination of characters."""
    basis = list(IRREPS.keys())
    # Extend the character basis closure under the relevant products: powers up
    # to 6 of (t + tbar) reach irreps beyond our 10-element table (e.g. 27,
    # 24, 35, ...).  To decompose EXACTLY we generate the full SU(3) character
    # table up to the needed highest weight on the fly via the Weyl character
    # formula evaluated symbolically is overkill; instead we verify the WEAKER
    # but sufficient statement directly: project (chi_3+chi_3bar)^n onto each
    # of the listed low irreps via exact monomial bookkeeping is not closed.
    #
    # Sufficient exact route: build a closed character ring up to highest
    # weight P by generating ALL CHAR_POLY for (p,q) with p+q <= P using the
    # recursion chi_{(p,q)} from products with the fundamental (Pieri /
    # explicit Weyl).  We generate the needed table programmatically.
    table = _full_char_table(max_pq=8)
    labels = list(table.keys())

    def base_poly():
        return _padd(table[(1, 0)], table[(0, 1)])

    ok = True
    min_coeff = None
    max_resid = 0.0
    base = base_poly()
    cur = {(0, 0): Fraction(1)}  # (chi_3+chi_3bar)^0 = 1
    for n in range(1, 7):
        cur = _pmul(cur, base)
        coeffs, rem = _decompose_full(cur, table, labels)
        resid = sum(abs(float(v)) for v in rem.values())
        max_resid = max(max_resid, resid)
        for lab, c in coeffs.items():
            if c.denominator != 1:
                ok = False
            iv = int(c)
            if min_coeff is None or iv < min_coeff:
                min_coeff = iv
            if iv < 0:
                ok = False
        if resid > 1e-9:
            ok = False
        # spot-check n=1 and n=2 against hand computation
        if n == 1:
            if int(coeffs.get((1, 0), 0)) != 1 or int(coeffs.get((0, 1), 0)) != 1:
                ok = False
        if n == 2:
            want2 = {(1, 1): 2, (0, 0): 2, (2, 0): 1, (0, 2): 1,
                     (1, 0): 1, (0, 1): 1}
            for lab, w in want2.items():
                if int(coeffs.get(lab, 0)) != w:
                    ok = False
    return ok, (min_coeff if min_coeff is not None else 0), max_resid


def _full_char_table(max_pq):
    """Generate SU(3) character polynomials in (t,tbar) for all (p,q) with
    p+q <= max_pq, via the explicit Weyl/Jacobi-Trudi recursion expressed in
    complete homogeneous symmetric polys h_k(e1=t, e2=tbar, e3=1).

    chi_{(p,q)} = Schur s_{lambda} with lambda = (p+q, q, 0).  Jacobi-Trudi:
      s_{(l1,l2,l3)} = det [[ h_{l1}, h_{l1+1}, h_{l1+2} ],
                            [ h_{l2-1}, h_{l2}, h_{l2+1} ],
                            [ h_{l3-2}, h_{l3-1}, h_{l3} ]]
    with h_{<0}=0, h_0=1, and the Newton recursion
      h_k = e1 h_{k-1} - e2 h_{k-2} + e3 h_{k-3},  e1=t, e2=tbar, e3=1.
    All exact in the (t,tbar) ring."""
    # complete homogeneous h_k as (t,tbar)-polynomials
    maxk = 2 * max_pq + 4
    h = {0: {(0, 0): Fraction(1)}}
    for k in range(-3, 1):
        if k < 0:
            h[k] = {}
    e1 = {(1, 0): Fraction(1)}
    e2 = {(0, 1): Fraction(1)}
    e3 = {(0, 0): Fraction(1)}
    for k in range(1, maxk + 1):
        term = _pmul(e1, h.get(k - 1, {}))
        term = _padd(term, _pmul(e2, h.get(k - 2, {})), scale=Fraction(-1))
        term = _padd(term, _pmul(e3, h.get(k - 3, {})))
        h[k] = term

    def H(k):
        return h.get(k, {}) if k >= 0 else {}

    def schur(l1, l2, l3):
        # 3x3 Jacobi-Trudi determinant expanded exactly over the (t,tbar) ring.
        M = [
            [H(l1), H(l1 + 1), H(l1 + 2)],
            [H(l2 - 1), H(l2), H(l2 + 1)],
            [H(l3 - 2), H(l3 - 1), H(l3)],
        ]
        # cofactor expansion along the first row (entries are polynomials)
        def minor(i, j):
            rows = [r for ri, r in enumerate(M) if ri != i]
            return [[rows[a][b] for b in range(3) if b != j] for a in range(2)]
        def det2(m):
            return _padd(_pmul(m[0][0], m[1][1]),
                         _pmul(m[0][1], m[1][0]), scale=Fraction(-1))
        det = {}
        for j in range(3):
            sign = Fraction((-1) ** j)
            det = _padd(det, _pmul(M[0][j], det2(minor(0, j))), scale=sign)
        return det

    table = {}
    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            table[(p, q)] = schur(p + q, q, 0)
    return table


def _decompose_full(poly, table, labels):
    """Exact triangular decomposition of a (t,tbar)-polynomial in a FULL
    character table (closed under the monomials present)."""
    def topmon(p):
        return max(p.keys(), key=lambda ij: (ij[0] + ij[1], ij[0]))

    cand = [(lab, table[lab], topmon(table[lab])) for lab in labels]
    cand.sort(key=lambda x: (x[2][0] + x[2][1], x[2][0]), reverse=True)
    rem = dict(poly)
    coeffs = {}
    for lab, cp, tm in cand:
        cur = rem.get(tm, Fraction(0))
        if cur == 0:
            continue
        mult = cur / cp[tm]
        coeffs[lab] = coeffs.get(lab, Fraction(0)) + mult
        rem = _padd(rem, cp, scale=-mult)
    return coeffs, rem


# ===========================================================================
# Haar sampling and Monte-Carlo character integrals (C3, C4, C5).
# ===========================================================================
def haar_su3(rng, n=1):
    out = np.empty((n, 3, 3), dtype=complex)
    for k in range(n):
        Z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / np.sqrt(2.0)
        Q, R = np.linalg.qr(Z)
        ph = np.diagonal(R) / np.abs(np.diagonal(R))
        Q = Q * ph[np.newaxis, :]
        d = np.linalg.det(Q)
        Q = Q / (d ** (1.0 / 3.0))
        out[k] = Q
    return out


def char_value(lab, t, tb):
    """Evaluate a low SU(3) character at (t, tbar) via its exact polynomial."""
    cp = CHAR_POLY[lab]
    return sum(complex(v) * (t ** i) * (tb ** j) for (i, j), v in cp.items())


def c_lambda_mc(lab, beta, traces):
    """Haar-MC c_lambda(beta) = <w, chi_lambda> and SEM, given precomputed
    traces t_k = Tr U_k."""
    re = np.empty(len(traces))
    for k, t in enumerate(traces):
        w = np.exp((beta / N_C) * t.real)
        re[k] = (w * np.conj(char_value(lab, t, np.conj(t)))).real
    return re.mean(), re.std(ddof=1) / np.sqrt(len(re))


def c_lambda_exact_series(lab, beta, nmax, table, labels, base):
    """Exact partial sum of the non-negative CG series

        c_lambda(beta) = sum_{n=0}^{nmax} (beta/(2 N_c))^n / n!
                            * [ mult of chi_lambda in (chi_3+chi_3bar)^n ].

    Every multiplicity is a non-negative integer (C1/C2 engine), so each term
    is >= 0 for beta >= 0; the partial sum is therefore a non-negative lower
    bound that converges UP to c_lambda(beta).  Exact integer multiplicities,
    float accumulation of the (manifestly non-negative) terms."""
    from math import factorial
    x = beta / (2.0 * N_C)
    cur = {(0, 0): Fraction(1)}
    total = 0.0
    all_nonneg = True
    for n in range(0, nmax + 1):
        coeffs, _ = _decompose_full(cur, table, labels)
        mult = coeffs.get(lab, Fraction(0))
        if mult.denominator != 1 or int(mult) < 0:
            all_nonneg = False
        total += (x ** n) / factorial(n) * float(int(mult))
        cur = _pmul(cur, base)
    return total, all_nonneg


def check_c_lambda_nonneg(rng):
    """C3: c_lambda(beta) >= 0 for low irreps over a beta grid.

    Two independent routes, cross-checked:
      (a) the EXACT non-negative CG series partial sum (manifestly >= 0,
          every term a non-negative-integer multiplicity times a positive
          scalar), and
      (b) a Haar Monte-Carlo estimate of c_lambda = <w, chi_lambda>.
    Passes iff (a) every series term is a non-negative integer, (b) every MC
    estimate satisfies c_lambda > -5*SEM, and (c) the MC estimate agrees with
    the exact series within 5*SEM (so the MC is actually measuring the
    non-negative quantity, not something else)."""
    betas = [0.0, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0]
    nsamp = 400_000
    Us = haar_su3(rng, nsamp)
    traces = np.array([np.trace(U) for U in Us])

    table = _full_char_table(max_pq=14)
    labels = list(table.keys())
    base = _padd(table[(1, 0)], table[(0, 1)])

    k = 5.0
    nmax = 16
    ok = True
    smallest = None       # smallest MC estimate (value, sem, lab, beta)
    max_series_gap = 0.0  # worst |MC - exact_series| / SEM
    min_series = np.inf   # smallest EXACT series value found (must be >= 0)
    for beta in betas:
        for lab in IRREPS:
            mean, sem = c_lambda_mc(lab, beta, traces)
            exact, nonneg = c_lambda_exact_series(lab, beta, nmax, table,
                                                  labels, base)
            if not nonneg:
                ok = False
            min_series = min(min_series, exact)
            if smallest is None or mean < smallest[0]:
                smallest = (mean, sem, lab, beta)
            if mean < -k * sem:
                ok = False
            # MC must agree with the exact non-negative series.
            if sem > 0 and abs(mean - exact) > k * sem:
                ok = False
            if sem > 0:
                max_series_gap = max(max_series_gap, abs(mean - exact) / sem)
    return ok, smallest, min_series, max_series_gap


def gram_min_eig(Us, weight_fn):
    m = len(Us)
    K = np.empty((m, m), dtype=complex)
    for i in range(m):
        for j in range(m):
            g = Us[j] @ Us[i].conj().T
            K[i, j] = weight_fn(g)
    K = 0.5 * (K + K.conj().T)
    ev = np.linalg.eigvalsh(K)
    return ev.min(), ev.max()


def check_kernel_psd(rng):
    """C4: K(U_i,U_j) = w(U_j U_i^dag) PSD on sampled configs; RP kernel
    exp(-beta(1 - Re Tr/N_c)) shares the spectrum up to e^{-beta} > 0."""
    betas = [0.5, 1.0, 2.0, 4.0, 6.0]
    m = 60
    ok = True
    worst = np.inf
    for beta in betas:
        Us = haar_su3(rng, m)
        w_fn = lambda U, b=beta: np.exp((b / N_C) * np.real(np.trace(U)))
        mn, mx = gram_min_eig(Us, w_fn)
        worst = min(worst, mn / max(mx, 1.0))
        if mn < -1e-8 * max(1.0, mx):
            ok = False
        rp_fn = lambda U, b=beta: np.exp(-b * (1.0 - np.real(np.trace(U)) / N_C))
        mn_rp, mx_rp = gram_min_eig(Us, rp_fn)
        if mn_rp < -1e-8 * max(1.0, mx_rp):
            ok = False
    return ok, worst


def check_nontriviality_control(rng):
    """C5: deformed weight w~ = w - eps*chi_8 with deliberately NEGATIVE octet
    coefficient gives (a) c_8(w~) < 0 and (b) a NON-PSD Gram."""
    beta = 2.0
    eps = 0.6
    nsamp = 300_000
    Us = haar_su3(rng, nsamp)
    traces = np.array([np.trace(U) for U in Us])

    c8_w, _ = c_lambda_mc((1, 1), beta, traces)

    # c_8 of deformed weight: c_8(w) - eps (since <chi_8,chi_8>=1).
    re = np.empty(nsamp)
    for k, t in enumerate(traces):
        wt = np.exp((beta / N_C) * t.real) - eps * char_value((1, 1), t, np.conj(t)).real
        re[k] = (wt * np.conj(char_value((1, 1), t, np.conj(t)))).real
    c8_tilde = re.mean()
    sem_tilde = re.std(ddof=1) / np.sqrt(nsamp)
    neg_coeff_ok = c8_tilde < -3.0 * sem_tilde

    # Non-PSD Gram of the deformed weight.
    m = 120
    Ug = haar_su3(rng, m)

    def w_tilde(U):
        t = np.trace(U)
        return np.exp((beta / N_C) * t.real) - eps * char_value((1, 1), t, np.conj(t)).real

    mn, mx = gram_min_eig(Ug, w_tilde)
    nonpsd_ok = mn < -1e-6 * max(1.0, mx)

    return bool(neg_coeff_ok and nonpsd_ok), (c8_w, c8_tilde, sem_tilde, mn, mx)


def main():
    rng = np.random.default_rng(20260530)

    c0_ok, c0_err = check_weyl_consistency()
    c1_ok, c1_minmult, c1_resid, c1_details = check_cg_nonnegativity()
    c2_ok, c2_min, c2_resid = check_positive_power_expansion()
    c3_ok, smallest, min_series, series_gap = check_c_lambda_nonneg(rng)
    c4_ok, c4_worst = check_kernel_psd(rng)
    c5_ok, c5_info = check_nontriviality_control(rng)

    checks = [
        ("C0_weyl_vs_tracepoly_characters", c0_ok),
        ("C1_cg_tensor_multiplicities_nonneg_integers", c1_ok),
        ("C2_positive_power_expansion_chi3_plus_chi3bar", c2_ok),
        ("C3_c_lambda_nonneg_over_beta_grid_MC", c3_ok),
        ("C4_wilson_transfer_kernel_gram_PSD", c4_ok),
        ("C5_nontriviality_control_negative_octet", c5_ok),
    ]

    print("# WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY runner")
    print(f"# MC seed=20260530 (np.random.default_rng)")
    print(f"# C0 max |Weyl - tracepoly| over generic torus pts = {c0_err:.3e}")
    print(f"# C1 exact CG: min multiplicity = {c1_minmult}, "
          f"max residual = {c1_resid:.3e}")
    if c1_details:
        print(f"#    C1 mismatches: {c1_details}")
    print(f"# C2 exact: min char-power coeff over n=1..6 = {c2_min}, "
          f"max residual = {c2_resid:.3e}")
    sm_val, sm_sem, sm_lab, sm_beta = smallest
    print(f"# C3 smallest MC c_lambda = {sm_val:.6e} +/- {sm_sem:.2e} (1-SEM) "
          f"at irrep {sm_lab} (dim {IRREPS[sm_lab]}), beta={sm_beta}; "
          f"pass band: c_lambda > -5*SEM = {-5*sm_sem:.2e}")
    print(f"#    smallest EXACT non-negative CG-series c_lambda over grid = "
          f"{min_series:.3e} (>= 0); worst |MC - exact|/SEM = {series_gap:.2f}")
    print(f"# C4 worst relative Gram min-eig over beta grid = {c4_worst:.3e}")
    c8_w, c8_t, sem_t, mn, mx = c5_info
    print(f"# C5 control: c_8(w,beta=2) ~ {c8_w:.4f}; deformed c_8(w~) = "
          f"{c8_t:.4f} +/- {sem_t:.2e} (expect <0); deformed Gram min-eig = "
          f"{mn:.4f} (max {mx:.2f}, expect <0)")
    print()

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
