# K1 kill report: X2 (three-generation corner package), F1-R1 (walker branch), F6-tC (anomaly gate)

- **Agent:** kill-round agent K1, Claude Opus 5.5. Same model family as the supervisor, route and combination agents, so **not an independent referee**. Window: 2026-10-14, 14:58Z to about 15:35Z.
- **Hygiene:** no repository was edited. Files are only in this folder. Four scripts ran one at a time with OMP_NUM_THREADS=2; the largest peaked at 161 MB. Nothing is still running. `PREREG.md` was written at 15:14Z, before any script or K1 web source; follow-ups A5, B3, B4 and C1 were appended later with dated headers, each before its own run. Two mistyped header times were corrected in place, and the correction is stated there.
- **Read:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (233 lines);
  - exercise SKILL steps 6 and 8 (origin/main);
  - the packet's `WALL.md`, `ASSUMPTIONS.md` and `ROUTES.md`, in full;
  - `combos/X2/COMBO_REPORT.md` and `PREREG.md`, `routes/F1/ROUTE_REPORT.md` and `routes/F6/ROUTE_REPORT.md` and `PREREG.md`, all in full;
  - the C1 script (`routes/F1/scripts/c1_emanant_z16.py`) and the tC script (`routes/F6/scripts/tC_anomaly_gate.py`), with their outputs.
- **Path abbreviations:**
  - **PK** = `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/chirality-grid-20261014/.claude/science/exercises/chirality-grid-20261014/`
  - **X2** = PK`combos/X2/COMBO_REPORT.md`; **F1** = PK`routes/F1/ROUTE_REPORT.md`; **F6** = PK`routes/F6/ROUTE_REPORT.md`
  - **OUT-A, OUT-B, OUT-B4, OUT-C** = `scripts/a1_emanant_reps.out`, `b1_meanfield_10channel.out`, `b4_staggered_10channel.out`, `c1_selection_recheck.out` in this folder.
- **Labels:** **proved** (a complete short argument here, unrefereed); **checked** (a script in this folder); **suggested** (an argument not checked); **reading** (an interpretation); **comparator** (literature).

---

## Plain-words summary

**The main kill failed.** X2 named one cheap test that could kill the package (X2:252): a hidden clash between grid symmetries and the mirror particles that would stop them being made heavy symmetrically. I computed it, and there is no such clash, in any form.

The reason is simple:
- The grid's shifts and rotations act on each special-momentum particle only by a plus or minus sign (checked).
- A sign that acts on a whole particle is indistinguishable from the particle's own fermion sign.
- So each corner's anomaly is just the anomaly of one Spin(10) 16, and the literature shows that is zero (comparator).

The consequence cuts both ways:
- **For X2:** nothing in the symmetries forbids gapping the mirror without breaking symmetry. That obligation is now purely dynamical.
- **Against overselling X2:** nothing in the symmetries protects the three light generations either. They stay light only because the law is built so they do not feel the strong force, and because their remaining couplings are weak. That is "natural", not topological.

**The second objection, Golterman–Petcher–Rivas (GPR), is not defused. It is sharpened.** GPR found that this kind of model breaks its symmetry on the way to strong coupling. In a mean-field estimate:
- X2's filter does not remove that tendency. With the 7-site filter it is slightly stronger than in the unfiltered model; with the 27-site filter it is about 3 times weaker (checked).
- Any such symmetry breaking would also break the Standard Model forces at the grid scale, which is fatal (proved).

Modern 4D lattice studies find an intermediate broken phase as the generic outcome; avoiding it takes an extra tuned parameter (comparator).

The usual escape is to go to very strong coupling, where the models become a lattice of independent sites with a symmetric ground state. X2's filtered interaction has no such limit: its "sites" overlap heavily (checked). So X2 must now also show that a symmetric strong-coupling phase exists at all, a precondition that EP and the staggered models get for free.

