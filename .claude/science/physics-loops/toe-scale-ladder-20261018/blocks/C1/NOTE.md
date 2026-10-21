# C1 — Sign-free, guide-free QMC of the cubic spin-1/2 link ring model: stoquasticity proved, Coulomb-vs-confined from the winding gap (string tension bounded, Coulomb not established), structure-factor criteria not evaluable (mixing failure)

**Block:** `toe-scale-ladder-20261018 / C1` (target: SCALE_LADDER_MAP.md, "C1", OBL-R2.1).
**Claim types used below:** [THM] proved statement with exhaustive finite certificate; [NUM] numerical
evidence from the QMC of this block; [EXT] repo result from a different code, not verified here;
[LIT] literature, recalled from memory, not re-checked; [VERDICT] application of pre-declared criteria.
**Status:** Reviewed in a separate agent context (same model as the author); unaudited. See `REVIEW.md` and the "Review dispositions" section at the end.
**Merges** `NOTE_part1_stoquastic.md` (§1–2) and `NOTE_part2_method.md` (§3). The full history,
including the times when criteria were declared, is in `WORKLOG.md`.

---

## 0. Bottom line

1. [THM] On every even cubic torus, for any static background, the ring Hamiltonian is stoquastic in the
   Gauss-legal σ^z basis for either sign of g, with the gauge chosen according to the sign: the identity for
   g > 0 and the diagonal ±1 gauge D for g < 0. D maps H(g) to H(−g). No single fixed gauge works for both signs.
   For odd L no diagonal gauge maps g to −g. The review confirmed this independently by brute-force ED over all
   2^24 configurations at L=2.
2. [THM] A local-update finite-temperature trace (worldline) code conserves a flip-class label and so does not
   sample Tr e^{−βH}. The L=2 control shows a large bias, E = −7.95 vs −9.02, consistent with the class restriction. No exact
   class-restricted reference was computed.
3. [NUM] The guide-free open-path projector built here reproduces exact L=2 results (W=0 and W=1 sectors) within
   3σ in 8 of 9 QMC-vs-exact cases (7 W=0 and 2 W=1); the other 4 checks are structural. The failure is in
   **E_mix** (z=+3.1), the production estimator, at V=0.9, T=3; equivalently N_f(end), z=−3.1. Fresh chains
   (a diagnostic, not a re-validation) gave z=−0.3. Under the pre-declared rule the case remains a FAIL.
4. [NUM/VERDICT] **Middle-of-path structure factors do not equilibrate for L ≥ 6.** They depend on the start
   state, and at L=8, T=32 E_mid differs from E_mix by about 100σ. The pre-declared S_T exponent, Bragg and
   photon-velocity criteria **cannot be evaluated**. This is a method failure, not a physics result.
5. [NUM/VERDICT] The guide-free electric-winding gap ΔE(L) = E0(W=1) − E0(W=0) at V=0 (see the table in §5)
   shows **no resolvable string tension**. With the Coulomb term included the fit gives σ = −0.010(15) at T=2L and +0.007(18) at the largest T, and the pure σL law is rejected (χ² 37–54/4). The
   pre-declared Coulomb form A/L fits, but so do the post hoc forms B/L² and const. The data **do not establish**
   Coulomb ∝1/L scaling. Verdict at V=0: **confined-with-resolvable-string-tension disfavoured; Coulomb
   consistent but not decided (inconclusive at accessible L)**. At V=0.5 and 0.9 the results are inconclusive, and
   the V=0.9 points show insufficient projection.
   **Caveats on these results (from the review):**
   - *L=4 dependence.* The pure-σL rejection and the bound σ ≲ 0.04 rest on the L=4 point alone. Without L=4,
     pure σL has χ² 6.9/3 (T=2L) and 2.7/3 (largest T), so it is not rejected, and the 2σ bound on σ
     loosens to about 0.05–0.08.
   - *Untested T-convergence.* The ΔE points at L = 4, 6 and 12 were not tested at a second T, yet they
     carry most of the fit leverage. At L=6 the single T=18 W=0 chain lies 1.7σ *above* the T=12 value, the
     opposite of the expected decrease with T.
   - *Cancellation assumption.* At 8³ this block's E(W=0) disagrees with the repo projector by 3.2–4.5σ. The
     difference, 0.37–0.46, is larger than ΔE(8) itself. The ΔE results at L ≥ 8 therefore **assume that the
     bias cancels between sectors**, which is untested.

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
  101–128, and the periodic-control seeds 129–131. **Re-running `step2_validate_L2.py` with the current driver would start its chains in the W=1 sector
  and fail.** Its seeds must be moved below 100 before re-use. The log as recorded is valid for the code at the
  time. It is empirically the W=0 sector: its E_mix values of −9.02 to −9.04 match the W=0 exact value, not W=1's
  −7.40. Step 3 covers only W=1 line starts at V = 0 and 0.5; the W=1 RK-walk starts and V=0.9 in W=1 are
  not validated.

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

