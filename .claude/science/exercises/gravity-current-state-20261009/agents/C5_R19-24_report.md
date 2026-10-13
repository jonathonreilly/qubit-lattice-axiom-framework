# C5 R19-24 report: can the charge block be paid by a number-free dynamical clause, or must it stay counterterms?

**Author and provenance.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 06:30Z to about 07:05Z. I edited no repository file and downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `.../scratchpad/C5/R19-24/` (this folder).
- `vX` = the referee record of item X in `TESTS`, or `P/agents/C5_X_referee_verdict.md`. `rX` = `P/agents/C5_X_report.md`.
- `vR19-20` = `.../scratchpad/C5/ref_R19-20/REFEREE_VERDICT.md`. It finished at about 06:38Z, during this run, and is not yet recorded in `TESTS`.

**Labels.** Each claim carries one of these labels:
- **proved**: a complete argument under stated hypotheses (mine, so unrefereed);
- **checked**: numerics run here;
- **suggested**: argued, not proved;
- **reading**: an interpretation;
- **comparator**: an outside reference. **RECALLED** marks anything taken from memory.

I also mark each source: **[ref]** means a referee record, and **[worker]** means an unrefereed worker report.

---

## 0. Against the FIXED readings (`TESTS:8304-8307`)

**Worker reading: COUNTERTERMS-NEEDED, in the stated class 𝒦′ (§2). A referee is required (no-go type; same family). There is an OPEN remainder, and a registration collision to flag.**

**1. DYNAMIC-CLAUSE is not met by the registered clause.**
- D1 as written is "the law includes whatever local quadratic terms make each species' **one-loop** dispersion Lorentz-invariant to O(q²)" (`TESTS:8289`).
- It is self-consistent (proved, §4.3).
- It is number-free in the definitional sense the campaign accepted for (S), (S\*) and (Σ) (`vR17-3:17,19`; `vR19-15:14,18`; `vR19-20` "number-free renormalization rule").
- It is local and gauge-invariant (proved, §4.3).
- It zeroes the one-loop charge rows by construction. The counterterm values are checked (§4.1).
- **It does not stay zero at two loops.**
  - Checked in a toy: λφ⁴ on Z³ × ℝ has an exactly zero one-loop speed row for every law. So D1 asks for no counterterm at all, yet the two-loop sunset gives δc² = −0.38 (λ/16π²)² on the nearest-neighbour (NN) edge and −0.093 (λ/16π²)² on the gravity root's own scalar edge G(2.526) (§4.4).
  - In QED (proved by charge counting, §4.4) the two-loop rows carry new charge structures, q⁴ and q²Σ_j n_j q_j². They have no reason to vanish when the one-loop rows do. Their generic size, u² × O(0.1–30) ≈ 3e-8 to 1e-5, is suggested only; even the smallest value is about 1e11 times the comparator ε\* = 2.66e-19.

**2. The registration collision (flagged for the referee, as `vR19-20` item 5 did for R19-20).**
- The all-orders restatement **D1∞**: "every law-level field's dressed dispersion in the lowest state is Lorentz-invariant through O(p²), at every order".
- Under literal-first (`TESTS:7124`) this is a new completion, priced as P-R19-24a below.
- It stays zero at two loops by construction. It is number-free in the same definitional sense as (Σ).
- On that sense alone it would meet DYNAMIC-CLAUSE's letter.
- But under the campaign's registered counting convention it is exactly the R19-12 counterterms, re-set at every order. That convention is:
  - "a tuning counts as a nonzero κ, or as one equation imposed on the common edge parameters" (`rR16-2:231`);
  - "a tuning is any continuous parameter of the law or counterterms" (`TESTS:5470`);
  - the counterterm basis rule (`TESTS:5700`).
- D1∞ is the on-shell renormalization condition of Lorentz-violating QED, with nonzero κ at every order.
- I report COUNTERTERMS-NEEDED because:
  - literal-first tests D1 as written;
  - the item's own setting names the counterterm basis rule;
  - D1∞'s content is literally "counterterms re-set at each loop order".

**3. The stated class 𝒦′ (hypotheses before the title).**
- **Arena:** law-level clauses on lattice QED on Z³ × ℝ (the R19-12 setting), with:
  - the axioms' symmetry group G: Z³ translations, proper cubic rotations, time translations, plus P, T, C and gauge;
  - fixed field content;
  - weak coupling, i.e. a perturbative neighbourhood of κ = 0.
