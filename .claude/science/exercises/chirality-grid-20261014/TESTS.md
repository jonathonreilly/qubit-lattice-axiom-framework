# Step 8 tests: index

Every test was pre-registered in its folder's `PREREG.md` before it ran. Results are as reported; referee status is noted.

| Test | Folder | Reading | Referee |
|---|---|---|---|
| F1 C1 (mod-16 table), C2 (GS reduced locator) | routes/F1 | COUNT-16 met; signatures located | — |
| F2 T1, T3b/c, T4b, T5b | routes/F2 | PASS (T4 FAIL: mis-built) | codex: confirmed (T3 defect norm ~2×) |
| F3 R1 / R1-F1 / R1-F2 / R2 | routes/F3 | R1 FAIL (tolerance); R1-F1, R1-F2, R2 PASS | — |
| F4 T-F4-1..4b | routes/F4 | lemma-consistent; price-prohibitive; T-F4-3 PASS (free); inverse-L | — |
| F5 T1, T2/T2b, T3a, T3′ | routes/F5 | T1/T3a not met; T2 PASS; T3′ FAIL | — |
| F6 tA–tD | routes/F6 | all PASS | — |
| X1 DI-Z8 | combos/X1 | CHAIN-CONSISTENT (instrument) | — |
| X2 T1–T5 | combos/X2 | PASS (structural) | — |
| X3 T-X3, T-X3b–f | combos/X3 | T-X3 PASS; gauged tests inconclusive | via K2 |
| K1 A1–A4, A3′, B1–B4 | kills/K1 | anomaly kill failed (all classes vanish); GPR mean-field upheld | — |
| K2 T1 (+V1–V6), T3 | kills/K2 | free X3-A survives; Fejér-measure open-time RP FAIL | codex: confirmed with corrections (Fejér scope; hard measure positive) |
| K2b T1, T2, V1–V5 | kills/K2b | torus PASS-at-power (Fejér); PV-DWF and Shamir negative (Fejér) | — (scope as K2) |
| K3 T1, T1F | kills/K3 | KILL-(b)-READING; NET-GAIN | — |
| K2c (hard-support RP) | kills/K2c | **running** | — |

**Update (18:36Z).** K2c finished. Under X3's hard measure, the as-registered searches are PASS-at-power, which turned out to be masking. The V2 W-matched follow-up gives a **FAIL on open time and the torus** (same-family; codex referee running).

**K2c referee (20:40Z):** CONFIRMED WITH CORRECTIONS. Non-RP of the hard-support overlap measure holds in the finite 2D U(1) proxy, including the tori. Wording correction: "certified" becomes "quadrature-converged".

## Next set of tests (pre-registered 2026-10-14 ~20:48Z, at Jon's request: "run the next set of tests")

Memory: ≤ 0.4 GB per run for NT-1 and NT-2, ≤ 1 GB for NT-3, one process at a time per agent. Each agent writes its detailed PREREG.md before running. The readings below are fixed now.

**NT-1. Chiral-measure RP (route 1, set B).** Does gauged reflection positivity also fail for a genuinely chiral, anomaly-free 2D U(1) overlap measure? Use Weyl projections with a charge set such as 3-4-5-0, or 1⁴(−1)⁴ with Kikukawa-type mirror vertices if needed, and a gauge-invariant measure (Lüscher-type measure term or its 2D abelian construction), with W-matched witnesses as in K2c.
- **CHI-RP-FAIL:** a quadrature-converged negative RP eigenvalue (< −10× the error estimate) on W-matched gauge-invariant witnesses.
- **CHI-RP-PASS-at-power:** PSD within error, with the vector-like K2c witness as the power reference.
- **OPEN:** otherwise, including "a gauge-invariant chiral measure could not be built in budget". State which.

**NT-2. Is the hard plaquette bound RP in 3D (pure gauge)?** This is X3's price P-X3d, owed by K2c. Use a 3D slice with a 2×2-plaquette crossing structure, the hard indicator |arg U_p| < δ, link reflection, and W-matched pools.
- **PG3-NEG:** a converged negative eigenvalue (the bound itself is not RP in 3D).
- **PG3-PSD:** PSD on searched pools at power.
- **OPEN:** otherwise.

**NT-3. T-G1 (route 2, X2).** Does the filter overlap destroy the unique symmetric gapped strong-coupling phase? Exact diagonalisation of a filtered "star" quartic, with an SU(4) (or Spin(6)) toy symmetry on 4–6-site rings or clusters, compared with the onsite quartic.
- **TG1-SYMMETRIC:** at strong coupling, the filtered model has a unique, symmetric, gapped ground state with no order-parameter growth with size.
- **TG1-BROKEN:** degeneracy or order that grows with size (an SSB precursor), or a gapless sector.
- **OPEN:** otherwise.

## Panel D work items (pre-registered 2026-10-14 ~21:10Z, at Jon's request: "do the recommended work then")

Memory: OBS-1 ≤ 0.3 GB per run, UV-1 ≤ 0.4 GB, BLEAK-1 ≤ 0.4 GB; one process at a time per agent. Each agent writes its detailed PREREG.md before running. These readings are fixed now.

**OBS-1. X2 observational sheet** (strategy panelist). Does the corner package survive data before any compute is spent?
- **R1, flavour–strain (X2-L8).** Compute the first-order strain coefficient that nontrivial CKM forces on the hw1 generation corners (at least one branch; state all branches tried). Map it to the m_p/m_e drift under the measured nHz GW background (clock bound ~4e-17/yr) and to matter-sector Lorentz-violation bounds.
  - **FLAV-KILL:** more than 10× over a bound on every allowed branch.
  - **FLAV-NEAR:** within 10× on some branch.
  - **FLAV-SAFE:** below 1e-2 of all bounds on every branch.
  - **OPEN:** otherwise.
- **R2, Z₄^F on the light sector.** Is Z₄^F exact on the light sector of the full X2 law, including leakage operators and electroweak breaking?
  - **Z4-EXACT:** implies Dirac neutrinos and no 0νββ, stated as a prediction.
  - **Z4-BROKEN:** name the breaking operator.
  - **OPEN.**
- **R3, proton decay.** From X2's leakage, the floor on 1/a set by Super-K's proton lifetime.
  - **PDK-SAFE-AT-PLANCK:** passes at a = ℓ_P; state the floor.
  - **PDK-FAIL-AT-PLANCK.**
  - **OPEN.**

**UV-1. Is the RP failure a grid-scale effect?** (qinfo panelist). Reuse K2c's code (2D U(1), vector-like overlap, hard support). Use gauge coupling β_g > 0 (at least 3 values, e.g. 1, 4, 8) and W-matched witnesses restricted to test functions supported at distance ≥ t₀ from the reflection plane (t₀ = 1, 2, 3, 4), on tori Lt = 12–20.
- **UV-ONLY:** at every β_g, the negativity vanishes (PSD at power) for t₀ ≥ t\* with t\* ≤ 3 lattice spacings.
- **PERSISTS:** a quadrature-converged negative eigenvalue at t₀ ≥ 3 for some β_g.
- **OPEN:** otherwise.

**BLEAK-1. Set B's RP-safe gravity bridge and the matter light cone** (gravity panelist).
- **Setup.** On Euclidean Z⁴, couple a free scalar, then a Wilson fermion, to the spatial-TT graviton plus R19-33's D2 bridge (the only site-RP realization on record). Compute at one graviton loop the matter time–space speed row allowed by the residual W(B3)×Z₂ᵀ symmetry.
- **Control.** The same loop with K2's exactly conserved stress, where W(B4) forces the row to zero.
- **Readings** (|δc| at a = ℓ_P with the canonical coupling):
  - **LEAK-ZERO:** zero by an identity.
  - **LEAK-SMALL:** below 1e-15.
  - **LEAK-PLANCK:** |δc| ≥ 1e-6.
  - **OPEN:** otherwise.

**COL-1. Can colour be carried by combinations of sites?** (Pre-registered 2026-10-14 ~21:12Z. Jon asked: "why does the site need to carry the color — can't it be combinations of sites that carry it?")
- **Plain question.** The qinfo panelist's "≥ 16 modes per site" assumes the colour gauge transformations act on each single site's state space (on-site). Can the components of a colour triplet live on different qubits, with:
  - (i) exact local SU(3) gauge invariance (a Gauss law), and
  - (ii) covariance under one-step translations, possibly twisted by an internal relabelling as in staggered fermions (shift ⊗ a cyclic colour permutation, which lies in SU(3)), and
  - (iii) nearest-neighbour or finite range?

  If not, what exactly forces the gauge "cell" to be a block, and what does a twisted, non-on-site realization cost? Relate this to non-on-site symmetry gauging (Seifnashri–Shirley; Thorngren–Preskill–Fidkowski disentanglers) and to emergent gauge fields.
