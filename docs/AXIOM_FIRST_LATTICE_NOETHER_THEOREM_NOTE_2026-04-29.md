# Axiom-First Lattice Noether's Theorem on Cl(3) ⊗ Z^3

**Date:** 2026-04-29 (originally); 2026-05-03 (sublattice repair); 2026-05-10 (gate-recategorization repair); 2026-05-10 (g_bare-removal repair); 2026-05-25 (Step 4b boundary repair); 2026-06-06 (onsite-generator scope, U(1) sign-directness, and KS chirality/parity bridge-support repairs); 2026-06-15 (registered-parent cycle-edge rescope)
**Status:** source-note proposal — author-declared `bounded_theorem`; effective
status set only by the independent audit lane.
**Claim type:** bounded_theorem
**Loop:** `axiom-first-foundations`
**Cycle:** 5 (Route R5)
**Runner:** `scripts/axiom_first_lattice_noether_check.py`
**Log:** `outputs/axiom_first_lattice_noether_check_2026-06-06.txt`
**Runner cache:** `logs/runner-cache/axiom_first_lattice_noether_check.txt`

## Authority disclaimer

This is a source-note proposal. Effective `effective_status` is generated
by the audit pipeline only after the independent audit lane reviews the
claim, dependency chain, and runner. The `claim_type`, scope, named
admissions, and bounded classification are author-proposed; the audit
lane has full authority to retag, narrow, or reject the proposal.

## KS chirality/parity bridge-support repair (2026-06-06)

The latest conditional audit identified that the Noether algebra closes on the
admitted Kawamoto-Smit staggered operator, but the restricted packet did not
provide a source-contained bridge for the KS phase/chirality sign surface.

This source-packet repair adds a narrow bridge for that specific sign surface:

