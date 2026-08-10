#!/usr/bin/env python3
"""Emit the Cycle 973 26-row semantic-repair hand-off.

This is a pinned-object measurement and obligation map, not a row repair.  The
26 corpus blobs are read only with ``git show <literal-pin>:<path>``.  No
working-tree corpus file is an input, and this program edits no landed source,
axiom, primitive, ledger, or audit status.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import ast
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PINNED_SNAPSHOT_COMMIT = "323d7fc32d77598f74ea6cd4d30c38dda0fe5070"
PINNED_OBJECTS = {
    "snapshot_commit": PINNED_SNAPSHOT_COMMIT,
    "snapshot_tree": "45f8bd67eedaccb34918cb6804e850e1ba7f21fb",
    "docs_tree": "7dbc99ea9bb07250a72fff4722d37cdc1c573daf",
    "scripts_tree": "b74e1639fc2a2250c0de2a56ad33665533a22c81",
}
CYCLE971_PROVENANCE_COMMIT = "0c453230c6334d8a9c0569925a8f95d96509e2f4"
CYCLE971_PROVENANCE = (
    {
        "path": "scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py",
        "sha256": "6def914db02ae5cd6c4187a0fc20b11bd640bbb223cfce73ba2df7f675f4be63",
        "use": "text and AST provenance for the pinned census and MEANING_CHANGED set",
    },
    {
        "path": "docs/AXIOM_FIDELITY_REREAD_CYCLE971_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "sha256": "0258535aea69bc7091e1ff1bae84a822ea9d9d684b68941c00e0e9fef673aa39",
        "use": "text provenance for the old/new semantic boundary",
    },
    {
        "path": "outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json",
        "sha256": "c3c25de48b46f4aecf32b0e56a1a07275beec932bbb16eb3e16308d4fc7b8455",
        "use": "text provenance for the exact 26-path hand-off set",
    },
)

RECEIPT_PATH = ROOT / "outputs/axiom_edit_repair_map_cycle973_receipt_2026_08_09.json"
CACHE_PATH = ROOT / "logs/runner-cache/frontier_cycle973_repair_map_2026_08_09.txt"

DELTA_VOCABULARY = {
    "STRICTLY_WEAKER": (
        "The new-reading proposition is entailed by the old-reading proposition, "
        "and the converse fails on an allowed same-support weight-change model."
    ),
    "STRICTLY_STRONGER": (
        "The old-reading proposition is entailed by the new-reading proposition, "
        "and the converse fails; this occurs when a weaker distribution premise "
        "is asked to carry the same conditional selector conclusion."
    ),
    "ORTHOGONAL_RESTATEMENT": (
        "The readings predicate different typed objects or bridges and neither "
        "row proposition entails the other without an extra identification."
    ),
    "UNDERDETERMINED_BY_TEXT": (
        "The row mixes historical, supplied, or resolution-ambiguous readings, "
        "so its text does not determine one comparable old/new proposition."
    ),
}

BEARING_VOCABULARY = {
    "BEARS": (
        "Cycle 970/972 is a covariant unique-law countermodel to identifying "
        "state-resolved distribution dependence with marginal dependence or "
        "support variation; it informs this semantic delta but does not discharge "
        "the row-specific obligation."
    ),
    "SILENT": (
        "The Cycle 970/972 state-resolved/marginal separation has no logical role "
        "in the row's semantic delta."
    ),
}

FAMILIES = {
    "corpus_family": "tracked docs/ and scripts/ blobs at the literal snapshot pin",
    "row_family": "Cycle 971 MEANING_CHANGED paths only",
    "quote_family": "exact pinned source blocks or exact Python AST string constants",
    "delta_family": "the four closed-vocabulary relations in delta_vocabulary",
    "discharge_family": "one named smallest machine-checkable obligation per row; no obligation is attempted",
    "witness_family": (
        "Cycle 970 state-resolved 1/1 and marginal 0/0 construction, proved "
        "covariant and unique by Cycle 972"
    ),
}

CAPS = {
    "direct_authoring_provenance_file_cap": 6,
    "direct_authoring_provenance_files_declared": 3,
    "map_row_cap_exact": 26,
    "pinned_corpus_blob_reads_exact": 26,
    "working_tree_corpus_reads": 0,
    "snapshot_path_families": 2,
    "delta_vocabulary_size": 4,
    "witness_vocabulary_size": 2,
}


def spec(
    path: str,
    anchor: str,
    old: str,
    new: str,
    delta: str,
    obligation_id: str,
    obligation: str,
    *,
    quote_mode: str = "paragraph",
) -> dict[str, str]:
    return {
        "path": path,
        "quote_anchor": anchor,
        "quote_mode": quote_mode,
        "old_assertion": old,
        "new_assertion": new,
        "delta_class": delta,
        "obligation_id": obligation_id,
        "obligation": obligation,
        "witness_bearing": "BEARS",
    }


ROW_SPECS = (
    spec(
        "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md",
        'The Admissibility axiom supplies "one fixed nearest-neighbor admissibility',
        "The framework supplies a support-valued nearest-neighbor rule whose available-possibility set varies, and the note classifies proper-to-full cubic extensions of rule-value channels on named alphabets.",
        "The framework supplies a neighbor-conditioned probability distribution; the note's scalar/frame rule-value channels are not thereby identified with either that distribution or its support.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-DISTRIBUTION-RULE-CODOMAIN",
        "Encode each classified rule value as a normalized probability distribution and machine-check equivariance plus the asserted support/value projection.",
    ),
    spec(
        "docs/BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md",
        "the available possibilities",
        "The first available set and every later availability map are support sets; their proper/improper orbit behavior controls nonemptiness, chirality, and propagation closure.",
        "A probability distribution exists at each condition and varies state-resolved, but its support need not carry the note's chirality or propagation action.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-BOOTSTRAP-SUPPORT-LIFT",
        "Set A(c)=supp(mu_c) for the note's rule and rerun the nonemptiness, improper-orbit, and propagation-closure checks on A.",
    ),
    spec(
        "docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md",
        "site-local possibility domains with neighbor-dependent availability",
        "The minimal axioms supply neighbor-dependent one-site availability support but no pair-level domain or entangled-menu eligibility.",
        "The minimal axioms supply a neighbor-dependent one-site probability distribution and still no pair-level domain or entangled-menu eligibility; support dependence is no longer supplied.",
        "STRICTLY_WEAKER",
        "O973-COMPOSITE-SUPPORT-NONCONSTANCY",
        "Exhibit two allowed neighbor conditions whose one-site distribution supports differ, while separately preserving the note's stated absence of a pair-level menu.",
    ),
    spec(
        "docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "availability rule's content is indexed by nearest-neighbor adjacency",
        "A site's availability support is indexed by nearest-neighbor adjacency, so the availability rule is not a single-site-only object.",
        "A site's probability distribution is indexed by nearest-neighbor conditions; that is weaker than nonconstant support and does not itself supply a bonded-pair carrier.",
        "STRICTLY_WEAKER",
        "O973-BONDED-PAIR-SUPPORT-BRIDGE",
        "Machine-check that the positive support relevant to the bonded-pair construction changes with an adjacent condition and is the same support object consumed by T2.",
    ),
    spec(
        "docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md",
        "This rule is determined by the nearest-neighbor conditions",
        "The explicit set-valued rule changes available sets with neighbor records and therefore witnesses the old vary-with clause while leaving dynamics unforced.",
        "The same set-valued rule remains a model choice, while the landed axiom concerns a probability distribution that the row never defines; the support model and distribution assertion are unlinked typed statements.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-DYNAMICS-UNIFORM-SUPPORT-LIFT",
        "Define mu_c uniformly on every nonempty exhibited available set and check normalization, covariance, supp(mu_c)=A(c), and mu_c!=mu_c' for the displayed control conditions.",
    ),
    spec(
        "docs/FROZEN_REGION_RECORD_SATURATION_LOCAL_FINALITY_BOUNDARY_INFLUENCE_BOUNDED_NOTE_2026-07-03.md",
        "the axiom fixes the clause",
        "For the exhibited support-valued rule, permanence gives monotone support containment and cavity-only singleton pinning as neighbor records accumulate.",
        "The landed clause constrains a probability distribution, while the note's monotone-containment theorem remains about an independently exhibited support-valued rule.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-FROZEN-REGION-DISTRIBUTION-LIFT",
        "Construct a normalized mu_c with support exactly the exhibited union-over-recorded-neighbors set and rerun the boundary containment and cavity controls.",
    ),
    spec(
        "docs/KINETIC_ISOTROPY_3D_FACTORIZED_PROTOCOL_SELECTION_ON_ANALYZED_CLASSES_BOUNDED_THEOREM_NOTE_2026-07-09.md",
        "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.",
        "The quoted nonconstant-support clause motivates an all-axis nonvacuous factor-support filter, conditional on a protocol--Admissibility support realization.",
        "Distribution variation may occur at fixed factor support, so the landed clause and the note's factor-support predicate are different typed filters.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-PROTOCOL-DISTRIBUTION-REALIZATION",
        "Supply an explicit protocol-to-mu map and machine-check that the note's all-axis factor-support predicate is equivalent to the required state-resolved distribution variation on the named ten protocols.",
    ),
    spec(
        "docs/MATTER_REALIZATION_ARENA_SPLIT_PRESERVATION_UNDER_AXIS_COUPLED_FRAMES_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        '"For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."',
        "The current foundation is quoted as requiring neighbor-varying availability support alongside the independent exchange-split calculation.",
        "The current foundation requires neighbor-varying probability distributions; the exchange-split calculation is unchanged, but support variation is not supplied.",
        "STRICTLY_WEAKER",
        "O973-ARENA-SPLIT-SUPPORT-NONCONSTANCY",
        "Exhibit two neighbor conditions on the arena surface with different positive supports for the landed distributions.",
    ),
    spec(
        "docs/MATTER_REALIZATION_KS_HOP_BRIDGE_EDGE_DIAG_MEMBERSHIP_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        '"For each site, the available possibilities are determined by, and vary with,',
        "Neighbor-varying availability support is available as foundation context for edge/diagonal membership on the KS-hop bridge surface.",
        "Only the probability distribution must vary; edge/diagonal positive-support membership does not follow from that variation.",
        "STRICTLY_WEAKER",
        "O973-KS-EDGE-DIAG-POSITIVE-MASS",
        "Check that every edge/diagonal projector used by the bridge has positive mu_c mass at its stated condition and that the relevant supports change where claimed.",
    ),
    spec(
        "docs/MATTER_REALIZATION_QUBIT_LEVEL_CROSS_SITE_BILINEAR_FROM_K1_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "available possibilities are determined by, and vary with",
        "Nonconstant availability support excludes the neighbor-constant K0 support structure, allowing the licensed K1 cross-site bilinear construction.",
        "The same K1 conclusion would have to follow from the weaker fact that probabilities vary, even though K0 can vary weights on constant support.",
        "STRICTLY_STRONGER",
        "O973-K1-BILINEAR-DISTRIBUTION-SEPARATION",
        "Under an explicit kinetic-to-distribution bridge, exhaust the licensed K0 class and prove every mu_c is neighbor-constant while a K1 mu_c varies.",
    ),
    spec(
        "docs/PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md",
        "available possibilities are determined by, and vary with, the",
        "Neighbor-dependent availability support is used as carrier-level motivation for one-tick dependency-set support of each plaquette term.",
        "Neighbor-conditioned probabilities do not identify the carrier support of a term with the distribution's positive support or prove one-tick reachability.",
        "ORTHOGONAL_RESTATEMENT",
        "O973-PLAQUETTE-DEPENDENCY-SUPPORT-LIFT",
        "Machine-check that every term carrier lies in supp(mu_c) generated from its stated one-step dependency set and that this identification is covariant.",
    ),
    spec(
        "docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md",
        "It uses the exact axiom clauses",
        "K0 admits only neighbor-constant availability maps whereas K1 admits a neighbor-conditioned support map, so a realized record can discriminate the branches under the old variation premise.",
        "The same branch discrimination would have to follow from distribution variation, although K0's constant support can carry condition-dependent weights.",
        "STRICTLY_STRONGER",
        "O973-RECORD-KINETIC-DISTRIBUTION-SEPARATION",
        "Under the record/kinetic realization, prove all licensed K0 conditional distributions are identical across neighbor contents and construct one varying K1 distribution with record-eligible positive support.",
    ),
    spec(
        "docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md",
        "The one-bit residual is NOT decided here",
        "The residual asks whether availability support varies nonvacuously on the qubit factor, which would distinguish K1 from K0.",
        "The landed reading asks whether a probability distribution varies, but the row does not specify state-resolved versus marginal evaluation or a distribution-to-qubit-support map.",
        "UNDERDETERMINED_BY_TEXT",
        "O973-DISCRIMINATOR-RESOLUTION-SPEC",
        "Specify the conditioning state and marginalization map, then check whether mu variation is equivalent to nonconstant qubit-factor support on both licensed branches.",
    ),
    spec(
        "docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md",
        "The minimal axiom note now states the clarified Admissibility clause",
        "The load-bearing support-variation premise removes K0 and selects K1 on the licensed two-class surface.",
        "The same K1 selection would be asserted from the weaker premise that the distribution varies, which allows same-support weight changes on K0.",
        "STRICTLY_STRONGER",
        "O973-K1-DISTRIBUTION-SEPARATION",
        "Under a pinned kinetic-to-mu realization, prove K0 cannot realize any allowed state-resolved distribution change and K1 can, with the quantifiers covering the full licensed two-class surface.",
    ),
    spec(
        "docs/REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md",
        "selection here uses the current minimal-axiom Admissibility variation premise",
        "A support-variation K1 selector is transported as a class function over the licensed local-U(1) orbit.",
        "A distribution-variation selector would be transported over that orbit without text excluding same-support K0 weight variation, strengthening the conditional selection claim.",
        "STRICTLY_STRONGER",
        "O973-FRAME-ORBIT-DISTRIBUTION-SEPARATION",
        "For every licensed local-U(1) frame, prove the induced mu family is neighbor-constant on K0 and varying on K1, and verify the property is a frame-orbit class function.",
    ),
    spec(
        "docs/REALIZED_KINETIC_BRANCH_SELECTION_GAUGED_BACKGROUND_INVARIANCE_NARROW_THEOREM_NOTE_2026-07-02.md",
        "Therefore the clarified clause",
        "The support-variation selector remains K1-only under the tested fixed legal gauge backgrounds.",
        "The same K1-only conclusion would have to hold for distribution variation, which need not change support and is not fixed by the qubit-algebra gaps.",
        "STRICTLY_STRONGER",
        "O973-GAUGED-DISTRIBUTION-SEPARATION",
        "For every tested fixed background and both branches, construct the induced mu and verify K0 equality and K1 inequality across neighbor conditions after factor recovery.",
    ),
    spec(
        "docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
        "For at least one nontrivially varying neighbor condition",
        "A separately supplied bridge identifies varying available rank-one possibilities with nontrivial spectral projectors of F(c), yielding b!=0.",
        "The conditional bridge may mean support or weights under the landed distribution reading, and the text mentions both formation support and weights without fixing which varies.",
        "UNDERDETERMINED_BY_TEXT",
        "O973-SPECTRAL-SUPPORT-BRIDGE",
        "Specify mu_c and check supp(mu_c) equals the nontrivial spectral-projector set of F(c) at the witness conditions, with no appended response sector.",
    ),
    spec(
        "docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md",
        "The live memo adds Admissibility",
        "A declared set-valued admissibility instance makes P1 available and varies its available set with neighbor conditions; record eligibility is support membership.",
        "Availability is positive support of a probability distribution, but the row and runner mix a declared support rule with the landed distribution sentence without specifying probabilities.",
        "UNDERDETERMINED_BY_TEXT",
        "O973-ATOM-POSITIVE-MASS",
        "Define the declared mu_c and check P1 has positive mass at every claimed lock condition, supp(mu_c) equals the declared rule, and mu_c varies at the stated control.",
    ),
    spec(
        "docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md",
        "requires only that available possibilities vary with neighbor",
        "A countermodel has genuinely varying availability support yet does not select the first-order staggered law or eight-corner zero set.",
        "The same countermodel would refute selection from the weaker distribution-variation premise once a compatible distribution is supplied; distribution variation alone is easier to satisfy.",
        "STRICTLY_WEAKER",
        "O973-KINETIC-COUNTERMODEL-DISTRIBUTION",
        "Extend the exact countermodel with a normalized covariant mu_c satisfying the landed state-resolved variation sentence and rerun the unchanged kinetic/corner falsifier.",
    ),
    spec(
        "docs/THETA_DEFECT_CLOSURE_FROM_ADMISSIBILITY_TEST_BOUNDED_NOTE_2026-07-03.md",
        "nearest-neighbor single-valued availability",
        "An explicit neighbor-varying single-valued availability encoding does not force dn=0 on the scoped finite branch complex.",
        "A probability-distribution encoding satisfying the weaker landed variation premise would likewise fail to force dn=0 if lifted from the same support witness.",
        "STRICTLY_WEAKER",
        "O973-THETA-COUNTERMODEL-DISTRIBUTION",
        "Attach normalized distributions to every encoded condition with support equal to the exhibited availability set and rerun the dn!=0 witness.",
    ),
    spec(
        "docs/TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md",
        "identifies nonvacuous variation of available",
        "Under a supplied bridge, nonconstant availability support is identified with nonzero off-site tick support and selects the two mover families.",
        "The same mover selection would have to follow from distribution variation, including same-support state-resolved weight changes whose uniform marginal can be constant.",
        "STRICTLY_STRONGER",
        "O973-TICK-DISTRIBUTION-BRIDGE",
        "Define the tick-induced conditional mu, state its marginalization, and exhaustively verify that landed distribution variation is equivalent to nonzero off-site tick support on the licensed period-2 family.",
    ),
    spec(
        "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
        "Admissibility already says available",
        "Unrecorded sites may have alternative available support, and Admissibility makes that support depend on nearest-neighbor conditions without supplying dynamics.",
        "Unrecorded sites have a probability distribution whose support defines availability, but only the distribution must depend on neighbors; the text does not resolve how many positive-mass alternatives or which marginal is meant.",
        "UNDERDETERMINED_BY_TEXT",
        "O973-FORTRESS-OPEN-SITE-SUPPORT",
        "At the exact fortress conditions, compute mu_c and verify at least two positive-mass unrecorded alternatives plus the declared state-resolved/marginal dependence behavior.",
    ),
    spec(
        "docs/work_history/repo/review_feedback/TWELVE_HOUR_TOE_FRAMEWORK_CAMPAIGN_DIAGNOSIS_2026-07-16.md",
        "Admissibility makes their availability depend on",
        "Admissibility makes availability support depend on neighbor conditions but supplies no actual evolving unrecorded-site possibility.",
        "Admissibility makes the probability distribution depend on neighbor conditions and still supplies no actual evolving possibility; the support-dependence part is dropped.",
        "STRICTLY_WEAKER",
        "O973-DIAGNOSIS-DISTRIBUTION-NONDYNAMICS",
        "Machine-check a neighbor-conditioned mu on the cited architecture and separately verify that no transition/update or evolving-site-state map is present in the supplied law fields.",
    ),
    spec(
        "scripts/frontier_record_local_finite_atom_availability_2026_06_17.py",
        "A4 live Admissibility axiom requires neighbor-varying availability",
        "The runner labels its axiom guard as neighbor-varying availability and tests a set-valued R_varying support control.",
        "The guard string matches the landed distribution sentence, but the executable control varies only a set and never constructs a probability distribution, leaving the tested proposition ambiguous.",
        "UNDERDETERMINED_BY_TEXT",
        "O973-RUNNER-ATOM-DISTRIBUTION-CONTROL",
        "Add an independent mu_c construction whose support is R_varying and assert normalization, positive-mass atom eligibility, and state-resolved inequality at the AD4 conditions.",
        quote_mode="ast_string",
    ),
    spec(
        "scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py",
        "clarified Admissibility variation selects K1 on the licensed two-class surface",
        "The executable selector requires support variation and therefore returns only K1.",
        "The same selector label would claim K1-only selection from distribution variation, though K0 constant support can carry condition-dependent weights.",
        "STRICTLY_STRONGER",
        "O973-RUNNER-K1-DISTRIBUTION-SEPARATION",
        "Enumerate the induced conditional distributions for every licensed K0/K1 representative and assert K0 equality, K1 inequality, normalization, and the declared conditioning resolution.",
        quote_mode="ast_string",
    ),
    spec(
        "scripts/realized_kinetic_branch_selection_gauged_background_invariance_2026_07_02.py",
        "clarified Admissibility variation still selects K1 for every fixed legal background tested",
        "The executable fixed-background selector preserves K1-only support variation under the tested factorized gauge actions.",
        "The same test label would infer K1-only selection from distribution variation without excluding same-support K0 weight changes.",
        "STRICTLY_STRONGER",
        "O973-RUNNER-GAUGED-DISTRIBUTION-SEPARATION",
        "For every listed background seed, construct the branch-conditioned mu family and assert K0 equality and K1 inequality across the exact neighbor controls after factor recovery.",
        quote_mode="ast_string",
    ),
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ("git", *args), cwd=ROOT, check=True, capture_output=True
    ).stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", errors="replace")


def exact_sentence(text: str, anchor: str) -> dict:
    position = text.find(anchor)
    if position < 0:
        raise AssertionError(f"quote anchor absent: {anchor!r}")
    paragraph_start = text.rfind("\n\n", 0, position)
    paragraph_start = 0 if paragraph_start < 0 else paragraph_start + 2
    paragraph_end = text.find("\n\n", position)
    paragraph_end = len(text) if paragraph_end < 0 else paragraph_end
    paragraph = text[paragraph_start:paragraph_end].rstrip("\n")
    local_anchor = position - paragraph_start
    boundaries = list(re.finditer(
        r"(?:[.!?][\"'”’]?|;)(?:\s+)(?=(?:[-*#>`]|[A-Z0-9]))",
        paragraph,
    ))
    local_start = 0
    for boundary in boundaries:
        if boundary.end() <= local_anchor:
            local_start = boundary.end()
    local_end = len(paragraph)
    for boundary in boundaries:
        if boundary.start() >= local_anchor:
            local_end = boundary.start() + 1
            if paragraph[boundary.start() + 1:boundary.end()].lstrip().startswith(('"', "'", "”", "’")):
                local_end += 1
            break
    start = paragraph_start + local_start
    block = paragraph[local_start:local_end].strip()
    leading_trim = len(paragraph[local_start:local_end]) - len(paragraph[local_start:local_end].lstrip())
    start += leading_trim
    return {
        "line_start": text.count("\n", 0, start) + 1,
        "line_end": text.count("\n", 0, start + len(block)) + 1,
        "exact_quoted_source_block": block,
        "quote_extraction": "punctuation-bounded exact raw source sentence containing the literal anchor",
    }


def exact_ast_string(text: str, anchor: str, path: str) -> dict:
    tree = ast.parse(text, filename=path)
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and anchor in node.value
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one AST string for {path}:{anchor!r}; got {len(matches)}")
    node = matches[0]
    return {
        "line_start": node.lineno,
        "line_end": getattr(node, "end_lineno", node.lineno),
        "exact_quoted_source_block": node.value,
        "quote_extraction": "exact Python AST string-constant value containing the literal anchor",
    }


def pinned_object_report() -> dict[str, str]:
    actual = {
        "snapshot_commit": git_text("rev-parse", PINNED_SNAPSHOT_COMMIT).strip(),
        "snapshot_tree": git_text("rev-parse", f"{PINNED_SNAPSHOT_COMMIT}^{{tree}}").strip(),
        "docs_tree": git_text("rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:docs").strip(),
        "scripts_tree": git_text("rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:scripts").strip(),
    }
    if actual != PINNED_OBJECTS:
        raise AssertionError(f"pinned object mismatch: expected={PINNED_OBJECTS} actual={actual}")
    return actual


def build_rows() -> list[dict]:
    rows = []
    seen: set[str] = set()
    for item in ROW_SPECS:
        path = item["path"]
        if path in seen:
            raise AssertionError(f"duplicate row path: {path}")
        seen.add(path)
        body_bytes = git_bytes("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")
        body = body_bytes.decode("utf-8", errors="replace")
        quote = (
            exact_ast_string(body, item["quote_anchor"], path)
            if item["quote_mode"] == "ast_string"
            else exact_sentence(body, item["quote_anchor"])
        )
        rows.append({
            "path": path,
            "pinned_blob": git_text("rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:{path}").strip(),
            "pinned_blob_sha256": sha256(body_bytes).hexdigest(),
            "quoted_old_semantics_consumption": quote,
            "what_the_row_asserts_under_old_availability_reading": item["old_assertion"],
            "what_the_same_text_asserts_under_landed_distribution_reading": item["new_assertion"],
            "delta_class": item["delta_class"],
            "minimal_discharge": {
                "obligation_id": item["obligation_id"],
                "smallest_machine_checkable_fact": item["obligation"],
                "attempted_here": False,
            },
            "cycle970_972_witness": item["witness_bearing"],
            "cycle970_972_bearing_reason": BEARING_VOCABULARY[item["witness_bearing"]],
        })
    return rows


def main() -> int:
    objects = pinned_object_report()
    rows = build_rows()
    classes = Counter(row["delta_class"] for row in rows)
    bearings = Counter(row["cycle970_972_witness"] for row in rows)
    paths = [row["path"] for row in rows]

    integrity = {
        "literal_snapshot_objects_match": objects == PINNED_OBJECTS,
        "row_count_is_task_contract_26": len(rows) == CAPS["map_row_cap_exact"],
        "row_paths_unique_and_sorted": len(paths) == len(set(paths)) and paths == sorted(paths),
        "all_quotes_nonempty_and_pinned": all(
            row["quoted_old_semantics_consumption"]["exact_quoted_source_block"]
            and row["pinned_blob"]
            and row["pinned_blob_sha256"]
            for row in rows
        ),
        "closed_delta_vocabulary": set(classes) <= set(DELTA_VOCABULARY),
        "closed_witness_vocabulary": set(bearings) <= set(BEARING_VOCABULARY),
        "all_obligations_named_and_unattempted": all(
            row["minimal_discharge"]["obligation_id"].startswith("O973-")
            and not row["minimal_discharge"]["attempted_here"]
            for row in rows
        ),
    }
    if not all(integrity.values()):
        raise AssertionError(f"integrity failure: {integrity}")

    receipt = {
        "artifact": "Cycle 973 bounded 26-row repair map hand-off",
        "claim_type": "meta",
        "actual_current_surface_status": "bounded-support",
        "audit_status_authority": "independent audit lane only",
        "measurement_only": True,
        "repairs_attempted": 0,
        "status_verdicts_authored": 0,
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "pinned_objects": objects,
        "cycle971_text_ast_provenance_commit": CYCLE971_PROVENANCE_COMMIT,
        "cycle971_text_ast_provenance": list(CYCLE971_PROVENANCE),
        "families": FAMILIES,
        "caps": CAPS,
        "delta_vocabulary": DELTA_VOCABULARY,
        "bearing_vocabulary": BEARING_VOCABULARY,
        "row_count": len(rows),
        "delta_class_histogram": dict(sorted(classes.items())),
        "witness_bearing_counts": dict(sorted(bearings.items())),
        "meaning_changed_path_digest": digest(paths),
        "rows": rows,
        "integrity": integrity,
    }
    receipt["map_digest"] = digest({
        "pin": PINNED_SNAPSHOT_COMMIT,
        "vocabulary": DELTA_VOCABULARY,
        "rows": rows,
    })

    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    RECEIPT_PATH.write_text(rendered, encoding="utf-8")
    cache_lines = [
        f"PASS A_PINNED_SNAPSHOT :: commit={PINNED_SNAPSHOT_COMMIT}; objects={compact(objects)}; working_tree_corpus_reads=0",
        f"PASS B_EXACT_ROW_SET :: rows={len(rows)}; path_digest={receipt['meaning_changed_path_digest']}; paths_sorted_unique=True",
        f"PASS C_EXACT_QUOTES_AND_OBLIGATIONS :: exact_quotes={len(rows)}; named_unattempted_obligations={len(rows)}; pinned_blob_reads={len(rows)}",
        f"PASS D_CLOSED_MAP :: delta_histogram={compact(dict(sorted(classes.items())))}; witness_counts={compact(dict(sorted(bearings.items())))}; map_digest={receipt['map_digest']}",
        "VERDICT: CYCLE973_26_ROW_REPAIR_MAP_EMITTED",
        "TOTAL: PASS=4 FAIL=0",
    ]
    cache = "\n".join(cache_lines) + "\n"
    CACHE_PATH.write_text(cache, encoding="utf-8")
    print(cache, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
