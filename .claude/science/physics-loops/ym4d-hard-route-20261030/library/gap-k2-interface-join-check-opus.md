lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T08:03Z

# Check of row 1499 (gap-k2-interface-join-astra62): the first charged-boundary join

Provenance: Claude Opus 5.5 high, Mac mini worker 2, cross-provider check of row 1499 (author gpt-6.2-astra max), commit 95552e859. One reading by one other model; not an audit. Started 2026-11-24T20:03Z (date -u).

## Plan

1. Read row 1499's output in full, and the definitions it uses from rows 1485, 1489, 1475, 1348 (r_1(beta), GL4, the corner observable F, the stars, the sixteen masses).
2. Rebuild the four corner words from the two stars; contract endpoint spin indices.
3. Check the reflection in the join plane and the reflected seam bound.
4. Check the covariance bounds (3/5) r_1 and (4/5) r_1, then rho_ij >= r_1 > 7/15, the row sum > 28/15, and the weighted-row statement.
5. Check the exact join of the sixteen masses and the two endpoints of the twisted secant.
6. Read the Lean source: does theorem margins state the inequalities used?
7. Verdict: HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line.

Credit: Balaban; Sussman and Alpoge (with Claude and Codex), whose account fixes the Wilson set-up these rows use.

## Repo search

Read: FINISH rows 1485, 1489, 1493, 1496-1500; `library/gap-k2-wilson-interface-astra62.md` (row 1485, all of it); `library/gap-k2-direction-checkpoint-check-astra62.md` (check 1497, (iii)); row 1475 section 5. `grep` of `library/open-core.md` and FINISH for "full-face", "charged boundary", "corner response": no statement of the overlap point in section 4 below. This check makes no new-result claim beyond that scope remark.

## 1. Geometry and the four corner words (step 2 of the plan)

Checked at 2026-11-24T20:07Z (date -u). Status: **holds**, with one reading fixed.

