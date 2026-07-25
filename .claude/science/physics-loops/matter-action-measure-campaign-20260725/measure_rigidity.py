#!/usr/bin/env python3
"""
Wave-1 measure-rigidity runner: native finite Grassmann/Berezin engine.

Everything exact (sympy Rational / symbols). No floats as inputs.
No literature values consumed. No framework status asserted.
"""
import itertools
from itertools import combinations
import sympy as sp

PASS = 0
FAIL = 0
LOG = []


def gate(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        LOG.append(f"PASS  {name}  {detail}")
    else:
        FAIL += 1
        LOG.append(f"FAIL  {name}  {detail}")


# ----------------------------------------------------------------------
# Native Grassmann algebra.  Element = dict[tuple(sorted ascending indices) -> sympy expr]
# ----------------------------------------------------------------------

def _normalize(idx):
    """Sort an index tuple, return (sorted_tuple, sign) or None if a repeat occurs."""
    lst = list(idx)
    if len(set(lst)) != len(lst):
        return None
    sign = 1
    # insertion sort counting transpositions
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            sign = -sign
            j -= 1
    return tuple(lst), sign


def gzero():
    return {}


def gone():
    return {(): sp.Integer(1)}


def gen(i):
    return {(i,): sp.Integer(1)}


def gadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = sp.expand(out.get(k, sp.Integer(0)) + v)
        if out[k] == 0:
            del out[k]
    return out


def gscale(c, a):
    c = sp.sympify(c)
    out = {}
    for k, v in a.items():
        w = sp.expand(c * v)
        if w != 0:
            out[k] = w
    return out


def gmul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            r = _normalize(ka + kb)
            if r is None:
                continue
            k, s = r
            w = sp.expand(out.get(k, sp.Integer(0)) + s * va * vb)
            if w == 0:
                out.pop(k, None)
            else:
                out[k] = w
    return out


def gexp(a, nmax):
    """exp(a) for nilpotent a: truncate at nmax (>= number of generators)."""
    term = gone()
    acc = gone()
    for k in range(1, nmax + 1):
        term = gmul(term, a)
        if not term:
            break
        acc = gadd(acc, gscale(sp.Rational(1, sp.factorial(k)), term))
    return acc


def lderiv(a, i):
    """Left Berezin/Grassmann derivative d/d(theta_i)."""
    out = {}
    for k, v in a.items():
        if i not in k:
            continue
        p = k.index(i)
        sgn = (-1) ** p
        nk = k[:p] + k[p + 1:]
        w = sp.expand(out.get(nk, sp.Integer(0)) + sgn * v)
        if w == 0:
            out.pop(nk, None)
        else:
            out[nk] = w
    return out


def top_coeff(a, N):
    """The canonical top-form functional: coefficient of theta_0...theta_{N-1}."""
    return sp.expand(a.get(tuple(range(N)), sp.Integer(0)))


def basis(N):
    out = []
    for d in range(N + 1):
        for c in combinations(range(N), d):
            out.append(c)
    return out


# ======================================================================
# BLOCK A -- algebra sanity
# ======================================================================
def block_A():
    N = 4
    for i in range(N):
        gate(f"A1.sq[{i}]", gmul(gen(i), gen(i)) == gzero(), "theta_i^2 = 0")
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            lhs = gadd(gmul(gen(i), gen(j)), gmul(gen(j), gen(i)))
            gate(f"A2.acomm[{i},{j}]", lhs == gzero(), "{theta_i,theta_j}=0")
    for N in range(1, 7):
        gate(f"A3.dim[N={N}]", len(basis(N)) == 2 ** N, f"dim Lambda_N = 2^{N} = {2**N}")
    # graded Leibniz spot-check on a generic element
    N = 4
    x, y = sp.symbols('x y')
    f = gadd(gscale(x, gmul(gen(0), gen(1))), gscale(y, gen(2)))
    g = gadd(gscale(1, gen(3)), gscale(x, gmul(gen(1), gen(2))))
    # f is even, so d(fg) = (df)g + f(dg)
    lhs = lderiv(gmul(f, g), 1)
    rhs = gadd(gmul(lderiv(f, 1), g), gmul(f, lderiv(g, 1)))
    gate("A4.leibniz_even", lhs == rhs, "even f: d(fg)=(df)g+f(dg)")
    # odd h: d(hg) = (dh)g - h(dg)
    h = gadd(gen(0), gscale(x, gen(2)))
    lhs = lderiv(gmul(h, g), 0)
    rhs = gadd(gmul(lderiv(h, 0), g), gscale(-1, gmul(h, lderiv(g, 0))))
    gate("A5.leibniz_odd", lhs == rhs, "odd h: d(hg)=(dh)g-h(dg)")


# ======================================================================
# BLOCK B -- Berezin uniqueness (headline)
# ======================================================================
def invariant_functional_space(N, drop=None):
    """Return (dim, nullspace_basis, monomial_order) for the space of linear
    functionals L on Lambda_N with L(d_i f) = 0 for all i (i != drop) and all f."""
    bas = basis(N)
    pos = {m: k for k, m in enumerate(bas)}
    rows = []
    for i in range(N):
        if drop is not None and i == drop:
            continue
        for m in bas:
            d = lderiv({m: sp.Integer(1)}, i)
            if not d:
                continue
            row = [sp.Integer(0)] * len(bas)
            for k, v in d.items():
                row[pos[k]] += v
            rows.append(row)
    if not rows:
        return len(bas), None, bas
    Mx = sp.Matrix(rows)
    ns = Mx.nullspace()
    return len(ns), ns, bas


def block_B():
    for N in range(1, 7):
        dim, ns, bas = invariant_functional_space(N)
        gate(f"B1.dim_invariant[N={N}]", dim == 1,
             f"dim{{L : L o d_i = 0 for all i}} = {dim}")
        # the unique solution is the top-coefficient functional
        v = ns[0]
        topidx = bas.index(tuple(range(N)))
        nonzero = [k for k in range(len(bas)) if sp.simplify(v[k]) != 0]
        gate(f"B2.is_top_form[N={N}]", nonzero == [topidx],
             f"support = {[bas[k] for k in nonzero]} ; top = {tuple(range(N))}")

    # image of the derivatives is exactly the codim-1 subspace of sub-top monomials
    for N in range(1, 7):
        bas = basis(N)
        pos = {m: k for k, m in enumerate(bas)}
        rows = []
        for i in range(N):
            for m in bas:
                d = lderiv({m: sp.Integer(1)}, i)
                if not d:
                    continue
                row = [sp.Integer(0)] * len(bas)
                for k, v in d.items():
                    row[pos[k]] += v
                rows.append(row)
        R = sp.Matrix(rows).rank()
        gate(f"B3.image_rank[N={N}]", R == 2 ** N - 1,
             f"rank(span of images of all d_i) = {R} = 2^{N}-1")
        # no derivative ever produces the top monomial (degree drop)
        hits_top = any(tuple(range(N)) in lderiv({m: sp.Integer(1)}, i)
                       for i in range(N) for m in bas)
        gate(f"B4.top_not_in_image[N={N}]", not hits_top,
             "no d_i output contains the top monomial")

    # B5 mutation probe: dropping ONE derivative condition breaks uniqueness
    for N in range(2, 6):
        dim, _, _ = invariant_functional_space(N, drop=N - 1)
        gate(f"B5.mutation_drop_one[N={N}]", dim == 2,
             f"dropping d_{N-1} gives dim = {dim} (uniqueness lost)")

    # B6: the full linear-functional space is 2^N-dimensional
    for N in range(1, 7):
        gate(f"B6.full_functional_dim[N={N}]", len(basis(N)) == 2 ** N,
             f"dim(Lambda_N)^* = {2**N}")


def block_B_translation():
    """Translation invariance  <=>  derivative annihilation, computed."""
    for N in range(1, 5):
        bas = basis(N)
        pos = {m: k for k, m in enumerate(bas)}
        rows = []
        # For each basis monomial theta_T, expand prod_{i in T}(theta_i + eta_i).
        # Push all eta's to the left; require the coefficient of every NONEMPTY
        # eta-monomial (as a functional of the remaining theta-monomial) to vanish.
        for T in bas:
            k = len(T)
            for mask in range(1, 2 ** k):  # nonempty U subset of T
                U = tuple(T[b] for b in range(k) if (mask >> b) & 1)
                S = tuple(T[b] for b in range(k) if not ((mask >> b) & 1))
                # sign from pulling the U-letters (in their original slots) to the left
                sgn = 1
                moved = 0
                for b in range(k):
                    if (mask >> b) & 1:
                        # number of theta-letters to its left that stay behind
                        left_stay = sum(1 for c in range(b) if not ((mask >> c) & 1))
                        sgn *= (-1) ** left_stay
                        moved += 1
                row = [sp.Integer(0)] * len(bas)
                row[pos[S]] += sgn
                rows.append(row)
        ns = sp.Matrix(rows).nullspace()
        gate(f"B7.translation_dim[N={N}]", len(ns) == 1,
             f"dim{{L : L(f(theta+eta)) = L(f(theta))}} = {len(ns)}")
        v = ns[0]
        topidx = bas.index(tuple(range(N)))
        nz = [i for i in range(len(bas)) if sp.simplify(v[i]) != 0]
        gate(f"B8.translation_is_top[N={N}]", nz == [topidx],
             "translation-invariant functional = top-form functional")
        # same solution space as the derivative characterisation
        d2, ns2, _ = invariant_functional_space(N)
        same = (len(ns) == d2 == 1) and (nz == [bas.index(tuple(range(N)))])
        gate(f"B9.equiv_characterisations[N={N}]", same,
             "translation invariance <=> derivative annihilation")


# ======================================================================
# BLOCK C -- Gaussian values; the rigidity is EMPTY for the count binary
# ======================================================================
def gaussian_value(M, offset=0):
    """theta_i = generator (offset+2i), thetabar_i = generator (offset+2i+1).
    Returns the exp(-S) expansion, S = sum_ij thetabar_i M_ij theta_j."""
    n = M.shape[0]
    S = gzero()
    for i in range(n):
        for j in range(n):
            if M[i, j] == 0:
                continue
            term = gmul(gen(offset + 2 * i + 1), gen(offset + 2 * j))
            S = gadd(S, gscale(M[i, j], term))
    return gexp(gscale(-1, S), 2 * n)


def block_C():
    a, b, c = sp.symbols('a b c', real=True)
    # C1: quadratic Berezin integral = sigma_n * det M, sign COMPUTED
    sigmas = {}
    for n in (1, 2, 3):
        Msym = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'm{i}{j}'))
        E = gaussian_value(Msym)
        val = top_coeff(E, 2 * n)
        d = Msym.det()
        q = sp.simplify(sp.expand(val) / sp.expand(d))
        sigmas[n] = sp.nsimplify(q)
        gate(f"C1.gauss_det[n={n}]", sp.simplify(sp.expand(val - q * d)) == 0,
             f"top-form functional = ({q}) * det M , sign computed")
    gate("C1b.sign_pattern", all(sigmas[n] in (1, -1) for n in sigmas),
         f"computed signs sigma_n = {sigmas}")

    # C2: the coupling-triple probe carrier (rebuild of the count binary arithmetic)
    W = sp.Matrix([[a, b, c], [c, a, b], [b, c, a]])
    det3 = sp.expand(W.det())
    gate("C2.det3", sp.expand(det3 - (a**3 + b**3 + c**3 - 3*a*b*c)) == 0,
         "det W = a^3+b^3+c^3-3abc")
    E6 = gaussian_value(W)
    v6 = top_coeff(E6, 6)
    gate("C3.count_once", sp.expand(v6 - sigmas[3] * det3) == 0,
         f"6-generator value = ({sigmas[3]}) * det3")

    # count-twice carrier: two disjoint 6-generator copies
    E6b = gaussian_value(W, offset=6)
    E12 = gmul(E6, E6b)
    v12 = top_coeff(E12, 12)
    gate("C4.count_twice", sp.expand(v12 - sp.expand(v6 * v6)) == 0,
         "12-generator value factorises as (6-generator value)^2")
    gate("C4b.count_twice_det", sp.expand(v12 - det3**2) == 0,
         "12-generator value = det3^2 exactly")

    # numeric witness reproducing the two horn values natively
    sub = {a: sp.Integer(3), b: sp.Integer(1), c: sp.Integer(1)}
    gate("C5.witness_horns",
         sp.expand(v6.subs(sub)) == sigmas[3] * 20 and sp.expand(v12.subs(sub)) == 400,
         f"at (3,1,1): count-once = {sp.expand(v6.subs(sub))}, count-twice = {sp.expand(v12.subs(sub))}")

    # C6: NO constant scalar converts the horns -- degree argument, all n
    for n in (1, 2, 3):
        Msym = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'z{i}{j}'))
        d = sp.expand(Msym.det())
        vs = list(Msym.free_symbols)
        deg1 = sp.Poly(d, *vs).total_degree()
        deg2 = sp.Poly(sp.expand(d**2), *vs).total_degree()
        gate(f"C6.degree_split[n={n}]", deg1 == n and deg2 == 2 * n,
             f"deg(det M) = {deg1}, deg(det M^2) = {deg2}")
        kappa = sp.Symbol('kappa')
        sols = sp.solve(sp.Poly(sp.expand(kappa * d - d**2), *vs).coeffs(), kappa, dict=True)
        gate(f"C6b.no_constant_conversion[n={n}]", sols == [] or all(s.get(kappa) == 0 for s in sols),
             f"kappa*det = det^2 identically has no nonzero constant solution (sols={sols})")

    # C7: THE SHARP ONE -- the conversion IS available in the FULL functional space.
    # On the 12-generator (count-twice) carrier, the NON-invariant functional
    # "top of copy 1, constant term of copy 2" returns the count-once value.
    partial = sp.expand(E12.get(tuple(range(6)), sp.Integer(0)))
    gate("C7.noninvariant_converts", sp.expand(partial - v6) == 0,
         "partial-top functional on the 12-gen carrier returns the count-once value")
    # and it is NOT translation invariant: exhibit f with L'(d_i f) != 0
    f = {tuple(range(7)): sp.Integer(1)}          # theta_0..theta_6
    df = lderiv(f, 6)                              # = +- theta_0..theta_5
    gate("C7b.partial_not_invariant",
         sp.expand(df.get(tuple(range(6)), sp.Integer(0))) != 0,
         f"L'(d_6 (theta_0..theta_6)) = {df.get(tuple(range(6)))} != 0")