- **Setting.**
  - One complex fermion mode or qubit per site on Z³ (and a Z¹ toy first).
  - SU(3) acting on clusters.
  - Classify the possible assignments of colour components to sites compatible with (ii).
  - Test whether a local Gauss law exists (gauge generators as local operators on clusters that commute with each other and generate SU(3) at every point). Check it algebraically and on small clusters.
- **Readings.**
  - **COLOUR-SPREAD-OK:** an explicit assignment with (i)+(ii)+(iii) and a commuting set of local SU(3) Gauss-law generators, checked.
  - **COLOUR-BLOCK-FORCED:** proof that (i)+(ii) force the gauge cell to be a translation-breaking block, or force non-commuting overlapping generators. Name the obstruction.
  - **COLOUR-EMERGENT-ONLY:** exact local SU(3) is impossible with spread components, but an emergent or approximate version is not excluded (state what would be needed).
  - **OPEN:** otherwise.
- **Expectation.** COLOUR-BLOCK-FORCED for exact local SU(3). Overlapping cluster generators fail to commute, and a translation-twisted assignment only relabels the block lattice. Emergent colour remains open.

**SIGN-1. Is the X2 corner-package Hamiltonian sign-free for QMC?** This is the lattice lens's gate 2. (Pre-registered 2026-10-14 ~21:15Z.)
- **Question.** Does X2's Hamiltonian, or a faithful reduced version of it (walker kinetic term, the cubic-invariant filtered Spin(10)/SO(10) 10-channel quartic, or a Spin(6)/SU(4) toy), meet a known sign-free criterion? Candidates: Majorana reflection positivity (Li–Jiang–Yao), Kramers positivity (Wu–Zhang), Majorana-time-reversal classes (Li–Jiang–Yao 2016), split orthogonal group (Wei et al.).
- **Readings.**
  - **SIGN-FREE:** an explicit criterion proved to hold for the faithful model (or a stated faithful reduction), with the decomposition written out.
  - **SIGN-PROBLEM:** proof that the known criteria fail for every decomposition considered, or explicit negative or complex weights on a small cluster in a natural decomposition, with the decompositions tried listed.
  - **OPEN:** otherwise.
- **Memory:** ≤ 0.2 GB.

**NT-3 result (21:20Z, same family; referee launched).**
- **Literal pre-registered reading: TG1-BROKEN.** The infinite-coupling gap falls with size for all three 1D filters, and the 6-channel susceptibility grows.
- **Worker's interpretation: OPEN.** The triggers are light-adjacent softening forced by the filter's zero (proof skeleton). The pre-registered light-attribution metric misfires for the self-conjugate sector.
- **Holds either way (checked):**
  - a unique SU(4)-singlet ground state everywhere;
  - no static order growth beyond the control [referee: too strong; read "no static-LRO threshold violation"];
  - the mirror corner stays gapped [referee: not established];
  - the cube gap is 1.31/1.65 against 1.0 on-site.
- **Next:** T-G1′ (2+1D at finite W), gated on SIGN-1.
- Memory overrun of ~1.1 GB for ~10 s, recorded.

**NT-2 result (21:19Z; same family; referee launched): PG3-NEG.**
- The hard plaquette bound is not RP in 3D pure U(1):
  - proved exactly on the 2×2 periodic slice (rational inertia (5,1), every δ < π/4) and on the 1×2 open strip (inertia (15,1), every δ < π/3);
  - converged negative on the open 2×2 block (smooth test functions).
- **Mechanism:** the cusp coefficient becomes a flux kernel with a negative direction in 3D.
- **Fix:** a positive-type profile with the same support restores pure-gauge RP. That is law data, not an axiom change, but it does not rescue the overlap.
- **Correction owed:** K2c and its referee's "3D/4D suggested" → "3D not RP" [referee: for the stated finite geometries; 4D still suggested].
- **Memory incidents:** a 5.2 GB run was killed by the supervisor; later watchdog kills were recorded.

**UV-1 amendment (2026-10-14 ~21:21Z, written before any UV-1 run).**
- **Why.** NT-2 showed the hard plaquette support is itself non-RP (3D; odd Lx in 2D). With a hard weight, a negative eigenvalue would mix gauge-weight and fermion effects.
- **Change.**
  - UV-1 runs **two arms**:
    - **(primary)** the positive-type triangle (Fejér) profile with the same support, which isolates the overlap determinant;
    - **(secondary)** the hard support, as originally registered.
  - The readings UV-ONLY / PERSISTS / OPEN are unchanged and are applied to each arm separately. The primary arm decides the headline.

**BLEAK-1 result (21:44Z; same family; referee launched): LEAK-PLANCK.**
- **Result:** one graviton loop through R19-33's RP-safe foliated gravity (spatial-TT plus instantaneous bridge) gives δc = (π/6)(ℓ_P/a)² exactly for a massless scalar (proved closed form; checked four ways).
- **Control premise refuted:** K2's conserved stress gives the same π/6 through the TT + bridge loop. Only the covariant (non-RP) graviton gives zero. The off-shell internal line defeats the on-shell identity.
- **Comparator:** a Wilson fermion gives about 0.85 (stress-dependent), so the shift is species-dependent.
- **Pass scales:** 1/a ≤ 5e11 GeV (10⁻¹⁵) or ≤ 5e8 GeV (10⁻²¹); otherwise one tuned counterterm per species per order.
- **Reading:** R19-28's "charge block = 0 by W(B4) at all orders" does not survive RP gravity.
- **Memory:** one run peaked at 443 MB (rerun at 245 MB, identical results).

**OBS-1 result (21:46Z; same family; referee launched).**
- **R1: FLAV-NEAR.** One loop, U(1) stand-in, SF strain.
  - Branch B (circulant up quarks and charged leptons, CKM in the down sector) gives an m_p/m_e drift of ×0.12–2.5 the clock bound.
  - Branch A (corner-aligned generations) gives ×80–360.
  - Branch B′ gives ×2–93.
  - Lemmas: staggered reflection makes on-site terms flavour-blind; circulant sectors are strain-blind.
- **R2: Z4-EXACT** (conditions: no ν^cν^c term; symmetric mirror phase). In fact X2 has an exact U(1)_{B−L}: Dirac neutrinos, zero 0νββ, no n–n̄ oscillation. The named breaking operator is ν^cν^c.
- **R3: PDK-SAFE-AT-PLANCK.** The floor is 1/a ≳ 2e16 GeV in the worst case. The skeptic's rate formula overstates by about 4800× [referee: 580–8100× across the packet's ranges].
- **Biggest open hazard:** the flavour-pattern Lorentz-violation anisotropy from corner-selective Yukawas (suggested, not computed), which needs a lattice Yukawa loop.

**COL-1 result (21:57Z; same family; referee launched).**
- **Class M (qubits, many-body colour charges): COLOUR-SPREAD-OK.**
  - Explicit constructions on Z¹ and Z³ with exact local SU(3) Gauss laws, one-step translation covariance of the law, finite range, and the colours on different qubits.
  - Checks: su(3) relations to ~1e-16, commuting generators, [H, G] = 0.
  - Forced costs:
    - OWN: each colour point needs a private register of at least 2 qubits, since shared qubits are read-only [referee: not proved; OWN gives private algebraic tensor factors, not private physical qubits; 4-qubit counterexample];
    - CAP: simultaneous colour density ≤ 0.63 per site, so colour is hard-core;
    - cells are marker patterns of 19 (Z¹) or 35 (Z³) qubits;
    - the linked example's vacuum breaks translations to one in 19 or 35;
    - Z³ ignores cubic rotations;
    - QCD universality is open.
- **Class Q (elementary quadratic charges): COLOUR-BLOCK-FORCED.** Proved: N ≥ 3|I| and translations force |I| ≥ N.
- **Memory:** the cap was breached three times (up to 1.61 GB), and reruns within the cap reproduced every result.

**SIGN-1 result (22:06Z; same family; referee pending).**
- **SIGN-FREE** for the ungauged X2 with global Spin(10) wherever λ1 ≤ 0 and |λ2|/|λ1| ≳ 0.15–0.18. This includes the pure BB + h.c. symmetric-gapping term. [Referee: rigorous at λ1 = 0; certified for λ1 ≤ 0 with |λ2/λ1| ≥ tan 10° ≈ 0.176, once the remainder is corrected. See below.]
- **Mechanism:** particle–hole swap one 8 of the Spin(8)×Spin(2) split. This gives a Kramers pair T1, T2 (both squaring to −1, anticommuting) with U(1)_c, i.e. Wu–Zhang / Li–Jiang–Yao Kramers class.
- **Evidence:** an explicit decomposition (an exact Fierz identity at λ1 = 0) and positive cluster weights (phase ≤ 4e-13; ≤ 4e-7 at W = 8). The natural 10-channel decomposition has a phase problem.
- **OPEN:** λ1 > 0.
- **Not covered:** the gauged model (no G_SM-invariant 2-plane in the 10).
- **Scope:** sign-freeness does not decide symmetric gapping; the sign-free region is the GPR-risk region.
- **Memory:** cap breach recorded (586 MiB resident).

