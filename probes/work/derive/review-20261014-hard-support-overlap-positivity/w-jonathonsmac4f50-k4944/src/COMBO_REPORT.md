# Combination X3: the Euclidean set-B package (overlap + OS time + spatial-TT gravity)

**Agent and provenance.**
- Claude Opus 5.5, run 2026-10-14 from 14:07 to 14:58Z. Same model family as the supervisor and every round-1 route agent, so nothing here is independent or refereed.
- No repository file was edited. One arXiv PDF was downloaded (Kikukawa–Usui, arXiv:1005.3751). It sits in `dl_untrusted/` and was only text-extracted, never executed.

**Refresher read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (233 lines). Cited as AX.
- The exercise skill and `proof-search-governance.md` (rounds, gap test, audit), from origin/main.
- Packet files: `WALL.md`, `ASSUMPTIONS.md` and `ROUTES.md` in full; F2 and F3 `ROUTE_REPORT.md` in full; `step0/PRIOR_ART.md` and `OUTSIDE_VIEW.md` by grep.
- Gravity, on HEAD:
  - `TESTS.md:8500-8990` (R19-28 to R19-36 and the closing map);
  - `agents/C5_R19-33_report.md:1-140`;
  - the R19-28, R19-33 and NF-1 referee verdicts in full;
  - the prices in `C5_R19-28_report.md:195-259`;
  - the R2-4 overlap paragraph (`C5_R2-4_report.md:195-300`);
  - `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:15-40`.

**Labels.** proved / checked / suggested / reading / comparator.
- **proved:** a complete argument, mine and unrefereed.
- **checked:** a script was run here; it is listed in §8.
- **comparator:** literature. Kikukawa–Usui was read this session from the PDF text. Other comparators are recalled and marked as such.

**Paths.**
- `CH/` = `.claude/science/exercises/chirality-grid-20261014/` in the chirality-grid worktree.
- `GR/` = `.claude/science/exercises/gravity-current-state-20261009/` in the toe-leverage worktree.
- `X3/` = this folder.

---

## 0. Plain-words summary

**The question.** A one-handed grid rule that ticks in real time hides its mirror particles half a tick away, at "quasi-energy π". Round 1 (F3-A) showed that copy is gapless, carries the same charges and is filled upside-down, so the vacuum either lases or the mirror is light. The standard Euclidean chirality tool, the overlap operator D = 1 + V, has the same structure on paper: V is unitary, the real particle sits at V = −1, and the 15 would-be doublers sit at the opposite point V = +1. So does F3-A's kill also hit the Euclidean route (set B)?

**Answer for free fields (proved and checked): no.** In the Euclidean theory V is not a time step. Reconstructing real time (Osterwalder–Schrader) builds a transfer matrix T, and T's spectrum is what decides. Computed exactly:
- **One light handed particle per projection, at zero momentum only.** At the standard setting (M ≤ 1) there is no π sector at all.
- **The doubler content is a continuum of heavy states,** at energy ≥ ln 2 ≈ 0.69 grid units, which is Planckian. It has positive norm and nothing is filled upside-down. That last point is forced: T's top state is the vacuum, so nothing can lie below it.
- **For 1 < M < 2 a π sector does appear.** It is gapped, has positive norm and is not inverted. It is the known non-positive Wilson transfer matrix, not F3-A's copy.

**The price is not escaped, only moved.**
- That heavy continuum is infinitely many states per site. Its threshold is exactly the energy of an infinite fifth-dimension band at zero fifth momentum (identity proved in §1.3).
- So round-1 F2-R's price (a), a non-rational kernel in the Euclidean law, becomes its price (b) once real time is rebuilt: infinitely many hidden modes per site, which is not a qubit site. Going Euclidean does not lower the bill.

**What the combination adds for gravity.**
- The overlap is the fermion edge C5 was missing. Its exact Ginsparg–Wilson symmetry keeps fermions massless under any strain, with no extra tastes (fixes NF-1's two-taste price and R19-34's Wilson hazard).
- Its proper 4D rotations keep the one-light-cone protection of set B.

**The gauge-field finding (checked; not decisive).** I tested whether the overlap stays reflection-positive once gauge fields are dynamical (open lemma L3g).
- **Mirror-symmetric gauge backgrounds:** every positivity check passes.
- **Gauge-fixed (axial) formulation:** fixing the links that cross the mirror plane to 1, the vacuum and one-particle kernels between different half-lattice gauge fields have **negative eigenvalues** (down to −0.3 relative), at zero gauge coupling, on an 8×8 2D U(1) lattice. Wilson fermions pass the identical test.
- **Gauge-invariant version:** average over gauge rotations, i.e. integrate the crossing links over the admissible set. No negative eigenvalue appears (+2e-3 to +3.5e-3), while the gauge-fixed kernel on the **same** configurations is negative (−1e-4 to −1.4e-3). The quadrature error (~5e-3) is as large as the signal, and the configurations are not cleanly admissible. So this is suggestive, not decided.
- **What it does establish (checked, small lattice):** the overlap lacks the gauge-fixed (Osterwalder–Seiler-style) positivity that Wilson fermions have. Any proof of L3g must use gauge invariance essentially; the standard Wilson-fermion proof route is closed for the overlap.