**Verdicts:**
- X2: **wounded** (two named gaps), not dead.
- F1-R1 walker branch: passes the full anomaly gate; wounded on its selection-rule claim and inherits X2's gaps.
- F6-tC: **survives**, and its named residual is now closed.

---

## Verdict table

| Item | Verdict | Reason (label) |
|---|---|---|
| X2's "cheapest open kill": mixed Z₂³ / crystalline classes on the 5-corner mirror (X2:252) | **survives (kill failed)** | Every class vanishes for every corner set at 16 per corner: absorption lemma (proved) plus A1, A3, A3' and A4 (checked); α₁₆ = 0 (comparator) |
| X2 package overall (L_X2, X2:171-177) | **wounded** | **G1.** No atomic strong-coupling limit, so whether a symmetric strong-coupling phase exists is a new explicit precondition (B2/B3 checked; reading). **G2.** The intermediate 10-vector SSB that breaks G_SM is inherited at mean-field strength (B0 proved; B1/B4 checked; 4D lattice record comparator). Still blocked-equivalent (GS condition 3). |
| X2:245 "intermediate SSB inherited structurally (suggested)" | **upheld; upgraded to checked at mean-field level** | f_NN: susceptibility 1.14× the unfiltered control; f_F1: 0.31×; uniform condensate leads (OUT-B4) |
| X2:248 "GPR rests on large-N extrapolation" | **corrected** | GPR used a strong-coupling hopping expansion (four-fermion) and large N (Higgs–Yukawa at strong coupling; both versions at weak coupling). Their symmetric strong-coupling phase is built on the on-site λ term with expansion parameter 1/√λ (comparator, hep-lat/9207005 text; the "atomic" reading is mine) |
| X2-L3 (F1:108 selection rule false for 3 light corners) | **survives (independently rechecked)** | 6 allowed light·mirror³ label sets and 1 allowed light³·mirror set (OUT-C) |
| X2-L5 (non-orthogonal ψ_S, X2:114) | **survives; quantified** | Aggregate overlap 0.63 (f_F1) and 1.22 (f_NN) of K(0); kernel support 125 and 25 sites (OUT-B) |
| F1-R1 walker branch (F1:116) | **wounded** | Passes the full anomaly gate, all classes not only cyclic (this report). Its selection-rule claim (F1:108) is dead for the 3-light split. It inherits G1/G2. |
| F1-C1 reading "ν_R forced by translations plus fermion parity alone on the staggered carrier" (F1:83) | **wounded (scope)** | That class is emanant. It binds only gapping that keeps the corner nodes in place. A one-line counterexample to the lattice-level reading: a chemical potential gaps one staggered field while keeping every shift, (−1)^F and i^F (proved). Not my main target; the full non-abelian staggered shift group was not checked. |
| F6-tC gate (F6:142-166) | **survives; residual closed** | The residual "global bordism classes of Spin × Z₂³ × G_SM beyond Z₁₆ and Witten" (F6:166) vanishes for translations × proper rotations × fermion parity × G_SM, with or without Z₄^X, given ν^c. Without ν^c, only classes involving Z₄^X fail, matching F6. (Proved via the lemma; checked A4.) |

---

## Test A: mixed anomaly classes (main kill test)

### Setup (pre-registered, PREREG.md §A)

**Content:**
- the walker H = Σ_a σ_a sin p_a on the site qubit;
- an on-site 16 of Spin(10);
- light at hw1, mirror at hw0 + hw2 + hw3.

**Symmetries kept:**
- lattice translations, which act on the corners as Z₂³;
- the 24 proper cubic rotations about a site, with SU(2) spin lift;
- fermion parity;
- Spin(10) ⊃ G_SM. Its centre Z₄ acts as i on the 16 and equals Z₄^X, since X = 5(B−L) − 4Y ≡ 1 mod 4 on all 16 components.

### The absorption lemma (proved here, unrefereed)

