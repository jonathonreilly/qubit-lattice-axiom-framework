# C3 lane P: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** DRAFTED, all claims traced (the PREREG disposition; lane P has no PASS/FAIL reading, TESTS.md:510-512). PRICE_NOTE.md runs to 197 lines. Its 161 path:line citations were machine-checked against the packet, candidate pack and docs at commit 8a68d36c62: 250 checks, 0 failed, every citation covered. Each unrefereed item is labelled "not refereed". It still needs the referee required by TESTS.md:512 before any PR.

**Plain summary:** I wrote the price note: one page saying what massless gravity costs on each substrate the packet tested, built only from refereed results. If we keep the fixed grid, the vacuum resists shear. The graviton then gets a mass unless two numbers are tuned by hand, each to 5.7e-99 of its natural size if a cell is one reduced Planck length. Using the registered a⁻¹ = M_Pl instead gives 9.0e-102; that is my arithmetic, not refereed. Lane K is still testing whether a third tuning, for the graviton's speed, is also needed. Frozen point patterns are either stiff on average or noisy patch by patch, and a flowing liquid loses the shared light speed. Events scattered in spacetime with link-only influence pass only for a scalar stand-in. They cost the Lattice axiom, unbounded valency, a supplied time order, and a reading of Record. Nothing tested produces the graviton itself. Placeholders are left for lanes G, M, K and X, and for F and D, which were added after this lane started.

# Lane P (campaign C3): the price note, worker report

**Worker:** Claude Opus 5.5 (max effort).
**Timing:** started 00:51Z, PREREG stamped 00:53:59Z, finished about 01:11Z.
**Repository:** no file was edited; the worktree is clean. HEAD moved from f603abf56d to 8a68d36c62 during the work. That commit only appended two lines to the end of TESTS.md, and all checks were re-run against it.

