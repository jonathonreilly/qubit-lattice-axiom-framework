# Working continuation: observable algebra and matter state

2026-09-16 02:32 UTC. Active personal derivation, not yet reviewed theorem.
Blocks02--03 are pushed at b1bed2bc535c1704e5e0d67ce21fee5c099603ad.
Deadline remains13:45:03 UTC; no subagents. The next milestone is the joint
equal-time state, not real-time or fixed-g physics.

## A. Exact transport and asymptotic Weyl multiplication

For w=(u,v), put beta=g W_E^(1/2)u and

    phi_w(theta)=int_0^1 Z(v)(theta+s beta) ds.

The actual exponential satisfies

    W_g(w)psi(theta)=exp[i phi_w(theta)] psi(theta+beta).

This follows by differentiating the first-order transport equation, without
assuming canonical commutators. Taylor expansion of sine has a uniform
pointwise remainder O(g) for fixed local u,v:

    phi_w=Z(v)(theta)+(1/2)(Su).diag(cos theta_p).v+O(g).

Thus the exact multiplication-phase difference in W(w)W(w') is

    phi_w(theta)+phi_w'(theta+beta)-phi_(w+w')(theta)
      =(1/2)[(Su).diag(cos theta_p).v'
                   -(Su').diag(cos theta_p).v]+O(g).

Define sigma(w,w')=(Su).v'-(Su').v. The compact remainder is a fixed
coefficient sum of cos theta_p-1 plus an O(g) bounded function. Its ground
L2 norm is O(g), including after any finite number of translations by
g W_E^(1/2)u_j. Therefore

    ||[W(w)W(w')-exp(i sigma/2)W(w+w')]||_rho=O(g),

and the same estimate holds on states made by finitely many W's and bounded
matter dressings on the right. The extra translation from W(w+w') must be
included, rather than bounding the phase on the untranslated ground state.
This gives the ordinary Weyl product and all finite pure-gauge word limits
from Block03. Check the positive sign exp(+i sigma/2).

## B. A local CAR extension with an explicit root

Fix root0 and an integer path p_x from0 to each lattice site x, with paths
finite for each fixed x. On a sufficiently large torus embed any given
finite collection without wrapping ambiguity. Define auxiliary charged

    a_(x,s)=U(p_x)^(q_s) c_(x,s),       q_+=1,q_-=-1.

These satisfy exact CAR because rotor multiplication commutes with all
matter operators. They carry gauge charge only at the root. Hence their
globally charge-neutral polynomials are physical, and define an exact
*-homomorphism j from the neutral finite CAR algebra to physical bounded
operators. The full CAR map exists on the ambient rotor/Fock Hilbert space
but its nonneutral elements do not preserve Gauss law; use them only as an
auxiliary positive state extension, not as physical charged observables.

The physical ground density matrix is also a positive trace-class state on
that ambient Hilbert space. Thus rho composed with the full finite CAR map
is positive, normalized, and zero on nonneutral monomials by gauge invariance.
Fixed N_+,N_- additionally gives the separate number symmetries.

Changing paths for a fixed neutral polynomial changes it by fixed finite
Wilson loops. Every such contractible loop is an integer sum of finitely
many plaquettes, so Block01 and telescoping bound its L2 difference by Cg.
Changing the root contributes a common connector phase, which cancels for
net charge zero. Consequently any limiting full CAR state is translation
invariant: translate the root/path system, then compare it to the original
one. Nonneutral expectations are zero on both sides. This does not assert
translation invariance of the rooted finite-g extension itself.

For fixed local smear u, [P(u),a_(x,s)] is exactly
g q_s <W_E^(1/2)u,p_x> a_(x,s); Z commutes with a. Therefore

    W(u,v) a_(x,s) W(u,v)^*
      =exp[i g q_s <W_E^(1/2)u,p_x>] a_(x,s).

The field unitaries commute in operator norm with every fixed dressed CAR
polynomial in the g->0 limit. This is stronger than a ground-state estimate.

## C. Energy forces the free filled-band covariance

State compactness supplies subsequential limits on the infinite CAR algebra.
Translation invariance follows from B. The local zero-field energy density
at root0 maps exactly to the physical gauge energy density for the onsite
term and the three forward nearest-neighbor links when p_(e_i)=e_i.
Alternatively a fixed-loop O(g) comparison is sufficient. Block02 gives

    omega(h_m,local)=lim E_m,L/V=e_m,free.

For a translation-invariant CAR state, its one-particle covariance is a
positive contraction C on l2(Z^3) tensor C^4 commuting with translations.
After Fourier transform it is multiplication by a measurable matrix
C(k), 0<=C(k)<=I almost everywhere. In particular it has no atomic momentum
measure at an isolated Weyl point: the CAR bound C<=I excludes atoms.

Let h(k)=h_+(k) direct-sum h_-(k) and P_-(k) its negative spectral projection.
The positive energy-density excess can be written

 int tr |h(k)| [P_+ C(k) P_+ + P_- (I-C(k)) P_-] dk/(2pi)^3.

It vanishes. The zeros of h are the finite Weyl-node set for0<zeta<1, hence
have Lebesgue measure zero. Positivity forces C=P_- almost everywhere;
off-diagonal blocks vanish by positivity of C and I-C. This reasoning uses
neither a finite-volume gap nor uniqueness of a finite-volume ground vector.

Projection covariance fixes the ENTIRE CAR state, not just its two-point
function. For f in range P_+, a(f) annihilates its GNS vector; for f in
range P_-, a(f)^* does. CAR reordering gives all polynomial expectations
as the filled-band Slater expectations. Approximate arbitrary vectors by
finite sums in orthonormal bases of the two spectral subspaces. Uniqueness
of this vacuum functional also proves purity: a convex decomposition must
give zero for each of the same nonnegative excitation occupations, so both
components have exactly the same vacuum functional.

## D. Joint state and factorization

Take a finite or countable set of local field probes and CAR polynomials.
Boundedness gives subsequential joint word limits. Exact CAR multiplication,
asymptotic field/CAR norm commutation, and the transported Weyl-product
estimate in A make this a positive state on the commuting Weyl/CAR algebra.
Positivity comes directly from rho(X^*X)>=0 for finite word polynomials;
the product estimates are required on all such word-excited vectors.

Its CAR marginal is the pure Slater state from C. For any positive bounded
gauge element G, the functional omega_G(B)=sigma(G B) on CAR is positive and
0<=omega_G<=||G|| omega. Purity implies omega_G=sigma(G) omega: otherwise
the dominated positive functional would give a nontrivial convex splitting
of omega. Extend by linearity to arbitrary bounded gauge elements.

Hence the joint limit factorizes into Block03's Gaussian gauge state and
the free paired Slater state. Any subsequence has the same finite-word
limits, so the full joint sequence converges. The physical statement is
restricted to neutral finite-path matter polynomials; the full CAR extension
is a proof device used to make purity available.

## Checks still to do

1. Explicitly test Weyl phase sign by exact transport or finite rotor matrices,
   including the translated cosine term and a sign-reversed discriminator.
2. Check rooted gauge-CAR phase conventions against literal charged matrices.
3. Keep zero-mode ambiguity distinct from the infinite-volume covariance
   argument; consider a finite zero-mode counterexample as a discriminator.
4. Write the full note only after the joint-state positivity and path estimates
   have been checked on word-excited states. No real-time or fixed-g claim.
