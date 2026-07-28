# Inference Audit

Run this **after the runner passes and before the note is frozen**, on every
cycle. It is the counterpart of the step-2 prior-art sweep: the sweep stops you
re-deriving something that exists, this stops you asserting more than you
showed.

## Why this exists

The 2026-07-25/26 campaign produced six consecutive value-gate rejections. In
**every one** the exact arithmetic was correct and reproduced cold; the defect
was in the step from the arithmetic to the sentence. Reviewers caught all six;
the author caught none before submission.

The author also recorded the lesson in a backlog file after four of them —
including, verbatim, *"every one of these would have been caught by writing the
one-sentence claim first and attacking it before building the runner"* — and
then committed the same class of error in the next cycle, writing a correctly
qualified theorem and an unqualified restatement of it in the same document.

**Self-recorded lessons did not work. The mechanical step-2 sweep did**, catching
six duplications in the same campaign. This audit is therefore mechanical and
produces an artifact, not a resolution.

## The step

1. Run the linter:

   ```bash
   python3 scripts/inference_audit_lint.py --runner <runner>.py --note <note>.md
   ```

2. Fix or justify every finding. A justification is a comment in the runner or
   a sentence in the note, not a silent narrowing.

3. Fill the **claim ledger** in the note. The linter enforces its presence and
   that no cell is empty; only you can fill it honestly.

## The claim ledger

One row per claim the note asserts — every `**Theorem**` statement, and every
restatement of one in an Answer/Summary/discussion section.

```text
| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
```

- **Claim** — the sentence as it appears in the note, verbatim. If a
  restatement differs from the theorem statement, it gets its **own row**.
  Diff the two; a dropped qualifier is a defect, not a simplification.
- **Support** — the runner row, landed note, or named theorem that establishes
  it. If this is empty, the claim rests on nothing shown. An objective, a
  weighting, an aggregation, or a coupling that *you* chose is not support; it
  is an import, and belongs in `ASSUMPTIONS_AND_IMPORTS.md` with a class.
- **Hypotheses** — every hypothesis of every named result cited, written out,
  each tagged **`[supplied]`** (assumed and unforced) or **`[satisfied]`** (met
  by construction). Separate multiple hypothesis entries with a semicolon or
  `<br>` and begin **each entry** with its own tag. The tag is the load-bearing
  part: it is the distinction whose absence caused the first cycle run under
  this audit to pass the audit and still be rejected.
  Identify the exact theorem, including composite names such as
  Kato–Rellich or Rellich–Kondrachov. A bare surname is ambiguous and is routed
  to manual identification rather than assigned a guessed hypothesis list.
  Ordinary identity word orders such as “Burnside's theorem on irreducible
  matrix algebras” are supported; hypothesis wording may include standard
  refinements such as a bounded Lipschitz domain.
  Not the conclusion. The linter's keyword check catches outright omission but
  **cannot** distinguish a hypothesis from a conclusion; this column is the only
  thing that does. A cited theorem whose hypotheses you cannot state is a
  theorem you are not entitled to use.
- **Shown vs claimed** — what the evidence establishes, then what the sentence
  asserts, as explicit `shown:` and `claimed:` clauses. This column exists
  because "X permits Y" and "Y requires X" are different statements and the
  second does not follow from the first. When the claim uses necessity language,
  the `shown:` clause must itself record necessity-strength evidence: a checked
  converse or equivalence, uniqueness, impossibility, or an exact negative
  existence result. Repeating the necessity word only in `claimed:` does not
  pass `DIRECTION`, nor does writing that a converse *could not* be established.
  Separate the clauses with `; claimed:` (or `<br>claimed:`); a comma does not
  establish an evidence boundary, and no second `claimed:` label may appear
  inside `shown:`. The parsed `claimed:` clause must match the Claim cell
  exactly (or say “the same”) with the same modality. Questions, quotations,
  and lack-of-evidence or negated-proof prose are not affirmative evidence.
  The reviewer still checks whether the recorded evidence is true.
- **Falsifier** — a concrete state of the world that would make the claim
  false. If you cannot name one, the claim is true by construction and is not a
  result.

## Checks the linter runs

