#!/usr/bin/env python3
"""Exact checks for the all-time volume-uniform walk-expansion LR note."""

import sympy as sp


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        ok = bool(condition)
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def com(a, b):
    return a * b - b * a


def is_zero(m):
    return sp.simplify(m) == sp.zeros(*m.shape)


def op_norm_sq(m):
    """Largest eigenvalue of m^dagger m, exact."""
    return max((m.H * m).eigenvals())


def lattice_distance(x_set, y_set):
    """Ambient Z^3 set distance, undefined for an empty support."""
    if not x_set or not y_set:
        return None
    return min(
        sum(abs(a - b) for a, b in zip(x, y))
        for x in x_set
        for y in y_set
    )


EDIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def bond_key(p, q):
    return tuple(sorted((p, q)))


def incident_bonds(site):
    out = set()
    for d in EDIRS:
        for sg in (1, -1):
            other = tuple(a + sg * x for a, x in zip(site, d))
            out.add(bond_key(site, other))
    return out


def adjacent_bonds(bond, box=None):
    out = set()
    for site in bond:
        for cand in incident_bonds(site):
            if box is not None and not all(
                -box <= c <= box for pt in cand for c in pt
            ):
                continue
            out.add(cand)
    out.discard(bond)
    return out


def main():
    checks = CheckRunner()

    # Group G1 -- algebraic kernel of the Duhamel step.
    P = sp.MatrixSymbol("P", 2, 2)
    Q = sp.MatrixSymbol("Q", 2, 2)
    Rr = sp.MatrixSymbol("Rr", 2, 2)
    jac = sp.expand(
        com(com(P, Q), Rr) - (com(P, com(Q, Rr)) - com(Q, com(P, Rr)))
    )
    checks.check(
        "G1a Jacobi rearrangement identity (symbolic zero)",
        jac == sp.ZeroMatrix(2, 2),
    )
    M = sp.MatrixSymbol("M", 2, 2)
    Minv = sp.Inverse(M)
    conj_lhs = sp.expand(M * com(P, Q) * Minv)
    conj_rhs = sp.expand(
        com(M * P * Minv, M * Q * Minv)
    )
    conj_diff = sp.expand(conj_lhs - conj_rhs).subs(
        Minv * M, sp.Identity(2)
    ).doit()
    checks.check(
        "G1b conjugation distributes over the commutator (symbolic zero)",
        sp.expand(conj_diff) == sp.ZeroMatrix(2, 2),
    )
    site_a = kron(SZ, I2, I2)
    bond_12_xx = kron(SX, SX, I2)
    bond_23_zz = kron(I2, SZ, SZ)
    bond_23_xx = kron(I2, SX, SX)
    checks.check(
        "G1c boundary reduction: bonds missing the support commute exactly",
        is_zero(com(bond_23_zz, site_a))
        and is_zero(com(bond_23_xx, site_a))
        and not is_zero(com(bond_12_xx, site_a)),
    )
    h_full = bond_12_xx + bond_23_zz
    checks.check(
        "G1d self-term drop: [h, h] = 0 and [H, h_12] = [h_23, h_12]",
        is_zero(com(bond_12_xx, bond_12_xx))
        and is_zero(com(h_full, bond_12_xx) - com(bond_23_zz, bond_12_xx)),
    )

    # Group G2 -- norm-transport lemma.
    V = sp.MatrixSymbol("V", 2, 2)
    W = sp.MatrixSymbol("W", 2, 2)
    Ht = sp.MatrixSymbol("Ht", 2, 2)
    f = sp.MatrixSymbol("f", 2, 2)
    Rm = sp.MatrixSymbol("Rm", 2, 2)
    v_prime = sp.I * Ht * V
    w_prime = -sp.I * W * Ht
    f_prime = sp.I * (Ht * f - f * Ht) + Rm
    checks.check(
        "G2a unitarity preserved: d/dt(WV) = 0 (symbolic zero)",
        sp.expand(w_prime * V + W * v_prime) == sp.ZeroMatrix(2, 2),
    )
    intertwiner = sp.expand(
        w_prime * f * V + W * f_prime * V + W * f * v_prime - W * Rm * V
    )
    checks.check(
        "G2b intertwiner: d/dt(W f V) = W R V (symbolic zero)",
        intertwiner == sp.ZeroMatrix(2, 2),
    )
    t, s = sp.symbols("t s", real=True)
    h_diag = sp.diag(1, 2)

    def u_of(x):
        return sp.diag(sp.exp(sp.I * 1 * x), sp.exp(sp.I * 2 * x))

    def r_of(x):
        return sp.Matrix([[x, 1 + x], [2 * x, 3]])

    g0 = sp.Matrix([[1, 2], [0, 1]])
    integ = sp.Matrix(
        2,
        2,
        lambda i, j: sp.integrate(
            (u_of(-s) * r_of(s) * u_of(s))[i, j], (s, 0, t)
        ),
    )
    g_sol = u_of(t) * (g0 + integ) * u_of(-t)
    voc_lhs = g_sol.applyfunc(lambda e: sp.diff(e, t))
    voc_rhs = sp.I * (h_diag * g_sol - g_sol * h_diag) + r_of(t)
    checks.check(
        "G2c variation-of-constants identity (exact rational-spectrum instance)",
        (voc_lhs - voc_rhs).applyfunc(
            lambda e: sp.simplify(sp.expand(e))
        )
        == sp.zeros(2, 2),
    )
    u_orth = sp.Rational(1, 5) * sp.Matrix([[3, 4], [-4, 3]])
    m_inst = sp.Matrix([[1, 2], [0, -1]])
    ev_conj = sorted(
        (( (u_orth * m_inst * u_orth.T).T
           * (u_orth * m_inst * u_orth.T)).eigenvals()).items(),
        key=lambda kv: sp.default_sort_key(kv[0]),
    )
    ev_raw = sorted(
        ((m_inst.T * m_inst).eigenvals()).items(),
        key=lambda kv: sp.default_sort_key(kv[0]),
    )
    checks.check(
        "G2d unitary invariance of the norm (spectrum of M^T M preserved)",
        [
            (sp.simplify(a[0] - b[0]) == 0 and a[1] == b[1])
            for a, b in zip(ev_conj, ev_raw)
        ]
        == [True, True],
    )
    m1 = sp.Matrix([[1, 0], [0, 0]])
    m2 = sp.Matrix([[-1, 0], [0, 0]])
    m3 = sp.Matrix([[0, 0], [0, 1]])
    lhs_tri = sp.sqrt(op_norm_sq(m1 + m2 + m3))
    rhs_tri = sum(sp.sqrt(op_norm_sq(m)) for m in (m1, m2, m3))
    checks.check(
        "G2e finite-sum triangle inequality (exact, strict witness 1 < 3)",
        sp.simplify(lhs_tri) == 1 and sp.simplify(rhs_tri) == 3,
    )
    u_minus_h = sp.diag(sp.exp(-sp.I * 1 * t), sp.exp(-sp.I * 2 * t))
    checks.check(
        "G2f negative time via H -> -H: tau_{-t}^{H} = tau_{t}^{-H} exactly",
        sp.simplify(u_of(-t) - u_minus_h) == sp.zeros(2, 2)
        and sp.simplify(
            u_of(-t) * g0 * u_of(t) - u_minus_h * g0 * u_minus_h.H
        ).applyfunc(sp.simplify)
        == sp.zeros(2, 2),
    )

    # Group G3 -- one-step Duhamel inequality, stationary-bond instance.
    theta = sp.symbols("theta", real=True)
    x1x2 = kron(SX, SX)
    z1 = kron(SZ, I2)
    z2 = kron(I2, SZ)
    y1x2 = kron(SY, SX)
    u_theta = sp.cos(theta) * sp.eye(4) + sp.I * sp.sin(theta) * x1x2
    conj_closed = (
        u_theta * z1 * u_theta.H
        - (sp.cos(2 * theta) * z1 + sp.sin(2 * theta) * y1x2)
    ).applyfunc(lambda e: sp.simplify(sp.expand_trig(sp.expand(e))))
    checks.check(
        "G3a stationary bond and conjugation closed form",
        is_zero(com(x1x2, x1x2))
        and conj_closed == sp.zeros(4, 4),
    )
    lhs_comm = com(
        sp.cos(2 * theta) * z1 + sp.sin(2 * theta) * y1x2, z2
    ).applyfunc(sp.simplify)
    target_comm = (-2 * sp.I * sp.sin(2 * theta) * kron(SY, SY)).applyfunc(
        sp.simplify
    )
    j_pos = sp.Symbol("J", positive=True)
    checks.check(
        "G3b instance closed forms: LHS = -2i sin(2theta) Y1Y2, RHS rate 4J",
        (lhs_comm - target_comm).applyfunc(
            lambda e: sp.simplify(sp.expand_trig(sp.expand(e)))
        )
        == sp.zeros(4, 4)
        and op_norm_sq(com(x1x2, z2)) == 4
        and sp.simplify(
            2 * 1 * sp.integrate(2 * j_pos, (s, 0, t)) - 4 * j_pos * t
        )
        == 0,
    )
    sin_ok = all(
        sp.simplify(val - sp.sin(val)).is_positive is True
        for val in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(3))
    )
    checks.check(
        "G3c |sin x| <= x at exact instances x = 1/2, 1, 3",
        sin_ok,
    )
    norm_sq_theta = op_norm_sq(
        com(sp.cos(2 * theta) * z1 + sp.sin(2 * theta) * y1x2, z2)
    )
    checks.check(
        "G3d instance norm is even in t: ||.||^2 = 4 sin^2(2theta)",
        sp.simplify(sp.expand_trig(norm_sq_theta - 4 * sp.sin(2 * theta) ** 2))
        == 0
        and sp.simplify(sp.sin(-2 * theta) + sp.sin(2 * theta)) == 0
        and sp.simplify(
            sp.expand_trig(
                norm_sq_theta.subs(theta, -theta) - norm_sq_theta
            )
        )
        == 0,
    )

    # Group G4 -- iteration into walks.
    s1, s2 = sp.symbols("s1 s2", positive=True)
    iterated = sp.integrate(
        sp.integrate(sp.integrate(1, (s, 0, s2)), (s2, 0, s1)), (s1, 0, t)
    )
    checks.check(
        "G4a iterated integral gives t^3/3! exactly",
        sp.simplify(iterated - t**3 / 6) == 0,
    )
    a_n, b_n, j_s, t_s, w1, w2 = sp.symbols(
        "a_n b_n j_s t_s w1 w2", positive=True
    )
    depth2_unrolled = (
        2 * a_n * (2 * j_s * b_n) * (w1 * t_s + w2 * (2 * j_s) * t_s**2 / 2)
    )
    depth2_claimed = 2 * a_n * sum(
        (2 * j_s) ** (k - 1) * w * (2 * j_s * b_n) * t_s**k / sp.factorial(k)
        for k, w in ((1, w1), (2, w2))
    )
    checks.check(
        "G4b depth-2 assembly identity (symbolic zero)",
        sp.simplify(depth2_unrolled - depth2_claimed) == 0,
    )
    q_sym = sp.Symbol("q_sym", positive=True)
    ratio_gap = sp.simplify(
        1 - (20 * j_s * t_s) / (20 * j_s * t_s + q_sym)
    )
    checks.check(
        "G4c remainder ratio < 1 past the threshold (symbolic) and instance",
        sp.simplify(ratio_gap - q_sym / (20 * j_s * t_s + q_sym)) == 0
        and ratio_gap.is_positive is True
        and sp.Rational(20, 42) < 1,
    )

    # Independent three-site check of the per-bond Jacobi flow at t = 0.
    # The mutation adds the forbidden self bond only to the forcing sum;
    # unlike the correctly reduced identity, it disagrees with the direct
    # derivative and is therefore killed.
    direct_bond_flow = sp.I * com(com(h_full, bond_12_xx), site_a)
    reduced_bond_flow = (
        sp.I * com(bond_23_zz, com(bond_12_xx, site_a))
        - sp.I * com(bond_12_xx, com(bond_23_zz, site_a))
    )
    self_bond_mutant = reduced_bond_flow - sp.I * com(
        bond_12_xx, com(bond_12_xx, site_a)
    )
    checks.check(
        "G4d previous-bond Jacobi flow matches the direct derivative exactly",
        is_zero(direct_bond_flow - reduced_bond_flow),
    )
    checks.check(
        "G4e self-bond-forcing mutation is killed on the three-site chain",
        not is_zero(direct_bond_flow - self_bond_mutant),
    )

    # A separate end-to-end coefficient oracle expands ad_H directly rather
    # than using the walk recursion.  The first far-site coefficient vanishes,
    # the second is nonzero, and its norm is below the displayed k=2 walk term.
    probe_x3_g4 = kron(I2, I2, SX)
    ad1_chain = com(h_full, site_a)
    ad2_chain = com(h_full, ad1_chain)
    reach1_chain = com(ad1_chain, probe_x3_g4)
    reach2_chain = com(ad2_chain, probe_x3_g4)
    k2_coefficient_norm = sp.sqrt(op_norm_sq(reach2_chain)) / sp.factorial(2)
    k2_walk_majorant = (
        2 * sp.Integer(1) * sp.Integer(1)
        * sp.Rational(1, 10) * sp.Integer(20) ** 2 / sp.factorial(2)
    )
    checks.check(
        "G4f direct finite-chain expansion first vanishes and second reaches",
        is_zero(reach1_chain) and not is_zero(reach2_chain),
    )
    checks.check(
        "G4g exact k=2 coefficient obeys the headline walk majorant",
        bool(k2_coefficient_norm <= k2_walk_majorant),
    )

    # Group G5 -- exact walk combinatorics on Z^3.
    origin = (0, 0, 0)
    start_bonds = sorted(incident_bonds(origin))
    checks.check(
        "G5a bonds incident to one site = 6 exactly",
        len(start_bonds) == 6,
    )
    central = bond_key(origin, (1, 0, 0))
    deg_5 = len(adjacent_bonds(central, box=5))
    deg_7 = len(adjacent_bonds(central, box=7))
    checks.check(
        "G5b bond-adjacency degree = 10 exactly, box-stable (5 and 7)",
        deg_5 == 10 and deg_7 == 10,
    )
    walks1 = [(b,) for b in start_bonds]
    walks2 = [w + (b,) for w in walks1 for b in adjacent_bonds(w[-1])]
    walks3 = [w + (b,) for w in walks2 for b in adjacent_bonds(w[-1])]
    per_bond_3 = [
        len([w for w in walks3 if w[0] == b0]) for b0 in start_bonds
    ]
    checks.check(
        "G5c walk counts: |W_2| = 60 = 6*10 and 100 = 10^2 for EVERY start bond",
        len(walks2) == 60 and per_bond_3 == [100] * 6,
    )
    y_site = (3, 0, 0)
    touches_y = lambda w: y_site in w[-1]
    checks.check(
        "G5d reach lemma sharp at d = 3: lengths 1,2 never, length 3 yes",
        not any(touches_y(w) for w in walks1)
        and not any(touches_y(w) for w in walks2)
        and any(touches_y(w) for w in walks3),
    )

    def max_site_dist(walks):
        return max(
            max(sum(abs(c) for c in site) for site in w[-1]) for w in walks
        )

    checks.check(
        "G5e walk sites stay within distance k of X (k = 1, 2, 3)",
        max_site_dist(walks1) <= 1
        and max_site_dist(walks2) <= 2
        and max_site_dist(walks3) <= 3,
    )

    # Group G6 -- theorem assembly.
    j_sym, n_sym, k_sym = sp.symbols("j_sym n_sym k_sym", positive=True)
    checks.check(
        "G6a coefficient assembly (2J)^k n 10^(k-1) = (n/10)(20J)^k",
        sp.simplify(
            (2 * j_sym) ** k_sym * n_sym * 10 ** (k_sym - 1)
            - (n_sym / sp.Integer(10)) * (20 * j_sym) ** k_sym
        )
        == 0,
    )
    k_val, d_val = 5, 2
    x_val = sp.Rational(3, 2)
    tail_lhs = sum(
        x_val**k / sp.factorial(k) for k in range(d_val, 40)
    )
    tail_rhs = x_val**d_val / sp.factorial(d_val) * sp.exp(x_val)
    checks.check(
        "G6b tail lemma: binomial >= 1 mechanism and exact partial instance",
        sp.binomial(k_val, d_val) >= 1
        and sp.Rational(sp.factorial(d_val), sp.factorial(k_val))
        <= sp.Rational(1, sp.factorial(k_val - d_val))
        and sp.simplify(tail_rhs - tail_lhs).is_positive is True,
    )
    checks.check(
        "G6c cone-decay ratio 20Jt/(d+1) < 1 (instance J=1, t=1/10, d=2)",
        sp.Rational(2, 3) < 1
        and sp.Rational(20, 10) / (2 + 1) == sp.Rational(2, 3),
    )
    big_cert = (
        sp.Integer(3) ** 200 * sp.Integer(200) ** 800
    ) * sp.Integer(10) ** 40 < sp.factorial(800)
    checks.check(
        "G6d large-d smallness certificate 3^200 200^800/800! < 10^-40",
        bool(big_cert),
    )
    probe_x3 = kron(I2, I2, SX)

    def supports_disjoint(x_set, y_set):
        return len(set(x_set) & set(y_set)) == 0

    checks.check(
        "G6e disjoint supports commute (d >= 1) and the d = 0 rejector trips",
        is_zero(com(site_a, probe_x3))
        and supports_disjoint([origin], [y_site])
        and not supports_disjoint([origin], [origin]),
    )
    checks.check(
        "G6e2 nonempty-support distance is defined; empty support is rejected",
        lattice_distance([origin], [y_site]) == 3
        and lattice_distance([], [y_site]) is None
        and lattice_distance([origin], []) is None,
    )
    a_d0 = SX
    b_d0 = SY
    lhs_d0 = sp.sqrt(op_norm_sq(com(a_d0, b_d0)))
    rhs_d0 = 2 * 1 * 1 * sp.Rational(1, 10) * sum(
        sp.Integer(0) ** k / sp.factorial(k) for k in range(0, 5)
    )
    checks.check(
        "G6e3 d = 0 exclusion is necessary: ||[A,B]|| = 2 > 1/5 = claimed RHS",
        sp.simplify(lhs_d0) == 2
        and rhs_d0 == sp.Rational(1, 5)
        and rhs_d0 < lhs_d0,
    )
    u_disconnected = (
        sp.cos(theta) * sp.eye(8) + sp.I * sp.sin(theta) * bond_12_xx
    )
    evolved_disconnected = (
        u_disconnected * site_a * u_disconnected.H
    ).applyfunc(lambda e: sp.simplify(sp.expand_trig(sp.expand(e))))
    checks.check(
        "G6e4 empty-bond J=0 convention and disconnected evolution are static",
        max([], default=0) == 0
        and is_zero(com(evolved_disconnected, probe_x3)),
    )
    mu_s, x_s, k_pos, j_pos2 = sp.symbols(
        "mu_s x_s k_pos j_pos2", positive=True
    )
    reweight = sp.simplify(
        x_s**k_pos / sp.factorial(k_pos)
        - sp.exp(-mu_s * k_pos)
        * (x_s * sp.exp(mu_s)) ** k_pos
        / sp.factorial(k_pos)
    )
    exponent_gap = sp.simplify(
        mu_s * (k_pos + j_pos2) - mu_s * k_pos - mu_s * j_pos2
    )
    mono_instances = all(
        sp.simplify(sp.exp(-a) - sp.exp(-b)).is_positive is True
        for a, b in ((sp.Integer(1), sp.Integer(2)),
                     (sp.Rational(1, 2), sp.Integer(3)))
    )
    checks.check(
        "G6f mu-reweighting identity (symbolic); drop via exponent "
        "comparison (symbolic) plus exp-monotonicity instances",
        reweight == 0
        and exponent_gap == 0
        and (mu_s * j_pos2).is_positive is True
        and mono_instances,
    )
    mu_val = sp.Integer(1)
    x_mu = sp.Rational(3, 2)
    d_mu = 2
    lhs_mu = sum(x_mu**k / sp.factorial(k) for k in range(d_mu, 40))
    rhs_mu = sp.exp(-mu_val * d_mu + x_mu * sp.exp(mu_val))
    checks.check(
        "G6g mu-bound instance: sum_{k>=2} (3/2)^k/k! < e^{-2 + (3/2)e}",
        sp.simplify(rhs_mu - lhs_mu).is_positive is True
        and sp.simplify(sp.exp(sp.Integer(1)) - 3).is_negative is True,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
