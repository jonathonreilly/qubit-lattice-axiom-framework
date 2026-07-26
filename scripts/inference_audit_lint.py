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

DIRECTION   a necessity/forcing word in the note with no recorded converse.
            (cycle 707 row F showed non-self-adjointness PERMITS a half-power
            and claimed half-powers REQUIRE it; cycle 702 showed the scale
            primitive SUPPLIES no dimensionless content and claimed it
            SELECTS zero.)

HYPOTHESIS  a named external theorem invoked without its hypotheses stated
            nearby. (cycle 707 invoked Rellich without its analyticity
            hypothesis, then called the conclusion unconditional.)

LEDGER      the note must carry a claim ledger with one row per claim and no
            empty cells. The columns are the ones that would have caught the
            remaining defects: `Support` empty catches an imported premise
            presented as framework content (cycle 705's `conf`); `Falsifier`
            empty catches a statement true by construction (cycle 701's
            symbol-disjointness).

Exit code 1 if any check fires.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

# Modal words that assert a direction stronger than "exhibited".
NECESSITY = re.compile(
    r"\b(requires?|required|only if|forces?|forced|necessary|must be|"
    r"cannot be|unreachable|impossible|uniquely|selects?)\b",
    re.I,
)

# External results whose hypotheses are routinely dropped when cited.
NAMED_THEOREMS = {
    "rellich": ["analytic", "self-adjoint"],
    "kato": ["analytic", "self-adjoint"],
    "gleason": ["dimension", "frame"],
    "busch": ["effect", "frame"],
    "burnside": ["finite group", "orbit"],
    "hellmann": ["eigenvector", "normalized"],
    "orbit-stabilizer": ["finite", "group action"],
    "noether": ["continuous", "symmetry"],
    "rayleigh": ["self-adjoint"],
}

SLICE_RE = re.compile(r"\[\s*:\s*-?\d+\s*\]|\[\s*-?\d+\s*:\s*\]|\bislice\(|\.head\(")
JUSTIFY_RE = re.compile(r"#.*\b(justif|because|why|deliberat|intentional|see )", re.I)


class Finding:
    def __init__(self, check: str, where: str, detail: str):
        self.check, self.where, self.detail = check, where, detail

    def __str__(self) -> str:
        return f"[{self.check}] {self.where}: {self.detail}"


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
        # `zip(xs, xs[1:])` is the adjacent-pairs idiom, not a domain restriction:
        # it pairs consecutive elements and tests every pair. Flagging it made the
        # check fire on a ubiquitous pattern, and a check that cries wolf on
        # idiomatic code gets ignored -- which is worse than not having it.
        adjacent_pair_slices = set()
        for it in iterables:
            for call in ast.walk(it):
                if (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                        and call.func.id == "zip" and len(call.args) >= 2):
                    bases = {ast.dump(a) for a in call.args
                             if not isinstance(a, ast.Subscript)}
                    for a in call.args:
                        if (isinstance(a, ast.Subscript)
                                and ast.dump(a.value) in bases):
                            adjacent_pair_slices.add(id(a))

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


def _normalize_body(fn: ast.FunctionDef) -> str:
    """Dump a function body with all identifiers erased, so clones collide."""
    class Anon(ast.NodeTransformer):
        def visit_Name(self, node):  # noqa: N802
            return ast.copy_location(ast.Name(id="_", ctx=node.ctx), node)

        def visit_arg(self, node):  # noqa: N802
            return ast.copy_location(ast.arg(arg="_", annotation=None), node)

    body = ast.Module(body=[ast.copy_location(s, s) for s in fn.body], type_ignores=[])
    stripped = [s for s in body.body if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, str))]
    body = ast.Module(body=stripped, type_ignores=[])
    return ast.dump(Anon().visit(body))


def check_clone(runner: Path) -> list[Finding]:
    """Two differently-named functions with the same body."""
    out: list[Finding] = []
    try:
        tree = ast.parse(runner.read_text())
    except SyntaxError:
        return out
    seen: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) > 1:
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
    r"^#{1,3}\s*(answer|claim|result|summary|consequence|why|"
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
        if ANY_HEADING.match(line):
            in_claim = bool(CLAIM_SECTION.match(line))
            continue
        if i == 1 or in_claim or "**Theorem" in line:
            out.add(i)
    return out