Production settings:
- open path, uniform trial state at both ends;
- 2–3 chains per point from different starts: canonical, cyclically rotated canonical, or an "RK-walk" random
  flip walk; for W=1, the line start or an RK-walk from it;
- the error on each sector energy is max(seed scatter/√n, combined binned SE).

Source files: `data/winding_gap.md`, `data/per_chain.md`, `data/summary_combined.md`; fits in
`logs/winding_fit2.log` and `data/winding_fit2.json`.

### 5.1 Electric-winding gap ΔE = E0(W=1) − E0(W=0) (mixed estimator, total energies, g=1)

| V | L | T | E(W=0) [chains] | E(W=1) [chains] | ΔE | ΔE·L |
|---|---|---|---|---|---|---|
| 0 | 2 | exact | −9.026721 | −7.399111 | 1.627610 | 3.255 |
| 0 | 4 | 8 | −56.253(45) [3] | −55.577(44) [2] | 0.676(63) | 2.71(25) |
| 0 | 6 | 12 | −187.455(76) [3] | −187.015(69) [2] | 0.440(102) | 2.64(61) |
| 0 | 8 | 16 | −443.734(77) [2] | −443.573(92) [2] | 0.161(120) | 1.29(96) |
| 0 | 8 | 32 | −443.828(140) [2] | −443.506(94) [2] | 0.322(169) | 2.6(1.3) |
| 0 | 10 | 20 | −866.374(152) [2] | −866.282(260) [2] | 0.092(301) | 0.9(3.0) |
| 0 | 10 | 40 | −866.658(189) [2] | −866.500(336) [2] | 0.158(385) | 1.6(3.9) |
| 0 | 12 | 24 | −1497.314(229) [2] | −1496.659(269) [2] | 0.655(353) | 7.9(4.2) |
| 0.5 | 2 | exact | −4.255811 | −3.524354 | 0.731458 | 1.463 |
| 0.5 | 4 | 8 | −26.823(19) | −26.638(33) [1] | 0.185(38) | 0.74(15) |
| 0.5 | 6 | 12 | −89.686(42) | −89.448(68) [1] | 0.238(80) | 1.43(48) |
| 0.5 | 8 | 16 | −212.154(102) [2] | −212.192(116) [1] | −0.038(154) | −0.3(1.2) |
| 0.9 | 4 | 8 | −5.175(6) | −5.107(9) [1] | 0.068(10) | 0.27(4) |
| 0.9 | 6 | 12 | −17.171(12) | −17.186(21) [1] | −0.014(24) | −0.09(14) |
| 0.9 | 8 | 16 | −40.578(26) [2] | −40.702(35) [1] | −0.124(43) | −0.99(34) |

### 5.2 Fits at V = 0 (weighted LSQ, L = 4..12)

Models C, S and Str were declared before L ≥ 8; Q and K are post hoc. The first p is A (or B or c), the second
is σ.

| set | C: A/L | S: A/L + σL | Str: σL | Q (post hoc): B/L² | K (post hoc): const |
|---|---|---|---|---|---|
| T = 2L | A=2.62(23), χ² 3.9/4 | σ = −0.010(15), χ² 3.4/3 | χ² 54.5/4 | χ² 4.4/4 | χ² 17.9/4 |
| largest T per L | A=2.70(23), χ² 1.6/4 | σ = +0.007(18), χ² 1.4/3 | χ² 36.7/4 | χ² 5.2/4 | χ² 7.8/4 |

