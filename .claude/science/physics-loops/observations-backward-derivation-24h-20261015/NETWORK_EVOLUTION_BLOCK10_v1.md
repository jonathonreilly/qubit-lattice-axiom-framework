# How many intermediate steps can an intervention reveal?

Personal author: /root, 2026-10-16. Status: conditional-support.
This extends the supplied finite linear network of block09. It derives an
observable short-time order from intermediate paths, rather than identifying
physical adjacency from an endpoint label. Matrix walk expansions and linear
response are established mathematics; no general new topology theorem is claimed.

## Exact response order within the declared candidate

Let K be a positive real symmetric stiffness matrix, e a unit coordinate at the
observed and driven node, and w the fixed direction of a calibrated intervention
Ktheta=K+theta*w*w^T, also positive. Initial data are zero and the input is an
ideal impulse at e. Denote by h0(t),htheta(t) the scalar displacement responses.
Define d as the smallest nonnegative integer for which

    mu_d = w^T K^d e != 0.

If no such integer exists, the observed Krylov space is orthogonal to w and the
intervention is invisible in this input/output channel for every time. A finite
matrix needs only its first dimension-many powers to decide that exact condition,
by its characteristic polynomial. This is a conditional algebraic statement,
not a stable numerical test from noisy data.

For finite d and nonzero theta, the rank-one identity of block09 and the Neumann
series R(z)=sum_(n>=0)(-1)^n K^n z^(-2n-2), at sufficiently large real z, give

    g0(z)-gtheta(z) = theta*mu_d^2*z^(-4d-4)+O(z^(-4d-6)).

Indeed e^T R w and w^T R e both first appear at order z^(-2d-2), their signs
square to one, and the denominator1+theta*w^T R w starts at one. Equivalently,
using the convergent impulse-response series

    hK(t)=sum_(n>=0)(-1)^n*(e^T K^n e)*t^(2n+1)/(2n+1)!,

all earlier difference coefficients vanish and

    h0(t)-htheta(t)=theta*mu_d^2*t^(4d+3)/(4d+3)!+O(t^(4d+5)).

This follows by matching the convergent resolvent series, or differentiating
finite-dimensional analytic response, not by an unqualified asymptotic inverse
Laplace transform. The result detects the degree of access to the changed
connection through this channel; it does not assign a microscopic coordinate
system or derive the network dynamics.

## When the algebraic order is graph distance

For a connected positive-spring graph, K has off-diagonal entries -k_ij<0 on
edges and zero otherwise, with positive grounding sufficient for K>0. For an
edge w=e_i-e_j, let d_i,d_j be distances from the observed vertex to its ends.
Below min(d_i,d_j), the corresponding matrix powers vanish: a walk cannot
traverse the graph in fewer steps. If d_i<d_j, the first contributing walks all
reach i at d_i and contain no diagonal stay or detour; their weights share sign
(-1)^d_i and are strictly positive in magnitude. Thus mu_d is nonzero at d=d_i.
The analogous claim holds when j is nearer. If the endpoints have equal distance,
their two weighted sums can cancel; graph distance alone then does not fix d.

On a bipartite graph, the distances to the ends of an edge have opposite parity
and differ by at most one, so they differ by exactly one. Hence the cancellation
case is absent for this single-edge perturbation with positive springs. A finite
connected subgraph of the cubic nearest-neighbor graph is an example, but the
classical spring action and readout remain extra premises beyond repo adjacency.
For edge distance d=0,1,2 the earliest response difference is respectively
order t^3,t^7,t^11. These are orders of small amplitudes, not hard propagation
delays. The continuous-time finite oscillator model has analytic tails and does
not by itself establish a relativistic light cone.

## A finite-time remainder certificate

Let M=max(||K||_2,||Ktheta||_2)>0. With m=2d+2, the first omitted term has degree
2m+1=4d+5. Each matrix moment difference is at most2 M^n. Therefore for real t

    |h0(t)-htheta(t)-theta*mu_d^2*t^(4d+3)/(4d+3)!|
      <= 2*M^(2d+2)*|t|^(4d+5)/(4d+5)! * cosh(sqrt(M)*|t|).

The bound follows by summing absolute Taylor terms and using
(4d+5+2r)! >= (4d+5)!*(2r)!. It is conservative but valid for all finite t under
the fixed matrices. It supplies no apparatus error certificate, impulse
bandwidth, minimum detectable signal or derivative estimate. Those must be
separately calibrated before inferring d from observations.

## Useful falsification and remaining ambiguity

The chain/triangle pair in block09 has identical original boundary response.
Applying the same physically labeled hidden-edge direction w=(0,1,-1) changes
the leading coefficient: in the chain mu1=-1; in the rotated network mu1=1/5.
Their intervention responses thus differ by a factor25 at the leading order,
even though their unperturbed endpoint responses agree exactly. If instead w
is also rotated by O, the equivalence persists: physical identification of the
intervention is precisely the extra information doing the work.

This gives a concrete observations-backward route: calibrated perturbations at
intermediate locations can constrain accessible path depth and distinguish
some networks hidden by endpoint equivalence. It does not prove that the actual
world is such a network, select its action, or remove the need for a physical
measurement map. Time-varying/adaptive K, nonlinear responses, unknown masses
and unmeasured channels require a new derivation of the response contract;
choosing their dynamics after seeing a discrepancy would be model development.
