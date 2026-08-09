#!/usr/bin/env python3
"""Render the axiom-baseline and approved-primitive-roster blocks in skill docs.

Four agent-facing surfaces restate the framework's axiom baseline and the
approved-primitive roster:

  * docs/ai_methodology/skills/physics-loop/SKILL.md
  * docs/ai_methodology/skills/review-loop/SKILL.md
  * docs/ai_methodology/skills/audit-loop/SKILL.md
  * docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md

Before this generator those restatements were hand-copied, so an owner-approved
axiom revision (for example the 2026-08-05 Admissibility distribution clause)
could land in ``docs/MINIMAL_AXIOMS_*.md`` while the skills kept quoting the
superseded wording. This script makes the restatements a *generated but tracked*
surface, in the same idiom as ``write_citation_graph_manifest.py``:

  * ``--write`` (default) re-renders each marked block and rewrites the tracked
    acknowledgment manifest ``docs/audit/data/skill_axiom_baseline_manifest.json``.
  * ``--check`` re-renders in memory and byte-compares against the committed
    blocks and the committed manifest, exiting nonzero with a precise diff.
    ``run_pipeline.sh`` runs ``--check``; the pipeline never rewrites skill docs.

What is actually sourced, and what is fail-closed
-------------------------------------------------
Three layers, deliberately distinguished so the guarantee is not oversold:

1. *Interpolated values.* Axiom names, the axiom-memo path, the primitive ids
   and their ``current_path``s, and the load-bearing axiom clauses listed in
   ``ATOMS`` are lifted verbatim (whitespace-normalized) out of the sources and
   substituted into the templates. Revise one of these in the source and every
   skill restatement changes with it on the next ``--write``.

2. *Anchor guards.* Each skill phrases the shared facts in its own voice (the
   readout-additivity and law clauses, the primitive boundary sentences). That
   per-file surface wording lives in the templates below, guarded by ``ANCHORS``:
   needles that must still be present in the source doc. If the source stops
   saying the thing a paraphrase paraphrases, the generator aborts and names the
   template to revisit.

3. *The acknowledgment manifest.* Whole-file and per-section digests of the
   axiom memo, the registry, and every registered primitive note. ANY edit to a
   source doc changes the manifest, so ``--check`` fails until a human reruns
   the generator and reviews the regenerated blocks in the diff. This is the
   layer that makes the check fail-closed for source edits the templates do not
   interpolate.

Roster discipline: every primitive registered in ``axiom_premise_nodes.json``
must be rendered inside a target's generated block or already named elsewhere in
that same file. Registering a new primitive therefore fails ``--check`` until
each skill says what the new primitive does and does not grant.

Deterministic: same sources -> byte-identical blocks and manifest.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_REL = "docs/audit/data/axiom_premise_nodes.json"
MANIFEST_REL = "docs/audit/data/skill_axiom_baseline_manifest.json"
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
GENERATOR_NAME = "generate_skill_axiom_baselines.py"

AXIOM_NODE_ID = "minimal_axioms"
BEGIN_MARKER = f"<!-- BEGIN GENERATED: axiom-baseline ({GENERATOR_NAME}) -->"
END_MARKER = "<!-- END GENERATED -->"
WRAP_WIDTH = 79

# The templates below are written against exactly this axiom roster. A rename,
# addition, or removal in the axiom memo is a governance event: it must fail
# loudly so a human rewrites the per-file prose rather than letting the
# generator silently emit a sentence that no longer parses.
EXPECTED_AXIOM_ROSTER = ["Lattice", "Qubit", "Admissibility", "Record"]

COUNT_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}


class SourceDrift(RuntimeError):
    """A source doc no longer carries text the templates depend on."""


# --------------------------------------------------------------------------
# Source atoms: verbatim clauses interpolated into the per-file templates.
# ``section`` is the axiom-memo heading (text after the leading '#'s) the clause
# must appear in; ``text`` is the whitespace-normalized verbatim substring.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Atom:
    key: str
    section: str
    text: str


ATOMS: tuple[Atom, ...] = (
    Atom("no_site_privileged", "Lattice / Physical Locality",
         "No site is privileged"),
    Atom("sites_distinguished", "Lattice / Physical Locality",
         "Sites are distinguished by the supplied lattice structure alone"),
    Atom("possibility_domain", "Qubit / Site Possibility",
         "domain of local possibilities"),
    Atom("algebra_presentation", "Qubit / Site Possibility", "`M_2(C)`"),
    Atom("equivalent_presentation", "Qubit / Site Possibility", "`Cl(3,0)`"),
    Atom("no_possibility_privileged", "Qubit / Site Possibility",
         "No possibility is privileged"),
    Atom("possibilities_distinguished", "Qubit / Site Possibility",
         "Possibilities are distinguished by the supplied algebraic structure "
         "alone"),
    Atom("distribution_clause", "Admissibility / Local Constraint",
         "the probability distribution over the possibilities is determined "
         "by, and varies with, the nearest-neighbor conditions"),
    Atom("record_lock", "Record / Fixed Reality",
         "locks exactly one admissible local possibility"),
    Atom("record_unique", "Record / Fixed Reality",
         "A site never carries more than one record; records are permanent"),
    Atom("records_readable", "Record / Fixed Reality",
         "Only records are readable"),
    Atom("readout_content", "Record / Fixed Reality",
         "readout value is determined by record content alone"),
    Atom("state_def", "Qualification", "A state is a configuration of records"),
)

# Anchors guard the per-file paraphrases that are not interpolated verbatim.
# (label, section, needle) -- the needle must survive in that section.
ANCHORS: tuple[tuple[str, str, str], ...] = (
    ("Lattice substrate paraphrase (the cubic `Z^3` nearest-neighbor locality "
     "substrate with standard translations and proper cubic rotations)",
     "Lattice / Physical Locality",
     "the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard "
     "translations, and proper cubic rotations about each site"),
    ("Admissibility rule paraphrase ('one fixed finite-neighborhood rule, the "
     "same at every lattice translate')",
     "Admissibility / Local Constraint",
     "There is one fixed nearest-neighbor admissibility rule, covariant under "
     "lattice translations and proper cubic rotations"),
    ("Admissibility support paraphrase ('availability is its support')",
     "Admissibility / Local Constraint",
     "\"available\"/\"admissible\" denotes its support"),
    ("Qubit full-presentation paraphrase",
     "Qubit / Site Possibility",
     "The full one-site possibility domain has algebraic presentation"),
    ("Cl(3,0) equivalence paraphrase ('equivalent notation, not extra "
     "primitive structure')",
     "Qubit / Site Possibility",
     "may be used equivalently and adds no further primitive structure"),
    ("Record formation clause",
     "Record / Fixed Reality", "Records form."),
    ("Readout-additivity paraphrase ('finite scalar readout is additive over "
     "finite pairwise-disjoint record collections')",
     "Record / Fixed Reality",
     "For any finite collection of pairwise-disjoint records, scalar readout "
     "`I` is additive"),
    ("Law-domain paraphrase ('its domain is a supplied condition, and where "
     "that condition holds it gives exactly one answer')",
     "Qualification",
     "A law privileges no states. Its domain is a supplied condition, and at "
     "every state where the condition holds it gives exactly one answer"),
)

# Anchors inside each registered primitive's own source note. These guard the
# roster boundary sentences rendered below.
PRIMITIVE_ANCHORS: dict[str, tuple[str, ...]] = {
    "scale_reference_primitive": (
        "`a^{-1} = M_Pl`",
        "This is a units conversion, not a physics axiom.",
        "It does not assert `a/l_P = 1` as a derived theorem.",
    ),
    "kinetic_isotropy_primitive": (
        "c_t = c_s",
        "grained on the same footing as the spatial lattice edge",
        "It does not supply the absolute scale",
    ),
    "realized_state_primitive": (
        "Derivations may evaluate at the realized state, pointwise.",
        "a law-admissible state",
        "The past hypothesis is a separate, stronger input.",
    ),
}

# --------------------------------------------------------------------------
# Downstream-exclusion vocabulary. One entry per excluded downstream structure;
# the value maps a target key to that file's surface wording ("*" = default).
# Keeping all four renderings adjacent is the point: a reviewer sees at a glance
# which surfaces name a given exclusion and how.
# --------------------------------------------------------------------------

EXCLUSIONS: dict[str, dict[str, str]] = {
    "readout_context": {
        "physics-loop": "the readout context",
        "review-loop": "readout-context selection",
        "audit-loop": "context selection",
    },
    "decomposition": {"*": "decomposition"},
    "k_cpt": {"*": "`K`/CPT structure"},
    "sector_generation": {
        "physics-loop": "sector-generation rule",
        "*": "sector-generation rules",
    },
    "distribution_values": {"*": "specific probability-distribution values"},
    "formation_rules": {"*": "formation-site and formation-rate rules"},
    "measurement_dynamics": {"*": "measurement/decoherence dynamics"},
    "record_production": {"*": "record-production dynamics"},
    "persistence": {"*": "physical persistence dynamics"},
    "update_law": {"physics-loop": "update law", "*": "update laws"},
    "time_metric": {"*": "time metric"},
    "within_sector": {"*": "within-sector data"},
    "occupancy": {"physics-loop": "occupancy rule", "*": "occupancy rules"},
    "p2_modulus": {"*": "P2/modulus"},
    "log_det": {"physics-loop": "log-det", "*": "log-det readouts"},
    "source_action": {
        "physics-loop": "source/action",
        "*": "source/action bridges",
    },
    "scale": {"*": "scale"},
    "state_selection": {"*": "state-selection rule"},
    "law_domain": {"*": "law-domain derivation"},
    "local_observability": {"*": "local observability"},
    "law_admissibility": {"*": "law-admissibility or transition relations"},
    "kinetic_branch": {"*": "kinetic-branch selection"},
    "observable_identification": {"*": "arbitrary observable identification"},
}

PHYSICS_LOOP_EXCLUSIONS = (
    "readout_context", "decomposition", "k_cpt", "sector_generation",
    "distribution_values", "formation_rules", "measurement_dynamics",
    "record_production", "persistence", "update_law", "time_metric",
    "within_sector", "occupancy", "p2_modulus", "log_det", "source_action",
    "scale", "state_selection", "law_domain", "observable_identification",
)

REVIEW_LOOP_EXCLUSIONS = (
    "readout_context", "decomposition", "k_cpt", "sector_generation",
    "distribution_values", "measurement_dynamics", "record_production",
    "persistence", "formation_rules", "update_law", "time_metric",
    "within_sector", "occupancy", "p2_modulus", "log_det", "source_action",
    "scale", "local_observability", "law_admissibility", "kinetic_branch",
    "observable_identification",
)

AUDIT_LOOP_EXCLUSIONS = (
    "readout_context", "decomposition", "k_cpt", "sector_generation",
    "distribution_values", "formation_rules", "update_law",
    "measurement_dynamics", "record_production", "persistence", "time_metric",
    "within_sector", "occupancy", "p2_modulus", "log_det", "source_action",
    "scale", "local_observability", "law_admissibility", "kinetic_branch",
    "observable_identification",
)

# --------------------------------------------------------------------------
# Primitive roster surfaces, per target. Each entry is the file's own framing of
# the same registry fact; PRIMITIVE_ANCHORS guards them against source drift.
# --------------------------------------------------------------------------

PRIMITIVE_SURFACES: dict[str, dict[str, str]] = {
    "scale_reference_primitive": {
        "physics-loop":
            "The scale-reference primitive is the approved units primitive; do "
            "not describe it as an admission or a bounded Planck import.",
        "audit-loop":
            "The scale-reference primitive is the approved units primitive, "
            "not an admission or a bounded Planck import.",
        "registry-check":
            "This grants the single dimensionful scale reference "
            "`a^{-1} = M_Pl` as a units conversion only. It is not a Planck "
            "import and not a bounded-status source. It does not assert "
            "`a/l_P = 1` as a derived theorem or supply any dimensionless "
            "physics.",
    },
    "kinetic_isotropy_primitive": {
        "physics-loop":
            "The kinetic-isotropy primitive is the approved structural OS0 "
            "kinetic-form isotropy `c_t = c_s`; do not describe it as an "
            "admission, a bounded import, a Lorentz-closure theorem, a "
            "dynamics, an absolute scale, a spacing-ratio theorem, or an "
            "empirical match.",
        "audit-loop":
            "The kinetic-isotropy primitive is the approved structural OS0 "
            "kinetic-form isotropy `c_t = c_s`, not an admission or a "
            "bounded-status source; it supplies no dynamics, Lorentz-closure "
            "theorem, absolute scale, spacing-ratio theorem, mass ratio, "
            "coupling, mixing angle, phase, selector, readout bridge, "
            "probability rule, normalization rule, or empirical match.",
        "registry-check":
            "This grants only the structural OS0 kinetic-form isotropy "
            "`c_t = c_s`: the emergent tick is grained on the same footing as "
            "the spatial edge. It is not an axiom and not a bounded-status "
            "source. It does not supply an absolute scale, spacing-ratio "
            "theorem, dynamics, Lorentz-closure theorem, mass ratio, coupling, "
            "mixing angle, phase, selector, readout bridge, probability rule, "
            "normalization rule, or empirical match.",
    },
    "realized_state_primitive": {
        "registry-check":
            "This grants only pointwise evaluation at a supplied "
            "law-admissible realized state (the axioms select no state; a "
            "history fixes one). It is not an axiom and not a bounded-status "
            "source. It does not supply a state, state-selection rule, "
            "measure, typicality or genericity assumption, weighting, "
            "normalization, probability rule, preferred or default state, or "
            "any state-contingent value; a quoted number that would differ had "
            "another permitted state been realized is registered data, not "
            "derivation output. The past hypothesis is explicitly not housed "
            "by this primitive.",
    },
}


# --------------------------------------------------------------------------
# Source loading
# --------------------------------------------------------------------------


def norm(text: str) -> str:
    """Collapse all whitespace runs to single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def lc(text: str) -> str:
    """Lowercase the first character only (sentence -> clause)."""
    return text[:1].lower() + text[1:] if text else text


