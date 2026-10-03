I did not find any rule of the allowed kinds whose calmest state is the two-part (parton) background. The main new result is an exact one. The soldered parton state is the projected π-flux singlet with every spin given a fixed, place-dependent half-turn (a Klein-type map). So the parent-rule question is the same as the long-open question of a parent rule for the 3D π-flux spin liquid. With nearest-neighbour rules, the soldered state beats the best product state only by at most 0.0036 per bond, in a thin window. After spin-wave corrections it loses everywhere by about 0.08–0.12 per bond.

This message is the full report. I did not write `SP/c8/A44/REPORT.md` because my harness forbids subagent report files.

**Housekeeping**
- No git writes, no repo edits, no PRs. The repo was read only with `git show origin/main:` at `b6fda5ae1d`; no fetch.
- Scripts are in `SP/c8/A44/`. Every run went through `run.sh`:
  - load gate below 6 and free memory at least 25%;
  - the shared `NUMLOCK`, treated as stale after 600 s, released after each run and now gone;
  - `nice -n 10` and the four BLAS caps at 1;
  - a Python `signal.alarm` of 285 s or less;
  - wall time and peak memory from `/usr/bin/time -l`.
- Loads at run time were 1.7–4.8 and free memory 31–49%. The longest run took 90 s; peak memory was 462 MB.

**Grades.** EXACT (proof or exact arithmetic), CHECKED (finite computation with stated tolerance or error bars), ARGUED (reasoning without proof), COMPARATOR (literature recalled from memory, not adopted). Every rule here is supplied, not adopted.

## 1. Question

Is there a rule allowed by the grid's turns (J σ·σ, K σ^aσ^a, D e_a·(σ×σ), plus star-local terms) whose calmest state is the Gutzwiller-projected parton background? That background has one fermion per site, the soldered hop iλσ^a, and optionally the scalar hop t; its half-pieces carry the walk's eight round crossings.

## 2. Answer, graded

**New exact structure: the Klein duality (EXACT; CHECKED).**
- Take V_x = (iσ¹)^{x1}(iσ²)^{x2}(iσ³)^{x3}. Then V_x†(iσ^a)V_{x+e_a} is a scalar times the identity, with Kogut–Susskind signs. So the soldered ansatz is the scalar π-flux ansatz in a site-dependent spin frame.
- Hence P_G|FS_sold⟩ = (⊗_x V_x) P_G|FS_π⟩, which is a four-sublattice π-rotation of the SU(2)-singlet projected π-flux state.
- CHECKED on the 16-site cubic cluster:
  - the V†-rotated soldered state has S² = 1.5e-29 (a singlet);
  - its overlap with the independently built π-flux state is 1.000000.
- Consequences:
  - (i) At t = 0, e_J = −s/3, e_K = +s/3 and e_D = 0, where s is the π-flux state's nearest-neighbour ⟨σ·σ⟩. VMC confirms this at L = 4, 6 and 8 within error bars.
  - (ii) On D = 0 the rule maps exactly as H(J,K) ↔ H(−J, K+2J). The 16-site spectra match: φ = 135° and 315° both give −0.61929.
  - (iii) The dual of any SU(2)-invariant, lattice-symmetric rule is a soldered-covariant rule with the same support. It is EXACT for pair terms (shown here), extends to triple products by the same argument, and to all invariants by invariant theory (ARGUED). For example, the face-diagonal σ·σ term becomes 2σ^cσ^c − σ·σ, with c the face normal.
  - (iv) Therefore "the soldered state is the calmest state of some covariant rule" holds exactly when "the π-flux singlet is the calmest state of the dual rule".
- **The gauge structure is larger than A43 stated (EXACT algebra; CHECKED).** After the staggered U(1) gauge, the whole (t, λ) hopping family commutes with the η-SU(2) generators (defect 0 over 60 random cases, plus an explicit Fock-space check). So the mean-field gauge group is SU(2), not just "at least U(1)". A same-sublattice hop breaks it to U(1).

**Q1. Projected background by VMC (CHECKED).** Per oriented bond, Pauli units, antiperiodic fermions. The error is the binning plateau; first and second halves agree within error.

