# Independent fully open rectangle coefficient check

Checked `/private/tmp/neutral_open_rectangle_root.md`. The leading matching coefficients and source arithmetic are correct for the stated fully open 4 by 6 transverse array, with open odd longitudinal height five. This is a finite whole-array coefficient calculation, not an embedded feature in a larger lattice.

## Boundary costs and matching uniqueness

To reverse a row of even length at the minimum number n of pair flips, every row site must be covered exactly once. The open path has exactly one perfect matching; edges leaving the row cannot appear at this minimum order. A subset of these dimers produces a bad plaquette at every boundary between a flipped and an unflipped dimer. There are c=1 neighboring plaquette strips for an outer row and c=2 for an interior row. Each bad plaquette costs 2K, hence the intermediate denominator is 2K c w, where w counts open-path domain walls. The analogous statement holds for columns.

## All-length open-path identity

For n matching dimers, let a=2Kc. The ordered-path denominator sum is

sum_permutations product_(proper intermediate subsets S) [a w(S)]^(-1) = (2/a)^(n-1).

A direct proof uses n flip times t_i, fixes t_n=0, and integrates exp[-a sum_(i=1)^(n-1)|t_i-t_(i+1)|] over the other n-1 times. Decomposing into all orderings of the times gives exactly the ordered-path denominator sum: each positive interval between successive flips contributes its duration times the number w of crossing path edges. Conversely the n-1 edge differences form independent real coordinates on the anchored path, with unit Jacobian, so the integral factorizes into n-1 copies of integral exp(-a|u|)du=2/a. This establishes the identity for every n, without extrapolation from small n.

Consequently the off-diagonal amplitude is -tau, tau=t^n/(Kc)^(n-1). The negative sign follows from n factors -t and n-1 negative resolvent denominators. Independent exact Fraction subset recursion at Kc=1 verifies tau/t^n=1 for n=2 through 9 in `/private/tmp/neutral_open_rectangle_check.py`. In particular n=2 gives t^2/(Kc), and n=3 gives t^3/(Kc)^2.

## Four by six coefficients and readout

Four rows of length six give two c=1 and two c=2 terms:

a=(2+2/4)t^3/K^2=(5/2)t^3/K^2=10 Jz lambda^7/361.

Six columns of length four give two c=1 and four c=2 terms:

b=(2+4/2)t^2/K=4t^2/K=2 Jz lambda^6/19.

Here t=Jz lambda^5/16 and K=19 Jz lambda^4/128 were independently checked previously. Thus the maximal-center neutral block -aX-bZ has gap 2sqrt(a^2+b^2), leading 4 Jz lambda^6/19. In this leading two-term model its first geometric expansion correction is order lambda^8.

The open transverse geometry changes constant matching prefactors, not logarithmic source derivatives. Therefore r3-r2=63/(38Jz) still holds. The derivative-source transition magnitude is ab|r3-r2|/sqrt(a^2+b^2), leading

315 lambda^7/6859.

These coefficients agree exactly with the root draft. Their conversion to the full native physical source still depends on the separately checked effective-source connection. This check does not establish all microscopic remainder orders, a global gap, or ground-sector classification. In particular the quoted native O(lambda^8) source remainder requires the separate native power-counting/connection argument; it is not proved merely by the matching identity.

Removing transverse periodicity removes wraparound assumptions but retains a chosen finite open geometry. Reinstating exterior bonds changes both the low manifold and denominators and requires a new calculation.
