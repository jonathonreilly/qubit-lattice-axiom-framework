# Generation Weight Dial: Shape Forced, Value Unfixed (from the Qualification) — Bounded Theorem

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the canonical `C3` generation readout context, every weight
rule that is lawful (single-valued on its supplied domain) and invariant under
the supplied automorphisms — the `C3` action and the supplied readout-context
antiunitary `K`/CPT exchange of the two doublet characters — lies on the
one-parameter dial `rho = diag(p_s, p_d/2, p_d/2)`. Doublet-internal equality is
forced; the singlet-versus-doublet split is not. By the axiom memo's own
Qualification, the point on that dial is a choice not fixed by the supplied
structure, so a law may not depend on it unless the choice is admitted or a
dynamical selection law is derived. This note derives no `r` value, prefers no
`r` value, claims no uniqueness of the dial family beyond the stated
invariant-conditioning scope, touches no quark/neutrino lane, proposes no axiom
change, and sets no audit status.
**Status authority:** independent audit lane only. This source note sets no audit
outcome, predicts no audit outcome, and changes no registry row.
**Current-main posture (2026-07-11):** banked as bounded supporting science in the
`r = 1/2` lane. It reopens, modifies, and supplies authority for no admission or
retirement record.
**Primary runner:**
[`scripts/frontier_koide_dial_shape_qualification_2026_07_11.py`](../scripts/frontier_koide_dial_shape_qualification_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_dial_shape_qualification_2026_07_11.txt`](../logs/runner-cache/frontier_koide_dial_shape_qualification_2026_07_11.txt)
(15 checks, all PASS)

## Purpose

The `r = 1/2` lane has a stable dial setting but no unconditional derivation of
the value. Prior lane work established negative facts — the listed `C3`/`S3`
symmetry routes do not fix `r = 1/2`
([`KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md)).
This note states the strongest **unconditional** positive statement the lane
currently supports, using only axiom sentences and the canonical readout
context:

1. the **shape** of every lawful automorphism-invariant weight rule on the
   generation context is forced onto a single one-parameter dial;
2. the **point** on that dial is, by the Qualification's own dichotomy, an
   unfixed choice — hence why the value is registered data today rather than a
   derived law.

This is a shape/value separation. It does not close the value question; it
certifies that the value question is open in the precise sense the Qualification
names.

## Supplied premises (named exactly)

Two kinds of input are used, and they are kept distinct throughout.

### Axiom content (quoted verbatim from `docs/MINIMAL_AXIOMS_2026-06-29.md`)

The **Qualification** (law/choice discipline):

> In particular, a law may not depend on a choice not fixed by the supplied
> structure, unless that choice is admitted.

> A state is a configuration of records.

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

The **Qubit** non-privilege sentence:

> No possibility is privileged. Possibilities are distinguished by the supplied
> algebraic structure alone.

### Supplied readout-context content (NOT axiom content)

The theorem is **conditional** on two supplied elements of the canonical
context; neither is promoted to axiom content, and the axiom memo explicitly
leaves `K`/CPT structure downstream:

