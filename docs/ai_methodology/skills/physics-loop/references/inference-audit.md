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
  by construction). The tag is the load-bearing part: it is the distinction
  whose absence caused the first cycle run under this audit to pass the audit
  and still be rejected.
  Not the conclusion. The linter's keyword check catches outright omission but
  **cannot** distinguish a hypothesis from a conclusion; this column is the only
  thing that does. A cited theorem whose hypotheses you cannot state is a
  theorem you are not entitled to use.
- **Shown vs claimed** — what the evidence establishes, then what the sentence
  asserts, as two clauses. This column exists because "X permits Y" and "Y
  requires X" are different statements and the second does not follow from the
  first.
- **Falsifier** — a concrete state of the world that would make the claim
  false. If you cannot name one, the claim is true by construction and is not a
  result.

## Checks the linter runs

| check | catches | limitation |
|---|---|---|
| `SLICE` | a check row iterating a narrowed domain (`for g in hill[:1]`), leaving the dropped elements untested | iteration position only; a display truncation is ignored |
| `CLONE` | two functions with identical bodies modulo names, then "verified" to agree | exact structural clones only |
| `DIRECTION` | a necessity word in claim position with no converse recorded in the ledger | claim positions only — title, `**Theorem`, Answer/Summary sections — since flagging proof internals was too noisy to run |
| `HYPOTHESIS` | a named external theorem invoked with its hypotheses absent nearby | keyword proximity; **does not** catch hypothesis/conclusion confusion |
| `LEDGER` | a missing ledger, or any empty cell | presence and completeness, not honesty |
| `TAG` | a hypothesis not marked `[supplied]` or `[satisfied]` | cannot tell whether your tag is honest |
| `HEADLINE` | any `[supplied]` row while the **title** carries no qualifier | title only; a body that overclaims is the reviewer's job |

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

`TAG` and `HEADLINE` are the second layer, added in response. The lesson
generalizes: **a mechanical check makes a defect visible; it does not make you
honest about it.** If a row is `[supplied]`, the title must say so — the reader
of a title is exactly the person who will not read the ledger.

## What this does not do

It does not check that the mathematics is right — the runner and the reviewer
do that. It checks that the sentences do not exceed the mathematics. A note can
pass this audit and still be wrong, thin, or duplicative; steps 2, 8 and the
cluster-cap evaluator are the other gates.
