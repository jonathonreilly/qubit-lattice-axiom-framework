lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T13:44Z

# Check of row 1421 (`library/gap-rg-signed-inclusion-astra62.md`)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 5e0307e18. This is one cross-provider reading of a gpt-6.2-astra max text. It is not an audit.

## Plan

1. Read row 1421 in full, then the parts of row 1418 it cites.
2. Check, in this order: the first-pair minor Y and the saving 3 b^6/32 (matchings, overlap 1/2, exterior-square identity, U(1) zero); the bounds on b over [2, 513/256]; the dimension count of the pair calculation; the commutation claim for reflection-invariant reductions (singlet lines by swap characters, 51 states, 5D with eight slots); identity (1) and its proof by classifying plaquettes; the lower bound on z_B; the table of responses; bound (2) and its arithmetic; the mixed-plaquette formula and (3) with its forest and one-cycle reductions.
3. Recompute the numerical bounds with exact rationals in /tmp scratch.
4. Verdict per statement: HOLDS, HOLDS AFTER CORRECTION or FAILS (first failing line); at most ten defects ranked.
5. Decisive outcome: is the one-link mechanism excluded as a 4D carry, and is the two-cycle reading the right next test (row 1424 has since run it).

## Repo search

Grep of `library/open-core.md` and FINISH for "exterior-square", "one-link mechanism", "signed inclusion" and "reflection-invariant endpoint": the only hits are rows 1421 and 1423 themselves (and an unrelated row 1321). The row's own repo search (its lines 1-17) names the priors it uses: (G8) of `library/gap-tree-astra.md` (overlap 1/2, line 219), Lemma FOREST, the sparse cycle readings, and row 1418. Row 1418 was checked by Claude (`library/gap-rg-step-sizing-check-opus.md`, all ten items HOLD), including its cycle magnitude d^(1-k/2) b^(k/4) (its Item 3); I rely on that check for the conventions and re-derive only what row 1421 adds. Later rows 1424, 1425 and 1430 already ran the next tests; I read only their FINISH results.

Credit: GL3-GL4 (Bessel recurrence and the character coefficients) are from the Sussman-Alpoge outline, SA 2195-2243 (Ethan Sussman and Levent Alpoge, writing with Claude and Codex). The Oeckl-Pfeiffer representation is the published dual (spin-foam) form of lattice gauge theory.

## Set-up as I read it

Normalized plaquette weight w(U) = e^(beta q(U))/A(beta) = sum_n b_n chi_(n/2)(U), q = tr/2, A = 2 I_1/beta, b_n = (n+1) I_(n+1)/I_1, b = b_1 = 2 I_2/I_1. Corner weight b_n^(1/4). A closed half-spin cycle of length k through k legs, each leg carrying the unit two-line singlet, has magnitude 2^(1-k/2) b^(k/4): triangle u = b^(3/4)/sqrt 2, four-cycle s = b/2. A triangle with its +1 leg left open gives u times the unit two-slot singlet (the two closed legs give 2^(-1), the open identity is sqrt 2 times the unit singlet). These match row 1418 lines 39 and 92.

## Step 1. The first Wilson pair (lines 32-57)

Verdict: HOLDS. Re-derived by hand.