- **Region.** A's star holds A, B = A + 2e_t, {-2,-1} x S and the six A + 2d_j. B's star holds B, A, {4,5} x S and the six B + 2d_j. The time link u_{s'} from (1,s') to (2,s') joins A + 2d_j to B + 2d_j. It lies in **neither** star's link set. It exists only if the joined law is the Wilson law on the subgraph induced by the union of the vertex sets. Row 1499 says this ("the plaquettes that appear when the two side arms meet"). That is the physical lattice, so the reading is the right one. Under the other reading (union of link sets) p_j is not a plaquette and G_j is not defined. **Repair R1 (wording):** state "induced subgraph on the union of the vertex sets" in the definition. Script check: in the induced region u_{s'} and the arm sites exist for j = -y, -z (and by symmetry +y, +z). No other new links appear: the time arms and the lateral arms, and two perpendicular lateral arms, differ in two coordinates.
- **Words.** For s = s_0 = (1,0,0), j = -y: s' = (1,-1,0) lies in S - 2e_y. a_j: (1,s) -> (1,s'); u_{s'}: (1,s') -> (2,s'); b_j^{-1}: (2,s') -> (2,s). So w_j = a_j u_{s'} b_j^{-1} is an open path from (1,s) to (2,s), the same endpoints as u_s. p_j = u_s b_j u_{s'}^{-1} a_j^{-1} = u_s w_j^{-1} is the elementary t-y plaquette over the bond (s,s') at times 1,2. Its four links lie in A-B, B-(B-2e_y), the two arms, and A-(A-2e_y): a double-cut (corner) plaquette. Same for -z, +y, +z (s_1 = (1,1,1), s' = s_1 + d_j). Holds.
- **Face reading.** u_{s_0}, u_{s_1} are near-side tangential to face +x (x = 1). a_j, b_j cross face j; u_{s'} is far-side tangential to face j. F and each G_j have disjoint link supports. Holds.

**Endpoint contraction, done directly.** Write a unit quaternion as g = (g_0, g⃗), so q(g) = g_0 and X = 2u_0, G = 2w_0. A gauge h at (1,s) sends u -> h u, w -> h w and fixes every other read link. Re(h u) = <h, ū> (Euclidean product in R^4). Under Haar, E_h[h_a h_b] = δ_ab/4. So E_h[(hu)_0 (hw)_0] = <ū, w̄>/4 = Re(u w^{-1})/4 = q(p_j)/4. Gauge invariance of the joined law then gives E[X_s G_j] = E q(p_j), and E X_s^2 = E G_j^2 = 1. A centre flip at (1,s) gives E X_s = E G_j = 0. A centre flip at (1, s_{1-k}) changes the sign of u_{s_{1-k}} and fixes all of w_j (its sites are (1,s_k), (1,s'), (2,s'), (2,s_k), and s' is outside S). So E[X_{s_{1-k}} G_j] = 0 and E[X_{s_0} X_{s_1}] = 0. With 3^2 + 4^2 = 5^2, E F^2 = 1. Hence E[F G_j] = (3/5) E q(p_j) for j = -y, -z and (4/5) E q(p_j) for j = +y, +z. This agrees with row 1499. These identities use only local gauge invariance, so they hold in every signed (twisted) Wilson law too.

## 2. The reflection in the join plane and the seam bound (step 3)

Status: **holds**.

- The map t -> 3 - t sends the region to itself: A <-> B, {-2,-1} x S <-> {4,5} x S, A + 2d_j <-> B + 2d_j. The cut links are the time links from t = 1 to t = 2. They sit over the slice set D = S ∪ (∪_j (S + 2d_j)); the time arms have no sites at t = 1, 2. They form a matching. The straddling plaquettes are exactly the squares over bonds of E(D). The corner plaquette p_j is the square over the bond (s,s'), which runs from S to an arm. Holds.
- Gauge the upper half so that the cut links are 1 (Haar invariance). Each straddling plaquette becomes q(U_b V_b^{-1}), with U_b, V_b the bond's links at t = 1 and t = 2. The two half weights are the same function H (a bounded positive function of the slice array) because the region is reflection symmetric. With coupling h on the bond e only: Z(h) = const · a(h) <H, (C_h^{(e)} ⊗ ⊗_{b≠e} C_β^{(b)}) H>. Holds.
- **Multipliers.** a(h) = ∫ e^{h cos θ}(2/π) sin^2 θ dθ = 2 I_1(h)/h. The normalized convolution acts on spin k/2 by r_k(h) = I_{k+1}(h)/I_1(h). From d/dh[h^{-ν} I_ν] = h^{-ν} I_{ν+1}, the ratio I_{ν+1}/I_ν is the mean of u under the density ∝ e^{hu}(1-u^2)^{ν-1/2}, and its derivative is that variance, ≥ 0. So each r_k is a product of nondecreasing positive ratios. Expanding H in products of matrix coefficients over E(D), the quadratic form is a sum of nonnegative squares times products of multipliers. So Z(h)/a(h) is nondecreasing. At h = β: E q(p_j) = (log Z)'(β) ≥ a'(β)/a(β). From I_1' = I_2 + I_1/h, a'/a = I_2/I_1 = r_1. Holds: **E q(p_j) ≥ r_1(β).**
- **Rational bound.** I_1 - I_3 = (4/β) I_2 gives r_1 = β/(4 + β I_3/I_2). Comparing series term by term, I_{ν+1}(x) < (x/(2ν+2)) I_ν(x) for x > 0: the coefficient ratio is (ν+1)/(l+ν+1) ≤ 1. So I_3/I_2 < β/6 and r_1(β) > β/(4 + β^2/6) = 1380/2929 at β = 23/10. Exact check (Python Fraction, /tmp script): 1380/2929 is the value; 20700 > 20503; so 1380/2929 > 7/15. Holds.

## 3. Covariances, pair bounds and the weighted row (step 4)

Status: **holds**. The per-pair and weighted-row parts are **true but trivially true** (scope point S1).

- Sum: (3/5 + 3/5 + 4/5 + 4/5) r_1 = (14/5) r_1 > (14/5)(7/15) = 98/75 > 1 (exact). Since ρ_ij ≥ |E F G_j| for unit centred probes, the row from face +x is above 98/75. Holds.
- Pair bound ρ_ij ≥ r_1 from reading X_{s_k} alone: holds. Spatial symmetries of the region (the hyperoctahedral group about the centre of S) move +x to any lateral face. The weighted-row argument (take the lateral face with smallest weight; then Σ_j (h_j/h_i) ρ_ij ≥ 4 r_1 > 28/15) holds.
- **S1 (scope, not an error).** Row 1499 defines the full data of a lateral face to include the near-side tangential links. In a side-two block every site of S is a corner of the 3-cube. So every near-side link of a lateral face also lies on other faces. Script count: each lateral face has 28 near-side links, and it shares 10 of them with each of its four perpendicular lateral faces. (It also shares the spatial links at t = 0 or t = 3 with the end caps.) Reading one shared link on both sides gives **ρ_ij = 1** for every perpendicular pair. So the per-pair bound and the weighted row hold with r_1 replaced by 1: the row sum is at least 4 among lateral faces, and at least 6 counting the caps. The direct full-face extension is false for this elementary reason. The plaquette pairing adds nothing to that conclusion.
- **S2 (scope of the disjoint-support test).** The 98/75 test has more content: the outgoing functions avoid F's links. But the correlated part of E[F G_j] is E[X_s G_j], and X_s = 2q(u_s) is itself a near-side link of face j (s_0 has y = z = 0 and s_1 has y = z = 1). So all four links of p_j lie in face j's own full data. The test measures a correlation **inside** one face's data. It shows no transmission across the joined block. It therefore constrains only criteria whose face spaces keep the shared near-side links. A proposal whose residual space drops them (for example, crossing plus far-side links, or a quotient by the shared edges) does not meet this counterexample. Row 1499's consequence asks such a proposal to "carry the four corner responses". This counterexample does not force that requirement. It forces only the first half: name the residual boundary space. (Read and sketched; no residual-space test is run here.)

## 4. The exact join of the sixteen masses (step 5, first half)

Checked at 2026-11-24T20:08Z (date -u). Status: **holds as bookkeeping** (read against rows 1485 and 1475 section 5; 1348 (1) itself was checked by row 1350 and is not re-derived here).

- Labels: ζ ∈ (Z/2)^3 temporal twists and τ ∈ {v, 2v} give 16 masses. With side-two boxes, a twisted coarse plaquette is a group of B^2 = 4 fine plaquettes with one sign (1475 section 5). c_2 = e^{-96β} z_2 = e^{-6β·2^4} z_2 agrees with 1485. Joining is Fubini with the shared links integrated once. An insertion F G_j uses the same variables. Holds.
- Pressure consequence: Z_+(τ) = (1/8) Σ_ζ Z^ζ_τ, P = Z_+(2v)/Z_+(v)^2. A per-label log error δ after a common b V_τ passes to each twist average (positivity). V_{2v} = 2 V_v cancels b, and |log P - log P̂| ≤ δ + 2δ = 3δ. Holds.
- Neutral mixture: each component law has E F = E G_j = 0 and unit variances (local gauge invariance holds with signs). So the mixture keeps the per-component lower bound. The mixed derivative of the unnormalized log mass with source e^{aF + bG_j} at 0 equals E[F G_j], and a source-free common scalar drops out. Holds.

## 5. The twisted secant and its two endpoints (step 5, second half)

Status: **holds**.

- **Translation covariance.** L_ζ'(h) = Σ_p η_p^ζ E_h q(U_p) over the N = m^3 τ temporal-d plaquettes. Moving a twist stack is a centre-sign change of variables, which preserves Haar and every signed insertion. So all signed means are equal, and L_ζ'(β)/N = E_ζ q(p_j) at a marked plaquette with η = +1 (placed away from the seam). Holds (read with row 1367's argument; the change of variables is the standard centre-sign move).
- **Untwisted transfer.** e^{L_0(h)} = K a(h)^N Tr(T_h^τ), with one factor a(h) per d-bond per time layer (m^3 τ = N factors). C_h ⪰ C_2 ⪰ 0 in the common matrix-coefficient basis, since each r_k(h) ≥ r_k(2) ≥ 0. Tensor products of commuting diagonal positive operators keep the order, and M A M ⪰ M B M. Min-max orders the eigenvalues of the positive trace-class operators, so Tr T_β^τ ≥ Tr T_2^τ. Then L_0(β) - L_0(2) ≥ N (log a(β) - log a(2)) ≥ N (β - 2) r_1(2), by convexity of log a. Also r_1(2) > 2/(4 + 4/6) = 3/7 (same series bound as section 2). Holds.
- **Endpoints.** At h = 2 and at h = β, at most 3m^2 plaquettes change sign (m^2 per twisted direction). Each change moves the exponent by at most 2 max(h, β) = 2β pointwise. So |L_ζ - L_0| ≤ 6β m^2 at each endpoint. Both endpoints are used, which gives the 12β m^2. Convexity of L_ζ (variance of the signed sum) gives L_ζ'(β) ≥ secant slope. Dividing by N(β - 2) gives E_ζ q(p_j) > 3/7 - 12β/((β-2) m τ) = 3/7 - 92/(mτ). Exact: 12(23/10)/(3/10) = 92. Holds.
- **Size.** Any mτ ≥ 8192 gives 3/7 - 92/(mτ) ≥ 3/7 - 92/8192 = 2/5 + 1243/71680 > 2/5 (exact). m = 512v with v ≥ 8 gives m ≥ 4096, so mτ ≥ 8192 for every τ ≥ 2. This holds whether τ is counted in fine or coarse units. The text's "mτ ≥ 8192 > 3220" is right; 35·92 = 3220. Then Σ_j E_{ζ,τ}[F G_j] > (14/5)(2/5) = 28/25 at every label. Holds.
- The torus half uses no reflection, so it is independent of the region definition in R1. Only the twist-0 transfer is ordered, as the text says.
- **S1 also applies here.** On the torus the 28/25 is again a correlation inside face j's own data.

## 6. The Lean statement (step 6)

Status: **the theorem states the rational facts used**.

theorem margins asserts: 3^2 + 4^2 = 5^2 (over 25); 23/10 / (4 + (23/10)^2/6) = 1380/2929; 7/15 < 1380/2929; (2·3/5 + 2·4/5)(7/15) = 98/75; 1 < 98/75; 2/(4 + 4/6) = 3/7; 12(23/10)/(23/10 - 2) = 92; 2/5 < 3/7 - 92/8192; (14/5)(2/5) = 28/25; 1 < 28/25. These are exactly the rational steps in sections 2, 3 and 5. The analytic steps stay hand proofs, as the note says: r_1 > β/(4 + β^2/6), r_1(2) > 3/7, monotonicity, and the step 92/(mτ) ≤ 92/8192. I did not replay the Lean myself. A second replay by the same method would not be an independent check. The lead's replay (FINISH row 1499: rc 0, axioms propext, Classical.choice, Quot.sound) is the record. My own exact Python Fraction recomputation of every displayed rational agrees (`/tmp/k2join-opus-scripts/chk.py`, guide only, not a proof step).

**R2 (wording).** Row 1499's text still says "Lean was unavailable ... It has not been run". That is stale: the lead replayed it. Update the sentence to the replay record.

## Verdict

**HOLDS AFTER CORRECTION.** I found no wrong line. Every displayed inequality holds, and the direct full-face extension is retired. Checked line by line by Claude Opus 5.5 high (cross-provider; author gpt-6.2-astra max), first failing step none. The checks: the four corner words, the endpoint contraction, the reflection at t = 3/2 and the seam bound E q(p_j) ≥ r_1(β) > 1380/2929 > 7/15, the covariances (3/5) r_1 and (4/5) r_1 with sum > 98/75, the per-pair bound and the weighted row, the sixteen-mass join with the 3δ purity transfer, and both endpoints of the twisted secant with > 28/25 at each label.

Repairs:
- **R1.** Define the joined law as Wilson on the subgraph **induced** by the union of the two stars' vertex sets. The link u_{s'} between A + 2d_j and B + 2d_j is in neither star. Without it, G_j and p_j are undefined.
- **R2.** Replace the stale "Lean unavailable, not run" sentence with the lead's replay record.
- **R3 (narrows the stated consequence).** The full-face extension fails for an elementary reason. In a side-two block, every near-side tangential link of a lateral face also lies on other faces: 10 shared links with each perpendicular lateral face, plus shared links with the caps. So ρ_ij = 1, and the row sum is at least 6 (section 3, S1). Even the disjoint-support test reads, for each j, a plaquette that lies entirely in face j's own data (S2). The counterexample therefore says nothing about a criterion on residual face spaces that drop the shared near-side links. Of the consequence in row 1499 (and its FINISH line), "a proposal must name its residual boundary space" stands. "And carry the four corner responses" is not forced by this counterexample and should be dropped or argued separately.

Not checked here: 1348 (1) itself (row 1350's check), the centre-sign translation argument of row 1367 (read, not re-derived), and the neutral-projection transfer identity Z_+ = K a^N Tr_{P_0 H} T^τ (read from 1469 section 2; standard 't Hooft twist algebra, not re-derived).

Credit: Balaban (multiscale set-up and the electric/transfer method lineage); Sussman and Alpoge, with Claude and Codex as authors of their outline and complete account (Wilson law at outline lines 240-277, GL3-GL4 at 2197-2257, revision 31a47c543775); row 1499's author (gpt-6.2-astra).

## Next two rows and their decisive outcomes

1. **No proof row from this check.** The interface line stays held under check 1497's triggers. A reopening proposal must name a residual face space with no shared near-side links. Decisive test for such a proposal: does a disjoint-support probe pair with one function per face, built from crossing and far-side links only, still give a row sum ≥ 1 after one join? Yes ends it; no is the first evidence for that proposal.
2. **Lead edit only.** Apply R1-R3 to the row 1499 text and its FINISH consequence. No lane is needed.

Finished 2026-11-24T20:08Z (date -u).
