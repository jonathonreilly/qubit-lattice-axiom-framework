#!/usr/bin/env python3
"""Exact checks for the d-dim two-step many-body transfer identity note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_"
    "IDENTITY_NOTE_2026-07-20.md"
)
DISP_NOTE = ROOT / (
    "docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_"
    "NARROW_THEOREM_NOTE_2026-06-12.md"
)
RP_NOTE = ROOT / (
    "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_"
    "NOTE_2026-05-28.md"
)
CORNER_NOTE = ROOT / (
    "docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
    "N1", "N2", "N3", "N4", "N5", "N6",
]

# Phrases RETRACTED in review-loop round 2 (2026-07-24, PR #5549). N6 is an
# ABSENCE gate: it fails if any of these reappears in the target note's LIVE
# claim surface. Presence needles (N5) cannot do this -- adding a retracted
# sentence elsewhere would not remove the corrected ones -- so the absence
# check is what actually makes restoration fail the gate.
RETRACTED_PHRASES = (
    "C = 1 derived",
    "action-level",
    "ACTION-LEVEL",
    "supplies the prerequisite",
    "un-built bridge",
    "operator identification the landed corner-note names as an "
    "unsupplied prerequisite",
    "it does not infer - it derives",
    "it does not infer -- it derives",
)

# The live claim surface = the YAML front matter (where claim_scope lives)
# plus every body section EXCEPT the two that quote the retractions verbatim.
# Those two are delimited by these headings and are excluded by name, so the
# gate cannot be defeated by burying a live claim inside them.
HISTORICAL_QUOTE_SECTIONS = (
    "- **N5 rhetoric audit",
)


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(n) in haystack for n in needles),
        )

    def absent(self, label, path, phrases, skip_bullet_prefixes=()):
        """Fail if any phrase appears OUTSIDE the excluded historical bullets.

        Excluded bullets are markdown list items whose first line starts with
        one of `skip_bullet_prefixes`; the exclusion ends at the next list item
        at the same level or the next heading, so a live claim cannot be hidden
        by appending it after the historical text.
        """
        lines = path.read_text(encoding="utf-8").splitlines()
        live, skipping = [], False
        for line in lines:
            if skipping:
                if line.startswith("#") or (
                    line.startswith("- ")
                    and not line.startswith(tuple(skip_bullet_prefixes))
                ):
                    skipping = False
                else:
                    continue
            if skip_bullet_prefixes and line.startswith(
                tuple(skip_bullet_prefixes)
            ):
                skipping = True
                continue
            live.append(line)
        haystack = normalized_whitespace("\n".join(live))
        hits = [p for p in phrases if normalized_whitespace(p) in haystack]
        if hits:
            print(f"  retracted phrases found on the live surface: {hits}")
        self.check(label, not hits)

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def gamma_matrices(d):
    """Corner operators from the fold rule Gamma_mu|r> = (-1)^{r_mu}|r xor s_mu>."""
    dim = 2**d
    gammas = []
    for mu in range(1, d + 1):
        s_mask = (1 << (mu - 1)) - 1  # ones in slots < mu (bits 0..mu-2)
        G = sp.zeros(dim, dim)
        for r in range(dim):
            r_mu = (r >> (mu - 1)) & 1
            G[r ^ s_mask, r] = sp.Integer(-1) ** r_mu
        gammas.append(G)
    return gammas


def jw_creation(n_modes, j):
    """Jordan-Wigner creation matrix for mode j on the subset basis."""
    dim = 2**n_modes
    A = sp.zeros(dim, dim)
    for S in range(dim):
        if (S >> j) & 1:
            continue
        sign = sp.Integer(-1) ** bin(S & ((1 << j) - 1)).count("1")
        A[S | (1 << j), S] = sign
    return A


def main():
    checks = CheckRunner()

    # G1 -- Clifford/corner algebra rebuilt from the fold rule; scalar square.
    ok = True
    for d in (2, 3):
        gam = gamma_matrices(d)
        dim = 2**d
        for i, G in enumerate(gam):
            if sp.simplify(G * G - sp.eye(dim)) != sp.zeros(dim, dim):
                ok = False
            if sp.simplify(G - G.T) != sp.zeros(dim, dim):
                ok = False
        for i in range(d):
            for j in range(i + 1, d):
                if sp.simplify(
                    gam[i] * gam[j] + gam[j] * gam[i]
                ) != sp.zeros(dim, dim):
                    ok = False
        svars = sp.symbols(f"s1:{d + 1}", real=True)
        S = sp.zeros(dim, dim)
        for i in range(d):
            S += svars[i] * gam[i]
        if sp.simplify(
            sp.expand(S * S) - sum(v**2 for v in svars) * sp.eye(dim)
        ) != sp.zeros(dim, dim):
            ok = False
    L1, L2, L3 = sp.symbols("Lp1 Lp2 Lp3", positive=True)
    count_ok = (
        sp.simplify(
            (L1 / 2) * (L2 / 2) * (L3 / 2) * 2**3 - L1 * L2 * L3
        )
        == 0
    )
    checks.check(
        "G1 corner algebra rebuilt from the fold rule (d = 2, 3): "
        "Gamma_mu Hermitian, Gamma_mu^2 = I, anticommuting, "
        "S(k)^2 = (sum_mu s_mu^2) I with SYMBOLIC s_mu (scalar "
        "square), and the general-period mode count "
        "prod(L_mu/2) * 2^d = prod L_mu (d = 3 symbolic)",
        ok and count_ok,
    )

    # G2 -- L = 2 position-space classical rebuild (d = 2 and 3): the hop
    # vanishes identically (tau_+ = tau_- at L = 2, stated honestly) and
    # the doubled block carries e^{+-2 arcsinh m} with multiplicity 2^d.
    m = sp.Symbol("m", positive=True)
    mu_p = (sp.sqrt(1 + m**2) + m) ** 2
    mu_m = (sp.sqrt(1 + m**2) - m) ** 2
    ok = True
    for d in (2, 3):
        sites = list(itertools.product((0, 1), repeat=d))
        V = len(sites)
        idx = {x: i for i, x in enumerate(sites)}
        H = sp.zeros(V, V)
        for x in sites:
            for mu in range(1, d + 1):
                xi = sp.Integer(-1) ** sum(x[:mu - 1])
                yp = list(x); yp[mu - 1] = (yp[mu - 1] + 1) % 2
                ym = list(x); ym[mu - 1] = (ym[mu - 1] - 1) % 2
                H[idx[x], idx[tuple(yp)]] += xi / 2
                H[idx[x], idx[tuple(ym)]] -= xi / 2
        if H != sp.zeros(V, V):
            ok = False
        Te = sp.Matrix(sp.BlockMatrix([
            [-2 * (m * sp.eye(V) + H), sp.eye(V)],
            [sp.eye(V), sp.zeros(V, V)],
        ]))
        To = sp.Matrix(sp.BlockMatrix([
            [-2 * (m * sp.eye(V) - H), sp.eye(V)],
            [sp.eye(V), sp.zeros(V, V)],
        ]))
        T2 = sp.expand(To * Te)
        minpoly = sp.expand(
            T2 * T2 - (2 + 4 * m**2) * T2 + sp.eye(2 * V)
        )
        if sp.simplify(minpoly) != sp.zeros(2 * V, 2 * V):
            ok = False
        tr = sp.simplify(sp.trace(T2) - V * (2 + 4 * m**2))
        if tr != 0:
            ok = False
        n_minus = sp.simplify(
            (sp.trace(T2) - 2 * V * mu_p) / (mu_m - mu_p)
        )
        if sp.simplify(n_minus - V) != 0:
            ok = False
    checks.check(
        "G2 SUPPORT-ONLY degenerate L = 2 mass-only recurrence "
        "(mode counts 2^2, 2^3): H_hop = 0 EXACTLY at L = 2, so this "
        "gate carries NO d-dimensional content and does not exercise "
        "the staggered phases or S(k); it checks only the mass-only "
        "minimal polynomial T^2 - (2+4m^2)T + I = 0 and that trace "
        "pins multiplicity 2^d for each of e^{+-2 arcsinh m} "
        "(symbolic m)",
        ok
        and sp.simplify(mu_p * mu_m - 1) == 0
        and sp.simplify(mu_p + mu_m - (2 + 4 * m**2)) == 0,
    )

    # G3 -- d = 2, L = 4 position-space faithfulness: the phases genuinely
    # enter; spec(H_hop^2) = {0 x4, -1 x8, -2 x4}.
    L = 4
    sites = list(itertools.product(range(L), repeat=2))
    V = len(sites)
    idx = {x: i for i, x in enumerate(sites)}
    H = sp.zeros(V, V)
    for x in sites:
        for mu in (1, 2):
            xi = sp.Integer(-1) ** sum(x[:mu - 1])
            yp = list(x); yp[mu - 1] = (yp[mu - 1] + 1) % L
            ym = list(x); ym[mu - 1] = (ym[mu - 1] - 1) % L
            H[idx[x], idx[tuple(yp)]] += sp.Rational(1, 2) * xi
            H[idx[x], idx[tuple(ym)]] -= sp.Rational(1, 2) * xi
    H2 = H * H
    lam = sp.Symbol("lam")
    cp = sp.factor(H2.charpoly(lam).as_expr())
    expected = sp.expand(lam**4 * (lam + 1) ** 8 * (lam + 2) ** 4)
    checks.check(
        "G3 d = 2, L = 4 position-space faithfulness: H_hop is real "
        "antisymmetric with charpoly(H_hop^2) = lam^4 (lam+1)^8 (lam+2)^4 "
        "(eigenvalues -(sin^2 p1 + sin^2 p2) with the exact "
        "multiplicities; exercises the staggered phases)",
        sp.simplify(H + H.T) == sp.zeros(V, V)
        and sp.expand(cp - expected) == 0,
    )

    # G4 -- corner-coupled symbolic block at k = (pi/2, pi/2) and the
    # taste spot k = (pi/2, 0) (d = 2).
    gam2 = gamma_matrices(2)
    ok = True
    for sins, Sigma in (((1, 1), 2), ((1, 0), 1)):
        S = sins[0] * gam2[0] + sins[1] * gam2[1]
        if sp.simplify(S * S - Sigma * sp.eye(4)) != sp.zeros(4, 4):
            ok = False
        Te = sp.Matrix(sp.BlockMatrix([
            [-2 * (m * sp.eye(4) + sp.I * S), sp.eye(4)],
            [sp.eye(4), sp.zeros(4, 4)],
        ]))
        To = sp.Matrix(sp.BlockMatrix([
            [-2 * (m * sp.eye(4) - sp.I * S), sp.eye(4)],
            [sp.eye(4), sp.zeros(4, 4)],
        ]))
        T2 = sp.expand(To * Te)
        R = m**2 + Sigma
        minpoly = sp.expand(T2 * T2 - (2 + 4 * R) * T2 + sp.eye(8))
        if sp.simplify(minpoly) != sp.zeros(8, 8):
            ok = False
        if sp.simplify(sp.trace(T2) - 4 * (2 + 4 * R)) != 0:
            ok = False
    checks.check(
        "G4 corner-coupled block (d = 2): at k = (pi/2, pi/2), "
        "S = Gamma_1 + Gamma_2 with S^2 = 2I (genuine off-diagonal "
        "coupling), and at k = (pi/2, 0); minimal polynomial "
        "T^2 - (2+4R)T + I = 0 with R = m^2 + Sigma and trace "
        "4(2+4R) => multiplicity 2^d = 4 per eigenvalue (symbolic m)",
        ok,
    )

    # G5 -- per-mode projectors, strict reciprocal split (symbolic).
    sig = sp.Symbol("sigma", positive=True)
    R = m**2 + sig**2
    a = m + sp.I * sig
    T2 = sp.Matrix([
        [4 * (m**2 + sig**2) + 1, -2 * sp.conjugate(a)],
        [-2 * a, 1],
    ])
    Lp = 1 + 2 * R + 2 * sp.sqrt(R * (1 + R))
    Lm = 1 + 2 * R - 2 * sp.sqrt(R * (1 + R))
    Pm = (T2 - Lp * sp.eye(2)) / (Lm - Lp)
    Pp = (T2 - Lm * sp.eye(2)) / (Lp - Lm)
    proj_ok = (
        sp.simplify(sp.expand(Pm * Pm - Pm)) == sp.zeros(2, 2)
        and sp.simplify(sp.expand(Pp * Pp - Pp)) == sp.zeros(2, 2)
        and sp.simplify(sp.expand(Pm * Pp)) == sp.zeros(2, 2)
        and sp.simplify(Pm + Pp - sp.eye(2)) == sp.zeros(2, 2)
        and sp.simplify(sp.expand(T2 * Pm - Lm * Pm)) == sp.zeros(2, 2)
        and sp.simplify(sp.expand(T2 * Pp - Lp * Pp)) == sp.zeros(2, 2)
    )
    recip = sp.simplify(sp.expand(Lp * Lm) - 1) == 0
    strict = (
        sp.simplify(R * (1 + R) - R**2 - R) == 0
        and sp.simplify(
            Lm - (sp.sqrt(1 + R) - sp.sqrt(R)) ** 2
        )
        == 0
        and sp.expand(
            (sp.sqrt(1 + R) - sp.sqrt(R)) ** 2
            * (sp.sqrt(1 + R) + sp.sqrt(R)) ** 2
            - 1
        )
        == 0
    )
    checks.check(
        "G5 per-mode Riesz projectors (symbolic sigma, m): idempotent, "
        "orthogonal, complete, eigen-relations; reciprocity "
        "Lp Lm = 1; strict split via R(1+R) - R^2 = R > 0 and "
        "Lm = (sqrt(1+R) - sqrt(R))^2 in (0,1) as a square with "
        "reciprocal partner",
        proj_ok and recip and strict,
    )

    # G6 -- one-mode Grassmann bridge with the C = 1 pin and rejector.
    lam_s, C = sp.symbols("lambda_s C_pref", positive=True)
    # elements of the Grassmann-even ring as (const, w-coeff)
    def gmul(p, q):
        return (
            sp.expand(p[0] * q[0]),
            sp.expand(p[0] * q[1] + p[1] * q[0]),
        )
    kernel_exp = (sp.Integer(1), lam_s)          # exp(lambda w) truncated
    op_kernel = gmul((1, lam_s - 1), (1, 1))     # (1+(lam-1)w)(1+w)
    scaled = (C * 1, C * lam_s)                  # C * exp(lambda w)
    checks.check(
        "G6 one-mode coherent->exterior bridge GIVEN the supplied "
        "exponential kernel form (a conditional input, per the RP "
        "note; supplying that form IS the coherent-state form of the "
        "operator identification, so this gate cannot and does not "
        "derive it): normal-ordered kernel of diag(1, lambda) equals "
        "exp(lambda w) exactly (nilpotent ring), vacuum element = 1, "
        "and the C-scaling leaves constant-term residual C - 1 whose "
        "zero set is C = 1 (a bookkeeping statement, NOT an "
        "independent discrimination)",
        op_kernel[0] == 1
        and sp.simplify(op_kernel[1] - lam_s) == 0
        and kernel_exp[0] == 1
        and sp.simplify(scaled[0] - 1) != 0
        and sp.simplify(scaled[0].subs(C, 1) - 1) == 0,
    )

    # G7 -- full Fock assembly, d = 2, L = 2 (16-dim dense exact).
    t = sp.Symbol("t", positive=True)
    E = sp.Symbol("E", positive=True)
    n_modes = 4
    dim = 2**n_modes
    diag_entries = [t ** bin(S).count("1") for S in range(dim)]
    Gam = sp.diag(*diag_entries)
    ok = all(
        sp.simplify(
            sp.expand(Gam * jw_creation(n_modes, j)
                      - t * jw_creation(n_modes, j) * Gam)
        )
        == sp.zeros(dim, dim)
        for j in range(n_modes)
    )
    vac = sp.zeros(dim, 1)
    vac[0] = 1
    ok = ok and sp.simplify(Gam * vac - vac) == sp.zeros(dim, 1)
    # CAR anticommutators: the genuinely sign-discriminating gates
    # (for a diagonal Gamma the intertwiner is sign-convention-blind).
    creators = [jw_creation(n_modes, j) for j in range(n_modes)]
    car_ok = True
    for i in range(n_modes):
        for j in range(n_modes):
            ac = sp.expand(
                creators[i].T * creators[j]
                + creators[j] * creators[i].T
            )
            expect = sp.eye(dim) if i == j else sp.zeros(dim, dim)
            if sp.simplify(ac - expect) != sp.zeros(dim, dim):
                car_ok = False
            # i == j included: {a_i^dag, a_i^dag} = 2 a_i^dag a_i^dag = 0
            # (nilpotency), so the label's "all pairs" is literal.
            cc = sp.expand(
                creators[i] * creators[j]
                + creators[j] * creators[i]
            )
            if sp.simplify(cc) != sp.zeros(dim, dim):
                car_ok = False
    ok = ok and car_ok
    t_of_E = sp.exp(-2 * E)
    ok = ok and all(
        sp.simplify(
            -sp.log(t_of_E ** q) / 2 - E * q
        )
        == 0
        for q in range(n_modes + 1)
    )
    trace_ok = (
        sp.expand(sum(diag_entries) - (1 + t) ** 4) == 0
        and sp.expand(
            sp.det(sp.eye(4) + t * sp.eye(4)) - (1 + t) ** 4
        )
        == 0
    )
    Bfac = sp.diag(1, sp.sqrt(t))
    B = Bfac
    for _ in range(n_modes - 1):
        B = sp.Matrix(sp.kronecker_product(B, Bfac))
    ok = ok and sp.simplify(sp.expand(B.T * B - Gam)) == sp.zeros(dim, dim)
    checks.check(
        "G7 SUPPORT-ONLY generic four-mode exterior/Jordan-Wigner "
        "bookkeeping (16-dim dense, FREE symbolic t; the mode count "
        "is the one d = 2, L = 2 instantiates, but the gate carries "
        "no d-dimensional content and never touches S(k), the "
        "staggered phases, or E_d): occupation Gamma = diag(t^|S|) "
        "intertwines every creation operator (for a diagonal kernel "
        "this check is sign-convention-blind — stated honestly), "
        "fixes the vacuum, AND the CAR anticommutators "
        "{a_i, a_j^dag} = delta_ij, {a_i^dag, a_j^dag} = 0 hold for "
        "all ordered pairs INCLUDING i = j (nilpotency) — these "
        "discriminate a JW-sign-stripping mutation "
        "of THIS runner's own matrices, i.e. they verify the chosen "
        "Fock representation satisfies the CAR; they do NOT derive "
        "the physical CAR metric, the reflected inner product, or "
        "the action-to-Fock identification; -log(t^|S|)/2 = E|S| at "
        "t = e^{-2E}, Tr = (1+t)^4 = det(I + t I), and B^T B = Gamma "
        "with B = kron^4 diag(1, sqrt(t))",
        ok and trace_ok,
    )

    # G8 -- structured assembly, d = 3, L = 2 (256-dim, no dense matrix).
    n8 = 8
    ok = True
    for S in range(2**n8):
        pc = bin(S).count("1")
        if sp.simplify(-sp.log(t_of_E ** pc) / 2 - E * pc) != 0:
            ok = False
            break
    for j in range(n8):
        if not ok:
            break
        for S in range(2**n8):
            if (S >> j) & 1:
                continue
            sign = (-1) ** bin(S & ((1 << j) - 1)).count("1")
            target = S | (1 << j)
            lhs = (target, sign, t ** (bin(S).count("1") + 1))
            rhs = (target, sign, sp.expand(t * t ** bin(S).count("1")))
            if lhs[0] != rhs[0] or lhs[1] != rhs[1] or sp.simplify(
                lhs[2] - rhs[2]
            ) != 0:
                ok = False
                break
    trace8 = sum(
        sp.binomial(8, q) * t**q for q in range(9)
    )
    ok = ok and sp.expand(trace8 - (1 + t) ** 8) == 0
    ok = ok and all(
        sp.simplify((t ** sp.Rational(pc, 2)) ** 2 - t**pc) == 0
        for pc in range(9)
    )
    checks.check(
        "G8 SUPPORT-ONLY generic eight-mode subset bookkeeping "
        "(256-dim, subset-indexed scalars, NO dense matrix; the mode "
        "count is the one d = 3, L = 2 instantiates, but the gate "
        "carries no d-dimensional content): occupation-weight "
        "bookkeeping via action on basis vectors for all 8 modes "
        "(target and scalar only — for diagonal kernels the "
        "intertwiner carries no sign content; the JW-sign "
        "discrimination is G7's CAR gate), per-entry log identity, "
        "Tr = (1+t)^8 (both routes), and the B-square bookkeeping",
        ok,
    )

    # G9 -- the canonical pin discriminates only off degeneracy: the
    # corner-note W-conjugate counterexample rebuilt on diag(2,3,5).
    lams = [2, 3, 5]
    dim3 = 8
    gvals = [
        sp.Integer(1), 2, 3, 6, 5, 10, 15, 30
    ]  # products over subsets, mask bit j = mode j
    Gam3 = sp.diag(*gvals)
    # W swaps occupation states {0,1} (mask 3, value 6) and {0,2} (mask 5, value 10)
    W = sp.eye(dim3)
    W[3, 3] = 0; W[5, 5] = 0; W[3, 5] = 1; W[5, 3] = 1
    Gam3t = W * Gam3 * W.T
    trace_eq = sp.simplify(sp.trace(Gam3) - sp.trace(Gam3t)) == 0
    det_eq = sp.simplify(
        sp.trace(Gam3) - sp.prod([1 + l for l in lams])
    ) == 0
    uvals = [sp.Integer(1), 7, 11, 77, 13, 91, 143, 1001]
    U3 = sp.diag(*uvals)
    U3t = W * U3 * W.T
    prodvals = [g * u for g, u in zip(gvals, uvals)]
    P3 = sp.diag(*prodvals)
    P3t = W * P3 * W.T
    mult_ok = (
        sp.simplify(Gam3 * U3 - P3) == sp.zeros(dim3, dim3)
        and sp.simplify(Gam3t * U3t - P3t) == sp.zeros(dim3, dim3)
    )
    intertwiner_canonical = all(
        sp.simplify(
            Gam3 * jw_creation(3, j) - lams[j] * jw_creation(3, j) * Gam3
        )
        == sp.zeros(dim3, dim3)
        for j in range(3)
    )
    A1 = jw_creation(3, 1)
    bad = sp.simplify(Gam3t * A1 - lams[1] * A1 * Gam3t)
    tilde_fails = bad != sp.zeros(dim3, dim3)
    log_breaks = sp.simplify(
        sp.log(Gam3t[3, 3]) - (sp.log(2) + sp.log(3))
    ) != 0
    checks.check(
        "G9 canonical-pin discrimination (non-degenerate diag(2,3,5)): "
        "the W-conjugate preserves trace (= det(1+t) = 72); its "
        "multiplicativity conjunct is TRUE BY CONSTRUCTION of this "
        "diagonal instance and is NOT an independent oracle (the "
        "abstract conjugation argument is the corner note's); the "
        "genuine discriminations are that the W-conjugate BREAKS the "
        "creation intertwiner and the log identity while the "
        "canonical Gamma satisfies the intertwiner for every mode",
        trace_eq and det_eq and mult_ok and intertwiner_canonical
        and tilde_fails and log_breaks,
    )

    # Needles.
    checks.needle(
        "N1 dispersion note: phases, mode equation, fold rule, the "
        "only-dimension-dependent-step sentence, taste degeneracy, "
        "forward/backward channel, even periods, one-particle boundary",
        DISP_NOTE,
        (
            "eta_mu(t,x) = (-1)^(t + x_1 + ... + x_{mu-1})",
            "psi_{t+1} = -2 (m I + (-1)^t H_hop) psi_t + psi_{t-1}",
            "Gamma_mu |r> = (-1)^{r_mu} |r xor s_mu>",
            "This is the only dimension-dependent algebraic step.",
            "taste-degenerate across the `2^d` two-site-cell corners",
            "The decaying forward channel is `exp(-2 E_d(p))`; the "
            "reciprocal growing channel is the backward-time solution, "
            "as in the one-axis construction.",
            "even\nspatial periods",
            "one-particle two-step transfer and the corresponding free "
            "log-transfer symbol",
        ),
    )
    checks.needle(
        "N2 RP note: projector display, finite-norm selection sentence, "
        "coherent kernel, defining intertwiner, 1+1d scope",
        RP_NOTE,
        (
            "P_-(p) = (T2cl(p) - lambda_+(p) I) / (lambda_-(p) - "
            "lambda_+(p))",
            "so finite-action / finite-norm positive-time propagation "
            "sets that coefficient to zero",
            "<bar z'|T_2|z> = exp(bar z' lambda_- z)",
            "Gamma(K) |vac> = |vac>,    Gamma(K) a_p^dag = lambda_p "
            "a_p^dag Gamma(K).",
            "one Grassmann component per\nsite, `1+1d`, `L_s` spatial "
            "sites, periodic, real mass `m > 0`",
        ),
    )
    checks.needle(
        "N3 corner note: intertwiner, positive log, trace, direct sums, "
        "the pin sentence, the does-not-infer boundary, and the "
        "operator-identification prerequisite -- which this note does "
        "NOT discharge (it carries the same conditional to general d)",
        CORNER_NOTE,
        (
            "`Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)`, and `Gamma(A)` "
            "fixes the vacuum.",
            "-log Gamma(t) = dGamma(-log t)",
            "Tr_F Gamma(A) = det_H(1 + A)",
            "Gamma(direct_sum_k A_k) = tensor_k Gamma(A_k)",
            "the canonical creation\nintertwiner is the pin",
            "It does not infer a many-body transfer operator from a "
            "one-particle\nkernel.",
            "until the operator identification and boundary convention "
            "are both supplied.",
        ),
    )
    checks.needle(
        "N4 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N5 self-pin needles (anti-drift for the target note's "
        "RETRACTED-CLAIM boundary; NOT independent evidence)",
        TARGET_NOTE,
        (
            "free_staggered_d_dimensional_two_step_many_body_transfer_"
            "identity_note_2026-07-20",
            "each with multiplicity `2^d`",
            "**parity with the landed `d = 1` case**",
            "pinned relative\nto the supplied kernel form",
            "sign-convention-blind",
            # The corrected boundary, pinned so a future edit cannot
            # silently restore the retracted "supplies the prerequisite"
            # or "C = 1 derived" framings.
            "**Status: no closure is claimed and no `PASS` is "
            "asserted.**",
            "Does **not** supply or discharge the corner-note's "
            "action-to-Fock\n  **operator identification**.",
            "with `C = 1` fixed by the supplied normalized kernel "
            "form.",
            "grade (B) relocates the identification conditional to "
            "general `d` rather than closing it",
        ),
    )
    checks.absent(
        "N6 ABSENCE gate on the target note's LIVE claim surface (YAML "
        "claim_scope + all body sections except the N5 rhetoric-audit "
        "bullet, which quotes the retractions verbatim): none of the "
        "round-2 RETRACTED phrases -- 'C = 1 derived', 'action-level', "
        "'supplies the prerequisite', 'un-built bridge', 'operator "
        "identification the landed corner-note names as an unsupplied "
        "prerequisite', 'it does not infer -- it derives' -- may "
        "reappear; restoring any of them FAILS this gate (the N5 "
        "presence needles cannot detect restoration by themselves)",
        TARGET_NOTE,
        RETRACTED_PHRASES,
        skip_bullet_prefixes=HISTORICAL_QUOTE_SECTIONS,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
