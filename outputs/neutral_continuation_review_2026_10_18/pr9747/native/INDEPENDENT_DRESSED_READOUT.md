# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused exactly dressed readout and correlator bound

Disposition: PASS conditional on the stated volume-uniform dressed-source decomposition and the previously checked dressed-H hypotheses. This closes the local-source truncation issue for the dynamical estimate without discarding an O(lambda) dressing term. It does not identify the retained effective dynamics with a scalar model.

Let C_w=sum_j w_j c_j, with ||c_j||=1 and two-site support. Assume the exact finite-product dressing yields

    U_m c_j U_m† = sum_Y c_(j,Y),
    sup_j sum_Y |Y| ||c_(j,Y)|| <= C_m,

uniformly in volume and smalllambda. This is a cardinality-weighted absolute norm bound, not merely a formal power series or a bound on a truncated dressed operator. It is sufficient for the argument below. For an infinite lattice, the exact dressing is interpreted as a quasi-local automorphism and the transformed state by composition; no infinite global unitary need be postulated.

## Exactly dressed single-observable estimate

Apply the earlier dynamics estimate separately to each c_(j,Y), which is supported on Y. Its bound depends linearly on |Y| and is independent of the diameter or shape of Y. Summing absolutely gives

    ||tau_H'(t) Ctilde_w - tau_(2N+D_m)(t) Ctilde_w||
      <= C_m ||w||_1 lambda^(m+1)
         |t| (1+lambda|t|)^3,

where Ctilde_w=U_m C_w U_m† is retained exactly. The cardinality-weighted decomposition permits the sums, thermodynamic limit, and norm estimate to be interchanged. No additional approximation of Ctilde_w by C_w, or by a finite-order source polynomial, has been used.

The assumed moment bound is the precise dressing input. If its independent derivation uses a mixed-word expansion, it must establish convergence after the extra |Y| factor, uniformly in j and volume. A fixed finite sequence of finite-range quasi-local evolutions can also establish such a bound by summable shell decompositions. This review verifies the consequence of that input; it does not independently reproduce the separate mixed-word majorant.

## Correlators and retarded response

Exact conjugation preserves operator norm, so

    ||Ctilde_w||=||C_w|| <= ||w||_1.

For the SAME initial state rho'=U_m rho U_m† in both evolutions, positivity and normalization of the state give

    |rho'[(tau_H' Ctilde_w-tau_B Ctilde_w) Ctilde_w]|
      <= ||delta Ctilde_w(t)|| ||w||_1.

Thus the two-point correlator error is bounded by

    C_m ||w||_1² lambda^(m+1)
        |t| (1+lambda|t|)^3.

The retarded commutator costs at most a factor2, absorbed into C_m. A connected correlator adds at most another fixed factor from its expectation-product subtraction. No stationarity, equilibrium, or eigenstate hypothesis is needed for this same-state finite-time norm estimate. For non-Hermitian weights use the appropriate adjoint in an autocorrelator; the same norm bound holds. A physical Hermitian readout uses real weights.

It is essential to keep the SAME transformed initial state. This does not bound differences between separately equilibrated Gibbs states, separately selected eigenstates, or different preparations of the two Hamiltonians.

## Scaling at the proposed observation time

For m=20 and |t|=O(lambda^-4), the common time/remainder factor is O(lambda^8). If the packet contains L=O(lambda^-2/3) terms with equal weights1/sqrt(L), then ||w||_1²=L and

    correlator/response error = O(lambda^(22/3)) = o(lambda^6).

For unweighted unit coefficients, ||w||_1²=L², so

    correlator/response error = O(lambda^(20/3)) = o(lambda^6).

Both exponents are correct. This calculation uses the actual l1 weight bound and does not mistake variance normalization for bounded operator norm. Fixed multiplicities of local terms per packet site are absorbed into constants; a different number of terms or weight profile must use its actual ||w||_1.

## Remaining scope

The comparison retains the full D20 and the exact dressed readout. Unknown D5 through D20 are not removed or shown dynamically irrelevant by this estimate. It establishes an absolute finite-time error, not spectral pole existence, an infinite-time transform bound, or agreement with a chosen lower-order scalar block. It also does not derive the state, select an observed source, or provide an empirical detector interaction. No repository edits or formal audit were performed.

## Explicit verification of dressed-source summability

Reviewed `/private/tmp/neutral_dressed_source_root.md`. The polynomial-support argument is valid, and its needed majorant can be written explicitly; the source moment bound is therefore derived from the finite-product generator hypotheses rather than an additional independent assumption.

Write the fixed finite product as U_m=product_(r=1)^m exp(G_r), where each G_r is an anti-Hermitian finite-range interaction, with maximal term cardinality s, maximal diameter b, and local norm

    g_r=sup_x sum_(Z containing x)||(G_r)_Z||.

For the finite-order construction, g=sum_r g_r=O_m(|lambda|) on a sufficiently small disk, while s,b depend only on fixed m. These are the generator-locality hypotheses already needed for the normal-form mixed-word bound; an extensive total operator norm is not substituted for g_r.

In an n-fold nested commutator acting on a two-site observable c, every surviving next interaction term intersects the current support. If that support has size k, the sum of its possible term norms is at most k*g_r, and each commutator costs a factor2. The resulting support size is at most2+n*s. Thus a word of specified generator types has total termwise norm bounded by

    ||c|| 2^n product_(j=0)^(n-1)(2+j*s)
         product_(r=1)^m g_r^(n_r).

The exponential expansion contributes1/product_r(n_r!). Summing all multiindices with total n uses the multinomial identity and yields the uniform majorant

    ||c|| [(2s*g)^n/n!] (2/s)_n,

where (a)_n is the rising factorial. This is the coefficient series of (1-2s*g)^(-2/s), and it converges when2s*g<1. Product ordering imposes no additional factorial: the commutator norm bound is insensitive to the allowed order, and the multiindex sum already bounds the actual ordered product expansion.

Multiplying by2+n*s is controlled by the derivative of that convergent power series. Each attached finite-range term also increases the diameter by at most b, so an exponential diameter weight exp(mu*diameter) is handled by replacing2s*g with2s*g*exp(mu*b), up to the fixed initial diameter factor. For any fixed finite mu one may choose lambda small enough to keep this quantity below1. The constants are uniform in the position of c and in volume.

Grouping the absolutely convergent individual interaction words according to their union support Y, and using the triangle inequality, now proves

    sup_j sum_Y |Y| exp(mu*diam(Y)) ||C_(j,Y)|| <= C_m.

In finite volume the expansion equals the exact conjugation. Absolute volume-uniform convergence then yields its quasi-local limit. No finite-support claim, formal asymptotic truncation, or discarded O(lambda) observable error is involved.

Accordingly the initial conditional summability qualification in this report is discharged PROVIDED the supplied finite-order generators satisfy the stated finite-range/local-norm bounds. The remaining conditions on the dressed-H decomposition, same-state comparison, and retention of all D20 are unchanged. The allowed small-lambda radius is an existence bound depending on m and the generator norms; this calculation does not certify a particular numerical coupling lies inside it.
