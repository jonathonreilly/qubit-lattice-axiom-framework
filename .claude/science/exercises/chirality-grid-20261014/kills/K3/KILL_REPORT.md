# K3 kill report: price theorems and reframings (chirality-grid exercise, step 6 with a step-8 test)

- **Agent:** K3, Claude Opus 5.5. Same family as the supervisor and every route/combo agent, so not independent. Unrefereed.
- **Window:** 2026-10-14, 14:58Z to about 15:25Z (machine clock).
- **Repos:** nothing edited. Everything is in this folder.
- **Read:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (cited as AX);
  - packet WALL, ASSUMPTIONS, ROUTES (both rounds) and step0/PRIOR_ART;
  - the target reports in full: F3, F6, F4, X1 and F5; F1 §R3;
  - origin/main `docs/repo/DEFERRED_DECISIONS.md` (#2, #4), `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` and the SPIN10 note §2/§9;
  - the walls commit `4bd42747e5`: WALLS.md T22–T25, kills/T22.md and attacks/T25.md.
- **Paths:** P = `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/chirality-grid-20261014/.claude/science/exercises/chirality-grid-20261014`.
- **Labels:** proved / checked / suggested / reading / comparator.

## Plain words first

**1. F3-A (one-handed tick).** The main conclusion survives: a one-handed tick still fails. But its two-branch story is wrong in one branch.
- The copy hidden at half a tick (the "π copy") is not a light mirror that would add to the Z width.
- Driven by a slow field, it only emits; it never absorbs.
- For the repo's own tick, its emission cancels the light particles' absorption exactly, at every frequency. For the literal single-light-Weyl tick, it emits 17 times more than the light particle absorbs. That vacuum is a true amplifier.
- Branch (b) of the dichotomy assumes an extra conserved energy. That energy cannot exist once the copy feels any massive gauge boson, as it must, since it carries the same charges.
- So the "dichotomy" has one live branch: the vacuum is unstable.
- I found no counterexample. Neither prethermal ticks, Floquet many-body localization, nor energy-selective structures give a stable, non-lasing one-handed tick.

**2. F6 (misframing).**
- The index lemma and the data exclusion of electroweak-mass mirrors stand.
- "T_d is an exact handedness operator" is true only as a symmetry. T_d is a lattice translation, not a ±1 grading, so it gives no chirality projectors.
- "#4 is not a price" is too strong. Every surviving route needs many fermion modes per site. That is the kind of site-algebra extension #4's own wake condition names, and that condition's literal text ("the chirality/generation program resumes") fires on this exercise. This is the owner's call, not a "checked" fact.
- "The 11-item failure list was guaranteed" and "free ticks fail by the lemma" are overreach. F3's own single-Weyl tick is a counterexample to the second.
- "8 vs 48 is a category error" overstates. T25 had already priced the matter count; F6 lowers that price, conditionally.

**3. F4-L2 (forced zero).** The lemma is the standard Green's-function-zero topology applied to the slab. It survives. The "iff" does not: only "slab works ⇒ Golterman–Shamir's (GS's) condition fails" is shown.

**4. X1.** E1, E2 and Lemma Z survive; E3 is open, as X1 says. E4 (T ⇒ gapped symmetric far wall) silently assumes that the target is realized with an exact on-site symmetry. The target contract also admits emergent, non-on-site and Euclidean realizations. So the regrading of F1-R3 to "target-equivalent, not stronger" is wounded, and F1's original grading stands for the full contract. The status (blocked-equivalent) does not change.

**5. F5.** Lemma B is correct and standard. Lemma D is correct under its declared reading, and F5-A's death does not depend on it.

## Verdict table

| # | Item | Verdict | One-line reason |
|---|---|---|---|
| 1a | F3-A A1 (identities, rep content) | **survives** | Re-derived. T1 also reproduces \|M\|² = 2 at both node types. |
| 1b | F3-A A2 (stabilizer, inversion) | **survives** | Two-band proof is correct. The multiband arc-boundary statement is the standard Floquet node-balance (comparator: Bessho–Sato). |
| 1c | F3-A A3 dichotomy (a) lasing / (b) light mirror | **wounded** | Branch (b) is empty for any gauge-coupled tick (proved below). Its observable has the wrong sign (checked, K3-T1). For U_g the linear-response gain exactly equals the loss, so "lasing" there means spontaneous-emission heating, not amplification (checked). The one-photon zero-threshold rate is unestablished (kinematics). |
| 1d | F3-A "price conclusion": tails-tick exit closed without deciding range | **survives (strengthened)** | Gauge coupling plus identical charges leaves no exactly conserved A2-class E′, so the vacuum is not stationary. No counterexample found. |
| 1e | F3-A's correction of T22 kill :19 | **survives, with a sign refinement** | The π nodes are soft, not "at cutoff", but they are inverted. T22's "2.0 copies" (counting them as ordinary species) was also wrong. |
| 2i | F6 T_d "exact handedness operator"; #2 not a price | **wounded / survives** | T_d is exact as a symmetry but is not an involution and not on-site. The #2 reading is fine (net handedness is flip-invariant). |
| 2i′ | F6 "#4 not a price", "does not fire #4 (checked)" | **wounded (contested governance)** | True for the γ5 motivation. False for site-algebra size: the C222-class clause is in #4's wake condition 1, and the condition's literal "chirality/generation program resumes" fires. |
| 2ii | F6 index lemma | **lemma survives; application wounded** | Lemma correct (standard). "Free ticks" and "11-item list guaranteed" are false or overreach. |
| 2iii | F6 EW-mass mirror exclusion (S, gg→h) | **survives** | Numbers re-read. gg→h is robust because h carries the EW VEV (κ_V ≈ 1). The S scan is model-scoped. |
| 2iv | F6 "8 vs 48 is a category error" | **wounded** | T25 already priced the matter count. F6's 3×16 is a conditional refinement. |
| 3 | F4-L2 forced zero; "slab works iff GS conjecture fails" | **lemma survives; "iff" wounded** | Only ⇒ is shown. The converse needs the far-wall dynamics (no SSB or relocation). |
| 4 | X1 E1–E6, Lemma Z, F1-R3 regrade | **E1, E2, Z survive; E3 open (as stated); E4 wounded; E5 skeleton; E6 conditional on suggested L3 parts; regrade wounded** | E4 needs T restricted to an exact on-site G. |
| 5 | F5 Lemma B / Lemma D | **survive** | B is standard Stokes. D holds under its reading and is not load-bearing. |

None of the five quietly assumes the target. No direct contradiction with a landed main note was found (details per item).

---

## 1. F3-A: the one-handed tick price theorem

Sources: P/routes/F3/ROUTE_REPORT.md (F3); routes/F3 scripts in the scratch folder.

**What was claimed.**
- A1: E = (i/2)(U−U†) = b·σ is local and conserved. Σχ(0) = Σχ(π) = W3. The π sector has the same representation content (F3:52-68).
- A2: the arc vacuum is population-inverted at the π nodes. Any conserved quadratic E′ with that vacuum as its Fermi sea puts every node at E_F (F3:83-89).
- A3 [suggested]: (a) with no local conserved E′, the vacuum lases at first order with zero threshold, rate ~αΛ⁴; (b) if E′ exists, the π copy "is a light mirror for every slow observable (Z width, soft gauge couplings)" (F3:91-97).
- The price conclusion: "the range question does not need to be decided for this exit" (F3:137). ROUTES:14 carries the dichotomy as "proved (2-band)".

**Does it assume the target?** No. **Contradict a landed main note?** None on main touches ticks; LATTICE_HANDEDNESS is branch-only.

### K3 finding 1: branch (b) is empty once the copy is gauge-coupled [proved, first order, two-band free fermions]

- Suppose E′_tot = E′_f + E′_b + O(e) commutes exactly with U_tot = U₀ + eU₁ + O(e²).
  - E′_f is any A2-class one-body E′ = a′ + c b̂·σ with c > 0 off nodes (F3:87).
  - E′_b is any one-body conserved quantity of a boson mode.
- At first order in e, [E′₀, U₁] + [E′₁, U₀] = 0. Between joint eigenstates with equal U₀ quasi-energy (on-shell mod 2π), this gives (E′_f − E′_i)·⟨f|U₁|i⟩ = 0. So every nonzero on-shell first-order amplitude conserves E′₀.
- Take a massive gauge boson at rest, frequency M (a Z). It couples to both sectors with identical charges (A1(iv), gauge invariance).
  - Z → light pair: on-shell, and ΔE′_f = 2c₀ > 0, so E′_b(Z) = +2c₀.
  - vacuum → Z + π-pair: the π-pair U-quasi-energy is −M mod 2π, so this is on-shell, and ΔE′_f = 2c_π > 0, so E′_b(Z) = −2c_π.
- These contradict each other unless the π-pair vertex vanishes. It does not:
  - |M|² = 2 at both node types (F3 R1-F2, F3:115);
  - the emission weight is nonzero in K3-T1.
- So no exactly conserved A2-class E′ exists for a gauge-coupled one-handed tick. Branch (b) cannot be realized. An only approximately conserved E′ is branch (a) with an O(1) vertex.

### K3 finding 2: branch (b)'s observable has the wrong sign [checked: K3-T1, pre-registered]

Test K3-T1 (`PREREG.md`, `k3_t1_signed_response.py`, output `k3_t1_output.txt`):
- **Setup:** the golden-rule weight of a uniform Peierls field at frequency ω on U_g's arc vacuum, using F3's own U_g and vertex.
- **Light sector:** absorbs at 2ε₊ = ω.
- **π sector:** has quasi-energy change 2ε₊ = 2π − ω ≡ −ω, so it can only emit.

| ω | A_abs (light) | A_em (π) | ratio | net/A_abs | π absorption at +ω |
|---|---|---|---|---|---|
| 0.2 | 2.0217e-3 | 2.0217e-3 | 1.000000 | 1e-12 | 0 |
| 0.01 | 5.0660e-6 | 5.0660e-6 | 1.000000 | 5e-12 | 0 |

- The pre-registered reading is met: **KILL-(b)-READING**. The full-BZ cross-check is clean (no weight outside the corner shells).
- **Observed after the run** (not part of the reading): the equality is exact at all ω because U_g(k+(π,π,π)) = −U_g(k).
- **Meaning:** for U_g the π copy cancels the light sector's linear absorption identically.
  - A Z-type width into these fermions nets to zero, instead of adding a mirror's share.
  - The vacuum is not a net amplifier at linear order. Its instability is spontaneous emission (vacuum → boson + π pair).

**Dated follow-up K3-T1F** (pre-registered before running; `k3_t1f_wilson.py`, output `k3_t1f_output.txt`):
- **Object:** F3's "literal single light Weyl" tick (Wilson-normalized M = −2; one node at ε=0 and seven at ε=π, F3:114).
- **Result:** A_em/A_abs = 17.0008 at ω = 0.01, against a desk prediction of 17 (Σ 1/v over the π nodes).
- **Reading:** NET-GAIN. That vacuum genuinely lases in linear response.
- **Instrument note:** a fixed-radius cross-check flagged a slow node; it is clean at radius 0.6 (`k3_t1f_crosscheck.txt`). This is an instrument issue, not a reading.

### What this does to F3-A

- **The price conclusion survives, and is sharper** [proved for gauge-coupled two-band free ticks, plus checked]. A one-handed tick coupled to the gauge bosons its charges require has no exactly conserved local E′ of A2 class, so its arc vacuum is not stationary.
  - For U_g the instability shows up as spontaneous emission with gain equal to loss.
  - For generic ticks it shows up as net gain.
  - The "light mirror" branch never occurs.
- **"Lasing … at first order with zero threshold, ~αΛ⁴"** (F3:94) is unestablished.
  - U_g has velocity 1 at every node (T1: A_abs/ref = 0.99999).
  - With a massless photon of speed c = 1, the one-photon process is collinear-marginal. If c < v_π, it is kinematically closed at first order, and the instability starts at second order.
  - A massive Z at rest is always on-shell. F3 had labelled the rate an estimate.
- **The A1(iv) wording** "exactly the same gauge representation content" holds for the chirality-weighted content only. Node counts differ (1 against 7 for M = −2), and non-chiral observables such as widths count nodes weighted by 1/v (T1F: 17×) [checked].
- **Counterexample search** for "a stable vacuum with no conserved E′ and no lasing":
  - **Prethermal ticks:** excluded at the one-body level [proved]. If ‖U(k) − e^{−iH(k)}‖ < 2 for all k with H local, then U is homotopic to e^{−iH}, which is homotopic to 1, so W3 = 0. W3 ≠ 0 also forces bands to reach both 0 and π, so there is no high-frequency window.
  - **Floquet MBL:** needs disorder and localizes the propagating Weyl. W3 ≠ 0 gives chiral lowest-Landau-level transport in a field (F3 R2: GNVW index 4N_φ), which cannot be localized [suggested].
  - **Energy-selective structures:** non-unitary, which is F5's domain (T3′ Planck conductivity).
  - None survives.
- **The T22 correction** (F3:117-120) stands: the π nodes are soft, not "at cutoff". Refinement: they are soft and *inverted*, so T22 Test B's count of them as ordinary low-energy species (kills/T22.md:19) was wrong as well.

---

## 2. F6: misframing (P/routes/F6/ROUTE_REPORT.md)

### (i) T_d, #4 and #2

**T_d: survives as a symmetry; the γ5 label is wounded.**
- [H, T_d] = 0 and T_d ε T_d⁻¹ = −ε are correct (checked by F6; F6:70-81).
- It is the walker form of K2a's selector (PRIOR_ART:84), which F6 itself states at :81.
- But T_d = T_xT_yT_z is a lattice translation with spectrum e^{i(kx+ky+kz)}. T_d² ≠ 1, so (1 ± T_d)/2 are not projectors.
  - The landed main note defines the missing object by γ5² = I (`docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md:60`, N3).
  - So "these are exactly the Hamiltonian-form properties of γ5" (F6:79) omits the involution and on-site properties.
  - Any chiral projector built from T_d is a momentum filter (exact only at the corners), so it inherits Eichten–Preskill leakage.
- **No contradiction with the landed note** [reading]: T_d is not in one site's M₂(C).

**#2 (orientation bit) not a price: survives** [reading].
- Flipping a Cl(3,0) axis flips every node's chirality at once.
- The net one-handedness is flip-invariant; the bit only fixes which hand is called "left".
- Wake condition 2 of #2 ("a weak-sector or handedness result needs the bit's status to state itself", origin/main DEFERRED_DECISIONS.md:73) does not fire.

**#4 not a price: wounded, contested governance.**
- #4's wake condition 1 reads: "A live lane hits the M₂(ℂ) wall the proposal addresses — the chirality/generation program resumes, or a C222-class site-algebra extension becomes load-bearing for a landing" (origin/main DEFERRED_DECISIONS.md:139-142).
- "C222-class" means a register enlarging the one-site algebra (C222's 24-dim register coin; origin/main `archive/chains/july-mass-era.md:83-93`).
- Every surviving route needs such an enlargement:
  - F6's own "matter count: 16 modes per site for KS, 32 for the walker" (F6:147);
  - F4-A's ~10³ qubits per site (F4:153-156);
  - X1's 64L modes per site (X1 §7).
- So the site-algebra question #4 belongs to is a price of this wall. Only its specific M₄(ℂ)-for-γ5 motivation is not.
- F6's "this exercise does **not** fire #4 … *(checked)*" (F6:92-95) labels a governance reading as checked, and it contradicts the literal clause. That clause is also what PRIOR_ART:230 flagged.
- Per the registry rule (DEFERRED_DECISIONS.md:13-15), the observer should report the possible firing to the owner rather than resolve it.
- ROUTES:31 inherits the overreach.

### (ii) Index lemma

**The lemma survives** [proved; standard].
- V/K ≅ (V/K)* for a G-invariant nondegenerate symmetric form, and characters are additive. Re-derived.

**The application is wounded.**
- F6:106-112 says that, together with NN, the lemma makes "every route in the free/bilinear class fail by theorem", including "free ticks". That is false for tails-ticks.
  - F3's checked M = −2 free tick has exactly one light Weyl at ε≈0 (F3:114). Its ε≈0 infrared is not vector-like.
  - It fails only through F3-A's π copy (§1), not through NN plus the lemma.
- "Their recorded failures … carried no information beyond this lemma" (F6:112, items 1–5 and 8–9) overreaches:
  - items 1, 8 and 9 are operator-existence no-gos (no γ5 in M₂(ℂ); no Z⁴ selector; no ultralocal GW), which a mass-form lemma does not imply;
  - item 4 (ticks) is not covered.
- ROUTES:20's "so the 11-item failure list was guaranteed" goes further still: it would include item 7 (interacting Spin(10) atom) and item 10 (record side), which are not bilinear.

### (iii) Electroweak-mass mirrors

**Survives** [checked by F6; numbers re-read in P/scripts/F6/tB_output.txt].
- S per mirror family is (3+1)/(6π) = 0.212, giving 0.637 for three families. Pull 6.5σ at U = 0, conservative compared with a T-conditioned fit.
- Robustness: gg→h ≥ 9.3. Any EW-chiral mirror gets its mass from EW breaking. The observed h has κ_V ≈ 1, so it carries the VEV and couples ∝ m/v even in a two-doublet alignment limit [suggested].
- **Scope:** the S/T scan assumes no compensating new physics (e.g. Majorana neutral leptons with negative S) and Dirac mirror masses ≥ 0.4 TeV. gg→h covers what S leaves.

### (iv) "8 vs 48 is a category error"

**Wounded.**
- T25's outcome was "PRICED: MATTER-COUNT, a per-cell space larger than one qubit, (gauge content) x (flavour 3)" (`4bd42747e5:.claude/science/walls/toe-walls-20260929/attacks/T25.md`, Outcome). "8 vs 48" was cited as evidence for that price, not as a species count.
- F6's 3×16 = 48 (F6:167) takes the flavour 3 from the hw1 corners. That lowers T25's per-cell factor from 48 to 16, which is a refinement, not a category error. It is conditional on:
  - the hw1-as-generations reading, an open bridge (PRIOR_ART T4; THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE:22-24);
  - symmetric gapping of hw0/2/3, which is the wall itself;
  - X2 having found F6's 3L+3R reduction tuned and covariance-breaking (P/combos/X2/COMBO_REPORT.md:116, :199).

---

## 3. F4-L2 forced-zero lemma (P/routes/F4/ROUTE_REPORT.md:65-90)

**The lemma survives as a proof skeleton** [proved skeleton].
- Its content is the standard momentum-space topology of Green's functions (comparator: Volovik; Gurarie PRB 83, 085426): the indices of poles and zeros of a Hermitian G(0,k) sum to zero by Stokes.
- Applied to the slab, a lone near-Weyl pole forces zeros of index −χ in every complete interpolator set.
- **Consistent with main.** The SPIN10 note on main shows an atomic zero removed by enlarging the interpolator set (SPIN10:136-157). That is exactly the "kinematical" case that L2 excludes for a successful slab, so there is no contradiction.
- **Novelty is the slab framing only**, which F4 itself half-says at F4:44.

**"The slab works ⇔ GS's 'zeros are kinematical' conjecture is false for that model" (F4:87): wounded.**
- Shown: works ⇒ GS condition D/4 fails (L2 step 4). Equivalently, by contraposition, GS's condition holds ⇒ the slab fails.
- Not shown: GS's conjecture fails for that model ⇒ the slab works. A non-removable zero only says the gapless poles of a complete set carry net index. Success further needs a far wall that gaps:
  - with a unique ground state;
  - without symmetry breaking;
  - without relocation;
  - with the near cones intact.
- Those are dynamical facts. F4's own test readings list FAIL-SSB and FAIL-RELOCATE as separate outcomes (F4:191-194).
- The "⇔" holds only if "GS false for that model" is defined to include a symmetric gapped far wall, which makes it a tautology.
- ROUTES:25's "a single observable" is right only as a discriminator between SMG-success and a GS composite *after* a gap without SSB is established.
- **Bookkeeping** [reading]: GS's no-zeros condition is numbered (3) in F1 and ROUTES, (4) in F4:86, and (D) in F6:53. One numbering should be fixed.

---

## 4. X1: E1–E6, Lemma Z, and the F1-R3 regrade (P/combos/X1/COMBO_REPORT.md)

- **E1** (S\* ⇒ H_DI; :78) **survives** [proved skeleton]. Truncating V's generator is fine by Lieb–Robinson, and the open steps (tails; near-wall stability) are named.
- **E2** is true by definition.
- **E3** (BBC-inv) is open, as stated.
- **E4: T ⇒ P_bdry** (:83, from F4:142) **is wounded.**
  - "Stack the T-model's 16_L on the far wall and pair it by a G-invariant bilinear" yields P_bdry, a G-symmetric gapped boundary with on-site G as S\* requires, only if the T-model has an exact, on-site G on a finite-dimensional tensor-product Hamiltonian lattice compatible with the slab.
  - The target contract also admits:
    - G "emergently with violations below observational bounds" (WALL.md:41);
    - transfer-matrix, QCA and Floquet dynamics (WALL.md:43);
    - Euclidean constructions with reflection-positive reconstruction (WALL.md:44);
    - GW/overlap and non-on-site G (F2-H, X3; Gioia–Thorngren).
  - None of these is covered. Converting a non-on-site anomaly-free G to on-site needs a TPF-type lemma, which X1 §6 notes uses infinite-dimensional rotors. Emergent G gives no exact P_bdry at all.
  - So **S\* is target-equivalent only to T_on** (T with exact on-site G), modulo BBC-inv.
  - X1's correction "this corrects F1's grading 'T ⇏ P, P stronger than T'" (:87; ROUTES:42) is therefore wounded. F1's grading (F1:136) stands for the full contract.
  - The status (blocked-equivalent) is the same either way.
- **E5** (S\* ⇒ T gauge side) is a skeleton. V's generator is quasi-local, so the gauge couplings are quasi-local, which raises the range question; X1 says so (§7).
- **E6** ("proved, given L3 and E1"; :89) is honestly conditional. But L3(b) is *suggested* and L3(c) is mostly suggested (F4:101-111), so E6 inherits "suggested" in those cases. ROUTES does not propagate this.
- **Lemma Z** (:125) **survives** [proved skeleton; comparator Gurarie]. It is the known statement that a gapped path changing the Green's-function winding needs zeros; it is not new.
- **Lemmas O and G:** checked in passing, no defect found.
  - The only G_SM-singlet ψψ on the 16 is ν^cν^c (re-derived by hypercharge arithmetic).
  - The Read-based "no dimer factorisation" step is in fact elementary: a block-product Gaussian state has a k-independent superlattice projector.
- **Does X1 assume the target?** No. **Contradict main?** No.

---

## 5. F5 Lemma B and Lemma D (F5 ROUTE_REPORT:69-99)

**Lemma B (Gaussian-state doubling): survives** [proved].
- The proof is Stokes on the line bundle of a rank-1 projector field on T³ minus points. It is the state-side twin of main's "net Weyl charge on the torus is 0 (Stokes)" (PRIOR_ART:68, LOCAL_HALL_FREE_MIXED_WEYL_QUARTET:400-407).
- Scope: translation-invariant Gaussian states, as F5 states.
- In F5-A's setting, Lemma C's analyticity excludes measure-zero discontinuity lines, so the three listed alternatives are exhaustive there.

**Lemma D (record capacity): survives under its declared reading**, but it is not load-bearing.
- Its premise "every jump writes one permanent record" is a reading. AX:182 lists decoherence mechanisms as outside the axioms and supplied separately, and a supplied dissipator need not write records. Then D is silent.
- F5-A still dies without D:
  - Lemma P plus T1 give e_sea → 1 at the node;
  - T3′ gives Planck conductivity on the energy-selective horn.
- The aftermath "the dynamics is Hermitian again" (F5:99) depends on the reading. If record-locked sites stop evolving (AX:77-80), the lattice freezes instead. The outcome (no one-handed vacuum) is the same.
- Neither lemma assumes the target or contradicts main.

---

## Tests run (all in this folder; nothing left running)

| Test | Pre-registered reading | Result | Resources |
|---|---|---|---|
| K3-T1 signed response, U_g | KILL-(b)-READING if A_em/A_abs → 1 ± 5% with zero π absorption at +ω | **KILL-(b)-READING** (ratio 1.000000 at all ω; exact via U_g(k+Q) = −U_g(k)) | 294 MB peak, under a minute |
| K3-T1F, Wilson M = −2 (dated follow-up) | NET-GAIN if ratio ≥ 2 | **NET-GAIN** (17.0008; desk 17) | 292 MB peak |
| T1F cross-check (instrument) | — | clean at radius 0.6 | small |

Both runs peaked at about 0.29 GB, just under the 0.3 GB limit.

## Files

- `PREREG.md`: the readings, the results, the dated follow-up and a timestamp note (the T1F heading's "15:16Z" was a clock mis-estimate; the order of writing and running is unchanged).
- `k3_t1_signed_response.py` → `k3_t1_output.txt`, `k3_t1_time.txt`
- `k3_t1f_wilson.py` → `k3_t1f_output.txt`, `k3_t1f_time.txt`
- `k3_t1f_crosscheck.py` → `k3_t1f_crosscheck.txt`
- `KILL_REPORT.md` (this file)

## What should change in ROUTES.md (suggested edits for the supervisor)

1. **F3-A row (ROUTES:14):** replace "Either the vacuum lases with no threshold, or E′ exists and the mirror is light" with: "A gauge-coupled one-handed tick has no exactly conserved local E′ (A2 class), so its vacuum is not stationary. U_g: gain equals loss exactly, with spontaneous emission. Generic (M = −2): net gain 17×." Keep "provisional no-go".
2. **ROUTES:20, :31:** "#4 not a price" becomes "#4's γ5 motivation is not a price. Site-algebra size (C222-class) is, and wake condition 1 may have fired: owner's call."
3. **ROUTES:20:** drop "the 11-item failure list was guaranteed". Scope the index lemma to bilinear masses on Hermitian finite-range carriers; exclude tails-ticks.
4. **ROUTES:25 and F4:87:** "⇔" becomes "⇒". "Single observable" becomes "the discriminator between SMG-success and a GS composite, once a symmetric gap without SSB is seen".
5. **ROUTES:42 (X1):** "corrects F1-R3 to target-equivalent" becomes "target-equivalent to T with exact on-site G (modulo BBC-inv); F1's 'stronger than T' stands for the full contract".
