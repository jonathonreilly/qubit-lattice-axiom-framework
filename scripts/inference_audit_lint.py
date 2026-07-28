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

HYPOTHESIS  an explicitly identified external theorem invoked without its
            hypotheses stated nearby, or a bare surname that needs manual
            identification. (cycle 707 invoked Rellich without its analyticity
            hypothesis, then called the conclusion unconditional.)

LEDGER      the note must carry the exact six-column claim-ledger schema with
            one row per claim and no empty cells. The columns are the ones that
            would have caught the remaining defects: `Support` empty catches
            an imported premise presented as framework content (cycle 705's
            `conf`); `Falsifier` empty catches a statement true by construction
            (cycle 701's symbol-disjointness).

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

# External results whose hypotheses are routinely dropped when cited. Match
# explicit theorem identities, longest/composite names first. Bare surnames
# are routed to manual identification below rather than guessed.
THEOREM_DASH = r"\s*[-\N{EN DASH}\N{EM DASH}]\s*"
NAMED_THEOREMS = (
    (
        "kato-rellich",
        re.compile(
            rf"\bkato{THEOREM_DASH}rellich(?:'s)?(?:\s+theorem)?\b",
            re.I,
        ),
        ("bounded", "self-adjoint"),
    ),
    (
        "rellich-kondrachov",
        re.compile(
            rf"\brellich{THEOREM_DASH}kondrachov(?:'s)?(?:\s+theorem)?\b",
            re.I,
        ),
        ("bounded domain", "compact"),
    ),
    (
        "rellich analytic perturbation theorem",
        re.compile(
            r"\brellich(?:'s)?\s+(?:analytic\s+perturbation\s+)?theorem\b",
            re.I,
        ),
        ("analytic", "self-adjoint"),
    ),
    (
        "kato analytic perturbation theorem",
        re.compile(
            r"\bkato(?:'s)?\s+analytic\s+perturbation\s+theorem\b",
            re.I,
        ),
        ("analytic", "self-adjoint"),
    ),
    (
        "gleason theorem",
        re.compile(r"\bgleason(?:'s)?\s+theorem\b", re.I),
        ("dimension", "frame"),
    ),
    (
        "busch theorem",
        re.compile(r"\bbusch(?:'s)?\s+theorem\b", re.I),
        ("effect", "frame"),
    ),
    (
        "burnside matrix-algebra theorem",
        re.compile(
            r"\b(?:"
            r"burnside(?:'s)?\s+(?:classical\s+)?theorem"
            r"\s+(?:on|for)\s+[^.;\n]{0,100}\bmatrix[- ]"
            r"(?:algebras?|semigroups?)"
            r"|burnside(?:'s)?\s+matrix[- ]algebra\s+theorem"
            r"|matrix[- ]algebra\s+burnside(?:'s)?\s+theorem"
            r")\b",
            re.I,
        ),
        ("irreducible", "matrix algebra"),
    ),
    (
        "burnside orbit-counting lemma",
        re.compile(
            r"\bburnside(?:'s)?\s+(?:lemma|orbit[- ]counting"
            r"(?:\s+(?:lemma|theorem))?|"
            r"theorem\s+(?:on|for)\s+[^.;\n]{0,100}"
            r"(?:finite[- ]group\s+orbits?|orbit[- ]counting))\b",
            re.I,
        ),
        ("finite group", "orbit"),
    ),
    (
        "hellmann-feynman",
        re.compile(rf"\bhellmann{THEOREM_DASH}feynman\b", re.I),
        ("eigenvector", "normalized"),
    ),
    (
        "orbit-stabilizer",
        re.compile(rf"\borbit{THEOREM_DASH}stabilizer\b", re.I),
        ("finite", "group action"),
    ),
    (
        "variational noether",
        re.compile(
            r"\bnoether(?:'s)?\s+(?:theorem|identity)\b",
            re.I,
        ),
        ("continuous", "symmetry"),
    ),
    (
        "rayleigh-ritz",
        re.compile(rf"\brayleigh{THEOREM_DASH}ritz\b", re.I),
        ("self-adjoint",),
    ),
)

THEOREM_NAMESAKE_EXCLUSIONS = (
    re.compile(
        rf"\bskolem{THEOREM_DASH}noether(?:'s)?(?:\s+theorem)?\b",
        re.I,
    ),
)
AMBIGUOUS_THEOREM_SURNAME = re.compile(
    r"\b(rellich|kato|gleason|busch|burnside|hellmann|noether|rayleigh)\b",
    re.I,
)
HYPOTHESIS_WINDOW = 800

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


def _int_literal(node: ast.AST | None) -> int | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, (ast.USub, ast.UAdd))
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, int)
    ):
        sign = -1 if isinstance(node.op, ast.USub) else 1
        return sign * node.operand.value
    return None


