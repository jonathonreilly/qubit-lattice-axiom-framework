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

Generation is extraction, not assertion
---------------------------------------
Nothing inside a generated block is authored here. Every sentence is a span
lifted out of a registered source document, located *structurally*:

1. *Axiom spans.* The axiom roster is read from the memo's ``Purpose`` list;
   each axiom's own section is then located by heading (``<Name> / ...``) and
   its whole body is extracted, followed by the memo's ``Qualification`` and
   ``Open Gates Outside The Axioms`` sections. Because the span is the whole
   section body, ANY edit inside it changes the rendered bytes and therefore
   fails ``--check`` until regeneration propagates it into every target.

2. *Primitive spans.* For every primitive registered in
   ``axiom_premise_nodes.json``, the ``What This Declares`` and ``What This Does
   Not Do`` sections of that node's ``current_path`` note are extracted whole.
   Those two sections are the primitive's grant and its boundary statement.

3. *Mechanical connective text only.* The generator supplies the label lines
   (which are the source headings themselves), the source paths, and one
   sentence of framing. It supplies no paraphrase: the four skills no longer
   restate the baseline in their own voice inside the block. Per-file framing
   and per-file instructions live OUTSIDE the block, where the file owns them.

4. *Mechanical normalizations, and only these:* whitespace is collapsed and
   re-wrapped to width 79 (a hand-wrapped compound word is rejoined without a
   space); ``[text](target)`` inline links are flattened to ``text`` so an
   extracted relative link cannot become a broken link in the consuming file; a
   fenced code block is inlined as a code span. Text is otherwise byte-preserved.

5. *The acknowledgment manifest.* Whole-file and per-section digests of the
   axiom memo, the registry, and every registered primitive note. An edit to a
   source region that no span extracts still changes the manifest, so
   ``--check`` fails until a human reruns the generator. The manifest is an
   acknowledgment of the source, never a substitute for propagation -- see the
   invariant below.

DIGEST/PROPAGATION INVARIANT
----------------------------
A stored source digest is written ONLY in a run that has already written every
target's regenerated block to disk and re-read it back byte-identical. If any
target cannot be written or verified, the manifest keeps its previous digests,
so the next ``--check`` still fails on the unpropagated source edit. A digest
refresh can therefore never be used as a substitute for propagation. Enforced
in ``run()`` and tested directly by
``tests/test_skill_axiom_baselines.py::DigestPropagationInvariantTest``.

Roster discipline: every primitive registered in ``axiom_premise_nodes.json`` is
rendered inside every target's generated block (``verify_block_covers_roster``
refuses to emit a block that does not), and ``missing_roster_coverage``
independently re-checks that each target *file* carries that primitive's
extracted grant and boundary text as *visible* prose -- HTML comments and other
commented-out regions are stripped before the check, so a bare node id or a
commented mention is never accepted as coverage. Registering a new primitive
therefore fails ``--check`` until every skill carries the new primitive's own
grant and boundary sentences.

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

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_REL = "docs/audit/data/axiom_premise_nodes.json"
MANIFEST_REL = "docs/audit/data/skill_axiom_baseline_manifest.json"
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
GENERATOR_NAME = "generate_skill_axiom_baselines.py"

AXIOM_NODE_ID = "minimal_axioms"
BEGIN_MARKER = f"<!-- BEGIN GENERATED: axiom-baseline ({GENERATOR_NAME}) -->"
END_MARKER = "<!-- END GENERATED -->"
WRAP_WIDTH = 79

# The axiom roster is read from the memo, not asserted here; this constant only
# makes a rename/addition/removal a loud governance event rather than a silent
# re-render of a differently named foundation.
EXPECTED_AXIOM_ROSTER = ["Lattice", "Qubit", "Admissibility", "Record"]

# Headings addressed structurally in the axiom memo. The per-axiom sections are
# located from the roster itself; these two are named because they carry the
# memo's own downstream/qualification content.
QUALIFICATION_SECTION = "Qualification"
OPEN_GATES_SECTION = "Open Gates Outside The Axioms"

