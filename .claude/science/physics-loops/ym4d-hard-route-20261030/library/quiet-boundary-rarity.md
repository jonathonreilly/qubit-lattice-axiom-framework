# Rarity with no rough field held fixed

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. The exact Markov property of the levels, with a layer frozen at every level, is Lemma 20.3 of `parts/upper-chain.md`, part of this project, and I use it as stated there after confirming (LOC) for this kernel. Stopping a layer from the outside is the device of the local form of Theorem OS, Text 5.3 of the producer. Balaban's objects are kept. This line is not independent of the Sussman-Alpoge account. Nothing here reads the sibling attempt.

Status: derived at the level of each term. If it stands, it replaces (RP_m[i]) and its index, and much that depended on them, for every consumer I can find. Those proofs stay on record in `library/relative-density-bound.md`. They have not been shown wrong, except by the corrections recorded there.

## Why the hierarchy existed, and why it can go

(RP_m[i]) compared F_m at two fields with the far data fixed, for far data of any flux. Its proof fixed the far children xi'' in numerator and denominator, and took a supremum over xi''. So the level below had to hold for rough far data as well. A rough far cell forces rough children, a chain can run from the changed region to that shadow, and every device that followed (the index i, the kept cells K_far and K_cut, the cut rule, the tame reference, the mixed term C_M) served that one supremum.

The supremum over xi'' is not needed. Both integrals integrate xi''. If a surface of quiet data, at every level, separates the changed region from everything farther out, then the outside is the *same integral* in numerator and denominator, exactly, by the Markov property, and the ratio is a supremum over the quiet data on the surface only. Nothing rough is ever on a boundary. A chain that blocks every surface is simply part of the region, and it pays.

## Setting

*Quiet.* A level-l cell is quiet if its flux is at most T; it is then labelled non-rough with probability one, as chi = 0 on [0, T]. Rough means flux above T. T_2 = C_p C_a T, D_l := { flux <= T_2 }, as in Text 5.9. Nothing here uses a threshold above T for labels.

*(LOC) for this kernel (derived from Text 5.2).* Include the labels as variables: P(labels | V_l) is a product over cells of a function of that cell's flux. Given labels, M_l on a parent bond reads V_l and labels in its two blocks, up to S_* + d_1 level-l cells beyond them, since hulls are per box and a box with at least m_* core cells is dropped whole. A Haar parent reads nothing. So the weight WW := exp(-x_0 A(V_0)) prod_l K(V_l, V_{l+1}) is a product of local positive factors, with range at most 2 L + S_* + d_1 in level-l cells.

*Layer family, with room.* Sigma = (Sigma_l) as in Lemma 20.3 of the upper chain, with two additions asked of it here. (i) Sigma_l is a union of whole level-(l+1) blocks. Check N of `checks/hard-core--mapped_sharp_two.py` shows why this is not a technicality: a thin frozen strip inside a block has a stabiliser mode, a constant rotation of the strip compensated inside its blocks, which is an exact gauge direction at flat data and a soft mode of order a'^2 near flat data. It is the "hole inside a box" of (H1) in the ball. With whole blocks it is gone. (ii) Clearance: Sigma_{l-1} lies at distance at least r_S level-l cells inside the shadow of Sigma_l, with r_S := max(r_*, (4 log L + C)/delta_#). Here r_* is the radius bound of descent, so that the shells of descent around a rough level-l cell do not meet a lower sheet, and the second term is what stops the boundary term from growing: see (I_l^𝔡) below. (iii) Thickness: t_0 := max(8 L, 4 r_S, 3 (2 L + S_* + d_1)) level-l cells, rounded to a multiple of 8 L, in place of 3 L, so that the core of the shadow of a level-l layer, that shadow less a margin r_S L on each side, is at least L/2 level-(l-1) bricks across. These are fixed numbers depending on L and a_*. Frozen data must also be taken on brick cells, `library/fibre-propagator.md`. *Brick:* a cell of side t_0 of the tiling of Lemma BG, `library/fibre-propagator.md`, on level-l cells, in which at most d + 1 cells meet at a vertex and any two that touch share a facet, made of whole level-(l+1) blocks. So t_0 is a multiple of 8 L, and at least 3 (2 L + S_* + d_1) for (LOC).