def split_sections(text: str) -> dict[str, str]:
    """Map ATX heading text (level >= 2) to that section's raw body."""
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{2,6})\s+(.*?)\s*$", line)
        if match:
            if current is not None:
                sections[current] = "\n".join(buf)
            current = match.group(2)
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf)
    return sections


@dataclass
class Primitive:
    node_id: str
    path: str


@dataclass
class AxiomSource:
    repo_root: Path
    axioms_path: str
    axiom_names: list[str]
    atoms: dict[str, str]
    primitives: list[Primitive]
    source_texts: dict[str, str]

    @property
    def names_and(self) -> str:
        return oxford(self.axiom_names)

    @property
    def names_slash(self) -> str:
        return "/".join(self.axiom_names)

    @property
    def names_count_word(self) -> str:
        count = len(self.axiom_names)
        if count not in COUNT_WORDS:
            raise SourceDrift(f"no spelled-out word for axiom count {count}")
        return COUNT_WORDS[count]


def oxford(items: list[str], conjunction: str = "and") -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"
    return ", ".join(items[:-1]) + f", {conjunction} {items[-1]}"


def load_source(repo_root: Path) -> AxiomSource:
    registry_path = repo_root / REGISTRY_REL
    if not registry_path.exists():
        raise SourceDrift(f"missing premise registry: {REGISTRY_REL}")
    registry_raw = registry_path.read_text(encoding="utf-8")
    registry = json.loads(registry_raw)

    nodes = registry.get("nodes") or {}
    canonical_ids = list(registry.get("canonical_ids") or [])
    if set(canonical_ids) != set(nodes):
        raise SourceDrift(
            f"{REGISTRY_REL}: canonical_ids and nodes disagree "
            f"({sorted(set(canonical_ids) ^ set(nodes))})"
        )
    if AXIOM_NODE_ID not in nodes:
        raise SourceDrift(f"{REGISTRY_REL}: missing '{AXIOM_NODE_ID}' node")

    axioms_path = nodes[AXIOM_NODE_ID].get("current_path")
    if not axioms_path:
        raise SourceDrift(
            f"{REGISTRY_REL}: '{AXIOM_NODE_ID}' has no current_path"
        )

    primitives = [
        Primitive(node_id=cid, path=nodes[cid]["current_path"])
        for cid in canonical_ids
        if cid != AXIOM_NODE_ID
    ]
    for prim in primitives:
        if not prim.path:
            raise SourceDrift(
                f"{REGISTRY_REL}: '{prim.node_id}' has no current_path"
            )

    source_texts: dict[str, str] = {REGISTRY_REL: registry_raw}

    axioms_file = repo_root / axioms_path
    if not axioms_file.exists():
        raise SourceDrift(f"registered axiom memo missing on disk: {axioms_path}")
    axioms_text = axioms_file.read_text(encoding="utf-8")
    source_texts[axioms_path] = axioms_text
    sections = split_sections(axioms_text)

    axiom_names = re.findall(
        r"^\d+\.\s+\*\*([^*]+)\*\*\s*$", sections.get("Purpose", ""), re.MULTILINE
    )
    axiom_names = [name.strip() for name in axiom_names]
    if axiom_names != EXPECTED_AXIOM_ROSTER:
        raise SourceDrift(
            f"{axioms_path}: axiom roster is {axiom_names!r}, templates are "
            f"written for {EXPECTED_AXIOM_ROSTER!r}. An axiom rename/addition/"
            f"removal is a governance event: update the per-file templates in "
            f"{GENERATOR_NAME} and EXPECTED_AXIOM_ROSTER, then regenerate."
        )

    normalized_sections = {name: norm(body) for name, body in sections.items()}

    atoms: dict[str, str] = {}
    for atom in ATOMS:
        if atom.section not in normalized_sections:
            raise SourceDrift(
                f"{axioms_path}: section '{atom.section}' not found "
                f"(needed by atom '{atom.key}')"
            )
        if atom.text not in normalized_sections[atom.section]:
            raise SourceDrift(
                f"{axioms_path} / '{atom.section}': atom '{atom.key}' no longer "
                f"present. Expected verbatim: {atom.text!r}. Update ATOMS and "
                f"the per-file templates in {GENERATOR_NAME}, then regenerate."
            )
        atoms[atom.key] = atom.text

    for label, section, needle in ANCHORS:
        if section not in normalized_sections:
            raise SourceDrift(
                f"{axioms_path}: section '{section}' not found (anchor: {label})"
            )
        if norm(needle) not in normalized_sections[section]:
            raise SourceDrift(
                f"{axioms_path} / '{section}': anchor for {label} is gone. "
                f"Expected: {norm(needle)!r}. The skill wording it guards is now "
                f"unsourced -- revisit the template in {GENERATOR_NAME}."
            )

    for prim in primitives:
        note_file = repo_root / prim.path
        if not note_file.exists():
            raise SourceDrift(
                f"registered primitive note missing on disk: {prim.path}"
            )
        note_text = note_file.read_text(encoding="utf-8")
        source_texts[prim.path] = note_text
        expected = PRIMITIVE_ANCHORS.get(prim.node_id)
        if expected is None:
            raise SourceDrift(
                f"primitive '{prim.node_id}' is registered but has no entry in "
                f"PRIMITIVE_ANCHORS. Add its boundary anchors and its per-file "
                f"roster wording in {GENERATOR_NAME}, then regenerate."
            )
        note_norm = norm(note_text)
        for needle in expected:
            if norm(needle) not in note_norm:
                raise SourceDrift(
                    f"{prim.path}: boundary anchor {norm(needle)!r} is gone. The "
                    f"roster sentence for '{prim.node_id}' is now unsourced -- "
                    f"revisit PRIMITIVE_SURFACES in {GENERATOR_NAME}."
                )
    for node_id in PRIMITIVE_ANCHORS:
        if node_id not in {p.node_id for p in primitives}:
            raise SourceDrift(
                f"PRIMITIVE_ANCHORS names '{node_id}', which is no longer "
                f"registered in {REGISTRY_REL}. Remove its templates from "
                f"{GENERATOR_NAME}, then regenerate."
            )

    return AxiomSource(
        repo_root=repo_root,
        axioms_path=axioms_path,
        axiom_names=axiom_names,
        atoms=atoms,
        primitives=primitives,
        source_texts=source_texts,
    )


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def exclusion_list(target_key: str, ids: tuple[str, ...]) -> str:
    surfaces: list[str] = []
    for vocab_id in ids:
        entry = EXCLUSIONS.get(vocab_id)
        if entry is None:
            raise SourceDrift(
                f"target '{target_key}' names undeclared exclusion "
                f"'{vocab_id}'; add it to EXCLUSIONS"
            )
        surface = entry.get(target_key, entry.get("*"))
        if surface is None:
            raise SourceDrift(
                f"exclusion '{vocab_id}' has no surface wording for target "
                f"'{target_key}' and no '*' default"
            )
        surfaces.append(surface)
    if len(surfaces) < 2:
        return "".join(surfaces)
    return ", ".join(surfaces[:-1]) + ", or " + surfaces[-1]