**Statement.** Let a corner's internal content be a representation V of K, with fermion parity either in Spin or equal to a central element of K. Suppose the emanant group G_em acts on the corner doublets by signed permutations that are scalar on each doublet. Then for every G_em-invariant set S of corners, the anomaly theory of S is a sum over orbits of transfers of pull-backs of α_V.

**Consequence.** The anomaly of S is trivial in every class, cyclic or mixed, whenever α_V is trivial.

**Proof:**
1. **Monomial means induced.** A monomial representation on one orbit is Ind from the stabiliser Stab(c) of χ_c ⊗ V, with χ_c : Stab(c) → {±1}.
2. **Induced means transfer.** The Dirac operator twisted by an induced bundle is the Dirac operator on the finite cover P/Stab(c), so α_{Ind} is the transfer of α_{χ⊗V}.
3. **A sign is fermion parity.** On fermions, χ_c = −1 is the same as fermion parity on that support. The map (λ, k, h) ↦ (λ·(−1)^{χ_c(h)}, k) twists the spin structure by the Z₂ bundle, or equivalently multiplies by −1 ∈ Spin(10). It is a homomorphism of structure groups, so α_{χ⊗V} = φ*α_V. ∎

### Checks

**A1 (checked, OUT-A:1-14): PASS.**
- The emanant internal action R_lat R_cont⁻¹ of all 24 spin-lifted rotations is a scalar ±1 on each corner Weyl doublet; the script asserts this for every rotation and corner.
- With translations, it generates a group of order 48 of signed permutation matrices.
- The stabiliser characters take only the values {−1, +1}.
- Orbits: {hw0}, {hw1}, {hw2}, {hw3}.
- The lemma's hypothesis therefore holds. The values never include ±i, ω or e^{iπ/4}.

**A2 (comparator): PASS. α₁₆ = 0 for Spin ×_{Z₂} Spin(10).**
- Wang & Wen, arXiv:1809.11171:
  - eq. (14): Ω₅ of (Spin × Spin(N))/Z₂^F is Z₂ for N ≥ 7;
  - eq. (18): the invariant is w₂w₃;
  - eq. (19): it is absent when the isospin-½ and isospin-(4r+3/2) multiplicities are even;
  - for even N ≥ 8 the spinor reduces to an even number of isospin-½ representations, so the bulk is trivial.
  - For the 16, under Spin(3) ⊂ Spin(10) with 10 = 3 + 7·1, this gives 2 ⊗ 8 = eight doublets.
- García-Etxebarria & Montero, arXiv:1808.00009: §3.6.3 states the Spin(10) GUT is free of Dai–Freed anomalies, and §4.3 states that Z₄ is the centre of Spin(10), so the mod-16 result follows.
- The perturbative part vanishes: Spin(10) has no cubic Casimir and there is no U(1) factor.
- Read via ar5iv/arXiv pages; the exact equations were seen through a fetch summary of the HTML.

**A3 (checked, OUT-A:16-27).**
- Method: every element u = g·zʲ with u² = (−1)^F was paired with every invariant corner set. That is 344 element-set pairs, covering the light set, the mirror set, the whole set and all 8 single corners.
- Results per component:
  - single corners give ν = ±1;
  - the light set gives {±1, ±3};
  - the mirror set gives {±1, ±3, ±5}.
- So d = 1 and d = 15 are obstructed, and **d = 16 gives 0 in every case**.

**A3' (checked, OUT-A:31-36): a genuinely mixed class.**
- The class is T_x × Spin(10) on S¹(A, T_x-twisted) × CP². It equals (−1)^{(number of corners with n_x = 1) · ind(CP²; 16)}.
- I tested 8404 torus-reducible Spin ×_{Z₂} Spin(10) bundles on CP². ind(16) is even in every case, so the class is trivial.
- Control: a single charged spin^c Weyl with c = 3 has ind = 1. The class would detect it, and both the light and mirror sets have an odd number of corners with n_x = 1.