*Region densities.* A *boundary datum* 𝔡 at level l is a layer family at levels below l with quiet data, and a set of frozen level-l bonds with quiet data. R_l^𝔡 is the free part at level l: a torus, or a region with holes. For V on R_l^𝔡:

    F_l^𝔡(V) := - log integral over all fields below level l, between the layers, of WW,

and F_l^𝔡 with a mark S: only chains with every cell of S rough. 𝔹_l^{S, 𝔡}(V) := inf over such chains of A(U) - sum_{j<l} sigma_j |R_j(chain)|, with sigma_j := 𝔈_j/x_j below. 𝔸 := 𝔹 with no rough cell.

*Fronts: the outermost family, by a monotone exploration (corrected 2026-10-31).* Let B be a multi-level set, with top level t. Its *annulus* is the set of level-t bricks within 6 bricks of the level-t part of B. A front family Phi = (Phi_j)_{j <= t} has Phi_t a closed surface of bricks in the annulus, and Phi_j a closed surface of level-j bricks in the core of the shadow of Phi_{j+1}. Explore from outside. Start with Phi_t at the outer edge of the annulus, and for lower j at the outer edge of the core. Apply until nothing changes: (1) if a brick of Phi_j contains a rough cell, move Phi_j inward past it. (2) If the cells read at level j - 1 under a brick b of Phi_j contain a chain of bricks with a rough cell, from the outer to the inner edge of the core of the shadow, so that no closed surface can pass under b, move Phi_j inward past b. Moves only reveal new cells on the inner side, so the result is a least fixed point, independent of the order, and it reads only fields on and outside the final fronts. *That final family, if it exists, is the outermost family (Sigma, d), and it is decided by the fields on and outside it.* It fails only if Phi_t reaches the inner edge of the annulus, and then there is a *certificate*: a chain of 6 level-t bricks across the annulus, each of them bad, meaning it contains a rough level-t cell, or has under it a chain of at least L/2 bad level-(t - 1) bricks. By recursion, a brick's weight is at most p_j <= t_0^4 z_j + C L^4 (c_a p_{j-1})^{L/2}, so p_j <= 2 t_0^4 z_j uniformly in j, and a bad brick has at least one rough cell.

*A correction.* An earlier form of this note fixed thin annuli at every level of width W_* = C R/T^2, to beat the surface's count L^{3 (l - j)} with the slope of the flow. That was inconsistent: the annulus at level j must fit under the layer at level j + 1, so t_0 >= 2 W_*/L, with R >= t_0, which asks T^2 L >= C, false. And it was unnecessary. Fine rough cells on a fine surface are typical, and there are many of them, but they do not obstruct anything: the lower surface goes around them, and where it cannot, the parent's surface moves inward. Only a top-level chain makes the construction fail. So the flow's slope is not read here.

## Theorem Z

