# Dirac / Weyl Fermion DOF From Lorentz and Chirality Admission Bridge Note

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py`](../scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py)

## 2026-06-07 source-packet repair

The audit blocker named two residual inputs: Q1 (`Cl(3,1)` signature
extension) and Q2 (on-shell thermal counting). On current `main`, Q1's finite
Clifford-algebra content is now audit-retained by
[`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md).
This repair updates the row accordingly:

- Q1 is retired as an unsupported algebraic admission for this dof bridge.
- Q2 is repaired as a textbook-counting import: the on-shell halving is now a
  source-local finite-rank statement for the Dirac mass-shell operator on
  `C^4`.
- The row still does not claim physical Wick rotation, spacetime dynamics, or
  forced Lorentzian-sign selection.
- The row still does not derive the Dirac equation or the physical thermal
  inventory; it proves the counting once that first-order mass-shell equation
  is the active free-particle equation.
- This is not a ledger retag; independent audit owns any effective-status
  change.

## 2026-06-08 label-semantics safe-narrow

The refreshed audit agrees that the finite algebra checks close, but flags a
remaining physical-label bridge: CPT exactness does not by itself derive that
the thermal inventory has a distinct particle-antiparticle species label, and
the per-site `SU(2)` doublet does not by itself derive the physical
spin/helicity label used in P4.

The 2026-06-08 direct branch-rank repair below removes those label semantics
from the load-bearing count. The conventional words "spin",
"particle-antiparticle", and "helicity-antiparticle" remain interpretation
labels for the parent inventory, but the integer count in this row is now
proved directly from the supplied first-order Dirac operator's branch ranks.

## 2026-06-08 direct branch-rank repair

The load-bearing count is now:

```text
Dirac on-shell branch count = dim_C ker D(E,+p) + dim_C ker D(-E,+p)
                            = 2 + 2
                            = 4.

Weyl fixed-chirality branch count
  = dim_C P_chi ker D(E,+p) + dim_C P_chi ker D(-E,+p)
  = 1 + 1
  = 2.
```

The runner checks the massive Dirac ranks at rest, moving positive-energy, and
negative-energy mass-shell points, and checks the massless positive- and
negative-energy branches after applying the chirality projectors. Thus the
parent P4 integer counts are no longer conditional on identifying the
framework `SU(2)` doublet with physical spin/helicity or CPT exactness with a
distinct physical particle-antiparticle thermal species. Those label bridges
remain non-load-bearing interpretive bridges.

## Claim

Given the retained Cl(3,1) finite Clifford-algebra source packet (Q1 below)
and the source-local on-shell branch-rank certificate (Q2 below), the finite
integer counts used by the Standard Model fermion thermal degree-of-freedom
premise P4 of the parent thermal-inventory proof-walk
`G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`,

```text
Dirac thermal dof per flavour-colour state = 2 (spin) * 2 (particle-antiparticle) = 4,
Weyl thermal dof per flavour-colour state  = 2 (helicity-antiparticle),
```

are reproduced without making those physical label names load-bearing. The
Dirac count is the direct branch-rank identity `2 + 2 = 4`: for the supplied
first-order Dirac mass-shell operator, each massive energy-sign branch has
`dim_C ker D(p) = 2`. The Weyl count is the direct fixed-chirality branch-rank
identity `1 + 1 = 2`: for the massless branches, each chirality projector has
rank one on the on-shell kernel for each energy sign.

R1 (`SU(2)` doublet) and R3 (CPT exactness) are now cross-check/context for the
usual P4 labels, not the load-bearing source of the integer count. R2 supplies
the chirality projectors used in the Weyl branch-rank split. The Cl(3,1)
algebra-cell fact supplying the `n = 4` even-generator count is now sourced by
the retained Q1 authority
`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`.
The on-shell halving is no longer imported as a textbook convention:
Q2 now proves, by explicit Dirac-operator rank, that imposing
`(gamma^mu p_mu - m) psi = 0` on an on-shell momentum leaves a
two-complex-dimensional solution space per massive energy branch and that a
fixed chirality leaves one complex dimension per massless energy branch.

This is a Q1/Q2-counting-repaired bounded bridge. It does **not** add a new
axiom, a new repo-wide theory class, or a retained-status claim. Q1 is retired
only as the finite Clifford-algebra cell `Cl(3,1) ~= M_4(R)` with a
four-real-dimensional faithful module; it does **not** claim the
framework has derived Wick rotation, spacetime dynamics, or physical
selection of the Lorentzian sign. Q2 is retired only as the finite
linear-algebra count for an already-supplied Dirac mass-shell equation;
this bridge does **not** derive that equation, the free-field dynamics,
or the physical thermal inventory itself.
This source note supplies the finite algebraic count and source-local
on-shell branch-rank certificate. Replacement of the parent note's conventional
label wording still requires a separate physical-label bridge, but the integer
counts `4` and `2` no longer depend on that bridge.

