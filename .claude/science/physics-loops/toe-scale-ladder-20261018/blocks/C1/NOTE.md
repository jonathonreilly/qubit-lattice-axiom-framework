# C1 — Sign-free, guide-free QMC of the cubic spin-1/2 link ring model: stoquasticity proved, Coulomb-vs-confined from the winding gap (string tension bounded, Coulomb not established), structure-factor criteria not evaluable (mixing failure)

**Block:** `toe-scale-ladder-20261018 / C1` (target: SCALE_LADDER_MAP.md, "C1", OBL-R2.1).
**Claim types used below:** [THM] proved statement with exhaustive finite certificate; [NUM] numerical
evidence from the QMC of this block; [EXT] repo result from a different code, not verified here;
[LIT] literature, recalled from memory, not re-checked; [VERDICT] application of pre-declared criteria.
**Status:** unaudited block output; no independent check has been done yet (see §9).
**Merges** `NOTE_part1_stoquastic.md` (§1–2) and `NOTE_part2_method.md` (§3). The full history,
including the times when criteria were declared, is in `WORKLOG.md`.

---

## 0. Bottom line

1. [THM] On every even cubic torus, for any static background, the ring Hamiltonian is stoquastic in the
   Gauss-legal σ^z basis for either sign of g. A diagonal ±1 gauge maps H(g) to H(−g). For odd L no diagonal
   gauge does this.
2. [THM] A local-update finite-temperature trace (worldline) code conserves a flip-class label and so does not
   sample Tr e^{−βH}. The L=2 control shows a large bias: E = −7.95 vs −9.02.
3. [NUM] The guide-free open-path projector built here reproduces exact L=2 results (W=0 and W=1 sectors) within
   3σ in 12 of 13 checks. The single failure was resolved as statistical by fresh chains, and both results are
   reported.
4. [NUM/VERDICT] **Middle-of-path structure factors do not equilibrate for L ≥ 6.** They depend on the start
   state, and at L=8, T=32 E_mid differs from E_mix by about 100σ. The pre-declared S_T exponent, Bragg and
   photon-velocity criteria **cannot be evaluated**. This is a method failure, not a physics result.
5. [NUM/VERDICT] The guide-free electric-winding gap ΔE(L) = E0(W=1) − E0(W=0) at V=0 (see the table in §5)
   shows **no string tension**. The fitted σ is FILL, and the pure σL law is rejected (χ² FILL). The
   pre-declared Coulomb form A/L fits, but so do the post hoc forms B/L² and const. The data **do not establish**
   Coulomb ∝1/L scaling. Verdict at V=0: **confined-with-resolvable-string-tension disfavoured; Coulomb
   consistent but not decided (inconclusive at accessible L)**. At V=0.5 and 0.9 the results are inconclusive, and
   the V=0.9 points show insufficient projection.

---

## 1. Supplied model (named premise)

Conventions are taken from
`docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_DECONFINED_AND_UNORDERED_AT_L_12_WITH_A_QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_BOUNDED_NOTE_2026-09-04.md`
(Definitions block) and from the runner of
`docs/RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`.

- Lattice and fields: periodic cubic torus L³, one spin-1/2 per link, E_l = σ^z_l/2, U_l = σ^+_l.
- Gauss law: G_v = (div E)_v − ρ_v = 0, with **ρ_v = 0 on every cubic torus** (3 in / 3 out). The repo's
  staggered background 2ρ = ±(−1)^i is declared only for the 2D *ladder*, so the task's phrase "staggered
  background" does not apply to the cubic torus. The exact statements in §2 hold for any static background.
- Hamiltonian: H = −g Σ_p (U_p + U_p†) + V Σ_p n_p, where n_p = 1 if p is flippable. Units g = 1; the RK point
  is V = g.
- Sectors: **W=0** is the flip component of the repo canonical state (σ_x = (−1)^y, σ_y = σ_z = (−1)^x).
  **W=1** is the flip component of that state with the directed x-line (y=0, z=0) reversed. This is one quantum
  of E-flux in the E = σ/2 normalisation; the repo's 09-24/09-25 notes call it q=1, W=(2,0,0).
- Frozen components exist on every even torus
  (`docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md`).
  All statements below are about these two specific flip components, not about whole winding sectors. At L=2
  the canonical component (864 states) contains the global W=0 ground state, and the W=1 seed component has
  464 states, matching the repo's sector ground energy −7.399111.

## 2. Stoquasticity [THM]

