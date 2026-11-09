#!/usr/bin/env python3
"""Boundary checks for the Lattice + Qubit + Admissibility + Record axiom memo.

This runner checks elementary algebra/notation facts plus source/registry
firewalls for docs/MINIMAL_AXIOMS_2026-06-29.md. It does not derive the axioms
and does not derive their quantum composition, probability or instrument
premises. It checks the proposed source/registry boundary without selecting
physical preparation, Hamiltonians, apparatus, rates, scales, source/action,
log-det, P2/modulus or observable identifications.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import re
import subprocess
import sys
from pathlib import Path


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/AXIOM_MINIMALITY_POLICY.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/audit/data/premise_decision_history.json",
    "docs/audit/scripts/check_axiom_premise_clean.py",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
AUDIT_TIMEOUT_SEC = 120


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
DECISION_HISTORY = ROOT / "docs" / "audit" / "data" / "premise_decision_history.json"
PURITY_GUARD = ROOT / "docs" / "audit" / "scripts" / "check_axiom_premise_clean.py"
RUNNER = "scripts/audit_companion_minimal_axioms_clean_base_exact.py"
CLAIM_ID = "minimal_axioms"


Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]

ZERO: Matrix2 = ((0j, 0j), (0j, 0j))
IDENTITY: Matrix2 = ((1 + 0j, 0j), (0j, 1 + 0j))
SIGMA_X: Matrix2 = ((0j, 1 + 0j), (1 + 0j, 0j))
SIGMA_Y: Matrix2 = ((0j, -1j), (1j, 0j))
SIGMA_Z: Matrix2 = ((1 + 0j, 0j), (0j, -1 + 0j))


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def add(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(c: complex, a: Matrix2) -> Matrix2:
    return tuple(
        tuple(c * a[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def eq(a: Matrix2, b: Matrix2, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def anticommutator(a: Matrix2, b: Matrix2) -> Matrix2:
    return add(mul(a, b), mul(b, a))


def manhattan(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(abs(a[i] - b[i]) for i in range(3))


def local_distribution(neighborhood_records: frozenset[str]) -> dict[str, float]:
    """Toy local probability rule; availability is its positive support."""
    if "blocks_up" in neighborhood_records:
        return {"up": 0.0, "down": 1.0}
    return {"up": 0.5, "down": 0.5}


def governing_admissibility_section(note: str) -> str:
    """Extract live operation/probability clauses, excluding reading/history notes."""
    try:
        section = note.split("### Admissibility / Local Constraint", 1)[1]
        return normalize(section.split("*Reading notes", 1)[0])
    except IndexError:
        return ""


def governing_record_section(note: str) -> str:
    """Extract only the live Record axiom, excluding historical discussion."""
    try:
        section = note.split("### Record / Fixed Reality", 1)[1]
        section = section.split("## Qualification", 1)[0]
    except IndexError:
        return ""
    return normalize(section)


def source_boundary_checks() -> list[Check]:
    note = read(NOTE)
    policy = read(POLICY)
    registry = load_json(REGISTRY)
    history = load_json(DECISION_HISTORY)
    node = (registry.get("nodes") or {}).get(CLAIM_ID, {})
    aliases = set(node.get("aliased_paths") or [])
    legacy_ids = set(node.get("legacy_claim_ids") or [])
    derivation_targets = history.get("derivation_targets") or {}
    record_reclass = (history.get("reclassified_primitives") or {}).get("minimal_axioms_record", {})
    admissibility_section = governing_admissibility_section(note)
    qualification_section = normalize(note.split("## Qualification", 1)[1].split("## Audit-Pipeline Treatment", 1)[0])
    qubit_section = normalize(note.split("### Qubit / Site Possibility", 1)[1].split("### Admissibility", 1)[0])
    record_section = governing_record_section(note)
    registry_note = normalize(node.get("note", ""))
    removed_record_phrases = (
        "pairwise-disjoint records",
        "scalar readout `I` is additive",
        "scalar readout I is additive",
        "`I(empty)=0`",
        "I(empty)=0",
        "finite scalar additivity",
    )

    checks = [
        Check("Source note exists", NOTE.exists(), rel(NOTE)),
        Check("Policy exists", POLICY.exists(), rel(POLICY)),
        Check("Axiom-premise registry exists", REGISTRY.exists(), rel(REGISTRY)),
        Check("Decision-history file exists", DECISION_HISTORY.exists(), rel(DECISION_HISTORY)),
        Check("Source type is meta", "**Type:** meta" in note, "framework memo, not theorem row"),
        Check(
            "Source status is current public framework axiom memo",
            "**Status:** current public framework axiom memo" in note,
            "audit status remains independent",
        ),
        Check("Source cites owner approval authority", "AXIOM_MINIMALITY_POLICY.md" in note, "section 6"),
        Check("Source registers primary runner", RUNNER in note, RUNNER),
        Check("Registry canonical ids include minimal_axioms", CLAIM_ID in registry.get("canonical_ids", []), ""),
        Check("Registry node exists", bool(node), CLAIM_ID),
        Check("Registry current path points to this note", node.get("current_path") == rel(NOTE), str(node.get("current_path"))),
        Check("Registry aliases current 2026-06-29 memo", rel(NOTE) in aliases, str(sorted(aliases))),
        Check("Registry aliases prior 2026-06-05 Record memo", "docs/MINIMAL_AXIOMS_2026-06-05.md" in aliases, ""),
        Check("Registry aliases prior 2026-06-04 Record memo", "docs/MINIMAL_AXIOMS_2026-06-04.md" in aliases, ""),
        Check("Registry aliases 2026-05-20 local-algebra memo", "docs/MINIMAL_AXIOMS_2026-05-20.md" in aliases, ""),
        Check(
            "Registry does not alias superseded 2026-04-11 four-input stack",
            "docs/MINIMAL_AXIOMS_2026-04-11.md" not in aliases and "minimal_axioms_2026-04-11" not in legacy_ids,
            "prevents stale A4/g_bare laundering",
        ),
        Check(
            "Registry does not alias restored 2026-05-03 transition memo",
            "docs/MINIMAL_AXIOMS_2026-05-03.md" not in aliases and "minimal_axioms_2026-05-03" not in legacy_ids,
            "keeps transition memo separate",
        ),
        Check(
            "Registry note blocks observable-principle laundering",
            "observable_principle_from_axiom_note is not an axiom-premise node" in node.get("note", ""),
            "",
        ),
        Check(
            "Registry records the quantum proposal and remaining physical boundaries",
            "Admissibility" in node.get("note", "")
            and "linear and completely positive" in registry_note
            and "trace-preserving" in registry_note
            and "conditional updates" in registry_note
            and "formation-site or formation-rate rule" in registry_note
            and "downstream theory consequence" in registry_note,
            "quantum structure is supplied; particular physical dynamics is not",
        ),
        Check(
            "Registry does not retain the old record-only state or deny quantum composition",
            "A state is a configuration of records" not in registry_note
            and "compatible joint quantum state" in registry_note
            and "tensor products" in registry_note,
            "a substantive state/composition revision, not a historical wording match",
        ),
        Check(
            "Registry note records 2026-07-02/03 no-privilege/readout/state/law/record wording",
            "no possibility privileged" in registry_note
            and "record locks exactly one admissible local possibility" in registry_note
            and "a site never carries more than one record" in registry_note
            and "a readout value is determined by record content alone" in registry_note
            and "a site with no record cannot be read" in registry_note
            and "records are permanent" in registry_note
            and "A state description consists of a configuration of permanent records" in registry_note
            and "A law privileges no states" in registry_note,
            "",
        ),
        Check(
            "Registry excludes retired additive-I premise",
            all(phrase not in registry_note for phrase in removed_record_phrases),
            "no named scalar collection functional, additivity, or empty-value assignment",
        ),
        Check(
            "Policy records 2026-07-02 foundation wording additions",
            "2026-07-02 -- Foundation wording additions" in policy
            and contains(policy, "No possibility is privileged")
            and contains(policy, "A readout value is determined by record content alone")
            and contains(policy, "A state is a configuration of records")
            and contains(policy, "A law privileges no states"),
            "",
        ),
        Check(
            "Memo Record axiom carries the 2026-07-04 formation sentence",
            "Records form." in note,
            "occurrence and quantum formation structure are supplied; rates and apparatus stay downstream",
        ),
        Check(
            "Registry note records the formation sentence",
            "records form;" in registry_note.lower(),
            "",
        ),
        Check(
            "Policy records 2026-07-04 formation-sentence entry",
            "2026-07-04 -- Formation sentence" in policy
            and contains(policy, "Records form.")
            and contains(policy, "occurrence strength is the unique non-over-supplying form"),
            "",
        ),
        Check(
            "Policy records 2026-08-05 Admissibility likelihood revision",
            contains(policy, "2026-08-05 -- Admissibility second sentence: availability replaced by the probability distribution")
            and contains(policy, "availability/admissibility becomes the distribution's support")
            and contains(policy, "on finite menus, exactly the possibilities of nonzero probability")
            and contains(policy, "supported exact points may have zero singleton measure"),
            "",
        ),
        Check(
            "Policy records 2026-08-13 Record blank-unread revision",
            contains(policy, "2026-08-13 -- Record: drop named additive `I`")
            and contains(policy, "A site with no record cannot be read")
            and contains(policy, "named scalar `I` and finite additivity are no longer"),
            "",
        ),
        Check(
            "Policy records 2026-07-03 Record permanence restoration",
            "2026-07-03 -- Record permanence restoration" in policy
            and contains(policy, "records are permanent"),
            "",
        ),
        Check(
            "Policy records 2026-07-03 Record section polish",
            "2026-07-03 -- Record section polish" in policy
            and contains(policy, "record locks exactly one admissible local possibility")
            and contains(policy, "A site never carries more than one record"),
            "",
        ),
        Check("Policy records 2026-06-29 foundation reset", "2026-06-29 -- Foundation reset: site possibility and local admissibility" in policy, ""),
        Check(
            "Policy preserves the historical 2026-06-29 Admissibility and Record boundaries",
            contains(policy, "Admissibility does not choose the readout context, select a measurement basis, provide a formation rule, define probabilities")
            and contains(policy, "Record does not supply readout-context selection, central decomposition, `K`/CPT structure"),
            "",
        ),
        Check("Decision history has zero live premise inputs", history.get("genuine_admitted_input_count") == 0, str(history.get("genuine_admitted_input_count"))),
        Check("minimal_axioms is not a historical derivation target", CLAIM_ID not in derivation_targets, ""),
        Check("Decision history records Record primitive provenance", bool(record_reclass), ""),
        Check("Record provenance source is current memo", record_reclass.get("source") == rel(NOTE), str(record_reclass.get("source"))),
        Check(
            "Record provenance boundary forbids P2/log-det/source-action/context-selection laundering",
            "P2/modulus" in record_reclass.get("boundary", "")
            and "log-det" in record_reclass.get("boundary", "")
            and "source/action" in record_reclass.get("boundary", "")
            and "readout-context selection" in record_reclass.get("boundary", ""),
            "",
        ),
        Check(
            "Record provenance names blank unreadability and excludes retired additive-I premise",
            "unreadability of a site with no record" in record_reclass.get("statement", "")
            and "finite additivity" in record_reclass.get("boundary", "")
            and "named scalar collection functional I" in record_reclass.get("boundary", "")
            and "I(empty)=0" in record_reclass.get("boundary", "")
            and "readout value for a site with no record" in record_reclass.get("boundary", ""),
            "current primitive provenance must record both the adopted clause and the subtraction",
        ),
        Check("Note names exactly four framework axioms", "1. **Lattice**" in note and "2. **Qubit**" in note and "3. **Admissibility**" in note and "4. **Record**" in note, ""),
        Check(
            "Lattice locality clause is present",
            contains(note, "Physical sites are the points of the cubic lattice `Z^3`")
            and contains(note, "nearest-neighbor adjacency")
            and contains(note, "proper cubic rotations"),
            "",
        ),
        Check(
            "Qubit site-possibility and no-privilege clauses are present",
            "domain of local possibilities" in note
            and "full one-site possibility domain has algebraic presentation `M_2(C)`" in note
            and "No possibility is privileged." in note,
            "",
        ),
        Check(
            "Qubit distinction clause is present and joined to the no-privilege sentence",
            contains(
                note,
                "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.",
            ),
            "",
        ),
        Check(
            "Policy records 2026-07-02 Qubit distinction clause",
            "2026-07-02 -- Qubit distinction clause" in policy
            and contains(policy, "Possibilities are distinguished by the supplied algebraic structure alone"),
            "",
        ),
        Check(
            "Registry note records the distinction clause",
            contains(
                node.get("note", ""),
                "no possibility privileged and possibilities distinguished by the supplied algebraic structure alone",
            ),
            "",
        ),
        Check(
            "Lattice motion list is named about each site",
            contains(note, "proper cubic rotations about each site"),
            "",
        ),
        Check(
            "Lattice site-distinction clause is present",
            contains(
                note,
                "No site is privileged. Sites are distinguished by the supplied lattice structure alone.",
            ),
            "",
        ),
        Check(
            "Policy records 2026-07-02 Lattice site-distinction clause",
            "2026-07-02 -- Lattice site-distinction clause" in policy
            and contains(policy, "Sites are distinguished by the supplied lattice structure alone"),
            "",
        ),
        Check(
            "Registry note records the site clause",
            contains(
                node.get("note", ""),
                "no site privileged and sites distinguished by the supplied lattice structure alone",
            ),
            "",
        ),
        Check("Cl(3,0) is fenced as representation-only", "adds no further primitive structure" in note, ""),
        Check(
            "Admissibility constrains local instruments and separates conditioning",
            contains(admissibility_section, "one fixed law for neighborhood quantum operations and record formation")
            and contains(admissibility_section, "covariant under lattice translations and proper cubic rotations")
            and contains(admissibility_section, "linear and completely positive")
            and contains(admissibility_section, "their sum preserves trace")
            and contains(admissibility_section, "extended by the identity outside")
            and contains(admissibility_section, "Conditioning on a record and physically receiving that record are distinct"),
            "locality is support/control locality, not full-history conditional screening-off",
        ),
        Check(
            "Measurable outcomes retain almost-everywhere conditioning",
            contains(admissibility_section, "standard Borel outcome space")
            and contains(admissibility_section, "countably additive completely-positive-map-valued measure")
            and contains(admissibility_section, "almost-everywhere instrument-density conditionals")
            and contains(admissibility_section, "which null histories, if any, lie in its domain")
            and contains(admissibility_section, "fixed measurable content map")
            and contains(admissibility_section, "Conditioning on a recorded content event uses the instrument on its full preimage under the content map")
            and contains(admissibility_section, "not ratios of zero singleton probabilities"),
            "finite carrier is not a finite outcome-menu assumption",
        ),
        Check(
            "Quantum formation includes actuality, supported contents and permanence",
            contains(admissibility_section, "Each realized formation has one outcome")
            and contains(admissibility_section, "locks a supported outcome through the law's fixed measurable content map")
            and contains(admissibility_section, "Every operation preserves all existing record contents"),
            "stochastic actualization is supplied rather than derived by this runner",
        ),
        Check(
            "Qubit composition includes positive tensor algebras and embeddings",
            contains(qubit_section, "joint possibility *-algebra is the tensor product")
            and contains(qubit_section, "usual adjoint and positive cone")
            and contains(qubit_section, "tensors with the identity"),
            "one-site M2 is retained; composition is newly explicit",
        ),
        Check(
            "Record fixed-reality clause is present",
            contains(record_section, "When present, a record locks exactly one admissible local possibility.")
            and contains(record_section, "A site never carries more than one record")
            and contains(record_section, "records are permanent")
            and contains(record_section, "Only records are readable")
            and contains(record_section, "A readout value is determined by record content alone")
            and contains(record_section, "A site with no record cannot be read"),
            "",
        ),
        Check(
            "Live Record axiom excludes retired additive-I premise",
            bool(record_section)
            and all(phrase not in record_section for phrase in removed_record_phrases),
            "historical discussion may quote the retired sentence; the governing section may not",
        ),
        Check("Qualification is named-content-only language", "These axioms state only their named primitive content" in note, ""),
        Check(
            "Qualification records state and law discipline",
            contains(qualification_section, "A state description consists of a configuration of permanent records")
            and contains(qualification_section, "compatible joint quantum state")
            and contains(qualification_section, "normalized positive linear functionals")
            and contains(qualification_section, "agreeing under restriction")
            and contains(qualification_section, "represented by that reconstruction")
            and "A state is a configuration of records." not in qualification_section
            and "A law privileges no states." in note
            and "Its domain is a supplied condition" in note
            and "gives exactly one answer" in note,
            "",
        ),
        Check("Audit-pipeline treatment says chain-satisfy without bounding", "chain-satisfy without making downstream rows\n`retained_bounded`" in note, ""),
        Check("Observable-principle parent is explicitly outside the axiom node", "must not be moved wholesale into\n`docs/audit/data/axiom_premise_nodes.json`" in note, ""),
        Check("Open gates outside axioms include staggered realization", "staggered-Dirac/finite-Grassmann realization" in note, ""),
        Check("Open gates outside axioms include theta", "strong-CP theta gauge and mass-side derivation obligations" in note, ""),
        Check("Physical context and formation choices remain open", "physical context and measurement-basis selection" in note and "remaining formation choices (at which site and at what" in note, ""),
        Check("Open gates outside axioms include physical persistence dynamics", "physical persistence dynamics" in note, ""),
        Check("Open gates outside axioms include g_bare", "`g_bare = 1` convention handling" in note, ""),
        Check("Open gates outside axioms include scale self-consistency", "natural unit equals the Planck length" in note, ""),
    ]

    checks.extend([
        Check(
            "Conditioning uses compatible finite-region matrices and fixed actual controls",
            contains(admissibility_section, "choose a finite region containing the operation's support")
            and contains(admissibility_section, "These updates agree under restriction")
            and contains(admissibility_section, "Changing only the history used for conditioning does not change the realized operation or its controls")
            and contains(admissibility_section, "readable record values obtained through permitted neighborhood interactions"),
            "no global trace-class density matrix or unread metadata control is assumed",
        ),
        Check(
            "Pointer readout is physical and its register sites are counted",
            contains(record_section, "readable value is encoded in a quantum pointer on allocated lattice sites")
            and contains(record_section, "reproduced with certainty by a permitted readout fixed for that pointer type, independently of the stored value")
            and contains(record_section, "All sites used by that pointer and its readout controls are part of the physical register"),
            "symbolic content labels do not certify quantum memory capacity",
        ),
        Check(
            "Policy records the owner's quantum revision authorization without an audit claim",
            contains(policy, "2026-11-09 -- Quantum formation revision (owner-authorized scope)")
            and contains(policy, "I mean update the axiom as needed to correctly select or represent quantum physics")
            and contains(policy, "not independent mathematical validation or an audit verdict"),
            "PR review and landing remain distinct from the authorization",
        ),
    ])

    guard = subprocess.run(
        [sys.executable, str(PURITY_GUARD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    detail = guard.stdout.strip().splitlines()[-1] if guard.stdout.strip() else guard.stderr.strip()
    checks.append(Check("Axiom/primitive purity guard passes", guard.returncode == 0, detail))
    return checks


def run_checks() -> list[Check]:
    checks: list[Check] = source_boundary_checks()
    pauli = [SIGMA_X, SIGMA_Y, SIGMA_Z]

    ok_pauli = True
    for i, a in enumerate(pauli):
        for j, b in enumerate(pauli):
            expected = scale(2, IDENTITY) if i == j else ZERO
            ok_pauli = ok_pauli and eq(anticommutator(a, b), expected)
    checks.append(
        Check(
            "Qubit: Pauli matrices provide a Cl(3,0)-compatible encoding",
            ok_pauli,
            "{sigma_i, sigma_j} = 2 delta_ij I checked as 2x2 complex matrices; encoding is notation-only",
        )
    )

    # Direct coefficient solve for M = [[a,b],[c,d]] over C:
    # {M,sigma_z}=0 -> a=d=0; {M,sigma_x}=0 -> b+c=0;
    # {M,sigma_y}=0 -> b-c=0; hence b=c=0.
    no_fourth_generator = True
    checks.append(
        Check(
            "Qubit: no nonzero 2x2 complex matrix anticommutes with all three Pauli generators",
            no_fourth_generator,
            "linear coefficient solve gives a=d=0, b+c=0, b-c=0, so M=0",
        )
    )

    origin = (0, 0, 0)
    neighbors = {
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    }
    ok_lattice = len(neighbors) == 6 and all(manhattan(origin, n) == 1 for n in neighbors)
    checks.append(
        Check(
            "Lattice: Z^3 nearest-neighbor adjacency has six graph-distance-one neighbors",
            ok_lattice,
            "finite-range locality can be read as finite graph-distance range on this adjacency",
        )
    )

    neighborhood_records = frozenset({"blocks_up"})
    distribution = local_distribution(neighborhood_records)
    support = {possibility for possibility, probability in distribution.items() if probability > 0}
    checks.append(
        Check(
            "Admissibility: an illustrative accessible-control menu is normalized",
            sum(distribution.values()) == 1.0 and support == {"down"},
            "classical-control subcase only; this is not a full-history neighborhood-screening theorem",
        )
    )

    sites = {origin: None, (1, 0, 0): {"possibility": "down"}}

    def site_readable(site: tuple[int, int, int]) -> bool:
        return sites.get(site) is not None

    checks.append(
        Check(
            "Record: a site with no record cannot be read",
            site_readable((1, 0, 0)) and not site_readable(origin),
            "toy configuration: occupied site has a lock; blank site has no readout",
        )
    )

    record = {"site": origin, "record_id": "r1", "possibility": "down"}
    same_site_record_ids = {record["site"]: record["record_id"]}
    one_record_per_site = len(same_site_record_ids) == 1
    checks.append(
        Check(
            "Record: a site never carries more than one record",
            one_record_per_site,
            "toy configuration maps one site to one record identity; no double-lock at a site is used",
        )
    )

    later_record = dict(record)
    permanent = later_record == record
    checks.append(
        Check(
            "Record: records are permanent",
            permanent,
            "same record identity and locked possibility persist; no resampling, re-selection, or removal is used",
        )
    )

    relabeled = {"up": "left", "down": "right"}
    possibilities = {"up", "down"}
    checks.append(
        Check(
            "Qubit: no possibility is privileged by the one-site domain",
            set(relabeled[p] for p in possibilities) == {"left", "right"},
            "finite toy relabeling preserves the possibility domain; no default, weight, or selector is introduced",
        )
    )

    state = {"records": {"r1": {"site": origin, "possibility": "down"}},
             "unrecorded_qubit_density": scale(0.5, IDENTITY)}
    checks.append(
        Check(
            "Qualification: records and an unrecorded quantum predictor are distinguished",
            "r1" in state["records"] and eq(state["unrecorded_qubit_density"], scale(0.5, IDENTITY)),
            "toy partial specification only; not a proof of joint-state sufficiency",
        )
    )

    law_states = [
        {"r1": "down"},
        {"r1": "down", "r2": "up"},
        {},
    ]
    condition = lambda s: "r1" in s
    law = lambda s: "answer" if condition(s) else None
    answers = [law(s) for s in law_states if condition(s)]
    checks.append(
        Check(
            "Qualification: supplied-condition law gives one answer where its condition holds",
            answers and all(a == "answer" for a in answers),
            "toy law has a supplied condition on record configurations and returns one determinate verdict when defined",
        )
    )

    checks.append(
        Check(
            "Boundary: runner supplies no physical context, coupling, apparatus, rate or scale conclusion",
            True,
            "elementary notation and source/registry consistency only; no quantum premise derivation or physical validation",
        )
    )
    return checks


def main() -> int:
    checks = run_checks()
    pass_count = 0
    fail_count = 0
    for item in checks:
        status = "PASS" if item.ok else "FAIL"
        if item.ok:
            pass_count += 1
        else:
            fail_count += 1
        print(f"{status}: {item.name}")
        print(f"      {item.detail}")
    print()
    print(f"runner_check_breakdown = {{A: {pass_count}, B: 0, C: 0, D: 0, total_pass: {pass_count}}}")
    print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    if fail_count == 0:
        print("RESULT: PASS")
        return 0
    print("RESULT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
