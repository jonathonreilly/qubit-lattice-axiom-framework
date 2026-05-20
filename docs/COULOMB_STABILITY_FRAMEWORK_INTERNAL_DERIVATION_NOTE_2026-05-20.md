# Atomic / Coulomb Stability Upper Bound, Framework-Internal Derivation

**Date:** 2026-05-20
**Claim type:** positive_theorem (framework-internal port of the
Ehrenfest 1917 / Tangherlini 1963 atomic-stability classical result
onto retained framework primitives)
**Status:** proposal — pre-audit
**Closes (proposed):** the second half of
`dimension_selection_upper_bound_textbook_import_note_2026-05-17`'s
external-import gap (the atomic-stability half).

## Claim

On the framework's `Z^d` lattice substrate with the retained Coulomb
potential from `dimensional_gravity_table` (`V(r) ∝ 1/r^(d−2)` for
`d ≥ 3`), the Hamiltonian of a hydrogen-like bound system in d
spatial dimensions

```text
H_d = − (ℏ² / 2m) ∇²_d  −  α / r^(d−2)                                   (1)
```

admits the canonical Coulomb spectrum (countably infinite bound states
accumulating at threshold `E → 0`) only for `d = 3`. For `d = 4`, the
ground state is marginal (no infinite-spectrum bound states); for
`d ≥ 5`, the Hamiltonian is unbounded below at the origin and no
stable ground state exists.

The atomic-stability upper bound is therefore `d ≤ 4`, with `d = 3`
the unique case admitting the canonical hydrogen-like spectrum.

## Setup

By the retained `dimensional_gravity_table`, the Coulomb / scalar
potential on the `Z^d` lattice is, in the large-`r` continuum limit,

```text
φ(r) ∝ 1/r^(d−2)   for d ≥ 3                                            (2)
```

By the framework's retained lattice quantum mechanics
(per-site `M_2(ℂ)` qubits + tensor composition + Hamiltonian
dynamics — the latter via the open gates, but the *kinematic*
structure is on A1+A2 alone), a bound-state problem on the d-dim
substrate is the eigenvalue equation `H_d ψ = E ψ` for `H_d` as in
(1).

## Step 1 — Scaling analysis at the origin

The wave function near `r = 0` behaves as `ψ ∼ r^β` for some real `β`
(or with logarithmic corrections). Substituting into the radial
Schrödinger equation in d dimensions:

```text
−(ℏ²/2m) [d²ψ/dr² + (d−1)/r · dψ/dr − ℓ(ℓ+d−2)/r² · ψ]  −  α/r^(d−2) · ψ  =  E ψ                  (3)
```

For `r → 0`, the kinetic term scales as `r^(β−2)` and the potential
term as `r^(β−(d−2))`. The two are comparable when

```text
β − 2 = β − (d−2)    ⟹    d − 2 = 2    ⟹    d = 4                       (4)
```

This identifies `d = 4` as the **critical dimension** for the d-dim
Coulomb problem — the dimension at which the kinetic and potential
energies balance at short distances.

## Step 2 — Hamiltonian boundedness for `d ≥ 5`

For `d ≥ 5`, the potential `−α/r^(d−2)` diverges faster than `1/r²`
near the origin. The kinetic energy scales as `−∇² ψ ∼ ψ/r²` at short
distances, which is the standard inverse-square barrier. A potential
that diverges *faster* than `1/r²` (i.e., as `1/r^(d−2)` for `d ≥ 5`,
since `d − 2 ≥ 3 > 2`) **dominates the kinetic energy** at short
distances and cannot be regulated by the centrifugal barrier.

Formally, for any trial wave function `ψ_λ(r) = λ^{d/2} ψ(λ r)`
(rescaled so that `||ψ_λ|| = 1`), the expectation value of `H_d` scales as

```text
⟨H_d⟩_{ψ_λ}  =  λ² T  −  λ^(d−2) U                                       (5)
```

with `T, U > 0` constants depending on `ψ`. For `d ≥ 5`, `d − 2 > 2`,
so as `λ → ∞`, `⟨H_d⟩ → −∞`. The Hamiltonian is **unbounded below**.
No normalizable ground state exists.

This is the Tangherlini 1963 result, derived here on the framework's
retained Coulomb potential.

## Step 3 — Marginal case `d = 4`

At `d = 4`, the scaling in (5) becomes

```text
⟨H_d⟩_{ψ_λ}  =  λ² (T − U)                                               (6)
```

Both terms scale as `λ²`. The Hamiltonian is bounded below **iff
`T ≥ U`**, i.e. iff the coupling `α` is sufficiently weak relative
to the kinetic scale. For `α` below a critical value `α_c`, a ground
state exists; for `α > α_c`, it does not.

