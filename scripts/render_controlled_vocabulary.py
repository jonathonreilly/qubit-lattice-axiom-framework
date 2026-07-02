#!/usr/bin/env python3
"""Deterministic renderer for the vocabulary docs.

Reads docs/repo/controlled_vocabulary.yaml + scripts/templates/*.template
and regenerates:
  - docs/repo/CONTROLLED_VOCABULARY.md
  - docs/KEY_TERMINOLOGY.md

The CV.md template carries `{{SLOT}}` markers where structured data
from the YAML fills in (tables, lists, term-family enums, etc.).
Prose narrative stays in the template, editable as plain Markdown.
KEY_TERMINOLOGY.md is currently a passthrough template (A-Z index
regeneration is deferred to Cleanup-1c).

Generated files carry a `<!-- generated; do not edit by hand;
source: docs/repo/controlled_vocabulary.yaml hash=<sha256> -->` header.
Direct edits to the rendered files are forbidden — change the YAML or
the template instead.

Usage:
  scripts/render_controlled_vocabulary.py            # write rendered output
  scripts/render_controlled_vocabulary.py --check    # diff render vs on-disk

Exit codes:
  0  rendered (write) / no drift (--check)
  1  drift detected (--check)
  2  template / YAML error
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = REPO_ROOT / "docs" / "repo" / "controlled_vocabulary.yaml"
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
CV_TEMPLATE = TEMPLATE_DIR / "CONTROLLED_VOCABULARY.md.template"
KT_TEMPLATE = TEMPLATE_DIR / "KEY_TERMINOLOGY.md.template"
CV_OUT = REPO_ROOT / "docs" / "repo" / "CONTROLLED_VOCABULARY.md"
KT_OUT = REPO_ROOT / "docs" / "KEY_TERMINOLOGY.md"


def load_yaml() -> dict:
    if not YAML_PATH.exists():
        print(f"FAIL: {YAML_PATH} missing", file=sys.stderr)
        raise SystemExit(2)
    return yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))


def yaml_sha256() -> str:
    return hashlib.sha256(YAML_PATH.read_bytes()).hexdigest()


# -----------------------------------------------------------------------------
# Slot renderers — each returns the Markdown string for one {{SLOT}}.
# -----------------------------------------------------------------------------


def render_vocab_hierarchy_table(data: dict) -> str:
    """The 5-layer Vocabulary Hierarchy table."""
    # Map YAML layers to the CV.md table rows. The table is hard-coded
    # in CV.md prose currently; we render a faithful reproduction here.
    rows = [
        (
            "0. Front-door A-Z lookup",
            "`docs/KEY_TERMINOLOGY.md`",
            "Single-page A-Z index of every repo-canonical term with a one-line definition and a pointer to its source-of-truth doc. The reader entry-point above all layers below; an index, not an authority. New terms enter the index only after the source-of-truth doc accepts them.",
        ),
        (
            "1. Framework substantive",
            "`docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/audit/data/axiom_premise_nodes.json`",
            "Framework axioms and explicitly approved primitive premise nodes the operational vocabulary uses: Lattice (`Z^3` with nearest-neighbor adjacency, standard translations, proper cubic rotations about each site, no privileged site, and site distinctions carried only by the supplied lattice structure), Qubit (the domain of local possibilities with full one-site algebraic presentation `M_2(ℂ)`; `Cl(3,0)` is equivalent notation, not extra primitive content; no possibility is privileged; possibilities are distinguished by the supplied algebraic structure alone), Admissibility (one fixed nearest-neighbor rule, covariant under lattice translations and proper cubic rotations, by which the available possibilities are determined by, and vary with, the nearest-neighbor conditions at each site), Record (optional fixed locking of one available local possibility; readout value determined by record content alone; finite scalar additivity), the state/law qualification clauses, the definition of `A_min`, the status of prior `A3` / `A4` / `A5` as open gates rather than axioms, and registered primitive premise nodes such as the scale-reference and kinetic-isotropy primitives. Changes only when a framework-level science decision changes.",
        ),
        (
            "2. External paper text",
            "[`docs/ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md`](../ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md), [`docs/ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md`](../ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md)",
            "Verbatim reusable disclosure paragraphs for papers, preprints, and talks. The framing paragraph is the short paper-facing form; the accountability disclosure is the longer package-level form. Both carry their own usage guidance (e.g. replacing `[repo URL]`, narrowing the tool list when only one was used).",
        ),
        (
            "3. Operational (this doc)",
            "`docs/repo/CONTROLLED_VOCABULARY.md`",
            "Status taxonomy, claim-strength labels, audit-lane field enums, repair classes, filename conventions, archival paths, topic language, and paper-facing prose voice — the working vocabulary used inside the repo across ledgers, tables, notes, runners, skills, and PR descriptions.",
        ),
        (
            "4. Methodology framing (adjacent)",
            "`docs/AI_METHODOLOGY_NOTE_2026-04-25.md`",
            "The curated front-door note for the methodology lane. Defines how to talk about the AI / methodology side at the project level.",
        ),
    ]
    out = ["| Layer | Source-of-truth doc | Governs |", "|---|---|---|"]
    for layer, source, governs in rows:
        out.append(f"| {layer} | {source} | {governs} |")
    return "\n".join(out)


def render_publication_capture_dispositions(data: dict) -> str:
    pcd = data["publication_capture_dispositions"]
    lines = [f"Use these on publication-control-plane surfaces such as", f"`PUBLICATION_MATRIX.md`.", ""]
    lines.append("| Label | Use |")
    lines.append("|---|---|")
    for entry in pcd["labels"]:
        lines.append(f"| `{entry['label']}` | {entry['use']} |")
    lines.append("")
    lines.append(pcd["footnote"])
    return "\n".join(lines)


def render_claim_strength_labels(data: dict) -> str:
    csl = data["claim_strength_labels"]
    lines = ["Use these on notes, claims tables, quantitative tables, and runner summaries.", ""]
    lines.append("| Label | Use |")
    lines.append("|---|---|")
    for entry in csl["labels"]:
        label = entry["label"]
        # Match CV.md's hand-formatted convention: for slash-separated
        # alternatives, wrap each side in its own backtick pair. For
        # single labels, wrap the whole thing in one pair.
        if " / " in label:
            parts = label.split(" / ")
            label_formatted = " / ".join(f"`{p}`" for p in parts)
        else:
            label_formatted = f"`{label}`"
        lines.append(f"| {label_formatted} | {entry['use']} |")
    lines.append("")
    lines.append(csl["allowed_composite_forms_intro"])
    lines.append("")
    for form in csl["allowed_composite_forms"]:
        lines.append(f"- `{form}`")
    lines.append("")
    lines.append(csl["allowed_composite_forms_footnote"])
    lines.append("")
    lines.append(csl["role_specialized_variants_intro"])
    lines.append("")
    for variant in csl["role_specialized_variants"]:
        lines.append(f"- `{variant}`")
    lines.append("")
    lines.append(csl["scope_qualifier_intro"])
    lines.append("")
    for ex in csl["scope_qualifier_examples"]:
        lines.append(f"- `{ex}`")
    lines.append("")
    lines.append(csl["review_adjective_warning"])
    return "\n".join(lines)


def _render_term_family_section(family_data: dict, name: str, kind_heading: str) -> list[str]:
    """Render one term-family subsection of the Audit Lane Field Vocabulary."""
    lines = []
    lines.append(f"### `{name}` ({kind_heading})")
    lines.append("")
    lines.append(family_data["description"])
    lines.append("")
    lines.append("Exactly one of:")
    lines.append("")
    for value in family_data["values"].keys():
        lines.append(f"- `{value}`")
    return lines


def render_audit_lane_field_vocabulary(data: dict) -> str:
    """The Audit Lane Field Vocabulary section.

    This renders the substantial body of the Audit Lane Field Vocabulary
    section — the per-field subheadings, value enumerations, and
    accompanying prose. The rendering mirrors the on-disk shape.
    """
    tf = data["term_families"]
    lines = []

    # claim_type
    lines.append("### `claim_type` (auditor-set)")
    lines.append("")
    lines.append("What kind of object the auditor says the row is. Exactly one of:")
    lines.append("")
    for v in tf["claim_type"]["values"]:
        lines.append(f"- `{v}`")
    lines.append("")
    lines.append(
        "`meta` is used for non-claim infrastructure rows (audit-prep notes,\n"
        "synthesis catalogues, infrastructure documentation). `meta` rows must\n"
        "not promote to non-meta claim types via re-classification — these notes\n"
        "are by design out-of-band."
    )
    lines.append("")

    # claim_scope
    lines.append("### `claim_scope` (auditor-set)")
    lines.append("")
    lines.append(
        "The auditor's short, citeable statement of exactly what was audited.\n"
        "Required for applied audits. Prose, not enum."
    )
    lines.append("")

    # audit_status
    lines.append("### `audit_status` (auditor-set)")
    lines.append("")
    lines.append("What the audit found. Exactly one of:")
    lines.append("")
    for v in tf["audit_status"]["values"]:
        lines.append(f"- `{v}`")
    lines.append("")

    # effective_status
    lines.append("### `effective_status` (derived by pipeline)")
    lines.append("")
    lines.append(
        "Publication-facing status derived from `claim_type` plus\n"
        "`audit_status` plus the citation-graph closure of dependencies. The\n"
        "pipeline computes this; do not write to it directly. Possible values:"
    )
    lines.append("")
    eff_explanations = [
        ("retained", "`claim_type = positive_theorem` plus\n  `audit_status = audited_clean` plus retained-grade dependencies"),
        ("retained_no_go", "`claim_type = no_go` plus\n  `audit_status = audited_clean` plus retained-grade dependencies"),
        ("retained_bounded", "`claim_type = bounded_theorem` plus\n  `audit_status = audited_clean` plus retained-grade dependencies"),
        ("retained_pending_chain", "clean theorem/no-go/bounded row whose\n  upstream chain is not yet retained-grade"),
        ("open_gate", "clean open gate; blocks retained propagation"),
        ("decoration_under_<parent_claim_id>", "audited decoration whose\n  parent is retained-grade"),
        ("meta", "non-claim infrastructure rows"),
        ("audited_<failure_mode>", "terminal non-clean audit verdicts on active\n  claims"),
    ]
    for name, expl in eff_explanations:
        lines.append(f"- `{name}` — {expl}")
    lines.append("")
    lines.append(
        "Generated audit data must not contain legacy source-status authority\n"
        "fields. The graph builder may use old source-note status prose as a\n"
        "one-way migration hint when seeding `claim_type`, but the ledger, queue,\n"
        "prompt, and rendered audit surfaces are\n"
        "`claim_type` / `audit_status` / `effective_status` only. `support` is\n"
        "not a claim class."
    )
    lines.append("")

    # repair_class
    lines.append("### Conditional repair classes")
    lines.append("")
    lines.append(
        "For every `audited_conditional` result, the auditor must make the next\n"
        "repair lane sortable by prefixing `notes_for_re_audit_if_any` with\n"
        "exactly one of these seven classes:"
    )
    lines.append("")
    repair_explanations = [
        ("missing_dependency_edge", "a needed source note or authority exists\n  or is named, but is not wired as a direct dependency for the audited\n  claim"),
        ("dependency_not_retained", "a direct dependency exists but is not\n  retained grade"),
        ("missing_bridge_theorem", "the claim needs a new theorem for a\n  physical carrier, readout, unit map, boundary condition, sector\n  choice, normalization, or observable bridge"),
        ("scope_too_broad", "a clean bounded core exists, but the current claim\n  scope includes an unclosed extension"),
        ("runner_artifact_issue", "a runner, log, classifier, threshold,\n  import, or pass/fail accounting problem blocks closure despite\n  otherwise local scope"),
        ("compute_required", "closure needs a completed long run, sliced\n  runner, cached certificate, or independent derivation"),
        ("other", "use only when none of the above fits, and state why"),
    ]
    for name, expl in repair_explanations:
        lines.append(f"- `{name}` — {expl}")
    lines.append("")
    lines.append("After the class, the auditor names the cheapest next repair action.")
    lines.append("")

    # independence
    lines.append("### Independence tiers")
    lines.append("")
    lines.append(
        "`auditor` must not equal `author`. Strength tiers for the `independence`\n"
        "field on an audit row:"
    )
    lines.append("")
    indep_explanations = [
        ("weak", "same model family, or a session whose context\n  restrictions cannot be established. Permitted for diagnostic review,\n  not eligible to land `audited_clean`"),
        ("fresh_context", "same model family, different\n  auditor/session identity, restricted-input audit. Same-family\n  clean-room tier for detecting context poisoning without claiming\n  cross-family review"),
        ("cross_family", "different model family from the author"),
        ("strong", "human auditor with no prior involvement in\n  the note"),
        ("external", "off-repo reviewer with no project context;\n  the audit lane does not produce these on its own"),
    ]
    for name, expl in indep_explanations:
        lines.append(f"- `independence: {name}` — {expl}")
    lines.append("")

    # auditor_family
    lines.append("### `auditor_family`")
    lines.append("")
    lines.append(
        "The model family of the auditor (e.g., `codex-gpt-5.5`, `codex-gpt-5.6`,\n"
        "`claude-opus-4.x`, `human`). Used to enforce cross-family independence.\n"
        "The designated cross-family auditor for this repo is the best available\n"
        "full Codex GPT model at maximum reasoning; see\n"
        "`docs/audit/FRESH_LOOK_REQUIREMENTS.md` for the auto-selection rule."
    )
    lines.append("")

    # load_bearing_step_class
    lines.append("### Load-bearing step classes")
    lines.append("")
    lines.append(
        "When the auditor records the kind of step the load-bearing sentence /\n"
        "equation is, pick exactly one of:"
    )
    lines.append("")
    lbsc_short = [
        ("(A)", "algebraic identity check on existing inputs"),
        ("(B)", "cross-note input verification (reads value from another note)"),
        ("(C)", "first-principles compute from the axiom (`Cl(3)` on `Z^3` plus\n  accepted normalizations) producing a number not present in any input"),
        ("(D)", "external comparator check against PDG / lattice QCD / observation"),
        ("(E)", "definition (introduces a new symbol)"),
        ("(F)", "renaming (asserts symbol identity between two existing concepts)"),
        ("(G)", "numerical match at a tuned input scale"),
    ]
    for cls, expl in lbsc_short:
        lines.append(f"- `{cls}` {expl}")

    return "\n".join(lines)


def render_migration_legacy_wording(data: dict) -> str:
    mlw = data["migration_legacy_wording"]
    lines = [mlw["intro"], ""]
    for v in mlw["values"]:
        lines.append(f"- `{v['label']}` — {v['definition']}")
    lines.append("")
    lines.append(mlw["ratified_surface_pointer"])
    lines.append("")
    lines.append(mlw["new_note_rule"])
    return "\n".join(lines)


def _render_simple_label_table(section: dict) -> str:
    lines = []
    # Use the YAML's use_context verbatim — preserves file-name casing.
    lines.append(f"Use these only on {section['use_context']}")
    lines.append("")
    lines.append("| Label | Use |")
    lines.append("|---|---|")
    for entry in section["labels"]:
        lines.append(f"| `{entry['label']}` | {entry['use']} |")
    return "\n".join(lines)


def render_historical_lane_board_labels(data: dict) -> str:
    return _render_simple_label_table(data["historical_lane_board_labels"])


def render_historical_discovery_log_labels(data: dict) -> str:
    return _render_simple_label_table(data["historical_discovery_log_labels"])


def render_column_rules(data: dict) -> str:
    cr = data["column_rules"]
    lines = []
    for f in cr["files"]:
        lines.append(f"- `{f['file']}`")
        for rule in f["rules"]:
            lines.append(f"  - {rule}")
    lines.append("")
    lines.append(cr["footnote"])
    return "\n".join(lines)


def render_protocol_qualifiers(data: dict) -> str:
    pq = data["protocol_qualifiers"]
    lines = [pq["intro"], ""]
    for v in pq["values"]:
        lines.append(f"- `{v}`")
    lines.append("")
    lines.append(pq["footnote"])
    return "\n".join(lines)


def render_evidence_terms(data: dict) -> str:
    et = data["evidence_terms"]
    lines = [et["intro"], ""]
    for v in et["preferred"]:
        lines.append(f"- `{v['term']}`: {v['definition']}")
    lines.append("")
    lines.append(et["avoid_intro"])
    lines.append("")
    for v in et["avoid"]:
        lines.append(f"- `{v['term']}` {v['context']}")
    return "\n".join(lines)


def render_hyphenation_rules(data: dict) -> str:
    rules = data["hyphenation_rules"]
    lines = []
    for r in rules:
        lines.append(f"- prefer `{r['prefer']}`")
    return "\n".join(lines)


def render_stale_narrative_archival(data: dict) -> str:
    sna = data["stale_narrative_archival"]
    lines = [sna["intro"], ""]
    lines.append("### Archive path")
    lines.append("")
    examples = ", ".join(f"`{e}`" for e in sna["archive_path"]["cluster_tag_examples"])
    lines.append(
        f"`{sna['archive_path']['pattern']}` — {sna['archive_path']['description']} "
        f"The cluster-tag is a short stable noun\nphrase for the wrapper cluster (e.g. {examples})."
    )
    lines.append("")
    lines.append("### Salvage-note required content")
    lines.append("")
    lines.append(sna["salvage_note_required_content"]["intro"])
    lines.append("")
    for item in sna["salvage_note_required_content"]["must_state"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append(
        "The salvage note must not " + sna["salvage_note_required_content"]["must_not"] + "."
    )
    lines.append("")
    lines.append("### Banned archival wording")
    lines.append("")
    for ban in sna["banned_wording"]:
        lines.append(f"- describing the archived wrapper as {ban['phrase']} — {ban['reason']}")
    lines.append("")
    lines.append(sna["workflow_pointer"])
    return "\n".join(lines)


def render_topic_local_language(data: dict) -> str:
    """Topic-local sections that Cleanup-2 moves out of CV.md."""
    sections = data["topic_local_language"]
    out = []
    for s in sections:
        out.append(f"## {s['heading']}")
        out.append("")
        out.append(s["body"])
        out.append("")
    return "\n".join(out).rstrip()


def render_paper_voice(data: dict) -> str:
    pv = data["paper_voice"]
    lines = [pv["intro"], "", "### The rule", "", pv["rule"], "", "### Use this voice", ""]
    for u in pv["use_this"]:
        lines.append(f"- {u}")
    lines.append("")
    lines.append("### Avoid this voice")
    lines.append("")
    for a in pv["avoid_this"]:
        lines.append(f"- {a}")
    lines.append("")
    lines.append("### Decoration-pruning tone")
    lines.append("")
    lines.append(pv["decoration_pruning_tone"])
    lines.append("")
    lines.append("### Paragraph test")
    lines.append("")
    lines.append(pv["paragraph_test_intro"])
    lines.append("")
    for i, q in enumerate(pv["paragraph_test"], start=1):
        lines.append(f"{i}. {q}")
    lines.append("")
    lines.append(pv["paragraph_test_footnote"])
    return "\n".join(lines)


# Slot → renderer function map
SLOT_RENDERERS = {
    "VOCAB_HIERARCHY_TABLE": render_vocab_hierarchy_table,
    "PUBLICATION_CAPTURE_DISPOSITIONS": render_publication_capture_dispositions,
    "CLAIM_STRENGTH_LABELS": render_claim_strength_labels,
    "AUDIT_LANE_FIELD_VOCABULARY": render_audit_lane_field_vocabulary,
    "MIGRATION_LEGACY_WORDING": render_migration_legacy_wording,
    "HISTORICAL_LANE_BOARD_LABELS": render_historical_lane_board_labels,
    "HISTORICAL_DISCOVERY_LOG_LABELS": render_historical_discovery_log_labels,
    "COLUMN_RULES": render_column_rules,
    "PROTOCOL_QUALIFIERS": render_protocol_qualifiers,
    "EVIDENCE_TERMS": render_evidence_terms,
    "HYPHENATION_RULES": render_hyphenation_rules,
    "STALE_NARRATIVE_ARCHIVAL": render_stale_narrative_archival,
    "TOPIC_LOCAL_LANGUAGE": render_topic_local_language,
    "PAPER_VOICE": render_paper_voice,
}


def render_template(template_text: str, data: dict) -> str:
    """Substitute {{SLOT}} markers in template with rendered content."""
    out = template_text
    for slot, renderer in SLOT_RENDERERS.items():
        marker = "{{" + slot + "}}"
        if marker in out:
            try:
                rendered = renderer(data)
            except Exception as e:
                raise SystemExit(f"FAIL: rendering slot {slot}: {e}")
            out = out.replace(marker, rendered)
    # Detect any unfilled slots.
    unfilled = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if unfilled:
        raise SystemExit(f"FAIL: unfilled slots remain: {sorted(set(unfilled))}")
    return out


def generated_header(yaml_hash: str) -> str:
    return (
        f"<!-- generated; do not edit by hand; "
        f"source: docs/repo/controlled_vocabulary.yaml hash={yaml_hash} -->\n"
    )


def render_cv(data: dict, yaml_hash: str) -> str:
    if not CV_TEMPLATE.exists():
        raise SystemExit(f"FAIL: {CV_TEMPLATE} missing")
    tpl = CV_TEMPLATE.read_text(encoding="utf-8")
    body = render_template(tpl, data)
    return generated_header(yaml_hash) + body


def render_kt(data: dict, yaml_hash: str) -> str:
    """KEY_TERMINOLOGY.md: passthrough template until Cleanup-1c.

    The A-Z index is not yet YAML-generated; the template is the current
    file content verbatim. The renderer's --check still ensures the file
    isn't hand-edited away from the template.
    """
    if not KT_TEMPLATE.exists():
        raise SystemExit(f"FAIL: {KT_TEMPLATE} missing")
    tpl = KT_TEMPLATE.read_text(encoding="utf-8")
    return generated_header(yaml_hash) + tpl


def diff_status(rendered: str, on_disk_path: Path) -> tuple[bool, str]:
    """Returns (drift_detected, summary)."""
    if not on_disk_path.exists():
        return True, f"{on_disk_path}: missing"
    actual = on_disk_path.read_text(encoding="utf-8")
    if rendered == actual:
        return False, f"{on_disk_path}: clean"
    return True, f"{on_disk_path}: drift detected"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render docs/repo/CONTROLLED_VOCABULARY.md and docs/KEY_TERMINOLOGY.md from controlled_vocabulary.yaml + templates."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to memory; compare to on-disk. Exit non-zero on drift. Do not modify files.",
    )
    args = parser.parse_args()

    data = load_yaml()
    yaml_hash = yaml_sha256()
    rendered_cv = render_cv(data, yaml_hash)
    rendered_kt = render_kt(data, yaml_hash)

    if args.check:
        drifted = False
        for rendered, out_path in [(rendered_cv, CV_OUT), (rendered_kt, KT_OUT)]:
            d, msg = diff_status(rendered, out_path)
            print(f"  {msg}")
            drifted = drifted or d
        if drifted:
            print(
                "render --check: drift detected. Run "
                "`python3 scripts/render_controlled_vocabulary.py` and commit the result.",
                file=sys.stderr,
            )
            return 1
        print("render --check: clean")
        return 0

    CV_OUT.write_text(rendered_cv, encoding="utf-8")
    KT_OUT.write_text(rendered_kt, encoding="utf-8")
    print(f"rendered {CV_OUT.relative_to(REPO_ROOT)}")
    print(f"rendered {KT_OUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