- **S1 — the canonical `C3` generation readout context.** The `hw = 1`
  generation factor identified with `C^3`, cyclic shift `U`, supplied circulant
  class `Y = a I + b U + conj(b) U^{-1}`, with two cells: the **singlet cell**
  (unit direction `I`, the eigenvalue-`1` character of `U`) and the **doublet
  cell** (the Hilbert–Schmidt orthocomplement `B = J - I`, the two remaining
  characters). Source:
  [`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md).
  This supplies the `C3` action `U`.

- **S2 — the antiunitary `K`/CPT exchange of the two doublet characters.** The
  standard-basis conjugation `K` that identifies the two doublet characters
  `omega <-> conj(omega)` as one `K`/CPT orbit (the "doublet `K`-orbit outcome
  `d`" of the canonical context). Per the axiom memo, "`K`/CPT orbit structure,
  central-sector decomposition, and any sector generation rule are downstream
  readout-context content, not generic axiom content," and "context selection,
  measurement basis selection, Born weights, probability rules" remain outside
  axiom content. **`K`/CPT structure is therefore a supplied readout-context
  element, not axiom content.** T1 below is conditional on S2; the note names it
  as such and does not silently upgrade it.

**Provenance note on S2 (read carefully).** In the standard basis `U` is a real
permutation, so `K` (coordinate conjugation) commutes with `U` as operators.
`K` nonetheless exchanges the two doublet characters, because it is antilinear:
if `U v = omega v` then `U (K v) = K (U v) = conj(omega) (K v)`, so `K` carries
the `omega`-eigenspace to the `conj(omega)`-eigenspace and fixes the real
singlet eigenspace. The exchange is a consequence of antilinearity, not of a
`U -> U^{-1}` relation. Runner CHECK 06 verifies exactly this.

## T1 — Dial shape is forced

**Statement.** Let `w` be a weight rule on the canonical `C3` generation readout
context that (law discipline) gives exactly one answer wherever its supplied
condition holds, and (Qubit non-privilege) depends only on the supplied
algebraic structure — the `C3` action `U` (S1) and the antiunitary `K`/CPT
doublet-character exchange (S2). Then the output state `rho` on the 3-dimensional
carrier `C^3` is invariant under the supplied automorphism group generated by
`U` and `K`, and every such invariant state has the form, in the character
(DFT) basis,

```text
rho = diag(p_s, p_d/2, p_d/2),   p_s, p_d >= 0.
```

Doublet-internal equality (`p_d/2 = p_d/2`) is **forced**. The singlet-versus-
doublet split (`p_s` vs `p_d`) is **not** forced. The invariant family is a
one-parameter dial; its coordinate is `r = p_d/(2 p_s)`.

**Proof.**

*Lawful ⇒ invariant.* The supplied condition (the canonical context) is fixed by
every supplied automorphism. A rule that "privileges no states" and is
"distinguished by the supplied algebraic structure alone" cannot produce an
output that distinguishes states the structure does not distinguish; hence its
single output `rho` commutes with the supplied unitary `U` and is fixed by the
supplied antiunitary `K`. So `rho` is an invariant state.

*`C3`-invariance ⇒ character-diagonal.* `U` has three distinct eigenvalues
`{1, omega, conj(omega)}` (three inequivalent `C3` characters; CHECK 02). Its
commutant is exactly the circulant algebra — the char-diagonal matrices, complex
dimension 3 (CHECK 04). A `C3`-invariant Hermitian state is therefore
`rho = a I + b U + conj(b) U^{-1}` with `a` real, `b` complex — three real
parameters. In the character basis this is `diag(p_0, p_1, p_2)` with the two
doublet weights `p_1, p_2` **free**: `p_1 = p_2` iff `b` is real, and `p_1 != p_2`
for non-real `b` (CHECK 05). So `C3` alone does **not** equalize the doublet.

*Antiunitary exchange ⇒ doublet-internal equality.* `K`-invariance
`K rho K^{-1} = rho` reads, in the standard basis, `conj(rho) = rho`, forcing the
circulant coefficient `b` real, hence `p_1 = p_2` (CHECK 06, CHECK 07). The joint
invariant Hermitian state space then has real dimension 2 and equals exactly
`{diag(p_s, p_d/2, p_d/2)}` (CHECK 07); 200 random Hermitian states project onto
this form (CHECK 08).

*Split not forced — the obstruction.* The singlet cell is the rank-1 projector
onto the eigenvalue-`1` character; the doublet cell is the rank-2 projector onto
the other two characters. No supplied automorphism, unitary or antiunitary, maps
the rank-1 cell to the rank-2 cell: a unitary or antiunitary preserves subspace
dimension, and `1 != 2` (CHECK 09). Equivalently, every one of the six group
elements fixes the singlet cell and permutes the doublet characters among
themselves, so the singlet orbit never meets the doublet cell (CHECK 10). Hence
`p_s` and `p_d` are independent invariants: the split is a genuinely free ratio.
The dial is one-parameter, coordinate `r = p_d/(2 p_s)`. ∎

## T2 — Value is unfixed: the admission dichotomy

**Statement.** There exist two weight rules, both lawful and both invariant under
everything in T1, that assign different `r`. Under the ratified component
dictionary `p_s = a^2`, `p_d = 2|b|^2`, `r = p_d/(2 p_s)` (reading the singlet
cell weight as `p_s` and the total doublet weight as `p_d`):

- the **dimension rule** `rho = I/3 = diag(1/3, 1/3, 1/3)` (equal weight per
  carrier dimension) gives `r = 1` (CHECK 11);
- the **cell-equipartition rule** `rho = diag(1/2, 1/4, 1/4)` (equal weight per
  cell, split evenly inside the doublet) gives `r = 1/2` (CHECK 12).

Both are single-valued on the supplied domain and invariant under `U` and `K`
(CHECK 11, CHECK 12). They disagree: `1 != 1/2` (CHECK 13). Therefore the
singlet/doublet weight is, in the Qualification's exact words, "a choice not
fixed by the supplied structure." By the Qualification, "a law may not depend on
a choice not fixed by the supplied structure, unless that choice is admitted." ∎

The two rules are the two most symmetric readings of "no possibility is
privileged": privilege no **dimension** (uniform over the three characters) or
privilege no **cell** (uniform over the two outcome cells). The supplied
structure distinguishes the two cells but assigns no relative weight between
them, so it does not adjudicate between counting dimensions and counting cells.
That undetermined arbitration **is** the free coordinate `r`.

**Corollary (stated plainly).** The current lane configuration — filing the value
as a realized-state registered datum together with an owner-governed grain
license — is the Qualification-compliant configuration, because it neither
smuggles the unfixed choice into a law nor asserts a derivation the structure
does not supply. The only lawful alternatives to registration are (a) an explicit
admission of the cell weight, or (b) a derived dynamical selection law. The open
derivational consumer for route (b) is the durability/`kappa` lane; this note
states that as the named open consumer and takes no dependence on it and derives
no part of it.

## T3 — Consistency corollary (recovers the known facts)

T1 recovers, as special cases, the symmetry facts of
[`KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md).
This is consistency, not novelty.

