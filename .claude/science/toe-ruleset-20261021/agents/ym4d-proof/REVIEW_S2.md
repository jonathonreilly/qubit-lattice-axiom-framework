# REVIEW_S2: independent hostile review of PROOF_session2_snapshot.md

Reviewer: independent agent (did not write the proof). Inputs: the session-2 snapshot (byte-identical to PROOF.md when
read), the session-1 snapshot, REVIEW_S1.md, LOG.md, and checks c5-c7 (re-run). PROOF.md and both snapshots were not
edited.

**Bottom line.** All 17 PROVEN-HERE items survive. Three need written fixes: L1e (scope), L7.0 (S5 is out of sync) and
L8b (it must cite the off-D extension).
- No PROVEN-HERE argument uses an IMPORTED-NOT-YET-REVERIFIED lemma.
- Every R1 finding is fixed, apart from the S5 sync gap noted below.
- The two substantive new results, L1e and L3s', are correct. I re-derived every inequality and constant.
- **Count caveat:** R3.1 is a promoted session-1 remark, and L3g(a)-block is a standard fact nothing uses. The real new
  content is L1e, L3s' and L9a-m.
- L3g-ob is a sound heuristic and is correctly kept OPEN. The proposed "fix via Dimock" is only partly transferable,
  because Dimock's covariance is abelian-specific (see (2)).

## (1) PROVEN-HERE items

### R1-fix audit (session-1 items)

| Item | Verdict | Notes |
|---|---|---|
| L0 | CORRECT | (iii) now reads D_N for N ≥ 7, which is more precise than R1's suggested wording. |
| L1a | CORRECT | Unchanged. |
| L1b | CORRECT | Fixed: 2 sin(π/6) = 1, so the bound 1 suffices for N ≤ 6. LOG and snapshot now agree. |
| L1c | CORRECT | Fixed: c1(d) is now relabelled as testing log U' vs avg log T_y. |
| L3s | CORRECT, scoped | Scope items (a)-(e) are added as R1 asked. |
| L4c | CORRECT | Fixed: the consequence is softened, and L4a now uses resolution indexing (finer j gives larger 1/g², the AF sign). |
| L7a, L8a | CORRECT | Vacuous, as before. |
| L8c | CORRECT | Fixed: mixed reflection via L9a-m. The off-D extension "set to 1" is θ-covariant: 1⁻¹ = 1, D is θ-invariant, and covariance passes through the iteration by induction. Locality survives because leaving D depends only on the links of the two blocks. |
| L9a' | CORRECT | Unchanged. |
| L7.0 (per K) | CORRECT-WITH-FIXES | See the S5 fix below. |
| L8b (narrowed) | CORRECT-WITH-FIXES | See the citation fix below. |
| L7c | correctly demoted | Now CONDITIONAL on E7.0, and "=" is corrected to "≥". |

**L7.0 fix.**
- The split and E7.0 are right. The threshold τ_N = min(1, 2 sin(π/N)) correctly keeps 3τ_N/4 < 2 sin(π/N).
- **S5 was not updated.** It still says "Fix w* ∈ (0,1)" and tunes the uncut E_K[1 − N⁻¹ Re tr V^(0)_p]. L7.0 tunes
  w̃ with w* < w̃_0(K). Align S5 with L7.0.

**L8b fix.** Reflection invariance needs V^(m)[θU] = θV^(m)[U] everywhere, so cite the off-D extension in L8c(b).

### New items

**L1e: CORRECT-WITH-FIXES (scope).** I re-derived it line by line.

- Recursion: ||T_c − S_b|| ≤ δ_{j+1}s_j²/L (L links); Z_y has ≤ (d+2)L links; the ribbon is correct (γ + s_j e_μ is
  c_Y's axial path by translation covariance and nested roots; ν = μ rectangles telescope to 1; ν ≠ μ grids give
  ≤ |γ_ν|s_jF with |γ_ν| < s_j/2); c = 4 arcsin(1/4) = 1.0107 (ratio increasing); ||e^X − 1|| ≤ ||X||. So
  ρ = (1 + c(d+2))/L.
- The corollary induction closes: (C_A + (d+2)C_δ/L)·F_0 = 1/2. At d = 4, L = 9: ρ = 0.785, C_δ = 7.05, F_0 = 0.081,
  and the coarse curvature is ≤ (1 + 4C_δ)F ≈ 29F.