**A4 controls (checked, OUT-A:28-29): PASS.**
- The 15 without ν^c, with Z₄^X, gives a mirror value of 3 mod 16, reproducing F6-tC (F6:163).
- The per-component translation table (−3, −1, −1, 1, −1, 1, 1, −5) reproduces F1-C1 exactly.

### Reading (pre-registered outcome)

**The mixed-anomaly kill fails.** For the full group (translations × proper rotations × fermion parity × Spin(10), or G_SM with or without Z₄^X), no anomaly forbids symmetrically gapping the 5-corner mirror or the 3-corner light set, with 16 per corner.

This also explains *why* C1 found "16 only": each corner individually needs d ≡ 0 mod 16 (OUT-A single-corner rows).

**Scope:**
- **Not covered:** time reversal or inversion (not in the axioms, AX:37-38), U(1)_F (broken in X2, X2:80), and the staggered carrier. Its shifts act through a Clifford group, not monomially, so the lemma's step 1 does not apply.
- **What a null result means:** it says nothing about whether a gapped phase exists.

### Framing correction (A5; checked, OUT-B:21-29; proved in one line)

The brief and X2:252 say "a nonzero mixed class would forbid symmetric gapping". That holds strictly only for classes that survive pull-back to the UV lattice group.
- **Where the strict obstruction lives.** It is the anomaly of the UV group, translations ⋊ proper rotations × on-site internal. For crystalline symmetries this is read through the crystalline equivalence principle (comparator: Thorngren & Else, arXiv:1612.00846).
- **What the IR must match.** The IR emanant group must match only that anomaly's pull-back (comparator: Cheng & Seiberg, arXiv:2211.12543, SciPost Phys. 15, 051; Seiberg & Shao, arXiv:2307.02534, whose Majorana chain has translation emanating (−1)^{F_L} with a mod-8 anomaly).
- **Illustration (A5).** Two Majorana chains carry an emanant ν = 2. A translation-invariant on-site term gaps them at |m| > 2: the nodes leave the corners and annihilate. Checked: the gap equals |m| − 2.
- **Same logic on the staggered carrier.** A single staggered field, whose emanant ν is −4, is gapped symmetrically by a chemical potential. This term keeps every shift, (−1)^F and i^F (proved: it is on-site, commutes with the shifts, and empties the band).
- **So emanant-only classes constrain only gapping that keeps the corner nodes pinned** (effective-field-theory-level SMG). This is moot for X2, where both kinds vanish. It does re-scope F1:83's staggered reading.

### Consequences for X2 (proved from the lemma; reading where marked)

1. **No 't Hooft matching forces massless mirror composites.** Every corner ⊗ 16 is individually anomaly-free, so the GS composite question (X2:173-177) is purely dynamical.
2. **The light 3 × 16 has no anomaly protection.** It is light only because:
   - X2-L1 forbids every symmetric bilinear;
   - the law's filter zero, X2-L2, decouples it;
   - its residual couplings are weak and irrelevant.

   This is the same status as a 16 of Spin(10) in the continuum, so it is not a defect relative to the target (reading). It does mean the hw1/mirror selection is a law choice, not something any anomaly enforces.
3. **F6's tC gate residual (F6:166) is closed for every corner split of the walker.**

---

## Test B: does GPR's intermediate SO(10) → SO(9) breaking apply to X2's filtered quartic?

**B0 (proved; OUT-B:1-2).** Under G_SM, the 10 = (3,1,−⅓) + (3̄,1,⅓) + (1,2,½) + (1,2,−½). It has **no G_SM singlet**, so any 10-vector condensate breaks G_SM at the lattice scale. In the broken phase the light stays massless, with E(hw1 + q) = |q| for both filters (OUT-B:11-14), but the gauge sector is broken. That is fatal if X2 sits there.