- **The demonstration has three branches:**
  - (A) **No symmetry clause exists in G** (proved, Lemma S, §4.2). This agrees with O1's refereed invariant count (`TESTS:2379`).
  - (B) **Every non-structural clause amounts to counterterms.** A clause that zeroes the rows without holding identically on an open set of laws is n_t equalities on law parameters at each order. That is codimension n_t by the implicit function theorem (IFT; proved, §4.3). Its solution moves from order to order (checked in the toy; proved structurally for QED, §4.4).
  - (C) **RG attraction is too slow.** It misses by 2.76e16 (`TESTS:1542` [ref], lane RE; counted once).
- **OPEN remainder:** non-symmetry structural identities. These are laws on which the rows vanish identically on an open set, at all orders, with no symmetry behind them.
  - None is known. Lemma F is OPEN on the subluminal class (`TESTS:5890-5893` [ref]).
  - The toy shows that an exact one-loop structural zero (λφ⁴, every law) does not survive to two loops (checked).
  - Closing this branch is suggested, not proved.

**4. Against the expectation (`TESTS:8308`).**
- **Borne out:** D1 is a renormalization condition, P73 restated.
- **Corrected in one respect:** the premise that "a source clause cannot touch [propagation speeds]" (`TESTS:8278`).
  - At linear order, (Σ) *is* a kinetic counterterm for the graviton (Lemma E, proved, §4.5). It zeroes graviton propagation rows.
  - So the asymmetry is not source against dynamics. It is **bridge against law**:
    - (Σ) defines a supplied sector: the graviton (P-N1) and the source map, which the axioms do not supply (`AX:140-146,187`). No law parameter changes.
    - The same sentence applied to the photon and charged matter fixes the law's own kinetic parameters.
  - A source-type clause for the photon, (Σ_γ), is available and is equivalent to κ_γ (§4.5).

**5. Where a number-free structural zero does exist (D2).** Hypercubic Z⁴, with time on the grid and a_t = a_s, zeroes every dimension-4 speed row at all orders by symmetry.
- **Refereed prior art:** `TESTS:60,82,85` (T1), `TESTS:1439` (F2), `TESTS:2379` (O1).
- **Two-loop toy control here:** the hypercubic version of the sunset is zero to 1.7e-21 λ² (checked).
- **But it lies outside the registered setting.** It costs set B's axiom-level price (Lattice: Z³ → Z⁴), and it leaves the R18-9/13 root, which is built on Z³ × ℝ.
- **Suggested follow-up, not checked here:** set B with (Σ). The charge rows would then be zero by symmetry and the gravity rows by stipulation. Set B's own walls would have to be re-read under (Σ): R2-4, R2-5, RK2 and R2-1 (`TESTS:2728-2760,1663`).

---

## 1. In plain words

- **The proposed rule is a counterterm prescription.** It says "the law contains whatever correction makes each particle's speed come out equal to light's". That is the standard way particle physicists fix a parameter by a measured condition (a renormalization condition). Written for one loop only, it fails at the next order:
  - in a toy model the one-loop correction is exactly zero, so the rule asks for nothing;
  - yet the two-loop correction is not zero.

  Written for all orders, it holds by definition. What it then does is restate the R19-12 bill: four tuned numbers per charge class (e, u, d and the photon), each re-set at every order, to about 1 part in 1e16.
- **Why the gravity rule looked free.** The source rule (Σ) for gravity looks number-free because it acts on the graviton, which the grid does not produce (it is supplied), and on "what gravitates", which the axioms leave open.
  - Moved to the other side of the equation, (Σ) is a counterterm on the graviton's own propagation. So "source clause against dynamics clause" is not the real difference.
  - The real difference: for gravity the numbers live in a part of the theory we supply anyway; for the photon and electrons they live in the grid's own law.
- **Only one thing pays the charge rows with no numbers:** a symmetry that mixes time and space. On a grid with continuous time there is none. On a 4D grid with time as a fourth lattice direction there is one, the 90° rotation of time into space. That is the known "set B" option, with its own costs.
- **Slow running does not help.** Letting the speed differences shrink as the energy falls (renormalization-group flow) is far too slow in QED; it misses by 16 orders of magnitude (refereed earlier).

---

## 2. Hypotheses, setting and conventions (stated before any title)

- **Setting (`TESTS:8285-8291`).**
  - One-loop QED on the SM root's edges (R19-12): Dirac D1(0.909104, 0.555604), scalar G(2.526104), photon γG_w(2.9435, 0.198093).
  - Continuous time, Peierls coupling, Feynman gauge, m → 0⁺ by Theorem L.
  - SM charged content: nine Dirac flavours; Σ_j n_j q_j² = 8.
  - Excluded, as in R19-12: W± and the non-Abelian sectors, mixed O(Ge²), and the matter graviton-loop rows.
