#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 route triage note.

This is a support runner. It verifies route arithmetic and the non-claim
boundary; it does not derive a charged-lepton mass or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2
M_W_ERR = 13.3
G_F = 1.1663787e-5


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("route triage note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = " ".join(note.split())

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        "docs/G_WEAK_FROM_FRAMEWORK_NOTE_2026-05-03.md",
        "docs/G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "E_H = m_e alpha(0)^2",
        "S_l     = 1/256",
        "Route A: `M_2(C)^tensor4` exponent route",
        "Route B: lattice `g_2^2 / 64` route",
        "Route C: C-iso anisotropy-ratio route",
        "Follow-up A1 firewall",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "(1/sqrt(2))*(1/16)",
        "Follow-up A1 full-cell source-carrier support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "full OS0-cell linear source",
        "slot-additive, diagonal",
        "Follow-up A1 D17/full-cell separability support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "(1/sqrt(2))*(1/256)",
        "Follow-up A1 source-coupled attachment support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md",
        "source-coupled local-action convention",
        "dS_lep/dj_c = h * B_lep * O_c",
        "Follow-up A2 discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "projection/Born trace",
        "algebra-basis coefficient density",
        "Follow-up A2 source-norm discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "L1 algebra-coordinate density",
        "L2 / Hilbert-Schmidt /",
        "Follow-up A2 source-action simplex transfer discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md",
        "top/RN/Fisher source-action precedent",
        "linear action coefficient density",
        "Follow-up A2 source-action simplex uniformity support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md",
        "local coordinate relabelings",
        "transitivity forces a single",
        "Follow-up A2 basis-selector discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "basis/source-frame selector",
        "full inner-automorphism covariance",
        "Follow-up A2 restricted tensor-frame support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "slot permutations",
        "coordinate bijections",
        "coefficient uniformity sub-wall",
        "Follow-up A2 source-slot frame selector support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md",
        "J(j) = sum_c j_c O_c",
        "Full `U(16)` conjugations change the source-control family",
        "Follow-up A2 source-strength additivity selector support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md",
        "source-strength additivity",
        "mu({c}) = 1/256",
        "L2/RN/Fisher source-unit class",
        "additive source-strength semantics",
        "Follow-up A2 source-control linearity support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md",
        "J(j_A + j_B) = J(j_A) + J(j_B)",
        "source-coupled local action gives algebraic",
        "does not supply positivity or total",
        "Follow-up A2 source-strength normalization gauge firewall",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md",
        "S_src[j] = h * B_lep * J(j)",
        "(h, j) -> (h/lambda, lambda j)",
        "total-strength section",
        "reads normalized source weight",
        "Follow-up A2 projective-simplex section support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md",
        "nonzero nonnegative projective source ray",
        "sigma([j])_c = j_c / sum_d j_d",
        "sigma([1])_c = 1/256",
        "physical projective semantics",
        "Follow-up A2 source positive-cone discriminator support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md",
        "real monotone finitely additive measure",
        "normalized source-strength weights",
        "source-strength semantic target",
        "Follow-up A2 source-coupling gauge quotient projectivization support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md",
        "H = h * sum_c j_c",
        "front/source-shape quotient",
        "physical source-probe readout rule",
        "Follow-up A2 source-shape readout selector discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "sigma([j])_c = (h*j_c)/H",
        "raw `h`, raw `j_c`, `h*j_c`, `H`",
        "source-shape selector",
        "Follow-up A2 projective tensor-frame uniform-ray support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md",
        "finite-order positive scale character",
        "projective invariance becomes ordinary invariance",
        "finite transitive tensor-frame projective invariance",
        "physical invariance bridge",
        "Follow-up A2 projective tensor-frame invariance bridge support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md",
        "source-family preserving relabeling",
        "rho_g J(j) = J(rho_g j)",
        "source-family naturality",
        "physical license for source-family naturality",
        "Follow-up A2 source-naturality label-free license support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md",
        "label-free, meaning its source controls carry no physical coordinate tag",
        "source-coordinate isomorphism invariance",
        "derivation or ratification of the label-free source interface",
        "Follow-up A2 `S_l` readout identity bridge support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md",
        "y_scale = g_2 * (1/sqrt(2)) * S_l",
        "S_l = sigma([j])_c",
        "physical license for the `S_l` source-readout convention",
        "Follow-up A2 source-probe interface compression support",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md",
        "normalized label-free charged-lepton full-cell source-probe interface",
        "exact `S_l = 1/256`",
        "Follow-up A2 source-probe ratification target discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "full F/L/P/R interface",
        "every one-clause-removed",
        "does not ratify F/L/P/R",
        "Follow-up A2 source-probe interface ratification decision packet",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "Follow-up A2 F-clause source/action assembly discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "F1 source-coupled local-action convention",
        "F2 charged-lepton sector specificity",
        "F3 full OS0-cell tensor source locality",
        "F4 scalar-multiplier attachment",
        "all F1-F4 supplied",
        "one-input-removed F target fails",
        "Follow-up A2 F1 source-coupled local-action ratification target discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "S[j] = S_0 + sum_c j_c A_c",
        "dS/dj_c = A_c",
        "does not ratify F1",
        "Follow-up A2 F2 charged-lepton source-block selector discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "D17 supplies the bounded charged-lepton scalar",
        "Z_lep^2 = 2",
        "does not ratify F2",
        "Follow-up A2 F3 full-cell tensor source-locality ratification target discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "physical charged-lepton source-locality license",
        "does not ratify F3",
	        "Follow-up A2 F4 scalar-multiplier attachment ratification target discriminator",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
	        "D17 block preservation instead of `512` product weights",
	        "does not ratify F4",
	        "Follow-up A2 L label-free source-coordinate ratification target discriminator",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
	        "source interface, tensor-frame relabeling",
	        "coordinate-tagged nonuniform ray",
	        "does not ratify L",
	        "Follow-up A2 P positive projective source-strength ratification target discriminator",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
		        "source-strength object, positive nonzero",
		        "raw `h`, raw `j_c`, `h*j_c`, `H`, and",
		        "does not ratify P",
		        "Follow-up A2 R `S_l` readout identity ratification target discriminator",
		        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
		        "scale-symbol context, source coefficient context",
		        "symbol-only, coefficient-only, mismatched-front",
		        "does not ratify R",
		        "Follow-up A2 source-coordinate unfixed-choice label-free support",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md",
        "law may not depend on an unfixed choice",
        "requires an admitted coordinate tag",
        "Follow-up A3 firewall",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "C_A3 = 0.999678091",
        "Follow-up A3 placement discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md",
        "source readout, the weak front factor",
        "Koide/electron readout factor",
        "license one placement",
        "Follow-up A3 precision-placement decision packet",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "ONE_PLACEMENT_SELECTED",
        "NO_SOURCE_DOUBLE_COUNT",
        "Koide native zero-section `#5007` impact discriminator",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "BRIDGE_TEXT_LOCK",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "Tier-A owner-retirement `#4991` impact discriminator",
        "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md",
        "owner-governed premise standing",
        "zero-source readout, the real-primitive Brannen endpoint",
        "physical electron species bridge",
        "Follow-up firewall",
        "Lane 6, charged leptons",
        "derive the charged-lepton `M_2(C)` exponent/selector",
        "retire the `/64` convention import",
        "Precision follow-up",
        "requires the theorem to declare whether `C_A3` belongs",
        "one-placement/no-double-count owner/audit contract",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed partial-triage passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    primitive_markers = [
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "minimal axioms",
    ]
    for marker in primitive_markers:
        audit.check(f"primitive-registry boundary named: {marker}", marker in note)

    section("Arithmetic: three 256 handles")
    dim_m2 = 4
    audit.check("M_2 complex dimension is 4", dim_m2 == 4)
    audit.check("M_2 tensor exponent handle gives 4^4 = 256", dim_m2**4 == 256)
    audit.check("reciprocal M_2 tensor value is exact 1/256", Fraction(1, dim_m2**4) == Fraction(1, 256))

    g2_lat_sq = Fraction(1, 4)
    y0_lattice = g2_lat_sq / Fraction(64)
    audit.check("lattice weak route gives (1/4)/64 = 1/256", y0_lattice == Fraction(1, 256))
    audit.check("squared lattice y0 gives 1/65536", y0_lattice * y0_lattice == Fraction(1, 65536))

    for xi in [Fraction(1, 16), Fraction(16, 1)]:
        beta_sigma = Fraction(6, 1) / xi
        beta_tau = Fraction(6, 1) * xi
        ratio = beta_tau / beta_sigma
        audit.check(
            f"C-iso ratio beta_tau/beta_sigma = xi^2 at xi={xi}",
            ratio == xi * xi,
            f"ratio={ratio}",
        )
        audit.check(
            f"C-iso geometric mean invariant at xi={xi}",
            beta_sigma * beta_tau == 36,
            f"beta_sigma*beta_tau={beta_sigma * beta_tau}",
        )

    section("Lepton scale comparator arithmetic")
    a2 = a_lepton_squared()
    empirical_divisor = M_W / a2
    offset = (M_W / 256.0 - a2) / a2
    n_sigma = abs(empirical_divisor - 256.0) / (256.0 * (M_W_ERR / M_W))
    v_gev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5
    v_mev = v_gev * 1000.0
    g2_from_mw = 2.0 * M_W / v_mev
    y_star = g2_from_mw * (1.0 / math.sqrt(2.0)) / 256.0
    y_from_mw = (M_W / 256.0) * math.sqrt(2.0) / v_mev
    audit.check(
        "empirical divisor is near 256.08, not exact 256",
        256.04 < empirical_divisor < 256.13 and abs(empirical_divisor - 256.0) > 0.05,
        f"N={empirical_divisor:.4f}",
    )
    audit.check(
        "m_W/256 offset is about 0.032 percent",
        0.0002 < abs(offset) < 0.0005,
        f"offset={100.0 * offset:+.4f}%",
    )
    audit.check(
        "integer 256 is more than 1.5 sigma_mW from preferred divisor",
        n_sigma > 1.5,
        f"sigma={n_sigma:.2f}",
    )
    audit.check(
        "lepton star identity is algebraic given m_W = g_2 v/2",
        abs(y_star - y_from_mw) / y_from_mw < 1e-12,
        f"relative diff={(y_star - y_from_mw) / y_from_mw:.3e}",
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the exponent `4`.",
        "No derivation of the `/64` normalization.",
        "No proof that `S_l = y_0_lattice`.",
        "No derivation of `m_e`, Koide, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives hydrogen",
        "This note derives a charged-lepton mass",
        "S_l is retained",
        "hydrogen is retained",
        "alpha(0) is derived",
        "m_e is derived",
        "the `/64` normalization is derived",
        "S_l = y_0_lattice is proven",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
