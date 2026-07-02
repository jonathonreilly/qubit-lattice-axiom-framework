# Koide First-Order Selector Localization: the Native R^3/C3 Circulant Route Fails; Any Physical r=1/2 Selector Must Enter Through a Chiral L-R Coupling Gate

**Date:** 2026-06-05
**Type:** bounded_theorem
**Claim type:** bounded_theorem (finite algebraic localization + correction).
This note does **not** claim a retained physical selector for the Koide
magnitude `r = |b|²/a²`. It proves the exact finite algebraic boundary around
the candidate first-order/holomorphic reading (`r=1/2`) versus the
second-order/modulus reading (`r=1`): the native `R³`/`C₃` route cannot supply a
nonzero `Γ_χ`-anticommuting selector, while a separate chirality tensor factor
can carry such an operator algebraically. If a physical first-order selector is
later supplied, it must enter through a chiral left-right coupling of the
algebraic shape `M(b)⊗σ₊` across that separate chirality factor — not through a
continuous `U(1)_b` symmetry, a static complex structure, or the native `R³`
circulant family alone. The `M(b)⊗σ₊` token names the **algebraic shape inside
the runner's `R³⊗C²` toy**; its identification with a physical action term is
**not** claimed here and is the unsupplied open bridge (see the 2026-06-20
repair below).
**Claim scope:** this is **not a derivation of `r = 1/2`** and not a bridge from
`AC_φλ` to a physical `M(b)⊗σ₊` action term. It localizes the open atom to one
dynamics gate and corrects prior framing. Two corrections: (i) the
**U(1)_b/C³=I incompatibility is a red herring** — `Q` is δ-independent, so the
(1,1)-vs-(1,2) count is a **functional choice**, not a quotient by a continuous
symmetry; (ii) the **discrete Z₃-character (clock) index** gives the conditional
(1,1) block balance → `r=1/2` while **respecting C³=I exactly**, so "an index
cannot output a continuous ratio" (a concern against #2743) is resolved as a
statement about the algebraic block-balance readout, not a framework-selected
physical modulus value.
**Status:** source proposal; independent audit lane owns downstream status.
**Status authority:** independent audit lane only. The note asserts no audit
outcome and does not set, predict, promote, demote, or edit any ledger, queue,
or publication-status surface.
**Runner:** [`scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py`](../scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py)

## Correction 1 — U(1)_b is a red herring

`Q = Σλ²/(Σλ)²` for the circulant spectrum `λ_k = a + 2|b|cos(δ + 2πk/3)` is **δ-independent**:
`Σλ = 3a`, `Σλ² = 3a² + 6|b|²`, so `Q = (1+2r)/3` with **no δ dependence** (runner (1)). The Koide value
therefore does **not** reference the doublet phase at all; the (1,1)-vs-(1,2) split is a choice of *which
functional* reads the mass operator (block/index vs dimension/trace), **not** a quotient by the continuous
rephasing `U(1)_b`. So "U(1)_b is incompatible with C³=I" — true (runner verifies only the discrete
`δ→δ+2π/3 = C₃` is a spectral symmetry) — **forecloses a mechanism the holomorphic count never required.**
It is not the fatal wall.

## Correction 2 — the discrete Z₃-character index can encode (1,1), C³=I respected

The clock grading `ρ(M)=Ω⁻¹MΩ`, `Ω=diag(1,ω,ω²)`, is a genuine non-trivial Z₃ action: `ρ(Cᵏ)=ωᵏCᵏ`
(runner (2a)). The equivariant character lands in `R(C₃)` with multiplicity `(1,1,1)` → block weighting
`(singlet,doublet)=(1,1)` (the multiplicity-functional output — a *choice* of readout, not forced over the
dimension count) → the `3a²=6|b|²` balance → `r=1/2`, **with `C³=I` exact** (runner (2b)). So a
*discrete* index can realize the "count once" algebra without any continuous symmetry — the #2743 index route
is concretely the discrete clock grading. This proves availability of the block-balance algebra; it does
not select that readout as the physical mass weighting.

## The wall: first-order vs second-order requires a chiral L-R coupling gate

The real open gate is the **order** of the generation determinant:

