#!/usr/bin/env python3
"""Inference audit linter for physics-loop cycles.

The prior-art sweep (step 2) fixed duplication because it is a MECHANICAL
pre-freeze check, not a resolution to remember. This linter is the same shape
for a different failure: claims that assert more than the arithmetic showed.

Every check below is derived from a defect that actually shipped to a value
gate in the 2026-07-25/26 campaign and was caught by a reviewer rather than by
the author. The `--selftest` mode re-runs the linter against those artifacts
and asserts it fires on each.

Usage:
    inference_audit_lint.py --runner R.py --note N.md
    inference_audit_lint.py --selftest CASES.json

Checks
------
SLICE       a test loop that narrows its own domain without justification.
            (cycle 707 row G: `hill = [1+f, -f]` then `for g in hill[:1]`,
            silently dropping the member whose derivative contradicted the
            row's own classification.)

CLONE       two functions with identical bodies modulo names, then "verified"
            to agree. (cycle 704: `can_form` and `can_migrate_into` written
            with the same body and scanned over 2187 rules.)

DIRECTION   a necessity/forcing word in a claim whose matching ledger row has
            no necessity-strength evidence in its `shown:` clause.
            (cycle 707 row F showed non-self-adjointness PERMITS a half-power
            and claimed half-powers REQUIRE it; cycle 702 showed the scale
            primitive SUPPLIES no dimensionless content and claimed it
            SELECTS zero.)

HYPOTHESIS  a named external theorem invoked without its hypotheses stated
            nearby. (cycle 707 invoked Rellich without its analyticity
            hypothesis, then called the conclusion unconditional.)

LEDGER      the note must carry the exact six-column claim-ledger schema with
            one row per claim and no empty cells. The columns are the ones that would have caught the
            remaining defects: `Support` empty catches an imported premise
            presented as framework content (cycle 705's `conf`); `Falsifier`
            empty catches a statement true by construction (cycle 701's
            symbol-disjointness).

Exit code 1 if any check fires.
"""

from __future__ import annotations

import argparse
import ast
import copy
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# Modal words that assert a direction stronger than "exhibited".
NECESSITY = re.compile(
    r"\b(requires?|required|only if|forces?|forced|necessary|must be|"
    r"cannot be|unreachable|impossible|uniquely|selects?)\b",
    re.I,
)

# External results whose hypotheses are routinely dropped when cited.  Match
# theorem identities, not surname substrings: "Noether" is not
# "Skolem--Noether", and the orbit-counting Burnside lemma is not Burnside's
# irreducible-matrix-algebra theorem.
NAMED_THEOREMS = (
    ("rellich", re.compile(r"\brellich(?:'s)?(?:\s+theorem)?\b", re.I),
     ("analytic", "self-adjoint")),
    ("kato", re.compile(r"\bkato(?:'s)?(?:\s+theorem)?\b", re.I),
     ("analytic", "self-adjoint")),
    ("gleason", re.compile(r"\bgleason(?:'s)?(?:\s+theorem)?\b", re.I),
     ("dimension", "frame")),
    ("busch", re.compile(r"\bbusch(?:'s)?(?:\s+theorem)?\b", re.I),
     ("effect", "frame")),
    (
        "burnside orbit-counting lemma",
        re.compile(
            r"\bburnside(?:'s)?\s+(?:lemma|orbit[- ]counting"
            r"(?:\s+(?:lemma|theorem))?)\b",
            re.I,
        ),
        ("finite group", "orbit"),
    ),
    (
        "hellmann-feynman",
        re.compile(r"\bhellmann(?:[-\N{EN DASH}\N{EM DASH} ]feynman)?\b", re.I),
        ("eigenvector", "normalized"),
    ),
    (
        "orbit-stabilizer",
        re.compile(r"\borbit[-\N{EN DASH}\N{EM DASH} ]stabilizer\b", re.I),
        ("finite", "group action"),
    ),
    (
        "variational noether",
        re.compile(
            r"(?<![-\N{EN DASH}\N{EM DASH}])\bnoether(?:'s)?\s+"
            r"(?:theorem|identity)\b",
            re.I,
        ),
        ("continuous", "symmetry"),
    ),
    (
        "rayleigh-ritz",
        re.compile(r"\brayleigh(?:[-\N{EN DASH}\N{EM DASH} ]ritz)?\b", re.I),
        ("self-adjoint",),
    ),
)