def _is_narrowing_slice(node: ast.AST) -> bool:
    """Whether an iteration-position slice can drop domain elements.

    An unbounded unit-stride copy and a pure reversal retain the full domain.
    Bounds, non-unit strides, and dynamic strides can all omit elements.
    """
    if not isinstance(node, ast.Subscript) or not isinstance(node.slice, ast.Slice):
        return False
    sl = node.slice
    if sl.lower is not None or sl.upper is not None:
        return True
    if sl.step is None:
        return False
    return _int_literal(sl.step) not in (1, -1)


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

        def is_tail_from_one(node):
            return (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Slice)
                and _int_literal(node.slice.lower) == 1
                and node.slice.upper is None
                and node.slice.step is None
            )

        def is_drop_last(node):
            return (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Slice)
                and node.slice.lower is None
                and _int_literal(node.slice.upper) == -1
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


def _argument_bindings(args: ast.arguments) -> list[ast.arg]:
    out = [*args.posonlyargs, *args.args, *args.kwonlyargs]
    if args.vararg:
        out.append(args.vararg)
    if args.kwarg:
        out.append(args.kwarg)
    return out


class _ScopeBindingCollector(ast.NodeVisitor):
    """Collect bindings in one lexical scope without descending into children."""

    def __init__(self, args: ast.arguments | None):
        self.ordered: list[str] = []
        self.globals: set[str] = set()
        self.nonlocals: set[str] = set()
        if args:
            for arg in _argument_bindings(args):
                self.add(arg.arg)

    def add(self, name: str | None) -> None:
        if name and name not in self.ordered:
            self.ordered.append(name)

    def visit_FunctionDef(self, node):  # noqa: N802
        self.add(node.name)

    def visit_AsyncFunctionDef(self, node):  # noqa: N802
        self.add(node.name)

    def visit_Lambda(self, node):  # noqa: N802
        return

    def visit_ClassDef(self, node):  # noqa: N802
        self.add(node.name)

    def visit_Name(self, node):  # noqa: N802
        if isinstance(node.ctx, ast.Store):
            self.add(node.id)

    def visit_Import(self, node):  # noqa: N802
        for alias in node.names:
            self.add(alias.asname or alias.name.split(".", 1)[0])

    def visit_ImportFrom(self, node):  # noqa: N802
        for alias in node.names:
            self.add(alias.asname or alias.name)

    def visit_ExceptHandler(self, node):  # noqa: N802
        self.add(node.name)
        self.generic_visit(node)

    def visit_Global(self, node):  # noqa: N802
        self.globals.update(node.names)

    def visit_Nonlocal(self, node):  # noqa: N802
        self.nonlocals.update(node.names)

    def _visit_comprehension(self, node: ast.AST) -> None:
        """Visit expressions but not comprehension-local iteration targets."""

        generators = node.generators
        for generator in generators:
            self.visit(generator.iter)
            for condition in generator.ifs:
                self.visit(condition)
        if isinstance(node, ast.DictComp):
            self.visit(node.key)
            self.visit(node.value)
        else:
            self.visit(node.elt)

    def visit_ListComp(self, node):  # noqa: N802
        self._visit_comprehension(node)

    def visit_SetComp(self, node):  # noqa: N802
        self._visit_comprehension(node)

    def visit_GeneratorExp(self, node):  # noqa: N802
        self._visit_comprehension(node)

    def visit_DictComp(self, node):  # noqa: N802
        self._visit_comprehension(node)

    def visit_MatchAs(self, node):  # noqa: N802
        self.add(node.name)
        if node.pattern:
            self.visit(node.pattern)

    def visit_MatchStar(self, node):  # noqa: N802
        self.add(node.name)

    def visit_MatchMapping(self, node):  # noqa: N802
        self.add(node.rest)
        for pattern in node.patterns:
            self.visit(pattern)


