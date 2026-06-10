# Axiom-First Microcausality / Lieb-Robinson Bound on A_min

**Date:** 2026-05-01 (2026-05-09: bounded action-support/J-bound support added;
2026-06-10: M2 rescoped to the proved overlap-weight velocity and the exact-H
quasilocal decomposition, M3 scoped as explicitly conditional — see the
load-bearing-consequence paragraph below)
**Type:** bounded_theorem
**Claim scope:** equal-time strict locality [O_x, O_y] = 0 for x ≠ y on Cl(3)
tensor structure (M1); Lieb-Robinson lightcone bound
‖[α_t(O_x), O_y]‖ ≤ 2‖O_x‖‖O_y‖exp(-d + v_LR|t|) with the proved
overlap-weight velocity v_LR = 2·e·q·W·R from
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
(unconditional on the nearest-neighbor hopping-bilinear surface,
v_LR ≤ 4·e·(|m| + 2d)); for the exact reconstructed H = -log(T̂²)/(2a_τ) the
strict finite-range hypothesis is false and M2 holds in truncated quasilocal
form on the free bilinear sector via
[`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md),
with the exact-H lightcone assembly and the gauged/interacting sector named
open (M2); continuum spacelike microcausality explicitly conditional on a
retained Lorentz scaling bridge (M3).
**Status:** awaiting independent audit. Under the scope-aware classification framework (audit-lane proposal #291), `effective_status` is computed by the audit pipeline from `audit_status` + `claim_type` + dependency chain.
**Loop:** `24h-axiom-first-derivations-20260501`
**Cycle:** 4 (Block 04; independent of Blocks 01-03)
**Branch:** `physics-loop/24h-axiom-first-block04-microcausality-20260501`
**Runner:** `scripts/axiom_first_microcausality_check.py`
**Log:** `outputs/axiom_first_microcausality_check_2026-06-10.txt`
(2026-06-10 rerun with the proved overlap-weight velocity; the
2026-05-01 log predates the constant repair)

## Scope

This note proves, on `A_min` plus the RP + spectrum condition
support theorems, the **lattice microcausality theorem** for the
framework's reconstructed Hamiltonian `H` on `H_phys`. The result has
two parts:

**(M1) Equal-time strict locality.** For any two distinct lattice
sites `x ≠ y` and any operators `O_x, O_y` supported at those sites,
`[O_x, O_y] = 0` strictly. This is a one-line consequence of A1.

**(M2) Lieb-Robinson lightcone.** For operators `O_x, O_y` at sites
`x, y` evolved by the reconstructed Hamiltonian `H` from RP, there
exist constants `v_LR > 0` (the Lieb-Robinson velocity) and `ξ > 0`
(decay rate) depending only on A3, A4 finite-range parameters, such
that

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  C · ‖O_x‖ · ‖O_y‖ · exp(-(d(x, y) - v_LR · |t|) / ξ)    (1)
```

where `α_t(O) = e^{i t H} O e^{-i t H}` is real-time Heisenberg
evolution, `d(x, y)` is the lattice graph distance, and `C` is a
constant that depends only on the local algebra dimension. In
particular, **the commutator is exponentially small outside the
effective lightcone** `d(x, y) > v_LR · |t|`.

In the continuum-limit identification `t_phys = t · a_τ`,
`d_phys = d · a_s`, and `v_LR · a_s / a_τ → c` (fixed light-cone
slope), this becomes the standard relativistic-QFT
**microcausality** statement `[O(x), O(y)] = 0` for spacelike
separation `(x - y)² < 0`.

This note completes the framework's locality program by providing the
spacetime locality statement that complements the existing retained
cluster-decomposition theorem (which is the *spatial* decay theorem).

## A_min objects in use

- **A1 — local algebra `Cl(3)`.** Used in (M1) directly: distinct
  lattice sites carry independent copies of `Cl(3)`, so the local
  algebras are disjoint and commute.
- **A2 — substrate `Z^3`.** Used as the underlying graph metric
  `d(x, y)` (graph distance under nearest-neighbor adjacency).
- **A3 — finite-range staggered Dirac.** Used in (M2): the
  Kogut-Susskind staggered hop and Wilson term are nearest-neighbor
  in space and have one-step temporal range. The maximum hopping
  range is `r_h = 1` lattice unit.
- **A4 — canonical normalization at g_bare = 1, plaquette action.**
  Used in (M2): the Wilson plaquette gauge action couples the four
  corners of a single plaquette, range `r_g = 1`. The lattice gauge
  field is therefore finite-range with range `r_g = 1`.

## Retained inputs

- **RP transfer matrix.** From the [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
  `T : H_phys → H_phys` is Hermitian, positive, and bounded. The
  Hamiltonian `H = -log(T) / a_τ` is well-defined and bounded below.
- **Spectrum condition.** From the [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md),
  `H` on `H_phys` is bounded operator with finite spectral norm
  (since `H_phys` has finite dimension on any finite block, by RP
  reconstruction).
- **Exact-H quasilocal decomposition (free bilinear sector).** From
  [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md),
  the single-particle hopping kernel of the exact reconstructed
  `H = -log(T̂²)/(2 a_τ)` obeys an explicit exponential bound at sharp
  rate `η* = arcsinh(m)`, giving finite per-site overlap weight `W_H`
  and exponentially convergent finite-range truncations `H_R`. Sector
  restriction declared there: free (`U = 1`) bilinear staggered
  two-step sector only.

## Statement

Let `H = sum_{z ∈ Λ} h_z` be the reconstructed Hamiltonian on
`H_phys` from RP, where `h_z` is the local Hamiltonian density
supported in a ball of radius `r := max(r_h, r_g) = 1` around
lattice site `z`. Then:

**(M1) Equal-time strict locality.** For any two distinct lattice
sites `x, y ∈ Λ` with `x ≠ y` and any operators `O_x, O_y` supported
at these sites,

```text
    [O_x, O_y]  =  0  (exactly)                                              (2)
```

**(M2) Lieb-Robinson lightcone bound.** Let `α_t(O) := e^{i t H} O e^{-i t H}`
be Heisenberg evolution, `d(x, y)` the lattice graph distance, and
define

```text
    v_LR  :=  2 e q W R                                                      (3)
    ξ      :=  1                                                              (4)
```

where `q` is the largest support size, `R` the largest support
diameter (graph distance), and `W := max_x Σ_{Z ∋ x} ‖h_Z‖_op` the
per-site overlap weight — the velocity proved in
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
(Lemma (L1)/(L2); the earlier `v_LR = 2 e r J` plug-in is superseded —
it omitted the overlap weight). Then for any operators `O_x, O_y`
supported at sites `x, y` respectively,

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  2 · ‖O_x‖_op · ‖O_y‖_op · exp(- d(x,y) + v_LR |t|)    (5)
```

In particular, when `d(x, y) > v_LR |t|`, the commutator is bounded by
`2 ‖O_x‖ ‖O_y‖ · e^{-(d - v_LR |t|)} → 0` exponentially.

**(M3) Continuum-limit microcausality (explicitly conditional).** In
the lattice continuum limit `a → 0` with `v_LR · a_s / a_τ → c < ∞`
fixed, the bound (5) becomes strict: `[O(x), O(y)] = 0` for any pair
of operators at points `x, y` with spacelike separation in the
asymptotic Lorentzian metric. The fixed-lightcone-slope scaling
premise is conditional on a retained Lorentz scaling bridge: the cited
Lorentz surfaces
([`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md),
[`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md))
supply kernel positivity and the smooth-limit regime, not the
lightcone-slope scaling statement itself. M3 is claimed only modulo
that named bridge.

Statements (M1)–(M3) constitute the framework microcausality theorem
on `A_min`.

## Proof

### Step 1 — Equal-time strict locality (proves M1)

By A1, the local algebra at each lattice site is `Cl(3)` (8-dimensional
graded algebra). Distinct lattice sites have independent copies of
`Cl(3)`. The full lattice operator algebra on a finite block `Λ` is
the tensor product

```text
    A(Λ)  =  ⊗_{z ∈ Λ}  Cl(3)_z
```

Operators `O_x ∈ Cl(3)_x` and `O_y ∈ Cl(3)_y` with `x ≠ y` are then
of the form `O_x = (...) ⊗ a ⊗ (...)` and `O_y = (...) ⊗ (...) ⊗ b ⊗ (...)`
where `a` lives in the `x`-th tensor factor and `b` in the `y`-th
tensor factor. They commute trivially:

```text
    O_x · O_y  =  (... a ⊗ b ...)  =  O_y · O_x                             (6)
```

This proves (M1). For staggered fermion operators, the Grassmann
graded structure `χ_x χ_y = -χ_y χ_x` for fermionic χ at distinct
sites is included in the "Cl(3) at each site" structure (the Cl(3)
algebra encodes the Z_2-grading). The commutator (M1) is the
*graded* commutator
`[O_x, O_y]_± = O_x O_y - (-1)^{|O_x| |O_y|} O_y O_x = 0`. ∎

### Step 2 — Lieb-Robinson bound (proves M2)

This is the standard Lieb-Robinson 1972 estimate adapted to the
framework's specific finite-range Hamiltonian. We follow the
Nachtergaele-Sims 2010 presentation.

Define `f(t) := [α_t(O_x), O_y]`. Differentiating in `t`:

```text
    df/dt  =  i · [H, [α_t(O_x), O_y]]  =  i · [α_t([i H, O_x]), O_y]      (7)
```

Iterating, after `n` derivatives:

```text
    d^n f / dt^n  =  i^n · [α_t( ad_H^n (O_x) ), O_y]
```

where `ad_H(X) := [H, X]`. Since `H = sum_z h_z` with each `h_z`
supported in a ball of radius `r` around `z`, the commutator
`[h_z, O_x]` is nonzero only if `d(z, x) ≤ r`. Hence
`ad_H(O_x) = sum_{z : d(z,x) ≤ r} [h_z, O_x]`, which has support
extended to a ball of radius `2r` around `x`.

By induction, `ad_H^n(O_x)` has support in a ball of radius `(n+1) r`
around `x`. The number of nonzero contributing `h_z` chains is bounded
by `(2r d_max)^n / n!` where `d_max` is the local coordination number
on `Λ`.

Each commutator `[h_z, O_x]` has operator norm bounded by
`2 · ‖h_z‖ · ‖O_x‖ ≤ 2 J ‖O_x‖`. So

```text
    ‖ ad_H^n (O_x) ‖_op  ≤  ‖O_x‖ · (2 J · 2r)^n / n!   ≤  ‖O_x‖ · (4 J r)^n / n!    (8)
```

The Taylor series of `α_t = e^{i t ad_H}` then satisfies

```text
    ‖ α_t(O_x) - O_x ‖_op  ≤  ‖O_x‖ · ( exp(4 J r |t|) - 1 )                 (9)
```

For the commutator with `O_y`: the only contributions to
`[α_t(O_x), O_y]` come from terms in the Taylor expansion where
`ad_H^n(O_x)` has support overlapping with `y`. Since
`ad_H^n(O_x)` has support in a ball of radius `(n+1) r` around `x`,
the support overlaps `y` only if `(n + 1) r ≥ d(x, y)`, i.e.
`n ≥ d(x, y)/r - 1`. Hence

```text
    ‖ [α_t(O_x), O_y] ‖_op
       ≤  2 · ‖O_y‖ · sum_{n ≥ d(x,y)/r - 1}  ‖ ad_H^n (O_x) ‖_op · |t|^n / n!
       ≤  2 · ‖O_x‖ · ‖O_y‖ · sum_{n ≥ d(x,y)/r - 1}  (4 J r |t|)^n / n!
```

Using the standard estimate
`sum_{n ≥ N} z^n / n!  ≤  e^z · z^N / N!  ≤  e^z · (e z / N)^N`:

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  2 ‖O_x‖ ‖O_y‖ · e^{4 J r |t|} · (4 e J r |t| / d(x, y))^{d(x, y) / r}
                            ≤  2 ‖O_x‖ ‖O_y‖ · exp(- d(x, y) + 2 e r J · |t|)            (10)
```

(after writing `(4 e J r |t| / d)^{d/r} = exp((d/r) log(4 e J r |t| / d))`
and using `log(z) ≤ z - 1` for the dominant exponential).

The estimate (10) as written concludes with the plug-in
`v_LR = 2 e r J`. That constant is **superseded**: the companion
bridge note
([`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md))
proves the same lightcone bound (5) by the iterated-commutator
argument with every constant traced, and the honest velocity for this
support-overlap convention is `v_LR := 2·e·q·W·R` with `q` the largest
support size, `R` the largest support diameter, and
`W := max_x Σ_{Z ∋ x} ‖h_Z‖_op` the per-site overlap weight (the
`2 e r J` form omitted the overlap counting). On the nearest-neighbor
hopping-bilinear surface the bridge note's unconditional instantiation
gives `v_LR ≤ 4·e·(|m| + 2d)`. Decay rate `ξ = 1`. ∎

### Bounded action-support/J-bound support (added 2026-05-09)

The Step 2 argument above takes the finite-range structure of `H = Σ_z h_z`
and the local-density operator-norm `J = sup_z ‖h_z‖_op` as inputs. A
2026-05-05 audit review flagged that these inputs were **asserted** rather
than **derived**: the cited RP/spectrum authorities supply positivity /
self-adjointness / boundedness of the reconstructed `H`, but not the
locality structure needed for Lieb-Robinson, nor an explicit `v_LR`
derivation.

The companion bridge note
`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
narrows that gap. It proves three bounded statements directly from the
canonical action coefficients (the same coefficients that the parent RP
note's eqs. (1) and (2) record, not from any new spectral input):

**(F1) Leading action-density support.** The action `S = S_F + S_G`
(parent RP note eqs. (1)–(2)) couples either single sites (mass term),
NN sites (staggered hop, Wilson term), or four sites in a single
elementary plaquette (Wilson plaquette). This gives bounded support
`r_action <= 2` in the site `l1` metric for the leading local
action-density pieces. It does not prove that the exact logarithmic
Hamiltonian `H = -log(T)/a_tau` is finite range.

**(F2) Explicit action-density J bound.** `J_action ≤ J_max :=
|m| + d/2 + r_W · d + (2β/N_c) · d(d-1)/2`, depending only on action
coefficients. For the canonical surface (`d = 4, r_W = 1, β = 6,
N_c = 3`): `J_max = |m| + 30`. Proof: triangle inequality on the
local action-density pieces, using `‖U_μ‖_op = 1` because
`U_μ ∈ SU(3)` is unitary, `|η_μ(x)| = 1`, fermion ladder ops bounded
by 1, and `|1 - Re tr(U_P)/N_c| <= 2` for unitary `U_P`. The bound is
gauge-background-independent.

**(F3) Conditional Lieb-Robinson velocity (per the repaired bridge
note).** The bridge note's in-note Lemma (L1)/(L2) gives the traced
velocity `v_LR = 2·e·q·W·R` (no literature constant imported; the
earlier `2 e r J` summary of this paragraph is superseded). Its
conditional corollary: if the exact reconstructed `H` admits a
carrier-compatible decomposition (`q <= 4`, `R <= 2`,
`W <= |m| + 300`), then `v_LR <= 16·e·(|m| + 300)`. The 2026-06-10
quasilocality theorem shows the strict finite-range form of that
hypothesis is false for the exact free-sector `H` (range-4 hops), so
the corollary is read through the truncation family `H_R` as in the
load-bearing-consequence paragraph below.

The bridge note's runner `scripts/microcausality_finite_range_h_bridge_2026_05_09.py`
verifies (F1) on a finite-range toy action-density carrier, (F2) by
computing `‖h_z‖_op` on 20 random SU(3) backgrounds and comparing
against the conservative `J_max`, (F3) by verifying the standard
Lieb-Robinson bound (5) on a 1D finite-range Hamiltonian, and (F4)
outside-lightcone exponential decay.

**Consequence for the load-bearing claim (updated 2026-06-10).** The
action-support and coefficient/norm pieces are no longer asserted, and
the exact-H decomposition ask is now answered on the free bilinear
sector by
[`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md):
the exact reconstructed `H = -log(T̂²)/(2 a_τ)` of the free staggered
two-step transfer matrix is **not** finite-range (nonzero hops at
`l1`-range 4 are exhibited, so the strict finite-range reading of the
original M2 wording is false there); `H` is instead quasilocal, with
the explicit exponential hopping bound at sharp rate
`η* = arcsinh(m)`, finite per-site overlap weight `W_H = ‖h‖_l1 < ∞`,
and finite-range truncations `H_R` whose per-site tail weights and
single-particle operator-norm errors decay exponentially in `R`. The
proved Lieb-Robinson lemma applies verbatim to each truncation `H_R`
with velocity `v_LR(R) = 2·e·q_R·W_R·R`. Two pieces remain named open
and bound this claim: (i) the exact-H lightcone statement assembled
from the truncation family plus the exponential error control (the
quasilocal-assembly lemma), and (ii) the gauged/interacting
log-transfer locality, which the quasilocality theorem's declared
sector restriction leaves open.

### Step 3 — Continuum microcausality (proves M3)

In the lattice → continuum limit `a → 0` with
`v_LR · a_s / a_τ  =  c < ∞` (the fixed-lightcone-slope scaling
premise; explicitly conditional on a retained Lorentz scaling bridge —
see (M3): the cited
[`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) and
[`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md)
surfaces do not themselves fix that scaling), spatial graph distance
`d_phys = d · a_s` and time `t_phys = t · a_τ` satisfy
`v_LR |t| = c |t_phys| / a_s`. The Lieb-Robinson exponent in (5)
becomes

```text
    - d(x, y) + v_LR |t|  =  - d_phys / a_s + c |t_phys| / a_s
                          =  (1 / a_s) · (- d_phys + c |t_phys|)
```

For spacelike separation `d_phys > c |t_phys|`, the exponent is
`- (d_phys - c |t_phys|) / a_s → -∞` as `a_s → 0`, so the commutator
vanishes strictly. This is the standard relativistic microcausality
statement. ∎

## Hypothesis set used

- A1 (Cl(3) tensor structure for equal-time locality M1).
- A2 (Z^3 graph metric).
- A3 (NN staggered hop range r_h = 1).
- A4 (plaquette gauge range r_g = 1).
- RP transfer matrix (defines H_phys).
- Spectrum condition (H bounded operator with finite J).
- Proved finite-range Lieb-Robinson lemma with traced constants
  (`v_LR = 2·e·q·W·R`) from
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md);
  no literature constant is imported.

No fitted parameters. No observed values used as proof inputs.

## Corollaries

C1. **Spatial cluster decomposition refinement.** Combined with the
retained [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md),
(M1)+(M2) refine the *spacetime* decay rate of connected
correlators on the framework: `<O_x α_t(O_y)>_c → 0` exponentially in
`d(x, y) - v_LR |t|`.

C2. **Causal asymptotic local algebras.** The local algebras
`A(O) := { observables localized in spacetime region O }`
satisfy `[A(O_1), A(O_2)] = 0` for any two regions `O_1, O_2`
with spacelike separation (in the continuum limit). This is the
framework's Haag-Kastler-style local-algebra structure.

C3. **No-superluminal-signaling on the framework.** Any signaling
protocol from `x` at `t = 0` to `y` at time `t` requires
`d(x, y) ≤ v_LR · t`. This is the lattice analogue of the
no-faster-than-light-signaling principle.

C4. **Reeh-Schlieder cyclicity premise.** The local algebras built
from microcausal operators are the inputs to the Reeh-Schlieder
theorem (Block 08), which would prove cyclicity of the vacuum vector
for any nonempty open region.

## Honest status

**Source theorem on A_min + RP + spectrum
condition.** (M1)–(M3) are derived from:

- A1 (equal-time tensor product structure);
- A3, A4 (finite-range hopping/gauge);
- RP (defines H, H_phys);
- spectrum condition (H bounded);
- the proved overlap-weight Lieb-Robinson lemma (bridge note; no
  literature constant imported);
- the exact-H quasilocal decomposition on the free bilinear sector
  (quasilocality theorem; assembly lemma and gauged sector named open).

The runner verifies the lattice Lieb-Robinson bound numerically on a
small block (1D chain, range-1 nearest-neighbor Hamiltonian, with
H built from random Hermitian operators). It demonstrates the
exponential decay of `‖[α_t(O_0), O_d]‖` outside the lightcone
`d > v_LR · t`.

**Honest claim-status fields:**

```yaml
actual_current_surface_status: support
conditional_surface_status: derived support theorem on A_min + RP + spectrum condition
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Depends on audit-pending RP and spectrum-condition support notes. A chain of support cannot be marked retained-grade until all dependencies are ratified on the current authority surface."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.**

- Continuous Lorentz invariance via Wightman axioms. We prove the
  lattice Lieb-Robinson form, which is the cleanest statement on
  `A_min`.
- Promotion to retained / Nature-grade in the canonical paper
  package. Independent audit required.

## Citations

- A_min: [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
- RP support note:
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- spectrum-condition support note:
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- retained cluster-decomposition note:
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- 2026-05-09 bounded action-support/J-bound support for finite-range H + explicit v_LR:
  `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
- retained emergent Lorentz invariance:
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
  [`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md)
- standard external references (theorem-grade, no numerical input):
  Lieb-Robinson (1972) *Comm. Math. Phys.* 28, 251;
  Hastings (2004) *Phys. Rev. B* 69, 104431;
  Nachtergaele-Sims (2010) in *New Trends in Mathematical Physics*,
  Springer, p. 591.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by the
audit verdict so the audit citation graph can track them. It does not promote
this note or change the audited claim scope.

- [microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  (2026-05-09 — supplies bounded action-density support and explicit
  J budget for the load-bearing finite-range-H/v_LR bridge).