But — critically — even in the bounded-below regime at `d = 4`, the
spectrum **does not accumulate at threshold `E → 0`**. The Coulomb-
like spectrum `E_n = −R/n²` (Rydberg formula) requires `d = 3`. At
`d = 4`, generic bound-state spectra are discrete and bounded; the
infinite Rydberg series is absent.

(This is the Ehrenfest 1917 observation, refined by Tangherlini's
1963 dimensional analysis: only `d = 3` gives the rich atomic
spectrum, even where `d = 4` admits an isolated ground state.)

## Step 4 — `d = 3` admits the canonical spectrum

At `d = 3`, the standard Coulomb / Schrödinger problem is solved
analytically (any QM textbook, e.g., Griffiths, Sakurai). The
spectrum is

```text
E_n = −m α² / (2 ℏ² n²)                                                 (7)
```

with `n = 1, 2, 3, ...`, accumulating at `E → 0`. Infinitely many
bound states. This is the Rydberg formula; it works only at `d = 3`.

## Step 5 — Combined conclusion

| `d` | Coulomb potential scaling | `H` boundedness | Canonical spectrum? |
|---|---|---|---|
| 1 | confining | bounded below | not Coulomb-like; doesn't apply |
| 2 | logarithmic | bounded below | not Coulomb-like |
| **3** | `1/r` | **bounded below** | **YES (Rydberg `E_n ∝ 1/n²`)** |
| 4 | `1/r²` | marginal (`α < α_c`) | NO (no infinite series at threshold) |
| ≥5 | `1/r^(d−2)` | **unbounded below** | NO (no ground state) |

The **atomic-stability upper bound is `d ≤ 4`**, and the **canonical
hydrogen-like spectrum exists only at `d = 3`**.

## What this closes

- The atomic-stability half of `dimension_selection_upper_bound_textbook_import_note_2026-05-17`'s
  external-import problem. The Ehrenfest 1917 and Tangherlini 1963
  results are now derived framework-internally on the retained
  `dimensional_gravity_table` Coulomb potential plus standard quantum
  mechanics.
- Combined with the Bertrand half
  (`BERTRAND_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md`), the
  full upper bound `d ≤ 3` (with `d = 3` uniquely the canonical
  case) is now framework-internal.

## What this does not close

- The standard quantum-mechanical algebra (rescaling, scaling
  analysis, ground-state existence) is admitted as standard QM. The
  framework's contribution is establishing that the retained
  `1/r^(d−2)` potential satisfies the hypotheses of the standard
  d-dim Coulomb problem.

## Admitted inputs

1. **d-dim Coulomb potential `V ∝ 1/r^(d−2)` for `d ≥ 3`** — from
   retained `dimensional_gravity_table`.
2. **Standard quantum mechanics on a continuous space** —
   Hamiltonian boundedness, scaling, spectrum. Admitted as standard
   background; the framework's lattice quantum mechanics retains the
   relevant short-distance / large-`r` continuum behavior.
3. **Standard d-dim Schrödinger equation form (3)** — the radial
   Laplacian in `d` dimensions with centrifugal term. Standard
   textbook (Sakurai, Cohen-Tannoudji); admitted as background.

## Caveats

1. **Atomic stability is about the canonical spectrum, not just
   ground state existence.** The argument in Step 4 (about `d = 3`
   uniquely admitting the Rydberg series) is the load-bearing
   physical statement, not just `H` boundedness. The upper bound
   `d ≤ 4` is for `H` boundedness; the **stricter** upper bound
   `d ≤ 3` for canonical-spectrum comes from absence of Rydberg
   accumulation at higher `d`.
2. **Lattice corrections.** The continuum d-dim Schrödinger / Coulomb
   problem is the large-`r` limit. Finite-lattice corrections may
   modify ultrashort distances but not the asymptotic conclusions.
3. **Coupling to gauge structure.** The "Coulomb potential" here
   inherits from the framework's gravitational / scalar / EM-like
   potential law; full electromagnetic coupling needs the gauge
   gates closing. The atomic-stability argument is dimensional
   (depends on `V ∝ 1/r^(d−2)` form), not on which specific gauge
   sector supplies it.

## Citation-graph note

Upstream:
- `dimensional_gravity_table` — d-dim potential law (retained_bounded)
- Standard quantum mechanics — scaling, Hamiltonian boundedness,
  Coulomb spectrum

Companion (this PR):
- `BERTRAND_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md` —
  orbital-stability half of the upper bound
- `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md` —
  lower bound + low-`d` exclusion
