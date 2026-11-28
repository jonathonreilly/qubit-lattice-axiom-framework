lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 13:50:47 UTC 2026, pinned at commit 544e6dffb. Author only, checked by no one.

# FINISH row 1688: how the Riemann hypothesis fell, as strategy, and what it gives (PUR-io)

Credit. The proof is by Levent Alpoge (with Claude). The explainer is by Michael Rubinstein.
This file reads both as sources. It ports no step of them.

## Plan (save protocol; steps are written below as they finish)

0. Read library/gap-purity-crux-card.md and the Lean files it cites. Restate the target.
1. Part 1 (closed folder): read explainer Part I (lines 144-1330) and the census (from line 12885). List the strategic moves.
2. Part 2 (closed folder): the (PUR-io) analogue of each move and of the whole chain.
3. Part 3 (Phase 2): read rows 1481-1487 and the registry. Mark each candidate new or on file.
4. Part 4: rank three candidates, first buildable component each, or the obstruction.
5. RESULT line.

Status: all steps written. Parts 1 and 2 were written before any lane file outside the crux card and the cited Lean files was opened. Two wording repairs made to Part 2 in Phase 2 are marked where they stand.

## 0. The target, restated for this file

Sources read for this section: `library/gap-purity-crux-card.md` (in full), `lean/gapchain/GapChain/Purity.lean` (in full), `Transfer.lean` L505-L560 and L690-L720, `Stage0.lean` L60-L80 and L140-L160, `PurIo.lean` (declaration list only).

Notation. n is the side of the spatial cube, u = n/512, T is the Wilson transfer operator at β, P₀ is the average of the eight centre translations. The transfer kernel is exp(−β·(action ≥ 0)), averaged over the vertex gauges (CITED: `Transfer.lean` L548-L552, `transferKernel_le_one` L702). With the top eigenvalue normalised to λ_0 = 1 and neutral eigenvalues λ_i in [0,1], put

    M(t) = Σ_i λ_i^t,   purity(t) = M(2t)/M(t)^2.

Three facts used below.

- (F1) CITED (Lean source `Purity.neutralTailLE_of_purity`, L72-L93, read; I did not run Lean): purity(u) ≥ 2/3 gives M(u) − 1 ≤ 1/2. The proof is M(2u) ≤ M(u), so purity ≤ 1/M(u).
- (F2) ARGUED: the target is an UPPER bound for a sum of positive terms, the excited weight Σ_{i≥1} λ_i^u. It is needed on an infinite set of cutoffs only.
- (F3) ARGUED (standard thermodynamics, not a proof step): log M(u) = (n/u)^3 · [p/T^4] at temperature T = 1/u in units of the box. A free massless gas has p/T^4 = const > 0 (π²/45 for a photon). Then log M(u) is about 0.22 · 512^3. So the target fails for weak 4D compact U(1) by a factor of about 10^8 in the exponent. The target asks that p/T^4 at T = 512/ℓ is below about 2·10^-9.

## Part 1. How the Riemann hypothesis fell: the architecture as strategic moves

Sources: Rubinstein's explainer `zeta-paper_v2.tex`, Part I, L144-L1330 (read in full) and the census, L12885-L13602 (read in full; table rows read for groups A-D, group text and summary for E-L). Alpoge's announcement `remark.pdf`, 4 pages, read in full. Line numbers are of the .tex file. All statements about the proof are CITED from these two sources. I checked none of the mathematics. The explainer itself says that the main inequality (M) is quoted from the Lean development and is not proved in the paper (L221-L223, L1296-L1299).

One-sentence architecture. A spectral statement (no zero right of the line) is turned into a one-sided bound for one positive smoothed count on a sparse set of long intervals; that bound comes from Chebyshev's rigid comparison "what divides an object is at most its size", run on a designed object (a chain of about √x theta lifts between lattices) whose divisibility is smooth, whose size is known exactly through the term linear in the order, and whose leftover defects are each repaired by one separate device.

The moves. Each is written as a pattern that does not mention number theory.

**M1. Turn the spectral claim into a one-sided bound for one positive statistic, on a sparse set.** RH follows from G(x) ≤ x^(1/2+ε) for a smoothed prime count G, on intervals [Y, Y^(3/2)] with Y arbitrarily large (L160-L164, L285-L309, L340-L344). Positivity does the work: Landau's theorem says that a transform of a function of one sign has its first singularity on the real axis (L291-L303). The statistic is chosen so that its kernel is the one the later construction produces (L672-L673: "This is where the smoothing in the definition of G comes from").
Pattern: state the goal as an upper bound for a positive sum; ask for it only infinitely often; choose the test function last, to fit the tool.

**M2. Find one rigid inequality that always points the needed way.** If Δ is a nonzero integer and p^e divides Δ, then Σ e_p log p ≤ log|Δ| (L346-L362). "Divisibility is a statement about each prime separately; size is a statement about the real numbers. The inequality is the bridge, and it always points the same way" (L357-L360). In the proof the integer becomes a map of lattices and the inequality becomes the slope inequality e log p ≤ log‖T‖ + μ_max(M) − μ(L) (L933-L946). For algebraic numbers the bridge is the product formula, and only the average over embeddings is controlled (L581-L589).
Pattern: two descriptions of one object, a local one (many independent places) and a global one (one real size), joined by a conservation law plus a one-sided local bound.

**M3. Say exactly where the classical method stalls, then write a wish list.** For Δ = n! both sides are exact, but the floor functions contribute an error as large as the linear term (L364-L374). The wish list (W1)-(W3): smooth exponents, size known far below the linear term, all primes reached (L376-L386). "No single integer does all three" (L384).
Pattern: locate the loss at the level of an order of magnitude (here: the linear term). Specify the object by its properties before any object is known.

**M4. Take a toy that has one wished property, and list its defects by name.** The lemniscate numbers have smooth exponents at inert primes (L388-L452). Three defects remain, "and each drives a part of the real proof" (L454): (D1) rounding costs the whole linear term; (D2) only half the primes appear; (D3) the size is off by a factor 2 in the leading term, so the inequality is "true and useless" (L455-L463).
Pattern: a true and useless inequality is the right starting point, if the loss is itemised.

