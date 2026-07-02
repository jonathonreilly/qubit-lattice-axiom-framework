#!/usr/bin/env python3
"""Route-2 source-domain bridge no-go for the R_conn endpoint target.

This block-03 Lane 3 runner checks the hard residual left by the Route-2
R_conn bridge obstruction:

    gamma_T(center) / gamma_E(center) = -R_conn = -8/9.

It verifies two facts at once.  First, if that source-domain bridge is added,
the Route-2 endpoint algebra forces rho_E = beta_E/alpha_E = 21/4 exactly.
Second, the current exact support bank has no typed edge from the retained
SU(3) color-projection channel to the Route-2 E/T endpoint readout.  Therefore
the bridge is a named missing theorem, not a retained up-type scalar law.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0
EXACT_TOL = 1.0e-12


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def percent_gap(value: float, target: float) -> float:
    return abs(value / target - 1.0) * 100.0


def r_conn(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_e_from_center_ratio(
    center_te: Fraction,
    q_t: Fraction = Fraction(5, 6),
    shell_te: Fraction = Fraction(-2, 1),
) -> Fraction:
    return shell_te * q_t / center_te


def rho_e_from_center_ratio(center_te: Fraction) -> Fraction:
    return 6 * (q_e_from_center_ratio(center_te) - 1)


def reduced_map(rho_e: Fraction) -> np.ndarray:
    return np.array(
        [
            [1.0, 0.0, float(rho_e), 0.0],
            [0.0, -2.0, 0.0, 2.0],
        ],
        dtype=float,
    )


@dataclass(frozen=True)
class TypedEdge:
    source: str
    target: str
    label: str
    authority: str
    role: str


CURRENT_TYPED_EDGES: tuple[TypedEdge, ...] = (
    TypedEdge(
        "route2_support_delta_A1",
        "route2_bilinear_carrier_K_R",
        "delta_A1 enters the exact bilinear support carrier",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        "support",
    ),
    TypedEdge(
        "route2_bright_E_T",
        "route2_bilinear_carrier_K_R",
        "E and T bright coordinates enter K_R",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        "support",
    ),
    TypedEdge(
        "route2_bilinear_carrier_K_R",
        "route2_restricted_readout_family",
        "restricted endpoints reduce to channelwise readout",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "support",
    ),
    TypedEdge(
        "route2_restricted_readout_family",
        "route2_endpoint_algebra",
        "endpoint ratios are algebraic in readout entries",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "support",
    ),
    TypedEdge(
        "route2_t_side_candidates",
        "route2_q_T_5_6_and_shell_TE_minus_2",
        "conditional T-side values used in the stretch attempt",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        "conditional",
    ),
    TypedEdge(
        "route2_center_TE_minus_8_9",
        "route2_q_E_15_8",
        "with q_T=5/6 and shell T/E=-2, center T/E=-8/9 fixes q_E",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "algebra",
    ),
    TypedEdge(
        "route2_q_E_15_8",
        "route2_rho_E_21_4",
        "rho_E = 6(q_E - 1)",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "algebra",
    ),
    TypedEdge(
        "su3_color_trace_channel",
        "su3_R_conn_8_9",
        "R_conn = (N_c^2 - 1)/N_c^2 at N_c=3",
        "RCONN_DERIVED_NOTE.md",
        "color",
    ),
)

MISSING_BRIDGE = TypedEdge(
    "su3_R_conn_8_9",
    "route2_center_TE_minus_8_9",
    "unsupported source-domain identification c_TE = -R_conn",
    "missing theorem",
    "missing",
)

EDGE_QUOTE_ANCHORS: dict[str, tuple[str, tuple[str, ...]]] = {
    "route2_support_delta_A1->route2_bilinear_carrier_K_R": (
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            'Given the named admitted-context input symbols `delta_A1, u_E, u_T : R^k -> R` and the decoupling fact of section "Named ingredients under upstream assumptions" as upstream admitted inputs, the bilinear microscopic carrier `K_R(q)` on the seven-site star support is **defined** as a 2x2 matrix of polynomial expressions in `(delta_A1(q), u_E(q), u_T(q))` and the runner verifies the corresponding endpoint-column identities to numerical zero.',
            "`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`,",
            "`vec K_R(q) := (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`.",
        ),
    ),
    "route2_bright_E_T->route2_bilinear_carrier_K_R": (
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`,",
            "`K_R(q) := (u_E(q), u_T(q), delta_A1(q) u_E(q), delta_A1(q) u_T(q))`.",
        ),
    ),
    "route2_bilinear_carrier_K_R->route2_restricted_readout_family": (
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "The exact bilinear carrier `K_R` and exact endpoint columns already force the restricted bright readout class into the channelwise form",
        ),
    ),
    "route2_restricted_readout_family->route2_endpoint_algebra": (
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "Once the readout is reduced to `P_R`, the endpoint ratios are algebraic:",
        ),
    ),
    "route2_t_side_candidates->route2_q_T_5_6_and_shell_TE_minus_2": (
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "the exact T-side candidates `rho_T = -1` and `alpha_T/alpha_E = -2` as a conditional stretch premise",
            "given the granted T-side values `q_T = 5/6` and `gamma_T(shell)/gamma_E(shell) = -2`.",
        ),
    ),
    "route2_center_TE_minus_8_9->route2_q_E_15_8": (
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "q_T = 5/6,  s_TE = -2,  c_TE = -8/9",
            "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6",
            "{5/6, -2, -8/9} -> 15/8 -> r_E = 21/4 -> D_E = 21/8.",
        ),
    ),
    "route2_q_E_15_8->route2_rho_E_21_4": (
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6",
            "beta_E / alpha_E = 21/4.",
            "{5/6, -2, -8/9} -> 15/8 -> r_E = 21/4 -> D_E = 21/8.",
        ),
    ),
    "su3_color_trace_channel->su3_R_conn_8_9": (
        "RCONN_DERIVED_NOTE.md",
        (
            "The Hilbert-space adjoint fraction is exactly `(N_c^2 - 1) / N_c^2`; at `N_c = 3` this is `8/9`.",
            "At `N_c = 3`, `F_adj = 8/9`.",
            "The exact `8/9` support remains available as `F_adj`, not as a derived connected-trace observable.",
        ),
    ),
}

UNANCHORED_EDGES: tuple[tuple[str, str], ...] = ()

DERIVED_ADDITIONAL_EDGES: tuple[TypedEdge, ...] = (
    TypedEdge(
        "route2_rho_E_21_4",
        "route2_q_E_15_8",
        "rho_E=21/4 is equivalent to q_E=15/8",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        "algebra",
    ),
    TypedEdge(
        "route2_q_E_15_8",
        "route2_center_TE_minus_8_9",
        "with granted T-side values, q_E=15/8 is equivalent to c_TE=-8/9",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        "algebra",
    ),
)

DERIVED_EDGE_QUOTE_ANCHORS: dict[str, tuple[str, tuple[str, ...]]] = {
    "route2_rho_E_21_4->route2_q_E_15_8": (
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "The target value is equivalent to any of these exact statements:",
            "rho_E = 21/4,\nq_E = gamma_E(center)/gamma_E(shell) = 15/8,",
        ),
    ),
    "route2_q_E_15_8->route2_center_TE_minus_8_9": (
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "q_E = gamma_E(center)/gamma_E(shell) = 15/8,\nc_TE = gamma_T(center)/gamma_E(center) = -8/9",
            "given the granted T-side values `q_T = 5/6` and\n`gamma_T(shell)/gamma_E(shell) = -2`.",
        ),
    ),
}

SWEEP_VOCABULARY: tuple[str, ...] = (
    "route2_support_delta_A1",
    "route2_bright_E_T",
    "route2_bilinear_carrier_K_R",
    "route2_restricted_readout_family",
    "route2_endpoint_algebra",
    "route2_t_side_candidates",
    "route2_q_T_5_6_and_shell_TE_minus_2",
    "route2_center_TE_minus_8_9",
    "route2_q_E_15_8",
    "route2_rho_E_21_4",
    "su3_color_trace_channel",
    "su3_R_conn_8_9",
    "delta_A1",
    "u_E",
    "u_T",
    "K_R",
    "bilinear microscopic carrier",
    "bilinear carrier",
    "aligned bright coordinate",
    "restricted bright readout class",
    "channelwise form",
    "P_R",
    "endpoint ratios",
    "endpoint algebra",
    "target ratio chain",
    "T-side candidates",
    "q_T = 5/6",
    "s_TE = -2",
    "gamma_T(shell)/gamma_E(shell) = -2",
    "c_TE = -8/9",
    "q_E",
    "15/8",
    "rho_E",
    "beta_E / alpha_E",
    "21/4",
    "SU(`N_c`)",
    "SU(3)",
    "F_adj",
    "8/9",
    "R_conn",
    "adjoint fraction",
    "connected-trace",
)

SWEEP_EXCEPTIONS: dict[tuple[str, str], str] = {
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "named admitted-context inputs `(delta_A1, u_E, u_T)` and a runner-verified"): "status fragment; edge anchor appears in the statement body",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "identification `u_E \u2194 <E_x, \xb7>`, `u_T \u2194 <T1x, \xb7>` from a canonical"): "open aligned-bright gap, not an inventory edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "A bridge theorem identifying the bilinear carrier `K_R(q)` with any"): "names an open physical-primitive bridge, not a current edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "`(delta_A1, u_E, u_T)` and the decoupling fact are accepted"): "audit-scope fragment, not a relation assertion",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "Whether `(u_E, u_T)`"): "sentence fragment for non-assertion about canonical coordinates",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "Under the named admitted inputs `(delta_A1, u_E, u_T)`, define the"): "lead-in to anchored K_R definition",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "- `K_R(q_A1 + E_x) - K_R(q_A1) = [[1,0],[delta_A1(r),0]]`"): "endpoint-column identity, not a new graph edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "- `K_R(q_A1 + T1x) - K_R(q_A1) = [[0,1],[0,delta_A1(r)]]`"): "endpoint-column identity, not a new graph edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "- `gamma_E = a_E u_E + b_E delta_A1 u_E`"): "old bounded projection context, not the exact restricted readout edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "- `gamma_T = a_T u_T + b_T delta_A1 u_T`"): "old bounded projection context, not the exact restricted readout edge",
    ("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md", "`K_R(q) := (u_E(q), u_T(q), delta_A1(q) u_E(q), delta_A1(q) u_T(q))`"): "restates anchored K_R definition",
    ("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md", "gamma_E = alpha_E u_E + beta_E delta_A1 u_E"): "formula inside anchored restricted readout class",
    ("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md", "gamma_T = alpha_T u_T + beta_T delta_A1 u_T"): "formula inside anchored restricted readout class",
    ("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md", "So `rho_E = 0` and `rho_E = 21/4` are both exact admissible maps on the"): "non-uniqueness statement, not an edge",
    ("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md", "- exact bilinear carrier `K_R`: already present,"): "status summary of existing edge",
    ("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md", "- smallest exact missing map entry: `beta_E / alpha_E = 21/4` after the"): "status summary of target, not a relation edge",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "`beta_E / alpha_E = 21/4`, and it does not claim retained `m_u` or `m_c`"): "scope hygiene, not an edge",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "rho_E := beta_E / alpha_E = 21/4"): "target definition restating rho_E node",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "This note asks whether `rho_E = 21/4` is forced by minimal Route-2 carrier"): "question framing, not an edge",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "`q_E = 1 + rho_E/6` and `q_T = 1 + rho_T/6`"): "definition-only algebra already covered by derived/current anchors",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "** The chain derives `21/4` if `-8/9` is"): "fan-out summary restating current chain",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "force `rho_E = 21/4`"): "negative theorem conclusion fragment, not an edge",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "The value `rho_E = 21/4`"): "lead-in to derived equivalence anchor",
    ("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md", "VERDICT: minimal Route-2 naturality does not derive rho_E = 21/4"): "runner verdict text, not an edge",
    ("RCONN_DERIVED_NOTE.md", "SU(3) adjoint channel fraction `8/9`"): "scope lead-in to anchored F_adj statement",
    ("RCONN_DERIVED_NOTE.md", "This is a no-go for unconditional `R_conn = 8/9` as a physical readout"): "negation/no-go statement, not an edge",
    ("RCONN_DERIVED_NOTE.md", "Monte Carlo connected-trace estimate with the analytic `8/9` target"): "diagnostic context, not a derivation edge",
    ("RCONN_DERIVED_NOTE.md", "- the exact adjoint fractions, including `F_adj = 8/9` at `N_c = 3`"): "runner-certificate summary of anchored color support",
    ("RCONN_DERIVED_NOTE.md", "Reopen the physical `R_conn = 8/9` readout only with a retained-grade"): "reopen condition, not a current edge",
    ("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md", "So `rho_E = 0` and `rho_E = 21/4` produce the same exact shell coupling but"): "time-coupling non-uniqueness, not a Route-2 source-domain edge",
}


def reachable(edges: tuple[TypedEdge, ...], source: str, target: str) -> tuple[bool, list[TypedEdge]]:
    graph: dict[str, list[TypedEdge]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge)

    queue: deque[tuple[str, list[TypedEdge]]] = deque([(source, [])])
    seen = {source}
    while queue:
        node, path = queue.popleft()
        if node == target:
            return True, path
        for edge in graph[node]:
            if edge.target in seen:
                continue
            seen.add(edge.target)
            queue.append((edge.target, [*path, edge]))
    return False, []


def edge_roles(edges: tuple[TypedEdge, ...]) -> set[str]:
    return {edge.role for edge in edges}


def edge_key(edge: TypedEdge) -> str:
    return f"{edge.source}->{edge.target}"


def normalize_ws(text: str) -> str:
    return " ".join(text.split())


def quote_in_text(quote: str, text: str) -> bool:
    return normalize_ws(quote) in normalize_ws(text)


def quote_is_meaningful(quote: str) -> bool:
    normalized = normalize_ws(quote)
    return len(normalized.split()) >= 8 or any(token in normalized for token in ("=", ":=", "->"))


def split_simple_sentences(text: str) -> tuple[str, ...]:
    sentences: list[str] = []
    current: list[str] = []
    for char in text:
        if char in ".;\n":
            sentence = "".join(current).strip()
            if sentence:
                sentences.append(sentence)
            current = []
        else:
            current.append(char)
    sentence = "".join(current).strip()
    if sentence:
        sentences.append(sentence)
    return tuple(sentences)


def vocabulary_hits(sentence: str) -> tuple[str, ...]:
    normalized_sentence = normalize_ws(sentence)
    hits = {
        item
        for item in SWEEP_VOCABULARY
        if normalize_ws(item) in normalized_sentence
    }
    return tuple(sorted(hits))


def authority_dependency_links(note_text: str) -> tuple[str, ...]:
    start = note_text.index("Admitted-context inputs (named upstream authorities")
    end = note_text.index("Admitted-context inputs (configured runner constants")
    block = note_text[start:end]
    filenames: set[str] = set()
    pos = 0
    while True:
        open_pos = block.find("](", pos)
        if open_pos == -1:
            break
        close_pos = block.find(")", open_pos)
        if close_pos == -1:
            break
        target = block[open_pos + 2 : close_pos]
        name = target.rsplit("/", 1)[-1]
        if name.endswith(".md"):
            filenames.add(name)
        pos = close_pos + 1
    return tuple(sorted(filenames))


def authority_bank(note_text: str) -> tuple[str, ...]:
    edge_authorities = {edge.authority for edge in CURRENT_TYPED_EDGES}
    note_authorities = set(authority_dependency_links(note_text))
    return tuple(sorted(edge_authorities | note_authorities))


def sweep_candidates(authorities: tuple[str, ...]) -> tuple[tuple[str, str, tuple[str, ...]], ...]:
    candidates: list[tuple[str, str, tuple[str, ...]]] = []
    for authority in authorities:
        text = read(DOCS / authority)
        for sentence in split_simple_sentences(text):
            hits = vocabulary_hits(sentence)
            if len(hits) >= 2:
                candidates.append((authority, normalize_ws(sentence), hits))
    return tuple(candidates)


def anchor_quote_records(include_derived: bool = True) -> tuple[tuple[str, str], ...]:
    records: list[tuple[str, str]] = []
    tables = [EDGE_QUOTE_ANCHORS]
    if include_derived:
        tables.append(DERIVED_EDGE_QUOTE_ANCHORS)
    for table in tables:
        for authority, quotes in table.values():
            for quote in quotes:
                records.append((authority, normalize_ws(quote)))
    return tuple(records)


def candidate_matches_anchor(authority: str, sentence: str) -> bool:
    for anchor_authority, quote in anchor_quote_records(include_derived=True):
        if authority != anchor_authority:
            continue
        if sentence in quote or quote in sentence:
            return True
    return False


def candidate_exception_reason(authority: str, sentence: str) -> str | None:
    for (exception_authority, exception_sentence), reason in SWEEP_EXCEPTIONS.items():
        if authority == exception_authority and normalize_ws(exception_sentence) == sentence:
            return reason
    return None


def flip_line(name: str, configured: bool, derived: bool) -> str:
    status = "FLIP" if configured != derived else "NO-FLIP"
    return f"{status}: {name} configured={configured} derived={derived}"


def main() -> int:
    print("=" * 88)
    print("LANE 3 ROUTE-2 SOURCE-DOMAIN BRIDGE NO-GO")
    print("=" * 88)

    new_note = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
    rconn_note = DOCS / "RCONN_DERIVED_NOTE.md"
    bridge_note = DOCS / "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md"
    readout_note = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    naturality_note = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
    bilinear_note = DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"
    time_note = DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    for path in (
        new_note,
        rconn_note,
        bridge_note,
        readout_note,
        naturality_note,
        bilinear_note,
        time_note,
    ):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    new_text = read(new_note)
    rconn_text = read(rconn_note)
    bridge_text = read(bridge_note)
    readout_text = read(readout_note)
    bilinear_text = read(bilinear_note)
    time_text = read(time_note)

    check(
        "R_conn surface is scoped color support, not Route-2 endpoint syntax",
        "F_adj = 8/9" in rconn_text
        and "not as a derived connected-trace observable" in normalize_ws(rconn_text)
        and "Route-2" not in rconn_text,
    )
    check("Route-2 bilinear carrier surface has no R_conn bridge", "K_R(q)" in bilinear_text and "R_conn" not in bilinear_text)
    check("Route-2 readout map surface has no R_conn bridge", "beta_E / alpha_E = 21/4" in readout_text and "R_conn" not in readout_text)
    check("Route-2 exact time-coupling surface has no R_conn bridge", "R_conn" not in time_text)
    check(
        "block02 already classified R_conn as conditional, not derivation",
        "conditional bridge" in bridge_text
        and "import boundary" in bridge_text
        and "not a retained derivation" in bridge_text,
    )
    check("new note forbids retained up-mass closure language", "does not claim retained `m_u` or `m_c`" in new_text)

    print()
    print("B. Conditional algebra if the missing bridge is supplied")
    print("-" * 72)
    r = r_conn(3)
    missing_center_ratio = -r
    q_e = q_e_from_center_ratio(missing_center_ratio)
    rho_e = rho_e_from_center_ratio(missing_center_ratio)
    check("N_c=3 gives R_conn=8/9 exactly", r == Fraction(8, 9), str(r))
    check("adding c_TE=-R_conn gives q_E=15/8 exactly", q_e == Fraction(15, 8), str(q_e))
    check("adding c_TE=-R_conn gives rho_E=21/4 exactly", rho_e == Fraction(21, 4), str(rho_e))
    check("using positive R_conn instead of -R_conn gives the wrong signed lift", rho_e_from_center_ratio(r) == Fraction(-69, 4), str(rho_e_from_center_ratio(r)))

    print()
    print("C. Typed source-domain graph")
    print("-" * 72)
    source = "su3_R_conn_8_9"
    target = "route2_rho_E_21_4"
    current_reaches, current_path = reachable(CURRENT_TYPED_EDGES, source, target)
    bridged_reaches, bridged_path = reachable(CURRENT_TYPED_EDGES + (MISSING_BRIDGE,), source, target)
    check("current typed bank has no path from R_conn to rho_E=21/4", not current_reaches, f"path length={len(current_path)}")
    check("adding the missing bridge creates the exact path to rho_E=21/4", bridged_reaches, " -> ".join(edge.target for edge in bridged_path))
    check("the only new edge in the successful path is explicitly missing", MISSING_BRIDGE in bridged_path and edge_roles(tuple(bridged_path)) >= {"missing", "algebra"})

    print()
    print("D. Endpoint-support non-uniqueness")
    print("-" * 72)
    data = restricted_readout_data()
    p_zero = reduced_map(Fraction(0, 1))
    p_target = reduced_map(Fraction(21, 4))
    e_shell = data.carrier_e_shell
    e_center = data.carrier_e_center
    t_shell = data.carrier_t_shell
    t_center = data.carrier_t_center

    check("rho_E=0 and rho_E=21/4 agree on E-shell", np.max(np.abs(p_zero @ e_shell - p_target @ e_shell)) < EXACT_TOL)
    check("rho_E=0 and rho_E=21/4 agree on granted T-shell", np.max(np.abs(p_zero @ t_shell - p_target @ t_shell)) < EXACT_TOL)
    check("rho_E=0 and rho_E=21/4 agree on granted T-center", np.max(np.abs(p_zero @ t_center - p_target @ t_center)) < EXACT_TOL)
    check("rho_E=0 and rho_E=21/4 differ only at E-center", abs((p_zero @ e_center)[0] - (p_target @ e_center)[0]) > 0.5)

    live_center = data.center_ratio_te
    check(
        "live center ratio is close to -R_conn but remains comparator-only",
        percent_gap(live_center, float(missing_center_ratio)) < 0.25 and abs(live_center - float(missing_center_ratio)) > EXACT_TOL,
        f"live={live_center:.12f}, target={float(missing_center_ratio):.12f}",
    )

    print()
    print("E. Stuck fan-out frames")
    print("-" * 72)
    low_complexity_scalars = {
        r,
        -r,
        1 - r,
        r - 1,
        1 / r,
        -1 / r,
        r / (1 - r),
        -(r / (1 - r)),
    }
    frame_results = {
        "support-endpoint": not current_reaches,
        "color-trace": r > 0 and missing_center_ratio < 0,
        "representation-domain": "singlet" in rconn_text and "adjoint" in rconn_text and "A1" in bilinear_text and "E" in bilinear_text and "T" in bilinear_text,
        "endpoint-functor": bridged_reaches and not current_reaches,
        "low-complexity-scalar": -r in low_complexity_scalars and len(low_complexity_scalars) > 4,
    }
    for name, ok in frame_results.items():
        check(f"{name} frame blocks untyped promotion", ok)
    check("fan-out has five orthogonal blocking frames", all(frame_results.values()) and len(frame_results) == 5)

    print()
    print("F. Import firewall")
    print("-" * 72)
    proof_inputs = {
        "route2_exact_carrier",
        "route2_endpoint_algebra",
        "conditional_t_side_candidates",
        "retained_su3_rconn_value",
        "typed_edge_inventory",
        "exact_rational_arithmetic",
    }
    forbidden_inputs = {
        "observed_quark_masses",
        "fitted_yukawa_entries",
        "ckm_j_target_error",
        "nearest_live_endpoint_selector",
        "untyped_rconn_endpoint_identification",
    }
    check("forbidden proof inputs are absent", proof_inputs.isdisjoint(forbidden_inputs), str(sorted(proof_inputs)))
    check(
        "new note names the missing theorem rather than closing Lane 3",
        "typed source-domain bridge theorem" in new_text
        and "claim status remains open" in new_text.lower(),
    )

    print()
    print("G. Quote-anchored typed-edge inventory")
    print("-" * 72)
    current_edge_keys = {edge_key(edge) for edge in CURRENT_TYPED_EDGES}
    anchor_edge_keys = set(EDGE_QUOTE_ANCHORS)
    unanchored_edge_keys = {edge_key for edge_key, _reason in UNANCHORED_EDGES}
    check(
        "every current typed edge is either quote-anchored or reported unanchored",
        current_edge_keys == anchor_edge_keys | unanchored_edge_keys,
        f"anchored={len(anchor_edge_keys)}, unanchored={len(unanchored_edge_keys)}",
    )
    check("no configured edge is unanchored", not UNANCHORED_EDGES)
    if UNANCHORED_EDGES:
        for name, reason in UNANCHORED_EDGES:
            print(f"FINDING: UNANCHORED edge={name} reason={reason}")
    else:
        print("FINDING: UNANCHORED none")

    for edge in CURRENT_TYPED_EDGES:
        key = edge_key(edge)
        authority, quotes = EDGE_QUOTE_ANCHORS[key]
        authority_text = read(DOCS / authority)
        check(f"anchor authority matches {key}", authority == edge.authority, authority)
        check(f"{key} has at least one quote anchor", bool(quotes), str(len(quotes)))
        for index, quote in enumerate(quotes, start=1):
            check(f"{key} quote {index} is meaningful", quote_is_meaningful(quote))
            check(f"{key} quote {index} is present in {authority}", quote_in_text(quote, authority_text))

    print()
    print("H. Exhaustiveness sweep over named authority bank")
    print("-" * 72)
    dependency_files = authority_dependency_links(new_text)
    bank_files = authority_bank(new_text)
    candidates = sweep_candidates(bank_files)
    candidate_keys = {(authority, sentence) for authority, sentence, _hits in candidates}
    anchored_candidates = [
        (authority, sentence)
        for authority, sentence, _hits in candidates
        if candidate_matches_anchor(authority, sentence)
    ]
    exception_candidates = [
        (authority, sentence)
        for authority, sentence, _hits in candidates
        if not candidate_matches_anchor(authority, sentence)
        and candidate_exception_reason(authority, sentence) is not None
    ]
    undispositioned = [
        (authority, sentence, hits)
        for authority, sentence, hits in candidates
        if not candidate_matches_anchor(authority, sentence)
        and candidate_exception_reason(authority, sentence) is None
    ]
    unused_exceptions = [
        key
        for key in SWEEP_EXCEPTIONS
        if (key[0], normalize_ws(key[1])) not in candidate_keys
    ]
    check(
        "note dependency parser finds the closed authority-bank additions",
        dependency_files
        == (
            "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
            "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
            "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
            "RCONN_DERIVED_NOTE.md",
            "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        ),
        str(dependency_files),
    )
    check(
        "authority bank is edge authorities plus dependency-linked Route-2 authorities",
        bank_files
        == (
            "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
            "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
            "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
            "RCONN_DERIVED_NOTE.md",
            "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        ),
        str(bank_files),
    )
    check("sweep found at least one candidate sentence", bool(candidates), str(len(candidates)))
    check(
        "all sweep candidate sentences are dispositioned",
        not undispositioned,
        f"candidates={len(candidates)}, anchored={len(anchored_candidates)}, exceptions={len(exception_candidates)}",
    )
    check("all sweep exceptions are currently used", not unused_exceptions, str(unused_exceptions[:2]))
    if undispositioned:
        for authority, sentence, hits in undispositioned:
            print(f"FINDING: UNDISPOSITIONED authority={authority} hits={hits} sentence={sentence}")
    check(
        "derived additional edges keep MISSING_BRIDGE out of the inventory",
        MISSING_BRIDGE not in DERIVED_ADDITIONAL_EDGES,
        str(len(DERIVED_ADDITIONAL_EDGES)),
    )
    check(
        "derived additional edges have quote-anchor entries",
        {edge_key(edge) for edge in DERIVED_ADDITIONAL_EDGES} == set(DERIVED_EDGE_QUOTE_ANCHORS),
        str(sorted(DERIVED_EDGE_QUOTE_ANCHORS)),
    )
    for edge in DERIVED_ADDITIONAL_EDGES:
        key = edge_key(edge)
        authority, quotes = DERIVED_EDGE_QUOTE_ANCHORS[key]
        authority_text = read(DOCS / authority)
        check(f"derived edge authority matches {key}", authority == edge.authority, authority)
        for index, quote in enumerate(quotes, start=1):
            check(f"derived {key} quote {index} is present in {authority}", quote_in_text(quote, authority_text))

    print()
    print("I. Reachability on quote-derived inventory")
    print("-" * 72)
    derived_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    derived_current_reaches, derived_current_path = reachable(derived_edges, source, target)
    derived_bridged_reaches, derived_bridged_path = reachable(derived_edges + (MISSING_BRIDGE,), source, target)
    configured_endpoint_functor = bridged_reaches and not current_reaches
    derived_endpoint_functor = derived_bridged_reaches and not derived_current_reaches
    flip_lines = (
        flip_line("source-to-rho without MISSING_BRIDGE", current_reaches, derived_current_reaches),
        flip_line("source-to-rho with MISSING_BRIDGE", bridged_reaches, derived_bridged_reaches),
        flip_line("endpoint-functor bypass predicate", configured_endpoint_functor, derived_endpoint_functor),
    )
    for line in flip_lines:
        print(line)
    check(
        "derived inventory still has no source-to-rho path without missing bridge",
        not derived_current_reaches,
        f"path length={len(derived_current_path)}",
    )
    check(
        "derived inventory plus missing bridge still reaches rho_E=21/4",
        derived_bridged_reaches,
        " -> ".join(edge.target for edge in derived_bridged_path),
    )
    check("derived reachability has no flips", all(line.startswith("NO-FLIP") for line in flip_lines))

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current Route-2 + SU(3) support has no typed R_conn")
        print("source-domain bridge.  Adding that bridge would force rho_E=21/4,")
        print("but without it the up-type scalar law remains open.")
        return 0
    print("VERDICT: source-domain bridge no-go verifier has failing checks.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
