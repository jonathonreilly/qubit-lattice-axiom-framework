I've run all three tests for R5. The answer is no: none of the codes the framework builds gives the three generations different code distances.

**Read before concluding:** `MINIMAL_AXIOMS_2026-06-29.md` in full, `PRIMITIVE_REGISTRY_CHECK.md`, `SCALE_REFERENCE_PRIMITIVE_NOTE.md`, and all of `derivation_obligations.json` (three AC/θ entries, none on the hierarchy). Then WALL.md, PR #9702 §§4–5, the corner-code note on main, HIER-2, GEN-1, GEN-2, and the hierwall reports R2, R3, R4, K, T and T2. All work is same-family (Opus 5.5) and unrefereed.

## Plain answer

- **One symmetry orbit everywhere.** Wherever the framework puts the three generations, a cube rotation maps each one onto the others: the hw1 corner triplet, the corner model's three uniaxial doubler pairs, GEN-2's orientations, and the corner code's three logical qubits. A symmetry gives images of each other the same distance, so they get the same mass at every order.
- **Unequal distances need supplied breaking.** The cube symmetry has to be broken down to three inequivalent axes, and that breaking (periods, or a strain direction) is put in by hand.
- **Loss does not make mass.** Random loss gives a protected mode a width only. Mass comes from the coherent part of the leakage, with the same exponent d as the unitary analysis.

## Prior art (git grep on origin/main)

