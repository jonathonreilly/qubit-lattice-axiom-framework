# PWC Derivation from the Standard Cumulant Generating Functional (Narrow)

**Date:** 2026-05-22; 2026-06-17 finite-source proof repair
**Claim type:** bounded_theorem
**Status:** bounded finite-source proof; independent audit required.
**Status authority:** independent audit lane only.
**Purpose:** Prove, on the finite qubit-region commuting-source surface,
that `W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` is exactly the
connected cumulant generator for the supplied finite-region state
`ρ_ref`. Textbook cumulant-generator references are retained as
parallel provenance, not as load-bearing premises. The clean theorem
scope is commuting bounded source families, with the noncommuting
quantum ordering convention left explicit.
**Primary runner:** [`scripts/pwc_commuting_cgf_framework_native_2026_06_17.py`](../scripts/pwc_commuting_cgf_framework_native_2026_06_17.py)

## Source boundary (2026-06-12)

**Boundary:** finite commuting-source proof over a supplied state, not a
derivation of the state or of a noncommuting ordering convention.
Effective status is audit-derived; this source records only the claim
boundary.

The derivative signs and normalization are proved on the
commuting-source scope by the finite spectral-measure calculation below
and by the registered runner. The load-bearing move is no longer a bare
appeal to textbook CGF terminology: once `rho_ref` and a commuting
finite source family are supplied, the trace expression itself has the
connected-cumulant derivatives. This note still does not derive `rho_ref`,
the probabilistic/state bridge, or any noncommuting ordering convention.

This note may be cited for the commuting-source cumulant identity and sign
convention. It may not be cited as a retained derivation of `W[J]` from minimal
axioms, of the reference state, or of the noncommuting source convention.

## 2026-06-17 finite-source proof repair

The previous source surface described the row as a standard-object
identification and cited probability / statistical-mechanics textbooks
as named non-derivation imports. This repair changes the load-bearing
shape:

- the finite commuting-source theorem is proved directly from the joint
  spectral decomposition of mutually commuting observables on a finite
  qubit-region algebra;
- the runner verifies `W[0]=0`, first, second, and third derivative
  cumulant identities with the fixed `(-1)^n` source-sign convention;
- the runner verifies that the trace expression and spectral-measure
  expression agree exactly on a two-qubit finite region;
- falsification legs show that dropping the logarithm gives raw
  moments, not connected cumulants, and that linearizing the source
  loses the connected second cumulant;
- textbook references now serve as parallel provenance for the same
  finite calculation, not as load-bearing premises.

Noncommuting source families remain outside this theorem.

## Why this note exists

