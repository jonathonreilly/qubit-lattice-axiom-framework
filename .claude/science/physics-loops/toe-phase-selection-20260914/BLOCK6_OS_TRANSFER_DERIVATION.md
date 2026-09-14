# Bounded Euclidean observables and the reconstructed transfer gap

Personal working derivation, 2026-09-14. This note separates an elementary
conditional transfer theorem from an application of two named literature
results to compact U(1) Villain theory. Neither establishes the selected
finite-clock Hamiltonian or an axiom-derived physical law.

## 1. Reconstruction from a specified probability state

Let mu be a translation-invariant probability measure on lattice fields in
Z^D. Use the algebra A_+ of bounded local continuous gauge-invariant functions
supported at times >=0. Theta_0 is complex conjugation followed by geometric
time reflection through the site plane t=0, including oriented-link reversal.
Assume site and link reflection positivity. Define

    (F,G)_OS = E[(Theta_0 F) G].

Positivity gives the quotient by null vectors. Since mu is a probability
measure, ||[F]||_OS <= ||F||_infinity. Time translation induces T[F]=[tau_1 F].
Translation invariance and Theta_0 tau_1=tau_-1 Theta_0 give symmetry of T.
The link reflection through t=-1/2 gives

    (F,TF)_OS = E[(Theta_-1/2 F) F] >= 0.

For well-definedness and boundedness, Cauchy--Schwarz gives
||TF||^2 <= ||F|| ||T^2 F||. Iterate the same inequality at doubled powers;
all translated functions have OS norm bounded by ||F||_infinity. Taking the
iterated root proves ||TF|| <= ||F||, including null vectors. Thus T extends
to a positive self-adjoint contraction. Spatial translations induce commuting
unitaries. Constants define a unit invariant vector Omega. Ground-space
uniqueness is not assumed. If T has a kernel, discuss -log T on its positive
spectral support; the near-one spectral conclusion below is unaffected.

For a finite spatial graph, a concrete Villain transfer is D P K D. D is the
square root of the spatial plaquette weight, P averages site gauge rotations,
and K is a tensor product of temporal heat convolutions. D and K commute
with P. Strictly positive heat Fourier coefficients make K injective and
positive; compactness and trace class hold on a finite product of circles.
On the physical range of P, DPKD is positive and injective. Its continuous
strictly positive kernel is positivity improving; the top eigenvector is
unique and positive at finite volume. These finite-volume facts do not alone
identify a thermodynamic state or provide a uniform gap.

## 2. The slab estimate, with invariant-space subtraction

Let F,G have time support in [0,1]. Set F^sharp=tau_1 Theta_0 F, also supported
in [0,1]. For R>=1 and spatial displacement y,

    E[F tau_(R,y) G] = ([F^sharp], T^(R-1) U_y [G])_OS.

This identity follows by translating both functions in the OS expectation
forward by one step. It does not require an operator T^(-1/2) K_F T^(-1/2).
Let P_1 be the projection onto ker(I-T). If P_1[G]=0 and
spec(T) subset [0,exp(-gamma)] union {1}, gamma>0, then

    |E[F tau_(R,y) G]| <= ||F||_infinity ||G||_infinity
                          exp[-gamma(R-1)].

A sufficient test for P_1[G]=0 is
E[(Theta_0 G) tau_t G] -> 0: the spectral theorem says its limit is
||P_1[G]||^2. This is stronger and more precise than merely subtracting the
one constant vector when the full ground space may be degenerate.

An equivalent finite-cylinder check uses T normalized to top eigenvalue one
and unit positive Perron vector Omega. If a slab insertion satisfies the
pointwise kernel inequality |K_F(a,b)| <= C_F T(a,b), then
|K_F Omega| <= C_F Omega and |K_F^* Omega| <= C_F Omega. Hence both vectors
have norm at most C_F. The connected two-insertion covariance is bounded by
C_F C_G exp[-gamma(R-1)] when the Perron vector is the full ground space.
The same proof works for a continuous positive integral kernel.

## 3. Isotropy and summability

Suppose the state is invariant under coordinate permutations and reflections,
and a finite family of centered local observables is closed under these
operations up to a common translation and a phase of modulus one. All have
support in one elementary cube and sup norm at most C. Assume the reflected
temporal two-point functions of this family tend to zero, so their OS vectors
have no invariant-space component. Rotate a coordinate realizing
n=||x||_infinity into positive time. Common anchor shifts cancel between the
two translated observables. Section 2 and the trivial bound at n=0 give

    |C_ab(x)| <= C^2 exp[-gamma max(n-1,0)].

Therefore all such covariances are absolutely summable. In D=4 the shell
cardinality is (2n+1)^4-(2n-1)^4=64 n^3+16 n. With q=exp(-gamma),

    sum_x |C_ab(x)| <= C^2 [1 + 64(1+4q+q^2)/(1-q)^4
                               + 16/(1-q)^2].

Consequently a clustering but nonsummable member of this covariant family
forces positive transfer spectrum arbitrarily close to one below one. This
is a gapless reconstructed Hamiltonian conclusion and needs no locality
hypothesis on its logarithm. It does require the stated Euclidean isotropy
and clustering. An anisotropic state with spatial power-law correlations
and a fixed Ornstein--Uhlenbeck temporal contraction is a counterexample if
isotropy is omitted. A mixture of constant fields plus independent local
noise is a counterexample if invariant-space subtraction is omitted.