*For all l, all boundary data 𝔡, all V on R_l^𝔡, and marks S: let X be the rough cells of V, tube(X) their d_x-neighbourhood in R_l^𝔡, with pockets filled, and V^fl any class field equal to V off tube(X), of flux at most C_a T (in the recursion, the reference V^# of Lemma OC, which differs from V only on a set small against a block). Then*

    F_l^{S, 𝔡}(V) - F_l^𝔡(V^fl) >= x_l-tropical( 𝔹_l^{S, 𝔡}(V) - 𝔸_l^𝔡(V^fl) ) - 𝔈_l |tube(X)| - x_l e^{-delta d_x} |boundary tube(X)|.

Here 𝔈_l := C(L, a_*) (d_x)^4 log x_l, and "x_l-tropical" is the form sum_i x_{i-1} (Lambda_{i-1} - Lambda_i) + x_l (Lambda_l - 𝔸(V^fl)) of Text 5.3, (RAR_j), read at its end with x_l - C(L).

*What it does not assume.* Nothing on far data: V has all its rough cells in X. And V^fl is class on the whole of R_l^𝔡, so F_l^𝔡(V^fl) is given by (I_l^𝔡).

*Input at each level:*

    (I_l^𝔡)  on class fields on R_l^𝔡: F_l^𝔡 = x_l A_l^𝔡 + vac_l |free cells| + R_l + Delta R_l^𝔡,

with R_l the bulk function read at a class extension, ||R_l||_n <= B_n, and Delta R_l^𝔡 supported near the frozen bonds up to tails, with all derivative norms at most C_n(L), uniformly in 𝔡. No Taylor extraction is needed for Delta R: boundary terms are fresh at each level, as Sigma_{l-1} lies under frozen parents at distance at least r_S level-l cells from any free level-l bond, so the lower boundary's term enters only through a tail. *The count (derived; a hostile check, which raised r_S from an absolute number).* A derivative at free parents y_1, ..., y_n reads Delta R_{l-1} through the lift K, at distance at least r_S parent cells: with the same sums as in (SB), this is at most C^n L^{4 - n} e^{-n delta_# r_S} ||Delta R_{l-1}||_n. At n = 1 this is C L^3 e^{-delta_# r_S}, and it must be below 1/2. With an absolute clearance the boundary term at low order would grow by a power of L per level, a flow of a boundary operator. With r_S >= (4 log L + C)/delta_# it contracts at every order, so ||Delta R_l||_n <= (1/2) ||Delta R_{l-1}||_n + C_n(L): bounded, with no extraction.

## Proof of Theorem Z (level of each term)

*Base.* l = 0: F_0 = x_0 A, equality.

*Step 1: the region.* Let A_0 be the level-(l-1) cells under parents in tube(X), with a collar of d_x level-(l-1) cells. Off A_0 the parents of V and V^fl agree. N := exp(-F_l^{S, 𝔡}(V)), D := exp(-F_l^𝔡(V^fl)).

*Step 2: every configuration has a surface, or a certificate.* Run the exploration above with B := A_0. If it fails, let B_1 be B with the certificate's top-level bricks and a margin, and run it again. The process ends at some B, at worst when B is all of R. Each configuration is therefore in N'_B for some B, where N'_B is the mass of configurations for which the exploration of B succeeds and which contain the certificates of the construction of B, a mark inside B. So N <= sum_B N'_B. *An inequality, not a partition: minimality of B would read fields outside.* Bricks have no pinch, so a failure gives a chain, by the elementary duality: if the bad cluster attached to the outer edge does not reach the inner edge, the cells touching it from the inner side form a closed surface of good cells.

*Step 3: the same outside.* Fix B. Split by the outermost family (Sigma, d) of B. By Lemma 20.3:

    N'_B = sum_Sigma integral dd O_B(Sigma, d) I^N_B(Sigma, d),    D >= sum_Sigma integral dd O_B(Sigma, d) I^D(Sigma, d),

with O_B the integral of WW outside Sigma, on the event that Sigma is outermost, *the same function in both*, since parents agree there and the event reads only fields on and outside Sigma. I^N_B, I^D are the integrals strictly inside Sigma, with parents V, V^fl; I^N_B carries the mark, and I^D carries nothing. The second is an inequality as these events are disjoint. Hence

    N / D <= sum_B sup_{Sigma, d} I^N_B(Sigma, d) / I^D(Sigma, d).        (M)

All rough cells outside Sigma, of any flux and any size, have gone. No sum over shapes is left on the fine surface: a surface that goes around an isolated rough cell is only a different Sigma, inside the supremum, with the same O_B on both sides, and B reads only top-level certificates. This is why a stop from outside has no surface excess, and a stop from inside, or a fixed surface, does. (A fixed surface gives N_fixed/D_fixed, and D_fixed/D is about exp(-z_l |surface_l|), which is not comparable to N_fixed/N without a decoupling.)

*Step 4: inside, a recursion with quiet data only.* Let 𝔡' be (Sigma, d) restricted below level l - 1, with Sigma_{l-1} and d_{l-1} as frozen bonds. W_B is the level-(l-1) field inside.

    I^N_B = integral over W_B in the fibre of V, with marks, of exp( -F_{l-1}^{S', 𝔡'}(W_B) ),    I^D = integral over W in the fibre of V^fl of exp( -F_{l-1}^{𝔡'}(W) ).

Let W^0 be the minimiser of 𝔸_{l-1}^{𝔡'} on the fibre of V^fl. It is class with room, by non-concentration: the parent has flux at most T_2, and the boundary is quiet. By (I_{l-1}^{𝔡'}) on a ball of radius g around W^0, on one side of label surfaces: I^D >= exp(-F_{l-1}^{𝔡'}(W^0)) (c g)^n e^{-C n}, with n the number of free bonds of W_B. By Theorem Z at level l - 1, for each W_B, and (I_{l-1}^{𝔡'}) with the class path lemma between W_B^fl and W^0:

    F_{l-1}^{S', 𝔡'}(W_B) - F_{l-1}^{𝔡'}(W^0) >= x_{l-1}-trop( 𝔹_{l-1}^{S', 𝔡'}(W_B) - 𝔸_{l-1}^{𝔡'}(W^0) ) - 𝔈_{l-1} |tube X(W_B)| - C_Loc n - tails.

Here all rough cells of W_B are in X(W_B): isolated ones too, so they need no separate treatment. The loss 𝔈_{l-1} |tube X(W_B)| is what the discount sigma_{l-1} in 𝔹 is for, so it is absorbed in 𝔹_l at this step and it does not recur. With the fibre's volume C^n and n log(C x_l) from the ball:

    I^N_B / I^D <= exp( -x_{l-1}-trop( a_B(d) - b(d) ) + C(L, a_*) n log x_l + tails ),

with a_B(d) := inf over W_B of 𝔹_l^{S, (Sigma, d)}, b(d) := 𝔸_l^{(Sigma, d)}(V^fl) = 𝔸_{l-1}^{𝔡'}(W^0).

*Step 5: classical.* (i) *Marks pay.* By (CI''') at fixed (Sigma, d), by descent with quiet boundary and clearance: a_B(d) >= a^none(d) + (1/16) A^{Z}(chains of the marks). (ii) *The collar.* a^none and b differ only at depth at least d_x from Sigma, and between them the minimisers are class. By the tail clause, the mixed difference in the quiet data d is at most C e^{-delta d_x} per boundary cell. So a^none(d) - b(d) >= 𝔹_l^{S, 𝔡}(V) - 𝔸_l^𝔡(V^fl) - tail. No kept cell and no near stage occur.

*Step 6: the sum over B.* n <= C(L, a_*) (|tube(X)| + the number of bricks added to B). Each certificate is a chain across the annulus, of 6 bad bricks, and each bad brick contributes a rough cell, so energy at least T^2/C_T by Lemma TE, and x_j/16 of that beats C(L, a_*) log x_j per brick. The number of B with given bricks is at most c_a^{bricks}. So the sum over B in (M) is at most 2. QED of the sketch.

## What follows at once

(A1') *Polymers.* Let V' be class on a region at level l + 1, with boundary 𝔡. Call a *polymer* a multi-level set: rough cells at level l connected at the range of a brick, with its certificates, that is, the chains at any level that block its surface. Polymers are compatible if their annuli are disjoint. Then the mass is the base integral with V_l class times a sum over compatible families, and for a compatible family F and a polymer Gamma, the same three steps give

    N(F u Gamma) / N(F) <= sup over quiet data of I^Gamma / I^class <= prod over cells c of Gamma of z_{l(c)},   z_j := exp( - c x_j T^2 + C 𝔈_j ),

by Theorem Z, (CI''') and Lemma TE. Own-level factors along a chain: Lemma OC below. *The far family F is outside the layers, so it cancels exactly, whatever its size and flux.* If a chain joins two far sets, they are one polymer, and the bound is for the whole of it: that is why no comparison of a rough set with and without a chain is needed. This replaces (A1), and removes the crossing gap. A forced child of a strongly rough parent has no energy of its own beyond the parent's, but Lemma TE counts it: the number of rough cells is at most C_T E/T^2.

Polymers with top below l are inside F_l^𝔡, as gas, level by level. So the fine rough cells, of which there are many per coarse cell, are never expanded at once. Only those in a certificate are.

(FF_j)(U): Theorem Z with R the torus and X all rough cells gives, pointwise at every V: F_j(V) >= F_j(V^fl) + x_j-trop(...) - 𝔈_j |tube X|. That is the upper bound (U), with no far data.

(RAR_j), at a field regular everywhere and under mu: expand the event over polymers containing S, and use (A1'). Own-level factors omega_l = exp(-c x_{l-1} T^2) come from the tropical form. Since the top is regular everywhere, r_1 of the earlier correction does not arise.

(H1)-(H3) with sites: exact. Given a family and its layers, the exterior integrand *is* exp(-F_l^{𝔡 with holes}), class data with quiet holes, by (I_l^𝔡). So there are no tails from far rough regions, no collective Hessian, no global wells.

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

*What (O3) needs of the recursion.* In Step 4 of the proof above, for W_B in the fibre of V, take the reference W_B^# := the level-(l-1) data of a minimiser for 𝒜_{l-1}, so its parents are V off Y_l. And in Step 4, W^0 is a minimiser on the fibre of V^#, so 𝔸(W^0) = Lambda_l. Then F_{l-1}(W_B^#) - F_{l-1}(W^0) = x_{l-1} (Lambda_{l-1} - Lambda_l) + (differences of R at most C_Loc n), as written there. Y_{l-1} depends on W_B, and on the chain below it through the labels, which is allowed as Theorem Z at level l - 1 holds for each W_B.

*Hostile.* (1) Is U^(j+1) really class below level j + 1? It is a minimal lift of a class field, so yes, by the induction of (f'). (2) A bump on a rough parent that is not dropped: V_{j+1} there has flux above T, and W_j e^h has that parent. The parent is then rough with a class chain below, as (O2) wants. Lines through the hull are a fraction f, or the box would be dense, and the mismatch is at most C f^{1/2} K^{1/2} T, by (a) of the hostile pass on Prop 10. (3) r_{I_*} against L: absolute against L_0, as in Prop 10. (4) Is V^# in the formula range? It is class by construction, with flux at most C_a T, from Lemma F and the bump. (5) The tail of Step 5 now reads the difference of two minimisers across a collar, one with a chain's rough data inside. It is the exchange argument, which uses only the collar, so wells inside do not matter. (6) x_i-low: if x were to rise along the chain, the bound falls to the lowest value so far, which is within C(L). This is where a rise could cost, and it costs only C(L) T^2 per cell, against x T^2.

## Prop MD*: the upper chain's (MD*_j) on this map

Statement as in the upper chain's Text 14, with layers on whole blocks with clearance, and quiet := flux at most T, so its eps_0/C_2 is at most T here.

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

1. (I_k^𝔡).
2. Theorem Z at level k.
3. Flow.

*Order.* (a) Classical, unchanged. (b) Theorem Z at level k + 1, from 1, 2 at level k and (a). (c) (I_{k+1}^𝔡): base integral with F_k^𝔡 in the chart, Laplace lemma; polymers by (A1'), (A2); contraction, (SB), (LG), Taylor, data recursion. **(Loc_k) is not in the hypothesis.** The class path lemma with (I) is enough in Step 4, and a far rough region is never read. So Theorem OS and its local form, the rarity of Omega by peeling, the first derivative in its earlier form, and the collective term in the ball are not consumed.

*Not consumed any more, if this stands:* (RP_m[i]) for i >= 1; K_far, K_cut, the cut rule, C_M; the tame reference and its upper bound (UB_j), (g); the fill next to a kept cell (i'); the oscillation form at a rough parent; (G1'); descent at a strongly rough parent as an input to rarity (it stays only inside (OS_j)(a), if the upper chain still asks kappa above what (R3) gives).

## Hostile check

(1) *Is (M) honest?* Numerator: a sum over B, with an upper bound. Denominator: for each fixed B, disjoint events. O_B is the same in both only if parents agree on the outside and on the layers: B contains A_0, so they do. The stop reads no inner field. Yes.

(2) *Does an outermost family exist when V is strongly rough?* It lives in annuli under parents off tube(X), which are class, so children are unforced there; X has a collar d_x. Yes, up to chains, which enlarge B.

(3) *A forced region.* Under a strongly rough V the children in A_0 are rough, and at the next levels too, for a depth about log(pi/T)/(kappa log L). They are inside X(W_B), and their number is at most C_T E/T^2, by Lemma TE. So their loss is at most C_T 𝔈 E/T^2, against x c E: paid for x >= x_*. *Unlike the earlier E_i, no factor (L^4 w^4)^i appears, since the count is by energy and not by multiplying children.* I had written a recursion with such a factor. It is not needed here.

(4) *V^fl has flux up to C_a T, and it must be in the formula range and have a class lift.* T_2 = C_p C_a T, and closure is Text 5.9. Yes. Note V^fl is not quiet. It does not lie on a layer: layers are in annuli, where V is class and unchanged, and at level l - 1, W^0 near Sigma is class with flux at most C T, by Dirichlet data at most T. If a layer at level l - 1 must be quiet, that is a statement on W, on the event. In D only the event's data are read. Yes.

(5) *Quiet data d, and F_{l-1}^{𝔡'} near a sheet.* The fine curvature on a level-j sheet is about T/s_j^2, enormous at the next scale. Theorems 5-7, F, F-D need the local scale: |F| s(x)^2 at most C a_*, with s(x) := s_{j+1} near the free level-j fields under Sigma_{j+1}. So a nest version, with IMS at the local scale. *This is the weakest point: not yet written.* The route is in `library/fibre-propagator.md`, *Nest coercivity*: IMS at the local scale from a one-jump model at U = 1; each patch sees at most one jump, by clearance. Check N, `checks/hard-core--mapped_sharp_two.py`, tests two levels at L = 3 only, at flat data and at constant flux: PASS, with coercivity 9.78 with a whole-block fine layer, the same as with none.

(6) *The tail clause with data d that are rough at the next scale.* Only the collar at level l - 1, where fields are class, is read.

(7) *The base integral in a region: does (I_k^𝔡) really have no surface growth?* Delta R is bounded in derivative norm, as boundary terms are fresh at each level. The vacuum's surface term is a number depending on d. It is common to numerator and denominator in all the ratios, and it does not enter a cross-ratio, being a function of the data on one side, up to tails that are in eps. For a layer with data, this number is not a constant: it depends on d, through energy on the sheet, E_sheet(d). It is on one side: a function of d^I alone, or d^O alone. Yes.

(8) *Marks at a lower level than the bottom of a tube.* Handled by Step 4's S'.

(9) *Does this hide the crossing gap?* Test case: far level-m cell Y strongly rough at fixed top data, and a chain from I to its shadow. In Theorem Z this case is not asked: V at level m has Y in X, so Y is filled too, on both sides of the comparison. **This is the real content, and it changes what is true to ask: a bound between a rough field and its total fill, not between two fields with a common rough part.** Consumers: (A1') has F outside the layers, and if a chain joins, Gamma contains it. I have looked for a consumer of the older form with a common rough part, and I find only: Prop MD with rough faces, which the upper chain no longer asks; (G1') and (UB_j), which it no longer asks; and the earlier form of (A1) with far sites, replaced above. If the upper chain returns to a rough top, this has to be redone, and (RP_m[i]) is the fallback on record.

(10) *A polymer with a huge top-level part.* Its activity is prod z_j over its cells, and its entropy is by cells. Sum over shapes: subcritical, since (range)^4 z_j << 1. Under a rough parent: forced children are not free choices, but they are in the shape, and the sum over shapes has c_a per cell against z_j. Yes.

(11) *What the rarity reads from the flow.* Only x_j >= x_l - C(L) for j < l, in the tropical form. An earlier form read the slope c_0, through an annulus width that could not fit; see the correction above.

(12) *Two different stops, and why.* Comparison (M) stops from outside, so that numerator and denominator share O_B, and there is no sum over fine shapes. But then O_B carries an event on the fields just outside Sigma, so it is not the free exterior integral, and it cannot be the representation used for derivatives. Representation: stop from inside, first quiet family from the polymer outward. Then the exterior is free and it is exactly exp(-F_l^{𝔡 with holes}), and the activity carries the event. So mass = sum over compatible families of prod I^{stop-in}_a times O^free. Dobrushin reads only O^free: the conditional law of site i given the others has density ratio exp(Delta_i Delta_k log O^free), a cross-ratio of a class integral. Rarity (A1') is a statement about masses, so it may be proved by the other stop. A site's absent state is a mixture over quiet d_i, with weights free of k, plus a rare part, so it has the same bound by the product-kernel step. If one tried (M) with the inside stop, the sum over fine shapes costs exp(z_l |surface_l|), growing like L^3 per level: this is the surface excess of an earlier failed route, and it is why the stop direction matters.

