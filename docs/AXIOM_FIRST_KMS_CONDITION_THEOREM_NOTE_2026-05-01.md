# Axiom-First KMS Condition for the Reconstructed Gibbs State

**Date:** 2026-05-01
**Type:** positive_theorem
**Claim scope:** the finite-temperature Gibbs state on the RP-reconstructed two-step transfer-matrix Hilbert space H_phys satisfies the KMS condition (K1)-(K4) at inverse temperature β_th = L_τ·a_τ for even raw Euclidean time length L_τ; equivalently, with N_τ := L_τ/2 blocked time steps and T := T_hat^2, the periodic-Euclidean path integral on (Z/L_τ Z) × Z^3 equals the trace of T^{N_τ} and the strip identity F(t + iβ_th) = G(t) holds for all bounded operators.
**Status:** awaiting independent audit. Under the scope-aware classification framework (audit-lane proposal #291), `effective_status` is computed by the audit pipeline.
**Loop:** `24h-axiom-first-derivations-20260501`
**Cycle:** 1 (Block 1)
**Branch:** `physics-loop/24h-axiom-first-block01-kms-20260501`
**Runner:** `scripts/axiom_first_kms_condition_check.py`
**Log:** `outputs/axiom_first_kms_condition_check_2026-05-01.txt`
**Artifact sync:** 2026-06-17 regenerated the referenced output log from
the current two-step runner so the source packet no longer carries the
legacy single-step `T^{L_tau}` wording. This does not assert an audit
verdict or promote the row.

## Scope

This note records, on the current framework baseline
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md))
plus the cited RP and spectrum-condition support surfaces, a finite-block
proof that the finite-temperature Gibbs state reconstructed from the
reflection-positivity (RP) two-step transfer matrix on a periodic
Euclidean-time block satisfies the **Kubo-Martin-Schwinger (KMS)
condition** at inverse temperature `β_th = L_τ · a_τ` when the raw
temporal length `L_τ` is even. The positive transfer object is
`T := T_hat^2`; it advances one blocked time interval
`a_blk := 2 a_τ`, so the number of blocked transfer factors is
`N_τ := L_τ / 2`. The companion artifacts are the
RP support note
([`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md))
and the spectrum-condition support note
([`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)).

After independent audit, the package's thermal-state language can quote a
source KMS theorem on the framework baseline plus RP/spectrum support
instead of treating the
periodic-Euclidean ↔ thermal-state correspondence as a background
convention. The result also opens the bridge to Hawking
temperature, Unruh temperature, Stefan-Boltzmann, and the Generalized
Second Law (each of which uses KMS at a different framework horizon
or vacuum state).

To avoid notational collision with the gauge-coupling convention
`β = 2 N_c / g_bare²`, we use `β_th` throughout for the thermal inverse
temperature.

## Framework and Support Inputs

- **Quantum / one-qubit operator algebra.** Used only through the
  finite physical Hilbert space `H_phys` reconstructed by the two-step
  RP sector from the local fermion/operator algebra.
- **Lattice / `Z^3` spatial slice.** Used only as the spatial part of
  the finite block `Λ = (Z/L_τ Z) × (Z/L_s Z)^d_s` with even raw
  Euclidean time length `L_τ` and periodic boundary in time and space.
  Periodicity in time is what makes the blocked transfer-matrix trace
  `Z = tr_{H_phys}(T^{N_τ})` finite-temperature.
- **Record.** No additional readout rule is imported here. The theorem
  uses the finite scalar trace/readout supplied by the reconstructed
  finite-dimensional Hilbert-space packet.
- **APBC finite-temperature convention.** For fermion observables we use
  the canonical anti-periodic-in-time, periodic-in-space boundary
  convention as part of the finite-temperature setup carried by the RP
  support surface; it is not promoted here as a new axiom.
- **Gauge normalization.** Positivity and normalization of the transfer
  object are consumed through the RP/spectrum support notes. This KMS
  row does not derive `g_bare`, `β = 6`, or a gauge-action normalization.

## Support-note inputs