**M5. Repair the leading term first: change the object until both sides agree to leading order.** Size is measured by a squared Gaussian norm, ‖z^a‖² = a!, so the squared size is about a! and not (a!)² (L559-L578). Then both sides are a log a + O(a), "the leading terms now agree, and the comparison has become a statement about the terms of order a" (L591-L598). The simplest theta function has the right size and the wrong divisibility; the lemniscate sine has the reverse; having both at once "is the deepest local statement in the argument" (L551-L556).
Pattern: make the leading terms cancel identically, by the choice of normalisation, before estimating anything.

**M6. Kill the discrete loss by a huge free parameter, and let a second parameter make the cut-off.** Order a ≈ x·b and weight w ≈ b with b = exp(x^ε). The exponent becomes (a/p^h − w)_+ = w·(x/p^h − 1)_+ (L649-L662). Each prime power below x contributes b times its ramp value, so the rounding is invisible after division by b (L669-L675). The subtraction of w has an elementary source: a minor absorbs one derivative per direction (L625-L636). The size of b is forced by a second need (integer weights at the other places, L677-L685).
Pattern: amplification. A loss of O(1) per item is harmless when every item is made to count b times. The price is that every other error must also be divided by b.

**M7. Remove what the object cannot see by an auxiliary family, at a separated scale, and need one good member only.** The object sees only inert primes, so the sum is "ζ minus L(χ_d)" (L687-L700). Auxiliary primes q, d are astronomically larger than x; the twisted sums are small for most pairs by a mean-square estimate over the family, and "one only needs one good pair" (L887-L897). It "is not circular, for a reason of scale" (L887-L889). Unwanted cells of the table are pushed to an enormous scale where unconditional theorems hold (L834-L841). Averaging over translates removes the dependence on the cell (L843-L852).
Pattern: when the tool reaches only a twisted version of the target, choose the twist from a large family so that the correction is provably small on average; push every unavoidable side term to a regime where known theorems apply.

**M8. Get the size through the linear term by exact formulas, and check that the same constants appear on both sides.** The linear term is computed exactly from the Gaussian integral, a period formula (Kronecker; Chowla-Selberg), the mass formula and the Weyl dimension formula (L181-L188, L954-L979). "That the two sides produce the same linear term is the reason the method can work at all" (L974-L976). "After an exact cancellation of factorials, the total is M" (L978-L979).
Pattern: precision at the decisive order comes from identities, not from estimates. If the constants on the two sides did not match, no estimate could help.

