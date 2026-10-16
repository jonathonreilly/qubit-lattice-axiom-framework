# Which neighborhood changes survive in a loop?

Personal author: /root, 2026-10-16. Conditional exploratory mathematics.
This extends the independently checked block03 transport class. It supplies
candidate contextual laws and compares their consequences; it does not derive
the physical law or identify the neighborhood variables with measured fields.

## Target

The user's intermediate-specialization idea requires more than replacing an
endpoint label with another label. Determine which changes to local relations
are observable around a closed route, which cancel as endpoint conventions,
and which depend on an imported time or spatial correlation scale. Known
geometric phase and ordinary phase averaging are prior art. The new work here
is an explicit, checkable candidate comparison for this campaign, with no claim
that the mathematical constructions themselves are historically new.

## Transport through an arbitrary finite history

Let a_0,...,a_m be unit axes with adjacent axes non-antipodal. Write A_i=a_i.sigma
and U_i=U0(a_(i-1),a_i), as defined in block03. Give each edge a real twist
theta_i and let

    T_i = U_i exp[-i theta_i A_(i-1)/2].

Using U_i A_(i-1)=A_i U_i inductively gives

    T_m ... T_1 = (U_m ... U_1) exp[-i A_0 sum_i(theta_i)/2].

No commutation of unrelated axes is assumed. Every stabilizer twist is moved
through the preceding axis transports to the initial axis. If a_m=a_0, the
base product commutes with A_0, and its plus-eigenstate phase acquires the
additional angle -sum(theta_i)/2. These are amplitude phases, not event
probabilities. Coherent comparison and a readout law remain supplied.

For a fixed third axis n consider the two-parameter candidate

    theta(a,b;n)=lambda*n.(a-b)+kappa*n.(a cross b).

Both terms are continuous, simultaneously SO(3)-invariant and antisymmetric
under a<->b, so the transport remains exactly reciprocal with n held fixed.
The lambda term telescopes on a closed history. Indeed it is a frame change
G(b) U0(a,b) G(a)^dagger with G(a)=exp[i lambda*(n.a)*A/2]. The kappa term has
loop sum kappa*n.W, where W=sum_i(a_(i-1) cross a_i). It generally survives.
For the octant triangle W=x+y+z. Thus a neighbor-dependent edge change need
not produce a new loop observable; the loop separates endpoint conventions
from genuine extra transport within this candidate class.

If the edge context is n_i rather than a fixed n, the lambda terms need not
telescope. A true vertex-frame convention theta_i=f_(i-1)-f_i always telescopes,
even with changing vertex contexts. Assigning an independently changing context
to each edge is a different physical law, not merely a coordinate change.

## A resolved loop family

For N>=3 and 0<=beta<=pi, take

    a_j=(sin(beta)cos(2*pi*j/N), sin(beta)sin(2*pi*j/N), cos(beta)),
    j=0,...,N, with a_N=a_0.

Set Delta=2*pi/N. Adjacent dot products are
c=cos(beta)^2+sin(beta)^2*cos(Delta)>-1. Direct summation gives

    W=(0,0,N*sin(beta)^2*sin(Delta)).

Using the continuous choice of spinor
|a_j+>=(cos(beta/2), exp(i*j*Delta)sin(beta/2)) shows that the phase per shortest
transport is minus arg[w], where
w=cos(beta/2)^2+exp(i*Delta)sin(beta/2)^2. Since cos(Delta/2)>0,

    gamma_0 = -pi + N*atan(cos(beta)*tan(pi/N))  (modulo 2*pi).

The branch includes gamma_0=0 at beta=0 and -2*pi at beta=pi, the same physical
phase. The limiting geometric phase is -pi*(1-cos(beta)), as expected from
the known spin-half solid-angle formula. For n=z the extra twist tends to
-kappa*pi*sin(beta)^2. Its beta dependence differs from the geometric term,
although the leading small-beta terms alone can look like a rescaling. The
discrete edge law and its continuum limit are distinct declared constructions;
neither supplies a microscopic lattice spacing or physical update cadence.