| check | catches | limitation |
|---|---|---|
| `SLICE` | a check row iterating a narrowed domain (`for g in hill[:1]`, `values[::2]`), leaving dropped elements untested | iteration position only; display truncation, unit-stride copies, pure reversal, and verified adjacent-pair idioms are ignored |
| `CLONE` | two functions with identical bodies modulo local names, then "verified" to agree | each nested lexical scope is alpha-normalized independently; captured outer locals follow their enclosing binding, while free names and outer-evaluated defaults, decorators, and annotations retain their semantics |
| `DIRECTION` | a necessity word in a claim whose modality-matched ledger row has no affirmative necessity-strength `shown:` clause | claim positions only — title, `**Theorem`, Answer/Summary/discussion sections; the check enforces separate clauses, exact `claimed:` binding, and affirmative evidence syntax, while the reviewer judges whether the evidence is true |
| `HYPOTHESIS` | an explicitly identified external theorem invoked with its own hypotheses absent nearby, or an ambiguous bare surname | exact composite identities before shorter names; keyword proximity still **does not** catch hypothesis/conclusion confusion |
| `LEDGER` | a missing ledger, or any empty cell | presence and completeness, not honesty |
| `TAG` | a hypothesis not marked `[supplied]` or `[satisfied]` | cannot tell whether your tag is honest |
| `HEADLINE` | the `**thesis**` row has a `[supplied]` hypothesis while the **title** carries no qualifier | title only; supplied hypotheses on separate secondary claims do not demote an independently closed thesis |
| `THESIS` | not exactly one Claim cell marked `**thesis**`, or a title the marked row does not cover | uses normalized, length-aware title/claim matching; cannot tell whether the row you marked is substantively the headline claim |

The linter is a filter, not a judge. Its self-test
(`--selftest tests/fixtures/inference_audit/selftest_cases.json`) asserts it
fires on the reconstructed historical defects and, as a negative control, that
it stays silent on a complete note.

## Failure modes this is built from

Each row is a defect that reached a value gate.

| cycle | what shipped | class |
|---|---|---|
| 701 | independence inferred from symbol-disjointness in separately transcribed equations — true by construction | no falsifier |
| 702 | "supplies no dimensionless content" read as "selects zero"; long-rangedness inferred from the symbol at one `k` | direction; over-general |
| 704 | formation and migration gates written with identical bodies, then "verified" to agree over 2187 rules | clone |
| 705 | theorem correctly qualified; the discussion restated it without the qualifier, making it false. Separately, an author-chosen objective described as a functional "the framework already carries" | restatement; import as support |
| 707 | Rellich invoked without its analyticity hypothesis and the conclusion called unconditional; "permits" shown, "requires" claimed; a control row that sliced away its own counterexample | hypotheses; direction; slice |

## Ledger completeness is necessary and not sufficient

The first cycle run under this audit (708) **passed** the linter and was still
rejected for the exact failure the audit was built to stop. The author recorded
the supplied operator-family hypothesis in the Hypotheses cell, and then titled
the note *"…and Covariance Repairs It Without New Input"*. The reviewer's words:

> "Listing the family in the Hypotheses column does not cure the headline
> claim. The inference audit is therefore syntactically complete but not
> substantively discriminating."

`TAG` and `HEADLINE` are the second layer, added in response. `HEADLINE`
follows the explicitly marked thesis row; a supplied premise on an unrelated
secondary claim does not force the whole title to become conditional.

The **next** cycle (709) then passed *both* layers and was rejected again, this
time because its complete eight-row ledger contained no row for its own thesis:

> "most importantly, the central route no-go has no ledger row or genuine
> falsifier."

`THESIS` is the third layer. Exactly one Claim cell carries the literal
`**thesis**` marker. Two mechanical designs were tried and abandoned
first — an allowlist of claim-bearing section headings missed the thesis
(it sat under "Why the route as posed cannot close"), and inverting to a
denylist flagged metadata and boilerplate in a clean note. Both fail the same
way: **a linter cannot tell a claim from a sentence.** So the author marks one
row `**thesis**` and the title must be covered by it — which forces the headline
claim to carry a Support, a tagged Hypotheses cell and a Falsifier like every
other claim. The lesson
generalizes: **a mechanical check makes a defect visible; it does not make you
honest about it** — and each layer has been defeated by the next cycle finding
a place the check does not look. Expect that to continue; add the layer rather
than re-resolving to be careful. If the thesis row is `[supplied]`, the title
must say so — the reader of a title is exactly the person who will not read the
ledger.

## What this does not do

It does not check that the mathematics is right — the runner and the reviewer
do that. It checks that the sentences do not exceed the mathematics. A note can
pass this audit and still be wrong, thin, or duplicative; steps 2, 8 and the
cluster-cap evaluator are the other gates.
