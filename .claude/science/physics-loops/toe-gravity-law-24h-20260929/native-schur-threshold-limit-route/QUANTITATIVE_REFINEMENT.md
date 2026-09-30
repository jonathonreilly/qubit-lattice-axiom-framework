# A controlled logarithmic rate for the fixed two-pair limit

This is an author refinement of the qualitative proof in REPORT.md, not a
new independent check. It uses the minimizer existence, uniform Sobolev
bounds and actual physical row geometry proved there. No new numerical
calculation or external dilute-gas theorem is used. All parameters R>=14,
mu,tau>0 are fixed; L is odd and sufficiently large.

There is a finite constant C=C(R,mu,tau) such that

 ||V S_(2,L)-T0|| <=C (log L)^(-2/3).                    (Q1)

For the actual lowest fifteen N4 eigenvalues the same rate holds after
multiplication by V. Moreover the raw constrained Schur minimizer psi_L[A]
and the infinite minimizing threshold profile psi_infty[A] obey

 sup_(diam(S)<=L^(1/4)) |psi_L[A](S)-psi_infty[A](S)|
                  <=C||A|| (log L)^(-1/3),              (Q2)

where finite shapes are identified with their unique large odd-torus images.
No full ell2 convergence, positive-energy scattering limit, growing-n
uniformity or physical cell-boundary replacement is asserted.

## 1. Uniform bounds available from the qualitative proof

All the estimates used there are uniform for ||A||<=1. The raw finite
minimizer energy satisfies E_L<=C||A||^2. Its graph-residual ordered field
F_L has common pin zero and

 ||F_L-mean F_L||_6<=C||A||,
 ||mean F_L-U A U^T||<=C||A|| V^(-1/2),
 ||Q_nm psi_L||_2<=C||A||.

For the second bound, the high component is controlled by the actual S
mean form at order V^-1/2, and the soft component by the fixed finite guard
and exact frame constraint at order V^-1. Thus, because V^(1/6)V^(-1/2)
is bounded and tends to zero,

 ||F_L-U A U^T||_6<=C||A||.                             (Q3)

The limiting minimizing profile from the qualitative proof has the same
bounds: in its separated-pair exterior u_infty=F_infty-U A U^T is ell6 with
norm at most C||A||, its nonmatching part is ell2 with norm at most C||A||,
and its actual energy is <A,T0 A><=C||A||^2. These constants are uniform in
the internal tensor A; no choice of a numerical threshold eigenvector is made.

## 2. A cutoff on actual configurations, with controlled row commutators

Set r_-=L^(1/4), r_+=L^(1/2), and J=log(r_+/r_-)=(log L)/4. Integer rounding
changes only fixed constants. Choose the real cutoff

 eta_L(s)=1                         for s<=r_-,
 eta_L(s)=1-log(s/r_-)/J             for r_-<s<r_+,
 eta_L(s)=0                         for s>=r_+.

In infinite configuration space let s(S) be the Chebyshev diameter of the
four occupied sites. On the torus minimize that diameter over lifts. For
diameters below L/3 the lift is unique modulo a common translation: in each
coordinate the missing circle arc exceeds twice the occupied arc. Every
configuration in the cutoff support therefore has a unique infinite image
for large L, as do all configurations in a neighboring Hamiltonian row.

Two inputs of one positive S or W row share the same two-site output, and
their removed graph pairs lie in a common bounded neighborhood. Their
diameters differ by a fixed constant independent of L. The same bound holds
for the minimized torus diameter, by moving each changed site to its nearby
lift. Consequently the cutoff difference across a row is bounded by

 C/[J max(r_-,s)]                                     (Q4)

in its transition region, and by C/(J r_-) globally.

Far from the fixed collision core, each positive row belongs wholly to the
separated matching exterior or wholly to Q_nm. To see this, fix its residual
two-site output. If that output is a graph edge and the created local pair
is far away, every input in the row consists of those two disconnected
graph edges. If the residual is not a graph edge and the created pair is
far away, every input is nonmatching. Any exception places all four sites
in a fixed bounded collision neighborhood, where eta_L=1 for large L.
This argument applies to individual positive rows, not only to a cancellation
in their summed Hamiltonian.

In the matching exterior, the diameter differs from the relative bond-anchor
radius by at most a fixed constant. The number of relative positions in an
integer shell of radius s is O(s^2). For all the finitely many channel and
row types, (Q4) therefore gives

 sum_(exterior row incidences) |delta eta_L|^3
       <=C J^(-3) sum_(s between r_- and r_+) s^(-1)
       <=C J^(-2).                                     (Q5)

The finite-range actual S/W rows have bounded width and bounded coefficient
incidence. Holder with exponents3/2 and3, or directly Cauchy within a row,
therefore bounds the commutator energy on an exterior correction u by

 E_comm,ext <=C ||u||_6^2
                    [sum|delta eta_L|^3]^(2/3)
             <=C||u||_6^2 J^(-4/3).                    (Q6)

There is no commutativity or scalar-polarization assumption on the internal
matrices. The physical exterior isometry and its fixed sqrt2 factors merely
change the fixed constant in this norm estimate.

For the nonmatching component q, use its ell2 bound and the supremum in(Q4):

 E_comm,Q <=C ||q||_2^2/(J^2 r_-^2).                    (Q7)

The coefficient-incidence constant is uniform: a four-site occupation has
only finitely many removable graph edges and local rows. More explicitly,
the sum of squared coefficients at an input is the diagonal of the positive
S+W form, bounded by ||H4||; the maximum row width is finite (at most eight).
Cauchy within a row then proves(Q7). The positive diagonal D term has no
commutator. It vanishes in the separated exterior, and in Q it is simply
multiplied by eta_L^2<=1. Inside the collision core the cutoff is one.