def registered(src: AxiomSource, target: "Target", node_id: str) -> Primitive:
    for prim in src.primitives:
        if prim.node_id == node_id:
            return prim
    raise SourceDrift(
        f"target '{target.key}' renders roster entry '{node_id}', which is not "
        f"registered in {REGISTRY_REL}. Drop it from that target's roster_scope "
        f"in {GENERATOR_NAME}, and remove its prose from {target.path}."
    )


def primitive_surface(node_id: str, target_key: str) -> str:
    entry = PRIMITIVE_SURFACES.get(node_id)
    if entry is None or target_key not in entry:
        raise SourceDrift(
            f"no '{target_key}' roster wording for registered primitive "
            f"'{node_id}'; add it to PRIMITIVE_SURFACES in {GENERATOR_NAME}"
        )
    return entry[target_key]


def render_physics_loop(src: AxiomSource, target: "Target") -> list[str]:
    a = src.atoms
    body = (
        f"The approved axiom baseline is the current {src.names_slash} surface "
        f"(`{src.axioms_path}`): "
        f"{lc(a['no_site_privileged'])}; {lc(a['sites_distinguished'])}; "
        f"{lc(a['no_possibility_privileged'])}; "
        f"{lc(a['possibilities_distinguished'])}; "
        f"Admissibility is one fixed finite-neighborhood rule, the same at "
        f"every lattice translate, and for each site {a['distribution_clause']}, "
        f"with availability/admissibility being that distribution's support; "
        f"a record, when present, {a['record_lock']}; "
        f"{lc(a['record_unique'])}; {lc(a['records_readable'])}; "
        f"{lc(a['readout_content'])}; finite scalar readout is additive over "
        f"finite pairwise-disjoint record collections; {lc(a['state_def'])}; "
        f"and a law privileges no states, has a supplied condition as its "
        f"domain, and gives exactly one answer where the condition holds. "
        f"It does not supply "
        f"{exclusion_list(target.key, PHYSICS_LOOP_EXCLUSIONS)}. "
        f"The neighborhood-determined probability distribution is therefore "
        f"axiom content; only its specific values are downstream. "
        + " ".join(
            primitive_surface(node_id, target.key)
            for node_id in target.roster_scope
        )
    )
    return wrap_paragraph(body, indent="")


