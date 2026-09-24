# POST comparison: actual first-birth rotor energy lower bound

No mathematical correction is required in the released root note. Its full
stated conclusion agrees with the independently sealed PRE:

    for each specified i and fixed delta,kappa>0,
    f_i(tau)>=c_i(1+tau)^(-5/2),   c_i>0,   tau>=0.

Hence these three limiting curves have no eventual upper bound A exp(-a tau)
with finite A and a>0. This is a scoped corollary for fixed physical inputs in
the supplied rotor model. It is not a universal physical no-go or a sharp
asymptotic law. The independent PRE's 27 bindings remain unchanged.

## Exact source and exposure record

The full released rate proof was read:
`ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND.md`, SHA256
`a8cbb5fa4f71f4fde6644a1242ef1741799c701c2ce8835b5da42b46c5075745`.
Its author seal is
`3a8305a55aaef7feb91ab07499b3c2c70059d1f3b7bf9a66d84fe5863f2082a4`.
The author packet contains one analytic note and four source identities; no
new scientific script is represented as having been independently replayed.

The full completed tail comparison report was also read, SHA256
`bf40d648eedecf994ad8668cbb9c647f36323940c03b43674f99061c06f2ef75`,
with final seal
`f3922528290f8f2f8d72e0b5cd230ab9586b1400d6b2cd8e90e7d55ae36c5fff`.
That report verifies the physical cycle-coordinate change, all288 nonzero
Laurent coefficients, the full exact rank witnesses and the actual first-mark
words. It requires no mathematical source correction. This POST reuses that
completed scoped check; it does not claim to repeat its full68-file review.
Its preserved execution failures and the earlier failed historical floating
comparison remain historical failures, not silently upgraded successes.

The independent rate PRE seal is
`84f629be9deb702e119a333fc8ae85d940586f4493ebd86405a0a215f61600d7`.
It was authenticated and read by root before the rate-author release. The
PRE's proof, new local matrix code, full output, source manifest, execution
receipt and restricted scope sidecar are unchanged. POST_SOURCE_BINDINGS.json
maps the released snapshots and the reused PRE dependencies by exact hashes.

## 1. Algebraic simplicity and the parameter domain

The root uses precisely the supplied bounded physical fibers
`L(theta)=-i delta G(theta)-kappa P_bright` on C96 and the complete five-cycle
rotor Fourier representation. It retains the original resolved/coherent
instruments, positive fixed delta,kappa, W=1, N=6 and total charge four.

For an imaginary-axis eigenvector at theta=0, dissipativity gives P_bright v=0.
The bright eigenvector equation then gives Q(0)v=0 because delta>0. Exact
rank(Q(0))=23 confines v to the span of the uniform dark vector u. Since the
dark block vanishes, its eigenvalue is zero. Thus the assertion that every
other eigenvalue has strictly negative real part is valid. It is stronger than
what the local rate proof needs, but does not assume normality.

Both L(0)u and L(0)*u vanish. The orthogonal decomposition
`span(u) direct-sum u-perp` therefore reduces L(0) to `0 direct-sum B0`.
The preceding kernel argument makes B0 invertible. This establishes algebraic
simplicity, not merely a one-dimensional geometric kernel, and excludes a
Jordan chain into u. It is the same valid simplicity argument made explicitly
in PRE section3.

The fixed-positive-parameter assumption is essential. No uniform claim as
delta or kappa tends to zero is made. Neither a numerical gap threshold nor a
full exceptional-phase classification is used.

## 2. Independent reconstruction of the root derivative route

The finite Laurent fiber is analytic in real angular coordinates and admits
a local analytic continuation. Choose a spectral circle around the simple
zero eigenvalue. Resolvent continuity keeps this circle free of spectrum in
a phase neighborhood. Its contour integral gives a rank-one analytic P(theta),
with P(0)=u u*. The finite-rank trace
`lambda(theta)=Tr[L(theta)P(theta)]` is its simple eigenvalue.

One may take `v(theta)=P(theta)u`; v(0)=u and it is nonzero nearby. Differentiating
`L(theta)v(theta)=lambda(theta)v(theta)` at zero yields

    (partial_j L)(0)u + L(0)(partial_j v)(0)
      = (partial_j lambda)(0)u + lambda(0)(partial_j v)(0).

Left multiplication by u* removes the second term and the last term, since
u*L(0)=0, lambda(0)=0 and u*u=1. Consequently

    partial_j lambda(0)=u*(partial_j L)(0)u.

Gamma is constant. Because the original G dark/dark block is identically zero
as a Laurent polynomial and u belongs to that fixed charge subspace,

    u*G(theta)u=0 for every theta,
    u*(partial_j G)(0)u=0,
    partial_j lambda(0)=0                         for j=1,...,5.

