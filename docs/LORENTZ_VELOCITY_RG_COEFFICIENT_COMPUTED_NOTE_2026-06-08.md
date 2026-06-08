# The One-Loop Velocity Anisotropy is Computed Nonzero and Not Internally (Taste) Protected: the Lorentz Naturalness Gap is a Computed, Regulator-Conditional Obstruction

**Date:** 2026-06-08
**Claim type:** no_go (computed, regulator-conditional obstruction)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.py`](../scripts/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.txt`](../logs/runner-cache/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.txt)

---

## Role

This note supplies the **named open input** of the two landed conditionals on the
emergent-Lorentz lane —
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
(#3121) and
[`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
(#3123) — namely the **one-loop velocity-RG coefficient, the spatial-only
power-divergent mixing, and the fixed-point anomalous dimension/suppression
sufficiency**. Two prior validations had shown that the **bare off-shell**
`δv = B − A` is an artifact (the naive `~0.31` is a doubler artifact; the Wilson
off-shell value is `~5×` sensitive to the regulator `r`) and left the
**gauge-invariant on-shell pole velocity** uncomputed, flagging the staggered
(taste) fermion as a possible protector.

This note **computes** it on the framework's stated native surface (spatial `Z³`
lattice + **continuous time**, SU(3) gauge at `β = 6` so `g² = 2N/β = 1`,
`α_s = g²/4π ≈ 0.080`). The result is **decisive but carefully conditional**:

1. the gauge-invariant **on-shell** velocity anisotropy is computed
   `δv ≈ (g²C₂/16π²)·c_v` with a **computed** `c_v ≈ 2` (O(1)), i.e.
   `δv|_UV(fund) ≈ 1.7×10⁻² ≈ 0.2 α_s` — a **finite** `~α_s/4π` Collins regeneration,
   loop-suppressed but **not** Planck-suppressed, and **nonzero** for every action
   tried (Wilson and staggered);
2. it is **not internally protected**: taste, the remnant `U(1)` chiral symmetry, and
   the per-site `Cl(3,0)` structure are **internal** symmetries that commute with (or
   grade-preserve) the spacetime `γ`-index and provably cannot relate a temporal to a
   spatial kinetic coefficient — only a **spacetime** (`t↔s`-crossing) symmetry can;
3. the speed-difference operator's anomalous dimension `γ = (C_F + T_F N_f)α_s =
   (4/3 + N_f/2)α_s ≈ 0.15–0.34` is **far below** the `γ_crit ≈ 0.54–1.32` needed for
   suppression; the residual **species-to-species** `δv(1 GeV) ≈ 10⁻⁸…10⁻⁴` exceeds
   the **tight** comparator bounds (`10⁻²⁰…10⁻²⁷`) by **12–21 orders** (robust to
   factor-2 in both `c_v` and `γ`);
4. **but the verdict is regulator-conditional.** It holds **if** the physical UV
   regulator is the framework's stated **asymmetric** surface (spatial `Z³` +
   continuous time), where the spacetime hypercubic group `B₄` is broken. The
   framework's **own** reflection-positivity / free-staggered-SO(4) / single-clock
   constructions are built on the **symmetric 4D Euclidean lattice** (continuous time
   as the `a_τ → 0` limit), where exact `B₄` symmetry **forbids** the marginal operator
   and `δv → 0`. So the `B₄` custodial route is **available-but-forgone, not absent**,
   and "continuous time breaks `B₄`" is a regulator **choice** / admitted dynamics
   gate, **not** a theorem.

**Net:** this **upgrades #3121/#3123 from an order-of-magnitude estimate to a computed
result** (the coefficient is computed nonzero), **closes the internal (taste)
protection escape**, and **sharpens the open problem to a single, named
regulator-commitment question** (asymmetric Hamiltonian surface → obstruction; the
`B₄`-symmetric-Euclidean limit → protected). Runner: **25 PASS / 0 FAIL**.

## The computation

### (0) The dim-6 lattice Lorentz-violating source
On the cubic `Z³` lattice the free dispersion is `E² = Σ_i sin²(k_i a)/a² = k² −
(a²/3)Σ_i k_i⁴ + O(a⁴)` (fermion; boson `a²/12`) — a CPT-even, parity-even
**dimension-6** operator, the retained leading lattice LV
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)).
This is what the Collins mechanism feeds into the **marginal** `δv`.

### (A) The bare off-shell `δv` is artifact-dominated (reproduced)
Naive fermions have `8` spatial doublers: the temporal `A` is log-divergent and the
spatial `B ≡ 0` by parity, so "`0.31`" is spurious; the Wilson off-shell `B − A`
varies `~5×` over `r ∈ [0.3, 2.0]` — a discretization artifact (runner Part A).

### (B) The gauge-invariant on-shell pole velocity — computed
At the Minkowski mass shell (`w_ext = i m₀, k → 0`) the gauge-dependent part of the
self-energy (`∝ S⁻¹`) vanishes by the **Nielsen identity**, so the pole velocity is
gauge-invariant. Computing `δv = Σ_s − Σ_t` (one-gluon/rainbow, spatial-`Z³` +
continuous-time loop):

- **the artifact is resolved**: the on-shell `r`-variation collapses from `~5×` to
  `<1×` (B1);
- **magnitude** `|δv| ≈ 0.011–0.016` per `g²C₂` `= O(0.1–0.2)α_s`, `c_v ≈ 2` (O(1));
  loop- but **not** Planck-suppressed (B2) — the value sits squarely inside the
  Groote–Shigemitsu anisotropic speed-of-light range and at the modest end of the
  Capitani lattice-`Z` spectrum (comparators);
- **sign** `v < 1` in this Euclidean extraction (B3) — **but** an independent
  real-time second-order-PT cross-check confirms the magnitude, nonzero-ness, and
  no-protection while **not** being able to certify the sign (its temporal renorm is
  contaminated by the lattice pair-creation threshold that the Euclidean method
  analytically avoids). The sign is therefore **not triangulated**; the verdict does
  not depend on it;
- **IR-finite** (B5): the velocity *difference* is stable as the gluon IR mass
  `λ → 0`;
- **honest residual** (B4): the rainbow-level value has a `~15%` gauge (`ξ`) spread;
  the **exact** O(1) `c_v` needs the full lattice vertex (Wilson/clover) and the
  **tadpole/seagull** diagram required by the lattice Ward identity.

### (C) No internal protection; the regulator question
On a **4D-symmetric** Euclidean lattice the temporal and spatial self-energy
coefficients are **equal** to `~10⁻¹⁵` (runner C1) — `δv = 0` by the `B₄` hypercubic
symmetry. The group theory is decisive (verified at machine precision in the
spin⊗taste representation): the kinetic form on `ℝ × Z³` has a **2-dimensional**
invariant space (`c_t ≠ c_s` *allowed*), collapsing to **1-dimensional** (`c_t = c_s`
*forced*) only under a `t↔s`-crossing **spacetime** element. Taste and the remnant
`U(1)` chiral symmetry are **internal** (they commute with, or are Lorentz-scalars
under, the spacetime `γ`-index) and impose **no** relation between `Σ_t` and `Σ_s`
(C2); the Record axiom supplies a timeless scalar with no spacetime-vector action.
So **no internal symmetry protects the velocity** — consistent with the runner's
nonzero staggered `δv`, and with the literature (staggered taste protects the *mass*
from additive renormalization, **not** the speed of light).

**Crucially, `B₄` *is* a custodial symmetry the framework possesses** — on the
**symmetric-Euclidean** regulator its own reflection-positivity / transfer-matrix,
free-staggered-SO(4), and single-clock constructions actually use, with continuous
time recovered as the `a_τ → 0` Stone limit of a `B₄`-symmetric object (C3). The
framework's **own** 2026-06-07 diagnostic note
([`DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md`](DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md))
concedes: "continuous time, if supplied by a self-adjoint Hamiltonian, does not add an
independent temporal lattice spacing … the framework must provide or admit the
self-adjoint Hamiltonian surface." So whether `δv ≠ 0` hinges on a regulator
**commitment** the framework has not settled; the `B₄` route is the **open**
constructive escape (C4), not a closed one.

### (D) The anomalous dimension `γ = (4/3 + N_f/2)α_s`
From the coupled velocity RG of #3121, the **difference mode** obeys
`d(v_F − v_b)/dl = −(C_F + C_B N_f)α(v_F − v_b)`; this eigenvalue **is** the
speed-difference operator's anomalous dimension. For SU(3): `C_F = (N²−1)/2N = 4/3`,
`C_B = T_F = 1/2` (the fermion-loop gluon dressing); the adjoint `C_A = 3` (pure-glue)
piece is `N_f`-independent and a pull toward a common reference, so it **drops out of
the difference channel**. Hence `c_γ = C_F + T_F N_f = 4/3 + N_f/2` and
`γ = c_γ α_s ≈ 0.15` (`N_f=1`) … `0.34` (`N_f=6`), central `~0.23` (`N_f=3`). Because
the gauge sector is **asymptotically free**, `α_s` — and so `γ` — is **weak exactly
at** the UV scale `M_Pl` where the anisotropy is regenerated (runner Part D).

### (E) RG run + species residual + verdict
Running `δv|_IR ≈ δv|_UV·(μ/M_Pl)^γ` (`μ/M_Pl ≈ 8×10⁻²⁰`), the **observable** is the
species residual `δv_obs = ΔC₂·(g²/16π²)c_v·(μ/M_Pl)^γ`:

| sector (comparator) | bound | `γ_crit` | central gap (`γ=0.2`) |
|---|---|---|---|
| quark/gluon (UHECR/mesons) | `10⁻¹²` | **0.54** (weakest) | `+6` |
| photon (GRB/Fermi-LAT) | `10⁻²⁰` | 0.96 | `+14` |
| electron (clock/Penning) | `10⁻²²` | 1.06 | `+16` |
| nucleon (Hughes–Drever) | `10⁻²⁷` | 1.32 | `+21` |

The framework's `γ ≈ 0.15–0.34` is **below even the weakest** `γ_crit = 0.54`
(closing it would need `c_γ ≥ 6.8`, a 3–4× inflation, not a strong fixed point
available near `M_Pl`). The residual species `δv(1 GeV) ≈ 10⁻⁸…10⁻⁴` exceeds the
**tight** bounds in **every** factor-2 corner of `(c_v, γ)` (runner E1–E6); the
**weakest** (colored) bound is at the **edge** — central gap `+6`, falling to `~+2.3`
under the most-optimistic honest factor-2 `(c_v/2, γ=0.4)`, still positive. The "all
species share one `v*`" steelman fails: different reps flow at different rates, and the
species difference **is** the observable (E5).

## Verdict

**Computed, regulator-conditional Lorentz-violation obstruction.** On the framework's
stated **asymmetric** native surface (spatial `Z³` + continuous-time Hamiltonian), the
interacting gauge dynamics generates a **computed, nonzero, not-internally-protected**
marginal velocity anisotropy `δv|_UV ≈ 1.7×10⁻² ≈ 0.2 α_s`, and the
asymptotically-free `γ ≈ 0.15–0.34` is far too small to suppress the residual species
`δv(1 GeV) ≈ 10⁻⁸…10⁻⁴` below the experimental bounds — a robust **12–21 order** gap
to the tight (photon/electron/nucleon) bounds, with the weakest (colored) bound at the
edge. This is the Collins–Perez–Sudarsky–Urrutia–Vucetich problem made **computed** for
the framework: the gauge dynamics does **not** close Lorentz naturalness on this
surface, and the **internal (taste)** protection escape is **refuted**.

**The single live escape is the regulator commitment.** The `B₄` hypercubic symmetry
— which the framework's own symmetric-Euclidean (RP / SO(4) / single-clock)
constructions possess, with continuous time as the `a_τ → 0` limit — **forbids** the
marginal operator and gives `δv → 0`. Whether the physical UV regulator is the
asymmetric Hamiltonian surface (obstruction) or the `B₄`-symmetric-Euclidean limit
(protected) is a **framework-definition question the framework has not settled**; it is
the dominant residual and the only thing that can flip the verdict. This note
therefore **upgrades #3121/#3123 to computed, closes the internal escape, and reduces
emergent-Lorentz naturalness to a sharp, named regulator-commitment question** plus the
explicit `B₄` custodial route (available-but-forgone).

## Honest scope (the named residuals)

- **Regulator commitment (dominant, can flip the verdict).** The verdict is
  conditional on the asymmetric surface being the physical regulator. The
  `B₄`-symmetric-Euclidean limit (the regulator of the framework's own
  RP/SO(4)/single-clock results) gives `δv → 0`. This is a framework-definition
  question, not a calculation; it is **open**.
- **Exact O(1) coefficient `c_v` (~factor-2).** Rainbow-only, single-continuum-gluon,
  crude vertex: the **tadpole/seagull** diagram required by the lattice Ward identity,
  the full Wilson/clover vertex, a consistent lattice gluon action, and continuum
  matching are not included. A Ward-enforced rainbow⊕tadpole cancellation to `c_v ≈ 0`
  is **unlikely but not formally excluded**; it would matter only for the **weakest**
  (colored, edge) bound, not the tight bounds.
- **Sign (`v < 1`).** Certified only by the Euclidean method; the independent
  real-time cross-check cannot triangulate it. The verdict does not depend on the sign.
- **Anomalous dimension.** `c_γ = 4/3 + N_f/2` carries an O(1) `N_f`/convention
  ambiguity; `γ` is structurally tethered to the weak AF `α_s`, so it cannot be `~1`
  at `M_Pl`. The physical fixed-point `γ` (vs the one-loop eigenvalue) remains the
  named open input. The verdict is robust to factor-2 in `γ`.
- **Species accounting.** The SU(3) computation gives color-singlet leptons (`C₂=0`)
  `δv = 0` from gluons; the photon/electron bounds constrain EM/weak sectors with
  **separate** couplings and runnings. The single-`α_s`, single-`ΔC₂` estimate is an
  O(1) cross-gauge-group simplification, sufficient for the order-of-magnitude verdict.
- **Constructive escapes** (what would overturn the obstruction): (i) commit to the
  `B₄`-symmetric-Euclidean regulator (the marginal operator is then forbidden); (ii) a
  framework-internal strong-coupling fixed point with `γ ~ 1` near `M_Pl` (precluded by
  asymptotic freedom); (iii) an honest custodial admission.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only a **computed,
  regulator-conditional** naturalness gap at the interacting level.
- It does **not** claim a 3-significant-figure `δv`; it claims a computed, nonzero,
  O(1)-coefficient value, robust in order of magnitude, with the exact coefficient
  scoped as a residual.
- It does **not** claim the `B₄` custodial route is **absent** — it is
  **available-but-forgone** on the framework's own symmetric-Euclidean regulator;
  "continuous time breaks `B₄`" is an admitted dynamics gate, not a theorem.
- It does **not** independently certify the `v < 1` sign (Euclidean-method-only).
- It does **not** contradict #3121 (the attractive flow is real) or the tree-level
  dissolution; it **computes** #3123's open coefficient, **refutes** the internal
  (taste) protection escape, and **sharpens** the open problem to the regulator choice.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG-fit /
  `g_bare` derivation input (`β = 6 → g² = 1` is the framework's own convention; the
  LV bounds are comparators).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, from Haar/lattice primitives): the dim-6 dispersion
  `a²/3`, `a²/12` (sympy); the naive-doubler off-shell artifact and the Wilson
  off-shell `~5×` `r`-sensitivity; the gauge-invariant on-shell `δv = Σ_s − Σ_t` with
  its `r`-stability, magnitude `~0.01–0.02` per `g²C₂`, gauge spread, IR-finiteness,
  and staggered non-protection; the 4D-symmetric `B₄` control (`δv = 0` to `10⁻¹⁵`) and
  the spin⊗taste internal-vs-spacetime invariant count; `C_F = 4/3`, `T_F = 1/2`, the
  difference-mode eigenvalue `γ = (4/3 + N_f/2)α_s`; the `γ_crit` table, the residual
  species gap, and its asymmetric factor-2 robustness.
- **Cited** (comparator/scope only, never a derivation input):
  Collins–Perez–Sudarsky–Urrutia–Vucetich *PRL* **93** (2004) 191301;
  Capitani *Phys. Rept.* **382** (2003) 113 (hep-lat/0211036, lattice one-loop
  `Z`-coefficients); Groote–Shigemitsu *PRD* **62** (2000) 014508 (hep-lat/0001021,
  anisotropic speed-of-light renormalization at the same on-shell point, generically
  nonzero `O(α_s)`); Giuliani–Mastropietro–Porta *Ann. Phys.* **327** (2012) 461
  (rigorous attractive emergent-Lorentz flow, restored only with a protecting Ward
  identity); Bednik–Pujolàs–Sibiryakov *JHEP* **1311** (2013) 064; Nielsen
  (gauge-parameter independence of the pole); Reisz (lattice power-counting,
  *CMP* 1988); Kostelecký–Russell SME data tables (LV comparator bounds).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
- [DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md](DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + the approved scale primitive `a⁻¹ = M_Pl`;
(2) the framework's stated native surface (spatial `Z³` + continuous time) as the
regulator under test, with the `B₄`-symmetric-Euclidean limit named as the alternative;
(3) the `β = 6` SU(3) bare coupling (`g² = 1`); (4) standard one-loop lattice
perturbation theory (rainbow self-energy, Wilson/staggered doubler control, the Nielsen
on-shell pole prescription, the coupled velocity RG of #3121); (5) SME/UHECR/GRB/clock
bounds as comparators. The result is a one-loop, rainbow-level computation; the exact
O(1) coefficient (full lattice vertex + tadpole) and the regulator commitment are the
named residuals.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (self-energy, pole velocity, Nielsen identity, Wilson/staggered
fermion, taste/hypercubic symmetry, anomalous dimension, RG flow, Reisz power-counting).
No fitted/PDG/lattice-MC value consumed as a derivation input (`β = 6 → g² = 1` is the
framework's own convention; the LV bounds are comparators).

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3121, #3123, the emergent-Lorentz notes, the free-staggered SO(4) note, the
diagnostic note, or any upstream row. The independent audit lane is the only status
authority.