def render_review_loop(src: AxiomSource, target: "Target") -> list[str]:
    a = src.atoms
    axioms_basename = src.axioms_path.rsplit("/", 1)[-1]
    body = (
        f"The framework baseline (per `{axioms_basename}`) is the "
        f"{src.names_count_word} named axioms {src.names_and}. "
        f"{src.axiom_names[0]} is the cubic `Z^3` lattice with "
        f"nearest-neighbor adjacency, standard translations, and proper cubic "
        f"rotations about each site; {lc(a['no_site_privileged'])}, and "
        f"{lc(a['sites_distinguished'])}. "
        f"{src.axiom_names[1]} is the {a['possibility_domain']} with full "
        f"one-site algebraic presentation "
        f"{a['algebra_presentation'].replace('(C)', '(ℂ)')}; "
        f"{a['equivalent_presentation']} is equivalent notation, not extra "
        f"primitive structure, and {lc(a['no_possibility_privileged'])}; "
        f"{lc(a['possibilities_distinguished'])}. "
        f"{src.axiom_names[2]} is one fixed finite-neighborhood rule, the same "
        f"at every lattice translate; for each site, "
        f"{a['distribution_clause']}; availability is its support. "
        f"A record, when present, {a['record_lock']}. "
        f"{a['record_unique']}. {a['records_readable']}; "
        f"a {a['readout_content']}; finite scalar readout is additive over "
        f"finite pairwise-disjoint record collections. {a['state_def']}. "
        f"A law privileges no states: its domain is a supplied condition, and "
        f"where that condition holds it gives exactly one answer. "
        f"Additional structures such as "
        f"{exclusion_list(target.key, REVIEW_LOOP_EXCLUSIONS)} remain "
        f"compatible downstream targets, but require derivation, bridge, or "
        f"approved primitive registration before use as load-bearing content."
    )
    return wrap_paragraph(body, indent="")