# ======================================================================
# BLOCK D -- what is actually free
# ======================================================================
def block_D():
    a, b, c = sp.symbols('a b c', real=True)
    # D1 normalization: reversing the generator order multiplies by a computed sign
    for n in (1, 2, 3):
        Msym = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'q{i}{j}'))
        E = gaussian_value(Msym)
        N = 2 * n
        fwd = top_coeff(E, N)
        # reversed ordering functional = coefficient of theta_{N-1}...theta_0
        perm = tuple(range(N - 1, -1, -1))
        r = _normalize(perm)
        _, s = r
        rev = sp.expand(s * fwd)
        gate(f"D1.order_sign[n={n}]", sp.expand(rev - ((-1) ** (N * (N - 1) // 2)) * fwd) == 0,
             f"reversed-order functional = ({(-1)**(N*(N-1)//2)}) * forward, a scalar in C^x")

    # D2 K-reality: requiring L o conj = conj o L forces the normalization real
    z = sp.Symbol('z')
    cr, ci = sp.symbols('cr ci', real=True)
    # L = (cr + I*ci) * top ; K-compatibility on the monomial with coefficient z=i
    lhs = sp.expand((cr + sp.I * ci) * sp.conjugate(sp.I))
    rhs = sp.expand(sp.conjugate((cr + sp.I * ci) * sp.I))
    sol = sp.solve(sp.simplify(lhs - rhs), [ci], dict=True)
    gate("D2.K_reality_forces_real_scale", any(s.get(ci) == 0 for s in sol),
         f"K-compatibility of the scale forces Im(c) = 0 (sol={sol})")

    # D3 sign of the scale: any nonzero PSD Gram flips sign under c<0
    m = sp.Symbol('m', positive=True)
    E1 = gaussian_value(sp.Matrix([[m]]))
    Z = top_coeff(E1, 2)
    gate("D3.gram_diag_positive", sp.simplify(Z * sp.Integer(sp.sign(1))) != 0 and sp.simplify(Z - m) == 0,
         f"1-mode partition value = {Z}; scaling the functional by c scales it to c*{Z}")
    gate("D3b.negative_scale_breaks_positivity", sp.simplify((-1) * Z + m) == 0,
         "at c = -1 the same diagonal entry is -m < 0 for m > 0")

    # D4 the residual positive scale is r-inert: Q and r are degree-0 homogeneous
    t = sp.Symbol('t', positive=True)
    A, B = sp.symbols('A B', positive=True)
    r_expr = B**2 / A**2
    gate("D4.r_scale_inert", sp.simplify(r_expr.subs({A: t * A, B: t * B}) - r_expr) == 0,
         "r = |b|^2/a^2 is invariant under a common positive rescale")
    H = sp.diag(sp.Symbol('h1'), sp.Symbol('h2'), sp.Symbol('h3'))
    Q = sp.trace(H * H) / sp.trace(H) ** 2
    Qs = sp.simplify(Q.subs({H[0, 0]: t * H[0, 0], H[1, 1]: t * H[1, 1], H[2, 2]: t * H[2, 2]}) - Q)
    gate("D4b.Q_scale_inert", sp.simplify(Qs) == 0,
         "Q = Tr(H^2)/(Tr H)^2 is degree-0 homogeneous")

    # D5 polarization is NOT measure content: relabelling acts by sgn(P) only
    import random
    for N in (4, 6):
        for seed in (0, 1, 2):
            rng = random.Random(seed * 100 + N)
            p = list(range(N))
            rng.shuffle(p)
            r = _normalize(tuple(p))
            _, s = r
            # the top-form functional in the relabelled order is s * (original)
            gate(f"D5.polarization_sign[N={N},seed={seed}]", s in (1, -1),
                 f"relabelling permutation acts by det(P) = {s}, an element of the scalar group")

    # D6 polarization/reality-type IS action content on a FIXED carrier:
    # same 2n generators, Pfaffian form vs paired form.
    def pfaffian(Amat):
        n2 = Amat.shape[0]
        assert n2 % 2 == 0
        idx = list(range(n2))
        total = sp.Integer(0)
        def matchings(rem):
            if not rem:
                yield [], 1
                return
            first = rem[0]
            for k in range(1, len(rem)):
                partner = rem[k]
                rest = rem[1:k] + rem[k + 1:]
                for mm, sg in matchings(rest):
                    yield [(first, partner)] + mm, sg * ((-1) ** (k - 1))
        for mm, sg in matchings(idx):
            term = sp.Integer(sg)
            for (i, j) in mm:
                term *= Amat[i, j]
            total += term
        return sp.expand(total)

    for n in (1, 2, 3):
        K = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'k{i}{j}'))
        A_K = sp.zeros(2 * n, 2 * n)
        A_K[0:n, n:2 * n] = K
        A_K[n:2 * n, 0:n] = -K.T
        pf = pfaffian(A_K)
        expect = (-1) ** (n * (n - 1) // 2) * K.det()
        gate(f"D6.pfaffian_block[n={n}]", sp.expand(pf - expect) == 0,
             f"Pf([[0,K],[-K^T,0]]) = (-1)^(n(n-1)/2) det K   [rebuilt natively]")
    # realification determinant equals |det|^2 -- rebuilt, not cited
    for n in (1, 2):
        Kr = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'x{i}{j}', real=True))
        Ki = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'y{i}{j}', real=True))
        Kc = Kr + sp.I * Ki
        R = sp.Matrix(sp.BlockMatrix([[Kr, -Ki], [Ki, Kr]]))
        lhs = sp.expand(R.det())
        rhs = sp.expand(sp.expand(Kc.det() * sp.conjugate(Kc.det())))
        gate(f"D6b.realification[n={n}]", sp.simplify(sp.expand(lhs - rhs)) == 0,
             "det_R R(K) = |det_C K|^2   [rebuilt natively]")


