# C5 R18-4 report: W15's last free finite-band holes — crossing bands (and a note on merely continuous multi-shift mixing)

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Not refereed. 2026-10-13, 02:18Z to 02:46Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R18-4/`.
- `S/r184_cross.py` and `S/r184_cross.out`: every numerical check below. Seven blocks, about 8 s at `OMP_NUM_THREADS=2`.
- `S/recheck/{R16-5,R17-5,R17-8}/`: the archived runners, copied unmodified from `P/scripts/C5/`.
  - R16-5 and R17-5: reruns byte-identical to the archived `.out` files (`diff` empty).
  - **R17-8: the archived runner fails as committed** (`rerun_ascommitted.out`: `ModuleNotFoundError: No module named 'r99_profiles_copy'`). It imports from `recheck/R16-5/` beside itself (`r178_mix.py:7`), which is not archived. With `R16-5/r99_profiles_copy.py` copied to `recheck/R16-5/`, the rerun is byte-identical to `r178_mix.out` (`rerun.out`). This is the same defect class R18-2 fixed for R17-7 (`TESTS:6625`). Suggested archive fix: point the import at `../R16-5`.
- No downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method (`:2302-2320`); Round 17 rules (`:5688-5706`); Round 18 head and rules (`:6392-6420`) and R18-4 (`:6557-6575`), the FIXED text reported against; R17-8 (`:6061-6087`); verdicts R17-6/7/8 (`:6283-6336`); `:6580-6663` (R17-9..13, R18-2, R18-5).
- `agents/C5_R17-8_report.md` (`rR17-8`) and `agents/C5_R17-8_referee.md` (`vR17-8`) in full; `agents/C5_R17-8_referee_verdict.md`.
- `agents/C5_R17-5_report.md` (`rR17-5`) in full; `agents/C5_R17-5_referee.md` (`vR17-5`) and its verdict file.
- `agents/C5_R16-5_report.md:30-135`; `agents/C5_R16-5_referee_verdict.md` (`vR16-5`) in full.
- `agents/C5_S23_synthesis.md` W15 sections (`:85-97,221-249,392,660-675,958-976`); `agents/C5_S20_synthesis.md` W15 hits (`:178-188,292`).

**Not read.** R9-9 and R8-2 reports (the graviton enters only through θ and R16-5's statement of H_g, as in R17-8). The pending R17-12/R17-13/R18-1/R18-2/R18-5 scratch reports: nothing here depends on them.

**Labels.** **proved** (complete under stated hypotheses); **checked** (numbers in `r184_cross.out`); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature or standard fact, RECALLED unless verified).

---

## 0. In plain words

1. **The question.** R17-8 showed (refereed, scoped) that for a *single isolated* band the field-dependent translation identity becomes a winding statement on the energy surfaces, and a torus can support at most one such winding while redshift needs three. Does a band *crossing* break that?
2. **No, for any two-band analytic crossing (proved, worker, modulo RECALLED standard facts).** There are two local kinds:
   - **Crossing surfaces where the bands swap smoothly** (decoupled species protected by a charge; folded bands protected by a half-translation). The right object is the smooth *branch*, not the "lower/upper" band. The branches live on a doubled zone at worst, which is again a 3-torus, so R17-8's argument runs unchanged there.
   - **Conical crossings** (Weyl points, protected nodal lines, quadratic touchings). The momentum operator must be a plain number on the touching pair at the crossing (new Lemma S0). So the band's momentum stays continuous through the crossing, and the winding argument goes through the cone tip.
   - **A cone at the bottom of a band** (massless Dirac/Weyl matter) still needs all three windings for redshift (new Lemma RB-X), so it fails too.
3. **Numbers agree (checked).** On Weyl, tilted-Weyl, nodal-loop and folded-band laws, the best fit to the needed identity stays at 76–79% residual, as on isolated bands (72–77%, `rR17-8:231-234`). The controls find solutions where they exist.
4. **Mixed crossings are covered too.** One configuration looked dangerous: a smooth-swap surface ending on a conical line and flipping the branch orientation as you go round the line. It cannot happen for analytic laws (Lemma X2). Real-analytic zero curves in a plane come in pairs of half-branches, and the flip parity is the same on both halves of a pair. This rests on RECALLED real-analytic geometry. Checked on 45 laws, with a non-analytic control that does flip.
5. **What is left.**
   - Merely continuous multi-shift mixing (the title's second hole) is still open. The most natural candidate I built for it fails a necessary spectral test (checked), but there is no general proof.
   - More than two bands (braids) is outside this item.
6. **Worker reading: EXCLUDED-CROSS for the whole stated two-band class, pending the referee.** The proof leans on standard facts I RECALLED rather than verified: the tame Reeb theorem in subanalytic form, half-branch evenness, and stratification. If the referee rejects any of them, the reading is OPEN, with that step named. No ESCAPE.

---

## 1. Hypotheses and classes (stated before any title)

Everything is R17-8's Theorem W setting (`rR17-8:66-93`, `vR17-8:39`), with one hypothesis removed.

- **Kept from R17-8:**
  - **H-mat:** free quadratic matter on Z³ × ℝ, continuous Hermitian Bloch symbol;
  - **H-an:** real-analytic symbols;
  - **H-ker:** continuous coupled kernels, C¹ in q at q = 0;
  - **H-W1:** W1_pf with time-dependent shifts and symmetric stress;
  - **H-grav:** R9-9's N-type graviton, projectable lapse;
  - **Lemma N** (`vR17-8:7`): canonical, local-in-time; Γ_j = Π_j := F^{0j}(k,k), and [h, Π_j] = 0;
  - **regular linear field-dependent generators**, with Lemma FD as corrected (`vR17-8:19`): on equal-energy transitions the identity holds through O(q), with an O(q²) remainder;
  - **multiplier shifts:** θ_j(q) = C_j·q + O(q²), one universal C (standard C = 1, or deformed);
  - **H-RB:** the redshift bridge, a hypothesis on `AX:187` (`vR17-5:15`).
- **Removed:** isolated (simple) bands (`TESTS:6566`).
- **H-2b (the setting, `TESTS:6560-6564`).**
  - h(k) = f(k)·1 + d(k)·σ, with f and d real-analytic and 2π-periodic.
  - Crossing set X = {d = 0} ≠ ∅.
  - Write Π_j = α_j + b_j·σ, with α_j and b_j analytic. Then [h, Π_j] = 0 ⇔ b_j × d = 0.
- **Point types.** At x ∈ X, let Λ(x) ⊂ S² be the set of limit directions of d̂(k) as k → x, k ∉ X.
  - **Conical point (B):** Λ(x) is not contained in any pair {±n}. Write X_* for the set of these.
    - Examples: Weyl points; nodal lines with nonzero transverse winding (PT- or mirror-protected); quadratic touchings, e.g. d = (x²−y², 2xy, ·).
  - **Smooth point (A):** near x, d = g·n with g and n analytic and |n| = 1. g may change sign across X.
    - Examples: generic points of a crossing surface. This covers decoupled species (n = const) and folded bands (n anti-periodic).
  - **Collinear non-smooth point (X_c):** Λ(x) ⊂ {±n₀}, but there is no analytic factorization. Example: d = (x²+y², x³, 0).
- **Class 𝒳.** H-2b with d ≢ 0, plus:
  - **(X1)** dim(X_* ∪ X_c) ≤ 1.
  - **(X2)** The line field ℓ = span d extends continuously to T³ ∖ X_*. Its orientation double cover over T³ ∖ X_* must extend to an *unbranched* cover of T³: no orientation monodromy around conical lines.
  - **Both are automatic for every H-2b law with d ≢ 0** (Lemma X1/X2, §3.6; proved, modulo RECALLED real-analytic geometry). So 𝒳 is the whole stated two-band class.
- **Excluded realizations (outside, with why).**
  - N > 2 bands, where non-abelian braid monodromy around conical lines is possible (comparator: non-Abelian band topology, Wu–Soluyanov–Bzdušek 2019, RECALLED).
  - d ≡ 0: a protected doublet, degenerate everywhere, so not a crossing surface or line. **Suggested:** the same continuity argument applies. At first order on shell, the sorted joint eigenvalues of the commuting Π_j satisfy (i) on the level sets of f, and sorted eigenvalues are continuous. Not refereed-ready.
  - Non-analytic symbols (P90 is the discontinuous extreme).
  - Towers (P64).
  - Mixing generators jointly with field-dependent ones (R17-8's other open item, not this one).
  - Interactions, non-symmetric couplings, non-projectable lapse (`TESTS:6564`).
- **Subtractions (named before any run).** None. All values are raw least-squares residuals, singular values and spectral defects.
- **Order.** W1_pf exact at O(√κ). The W2_pf zeroth moment at O(κ), on the equal-energy surface through first order in q (Lemma FD). RB at linear order in the strain.

## 2. Prior art (each counted once)

- **R17-8 and vR17-8.**
  - Theorem W (i)–(ii) are confirmed. (iii) is repaired by continuing B_abj = v_a(∂_bπ_j − C_jb) − v_b(∂_aπ_j − C_ja) analytically, then applying the tame Reeb theorem (`vR17-8:21-29`).
  - The steelman is "an analytic crossing-band or joint mixing/field-dependent completion" (`vR17-8:35`).
  - R17-8 itself only suggested crossings: "a braid lifts to a finite cover of T³, which is again a 3-torus" (`rR17-8:240`).
  - §3.2 below is that suggestion, made precise for sign-flip crossings. §3.1 and §3.3 are new: the conical case, where no analytic branch exists.
- **R17-5 and vR17-5.**
  - MB-A partner step (`vR17-5:7`).
  - Lemma F, P_E F^{(ij)} P_E = V_iΠ_j|_E (`vR17-5:9`), used for R = v·π off X.
  - RB as a bridge (`vR17-5:15`).
  - The bridge-free lattice-translation test (`rR17-5:191-195`) applies to every continuous finite-band Π, crossings included. Counted once, not re-derived.
- **R16-5 and vR16-5.** T_pf, the half-space argument, pair grading (`vR16-5:11,19`).
- **Tame Reeb facts** as cited in `vR17-8:29` (Kaluba–Marzantowicz–Silva arXiv:1405.4579; Gelbukh arXiv:1903.00777). Comparators, RECALLED. §3.2 needs their subanalytic (o-minimal) form for the Lipschitz sorted band; that extension is RECALLED, not verified.
- **Repo grep.** Searched `TESTS.md`, `SUMMARY.md` and `agents/*.md` for "crossing band", "crossing-band", "band crossing", "Weyl", "nodal", "conical" and "folded".
  - **Relevant, counted once:**
    - **C4 I1 referee** (`agents/C4_I1_referee_full.md:112-133`). Crossings leave the *trace* sum rule intact. "at a band crossing an analytic/monodromy branch need not itself be periodic". An N-cycle spectral unfolding "is only a spectral equivalence". §3.2's cover construction is the eigenvector-level version for two bands: P_E and π_E are periodic on the cover, and no claim is made that the unfolded model is "the same model".
    - **C4 I3** (`agents/C4_I3_report.md:25,41`): superlattice bands are folded fine bands, and the zone sum rule holds through crossings.
    - **TESTS:1448** (RD lane): "two-band crossings" listed as open for the SLAC/Herglotz face-jump question. A different identity, not used.
    - R17-8's suggestion (`rR17-8:240`), vR17-8's steelman, S23's open lists (`S23:96,240,248`) and R18-4 itself.
  - **Unrelated:**
    - "Weyl" hits: Weyl fermion counting (`TESTS:14`), Weyl automata (C4 B1), Weyl's law (R5-5);
    - "nodal": nodal sets of eigenfunctions (R5-5);
    - "conical": conical lattice defects (R3-3).
  - None treats the shift-generator momentum at a crossing.

---

## 3. Results

### 3.1 Lemma S0 (the momentum is a number at a conical point). Proved

**Statement.** In H-2b, let x ∈ X_*. Then Π_j(x) = α_j(x)·1. On T³ ∖ X, the band momenta π_{±,j} = α_j ± b_j·d̂ extend continuously to x, both with the value α_j(x).

**Proof.**
1. [h, Π_j] = 0 gives b_j(k) = (b_j·d̂)d̂ for k ∉ X.
2. Take sequences k_n → x with d̂(k_n) → u₁ and d̂(k_n′) → u₂, where u₁ ≠ ±u₂ (definition of X_*). b_j is continuous, so b_j(x) ∥ u₁ and b_j(x) ∥ u₂. Hence b_j(x) = 0.
3. Then |π_± − α_j| = |b_j·d̂| ≤ |b_j| → 0 at x. ∎

**Checked** (`r184_cross.out:1-5`).
- The limit-direction sets have rank 3 at a Weyl point (singular values 44.8, 31.7, 31.4) and rank 2 at a nodal-loop point (46.9, 42.4, 0). Both are non-collinear.
- For an explicit commuting Π = α + λ d·σ, |π_+ − π_−| ≤ 3.6e-6 on a sphere or circle of radius 1e-6.

### 3.2 Theorem WX (Theorem W across a crossing). Proved, given the tame Reeb facts (RECALLED)

**Construction (proved, standard covering theory).**
- By X2, there is a cover T̂ of T³. It is either two copies of T³ or a connected 3-torus ℝ³/Λ′, with Λ′ ⊂ 2πZ³ of index 2. (Finite covers of T³ are 3-tori because finite-index subgroups of Z³ are ≅ Z³; standard.)
- On T̂ there is a continuous unit field n̂ ∥ d. Define:
  - the branches E_± = f ± d·n̂;
  - the projectors P_± = (1 ± n̂·σ)/2;
  - the branch momenta π_{±,j} = tr(P_±Π_j).
- Let Ω = T̂ ∖ preimage(X_* ∪ X_c).
  - n̂, E_±, P_± and π_± are analytic on Ω. At A-points this follows from the local factorization, up to the sign that the cover fixes.
  - Ω is connected: by X1, a closed set of dimension ≤ 1 does not disconnect a 3-manifold (RECALLED, standard).
- π_± is continuous on all of T̂:
  - at X_c points, because n̂ is continuous;
  - at X_* points, by Lemma S0.
- On pure-B laws the branches are the sorted bands, Lipschitz at X. On pure-A laws they are the smooth branches, which may be exchanged across the zone (folded bands).

**Statement.** Under §1, let E be a branch with π_E ≢ 0 on Ω, and v_E ≢ 0 (no flat band). Then:
- **(i)** t·∇π_{E,j} = C_j·t for every t ⊥ v_E, at every k ∈ Ω ∖ X with π_E(k) ≠ 0 and v_E(k) ≠ 0;
- **(ii)** the tensor B_abj vanishes identically on Ω;
- **(iii)** on the lift of T̂, ψ_j = π_{E,j} − C_j·k is constant on every connected level component of E whose points in the regular part of Ω are dense in it;
- **(iv)** rank C ≤ 1.

**Proof.**
- **(i)** At k ∉ X the two bands are non-degenerate in a neighbourhood, and E is locally one of them. R17-8's derivation of (i) (`rR17-8:220`; `vR17-8:21`) applies verbatim:
  - Use the generator j acting on any coupled density 0i with F^{0i}_{EE}(k,k) = π_{E,i}(k) ≠ 0.
  - On intraband equal-energy transitions, Lemma FD leaves (π_j(k+q) − π_j(k) − θ_j(q))·F^{0i}_{EE}(k,k+q) = O(q²).
  - Near X, interband equal-energy transitions at small q impose further identities of the same form. They add constraints and remove none.
- **(ii)** B is analytic on the connected Ω and vanishes on the nonempty open set where (i) holds (π_E and v_E are analytic and ≢ 0, so their nonzero sets are open and dense). So B ≡ 0 on Ω. This is vR17-8's repair (`vR17-8:25-29`), run on Ω instead of T³.
- **(iii)** B ≡ 0 is the same as dψ_j ∧ dE = 0. So ψ_j is locally constant along regular level sets in Ω. Take a level component L of the kind stated.
  - ψ_j is continuous on L (π_E is continuous on T̂).
  - It takes finitely many values on the dense regular part (finitely many components, by subanalytic finiteness; RECALLED).
  - So ψ_j(L) is a connected subset of a finite set: a single point.
- **(iv)** Let γ be a loop in a regular level component of T̂, and lift it to a path from k to k + λ, with λ ∈ Λ′. Periodicity of π_E on T̂ and (iii) give 0 = ψ_j(k+λ) − ψ_j(k) = −C_j·λ for every j, so Cλ = 0.
  - By the tame Reeb facts (`vR17-8:29`; RECALLED), the classes of regular level cycles generate a subgroup of H₁(T̂) ≅ Λ′ of rank ≥ 2. The reason: the Reeb graph of a function on a 3-torus has first Betti number ≤ 1, and the level cycles generate the kernel of H₁(T̂) → H₁(Reeb).
  - For pure-B laws, E is subanalytic and Lipschitz rather than analytic. The tame (o-minimal, Hardt-trivial) version is needed there: RECALLED, not verified.
  - So ker C has dimension ≥ 2, and rank C ≤ 1. ∎

**Answer to probe (a).** Yes, the analytic-continuation step of `vR17-8:25-29` survives across crossings in 𝒳, with two changes:
- it runs along branches on the orientation cover, not along sorted bands. Across a sign-flip surface, a sorted band's momentum jumps from one branch's value to the other's, so sorted-band level sets would carry two different constants of ψ;
- at conical points the continuation is not analytic. The gap has codimension ≥ 2, and Lemma S0 makes ψ continuous through it.

This is where the expectation's caveat ("if the branch continuation fails at the crossing set", `TESTS:6575`) was tested. Continuation fails analytically, but continuity is enough.

### 3.3 Lemma RB-X (redshift at an extremum of any homogeneous order, conical included). Proved

**Statement.** Let k₀ be an IR-regular extremum of the branch E that carries the IR particle. Its leading dispersion φ_s(p) is positive, homogeneous of degree s > 0, and C¹ off 0. Cases:
- s = 2, analytic: the massive case of R17-8 (ii);
- s = 1, at a conical point of X_*: type-I Weyl or Dirac matter at the band bottom.

Assume π_E ≢ 0 near k₀; otherwise R ≡ 0 and RB fails at once. Then H-RB forces **rank C = 3**.

**Proof.**
1. **Form of π near k₀.** Near k₀ the level sets of E are single star-shaped spheres. By (iii), π_E = Cp + F(E), with F continuous.
   - For s = 1, F has a right derivative f₁ at the bottom level. This follows from π_E = α + b·n̂ with α analytic and b(k₀) = 0 (Lemma S0): π_E = π₀ + Λ(p) + O(p²), with Λ positively homogeneous of degree 1.
   - For s = 2, F(E) = π_E − Cp is analytic and a function of a positive quadratic form, so it is a series in E.
2. **Degree s − 1.** R = v·π (`vR17-5:9`, off X, with continuity) must equal p·v = sφ_s (Euler) at leading order. The degree-(s−1) term is ∇φ_s(p)·π₀. It must vanish for all p, and putting p = π₀ gives ∇φ_s(π₀)·π₀ = sφ_s(π₀) > 0 unless π₀ = 0. So π₀ = 0.
3. **Degree s.** The remaining condition is ∇φ_s(p)·Y(p) = 0, with Y(p) = (C − 1)p + [s = 1]·f₁φ_1(p).
   - So on the level surface S = {φ_s = 1}, the affine field Y_S(p) = (C − 1)p + [s = 1]·f₁ is tangent to S.
   - S is a compact C¹ surface: ∇φ_s ≠ 0 on S by Euler. So S is invariant under the flow of Y_S.
4. **C is invertible.** Suppose C were singular.
   - Then A = C − 1 has eigenvalue −1. Let E₋ be its generalized eigenspace and E′ the complementary A-invariant subspace.
   - The E₋-component of the flow is x(t) = x* + e^{A₋t}(x(0) − x*), and it is unbounded as t → −∞ unless x(0) = x*.
   - So the compact invariant S would lie in x* + E′, an affine subspace of dimension ≤ 2.
   - But S contains the points u/φ_s(u)^{1/s} for every unit vector u, which do not lie in a plane. Contradiction.
5. So rank C = 3. ∎

**Checked** (`r184_cross.out:19-24`). The equations were solved for (C, f₁) on four cones: isotropic; tilted with |w| = 0.5; oblique tilt with |w| = 0.88; anisotropic plus tilt.
- Each solution space is 3-dimensional. It contains C = 1 (Euler).
- The smallest σ_min(C) found by sampling each solution space is 1.000, 0.990, 0.780 and 0.683 respectively. This is consistent with rank 3, but a sample, not the proof.

**Remark.** RB-X re-proves R17-8 (ii) uniformly: s = 2 gives A ∈ so(M), i.e. C = 1 + M⁻¹K. It also closes R17-8's massless line, which cited only "the degree count" (`rR17-8:223`).

### 3.4 Corollary (no band in 𝒳 carries redshifting momentum). Proved, given §3.2's RECALLED facts

C is universal, because there is one graviton (`rR17-5:74`).
- If any branch has π ≢ 0, WX (iv) gives rank C ≤ 1.
- RB-X needs rank C = 3 at the IR particle's extremum.
- Hence π ≡ 0 on every branch, and RB fails for every band, as in R17-8 (`vR17-8:39`).
- This holds for standard W2_pf (C = 1) and for every deformed multiplier.
- The bridge-free lattice-translation test fails independently, by determinant winding (`rR17-5:191-195`; counted once).

### 3.5 Probe (b): crossing-band candidates. Checked; no candidate survives

The test is the necessary energy-shell identity t·∇π_x = t_x (C = 1). It is fitted by least squares, as in R17-8 (`rR17-8:230-236`), with ansatz π_+ = A + B|d|, where A and B are full real Fourier polynomials with |n_i| ≤ R. This is exactly the eigenvalue class of every analytic Π = a + b·h. Points with |d| ≤ 0.05 are dropped. Raw relative residuals (`r184_cross.out:8-11`):

| Law | Crossing type | R = 1 | R = 2 | R = 3 |
|---|---|---|---|---|
| Weyl pair, d = (sin k_x, sin k_y, 2 − Σcos) | B | 0.843 | 0.810 | 0.788 (685 fns) |
| tilted Weyl pair (f = 0.3 sin k_z + 0.2 sin k_x) | B | 0.828 | 0.794 | 0.769 |
| PT nodal loop, d = (2 − Σcos, 0, sin k_z) | B | 0.822 | 0.782 | 0.757 |
| folded NN band, branch on the 4π×2π×2π cover | A (with monodromy) | 0.858 | 0.797 | 0.767 (342 fns) |

- These sit at the same level as R17-8's isolated-band floors (0.716–0.769, `rR17-8:231-234`). The slow decrease with R is consistent with WX's positive obstruction. It does not prove a positive L² infimum.
- **Controls, measuring the same observable** (`r184_cross.out:13-17`):
  - **Tower control.** Admitting the non-periodic k_x (continuum or tower momentum) gives a residual of 3.8e-15, with coefficient 1.000000. The test finds solutions where they exist.
  - **One-axis control.** Scaling the Weyl law's transverse terms by δ takes the x-identity residual through 0.786, 2.6e-2 and 4.0e-4 at δ = 1, 0.1 and 0.01. The y-identity stays at 0.77–0.99. A one-axis band absorbs one winding only, as WX (iv) says.
- **Rank C and the redshift test.** Theory gives rank C ≤ 1 (WX), but RB needs 3 (RB-X, block 4). No candidate passes the W2_pf part, so the full redshift test has nothing to run on.
- **The steelman tried and how it dies.** The best-looking escape is a sign-flip crossing. A sorted band's momentum may jump there, so the sorted band's level sets do carry two ψ constants. The folded law is the explicit case. It dies because (i)–(ii) hold on each *branch* over its whole domain, including where it is the other sorted band. The branch is the unfolded band on a 3-torus cover (row 4).

### 3.6 Lemma X1/X2 (𝒳 is the whole two-band class). Proved, modulo RECALLED real-analytic geometry

**The worry.** A sign-flip surface might end on a conical line, so that the branch orientation flips around that line. The branches would then live on a cover of T³ branched along the line, which need not be a torus, and the Reeb bound would fail.

**X1.** Assume d ≢ 0.
- Take a 2-dimensional stratum S of X; real-analytic sets admit analytic stratifications (Łojasiewicz, RECALLED). Near x ∈ S, S = {g = 0} with dg ≠ 0.
- Every d_c vanishes on S, so d = g·d′ locally. Repeat while d′ vanishes on S. Since d ≢ 0, this stops at d = g^m e with e ≢ 0 on S.
- Where e ≠ 0, x is an A-point: n = e/|e|, G = g^m|e|.
- So the non-A points of S lie in the proper analytic subset {e = 0} ∩ S, of dimension ≤ 1.
- 3-dimensional strata would force d ≡ 0. Hence dim(X_* ∪ X_c) ≤ 1. ∎

**X2.**
1. **Points.** 0-dimensional parts of X_* have codimension 3, so a small loop around one is contractible in ℝ³ minus a point. No monodromy.
2. **Lines.** For a 1-dimensional stratum Y ⊂ X_*, take a generic y ∈ Y and a small transverse analytic disc D, with X_* ∩ D = {y}. Monodromy around ∂D is (−1)^(number of sign-flip crossings), since ℓ's orientation flips exactly where d changes sign relative to ℓ.
3. **Factor Δ.** Δ := |d|²|_D is a real-analytic germ in two variables. In the UFD of convergent series (Weierstrass; RECALLED), Δ = Π_i h_i^{a_i}·u, with h_i real-irreducible and each a_i even (Δ ≥ 0, and h_i is reduced, so it changes sign across its regular points).
4. **Local form.** At regular points of {h_i = 0} (dh_i ≠ 0, generic since h_i is reduced), local division gives d = h_i^{m_i}·e_i, with m_i = a_i/2 and e_i ≠ 0. So d flips sign across every half-branch of {h_i = 0} if m_i is odd, and across none if m_i is even.
5. **Count.** The zero set of any real-analytic plane germ has an even number of half-branches (classical; RECALLED). So the number of sign-flip crossings of ∂D is Σ_i (m_i mod 2)·#half-branches(h_i) ≡ 0 (mod 2). No monodromy.
6. **Extension.** For X_* of codimension ≥ 2, π₁(T³ ∖ X_*) → π₁(T³) is onto, with kernel normally generated by meridians (RECALLED). So the orientation cover extends to an unbranched cover of T³. ∎

**Checked** (`r184_cross.out:41-50`). A continuous unit field n ∥ d is tracked around small circles through the sign-flip zeros.
- Monodromy is +1 on 5 hand-picked laws: a line and a cusp of A-points through a conical point, a cubic mixture, a conical-only law, and a Weyl-like law. Flip counts are 2, 2, 0, 0 and 0.
- Monodromy is +1 on 40 random laws (linear form) × (random quadratic + cubic vector). Each has exactly 2 flips.
- **Control:** the non-analytic d = (y, r − x, 0), whose zero set is a single half-line, gives monodromy −1 with 1 flip. The tracker sees an odd case when one exists, and only non-analytic laws produce it.

**What remains outside WX:** N > 2 bands (braids); joint mixing + FD; non-analytic symbols.

### 3.7 Merely continuous multi-shift mixing (the title's second hole). OPEN; one candidate killed

**The local step without Rellich (proved, restating `vR17-8:15`).** Along a lattice line, every nonzero distinct eigenvalue of Π_j that stays separated on an interval is affine there. Analyticity was used only to continue across coincidences.

**My N = 2 gap argument was wrong.** It used affine pieces between coincidences. Kinks at zero eigenvalue defeat it. The counterexample to the argument is γ₁ = c and γ₂ = a triangle wave between 0 and c.

**The natural continuous candidate fails a necessary test.** The candidate is a momentum triangle wave whose turning points touch constant "spectator" branches: spectrum {tri, ±π/2}, with Σ₀(q) = {0, ±q}. It would turn its momentum without a separated kink.
- It fails the forward spectral partner relation (MB-A step 1, which needs no separation) at base points within q of a turning point.
- The defect is q/3 by hand (0.314–0.319 q checked, `r184_cross.out:33-37`). The hand calculation: for t = peak − δ, the best partner misses by min(δ, |q − 2δ|), which is q/3 at δ = q/3.
- R17-8's separated zigzag control fails as well (0.37–0.50 q).
- The intertwiner identity (★), W1 and RB were not run on either.

**No class-wide proof for continuous symbols.** The hole stays OPEN.

---

## 4. Against the FIXED readings (`TESTS:6572-6575`)

**Worker reading: EXCLUDED-CROSS for the stated class, pending the referee (codex gpt-5.6-sol, xhigh).**
- **ESCAPE: not met.** No crossing-band law satisfies the energy-shell identity with nonzero momentum (WX, proved in 𝒳; four laws checked). RB-X excludes the redshift at conical extrema too.
- **EXCLUDED-CROSS.** WX + RB-X + Lemma X1/X2 + the Corollary are offered as the no-go.
  - 𝒳 is every two-band analytic Bloch law with a crossing (d ≢ 0). That contains the stated class, "symmetry-protected crossing surface or line" (`TESTS:6561`): decoupled species, folded (non-symmorphic) bands, PT- or mirror-protected nodal lines, quadratic touchings. It also contains unprotected Weyl points.
  - **Steps resting on RECALLED facts the referee must accept or replace:**
    - the tame Reeb kernel theorem in subanalytic, Lipschitz form;
    - half-branch evenness and the UFD factorization;
    - analytic stratification;
    - meridians normally generating the kernel.
  - If any of these fails, the reading is OPEN, with that step named. It cannot be recorded as EXCLUDED-CROSS until it is refereed.
- **The title's second hole** (continuous multi-shift mixing) has no FIXED reading of its own. It remains OPEN (§3.7).

**Against the expectation.**
- **As expected:** the obstruction is topological, and the branches still live on a 3-torus.
- **Not expected:**
  - The branches live on a *cover* (folded bands), not on T³ itself.
  - At conical points there is no analytic branch at all, and the step survives only because the commuting momentum must be scalar there (Lemma S0).
  - Massless matter sitting on a crossing cone needs rank C = 3 by a flow argument (RB-X), not by a degree count.
- **Removed hypothesis:** isolated bands. **Kept:** analyticity, multiplier shifts, regular linear FD, H-RB, free/symmetric/projectable.

## 5. Round rules (`TESTS:5688-5706`, `:6395-6406`)

- **Whole-zone v_max** (`r184_cross.out:26-31`). The test laws reach v_max 1.46–1.61 (Weyl, tilted Weyl, nodal) and 1.50 (folded), so as written they are superluminal.
  - The test is invariant under h → h/λ: P_⊥ depends only on v̂, and the ansatz is scale-free. So the subluminal rescalings have identical residuals (proved by invariance).
  - No gauge-field symbol is introduced. The graviton enters only through θ.
- **Locality of vertices (Lemma M).** No TT or stress vertex is constructed. The no-go concerns the shift generator. Not applicable.
- **Number-free ≠ forced; Λ mechanisms.** Not applicable.
- **Bounded classes for spectra.** "Gapped" is not used. The laws are gapless at X by construction.
- **Certificates.** No CONFLICT from a relaxation is claimed. The numerics are consistency checks, and the no-go is analytic.
- **Counting conventions.** No tuning count.
- **Self-force.** No frame-tied kernel is introduced.
- **Standard or deformed.** WX and RB-X hold for any C (standard C = 1 and deformed).
- **Physical controls.** The tower and the one-axis band measure the same identity residual (§3.5).
- **Readout bridges.** H-RB is named as a hypothesis on `AX:187`. The bridge-free translation test is counted once.
- **Forks.** The A/B/X_c classification is exhaustive by definition: a point is non-collinear, collinear with factorization, or collinear without. The excluded alternatives are listed in §1, with reasons.
- **Generic GR.** No initial-state or memory claim is made.
- **Changed hypothesis.** Isolated bands.

## 6. Prices (named, not adopted)

- **No new price.** No escape was found in 𝒳.
- **P64 (tower), P90 (discontinuous symbol), P124 (non-canonical shift action).** Unchanged, counted once (`S23:523,565`).
- **Open routes (unpriced):**
  - N > 2 braided crossings;
  - merely continuous multi-shift mixing (§3.7);
  - joint mixing + FD;
  - interactions, non-symmetric couplings, non-projectable lapse.
- **Axiom touchpoints.** H-RB rests on `AX:187` (source/action and observable identification). The free Hamiltonian is not supplied by Admissibility (`AX:116-123`). Nothing here touches Lattice (`AX:37-38`) or Qubit (`AX:47`) beyond the finite-band (N = 2) assumption.

## 7. Strong-word check

- **"Proved":**
  - Lemma S0;
  - the cover construction;
  - WX (i)–(iii) and (iv), given the RECALLED tame Reeb, dimension and stratification facts;
  - RB-X (flow argument);
  - the Corollary;
  - Lemma X1/X2 (§3.6), given the RECALLED real-analytic facts;
  - the §3.7 local step (restated) and the q/3 defect by hand.
- **"Checked":** every number cited from `r184_cross.out`, and the three archive reruns.
- **"Suggested":**
  - the d ≡ 0 doublet remark (§1);
  - N > 2 (not claimed);
  - the tame Reeb theorem in its subanalytic, Lipschitz form is RECALLED, so WX (iv) for laws with conical points is proved only conditionally on it.
- **"No / every / all":** only within 𝒳 and §1's kept hypotheses.
- **RECALLED:**
  - the tame Reeb facts (KMS 2014; Gelbukh 2019);
  - o-minimal/Hardt triviality;
  - codimension-2 sets not separating;
  - analytic stratification;
  - finite covers of T³;
  - convergent power series in two variables form a UFD (Weierstrass);
  - the zero set of a real-analytic plane germ has an even number of half-branches;
  - meridians normally generate ker(π₁(T³ ∖ X_*) → π₁(T³));
  - non-Abelian band topology (Wu–Soluyanov–Bzdušek 2019).

## 8. For the referee

1. **Lemma S0.** Is non-collinearity of the limit set the right condition? Is continuity of π at X_* enough to carry (iii) across X_* by the finite-image argument?
2. **Cover construction and Lemma X1/X2.** Is n̂ analytic on Ω at A-points, up to the sign the cover fixes? Is Ω connected? Is the division and stratification argument for X1 right? Is the half-branch parity argument for X2 right, in particular the claim that the flip parity is constant on every half-branch of an irreducible factor?
3. **WX (iv) for pure-B laws.** Is the tame Reeb kernel theorem valid for the subanalytic, Lipschitz sorted band? Is the "regular level cycles generate" formulation correct when some level components lie inside X?
4. **RB-X.** The flow argument, and the existence of f₁ at a conical extremum.
5. **Scope.** With X1/X2 automatic, 𝒳 contains the stated class (`TESTS:6561`). Is EXCLUDED-CROSS then met, or do the RECALLED facts need independent proof first?

## 9. Files

- `S/r184_cross.py` and `S/r184_cross.out`. Blocks:
  - (1) Lemma S0;
  - (2) energy-shell identity on four crossing laws;
  - (3) controls;
  - (4) the RB-X linear solve;
  - (5) v_max;
  - (6) the continuous-mixing spectral test;
  - (7) orientation monodromy (Lemma X2), with a non-analytic control.
- `S/recheck/R16-5/rerun.out`, `S/recheck/R17-5/rerun.out`: identical.
- `S/recheck/R17-8/rerun_ascommitted.out`: ModuleNotFoundError.
- `S/recheck/R17-8/rerun.out`: identical after supplying `recheck/R16-5/r99_profiles_copy.py`.