This verifies the full complex derivative, not just its real part. The
identical dark-block statement is the load-bearing premise at this step;
knowing only G(0)u=0 would not by itself establish all complex derivatives.
The completed tail comparison explicitly checked that polynomial premise.

For a smaller closed real ball, the analytic eigenvalue has bounded second
real derivatives. Applying the one-variable integral Taylor formula to
`g(s)=lambda(s theta)` gives

    lambda(theta)=integral_0^1 (1-s)
                 sum_(j,k) theta_j theta_k
                      partial_j partial_k lambda(s theta) ds.

A finite bound for this quadratic form therefore supplies M with
`|lambda(theta)|<=M|theta|²`. In particular
`Re lambda(theta)>=-M|theta|²`; dissipativity supplies the other inequality
`Re lambda(theta)<=0`. No Hessian positivity, reality of lambda, or leading
nonzero quadratic coefficient is required. If the dispersion is flatter, the
claimed lower bound remains valid.

The independent PRE used a different sufficient estimate. Its resolvent
bounds give `v(theta)=u+O(|theta|)`, and the original dissipative form gives

    Re lambda(theta)=-kappa||P_bright v(theta)||²/||v(theta)||²
                    >=-beta|theta|².

That proof needs only a quadratic bound on the real part and does not establish
that the full complex first derivative vanishes. The root's stronger local
complex estimate is correct for the additional identically-zero-dark-block
premise. Neither route is silently substituted for the other. PRE section2's
separate contractive Duhamel lower bound proportional to (1+tau)^(-5) is also
retained as its own weaker derivation.

## 3. Fixed-input projection and physical five-ball integration

The root uses exactly the finite physical-word coefficients R_i/sqrt(b_i).
Their normalized flat projections have squares1/12,1/12,1/6. These values were
independently reconstructed in PRE from local charge/link actions, with Gauss
checks and all1728 flat bright/dark matrix entries compared by charge labels.
They are fiber overlaps, not physical probabilities of occupying a single phase.

Their Fourier vectors and the Riesz projector are continuous. Nonzero flat
projections therefore give a positive lower bound a_i on
`||P(theta)rhat_i(theta)||` in a sufficiently small fixed neighborhood, while
`||P(theta)||<=B` there for a finite B. Rank one and commutation with L give

    P(theta) exp[tau L(theta)]rhat_i(theta)
      =exp[tau lambda(theta)]P(theta)rhat_i(theta).

The norm inequality `||w||>=||P(theta)w||/||P(theta)||` is valid for a general
bounded idempotent, including a nonorthogonal spectral projector. Thus the
root's lower estimate does not presume normality, subtract a decaying
complement, or overlook cancellation among spectral components.

In the phase ball `|theta|<=r/sqrt(1+tau)`, the projected norm is at least
`(a_i/B) exp(-M r²)`. Its squared integral has normalized Haar volume

    Vol(B5(1)) r^5 / [(2pi)^5(1+tau)^(5/2)],
    Vol(B5(1))=8pi²/15.

This gives exactly the root's positive constant and exponent. The coordinate
ball is within the torus chart. The initial vector remains fixed; only the
region used to bound its physical integral shrinks with time. This is the
required step that the prior operator-norm nondecay result alone did not give.

The contradiction with an eventual exponential upper bound is immediate from
`exp(a tau)/(1+tau)^(5/2)->infinity`. It does not exclude exponentially decaying
pieces of the solution or establish any rate for inputs whose flat projection
vanishes. The PRE's relative-minus coherent discriminator retains an explicit
example where this input hypothesis fails.

## 4. Dependency update, limits and disposition

The strong-decay predecessor now has a completed independent comparison under
its exact scope. Combined with the present lower bound, it gives
`f_i(tau)->0` with no eventual positive-rate exponential upper bound for these
three fixed curves. The compact-time identification remains the separately
checked original-lambda-zero, zero-field, canonical-first-output result.
Updating that dependency record does not alter any frozen PRE bytes or grant
formal retained/audit status.

Both notes take the rotor/compact joint limit first, then discuss large tau
for the resulting curve. Neither permits tau=t/epsilon² inside the compact
estimate. Neither claims a fixed-positive-physical-time microscopic result,
finite-spin long-time theorem, sharp asymptotic, matching upper bound,
exceptional-set classification, energy destination, bath, reservoir selection
or universal damping no-go.

There is no discrepancy or required mathematical correction. The present POST
adds analytic source comparison and hash authentication only; no new matrix
scan, numerical fit, author replay or broadened research was needed. All PRE
and root bytes remain unchanged. No editable prompt, workflow or platform
instruction was modified; no commit, publication, audit or landing action was
performed. The scientific source aliases are portable by hash; any later
public omission of historical instruction snapshots requires explicit
provenance omissions in its own manifest.