- **Parties and observables.** δc_i = q_i²·u·F_s(m_i) and δc_γ = u·Σ (Lemma Q, `vR16-2:5`), with u = α/4π = 5.807e-4 (α RECALLED).
- **Counterterm basis (`TESTS:5700`).** Per (spin, |q|) class (C), per species (S), or q²-correlated (Q), as in R19-12 (`rR19-12:80-85`). Tuning convention: `rR16-2:231`; `TESTS:5470`.
- **Clause classes.**
  - **D1:** renormalization-condition clauses: an implicit definition of law parameters by the law's own dressed outputs.
  - **D2:** symmetry clauses.
  - **D3:** RG-flow mechanisms.
- **𝒦′** is as in §0 item 3.
- **Excluded alternatives (Forks rule, `TESTS:5704`):**
  - set A, a continuum base with Lorentz invariance in law;
  - set B, Z⁴ (§0 item 5);
  - supersymmetry outside the refereed lattice classes;
  - strong dynamics outside lane RE's class;
  - non-perturbative clauses with κ outside the IFT neighbourhood;
  - non-symmetry structural identities (the OPEN remainder).
- **Subtractions named before any run.**
  - The toy's speed row is c² − 1 = ∂_{p²}Π + ∂_{E²}Π on shell, or ∂_{p²}Π − ∂_{ω²}Π at Euclidean zero.
  - The one-loop tadpole and the two-loop double tadpole are momentum-independent, so they are not subtracted but drop out (proved).
- **Removed hypothesis (`TESTS:8298`):** counterterms as the only route.

## 3. Prior art (each counted once)

- **R16-2 + vR16-2:**
  - Lemma Q;
  - the counting convention (`rR16-2:231`);
  - "κ_γ is replaceable" (`TESTS:5422-5426`; `vR16-2:13`).
- **R16-10 + vR16-10:**
  - Theorem L: no IR log at one loop;
  - the Dirac zero only with a superluminal photon;
  - Lemma F OPEN on the subluminal class;
  - "a tuning is any continuous parameter" (`TESTS:5470,5890-5893`).
- **R16-1 + vR16-1:** the Wilson-edge interval no-go (`TESTS:5416-5421`).
- **R19-12 + vR19-12:**
  - the root-edge values F_½ = −5.2444 and Σ = 0.9187;
  - Lemma A: 4 per class, 10 per species, 2 q²-correlated;
  - route B, the Σ = 0 gravity-family root, which pays the photon row by an equality (`TESTS:8099-8110`).
- **R13-7 + vR13-7:** the interval no-go on the regulated literal edge; no interval zero is known (`TESTS:4844-4857`).
- **R10-1 + vR10-1:** Theorem P. Supersymmetric pairing cancels the photon coefficient, but the paired electron speed stays at −10.66 to −17.96 (`TESTS:4270-4279`).
- **R11-1 + vR11-1:** pairing (both statistics) is necessary for an untuned interval cancellation, at aggregate-measure level (`TESTS:4394-4405`).
- **R10-5:** a doubler-free box photon is excluded in the SUSY class 𝒮 (`TESTS:4303-4311`).
- **R19-15 + vR19-15:** (S\*) is a "stipulated renormalization/source definition" (`agents/C5_R19-15_referee_verdict.md:14,18`).
- **R19-19 [worker]** (`TESTS:8133-8143`).
- **R19-20 [worker] + vR19-20 [ref]:**
  - (Σ) is a "number-free renormalization rule" that "imposes—rather than derives";
  - 33 physical constraints plus one convention (`vR19-20` items 3, 6 and the strongest statement).
- **R17-3 + vR17-3:** (S) is number-free, not forced, and "radiatively tracking by definition" (`agents/C5_R17-3_referee_verdict.md:17,19`).
- **C4 V3 referee:** a renormalization condition that subtracts the tested quantity is "explicitly tautological" (`agents/C4_V3_referee.md:29`).
- **Set B / Z⁴:**
  - O1's invariant counts (`TESTS:2379`);
  - T1's Z⁴ control (`TESTS:60,82,85`);
  - F2's ξ = 1 (`TESTS:1439`);
  - RK2 K1: N_tune(Z⁴) = 11 (`TESTS:1663`);
  - R2-4, R2-5, R2-1 (`TESTS:2728-2760`).
