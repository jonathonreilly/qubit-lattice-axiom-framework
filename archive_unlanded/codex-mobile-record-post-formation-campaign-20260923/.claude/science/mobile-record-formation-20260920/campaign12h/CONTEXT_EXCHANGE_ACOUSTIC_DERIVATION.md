# A context-dependent immutable exchange with an isotropic acoustic current sector

Primary construction, 2026-09-21. This is a supplied stochastic generator, not
an axiom derivation. The stationary law, currents and tuned current spectrum
have a completed separate calculation made before access to this source
(`independent_context_exchange/`, sealed 03:41:53 UTC). The subsequent nonlinear
entropy identity below is a primary derivation. A new local-equilibrium proof
candidate is in `CONTEXT_EXCHANGE_EULER_DERIVATION.md`; its independent check is
in progress. No microscopic hydrodynamic theorem is yet treated as checked.

## The question and the change of hypothesis

The endpoint-only classification in `PAIR_EXCHANGE_CURRENT_CLASSIFICATION.md`
fixes product-stationary cubic currents to one scalar multiple of
`p_a (v_a-g)`. Its six-field Euler linearization has direction-dependent
couplings to the two axis-quadrupole densities. That result explicitly leaves
context-dependent rates open. We now use the two collinear sites immediately
outside an exchanged nearest-neighbor pair. Every update is still an exchange
of two complete immutable records (or a record with a vacancy).

The lattice is Z^3 or a simple cubic torus with every period at least four.
The alphabet is vacancy 0 and six occupied labels a with vectors v_a=+/-e_i.
Set n(0)=0, v_0=0 and n(a)=1 for occupied labels. For the positive-i bond
`(x,x+e_i)`, denote its four-site string by

`(l,a,b,r)=(eta_(x-e_i),eta_x,eta_(x+e_i),eta_(x+2e_i))`.

Write f_i(a)=v_a dot e_i. Define the antisymmetric rate difference

`h_i(l,a,b,r) = u [f_i(a)-f_i(b)]`

` + E { [f_i(a)-f_i(b)] [n(l)+n(r)]`

`       + [n(a)-n(b)] [f_i(l)+f_i(r)] }`,                         (1)

and the actual bond exchange rate

`c_i(l,a,b,r)=K+h_i(l,a,b,r)/2`,                                 (2)

where `K>|u|+2|E|`. Indeed `|h_i|<=2|u|+4|E|`: if both endpoints
are occupied the second bracket in (1) vanishes; if exactly one is occupied,
each external site's combined contribution has magnitude at most two. Both
vacant endpoints give zero. The stated strict inequality gives a positive
uniform rate floor and a finite ceiling. Null exchanges of identical contents
may be retained as tagged-record swaps or omitted for the content process.

A second admissible implementation is `c_i=kappa_0+max(h_i,0)` with
kappa_0>0. It has the same antisymmetric difference h_i, so all stationary
current statements below are unchanged. Its symmetric rate can be smaller
than the conservative constant K bound; its damping need not be the same.

There is one clock per undirected bond, represented in its positive direction.
The rate describes the same physical edge after reversing its orientation:
reverse the order `(l,a,b,r)`, and replace f_i by -f_i. Each term in (1)
is unchanged. Proper cubic rotations permute these rules. There is no
preferred lattice axis, external vector, record redraw, removal or creation
in this conservative generator.

## Exact product stationarity

For every homogeneous seven-category product measure, a pair exchange leaves
the weight of a configuration unchanged. Its stationarity equation therefore
reduces, at each configuration on a finite torus, to

`sum_(x,i) h_i(eta_(x-e_i),eta_x,eta_(x+e_i),eta_(x+2e_i))=0`.     (3)

The u term telescopes. For the E term write f_x=f_i(eta_x), n_x=n(eta_x)
along one periodic line. Its sum is

`sum_x (f_x-f_(x+1))(n_(x-1)+n_(x+2))`

`     +(n_x-n_(x+1))(f_(x-1)+f_(x+2))`.

