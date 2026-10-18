# Panel D, gravity lens: quantum gravity / GR (Euclidean vs Lorentzian, OS reconstruction, emergent gravity on lattices)

**Provenance.** Claude Opus 5.5 at the configured effort. This is the same model family as the supervisor, every route, kill and test agent, and the other panelists, so it is not an independent check. Unrefereed. The panel advises; Jon decides. Nothing here is adopted.

**What I read.**
- In full: the dossier; `SUMMARY.md`, `ROUTES.md`, `WALL.md`, `ASSUMPTIONS.md`, `OUTSIDE_VIEW.md` and `TESTS.md` of the chirality packet (branch `origin/claude/chirality-grid-exercise-20261014`, cited as `CH/`); and `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines, cited as `AX`).
- `DEFERRED_DECISIONS.md:121-146` (origin/main).
- Chirality reports: `combos/X3/COMBO_REPORT.md`; `kills/K2/KILL_REPORT.md` (verdicts and contingency); `kills/K2c/K2c_REPORT.md` (summary); `kills/K2c/REFEREE_VERDICT.md`; the X2-L8 lines.
- Gravity packet (cited as `GR/`):
  - `SUMMARY.md` §§21–27 (`:534-813`);
  - `TESTS.md`: R19-28/R19-33 (`:8506-8913`) and the whole C5 follow-up (`:9146-9735`: F1–F6, NF-1, E1, TW-1/2/3);
  - `agents/panel_F/SYNTHESIS.md`;
  - `agents/C5_R19-28_report.md` and verdict;
  - `agents/C5_R19-33_report.md` (§0 and §5) and verdict;
  - `agents/C5_R2-4_report.md:270-340` and `C5_R2-4_referee.md`;
  - `agents/C5_R2-5_referee.md` §7.

**NT-1/2/3.** No reports had landed in `next/NT*/` at 20:51Z, so I give conditional moves in §4.

**Labels.** proved / checked / suggested / reading / comparator (RECALLED = from memory, not re-verified this session).

**Script.** One tiny script: `scripts/overlap_det_reality.py` → `.out`. Under 50 MB, seconds.

---

## Plain words first

**D3 (time) is the decision that matters from my side, and it hinges on reflection positivity.**
- Set B (Euclidean Z⁴ with a_t = a_s) earned its "best gravity bill" from one symmetry. A 90° turn that swaps time and space makes every particle share one light cone automatically.
- But a Euclidean rule becomes quantum physics only through reflection positivity (RP). RP is what turns a Euclidean weight into a Hilbert space, a Hamiltonian and probabilities.
- RP has now failed in both places where set B needed an exact structure:
  - gravity's Newtonian/conformal part, when built from an exactly conserved stress (R19-33, refereed);
  - gauge-coupled overlap fermions (K2c, refereed, 2D proxy).
- The one gravity construction on record that restores RP (R19-33's "D2" version) does it by picking out a time axis. A preferred time axis is exactly what lets loops split the light cones again, which is the problem set B was chosen to avoid. This is suggested by the R19-33 worker and allowed by symmetry per its referee; the size has never been computed.
- My judgement: set B's advantage is likely gone exactly where it was supposed to pay. Work in set C, where a Hamiltonian makes positivity automatic. Keep set B as a comparator with one sharp reopen test (§5).

**Two clarifications the owner should have before choosing set B's "prices".**
1. **"Π-W for matter" does not pay K2c's failure as Π-W is defined.**
   - Π-W keeps reflection positivity, only with a complex-conjugated reflection (`GR/agents/C5_R2-4_report.md:293`).
   - K2c's weight is real and positive (checked here), so the conjugation changes nothing.
   - So "Π-W for matter" really means giving up positivity of the real-time theory: no Hilbert-space probabilities for matter. That collides with Admissibility's "probability distribution" (`AX:60-61`) and with the wall's forbidden weakening (`CH/WALL.md:44`).
2. **"5D fermions without Pauli–Villars" works for vector-like matter, but not for chiral matter.**
   - The bare 5D determinant is RP (checked by K2c).
   - But a finite fifth dimension puts the mirror particle on the far wall, under the same forces. Removing it again needs symmetric mass generation (SMG), the same open problem set C's routes face.
   - So set B no longer offers a chirality route that avoids SMG, unless NT-1 passes and a 4D/infinite-volume RP mechanism turns up.

**The other three decisions.**
- **D1 (matter per site): (a).** Read a physical site as a coarse cell, and decide this once for matter and the graviton together. The supplied graviton already needs about 10 slots per cell and conflicts with one M₂(C) per site.
- **D2 (range): do not adopt now.** If it is ever adopted, allow quasi-locality in space only (set C), never in Euclidean time, which is what breaks RP.
- **D4 (compute): (b) with (c).** Seek SMG/QMC collaborators with a precise ask, and record the prices meanwhile. First run two cheap gravity-side kill tests that could save weeks of QMC.

**Next action: compute the one-loop light-cone leak from the RP-repaired (D2) gravity bridge on Z⁴.** It decides D3 from the gravity side, independent of chirality.

---

## 1. Recommendations per decision

### D1. Matter per site: recommend (a), stated precisely and counted once with the graviton

**Plain reasons.**
- Every gravity construction C5 kept alive already needs more than a qubit per cell:
  - the supplied graviton (P-N1, "conflicts with one M₂(C) per site", `GR/SUMMARY.md:777`);
  - the Krein graviton's 10 slots per cell (P-r19-25b, `GR/TESTS.md:8648-8649`);
  - the root's roughly 90 fermion modes, which make a root "site" at least a 90-qubit block (`GR/agents/panel_F/SYNTHESIS.md:52`).
- So the program has been running (a) silently. Saying it once, for all sectors, is honest bookkeeping. Deciding it separately for chirality would double-count.
- **(b) is the wrong lever.** Lemma R is independent of fibre size (`CH/ROUTES.md:146-156`, referee-confirmed), and the surviving routes need 16 to about 10³ modes, not 4.
- **(c) is not a final option** under "only observed outcomes need matching": handedness is observed. It is acceptable only as the interim record (D4(c)).

**Technical cautions on (a)** (reading/suggested).
1. **"Coarse cell" must not break the fine lattice's translation covariance in the law** (`AX:57-58`). There are three honest readings:
   - **(a-RG):** the physical spacing is an emergent correlation length. E1 found a covariant emergent cutoff, with protected gaps staying at zero (`GR/TESTS.md:9593-9607`).
   - **(a-SSB):** the state breaks translations down to a superlattice. Suggested hazard: N³ degenerate registrations give domain walls with cutoff-scale tension, which is cosmologically dangerous unless they formed before any inflation-like era.
   - **(a-ladder):** an internal stack per site. That is (b) in disguise.

   Only (a-RG) is clean.
2. **Coarse-graining does not evade Nielsen–Ninomiya or Lemma R.** Anomaly and index content are invariant under blocking (comparator; `CH/OUTSIDE_VIEW.md:19`). So (a) changes the counting, not the wall. The chirality work still has to be done by interactions at some scale.
3. **Records must live on fine (qubit) sites.** Otherwise P-X2-1 strains "one record per site" (`AX:79-80`; `CH/combos/X2/COMBO_REPORT.md:212`).
4. **Which spacing is ℓ_P?**
   - a = ℓ_P is load-bearing and not asserted by the axioms (`GR/agents/panel_F/SYNTHESIS.md:44`; `AX:189-190`).
   - Under (a) this choice must be stated, because every C5 exceedance scales with it.

### D2. Range: recommend not adopting a non-finitely-generated kernel now; if ever, quasi-local in space only

**Plain reasons.**
- The only route that needs D2 is set B's overlap (route 1), and its RP is failing.
- In set C, a kernel with exponential tails in space does no harm to unitarity: the Hamiltonian is still Hermitian, and signals still have an effective light cone up to exponentially small leakage.
- But quasi-locality alone does not crack the wall in continuous time. F2-T's Lemma H shows that compact non-on-site chiral charges are balanced per charge sector (proved for free fields; `CH/ROUTES.md:13`). The referee says this does not fully reduce to SMG (`CH/ROUTES.md:156`), but no route uses the remaining gap.
- So adopting D2 now buys nothing concrete.

**Technical.**
- **Euclidean-time tails are what break RP.**
  - K2's mechanism is "a non-factorizable coupling of U₊ and U₋ through a time-nonlocal fermion kernel" (`CH/kills/K2/KILL_REPORT.md`, consistency section on R10-2). The kill report's R19-33 bullet adds, as suggested and untested, that a graviton coupled through the same kernel looks worse.
  - The overlap's locality also needs the plaquette bound (Hernández–Jansen–Lüscher, comparator; X3 price P-X3d). That bound is itself non-RP for odd Lx (K2c, referee-confirmed) and suggested non-RP in 3D/4D (NT-2 tests this).
  - So in set B, D2 is not a mild range relaxation. It carries an RP liability.
- **The gravity sector already prices worse non-locality.**
  - Π-NL is a power-law instantaneous 1/∇² constraint (`GR/agents/C5_R2-4_report.md:294`).
  - Comparator: Coulomb-type instantaneous constraints are acceptable because they solve constraints and carry no propagating signal. Generic power-law dynamical couplings lose Lieb–Robinson-type causality (RECALLED).
  - Recommended reading (owner's call): if D2 is ever adopted, adopt it as "exponentially decaying in space, with a stated decay length of a few a", and record it as Π-QL (`C5_R2-4_report.md:296`). Do not adopt "any non-rational kernel".

### D3. Time: recommend set C as the working arena; set B as a comparator with a sharp reopen test

**Plain reasons (gravity jointly with chirality).**
1. **Set B's gravity advantage is narrower than "best bill" suggests.**
   - The referee narrowed R19-28 to "its formal linear-response and charge-counterterm bill is lower", not its total bill (`GR/agents/C5_R19-28_referee_verdict.md:13-18,22`).
   - What remains walled or open:
     - R2-4 (`GR/agents/C5_R2-4_referee.md:77-81`): GR cannot come from a positive local Gibbs weight;
     - R2-5 (records in OS-reconstructed time, open);
     - R2-1 and K2 (nonlinear completion, open);
     - R19-33: the conserved GR bridge fails site RP [ref] (`GR/TESTS.md:8909-8913`).
2. **Repairing gravity's RP on Z⁴ re-introduces a foliation.**
   - The only RP realization on record (D2) breaks W(B4) to W(B3)×Z₂ᵀ and loses exact conservation at dimension 6 (`GR/agents/C5_R19-33_report.md:220-245`; referee item 7, `C5_R19-33_referee_verdict.md:17`).
   - A dimension-6 Ward violation inside a cutoff-dominated loop is the textbook Collins et al. route by which a frame leaks into dimension-4 light-cone rows. The campaign's own R7-5 says the same: leakage is "forced by any part of the dynamics that sees the lattice frame" (`GR/agents/C5_R7-5_report.md:44`).
   - Power counting (suggested): δc ~ (κ²/a²)/(16π²) × c₆. At a = ℓ_P, κ²/a² = 32π. So δc ~ 0.6·c₆, against matter-cone bounds around 1e-15 to 1e-21.
   - Unless c₆ is zero by some protection, **set B with RP-repaired gravity loses its one-cone protection to the gravitational loops**. R19-33 itself flags this (`C5_R19-33_report.md:242-245`).
3. **Set B's chirality advantage is under the same RP stress** (the plain-words points above):
   - K2c fails RP on the torus for the exact hard measure [ref];
   - Π-W does not absorb it (checked + proved, below);
   - the 5D escape returns to SMG for chiral matter.
4. **Set C costs, stated honestly.** The matter light cones need either:
   - 4 tunings per charge class per order; or
   - one law-functional clause (D1∞), counted as zero numbers under the campaign's convention (`GR/SUMMARY.md:771-774,792`).

   Positivity, records and the Lattice axiom are untouched (Z³ is kept; continuous time is supplied content, and the "time metric" is an open gate, `AX:185`).

**Technical: the Π-W point.**
- **Π-W's text:** "weight (real or complex), reflection-positive under Θ = θ∘conj" (`GR/agents/C5_R2-4_report.md:293`). That is the θ-term precedent (`:281`). It drops positivity of the *measure* and keeps OS positivity of the reconstructed space.
- **K2c's failure is a failure of OS positivity itself**, on gauge-invariant test functions (`CH/kills/K2c/REFEREE_VERDICT.md:22`).
- **Checked** (`scripts/overlap_det_reality.out`). In the K2c proxy (2D U(1), M = 1, m = 0.05, antiperiodic time, admissible links), det D_ov(m) is real and positive to 1e-16 over 120 configurations (Lx×Lt = 2×12, 2×16, 4×8), with min|H_W| ≥ 0.86. The unitary-phase/Hermitian-γ5 argument makes this exact for vector-like overlap (proved, one line: γ5-hermiticity pairs eigenvalues, and the real eigenvalues map to m and 2).
- **Hence** Θ∘conj = Θ on this weight, and Π-W *as defined* cannot pay K2c (proved, given the check).
- **The dossier's "Π-W for matter" is therefore a new, stronger price:** OS positivity is abandoned for matter. Its real-time theory then has an indefinite metric (Krein space), with Planck-scale negative-norm states.
- **Comparator (RECALLED):** lattice QCD tolerates cutoff-scale RP violation (improved gauge actions, overlap) because only the continuum limit is physical. This framework has no continuum limit; its lattice *is* the physics (`AX:37-41`). That tolerance does not transfer.
- **Recommendation:** rename it, e.g. "Π-W′: matter OS positivity abandoned", so the owner does not price it as the milder Π-W.

**Technical: the 5D escape** (comparator plus reading).
- Finite-L_s domain-wall fermions without PV fields have a positive 5D determinant (K2c checked; standard Wilson-in-time positivity).
- The bulk modes become physical Planck-mass states.
- But a 4D gauge field that is constant across the fifth dimension couples to both walls, so the light spectrum is vector-like (Kaplan 1992; `CH/OUTSIDE_VIEW.md:75`).
- Chirality then needs far-wall symmetric gapping (F4/X1, frontier I) or a localized gauge field (Grabowska–Kaplan, which has its own non-locality critiques; `CH/OUTSIDE_VIEW.md:84`).
- Lemma R makes the same point from the other side: finitely many helper fields per site means zero net chirality (`CH/SUMMARY.md:30`).

**What time structure gravity needs** (reading, from the tradition and from the repo's own results).
- Lorentzian signature, one causal cone shared by matter and gravity (GW170817), positive-norm TT quanta, and positive energy.
- An instantaneous constraint sector (the Newtonian/conformal part) that carries no propagating states.
- **Every working quantization of linear GR gets the last two by separating time from space at some stage:** ADM/TT reduction with the positive-energy theorem, or Gupta–Bleuler/Krein for covariant gauges (comparator).
- **Covariant Euclidean gravity has the conformal-factor problem** (Gibbons–Hawking–Perry). The repo rediscovered it as R2-4's negative trace eigenvalue (`C5_R2-4_referee.md:34`) and R19-33's conserved-bridge RP failure.
- **Lattice quantum gravity's history agrees** (comparator, RECALLED): Euclidean dynamical triangulations did not produce extended 4D geometry, while causal (foliated) triangulations with a transfer matrix did.
- **Foliated continuum gravity (Hořava–Lifshitz type) has exactly the matter-cone percolation problem from graviton loops.** Published estimates push its Lorentz-violating scale far below M_Pl, roughly 1e10–1e11 GeV (Iengo–Russo–Serone 2009; Pospelov–Shang 2012; RECALLED, figure approximate).
- So gravity wants a foliation, and a foliation gives up the symmetric cone protection. **Set C states that openly; set B, once gravity is made positive, arrives at the same place by a longer road.**

### D4. Compute and collaborators: recommend (b) with (c), after two cheap gravity-side kill tests

**Plain reasons.**
- The decisive tests for routes 2 and 3 are QMC/HMC at weeks scale. On a 16 GB machine with a 1.5 GB-per-process budget, in-house (a) is not realistic. What decides these questions is expertise in the diagnostics: Golterman–Shamir zeros, intermediate SSB phases. Cycles are secondary.
- Ask people who already run these codes. Record the prices meanwhile; the wall is the field's open problem.

**Technical sequencing (suggested).**
1. **Before any QMC for route 2, size X2-L8 (P-X2-7).** Non-trivial CKM *forces* a first-order traceless-strain channel in the flavour sector (`CH/combos/X2/COMBO_REPORT.md:126-136,218`; proved, checked over 1120 subgroups).
   - First-order strain couplings are exactly what TW-2 found exceeding the NANOGrav clock row by ×4.7–17.8 on one branch (`GR/TESTS.md:9709-9711,9728`).
   - This takes hours. It could kill route 2 on observation before any SMG question arises, unless Jon adopts panel F's single primitive (`GR/agents/panel_F/SYNTHESIS.md:81-89`), which would stipulate the channel away.
2. **Run the B-LEAK test (§5)** before spending anything on 4D HMC for set B.
3. **Collaborator asks**, each a precise question:
   - Kikukawa (or Fukaya/Onogi): "Is non-RP of the gauged overlap/PV-DWF measure at finite spacing known? Is there an infinite-volume or 4D mechanism?"
   - Catterall/Hasenfratz: "Does a filtered cubic-invariant quartic on the walker corners (X2) have a symmetric strong-coupling phase in your 4D staggered SMG code?"
   - Golterman–Shamir: the F4-L2 propagator-zero diagnostic.

---

## 2. How the decisions interact

- **Does D3 = set B force D2?**
  - Only if set B is to deliver chirality without SMG. The overlap needs a non-rational kernel (Lemma R).
  - With finite range, set B's chiral option is finite-L_s 5D, and the mirror sits on the far wall, so it reduces to SMG exactly as in set C.
  - So set B forces D2 = yes in its only SMG-free form, which is the form now failing RP (K2c; NT-1 pending).
- **Does D1 = (a) make D2 moot?** No.
  - Lemma R is fibre-independent (`CH/ROUTES.md:146-153`).
  - What (a) does: a non-rational kernel on the coarse lattice could be the effective law of a finite-range fine lattice plus a large internal slab (A4's cheapest test, `CH/ASSUMPTIONS.md:10`). Lemma R applied to the fine rule then puts the mirror at the slab's far end, so route 1 becomes route 3 (10³ modes per cell, far-wall SMG).
  - Either way, D1 (a) relocates the D2 question; it does not remove it.
- **D3 is coupled to C5's owner Question 2, the counting convention** (`GR/SUMMARY.md:792`).
  - If law-functional clauses count as zero numbers, as (S) and (Σ) were counted, set C's cone cost is one clause (D1∞), and set B's advantage shrinks to bookkeeping (12 vs 33+ conditions).
  - If not, set C carries 4 tunings per class per order (~1e-16), and set B is the only untuned cone mechanism. Then its RP problems would be worth fighting despite the failures.
  - **I recommend Jon answer Q2 before D3.**
- **D3 is also coupled to the scale choice** (`AX:189-190`).
  - Gravitational-loop leaks scale as (ℓ_P/a)².
  - If 1/a ≲ 1e10–1e11 GeV were allowed, set B plus foliated gravity could keep the matter cones at the cost of a sub-Planckian grid. Panel F found the same threshold for the Earth row, 1/a ≲ 8e10 GeV (`GR/agents/panel_F/SYNTHESIS.md:44`) (suggested).
  - A sub-Planckian grid also brings dimension-6 Lorentz violation at a² ~ (1e-10 GeV)⁻², which GRB dispersion bounds already probe (comparator, RECALLED, not checked).
- **D1 interacts with gravity through the species count.** More modes per cell mean more contributions to the shear and strain rows. Panel F's single primitive covers all of them by stipulation. Without it, each extra species adds strain channels (F1/F6 type) that must be checked.
- **D4 sequencing interacts with D3.** If B-LEAK comes out Planck-sized, 4D HMC for set B is moot, and the compute and collaborator effort goes entirely to SMG (routes 2 and 3).

---

## 3. The strongest argument from my tradition, and the steelman against me

**For my recommendation.**
- A Euclidean lattice is a superb regulator and a poor ontology.
- OS reconstruction is the only bridge from a Euclidean weight to quantum probabilities. In a framework whose lattice is physical (no continuum limit, `AX:37-41`; the Born-weight reading of Π-W, `C5_R2-4_report.md:293`), every failure of reflection positivity at finite spacing is a physical negative-norm sector, not a removable artefact.
- Gravity is the field that most resists Euclidean positivity (the conformal factor). The repo hit that twice (R2-4, R19-33), and the only positive repair re-introduces a time axis (D2).
- Set B's one real advantage, symmetric cone protection, therefore has to survive a foliated gravitational sector. Power counting says it probably does not at a = ℓ_P.
- Set C makes the foliation explicit from the start, keeps positivity automatic (Hermitian H), keeps the Z³ axiom, and pays the cone cost as one openly counted clause.

**The steelman against me.**
1. **Set B is the only *mechanism* for one light cone in the whole program.** Everything else (D1∞, (Σ), the single primitive) states the answer. Lorentz invariance of matter is the best-tested symmetry in physics, at 1e-20 and beyond. Giving up its only mechanism for a few finite-size 2D failures is premature.
2. **The failures are small and narrow.** They are a 2D U(1) vector-like proxy at Lx = 2, finite tori, relative eigenvalues ~5e-6 (`CH/kills/K2c/REFEREE_VERDICT.md:22`).
   - The referee explicitly withholds 4D, non-abelian, infinite-volume and chiral conclusions.
   - The D2 leak is uncomputed. Its coefficient could vanish, for instance if residual W(B3)×Z₂ᵀ, on-shell conservation to O(a²), and the TT/bridge identity on conserved sources (`C5_R19-33_report.md:228-235`) protect the dimension-4 rows at one loop.
3. **Lattice QCD, the only non-perturbative 4D gauge theory that works quantitatively, is Euclidean and hypercubic**, and lives with cutoff-scale RP violations. Hamiltonian lattice gauge theory is far less developed.
4. **Set C's clause makes the framework unpredictive in exactly the sector where a grid might show itself** (panel F, C5: "imposes rather than predicts").
5. **The "Π-W′" objection cuts both ways.** In set C, chiral gauge theory has no constructed Hamiltonian version either. So set C is not ahead on chirality, only on positivity.

**My answer.** Points 1 and 3 are the serious ones.
- Point 3 does not transfer, because lattice QCD takes a continuum limit and this framework cannot.
- Point 1 is why I make the B-LEAK computation the next action rather than closing set B. If the leak is protected, the steelman wins and I would reverse on D3.

---

## 4. What would change my mind (including NT-1/2/3)

| Evidence | Effect on my recommendations |
|---|---|
| **B-LEAK = protected zero, or below bounds at a = ℓ_P** | Set B's cone advantage survives with positive gravity. I would move D3 to "set B active, conditional on NT-1 and a 4D RP check", and support D4 spending on set-B HMC. |
| **B-LEAK = O(κ²/a²/16π²), i.e. Planck-sized** | D3 → set C firmly, independent of chirality. Set B survives only with a sub-Planckian grid (re-opening `AX:189-190`). |
| **NT-1 CHI-RP-FAIL** | Route 1's real-time branch needs Π-W′ (matter OS positivity abandoned), which I would advise against, or the 5D/SMG fallback. Set B's chirality is then no better than set C's. Reinforces set C. |
| **NT-1 CHI-RP-PASS-at-power** | Surprising and important: the chiral measure would behave differently from its vector-like part. I would want a non-abelian or 4D-slice repeat before reopening route 1. Combined with a benign B-LEAK, this would flip D3 to set B. |
| **NT-1 OPEN (measure not built)** | No movement. |
| **NT-2 PG3-NEG** | The admissibility bound that the overlap's locality needs is itself non-RP in 3D. Set B's route 1 is then priced twice: the pure-gauge support plus the fermion kernel. Reinforces set C and D2 = no (in time). |
| **NT-2 PG3-PSD** | Removes that one liability only. K2c still stands. |
| **NT-3 TG1-SYMMETRIC** | Route 2 survives its cheapest kill. It is a set-C-compatible (continuous-time, finite-range) route, so this strengthens set C and the D4 collaborator ask to Catterall/Hasenfratz. X2-L8's first-order strain channel still needs sizing. |
| **NT-3 TG1-BROKEN** | Set C's chirality rests on route 3 (F4 slab DQMC) alone. It does **not** push me to set B, because set B's chirality fallback is also SMG. It raises the priority of D4(b) for F4's DQMC. |
| **Jon answers C5 Q2 "no"** (law-functional clauses count as numbers) | Set C's cones cost tunings at every order. I would then recommend fighting for set B's RP (literature asks, 4D tests) despite the failures. |
| **A literature mechanism for infinite-volume gauged-overlap RP** (Kikukawa or Lüscher school) | Reopen route 1's real-time branch. |

---

## 5. One concrete next action: test "B-LEAK"

**Question.** On Euclidean Z⁴ with a_t = a_s, couple a free massive scalar (then a Wilson fermion as a comparator) to the spatial-TT graviton plus the D2 instantaneous bridge. This is the only gravity realization on record that is site-RP to all orders (`GR/agents/C5_R19-33_report.md:20-35`). At one graviton loop, is the matter's time–space speed row (the W(B3)×Z₂ᵀ-allowed dimension-4 anisotropy) zero, small, or of order (κ²/a²)/16π²?

**Controls.**
- The same loop with K2's exactly conserved stress (not RP, but W(B4)-covariant on shell). Its speed row should vanish by W(B4) (T1/F2/O1).
- A pure W(B4) control kernel.

**Pre-register these FIXED readings.**
- **LEAK-ZERO:** the row vanishes, proved or ≤ 1e-12 checked, with the protecting identity named.
- **LEAK-SMALL:** nonzero but below the matter-cone bounds at a = ℓ_P; state the bound used.
- **LEAK-PLANCK:** |δc| ≥ 1e-6 at a = ℓ_P.
- **OPEN:** otherwise.

**Reuse.** R19-33's scripts (`.../scratchpad/C5/R19-33/scripts/`) and R19-28's Z⁴ kernel counts.

**Cost.** Hours to a day. Small Fourier-space loop sums on L⁴ grids, well under 1 GB.

**Why this serves "match observed physics".** One light cone for all matter is among the most precisely observed facts. This test decides whether the time structure that was supposed to deliver it (set B) still does once gravity is made quantum-mechanically consistent. That settles D3 on gravity grounds, whatever NT-1 shows.

**Expectation (suggested).** LEAK-PLANCK, on power counting.
