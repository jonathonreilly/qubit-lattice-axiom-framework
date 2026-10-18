# Independent parity-projection check

Reviewed the formula and `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/parity_control.py`. The even-parity expression and stated uniform algebraic bound are correct for **distinct one-particle modes a != b** in a globally parity-projected free grand-canonical ensemble. This does not assume the projected state is Gaussian.

## Direct derivation and odd extension

Let independent unprojected mode occupations have probabilities f_i, define R_i=1−2f_i, r=prod_i R_i and r_rest=prod_(i != a,b) R_i. Total fermion parity is Pi=prod_i(1−2n_i). For desired parity sigma=+1 (even) or −1 (odd),

    P_sigma=(1+sigma Pi)/2,
    Pr(sigma)=(1+sigma r)/2.

For a!=b, (c_b^dagger c_a)^dagger(c_b^dagger c_a)=n_a(1−n_b). On its nonzero support, n_a=1,n_b=0, so the parity of these two modes is −1. Independence of the **unprojected** occupations therefore gives

    <n_a(1−n_b)>=f_a(1−f_b),
    <Pi n_a(1−n_b)>=−f_a(1−f_b)r_rest.

Conditioning yields exactly

    W_ab^(sigma)=f_a(1−f_b)(1−sigma r_rest)/(1+sigma r).

Thus even weight is the root's expression and odd weight is

    W_ab^(odd)=f_a(1−f_b)(1+r_rest)/(1−r).

Projection is used explicitly; unrestricted Wick factorization is not invoked after projection. The formula remains valid at coincident energies provided modes are distinct. Transitions at zero energy then contribute elastic structure-factor weight, not positive-frequency dynamical weight.

## Relative correction and uniform bound

For a positive unprojected pair weight,

    W_ab^(sigma)/[f_a(1−f_b)]−1
        =−sigma(r_rest+r)/(1+sigma r).

Consequently, if |r|<1,

    |relative correction|
        <= (|r_rest|+|r|)/(1−|r|).

Taking max over pairs gives the stated bound, valid for both parities. Since r=R_a R_b r_rest, one can also retain the exact numerator r_rest(1+R_a R_b) when useful. An unprojected zero pair weight remains zero under a defined conditioning; its relative error is undefined, but the absolute equality remains valid.

For a finite set of at least two modes with x_i=|R_i| in [0,1], max over all distinct pairs of prod_(i != a,b)x_i is obtained by removing the two smallest x_i. This is an upper bound if the physical probe permits only a subset of all pairs. It must not be described as the exact maximum over that subset unless the minimizing pair is allowed.

## Zero and nearly saturated cases

- With at least three exact R_i=0, every r_rest and r vanish, so all distinct-mode pair weights are unchanged by either parity projection.
- With two zeros, removing exactly those two can leave nonzero r_rest. With one zero, removing it and the next-smallest magnitude maximizes the remainder. Therefore calculating r_rest by division r/(R_a R_b) is unsafe; sorting and directly multiplying the remaining magnitudes handles zeros.
- Finite T and finite one-particle energies give |R_i|<1 and both parity sectors nonzero probability. At zero T, r can equal +1 or −1. Conditioning onto the unsupported opposite parity then has a zero denominator and is not defined by this state. A finite-T limiting conditional ensemble may exist but requires a separate limiting calculation.
- When |r| is near one, the bound can be large and numerically ill-conditioned; this is not evidence that it is safe to ignore parity. Log-domain sector probabilities or higher precision may be needed.

## Retarded weights and moments

For the reverse ordered pair the same r_rest and correction factor apply. Hence

    W_ab^(sigma)−W_ba^(sigma)
        =(f_a−f_b)(1−sigma r_rest)/(1+sigma r).

The parity-conditioned finite-T detailed-balance ratio is unchanged for these number-conserving transitions because they preserve parity. Thus the same multiplicative factor corrects the positive-frequency commutator weights. If a uniform epsilon bounds the relative correction, it also bounds relative changes of nonnegative unnormalized moments of that positive-frequency measure (when those moments are nonzero). Normalized moments, variance and ratios require propagating numerator and denominator errors; they do not inherit epsilon unchanged. Diagonal probes and their cross-covariances need separate formulas.

## Encoded-sector scope

To apply this to the BKSF physical sector, verify which total fermion parity that representation actually selects, then calculate f_i from the Hamiltonian in the chosen gauge/holonomy sector. A fixed gauge sector can change the allowed single-particle spectrum and boundary conditions. This calculation conditions only total parity, not fixed particle number, local occupancy constraints, or a mixture of flux sectors.

The product is over **all actual one-particle modes of the finite physical system**, including the genuine degeneracies. A quadrature grid used only to approximate an infinite-volume integral is not automatically a physical finite box whose mode count can be inserted into this product. The current script's declared N^3 discrete momentum lattice can be interpreted as such a finite-box development control if that convention is explicitly retained. Nonzero q should be checked modulo reciprocal vectors/supercell folding: the operative condition is a!=b, not merely a nonzero printed q.

## Code observations

The current code correctly removes the two smallest log magnitudes, computes the algebraic bound in log form, preserves a log-bound when the exponential underflows, and brute-forces 12 distinct ordered pairs in the even four-mode example. The formula above independently extends that check to odd parity without modifying root files.

Clamping an exact zero |tanh| upward to the smallest positive float makes its magnitude product an upper estimate in exact arithmetic; this is conservative rather than an exact log expectation. Labels should distinguish a clipped log bound from the exact log expectation if an exact zero occurs. Floating-point eigenvalues, tanh, summation and exponentiation are not interval-enclosed, so the returned number is a numerical evaluation of a rigorous algebraic bound, not a machine-certified upper enclosure. Saturated tanh values can also round to one; rbound=1 makes the displayed denominator singular. These do not invalidate the algebra, but should be reported honestly if encountered.