- **Not on main:** code distance as a generation exponent; peripheral-spectrum, Petz-recovery or data-processing c-functions.
- **Already mapped, not mine:**
  - HIER-2 (PR #9783 branch): the momentum orders {1, 3}, and the control where 400/400 random spectra fit with free integers.
  - hierwall R2: Chamon d(4) = 4.
  - Main's no-go `REDUNDANCY_NOT_FORCED_BY_PND_LOCALITY_NO_GO_NOTE_2026-06-08.md`: records need not be stored redundantly.
  - Main's dynamics-clause notes: evolution between records is completely positive.

## Route 1: the distance ladder, m_i ∝ ε^{d_i}

**Object.** d_i is the fewest local perturbation terms whose product maps generation i's left component onto its right component inside a framework code.

**Lemma (proved).** If a symmetry of both the code and the perturbation class maps generation i to generation j, the whole perturbative series agrees, so d_i = d_j and m_i = m_j.
- All three d_i distinct needs a residual group that permutes no axes (D2h, orthorhombic).
- That is GEN-2's Eg vacuum in a generic direction, and it is supplied.

**What each framework code fixes:**
- **Corner code.** It fixes the qubit weight of each fermion bilinear, but the same weight for every generation.
  - Its three logical qubits are, I suggest, the Z₂ holonomies around the three torus cycles. That is the first Betti number of T³, so the "3" is topological.
  - They exist only on a torus. Z³ has none.
  - Their distance grows with L and is equal for all three by C3.
- **Chamon code (cited):** d(L) ≈ L with 4L logical qubits, so the integer is the region size.
- **Records (proved from the axioms):** one record per site makes a record a distance-1 code, and permanence is distance ∞ by axiom. Neither gives three finite integers.

**Number it would fix:** (d₁, d₂, d₃) per sector. It is not supplied, for the orbit reason above.

**Data test (checked, T2; masses are HIER-2's three recalled sets, CKM recalled).** Four code-natural shapes, fixed before the run:

| Shape | Exponents (light → heavy) | Origin |
|---|---|---|
| Linear | 3, 2, 1 | distance ∝ an integer size |
| Odd | 5, 3, 1 | consecutive odd orders; same shape as linear |
| Concatenated, d = 2 | 4, 2, 1 | 2^r |
| Concatenated, d = 3 | 9, 3, 1 | 3^r |

- **Model A** (one shape for all sectors, one ε, three scales; 4 continuous parameters plus the shape choice, 9 masses):
  - The best shape misses ×3 in every set: ×3.42 (M_Z), ×3.65 (GUT), ×3.08 (mixed). **Registered reading: R5-FAIL.**
  - Under the left–right symmetric split, the linear shape gets the CKM within ×2.5–2.95, but it predicts V_us = V_cb (observed ratio 5.5).
  - Concatenated shapes put V_cb above V_us, the wrong order, missing by ×5.5–8.8.
  - Observed CKM needs the left-handed distance gaps to shrink toward the light generation (ln V_us/ln V_cb ≈ 0.47). Linear and geometric ladders cannot do that.
- **Model B** (shape and ε per sector; 6 continuous parameters plus 3 shape choices):
  - Fits within ×1.2–1.4.
  - 38–41% of random six-decade spectra also fit within ×3.
  - The data beat random at p = 0.02–0.07. That p is not blind: I had worked out the observed shape ratios before fixing the shape list (disclosed in PREREG).
- **Free integers** (HIER-2): 2 continuous parameters plus 9 integers fit anything.

**Strongest objection.** Masses may be driven by interactions rather than leakage (campaign block B7), or an unbuilt code might carry generations as truly different sectors.

**Kill condition:** no framework code places the generations in three distinct orbits without supplied D2h breaking. It is met for every code built.

**Cheapest next test.** Build the corner code on an L_x×L_y×L_z torus and confirm d_i ∝ L_i, about 1–2 hours of GF(2) work. That would show the distances track supplied periods.

## Route 2: lossy leakage, read as mass versus width

**Object.** The per-rung logical eigenvalue λ = |λ|e^{iθ}. The phase θ plays the role of mass; 1−|λ| is a width.

**Checked (T1, exact; repetition codes with d = 3, 5, 7 and the [[5,1,3]] code).** Fitted slopes match prediction to within 0.02.

| Reading | Phase θ (mass) | Width 1−\|λ\| |
|---|---|---|
| Hamiltonian splitting | ε^d | — |
| Coherent rung + decoder | ε^d | ε^{d+1} |
| Pauli rung + decoder | exactly 0 | p^{⌈d/2⌉} |
| Passive (no decoder per rung) | — | logical failure per rung grows as N^{(d−1)/2}, so there is no constant rate |

- **Proved (standard):** Pauli noise with Pauli-frame decoding gives a logical Pauli channel, whose eigenvalues are real.
- **Suggested:** any detailed-balance dissipation has a real spectrum. Complex eigenvalues from dissipation alone need population cycles among three or more logical states, which are not a coherent left–right phase.

**Number it would fix:** the map from d to the order of the effect. It depends on the reading, and the loss strength p is a second supplied number.

**Strongest objection.** A rung is a change of description, not physical time. If so, the loss falls only on discarded data and the rung is an isometry on the kept sector, which leads to the same conclusion.

**Kill condition: met for masses.** A stable, coherent electron requires the rung to be exactly reversible on its sector (suggested).

## Q1: is data processing a c-function? Label: DPI-NO-C-FUNCTION (proved, standard; T3 checked)

- **What it gives.** D(ρ_n‖σ_n) to a fixed reference state cannot increase. That is a Lyapunov function for flows of states.
- **What it allows.** Damped spirals: a lossy qubit channel has a complex pair with |λ| = 0.975, winding 6.6 times while its relative entropy falls.
- **Cycles.** An exact cycle needs equality at every step, which means Petz-reversibility. So cycles live only on the protected (peripheral) sector, where the rung acts as a unitary.
  - Example: a period-5 cycle with D constant at 0.7136.
  - None of 200 random full-Kraus-rank channels has a non-unit peripheral eigenvalue; the largest is 0.744.
- **On coupling space.** Relative entropy per site may grow by up to b^d per rung. With finite Fisher information this bounds only y ≤ d/2, which is the condition α ≤ 0. It does not forbid spirals.
- **What actually forbids cycles** in the c-, a- and F-theorems is reflection positivity together with Euclidean (Lorentz) invariance. Unitarity alone does not: Efimov limit cycles occur in unitary non-relativistic systems (comparator).

## Q2: earlier no-gos that rest on unitarity or reflection positivity

- **Fails for lossy maps:** R3 Lemma C (Δ ≥ 1 unitarity bound). K already wounded it.
- **Premise to correct:** R4's and T-SPIRAL's statement that "unitary, reflection-positive theories forbid spirals". The theorems need Lorentz invariance; a unitary cubic-lattice theory is not protected either.
- **Reversible only, by construction:** block 93 and PR #8692 (detailed balance). The lossy class is covered instead by **T-SPIRAL Lemma C**, which uses no unitarity and survives.
- **Not covered:** T-LIGHTCONE. Its O(3) bilayer is reflection-positive and a comparator; a lossy level-time model that respects the Record axiom is untested.
- **Survives in coherent form only:** R2's tunnelling εⁿ (T1b). In a stochastic reading the relevant integer becomes the barrier height, not n (suggested).
- **Should survive (suggested):** HIER-2 R1, R4 and R5, and R1's Lemmas A and B. They need only the symmetry, which a covariant channel has; and T1 shows loss opens no route to mass.
- **Survive, no unitarity used:** R2 Lemma 2 and R4 Lemma B in 1D.

Peak memory was 158 MB, one process at a time, and nothing is left running. Nothing outside my folder was edited.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R5/`:
- `PREREG.md`, with the dated addendum
- `t1_leakage.py` / `.out`
- `t2_data.py` / `.out`
- `t2b_ckm_split.py` / `.out`
- `t3_dpi.py` / `.out`