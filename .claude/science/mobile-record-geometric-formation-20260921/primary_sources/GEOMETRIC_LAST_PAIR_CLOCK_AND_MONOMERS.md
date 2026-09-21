# The final-pair formation clock and equilibrium monomer correlations

2026-09-21. Root conditional derivation, pending selective independent check.
The process, classical antipodal-key resource, graph hypotheses and finite
volume rate limit are those in GEOMETRIC_PARTNER_RECORD_FORMATION.md and
GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md. This note concerns the elapsed
time between first reaching two vacancies and filling, not the whole growth
time from empty. An existing equilibrium theorem is imported explicitly;
it is not rederived or presented as a new result about dimers.

## A finite-state clock law, including its exit state

Let Omega be the near-perfect geometric matchings on a finite connected
regular bipartite simple graph with 2K vertices. The slide generator S is
irreducible and symmetric; kappa>0 is fixed, and fixed additional symmetric
conservative rates are allowed. Let pi be uniform on Omega. Write h(M)=1
when the two vacant vertices are adjacent and 0 otherwise, H=diag(h), and
p=pi(h)>0. For each full matching F, a_F(M) indicates that the unique birth
at M completes F. Put tau for this next-birth waiting time.

For s>=0, the joint Laplace transform

    u_(beta,s,F)(M)=E_M[exp(-s beta tau) 1_(exit=F)]

solves

    [-S+beta(H+sI)] u_(beta,s,F)=beta a_F.              (1)

The bounded vector u takes values in [0,1]. Along any beta->0 sequence, every
convergent subsequence solves S u_0=0, hence is constant, by irreducibility.
Multiply (1) by pi before taking the limit to obtain

    u_(beta,s,F)(M) -> pi(a_F)/(p+s)
                     = (1/|Fset|) p/(p+s).             (2)

Here pi(a_F)=K/|Omega| and p=K|Fset|/|Omega| by the edge-deletion count.
The convergence is uniform in M because Omega is finite. Thus beta tau
converges in law to an exponential variable of rate p, and the full matching
converges jointly to an independent uniform member of Fset. This holds for
an entrance distribution at the two-vacancy level that itself depends on
beta. It does not posit equilibration at earlier pair counts.

## Mean waiting time: do not infer moments from weak convergence alone

Let L=-S, let P project onto constant functions in L2(pi), and Q=I-P.
For |Omega|>1, L restricted to the centered subspace has strictly positive
smallest eigenvalue. Define the centered inverse

    R_beta = [Q L Q + beta Q H Q]^{-1} on ran Q,
    q=h-p 1,    C_beta=<q,R_beta q>_pi.

R_beta stays bounded as beta decreases to zero. The unique mean hitting
time t_beta solves (L+beta H)t_beta=1. Decompose t_beta=c 1+v, pi(v)=0.
The centered and constant equations give exactly

    v=-beta c R_beta q,
    c=1/[beta(p-beta C_beta)],
    t_beta(M)=[1-beta(R_beta q)(M)]
                   /[beta(p-beta C_beta)].              (3)

The denominator is positive: L+beta H is positive definite, and its Schur
complement on constants is beta(p-beta C_beta)>0. Consequently, at each
fixed graph,

    beta E_M tau -> 1/p=|Omega|/[K |Fset|],             (4)

uniformly over starts. This proves mean convergence separately. A one-state
near-perfect chain has h=1 and the assertion is directly exponential; no
centered spectral gap is needed in that case. Since C_beta>=0, the mean
from pi is at least 1/(beta p); finite-rate persistence of the local birth
hazard increases that stationary-start mean. No such one-sided bound for
every individual start is asserted.

The O(1) correction at fixed graph can also be read from (3): with R_0 the
centered inverse of L and C_0=<q,R_0 q>,

    E_M tau=1/(beta p)+C_0/p^2-(R_0 q)(M)/p+O(beta).   (5)

