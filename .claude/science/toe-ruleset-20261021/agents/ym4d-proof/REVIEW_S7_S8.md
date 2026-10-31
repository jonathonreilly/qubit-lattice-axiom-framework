# REVIEW_S7_S8: independent hostile review of sessions 7 and 8

Reviewer: an independent agent that did not write the proof.

Inputs:
- PROOF.md, byte-identical to PROOF_session8_snapshot.md (checked with `cmp`).
- `diff PROOF_session6_snapshot.md PROOF_session8_snapshot.md` (521 lines), and PROOF.md read by offset
  (l.1-60, 819-1076, 1448-1640, 1655-1676, 2050-2100).
- RTARGET.md; LOG.md sessions 7-8; literature/NOTES.md §11; REVIEW_S5_S6.md.
- checks c18c and c19: criteria files, scripts and outputs. Both were re-run.
- The provenance of the pre-statements, checked against the session-7 and session-8 agent transcripts (tool-call
  timestamps). This was needed because the directory is untracked, so git history is unavailable.

PROOF.md, LOG.md, RTARGET.md, the snapshots and the checks were not edited. Scratch work is in the scratchpad `rev78/`.

**Bottom line.**
- All 9 REVIEW_S5_S6 binding fixes are applied, and applied correctly.
- The six new PROVEN-HERE statements survive:
  - R2D-iso [S7];
  - GT, R4D-iso, W1-def, W1-size and W1-sym [S8]. These are counted as 3 tally items.
- None is WRONG. Three need fixes:
  - R2D-iso: A_B is not a function of the data;
  - R4D-iso: the scope of its consequence;
  - W1-sym: periodicity of the family on the torus.
- The representation theory of Lemma GT is right. Λ²R⁴ is absolutely irreducible under B_4. Over the rotation
  subgroup it splits into the self-dual and anti-self-dual parts, and the reflections swap them.
- Three non-PROVEN statements are defective:
  - **WRONG.** The 2D-wall cost "a = ε_1²/2, a ≤ 2 for any cut" and its corollary "every single-bond cut lies in the
    divergent window for 3 ≤ N ≤ 8". The cheapest excluded configuration costs ≈ ε_1², not ε_1²/2, because the rest of
    the lattice must relax (effective resistance 1/2).
  - **GAP.** The "Consequence" paragraphs and the header line "LF-count's 4D divergence sits entirely in ρ_0". They
    apply a theorem about continuum s-families to lattice RG backgrounds, with no interpolation or regularity lemma.
  - **GAP.** W1-loc as stated. W1-cl demands an extra g^{2q} that is not available. It omits the direct
    Φ_0-dependence of ρ_□. Its family is not periodic on the torus.
- The pre-statements are genuine in file order. RTARGET §0-3, §5-7 and both criteria files were written before the
  corresponding derivation text and the first runs. The separation in time is only minutes; see (6).
- Both checks reproduce exactly. Neither tests a cube integral ρ. c19 lacks the one control that would show the
  reflections are load-bearing.

## [R56-fix] audit (REVIEW_S5_S6 binding fixes 1-9)

| # | Fix | Where | Verdict |
|---|---|---|---|
| 1 | A1-NA(1)(c) by concavity | l.1571-1580 | Applied, correct. f(t) = 1 - cos√t has f' = sin√t/(2√t) ≥ 0, decreasing on [0, π²]. So f(t)/t is non-increasing. Both cases are right. The Σθ_j = 0 remark is right. |
| 2 | Principal branch (-π, π]; coarse side ≥ 3; c_N = c√N | l.1520-1524, 1581-1583 | Applied. c = 4 arcsin(1/4) ≈ 1.011 is the sharp θ/|1 - e^{iθ}| at |1 - e^{iθ}| = ½. Correct. |
| 3 | A1-NA(k) and L1d restricted to S4' iterates; new OPEN L1e-(0.4) | l.279-293, 377-378, 1617-1639, header l.45-46, 52-53, tally | Applied everywhere I checked. |
| 4 | LF-count in one normalisation; "every threshold" made conditional; LOG "iff" | l.814-816, 1662-1673, tally; LOG l.368, l.396 | Applied. Re-computed: ε_1 ≲ 1.16 (SU(2)) and 0.77 (SU(3)). The session-6 LOG line was annotated in place (marked) and the correction was also logged. Acceptable. |
| 5 | A2 corollary restricted to E8** | l.1485-1491 | Applied, with the E8* sentence withdrawn. |
| 6 | A1 supremum not attained; "equal action" quadratic only | l.1450-1453, 1466-1471 | Applied. |
| 7 | L4a-Π phase sign; cite (1.21) | l.722-723, 749 | Applied. |
| 8 | L4a-form torus side | l.695-698 | Applied. |
| 9 | c18b outside the regime; in-regime check added | l.1599-1615 | Applied. The check was added as c18c, not c19; that is immaterial. |

