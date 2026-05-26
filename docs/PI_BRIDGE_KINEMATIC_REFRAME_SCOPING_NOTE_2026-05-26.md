# π-Bridge Kinematic Reframe: `3δ = Q` Identifies an Azimuthal Radian with a Radial Koide Ratio — Scoping of a Kinematic Attack

**Date:** 2026-05-26
**Claim type:** scoping (not a theorem, not a closure)
**Status authority:** independent audit lane only. This is a scoping note that opens a previously
unpursued kinematic attack on the radian-bridge primitive `P`. It adds no new axiom, derives no new
quantity, and sets no audit status. Author claim: framing + survey + roadmap. **Audit required
before any effective status.**
**Primary runner:** [`scripts/frontier_pi_bridge_kinematic_reframe_scoping_discriminator.py`](../scripts/frontier_pi_bridge_kinematic_reframe_scoping_discriminator.py)
**Authority role:** opens strategic option 3 of `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp`
(pivot to a dimensionless-only readout law) as the live frontier identified by the dynamics-lane
milestone-3 result — the bridge is **kinematic**, not dynamical, and a re-expression of the Brannen
observable in dimensionless `Q` may dissolve the radian unit entirely. **Strictly scoping; the actual
re-expression attempts (K1-K4 below) are out of scope here.**

## The π-bridge in its cleanest current form

From [`DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md`](DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md):
the spontaneous-CP stationarity of the C₃-clock + CP flavon potential `V(δ) = A cos(3δ) + B cos(6δ)`
gives

```
cos(3δ) = -A/(4B)   ⟺   3δ = 2/3   ⟺   3δ = Q   ⟺   δ = Q/N_gen ,
```

where **`Q = 2/3` is the retained Koide cone** (`w_axis = w_perp = 1/2`) and `N_gen = 3`. The bridge
in its sharpest form is therefore:

> **The C₃-azimuthal radian `3δ` equals the retained radial Koide dimensionless ratio `Q = 2/3`.**

This is the π-bridge stripped of its earlier "rational-radian" obfuscation. A *radian* (3δ) is being
*identified* with a *dimensionless ratio* (Q). By Lindemann-Weierstrass, no Q-rational combination
of retained rationals can produce `2π` (the unit that turns a dimensionless number into a radian),
so the identification cannot be derived from the retained rational inventory alone (six prior no-go
routes; see Cross-references). What is needed is a **kinematic identification of `Q` with `3δ`** by
some retained kinematic structure.

## The kinematic reframe (the M3 contribution)

The dynamics-lane milestone-3 result ([`DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md`](DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md))
shifted the residual diagnosis from "dynamics" to "kinematics":

> The flavor *value* is **counting** (the retained variance `V(3)`), not a dynamical fixed point.
> What is genuinely open is purely **kinematic**: the **radian-bridge license** — why a
> counting-variance enters a cosine as a radian (the missing, transcendental **factor of π**).

The 2026-05-10 expanded-inventory note explicitly listed (and did not pursue) strategic option 3:

> *Pivot to a dimensionless-only readout law. Reformulate the Brannen circulant to take
> dimensionless inputs directly, bypassing the radian unit.*

This scoping note opens that option as the live frontier consistent with M3's kinematic reframe.

## The kinematic-reformulation hypothesis (`KH`)

**`KH`** — The Brannen-Koide circulant observable

```
m_k² ∝ cos(δ + 2πk/3)        (Brannen form; δ = Q/N_gen)
```

is a **re-expression** of an underlying observable whose canonical form takes the dimensionless
Koide ratio `Q` (and the C₃-equivariant index `k`) as inputs *without passing through any literal
radian*. The literal identity `δ = Q/N_gen = 2/9 rad` is then either:

- a **coordinate** label on a C₃-azimuthal parameterization, with the actual observable depending
  on `Q` *as a dimensionless ratio*, OR
- a **Taylor-coefficient** appearance, where `Q` enters as a dimensionless cumulant of a discrete
  C₃ distribution and the literal `δ` radian only emerges in a perturbative re-summation.

If `KH` is correct, the radian-bridge primitive `P` dissolves: the observable never required a
radian, only the chosen parameterization did. **`KH` is currently unproven — it is the scoping
hypothesis this note opens.**

## Why kinematic, not dynamical