- **Lane RE (D3):** FAIL (bounded). The SM one-loop flow takes the split from 8.55e-3 to 7.34e-3 at 1.4 PeV and misses by 2.76e16 (`TESTS:1523-1547`).
- **Literature (RECALLED):**
  - Collins–Perez–Sudarsky–Urrutia–Vucetich 2004 (Planck-scale LV regulators feed O(α/π) into dimension-4 speeds);
  - Chadha–Nielsen 1983 (Lorentz invariance as an IR fixed point, approached logarithmically);
  - Kostelecký–Lane–Pickering 2002 (one-loop running of the c and k_F coefficients);
  - Groot Nibbelink–Pospelov 2005 and Pospelov–Shang 2012 (SUSY as a custodian of dimension-4 Lorentz invariance);
  - the standard lattice-QCD fact that isotropic hypercubic lattices need no speed-of-light tuning, while anisotropic ones need the bare anisotropy tuned.
- **Grep.** I searched TESTS, `P/agents/*.md` and SUMMARY for "renormalization condition", "on-shell", "D1", "dynamical clause", "self-consistent" and "own loop". The hits are the C4 V3 R₀ and the (S\*)/(Σ) records above. No prior item states Lemma E (a source clause equals a kinetic counterterm) or tests a law-level clause at two loops.

---

## 4. Results

### 4.1 Recheck of the archived runners (checked; `S/scripts/r1924_recheck.out`)

- **Setup.** R16-10, R16-2 and R18-5 were copied unmodified from `P/scripts/C5/` into `S/arch/`, in R19-12's layout. R19-12's `r1912_lib.py` was used unmodified.
- **Reproduced to every printed digit:**
  - F_½(0⁺) = −5.24436 (N = 64) and −5.24444 (N = 128);
  - F_0(0⁺) = −1.16743;
  - G_½(m = 0.0025) = +0.114293 and G_0 = −0.059166.

  These match `P/scripts/C5/R19-12/r1912_a.out` lines 4–8 and 21, and vR19-12 item 1.
- **The one-loop D1 counterterms on the root edges** (checked, basis C):
  - κ_e = +3.0455e-3;
  - κ_u = +1.3535e-3;
  - κ_d = +3.384e-4;
  - κ_γ = −5.335e-4.
- **Bare v_max.** Put on the spatial symbol (or equivalently on the time-derivative term), κ_e makes the bare e-class law's in-box group velocity 1 + κ_e = **1.00305**. So the bare law's whole-zone v_max is at least 1.003: superluminal, as the head rule requires me to state (`TESTS:5039,5699`). The photon's bare speed is 1 − 5.3e-4.

### 4.2 (a) Classification of D1–D3

| clause | type | number-free? | zeroes the rows at 1 loop / 2 loops | where it lives | status |
|---|---|---|---|---|---|
| D1 as registered (one-loop) | renormalization condition | definitional sense only; n_t equalities on law parameters | yes / **no** | law | §4.3–4.4 (proved; checked toy) |
| D1∞ (restatement) | renormalization condition, all orders | definitional sense only; n_t equalities at every order | yes / yes, by construction | law | §4.4; P-R19-24a |
| D2 in G (Z³ × ℝ) | symmetry | — | **none exists** | — | Lemma S (proved) |
| D2 on Z⁴ (hypercubic) | symmetry | yes, structurally | yes / yes, all orders, dimension 4 | axiom (Lattice) | [ref] T1, F2, O1; toy control checked |
| D2 as SUSY pairing | symmetry relating species | yes | photon row only; electron row stays | content | [ref] R10-1, R10-5, R11-1, R13-7 |
| D3 RG flow | mechanism | yes | O(1) suppression only | — | [ref] lane RE: misses by 2.76e16 |

**Lemma S (no time–space symmetry in G). Proved.**
- **Hypotheses.** G is generated by:
  - Z³ translations and proper cubic rotations, which act on x only;
  - time translations, which act on t only;
  - P, T and C, which act diagonally on (t, x);
  - gauge and internal transformations that commute with these.
- **Claim.** The dimension-4 kinetic operators O_t = ψ̄γ⁰D₀ψ and O_s = Σ_i ψ̄γⁱD_iψ, and for the photon E² and B², are each separately G-invariant. So the speed, the ratio of their coefficients, is not fixed by G.
- **Proof.**
  - Every generator acts block-diagonally on (t, x): it maps D₀ to D₀ and the set {D_i} to itself.
  - The photon field strengths transform as E ∈ T1u and B ∈ T1g of O_h. Each of T1u⊗T1u and T1g⊗T1g contains exactly one A1g; E·B lies in A1u and is odd under P. So {E², B²} are the only invariant quadratic forms.
  - For Dirac fields, γ⁰D₀ and γⁱD_i are separately invariant for the same reason. This is O1's (V, S2) = (1, 2) count [ref] (`TESTS:2379`). ∎
