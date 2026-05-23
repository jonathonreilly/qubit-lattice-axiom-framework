# PWC Derivation from the Standard Cumulant Generating Functional (Narrow)

**Date:** 2026-05-22
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Identify the framework's pre-record connected generating functional `W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` as the standard finite-source cumulant generating functional applied to a given pre-record reference state, rather than ratifying it as a framework rule. The clean theorem scope is commuting bounded source families, with the noncommuting quantum ordering convention left explicit.

## Why this note exists

The framework uses the pre-record connected generating functional `W[J]` whose `n`-th `J`-derivatives at `J = 0` are the connected `n`-point cumulants of observables under `ρ_ref`. The earlier ratification path (bundled in the closed PR #1658) proposed adding the explicit definition `W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` as a load-bearing framework rule alongside k=1 / LSP-projective / PRR-local.

Following the same audit-feedback that drove the k=1, LSP-projective, and PRR-local derivation refactors, this note **identifies** the framework's `W[J]` as the standard cumulant generating functional of probability theory — i.e., as **which** standard mathematical object `W` already is — rather than ratifying its form as a framework rule.

## Honest scope

This note **does not**:
- Add a new framework rule
- Re-derive the cumulant generating functional formalism from scratch (cited as standard probability / statistical mechanics)
- Claim Pattern-L-style "selection from a family" for the commuting finite-source cumulant generator
- Derive or audit the choice of `ρ_ref`; this note takes the finite-region state as the input to the cumulant generator
- Resolve noncommuting operator-ordering, Wick / Schwinger rotation, time-ordering conventions, or path-integral measures (separate lanes)

This note **does**:
- Cite the standard probability-theory definition of the cumulant generating functional
- Show that the framework's `W[J]` form is the standard cumulant generating functional applied to `ρ_ref` with a commuting `J`-coupled observable source
- Record that `W[0] = 0` and `∂^n W / ∂J^n |_{J=0}` reproduces the connected `n`-point function of the commuting source observables, which is the standard cumulant content

## Position: identification, not selection

The selection / identification distinction matters for Pattern-L circularity discipline:

- **Selection (Pattern-L-circular).** "Among a family of candidate functionals `{W_α[J]}`, the framework selects `W_0[J]`." This requires axiom-level input picking out which member of the family the framework uses, and risks circularity if downstream content already constrains the choice.
- **Identification (the current case).** "On the commuting-source scope, there is one standard mathematical object — the cumulant generating functional — and the framework's `W` is that object." No family to select from; the standard definition is what `W` *is*.

For commuting bounded sources, `W[J] := log Tr(ρ · e^{-J})` is the standard cumulant generating functional in classical probability theory applied to the joint spectral measure. For noncommuting quantum sources, the same expression is a standard Kubo/statistical-mechanics source convention, but it does not eliminate the separate ordering-convention lane.

The pre-record subscript reflects which state `ρ_ref` is used; this note does not derive that state. The cumulant-generating-functional form itself is not a framework choice on the commuting-source scope.

## Claim

For a given finite-region pre-record reference state `ρ_ref` on the one-qubit operator algebra over the `Z^3` spatial substrate, with `J` an observable source coupled to bounded self-adjoint operators on `A_Λ`:

**Theorem (narrow commuting-source form).** For a finite family of mutually commuting bounded self-adjoint source observables on `A_Λ`, the framework's pre-record connected generating functional is

```text
W[J]  :=  log Tr(ρ_ref · e^{-J})  -  log Tr(ρ_ref)                       (PWC)
```

This is **the standard cumulant generating functional of probability theory** applied to the joint spectral measure induced by `ρ_ref` and the commuting source family. Its `n`-th `J`-derivatives at `J = 0` reproduce the connected `n`-point functions of those commuting source observables under `ρ_ref`. Since `Tr(ρ_ref) = 1` for normalized `ρ_ref`, the second term vanishes and `W[J] = log Tr(ρ_ref · e^{-J})` directly. The `- log Tr(ρ_ref)` term is recorded for the general case where `ρ_ref` may not yet be normalized (e.g., in intermediate constructions).

## Proof

### Step 1 — Standard cumulant generating functional definition

In classical probability theory (Feller *An Introduction to Probability Theory and Its Applications* Vol. II Ch. VII §5; Billingsley *Probability and Measure* §21), the **cumulant generating functional** of a real-valued random variable `X` under a probability measure `μ` is

```text
K(t)  :=  log E_μ[e^{tX}]  =  log ∫ e^{tx} dμ(x).                        (P1)
```

Its `n`-th derivative at `t = 0` gives the `n`-th cumulant `κ_n` of `X` under `μ`:

```text
κ_n  =  d^n K / dt^n |_{t=0}.                                            (P2)
```

In particular:
- `K(0) = log E[1] = log 1 = 0` (normalization)
- `K'(0) = E[X]` (mean)
- `K''(0) = E[X²] - E[X]²` (variance)
- Higher derivatives give higher cumulants

For a *family* of source-coupled observables `{X_α}` with source vector `J = (J_α)`, the **multivariate cumulant generating functional** is

```text
K(J)  :=  log E_μ[e^{Σ_α J_α X_α}]                                       (P3)
```

with mixed `J`-derivatives at `J = 0` giving multivariate cumulants (connected `n`-point functions of the `X_α`).

### Step 2 — Quantum extension

For a quantum state `ρ` and a mutually commuting bounded self-adjoint source family `J = Σ_α J_α O_α`, the same functional is obtained by applying (P3) to the joint spectral measure. In quantum statistical mechanics, the source-coupled expression is commonly written (Kubo, Toda, Hashitsume *Statistical Physics II* Ch. 1; Jaksic-Pillet *Course on Statistical Mechanics* §2):

```text
W[J]  :=  log Tr(ρ · e^{-J})  -  log Tr(ρ).                              (Q1)
```

The sign convention `e^{-J}` matches the partition-function convention `Z = Tr(e^{-βH})` of quantum statistical mechanics; the framework follows this convention.

**Sign bookkeeping (made explicit).** With the `e^{-J}` convention, the order-`n` `J`-derivative at `J = 0` returns `(-1)^n` times the connected `n`-point cumulant `κ_n`: i.e. `κ_n = (-1)^n · ∂^n W / ∂J^n |_{J=0}`. Equivalently, define the framework's connected `n`-point function as the cumulant of `+J·O` and absorb the sign by reading derivatives of `W[-J]`. Either way the `(-1)^n` is a fixed bookkeeping factor of the chosen `e^{-J}` source convention, not an ambiguity: even-order cumulants (variance and up) come out with the textbook sign; odd-order ones carry the explicit `(-1)`. The list below states the raw `δW/δJ` derivatives (carrying the `e^{-J}` sign); the cumulants are these times `(-1)^n`.

The functional `W[J]` satisfies:

- `W[0] = log Tr(ρ) - log Tr(ρ) = 0` (normalization)
- `δW / δJ_α |_{J=0} = - Tr(ρ O_α)` (one-point function; the `-` is the `n=1` factor `(-1)^1` of the `e^{-J}` convention, so `κ_1 = Tr(ρ O_α)`)
- `δ²W / δJ_α δJ_β |_{J=0} = Tr(ρ O_α O_β) - Tr(ρ O_α) Tr(ρ O_β)` for commuting `[O_α, O_β] = 0`; this is `(-1)^2 = +1` times the connected two-point function (covariance), i.e. the textbook sign
- Higher functional derivatives give `(-1)^n` times the connected `n`-point functions

For commuting observable families (`[O_α, O_β] = 0` for all `α, β`), the multivariate quantum cumulant generating functional reduces to the classical one applied to the joint spectral measure of the `{O_α}`. For non-commuting families, ordering issues require care; (Q1) is a standard Kubo/source convention, not a proof that all ordering choices are physically equivalent.

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

For commuting bounded source families, the framework's `W[J] = log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` is the standard cumulant generating functional of probability theory / quantum statistical mechanics applied to the given pre-record reference state `ρ_ref`. Its content (connected `n`-point functions as `J`-derivatives at `J = 0`) is the standard cumulant content. No framework-rule selection is required on that scope: the form **is** the standard mathematical object. ∎

## Cited authorities (one hop)

Load-bearing markdown-link upstream:

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the qubit-per-site axiom and `Z^3` spatial substrate on which `ρ_ref` lives

Named non-derivation imports (standard textbook content):

- **Cumulant generating functional** in classical probability (Feller Vol. II Ch. VII §5; Billingsley §21; standard MGF / cumulant theory)
- **Quantum cumulant generating functional** in quantum statistical mechanics (Kubo-Toda-Hashitsume *Statistical Physics II* Ch. 1; Jaksic-Pillet course; standard finite-temperature source-coupled formalism)
- **Joint spectral measure** for commuting bounded observable families (standard)

Plain-text contextual pointer (not load-bearing dep):

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — one framework route for deriving the reference state later used as the `ρ_ref` input

## What this derivation supplies

The same `W[J] = log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)` form, now stated as the **standard cumulant generating functional of probability theory applied to `ρ_ref`** on commuting source families, not a load-bearing framework rule. The "selection from a family" structure that would have made it a framework rule does not exist on that narrow scope.

## What this does NOT close

- **Wick / Schwinger rotation between Euclidean and Lorentzian sources** — separate lane
- **Time-ordering and operator-ordering conventions for non-commuting `J`** — standard but separate lane
- **Path-integral measure / Wilson lattice measure compatibility with `ρ_ref`** — separate lane (the Radon-Nikodym question flagged in the tracial-route note)
- **Choice or derivation of `ρ_ref`** — separate lane; this note only identifies the cumulant-generator form given that input state
- **Downstream Wilson-coefficient extraction from `W[J]`** — separate lane
- **Promotion of any downstream row** — auditor-owned

## Citation-graph note

This is a bounded_theorem candidate at narrow-theorem granularity. Standard probability / statistical mechanics applied to the framework's specific pre-record reference state to identify the framework's `W[J]` as the standard cumulant generating functional on commuting finite-source families.

Plain-text pointer references (NOT load-bearing deps):

- `QUBIT_K1_DERIVATION_FROM_MINIMALITY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing the prior k=1 ratification with derivation)
- `LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing LSP-projective ratification with derivation)
- `PRR_LOCAL_DERIVATION_FROM_JAYNES_MAX_ENTROPY_NARROW_THEOREM_NOTE_2026-05-22.md` — companion derivation in the same lane (replacing PRR-local ratification path with derivation)
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_FREE_CUMULANT_ROUTE_NARROW_NOTE_2026-05-21.md` — contextual pointer; uses classical and free cumulant frameworks in a different bridge attempt
- `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md` — contextual pointer; uses cumulants in the gauge-plaquette mixed-cumulant context

## What this file is not

- Not a new framework rule
- Not a re-derivation of the cumulant generating functional formalism (cited as standard)
- Not a Pattern-L selection from a family of admissible cumulant generators on the stated commuting-source scope
- Not a promotion of any downstream row (auditor-owned)
- Not a numerical-prediction change