**Referee verdicts on NT-2, NT-3, BLEAK-1 and OBS-1 (codex gpt-5.6-sol, xhigh; recorded 22:10Z; each returned 21:22–21:55Z). All four: CONFIRMED WITH CORRECTIONS.**
- **NT-2 → PG3-NEG confirmed.**
  - The referee independently reproduced T22 (exact inertia (5,1), vector value −27/12500·(2π)⁻³, every 0 < δ < π/4) and O12 (inertia (15,1), δ < π/3).
  - O22 is confirmed as quadrature-converged (λ_min −1.6082e-3), not as a certified analytic bound.
  - **Correction (scope):** pure compact U(1), β_g = 0, flat hard indicator, link reflection, and the stated finite geometries. This disproves universal finite-lattice RP. It does not prove non-RP for every geometry, the infinite-volume state, or 4D.
  - The K2c admissible-boundary residual is closed for finite 3D; 4D stays suggested.
  - **Record:** the runner's final-message output overwrote the referee's own 168-line record. It was recovered verbatim from the run log as REFEREE_RECORD_FULL.md, and the runner was fixed (v2).
- **NT-3 → literal TG1-BROKEN confirmed; the worker's OPEN does not follow the fixed wording.**
  - The referee's independent block solver reproduced Δ₆, S₆ and the cube gaps 1.312 / 1.648.
  - **Corrections:**
    - "no static growth beyond the control" is too strong: the mirror ratios 1.346 and 1.323 exceed C1's 1.219, though they stay under the 1.4 threshold;
    - "87–99.95% near-light" covers only F★ and F_hi; F_lo is at 59–67%;
    - "**the mirror corner stays gapped**" is **not established**: the resolved levels capture 0–0.1% of the spectral weight.
  - A filter zero gives an exactly free mode in the unrestricted space. That is not a proof of a vanishing restricted gap for every filter; the softening is observed and naturally explained only for these three 1D filters.
  - **Consequence:** NT-3 neither kills nor defuses GPR. G1 and G2 stay open (K1:202).
- **BLEAK-1 → LEAK-PLANCK confirmed.**
  - The referee independently reproduced I_s − I₄ = −1/96 and δc = (π/6)G/a², and confirmed that K2 gives the same row for the stated off-shell reason.
  - **Corrections:**
    - "a seagull would cancel it" is not proved: a seagull can change or be tuned to cancel the row;
    - the deleted zero mode is a stated prescription, so another prescription can add an anisotropic O(p²) term;
    - the result is a bare, prescription-dependent exchange coefficient, not a gauge-complete observable;
    - at a = ℓ_P it is formal (G/a² = 1);
    - the Wilson comparator (0.8497) is diagnostic only.
- **OBS-1 → R1 numerics, R2 and R3 confirmed with narrowed scope.**
  - **R1:** fresh N = 40 runs reproduce L₀, the leak and K, and the clock slopes and bounds check against Lange et al. and NANOGrav 15-yr. **Corrections:**
    - FLAV-NEAR holds only for the registered E_g, U(1), bilinear-proxy completion; the complete X2/SM reading stays OPEN (T₂g, the non-abelian chiral loop and the mirror self-energy are uncomputed);
    - the staggered-reflection lemma fails once the non-on-site mirror proxy is inserted;
    - the circulant lemma does not suppress the CKM-broken down sector.
  - **R2:** confirmed conditionally. **Correction:** the protection is the manifest cutoff symmetry [H_X2, Q_X] = 0, not anomaly freedom; electroweak breaking leaves U(1)_{B−L} (X + 4Y), not bare X.
  - **R3:** arithmetic confirmed (Γ formula, Super-K 2.4e34 yr, 1/a ≳ 1.95e16 GeV at c_eff = 10). **Corrections:** the "4800×" holds only at the representative point (580–8100× across ranges); PDK-SAFE is conditional on the assumed c_eff ≤ 10, and X2's leakage coefficient is not derived.

**NT-1 result (22:16Z; same family; referee launched): CHI-RP-FAIL.**
- **Setup:** a genuinely chiral, anomaly-free 2D U(1) measure ("11112": four left-handed charge-1 Weyl fermions plus one right-handed charge-2). Overlap Weyl determinants; Lüscher's abelian phase (straight-path transport plus a gauge-restoring current).
- **Checks:** exactly gauge invariant (1e-7 to 1e-8); reflection condition ρ(θU) = conj ρ(U) to 1e-13, so the kernel is Hermitian.
- **Result:** the kernel has a certified negative eigenvalue on 4/4 W-matched pools (open time, Lt = 12 and 20), at 4,600–13,600 × the error estimate. The Wilson and pure-gauge controls are PSD.
- **Power reference:** the vector-like K2c values are reproduced to every printed digit. The chiral violation is 4.4–4.7× larger.
- **Mechanism:** the phase plays no role on these witnesses. The kernel equals the modulus kernel, and |ρ_χ| = |det D(1)|²|det D(2)|^{1/2}. So the failure is the overlap's own non-positivity, carried over to the chiral theory.
- **Not tested:** anomaly cancellation (at Lx = 2 even an anomalous single Weyl fermion is gauge invariant), the torus, Lx ≥ 4, 4D, non-abelian groups, 3-4-5-0.
- **Consequence:** the chiral measure is no escape from K2c's failure, so the X3 contingency stays triggered. [Referee: NOT CONFIRMED. The measure's legitimacy (locality, global integrability) is not established, so the strict reading is OPEN; what is shown is the RP failure of the fractional-power modulus. See the referee entry below.]
- **Deviations:** registered gate G4 failed and was replaced by Richardson extrapolation before any kernel was computed; a sign bug was fixed (either sign gives FAIL).

**COL-1 referee (codex gpt-5.6-sol, xhigh; returned 22:12Z; recorded 22:18Z): CONFIRMED WITH CORRECTIONS.** COLOUR-SPREAD-OK is met as fixed.
- **Confirmed:**
  - Lemma C and the parse lemma. Incompatible markers give P_xP_y = 0; compatible ones have disjoint registers and colour-blind projectors. So the generators commute, and [PQ^aP, PQ^bP] = if^{abc}G^c holds on the full Hilbert space.
  - Full-space gauge invariance of H. The referee added an independent predicate-pullback check, because pair creation changes occupancy; it found no projector toggles.
  - The Z¹ matter-only checks, reproduced at L = 14–18 (224 MB).
  - Class Q, within its domain (finite range, elementary quadratic or BdG charges, a gauge point in every translation orbit).
- **Corrections:**
  - **OWN does not force private physical qubits.** The commuting-algebra decomposition gives private *algebraic tensor factors*. An entangling basis change can put two commuting SU(3)s across the same shared qubits; the referee gives an explicit 4-qubit counterexample with zero cross-commutator, both acting quantumly on both shared qubits. So "≥ 2 private qubits per colour point" is not proved.
  - **CAP** (≤ 0.63 per site) holds only for colour charges carried *in one joint sector*. It does not bound gauge factors that live in mutually exclusive sectors.
  - The gauge representation is highly reducible and state-controlled: SU(3)_x acts trivially outside valid marker sectors. Lemma C should have been written out, not invoked.
  - The low-memory linked rerun covered offset 0 only, with the covariance fields set to nan, so REPORT:146 overstates it. Covariance follows exactly from the definitions anyway.
  - "The vacuum breaks translations to 1 in 19" is not proved: the fixed-offset marker sector is crystalline, but no ground state was computed.
  - The Seifnashri–Shirley and Thorngren–Preskill–Fidkowski citations are context, not coverage.
- **Strongest correct statement (referee):**
  - One 2-dimensional site cannot carry SU(3).
  - One-mode-per-site elementary quadratic colour charges cannot give a Gauss generator at every translation-related point.
  - But one-qubit sites can collectively carry exact, finite-range, one-step-translation-covariant SU(3) through gated many-body representations, with a commuting Gauss law and gauge-invariant local dynamics.
  - The construction is kinematic, state-controlled, anisotropic in Z³ and sector-crystalline.