- **RP transfer matrix.** From the RP support note (R3),
  `T := T_hat^2 : H_phys → H_phys` is Hermitian, positive, and has
  operator norm `‖T‖ ≤ 1` on the canonical surface. It advances two
  raw lattice time steps, i.e. one blocked interval `a_blk := 2 a_τ`.
- **Spectrum condition.** From the spectrum-condition support
  note (SC1, SC2), `H := -(1/(2 a_τ)) log(T / M_T)` is self-adjoint
  and `H ≥ 0` on `H_phys`, with `M_T = ‖T‖_{op}`. Equivalently
  `T = M_T · e^{-2 a_τ H}` with `H ≥ 0`.
- **Finite-dim physical Hilbert space.** From RP (R2), `H_phys` has
  finite dimension on any finite block `Λ`. This makes all traces
  finite and all operator products bounded.

## Admitted-context inputs

- **Wick rotation:** standard convention. The reconstruction (R1)–(R4)
  of the RP note already pays for the Euclidean ↔ Lorentzian bridge
  by defining the analytic continuation of `T^n` to `e^{-itH}` for
  `t > 0` via `T^n ↔ e^{-itH}` with `t = -i n (2 a_τ)`.
- **Cyclic-trace property** of finite-dimensional traces:
  `tr(AB) = tr(BA)` for any operators on a finite-dim Hilbert space.
  This is a basic linear-algebra fact, not an import.

## Statement

Let `Λ = (Z/L_τ Z) × (Z/L_s Z)^d_s` be the finite block with periodic
boundary in both time and space and even raw time length `L_τ`. Set
`N_τ := L_τ / 2`. Let `T := T_hat^2 : H_phys → H_phys` be the
RP-reconstructed two-step transfer matrix, and let
`H := -(1/(2 a_τ)) log(T / M_T)` be the reconstructed Hamiltonian
(which is `≥ 0` after the constant `(1/(2 a_τ)) log M_T` shift; we
absorb this shift into the zero of energy, equivalent to the standard
convention `M_T = 1`).

Define the **finite-temperature Gibbs state** at inverse temperature
`β_th := L_τ · a_τ = N_τ · (2 a_τ)` by

```text
    < O >_{β_th}  :=  (1 / Z_{β_th}) · tr_{H_phys}( e^{-β_th H} · O )      (1)
    Z_{β_th}      :=  tr_{H_phys}( e^{-β_th H} )  =  tr_{H_phys}( T^{N_τ} )  (2)
```

for any operator `O` on `H_phys`. Define Heisenberg-picture time
evolution by

```text
    α_t(A)  :=  e^{i t H} · A · e^{-i t H}                                  (3)
```

for any `A` on `H_phys` and any `t ∈ R`.

Then on the framework baseline plus the RP + spectrum-condition surface:

**(K1) Path-integral ↔ Gibbs-state correspondence.** The Euclidean
path-integral on `Λ` with periodic-boundary fields and APBC fermions
equals the trace `Z = tr_{H_phys}(T^{N_τ})`, hence the path-integral
expectation `<O>_{path}` of any operator `O` localized in a blocked
Euclidean time slice equals the Gibbs expectation `<O>_{β_th}` of the
corresponding `H_phys`-operator at inverse temperature
`β_th = L_τ · a_τ`.

**(K2) KMS condition.** For any two bounded operators `A, B` on
`H_phys` and any real `t ∈ R`, the Gibbs expectation values

```text
    F_{A,B}(t)  :=  < A · α_t(B) >_{β_th}                                   (4a)
    G_{A,B}(t)  :=  < α_t(B) · A >_{β_th}                                   (4b)
```

are related by the **KMS condition**: `F_{A,B}` extends to an entire
analytic function on `C` (because `H` is bounded on finite-dim `H_phys`,
α_z is entire-analytic in `z`), and on the strip-endpoint `Im z = β_th`
it equals `G_{A,B}` shifted to the real axis:

```text
    F_{A,B}( t + i β_th )  =  G_{A,B}( t )                                  (5)
```

Equivalently, in `G`-form:

```text
    G_{A,B}( t - i β_th )  =  F_{A,B}( t )                                  (5')
```

i.e. the analytic continuation of `G_{A,B}` from `t ∈ R` down to
`t - i β_th` (the lower edge of the strip `Im z ∈ [-β_th, 0]`) equals
the real-axis values of `F_{A,B}`.