**Bottom line.**
- X3 removes one would-be kill (F3-A) from the Euclidean route and pins its price.
- It closes the standard proof route for L3g (gauge-fixed positivity fails) and finds no violation on gauge-invariant observables (inconclusive).
- It does not touch the route's main open lemma: locality of the non-abelian measure, L2.
- Net: a scope correction plus a sharpened obligation map, not a new mechanism that cracks the wall.

---

## 1. The combined construction

**Object (set-B package).**
1. **Lattice and time.** Euclidean Z⁴ = Z³ × Z_τ with a_t = a_s and whole-law B4⁺ covariance. This is set B (`GR/agents/C5_R19-28_report.md:202-203`). It is the regulator geometry the kinetic-isotropy primitive already names (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:15-27`).
2. **Matter.** Overlap fermions D = 1 + γ5 sign(H_W), with H_W = γ5(D_W − M) built from the hypercubic Wilson kernel. Matter is chirally projected with P̂ = (1 ∓ γ̂5)/2 and γ̂5 = γ5(1 − D), one generation as the 16 (F2-H, `CH/routes/F2/ROUTE_REPORT.md:93-113`). It takes either:
   - (α) Lüscher's gauge-invariant measure for the anomaly-free representation, with no mirror at all; or
   - (β) Kikukawa's strongly coupled mirror.
3. **Real time.** OS reconstruction under link reflection. The transfer matrix T is the time-step operator; records form in the reconstructed theory (set-B price B4, `C5_R19-28_report.md:208-211`).
4. **Gravity.** The spatial-TT graviton coupled to matter, which is site- and link-RP for slice-local stresses [ref, `GR/agents/C5_R19-33_referee_verdict.md:19`]. The Newtonian/constraint sector is carried per R2-4's price (Π-W or Π-NL), because the conserved GR bridge fails site RP [ref, `GR/TESTS.md:8909-8913`].

### 1.1 Lemma X3-A: the free OS spectrum of the overlap (proved; checked by T-X3)

**Setting.** Free overlap on Z⁴, 0 < M < 2, Wilson r = 1 kernel. At spatial momentum p write:
- β(p) = 1 − M + Σ_k(1 − cos p_k);
- S² = Σ_k sin² p_k;
- z = e^{ip₄}.

**Claims.**

1. **(algebra)** ω² := X†X = 1 + S² + β² − β(z + 1/z), which is linear in z + 1/z. D⁻¹ = ½ − iγ·s/(2(ω + b)), with b = β − cos p₄.

2. **(light states)** Write the correlator as C(t; p) = ⟨ψ(t)ψ̄(0)⟩ at t ≥ 1. It has a pole at λ = e^{−E} with sinh E = S if and only if β < √(1 + S²).
   - The pole region Ω contains p = 0 and none of the 7 spatial doubler corners. At those corners β ≥ 3 − M > 1.
   - There is no pole at the time-doubler location λ = −e^{−E} for M < 2.
   - E → 0 only at p = 0.
   - Γ·Res with Γ = γ4 is block-diagonal in the chiral basis, with blocks sinh E ± σ·s. Each block has rank 1 at sinh E = S.
   - So: **one light Weyl state per chirality projection**, matching Kikukawa–Usui's Weyl reduction, their eqs. (47)–(48).

3. **(doublers)** All remaining spectral weight is a cut.
   - It runs over transfer eigenvalues λ ∈ (0, e^{−E₁}] if β > 0, and over [−e^{−E₁}, 0) if β < 0, where cosh E₁ = (1 + S² + β²)/(2|β|).
   - Its density is (1/2π)(γ4 sinh E ∓ iγ·s)|ω|/(sinh²E − S²).
   - γ4 times it has eigenvalues ±(sinh E ± S), which have definite sign because E > E₁ > arcsinh S.

4. **(positivity)** Link RP holds on both sectors: Γ·W/λ is PSD. The λ > 0 sector has Γ·W PSD; the λ < 0 sector has Γ·W NSD.
   - Hence for **0 < M ≤ 1, T ≥ 0**: no λ < 0 sector exists, since β ≥ 1 − M ≥ 0.
   - For **1 < M < 2**, T has a gapped negative-eigenvalue continuum for p with β(p) < 0. It is identical in origin to Wilson r = 1 with B(p) < 0 (Lüscher's positivity condition, comparator, recalled).

5. **(thresholds)** At S = 0, E₁ = |ln|β||. So E₁,min(M) = min(|ln|1 − M||, ln(3 − M)), taken on S = 0 points:
   - M = 1: ln 2 = 0.693;
   - M = 0.5: 0.693;
   - M = 1.5: 0.405, with the π sector at 0.693;
   - M = 1.9: 0.095, with the π sector at 0.105.
   - The best value is 0.881, at M = 2 − √2 (formula; grid-checked at the four M values).

6. **(the light band ends in the continuum)** On ∂Ω the pole meets the branch point (b = 0 there, so ω = 0). Checked: min(E₁ − E_pole) → 2e-4 on the grid. The light Weyl band is therefore not a section over all of T³. Its Berry monopole is not cancelled by a second node; the band dissolves into the continuum instead.

**Proof.**
- Claims 1–3: closed-form contour deformation of ∫dp₄/2π e^{ip₄t}D⁻¹. The principal branch of ω is continuous on the unit disc minus the cut, because ω² is negative real only for real z ∈ (0, z_b) or (z_b, 0).
- Claim 4: block-diagonality, plus the link-form identity Σ c_i†Γ C(i+j−1) c_j = Σ_n |Σ_j λ_n^{j−1/2} c_j|²_{ΓW_n/λ_n}.
- Claim 5: algebra.
- Each step was checked numerically (T-X3, §6). Decomposition residual against a direct p₄ sum: 1.2e-13. ∎

**Comparator.** Kikukawa–Usui (PRD 82, 114503 (2010), arXiv:1005.3751) prove link RP for the free overlap via the cut on Re p₀ = 0 (their eqs. 26–30, read this session).
- Their contour covers the β > 0 cut only, i.e. M ≤ 1.
- For 1 < M < 2 the cut also sits on Re p₀ = π.
- Reading: their conclusion (link RP) still holds there (checked here, H0 PSD at M = 1.5 and 1.9), but T ≥ 0 does not (H1 indefinite). This does not contradict them; their abstract claims link RP only.

### 1.2 Corollary X3-B: F3-A's π-copy kill does not reach the Euclidean route (proved for free fields)

F3-A's dichotomy, "inverted gapless π copy ⇒ lasing, or a conserved E′ makes it a light mirror" (`CH/routes/F3/ROUTE_REPORT.md:83-97`), uses two premises:
1. the dynamics is the unitary whose spectral degree forces nodes at both 0 and π;
2. the band count is finite.

In the OS reconstruction:
- **(1) fails.** The dynamics is T, a self-adjoint contraction with TΩ = Ω and |λ| ≤ 1 (standard OS; comparator, recalled). No state lies above the vacuum in |λ|, so nothing is inverted. F3-A's lasing branch has no analogue. The conserved energy is H = −log|T| ≥ 0 itself, and under it the doubler content sits at E ≥ E₁,min > 0 (X3-A.3/5).
- **(2) fails.** The fibre is infinite-dimensional (X3-A.6 and X3-C).

**Reading.** The degree of V (deg n = 1; the 15 V = +1 corners carry the compensating chirality) lives on V's circle, not in T's spectrum. The analogy "overlap doublers ≈ F3's π copy" is correct for V and wrong for time evolution. The only π sector T can carry (1 < M < 2) comes from the Wilson kernel's B < 0, not from V = +1. It is gapped and not inverted.

### 1.3 Lemma X3-C: the price relocates across OS (proved, elementary; checked)

- **(i)** The cut density is positive-definite (rank 4) on an interval of E. So span{ψ̄(t)Ω : t ≥ 1} at fixed p is infinite-dimensional.
  - Checked: the block-Hankel rank of the overlap is 4n (full) for n ≤ 5, growing until the 1e-11 precision floor (20–28).
  - Wilson r = 1 stays at exactly 2 for every n (T-X3 step 2).
  - So the reconstructed real-time theory needs infinitely many single-particle modes per spatial site.
- **(ii) Identity (algebra).** For a 5D Wilson fermion with mass −M, the 4D-time transfer poles satisfy cosh E = (1 + S² + sin²p₅ + B₅²)/(2B₅), with B₅ = β + 1 − cos p₅. At p₅ = 0 this equals cosh E₁(p).
  - So **the overlap's doubler threshold is the 5D bulk band energy at p₅ = 0.** It is not always the band minimum: near p = 0 with β small the band can dip lower.
  - Reading/suggested: the overlap's continuum is the 4D shadow of the infinite fifth-dimension (inflow) bulk, as in the L_s = ∞ domain-wall picture with Pauli–Villars subtraction. Full equivalence is not shown; only this threshold identity is proved.
- **Consequence (reading).** F2-R's options (a) and (b) (`CH/routes/F2/ROUTE_REPORT.md:149-155`) are one price, seen from the two sides of OS:
  - (a) is a non-rational kernel in the Euclidean law (AX:57);
  - (b) is an infinite-dimensional reconstructed real-time site (AX:47, AX:37-41).
  - Choosing set B does not cheapen chirality.

### 1.4 X3-D: compatibility with C5 (proved for the free part; the interacting part is comparator)

- **Strain-protected masses (WALL.md:45 edge case).** For any uniformly strained Wilson kernel (hopping weights w_μ), X(p = 0) = −M·1, so V(0) = −1 and D(0) = 0 exactly (proved, one line).
  - With interactions, exact GW (Lüscher) symmetry forbids additive mass renormalization (comparator, recalled).
  - This removes R19-34's Wilson PSI-HAZARD channel. Its worker already listed GW edges among the zeros, `GR/TESTS.md:8886` [worker]; the referee left R19-34 OPEN, `:8914-8918`.
  - It also removes NF-1's two-identical-taste price (`GR/agents/C5_NF1_referee_verdict.md:19`), because the overlap has one taste.
  - New cost: the non-rational kernel.
- **Light cone.** The chiral projection commutes with proper 4D rotations (γ5 commutes with Spin(4)), so the theory is B4⁺-covariant.
  - The refereed cone protection comes from the 90° time–space rotation zeroing every dimension-4 speed row (T1/F2/O1; `GR/TESTS.md:8510` quoting them). That rotation is proper, so B4⁺ suffices (reading).
  - R19-28 also finds B4⁺ and W(B4) give identical graviton-kernel counts (`C5_R19-28_report.md:124`).
  - Parity is not kept; the axioms do not ask for it (`CH/WALL.md:55`).
- **Gravity coupling (open; new leaf L3grav).** R19-33's RP proof for matter + spatial-TT needs a slice-local stress (`C5_R19-33_report.md` §2.1). The overlap stress is exponentially non-local in time, so that proof does not apply. RP of overlap + h^TT is open.

### 1.5 X3-E: the gauged RP lemma L3g, tested (checked; not decisive)

- **T-X3b (diagonal backgrounds).** In 160 θ-symmetric 2D U(1) backgrounds the overlap passes, static and with electric fields. That is, U on the negative-time half equals the mirror image of U on the positive half.
  - The one-particle RP matrix is PSD.
  - K–U's cross kernels have the right signs (Q1 NSD, Q2 PSD).
  - Wilson passes too.
  - So K–U's Pauli–Villars obstruction ([∇₀, ∇_k] ≠ 0, their §VI, eqs. 60–61) is not visible per background.
- **T-X3c (off-diagonal, axial-gauge-fixed).** Take independent half-lattice configurations u_a, u_b, with the crossing links set to 1 on both planes, at gauge coupling β_g = 0.
  - The vacuum kernel Z_ab = det D[(u_a, θu_b)] has min eigenvalue/max = −6.2e-3, −0.31 and −1.9e-2 (types S 0.3, S 1.0, E 0.3). E 1.0 stayed PSD.
  - The one-particle kernel gives −1.0e-2, −0.34, −2.3e-2 and −0.23.
  - **Wilson is PSD in the same sets** (Z ≥ +8e-4; one-particle ≥ −5e-16).
  - This is a reflection-positivity violation of the gauged overlap, in the gauge-fixed formulation, at β_g = 0, on 8×8.
  - **Caveat (mine):** f concentrated on one configuration is not invariant under gauge rotations of the boundary slice. Physical RP needs only gauge-invariant observables.
- **T-X3d (gauge-invariant, 4 crossing links Haar-integrated).** OPEN. Wilson is exact and PSD. The overlap quadrature does not converge (n = 4/6/8 give +3.5e-2, +4.9e-3, −6.0e-4; change 4e-2).
  - Reading: Haar-random crossing links break the plaquette bound, H_W gets zero modes, and det D_ov jumps.
  - So **admissibility enters RP as a cross-plane support constraint.** That is itself non-factorizable.
- **T-X3e (2 crossing links, n up to 128).** OPEN, killed for memory after one set.
  - Overlap −1.5e-4, but quadrature change 6.2e-3.
  - 65% of the Haar grid is non-admissible (min|H_W| < 0.05).
- **T-X3f′ (gauge-invariant, crossing links integrated over the ADMISSIBLE set |arg P| < 0.3 only; Lx = 4, open time, s = 0.15, 3 sets).**
  - Overlap min eig/max at n = 12: +2.1e-3, +2.5e-3, +3.5e-3. Wilson + indicator: +1.3e-3, +2.0e-3, +1.3e-3.
  - Quadrature change n = 8 → 12: 2.6e-3 to 5.7e-3.
  - Formally GIA-PASS, but **not clean**: min|H_W| = 0.002–0.021 < 0.05, because bulk plaquettes reach 0.74.
- **D1 (diagnostic, same lattice and configurations, gauge-fixed).** Wilson PSD (+5e-5). Overlap −1.0e-4, −1.4e-3, −1.2e-3.
- **Reading.**
  - The gauge-fixed violation is reproduced, and is not seen after averaging over boundary gauge rotations. That is consistent with a property of non-gauge-invariant observables.
  - Checked consequence: the Osterwalder–Seiler axial-gauge RP property, which Wilson fermions have and which their RP proof uses, **fails for the overlap**. L3g, if true, holds only on gauge-invariant observables and needs a proof that uses gauge averaging.
- **Why the admissible set is a fair test (proved, character expansion).** At β_g = 0 the pure-gauge part of the cross-plane kernel is Σ_n c_n^{L_x}(W_b W̄_a)^n, with c_n = sin(nδ)/(nπ) and W the boundary-slice Wilson line. For even L_x it is positive-type. So the plaquette bound alone does not break RP there.

---

## 2. Admissibility checks against the axioms (reading, with lines)

| Item | Status | Line |
|---|---|---|
| Z⁴ sites with a_t = a_s | Price B1 (set B). AX has Z³ only | AX:37-41; `C5_R19-28_report.md:202` |
| B4⁺ covariance of the whole law | Price B2. AX has proper cubic rotations about sites in 3D | AX:37-41, :57-58 |
| sign(H_W) kernel, exponentially local, not finitely generated | Price P-X3a = F2-R (a). One fixed **nearest-neighbour** rule is violated | AX:57; `CH/routes/F2/ROUTE_REPORT.md:153` |
| Euclidean weight; probabilities only after OS | Price B3, extended by the R2-4 gravity price | AX:60-61, :63-73; `C5_R2-4_report.md:293-294` |
| Real-time site = infinite-dimensional fibre | Price P-X3b = F2-R (b), relocated (X3-C) | AX:47 |
| Grassmann statistics | Supplied (WALL three-column) | `CH/WALL.md:55` |
| Records in the reconstructed theory | Price B4; R2-5 open | AX:77-83; `C5_R19-28_verdict.md:11` |
| Plaquette bound (locality) | Reading: a support constraint (AX reading note 3). T-X3d shows it acts across the reflection plane | AX:63-73 |
| A law privileges no states | Respected. No vacuum projector is used, unlike F2-R option (c) | AX:94 |

---

## 3. The full set-B package and its open lemmas

**Statement (suggested as a package; not constructed).** Three generations, each the 16 including ν_R. The F1 mod-16 gate passes only at 16 (`CH/ROUTES.md:9`).

**Construction.**
- Overlap-projected Weyl fields on Euclidean Z⁴ in the hypercubic Wilson-kernel overlap at M ∈ (0, 1].
- Exactly gauge-invariant chiral measure: route (α) Lüscher, or (β) Kikukawa mirror.
- SU(3) × SU(2) × U(1)_Y link fields restricted by the plaquette bound.
- Spatial-TT graviton, with the constraint sector by Π-W or Π-NL.
- OS reconstruction to real time; records in the reconstructed slices.

**Open lemmas** (dependency order; leaves marked).

| Id | Statement | Status | Evidence |
|---|---|---|---|
| L3-free | Free (Weyl) overlap RP, with T ≥ 0 for M ≤ 1, one light Weyl per projection, doublers in a positive continuum | **closed** (comparator + proved + checked) | X3-A; K–U |
| L1 | Locality of D[U] under the plaquette bound | comparator (Hernández–Jansen–Lüscher) | F2 :109 |
| **L2α** | Locality and smoothness of the Lüscher measure term for the SM 16 in all sectors, non-abelian, nonperturbative | **OPEN, terminal** | Known: U(1) proved, all orders proved, SU(2)×U(1) with zero U(1) flux (Kadoh–Kikukawa) (F2 :101-106) |
| L2β (alternative) | Kikukawa mirror decoupling (locality of the mirror vertex sector) | OPEN. 2D test designed (F2 :189-195). Golterman–Shamir objections unanswered | F2 :120 |
| **L3g** | RP of the gauged chiral measure on gauge-invariant observables | **OPEN.** Gauge-fixed positivity FAILS (T-X3c, D1), so the Osterwalder–Seiler route is closed. No violation on gauge-invariant observables (T-X3f′; not clean, quadrature error ≈ signal) | X3-E |
| L3-phase | The chiral determinant is complex (P-odd phase; `C5_R2-4_report.md` A4), so RP must be read with complex weights, Θ = θ∘conj (Π-W) | OPEN (suggested feasible, R2-4 :281) | — |
| L3grav | RP of overlap matter + spatial-TT graviton (the stress is not slice-local) | OPEN (new leaf) | X3-D |
| Lbridge | Constraint sector: the conserved GR bridge is not site-RP | **[ref] B-RP-FAILS.** Pay Π-W or Π-NL | `GR/TESTS.md:8909-8913`; `C5_R19-28_verdict.md:9` |
| Lrec | Records via OS (R2-5) | OPEN, Record-sector cost | `C5_R19-28_verdict.md:11` |
| Lnorm | Normalizability with the bridge (Newtonian collapse; a field cutoff is needed) | [ref] a cutoff suffices; not supplied by Qubit | `C5_R19-33_referee_verdict.md:15` |

**What the package does NOT need** (pruned by X3 and round 1):
- no M₄(C) (F2-R);
- no taste doubling (contrast NF-1);
- no additive strain-mass tuning (contrast R19-34);
- no continuous-time K2a selector (PRIOR_ART T5, `CH/step0/PRIOR_ART.md:289`, resolved toward hypercubic time);
- no mirror SMG on route (α).

### Total price list (named only, none adopted; counted once)

| # | Price | Axiom text touched | Source |
|---|---|---|---|
| B1 | Z³ → Z⁴, a_t = a_s | AX:37-41 | R19-28 :202 |
| B2 | Whole-law B4⁺ covariance (regulator, counterterms, records) | AX:57-58 | R19-28 :203 |
| B3 | The site distribution is the conditional of an RP Euclidean weight. **Plus** R2-4's forced gravity price: a non-positive (complex, Θ = θ∘conj) weight Π-W, or a power-law non-local bridge Π-NL | AX:60-61, :63-73 (Π-NL also :57, :61) | R19-28 :204-207; R2-4 :293-294 |
| B4 | Records formed in OS-reconstructed slices; arrow in the state | AX:77-83, :185-186 | R19-28 :208-211 |
| P-X3a | Non-rational kernel sign(H_W) (F2-R (a)) | AX:57 ("one fixed nearest-neighbor rule") | F2 :153 |
| P-X3b | The reconstructed real-time site is infinite-dimensional (F2-R (b), relocated; **the same price as P-X3a, not additional**) | AX:47 | X3-C |
| P-X3c | Wilson-kernel parameter M ∈ (0, 1] for T ≥ 0 (otherwise a two-step T² reconstruction) | none (law data, one inequality) | X3-A.4 |
| P-X3d | Plaquette bound as a hard support constraint (also needs F2-H's Π-FR finite-range-clique reading) | AX:57-61, :63-73 | F2 :114; R2-4 Π-FR |
| P-X3e | Fermions as Grassmann variables; the 16 with ν_R per generation; SM gauge links | supplied (middle column) | WALL :55 |
| Grav | P-N1 (supplied graviton), (Σ), W1-weight + N, carrier: unchanged from R19-28 | AX:47, :94, :114-123, :187 | R19-28 :212-216 |
| L3g contingency | If L3g fails on gauge-invariant observables, OS reconstruction of chiral **gauge** matter is lost. The package then falls under "Euclidean-only without RP" (forbidden, `CH/WALL.md:44`), unless matter also pays Π-W in a form not yet constructed | AX:60-61 | X3-E |

---

## 4. Which round-1 obligation it changes, and how

1. **F3-A (provisional no-go), scope restricted.** It constrains finite-band unitary ticks, not OS-reconstructed Euclidean theories (X3-B, proved free). Registry note: "F3-A does not apply to F2-H/set B."
2. **F2-H's L3 split.**
   - L3-free is **closed**.
   - **L3g** gains finite tests: gauge-fixed positivity fails (proof route closed); the gauge-invariant version shows no violation (inconclusive).
   - **L3grav** is a new leaf.
   - L2 is unchanged.
3. **F2-R's trichotomy is partly collapsed.** (a) and (b) are one price across OS (X3-C). The owner's range question and the site-algebra question are the same decision for this family.
4. **WALL edge case "compatibility with C5" (`CH/WALL.md:45`)** is met by the overlap edge: strain-protected masslessness and the B4⁺ cone. This is a cross-campaign gain. The C5 gravity root currently uses Wilson-type D1 edges, which carry the PSI hazard (`GR/TESTS.md:8883`).
5. **PRIOR_ART T5** (continuous time selector vs hypercubic RP): set B with the overlap needs no continuous-time selector and resolves T5 in favour of hypercubic time, conditional on L3g.

---

## 5. Theorem-strength gap test

**The package's terminal lemma** is L_pkg = L2α ∧ L3g ∧ L3grav ∧ L3-phase. The prices, the Lbridge payment (Π-W or Π-NL), Lrec and Lnorm come on top.
- **L_pkg ⇒ T?** Yes, in T's "Euclidean with RP real-time reconstruction" form, given the prices. The light content and gauge invariance come from L2α; the absence of light mirrors from X3-A.
- **T ⇒ L_pkg?** No. T could be met by SMG constructions without exact GW symmetry, or in continuous time.
- **Strength:** L_pkg is **stronger** than T. It is a sufficient condition and not a restatement: each leaf is a property of a fully specified object, testable by finite computation.

**Governance rule.** A stronger terminal is not near closure unless the route advances its leaves with a new mechanism.
- X3 **closes one leaf** (L3-free).
- It **removes a would-be leaf** (no π copy after OS), by proof in the free case.
- It **adds one leaf** (L3grav).
- It **closes one proof route of another** (L3g: gauge-fixed positivity fails) without deciding it.
- It supplies **no new mechanism for L2α**, the leaf that carries the non-abelian chiral-gauge difficulty.

**Classification.** Not target-equivalent. Repackaging with a scope correction and a sharpened obligation map. **No genuinely new mechanism toward T.** The set-B family stays `active` only through finite tests of L2 (F2-H's 2D test) and L3g (§6). If L3g fails on gauge-invariant observables, the family's real-time branch becomes `blocked`, and only a Π-W-for-matter construction would reopen it.

**Reopen conditions:**
1. a proof or finite certificate of gauge-invariant RP for the gauged overlap (or a DWF formulation at finite L_s with RP and a controlled L_s → ∞ limit);
2. a nonperturbative locality proof for the non-abelian Lüscher measure term on the SM 16.

---

## 6. Cheapest decisive tests (all pre-registered in `X3/PREREG.md` before running)

| Test | Question | Result | Label |
|---|---|---|---|
| **T-X3** (the brief's test) | Free overlap on Z⁴: where do the doublers sit in the OS transfer spectrum? | **PASS** for M ∈ {0.5, 1.0}, i.e. the window containing M = 1. Per projection one light Weyl (residue ranks Dirac 2, Weyl 1 + 1, PSD), no pole at any of the 15 doubler corners, only λ > 0 continuum with E₁ ≥ 0.693 (grid min = ln 2; random search 0.695), H0 and H1 PSD (worst −1.3e-14), decomposition residual 1.2e-13. Controls: Wilson r = 1 PSD with Hankel rank 2; naive H1 = −1.00 (time doubler is a π pole); Wilson m = −1.5 H1 indefinite. **Secondary:** M = 1.5 and 1.9 have a λ < 0 continuum (81 and 179 of 4095 momenta) with H0 PSD (link RP intact) and H1 indefinite (−3e-3, −2.7e-2); thresholds 0.693 and 0.105 at p = 0. Matches Amendment A1 (written before the run) | checked |
| T-X3b | Gauged, θ-symmetric backgrounds (necessary condition) | **BG-PASS.** 160/160 backgrounds; P PSD; Q1 NSD and Q2 PSD; Wilson PSD | checked |
| T-X3c | Gauged, off-diagonal, axial gauge (crossing links = 1), β_g = 0 | **Z-FAIL** as registered (−6.2e-3 to −0.31 vacuum; −1e-2 to −0.34 one-particle); Wilson PSD. Gauge-fixing caveat recorded after the run | checked (caveat) |
| T-X3d | Gauge-invariant version (Haar-integrated crossing links), Lx = 4 | **OPEN.** The overlap quadrature is not converged (Δ = 4e-2); Wilson exact and PSD | checked (inconclusive) |
| T-X3e | Gauge-invariant version, Lx = 2, n up to 128 | **OPEN.** Killed for memory after one set. Overlap −1.5e-4 against a quadrature change of 6.2e-3; 65% of the Haar grid non-admissible | checked (inconclusive) |
| T-X3f / T-X3f′ | Gauge-invariant version, crossing links over the ADMISSIBLE set (δ = 0.5, then 0.3) | T-X3f: killed for memory after 1 set; PSD. **T-X3f′: formally GIA-PASS** (overlap +2.1e-3..+3.5e-3, Wilson +1.3e-3..+2.0e-3), **not clean** (min\|H_W\| ≤ 0.021; quadrature error ≈ signal) | checked (not clean) |
| D1 (diagnostic) | Gauge-fixed kernel on T-X3f′'s configurations | Overlap −1.0e-4 to −1.4e-3; Wilson +5e-5: the gauge-fixed violation reproduced | checked |

**The single cheapest decisive next test** (pre-registrable; cost about 1–2 h with a converged quadrature).
- **Setup.** Gauge-invariant RP of the gauged Dirac overlap at β_g = 0 with an admissibility-respecting measure, now made clean:
  - all plaquettes, bulk included, bounded so that min|H_W| > 0.1 (s ≲ 0.05, or an explicit bulk constraint);
  - the crossing-link integral over the admissible set, with an adaptive or exact-polytope quadrature reaching error < 1e-5;
  - several lattice sizes.
- **PASS:** Z̃ and B̃ PSD to within the converged quadrature error, Wilson PSD.
- **FAIL:** a negative eigenvalue larger than 10× the quadrature change.
- **If FAIL:** L3g is dead in this formulation. The set-B package then needs Π-W for matter, or a DWF formulation at finite L_s, which is 5D-Wilson RP; that formulation's gauge invariance is only approximate, so it falls back to F2-R's finite-n price, about 60 auxiliary fields per site.

---

## 7. Strongest objection (my own kill pass; not a referee)

- **K1. "The free result is textbook (K–U plus the domain-wall folklore)."** Mostly true. What is new here:
  - the explicit verdict on the F3-A question;
  - the M-window statement, i.e. T ≥ 0 exactly for M ≤ 1, and a gapped non-inverted π sector with link RP intact for 1 < M < 2, plus the scope remark on K–U's contour;
  - the identity E₁ = the 5D bulk band energy at p₅ = 0;
  - the Hankel-rank form of the price relocation.

  None of this is a new mechanism. **Conceded.**
- **K2. "T-X3c kills the package."** No. It is a gauge-fixed violation on non-gauge-invariant observables. Gauge averaging over the admissible set removes it within the (large) quadrature error (T-X3f′, D1).
  - What survives is a method result: the Osterwalder–Seiler axial-gauge positivity that makes Wilson-fermion RP easy fails for the overlap.
  - Mechanism (reading): D_ov[U] couples U₊ and U₋ non-factorizably, through a kernel that is not finite-range across the plane.
- **K3. "An infinite-dimensional real-time site violates Qubit, so the package is excluded."** It is a price (P-X3b), and the same one as P-X3a. Set B already moves the record sites to reconstructed slices (B4). The Qubit axiom then has to be read on the Euclidean variables. That is a reading change the owner must decide; it is not adopted.
- **K4. "Gravity RP is already refereed-dead for set B (B-RP-FAILS)."** Only for the conserved GR bridge. The package inherits R2-4's price Π-W or Π-NL [ref]. And L3grav adds a further open item for overlap matter (non-slice-local stress).
- **K5. "M ≤ 1 might fail in rough gauge fields."** Suggested, not checked: with gauge fields, β becomes 1 − M plus the covariant spatial Wilson term, which is ≥ 0 as an operator. So no B < 0 sector, and T ≥ 0 per static background, for M ≤ 1. With time-dependent fields this argument does not apply.
- **Does it assume the target?** No.
- **Does it contradict a refereed result?** No. It refines `C5_R2-4_report.md:204` (free overlap RP: established, comparator K–U, as F2-H already said) and restricts F3-A's scope.

---

## 8. Files (all in `X3/`)

- `PREREG.md`: T-X3 (and Amendment A1, before the run), T-X3b, T-X3c, T-X3d, T-X3e, T-X3f, T-X3f′ and D1, each written before its run, with result lines appended.
- `scripts/tx3_overlap_transfer.py` → `.out`: T-X3. 2 s, 202 MB peak.
- `scripts/tx3b_gauged_rp_2d.py` → `.out`: T-X3b. 2 s, 48 MB.
- `scripts/tx3c_offdiag_rp_2d.py` → `.out`: T-X3c. 23 s, 149 MB.
- `scripts/tx3d_gauge_invariant_rp_2d.py` → `.out`: T-X3d. Killed after 5 of 8 sets; about 203 MB.
- `scripts/tx3e_gauge_invariant_rp_2d_Lx2.py` → `.out`: T-X3e. Killed after 1 set at 280 MB (over the limit).
- `scripts/tx3f_admissible_gi_rp_2d.py` → `.out`: T-X3f. Killed after 1 set at 306 MB (over the limit).
- `scripts/tx3fp_admissible_gi_rp_2d.py` → `.out`: T-X3f′. Completed; peak 261 MB = 249 MiB, at the limit.
- `scripts/d1_gaugefixed_same_configs.py` → `.out`: D1. 36 MB.
- **Memory note:** three runs exceeded or touched the 0.25 GB rule (T-X3e 280 MB, T-X3f 306 MB, T-X3f′ 261 MB peak). Each was killed or ended within minutes, and nothing is left running.
- `scripts/pdf2txt.py`: text extraction of the downloaded PDF (pypdf, run outside the download folder).
- `dl_untrusted/`: the Kikukawa–Usui PDF and its extracted text (untrusted; read only).

**Literature used.**
- Kikukawa & Usui, [arXiv:1005.3751](https://arxiv.org/abs/1005.3751), PRD 82, 114503 (2010). Read this session: §III eqs. 26–31, §IV eqs. 38–48, §VI eqs. 60–61.
- Usui, [arXiv:1201.3415](https://arxiv.org/abs/1201.3415). Abstract only: the overlap scalar boson violates RP.
- Kikukawa, [hep-lat/0111035](https://arxiv.org/abs/hep-lat/0111035). Abstract only.
- Lüscher (1977) on the Wilson transfer matrix: recalled.
- Hernández–Jansen–Lüscher (overlap locality): recalled, via F2.
