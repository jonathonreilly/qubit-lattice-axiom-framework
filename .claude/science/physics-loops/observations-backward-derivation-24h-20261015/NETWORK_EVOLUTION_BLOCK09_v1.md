# Hidden-neighbor memory and an intervention test of a common network

Personal author: /root, 2026-10-16. Status: conditional-support.
This is a constructive response to the user's intermediate-neighborhood idea.
It does not derive a quantum or scalar action. Finite linear elimination and
rank-one resolvent algebra are established mathematics, reconstructed here.
The useful proposed interface is a calibrated cross-environment intervention
with a division-free uncertainty test, rather than an independent fit per setting.

## Explicit candidate and observation contract

Assume a finite real network with unit kinetic matrix, time-independent positive
symmetric stiffness K, action L=(dot Q.dot Q-Q.K.Q)/2+f b.Q, and calibrated
linear readout c.Q. Unit kinetic normalization, finite linear dynamics, source,
readout, initial preparation and physical coordinates are supplied. They are
not derived from repo Records, a lattice or the measured scalar theory.
Positive graph springs and ground springs form a subclass. A graph may be a
physical candidate only after its sites and edges are independently identified.

An observed impulse response or transfer function measures a relation between
specified input/output channels. It need not expose every intermediate node.
The equations below give constraints for that declared experimental contract;
no new dataset, response spectrum or independent empirical test is supplied.

## Eliminating a neighborhood produces memory and initial-state forcing

Split Q=(q,x), K=[[a,b^T],[b,C]], with scalar observed q and C positive. Write

    q''+a*q+b^T*x=f,
    x''+C*x+b*q=0.

Duhamel's formula gives, for t>=0,

    x_h(t)=cos(sqrt(C)t)x0+C^(-1/2)sin(sqrt(C)t)v0,
    x(t)=x_h(t)-integral_0^t C^(-1/2)sin(sqrt(C)(t-s))b*q(s) ds.

Differentiating verifies the hidden equation and its two initial conditions.
Thus the exact observed equation is

    q''+a*q-integral_0^t M(t-s)q(s) ds=f-b^T*x_h(t),
    M(t)=b^T*C^(-1/2)sin(sqrt(C)t)*b.

The minus sign is fixed by elimination. No stochastic noise assumption was
needed: unknown initial neighbors give an unknown forcing function. Declaring
that forcing thermal, white, independent, stationary or zero adds information.
For zero initial data and Laplace z in the right half-plane,

    chi(z)=1/[z^2+a-b^T(z^2 I+C)^(-1)b].

Diagonalizing C makes the self-energy a sum of nonnegative modal weights over
z^2+omega_j^2. A fitted memory law therefore has a specific admissibility class
under this candidate. The Schur condition a>b^T C^(-1)b ensures positivity of
the full stiffness. The apparent temporal nonlocality disappears when x is
retained, but this is ordinary coarse-grained dynamics, not a replacement for
quantum interference. Projection-induced memory is known prior art; see
[Mori1965](https://doi.org/10.1143/PTP.33.423), whose abstract was consulted.
No theorem or fluctuation-dissipation premise from that article is imported.

## Even a complete endpoint response need not identify physical adjacency

Take K=[[4,-1,0],[-1,5,-1],[0,-1,6]], observe/force e0, and let O fix e0 while
rotating the two hidden coordinates by [[3/5,-4/5],[4/5,3/5]]. Then K'=O K O^T
has exactly the same e0^T(z^2 I+K)^(-1)e0 for every invertible z.
K is a chain; K' has all three nonzero negative pair off-diagonals. Both have
positive row sums and are realizable as positive springs plus positive ground
springs with unit masses. They differ in adjacency in their declared nodal
coordinates yet have identical measured boundary response. The proof is direct
orthogonal similarity with Oe0=e0. No numerical spectral fit is involved.

An effective chain or a count of observable normal modes can be useful without
being a reconstruction of microscopic adjacency. Extra channels, known spatial
coordinates, source access or controlled interior interventions can break some
of this ambiguity. We do not claim all such information is insufficient.

## A common interior intervention gives a stronger observable constraint

Now restore arbitrary input b and readout c. At fixed z let A=z^2 I+K0 and
R=A^(-1). Suppose the ONLY change across environments is a calibrated stiffness
term theta*w*w^T, with fixed known direction w. For a single spring between
nodes i,j, w=e_i-e_j and the added potential is theta*(Q_i-Q_j)^2/2.
The same source, readout, background and linear response definition must hold.
Require A and A+theta*w*w^T invertible; stability also requires an admissible
Ktheta if interpreted dynamically. Define

    gtheta=c^T(A+theta*w*w^T)^(-1)b,
    Delta(theta)=g0-gtheta,
    H=(c^T R w)(w^T R b), J=w^T R w.

Multiplication by A+theta*w*w^T verifies the standard rank-one inverse formula
and gives

    Delta(theta)=theta*H/(1+theta*J).

This uses transpose bilinear products even for complex z, not Hermitian norms.
No positivity of H is asserted for different source/readout channels. This is
established Sherman-Morrison algebra, not a novel identity. The relation holds
for the full response, without isolating one mode or discarding a background.
For nonzero theta and H, theta/Delta(theta)=1/H+theta*J/H is affine in theta.
For any three calibrated theta1,theta2,theta3 the division-free necessary test is

    Rtest = theta2*(theta3-theta1)*Delta1*Delta3
          - theta3*(theta2-theta1)*Delta1*Delta2
          + theta1*(theta2-theta3)*Delta2*Delta3 = 0.

This polynomial remains true at blind channels H=0, including Delta=0, where
it carries no identifying power. Distinct nonzero settings are needed for a
useful test; near-zero responses make the divided version unstable. Passing
this test is necessary within the contract, not sufficient to prove a rank-one
physical intervention: invisible additional changes and special degeneracies
can also pass. A generic rank-two perturbation can fail it, as the controls show.
If theta or the background/readout is freely refitted for each environment, the
cross-environment claim has changed and this test loses its intended force.

## Deterministic measurement-error certificate

Let measured complex differences be d_i, with certified |Delta_i-d_i|<=epsilon_i.
For each product define

    B_ij=epsilon_i*|d_j|+epsilon_j*|d_i|+epsilon_i*epsilon_j.

Triangle inequality gives |Delta_i Delta_j-d_i d_j|<=B_ij, hence

    |Rtest(d)| <= |theta2*(theta3-theta1)| B_13
                 + |theta3*(theta2-theta1)| B_12
                 + |theta1*(theta2-theta3)| B_23

under the model. The differences share a baseline measurement; this deterministic
bound permits arbitrary correlated errors. It assumes exact or independently
certified theta values; errors in theta require extra terms. It does not infer
error bars from data or turn an error certificate into a statistical confidence
statement. A violation beyond valid errors rejects this specific common-response
contract; it does not by itself identify which physical premise failed.

## What can actually be pursued

The intermediate-connection hypothesis yields a research protocol: identify
input/readout physically, characterize preparation and memory, calibrate one
local coupling perturbation, then compare several settings using one shared
response model and a reserved test setting. Calibration/development settings
must be labeled before independent tests. We have derived an observable
constraint of a candidate, not its action, scale, initial state or measurement
identification. No existing endpoint-only scalar reconstruction supplies these
missing intervention premises. The useful next step is an actual fixed-action
response calculation with justified source/environment/readout, rather than
calling an adjustable network or a fitted memory kernel a derivation.