SLICE_RE = re.compile(r"\[\s*:\s*-?\d+\s*\]|\[\s*-?\d+\s*:\s*\]|\bislice\(|\.head\(")
JUSTIFY_RE = re.compile(r"#.*\b(justif|because|why|deliberat|intentional|see )", re.I)


class Finding:
    def __init__(self, check: str, where: str, detail: str):
        self.check, self.where, self.detail = check, where, detail

    def __str__(self) -> str:
        return f"[{self.check}] {self.where}: {self.detail}"


@dataclass(frozen=True)
class InlineSource:
    """Path-like source used by deterministic, file-free self-test cases."""

    name: str
    text: str

    def read_text(self) -> str:
        return self.text

    def exists(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------------------
# runner checks
# ---------------------------------------------------------------------------


def _is_narrowing_slice(node: ast.AST) -> bool:
    """A subscript that drops elements: x[:n], x[n:], but not x[:] or a display."""
    if not isinstance(node, ast.Subscript) or not isinstance(node.slice, ast.Slice):
        return False
    sl = node.slice
    return (sl.lower is not None or sl.upper is not None) and sl.step is None


def check_slice(runner: Path) -> list[Finding]:
    """A slice in ITERATION position inside a check row, with no justification.

    Restricted to iteration position on purpose: a slice in a display string
    (`{sorted(...)[:4]}` in an f-string) truncates output, which is harmless,
    while a slice in a `for ... in xs[:1]` or `all(... for g in xs[:1])`
    silently shrinks the tested domain. An earlier regex version of this check
    flagged both and was too noisy to be worth running.
    """
    out: list[Finding] = []
    lines = runner.read_text().splitlines()
    try:
        tree = ast.parse("\n".join(lines))
    except SyntaxError as exc:
        return [Finding("PARSE", str(runner), f"cannot parse: {exc}")]

    for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
        src = "\n".join(lines[fn.lineno - 1 : (fn.end_lineno or fn.lineno)])
        if "check(" not in src:
            continue
        iterables: list[ast.AST] = []
        for node in ast.walk(fn):
            if isinstance(node, ast.For):
                iterables.append(node.iter)
            elif isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
                iterables.extend(g.iter for g in node.generators)
        # Exempt only verified adjacent-pair idioms.  The earlier implementation
        # exempted every sliced argument whose base also appeared unsliced, so
        # `zip(xs, xs[:1])` silently truncated a check and still passed.
        adjacent_pair_slices = set()

        def int_value(node):
            if isinstance(node, ast.Constant) and isinstance(node.value, int):
                return node.value
            if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)
                    and isinstance(node.operand, ast.Constant)
                    and isinstance(node.operand.value, int)):
                return -node.operand.value
            return None

        def is_tail_from_one(node):
            return (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Slice)
                and int_value(node.slice.lower) == 1
                and node.slice.upper is None
                and node.slice.step is None
            )

        def is_drop_last(node):
            return (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Slice)
                and node.slice.lower is None
                and int_value(node.slice.upper) == -1
                and node.slice.step is None
            )

        for it in iterables:
            for call in ast.walk(it):
                if (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                        and call.func.id == "zip" and len(call.args) >= 2):
                    unsliced = {
                        ast.dump(a) for a in call.args
                        if not isinstance(a, ast.Subscript)
                    }
                    tails = [a for a in call.args if is_tail_from_one(a)]
                    drops = [a for a in call.args if is_drop_last(a)]
                    for tail in tails:
                        base = ast.dump(tail.value)
                        if base in unsliced:
                            adjacent_pair_slices.add(id(tail))
                        for drop in drops:
                            if ast.dump(drop.value) == base:
                                adjacent_pair_slices.update((id(tail), id(drop)))

        for it in iterables:
            for sub in ast.walk(it):
                if id(sub) in adjacent_pair_slices:
                    continue
                if _is_narrowing_slice(sub):
                    ln = getattr(sub, "lineno", fn.lineno)
                    window = "\n".join(lines[max(0, ln - 4) : ln + 1])
                    if JUSTIFY_RE.search(window):
                        continue
                    out.append(
                        Finding(
                            "SLICE",
                            f"{runner.name}:{ln}",
                            f"in check row `{fn.name}`, `{lines[ln - 1].strip()}` iterates "
                            f"over a narrowed domain with no justifying comment; the "
                            f"dropped elements are untested",
                        )
                    )
    return out


