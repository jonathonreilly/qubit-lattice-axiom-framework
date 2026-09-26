# Referee: the general tie of bond and coin rotations, attempt 2

Attempt `w-macbookpro9927a-jf66c`. The constraint matrix is rebuilt here. The attempt's script is not imported. Part (b), already refereed at reach one, is not redone.

A tie reads the site rotation through a translation-invariant linear map into the nine bond strains. It is consistent with an energy blind to coin rotations when the adjoint of that map kills the bond current on every stationary state.

## Verdicts

**Reach one, as a check of the symbol.** The same rows reproduce the refereed ranks: 108 unknowns, 21 relabellings, rank 81 on `4³`, and rank 87 on both `6³` and `8³`.

**Reach two.** The stencil is the 38 sites within taxicab distance 2 of either end of the bond. That is 342 unknowns per rotation component. The radius-two ball has 25 sites, so the relabelling family has 75 members per component. Those 75 vectors are independent over the rationals. On the `8³` torus the symbol produces 472832 rows. Their rank is 267 over both `F_1048681` and `F_1049281`, and every relabelling dots to 0 on every row. A nonzero minor modulo either prime is nonzero over the coefficient field, so the rank over that field is at least 267 and the nullity is at most 75.

**Why the relabellings solve.** If `B_a^j(x) = ξ_j(x+e_a) - ξ_j(x)`, the pairing with the current telescopes to `-ξ · div J`. Stationary states have vanishing divergence, so the pairing vanishes on `Z³` and on every torus. The solution space therefore contains the 75 relabellings and has dimension at most 75, hence equals them.

**From the torus to `Z³`.** Stencil offsets differ by at most 5, which is less than 8, so the torus does not alias two stencil sites. Every torus constraint is also a constraint on `Z³`. The solution space on `Z³` is therefore no larger, and the relabellings remain solutions.

## What stays open

Reach three, on a `12³` torus, was not rebuilt. A reach-independent spanning lemma for the currents was not proved.

## Result

HIT: confirmed. At reach two the ties are exactly the relabelling ties on the radius-two ball, 75 per component, so the nine-plus-three variables stay forced.