The distance-one terms cancel by shifting the line sum; so do the distance-two
terms. This proves (3) for each axis separately. Infinite-lattice product
invariance follows from the bounded local graphical process and its finite
volume limit on local cylinder functions. It does not require a hydrodynamic
limit. Positive rates also allow every finite-torus adjacent transposition,
so each fixed-count content sector is irreducible; no infinite-volume
classification of all stationary measures is asserted.

## Exact currents and the susceptibility identity

Let p_a be the six occupied probabilities, rho=sum_a p_a, p_0=1-rho,
g=sum_a p_a v_a, and Q=sum_a p_a v_a tensor v_a. The current of label a
through a positive-i edge is the expectation of
`c_i(l,a_x,a_y,r) [1_(a_x=a)-1_(a_y=a)]`.
The symmetric K contribution vanishes in the product state. The external
sites are independent of the endpoints. Direct averaging gives

`J_a = p_a [F(rho) v_a + G(rho) g]`,                             (4)

`F(rho)=u+2 E rho`,

`G(rho)=-u+2 E(1-2rho)=(1-rho)F'(rho)-F(rho)`.

Consequently the number and vector-content currents are

`J_number = (1-rho) [F(rho)+rho F'(rho)] g`,                     (5)

`J_vector = F(rho) Q + G(rho) g tensor g`.                      (6)

These are exact homogeneous-product expectations. They do not replace the
current of a non-product evolving state.

At an isotropic state p_a=rho/6 with 0<rho<1, let C=diag(p)-p p^T be
the one-site covariance and A_i=partial J_i/partial p. Formula (4) gives

`A_i = F diag(f_i) + F' (p .* f_i) 1^T + G p f_i^T`.             (7)