The framework uses the pre-record connected generating functional `W[J]` whose `n`-th `J`-derivatives at `J = 0` are the connected `n`-point cumulants of observables under `ρ_ref`. The earlier ratification path (bundled in the closed PR #1658) proposed adding the explicit definition `W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` as a load-bearing framework rule alongside k=1 / LSP-projective / PRR-local.

Following the same audit-feedback that drove the k=1, LSP-projective, and PRR-local derivation refactors, this note **identifies** the framework's `W[J]` as the standard cumulant generating functional of probability theory — i.e., as **which** standard mathematical object `W` already is — rather than ratifying its form as a framework rule.

## Honest scope

This note **does not**:
- Add a new framework rule
- Claim Pattern-L-style "selection from a family" for the commuting finite-source cumulant generator
- Derive or audit the choice of `ρ_ref` (`rho_ref`); this note takes the finite-region state as the input to the cumulant generator
- Resolve noncommuting operator-ordering, Wick / Schwinger rotation, time-ordering conventions, or path-integral measures (separate lanes)

This note **does**:
- Prove the finite commuting-source cumulant identities directly from
  the joint spectral measure induced by `ρ_ref`
- Cite standard probability / statistical-mechanics treatments only as
  parallel provenance for the same object
- Record and runner-check that `W[0] = 0` and
  `∂^n W / ∂J^n |_{J=0}` reproduces `(-1)^n` times the connected
  `n`-point cumulant of the commuting source observables

## Position: identification, not selection

The selection / identification distinction matters for Pattern-L circularity discipline:

- **Selection (Pattern-L-circular).** "Among a family of candidate functionals `{W_α[J]}`, the framework selects `W_0[J]`." This requires axiom-level input picking out which member of the family the framework uses, and risks circularity if downstream content already constrains the choice.
- **Identification (the current case).** "On the commuting-source scope, there is one standard mathematical object — the cumulant generating functional — and the framework's `W` is that object." No family to select from; the standard definition is what `W` *is*.

For commuting bounded sources, the finite trace expression reduces to
the joint spectral measure and the logarithm extracts connected
cumulants. For noncommuting quantum sources, the same expression is a
standard Kubo/statistical-mechanics source convention, but this note
does not prove ordering equivalence and does not eliminate the separate
ordering-convention lane.

The pre-record subscript reflects which state `ρ_ref` is used; this note does not derive that state. The cumulant-generating-functional form itself is not a framework choice on the commuting-source scope.

## Claim

For a given finite-region pre-record reference state `ρ_ref` on the one-qubit operator algebra over the `Z^3` spatial substrate, with `J` an observable source coupled to bounded self-adjoint operators on `A_Λ`:

**Theorem (narrow commuting-source form).** For a finite family of mutually commuting bounded self-adjoint source observables on `A_Λ`, the framework's pre-record connected generating functional is

```text
W[J]  :=  log Tr(ρ_ref · e^{-J})  -  log Tr(ρ_ref)                       (PWC)
```

This is the finite joint-spectral cumulant generator induced by
`ρ_ref` and the commuting source family. Its `n`-th `J`-derivatives at
`J = 0` reproduce `(-1)^n` times the connected `n`-point cumulants of
those commuting source observables under `ρ_ref`. Since
`Tr(ρ_ref) = 1` for normalized `ρ_ref`, the second term vanishes and
`W[J] = log Tr(ρ_ref · e^{-J})` directly. The `- log Tr(ρ_ref)` term is
recorded for the general case where `ρ_ref` may not yet be normalized
(e.g., in intermediate constructions).

## Proof

### Step 1 — Finite joint-spectrum calculation

Let `O_1,...,O_m` be mutually commuting bounded self-adjoint operators
on a finite region algebra `A_Λ`. By simultaneous finite-dimensional
spectral decomposition, there is a common eigenbasis indexed by `r`,
with eigenvalue vectors `o(r) = (o_1(r),...,o_m(r))`. For a positive
finite-region state `ρ_ref`, set `w_r := <r|ρ_ref|r>`. Off-diagonal
entries of `ρ_ref` do not contribute to the trace of a diagonal source
exponential, so

```text
Tr(ρ_ref e^{-Σ_a J_a O_a}) = Σ_r w_r exp(-Σ_a J_a o_a(r)).              (P1)
```

Therefore

```text
W[J] = log(Σ_r w_r exp(-Σ_a J_a o_a(r))) - log(Σ_r w_r).                (P2)
```

This finite formula proves the needed identities by direct
differentiation:

- `W[0] = 0`;
- `∂_a W|_0 = -E[O_a]`;
- `∂_a∂_b W|_0 = E[O_a O_b] - E[O_a]E[O_b]`;
- higher derivatives give `(-1)^n` times the corresponding connected
  cumulants, because the logarithm is exactly the finite moment-to-
  cumulant transform.

The runner verifies these identities exactly through third order on a
non-degenerate two-source finite spectrum and also checks falsifiers:
without the logarithm the second derivative is the raw moment, not the
connected covariance; with a linearized source the connected second
cumulant disappears.

Classical probability texts call (P2) the cumulant generating
functional; those references are parallel provenance, not the
load-bearing proof.

### Step 2 — Quantum extension

For a quantum state `ρ` and a mutually commuting bounded self-adjoint
source family `J = Σ_α J_α O_α`, Step 1 is already the quantum proof:
the trace reduces to the finite joint spectral measure. Quantum
statistical mechanics commonly writes the same source-coupled
expression as

```text
W[J]  :=  log Tr(ρ · e^{-J})  -  log Tr(ρ).                              (Q1)
```

The sign convention `e^{-J}` matches the partition-function convention `Z = Tr(e^{-βH})` of quantum statistical mechanics; the framework follows this convention.

**Sign bookkeeping (made explicit).** With the `e^{-J}` convention, the order-`n` `J`-derivative at `J = 0` returns `(-1)^n` times the connected `n`-point cumulant `κ_n`: `κ_n = (-1)^n · ∂^n W / ∂J^n |_{J=0}`. The `(-1)^n` is a fixed bookkeeping factor of the chosen source convention, not an ambiguity — even-order cumulants come out with the textbook sign, odd-order ones carry the explicit `(-1)`. The list below states the raw `δW/δJ` derivatives (carrying the `e^{-J}` sign); the cumulants are these times `(-1)^n`.

The functional `W[J]` satisfies:

- `W[0] = log Tr(ρ) - log Tr(ρ) = 0` (normalization)
- `δW / δJ_α |_{J=0} = - Tr(ρ O_α)` (the `-` is the `n=1` factor `(-1)^1`, so `κ_1 = Tr(ρ O_α)`)
- `δ²W / δJ_α δJ_β |_{J=0} = Tr(ρ O_α O_β) - Tr(ρ O_α) Tr(ρ O_β)` for commuting `[O_α, O_β] = 0`; `(-1)^2 = +1` times the connected two-point function (covariance) — the textbook sign
- Higher functional derivatives give `(-1)^n` times the connected `n`-point functions

For commuting observable families (`[O_α, O_β] = 0` for all `α, β`),
the multivariate quantum cumulant generating functional is therefore
proved by the finite joint-spectrum calculation. For non-commuting
families, ordering issues require care; (Q1) is a standard Kubo/source
convention, not a proof that all ordering choices are physically
equivalent.

### Step 3 — Framework's `W[J]` is exactly (Q1)

For the commuting-source scope, the framework's pre-record connected generating functional is

```text
W[J]  :=  log Tr(ρ_ref · e^{-J})  -  log Tr(ρ_ref)                       (PWC)
```

This is the right-hand side of (Q1) with `ρ = ρ_ref`. On commuting source families, the framework's `W[J]` is therefore the standard cumulant generating functional applied to the given pre-record reference state. **Identification.**

For normalized `ρ_ref` (which is the standing assumption on PRR), `Tr(ρ_ref) = 1` and `log Tr(ρ_ref) = 0`, so

```text
W[J]  =  log Tr(ρ_ref · e^{-J}).                                         (PWC-normalized)
```

The `- log Tr(ρ_ref)` term is the standard general-case normalization shift that keeps `W[0] = 0` even for un-normalized `ρ`.

### Step 4 — Why this is not Pattern-L circularity

Pattern L circularity arises when an axiom-level claim **selects** one element from a family of mathematically distinct candidates whose downstream content already depends on the selection. The selection-out-of-a-family structure is what makes the choice load-bearing.

On the commuting finite-source scope, there is no competing family of cumulant generators:

- Standard probability theory defines **one** cumulant generating functional `K(t) = log E_μ[e^{tX}]` (P1).
- Standard quantum statistical mechanics uses `W[J] = log Tr(ρ e^{-J}) - log Tr(ρ)` (Q1) as the Kubo/source convention.
- The framework's `W[J]` (PWC) **is** that standard object applied to `ρ_ref`. Not a selection; an identification.

Alternative functional forms with different `n`-point structure (e.g., `Tr(ρ J^n)` without the logarithm, or `Tr(ρ log e^{-J})` with the log inside) are **not cumulant generating functionals** on this commuting-source scope; they are different objects with different `n`-point content. Noncommuting ordering conventions remain explicitly outside this note's closure.

So on the stated commuting-source scope, the framework's `W[J]` form is the standard mathematical object, not a Pattern-L-selected member of a candidate family. The broader noncommuting ordering lane remains open.

### Step 5 — Conclusion

For commuting bounded source families, the framework's
`W[J] = log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` is the finite
joint-spectral cumulant generator applied to the supplied finite-region
state `ρ_ref`. Its content (connected `n`-point cumulants as
`J`-derivatives at `J = 0`, with the fixed `(-1)^n` sign convention)
follows by direct finite-dimensional differentiation. No framework-rule
selection is required on that scope. ∎

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — supplies the current Lattice/Quantum/Record axiom memo; this row uses only the Lattice and Quantum finite-region algebra surface on which `ρ_ref` lives

Parallel provenance (not load-bearing premises):

- **Cumulant generating functional** in classical probability (Feller Vol. II Ch. VII §5; Billingsley §21; standard MGF / cumulant theory)
- **Quantum cumulant generating functional** in quantum statistical mechanics (Kubo-Toda-Hashitsume *Statistical Physics II* Ch. 1; Jaksic-Pillet course; standard finite-temperature source-coupled formalism)
- **Joint spectral measure** for commuting bounded observable families (standard)

Plain-text contextual pointer (not load-bearing dep):

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — one framework route for deriving the reference state later used as the `ρ_ref` input

## What this derivation supplies

The same `W[J] = log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` form, now
proved as the finite joint-spectral connected-cumulant generator
applied to `ρ_ref` on commuting source families, not a load-bearing
framework rule. The "selection from a family" structure that would have
made it a framework rule does not exist on that narrow scope.

## What this does NOT close

- **Wick / Schwinger rotation between Euclidean and Lorentzian sources** — separate lane
- **Time-ordering and operator-ordering conventions for non-commuting `J`** — standard but separate lane
- **Path-integral measure / Wilson lattice measure compatibility with `ρ_ref`** — separate lane (the Radon-Nikodym question flagged in the tracial-route note)
- **Choice or derivation of `ρ_ref`** — separate lane; this note only identifies the cumulant-generator form given that input state
- **Downstream Wilson-coefficient extraction from `W[J]`** — separate lane
- **Promotion of any downstream row** — auditor-owned

## Verification

Run:

```bash
python3 scripts/pwc_commuting_cgf_framework_native_2026_06_17.py
```

Expected result:

```text
PWC commuting-source cumulant-generator finite proof
TOTAL: PASS=14 FAIL=0
```

## Citation-graph note

This is a bounded_theorem candidate at narrow-theorem granularity. The
load-bearing proof is finite-dimensional and source-native over a
supplied finite-region state and commuting finite-source family.
Textbook probability / statistical-mechanics references are parallel
provenance for the same object.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_K1_DERIVATION_FROM_MINIMALITY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing the prior k=1 ratification with derivation)
- `LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing LSP-projective ratification with derivation)
- `PRR_LOCAL_DERIVATION_FROM_JAYNES_MAX_ENTROPY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing PRR-local ratification path with derivation)
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_FREE_CUMULANT_ROUTE_NARROW_NOTE_2026-05-21.md` — contextual pointer; uses classical and free cumulant frameworks in a different bridge attempt
- `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md` — contextual pointer; uses cumulants in the gauge-plaquette mixed-cumulant context

## What this file is not

- Not a new framework rule
- Not a derivation of `rho_ref`, noncommuting ordering, or source-production dynamics
- Not a Pattern-L selection from a family of admissible cumulant generators on the stated commuting-source scope
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
