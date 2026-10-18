# Independent numerical scattering check

Disposition: PASS for the specified leading coefficient model and Euclidean, zero-external-momentum finite-rank amplitude. No physical cross section or full-native scattering result is certified.

## Matrix identity and normalization

Set L0=4-adj on the full square lattice, v=U/t on the twenty outer sites, and put positive potential h on the thirty-seven excluded sites, then take h to infinity. The resolvent identity gives the dimensionless Euclidean scattering matrix [v^{-1}+G_epsilon]^{-1}, where G_epsilon=(epsilon+L0)^{-1} restricted to these 57 sites. The hard-core entries of v^{-1} tend to zero. Thus the root expression 1^T[v^{-1}+G]^{-1}1 is exactly the zero-external-momentum amplitude in the ordered relative-coordinate lattice convention. The hard-core limit deletes hopping through excluded sites while retaining diagonal 4; it does not replace 4 by the degree of the punctured graph. The code implements the former, correctly. Finite negative outer potentials do not change this identity.

The checked sets contain 37 core sites and 20 outer sites (4 axis-four, 8 of type (4,1), and 8 of type (3,2)); exact ratios are -8/17, -4/17, and 30305/161109. Integrating one momentum component of the square-lattice Green function gives the code's ratio 2/(2+delta+sqrt(delta*(4+delta))) and denominator pi*sqrt(delta*(4+delta)). No missing factor two was found.

## Independent limiting calculation

I independently evaluated the zero-energy potential kernel at 45 decimal digits and reduced the 57-site matrix to its 11 orbit-constant D4 coordinates. This avoids fitting or extrapolating the finite-epsilon data. Let A(r)=lim[G_epsilon(0)-G_epsilon(r)] and C=diag(v^{-1})-A. With beta=1^T C^{-1}1, the rank-one identity gives 1/T=G_epsilon(0)+1/beta+o(1). The exact elliptic-integral asymptotic is G_epsilon(0)=log(32/epsilon)/(4*pi)+o(1). Consequently:

- beta = -2.34383820836198466293971842576894
- B = log(32)/(4*pi)+1/beta = -0.150856109237922588963761917201
- exp(4*pi*B) = 0.150211079390134206808579213456

The supplied epsilon=1e-12 row differs from this B limit by 8.29e-12 and from the scale limit by 1.56e-11, consistent with finite-epsilon corrections. Its quoted decimal limiting values are supported. Independent code/output are /tmp/neutral_pair_scattering_reviewer.py and .json. Root source acquired an additional potential-kernel calculation during this check; the independent calculation was written separately, uses mpmath and orbit reduction, and its result agrees with that new formulation as well.

The scale means T/t ~ 4*pi/log(scale/epsilon) in this convention. It is not by itself a cross section, a normalized bosonic scattering amplitude, or an identified scattering length. Energy here is negative, -t*epsilon, and external momentum zero is off shell. Analytic continuation and symmetrized-state conventions require separate work. This check does not certify completeness of the native order-ten potential list.

## Source identities

- `/tmp/neutral_pair_scattering.py`: `dd2d9b2d414b3cf8b9233647ce0a537cbcf7dfabeb75f945812113c5364089dd`
- `/tmp/neutral_pair_scattering.json`: `dda9faff6b37c01a22ded8ee1c8490e99e0ea0bbdc167f2b90e29479c6bc6834`
- `/tmp/neutral_pair_scattering_reviewer.py`: `e3b343fb155e817f43911b7771d02308e79922196dfadc27db4e82a0e468cef2`
- `/tmp/neutral_pair_scattering_reviewer.json`: `f6aea2e424dc71ebc55b8827f4652ed5f72d7cbd27ae3ef750bd210c3c4216d5`