For a finite-energy physical profile psi with incoming Phi_A, form

                   Y=Phi_A+eta_L(psi-Phi_A).             (Q8)

All positive rows of Phi_A vanish outside a fixed collision region. In the
transition region a row of Y is eta at a reference input times that row of
psi, plus the just-bounded commutator. In the inner region it is exactly the
row of psi, and outside the cutoff it is zero. Minkowski in the complete
positive-row norm, including the diagonal D factors, yields

 sqrt(E(Y))<=sqrt(E(psi))+sqrt(E_comm,ext+E_comm,Q).

With the uniform bounds(Q3), their infinite counterparts, and E(psi)<=C||A||^2,
we obtain

              E(Y)<=E(psi)+C||A||^2 J^(-2/3).           (Q9)

For a finite-torus profile, use its unique infinite lifts only inside the
cutoff and put the infinite incoming profile outside. Every retained or
transition row has diameter below r_++O(1)<L/3, so its embedding is injective
and its coefficient is exactly the actual infinite-lattice coefficient.
The retained squared row norms are a subset of the finite-torus ones.
Thus(Q9) holds in this finite-to-infinite direction as well. It is a cutoff
in fixed four-particle relative configuration space, not a lower decomposition
of a many-particle spatial system into independent boxes.

## 3. Quantitative lower comparison

Apply(Q8) to the raw finite constrained minimizer psi_L[A]. Its correction
is compact in the infinite orbit space: every retained four-site shape has
diameter at most r_+. It therefore is an admissible competitor in the actual
T0 variational definition. Equations(Q3),(Q9) give, uniformly for all A,

 <A,T0 A> <= V<A,S_(2,L)A>+C||A||^2(log L)^(-2/3).       (Q10)

No finite-torus zero-energy inverse has been replaced by an infinite one.

## 4. Quantitative upper comparison and exact frame correction

Apply(Q8) instead to the infinite minimizing profile psi_infty[A] from the
qualitative proof. Its compact correction has support of diameter at most
r_+, so it embeds on the odd torus without row aliasing. Its raw energy is
at most <A,T0 A>+C||A||^2(log L)^(-2/3).

It remains to impose the EXACT polar-frame constraint. If ell_L(Y) denotes
G_L^(-1/2)chi_R,L^dagger Y/V, then

 ||ell_L(Y)-A|| <=C||A||[V^-1+r_+^(5/2)/V]
                <=C||A|| L^(-7/4).                    (Q11)

Indeed the guarded incoming contribution differs from A by O(V^-1).
The nonmatching correction has zero overlap with the guarded frame. In the
exterior, Holder bounds the sum of a compact ell6 field by the five-sixths
power of its O(r_+^3) support, namely C r_+^(5/2)||u||_6. The finite matching
core contributes only O(V^-1). The inverse square root of G_L is uniformly
bounded for large L.

For beta_L=ell_L(Y)-A subtract the raw physical polar-frame vector

                   Z_L beta_L=chi_R,L G_L^(-1/2)beta_L.

Its polar coordinate is exactly beta_L, so Y-Z_L beta_L is an admissible
finite Schur trial. The checked trial bound gives

 E(Z_L beta_L)<=V theta_L ||beta_L||^2<=C||beta_L||^2.

Cauchy in the physical energy form prices its cross term by C||A||||beta_L||.
Using(Q11) therefore changes the trial energy by only O(||A||^2 L^(-7/4)).
The finite constrained minimum yields

 V<A,S_(2,L)A> <=<A,T0 A>
               +C||A||^2[(log L)^(-2/3)+L^(-7/4)].     (Q12)

Together(Q10),(Q12) prove(Q1), after increasing the constant. This is a
quadratic-form bound for every complex symmetric A, hence an operator-norm
bound on the complete fifteen-dimensional space. A coherent tensor alone
would not have sufficed.

## 5. Actual spectra and quantitative local response

The earlier Schur-to-spectrum error is O(L^-1) after multiplication by V.
It is absorbed by the bound in(Q1), giving the same logarithmic rate for
all fifteen rescaled physical eigenvalues. Higher levels still obey
V lambda_16>=V Delta_L, of order L.

For the response estimate, let Y_L be the infinite compact trial obtained
by cutting the finite minimizer in Section3. Its energy is at most
<A,T0 A>+C||A||^2(log L)^(-2/3), by(Q1),(Q9). Since psi_infty[A] is the
minimizer in the affine energy completion, stationarity against that
completion gives

 E(Y_L-psi_infty[A])=E(Y_L)-<A,T0 A>
                   <=C||A||^2(log L)^(-2/3).             (Q13)

For a compact zero-incoming physical variation w, the infinite discrete
Sobolev inequality and the actual removal-gradient bound give

 ||F_w||_6<=C sqrt(E(w)/a),
 ||Q_nm w||_2<=sqrt(E(w)/mu).

These bounds extend to the energy completion by compact approximation.
Every matching occupation amplitude is sqrt2 times an entry of F_w; every
nonmatching amplitude is bounded by its ell2 norm. Thus every physical
coefficient of w is at most C sqrt(E(w)). Applying this to(Q13), and noting
that Y_L equals psi_L on diameters at most r_-, proves(Q2).

The estimate controls only this fixed N4 threshold response, in raw orbit
normalization and with the incoming tensor held fixed. Neither its constants
nor its geometry have been proved uniform as the number of pairs grows.
