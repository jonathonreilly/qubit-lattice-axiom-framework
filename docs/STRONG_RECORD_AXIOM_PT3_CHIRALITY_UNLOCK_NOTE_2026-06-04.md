# Strong-Record-Axiom Pressure-Test #3: the Doublet Complex Structure J Does NOT Unlock the Chirality Gate

**Date:** 2026-06-04
**Claim type:** meta
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it is a
structural pressure-test of a *candidate* axiom, reporting a negative result
about that candidate's reach.
**Primary runner:**
[`scripts/frontier_strong_record_axiom_pt3_chirality_unlock.py`](../scripts/frontier_strong_record_axiom_pt3_chirality_unlock.py)
(SCORECARD PASS=36, FAIL=0)

## What was tested

A candidate "strong record axiom" is being designed:

> A record registers *which real classical alternative is realized*; the real
> classical alternatives are the real superselection sectors (real Wedderburn
> blocks); each is one alternative; record readout *counts* alternatives,
> dimension-blind.

On the three-generation space `R[Z_3] = R (+) C` the two real Wedderburn blocks
are the singlet (`R`, trivial rep) and the doublet (`C`, the 2-dim real irrep).
A bonus mechanism was proposed for the framework's *most-shared open gate* --
the charged-lepton **chirality** gate. The doublet block, read as the real
division algebra `C = R^2`, carries a canonical **complex structure** `J`
(multiplication by `i`), `J^2 = -I` on the doublet. The hope: this intrinsic
`J`, which exists only in the *real* reading, is the chiral grading the
framework needs -- an operator that anticommutes with a mass operator on the
generation `R^3` and pins the charged-lepton Koide ratio `Q = 2/3`.