The M3 result closes the **dynamical** routes (R1-R5): no fixed-point / mode-locking / group-
theoretic mechanism on retained substrate produces the literal radian. R6 (canonical modular/KMS
phase, `q·π`) and Probes 20, 24 (Pancharatnam-Berry on C₃ qubits) close the **geometric-phase**
routes. The six closing-input candidates (a)/(b)/(c) of
[`KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md`](KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md)
§4 are **new structural admissions** (a new lattice propagator quantum, a new Wilson holonomy
class, a new Z₃-orbit quantization) and none are retained.

What remains: a **kinematic re-expression** that does not invoke a new dynamical principle and does
not add a new admission. This is `KH`. It is the only route currently consistent with M3's
"kinematic, not dynamical" reframe and the strategic option flagged 16 days earlier in the
expanded-inventory note.

## Candidate kinematic structures to host the re-expression

The retained kinematic substrate eligible to carry the re-expression:

### K1 — Cl(3) projector triple product

A1 fixes `M₂(ℂ) = Cl(3,0)` at each site, with `i = e₁e₂e₃` the pseudoscalar. The three generation
states `|e⟩, |μ⟩, |τ⟩` realize as a triple of Cl(3) projectors `P₁, P₂, P₃`. The mass observable
may be expressible as

```
m_k² = Tr(P_k · D[Q]),    D[Q] = a(Q)·𝟙 + b(Q)·(C + C†) ,
```

with `C` the C₃ clock and `(a, b)` dimensionless functions of `Q`. The eigenvalues of `D` give the
Brannen-circulant `cos(2πk/3 + δ)` form via C₃ representation theory; whether `δ` enters as a
literal radian or only via `Q` *inside* `(a, b)` is the testable point.

### K2 — C₃-equivariant cumulant expansion

The retained Bernoulli family `M(N) = (N-1)/N`, `V(N) = (N-1)/N²`, `V(N) = M(N)/N` is the
mean-variance pair of the discrete uniform distribution on `N` points. The lepton sqrt-mass triplet
is its C₃-realization. A cumulant expansion of the mass observable in `V(N)` would have:

- 0th cumulant (mean): trivial constant.
- 1st cumulant (variance `V(N)`): the dominant deformation away from the C₃-symmetric point.
- 2nd / higher cumulants: subleading.

The Brannen-Koide `cos(δ + 2πk/3) = -1/2 - (√3/2)·δ + (1/4)·δ² + O(δ³)` at `δ → 2/9` matches the
small-`δ` regime; if the underlying observable is a low-order cumulant series in `V(N)`, the
literal radian appearance is a Taylor-coefficient artifact.

### K3 — Determinantal C₃-circulant identity

For a 3×3 circulant `C` with first row `(c₀, c₁, c₂)`, eigenvalues are
`c₀ + c₁·ω^k + c₂·ω^{2k}` with `ω = e^{2πi/3}`. If the lepton mass operator is a circulant with
`Q`-dependent entries `c_j = f_j(Q)` (dimensionless functions of the Koide ratio), the eigenvalues
take the C₃-character cosines as *naturally-radian factors of `2π/3`* (already algebraic, `cos(2πk/3)
∈ {1, -1/2}`), and the only place `δ` enters is via `Q` *inside* the dimensionless `f_j(Q)`.

### K4 — Plancherel-Frobenius rational `2/d² = 2/9`

Probe 24 identifies `2/9` as the Plancherel-Frobenius rational `2/d²` at `d = 3` (irreducible
character of the regular Z₃ rep). In K3's parameterization, the natural appearance of this rational
is as a **coefficient** in `f_j(Q)` (e.g., the leading non-trivial Casimir-derived weight), never as
an angle. If K1-K3 reproduce the Brannen form with the literal `δ = Q/N_gen` emerging only via
re-expression, then `2/9` lives where it was always retained: in the Plancherel inventory.

## What the runner verifies (scoping-grade arithmetic)

The accompanying runner verifies:

1. The exact identity `3δ = Q = 2/3` (seed-note algebra).
2. `Q/N_gen = V(N_gen)` for `N_gen = 3` (`2/3 / 3 = 2/9 = V(3)`).
3. The Bernoulli family identity `V(N) = (N-1)/N² = M(N)/N` for `N = 3, 6`.
4. Lindemann-Weierstrass at the level of the bridge: `cos(2/3)` and `cos(2π/3)` are *different*
   numbers (cos(2/3) ≈ 0.7859, cos(2π/3) = -0.5); their difference is the bridge gap.
5. Retained-substrate eligibility check for K1-K4 (each kinematic structure has a cited retained
   provenance in the repo).