Leverage comes almost entirely from L = 4, 6 and 8. At L ≥ 10 the errors are 50–250% of ΔE.

### 5.3 Projection (T) and start checks for the winding energies

- **Start consistency of E_mix** (same L, T, W, different starts; V=0, L ≥ 8): 10 pairs with total
  χ² = 12.8/10. The two largest tensions are both in W=1 at L=10: 2.1σ at T=20 and 2.0σ at T=40.
- **T-dependence.**
  - L=8, T=16 → 32: ΔE goes 0.161(120) → 0.322(169), consistent.
  - L=10, T=20 → 40: E(W=0) drops by 0.28(24) and E(W=1) by 0.22(42); ΔE goes 0.09(30) → 0.16(39).
  - These shifts are not significant, but they are of the same size as ΔE itself. T-convergence of ΔE is
    therefore **not demonstrated** at L ≥ 10, and L=12 has only T = 2L.
- **Binned errors.** The binned SE on E_mix still grows by about 5–10% over the last bin doublings, so the quoted
  per-chain errors may be underestimates of that order.
- **V=0.9.** ΔE < 0 at L=6 and 8. If both runs were converged, a negative ΔE would mean the W=1 component lies
  below W=0, which is not excluded a priori. With T = 2L near RK, where soft modes need T ~ L², it is read as
  insufficient projection, and no conclusion is drawn.

### 5.4 Middle-of-path observables: not equilibrated (mixing failure)

| L | T | E_mix/N_p (all chains) | E_mid/N_p | S_T(k1) by start |
|---|---|---|---|---|
| 6 | 12 | −0.2894…−0.2891 | −0.2880…−0.2894 | 0.185 / 0.248 / 0.369 |
| 8 | 16 | −0.2889 | −0.2878…−0.2892 | 0.14–0.15 (canon/line) vs 0.39–0.40 (RK-walk) |
| 8 | 32 | −0.2890…−0.2887 | −0.2754…−0.2795 | 0.10–0.13 vs 0.23–0.28 |
| 10 | 20 | −0.2889…−0.2887 | −0.2862…−0.2872 | 0.11–0.12 vs 0.44–0.64 |
| 10 | 40 | −0.2889…−0.2887 | −0.2775…−0.2801 | 0.06–0.12 |
| 12 | 24 | −0.2888…−0.2887 | −0.2757…−0.2779 | 0.10–0.11 vs 0.24–0.25 |

- E_mid and E_mix must agree in expectation. For T ≥ 24 they differ by 0.010–0.013 per plaquette, which is
  more than 20σ. The middle of a long path stays far from the projected state; longer paths are *worse*.
- S_T(k1) at L=10 and 12 differs by a factor of 2–5 between starts.
- Flippability Bragg weights are also start-dependent. Example: at L=8, T=32, m2_n(X) is 0.10 (canonical) vs
  0.03 (RK-walk).

These numbers are reported as per-start ranges only. They are **not** estimates of ground-state structure
factors.

### 5.5 External comparison [EXT]

The repo's guide-dependent projector with loop moves (different algorithm and code;
`scripts/ring_model_electric_coupling_from_winding_sector_energies_and_the_comparator_coupling_constant_2026_09_25.py`,
cached output in `logs/runner-cache/`) gives, for the same q=1 sector:

| L | repo ΔE | this block ΔE | difference |
|---|---|---|---|
| 4 | 0.7315(84) | 0.676(63) | 0.9σ |
| 6 | 0.370(20) | 0.440(102) | 0.7σ |
| 8 | 0.169(44) | 0.322(169) at T=32 | 0.9σ |

- The two ΔE sets agree within 1σ at every common L.
- Refitting the repo's more precise numbers with the same models gives A/L χ² = 51/2 (rejected) and B/L² χ² =
  5.1/2. A/L + σL gives σ = −0.034(5), χ² 0.07/1. So the repo data show ΔE·L *decreasing* from 2.9 to 1.35
  over L = 4..8.
