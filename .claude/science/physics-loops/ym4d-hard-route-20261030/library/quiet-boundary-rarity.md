# Rarity with no rough field held fixed

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. The exact Markov property of the levels, with a layer frozen at every level, is Lemma 20.3 of `parts/upper-chain.md`, part of this project, and I use it as stated there after confirming (LOC) for this kernel. Stopping a layer from the outside is the device of the local form of Theorem OS, Text 5.3 of the producer. Balaban's objects are kept. This line is not independent of the Sussman-Alpoge account. Nothing here reads the sibling attempt.

Status: derived at the level of each term. If it stands, it replaces (RP_m[i]) and its index, and much that depended on them, for every consumer I can find. Those proofs stay on record in `library/relative-density-bound.md`. They have not been shown wrong, except by the corrections recorded there.

## Why the hierarchy existed, and why it can go

(RP_m[i]) compared F_m at two fields with the far data fixed, for far data of any flux. Its proof fixed the far children xi'' in numerator and denominator, and took a supremum over xi''. So the level below had to hold for rough far data as well. A rough far cell forces rough children, a chain can run from the changed region to that shadow, and every device that followed (the index i, the kept cells K_far and K_cut, the cut rule, the tame reference, the mixed term C_M) served that one supremum.

The supremum over xi'' is not needed. Both integrals integrate xi''. If a surface of quiet data, at every level, separates the changed region from everything farther out, then the outside is the *same integral* in numerator and denominator, exactly, by the Markov property, and the ratio is a supremum over the quiet data on the surface only. Nothing rough is ever on a boundary. A chain that blocks every surface is simply part of the region, and it pays.

## Setting

*Quiet.* A level-l cell is quiet if its flux is at most T; it is then labelled non-rough with probability one, as chi = 0 on [0, T]. Rough means flux above T. T_2 = C_p C_a T, D_l := { flux <= T_2 }, as in Text 5.9. Nothing here uses a threshold above T for labels.

*(LOC) for this kernel (derived from Text 5.2).* Include the labels as variables: P(labels | V_l) is a product over cells of a function of that cell's flux. Given labels, M_l on a parent bond reads V_l and labels in its two blocks, up to S_* + d_1 level-l cells beyond them, since hulls are per box and a box with at least m_* core cells is dropped whole. A Haar parent reads nothing. So the weight WW := exp(-x_0 A(V_0)) prod_l K(V_l, V_{l+1}) is a product of local positive factors, with range at most 2 L + S_* + d_1 in level-l cells.

*Layer family, with room.* Sigma = (Sigma_l) as in Lemma 20.3 of the upper chain, with two additions asked of it here. (i) Sigma_l is a union of whole level-(l+1) blocks. Check N of `checks/hard-core--mapped_sharp_two.py` shows why this is not a technicality: a thin frozen strip inside a block has a stabiliser mode, a constant rotation of the strip compensated inside its blocks, which is an exact gauge direction at flat data and a soft mode of order a'^2 near flat data. It is the "hole inside a box" of (H1) in the ball. With whole blocks it is gone. (ii) Clearance: Sigma_{l-1} lies at distance at least r_S level-l cells inside the shadow of Sigma_l, with r_S := max(r_*, (4 log L + C)/delta_#). Here r_* is the radius bound of descent, so that the shells of descent around a rough level-l cell do not meet a lower sheet, and the second term is what stops the boundary term from growing: see (I_l^𝔡) below. (iii) Thickness: t_0 := 2 W_*/L + 2 r_S level-(l+1) cells in place of 3, so that the annulus one level down fits inside. These are fixed numbers depending on L and a_*. Frozen data must also be taken on brick cells, `library/fibre-propagator.md`.

*Region densities.* A *boundary datum* 𝔡 at level l is a layer family at levels below l with quiet data, and a set of frozen level-l bonds with quiet data. R_l^𝔡 is the free part at level l: a torus, or a region with holes. For V on R_l^𝔡:

    F_l^𝔡(V) := - log integral over all fields below level l, between the layers, of WW,

and F_l^𝔡 with a mark S: only chains with every cell of S rough. 𝔹_l^{S, 𝔡}(V) := inf over such chains of A(U) - sum_{j<l} sigma_j |R_j(chain)|, with sigma_j := 𝔈_j/x_j below. 𝔸 := 𝔹 with no rough cell.

*Annuli.* For a multi-level set B: annulus_l(B) is the set of level-l cells at distance between 1 and W_* from the level-l part of B, inside the shadow of annulus_{l+1}(B). W_* := C R / T^2, in level-l cells: chosen so that a chain crossing an annulus at level l, with weight at most exp(-c x_l T^2 W_*/R), beats the surface's count L^{3 (m - l)}, using x_l >= x_m + c_0 (m - l) - C(L) and c_0 of order log L. It is a number depending on L and a_* only. A *family in annuli(B)* is a layer family with Sigma_l in annulus_l(B). It is *outermost* if at each level, from the top down, it is the first closed quiet layer met coming from outside. This is decided by the fields on and outside it.