# Headings addressed structurally in every registered primitive's source note:
# the grant and the boundary statement.
PRIMITIVE_GRANT_SECTION = "What This Declares"
PRIMITIVE_BOUNDARY_SECTION = "What This Does Not Do"

SPAN_AXIOMS = "axioms"
SPAN_PRIMITIVES = "primitives"


class SourceDrift(RuntimeError):
    """A source doc no longer has the structure the extraction addresses."""


# --------------------------------------------------------------------------
# Text mechanics
# --------------------------------------------------------------------------

BULLET_RE = re.compile(r"^\s*[-*]\s+(.*)$")
FENCE_RE = re.compile(r"^\s*```")
LINK_RE = re.compile(r"\[([^\]\[]+)\]\([^()\s]*\)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def norm(text: str) -> str:
    """Collapse all whitespace runs to single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def join_source_lines(lines: list[str]) -> str:
    """Join hand-wrapped source lines back into one logical line.

    Source notes are hand-wrapped, so a compound word can be split across a line
    break (``explicit approved-\\nprimitive registration``). Re-joining with a
    space would silently corrupt the extracted word, so a line that ends in a
    single word-internal hyphen is joined to a following lowercase word without
    one. Every other join inserts a space.
    """
    out = ""
    for raw in lines:
        piece = raw.strip()
        if not piece:
            continue
        if not out:
            out = piece
            continue
        if re.search(r"(?<![-\s])-$", out) and re.match(r"[a-z]", piece):
            out += piece
        else:
            out += " " + piece
    return out


def delink(text: str) -> str:
    """Flatten ``[text](target)`` to ``text``.

    Extracted spans are re-rendered inside other files, where a relative link
    target from the source note would resolve to a path that does not exist.
    Flattening keeps the sentence verbatim and keeps the consuming file's links
    honest; the block cites the source path directly instead.
    """
    previous = None
    while previous != text:
        previous = text
        text = LINK_RE.sub(r"\1", text)
    return text


def strip_html_comments(text: str) -> str:
    """Drop every HTML comment so commented-out text is not read as prose."""
    return HTML_COMMENT_RE.sub(" ", text)


def visible_text(text: str) -> str:
    """Normalized, comment-free rendering of a file for coverage checks."""
    return norm(strip_html_comments(text))


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


@dataclass(frozen=True)
class Chunk:
    """One rendered unit of an extracted span."""

    kind: str  # "para" | "bullet" | "code"
    text: str


def parse_chunks(body: str, where: str) -> tuple[Chunk, ...]:
    """Split a raw section body into paragraphs, bullets, and inlined fences."""
    chunks: list[Chunk] = []
    buf: list[str] = []
    kind = "para"
    in_fence = False
    fence_buf: list[str] = []

    def flush() -> None:
        nonlocal buf, kind
        text = norm(join_source_lines(buf))
        if text:
            chunks.append(Chunk(kind, text))
        buf = []
        kind = "para"

    for line in body.splitlines():
        if FENCE_RE.match(line):
            if in_fence:
                flush()
                code = norm(" ".join(fence_buf))
                if code:
                    suffix = ""
                    while code and code[-1] in ",.;:":
                        suffix = code[-1] + suffix
                        code = code[:-1]
                    chunks.append(Chunk("code", f"`{code}`{suffix}"))
                fence_buf = []
                in_fence = False
            else:
                flush()
                in_fence = True
            continue
        if in_fence:
            fence_buf.append(line)
            continue
        if not line.strip():
            flush()
            continue
        bullet = BULLET_RE.match(line)
        if bullet:
            flush()
            kind = "bullet"
            buf = [bullet.group(1).strip()]
            continue
        buf.append(line.strip())
    flush()
    if in_fence:
        raise SourceDrift(f"{where}: unterminated code fence in an extracted span")
    return tuple(chunks)


def wrap_chunks(chunks: tuple[Chunk, ...], indent: str) -> list[str]:
    """Render chunks at ``indent``, blank-separated except inside a bullet run."""
    lines: list[str] = []
    previous: str | None = None
    for chunk in chunks:
        if previous is not None and not (previous == "bullet" == chunk.kind):
            lines.append("")
        if chunk.kind == "bullet":
            lines.extend(
                textwrap.wrap(
                    chunk.text,
                    width=WRAP_WIDTH,
                    initial_indent=indent + "- ",
                    subsequent_indent=indent + "  ",
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
        else:
            lines.extend(
                textwrap.wrap(
                    chunk.text,
                    width=WRAP_WIDTH,
                    initial_indent=indent,
                    subsequent_indent=indent,
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
        previous = chunk.kind
    return lines


# --------------------------------------------------------------------------
# Source loading (structural extraction)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Extract:
    """A span lifted verbatim out of one section of one source document."""

    source: str
    heading: str
    chunks: tuple[Chunk, ...]

    @property
    def normalized(self) -> str:
        """The span exactly as it renders, whitespace-normalized.

        Indent- and wrap-independent, so this is what a target file must carry
        for the span to count as covered.
        """
        return norm("\n".join(wrap_chunks(self.chunks, "")))


@dataclass
class Primitive:
    node_id: str
    path: str
    grant: Extract
    boundary: Extract


@dataclass
class AxiomSource:
    repo_root: Path
    axioms_path: str
    axiom_names: list[str]
    axiom_extracts: list[Extract]
    primitives: list[Primitive]
    source_texts: dict[str, str]

    @property
    def names_and(self) -> str:
        return oxford(self.axiom_names)


def oxford(items: list[str], conjunction: str = "and") -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"
    return ", ".join(items[:-1]) + f", {conjunction} {items[-1]}"


def read_source(repo_root: Path, rel_path: str, what: str) -> str:
    """Read a registered source, failing closed on anything unreadable."""
    path = repo_root / rel_path
    if not path.exists():
        raise SourceDrift(f"{what} missing on disk: {rel_path}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SourceDrift(f"{what} is unreadable ({rel_path}): {exc}") from exc


def extract_section(
    sections: dict[str, str], rel_path: str, heading: str, why: str
) -> Extract:
    if heading not in sections:
        raise SourceDrift(
            f"{rel_path}: section '{heading}' not found. {why} is extracted from "
            f"that section; a heading rename is a governance event -- restore the "
            f"heading or update the extraction plan in {GENERATOR_NAME}."
        )
    chunks = parse_chunks(delink(sections[heading]), f"{rel_path} / '{heading}'")
    if not chunks:
        raise SourceDrift(
            f"{rel_path}: section '{heading}' is empty, so {why} would render "
            f"nothing. Refusing to emit an empty baseline."
        )
    return Extract(source=rel_path, heading=heading, chunks=chunks)


def load_source(repo_root: Path) -> AxiomSource:
    registry_raw = read_source(repo_root, REGISTRY_REL, "premise registry")
    try:
        registry = json.loads(registry_raw)
    except json.JSONDecodeError as exc:
        raise SourceDrift(f"{REGISTRY_REL} is not valid JSON: {exc}") from exc

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

    source_texts: dict[str, str] = {REGISTRY_REL: registry_raw}

    axioms_text = read_source(repo_root, axioms_path, "registered axiom memo")
    source_texts[axioms_path] = axioms_text
    sections = split_sections(axioms_text)

    axiom_names = [
        name.strip()
        for name in re.findall(
            r"^\d+\.\s+\*\*([^*]+)\*\*\s*$",
            sections.get("Purpose", ""),
            re.MULTILINE,
        )
    ]
    if axiom_names != EXPECTED_AXIOM_ROSTER:
        raise SourceDrift(
            f"{axioms_path}: axiom roster is {axiom_names!r}, this generator is "
            f"registered for {EXPECTED_AXIOM_ROSTER!r}. An axiom rename/addition/"
            f"removal is a governance event: update EXPECTED_AXIOM_ROSTER in "
            f"{GENERATOR_NAME} deliberately, then regenerate."
        )

    axiom_extracts: list[Extract] = []
    for name in axiom_names:
        matches = [
            heading
            for heading in sections
            if heading == name or heading.startswith(f"{name} /")
        ]
        if len(matches) != 1:
            raise SourceDrift(
                f"{axioms_path}: expected exactly one section for axiom "
                f"'{name}' (heading '{name}' or '{name} / ...'), found "
                f"{sorted(matches)!r}."
            )
        axiom_extracts.append(
            extract_section(
                sections, axioms_path, matches[0], f"the {name} axiom baseline"
            )
        )
    for heading, why in (
        (QUALIFICATION_SECTION, "the axioms' qualification clause"),
        (OPEN_GATES_SECTION, "the memo's downstream/open-gate boundary"),
    ):
        axiom_extracts.append(
            extract_section(sections, axioms_path, heading, why)
        )

    primitives: list[Primitive] = []
    for node_id in canonical_ids:
        if node_id == AXIOM_NODE_ID:
            continue
        path = nodes[node_id].get("current_path")
        if not path:
            raise SourceDrift(
                f"{REGISTRY_REL}: '{node_id}' has no current_path, so its "
                f"boundary statement cannot be extracted."
            )
        note_text = read_source(
            repo_root, path, f"registered primitive note for '{node_id}'"
        )
        source_texts[path] = note_text
        note_sections = split_sections(note_text)
        primitives.append(
            Primitive(
                node_id=node_id,
                path=path,
                grant=extract_section(
                    note_sections,
                    path,
                    PRIMITIVE_GRANT_SECTION,
                    f"the grant statement for '{node_id}'",
                ),
                boundary=extract_section(
                    note_sections,
                    path,
                    PRIMITIVE_BOUNDARY_SECTION,
                    f"the boundary statement for '{node_id}'",
                ),
            )
        )
    if not primitives:
        raise SourceDrift(
            f"{REGISTRY_REL}: no approved primitives are registered; the roster "
            f"block would render nothing."
        )

    return AxiomSource(
        repo_root=repo_root,
        axioms_path=axioms_path,
        axiom_names=axiom_names,
        axiom_extracts=axiom_extracts,
        primitives=primitives,
        source_texts=source_texts,
    )


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


@dataclass
class Target:
    key: str
    path: str
    marker_indent: str
    # Which extracted spans this file's block renders. Selection is structural;
    # no target paraphrases a span it omits. Every target renders SPAN_PRIMITIVES
    # so that each registered primitive states its own boundary on every surface.
    spans: tuple[str, ...] = field(default_factory=tuple)


TARGETS: tuple[Target, ...] = (
    Target(
        key="physics-loop",
        path="docs/ai_methodology/skills/physics-loop/SKILL.md",
        marker_indent="",
        spans=(SPAN_AXIOMS, SPAN_PRIMITIVES),
    ),
    Target(
        key="review-loop",
        path="docs/ai_methodology/skills/review-loop/SKILL.md",
        marker_indent="",
        spans=(SPAN_AXIOMS, SPAN_PRIMITIVES),
    ),
    Target(
        key="audit-loop",
        path="docs/ai_methodology/skills/audit-loop/SKILL.md",
        marker_indent="  ",
        spans=(SPAN_AXIOMS, SPAN_PRIMITIVES),
    ),
    Target(
        key="registry-check",
        path="docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md",
        marker_indent="",
        spans=(SPAN_PRIMITIVES,),
    ),
)


def label_lines(text: str, indent: str) -> list[str]:
    return textwrap.wrap(
        text,
        width=WRAP_WIDTH,
        initial_indent=indent,
        subsequent_indent=indent,
        break_long_words=False,
        break_on_hyphens=False,
    )


def render_primitive(prim: Primitive, indent: str) -> list[str]:
    lines = label_lines(f"**`{prim.node_id}`** (source: `{prim.path}`)", indent)
    for extract in (prim.grant, prim.boundary):
        lines.append("")
        lines.extend(label_lines(f"*{extract.heading}*", indent))
        lines.append("")
        lines.extend(wrap_chunks(extract.chunks, indent))
    return lines


def render_block(src: AxiomSource, target: Target) -> list[str]:
    """Render one target's block. Only the framing sentence is authored here."""
    indent = target.marker_indent
    if not target.spans:
        raise SourceDrift(f"target '{target.key}' declares no spans to render")

    framing = (
        "Generated by `%s`: every paragraph below is extracted verbatim from the "
        "source section named in italics above it (whitespace re-wrapped, inline "
        "links flattened). The cited source file is the authority; do not "
        "hand-edit inside the markers." % GENERATOR_REL
    )
    lines = label_lines(framing, indent)

    if SPAN_AXIOMS in target.spans:
        lines.append("")
        lines.extend(
            label_lines(
                f"**Axiom baseline** (source: `{src.axioms_path}`; axioms: "
                f"{src.names_and})",
                indent,
            )
        )
        for extract in src.axiom_extracts:
            lines.append("")
            lines.extend(label_lines(f"*{extract.heading}*", indent))
            lines.append("")
            lines.extend(wrap_chunks(extract.chunks, indent))

    if SPAN_PRIMITIVES in target.spans:
        lines.append("")
        lines.extend(
            label_lines(
                f"**Approved primitives** (registry: `{REGISTRY_REL}`)", indent
            )
        )
        for prim in src.primitives:
            lines.append("")
            lines.extend(render_primitive(prim, indent))

    return lines


def render_all(src: AxiomSource) -> dict[str, list[str]]:
    return {target.key: render_block(src, target) for target in TARGETS}


# --------------------------------------------------------------------------
# Roster coverage
# --------------------------------------------------------------------------


def missing_roster_coverage(src: AxiomSource, text: str) -> list[tuple[str, Extract]]:
    """Registered primitives whose extracted spans are not visible in ``text``.

    Semantic, not nominal: the predicate is that the text carries the *content*
    of the grant and boundary statements extracted from the primitive's
    registered ``current_path`` note. HTML comments are stripped first, so a
    commented-out mention -- or a bare node id anywhere in the file -- is not
    coverage.
    """
    visible = visible_text(text)
    missing: list[tuple[str, Extract]] = []
    for prim in src.primitives:
        for extract in (prim.grant, prim.boundary):
            if extract.normalized not in visible:
                missing.append((prim.node_id, extract))
    return missing


def coverage_failure(where: str, node_id: str, extract: Extract) -> str:
    return (
        f"  FAIL {where}: registered primitive '{node_id}' does not carry the "
        f"'{extract.heading}' text extracted from `{extract.source}` as visible "
        f"prose\n"
        f"       (HTML comments and other commented-out regions do not count). "
        f"Every registered\n"
        f"       primitive must state what it grants and does not grant on every "
        f"skill surface.\n"
        f"       expected, normalized: {extract.normalized[:120]!r}..."
    )


def verify_block_covers_roster(src: AxiomSource, target: Target, block: list[str]) -> None:
    """The regenerated block itself must state every registered primitive.

    This is the generator-configuration check behind the roster promise: if a
    target's ``spans`` ever stop rendering the primitive roster, or a newly
    registered primitive is not reached by any span, the generator refuses to
    emit rather than relying on unmanaged prose elsewhere in the file.
    """
    missing = missing_roster_coverage(src, "\n".join(block))
    if missing:
        node_id, extract = missing[0]
        raise SourceDrift(
            f"target '{target.key}' ({target.path}) renders spans "
            f"{list(target.spans)}, which do not state the '{extract.heading}' "
            f"boundary of registered primitive '{node_id}' (`{extract.source}`). "
            f"Every target must render the primitive roster; fix the target's "
            f"spans in {GENERATOR_NAME}."
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

    extraction_plan: dict[str, list[str]] = {
        src.axioms_path: [extract.heading for extract in src.axiom_extracts]
    }
    for prim in src.primitives:
        extraction_plan.setdefault(prim.path, [])
        for extract in (prim.grant, prim.boundary):
            if extract.heading not in extraction_plan[prim.path]:
                extraction_plan[prim.path].append(extract.heading)

    targets: dict[str, dict] = {}
    for target in TARGETS:
        rendered = "\n".join(blocks[target.key]) + "\n"
        targets[target.path] = {
            "block_lines": len(blocks[target.key]),
            "block_sha256": sha256_text(rendered),
            "spans": list(target.spans),
        }

    return {
        "schema_version": 2,
        "generator": GENERATOR_REL,
        "axiom_roster": list(src.axiom_names),
        "axioms_path": src.axioms_path,
        "primitive_roster": [p.node_id for p in src.primitives],
        "extracted_sections": {
            path: sorted(headings) for path, headings in extraction_plan.items()
        },
        "sources": sources,
        "targets": targets,
    }


def manifest_bytes(manifest: dict) -> str:
    return json.dumps(manifest, indent=1, sort_keys=True) + "\n"


# --------------------------------------------------------------------------
# Drive
# --------------------------------------------------------------------------


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


def diff_report(path: str, committed: list[str], expected: list[str]) -> str:
    diff = difflib.unified_diff(
        [ln + "\n" for ln in committed],
        [ln + "\n" for ln in expected],
        fromfile=f"{path} (committed block)",
        tofile=f"{path} (regenerated)",
        lineterm="\n",
    )
    return "".join(diff)


def rebuild(original: str, target: Target, expected: list[str]) -> str:
    lines = original.splitlines()
    begin, end = find_block(lines, target)
    indent = target.marker_indent
    rebuilt_lines = (
        lines[:begin]
        + [indent + BEGIN_MARKER]
        + expected
        + [indent + END_MARKER]
        + lines[end + 1:]
    )
    return "\n".join(rebuilt_lines) + ("\n" if original.endswith("\n") else "")


def run(repo_root: Path, check_only: bool) -> int:
    src = load_source(repo_root)
    blocks = render_all(src)
    manifest = manifest_bytes(build_manifest(src, blocks))

    failures: list[str] = []
    for target in TARGETS:
        file_path = repo_root / target.path
        expected = blocks[target.key]
        # Generator-configuration check: the block we are about to emit must
        # itself state every registered primitive's grant and boundary.
        verify_block_covers_roster(src, target, expected)

        if not file_path.exists():
            failures.append(f"  FAIL {target.path}: file missing on disk")
            continue
        original = file_path.read_text(encoding="utf-8")
        begin, end = find_block(original.splitlines(), target)
        committed = original.splitlines()[begin + 1:end]
        rebuilt = rebuild(original, target, expected)

        if check_only:
            for node_id, extract in missing_roster_coverage(src, original):
                failures.append(coverage_failure(target.path, node_id, extract))
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
            continue

        if rebuilt != original:
            file_path.write_text(rebuilt, encoding="utf-8")
            print(f"  wrote {target.path} ({len(expected)} block lines)")
        else:
            print(f"  unchanged {target.path} ({len(expected)} block lines)")

        # Propagation proof: re-read what is now on disk. The manifest below is
        # written only if every target actually carries the regenerated span.
        written = file_path.read_text(encoding="utf-8")
        w_begin, w_end = find_block(written.splitlines(), target)
        if written.splitlines()[w_begin + 1:w_end] != expected:
            failures.append(
                f"  FAIL {target.path}: block on disk does not match the "
                f"regenerated block after writing"
            )
            continue
        for node_id, extract in missing_roster_coverage(src, written):
            failures.append(coverage_failure(target.path, node_id, extract))

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
    elif failures:
        # DIGEST/PROPAGATION INVARIANT: a source digest is refreshed only in a
        # run that propagated that source into every target. Leaving the stale
        # manifest in place keeps the next --check red on the source edit.
        print(
            f"  refusing to refresh {MANIFEST_REL}: propagation failed for at "
            f"least one target (see below). A digest refresh is never a "
            f"substitute for propagation."
        )
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