- **Recorded disagreement:** the repo's 8³ W=0 energy −443.364(31) lies 0.46 (3.2–4.5σ depending on the error estimate; see REVIEW.md) *above* this block's
  −443.828(140). This block's estimator is a Rayleigh quotient and so, in expectation, an upper bound. Either the
  repo value is biased high (guide or population effects) or this one is biased low (residual mixing). This is not
  resolved here. Further points from the review:
  - Against the T=16 value −443.734(77) the disagreement is 4.5σ.
  - At L = 4 and 6 the absolute energies agree, so the problem first appears at L=8.
  - The repo's loop moves target the whole sector, whose ground energy is ≤ that of the component. The
    component/sector difference therefore cannot explain the repo value being higher.
  - One of the two codes is biased by at least about 3e−4 per plaquette, which is the size of ΔE/N_p at L ≥ 8.
  - Agreement of ΔE with the repo at L=8 therefore holds only if this bias cancels between the sectors.

## 6. Verdicts against the pre-declared criteria [VERDICT]

| criterion (declared) | V=0 | V=0.5 | V=0.9 |
|---|---|---|---|
| S_T exponent p (Coulomb p≈1, ordered p≥1.6, RK p≤0.4) | **not evaluable**: middle not equilibrated (§5.4) | not evaluable | not evaluable |
| Bragg ratio R_Q (ordered R_Q≥0.5; Coulomb ≤0.25) | **not evaluable** (start-dependent, §5.4) | not evaluable | not evaluable |
| ω_eff·L photon criterion | not evaluable (C(τ) measured at the non-equilibrated middle) | not evaluable | not evaluable |
| projection rule (two T agree within 2σ) | ΔE: passes formally at L=8 and 10, but the errors are as large as ΔE. **L = 4, 6, 12 untested**: a single T for W=1; the L=6 T=18 W=0 chain is 1.7σ above T=12 | not tested at L=8 | fails in effect (ΔE<0) |
| winding gap: confined ⇒ ΔE ∝ L | **pure σL rejected** (χ² 37–54/4). With the Coulomb term included, σ = −0.010(15) or +0.007(18): **no resolvable string tension; σ ≲ 0.04 g (2σ)** at L ≤ 12. **Both of these depend on L=4**: without it, pure σL has χ² 2.7–6.9/3 (not rejected) and σ ≲ 0.05–0.08 (2σ). L ≥ 8 points assume sector-bias cancellation | σ = 0.007(18) from L=4..8 only: no evidence of confinement | inconclusive (insufficient projection) |
| winding gap: Coulomb ⇒ ΔE·L → const | **consistent** (A/L χ² 1.6–3.9/4), but **not established**: B/L² fits equally well, L ≥ 10 errors are too large, the T-convergence of ΔE at L ≥ 10 is not shown, and the more precise repo [EXT] values show ΔE·L falling over L = 4..8 | consistent but untested beyond L=8 | — |

**Overall verdict for OBL-R2.1:** **INCONCLUSIVE at accessible L.**
- Supported: the method is sign-free and guide-free, and a large string tension is excluded on L ≤ 12. This exclusion depends on the L=4 point and on the L ≥ 8 bias-cancellation assumption.
- Not supported: neither a Coulomb phase (S_T ∝ |k|, a 1/L winding gap, a finite photon velocity) nor an
  ordered phase is established.
- Reason: the structure-factor criteria failed for an algorithmic reason (mixing in the middle of the path),
  which is operational and not physical evidence. The one robust observable does not separate 1/L from faster
  decay.

## 7. Scope and caveats

- **Model scope.** These are statements about the two specified flip components (W=0 canonical and W=1
  line-reversed), with ρ = 0, on even L ≤ 12. They are not about all components or whole winding sectors.
- **Exactness of the energy estimator.** E_mix is exact in expectation for the uniform trial state *only if the
  chain is equilibrated*. The ends move fast and agree across starts (§5.3), but the middle does not equilibrate
  (§5.4). A residual end bias at the 1e−4-per-plaquette level would be enough to move ΔE at L ≥ 10. Agreement
  between starts is evidence, not proof.