## Theorem Z

*For all l, all boundary data 𝔡, all V on R_l^𝔡, and marks S: let X be the rough cells of V, tube(X) their d_x-neighbourhood in R_l^𝔡, with pockets filled, and V^fl the class fill of V on tube(X), of flux at most C_a T. Then*

    F_l^{S, 𝔡}(V) - F_l^𝔡(V^fl) >= x_l-tropical( 𝔹_l^{S, 𝔡}(V) - 𝔸_l^𝔡(V^fl) ) - 𝔈_l |tube(X)| - x_l e^{-delta d_x} |boundary tube(X)|.

Here 𝔈_l := C(L, a_*) (d_x)^4 log x_l, and "x_l-tropical" is the form sum_i x_{i-1} (Lambda_{i-1} - Lambda_i) + x_l (Lambda_l - 𝔸(V^fl)) of Text 5.3, (RAR_j), read at its end with x_l - C(L).

*What it does not assume.* Nothing on far data: V has all its rough cells in X. And V^fl is class on the whole of R_l^𝔡, so F_l^𝔡(V^fl) is given by (I_l^𝔡).

*Input at each level:*

    (I_l^𝔡)  on class fields on R_l^𝔡: F_l^𝔡 = x_l A_l^𝔡 + vac_l |free cells| + R_l + Delta R_l^𝔡,

with R_l the bulk function read at a class extension, ||R_l||_n <= B_n, and Delta R_l^𝔡 supported near the frozen bonds up to tails, with all derivative norms at most C_n(L), uniformly in 𝔡. No Taylor extraction is needed for Delta R: boundary terms are fresh at each level, as Sigma_{l-1} lies under frozen parents at distance at least r_S level-l cells from any free level-l bond, so the lower boundary's term enters only through a tail. *The count (derived; a hostile check, which raised r_S from an absolute number).* A derivative at free parents y_1, ..., y_n reads Delta R_{l-1} through the lift K, at distance at least r_S parent cells: with the same sums as in (SB), this is at most C^n L^{4 - n} e^{-n delta_# r_S} ||Delta R_{l-1}||_n. At n = 1 this is C L^3 e^{-delta_# r_S}, and it must be below 1/2. With an absolute clearance the boundary term at low order would grow by a power of L per level, a flow of a boundary operator. With r_S >= (4 log L + C)/delta_# it contracts at every order, so ||Delta R_l||_n <= (1/2) ||Delta R_{l-1}||_n + C_n(L): bounded, with no extraction.

## Proof of Theorem Z (level of each term)

*Base.* l = 0: F_0 = x_0 A, equality.

*Step 1: the region.* Let A_0 be the level-(l-1) cells under parents in tube(X), with a collar of d_x level-(l-1) cells. Off A_0 the parents of V and V^fl agree. N := exp(-F_l^{S, 𝔡}(V)), D := exp(-F_l^𝔡(V^fl)).

*Step 2: every configuration has a surface, or a certificate.* Explore from A_0. Given B_i, if annuli(B_i) contain a family, stop. Otherwise there is a chain of rough cells crossing some annulus_j(B_i), by duality for closed surfaces on brick cells. Let B_{i+1} be B_i with such chains and their margins. The process ends at some B, at worst when B is all of R. Each configuration is therefore in N'_B for some B, where N'_B is the mass of configurations with a family in annuli(B) and with the chains of the construction of B, a mark inside B. So N <= sum_B N'_B. *An inequality, not a partition: minimality of B would read fields outside.*

*Step 3: the same outside.* Fix B. Split by the outermost family (Sigma, d) in annuli(B). By Lemma 20.3:

    N'_B = sum_Sigma integral dd O_B(Sigma, d) I^N_B(Sigma, d),    D >= sum_Sigma integral dd O_B(Sigma, d) I^D(Sigma, d),

with O_B the integral of WW outside Sigma, on the event that Sigma is outermost, *the same function in both*, since parents agree there and the event reads only fields on and outside Sigma. I^N_B, I^D are the integrals strictly inside Sigma, with parents V, V^fl; I^N_B carries the mark, and I^D carries nothing. The second is an inequality as these events are disjoint. Hence

    N / D <= sum_B sup_{Sigma, d} I^N_B(Sigma, d) / I^D(Sigma, d).        (M)

All rough cells outside Sigma, of any flux and any size, have gone. No sum over shapes is left on the fine surface except through B, since a surface that merely goes around an isolated rough cell is inside the same event: this is why a stop from outside has no surface excess, and a stop from inside, or a fixed surface, does. (A fixed surface gives N_fixed/D_fixed, and D_fixed/D is about exp(-z_l |surface_l|), which is not comparable to N_fixed/N without a decoupling.)