**(K3) Finite-strip analyticity.** The functions

```text
    F_{A,B}(z) = (1/Z) tr( e^{-β_th H} · A · e^{i z H} · B · e^{-i z H} )
    G_{A,B}(z) = (1/Z) tr( e^{-β_th H} · e^{i z H} · B · e^{-i z H} · A )
```

are entire-analytic on `C` because `H` is bounded on finite-dim
`H_phys`. On the closed strip `S_F = {z : 0 ≤ Im z ≤ β_th}` the
function `F_{A,B}` satisfies the bound

```text
    sup_{z ∈ S_F}  | F_{A,B}(z) |  ≤  ‖A‖ · ‖B‖ · exp( β_th · σ(H) )       (6)
```

where `σ(H) = E_max - E_min` is the energy spread on `H_phys`. The
analogous strip for `G_{A,B}` is `S_G = {z : -β_th ≤ Im z ≤ 0}` with
the same form of bound. The boundary values of `F_{A,B}` are
`F_{A,B}(t) = < A α_t(B) >_{β_th}` on the real axis and
`F_{A,B}(t + i β_th) = G_{A,B}(t) = < α_t(B) A >_{β_th}` on the
upper edge of the strip — this is the KMS identity (5).

**(K4) Equilibrium uniqueness.** The Gibbs state is the unique state
on the finite-dim algebra `B(H_phys)` that satisfies (K2) at inverse
temperature `β_th` and is invariant under `α_t`. The proof is the
matrix-unit calculation in Step 5 below; Bratteli-Robinson is cited
only as the standard continuum/operator-algebra reference.

Statements (K1)–(K4) constitute the KMS theorem on the framework baseline
plus the RP + spectrum-condition surface.

## Proof

The proof is a finite-dimensional linear-algebra calculation once
(R3) of the RP note has supplied the Hermitian positive transfer
matrix `T` on the finite-dim `H_phys`. We avoid any continuum or
infinite-dim manipulation.

### Step 1 — Path integral equals transfer-matrix trace

The path integral on `Λ` with periodic boundary in time and APBC
for fermions is the finite transfer-matrix product supplied by the RP
note. Because the temporal boundary is periodic, the product closes into
a finite trace:

```text
    Z  =  ∫_periodic  Dχ̄ Dχ DU  exp(-S)                                    (7)
       =  tr_{H_phys}( T^{N_τ} )                                             (8)
```

The equality (7)→(8) is the same Osterwalder–Seiler / Sharatchandra
factorisation that Steps 1–3 of the RP note used to establish (R1).
Periodicity in `t` is what closes the trace; without it (open
boundary) one would get a state-vector overlap rather than a trace.

For an operator `O_k` localized on a blocked Euclidean time slice `k`,
let `Ô` be the corresponding reference-block operator on `H_phys` after
the RP reconstruction. The blocked transfer-matrix insertion has the
finite form

```text
    Num_k(O)  =  tr_{H_phys}( T^{N_τ-k} · Ô · T^k )                         (9)
```

where `0 <= k <= N_τ` and all powers are ordinary finite matrix powers.
The case `k = 0` is the reference block. For any `k`, cyclicity gives

```text
    Num_k(O)
      = tr( T^{N_τ-k} · Ô · T^k )
      = tr( T^k · T^{N_τ-k} · Ô )
      = tr( T^{N_τ} · Ô ).                                                (10)
```

Thus the blocked-slice expectation is independent of the block label and
is exactly

```text
    < O >_{path}
      = (1/Z) · tr( T^{N_τ} · Ô )
      = (1/Z) · tr( e^{-β_th H} · Ô ),                                    (11)
```

because `T = e^{-2 a_τ H}` and `β_th = N_τ (2 a_τ) = L_τ a_τ`. No
inverse transfer matrix, external KMS lemma, or continuum bookkeeping
is used in this step. This proves (K1) for the finite-block blocked-slice observables
needed by the downstream thermal-state rows. Multi-time ordered
correlators keep their ordered product of transported insertions; the
KMS strip identity for arbitrary bounded `A,B` is proved directly in
Step 3.

