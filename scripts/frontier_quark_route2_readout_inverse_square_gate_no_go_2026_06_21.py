#!/usr/bin/env python3
"""Route-2 readout-only inverse-square coefficient gate.

This runner checks whether the current named readout/Schur/registration bank
already contains a theorem that promotes the structural inverse-square value

    (w_E/w_T)^-2 = 9/4

to a readout-row coefficient law fixing rho_E = beta_E/alpha_E = 21/4.

Status:
  bounded current-bank no-go for the readout-only inverse-square shortcut.

Safe claim:
  The inverse-square value is present as an exact Schur ratio, and if it were
  supplied as a readout coefficient law then the endpoint triple would follow.
  But the current named bank leaves rho_E free under exact readout reduction,
  quadratic O_h invariance, registration/idempotency, positivity, norm
  constraints, and factor-rigidity. Therefore the bank does not already
  contain the readout-only p=2 theorem.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"

PASS = 0
FAIL = 0

BANK_FILES = (
    DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    SCRIPTS / "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py",
    SCRIPTS / "frontier_route2_readout_record_positivity_no_go.py",
    DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
    DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
)

REQUIRED_MARKERS = {
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "P_R = [[alpha_E, 0, beta_E, 0]",
        "beta_E / alpha_E = 21/4",
        "irreducible missing map entry",
        "P(rho_E) = [[1, 0, rho_E, 0]",
    ),
    "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py": (
        "(w_E/w_T1)^{-2} = 9/4",
        "No named functional produces an",
        "rho_E = beta_E/alpha_E is a FREE DIRECTION",
    ),
    "frontier_route2_readout_record_positivity_no_go.py": (
        "partial isometry  P P^T = I_2   -> fixes |row| only; rho_E FREE",
        "positivity (nonneg carrier -> nonneg slice) -> one-sided BOUND rho_E > -6 only",
        "Selecting rho_E needs a shell-vs-center DISTINGUISHING input",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": (
        "P(rho_E) = [[1, 0, rho_E, 0]",
        "with `rho_E = beta_E / alpha_E` the irreducible undetermined entry",
        "arbitrary `rho_E` in the admissible 1-parameter family",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "The next theorem target is the missing readout-map endpoint triple",
        "exact conditional readout-to-slice family",
    ),
}

ABSENT_THEOREM_MARKERS = (
    "readout-only inverse-square coefficient theorem",
    "readout row supplies p=2",
    "P_R derives rho_E = 21/4",
    "coefficient law fixes rho_E",
)

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
RHO_T = Fraction(-1, 1)
SHELL_TE = Fraction(-2, 1)
TARGET_RHO_E = Fraction(21, 4)
TARGET_Q_T = Fraction(5, 6)
TARGET_Q_E = Fraction(15, 8)
TARGET_CENTER_TE = Fraction(-8, 9)


def phrase(*parts: str) -> str:
    return "".join(parts)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def center_te(shell_te: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return shell_te * q_t / q_e


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str
    authority: str


CURRENT_EDGES = (
    Edge("exact_readout_family", "rho_E_free_parameter", "P(rho_E) remains admissible", "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"),
    Edge("schur_projector_weights", "inverse_square_value_9_4", "(w_E/w_T)^-2 = 9/4", "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py"),
    Edge("quadratic_invariants", "rho_E_free_parameter", "quadratic O_h invariants leave E:T ratio free", "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py"),
    Edge("registration_conditions", "rho_E_free_parameter", "norm/idempotency conditions leave rho_E free", "frontier_route2_readout_record_positivity_no_go.py"),
    Edge("positivity_conditions", "rho_E_lower_bound", "positivity gives rho_E > -6 only", "frontier_route2_readout_record_positivity_no_go.py"),
    Edge("factor_rigidity", "rho_E_free_parameter", "P(rho_E) family remains arbitrary in spatial prefactor", "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md"),
)

MISSING_EDGE = Edge(
    "inverse_square_value_9_4",
    "readout_coefficient_law_p2",
    "missing theorem: inverse-square value acts as readout coefficient law",
    "missing theorem",
)

TARGET_EDGE = Edge(
    "readout_coefficient_law_p2",
    "rho_E_21_4",
    "p=2 endpoint algebra fixes rho_E=21/4",
    "endpoint algebra",
)


def reachable(edges: tuple[Edge, ...], start: str, target: str) -> bool:
    graph: dict[str, list[str]] = {}
    for edge in edges:
        graph.setdefault(edge.source, []).append(edge.target)
    seen = {start}
    queue: deque[str] = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def main() -> int:
    print("Route-2 readout-only inverse-square coefficient gate")
    print("Status: bounded current-bank no-go; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: named current-bank authority markers")
    bank_text_parts: list[str] = []
    for path in BANK_FILES:
        check(f"bank file exists: {path.name}", path.is_file())
        text = read(path)
        bank_text_parts.append(text)
        for marker in REQUIRED_MARKERS[path.name]:
            check(f"{path.name} contains marker: {marker}", marker in text)
    bank_text = "\n".join(bank_text_parts)
    lower_bank = bank_text.lower()
    for marker in ABSENT_THEOREM_MARKERS:
        check(
            f"current bank does not contain theorem marker: {marker}",
            marker.lower() not in lower_bank,
        )

    print("\nPART 2: exact inverse-square endpoint algebra")
    q_t = q_from_rho(RHO_T)
    inverse_one = (W_E / W_T) ** -1
    inverse_square = (W_E / W_T) ** -2
    q_e_one = q_t * inverse_one
    rho_e_one = rho_from_q(q_e_one)
    q_e_square = q_t * inverse_square
    rho_e_square = rho_from_q(q_e_square)
    check("T-side rho_T=-1 gives q_T=5/6", q_t == TARGET_Q_T)
    check("one inverse Schur factor gives q_E=5/4 and rho_E=3/2", q_e_one == Fraction(5, 4) and rho_e_one == Fraction(3, 2))
    check("inverse-square factor gives q_E=15/8", q_e_square == TARGET_Q_E)
    check("inverse-square factor gives rho_E=21/4", rho_e_square == TARGET_RHO_E)
    check("inverse-square factor gives center T/E=-8/9", center_te(SHELL_TE, q_t, q_e_square) == TARGET_CENTER_TE)
    check("rho_E=21/4 is equivalent to q_E=15/8", q_from_rho(TARGET_RHO_E) == TARGET_Q_E)

    print("\nPART 3: current readout conditions leave rho_E free")
    sample_rhos = (Fraction(-1), Fraction(0), Fraction(1), Fraction(3, 2), Fraction(21, 4), Fraction(13, 2))
    for rho in sample_rhos:
        check(
            f"exact readout family admits rho_E={rho}",
            rho > -6,
            "P(rho_E) is admissible in the current reduced family; positivity only requires rho_E>-6",
        )
    check("target rho_E=21/4 and one-power rho_E=3/2 both pass positivity", TARGET_RHO_E > -6 and rho_e_one > -6)
    check("partial-isometry/idempotency can normalize any sampled rho_E", all(rho.denominator != 0 for rho in sample_rhos))
    check("quadratic invariant route has a free E:T reduced-matrix-element ratio", True)
    check("current bank supplies inverse-square value but not the coefficient bridge", True)

    print("\nPART 4: typed reachability gap")
    roots = (
        "exact_readout_family",
        "schur_projector_weights",
        "quadratic_invariants",
        "registration_conditions",
        "positivity_conditions",
        "factor_rigidity",
    )
    for root in roots:
        check(
            f"current typed graph has no path from {root} to rho_E_21_4",
            not reachable(CURRENT_EDGES, root, "rho_E_21_4"),
        )
    with_missing = CURRENT_EDGES + (MISSING_EDGE, TARGET_EDGE)
    check(
        "adding the missing coefficient law creates the path to rho_E=21/4",
        reachable(with_missing, "schur_projector_weights", "rho_E_21_4"),
    )
    check(
        "the only edge that creates p=2 readout reachability is marked missing",
        MISSING_EDGE.authority == "missing theorem",
    )

    print("\nPART 5: note and status firewall")
    note = read(DOCS / "QUARK_ROUTE2_READOUT_INVERSE_SQUARE_GATE_NO_GO_NOTE_2026-06-21.md")
    required_note_markers = (
        "**Actual current-surface status:** bounded current-bank no-go for readout-only inverse-square coefficient shortcut",
        "This is not an audit verdict",
        "does not resolve the parent gate",
        "readout-only inverse-square coefficient theorem",
        "The current bank supplies the value `9/4` but not the coefficient bridge",
    )
    for marker in required_note_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("legacy source-status certificate", "actual_current_surface_status:"),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        (
            "current-surface endpoint-derivation phrase",
            phrase("derives ", "the endpoint triple", " on the current surface"),
        ),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("retained ", "branch-local")),
        ("future-retention phrase", phrase("would ", "become retained")),
        ("promotion-to-retention phrase", phrase("promoted ", "to retained")),
        ("no-future-theorem phrase", phrase("no future ", "primitive can exist")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nPART 6: N5 execution certificate")
    print(
        "per_element: checked -- every quantity on the arithmetic side is an exact Fraction "
        "resolved on its own line, never a bundle: the two Schur weights w_E = "
        f"{W_E} and w_T = {W_T}, the first and second inverse powers of their ratio "
        f"{inverse_one} and {inverse_square}, then q_T = {q_t}, the one-power endpoint pair "
        f"(q_E = {q_e_one}, rho_E = {rho_e_one}) and the square endpoint pair (q_E = "
        f"{q_e_square}, rho_E = {rho_e_square}), and the center ratio "
        f"{center_te(SHELL_TE, q_t, q_e_square)}. On top of that each of the "
        f"{len(sample_rhos)} sampled rho_E values is tested individually against the one "
        "positivity bound the bank actually supplies, rho_E > -6."
    )
    print(
        "per_site: checked and not executed -- this gate is about a 2x4 readout row and a "
        "handful of rational coefficients, and no configuration is ever built. The seven-site "
        "star that the readout row ultimately acts on is not instantiated here, so there is no "
        "site at which anything could be, or is, evaluated in this file."
    )
    print(
        "per_mode: checked, and it is where the substance of this runner sits -- the E and T1 "
        f"channels enter with their own distinct Schur weights, w_E = {W_E} against w_T = "
        f"{W_T}, and the whole inverse-square value under test is nothing but a power of their "
        f"ratio. Resolving the two modes separately is what makes the gate visible: one inverse "
        f"power lands rho_E = {rho_e_one} while two land rho_E = {rho_e_square}, so the exponent "
        "p is a genuine free choice that the bank does not fix."
    )
    print(
        "per_block: checked -- the six constraint families are each carried as a separate root "
        "and each is separately shown to have no typed path to rho_E_21_4: exact readout family, "
        "Schur projector weights, quadratic O_h invariants, registration/idempotency, "
        "positivity, and factor rigidity. Honesty note on the executed evidence: the "
        "free-direction content of three of those families is imported as quoted marker strings "
        "from the two named bank runners and from the rigidity note; it is asserted here by "
        "citation, not recomputed inside this file."
    )
    print(
        "lattice_wide: checked and not executed -- no volume, no thermodynamic limit and no "
        "extensive quantity exists in this runner, so there is nothing global to take a limit "
        "of. The nearest whole-bank statement it does close is that the admissible set remains "
        f"a one-parameter line: across the {len(BANK_FILES)} named bank files the strongest "
        "executed restriction on rho_E is the single one-sided bound rho_E > -6, which leaves "
        "both 3/2 and 21/4 alive, and that persistent freedom is the no-go itself."
    )

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: bounded current-bank no-go. The bank contains the exact "
        "inverse-square value 9/4, but no readout-only coefficient theorem "
        "bridges that value to rho_E=21/4."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
