# Qubit k = 1 Per-Site Selection from Minimal Faithful Representation (Narrow)

**Date:** 2026-05-22
**Type:** positive_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Derive the per-site `k = 1` selection (single faithful complex irrep, `H_x = ℂ²`) from the qubit-per-site axiom plus the standard quantum-information definition of "qubit" as the minimal faithful representation of `M_2(ℂ)`. Replaces the prior k=1 ratification clause (`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II") with a proper derivation candidate.

## Source boundary (2026-06-12)

**Boundary:** axiom-term interpretation / minimal-module identification.
Effective status is audit-derived; this source records only the claim boundary.

The matrix-algebra classification supports the minimal faithful module
statement, but the load-bearing move is identifying the axiom word "qubit" with
the minimal two-dimensional carrier rather than deriving that semantic choice
from operator algebra alone.

This note may be cited for the standard `M_2(C)` module classification and the
minimal-faithful `k=1` reading under the qubit-per-site axiom. It may not be
cited as a retained derivation of the axiom's semantic content or as a
framework-native proof that excludes all nonminimal multiplicity readings
without that semantic premise.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this k=1 derivation is a non-chain-closing
alias/decorative handle, the candidate parent is
[`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

## Why this note exists

The 2026-05-22 k=1 ratification (PR #1656 / commit `f471b5b`) added `k = 1` as a load-bearing axiom-content clause on the canonical axiom surface. Subsequent audit feedback ("the right process is not Option A; auditing axiom docs as positive_theorem would blur categories") suggests the cleaner path is a **derivation** that names standard QI machinery as an explicit input rather than promoting it to axiom-rule status.

This note supplies that derivation. The result is the same — per-site `H_x = ℂ²` with `k(x) = 1` — but the path is now a theorem citing the qubit-per-site axiom on the `Z^3` spatial substrate plus the standard definition of "qubit," not a framework-rule selection requiring user approval.

## Honest scope

This note **does not**:
- Add a new framework rule or axiom
- Re-derive Schur's lemma or Wedderburn classification from scratch (cited as standard math)
- Re-define what "qubit" means (cited as standard QI definition)
- Force chirality choice (ρ_+ vs ρ_-) — separate convention

This note **does**:
- Derive `H_x = ℂ²` with `k(x) = 1` from the qubit-per-site axiom plus standard QI "qubit" definition
- Cite standard simple-matrix-algebra representation theory (Schur + Wedderburn) as the load-bearing math
- Expose the multiplicity-decomposition family `H_x ≅ ρ_+^{n_+} ⊕ ρ_-^{n_-}` and identify `k = 1` as the minimal-faithful case

## Claim

By the qubit-per-site axiom in [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) ("Reality is a qubit at every lattice site. Equivalently: each site `x ∈ Z^3` carries the per-site operator algebra `M_2(ℂ)`, equivalent under the real-algebra isomorphism `M_2(ℂ) ≅ Cl(3,0)`."), combined with the standard quantum-information definition of "qubit" (Nielsen–Chuang Ch. 1; Wilde Ch. 2; Watrous Ch. 1):

**Theorem (narrow).** For every lattice site `x ∈ Z^3`, the per-site Hilbert space `H_x` is `ℂ²` (the minimal faithful complex irreducible module of `M_2(ℂ)`), with multiplicity index `k(x) = 1`.

## Proof

### Step 1 — Standard QI definition of "qubit"

In contemporary quantum information theory, a **qubit** is defined as a 2-dim complex Hilbert space `ℂ²` carrying the operator algebra `M_2(ℂ)` acting irreducibly — equivalently, the **minimal faithful complex irreducible module** of `M_2(ℂ)`. References:

- Nielsen & Chuang, *Quantum Computation and Quantum Information*, Ch. 1.2
- Wilde, *Quantum Information Theory*, Ch. 2.1
- Watrous, *The Theory of Quantum Information*, Ch. 1.1

This is textbook content with no ambiguity.

### Step 2 — Multiplicity classification on `M_2(ℂ)`

Every finite-dimensional complex representation `ρ : M_2(ℂ) → End(V)` decomposes by the **Wedderburn–Artin classification** of representations of simple matrix algebras:

```text
V ≅ ρ_{std}^{⊕ k}                                                        (M)
```

where `ρ_{std}` is the standard 2-dim irreducible representation of `M_2(ℂ)` on `ℂ²`, and `k ∈ ℤ_{≥0}` is the multiplicity. So `dim_ℂ V = 2k`.

For Cl(3,0) (real-algebra label of `M_2(ℂ)` under the retained `cl3_complexification_split_narrow_theorem_note_2026-05-10` §(K3)), the same classification gives:

```text
V ≅ ρ_+^{n_+} ⊕ ρ_-^{n_-}                                                (M')
```

with `(n_+, n_-) ∈ ℤ²_{≥0}` and total multiplicity `k = n_+ + n_-`. The two summands correspond to the chirality split.

### Step 3 — The qubit-per-site axiom selects k = 1

The qubit-per-site axiom says "qubit at every site." By Step 1's standard QI definition, "qubit" is the **minimal faithful** complex irreducible module of `M_2(ℂ)`. By Step 2's classification, the minimal-faithful case is `k = 1`:

- `k = 0` (zero rep `ρ_x ≡ 0`): not faithful — fails the Clifford relation `γ_i² = 1 ≠ 0` under `M_2(ℂ) ≅ Cl(3,0)`
- `k = 1`: minimal faithful, `dim_ℂ V = 2`, single faithful irrep
- `k ≥ 2`: faithful with multiplicity, `dim_ℂ V = 2k ≥ 4`, but **not minimal**

The axiom's "qubit" reading therefore selects `k = 1` via Step 1's definitional minimality.

### Step 4 — Conclusion

```text
H_x  =  ℂ²   ,    k(x) = 1   ,    A_x = M_2(ℂ)
```

for every site `x ∈ Z^3`. ∎

## What this derivation supplies

The same content as the previous k=1 ratification, now stated as a **theorem on the qubit-per-site axiom plus standard QI machinery**, not as a framework rule. Downstream rows that previously cited the k=1 ratification can cite this theorem instead.

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the qubit-per-site axiom and `Z^3` substrate
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md) — retained; supplies (M') chirality split

Named non-derivation imports (standard textbook content):

- **Nielsen–Chuang** Ch. 1.2: standard QI definition of "qubit" as minimal faithful complex irrep of `M_2(ℂ)`
- **Wedderburn–Artin classification** of finite-dim representations of simple matrix algebras (any algebra textbook; Curtis–Reiner, Jacobson)
- **Schur's lemma** (standard linear algebra)

## What this does NOT close

- Chirality convention (ρ_+ vs ρ_-) — separate convention recorded in `AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`
- The staggered-Dirac realization gate's substep-1 multiplicity-selection question for downstream matter content (still open, separate lane)
- Promotion of any audited_conditional row

## Citation-graph note

This is a positive_theorem candidate at narrow-theorem granularity. Same pattern as the retained `cl3_complexification_split_narrow_theorem_note_2026-05-10` and the landed Gleason / Busch / Kraus-Choi / Stinespring / Powers / Tomita / Inner-aut qubit-lattice companions: standard math (Wedderburn + Schur + standard QI definition) applied to the framework's specific substrate to derive a definite per-site selection.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II" — the prior k=1 ratification clause that this derivation supersedes; the axiom-doc cleanup PR will remove that section in favor of citing this derivation after audit retention
- `STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md` — substep-1 U4 conditional that now closes under this derivation
- `r1_qubit_k1_reaudit_queue_2026-05-22.json` — dispatch sidecar for downstream k=1 consumers

## What this file is not

- Not a new framework rule (it's a theorem on the qubit-per-site axiom + standard QI content)
- Not a re-derivation of Schur / Wedderburn (cited as standard)
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