- **`C3` leaves `r` free.** Under `C3` alone the doublet-split coordinate is a
  free real parameter (two `C3`-invariant states with different doublet weights;
  CHECK 05, CHECK 15). That is exactly the no-go's "`C3` leaves `r` free
  (`Q = (1 + 2r)/3` is non-constant)."
- **No unitary singlet/doublet swap.** The rank/dimension obstruction `1 != 2`
  forbids any unitary in the supplied group from swapping the cells (CHECK 09,
  CHECK 15) — the no-go's "the singlet (dim 1) and doublet (dim 2) are
  different-dimensional irreps, so no unitary singlet/doublet swap exists."
- **Norm-balance dictionary.** With `p_s = a^2`, `p_d = 2|b|^2`, one has
  `r = |b|^2/a^2 = p_d/(2 p_s)`, `Q = (1 + 2r)/3`, and `r = 1/2` iff the channel
  energies balance `E_+ = 3 a^2 = E_perp = 6|b|^2` (CHECK 14) — the no-go's
  equal-channel-energy characterization of `r = 1/2`.

## Overlap check — what is new versus the Frobenius isotype-weight no-go

Compared with
[`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md).
**Verdict: this note is NOT a restatement of the Frobenius note.** There is a
real structural echo — each ends with one ratio freedom between two isotype
blocks — but the object, the group, the equalizing mechanism, and the binding
content all differ.

| | Frobenius note (2026-04-21) | This note (2026-07-11) |
|---|---|---|
| Object classified | Ad-invariant **inner products** (bilinear forms `alpha Tr(AB) + beta tr(A)tr(B)`) | Automorphism-invariant **states / weight rules** `rho` |
| Underlying space | operator space `Herm(3)` (real dim 9) | outcome carrier `C^3` (the readout cells) |
| Symmetry group | full **adjoint** action (SU(3)/U(3)) | **`C3`** cyclic group + supplied **antiunitary `K`** exchange |
| Isotype decomposition | scalar (dim 1) ⊕ traceless (dim 8) | singlet character ⊕ two doublet characters |
| Why the "internal" block is equal-weighted | automatic by **Schur** (the 8-dim traceless block is a single irreducible Ad-isotype) | **not** automatic — the two doublet characters are inequivalent 1-dim `C3` irreps; equality is forced only by the **supplied antiunitary S2** |
| Freedom left | scalar/traceless weight ratio `beta/alpha` | singlet/doublet split ratio `r` |
| Binding new content | none of the below | the **Qualification admission dichotomy**: the free ratio is a "choice not fixed by the supplied structure," so a law may not depend on it unless admitted or derived |
| Grounding | pre-reset linear-algebra premises (PD + Ad-invariance + orthogonality) | post-reset **axiom sentences** (Qualification, law discipline, Qubit non-privilege) + canonical context |

What the Qualification adds that the Frobenius note lacks: the Frobenius note
ends at "future positive work must supply an independent authority that fixes the
ratio." This note converts the residual freedom into a **named dichotomy** — the
value is registered data, or it is admitted, or it is derived as a dynamical law
— grounded in an axiom sentence rather than in an external appeal. The equalizing
mechanism is also genuinely different: Frobenius gets internal equality for free
by Schur on an irreducible block, whereas here the two doublet characters are
inequivalent under the group that is actually supplied (`C3`), and their equality
is a **conditional** consequence of the named antiunitary S2. Remove S2 and the
doublet split reopens (CHECK 05); there is no analog of that dependence in the
Frobenius picture.

## What this note does NOT claim

- Does not derive, prefer, or predict any `r` value (in particular does not
  derive `r = 1/2`).
- Does not claim the dial family is unique beyond the stated
  invariant-conditioning scope (lawful automorphism-invariant weight rules on
  this canonical context under the group generated by `U` and `K`).
- Does not promote the antiunitary `K`/CPT exchange to axiom content; T1 is
  conditional on the supplied readout-context element S2, and this is stated in
  the premise list.
- Does not touch the quark or neutrino lanes.
- Does not propose or depend on any axiom change, primitive registration, or
  Tier-A admission; sets no audit status and uses no `effective_status`/audit
  language.
- Does not consume PDG values, fitted selectors, lattice numerics, or unit
  conventions. The charged-lepton `Q = 2/3` is a comparator only, not an input.
- Does not derive the durability/`kappa` dynamical selection law; it names that
  lane as the open derivational consumer and takes no dependence on it.

## Boundaries and residues

- The shape result T1 is unconditional given S1 and S2; the value result T2 is
  the statement that the shape's one coordinate is not fixed by the supplied
  structure. Neither closes the value question.
- The open positive route is a derived dynamical selection law (route (b) of the
  T2 corollary), gated on the durability/`kappa` lane. Nothing here derives it.
- If a later authority admits the cell weight (route (a)), the value becomes a
  registered admission rather than a derived law; that admission is an
  owner/audit action, not a content of this note.

## Validation

Run:

```bash
python3 scripts/frontier_koide_dial_shape_qualification_2026_07_11.py
```

Expected terminal form: `CHECK NN: PASS/FAIL -- <description>` lines followed by
the four-line summary whose final line is `TOTAL: PASS=15 FAIL=0`. The 15 checks:
(01) `U` unitary of order 3; (02) three distinct `C3` characters; (03) `U`
diagonal in the character basis; (04) commutant = circulant algebra (dim 3);
(05) `C3` alone leaves the doublet weights free; (06) antiunitary `K` swaps the
doublet characters, fixes the singlet; (07) `K`-invariance forces `p_1 = p_2`
(joint-invariant states = `diag(p_s, p_d/2, p_d/2)`, real dim 2); (08) robustness
over 200 random states; (09) cell rank obstruction (no singlet→doublet map);
(10) cell orbit obstruction; (11) dimension rule `rho = I/3` gives `r = 1`;
(12) cell-equipartition rule `diag(1/2,1/4,1/4)` gives `r = 1/2`; (13) admission
dichotomy witness (`1 != 1/2`); (14) dictionary/`Q`/equal-energy consistency;
(15) file-4 recovery (`C3` leaves `r` free; no unitary swap).

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Qualification,
  law-discipline, and Qubit non-privilege sentences (quoted verbatim above); and
  the memo's statement that `K`/CPT structure is downstream readout-context
  content.
- [`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md)
  — the canonical context, its two cells, and the ratified component dictionary
  `p_s = a^2`, `p_d = 2|b|^2`, `r = p_d/(2 p_s)`.

## Cross-references

- [`KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md)
  — T3 recovers its `C3`-leaves-`r`-free and no-unitary-swap facts; consistent
  with its equal-channel-energy characterization of `r = 1/2`.
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — overlap check above; distinct object (states vs inner products), group
  (`C3`+antiunitary vs Ad), equalizing mechanism, and binding content
  (Qualification dichotomy).
