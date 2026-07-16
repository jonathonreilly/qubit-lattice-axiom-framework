# Hierarchy L_t = 4 Physical-Selection Proof-Walk Bounded Note

**Current premise authority (2026-07-16):** the legacy “admission”
terminology in earlier versions is normalized here to three explicit
conditional inputs. None of those inputs is an axiom or approved primitive
in `axiom_premise_nodes.json`, and their current live-ledger rows are
`unaudited`; consequently none currently chain-satisfies a dependency.

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; later status is generated
by the audit pipeline after independent review.
**Source-note proposal disclaimer:** this note is a source-note
proposal; audit verdict and downstream status are set only by the
independent audit lane.
**Primary runner:** [`scripts/frontier_hierarchy_lt4_physical_selection_proof_walk.py`](../scripts/frontier_hierarchy_lt4_physical_selection_proof_walk.py)

## 1. Claim scope

> **Theorem (Conditional `L_t = 4` physical-selection proof-walk).**
> Given (i) the cited algebraic source statements and the runner-rederived
> Klein-four orbit calculation on the staggered-Dirac APBC temporal circle
> ([`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md),
> cited without importing its audit status;
> [`HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md`](HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md),
> likewise cited without importing its audit status), and (ii) three explicitly named conditional inputs
> (the staggered-Dirac realization gate, scalar-additivity premise,
> and CPT phase-blindness premise), the algebraic `L_t = 4`
> selector on the staggered block IS the physical EWSB temporal
> block. The three conditional inputs are necessary: without any one of
> them, the algebraic-to-physical bridge does not close from
> the physical Cl(3) local algebra plus Z^3 spatial substrate alone.

This bounded theorem **explicitly does NOT** claim:

- unconditional discharge of any of the three conditional inputs from the
  physical Cl(3) local algebra plus Z^3 spatial substrate;
- closure of the framework's electroweak hierarchy formula
  `v = M_Pl × α_LM^16 × (7/8)^(1/4)` (downstream chain);
- closure of `M_Pl` or `α_LM^16` (separate authority chains);
- retirement of the open staggered-Dirac realization gate
  ([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md));
- a positive-theorem promotion of any cited authority. The
  conditional shape — closure given the three named inputs —
  is the load-bearing content.

This note walks the existing chain step-by-step and isolates the
named conditional inputs, without adding new content beyond making the
conditional shape explicit.

## 2. Background — cited source statements and runner-rederived content

The hierarchy authorities cited above collectively establish the
following four algebraic facts on the exact minimal hierarchy
block (`L_s = 2`, staggered Dirac on APBC temporal circle):

1. **Exact Matsubara closed form** ([`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md),
   cited without importing its audit status):

   ```text
   |det(D + m)|  =  Π_ω  [m² + u_0² (3 + sin²ω)]⁴,
   ω_n = (2n + 1)π / L_t.
   ```

2. **Klein-four orbit decomposition on APBC phases**
   ([`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md`](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md),
   currently `unaudited` per ledger): the APBC temporal phase
   set decomposes into sign-and-conjugation closed orbits under
   the Klein-four action `z → z, −z, z*, −z*`. `L_t = 2` carries
   only the unresolved sign pair `{+i, −i}`; `L_t = 4` carries
   the unique minimal **resolved** orbit of size 4; the runner
   checks the next even cases `L_t = 6, 8` as split into multiple
   orbit sectors.

3. **Context-only finite temporal-weight check.** At `L_t = 4`,
   `sin²((2n+1)π/4) = 1/2` for all `n ∈ {0, 1, 2, 3}`. At the
   checked sizes `L_t ∈ {6, 8}`, the sampled `sin²` values are not
   uniform. These finite facts are recomputed by the paired runner,
   are non-load-bearing here, and do not select a physical temporal
   size or establish uniqueness over all `L_t`.

4. **Spatial-BC and `u_0`-scaling closure**
   ([`HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md`](HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md),
   cited without importing its audit status): on the minimal `L_s = 2` block, spatial APBC
   is selected by the existence of a finite intensive 3+1 order-
   parameter limit, and the linear `1/u_0` tadpole scaling is the
   exact local statement.

Items 1, 2, and 4 supply the stated algebraic/background chain on the
staggered-Dirac block. Item 3 is only a finite context check and does
not contribute a temporal-size selector. What is not settled is the
bridge from "algebraic L_t = 4 on the staggered block" to "physical
EWSB temporal block."

