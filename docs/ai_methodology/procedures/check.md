# check

Decide independently whether one statement is right as written, and leave a
record from which its standing is computed (`RULES.md` sections 1 and 3). A
check is not a landing review and not an audit.

## Use when

A statement is about to be built on: at an interface between parts, when a
published result is rebuilt in `library/`, before heavy work rests on a
bridge, and at assembly. An author's own skeptic pass writes no record.

## Takes

- One named statement at one pushed commit, with quantifiers, domain and
  premises. If any is missing or still changing, record `undecided` and stop.
- The raw artifacts: text, proof, runner source, logs, cited sources and the
  target's search records. Keep any new search short (`SETTINGS.md`).
- A neutral brief naming the statement, commit and consumer. It carries no
  author conclusion, favoured route or other checker's verdict.
- A checker outside the author's lineage that passes
  `lab_ops.py preflight --role checker` (`SETTINGS.md`, models by role).

## Steps

1. Fix the claim: conclusion, quantifiers, domain, edge cases, each premise.
   Decide whether it claims a formal implication only or also a physical
   identification. The verdict covers exactly what it claims.
2. Read line by line and redo the load-bearing step by a different derivation
   or implementation. Two results traced to one expected constant are one
   path. Do not catalogue inputs; report one only if it is false or missing.
3. Attack the bridges before the algebra: what is selected, fitted, imposed,
   conventional, finite-order or shown in one setting only. Judge against the
   stated premises and axioms; known physics is a disclosed comparator only.
4. In a proof, confirm each reduction keeps hypotheses and domain, each
   constructed object meets the definition required, boundary, degenerate and
   normalization cases are covered, and no equivalent of the target is used.
5. In a computation, a passing runner is never sufficient. Trace every number
   to its origin. Drop or perturb a term and confirm the test fails. A constant
   with no derivation is fitted; a rounded or proxy quantity is not the one
   claimed. Name the one-line bug that would give this result; look for it.
6. Verify every cited number, log and source at its origin. Settle a clash
   with another statement on exact domains and proofs, never on standing.
7. Answer three questions: is it right; are the open obligations fewer or
   strictly weaker; which consumer's exact input does it deliver. Reaching a
   lemma equivalent to or stronger than the target is not a reduction.
8. Decide. `right` needs your own path to close. `wrong` needs a failing step
   or a counterexample inside the stated domain that others can verify; a
   count of concerns is neither. Otherwise `undecided`, unfinished runs too.
9. Write the record, commit it with your `Provenance` trailer and push.

## The record

One file per check, `checks/<statement>-<commit>.md` (twelve hex digits; add
`-b`, `-c` if taken), never edited once pushed. Front matter is flat lines.

```text
---
statement: <descriptive-name, never a bare code>
commit: <40 hex>
content: <sha256>
text:
  - <sha256> <path>[#<heading>]
reads:
  - <sha256> <statement>|- <path>[#<heading>]
verdict: right|wrong|undecided
failure: none|step <path>:<line>|counterexample <path>:<line>
path: <derivation or implementation used, and how it differs>
checker: <provider>/<model>/<effort> <session id>
author: <provider>/<model>/<effort> <session id>
answers: <record files>|none
steer: advance <consumer>|no-advance|none
---
```

`lab_ops.py check-hash` prints the `content`, `text` and `reads` lines: SHA-256
of the file, or with `#<heading>` of that section up to the next heading of
equal or higher level (it must occur once). Names have no spaces. `text` is
the statement and its argument; `reads` is every premise, lemma, number, log
and runner it reads, led by its statement name or `-`. `author` is the
`Provenance` of the commit that last changed `text`. `answers` names records
whose verdict this one tests by a third path. `steer` (`advance`: yes to
questions two and three) is never standing. Body: `## Finding`, `## Not run`.

`lab_ops.py status` computes standing. It rejects a record with a missing,
repeated or unknown field, one session on both sides or a wrong `content`.
A record counts while every hash matches and no live record `answers` it.
Every `wrong` record, even about an earlier text, and every rejected one that
does not plainly say `right` or `undecided`, keeps `checked` away until a live
record `answers` it. `right` and `wrong` together leave the statement `argued`,
shown as disputed; else a counterexample gives `refuted`, another `wrong`
`open`, and a `right` `checked` given its reads. Answers in a circle are void.

## Obstructions

Check an obstruction as a theorem (`RULES.md` section 2, rule 6) and answer
two more questions in `## Finding`:

1. Is the family ruled out stated with explicit quantifiers: which objects,
   premises and resolution (element, site, mode, block or lattice)?
2. Does every title, summary and citing statement claim no more than that?

An open admissible route inside the family makes the statement `wrong` as
written; an escape outside it refutes nothing. Conditions called independent
need both non-implications shown. A cited result counts only if it attacks
the same residual. An obstruction that a relabelling, a convention or a
published route removes is not the physical one claimed.

Interim rule. The N1 to N8 packet is a checker's aid: prompts, never a verdict.
Until the tooling changes it stays required by `land` (answers committed with
the note; five N5 runner-output lines, checked by script), by `audit` (the
packet and its five-route quota) and, in prose, by the older `no-go-discipline`
skill. A check neither writes nor grades it: never `wrong` for a missing or
short packet, never `right` for a passing one, never an invented route family.
Note its state in the record body; a packet failing the schema stays pending.

## At assembly

The conclusion matches the `GOAL.md` contract, quantifiers included. The
obligation graph is acyclic and every leaf is `checked`. Each interface
statement is one text on both sides. Nothing equivalent to the target is
imported or renamed. Computation is proof only where exhaustive or made
decisive by a theorem. Record the result with every constituent in `reads`.

## Ends

With one pushed record and a report to whoever asked: the verdict, the failing
step or counterexample, and what was not run. A `wrong` goes to `repair`.

## Never

- Check your own lineage, or count a same-lineage isolated pass as a check.
- Read the author's conclusion, or a record you do not answer, before deciding.
- Edit or repair the source you check, or change GitHub state.
- Put a verdict, a standing or a `steer` value into a title, a note's status
  line, a ledger field or an audit packet.
- Claim more in the record than its path verified, or fabricate a run.
- Record `right` to unblock a consumer, or `wrong` for a packaging gap.

## Step references

Read one only at the step that needs it.

| Step | On `main`, in `docs/ai_methodology/skills/` unless `.claude/` | Why |
|---|---|---|
| 1, 3, 5 | `.claude/commands/` `theory-review`, `sanity`, `validate` | Lists |
| 3 | `PRIMITIVE_REGISTRY_CHECK.md` | What each approved primitive grants |
| 4, 7 | `physics-loop/references/proof-search-governance.md` | Also assembly |
| 5, Obstructions | `physics-claim-reviewer/SKILL.md` | Its two batteries |
| Obstructions | `no-go-discipline/` (skill, case studies) | N1 to N8 prompts |