- **Within `R³` the first-order reading is structurally forbidden.** The generation chirality grading
  `Γ_χ=(2/3)(I+C+C²)−I` is itself **circulant**, so every C₃-equivariant (circulant) operator **commutes**
  with `Γ_χ`. The only C₃-equivariant `Γ_χ`-anticommuting operator is `0` (`comm(C)∩anticomm(Γ_χ)={0}`,
  runner (3)). This is a forward/native-circulant implication, not a global equivalence: commuting with
  `Γ_χ` only says the singlet and doublet subspaces are preserved, and it does not by itself imply
  `C₃`-equivariance. The native C₃-equivariant mass therefore stays on the second-order/Berry-flat side of
  the finite comparison; using that side as a physical `r=1` weighting still requires a readout rule.
  (This is the bounded
  support identity [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md);
  the native circulant mass is correspondingly **Berry-flat** — b-independent Fourier eigenvectors, runner (5)
  — so the finite comparison puts it on the commuting/second-order side; treating that side as a physical
  `r=1` weighting still requires a readout rule, per
  [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md).)
- **The escape is a factor-crossing chiral coupling.** On `R³⊗C²`, `O=I₃⊗σ_x` **commutes** with `C⊗I`
  (C₃-equivariant) **and anticommutes** with `I₃⊗σ_z` (chirality) — it is nonzero (runner (4)). So the
  `Γ_χ`-anticommuting operator the first-order reading needs **exists once chirality sits on a separate tensor
  factor** — which the framework has as a grading (`ε`, #2685). A physical first-order branch would need an
  operative **L-R Yukawa block** `M(b)⊗σ₊`, which can make the generation eigenvectors b-dependent. This note
  proves that such an escape is algebraically possible across factors; it does not prove the framework
  supplies the action term or the `r`-weighting rule.

> **The remaining selector gate is the L-R coupling plus a readout rule.** The framework supplies
> the chiral **grading** `ε`, but **not** the chiral coupling that wires `ε` to the b-dependent generation
> mass. The existence of that coupling's action term is the open staggered-Dirac corner realization
> (`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`,
> substep-4), and is **not** fixed by `C₃ + C³=I` (which fix only the algebra, not which determinant the
> dynamics evaluate).

## Net

| piece | status |
|---|---|
| `Q=(1+2r)/3` δ-independent → U(1)_b red herring | exact (runner (1)) |
| discrete Z₃-character index can encode the (1,1) block balance → r=1/2 while respecting C³=I | exact algebraic availability (runner (2)); not a physical selector |
| native circulant `R³` family: C₃-equivariance forces the commuting/Berry-flat side; converse not claimed outside that family | exact (runner (3),(3c),(5)); cited no-go |
| factor-crossing L-R coupling algebraically supplies the first-order escape shape | exact algebraic availability (runner (4)) |
| framework supplies grading `ε`, not the coupling or readout rule | open gate (AC_φλ corner realization; no retained bridge supplied here) |
| **derive r=1/2** | **open — gated on the corner-mass L-R coupling** |

The contribution is to **localize the explicit first-order escape tested here** (a chiral L-R coupling, not
a symmetry, not a static `J`/`ε`, not SUSY) and to **clear two red-herring walls** (U(1)_b; "index can't give
a continuous ratio"). It does **not** derive `r=1/2`; the framework does not currently supply the coupling,
and the native (C₃-diagonal, Berry-flat) generation mass remains on the commuting/second-order side of the
finite comparison.

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
  escape, the non-converse counterexample, Fourier Berry-flatness) is **reproven** from the C₃ cyclic-shift algebra in
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

## 2026-06-15 source-boundary repair

This repair removes the residual positive-selector reading that caused the
terminal conditional audit. The bounded theorem payload is now only:

1. exact `Q` δ-independence, so continuous `U(1)_b` is not the mechanism;
2. exact clock-character multiplicity, so a discrete `C₃` index can encode the
   `(1,1)` block-balance algebra without violating `C³=I`;
3. exact native-family no-go `comm(C)∩anticomm(Γ_χ)={0}`;
4. exact separate-factor escape algebra on `R³⊗C²`;
5. explicit disclosure that no retained bridge supplies the physical
   `AC_φλ -> M(b)⊗σ₊` coupling or the physical first-order/readout weighting.

Accordingly this note should be read as bounded algebraic localization and
no-go demarcation, not as a retained positive theorem deriving the physical
Koide `r=1/2` branch.

## 2026-06-18 bounded-localization source packet

The companion certificate
`KOIDE_FIRST_ORDER_SELECTOR_BOUNDED_LOCALIZATION_CERTIFICATE_2026-06-18.md`
chooses the bounded-localization repair branch named by the prior boundary
review. It is context for this source-boundary repair, not an additional
load-bearing authority:
keep downstream use strictly bounded to the finite algebraic localization
surface, rather than claiming a physical selector bridge.

Load-bearing theorem surface:

1. `Q=(1+2r)/3` is delta-independent, so continuous `U(1)_b` is not the
   selector mechanism.
2. The discrete `C3` clock character has multiplicities `(1,1,1)`, so the
   `(1,1)` block-balance algebra is available without violating `C^3=I`.
3. Inside the native circulant `R^3` generation family,
   `comm(C) cap anticomm(Gamma_chi) = {0}`.
4. On a separate `R^3 tensor C^2` chirality factor, a nonzero algebraic
   factor-crossing anticommuting shape exists.
5. The native circulant mass has b-independent Fourier eigenvectors and stays
   on the Berry-flat/commuting side of the finite comparison.

Non-load-bearing open gates:

- the physical `AC_phi_lambda -> M(b) tensor sigma_+` action term;
- the physical first-order/readout weighting rule;
- any derivation of the Koide `r=1/2` branch.

Thus this row should not be consumed as a retained physical selector. It is a
bounded algebraic localization and route-pruning theorem whose positive value
is that it names the explicit first-order escape isolated by the finite
analysis and removes the native `R^3`/continuous-symmetry routes.

## 2026-06-20 bounded-localization source-boundary repair

The prior boundary review named two branches:

> "retain a bridge from `AC_phi_lambda`/staggered corner data to the physical
> `M(b)` tensor `sigma_+` L-R coupling plus the physical `r`-weighting/readout
> rule, **or keep downstream use strictly bounded to the finite algebraic
> localization**."

This repair confirms the **second** branch. No physical `M(b)⊗σ₊` bridge and no
physical `r`-weighting/readout rule are retained or supplied. The load-bearing
content of this row is **only** the finite algebraic localization:

1. `Q=(1+2r)/3` is exact and `δ`-independent (runner (1)), so continuous
   `U(1)_b` is not the selector mechanism.
2. The discrete `C₃` clock character has multiplicities `(1,1,1)` (runner (2)),
   so the `(1,1)` block-balance algebra is available while respecting `C³=I`.
3. Inside the native circulant generation family,
   `comm(C) ∩ anticomm(Γ_χ) = {0}` (runner (3)); the converse is **not** claimed.
4. On the separate `R³⊗C²` chirality factor a nonzero algebraic
   factor-crossing anticommuting shape exists (runner (4)).
5. The native circulant mass has `b`-independent Fourier eigenvectors and stays
   on the Berry-flat/commuting side of the finite comparison (runner (5)).

The following remain **conditional/open** and are **not** claimed by this row:

- the identification of the runner's `R³⊗C²` toy `M(b)⊗σ₊` shape with a
  **physical** L-R coupling / framework action term (the `AC_phi_lambda` /
  staggered corner bridge is **unsupplied**);
- the physical first-order/readout `r`-weighting rule;
- any derivation of the Koide `r=1/2` branch.

Consistent with the framework's dial discipline, `r=1/2` is a **stable dial
setting, not a forced value**: the bounded surface above neither selects nor
forces it; selecting it physically would require the unsupplied chiral-coupling
and readout bridges. A downstream consumer must read this row **only** as the
bounded algebraic localization (1)-(5) plus the route-pruning statement that the
native `R³`/`C₃`/`U(1)_b` routes do not supply the physical first-order
selector. It must **not** consume this row as a physical selector, an
`AC_phi_lambda → M(b)⊗σ₊` action/readout bridge, or an `r=1/2` derivation.

## Dependencies and Context

Graph-visible load-bearing dependencies:

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)

Context-only, non-load-bearing references:

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — names the open
  physical corner-realization bridge; not consumed as an authority here.
- `KOIDE_FIRST_ORDER_SELECTOR_BOUNDED_LOCALIZATION_CERTIFICATE_2026-06-18.md` —
  prior certificate context absorbed by this source-boundary repair; not
  consumed as an authority here.

**Status authority:** independent audit lane only. This note asserts no
downstream status change.