**UV-1 result (22:49Z; same family; referee launched): OPEN for both arms (headline OPEN).**
- **Why OPEN:** registered in advance as forced by budget. At finite β_g on a torus, t₀ ≥ 2 is an 11–19-dimensional integral.
- **Supplementary (checked):**
  - **t₀ = 1 (torus):** negative at every β_g = 0–8 in both arms, changing by less than 2% across β_g.
  - **t₀ = 2 (open proxy, finite β_g):** negative in all 8 cells, at about 1/57 of the depth-1 value.
  - **β = ∞ (flat field near the plane):** negative to t₀ = 4 at Lt = 20 (−7.8e-6, −5.9e-7, −1.4e-8, −9.5e-11), confirmed by a second seed and reproduced by K2c's independent builder.
- **Reading:**
  - the violation lives in the overlap determinant, not in gauge fluctuations;
  - its decay length is lattice-scale (0.2–0.4 spacings) and independent of β_g;
  - it never reaches zero at finite depth, which leans to PERSISTS at fixed lattice depth;
  - a continuity lemma (worker's; unrefereed) gives non-PSD at finite depth for all β above some β₀, but β₀ is not computed.
- **For set B:** exact OS reconstruction fails at every depth in this proxy. An approximate transfer matrix with e^{−κt₀} errors is plausible but not shown.
- **Additions after registration:** the β = ∞ comparator and the continuity lemma.

**SIGN-1 referee (codex gpt-5.6-sol, xhigh; returned 22:22Z; recorded 22:50Z): CONFIRMED WITH CORRECTIONS.** SIGN-FREE is met, narrowly.
- **Confirmed:**
  - T1² = T2² = −1 and {T1, T2} = 0 exactly.
  - All 1,024 HS channels have the required parities and commute with U(1)_c. The walker and any real flavour-blind filter keep the symmetries, so every HS slice is Kramers-class (Wu–Zhang; Li–Jiang–Yao).
  - The quartic identity, checked exhaustively over all 635,376 components: residual 4e-16 at 230° and 3e-16 for the 270° Fierz identity.
  - Cluster weights, reproduced with the corrected Hamiltonian: maximum phase 1e-14 at W = 0.5 and 2e-12 at W = 8, stabilised.
- **Corrections:**
  - **The cluster code's filtered remainder is wrong for λ1 ≠ 0.** With F Fᵀ = ρI, the remainder must be ρFᵀK_RF, and the scalar part takes a factor ρ² (ρ = 3/8 for the 4-site filter). The fix keeps Kramers symmetry, and R = 0 at λ1 = 0.
  - The full trace is det(1 + M_d)/√det M_d. The denominator is positive.
  - The four-form image has rank 12, not 11, so the worker's minimal-norm correction did not by itself establish an exact identity. A rank-12 correction stays strictly inside the cone at 230° (margin 0.318).
  - At 270°, the worker's minimal correction has a negative margin (−4.3e-7). The exact Fierz solution (−34, +2, −2, +2) repairs it, with margin 2.
  - REPORT:90-97 is incomplete: it omits four density blocks and does not specify R.
  - **Certified region:** an exhaustive 190° check (margin 0.0156) plus convexity gives λ1 ≤ 0 and |λ2/λ1| ≥ tan 10° = 0.1763. The "0.15–0.18" is a bracket, not a sharp threshold.
  - The P1 classification of admissible MTRs is underproved: representatives were built, not classified.
  - The gauged obstruction (no G_SM-invariant real 2-plane in the 10 = 6 + 4) kills this fixed-U(1)_c construction only, not every sign-free construction.
- **Strongest correct statement:** the ungauged X2 matter Hamiltonian with a real flavour-blind filter is rigorously Kramers-class sign-free at λ1 = 0, λ2 ≠ 0. With the remainder corrected, it is numerically certified with strict margin throughout λ1 ≤ 0, |λ2/λ1| ≥ 0.1763. λ1 > 0 and the dynamically gauged theory remain open.

**NT-1 referee (codex gpt-5.6-sol, xhigh; returned 22:26Z; recorded 22:50Z): NOT CONFIRMED. The strict reading is OPEN.**
- **Confirmed:**
  - The Weyl projectors, chirality conventions and determinant factorisation.
  - **The negative eigenvalues on all four pools:** independent full-kernel polar-overlap rebuilds agree with the saved kernels to 1.6–3.3e-14, stable from n = 16 to 32. The witnesses are exactly W-matched and admit gauge-invariant bump realisations.
  - The reflection lemma (for a separating class of witnesses) and the F3 sign fix. No global sign or phase can make the kernels PSD.
  - |ρ_11112| = C|det D(1)|²|det D(2)|^{1/2}.
- **Verdict-controlling defect: the measure is not shown to be a legitimate Lüscher measure.**
  - Gauge invariance holds numerically at the transport resolution, not exactly.
  - The cumulative current is not shown to meet the locality, symmetry and global-integrability conditions of Lüscher's reconstruction theorem. That theorem is for periodic finite volume and does not directly cover Lx = 2 with open time.
  - The anomalous L1 model is gauge-restored just as well, which exposes the gap.
  - So the phase is "a numerically gauge-restored chart prescription", and the CHI-RP-FAIL setup gate (a gauge-invariant chiral measure) is not met.
- **Phase constancy** also holds for the anomalous L1 and for isolated L2/R2. It is a property of the restricted Lx = 2, open-time, W-matched sector, not of chiral measures.
- **What is new beyond K2c:** RP failure of the fractional-power overlap modulus |det D(1)|²|det D(2)|^{1/2}. No chirality- or anomaly-specific mechanism is shown.
- **Consequence:** route 1's "chiral measure escapes K2c" question is **not closed**. It needs Lx ≥ 4 and a measure that meets Lüscher's conditions (or Kadoh–Kikukawa's).

**UV-1 referee (codex gpt-5.6-sol, xhigh; returned 23:15Z; recorded 00:26Z 10-15): CONFIRMED WITH CORRECTIONS.** OPEN is the correct reading for both arms.
- **Why OPEN:** PERSISTS needs a convergence-checked finite-β torus negative at t₀ ≥ 3, and none was computed. The β = ∞ result was registered as a comparator only.
- **Confirmed:**
  - The β = ∞ comparator is the legitimate limit of both arms' diagonally normalised kernels. The residual Polyakov holonomy stays Haar-integrated, and the field is not globally flat.
  - Lt = 20, t₀ = 4: −1.50797e-9 reproduced at 12, 24 and 48 Polyakov nodes (gap ≥ 0.78).
  - The continuity lemma, for each fixed pool. It gives no useful β₀.
  - Stage B's bug fix. A primary-arm β = 8 2×2 subkernel stays negative from n = 2 to n = 4 (about −8.42e-6), so the registered depth-2 threshold is securely met.
- **Corrections:**
  - "Exact-kink" describes the domain partition, not exact integration of the determinant.
  - A β-independent decay exponent, or a universal 0.2–0.4-spacing decay length, is not established: the deep points use separately optimised pools, and only t₀ ≤ 2 was tested at finite β.
  - Exact OS reconstruction already fails for each tested finite measure once any t₀ = 1 witness is negative. But "fails at every depth", failure in the continuum, and a full set-B no-go are not established.
- **Strongest correct statement:** in the finite 2D U(1) overlap proxy, finite-β torus RP negativity is established at t₀ = 1, the open proxy stays negative at t₀ = 2, and the normalised β → ∞ torus kernel is independently negative at t₀ = 3 and 4. So an exact compact-depth UV cutoff is excluded in substance for large enough β. The evidence supports an exponentially small lattice-scale tail, not a physical-depth or continuum obstruction.

---

## 24-hour campaign, wave 1 (pre-registered 2026-10-15T00:28Z; Jon: "run another 24 hour campaign")

**Scope.** Jon took the "what's next" plan as the campaign. Route 2 (the X2 corner package) first: a cheap kill test (OBS-2), then the sign-free simulation pilot SIGN-1 unlocked (QMC-1). Route 1 gets the corrected handed-measure test NT-1 owes (NT-1′). Wave 2 is pre-registered later, after wave 1 reads out.

**Common rules.**
- Agents are Opus 5.5 at xhigh (same family; not independent). Each is refereed by codex gpt-5.6-sol at xhigh before its result is used downstream.
- Every agent writes a detailed PREREG.md before any run. The readings below are FIXED and may not be changed.
- **Memory:** a per-run cap is enforced by a watchdog wrapper; one process at a time; OMP_NUM_THREADS=2.

**OBS-2. X2's flavour-pattern Lorentz violation and the T₂g strain channel** (route 2 kill test; OBS-1's open hazard). Cap 0.4 GB.
- **Setup.** X2's walker carrier with corner-selective Yukawas and a lattice Higgs (nearest-neighbour), at one loop. Branches A, B and B′ are as in OBS-1; B is primary.
- **What to compute.** Separate each charged-fermion mass eigenstate's Yukawa-induced Lorentz-violating kinetic terms (dimension 4) into:
  - (i) the part set C's existing counterterm removes: one cubic-invariant kinetic counterterm per SM field (OBS-1 REPORT:74-78);
  - (ii) the residual (flavour-pattern) part.

  Compare (ii) with the current SME bounds (Kostelecký–Russell data tables; cite the table and row).
- **LV readings:**
  - **LV-SAFE:** on branch B, every residual is within its bound with no further counterterms.
  - **LV-PRICE(n):** some residual exceeds its bound, but n named, local, X2-symmetric counterterms remove it. State n and the tuning level.
  - **LV-KILL:** a residual exceeds its bound, and no local counterterm respecting X2's symmetries (unit translations, cubic rotations as realised on the corners, Spin(10) ⊃ G_SM) can remove it.
  - **OPEN:** otherwise.
- **T₂g strain.** Add the T₂g (off-diagonal) strain response to OBS-1's E_g. The rate is the m_p/m_e drift under the nHz GW background, against the 3.6e-17/yr clock bound.
  - **FLAV2-KILL:** more than 10× over the bound on every branch.
  - **FLAV2-NEAR:** within 10× on some branch.
  - **FLAV2-SAFE:** below 1e-2 of the bound on some branch.
  - **OPEN:** otherwise.

**QMC-1. Sign-free simulation pilot of X2's mirror gapping** (T-G1′ pilot; field question I). Cap 1.5 GB per process.
- **Model.** Ungauged X2 with global Spin(10), at λ1 = 0, λ2 ≠ 0: rigorously Kramers-class sign-free (SIGN-1 and its referee).
- **Geometries.** 1+1D and 2+1D analogues: walker Σ σ_a sin p_a; a real filter vanishing exactly at the light corners; the filtered BB + h.c. channel.
- **Power reference.** The unfiltered on-site control (f ≡ 1).
- **Measure, as functions of W:**
  - the 10-vector structure factor S₁₀(L), the symmetry-breaking signal;
  - the mirror single-particle gap, from imaginary-time Green's functions at the mirror corners;
  - the light-corner Green's function.
- **Validation gate (must pass before any production reading):**
  - (i) W = 0 reproduces the free Green's functions exactly;
  - (ii) every sampled weight is real and positive (relative phase ≤ 1e-8);
  - (iii) one observable at finite W agrees with an exact method (ED or enumeration) at one small size, within statistical error;
  - (iv) on even L at finite W, the light-corner Green's function equals the free one (X2-L2).
- **Readings:**
  - **SMG-PILOT:** in 2+1D there is a W window where, between L = 4 and L = 6, the mirror gap is open and stable within errors and S₁₀/L² decreases.
  - **GPR-PILOT:** in 2+1D, at every W where the mirror gap is open, S₁₀/L² is flat or growing between L = 4 and 6 (the mirrors gap by breaking the symmetry).
  - **OPEN:** otherwise, including "sizes cannot separate" and "validation not passed in budget"; state which.
- **Deliverable either way:** validated code with a cost model for a cluster run at L = 8–12 and in 3+1D.

**NT-1′. A legitimate chiral measure and gauged RP** (route 1; the referee's open item from NT-1). Cap 0.5 GB.
- **Setup.** 2D U(1) overlap with an anomaly-free chiral charge set (3-4-5-0 if admissible at feasible δ, otherwise 11112), link reflection, W-matched gauge-invariant witnesses as in K2c.
- **Setup gate G-LEG.** It must pass before CHI-RP-FAIL or CHI-RP-PASS can be read:
  - (a) Lx ≥ 4;
  - (b) the measure term follows Lüscher's construction (NPB 549 (1999) 295) or an explicit published 2D U(1) construction (for example Kadoh–Kikukawa). Gauge invariance is exact to roundoff. Locality is measured: the response of the measure current to a local variation decays exponentially with distance;
  - (c) **anomalous control:** the same construction applied to an anomalous charge set visibly fails gauge invariance, locality or integrability;
  - (d) the reflection condition ρ(θU) = c·conj ρ(U) is measured.
- **Readings:**
  - **CHI-RP-FAIL:** G-LEG passes, and the kernel has a quadrature-converged negative eigenvalue below −10× the error estimate.
  - **CHI-RP-PASS-at-power:** G-LEG passes, and the kernel is PSD within error, using the vector-like K2c witness on the same geometry as the power reference.
  - **OPEN:** otherwise, naming the failed gate item.

**Campaign interruption (recorded 11:22Z on 10-15).** The supervisor's session ended at about 00:47Z, and all three wave-1 agents stopped with it.
- **Progress at the break:**
  - OBS-2 had its PREREG and kinetic runs up to N = 96;
  - QMC-1 had its PREREG and a model builder;
  - NT-1′ had literature only, and no PREREG yet.
- **Resumed at 11:22Z** from the agents' own transcripts, with new deadlines: OBS-2 14:00Z, NT-1′ 16:30Z, QMC-1 18:30Z.
- **Close:** the campaign close moves to about 11:30Z on 10-16, so the campaign still gets 24 working hours.
- No reading or pre-registration was changed.

**OBS-2 result (11:38Z; same family; referee launched): LV-PRICE(19) [14 if set C's counterterm already includes the tetragonal operator]; FLAV2-NEAR.** [Referee: CONFIRMED WITH CORRECTIONS. LV-SAFE fails robustly; the integer n is not established as minimal. See below.] [OBS-3, refereed: this price is texture-dependent and not forced by CKM at one loop.]
- **Where the residual sits.** On branch B, the up quarks and charged leptons are circulant, so their flavour-pattern Lorentz violation cancels exactly. The residual comes from the CKM-broken down sector.
  - d quark: c_TT ≈ −2e-8 (range −0.9 to −3.5e-8; −(1.8–7.1)e-9 with Planck-scale couplings). The bound is Kostelecký–Russell D44 part 3, c_TT^d > −1e-22 (astrophysics): ×2e13–3.5e14 over.
  - s quark: ×1.5–28 over the kaon row (mapping suggested).
  - e, μ, τ, c, b, t: within their bounds.
- **The counterterm price.**
  - 14 flavour-pattern kinetic coefficients on Q and d^c. They need tuning of 3e-15 to 6e-14 of the residual, and they are cubic-covariant only with a flavour spurion.
  - Plus 5 tetragonal A₁ counterterms Σσ_a sin p_a(cos p_b + cos p_c), one per charged field. Set C's speed counterterm cannot do their job.
  - No reallocation of set C's counterterms gives LV-SAFE.
- **T₂g gives no first-order spin-averaged mass shift** (proved by little-group symmetry; checked to ≤1.5e-13). The clock row (E_g + T₂g) on branch B is ×0.09–2.5.
- **Side finding (checked).** OBS-1's spin-blind (π,π,0) mass condensate is itself Lorentz-violating at dimension 3 (±0.385 q²). A τ_xσ_c condensate is exactly isotropic. This is a completion fix, not a kill.
- **Scope.** One loop; a nearest-neighbour Higgs in the symmetric phase; corner symbols g_c = (1 − cos k_c)/2; IR regulators and vertex placements varied (about ×4 spread); N-converged to under 2%. No running from 1/a.
- **Supervisor's own-thread comparison.** I predicted n ≈ 6 with LV-SAFE possible, and named the top quark as the main hazard. I missed that circulant sectors cancel exactly and that the CKM-broken d quark against a 1e-22 astrophysical bound is the binding row.

**OBS-2 referee (codex gpt-5.6-sol, xhigh; returned 11:51Z; recorded 11:52Z): CONFIRMED WITH CORRECTIONS.**
- **Confirmed.**
  - The referee's independent projector calculation (`ref_check.py`) reproduces c_TT^d = −2.1067e-8 (Δ = 0) and −2.1176e-8 (Δ = 0.5) at N = 24, together with d_TT^d ≈ +7e-9. The negative sign is confirmed.
  - The SME map c_TT = −(3/4)δv is correct.
  - **LV-SAFE fails robustly:** the direct d-quark vector row and axial row each fail, without relying on the kaon or nucleon maps.
  - The tuning level for the binding vector row is 2.9e-15 to 5.5e-14.
  - The T₂g null for spin-averaged masses.
  - The dimension-3 side finding, with a limit of ±0.400 as q → 0 (the worker's ±0.385 is a finite-q value).
- **Corrections.**
  - **The integer in LV-PRICE(19)/(14) is not established as minimal.** Seven per field is the dimension of a generic residual tensor, not a minimal count of spurion invariants or of the combinations that observation constrains. So the strict fixed reading is LV-PRICE with n not established (OPEN on n), not LV-KILL.
  - **X2 symmetry of the counterterms** needs a specified dynamical flavour spurion: a frozen κ array breaks the cubic action.
  - **Bound-row citation.** The clean D44 part-3 rows are c̊^d − ¾κ̃_tr − ⅜(f̊^d)² > −1e-22 and |d̊^d| < 1e-22. The later row the report cited is internally inconsistent as printed.
  - **The s quark** (×1.5–28) rests on identifying the kaon's coefficient with the valence s quark, which the tables say is not known. So "no reallocation gives LV-SAFE" is conditional on that map.
  - **Circulant cancellation** holds for the own Y_u and Y_e contributions only. Physical up quarks get a residual through the shared Q_L, from Y_d Y_d†.
  - **CKM alone does not fix the magnitude.** The textures, the U_d = F·V_CKM choice, the corner symbols, the vertex placement and the regulator all enter.
- **Strongest correct statement (referee).** Within the chosen one-loop, symmetric-phase lattice Yukawa model, branch B's CKM-broken down source gives c_TT^d ≈ −(0.9–3.5)e-8 at low-scale Yukawas, with d_TT^d of order +1e-9. This violates the clean D44 c̊^d and d̊^d astrophysical rows by about 1e14. Removing it needs counterterms tuned to about 1e-14; the minimal count is not established. FLAV2-NEAR is confirmed for spin-averaged masses.

## Campaign wave 2a (pre-registered 2026-10-15T11:53Z)

**OBS-3. Is X2's flavour-pattern Lorentz violation forced by CKM?** (route 2; follows OBS-2 and its referee). Cap 0.4 GB.
- **Why.** OBS-2 found c_TT^d ≈ −2e-8 against a 1e-22 astrophysical row. Its referee found that CKM alone does not fix the size: the textures, the corner embeddings U_u and U_d, the corner symbols, the vertex placement and the left/right assignment all enter.
- **Question.** Over a stated family of X2-admissible realisations of the observed quark masses and CKM, what is the minimum flavour-pattern residual? The family must include at least:
  - generation-to-corner embeddings W_u and W_d with W_u†W_d = V_CKM (left-handed);
  - free right-handed rotations;
  - corner symbols of range ≤ 2;
  - on-site and corner-selective vertices;
  - off-diagonal entries carried by covariant τ_xσ_c condensates or flavons;
  - a nearest-neighbour Higgs.

  The residual is what remains after the per-field speed counterterm and the per-field tetragonal A₁ counterterm, both allowed. It is measured against the clean D44 rows (c̊^d, d̊^d, c̊^u, d̊^u > or < 1e-22 as printed) and the electron rows.
- **Readings.**
  - **TEXTURE-ESCAPE:** some realisation in the family keeps every direct-row residual within its bound with no further counterterms.
  - **TEXTURE-FORCED:** every realisation in the family exceeds some direct row by more than 10×. Give the minimum over the family, and a lower-bound argument if one exists, for example that the up and down embeddings cannot both be unbiased to the corner basis unless V_CKM is equivalent to a circulant.
  - **OPEN:** otherwise.
- **Scope to state:** one loop, symmetric-phase Higgs, the family as built, no running from 1/a.

**OBS-3 result (13:08Z; same family; referee launched): TEXTURE-ESCAPE.** [Referee: CONFIRMED WITH CORRECTIONS, within the declared one-loop family. See below.]
- **Main construction.** At one loop, a corner's Lorentz-violating kinetic data depend only on coupling moduli and the diagonal Gram matrix. CKM phases never enter (proved structure, S2).
  - Corner-basis Yukawas with equal diagonal moduli and equal off-diagonal moduli, plus free orientation-dependent phases ("B-gen"), fit every quark mass ratio, every |V_ij| and |J| exactly (χ² = 7e-23).
  - The data are then S3-invariant, so every residual row is zero by identity (Lemma S), for all regulators, placements, symbol ranges and carrier models.
  - The symmetric-off-diagonal version cannot fit J (best χ² 4.7e3; matches the USY literature). Orientation-selective τ_xσ_c carriers of range ≤ 2 are needed.
- **OBS-2's −2e-8 is removed by a d^c rotation alone** (M1 diagonal equalisation).
- **Proved:** W_u and W_d are both flat if and only if V_CKM is circulant-equivalent (Haagerup). The observed CKM is not circulant-equivalent (30.6σ).
- **Restricted to "up flat" with couplings carrying the mass pattern (M2):** no structural zero. A zero needs tuning to about 2e-15.
- **Outside the family (proved, symmetric-phase effective action, all orders):** a cubic-covariant law with flavour breaking only in vevs gives zero residual. What remains is about y²(va)² ≈ 1e-34 (suggested).
  - **Price not computed:** a tree-level FCNC question from the hw2 electroweak-doublet carriers with O(y_t) flavour-violating couplings.
- **Forced at two loops (suggested).** CKM forces some word in H_u, H_d to have a corner-dependent diagonal (L-words, proved). At two loops that could give about 1e-9–1e-10, i.e. about 1e13 over the u/d rows, unless the couplings are law-level covariant.
- **Supervisor's own thread:** I predicted TEXTURE-FORCED from the flatness argument. That was wrong. Flatness is sufficient but not necessary; universal-strength textures and right-handed rotations escape.

**OBS-3 referee (codex gpt-5.6-sol, xhigh; returned 13:25Z; recorded 13:26Z): CONFIRMED WITH CORRECTIONS.** TEXTURE-ESCAPE is met within the declared effective one-loop family. It is not shown for a complete, FCNC-safe, gauged X2 UV completion.
- **Confirmed.**
  - B-gen's parameterisation imposes the equalities **exactly**: one common complex diagonal entry and six exactly equal off-diagonal moduli (`univ.py:78-85`).
  - It fits the official PDG 2024 quark masses and CKM fit far inside their uncertainties (checked at 80–100 digits with mpmath).
  - Cubic covariance then puts every quark tensor in the span of α + βδ_ca, which the allowed counterterms remove exactly.
  - Also confirmed: the flat-flat ⟺ circulant-equivalent theorem, and the L-words result.
- **Corrections.**
  - **Lemma S needs fully S3-invariant data with separate, non-mixing carriers.** With selective diagonal symbols, the diagonal phases enter through Re(η_s η_t*), so equal moduli alone are not sufficient. B-gen survives because its diagonals are the same complex number. B-gen120 uses the cubic-character phase pattern.
  - **The literal saved binary64 matrices miss the direct bounds by 5e2–4e3**, through rounding. The zero belongs to the exact ansatz, not to the stored numbers.
  - **M1 diagonal equalisation** is supported for OBS-2's realisation; "for any W_u" is not proved.
  - **"Up-flat + M2 has no structural zero"** is established only to the extent of excluding the S3-invariant route.
  - **Mechanism 1's all-orders zero** holds at v = 0 (symmetric phase), not for an arbitrary fixed broken vacuum. The (va)² suppression is reasonable but uncomputed, and FCNC safety is open.
- **Strongest correct statement (referee).** The exact B-gen parameterisation fits the observed quark data while making the one-loop data S3-invariant, so every quark tensor is removable by the allowed counterterms. OBS-2's d-quark violation is therefore texture-dependent and not forced by CKM at one loop.

## Campaign wave 2b (pre-registered 2026-10-15T13:27Z)

**OBS-4. Tree-level FCNC from the corner carriers in X2's texture escape** (route 2; the hazard OBS-3 and its referee named). Cap 0.4 GB.
- **Why.** OBS-3's escape (B-gen) needs off-diagonal corner Yukawas of size about y/3. These are carried by fields at the corner-difference momenta (hw2): orientation-selective τ_xσ_c carriers, flavons, or a Higgs degenerate at those momenta. Their physical scalar modes couple to quark mass eigenstates in a flavour-changing way at tree level. That is the classic multi-Higgs FCNC problem.
- **Question.** For B-gen and B-gen120, and for any other exact OBS-3 escape realisation the worker builds:
  - derive the tree-level ΔF = 2 couplings of the carrier scalars in the mass basis;
  - compare them with K–K̄ (ε_K, Δm_K), B_d, B_s and D mixing bounds (state the sources);
  - find the minimum carrier mass M* that passes every bound;
  - say whether the construction can give those carriers mass M* while their condensate supplies the electroweak-scale off-diagonal Yukawas (for example: no tuning; a tuning of a stated size; or forced to be light).
- **Readings.**
  - **FCNC-SAFE:** some exact escape realisation passes every ΔF = 2 bound with carrier masses the construction supplies without new tuning.
  - **FCNC-PRICE:** passing needs M* above a stated scale, or alignment, and that costs a named tuning or structure; state its size.
  - **FCNC-KILL:** every escape realisation built violates some ΔF = 2 bound by more than 10× for every carrier mass the construction allows.
  - **OPEN:** otherwise.
- **Scope to state:** tree level, the carrier model, the meson matrix elements used, and the running.

**NT-1′ result (14:03Z; same family; referee launched): OPEN.** The failed item is G-LEG (c), and only as the worker operationalised it. [Referee: CONFIRMED WITH CORRECTIONS; OPEN is correct, but it fails at G-LEG (b), not (c). See below.]
- **The measure.** Lüscher's construction (eq. 5.8) for 11112 at Lx = 4: straight-ray overlap basis, a local cohomology current with the monopole removed, and a finite-volume correction.
- **Gate items that pass.**
  - Gauge invariance is exact to 7e-14, via a canonical representative. The un-fixed Ward identity converges as Ns⁻⁴.
  - Locality: ν ≈ 1.6 per spacing. A small x-flat residual remains in the anomaly-free current (4.6e-4 → 1–2e-4 from Lx 4 to 8; exponential decay not shown).
  - The reflection condition holds to 1.4e-13.
- **The anomalous control, in substance.** L1's monopole defect goes 0.140 → 0.158, approaching 1/2π. Its current has a flat Wilson-line plateau ∝ 1/Lx. Without the nonlocal correction, its Ward identity fails.
  - The registered pointers for (c) were blind to x-only nonlocality, so (c) is not met as registered.
- **Kernels.** Chiral λ_min is negative on 3/3 pools (Lt 8 searched, Lt 8 random, Lt 12 random) at 22–49 × E. That is 4.0–4.7× the vector reference. The Wilson and pure-gauge controls are PSD.
- **Phase.** It now varies (7–9 mrad), but moves λ_min only at second order (0.04–1.2%). The negativity is carried by the modulus |det D(1)|²|det D(2)|^½.
- **Not tested.** Global integrability around the Wilson-line circle, counterterm freedom, Lx > 4 kernels, 4D, non-abelian.
- **If (c) is accepted on substance,** the reading would be CHI-RP-FAIL.

**OBS-4 result (14:16Z; same family; referee launched): FCNC-PRICE, at KILL level for X2 as written.** [Referee: CONFIRMED WITH CORRECTIONS; FCNC-PRICE correct; the universal 1.1 TeV ceiling and the universal KILL are not established. See below.]
- **Selection rule (proved).** Exact unit translations allow a corner-(c, c′) Yukawa only through a scalar at momentum Q_c + Q_c′. So OBS-3's escape needs three extra electroweak doublets at the hw2 momenta (four doublets in all).
- **The carriers change flavour.** In the mass basis their couplings are large: |Ŷ_uc| up to 0.66, |Ŷ_sd| about 0.015. Even the k = 0 Higgs part is flavour-changing.
- **Alignment is impossible** (proved; disjoint supports, and |V_ub| ≠ 0). Natural flavour conservation would force a permutation CKM (proved).
- **Required carrier mass M\*.** ΔF = 2 (Isidori–Nir–Perez / UTfit LR rows) needs M* ≈ 1.3e3–7.9e3 TeV untuned; D mixing and ε_K bind. Vev-tuned cancellation brings it to 15–43 TeV, but at a 4e-5 cancellation that is fragile to 1% jitter.
- **The construction cannot supply M\* (proved at tree level).** Exact translations act as Z₂×Z₂ on (H₀, Φ_K), so there is no tadpole and no decoupling limit. The carriers are forced to 1.1 TeV or less (λ ≤ 8π; global search). The shortfall is ≥ 1.4e6 untuned and ≥ 180 tuned.
- **The passing route (class S)** is an electroweak-singlet condensate at hw2, at about the lattice scale (f ≳ 0.03/a), with one light Higgs doublet and no tree-level FCNC.
  - Its cost: unit translations break spontaneously to BCC, so hw1 and hw3 share a label, and light–mirror hopping ψ†_{hw1}ψ_{hw3}S_K becomes allowed. That voids X2-L1/L2's exact-translation protection. The effect is not computed.
  - Alternatives: P2, a hierarchy tuning of about 1e-20 to 1e-25; P3, a cancellation whose existence is not shown.
- **Side findings.** OBS-3's saved B-gen has the CP-conjugate sign of J; the conjugate fit is equivalent. Light h alignment |sin ε| ≲ 5e-5 is needed within X2 as written.
- **Reading (supervisor).** CKM in X2 needs corner-changing couplings, which need translation-breaking condensates. Breaking at the electroweak scale gives light carriers and tree-level FCNC; breaking at the lattice scale removes the light-generation protection. Pending the referee.

**NT-1′ referee (codex gpt-5.6-sol, xhigh; returned 14:17Z; recorded 14:18Z): CONFIRMED WITH CORRECTIONS. The fixed reading is OPEN, failing at G-LEG (b), not (c).**
- **G-LEG (c) passes the FIXED wording.** The anomalous L1 control visibly fails locality: its monopole defect tends to the nonzero anomaly coefficient, and its current has a plateau with fixed total weight. The worker's narrower pointer cannot override the parent fixed wording.
- **G-LEG (b) is not confirmed.** The code is a serious, substantially correct finite-chart implementation of the structure of Lüscher's eq. 5.8. But its explicit finite-volume term is a global right inverse of the divergence, not Lüscher's proved exponentially small correction (compare Kadoh–Kikukawa's separate Wilson-line construction and its locality bound). The anomaly-free flat tail is not shown to be exponentially suppressed in volume, and global integrability around the Wilson-line circle is unchecked. So the sampled chart weight is not shown to complete to a legitimate global local Lüscher measure.
- **Confirmed independently.** Reloading the saved log-kernels reproduces all three λ_min (−2.4485e-3, −9.5787e-4, −5.3679e-4), their ratios to E (49.0, 26.0, 22.1), the W-matching, the reflection behaviour, and the fact that the negativity is carried by the modulus.
- **Conditional.** If the anomaly-free flat tail is accepted as Lüscher's small finite-volume term, and a chart-local measure is accepted as sufficient, the fixed rule gives CHI-RP-FAIL.
- **What would close it:** a Kadoh–Kikukawa-type explicit Wilson-line measure term with its locality bound, or a demonstration that the flat tail falls exponentially with Lx, together with the integrability check.

## Campaign wave 2c (pre-registered 2026-10-15T14:19Z)

**NT-1″. Completing the chiral measure (route 1; closes NT-1′'s referee gap at G-LEG (b)).** Cap 0.5 GB.
- **Why.** The NT-1′ referee confirmed the negative kernels and (c), but not (b). Its finite-volume term is a global right inverse of the divergence, not Lüscher's exponentially small correction. Neither the exponential decay of the anomaly-free flat tail nor integrability around the Wilson-line circle is shown.
- **Gate.** The readings (CHI-RP-FAIL / CHI-RP-PASS-at-power / OPEN) are NT-1′'s, unchanged. G-LEG (b) is made concrete by two items, and both must pass.
  - **(b′) Finite-volume part.** Either:
    - replace it with an explicit Wilson-line measure term of Kadoh–Kikukawa type (arXiv:0709.3656) and demonstrate its locality bound numerically; or
    - show that the anomaly-free x-flat tail falls exponentially with Lx: at least 3 sizes among Lx = 4, 6, 8, 10, a fitted rate > 0 at ≥ 3σ, and the L1 plateau ∝ 1/Lx as a contrast.
  - **(b″) Integrability around the Wilson-line circle.** Transport the measure around closed loops in Wilson-line space, including at least one non-contractible loop. The accumulated phase must be trivial (a multiple of 2π) to stated precision for 11112, and the anomalous control should fail.
- **Readings.**
  - **CHI-RP-FAIL:** (b′) and (b″) pass, NT-1′'s (a), (c) and (d) hold, and at least one NT-1′ pool, recomputed with the completed measure, stays below −10E.
  - **CHI-RP-PASS-at-power:** the gate passes, and the kernel is PSD within error.
  - **OPEN:** otherwise, naming the failed item.

**OBS-4 referee (codex gpt-5.6-sol, xhigh; returned 14:33Z; recorded 14:33Z): CONFIRMED WITH CORRECTIONS. FCNC-PRICE is correct under PREREG rule 10.**
- **Confirmed.**
  - S1, the selection rule, including the spin structure. D3 cross-charge bilinears are forbidden.
  - Mass-basis couplings, independently: |Ŷ⁰_uc| = 0.65695, |Ŷ⁰_sd| = 0.01506.
  - The degenerate-H/A C4 formula, and the INP Table I and UTfit Table IV rows. M* = 7693.6 TeV for B-gen and 3799.6 TeV for B-gen120.
  - The 15–43 TeV vev cancellations and their fragility at the 1e-4–1e-5 amplitude level, within that ansatz.
  - Class S: the residual lattice is BCC and every hw1 corner shares the hw3 label, so X2-L2's exact guarantee is lost. O(1/a) light–mirror hopping is symmetry-allowed but not dynamically shown to be nonzero, and no protecting residual symmetry is supplied.
- **Corrections.**
  - 0.881 TeV is a single-quartic-source estimate, not a general-potential bound. The 0.77/1.09 TeV searches reproduce but are heuristic, and the 8π optimum is not bounded from below.
  - D6 allows same-translation-charge bilinears and was not covered by the four-doublet search.
  - A Higgs-basis rotation is legitimate after translation breaking (it is a field redefinition), but H₀ is not itself the aligned physical Higgs.
  - The no-alignment and NFC lemmas hold for the stated definite-momentum D3/B-gen content. They are not a no-go against arbitrary extra fields, symmetries or propagator tuning.
  - "KILL level for X2 as written" is supported for the tested D3 spectra. It is not proved universally for D6 or for general non-degenerate potentials.
- **Strongest correct statement (referee).** In the degenerate-heavy D3 benchmark, exact B-gen textures necessarily have large flavour-changing couplings in the mass basis, and need about 1.3e3–7.9e3 TeV untuned; vev cancellations reach 15–43 TeV only through 1e-4–1e-5 amplitude tuning. Exact translations remove the ordinary D3 decoupling term, so TeV-scale active carriers are the natural perturbative outcome. But a universal 1.1 TeV ceiling and a universal X2 KILL are not established. The fixed result stays FCNC-PRICE, because the concrete high-scale singlet escape is named extra structure that breaks translations to BCC and forfeits X2-L2 protection.

## Campaign wave 2d (pre-registered 2026-10-15T14:35Z)

**CLS-1. Does class S (lattice-scale translation breaking to BCC) destroy X2's light generations?** (route 2; follows OBS-4 and its referee). Cap 0.4 GB.
- **Why.** CKM ≠ permutation needs corner-changing Yukawas (OBS-4: the NFC lemma and the selection rule). Under exact translations these need light electroweak doublets, which fail FCNC in the D3 benchmark. The passing route, class S, is an electroweak-singlet condensate at the hw2 momenta with f ≳ 0.03/a. It breaks unit translations to BCC, and the OBS-4 referee confirmed that X2-L2's exact guarantee is then lost: hw1–hw3 hopping is symmetry-allowed.
- **Questions.**
  - (i) Under BCC translations, do bilinear masses still fail to gap the light corners? Check whether the label sectors {hw1, hw3} and {hw0, hw2} contain only one chirality each.
  - (ii) How strongly do the light corners now couple to the filtered mirror interaction, as a function of the mixing set by f? Is that below the symmetric-mass-generation threshold, so the light modes stay gapless? Use mean-field, a free-fermion proxy with the mirror gap modelled by an auxiliary partner, or exact diagonalisation on a toy; state which.
  - (iii) What observable change does the mixing cause in the light sector? Consider at least velocity and Lorentz violation (does OBS-3's zero survive?), gauge couplings, and any new light–composite couplings. Compare each with bounds.
- **Readings.**
  - **CLS-SAFE:** (i) holds, (ii) leaves the light modes gapless, and (iii) is within bounds, for every f in the range the up-sector Yukawas need (g·f·a ≈ 0.33, g ≤ 4π).
  - **CLS-PRICE:** safe only for part of that range, or with a named extra tuning or structure. State its size.
  - **CLS-KILL:** for every f in that range, the light generations are gapped, or modified beyond a bound by more than 10×.
  - **OPEN:** otherwise.
- **Scope to state:** the model of the mirror gap, the dimension, and the order.

**NT-1″ result (15:06Z; same family; referee launched): OPEN at (b″). The obstruction is in the open-time geometry, not in the measure.** [Referee: CONFIRMED WITH CORRECTIONS; OPEN at (b″) is correct. See below.]
- **(b″): edge zero modes (proved; checked).** On the open-time strip, H_W has exact zero modes on the top or bottom slice whenever e·W_edge ≡ π, for any plaquettes. Every winding of the Wilson-line circle crosses such a point. So there is no admissible non-contractible loop: 0/17 at Lx 4, 0/11 at Lx 6 and at Lx 8. The anomalous L1 control is blocked the same way.
- **On a torus (descriptive):** the toron Chern number is C(11112) = 0 and C(L1) = −1. The 11112 holonomy spread decays at rate ln 2, with winding 0 against L1's 1.
- **(b′): bulk tail exponential.** ν = 0.869 ± 0.064 (13.5σ) on random fields; about ln 2 on clean backgrounds to Lx 22. L1's plateau is exactly 1/(8π)/Lx.
- **Edge tail algebraic.** Within two slices of the open edges it falls as about Lx⁻⁵ (checked to Lx 24).
  - The cause: H_W is a Chern insulator with edge-state gap sin(π/Lx).
  - Proved (elementary): any gauge-invariant current with ∂*j = 𝒜 inherits a response of at least ¼ of the anomaly's.
  - So no measure on this geometry meets a uniform exponential bound as Lx → ∞ (suggested).
- **Implication.** NT-1′'s negatives are modulus-carried, so this concerns legitimacy, not sign. A fixed-rule reading needs periodic-time RP kernels at Lx ≥ 4, which is new work: K2c's torus code covers Lx = 2 only.

## Campaign wave 2e (pre-registered 2026-10-15T15:07Z)

**TOR-1. The chiral-measure RP test on a periodic torus** (route 1). This is the geometry NT-1″ says a fixed-rule reading needs. Cap 0.5 GB.
- **Why.** On open time, H_W's edge zero modes block every non-contractible Wilson-line loop, and they make the finite-volume tail algebraic at the edges (NT-1″). The periodic torus is Lüscher's own setting (NPB 549, the finite-volume Theorem 5.4). There, NT-1″ found C(11112) = 0 and C(L1) = −1.
- **Setup.**
  - 2D U(1) on an Lx × Lt torus, with Lx ≥ 4 and Lt even (8 if affordable).
  - Link reflection, with the hard weight δ = 0.6 at β_g = 0, as in K2c.
  - Overlap fermions; charge set 11112.
  - A Lüscher measure with the torus finite-volume construction.
  - W-matched, gauge-invariant witnesses, with the vector-like witness as the power reference.
- **Gate G-LEG-T: every item must pass.**
  - (a) Lx ≥ 4.
  - (b) Gauge invariance exact to roundoff. Exponential locality of the measure current in the bulk, with no edges.
  - (b″) Transport around at least one non-contractible Wilson-line loop returns a trivial phase for 11112, and the anomalous L1 control fails.
  - (c) The anomalous control visibly fails locality or integrability.
  - (d) The reflection condition holds.
- **Readings.**
  - **CHI-RP-FAIL:** G-LEG-T passes, and the kernel has a quadrature-converged negative eigenvalue below −10E.
  - **CHI-RP-PASS-at-power:** G-LEG-T passes, and the kernel is PSD within error, with the vector-like reference negative on the same geometry.
  - **OPEN:** otherwise, naming the item.
- **Comparator.** K2c's torus results at Lx = 2: negative for the vector-like overlap at Lt = 12 and 16.

**NT-1″ referee (codex gpt-5.6-sol, xhigh; returned 15:17Z; recorded 15:19Z): CONFIRMED WITH CORRECTIONS. The correct reading is OPEN, failing (b″).**
- **The edge lemma** is confirmed for modes supported on the boundary. Independent checks on nonuniform fields give residuals of 6e-17 to 2e-16. The "iff" does not exclude unrelated bulk zero modes.
  - This is standard Wilson-fermion / Chern-insulator edge physics (Sen, PRD 102, 094520; Kaplan–Sen, PRL 132, 141604).
- **(b″) cannot be met on this strip.** Every degree-one winding of the Wilson line crosses an edge zero. Vacuous integrability on contractible pieces does not satisfy the explicit non-contractible-loop requirement.
- **(b′)'s registered bulk proxy passes** (ν = 0.8691 ± 0.0644, 13.5σ), with the L1 1/Lx contrast.
  - The edge data fit Lx^−4.974 through Lx = 24.
  - The argument that any Ward current inherits this edge behaviour is correct. But the universal asymptotic "no local measure on this strip" claim is strongly supported, not proved from finite sizes.
- **Torus topology is confirmed independently:** C_L(1) = −1 and C_R(2) = +4, so C(11112) = 0 and C(L1) = −1.
- **For route 1:** periodic-time link-reflection positivity is well defined on an even torus with two reflection cuts (Osterwalder–Seiler). A global torus measure and new kernels at Lx ≥ 4 are the natural next work (TOR-1, running). Periodic time is not the only conceivable change of geometry.