*Step 4: inside, a recursion with quiet data only.* Let 𝔡' be (Sigma, d) restricted below level l - 1, with Sigma_{l-1} and d_{l-1} as frozen bonds. W_B is the level-(l-1) field inside.

    I^N_B = integral over W_B in the fibre of V, with marks, of exp( -F_{l-1}^{S', 𝔡'}(W_B) ),    I^D = integral over W in the fibre of V^fl of exp( -F_{l-1}^{𝔡'}(W) ).

Let W^0 be the minimiser of 𝔸_{l-1}^{𝔡'} on the fibre of V^fl. It is class with room, by non-concentration: the parent has flux at most T_2, and the boundary is quiet. By (I_{l-1}^{𝔡'}) on a ball of radius g around W^0, on one side of label surfaces: I^D >= exp(-F_{l-1}^{𝔡'}(W^0)) (c g)^n e^{-C n}, with n the number of free bonds of W_B. By Theorem Z at level l - 1, for each W_B, and (I_{l-1}^{𝔡'}) with the class path lemma between W_B^fl and W^0:

    F_{l-1}^{S', 𝔡'}(W_B) - F_{l-1}^{𝔡'}(W^0) >= x_{l-1}-trop( 𝔹_{l-1}^{S', 𝔡'}(W_B) - 𝔸_{l-1}^{𝔡'}(W^0) ) - 𝔈_{l-1} |tube X(W_B)| - C_Loc n - tails.

Here all rough cells of W_B are in X(W_B): isolated ones too, so they need no separate treatment. The loss 𝔈_{l-1} |tube X(W_B)| is what the discount sigma_{l-1} in 𝔹 is for, so it is absorbed in 𝔹_l at this step and it does not recur. With the fibre's volume C^n and n log(C x_l) from the ball:

    I^N_B / I^D <= exp( -x_{l-1}-trop( a_B(d) - b(d) ) + C(L, a_*) n log x_l + tails ),

