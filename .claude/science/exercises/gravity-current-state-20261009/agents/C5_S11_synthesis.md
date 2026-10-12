# C5 S11: synthesis after rounds 8–9 (refereed through 18:14Z; R10-1..R10-5 pending)

**Author.** Claude Opus 5.5 (S11), the same model family as every C5 worker, the supervisor, S5 and S8. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict as recorded in `TESTS.md` or in the cited `C5_*_referee_verdict.md`. Written 2026-10-12, 18:23Z to about 19:05Z. No repository file was edited.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:3441-4077` (round 8 to the end); `agents/C5_S8_synthesis.md`; `SUMMARY.md:534-636` (§§21–24); referee verdicts `C5_R8-1`, `C5_R8-4`, `C5_R8-5`, `C5_R9-1`, `C5_R9-2`, `C5_R9-4`, `C5_R9-5`, `C5_R9-6`, `C5_R9-7`, `C5_R9-8`, `C5_R9-9`, `C5_R9-10` (`_referee_verdict.md`). **Read in part:** `C5_S5_synthesis.md:1-50,218-262`; `C5_R9-3_referee_verdict.md:1-3,86-110`; `TESTS.md:2302-2320` (method), `:2399-2404` (O3), `:2878-2898` (R5-3 registration), `:2985-2994` (R5-3), `:3331-3343` (R6-2), `:3409-3419` (R6-4), `:725-760` (lane R); `SUMMARY.md:281-293,430-436`. **Pending, used only as pending:** `C5_R10-1_report.md:37-63,121-136,245-284` and `C5_R10-2_report.md:24-44,179-248` (worker reports; referees running). R10-3 and R10-4 worker reports exist in scratch and were **not** read for content; R10-5 has no report.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `PRICE_NOTE` are in `P/`; bare `C5_*` are in `P/agents/`; `vR8-1` abbreviates `C5_R8-1_referee_verdict.md` (and so on). `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.**
- **[ref]** referee-confirmed, with the referee's scope.
- **[ref, bounded: …]** a refereed FAIL, EXCLUDED or no-go, with its class.
- **[pending]** R10-1, R10-2, R10-4 (referees running); R10-3, R10-5 (workers running). Worker claims, not verdicts.
- **[S11 reading]** an interpretation made here; same family; unrefereed.

**Sets** (as S8, `C5_S8_synthesis.md:17`). A = continuum base, discreteness only in records. B = Euclidean Z⁴, whole law hypercubic. B′ = Lorentz-random lattice. C = the axioms' Z³ (continuous time) and tune. C-box = Z³ × ℝ with a box-exact law (dispersion exactly √(m²+k²) on an open momentum box, smooth and periodic outside). E = holographic or lower-dimensional substrates.

**Dated correction carried in (2026-10-12, `TESTS:3797`).** The R7-1 referee's "the quartic prefactor must be ¼" is withdrawn; ½ is right. S8's rung-3 line "the drift survives a ¼ rerun (δ ≈ 0.019)" (`C5_S8_synthesis.md:64`) should read: the correct-normalization drift is δ ≈ 0.074.

---

## 1. What changed since S8, in plain words

### 1.0 The short version

At S8 (16:36Z) the box route had one PASS (free particles) and one warning (Theorem E: some states on a periodic band must fall the wrong way). Since then the box route was pushed up a ladder, and the ladder split cleanly in two.

1. **Everything that lives inside the box came out exact.** Two interacting particles keep exact relativity in 1D, 2D and 3D. Bound bodies of any binding, and in 2D with spin, fall at exactly the same rate. The free box law runs on plain qubits, one per site, in a sector with no vortices.
2. **Everything that sums over the whole momentum zone came out broken.** Gauge fields, loops that create pairs, a filled vacuum, and the graviton's own loops all reach the edge outside the box, and the edge carries the grid's leftover anomaly. Light and electrons then travel on different light cones by as much as on a plain grid (R8-5, R9-8), and the graviton's speed shift is an average of the same anomaly (R9-9).
3. **The pending R10-1 worker says the box saves no tunings at one loop** (C-box's count equals set C's) and finds one structural cancellation for the photon, a boson–fermion pairing on the edge. It does not reach the electron. R10-5 tests whether full pairing does.