## 3. The bridge chain — four steps + three conditional-input walls

The bridge from algebraic `L_t = 4` to physical EWSB temporal block
is the four-step chain (a)-(d) below. Each step's inputs are
catalogued, and the three named conditional inputs are isolated.

### Step (a). Klein-four orbit on the staggered block at `L_t = 4`

**Statement:** the Klein-four action `z → z, −z, z*, −z*` on the
APBC temporal phases `z_n = exp(i(2n+1)π/L_t)` has a unique minimal
**resolved** orbit at `L_t = 4`.

**Source:** item 2 of §2 above, with the finite orbit calculation
rerun by the paired verifier. This step is algebraic on the checked
sizes. The separate `sin²` samples in item 3 are not used to select
`L_t = 4`.

**Inputs needed:** APBC phase set on the temporal circle;
Klein-four group action.

**Conditional-input walls invoked:** none at this algebraic step.

### Step (b). The EWSB order parameter is a local bosonic CPT-even bilinear

**Statement:** the physical EWSB order parameter, identified with
the local curvature of the effective action
`∂²_φ ΔV_eff |_{φ = 0}`, is:

- bosonic (Z₂ fermion-sign blind);
- quadratic / bilinear in fermions;
- CPT-even (invariant under complex conjugation / time reversal);
- local.