- N ≤ 12 is right: 2 sin(π/12) = 0.518 > 1/2 > 2 sin(π/13) = 0.479.

**Required fix (scope).** The hypothesis is F ≤ 0.08 in *physical* units, i.e. ||1 − U_p|| ≤ 0.08 ε² at the fine
scale. That describes classical smooth fields such as the backgrounds U(V). It does not describe Balaban's small-field
regime, whose conditions are dimensionless (||1 − U_p|| ≲ p(g_k)·g_k at each scale), so F ~ ε⁻² there. The L1d line
"the k-uniform sup-curvature part of this obligation is now proven" therefore overstates what was shown. The
fine-to-coarse small-field propagation in L1d is untouched. State L1e as a theorem about smooth backgrounds, as L3s(d)
already does.

**R3.1: CORRECT.** Cauchy-Schwarz (block volume 1), (x − y)² ≥ x²/2 − y², and Step 3 with min(2, a/2) all hold; the
Combes-Thomas block part needs only unitary transports. It is a session-1 remark relabelled, not new work.

**L3s': CORRECT.**
- (I): the per-coordinate length is Σ_{i≥1} ((L−1)/2)L⁻ⁱ = 1/2, strictly less at finite k. That gives fewer than
  d/(2ε) fine bonds, all intra-block. Each has ||U^ax − 1|| ≤ (d−1)εF/2. Hence θ_I ≤ d(d−1)F/4 = 3F in d = 4. The
  identity ||W_y − P|| = ||W^ax_y − 1|| holds because g(c) = 1.
- (II): Σ_{i≥1} d((L−1)/2)C_δ L⁻²ⁱ = dC_δ/(2(L+1)), which is 1.41 at L = 9, so C_path' ≈ 4.41.
- With a = 1 and F ≤ F_0: m' ≥ 0.5 − 28.4F² ≥ 0.31 > 0. This is consistent.
- It inherits L1e's smooth-background scope, which L3s(d) already states.

**L3g(a)-block: CORRECT.** The mixed terms of the graded tensor product anticommute, and on 1D C¹, dd* has exactly the
n−1 nonzero Neumann eigenvalues, so λ_min = (4/ε²)sin²(π/2n) ≥ 4 (c6(A) is exact). It is abelian and flat, does not
localise d*, and nothing downstream uses it.

**L9a-m: CORRECT.** On odd side S, x ↦ 1 − x fixes the link plane at 1/2 and the site plane h = (S+1)/2 ≠ 1 for S ≥ 3,
so the gauge fixing at x = 1 misses Π_s. θ fixes the W-links with their orientation. The plaquettes split into in-plane
(h(W) ≥ 0), positive, θ-images and Π_l-crossing; none straddles both planes. Conditional on W the Haar measure
factorises, and the θ change of variables gives |·|² with c_α ≥ 0. S = 3 works. In L8c the block grid is θ-invariant
(Π_s is a block mid-plane), so L9a' applies; "positive half union of blocks" must exclude the block cut by Π_s, so say
so. Not checked numerically (admitted).

## (2) L3g-ob and the Dimock fix

**The mechanism is sound (heuristic, correctly OPEN).** Every complete-axial leg out of c_X starts on the coordinate-1
line through c_X, so averaging over y gives a codimension-3 line functional with O(1) weight.
- Tube capacity ~4πε per unit length gives ||ℓ||²_{H⁻¹} ~ n in d = 4 (log n in d = 3, bounded in d = 2). The
  coordinate-2 legs add an unmentioned codimension-2 sheet (~ log n); harmless.
- ℓ_X is μ-independent, so σ = Σφ(c_X)τ_X cancels Q(dφ) = φ(c_Y) − φ(c_X) for all μ at once. The quotient
  k² + C/(nk²) and T ≳ n^{1/4} are self-consistent; the cross terms are unwritten (stated).