## Framework authority and context packet (R1-R4)

The following existing framework authorities and context rows keep the
conventional parent wording visible without making physical label semantics
load-bearing. Their effective statuses are checked by the audit pipeline and
are not asserted by this source note.

- **R1 Per-site `j = 1/2` SU(2) doublet (interpretive cross-check, not
  load-bearing for the branch-rank count).**
  Supplied by `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`
  as an existing audit-ledger authority. On every framework site, the
  per-site Hilbert space carries exactly the `j = 1/2` irreducible
  representation of su(2); the diagonal generator `S_3 = sigma_3 / 2`
  has eigenvalues
  `m in {-1/2, +1/2}`, supplying a two-label algebraic doublet. The direct
  branch-rank count below does not need this label as a premise. This row also
  does not derive that this doublet is the physical thermal spin/helicity
  label.

- **R2 Chirality operator `gamma_5` exists iff `n` (total Clifford
  generator count) is even.** Supplied by
  [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  as an existing audit-ledger authority. An element `gamma_5` of
  `Cl_C(p, q)` satisfying `gamma_5^2 = +I` and
  `{gamma_5, gamma_mu} = 0` for every generator exists iff
  `n = p + q` is even. With `n = 4` supplied by Q1, this theorem gives
  the chirality projectors
  `P_L = (I - gamma_5) / 2` and `P_R = (I + gamma_5) / 2`, supplying
  the fixed-chirality split used in the Weyl branch-rank count.

- **R3 CPT exact preservation (interpretive cross-check, not load-bearing for
  the branch-rank count).**
  Supplied by `CPT_EXACT_NOTE.md` as an existing audit-ledger authority. Exact
  CPT preservation supplies the
  pairing symmetry expected by the conventional particle-antiparticle wording.
  The direct branch-rank count below does not need this label as a premise.
  This row does not derive that distinct thermal species label from CPT alone. The
  mass-equality decoration
  `CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`
  is reader context only; it is not load-bearing for this integer
  count.

- **R4 Fermionic CAR irreducible single-mode carrier dim 2.** Supplied
  by `SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`
  and `SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`
  as existing audit-ledger authorities. The fermionic CAR algebra has a 2-dim
  irreducible single-mode realisation, and the squared creation
  operator vanishes (`(a^†)^2 = 0`), giving single-mode occupation
  `n in {0, 1}`. R4 supplies the per-mode finite Grassmann / Berezin
  algebraic framing. The branch-rank count does not require choosing a
  physical spin or particle-antiparticle label basis.

The per-site `Cl(3, 0)` algebra supporting R1 is supplied by the
Cl(3) backbone
`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md` and
`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`; these
are framework-baseline context pointers and not load-bearing for the
dof arithmetic.

## Retained source plus source-local counting packet (Q1-Q2)

The following packet supplies the Lorentzian-signature spinor-space
dimension and the on-shell branch-rank count. Q1 is now a retained finite
Clifford-algebra authority on the current ledger; Q2 is repaired inside this
packet as a finite rank calculation. Neither is promoted to an axiom.

- **Q1 Cl(3,1) finite Clifford-algebra source (`n = 4` even generator
  count; `Cl(3, 1) ≅ M_4(R)`).** This is now supplied by the retained
  source
  [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md).
  That theorem proves the two one-generator real-Clifford extensions of
  the framework `Cl(3,0)` cell, identifies the `ε = -1` branch as
  `Cl(3,1) ≅ M_4(R)`, and gives the faithful real `R^4` module used
  here. Q1 is therefore retired as an unsupported admission for this
  local algebraic dof bridge. Boundary: the retained theorem does not
  derive Wick rotation, physical spacetime, dynamics, or why the
  framework must select the Lorentzian sign; any downstream use that
  requires those physical claims must still carry that separate
  bounded premise.

- **Q2 On-shell finite-rank counting certificate (factor of `1/2`
  from off-shell spinor space to one energy-branch solution space).**
  Let the retained Q1 `Cl(3,1)` cell be represented by gamma matrices
  satisfying `{gamma^mu, gamma^nu} = 2 eta^{mu nu} I_4` with
  `eta = diag(+,-,-,-)` after the standard real/complex presentation
  change used by the runner. For a momentum satisfying the mass-shell
  relation `p_0^2 - |p|^2 = m^2`, the Dirac operator
  `D(p) = gamma^mu p_mu - m I_4` obeys `D(p)(gamma^mu p_mu + m I_4)=0`
  on shell. In the explicit Q1 gamma representation the runner checks
  that `rank D(p) = 2` and therefore `dim_C ker D(p) = 2` for:

  ```text
  p = (m, 0, 0, 0)        rest branch,
  p = (5, 0, 0, 4), m=3   nonzero-momentum branch,
  p = (-5, 0, 0, 4), m=3  antiparticle/negative-energy branch.
  ```

  Thus the "on-shell halving" is not an imported textbook counting
  convention in this row: it is the finite linear-algebra fact
  `C^4 -> ker D(p)` with nullity `2` per energy branch. The real
  off-shell phrase `8 -> 4` is the same statement after multiplying
  complex dimensions by `2`. Boundary: Q2 does not derive the Dirac
  equation, does not derive the physical free-field dynamics, and does
  not by itself prove that the high-temperature thermal inventory must
  use this free Dirac mass-shell surface.

  For the massless Weyl count the runner also checks both lightlike
  energy-sign branches, for example `p=(1,0,0,1)` and `p=(-1,0,0,1)`.
  The massless Dirac kernel has complex dimension `2` on each branch, while
  a fixed chirality projector has rank `1` on each branch. Hence a single
  chirality supplies the branch-rank count `1 + 1 = 2` without importing the
  physical helicity-antiparticle label.

Q1 names the retained algebraic extension to `n = 4` Clifford
generators; Q2 supplies the source-local on-shell rank count used by
the parent thermal-inventory note.

## Proof-walk

Each row of the table is a step in the parent inventory note's
fermion-side arithmetic. The "Load-bearing input" column names the
smallest framework authority or admitted premise consumed;
the "Lattice-action input?" column shows that no lattice-action
quantity (plaquette, staggered phase, link unitary, `u_0`,
Monte-Carlo measurement, fitted comparator) enters the proof-walk.

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (F1) | Cl(3,1) Lorentzian extension at `n = 4` total generator count | Q1 | no |
| (F2) | Volume-element chirality: `gamma_5` exists iff `n` even; with `n = 4`, `gamma_5` exists | R2 + (F1) | no |
| (F3) | Chirality projectors `P_L = (I - gamma_5)/2`, `P_R = (I + gamma_5)/2` are well-defined orthogonal projectors with `P_L + P_R = I`, `P_L P_R = 0` | R2 | no |
| (F4) | Faithful real irrep of `Cl(3, 1) ≅ M_4(R)` has real dimension 4 | Q1 | no |
| (F5) | Massive positive-energy branch: `rank(gamma.p - m)=2`, so `dim_C ker D(E,+p)=2` | Q2 finite-rank certificate | no |
| (F6) | Massive negative-energy branch: `rank(gamma.p - m)=2`, so `dim_C ker D(-E,+p)=2` | Q2 finite-rank certificate | no |
| (F7) | Dirac on-shell branch-rank count: `2 + 2 = 4` | (F5) + (F6) | no |
| (F8) | Massless positive-energy branch: `dim_C ker D=2`, and fixed chirality has rank `1` on the kernel | Q2 + R2 | no |
| (F9) | Massless negative-energy branch: `dim_C ker D=2`, and fixed chirality has rank `1` on the kernel | Q2 + R2 | no |
| (F10) | Weyl fixed-chirality branch-rank count: `1 + 1 = 2` | (F8) + (F9) | no |
| (F11) | Conventional Dirac wording `2 (spin) * 2 (particle-antiparticle)` is a non-load-bearing interpretation of the branch-rank count | R1 + R3 as context only | no |
| (F12) | Conventional Weyl wording `2 (helicity-antiparticle)` is a non-load-bearing interpretation of the fixed-chirality branch-rank count | R2 + R3 as context only | no |
| (F13) | Active neutrino is single Weyl per generation (no `nu_R` in the relativistic thermal inventory, by P1 of the parent note) | P1 of parent note + (F10) | no |

The proof-walk does not cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, the lattice scale
`u_0`, a Monte Carlo measurement, or a fitted observational value.

## Exact arithmetic check

The Dirac on-shell count is the branch-rank identity

```text
dof_Dirac (on-shell)
  = dim_C ker D(E,+p) + dim_C ker D(-E,+p)
  = 2 + 2
  = 4.
```

Equivalently, for either fixed massive energy branch, the spinor-space
dimension and Q2 finite-rank on-shell halving give

```text
dim_R V_(3,1) * 2 / 2 = 4
```

where `dim_R V_(3,1) = 4` is the real dimension of the faithful real
irreducible module of `Cl(3, 1) ≅ M_4(R)` (Q1), the `* 2` is the
real-vs-complex doubling for a complex Dirac spinor (4 complex
components -> 8 real components), and the `/ 2` is the Q2 finite-rank
halving from the first-order Dirac mass-shell operator. The branch-rank
identity above is the load-bearing thermal integer count; the conventional
factorisation `2 (spin) * 2 (particle-antiparticle) = 4` is a label
interpretation of the same integer, not a premise of this proof.

The Weyl on-shell count for a fixed chirality is

```text
dof_Weyl (on-shell)
  = dim_C P_chi ker D(E,+p) + dim_C P_chi ker D(-E,+p)
  = 1 + 1
  = 2,
```

where `P_chi` is either `P_L` or `P_R`, supplied by R2 (existence of
`gamma_5` at even `n = 4`). The conventional parent wording

```text
2 (helicity-antiparticle)
```

is a label interpretation of this `1 + 1` fixed-chirality branch-rank count,
not a load-bearing input.

The runner repeats the branch sums with `fractions.Fraction` (no
floating-point arithmetic), checks the massive and massless branch ranks
with exact `sympy` matrices, and separately verifies that the conventional
label wording is non-load-bearing context.

## Mapping to the parent note's P4 premise

The parent note's P4 premise reads:

> Each Dirac fermion state contributes `2 (spin) * 2 (particle-antiparticle)
> = 4` thermal degrees of freedom. The active neutrino is a single
> Weyl fermion per generation, contributing `2 (helicity-antiparticle)`
> states.

This bridge supplies the algebraic integer counts used by P4 in two parts. It
can replace the numeric `4` and `2` inputs as branch-rank counts, but it does
not by itself make the parent note's conventional physical label words
load-bearing:

- **The Dirac integer `4`** is supplied by the branch-rank count
  `dim_C ker D(E,+p) + dim_C ker D(-E,+p) = 2 + 2 = 4`.
  After this bridge is independently audited, the numeric content of the
  parent note's P4 premise can be restated as:
  
  > Each Dirac fermion state contributes `4` on-shell branch-rank degrees of
  > freedom: `2` on the positive-energy branch and `2` on the negative-energy
  > branch, with the source-local rank count from Q2 and the four-component
  > spinor space from Q1.
  
  The conventional factorisation `2 (spin) * 2 (particle-antiparticle)` can
  remain as interpretation only unless a separate physical-label bridge is
  supplied. Q1 (finite `Cl(3,1)` algebra cell) is retained-sourced, and Q2's
  textbook on-shell-counting import is replaced by this source-local rank
  certificate. The residual boundary is explicit: the bridge does not derive
  the Dirac equation/free-field mass-shell input, the physical thermal-
  inventory use of that input, the physical spin/helicity label, or the
  distinct particle-antiparticle thermal label.

- **The Weyl integer `2`** is supplied by the fixed-chirality branch-rank count
  `dim_C P_chi ker D(E,+p) + dim_C P_chi ker D(-E,+p) = 1 + 1 = 2`.
  R2 supplies the `gamma_5` projectors. The parent note's
  `2 (helicity-antiparticle)` phrase can remain as interpretation only unless
  the physical helicity-antiparticle label bridge is supplied.

P4's numeric dof counts can therefore be source-supported by this bounded row
after independent audit. P4's conventional label wording remains a separate
physical-label bridge. The operational purpose of this source note is to retire
the textbook on-shell-counting import and isolate label semantics as
non-load-bearing interpretation.

## Dependencies

Load-bearing dependencies for this bridge:

- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the chirality projectors used in the fixed-chirality Weyl
  branch-rank count.
- [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
  is now the retained Q1 source for the Cartan-Bott classification cell
  `Cl(3, 1) ≅ M_4(R)` and its four-real-dimensional faithful module.
- Q2 finite-rank on-shell counting is source-local to this note and runner:
  explicit gamma matrices verify `rank(gamma.p - m)=2` on mass shell and
  chirality projectors split the massless branch.
- `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`
  parent honest-status note naming the Wick-rotation `Z^3 -> Z^4`
  admission (P2). This bridge does not claim to close that physical
  Wick-rotation premise; it only uses the retained finite
  Clifford-algebra Q1 cell.

Non-load-bearing context:

- `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`
  per-site `j = 1/2` SU(2) carrier. Context for the conventional spin/helicity
  wording; not load-bearing for the branch-rank arithmetic.
- `CPT_EXACT_NOTE.md`
  CPT exact preservation. Context for the conventional particle-antiparticle
  wording; not load-bearing for the branch-rank arithmetic.
- `SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`
  and `SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`
  fermionic CAR/Berezin framing. Context only for this branch-rank bridge.
- `CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`
  `Cl(3, 0) tensor_R C ≅ M_2(C) + M_2(C)` chirality-pair
  structure at signature `(3, 0)`. Framework-baseline backbone for
  the per-site `Cl(3, 0)` algebra; not load-bearing for the dof
  arithmetic.
- `CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
  Pauli-irrep uniqueness at `Cl(3, 0)` over `C`. Framework-baseline
  backbone; not load-bearing for the dof arithmetic.
- `MINIMAL_AXIOMS_2026-06-05.md` framework-baseline three-axiom
  packet; context only.

These are imported authorities and context pointers for a bounded branch-rank
bridge. The row remains under independent audit authority until the audit lane
reviews this note, its load-bearing dependencies, the source-local Q2 branch
certificate, and the runner.

## Boundaries

This bridge does not close:

- physical derivation of Wick rotation, spacetime dynamics, or forced
  Lorentzian-sign selection. Q1 retires only the finite algebraic
  `Cl(3,1) ~= M_4(R)` cell used for the spinor module;
- derivation of the Dirac equation/free-field dynamics themselves. Q2
  proves the finite count once the first-order Dirac mass-shell equation
  is the active equation;
- derivation of the Lorentz group `SO(3, 1)` or its spin cover
  `SL(2, C)`;
- derivation of the spin-statistics theorem (R4 supplies the CAR
  cardinality core but does not derive the spin-statistics theorem
  proper);
- the staggered-Dirac realization gate (still open);
- closure of the parent note
  `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  (the parent inventory note still has P1, P2, P3, P5 as admitted
  premises; this bridge only supports the finite numeric branch-rank
  component of P4);
- physical derivation that the framework `SU(2)` doublet is the thermal
  spin/helicity label;
- physical derivation that CPT exactness supplies the distinct thermal
  particle-antiparticle species label;
- any downstream cosmology, leptogenesis, or DM claim;
- promotion of `cl3_to_cl31_spinor_extension_narrow_theorem_note_2026-05-27`
  (the present bridge does not alter the audit status of cited
  authorities);
- any parent theorem/status promotion.

## What this claims and does not claim

- The bridge **claims** that `dof_Dirac = 4` is exact branch-rank
  arithmetic, given retained Q1 plus the Q2 finite-rank on-shell count, and
  that the Weyl count `dof_Weyl = 2` follows from the fixed-chirality
  branch-rank split using R2 (chirality operator at even `n`).
- The bridge **does not claim** that R1 and R3 alone derive the physical
  spin/helicity and particle-antiparticle thermal labels. Those label
  semantics remain non-load-bearing interpretation unless a separate bridge is
  supplied.
- The bridge **does not claim** that the Lorentzian sign is physically
  forced by the framework. The retained Q1 theorem supplies the finite
  algebraic cell; physical sign selection remains outside this bridge.
- The bridge **does not claim** that the Dirac equation/free-field
  mass-shell surface is derived by this row. It only removes the
  textbook import for the on-shell dimension count once that equation
  is supplied.
- The bridge **does not claim** parent-note status promotion. The
  parent note
  `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  retains the remaining premises P1 (declared SM particle inventory),
  P2 (two transverse polarizations per massless vector), P3 (four
  real scalar dof in complex Higgs doublet), and P5 (temperature
  regime). P4's numeric `4` and `2` can only be replaced after this bounded
  bridge is independently audited; P4's conventional label wording still needs
  the separate physical-label bridge, with any separate downstream premise
  that tries to use Q1 as a physical Wick-rotation/sign-selection theorem kept
  outside this row.
- The bridge **does not claim** that the framework's per-site Hilbert
  space becomes `R^4`-valued under Wick rotation. The framework's
  per-site site module is `C^2`-valued per
  `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`; the
  `Cl(3, 1) ≅ M_4(R)` action lives on the abstract real
  Clifford algebra at the extended `n = 4` signature `(3, 1)`, not
  on the per-site site module.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py
```

Expected:

```text
TOTAL: PASS=<n> FAIL=0
VERDICT: bounded counting bridge passes; Dirac dof = 4 and Weyl
dof = 2 follow by exact rational arithmetic from retained Q1 and
source-local Q2 branch-rank counting; conventional physical-label semantics
are checked only as non-load-bearing interpretation.
```