def render_audit_loop(src: AxiomSource, target: "Target") -> list[str]:
    a = src.atoms
    body = (
        f"The current axiom baseline is {src.names_and}. "
        f"{src.axiom_names[0]} is the cubic `Z^3` nearest-neighbor locality "
        f"substrate with standard translations and proper cubic rotations "
        f"about each site; {lc(a['no_site_privileged'])}, and "
        f"{lc(a['sites_distinguished'])}. "
        f"{src.axiom_names[1]} is the {a['possibility_domain']} with full "
        f"one-site algebraic presentation {a['algebra_presentation']}, with "
        f"{a['equivalent_presentation']} only as equivalent notation, "
        f"{lc(a['no_possibility_privileged'])}, and "
        f"{lc(a['possibilities_distinguished'])}. "
        f"{src.axiom_names[2]} is one fixed finite-neighborhood rule, the same "
        f"at every lattice translate; for each site, "
        f"{a['distribution_clause']}; availability is its support. "
        f"A record, when present, {a['record_lock']}. "
        f"{a['record_unique']}. {a['records_readable']}; "
        f"a {a['readout_content']}; scalar-valued finite readout is additive "
        f"over finite pairwise-disjoint record collections. {a['state_def']}. "
        f"A law privileges no states: its domain is a supplied condition, and "
        f"where that condition holds it gives exactly one answer. "
        f"Downstream structures such as "
        f"{exclusion_list(target.key, AUDIT_LOOP_EXCLUSIONS)} remain "
        f"compatible targets but require derivation, bridge, retained "
        f"derivation or approved primitive registration before use as "
        f"load-bearing content. "
        + " ".join(
            primitive_surface(node_id, target.key)
            for node_id in target.roster_scope
        )
    )
    return wrap_paragraph(body, indent="  ")


