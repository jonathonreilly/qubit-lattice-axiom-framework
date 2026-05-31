# Koide: the Kähler-Dirac structure is silent on the measure — the value reduces to one substep4 binary

**Date:** 2026-05-30
**Claim type:** bounded structural localization / sharpening of a retained no-go (positive)
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the per-block-vs-per-dimension convention tier.
**Primary runner:**
`scripts/frontier_koide_kahler_dirac_silent_on_measure_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_kahler_dirac_silent_on_measure_2026_05_30.txt`.

## Result (one sentence)

After the orientation bit is stripped, the charged-lepton Koide value is decided by
the **modulus** `r` (per-block `(1,1) -> r=1/2 -> Q=2/3` vs per-dimension
`(1,2) -> r=1 -> Q=1`), and this runner shows the retained **Kähler-Dirac dynamics is
provably silent** on it — its within-generation block vanishes — so the value reduces
to exactly **one discrete, currently-open input**: does the generation matter field
carry a within-generation **real-antisymmetric** (symplectic) bilinear (`-> ` uniquely
`Jcs -> Q=2/3`) or not (`-> ` the central generation-blind `i -> Q=1`)?

## The retained Kähler-Dirac structure is silent (the decisive new fact)

On `Lambda*(R^3)` (the 8-dim form complex / 3-mode Fock space — the retained
staggered `<->` Kähler-Dirac identification, `staggered_dirac_substep2`), the
operator `D_KD = d - delta = sum_mu (a_mu^dag - a_mu)` is real-antisymmetric with
`i D_KD` Hermitian (F1). Because `d` and `delta` shift form-degree by `+-1`, **every**
grade-diagonal `Lambda^k -> Lambda^k` block of `D_KD` is **identically zero** — in
particular the within-generation block `Lambda^1 -> Lambda^1` (the `hw=1` generation
triplet), `max = 0` (F2). So the retained dynamics supplies **no** within-generation
kinetic operator: the complex structure that decides the measure comes from **neither**
retained candidate, and the residual is localized off the retained surface.

## det_C is a red herring; neither native structure is a full-space `J`

For the generation mass operator `M = aI + b(C+C^2)`, `det(M) = (a+2b)(a-b)^2` and
`Pf(M (x) eps)^2 = det(M)^2` — **both** weight the doublet eigenvalue to its
**dimension** power `2`, i.e. `(mu,nu)=(1,2) -> r=1 -> Q=1` (F3). So the per-block
`(1,1)` measure is **not** the output of any spectral determinant / Grassmann /
Pfaffian measure; the "`det_C -> Q=2/3`" reading is false.

The two native complex structures are each ineligible as the deciding full-space `J`
(F4): the ambient form-complex scalar is the **central** `i*I_3` (`= ` Cl(3)
pseudoscalar `omega = g1g2g3`, the `i` making `i D_KD` Hermitian), with eigenvalues
`{+i,+i,+i}` — no `-i` eigenspace, generation-blind `-> Q=1`; and the native `Jcs`
has `Jcs^2 = -P_doublet != -I_3` (`det Jcs = 0`), so it is **not** a full-space complex
structure either — though it is the unique object that counts the doublet **once**
(`-> Q=2/3`).

## The one binary (where the value actually sits)

The only `C_3`-equivariant **real-antisymmetric** operator on `R^3` is `span{Jcs}`
(1-dimensional, F5.1); every `C_3`-equivariant **symmetric** operator commutes with
**both** `Jcs` and central-`i` and is therefore measure-blind (F5.2). So the measure
is decided by exactly one discrete input:

> **Does the generation matter action carry a within-generation real-antisymmetric
> (symplectic / Berry) bilinear?** If yes, it is uniquely `Jcs -> ` the doublet is one
> mode `-> r=1/2 -> Q=2/3`. If no, the generation index is a passive flavor label
> counted by the central `i -> r=1 -> Q=1`.

That binary is the **reality-type / kinetic-order** of the generation matter field —
the **open substep4** gate (`staggered_dirac_realization_gate`, audited_renaming /
open). It is precisely the **dynamical** "external authority" that the *static*
rep-theory no-go (`koide_frobenius_isotype_split_uniqueness`, retained_no_go) says is
required and which it cannot itself supply or pre-refute.

## Boundary

`Q=1` is the retained **default** — every retained object that resolves the
within-generation complex structure (the form-complex central scalar; the determinant
/ Pfaffian) computes it — **not** a coin-flip. `Q=2/3` requires the one specific open
input above. This is **not** a closure of `Q=2/3`: it **sharpens**
`koide_frobenius_isotype_split_uniqueness` from "rep theory ranks neither weight" to
"and the retained Kähler-Dirac dynamics is provably silent, so the deciding authority
is precisely substep4." The framework reproduces `Q=2/3` (`<0.05%`), so that input has
a value to be derived.

**The next path** (a single, well-posed dynamical question, not a missing parameter):
classify whether the framework's matter action contains a within-generation
real-antisymmetric (symplectic) generation bilinear — equivalently, pin the substep4
reality-type (is the generation field `d` **real** form-directions, making `Jcs`
eligible, or `2d` complexified Dirac dofs, forcing central-`i`?), attackable via
`staggered_dirac_substep1_u4_conditional_single_module` (retained_bounded). Two
adversarial cautions verified here: the `arg(b)`-is-dynamical framing is a state-space
**redundancy** (`[Jcs,C]=0`, retained `koide_c3_generator_rephasing_obstruction`), and
the OS-Born-metric route leans on `axiom_first_rp_two_step_transfer_matrix_positivity`
(audited_conditional, not retained).

## Relation to prior notes

Complements `KOIDE_IMPORT_TWO_BIT_DECOMPOSITION_NOTE` (which isolated the orientation
and modulus bits and established the native Kähler triple): this note resolves the
**modulus** bit's status against the retained dynamics — silent — and corrects the
`det_C` counting reading.

## Anchors (live-ledger tiers)

retained / retained_bounded / retained_no_go:
`staggered_dirac_substep2_kahler_dirac_equivalence` (retained_bounded),
`cl3_complexification_split`, `koide_frobenius_isotype_split_uniqueness` (retained_no_go),
`koide_c3_generator_rephasing_obstruction`, `koide_circulant_q_two_thirds_algebraic`,
`staggered_dirac_substep1_u4_conditional_single_module` (retained_bounded).
audited_conditional (named, not load-bearing): `axiom_first_rp_two_step_transfer_matrix_positivity`.