| Cluster | State | e_J | e_K | e_D |
|---|---|---|---|---|
| 16 cubic, exact | soldered (t = 0) | +0.36296 | −0.36296 | 0 |
| 16 cubic, VMC check | soldered | +0.3623(37) | −0.3626(31) | 0 |
| 16 cubic, exact / VMC | θ = 45° | +0.03859 / +0.0368(22) | −0.17201 / −0.1723(16) | −0.36126 / −0.3598(18) |
| 4³ | soldered | +0.3433(24) | −0.3471(14) | 0 |
| 4³ | θ = 45° (t = λ) | −0.0089(11) | −0.2226(7) | −0.3786(8) |
| 4³ | t only | −0.9302(72) | −0.3103(26) | 0 |
| 4³ | π-flux singlet | −1.0380(21) | −0.3464(11) | 0 |
| 6³ | soldered | +0.3379(13) | −0.3355(9) | 0 |
| 6³ | θ = 62.5 / 51 / 40 / 15° | +0.2530 / −0.0580 / −0.2926 / −0.6082 | −0.2821 / −0.2146 / −0.2141 / −0.2363 | −0.1699 / −0.3933 / −0.4215 / −0.2889 |
| 8³ | soldered (two runs) | +0.3361(9), +0.3360(14) | −0.3357(8), −0.3358(7) | 0 |
| 8³ | t only | −0.8800(85) | −0.2932(28) | 0 |

- The 6³ mixed states' errors are at most 0.0013.
- On 4³ (and the 16-site cluster) with antiperiodic fermions, |sin k| is the same at every k-point. So the family has only three distinct projected states there: t-only for θ < 30°, mixed for 30–60°, soldered for θ > 60°.
- On 6³ the soldered state is unchanged for θ ≥ 75°.
- Convergence of s: −1.089 (16 sites), −1.036(4) (4³), −1.010(2) (6³), −1.0077(18) (8³). Extrapolating with L⁻³ or L⁻⁴ gives s∞ ≈ −1.003 to −1.006 (ARGUED).
- Projection multiplies the unprojected bond correlation (A43: 0.080) by about 4.2.

**Q2. Exact 16-site cross-check (CHECKED; Lanczos tol 1e-10; parton states by full enumeration of 65,536 determinants).**
- I ran the requested 2×2×4 cluster and also the cubic-symmetric cluster Z³ mod ⟨(2,2,0),(2,0,2),(0,2,2)⟩. The second has no doubled bonds and keeps all 24 turns.
- On 2×2×4 the x and y bonds are doubled, and the Moriya term cancels identically on them (EXACT). So D acts only along z there, and the cluster favours singlet states.
- Cubic-cluster results, energies per bond:

| φ (D = 0) | E₀ exact | Best product | Soldered: E, overlap | π-flux: E, overlap | Best product overlap |
|---|---|---|---|---|---|
| 0° (J = 1) | −1.2982 | −1.0000 | +0.3630, 0.000 | −1.0889, 0.722 | 0.10 |
| 90° (K = 1) | −0.4556 | −0.3333 | −0.3630, 0.272 | −0.3630, 0.272 | 0.03 |
| 105° | −0.5319 | −0.4082 | −0.4445, **0.726** | −0.0688, 0.000 | 0.10 |
| 120° | −0.5913 | −0.4553 | −0.4958, 0.722 | +0.230, 0 | 0.10 |
| 135° | −0.6193 | −0.4714 | −0.5133, 0.722 | +0.513, 0 | 0.09 |
| 150° | −0.7171 | −0.6994 | −0.4958, 0.081 | — | 0.15 |
| β = 30°, φ = 120° | −0.5474 | −0.3943 | −0.4294, 0.542 | — | 0.08 |
| pure D | −0.7507 | −0.5774 | best parton (θ = 45°) −0.3613, 0.008 | — | 0.02 |

- On 2×2×4 the soldered overlap reaches 0.842 at φ = 105°. At φ = 135° it gives E = −0.6695 against exact −0.7097.
- Product-state overlaps on a finite symmetric cluster are suppressed by symmetry. At the ferromagnetic point the ground space is the 17-fold S = 8 multiplet; four Lanczos vectors capture it only partly, so the overlaps there are lower bounds.