### Step 2 — Setup of KMS strip

Define `α_t(A) := e^{i t H} A e^{-i t H}` for `t ∈ R` and `A` on the
finite-dim `H_phys`. Since `H = H†` on `H_phys` (from spectrum
condition SC1), the time evolution `α_t` is a one-parameter group of
*-automorphisms of `B(H_phys)`. Since `H_phys` is finite-dim, `H` is
bounded, so `α_t` extends to an entire-analytic family `α_z` for
`z ∈ C`:

```text
    α_z(A)  :=  e^{i z H} · A · e^{-i z H}                                  (12)
```

This is the matrix exponential, well-defined for all `z ∈ C` because
`H` is a bounded matrix.

### Step 3 — KMS identity by cyclicity

We prove `F_{A,B}(t + i β_th) = G_{A,B}(t)` directly. Compute
`F_{A,B}(t + i β_th)` in the trace form:

```text
    F_{A,B}(t + i β_th)
       :=  < A · α_{t + i β_th}(B) >_{β_th}
        =  (1/Z) · tr( e^{-β_th H} · A · e^{i(t + i β_th) H} · B · e^{-i(t + i β_th) H} )    (13)
```

Expand the analytic time evolution at the shifted argument. Since
`e^{a H} · e^{b H} = e^{(a + b) H}` for any complex `a, b` (factors of
`H` commute), we have `e^{i(t + i β_th) H} = e^{i t H} · e^{-β_th H}`
and `e^{-i(t + i β_th) H} = e^{-i t H} · e^{β_th H}`. Substituting:

```text
    F_{A,B}(t + i β_th)
       =  (1/Z) · tr( e^{-β_th H} · A · e^{i t H} · e^{-β_th H} · B · e^{-i t H} · e^{β_th H} )    (14)
```

Apply cyclic-trace: pull the rightmost factor `e^{β_th H}` around to
the front. The cyclic move `tr(X1 ... Xk · e^{β_th H}) = tr(e^{β_th H} · X1 ... Xk)`
gives

```text
    F_{A,B}(t + i β_th)
       =  (1/Z) · tr( e^{β_th H} · e^{-β_th H} · A · e^{i t H} · e^{-β_th H} · B · e^{-i t H} )
       =  (1/Z) · tr( A · e^{i t H} · e^{-β_th H} · B · e^{-i t H} )                                (15)
```

using `e^{β_th H} · e^{-β_th H} = I`. Now since `e^{i t H}` commutes
with `e^{-β_th H}` (both functions of the same `H`), we can pull
`e^{-β_th H}` left of `e^{i t H}`:

```text
    F_{A,B}(t + i β_th)
       =  (1/Z) · tr( A · e^{-β_th H} · e^{i t H} · B · e^{-i t H} )
       =  (1/Z) · tr( e^{-β_th H} · e^{i t H} · B · e^{-i t H} · A )                                (16)
```

where the last equality is again cyclic-trace bringing `A` to the
right end. By definition,
`(e^{i t H} · B · e^{-i t H}) = α_t(B)` (real-axis Heisenberg
evolution), so (16) reads

```text
    F_{A,B}(t + i β_th)  =  (1/Z) · tr( e^{-β_th H} · α_t(B) · A )
                        =  < α_t(B) · A >_{β_th}
                        =:  G_{A,B}(t)                                                              (17)
```

Equation (17) is the **KMS condition (K2)**. ∎

To verify in eigenbasis form (used by the runner for numerical
stability): in the eigenbasis of `H` with eigenvalues `E_n`,

```text
    F_{A,B}(z)  =  (1/Z) · Σ_{n,m}  e^{-β_th E_n} · A_{nm} · e^{i z (E_m - E_n)} · B_{mn}
    G_{A,B}(z)  =  (1/Z) · Σ_{n,m}  e^{-β_th E_n} · e^{i z (E_n - E_m)} · B_{nm} · A_{mn}
```

