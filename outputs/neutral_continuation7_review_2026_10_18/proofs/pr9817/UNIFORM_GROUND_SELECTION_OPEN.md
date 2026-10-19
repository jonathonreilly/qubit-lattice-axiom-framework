<!-- Original PR9817 source SHA256 963e871b24cd3bfbbb9d3bb75a687693405cfb07476e7599ad380ebf2261bc0f. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Deep focused check: uniform plane-character selection

Disposition: NOT PROVED; retain the selected-sector premise on R~lambda^-p, 1<p<2. The proposed relative line-decoration estimate is a plausible sufficient route, but it does not follow from the existing finite-order normal forms or fixed-R leading coefficient. I found no native counterexample to all-positive selection. The obstacle is a missing uniform relative expansion, not an incorrect leading sign.

Reviewed `/tmp/neutral-uniform-character-route.md` and the native fixed-size ground-selection and polynomial-grid arguments. No shared files were edited.

## What can already be bounded rigorously

For the leading matching histories at L=10, a partial row with c runs has Q=4c and leading flux energy Delta_c c lambda^4. Any retained connected diagonal correction with the proven scalar-subtracted form bound C lambda^2 Q in the rescaled column Hamiltonian changes this denominator by at most a relative C'lambda^2, uniformly in c. This is a real improvement over an extensive norm bound: long flat interiors do not generate an area or run-length cost.

Likewise a specified fixed-order correction to a nearest-column winding vertex has a uniformly bounded relative O(lambda^2) coefficient; the explicitly computed plaquette-dependent detour is an example because its Pauli factors have norm one. For a leading history with n=R/2 vertices and n-1 denominators, if those bounds held for exact resummed quantities, elementary product estimates would give

|weight_exact/weight_leading-1| <= exp(C R lambda^2)-1.

All leading matching weights have the same sign, so the same bound holds after summing their positive absolute weights. No lower bound on an individual ordering probability is needed for that step. Since R lambda^2 tends to zero for p<2, this would preserve the primitive-line sign.

The emphasized condition is exact resummed quantities. The available bounds establish this for any chosen fixed retained order, not the complete amplitude at a winding order growing as R.

## Why fixed-order control cannot finish the proof

The primitive coefficient has scale t_R lambda^(3R+4), with log magnitude -3R log(1/lambda)+O(R). An absolute R^2 lambda^M remainder at any fixed M is much larger. Even exp(-c/lambda) does not resolve that scale when p>1. Constants in the fixed-order commutator estimates depend on the order; setting that order proportional to R without bounding their growth is invalid.

Evenness in lambda does not cure this: an expansion in even powers may have coefficients growing as (2n)!, rather than n!. It does not automatically supply a uniform convergent expansion in lambda^2 or an optimal order proportional to lambda^-2. Thus R lambda^2 small is the desired conclusion's small parameter, not an already established convergence parameter for the exact microscopic reduction.

The exact high-wall identification and the finite-order Q normal form also cannot simply be promoted to an exactly local, all-Q block diagonalization. The latter would introduce an exact emergent conservation law not established by finite-order averaging. It is sufficient to construct the needed low-energy effective amplitudes, but that construction must control its nonlocal winding tail relative to its leading native order.

## Where history counting must be strengthened

A primitive row has O(R) event positions and O(R) time-ordered events. Merely requiring a correction to touch the row does not distinguish O(R) local vertex insertions from O(R^2) independent event/position attachments. The diagonal Q-relative bound handles diagonal energy renormalizations after proper resummation; it does not bound all off-diagonal excursions or their temporal ordering.

A useful exact expansion would separate:

1. Local dressed winding vertices and diagonal flux-energy corrections, with absolutely convergent uniform coefficients and relative bounds.
2. Irreducible excursions leaving the minimal matching histories, with a weighted summation bound after disconnected vacuum bubbles cancel.
3. Connected contributions whose support winds around more than one line.

One must prove that these exhaust the exact low-energy amplitude, not just formal words through a fixed order. In particular a fixed-order quasi-local remainder with an ordinary exp(-mu*range) tail is insufficient: at range R it need not carry the necessary lambda^(3R) suppression. The tail must retain native flip/weighted-order information as well as spatial decay.

## Primitive-line signs are not sufficient

Let the flat group be generated by R row and R column flips, with the single relation that the product of all 2R generators is identity. Choose a consistent representative subset S for each group element, retaining singleton representatives for primitive lines. Write the correction to the leading convolution as sum_S a_S G_S.

A sufficient character-incidence norm is

sup_j sum_(S containing j) |a_S| <= epsilon(lambda) t_R lambda^(3R+4),

with epsilon tending to zero. For a character with k negative generator values, |1-chi(S)| is bounded by twice the number of its negative generators in S. Its correction to the energy difference from the all-positive character is therefore at most 2k epsilon t_R lambda^(3R+4), whereas its leading penalty is 2k t_R lambda^(3R+4). This proves selection if the incidence bound holds, without losing an additional factor R from a global norm. The group relation imposes even k and must be retained.

The next smallest multi-line pattern, one row plus one column, changes 2R-2 columns. Its minimal weighted order is 3(2R-2)+4=6R-2, later than the primitive line by 3R-6. This strongly suggests suppression. It does not sum all histories: a uniform exponential-in-support coefficient bound and a summable polymer count would still be needed. Those cannot be inferred from fixed-R order counting alone.

## Exact sign shortcut is unavailable in the obvious basis

The local XX/YY anticommutation cycle gives a negative product of configuration-space edge amplitudes around a four-step closed path. That product is invariant under diagonal phase gauges, whereas four nonpositive stoquastic entries would have positive product. Thus no simple configuration-phase change proves exact native Perron–Frobenius positivity. Negative primitive winding coefficients do not imply sign-definite longer effective words. A non-diagonal positivity or sector-ordering theorem would require a separate explicit proof.

## Concrete next proof target

The sharp useful target is an exact connected low-energy expansion carrying both spatial support and weighted native order, with a primitive-line relative decoration bound and the character-incidence estimate above. The local Q-relative denominator estimate already supplies one component. What remains is a uniform all-history/long-support estimate; no generic assertion of convergent perturbation or locality substitutes for it.

Accordingly the current polynomial-grid neutral-pole theorem should continue to specify its plane sector. Fixed-R actual-ground selection and the existence-only ordered diagonal sequence remain valid. No failure of the proposed all-positive sector has been shown, but the exp(C R lambda^2)-1 estimate is not yet an established property of the exact native winding amplitude.