def render_registry_check(src: AxiomSource, target: "Target") -> list[str]:
    lines: list[str] = []
    for node_id in target.roster_scope:
        prim = registered(src, target, node_id)
        lines.append(f"- `{prim.node_id}`:")
        body = f"`{prim.path}`. {primitive_surface(node_id, target.key)}"
        lines.extend(wrap_paragraph(body, indent="  "))
    return lines


def wrap_paragraph(text: str, indent: str) -> list[str]:
    return textwrap.wrap(
        norm(text),
        width=WRAP_WIDTH,
        initial_indent=indent,
        subsequent_indent=indent,
        break_long_words=False,
        break_on_hyphens=False,
    )


# --------------------------------------------------------------------------
# Targets
# --------------------------------------------------------------------------


@dataclass
class Target:
    key: str
    path: str
    renderer: Callable[[AxiomSource, "Target"], list[str]]
    marker_indent: str
    # Primitives whose roster sentence this file's generated block renders.
    # Registered primitives outside this scope must still be named somewhere in
    # the same file (checked by verify_roster_coverage).
    roster_scope: tuple[str, ...] = field(default_factory=tuple)


TARGETS: tuple[Target, ...] = (
    Target(
        key="physics-loop",
        path="docs/ai_methodology/skills/physics-loop/SKILL.md",
        renderer=render_physics_loop,
        marker_indent="",
        roster_scope=("scale_reference_primitive", "kinetic_isotropy_primitive"),
    ),
    Target(
        key="review-loop",
        path="docs/ai_methodology/skills/review-loop/SKILL.md",
        renderer=render_review_loop,
        marker_indent="",
        roster_scope=(),
    ),
    Target(
        key="audit-loop",
        path="docs/ai_methodology/skills/audit-loop/SKILL.md",
        renderer=render_audit_loop,
        marker_indent="  ",
        roster_scope=("scale_reference_primitive", "kinetic_isotropy_primitive"),
    ),
    Target(
        key="registry-check",
        path="docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md",
        renderer=render_registry_check,
        marker_indent="",
        roster_scope=(
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ),
    ),
)


