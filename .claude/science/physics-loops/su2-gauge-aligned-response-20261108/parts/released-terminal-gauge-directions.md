# Residual gauge directions after releasing terminal links

Author proof proposal, 2026-11-09. This is a finite-dimensional diagnostic
for the actual two-step conditional denominator, not a physical mass-gap
claim. Independent checking is pending. The prior identity-terminal proof
and its frozen reports are unchanged. No numerical experiment is used.

## 1. Law and coordinate convention

Use the finite four-dimensional periodic lattices, actual normalized
paired-root-leg kernels, fixed odd L >= 3, kappa > 0, u >= 1 and terminal
side m >= 3 of [the full response proof](full-connected-four-response.md).
Let J be terminal links integrated out and O their complement. At zero
sources and held output V_O = I, the unnormalized hidden density is exactly

    f_J(U0,U1) = q_u(U0) K0(U1|U0) product_(c in O) k1,c(I|U1).       (G1)

Indeed each missing output integral is one, including its input-dependent
normalizer. All factors present in (G1) retain their own normalizers.
Dividing by the integral of (G1) gives rho_J. No intermediate Wilson action
is inserted. The statement concerns zero source only; a source can break
the symmetries below.

Use exactly the terminal-root fine forest of
[compact disintegration](compact-forest-exchange.md), with all its fine
tree links fixed to I, all fine non-tree links and all intermediate links
retained. Let b(x) be the terminal root of the fine forest cell containing
an embedded vertex x. Write a_e = exp(i z_e dot sigma) for the retained
links near identity. The density relative to product Haar on this slice
is fbar_J(a). Put

    S_H,J(z) = -log fbar_J(exp(i z dot sigma)),
    S_J(z) = S_H,J(z) - sum_e log j(z_e) + n log(2pi^2),
    j(z) = (sin |z| / |z|)^2,
    H_J,u = u^(-1) Hess S_J(0).                              (G2)

There are n retained group coordinates. Every physical constant, including
the normalization convention for q_u, stays in S_H,J. Normalizing rho_J
would add a constant and does not change these Hessians. The Haar convention
matches [the Gaussian supplier](frozen-gaussian-producers.md), section 1.

Let G_O be the undirected graph with all terminal vertices and the retained
terminal edges O. Let r be its number of connected components, including
isolated vertices. No connectivity assumption on G_O is made.

## 2. Exact component symmetry

Choose k_C in SU(2) for each component C of G_O. For any embedded fine or
intermediate vertex x define k(x) = k_C where b(x) belongs to C. Act on
every retained hidden link by

    a_(x,y) -> k(x) a_(x,y) k(y)^*.                         (G3)

Both endpoints of each fine forest edge have the same b, so its value I
is preserved. Thus this is an action on the existing slice, not a further
gauge fixing or a change of integration variables depending on the field.
Product Haar on the retained coordinates is preserved by left and right
invariance.

Every fine plaquette trace is invariant. Telescoping along each actual
path word gives M_l,c -> k(x) M_l,c k(y)^*. For a first-layer kernel,
its output transforms by the same two endpoint matrices; its pairing and
radial norm, hence its numerator AND its normalizer, are invariant. For
c in O, its two terminal roots belong to the same component, so k(x)=k(y).
The last-layer output I is then fixed, and its mean is conjugated. That
kernel is invariant too. These arguments apply to each original path in
the average, so overlap and repeated edges do not change the conclusion:

    fbar_J(k.a) = fbar_J(a).                               (G4)

In particular applying (G3) to a = I gives the exact pure-gauge family

    a_(x,y)(k) = k(x) k(y)^*.                              (G5)

Every fine plaquette is I, each first-layer path mean equals its transformed
intermediate output, and every retained last-layer mean is I. The radial
norms of all these means remain one. Thus the physical density, including
the radial normalizers, is constant on this family. This last observation
checks (G4) at the configuration used next; it is not a concentration claim.

## 3. Explicit Hessian directions

