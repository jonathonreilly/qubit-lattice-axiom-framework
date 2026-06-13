# The Koide r=1/2 Selector Is the Chiral L-R Coupling, Not a Symmetry: U(1)_b Is a Red Herring; the Framework Supplies the Grading ε, Not the Coupling

**Date:** 2026-06-05
**Type:** narrow_theorem
**Claim type:** narrow_theorem (localization + correction, computable-side). Sharpens the staggered-Dirac
gate for the Koide magnitude `r = |b|²/a²` and **corrects two premature walls**. The selector between the
first-order/holomorphic reading (`r=1/2`) and the second-order/modulus reading (`r=1`) is **exactly a chiral
left-right coupling** `M(b)⊗σ₊` across the chirality factor — not a continuous symmetry and not a static
complex structure. Within the native generation factor `R³` it is **structurally forbidden** because a
`C₃`-equivariant operator is circulant and therefore commutes with `Γ_χ`, while the only
`C₃`-equivariant `Γ_χ`-anticommuting operator is zero. The converse is not claimed: operators can preserve
the singlet/doublet split and commute with `Γ_χ` without being `C₃`-equivariant. The framework supplies the
chiral **grading** `ε` (#2685) but **not** the chiral **coupling**, whose action term is the gated `AC_φλ`
corner realization.
**Claim scope:** this is **not a derivation of `r = 1/2`**. It localizes the open atom to one dynamics gate
and corrects prior framing. Two corrections: (i) the **U(1)_b/C³=I incompatibility is a red herring** — `Q`
is δ-independent, so the (1,1)-vs-(1,2) count is a **functional choice**, not a quotient by a continuous
symmetry; (ii) the **discrete Z₃-character (clock) index** gives the (1,1) block balance → `r=1/2` while
**respecting C³=I exactly**, so "an index cannot output a continuous ratio" (a concern against #2743) is
resolved — the discrete index selects the *block balance*, not the modulus value directly.
**Status:** review-loop source proposal. No audit verdict; no effective-status change; independent audit
required.
**Runner:** [`scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py`](./../scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py)

## Correction 1 — U(1)_b is a red herring

`Q = Σλ²/(Σλ)²` for the circulant spectrum `λ_k = a + 2|b|cos(δ + 2πk/3)` is **δ-independent**:
`Σλ = 3a`, `Σλ² = 3a² + 6|b|²`, so `Q = (1+2r)/3` with **no δ dependence** (runner (1)). The Koide value
therefore does **not** reference the doublet phase at all; the (1,1)-vs-(1,2) split is a choice of *which
functional* reads the mass operator (block/index vs dimension/trace), **not** a quotient by the continuous
rephasing `U(1)_b`. So "U(1)_b is incompatible with C³=I" — true (runner verifies only the discrete
`δ→δ+2π/3 = C₃` is a spectral symmetry) — **forecloses a mechanism the holomorphic count never required.**
It is not the fatal wall.

## Correction 2 — the discrete Z₃-character index gives (1,1), C³=I respected

The clock grading `ρ(M)=Ω⁻¹MΩ`, `Ω=diag(1,ω,ω²)`, is a genuine non-trivial Z₃ action: `ρ(Cᵏ)=ωᵏCᵏ`
(runner (2a)). The equivariant character lands in `R(C₃)` with multiplicity `(1,1,1)` → block weighting
`(singlet,doublet)=(1,1)` (the multiplicity-functional output — a *choice* of readout, not forced over the
dimension count) → the `3a²=6|b|²` balance → `r=1/2`, **with `C³=I` exact** (runner (2b)). So a
*discrete* index realizes the "count once" without any continuous symmetry — the #2743 index route is
concretely the discrete clock grading, and an index *can* select the block balance.

## The wall: first-order vs second-order is the chiral L-R coupling

The real selector is the **order** of the generation determinant:

- **Within `R³` the first-order reading is structurally forbidden.** The generation chirality grading
  `Γ_χ=(2/3)(I+C+C²)−I` is itself **circulant**, so every C₃-equivariant (circulant) operator **commutes**
  with `Γ_χ`. The only C₃-equivariant `Γ_χ`-anticommuting operator is `0` (`comm(C)∩anticomm(Γ_χ)={0}`,
  runner (3)). This is a forward/native-circulant implication, not a global equivalence: commuting with
  `Γ_χ` only says the singlet and doublet subspaces are preserved, and it does not by itself imply
  `C₃`-equivariance. The native C₃-equivariant mass therefore stays on the **second-order**/`r=1` branch.
  (This is the bounded
  support identity [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md);
  the native circulant mass is correspondingly **Berry-flat** — b-independent Fourier eigenvectors, runner (5)
  — so it lands on the second-order/`r=1` branch, *derived* not assumed, per
  [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md).)
- **The escape is a factor-crossing chiral coupling.** On `R³⊗C²`, `O=I₃⊗σ_x` **commutes** with `C⊗I`
  (C₃-equivariant) **and anticommutes** with `I₃⊗σ_z` (chirality) — it is nonzero (runner (4)). So the
  `Γ_χ`-anticommuting operator the first-order reading needs **exists once chirality sits on a separate tensor
  factor** — which the framework has (`ε`, #2685). The operative term is the **L-R Yukawa block** `M(b)⊗σ₊`,
  which makes the generation eigenvectors b-dependent → nonzero Berry curvature → first-order → `r=1/2`.

> **The selector is exactly that L-R coupling.** The framework supplies the chiral **grading** `ε`, but **not
> the chiral coupling** that wires `ε` to the b-dependent generation mass. The existence of that coupling's
> action term is the open staggered-Dirac corner realization
> ([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md),
> substep-4), and is **not** fixed by `C₃ + C³=I` (which fix only the algebra, not which determinant the
> dynamics evaluate).

## Net

| piece | status |
|---|---|
| `Q=(1+2r)/3` δ-independent → U(1)_b red herring | exact (runner (1)) |
| discrete Z₃-character index → (1,1) → r=1/2, C³=I respected | exact (runner (2)) |
| native circulant `R³` family: C₃-equivariance forces second-order/Berry-flat branch ⇒ `r=1`; converse not claimed outside that family | exact (runner (3),(3c),(5)); cited no-go |
| factor-crossing L-R coupling `M(b)⊗σ₊` = the first-order escape | exact (runner (4)) |
| framework supplies grading `ε`, not the coupling | open gate (AC_φλ corner realization; no retained bridge supplied here) |
| **derive r=1/2** | **open — gated on the corner-mass L-R coupling** |

The contribution is to **name the selector precisely** (a chiral L-R coupling, not a symmetry, not a static
`J`/`ε`, not SUSY) and to **clear two red-herring walls** (U(1)_b; "index can't give a continuous ratio").
It does **not** derive `r=1/2`; the framework does not currently supply the coupling, and `r=1` remains the
forced reading of the native (C₃-diagonal, Berry-flat) generation mass.

## No-go discipline (the within-R³ structural fact is a cited prior no-go)

The within-`R³` structural fact (`comm(C)∩anticomm(Γ_χ)={0}`) is **not** newly asserted here — it is the
bounded algebraic support identity
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
reproven in the runner as the foundation this note sharpens. **Steelman (N7):** the strongest case for `r=1/2`
is that the anti-Hermitian operator `C−C²` has a genuine conjugate `±i√3` doublet pair that CPT fuses to one
complex mode → count once → `r=1/2`. That steelman is **real but conditional on the first-order (anti-Hermitian)
operator**: the Hermitian (second-order) mass has two *independent real* doublet eigenvalues with no pair to
fuse. So CPT-fusion **is** the holomorphic polarization — available only if the corner coupling is first-order.
This is exactly the gate, not a closure.

## Forbidden-import / reprove-and-cite discipline

- Every identity (δ-independence, clock-character multiplicity, `comm(C)∩anticomm(Γ_χ)={0}`, the `R³⊗C²`
  escape, the non-converse counterexample, Fourier Berry-flatness) is **reproven** from the C₃ primitive in
  the runner (sympy exact).
- McKean-Singer / Dolbeault index, Coleman-Weinberg, and the Berry-phase comparators are non-derivation
  context only. No PDG values; `r=1/2` is named only as the target this note does **not** derive.

## 2026-06-12 audit-scope repair

This repair removes the overbroad shorthand `C₃-equivariance ⟺ commutes-with-Γ_χ`. The only retained-side
claim used here is the narrower native-family statement: for circulant generation masses, C₃-equivariance
forces commutation with `Γ_χ`, and the C₃-equivariant/`Γ_χ`-anticommuting intersection is zero.
The converse is **not** claimed in the full endomorphism algebra; the runner exhibits a non-circulant
counterexample.

This repair does **not** supply a retained bridge from `AC_φλ` to the physical `M(b)⊗σ₊` coupling or to the
physical `r`-weighting. Those remain the load-bearing open gates for any positive `r=1/2` derivation.

## 2026-06-13 bridge-scope firewall

The phrase "`M(b)⊗σ₊` is the escape" is an algebraic localization statement
inside the runner's `R³⊗C²` toy factor. It is not a retained bridge from
`AC_φλ` to a framework action term, not a physical `r`-weighting derivation,
and not a proof that the framework supplies the first-order chiral coupling.

The only native-family implication used here is one-way:

```text
C3-equivariant circulant generation mass  =>  commutes with Gamma_chi
```

The converse is false and remains excluded:

```text
commutes with Gamma_chi  does not imply  C3-equivariant.
```

A downstream row must not cite this packet as a retained derivation of
`r=1/2`, of the physical `M(b)⊗σ₊` tensor coupling, of an `AC_φλ` corner mass,
or of the physical `r`-weighting. Those require a separate retained bridge.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
