# Charged-Lepton Koide Value Reduces to a Single Counting-Measure Bit; the Order-4 J_cs Is Native, Not Missing — Narrow Synthesis

**Date:** 2026-06-05
**Claim type:** meta
**Type:** structural reduction / route-boundary synthesis
**Claim scope:** a Quantum-and-Lattice-native algebraic reduction of the
charged-lepton Koide readout `Q`: given the circulant mass-spectrum variables
and the native order-4 complex structure, the remaining value choice is one
binary measure choice (block-count vs dimension) on `R[Z_3] = R (+) C`, which
the retained no-go
`koide_frobenius_isotype_split_uniqueness` forces neither way. Does **not** claim
to force `Q=2/3`; characterizes the residual.
**Status authority:** independent audit lane; no audit outcome set; no new axiom,
no import, no fitted value (`Q=2/3` is a downstream check, never an input).
**Primary runner:** `scripts/charged_lepton_value_one_counting_bit.py`
(SCORECARD PASS=22 FAIL=0, exact sympy).

## 1. The reduction (what the framework natively supplies)

On the generation triplet `C^3` = grade-1 of `Cl(3,0)` (directions `e_x,e_y,e_z`),
with the C_3 cyclic shift `C` and the Hermitian circulant mass operator
`H = a I + b C + b* C^2`, the Koide ratio is exactly

```
Q = Tr(H^2) / (Tr H)^2 = 1/3 + (2/3) r ,   r = |b|^2 / a^2          (verified, A)
```

(`r=0 -> Q=1/3`; `r=1/2 -> Q=2/3`, charged-lepton target; `r=1 -> Q=1`). Within
this circulant carrier, the framework-side algebra supplies the following
ingredients while leaving one count choice unforced:

- **the spectral masses of the chosen circulant operator** `m_k = lambda_k^2`
  (the real spectrum, fixed by `a, |b|, arg b`);
- **the form** `Q = 1/3 + (2/3) r` (retained `koide_lightcone_primitive_theorem`,
  `koide_circulant_q_two_thirds_algebraic`);
- **the order-4 complex structure** `J_cs = (C - C^2)/sqrt(3)` on the doublet:
  `J_cs` is **real**, antisymmetric, `J_cs^2 = -P_doublet` (a genuine order-4
  complex structure), `J_cs^4 = +P_doublet`, and `[J_cs, H] = 0` (verified, B).

## 2. The order-4 J_cs is native, not missing (correction of a tempting framing)

It is tempting to say `R^3` is odd-dimensional, has no complex structure, and so
the order-4 `J` needed for the complex (`det_C`) reading is *missing* — which would
invite a 4th dimension (emergent time, a quantum-link, etc.) to supply it. **That
framing is wrong.** `det_C` only needs a complex structure on the **doublet**,
which is **2-dimensional (even)** and **already carries** `J_cs` with no extra
structure. The odd direction is the *singlet* (the `0`-eigenvector of `J_cs`),
irrelevant to the doublet. The order-4 object is present and native; it is **not**
the gap.

## 3. Why J_cs does not fix the value: a static J is measure-neutral

`J_cs` exists but cannot, by itself, select the value. `exp(s J_cs)` is an
orthogonal rotation in the doublet plane with **`det = 1`** (it preserves the real
volume) **and** `|det_C| = 1` (it preserves the complex volume): a static complex
structure is an **automorphism of both the real and the complex volume** (verified,
C). To set the value, `J_cs` would have to act as the **measure** — to promote the
*operator* `J` to the *counting field* (`v |-> J v` as a mode-count), i.e. to count
the doublet as **one complex mode** (`det_C`) rather than **two real modes**
(`det_R`). A static `J` does not do that.

## 4. The residual: one counting-measure bit

`R[Z_3] = R (+) C` has exactly two minimal central idempotents (ranks 1 and 2,
verified, D). The value is the choice between the two canonical measures on them:

| measure | weighting | r | Q | role |
|---|---|---|---|---|
| **block-count `(1,1)`** = det_C | equal weight / equal HS energy per block (`3a^2 = 6|b|^2`) | **1/2** | **2/3** | charged-lepton target |
| **dimension `(1,2)`** = det_R | real-dimension / Born / trace | **1** | **1** | over-determined default |

`koide_frobenius_isotype_split_uniqueness` (**retained_no_go**) proves the
Ad-invariant isotype-weight family has a free parameter — it forces **neither**
`(1,1)` nor `(1,2)`. The masses are identical either way; only the **count** (the
`Q` readout / the sign of `sqrt(m)` on the doublet) differs. So:

> **The charged-lepton Koide value is one binary counting-measure bit
> (block-count/`det_C`/`r=1/2`/`Q=2/3` vs dimension/`det_R`/`r=1`/`Q=1`). The
> framework's over-determined default is `Q=1`; the charged-lepton target `Q=2/3` is the
> natively-available-but-unforced block-count reading.**

This single bit is the same object that the chirality gate (anticommutation with
`Gamma_chi`), the Dirac-vs-Majorana / signed-`sqrt(m)` choice, the K-reality
partition, and the fermionic-frame all reduce to — they are one counting bit on
different tensor factors.

## 5. Convergence (why this is the residual, from every angle attacked)

Multiple independent routes were built and each reduced, time-independently, to
this same counting bit (not to a missing structure):

- **variational / measure** — the canonical HS metric and the derived reference
  state land at `r=1` (det_R); `r=1/2` is the block-fold/equal-block point
  (`flavor_r_half_is_a_stationary_point_not_forced`, retained_bounded);
- **reflection positivity** — the channel Gram is diagonal, so positivity is a
  one-sided sign window; it does not see the diagonal balance `r=1/2`;
- **dynamics / einselection** — the native imaginary-time (heat-kernel) arrow
  flows `r -> 1`; recording yields the same det_R default;
- **gauge-invariant footing** — the gauge constraint is the circulant commutant;
  both `det_R` and `det_C` are functions of the *same* circulant, so the
  constraint is orthogonal to the `r`-value;
- **4th dimension (emergent time / quaternionic)** — `J_cs` is already native on
  the even doublet, so the even-dim 4th direction is not needed; a spacetime J
  lands on the spacetime factor and commutes with the generation operators
  (`parity_violation_does_not_reach_generation_triplet`, retained_bounded;
  `koide_z3_equivariant_anticommuting_no_go`, retained_bounded).

## 6. The one open handle (the right shape for a forcing)

A static `J` is measure-neutral; what *could* force the count is a **grading**, not
a complex structure — an object that promotes the operator to a mode-count. The
sharpest named candidate is the **chirality-graded supertrace / equivariant index**
(a counting in the representation ring, which genuinely promotes operator -> count),
**conditional on the gated staggered-Dirac mass structure** and the
operator-algebraic **sector-factorization** on the `M_2(C)`-per-site `(x) R[C_3]`
algebra. This route is the next target; it is decoupled from the 4th-dimension and
recording routes, and it is gated on separate open work.

## No-go discipline gate (N1-N8)

**No-go discipline result: PASS for the narrow scoped reduction only** — this note does NOT close
`Q=2/3`, does NOT rank the two measures, and does NOT introduce a forcing.

**N1 - Alternative route enumeration.** Concrete routes that would force `det_C`
without a grading, each shown to reduce to the same unforced count:

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| static complex structure `J_cs` | use the native `J` to set the count | `J_cs` is measure-neutral (det=1 real, |det_C|=1) — automorphism of both volumes | ATTEMPTED |
| variational extremum | a native functional with `r=1/2` minimum | canonical HS metric / reference state extremize at `r=1` | ATTEMPTED |
| reflection-positivity saturation | RP equality at `r=1/2` | channel Gram diagonal -> one-sided sign window, blind to the balance | ATTEMPTED |
| dynamical attractor | native flow to `r=1/2` | heat-kernel/records arrow flows to `r=1` (det_R) | ATTEMPTED |
| 4th dimension / emergent time | order-4 `J` from a time direction | order-4 `J_cs` already native on the even doublet; time-`J` is spacetime-factor, commutes with generations | ATTEMPTED |
| gauge holonomy | det_C from the Wilson-loop order | holonomy order-3 on the dim-3 vector carrier; gauge constraint orthogonal to `r` | ATTEMPTED |
| Bargmann radial measure | det_C from the holomorphic radial count | radial shortcut equals the C_3-forbidden phase collapse | ATTEMPTED |
| chirality-graded supertrace/index | a grading that promotes operator->count | the one route of the right shape; OPEN, gated on the staggered-Dirac mass structure | OPEN |

