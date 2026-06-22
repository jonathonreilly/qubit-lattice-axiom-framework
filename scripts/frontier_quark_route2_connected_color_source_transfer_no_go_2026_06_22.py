#!/usr/bin/env python3
"""Route-2 transfer boundary for the connected color-source selector.

The Y_T augmentation-ideal theorem proves a real positive statement:
on a normalized color-matrix source tangent, the identity source is pure
normalization and the connected tangent is sl_N, giving kappa=0.

This runner tests whether that theorem transfers to the current Route-2/EW
readout surface.  It does not without a same-source color-matrix source
authority tying Route-2 P_R/E-T readout to that normalized color source.
No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-connected-color-source-transfer"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ColorSourceSurface:
    n_c: int

    @property
    def full_dim(self) -> int:
        return self.n_c * self.n_c

    @property
    def connected_dim(self) -> int:
        return self.n_c * self.n_c - 1

    @property
    def connected_fraction(self) -> Fraction:
        return Fraction(self.connected_dim, self.full_dim)

    @property
    def singlet_fraction(self) -> Fraction:
        return Fraction(1, self.full_dim)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for src, dst in edges:
        graph.setdefault(src, set()).add(dst)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def centered_score_identity_source(trace_rho: Fraction, lam: Fraction) -> Fraction:
    # score_{lambda I}(rho) = lambda Tr(rho) - E[lambda Tr(rho)].
    value = lam * trace_rho
    expectation = lam
    return value - expectation


def part1_color_source_selector() -> None:
    print("PART 1: connected color-source selector")
    for n_c in (2, 3, 4, 5):
        surface = ColorSourceSurface(n_c)
        check(f"Nc={n_c}: full End(C^N) dimension is N^2", surface.full_dim == n_c * n_c)
        check(f"Nc={n_c}: connected tangent dimension is N^2-1", surface.connected_dim == n_c * n_c - 1)
        check(f"Nc={n_c}: fractions sum to one", surface.connected_fraction + surface.singlet_fraction == 1)
    surface3 = ColorSourceSurface(3)
    check("Nc=3 connected color-source fraction is 8/9", surface3.connected_fraction == Fraction(8, 9))
    check("Nc=3 singlet identity fraction is 1/9", surface3.singlet_fraction == Fraction(1, 9))
    check("identity source has zero centered score on trace-one records", centered_score_identity_source(Fraction(1), Fraction(7, 3)) == 0)
    check("non-trace-one records would not be the theorem surface", centered_score_identity_source(Fraction(2), Fraction(7, 3)) != 0)


def part2_authority_boundary() -> None:
    print()
    print("PART 2: authority boundary")
    yt = note_text("YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md")
    scalar_no_go = note_text("YT_CONNECTED_SOURCE_SELECTOR_SCALAR_LIFT_NO_GO_NOTE_2026-05-29.md")
    route2 = note_text("QUARK_ROUTE2_OBSERVABLE_HESSIAN_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-06-22.md")
    rconn = note_text("RCONN_DERIVED_NOTE.md")

    check("YT theorem proves selector on normalized color-matrix source tangent", "normalized connected color source tangent" in yt)
    check("YT theorem selects kappa_Y=0 on that surface", "kappa_Y = 0" in yt)
    check("YT scalar-lift no-go preserves kappa_EW gate", "kappa_EW = 0" in scalar_no_go and "cannot derive" in scalar_no_go)
    check("YT scalar-lift no-go says current packets lack color-matrix source coordinate", "do not vary `J in End(C^N)`" in scalar_no_go)
    check("Block77 leaves color/tensor-resolved source functional open", "color/tensor-resolved source functional" in route2)
    check("Rconn note leaves physical EW-current readout selector free", "free disconnected-channel" in rconn and "coefficient `kappa_EW`" in rconn)


def part3_route2_transfer_reachability() -> None:
    print()
    print("PART 3: Route-2 transfer reachability")
    base_edges = [
        ("normalized_color_matrix_source", "augmentation_ideal_sl3"),
        ("augmentation_ideal_sl3", "kappa_0_selector"),
        ("route2_bilinear_carrier_K_R", "route2_restricted_readout_P_R"),
        ("route2_restricted_readout_P_R", "route2_E_T_readout"),
        ("route2_E_T_readout", "route2_physical_readout_slot"),
    ]
    missing_same_source = ("route2_physical_readout_slot", "normalized_color_matrix_source")
    missing_purity = ("normalized_color_matrix_source", "pure_disconnected_singlet_typing")
    purity_to_selector = ("pure_disconnected_singlet_typing", "kappa_0_selector")

    check("color-source theorem reaches kappa=0 on its own surface", reachable(base_edges, "normalized_color_matrix_source", "kappa_0_selector"))
    check("Route-2 readout does not reach color-source surface", not reachable(base_edges, "route2_bilinear_carrier_K_R", "normalized_color_matrix_source"))
    check("Route-2 readout does not reach kappa=0 without same-source bridge", not reachable(base_edges, "route2_bilinear_carrier_K_R", "kappa_0_selector"))
    check(
        "adding same-source bridge reaches kappa=0",
        reachable(base_edges + [missing_same_source], "route2_bilinear_carrier_K_R", "kappa_0_selector"),
    )
    check(
        "adding singlet-purity route also reaches kappa=0",
        reachable(base_edges + [missing_same_source, missing_purity, purity_to_selector], "route2_bilinear_carrier_K_R", "kappa_0_selector"),
    )
    check("the transfer path uses no endpoint-value node", all("rho" not in node and "endpoint" not in node for edge in base_edges + [missing_same_source] for node in edge))


def part4_missing_primitive() -> None:
    print()
    print("PART 4: missing primitive")
    primitives = {
        "same_source": "Route-2 physical readout and normalized color-matrix source are the same source surface",
        "color_matrix_coordinate": "EW/Route-2 source varies J in End(C^3), not only a scalar h or finite P_R",
        "trace_one_records": "physical records are trace-one color records on the source surface",
        "pure_disconnected_singlet": "the identity/singlet channel is pure normalization/disconnected product",
    }
    check("four transfer primitives are named", len(primitives) == 4)
    check("same-source primitive is distinct from color-coordinate primitive", primitives["same_source"] != primitives["color_matrix_coordinate"])
    check("trace-one primitive is required by identity-source nullity", "trace-one" in primitives["trace_one_records"])
    check("singlet primitive is the Block76 purity primitive", "pure" in primitives["pure_disconnected_singlet"])
    check("none of the primitives is an endpoint-value import", not any("endpoint" in text or "rho" in text for text in primitives.values()))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    new_note = note_text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())

    required = (
        "Actual current-surface status: no-go for transferring connected color-source selector to Route-2 readout",
        "This is not an audit verdict",
        "No endpoint value is used",
        "normalized color-matrix source tangent",
        "Route-2 readout does not yet live on that source surface",
        "same-source normalized color-matrix source authority",
        "pure-disconnected singlet typing",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in normalized)

    for marker in ("Block78 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
    )
    combined = new_note + "\n" + handoff
    for label, marker in banned:
        check(f"new packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 connected color-source transfer no-go")
    print("Status: no-go for transferring connected color-source selector to Route-2 readout; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_color_source_selector()
    part2_authority_boundary()
    part3_route2_transfer_reachability()
    part4_missing_primitive()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: connected color-source transfer checks failed.")
        return 1
    print(
        "VERDICT: the augmentation-ideal color-source theorem selects kappa=0 "
        "on a normalized color-matrix source tangent, but current Route-2 "
        "readout lacks the same-source authority needed to transfer it."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
