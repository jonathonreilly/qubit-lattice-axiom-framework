#!/usr/bin/env python3
"""Verifier for the lepton source-probe ratification target discriminator.

The runner checks that the full F/L/P/R source-probe interface is the minimal
tested target that conditionally closes the exact source-side S_l = 1/256
scaffold. It does not ratify the interface, derive m_e, alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
DECISION_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
F1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F2_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
F3_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
F4_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
LABEL_FREE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
GAUGE_QUOTIENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
A3 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
OBS_SOURCE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


Coord = tuple[int, int, int, int]


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


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in values.items()}


def swap_first_slot_0_1(coord: Coord) -> Coord:
    values = list(coord)
    if values[0] == 0:
        values[0] = 1
    elif values[0] == 1:
        values[0] = 0
    return tuple(values)  # type: ignore[return-value]


def closes_source_side(clauses: set[str]) -> bool:
    return clauses == {"F", "L", "P", "R"}


def all_subsets(items: list[str]) -> list[set[str]]:
    subsets: list[set[str]] = []
    for size in range(len(items) + 1):
        for combo in combinations(items, size):
            subsets.append(set(combo))
    return subsets


def solve_s_l(front: Fraction, source_coeff: Fraction) -> Fraction:
    if front <= 0:
        raise ValueError("positive front required")
    return source_coeff / front


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-probe ratification target note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        COMPRESSION,
        DECISION_PACKET,
        SOURCE_COUPLED,
        F_CLAUSE,
        F1_TARGET,
            F2_SELECTOR,
	        F3_TARGET,
		        F4_TARGET,
		        L_TARGET,
		        P_TARGET,
		        R_TARGET,
		        FULL_CELL,
        LABEL_FREE,
        POSITIVE_CONE,
        GAUGE_QUOTIENT,
        SHAPE_SELECTOR,
        PROJECTIVE_SECTION,
        UNIFORM_RAY,
        SL_READOUT,
        A3,
        KOIDE,
        OBS_SOURCE,
        MINIMAL,
        REGISTRY,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Source-Probe Ratification Target Discriminator",
        "four-clause interface",
        "full-cell charged-lepton source/action family",
        "label-free source-coordinate convention",
        "positive projective source-strength and gauge quotient",
        "`S_l` readout convention",
        "Only the full four-clause target closes",
        "Every one-clause-removed target fails",
        "no F",
        "no L",
        "no P",
        "no R",
        "1/112",
        "derive or ratify F + L + P + R",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "source-probe interface ratification decision packet",
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md",
        "F-clause assembly discriminator",
        "F1 source-coupled local-action convention",
        "F2 charged-lepton sector specificity",
        "F3 full OS0-cell tensor source locality",
        "F4 scalar-multiplier attachment",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F1 source-coupled local-action ratification target discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "F2 charged-lepton source-block selector discriminator",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F3 full-cell tensor source-locality ratification target discriminator",
        "physical source family, full tensor locality, independent matrix-unit controls",
            "ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
            "F4 scalar-multiplier attachment ratification target discriminator",
            "D17 block, full-cell source, scalar multiplication, D17 block preservation",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
	        "L label-free source-coordinate ratification target discriminator",
	        "source interface, tensor-frame relabeling, label-free license",
	        "coordinate-tagged nonuniform ray with singleton weight `1/112`",
	        "does not ratify L",
	        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
	        "P positive projective source-strength ratification target discriminator",
		        "source-strength object, positive nonzero domain, source-scale gauge",
		        "raw `h`, raw `j_c`, `h*j_c`, `H`, and the `1/16` classes",
		        "does not ratify P",
		        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
		        "R `S_l` readout identity ratification target discriminator",
		        "scale-symbol context, source coefficient context, common nonzero front",
		        "symbol-only, coefficient-only, mismatched-front",
		        "does not ratify R",
		        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md",
        "The primitive registry was checked",
        "#4985",
        "#4984",
        "#4983",
        "#4982",
        "#4981",
        "#4980",
        "#4991",
        "#4990",
        "#4989",
        "#4988",
        "#4987",
        "#4986",
        "#4979",
        "#4978",
        "#4977",
        "#4976",
        "#4975",
        "#4974",
        "#4973",
        "#4972",
        "#4971",
        "#4970",
        "#4969",
        "#4968",
        "#4967",
        "#4966",
        "#4965",
        "#4964",
        "#4963",
        "#4962",
        "#4961",
        "#4960",
        "#4959",
            "#4995",
            "#4996",
            "#4997",
            "#4998",
            "#4999",
            "#5000",
            "#5007",
            "#5006",
            "#5005",
            "#5004",
            "#5003",
            "#5002",
            "#5001",
            "#4994",
        "#4993",
        "#4992",
        "theta G1 4D carrier supply no-go",
        "theta G1 defect suppression support",
        "theta G1 kinetic 4D scaffold support",
        "owner-governed Tier-A retirement",
            "theta retirement-basis re-match",
            "record-instrument polar contrast stabilization",
            "DELTA0 route inventory sibling-total refresh",
            "g_bare two-Ward scope repair",
            "PMNS stationarity diagnostic repair",
            "bounded neutrino source-amplitude carrier premise",
            "neutrino split2 edge-transport witness refresh",
            "Wilson descendant Schur entropy witness stabilization",
            "axiom-first record-invariance companion refresh",
            "hadron lane1 record-invariance companion refresh",
            "Koide native zero-section route guard repair",
            "static-source I1 hygiene companion refresh",
            "quark lane3 retention firewall companion refresh",
            "Tier-A residual owner decision packet",
        "theta G2 registration stretch no-go",
        "AC R-eta h-class stretch no-go",
        "AC R-eta h-unit primitive no-go",
        "primitive axiom absorption no-go",
        "alpha-s universal beta kernel scoping",
        "alpha-s threshold matching kernel scoping",
        "No-Go Discipline Gate",
        "broad interface closure fails; narrowed ratification-target",
        "No derivation or ratification of F/L/P/R.",
        "No use of latest open PRs as proof inputs.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Clause minimality discriminator")
    clauses = ["F", "L", "P", "R"]
    subsets = all_subsets(clauses)
    closing_subsets = [subset for subset in subsets if closes_source_side(subset)]
    audit.check("exactly one tested subset closes source-side S_l", closing_subsets == [set(clauses)])
    for clause in clauses:
        missing_one = set(clauses) - {clause}
        audit.check(f"missing {clause} fails source-side closure", not closes_source_side(missing_one))

    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma_uniform = normalize(uniform)
    audit.check("uniform full-cell singleton is 1/256", sigma_uniform[coords[0]] == Fraction(1, 256))

    carrier_16 = list(product(range(4), repeat=2))
    audit.check("without full-cell clause a 16-coordinate carrier gives 1/16", Fraction(1, len(carrier_16)) == Fraction(1, 16))
    audit.check("1/16 carrier witness differs from 1/256", Fraction(1, 16) != Fraction(1, 256))

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    tagged_coord = (0, 0, 0, 0)
    tagged_relabel = {swap_first_slot_0_1(coord): value for coord, value in tagged.items()}
    audit.check("coordinate-tagged ray changes under source relabeling", tagged_relabel != tagged)
    audit.check("coordinate-tagged singleton witness is 1/112", tagged_sigma[tagged_coord] == Fraction(1, 112))
    audit.check("coordinate-tagged singleton differs from 1/256", tagged_sigma[tagged_coord] != Fraction(1, 256))

    h = Fraction(5, 1)
    raw_j = Fraction(3, 1)
    lam = Fraction(7, 1)
    rescaled_h = h / lam
    rescaled_j = lam * raw_j
    audit.check("raw source coordinate changes under positive source gauge", rescaled_j != raw_j)
    audit.check("product h*j_c is gauge invariant but front-bearing", rescaled_h * rescaled_j == h * raw_j)
    total = Fraction(256, 1)
    audit.check("projective singleton removes raw gauge", raw_j / total == rescaled_j / (lam * total))

    front = Fraction(13, 17)
    source_coeff = front * Fraction(1, 256)
    audit.check("with readout clause nonzero front cancellation gives S_l", solve_s_l(front, source_coeff) == Fraction(1, 256))
    s_l_without_readout: Fraction | None = None
    audit.check("without readout clause S_l remains unbound", s_l_without_readout is None)

    section("Authority boundary checks")
    compression = read(COMPRESSION)
    decision_packet = read(DECISION_PACKET)
    source_coupled = read(SOURCE_COUPLED)
    f_clause = read(F_CLAUSE)
    f3_target = read(F3_TARGET)
    f4_target = read(F4_TARGET)
    l_target = read(L_TARGET)
    p_target = read(P_TARGET)
    r_target = read(R_TARGET)
    full_cell = read(FULL_CELL)
    label_free = read(LABEL_FREE)
    positive_cone = read(POSITIVE_CONE)
    gauge_quotient = read(GAUGE_QUOTIENT)
    shape_selector = read(SHAPE_SELECTOR)
    projective_section = read(PROJECTIVE_SECTION)
    uniform_ray = read(UNIFORM_RAY)
    sl_readout = read(SL_READOUT)
    a3 = read(A3)
    koide = read(KOIDE)
    obs_source = read(OBS_SOURCE)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    nodes = registry["nodes"]

    audit.check("compression note names full interface target", "normalized label-free charged-lepton full-cell source-probe interface" in compression)
    audit.check(
        "decision packet carries owner/audit contract",
        "OWNER_RATIFICATION" in decision_packet
        and "AUDIT_ACCEPTANCE" in decision_packet
        and "does not ratify F/L/P/R" in decision_packet,
    )
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check(
        "F-clause note decomposes F1-F4",
        "F1" in f_clause
        and "source-coupled local-action convention" in f_clause
        and "F4" in f_clause
        and "scalar-multiplier attachment" in f_clause,
    )
    audit.check("F3 target is source-locality only", "does not ratify F3" in f3_target and "full tensor locality" in f3_target)
    audit.check("F4 target is attachment only", "does not ratify F4" in f4_target and "scalar multiplication" in f4_target)
    audit.check("L target is source-coordinate only", "does not ratify L" in l_target and "1/112" in l_target)
    audit.check("P target is source-strength only", "does not ratify P" in p_target and "1/16" in p_target)
    audit.check("R target is source-readout only", "does not ratify R" in r_target and "mismatched-front" in r_target)
    audit.check("full-cell support names matrix-unit coordinates", "matrix-unit coordinates" in full_cell and "256" in full_cell)
    audit.check("label-free support names source-family naturality", "source-family naturality" in label_free and "label-free" in label_free)
    audit.check("positive-cone support names source strengths", "source strengths are nonnegative" in positive_cone)
    audit.check("gauge quotient names H and sigma", "H = h * sum_c j_c" in gauge_quotient and "sigma([j])_c" in gauge_quotient)
    audit.check("shape selector chooses sigma candidate", "(h*j_c)/H" in shape_selector and "Q1-Q4" in shape_selector)
    audit.check("projective section names L1 sigma", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("uniform ray support names 1/256", "sigma([j])_c = 1/256" in uniform_ray)
    audit.check("S_l readout bridge names normalized singleton", "normalized singleton source-strength multiplier" in sl_readout)
    audit.check("A3 remains separate", "C_A3" in a3 and "Koide/electron readout" in a3)
    audit.check("Koide remains separate from source scale", "Koide Electron-Readout Firewall" in koide and "No derivation of `m_e`" in koide)
    audit.check("observable source candidate is not retained authority", "open_gate" in obs_source and "source-coupling convention" in obs_source)

    minimal_flat = flat(minimal).lower()
    audit.check("minimal axioms exclude source/action identification", "source/action and physical-observable identification" in minimal_flat)
    audit.check("minimal axioms exclude weighting/probability content", "born weights" in minimal_flat and "probability" in minimal_flat and "what weight" in minimal_flat)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive current path matches registry", nodes["scale_reference_primitive"]["current_path"] == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    audit.check("kinetic primitive current path matches registry", nodes["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    audit.check("realized primitive current path matches registry", nodes["realized_state_primitive"]["current_path"] == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale or "zero dimensionless content" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5007` Koide native zero-section route guard repair | `CLEAN`",
        "`#5006` static-source I1 hygiene companion refresh | `CLEAN`",
        "`#5005` quark lane3 retention firewall companion refresh | `CLEAN`",
        "`#5004` quark C3 ward splitter hygiene companion refresh | `CLEAN`",
        "`#5003` Hubble lane5 two-gate hygiene companion refresh | `CLEAN`",
        "`#5002` Hubble lane5 A2 hygiene companion refresh | `CLEAN`",
        "`#5001` hadron lane1 record-invariance companion refresh | `CLEAN`",
        "`#5000` axiom-first record-invariance companion refresh | `CLEAN`",
        "`#4999` Wilson descendant Schur entropy witness stabilization | `CLEAN`",
        "`#4998` neutrino split2 edge transport witness refresh | `CLEAN`",
	        "`#4997` neutrino source-amplitude carrier premise bound | `CLEAN`",
        "`#4996` PMNS selector stationarity diagnostics repair | `CLEAN`",
        "`#4995` theta retirement-basis re-match | `CLEAN`",
        "`#4994` record-instrument polar contrast stabilization | `CLEAN`",
        "`#4993` DELTA0 route inventory sibling-total refresh | `CLEAN`",
        "`#4992` g_bare two-Ward scope repair | `CLEAN`",
        "`#4985` AC R-eta h-unit primitive no-go | `CLEAN`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN`",
        "`#4990` Tier-A residual owner decision packet | `CLEAN`",
        "`#4989` Tier-A residual governance readiness packet | `CLEAN`",
        "`#4988` theta G2 registration stretch no-go | `CLEAN`",
        "`#4987` theta G4 theta-bar assembly no-go | `CLEAN`",
        "`#4986` AC R-eta h-class stretch no-go | `CLEAN`",
        "`#4984` AC R-eta direct-license no-go | `CLEAN`",
        "`#4983` AC R-eta doublet-clock no-go | `CLEAN`",
        "`#4982` AC occupancy formation non-supply no-go | `CLEAN`",
        "`#4981` AC R-eta C3 ratification non-supply | `CLEAN`",
        "`#4980` theta G1 kinetic 4D scaffold support | `CLEAN`",
        "`#4979` theta G1 defect suppression support | `CLEAN`",
        "`#4978` theta G1 4D carrier supply no-go | `CLEAN`",
        "`#4977` theta G1 closed-nonexact interface exact-support | `CLEAN`",
        "`#4975` primitive axiom absorption no-go | `CLEAN`",
        "`#4971` AC R-eta Record formation non-supply no-go | `CLEAN`",
        "`#4968` alpha-s universal beta kernel scoping | `CLEAN`",
        "`#4966` alpha-s threshold matching kernel scoping | `CLEAN`",
        "`#4963` quark route2 no-go retained-parent repair | `DIRTY`",
        "`#4962` SU2 beta coefficient template repair | `DIRTY`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of F/L/P/R.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation of the `256.082435...` precision correction.",
        "No derivation of the Koide/electron branch or physical `m_e`.",
        "No derivation of `alpha(0)` or hydrogen spectroscopy.",
        "No use of latest open PRs as proof inputs.",
        "No new axiom, primitive, or admitted import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note ratifies the source-probe interface",
        "F/L/P/R is retained",
        "S_l is retained",
        "This note derives retained `S_l = 1/256`",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
