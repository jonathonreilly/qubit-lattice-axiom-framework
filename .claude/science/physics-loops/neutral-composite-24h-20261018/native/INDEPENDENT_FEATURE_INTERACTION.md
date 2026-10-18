# Native fourth-order feature/environment diagonal coupling

The proposed inclusion-exclusion formula is correct for the established bulk plaquette term -kappa sum_(p,z) B_p, kappa=Jz lambda^4/128, evaluated on column backgrounds and finite flipped intervals. This is a diagonal coefficient of the supplied native normal form, not a new added interaction or a scattering theorem.

Let chi_F(p)=|p intersect F| mod 2. Flipping column set F at a bulk layer changes B_p to (-1)^chi_F(p) B_p. Therefore

Delta epsilon_F= kappa sum_p [1-(-1)^chi_F(p)] B_p
               =2kappa sum_(p in boundary F) B_p.

For two flips present at the same layer, the net sign is the product of their two signs. The connected diagonal energy is

E(F,G)-E(F)-E(G)+E(empty)
 =-kappa sum_p B_p [(-1)^chi_F-1][(-1)^chi_G-1]
 =-4kappa sum_(p in boundary F intersect boundary G) B_p.

Only layers in I intersect J contain both flips. For a z-independent column background the bulk connected term is consequently

-4kappa |I intersect J| sum_(p in boundary F intersect boundary G) B_p.

If the background itself changes with z, replace the factorized expression by the actual sum of B_p(z) over the overlap; the overlap length alone is insufficient. Disjoint column sets make the interpretation as two separate features clean. Algebraically the same parity identity also handles overlapping sets, with the combined flipped set interpreted as their symmetric difference rather than their union.

## Explicit example

Index a plaquette by its lower-left transverse corner. For F={(0,0),(2,0)}, its eight toggled plaquettes have x coordinates -1,0,1,2 and y coordinates -1,0. For G={(0,1),(2,1)}, its eight have those same x coordinates and y coordinates 0,1. Their intersection is exactly the four plaquettes with y=0.

On the all-up background each feature has tension density 2kappa times eight =16kappa. The connected density in the overlap is -4kappa times four=-16kappa. Equivalently the combined four-column feature toggles eight plaquettes, with density16kappa, rather than the sum32kappa of the separate features. This direct symmetric-difference count independently verifies the sign and factor.

For a background plaquette B_p=-1 the corresponding shared contribution reverses sign. Thus the coefficient gives an explicit dependence on the supplied local column environment, rather than an unconditional attraction. At this order only shared plaquettes contribute; it is not a long-range pair potential.

## Endpoint and dynamical qualifications

The bulk formula applies away from longitudinal endpoints where the local wall-free plaquette derivation holds. At fixed finite transverse feature shapes, only a bounded number of longitudinal layers near each endpoint fall outside that derivation. Their fourth-order contributions are O(Jz lambda^4) with a shape-dependent constant, independent of a long overlap length. If the overlap is only a few layers long, this remainder can be comparable to the displayed term; no definite total sign should be claimed without computing the endpoints. Growing feature perimeter would also change the remainder constant.

The calculation compares diagonal matrix elements in specified spin configurations. The relevant two-feature wall sector also has off-diagonal native dynamics, including lower-order terms that may be parametrically faster than Jz lambda^4. The negative connected coefficient alone therefore does not establish bound states, an attractive scattering amplitude, a stable two-feature channel, or an effective force law. Those require the complete multiwall sector, admissible states, kinetic mixing, and reference/background energetics.

What is derived here is a concrete microscopic origin for a local environment-dependent diagonal coefficient. It does not derive a measured source/detector coupling, cosmological scalar identification, or a selected ambient background.