The constants in this expansion may deteriorate with volume. In particular,
beta_N->0 on a sequence of growing systems is not enough without control
of the relevant conservative relaxation. None of (2)--(5) supplies that
control for cubic tori.

## The counting ratio is exactly a monomer susceptibility

Now specialize to the even periodic d-dimensional cubic torus of side N>=4,
volume V=N^d and K=V/2. Let Z_N be its number of full matchings, and let
Z_N(u,v) count matchings with precisely u and v vacant, where u,v lie on
opposite bipartite sublattices. Define

    Xi_N(v)=Z_N(0,v)/Z_N,
    chi_N=sum_(v odd) Xi_N(v).

Counting a near-perfect matching once by its unique pair of vacant vertices,
then using translation invariance, gives

    |Omega|=K Z_N chi_N,
    p_N=1/chi_N,
    lim_(beta->0) beta E_M tau=chi_N.                  (6)

Every neighbor has Xi_N(e_i)=1/(2d): adding the missing edge bijects its
two-vacancy matchings with full matchings containing that edge, whose
uniform occupation probability is1/(2d). There are 2d such neighbors, so
the adjacent-pair weight in the sum is exactly 1, consistent with p_N=1/chi_N.
This identifies the leading formation clock with a precise equilibrium
counting observable; it does not assume a continuum effective action.

## Explicit external input in dimensions greater than two

Use Lorenzo Taggi, [arXiv:1909.06558v3](https://arxiv.org/html/1909.06558v3),
Theorem 2.1, Eq. (2.3), and the bound Eq. (2.5). His even periodic torus and
unweighted monomer counting ratio coincide with the definitions above.
Writing r_d for the expected number of strictly positive-time returns of
simple random walk on Z^d, these results give, for d>2,

    liminf_(N even->infinity) (1/K) chi_N
                 >= [1-r_d/2]/(2d),
    Xi_N(v)<=1/(2d).                                  (7)

For d=3, the paper records 0.51<r_3<0.52, so the lower constant is positive.
The theorem also bounds insertion ratios away from zero at odd axis
separations up to an N-proportional distance (Eq. (2.4)), with the stated
margin and sufficiently large even N. This is an equilibrium monomer
nonconfinement statement; it is not a dipolar dimer-correlation, Gaussian
field, dynamical mixing or photon theorem.

Combining the exact counting identity (6) with (7) yields the conditional
formation consequence

    [1-r_d/2]/(4d)
       <=liminf_(N even->infinity) chi_N/V
       <=limsup_(N even->infinity) chi_N/V
       <=1/(4d).                                      (8)

In particular, in 3D the mean final-pair time has a coefficient between
[1-r_3/2]/12 and1/12 when beta tends to zero first and time is measured in
units V/beta. This is an ordered-limit bound, not a fitted numerical value
for a fixed positive beta. It makes no claim that chi_N/V has a limit.
The full growth time is at least the last-pair time, but(8) is not an upper
bound for the complete empty-start growth process.

For the normalized two-vacancy equilibrium law, conditional on one vacancy
being at0, the other vacancy has probability Xi_N(v)/chi_N at odd v. Equation
(7) therefore also connects the late formation stage to spatially separated
vacancies. This conditional equilibrium law is the conservative near-perfect
law; it is not claimed to hold at every instant of a finite-rate trajectory.

## Scientific scope

The permanent-record process now has a controlled route to uniform full
geometries and a quantitative late formation law tied to a rigorously studied
constrained ensemble. The exact geometric divergence charges are vacancies,
and births remove them in opposite-sublattice pairs. None of this identifies
them as physical electric charges, supplies the missing exact-content
recognition operation on unknown qubits, or gives transverse propagation.
The fixed-rate large-volume screen tests a different order of limits and
must remain labeled numerical. No inference from its apparent infrared
power to the hypotheses or conclusions of Taggi's theorem is used here.
