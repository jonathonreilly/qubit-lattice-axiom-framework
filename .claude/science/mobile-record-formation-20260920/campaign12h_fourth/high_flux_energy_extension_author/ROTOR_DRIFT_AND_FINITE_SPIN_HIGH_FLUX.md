# Exact rotor energy drift and the moving finite-spin input

Personal author continuation, 2026-09-24. This extends the frozen
[actual-birth note](../high_flux_energy_author/HIGH_FLUX_ACTUAL_BIRTH_ENERGY_SPREAD.md)
in the **supplied compensated model**. The original note remains unchanged.
The fresh independent reconstruction and any subsequent comparison have
their own source-bound records; this note itself is author evidence.

The cube has vertices 0,...,7, A={0,3,5,6}, and its twelve edges oriented
from smaller to larger endpoint. The normalizable input Omega_n has all A
records positive, B sites vacant, and circulation
E01=n, E13=n, E23=-n, E02=-n, with the other fields zero. Both existing
formation instruments are retained. No energy filter, reservoir, or new
framework axiom is introduced.

## 1. Exact rotor magnetic contribution

In the compensated rotor cube, h=KD+delta H4 and H4=-Z*Z/2. Here
Z=Pi2 T Pi1 T P, using the actual unsigned outward paths twice (the two
minus hopping signs multiply to plus). Translation of every field by the
fixed divergence-free face circulation is a unitary U_n. It commutes with
all rotor hops, their reverses, Z, H4, and each B_j. Consequently all pure
H4 moments in this family are independent of n. D does not share this
translation symmetry.

For clarity, Omega_n is **not** an H4 eigenvector. The checked first-sector
identity H4=-84 I-2 sum_faces(W_p+W_p*) gives

    <H4>_before=-84,       Var(H4)_before=48.             (1)

For the resolved mark (01,+ at0), put v_n=B_(01,+) Omega_n. The original
two actual outputs have coefficients one, so ||v_n||^2=2. Direct application
of Z and its adjoint at n=0 gives the finite certificate

    ||Z Omega_0||^2=168,  ||Z v_0||^2=80,
    <v_0,H4 v_0>=-40,    ||H4 v_0||^2=1584.             (2)

An explicit complete image certificate lists all 47 nonzero physical
charge/field words of H4 v_0. Its coefficient histogram is

| coefficient | -20 | -12 | -8 | -6 | -4 | -2 |
|---|---:|---:|---:|---:|---:|---:|
| number of words | 2 | 1 | 4 | 4 | 8 | 28 |

Both words in v_0 itself have coefficient -20. Squaring these coefficients
and summing gives 1584. This is exhaustive finite path enumeration, not a
fit in n or spin. It is reproduced by `full_rotor_energy_control.py`, which
applies physical outward paths twice and physical reverse paths twice.
Gauss is checked on every generated transition. The certificate and the
translation identity extend (2) to every integer n.

Since H4 v_n has coefficient -20 at each of the two words in v_n, the
symmetrized covariance of H4 with any diagonal observable on those words
vanishes in the normalized v_n. In particular, the original exact D values
0 and 2n^2 give

    <h>_before = 4K n^2-84delta,
    <h>_after  = K n^2-20delta,
    Var(h)_after = K^2 n^4+392delta^2,
    <h>_after-<h>_before = -3K n^2+64delta.              (3)

These are pre-event and conditional post-event system moments. The input's
Hamiltonian variance is 48delta^2. Thus (3) is not the distribution of a
two-projective-measurement heat protocol, which would change this input.
Adding mu N shifts the mean difference by 2mu and leaves the conditional
variance unchanged.

## 2. Full initial energy derivative, with the loss term

On the initial all-A-plus rotor sector, Gamma=sum_j B_j*B_j=48 I, for
either specified instrument. For a basis input this also follows directly:
each marked two-hop output reverses uniquely to the initial state under
the same B_j*, and there are 48 signed legal paths. The exact control
checks the full vector identity Gamma Omega_n=48 Omega_n.

For the 24 resolved marks, the exact Z norms divide into twelve values 80
and twelve values 56. Which value occurs depends on the created charge at
the A endpoint. Thus

    sum_j ||Z B_j Omega_n||^2=1632,
    sum_j <B_j Omega_n,H4 B_j Omega_n>=-816.             (4)

The two resolved orientations of one coherent edge mark have orthogonal
Z images. For the orientation that creates a negative record at B, that
negative record cannot move during the outward Z paths. In the other
orientation the negative record begins at A and can only remain there or
move to a *different, vacant* B site; the first birth B is already occupied
by a plus. Their resulting negative-record locations cannot coincide.
Hence grouping orientations leaves both (4) and the all-mark D sum
unchanged. The exact control checks all twelve Z inner products as zero.
This statement does not identify the two instruments' selected states or
their later histories.