- Matchings. Four of the six slots {+-2, +-3, +-4} fall on three axes, so at least one opposite pair occurs. A triangle at x needs its two +1 slots on different axes (a (+mu, -mu) corner is not a plaquette). With one opposite pair {+a, -a, b, c}, the matching (a,-a)(b,c) is excluded and the other two are admissible; with two opposite pairs the same holds. So k = 2 for all 15 patterns in 4D.
- Column. The exterior labels at x (legs +-mu other than +1) each carry two fundamental slots, so their intertwiners are unique and they fix the matching and every corner spin. The column is u^2 p_m with p_m the unit product of two singlets. Higher spins cannot enter these four entries.
- Overlap. Two distinct singlet pairings of four spin-1/2 have overlap of modulus 1/2 ((G8), gap-tree-astra line 219). The product of the four entries of Y has sign sign(<p,q><q,p>) = +, so independent row and column rephasing makes all entries positive: Y = u^4 [[1, 1/2], [1/2, 1]].
- Norms. ||Y||^2 = u^8 (1 + 1 + 1/4 + 1/4) = 5u^8/2; endpoint product (2u^4)(2u^4) = 4u^8; saving 3u^8/2 = 3b^6/32 since u^8 = b^6/16. det Y = 3u^8/4 and (tr Y)^2 - 2 det Y = 5u^8/2. Lagrange: ||x||^2||y||^2 - |<x,y>|^2 = ||x wedge y||^2; only the two mismatched ordered pairs contribute, each u^8 (1 - 1/4).
- Commutator. With p = (1,0), q = (1/2, sqrt3/2): [P,Q] = [[0, sqrt3/4], [-sqrt3/4, 0]], [P,Q]^*[P,Q] = (3/16) I, [P,Q]^2 = -(3/16) I, tr PQ - tr PQPQ = 1/4 - 1/16 = 3/16.
- Sum over patterns. Within one pattern S the saving is a sum of nonnegative terms ||x_i wedge y_j||^2 over all x- and y-columns with that pattern; the two-triangle pairs give 3b^6/32 and the rest add. 15 x 3/32 = 45/32. Correct as a lower bound on the saving relative to the sectorwise Cauchy-Schwarz bound.
- U(1). At fixed charges the invariant space of the link has dimension at most one, so every x_i wedge y_j = 0. The example (+1,-1,-1,+1) admits both pairings on the same line. Correct.

Remark (not a defect): the saving is a saving in a squared-norm bound against the sectorwise Cauchy-Schwarz bound. It is not yet a signed term in a coupling flow. The row says this itself (line 48, last two sentences).

## Step 2. Bounds on b over I = [2, 513/256] (lines 59-66)

Hand check: HOLDS.