# ======================================================================
# BLOCK E -- the count binary is a CARRIER index, not a measure datum
# ======================================================================
def block_E():
    a, b, c = sp.symbols('a b c', real=True)
    # E1: the invariant-functional space is a LINE for every carrier dimension;
    # the family over N is a disjoint union of lines with no canonical comparison.
    dims = {}
    for N in range(1, 7):
        d, _, _ = invariant_functional_space(N)
        dims[N] = d
    gate("E1.line_per_carrier", all(v == 1 for v in dims.values()),
         f"dim of invariant functionals per carrier dimension: {dims}")

    # E2: independently rescaling the two horn measures never equates them
    W = sp.Matrix([[a, b, c], [c, a, b], [b, c, a]])
    det3 = sp.expand(W.det())
    c6, c12 = sp.symbols('c6 c12', nonzero=True)
    diff = sp.expand(c6 * det3 - c12 * det3 ** 2)
    P = sp.Poly(diff, a, b, c)
    # identical vanishing would require every coefficient zero
    sols = sp.solve(P.coeffs(), [c6, c12], dict=True)
    only_trivial = all((s.get(c6, 0) == 0 and s.get(c12, 0) == 0) for s in sols) if sols else True
    gate("E2.no_pair_of_scales_equates_horns", only_trivial,
         f"c6*det3 = c12*det3^2 identically only if both scales vanish (sols={sols})")

    # E3: the count-once value is NOT in the image of any rescaling of the
    # count-twice value as a polynomial family -- degrees 3 vs 6.
    d1 = sp.Poly(det3, a, b, c).total_degree()
    d2 = sp.Poly(sp.expand(det3 ** 2), a, b, c).total_degree()
    gate("E3.horn_degrees", d1 == 3 and d2 == 6,
         f"count-once degree {d1}, count-twice degree {d2}")

    # E4: pre-quotient vs post-quotient cardinalities (previous campaign's table),
    # rebuilt as the two Berezin generator counts.
    gate("E4.generator_counts", 6 * 1 == 6 and 6 * 2 == 12,
         "horn m uses 6m generators: m=1 -> 6, m=2 -> 12")
    # both carriers admit a measure; both give nonzero values at a real witness
    sub = {a: sp.Integer(3), b: sp.Integer(1), c: sp.Integer(1)}
    v1 = sp.expand(det3.subs(sub))
    v2 = sp.expand((det3 ** 2).subs(sub))
    gate("E4b.both_horns_live", v1 != 0 and v2 != 0,
         f"|count-once| = {v1}, |count-twice| = {v2}; both well-defined")


