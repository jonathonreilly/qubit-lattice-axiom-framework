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
  - no static order growth beyond the control;
  - the mirror corner stays gapped;
  - the cube gap is 1.31/1.65 against 1.0 on-site.
- **Next:** T-G1′ (2+1D at finite W), gated on SIGN-1.
- Memory overrun of ~1.1 GB for ~10 s, recorded.

**NT-2 result (21:19Z; same family; referee launched): PG3-NEG.**
- The hard plaquette bound is not RP in 3D pure U(1):
  - proved exactly on the 2×2 periodic slice (rational inertia (5,1), every δ < π/4) and on the 1×2 open strip (inertia (15,1), every δ < π/3);
  - converged negative on the open 2×2 block (smooth test functions).
- **Mechanism:** the cusp coefficient becomes a flux kernel with a negative direction in 3D.
- **Fix:** a positive-type profile with the same support restores pure-gauge RP. That is law data, not an axiom change, but it does not rescue the overlap.
- **Correction owed:** K2c and its referee's "3D/4D suggested" → "3D not RP".
- **Memory incidents:** a 5.2 GB run was killed by the supervisor; later watchdog kills were recorded.

**UV-1 amendment (2026-10-14 ~21:21Z, written before any UV-1 run).**
- **Why.** NT-2 showed the hard plaquette support is itself non-RP (3D; odd Lx in 2D). With a hard weight, a negative eigenvalue would mix gauge-weight and fermion effects.
- **Change.**
  - UV-1 runs **two arms**:
    - **(primary)** the positive-type triangle (Fejér) profile with the same support, which isolates the overlap determinant;
    - **(secondary)** the hard support, as originally registered.
  - The readings UV-ONLY / PERSISTS / OPEN are unchanged and are applied to each arm separately. The primary arm decides the headline.