class _LexicalAlphaNormalizer(ast.NodeTransformer):
    """Alpha-normalize each function scope while retaining genuine free names."""

    def __init__(self):
        self.scopes: list[tuple[dict[str, str], set[str]]] = []
        self.next_scope = 0

    def _resolve(self, name: str) -> str:
        for mapping, global_names in reversed(self.scopes):
            if name in global_names:
                return name
            if name in mapping:
                return mapping[name]
        return name

    def _scope_for(
        self,
        args: ast.arguments,
        body: list[ast.AST],
    ) -> tuple[dict[str, str], set[str]]:
        collector = _ScopeBindingCollector(args)
        for statement in body:
            collector.visit(statement)
        scope_number = self.next_scope
        self.next_scope += 1
        excluded = collector.globals | collector.nonlocals
        ordered = [name for name in collector.ordered if name not in excluded]
        mapping = {
            name: f"_scope_{scope_number}_{index}"
            for index, name in enumerate(ordered)
        }
        return mapping, collector.globals

    def _comprehension_scope(
        self,
        generators: list[ast.comprehension],
    ) -> tuple[dict[str, str], set[str]]:
        collector = _ScopeBindingCollector(None)
        for generator in generators:
            collector.visit(generator.target)
        scope_number = self.next_scope
        self.next_scope += 1
        mapping = {
            name: f"_scope_{scope_number}_{index}"
            for index, name in enumerate(collector.ordered)
        }
        return mapping, set()

    def _visit_outer_arguments(self, args: ast.arguments) -> None:
        for arg in _argument_bindings(args):
            if arg.annotation:
                arg.annotation = self.visit(arg.annotation)
        args.defaults = [self.visit(default) for default in args.defaults]
        args.kw_defaults = [
            self.visit(default) if default else None
            for default in args.kw_defaults
        ]

    @staticmethod
    def _rename_argument_bindings(
        args: ast.arguments,
        mapping: dict[str, str],
    ) -> None:
        for arg in _argument_bindings(args):
            if arg.arg in mapping:
                arg.arg = mapping[arg.arg]

    def _normalize_function(
        self,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
        *,
        root: bool,
    ):
        original_name = node.name
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, str)
        ):
            node.body = node.body[1:]

        # Definition-time expressions execute in the surrounding scope.
        node.decorator_list = [
            self.visit(decorator) for decorator in node.decorator_list
        ]
        self._visit_outer_arguments(node.args)
        if node.returns:
            node.returns = self.visit(node.returns)
        if hasattr(node, "type_params"):
            node.type_params = [
                self.visit(type_param) for type_param in node.type_params
            ]

        mapping, global_names = self._scope_for(node.args, node.body)
        node.name = "_function" if root else self._resolve(original_name)
        self.scopes.append((mapping, global_names))
        self._rename_argument_bindings(node.args, mapping)
        node.body = [self.visit(statement) for statement in node.body]
        self.scopes.pop()
        return node

    def visit_FunctionDef(self, node):  # noqa: N802
        return self._normalize_function(node, root=False)

    def visit_AsyncFunctionDef(self, node):  # noqa: N802
        return self._normalize_function(node, root=False)

    def visit_Lambda(self, node):  # noqa: N802
        self._visit_outer_arguments(node.args)
        mapping, global_names = self._scope_for(node.args, [node.body])
        self.scopes.append((mapping, global_names))
        self._rename_argument_bindings(node.args, mapping)
        node.body = self.visit(node.body)
        self.scopes.pop()
        return node

    def visit_ClassDef(self, node):  # noqa: N802
        # A class body uses a dynamic namespace rather than a function closure.
        # Preserve it exactly so class-local names cannot be mistaken for
        # enclosing-function locals; only definition-time outer expressions
        # and the class's binding in the enclosing scope are normalized.
        node.name = self._resolve(node.name)
        node.decorator_list = [
            self.visit(decorator) for decorator in node.decorator_list
        ]
        node.bases = [self.visit(base) for base in node.bases]
        node.keywords = [self.visit(keyword) for keyword in node.keywords]
        return node

    def _visit_comprehension(self, node: ast.AST):
        generators = node.generators
        if not generators:
            return node

        # Python evaluates the outermost iterable in the surrounding scope.
        generators[0].iter = self.visit(generators[0].iter)
        mapping, global_names = self._comprehension_scope(generators)
        self.scopes.append((mapping, global_names))

        generators[0].target = self.visit(generators[0].target)
        generators[0].ifs = [
            self.visit(condition) for condition in generators[0].ifs
        ]
        for generator in generators[1:]:
            generator.iter = self.visit(generator.iter)
            generator.target = self.visit(generator.target)
            generator.ifs = [
                self.visit(condition) for condition in generator.ifs
            ]
        if isinstance(node, ast.DictComp):
            node.key = self.visit(node.key)
            node.value = self.visit(node.value)
        else:
            node.elt = self.visit(node.elt)
        self.scopes.pop()
        return node

    def visit_ListComp(self, node):  # noqa: N802
        return self._visit_comprehension(node)

    def visit_SetComp(self, node):  # noqa: N802
        return self._visit_comprehension(node)

    def visit_GeneratorExp(self, node):  # noqa: N802
        return self._visit_comprehension(node)

    def visit_DictComp(self, node):  # noqa: N802
        return self._visit_comprehension(node)

    def visit_Name(self, node):  # noqa: N802
        resolved = self._resolve(node.id)
        if resolved == node.id:
            return node
        return ast.copy_location(ast.Name(id=resolved, ctx=node.ctx), node)

    def visit_Nonlocal(self, node):  # noqa: N802
        node.names = [self._resolve(name) for name in node.names]
        return node

    def visit_ExceptHandler(self, node):  # noqa: N802
        if node.name:
            node.name = self._resolve(node.name)
        return self.generic_visit(node)

    def visit_MatchAs(self, node):  # noqa: N802
        if node.name:
            node.name = self._resolve(node.name)
        if node.pattern:
            node.pattern = self.visit(node.pattern)
        return node

    def visit_MatchStar(self, node):  # noqa: N802
        if node.name:
            node.name = self._resolve(node.name)
        return node

    def visit_MatchMapping(self, node):  # noqa: N802
        if node.rest:
            node.rest = self._resolve(node.rest)
        node.keys = [self.visit(key) for key in node.keys]
        node.patterns = [self.visit(pattern) for pattern in node.patterns]
        return node

    def visit_Import(self, node):  # noqa: N802
        for alias in node.names:
            binding = alias.asname or alias.name.split(".", 1)[0]
            resolved = self._resolve(binding)
            if resolved != binding:
                alias.asname = resolved
        return node

    def visit_ImportFrom(self, node):  # noqa: N802
        for alias in node.names:
            binding = alias.asname or alias.name
            resolved = self._resolve(binding)
            if resolved != binding:
                alias.asname = resolved
        return node