The Lindblad generator form on this finite-support input therefore gives

    d<h>/dt at t=0
       = kappa[-816-48(-84)]delta -96kappa K n^2
       = 3216kappa delta-96kappa K n^2.                 (5)

The Hamiltonian contribution to its own energy is zero. The loss term in
(5) uses the full Gamma eigenidentity, not an assumption that Omega_n is
an energy eigenvector. Equations (1)-(5) are exact for every integer n.
Finite-support vectors belong to the required multiplication domains and
all finite-path images are still finite support; differentiation here is
a form calculation on these inputs, not an all-trace-class assertion.

## 3. Exact finite-spin first-output identities

Now keep the *effective finite-spin target*, C=S(S+1), integer S>=1, and
0<=n<=S. A physical link shift E->E+k has squared amplitude
1-E(E+k)/C, vanishing at its forbidden boundary. For the same selected
resolved mark set a=1-n(n+1)/C. Its old destinations 2 and 4 have squared
path amplitudes a^2 and a respectively. Their D values remain exactly
0 and 2n^2. Therefore, when n<S,

    ||B_(01,+,S) Omega_n||^2 = a(1+a),
    <D>_after = 2n^2/(1+a),
    Var(D)_after = 4n^4 a/(1+a)^2.                     (6)

At n=S the chosen mark has zero intensity; a conditional output is then
undefined. The original rotor formula must not be assigned to this edge
case. The exact spin comparison tests both boundaries and zero field.

There is also an exact all-mark expression. With u=n^2/C, let R_S be the
sum of squared first-output norms and P_S the sum of their D expectations
before normalization. Direct symbolic summation of all 48 signed paths
gives, for both instruments,

    R_S = 48-32u+8u^2,
    P_S = 96n^2-(32n^4+16n^2)/C,
    P_S-4n^2 R_S
        = -32n^2(3-3u+u^2)-16n^2/C.                  (7)

These formulas also hold for -S<=n<=S. They are rational identities, not
large-S fits. For the rate, if a_-=1-(n^2-n)/C and a_+=1-(n^2+n)/C, the
zero-, one-, and two-high-link path contributions are respectively
24, 8(a_-+a_+), and 2(a_-+a_+)^2. For the D sum, each saved path has its
explicit polynomial D value and product of the two spin weights. Expanding
those 48 terms yields the displayed P_S, including its -16n^2/C term.
`symbolic_spin_energy_balance.py` saves every term and the factored sums.
A separate author comparison against the earlier independently written
physical-path implementation checks 55 (S,n) cases through S=128, both
instruments, and the actual boundary exclusions. That reuse is a cross-check;
it is not represented as a new independent review.

## 4. Moving-input limit and its precise scope

Let n=floor(xS), fixed 0<x<1, and S tend to infinity. Then a and 1-u tend
to a_infinity=1-x^2>0. The selected event keeps a positive limiting
intensity kappa a_infinity(1+a_infinity), while

    Var(D)_after/n^4 -> 4a_infinity/(1+a_infinity)^2,
    R_S -> 24+16a_infinity+8a_infinity^2,
    (P_S-4n^2R_S)/n^2 -> -32(1+a_infinity+a_infinity^2). (8)

The finite-spin cube fourth coefficient is not simply the rotor H4. Since
the original gated compensation vanishes on W=1 and C0=M+D/C, its exact
canonical coefficient is

    H4_S^C = -{M_S,D}/(2C)-Z_S*Z_S/2.                  (9)

The normalized hopping operators, M_S and Z_S are uniformly bounded on a
fixed graph. Each active E(E+k)/C lies in [0,1] in the physical spin box,
so D/C is uniformly bounded too. Thus ||H4_S^C|| has a bound independent
of S and n. With h_S=KD+delta H4_S^C, (6) consequently implies

    Var(h_S)_after = K^2 Var(D)_after+O(n^2+1),
    d<h_S>/dt at0 = kappa K(P_S-4n^2R_S)+O(kappa delta), (10)

where the constants depend on the fixed cube and fixed couplings, not S.
For the drift, the dissipator applied to the bounded fourth coefficient
is bounded by its norm and the finite sum of bounded jump norms. No
finite-spin Gamma eigenidentity is needed for its electric term because
D Omega_n=4n^2 Omega_n.

This is a moving-input theorem about an explicitly supplied effective
finite-spin target. These inputs escape any fixed compact flux set and do
not converge in rotor trace norm. The earlier statewise rotor limit alone
does not prove (8); the exact finite-spin identities do. The uniform
microscopic density approximation is also not a uniform approximation of
the unbounded physical microscopic energy or its moments. Those moments,
an energy-conserving source, sustained heating, physical selection of the
compensation, and an empirical identification remain separate obligations.

The new calculations sharpen the model's system-energy account while
keeping its premise and limit order explicit. They do not rule out finite
preparation, changed Hamiltonians, driven sources, or suitable environments.