The chirality mechanism the framework actually uses
([`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)):
for a Hermitian mass operator `H` with `{H, Gamma_chi} = 0`, every nonzero
eigenvector `v` satisfies `<v|Gamma_chi|v> = 0`, which is exactly `Q(v) = 2/3`.
The retained obstruction
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)):
no `Z_3`-equivariant (circulant) Hermitian operator anticommutes with the
circulant grading `Gamma_chi = (2/3) J_ones - I`, so a circulant mass operator
gives `Q = 1`, not `2/3`. The question here is whether the real-structure `J`
escapes that obstruction by being intrinsic to the doublet division algebra
rather than imposed in a site-diagonal basis.

## Verdict: DOES-NOT-UNLOCK-CHIRALITY

The doublet complex structure `J` is the **wrong algebraic object** to be a
chiral grading. Three independent, basis-independent facts each foreclose it;
the runner verifies all three.

### Obstruction 1 -- `J` is anti-Hermitian, not a `Z_2` grading

A chirality grading must be a **Hermitian involution** (`Gamma = Gamma^dagger`,
`Gamma^2 = I`, spectrum `+-1`): only then is `{H, Gamma} = 0` a sign-flip
condition on a Hermitian `H`, and only then is `<v|Gamma|v>` a real expectation
forced to vanish. But `J` is **antisymmetric** (`J^T = -J`), i.e. anti-Hermitian,
with spectrum `{0, +i, -i}`. `J^2 = -P_doub != +I`, so `J` is not an involution.
The literal axiom object `(2/3) J - I` (with `J` the complex structure) is not
even Hermitian and not an involution -- it cannot be a chirality grading. (By
contrast `Gamma_chi = (2/3) J_ones - I` *is* a Hermitian involution with
spectrum `{+1, -1, -1}`.)

### Obstruction 2 -- `J` is circulant; the involution it generates is `Gamma_chi`

`J` commutes with the cyclic shift `R`: in fact `J = (R - R^T)/sqrt(3)`, the
anti-Hermitian part of the 3-cycle. It is therefore in the circulant algebra --
not a site-diagonal accident, but also not new: it is the *same* operator that
[`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
§6.1 already identified as **commuting** with `Gamma_chi`. The only Hermitian
`Z_2` involution that splits singlet from doublet is `+-(P_sing - P_doub) =
+-Gamma_chi`, which is itself circulant -- so the retained no-go
`comm(R) cap anticomm(Gamma_chi) = {0}` applies directly (re-verified in the
runner: the symmetric-circulant anticommutant of `Gamma_chi` is `{0}`). The
real reading supplies no *new* Hermitian grading beyond `Gamma_chi`.

### Obstruction 3 -- `J`-anticommutation is vacuous (the decisive point)

This is the sharpest finding, and it corrects a naive first impression. A
nonzero real-symmetric `H` **does** anticommute with `J`: the anticommutant of
`J` on `Sym(3)` is a 3-parameter family (`H = [[f,d,e],[d,e,f],[e,f,d]]`,
verified by SVD nullspace `dim = 3`). So "no `H` anticommutes with `J`" is
*false*. But the anticommutation is **physically empty**: because `J` is
antisymmetric, `<v|J|v> = 0` for **every** real vector `v`. The
anticommuting-operator theorem's conclusion `<v|Gamma|v> = 0` therefore carries
**no information** when `Gamma = J` -- it is trivially true for all `v`, so it
imposes **no Koide constraint**. Concretely, the eigenvectors of `J`-anticommuting
`H` give a grab-bag of Koide ratios `Q in {inf, 1/2, 1/3, 1}` depending on the
three parameters -- the *prior failure modes* (`1/2` was the site-diagonal
`diag(1,-1,1)` failure; `1` is the circulant default) -- but **never** the
locked `2/3`. The whole content of the genuine mechanism is that
`<v|Gamma_chi|v>` is *generically nonzero* and vanishes *exactly* on the Koide
cone; `J` has no such selecting power.

### CPT / time-orientation does not rescue it

The proposal's CPT hook -- complex conjugation acts on the complex structure by
`K J K^{-1} = -J`, so orienting `J` ("`+J` vs `-J`") is "picking a chirality" --
is real but inert here. `+J` and `-J` have identical (vacuous) anticommutation
content and identical degenerate spectra; the runner confirms both orientations
yield the *same* Koide grab-bag and neither yields `2/3`. The arrow of time can
orient `J`, but orienting an object that imposes no constraint changes nothing.

## The Koide Q the J-grading gives

`Q != 2/3`. Specifically: `J`'s own doublet sectors have zero row-sum, giving
`Q = inf` (degenerate); `J`'s eigenvalue spectrum `{0, +i, -i}` sums to zero,
giving `Q = inf` on the eigenvalue readout; and the `J`-anticommuting Hermitian
operators give `Q in {inf, 1/2, 1/3, 1}` on their eigenvectors. The locked
value `2/3` is delivered *only* by `Gamma_chi`-anticommutation (control case in
the runner: every nonzero eigenvector gives exactly `2/3`).

## What this means for the "up-and-down-the-stack" hope

The same real-structure reading that the strong record axiom invokes for the
*value* side (`r = 1/2`, block-counting) does **not** also discharge the
chirality gate. The complex structure `J` is genuinely present in the real
reading, but it is the imaginary unit of the doublet division algebra -- an
anti-Hermitian, circulant rotation generator -- not a parity. The chirality
gate continues to require a *Hermitian, `C_3`-orbit-splitting* grading on the
generation factor, which is precisely the single confirmed import the broader
charged-lepton arc already isolates. This pressure-test removes one specific
candidate (the doublet `J`) cleanly and explains *why* the failure is
structural, not a basis artifact: it is the Hermitian-vs-anti-Hermitian
distinction, not the site-vs-intrinsic distinction, that decides the matter.

## Scope and non-circularity

- No PDG / measured / empirical lepton mass is consumed. Every check is a
  structural fact about `R[Z_3]`; `Q = 2/3` appears only as a *target* the
  candidate fails to hit, and as the verified output of the *existing*
  `Gamma_chi` control.
- This note does not retire, demote, or promote any audit row. It reports that
  one candidate chirality mechanism (the doublet complex structure `J`) does
  not reach `Q = 2/3`.
- The candidate axiom itself is not adopted here; only the consequence "`J`
  unlocks chirality" is tested, and found false.

## Next paths this opens

- The chirality gate's requirement is now stated sharply against this candidate:
  a **Hermitian** involution that **breaks** `C_3`-equivariance on the
  generation `R^3` (the doublet `J` is Hermitian-failing *and*
  `C_3`-preserving, failing both ways). Any future grading proposal can be
  triaged immediately against these two properties.
- The value-side `r = 1/2` block-counting reading and the chirality gate remain
  *separate* requirements; this note shows the real structure does not collapse
  them into one. A genuine collapse would need a Hermitian object built from the
  real structure that is *not* `+-Gamma_chi` and *not* circulant -- the runner's
  obstructions 2 and 3 are the precise hurdles such an object must clear.

## Cross-references (non-load-bearing)

- [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md`](KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md)
- [`KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md`](KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md)