## (1) New PROVEN-HERE items

**Proposition R2D-iso [S7] (l.830-880): CONFIRMED-WITH-FIX.**

Every step was re-derived.

- **Step 1.**
  - Numerator. On {χ = 0} the cut bond alone has (1 - n·n')/g² ≥ ε_1²/(2g²), and every other term is ≥ 0.
  - Caps. |n_x - n(0)| ≤ rg with r = ε_1/4 gives interior bonds ≤ ε_1g/2 < ε_1.
  - Collar. |y|_1 ≤ L for y ∈ Γ (Γ excludes the corners), and |Φ(s) - n(0)| ≤ s(L - 1).
  - Action. 4L crossing bonds plus the constraint give S ≤ C_0 + (4L + κ)L²s²/g².
  - So s_0 = ε_1/(2√B) and the bound ρ ≤ C_1g^{-(N-1)L²}e^{-ε_1²/(4g²)} are right.
- **Step 2.** Faà di Bruno with g ≤ 1 gives (Λ/g²)^q. Positivity and the s-independent indicator give the quotient
  bound. Right. Only q ≤ 4 is needed, and the C⁴ hypothesis supplies it.
- **Step 3.** m_{-y}(s) = m_y(-s) and Φ(-s) = Φ(s), and ι preserves dσ, S and χ. Right.
- **Step 4.** O(N) rotation of the integration variables. Right.
- **Step 5.**
  - Chain rule: ρ''(0) = D²ρ(m', m') + Dρ(m'').
  - The O(N-1) stabiliser forces the gradient ∥ e and the e^⊥ Hessian h(u·v). Reflections in O(N-1) exclude the
    ε-form for N = 3.
  - Φ'(0) = 0, and e·w_μν = -u_μ·u_ν. The signs in T are right.
  - D_4 is absolutely irreducible on R², so T_sym ∝ 1.
- **Steps 6-7.** The matching δβ = c/b is right. The bounds are right; the polynomial g-loss is absorbed by taking
  a < ε_1²/4.
- The target was met as pre-stated: same quantifiers, same a, g-independent s_0.
  - The proof allows N ≥ 2, where the target has N ≥ 3. That is more general, which is harmless.
  - The target writes 0 ≤ s ≤ s_0; the proof gives |s| ≤ s_0.
- **Fix (l.834, l.867).**
  - B := "the nearest-neighbour bonds of □ ∪ Γ" includes bonds with an end inside □. There the "background" m does not
    exist, so A_B(m(s)) = ½Σ_B|n(sy) - n(sy')|² uses the continuum interpolant n.
  - RTARGET §2 pre-stated A_B(m) as a function of the data. The counterterm must also be a function of the
    variables that the effective action depends on.
  - Remedy: take B = the Γ-Γ bonds, i.e. the L - 1 bonds along each side, which gives b = 2(L - 1) per direction. B is
    still D_4- and ι-symmetric, and steps 6-7 go through verbatim.
  - The natural RG choice is a block-lattice bond set in Φ, as W1-sym already does.

**Lemma GT [S8] (l.915-955): CONFIRMED.**

- **Step 2 (lattice data of a continuum radial A).**
  - x^μA_μ = 0 gives A(0) = 0 and ∂_(μA_ν)(0) = 0, so ∂_νA_μ(0) = ½F_νμ(0).
  - A^{(s)} = O(s²). The first Magnus term is ½x^νF_νμ(0), because the e_μ-component of the path integrand meets
    F_μμ = 0.
  - Radial segments from 0 have transporter exactly 1 for all s, not only at order s².
  - Path-ordering corrections are O(s⁴).
- **Step 3.** DF̃(0) is a diagonal-Ad-invariant functional, so each component is an Ad-invariant element of su(N)*,
  hence 0. Faà di Bruno with X'(0) = 0 gives f' = f'' = f''' = 0 and f^{(4)}(0) = 3D²F̃(X'', X'') = 12D²F̃(𝓛Φ, 𝓛Φ).
  Right.
  - The step uses only constant gauge transformations.
  - Linear invariants of the D D F type are killed by the same DF̃(0) = 0. So the s⁴ coefficient depends on F(0)
    alone.
- **Step 4.** ι*A(x) = -A(-x) is radial, and A^{(-s)} = ι*(A^{(s)}). Right. ι ∈ B_4.
- **Step 5, checked independently.**
  - R·A := RA(R^{-1}·) is radial, since (R^Tx)·A(R^{-1}x) = 0. Its curvature at 0 is Λ²(R)F(0). Under R, links map to
    links, with inversion when Re_μ = -e_ν. This is the data action under which (ii) must hold.
  - Λ²R⁴. The sign group acts on e_μ∧e_ν by the character ε_με_ν. The six pairs give six distinct characters, so the
    commutant is diagonal. S_4 is transitive on the pairs, so the commutant is scalar. So Λ²R⁴ is absolutely
    irreducible under B_4.
  - Over B_4 ∩ SO(4) the character norm is 2: two inequivalent irreducibles, the self-dual and anti-self-dual parts.
    det = -1 elements anticommute with the Hodge star and swap them. This is why the reflections are needed.
  - c19 P1 confirms 1 and 2.
  - (V ⊗ W) commutant for G_1 × G_2 = End_{G_1}V ⊗ End_{G_2}W = R. So Q = c Σ||Φ_μν||².
- **Step 6.** Lagrange remainder at order 6, with f^{(5)}(0) = 0 by evenness. Right.
- **Constant uniformity.** GT itself only asserts the bound with sup|f^{(6)}|. Uniformity in A comes from R4D-iso
  step 3, where C_j(L) depends only on ||∂^αA|| ≤ 1 (|α| ≤ 6) and the size of the data region. Right.
- **Lattice point (not a defect of GT, see the GAP in (3)).** GT is a statement about the family D(s) generated by a
  continuum A. Every hypothesis is on that family. The theorem is fine as stated.
  - Radial-gauge A is A_μ(x) = ∫_0^1 t x^νF_νμ(tx) dt. So the hypothesis is really a bound on F and its covariant
    derivatives, which is gauge-covariant. That is in its favour.

**Proposition R4D-iso [S8] (l.956-1001): CONFIRMED-WITH-FIX (scope only).**

- **Step 1.**
  - A gauge transformation at every touched site, including the interior sites 0 and the boundary sites of □, is
    absorbed by Haar invariance of the interior links.
  - The words U(Γ)U([x,x'])U(Γ')^{-1}V(c)^{-1} are closed at 0.
  - The B_4 symmetry of "all orders, both ends" holds.
- **Step 2.**
  - (B): 1 - N^{-1}Re tr U = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).
  - Balls of radius ε_1g/8 make every interior plaquette ≤ ε_1g/2.
  - ||D_b - 1|| ≤ C_Ls² with C_L = O(L²): the V(c) of length L lie at |y|_1 ≤ L, and the Γ' links lie at |y|_1 ≲ 3L.
  - 1 - N^{-1}Re tr W ≤ ½||1 - W||²_op is right: average the eigenvalues of 1 - cos θ = ½|1 - e^{iθ}|².
  - s_0 = (ε_1²/(4NB))^{1/4} is g-independent. Correct.
- **Steps 3-5.**
  - c_B = n_B/(2N), since -N^{-1}Re tr(Y²/2) = ||Y||²_HS/(2N) and tr Y = 0.
  - The test connection ½x^μF⁰_μν with a single F⁰_12 = T is radial and abelian, with F = F⁰ and Σ||F||² = 2.
  - g^{-p-12}. All right.
- The result is as pre-stated, with the same a < ε_1²/(4N), s⁶ remainder, and R4-F1..F4 avoided.
- **Fix (scope).** The proof is correct. The paragraph after it (l.993-997) and the header (l.9-10) are not: see (3).
  "LF-count's 4D divergence sits entirely in ρ_0" must carry "for isolated cubes on smooth s-family backgrounds; the
  application to lattice RG backgrounds needs BG-reg (new OPEN)".

**Lemma W1-def [S8] (l.1015-1022): CONFIRMED.**
- S = S_□ + S_rest, with S_rest independent of n_□ (crossing bonds only join □ to Γ). Fubini gives
  Z^rel/Z^cut = 1 + ⟨ρ_□⟩_cut.
- The derivative formula ∂_{Φ_c}⟨ρ_□⟩ = -(κ/g²)Cov(ρ_□, Φ_c - avg_c), c ≠ □_0, is right.
- Higher Φ_c-derivatives are pure cumulants (times (-κ/g²)^q), because ∂²S/∂Φ_c∂Φ_c' = (κ/g²)δ_cc' is constant. It
  is worth stating this, since W1-red relies on it.

**Lemma W1-size [S8] (l.1023-1029): CONFIRMED.**
- On E^c: crossing bonds ≤ (1/g²)(r²g² + δ_0²), and the constraint ≤ (κ/g²)(δ_0² + r²g²). So
  (4L + κ)δ_0² = ε_1²/4, which gives e^{-ε_1²/(4g²)}.
- On E: ⟨ρ1_E⟩_cut = Z^rel[□_0 large, E]/Z^cut ≤ P_rel(E)(1 + ⟨ρ⟩_cut).
- The rearrangement is right, given P_rel(E) < 1.

**Lemma W1-sym [S8] (l.1030-1045): CONFIRMED-WITH-FIX.**
- The calculus is right:
  - Faà di Bruno with |Φ_c^{(j)}| ≤ |c|_1^j against e^{-κ_d max|c_j|}: summable and T-independent.
  - Evenness, the vacuum part and the stabiliser analysis.
  - D_4 absolute irreducibility.
- **Fix.** On the block torus, the family Φ_c(s) = n(sc) over the representatives |c_μ| ≤ (T-1)/2 is not periodic.
  Across the seam, |Φ_c - Φ_c'| can be O(sT). The family then leaves D_reg(ε_0) for sT ≳ ε_0, and hypothesis (iii)
  "on the family" cannot be supplied by W1-loc there.
  - Remedy: restrict to n that are constant outside a ball of radius R_0 (so that sR_0 < T/2 keeps the seam constant),
    or to T-periodic n(s·).
  - The lemma as a calculus statement is unaffected. Its use in W1-red is affected.

## (2) RTARGET §0 and the 2D wall (non-PROVEN, but carried into the header l.28, L5 [S7] l.823 and LOG)

**The 2D wall arithmetic is right.** Divergence for aβ' ≤ 2 is the LF-count proof with exponent 2. The rate is right:
d(1/g²)/d ln μ = (N-2)/(2π) for S = (1/2g²)∫(∂n)². (N-2)/π ≤ 2 ⇔ N ≤ 8.28, given the stated a.

**WRONG: the cost a.** "Cost of the cheapest excluded configuration for a single-bond cut: a = ε_1²/2, and a ≤ 2 for
any cut (antiparallel bond)" (RTARGET l.15-17, PROOF l.823).
- ε_1²/2 is the cut bond's own term: a lower bound on the action of an excluded configuration. A divergence argument
  needs w_k ≥ e^{-a/g²}, which requires an upper bound on the cheapest cost. The text used the wrong direction.
- If x and x' differ by ε_1, every other path between them must carry the same difference.
  - Linearised minimum: ½ε_1²/R_eff, with R_eff = 1/2 between neighbours of Z². So a ≈ ε_1².
  - Re-computed in `rev78/reff.py`: cost/ε_1² = 1.0115, 1.0007 and 1.0001 on 11², 41² and 101² boxes with pinned
    boundary. A frozen collar raises it further.
- For an antiparallel bond, the rest of the network must also carry geodesic angle π. The heuristic cost is
  2 + π²/2 ≈ 6.9, not ≤ 2.
- Corrected window, linearised: aβ' ≤ 2 ⇔ ε_1² ≲ 4π/(N-2).
  - "Every cut ε_1 < 2" then holds at most for N ≤ 5 (linearised).
  - With the ≈ 6.9 near-antipodal estimate it is only plausible for N = 3.
  - "3 ≤ N ≤ 8" is wrong. The N ≥ 9 bound (8π/(N-2))^{1/2} should read ≈ (4π/(N-2))^{1/2}.
- The qualitative conclusion survives for small ε_1: the wall is present in d = 2, by the same mechanism.

**O(3) instanton marginality ("from memory"): CONFIRMED, with a caveat.**
- ∫(∂n)² ≥ 8π|Q| gives S ≥ 4π|Q|/g². Then aβ' = 4π/(2π) = 2 = d: marginal. This matches the known UV log-divergence of
  the small-instanton gas (Lüscher, NPB 200 (1982); the reviewer agrees from memory, not re-read).
- Caveat: with the standard lattice action, lattice-scale Q = 1 configurations ("dislocations") have action below the
  continuum 4π [m, Berg-Lüscher 1981; not re-read]. On the lattice, aβ' < 2 strictly, so the divergence is
  geometric, not marginal. Add this.
- The 4D product aβ' = 11N/3 > 4 is right.

**Literature (§11).** The CMP 198 reclassification and the Kopper quote are tagged [read-abs]/[read-skim]. They were
not re-fetched in this review and are not load-bearing for any PROVEN item.

## (3) Scope GAPs in non-item statements

**GAP: background regularity, and the "Consequence" paragraphs (l.874-880, l.993-997, header l.9-10, LOG).**
- R2D-iso and R4D-iso are theorems about backgrounds that are the lattice data of a continuum field n or A with
  |∂^α| ≤ 1, rescaled by s. The summation "a level-j cube against a level-k background has s = L^{-(k-j)}" applies
  them to actual RG backgrounds, which are lattice fields.
- A lattice small-field background (|F_p| small, or |n_x - n_x'| small) is not the s-rescaled data of a smooth field
  with bounded 4 or 6 derivatives. The small-field condition gives no derivative bounds.
- So two things are needed for the consequence:
  - (a) a lattice interpolation lemma: lattice data on the data region ↔ a smooth A, with ||∂^α A|| controlled by
    lattice covariant differences of F;
  - (b) derivative bounds for the level-k background in level-k units: Balaban's minimiser regularity, i.e. L2,
    IMPORTED-NOT-YET-REVERIFIED.
- The same conflation appears in W2's description (l.887-889): "covers only cubes whose coarse neighbourhood is
  small-field". It actually covers only cubes whose background is a smooth s-family.
- Fix:
  - new OPEN item **BG-reg** = (a) + (b);
  - tag the two Consequence paragraphs and header l.9-10 "[conditional on BG-reg, hence on L2]";
  - in W2, replace "small-field" by "smooth s-family".
- This is the 4D analogue of what Balaban gets from CMP 102/109 regularity, so it is not a new wall. It is an
  unstated premise.

**GAP: W1-loc / Corollary W1-red as stated (l.1046-1054, tally l.2057-2059).**
1. **Overstrong W1-cl.** W1-cl requires joint truncated correlations ≤ C_q e^{-a/g²}(g²/κ)^q.
   - The natural size of Cov(ρ_□, Φ_c - avg_c) is O(⟨ρ⟩)·(decay), with no g² gain. By Gaussian integration by parts,
     Cov ≈ Σ_y⟨∂_{n_y}ρ⟩C(n_y, X_c), with C ~ g²/κ and ∂_{n_y}ρ ~ ρ/g², because S_□ carries 1/g².
   - As stated, the target is probably unattainable.
   - It is also unnecessary: W1-sym(iii) tolerates any polynomial g-loss, which is absorbed by a' < a.
   - Restate W1-cl as ≤ C_q g^{-p_q} e^{-a/g²} e^{-κ_d max_j|c_j|_1}.
2. **Missing terms.** ρ_□ depends on Φ_0 directly. Derivatives of F = log(1 + ⟨ρ_□⟩) with some c_j = 0 therefore
   produce ⟨∂^k_{Φ_0}ρ_□; X_{c_1}; …⟩, which W1-cl does not cover.
   - |∂^k_{Φ_0}ρ_□| ≤ C(Λ/g²)^kρ_□, by the R2D-iso step-2 argument, gives the q = k bound.
   - The mixed truncated correlations of ∂^k_{Φ_0}ρ_□ must be added to W1-cl.
3. **Seam.** W1-loc's family Φ(s) has the torus-seam problem of W1-sym. Fix as there.
4. **Header overclaim (l.13-16).** "The exact remaining wall is W1-loc" holds only for the weak, single-defect form,
   and only with 1-3 applied. The strong form (W1-a/b) also needs a multi-defect polymer expansion in a non-ultralocal
   sea (W1-F3). That is not an OPEN item; it stays inside L5.
   - Say "the exact remaining wall for the weak form".
5. W1-LD needs s_0 ≲ δ_0 = ε_1/(2√(4L + κ)). Otherwise the neighbouring Φ_c alone push the collar into E. W1-loc
   allows s_0 to be chosen, so this is consistent, but state it.

**Bookkeeping (header l.13 vs tally l.2053).** The header says three W1 lemmas are PROVEN-HERE; the tally counts one
item. The tally sentence explains this. Make the header say "(counted as one item)".

## (4) Status labels

- No PROVEN-HERE item uses an IMPORTED-NOT-YET-REVERIFIED lemma as a premise.
  - GT's "cf. CMP 109 (4.14)" is a cross-reference only; the semisimplicity argument is self-contained.
  - "Fock-Schwinger", "Haar balls ≥ c_Nδ^{N²-1}" and "smooth dependence of transporters on s" are elementary and
    correctly tagged.
- The violations are in the consequence lines, (3): they use L2-type regularity without saying so.
- L5 stays IMPORTED-NOT-YET-REVERIFIED. Correct.

## (5) Checks re-run

Setup: laptop, nice 10, OMP/OpenBLAS/MKL/vecLib threads = 1, load 2.2-2.3, 38% free memory, sequential runs, no
`timeout`. Outputs are in the scratchpad `rev78/`.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c18c | 16/16 PASS | 0.94 s | 69 MB | identical except the runtime line |
| c19 | 10/10 PASS | 17.8 s | 63 MB | byte-identical |

**c18c: CONFIRMED-WITH-FIX.**
- Pre-registered: criteria 12:16:12 UTC, script 12:16:59, single run 12:17:06.
- The setting is in the lemma's regime: HS norms, principal log, coarse side ≥ 3, fine φ ≤ 0.022, coarse ≤ 0.13.
- Criterion (c) is meaningful. It fails only if the leading constant is not the abelian one. The data show
  |R_log - R_ab| = O(φ²).
- But it does not stress the lemma's inequality:
  - R_ab/L^{4-d} = 0.79 and 0.51;
  - (a)'s threshold of 0.5 is passed by 0.5075 in d = 3;
  - C_rep = 0.
  This is disclosed (l.1611-1614).
- Fix (l.1607): "the largest available on these tori" is unverified; no scan was done. Delete it or support it.

**c19: CONFIRMED-WITH-FIX.**
- Pre-registered: criteria 12:35:10, script 12:37:51, first and only run 12:38:51.
- The background really is in radial gauge: A_ν = x^μΩ_μν with Ω antisymmetric, and F(0) = 2Ω⁰.
- The self-dual and anti-self-dual projections are correct.
- P3-P10 are implemented as written. P5 (c universal across self-dual, anti-self-dual and generic backgrounds, to
  ≤ 5e-8) is the real test of "one invariant".
- **Undisclosed deviation.** At 12:38:38, before the first run, the script was edited.
  - The edit removed a stray line and replaced sampled B_4 elements by generators (an improvement).
  - It also cut the random Ad elements from the pre-registered 20 to 5.
  - This is mathematically harmless: 5 generic elements generate a dense subgroup, and the null-space gap is
    6.6e14.
  - But it deviates from the criteria file and is not disclosed. Disclose it.
- **Missing control.** No control is invariant under B_4 ∩ SO(4) but odd under reflections. Example: a clover
  ε^{μνρσ}Re tr(U_{μν}U_{ρσ}) density.
  - Such a function would give c_SD ≠ c_ASD. That is the one failure mode (R4-F2) the reflection hypothesis is there
    to exclude.
  - The present controls break B_4 entirely, so they do not isolate it. P1's "rotation subgroup: 2" covers it at the
    rep-theory level only.
  - Add this control.
- Neither check evaluates ρ itself. That is stated (l.1000-1001).

## (6) Pre-statement provenance (RTARGET and criteria)

The directory is untracked, so git is uninformative. Tool-call timestamps from the two session transcripts (UTC):

- **Session 7.**
  - 12:19:11: "Now the pre-stated target, before any derivation."
  - 12:19:45: RTARGET §0-4 written.
  - 12:20:45: one edit to §3. (F2) was reworded: the 4D analogue was clarified as "a second marginal-order term". It
    clarifies, not weakens.
  - 12:21:52-12:22:10: R2D-iso drafted and inserted into PROOF.md.
- **Session 8.**
  - 12:25:40-12:33:31: reading.
  - 12:34:21: §5-7 appended.
  - 12:34:36: the disclosed typo fix (a "|Φ_c| = 1... replaced by" artefact).
  - 12:35:10: c19 criteria.
  - 12:44:06-12:44:46: GT, R4D-iso and W1 inserted into PROOF.md.
  - 12:45:18: §8 outcome pointers appended. Section 8 is marked as added afterwards.
- The LOG claims are consistent with this: targets came first in file order, and no section 0-3 or 5-7 text was
  edited after the derivations were inserted.
- Two caveats:
  - The separations are 2-10 minutes. Pre-statement is a file-order fact, not evidence that no derivation preceded
    it in the author's reasoning.
  - One deviation: the RTARGET §2 counterterm A_B(m) was implemented in a non-data form; see the R2D-iso fix.
- The targets were not quietly weakened. The isolated-cube, frozen-exterior, smooth-family and soft-constraint
  restrictions were all pre-stated as "not success" (W1-W3).
- The weak form of §5 is ambiguous as pre-stated. Its formula F = log Z - log Z_{χ_0=1} uses the full Z, but the
  parenthesis says "all other cubes cut". The proof adopted the easier reading, all others cut. Record this.

## (7) Strategy

**Progress.** Sessions 7-8 are real progress on L5's quantitative core, which REVIEW_S5_S6 said was untouched.
- R2D-iso and R4D-iso, with GT, are correct theorems.
- They show that the isolated-cube large-field weight renormalises:
  - a background-independent vacuum part;
  - one marginal coupling shift, with no relevant term and no second marginal invariant;
  - a remainder with α = 2.
- The 4D symmetry argument is clean and checked.

What remains is exactly the hard part of Balaban's CMP 116/122:
- localisation in a fluctuating sea (W1);
- nested scales (W2);
- the hard constraint (W3);
- plus BG-reg, newly named here.

**Verdict on the next target: W1-loc, restated, in 4D form, after two short items. Not W2, and not W3 until decision 4.**
1. **L1e-(0.4) first.** It is short (a two-axial-path ribbon, C_A → ~2C_A). It unblocks the A1-NA(k) readings and
   decision 4.
2. **BG-reg.** Write it, at least as a precise conditional on L2's minimiser regularity. Without it, neither
   Consequence paragraph applies to an RG background.
3. **W1-loc, restated per (3).1-3.**
   - Do not invest in the 2D sea clustering (W1-cl in 2D). The literature already says the full-lattice 2D O(N) UV
     problem was open beyond the hierarchical case (NOTES §11). The 2D testbed has no template, and its W1-cl is
     plausibly harder than the 4D one that Balaban did.
   - Take W1-LD (collar large deviations) as the size half. It is the most tractable piece. It needs a stiffness
     estimate for the non-convex cut sea, so Brascamp-Lieb does not apply directly.
   - Take W1-cl in 4D through the Dimock-I route: random-walk-expanded covariance, ultralocal measure, then
     polymers with a defect. This simultaneously answers W1-F3.
4. **W2** needs the W1 machinery. Pre-stated only; keep it there.
5. **W3** depends on decision 4: soft constraint vs Balaban's δ(M(U)V^{-1}). That is an owner decision. Do not attack
   W3 before it is made.
6. **CMP 122 remains decisive** for W1/W2. Keep it first in the owner request.

## Required fixes (binding for session 9)

1. **2D wall cost (RTARGET l.15-17, PROOF l.823, header l.28, LOG session 7).**
   - Replace a = ε_1²/2 with "a ≈ ε_1²/(2R_eff) = ε_1² (linearised, R_eff = 1/2 on Z²); the bond term ε_1²/2 is a
     lower bound only".
   - Delete "a ≤ 2 for any cut".
   - Replace "every cut for 3 ≤ N ≤ 8" by "every ε_1 ≲ (4π/(N-2))^{1/2} [linearised; inference on the one-loop rate]".
   - RTARGET §0 is a pre-statement, so annotate it with a marked [R78-fix] rather than rewriting it.
2. **O(3) marginality (same places).** Add the lattice-dislocation caveat: on the lattice aβ' < 2, so the divergence
   is geometric there [m].
3. **R2D-iso, B (l.834, 867).** Take B ⊂ Γ-Γ bonds (b = 2(L-1)), or a block-lattice set, so that A_B is a function of
   the data, as pre-stated.
4. **BG-reg (new OPEN).**
   - Tag l.874-880, l.993-997 and header l.9-10 "[conditional on BG-reg, hence on L2]".
   - Define BG-reg = lattice interpolation plus level-k derivative bounds.
   - Correct W2's "small-field" to "smooth s-family" (l.887-889).
5. **W1-loc (l.1049-1054, tally l.2057-2059).**
   - Restate W1-cl with C_qg^{-p_q} in place of (g²/κ)^q.
   - Add the Φ_0-derivative terms of ρ_□.
   - Make the family periodic or constant near the seam, in W1-sym, W1-red and W1-loc.
   - State s_0 ≲ δ_0 for W1-LD.
   - State that higher Φ_c-derivatives are pure cumulants, because the constraint Hessian is constant.
6. **Headers.**
   - l.13-16: "exact remaining wall for the weak (single-defect) form; the strong form also needs a multi-defect
     expansion in a non-ultralocal sea (W1-F3, inside L5)".
   - l.13: W1-def, W1-size and W1-sym are "counted as one item".
   - l.9-10: add "on smooth s-family backgrounds".
7. **RTARGET §5 weak form.** Record in §8 that the weak form was read as "all other cubes cut", not as the full Z.
8. **c18c (l.1607).** Remove or support "the largest available on these tori".
9. **c19.**
   - Disclose in PROOF l.1002-1013 that the pre-run edit reduced the random Ad elements from 20 to 5 and switched to B_4
     generators.
   - Add a rotation-invariant, reflection-odd control (e.g. a clover εFF density) as c19b. Its pre-registered
     criterion: c_SD ≠ c_ASD by > 10%.

**Count.**

New PROVEN-HERE statements: 6, counted as 4 tally items (R2D-iso, GT, R4D-iso, W1-sym incl. W1-def/W1-size).
- 3 are CONFIRMED: GT, W1-def and W1-size.
- 3 are CONFIRMED-WITH-FIX: R2D-iso (B not a data function), R4D-iso (scope of the consequence only) and W1-sym (torus
  seam).
- 0 are GAP and 0 are WRONG.

Non-item statements:
- 1 WRONG: the 2D-wall cost a = ε_1²/2, "a ≤ 2", and "3 ≤ N ≤ 8".
- 2 GAP: BG-reg, i.e. the Consequence paragraphs and header l.9-10; and the W1-loc statement.
- Fixes for c18c/c19 and the headers.

The REVIEW_S5_S6 fixes: 9/9 applied correctly.

**Corrected tally.** 43 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / **24** OPEN.
- The added OPEN item is BG-reg.
- W1-loc stays OPEN, restated per fix 5.
- R2D-iso, GT and R4D-iso are now reviewed.
