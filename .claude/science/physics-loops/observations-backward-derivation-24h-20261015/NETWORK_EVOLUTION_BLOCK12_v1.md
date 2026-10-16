# A matched-phase loop test for an explicitly contextual neighborhood connection

This is root's personal development proposal, not an empirical result or a new
quantum law. It sharpens the earlier contextual-connection candidate into two
finite paths whose ordinary transport agrees but whose extra context response
differs. The pair-relative transport and all physical orientation/control
identifications remain supplied. Geometric phase itself is established physics.

## Candidate and finite geometry

For unit orientations a,b with a.b>-1, put A=a.sigma, B=b.sigma and
U0(b,a)=(I+B*A)/sqrt(2*(1+a.b)). Take the explicitly chosen alternative

    U(b,a;n)=U0(b,a)*exp[-i*kappa*n.(a cross b)*A/2].

The context vector n and coupling kappa are fixed during each entire compared
path. This is a testable extra contextual twist, not a derivation of n, kappa,
or the pair-only reference law. At every step U0 carries the current A to B.
Consequently, along a closed path based at anchor az, all extra twists transport
to the same anchor generator and add. The extra eigenphase is

    delta_gamma=-kappa*n.W/2,   W=sum_edges(a cross b).

For an N-vertex latitude loop a_j=(sin(beta)cos(2pi*j/N),
sin(beta)sin(2pi*j/N),cos(beta)), traversed in that order, with N>=3 and
0<beta<pi/2,

    gamma(beta,N)=-pi+N*atan(cos(beta)*tan(pi/N)),
    W(beta,N)=N*sin(beta)^2*sin(2pi/N)*z.

Here gamma is the eigenphase on the transported positive spinor, with the
continuous branch gamma->0 as beta->0. It follows by multiplying the repeated
step in a frame rotating by2pi/N, or by the finite polygon solid angle. The
primary control multiplies the actual two-by-two matrices. The W formula is
the direct cross-product sum, whose transverse terms telescope by rotational
symmetry. Connect the anchor z to the first latitude point and return along
the reversed connector; this conjugates the loop to the common anchor and
adds zero to W. Connectors must avoid antipodal endpoints.

## Two paths with equal reference phase and unequal context response

Choose betaA in(0,pi/2), N>=3. Let gammaA=gamma(betaA,N), and define

    cos(betaB)=tan((pi+gammaA/2)/N)/tan(pi/N).

The right side lies between cos(betaA) and1, so0<betaB<betaA<pi/2,
and gamma(betaB,N)=gammaA/2 on the same branch.

PathA is the betaA loop with its out-and-back connectors. PathB consists of
two betaB loops, each brought to the same anchor by its own connector: the
first around+z, the second obtained by a proper pi rotation about x, hence
around-z. Both loops have the same signed reference eigenphase gammaA/2.
Their W vectors are equal and opposite; each connector pair cancels exactly.
At the anchor both reference matrices commute with az.sigma and have determinant
one, so equal eigenphases imply the full matrices agree, not just one intensity.

    U0(PathA)=U0(PathB),
    W_A=N*sin(betaA)^2*sin(2pi/N)*z,   W_B=0,
    gamma_context(A)-gamma_context(B)=-kappa*n_z*|W_A|/2.

Thus this specific contextual candidate predicts a relative phase despite
equal ordinary transport. Reversing either path changes its signed phase, so
the acquisition must track that convention. The equality says nothing about
real hardware loss, dynamical phase, pulse timing or uncontrolled environment;
those are calibration obligations. If n changes during the path, the cancelled
sum is replaced by edge-weighted contexts and the exact cancellation is lost.
That is a different candidate requiring a specified correlation law, not an
adjustment to make a discrepancy disappear.

## What could be constrained without an assumed orientation ensemble

No distribution of n is required for the deterministic relative phase above.
If a matched-phase experiment bounds its extra phase by eps after known
instrument/systematic errors, within a specified unwrapped small-phase interval,
then |kappa*n_z|<=2*eps/|W_A|. Rotate the complete two-path construction by
three known orthogonal proper rotations. If the same n is fixed across all
three comparisons and their phase bounds are eps_i with geometric coefficients
W_i>0, then

    |kappa*n| <= 2*sqrt(sum_i (eps_i/W_i)^2).

The unwrapping qualification is essential: a phase observed only modulo2pi
permits aliases; a single null result alone cannot bound an arbitrarily large
coupling. A controlled continuous amplitude sweep or independent prior range
is additional input needed to remove those aliases. Context stability across
the comparisons and independent geometric/phase calibration are also premises.

If instead n is supplied as an isotropic unit vector freshly sampled between
whole paths, the mean extra coherence forA is sinc(kappa*|W_A|/2), whileB has
unit extra coherence. This is a conditional ensemble prediction; it does not
derive that ensemble. A conventional quantum system with an appropriate
environmental interaction can also acquire such a context-dependent phase.
The test diagnoses a missing interaction relative to the specified reference,
not failure of quantum mechanics as a whole.

## Observation protocol and remaining obligations

Before opening a new dataset: identify a physical orientation transport,
calibrate its ordinary full transformation and systematic differences between
the two paths, specify a bounded context-stability interval, chooseN/beta and
phase-unwrapping rule, then freeze which paths estimate parameters and which
are reserved tests. Interleave path orders and track preparation/measurement
history. A calibration fit is development data; reserve additional loop shapes
or axes before calling any comparison independent.

The earlier Kwiat/Chiao geometric-phase/anticoincidence paper motivates the
joint phase-and-record obligation; its published summary is already exposed.
No new optical data have been acquired here. The concrete gain is a pair of
finite histories with the same reference transformation and an exact candidate
context discriminator. The hard gap remains deriving or empirically identifying
the contextual interaction, coupling, state and control map. The chosen twist
is challenged by this test rather than counted as an eliminated assumption.