**B1 and B4: mean-field susceptibility of the 10 pairing channel (checked; OUT-B:3-10, OUT-B4).** The model is the walker dispersion, both legs filtered, with full BdG coherence factors.

| Filter | χ(Q=0) / χ_control(0) | Onset g_c relative to the control | Leading Q | Pre-registered reading |
|---|---|---|---|---|
| Control f = 1 (EP-like channel) | 1 | 1 | 0 (by hw: 1, ⅔, ⅓, 0) | — |
| X2 f_NN (7-site star) | **1.145** | 0.87 | 0 | **channel survives the filter** |
| X2 f_F1 (27-site cube) | **0.308** | 3.24 | 0 | partially suppressed (B1); neither "survives" (≥ ⅓) nor "strongly suppressed" (< 0.1) (B4) |

- Grid convergence: I[f] is stable to 5 digits between N = 128 and 192. B4's χ(0) ratios match B1 to 0.1%.
- A staggered condensate never leads.
- **Fixed scope:** mean field always predicts SSB above g_c and cannot produce a symmetric gapped phase.

**B2/B3: strong-coupling structure (checked; OUT-B:15-20).** The overlap kernel is K(r) = {ψ_S(x), ψ_S(x+r)†}.

| Filter | Largest neighbour overlap max_{r≠0} \|K(r)\|/K(0) | Aggregate overlap √(Σ_{r≠0}\|K\|²)/K(0) | Support |
|---|---|---|---|
| f_NN | 0.400 | 1.225 | 25 sites |
| f_F1 | 0.185, at r = (1,0,0) | 0.634 | 125 sites |

- f_NN is **not atomic** on both measures.
- f_F1 passes the pre-registered pointwise threshold (0.2) narrowly but fails the aggregate threshold.
- Reading: neither filter has an atomic strong-coupling limit.

**Literature (comparator):**
- **GPR.** hep-lat/9206010 (abstract): the EP model "is shown to undergo spontaneous symmetry breaking", and the fermions are "Dirac-like everywhere". hep-lat/9207005 (text via ar5iv):
  - the breaking is to SO(9);
  - "a broken phase separates the two symmetric phases at strong and weak coupling";
  - the strong-coupling results come from a hopping expansion in α = 1/√λ around the on-site λ term.
- **4D lattice SMG record:**
  - Catterall & Butt, arXiv:1708.06715: a very narrow broken phase between the massless and massive phases in 4D (search summary).
  - Butt, Catterall & Schaich, arXiv:1810.06117: adding a scalar kinetic term gives a region with no condensate, consistent with a single continuous transition (abstract).
  - Butt, Catterall, Hartshaw & Hasenfratz, arXiv:2608.18239 (Aug 2026): "An intermediate anti-ferromagnetic phase separates these two regimes"; the critical lines merge at a multicritical point (abstract).

**Reading (pre-registered B outcome).** GPR **applies** to X2 with f_NN, and is **not defused** for f_F1. Defusing required more than 10× suppression *and* an atomic limit; neither holds. GPR does not *kill* X2, since mean field alone never kills.

The sharper version, which is my reading:
- X2 does not need a continuum critical point; a lattice-scale mirror gap suffices. So X2 could sit at strong coupling, beyond the intermediate broken phase, **if** a symmetric strong-coupling phase exists.
- In EP and in the staggered SMG models, that phase is underwritten by the atomic limit.
- X2's filtered quartic has no atomic limit (B2/B3): its overlap enters the interaction itself, so it is not suppressed as W → ∞.

So X2 escapes GPR's strong-coupling Dirac-pairing failure (X2-L2), but it also loses the only controlled argument that its symmetric strong-coupling phase exists. Two gaps follow:
- **G1.** A symmetric, gapped, unique ground state of Σ_x Q(ψ_S(x)) at large W, restricted to the mirror sector, is an explicit, unproven precondition, separate from GS condition (3).
- **G2.** The intermediate 10-vector SSB (which breaks G_SM) must be absent where X2 operates. On the 4D lattice record, one coupling is generically not enough (suggested).