with a_B(d) := inf over W_B of 𝔹_l^{S, (Sigma, d)}, b(d) := 𝔸_l^{(Sigma, d)}(V^fl) = 𝔸_{l-1}^{𝔡'}(W^0).

*Step 5: classical.* (i) *Marks pay.* By (CI''') at fixed (Sigma, d), by descent with quiet boundary and clearance: a_B(d) >= a^none(d) + (1/16) A^{Z}(chains of the marks). (ii) *The collar.* a^none and b differ only at depth at least d_x from Sigma, and between them the minimisers are class. By the tail clause, the mixed difference in the quiet data d is at most C e^{-delta d_x} per boundary cell. So a^none(d) - b(d) >= 𝔹_l^{S, 𝔡}(V) - 𝔸_l^𝔡(V^fl) - tail. No kept cell and no near stage occur.

*Step 6: the sum over B.* n <= C(L, a_*) (|tube(X)| + the size of the chains in B). The chains' energy is at least T^2/C_T per rough cell at each level, by Lemma TE, and x_j (1/16) of that beats C(L, a_*) log x_j per cell of chain. The number of B with a given chain is at most c_a^{cells}. And a chain crosses an annulus at level j in at least W_*/R hops. So the sum over B in (M) is at most 2. *The count over the surface at level j, L^{3 (l - j)} |boundary tube|, is beaten by the choice of W_*, which reads the slope c_0 of the flow: this is the one place where asymptotic freedom enters the rarity.* QED of the sketch.

## What follows at once

(A1') *Polymers.* Let V' be class on a region at level l + 1, with boundary 𝔡. Call a *polymer* a multi-level set: rough cells at levels at most l, including level l, connected at range W_* level by level and through parents, with the chains that block its annuli. Polymers are compatible if their annuli are disjoint. Then the mass is the base integral with V_l class times a sum over compatible families, and for a compatible family F and a polymer Gamma, the same three steps give

    N(F u Gamma) / N(F) <= sup over quiet data of I^Gamma / I^class <= prod over cells c of Gamma of exp( - c x_{l(c)} T^2 + 𝔈_{l(c)}/... ),

so a factor z_j per rough cell at level j, by Theorem Z, (CI''') and Lemma TE. *The far family F is outside the layers, so it cancels exactly, whatever its size and flux.* If a chain joins two far sets, they are one polymer, and the bound is for the whole of it: that is why no comparison of a rough set with and without a chain is needed. This replaces (A1), and removes the crossing gap. A forced child of a strongly rough parent has no energy of its own beyond the parent's, but Lemma TE counts it: the number of rough cells is at most C_T E/T^2.

Polymers with top below l are inside F_l^𝔡, as gas, level by level. So the fine rough cells, of which there are many per coarse cell, are never expanded at once. Only those connected to a level-l rough cell are.

(FF_j)(U): Theorem Z with R the torus and X all rough cells gives, pointwise at every V: F_j(V) >= F_j(V^fl) + x_j-trop(...) - 𝔈_j |tube X|. That is the upper bound (U), with no far data.

(RAR_j), at a field regular everywhere and under mu: expand the event over polymers containing S, and use (A1'). Own-level factors omega_l = exp(-c x_{l-1} T^2) come from the tropical form. Since the top is regular everywhere, r_1 of the earlier correction does not arise.

(H1)-(H3) with sites: exact. Given a family and its layers, the exterior integrand *is* exp(-F_l^{𝔡 with holes}), class data with quiet holes, by (I_l^𝔡). So there are no tails from far rough regions, no collective Hessian, no global wells.

(A2), first differences in V': the vector field on lines at distance about L/C from hot cells is as in Text 5.3, and it now reads D F_l at class bonds across a quiet layer, so only (I_l^𝔡). (D), the influence between two polymers: the cross-ratio of the exterior class integral in the two polymers' boundary data, Prop MD* below, Lemma HS-P and Theorem F-D.

## Prop MD*: the upper chain's (MD*_j) on this map

Statement as in the upper chain's Text 14, with layers on whole blocks with clearance, and quiet := flux at most T, so its eps_0/C_2 is at most T here.

*Decomposition.* Z^*(d^I, d^O) = T^* (1 + gas), with T^* the integral over V_j class between the layers of exp(-F_j^𝔡), and the gas of polymers with top j, floating.

*Step 1: the class integral across the middle third M.* Fix m := V_j on M, class. Then exp(-F_j^𝔡(p, m, q)) with p, q class is an integral over lower levels with class parents everywhere. Choose lower layers in the inner and outer thirds of the shadow of M, stopped from the inner and the outer side: this is a product kernel, so a cross-ratio at most 4 times that of Z^*_{j-1} at thickness L D/3, on the event that both exist. On the complement a chain crosses the shadow under class parents: it is rare uniformly in p, q, by (M). So F_j^𝔡 = u(p, m) + v(m, q) + E, |E| <= 4 eps_{j-1}(L D/3) + (crossing). This is where the earlier proof needed rough p, q; here p, q are class, since rough sets are in polymers.

*Step 2: the integral over m.* As Step 4 of Prop MD: convexity in the chart, Hessian within small relative distance of M_m, the Schur complement at a reference, by shifting y with m. Interpolate on m, covariance by Lemma HS-P and HS-C with A = M_Y^-1, Theorem F-D. So log CR(T^*) is at most C(L) x |A| (e^{-rho D/3} + z^{1/2} e^{-rho_s D/3}) + 4 eps_{j-1}.

*Step 3: the gas.* Total covariance, with sites the polymers. Dobrushin with hard core at range R_c >= C_R (log(x |A|) + log L)/rho, as Step 5 of Prop MD. The influence of k on i is the cross-ratio of the exterior class integral, at most C x |A|^2 e^{-rho d(i, k)}. A large polymer is one variable. Compatible means disjoint annuli, and connection is at range max(W_*, R_c).

*Closure.* As Step 6: c_t := rho/3, and the term from level j - 1 has a much larger exponent.

Shapes in a quadruple may differ, since m is common and the shapes enter p, q only.

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

(12) *Two different stops, and why.* Comparison (M) stops from outside, so that numerator and denominator share O_B, and there is no sum over fine shapes. But then O_B carries an event on the fields just outside Sigma, so it is not the free exterior integral, and it cannot be the representation used for derivatives. Representation: stop from inside, first quiet family from the polymer outward. Then the exterior is free and it is exactly exp(-F_l^{𝔡 with holes}), and the activity carries the event. So mass = sum over compatible families of prod I^{stop-in}_a times O^free. Dobrushin reads only O^free: the conditional law of site i given the others has density ratio exp(Delta_i Delta_k log O^free), a cross-ratio of a class integral. Rarity (A1') is a statement about masses, so it may be proved by the other stop. A site's absent state is a mixture over quiet d_i, with weights free of k, plus a rare part, so it has the same bound by the product-kernel step. If one tried (M) with the inside stop, the sum over fine shapes costs exp(z_l |surface_l|), growing like L^3 per level: this is the surface excess of an earlier failed route, and it is why the stop direction matters.

(11) *W_* depends on c_0's slope.* If the flow had a plateau with x_l nearly constant over many levels, the surface count would win. The flow bound x_l >= x_m + (m - l) c_0 - C(L) is Theorem P1, which is itself an implication. So rarity reads the flow, in the order: flow at levels below, hence in H(k). Fine: it is in the induction, and Step 6 at level l reads x_j for j < l only.