## Context averaging makes correlation scale load-bearing

Set lambda=0 for the stochastic comparisons below. With changing edge contexts,
a nonzero lambda would contribute further terms and cannot be dropped as gauge.

Assume a third context n is uniformly distributed on S^2, independent of the
prepared amplitude state, and held fixed throughout each entire loop. This is
an ensemble assumption, not selection of an actual record/history. Its extra
phase factor averages to

    C_common = E exp[-i*kappa*n.W/2] = sinc(kappa*|W|/2),
    sinc(x)=sin(x)/x, sinc(0)=1.

The equality follows because n.W/|W| is uniform on [-1,1]. A negative real C
reverses the averaged fringe phase by pi; visibility is |C|. It must not be
silently treated as a positive attenuation at every kappa.

If instead independent uniform contexts n_i are assigned to every edge,

    C_independent = product_i sinc(kappa*|a_(i-1) cross a_i|/2).

For the resolved latitude loop all factors agree. At fixed kappa, N->infinity
gives C_independent->1, with

    log C_independent = -kappa^2*pi^2*sin(beta)^2/(6*N) + O(N^-3).

This is the asymptotic expansion in the eventual positive-factor regime for
fixed beta,kappa; it does not apply to arbitrary small N or near a sinc zero.
By contrast C_common->sinc(kappa*pi*sin(beta)^2), which is generally not one.
If kappa is changed with resolution as kappa_N=kappa0*sqrt(N), then

    C_independent -> exp[-kappa0^2*pi^2*sin(beta)^2/6].

That finite limit imports a particular noise scaling. It is not a dimensionful
scale or law derived from the lattice. Consequently an assertion that fresh
neighbor fluctuations automatically produce finite macroscopic decoherence
is false without a specified correlation or scaling rule.

More generally, zero-mean isotropic contexts with
E[n_i n_j^T]=C_ij*I/3 give the exact extra-phase variance

    Var(delta_gamma) = kappa^2/12 * sum_ij C_ij v_i.v_j,
    v_i=a_(i-1) cross a_i.

This is only a second moment. Covariance alone does not fix the characteristic
function, the visibility or a Gaussian law. A physical C_ij and the mapping
from edge index to measured length/time remain independent obligations.

## Slow context leaves a different record signature

For a coherent comparison phase alpha, suppose a loop's output fraction is

    p(n)=[1+cos(alpha-q*X)]/2,
    q=kappa*|W|/2, X=n.W/|W| uniform on [-1,1].

At W=0 the expressions use their continuous q=0 limit. If the explicit
uniform-reservoir detector from block04 is additionally adopted, independently
of the context sequence, the records are conditionally independent with these
fractions. Their common marginal mean and context variance are

    mu=[1+sinc(q)*cos(alpha)]/2,
    Var(p)={ [1+sinc(2*q)*cos(2*alpha)]/2
              -sinc(q)^2*cos(alpha)^2 }/4.

For a context frozen across L trials and resampled between runs,

    Cov(Z_i,Z_j)=Var(p), i!=j,
    Var(N0)=L*mu*(1-mu)+L*(L-1)*Var(p).

Here Z denotes the indicator of a click in output 0. Independent contexts on
each trial instead produce iid Bernoulli(mu) in this particular detector model,
with Var(N0)=L*mu*(1-mu). At alpha=pi/2, Var(p)=[1-sinc(2*q)]/8. Thus equal
average visibility can conceal very different time correlations. Slow
apparatus drift can also give such overdispersion; it is not unique evidence
of a new neighborhood mechanism. These equations are not assertions that the
published experiment used this context ensemble or this detector.

## An explicit neighborhood renewal law

To interpolate between frozen and fresh contexts, supply this Markov rule:
keep the preceding unit context with probability rho, otherwise replace it by
an independent uniform unit vector. Start with a uniform context. Then
C_ij=rho^|i-j|. This is a candidate environmental dynamics, not a consequence of
symmetry or of the framework's Record premise. It explicitly uses a probability
law and incoming context resource; the detector reservoir does not derive it.