The physical function S_H,J is smooth near identity. Each complete local
term is invariant under simultaneous global conjugation. Identity is fixed
by this action, and the tangent consists of copies of the adjoint three-
dimensional representation of SU(2). There is no nonzero invariant linear
functional on a copy. Restricting a derivative to each coordinate proves

    grad S_H,J(0) = 0.                                    (G6)

This also follows by differentiating each plaquette and normalized kernel:
their scalar part or radial norm has zero first derivative at identity.

Choose arbitrary vectors xi_C in R^3 and set
k_C(t)=exp(i t xi_C dot sigma). The tangent of (G5), in the stated logarithm
coordinates, is

    v_(x,y) = xi_(component(b(x))) - xi_(component(b(y))). (G7)

To prove that this is a kernel vector, a zero second derivative along the
orbit alone is insufficient for a general indefinite Hessian. Instead use
the full invariance (G4). Each point (G5) is a critical point, because a
diffeomorphism preserving S_H,J carries a critical point to a critical
point. Differentiating its zero gradient along the orbit at t=0 yields

    Hess S_H,J(0) v = 0.                                  (G8)

This argument requires no positivity assumption or asymptotic replacement
of a radial normalizer.

The map from the r vectors xi_C to retained-link tangents has kernel
exactly the common constant vectors. For if every retained-link difference
vanishes, it vanishes also on each forest edge by construction. The full
fine nearest-neighbor lattice is connected, so the resulting fine-vertex
function is constant. Every terminal root is a fine vertex; hence all
xi_C coincide. Conversely common values give v=0. Its rank is therefore
3(r-1). This is a subspace of gauge directions, not an assertion that it
exhausts all physical-action null directions.

Finally -log j(z) = |z|^2/3 + O(|z|^4). Therefore the coordinate Haar term
contributes (2/3) times the identity to the Hessian at zero. Equations
(G2) and (G8) give the exact finite-u statement

    H_J,u v = (2/(3u)) v                                  (G9)

on this 3(r-1)-dimensional subspace. The small positive number in (G9) is
a coordinate Haar curvature, not a physical mass. It does not assert any
negative mode or failure of a suitable further quotient.

## 4. Concrete witness and its scope

In four dimensions with m >= 3, choose J to contain all eight distinct
terminal edges incident to one terminal vertex and no others. That vertex
is isolated in G_O, so r >= 2. Equations (G7)-(G9) supply at least three
explicit directions of eigenvalue 2/(3u) on the unchanged terminal-root
slice. They are obtained by choosing xi nonzero only at the isolated root.
The full-lattice connectivity argument makes their linear independence
exact. No numerical spectral approximation is needed.

Consequently the uniform positive precision lower bound used for the
fully pinned law cannot simply be reused on this unchanged slice for
arbitrary J. This follows from this specific family of eigenvectors;
it is not an impossibility statement for the conditional-response route.
Removing the additional gauge freedom by an adapted quotient is a possible
next construction, with its own locality and source-covariance obligations.

The canonical union of two adjacent plaquettes has only seven edges. The
eight-edge example is NOT evidence that its particular complement graph
is disconnected, and gives no quantitative bound for that seven-edge law.
Even if a chosen G_O is connected, r=1 merely removes this witness. It
does not establish a compact coercivity constant, exclude other soft
directions, or bound any connected cumulant. Those are separate tasks.

No inference is made from these gauge modes to physical masslessness or
to a no-go for Yang-Mills. Gauge-invariant observables may be constant on
them. The actual next local task is a quantitative estimate for the stated
two-plaquette marginal, with its exact quotient, sources and normalizers;
arbitrary backgrounds and repeated blocking remain further obligations.

## Sources and checking status

Read inputs at author branch 4a3f6be4cf4ea0321bb5042c2969fc035479e7c2:

| Source | SHA-256 |
|---|---|
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |
| frozen-gaussian-producers.md | ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3 |
| full-connected-four-response.md | 04ef141738a356dd914608421a1d2cd135ff0f3cfbc1ac5f1ece81a71f0825c7 |

Supervisor derivation at the user's selected reasoning profile; exact model
identifier is not exposed. This is a mathematical proposal pending a fresh-
context proof check, with no formal audit or retained-status promotion.
