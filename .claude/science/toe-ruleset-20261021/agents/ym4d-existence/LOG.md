# LOG: YM4D existence from UV stability

## Session 1 (2026-10-27)

**Brief.** Open layer 2: a conditional theorem "H-Bal ⇒ (a) subsequential continuum limits, (b) OS axioms that
survive, (c) non-triviality, (d) infinite volume". Layer 1 is P = ../ym4d-proof/ (read-only; nothing in P edited).
No commits, PRs, CL or axiom edits.

**Read (context).** P/PROOF.md (session-15/16 header, §0-§1, L6, L6loc E8.3/S5'/E8*, L7-L10, tally line), P/literature/
NOTES.md (all), P/REVIEW_S15_CONVERGENCE.md (Job 1 opening, Job 2 in full), ../openai-balaban-review/review.md (all).
Note: P's PROOF.md moved to a session-16 header during this session (tally 64/2/7/24 + 1); only its header was re-read.

**Literature (NOTES.md).** Read: MRS mp_arc 92-38 (intro, theorem), Chatterjee 1803.01950 §5-6, Lüscher 1006.4518
(§1, §4.1), Lüscher-Weisz 1101.0963 (abstract, §1), Narayanan-Neuberger hep-th/0601210 (abstract), Cao-Chatterjee
2111.12813 (§1 to Theorem 1.6). All open access; no barrier crossed.

**Method.** Each lemma's statement was written before its proof in EXISTENCE.md. Pre-stated targets in order:
(1) state H-Bal with quantifiers; (2) the soft layer (algebra, limit state, consistency, symmetries, RP, OS transfer);
(3) what H-Bal-3 adds (non-degeneracy, analytic limit, Cauchy estimates); (4) what needs more (OS0, continuity,
rotations, sources); (5) infinite volume.

**Findings.**
1. **H-Bal-2 (the published Z-stability) is used by no node.** All non-soft content comes from H-Bal-3, the law of the
   block variables at a physical scale with Balaban's small-field form and a large-field mass bound (the inductive
   content of the proof, after the R-operation), plus the flow H-Bal-1.
2. **A continuous block map exists (X-S4c):** a smooth cutoff of the principal log at radius < 2π/N keeps gauge,
   reflection and permutation covariance and Balaban's small-field form. With it, consistency across resolutions is
   automatic (X-CONS). This removes the need, stated in P §0 and S5' "Price", for E8* to make limit points consistent;
   E8* becomes a regularity property. (Not written into P.)
3. **OS reconstruction yields a Hamiltonian H ≥ 0 on (ker T)^⊥ for every limit point** (X-OS), from RP on the
   L-adic planes alone, via uniqueness of positive roots (T(2L^{-m}) = T(2)^{L^{-m}}). The single time-axis estimate
   left is ker T = 0 ⇔ time continuity (H-cont).
4. **Flowed loops are bounded and continuous but non-local at every positive flow time** (X-FLOW-NL; check x1 PASS):
   exact RP is not available for them; X-ARP + H-loc is the bridge.
5. **OS0:** the exponential-moment route (X-MOM, an implication) works for any linear field satisfying H-src; the
   dimension-4 composite (action density) violates the naive form (variance ~ ε^{-4}, ARGUED), so for composites
   H-src must be posed at non-coincident supports, which amounts to UV stability with a position-dependent coupling.
6. Non-triviality: weak form proven conditionally (X-ND, X-MONTEL, X-CAUCHY); strong forms (non-Gaussian 4-point,
   asymptotic-freedom signature) reduced to finite-dimensional Laplace lemmas, OPEN.

**Check x1.** Criteria (checks/x1_criteria.md) written before the script. Hodge Laplacians on 1- and 2-forms equal the
componentwise scalar Laplacian exactly (sides 4, 5); heat kernel strictly positive; far-link responses non-zero.
PASS, 0.5 s, 67 MB, nice 10, threads 1, load ≈ 2.3, memory free 36%. Run as python3 without -I (user-site numpy;
no external files read).

**Tally.** PROVEN-HERE 16 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 4 (hypotheses) / OPEN 9.
Unreviewed.

**Next.** LAP-1 + X-NTAF; H-cont reduction to a two-grid one-step statement; H-src' as stability with g_0(x).

## Session 2 (2026-10-27)

**Brief.** Targets: (1) X-NTAF via a one-link Laplace lemma; (2) reduce H-cont to a two-grid single-step statement and
prove what can be proven in the small-field/linear setting; (3) H-src as stability with a position-dependent coupling;
(4) a "what a reader needs to trust" section. P (../ym4d-proof/) read-only; a P session was editing PROOF.md/RLARGE.md,
neither touched. No commits, PRs, CL or axiom edits.

**Read.** EXISTENCE.md (all, by offset), LOG.md, NOTES.md, checks/x1*; P/literature/NOTES.md §2 (Dimock II large-field
thresholds) and §9 (CMP 109 transcription); P/LINEAR_PACKAGE.md (all); P/PROOF.md l.218-219, 1760-1810 (polymer
constants κ_0, K_0 only). No new primary literature; no web access used.

**Method.** Targets pre-stated in EXISTENCE.md §9 before any proof; check x2 criteria written before the script.