def check_direction(note: Path, ledger: str) -> list[Finding]:
    """Necessity claims must have their converse recorded in the ledger."""
    out: list[Finding] = []
    text = note.read_text()
    claim_lines = _claim_positions(text)
    for lineno, sent in _sentences(text):
        if lineno not in claim_lines:
            continue
        m = NECESSITY.search(sent)
        if not m:
            continue
        # a converse must be recorded somewhere in the ledger for this sentence
        # Coverage is content-word overlap against the ledger ROWS, not a
        # prefix match. A prefix match is brittle whenever a sentence opens
        # with an inline formula ("`G_0 = H^{-1}` does not exist and ...");
        # the first six tokens are then punctuation debris and can never be
        # found. Overlap asks the question that matters: does some ledger row
        # actually talk about this claim?
        def content(t: str) -> set:
            words = re.sub(r"[^a-z0-9 ]", " ", t.lower()).split()
            return {w for w in words if len(w) > 3}

        sent_words = content(sent)
        covered = False
        for row in ledger.splitlines():
            if len(sent_words & content(row)) >= 4:
                covered = True
                break
        if covered:
            continue
        out.append(
            Finding(
                "DIRECTION",
                f"{note.name}:{lineno}",
                f'asserts "{m.group(0)}" but no claim-ledger row covers '
                f"it: \"{sent[:70]}...\"",
            )
        )
    return out


def check_hypothesis(note: Path) -> list[Finding]:
    """A named theorem must have its hypotheses within 400 chars of the mention."""
    out: list[Finding] = []
    text = note.read_text()
    low = text.lower()
    for name, hyps in NAMED_THEOREMS.items():
        for m in re.finditer(re.escape(name), low):
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


LEDGER_HEADER = re.compile(r"\|\s*ID\s*\|\s*Claim\s*\|\s*Support\s*\|", re.I)


def check_ledger(note: Path) -> tuple[list[Finding], str]:
    """The note must carry a complete claim ledger."""
    text = note.read_text()
    out: list[Finding] = []
    if not LEDGER_HEADER.search(text):
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
    rows, in_tbl, ledger_text = [], False, []
    for i, line in enumerate(text.splitlines(), 1):
        if LEDGER_HEADER.search(line):
            in_tbl = True
            continue
        if in_tbl:
            if not line.strip().startswith("|"):
                break
            ledger_text.append(line)
            if set(line.replace("|", "").strip()) <= set("-: "):
                continue
            rows.append((i, [c.strip() for c in line.strip().strip("|").split("|")]))
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


def _ledger_rows(ledger: str):
    for row in ledger.splitlines():
        if set(row.replace("|", "").strip()) <= set("-: "):
            continue
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 4:
            yield cells


def check_headline(note: Path) -> list[Finding]:
    """A claim resting on a SUPPLIED hypothesis may not appear unqualified in
    the title.

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
    supplied = [c[0] for c in _ledger_rows(ledger) if SUPPLIED_TAG.search(c[3])]
    if not supplied:
        return out
    if QUALIFIER.search(title):
        return out
    out.append(
        Finding(
            "HEADLINE",
            f"{note.name}:1",
            f"rows {supplied} rest on [supplied] hypotheses, but the title carries no "
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
    thesis = [c for c in rows if re.search(r"\bthesis\b", " ".join(c), re.I)]
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

    def content(t: str) -> set:
        return {w for w in re.sub(r"[^a-z0-9 ]", " ", t.lower()).split() if len(w) > 4}

    tw = content(title)
    if not any(len(tw & content(c[1])) >= 3 for c in thesis):
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
        if not (SUPPLIED_TAG.search(hyp) or SATISFIED_TAG.search(hyp)):
            out.append(
                Finding(
                    "TAG",
                    f"{note.name}",
                    f"row `{cells[0]}` hypothesis is untagged; mark each as "
                    f"`[supplied]` (assumed, unforced) or `[satisfied]` (met by "
                    f"construction) -- the distinction is what the headline check needs",
                )
            )
    return out


TRIVIAL_HYP = {"", "-", "none", "n/a", "none needed"}


# ---------------------------------------------------------------------------


def run(runner: Path | None, note: Path | None) -> list[Finding]:
    findings: list[Finding] = []
    ledger = ""
    if note and note.exists():
        led_findings, ledger = check_ledger(note)
        findings += led_findings
        findings += check_hypothesis(note)
        findings += check_direction(note, ledger)
        findings += check_headline(note)
        findings += check_hypothesis_tags(note)
        findings += check_thesis(note, ledger)
    if runner and runner.exists():
        findings += check_slice(runner)
        findings += check_clone(runner)
    return findings


def selftest(cases_path: Path) -> int:
    """Assert the linter fires on the historical defects it was built from."""
    cases = json.loads(cases_path.read_text())
    failures = 0
    print("Inference-audit linter self-test against shipped defects")
    print("=" * 74)
    for case in cases:
        runner = Path(case["runner"]) if case.get("runner") else None
        note = Path(case["note"]) if case.get("note") else None
        want = set(case["expect"])
        got = {f.check for f in run(runner, note)}
        ok = want <= got
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"[{status}] {case['id']:<24} expect {sorted(want)}  got {sorted(got)}")
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
        return selftest(args.selftest)

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
