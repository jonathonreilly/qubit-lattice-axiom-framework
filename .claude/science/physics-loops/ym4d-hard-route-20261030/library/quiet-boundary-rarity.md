# Rarity with no rough field held fixed

Own derivation, 2026-10-31; not reviewed by anyone at this form. Part: `hard-core--mapped`. The exact Markov property of the levels, with a layer frozen at every level, is Lemma 20.3 of `parts/upper-chain.md`, part of this project, and I use it as stated there after confirming (LOC) for this kernel. **The stopping set below is Lemma 22.1 of `parts/upper-chain.md`, mirrored and adapted to bricks, and the recursion for bad cells follows its Lemma 22.2; both are that part's, read at its checkpoint events_22.** Stopping a layer from the outside is the device of the local form of Theorem OS, Text 5.3 of the producer. Balaban's objects are kept. This line is not independent of the Sussman-Alpoge account. Nothing here reads the sibling attempt.

Status: **the form gated at 3b7fd4e57 was wrong as written** (`gates/theorem-z-3b7fd4e57.md`: D1 to D6, D9 to D11, which I have checked against that text; D8 was already replaced by Lemma OC, which that gate did not read). This is a repair written at the level of each term, not gated. Theorem Z here reads new inputs at their own labels: (VAL), (VAL^𝔡) and (Loc^c) of `library/sector-values.md`; a fill (F2) below, written by strata only; and stability of the minimiser in l^2, Lemma ST below. (RP_m[i]) and its index stay on record in `library/relative-density-bound.md`, but they also read the class path lemma, so they are hit by D4 and are no safer. So I stand on this repair, not on that fallback.

## Why the hierarchy existed, and why it can go

(RP_m[i]) compared F_m at two fields with the far data fixed, for far data of any flux. Its proof fixed the far children xi'' in numerator and denominator, and took a supremum over xi''. So the level below had to hold for rough far data as well. A rough far cell forces rough children, a chain can run from the changed region to that shadow, and every device that followed (the index i, the kept cells K_far and K_cut, the cut rule, the tame reference, the mixed term C_M) served that one supremum.

The supremum over xi'' is not needed. Both integrals integrate xi''. If a surface of quiet data, at every level, separates the changed region from everything farther out, then the outside is the *same integral* in numerator and denominator, exactly, by the Markov property, and the ratio is a supremum over the quiet data on the surface only. Nothing rough is ever on a boundary. A chain that blocks every surface is simply part of the region, and it pays.

## Setting

*Rough, regular.* Rough: flux above T. T_2 = C_p C_a T, D_l := { flux <= T_2 }, as in Text 5.9. The cut and the labels stay at T.

*Local lift.* For a brick b at level l, with its patch b^++ := the bricks within r_lift parents of b, and regular parents on the patch: Lift_b := the minimiser of A_l on the patch, in the fibre of those parents, free at the patch's edge. r_lift is below, and t_0 is large against it. The patch reads only parents above and near b. These are on or outside Sigma_{l+1}, by the clearance r_S >= r_lift.

*Quiet (second repair of D3, 2026-10-31).* **A brick b is quiet if its parents on the patch are regular and**

    Dev_b(V_l) := sum over c in b of | theta_c(V_l) - theta_c(Lift_b) |^2 <= eps_q^2 T^2,

with eps_q absolute, C_s eps_q <= 1/8. The lift has flux at most T/4 by non-concentration, so a quiet brick has flux at most T/4 + eps_q T <= T/2, and its labels are 0 with probability one. A typical field has Dev_b about t_0^4/x, far below eps_q^2 T^2 for x >= x_*. A brick with a cell above T is not quiet.

*Why not a threshold on flux: a first repair, withdrawn.* I first took quiet := flux at most T_q := T/(2 C_bd), C_bd the largest flux of a minimiser next to frozen data of flux at most 1. C_bd is not an absolute number: U(1) gives 2.86 at L = 17 in d = 2, and 1.89, 3.00, 3.61, 4.03 at L = 3, 5, 7, 9 in d = 3 (`checks/hard-core--mapped_face_constant.py`, which failed its cap of 4). By a count it is a Riesz transform of tangential data, so about log L on a flat face. At a re-entrant corner of a staircase of bricks, harmonic theory suggests a power of the brick's side, which that check did not test. And a descent at T_q, item (g) of `library/relative-density-bound.md`, only tolerates C_bd <= L^{c_1} with c_1 small. *A sup norm on the data is the wrong norm: the response at a point to data bounded in sup norm is singular, while the response to data small in l^2 is bounded by energy alone.* That is Lemma ST.

**Lemma ST (stability; level of each term).** *Let the frozen bonds of a layer on R_l^𝔡 have quiet data d, let W^0 be the minimiser on the fibre of a class parent V^fl, and W^ref the minimal lift of V^fl with no frozen bonds. Then at every free cell c, |theta_c(W^0) - theta_c(W^ref)| <= C_s eps_q T + tails, with C_s absolute.*

*Proof.* Whole blocks are frozen, with the same parents, so on the frozen blocks d = W^ref e^{w_b} with w_b in the fibre, Q w_b = 0, in a box gauge with ||w_b||_{l^2(block)} <= C L ||theta(d) - theta(W^ref)||_{l^2(block^+)}, by Lemma U, as flux is small. Now the action including the frozen plaquettes is stationary at W^ref on the whole fibre, so it has no first-order term in w: A(W^ref e^w) - A(W^ref) is the Hessian form, up to higher order. Minimising over w with w = w_b on the frozen blocks is at most its value at any extension: chi w_b, cut off in one block, with a correction restoring Q = 0, by Theorem F-D, whose C_ext is absolute at bricks. So ||d_{W^ref} w||^2 <= C sum_blocks ||theta(d) - theta(W^ref)||^2 with exponential weights: the response decays at a rate rho per block, as in Theorem F-D. At one cell, |theta_c - theta_c^ref| <= (local energy of the response)^{1/2}, and the bricks within a block of c contribute at most eps_q T each, with bounded overlap, up to the difference of Lift_b and W^ref on b, a tail by the choice of r_lift. QED at this level. *No Calderon-Zygmund bound and no analysis of corners is read:* a cell's flux is at most the square root of its energy. `checks/hard-core--mapped_face_stability.py`, U(1), one level, criteria written first: **PASS**. C_s = 0.319, 0.302, 0.290, 0.284 at L = 3, 5, 7, 9 on a flat face in d = 3; 0.511, 0.512, 0.500 at L = 3, 5, 7 at a re-entrant edge in d = 3; 0.286, 0.284 at L = 3, 5 flat in d = 4, 0.294 at L = 3 with 2 blocks across, and 0.470 with the edge. No growth in L, in contrast with C_bd.