For v_i=a_(i-1) cross a_i, define

    Phi(i,j)=sinc[(kappa/2)*|sum_(r=i)^j v_r|].

Let F_j be the average extra phase factor for the first j edges. Conditioning
on the start i of the final uninterrupted context segment yields the exact
finite recursion

    F_0=1,
    F_j=rho^(j-1)*Phi(1,j)
        +(1-rho)*sum_(i=2)^j rho^(j-i)*F_(i-1)*Phi(i,j), j>=1.

Earlier segments and the final renewed context are independent. The first
term is the event of no renewal. This O(N^2) recursion replaces a sum over
2^(N-1) renewal patterns. It gives the common-context result at rho=1 and the
independent-context product at rho=0, with the usual 0^0=1 convention in these
finite probability weights. It is a characteristic function and may be signed.

## A continuum limit with a declared correlation length

Now specify a continuously differentiable unit-axis curve a(s), 0<=s<=L,
with |a'(s)|<=M, and a context n(s) that renews at Poisson rate 1/ell to an
independent uniform unit vector, ell>0. Choose parameter step h=L/N and sample
n_i=n((i-1)h). Its exact discrete transition kernel has rho=exp(-h/ell): no
Poisson event retains the old context, while at least one event leaves the
last independent uniform mark. This is a particular refinement-consistent
model. The meaning and units of s, physical ell, and Poisson law are imports.

Compare the discrete and continuous phase twists

    delta_N=-(kappa/2)*sum_i n((i-1)h).(a((i-1)h) cross a(ih)),
    delta=-(kappa/2)*integral_0^L n(s).(a(s) cross a'(s)) ds.

They can be coupled using the same continuous context path. Over one interval,
the cross-product increment differs from integral a cross a' by at most
M^2*h^2/2: write a(ih)-a((i-1)h) as the integral of a' and use
|a(s)-a((i-1)h)|<=M*(s-(i-1)h). The expected context replacement contribution
is at most 2*M*integral_0^h t/ell dt=M*h^2/ell, since a context difference is
at most 2 and the probability of a renewal by elapsed time t is <=t/ell.
Summing, multiplying by |kappa|/2, and using |exp(ix)-exp(iy)|<=|x-y| gives

    |E exp(i delta_N)-E exp(i delta)|
       <= E|delta_N-delta|
       <= (|kappa|/2)*L*h*(M^2/2+M/ell).

This explicit error bound establishes convergence for the supplied Poisson
context model. It is not evidence that a real apparatus has Poisson contexts,
and it cannot determine ell from a lattice step chosen in code. Fixed rho while
refining h would shrink the physical correlation length and describe a different
family of environments. This distinction is the principal unresolved scale
assumption isolated by this block.

## What a useful observation protocol must resolve

Measure a full reference-phase fringe for each fixed orientation loop, with
separately checked source, detector and timing response. Vary path geometry
at fixed endpoints. When a third context has an independently specified
physical meaning, change it while preserving the path and apply a fixed-context
reversal echo. Record time sequences and vary the context switching rate.
The candidate distinguishes endpoint-gauge cancellation, path phase, and slow
versus fresh context by these measurements. Uncalibrated loss, spectral
averaging and ordinary dynamical phase are competing explanations.

The 1991 experiment's reported visibility is therefore not inserted as a bound
on kappa here: its actual n, correlation law, ordinary visibility budget and
measurement bridge have not been identified. A numerical fit without those
inputs would only supply the very assumptions the campaign is trying to derive.

No initial-state selection, physical scalar action, potential or absolute scale
is retired. The result isolates an explicit missing context correlation law
and shows why a phase assigned directly between endpoint labels cannot select
it. The primary geometric-phase and generalized-baker sources cited in blocks
03-04 remain prior art; the new calculations below are conditional controls,
not empirical tests or a claim of quantum mechanics being disproved.
