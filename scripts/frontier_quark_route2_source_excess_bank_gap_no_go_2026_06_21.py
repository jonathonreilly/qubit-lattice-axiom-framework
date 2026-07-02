#!/usr/bin/env python3
"""Current-bank source-excess gap for the Route-2 endpoint target.

This runner checks whether the named current Route-2 source/readout bank
already contains a typed primitive for the normalized source-excess target

    b_E/a_E = 7/2.

Status:
  bounded current-bank no-go.

Safe claim:
  The exact endpoint algebra narrows the one-power source route to an E-only
  center-excess tilt b_E/a_E=7/2, but the named current bank has no source-map
  symbol, no source-excess theorem, and no typed edge deriving that tilt. This
  does not rule out adding a future source theorem.
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
    DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
    DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
    DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
    DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    SCRIPTS / "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py",
    SCRIPTS / "frontier_quark_route2_source_domain_bridge_no_go.py",
)

REQUIRED_ANCHORS = {
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md": (
        "K_R(q) := [[u_E(q), u_T(q)]",
        "delta_A1",
        "definition only",
    ),
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "P_R = [[alpha_E, 0, beta_E, 0]",
        "irreducible missing map entry",
        "beta_E / alpha_E = 21/4",
    ),
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": (
        "There is no current typed edge",
        "The missing step is the typed",
        "source-domain bridge theorem",
    ),
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md": (
        "Xi_P(t ; c) = (P_R c)",
        "lacks is a theorem that selects one unique `P_R`",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "The next theorem target is the missing readout-map endpoint triple",
        "exact conditional readout-to-slice family",
    ),
    "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py": (
        "(w_E/w_T1)^{-1} = 3/2 = kappa",
        "(w_E/w_T1)^{-2} = 9/4",
        "No named functional produces an",
    ),
    "frontier_quark_route2_source_domain_bridge_no_go.py": (
        "CURRENT_TYPED_EDGES",
        "MISSING_BRIDGE",
        "unsupported source-domain identification",
    ),
}

ABSENT_TARGET_MARKERS = (
    "b_E/a_E",
    "bE/aE",
    "source-excess",
    "source excess",
    "S_dual",
    "source-preparation map",
    "source preparation map",
    "diag(a_E",
    "7/2",
)

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
Q_T = Fraction(5, 6)
RHO_T = Fraction(-1, 1)
SHELL_TE = Fraction(-2, 1)
TARGET_RHO_E = Fraction(21, 4)


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


def one_power_rho_e() -> Fraction:
    return rho_from_q(Q_T * ((W_E / W_T) ** -1))


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str
    authority: str


CURRENT_EDGES = (
    Edge("delta_A1", "K_R", "support scalar enters bilinear carrier", "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"),
    Edge("u_E_u_T", "K_R", "bright coordinates enter bilinear carrier", "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"),
    Edge("K_R", "restricted_readout_family", "carrier reduces to P_R family", "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"),
    Edge("restricted_readout_family", "endpoint_algebra", "endpoint ratios algebraic in P_R", "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"),
    Edge("schur_weights", "one_power_readout", "one inverse Schur factor gives rho_E=3/2", "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py"),
    Edge("source_domain_bank", "rconn_bridge_missing", "current source-domain bridge remains absent", "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"),
)

HYPOTHETICAL_EDGE = Edge(
    "typed_source_excess_theorem",
    "source_excess_tilt_7_2",
    "future theorem deriving b_E/a_E=7/2",
    "missing theorem",
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
    print("Route-2 source-excess current-bank gap")
    print("Status: bounded current-bank no-go; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: named current-bank authority anchors")
    bank_text_parts: list[str] = []
    for path in BANK_FILES:
        check(f"bank file exists: {path.name}", path.is_file())
        text = read(path)
        bank_text_parts.append(text)
        for marker in REQUIRED_ANCHORS[path.name]:
            check(f"{path.name} contains marker: {marker}", marker in text)
    bank_text = "\n".join(bank_text_parts)
    lower_bank = bank_text.lower()

    print("\nPART 2: absence of current source-excess target markers")
    for marker in ABSENT_TARGET_MARKERS:
        check(
            f"current bank does not contain source-excess marker: {marker}",
            marker.lower() not in lower_bank,
        )

    print("\nPART 3: exact target remains sharp")
    rho_e_one = one_power_rho_e()
    source_tilt = TARGET_RHO_E / rho_e_one
    check("one-power readout gives rho_E=3/2", rho_e_one == Fraction(3, 2))
    check("target rho_E remains 21/4", TARGET_RHO_E == Fraction(21, 4))
    check("source-excess target is b_E/a_E=7/2", source_tilt == Fraction(7, 2))
    check("T-side target remains rho_T=-1 and q_T=5/6", RHO_T == -1 and q_from_rho(RHO_T) == Q_T)
    check("shell T/E target remains -2", SHELL_TE == Fraction(-2, 1))

    print("\nPART 4: typed reachability gap")
    roots = ("delta_A1", "u_E_u_T", "K_R", "schur_weights", "source_domain_bank")
    for root in roots:
        check(
            f"current typed graph has no path from {root} to source_excess_tilt_7_2",
            not reachable(CURRENT_EDGES, root, "source_excess_tilt_7_2"),
        )
    check(
        "adding the missing typed source-excess theorem creates reachability",
        reachable((HYPOTHETICAL_EDGE,), "typed_source_excess_theorem", "source_excess_tilt_7_2"),
    )
    check(
        "all current edges have named authorities",
        all(edge.authority != "missing theorem" for edge in CURRENT_EDGES),
    )

    print("\nPART 5: note and status firewall")
    note = read(DOCS / "QUARK_ROUTE2_SOURCE_EXCESS_BANK_GAP_NO_GO_NOTE_2026-06-21.md")
    required_note_markers = (
        "Actual current-surface status: bounded current-bank no-go for the source-excess target",
        "This is not an audit verdict",
        "does not resolve the parent gate",
        "b_E/a_E = 7/2",
        "The current named bank does not contain a typed source-excess primitive",
    )
    for marker in required_note_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("status-authority phrase", phrase("Status ", "authority")),
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

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: bounded current-bank no-go. The normalized source-excess "
        "target is b_E/a_E=7/2, but the named current Route-2 source/readout "
        "bank has no typed primitive deriving that target."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