def find_block(lines: list[str], target: Target) -> tuple[int, int]:
    """Return (begin_index, end_index) of the marker lines, or raise."""
    begins = [i for i, ln in enumerate(lines) if ln.strip() == BEGIN_MARKER]
    ends = [i for i, ln in enumerate(lines) if ln.strip() == END_MARKER]
    if len(begins) != 1 or len(ends) != 1:
        raise SourceDrift(
            f"{target.path}: expected exactly one BEGIN and one END marker, "
            f"found {len(begins)} and {len(ends)}. Markers are:\n"
            f"  {BEGIN_MARKER}\n  {END_MARKER}"
        )
    if ends[0] <= begins[0]:
        raise SourceDrift(f"{target.path}: END marker precedes BEGIN marker")
    return begins[0], ends[0]


def verify_roster_coverage(src: AxiomSource, target: Target, text: str) -> None:
    for prim in src.primitives:
        if prim.node_id in target.roster_scope:
            continue
        if prim.node_id not in text:
            raise SourceDrift(
                f"{target.path}: registered primitive '{prim.node_id}' is "
                f"neither rendered in the generated block nor named elsewhere "
                f"in the file. Every registered primitive must have a stated "
                f"boundary on every skill surface: add prose naming it (or add "
                f"it to this target's roster_scope in {GENERATOR_NAME})."
            )


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_manifest(src: AxiomSource, blocks: dict[str, list[str]]) -> dict:
    sources: dict[str, dict] = {}
    for rel_path, text in sorted(src.source_texts.items()):
        entry: dict[str, object] = {"sha256": sha256_text(text)}
        if rel_path.endswith(".md"):
            entry["sections"] = {
                name: sha256_text(norm(body))[:12]
                for name, body in sorted(split_sections(text).items())
            }
        sources[rel_path] = entry

    targets: dict[str, dict] = {}
    for target in TARGETS:
        rendered = "\n".join(blocks[target.key]) + "\n"
        targets[target.path] = {
            "block_lines": len(blocks[target.key]),
            "block_sha256": sha256_text(rendered),
            "roster_scope": list(target.roster_scope),
        }

    return {
        "schema_version": 1,
        "generator": GENERATOR_REL,
        "axiom_roster": list(src.axiom_names),
        "axioms_path": src.axioms_path,
        "primitive_roster": [p.node_id for p in src.primitives],
        "sources": sources,
        "targets": targets,
    }


