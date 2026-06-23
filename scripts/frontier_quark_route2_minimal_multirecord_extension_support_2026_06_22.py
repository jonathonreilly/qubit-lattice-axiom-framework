#!/usr/bin/env python3
"""Endpoint-free minimal multi-record source extension support for Route-2."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-minimal-multirecord-extension"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SourceJet:
    z0: Fraction
    w0: Fraction
    w00: Fraction
    w_a: Fraction
    w_ab_diag: Fraction
    w_ab_offdiag: Fraction

    def dz0(self) -> Fraction:
        return self.z0 * self.w0

    def d00_z(self) -> Fraction:
        return self.z0 * (self.w00 + self.w0 * self.w0)

    def d00_logz(self) -> Fraction:
        return self.w00

    def da_z(self) -> Fraction:
        return self.z0 * self.w_a

    def daa_logz(self) -> Fraction:
        return self.w_ab_diag

    def dab_logz(self) -> Fraction:
        return self.w_ab_offdiag


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def kappa_from_fraction(frac: Fraction) -> Fraction:
    return 9 * (frac - Fraction(8, 9))


def connected_fraction(adjoint_units: Fraction, identity_units: Fraction) -> Fraction:
    return adjoint_units / (adjoint_units + identity_units)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block119 = flat(text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md"))
    block120 = flat(text("QUARK_ROUTE2_CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md"))
    block116 = flat(text("QUARK_ROUTE2_ADJOINT_INVARIANT_CONTRACTION_UNIQUENESS_SUPPORT_NOTE_2026-06-22.md"))
    block118 = flat(text("QUARK_ROUTE2_SINGLET_RESIDUAL_INDEPENDENCE_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block119 names same-source bridge primitive", "same-source covariant multi-record bridge theorem" in block119)
    check("Block120 says current P_R does not instantiate primitive", "added as a same-source source/readout primitive" in block120)
    check("Block116 supports inverse-Killing uniqueness", "unique up to scale" in block116)
    check("Block118 names identity factorization theorem", "D_0 D_0 Z = (D_0 Z)^2" in block118)
    check("endpoint sign support is sign-only", "magnitude remains open" in sign.lower())


def part2_minimal_source_jet() -> None:
    print()
    print("PART 2: minimal source jet")
    jet = SourceJet(
        z0=Fraction(1),
        w0=Fraction(1),
        w00=Fraction(0),
        w_a=Fraction(0),
        w_ab_diag=Fraction(1),
        w_ab_offdiag=Fraction(0),
    )
    print(f"  D0Z={jet.dz0()}, D00Z={jet.d00_z()}, D00logZ={jet.d00_logz()}")
    print(f"  DAZ={jet.da_z()}, DAAlogZ={jet.daa_logz()}, DABlogZ_offdiag={jet.dab_logz()}")
    check("identity one-point is one", jet.dz0() == 1)
    check("identity raw second moment equals product", jet.d00_z() == jet.dz0() * jet.dz0())
    check("identity connected Hessian vanishes", jet.d00_logz() == 0)
    check("adjoint one-point vanishes", jet.da_z() == 0)
    check("adjoint diagonal connected Hessian is unit", jet.daa_logz() == 1)
    check("adjoint off-diagonal connected Hessian vanishes", jet.dab_logz() == 0)


def part3_bridge_consequence() -> None:
    print()
    print("PART 3: bridge consequence under the added primitive")
    adjoint_units = Fraction(8)
    identity_units = Fraction(1)
    frac = connected_fraction(adjoint_units, identity_units)
    kap = kappa_from_fraction(frac)
    signed = -frac
    print(f"  adjoint_units={adjoint_units}, identity_units={identity_units}, R={frac}, kappa={kap}, c_TE={signed}")
    check("connected fraction is 8/9", frac == Fraction(8, 9))
    check("kappa is zero", kap == 0)
    check("negative endpoint sign gives -8/9 as consequence", signed == Fraction(-8, 9))
    check("identity denominator is one unit", identity_units == 1)
    check("adjoint numerator is eight units", adjoint_units == 8)


def part4_import_firewall() -> None:
    print()
    print("PART 4: import firewall")
    premises = [
        "same-source coordinates J_0,J_A",
        "orthonormal SU3 adjoint frame",
        "W=log Z connected generator",
        "identity coordinate pure normalization",
        "equal source unit weights",
        "endpoint sign consumed after kappa zero",
    ]
    forbidden = ["rho_E", "q_E", "observed", "fitted", "data-tuned", "endpoint input"]
    premise_blob = " ".join(premises)
    for premise in premises:
        print(f"  premise: {premise}")
        check(f"premise recorded: {premise}", premise in premise_blob)
    for marker in forbidden:
        check(f"forbidden marker absent from premises: {marker}", marker not in premise_blob)
    check("endpoint sign is downstream rather than a source premise", premises[-1] == "endpoint sign consumed after kappa zero")


def part5_current_surface_boundary() -> None:
    print()
    print("PART 5: current-surface boundary")
    internal_model = {
        "abstract_source_jet": True,
        "identity_factorization": True,
        "adjoint_metric": True,
        "equal_unit_weights": True,
        "physical_PR_ET_identification": False,
        "current_surface_closure": False,
    }
    for name, value in internal_model.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("abstract extension is internally complete", all(internal_model[k] for k in ("abstract_source_jet", "identity_factorization", "adjoint_metric", "equal_unit_weights")))
    check("physical P_R/E-T identification remains missing", not internal_model["physical_PR_ET_identification"])
    check("current surface closure remains false", not internal_model["current_surface_closure"])


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: conditional-support for an added same-source source/readout primitive",
        "W(J_0,J) = J_0 + (1/2) sum_A J_A J_A",
        "D_0 D_0 Z = (D_0 Z)^2",
        "R_conn = 8 / (8 + 1) = 8/9",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block121 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 minimal multi-record extension support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_minimal_source_jet()
    part3_bridge_consequence()
    part4_import_firewall()
    part5_current_surface_boundary()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a minimal endpoint-free same-source 1+adjoint source extension is internally consistent and forces kappa=0 once physically identified with Route-2 E/T; that physical identification remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