At `z = t + i β_th`, the `F` factor becomes
`e^{-β_th E_n} · e^{i t (E_m - E_n)} · e^{-β_th(E_m - E_n)} = e^{-β_th E_m} · e^{i t (E_m - E_n)}`,
which after relabeling `n ↔ m` matches the `G(t)` summand exactly:
`e^{-β_th E_m} · e^{i t (E_m - E_n)} · A_{nm} B_{mn} = e^{-β_th E_n'} · e^{i t (E_n' - E_m')} · B_{n'm'} A_{m'n'}`
with `n' = m`, `m' = n`. This is the same identity (17) at the level
of matrix elements.

### Step 4 — Strip analyticity (K3)

For finite-dim `H` with eigenvalues `0 = E_0 ≤ E_1 ≤ ... ≤ E_{d-1}`,
the matrix function `z ↦ e^{i z H}` is entire-analytic in `z`. Hence

```text
    z  ↦  α_z(B)  :=  e^{i z H} · B · e^{-i z H}
```

is an entire-analytic operator-valued function, and the Gibbs
expectations `F_{A,B}(z), G_{A,B}(z)` are entire-analytic in `z` on
`C`.

For the strip bound (6), express `F_{A,B}` in the eigenbasis of `H`:

```text
    F_{A,B}(z)  =  (1/Z) · Σ_{n,m}  e^{-β_th E_n} · A_{nm} · e^{i z (E_m - E_n)} · B_{mn}
```

For `z = t + i s` with `s ∈ [0, β_th]`,
`|e^{i z (E_m - E_n)}| = e^{-s (E_m - E_n)} ≤ e^{β_th · σ(H)}`
where `σ(H) := E_max - E_min` is the energy spread on `H_phys`.
Hence

```text
    |F_{A,B}(t + i s)|
       ≤  (1/Z) · e^{β_th σ(H)} · Σ_{n,m}  e^{-β_th E_n} · |A_{nm}| · |B_{mn}|
       ≤  (1/Z) · e^{β_th σ(H)} · Σ_n  e^{-β_th E_n} · ‖A‖_op · ‖B‖_op
       =  ‖A‖_op · ‖B‖_op · e^{β_th σ(H)}
```

establishing the strip bound (6). Note this bound is `‖A‖ · ‖B‖`
times the *thermal-spread factor* `exp(β_th σ(H))`; in any free
QFT in infinite volume, σ(H) → ∞ and the bound is replaced by
finite-band cutoff arguments. On the framework's finite block `Λ`,
σ(H) is finite by RP-reconstruction so the bound is finite. ∎

### Step 5 — Equilibrium uniqueness (K4)

Let `ω(X) = tr(ρ X)` be any state on `B(H_phys)` that is invariant under
`α_t` and satisfies the endpoint KMS identity. Diagonalize
`H = Σ_r E_r P_r`, with finite-rank spectral projectors `P_r`.
Invariance gives `ρ = Σ_r P_r ρ P_r`; all cross-energy blocks vanish.

Within one degenerate energy block, `α_t` is the identity. KMS then says
`tr(ρ A B) = tr(ρ B A)` for every pair of matrix units `A,B` inside that
block. The only matrices whose trace pairing is cyclic against all
matrix units in a full matrix algebra are scalar multiples of the
identity, so `P_r ρ P_r = c_r P_r`.

For two energy blocks `r,s`, choose unit vectors `u in P_r H_phys`,
`v in P_s H_phys`, and matrix units `A = |u><v|`,
`B = |v><u|`. The endpoint identity at `t=0` gives

```text
    c_s  =  exp( β_th (E_r - E_s) ) · c_r.                                (18)
```

Hence `c_r exp(β_th E_r)` is constant across all `r`, and normalization
`tr ρ = 1` fixes

```text
    ρ  =  e^{-β_th H} / tr(e^{-β_th H}).                                  (19)
```

Therefore the Gibbs state is the unique finite-dimensional invariant
KMS state. This is the framework-native finite proof of (K4);
Bratteli-Robinson Vol. II, Theorem 5.3.30 is only the parallel
operator-algebra reference.
∎

This completes the proof of (K1)–(K4) on the framework baseline plus the
stated RP/spectrum finite-block support surfaces.

## Hypothesis set used

- Lattice, Quantum, and Record only in the narrow current-baseline sense
  stated in [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).