- The spreading caveat is correct: root covariance forces d*J = δ_{c_Y} − δ_{c_X}, so ∫k⁻⁴k³dk ~ log n.
- c6(B') has only 3 points. The increments (0.070, 0.075) favour linear over log, but the pass criterion is lax.

**Dimock, "Covariant axial gauge", arXiv:1410.2798: VERIFIED** (abstract and HTML body read; the published version is
DOI 10.1007/s11005-015-0763-0, i.e. Lett. Math. Phys. 2015). What I could confirm:
- Abelian and single-scale, mainly d = 3 ("weight L⁻⁴" should read L^{−d}). Q sums A over paths parallel to the coarse
  bond, one per fine site, with no centre legs.
- The centre paths appear only in the gauge-fixing operator τ, averaged over coordinate orderings. The gauge fixing is
  δ(τA). Q_kλ = 0 constrains the Faddeev-Popov parameter. Landau uses δ(R_kδ𝒜); Feynman uses exp(−½α⁻¹⟨δ𝒜, R_kδ𝒜⟩).
- The snapshot's quotes about Balaban (tree-averaging; exponential gauge fixing in the YM papers) are accurate.

**Hostile point: the fix only partly transfers.** The covariance Q∂λ = ∂Qλ, with a block-averaged gauge function, is
abelian. A nonabelian covariant map whose coarse gauge group acts at points necessarily linearises to root covariance.
So the log part is unavoidable, by the snapshot's own caveat.
- What transfers: straight legs or spread funnels (these kill the ~n line part), and a Q-adapted gauge term R_k (not
  the plain dd*). This matches the "Revised L3g(a) target", which is correct.
- What does not transfer: "revise S4 toward averaged gauge functions" in the nonabelian setting.
- Dimock's order-averaging acts on τ (the gauge fixing), not on Q. So it is an analogy for repairing L8b, not the repair
  itself. Order-averaging S4 still has to re-prove L1e and L9a'.

## (3) Migdal-Kadanoff toy (c7)

- **It does test** the E7 trajectory-Cauchy form in an exact one-function block map: RC fixes the marginal direction and
  the rest contracts. The rate fits: t is marginal, u → u/p³·b² = u/16, measured 0.0636-0.067.
- **It does not test** locality, polymers, spatial large-field regions or the interface, so it says nothing about
  E7.2/E7.4 in 4D (stated in the text). The "large-field bump" is a pointwise deformation that w^p kills trivially; at
  a* = 0.9 its effect is 1e-15, so that sub-test is vacuous. b0_MK ≈ 0.0457 vs 0.0464 is plausibly accidental (not
  claimed).
- **Process:** the pre-registered spread criterion failed and was replaced. This is disclosed, the first run is kept,
  and the new criterion is sensible. MK exactness for gauge models stays [m].

## (4) Citations

- **Confirmed (web, this review):**
  - Dimock arXiv:1410.2798 (above).
  - arXiv:1406.4177 exists: S. Farinelli, math.GM, which claims a Wightman YM4 with a mass gap. It is correctly NOT
    imported. Treat it as non-credible.
  - Cao-Chatterjee: **CMP 405 (2024), no. 1, art. 3**, DOI 10.1007/s00220-023-04870-y. The "CMP 2024" is now confirmed
    (R1 had left it open).
- **Unchanged from R1:** the Balaban CMP set.
- **Not checked, consistent with my knowledge:** Migdal (1975) and Kadanoff (Ann. Phys. 100, 1976) [m], so add exact
  references; Lüscher JHEP 08 (2010) 071. The Dimock II body claims are plausible and labelled data-only; I did not
  re-verify them.
- **Suspicious or fabricated:** none found.

## (5) Checks re-run

Laptop, BLAS = 1, nice 10, load about 1.8, 34% RAM free. `timeout` is absent on macOS, so each check was timed with
/usr/bin/time.

| Check | Result | Time | Notes |
|---|---|---|---|
| c5 | 17/17 PASS | 22 s | Output identical to c5_out.txt apart from timings. |
| c6 | 9/9 PASS | 44 s | Identical apart from timings. |
| c7 | 4/4 PASS | 1.5 s | Byte-identical. |

Caveats: c5 never instantiates d = 4, L ≥ 9 (every d = 4 case has L = 3, ρ = 2.35), so the corollary rests on the
proof alone, which holds up. c6's first-run FAIL output was overwritten (only the LOG records it); keep first runs.

## Required fixes (summary)

1. **L1e/L1d:** smooth-background scope. Withdraw "k-uniform sup-curvature part of L1d proven".
2. **S5:** align with L7.0 (w̃, w* < w̃_0(K), E7.0).
3. **L8b:** cite the off-D extension.
4. **L8c:** exclude the block cut by Π_s.
5. **Dimock entry:** L^{−d}; abelian-only covariance; order-averaging is on τ, not Q.
6. **Tally:** mark R3.1 as promoted; add Migdal/Kadanoff references.