def _normalize_body(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """Alpha-normalize nested lexical scopes and preserve semantic free names."""

    fn_copy = copy.deepcopy(fn)
    normalizer = _LexicalAlphaNormalizer()
    normalized = normalizer._normalize_function(fn_copy, root=True)
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


def _claim_tokens(text: str) -> tuple[str, ...]:
    """Normalize Markdown presentation while preserving mathematical syntax."""

    cleaned = re.sub(r"\*\*\s*thesis\s*\*\*", " ", text, flags=re.I)
    cleaned = re.sub(r"^\s*#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"<br\s*/?>", " ", cleaned, flags=re.I)
    cleaned = cleaned.strip()
    for marker in ("**", "`"):
        if cleaned.startswith(marker) and cleaned.endswith(marker):
            cleaned = cleaned[len(marker) : -len(marker)].strip()
    cleaned = re.sub(r"\\([\\`*_[\]{}()#+.!|<>-])", r"\1", cleaned)
    # Non-word tokens are retained individually, so x < y cannot equal x > y.
    return tuple(re.findall(r"\w+|[^\w\s]", cleaned.casefold()))


CLAIM_MODALITIES = (
    ("permits", re.compile(r"\b(permits?|permitted|allows?|allowed|enables?)\b", re.I)),
    ("requires", re.compile(r"\b(requires?|required|necessary|must|only if)\b", re.I)),
    ("forces", re.compile(r"\b(forces?|forced)\b", re.I)),
    (
        "negative",
        re.compile(
            r"\b(cannot|does not exist|no [^.;]{0,80} exists|"
            r"unreachable|impossible)\b",
            re.I,
        ),
    ),
    ("unique", re.compile(r"\b(unique|uniquely|uniqueness)\b", re.I)),
    ("selects", re.compile(r"\b(selects?|selected)\b", re.I)),
)


def _claim_modality(text: str) -> frozenset[str]:
    return frozenset(
        name for name, pattern in CLAIM_MODALITIES if pattern.search(text)
    )


def _claim_text_matches(
    left: str,
    right: str,
    *,
    allow_coverage: bool = False,
) -> bool:
    a = _claim_tokens(left)
    b = _claim_tokens(right)
    if not a or not b:
        return False
    left_modality = _claim_modality(left)
    if left_modality and left_modality != _claim_modality(right):
        return False
    if a == b:
        return True
    if not allow_coverage:
        return False

    def contains(haystack: tuple[str, ...], needle: tuple[str, ...]) -> bool:
        width = len(needle)
        return any(
            haystack[index : index + width] == needle
            for index in range(len(haystack) - width + 1)
        )

    return contains(a, b) or contains(b, a)


DIRECTION_META_OR_DENIAL = re.compile(
    r"\b(?:cannot|could not|does not|did not|fails? to|failed to|"
    r"has not|have not|was not|were not)\s+"
    r"(?:\w+\s+){0,3}(?:establish|show|prove|check|verify|demonstrate|"
    r"derive|infer|conclude|justify|certify)\b|"
    r"\b(?:not|never)\s+(?:\w+\s+){0,5}"
    r"(?:established|shown|proved|checked|verified|demonstrated|derived|"
    r"inferred|justified|certified)\b|"
    r"\bno\s+(?:(?:checked|established|proved|verified)\s+)?"
    r"(?:converse|equivalence|uniqueness|impossibility|necessity)\b|"
    r"\b(?:there\s+is\s+)?no\s+(?:\w+\s+){0,3}"
    r"(?:evidence|proof|support|verification|demonstration|argument|"
    r"derivation|calculation|analysis)\b|"
    r"\b(?:lacks?|lacking|without)\s+(?:\w+\s+){0,3}"
    r"(?:evidence|proof|support|verification|demonstration|argument|"
    r"derivation|calculation|analysis)\b|"
    r"\b(?:proves?|proved|shows?|shown|establishes?|established|"
    r"verifies?|verified|checks?|checked|demonstrates?|demonstrated|"
    r"derives?|derived|confirms?|confirmed)\b[^.;]{0,80}"
    r"\b(?:no|not)\s+(?:\w+\s+){0,3}"
    r"(?:converse|equivalence|necessity|unique(?:ness)?|impossibility)\b|"
    r"\b(?:tests?|asks?|examines?|considers?|investigates?|questions?|"
    r"quotes?|repeats?|restates?|mentions?|records?|reports?|asserts?|states?)\b"
    r"[^.;]{0,100}\b(?:whether|if|claimed|required|forced|necessary|must|"
    r"converse|equivalence|iff|unique(?:ly)?|uniqueness|impossible|"
    r"impossibility)\b",
    re.I,
)
DIRECTION_AFFIRMATIVE = re.compile(
    r"\b(?:if and only if|iff|equivalent(?:\s+to)?)\b|"
    r"\b(?:proves?|proved|shows?|shown|establishes?|established|"
    r"verifies?|verified|checks?|checked|demonstrates?|demonstrated|"
    r"derives?|derived|confirms?|confirmed)\b"
    r"[^.;]{0,120}\b(?:requires?|forced?|necessary|necessity|must|"
    r"converse|equivalence|unique(?:ly)?|uniqueness|impossible|"
    r"impossibility|does not exist|no [^.;]{0,40} exists|selects?)\b|"
    r"\b(?:converse|equivalence|necessity|impossibility|uniqueness)\b"
    r"[^.;]{0,80}\b(?:holds?|is|was|has been)\s+"
    r"(?:proved|shown|established|verified|checked|demonstrated|derived)\b|"
    r"\b(?:exact|exhaustive|complete)\b[^.;]{0,120}"
    r"\b(?:requires?|forced?|necessary|must|unique(?:ly)?|uniqueness|"
    r"impossible|does not exist|selects?)\b|"
    r"\b(?:exactly one|does not exist|"
    r"no [^.;]{0,80} exists|unreachable|impossible|"
    r"cannot (?:exist|occur|hold|satisfy|equal|"
    r"be (?:reached|satisfied|realized|constructed|nonzero|invertible)))\b",
    re.I,
)
DIRECTION_AUTHORIZED_NEGATIVE = re.compile(
    r"\bdoes\s+not\s+exist\b|"
    r"\bno\s+[^.;]{0,80}\s+exists\b|"
    r"\bcannot\s+(?:exist|occur|hold|satisfy|equal|"
    r"be\s+(?:reached|satisfied|realized|constructed|nonzero|invertible))\b",
    re.I,
)
DIRECTION_UNSUPPORTED_POLARITY = re.compile(
    r"\b(?:false|neither|nor|insufficient|inconclusive|unproven|"
    r"undemonstrated|unsupported|unknown|unclear|uncertain|allegedly|"
    r"purportedly|perhaps|possibly|probably|apparently|hardly|scarcely|"
    r"barely|doubtful|may|might|could|would|seems?|appears?|suggests?)\b|"
    r"\b(?:absence|failure)\s+of\b|"
    r"\bnon[- ](?:unique(?:ly|ness)?|equivalent|equivalence|necessary|"
    r"necessity)\b|"
    r"\b(?:prints?|discusses?|describes?|quotes?|repeats?|restates?|"
    r"mentions?|records?|reports?|asks?|examines?|considers?|"
    r"investigates?|questions?|contains?|reproduces?|summarizes?|"
    r"paraphrases?|cites?|transcribes?|lists?|displays?|presents?)\b|"
    r"\b(?:says?|writes?|reads?|notes?|supposes?|assumes?|hypothesizes?|"
    r"conjectures?|postulates?)\b|"
    r"\b(?:disproves?|refutes?|contradicts?|denies?)\b|"
    r"\baccording\s+to\b|"
    r"\b(?:not|no|never|without|lacks?|lacking)\b",
    re.I,
)
SHOWN_CLAIMED = re.compile(
    r"^\s*shown\s*:\s*(?P<shown>.+?)\s*"
    r"(?:;|<br\s*/?>)\s*claimed\s*:\s*(?P<claimed>.+?)\s*$",
    re.I | re.S,
)


def _split_shown_claimed(cell: str) -> tuple[str, str] | None:
    match = SHOWN_CLAIMED.fullmatch(cell)
    if not match:
        return None
    shown = match.group("shown").strip()
    claimed = match.group("claimed").strip()
    if not shown or not claimed:
        return None
    return shown, claimed


def _claimed_clause_matches(claimed: str, claim: str) -> bool:
    normalized = _claim_tokens(claimed)
    if normalized in {
        ("same",),
        ("the", "same"),
        ("same", "claim"),
        ("the", "same", "claim"),
    }:
        return True
    return _claim_text_matches(claimed, claim)


def _direction_evidence_is_affirmative(shown: str) -> bool:
    if (
        re.search(r"\bclaimed\s*:", shown, re.I)
        or "?" in shown
        or re.search(r'["“”‘’`]', shown)
        or re.search(r"(?<!\w)'[^']+'(?!\w)", shown)
    ):
        return False
    if DIRECTION_META_OR_DENIAL.search(shown):
        return False
    polarity_text = DIRECTION_AUTHORIZED_NEGATIVE.sub(
        " established-impossibility ",
        shown,
    )
    if DIRECTION_UNSUPPORTED_POLARITY.search(polarity_text):
        return False
    return bool(DIRECTION_AFFIRMATIVE.search(shown))


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
            parsed = _split_shown_claimed(cells[4])
            if not parsed:
                continue
            shown, claimed = parsed
            if (
                _claimed_clause_matches(claimed, cells[1])
                and _direction_evidence_is_affirmative(shown)
            ):
                supported = True
                break
        if supported:
            continue
        reason = (
            "no matching claim-ledger row"
            if not matching
            else "the matching row has no canonical, affirmative `shown:` "
                 "record of a converse, equivalence, uniqueness, impossibility, "
                 "or other necessity-strength evidence whose `claimed:` clause "
                 "binds exactly to the Claim cell"
        )
        out.append(
            Finding(
                "DIRECTION",
                f"{note.name}:{lineno}",
                f'asserts "{m.group(0)}" but {reason}: \"{sent[:70]}...\"',
            )
        )
    return out


HYPOTHESIS_PATTERNS = {
    "bounded domain": re.compile(
        r"\bbounded(?:\s+[\w-]+){0,3}\s+domain\b",
        re.I,
    ),
    "irreducible": re.compile(
        r"\birreducib(?:le|ly|ility)\b|"
        r"\bno\s+(?:(?:proper|nonzero)\s+){1,2}subspace\b"
        r"[^.;\n]{0,100}\binvariant\b",
        re.I,
    ),
    "matrix algebra": re.compile(
        r"\bmatrix[- ]algebras?\b|"
        r"\bm\s*_?\s*(?:\d+|n)\s*\(\s*c\s*\)",
        re.I,
    ),
    "finite group": re.compile(r"\bfinite[- ]groups?\b", re.I),
}


def _hypothesis_present(label: str, text: str) -> bool:
    pattern = HYPOTHESIS_PATTERNS.get(label)
    return bool(pattern.search(text)) if pattern else label in text


def _paragraph_containing(text: str, start: int, end: int) -> str:
    left = text.rfind("\n\n", 0, start)
    right = text.find("\n\n", end)
    return text[left + 2 if left >= 0 else 0 : right if right >= 0 else len(text)]


BURNSIDE_MATRIX_CONTEXT = re.compile(
    r"\bmatrix[- ](?:algebras?|semigroups?|units?)\b|"
    r"\bm\s*_?\s*(?:\d+|n)\s*\(\s*c\s*\)",
    re.I,
)
BURNSIDE_ORBIT_CONTEXT = re.compile(
    r"\borbits?\b|\borbit[- ]counting\b|\bgroup\s+action\b",
    re.I,
)


def _burnside_shorthand_schema(
    paragraph: str,
) -> tuple[str, tuple[str, ...]] | None:
    matrix = bool(BURNSIDE_MATRIX_CONTEXT.search(paragraph)) or bool(
        re.search(r"\bsubalgebra\b", paragraph, re.I)
        and re.search(
            r"\birreducib(?:le|ly|ility)\b|\brank[- ]one\b",
            paragraph,
            re.I,
        )
    )
    orbit = bool(BURNSIDE_ORBIT_CONTEXT.search(paragraph))
    if matrix == orbit:
        return None
    if matrix:
        return "burnside matrix-algebra theorem", ("irreducible", "matrix algebra")
    return "burnside orbit-counting lemma", ("finite group", "orbit")


def check_hypothesis(note: Path) -> list[Finding]:
    """An explicitly identified theorem needs its hypotheses nearby.

    Composite names and known namesakes reserve their full spans before
    shorter identities are considered. A bare surname receives a manual-
    identification finding instead of being assigned a guessed theorem.
    """
    out: list[Finding] = []
    text = note.read_text()
    low = text.lower()
    occupied: list[tuple[int, int]] = []

    def overlaps(span: tuple[int, int]) -> bool:
        return any(span[0] < end and start < span[1] for start, end in occupied)

    for pattern in THEOREM_NAMESAKE_EXCLUSIONS:
        occupied.extend(match.span() for match in pattern.finditer(text))

    for line_number, line_text in enumerate(text.splitlines(), 1):
        burnside_match = re.search(r"\bburnside\b", line_text, re.I)
        if (
            burnside_match
            and BURNSIDE_MATRIX_CONTEXT.search(line_text)
            and BURNSIDE_ORBIT_CONTEXT.search(line_text)
        ):
            line_start = sum(
                len(line) + 1 for line in text.splitlines()[: line_number - 1]
            )
            span = (
                line_start + burnside_match.start(),
                line_start + burnside_match.end(),
            )
            occupied.append(span)
            out.append(
                Finding(
                    "HYPOTHESIS",
                    f"{note.name}:{line_number}",
                    "conflates matrix-algebra and orbit-counting Burnside "
                    "identities on one line; name each result separately",
                )
            )

    for name, pattern, hyps in NAMED_THEOREMS:
        for m in pattern.finditer(text):
            if overlaps(m.span()):
                continue
            occupied.append(m.span())
            window = low[
                max(0, m.start() - HYPOTHESIS_WINDOW)
                : m.start() + HYPOTHESIS_WINDOW
            ]
            missing = [h for h in hyps if not _hypothesis_present(h, window)]
            if missing:
                line = text[: m.start()].count("\n") + 1
                out.append(
                    Finding(
                        "HYPOTHESIS",
                        f"{note.name}:{line}",
                        f"invokes `{name}` without stating hypotheses {missing} nearby",
                    )
                )
    for match in AMBIGUOUS_THEOREM_SURNAME.finditer(text):
        if overlaps(match.span()):
            continue
        occupied.append(match.span())
        line = text[: match.start()].count("\n") + 1
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        line_text = text[line_start : line_end if line_end >= 0 else len(text)]
        if re.match(r"^\s*#{1,6}\s", line_text):
            continue
        if match.group(1).lower() == "burnside":
            suffix = text[match.end() : match.end() + 12]
            if re.match(r"-(?:type|style|related)\b", suffix, re.I):
                continue
            paragraph = _paragraph_containing(text, *match.span())
            schema = _burnside_shorthand_schema(paragraph)
            if schema:
                name, hyps = schema
                local_context = paragraph
                paragraph_start = text.rfind("\n\n", 0, match.start()) + 2
                for label in re.findall(r"\(T\d+\)", paragraph):
                    prior = text.rfind(
                        label,
                        max(0, match.start() - HYPOTHESIS_WINDOW),
                        paragraph_start,
                    )
                    if prior >= 0:
                        local_context = text[prior:paragraph_start] + paragraph
                        break
                missing = [
                    h
                    for h in hyps
                    if not _hypothesis_present(h, local_context.lower())
                ]
                if missing:
                    out.append(
                        Finding(
                            "HYPOTHESIS",
                            f"{note.name}:{line}",
                            f"uses local shorthand for `{name}` without stating "
                            f"hypotheses {missing} in the same paragraph",
                        )
                    )
                continue
        out.append(
            Finding(
                "HYPOTHESIS",
                f"{note.name}:{line}",
                f"mentions ambiguous bare surname `{match.group(0)}`; identify "
                "the exact theorem (including a composite name when applicable) "
                "and state its hypotheses for manual review",
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
        if not _split_shown_claimed(cells[4]):
            out.append(
                Finding(
                    "LEDGER",
                    f"{note.name}:{lineno}",
                    "the `Shown vs claimed` cell must contain non-empty "
                    "`shown: ...; claimed: ...` clauses (or use `<br>` as the "
                    "delimiter); a comma does not separate the evidence from "
                    "the claim",
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
    if not _claim_text_matches(title, thesis[0][1], allow_coverage=True):
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
