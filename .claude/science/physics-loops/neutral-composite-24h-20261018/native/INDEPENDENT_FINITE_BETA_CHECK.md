# Finite-beta broad energy features and composite overlap

## Checked external input

I read Theorem2, equations9–11, and Corollary2 of [Kliesch et al., *Locality of temperature*, arXiv:1309.0816v4](https://arxiv.org/html/1309.0816). They give finite-volume, size-independent generalized-covariance clustering for every tau in[0,1], subject to the stated minimum-distance threshold, and finite-buffer local-state approximation. Thus ordinary covariance at tau endpoints is covered. The temperature condition is

    |beta|<log[(1+sqrt(1+4/alpha))/2]/(2J).

Below, short distances are bounded separately; the theorem is not used outside its distance condition. These are high-temperature equilibrium inputs, not diffusion or equilibration-time theorems.

## Exact weighted-energy current

For E_f=sum_x f_x e_x, first combine the two local assignments to each nearest bond:

    E_f=(K/2)sum_<xy> (f_x+f_y) sigma_x^a sigma_y^a.

Pair two different-axis bonds meeting at p, with endpoints p+s e_a and p+t e_b, a<b and s,t=±1. Their combined commutator coefficient is their weight difference. Since i[sigma_p^a,sigma_p^b]=−2 epsilon_abc sigma_p^c,

    D E_f = −K² sum_(p,a<b,s,t) epsilon_abc
       [f_(p+t e_b)−f_(p+s e_a)]
       sigma_(p+s e_a)^a sigma_p^c sigma_(p+t e_b)^b.

The proposed sign and normalization are correct. K=0 is excluded from the subsequent positive-energy-variance claim. No new Hamiltonian term is introduced.

## Clustering and the Schur bound

Index the unit-norm three-spin words by j=(p,a,b,s,t), and call their coefficients g_j, including the Levi-Civita sign but excluding K². In a stationary Gibbs state <D E_f>=0. One can therefore use their centered covariance matrix even without separately assuming every current mean is zero. For the usual time-reversal-invariant Gibbs preparation the individual three-spin means also vanish.

Each current has uniformly bounded finite support. Exponential clustering plus a separate bounded short-distance contribution gives

    M_beta = sup_i sum_j |Cov_beta(J_i,J_j)| < infinity.

There are only finitely many current types per site, and lattice shells grow polynomially. The covariance matrix is a positive Hermitian Gram matrix in the ordinary thermal operator inner product. The Schur bound yields

    ||D E_f||_beta² <= K^4 M_beta sum_j |g_j|².

For a Gaussian f_x=exp(−|x|²/(2R²)), the discrete difference sum is O(R) in three dimensions. In fact its leading unweighted asymptotic is12 pi^(3/2) R: summing the twelve corner types gives8 integral|grad f|², and integral|grad f|²=(3/2)pi^(3/2)R. Only the O(R) bound is needed here. A mean-value estimate gives a direct bound uniform over the finite shifts, without pretending the lattice sum is exactly the continuum integral.

## Graph constant and temperature window

The infinite simple cubic bond graph has six bonds at each site. A given bond shares an endpoint with ten other bonds, so its line graph has maximum degree10. A connected m-vertex set of this line graph containing a fixed root has a deterministic spanning-tree depth-first walk of length2(m−1) visiting exactly that set. Distinct sets give distinct visited sets/walks. There are at most10^[2(m−1)] such walks, hence the rooted-animal count is bounded by100^m. Alpha=100 is a valid conservative upper bound. Each unique compass bond has operator norm J=|K|.

This supplies the proposed sufficient clustering window. It is not an estimate of the actual critical temperature. Short periodic multiedge systems need their actual interaction grouping/norms; the argument concerns the ordinary infinite lattice or suitable nonaliasing finite volumes.

## Energy susceptibility and denominator

Center the packet: delta E_f=E_f−<E_f>. Using the raw, uncentered norm would include a large identity expectation and would not be the claimed fluctuation result.

Let S_e(q,beta) be the Fourier transform of the translation-invariant ordinary connected energy covariance. Absolute summability makes it continuous in q; positive definiteness makes it nonnegative. At beta=0,

    S_e(0,0)=3K²>0.

A legitimate route to continuity in beta is:
1. On a compact smaller high-temperature interval, use uniform finite-buffer locality to obtain a uniform local thermodynamic limit. Finite-buffer Gibbs expectations are continuous in beta, so the limiting fixed-support covariances are continuous.
2. The clustering envelope can be chosen summable uniformly on that smaller interval; handle the bounded short-distance region separately.
3. Dominated convergence then gives continuity of the summed energy covariance S_e(0,beta), and joint continuity near q=0.

Therefore an unspecified smaller neighborhood |beta|<delta exists with S_e(q,beta)>=kappa>0 on a fixed small q ball. This argument does not provide a numerical delta, and does not establish positivity throughout the entire clustering window without further estimates.

For broad Gaussian packets, their Fourier mass concentrates inside that ball. Consequently for sufficiently large R,

    Var_beta(E_f)>=c kappa sum_x f_x² = Omega(R³).

**This is a low-q packet bound, not a lower bound for every f.** The checkerboard combination e_Q is identically zero, so a global all-q coercive lower bound is impossible. Together with the current estimate it gives

    ||D E_f||_beta / sqrt[Var_beta(E_f)] = O(1/R)

at each fixed beta in the smaller neighborhood. Constants may depend on beta and K. Stationary Gibbs dynamics is unitary in this thermal norm, giving the exact centered-packet estimate

    ||delta E_f(t)−delta E_f||_beta / ||delta E_f||_beta
       <= |t| ||D E_f||_beta / ||delta E_f||_beta.

No diffusion, sound velocity or particle pole is inferred.

## Making the composite overlap thermodynamically uniform

Continuity alone does **not** justify differentiating a covariance sum or inheriting the coefficient −2beta from finite boxes. One may use a separately justified convergent high-temperature linked-cluster expansion. Alternatively, the explicit small-beta behavior of the cited clustering/locality bounds permits a finite-order argument without asserting full pressure analyticity:

Define

    b(beta)=alpha exp(2|beta|J)[exp(2|beta|J)−1]=O(|beta|).

The spatial exponential is b(beta)^distance. For fixed-support observables the minimum-distance threshold tends to zero as beta->0, and prefactors stay bounded on a sufficiently small interval. Truncating a covariance sum outside a **fixed sufficiently large distance m** then gives an O(|beta|^m) tail, uniformly in volume; polynomial shell counts do not change that order. For the remaining finite list of local covariance terms, approximate the state by a fixed buffer whose boundary is at distance at least m from their union. The local-state error has an additional |beta| factor and is O(|beta|^(m+1)), with fixed buffer prefactors.

The resulting finite-buffer expression has an ordinary finite-dimensional Taylor expansion. Taking m large enough transfers its coefficients and a finite-order remainder to the infinite-volume covariance sum. The coefficients already counted locally are thus legitimate thermodynamic coefficients after writing out this truncation argument. Spectral-reflection symmetry in the infinite lattice/even-volume limit removes the inappropriate parity orders.

In particular,

    S_Ce(0,beta)=sum_r Cov_beta(C0,e_r)
                =−6 beta K²+O(beta³),
    S_e(0,beta)=3K²+O(beta²),
    S_Ce(0,beta)/S_e(0,beta)=−2beta+O(beta³).

For all sufficiently small nonzero beta this overlap is nonzero. The allowed subinterval is existential until a remainder constant is actually bounded. This is more than formal finite-volume expansion, but the truncation/locality step is essential and should appear in the proof rather than be silently inferred from the word 'clustering'.

For Gaussian packets, summability gives the corresponding covariance-density limits as R->infinity. The limiting projection coefficient onto their energy component is the displayed ratio; its norm fraction has leading4beta²K² when the C covariance density tends to3 at beta0. Finite-q propagation or hydrodynamics does not follow from a static projection. State selection and matching to physical observations remain outside this result.
