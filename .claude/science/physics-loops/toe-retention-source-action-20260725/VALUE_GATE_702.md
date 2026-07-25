# Promotion Value Gate — Cycle 702

Answered before the PR. Not an audit certificate; predicts no audit verdict.

## V1 — obstruction

Two, both quoted verbatim from audit verdicts:

- `gate_b_farfield_note`: *"cite or derive retained connections from the accepted
  framework premises to the growth rule, source field, propagation/action rule,
  and TOWARD/F~M physical readout before seeking a non-conditional physics
  verdict."*
- `gravity_law_cleanup_note` (five-judge panel): *"the minimal-axiom authority
  expressly withholds dynamics, weights, source/action, and physical-observable
  bridges, while the runner stipulates each of those ingredients."*

Part I addresses the **propagation/action rule** clause: it shows the rule is
not free in the way the panel's wording suggests, because exactly one member of
the covariance-forced family can be written without supplying a dimensionless
number. Part II addresses a different obstruction — the coherence of the Record
additivity clause against the Admissibility "vary with" clause — which no
verdict names because it has not been noticed.

## V2 — new derivation, with the sweep

**Searched commit `7d896653f0`** (and `49213b5b5b` for Part II's sweep),
refreshed immediately before each sweep.

| # | command | hits | classification |
|---|---|---|---|
| S1 | `git grep -n -iE "needs no (supplied\|dimensionless)\|without supplying a dimensionless\|unique member.{0,40}(no\|zero) (supplied\|dimensionless)" origin/main -- 'docs/*.md'` | **none** | absence |
| S2 | `git grep -n -iE "yukawa.{0,40}(screening\|mass term)\|screening length.{0,40}lattice unit" origin/main -- 'docs/*.md'` | 2026-04-11 memory-decay diagnostics; a Higgs-Yukawa selection note; a spectral-trajectory note quoting a numerical screening length | **nonmatching.** All are numerical or empirical diagnoses on particular runners, not a classification of the covariant law family. |
| S3 | `git grep -n -i "zero dimensionless content" origin/main -- 'docs/*.md'` | eight notes | **method precedent, opposite direction.** Every hit uses the clause as a **blocker** — "the primitive supplies nothing dimensionless, so this route is BLOCKED". None uses it as a **selector**. |
| R1 | `git grep -n -iE "hereditar\|downward.closed\|upward.closed\|monotone.{0,25}(rule\|admissib)\|antitone" origin/main -- 'docs/*.md'` | monotone-closure hits are about **formation** as a closure operator, in `work_history/review_feedback` | **nonmatching** |
| R2 | `git grep -n -iE "additivity.{0,40}(incompatib\|tension\|conflict)" origin/main -- 'docs/*.md'` | the Darwinism note's additivity-vs-redundancy tension; a theta post-erasure additivity incompatibility | **nonmatching.** Different tensions: redundancy/saturation, and a log-equivalence on the theta side. Neither is additivity against varying availability. |
| R3 | `git grep -n -iE "rule (must be\|is forced to be) constant\|constant admissibility rule" origin/main -- 'docs/*.md'` | **none** | absence |

New content: the identification of `A = 0` as the unique member of the landed
family writable without a supplied dimensionless number, with the Yukawa
screening length that the alternatives carry; and the incompatibility of the
unrestricted additivity clause with the "vary with" clause, exhaustive over the
count-only rule space.

## V3 — could the audit lane already do this from retained primitives plus standard math?

The mathematics is elementary in both parts — a symbol at zero momentum, a
quadratic expansion, and a monotone/antitone lattice argument. What is not
available to the audit lane is the **reading**: S3 shows the repo consistently
uses the scale primitive's "zero dimensionless content" clause to *block*
routes. Using the same clause in the opposite direction, to distinguish the one
member of a classified family that needs no dimensionless input, is not a move
the corpus has made. Part II likewise turns an axiom-coherence question nobody
has posed into an exhaustive negative.

## V4 — non-trivial?

Yes, and deliberately bounded. Part I's chain is four exact computations, one of
which (P4) is an entrywise matrix identity with a wrong-rescaling control. Part
II's Q3 is exhaustive over 2187 rules with Q4 as a live-filter control showing 24
rules pass exactly one closure. The step from Part I's computations to the
"needs no supplied number" statement is an argument about quoted primitive text
and is flagged in the note as such rather than presented as computed.

## V5 — one-step variant?

**Checked against `origin/main` at `7d896653f0`.** No. Against the landed kernel
classification: that note classifies the family and explicitly disclaims
deriving that a law is linear, local, covariant, or constant-annihilating; it
says nothing about which member needs a supplied number, and nothing about
screening. Against landed cycles 698/699: no law, no symbol, no admissibility
rule. Against the campaign's backlogged cycle 700: that note showed closure can
fail for *some* rules; Part II shows no varying rule can have **both** closures,
which is a different and strictly stronger statement, and it is what makes the
result a constraint on the law rather than a caveat.

**Verdict: PR allowed.**

## Owner direction

This cycle exists because the owner declined to accept a counting convention
unless it were obvious, and asked to build from the already-granted Planck scale
toward identifying the law. Neither part adopts a convention of any kind.