6. The six prior no-go routes against `P` are enumerated; none addressed the dimensionless-only
   readout reformulation.
7. Taylor expansion of `cos(δ + 2πk/3)` at the C₃-symmetric point `2πk/3` for small `δ = 2/9`:
   reports the first three coefficients (`cos(2πk/3)`, `-sin(2πk/3)`, `-cos(2πk/3)/2`) as a
   structural baseline the kinematic re-expression would need to reproduce.
8. Numerical sanity at the lepton match: `cos(4π/3 + 2/9)` reproduces the charged-lepton sqrt-mass
   triplet to `~7×10⁻⁶` (PDG appears only as a comparator, never as a derivation input).
9. Strategic-option-3 audit: the radian-bridge no-go inventory of 2026-05-10 explicitly listed but
   did not pursue the dimensionless-only readout pivot — this scoping note is the first opening of
   that option after the M3 kinematic reframe.

The runner does **not** attempt any of K1-K4. It verifies arithmetic only.

## What this note IS NOT

- **NOT** a derivation of `P`. `P` remains the open primitive.
- **NOT** a new axiom. No new structure is admitted.
- **NOT** a closure of the dynamics lane. The M3 bounded no-go stands unchanged.
- **NOT** an attack on the M3 result. The five algebraic-fixed-point routes (R1-R5) remain closed;
  this scoping note works inside their boundary, treating the residual as kinematic per M3.
- **NOT** an audit verdict. Branch-local scoping; audit required.

## Roadmap (out of scope for this note; each is a separate follow-up)

If a reviewer endorses this scoping, the natural next attempts are:

**(R1)** **Attack K1.** Express `m_k² = Tr(P_k · D[Q])` for `D[Q] = a(Q)·𝟙 + b(Q)·(C + C†)`,
determine whether `(a(Q), b(Q))` can be chosen as dimensionless `Q`-rationals that reproduce the
Brannen eigenvalues *without* the literal `δ = Q/3` appearing as a radian. **Falsification:** if
the only choice that reproduces the eigenvalues introduces a literal `cos(Q)` evaluated on a radian
argument, `KH` fails on K1.

**(R2)** **Attack K2.** Expand `cos(δ + 2πk/3)` as a Taylor series in `V(N) = 2/9`, identify
whether the series can be resummed as a *dimensionless* cumulant generating function of the
discrete-uniform C₃ distribution. **Falsification:** if any term in the resummation requires `2π`
as an explicit transcendental coefficient, `KH` fails on K2.

**(R3)** **Attack K3.** Diagonalize a circulant with `Q`-rational entries; verify whether the
character cosines `cos(2πk/3)` plus `Q`-dependent coefficients reproduce the Brannen form, with the
literal `δ` emerging only as a re-expression label. **Falsification:** if the diagonalization
requires injecting a radian as input, `KH` fails on K3.

**(R4)** **Adversarial review.** Independent hostile-reviewer pass on any (R1)-(R3) attempt:
confirm the kinematic re-expression does not smuggle in the radian via cumulant-to-operator or
circulant-to-Cl(3) bridges.

## Cross-references (plain-text, non-load-bearing)

- [`DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md`](DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md)
  — the bounded no-go this scoping addresses the residual of (the kinematic reframe).
- [`DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md`](DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md)
  — the `3δ = Q` identification this scoping reframes.
- [`RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md`](RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md)
  — six prior no-go routes; strategic option 3 (dimensionless-only readout) listed and unexplored
  until this scoping.
- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  — Type-A vs Type-B split; period-1 vs period-2π convention diagnosis.
- [`KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md`](KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md)
  — closing-input candidates (a)/(b)/(c); none retained.
- [`KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md`](KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md)
  — `φ_dim = 2/9` Plancherel-Frobenius rational (K4 substrate).
- [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
  — Brannen circulant eigenvalue formula (K3 substrate).
- [`CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md)
  — retained `V(3) = 2/9`, `V(6) = 5/36`, `V(N) = M(N)/N` (K2 substrate).
- `.claude/science/physics-loops/dynamics-lane/NO_GO_LEDGER.md` — N1-N8 discipline record for M3.

## Command

```bash
python3 scripts/frontier_pi_bridge_kinematic_reframe_scoping_discriminator.py
```

Expected: `PASS=N, FAIL=0` for the scoping-arithmetic checks. The runner does **not** attempt
closure of `P`; it verifies the framing only.