**Theorem 1.** For every L ≥ 2 and every static background, in the basis of Gauss-legal σ^z configurations:
- ⟨s'|H|s⟩ = −g if s' = F_p s for a flippable plaquette p;
- ⟨s'|H|s⟩ = 0 for every other s' ≠ s.

Hence H is stoquastic for g ≥ 0.

*Proof.* U_p is the oriented product s⁺s⁺s⁻s⁻ on the four links of p. Spin-1/2 ladder operators have matrix
elements in {0,1}, so U_p + U_p† maps |s⟩ to |F_p s⟩ with amplitude 1 if p circulates in s, and to 0
otherwise. Distinct plaquettes have distinct link sets (checked for L = 2, 3, 4, 6, 8, 10, 12; immediate for
L ≥ 3), so no matrix element is a sum of two terms. The V term is diagonal. ∎

**Theorem 2 (sign of g, even L).** Let Λ = {x-links (v,x) with y+z even} ∪ {y-links (v,y) with z even}, and let
D = Π_{l∈Λ} σ^z_l. Every plaquette contains an odd number of Λ-links. Therefore D (U_p+U_p†) D = −(U_p+U_p†)
for all p, and D H(g,V) D = H(−g,V). D is diagonal, so it preserves the Gauss law, every winding sector and
every flip component.

*Proof.* There are three plaquette orientations.
- xy-plaquette: its two x-links have y+z of opposite parity, so exactly one is in Λ. Its two y-links have the
  same z, so both or neither are in Λ.
- yz-plaquette: its y-links sit at z and z+1, so exactly one is in Λ. It has no x-links.
- xz-plaquette: its x-links sit at (y,z) and (y,z+1), so exactly one is in Λ. It has no y-links.

In every case the count is odd. Periodicity of Λ needs L even. ∎

**Remark (odd L) [THM].** For odd L no diagonal ±1 gauge maps g to −g. The xy-plaquettes of one plane form a
mod-2 2-cycle, so Σ_p |Λ∩∂p| over that plane is even for every Λ. A gauge would need it to equal L² mod 2,
which is odd. The cubic condition 6π ≡ 0 is therefore necessary but not sufficient; the global plane classes
also matter. In any case, odd L has an empty zero-winding sector.

**Certificate.** `scripts/step1_stoquastic.py` writes `logs/step1_stoquastic.log` and ends
`TOTAL: PASS=26 FAIL=0`. It checks:
- the odd-count property for L = 2..12;
- an independent GF(2) solve of δΛ = 1, which is consistent for L = 2, 4, 6 and inconsistent for L = 3, 5;
- exact L=2: 9600 Gauss states, 937 flip components, largest 864 (repo values); all off-diagonals equal −1;
  D H(+g) D = H(−g) exactly; spectra of H(±g) agree on all 937 components to 7e−14 for V = 0, 0.5, 0.9;
  E0(V=0) = −9.0267209135 (repo value).

**Consequence.** Path weights g^n exp(−V∫N_flip) are nonnegative for either sign of g on even tori. There is no
sign problem in any winding sector.

## 3. Method

### 3.1 Local finite-T trace codes are class-restricted [THM + NUM]

**Lemma 3.** Let n_p be the net signed number of flips of plaquette p over one period of a periodic worldline.
The chain n = Σ n_p p is a 2-cycle. Pair insertions and removals of consecutive opposite flips, and time shifts,
leave every n_p unchanged. So a local-update trace code samples only the class n = 0, whereas Tr e^{−βH} sums
over all classes (cube boundaries and three global plane classes).

*Proof.* Consecutive flips of one plaquette, with its links unchanged in between, alternate sign. ∎

Control: L=2, exact thermal trace on the 864-state component (`logs/step2_validate_L2.log`, [INFO] lines).

| V | β | QMC E | exact E | N_flip z |
|---|---|---|---|---|
| 0 | 4 | −7.95 | −9.02 | +6.9 |
| 0.5 | 4 | −3.08 | −4.24 | — |

### 3.2 What is used: guide-free open-path projector (PIGS type), continuous imaginary time [construction]

The sampled quantity is Z(T) = ⟨1|e^{−TH}|1⟩, with the uniform vector |1⟩ on the flip component at both ends.
There is no importance function. The weights are nonnegative (§2), and the middle τ = T/2 is distributed as
|ψ_{T/2}|². Moves, all detailed-balanced (`scripts/qmc.py`, numba):
- pair insertion and removal;
- single-kink time shifts;
- single-kink insertion and removal at either free end. These change the end states, so there is no class
  restriction.