- **Consequence (suggested exhaustiveness, with the excluded list).** A symmetry that fixes the speed must act off the block diagonal in (t, x). The candidates are:
  - a boost, excluded on the fixed grid by the refereed boost no-go cluster (C3/K2/RB/RFW, `TESTS:2324-2325`);
  - a 90° time–space rotation, which needs time on the grid (Z⁴: set B);
  - continuous Lorentz symmetry (set A).

  A species-relating graded symmetry (SUSY) is the remaining door. The refereed lattice classes leave the electron's own row unpaired (`TESTS:4276-4277`).

**D3 (counted once, [ref]).** Lane RE's E2 is the verified one-loop flow: 8.55e-3 → 7.34e-3 at 1.4 PeV, missing by 2.76e16 (`TESTS:1542`).
- This matches RECALLED Chadha–Nielsen: the approach to Lorentz invariance is logarithmic with O(α/π) anomalous dimensions, so ln(M_P/PeV) ≈ 30 e-folds give an O(1) factor.
- Strong-coupling power-law flows are FAIL (bounded) for the SM's weakly coupled content (`TESTS:1527-1539`).

### 4.3 (b) D1 at one loop: self-consistent, local, gauge-invariant (proved)

**Lemma IFT (self-consistency and codimension). Proved.**
- **Hypotheses.**
  - Write c_A(θ, κ) = 1 + κ_A + u·f_A(θ, κ) + O(u²) for the parties A ∈ {e, u, d, γ} in basis C, where θ are the non-counterterm law parameters.
  - f_A is C¹ in κ near 0 at fixed m, λ > 0. This follows because the propagator denominators stay bounded away from zero for small κ, as in R13-7's Lemma A (`vR13-7` item 4).
  - The tree velocities with κ stay below the Cherenkov threshold at p → 0 (true for |κ| ≪ 1).
- **Claim.** The map κ ↦ c − 1 has Jacobian I + O(u). So for small u the set {c_A = 1 for all A} is, near κ = 0, a graph κ = κ\*(θ) with a unique κ\* = −u·f(θ, 0) + O(u²).
- **Consequences.**
  - "A law that contains its own one-loop counterterm" is self-consistent and unique in that neighbourhood.
  - The solution set has codimension exactly n_t = 4 (basis C), 10 (S) or 2 (Q) in (θ, κ) space. These are R19-12's numbers (vR19-12 item 2).
- **A scheme ambiguity.** "The one-loop dispersion" can be computed with or without κ in the internal propagators. The two choices differ at O(u·κ) = O(u²), the same order at which §4.4 shows the clause fails.

**Gauge invariance and locality (proved; question (ii)).**
- **Matter counterterms.** κ_i multiplies either Z₀ψ†(i∂_t − q_iA₀)ψ or the Peierls-coupled spatial symbol. Both are gauge-covariant by construction, and the Peierls vertex is generated by the counterterm symbol, so the lattice Ward identity holds exactly.
- **Photon counterterm.** κ_γ multiplies one of the two invariants E² or B² (Lemma S). These are gauge-invariant, and the induced current stays conserved.
- **Locality.** The counterterms have the locality class of the edges they rescale: box-exact, Gevrey-quasi-local.
- **The Ward identity in the round-16 sense is standard,** not deformed (`TESTS:5039`).

**Number-free (question (i)).** The clause contains no free number. The target, "the neutral/graviton cone", is the unit convention. But its output is four numbers in the law, κ = (3.0455e-3, 1.3535e-3, 3.384e-4, −5.335e-4), needed to about 1e-16 relative (`rR19-12:152`).
- **Reading.** It is a law-level statement whose content is numbers in the law, specified implicitly by the law's own outputs.
- **Axiom lines touched.**
  - `AX:57` ("one fixed nearest-neighbor admissibility rule"): the rule's coefficients are fixed by a global, all-species, all-orders computation.
  - `AX:114-130`: no kinetic branch or values are supplied, and D1 supplies them by an output condition.

### 4.4 (b) Two loops: the registered (one-loop) D1 does not stay zero