**Findings.**
1. **X-NTAF proven in two-sided form (| H-Bal-1, H-Bal-3L, H-Bal-3T; conditional on new hypotheses that no source
   states) [RX12-fix 11, added session 3]:** (δ_*/2)/(1/g² + β'm log L) ≤ ω(1 - P_{p,m}) ≤
   φ(G_m), uniform in K and the volume. The lower bound comes from LAP-1, an anti-concentration lemma that uses only
   one-link density ratios (Haar invariance of a one-link left shift, AM-GM on ±shifts so the linear term cancels,
   Cauchy for the second difference, a packing along a one-parameter subgroup). Corollary: the block plaquette approaches
   its free value logarithmically in the scale; the limit is not dilation invariant and admits no power-law approach.
   Unconditional instance X-WIL for Wilson lattice gauge theory (any d, N, volume): 1 - ⟨P⟩ ≥ δ_W g²/2, g ≤ 1/2.
   The sharp form (coefficient c_blk, rate 1/(2b_0 log μ)) is OPEN with two named walls: W-AF1 (Balaban's deferred flow
   theorem with β = β' = 2b_0 log L) and W-AF2 = H-corr (a correlation/Gaussian-comparison bound).
2. **ker T:** X-KER shows [observables supported at positive distance from the reflection plane] ⊂ 𝒦^⊥, so 𝒦 = {0}
   needs only a boundary-layer approximation (H-bl), weaker than translation continuity. X-2GRID (exact): the joint law
   on two grids offset by s = jL^{-n} is the push-forward of the single-resolution law ν_{K,n} under one averaging step on
   two grids offset by j/L of a block, followed by the common map A^{n-1-m}.
3. **Free Gaussian model:** X-CONT-G proves E|ΔF|² ≤ (4/β)w (w = L^m|s|) for linearised S4' block curvatures, uniformly
   in the cutoff and the volume (composite flux formula re-derived from P's Lemma 2.2(i)). Check x2 B: the true scaling
   is w²; the one-step discrepancy is O(1) (42-67% of the plaquette variance). So no single-step bound in a *local*
   norm can give H-cont [narrowed in session 3, RX12-fix 10: a dual (H^{-1}-type) norm of the one-step difference is
   not excluded]: smallness is a cancellation carried by the composite. The interacting input is H-corr (ℓ²-domination of
   block-curvature two-point functions at every resolution) + H-lin (linearisation of the composite), ARGUED to suffice.
   The small-field single step is not provable from P's linear package: it needs the fluctuation covariance at general
   backgrounds (P node N5; Balaban CMP 99, not read), which the package explicitly does not contain.
4. **Sources:** H-src' stated as a K-uniform bound on the inclusion-exclusion ΔΨ of log-partition functions with a
   position-dependent bare coupling 1/g_0² + Σz_ih_i(x) at δ-separated supports. Local counterterms cancel exactly
   (X-SRC-CT), giving K-uniform bounds on connected correlations of the action density at separated points; H-src' is
   implied by a multiscale local polymer representation (H-Bal-loc) with an explicit constant (X-SRC-RED, using P's
   polymer constant K_0). Coincident points (contact terms): H-src'-diag, OPEN.
5. Trust list written (§10.4): standard analysis, lattice RP, H-Bal-1, H-Bal-3, and local versions (3G/3L/3T, loc);
   H-Bal-2 still unused.

**Check x2.** PASS (A: exact 2D SU(2) Wilson model, LAP-1 bounds and the pair inequality, 12/12; E/g² = 0.37494 vs 3/8.
B: Gaussian two-grid variances at depths 1-3, B1/B2 hold, B3 expectations met). 0.6 s, 162 MB, nice 10, threads 1,
load 1.7, memory free 37%. `python3` without -I (user-site numpy); no external files read.

**Tally.** PROVEN-HERE 24 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 7 / OPEN 11. Unreviewed.
Snapshot: EXISTENCE_session2_snapshot.md.

**Next.** H-corr for compact U(1) at weak coupling (exactly linear composite on regular configurations); H-bl directly
from local bounds; independent review of §10.

## Session 3 (2026-10-27)

**Brief.** (1) Apply the 12 binding fixes of REVIEW_X1_X2.md and relabel every hypothesis by provenance; (2) reduce
H-Bal-3L (and 3T, 3G) to H-Bal-3(3a)-form + ONE large-field localisation hypothesis H-loc-LF aligned with layer 1's RLF
(RLARGE.md §1); (3) literature status of X-WIL; (4) public statement. P (../ym4d-proof/) read-only (a review runs there);
nothing in P edited. No commits, PRs, pushes, CL or axiom edits.

**Read.** REVIEW_X1_X2.md (all); EXISTENCE.md (all, by offset); LOG.md; P/RLARGE.md (all, by offset); P/LINEAR_PACKAGE.md
§1-§5 (N2-E, N2-lin, N2-exp, Lemma 2.5, Theorem CE); P/literature/NOTES.md §9.4-9.5 (CMP 109 (0.22)-(0.31), (1.18)).
Web (open access, no barrier): two searches; arXiv abstract pages 1602.01222, 2511.07297; ar5iv HTML of 1602.01222 via a
page summariser [read-skim]. Tags in NOTES.md (session-3 section).

**Method.** Fixes first (tagged [RX12-fix n] in EXISTENCE.md; LOG session-2 findings 1 and 3 annotated). Targets T5-T7
pre-stated in EXISTENCE.md §11.0 (21:44 UTC) before any derivation in §11.1-11.7. No numerical check run (none needed:
all steps are inequalities on stated hypotheses), so no criteria file.

**Fixes (all 12 applied).** Provenance labels and the status HYPOTHESIS (new; no source); H-Bal-1 SU(N) caveat and
M-uniformity [unverified]; H-Bal-3 split into (3a)-form (Balaban states it) and full-law packaging (new), (0.28)-(0.30)
cited instead of (1.18) with the polymer regrouping and analytic extension marked [unverified], |R| ≤ 1/2 replaced by
e^{±C_R|Λ_m|}, η_0 = η_0(m, ℓ), "diagonal-pairing variant of (0.4)"; X-ND constants redone; q ∈ [1/3, 3] remark struck;
X-CONS via the quotient 𝔄_∞ = 𝔄/𝔍 and the coarse gauge lift; X-KER reverse inclusion; H-cont in the joint L² two-grid
form (the single-expectation form is vacuous and deleted); X-FLOW-NL torus caveat and "X-RP does not apply"; X-IVND
gauge-invariance and η_0 condition; α ≤ ε_0/3; single-step finding narrowed to local norms (H^{-1}-type dual-norm route
noted); 𝒦^⊥ = CΩ caveat in X-OS and §0; §0 and §10.4 rewritten; x2 discrimination notes; X-WIL "novelty unverified".
Tally after the fixes: 24 / 1 / 3 / HYPOTHESIS-NEW 5 / 11 (the review's corrected tally).

**Findings.**
1. **One hypothesis instead of three (§11).** H-loc-LF: on the regular region Ω(V) of every coarse configuration, the
   block law has Balaban's (3a)-form (background action + renormalised polymers, localised), times exp of local
   large-field polymer activities with e^{-κd} one-link increments, and P(|V_p - 1| ≥ ε_0/3) ≤ C_Pe^{-a_P/g²} (RLF-3's
   per-cube weight). Proven: **H-Bal-3L ⇐ H-Bal-1 + H-loc-LF** (Theorem LF⇒3L; q ≡ 1, G_b = {N(b) regular},
   η_L = 2(d-1)C_Pe^{-a_P/g²}), via BG-1L-B (background-action increment from the response decay) and POL-1L (Balaban's
   (0.30) mechanism for one-link increments). Soft linear instance BG-1L-lin from P's N2-E, N2-lin, N2-exp: the increment
   is exactly -κ_{k-1}r_{k-1}(b)s + E_k(e_b)s² (envelope theorem), volume-uniform, far field weighted by e^{-m'·dist}.
2. **H-Bal-3 full-law packaging and (3b) are no longer needed** (Corollary LF⇒3: X-ND re-proven with 𝒵 bounded above
   by the per-cell upper bound instead of a large-field mass bound); **H-Bal-3G no longer needed** (X-IVND': not flat by
   LAP-1, not Haar by (LF-P), volume-uniform).
3. **H-Bal-3T not reduced.** H-Bal-3T ⇐ H-loc-LF + H-sg (small-field moderate deviations of one block plaquette). Wall
   named: one-link holomorphic ratios give anti-concentration, not concentration; H-sg is a Gaussian-domination input
   like W-AF2/H-corr.
4. **H-loc-LF ≠ RLF.** Differences: (D1) soft-kernel Markov level variable vs deterministic S4c/Balaban average; (D2)
   local Wilson leading action vs Balaban's nonlocal background action; (D3) history sum vs exponentiated fixed-field
   form; (D4) RLARGE's (PLD) is an input to RLF, (LF-P) an output needed here; (D5) C³ vs analytic on a fixed radius;
   (D6) op vs HS thresholds. Proposed meeting point **RLF-loc** (H-loc-LF with soft variable and Wilson leading term),
   usable here under "Option S" (soft block variables; RP argued: crossing coarse variables integrate out by
   ∫K dV = 1); RLF ⇒ RLF-loc ARGUED with gaps D3, D4.
5. **X-WIL literature:** no prior statement found. Chatterjee's free-energy theorem (arXiv:1602.01222) plus convexity of
   log Z gives an asymptotic U(N)-on-boxes lower bound E[S] ≳ ½(d - 1)N² log 2·n^d/β (my derivation, ARGUED); X-WIL is
   explicit, finite-volume, SU(N), periodic. Novelty unverified; not headlined.
6. **Public statement** rewritten (EXISTENCE.md §12), word for word, conservative.

**Tally.** PROVEN-HERE 29 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 3 (H-loc-LF,
H-sg, H-Bal-loc) / OPEN 11. §11 unreviewed. Snapshot: EXISTENCE_session3_snapshot.md.

**Next.** Independent review of §11; decide Option S with layer 1 (X-RP^S written proof); RLF ⇒ RLF-loc gaps D3, D4;
H-bl from local bounds; H-sg.

## Session 4 (2026-10-27)

**Brief.** (1) Merge the lanes: switch the block variables to layer 1's soft-kernel Markov variables, prove RLF ⇒ the
soft H-loc-LF ("RLF-loc") closing gaps D3, D4, re-check (a)-(d), X-NTAF, X-ND, H-Bal-3L under the switch, in particular
RP with soft blocking. (2) H-sg via the linear package and Brascamp-Lieb / log-concavity. P (../ym4d-proof/) read-only;
session 18 was editing RLARGE.md and LINEAR_PACKAGE.md; nothing in P edited. No commits, PRs, pushes, CL or axiom edits.

**Read.** EXISTENCE.md §0-§3, §6, §10.1-10.2 (X-KER), §11-§12; LOG.md; REVIEW_X1_X2.md (label table, binding fixes,
public-claim audit); P/RLARGE.md §0-§13 (session-17 text, at the start) and §0 header, §1, §1A (session-18 text, at the
end); P/LINEAR_PACKAGE.md §1-§11 (at the start), header and Props 6.4, 7.1 (frozen v1, at the end). Web: arXiv abstract
page of Biskup math-ph/0610025 [read-abs]; its PDF (open access) was fetched but its text could not be extracted, so
nothing in it was read. Tags in NOTES.md.

**Method.** Targets T8-T10 pre-stated in EXISTENCE.md §13.0 (22:15 UTC) before any derivation; check x3 criteria written
before the script.

**Findings.**
1. **RP survives soft blocking across every block-boundary plane (Theorem X-RP^S, PROVEN).** Crossing variables are not
   observed; the variables of a positive-side observable and all their ancestors lie on the positive side (kernel
   locality, nesting); everything else integrates out exactly (∫K dV = 1, coarsest first); reflection covariance of the
   kernel (Re tr(VM̄^†) = Re tr(V^{-1}M̄), 𝒩(M̄^†) = 𝒩(M̄)) turns the negative half into θ of the positive half; X-LRP
   finishes. **What breaks: site planes.** The kernel's 1/𝒩(M̄) for a link in the plane mixes both sides; in the exact
   toy of x3 the site-plane Gram matrix has min/max eigenvalue -0.195 (normalised kernel) and is PSD with the
   unnormalised kernel. X-OS needs only block-boundary planes. The whole soft layer (a), (b), (d)-soft transfers with no
   hypothesis; shifted grids are a tree of conditionally independent branches; X-S4c is not needed (M̄ is polynomial).
   The OPEN item "Option S soft-layer transfer" is closed.
2. **Under the switch, non-flatness and the lower bound become kernel facts.** The soft law has Haar density in
   [e^{-2κn_c/g'²}, (e c_N^{-1}(κ/g'²)^{N²-1})^{n_c}], entire in the complexified links (Prop. KB); the conditional law
   given the finer field satisfies H-Bal-3L exactly (η_L = 0, A_1 = κ(e - 1)/√N), so LAP-1 gives ⟨1 - P⟩_m ≥ (δ^S_*/2)g'_m²
   for any law of the finer field (Prop. LAP^S). These carry no information about the Wilson measure and must not be
   presented as Yang-Mills non-triviality. The deterministic (S4c) branch keeps its session-3 content.
3. **D4 closed by chessboard estimates (Theorem CB).** With RP for all cube-boundary planes and an even torus of cubes,
   Lemma CBE (chessboard estimate; proof written out; FILS/Shlosman/Biskup [not-read / read-abs]) gives
   P(cube Q bad) ≤ P(every level-k cube bad)^{1/N_k}. So the local large-field probability (LF-P) follows from ONE
   extensive bound, (RLF-3^dis): P(E_all) ≤ (C_dg^{-p_d}e^{-a/g_k²})^{N_k}. That is RLF-3 for the single unreturned defect
   configuration "all cubes", provided RLF-3's weights are nonnegative ratios Z_K[𝔥]/Z_K^{ref}; with session 18's
   Z_K^{ref} (fix R-2) and |T| ≤ N_k every extra factor is e^{O(N_k)} (ARGUED reading; restatement proposed to layer 1).
   Corollary: the soft limit is neither flat nor Haar at every resolution, volume-uniformly, given (RLF-3^dis) alone.
   **[RX34-fix 4, session 5] Corrected:** not Haar | (RLF-3^dis), (F); "not flat" is kernel-only (no Yang-Mills content).
   D3 is not needed (Lemma MIX: the pair inequality survives nonnegative history mixtures; soft branch uses no
   one-link ratio of the full law). [RX34-fix 8, annotated session 7 per RX56-fix 11] D3 is "reduced", not
   "dissolved".
4. **H-sg reduced, not proven (Theorem CB-sg).** Super-blocks of 2⁴ cubes and the all-cut conditioning turn H-sg into a
   disseminated moderate-deviation bound for the all-cut measure, (PLD^mod_dis): RLF-step's own input (PLD)_k (i) at
   variable threshold τ with Gaussian dependence τ²/g², for one family of plaquette sets. With (RLF-3^dis) it gives
   H-Bal-3T^S and the AF upper bound for the soft plaquette. Lemma KN (kernel tail with the background defect entering
   quadratically, ||W'^{-1}M̄ - 1|| ≤ 3δ²; x3 C max ratio 0.43) shows the kernel adds nothing to the difficulty, and
   removes the linear δ_c loss of RLARGE's Lemma RS (R4) (useful to layer 1). Gaussian instance: holds (layer 1's A2 for
   deterministic averaging). Wall **(W-lc)**: the all-cut SU(N) measure is not a log-concave perturbation of a Gaussian in
   any global chart (compact configuration space, unconstrained crossing plaquettes, no uniform gap of the free Hessian);
   the per-level gap (LINEAR_PACKAGE Prop. 6.4) is for the finer field given the coarser, which is the wrong direction for
   a marginal bound. Progress: the chessboard step removes the localisation problem of §11.4; only an extensive
   statement is now needed.
   **[RX34-fix 7, session 5] Corrected:** the A2 instance is for deterministic averaging; for the soft chain the free
   instance was open at the end of session 4 (settled in session 5, EXISTENCE §14.2). [Moved out of the sentence in
   session 7, RX56-fix 11.]
5. **The existence theorem (soft branch) rests on:** nothing for (a), (b); the kernel for non-flatness; (RLF-3^dis) for
   "not Haar"; (RLF-3^dis) + (PLD^mod_dis) + (F) for the AF upper bound. So it does **not** rest on RLF + (F) only; the
   extra input is one named small-field statement of layer-1 type.
6. **Public statement** (EXISTENCE §12.1) updated conservatively: both block-variable kinds; the kernel-only bound
   labelled as carrying no Yang-Mills content; the two disseminated hypotheses named as unpublished.
7. **End-of-session re-read of RLARGE §1** (it changed: session 18 added §1A). Effects in EXISTENCE §13.9: layer 1 now uses
   the label (RLF-5) for complex fields (not used here); RLF-3 now speaks of defect configurations with n > n_♯ and
   exponent a_♯ (E_all is still one of them); Z_K^{ref} is now defined, which settles half of the normalisation reading.

**Check x3.** PASS (A: block-boundary RP of a soft-blocked clock ring, min/max eigenvalue ≥ -9·10⁻¹⁶; C: Lemma KN core on
SU(2), SU(3)); B1 informational (site-plane RP fails for the normalised kernel); B2 PSD. 3.5 s, 93 MB, nice 10, threads
1, load 3.0, memory free 33%; `python3` without -I (user-site numpy; no external files read).

**Tally** ([RX34-fix 3, session 5]: corrected to 37 / 1 / 3 / 5 / 10, Lemma CBE PROVEN-HERE). PROVEN-HERE 36 / IMPORTED-AND-REVERIFIED 2 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 (H-loc-LF, H-sg,
H-Bal-loc for the deterministic branch; (RLF-3^dis), (PLD^mod_dis) for the soft branch) / OPEN 10. §11 and §13
unreviewed. Snapshot: EXISTENCE_session4_snapshot.md.

**Next.** Independent review of §13 (X-RP^S, Lemma CBE's proof, Theorem CB, CB-sg). Ask layer 1 to state RLF-3 as a
ratio to Z_K^{ref} (makes (RLF-3^dis) a literal instance). (PLD^mod_dis) in the Gaussian soft linear chain via symbols
(the operator-norm bound on the coarse-curvature covariance). The deterministic lower bound via chessboard + a
disseminated one-link statement?

## Session 5 (2026-10-27)

**Brief.** (1) Apply every REVIEW_X3_X4 binding fix, tagged [RX34-fix]. (2) The decisive test, pre-stated: the free
Gaussian (abelian, linear) soft RG chain; does the accumulated kernel noise at fixed physical resolution converge or
diverge as K → ∞; if it diverges, which existence statements fail and is there a repair. (3) Only if (2) passes: a new
route to ker T = 0 for soft variables. P (../ym4d-proof/) read-only; nothing in P edited. No commits, PRs, pushes, CL or
axiom edits.

**Read.** REVIEW_X3_X4.md (all); EXISTENCE.md §0, §4 (X-CONT), §6, §10.2, §11.3-11.4, §12, §13 (by offset); LOG.md
session 4; P/LINEAR_PACKAGE.md §0-§2 (frozen v1, md5 4fbf5342…). No web access.

**Method.** All 12 binding fixes applied first. T11-T13 pre-stated in EXISTENCE §14.0 (22:54 UTC) with explicit
PASS / FAIL / INTERMEDIATE meaning before any derivation; check x4 criteria written before the script.

**Fixes [RX34-fix 1-12].** §0 H-Bal-3T → H-sg, X-IVND' + H-Bal-1 (M-uniform), soft (F) labelled a plausible extension of
H-Bal-1 (layer-1 node A5, OPEN); E_1 := E_bg + 2H_0K_0 and the g-conditions stated on g, not γ; H-sg "reduction" of 3T
labelled nominal; X-RP^S class redefined by continuum supports, the reviewer's L = 3 counterexample recorded; Lemma CBE
relabelled PROVEN-HERE (sources not read); KN's Lemma-RS claim tied to KN-step's re-centred dichotomy (η_1 → c_1ε_1,
A_dη ≤ 1); MIX: D3 "reduced", not "dissolved"; merge table: not Haar needs (F), X-LRP, L9a', D4-norm (2) and smallness
listed; (F) for the soft scheme = layer-1 open item; (RLF-3^dis) "follows under an unadopted reading of RLF-3, plus
RLF-1, RLF-4, node A"; RLF threshold renamed g_RLF; P_cut identification corrected; Gaussian evidence for (PLD^mod_dis)
labelled deterministic-averaging only; kernel-only "not flat" separated from "not Haar" (l.1455, merge text, §12.1);
§12.1 replaced by the reviewer's text word for word; H-cont / H-bl in L² form recorded as FALSE for soft variables
(§4 X-CONT, §13.2, T8a). Tally after fixes 37 / 1 / 3 / 5 / 10.

**Findings.**
1. **T11 PASSES: the kernel noise converges.** By Lemma GS-1 (Q_root^n - Q_str^n is exact, so all gauge-invariant
   content of the soft chain is that of the straight chain) and Lemma GS-2 (n straight steps of white noise: link
   variance (σ²/3)(2s^{-2} + s^{-4}), block-plaquette variance (4σ²/3)(2s^{-2} + s^{-4}), s = L^n, link symbol ≤ σ²s^{-2}),
   Theorem GS: at fixed resolution m the block-plaquette noise variance is N = (4/3)Σ_nσ²_{m+1+n}(2L^{-2n} + L^{-4n})
   (between 4σ'² and 4.35σ̄² at L = 3), the curvature covariance has ||Σ|| ≤ g_0² + 16Σ_nσ²L^{-2n}, loop fluxes are
   bounded; the K-dependence is a tail ≤ 4σ̄²L^{-2(K-m)}/(1 - L^{-2}). **Exact rate: geometric, L^{-2n} per level of
   depth; no log K.** Session 4's log-divergent recursion treated white noise as smooth curvature. The only divergent
   quantity is the gauge-variant root-representative link variance (≥ 0.0020Σσ_i² at L = 3, pure gauge dλ_n; [RX56-fix 5: was 0.0042, from 0.0654 for 0.0453]), invisible to every
   soft generator.
2. **Consequences.** No existence statement fails at the free level; decision 4's soft variables survive the test; no
   repair needed. An unconditioned analogue of (PLD^mod_dis) in the free noncompact abelian soft chain (N² - 1
   independent copies) [RX56-fix 3] (Corollary PLD-G^S: ||Σ_j|| ≤
   σ_*²g_j², σ_*² = β̂(1 + 16L²/((L² - 1)κ_-)), unconditioned law). Under an (F)-type sequence the free soft block law at
   fixed m is asymptotically pure kernel noise (no running in the free model), confirming that soft fluctuation size
   carries no fine-measure information. Compact non-abelian corrections: ARGUED (local mean-zero noise is damped the same
   way; absence of a bias term not proven).
3. **T12: time continuity for soft variables through the OS seminorm.** Theorem X-KER^S: E[θ(F)^*G] = E_μ[θ(F̃)^*G̃] with
   F̃ = E[F | U_0]; ||[F]||²_OS ≤ liminf E_μ|F̃|²; so H-cont^S (lim_{s→0} limsup_K E_μ|E[τ_sF - F | U_0]|² = 0 on a dense set)
   ⇒ 𝒦 = {0}. H-cont^S is not false for the kernel-noise reason (the conditional expectation removes it). Corollary
   X-CONT-G^S: in the free soft chain E|E[f(F_t) - f(F_0) | B_0]|² ≤ Λ²|X|4g_0²w (Gaussian smoothing reduces it to
   X-CONT-G). Interacting case: OPEN.
4. **Public statement.** §12.1 = the reviewer's text. §12.2 records that its clause "no instance … even for free fields"
   is now out of date for the unconditioned free soft chain, and proposes an amended clause for the next review.

**Check x4.** PASS: A (literal S4' contours, dQ_root = dQ_str to 2.6e-14), B (closed forms by position-space adjoints and
exact Fourier alias sums, ≤ 1.1e-12), C (symbol bounds; s²·sup curvature eigenvalue = 12 < 16 for n ≥ 1); D CONVERGES
(N_60 - N_30 = 0; crude bound 16 → 960). 12.3 s, 230 MB, nice 10, threads 1, load 2.0, memory free 42%, numeric lock held.

**Tally.** PROVEN-HERE 40 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 10
(ARGUED 11, uncounted). §14 unreviewed. Snapshot: EXISTENCE_session5_snapshot.md.

**Next.** Independent review of §14 (GS-1/GS-2 constants, Theorem GS (iv), X-KER^S (i)-(iii)). H-cont^S in the
interacting case (doubled chain; H-corr + H-lin analogue). The compact non-abelian noise: prove the absence of a bias
term and the GS-2 damping for the nonlinear injected noise. Ask layer 1 to adopt RLF-3 in ratio form.

## Session 6 (2026-10-27)

**Brief.** (1) Non-abelian soft noise: extend Theorem GS to the compact SU(N) chain; decide whether a bias term exists.
(2) Interacting H-cont^S from named layer-1 hypotheses, or the wall. (3) Review §12.2's proposed clause conservatively;
ASSEMBLY statement with hypothesis list. P (../ym4d-proof/) read-only. No commits, PRs, pushes, CL or axiom edits.

**Read.** EXISTENCE §0, §1, §4 (X-OS, X-CONT), §6, §10.2, §12-§14 (by offset); LOG session 5; REVIEW_X3_X4 §4-§7, binding
fixes, public-statement and strategic verdicts; checks/x4_criteria.md, x4_soft_noise.py (contour code); P/PLD.md (lane E,
session 1: targets only); P/RLARGE.md §0, §1, §1A, §8. FLOW.md and HIST.md, named by P/PLD.md as layer-1 files, were not
present in P when read; both appeared later in the session (FLOW.md: lane C, the flow (F); HIST.md: lane D, (H-pos) and
(HIST)) and were not read; §15.6 names them as owners only. No web access.

**Method.** Targets pre-stated in EXISTENCE §15.0 (23:21 UTC); checks/x5_criteria.md written a few minutes before §15.0
and before any derivation or script. Check x5 run once under the numeric lock; one post-hoc re-run (labelled).

**Findings.**
1. **Exact one-step structure (SU(2)).** The contour mean is r·W with W ∈ SU(2), so the decision-4 kernel is exactly a
   central heat-kernel-type law μ_t (t = κr/g²) translated by W (Lemma NA-1). For a block loop with distinct links,
   V_C = W_C·Ỹ with Ỹ central and inversion-symmetric: characters contract by Πμ̂, the floor is 1 - Πa ≤ Σ3g²/(2κr), and
   the location is exactly W_C (Lemma NA-2). For N ≥ 3 the kernel is non-central at order δ² (ARGUED).
2. **In a flat background (U_0 pure gauge), no additive bias, any N, any depth** [RX56-fix 4] (Proposition NA-3): in a flat background every block holonomy's law is central
   and inversion-symmetric (constant gauge + charge conjugation).
3. **O(σ²) part damped (SU(2), flat background, fixed K)** [RX56-fix 4] (Theorem NA-GS1): the small-noise coefficient of the compact floor is (3/2)N_j, Theorem GS's
   damped sum. Undamped terms are O(σ⁴) and summable under (F). Uniformity in K of the remainder: (NA-R2), OPEN.
   Background-dependent drift: none at injection (exact), no zero-derivative term later (parity, ARGUED); the marginal
   effect is inside (F) (ARGUED).
4. **𝒦^S = {0} unconditionally** (Theorem X-KER^S (iv)): soft generators have open continuum supports [RX34-fix 1], so all
   lie in 𝔄_{++} and X-KER (i) applies. Temporal H-cont^S is not needed. Non-triviality (H^S ≠ CΩ) is untouched (may be
   vacuous: H^S_ω may be CΩ; in the free (F)-type soft chain it is) [RX56-fix 1].
5. **H-cont^S (now: spatial continuity) reduced, not proven.** Proposition H-cont^S-red: K → ∞ first (shared resolution-n
   field), and products of loops reduce to single loops under any coupling of the noise. Wall: (H-corr^S) + (H-lin^S),
   and H-lin^S = NA-R2, so T14 and T15 stop at one estimate. [RX56-fix 6] Overclaim: H-lin^S ⇐ (NA-R2^bg), a
   background-uniform pathwise form of NA-R2 (ARGUED); NA-R2 is a flat-background expectation.
6. **T16.** §12.2's wording rejected (it pairs a conditioned hypothesis with an unconditioned free fact); narrower clause
   proposed; a time-continuity clause proposed for review only. §12.1 unedited. ASSEMBLY: §15.6.

**Check x5.** A PASS (identities to 2e-16; sampler and convolution within 1.2 SE; one kernel location component at -3.8 SE,
inside the 4 SE criterion; post-hoc re-run with three seeds within 1.8 SE). B PASS: one literal S4' step, R(t) → 0.461 (fit)
vs 38/81 = 0.469, R(400) within 2.2%; the fit's χ²/dof = 101 (model inadequate, the PASS rests on the tolerance and on
R(400)); finding: the O(σ⁴) coefficient is not damped at the step that creates it (b ≈ +4.1 from a fit R_∞ + b/t + c/t², χ²/dof 0.16; the two-parameter fit gives 5.6 [RX56-fix 10]; vs b_0 ≈ -15). C as expected:
two steps, R2 = 0.0546 vs 0.0497 linear, ratio 0.1062 vs 0.1059. 289 s, 922 MB peak, nice 10, threads 1, load 2.7, memory
free 42%, numeric lock held.

**Tally.** PROVEN-HERE 46 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 11 (ARGUED
15, uncounted). §15 unreviewed. Snapshot: EXISTENCE_session6_snapshot.md.

**Next.** Independent review of §15 (first X-KER^S (iv): check that no plane-touching soft generator exists in the algebra
on which T(s) acts; then NA-GS1's cross-term step and the parity count). (NA-R2): a depth-uniform weighted-influence
(Efron-Stein-type) bound for the polar averages. Non-triviality of H^S_ω (a connected correlation across the plane).
Ask layer 1 to adopt RLF-3 in ratio form (still open).

## Session 7 (2026-10-28)

**Brief.** (1) Apply every REVIEW_X5_X6 binding fix, tagged [RX56-fix]; tally 46/1/3/5/12 with (H-sig^S) OPEN. (2)
(H-sig^S), non-triviality of the soft OS space: diagnose the free-model degeneracy found by the reviewer ((a)
unrenormalised observables, (b) free model with running-coupling inputs, (c) a genuine soft obstruction); construct the
renormalised algebra; prove (H-sig^S) where possible; relate to X-NTAF and PLD-AF. P (../ym4d-proof/) read-only. No
commits, PRs, pushes, CL or axiom edits.

**Read.** REVIEW_X5_X6.md (all); EXISTENCE §0, §6, §10.1-10.2, §12, §14-§15 (by offset); LOG sessions 4-6;
P/PROOF.md header (S18-S19) and N5 node, P/REVIEW_S18_S19.md bottom line, P/LINEAR_PACKAGE.md Lemma 2.2 (md5
4fbf5342…, unchanged), P/PLD.md §14.0-14.2, §14.8-14.9. No web access.

**Method.** Fixes first (00:14-00:18 UTC). Targets T17-T20 pre-stated in EXISTENCE §16.0 at 00:18 UTC before any
derivation; checks/x6_criteria.md written before checks/x6_sig_free.py (one amendment to C's parameters, recorded in the
file, made before the script existed).

**Fixes [RX56-fix 1-12].** X-KER^S (iv) framing (X-KER (i) for the open-support algebra; continuity on D; real-s
interpolation) and the free rank-one remark; (H-sig^S) added as OPEN (§6, §15.3, §15.6 (I) and "Not delivered", table);
"instance of (PLD^mod_dis)" → "unconditioned analogue … free noncompact abelian … (N² - 1 copies)" (§0, §14.2 title and
two lines, §14.5, LOG); NA-3 "flat background (U_0 pure gauge)" and NA-GS1 "(SU(2), flat background, fixed K)" in header,
§0, §15.2 item 1, §15.6 (I), §15.7, LOG; GS (iv) 0.0453 / 0.00205 ≥ 0.0020 (L = 3), A1 named as imported in GS (ii);
"H-lin^S ≡ NA-R2" → "H-lin^S ⇐ (NA-R2^bg) (ARGUED)" (§6, §15.3 twice, §15.6 table, §15.7, LOG); (NA-R2) restricted to
SU(2) (coefficient 3/2), garbled clause removed; H-cont^S-red n := max(n(a), class levels); ASSEMBLY (I) OS statements
need time side → ∞, "H^S_ω may be CΩ", C-invariance = proof of NA-3; table: (L) proven here, (C) reflection identities
re-derived here with L9a′ imported, D4-norm (2) imported (PROVEN there, not re-verified here), A1 / (R) / (IT) rows added,
N5 OPEN at levels i ≥ 1 (S18 trivial background and S19 level-0 curvature-small backgrounds PROVEN; layer-1 tally 71/2/7/24
+ 1 after S19, confirmed by REVIEW_S18_S19), (F) = self-consistency condition (ARGUED); x5 b ≈ 4.1 (three-term fit,
χ²/dof 0.16, R_∞ = 0.4694 ± 0.0006) and the reviewer's same-M replay (+1.33 SE) recorded; X-CONT-G^S vacuous under
(F)-type couplings; §14.2 heading inserted; LOG l.209-210 annotation moved, LOG l.200 annotated; §12.1 three
replacements word for word, §12.2 retired. Tally after fixes 46 / 1 / 3 / 5 / 12, ARGUED 16.

**Findings.**
1. **(H-sig^S) restated (Lemma SIG-0).** dim H^S_ω > 1 iff some positive-side soft observable has a non-zero connected
   correlation with its mirror image. That correlation is carried by U_0 alone, because the kernel noise does not cross
   the plane. Fixed-scale normalisations (by g_m) are reparametrisations of the same algebra.
2. **Diagnosis: (b), sharpened.** In the free soft chain the decisive parameter is the fine (signal) coupling g_0, not
   the kernel couplings and not κ (Theorem SIG-FREE).
   - (i) If g_0 → 0, then H^S_ω = CΩ. This re-checks and extends the reviewer's computation, with rate O(m/K) under (F).
   - (ii) If liminf g_0 > 0, then dim H^S_ω > 1, with an explicit K-uniform lower bound from one spatial Fourier mode:
     c_* = (4/T³)q sinc⁴(q/2)(∫_{t_b}^{t_b+1}e^{-qτ}dτ)²/2. This holds for every κ, including (F)-type kernel couplings.
   - (a) EXCLUDED: Lemma SIG-1 gives Var E[f | fine] ≤ (2/π)||f||²_∞ g_0²/(c(X)σ²). It is sharp, and no rescaling of
     the observables helps.
   - (c) EXCLUDED at the free level.
   - The reviewer's example violates the lower half of (F)'s self-consistency.
   - **[RX7-fix 3]** The "decisive parameter g_0" finding is free-model only; in SU(N) the bare coupling → 0
     necessarily, and the decisive quantity is the noise-free signal at the observation scale, (H-sig^♭).
     **[RX7-fix 2]** "(a) EXCLUDED" holds only when g_0²/σ² → 0; if σ ∝ g_0, (a) is right (normalisation artefact).
3. **Renormalisation condition (Lemma RC).** The bare coupling can always be fixed by a noise-free reference expectation;
   in the free model this gives a constant coupling, hence a non-trivial OS space. Proposed to layer 1, not adopted.
   **[RX7-fix 5] Proposal withdrawn:** layer 1 already fixes the bare coupling by g_K = g (FLOW F-tune); the
   "proposed reading" misdescribed FLOW.
   ARGUED: a bare coupling whose rate differs from the one-loop β_1 makes g̃_m → 0 (trivial) or strongly coupled; even
   the two-loop log K must be matched.
4. **SEP.** Two-sided one-point AF-type bounds, the PLD analogue and noise convergence all hold in a model with
   H^S_ω = CΩ. So ASSEMBLY (II)-(III)-type statements cannot give non-triviality. PLD-AF is the upper half of the
   self-consistency; (H-sig^♭) is the lower half. **[RX7-fix 7] ARGUED (analogy) only: neither is a half of (F).**
5. **SU(N): Proposition SIG-RED.** |Cov_P(θF^*, F) - Cov_μ(θΦ^*, Φ)| ≤ sd(F - Φ)(sd F + sd Φ). Hence
   (H-sig^S) ⇐ (H-sig^♭) (Wilson half: a cross-plane two-point lower bound for noise-free skeleton block observables,
   renormalised by g_m⁴) + (TRACK) (⇐ (NA-R2^bg), ARGUED). Both are OPEN. No layer-1 hypothesis gives cross-plane lower
   bounds; the named route is a two-sided W-AF2 (ARGUED).

**Check x6.** A PASS: c(r) = 2.8414e-4 → 2.2835e-4 (r = 1..4) → c_∞ = 2.2828e-4, with error ∝ L^{-2r}; the FFT route agrees to
   4e-15; the single-mode value = the closed form c_*. B PASS: max ratio 0.9999 (the bound is sharp); c(X) > 0 and
   Bianchi dim 5. C INCONCLUSIVE: the MC agrees (z = +0.45, +0.28), but C1's effect is 2.4 SE < 5 (pre-registered); the
   script line "OVERALL: FAIL" implements that rule. Post-hoc (labelled): ψ-free linear covariance 2.97e-4 ± 0.48e-4 vs
   2.84e-4 (z = +0.26, 6.2 SE). D: (F)-type sup Q ∝ 1/K. Runs: 576 s, 412 MB peak; post-hoc 280 s. nice 10, threads 1,
   load ≤ 4.5, memory free 45%, my lock only, released once each; `python3` without -I.

**Tally.** PROVEN-HERE 49 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12 (ARGUED
19, uncounted). After the fixes alone: 46 / 1 / 3 / 5 / 12. §16 unreviewed. Snapshot: EXISTENCE_session7_snapshot.md.
Session-6 tally line above: corrected to OPEN 12 [RX56-fix 2].

**Next.** (H-sig^♭) for SU(N): a K-uniform two-point lower bound for noise-free block observables across the plane;
the most direct route named is a two-sided W-AF2 at fixed separation (ARGUED). ~~Propose (RC) to layer 1 (bare coupling
fixed by a renormalisation condition, (F) for the kernel couplings).~~ [RX7-fix 5: dropped] (TRACK) together with (NA-R2^bg) / P's (NH-iii) as one
item. Independent review of §16 (Lemma SIG-1's constants, Theorem SIG-FREE (ii)'s single-mode limit, SIG-RED).

## Session 8 (2026-10-28)

**Brief.** (1) Apply the 12 REVIEW_X7 binding fixes, tagged [RX7-fix]; tally 49/1/3/5/12, ARGUED 20. (2) Test the lead's
route to non-triviality: (H-sig^♭) / (H-sig^S) from layer 1's output at the physical scale (F-tune: g_K = g; RLF;
(I_k^E); small-field package at level K - m_*), by a weak-coupling expansion at fixed g; state consumed outputs as
"given H"; decide survival of K → ∞; relate to REVIEW_X7's known-hard remark. P (../ym4d-proof/) read-only. No commits,
PRs, pushes, CL or axiom edits. Mid-session (coordinator): RLARGE v2 installed; answer K8 ((RLF-3^dis) against v2's Z_K^{sf}
form), K9 (anisotropic tori, two shifts), and cite layer-1 outputs by v2 names.

**Read.** REVIEW_X7.md (all); EXISTENCE §0, §6, §12, §15.6-§16 (by offset), §13.4-§13.5, §13.9, X-S4c; LOG session 7;
P/FLOW.md §0-§1, §4, §7-§10; P/RLARGE.md v1 §0, §1, §1A, §8.2, then v2 §0, §1.1-§1.3, §4.1-§4.2, §8; P/HIST.md §14.0-§14.2;
P/PROOF.md Theorem CE (L5 [S10]) and the S19-S20 entries by grep. No web access.

**Method and timestamps (UTC).** Fixes 01:06-01:18. §17.0 targets written 01:19:39 (after the fixes and after exploratory
reasoning; before any written derivation or script). checks/x7_criteria.md written next; its mtime:
`stat`: 2026-10-27 21:20:04 EDT (= 01:20:04 UTC). x7 script written after the criteria. Lock acquired 01:22:02; a
reduced-size smoke run (scratchpad copy, ~9 s) preceded the full run; full run started immediately after, same lock.
Derivations §17.1-§17.6 written 01:23-01:26 while x7 ran; §17.8 (K8/K9) 01:27-01:29 after the coordinator's note; the
(O3) citations in §17.2 were re-based on v2 names then (v1 (PLD)_k withdrawn as an input).

**Fixes [RX7-fix 1-12].** (1) c_* → 0 as T_m → ∞; full mode sum → continuum; SIG-FREE (ii) bound is fixed-torus. (2) "(a)
EXCLUDED" restricted to g_0²/σ² → 0, σ ∝ g_0 counter-case added (normalisation artefact; invariant g_0/σ) in §0, SIG-1
reading, §16.3 (a), §16.6 T17, LOG. (3) free-model-only qualifier in §0, §16.3 (b), §16.6, LOG finding 2. (4) "free model:
(RC) ⇒ liminf g_0 > 0; SU(N): AF, nothing bounds it below" at §6 and §16.4 item 4. (5) "proposed reading" withdrawn and
replaced by REVIEW_X7's text; P/PLD (W-F3) credited; LOG Next item struck. (6) Lemma RC: X-S4c (i) global continuity
cited; uniqueness and g_0^{RC} ∈ (0, γ] not given. (7) two-halves reading ARGUED (analogy) at §16.4 item 2, table row (F),
§16.6 T20, LOG finding 4; ARGUED 20. (8) TRACK fails in REVIEW_X5_X6's example (estimate holds, s_0 = 0); SIG-RED lossy
(κ ≥ κ_0(F)); §0 too. (9) (H-sig^♭_ren): g_m := FLOW's tuned effective sequence. (10) SEP "model-independently";
product-measure remark added. (11) SIG-0 (iv) noncompact; SIG-FREE (i) "(curvature algebra)"; §0 "liminf_j g_0(K_j) = 0".
(12) l.1376 annotated; header (l.9) annotated. Tally after fixes: 49 / 1 / 3 / 5 / 12, ARGUED 20.

**Findings.**
1. **The soft variables at a fixed level are the effective-action field (Lemma NT-0).** The law of U_j under the chain is
   e^{-S_j}/Z exactly, so (H-sig^S) at level j is a two-point lower bound for layer 1's output law. (TRACK) does not arise;
   the right target for layer-1 output is (H-sig^S) directly, not (H-sig^♭) (which is about the noise-free skeleton of U_0).
2. **Orders corrected.** For SU(N) gauge-invariant observables **with contractible support** [RX8-fix 1] the leading
   cross-plane connected term is O(g_j⁴) (two-gluon exchange; ARGUED, a Laplace statement [RX8-fix 1]), not O(g²); the O(g³)
   remainder is not established (zero-mode sector). Wrapping observables (spatial Polyakov loops) have O(1) connected
   correlation through the toron moduli [RX8-fix 1]; "O(g²) only for abelian models" concerns the linear term only.
3. **Theorem NT-red (PROVEN-HERE | (O1)-(O3), (WC)).** On a fixed hypercubic physical torus, (H-sig^S) holds along the full
   sequence K → ∞ (dim H^S_ω > 1 for every limit state of the finite-torus OS construction), given (O1) the F-tune
   bracket for u_{K-m_*} (v2 #1), (O2) the (I_j^E) density on the all-small-field event (v2 #4), (O3) large fields with
   probability o(g⁴) (⇐ v2 (RLF-3) + HIST-sum + three-way price, ARGUED), and **(WC)**, a K-free lower bound for a class of
   finite-dimensional weak-coupling gauge integrals. Parts: large-field removal (6p||F||²), sector inequality (for a θ-invariant sector
   variable b, Cov ≥ E[Cov | b]), and ~~necessity (failure ⟺ a product limit
   law across the plane, by compactness)~~ [RX8-fix 3] one direction: (H-sig^S) ⇒ no product limit point; "dim H_ω > 1 ∀ω"
   ⟺ no product limit point; the converse to (H-sig^S) only if (ν_{K,j}) converges. Uniformity in K enters only through
   membership in the class. [RX8-fix 4] NT-red meets T21's second branch only: (WC) is itself a class-uniform two-point
   lower bound containing every ν_s. [RX8-fix 2] ν_s := law(U_j | A), A = {U_j all small-field} ∩ {𝔥_{≤j} = ∅} a
   joint-chain event; (O2)'s display is e^{-S_j}|_∅.
4. **Lemma NT-G.** The Gaussian part u_jH_j of the level-j output is exactly the free soft chain at constant coupling g_j
   and constant noise 1/(κu_j); SIG-FREE (ii) gives its K-uniform cross-plane bound. This is where the free model properly
   enters (REVIEW_X7: free g_0 ↔ g_m). Leading term only.
5. **(WC) is not a Gaussian computation and not a Theorem-CE cluster expansion.** Theorem CE needs a product measure and
   activities ≤ c_0(κ)e^{-κd}, κ > 457; the level-j field's Gaussian is massless (constant modes; power-law curvature
   covariance), and N5/RW/NAH1 concern the massive fluctuation operator of one step. On the fixed torus (WC) is a
   finite-dimensional Laplace analysis on a singular critical set: the toron moduli (commuting holonomies, dimension
   4(N - 1)) with quartic constant modes at ~~reducible points~~ the singular strata [RX8-fix 10]. Named: (WC-tor) OPEN;
   (SF-bg^tor) OPEN: ~~layer 1's (SF-bg) is stated near the trivial field only, so (O2) on all of 𝒮_j needs it at flat
   non-trivial backgrounds (a global form of HIST GAP S2-1 on a torus; reported for layer 1)~~ [RX8-fix 6] narrowed against
   HIST §20.3 (C) (I_j^E)': items (a3)-(a4) and (SF-∞) at flat non-trivial backgrounds on wrapping charts/polymers
   (contractible charts covered by (a4)'s local form). [RX8-fix 10] "massless" → CE's product/decay hypotheses unmet +
   the zero-mode/moduli set. [RX8-fix 5] (WC) is not K-free: depth-uniform inputs (a) Hessian at flat backgrounds, (b)
   CLS-cone ⇐ (AE) OPEN, (c) C³-C⁴ bounds. ARGUED: the leading coefficient is ≥ ½(N - 1)c_*²u^{-2} in every toron
   sector (Cartan components untwisted; all Wick terms ≥ 0).
6. **K → ∞ (T23).** Survives on the fixed torus (given the above). Time side → ∞ or infinite volume: NOT supplied: needs
   (WC_∞), an infrared statement (zero-spatial-momentum quantum mechanics uniformly in the time extent; the mass-gap part).
7. **T24.** Hard parts: (1) producing layer-1 output, which is more than Balaban's published Z bounds ((O2) is a density
   statement with K-uniform constants), and (3) the infrared (WC_∞). The finite-volume step (2) = (WC) is K-free and
   finite-dimensional but not done. So "(H-sig^♭) known-hard" stands as stated (it contains (1)); "given layer-1 output,
   this step is not the hard part" is ARGUED, with (WC) still to prove. Not a corollary of layer-1 output yet.
8. **K8.** (RLF-3^dis)_v2 restated (quantifier: chain's own sequence, (F_R), hypercubic tori). It is a literal instance of
   v2 (RLF-3) + (RLF-4) iff the history sum Σ_𝔥Z(𝔥) and Z_K^{sf} carry the same vacuum c-number (equivalently Z(𝔥)
   decompose Z_K^{ren}); read literally ~~(Z_K = ΣZ(𝔥), vacuum included, bounded by Z_K^{sf}) the ratio carries e^{𝒱^{LF}},
   K-divergent, and the instance fails~~ [RX8-fix 7] the instance fails by the sign: HIST-sum Z_K ≤ Z^{sf}e^{…} with (RLF-1),
   (RLF-4) forces 𝒱^{LF} ≤ O(|T|), so a K-divergent 𝒱^{LF} goes to -∞, which defeats Z(∅) ≥ e^{-E_∅|T|}Z^{sf}. Requested of v2: state which. Also needs HIST-sum's restricted-sum factorisation
   (ARGUED). v2's e^{B_0} per cube per level is absorbed into C_d.
9. **K9.** NT-red and the RLF consumers (ASSEMBLY (II)-(III), X-IVND^S, CB-sg) are taken on hypercubic tori (ES1 restricted
   to ℓ_0 = ℓ for RLF-consuming statements); nothing beyond v2 is needed for them. ASSEMBLY (I) (time side → ∞) consumes
   no RLF. Any future anisotropic use ((WC_∞)) needs (K9-req): two per-level shifts δβ^{el}, δβ^{mag} with v2's bounds
   uniformly in the time side, or confirmation that v2's counterterms are infinite-volume numbers with anisotropy only at
   the wrap levels.

**Check x7.** A PASS (formula vs dense 2.5e-16; projector identities exact; leading coefficient 3.53-3.66e-6 across 256
SU(2) toron sectors, < 4% variation; LB 1.18e-6, UB 3.86e-6). B INCONCLUSIVE under the pre-registered rule: R = C(1)/g⁴ =
4.87, 3.41, 2.83 (·1e-6, ± 0.9, 0.8, 0.7) at β = 8, 16, 32, all inside [0.5LB, 1.5UB] and within ~1 SE of the leading
coefficient, but 4.5 and 4.1 SE < 5 at β = 16, 32 (under-powered by ≈ 1.5× in samples; the smoke run hinted it; criteria not
changed). B0 PASS (⟨s⟩β = 0.754 at β = 32). 695 s wall, 247 MB peak, nice 10, threads 1, load 6.45 at start (< 8), my lock
only (acquired 01:22:02, released once 01:34:37), `python3` without -I.

**Tally.** PROVEN-HERE 50 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12 (ARGUED
24, uncounted). After the fixes alone: 49 / 1 / 3 / 5 / 12, ARGUED 20. §17 unreviewed. Snapshot:
EXISTENCE_session8_snapshot.md.

**Next.** (WC-tor): the sector-wise Laplace lower bound on a fixed torus, first for SU(2) and the Wilson action (depth 0,
no polymers: the simplest class member), handling the reducible point by the sector inequality; then the class
uniformity in the depth and the polymers (Cauchy bounds). Report (SF-bg^tor) to layer 1 (the (O2) domain at flat
non-trivial backgrounds). Ask v2 for the K8 normalisation (does Σ_𝔥Z(𝔥) decompose Z_K or Z_K^{ren}?) and K9 (one shift
with wrap-level anisotropy, or two shifts). A better-powered x7 B (≥ 2× samples, criteria re-registered) if B is to count.
Independent review of §17.

## Session 9 (2026-10-28)

**Brief.** (1) Apply the 12 REVIEW_X8 binding fixes, tagged [RX8-fix]; tally 50/1/3/5/12, ARGUED 25. (2) Fixed-torus
non-triviality by the cheaper routes: (a) spatial Polyakov loops (prove a K-uniform lower bound given layer-1 output, v2
names), (b) 't Hooft-twisted spatial boundary conditions; physical-box caveat. (3) State (WC_∞) precisely (no mass-gap
attempt). P read-only; no commits, PRs, pushes, CL or axiom edits.

**Read.** REVIEW_X8.md (all); EXISTENCE §0, §15.3, §15.6, §16.1-§16.2, §17 (all); LOG session 8; P/HIST.md §14.1, §20.3 (A)-(C),
§25.5-§25.6; P/RLARGE.md v2 §0, §1.2-§1.3, §3, §4.1-§4.2; P/PROOF.md S1-S4' (l.520-560). No web access.

**Method and timestamps (UTC).** Fixes 02:10-02:24. §18.0 targets written 02:24 (after the fixes and after exploratory
reasoning on the Polyakov route; before any written derivation or x8 file). checks/x8_criteria.md next, then the x8
script; x8 waited for the numeric lock (held by another process from 02:08 local-lock mtime). Derivations §18.1-§18.7
written 02:27-02:35 while waiting.

**Fixes [RX8-fix 1-12].** (1) O(g⁴) restricted to contractible supports, ARGUED; Polyakov O(1) counter-case; linear-term-
only reading of the abelian remark (§17.1, §17.5, §0, LOG f2). (2) ν_s := law(U_j | A), A a joint-chain event; (O2)'s
display e^{-S_j}|_∅; covariance of the history construction stated. (3) NT-cpt one direction; "dim H > 1 ∀ω ⟺ no product
limit point"; converse under convergence; §15.3 "equivalently" → "which implies". (4) T21 decided under branch 2 only.
(5) (WC)'s depth inputs (a) Hessian at flat backgrounds, (b) CLS-cone ⇐ (AE), (c) C³-C⁴; "no K" → "no measure-theoretic UV
limit; depth via 𝓔_k"; t_b defined; θ/gauge invariance of E. (6) (O2) re-cited as (I_j^E)' (HIST §20.3 (C)); (SF-bg^tor)
narrowed to (a3)-(a4) + (SF-∞) at flat backgrounds on wrapping charts/polymers. (7) K8 sign argument. (8) (O3) constants
e^{E_∅|T|}, e^{(n_♯+1)a_♯R}. (9) small-coupling fixed torus = small physical box (NT-red, T23). (10) "massless" → CE's
product/decay hypotheses + zero-mode set; "reducible points" → singular strata. (11) T24: (WC) consumes CLS-cone ⇐ (AE).
(12) "fixed resolution"; K9 "(RLARGE)"; §17 subsections re-ordered; §0 "for some limit point". Tally after fixes:
50 / 1 / 3 / 5 / 12, ARGUED 25.

**Findings.**
1. **Lemma CTR (exact).** The soft chain is invariant under the spatial centre transformations (multiply the links
   crossing a block-boundary hyperplane H_μ by z ∈ Z_N at every level): the Wilson action, Haar measure and every kernel
   (each S4' transporter of a crossing coarse link crosses H_μ exactly once) are invariant. So charged Polyakov traces
   have mean 0 under ν_{K,j}, for every K and any time side.
2. **POL-det.** SU(2): (½trW_1)² + (½trW_2)² + (½trW_1W_2)² ≥ 3/4 - ||1 - [W_1, W_2]||; SU(N): a finite charged family whose
   traces cannot all be small on near-commuting triples (compactness; a Z_N³-invariant N-atom measure on 𝕋³ is impossible).
   Lattice Stokes bounds the commutator by the 2-torus plaquettes and slice-to-slice changes by ribbon plaquettes.
3. **Theorem NT-pol.** Cov_{P_K}(θF_2, F_2) ≥ 3/4 - (n_s² + 4n_sd_t)η^{1/2}, η = max one-point E||1 - U_p||²; with Lemma SMALL
   (η ≤ η_*(g) → 0 K-uniformly | (O1), (O2)', (O3), CLS-cone ⇐ (AE), (a3-q)) this gives ≥ 3/8 and dim H^S_ω > 1 on a fixed
   hypercubic torus. No moduli density, no two-point input. Corollary NT-pol^OS: the same at a fixed spatial torus with
   time side → ∞ | ASSEMBLY (III)'s inputs + (K9-req): the literal (H-sig^S) holds there for SU(2), via a wrapping
   observable.
4. **Caveat (binding).** Coupling exponentially small in the box volume (e^{2E_0N_c} in Lemma SMALL), or g p(g) ≲ 1/n_s²:
   box ≪ Λ^{-1}; the signal is the holonomy/centre zero-mode sector. (H-sig^S) is re-scoped to contractible supports,
   (H-sig^S_loc); OPEN count unchanged.
5. **Twisted route (ARGUED).** A (1,2) 't Hooft twist leaves N² isolated flat points with centre stabiliser; (WC) becomes a
   non-degenerate Laplace problem (WC-tw); every periodic-torus layer-1 statement must be re-checked on twisted tori.
6. **(WC_∞), (WC_∞^sp) stated.** Box-uniform lower bounds on a local two-point function at fixed separation (and on its
   drop between two separations). **[RX9-fix 1, session 10]** As written in session 9 the constants were g-uniform, which is wrong
   (local connected correlations → 0 like g⁴); re-quantified in §18.7 to one coupling g with c(g) > 0 (family form ∝ g⁴),
   and iterated vs joint limit points distinguished. Proposition SP: dim H > 1 can be pure vacuum degeneracy; clustering makes the forms
   equivalent; a gap is an upper bound, not needed; existence of limit points needs no IR input. Fixed-volume (WC) does
   not transfer without (FS), which needs control up to box size ≍ Λ^{-1} (ARGUED); (WC^bg) is a candidate localisation
   with a named obstacle (θ-invariant coarse σ-algebra).

**Check x8.** A1 PASS (min 0.75 exactly); A2 PASS (10⁶ pairs, 0 violations, min slack 1.4e-5); A3 PASS (190 configs, 0
violations); A4 info (SU(3) minima 4.444 and 0.4587 > 0). B0, B1 PASS: X(1) = 1.35 ± 0.02, 1.80 ± 0.04, 2.17 ± 0.05 at
β = 8, 16, 32 (8 × 4³), no decay with separation; centre-sector sticking visible in E f_n, irrelevant for the centre-neutral
X(d); theorem bound vacuous at these β, as predicted. 308 s, 576 MB, nice 10, threads 1, load 3.83, lock acquired 02:44:37,
released once 02:49:45, `python3` without -I. Non-load-bearing.

**Tally.** PROVEN-HERE 52 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12 (ARGUED
28, uncounted). After the fixes alone: 50 / 1 / 3 / 5 / 12, ARGUED 25. §18 unreviewed. Snapshot:
EXISTENCE_session9_snapshot.md.

**Next.** Independent review of §18 (CTR's crossing count, POL-det (ii), Lemma SMALL's use of CLS-cone/(a3-q) on the torus,
the re-scoping of (H-sig^S)). For layer 1: (SF-bg^tor) (narrowed), K8 normalisation, K9 (one or two shifts), and whether
twisted tori are wanted. The meaningful open targets are (H-sig^S_loc) and (WC_∞^sp); per REVIEW_X8, further fixed-torus
results are not progress toward continuum non-triviality.

## Session 10 (2026-10-28)

**Brief.** (1) Apply the 10 REVIEW_X9 binding fixes, tagged [RX9-fix]; tally 52/1/3/5/12, ARGUED 29 (28 if the
independence claim is dropped). (2) Test the lead's route to (WC_∞^sp): non-vacuum spectral weight from a non-constant
short-time correlation at order g⁴, volume-uniform because local; state what of layer 1 is consumed; prove or name the
missing step; say whether it gives a non-trivial infinite-volume theory. P read-only; no commits, PRs, pushes, CL or axiom
edits.

**Read.** REVIEW_X9.md (all); EXISTENCE §0, §15.6 ASSEMBLY, §17 (all), §18 (all), §13.4 (Theorem CB, X-IVND^S); LOG session
9. No web access.

**Method and timestamps (UTC).** Fixes 03:36-03:43. §19.0 targets 03:44 (after the fixes and exploratory reasoning;
before any derivation or x9 file). checks/x9_criteria.md ~~~03:46~~ 03:45:30 (mtime) [RX10-fix 11], then the x9 script
(03:46:05). x9 waited 03:46:29-03:52:29 for the lock (another holder). Derivations §19.1-§19.5 written 03:45-03:50 (begun
at about the minute of the criteria file, partly while waiting); §19.6-§19.8 after the run, 03:53.

**Fixes [RX9-fix 1-10].** (1) (WC_∞), (WC_∞^sp) re-quantified: one coupling g with c(g) > 0 (family form ∝ g⁴); the
g-uniform form is struck as wrong; minimal IR statement in the one-g form; §0 and LOG finding 6 annotated. (2) Iterated vs
joint limit points defined; consequences stated for iterated limit points, joint form named. (3) RP plane: C_F(s_1) =
⟨θ(G), G⟩ with G = τ_{s_1/2}F, RP in Π_0. (4) The independence claim is deleted (not counted); gap + uniqueness + (WC_∞) ⇒
(WC_∞^sp) needs the gap uniform over limit points. (5) Caveat: "must be exponentially small" becomes the theorem's
sufficient condition (an artefact of e^{2E_0N_c}); intrinsically the box is ≪ the confinement length (§18.4, §18.9, §0);
ASSEMBLY carries the mechanism (holonomy/electric-flux zero-mode sector). (6) NT-pol^OS uses g_+ := sup_{K ≥ K_0}g^S_{m_*}(K).
(7) CTR: the floor-type (unshifted) block convention; levels ≤ j, proper blocks. (8) SMALL: the torus term-set reading of
(a3-q) is tagged for layer-1 confirmation (§19.8 item 2); 8u^{-1/2} noted as conservative; N_c = n_s⁴ level-j unit cubes.
(9) SP (iii): RP, θ- and τ-invariant states. (10) "K-free" → "depth-uniform" (§17.3 title, ASSEMBLY table); SU(N) "Re" in
NT-pol^abs; e^{u/β_1} → e^{u/(2β_0)}. Tally after the fixes: 52 / 1 / 3 / 5 / 12, ARGUED 28.

**Findings.**
1. **Lemma DIFF (exact).** C_F(0) - 2C_F(h) + C_F(2h) = Cov(θ(D)^*, D) with D = F - τ_hF: an OS norm at every finite volume,
   whose limit is ∫(1 - e^{-hλ})²dσ_F. It is blind to vacuum degeneracy and bounds σ_F((0, ∞)) and the drop from below. A
   box- and K-uniform lower bound on it gives (WC_∞^sp) and (WC_∞) for iterated **and** joint limit points.
2. **Lemma LO-D.** The order-g⁴ (Gaussian) second difference is 2c_N²(N² - 1)∫∫(1 - e^{-h(λ+μ)})²dρdρ, strictly positive in
   infinite volume (decay of the free curvature correlator); x9: A(1,1) = 2.25e-3 (95% of C(1)), A(3,1) = 2.21e-6, one colour,
   box-converged.
3. **The lead's step as stated is not supplied.** "Local ⇒ volume-uniform" is not an estimate: (O2) is global (its
   infinite-volume small-field event has probability → 0); on small fields the level-j measure is a massless lattice gauge
   theory in the whole volume; short times do not localise the measure. The missing estimate is (WC_∞^Δ) itself.
4. **Theorem SPEC-red (repair).** Condition on the level-j' soft field (j' = j + n, n ≍ log(1/g), still weak coupling) and
   bound the coarse-mediated term **in absolute value** by Var(E[D | 𝔅]) (no θ-invariance needed: this removes session 9's
   (WC^bg) obstacle). Then | (LF-loc) (⇐ Theorem CB + (RLF-3^dis) + (F)) and the new **(CE-cond)** ((a) conditional covariance
   ≥ (1 - r)g⁴A_* - e(R); (b) oscillation of the conditional mean over small-field coarse backgrounds; e(R) decoupling),
   σ_F((0, ∞)) ≥ u_+^{-2}A_*/2 at every infinite-volume limit point along hypercubic tori. No IR input, no gap, no (O2)/(O3).
5. **(CE-cond) is UV-type (ARGUED).** Couplings g_j…g_{j'} only; conditional problem pinned by the kernels (massive, no
   zero modes); (b) small by dimension counting (L^{-4n}); e(R) is a Balaban-type localisation. Not stated by layer 1 (needs
   sources and a prescribed endpoint). Named failure points listed (§19.5). The T24 attribution is revised: spectral
   non-triviality is UV-type given (CE-cond); the gap stays infrared.
6. **What it gives (conditional).** ~~Not the trivial theory,~~ **[RX10-fix 7]** not the vacuum-only (dim H = 1) theory
   (Gaussianity of the limit is not excluded), not vacuum-degeneracy-only, weight at finite energies. **Not**
   non-Gaussianity (free gluons satisfy the same bound), not a gap.

**Check x9.** A0-A3 PASS (dense vs momentum 9.7e-17; G > 0; A > 0 at all (d, h, T); box convergence 8e-6, 2e-4). A4 info:
log-convex; decay exponent -4.41. B info: exact split (identity 4e-19); coarse-mediated term/C(1) = 4e-4, 1e-6, 1e-9 at ℓ = 4, 8,
16; for the second difference it is not sign-definite and ≤ 2e-6 relative; the registered exponent window for V_l missed
(-4.91 vs [-4.5, -3.5]): "not consistent" as registered (decay faster than the dimension count; coarse Riemann sum at ℓ = 16).
Lock 03:52:29-03:52:30, released once; nice 10; threads 1; load 4.10; 43% memory free; 129 MB. Load-bearing: the explicit
A values only.

**Tally.** PROVEN-HERE 53 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 6 / OPEN 12 (ARGUED
31, uncounted). After the fixes alone: 52 / 1 / 3 / 5 / 12, ARGUED 28. §19 unreviewed. Snapshot: EXISTENCE_session10_snapshot.md.

**Next.** Independent hostile review of §19, aimed at Theorem SPEC-red's split and at whether (CE-cond) is really UV-type
(§19.5 failure points (i)-(iii)). Report §19.8's five items to layer 1, with (CE-cond) as the new request. If (CE-cond)
stands, the next step is non-Gaussianity by the same conditional route ~~(a connected four-point bound)~~ **[RX10-fix 8]**
(a quantity that vanishes for every Gaussian, e.g. an odd f^{abc}-carrying curvature cumulant, or a two-sided O(g⁶)
running statement; a connected four-point bound on Φ is not a test, since Φ's cumulants are non-zero for free fields), not
further fixed-torus work.

## Session 11 (2026-10-28)

**Brief.** (1) Apply the 11 REVIEW_X10 binding fixes, tagged [RX10-fix]; tally 53/1/3/6/12, ARGUED 31 or 32. (2) Restate
(CE-cond) with a mean-square (b) so that n = O(1); handle the no-RP-after-conditioning point without Theorem CB; test
whether lane F's Theorem CE-exp (SF.md) supplies it. (3) A genuine non-Gaussianity statement (odd f^{abc} cumulant or a
two-sided O(g⁶) running statement). P read-only; no commits, PRs, pushes, CL or axiom edits.

**Read.** REVIEW_X10.md (all); EXISTENCE §18.7, §19 (all), §17 conventions/(O1), §13.4 (Theorem CB, (RLF-3^dis)); LOG
session 10; ../ym4d-proof/SF.md §0-§1, SF-cut, SF-A2^0, §6.1, §7.1 (LOC-s, HULL, CE-exp, CE-exp-𝒞, CE-exp^0, CE-exp^k, (CE-Q));
../ym4d-proof/PROOF.md Theorem CE (l.1857-1960). No web access.

**Method and timestamps (UTC).** Fixes 04:24-04:27. §20.0 targets 04:27 (after the fixes and unwritten exploratory
reasoning, which included a by-hand Wick evaluation for i.i.d. links; before any §20 derivation or x10 file).
checks/x10_criteria.md 04:27:55 (mtime). Script written next; x10 waited 04:29:23-04:31:03 for another lock holder, ran
04:31:03-04:33:17. §20.1-§20.3 appended 04:34 (drafted before; the SU(2) A lines of x10 were read at 04:32:48; no §20.1-§20.3
statement uses an x10 number); §20.4-§20.7 after the run, 04:35-04:37.

**Fixes [RX10-fix 1-11].** (1) (CE-cond) stated at one pair (g, n(g)), circular g ≤ g_c(n) removed. (2) m_* ≥ n stated;
u_{j'} ≥ g^{-2} + β_-(m_* - n)log L - R_O. (3) e(R) := C_ee^{-m_eR}, with R_0(g) and the compatibility check. (4) a_± :=
u_∓^{-2}A_* in the conditions; CB's exponent written a_d, (O1)'s constant R_O. (5) Lemma DIFF (ii) narrowed to T_0 → ∞ limit
points; fixed-torus thermal OS remark. (6) §19.5 failure point (iv) added (no RP after conditioning); "coercivity" sentence
marked an assertion; (ii)+(iii) ranked binding (NAH-ind 10⁻⁴⁰/level). (7) "not the trivial theory" → "not the vacuum-only
(dim H = 1) theory; Gaussianity not excluded" (§19.7, §0, LOG finding 6). (8) LOG Next: four-point bound replaced. (9) family
form "stronger, implies the one-g form"; joint-form scope K_n ≥ K_0(·). (10) §19.3 rate replaced by extensivity. (11)
SPEC-red header; 95% = (1 - e^{-hλ})² factor; B identity tautological; T = 128/256 exponents credited to REVIEW_X10; times
harmonised; β_0 := 11N/(48π²). Tally after the fixes: 53 / 1 / 3 / 6 / 12, ARGUED 31.

**Findings.**
1. **Lemma MIX-cond.** Conditional large fields need no estimate on the conditional law: with q := P(B_N | 𝔅), Cov(·|𝔅) ≥
   (1 - q)Cov_{μ^s} - 20M²q, and {q ≤ η} is 𝔅-measurable with P(q > η) ≤ P(B_N)/η, P(B_N) from Theorem CB on the RP law.
2. **Theorem SPEC-red^ms.** | (CE-cond^ms) ((a^s) conditional covariance ≥ (1 - r)g⁴A_* - β_ag²Q_w - e; (b^q) |conditional
   mean| ≤ β_bQ_w + e, Q_w a weighted sum of ||1 - V_p||²), (MOM_4) (E||1 - U_{j'}(p)||⁴ ≤ C_4g⁴), (LF-loc)^ε: Cov(θD_h, D_h) ≥
   a/2, hence σ_F((0, ∞)) ≥ u_+^{-2}A_*/2 at every infinite-volume limit point. n is fixed before g by the g-free condition
   (K); the threshold ε is fixed and contains the typical field. n = 1 is one stage-j integrand (Lemma MK). n = O(1)
   ARGUED (β ≍ L^{-4n}); n_0 = 1 undecided.
3. **Lane F's CE-exp does not supply it.** Lemma CE-cov (proven, with CE-par): in a CE-exp representation the interaction
   moves a source covariance by ≤ 64K_0C_1c_0s_1s_2h_0/h_*³ (relative O(g)). Missing: (M1) **(CE-loc)** [~~binding: CE-exp
   expands the global cut-good event, probability → 0 in infinite volume; (CE-Q) OPEN; 𝔑(α_*) is whole-torus~~
   **[RX11-fix 2-3, session 12] co-binding with (M2); Theorem CE-Q (band) PROVEN in SF session 3 but conditioned on the
   global 𝔇^c (P(𝔇) extensive); (CE-Q^∞) OPEN; owners SF + RLARGE §3.2 (ii), (iii)**], (M2)
   level-uniform CE-exp^j **[carries (L-loc)_j, B-NA wall; (L-hol) withdrawn by SF]**, (M3) (A-cond), (M4) (BG-reg), (M5) (MOM_4).
4. **Lemma PO (correction to the brief and REVIEW_X10 (7)(a)).** The odd f^{abc} corner cumulant E tr(Y_12[Y_23, Y_31]) is
   ¾N(N² - 1)σ⁴ + O(σ⁶) for i.i.d. centred Gaussian links (path ordering in the plaquette logs), and 0.008268·N(N² - 1)σ⁴ for
   the Feynman-gauge Maxwell covariance: it does **not** vanish for every Gaussian gauge field. It vanishes for every
   sign-symmetric (abelianised) law (Lemma NG-wit).
5. **Theorem NG-red.** A level recursion (contraction ≍ L^{-6n}, n = O(1), m_* ≍ log(1/g)) avoids bounding the classical
   cubic term (≍ L^{-6n}g³ ≫ g⁴): | (CE-cond^3), (MOM_4), (LF-loc)^ε, (O1), every limit point has |ω(O)| ≥ u_+^{-2}|c(t_0)|/2.
   This excludes abelianised limits, **not** ~~Gaussian-connection~~ Feynman-gauge Gaussian-connection limits:
   non-Gaussianity in the constructive sense is not established; (NG-conn) named OPEN **[RX11-fix 1, 8, session 12: the
   one-point conclusion does not exclude dim H = 1; (NG-conn) re-posed with a named gauge (§21.2)]**.

**Check x10.** A1 PASS (c_4 = 4.497 ± 0.022 vs 4.5; 18.14 ± 0.08 vs 18), A2 PASS, B0 PASS (exact), C PASS (linearised
control 0 within 1.7 SE); B info: Feynman-gauge c_4 = 0.008268·N(N² - 1), box-converged. Lock 04:31:03-04:33:17, released
once; nice 10; threads 1; load 5.14; 43% memory free; 134 s; 267 MB. Load-bearing: A1, A2 (C control).

**Tally.** PROVEN-HERE 57 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 8 / OPEN 12 (ARGUED
35, uncounted). After the fixes alone: 53 / 1 / 3 / 6 / 12, ARGUED 31. §20 unreviewed. Snapshot:
EXISTENCE_session11_snapshot.md.

**Next.** Independent hostile review of §20 (MIX-cond's use; SPEC-red^ms constants; CE-par/CE-cov; Lemma PO and its
reading; NG-red's family and quantifiers). For layer 1: the n = 1 request with (CE-loc), (MOM_4), (BG-reg) (§20.7). Science:
a witness that vanishes for every centred Gaussian connection ((NG-conn)); without it, non-Gaussianity of the limit stays
open even conditionally.

## Session 12 (2026-10-28)

**Brief.** (1) Apply REVIEW_X11's binding fixes, tagged [RX11-fix]; tally 57/1/3/9/12, ARGUED 36. (2) A genuine
non-Gaussianity statement conditional on layer-1 outputs: (a) the f^{abc} third cumulant of complete-gauge link logs or (b)
one-loop running between two resolutions; prove the implication by the level recursion. (3) A CONSUMER LIST of the layer-1
outputs the existence theorem needs. P read-only; no commits, PRs, pushes, CL or axiom edits.

**Read.** REVIEW_X11.md (all, BINDING); EXISTENCE §0, §15.6, §17.2, §19.8, §20 (all); LOG session 11; ../ym4d-proof/SF.md
§9-§11 and [RSF2-fix CEk-1] (l.836-862); RLARGE.md v2 §1.2-§1.3, §4.2; REVIEW_S22.md Part 5 (BFT). No web access.

**Method and timestamps (UTC).** Fixes 04:59-05:01. §21.0 targets 05:02 (after the fixes and unwritten exploratory
reasoning, which included the star-corner-tree observation). checks/x11_criteria.md ~05:04; x11 ran 05:04:36-05:04:41 (no
wait). x11 showed that its ξ-check is structurally vacuous; checks/x11b_criteria.md ~05:07 was written **after reading x11**
(disclosed in the file), before the x11b script; x11b ran 05:07:46-05:07:51. §21.1-§21.5 written 05:08-05:11.

**Fixes [RX11-fix 1-11].** (1) "not vacuum-only" deleted from NG-red (a one-point function allows dim H = 1). (2) (M1)'s
reason updated to SF session 3: Theorem CE-Q (band) PROVEN (⇐ (FP-loc)_0), global restriction now the deep set 𝔇 (P(𝔇)
extensive); (CE-loc) = (CE-Q^∞) localised + coarse large-V regions. (3) (M2) cites (L-loc)_k (B-NA wall), inherited
activities, CE-exp-col; (M1), (M2) co-binding. (4) RLARGE branch (iii) added as owner. (5) B_N Z-event bound is a ν-bound;
B_N in U-variables only. (6) ε := ε_1. (7) Tally 57/1/3/9/12, ARGUED 36. (8) NG-wit nearly vacuous; (NG-conn) gauge-dependent,
re-posed with a named gauge. (9) d-type members in 𝒯; max_{t'}; separate r_2. (10) A_*(n); x9's h = 1 inadmissible; (b^q)
uniformly quadratic. (11) x10 sample-count deviation recorded; control C a symmetry tautology; reviewer's exact
re-computation credited.

**Findings.**
1. **Lemma AX.** For each of the 8 "star corner trees" (the three links at the corner site plus one outer link per corner
   plaquette), in any complete gauge whose spanning tree contains it the three corner plaquettes are single gauge-fixed
   links (or inverses). Every complete axial (comb) gauge contains one at its root. So the corner witness is the f^{abc}
   cubic of three complete-gauge link logs.
2. **Lemma NG-ax / Theorem NG-ax.** The witness is exactly 0 for every centred Gaussian connection in such a gauge (any
   covariance, any coupling). | NG-red's hypotheses ((O1) ⇐ (F_R), (MOM_4), (LF-loc) ⇐ CB + (RLF-3^dis), (CE-cond^3) with
   c(t_0) ≠ 0): every limit point is separated from that class by ≥ u_+^{-2}|c(t_0)|/2 at resolution m_*. This qualifies
   REVIEW_X11 (4b): NG-wit's sign-symmetric class already contains the axial-gauge Gaussian connections. Not excluded:
   covariant-gauge / i.i.d. Gaussian connections (Lemma PO), tree gauges without a star corner tree, dim H = 1.
3. **Tree-level Wilson value.** E_W[O] = 0.012827·N(N² - 1)g⁴ + O(g⁶) (formal expansion): covariant gauges (κ_PO = 0.008268,
   κ_V = 0.004559, each ξ-independent) and a complete axial gauge (κ_PO ≡ 0, κ_V → 0.01281 at T = 12, within 1.2e-3). The
   vertex does not cancel path ordering. (c3-nz) for the conditional constant stays ARGUED.
4. **CONSUMER LIST (§21.3).** Layer-1 inputs: (F_R) [(U-IR) OPEN]; (RLF-3)+(H-w)+HIST-sum [(H-w) OPEN]; (I_j^E)'' with BFT-0/1/2/4/5
   [B-NA]; (SF^J)_k with (SG^fl)_k; CLS-sf/(AE) [branch (iii)]; (CE-Q^∞) localised + (CE-loc) [branch (ii)]; CE-exp^j
   level-uniform ⇐ (L-loc)_j [B-NA; beyond BFT-3's orders ≤ 4], (FP-loc)_j, (N5-reg)_j, (N5-unif); (BG-reg) ⇐ BFT-1 + BFT-3.

**Checks.** x11: A1 PASS (structurally vacuous), A2 PASS, B PASS, C PASS, **D FAIL** (pre-registered absolute threshold
ignored the |X|⁴ scale), E PASS. x11b (post-x11 criteria, disclosed): F1, F2, D' PASS. Both under the lock, released once;
nice 10; threads 1; load 2.3; 5.0 s / 702 MB and 4.2 s / 122 MB. Load-bearing: x11 A2, B; x11b F2.

**Tally.** PROVEN-HERE 58 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 9 / OPEN 12 (ARGUED 38,
uncounted). After the fixes alone: 57 / 1 / 3 / 9 / 12, ARGUED 36. §21 unreviewed. Snapshot: EXISTENCE_session12_snapshot.md.

**Next.** Independent hostile review of §21 (Lemma AX, the comb rule, the qualification of REVIEW_X11 (4b), the tree-level
formula and x11b's toron treatment, completeness of §21.3). Science: the conditional constant c(t_0) at one RG step (n = 1,
blocked tree-level propagator pinned at the coarse level), computed in a complete axial gauge where it is pure vertex;
a lasso witness for tree gauges without a star corner tree. For layer 1: the §21.3 list is the interface.
