# Order independence on a general possibility alphabet

Personal proof candidate, 2026-09-15. This extends the finite
binary path/star argument to standard Borel alphabets using reversible
Markov operators. It is conditional on a supplied sequential construction,
slot-isotropic kernels and independence from every supplied order. None of
those process choices is adopted as an axiom. Finite author challenges pass; independent review is absent.

Let X be a standard Borel possibility space, pi the empty-neighbour law,
K(x,dy) the common one-recorded-neighbour kernel, and R_A the kernel for
each recorded slot subset A of the six neighbours. Write R_m for one such
fixed subset of size m; the star argument applies separately to every subset. Assume the output process on every finite
cubic window is the product of these conditional kernels in its supplied
site order. Suppose its finished joint law is the same for every order.
The same one-neighbour K in every slot is a substantive assumption.
All equalities below are measure equalities; null conditioning profiles
are never canceled as if they had positive probability.

On two neighbouring sites, the two orders give

    pi(dx) K(x,dy) = pi(dy) K(y,dx).

Therefore K preserves pi and is a selfadjoint contraction on L2(pi).
The three-site path in chain order gives endpoint law pi(dx)K^2(x,dz).
With endpoints first, their law is pi(dx)pi(dz), regardless of the final
middle-site kernel. Order independence implies K^2=Pi, where Pi is the
orthogonal projection onto constants in L2(pi).

For any real or complex f with pi(f)=0,

    ||Kf||_2^2 = <f,K^2f> = <f,Pi f> = 0.

Thus K=Pi as an L2(pi) operator. On a standard Borel space, apply this to
a countable generating class and intersect its full-measure sets, then use
uniqueness of probability measures. It follows that K(x,.)=pi for pi-almost
every x. No one-neighbour strict-positivity hypothesis is needed for this
a.e. assertion.

Now use a star with m mutually nonadjacent leaves. In center-first order
its joint law is pi(da) product_i K(a,db_i)=pi^(m+1). In leaves-first order
it is pi^m(db) R_m(b,da). Equality and regular-conditional uniqueness give

    R_m(b,.)=pi for pi^m-almost every b, m<=6.

The case m=0 is the definition. These a.e. identities also imply that all
finite empty-start joint laws are products: in any finite supplied order,
induction gives pi-product values at the already formed sites, so the next
site sees a pi^m-distributed neighbour profile and its conditional law is pi
almost surely. Conversely those a.e. kernel identities give product laws
in every supplied order by the same induction.

## From almost everywhere to pointwise needs regularity

If X is Polish, pi has full topological support on S, and the restrictions
R_m:S^m -> Probability(X) are weakly continuous, then the a.e. equality
extends to every profile in S^m. For a bounded continuous test function f,
the difference integral f dR_m(b)-integral f dpi is continuous and zero
pi^m-a.e. Every nonempty relatively open subset of S^m has positive pi^m
measure, so that difference vanishes everywhere. Bounded continuous functions
determine probability measures on a Polish space. This proves pointwise
constancy on the supported profiles, not on unsupported inputs outside S.

Without continuity the distinction matters. Let pi be uniform on [0,1],
set R_m=pi except on the profile (0,...,0), where R_m=delta_0 for m>=1.
The rule varies pointwise but all finite empty-start process laws are iid pi
under every order: almost surely no record equals zero, and all exceptional
profiles are null. The construction extends to a central scalar interval in
M2(C) and is covariant under algebra automorphisms. It does not furnish
positive-probability observable variation. An axiom's pointwise variation
wording cannot silently be replaced by an a.e. or continuity requirement.

## Why the two-site hypothesis matters

The endpoint condition K^2=Pi alone is insufficient. On three labels with
uniform pi, let u=(1,-1,0)^T, v=(1,1,-2)^T and

    K=Pi+(1/12) u v^T.

It is a positive stochastic matrix, has uniform invariant measure, and
K^2=Pi because v^T u=0 and both vectors have zero sum. But K is not Pi
and is not reversible. The two-site order identity fails. Thus no proof
may discard the two-site measure symmetry and infer K=Pi merely by taking
a square root of a nonsymmetric stochastic matrix.

## Scope of the model-pair application

The preceding full-algebra K_p has positive-probability variation on its
0/I support for every p>0. It therefore cannot be independent of every
supplied formation order. Its iid-priority mixture is nevertheless a
well-defined covariant law. Invariance of a random-order mixture is a
different requirement from equality of all conditional order laws.

This theorem identifies what an added order-independent sequential reading
would do on the declared slot-isotropic class. It neither selects that
reading nor equates a formation kernel with a static Gibbs conditional.
The kinetic-isotropy compatibility of the broader model-pair target remains
unresolved, and no axiom-update conclusion is asserted.


## A direction-sensitive escape, outside the common-K hypothesis

On a one-dimensional path, let each site's possibility label be two bits
(l,r). For each edge independently draw the adjacent ports (r_x,l_(x+1))
with joint probability [1+p(2r_x-1)(2l_(x+1)-1)]/4. Unpaired boundary
ports are independent fair bits. At formation, a target's left port uses
the conditional binary copy kernel of the recorded left neighbour's right
port when present, and otherwise is fair; the right port does the analogous
thing with the recorded right neighbour's left port. The two target ports
are conditionally independent. Every order generates exactly the same
product-over-edge joint law, since each edge's first port is fair and its
second port uses the matching conditional. The law varies for p>0.

Left and right one-neighbour kernels are adjoints, not one common reversible
K. Reflection exchanges the two ports and preserves the family. This is a
concrete escape from an overbroad arbitrary-kernel version of the theorem.
It is a supplied two-port alphabet on a path, not a full cubic M2-algebra
model; no embedding of six spatial ports or physical kinetic sector is
claimed. The four diagonal matrices diag(l,r) can display the path labels,
but doing that alone would not prove the full-domain/cubic extension.


## Author checks and negative-claim scope

The exact runner verifies the nonreversible positive three-label example,
its failed detailed balance and exact K^2=Pi identity. Reversible controls
have the predicted square residual lambda^2(I-Pi). The direction-sensitive
port construction passes all 384 order/configuration checks on a three-site
path, including its reflection that swaps ports. This preserves a concrete
escape rather than inferring arbitrary-kernel impossibility. The standard
Borel a.e. theorem and continuous supported-profile upgrade are analytic
proofs, not finite census extrapolations.

The scope and alternatives are recorded in BLOCK3_NO_GO_DISCIPLINE_CHECKLIST.md.
This conditional order theorem neither adopts a physical process reading
nor closes the intended full-foundation model-pair target.
