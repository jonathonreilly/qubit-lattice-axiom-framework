# Polynomial relaxation and a simultaneous volume/formation limit

2026-09-21. Root candidate derivation, awaiting exact controls and selective
independent reconstruction. This uses the supplied classical-key geometric
process and the general-graph two-vacancy construction. It does not add a
deletion event to the physical process. Established matching-chain and
monomer-correlation results are explicit external inputs, not new results
claimed here. No formal retained or audit status is asserted.

## Definitions and finite-graph statement

Let G be a connected simple graph on 2K vertices with a perfect matching,
K>=2. Write m=|E(G)|, P for its perfect matchings, Omega for its (K-1)-edge
matchings, n=|Omega|, Z=|P|, R=n/Z, and pi for uniform measure on Omega.
Let S be the continuous-time slide generator, with rate kappa>0 for each
legal replacement {b,c}->{a,b} when a is vacant. Additional symmetric
conservative transitions can be present; all estimates below continue to
hold because they add a nonnegative Dirichlet form. The state-space
connectivity proof is GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md.

Put L=-S and denote its smallest positive eigenvalue by g. The comparison
below gives

    C_K = 1+2K(K-1),
    g >= kappa/[256 m R^4 C_K].                         (1)

This bound is useful when R is polynomially bounded. It does not claim
polynomial mixing on arbitrary connected graphs, for which R may be
exponential. The singleton K=1 case needs no relaxation estimate.

## An auxiliary chain and its trace on the actual state space

Use the Broder chain on Omega union P only as a comparison object. In
continuous time it has rate kappa for each slide, each completion of a
vacant edge, and each deletion of an edge from a perfect matching. Its
uniform law is reversible. At a full matching F, its K neighbors are
F-e for e in F, and its next neighbor is uniform among them.

Erase the time spent in P. The resulting trace chain on Omega consists of
the original slides and, for every F, jumps F-e -> F-f at rate kappa/K
for e!=f. Self-return excursions contribute no off-diagonal transition.
If A is the near/full incidence matrix and H=diag(h), where h indicates
adjacent vacancies, the positive trace generator is the Schur complement

    L_trace = L_slide + kappa [H - A A^T/K].             (2)

Each near-perfect matching has at most one full completion, since its two
holes specify the only possible missing edge. Every column of A sums to K.
In particular, (2) has zero row sums, as a conservative generator should.

For g0:Omega->R, extend it harmonically to a full F by the average of its
values at the K parents F-e. If mu is uniform on Omega union P, the
Dirichlet energy of this extension is mu(Omega) times the trace energy,
while its variance is at least mu(Omega) Var_pi(g0), by conditional
variance. The Rayleigh principle therefore gives

    gap(trace) >= gap(Broder continuous time).            (3)

The trace is an analytic comparison, not an assertion that a record is
actually erased and later recreated with the same content.

## Route every extra trace jump through record-preserving slides

Fix F. Contract each of its K edges. Choose once and for all a simple path
in the connected contraction graph between every ordered pair e,f in F,
and choose a bridge edge of G for each step. As proved in the general-graph
note, two legal slides move the pair of vacancies from one missing F edge
to the next. This gives a path from F-e to F-f of length at most
D=2(K-1). No edge of the resulting slide path repeats: a micro-edge touches
one of the distinct parent states along a simple contraction path, and
each intermediate state identifies its two missing F edges and bridge.

For a fixed unoriented micro-edge in the slide graph, there are at most
two possible reference perfect matchings F whose routed paths use it.
Indeed, one endpoint of that micro-edge must be a parent F-e; completing
the two holes at either endpoint determines F uniquely. For a fixed F
there are at most K^2 ordered parent pairs. Consequently at most 2K^2
routed paths use any micro-edge. This deliberately loose bound suffices.

The original slide energy is

    E_slide(g0) = (kappa/n) sum_unoriented_slide_edges (Delta g0)^2.

The added trace energy is

    E_add(g0) = kappa/(2Kn)
                sum_F sum_(e,f in F) [g0(F-e)-g0(F-f)]^2.

Cauchy-Schwarz along each path, followed by the preceding congestion
count, gives

    E_add <= D K E_slide,
    E_trace <= C_K E_slide.

Thus gap(slides) >= gap(trace)/C_K. Extra symmetric moves only improve
this lower bound for the actual conservative generator.

## The imported Broder bound and its clock normalization

Jerrum and Sinclair, *Approximating the permanent* (1989), Theorem 3.6,
gives the conductance bound

    Phi >= 1/(16 m R^2)

for their lazy edge-proposal chain on P union Omega, on any graph with
a perfect matching. Their Section 3, pp.1156-1157, selects one graph edge
uniformly and adds a holding probability 1/2. Hence every nontrivial
transition probability is 1/(2m). With our rate convention its transition
matrix is I+B/(2m kappa), where B is the continuous-time Broder generator.
The reversible conductance inequality gap(discrete)>=Phi^2/2 then yields

    gap(Broder continuous time) >= kappa/(256 m R^4).

