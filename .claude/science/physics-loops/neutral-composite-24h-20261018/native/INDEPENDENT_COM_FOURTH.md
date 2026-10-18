# Fourth-order longitudinal COM coefficient check

Read the actual `native/neutral_slow_fourth_kernel.json`, the coefficient construction in `native/FIXED_ORDER_COMPOSITE_POLE_PROOF.md`, and the earlier local long-arm argument. The JSON contains ell=5 and ell=6 controls, not an all-length numerical scan. At both lengths it gives single-end growth by one 19/64, growth by two -13/256, and two tested combined-endpoint motions zero after exact folded cancellation. The proposed COM factors and bulk symbol are correct.

## Fourier factors

Use the physical interval center c=(l+r)/2. Moving one endpoint by h changes c by +/-h/2. Longitudinal inversion equates the left and right native amplitudes, so the two contributions to a length-h link are 2 a_h cos(hp/2). Thus

h=1: 2(19/64)cos(p/2)=(19/32)gamma;
h=2: 2(-13/256)cos p=-(13/128)cos p.

A Hermitian length-link coefficient multiplies S^h+S*^h. Hence, with the separately checked diagonal ell/8+29/192,

Vbulk(p)=29/192 I+(19/32)gamma(S+S*)-(13/128)cos p(S^2+S*^2).

Its zero-relative-wave-number symbol is

c(p)=29/192+(19/16)gamma-(13/64)cos p,

which at p=0 is 109/96. No additional factor of two belongs in either hopping coefficient. For reference c(p)=109/96-(3/64)p^2+O(p^4).

## Why this is a long-arm statement rather than a fit

At order four every transition contains exactly four transverse flips; diagonal denominators do not change spin configurations. For ell>=5, changing the unordered column pair is impossible by the existing Hamming bound (at least 2ell physical spin changes, versus at most eight from four edges). With the same column pair, changing the length by h requires at least 2|h| transverse edges for axial separation two, so |h|<=2.

A single-end growth by one requires two transverse edges on the added layer. Any additional pair in a diagonal-return excursion can affect its connected coefficient only on that layer or an adjacent layer: all transverse edges act within a z layer and the unperturbed energy couples only neighboring z layers. A distant two-edge bubble has additive intermediate energy and cancels from the canonical connected coefficient against folded terms. Growth by two exhausts the four edges on the two added neighboring layers. Therefore these surviving one-end coefficients depend only on the fixed local endpoint configuration, which is identical at ell=5, ell=6 and every longer interval. Translation and reflection supply the corresponding shrinkages and left-end entries.

Combined moves of both ends exhaust four edges in two groups of two at the two endpoint layers. For ell>=5 those groups have disjoint spins and disjoint incident longitudinal energy bonds. There is no connected fourth-order contribution between them. The two independent endpoint processes are iterations of lower-order effective motion, not an additional fourth-order Hamiltonian entry. Canonical folded subtraction removes their disconnected contribution; the JSON's -1/8 +1/8 cancellation is the direct finite control. This accounts for both simultaneous growth/contraction and interval translation, rather than assuming away an untested center-hop term.

For diagonal entries, four transverse edges returning all spins must have even incidence in each individual layer. They are either a same-layer square/repeated-edge graph or two two-edge return groups. The latter are connected through H0 only when their layers are adjacent. Thus their diagonal connected support is bounded independently of ell. Counting bulk translations gives an affine function of ell plus fixed endpoint constants; the previously checked local diagonal coefficient is ell/8+29/192. No term spanning two distant ends survives in the long-arm connected coefficient.

These arguments use the linked/canonical folded cancellation already established for the coefficient construction. An arbitrary nonlocal within-band gauge transformation could obscure this local decomposition; the claim concerns the specified local normal form/canonical long-slow block, whose order-four equality was separately established. Short intervals remain a finite boundary matrix and are not assigned these bulk entries without checking.

## Use in the pole expansion

Conditional on the already checked momentum-dependent Airy/outgoing construction, the order-lambda^4 coefficient is c(p)+(2+a_p)/8. The c(p) part is real for real p; its imaginary contribution is therefore entirely the boundary scattering term at this order. The calculation does not independently establish that pole construction, error-controlled energy derivatives, or a full microscopic propagating pole. It does establish that the retained native long-arm K4 term has the stated p dependence and that there is no missing long-arm fourth-order rigid-translation entry.