**N2 - Wall-independence audit.** The collapsed wall is single: the
`(1,1)`-vs-`(1,2)` isotype-weight freedom (`koide_frobenius_isotype_split_uniqueness`,
retained_no_go). Every route above is an alternate face of it, not an independent
wall. A retained grading (supertrace/index, conditional) would change the verdict.

**N3 - Hidden-wall scan.** Load-bearing inputs are explicit: the C_3 circulant
algebra, the exact `Q = 1/3 + (2/3) r`, the doublet/singlet idempotents, the exact
identities `J_cs^2 = -P_d`, `[J_cs,H]=0`, `det(exp s J_cs)=1`. No rhetorical phrase
("native", "default") is used as a hidden retained premise; "default" means
explicitly the dimension/Born/trace weighting.

**N4 - Residual matching.** The attacked residual is the value-selection bit, not
the form. `koide_lightcone_primitive` / `koide_circulant_q_two_thirds` (retained)
supply the form; `koide_frobenius_isotype_split_uniqueness` (retained_no_go) is the
exact residual. Non-matching context (signed-vs-singular readout notes; the
tracial-reference chain) is **not** load-bearing here (several are unaudited on
main and are excluded).

**N5 - Rhetoric audit.** "Reduces to one bit", "native, not missing",
"measure-neutral", "over-determined default" are scoped to: the C_3 circulant model,
the two canonical measures, and the exact identities verified in the runner. The
note does **not** claim `Q=2/3` is excluded (it is the block-count reading), nor
that `Q=1` is the physical answer (it is the unforced default), nor that no grading
can force `det_C`.

**N6 - Partial-closure path scan.** Open, non-axiom partial-closure paths: the
chirality-graded supertrace/equivariant index, and operator-algebraic
sector-factorization on the per-site `(x) R[C_3]` algebra. Neither is called a new
axiom; both are gated on the staggered-Dirac mass structure.

**N7 - Steelman.** Strongest objection: "the charged-lepton target `Q=2/3` *is* the block-count
reading, so the framework `predicts` it via `J_cs`." Rebuttal: `J_cs`'s existence
is necessary but not sufficient — it is measure-neutral, so its presence does not
promote the block-count over the dimension reading; the promotion is the open
grading. The note concedes the block-count reading is natively *available* (not an
external import) — that is the positive content — while denying it is *forced*.

**N8 - Cross-cycle echo.** The repo's overclaim failure mode is to call the value
"derived" once the form and a candidate structure (here `J_cs`) are in hand. This
note avoids that by separating *form + structure + masses* (native) from *the
count* (one unforced bit), and by pinning the only forcing-shaped route (a grading)
as explicitly open and gated.

## Provenance

Quantum (`per-site qubit = Cl(3,0) spinor`) + Lattice (`Z^3`) + retained form
rows; no new axiom, no import, no fitted value. Retained anchors verified on
`origin/main`: `koide_lightcone_primitive_theorem`,
`koide_circulant_q_two_thirds_algebraic`,
`koide_anticommuting_operator_derivation_theorem` (retained);
`koide_frobenius_isotype_split_uniqueness` (retained_no_go);
`koide_z3_equivariant_anticommuting_no_go`,
`flavor_r_half_is_a_stationary_point_not_forced`,
`parity_violation_does_not_reach_generation_triplet` (retained_bounded).