The V weight is integrated exactly piecewise. `delta_toggle_fast` is bit-identical to the reference
implementation on 8524 random intervals (`logs/test_delta_fast.log`).

Estimators:
- **Mixed energy** E_mix = (V−g)⟨N_f(end)⟩. This is exact for the uniform trial state, because
  (H|1⟩)(s) = (V−g)N_f(s), and it equals ⟨1|He^{−TH}|1⟩/Z. It is a Rayleigh quotient of ψ_{T/2}, so in
  expectation it is ≥ E0 of the component and decreases monotonically in T.
- **Middle-state observables:** S_T(k), flippability and E-field spectra, and E_mid.
- **Imaginary-time transverse correlator.**

E_mid and E_mix estimate the same exact number, so E_mid − E_mix is a parameter-free equilibration test of the
middle of the path.

### 3.3 Sampler bug found and fixed (disclosed)

The first version made a number of moves per sweep that depended on the current state. This biased the kink
count low by 1.5–3% (z down to −4.5 against ⟨n⟩ = gT⟨N_f(end)⟩). The number of moves is now frozen after
thermalisation. After the fix, the exact fixed-end P(n) at T=0.3 is reproduced:
0.1675/0.2002/0.2403/0.1807 vs exact 0.1665/0.1998/0.2397/0.1798.

### 3.4 Exact validation at L=2 [NUM]

- **W=0** (`scripts/step2_validate_L2.py`, `logs/step2_validate_L2.log`, `TOTAL: PASS=8 FAIL=1`): seven open-path
  cases with V ∈ {0, 0.5, 0.9} and T from 1 to 8, four chains each. Observables checked: E_mix, N_f(mid),
  N_f(end), S_T, the windowed kinetic energy and C(τ).
  - The failure is V=0.9, T=3: N_f(end) z = −3.1.
  - Six fresh chains then gave z = −0.3 (`logs/dbg_vend.log`, a debug log without a TOTAL line). This is read as
    long autocorrelation near RK. Both results stand.
- **W=1** (new, `scripts/step3_validate_W1_L2.py`, `logs/step3_validate_W1_L2.log`, `TOTAL: PASS=4 FAIL=0`).
  The reference is built independently: BFS from the production W=1 seed (464 states, disjoint from W=0), then
  dense diagonalisation.
  - V=0, T=4: E_mix −7.4015(105) vs −7.3991.
  - V=0.5, T=4: E_mix −3.5250(66) vs −3.5244.
  - Exact L=2 gap: ΔE = 1.62761 at V=0 and 0.73146 at V=0.5.
- **Reproducibility hazard (found at resumption).** `driver.Sim` now interprets seed ≥ 100 as a W=1 start.
  The logged step-2 run (finished 19:49) predates that change (driver.py modified 20:00), but step 2 uses seeds
  101–128. **Re-running `step2_validate_L2.py` with the current driver would start its chains in the W=1 sector
  and fail.** Its seeds must be moved below 100 before re-use. The log as recorded is valid for the code at the
  time.

## 4. Pre-declared criteria (copied; see WORKLOG for timestamps)

Declared 18:56 UTC, before any production data:
- S_T(k_min) exponent p from the two largest L. Coulomb: p ∈ [0.6, 1.4]. Ordered/gapped: p ≥ 1.6. RK-like:
  p ≤ 0.4.
- Bragg ratio R_Q = [S(Q,L_max)/S(Q,4)]/[N_v(L_max)/N_v(4)]. Ordered if R_Q ≥ 0.5 with 2σ lower bound ≥ 0.4.
  Coulomb requires all R_Q ≤ 0.25 at the 2σ upper bound.
- Photon criterion: ω_eff·L constant (z=1) better than ω_eff·L².
- Projection-convergence rule: two values of T must agree within 2σ.
- Validation rule: |QMC − exact| ≤ 3σ.

Declared 20:27 UTC, after L=4 and 6 but before any L ≥ 8 data (prior exposure: L=4 and 6 values known):
**Coulomb ⇒ ΔE ∝ 1/L (ΔE·L → const); confined ⇒ ΔE ∝ L (string tension).**

Declared 19:57–20:27, before L ≥ 8: chains are run from ≥ 2 different starts, and agreement between starts is a
mixing check.

## 5. Results [NUM]

FILL

## 6. Verdicts against the pre-declared criteria [VERDICT]

FILL

## 7. Scope and caveats

FILL

## 8. Literature and repo context

FILL

## 9. Load-bearing step and what an independent check must do

FILL

## 10. What a decisive follow-up needs

FILL

## 11. Files

FILL