def manifest_bytes(manifest: dict) -> str:
    return json.dumps(manifest, indent=1, sort_keys=True) + "\n"


# --------------------------------------------------------------------------
# Drive
# --------------------------------------------------------------------------


def render_all(src: AxiomSource) -> dict[str, list[str]]:
    return {target.key: target.renderer(src, target) for target in TARGETS}


def diff_report(path: str, committed: list[str], expected: list[str]) -> str:
    diff = difflib.unified_diff(
        [ln + "\n" for ln in committed],
        [ln + "\n" for ln in expected],
        fromfile=f"{path} (committed block)",
        tofile=f"{path} (regenerated)",
        lineterm="\n",
    )
    return "".join(diff)


def run(repo_root: Path, check_only: bool) -> int:
    src = load_source(repo_root)
    blocks = render_all(src)
    manifest = manifest_bytes(build_manifest(src, blocks))

    failures: list[str] = []
    for target in TARGETS:
        file_path = repo_root / target.path
        if not file_path.exists():
            failures.append(f"  FAIL {target.path}: file missing on disk")
            continue
        original = file_path.read_text(encoding="utf-8")
        lines = original.splitlines()
        begin, end = find_block(lines, target)
        verify_roster_coverage(src, target, original)

        committed = lines[begin + 1:end]
        expected = blocks[target.key]
        indent = target.marker_indent
        rebuilt_lines = (
            lines[:begin]
            + [indent + BEGIN_MARKER]
            + expected
            + [indent + END_MARKER]
            + lines[end + 1:]
        )
        rebuilt = "\n".join(rebuilt_lines) + ("\n" if original.endswith("\n") else "")

        if check_only:
            if committed != expected:
                failures.append(
                    f"  FAIL {target.path}: generated block is stale\n"
                    + diff_report(target.path, committed, expected)
                )
            elif rebuilt != original:
                failures.append(
                    f"  FAIL {target.path}: marker indentation drifted"
                )
            else:
                print(f"  OK   {target.path}: axiom-baseline block in sync")
        else:
            if rebuilt != original:
                file_path.write_text(rebuilt, encoding="utf-8")
                print(f"  wrote {target.path} ({len(expected)} block lines)")
            else:
                print(f"  unchanged {target.path} ({len(expected)} block lines)")

    manifest_path = repo_root / MANIFEST_REL
    if check_only:
        committed_manifest = (
            manifest_path.read_text(encoding="utf-8")
            if manifest_path.exists()
            else ""
        )
        if committed_manifest != manifest:
            detail = "".join(
                difflib.unified_diff(
                    committed_manifest.splitlines(keepends=True),
                    manifest.splitlines(keepends=True),
                    fromfile=f"{MANIFEST_REL} (committed)",
                    tofile=f"{MANIFEST_REL} (recomputed)",
                    lineterm="\n",
                )
            )
            failures.append(
                f"  FAIL {MANIFEST_REL}: source acknowledgment is stale\n" + detail
            )
        else:
            print(f"  OK   {MANIFEST_REL}: source acknowledgment current")
    else:
        manifest_path.write_text(manifest, encoding="utf-8")
        print(f"  wrote {MANIFEST_REL}")

    if failures:
        print("\n".join(failures))
        print(
            "\ngenerate_skill_axiom_baselines: the skill axiom-baseline surfaces "
            "no longer match\ntheir sources. Do not hand-edit the generated "
            "blocks. Review the drift above, then\nrun:\n"
            f"    python3 {GENERATOR_REL}\nand commit the regenerated blocks and "
            "manifest with the source change."
        )
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed blocks and manifest instead of writing",
    )
    parser.add_argument(
        "--repo-root",
        default=str(REPO_ROOT),
        help="repository root to operate on (used by tests)",
    )
    args = parser.parse_args(argv)
    try:
        return run(Path(args.repo_root).resolve(), check_only=args.check)
    except SourceDrift as exc:
        print(f"generate_skill_axiom_baselines: SOURCE DRIFT\n  {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