## 4. Original and dual Villain observables: sign and contact term

Use normalized Haar measure and phi_beta(theta)=sum_n exp[-n^2/(2beta)]
exp(i n theta). It is a positive smooth even function. The real score
s=phi_beta'/phi_beta is bounded and odd; the FS convention is Phi=-i s.
On a finite contractible region, expanding each plaquette Fourier series and
integrating all links gives the positive integer two-form law

    probability(n) proportional exp[-||n||^2/(2beta)], delta n=0.

One insertion of Phi replaces a plaquette weight by -i phi', with Fourier
coefficient n exp[-n^2/(2beta)]. Two distinct insertions therefore reproduce
E[n_p n_q]. At a repeated plaquette the n^2 insertion is -phi''/phi, which
is not Phi^2. In the charge-conjugation-invariant state all first moments
vanish. For one orientation in a translation-invariant limit,

    C_s(x) = kappa delta_(x,0) - C_n(x),
    kappa = E[-(log phi_beta)''(d theta_p)]
          = E[n_p^2]+E[s_p^2].

Both sides have a well-defined local limit if the compact state does. The
same calculation includes fixed Hodge-dual orientation/anchor conventions.
The integer closed two-form is *dA on a free finite box; no periodic harmonic
sector is silently dropped. The diagonal contact term changes a Fourier
transform by a constant and cannot remove a directional discontinuity.

## 5. Exact imported estimate and the inference drawn from it

The deep input is Fröhlich--Spencer (IHES P/81/40, pp.44--52, equations
2.90--2.106; published CMP83 (1982) 411--454): for sufficiently large beta,
there is beta''>0 with a two-sided covariance bound on finitely supported
coclosed dual one-forms mu,

    beta'' (mu,(-Delta)^-1 mu) <= E[|A(mu)|^2]
                              <= beta (mu,(-Delta)^-1 mu).

It is a result about four-dimensional compact U(1) Villain theory in its
free-boundary state. The present note does not re-prove the deep
renormalization estimate. Its observable and state hypotheses are checked
here; the remaining argument is supplied explicitly. No finite-Z_N
field-strength estimate is imported from section 3's loop estimates.

Take mu=delta sigma, where sigma is a finitely supported test two-form of
one dual plaquette orientation (rho,sigma). Fourier transformation of the
free discrete Hodge Laplacian yields the multiplier

    q_rs(k)=(|e^(i k_r)-1|^2+|e^(i k_s)-1|^2)
             / sum_j |e^(i k_j)-1|^2,  k != 0.

The two-sided quadratic-form inequality implies the dual covariance has a
density S_n with beta'' q_rs <= S_n <= beta q_rs almost everywhere. In
particular S_n is bounded and integrable. The Riemann--Lebesgue lemma gives
C_n(x)->0, and section 4 gives the same clustering for the bounded score.

If C_s were summable, its Fourier transform would be continuous, so
S_n=kappa-hat(C_s) would admit a continuous version. The almost-everywhere
sandwich would then hold everywhere away from zero by continuity. Along an
axis outside the rs plane it forces the limit to zero; along an axis in the
plane it forces liminf >= beta''>0. Contradiction. Thus the bounded score
clusters but is not summable. Under the reconstruction and isotropy checked
in sections 1 and 6, section 3 implies gaplessness in its observable sector.

## 6. State selection and reflection positivity: checks still to complete

Chevyrev--Garban, arXiv:2404.09928v2, Corollary 1.6, proves monotonicity of
Villain Wilson-loop expectations in the plaquette couplings. Its proof uses
the carpet-graph limit in Theorem 1.5. Remark 1.7 explicitly observes that
log Villain weight does not have all nonnegative Fourier coefficients, so a
direct application of the usual exponential-cosine Ginibre premise is invalid.

Given this monotonicity, extend a smaller box's couplings by zero in a larger
box. Increasing the new couplings to beta gives monotonicity in region size.
Every finite closed integer edge current can be written as a single closed
walk, allowing repeats and adding canceling connecting paths; Abelianity
makes its character the required Wilson loop. Nonclosed currents have zero
expectation by gauge invariance. Thus every local character has a unique
free-boundary net limit. Character density on finite products of circles
and consistency give a local probability limit. Cofinality of translated,
rotated or reflected rectangular exhaustions yields the same limit, proving
the required symmetries. Charge conjugation follows already at finite volume.

For site reflection, a symmetric finite box factors over its fixed boundary
variables into a half weight and its reflected conjugate, giving a squared
modulus integral. For link reflection, fix the crossing temporal links to
identity by gauge transformations (they form a forest). Gauge-invariant
functions are unchanged. Every crossing plaquette weight then has the form
sum_n c_n (Theta chi_n) chi_n with c_n>=0; integration gives a sum of squared
moduli. Symmetric finite boxes around either required plane have the same
free-boundary local limit, preserving these inequalities. This supplies both
site and link reflection positivity needed in section 1. The explicit
boundary conventions and null-vector argument still require author checks.

## 7. Scope

This route spells out how the established Villain Euclidean masslessness
result yields a positive-energy accumulation for a specified reconstructed
transfer. It is not a new discovery of the U(1) massless phase. It removes a
locality proof as a prerequisite for this particular gap inference. The
selected finite-clock continuous-time operator, its phase, its native
formation law, the linear dispersion and detailed particle interpretation
remain separate obligations. No axioms or primitives have been changed.