**Source:** [`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md`](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
asserts this identification. The asserted identification names the
order parameter via a continuum effective-action object
(`ΔV_eff`), which is then matched to the lattice scalar generator
via [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).

**Inputs needed:** an identification of the physical EWSB order
parameter with the lattice scalar generator `W[J] = log|det(D + J)|`.
That identification is the scalar-additivity conditional input below.

**Conditional-input wall invoked:**

- **Scalar-additivity / observable-class conditional input.**
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  records the proposed scalar generator `W = log|det(D + J)|` after
  scalar additivity on independent subsystems is supplied. Its current
  live-ledger row is `unaudited`, and the note is not an axiom-premise
  node. Therefore this proof-walk treats the observable-class step as an
  explicit conditional input, not as a chain-satisfying premise.

### Step (c). Klein-four invariance of the EWSB sector

**Statement:** the physical EWSB scalar curvature must be
invariant under the Klein-four action on the APBC temporal
phases.

**Source:** items 2 of §2 (algebraic Klein-four invariance) combined
with item (b) (the EWSB order parameter is the local bosonic
CPT-even bilinear). On the staggered block, the Klein-four
invariance of the bilinear is a structural consequence of CPT-even
phase blindness applied to the source-deformed Dirac determinant.

**Inputs needed:** CPT-even phase blindness on the staggered block.

**Conditional-input wall invoked:**

- **CPT-even phase-blindness conditional input.** The CPT source
  is supplied by [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md), which
  carries `effective_status = unaudited` in the live audit ledger.
  The 2026-05-10 narrow specialization
  [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  also carries `effective_status = unaudited`, and the older
  `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`
  is likewise `unaudited`. None of these sources is currently retained
  or registered as an approved primitive; CPT-even phase blindness is
  therefore an explicit conditional input at the bridge from algebra
  to physical bilinear class.

### Step (d). The physical EWSB temporal block IS L_t = 4

**Statement:** combining (a) + (b) + (c), the physical EWSB scalar
curvature on the staggered block is Klein-four invariant, hence its
temporal support lies in a Klein-four-closed orbit. The unique
minimal resolved Klein-four orbit on the APBC temporal circle is
`L_t = 4`. Therefore the physical EWSB temporal block IS `L_t = 4`.

**Source:** algebraic combination of (a) + (b) + (c).

**Inputs needed:** the staggered-Dirac block on which the curvature
lives must itself be the physical EW substrate.

**Conditional-input wall invoked:**

- **Staggered-Dirac realization conditional input.** The framework baseline is
  **the physical Cl(3) local algebra plus Z^3 spatial substrate**. The
  staggered-Dirac realization on `Z³` (with APBC temporal extent
  and 8-corner doubler structure) is recorded as an **open gate**
  in
  [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  with current `effective_status = unaudited`. Without closure of that
  gate, "the staggered block IS the physical EW substrate" is an
  explicit conditional input, not a derivation. The Klein-four argument lives on
  the staggered block; it inherits the gate.

## 4. Conditional load-bearing statement

> Conditional on (i) the staggered-Dirac realization gate closing
> from the physical Cl(3) local algebra plus Z^3 spatial substrate,
> (ii) scalar-additivity P1 on independent subsystems forcing
> `log|det|` as the physical scalar generator, and (iii) CPT-even
> phase blindness on the staggered block being supplied by a
> chain-satisfying CPT authority, the chain (a) → (b) → (c) → (d)
> in §3 closes and the
> physical EWSB temporal block is `L_t = 4`.

This is the bounded conditional shape this note targets.
**Unconditional discharge of the three conditional inputs from the physical
Cl(3) local algebra plus Z^3 spatial substrate is not closed by this
note.** Each input is recorded by an existing `unaudited` authority row
in the live ledger and remains non-chain-satisfying.

## 5. Proof-Walk catalogue

The chain has four steps and three conditional inputs. The proof-walk
catalogue is:

| Step | Statement | Algebra source | Conditional-input wall? |
|---|---|---|---|
| (a) | Klein-four orbit on APBC phases, unique resolved at L_t=4 | cited Matsubara source + Klein-four orbit source + cited spatial-BC source | none (algebraic) |
| (b) | EWSB order param = local bosonic CPT-even bilinear = `log\|det\|` curvature | bosonic-bilinear selector + observable principle | scalar-additivity input |
| (c) | Physical EWSB curvature is Klein-four invariant | CPT-even phase blindness on staggered D | CPT phase-blindness input |
| (d) | Therefore physical EWSB temporal block = L_t = 4 | (a) ∧ (b) ∧ (c); staggered block IS physical substrate | staggered-Dirac realization gate |

The checked proof-walk **does not** add any new axiom, any new
repo-wide theory class, or any retained status claim. It does
not discharge any of the three conditional-input walls.

## 6. Forbidden imports check

- **NO** new framework axioms beyond the physical Cl(3) local algebra
  plus Z^3 spatial substrate baseline.
- **NO** PDG observed values consumed as derivation inputs.
- **NO** fitted matching coefficients.
- **NO** new repo vocabulary. Terms used (`Klein-four`,
  `APBC temporal circle`, `staggered Dirac`, `bilinear`,
  `EWSB`, `effective potential`, `CPT-even`,
  `scalar additivity`) are all standard physics / repo-canonical
  vocabulary.
- **NO** new repo-wide tags. The note is positioned as a `bounded_theorem`
  proof-walk in the existing proof-walk-bounded-note family.

## 7. Load-bearing boundary

The load-bearing result is a bounded reframing: it recasts the
algebraic Klein-four orbit result into the conditional
physical-selection statement by walking the four bridge steps and
isolating the three conditional inputs. The orbit content is supported by the
named upstream rows plus the paired verifier. The runner's finite
`sin²` checks are context-only and do not supply the physical selector;
the bridge to "physical" remains conditional on the three named
inputs.

## 8. What this bounded theorem supports

- An **explicit catalogue** of the three conditional-input walls between
  the runner-rederived algebraic L_t = 4 result and the physical EWSB
  temporal-block claim used by the v formula
  `v = M_Pl × α_LM^16 × (7/8)^(1/4)`.
- A **conditional load-bearing statement** that downstream rows
  citing the L_t = 4 selection can use to inherit the three
  conditional-input walls explicitly rather than implicitly.
- **Audit-tractable narrowing**: the electroweak hierarchy
  baseline conditional input used by the v formula is now decomposed into
  three existing authority rows: the staggered-Dirac realization
  gate, scalar-additivity P1, and CPT-even phase blindness.

## 9. What this theorem does NOT close

- **Unconditional retirement of the staggered-Dirac realization gate.** Closure of the
  staggered-Dirac realization gate from the physical Cl(3) local algebra plus Z^3 spatial substrate is the explicit
  open-gate identity carried by
  [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md);
  it is not retired here.
- **Unconditional retirement of scalar-additivity P1.** Derivation of scalar
  additivity P1 on independent subsystems from the physical Cl(3) local algebra plus Z^3 spatial substrate is the
  audit-named repair target for
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md);
  it is not retired here.
- **Unconditional retirement of CPT-even phase blindness.** Closure of
  CPT-even phase blindness remains downstream of
  [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) (unaudited) and
  [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  (unaudited); it is not retired here.
- **The v formula closure.** The full chain
  `v = M_Pl × α_LM^16 × (7/8)^(1/4)` includes `M_Pl` closure,
  `α_LM^16` closure, and the `(1/4)` outer-exponent closure
  (downstream of `HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`);
  none of those is in scope here.

## 10. Verification (runner)

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_lt4_physical_selection_proof_walk.py
```

The runner verifies the finite algebraic content:

1. **T1.** On `L_t = 4`, the APBC phase set under the Klein-four
   action `z → z, −z, z*, −z*` is one orbit of size 4
   (recomputed via `cmath` on the explicit phase list, independent
   of the cited authority).
2. **T2.** On `L_t = 2`, the APBC phase set is one orbit of size 2
   (the unresolved `{+i, −i}` sign pair, no resolved orbit).
3. **T3.** On `L_t ∈ {6, 8}`, the APBC phase set splits into
   multiple Klein-four orbit sectors.
4. **T4.** `sin²((2n + 1)π/4) = 1/2` for all `n ∈ {0, 1, 2, 3}`
   (finite context check only; not a temporal-size selector).
5. **T5.** `sin²((2n + 1)π/6)` takes values `{1/4, 1, 1/4, 1/4, 1, 1/4}`
   (finite context check only; non-uniform at `L_t = 6`).
6. **T6.** Conditional-input catalogue: the proof-walk has exactly
   three explicit inputs, each tied to a live upstream authority row
   that is neither retained-grade nor present in the approved
   axiom/primitive registry. The runner reads tracked governance shards
   so the non-chain-satisfying conditional shape is checked at runtime
   without pinning one exact mutable audit status.
7. **T7.** Forbidden-imports check: the runner re-derives T1-T5
   from `cmath` / `math` only, with **no** import of PDG values,
   `M_Pl`, `α_LM`, `u_0`, or any framework numerical constant.

Target PASS = 7, FAIL = 0.

## 11. Cross-references

### Algebraic source statements (audit-owned status)
- [`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md)
  — cited source for the exact Matsubara determinant
  closed form on `L_s = 2`.
- [`HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md`](HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md)
  — cited source stating that a finite intensive 3+1 limit forces spatial
  APBC at `L_s = 2`.

### Arithmetic context only
- `HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`
  — positive-theorem source pending independent re-audit; proves that
  two ratios equal `7/8` while a separate alignment residual vanishes
  at `d = 4`. Its finite `sin²` checks are context-only and do not
  select `L_t` or enter the physical-selection chain here.

### Algebraic upstream and bridge context
- [`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md`](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
  — unaudited (bounded_theorem); algebraic Klein-four orbit
  decomposition statement. The present proof-walk recomputes its
  algebraic content T1-T5 from primitives, while its EWSB-bilinear
  identification remains part of the disclosed bridge context.

### Conditional-input authorities
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  — unaudited; staggered-Dirac realization gate authority.
- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  — unaudited; scalar-additivity P1 source, not an axiom-premise node.
- `OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md`
  — meta; records the audit verdict naming P1.
- [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
  — unaudited; CPT-even phase-blindness authority.
- [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  — unaudited; CPT-even phase-blindness narrow specialization.
- `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`
  — unaudited; CPT-even phase-blindness older route.

### Framework axiom set
- `MINIMAL_AXIOMS_2026-05-03.md`
  — meta; records the physical Cl(3) local algebra plus Z^3 spatial
  substrate baseline.

### Downstream chain (relational, not load-bearing here)
- `HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`
  — unaudited (bounded_theorem); handles the `(1/4)` outer
  exponent question; not consumed here.
- `COMPLETE_PREDICTION_CHAIN_2026_04_15.md`
  — full `v = M_Pl × α_LM^16 × (7/8)^(1/4)` chain; not closed by
  this note.

## 12. Audit boundary

This note is a conditional proof-walk. It walks the existing four-
step bridge chain from the runner-rederived algebraic L_t = 4 result on the
staggered block to the physical EWSB temporal block, isolates the
three disclosed conditional inputs, and states the
conditional closure. It does not retire any of the three walls. It
does not promote any cited authority. The audit lane is the
authority on effective status; this proposal merely contributes a
bounded conditional row whose load-bearing chain is the
conditional-input catalogue plus the conditional closure statement.