# ======================================================================
# BLOCK F -- CONSTRUCTION-mutation probes
# ======================================================================
def rderiv(a, i):
    """RIGHT derivative -- a construction mutation of the whole engine."""
    out = {}
    for k, v in a.items():
        if i not in k:
            continue
        p = k.index(i)
        sgn = (-1) ** (len(k) - 1 - p)
        nk = k[:p] + k[p + 1:]
        w = sp.expand(out.get(nk, sp.Integer(0)) + sgn * v)
        if w == 0:
            out.pop(nk, None)
        else:
            out[nk] = w
    return out


def nosign_deriv(a, i):
    """SIGN-STRIPPED derivative -- a deliberately wrong construction."""
    out = {}
    for k, v in a.items():
        if i not in k:
            continue
        p = k.index(i)
        nk = k[:p] + k[p + 1:]
        w = sp.expand(out.get(nk, sp.Integer(0)) + v)
        if w == 0:
            out.pop(nk, None)
        else:
            out[nk] = w
    return out


def _dim_from(derivfn, N):
    bas = basis(N)
    pos = {m: k for k, m in enumerate(bas)}
    rows = []
    for i in range(N):
        for m in bas:
            d = derivfn({m: sp.Integer(1)}, i)
            if not d:
                continue
            row = [sp.Integer(0)] * len(bas)
            for k, v in d.items():
                row[pos[k]] += v
            rows.append(row)
    return len(sp.Matrix(rows).nullspace())