This proves (1) using (3) and the route comparison. The exact source is the
[author-hosted paper](https://people.eecs.berkeley.edu/~sinclair/perm.pdf),
DOI [10.1137/0218077](https://doi.org/10.1137/0218077), Theorems 2.2 and 3.6
and the stated transition convention. The theorem's general-graph scope,
factor16, squared counting ratio, and lazy factor1/2 were checked against
the primary text. Its established conductance theorem is imported; a
new independent reconstruction of the entire 1989 proof is not claimed.

## A uniform rare-killing estimate without an inverse-hazard penalty

The following argument applies to any irreducible symmetric conservative
chain on Omega with gap g and uniform pi. Let P_t=exp(tS), Pi project onto
constants, and

    A0 = integral_0^infinity (P_t-Pi) dt,
    T_G = (1+log n)/g.

Then A0 is the centered inverse of L and

    ||A0 f||_infinity <= T_G ||f||_infinity.             (4)

To verify the constant, the spectral estimate gives
2 TV(P_t(x,.),pi)<=min(2,sqrt(n-1) exp(-g t)). Split its integral at
(log n)/(2g): the first part is at most (log n)/g and the tail at most1/g.
This proves (4), including functions that are not centered initially.

Now let every adjacent vacant pair complete at rate beta, and let tau be
the remaining time to that birth. Put p=pi(h)=KZ/n and U for uniform
measure on P. For any subset D of perfect matchings, let
a_D(M)=h(M) 1_{completion(M) in D}. Then pi(a_D)=p U(D).
The exit probability u(M)=Pr_M(exit in D) satisfies

    (L+beta H)u=beta a_D,       0<=u<=1.

Write u=c+v, c=pi(u). The centered inverse identity gives

    v=beta A0(a_D-hu),       ||v||_infinity<=beta T_G.

The stationary equation is pi(hu)=p U(D), so
c-U(D)=-pi(hv)/p and |c-U(D)|<=||v||_infinity. The factor p cancels,
because h is nonnegative. Uniformly over every initial near-perfect state,

    TV(law(exit),U) <= min(1,2 beta T_G).                (5)

This estimate also holds from any initially nonfull matching: the earlier
finite-graph filling result gives almost-sure entry to the two-vacancy
level, and (5) is uniform over its possibly beta-dependent entrance law.
No equilibration or mixing estimate at lower pair counts is required for
this statement about the final geometry.

For lambda>=0 the joint transform
u_lambda(M)=E_M[exp(-lambda beta p tau) 1_{exit in D}] solves

    [L+beta(H+lambda p I)]u_lambda=beta a_D.

Repeating the argument, using 0<=u_lambda<=1, gives the explicit bound

    |u_lambda(M)-U(D)/(1+lambda)|
       <= beta T_G (1+lambda p) [1+1/(1+lambda)]
       <= 2 beta T_G (1+lambda).                       (6)

The remaining clock tau always starts at the two-vacancy entrance, even
when the full process starts empty. Equation(6) does not apply to the
entire empty-start duration by silently including its earlier stages.

Mean convergence is checked separately. Set z=beta p E_M[tau]. Its equation
is (L+beta H)z=beta p, with z>=0 and pi(hz)=p. For v=z-pi(z), (4) gives
||v||_infinity<=beta T_G ||z||_infinity, while
|pi(z)-1|<=||v||_infinity. Consequently, if 2 beta T_G<1,

    sup_M |beta p E_M[tau]-1|
           <= 2 beta T_G/(1-2 beta T_G).                (7)

These statements do not infer convergence of moments from weak convergence.

## Even cubic tori: a polynomial schedule

For the periodic d-dimensional cubic torus of even side N>=4, d>2,
K=N^d/2 and m=2dK. The counting identity in the clock note is

    R=K chi_N,
    chi_N=sum_(v odd) Z_N(0,v)/Z_N.

Taggi, [arXiv:1909.06558v3](https://arxiv.org/html/1909.06558v3), Eq.(2.5),
bounds each monomer ratio by1/(2d) under these torus hypotheses. Therefore
R<=K^2/(2d). Substituting in (1), and using C_K<=2K^2, yields

    g_N >= kappa d^3/(64 K^11).

Also n<=2^m since every matching is an edge subset. Thus a fully explicit
upper bound usable in (5)-(7) is

    T_G <= Tstar_N
        := 64 K^11 [1+2dK log2]/(kappa d^3).             (8)

In particular, any schedule with

    (beta_N/kappa) K^12 -> 0                            (9)

gives total-variation convergence of the completed geometry to the uniform
matching law as volume grows. It also gives an asymptotically exponential
last-pair clock beta_N p_N tau of mean1, factorized from the exit geometry
in the precise uniform-event Laplace sense of(6). For example,
beta_N=kappa K^(-12-delta), any delta>0, suffices. This is a conservative
sufficient schedule, not a necessary scaling law or a practical estimate
of relaxation. The exponent12 is an upper-bound artifact, not a critical
or measured exponent of the physical process.

Combining (7) with Taggi's Theorem2.1 lower bound and the clock note's
counting conversion gives the same positive lower and upper constants for
beta_N E[tau]/V as in the earlier ordered limit, now along schedules(9):

    [1-r_d/2]/(4d) <= liminf beta_N E[tau]/V
       <= limsup beta_N E[tau]/V <= 1/(4d).

Neither existence of a coefficient limit nor a total-growth-time upper
bound is asserted. The lower clock bound is imported only for d>2.

## What this closes and leaves open

This supplies a quantitative bridge from permanent local record motion to
a known equilibrium matching ensemble in a simultaneous large-volume and
slow-formation limit. It replaces an unspecified size-dependent choice of
beta by an explicit sufficient polynomial one, subject to the named
external results. The auxiliary deletion is eliminated from the actual
model by a proved comparison path; no physical erasure channel is assumed.

Total-variation convergence transfers bounded-observable distributions and
probability-one limiting events from the uniform ensemble. By itself it
does not transfer exponentially small probabilities, large-deviation rate
functions, or unbounded-moment estimates. The finite-beta experimental
limit is different. No fixed-beta mixing/selection claim, dipolar dimer
correlation theorem, Coulomb-phase theorem, propagating field dynamics,
unknown-qubit recognition mechanism or TOE identification is proved here.