- I_(k-1) - I_(k+1) = (2k/beta) I_k gives 1/r_k = 2(k+1)/beta + r_(k+1), hence r_k <= beta/(2(k+1)).
- beta = 2: r_4 <= 1/5, r_3 = 1/(4 + r_4) >= 5/21, r_2 = 1/(3 + r_3) <= 21/68, r_1 = 1/(2 + r_2) >= 68/157, b >= 136/157. b is increasing (b/2 = A'/A is the mean of q under e^(beta q)/A; its derivative is the variance), so this holds on I.
- Upper end: r_3 <= beta/8 <= 513/2048; r_2 >= 1/(6/beta + r_3) >= 1/(3 + 513/2048) = 2048/6657 (uses beta >= 2); b = 2/(4/beta + r_2) <= 2/(1024/513 + 2048/6657).
- Exact recomputation: see Step 9.

## Step 3. Dimension count of the pair calculation (line 68)

Verdict: HOLDS. Re-derived by hand; counts rerun in Step 9.

- In dimension d the link has 2(d-1) signed transverse slots. Four occupied slots with no opposite pair lie on four distinct axes: 16 C(d-1,4) patterns, all three matchings admissible, k = 3. Any opposite pair gives k = 2.
- The k unit matching vectors have pairwise overlaps of modulus 1/2, so ||Y||^2 = u^8 (k + k(k-1)/4) and the endpoint product is k^2 u^8. Ratios sqrt(5/8) (k = 2) and sqrt(1/2) (k = 3). 4D: 15 patterns, all k = 2. 5D: C(8,4) = 70 = 54 + 16; saving 54(3/2) + 16(9/2) = 153 in units u^8, that is 153 b^6/16.
- The "formal" multiplication by 2^(d-4) is labelled formal by the row and is not used later. No defect.

## Step 4. Commutation of reflection-invariant endpoint reductions (lines 72-82)

Verdict: HOLDS for the class as defined (one wording defect, D4 below). Re-derived by hand; the multiplicity statements rerun exactly in Step 9.

- Why reflection is a slot swap. Orient every plaquette through the directed link forwards (allowed: SU(2) characters are real, so w(U) = w(U^-1)). A transverse reflection fixes the directed link and maps the forward plaquette (1,+mu) to the forward plaquette (1,-mu). So it acts on the slot space as the transposition of the two slots, up to a scalar on each slot (any other intertwiner of the fundamental is a scalar by Schur). A scalar does not change eigenspaces. So a reduction XDX^* in the class commutes with that swap on the invariant space.
- Multiplicity-free decomposition (4D, six slots). Occupancy 0, 2: dimension one. Occupancy 4: some opposite pair occurs; spin 0 (swap -1) or spin 1 (swap +1) for that pair, each with exactly one singlet. Occupancy 6: three opposite pairs; singlet-admitting tuples (0,0,0), three permutations of (1,1,0), (1,1,1), each multiplicity one; 5 = dim Inv(V^(x)6). Odd occupancy: no invariant. Count 1 + 15 + 15 x 2 + 5 = 51. Each joint swap character has multiplicity at most one, so every operator in the commutant is diagonal in the same lines and any two commute.
- P and Q. On {+2,-2,+3,+4} the swap of +-2 maps p = (+2,+3)(-2,+4) to q = (-2,+3)(+2,+4), so P <-> Q and [P,Q] changes sign. The symmetric endpoint Gram is u^4 (P + Q).
- 5D. With only the opposite-pair swaps the 5D statement would be false: four occupied singletons on four axes have no swap at all and a 2-dimensional invariant space, whose commutant is all of M_2. The row correctly imposes the full signed-permutation stabilizer of the pattern. Singleton pairs are swapped by an axis transposition (with a sign flip where needed) that moves only unoccupied slots otherwise. At most three pairs for occupancy at most six, so multiplicity at most one. Occupancy 8: tuples with t spin-one pairs give singlet multiplicities 1, 0, 1, 1, 3 for t = 0..4; 1 + 6 + 4 + 3 = 14 = dim Inv(V^(x)8). On the 3-dimensional (1,1,1,1) block the three delta pairings are permuted by S_4 through its quotient S_3, a multiplicity-free representation (trivial plus standard), so its commutant {aI + bJ} is commutative.

## Step 5. Identity (1) and the lower bound on z_B (lines 86-98)

Verdict: HOLDS. Re-derived by hand.

- Classification. In B = {0,1}^d every site has one outward and one inward bond per axis. A fine plaquette at x in the plane (mu, nu) is out/out (meets B only at x), out/in (meets B along an internal edge; it contains two boundary bonds, whose labels set its spin to zero on the chosen subspace) or in/in (inside B). So out/in corners carry spin 0, the site network splits into an outward graph and an inward graph joined only by trivial strands, and the internal network is the one for vacuum externals. Dividing by z_B gives (1) coefficient by coefficient. Distinct boundary bonds (lattice, or torus with periods at least four) are needed and are assumed.
- Internal tail. b_n <= (beta/2)^n/n! (GL4) and |chi_(n/2)| <= n+1 give absolute convergence on the finite graph. Correct.
- z_B. With vacuum externals, mixed and out/out plaquettes have spin 0, so z_B = integral of prod_(p in B) e^(beta q(U_p))/A over Haar links. Each U_p is Haar-distributed, so E q(U_p) = 0 and Jensen gives z_B >= A^(-N_p), N_p = C(d,2) 2^(d-2) = 24 in 4D. A = sum (beta^2/4)^k/(k!(k+1)!) <= e^(beta^2/8) since (k+1)! >= 2^k; beta^2/8 <= (513/256)^2/8 < 2/3, and e^(2/3) < 2 iff e^2 < 8. So z_B > 2^(-24). (Trivially also A >= 1.)
- Corner subspace in 4D. The outward graph at a site is K_4; at half spin an active leg has even degree at most 3, hence 2; the even subgraphs with all degrees in {0,2} are the empty graph, four triangles and three 4-cycles. So 8^16 coordinates, magnitudes u (triangle) and s = b/2 (4-cycle). No outward leg carries four occupied slots in 4D. In 5D an outward leg has four out/out slots. Correct.

## Step 6. The table of responses (lines 100-107)

Arithmetic HOLDS: the directed triangle on +1,+2,+3 faces outwards at the 2^(d-3) sites with x_1 = x_2 = x_3 = 1; each copy has coefficient u(beta) by (1); the Euclidean response is 2^((d-3)/2): sqrt 2 in 4D, 2 in 5D.

Interpretation: see defects D1 and D2. The per-copy response is 1 in every dimension, while the classical factor is 2^(d-4). The resolved Euclidean response counts copies in a chosen norm. It equals 2^(d-4) only at d = 5; in 4D it is sqrt 2, not 1. The row's own text (line 107) only says the per-copy decrement is zero in 4D. That is correct.

## Step 7. Bound (2) and its arithmetic (lines 109-125)

Verdict: HOLDS (arithmetic rerun exactly in Step 9). Its force is limited (defect D3).

- b' = 2(1 - 3r/beta - r^2): A = sum a_k beta^(2k), a_k = 1/(4^k k!(k+1)!), and a_(k+1) 4(k+1)(k+2) = a_k give A'' + 3A'/beta = A; with r = A'/A, r' = A''/A - r^2 = 1 - 3r/beta - r^2. With r < 87/200 and beta >= 2: b' > 2(1 - 261/400 - 7569/40000) = 6331/20000 > 5/16.
- u' = (3/(4 sqrt 2)) b^(-1/4) b' > (3/(4 sqrt 2))(5/16) = 15/(64 sqrt 2) > 5/32 (uses b < 1). So u_+ - u_- > 5/8192.
- b > 6/7 gives u^4 = b^3/4 > 54/343 > (5/8)^4.
- The 4^16 coordinates (one outward triangle at every site) have values +-u^16 with beta-independent signs. Distance of the projected endpoints = 2^16 (u_+^16 - u_-^16) >= 2^16 * 16 u_-^15 (u_+ - u_-) > 2^20 (5/8)^15 (5/8192) = 640 (5/8)^15. Radius at least half of that: 320 (5/8)^15. And 320 (5/8)^15 > 1/4 iff 5^16 > 2^37.
- An isometry preserves the distance, so the bound holds for every common isometry and every centre of any rank. Correct.
- Side claims: 64 single triangles give distance 8(u_+ - u_-); 16 C(16,2) = 1920 distinct-site double triangles give sqrt(1920)(u_+^2 - u_-^2). Correct.

## Step 8. Mixed-plaquette formula, forest, one-cycle formula (3) (lines 127-152)

Verdict: HOLDS. Re-derived by hand.

- Formula. Undoing the Haar spin sums on internal links, four internal corners reassemble w(U_p) for every internal plaquette; a mixed plaquette leaves D^(n_p/2)(U_e) on its internal edge e and two corner weights b^(1/4) in B, hence b^(1/2); out/out corners give b^(1/4) and no matrix. F_lambda is a contraction of these matrices with fixed external intertwiners, gauge invariant under vertex gauges of B. Coefficient of R_B/z_B = a_lambda E_(mu_B) F_lambda. Correct.
- Forest. An internal edge e = (x, x + in nu) lies in two plaquettes per transverse axis mu; both endpoints have the same x_mu, so exactly one of the two leaves B: d - 1 mixed plaquettes. In 4D at most three fundamentals on e; the Haar invariant space of at most three spin-1/2 has dimension 0 or 1. By Lemma FOREST the Wilson marginal on a forest is product Haar. So no four-strand interior operator in a forest reading. Correct.
- (3). Gauge-fix a spanning forest to 1; the remaining edge of cyclic component i carries the holonomy h_i; mu_B is invariant under gauges constant on each component, so the joint law of (h_i) is invariant under independent conjugations. Schur gives integral of rho_j(g h g^-1) dg = chi_j(h)/(2j+1) I. Hence (3), with all Wilson dependence in scalars multiplying the fixed commuting projectors prod_i Pi_(i j_i). Any two such operators commute. In a component with one independent cycle all closed walks at a base vertex are powers of one generator. Correct.
- The row's own limitation (line 152) is accurate: the obstruction covers the interior-dependent channel operators only; a fixed exterior contraction may still carry noncommuting recoupling projectors, and two independent cycles in one component are not covered.

## Step 9. Exact recomputation (scratch `/tmp/w2-check1423/code`, not committed)

Run under `lab_ops.py numeric-lock` (holder w2-check1423, released), memory free 67 percent. All numbers claimed below are exact rationals or integer counts, or rational enclosures from positive series with a geometric tail bound. No Lean replay exists; these are a second data path, not a kernel check.

- `s1.py` (exact Fractions, 33 checks, all PASS): r_4 = 1/5, r_3 >= 5/21, r_2 <= 21/68, b >= 136/157 at beta = 2; r_3 <= 513/2048, r_2 >= 2048/6657; the upper bound 2/(1024/513 + 2048/6657) = 1138347/1311232 = 0.86815... < 87/100; b' > 6331/20000 > 5/16; 15/(64 sqrt 2) > 5/32 (as 480^2 > 2 * 320^2); u_+ - u_- > 5/8192; 136/157 > 6/7; (6/7)^3/4 = 54/343 > (5/8)^4; 2^20 (5/8192) = 640; 320(5/8)^15 = 0.27756 > 1/4; 5^16 = 152587890625 > 2^37 = 137438953472; (513/256)^2/8 < 2/3; e^2 < 8; the coefficient identity a_(k+1) 4(k+1)(k+2) = a_k for k < 40 (it holds for all k by the formula); counts 15, 45/32, 70 = 54 + 16, 153, 51, N_p = 24, 1920; ||Y||^2 = 5u^8/2 and saving 3u^8/2 = 3b^6/32.
- `s1b.py` (independent data path: Bessel power series in exact rationals with geometric tail): b(2) in [0.866254853444623, same to 1e-97] and b(513/256) = 0.867525103455284 (width 2e-98). Both satisfy 136/157 <= b < 87/100 and b > 6/7. Rational lower bound u_+ - u_- >= 6.83e-4 > 5/8192 = 6.10e-4. Rational lower bound 2^16(u_+^16 - u_-^16) >= 0.8108, against the row's 640(5/8)^15 = 0.5551. So the bounds in (2) hold with margin.
- `s2.py` (exact sympy rationals): builds Inv(V^(x)m) from singlet pairings on the occupied slots, lets slot permutations act, solves for the commutant and tests whether it is commutative.
  - d = 4, opposite-pair swaps only: 32 even patterns, 51 states, commutant commutative on every pattern. Confirms the 51-state claim and the 4D commutation.
  - d = 5, opposite-pair swaps only: 128 patterns, 323 states, 41 patterns with a noncommutative commutant (first: four singletons +2, +3, +4, +5). So the 5D claim needs isotropy.
  - d = 5, full signed-permutation stabilizer of the pattern: 0 noncommutative patterns. Confirms the row's 5D claim as stated (line 82 imposes the full symmetry).
- `s3b.py` (exact): unit overlaps of the three pairings of four spin-1/2 are 1/2, 1/2, -1/2; the swap of slots +-2 maps p = (+2,+3)(-2,+4) exactly to q = (+2,+4)(-2,+3).

## Verdicts

| Statement (row 1421 lines) | Verdict |
|---|---|
| First-pair minor Y, saving 3b^6/32, exterior-square sum 45b^6/32, U(1) zero (32-57) | HOLDS |
| Bounds 136/157 <= b < 87/100 on [2, 513/256] (59-66) | HOLDS (exact rerun; series enclosure agrees) |
| Dimension count k = 2, 3; 54 + 16; 153 b^6/16 (68) | HOLDS |
| Commutation of reflection-invariant reductions, 51 states, 5D with eight slots (72-82) | HOLDS (exact commutant check); wording defect D4 |
| Identity (1) by plaquette classification; K_4 corner states (86-98) | HOLDS |
| z_B > 2^(-24) (96) | HOLDS |
| Table of responses (100-107) | arithmetic HOLDS; interpretation corrected in D1 |
| Bound (2) and its arithmetic (109-125) | HOLDS (exact rerun, margin 0.81 vs 0.555); force limited, D3 |
| Mixed-plaquette formula, forest reading, (3) and one-cycle reduction (127-152) | HOLDS |

Overall: **HOLDS.** First failing line in the mathematics: none. One correction is needed in the FINISH summary of row 1421 (D1), and the scope of "drift fails" must be read as in D2.

## Defects, ranked by what each breaks

- **D1 (breaks the row-1421 summary in FINISH, not the note).** The FINISH result says the exposed triangle has "resolved response sqrt 2 in 4D and 2 in 5D, exactly the classical factor". In 4D the classical factor is 1, not sqrt 2. The correct statement: the per-copy response is 1 in every dimension, so the decrement against the classical factor 2^(d-4) is zero in 4D (note line 107). The "resolved Euclidean response" 2^((d-3)/2) counts copies in one chosen norm. It is not a coupling, and it meets 2^(d-4) only at d = 5. It is no test of drift.
- **D2 (scope of the drift verdict).** Identity (1) holds for every exact regrouping of the block. The out/out corner plaquettes join four blocks and are not integrated by the 2^4 contraction, so they must keep their bare weights. So (1) shows that a chart which keeps these coordinates cannot see a running there. It says nothing about the dynamics of the Wilson block. The note states this limit (lines 125, 156). The decisive outcome below keeps it.
- **D3 (force of (2)).** The bound is correct, but the ceiling 1/4 comes from no stated requirement (the note says so at line 125). As a guide only (floating point), the corner-subspace norm of R_B/z_B at beta = 2 is (1 + 4u^2 + 3s^2)^8 = 3.175^8, about 1.0 x 10^4. The forced radius is therefore a relative radius of about 3 x 10^(-5). So (2) excludes only a chart that asks for an absolute radius below 1/4 in the unscaled norm.
- **D4 (wording, line 78 last sentence).** "The conclusion holds with arbitrary spectator spins at the other legs" is true only for spectator patterns that are invariant under the reflections used. Fixing, for example, spin 1/2 on the corner (+2,+3) selects the column p alone. That reduction is u^4 P, which is not in the class, and it does not commute with u^4 Q. The note already excludes "a single asymmetric exterior column" (line 72), so no conclusion changes.
- **D5 (minor, line 100).** "including when all other plaquette spins in the block are summed" means the internal spins. The exterior labels other than the triangle are fixed to vacuum. No conclusion changes.

No defect breaks a consumer statement. The exterior-square saving improves a norm estimate only. The note says this (line 48), and no later row uses it as a carry.

## Decisive outcome

1. **Is the one-link mechanism excluded as a four-dimensional carry?** Yes, for the classes the note states, and checked here:
   - the commutator of any two reflection-invariant one-link reductions is zero on every fixed half-spin pattern in 4D (all 51 states, exact);
   - a uniform debit on the resolved raw triangle coordinates contradicts (1);
   - interior channel operators commute when each component has at most one independent cycle, by (3).
   
   Three things are not excluded: asymmetric exterior contractions (single columns), charts that integrate or redistribute the inter-block corner plaquettes, and charts that depend on beta or rescale the norm (D2, D3).
2. **Was the two-cycle reading the right next test?** Yes, as the next interior test. By (3), two independent cycles in one component is the smallest interior reading outside the obstruction, and the test is cheap. It was not the only open route. The note itself names the asymmetric exterior contraction (line 152) and redistribution across blocks (line 156). Row 1424 has since rejected the single-strand two-cycle reading (an exact axis-swap cancellation), and row 1425 found the two-strand ring to have the wrong sign (its check, row 1429, is pending). Recommendation, not proved: by (1), no exact regrouping can show running on the corner coordinates. So after the exterior-response search of row 1430, the next test should be a chart that integrates the out/out corner plaquettes between neighbouring blocks, carrying its mixed boundary interactions (row 1341 (25)-(27)).

## Provenance and limits

Checked line by line by Claude Opus 5.5 at high effort. This is one reading of a gpt-6.2-astra max text, not an audit. Hand re-derivations cover every displayed statement. Scratch scripts are in `/tmp/w2-check1423/code` (s1.py, s1b.py, s2.py, s3b.py) and are not committed. They use exact rationals and integers. They are not Lean-replayed, so they are a second data path, not a proof step. Lines 7-17 of the note (its outline and main-branch citations) were not re-read against their sources.
