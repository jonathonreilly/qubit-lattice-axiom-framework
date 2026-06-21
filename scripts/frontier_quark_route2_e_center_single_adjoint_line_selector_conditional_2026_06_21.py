"""Conditional single-adjoint-line selector for the Route-2 E-center lift.

This runner checks a constructive but conditional Route-2 source/readout
primitive:

    a typed source-domain selector supplies one distinguished adjoint line,
    and the E-center excess reads the normalized complement rank in the
    SU(3) adjoint space.

Because dim(adj SU(3)) = 8, the complement of one typed line has normalized
rank 7/8.  With the Route-2 center denominator 6, this gives
rho_E = 6 * (7/8) = 21/4 and q_E = 15/8.

The runner also checks the firewall: this primitive is not present in the
current source bank.  The status is conditional support only, not current
surface closure.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_SINGLE_ADJOINT_LINE_SELECTOR_CONDITIONAL_SUPPORT_NOTE_2026-06-21.md"
S3_GATE = DOCS / "S3_TIME_PRIMITIVE_CHAIN_NOTE.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
BLINDNESS = DOCS / "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md"
SOURCE_BRIDGE = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
RCONN = DOCS / "RCONN_DERIVED_NOTE.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def e_excess_from_rank(rank: int, dim_adj: int = 8) -> Fraction:
    return Fraction(rank, dim_adj)


def q_e_from_excess(e_excess: Fraction) -> Fraction:
    return Fraction(1, 1) + e_excess


def rho_e_from_excess(e_excess: Fraction, center_denominator: int = 6) -> Fraction:
    return center_denominator * e_excess


def center_te_from_qe(q_e: Fraction) -> Fraction:
    q_t = Fraction(5, 6)
    shell_te = Fraction(-2, 1)
    return shell_te * q_t / q_e


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def main() -> int:
    print("ROUTE-2 E-CENTER SINGLE-ADJOINT-LINE SELECTOR: CONDITIONAL CHECK")
    print("=" * 86)

    for path in (NOTE, S3_GATE, READOUT, NATURALITY, BLINDNESS, SOURCE_BRIDGE, RCONN):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    s3_gate = read(S3_GATE)
    readout = read(READOUT)
    naturality = read(NATURALITY)
    blindness = read(BLINDNESS)
    source_bridge = read(SOURCE_BRIDGE)
    rconn = read(RCONN)

    print("\nA. Exact conditional arithmetic")
    dim_adj = 8
    selected_line_rank = 1
    complement_rank = dim_adj - selected_line_rank
    e_excess = e_excess_from_rank(complement_rank, dim_adj)
    q_e = q_e_from_excess(e_excess)
    rho_e = rho_e_from_excess(e_excess)
    c_te = center_te_from_qe(q_e)

    check("SU(3) adjoint dimension is the exact integer 8", dim_adj == 8)
    check(
        "a one-line complement in the adjoint has normalized rank 7/8",
        e_excess == Fraction(7, 8),
        f"rank={complement_rank}, dim={dim_adj}, e_E={e_excess}",
    )
    check("the Route-2 center denominator turns e_E=7/8 into rho_E=21/4", rho_e == Fraction(21, 4), str(rho_e))
    check("the same excess gives q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("with granted T-side values, q_E=15/8 gives c_TE=-8/9", c_te == Fraction(-8, 9), str(c_te))
    check("the resulting center-ratio magnitude equals F_adj=8/9", -c_te == f_adj(3), f"-c_TE={-c_te}, F_adj={f_adj(3)}")

    print("\nB. Uniqueness among integer-rank adjoint projectors")
    table = []
    hits = []
    for rank in range(dim_adj + 1):
        e = e_excess_from_rank(rank, dim_adj)
        q = q_e_from_excess(e)
        rho = rho_e_from_excess(e)
        c = center_te_from_qe(q)
        row = (rank, e, q, rho, c)
        table.append(row)
        if q == Fraction(15, 8) and rho == Fraction(21, 4) and c == Fraction(-8, 9):
            hits.append(row)
    for rank, e, q, rho, c in table:
        print(f"  rank={rank}: e_E={e}, q_E={q}, rho_E={rho}, c_TE={c}")
    check(
        "rank 7 is the unique integer adjoint-projector rank that gives the Route-2 E target",
        len(hits) == 1 and hits[0][0] == 7,
        f"hits={[row[0] for row in hits]}",
    )

    print("\nC. Falsifiers and same-number traps")
    line_e = e_excess_from_rank(1, dim_adj)
    full_e = e_excess_from_rank(8, dim_adj)
    f_as_excess = f_adj(3)
    check(
        "reading the selected line itself fails the target",
        (q_e_from_excess(line_e), rho_e_from_excess(line_e)) != (Fraction(15, 8), Fraction(21, 4)),
        f"line readout: q_E={q_e_from_excess(line_e)}, rho_E={rho_e_from_excess(line_e)}",
    )
    check(
        "reading the full adjoint also fails the target",
        (q_e_from_excess(full_e), rho_e_from_excess(full_e)) != (Fraction(15, 8), Fraction(21, 4)),
        f"full readout: q_E={q_e_from_excess(full_e)}, rho_E={rho_e_from_excess(full_e)}",
    )
    check(
        "using F_adj=8/9 directly as the E-excess fails the target",
        (q_e_from_excess(f_as_excess), rho_e_from_excess(f_as_excess), center_te_from_qe(q_e_from_excess(f_as_excess)))
        != (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        f"F_adj as excess: q_E={q_e_from_excess(f_as_excess)}, "
        f"rho_E={rho_e_from_excess(f_as_excess)}, c_TE={center_te_from_qe(q_e_from_excess(f_as_excess))}",
    )

    print("\nD. Current-surface firewall")
    check(
        "S3 gate names the same missing E-side entry",
        "beta_E / alpha_E = 21/4" in s3_gate
        and "additional" in s3_gate
        and "E-center endpoint ratio" in s3_gate
        and "source-domain rule" in s3_gate,
    )
    check(
        "readout authority defines q_E through beta_E/alpha_E and the denominator 6",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6" in readout,
    )
    check(
        "naturality boundary says rho_E remains free without E-center/source/readout input",
        "remains a free parameter unless an additional E-center endpoint ratio" in naturality
        and "source-domain" in naturality
        and "readout-map primitive" in naturality,
    )
    check(
        "E-center blindness note says positive repair must see the E-center column",
        "A positive repair\nmust supply a genuine E-center lift" in blindness
        or "A positive repair must supply a genuine E-center lift" in " ".join(blindness.split()),
    )
    check(
        "source-domain bridge note does not contain the single-line complement primitive",
        "single-adjoint-line" not in source_bridge
        and "codimension-one adjoint complement" not in source_bridge,
    )
    check(
        "Rconn authority keeps 8/9 as F_adj support, not as the E-excess",
        "F_adj = 8/9" in rconn and "gamma_E(center)" not in rconn,
    )

    print("\nE. Note/status firewall")
    forbidden = (
        "proposed_" + "retained",
        "proposed_" + "promoted",
        "would become " + "retained",
        "promoted to " + "retained",
        "retained on the actual " + "surface",
        "Nature-grade " + "closure",
    )
    check(
        "note marks actual status as conditional-support",
        "**actual_current_surface_status:** conditional-support" in note,
    )
    check("note marks proposal language as disallowed", "**proposal_allowed:** false" in note)
    check("note names the absent primitive explicitly", "single-adjoint-line source selector" in note)
    check("note avoids retained/proposal overclaim phrases", not any(token in note for token in forbidden))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: conditional-support only.  A typed source-domain primitive that selects one adjoint "
        "line and reads the normalized complement rank would force e_E=7/8, q_E=15/8, "
        "rho_E=21/4, and c_TE=-8/9 exactly; rank 7 is unique among integer adjoint-projector ranks.  "
        "The current source bank does not supply this single-line selector, so the S3/Route-2 endpoint "
        "triple remains open on the actual current surface."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
