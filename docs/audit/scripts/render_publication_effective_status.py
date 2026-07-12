#!/usr/bin/env python3
"""Render audit-derived effective-status views of publication tables.

For each table-style publication doc, walk every markdown link to a note
inside docs/, look up the cited note's audit row in audit_ledger.json,
and produce a parallel `<NAME>_EFFECTIVE_STATUS.md` view that annotates
each link with the audit-derived `effective_status` and `audit_status`.

Author-side prose (Status / claim columns) is preserved; audit verdict
is appended in `[ ]` brackets after each link.

Also emits PUBLICATION_AUDIT_DIVERGENCE.md, a single-page report listing
every cited note in publication tables whose audit-derived status is NOT
retained-grade. This is the work queue for "which retained claims aren't
actually retained yet."

Outputs (all under docs/publication/ci3_z3/):
  ARXIV_DRAFT_EFFECTIVE_STATUS.md
  CLAIMS_TABLE_EFFECTIVE_STATUS.md
  DERIVATION_ATLAS_EFFECTIVE_STATUS.md
  PUBLICATION_MATRIX_EFFECTIVE_STATUS.md
  FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md
  USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md
  RESULTS_INDEX_EFFECTIVE_STATUS.md
  QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md
  DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md
  PUBLICATION_AUDIT_DIVERGENCE.md

This script is mechanical and idempotent. Re-run via run_pipeline.sh.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS = REPO_ROOT / "docs"
PUB_DIR = DOCS / "publication" / "ci3_z3"
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
sys.path.insert(0, str(REPO_ROOT / "docs" / "audit" / "scripts"))
import premise_nodes

# Tables to render. Each entry: (source_basename, output_basename, scope_label)
TABLES = [
    ("ARXIV_DRAFT.md", "ARXIV_DRAFT_EFFECTIVE_STATUS.md",
     "public manuscript"),
    ("CLAIMS_TABLE.md", "CLAIMS_TABLE_EFFECTIVE_STATUS.md",
     "manuscript claim surface"),
    ("DERIVATION_ATLAS.md", "DERIVATION_ATLAS_EFFECTIVE_STATUS.md",
     "atlas of reusable derivations"),
    ("PUBLICATION_MATRIX.md", "PUBLICATION_MATRIX_EFFECTIVE_STATUS.md",
     "publication matrix"),
    ("FULL_CLAIM_LEDGER.md", "FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md",
     "full claim ledger"),
    ("USABLE_DERIVED_VALUES_INDEX.md", "USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md",
     "usable derived values index"),
    ("RESULTS_INDEX.md", "RESULTS_INDEX_EFFECTIVE_STATUS.md",
     "results index"),
    ("QUANTITATIVE_SUMMARY_TABLE.md", "QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md",
     "quantitative summary table"),
    ("DERIVATION_VALIDATION_MAP.md", "DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md",
     "derivation / validation map"),
]
DIVERGENCE_OUT = "PUBLICATION_AUDIT_DIVERGENCE.md"

# Match markdown links whose target ends in .md (with optional anchor)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s#]+\.md)(#[^)]*)?\)")

RETAINED_GRADE = {
    "retained",
    "retained_bounded",
    "retained_no_go",
}
AUDIT_BADGE_RE = re.compile(r"\[audit:([^\]]+)\]")
DERIVED_SAFETY_RE = re.compile(
    r"<!--AUDIT_DERIVED_(SAFE|UNSAFE|NEUTRAL|PREMISE)(?::([a-z0-9_.-]+))?-->"
)
DERIVED_SAFE = "<!--AUDIT_DERIVED_SAFE-->"
DERIVED_UNSAFE = "<!--AUDIT_DERIVED_UNSAFE-->"
DERIVED_NEUTRAL = "<!--AUDIT_DERIVED_NEUTRAL-->"
FOUNDATIONAL_ROW_ALLOWLIST = {
    (
        "CLAIMS_TABLE.md",
        "The named Lattice, Qubit, Admissibility, and Record axioms are the current minimal framework surface",
    ): {"minimal_axioms"},
    (
        "FULL_CLAIM_LEDGER.md",
        "The named Lattice, Qubit, Admissibility, and Record axioms are the current minimal framework surface",
    ): {"minimal_axioms"},
    ("PUBLICATION_MATRIX.md", "Framework"): {"minimal_axioms"},
    ("DERIVATION_ATLAS.md", "Framework axioms"): {"minimal_axioms"},
    (
        "DERIVATION_VALIDATION_MAP.md",
        "Lattice, Qubit, Admissibility, and Record form the current minimal axiom surface",
    ): {"minimal_axioms"},
    ("RESULTS_INDEX.md", "Framework / claim surface"): {"minimal_axioms"},
}
PROTECTED_INLINE_RE = re.compile(
    r"(\[[^\]]+\]\([^)]+\)|\[audit:[^\]]+\]|`[^`]*`)"
)


def strip_source_audit_annotations(body: str) -> str:
    """Remove badge-shaped source prose before adding ledger-derived badges."""
    body = DERIVED_SAFETY_RE.sub("", body)
    return AUDIT_BADGE_RE.sub("[source audit label ignored]", body)


def _neutralize_source_status_words(line: str) -> str:
    parts = PROTECTED_INLINE_RE.split(line)
    for index in range(0, len(parts), 2):
        parts[index] = re.sub(
            r"\b(?:retained(?:_bounded|_no_go|_pending_chain)?|promoted|"
            r"audited_(?:clean|conditional|renaming|decoration|failed|numerical_match)|"
            r"audit_in_progress|unaudited|open_gate)\b",
            "unratified-source-label",
            parts[index],
            flags=re.IGNORECASE,
        )
    return "".join(parts)


def demote_nonretained_table_rows(body: str, source_name: str | None = None) -> str:
    """Make audit-effective views impossible to read as retained prose.

    Source tables preserve author history. In the generated effective view,
    any table row citing at least one non-retained authority receives an
    explicit row marker and retained/promoted source labels are neutralized.
    """
    rendered: list[str] = []
    in_table = False
    data_row_index = 0
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            in_table = False
            data_row_index = 0
            rendered.append(line)
            continue
        if not in_table:
            in_table = True
            data_row_index = 0
        is_separator = bool(
            re.fullmatch(r"\s*\|(?:\s*:?-+:?\s*\|)+\s*", line)
        )
        is_header = data_row_index == 0
        data_row_index += 1
        if is_separator or is_header:
            rendered.append(line)
            continue
        safety = DERIVED_SAFETY_RE.findall(line)
        # Source-authored badge-shaped strings are stripped before annotation.
        # Retained-grade claim links make a row safe. Foundational premises are
        # dependency-satisfying, not downstream ratifications, so a premise-only
        # row is safe only on the exact controlled framework-row allowlist.
        kinds = [kind for kind, _ in safety]
        premise_ids = {claim_id for kind, claim_id in safety if kind == "PREMISE"}
        cells = line.split("|")
        first_cell = cells[1].strip() if len(cells) > 2 else ""
        allowed_premises = FOUNDATIONAL_ROW_ALLOWLIST.get(
            (source_name or "", first_cell)
        )
        premise_declaration = bool(
            premise_ids and allowed_premises == premise_ids
        )
        nonretained = (
            "UNSAFE" in kinds
            or not ("SAFE" in kinds or premise_declaration)
        )
        line = DERIVED_SAFETY_RE.sub("", line)
        if not nonretained:
            rendered.append(line)
            continue
        line = _neutralize_source_status_words(line)
        line = re.sub(
            r"^(\s*\|\s*)",
            r"\1**AUDIT-NONRETAINED ROW** — ",
            line,
            count=1,
        )
        rendered.append(line)
    return "\n".join(rendered) + ("\n" if body.endswith("\n") else "")


def strip_non_table_narrative(body: str) -> str:
    """Generated table views must not publish unbadged author prose."""
    rendered: list[str] = []
    omitted = False
    section_index = 0
    for line in body.splitlines():
        keep = (
            not line.strip()
            or line.lstrip().startswith("#")
            or line.lstrip().startswith("|")
        )
        if keep:
            if omitted:
                rendered.append(
                    "> **Author-side narrative omitted from this audit-derived view.**"
                )
                rendered.append("")
                omitted = False
            if line.lstrip().startswith("##"):
                section_index += 1
                hashes = line[: len(line) - len(line.lstrip("#"))]
                rendered.append(
                    f"{hashes} Audit-badged section {section_index}"
                )
            else:
                rendered.append(line)
        else:
            omitted = True
    if omitted:
        rendered.append(
            "> **Author-side narrative omitted from this audit-derived view.**"
        )
    return "\n".join(rendered) + ("\n" if body.endswith("\n") else "")


def load_ledger() -> dict[str, dict]:
    if not LEDGER_PATH.exists():
        raise SystemExit(f"FATAL: {LEDGER_PATH} missing; run pipeline first")
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))


def index_by_path(rows: dict[str, dict]) -> dict[Path, tuple[str, dict]]:
    out: dict[Path, tuple[str, dict]] = {}
    for cid, r in rows.items():
        np = r.get("note_path") or ""
        if not np:
            continue
        try:
            out[(REPO_ROOT / np).resolve()] = (cid, r)
        except Exception:
            continue
    return out


def resolve_link(target: str, source: Path) -> Path | None:
    """Replicate the citation-graph builder's resolver semantics: handle
    legacy absolute paths via the /docs/ marker; URL-decode."""
    decoded = urllib.parse.unquote(target)
    if decoded.startswith("/"):
        marker = "/docs/"
        idx = decoded.find(marker)
        if idx < 0:
            return None
        candidate = (DOCS / decoded[idx + len(marker):]).resolve()
    else:
        candidate = (source.parent / decoded).resolve()
    return candidate


def status_badge(eff: str | None, ast: str | None) -> str:
    """Compact one-cell badge for inline annotation."""
    eff = eff or "?"
    ast = ast or "?"
    if eff in RETAINED_GRADE:
        return f"[audit:{eff}]"
    if eff.startswith("decoration_under_"):
        return f"[audit:{eff}]"
    if eff == "retained_pending_chain":
        return f"[audit:retained_pending_chain]"
    if eff == "meta":
        return f"[audit:meta]"
    if eff == "open_gate":
        return f"[audit:open_gate]"
    return f"[audit:{eff}]"


def annotate_links(body: str, source: Path,
                   by_path: dict[Path, tuple[str, dict]]) -> tuple[str, list[dict]]:
    """Append a status badge after every markdown link to a docs/ note.
    Returns the rewritten body and a list of per-link audit lookups."""
    lookups: list[dict] = []

    def repl(m: re.Match[str]) -> str:
        whole = m.group(0)
        target = m.group(2)
        resolved = resolve_link(target, source)
        if resolved is None:
            return whole
        try:
            resolved.relative_to(DOCS)
        except ValueError:
            return whole
        match = by_path.get(resolved)
        if not match:
            relative = str(resolved.relative_to(REPO_ROOT))
            if relative == "docs/repo/FRONT_DOOR_STATUS.md":
                return f"{whole}&nbsp;{DERIVED_NEUTRAL}[audit:control-plane]"
            lookups.append({
                "claim_id": None,
                "note_path": relative,
                "audit_status": None,
                "effective_status": "unresolved",
                "criticality": None,
            })
            return f"{whole}&nbsp;{DERIVED_UNSAFE}[audit:unresolved]"
        cid, row = match
        eff = row.get("effective_status")
        ast = row.get("audit_status")
        crit = row.get("criticality")
        lookups.append({
            "claim_id": cid,
            "note_path": str(resolved.relative_to(REPO_ROOT)),
            "audit_status": ast,
            "effective_status": eff,
            "criticality": crit,
            "accepted_premise": premise_nodes.is_axiom_premise(cid),
        })
        badge = status_badge(eff, ast)
        is_premise = premise_nodes.is_axiom_premise(cid)
        safe = eff in RETAINED_GRADE or (
            isinstance(eff, str) and eff.startswith("decoration_under_")
        )
        # Append the badge AFTER the link, with a thin space
        if is_premise:
            marker = f"<!--AUDIT_DERIVED_PREMISE:{cid}-->"
        else:
            marker = DERIVED_SAFE if safe else DERIVED_UNSAFE
        return f"{whole}&nbsp;{marker}{badge}"

    new_body = LINK_RE.sub(repl, body)
    return new_body, lookups


def render_table(source_name: str, output_name: str, scope_label: str,
                 by_path: dict[Path, tuple[str, dict]],
                 generated_label: str) -> tuple[Path | None, list[dict]]:
    src = PUB_DIR / source_name
    if not src.exists():
        return None, []
    body = strip_source_audit_annotations(src.read_text(encoding="utf-8"))
    annotated, lookups = annotate_links(body, src, by_path)
    if source_name == "ARXIV_DRAFT.md":
        counts: dict[str, int] = {}
        manuscript_rows = {
            lookup["claim_id"]: lookup for lookup in lookups
        }
        for lookup in manuscript_rows.values():
            status = str(lookup.get("effective_status") or "unaudited")
            counts[status] = counts.get(status, 0) + 1
        annotated = (
            "## Current audit-derived manuscript gateway\n\n"
            "The author-side manuscript is intentionally **not reproduced** in "
            "this public gateway because prose-level labels cannot override the "
            "claim ledger. Counts below cover unique claims linked directly by "
            "the author manuscript. Use the generated surfaces below; any claim absent "
            "from a retained-grade row remains non-retained.\n\n"
            f"- `retained`: {counts.get('retained', 0)}\n"
            f"- `retained_bounded`: {counts.get('retained_bounded', 0)}\n"
            f"- `retained_no_go`: {counts.get('retained_no_go', 0)}\n"
            f"- `unaudited`: {counts.get('unaudited', 0)}\n\n"
            "Author source: [ARXIV_DRAFT.md](ARXIV_DRAFT.md) "
            "(non-authoritative narrative).\n\n"
            "Audit-derived claim surfaces: "
            "[CLAIMS_TABLE_EFFECTIVE_STATUS.md](CLAIMS_TABLE_EFFECTIVE_STATUS.md), "
            "[DERIVATION_ATLAS_EFFECTIVE_STATUS.md](DERIVATION_ATLAS_EFFECTIVE_STATUS.md), "
            "[RESULTS_INDEX_EFFECTIVE_STATUS.md](RESULTS_INDEX_EFFECTIVE_STATUS.md), "
            "and [PUBLICATION_AUDIT_DIVERGENCE.md](PUBLICATION_AUDIT_DIVERGENCE.md).\n"
        )
        lookups = []
    else:
        annotated = strip_non_table_narrative(
            demote_nonretained_table_rows(annotated, source_name=source_name)
        )

    if source_name == "ARXIV_DRAFT.md":
        view_description = (
            f"**Auto-generated.** This is the audit-derived public gateway for "
            f"[`{source_name}`]({source_name}); it deliberately withholds the "
            "non-authoritative narrative and routes readers to generated claim "
            "surfaces. Edit the source file; this gateway refreshes via "
            "`docs/audit/scripts/run_pipeline.sh`.\n\n"
        )
    else:
        view_description = (
            f"**Auto-generated.** This is a parallel view of "
            f"[`{source_name}`]({source_name}) with each linked note annotated "
            f"with its audit-derived `effective_status` badge `[audit:STATUS]`. "
            "Edit the source file; this view refreshes via "
            "`docs/audit/scripts/run_pipeline.sh`.\n\n"
        )
    header = (
        f"<!-- AUTO-GENERATED by docs/audit/scripts/render_publication_effective_status.py -->\n"
        f"<!-- Source: {source_name}  generated: {generated_label} -->\n"
        f"<!-- DO NOT EDIT THIS FILE BY HAND. Edit the source above; this view auto-refreshes. -->\n\n"
        f"# {scope_label.title()} - Audit-Derived Effective-Status View\n\n"
        f"{view_description}"
        f"**Retained-grade values:** `retained`, `retained_bounded`, `retained_no_go`. "
        f"Anything else means the audit lane has NOT confirmed the claim, regardless of "
        f"the author-side status text in the row.\n\n"
        f"---\n\n"
    )

    out_path = PUB_DIR / output_name
    out_path.write_text(header + annotated, encoding="utf-8")
    return out_path, lookups


def render_divergence(all_lookups: dict[str, list[dict]],
                      generated_label: str) -> Path:
    """Build a single divergence report: every distinct (table, note) pair
    whose audit verdict is NOT retained-grade."""
    distinct_non_retained: dict[str, dict] = {}  # claim_id -> row
    for table, lookups in all_lookups.items():
        for L in lookups:
            eff = L.get("effective_status") or ""
            if eff in RETAINED_GRADE or eff.startswith("decoration_under_") or eff == "meta":
                continue
            cid = L.get("claim_id")
            row_key = cid or f"unresolved:{L['note_path']}"
            entry = distinct_non_retained.setdefault(row_key, {
                "claim_id": row_key,
                "note_path": L["note_path"],
                "effective_status": eff,
                "audit_status": L.get("audit_status"),
                "criticality": L.get("criticality"),
                "appearing_in": set(),
            })
            entry["appearing_in"].add(table)

    rows = sorted(distinct_non_retained.values(),
                  key=lambda r: (
                      0 if r["criticality"] == "critical" else
                      1 if r["criticality"] == "high" else
                      2 if r["criticality"] == "medium" else 3,
                      r["claim_id"],
                  ))

    lines: list[str] = []
    lines.append("<!-- AUTO-GENERATED by docs/audit/scripts/render_publication_effective_status.py -->")
    lines.append(f"<!-- generated: {generated_label} -->\n")
    lines.append("# Publication Audit Divergence Report")
    lines.append("")
    lines.append(f"**Auto-generated.** Every distinct cited note in any tracked")
    lines.append(f"publication table whose audit-derived `effective_status` is NOT")
    lines.append(f"retained-grade. This is the work queue for closing the gap between")
    lines.append(f"author-side claim language and audit-lane verdicts.\n")
    lines.append(f"**Retained-grade values:** `retained`, `retained_bounded`, `retained_no_go`,")
    lines.append(f"plus `decoration_under_*` (boxed under retained parent). Anything else")
    lines.append(f"means the audit has not confirmed the claim, regardless of how the")
    lines.append(f"publication tables phrase it.\n")
    lines.append(f"## Summary by criticality\n")

    by_crit_eff: dict[tuple[str, str], int] = {}
    for r in rows:
        key = (r["criticality"] or "?", r["effective_status"] or "?")
        by_crit_eff[key] = by_crit_eff.get(key, 0) + 1

    lines.append("| criticality | effective_status | count |")
    lines.append("|---|---|---:|")
    for (c, e), n in sorted(by_crit_eff.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {c} | `{e}` | {n} |")
    lines.append("")
    lines.append(f"**Total non-retained-grade rows in publication tables:** {len(rows)}\n")
    lines.append("## Per-row breakdown\n")
    lines.append("| criticality | claim_id | effective_status | audit_status | appearing in |")
    lines.append("|---|---|---|---|---|")
    for r in rows:
        tables = ", ".join(sorted(r["appearing_in"]))
        lines.append(
            f"| {r['criticality'] or '?'} | "
            f"`{r['claim_id']}` | "
            f"`{r['effective_status'] or '?'}` | "
            f"`{r['audit_status'] or '?'}` | "
            f"{tables} |"
        )

    out_path = PUB_DIR / DIVERGENCE_OUT
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def main() -> int:
    missing_sources = [src for src, _, _ in TABLES if not (PUB_DIR / src).exists()]
    if missing_sources:
        print(
            "FATAL: publication effective-status sources missing: "
            + ", ".join(missing_sources),
            file=sys.stderr,
        )
        return 2
    ledger = load_ledger()
    rows = ledger.get("rows", {})
    by_path = index_by_path(rows)
    generated_label = "pipeline-derived"

    all_lookups: dict[str, list[dict]] = {}
    rendered: list[Path] = []
    for src, out, scope in TABLES:
        result, lookups = render_table(src, out, scope, by_path, generated_label)
        if result is None:  # guarded by the all-source preflight above
            raise RuntimeError(f"publication source disappeared during render: {src}")
        all_lookups[src] = lookups
        rendered.append(result)
        print(f"  rendered {result.relative_to(REPO_ROOT)}  ({len(lookups)} link annotations)")

    div = render_divergence(all_lookups, generated_label)
    print(f"  wrote    {div.relative_to(REPO_ROOT)}")
    print(f"\nDone. {len(rendered)} effective-status views + 1 divergence report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