**[S11 reading], the one-sentence picture.** The box is exact for a world with a fixed number of particles that never create pairs and has an empty vacuum. Our world creates pairs (QED's vacuum polarization is measured), so the loops are not optional, and the edge must be dealt with. On present evidence the only untuned way to deal with it is a boson–fermion pairing, the same structure O3 found is needed to cancel vacuum energy (`TESTS:2400-2403`).

### 1.1 The C-box ladder: what is exact for matter

Each rung is refereed, with scope. "Box domain" means a common invariant Lie-algebra domain, not an exponentiating Poincaré sector (`vR8-1:36`).

**Rung 1, free particles: PASS WITH SCOPE (R7-1, unchanged; `TESTS:3398-3407`).** Now also realized on qubits (rung Q below).

**Rung 2, two interacting particles.**
- **d = 1 and d = 2: PASS WITH SCOPE [ref; `TESTS:3795-3805`].**
  - Boost-sign repair confirmed. d = 1 lattice ring residuals 1.1e-11 to 3.1e-8 at L = 2048.
  - d = 2: a p-wave doublet with spin term, α = +1 forced by [K_x, K_y] = −iJ; the chart algebra closes to 9e-11.
  - The direct lattice-native d = 2 run is not a precision check (residuals 7e-3 to 0.35); the fixed PASS sentence is met by the exact chart-to-lattice proof (`vR8-1:32-34`).
  - The interacting leakage theorem holds: ‖(U_lat − ι U_BT)ψ‖ ≤ 2‖(1 − E)ψ‖ (`vR8-1:36`).
- **d = 3: PASS WITH SCOPE [ref; `TESTS:4016-4024`].**
  - A rotationally scalar p-wave triplet with K = ½{H, X_NW} + (P × S)/(M + H). α = 1 is forced.
  - All 45 chart commutators converge from 5.5e-7 (NP = 28) to 1.5e-10 (NP = 40). The triplet mass is direction- and P-independent.
  - The interaction support lies in |k| < 1.548 < B, so the **ball** sector carries exact E(3). The deformed rotation flows commute with H but do not form SO(3) off the cube (`vR9-6:40`).
  - Scope: two particles; no N ≥ 3, pair creation, loops, gauge, Ward identities or gravity.

**Rung 3, three bodies: still INCONCLUSIVE physically [ref; `TESTS:3902-3907`].**
- R9-3's literal reading is FAIL, but as a **registration artefact**: cluster separability forces non-zero spectator-channel limits (B → B_a ≠ I), which the fixed tail clauses forbade as worded (`vR9-3:3`).
- The physical question (subtracted tails, assembled H_S and K_S) is open. B, H_S and K_S were never assembled.
- The pair-sum drift is real (R7-6; δ ≈ 0.074 at the correct normalization, `TESTS:3797`).

**Rung 4, gravity on bound bodies (uniform field, linear order).**
- **d = 1: PASS WITH SCOPE [ref; `TESTS:3889-3900`].**
  - The Weyl-midpoint density gives a Hermitian, quasi-local stress with ∫T⁰⁰ = H and energy dipole K.
  - Energy conservation is exact globally. Momentum conservation is exact only box-to-box, with a transition-shell source outside (`vR9-2:7`).
  - **On the box domain, Ẍ_E = −g(1 − 2V²)**: zero linear-order Eötvös violation between equal-velocity bodies of different binding. This is an operator theorem; the numerics are consistency checks (`vR9-2:9-11`).
- **d = 2 with spin: INCONCLUSIVE against the fixed reading, with the fall theorem confirmed [ref; `TESTS:4037-4044`].**
  - A symmetric, Hermitian, Gevrey-quasi-local (Belinfante) stress exists, constructively, with J_T = J box-to-box. The numerically checked chart stress is not the global quasi-local flux (`vR9-10:12`).
  - **Ẍ_E = −g + 2(g·V)V on the box domain, independent of binding and spin** (`vR9-10:17-19`). This is the 1D result's natural 2D form.
  - Unmet: GR's curved-field couplings (geodetic, spin–curvature). Only the special-relativistic accelerated-frame term and unit rigid-rotation coupling are confirmed (`vR9-10:21-22`).
- **Free shear (R9-2(a)) [ref; `TESTS:3897-3900`].**
  - SHEAR-ABSENT in R8-2's actual empty vacuum.
  - With a supplied scalar zero-point completion, the shear is edge-carried: μ_E = −0.20565108 (literal edge) or +0.0079760558 (gapped edge) at m = 1, μ_T2 = 0. A profile zero at t* = 0.287922 is an edge tuning.

**Rung Q, the box law on qubits: a genuine sector-qualified realization; INCONCLUSIVE under the fixed clause [ref; `TESTS:3917-3923`].**
- An explicit one-qubit-per-site brick-wall Pauli-string Hamiltonian in d = 2, super-polynomially quasi-local. Its simply connected flux-free invariant direct sum is unitarily equivalent to R7-1's free Fock law.
- So the undeformed Poincaré Lie algebra holds on the box domain at every finite particle number: even N in the vacuum representation, odd N in the ε representation (`vR9-5:17-18`).
- Visons are exactly conserved and static; their bands are flat. A local σ^z leaves the flux-free subspace.
- Δ_v = 0 does not select the flux-free vacuum. The tested threshold is about 3.81e-3 but no bound covers every flux configuration. Tail constants are numerical estimates, not certificates (`vR9-5:9,12`).
- **[S11 reading]** This partly answers S8's open owner question (`C5_S8_synthesis.md:504`): fermion composition is not forced on the Qubit text; the price moves to which sector is physical (P45 below).

### 1.2 What loops, gauge fields and gravity break

**Gauge fields.**
- **R8-5: FAIL (bounded) [ref, bounded: conventional Hamiltonian U(1), finite-component, bilinear, translation-covariant, ℓ¹-quasi-local gauge generators; `TESTS:3807-3813`].**
  - *Lemma C (charge rigidity).* The non-zero charge spectrum has constant multiplicity over the Brillouin torus. So the complete gauge vertex cannot vanish when a fermion leg leaves the box. The edge is charged.
  - *The split.* In explicit Peierls-coupled box QED, the in-box rules and Ward identity are exact, yet the electron–photon cone split is unsuppressed: Δ ≈ −11 to −71 (nine shapes), −21.8 ± 0.15 as m → 0, about −713 at Wilson r = 32 (in e²/16π² units).
- **R9-8: INCONCLUSIVE [ref; `TESTS:4026-4035`].** The cheapest non-minimal construction (FW frame, symmetrized-staircase Wilson lines): Δ = −33.586; all 15 quasi-local staircase cases have |Δ| ≥ 12.9; path changes move the photon coefficient by −5.5 to −69.3. "Strongly rejects protection in the cheapest construction"; not a stated-class no-go (`vR9-8:27`).

**Pair-creating loops without gauge fields.**
- **R7-5 (pre-S8): FAIL bounded for point (P) and frame-fixed (FF) vertices** (`TESTS:3500-3504`).
- **R8-4: INCONCLUSIVE [ref; `TESTS:3815-3820`].** Model S (four CAR modes per site) is stable and Lorentz-invariant at one loop **only after** a frame-dependent fermion factor h = (3W − E)/(W + E), "a tuned non-scalar kinematic factor" (`vR8-4:28`). The ordering-truncated toy N fails at two loops: −6.2% (fermions), −0.60% (bosons) at p = m/3.
- **R9-7: INCONCLUSIVE [ref; `TESTS:3925-3937`].** The complete set of 24 orderings removes most of toy N's failure. The registered completion P1 still leaves +4.8e-4 (bosons) and −1.35% to −3.62% (fermions). P2 closes exactly for bosons but keeps no leg in the box. The completed fixed-box Hamiltonian is untested.

**The graviton.**
- **R9-9: INCONCLUSIVE, with a narrow mass FAIL [ref; `TESTS:3939-3950`].**
  - *Tree level is exact.* The N-type graviton with a smooth non-analytic symbol d(q) has an exact linear constraint algebra, two TT modes with ω = |q| in the box, no doubler, and an exact midpoint-phase Ward coupling to R8-2's number-conserving stress.
  - *Theorem T [ref].* For pair-creating scalar TT vertices independent of k_z and q, the one-loop paramagnetic coefficient is Ξ = ⟨|V|²[Hess_zz(ε²/2) − 1]/ε⁵⟩/32: a moment of Theorem E's anomaly. Negative on the gapped edge (proved), positive on the literal edge (numerical).
  - *Not class-wide.* The pair stress is not Ward-completed; the seagull is not fixed by a second-order Ward identity; polarization-dependent ultralocal seagulls can cancel the mass split; and **the dressed matter speed was not computed**, so Ξ ≠ 0 is a shift against the bare cone, not yet a graviton–matter split (`vR9-9:23`).

**The literal edge.**
- **R9-1 [ref; `TESTS:3839-3847`].**
  - **L under G-out: EXCLUDED.** Seven electron corner valleys add about 588 MeV to the Z width (ΓZ = 2495.5 ± 2.3 MeV), for any lattice parameters (`vR9-1:9`).
  - **G-in is inconsistent, not equivalent to G-out**: exact conservation of a momentum-diagonal charge under an arbitrary lapse forces the charge to be constant over the connected torus (Lemma Q; `vR9-1:5-6`). [S11 reading] Lemma Q is Lemma C seen from gravity's side.
  - G overall OPEN. HARMLESS only for an exactly empty initial edge in the strictly number-conserving law. Under separate stable-equilibrium assumptions the relic bound crosses Ω_c h² at T ≈ 3.52e17 GeV (`vR9-1:15,25`).
  - The flat edge mean is exact: ⟨A_ii⟩_edge = −1/f_edge (`vR9-1:18`).

**[pending] R10-1, the anomaly-inflow test (worker reading SUGGESTED; `TESTS:4046-4052`; `C5_R10-1_report.md:37-63`).**
- *Localization lemma (sketch).* Under box exactness, every one-loop dimension-4 LV coefficient lives on the edge and the face shell; the box contributes exactly zero (`:123-135`).
- *Theorem T′.* The scalar-QED photon speed shift is an A-moment with a Ward-forced positive weight.
- *Theorem D.* The Dirac-sea photon shift is a zone average of **four** anomaly functions (A; a = |∂h|² − 1; two Wilson-mixing terms). It reproduces R8-5's refereed numbers to ≤ 1e-3. For box shapes the a-term dominates (S3: +21.0 from a, +0.5 from A, −6.4 from mixing).
- *Theorem P.* Clifford-flat fermions (8 components per site) plus two matched complex scalars cancel the photon's shift pointwise, for every edge shape, masses free: an edge supertrace.
- *What remains.* The electron's own shift in the paired law is −10.7 to −18.0, so c_e − c_γ ≈ −6e-3 to −1e-2. The graviton sector is not paired.
- *Count.* Equal to set C's ≥ 6 at one loop, with or without pairing (`:245-260`; a reading).

### 1.3 Theorem E as the common cause [S11 reading, built from refereed parts]

1. **The identity [ref].** For any C² periodic band, ∫_zone Hess(ε²/2) = 0, so A = Hess(ε²/2) − I averages to −I (`TESTS:3556`). Inside the box A = 0, so the edge carries all of it: ⟨A_ii⟩_edge = −1/f_edge (`vR9-1:18`). No edge shape removes it.
2. **Why the edge cannot be hidden [ref].** Any conserved charge that couples to a gauge field (Lemma C, `TESTS:3808`) or to gravity under an arbitrary lapse (Lemma Q, `TESTS:3841`) must take the same value on the edge as in the box. So edge states couple with full strength.
3. **Where it shows up.**
   - In free fall of edge quanta (Theorem E, `TESTS:3556`) [ref].
   - In the graviton's one-loop speed (Theorem T, `TESTS:3945`) [ref].
   - In the free shear once a zero-point sea is supplied (`TESTS:3897-3900`) [ref].
   - In the photon's one-loop speed, as an A-moment for scalars and as A plus three removable functions for Dirac matter [pending R10-1].
4. **The rule [S11 reading].** Anything that lives in the box is exact. Anything that sums the whole zone (loops with pair creation, a filled sea, a thermal population, a gauge charge) integrates the edge anomaly.
5. **The caveat.** "Common cause" is exact for the irreducible part only. R10-1's Dirac a- and mixing-terms are not forced by periodicity: Clifford-flat structure sets a ≡ 0 (pending). A is the part no structure removes, because its zone integral is fixed.
6. **The only cancellation found.** An unavoidable A-moment has been cancelled only by contributions of opposite sign from bosons and fermions (Theorem P, pending). [S11 reading] The structure resembles Nielsen–Ninomiya (a zone-integral identity forcing something at the edge, RECALLED), and the cure resembles supersymmetry.

### 1.4 Set A: records as the classical metric

- **Newtonian: VIABLE** on 4e-10 ≲ ℓ_s ≲ 5e-6 m (true lower end about 1e-10 m) [ref; R6-4, `TESTS:3409-3418`]. Unchanged.
- **Covariant: OPEN, with excluded subclasses narrowing it [ref; R8-3 `TESTS:3559-3573`; R9-4 `TESTS:3909-3915`].**
  - **(i) Spacelike-only noise: EXCLUDED** in class T (stationary linear-meter dilation, (H-T), standard retarded propagator, one-sided cone limits). It forces a response jump whose generic radiation carries (ln r)/r.
  - **(ii) Scalar-only noise: EXCLUDED** (it cannot pay for a GR-normalized spin-2 response); its additive spin-2 repair inherits R8-3.
  - **(iii) Correlated, emission-cancelled histories: OPEN.** OWD Eq. (27) is additive, so it is inside R8-3's subclass, but correlated histories are not. **[pending] R10-3** builds the simplest one.
  - **(iv) Preferred frame: OPEN.** UV convergence needs integer n ≥ 3; D′₀ ∝ 1/|s| is not a locally finite positive measure at the cone, so a regulator or restricted domain is needed. The 2e-7 to 5e-6 m interval is only a search target (`vR9-4:11`).
  - (H-T) is not proved for general completely positive Gaussian CQ histories (`vR9-4:3`).
- **[S11 reading]** A's discrete records can do gravitational work only through noise that is correlated in time (iii) or tied to a frame (iv). Everything simpler is now excluded in its class.

### 1.5 Λ

- **Mean [ref; R5-3, `TESTS:2985-2993`]: all four routes OPEN.**
  - Lemma PT holds within G1–G3: the electroweak shift alone needs cancellation to 1 part in 4.7e54.
  - Global Kaloper–Padilla sequestering is EXCLUDED (bounded): |Ω_k0| ≥ 0.917.
  - "Records form until frozen" leaves an additive constant; it needs an extra q-type source rule.
- **[pending] R10-4** tests records as a conserved q-charge in set A (continuum base, volume free; `TESTS:4000-4012`).
- **New from the box route [ref].** C-box's clean vacuum results hold only for the empty Fock vacuum: no shear (R9-2), zero graviton self-energy (`vR9-9:23`), no cosmological edge production (`vR9-1:15`). A sea brings the edge back. **[S11 reading]** In C-box the vacuum question and the edge-anomaly question are the same question: both are zone sums.
- **The shared cure [S11 reading].** O3 (refereed) found untuned vacuum cancellation needs matched boson and fermion spectra, and a qubit site cannot carry both CCR and CAR modes (`TESTS:2400-2402`). R10-1's photon cancellation (pending) needs the same kind of pairing. R10-5 computes whether one edge-SUSY structure does both at one loop.
- **Fluctuation:** unchanged since S8 (`C5_S8_synthesis.md:191`).

### 1.6 Set B with box symbols [pending R10-2; worker reading FAIL (bounded); `TESTS:4054-4060`]

- *Lemma A.* Reflection positivity (RP) forces each two-point function to be analytic in the Euclidean time momentum k₄ away from πZ. A smooth box symbol is non-analytic at its edge, so it is not RP.
- *Lemma B.* No smooth RP law is exactly O(4) on an open set.
- *The survivor.* Whole-zone SLAC passes link RP numerically, but RP then forces a gapless continuum of zero-energy time-doublers at every spatial momentum: R2-1's tower again.
- *Without RP,* the registered graviton count falls from 11 to 5 + Λ, not to 2. γ ≤ ½ (R2-4) binds unchanged (`C5_R10-2_report.md:179-226`).
- [S11 reading] If confirmed, set B cannot use the box trick at all. The trick needs a non-analytic symbol, and positivity forbids exactly that.

### 1.7 Calibration of S8's expectations [S11 reading]

- **Right:**
  - R9-1: L under G-out EXCLUDED.
  - R9-2(b)–(c): PASS in d = 1.
  - R9-4: all OPEN, with the q² = 0 risk realized as (ln r)/r.
  - R9-5: INCONCLUSIVE, with the vison gap as the risk.
  - R9-7: INCONCLUSIVE.
- **Better than expected:** R9-6 got PASS WITH SCOPE, not INCONCLUSIVE.
- **Wrong:**
  - R9-2(a): S8 expected SHEAR-PRESENT. It is absent in the empty vacuum and present only with a supplied sea.
  - R9-1 G-in: S8 expected "leaning HARMLESS". It is inconsistent within the exact-Ward class.
  - R9-3: an INCONCLUSIVE was expected, and the physics is INCONCLUSIVE, but S8's own registration made the literal reading FAIL. That defect is S8's (`vR9-3:3`).

---

## 2. Table: forced / dead (bounded) / open

**Legend.**
- **F** = forced or met under stated hypotheses.
- **D(b)** = dead, bounded to the named class.
- **O** = open.
- **P** = premise (supplied).
- **pend** = R10-x.
- "as S8" = unchanged since S8 (`C5_S8_synthesis.md:183-194`).
- **New** marks a change since S8.

| Item | A: continuum + records | B: Euclidean Z⁴ | B′: LRL | C: Z³ + tune | C-box: Z³ + box law | E: holographic |
|---|---|---|---|---|---|---|
| **One cone, matter, tree level** | F (as S8) | F at dim 4 (as S8). **pend R10-2:** box symbols not RP | as S8 | P: tuned (F2 3.1e-17) | F inside the box. **New:** 2-body exact in d = 1, 2, 3 (`TESTS:3795-3803,4016-4024`); free law on qubits in a sector (`TESTS:3917-3923`). O: N ≥ 3 (`TESTS:3902-3907`) | O (as S8) |
| **One cone at one loop (gauge, pairs)** | F | F at dim 4 | O | P: ≥ 6 conditions (reading, `SUMMARY:436`) | **New D(b):** Peierls box QED, Δ ≈ −11 to −71 (`TESTS:3808-3812`); G-in inconsistent with exact Ward (`TESTS:3841`). O: non-minimal (R9-8: cheapest Δ = −33.6, `TESTS:4031`); INV two-loop (`TESTS:3815-3820,3925-3937`). **pend R10-1:** count = C's; photon-only supertrace. **pend R10-5** | O |
| **Graviton: gauge identity / production** | O (R6-2). Supplied in every built A | D(b) finite fibre (as S8) | as S8 | Linear N-type bridge (as S8) | **New F (tree, supplied):** N-type box graviton, 2 TT modes ω = \|q\|, no doubler, exact Ward coupling to number-conserving stress (`TESTS:3940-3944`). Production: O everywhere | as S8 |
| **Graviton: one-loop protection** | n/a (supplied, continuum) | 11 tunings; **pend R10-2:** 5 + Λ without RP | 5 (conditional) | 2 TT + 3 speed codims (reading) | **New:** Theorem T speed anomaly is an A-moment [ref] (`TESTS:3945`). Narrow mass FAIL only for minimal-metric seagull (`TESTS:3946`). Dressed matter speed not computed (`vR9-9:23`) | n/a |
| **Equivalence principle** | F, exact | SUGGESTED (as S8) | O | Tuned via speeds | **New F (uniform field, linear order, box domain):** bound bodies of any binding fall alike, d = 1 (`TESTS:3895`); any binding and spin, d = 2 (`TESTS:4043`). D(b): literal edge with charged doublers (Z width, `TESTS:3840`). O: curved-field spin couplings (`TESTS:4044`); space–space (γ) coupling of bound bodies; edge population (G OPEN) | n/a |
| **Free shear (E_g mass)** | F (Ward) | tuned | one tuning | tuned (P0) | **New:** ABSENT in empty vacuum; with supplied sea, edge-carried μ_E = −0.206 (L) / +0.0080 (G); zero only by edge tuning t* (`TESTS:3897-3900`) | n/a |
| **Λ mean** | P. **pend R10-4** (records as q-charge) | P | P | P | P. **New:** empty-vacuum results do not survive a sea (§1.5) | P (as S8) |
| **— shared mean results** | R5-3 all OPEN; Lemma PT; KP global D(b) (`TESTS:2985-2993`). O3: untuned cancellation needs matched B/F spectra; qubit site D(b) for CCR+CAR (`TESTS:2400-2402`). **pend R10-5** (edge-SUSY vacuum energy) | ← | ← | ← | ← | ← |
| **Λ fluctuation** | as S8 | as S8 | D(b) under H1/H2/H4 (as S8) | as S8 | Not addressed | as S8 |
| **Records & metric** | **New:** Newtonian VIABLE (as S8). Covariant: spacelike-only (i) and scalar-only/additive (ii) D(b) in class T (`TESTS:3911-3912`); (iii) correlated O, **pend R10-3**; (iv) preferred frame O, n ≥ 3 (`TESTS:3915`) | D(b) classical RP (as S8) | as S8 | Shared budget | Not addressed | O |
| **Qubit (⊗M₂) realization** | n/a (infinite fibre) | as S8 | P18 (as S5) | F (one qubit per site, by construction) | **New:** free law exact on the flux-free invariant sum, d = 2 [ref, INCONCLUSIVE under fixed clause]; vison gap not bounded; d = 3 not built (`TESTS:3917-3923`). Pair-creating model S needs 4 CAR modes per site (`vR8-4:77`) | n/a |
| **Per-realization law / frame** | n/a | Exists; γ ≤ ½ (as S8) | as S8 | Preferred frame | Exists; frame hidden up to the rapidity budget; **New:** exact E(3) on the ball sector only (`TESTS:4020-4023`) | O |

**Closed since S8 (bounded deaths, no price).**
- C-box:
  - the literal edge with charged doublers under point-local coupling (`TESTS:3840`);
  - box-supported Ward-exact gauge vertices with a charged edge, within the exact-Ward class (`TESTS:3841`);
  - Peierls box QED as a protection mechanism (`TESTS:3808-3812`);
  - ordering-truncated INV toy N at two loops (`TESTS:3818`);
  - the minimal-metric graviton seagull on the L → G edge family (`TESTS:3946`).
- Set A: spacelike-only CQ noise; scalar-only and additive spin-2 CQ, both in class T (`TESTS:3911-3912`).
- Registration defect: R9-3's tail clauses (`TESTS:3903`). This is a lesson for drafting, not physics.

---

## 3. Price ledger delta since S8 (named only, none adopted)

S8 ended at P34 (`C5_S8_synthesis.md:225-237`).

**Axiom lines.**
- Lattice `AX:37-41` ("proper cubic rotations" `:37-38`; "No site is privileged" `:40`).
- Qubit `AX:45-53` (M₂(C) `:47`; "No possibility is privileged" `:52`).
- Admissibility `AX:57-61` (nearest-neighbor rule `:57-58`; distribution `:60-61`); reading notes `:63-73`.
- Record `AX:77-83`.
- Qualification `AX:87-95` ("A law privileges no states" `:94`).
- Not a dynamics axiom `AX:116-130`.
- Open gates `AX:173-190` (formation rules `:182-184`; source/action `:187`; scale reference `:189-190`).

| # | Price (named only) | Text touched | Set | What the refereed record says it buys or costs |
|---|---|---|---|---|
| P35 | **Rotation multiplets and the ball.** In d ≥ 2 the two-body box law needs rotationally scalar p-wave multiplets with the spin term (P × S)/(M + H), α = 1 forced. Exact continuous rotations hold only on the ball sector; the deformed flows are not SO(3) off the cube | Lattice `AX:37-38` supplies proper *cubic* rotations only; continuous SO(3) on the ball is law content [S11 reading]. Plus the H-P bridge (P29) | C-box | Buys exact two-body Poincaré in d = 2, 3 (`TESTS:3800-3803,4017-4023`). Not an exponentiating sector (`vR9-6:40`) |
| P36 | **Box-to-box gravitational conservation.** The interacting stress (Weyl midpoint; Belinfante in d = 2) conserves momentum only box-to-box, with off-box shell and torque sources. Gravity enters through the supplied first-moment lapse bridge | None in the four texts; the bridge is the open gate "source/action and physical-observable identification" `AX:187` | C-box | Buys exactly universal uniform-field fall for any binding (d = 1) and binding plus spin (d = 2) (`TESTS:3895,4043`). Costs: no globally source-free interacting stress (`TESTS:3896`); curved-field spin couplings untested (`TESTS:4044`) |
| P37 | **Gauge charge rigidity.** To keep gauge vertices off the edge, give up one of: finite-component, bilinear, translation-covariant or ℓ¹-quasi-local gauge generators. Otherwise accept a fully charged edge and its unsuppressed cone split. Gravity's analog: Lemma Q | Qubit `AX:47` (finite component); Lattice `AX:37-41` (translations); Admissibility `AX:57-58` only if "nearest-neighbor" is read as a range limit on dynamics, which `AX:116-130` does not support [S11 reading] | C-box | `TESTS:3808-3813,3841`; non-minimal escape INCONCLUSIVE (`TESTS:4035`) |
| P38 | **Gapped edge for charged species.** With point-local gauge coupling the literal edge is excluded (Z width +588 MeV), so P27(a) dies for charged matter and P27(b) is required. Conditional cosmology: under stable equilibrium the relic bound crosses Ω_c at T ≈ 3.52e17 GeV | None (law choice). The temperature cap is a condition on the state, which the axioms neither supply nor forbid (`AX:92-95`) [S11 reading] | C-box | `TESTS:3839-3847`; `vR9-1:9,15,25` |
| P39 | **Loop protection, revised (refines P28a).** Invariant-mass vertices need: (i) a supplied block of four CAR modes per site; (ii) a frame-dependent fermion factor h = (3W − E)/(W + E), a tuned non-scalar factor; (iii) the full crossing set, whose vertex functions the prescription does not fix. The only exactly closing completion found (P2, bosons) is not box-confining | Qubit `AX:47`: a 16-dimensional site block against the one-site M₂(C) (`vR8-4:77`) | C-box | `TESTS:3815-3820,3925-3937`; `vR8-4:28` |
| P40 | **The empty vacuum (scope price).** C-box's clean vacuum results need a number-conserving law with an empty Fock vacuum. A sea or zero-point completion brings back edge shear and Theorem T | None directly; the Hamiltonian is downstream (`AX:116-130`) | C-box | `TESTS:3897-3900`; `vR9-9:23`; `vR9-1:15`. [S11 reading] Observed pair creation and vacuum polarization make this a scope, not an option, for charged leptons |
| P41 | **A supplied box graviton.** The N-type graviton with non-analytic symbol d(q) is exact at tree level. At one loop with pair creation it carries Theorem T's speed anomaly, and its seagull is not Ward-fixed. Removal needs a polarization-dependent seagull choice (a tuning) or pairing | Qubit `AX:45-53`: a link tensor field is not site-possibility content [S11 reading]; source/action gate `AX:187` | C-box | `TESTS:3939-3950`; `vR9-9:21-25` |
| P42 | **[pending R10-1/R10-5] The edge supertrace.** Clifford-flat fermions (8 components per site, unit-speed edge curve) plus two complex scalars per four fermion components on the same curve. For observables: matched partner loops for matter self-energies, a TT pairing, two-loop stability | Qubit `AX:47`: bosons and 8-component fermions per site. O3: a qubit site cannot carry both CCR and CAR (`TESTS:2402`); FS-type lattice SUSY is the known interacting escape (`TESTS:2403`) | C-box | `C5_R10-1_report.md:206-243,278-284`; R10-5 (`TESTS:4064-4076`) |
| P43 | **[pending R10-2] Box symbols in set B.** Either give up reflection positivity, or use whole-zone SLAC: 1/r² tails, link RP only, a gapless time-doubler continuum, and no count reduction | Admissibility `AX:60-61`: RP is what makes the Euclidean weight a probability law with a Hilbert space (`C5_R10-2_report.md:245`) | B | `C5_R10-2_report.md:228-248` |
| P44 | **Covariant CQ, narrowed (refines P33).** Remaining escapes: correlated, emission-cancelled (non-Markovian) noise histories; or a preferred frame with an integer n ≥ 3 UV kernel and a regulator at the cone | Admissibility `AX:60-61`: the distribution is "determined by ... nearest-neighbor conditions". History-dependent noise must be carried by present conditions. Permanent records (`AX:80`) are one possible carrier [S11 reading]. A preferred frame adds a frame to the law | A | `TESTS:3909-3915`; `vR9-4:15` |
| P45 | **Sector selection for qubits.** The qubit realization holds on the flux-free invariant sum only. Visons are static; σ^z exits the sector; no plaquette threshold is proved for all flux configurations; index-2/C4 covariance price | Qubit `AX:47` is met literally (one qubit per site). But choosing the flux-free sector privileges states unless an energy gap selects it: "No possibility is privileged" `AX:52`; "A law privileges no states" `AX:94` [S11 reading] | C-box | `TESTS:3917-3923`; `vR9-5:12,21` |

**[S11 reading] How the price structure shifted since S8.**
- **C-box's matter prices are paid and bought something real** (P35, P36, P45): exact kinematics and exact uniform-field universality for bound bodies.
- **Its field prices** (P37–P41) **buy nothing yet at one loop.** If R10-1 is confirmed, C-box at one loop costs C's tunings plus C-box's structural prices. Only P42 (pairing) could change that.
- **Set A** narrowed to two escape classes (P44).
- **Set B** may lose the box trick altogether (P43, pending).

---

## 4. The decision this campaign is converging to (for Jon; named options, nothing adopted)

**The question in one line [S11 reading].** Grid relativity can be made exact for matter but not for loops. Something must pay for the loops: tunings, a continuum, or a boson–fermion structure on the grid.

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, an exact equivalence principle, no LV tunings.
- *Pays:*
  - the set-A axiom prices (Lattice becomes points of a continuum; bounded-region algebras infinite-dimensional; `C5_S5_synthesis.md:94`);
  - a supplied graviton, or the records as a classical metric (P32), Newtonian-viable only;
  - covariant completion via P44 (R10-3 pending);
  - Λ as a premise (R10-4 pending).
- *Still open:* whether A's records do any relativistic gravitational work.

**Option C: keep the four texts and tune.**
- *Buys:* no axiom text changes.
- *Pays:*
  - at least 6 one-loop conditions (reading, `SUMMARY:436`);
  - F2's 3.1e-17;
  - b₀ at 43–49 decades (worker, unrefereed);
  - Λ to 1e-123;
  - a graviton supplied through the N-type bridge.
- *Still open:* the full count (R2's lane INCONCLUSIVE).

**Option C-box: keep Z³, a box-exact law, qubits in a sector.**
- *Buys:* exact relativity and exactly universal uniform-field fall for number-conserving matter inside a rapidity budget (about 45 for a proton at Planck spacing, a reading on `AX:189-190`).
- *Pays:* P26–P29 and P35–P41, P45. **At one loop, if R10-1 is confirmed, it also pays C's count.**
- *Honest status [S11 reading]:* without a further structure, C-box is option C with exact tree-level kinematics. The box changes the size of each tuning, not their number (pending).

**Option C-box-S: C-box with an edge supertrace (boson–fermion pairing on the edge).**
- *Would buy:*
  - removal of the photon's one-loop shift (Theorem P, pending);
  - possibly the electron's and the graviton's (R10-5);
  - possibly the vacuum energy's one-loop cancellation (O3's matched spectra).
  - [S11 reading] That would be one structure paying for two first-class problems.
- *Pays:* P42 (8-component fermions plus bosons per cell; partner loops; two-loop stability). It also needs a qubit realization of bosons, which O3 excludes on-site for free fields. FS-type interacting lattice SUSY is the known escape.
- *Still open:* everything beyond the photon.

**Off the table on present evidence [S11 reading].**
- **B:**
  - pending R10-2: box symbols are not RP;
  - γ ≤ ½ binds;
  - 11 (or 5 + Λ without RP) graviton tunings.
- **B′:** no long-distance law; δΛ too large (as S8).
- **E:** unbuilt in 4D (as S8).

**Owner questions this exposes (unanswered here).**
1. **The sector.** Is a dynamically invariant sector (flux-free), selected by hand or by an unproved gap, acceptable as "the physical sector"? (P45; `AX:52,94`)
2. **The budget.** Is relativity exact inside a finite rapidity budget (a local Lie-algebra domain, not integrated covariance) acceptable as "relativity"? (P26b)
3. **The range.** Must the law's range be nearest-neighbour? `AX:116-130` leave dynamics downstream; every box law is super-polynomially, not exponentially, local. (P26a, P37)
4. **The pairing.** Is a graded boson–fermion structure per cell a price Jon would consider? (P42; it touches Qubit `AX:47`.)

**Honestly open whichever option is chosen.**
- **Producing the graviton.** Every set supplies it.
- **Λ's mean.** A premise everywhere.
- **The full linearized gravitational coupling of box bodies** (space–space and tidal).
- **N ≥ 3 closure** in the box.
- **Whether R10-1's "count equals C's" survives refereeing.** A class-wide no-go is not proved (R8-5, R9-8 and R9-9 are all bounded or INCONCLUSIVE).

---

## 5. Big open problems, ranked by leverage

"Leverage" = how far a definite answer moves the choice among A, C, C-box and C-box-S. The three hard problems (edge anomaly, graviton production, Λ's mean) are ranked first-class.

1. **The edge anomaly, class-wide.**
   - *Decides:* whether C-box differs from C at all beyond tree level, and whether pairing is the only exit.
   - *State:* see §1.2–1.3. R10-1 pending; R10-5 running.
   - → **R11-1** (the converse of R10-5: is pairing necessary? plus the dressed matter speed from graviton loops).
2. **Producing the graviton (first-class).**
   - *State:* every set OPEN (R6-2). The weak N-type theory has two linear TT modes and a 1/r pull (`SUMMARY:290`). Its box version is exact at tree level with a Ward-exact matter coupling (R9-9). The named decisive test, a qubit realization, has never been run (`SUMMARY:290`).
   - → **R11-2.**
3. **Λ's mean (first-class).**
   - *State:* a premise everywhere; R10-4 tests set A. Never asked for the grid sets: what is the universe's volume mode on a fixed Z³, and does the vacuum source it?
   - → **R11-3.**
4. **The full gravitational coupling of box bodies.**
   - *State:* only the uniform-field first-moment lapse has been tested. The space–space coupling (γ, light-bending-type) and the tidal and spin–curvature terms have not.
   - → **R11-4.**
5. **Covariant records-as-metric (set A).**
   - *State:* (iii) R10-3 running.
   - → **R11-5** for (iv), the preferred frame.
6. **N ≥ 3 closure with lattice tails.**
   - *State:* the physical question is INCONCLUSIVE because the operators were never assembled (R9-3).
   - → **R11-6** (re-registered without the defect).
7. **Two-loop closure in the fixed box** (R9-7's open item). Lower leverage: Lemma C pushes gauge vertices onto the whole zone anyway. Revisit after R10-5. No item.
8. **The qubit sector gap and a d = 3 qubit realization** (R9-5). No item; it matters only if C-box survives.
9. **Edge cosmology** (G relic, reheating cap). No item.
10. **B, B′, E.** No item (R10-2 pending).

---

## 6. Draft round-11 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–10).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Numbers from memory are labelled RECALLED unless verified.
- **New rule (from R9-3's defect).** Every tail or decay clause names its subtraction (which channel limit is subtracted) before any run.

**Overlap check.**
- R10-3 is emission-cancelled CQ (variant iii). R11-5 is variant (iv) only.
- R10-4 is set A (free volume, records as q-charge). R11-3 is sets C and C-box (fixed grid). It does not test records as a q-charge.
- R10-5 builds the edge-SUSY law and computes c_e − c_γ, the graviton TT speed with partners, and the one-loop vacuum energy. R11-1 asks the converse (is pairing *necessary*?) and computes the matter self-energy from graviton loops, which R10-5 does not.
- R11-2, R11-4 and R11-6 overlap nothing running.

**Priority.** R11-1 (after R10-1's referee), R11-2, R11-3, R11-4, R11-5; R11-6 when a slot frees.

---

**R11-1. Is an edge supertrace necessary? And the dressed matter speed under graviton loops.**
*(Launch after R10-1's referee. If Theorems T′, P or Lemma N(m) are not confirmed, use only refereed Theorem T and prove T′ inside the probe.)*

- **Plain question.** The box route's one-loop light-speed shifts all live on the edge. R10-1's worker found one way to cancel one of them: bosons and fermions contributing with opposite signs. Is that the *only* untuned way, or can some edge shape or vertex choice do it without pairing? Separately, R9-9 computed the graviton's speed shift but not the matter's shift from graviton loops. Without it, "graviton and matter on different cones" is not yet a computed fact.
- **Setting (class 𝒞_A).**
  - Z³ × ℝ, continuous time, Gaussian matter species s with C² periodic bands, box-exact on an open box (H-box, `C5_R10-1_report.md:67-96`).
  - Gauge and graviton vertices are Ward-forced onto the whole zone (Lemma C `TESTS:3808`; Lemma Q `TESTS:3841`).
  - Species are complex scalars or Clifford-flat fermions, the subclass in which each one-loop coefficient is a signed A-moment.
  - "Untuned" means: band shapes and vertices are fixed per statistics and do not depend on the observable or the mass.
  - Excluded: the Dirac class (D) with non-zero a- and mixing-moments (stated as outside); interactions beyond one loop; set C's own discretization.
- **Prior art (count once).**
  - R8-2 Theorem E (`TESTS:3556`);
  - R9-9 Theorem T and Lemma N with its richness caveat (`vR9-9:12-14`);
  - R10-1 Theorems T′, D, P and Lemma N(m) (pending, `C5_R10-1_report.md:137-260`);
  - O3 Theorem 1a, equal signed DOS (`TESTS:2400`);
  - R10-5 (running; do not duplicate its construction);
  - Nielsen–Ninomiya (RECALLED).
- **Probes.**
  - (a) **Necessity.** Suppose C_O(m) = 0 for every m² in an interval and every O in {photon speed, graviton TT speed}, with no per-O tuning. Prove or refute: the species' band pushforward measures must pair across statistics, observable by observable. A counterexample must be explicit and checked.
  - (b) **Dressed matter speed.** Compute the one-loop matter (scalar) self-energy from R9-9's tree-level box graviton, on the L and G edges, at m = 1 and 0.3. Give c_matter − c_T at one loop, including R9-9's Ξ, in units of κ_lat²/(16π²a²). State the size at a = ℓ_P (a reading on `AX:189-190`).
  - (c) Restate the one-loop count with and without pairing. Note any change from R10-1's referee.
- **FIXED readings.**
  - (a) uses the derivation readings (`TESTS:2314-2318`):
    - **DERIVED:** pairing is necessary in 𝒞_A, proved (refereed);
    - **REFUTED:** an explicit unpaired untuned choice nulls both coefficients for all m² in an interval, checked;
    - **SUGGESTED:** otherwise.
  - (b) is reported as:
    - **SPLIT-PRESENT:** c_matter − c_T ≠ 0 computed for both edges, with the number;
    - **SPLIT-ABSENT:** it vanishes identically, with the reason;
    - **OPEN:** otherwise.
    - A SPLIT-PRESENT claimed as class-wide goes to the referee.
- **Expectation.**
  - (a) DERIVED in 𝒞_A. The mass-independence plus Laplace uniqueness argument of Lemma N(m) should force equality of signed measures, as O3's Theorem 1a does for vacuum energy. SUGGESTED beyond 𝒞_A.
  - (b) SPLIT-PRESENT, sign-definite on the gapped edge (A_zz ≤ 0 there, `vR9-9:12`), unsuppressed at a = ℓ_P.

---

**R11-2. Producing the graviton: a qubit realization of the weak N-type box graviton, and Weinberg–Witten on box domains.**

- **Plain question.** In every set the graviton is put in by hand. Lane R found one gauge structure on Z³, the weak N-type (Gu–Wen "weak" type), with two light-like graviton modes and a 1/r pull. R9-9 gave it a box law that is exact at tree level and couples exactly to box matter. The decisive test named in `SUMMARY:290` was never run: can one qubit per site, with local terms only, *produce* that field as its low-energy sector, the way R9-5 produced box matter? And does Weinberg–Witten, which forbids composite gravitons, apply when boosts are exact only inside a budget?
- **Setting.**
  - ⊗_{Z³} M₂(C), local or super-polynomially quasi-local terms.
  - The constraints are enforced energetically (stabilizer- or ice-type) or as invariant sectors (R9-5 style). At linear order the N-type constraints commute, as linearized diffeomorphisms are abelian (RECALLED; verify in the probe).
  - The target is R9-9's tree-level box graviton: an exact linear constraint algebra, 2 TT modes with ω = |q| in the box (or ω ∝ |q| at low q), no doubler (`TESTS:3940-3944`).
  - Matter: R9-5's flux-free fermion sector, or constraint violations (defects).
  - Excluded: nonlinear gravity; pair-creating matter; Λ.
- **Prior art (count once).**
  - lane R, `TESTS:685-776`, notably R1 and R2 at `:740-760`: "V gives k², VS gives k³ in the regular analytic compact class"; "a noncompact IR field can emerge from qubits"; strong-class mode counts 5/4/3/2;
  - the 09-14 note (`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`);
  - PR #9363 probes 10–21;
  - R6-2 (`TESTS:3331-3343`);
  - R9-9 (`TESTS:3939-3950`); R9-5 (`TESTS:3917-3923`);
  - `OUTSIDE_VIEW.md:46,49` (Gu–Wen, Xu, Pretko);
  - Gu–Wen 2009 helicity-±2 model, Xu 2006, Pretko 2017 (RECALLED).
  - Read every section naming "N-type" or "weak VS" before building.
- **Probes.**
  - (a) **WW on box domains.** Does the Weinberg–Witten proof go through when finite boosts act exactly only on a budget-limited domain? This covers (i) a composite spin-2 state made of box matter and (ii) a gauge graviton without a gauge-invariant stress. State which step uses unbounded boosts.
  - (b) **Construction.** Build the cheapest ⊗M₂ Hamiltonian whose constraint-satisfying low-energy sector carries the N-type gauge structure. Compute its emergent dispersion (perturbative ring exchange or exact sector map), its mode count, and any extra helicity-1 or 0 modes.
  - (c) **Box symbol.** Can the box trick (R9-9's d(q)) be applied to the emergent field's effective symbol? Or is the emergent dispersion fixed by the constraint structure (k² or k³, as lane R found)?
  - (d) **Source.** Do matter excitations source the emergent field through their energy-momentum (universal, Ward-exact) or through an emergent charge (lane R's failure mode)?
  - (e) Name the prices.
- **FIXED readings.**
  - **PRODUCED:** an explicit ⊗M₂ quasi-local model whose stated low-energy sector contains exactly two TT modes, light-like in a box (or at low q), with the N-type constraint algebra, no extra gapless modes, and matter coupling through a Ward-exact universal stress, checked.
  - **EXCLUDED:** a refereed no-go that, in a stated class of ⊗M₂ constraint models on Z³, the emergent tensor field is never light-like or never couples to energy-momentum.
  - **OPEN:** otherwise. Report (a) separately as DERIVED / REFUTED / SUGGESTED.
- **Expectation.**
  - (a) SUGGESTED: WW binds composite TT states built from box matter inside the budget; it does not bind a gauge graviton, as in GR.
  - (b)–(d) OPEN. Most likely an emergent field with k² or k³ dispersion, or one sourced by an emergent vector or fracton charge rather than by energy. A light-like N-type sector from qubits would be the campaign's first produced graviton.

---

**R11-3. Λ's mean on a fixed grid: the volume mode, the vacuum's tadpoles, and its equation of state (sets C and C-box).**

- **Plain question.** On a continuum (set A), space can expand freely. On the axioms' Z³ the sites are fixed. So what is the universe's expansion on a grid? Either the proper spacing grows, making the volume a field, or new sites appear, a price on Lattice. Does the vacuum energy push on that volume mode? If space's volume per site were fixed, the vacuum's energy might stop gravitating, as in unimodular gravity. Separately, a grid vacuum need not have pressure equal to minus its energy (w = −1). If it doesn't, it is not a cosmological constant at all, and cancelling it costs two numbers, not one.
- **Setting.**
  - R9-9's N-type box graviton (lapse N, shift N_i, h_ij) on Z³ × ℝ, coupled to R8-2's stress with R9-2's supplied scalar zero-point completion, on the L and G edges. Add a Dirac sea if feasible, gapped edge only (P38).
  - Three options for the volume mode:
    - (V1) the trace h_ii is dynamical (spacing grows);
    - (V2) √h is fixed per site (a "spatially unimodular" grid), lapse dynamical;
    - (V3) the lapse is also fixed (a projectable, preferred-time grid).
  - Excluded: records as a q-charge (R10-4); edge-SUSY (R10-5; use its vacuum result only as a control if it has reported).
- **Prior art (count once).**
  - R5-3 route 1 (unimodular with Λ an integration constant; `TESTS:2888-2889`, result `:2985-2993`);
  - lane RN's "TDiff, unimodular, Hořava are not escapes" (for the graviton's mass, `TESTS:809,870`; a different question, counted once);
  - R9-2 free shear (`TESTS:3897-3900`);
  - O3 (`TESTS:2399-2404`);
  - R4-5 everpresent-Λ unimodular conjugacy (`TESTS:2939`);
  - `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` and every repo doc on the cosmological constant;
  - comparator: momentum-cutoff vacuum w = 1/3 (Akhmedov; Koksma–Prokopec; RECALLED).
- **Probes.**
  - (a) **Tadpoles.** Compute ⟨T⁰⁰⟩_vac and ⟨T^ij⟩_vac (isotropic p_vac; anisotropic part = R9-2's shear), split into box and edge contributions, for L and G. Give w = p_vac/ρ_vac for each part, and test whether any edge profile gives w = −1 without tuning. State any zone-integral identity relating ρ_vac + p_vac to A-moments.
  - (b) **Decoupling.** For each of V1–V3, does a step change in ρ_vac (a phase transition: change one species' m) source curvature or expansion? Derive it in the linear N-type theory.
  - (c) **Expansion.** For each option, state how a FRW-like expansion is realized: growing spacing, site creation, or none. Give the consequence for the rapidity budget in physical units and for the scale reference (`AX:189-190`).
  - (d) Name the prices per option.
- **FIXED readings (per option V1, V2, V3).**
  - **DECOUPLED:** vacuum-energy shifts, including a phase-transition step, provably do not source curvature or expansion; the residual Λ is named as an integration constant, and prices are named.
  - **SOURCED:** the vacuum sources the volume or lapse mode with computed coefficients (ρ_vac, p_vac, w stated). The mean remains a tuning. If w ≠ −1 is claimed to cost two tunings, that goes to the referee.
  - **EXCLUDED:** the option is inconsistent with observed expansion or with the N-type constraint algebra (refereed).
  - **OPEN:** otherwise.
- **Expectation.**
  - V1: SOURCED, with the edge part's w ≠ −1, so two tunings (ρ and p) instead of one.
  - V2: SOURCED through the lapse, since ρ_vac√h still enters the Hamiltonian constraint.
  - V3: DECOUPLED at linear order, but EXCLUDED or OPEN on expansion: a fixed grid with fixed lapse cannot expand without site creation, a Lattice price, which links to the owner's "count rises" thought, tested only as a hypothesis.

---

**R11-4. Box bodies in a curved field: the space–space coupling (γ), von Laue, geodetic precession and the spin–curvature force (d = 3).**

- **Plain question.** Every gravity test of box bodies so far used a uniform field coupled to the energy's first moment. Light bending, Shapiro delay and the precession of a spinning gyroscope test the rest of the coupling: how a body's internal pressure and momentum flow respond to curved space. A bound body at rest has zero total internal stress (von Laue's condition) only if its momentum is exactly conserved. In the box law momentum is conserved only box-to-box. Does the condition still hold, and does a spinning bound body precess at GR's rate?
- **Setting.**
  - R9-6's d = 3 two-body triplet law (`TESTS:4016-4024`).
  - A d = 3 symmetric stress built as in R9-10 (Weyl midpoint plus KB/Belinfante division).
  - Linear coupling ½h_μν T^μν to prescribed static fields: (i) uniform lapse (control); (ii) isotropic linearized Schwarzschild, h₀₀ = −2Φ, h_ij = −2γΦδ_ij with γ = 1; (iii) a pure tidal field; (iv) gravitomagnetic h₀ᵢ.
  - Fallback if the d = 3 stress is not constructible in time: d = 2 for von Laue and tidal only, with that stated.
  - Excluded: pair creation; N ≥ 3; nonlinear gravity.
- **Prior art (count once).**
  - R9-2 (`TESTS:3889-3900`); R9-10 (`TESTS:4037-4044`, the unmet GR-spin clause `vR9-10:21-22`); R9-6;
  - R8-2's stress (`TESTS:3554`); R7-4's conditional exclusion (`TESTS:3496-3497`; `vR9-2:17`);
  - comparators: Gravity Probe B geodetic precession (3/2, about 0.3%), Cassini γ, Mathisson–Papapetrou–Dixon force, von Laue's theorem (RECALLED unless verified).
- **Probes.**
  - (a) Construct the d = 3 stress: symmetric, Hermitian, quasi-local, ∫T⁰⁰ = H, first moments K and J, box-to-box momentum conservation, sources stated.
  - (b) **Von Laue.** Is ∫T^ij = 0 for bound states at rest, exactly on the box domain? Compute any shell-source contribution as a function of binding.
  - (c) The passive coupling to (ii): the acceleration and the effective γ of bound bodies of two binding fractions, at rest and moving within the budget.
  - (d) The geodetic precession of the triplet's spin in (ii), against 3/2; the MPD force in (iii); the frame-dragging response to (iv).
- **FIXED readings.**
  - **PASS:** (a) met; von Laue exact on the box domain; the effective γ is binding-independent and equal to 1 at linear order; geodetic 3/2 and the MPD force reproduced, checked.
  - **FAIL:** a computed binding-dependent γ or a precession ≠ 3/2 at linear order that no choice in a stated class removes (refereed).
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** PASS on the box domain. Von Laue follows from box-to-box momentum conservation for stationary bound states, and 3/2 follows from ½h_μνT^μν with a symmetric von-Laue stress (S11 expectation). The risks: the second moments (x² weights) needed for tidal and MPD terms may reach the shell sources, and the d = 3 global quasi-local flux may again be existence-only. INCONCLUSIVE overall is likely.

---

**R11-5. Set A: a regulated preferred-frame CQ kernel and its window (R9-4 variant iv).**

- **Plain question.** The simplest relativistic forms of "the records are the classical metric" are excluded. One open form keeps a preferred frame, with noise tied to it. That needs a UV power n ≥ 3 and a regulator at the light cone. Build one, then ask whether any smearing length survives every bound, including effects of Earth's motion through the frame.
- **Setting.**
  - Linearized Gaussian CQ gravity with mean GR coupling and noise kernel D(ω, k) defined in a preferred frame u^μ (taken as the CMB frame).
  - Integer n ≥ 3 UV falloff. An explicit regulator or restricted domain at the cone, making D′₀ a locally finite positive measure.
  - Spatial smearing ℓ_s.
  - Excluded: correlated emission-cancelled histories (R10-3); trace-only kernels already excluded (`TESTS:3911-3912`).
- **Prior art (count once).**
  - R6-4 (`TESTS:3409-3418`); R8-3 (`TESTS:3559-3573`); R9-4 (`TESTS:3909-3915`; `vR9-4:11`);
  - R4-4 Lemma N (a BMV-type positive result excludes every variant, `TESTS:2935`);
  - PPN preferred-frame bounds α₁, α₂ (RECALLED; verify).
- **Probes.**
  - (a) Construct the regulated kernel. Prove complete positivity and the mean-field limit.
  - (b) Compute γ, c_T, the vacuum-excitation rate in the frame, and the heating and diffusion rates for matter moving at v ≈ 370 km/s through the frame, including their annual modulation.
  - (c) Compare against:
    - R6-4's decoherence and diffusion bounds (Cs-133 for 70 s; LISA Pathfinder; corrected torsion σ_a² = (48π/5)G²D₂/(RT));
    - Cassini;
    - GW170817;
    - PPN α₁, α₂, if the noise feeds the mean metric at any order.
  - (d) Give the allowed ℓ_s interval, or none.
- **FIXED readings.**
  - **VIABLE:** an explicit regulated kernel passing every stated test, with an allowed ℓ_s interval and named prices.
  - **EXCLUDED:** every regulated kernel in a stated class violates a stated bound for every ℓ_s (refereed).
  - **OPEN:** otherwise.
- **Expectation.** OPEN, leaning VIABLE on a narrow interval inside 2e-7 to 5e-6 m. The new risk is the velocity-dependent heating and its annual modulation, which no earlier probe computed.

---

**R11-6 (when a slot frees). Assembled Sokolov three-body box law with subtracted channel tails (R9-3 re-registered, d = 1).**

- **Plain question.** For three bodies, summing pair forces breaks relativity, and the textbook cure (Sokolov packing) was never assembled on the lattice. R9-3's registration also asked for the impossible. Assemble the operators and measure the right tails.
- **Setting.**
  - d = 1; three spinless fermions; R8-1's pair law with R7-6's plateau; the normalization ½ (`TESTS:3797`).
  - A stated interpolation or discretization prescription for P ≠ 0 rings (`vR9-3:110`).
- **Prior art (count once).** R7-6 (`TESTS:3506-3510`); R9-3 (`TESTS:3902-3907`; `vR9-3:3,26,43,110`); Keister–Polyzou, Coester–Polyzou (as cited there).
- **Probes.**
  - (a) Assemble B, H_S = B H_BT B†, K_S on the three-body box sector, on at least three ring sizes.
  - (b) Check [K, P] = iH, [K, H] = iP, [H, P] = 0.
  - (c) **Subtracted tails (fixed now).** For the spectator channel a = (12)(3), measure ‖(B − B_a)ψ_r‖ and ‖(H_S − H_a ⊗ 1 − 1 ⊗ h₃)ψ_r‖ against separation r over at least 1.5 decades. Use a pre-registered information-criterion comparison of exp(−c r^β) against a power law, over the full range.
  - (d) The trimer invariant mass at P = 0, ±P₁, ±P₂.
- **FIXED readings.**
  - **PASS:** (b) residuals → 0 with L; (d) flat to the discretization floor; (c) super-polynomial by the pre-registered comparison; checked.
  - **FAIL:** a refereed proof that the *subtracted* channel deviations decay no faster than a power, in a stated class.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. The algebra closes by construction; the subtracted tails should track the form-factor proxies (`vR9-3:43`), but a uniform operator bound is unlikely within one run.

---

## 7. Caveats

- **Same family, unrefereed.** The C-box/C-box-S option split, every "[S11 reading]" cell, the "common cause" synthesis in §1.3, the price numbering P35–P45, the rankings and the R11 drafts are S11's.
- **Pending.**
  - R10-1's Theorems T′, D, P, the localization lemma and the "count equals C's" reading are worker claims.
  - R10-2's Lemmas A and B and its FAIL reading are worker claims.
  - R10-3, R10-4 and R10-5 have no verdict, and their content was not used.
  - If the R10-1 referee rejects Theorem D or P, §1.3 items 3–6, P42, option C-box-S and R11-1(a) must be revisited.
- **Bounded, not class-wide.** R8-5's FAIL holds in its gauge-generator class only. R9-8 and R9-9 are INCONCLUSIVE. **No refereed result yet says the edge anomaly is unremovable in general.**
- **Scale bridge.** Every Planck-unit statement (rapidity budgets, the T ≈ 3.52e17 GeV crossing, R11-1(b)'s size) uses a = ℓ_P, which the axioms leave open (`AX:189-190`).
- **The sets are not exhaustive** (as S5 and S8). Relational and non-commutative constructions are unexamined.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items. R11-1 should wait for R10-1's referee.
