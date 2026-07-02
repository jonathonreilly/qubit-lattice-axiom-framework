# CTX Canonical Two-Cell Family: Generation Discharge and the EW Instance

**Date:** 2026-07-02
**Type:** bounded theorem (family definition + discharge + instance)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note writes no audit
verdict, sets no audit status, and predicts no audit outcome. Any status change
is effective only upon the independent audit lane's own action.
**Actual current surface status:** the parent EW `kappa_EW` no-go stands as
written; the generation-side and EW-side CTX questions live in review-pending
sibling blocks whose statuses belong to the audit lane. This note adds a
note-level family definition and exhibits finite witnesses; it moves no wall.
**Primary runner:**
[`scripts/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.py`](../scripts/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.py)
**Runner output:**
[`outputs/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.txt`](../outputs/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.txt)
— `TOTAL: PASS=24 FAIL=0`.

## FIREWALL (read first)

- **Nothing is adjudicated here.** This note sets no audit status and predicts
  no audit outcome.
- **No wall is closed.** The parent EW no-go
  (`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`) — "the
  approved axiom and primitive baseline supplies no weighting rule" — is **not
  closed** by anything below and stands exactly as written.
- **Sibling blocks are review-pending.** Blocks 08 (PR #4823), 11 (PR #4826),
  16 (PR #4846), 17 (PR #4849), and 18 (PR #4852) are review-pending; their
  statuses belong to the independent audit lane. This note reads none of their
  branches; it quotes only the supervisor-supplied residuals below and reasons
  against **landed on-main** text.
- **The T3 EW identification is a named instance premise with witnesses, not a
  ruling.** It is stated as the instance premise this note supplies finite
  witnesses for; it is not an adjudication that the EW cells are placed here.
- **No axiom, policy, primitive, or registry content** is added or modified.
  The canonical family is a note-level *definition* (as block11 defined its
  class), not new axiom content.
- **No value of `kappa_EW` is claimed** — not `0`, not `1`, not any number.

## Purpose

Two landed surfaces already fix a two-cell readout structure and its arithmetic:
the `C_3` generation context (owner-ratified naming) and the EW color family
`Pi_phys = C + kappa_EW S`. This note (i) names, at note level, the **canonical
two-cell context** they are both instances of; (ii) discharges the
generation-side CTX-match residual onto the already-landed owner ratification;
(iii) exhibits the EW color surface as a witnessed instance of the same family;
(iv) states, conditionally and honestly, what the review-pending class results
then instantiate to. This is bookkeeping of *what is already landed* plus finite
witnesses — not new physics and not a verdict.

## Supplied Surface (quoted; landed on-main) [checks 01-08]

**Canonical `C_3` context — Definition** (from
`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`,
owner-ratified, quoted verbatim):

> 1. the **singlet cell**: the algebra unit direction `I`;
> 2. the **doublet cell**: the Hilbert-Schmidt orthocomplement of the unit
>    inside the circulant span (represented by `B = J - I`).
> With Hilbert-Schmidt normalization `||I||^2 = 3`, `||B||^2 = 6`, `<I, B> = 0`.

**Ratified naming equivalence** (same note, verbatim):

> The following are two namings of the same two cells of this one context, not
> two independent structures:
> - the **outcome naming**: the singlet outcome `s` and the doublet `K`-orbit
>   outcome `d`, with component-dictionary registered weights `p_s = a^2`,
>   `p_d = 2|b|^2`;
> - the **channel naming**: the unit channel `I` and the complement channel
>   `B`, with channel Hilbert-Schmidt energies `(3 a^2, 6 |b|^2)`.
> The registered weights and the channel energies are the same quadratic
> contents up to the common factor `N = 3`, which cancels from every equal-cell
> condition.

**Parent kappa surface — Load-Bearing Fact 1** (from
`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`, verbatim):

> The EW color readout uses a family `Pi_phys = C + kappa_EW S`, where `C` and
> `S` are the adjoint and singlet channel contributions. ... The central-sector
> partition gives the cardinality count `8/9`; it does not pick the inter-sector
> weight `kappa_EW`.

The audit-ledger rationale for that count states the arithmetic as its own
formula: `8/9 = (3^2 - 1)/3^2`.

**Axiom sentences used** (from `MINIMAL_AXIOMS_2026-06-29.md`, verbatim):

> [Lattice] No site is privileged. Sites are distinguished by the supplied
> lattice structure alone.
> [Qubit] No possibility is privileged. Possibilities are distinguished by the
> supplied algebraic structure alone.
> [Record] A readout value is determined by record content alone. For any finite
> collection of pairwise-disjoint records, scalar readout `I` is additive, with
> `I(empty)=0`.

## T1 — The canonical two-cell family (note-level definition) [checks 09-11]

**Definition (note level, not axiom content, in the manner of block11's
class).** A **canonical two-cell context** on a supplied finite-dimensional
matrix `*`-algebra with unit and Hilbert-Schmidt inner product is the frame
`{unit direction ; HS-orthocomplement of the unit}`.

The landed `C_3` note is exactly this construction on the supplied `hw=1`
circulant span (identified with `C^3`, cyclic shift `U`, class
`Y = a I + b U + conj(b) U^{-1}`): singlet cell = algebra unit direction `I`;
doublet cell = HS orthocomplement `B = J - I = U + U^2`, with `||I||^2 = 3`,
`||B||^2 = 6`, `<I,B> = 0` (all exact, checks 09-10).

The frame is **supplied-structure-carried, not imported**. Every `*`-algebra
automorphism fixes the unit and preserves its orthocomplement; on the supplied
`C_3` slot structure this is witnessed on all six `S_3` slot-relabeling
permutation-matrix automorphisms, each of which fixes `I` and maps `B` to `B`
(check 11). The orthocomplement is always taken inside the supplied algebra
itself — for the `C_3` instance the 2-dim complement within the circulant span,
not the traceless part of any ambient algebra — and only frame-level facts
(unit-fixing, orthogonality, two-cell additivity) transfer across instances;
family membership is by-construction and classifies nothing beyond its
instances. In the manner of the Qubit distinction clause's discipline —
"Possibilities are distinguished by the supplied algebraic structure alone" —
and resting on the automorphism witnesses, the two cells are distinguished by
supplied structure alone, with no imported selector.

## T2 — Generation-side CTX-match discharges onto the landed ratification [checks 12-13]

Block08 (PR #4823, review-pending) states the CTX-match residual as:

> `CTX-match` asserts ... that: the equipartition central-sector cells and the
> carrier-measure unit/complement cells are cells of one and the same supplied
> `C_3` readout context; `s` is the unit-channel cell and `d` is the
> doublet-complement channel cell; the match is not merely an isomorphism of two
> independent two-cell diagrams.

This is what the landed `C_3` note **ratifies**, in substance — with the
orientation forced, not assumed:

| block08 residual | landed `C_3` ratification |
|---|---|
| "cells of one and the same supplied `C_3` readout context" | "two namings of the same two cells of this one context, not two independent structures" |
| "`s` is the unit-channel cell and `d` is the doublet-complement channel cell" | outcome naming `(p_s=a^2, p_d=2\|b\|^2)` vs channel naming energies `(3a^2, 6\|b\|^2)` — one context, two namings |
| "not merely an isomorphism of two independent diagrams" | "the same quadratic contents up to the common factor `N = 3`, which cancels from every equal-cell condition" |

The `/3` factor identity is checked exactly: channel energies
`(3a^2, 6|b|^2) = 3 * (a^2, 2|b|^2)` on rational samples with
`|b|^2 = br^2 + bi^2` (check 12), and every equal-cell condition is invariant
under that factor, `a^2 = 2|b|^2` iff `3a^2 = 6|b|^2` (check 13) — so the two
namings are the same cells, not two diagrams that happen to be isomorphic.

The `s <-> I` orientation is carried twice over: the Definition's item 1 names
the *singlet cell* as the unit direction while the outcome naming names the
*singlet outcome* `s`; and the factor-3 pairing is unique at the polynomial
level — `a^2 <-> 3a^2` with `2|b|^2 <-> 6|b|^2` is the only factor-3 matching
of the quadratics (the swap `a^2 <-> 6|b|^2` fails identically). Row 3's direct
carrier is the ratified "not two independent structures" sentence, with the
common-factor sentence supplying the same-cells arithmetic. Block08's residual
text in the left column is supervisor-quoted from a review-pending branch and
is not runner-guarded; the ratification's owner-approval record is the
2026-07-02 foundation entry in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section
6 (guarded: check 26).

Block08 also carries a **pre-reset-wording caveat** (its equipartition note
quotes pre-reset Record wording; block08 "does not read or use the current
MINIMAL_AXIOMS"). This is routed around by the landed `C_3` note directly: its
Dependencies cite the **current** axiom memo (`MINIMAL_AXIOMS_2026-06-29.md`,
Record readability/additivity and Qualification), so the ratification this note
leans on already rests on current axiom text.

**Consequence (stated carefully).** The generation-side CTX-match residual is
carried by landed, owner-ratified text. Block08 itself remains review-pending
and the audit lane owns its status; **nothing is adjudicated** here.

## T3 — The EW instance (named premise, witnessed) [checks 14-20]

The EW color surface is `M_3(C)` with the HS inner product. The canonical
two-cell frame of T1 on this algebra is `{unit I_3 direction ; traceless
orthocomplement}`. Exact witnesses:

- `Tr(I_3) = 3` and HS `||I_3||^2 = 3` (check 14);
- `dim(traceless) = 3^2 - 1 = 8`: eight exhibited exact traceless matrices with
  coordinate-matrix rank `8` over `Q` (check 15);
- `I_3` HS-orthogonal to the traceless subspace, `Tr(I_3^* T) = 0` on the basis
  and on random rational traceless combinations (check 16);
- the cardinality fraction `8/9 = (3^2 - 1)/3^2` as exact Fractions (check 17) —
  the **parent kappa note's own count** and **the ledger's own formula**;
- the frame is automorphism-canonical: conjugation by any unitary fixes `I_3`,
  preserves trace and tracelessness, and preserves the HS inner product —
  witnessed exactly on all six `3x3` permutation matrices (checks 18-20).

The parent note itself carries only the bare `8/9` cardinality count, with the
channels *named* adjoint and singlet; the audit ledger's rationale for the
parent row spells the count as `8/9 = (3^2 - 1)/3^2` (guarded: check 25). Count
and naming are consistent with, and most naturally read as, this canonical pair
— but a cardinality alone underdetermines cell structure (nine atomic sectors
grouped 8:1 give the same count), so the identification, including its
Hilbert-Schmidt structure, is supplied by the named instance premise, not by
the parent's count.

With contents `(x_C, x_S) = (adjoint content, singlet content)`, the block11
normal form on this instance is `Pi_phys = C + kappa_EW * S`.

**HONESTY.** The instance-identification premise is: *the EW readout context, as
the parent lane supplies it, is this canonical `M_3` two-cell context.* It is
supported by the parent's own count formula and channel naming, and is marked
as the **instance premise** this note supplies witnesses for — not an
adjudication.

## T4 — Kappa consequence (conditional, honest) [checks 21-23]

Under the T3 instance identification, the review-pending class results
instantiate. All statements below are conditional on that premise:

- block11's normal form `Pi = x_C + kappa*x_S` is content-determined/additive
  and reproduces the count toggle `Pi(0)=C`, `Pi(1)=C+S` at `kappa=1`
  (check 21);
- every ratio readout at **equal-cell-content** states (`x_C = x_S`) is
  `kappa_EW`-free — the common `(1+kappa)` factor cancels, matching the parent
  note's own `K_EW`-cancellation remark at class level; checked kappa-independent
  across `>= 3` `kappa` values (check 22);
- every landed EW readout in the classified lanes is kappa-free under its stated
  premise (block17, PR #4849, review-pending);
- `kappa_EW`'s remaining physical content is exactly the `W_readout_coupling`
  triple — off-diagonal evaluation, cross-family calibration, non-scale-
  referenced absolute — witnessed by the off-diagonal (`x_C != x_S`)
  kappa-sensitivity of the ratio (check 23), the honest load-bearing premise.

**The parent wall is NOT closed.** Its no-go — "the baseline supplies no
weighting rule" — stands. What changes, *conditionally*, is only that the
missing rule's remaining content is one registered-number gate plus convention,
with T3's instance premise as the only interpretive premise remaining. No
value of `kappa_EW` is claimed.

## T5 — Ladder end-state (flag; do not close) [check 24]

Block16 T4 (PR #4846): IF the EW color readout context is a two-cell instance of
the same supplier family (CTX open), THEN the class results instantiate to
`kappa_EW`. Block18 (PR #4852): `R*` and `D`-totality discharge to landed axiom
text; the ladder's non-reading residue is `{CTX}` + the gate.

Combining T2 (generation CTX discharged onto landed ratification), T3 (EW
instance exhibited with witnesses under a named premise), and review-pending
blocks 16/17/18: the carrier/`kappa` ladder carries **one named premise rung**
— the T3 EW instance premise, which is the surviving EW-side CTX residual
(block16's antecedent), now sharpened to a witnessed named premise awaiting a
`C_3`-style ratification path or equivalent supply. The residue is therefore
(i) the `W_readout_coupling` registered-number gate — supplied-content
governance, an owner surface; (ii) the T3 instance premise as the sharpened EW
CTX residual; and (iii) the ordinary audit of the review-pending siblings. A
flag, not a closure: phrasing is conditional throughout, no wall is closed,
and **nothing is adjudicated**.

## Consequence

The generation surface is an instance by the landed ratification; the EW
surface is an instance under the named T3 premise. Under that premise the review-pending class results instantiate to
the `Pi_phys` normal form with `kappa_EW` the sole one-parameter freedom, whose
residual content is a single registered-number gate plus convention. No wall
moves; the value question is untouched.

## Does NOT

- Does **not** close the EW `kappa_EW` wall and does **not** claim any value of
  `kappa_EW`.
- Does **not** adjudicate block08 or any sibling (11/16/17/18); it quotes their
  supervisor-supplied residuals and reasons against landed text only.
- Does **not** add the canonical family as axiom content — the family is a
  note-level definition, exactly as block11's class was a definition, not new
  axiom or primitive content.
- Does **not** touch the `w` classification or the `W_readout_coupling` gate
  content; those remain the registered-number owner surface.
- Does **not** set, retag, or predict any audit status.

## Dependencies

Landed, on-main:

- `docs/C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`
  (owner-ratified canonical `C_3` context Definition and naming equivalence).
- `docs/EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`
  (parent kappa no-go; Load-Bearing Fact 1; the `8/9` count).
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice and Qubit distinction clauses;
  Record content-determination and additivity).

Review-pending (quoted only; branches not read; statuses the audit lane's):
PR #4823 (block08), PR #4826 (block11), PR #4846 (block16), PR #4849 (block17),
PR #4852 (block18).

## No-Promotion Statement

This note promotes nothing. It defines a note-level family, discharges one
generation-side residual onto already-landed owner-ratified text, and exhibits
finite witnesses for a named EW instance premise. It changes no axiom,
primitive, policy, or registry surface; it sets no audit status; it claims no
value of `kappa_EW`; and it closes no wall. The review-pending siblings remain
review-pending under the independent audit lane.
