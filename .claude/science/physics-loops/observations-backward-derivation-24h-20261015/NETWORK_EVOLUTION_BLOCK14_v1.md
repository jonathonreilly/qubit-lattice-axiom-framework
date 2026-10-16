# Conditioning and finite-error bounds for the matched-path context test

Root's personal conditional continuation of the matched-phase construction.
This derives finite tolerances and removes its nearly antipodal connector from
one implementable geometry. It supplies no actual instrument accuracy, physical
context source or empirical result. The contextual law remains an explicit
candidate; its coupling and dynamics have not been selected by observations.

## Replace the direct connector without changing the ideal discriminator

Use N>=4 and0<beta<pi/2. Connect the anchor z to the first point of each north
or rotated-south latitude loop through x=(1,0,0), then return along the exact
reverse connector. Every connector dot product is nonnegative. Consecutive
latitude points also have dot product cos²(beta)+sin²(beta)cos(2pi/N)>=0.
Thus every nominal edge has1+a.b>=1. This stays away from the antipodal
singularity even as beta approaches zero, unlike the original direct south
connector. The latitude phase is unchanged by connector conjugation; its
out-and-back contribution to W cancels. The same two-loop comparison and
candidate relative phase therefore hold exactly.

This is a constructive control-path improvement, not a claim that the physical
controls, their timing or their errors can be freely chosen. N=3 is outside
this convenient uniform-gap construction but remains allowed in the earlier
ideal theorem.

## Pair transport sensitivity without a stochastic noise model

Let nominal and perturbed unit orientations obey |a'-a|<=ea, |b'-b|<=eb.
For the pair transport U0=(I+B*A)/d with d=sqrt(2(1+a.b)), writeN=I+B*A.
Pauli norms give||N'-N||<=ea+eb. BecauseN=d*U0,||N||=d; the reverse norm
inequality yields|d'-d|<=||N'-N||. If both edges obey1+a.b>=eta>0, then

    ||U0'-U0|| <= sqrt(2)*(ea+eb)/sqrt(eta).

Indeed subtractN'/d'-N/d and use d'>=sqrt(2eta) in both terms. For products
of unitary steps, a telescoping sum gives the total operator error

    S_path <= sum_edges sqrt(2)*(ea+eb)/sqrt(eta_edge).

There is no exponential product amplification. If nominal gaps are at least1
and all vertex errors are at mostdelta<1/2, both actual and nominal gaps are
at least1-2delta. PathA hasN+4 edges and pathB has2(N+4), so these counts
give a simple conservative certificate. Shared/repeated vertex errors may be
correlated; the deterministic bound remains valid.

For a nominal return amplitude of modulus one and a perturbation bounded by
S<1, its actual overlap lies in a radiusS disk centered at the nominal complex
amplitude. The tangent from the origin gives a principal phase error at most
arcsin(S). Therefore the difference of the two measured reference phases has
error at mostarcsin(S_A)+arcsin(S_B), before adding actual readout errors.
This is a deterministic small-phase certificate, not a statistical interval.
For exactly closed anchor paths a tighter unitary eigenphase bound is possible;
the disk bound is sufficient here. If S>=1 it provides no useful phase bound.

## Explicit context drift and geometry error

For the chosen twist, arbitrary edge-dependent contexts still give the extra
closed-path phase -kappa*sum(n_edge.(a cross b))/2. If||n_edge-n0||<=delta_n,
the departure from the fixed-context prediction obeys

    |delta_gamma_drift| <= |kappa|*delta_n/2 * sum_edges||a cross b||.

No sampling distribution is needed. The paired-loop cancellation requires
delta_n=0; a measured or stipulated bound permits a finite error instead.
If the actual unit orientations are perturbed, cross-product subtraction gives
||W'-W||<=sum_edges(ea+eb). For a fixed context of norm at mostN_context,
the predicted extra phase therefore changes by at most

    |kappa|*N_context/2 * sum_edges(ea+eb).

For a full two-path comparison sum the two path bounds. Use the actual cross
length or a justified upper bound in the drift term. Combining this with the
reference-transport phase bound is valid when both actual paths use the same
identified anchor/preparation/readout and the accumulated phase remains in the
specified unwrapped interval. Instrument phase error, finite controls and
preparation drift are separate terms; none is estimated from the synthetic
controls here. Unknown kappa or context magnitude needs its own bound for a
numerical prediction interval. That requirement cannot be omitted by fitting
the candidate to the same observations used to test it.

## A planning calculation, not an instrument specification

For N=16, betaA=pi/3 anddelta=1e-5 on every vertex, the conservative pair-only
phase-error bound is computed directly by the runner. The nominal geometric
coefficient isW_A=16*(3/4)*sin(pi/8). These dimensionless values are selected
synthetic planning inputs. No claim is made that an existing apparatus achieves
this tolerance, or that a particular kappa/context is physically realized.

The next empirical step is to characterize those actual controls and reserve
the two-path comparisons before opening data. The useful derived result is a
well-conditioned finite path and deterministic tolerance accounting; the
physical source of the additional contextual interaction remains open.