- **Finite projection.** E_mix(T) ≥ E0 only in expectation. ΔE is a difference of two upper bounds, so it has no
  bound of either sign at finite T.
- **Errors.** Errors come from binning plus seed scatter over only 2–3 starts. They have no proved coverage.
- **Prior exposure.** The ΔE criterion was declared after the L=4 and 6 values were seen. Fit forms Q and K are
  post hoc.
- **Lost or incomplete runs.** The run of 2026-10-18/19 lost these jobs to container restarts and the 25-minute
  job limit: L=12 W=0 seed 2 (killed at the limit); the L=12 W=1 seed-112 job (dropped); and earlier queue jobs
  never run (V=0.5 and 0.9 second W=1 chains, V=0.5/0.9 at L ≥ 10). V=0.5 and 0.9 rest on one W=1 chain per L.

## 8. Literature and repo context

[LIT], recalled from memory; no numbers relied on:
- Hermele, Fisher and Balents, PRB 69, 064404 (2004): a U(1) Coulomb phase with emergent photon in pyrochlore
  quantum spin ice, perturbatively near the ring-exchange limit.
- Banerjee, Isakov, Damle and Kim, PRL 100, 047208 (2008): QMC support for the photon in the pyrochlore ring
  model.
- Shannon, Sikora, Pollmann, Penc and Fulde, PRL 108, 067204 (2012): quantum ice, the photon with ω ~ k² near RK
  crossing over to ω ~ k.
- Cubic quantum dimer model (Sikora et al., PRL 103, 247001 (2009) and PRB 84, 115129 (2011)): a Coulomb phase
  only in a window below the RK point, with crystalline order at smaller V. I do not reliably recall the window
  edges, nor whether the pure-ring point V=0 is inside it.
- 3D U(1) quantum link models (Wiese and collaborators; Banerjee et al.): known; specific results not recalled.

Implication: the cubic dimer analogy makes a *confined/ordered* phase at V=0 a live possibility. A tiny string
tension, or a crystal with a weak Bragg weight, would be invisible at L ≤ 12 with these errors. I could not
confirm a literature treatment of exactly this cubic spin-1/2 link model, and novelty has not been checked
beyond memory.

Repo context:
- `docs/RING_MODEL_*` notes use guided projectors. Their winding splittings (§5.5) are consistent with ours.
  Their 8³ energy disagrees with ours at 3.2–4.5σ.
- The 09-04 note title claims a "quadratic transverse mode, not a Maxwell photon". ΔE·L decreasing in the repo
  data would fit that reading, but this block cannot test it.

## 9. Load-bearing step and what an independent check must do

**Load-bearing step:** the estimate ΔE(L) = E_mix(W=1) − E_mix(W=0) at V=0, L = 4..12. In particular:
1. the claim that the mixed estimator with the uniform trial state and free-end moves is equilibrated at the ends
   even though the middle is not;
2. the T-convergence of ΔE at L ≥ 8.

The rejection of a pure string tension rests on L=4. The L ≥ 8 points additionally assume that the 8³ absolute-energy bias, seen against the repo projector, cancels between sectors.

An independent check must use a *different path*, for example:
- (a) exact or Lanczos ground energies of both components at L=4. This may be infeasible: the 4³ ice
  manifold is large. Check its size first.
- (b) a different QMC (SSE or worm/loop) with its own code, computing E0(W) or the winding susceptibility
  ⟨W²⟩ at finite β.
- (c) a reptation or forward-walking estimator, with E_mid ≈ E_mix as an acceptance test.

Re-running `scripts/prod.py` with new seeds is **not** independent. The stoquasticity proof (§2) is
self-contained and can be checked by hand.

## 10. What a decisive follow-up needs

The follow-up block with non-local updates is `blocks/C1b`.

1. **Non-local updates.** Loop or worm updates in space-time, i.e. directed loops in the plaquette-flip worldline,
   or cluster moves on the dual height/flux representation. These would remove the frozen-middle problem. The
   pass criterion is E_mid = E_mix within errors and agreement of S_T and Bragg weights across starts.