- RP transfer-matrix structure (R3 of the RP note).
- Spectrum condition (SC1, SC2) for `H ≥ 0`.
- APBC finite-temperature boundary convention and Wick rotation as already
  paid for by the RP reconstruction.
- Cyclic-trace identity for finite matrices (basic linear algebra).

No fitted parameters. No observed values used as proof inputs. No
imports beyond the explicit Wick-rotation convention already used by
the RP reconstruction. External KMS theorems are citations, not proof
inputs for this finite-block result.

## Corollaries (downstream tools)

C1. **Periodic-Euclidean ↔ thermal correspondence is a theorem on the
framework baseline plus RP/spectrum support.** Any package note that quotes "the path integral with
period `L_τ` in Euclidean time describes a thermal state at
temperature `T = 1/(L_τ a_τ)`" can cite this note instead of
treating it as a convention.

C2. **Hawking temperature bridge.** The framework's discrete GR
action on `S^3 × R` (UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE) plus
a Killing horizon admits a Wick-rotated regular Euclidean section
with period `2π/κ` (the standard Hawking-Gibbons argument). Combining
that period with (K1)–(K2) yields `T_H = κ/(2π)` as a corollary on
the framework GR action surface. This is the load-bearing input for
the Hawking temperature block (Block 2 of this campaign).

C3. **Unruh temperature bridge.** The framework's Lorentz kernel
(LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE) admits Rindler wedge boost
generators. The Bisognano-Wichmann-style argument gives a periodic
Rindler-time identification, and (K1)–(K2) yields `T_U = a/(2π)`.
This is the load-bearing input for the Unruh temperature block.

C4. **Stefan-Boltzmann bridge.** The Gibbs photon partition function
on framework photon spectrum (gauge-field KK tower from
VECTOR_GAUGE_FIELD_KK_TOWER_THEOREM_NOTE) plus the KMS-derived
thermal occupation `n(E) = 1/(e^{β_th E} - 1)` (Planck distribution
follows from KMS for harmonic oscillators) gives the
Stefan-Boltzmann law. This is the load-bearing input for the
Stefan-Boltzmann block.

## Honest status

**Source theorem.** (K1)–(K4) are proved on the current framework
baseline plus the RP and spectrum-condition support surfaces by Steps
1–5. The proof leans entirely on:

- the two-step RP transfer matrix `T := T_hat^2` supplied by the RP
  support note;
- the spectrum-condition Hamiltonian `H ≥ 0` supplied by the companion
  spectrum-condition support note;
- the cyclic-trace property of finite-dim traces (basic linear
  algebra, including the native slice-insertion and uniqueness
  matrix-unit calculations above);
- the Wick-rotation / Euclidean-Lorentzian convention already paid
  for by the RP reconstruction.

The runner exhibits the structural content (generic finite
`H_phys` construction, explicit KMS-strip evaluation,
finite-temperature trace identity, native slice-insertion cyclicity,
and matrix-unit uniqueness equations) and cross-checks numerical
equality of `F_{A,B}(t + i β_th)` and `G_{A,B}(t)` on a small grid.

**Honest claim-status fields:**

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: derived support theorem on the framework baseline + RP + spectrum condition
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "effective status requires independent audit of this row and retained-grade dependency closure for the cited RP/spectrum support surfaces."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.**

- Continuum KMS / Tomita-Takesaki / modular automorphism. We prove
  the finite-block lattice analogue supported by the framework baseline
  plus RP/spectrum reconstruction.
- Promotion to retained / Nature-grade in the canonical paper
  package. That requires independent audit of this repaired row and
  dependency closure through the audit pipeline.

## Citations

- framework baseline: [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- RP support note: [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- spectrum-condition support note: [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- companion cluster-decomposition note: [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- companion CPT note: [`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md)
- standard external proofs (parallel references only; the proof above
  supplies the finite framework calculation and imports no numerical
  input):
  Kubo (1957) *J. Phys. Soc. Jpn.* 12, 570;
  Martin–Schwinger (1959) *Phys. Rev.* 115, 1342;
  Haag–Hugenholtz–Winnink (1967) *Comm. Math. Phys.* 5, 215;
  Bratteli–Robinson (1981) *Operator Algebras and Quantum Statistical
  Mechanics*, Vol. II, ch. 5.3.
