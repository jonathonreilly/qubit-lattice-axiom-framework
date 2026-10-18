# Native finite-array ground-band tunneling

Status: bounded-support. Fix an even transverse M by M periodic grid, M>=4,
and an open vertical height L>=6, also even. Take the supplied directional
XX/YY/ZZ Hamiltonian with Jx=Jy=lambda Jz>0. All dimensions are fixed as
lambda tends to zero. This is NOT the growing periodic cube limit of the
microscopic ground-window theorem.

## 1. Two exact finite-dimensional reductions

At lambda=0 the aligned-column manifold is isolated by a nonzero vertical
wall gap. An analytic, symmetry-preserving Kato direct rotation gives its
exact continued block. Every coefficient of order p is a sum of p native
transverse bond operations interspersed with functions/projectors of H0.
Those intermediate factors are diagonal in physical spin coordinates.
Consequently a matrix entry flipping k complete columns vanishes through
orders p<kL/2. The statement includes folded terms: folding does not create
extra physical flips.

The second-order block is scalar. The first nonconstant diagonal term is
-K sum_square P, K=(L+14)Jz lambda^4/128. The first offdiagonal entry flips
nearest-neighbor column pairs with amplitude -t, t=Jz lambda^L/2^(L-1).
These are the previously derived native coefficients for open columns.
For even L both X and Y edges give the same logical XX sign. A nonneighbor
pair cannot saturate the order-L bound, since every minimal physical edge
would have to touch only the two target columns.

Subtract the scalar analytic part and divide by Jz lambda^4. The leading
operator has the plaquette-positive manifold P+ as an isolated lowest
space. A second exact finite-dimensional analytic reduction is therefore
available. All higher diagonal coefficients have positive powers after
this division; the order-four diagonal term is already in the unperturbed
operator and its resolvents. Its gap supplies the small physical denominators
of order Jz lambda^4. Exact plane symmetry makes any diagonal operator
constant on the gauge patterns s_xy=a_x b_y. Thus diagonal corrections
cannot select among these patterns.

## 2. Valuation of the first offdiagonal ground transition

Distinct gauge patterns differ in at least M columns. Equality corresponds
to flipping one complete row or column. A second-reduction path with b
nontrivial offdiagonal aligned-block events, flipping k_i>=2 columns at each
event, has total native degree at least (L/2) sum_i k_i. Its b-1 small
resolvents can lower the physical lambda valuation by 4(b-1). Diagonal
perturbative insertions have strictly positive divided-block degree and
cannot improve the bound. Since b<=sum_i k_i/2 and sum_i k_i>=M,

    valuation >= (L/2) sum_i k_i - 4(b-1)
              >= (L-4) sum_i k_i/2 + 4
              >= nL-4(n-1),             n=M/2.

Because L>4, equality requires exactly n events, each a minimal nearest-
neighbor pair flip, covering the target row/column without repetition.
Grouping several pairs into one primitive coefficient loses a small
resolvent and is higher order. Additional pair events cost positive degree.
Proper subsets of a minimal row matching lie outside P+, so no intermediate
return is folded. Lower-order P+ operators are scalar; their subtraction
cannot change this first nonconstant offdiagonal coefficient. This is an
asymptotic argument at fixed finite sizes, not a uniform all-size bound.

## 3. Coefficient and its sign

There are exactly two perfect matchings of the even row cycle. A proper
subset of one matching, with r occupied runs in cyclic dimer order, has
4r bad plaquettes and excitation energy 8Kr. The n bond numerators have
sign (-1)^n and n-1 resolvents sign (-1)^(n-1), giving a negative amplitude.
For one matching the path sum is

    W_n = sum_orders product_(proper prefixes S) 1/r(S)
        = binom(2n-2,n-1).

For completeness, map dimer occupations to spins on an n-site cycle.
Domain walls number 2r, and a dimer flip toggles its two neighboring domain
walls. The distinct-edge cycle coefficient has the time integral
U_n=integral dω/(2π) [2/(1+ω²)]^n
=binom(2n-2,n-1)/2^(n-1). Each site has exactly two insertions, so no Gaussian
factorization is assumed. Multiplying by 2^(n-1) converts wall denominators
to run denominators and gives W_n. For n=2 the two parallel dual edges can
also be checked directly: W_2=2.

Therefore the first nonconstant ground-band operator is

    -tau_M [sum_x R_x + sum_y C_y],
    tau_M = 2 binom(2n-2,n-1) t^n/(8K)^(n-1) > 0.

All omitted nonconstant terms are o(tau_M) for the fixed dimensions.
For M=4,L=6 this gives tau_M=Jz lambda^8/320. The exponent is smaller than
the minimum twelve native bond operations because of the intervening
plaquette denominator lambda^4. Bare word order is not a splitting exponent.

## 4. State and source are consequences, with a charged-channel boundary

The row/column flips generate the regular representation on P+, with the
single relation product_x R_x product_y C_y=I. The leading all-plus
character is unique. Every other allowed character flips an even number of
signs; the smallest energy cost is 4tau_M. For sufficiently small lambda at
fixed M,L this gives a unique native ground character and

    gap = 4tau_M + o(tau_M).

A physical local Z_xyz projects to the column sign a_x b_y. In the character
basis it toggles precisely R_x and C_y, with matrix element one. Analytic
dressing and the finite-dimensional reductions tend to the identity, so
its corresponding native low-energy spectral weight tends to one. For the
M=4,L=6 example the line gap is Jz lambda^8/80 + o(lambda^8).

This is a CHARGED longitudinal-spin transition. Plane-charge conservation
confines correlations of translated single-Z probes to the same vertical
column in a symmetry-invariant state. The original neutral distance-two
readout projects to identity and cannot connect distinct ground characters.
Thus the derived ultrasoft line is not a neutral scalar mediator. A large
feature has produced a native scale and a native coupling in this finite
problem, but has not supplied a three-dimensional cosmological scalar.

The Hamiltonian, finite geometry, anisotropy, ground-state problem and
measurement interpretation remain inputs. No empirical calibration or
independent observation test is used. The displayed runner diagonalizes
only the 16-column coefficient model, in 512-dimensional character sectors;
it does not diagonalize the 96-physical-qubit native example.
