# A finite-clock local generator for anisotropic monopole suppression

Personal working derivation; no independent review, retained status, or photon
phase theorem. This is an explicitly DIFFERENT candidate Hamiltonian from the
nearest-clock model of PR8120/8121. It is not an axiom-selected dynamics.

## 1. Candidate on the actual three-state link carrier

On a finite cubic spatial lattice let a_l in Z3, let F be the face-edge
incidence matrix, and let b_p=principal((F a)_p) in {-1,0,1}.
For a unit shift of link l by sigma=+1 or -1, put

    b'_p=principal(b_p+sigma F_pl),
    m_p(a,l,sigma)=(b'_p-b_p-sigma F_pl)/3,
    r_(l,sigma)(a)=t exp[-mu_t sum_(p incident l) m_p(a,l,sigma)^2].

Here t>0, mu_t>=0. Each m_p is an integer, with absolute value at most1.
At most four spatial plaquettes meet a cubic link. Thus

    t exp(-4 mu_t) <= r_(l,sigma)(a) <= t.

Define A_l by its coordinate matrix elements

    A_l |a> = sum_(sigma=+1,-1) r_(l,sigma)(a) |a+sigma e_l>.

Reversing the move changes m to -m and preserves its rate, so A_l is
Hermitian. Its entries are nonnegative, its row sums at most2t, and
||A_l||<=2t. Every A_l is invariant under lattice Gauss translations,
since its rates depend only on plaquette flux and shifts commute.
Its support is the union of plaquettes incident on l. Consequently

    H_mu = sum_l (2t I-A_l) + V_spatial(b)

is a bounded finite-range Gauss-invariant Hamiltonian for any bounded local
real diagonal V_spatial. The individual electric summands are positive.
For finite mu_t, every link shift still has strictly positive rate. On a
finite connected full coordinate configuration graph, Perron-Frobenius
therefore gives a unique strictly positive ground vector. Gauss invariance
then makes that vector physical. This is a finite-volume statement; the
spectral gap may close in a thermodynamic limit.

One possible spatial potential is

    V_spatial = K sum_p [1-cos(2pi b_p/3)]
                + lambda sum_c [(d b)_c/3]^2,

with K,lambda>=0 and the integer cube charge evaluated with oriented b.
The Bianchi identity makes (d b)_c divisible by3. The second sum vanishes
on a purely two-dimensional open strip but is local in three dimensions.

## 2. Finite-box transfer limit with all scaling choices exposed

Let delta>0 be the temporal step. Set x=delta t. A temporal link difference
eta_l in Z3 has normalized weight x for eta_l=+/-1 and weight1 for0.
This is exactly the normalized three-state Wilson temporal weight when

    exp[-3 beta_t/2]=delta t.

For adjacent configurations a,a', multiply these link weights by

    exp[-mu_t sum_p ((b'_p-b_p-(F principal(eta))_p)/3)^2],

where eta=a'-a mod3. Gauge projection amounts to summing these differences
in the physical flux kernel. On a fixed finite box the identity difference
has weight1. Every single nonzero link difference has weight delta t and
the indicated rate multiplier. Differences on at least two links have
weight O(delta^2); there are finitely many. Hence

    K_delta = I + delta sum_l A_l + O_box(delta^2).

The exponent's mismatch is integer because F eta=b'-b modulo3. Reversing
a,a' sends both principal eta and the mismatch to their negatives, so the
kernel is symmetric. It is positive definite for sufficiently small delta
on each fixed box, by continuity from I; this is NOT a volume-uniform
reflection-positivity theorem for arbitrary step or geometry.

Sandwich with M_delta=exp[-delta V_spatial] and normalize by the harmless
scalar exp[-2t |E| delta]:

    T_delta = exp[-2t |E| delta] M_delta^(1/2) K_delta M_delta^(1/2)
            = I-delta H_mu+O_box(delta^2).

It follows in finite-dimensional operator norm that, at fixed box and time,
T_delta^(floor(T/delta)) -> exp[-T H_mu]. This is a genuine local generator
on a fixed three-state link payload. The remainder is not asserted uniform
in volume, nor sufficient for interchanging infrared and time-step limits.

A crucial distinction is that mu_t remains fixed on temporal cubes, while
the coefficient of the spatial cube penalty in the Euclidean action must
be delta lambda to obtain finite lambda above. Keeping a nonzero spatial
penalty coefficient fixed as delta->0 instead imposes an infinite penalty;
the low-energy constrained dynamics then needs a separate derivation.
The isotropic Euclidean model does not silently choose this anisotropic
trajectory or prove that it stays in a photon phase.

## 3. Compatibility with the remote membrane deformation estimate

Let V_v be the product link shift for the membrane used in PR8120, with
curl Fv confined to its boundary. Conjugation by V_v changes diagonal
plaquette flux only where Fv is nonzero. It changes A_l only if a plaquette
incident on l meets that boundary. Thus V_v H_mu V_v*-H_mu is supported in
a fixed-radius enlargement of the membrane boundary, with norm bounded
by a constant times its size. The added spatial cube potential has the
same property because it depends locally on b. Loop charge algebra and
full carrier Lieb-Robinson bounds therefore remain available with updated
interaction constants. The optimized-loop and transition-norm criterion
can be investigated for this candidate without assuming locality of a
finite-step transfer logarithm.

This locality observation supplies no estimate of the same-state loop
expectations. It also does not prove that changing mu_t induces a photon
phase, that positive ground amplitudes control quantum fidelity, or that
the original charged-matter Hamiltonian is equivalent to H_mu.

## 4. Source boundary and remaining test

The effective-field-theory discussion in [Nguyen, Sulejmanpasic and Unsal,
arXiv2401.04800v2](https://arxiv.org/html/2401.04800v2) explicitly assumes
Poincare symmetry and studies a constrained Villain alternative. Its
Wilson deformation is proposed there. That analysis does not select the
anisotropic generator above or derive native emergent relativity. Reading
scope here: main text sectionsI-IV; the corrupted HTML appendix was not
used. The finite-clock generator above is a direct expansion of the
explicit kernel, with its own stated assumptions.

Next decisive work: either establish useful dressed-loop and boundary
transition estimates for H_mu at fixed N=3, or show why the proposed
monopole penalty fails to produce them. First compare the actual phase
under a controlled anisotropic interpolation. Neither finite positive
transfer samples nor the infinitesimal expansion prove such stability.

## 5. Explicit remainder and the normalization distinction

Let E=|E|>=2, x=delta t, and R_delta=K_delta-I-delta sum_l A_l.
Its coordinate entries are nonnegative: they sum precisely the moves on
at least two links. Since mu_t>=0 suppresses their weights, each row sum
is at most

    (1+2x)^E-1-2Ex <= 2E(E-1)x^2(1+2x)^(E-2).

The last inequality is Taylor's integral remainder for (1+2x)^E. Symmetry
then bounds ||R_delta|| by the same expression. Orthogonal Gauss projection
cannot increase this operator norm. For E=0 or1 the corresponding remainder
is zero. This makes the finite-box qualification quantitative: the bound
grows with E and does not by itself control an infinite-volume phase.

For a nonnegative spatial potential, ||M_delta^(1/2)||<=1 and the normalized
transfer obeys

    ||T_delta|| <= exp(-2Ex)(1+2x)^E <=1.

Also H_mu>=0. Telescoping powers against exp(-delta H_mu) yields the direct
finite-time error at n steps,

    ||T_delta^n-exp(-n delta H_mu)||
       <= n ||T_delta-exp(-delta H_mu)||.

Together with the Taylor bounds for the diagonal sandwich and scalar
normalizer, this proves the stated O_box(T delta) convergence for fixed T.
It supplies no exchange of volume, time-step and long-distance limits.

The electric diagonal 2t per link comes from the scalar normalization.
It is generally NOT sum_sigma r_(l,sigma)(a). Replacing it by that
configuration-dependent escape rate would create a different Markov-type
Hamiltonian and alter the ground state. Such a replacement cannot be used
to identify this Euclidean limit with a chosen stochastic dynamics.

The separate three-dimensional finite check uses a periodic 5^3 cubic
complex, verifies both incidence identities, Gauss invariance, integer
cube charges, the four-plaquette rate bound, reverse-move symmetry, and
unchanged rates outside the enlarged boundary of a four-link membrane.
The exact transfer comparison uses the open two-plaquette physical flux
space and all 2187 link differences. These are complementary author
checks of the construction, not an independent scientific review.