**Q3. The map (CHECKED numerics; spin-wave validity COMPARATOR).**
- **Best product state.** In the window below, the best product state is exactly the compass-staggered one (each component alternates along its own axis), with E = (J − K)/3. The Luttinger–Tisza bound is attained there (EXACT), and the 4³ greedy search agrees.
- **Window algebra (EXACT).** E_sold − E_cs = −(K−J)(|s|−1)/3.
- **Lowest variational energy.**
  - Variational states compared: the parton family, t-only, the π-flux singlet and the best product state.
  - The soldered state is lowest only on the D = 0 band φ ∈ (89.9°, 135.2°), that is J ∈ (−0.71, 0) with K ∈ (0.71, 1). The margin is at most 0.0036 per bond at L = 8.
  - The band slightly leaves the plane: at β = 30°, φ = 120° it beats product states, but a mixed parton with e_D ≠ 0 is lower there.
  - The band exists only if |s∞| > 1, which is marginal.
- **After corrections.** Linear spin waves (A43's library; k-grid converged to 2e-4; Néel −1.1943 per bond, matching the textbook value) are lower everywhere. In the window the gap is 0.08–0.12 per bond: for example −0.4565 against −0.3357 at φ = 90°, and −0.5852 against −0.4750 at φ = 135°.
- **Exact duality check.** At φ = 116.57°, which is (J,K) = (−1,2)/√5 and the dual of the plain antiferromagnet, the soldered state gives −0.4507 per bond. The dual of the cubic antiferromagnet gives about −0.538 (QMC −1.203 per bond, COMPARATOR), and that state is Néel-ordered (COMPARATOR). So the calmest state there is the dual of Néel order, a compass-staggered ordered state.
- **Directions with D.** The mixed partons reach e_D = −0.4215. Against pure D: −0.42 for the parton, −0.577 for the classical spiral, −0.664 with spin waves. They lose.
- **t-only reference.** It is worse than the π-flux singlet everywhere it matters (−0.880 against −1.008 at J = 1).

**Q4. Star terms (optional; numbers CHECKED, conclusion ARGUED).**
- By (iii), every frustrating SU(2)-invariant star-local term gives a covariant star-local term. In the dual frame at L = 8 the parton's correlations are:
  - nearest neighbour −1.008;
  - face diagonal +0.401(2);
  - axis pair (x, x+2e_a) +0.264(3).

  So a dual J₂ costs the ordered competitor +6j per site (classical) but the parton only 2.41j. In the original frame that term is j Σ_fd (2σ^cσ^c − σ·σ).
- Per site, parton −3.023 + 2.407j compared with spin-wave estimates:

| j | Parton | Néel (spin waves) | Collinear (spin waves) |
|---|---|---|---|
| 0.25 | −2.42 | −2.67 | −2.29 |
| 0.30 | −2.30 | unstable | −2.27 |
| 0.40 | −2.06 | — | −2.41 |

- So the parton only ties near j ≈ 0.3, exactly where spin waves break down.
- On the 16-site cluster the parton overlap peaks at 0.775 (j = 0.2), and the exact energy stays 0.26–0.35 per site below the parton.
- COMPARATOR (uncertain): the 3D J₁–J₂ cubic model is usually placed as a direct Néel-to-collinear transition near J₂/J₁ ≈ 0.25–0.28, with no established spin liquid.
- This is the only candidate region I found; it is not evidence.

**Q5. Verdict.**
- No evidence for a parent rule among the allowed kinds. Three reasons:
  - the exact reduction to a known-ordered dual;
  - the margin of at most 0.004 per bond over product states;
  - the loss of about 0.1 per bond to corrected ordered states and to the exact 16-site ground states.
- A parent rule would need all of the following:
  - **Frustrate the dual Néel order without hurting the singlet bonds.** That means star-local Klein duals of SU(2)-frustrating terms (J₂/J₃-type or multi-spin), which is the open 3D π-flux parent problem.
  - **A further SU(2) → U(1) breaking** (for example a same-sublattice hop) so that the emergent field could act like light, since at mean field it is non-abelian.
  - **The gate**, for quietness (A39/A43; not computed here).
- For "matter and light from one qubit per place, with no painted pattern":
  - The soldered background is pattern-free: covariant and translation-invariant.
  - But the covariant pair rules prefer ordered states, which are magnet-like ripple carriers and a 1-of-N pick held in the state.
  - So with pair rules, one qubit per place gives patterned order, not the two-part background.

## 3. Methods and derivations

- **Duality.** V_x†σ^bV_x = (R_x)_{bb}σ^b, with R_x = diag((−1)^{x2+x3}, (−1)^{x1+x3}, (−1)^{x1+x2}). On an a-bond, R_xR_{x+e_a} flips the b and c components. So σ·σ → 2σ^aσ^a − σ·σ, the compass term is unchanged, and the Moriya term becomes staggered.
- **Covariance of duals.** R_xR_{x+d} depends only on d mod 2, and sg(gd) is sg(d) with components permuted by g. Hence duals of SU(2)-invariant pair and triple terms are covariant.
- **Gauge group.** A bond f_x†Mf_y + h.c. commutes with η⁺ exactly when Mε + εM* = 0 (ε = iσʸ; derived from the commutator [η_y⁺, f_ys]). For M → iM this holds for every t + iλσ^a.
- **VMC.**
  - Determinant ratios with Sherman–Morrison single flips and rank-2 Woodbury pair-flip updates.
  - Pair flips are required: the soldered state conserves the twisted magnetisation Σ(−1)^{x1+x2}σᶻ, so single flips are never accepted.
  - Local estimators come from 1-, 2- and 4-row ratios, at O(N²) per measurement.
  - The inverse is refreshed every 10 sweeps; drift was at most 1e-11.
- **ED.** Sparse CSR matrices built per bond direction, `eigsh` with k = 4.
- **Spin waves.** E = E_cl + ½⟨Σω − tr A⟩_k (A43's Holstein–Primakoff blocks), restricted to backgrounds that are stationary and stable.

## 4. Checks (all in `SP/c8/A44/`; outputs `out_*.txt`, timing `time_*.txt`)

| Script | Runtime, peak memory | Key results |
|---|---|---|
| `ed16.py fcc16` | 38 s, 462 MB | Duality S² 1.5e-29; overlap 1.000000; product quantum−classical ≤ 7e-14 |
| `ed16.py 224` | 30 s, 374 MB | Moriya cancels on the length-2 directions |
| `vmc.py` (16-site check) | 6 s | All four states agree with enumeration within 1σ |
| `vmc.py` at 4³ / 6³ / 6³ / 8³ / 8³ | 20 / 88 / 88 / 70 / 90 s; ≤ 170 MB | Q1 table above |
| `gaps.py` | 3 s | Closed-shell θ windows |
| `lswt.py` | 53 s | k-grids 4/6/8 converged |
| `map.py` | 0.1 s | Q3 map and window |
| `star_j2.py` | 14 s, 453 MB | Q4 cluster and spin-wave table |
| `star_vmc.py 8` | 83 s | Q4 correlations |
| `igg.py` | 0.1 s | Gauge-group algebra |

**Superseded or flagged runs, recorded honestly.**
- The first 16-site VMC validation used exchange-only moves. It was non-ergodic for the soldered state (e_J = 0.324 against exact 0.363). The validation caught it, and pair flips fixed it. `vmc_v1.py` is an intermediate copy of `vmc.py` saved after that fix; the exchange-only version itself was not kept.
- The first `star_vmc` run crashed in post-processing (a negative integer power) and was rerun with identical numbers.
- The `lswt.py` Luttinger–Tisza column prints twice the bound (a missing ½). I halved it in the analysis; the corrected bound equals the 4³ greedy minimum on the whole D = 0 circle.

## 5. Open edges

1. Pin down |s∞| − 1, which decides whether the thin variational window survives: VMC at 10³ or 12³, or twist averaging.
2. Treat the dual J₁–J₂ cubic model near J₂/J₁ ≈ 0.3 better than spin waves, for example with correlated variational competitors.
3. Add multi-spin dual terms of ring type, which the parton may favour more strongly.
4. Search for an SU(2) → U(1) or Z₂ breaking deformation (same-sublattice hops, pairing via Pfaffians) and its energetics.
5. Check whether the soldered background's star reductions are full rank, which bears on gate quietness (A39).
6. Correction for A43's (d): at mean field the gauge group is SU(2), not just U(1).

## 6. Plain-language summary

The entangled two-part background turns out to be a familiar entangled state in disguise: give every spin a fixed half-turn that depends on its place, and it becomes the standard "π-flux" state. Because of that disguise, asking for a rule that makes the background the calmest state is the same as asking for one that makes the standard state the calmest. For the simple neighbour rules the grid allows, that does not happen. The background beats the best plain arrangement of spins only by a hair, in a narrow range of rules. Once the small quantum jiggles of those arrangements are counted, ordered magnet-like states always win, by about a tenth of a bond's energy. Making the two-part background win would need richer rules that spoil the magnetic order, and its hidden field would then need a further step before it could act like light.