**Toy (checked; `S/scripts/r1924_sunset.out`, `r1924_sunset_conv.out`).** The model is λφ⁴ on Z³ × ℝ with continuous Euclidean time.
- **Method.** Position-space sunset Π₂(x, τ) = −(λ²/6)G(x, τ)³, with G computed by FFT per τ node. τ uses Gauss–Legendre panels, with 20 and 32 nodes per panel agreeing to all 7 printed digits. Space uses minimal-image moments.
- **One loop (proved).** The tadpole (λ/2)G(0, 0) is momentum- and frequency-independent, so δc² = 0 exactly, for every edge and mass. D1 as registered therefore asks for **no counterterm**.
- **Two loops.** The double tadpole is also constant, so the sunset is the only O(λ²) source. Values of δc² in units of (λ/16π²)² (× λ²/24936):

| edge | m = 1.0 | m = 0.5 | m = 0.3 | m = 0.2 | m = 0.1 |
|---|---|---|---|---|---|
| NN | −0.167 | −0.287 | −0.339 | −0.362 | −0.380 |
| G(2.526) (the root's scalar edge) | −0.055 | −0.079 | −0.088 | −0.091 | −0.093 |
| G(1.4) | −0.087 | −0.134 | −0.152 | — | — |

- **Convergence.** L-converged to ≤ 1e-3 relative (L = 24 to 96). On-shell and Euclidean-zero definitions agree to < 1% at m ≤ 0.3. The m → 0 trend is roughly linear in m, which suggests a finite massless limit (about −0.40 for NN and −0.095 for G(2.526)) and no IR log (suggested).
- **Z⁴ hypercubic control** (the same sunset with time on the grid): the Euclidean-zero LV coefficient is +8.5e-22 and −1.7e-21 λ² (m = 0.5 and 0.3). That is zero by the 90° time–space rotation (checked; a symmetry identity).
- **Reading.**
  - The two-loop number is not fixed by the one-loop one. Here the one-loop row vanishes for every law, so no one-loop clause can know it.
  - An exact one-loop structural zero, which holds on all of law space, does not survive radiative corrections without a symmetry. This is question (iii) for D1.
  - The box-exact root edge, which is exactly Lorentz-invariant inside its box, still has a nonzero two-loop row. It comes from the box edge (UV-localized), as at one loop.

**QED charge structure at two loops (proved by Feynman-rule counting).** Peierls vertices carry q (one photon) and q² (seagull). So at O(e⁴):
- the species-i self-energy has two-photon graphs (rainbow, crossed, vertex, seagull) ∝ q_i⁴, and vacuum-polarization insertions ∝ q_i²·Σ_j n_j q_j²;
- the photon has the two-loop vacuum polarization ∝ Σ_j n_j q_j⁴;
- the one-loop counterterm insertions carry the same structures, since κ_i ∝ q_i² and κ_γ ∝ Σ_j n_j q_j².

So δc_i^(2) = u²[q_i⁴A_s + q_i²Σ_j n_j q_j²B_s] and δc_γ^(2) = u²Σ_j n_j q_j⁴C_{s_j}. Consequences:
- **Basis C (4) and basis S (10)** keep their counts at every order. The same operators absorb the shifts, so only the values are re-set (proved, given Lemma S).
- **Basis Q is not stable across loop orders** (suggested; it needs A_s ≠ 0, which is generic and not computed). One q²-correlated κ cannot absorb q⁴A_s. With three distinct q² values, the count rises from 2 at one loop to 3 at two loops, and saturates at the per-class 4 from three loops on.
- **Size and orders.** The residual left by the one-loop D1 at two loops is u²·c₂. With c₂ = O(0.1–30) (generic, not computed; the toy gives 0.09–0.4), that is 3e-8 to 1e-5, i.e. ≥ 1e11 × ε\*. A clause truncated at L loops needs u^L·c_L ≲ 2.66e-19, i.e. **L ≥ 6** for c_L = O(1) (u⁵ = 6.6e-17, u⁶ = 3.8e-20; suggested). Only the all-orders D1∞ is loop-stable.
- **IR logs (suggested, EFT argument).** Counterterm-induced tree mismatches produce u·κ·ln(1/ma) terms. These cancel at O(u²) against the IR running of the one-loop LV subgraph, because the running is driven by the effective coefficient δ(μ₀) = κ + u·f ≈ 0. So within a class, the residuals stay O(u·F′·ma), as in R19-12 (≤ 3.8e-21). Not computed.

**D1∞, the all-orders restatement.**
- **Self-consistent order by order:** apply the IFT at each order (proved, given smoothness at every order).
- **Stays zero at two loops:** by construction. In the toy the needed O(λ²) counterterm is finite, converged and nonzero (checked).
- **What it is:** the on-shell renormalization condition. Counted in the registered basis, it is P73 = 4 per class (10 per species), re-set at every order.
- **Precision:** about 1e-16 relative for the κ_c, and about 5e-16 relative for κ_γ against the e class.

### 4.5 (c) Source against dynamics: Lemma E and where the numbers live

**Lemma E (a source clause is a kinetic counterterm at linear order). Proved.**
- **Setting.** Let a field φ obey K·φ = J_src[φ], with J_src = ⟨J⟩_{state,φ} − (L·φ + c).
- **Hypothesis.** L·φ + c is a state-independent subtraction, linear in φ.
- **Claim.** The equation is identical to (K + L)·φ = ⟨J⟩_{state,φ} − c. So the subtraction changes φ's propagation exactly as a kinetic counterterm L would. ∎
- **Applied to (Σ).** (Σ) subtracts (T₂[Π_vac] − Z·E_EH)·h (`rR19-20:103`). So at linear order (Σ) is the graviton counterterm that sets the graviton's dressed quadratic action to (1/16πG + Z)E_EH through O(p²).
  - This is why R19-19's (S\*\*) zeroes the six graviton-cone rows, which are graviton speeds and masses.
  - (Σ) is D1∞ for the graviton.

**Corollary for the photon row. Proved, with the photon's analogue of (Σ).**
- **The clause (Σ_γ):** "the electromagnetic source is j minus the lowest state's linear current response through O(q²), replaced by its Lorentz-invariant (Ward-exact) form".
- **Properties.**
  - Local: a Taylor polynomial.
  - Gauge-invariant. The lattice vacuum polarization is transverse (exact Ward identity with Peierls coupling). The transverse O(q²) kernels under O_h × T are spanned by E² and B² (Lemma S). So the subtracted LV part is transverse.
  - Number-free in (Σ)'s sense, and radiatively tracking by definition.
  - By Lemma E it **is** κ_γ.
- **Consequence.** It pays R19-12's photon-to-neutral row (P-R19-12a) in exactly the way (Σ) pays the graviton rows. Route B's Σ = 0 gravity-family equality (`TESTS:8104`) remains the alternative payer.
- **Charged matter.** The matter rows have no source form; matter is not sourced by a bridge. Their (Σ)-type sentence, "the lowest state's self-energy contributes only its Lorentz-invariant form", is D1∞ itself.

**The real asymmetry (reading, from Lemma E and the bookkeeping records).**
- **(Σ) and D1∞ are the same logical move:** stipulate the Lorentz-invariant answer for a vacuum dressing. vR19-20 calls (Σ) "a number-free renormalization rule" that "imposes—rather than derives".
- **They differ in where the outputs live.**
  - (Σ)'s 33 constraints (vR19-20 item 3) fix a sector the grid does not supply: the graviton (P-N1) and the source map, which the axioms leave open (`AX:140-146,187`). No law parameter changes. The campaign has counted such definitions as 0 numbers (vR17-3, vR19-15, vR19-20).
  - D1∞ and (Σ_γ) fix the law's own kinetic parameters. The registered tuning convention counts those as tunings (`rR16-2:231`; `TESTS:5470`).
- **So: a source clause is "number-free" only because the sector it defines is not part of the law.** Once the field is law-level, the same sentence is a renormalization condition on law parameters.
- **Consistency demand (reading, for the referee and owner).** Either:
  - the definitional exemption extends to law-level clauses: the charge block becomes 0 numbers + 1 clause, and the whole cone bill reads "Lorentz invariance of every vacuum dressing, imposed"; or
  - it does not: then (Σ)'s graviton content is equally "33 conditions" (vR19-20 item 3), and the gravity block's "0 numbers" is a bookkeeping choice, not a physical difference.
- **One physical asymmetry survives, and it favours the law-level version** (suggested).
  - D1∞'s counterterms are state-independent constants in the law. The charge rows' mass dependence is O(u·F′·ma) ≲ 1e-20. So the pre-crossover mismatch that threatens the state-tied (Σ) (R19-19/R19-21, `TESTS:8148-8150`) has no charge-row analogue of comparable size.
  - The reason is that the speed rows are dimensionless and depend weakly on mass, while the shear rows are mass-type.

### 4.6 (d) Prices (named, none adopted; counted once)

- **P-R19-24a (new completion): D1∞ / (Σ_ψ,γ).**
  - The clause: "every law-level field's lowest-state dressing contributes only its Lorentz-invariant form through O(p²), at all orders."
  - **Cost:** P73 restated. That is 4 per class (10 per species) equalities on law parameters, re-set at every loop order. The q²-correlated basis is not loop-stable (2 → 3 → 4).
  - **Precision:** about 1e-16. The bare e-class law is superluminal (v_max ≥ 1.003).
  - **Axiom lines:** `AX:57`, `AX:114-130`, and `AX:94` through "the lowest state" (count once with (Σ) and S26 Q1(ii)).
- **P-R19-24b (variant): (Σ_γ) alone.** It pays only the photon row. It is equivalent to κ_γ, or to R19-12's route-B equality.
- **D2 on Z⁴:** no new price. This is set B's Lattice change (O5 set B; `TESTS:2426,2444`) with its refereed walls: R2-4, R2-5, R2-1 and RK2 K1, which 11 graviton conditions would turn into (Σ) stipulations.
- **P73:** unchanged in count (4 / 10). Its stability across loop orders is now explicit: the values must be re-set at each order through about 6 loops, or the clause stated to all orders.
- **Bill (reading, per class, on one law; count once with vR19-12 and R19-20):**
  - **Gravity block:** 0 numbers + (Σ), (W1-weight + N), carrier [ref vR19-20: a "proposed package"].
  - **Charge block:** 4 per class, or 0 numbers + P-R19-24a if the definitional exemption is extended.
  - **CC:** 0 by (S).

---

## 5. Strong-word check

- **"Proved":**
  - Lemma S (block-diagonal action; representation counting);
  - Lemma IFT (under the stated smoothness);
  - gauge invariance of the counterterms;
  - Lemma E (one line of algebra);
  - the zero one-loop row in λφ⁴;
  - the QED two-loop charge structures.

  All are unrefereed.
- **"Checked":**
  - the runner recheck;
  - the κ values;
  - the toy's two-loop rows (convergence in L, τ quadrature and m);
  - the Z⁴ control.
- **"Does not stay zero at two loops":** checked in the λφ⁴ toy on Z³ × ℝ, including the root's scalar edge. For QED it is suggested (generic): the coefficients A_s, B_s and C_s are not computed.
- **"No symmetry exists":** proved within G. Exhaustiveness beyond G is suggested, with the excluded list in §2.
- **"Number-free":** used only in the campaign's definitional sense, and always paired with the counting-convention statement.
- **"COUNTERTERMS-NEEDED":** a worker reading, in 𝒦′, needing a referee. The structural-identity remainder is OPEN.
- **Not claimed:**
  - any QED two-loop value;
  - minimality in a convention-independent sense beyond the IFT codimension;
  - set B + (Σ) viability;
  - W±, QCD, or the matter graviton-loop rows;
  - the IR-log cancellation (EFT argument only).

## 6. For the referee

1. **The registration collision.** Is D1∞ "number-free" under DYNAMIC-CLAUSE, given vR17-3, vR19-15 and vR19-20's treatment of (S), (S\*) and (Σ)? Or is it "counterterms re-set at each order" under `rR16-2:231`, `TESTS:5470` and `TESTS:5700`? Lemma E says the same answer must apply to (Σ)'s graviton content.
2. **Lemma E** and its application to (Σ) at linear order: is (Σ) exactly a graviton kinetic counterterm?
3. **The toy.** Reproduce the sunset speed row:
   - NN at m = 0.2: −1.4505e-5 λ²;
   - G(2.526) at m = 0.2: −3.6406e-6 λ²;

   and the zero one-loop row. Is the toy an adequate witness for "a one-loop clause does not stay zero at two loops"?
4. **Lemma S.** Is the exhaustiveness list complete enough for COUNTERTERMS-NEEDED in 𝒦′? Should the OPEN remainder downgrade the reading to OPEN?
5. **Basis Q's instability** across loop orders (2 → 3 → 4): does the generic A_s ≠ 0 need a computation?

## 7. Files (`S/`)

- `arch/`: unmodified copies of `P/scripts/C5/{R16-10, R16-2 (under R16-10/arch/), R18-5}`.
- `scripts/r1912_lib.py`, `r1912_a.py`, `r1912_recheck.py`: unmodified copies from `P/scripts/C5/R19-12/`.
- `scripts/r1924_recheck.{py,out}`: the runner recheck and the D1 κ values (4 s).
- `scripts/r1924_sunset.{py,out}`: the λφ⁴ two-loop speed row on NN, G(2.526) and G(1.4), plus the Z⁴ control (4 s).
- `scripts/r1924_sunset_conv.{py,out}`: τ-quadrature and m → 0 checks (22 s). It imports `r1924_sunset.py`, so its first block repeats that table.
- Every run used `OMP_NUM_THREADS=2` and took under 30 s.
