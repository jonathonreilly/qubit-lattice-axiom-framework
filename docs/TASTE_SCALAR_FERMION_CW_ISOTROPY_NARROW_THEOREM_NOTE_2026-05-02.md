# Taste-Scalar Fermion Coleman-Weinberg Isotropy — Narrow Theorem

**Date:** 2026-05-02
**Type:** bounded_theorem (axiom-reset source narrowing 2026-05-03; source-scope sync 2026-06-12)
**Physical context pointer:** staggered-Dirac realization derivation target
(plain-text, non-load-bearing for the theorem below:
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`).
**Primary runner:** `scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py`

## Claim scope (proposed)

> On `ℂ⁸ = (ℂ²)^{⊗3}` with commuting taste-shift involutions `S_i = σ_x ⊗ I ⊗ I, I ⊗ σ_x ⊗ I, I ⊗ I ⊗ σ_x` and the linear taste Hamiltonian
> `H(φ) = Σ_i φ_i S_i`, the one-loop fermion Coleman-Weinberg Hessian
> at the axis-aligned point `φ = (v, 0, 0)` (with `v ≠ 0`) is
> exactly isotropic:
> ```
> ∂²V_f / ∂φ_i ∂φ_j  =  δ_{ij} · C(v)
> ```
> for any smooth `f` such that `V_f(φ) = Σ_s f(λ_s(φ)²)`.

The narrow scope is **purely the fermion Coleman-Weinberg isotropy
identity** on the binary taste block. The parent audit handoff's safe
boundary was the exact fermion Coleman-Weinberg block; this narrow theorem
keeps only that algebraic scope.

The narrow theorem **does not** claim:

- gauge-loop or scalar-loop contributions to the Hessian (these use
  separate split models that are bounded — out of scope here);
- electroweak minimum selection or phase-transition consequences (separate downstream);
- Higgs-mass splitting from any non-fermionic source (separate);
- a Standard-Model Higgs-sector prediction.

## Formal inputs

| Input | Status | Role |
|---|---|---|
| Binary product algebra `ℂ⁸ = (ℂ²)^{⊗3}` with `σ_x` shift operators | internal algebra setup | Load-bearing algebraic surface for the isotropy identity. |
| `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | plain-text context pointer | Non-load-bearing physical taste/fermion naming context; not used to prove the binary orthogonality identity. |
| [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) | axiom memo | Current axiom surface (registered premise node; replaces the superseded 2026-05-03 memo). |

The note operates on the abstract Cl(3)/Z³ taste-cube structure. While
this structure is the framework's setup, the load-bearing step does not
depend on the physical realization gate; it is an algebraic identity on
binary products of σ_x operators. The staggered-Dirac filename above is a
plain-text context pointer only, not a citation edge. The markdown axiom-memo
link records historical axiom context so graph consumers do not treat the row
as no-context bookkeeping.

## Physical-context narrowing (2026-06-11; audit-requested repair)

The 2026-06-11 conditional audit repair allowed this row to narrow the
physical-context dependency rather than obtain retained-grade closure of the
staggered-Dirac gate. This section takes that narrowing route.

1. **The algebra is standalone.** The load-bearing theorem closes on the
   binary orthogonality identity and the Hessian factorization
   `∂_ij f(λ²) = (2f'(v²)+4v²f''(v²))(-1)^{s_i+s_j}` at
   `φ = (v, 0, 0)`. No carrier input is used.
2. **What the physical context carries.** The pointer
   `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` carries only the
   physical taste-block/fermion naming. The proof and runner do not consume
   the staggered Dirac action, the BZ-corner realization, or any
   Grassmann/CAR carrier construction.
3. **Citation narrowing.** Gate-note references in this note are plain-text
   pointers, not markdown links. The physical-context dependency is
   explicitly **NON-LOAD-BEARING** for the Hessian factorization theorem.
   The independent audit lane decides how to read this narrowing; this note
   asserts no audit or effective status.

## Load-bearing step (class A)

```text
Setup: C^8 = (C^2)^{⊗3}, simultaneous shift-eigenbasis |s_1, s_2, s_3⟩
       with s_i ∈ {0, 1}.
Operators: S_i = σ_x acting on tensor factor i.
Eigenvalue: S_i |s⟩ = (-1)^{s_i} |s⟩ in the simultaneous S_i eigenbasis.
            Equivalently, rotate each tensor factor so σ_x is diagonal;
            the formal identity is basis-independent.

H(φ) = Σ_i φ_i S_i  →  λ_s(φ) = Σ_i φ_i (-1)^{s_i}    [exact eigenvalue]

At φ = (v, 0, 0):  λ_s(v, 0, 0) = v · (-1)^{s_1}, so |λ_s| = v ∀s.
                   Therefore  f(λ_s²) = f(v²)  ∀s.

Hessian:
    ∂²V_f / ∂φ_i ∂φ_j |_{φ=(v,0,0)}
       = Σ_s [ 2 f'(λ_s²) (∂λ_s/∂φ_i)(∂λ_s/∂φ_j)
              + 2 λ_s f''(λ_s²) λ_s (∂λ_s/∂φ_i)(∂λ_s/∂φ_j) ... ]
         simplified at λ_s² = v² uniform:
       = [coeff in v] · Σ_s (-1)^{s_i} · (-1)^{s_j}

Binary orthogonality sum:
    Σ_{s ∈ {0,1}^3} (-1)^{s_i} · (-1)^{s_j}
       = (Σ_{s_i ∈ {0,1}} (-1)^{2 s_i}) · (Σ_{s_j ≠ i} 1) · 4   if i = j
       = 8 · δ_{ij}                                           [exact]

Therefore Hessian = δ_{ij} · C(v) where C(v) absorbs the 8 and the
f-derivatives.   ∎
```

This is class (A) — algebraic identity on binary product structure.
No external source is load-bearing.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py
```

Verifies, at exact rational precision via Python `Fraction`:

1. Binary orthogonality sum `Σ_s (-1)^{s_i}(-1)^{s_j} = 8 δ_{ij}` for all
   pairs `(i, j) ∈ {1, 2, 3}²`.
2. Eigenvalue `λ_s(φ) = Σ_i φ_i (-1)^{s_i}` is exact for any φ.
3. At `φ = (v, 0, 0)`: `λ_s² = v²` uniformly across all 8 basis states
   (verified for `v ∈ {1, 2, -3, 7/11}`).
4. Hessian off-diagonal `∂²/∂φ_i ∂φ_j` for `i ≠ j` evaluates to 0 at
   the axis-aligned point (concrete exact tests for several `f`
   choices: `f(x) = x`, `f(x) = x²`, `f(x) = x³`).
5. Hessian diagonal `∂²/∂φ_i ∂φ_i` evaluates to a common value; concrete
   examples have nonzero common value.

## Audit-lane disposition (proposed)

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Pure algebraic isotropy identity for one-loop fermion Coleman-Weinberg
  Hessian on Cl(3)/Z³ taste block at axis-aligned point phi=(v,0,0).
  Gauge-loop, scalar-loop, EW-phase-transition, and Higgs-sector
  consequences explicitly out of scope.
proposed_load_bearing_step_class: A
audit_required_before_effective_retained: true
```

Audit handling is external to this note. The load-bearing identity is
self-contained algebra on binary products; the staggered-Dirac filename is
retained only as non-load-bearing physical context, and the axiom memo remains
historical context. Independent audit handling decides any row state.

## What this theorem closes

The exact fermion Coleman-Weinberg isotropy half of the parent
`TASTE_SCALAR_ISOTROPY_THEOREM_NOTE`. The parent audit handoff named this
as the safe algebraic scope.

## What this theorem does NOT close

- Gauge-loop Hessian contributions (separate bounded model).
- Scalar-loop Hessian contributions (separate bounded model).
- Electroweak minimum selection, phase transition, or thermal scalar-cubic
  claims (separate bounded lanes).
- The full Higgs-sector spectrum (separate).

## Cross-references

- `TASTE_SCALAR_ISOTROPY_THEOREM_NOTE.md` — parent with a conditional audit
  verdict; this narrow theorem carves out the fermion CW isotropy half
  cleanly.
- Cycles 1-7 (PRs #292-302) — sister narrow theorems on different lanes.


## Historical hypothesis bookkeeping (axiom-reset 2026-05-03; narrowed 2026-06-11)

Per `MINIMAL_AXIOMS_2026-05-03.md`, the original axiom-reset bookkeeping
listed the staggered-Dirac realization derivation target as physical context
for fermionic/taste-block language. The 2026-06-11 narrowing above makes that
context non-load-bearing: the proof and runner use only the abstract binary
product algebra, the eigenvalue formula, and the Hessian factorization. They
do not invoke fermion fields, fermion-number operators, fermion correlators,
fermion bilinears, the staggered Dirac action, the BZ-corner doubler
structure, the `hw=1` triplet, charged-lepton sector content, neutrino sector
content, quark / hadron content, the Koide / PMNS / CKM observable surfaces,
or the Grassmann CAR boundary structure.

Plain-text parent pointer: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
(`claim_type: open_gate`). Historical in-flight supporting work (see
`MINIMAL_AXIOMS_2026-05-03.md`):

- `PHYSICAL_LATTICE_NECESSITY_NOTE.md`
- `THREE_GENERATION_STRUCTURE_NOTE.md`
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`
- `scripts/frontier_generation_rooting_undefined.py`
- `GENERATION_AXIOM_BOUNDARY_NOTE.md` (preserved)

These entries are a historical context dependency for this theorem's physical
naming only: a non-load-bearing physical-context edge, not an input to the
Hessian factorization or runner checks.

## Audit context repair pointers

This graph-bookkeeping section preserves the historical axiom-memo citation
named by a prior conditional audit and lists the staggered-Dirac gate as a
plain-text context pointer only. It does not promote this note or change the
audited claim scope.

- `staggered_dirac_realization_gate_note_2026-05-03` (plain-text physical-context pointer; non-load-bearing)
- [minimal_axioms_2026-06-05](MINIMAL_AXIOMS_2026-06-05.md) —
  current premise node (repointed 2026-06-11 from the superseded
  2026-05-03 memo).

## Changelog

- **2026-06-11** — audit-requested repair: demoted staggered-Dirac gate-note
  references from markdown links to plain-text context pointers, added the
  explicit non-load-bearing physical-context narrowing, and corrected the
  verification prose to the runner's `x³` example.
- **2026-06-12** — source-scope sync: kept the staggered-Dirac context
  non-load-bearing and removed the runner's live audit-status read.