*So W^0 next to quiet data has flux at most T/4 + T/8 <= T, its labels are 0, and the cut fits.* The earlier hostile item on a forced zone does not arise.

*(LOC) for this kernel (derived from Text 5.2; range corrected for D9).* Include the labels as variables: P(labels | V_l) is a product over cells of a function of that cell's flux. Given labels, M_l on a parent bond reads V_l and labels in its two blocks, and whether a bond is Haar reads labels within the merged dense cluster: dense boxes merge at range 2 J. So the weight WW := exp(-x_0 A(V_0)) prod_l K(V_l, V_{l+1}) is a product of local positive factors with range at most R_loc := (2 J + 2) L + S_* + d_1 in level-l cells, with L large against J.

*Bricks and layers (units corrected for D11).* t_0 := max(8 L, 4 r_S, 3 R_loc, C L log(1/T)) level-l cells, rounded to a multiple of 8 L, with r_S := max(r_*, r_lift, (4 log L + C)/delta_#) in level-(l+1) cells, and r_lift := (C/rho) log(t_0/(eps_q T)) parents, so that a difference of lifts at the edge of a patch is below eps_q T in l^2 on b; t_0 >= C L log(1/T) is what makes this consistent. A *brick* at level l is a cell of side t_0 of the tiling of Lemma BG, `library/fibre-propagator.md`, made of whole level-(l+1) blocks: at most d + 1 meet at a vertex, any two that touch share a facet, and any union is locally bi-Lipschitz to a half-space. These numbers depend on L and a_* and not on l. Check N of `checks/hard-core--mapped_sharp_two.py` shows why whole blocks are needed: a thin frozen strip inside a block has a stabiliser mode.

For a union E of bricks, Sigma(E) := bricks not in E that touch E. N(S) := all bricks within 3 t_0 of S. A family E = (E_l)_{l <= t} is **nested** if for l < t:

    (N) N(shadow E_{l+1}) is in E_l,    (B) every brick of E_l is within R_B := (2/3) t_0 L of shadow E_{l+1}.

*Layers.* If E is nested, Sigma_l := Sigma(E_l) is a layer family as in Lemma 20.3. A cell y of Sigma_l is farther than 3 t_0 from shadow E_{l+1}, by (N), and within R_B + 2 t_0, by (B). So its parent is not in E_{l+1}, and it is within (R_B + 2 t_0)/L + 2 <= t_0 - 1 of it, so in Sigma_{l+1}. The clearance on the inner side is at least t_0 L - R_B - 2 t_0 >= (t_0/3 - 2 t_0/L) L >= r_S L, since t_0 >= 4 r_S. So free level-(l+1) bonds are at least r_S parents from Sigma_l, as (I_l^𝔡) needs. Thickness at least t_0 >= 3 R_loc is what Lemma 20.3 needs, with (LOC). The gate's check of the upper chain's numbers is this same inequality at t_0 = 3 L.

*Tube, with no pockets filled (repair of D5).* For a set X of level-l cells, F := cells farther than 2 d_x from X, tube(X) := the cells not within d_x of F, rounded out to bricks. So tube(X) is within 2 d_x + t_0 of X, and |tube(X)| <= C (d_x + t_0)^4 |X| **always**, including for a shell; and its complement is a union of balls of radius d_x: thick wherever it exists. A shell with a large interior leaves that interior outside the tube. d_x >= C max(t_0, T^-1/2): it is a fixed number after a_*, before x_*.

*Reference: (F2), the fill of a tube with data on all its boundary (route by strata; gap, constants not computed).* Let V be a level-l field with flux at most T off X. There is a class V^fl, flux at most C_a T with C_a absolute, equal to V off tube(X). *A first outline here was wrong:* flat bands on each boundary component and a pure gauge between them. Flat bands are pure gauge only if their cross-section is simply connected. A vortex sheet X, of codimension 2 with holonomy -1 around it, leaves a band S^1 x X x I with holonomy -1 on S^1, which cannot be capped flat: it needs flux pi through a disc across the tube. That is allowed exactly when the tube is wider than (pi/T)^{1/2}. *The route is the stratified fill* (`library/relative-density-bound.md`; described there at the level of strata; the gate did not check it). Take a grid complex on tube(X) of side R_1 with T R_1^2 = K_1, K_1 >= C pi, adapted to the boundary. Interior edges trivial. On a 2-cell, cap the boundary holonomy, of angle at most pi, with flux at most pi C/R_1^2 <= T. On a 3-cell the boundary S^2 has curvature at most K_1/R_1^2, and SU(2) has pi_1 = 0, so a monopole-like boundary still extends, with a non-abelian core. On a 4-cell the boundary S^3 has a global gauge with |A| <= C(K_1)/R_1, as the bundle on S^3 is trivial, and A may be cut off, at the price of a charge in the cell, which is allowed: a 4-cell has volume with T^2 R_1^4 = K_1^2 >= 8 pi^2 for K_1 large. In scale-invariant form each stratum is an extension problem in a compact family, so its curvature bound is C(K_1)/R_1^2 =: C_a T with C_a absolute. *Lattice to continuum:* flux at most T per plaquette at mesh 1/R_1 interpolates to an L^infinity curvature, and a continuum extension restricts back with plaquette angle at most its supremum. **Compactness of connections on S^2, S^3 with L^infinity curvature, and continuity of the extension, are read, not proved here. Requires d_x >= C R_1, which is why d_x >= C T^-1/2.** Number of components of the boundary does not enter, so thick interiors are nothing special. In the recursion the reference is V^# of Lemma OC, which is built by descent, by local cube fills, wherever the region is not dense.

*Region densities.* A *boundary datum* 𝔡 at level l is a layer family at levels below l with quiet data, and a set of frozen level-l bonds with quiet data. R_l^𝔡 is the free part at level l: a torus, or a region with holes. For V on R_l^𝔡:

    F_l^𝔡(V) := - log integral over all fields below level l, between the layers, of WW,

and F_l^𝔡 with a mark S: only chains with every brick of S non-quiet. 𝔹_l^{S, 𝔡}(V) := inf over such chains of A(U) - sum_{j<l} sigma_j |R_j(chain)|, with R_j the cells above T at level j, sigma_j := 𝔈_j/x_j below. 𝔸 := 𝔹 with no cell above T.

*Exploration: a stopping set (repair of D1, D2; Lemma 22.1 of the upper chain, mirrored from outside, on bricks).* Let B be a set of level-t bricks, t the top level of the family, containing the parents' differences and the marks. Let E_t^start := the bricks farther than 6 bricks from B, E_l^start := N(shadow E_{l+1}^start). Repeat: read V_l on the current layers Sigma_l, in a fixed order, brick by brick. If a brick of Sigma_l is not quiet, add it to E_l, then restore with no further reading: (N) top-down; and for (B), while a brick b' of E_l is farther than R_B from shadow E_{l+1}, add the brick of a parent of b' to E_{l+1}, and restore (N) below. Stop when every layer is quiet (**success**), or when E_t comes within one brick of B (**failure**).

*(i) Stopping set.* Sets only grow. A cell read at some time lies in E or Sigma of that time, so on or outside the final layer. So two fields that agree on and outside a final family run the same trajectory, and {final family = sigma} is a function of the fields on and outside sigma. *This is the definition of the outermost family: the output of this algorithm, not an extremal object.* No duality is claimed. The earlier "Step 2" duality was false (D2), and the annuli of the earlier form could not nest (D1).

*(ii) Bad cells.* bad_0(c) := a brick within 6 t_0 of c is not quiet. bad_l(c) := a brick within 6 t_0 of c at level l is not quiet, or there is a chain of bad_{l-1} cells at range 4 t_0, of diameter at least R_B/2, under the ball of radius 2 t_0 about c. Claim: each brick added by reading or by (B) contains a bad cell, its witness, and its witness is within 4 t_0 of a witness of a brick present when it was added, or of a brick from (N) or the start. *Proof, following the upper chain.* Reading: a cell of the brick read, which is within 3 t_0 of the brick it touched. By (B) at level l + 1: the parent p. b' lies in a brick added earlier at level l, by reading or by (B), since bricks from (N) and the start are within 4 t_0 of shadow E_{l+1}. Following predecessors gives a chain of bad_l cells at range 4 t_0, from b' to within 4 t_0 of shadow E_{l+1}, so of diameter at least R_B - 8 t_0 >= R_B/2. Its first segment reaching R_B/2 lies under the ball of radius (R_B/2 + 4 t_0)/L + 2 <= 2 t_0 parents about p. So p is bad_{l+1}. And p is within t_0 of E_{l+1}, so range holds. QED.

*(iii) Failure:* a chain of bad_t cells at range 4 t_0 across the annulus at level t only. So failure enlarges B by top-level bricks only, and *neither the count L^{3 (l-j)} nor the slope of the flow is read.*

*The recursion for a leaf (no Cauchy-Schwarz; the marked form).* A *witness tree* of a bad_l cell c: either a leaf, a non-quiet brick within 6 t_0 of c; or a node, all bricks within 6 t_0 of c quiet, with q := ceil(L/C_q) cells bad_{l-1}, pairwise farther than 12 t_0 apart, in the chain, and a witness tree for each. (Hops of range 4 t_0 over diameter R_B/2 = t_0 L/3 give at least L/12 hops, so every third gives q separated cells, with C_q := 36.) The cells of T_c lie under the ball about c, so *their parents are quiet*, and leaves below a node have quiet parents within 6 t_0 at their own scale. There are at most N := (C L^4)^q choices of T_c. So forced children never appear as marks (repair of D10): if a parent in the ball were not quiet, the tree would stop there, at that parent.

Let S(tau) be the leaves of a tree tau, a set of separated bricks. Then a mass with c bad_l is at most the sum over tau of the mass with S(tau) non-quiet. By Theorem Z with marks, each is at most the product over leaves of own-level factors against one denominator. So, with z'_j := 13^4 z_j, the weight of "c is bad_j" obeys p_j <= z'_j + N p_{j-1}^q, in one inequality against one I^D, so p_j <= 2 z'_j for x >= x_*: as q >= 4 and x_{j-1} >= x_j - C(L), the second term has exponent q c x_{j-1} eps_q^2 T^2 and is below z'_j.

## Theorem Z

*For all l, all boundary data 𝔡, all V on R_l^𝔡, and marks S at levels below l: let X be the cells of V above T, tube(X) as above, and V^fl any class field equal to V off tube(X), of flux at most C_a T (in the recursion, the reference V^# of Lemma OC). Then*

    F_l^{S, 𝔡}(V) - F_l^𝔡(V^fl) >= x_l-tropical( 𝔹_l^{S, 𝔡}(V) - 𝔸_l^𝔡(V^fl) ) - 𝔈_l ( |tube(X)| + d_x^4 |S| ) - x_l e^{-delta d_x} |boundary tube(X)|.

Here 𝔈_l := C(L, a_*) (d_x)^4 log x_l, and "x_l-tropical" is the form of Lemma OC, read at its end with x_l - C(L). *So its value at chains with cells above T or marked non-quiet bricks is at least (c/2) eps_q^2 T^2 sum over those of x_{l(c) - 1}.*

*What it does not assume.* Nothing on far data: V has all its cells above T in X. And V^fl is class on the whole of R_l^𝔡, so F_l^𝔡(V^fl) is given by (I_l^𝔡).

*Input at each level:*

    (I_l^𝔡)  on class fields on R_l^𝔡: F_l^𝔡 = x_l A_l^𝔡 + vac_l |free cells| + E_sheet(𝔡) + R_l + Delta R_l^𝔡,

with R_l the bulk function read at a class extension, ||R_l||_n <= B_n, (VAL_l), (Loc^c_l) for R_l, and Delta R_l^𝔡 supported near the frozen bonds up to tails, with derivative norms at most C_n(L), and for values the region clause (VAL^𝔡_l), all uniformly in 𝔡. The contraction of Delta R by clearance is as before: at n = 1, C L^3 e^{-delta_# r_S} <= 1/2, by r_S >= (4 log L + C)/delta_#.

## Proof of Theorem Z (level of each term)

*Base.* l = 0: F_0 = x_0 A, equality.

*Step 1: the region (repair of D10).* Let A_0 be the level-(l-1) cells under parents in tube(X), together with the marks of level l - 1, and, for marks at lower levels, the cells above them, with a collar of d_x level-(l-1) cells. Off A_0 the parents of V and V^fl agree, and no mark lies outside. N := exp(-F_l^{S, 𝔡}(V)), D := exp(-F_l^𝔡(V^fl)).

*Step 2: every configuration has a stop, or a certificate.* Run the exploration with B := A_0, at top level t := l - 1. On each component of the complement of B, separately: a thick interior has its own stop, from its own side, as the outside of the tube. If it fails, let B_1 be B with the top-level bricks of the certificate and a margin of 6 bricks, and run it again. This ends, at worst when B is all of R. So each configuration is in N'_B for some B, where N'_B is the mass of configurations for which exploration of B succeeds and which contain the certificates of the construction of B, as marks inside B. So N <= sum_B N'_B: an inequality, since minimality of B would read fields outside.

*Step 3: the same outside.* Fix B. Split by the final family (Sigma, d) of B. By Lemma 20.3:

    N'_B = sum_Sigma integral dd O_B(Sigma, d) I^N_B(Sigma, d),    D >= sum_Sigma integral dd O_B(Sigma, d) I^D(Sigma, d),

with O_B the integral of WW outside Sigma, on the event that Sigma is final, *the same function in both*, since parents agree there and the event reads only fields on and outside Sigma. I^N_B, I^D are the integrals strictly inside Sigma, with parents V, V^fl; I^N_B carries the marks, and I^D carries nothing. The second is an inequality as these events are disjoint for fixed B. Hence

    N / D <= sum_B sup_{Sigma, d} I^N_B(Sigma, d) / I^D(Sigma, d).        (M)

All cells outside Sigma, of any flux and any size, have gone. The gate confirmed this algebra for any stop that is a function of fields on and outside Sigma.

*Step 4: inside, a recursion with quiet data only (repaired for D3, D4).* Let 𝔡' be (Sigma, d) restricted below level l - 1, with Sigma_{l-1} and d_{l-1} as frozen bonds. W_B is the level-(l-1) field inside.

    I^N_B = integral over W_B in the fibre of V, with marks, of exp( -F_{l-1}^{S', 𝔡'}(W_B) ),    I^D = integral over W in the fibre of V^fl of exp( -F_{l-1}^{𝔡'}(W) ).

Let W^0 be the minimiser of 𝔸_{l-1}^{𝔡'} on the fibre of V^fl. Its flux is at most T/4 + C_s eps_q T <= T, by Lemma ST: so *its labels are 0 and the ball below is in the base chart, on one side of no label surface.* By (I_{l-1}^{𝔡'}) on a ball of radius g around W^0: I^D >= exp(-F_{l-1}^{𝔡'}(W^0)) (c g)^n e^{-C n}, with n the number of free bonds of W_B. By Theorem Z at level l - 1, for each W_B, with reference W_B^# of Lemma OC. Then (I_{l-1}^{𝔡'}) between the class fields W_B^# and W^0, on the region inside Sigma, which *may lie in different sectors*:

    | R_{l-1}^{𝔡'}(W_B^#) - R_{l-1}^{𝔡'}(W^0) | <= 2 B_r n =: C_Loc n,

by the region clause (VAL^𝔡_{l-1}), `library/sector-values.md`, Section 6: each value is read along its own chain, with nothing integrated beyond Sigma, so no comparison across a far zone is needed. This replaces the class path lemma, item (r), which is false across sectors. So

    F_{l-1}^{S', 𝔡'}(W_B) - F_{l-1}^{𝔡'}(W^0) >= x_{l-1}-trop( 𝔹_{l-1}^{S', 𝔡'}(W_B) - 𝔸_{l-1}^{𝔡'}(W^0) ) - 𝔈_{l-1} ( |tube X(W_B)| + d_x^4 |S'| ) - C_Loc n - tails.

The loss 𝔈_{l-1} |tube X(W_B)| is what the discount sigma_{l-1} in 𝔹 is for: |tube X(W_B)| <= C (d_x + t_0)^4 |X(W_B)|, by construction of the tube (repair of D5), and Lemma OC's own-level gain on each cell of X(W_B) is above it. So it is absorbed at this step and does not recur. With the fibre's volume C^n and n log(C x_l) from the ball:

    I^N_B / I^D <= exp( -x_{l-1}-trop( a_B(d) - b(d) ) + C(L, a_*) n log x_l + tails ),

with a_B(d) := inf over W_B of 𝔹_l^{S, (Sigma, d)}, b(d) := 𝔸_l^{(Sigma, d)}(V^fl) = 𝔸_{l-1}^{𝔡'}(W^0). *The marks' gain is not (CI''') at a fixed mark (repair of D10):* it is in the tropical form, by Lemma OC, at each mark's own level.

*Step 5: the collar, by exchange (closes the gap the gate left at (ii)).* Let (a, b) be a_B(d), b(d), and (𝔹, 𝔸) the same with no data on Sigma, marks kept. Fields W_a for a(d), W_* for 𝔸. Both have the same parents in the collar, and both are class there: marks and cells above T lie in A_0. So they lie in one fibre, whose chart is connected: *no sector enters.* Glue at the middle of the collar by a cut-off in the chart: P := W_a outside and W_* inside, a competitor for b(d); P' := W_* outside and W_a inside, a competitor for 𝔹. So

    b(d) + 𝔹 <= E(P) + E(P') = a(d) + 𝔸 + tr,

so a(d) - b(d) >= 𝔹 - 𝔸 - tr. By convexity in the chart on the collar, with Nest coercivity and Theorem F-D, the relative field of W_a, W_* at depth d_x/2 is at most C T e^{-delta d_x/2}, and tr, a quadratic form in it on the surface, is at most C e^{-delta d_x} T^2 |boundary tube|. No path in quiet data is read, and no mixed difference in d. *Sign:* in the tropical form, a G_i < 0 is read with x_{i-1} in place of x_i; the difference is at most C(L) |G_i| <= C(L) T^2 |tube|, absorbed in 𝔈 |tube|.

*Step 6: the sum over B (repair of D1, D6).* n <= C(L, a_*) (|tube(X)| + d_x^4 |S| + bricks of B beyond A_0). Each certificate is a chain of bad top-level bricks, each of weight at most p_{l-1} <= 2 z'_{l-1}, by the recursion above, against C(L, a_*) log x_l per brick from n. Sum over B: start from elements of the boundary of A_0. The bricks added form connected clusters attached to it, with at most C_a choices per brick, so the sum over B is at most exp( epsilon |boundary tube(X)| ) for x >= x_*, and this is absorbed in 𝔈 |tube(X)|. *Not "at most 2":* the factor per surface element is real and it is harmless. QED of the sketch.

## What follows at once

(A1') *Polymers (labels corrected; repair of D11).* Let V' be class on a region at level l + 1, with boundary 𝔡. *Polymers at level l are the output of an algorithm on the whole configuration.* Start with clusters of cells of V_l above T, at the range of an annulus of 6 bricks. For each cluster run exploration. If it fails, add the certificate's bricks, re-cluster, and repeat. The output is a family of multi-level sets, each with its final stop, with disjoint annuli. Let N(F) be the mass of configurations whose output is *exactly* F. For a compatible family F and a polymer Gamma compatible with it:

    N(F u Gamma) / N(F) <= sup over quiet data of I^Gamma / I^class <= prod over cells c of Gamma of z_{l(c)},   z_j := exp( - c x_j eps_q^2 T^2 + C 𝔈_j ),

by (M) with the single B = Gamma, Theorem Z and Lemma OC, with the product over the cells above T at level l and the non-quiet bricks that are leaves of the witness trees of the certificates. *I^class is the integral inside the stop with V_l class, lower fields free.* Then the output has no further polymer inside this stop, since no cell above T at level l is there and lower chains generate polymers only as certificates of a level-l cluster. The far family F lies outside the layers, so it cancels exactly, whatever its size and flux. If a chain joins two far sets, they are one polymer, and the bound is for the whole of it. This replaces (A1), and removes the crossing gap. Each polymer's loss 𝔈 per cell uses |tube| <= C d_x^4 |X|, so there is a factor per cell for shells too.

Polymers with top below l are inside F_l^𝔡, as gas, level by level. So the fine rough cells, of which there are many per coarse cell, are never expanded at once. Only those in a certificate are.

(FF_j)(U): Theorem Z with R the torus and X all cells above T gives, pointwise at every V: F_j(V) >= F_j(V^fl) + x_j-trop(...) - 𝔈_j |tube X|. That is the upper bound (U), with no far data. Its comparison at V^fl reads (VAL_j).

(RAR^1_j), under a law: Theorem Z with marks, one level at a time; no joint rarity. **A non-quiet brick is mostly not above T: its cost is own-level through (O2') below, not through (A1').**

(H1)-(H3) with sites: exact, *and the holes' faces are quiet, so W^0 next to a hole has labels 0, by Lemma ST: the first form, with quiet = flux at most T, forced rough cells on the face (D3).* Given a family and its layers, the exterior integrand is exp(-F_l^{𝔡 with holes}), class data with quiet holes, by (I_l^𝔡).

(A2), first differences in V': the vector field on lines at distance about L/C from hot cells is as in Text 5.3, and it now reads D F_l at class bonds across a quiet layer, so only (I_l^𝔡). (D), the influence between two polymers: the cross-ratio of the exterior class integral in the two polymers' boundary data, Prop MD* below, Lemma HS-P and Theorem F-D.

## Lemma OC: own-level factors along a chain, with no sign of beta (derived 2026-10-31; replaces a false step)

*The false step.* Text 5.3 said Lambda_{i-1} - Lambda_i >= c T^2 |R_i| - delta T^2 |R_{i-1}|, with Lambda_i the energy of the class fill on the tube of V_i, and delta small "since tubes are small against a box". But d_x >= 3 L, so tubes are not small against a box. Take a rough level-(i-1) cell under a class parent of flux near T. The fill on its tube is unconstrained by the parents inside the tube, so it removes their energy too, and Lambda_{i-1} - Lambda_i can be about -T^2 (d_x/L)^4. So delta is not small, and the step fails. It would matter only through a negative beta_i: in the form x_m (A - 𝔸) + sum beta_i (A - Lambda_i) each bracket is non-negative, and if every beta_i were positive this would be enough, but no sign of beta per step is proved.

*The repair: two different sets.* The region of comparison in Theorem Z has width d_x, for its collar and its tails. The set where the reference differs from V need not. Theorem Z holds for any class reference V^fl equal to V off a subset Y of tube(X): its proof reads only that parents agree off A_0, that the data are quiet, and the formula at V^fl.

*Definitions.* A chain (U = V_0, V_1, ..., V_m), with labels and quiet boundary. R_i: its rough cells at level i, and Haar parents charged to their m_* rough children as in Lemma TE, Step 4. Y_i: the hull of R_i at the radius r_{I_*} of descent, absolute, so small against a block, and the blocks of affected parents. 𝒜_i: class fine fields whose level-i data equal V_i off Y_i, and whose level-(i+1) data equal V_{i+1} off Y_{i+1}. Lambda_i := inf of A over 𝒜_i, V_i^# the level-i data of a minimiser. E_i := A(U) - Lambda_i, G_i := Lambda_{i-1} - Lambda_i = E_i - E_{i-1}, E_0 := 0.

**(O1) G_i >= -delta T^2 |R_i|, delta small for L large.** Take a minimiser for 𝒜_{i-1}. Its level-i data equal V_i off Y_i. Its parents agree with V_{i+1} except on parents whose lines meet Y_i, a fraction f <= C (r_{I_*}/L)^3 of the lines of a parent that is not dropped. Restore them by the bump of (f'), at a cost at most C K f^{1/2} T^2 per affected parent. So it is in 𝒜_i at that price, and the number of affected parents is at most C |R_i|.

**(O2) Sequential descent: E_i >= c T^2 sum_{j <= i} |R_j|, c absolute.** Put U^(0) := U. Suppose U^(j) is class below level j, with level-j data V_j. Each rough cell of V_j has no rough cell below it in U^(j), so its energy in U^(j) is at least c_b T^2, by (BE_2). **This is the point: filling at level j - 1 and restoring V_j does not remove the rough cell at level j. Its energy is still there, in the field that realises V_j.** Run the descent at level j, ending at a field with no level-j cell above kappa T^2 in the region touched. By the energy form, (c) of the hostile pass on Prop 10, the gain is at least (1/8) of the energy of U^(j) on the cells of Z, and each cell of R_j has at least c_b T^2 in its neighbourhood, with bounded overlap, so the gain is at least c' T^2 per cell of R_j, dense boxes included. (A count of m_* cells per step would fail in a dense box. The energy form does not.) Go to the minimal lift of its level-j data, by CA_j, and bump to restore V_{j+1} on the parents that are not dropped, at the cost of (O1), which is a fraction of the gain. This is U^(j+1). So A(U^(j)) - A(U^(j+1)) >= (c'/2) T^2 |R_j|, and U^(i+1) is in 𝒜_i. Summing gives (O2). **So energies add across levels, by a descent one level at a time, with no factor per level, and it needs no count beyond (BE_2).** A dropped box: parents are Haar, and they are not restored. They are in Y_{j+1}, and their price is the m_* rough children, already counted.

**(O3) No sign of beta.** Theorem Z's tropical form, with these references, is Trop := sum_{i=1}^{m+1} x_{i-1} G_i, where G_{m+1} := Lambda_m - 𝔸(V^0). Let G~_i := G_i + delta T^2 |R_i| >= 0, with partial sums at least a_i := c T^2 sum_{j<=i} |R_j|. Let x_i-low := min_{j <= i} x_{j-1}, which is non-increasing. By the flow, x_i-low >= x_{i-1} - C(L). Then sum_i x_{i-1} G~_i >= sum_i x_i-low G~_i, and by Abel's summation this is at least sum_i x_i-low (a_i - a_{i-1}). So

    Trop >= c T^2 sum_i (x_{i-1} - C(L)) |R_i| - delta T^2 sum_i x_{i-1} |R_i| >= (c/2) T^2 sum over rough cells of x_{l(c) - 1},

for delta <= c/4 and x >= x_*(L). **Each rough cell pays at its own level, however the cells are nested, and only x_l >= x_m - C(L) for l < m is read.** So a tower of s + 1 nested rough cells costs the product of its own-level factors.

*With marks: (O2') (2026-10-31, after the gate's D3, D6; level of each term).* Let R_i be the cells of level i above T, and S_i marked non-quiet bricks with no cell above T, pairwise separated by 12 t_0. Run (O2) as written at threshold T: descent at level j, gain at least c' T^2 |R_j|, with cells above T paid whatever their label, as (BE_2) and the descent do not read labels. *That dissolves D6.* Lemma TE, verdict ADVANCE at hard labels with its repairs D7, is no longer consumed; it stays as a check on the count. Then, for each b in S_j whose patch does not meet a hull: on the patch the field is class, with regular parents. Replace it there by the minimiser with the same boundary and the same parents. By convexity in the patch, (o) and Theorem F-D, the gain is at least c ||theta - theta^min||^2 on the patch. In b, theta^min differs from theta(Lift_b) by a difference of minimisers across r_lift, at most eps_q T/4 in l^2. So the gain is at least (c/4) eps_q^2 T^2. Patches of separated marks are disjoint. A b whose patch meets a hull is charged to a cell of R_j in it, with bounded multiplicity, as hulls have absolute radius and marks are 12 t_0 apart. So

    E_i >= c_1 T^2 sum_{j <= i} |R_j| + c_2 eps_q^2 T^2 sum_{j <= i} |S_j|,    Trop >= (c/2) eps_q^2 T^2 sum over cells of R and bricks of S of x_{l - 1}.

*Forced marks.* A non-dropped box has energy at most K T^2, so its parent has flux at most C K^{1/2} T, and its lift is small. So under a non-dropped parent nothing is forced non-quiet, and under a dropped box parents read nothing. Forcing occurs only under the given V at the top of Theorem Z, inside the tube. The leaf rule keeps marks away from it in any case.

*What (O3) needs of the recursion.* In Step 4 of the proof above, for W_B in the fibre of V, take the reference W_B^# := the level-(l-1) data of a minimiser for 𝒜_{l-1}, so its parents are V off Y_l. And in Step 4, W^0 is a minimiser on the fibre of V^#, so 𝔸(W^0) = Lambda_l. Then F_{l-1}(W_B^#) - F_{l-1}(W^0) = x_{l-1} (Lambda_{l-1} - Lambda_l) + (differences of R at most C_Loc n), as written there. Y_{l-1} depends on W_B, and on the chain below it through the labels, which is allowed as Theorem Z at level l - 1 holds for each W_B.

*Hostile.* (1) Is U^(j+1) really class below level j + 1? It is a minimal lift of a class field, so yes, by the induction of (f'). (2) A bump on a rough parent that is not dropped: V_{j+1} there has flux above T, and W_j e^h has that parent. The parent is then rough with a class chain below, as (O2) wants. Lines through the hull are a fraction f, or the box would be dense, and the mismatch is at most C f^{1/2} K^{1/2} T, by (a) of the hostile pass on Prop 10. (3) r_{I_*} against L: absolute against L_0, as in Prop 10. (4) Is V^# in the formula range? It is class by construction, with flux at most C_a T, from Lemma F and the bump. (5) The tail of Step 5 now reads the difference of two minimisers across a collar, one with a chain's rough data inside. It is the exchange argument, which uses only the collar, so wells inside do not matter. (6) x_i-low: if x were to rise along the chain, the bound falls to the lowest value so far, which is within C(L). This is where a rise could cost, and it costs only C(L) T^2 per cell, against x T^2.

## Prop MD*: the upper chain's (MD*_j) on this map

*Gate at 3b7fd4e57: CORRECT-NO-ADVANCE: it is right given (A1') and Theorem Z, and it adds nothing past them. So its status is conditional on the repair above.* Statement as in the upper chain's Text 14, with layers on bricks with clearance, and quiet as above, so its "quiet" is the l^2 condition on bricks here; the threshold (RAR^1) reads at a brick is x_l eps_q^2 T^2.

*Decomposition.* Z^*(d^I, d^O) = T^* (1 + gas), with T^* the integral over V_j class between the layers of exp(-F_j^𝔡), and the gas of polymers with top j, floating.

*Step 1: the class integral across the middle third M.* Fix m := V_j on M, class. Then exp(-F_j^𝔡(p, m, q)) with p, q class is an integral over lower levels with class parents everywhere. Choose lower layers in the inner and outer thirds of the shadow of M, stopped from the inner and the outer side: this is a product kernel, so a cross-ratio at most 4 times that of Z^*_{j-1} at thickness L D/3, on the event that both exist. On the complement a chain crosses the shadow under class parents: it is rare uniformly in p, q, by (M). So F_j^𝔡 = u(p, m) + v(m, q) + E, |E| <= 4 eps_{j-1}(L D/3) + (crossing). This is where the earlier proof needed rough p, q; here p, q are class, since rough sets are in polymers.

*Step 2: the integral over m.* As Step 4 of Prop MD: convexity in the chart, Hessian within small relative distance of M_m, the Schur complement at a reference, by shifting y with m. Interpolate on m, covariance by Lemma HS-P and HS-C with A = M_Y^-1, Theorem F-D. So log CR(T^*) is at most C(L) x |A| (e^{-rho D/3} + z^{1/2} e^{-rho_s D/3}) + 4 eps_{j-1}.

*Step 3: the gas.* Total covariance, with sites the polymers. Dobrushin with hard core at range R_c >= C_R (log(x |A|) + log L)/rho, as Step 5 of Prop MD. The influence of k on i is the cross-ratio of the exterior class integral, at most C x |A|^2 e^{-rho d(i, k)}. A large polymer is one variable. Compatible means disjoint annuli, and connection is at the range max(t_0, R_c).

*Closure.* As Step 6: c_t := rho/3, and the term from level j - 1 has a much larger exponent.

Shapes in a quadruple may differ, since m is common and the shapes enter p, q only.

## The bulk step near a layer (derived at the level of counts; the one part of (I_k^𝔡) not on the torus)

Let 𝔡 be data at level k + 1. Sigma_k lies under frozen parents, and it is made of whole blocks. So each level-(k+1) block is wholly frozen or has no frozen bond, and a free level-k bond has at least one end in a free block. *Chart:* as Text 5.1 on free blocks; tree gauge there, nothing on frozen blocks, so it is the coordinate subspace xi_Omega = 0 of the torus chart at a class fill. *(H1):* `Nest coercivity` and the box-local chart map give gamma(L) on this subspace. *(H2):* derivatives of A_k^{𝔡'} at free bonds: the saddle system of Theorem F-D with layers, with absolute rate. *(H3):* V^* is the minimiser on the fibre with the frozen data, so the first variation vanishes among admissible variations, and D_xi S(0) = g D(R_k + Delta R_k)(V^*) applied to the chart, with Delta R_k bounded. Note that V^* next to frozen quiet data has flux at most C_D T <= T_2. *Laplace, gas:* as on the torus, with (A1') and compatible annuli in the region; the chain joining a polymer to the frozen data is not a thing, as frozen data are quiet. *Identification of Delta R_{k+1}:* G^𝔡 - G^bulk at a class extension, on one coordinate space. The forcing is at distance at least the distance to the frozen bonds, so by the interpolation S_t and Lemma HS-P, its derivatives are at most C_n(L) e^{-rho dist}, and this is Delta R_{k+1}, with the contraction by clearance on its older part.

## The induction, restated

Replacing H(k) of Text 5.10. For all boundary data:

1. (I_k^𝔡), with (VAL_k), (Loc^c_k), (VAL^𝔡_k).
2. Theorem Z at level k.
3. Flow.

*Order.* (a) Classical, unchanged. (b) Theorem Z at level k + 1, from 1, 2 at level k and (a). (c) (I_{k+1}^𝔡): base integral with F_k^𝔡 in the chart, Laplace lemma; polymers by (A1'), (A2); contraction, (SB), (LG), Taylor, data recursion. **(Loc_k) with rough far data is not in the hypothesis. (Loc^c_k), with class fields only and any sector, is, as Lemma 3 of the Taylor note reads it (corrected after D4).** A far rough region is never read. So Theorem OS and its local form, the rarity of Omega by peeling, the first derivative in its earlier form, and the collective term in the ball are not consumed. (VAL_{k+1}) is proved after the gas, as SRC reads it: `library/sector-values.md`, hostile (10).

*Not consumed any more, if this stands:* (RP_m[i]) for i >= 1; K_far, K_cut, the cut rule, C_M; the tame reference and its upper bound (UB_j), (g); the fill next to a kept cell (i'); the oscillation form at a rough parent; (G1'); descent at a strongly rough parent as an input to rarity (it stays only inside (OS_j)(a), if the upper chain still asks kappa above what (R3) gives).

## Hostile check

(1) *Is (M) honest?* Numerator: a sum over B, with an upper bound. Denominator: for each fixed B, disjoint events. O_B is the same in both only if parents agree on the outside and on the layers: B contains A_0, so they do. The stop reads no inner field. Yes.

(2) *Does a final family exist when V is strongly rough?* It lives in annuli under parents off tube(X), which have flux at most T, so their lift is typically quiet, and X has a collar. Yes, or a certificate, which enlarges B.

(3) *A forced region.* Under a strongly rough V the children in A_0 are rough, and at the next levels too, for a depth about log(pi/T)/(kappa log L). They are inside X(W_B), and their number is at most C_T E/T^2, by Lemma TE. So their loss is at most C_T 𝔈 E/T^2, against x c E: paid for x >= x_*. *Unlike the earlier E_i, no factor (L^4 w^4)^i appears, since the count is by energy and not by multiplying children.* I had written a recursion with such a factor. It is not needed here. The count is now (O2), by the sequential descent, and it reads no labels.

(4) *V^fl has flux up to C_a T, and it must be in the formula range and have a class lift.* T_2 = C_p C_a T, and closure is Text 5.9. Yes. V^fl need not be quiet. It does not lie on a layer. **An earlier form of this item said "W^0 near Sigma is class with flux at most C T, by Dirichlet data at most T". The gate's D3 is right that this was a real error: with C >= 2 the label branch has weight zero at W^0, and N2 finds C above 2 from L = 7.** Lemma ST is the repair. It reads only energy. What it does not check: the Hessian with lower layers near the face, beyond clearance.

(5) *Quiet data d, and F_{l-1}^{𝔡'} near a sheet.* The fine curvature on a level-j sheet is about T/s_j^2, enormous at the next scale. Theorems 5-7, F, F-D need the local scale: |F| s(x)^2 at most C a_*, with s(x) := s_{j+1} near the free level-j fields under Sigma_{j+1}. So a nest version, with IMS at the local scale. *This is the weakest point: not yet written.* The route is in `library/fibre-propagator.md`, *Nest coercivity*: IMS at the local scale from a one-jump model at U = 1; each patch sees at most one jump, by clearance. Check N, `checks/hard-core--mapped_sharp_two.py`, tests two levels at L = 3 only, at flat data and at constant flux: PASS, with coercivity 9.78 with a whole-block fine layer, the same as with none.

(6) *The tail clause with data d that are rough at the next scale.* Only the collar at level l - 1, where fields are class, is read.

(7) *The base integral in a region: does (I_k^𝔡) really have no surface growth?* Delta R is bounded in derivative norm, as boundary terms are fresh at each level. The vacuum's surface term is a number depending on d. It is common to numerator and denominator in all the ratios, and it does not enter a cross-ratio, being a function of the data on one side, up to tails that are in eps. For a layer with data, this number is not a constant: it depends on d, through energy on the sheet, E_sheet(d). It is on one side: a function of d^I alone, or d^O alone. Yes.

(8) *Marks at a lower level than the bottom of a tube.* Handled by Step 4's S'.

(9) *Does this hide the crossing gap?* Test case: far level-m cell Y strongly rough at fixed top data, and a chain from I to its shadow. In Theorem Z this case is not asked: V at level m has Y in X, so Y is filled too, on both sides of the comparison. **This is the real content, and it changes what is true to ask: a bound between a rough field and its total fill, not between two fields with a common rough part.** Consumers: (A1') has F outside the layers, and if a chain joins, Gamma contains it. I have looked for a consumer of the older form with a common rough part, and I find only: Prop MD with rough faces, which the upper chain no longer asks; (G1') and (UB_j), which it no longer asks; and the earlier form of (A1) with far sites, replaced above. If the upper chain returns to a rough top, this has to be redone. (RP_m[i]) is on record, and it reads the class path lemma as well, so it would then need a value bound of the kind in `library/sector-values.md` too.

(10) *A polymer with a huge top-level part.* Its activity is prod z_j over its cells, and its entropy is by cells. Sum over shapes: subcritical, since (range)^4 z_j << 1. Under a rough parent: forced children are not free choices, but they are in the shape, and the sum over shapes has c_a per cell against z_j. Yes.

(11) *What the rarity reads from the flow.* Only x_j >= x_l - C(L) for j < l, in the tropical form. An earlier form read the slope c_0, through an annulus width that could not fit; see the correction above.

(12) *Two different stops, and why.* Comparison (M) stops from outside, so that numerator and denominator share O_B, and there is no sum over fine shapes. But then O_B carries an event on the fields just outside Sigma, so it is not the free exterior integral, and it cannot be the representation used for derivatives. Representation: stop from inside, first quiet family from the polymer outward. Then the exterior is free and it is exactly exp(-F_l^{𝔡 with holes}), and the activity carries the event. So mass = sum over compatible families of prod I^{stop-in}_a times O^free. Dobrushin reads only O^free: the conditional law of site i given the others has density ratio exp(Delta_i Delta_k log O^free), a cross-ratio of a class integral. Rarity (A1') is a statement about masses, so it may be proved by the other stop. A site's absent state is a mixture over quiet d_i, with weights free of k, plus a rare part, so it has the same bound by the product-kernel step. If one tried (M) with the inside stop, the sum over fine shapes costs exp(z_l |surface_l|), growing like L^3 per level: this is the surface excess of an earlier failed route, and it is why the stop direction matters. At quiet = flux at most T, the free exterior integrand next to a hole had forced rough cells on the face (D3); with Lemma ST it does not.

(13) *The gate's list, against this form.* D1: no annuli at lower levels; nesting by (N), (B). D2: no duality; an algorithm. D3: Lemma ST, with quiet in l^2. D4: (VAL), (VAL^𝔡), (Loc^c). D5: tube with no pockets, (F2). D6: (O2'). D7: repairs in Lemma TE, recorded there; not consumed now. D8: Lemma OC, ungated. D9: R_loc, t_0. D10: leaf rule, S in A_0. D11: units fixed; (A1') by an algorithm with N(F) exact. *What the gate said it did not check, and I have not added to:* (CI'''), Claim A, Text 5.9's bulk step, Theorem F-D, Lemma D-coer, Brick geometry beyond its check, Lemmas 20.1, 20.2, (A2), the Dobrushin step, Step 4 of Prop MD, and the stratified fill.

(14) *Attack on the newest step: does exploration read a cell inside a final family's brick?* It reads layers, which are outside the interior. (B) adds a parent's brick with no reading. A reader of "chain under a ball" in the definition of bad reads nothing in the algorithm: bad is used only in the bound. Yes.

(15) *Attack: the witness of a brick added by (B) needs a chain of bad cells at the level below, each with a tree whose nodes have quiet balls. But a chain cell may have a non-quiet parent in its ball.* Then the higher cell's ball contains a non-quiet cell, so that cell is a leaf at the higher level. The tree stops there, and the lower chain is not used. A tree exists in each case, by taking the highest such. Yes. The weight is the same recursion.

(16) *Attack: a leaf at the top level t lies in the annulus. Its parent is V off the tube, flux at most T, not quiet.* (O2') needs regular parents on the patch, not quiet ones. Yes.

(17) *Attack: x_l e^{-delta d_x} |boundary tube| against own-level gain, when X is one cell.* |boundary tube| <= C d_x^3, and d_x is large, so this term is at most x T^2 C d_x^3 e^{-delta d_x} per cell of X against x eps_q^2 T^2 c: it needs d_x >= (C/delta) log d_x. Fine.

(18) *What is weakest now.* In order: (F2), by strata, with compactness read; Lemma OC, ungated; Lemma ST's Hessian near lower layers; and everything marked as not checked in (13).

(19) *Attack on the new quiet: does a read of Dev_b make the stop depend on fields inside?* It reads V_l on b and parents on the patch. b is on the layer. The parents are on Sigma_{l+1} or farther out, by clearance. At the top level t = l - 1 they are V, off A_0, the same in numerator and denominator. Yes.

(20) *Attack: a brick has t_0^4 cells, so Dev_b sums many fluctuations.* Typical Dev_b is about t_0^4/x. It must be far below eps_q^2 T^2: x >= C t_0^4/(eps_q T)^2. And its rarity is exp(-c x eps_q^2 T^2) only if that exceeds entropy t_0^4 log x. Both for x >= x_*(L, a_*), since t_0 depends on L and a_* only. The cost is per brick and not per cell. That is enough: only bricks enter the witness trees, at a factor z_j each.

