# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Exact native scalar double-commutator check

Let A_e be the two-spin Pauli product on a compass bond, H_a=-J sum_(e parallel a) A_e, and H=sum_a H_a. Define Q=sum_a[H_a,[H,H_a]]. This is an observable constructed from the existing Hamiltonian; it is not an added interaction.

## Bond-algebra derivation

All a-axis bond operators commute with one another. For a b-axis bond f=(i,j), b!=a, let K_af be the sum of the a-axis bond operators that anticommute with A_f. Other a-axis bonds commute with both A_f and K_af, so

[sum A_e,[sum A_e,A_f]]=4 A_f K_af^2.

The signs from H_a=-J sum A_e and H_b=-J sum A_f give

Q=4J^3 sum_(b,f parallel b) sum_(a!=b) A_f K_af^2.

On a nondegenerate periodic cube with side at least three, K_af has four distinct terms: the two a-bonds incident on i and the two incident on j. Its square is 4I plus twice the sum over its six unordered distinct pairs. Therefore the bond contribution is 32J^3 sum_f A_f=-32J^2 H. The proposed J=1 expression is correct.

## Explicit real-space four-spin terms

Let c be the third axis distinct from a,b, and j=i+e_b. The remaining contribution for each ordered axis choice a!=b and each b-bond is

8J^3 A_f [sigma_(i-e_a)^a sigma_(i+e_a)^a
          +sigma_(j-e_a)^a sigma_(j+e_a)^a]

-8J^3 sum_(s,t=+/-1) sigma_i^c sigma_j^c
                         sigma_(i+s e_a)^a sigma_(j+t e_a)^a.

For the first line, the two a-bonds share an endpoint, so their equal Pauli factors cancel there. For the second line, sigma^b sigma^a=i epsilon_(bac) sigma^c at both endpoints, producing the minus sign. Thus these are products of three native bond operators but generally four-spin Pauli strings, not three-spin terms. This is an uncollected local sum; any finite-size identifications may be combined afterward.

Independent scratch control `/private/tmp/neutral_native_Q_algebra_check.py` computes both the nested commutators and this explicit four-spin expression using binary Pauli multiplication on the full periodic 3x3x3 geometry. All 1053 nonzero combined coefficients agree exactly, with maximum discrepancy zero. No Hilbert-space eigensolve or reduced-sector representation was needed.

On open boundaries the same K_af identity remains exact, but the number of incident anticommuting bonds varies, so the uniform -32J^2 H bond simplification must be replaced by its local bond count. Length-two periodic bond duplication likewise requires separate counting.

## Spectral sum rule and symmetry

For an energy eigenstate |0> of energy E0,

<0|Q|0> = 2 sum_(a,n) (E_n-E0) |<n|H_a|0>|^2.

This follows by expanding the double commutator as 2 H_a H H_a-H_a^2 H-H H_a^2. It is nonnegative for a ground state, or for a lowest state within a preserved sector because H_a preserves that sector. It need not be nonnegative in an arbitrary excited state. Q is not a positive operator in general; for finite matrices its trace is zero, so a nonzero Q cannot be everywhere positive.

At isotropic coupling, cubic spatial/spin rotations permute the H_a, leaving H invariant. Their sum of double commutators is consequently a cubic scalar. For anisotropic couplings this full cubic invariance is absent unless the parameter transformation is included.

## Meaning of the finite response

A resolved finite-cube Q transition at the same energy as an S transition is compatible with two scalar probes reaching the same eigenstate. It does not identify Q with S, prove a unique scalar mode, or supply a physical detector coupling. The expectation sum rule measures energy-weighted directional fluctuations of the chosen state. The response spectrum of Q is a distinct higher composite diagnostic. Neither its algebraic generation from H nor its cubic-scalar symmetry derives an empirical measurement bridge, a cosmological field, or a new autonomous interaction.