def _normalize_body(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """Alpha-normalize local bindings while preserving semantic free names."""

    fn_copy = copy.deepcopy(fn)
    if (
        fn_copy.body
        and isinstance(fn_copy.body[0], ast.Expr)
        and isinstance(fn_copy.body[0].value, ast.Constant)
        and isinstance(fn_copy.body[0].value.value, str)
    ):
        fn_copy.body = fn_copy.body[1:]

    ordered: list[str] = []
    global_or_nonlocal: set[str] = set()

    def add(name: str | None) -> None:
        if name and name not in ordered:
            ordered.append(name)

    args = fn_copy.args
    for arg in [*args.posonlyargs, *args.args, *args.kwonlyargs]:
        add(arg.arg)
    if args.vararg:
        add(args.vararg.arg)
    if args.kwarg:
        add(args.kwarg.arg)

    class BindingCollector(ast.NodeVisitor):
        def visit_FunctionDef(self, node):  # noqa: N802
            return

        def visit_AsyncFunctionDef(self, node):  # noqa: N802
            return

        def visit_Lambda(self, node):  # noqa: N802
            return

        def visit_ClassDef(self, node):  # noqa: N802
            return

        def visit_Name(self, node):  # noqa: N802
            if isinstance(node.ctx, ast.Store):
                add(node.id)

        def visit_Import(self, node):  # noqa: N802
            for alias in node.names:
                add(alias.asname or alias.name.split(".", 1)[0])

        def visit_ImportFrom(self, node):  # noqa: N802
            for alias in node.names:
                add(alias.asname or alias.name)

        def visit_ExceptHandler(self, node):  # noqa: N802
            add(node.name)
            self.generic_visit(node)

        def visit_Global(self, node):  # noqa: N802
            global_or_nonlocal.update(node.names)

        def visit_Nonlocal(self, node):  # noqa: N802
            global_or_nonlocal.update(node.names)

    collector = BindingCollector()
    for statement in fn_copy.body:
        collector.visit(statement)
    ordered = [name for name in ordered if name not in global_or_nonlocal]
    mapping = {name: f"_local_{i}" for i, name in enumerate(ordered)}

    class LocalAlphaNormalizer(ast.NodeTransformer):
        def visit_Name(self, node):  # noqa: N802
            if node.id in mapping:
                return ast.copy_location(
                    ast.Name(id=mapping[node.id], ctx=node.ctx), node
                )
            return node

        def visit_arg(self, node):  # noqa: N802
            if node.arg in mapping:
                node.arg = mapping[node.arg]
            return self.generic_visit(node)

    fn_copy.name = "_function"
    normalized = LocalAlphaNormalizer().visit(fn_copy)
    ast.fix_missing_locations(normalized)
    return ast.dump(normalized, include_attributes=False)


def check_clone(runner: Path) -> list[Finding]:
    """Two differently-named functions with the same body."""
    out: list[Finding] = []
    try:
        tree = ast.parse(runner.read_text())
    except SyntaxError:
        return out
    seen: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            key = _normalize_body(node)
            if key in seen and seen[key] != node.name:
                out.append(
                    Finding(
                        "CLONE",
                        f"{runner.name}:{node.lineno}",
                        f"`{node.name}` has the same body as `{seen[key]}` modulo names; "
                        f"a row comparing them cannot fail",
                    )
                )
            else:
                seen[key] = node.name
    return out


# ---------------------------------------------------------------------------
# note checks
# ---------------------------------------------------------------------------


def _sentences(text: str) -> list[tuple[int, str]]:
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith(("|", "```", ">")):
            continue
        for s in re.split(r"(?<=[.;:])\s+", line):
            if s.strip():
                out.append((i, s.strip()))
    return out


CLAIM_SECTION = re.compile(
    r"^#{1,3}\s*(answer|claim|result|summary|discussion|consequence|why|"
    r"what this (shows|establishes)|the no.go|obstruction|"
    r"cannot close|does not close)",
    re.I,
)
ANY_HEADING = re.compile(r"^#{1,6}\s")


def _claim_positions(text: str) -> set[int]:
    """Line numbers where a claim is asserted rather than a proof step taken.

    Scoped deliberately: the title, any `**Theorem ...**` statement, and
    sections whose heading names a claim (Answer, Result, Summary, ...).
    Proof bodies are excluded -- a necessity word inside a proof is a step
    justified by the surrounding argument, and flagging those made the check
    too noisy to run (9 findings on one note, 7 of them proof internals).
    """
    lines = text.splitlines()
    out: set[int] = set()
    in_claim = False
    for i, line in enumerate(lines, 1):
        if i == 1:
            out.add(i)
        if ANY_HEADING.match(line):
            in_claim = bool(CLAIM_SECTION.match(line))
            continue
        if in_claim or "**Theorem" in line:
            out.add(i)
    return out


def _claim_words(text: str) -> list[str]:
    cleaned = re.sub(r"\*\*\s*thesis\s*\*\*", " ", text, flags=re.I)
    return re.findall(r"[a-z0-9]+", cleaned.lower())


def _claim_text_matches(left: str, right: str) -> bool:
    a = " ".join(_claim_words(left))
    b = " ".join(_claim_words(right))
    if not a or not b:
        return False
    if a in b or b in a:
        return True
    aset, bset = set(a.split()), set(b.split())
    shorter = min(len(aset), len(bset))
    if shorter == 0:
        return False
    required = min(3, shorter)
    return len(aset & bset) >= required and len(aset & bset) / shorter >= 0.8


DIRECTION_SUPPORT = re.compile(
    r"\b(requires?|forced?|necessary|must|cannot|does not exist|"
    r"no [^;]{0,80} exists|unreachable|impossible|unique(?:ly)?|selects?|"
    r"if and only if|iff|equivalent|converse)\b",
    re.I,
)
SHOWN_CLAUSE = re.compile(
    r"\bshown\s*:\s*(.*?)(?=(?:;|<br\s*/?>)\s*claimed\s*:|$)",
    re.I,
)


def check_direction(note: Path, ledger: str) -> list[Finding]:
    """Necessity claims need a matching row whose shown clause supports it."""
    out: list[Finding] = []
    text = note.read_text()
    claim_lines = _claim_positions(text)
    rows = list(_ledger_rows(ledger))
    for lineno, sent in _sentences(text):
        if lineno not in claim_lines:
            continue
        m = NECESSITY.search(sent)
        if not m:
            continue
        matching = [cells for cells in rows if _claim_text_matches(sent, cells[1])]
        supported = False
        for cells in matching:
            shown_match = SHOWN_CLAUSE.search(cells[4])
            if shown_match and DIRECTION_SUPPORT.search(shown_match.group(1)):
                supported = True
                break
        if supported:
            continue
        reason = (
            "no matching claim-ledger row"
            if not matching
            else "the matching row's `shown:` clause records no converse, "
                 "equivalence, uniqueness, impossibility, or other necessity-strength evidence"
        )
        out.append(
            Finding(
                "DIRECTION",
                f"{note.name}:{lineno}",
                f'asserts "{m.group(0)}" but {reason}: \"{sent[:70]}...\"',
            )
        )
    return out


def check_hypothesis(note: Path) -> list[Finding]:
    """A named theorem must have its hypotheses within 400 chars of the mention."""
    out: list[Finding] = []
    text = note.read_text()
    low = text.lower()
    for name, pattern, hyps in NAMED_THEOREMS:
        for m in pattern.finditer(text):
            window = low[max(0, m.start() - 400) : m.start() + 400]
            missing = [h for h in hyps if h not in window]
            if missing:
                line = text[: m.start()].count("\n") + 1
                out.append(
                    Finding(
                        "HYPOTHESIS",
                        f"{note.name}:{line}",
                        f"invokes `{name}` without stating hypotheses {missing} nearby",
                    )
                )
    return out


LEDGER_HEADERS = (
    "id",
    "claim",
    "support",
    "hypotheses",
    "shown vs claimed",
    "falsifier",
)


def _split_markdown_row(line: str) -> list[str]:
    """Split a Markdown table row on unescaped pipes."""

    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith(r"\|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    buf: list[str] = []
    escaped = False
    for char in stripped:
        if escaped:
            buf.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(char)
    if escaped:
        buf.append("\\")
    cells.append("".join(buf).strip())
    return cells


def _is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells
    )


def check_ledger(note: Path) -> tuple[list[Finding], str]:
    """The note must carry a complete claim ledger."""
    text = note.read_text()
    out: list[Finding] = []
    lines = text.splitlines()
    header_at = None
    header_cells: list[str] = []
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = _split_markdown_row(line)
        lowered = tuple(cell.lower() for cell in cells)
        if lowered[:3] == LEDGER_HEADERS[:3]:
            header_at = index
            header_cells = cells
            break
    if header_at is None:
        return (
            [
                Finding(
                    "LEDGER",
                    note.name,
                    "no claim ledger found; expected a table with columns "
                    "`| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |`",
                )
            ],
            "",
        )
    if tuple(cell.lower() for cell in header_cells) != LEDGER_HEADERS:
        out.append(
            Finding(
                "LEDGER",
                f"{note.name}:{header_at + 1}",
                "malformed claim-ledger header; expected exactly "
                "`| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |`",
            )
        )
        return out, ""

    rows: list[tuple[int, list[str]]] = []
    ledger_text: list[str] = []
    separator_seen = False
    for index in range(header_at + 1, len(lines)):
        line = lines[index]
        if not line.strip().startswith("|"):
            break
        cells = _split_markdown_row(line)
        if _is_separator_row(cells):
            ledger_text.append(line)
            separator_seen = True
            if len(cells) != len(LEDGER_HEADERS):
                out.append(
                    Finding(
                        "LEDGER",
                        f"{note.name}:{index + 1}",
                        "claim-ledger separator does not have exactly six cells",
                    )
                )
            continue
        ledger_text.append(line)
        if len(cells) != len(LEDGER_HEADERS):
            out.append(
                Finding(
                    "LEDGER",
                    f"{note.name}:{index + 1}",
                    f"claim-ledger row has {len(cells)} cells; exactly six are required "
                    "and literal pipes inside cells must be escaped as `\\|`",
                )
            )
            continue
        rows.append((index + 1, cells))
    if not separator_seen:
        out.append(Finding("LEDGER", note.name, "claim ledger has no separator row"))
    if not rows:
        out.append(Finding("LEDGER", note.name, "claim ledger has no rows"))
    for lineno, cells in rows:
        for j, cell in enumerate(cells):
            if cell in ("", "-", "n/a", "N/A", "TBD", "?"):
                out.append(
                    Finding(
                        "LEDGER",
                        f"{note.name}:{lineno}",
                        f"claim ledger column {j + 1} is empty for row `{cells[0]}`; "
                        f"an empty Support means the claim rests on nothing shown, and "
                        f"an empty Falsifier means it is true by construction",
                    )
                )
    return out, "\n".join(ledger_text)



QUALIFIER = re.compile(
    r"\b(conditional|conditionally|given|assuming|granted|under|subject to|"
    r"modulo|premise|supplied|imported|unforced)\b",
    re.I,
)
SUPPLIED_TAG = re.compile(r"\[supplied\]", re.I)
SATISFIED_TAG = re.compile(r"\[satisfied\]", re.I)
THESIS_MARKER = re.compile(r"\*\*\s*thesis\s*\*\*", re.I)
TAGGED_HYPOTHESIS = re.compile(
    r"^(?:\*\*)?\[(supplied|satisfied)\](?:\*\*)?(?:\s|$)",
    re.I,
)


def _ledger_rows(ledger: str):
    for row in ledger.splitlines():
        cells = _split_markdown_row(row)
        if _is_separator_row(cells):
            continue
        if len(cells) == len(LEDGER_HEADERS):
            yield cells


def _thesis_rows(ledger: str) -> list[list[str]]:
    return [
        cells for cells in _ledger_rows(ledger)
        if THESIS_MARKER.search(cells[1])
    ]


def check_headline(note: Path) -> list[Finding]:
    """A thesis resting on a SUPPLIED hypothesis needs a qualified title.

    This check exists because the first cycle run under the inference audit
    passed the audit and was still rejected for exactly the failure the audit
    was built to stop. The author recorded the load-bearing assumption in the
    Hypotheses cell and then titled the note as though it were not there. The
    reviewer's words: "Listing the family in the Hypotheses column does not
    cure the headline claim."

    Ledger completeness is necessary and not sufficient. Two refinements were
    needed after the first attempt at this check fired on a clean note and
    stayed silent on the rejected one:

    * only hypotheses tagged `[supplied]` count. A hypothesis satisfied by
      construction (`[satisfied]`, e.g. "finite group action") constrains
      nothing about the headline. The tag forces the author to make exactly the
      distinction whose absence caused the failure.
    * the qualifier must be in the TITLE, not anywhere in the Answer section.
      Scanning a long blob for "if" or "given" suppressed the check on every
      real note.
    """
    out: list[Finding] = []
    text = note.read_text()
    lines = text.splitlines()
    title = lines[0] if lines else ""

    _, ledger = check_ledger(note)
    supplied = [
        cells[0] for cells in _thesis_rows(ledger)
        if SUPPLIED_TAG.search(cells[3])
    ]
    if not supplied:
        return out
    if QUALIFIER.search(title):
        return out
    out.append(
        Finding(
            "HEADLINE",
            f"{note.name}:1",
            f"thesis rows {supplied} rest on [supplied] hypotheses, but the title carries no "
            f"qualifier. A title that advertises an achievement while a load-bearing "
            f"row is unforced overstates the result -- qualify the title or move the "
            f"claim out of it",
        )
    )
    return out


def check_thesis(note: Path, ledger: str) -> list[Finding]:
    """The ledger must contain the note's own headline claim, marked as thesis.

    Added after cycle 709, whose ledger was complete over eight component rows
    and contained NO row for the note's thesis. The reviewer: "most importantly,
    the central route no-go has no ledger row or genuine falsifier."

    Detecting "substantive claims" in prose mechanically was tried first and
    abandoned: an allowlist of section headings missed the thesis (it sat under
    "Why the route as posed cannot close"), and inverting to a denylist flagged
    metadata lines and boilerplate in a clean note. Both failures are the same
    shape -- the linter cannot tell a claim from a sentence.

    So responsibility is flipped onto the author, where it belongs: mark one
    ledger row `**thesis**`, and the title must be covered by it. That makes the
    headline claim carry a Support, a Hypotheses tag, and a Falsifier like every
    other claim -- which is exactly what 709 lacked.
    """
    out: list[Finding] = []
    if not ledger:
        return out  # LEDGER already reports the absence
    text = note.read_text()
    title = text.splitlines()[0] if text else ""

    rows = list(_ledger_rows(ledger))
    thesis = [cells for cells in rows if THESIS_MARKER.search(cells[1])]
    if not thesis:
        out.append(
            Finding(
                "THESIS",
                f"{note.name}",
                "no ledger row is marked `**thesis**`; the note's headline claim must "
                "carry a Support, a tagged Hypotheses cell and a Falsifier like every "
                "other claim",
            )
        )
        return out
    if len(thesis) > 1:
        out.append(
            Finding(
                "THESIS",
                f"{note.name}",
                f"claim ledger has {len(thesis)} `**thesis**` rows; exactly one "
                "headline claim is required",
            )
        )
        return out
    if not _claim_text_matches(title, thesis[0][1]):
        out.append(
            Finding(
                "THESIS",
                f"{note.name}:1",
                "the title is not covered by the `**thesis**` ledger row; either the "
                "title claims something the ledger does not, or the thesis row is not "
                "the note's headline claim",
            )
        )
    return out


def check_hypothesis_tags(note: Path) -> list[Finding]:
    """Every non-trivial Hypotheses cell must be tagged [supplied] or [satisfied]."""
    out: list[Finding] = []
    _, ledger = check_ledger(note)
    for cells in _ledger_rows(ledger):
        hyp = cells[3]
        if hyp.lower() in TRIVIAL_HYP or len(hyp) < 8:
            continue
        entries = [
            entry.strip()
            for entry in re.split(r"\s*(?:;|<br\s*/?>)\s*", hyp, flags=re.I)
            if entry.strip()
        ]
        untagged = [
            entry for entry in entries
            if entry.lower() not in TRIVIAL_HYP
            and not TAGGED_HYPOTHESIS.match(entry)
        ]
        if untagged:
            out.append(
                Finding(
                    "TAG",
                    f"{note.name}",
                    f"row `{cells[0]}` has untagged hypothesis entries "
                    f"{untagged}; mark each as "
                    f"`[supplied]` (assumed, unforced) or `[satisfied]` (met by "
                    f"construction) -- the distinction is what the headline check needs",
                )
            )
    return out


TRIVIAL_HYP = {"", "-", "none", "n/a", "none needed"}


# ---------------------------------------------------------------------------


def run(runner: Path | InlineSource | None, note: Path | InlineSource | None) -> list[Finding]:
    findings: list[Finding] = []
    ledger = ""
    if note:
        if not note.exists():
            findings.append(Finding("INPUT", str(note), "note does not exist"))
        else:
            led_findings, ledger = check_ledger(note)
            findings += led_findings
            findings += check_hypothesis(note)
            findings += check_direction(note, ledger)
            findings += check_headline(note)
            findings += check_hypothesis_tags(note)
            findings += check_thesis(note, ledger)
    if runner:
        if not runner.exists():
            findings.append(Finding("INPUT", str(runner), "runner does not exist"))
        else:
            findings += check_slice(runner)
            findings += check_clone(runner)
    return findings


def _case_source(case: dict, kind: str) -> Path | InlineSource | None:
    text_key = f"{kind}_text"
    lines_key = f"{kind}_lines"
    if text_key in case or lines_key in case:
        text = (
            case[text_key]
            if text_key in case
            else "\n".join(case[lines_key]) + "\n"
        )
        return InlineSource(
            case.get(f"{kind}_name", f"{case['id']}-{kind}"),
            text,
        )
    value = case.get(kind)
    return Path(value) if value else None


def _run_selftest_case(
    case: dict,
    runner: Path | InlineSource | None,
    note: Path | InlineSource | None,
) -> list[Finding]:
    only = case.get("only")
    if not only:
        return run(runner, note)
    if only == "HYPOTHESIS" and note and note.exists():
        return check_hypothesis(note)
    if only == "HEADLINE" and note and note.exists():
        return check_headline(note)
    if only == "THESIS" and note and note.exists():
        _, ledger = check_ledger(note)
        return check_thesis(note, ledger)
    if only == "SLICE" and runner and runner.exists():
        return check_slice(runner)
    if only == "CLONE" and runner and runner.exists():
        return check_clone(runner)
    return [
        Finding(
            "SELFTEST",
            case["id"],
            f"unsupported or unavailable focused check `{only}`",
        )
    ]


def selftest(cases_path: Path) -> int:
    """Assert the linter fires on the historical defects it was built from."""
    cases = json.loads(cases_path.read_text())
    failures = 0
    print("Inference-audit linter self-test against shipped defects")
    print("=" * 74)
    for case in cases:
        runner = _case_source(case, "runner")
        note = _case_source(case, "note")
        want = Counter(case["expect"])
        got = Counter(
            finding.check for finding in _run_selftest_case(case, runner, note)
        )
        ok = want == got
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(
            f"[{status}] {case['id']:<24} "
            f"expect {dict(sorted(want.items()))}  got {dict(sorted(got.items()))}"
        )
        print(f"        {case['why']}")
    print("=" * 74)
    print(f"{len(cases) - failures} PASS / {failures} FAIL")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner", type=Path)
    ap.add_argument("--note", type=Path)
    ap.add_argument("--selftest", type=Path)
    args = ap.parse_args()

    if args.selftest:
        if args.runner or args.note:
            ap.error("--selftest cannot be combined with --runner or --note")
        if not args.selftest.is_file():
            ap.error(f"self-test case file is not a readable regular file: {args.selftest}")
        return selftest(args.selftest)
    if not (args.runner or args.note):
        ap.error("provide --note and/or --runner, or use --selftest")
    for label, path in (("runner", args.runner), ("note", args.note)):
        if path and not path.is_file():
            ap.error(f"{label} is not a readable regular file: {path}")

    findings = run(args.runner, args.note)
    for f in findings:
        print(str(f))
    if findings:
        print(f"\n{len(findings)} inference-audit finding(s). Fix or justify before freezing.")
        return 1
    print("inference audit: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