2. **Finite-T SSE with winding-changing loops.** This avoids the class restriction of Lemma 3. It would measure
   ⟨W²⟩/L (Coulomb: finite stiffness) and S_T(q, iω_n) directly, with β ∝ L and β ∝ L² both run.
3. **Larger L at fixed relative error.** ΔE at L=16 with an error ≲ 0.05 needs about 50× the statistics used here.
   That requires a variance-reduced estimator, e.g. a correlated W=0/W=1 pair, or thermodynamic integration of
   the flux energy.
4. **Before claiming Coulomb vs order, rerun the pre-declared criteria unchanged** on equilibrated data. Add a
   check that ΔE·L stabilises rather than falls: the repo [EXT] values show it falling.

## 11. Files (all in this block)

- Scripts: `scripts/step1_stoquastic.py`, `scripts/step2_validate_L2.py` (see the seed hazard in §3.4),
  `scripts/step3_validate_W1_L2.py`, `scripts/qmc.py`, `scripts/driver.py`, `scripts/prod.py`,
  `scripts/analyze.py`, `scripts/winding_fit.py`, `scripts/winding_fit2.py`, `scripts/run1.sh`,
  `scripts/jobs_*.txt` (`jobs_C.txt` = the resumption runs, with the changes annotated).
- Logs:
  - validation, each ending with a TOTAL line: `logs/step1_stoquastic.log` (PASS=26 FAIL=0),
    `logs/step2_validate_L2.log` (PASS=8 FAIL=1), `logs/step3_validate_W1_L2.log` (PASS=4 FAIL=0);
  - debug logs `dbg_*.log` and `test_delta_fast.log` (no TOTAL line; diagnostics, not runners);
  - production: `logs/prod.jsonl`, `logs/queue_*.log` (`queue_C.log` = resumption);
  - fits: `logs/winding_fit.log`, `logs/winding_fit2.log`.
- Data: `data/run_*.npz` (one per chain), `data/winding_gap.{md,json}`, `data/winding_fit{,2}.json`,
  `data/per_chain.md`, `data/summary_combined.md`.

## Review dispositions

Review: `REVIEW.md`, written in a separate agent context (same model as the author). It found no incorrect
claim and confirmed stoquasticity independently with 2^24 brute-force ED at L=2.

| item | severity | disposition |
|---|---|---|
| C2: the gauge is chosen per sign of g | minor | **Accepted.** §0.1 now says: identity for g > 0, D for g < 0, no single gauge for both. |
| C6: periodic-control attribution | minor | **Accepted.** §0.2 now says "consistent with the class restriction"; no exact n=0 reference was computed. |
| C7: validation counts and the failed observable | minor | **Accepted.** 8 of 9 QMC-vs-exact cases pass; the other 4 checks are structural. The failure is in E_mix, the production estimator. dbg_vend is a diagnostic, and the case stays a FAIL. |
| C8: seed hazard | minor | **Accepted.** Seeds 129–131 added. The recorded step-2 log is W=0, confirmed by its E_mix values. |
| C9: step-3 scope | minor | **Accepted.** Only W=1 line starts at V = 0 and 0.5 are validated; this is stated in §3.4. |
| C12: L=4 dependence of the σL rejection | moderate | **Accepted.** Both statements are now given, with and without L=4, in §0, §6 and §9. |
| C14: projection untested at L = 4, 6, 12; L=6 T=18 inversion | moderate | **Accepted.** Flagged in §0 and in the §6 projection row. |
| C15: 8³ disagreement of 3.2–4.5σ, larger than ΔE(8) | moderate | **Accepted.** Stated in §0, §5.5, §6 and §9: the L ≥ 8 gap results assume the bias cancels between sectors. Unresolved; left to C1b. |
| Others (C1, C3–C5, C10, C11, C13, C16, C17) | — | Confirmed correct; no change. |

The overall verdict is unchanged: **INCONCLUSIVE at accessible L**. The supporting evidence against confinement is
now explicitly conditional, as described above.