## What I read (in full)
- **Docs:** `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- **Packet:** SUMMARY.md, TESTS.md (all of it, including C3 and the added lanes F and D), ROUTES.md and APPROACH_REGISTRY.md.
- **Every `agents/*referee*.md`:** B, E1, E1p, E1p_b, E23, kill_F1a, kill_F1b and kill_F2.
- **The T1 and T2 verdicts:** `scripts/T1/referee/REFEREE_VERDICT.md` and `scripts/T2/referee/REFEREE_VERDICT.md`.
- **Candidate pack `TEST_LOG.md`, referee sections for:** K7a, K3a, K3a′, K3a″, G0c, W1, W2, FR1 and FR3. These are the refereed inputs that SUMMARY and ROUTES cite.
- **Also:** `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (grep only), to check which M_Pl convention it uses. It does not say.
- **Diff since C3 launch:** the supervisor's C3 expectations and lanes F and D. These are not used as results.

## Method
1. **PREREG.md** was written first and stamped (`date -u`). It fixes the dispositions: DRAFTED, DRAFTED WITH GAPS, or NOT DELIVERED.
2. **Drafting.** The note has the six requested sections. Each claim is drawn from a referee file or from a packet line that records a referee verdict, and is cited as path:line. Verdicts are quoted exactly.
3. **`check_citations.py`.** It holds 250 entries of the form (file, line range, verbatim needle) and checks that each cited line really contains the quoted number or phrase. Result: 250 checks, 0 failed.
4. **`coverage_check.py`.** It parses every path:line in the note (161 found) and confirms each falls inside a verified range. Result: none uncovered.
5. **`arith_check.py`.** It re-does every number the note combines:
   - μ = 2.391e8 eV⁴, μ^¼ = 124.36 eV, μ/M_Pl⁴ = 1.076e-104;
   - μ/(1.2e-3·M̄_Pl⁴) = 5.67e-99, and μ/(1.2e-3·M_Pl⁴) = 8.97e-102;
   - the K3a″ and W1 per-cell values times e² (1.195e-3 and 1.28e-3);
   - 1/(60π²) = 1.689e-3;
   - Ξ minimum 3.872e-4;
   - √(3/N̄) = 3.69e-29;
   - the 1 Gpc arrival offset 2.20e-104 s and spread 1.66e-104 s;
   - 5.01e122 links over c·t₀;
   - the proton e-fold length 5.8e22 m.
6. **Strong-word pass.** I grepped for only, never, every, exactly, dead, cannot, must and forbids (`strongwords.txt`) and checked each against its referee's scope. Fixes made as a result:
   - "Protected only with time on the lattice" became "Protected when time is on the lattice", because T1 shows sufficiency, not necessity.
   - "Nonzero in both channels at every p" became "never zero in both channels at once".
   - "White at every p < 1" became "white at p = 0.1, 0.3116 and 0.5", per the E23 referee.
   - "Lost" became "generically lost" for the liquid.
   - The FR1 wording was narrowed to the tested models.
   - I added the B referee's caution that a failed kernel or scalar model excludes that implementation, not a whole substrate class.

## Results: the note's substrate table, condensed (full cells and citations in PRICE_NOTE.md)

| Substrate | Averages | Noise per realization | One cone | Graviton | Status (referee) | Price |
|---|---|---|---|---|---|---|
| Fixed grid, untuned | Stiff. K3a″ about 1.2e-3 per cell at α = 1/137; W1 about 1.3e-3 (doubled after the referee's normalization) | None (one crystal) | Z⁴: zero by symmetry. Z³ with continuous time: −2.50 g²/16π² | Supplied only. K7a protection hangs on K3a, which is INCONCLUSIVE | Naturalness kill (K3a″ CWC, W1 CWC) | Mass near the cutoff |
| Fixed grid, tuned | Zero by two E_g/T_2g counterterms | None | As above. [Lane K pending] | Supplied | Owner decision. T2: bounded FAIL, CWC (6.45e-4 at width 10) | μ ≤ 2.39e8 eV⁴, which is 5.7e-99 of 1.2e-3·M̄_Pl⁴ (B1 c1, CWC) |
| Frozen point sets | 0 (Poisson, ensemble only) or nonzero (diluted, quasicrystal unless the range is tuned, hyperuniform +0.024) | White in the random and diluted models (strong evidence, not a bound). Quasicrystal S(0) not established | Tree level only (Poisson–Delaunay) | None | F1a kill CWC; E2 and E3 FAIL, CWC; not a theorem for all frozen sets | An exact realization-wise identity, none exhibited |
| Flowing liquid | Exactly 0 for a supplied metric | None | Generically lost, ≥ 3.872e-4 | None (a vector) | "Dead as a complete untuned escape," CWC | ρ + p = 0 degeneracy, a Lorentz-violation tuning, Qubit and Lattice |
| Events, BD | Exact law shape-blindness; mean cone | Crackle; infinite L² gain; unstable at ε = 0.2 | In mean | None | "INCONCLUSIVE — leaning FAIL" | Lattice, supplied order, Record |
| Events, links only | Shape-blind in law; massless mean kernel | Var ≤ (3 + C′s/D)·N̄; ≲ 3.7e-29 at 1 Gpc | In mean | Scalar proxy only. [Lane G pending] | Gravity PASS for the scalar proxy (E1′-b CWC); matter M-INCONCLUSIVE | Above, plus about 5e122 links per event. [Lane F pending] |

**Other sections:**
- **§3, proved versus naturalness.** Taken from B_referee items 1, 4, 8, 12 and 14 and the strongest combined statement. It adds Lemma R (narrowed), Lemma P (corrected), the fluid lemma, Lemma N, the E1 and E1′-b exact pieces, T1 and K7a, plus the naturalness qualifiers.
- **§4, axiom prices** (named as prices, none adopted):

| Price | What it touches |
|---|---|
| P0 | tune, keeping all four axioms |
| P1 | Lattice |
| P2 | Admissibility's nearest-neighbour rule |
| P3 | a supplied causal order, a new unregistered primitive |
| P4 | Record |
| P5 | Qubit, on the liquid route |

- **§5, open questions.** Placeholders for G, M, K and X, as asked, plus F and D. The extra two were pre-registered at TESTS.md:526-546 after this lane launched. There are also 8 other open items.
- **§6, provenance.** 15 rows, with verdicts quoted exactly.

## Verdict
**DRAFTED, all claims traced.** Every claim cites a refereed source, every number matches its source line, and no strong word goes beyond its referee's scope. Items that are not refereed are labelled and kept out of the verdicts:
- T0 (its Weyl value is confirmed inside the W1 referee);
- the F3 and F7 step-4 checks;
- W2 (not used);
- lane P's denominator arithmetic;
- two lane P readings.

## What a referee should re-check
1. **The tuning's denominator.** The refereed 5.7e-99 takes a cell as 1/M̄_Pl (B_referee.md:35). The registered `scale_reference_primitive` (a⁻¹ = M_Pl) does not say whether M_Pl is reduced; the non-reduced value gives 9.0e-102 (lane P arithmetic). Which should the owner-level sentence use?
2. **One cone on the fixed grid.** The note says the split is zero on Z⁴ but O(1) (−2.50) on Z³ with continuous time (TESTS.md:59-60). Is that framed fairly against the framework's continuous-time Hamiltonian models (K3a″) and K7a's tick-size condition?
3. **Two lane P readings, not refereed:**
   - the `realized_state_primitive` as the framework's own reason to require control in each realization (§5, item 8);
   - the `kinetic_isotropy_primitive` needing re-reading under P1 (§4).
4. **The P3 classification.** Is a supplied causal order correctly called "a new primitive, not in the registry"?
5. **The plain-words section.**
   - Is "no tested regulator that keeps the grid and ordinary interactions removes the mass without that tuning" in scope, given that T2 was free-level and Lemma R is narrowed?
   - Is "massless on one light cone up to Planck-suppressed power corrections" right for E1′?
6. **Inclusion choices.** I included K3a's INCONCLUSIVE, B1 c5's bounded FAIL, and FR1/FR3 as notes on the table. Are these right?
7. **What the checker does not cover.** It confirms that quoted fragments are present at the cited lines. It does not judge whether each paraphrase is faithful, so the paraphrases in §3 and the table cells deserve a read against the referee texts.

## Files (absolute paths)
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/PRICE_NOTE.md (the deliverable, 197 lines)
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/PREREG.md
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/check_citations.py and check_citations.out (250 checks, 0 failed)
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/coverage_check.py (161 citations, none uncovered)
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/arith_check.py and arith_check.out
- /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/strongwords.txt (the strong-word audit list)

**Why needs_referee is true.** The result is neither a FAIL nor a no-go. But lane P's fixed reading requires a referee before any PR to main (TESTS.md:512), and the note restates several refereed no-gos as owner-level prices.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** DRAFTED WITH GAPS, not "DRAFTED, all claims traced". All numbers are right and every path:line exists and contains its quoted fragment. But several paraphrases go beyond their referee's scope, one sentence states a settled fact as an open question, and two refereed price results are left out. Under the PREREG's own outcome mapping, a claim that exceeds its referee's scope or cannot be traced to a refereed source makes the result DRAFTED WITH GAPS. The note can go to the lane-P referee once the items in `issues` are fixed: either reword them to the referee's exact scope, or label them "reading, not refereed".

**Issues:** **Numbers: no wrong number found.** I independently recomputed:
- μ = 2.391e8 eV⁴ and μ^¼ = 124.4 eV;
- 1.076e-104 M_Pl⁴;
- 5.67e-99 with the reduced Planck mass and 8.97e-102 with the non-reduced one;
- 3.872e-4, 3.69e-29, 2.20e-104 s and 1.66e-104 s, 5.01e122 links, 6.45e-4.

Every table number I checked matches its cited referee line.

**Scope and faithfulness problems** (my judgement after reading the cited referee texts):

1. **§1, events (PRICE_NOTE.md:37): "Two things are still open: whether a single realization's order responds smoothly to strain, and anything beyond the scalar stand-in."**
   - That the order is not smooth is already established. E1_referee.md:31 says the per-realization order is "piecewise constant in strain with jumps", and E1p_referee.md:187 says links change discontinuously. What is open is whether this crackle is harmless at physical h (the lane G-A bar).
   - "Two things" also undercounts. E1p_b_referee.md:163 lists four things not established: the tensor, nonlinear gravity, the strain response, and stable initial-value dynamics. Matter is also M-INCONCLUSIVE (E1p_referee.md:10), and the events have no dynamics of their own (SUMMARY.md:232). None of these is in the plain-words list.

2. **§3, paraphrase of the strongest combined statement (line 116).**
   - "An exact linearized-diffeomorphism identity forbids the graviton mass": B_referee.md:209 says it forbids "an h-only nonderivative mass". B_referee.md:24 notes that a Stückelberg theory can be gauge-invariant and still massive.
   - "physical reference labels need protection" drops the referee's word "generic".
   - "universality" should be "leading universality".
   - The hypotheses "ordinary factorization" and "a local analytic description in terms of h_μν" are left out.

3. **§4, P0 (line 128): "Two TT counterterms, each at about 5.7e-99 of natural size" is wrong.** The counterterms are of natural size. What must be at most 5.7e-99 of natural size is the net shear number left after the counterterm (B_referee.md:26-35; row 2 of the note's own table says this correctly). "About" should also be "at most", since μ is an upper bound. The plain-words wording at line 25 has the same "about".

4. **§1, line 26: "No tested regulator that keeps the grid and ordinary interactions removes the mass without that tuning."** No single referee statement says this, and the sentence gives no scope.
   - T2 tested free fields only, and its FAIL is bounded to the families tested (T2-REF:29). The stiffness there falls as σ⁻², so it is not floored at a fixed value.
   - The F2 Gaussian kernel on Z³ does suppress the free-field stiffness exponentially without tuning. It pays by breaking reflection positivity, needing about 5e6 couplings per site, giving the Dirac field zeros at the zone corners, and keeping power-law residuals for the two tested gauge-path families (kill_F2_referee.md:64).
   - The sentence leans on SUMMARY.md:85 ("closed by T2"), which is summary prose, not a referee verdict.

5. **Refereed price results left out of the table and plain words.**
   - T1(a2) is a refereed FAIL: a smooth spatial regulator with continuous time splits the fermion and scalar speeds by about −0.696·g²/16π², depending on the regulator's shape (T1-REF:4,19,27).
   - The regulator trilemma (SUMMARY.md:55; ROUTES.md:54: "Every tested way to protect it loses one of the other three"). This is the price of a keep-the-grid regulator without tuning, and the price note was supposed to assemble it.
   - Both appear only in the provenance table.

6. **One cone on the grid: K7a's conditions are left out.** "Protected when time is on the lattice" and the plain words at line 23 omit two conditions from TEST_LOG.md:32-33:
   - Hypercubic symmetry needs a_t = 2 fine edges, and A25's leapfrog at τ = a_s is unstable (max|eig| 9.9). The stable τ = a_s/2 is not hypercubic.
   - 4D staggered fermions have 4 tastes, which differ from the 3D Hamiltonian H_ψ.

   The protection has not been shown together with stable evolution of the framework's model. This also answers the worker's question 2.

7. **"Nothing produces the graviton" (row 1, citing SUMMARY.md:59) and "No tested substrate produces the graviton itself" (line 44) are unlabelled.** SUMMARY.md:59 marks this as "(reading, as on 09-29)". The note's own rule is to label anything not refereed. It is partly backed by referee results (kill_F1b_referee.md:74; FR3 at TEST_LOG.md:643), but it should still be labelled.

8. **The B1 c5 note (line 60).**
   - It calls the 4D Euclidean random lattice "the finite-valency gap that BHS leaves". B_referee.md:75-76 says the graph has finite random degree, not a uniform valency bound, and is only O(4)-symmetric, not Lorentzian. BHS concerns Lorentzian sprinklings.
   - "Per-site TT noise is white" overstates. The referee calls the result a total-box estimator, not a direct k→0 spectrum (B_referee.md:74).

9. **The tuning's denominator (the worker's question 1) is answerable from the repo.**
   - The registered primitive pairs a⁻¹ = M_Pl with the open target a/l_P = 1 (SCALE_REFERENCE_PRIMITIVE_NOTE.md:17,39-41). l_P corresponds to the non-reduced M_Pl.
   - Repo docs use M_Pl = 1.2209e19 GeV, in 27 places, some marked "AXIOM" or "framework UV scale". No doc uses 2.435e18 GeV.
   - So the framework-convention figure is about 9.0e-102 (about one part in 10^101). That fits K3a″'s own "about 1e-100" (TEST_LOG.md:409).
   - The plain words lead with the reduced-convention 10^98. They should give both figures, or the framework's convention first. The 5.7e-99 stays the refereed figure.

10. **Minor items.**
   - P4: "4e-151 per event" is the referee's per-event *fraction* (B_referee.md:103).
   - §5 item 5 drops the referee's qualifier "which alone is not sufficient" after "suitably dynamical adjacency" (TEST_LOG.md:528).
   - §5 item 8 turns the realized_state_primitive's "registered data, not derivation output" (a rule about what counts as derived) into "the framework's own reason to require control in each realization". B_referee.md:160 calls the requirement for control in each realization naturalness-backed, not mandatory. The note does label item 8 a reading, so this is low severity.
   - The header's "every citation was machine-checked" could be read as "every claim verified". The checker only confirms that each quoted fragment is present at its cited line.

**Checked and correct:**
- All 15 provenance verdicts, quoted exactly.
- Table rows 3 to 6, apart from the items above.
- The §3 lists of what is proved and what rests on naturalness.
- P1, P2 and P5 axiom quotes.
- The P3 classification. A supplied causal order is not among the three registered primitives, so calling it unregistered and unapproved is fair.

**Re-runs:** - **check_citations.py:** re-run with OMP_NUM_THREADS=2 and `python3 -I`. 250 checks, 0 failed, matching the worker. Some needles are trivially weak, e.g. "| — |", "INCONCLUSIVE", "unbounded", "0.05" and "T0". The script shows that fragments are present, not that paraphrases are faithful.
- **coverage_check.py:** re-run. 161 citations, none uncovered.
- **Arithmetic:** re-done independently in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/P/verify/indep_arith.py. Results:
  - μ = 2.391e8 eV⁴ and μ^¼ = 124.36 eV;
  - μ/M_Pl⁴ = 1.076e-104;
  - μ/(1.2e-3·M̄⁴) = 5.67e-99, and μ/(1.2e-3·M_Pl⁴) = 8.97e-102;
  - using the exact |c₂|·e², the two ratios are 5.69e-99 and 9.01e-102;
  - the natural graviton mass is m_g ≈ 0.069·M̄ with a reduced-Planck cell, or 0.35·M_Pl with a non-reduced one;
  - (2/3)·g²/16π² = 3.872e-4;
  - √(3/2.2e57) = 3.69e-29;
  - offset and spread at 1 Gpc are 2.20e-104 s and 1.66e-104 s;
  - √6·π·(c·t₀/ℓ_P)² = 5.01e122;
  - 0.0647/100 = 6.47e-4.

  All agree with the note.
- **Source read-through:** read in full against the note's claims:
  - B_referee, E23_referee, kill_F1a/F1b/F2_referee, E1_referee, E1p_referee and the E1p_b_referee ending;
  - T1-REF and T2-REF;
  - TESTS.md:1-548;
  - SUMMARY.md:50-95 and 190-232, ROUTES.md and APPROACH_REGISTRY.md;
  - TEST_LOG.md:1-60, 230-262, 370-432, 455-535 and 580-649;
  - MINIMAL_AXIOMS:25-95, PRIMITIVE_REGISTRY_CHECK.md and SCALE_REFERENCE_PRIMITIVE_NOTE.md.
- **Planck-mass convention:** grepped docs/*.md. 27 lines use 1.22e19 GeV (non-reduced), 0 use 2.435e18 GeV.

No repository file was edited.