For a!=b, `(A_i C)_(ab)=p_a p_b [(p_0 F'-F) f_i(a)+G f_i(b)]`.
Thus (4)'s identity `G=p_0 F'-F` makes A_i C symmetric. C is positive
definite in the stated interior. This checks the symmetrization condition
for the six linear currents without assuming detailed balance.

There is also a compact nonlinear proof valid at every full-support product
composition. Introduce chemical coordinates mu_a=log(p_a/p_0), so
`partial p_a/partial mu_b=C_(ab)`, and the vector flux potential

`Psi_i(mu)=F(rho(mu)) g_i(mu)`.

Its derivative is exactly
`partial Psi_i/partial mu_a=p_a[F v_(a,i)+(p_0 F'-F)g_i]=J_(a,i)`.
Thus `A_i C` is a Hessian and is symmetric throughout the interior. Equivalently,
`H A_i` is symmetric for the positive entropy Hessian
`H=C^(-1)=diag(1/p)+11^T/p_0`. The categorical entropy
`eta=sum_a p_a log p_a+p_0 log p_0` supplies the compatible entropy flux
`q_i=sum_a mu_a J_(a,i)-Psi_i`. These identities prove symmetrizability of
the proposed nonlinear conservation law. They still do not prove that law
is the microscopic hydrodynamic limit. This algebra extends to any smooth
F with G=p_0 F'-F; only the linear F above has been realized by the specific
four-site generator here.

## A tuned density with isotropic linear acoustic currents

Choose an interior density rho_* and E!=0, and set u=-2 E rho_*.
Then F(rho_*)=0, while F'=2E. Linearize the conditional Euler conservation
law `partial_t p_a + div J_a(p)=0` about the isotropic product state there.
Write delta rho, delta g, and the two independent traceless diagonal entries
of delta Q. Equations (5)-(6) become

`partial_t delta rho + 2 E rho_* (1-rho_*) div delta g = 0`,       (8)

`partial_t delta g + (2 E rho_*/3) grad delta rho = 0`,            (9)

`partial_t delta Q_traceless = 0`.                               (10)

For (10), the label-quadrupole current is obtained by weighting (4) with
`v_(a,i)^2-1/3`. At g=0 the equilibrium third moment vanishes, and its
linear derivative is proportional to F, which is zero at rho_*.
There are two acoustic current eigenvalues and four zero current eigenvalues:

`omega=+/- c_s |k|`, `c_s=2 |E| rho_* sqrt((1-rho_*)/3)`,         (11)

plus the two transverse vector and two quadrupole modes. The two propagating
eigenvalues depend only on |k|, not the lattice direction. This is an exact
algebraic statement about the stationary current Jacobian, not yet a theorem
about the microscopic dynamic structure factor. For pure density initial
data the linear PDE predicts `delta rho(k,t)=delta rho(k,0) cos(c_s|k|t)`.

The separate calculation also proves necessity of this tuning within the
specified rate family. Put `R=(1-rho)(u+4E rho)^2>=0`. In a unit axis direction
the only possibly nonzero squared speed is `(2F^2+R)/3`. In a unit body-diagonal
direction the squared speeds are `F^2/3,F^2/3,R/3`. A nonzero speed common to
all directions must occur in both lists. Equality with R/3 forces F=0;
equality with F^2/3 would require F^2+R=0 and hence a zero speed. Thus F=0
is necessary, and (8)-(11) prove sufficiency for E!=0 and 0<rho<1. This does
not classify other context rules or prove that dynamics selects the tuning.

The finite-time stationary covariance first-moment sum rule from
`IMMUTABLE_STREAMING_DERIVATION.md` is expected to extend to this bounded
conservative range-two generator once its hypotheses are rechecked. It would
fix signed correlation centers. Even that identity would not establish
propagating narrow peaks, their widths, a hydrodynamic limit or a relativistic
field. The current derivation does not use that extension as a premise.

## Relation to continuing formation

The conservative process admits arbitrary homogeneous product compositions.
If every vacant site forms each of the six labels at the same additional
constant rate epsilon, the product family still evolves exactly:

`p_0(t)=p_0(0) exp(-6 epsilon t)`,

`p_a(t)=p_a(0)+p_0(0)[1-exp(-6 epsilon t)]/6`.

This follows because the exchange generator annihilates each member of that
family and the independent insertion generator is tangent to it. Thus records
may swap or move, leave vacancies, and permit later formation; counts increase
until full occupancy. An initially empty system crosses rho_* at
`t_*=-log(1-rho_*)/(6 epsilon)`. The exact evolving product background alone
does not prove an acoustic response about it. The conservative sound
linearization is an instantaneous frozen-density target; formation sources,
time variation and damping must be controlled before using it during growth.

The tuning is real: u/E and rho_* are supplied, not selected. Fixed positive
formation does not keep rho at rho_*. At full occupancy the number density
does not fluctuate, and (11) degenerates as rho_* tends to one. This candidate
therefore does not yet supply a permanently active density wave after all
vacancies have filled. It does show that the endpoint-only current restriction
cannot be promoted to all local immutable-record exchange laws.

## Scientific status and decisive next checks

The primary portable check and the separate pre-source calculation both cover
product stationarity, covariance including reversed bonds, positive rates,
direct product averages, the six-field current spectrum and homogeneous
insertion. The separate report also supplies the tuning necessity argument
above. Its report SHA is
`277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713`.
Its scope is the exact generator and current algebra; it does not approve the
later Euler proof, finite simulations or any physical identification.

The first calibrated microscopic screen on sides 16,24,32 has oscillatory
density correlations and finite-wave-number speeds approaching (11). The
larger-lattice follow-up and a separately declared continuing-formation test
are in progress. These finite results are evidence about this supplied model;
they do not establish convergence or isotropy in a scaling limit. The new
Euler proof attempts the more important missing local-equilibrium step for
smooth profiles. The nonlinear symmetrizer, one-block argument, reaction
scaling and distinction from equilibrium fluctuations require separate scrutiny.

Speed-change exclusion and multi-species product-stationary transport are
established subjects. The self-contained four-site cancellation and its
six-axis tuning are the present candidate; no novelty or borrowed
hydrodynamic theorem is asserted. The initial literature search located the
relevant subject but has not yet checked a primary theorem applicable to this
specific generator.