A further point, suggested and not computed: flipping the sign of Q so the 10 channel is repulsive moves the attraction into another channel by Fierz (16⊗16 = 10 + 120 + 126; 16⊗16̄ = 1 + 45 + 210). Mean field would then predict a different SSB.

---

## Other kill checks

- **Does X2 assume the target?** No. L_X2 (X2:171-177) is GS condition (3) plus "no SSB", and X2 grades it blocked-equivalent itself (X2:182-184; ROUTES.md:43). This report adds G1 as a precondition, so L_X2 is strictly stronger than X2 stated.
- **Contradiction with a landed result?** None found. The SPIN10 atomic-gap failure does not transfer, for the reason above (X2-L5 upheld).
- **Already tried (step 0)?** Eichten–Preskill and GPR were flagged at `OUTSIDE_VIEW.md:82` and `PRIOR_ART.md:84`. X2 is the EP design with exact light decoupling (X2:248). This report confirms that and adds that the EP-family weakness reappears as G1 and G2.

---

## Smallest decisive next tests (not run; for the supervisor)

**T-G1 (cheapest: hours to a day, exact diagonalization).** Replace Spin(10)/16 by the smallest symmetric-gapping-capable toy, for example SU(4) with four flavours and the 6-channel quartic. Build the filtered star quartic Σ_x Q(ψ_S(x)) on the smallest cluster where stars overlap, for example a 1D ring of 4–6 sites with a 1D filter vanishing at one light momentum.
- **Measure:** ground-state degeneracy, gap and bilinear correlations, against the unfiltered on-site quartic as control.
- **PASS for G1:** a unique symmetric gapped ground state, as in the control.
- **FAIL:** degeneracy or bilinear order caused by the overlaps.

It is not decisive for 4D, but it tests whether the overlap frustration destroys the symmetric strong-coupling state that GPR-type arguments need.

**X2-MB (X2:280-299)** remains the decisive test. It must measure the 10-vector order parameter (iii) as well as composites.

---

## Files and sources

**Files** (all in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/kills/K1/`):
- `PREREG.md`
- `KILL_REPORT.md` (this file)
- `scripts/a1_emanant_reps.py` and `.out`: A1, A3, A3', A4
- `scripts/b1_meanfield_10channel.py` and `.out`: B0–B3, A5
- `scripts/b4_staggered_10channel.py` and `.out`
- `scripts/c1_selection_recheck.py` and `.out`
- `*.err` files (time and memory)

**Sources** (comparators; how each was read is noted):
- Wang & Wen, arXiv:1809.11171: eqs. (14), (18), (19) and the N ≥ 8 conclusion, via an ar5iv fetch summary.
- García-Etxebarria & Montero, arXiv:1808.00009: §3.6.3 and §4.3, via ar5iv fetch.
- Wang, Wen & Witten, arXiv:1810.00844: abstract only. It does not discuss Spin(10).
- Thorngren & Else, arXiv:1612.00846 (crystalline equivalence principle): abstract via search.
- Cheng & Seiberg, arXiv:2211.12543: abstract and seminar summary.
- Seiberg & Shao, arXiv:2307.02534: abstract.
- Golterman, Petcher & Rivas: hep-lat/9206010 (abstract) and hep-lat/9207005 (abstract plus ar5iv text summary).
- Catterall & Butt, arXiv:1708.06715: search summary.
- Butt, Catterall & Schaich, arXiv:1810.06117: abstract.
- Butt, Catterall, Hartshaw & Hasenfratz, arXiv:2608.18239: abstract.
- Hsieh, arXiv:1808.02881, as cited at F6:165 (Ω₅^Spin(BZ₂) = 0; consistent with the lemma, since a sign is absorbed into the spin structure).
