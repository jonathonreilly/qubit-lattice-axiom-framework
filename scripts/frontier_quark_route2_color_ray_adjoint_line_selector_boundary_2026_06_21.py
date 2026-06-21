#!/usr/bin/env python3
"""Route-2 color-ray adjoint-line selector boundary.

This runner checks a narrow conditional primitive:

    a supplied physical color ray psi in C^3
        -> H_psi = |psi><psi| - I/3
        -> one adjoint line plus a 7-dimensional complement
        -> E-center excess 7/8
        -> rho_E = 21/4 under the granted T-side Route-2 values.

It also checks the current-source boundary: the present color/source notes do
not admit a physical color orientation/ray as source data. Color orientation is
treated as gauge or predictively vacuous on the current surface, while the
color-singlet/Fierz notes supply 1+8 channel algebra, not a line inside the 8.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def has_all(text: str, phrases: list[str]) -> bool:
    return all(p in text for p in phrases)


def gell_mann_halves() -> list[sp.Matrix]:
    I = sp.I
    zero = sp.Integer(0)
    one = sp.Integer(1)
    sqrt3 = sp.sqrt(3)
    lambdas = [
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
        (one / sqrt3) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
    ]
    return [lam / 2 for lam in lambdas]


def trace_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.H * b))


def adjoint_coordinates(x: sp.Matrix, basis: list[sp.Matrix]) -> sp.Matrix:
    # With Tr(t_a t_b) = delta_ab/2, X = sum_a h_a t_a has
    # h_a = 2 Tr(t_a X).
    return sp.Matrix([sp.simplify(2 * trace_inner(t, x)) for t in basis])


def matrix_rank(mat: sp.Matrix) -> int:
    return int(mat.rank())


def main() -> int:
    print("Route-2 color-ray adjoint-line selector boundary")
    print("=" * 78)

    basis = gell_mann_halves()
    gram = sp.Matrix([[sp.simplify(trace_inner(a, b)) for b in basis] for a in basis])
    expected_gram = sp.eye(8) / 2
    record(
        "Gell-Mann half-generators have Tr(t_a t_b)=delta_ab/2",
        sp.simplify(gram - expected_gram) == sp.zeros(8),
        "standard SU(3) adjoint coordinate normalization",
    )

    psi = sp.Matrix([0, 0, 1])
    p_psi = psi * psi.T
    h_psi = sp.simplify(p_psi - sp.eye(3) / 3)
    coords = adjoint_coordinates(h_psi, basis)
    norm_sq = sp.simplify((coords.T * coords)[0])
    p_line = sp.simplify(coords * coords.T / norm_sq)
    p_comp = sp.eye(8) - p_line

    record(
        "a supplied color ray produces a nonzero traceless adjoint element",
        sp.trace(h_psi) == 0 and sp.simplify(trace_inner(h_psi, h_psi)) == sp.Rational(2, 3),
        f"H_psi=diag(-1/3,-1/3,2/3), Tr(H_psi^2)={sp.simplify(trace_inner(h_psi, h_psi))}",
        status="CONDITIONAL",
    )
    record(
        "the color-ray adjoint line is a rank-one projector in the adjoint coordinate space",
        matrix_rank(p_line) == 1 and sp.simplify(p_line * p_line - p_line) == sp.zeros(8),
        f"rank(P_line)={matrix_rank(p_line)}, trace(P_line)={sp.trace(p_line)}",
        status="CONDITIONAL",
    )
    record(
        "the orthogonal complement has rank 7 and normalized fraction 7/8",
        matrix_rank(p_comp) == 7 and sp.simplify(sp.trace(p_comp) / 8) == sp.Rational(7, 8),
        f"rank(P_comp)={matrix_rank(p_comp)}, trace(P_comp)/8={sp.simplify(sp.trace(p_comp) / 8)}",
        status="CONDITIONAL",
    )

    e_excess = Fraction(7, 8)
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = 1 + e_excess
    rho_e = 6 * e_excess
    c_te = s_te * q_t / q_e
    record(
        "reading the color-ray complement as E-center excess gives the Route-2 endpoint triple",
        q_e == Fraction(15, 8) and rho_e == Fraction(21, 4) and c_te == Fraction(-8, 9),
        f"e_E={e_excess}, q_E={q_e}, rho_E={rho_e}, c_TE={c_te}",
        status="CONDITIONAL",
    )

    theta = sp.pi / 4
    c = sp.sqrt(2) / 2
    s = sp.sqrt(2) / 2
    u = sp.Matrix([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    h_rot = sp.simplify(u * h_psi * u.H)
    coords_rot = adjoint_coordinates(h_rot, basis)
    p_line_rot = sp.simplify(coords_rot * coords_rot.T / sp.simplify((coords_rot.T * coords_rot)[0]))
    line_delta_rank = matrix_rank(sp.simplify(p_line_rot - p_line))
    record(
        "the color-ray adjoint line is gauge-covariant but not gauge-invariant",
        line_delta_rank > 0 and sp.simplify(u.det()) == 1,
        f"SU(3) rotation determinant={sp.simplify(u.det())}, rank(P_rot-P_line)={line_delta_rank}",
        status="FIREWALL",
    )
    record(
        "the selected H_psi line is moved by an adjoint generator",
        sp.simplify(basis[3] * h_psi - h_psi * basis[3]) != sp.zeros(3),
        "commutator [t_4,H_psi] is nonzero, so the line is not fixed by SU(3)",
        status="FIREWALL",
    )

    # General invariant-vector firewall: any traceless 3x3 matrix commuting
    # with all Gell-Mann generators must vanish.
    vars_ = sp.symbols("x0:9")
    x = sp.Matrix(3, 3, vars_)
    equations: list[sp.Expr] = []
    for t in basis:
        comm = sp.simplify(t * x - x * t)
        equations.extend(list(comm))
    equations.append(sp.trace(x))
    coeff_rows = []
    for eq in equations:
        coeff_rows.append([sp.expand(eq).coeff(v) for v in vars_])
    rank = sp.Matrix(coeff_rows).rank()
    null_dim = len(vars_) - rank
    record(
        "no nonzero SU(3)-invariant traceless adjoint vector exists",
        null_dim == 0,
        f"linear system rank={rank}, traceless invariant dimension={null_dim}",
        status="FIREWALL",
    )

    source_domain = read("docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    route2_rconn = read("docs/QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md")
    color_orientation = read("docs/COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md")
    depol_necessary = read("docs/MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md")
    color_singlet = read("docs/CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md")
    fierz = read("docs/EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md")
    z3_bridge = read("docs/Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md")
    readout_assessment = read("docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md")

    record(
        "Route-2 current bank still names the missing typed source-domain bridge",
        has_all(
            source_domain,
            [
                "there is no typed current-bank derivation",
                "gamma_T(center)/gamma_E(center) = -R_conn",
                "beta_E/alpha_E = 21/4",
            ],
        ),
        "source-domain bridge no-go keeps the R_conn -> c_TE edge absent",
        status="TEXT",
    )
    record(
        "June 12 Rconn bridge attempt keeps F_adj untyped as a Route-2 center readout",
        has_all(
            route2_rconn,
            [
                "`F_adj` is not typed as a Route-2",
                "center readout",
                "Route-2 E-center source/readout primitive",
                "up-sector scalar law `beta_E/alpha_E = 21/4`",
            ],
        ),
        "F_adj remains exact support, not a center-ratio selector",
        status="TEXT",
    )
    record(
        "current color-orientation surface rejects a named color direction as physical source data",
        has_all(
            color_orientation,
            [
                "Requiring a particular color orientation",
                "specific point inside an `SU(3)` orbit",
                "not a physical admission",
            ],
        ),
        "a color ray would be exactly such an orientation datum",
        status="TEXT",
    )
    record(
        "color-density centrality forces depolarization, not a color ray",
        has_all(
            depol_necessary,
            [
                "matter color density to be unpolarized",
                "traceless(ρ_color)",
                "ρ_color = I₃ / 3",
            ],
        ),
        "the current centrality route collapses the adjoint mean instead of selecting a line",
        status="TEXT",
    )
    record(
        "color-singlet/Fierz authorities supply 1+8 algebra, not a line inside the adjoint 8",
        has_all(
            color_singlet,
            ["1 ⊕ 8", "8-dimensional complement", "physical SM-color identification remains a"],
        )
        and has_all(
            fierz,
            ["adjoint-channel dimension fraction", "matching rule is **not derived in this note**"],
        ),
        "available color algebra is singlet-vs-adjoint channel support only",
        status="TEXT",
    )
    record(
        "axis/cyclic label geometry remains an open bridge, not a color-ray source",
        has_all(
            z3_bridge,
            [
                "a physical identification of the three color labels with the three",
                "open gate",
                "does not by itself derive a physical bridge",
            ],
        ),
        "shared Z3/axis labels do not supply an SU(3) adjoint line",
        status="TEXT",
    )
    record(
        "readout primitive bridge assessment still leaves unique P_R selection open",
        has_all(
            readout_assessment,
            [
                "selects one unique `P_R`",
                "rho_E = beta_E / alpha_E",
                "not derived here as the physical/canonical",
            ],
        ),
        "the conditional color-ray primitive would be a new selector, not current closure",
        status="TEXT",
    )

    print()
    print("Verdict:")
    print(
        "A physical color ray is a sufficient non-invariant primitive for the "
        "single-adjoint-line/complement mechanism: it yields a rank-1 adjoint "
        "line, complement fraction 7/8, q_E=15/8, rho_E=21/4, and c_TE=-8/9 "
        "under the granted T-side Route-2 values. On the current source surface, "
        "however, such a color ray is not supplied: color orientation is gauge/"
        "predictively vacuous, depolarization routes erase traceless color mean, "
        "and Fierz/singlet authorities provide only 1+8 channel algebra. The "
        "result is conditional support plus a current-bank boundary, not a "
        "retained derivation of the endpoint triple."
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
