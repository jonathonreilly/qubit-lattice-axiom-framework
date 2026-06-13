#!/usr/bin/env python3
"""Exact W80 checker for the Route-2 c_TE magnitude structural-status probe.

No randomness, no live comparator values, no external citations, and no floating
arithmetic are used.  The runner checks only exact rational consequences of the
repo-internal W67/W77/Rconn authority bank and source-note hygiene.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "QUARK_ROUTE2_CTE_MAGNITUDE_STRUCTURAL_STATUS_BOUNDED_NOTE_2026-06-12.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" -- {detail}" if detail else ""))


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_from_rho(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def c_te(q_e: Fraction) -> Fraction:
    return -Fraction(5, 3) / q_e


def q_for_magnitude_identity(n_c: int) -> Fraction:
    return Fraction(5, 3) / f_adj(n_c)


def rho_for_magnitude_identity(n_c: int) -> Fraction:
    return 6 * (q_for_magnitude_identity(n_c) - 1)


def c_f(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, 2 * n_c)


def c_f_squared_t_f(n_c: int) -> Fraction:
    return c_f(n_c) * c_f(n_c) * Fraction(1, 2)


def r_phys(n_c: int, kappa_ew: Fraction) -> Fraction:
    f = f_adj(n_c)
    return f + kappa_ew * (1 - f)


def run_exact_endpoint_checks() -> None:
    rho_target = Fraction(21, 4)
    q_target = q_from_rho(rho_target)
    c_target = c_te(q_target)

    check("target rho_E gives q_E=15/8", q_target == Fraction(15, 8), f"q_E={q_target}")
    check("target q_E gives c_TE=-8/9", c_target == -Fraction(8, 9), f"c_TE={c_target}")
    check("target magnitude is 8/9", abs(c_target) == Fraction(8, 9), f"|c_TE|={abs(c_target)}")

    samples = [Fraction(-5, 1), Fraction(0, 1), Fraction(21, 4), Fraction(9, 1)]
    for rho_e in samples:
        q_e = q_from_rho(rho_e)
        check(
            f"W77 sign formula negative at rho_E={rho_e}",
            rho_e > -6 and q_e > 0 and c_te(q_e) < 0,
            f"q_E={q_e}, c_TE={c_te(q_e)}",
        )

    boundary_q = q_from_rho(Fraction(-6, 1))
    check("rho_E=-6 is the undefined center-ratio boundary", boundary_q == 0, f"q_E={boundary_q}")


def run_structural_identity_checks() -> None:
    for n_c, expected_f, expected_q, expected_rho in [
        (2, Fraction(3, 4), Fraction(20, 9), Fraction(22, 3)),
        (3, Fraction(8, 9), Fraction(15, 8), Fraction(21, 4)),
        (4, Fraction(15, 16), Fraction(16, 9), Fraction(14, 3)),
    ]:
        f = f_adj(n_c)
        q_e = q_for_magnitude_identity(n_c)
        rho_e = rho_for_magnitude_identity(n_c)
        c = c_te(q_e)
        check(f"N_c={n_c} F_adj exact", f == expected_f, f"F_adj={f}")
        check(f"N_c={n_c} structural q_E exact", q_e == expected_q, f"q_E={q_e}")
        check(f"N_c={n_c} structural rho_E exact", rho_e == expected_rho, f"rho_E={rho_e}")
        check(f"N_c={n_c} |c_TE| tracks F_adj", abs(c) == f, f"|c_TE|={abs(c)}")

    fixed_target = Fraction(8, 9)
    check("fixed N_c=3 target does not track F_adj at N_c=2", fixed_target != f_adj(2), f"8/9 vs {f_adj(2)}")
    check("fixed N_c=3 target tracks F_adj at N_c=3", fixed_target == f_adj(3), "8/9 vs 8/9")
    check("fixed N_c=3 target does not track F_adj at N_c=4", fixed_target != f_adj(4), f"8/9 vs {f_adj(4)}")


def run_independent_appearance_checks() -> None:
    # SU(3) adjoint fraction.
    check("F_adj(3)=8/9", f_adj(3) == Fraction(8, 9), f"F_adj={f_adj(3)}")

    # Same singlet-adjoint complement, written as projector/dimension data.
    total_dim = 3 * 3
    singlet_dim = 1
    adjoint_dim = total_dim - singlet_dim
    check("3 x 3bar complement has dimension 8 of 9", Fraction(adjoint_dim, total_dim) == Fraction(8, 9))

    # A separate SU(3) Casimir-product hit: C_F^2 T_F = 8/9 at N_c=3.
    cf2tf_values = {n_c: c_f_squared_t_f(n_c) for n_c in (2, 3, 4)}
    check("SU(3) C_F^2 T_F also equals 8/9", cf2tf_values[3] == Fraction(8, 9), f"C_F^2 T_F={cf2tf_values[3]}")
    check(
        "C_F^2 T_F does not track F_adj under N_c variation",
        cf2tf_values[2] != f_adj(2) and cf2tf_values[4] != f_adj(4),
        f"N2={cf2tf_values[2]} vs {f_adj(2)}, N4={cf2tf_values[4]} vs {f_adj(4)}",
    )

    # The physical kappa family keeps the count separate from weighting.
    check("kappa_EW=0 specialization equals F_adj", r_phys(3, Fraction(0, 1)) == Fraction(8, 9))
    check("kappa_EW=1 specialization equals full channel", r_phys(3, Fraction(1, 1)) == Fraction(1, 1))
    check("kappa_EW changes physical readout while count is fixed", r_phys(3, Fraction(0, 1)) != r_phys(3, Fraction(1, 1)))


def run_source_snippet_checks() -> None:
    sources = {
        "W77": ROOT / ".claude" / "tmp" / "refs" / "W77_NOTE.md",
        "W67": ROOT / ".claude" / "tmp" / "refs" / "W67_NOTE.md",
        "RCONN": ROOT / "docs" / "RCONN_DERIVED_NOTE.md",
        "KAPPA": ROOT / "docs" / "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
        "FIERZ": ROOT / "docs" / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md",
        "SINGLET": ROOT / "docs" / "CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md",
        "K3": ROOT / "docs" / "YT_P3_MSBAR_TO_POLE_K3_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md",
    }
    for label, path in sources.items():
        check(f"{label} source exists", path.exists(), str(path.relative_to(ROOT)))

    if sources["W77"].exists():
        w77 = text(sources["W77"])
        check("W77 records E_pos family", "E_pos = { lambda*(1,rho_E)" in w77)
        check("W77 records magnitude remains open", "The magnitude remains open" in w77)
    if sources["W67"].exists():
        w67 = text(sources["W67"])
        check("W67 records F_adj not typed as Route-2 center readout", "F_adj` is not typed as a Route-2" in w67)
        check("W67 records q_E=15/8 is not supplied by Fierz", "neither supplies the E-center lift" in w67)
    if sources["RCONN"].exists():
        rconn = text(sources["RCONN"])
        check("RCONN records exact F_adj formula", "(N_c^2 - 1) / N_c^2" in rconn and "8/9" in rconn)
        check("RCONN keeps physical readout rule separate", "does not follow from that algebra" in rconn)
    if sources["KAPPA"].exists():
        kappa = text(sources["KAPPA"])
        check("kappa note says count is not weight", "Count is not weight" in kappa)
        check("kappa note says Record does not supply readout context", "Record does not supply the missing readout context" in kappa)
    if sources["K3"].exists():
        k3 = text(sources["K3"])
        check("K3 color-tensor note records C_F^2 T_F=8/9", "C_F^2 T_F    =  8/9" in k3)


def run_note_hygiene_checks() -> None:
    check("new note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    if not NOTE.exists():
        return

    note = text(NOTE)
    check("note has status authority block", "Status authority:** independent audit lane only" in note)
    check("note names primary runner", "scripts/quark_route2_cte_magnitude_structural_status_bounded_2026_06_12.py" in note)
    check("note names runner cache", "logs/runner-cache/quark_route2_cte_magnitude_structural_status_bounded_2026_06_12.txt" in note)
    check("note records exact magnitude-only theorem needed", "q_E(N_c) = 5*N_c^2/(3*(N_c^2 - 1))" in note)
    check("note records rho_E(N_c) exact form", "rho_E(N_c) = 2*(2*N_c^2 + 3)/(N_c^2 - 1)" in note)
    check("note records independent appearance count", "Independent structural appearance count: 2" in note)
    check("note records no-coincidence open theorem", "sharpened open theorem" in note)
    check("note records Record/Quantum boundary", "Count is not weight" in note and "Record does not supply" in note)
    check("note records N_c=2,3,4 falsifier table", "| `2` | `3/4` | `8/9` | no | `20/9` | `22/3` | `3/4` |" in note)
    forbidden_phrases = {
        "overreach_A": "only " + "route",
        "overreach_B": "last " + "route",
        "overreach_C": "exh" + "austed",
        "overreach_D": "closes " + "the " + "program",
    }
    for label, phrase in forbidden_phrases.items():
        check(f"note avoids forbidden phrase {label}", phrase not in note)
    audit_tokens = ["audited" + "_" + "cl" + "ean", "effective" + "_" + "status"]
    check("note avoids audit-status prediction tokens", all(token not in note for token in audit_tokens))
    url_tokens = ["ht" + "tp://", "ht" + "tps://"]
    check("note has no external URL tokens", all(token not in note for token in url_tokens))


def main() -> int:
    run_exact_endpoint_checks()
    run_structural_identity_checks()
    run_independent_appearance_checks()
    run_source_snippet_checks()
    run_note_hygiene_checks()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