- [`STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md)
  proves that the scalar nearest-neighbor edge-flip grading on the `Z^3`
  coordinate graph is unique up to global sign and equals
  `epsilon(x)=(-1)^(x_1+x_2+x_3)`, then combines it with the A1 central
  pseudoscalar `Omega_global=sigma_1 sigma_2 sigma_3=i I` to give
  `Omega(x)=epsilon(x) Omega_global`.
- [`ETA_HOLONOMY_BASE_FLUX_SCOPE_BOUNDARY_NOTE_2026-06-06.md`](ETA_HOLONOMY_BASE_FLUX_SCOPE_BOUNDARY_NOTE_2026-06-06.md)
  supplies the companion exact spin-diagonal connection identity
  `T(x)^dag sigma_mu T(x+e_mu)=eta_mu(x) I_2` for the displayed KS phases.

This does **not** promote the full staggered-Dirac realization gate and does
not remove every admitted carrier boundary. The broader Grassmann/CAR
realization, full kinetic-operator selection, and species-label interpretation
remain governed by their own rows and by independent audit. The repair only
removes the avoidable source-packet gap where this Noether row used the KS
phase/chirality sign surface without a same-packet derivation/citation.

## Onsite-generator scope repair (2026-06-06)

The 2026-06-06 repair removes a remaining overbroad reading of the
general Noether statement. The local bilateral current (5) is proved
only for **onsite/internal infinitesimal generators**: generators whose
action at site `x` is `(T^A chi)_x = t^A chi_x` (or the finite internal
matrix analogue at the same lattice site). It is not asserted for
arbitrary site-mixing matrices `T^A_{xy}`. Site-mixing symmetries, if
needed later, require a separate envelope-localization theorem.

The repair also makes the U(1) sign convention explicit. With the
phase generator `t = +i`, the coefficient obtained from the local-alpha
variation is the imaginary generator current `J_phase = (i/2) eta B`.
This note defines the displayed real fermion-number current by
`J_real := i J_phase = -(1/2) eta B`. Choosing the opposite generator
`t = -i` flips the displayed sign and the charge orientation, not the
conservation statement.

Runner exhibit `E5` is upgraded from a sampled lattice check plus a
scalar placeholder to an arbitrary-bilinear symbolic identity:
for independent bilinears `B_+ = chibar_x t chi_{x+mu}` and
`B_- = chibar_{x+mu} t chi_x`, it verifies exactly that
`i * (i/2) * (B_+ + B_-) = -1/2 * (B_+ + B_-)`.

## U(1) sign-directness repair (2026-06-06)

The same 2026-06-06 repair adds a separate arbitrary-field check,
`E5b`, so the U(1) specialization is not visible only through a
propagator expectation surface where some symmetric link-bilinear sign
errors can cancel:

- it samples arbitrary complex finite fields `chi`, `chibar` and an
  arbitrary real local envelope `alpha_x`;
- it computes the local U(1) variation of the staggered action directly,
  `delta S = (-i alpha chibar) M chi + chibar M (i alpha chi)`;
- it independently computes the bilateral plus-sign expression in (7c)
  with `T = i I`;
- it verifies that the direct variation and the bilateral plus-sign
  current agree to roundoff, while the historical minus-sign current is
  separated by an order-one residual on the same fields.

This does not change the theorem scope or remove the admitted
staggered-carrier boundary. It only makes the U(1) `(5) -> (4)` sign
closure independently visible to the runner.

## Step 4b boundary repair (2026-05-25)

The 2026-05-25 audit pass identified that the prior Step 4b still
overstated the translation branch. In particular, runner exhibit `E6`
checked the finite-block propagator expectation of the canonical
staggered momentum density (3), but did **not** supply an audit-clean
symbolic derivation of (3) from a site-dependent two-shift Ward identity
for arbitrary on-shell fields.

This repair does not add any framework axiom and does not retag the
audit ledger. It makes the source note honest for re-audit:

- the load-bearing `(2Z)^3` translation statement is narrowed from
  "the canonical density (3) is derived by Step 4b" to the exact
  two-step Ward identity generated by the central two-shift operator
  `D^{(2ρ)} = (S^{(+2ρ)} - S^{(-2ρ)})/2`;
- the canonical density (3) is kept only as a support exhibit on
  the admitted free staggered carrier, checked by `E6`, and is no longer
  claimed as the arbitrary-field Ward current derived from the
  two-shift symmetry;
- the runner adds `E7`, a nondegenerate `L=6` field-level check of the
  localized two-step Ward identity for arbitrary local envelopes, plus
  the on-shell vanishing check for sampled massless nullspace fields;
- the current framework memo is
  `MINIMAL_AXIOMS_2026-05-20.md`, which supersedes
  `MINIMAL_AXIOMS_2026-05-03.md` without adding axioms. The Noether
  note's live load-bearing framework dependency is therefore the
  2026-05-20 two-axiom memo; the 2026-05-03 memo is historical context
  only.

## Gate-recategorization repair (2026-05-10)

The 2026-05-05 audit verdict identified two gaps on the post-2026-05-03
note:

1. **Open-gate dependency.** The note's hypothesis section listed
   the staggered-Dirac/Grassmann action as an `A_min` axiom (former
   `A3`). Under the current public framework memo
   `MINIMAL_AXIOMS_2026-05-03.md` the
   staggered-Dirac realization is **not** a current framework axiom; it
   is an explicit `open_gate` derivation target listed there. Lanes
   (including `lattice_noether`) that depend on this gate must be
   reviewed as `bounded_theorem` surfaces with the gate named in
   `admitted_context_inputs` until the gate closes.

2. **Missing `(5) → (3)` verification.** The runner E5 checked the
   bilateral-current closure `(5) → (4)` for U(1) phase, but did not
   verify the analogous `(5) → (3)` specialization to the
   `(2Z)^3` sublattice momentum-density form. The note's textual
   reduction `(5) → (3)` was not independently validated.

This 2026-05-10 repair addresses both gaps:

- **(R1) Authority rebase.** The hypothesis set is rebased on
  `MINIMAL_AXIOMS_2026-05-03.md`. Only
  `A1` (Cl(3) per-site algebra) and `A2` (`Z^3` substrate, restricted
  to its `(2Z)^3` sublattice) are framework axioms here. The
  staggered-Dirac/Grassmann action `M_KS` is admitted as a named
  open-gate input under `admitted_context_inputs`; the canonical
  normalization surface is admitted as a separate named open-gate
  input. The proof is then a bounded Noether identity on the admitted
  staggered/Grassmann carrier. This matches the recategorization in
  `MINIMAL_AXIOMS_2026-05-03.md` line 173 (`lattice_noether` listed
  among lanes depending on the staggered-Dirac realization gate).
- **(R2) Direct `(5) → (3)` verification.** The runner now includes
  `E6`, an explicit numerical check that the canonical staggered
  sublattice-momentum density `(3)` is on-shell divergence-free
  (`∂^L_μ P^μ_x = 0` to machine precision) on a free pure-staggered
  block. `E6` provides the runner-level verification of the
  specialization claim; the textual reduction `(5) → (3)` is now
  recorded with an explicit caveat that it is a discrete Ward-identity
  rearrangement (not a literal infinitesimal-generator substitution),
  and the runner numerically confirms the resulting current.

## Sublattice repair (2026-05-03 — recapped)

The 2026-05-03 review follow-up identified that the staggered
Kogut–Susskind action `M_KS` is **not** invariant under one-site
shifts `T_μ̂` because the staggered phase factor `η_μ(x)` flips sign
under such shifts; only the index-2 sublattice `(2Z)^3` of two-step
shifts is an exact symmetry of `M_KS` (and the runner's E2 exhibit
verifies precisely two-step shifts). One-site shifts generate a
**larger** symmetry group together with compensating staggered/taste
rotations, but they are not pure translations.

The 2026-05-03 repair restated (N1) on the `(2Z)^3` sublattice that
the runner actually verifies. The conserved current (3) is the
`(2Z)^3` momentum density. The full taste-shift structure (one-site
shift composed with a staggered sign rotation) is acknowledged as a
separate, larger symmetry whose Noether current is not in scope
here. The U(1) phase result (N2) is unaffected by the repair.

## Scope

This note derives, on the current public framework memo
`MINIMAL_AXIOMS_2026-05-20.md` plus the
explicitly admitted staggered-Dirac realization gate, a lattice analogue
of Noether's theorem for the two generator classes proved here:
onsite/internal one-parameter Lie symmetries of the admitted canonical
action, and the separate discrete `(2Z)^3` two-step translation Ward
identity. For an onsite/internal Lie symmetry, there is an explicit
*conserved lattice current* `J^μ_x` with discrete divergence

```text
    ∂^L_μ J^μ_x   :=   Σ_μ  ( J^μ_x  -  J^μ_{x - μ̂} )   =   0  on shell.   (1)
```

The theorem is established for the two physically-load-bearing
symmetries of the admitted canonical action:

- **(N1) `(2Z)^3` sublattice translation symmetry → exact two-step
  Ward identity.** (Pure `Z^3` one-site shifts
  are not symmetries of `M_KS`; see the staggered-shift caveat
  below.) The translation case is **discrete**. The exact
  arbitrary-envelope statement is the localized Ward identity for the
  central two-step generator `D^{(2ρ)}` in Step 4b. The older claim that
  this identity derives the canonical density (3) for arbitrary
  on-shell fields is retracted; (3) remains only a support exhibit on
  the admitted free carrier.
- **(N2) Global U(1) phase symmetry of the matter sector →
  conserved fermion-number current.** This case IS a clean
  infinitesimal Lie-generator substitution into (5).

This is a `bounded_theorem`: it closes the Noether identity given the
staggered-Dirac/Grassmann action as an admitted carrier. When the
staggered-Dirac realization derivation target (open gate per
`MINIMAL_AXIOMS_2026-05-20.md`) and the residual `KS-phase-form`
structural admission close, the row becomes eligible for retagging as
`positive_theorem` by the independent audit lane.

After this note, any package lane that quotes "the canonical action
has a conserved current of type X" can cite the U(1) current (4) and
the onsite/internal local-infinitesimal current (5). Any downstream use
of the translation branch must preserve the narrower Step 4b statement:
exact two-step Ward identity on the admitted staggered carrier, with
the canonical density (3) support-only unless a later audit-clean proof
derives it from the two-shift Ward identity for arbitrary on-shell
fields. Site-mixing infinitesimal symmetries are not licensed by this
row.

## Hypothesis set used

The proof uses the two framework axioms from the current
`MINIMAL_AXIOMS_2026-05-20.md` memo, plus
the **named admitted carrier inputs** recorded below:

**Framework axioms (current):**

- **Axiom 1 — one qubit / local `Cl(3,0) ≅ M_2(ℂ)` algebra per
  site.** Used only via the existence of the primitive local qubit
  operator algebra on each site, equivalently the physical `Cl(3,0)`
  local algebra.
- **Axiom 2 — substrate `Z^3`.** Used via the discrete translation
  action `T_a : x ↦ x + a`, restricted to the `(2Z)^3` index-2
  sublattice that is an exact symmetry of `M_KS`. One-site shifts
  `T_μ̂` flip the staggered sign factor `η_μ(x)` and require
  compensation by a staggered/taste rotation to give a symmetry; the
  Noether theorem in this note applies to the `(2Z)^3` sublattice
  generators only.

**Admitted context input (open gate per current axiom memo):**

- **`staggered_dirac_realization_gate`.** The Grassmann partition
  with staggered Dirac action

  ```text
      S_F[χ̄, χ]  =  Σ_{x,y}  χ̄_x  M_xy  χ_y                            (2)
  ```

  with `M = m + M_KS`, `M_KS` the staggered Kogut–Susskind hop, is
  admitted as a named carrier. Recategorized from the prior `A3`
  axiom by the restored two-axiom framework memo, now current as
  `MINIMAL_AXIOMS_2026-05-20.md`,
  to an open derivation target whose canonical parent note is
  pending packaging. The action is invariant under both `T_{2a}`
  (two-site shift acting on lattice indices) and global `U(1)` phase
  (acting as `χ → e^{iα} χ`, `χ̄ → e^{-iα} χ̄`).

  The specific scalar chirality/parity sign and spin-diagonal KS phase
  surface used by `M_KS` is no longer left as an uncited free premise in this
  packet: the 2026-06-06 chirality/parity bridge and eta-holonomy base-flux
  note cited above supply a source-side exact-support derivation of
  `epsilon(x)=(-1)^(x_1+x_2+x_3)` and
  `eta_1=1`, `eta_2=(-1)^x_1`, `eta_3=(-1)^(x_1+x_2)`.
  Independent audit still decides whether those bridge notes are sufficient
  authority for this row. The full staggered-Dirac realization gate remains
  outside this Noether note's author-side status authority.

**Note on `g_bare` (not a load-bearing admission of this note).** The
`g_bare = 1` canonical SU(3) normalization recategorized from the prior
`A4` axiom (parent: `G_BARE_DERIVATION_NOTE.md`) is not a
load-bearing input to (N1)–(N3). The Noether identities are quantitatively
`g_bare`-independent: the gauge action `S_G` enters only through the
gauge-invariance hypothesis carried by the admitted canonical-action surface,
not through the `g_bare` numerical normalization gate.
Per the 2026-05-10 audit verdict's repair-target option "separately
close or remove the structural `g_bare` dependency if it is not
load-bearing", the `g_bare` gate is therefore **removed** from this
note's named-admission list (2026-05-10 g_bare-removal repair below).

When the staggered_dirac_realization_gate closes on the current
physical `Cl(3)` local algebra plus `Z^3` spatial substrate framework
surface, the row becomes eligible for retagging by the independent
audit lane.

## Statement

Let `S = S_F + S_G` be the canonical action on `A_min`, and let
`G` be a one-parameter symmetry group that maps the action into
itself: `S[g · ϕ] = S[ϕ]` for all `g ∈ G`. Then on `A_min`:

**(N1) `(2Z)^3` sublattice two-step Ward identity.** For the
discrete sublattice translation symmetry `T_a ∈ (2Z)^3` (two-site
shifts in any axis direction, generated by `T_{2ρ̂}` for
`ρ ∈ {1,2,3}`), the exact field-level statement is the localized Ward
identity for the central two-step generator

```text
    D^{(2ρ)}  :=  ( S^{(+2ρ̂)} - S^{(-2ρ̂)} ) / 2.
```

Since `[M_KS, D^{(2ρ)}] = 0`, the site-envelope variation

```text
    δ_ω χ_x  =  ω_x (D^{(2ρ)}χ)_x,
    δ_ω χ̄_x = -ω_x (χ̄ D^{(2ρ)})_x
```

obeys

```text
    δ_ω S_F
      =  Σ_x ω_x [ -(χ̄ D^{(2ρ)})_x (Mχ)_x
                   + (χ̄ M)_x (D^{(2ρ)}χ)_x ]                 (3a)
      =  0 on shell
```

for arbitrary local envelopes `ω_x`. This is the load-bearing
translation statement on the admitted staggered carrier.

The canonical staggered sublattice-momentum density previously written
as (3),

```text
    P^μ_x  =  - (i/2) η_μ(x)  ( χ̄_x  ∂^L_μ χ_x  -  ∂^L_μ χ̄_x · χ_x ),   (3)
```

with `∂^L_μ` the symmetric lattice difference, is no longer claimed as
the arbitrary-field Ward current derived from the two-step symmetry.
Runner exhibit `E6` keeps it as a free-carrier support check only.

**(N2) Fermion-number current.** For the global `U(1)` phase
symmetry `χ → e^{iα} χ`, the conserved current is

```text
    J^μ_x  =  - (1/2) η_μ(x)  ( χ̄_x  χ_{x + μ̂}  +  χ̄_{x + μ̂}  χ_x ),    (4)
```

with lattice divergence `∂^L_μ J^μ_x = 0` on shell. Integration over
a Cauchy surface (lattice time slice) gives the conserved fermion
number `Q = Σ_x χ̄_x χ_x`.

**(N3) Onsite/internal lattice Noether identity.** For any
onsite/internal infinitesimal symmetry
`δ_α χ_x = α^A t^A χ_x` (and conjugate variation
`δ_α χ̄_x = -α^A χ̄_x t^A`) of the canonical action with
nearest-neighbour staggered hop `M_{x, x±μ̂} = ±(1/2) η_μ(x)`, the
on-shell conserved current splits over the two staggered-hop
directions and reads

```text
    J^{μ,A}_x  =  (1/2) η_μ(x) [ χ̄_x  T̂^A  χ_{x+μ̂}  +  χ̄_{x+μ̂}  T̂^A  χ_x ]
                                                                    (5)
```

where `T̂^A` denotes the same onsite/internal matrix `t^A` acting on
the field component at the displayed site. The two-term structure
`χ̄_x χ_{x+μ̂} + χ̄_{x+μ̂} χ_x` arises from the **bilateral
staggered hop** (forward `M_{x,x+μ̂}` and backward
`M_{x,x-μ̂} = -M_{x,x+μ̂}` reindexed with `x' = x - μ̂`). The proof
of the bilateral form is given explicitly in Step 2 below. Arbitrary
site-mixing generators `T^A_{xy}` are outside this formula's scope.

The proof of (N2) is the specialisation of (N3) to the U(1) phase
generator (clean onsite/internal infinitesimal-Lie substitution into
(5); runners E5 and E5b verify). The proof of (N1) follows the exact localized two-step Ward
route in Step 4b because two-site translation is a *discrete* symmetry
of `M_KS`, not an infinitesimal Lie generator. Runner E7 verifies the
field-level identity (3a) on a nondegenerate `L=6` block; runner E6 is
kept only as support for the non-load-bearing free-carrier density (3).

**Review-loop repair clarification (2026-05-03 second pass, then
2026-05-10 gate-recategorization repair):** the original
(5) form `... (χ̄_x χ_{x+μ̂} - χ̄_{x+μ̂} χ_x)/2` (with a minus sign and
only one bilinear term) cannot specialise to (4)'s plus-sign bilateral
form. The corrected (5) above factors the bilateral contribution
explicitly and now closes algebraically when specialised to U(1) phase
(giving (4); E5). The (2Z)^3 sublattice translation case requires a
*discrete* Ward identity (not a literal substitution into (5)). The
2026-05-10 repair retracted the prior literal-substitution claim
`(5) → (3)`. The 2026-05-25 repair narrows the translation branch
further: the load-bearing translation statement is the exact two-step Ward
identity (3a), while the canonical density (3) is support-only until a
separate audit-clean proof derives it from the two-shift Ward identity for
arbitrary on-shell fields.

**Site-mixing boundary.** Formula (5) must not be read as a theorem for
an arbitrary lattice-index matrix `T^A_{xy}`. The local-alpha promotion
used below assigns one envelope value to each lattice site; for
site-mixing `T^A_{xy}` a single factor `(alpha_y - alpha_x)` no longer
captures all bilinear legs without a separate locality/envelope theorem.
This note supplies no such theorem.

## Proof

The proof is the standard variational Noether argument adapted to
the finite Grassmann lattice action.

### Step 1 — variation of the action under an onsite/internal infinitesimal symmetry

Write `δχ_x = α^A t^A χ_x` with `α^A` infinitesimal and `t^A`
acting only on the finite internal field component at the same lattice
site. The conjugate variation is `δχ̄_x = -α^A χ̄_x t^A`. The
variation of the action `S_F = χ̄ M χ` is

```text
    δS_F  =  α^A Σ_{x,y} χ̄_x ( M_xy t^A - t^A M_xy ) χ_y.
```

For `t^A` to be an onsite/internal *symmetry*, the variation must
vanish for arbitrary χ̄, χ:

```text
    [ M_xy , t^A ]   =   M_xy t^A - t^A M_xy   =   0
    for every nonzero hop/local block M_xy.                                (6)
```

This is the symmetry condition for this row's local-current theorem.
The scalar staggered hop and the U(1) generator `t = i` satisfy it
immediately. A site-mixing generator is not covered by (6).

### Step 2 — promote `α` to a slowly-varying lattice field

Now allow `α^A` to depend on the lattice site: `α^A → α^A_x`. The
variation of the action under `δχ_y = α^A_y t^A χ_y` and
`δχ̄_x = -α^A_x χ̄_x t^A` reads

```text
    δS_F[α(x)]
      = Σ_{x,y} ( α^A_y - α^A_x )  χ̄_x  M_{xy}  t^A  χ_y             (7a)
```

(the constant-α piece `α (M t^A - t^A M)` vanishes by the symmetry
condition (6)).

For the canonical staggered hop `M_{x, x+μ̂} = +(1/2) η_μ(x)` and
`M_{x, x-μ̂} = -(1/2) η_μ(x)`, only nearest-neighbour pairs contribute,
so the sum (7a) splits into a forward-hop piece and a backward-hop
piece:

```text
  forward (y = x+μ̂):
    Σ_{x,μ}  (1/2) η_μ(x) χ̄_x T̂^A χ_{x+μ̂}  ·  ( α^A_{x+μ̂} - α^A_x )
  backward (y = x-μ̂):
    Σ_{x,μ} -(1/2) η_μ(x) χ̄_x T̂^A χ_{x-μ̂}  ·  ( α^A_{x-μ̂} - α^A_x ).
                                                                     (7b)
```

Reindex the backward piece with `x' = x - μ̂` (so `x = x' + μ̂` and
`η_μ(x) = η_μ(x' + μ̂) = η_μ(x')` because `η_μ` depends on the
coordinates `x_1, …, x_{μ-1}` not on `x_μ`):

```text
  backward (after reindex):
    Σ_{x',μ}  (1/2) η_μ(x') χ̄_{x'+μ̂} T̂^A χ_{x'}  ·  ( α^A_{x'+μ̂} - α^A_{x'} ).
```

Combining the forward and (reindexed) backward pieces:

```text
    δS_F[α(x)]
      = Σ_{x,μ}  (1/2) η_μ(x) [ χ̄_x T̂^A χ_{x+μ̂} + χ̄_{x+μ̂} T̂^A χ_x ]
                              ·  ( α^A_{x+μ̂} - α^A_x ).               (7c)
```

Identifying the coefficient of the discrete forward derivative
`(∂^L_μ α^A)_x = α^A_{x+μ̂} - α^A_x`, the conserved current
`J^{μ,A}_x` is the **bilateral form (5)** above. This is the explicit
algebraic derivation requested by the review follow-up, now restricted
to the onsite/internal generator class for which the local-envelope
calculation is valid.

### Step 3 — on-shell conservation

When the equations of motion `(M χ)_x = 0` and `(χ̄ M)_x = 0` are
satisfied (i.e. classical solutions of the Grassmann action), the
"bulk" piece of `δS_F[α(x)]` vanishes for the onsite/internal
variation, including constant `α^A`. By global symmetry (`α^A`
constant), the action itself is invariant: `δS_F[constant α] = 0`.

Conversely, for non-constant `α^A_x`, the bulk piece still vanishes
on shell, so

```text
    Σ_x  α^A_x · ∂^L_μ J^{μ,A}_x   =   0                              (9)
```

for any `α^A_x`. By choosing `α^A_x = δ_{x, x_0}` (delta-function
test field), we obtain

```text
    ∂^L_μ J^{μ,A}_{x_0}   =   0   on shell.                          (10)
```

This is the onsite/internal lattice Noether identity.

### Step 4 — specialisation to `(2Z)^3` sublattice translation and U(1) phase

#### Step 4a — U(1) phase → fermion-number current (4)

For `U(1)` phase, `T̂^A χ_y = i χ_y` (the generator is `i` acting as
a multiple of identity). Substituting into the bilateral (5):

```text
    J^μ_x  =  (1/2) η_μ(x) [ χ̄_x · i · χ_{x+μ̂}  +  χ̄_{x+μ̂} · i · χ_x ]
           =  (i/2) η_μ(x) [ χ̄_x χ_{x+μ̂}  +  χ̄_{x+μ̂} χ_x ].          (4a)
```

The `i` factor is the imaginary phase generator. The fermion-number
current (4) is the corresponding **real** charge current, related by
the convention `J^μ_x [real] := i · J^μ_x [imaginary phase generator]`,
giving

```text
    J^μ_x  =  -(1/2) η_μ(x) [ χ̄_x χ_{x+μ̂}  +  χ̄_{x+μ̂} χ_x ]
                                                                     (4)
```

exactly as stated in (N2). The substitution closes algebraically.
With the opposite phase-generator convention `t = -i`, the displayed
current changes sign; this is only the orientation convention for the
conserved charge. The conservation law and the charge-sector
decomposition are unchanged.

#### Step 4b — `(2Z)^3` sublattice translation → exact two-step Ward identity

**Discrete-vs-infinitesimal caveat (2026-05-25 boundary repair).**
Two-site translation is a **discrete** symmetry of `M_KS`, not a
one-site infinitesimal Lie generator on the lattice. The bilateral form
(5) is the conserved current associated with a local infinitesimal
generator `T^A`; it must not be used as a literal substitution rule for
the finite two-site shift. The source-note claim that this step derives
the canonical density (3) is therefore narrowed here.

**Symmetry condition.** For `(2Z)^3` sublattice translation in direction
`ρ`, let `S^{(2ρ̂)}` be the two-site shift operator on field indices,
`(S^{(2ρ̂)} χ)_y := χ_{y + 2ρ̂}`. The symmetry condition is
`M_KS S^{(2ρ̂)} = S^{(2ρ̂)} M_KS`. Direct check:

```text
    (M_KS)_{x+2ρ̂, y+2ρ̂}
      = (1/2) η_ν(x + 2ρ̂) [ δ_{y+2ρ̂, x+2ρ̂+ν̂} - δ_{y+2ρ̂, x+2ρ̂-ν̂} ]
      = (1/2) η_ν(x) [ δ_{y, x+ν̂} - δ_{y, x-ν̂} ]
      = (M_KS)_{xy}
```

(the key step uses `η_ν(x + 2ρ̂) = η_ν(x)` for every direction `ν`
because each component of `2ρ̂` is even, so the parity sum that
defines `η_ν` is unchanged). The runner's E2 exhibit verifies this
identity to machine precision for all three axis directions.

**Exact localized Ward identity.** The finite shift itself is discrete,
but the central two-step difference operator

```text
    D^{(2ρ)} := (S^{(+2ρ̂)} - S^{(-2ρ̂)})/2
```

is a skew-adjoint linear generator on the finite field space and
commutes with `M_KS` because both shifts commute with `M_KS`.
For a local envelope `ω_x`, set

```text
    δ_ω χ_x  :=  ω_x (D^{(2ρ)}χ)_x,
    δ_ω χ̄_x := -ω_x (χ̄ D^{(2ρ)})_x.
```

Then the finite-dimensional Grassmann bilinear action obeys the exact
identity

```text
    δ_ω S_F
      = -χ̄ D^{(2ρ)} Ω Mχ + χ̄ M Ω D^{(2ρ)}χ
      =  Σ_x ω_x [ -(χ̄ D^{(2ρ)})_x (Mχ)_x
                   + (χ̄ M)_x (D^{(2ρ)}χ)_x ],               (3a)
```

where `Ω = diag(ω_x)`. If the left and right equations of motion
`χ̄ M = 0` and `Mχ = 0` hold, (3a) vanishes for arbitrary envelopes
`ω_x`. This is the exact arbitrary-field two-step Ward identity
supported by Step 4b and runner exhibit `E7`.

**Boundary on the old density (3).** The canonical staggered density

```text
    P^μ_x  =  -(i/2) η_μ(x) [ χ̄_x ∂^L_μ χ_x
                              - ∂^L_μ χ̄_x · χ_x ]             (3)
```

is no longer asserted as the arbitrary-field current derived from the
two-shift Ward identity. `E6` verifies a free-carrier expectation-level
support property of (3); it is not a symbolic Step 4b proof. Any future
use of (3) as a load-bearing sublattice momentum current needs a
separate audit-clean proof deriving (3) from the two-step Ward identity or
an explicit source theorem for the KS-phase momentum-density form.

#### Step 4c — combined: closure of (5) → (4) and two-step Ward identity

The bilateral (5) form, derived in Step 2 from the local-α expansion
of the canonical action for onsite/internal generators, specialises to
(4) under U(1) phase substitution (a clean Lie-generator substitution;
runner E5 confirms algebraically, including the arbitrary-bilinear sign
identity for the real-current convention; runner E5b verifies by direct
arbitrary-field action variation that the plus-sign bilateral form is
the one selected by the local-envelope calculation). The `(2Z)^3`
sublattice translation case is handled by the exact localized two-step
Ward identity (3a), not by identifying (3) with a literal specialization
of (5). The U(1) branch remains a closed local-current statement on the
admitted carrier; the translation branch is an exact Ward identity with
(3) explicitly scoped as support-only. ∎

### Step 5 — why one-site shifts are not pure translations

For one-site shifts `T_μ̂` (which are NOT in `(2Z)^3`), `η_ν(x +
μ̂)` differs from `η_ν(x)` by a sign for those `ν` where the
parity-sum definition of `η` includes the index `μ`. Concretely
`η_1(x) = +1`, `η_2(x) = (-1)^{x_1}`, `η_3(x) = (-1)^{x_1+x_2}`,
and a shift `x_1 → x_1 + 1` flips both `η_2` and `η_3`. The
substituted operator `S^{(μ̂)} M_KS S^{(-μ̂)}` therefore differs
from `M_KS` by a global sign on the shifted directions; the symmetry
condition (6) fails as stated. The composite operator `S^{(μ̂)}` ⋅
(staggered sign rotation) IS a symmetry — that is the staggered
**taste shift symmetry**, which generates a larger group than `(2Z)^3`
translation. Its conserved current is the staggered taste current,
which is **not** the (2Z)^3 momentum density of (3) and is out of
scope for this note.

## Hypothesis-set summary (after Step 4b boundary repair)

The proof uses the two current framework axioms from
`MINIMAL_AXIOMS_2026-05-20.md`: Axiom 1 (one qubit per lattice site,
equivalently the local `Cl(3,0) ≅ M_2(ℂ)` operator algebra) and
Axiom 2 (`Z^3` substrate, used here through its `(2Z)^3` sublattice
translation action), plus
the one named admitted input `staggered_dirac_realization_gate`. The
`g_bare` normalization gate, formerly listed alongside the carrier
gate, is **removed** from the load-bearing input list per the
2026-05-10 audit verdict's explicit option to "remove the structural
`g_bare` dependency if it is not load-bearing": the Noether
identities (N1)–(N3) are quantitatively `g_bare`-independent (see
§"Hypothesis set used" near the top of this note for the precise
non-load-bearing role of `S_G`'s normalization). No imports from the
forbidden list.

The "external import" is the variational Noether technique itself,
which is an elementary finite-Grassmann manipulation, not a primitive
imported as a black box.

## Corollaries (downstream tools)

C1. *Conserved fermion number on the canonical surface.* The
`U(1)` charge `Q = Σ_x χ̄_x χ_x` is a conserved quantum number,
which underlies any "baryon number" / "lepton number" lane on
A_min.

C2. *Discrete sublattice-translation quantum number.* On a finite
block `Λ` with periodic boundary that respects the `(2Z)^3`
sublattice (i.e. `L_μ` even in every direction), the sublattice
translation symmetry gives discrete `(2Z)^3` momenta `k_μ ∈ {0, 2π/L,
…, π}` as good quantum numbers — the basis on which the package's
spectral / band-structure language depends. The first Brillouin
zone is correspondingly halved in each direction relative to the
naive `Z^3` zone. This corollary uses the exact two-step shift
symmetry, not the support-only density (3).

C3. *Compatibility with reflection positivity (R2).* The conserved
charge `Q` is `Θ_RP`-invariant (charge is even under reflection
positivity), so the physical Hilbert space `H_phys` decomposes into
fixed-`Q` superselection sectors. This is the structural support
for the package's separate fermion-number / gauge-charge sectors.

C4. *Anomaly slot.* Lattice Noether by itself does not say whether
a *quantum* current remains conserved (anomalies). The
gauge-invariance + flavour-anomaly closure of the package — captured
in the anomaly-forced 3+1 row — is the next layer above the
classical Noether identity here. This note does not claim to
discharge anomaly cancellation.

## Honest status (post-2026-06-06 onsite-generator scope repair)

**Author-proposed bounded theorem on the admitted staggered/Grassmann
carrier.** (N2) and the onsite/internal local-infinitesimal part of
(N3) are proved by the standard variational argument adapted to the
finite Grassmann staggered action. The row does not prove a
site-mixing local-current theorem. (N1) is narrowed to the exact
localized Ward identity (3a) for the `(2Z)^3` central two-step
generator. One named open gate is admitted explicitly per
`MINIMAL_AXIOMS_2026-05-20.md`: the staggered-Dirac realization gate
(carrier of the action `M_KS`). The `g_bare = 1`
canonical-normalization gate, formerly admitted alongside, is
**removed** from this note's load-bearing input list per the 2026-05-10
audit verdict (Noether identities (N1)–(N3) are quantitatively
`g_bare`-independent).

**Sub-claim status:**

- **(N2) U(1) fermion-number current.** The bilateral form (5)
  specialises cleanly to (4) by onsite/internal infinitesimal
  Lie-generator substitution. Runner E5 verifies `(5) → (4)` to
  machine precision and includes an arbitrary-bilinear symbolic sign
  check for the real-current convention. **Closed form on the admitted
  staggered carrier.**
- **(N1) `(2Z)^3` sublattice two-step Ward identity.** Two-site
  translation is a *discrete* symmetry. Runner E2 verifies the symmetry
  condition for `M_KS` under two-site shifts. Runner E7 verifies the
  localized identity (3a) for arbitrary local envelopes on a
  nondegenerate `L=6` block and checks on-shell vanishing for sampled
  massless nullspace fields. The canonical density (3) is support-only;
  runner E6 no longer carries theorem status for arbitrary-field
  translation-current closure.
- **(N3) Onsite/internal lattice Noether identity.** The bilateral (5)
  is the conserved current for a local *onsite/internal infinitesimal
  Lie* generator. It is not a theorem for arbitrary site-mixing
  `T^A_{xy}`. For the discrete two-step generator, Step 4b supplies the
  separate localized Ward identity (3a); it does not identify (3) as a
  literal specialization of (5). Runner E5 + E7 jointly confirm the two
  regimes on the admitted staggered carrier.

**When admitted gates close.** When
`MINIMAL_AXIOMS_2026-05-20.md`'s
staggered-Dirac realization derivation target closes (canonical parent
note pending packaging) and the residual `KS-phase-form` structural
admission is supplied by retained-grade authority, this row becomes
eligible for retagging from `bounded_theorem` to `positive_theorem` by
the independent audit lane. The structural Noether-identity content of
the proof is unchanged by that closure; only the input-tier of the
carrier moves from "admitted open gate" to "derived from Axiom 1 +
Axiom 2 + infrastructure".

**Not in scope.**

- Anomaly closure for the conserved currents at the quantum level.
  That requires the index theorem / anomaly-forced 3+1 row of the
  package's existing retained closure, not the classical Noether
  identity established here.
- Lattice analogue of full energy-momentum tensor conservation.
  We give the exact two-step Ward identity and a support-only
  free-carrier density exhibit; the full `T^{μν}` and any theorem-grade
  identification of (3) as the sublattice momentum current require more
  careful identifications which are deferred.
- The full staggered taste-shift symmetry group (one-site shift
  composed with a staggered sign rotation). That is a strictly
  larger symmetry group than `(2Z)^3` translation alone; its
  conserved current is the staggered taste current and is out of
  scope. Step 5 of the proof documents why one-site shifts alone
  are not pure translations of `M_KS`.

## Load-bearing Dependencies

- Current public framework memo:
  `MINIMAL_AXIOMS_2026-05-20.md`
  (supersedes `MINIMAL_AXIOMS_2026-05-03.md`, which superseded
  `MINIMAL_AXIOMS_2026-04-11.md`).

## Citations

- prior cycles in this loop, cited for context rather than as
  load-bearing inputs:
  - `docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`
  - `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
  - `docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
  - `docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`
- assumption / derivation ledger, cited for package context:
  `docs/ASSUMPTION_DERIVATION_LEDGER.md`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [minimal_axioms_2026-05-20](MINIMAL_AXIOMS_2026-05-20.md) —
  current public framework memo; framework-axiom dependency after the
  2026-05-25 Step 4b boundary repair and qubit-reframe rebase.
- [staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  — retained-grade narrow theorem supplying the finite-Grassmann
  partition with per-site `(χ_x, χ̄_x)` generators, per-site Fock
  dim 2, and the Berezin determinant readout. Load-bearing for the
  Step 1-3 variational derivation of (5). Added 2026-05-24 rewire
  repair, replacing the old gate-alias dependency per the
  gate-closure synthesis endorsement.

The historical parent-identity alias
for the staggered-Dirac realization gate is no longer
cited as retained one-hop authority for the finite-Grassmann algebra;
that algebra is supplied by the substep-1 narrow theorem above, per the
rewire endorsement in the gate-closure synthesis note. The gate alias
is cited below only as the registered Tier-A
carrier route for the residual `KS-phase-form` structural admission,
not as retained authority and not as closure of that residual. The
chain-pending JW bridge
`STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`
is intentionally not cited as a load-bearing one-hop dependency here
until its pending chain closes.

## Admitted context inputs

Per the 2026-05-10 gate-recategorization repair, the following named
admitted inputs are explicitly carried by this row in addition to its
framework-axiom dependency on `minimal_axioms_2026-05-20`. Per the
2026-05-24 rewire repair, the load-bearing **finite-Grassmann partition
content** of the gate (per-site `(χ_x, χ̄_x)` generators with
anticommutation `(G1)-(G3)`, Berezin integration rules, per-site Fock
dim 2 — the entire algebraic surface used by the Step 1-3 variational
derivation of (5)) is supplied by the retained substep-1 Grassmann narrow theorem
listed below; the historical parent-identity gate alias
for the staggered-Dirac realization gate is not cited as
retained one-hop authority for that finite-Grassmann algebra. It is
cited below only as the registered Tier-A carrier route for the
residual `KS-phase-form` input, per the explicit rewire endorsement
that downstream rows with substep-specific needs should cite the
relevant `STAGGERED_DIRAC_SUBSTEP{1,2,3,4}_*` retained theorems
directly rather than this gate alias.

**Load-bearing one-hop dep (retained):**

- [staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  — supplies the finite-Grassmann partition with per-site `(χ_x, χ̄_x)`
  generators, anticommutation `(G1)-(G3)`, per-site Fock dim 2, and the
  Berezin determinant readout `Z_F[M] = det(M)`. This is the
  load-bearing algebraic surface used by the Step 1-3 variational
  derivation of the bilateral lattice current (5) and the on-shell
  identity (10). The substep-1 narrow theorem isolates exactly this
  per-site Grassmann-vs-bosonic algebraic content from the parent
  staggered-Dirac realization gate and is independently `retained_bounded`.

**Chain-pending support reference (NOT a load-bearing dep yet):**

- `STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`
  supplies the cross-site canonical anticommutation realization
  (`{c_x, c_y^†} = δ_{xy}`) on the tensor-product Fock space
  `H_Λ = V^{⊗|Λ|}` with per-site `V ≅ ℂ²`. It is currently
  `retained_pending_chain`, so it is not in the retained-grade dependency
  set for this row. Once its pending chain closes, it may support corollary
  C1 (conserved fermion-number `Q = Σ_x χ̄_x χ_x` as a Hilbert-space
  quantum number) and C3 (compatibility with reflection-positivity
  superselection), but this rewire does not consume it as audit authority.

**Registered Tier-A carrier route (historical context, not a current
citation-graph dependency):**

- The staggered-Dirac realization gate's canonical parent note,
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, is the
  parent-identity gate alias and registered Tier-A derivation target
  `AC_φλ`, previously recorded as the carrier route for the residual
  `KS-phase-form` input. This parent alias is not retained authority and
  does not close the gate. The current source graph follows the explicit
  narrow suppliers below instead: retained substep-1 Grassmann for the
  finite-Grassmann algebra, retained eta-holonomy and retained_bounded
  chirality/parity for the displayed KS sign/phase surface, and the
  kinetic/P-FLUX cascade for the remaining carrier-selection residual.
  The parent filename remains visible as registered context only, not
  as a markdown dependency edge.

**Residual structural admission (admitted context, not supplied by any
current retained narrow theorem):**

- `KS-phase-form` — the specific Kawamoto-Smit phase structure
  `η_1(x) = +1`, `η_2(x) = (-1)^{x_1}`, `η_3(x) = (-1)^{x_1+x_2}` on the
  nearest-neighbour hop `M_{x,x±μ̂} = ±(1/2) η_μ(x)`. Used in (a) Step 2
  reindexing `η_μ(x' + μ̂) = η_μ(x')`, (b) Step 4b's two-site-shift
  symmetry verification `η_ν(x + 2μ̂) = η_ν(x)`, (c) Step 5's
  one-site-shift counterexample. **Status refresh (2026-06-11):** the
  substep-2 Kawamoto-Smit forcing source-note
  (`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`,
  plain-text pointer) now exists on the surface and proves the forcing
  as a bounded theorem (scalarization iff the Clifford `−1` cocycle,
  with exactly one local gauge class — the KS class), bounded on its
  own declared kinetic-class premises (its P-KIN/P-SD); its current
  ledger grade is not retained, so `KS-phase-form` remains an
  admitted-context structural input here, named rather than silently
  imported. **Status refresh (2026-06-15):** the displayed eta identities
  are now directly supplied in this packet by retained
  `ETA_HOLONOMY_BASE_FLUX_SCOPE_BOUNDARY_NOTE_2026-06-06.md` and
  retained_bounded
  `STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`.
  The full carrier-selection residual is still the kinetic/P-FLUX
  cascade below, so this row remains bounded/conditional; however the
  parent realization-gate alias is no longer a current citation-graph
  dependency. The Noether identities (N1)-(N3) close as stated on the
  admitted KS-phase carrier.

## Kinetic supply-line refresh (2026-06-12; audit-unblock repair)

The 2026-06-11 registered-routing section below correctly kept this
row bounded/conditional because the residual `KS-phase-form` structural
input was still routed through the registered staggered-Dirac target.
Latest main now makes that route sharper without changing this row's
status:

1. [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
   supplies a source-side two-flux-class theorem on the licensed
   nearest-neighbor bilinear surface. Its cache
   `logs/runner-cache/staggered_dirac_kinetic_class_forcing_check_2026_06_10.txt`
   records `TOTAL: PASS=27 FAIL=0`. For this Noether row, the two
   relevant outputs are:
   - P-SD is discharged as the absorbing-frame theorem on the
     flux-`-1` branch;
   - P-KIN is reduced from a broad kinetic-class declaration to the
     one-bit P-FLUX selector `phi = -1`, with `K0` the computed
     countermodel inside the tested constraint set.
2. [`P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`](P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md)
   supplies the conditional composer for that bit. Its cache
   `logs/runner-cache/p_flux_selection_via_fsb_k_check_2026_06_11.txt`
   records `TOTAL: PASS=16 FAIL=0`: using the retained
   [`STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md`](STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md)
   geometry leg, P-FLUX is selected only if FSB-K reaches retained
   grade with its realized-kernel quantifier and FSB-CL intact.
3. [`AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md)
   remains the named open condition for that composer as of this sync.

Thus this Noether row's residual is no longer "derive the entire
Kawamoto-Smit carrier from scratch"; it is the sharper cascade

```text
kinetic-class forcing
  -> P-SD discharged on K1
  -> P-KIN reduced to P-FLUX
  -> P-FLUX conditionally selected by FSB-K + retained Z
```

Source-only sync verifier:
`scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py`;
cache:
`logs/runner-cache/staggered_dirac_kinetic_supply_line_sync_2026_06_12.txt`.

The local Noether algebra is unchanged and remains the same finite
Grassmann/Kawamoto-Smit carrier identity checked by
`scripts/axiom_first_lattice_noether_check.py`. This section does not
promote the row: until the supplier rows are independently audited and
the conditional FSB-K leg resolves, the Noether row remains bounded on
the admitted `KS-phase-form` carrier.

## Registered Tier-A routing (2026-06-11; audit-requested repair; 2026-06-15 graph rescope)

The recorded re-audit target for this row is to "close the full
staggered-Dirac/Kawamoto-Smit kinetic carrier, including the residual
KS-phase-form structural input, with retained-grade authority or keep
this row bounded/conditional." This section takes the precedented
registered-routing form of that repair (per
`PMNS_TWISTED_FLUX_TRANSFER_HOLONOMY_BOUNDARY_NOTE.md` and
`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`,
plain-text precedent pointers): the residual carrier admission is
routed explicitly into the **registered Tier-A derivation target**, so
the citation graph carries a registered admission rather than an
unregistered conditional blocker.

1. **The algebra is standalone.** The load-bearing content — the
   plus-sign bilateral lattice current, the two-step Ward identity,
   and the on-shell Noether identities (N1)-(N3) — closes by finite
   matrix/Grassmann algebra, with the finite-Grassmann partition
   surface supplied by the retained substep-1 narrow theorem (the
   load-bearing one-hop dep above).
2. **What the carrier admission carries.** Only the specific
   Kawamoto-Smit phase form `η_μ(x)` (the `KS-phase-form` residual
   above) consumes the staggered-Dirac realization complex; it is
   substep-2 content of that complex.
3. **The registered target is retained as plain-text context only.**
   The canonical staggered-Dirac realization parent
   remains the registered Tier-A derivation target `AC_φλ` in the
   admission registry (`docs/audit/data/premise_decision_history.json`), but
   this Noether row no longer uses a markdown edge to that parent alias
   as a one-hop dependency. The current dependency graph follows the
   explicit supplier cascade above. This note does **not** close the
   gate, does **not** promote the substep-2 forcing note, and does
   **not** assert a retained-grade carrier-selection result.
4. **No status assertion.** This section makes the narrow re-audit
   case only. The audit lane is the sole authority on whether to honor
   it; this note asserts no `effective_status` and predicts no audit
   outcome.

When the explicit kinetic/P-FLUX cascade closes to retained grade, the
`KS-phase-form` residual admission discharges and the row becomes
eligible for retagging from `bounded_theorem` to `positive_theorem` by
the independent audit lane.

**Removed (2026-05-10 g_bare-removal repair):**
- `g_bare_canonical_normalization_gate` — formerly listed here as a
  named admission. The 2026-05-10 audit verdict's repair-target option
  "separately close or remove the structural `g_bare` dependency if it
  is not load-bearing" applies: the Noether identities (N1)–(N3) are
  quantitatively `g_bare`-independent, with `S_G` entering only via
  the gauge-invariance hypothesis carried by the admitted
  canonical-action surface, not through the `g_bare` numerical
  normalization gate. The gate is therefore removed from this note's
  named-admission list. Sister authorities and other rows that
  genuinely depend on `g_bare` are unchanged; this removal is local to
  this Noether note's load-bearing chain.