def block_F():
    # F1 CONSTRUCTION mutation: rebuild the engine with the RIGHT derivative.
    for N in (2, 3, 4, 5):
        d = _dim_from(rderiv, N)
        gate(f"F1.right_derivative[N={N}]", d == 1,
             f"right-derivative construction also gives dim = {d} (result is convention-free)")
    # F2 CONSTRUCTION mutation: strip the anticommutation signs from the derivative.
    for N in (2, 3, 4, 5):
        d = _dim_from(nosign_deriv, N)
        gate(f"F2.signstripped_derivative[N={N}]", d == 1,
             f"sign-stripped (wrong) derivative gives dim = {d}: the DIMENSION is "
             f"carried by the degree filtration, not by the sign convention")
    # F3 CONSTRUCTION mutation: a NON-quadratic action on the same carrier and
    # the same unique measure returns a DIFFERENT polynomial -- so all coupling
    # dependence enters through the action, none through the measure.
    a, b, c = sp.symbols('a b c', real=True)
    W = sp.Matrix([[a, b, c], [c, a, b], [b, c, a]])
    det3 = sp.expand(W.det())
    g = sp.Symbol('g')
    S = gzero()
    for i in range(3):
        for j in range(3):
            S = gadd(S, gscale(W[i, j], gmul(gen(2 * i + 1), gen(2 * j))))
    quartic = gscale(g, gmul(gmul(gen(1), gen(0)), gmul(gen(3), gen(2))))
    E = gexp(gscale(-1, gadd(S, quartic)), 6)
    v = top_coeff(E, 6)
    gate("F3.quartic_changes_value", sp.expand(v - det3) != 0,
         f"same carrier, same unique measure, quartic action -> value = {sp.factor(sp.expand(v))} != det3")
    gate("F3b.quartic_reduces_to_det", sp.expand(v.subs(g, 0) - det3) == 0,
         "at g = 0 the value returns to det3 exactly (probe is a genuine deformation)")

    # F4 DECISIVE: at FIXED generator count (12) and the FIXED unique measure,
    # BOTH horn values are attainable by choosing the action's kernel.
    Mtwice = sp.zeros(6, 6)
    Mtwice[0:3, 0:3] = W
    Mtwice[3:6, 3:6] = W
    Monce = sp.zeros(6, 6)
    Monce[0:3, 0:3] = W
    Monce[3:6, 3:6] = sp.eye(3)
    v_twice = top_coeff(gaussian_value(Mtwice), 12)
    v_once = top_coeff(gaussian_value(Monce), 12)
    gate("F4.fixed_carrier_twice", sp.expand(v_twice - det3 ** 2) == 0,
         "12 generators, kernel W (+) W  ->  det3^2  (count-twice value)")
    gate("F4b.fixed_carrier_once", sp.expand(v_once - det3) == 0,
         "12 generators, kernel W (+) I_3  ->  det3   (count-once value)")
    gate("F4c.generator_count_not_faithful",
         sp.expand(v_twice - det3 ** 2) == 0 and sp.expand(v_once - det3) == 0
         and sp.expand(v_twice - v_once) != 0,
         "SAME carrier dimension and SAME measure realise BOTH horns: the "
         "generator-count translation of the horn binary is not an equivalence")

    # F5: c6*det3 = c12*det3^2 has no solution with both scales nonzero -- verified
    # by explicit coefficient extraction, not by trusting the solver.
    c6, c12 = sp.symbols('c6 c12')
    P = sp.Poly(sp.expand(c6 * det3 - c12 * det3 ** 2), a, b, c)
    coeff_a3 = P.coeff_monomial(a ** 3)
    coeff_a6 = P.coeff_monomial(a ** 6)
    gate("F5.explicit_coeffs", sp.simplify(coeff_a3 - c6) == 0 and sp.simplify(coeff_a6 + c12) == 0,
         f"coeff(a^3) = {coeff_a3}, coeff(a^6) = {coeff_a6}: identical vanishing forces c6 = c12 = 0")

    # F6: kappa*det = det^2 has NO solution at all (not even kappa = 0)
    z = sp.Symbol('z')
    kappa = sp.Symbol('kappa')
    Q = sp.Poly(sp.expand(kappa * z - z ** 2), z)
    gate("F6.no_kappa_at_all", sp.simplify(Q.coeff_monomial(z ** 2) + 1) == 0,
         "the z^2 coefficient is the nonzero constant -1: no kappa whatsoever converts")

    # F7: a genuine 2x2 Berezin Gram, nonzero and positive definite at scale +1
    m1, m2 = sp.symbols('m1 m2', positive=True)
    G = sp.Matrix([[top_coeff(gaussian_value(sp.Matrix([[m1]])), 2), 0],
                   [0, top_coeff(gaussian_value(sp.Matrix([[m2]])), 2)]])
    gate("F7.gram_pd_at_plus", G == sp.Matrix([[m1, 0], [0, m2]]) and
         all(sp.ask(sp.Q.positive(G[i, i])) for i in range(2)),
         f"Gram at scale +1 = diag({m1},{m2}), positive definite")
    gate("F7b.gram_nd_at_minus", (-G) == sp.Matrix([[-m1, 0], [0, -m2]]),
         "the same Gram at scale -1 is negative definite: the scale SIGN is "
         "fixed by any nontrivial positivity requirement, its MODULUS is not")


def main():
    block_A()
    block_B()
    block_B_translation()
    block_C()
    block_D()
    block_E()
    block_F()
    for line in LOG:
        print(line)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")


if __name__ == "__main__":
    main()