**M9. Win multiplicity by composition; balance an error made once against an error made per step.** A chain of m lifts multiplies the matrices, so the exponents add (L948-L950; Stepanov's multiplicity). The errors are x/m (made once, at the two ends) and m (accumulated), balanced at m ≈ √x: "that is where the exponent 1/2 comes from" (L1016-L1031). With per-step cost m² the same argument gives only 2/3 (L1031-L1034; announcement step 14: "one would stop at 2/3 a priori ... need for division"). "So the precision of the comparison of lattices is decisive" (L1034-L1035).
Pattern: the exponent of the final theorem is the solution of a balance equation. Compute the cost of one step exactly before building the chain; the first honest count showed a stall at 2/3 and named the missing device.

**M10. Upgrade a top-slope bound to a mean-slope bound by a family that is spread evenly.** One map of small rank controls only the largest slope of the target. Many maps are used. A second moment (a relative trace formula) shows that Σ (adjoint∘map) is close in mean square to a multiple of the identity; a lemma of linear algebra then says the images fill almost the whole target (L991-L1003; L205-L210).
Pattern: one test object bounds an extreme; a tight frame of test objects bounds the average. The input is a second moment, not a pointwise fact.

**M11. Use the freedom that leaves the answer unchanged to build the missing structure; pay for it with one deep bound that has slack.** The lifts need not preserve integrality. The lattices are assembled prime by prime, using the freedom to twist the intermediate lifts by characters "without changing the final period" (L196-L204, L981-L990; announcement steps 12, 15). The cost is a sum of lengths of Galois cohomology groups, bounded by √b (L683-L685), which is negligible after division by b. This one sub-bound takes the most outside mathematics (L203). The census: of 195 outside statements, 80 are passed to the one inequality for Galois cohomology and 46 to the one covolume bound; the two trace-formula statements take two rows (L13497-L13503).
Pattern: distant mathematics enters at one interface, as one inequality with a stated budget, after the main chain has shown how much slack that interface has.

**M12. Keep the logic as one inequality with an explicit error budget.** Everything from the construction is packed into (M) with four error terms (L771-L781). The skeleton is three lines (L230-L236). The order of choices is stated (L239-L245). Parameters are chosen at the end (L1016-L1030).
Pattern: one named inequality carries the whole construction; the consumer is proved first and separately.

**M13. Order of discovery (announcement, pages 3-4).** The toy came first (steps 1-2, 6-9 October). The statistic was changed to fit the method (step 5). The chain of lifts and its length came late (step 8, 15 November), followed by the exact cost per step, the stall at 2/3, and then the "division" that removed it (steps 14, 15, 17).
Pattern: toy, defect list, exact cost, named missing device, in that order.

## Part 2. The analogue of each move for (PUR-io) (closed folder)

Method. For each move I looked for the Yang-Mills object, the two competing bounds, a statement, a first estimate, the place where it reads the non-abelian structure and the dimension, its fate for weak 4D compact U(1), and the place where it dies. Labels as in the shared rules. Small lemmas are proved in section 2.12.

### 2.1 (M1) One-sided bound for one positive statistic: already done

The purity test is the Yang-Mills form of M1. It is one-sided, it concerns a positive sum, and it is asked for infinitely many cutoffs (F1, F2). The ratio M(2u)/M(u)² needs no knowledge of the top eigenvalue. This is the same design step as the choice of G.
Where the campaign stands in the RH architecture (ARGUED): at L344, "from now on the goal is an upper bound for a sum over primes". The reduction is done. The Chebyshev object is missing. Every move from M2 on is open.

### 2.2 (M2) The rigid inequality: five candidates, and the direction of each

The need: an inequality that bounds the excited weight from above, holds without a small parameter, and is fed by a computable "size".

(a) Positive-definite kernel. Let K be the continuous kernel of A = P₀T^u. Then K(U,V)² ≤ K(U,U)K(V,V) (PROVED, Lemma P1). This gives purity ≤ 1. It points the wrong way. But it gives the exact deficit formula of Lemma P1.

(b) Sector positivity. Each centre-twisted trace tr(C_k T^t) is a twisted partition function with a positive integrand, and each flux-sector trace is positive. Result: (1/8) tr T^t ≤ tr P₀T^t ≤ tr T^t (PROVED, Lemma P4). This is the exact analogue of Chebyshev's c₁n ≤ ψ(n) ≤ c₂n: right order, constants only (compare L371-L374). It reads the finite centre. For U(1) the centre is a circle, the flux sectors are Z³, and the lower bound is void.

(c) Integer multiplicities. Each eigenvalue has multiplicity at least 1. This is the literal analogue of "a nonzero integer has size at least 1". It gives LOWER bounds for M(t). It points the wrong way.

(d) Topological charge. With twists k (time-space planes) and m (space-space planes) and k·m odd, the SU(2) charge is a half-integer, and the continuum action is at least 4π²/g² (CITED from memory, UNVERIFIED: 't Hooft 1979-1981 on twisted tori; van Baal 1982). This is "a nonzero half-integer has size at least 1/2". It needs two orthogonal planes, so it reads dimension four. It reads π₃(SU(2)). It dies twice. First, (PUR-io) lives on the periodic cube with m = 0, where a single-plane twist has zero classical cost (flat twisted connections exist because the group is non-abelian). Second, the rigidity bounds the ACTION, and the target is a FREE ENERGY. The entropy of the size modulus of a charge-1/2 object is not rigid, and at the scale where the running coupling is of order one it cancels the action. This is defect (D1) in Yang-Mills form: a loss as large as the main term (ARGUED).

(e) Strong subadditivity of entropy. For every state, S(XYZ) + S(Y) ≤ S(XY) + S(YZ) (CITED from memory: Lieb and Ruskai 1973). It bounds a total entropy from above by local conditional entropies. It always points the needed way: with Lemma P2, −log purity ≤ S(ρ). It needs no small parameter. It is true for U(1) too; the U(1) failure must sit in the local terms. See candidate E in 2.11.

Finding (ARGUED). Rigid inequalities that point the needed way exist: (b), (d), (e). None reads the non-abelian structure in the neutral sector by itself. In RH the rigidity (integrality) and the arithmetic content (which primes divide) sit in the same object. Here they are apart.

### 2.3 (M3, M4) Where the classical method stalls; a wish list; toys and their defects

The "classical method" here is the comparison of partition functions. The exact form (Lemma P1, replica or swap form):

    purity = E_ν[ K(U,V)² / (K(U,U) K(V,V)) ],   ν ∝ K(U,U) K(V,V) dU dV.

So purity is the mean squared cosine of the angle between the half-time states of two independent slice configurations. Jensen's inequality applied to the seam (cut each periodic copy at one time and reconnect crosswise) gives purity ≥ exp(−β E[Δ_seam]), and E[Δ_seam] is of order n³ (ARGUED: 3n³ spatial links at each of two seams, each changed temporal term of order 1/β). So the classical bound is exp(−c n³). It is true and useless, and it is off at the LEADING order, exactly as (D3) (L460-L463).

Wish list for a Yang-Mills "divisible object":
- (Y1) an exact identity that writes the excited weight as a sum of terms in [0,1] (have: Lemma P1);
- (Y2) the extensive terms cancel identically (have: the two tori n³×2u and two copies of n³×u have the same sites, plaquettes and couplings);
- (Y3) a one-way inequality whose input is local in at least one direction (candidate: 2.2(e));
- (Y4) a place where the sign C_A > 0 or the finite centre enters with a size (missing).

Toys.
- β = 0: the kernel is identically 1, T is the projection on constants, and purity = 1 exactly (PROVED, Lemma P5). Defect: wrong end of the trajectory.
- Strong coupling, β small: cluster expansion. Defect: true for U(1) as well; wrong end.
- Small physical volume: perturbative. Defect: the purity fails there for SU(2) as for U(1), because modes of energy 2π/ℓ are not suppressed at time ℓ/512 (ARGUED: exp(−2π/512) = 0.988).
- Two dimensions: solvable, gapped for both groups. Defect: no dimension four.
No toy has the wished property (Y4). This is the largest difference from RH, where the lemniscate had (W1).

### 2.4 (M5) Leading terms agree

Analogue: (Y2). The purity is built so that bulk terms cancel exactly. A second cancellation is available in the entropic route: for arcs X, Y on the circle of direction 1 with X∪Y the whole circle, the combination S(X) + S(Y) − S(X∩Y) has two walls plus two walls minus four walls. The ultraviolet wall terms cancel identically (ARGUED; this is the cancellation used in entropic c-functions, Casini and Huerta, CITED from memory, UNVERIFIED).
Dies: cancellation of leading terms is necessary, not sufficient. In RH it moved the problem to the linear term, where exact formulas existed.

### 2.5 (M6) Amplification by a huge free parameter

The free parameters of (PUR-io) are ℓ (any multiple of 1024), the cutoff set (any infinite set) and L.
- Time amplification (PROVED, Lemma P3): purity ≥ 2/3 at time s gives purity ≥ 457/625 at time 3s. More generally purity ≥ c > 1/2 at time s gives M(ks) − 1 ≤ (1/c − 1)^k.
- Top-to-trace (PROVED, Lemma P3(i)): M(t) − 1 ≤ λ_1^(t−s) (M(s) − 1) for s ≤ t.
Pattern match: polynomial multiplicities are the "rounding". They are invisible once ℓ is large, because only an exponential rate is needed. So the constants 512 and 457/625 are not the difficulty.
Fate for U(1): the lemmas hold for any spectrum; no reading of the group. Dies: amplification needs one strict contraction to amplify. It creates none.

### 2.6 (M7) Auxiliary family, separated scale, one good member

Analogues found:
- The "infinitely often" quantifier plays the role of the intervals [Y, Y^(3/2)]. `PurIo.lean` (`record_in_every_block`, L36) already uses a pigeonhole on cutoffs.
- Sectors as a family: Σ_e Z_e = Z, so one flux sector has weight at most Z/8. The consumer fixes e = 0, so "one good member" is not free here.
- Boundary conditions as a family: magnetic twists m ∈ Z_2³. With m = (1,1,1) there are no zero modes (ARGUED). The consumer is stated for the periodic cube. A transfer lemma between m-sectors at large ℓ is itself an infrared statement.
- Scale separation and non-circularity: the calibrated trajectory has β_K above 2^2800 while the question lives at the scale ℓ. In RH the separation made the auxiliary L-functions harmless. Here the same separation is the difficulty: the computable regime (scale of the cutoff) and the regime of the question (scale ℓ) are joined only by K renormalisation steps.
Dies: no family was found over which the purity deficit has a computable average.

### 2.7 (M8) Size through the decisive order by exact formulas

Exact anchors found:
- purity(β = 0) = 1 (Lemma P5).
- Charging identity (PROVED formally, Lemma P5): with F_t(β) = log tr(P₀T_β^t), each F_t is convex in β, F_t'(β) = −⟨A⟩_t (A ≥ 0 the total action on n³×t in the eight-twist mixture), and

      log purity(β) = ∫_0^β ( 2⟨A⟩_{u,b} − ⟨A⟩_{2u,b} ) db.

  The integrand vanishes at b = 0 because the two geometries have the same number of plaquettes.
- "The same constants on both sides": in thermodynamic language, p/T⁴ at high temperature is the Stefan-Boltzmann constant (asymptotic freedom), and T d/dT (p/T⁴) = (ε − 3p)/T⁴, the trace anomaly. The target says that the integrated trace anomaly uses up the whole Stefan-Boltzmann constant to nine decimal places before T falls to 512/ℓ (ARGUED, from F3). For U(1) the trace anomaly is zero and p/T⁴ stays constant.
Reads: the trace anomaly is (β-function) × (action density difference). Its sign and size come from b₀ > 0, so from C_A > 0, and it is marginal exactly in dimension four. This is the cleanest place where non-abelian structure and dimension enter a formula for the purity itself.
Dies: the sum rule is an identity. Equivalent is not progress. The integrand must be bounded at every intermediate coupling, which is the mass gap at all couplings. No exact formula is known for the integrand at any β > 0.

### 2.8 (M9) Composition, and an error made once against an error per step

Three chains with this budget shape:
- Renormalisation steps. The coupling after k steps obeys 1/g_k² = 1/g_0² − 2b₀ k log L + ... . The initial term is "paid once", the b₀ term accumulates, and the balance point k* = 1/(2b₀ g_0² log L) is the scale of the mass. So the mass scale is the solution of a balance equation, as the exponent 1/2 is (ARGUED; standard dimensional transmutation). The analogue of "stopping at 2/3": any per-step error not summable against Σ g_k⁴ moves the balance point.
- Time slabs: T^u = (T^(u/m))^m. A contraction per slab is collected m times. Needs the contraction.
- Swap chain. Let R(A) = tr[(ρ⊗ρ) SWAP_A] for a region A of the spatial cube. R(∅) = 1 and R(cube) = purity. For slabs A_j = {x_1 < j}: purity = Π_j R(A_(j+1))/R(A_j). The two walls are created once and removed once (the "x/m" term); the n − 2 middle steps each cost the thermal Rényi entropy of one layer (the "m" term) (ARGUED). Each ratio is the expectation of a local swap in a two-replica geometry.
Dies: each middle ratio must be 1 − O(1/n). Proving that is clustering in the replica geometry. No balance parameter is left to choose.

### 2.9 (M10) From the top to the mean by an evenly spread family

This move matches the structure of (PUR-io) most closely. The gap is a "top slope" statement (λ_1 < 1). The purity is a "mean" statement (a trace). The upgrade:
- Lemma P3(i): gap plus a multiplicity bound at one earlier time gives the trace bound.
- The multiplicity bound M(s) ≤ exp(C (n/s)³) is a Stefan-Boltzmann type bound. It is ultraviolet, and it is TRUE for U(1). In RH language it is the "size" side; the gap is the "divisibility" side.
- Frame form: tr(P T^u) ≤ c⁻¹ Σ_a ⟨φ_a, T^u φ_a⟩ when Σ_a |φ_a⟩⟨φ_a| ≥ c·P on the excited neutral space.
Dies: the crux card already offers a plug-in for exponential clustering at one rate (`ExpClusters`), which needs no cube. So the upgrade top-to-mean is not the missing step. The missing step is the top itself.

### 2.10 (M11) Freedom that leaves the answer unchanged; distant mathematics at one interface

Transformations that leave the purity unchanged: gauge transformations; similarity T ↦ S T S⁻¹; the choice of the transfer direction (hypercubic symmetry: the trace over time u equals a trace of n steps of the transfer operator of the slab n×n×u); any block-spin map with a normalised kernel, applied to all the tori together.
- Crossed channel (ARGUED): −log purity ≈ n·[ε(n,n,2u) − 2ε(n,n,u)], where ε(a,b,c) is the ground energy on the cross-section a×b×c. The inequality tr T^(2u) ≤ (tr T^u)² gives ε(n,n,2u) ≥ 2ε(n,n,u). The purity is the reverse inequality up to 0.31/n. So the target says that the vacuum energy is additive under doubling of the thin side; that is, the Casimir energy of thickness ℓ/512 vanishes to that precision.
- Interfaces where distant mathematics could enter as ONE inequality with a budget: (i) strong subadditivity and the entropic inequalities of quantum information (candidate E); (ii) Bakry-Émery curvature bounds, which read Ric(SU(2)) > 0 = Ric(U(1)) (candidate B); (iii) semidefinite bounds from loop equations plus reflection positivity, where the non-abelian loop equation has a quadratic term that U(1) lacks (CITED from memory, UNVERIFIED: Anderson and Kruczenski 2017; Kazakov and Zheng 2022).

### 2.11 The analogue of the whole chain, and the candidates it gives

Whole chain (ARGUED), in the order of the eight steps of L160-L219:

1. Spectrum to a positive sum: mass gap ⇐ purity bound, infinitely often. DONE (consumer).
2. Rigid one-way inequality: −log purity ≤ S(ρ) ≤ Σ local conditional entropies. AVAILABLE (Lemma P2 + strong subadditivity).
3. Smooth local quantity: the conditional entropy of one slab given its neighbour, in which wall terms cancel. DEFINED, not estimated.
4. Size through the decisive order: needs the local term to precision 0.31·w/n. MISSING. The only exact anchors are β = 0 and the sum rule of 2.7.
5. Structure-preserving freedom: block-spin maps and the transfer direction. AVAILABLE, unused.
6. Top to mean: Lemma P3. AVAILABLE.
7. Balance: dimensional transmutation fixes the mass scale; ℓ is then taken large. AVAILABLE.
8. Removal of auxiliaries: none needed.
The chain breaks at step 4, and step 4 is where C_A > 0 must enter (wish Y4).

Candidates from Part 2. Each says how it fails for U(1).

**Candidate E (entropic slope inequality).** Object: the neutral thermal state ρ = P₀T^u / tr(P₀T^u) on L²(SU(2)^links), which is a tensor product over spatial links. Competing bounds: S₂(ρ) = −log purity from below by 0; from above by S(ρ) (Lemma P2), and S(ρ) by the cyclic chain of Lemma P6. Statement Λ_E: for a partition of direction 1 into N slabs X_1..X_N of width w,

    S(X_1X_2) + Σ_{i=3}^{N−1} [S(X_(i−1)X_i) − S(X_(i−1))] + [S(X_(N−1)X_N X_1) − S(X_(N−1)X_1)] ≤ log(625/457).

First estimate: if S(X) = c·|∂X| + s·|X| + r(X) for unions of slabs, with |r| ≤ δ, then the left side is s·n³ + (2N+1)·δ-type remainder; the wall terms cancel as 2 + 0 − 2. So Λ_E needs s·n³ + 2Nδ ≤ 0.313.
Reads non-abelian structure: nowhere in the inequality; only in the estimate of s and δ. Reads dimension: nowhere in the inequality.
U(1): the inequality holds. The estimate fails: a massless field has a slab term of the form κ n²/w² in S(X), so S(2w) − S(w) is of order n²/w², and thermal entropy s ≈ (4/3)·0.22/u³ per site (ARGUED).
Dies: at the estimate of s and δ, which is the infrared problem again, now for a von Neumann entropy, which is not a partition function.

**Candidate B (curvature sign).** Object: the ground state measure Ω² dU on SU(2)^links. Competing bounds: Bakry-Émery, gap ≥ inf (Ric + 2 Hess W), Ω = e^(−W), for the Dirichlet operator of Ω². Statement Λ_B: an effective curvature bound at a block scale. Reads C_A through Ric(SU(2)) = positive multiple of the Killing form, which is the same invariant that gives b₀ (ARGUED). U(1): Ric = 0, the bound is void; this is correct, because the photon is massless. Dies: the Wilson transfer operator is not the heat semigroup, so the Dirichlet operator of Ω² is not T; and at weak coupling Hess W must cancel Ric almost exactly, because the true gap is exponentially small in lattice units. Does not read dimension four. Known at strong coupling (CITED from memory, UNVERIFIED: Shen, Zhu and Zhu 2023).

**Candidate S (thermal sum rule).** 2.7. An identity; dies as equivalent. Kept for its anchor (Lemma P5).

**Candidate T (twist ratio).** Statement Λ_T: Z(k)/Z(0) ≥ 1/2 for the seven non-trivial centre twists k, at β_K, at the physical side ℓ, for infinitely many K. In words: for each k, the flux sectors that are odd under k carry at most a quarter of the full trace. Not equivalent to the seed: it concerns the sectors e ≠ 0, which the purity does not see; neither implies the other by local steps (ARGUED). Reads the finite centre and, through flat twisted connections, the non-abelian structure: the classical cost of a single-plane twist is zero for SU(2) and 2π²·512/g² for U(1) (ARGUED). U(1): false at weak coupling, Z(k)/Z(0) is a theta-function ratio of order exp(−c/g²). Dies: it is the vanishing of the vortex free energy, which is confinement at weak coupling; open. Tomboulis and Yaffe (CITED from memory, UNVERIFIED: Comm. Math. Phys. 100 (1985) 313) bound Wilson loops by this ratio.

**Candidate A (amplification and top-to-mean).** 2.5 and 2.9. Tool lemmas, proved. Not an estimate about the Wilson law.

### 2.12 Lemmas proved in this file

**Lemma P1 (deficit formula). PROVED.** Let X be a compact space with a probability measure μ of full support, and let A be a positive trace-class operator on L²(μ) with a continuous kernel K. Then tr A = ∫K(x,x)dμ, tr A² = ∫∫K(x,y)² dμdμ, K(x,y)² ≤ K(x,x)K(y,y), and

    1 − tr A²/(tr A)² = (tr A)⁻² ∫∫ [K(x,x)K(y,y) − K(x,y)²] dμ(x)dμ(y),

with a pointwise non-negative integrand.
Proof. Mercer's theorem gives K(x,y) = Σ λ_i φ_i(x)φ_i(y), uniformly, with continuous φ_i. Integrate the diagonal for the trace. The Hilbert-Schmidt norm gives tr A². Positive definiteness of the 2×2 matrix (K(x,x), K(x,y); K(y,x), K(y,y)) gives the pointwise bound. ∎
Use. A = P₀T^u, when P₀ commutes with T (ARGUED from the definition of P₀ as an average of symmetries; not checked in Lean by me). Then A² = P₀T^(2u), and the left side is 1 − purity.

**Lemma P2 (Rényi below von Neumann). PROVED.** For a density operator with eigenvalues p_i: Σp_i² ≥ exp(Σ p_i log p_i).
Proof. Jensen for the convex function exp and the probability weights p_i: Σ p_i·exp(log p_i) ≥ exp(Σ p_i log p_i). ∎
Use. purity ≥ exp(−S(ρ)). So S(ρ) ≤ log(625/457) = 0.3131 gives the test.

**Lemma P3 (amplification). PROVED.** Let 1 = λ_0 and λ_i ∈ [0,1] for i ≥ 1, with M(t) = Σλ_i^t finite for t ≥ t_0, and λ_* = sup_{i≥1} λ_i.
(i) For t_0 ≤ s ≤ t: M(t) − 1 ≤ λ_*^(t−s)·(M(s) − 1).
(ii) If M(2s)/M(s)² ≥ c > 1/2, then x := M(s) − 1 ≤ 1/c − 1 < 1, and for every integer k ≥ 1: M(ks) − 1 ≤ x^k and M(2ks)/M(ks)² ≥ (1 + x^k)⁻².
(iii) In particular c = 2/3 and k = 3 give purity at time 3s at least (9/8)⁻² = 64/81 > 457/625.
Proof. (i) λ_i^t ≤ λ_*^(t−s) λ_i^s. (ii) M(2s) ≤ M(s) gives c ≤ 1/M(s). Each λ_i^s ≤ x for i ≥ 1, so λ_i^(ks) ≤ x^(k−1)λ_i^s; sum over i. M(2ks) ≥ 1. (iii) 64/81 = 0.7901, 457/625 = 0.7312. ∎

**Lemma P4 (sector sandwich). PROVED, given the trace formula of P1.** For t ≥ 2 and β ≥ 0: (1/8) tr T^t ≤ tr P₀T^t ≤ tr T^t.
Proof. tr P₀T^t = (1/8)Σ_k tr(C_kT^t), and tr(C_kT^t) = ∫K_t(c_k x, x)dμ > 0 because the kernel of T^t is positive (`transferKernel_pos`, L693, and composition). The term k = 0 is tr T^t. For the upper bound, P₀ is a projection that commutes with T^t ≥ 0, so tr(P₀T^t) = tr(T^(t/2)P₀T^(t/2)) ≤ tr T^t. ∎ (Corrected in Phase 2: the first draft used a longer Cauchy-Schwarz argument.)

**Lemma P5 (anchor at β = 0, and charging identity). PROVED for the anchor; the identity is PROVED formally (differentiation under a finite-dimensional compact integral).** (a) At β = 0 the kernel `transferKernel 0 R` is identically 1 (`transferKernel_apply`, L552: every exponent is 0, and the gauge Haar measure has mass 1). So T is the orthogonal projection on the constants, P₀T^t = T for t ≥ 1, the trace is 1 and the purity is 1. (b) For β > 0, tr(C_kT_β^t) = ∫ exp(−β·A_k) over the link variables of n³×t with the twisted action A_k ≥ 0. So F_t(β) = log((1/8)Σ_k ∫exp(−βA_k)) is smooth, F_t' = −⟨A⟩, F_t'' = Var(A) ≥ 0, and log purity(β) = F_2u(β) − 2F_u(β) with value 0 at β = 0. ∎

**Lemma P6 (cyclic chain). PROVED from strong subadditivity (CITED).** Let ρ be a state on H_1⊗…⊗H_N, N ≥ 4, with all the entropies below finite. Then
S(1…N) ≤ S(12) + Σ_{i=3}^{N−1}[S(i−1,i) − S(i−1)] + [S(N−1,N,1) − S(N−1,1)].
Proof. Chain rule: S(1…N) = S(12) + Σ_{i=3}^{N} S(i | 1…i−1). Strong subadditivity says that dropping part of the condition does not decrease a conditional entropy. For 3 ≤ i ≤ N−1 keep the condition i−1. For i = N keep the condition {N−1, 1}. ∎

**Lemma P7 (explicit formula for the purity in the coupling plane). PROVED, given Hadamard's factorisation theorem (CITED, classical; not rebuilt here).** Added in Phase 2, see Part 3 row 12. Fix a finite Γ and t ≥ 2. Put Z_t(β) = (1/8) Σ_k ∫ exp(−β A_{k,t}(U)) dU for complex β, where A_{k,t} is the k-twisted Wilson action on n³×t, with 6n³t plaquette terms, each in [0,2]. Then:
(i) Z_t is entire, Z_t(0) = 1, |Z_t(β)| ≤ exp(12 n³ t |β|), and Z_t'(0) = −6n³t.
(ii) With 𝒵_t the zero set of Z_t, counted with multiplicity: Σ_{z∈𝒵_t} |z|⁻² < ∞ and Z_t(β) = exp(−6n³tβ) Π_{z∈𝒵_t} (1 − β/z) e^(β/z).
(iii) For real β ≥ 0: log purity(Γ,β,u) = Σ_{z∈𝒵_2u} [log|1 − β/z| + β Re(1/z)] − 2 Σ_{z∈𝒵_u} [log|1 − β/z| + β Re(1/z)]. The linear terms −6n³(2u)β and −2·6n³uβ cancel exactly.
(iv) If log purity(β) = O(β^m) at β = 0, then Σ_{z∈𝒵_2u} z^(−j) = 2 Σ_{z∈𝒵_u} z^(−j) for every integer j with 2 ≤ j < m.
Assumption (ARGUED, not checked in Lean by me): tracePW(P₀T^t) equals this Z_t for real β > 0, that is, the Peter-Weyl trace is the integral of the kernel on the diagonal.
Proof. (i) Each plaquette term is in [0,2], and the Haar mean of 1 ∓ (1/2)tr U_p is 1 for both signs. (ii) Order at most 1 and Z_t(0) = 1; Hadamard. (iii) Z_t > 0 on the real axis; take logarithms of absolute values. (iv) For |β| below the least modulus of a zero, log(1 − β/z) + β/z = −Σ_{j≥2} (β/z)^j / j, with absolute convergence of the double sum; compare coefficients. ∎
Reading. (iii) is the Yang-Mills counterpart of the explicit formula of L273-L276, read in the reverse direction: the positive statistic is a sum over zeros. (iv) says that the zeros of Z_2u and the doubled zeros of Z_u agree in their inverse power sums up to the order of contact at β = 0. The lane reports that order as 4k for its free-energy differences (Theorem SC, as cited in row 1481 T2; I did not verify it for the neutral mixture).

## Part 3 (Phase 2). Each candidate against the record

Opened in Phase 2: `library/gap-rh-tools-transfer-fable.md` (row 1481: outcome, sections 3 to 6 in full, lines cut at 750 characters), `gap-rh-tools-transfer-astra62.md` (row 1482: last two sections), `gap-rh-tools-transfer-check-opus.md` (row 1487: steps 4 and 5 and RESULT), `library/prior/gap-rh-explainer-rest-luna.md` (row 1486: findings (a) to (d)), `library/open-registry.md` (header and first rows; then keyword search), and keyword searches over `library/*.md` with the hit lines read. Limits: I did not read rows 1481, 1482, 1487 from first line to last. The registry holds the open statements of the ultraviolet account; of the keyword families I searched for the candidates below, only "trace anomaly" has a registry hit (1 hit). The attack record is in the library files. A truncated or searched read proves nothing about lines I did not see.

What rows 1481, 1482 and check 1487 did, and how this row differs. They tested the TOOLS, one by one (T1 to T10, N1 to N7), each for a transfer lemma. Outcome (B): no transfer. Their summary: "Without a second kind of place every inequality comes from positivity and points the same way, the wrong one" (row 1481, T2), and "The lane has no second object" (row 1481, section 5). This row read the ORGANISATION. Three results differ from those rows:
1. Position. In the RH architecture the campaign stands at explainer L344. The consumer is the analogue of step 1. Row 1481 says the one-sided step "is free in the crux" (T1). Same fact; this row adds that every later move is then a specification for the missing object (wish list Y1 to Y4, section 2.3).
2. A class of one-way inequality outside Proposition PER. PER (row 1303) closes "inequalities that follow from positivity of the spectral measure". Quantum strong subadditivity uses the tensor product over space, not the spectral measure, and it points the needed way (Lemma P6). Rows 1584/1585 tested and refuted the Rényi-2 form. The von Neumann form holds. See row 1 of the table.
3. T7 said the balance has no transfer because the number of steps is not free. This row agrees for the chain. It notes that ℓ is free and plays the part of b (2.5). That is on file as PER (c).

| # | Candidate or lemma of this file | Nearest on file (quoted phrase) | Verdict |
|---|---|---|---|
| 1 | E: −log purity ≤ S(ρ) ≤ cyclic chain of conditional von Neumann entropies of slabs, walls cancel (2.11, P2, P6) | Check 1675, `gap-direction9-check-astra62.md` L27: "A bound on von Neumann entropy would be sufficient and different". Check 1585 (vi), `gap-band-direction5-check-astra62.md` L154: "Even collision-entropy strong subadditivity does not follow from conditional independence". `gap-mech-k2-solve-fable-check-astra62.md` L110: "Rényi-2 lacks even ordinary subadditivity". `gap-paths-fable.md` 6.4: "S(2T) <= J_T <= S(T) ... a restatement, not a route". `gap-afield-b-max.md` B4 (conditional mutual information and recovery). `gap-compress-opus.md` L137: "Group-blind: yes". | NEW AS A VARIANT. The record refutes the Rényi-2 inequality and notes that a von Neumann bound would suffice. It does not write the quantum chain with the wall cancellation. The verdict "group-blind" of row 839 applies to the inequality. |
| 2 | Lemma P1, deficit and swap form | Proposition PER (b) of row 1303, quoted in row 1481 T6: "Z_+(2u) = double integral of K_u(U, V)^2 ... its content is the seed" | ON FILE |
| 3 | Lemma P3, amplification and top-to-trace | PER (c), `gap-positivity-fable.md` L369: "s(mu) <= s(u)^m" | ON FILE. The instance "2/3 at time s gives 457/625 at time 3s" is a corollary. |
| 4 | Lemma P4, sector sandwich with constant 8 | Row 1468 3.1 (neutral projection as a character sum over the sixteen masses), as cited in row 1481 T6 (b): "eight spatial twists, whatever the volume" | ON FILE in substance |
| 5 | Lemma P5, anchor at β = 0 and charging identity; candidate S, thermal sum rule and trace anomaly | `gap-direction7-fable.md` L89: "the pressure over T^4 ... must fall from the Stefan-Boltzmann value to about 1e-9; carry it down in temperature with the trace anomaly". `gap-crux-exercise4-max.md` L297: "blocked-equivalent ... (MONO-Delta) is false for the ordered Ising model". Theorem ZB/SC: contact of order 4k at β = 0. | ON FILE |
| 6 | Candidate T, twist ratio and vortex free energy | `gap-tomboulis-read.md` and more than 100 files that name Tomboulis; `gap-brainstorm2-max.md` L116: "the odd electric-flux sector of a time slice has exponentially small weight" | ON FILE |
| 7 | 2.2 (d), half-integer charge; action against free energy | `gap-mech-k2-solve-fable-check-astra62.md` L115: "A positive action bound in a specified sector would still need an entropy and neutral-trace comparison" | ON FILE, with the same death |
| 8 | Candidate B, Ricci curvature of SU(2) | Row 1481 T3: "the Ricci curvature 2 of SU(2) in Lemma NG (row 1474)"; more than 100 files name Bakry | ON FILE |
| 9 | 2.8 swap chain over slabs | Check 1585 (vi), `gap-direction6-fable.md` L197: "-log P = A_0 - A_(n/2) is an identity ... None of these three arguments produced a front-shift estimate" | ON FILE |
| 10 | 2.10 crossed channel, Casimir energy, lower bound on a partition function by a trial measure | `gap-crux-exercise-r858-max.md` L185: "Every form of the seed is a LOWER bound on a partition function"; `gap-afield-a-max.md` A5 (Gibbs variational principle for the Casimir free energy) | ON FILE |
| 11 | 2.10 block maps leave the purity unchanged; 2.10 (iii) loop-equation bounds | Lemma TW and Theorem K2 (row 1468): "every probability kernel carries the sixteen masses". `gap-purity-bootstrap-compare-astra62.md` exists in this campaign (not opened). | ON FILE |
| 12 | Lemma P7, Hadamard product over the coupling zeros of Z_u and Z_2u, cancelled linear term, matching power sums | `gap-zero-transport.md` (row 670): "from zeros of torus partition functions to a spectral gap"; Theorem ZB; Lemma PRG (row 1481): "Z^z and Z_+ have complex zeros". Row 1482 N3 treats the explicit formula in the TIME variable: "It expresses the same unknown eigenvalues on both sides". Search for "Hadamard product", "product over zeros", "exponential type": no hit for this statement. | NEW AS A VARIANT of the zero route. An identity, so not a candidate by itself. |
| 13 | 2.6 one good member; sectors or boundary conditions as the family | Row 1481 T8 (ii): "On file as an empty frame ... The family of auxiliary primes is exogenous ... The cutoffs K of one renormalisation trajectory are neither" | ON FILE |
| 14 | The reverse rigidity: U(1) has continuous one-form symmetries and integer flux | 31 files name higher-form symmetry; `gap-brainstorm2-max.md` item 24 (integer flux of U(1)) | ON FILE |

Count: 14 items; 12 on file; 2 new as variants (rows 1 and 12). No item passes the four-point gate of the crux card.

## Part 4. Ranking, first buildable components, and the obstruction

**No candidate survives.** No analogue of a move of the RH proof gave an estimate that is (1) a signed inequality at β_K uniform in K, (2) false for weak 4D U(1) with a proof that reads the dimension, (3) not equivalent to the seed, and (4) written out. The reason is structural (ARGUED): in the RH proof one object carries both the rigid inequality and the arithmetic content. For (PUR-io) I found three rigid inequalities that point the needed way. Each is blind to the group in the neutral sector.

The three components below are the ones not found on file. They are tools. I rank them by what a lane could build first.

**Rank 1. Proposition ENT (entropic slope inequality).**
Statement. For all finite Γ of side n, all β > 0, all u ≥ 2 and all integers N ≥ 4 that divide n: let X_i (1 ≤ i ≤ N) be the set of spatial links whose base vertex has first coordinate in [(i−1)n/N, in/N), so that L²(slice) = ⊗_i L²(SU(2)^(X_i)). Let ρ = P₀T^u / tr(P₀T^u), and write S(·) for the von Neumann entropy of the reduced state on a union of slabs. If these entropies are finite and
S(X_1X_2) + Σ_{i=3}^{N−1} [S(X_(i−1)X_i) − S(X_(i−1))] + [S(X_(N−1)X_N X_1) − S(X_(N−1)X_1)] ≤ log(625/457),
then purity(Γ, β, u) ≥ 457/625.
Proof. Lemma P6, then Lemma P2. ∎ (PROVED here, given strong subadditivity for states with finite entropies, CITED from memory, UNVERIFIED for the separable infinite-dimensional case.)
Build. By hand: done above. In Lean: Lemma P2 is elementary. Strong subadditivity is the cost; I do not know that Mathlib has it (UNVERIFIED).
Not equivalent to the seed: it is a strictly stronger sufficient condition (S ≥ S₂ with equality only for flat spectra), and its input is a set of entropies of slabs of width 2n/N, which the seed does not determine.
U(1): the implication holds. The hypothesis fails: a massless field gives S(2w) − S(w) of order n²/w², and a thermal entropy of order (n/u)³ (ARGUED).
Where it dies: at the slab entropies. They are not partition functions. The inequality is group-blind (the verdict of row 839 on entropic statements).
Tightness (PROVED): the chain is an equality for product states. So ENT cannot give the seed without an input on the local terms. Example: N copies of diag(1 − ε, ε) have every step of P6 with equality and purity ((1 − ε)² + ε²)^N, which is below any c > 0 for N large.

**Rank 2. Lemma P7 (explicit formula in the coupling plane).** Statement and proof in 2.12. Build: by hand, done; in Lean, needs Hadamard factorisation for order one (UNVERIFIED in Mathlib).
Not equivalent to the seed as a tool: it is an identity for every β, and it adds the matching of power sums (iv). As an estimate it is equivalent: a bound on the right side of (iii) at β_K is the seed.
U(1): the identity holds. For weak U(1) the zeros of Z_u and Z_2u do not pair near the real axis (ARGUED from F3).
Where it dies: at a zero-free region near [0, β_K], which is the wall of Theorem ZB (row 1481 T2: "stops at a zero-free neighbourhood above beta about 0.102").
What it adds to the zero route: both sets of zeros appear with signs +1 and −2, the linear term has cancelled, and contact of order m at β = 0 is m − 2 matched power sums. A next row could ask one sharp question: on the lattice n³×u, do the zeros of Z_u nearest to the real axis lie beyond β_K (GUESSED: yes, near the thermal crossover of the lattice with u time slices)?

**Rank 3. The wish list (Y1) to (Y4) of 2.3 as a filter for the other lanes of the campaign.** This is not a lemma. (Y1) and (Y2) are on file (rows 2 and 5 of the table). (Y3) is ENT. (Y4), a one-way inequality that reads C_A > 0 or the finite centre in the neutral sector with a size, is what the RH architecture says is missing. A far-afield or literature lane should be judged by whether it supplies (Y4).

**The strongest obstruction I can prove.**
Proposition OBS (PROVED). Each of the following holds for every positive trace-class operator with a commuting finite group action, or for every state on a tensor product, and so none implies purity ≥ c for any c > 0:
(a) the deficit formula (P1): the operator with kernel a + bN·δ_xy on N points with uniform measure, a, b > 0, a + bN ≤ 1, is positive with a strictly positive kernel at most 1 and has purity (1 + (N−1)r^(2u)) / (1 + (N−1)r^u)², r = b/(a+b); with r^u = (N−1)^(−1/2) this is 2/(1 + (N−1)^(1/2))², which tends to 0;
(b) the sector sandwich (P4): the same example with the trivial action;
(c) the amplification (P3): it needs purity above 1/2 as an input;
(d) the entropic chain (P6): equality for product states of arbitrarily small purity.
The Bogomolny bound of 2.2 (d) is not in this list. It fails for a different reason (ARGUED): it bounds an action in sectors with k·m odd, and the neutral trace has m = 0.
Meaning. The RH proof had a second kind of size on the same object. For the neutral purity, every one-way inequality on file or found here is satisfied by models of purity near zero. A new attack must bring a one-way inequality whose proof uses the commutator of SU(2) and the dimension. This row did not find one.

## Credits

Levent Alpoge (with Claude): the proof of the Riemann hypothesis and the announcement. Michael Rubinstein: the explainer and every line cited from it. Ethan Sussman and Levent Alpoge (with Claude and Codex): the release behind the Lean consumer; Tadeusz Balaban: the method. Authors of the lane rows cited (1303, 1468, 1481, 1482, 1486, 1487, 1584, 1585, 1672, 1675, 670, 839) are as FINISH records them. Classical results named: Landau, Chebyshev, Mercer, Jensen, Hadamard, Lieb and Ruskai.

## Labels

PROVED here: Lemmas P1 to P7, Proposition ENT, Proposition OBS, each given the classical theorems named in it. CITED: all statements about the RH proof (explainer line numbers), and the lane rows quoted in Part 3. ARGUED: F2, F3, sections 2.2 to 2.11 where marked, the structural reason in Part 4. GUESSED: the place of the nearest zeros in Rank 2. UNVERIFIED: every literature reference given from memory ('t Hooft, van Baal, Casini and Huerta, Shen-Zhu-Zhu, Tomboulis and Yaffe, Anderson and Kruczenski, Kazakov and Zheng, Lieb and Ruskai in infinite dimension), and whether Mathlib has strong subadditivity or Hadamard factorisation. No numeric run. No Lean run. No commit. Author only, checked by no one.

RESULT: The RH proof turns a spectral claim into a one-sided bound for a positive sum, then gets it from one rigid divisibility-against-size inequality on a designed object, with each defect repaired separately. (PUR-io) stands after the first step; no analogue passes the gate. Of 14 items, 12 are on file. New as variants: (1) Proposition ENT, strong subadditivity bounds −log purity by slab conditional entropies with walls cancelled; (2) Lemma P7, a Hadamard explicit formula over coupling zeros of Z_u and Z_2u with matched power sums; (3) a wish list naming the missing piece. Obstruction (proved): every one-way inequality found holds for models of purity near zero.
