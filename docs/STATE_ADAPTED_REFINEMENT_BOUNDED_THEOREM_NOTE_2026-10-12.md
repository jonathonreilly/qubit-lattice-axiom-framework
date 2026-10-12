---
claim_id: state_adapted_refinement_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_type_reason: "Conditional analytic theorem in the supplied free-chain model; finite diagnostics and arithmetic repair are supporting evidence."
claim_scope: "For the supplied massive free one-dimensional chain, Bogoliubov-conjugated even refinements preserve the chosen state exactly and have the same intrinsic Cauchy sections, geometric local quotient and actual fixed mixed-flow limits as Haar refinement."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - continuum_local_boost_bounded_theorem_note_2026-10-12
  - microscopic_local_boost_limit_bounded_theorem_note_2026-10-12
  - mixed_local_poincare_correlations_bounded_theorem_note_2026-10-12
  - dyadic_even_refinement_bounded_theorem_note_2026-10-12
runner: scripts/state_adapted_refinement_2026_10_12.py
artifact_role: theorem
target_claim_id: null
target_blocker_text: "Compatibility of exact selected-state refinement with intrinsic geometric sections and actual mixed-flow limits."
source_of_blocker_text: user_goal
next_trace_action: "Use the proved section-level equivalence while retaining finite-scale locality and energy witnesses; no broader physical realization is claimed."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "State-adapted even-spin inductive limit with unchanged geometric Cauchy sections and actual mixed-flow limits, conditional on pinned supplied-chain parents"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem


**Publication chronology:** The scientific source below is frozen at SHA-256 `459868fcd7f80fa3063c9e7f7a6d62df393eb80f2edc72b221ecda533ba2a971`. The later fresh source review and root source-bound verification accepted the frozen theorem and narrow arithmetic repair at this bounded scope. Original pending-review and 85/86 author-result statements remain historical records. The separately corrected helper is not a rewrite of the original run.


# State-adapted refinement and the same geometric continuum limit

**Author probe, 2026-10-12.** Conjugating the Haar refinement by the
supplied chain's actual Bogoliubov automorphisms gives exact selected-state
compatibility. Its compatible continuum embedding has a strong geometric
limit. In fact its intrinsic Cauchy sections are exactly the original
Haar Cauchy sections, with the same limit evaluation. This preserves the
geometric local section quotient and the actual mixed-flow limits.

These statements do not make the finite-scale maps local or dynamically
compatible. The image of a single Z operator has infinite support for
every positive spacing. An explicit even observable also witnesses
failure of exact energy-flow intertwining. Fixed-spacing exponential
coefficient tails and convergence of fixed observables are proved below;
no uniform physical tail constant or operator-norm convergence on all
observables is asserted.

## 1. Scope, pinned premises and prior art

Let S be the directory containing this note, and E=S/state_adapted_refinement.
The source copies and hashes in E/source_inventory.json are the authority
for this conditional calculation. The exact parents are:

| Parent | SHA-256 | Imported content |
|---|---|---|
| DYADIC_EVEN_REFINEMENT_PROBE.md | 646ad05eb2f3ba02b6410e4043a4f258ca84ea2c15b92a4ca7d0ab25e05ecc9c | Even Haar maps, cell embeddings, inductive limit, intrinsic sections, and section 11 candidate |
| LOCAL_EVEN_CONTINUUM_PROBE.md | 7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b | Actual chosen covariance, coefficient action of beta, strong covariance limit |
| CONTINUUM_LOCAL_BOOST_REVISED_PROBE.md | 59d34a51720446a554c41ec070c0b52b6dde67692c72b4c42a4937f7f4ca9d16 | Closed real continuum boost and geometric spacetime net |
| MICROSCOPIC_LOCAL_BOOST_LIMIT_PROBE.md | 70118e0b1f7fd4fa9d041ce837f967abdd0e2f682a854d38885466fd6e4b125d | Identification with actual spin scaled boost, closed domains and strong comparison |
| MIXED_LOCAL_POINCARE_CORRELATIONS_PROBE.md | 8c3a308b57a2e53d117a7c76046b4995c3a2ffc150e31cb142a90bd926796418 | Compact-parameter strong convergence of each fixed mixed word |
| CONCRETE_GAPPED_CHAIN_PROBE.md | 0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd | Supplied Hamiltonian, beta as an actual spin automorphism, selected state and actual flows |

The dyadic parent is still provisional at dispatch: fresh review is being
sealed by root, and root's final acceptance has not been supplied here.
This note does not convert that dependency into retained authority.
The pending LOCAL_EVEN_NET_SECTIONS_PROBE is not a dependency. The same
campaign's verified four immediate parent reads are reused at unchanged
hashes; the load-bearing beta and mixed-flow sections were refreshed.
Concrete's relevant construction was read, not given a new complete audit.
Oversized initial refresh output was truncated and is not counted as a
new full read. Exact instruction snapshots are retained under E/instructions.

Fix a_0,m,v>0, a_n=a_0 2^{-n}. These supplied model data and the chosen
ground state are additional premises, not consequences of a framework
primitive. No physical axiom, odd bilateral spin embedding, Fock-space
implementer of the continuum Bogoliubov map, or empirical prediction is
introduced. Root supplied the candidate and conjectural continuum route;
this is coauthor exposure, not independent discovery or independent review.

Operator-algebraic renormalization, wavelet CAR refinements, inductive
limits and intrinsic convergent sections are prior machinery. See
Osborne--Stottmeister, [Conformal Field Theory from Lattice Fermions](https://doi.org/10.1007/s00220-022-04521-8),
CMP 398 (2023), especially its convergent-sequence criterion. The official
primary publisher source was revisited. No generic novelty is claimed.
The specific question here is compatibility of the actual massive-chain
Bogoliubov gauge with physical cells and actual flows; the new steps are
proved directly, without importing unspecified wavelet regularity.

## 2. Notation and the fixed coefficient convention

K_n=ell^2(Z;C^2), K=L^2(R;C^2), with real position subspaces K_n,R and
K_R. Fourier transforms use exp(-iqx) in the continuum and exp(-ikj)
on the lattice, with normalized lattice measure dk/(2pi). Inner products
are conjugate-linear in the first entry. For real
inputs, the Majorana fields obey ||c(f)||=||f|| and
{c(f),c(g)}=2(f,g)_R. Write jw_n for the compatible even Jordan--Wigner
isomorphism into A_n, the even bilateral spin algebra. All CAR maps below
are restricted to the even algebra when interpreted as spin maps.

The parent cell isometry and its adjoint are

    (j_n z)(x)=a_n^(-1/2)z_j on [a_n j,a_n(j+1)),
    (C_n f)_j=a_n^(-1/2) integral_cell f,
    Q_n=j_n C_n, C_n j_n=1, Q_n ->1 strongly.            (S1)

Let H_(m,n) be the real Haar isometry, repeating each coarse coefficient
over 2^(m-n) children with multiplier 2^(-(m-n)/2). Thus
j_m H_(m,n)=j_n, and rho_(m,n)=jw_m CAR(H_(m,n)) jw_n^-1.
The parent's injection is Phi_n=CAR(j_n) jw_n^-1 into
A=CAR(K_R)^even. Its images are nested and dense.

The actual chain parameters and polarization are

    sigma_a=sqrt(m^2/4+v^2/a^2),
    g_a=sigma_a/2+m/4, J_a=sigma_a/2-m/4,
    D_a(q)=-2J_a sin(aq) sigma_x-2(g_a-J_a cos(aq)) sigma_y,
    E_a(q)=sqrt(m^2+4v^2 sin^2(aq/2)/a^2),
    T_a=D_a/E_a, P_a=(1+T_a)/2, C_0=-sigma_y,
    P_0=(1+C_0)/2.                                      (S2)

Put r_a=J_a/g_a in (0,1). The actual beta_a acts on coefficient
smearings by the real unitary F_a, not by its adjoint:

    theta_a(q)=arg(g_a-J_a exp(-iaq)),
    F_a(q)=exp(-i theta_a(q) sigma_z/2),
    beta_a(c_a(z))=c_a(F_a z) on even products,
    F_a T_a F_a*=C_0, P_a=F_a* P_0 F_a,
    omega_a=omega_0 beta_a.                              (S3)

The field-column convention in Concrete is the adjoint matrix. The
coefficient convention S3 follows from the actual parent's covariance
and is independently checked in the controls. Theta_a is smooth, odd
and periodic because g_a>J_a, so F_a preserves position-real vectors.

In the continuum define

    D(q)=-vq sigma_x-m sigma_y, E(q)=sqrt(m^2+v^2q^2),
    T=D/E, P=(1+T)/2,
    theta(q)=arctan(vq/m), F(q)=exp(-i theta(q) sigma_z/2).
    F T F*=C_0, P=F* P_0 F.                             (S4)

F is a real unitary Fourier multiplier. CAR(F) is therefore a well-defined
quasilocal CAR C*-automorphism. No Hilbert-space implementability in a
preselected infinite vacuum representation is required. Let omega be the
continuum quasifree state with two-point form 2<f,Pg>; equivalently
omega=omega_0 CAR(F), where omega_0 has constant polarization P_0.

## 3. A bounded polar formula proves the strong Bogoliubov limit

The pinned local-even theorem gives j_n P_(a_n) C_n ->P strongly. Extend
the lattice involution to K by

    T_hat_n=j_n T_(a_n) C_n+C_0(1-Q_n).                  (S5)

Q_n commutes with the constant C_0. Thus T_hat_n is a self-adjoint
involution, and S5 tends strongly to T: its first term is
2j_n P_(a_n) C_n-Q_n, and the added complement tends to zero.

For either the lattice or continuum symbol,

    (C_0 T+T C_0)/2=h 1,
    h=m/E in the continuum,
    h_a=2(g_a-J_a cos(aq))/E_a>0 on the lattice.

On the complement in S5 the corresponding h is 1. Hence
2<=2+C_0 T_hat_n+T_hat_n C_0<=4 as operators. The same bounds hold for T,
including arbitrarily high continuum momentum where h tends to zero.
The correct square root is consequently uniformly separated from zero.
Direct matrix multiplication in S3 gives the bounded polar identity

    F_a=(1+C_0 T_a)(2+C_0 T_a+T_a C_0)^(-1/2),
    F  =(1+C_0 T  )(2+C_0 T  +T   C_0)^(-1/2).           (S6)

Indeed C_0 T_a=exp(-i theta_a sigma_z), so the numerator is
2 cos(theta_a/2) F_a and the positive denominator is
2 cos(theta_a/2). The angle is in (-pi/2,pi/2).

Apply S6 to T_hat_n. On j_n K_n it is j_n F_(a_n) C_n and on the
orthogonal complement it is 1. Products of uniformly bounded strongly
convergent operators converge strongly; polynomial approximation to
x^(-1/2) on [2,4] therefore proves

    F_hat_n=j_n F_(a_n) C_n+(1-Q_n) ->F strongly.        (S7)

Each F_hat_n and F is unitary, so the adjoints converge strongly too:
||F_hat_n* f-F* f||=||f-F_hat_n F* f||->0. This proves S7 on every L^2
vector. It uses neither a smooth Haar indicator nor a graph-domain
estimate. It also supplies a direct hypothesis check on the candidate
continuum Bogoliubov rotation, rather than assuming pointwise symbols
automatically imply convergence across changing Hilbert spaces.

## 4. Exact state-adapted system and compatible continuum injection

Define the actual even spin maps and their one-particle isometries by

    rho^omega_(m,n)=beta_(a_m)^-1 rho_(m,n) beta_(a_n),
    G_(m,n)=F_(a_m)* H_(m,n) F_(a_n).                    (S8)

The beta conjugations telescope, so this is an injective isometric
inductive system. H_(m,n) intertwines the constant P_0, and consequently
G_(m,n)* P_(a_m) G_(m,n)=P_(a_n). All quasifree even moments and norm
density give exact actual-state compatibility

    omega_(a_m) rho^omega_(m,n)=omega_(a_n).            (S9)

Choose the continuum injection

    k_n=F* j_n F_(a_n),
    Psi_n=CAR(k_n) jw_n^-1 : A_n -> A.                 (S10)

It is real and isometric. Direct substitution, with no limit, gives

    k_m G_(m,n)=k_n,
    k_n K_n=F* j_n K_n,
    k_n* P k_n=P_(a_n).                               (S11)

The range subspaces in S11 are nested because the cell subspaces are;
their union is dense because F* is unitary. Polynomial density proves
that Psi_n realizes the full even-CAR C*-inductive limit. S11 also gives

    omega Psi_n=omega_(a_n)                            (S12)

on every scale, by quasifree moments and continuity. The inductive-limit
selected state is therefore exactly omega. The reference embedding
CAR(j_n F_(a_n)) would instead identify the selected limit with omega_0;
conjugating the common algebra by CAR(F*) is what restores the stated
geometric Dirac convention. These are specified identifications, not a
claim of a uniquely selected embedding.

The comparison with physical cells is

    k_n C_n f=F* j_n F_(a_n) C_n f ->f,
    k_n k_n*=F* Q_n F ->1 strongly.                   (S13)

Both follow from S7 and Q_n->1. Thus physical averages of any fixed L^2
input have their ordinary geometric field limit under the exact
state-compatible injection.

## 5. The two intrinsic Cauchy-section algebras are identical

For a bounded sequence x=(x_n), the Haar criterion is

    lim_N sup_(m>=n>=N)||x_m-rho_(m,n)x_n||=0.          (S14)

The adapted criterion replaces rho by rho^omega. Denote the respective
C*-algebras by Gamma and Gamma^omega; Gamma_0 is the common c0 ideal.
The dyadic parent's proof turns S14 into convergence of Phi_n x_n.
The same proof using S10-S11 turns the adapted criterion into convergence
of Psi_n x_n, and identifies its quotient with A.

There is a stronger equality. Define real unitaries on the one common K by

    L_n=F* F_hat_n, gamma_n=CAR(L_n)|even.              (S15)

S7 gives L_n,L_n* ->1 strongly. CAR field norm continuity, finite-product
telescoping and polynomial density give gamma_n(b)->b and
gamma_n^-1(b)->b in norm for every fixed b in A. On the actual image,

    Psi_n=gamma_n Phi_n.                              (S16)

If Phi_n x_n->b, then
||Psi_n x_n-b||<=||Phi_n x_n-b||+||gamma_n(b)-b||->0.
The inverse argument proves the converse. Therefore, as subsets of the
same bounded product of actual spin algebras,

    Gamma^omega=Gamma,
    lim_n Psi_n x_n=lim_n Phi_n x_n=:ev_infinity(x),
    Gamma^omega/Gamma_0 = A isometrically.             (S17)

This is not uniform closeness of the two injections on arbitrary bounded
microscopic sequences. It is point-norm asymptotic conjugacy on the common
algebra, applied to converging images. A fixed x_N refined recursively by
rho has limit Phi_N x_N; the different recursively adapted sequence has
limit Psi_N x_N. These two fixed-scale limits need not agree. S17 equates
the evaluations of a *single same sequence* that satisfies either criterion.

## 6. Exact geometric local section quotient, without a local inductive system

For a bounded open interval I, let Lambda_n(I) be the cells wholly inside I.
Let Gamma(I) consist of Gamma sequences with x_n in A_n(Lambda_n(I))
for every n. Finite initial coordinates could instead be discarded with
the same quotient. S17 makes this also the adapted local section algebra.
The quotient by Gamma(I) intersect Gamma_0 is exactly

    A(I)=CAR(L^2(I;R^2))^even.                         (S18)

Here is the check. Phi_n sends each such local element into the closed
algebra A(I), so its norm limit lies there. Conversely the nested
inner-cell Haar images exhaust A(I), as proved in the dyadic parent.
For any b in A(I), choose increasingly accurate approximants in these
images and use the later Haar maps between successive approximation
indices; put scalars or zero before the first index. This gives a bounded
sequence in the local algebras with Phi_n x_n->b. By S17 it is adapted
Cauchy too. Kernel and quotient norm are the usual c0 kernel and
lim_n||x_n||. This proves both directions of S18.

For real f_j of compact support in I, the sampled spin polynomial
jw_n product c_n(C_n f_j) is eventually supported in Lambda_n(I) if
the support has positive distance from the boundary; S13 gives its
usual continuum product in norm. Compactly supported L^2 inputs suffice;
Haar indicators are allowed. General local elements follow by density.

The adapted maps themselves do not define an inductive system of the
finite interval algebras: section 8 gives an exact failure of that claim.
For a fixed convergent local section, however,
dist(Psi_n x_n,A(I))<=||Psi_n x_n-Phi_n x_n||->0.
This is approximate locality for fixed convergent observables. It does
not give a uniform error on every unit vector in each growing local
algebra, a physical tail rate, or preservation of exact support at finite n.

## 7. Actual mixed flows and all section moments have the same limit

The pinned parents give actual even-spin coefficient words W_n(w,p),
where w is any fixed finite word of

    exp(+it D_(a_n)),
    T_n(ell)z_j=z_(j-floor(ell/a_n)),
    exp(-is B_(a_n)), B_a={X_a,D_a}/2-aD_a/2, X_a z_j=aj z_j.

Their continuum words W(w,p) use exp(+itD), physical translations and
exp(-isB), with B=iv sigma_x(x partial_x+1/2)-mx sigma_y and the closed
domain established by the continuum and microscopic parents. The boost
is the actual spin action lambda^b_(-a_n s), not a separately chosen
quadratic flow. The lattice boost has Fourier periodic H^1 domain;
the continuum band domain is the transport of
{psi locally AC: psi,E psi'+E'psi/2 in L^2}. No new domain claim is used.

For parameters continuous in a compact space P, those parents prove

    sup_p ||j_n W_n(w,p) C_n f-W(w,p)f||->0
    for every f in K.                                  (S19)

Thus W_hat_n=j_n W_n C_n+1-Q_n tends strongly to W, uniformly on P on
each vector. The extension adapted to k_n is the real unitary

    W_tilde_n=k_n W_n k_n*+1-k_n k_n*
             =L_n W_hat_n L_n*.                        (S20)

This equality follows on the two reducing subspaces and uses
F_hat_n Q_n F_hat_n*=Q_n. S15 and S19 imply W_tilde_n->W strongly,
uniformly on P: the only moving continuum vectors W(p)f range over a
compact set, where strong convergence of the uniformly bounded L_n is
uniform by a finite epsilon-net. No generator convergence is inferred.

For x in Gamma^omega=Gamma with b=ev_infinity(x), field continuity and
polynomial density now give

    sup_p ||Psi_n alpha_n(w,p)x_n-alpha(w,p)b||->0.      (S21)

Indeed the left embedded action is CAR(W_tilde_n)(Psi_n x_n), so its
error is bounded by ||Psi_n x_n-b|| plus the point-norm convergence
error on fixed b. For any fixed finite ordered collection x^1,...,x^r
and fixed mixed words w_1,...,w_r, product telescoping and S12 give

    sup_p |omega_(a_n)(product_j alpha_n(w_j,p)x_n^j)
             -omega(product_j alpha(w_j,p)ev_infinity(x^j))|->0. (S22)

Here no extra state-limit approximation is needed: the same continuum
state restricts exactly at every n. The actual mixed-flow statement and
the selected limiting state nevertheless agree with the original Haar
section limit. The parent's geometric spacetime-net covariance therefore
applies to S18 and S21. Finite-scale rounded translations retain their
rounding defects. Exact coarse-integer translation equivariance survives,
since each F_a commutes with translations and H intertwines a coarse
shift with twice as many fine shifts.

A nonzero Haar cell indicator is generally outside H^1 and H^2. S7,
S13 and S19-S22 hold on such inputs by strong L^2 convergence and bounded
CAR continuity, not by substituting them into smooth-input O(a) bounds.
This packet claims no O(a) rate, differentiated flow limit, graph-norm
convergence, growing words, growing rapidity, or limit m->0.

## 8. A local Z has infinite support; fixed-a tails remain controlled

Take one coarse-to-fine step, coarse spacing a and fine spacing a/2.
Use dimensionless fine momentum k and z=exp(-ik). For input e_(0,1),
the first component of G_(fine,coarse)e_(0,1) has Fourier symbol

    M_+(k)=(1+exp(-ik))/sqrt(2)
            exp(i[theta_(a/2)(k)-theta_a(2k)]/2),        (S23)

where theta_b(k)=arg(1-r_b exp(-ik)) in dimensionless notation.
The second component has the opposite phase M_-. Set c=r_a,f=r_(a/2).
The fourth power of S23 is the rational function

    M_+^4=(1+z)^4(1-fz)(z^2-c)
                  /[4z(z-f)(1-cz^2)].                 (S24)

To check that its pole is genuine, put t=ma/(2v)>0. Direct algebra gives
c=exp(-2 asinh(t)), f=exp(-2 asinh(t/2)). Strict concavity of asinh on
positive arguments gives asinh(t)<2 asinh(t/2), hence c>f^2. The residue
at z=f is

    (1+f)^4(1-f^2)(f^2-c)/[4f(1-cf^2)] !=0.           (S25)

If the input's image had finite coefficient support, M_+ would be a
Laurent polynomial, so its fourth power could have no pole at nonzero
finite z. S24-S25 contradict that. Equality on the unit circle would
give the same rational identity by analytic continuation, so the
argument does not assume a particular continuation branch for M_+.

Let u=G e_(0,1), v=G e_(0,2). Their supports lie in separate component
coordinates and both are nonzero. The adapted image of Z_0 is
-i c(u)c(v). Its grade-two coefficients are u_(j,1)v_(l,2). If this
element belonged to the even algebra of any finite interval Lambda,
all such coefficients with an index outside Lambda would vanish.
The infinite support of u and nonzero v make that impossible. This
grade statement follows in finite Clifford expansions and then by their
orthogonal trace coefficients; equivalently use the trace-complement
expectation onto Lambda. Thus rho^omega(Z_0) has no finite spin support.

There is still fixed-a exponential quasi-locality. The holomorphic
extension of theta_b uses the difference of logarithms of
1-r_b exp(+-ik), and is analytic for |Im k|<-log r_b. S23 is analytic
and periodic for

    |Im k|<mu_0=min(-log f,-(log c)/2)=asinh(t).         (S26)

For each 0<mu<mu_0 its entries are bounded on the closed narrower strip.
Contour shifting their Fourier coefficients gives
|u_j|,|v_j|<=C_(a,mu) exp(-mu|j|). Their l^2 tails and CAR product
telescoping then give exponentially good finite-interval approximations
to rho^omega(Z_0); the same argument handles every fixed finite local
polynomial. This is consistent with the parent's quasilocal beta.

The strip's physical inverse-length scale is
mu_0/(a/2)=2 asinh(ma/(2v))/a ->m/v. This computation alone does not
bound C_(a,mu) uniformly when a changes, nor turn beta into a shrinking
physical-support transformation. No such uniform physical-tail claim is
needed for S17-S22 and none is supplied. Fixed-observable convergence
in section 6 is a separate, proved statement.

## 9. Exact selected-state compatibility does not fix energy intertwining

In beta coordinates the actual one-body energy is E_a C_0. Hence

    D_f G-G D_c
       =F_f* (E_f H-H E_c) C_0 F_c.                   (S27)

For dimensionless fine k, the scalar defect multiplies the Haar symbol by
d(k)=E_f(k)-E_c(2k). An exact calculation gives

    E_f(k)^2-E_c(2k)^2
          =16v^2 sin^4(k/2)/a^2.                      (S28)

This is positive except at k=0 modulo 2pi. It proves a one-body
intertwining defect, but an even observable still needs a witness because
a common scalar phase would cancel in a number operator.

Use the actual even quasilocal coarse observable
x=beta_c^-1(n_0), n_0=(1-Z_0)/2. After beta_f, its refined image is the
reference number observable n(s), where
s(k)=(1+exp(-ik))/sqrt(2) and mean |s|^2=1. Comparing the two actual
time evolutions in these reference coordinates, their one-particle
rank-one number projections have derivative difference

    i(|g><s|-|s><g|), g(k)=d(k)s(k).                   (S29)

The norm of this rank-two operator is

    sigma_d=sqrt(mean |s|^2 d^2-(mean |s|^2 d)^2)>0.    (S30)

The strict inequality is the variance criterion: d is continuous,
d(0)=0, d(pi)>0, and |s|^2=1+cos k is positive almost everywhere.
It cannot be constant almost everywhere under this weight. S29 acts
nontrivially on the product Fock one-particle sector, so the actual even
observables cannot have identical flows. At fixed a the one-body
energies are bounded, making the coefficient and finite-field-product
derivatives norm derivatives; no formal unbounded infinite spin sum is
being differentiated without a domain argument. The beta conjugacy to
the actual flow is the pinned Concrete theorem.

This exact failure is for the specified adapted G and actual energies,
not all state-compatible refinements. It coexists with S21-S22. The
original Haar map's strict state inequality and local Hamiltonian
coefficient witness in dyadic equations D28 and D30 remain unchanged:
rho and rho^omega are different maps. No preceding failure has been
erased by the new construction.

## 10. Scope stress test and controls frozen before execution

The target is the conditional theorem S7-S22, together with the exact
finite-scale witnesses S24-S30. The accepted outcome is a focused author
proof plus reproducible diagnostic controls; any load-bearing failure
must be preserved and the dependent statement corrected or left open.
Numerical agreement cannot certify the infinite-dimensional proof.
Independent review of this source and final root acceptance of the
provisional dyadic dependency remain open. Formal audit remains separate.

The No-Go Discipline scope check is recorded honestly:

* N1: Haar refinement, conjugation to the selected state, continuum
  unrotation and intrinsic local sections are the real approaches used.
  They do not exhaust every possible local/state/dynamical refinement.
  The five-family negative-packet minimum is not certified; no generic
  no-go or mechanical no-go PASS is claimed.
* N2: state compatibility is proved; finite support and exact energy
  intertwining fail by different witnesses. No number of independent
  walls or logical independence theorem is claimed. Uniform tail
  constants are unproved estimates, not necessary hypotheses of S17-S22.
* N3: the mass gap, fixed beta gauge, supplied chain/state, real CAR,
  parity restriction, parent domains, compact parameters and fixed word
  lengths are explicit. A source scan will be retained.
* N4: the original D28/D30 concern the original Haar map only. The new
  nonlocality and energy defects use S24 and S29, respectively. No old
  no-go is reused as a witness against the changed map.
* N5: nonlocality is proved on a single local Z for every positive a,m,v.
  The energy witness is a specified even quasilocal number observable;
  it is not a claim that every mode or local operator has a nonzero
  defect. Constants and exact coarse-integer translation equivariance
  survive. Diagnostic finite rings do not prove the infinite witnesses.
* N6: no new physical axiom is needed for these conclusions. A different
  embedding convention trades the geometric state for the reference
  state; S10 explicitly makes that convention choice. Changing the
  refinement or dynamics would change the equations in section 9.
* N7: an energy-adapted filter with a different dispersion transport
  could challenge a broad impossibility claim. Its terminal obligations
  would be exact real-CAR isometry, actual-state compatibility, locality
  and energy intertwining together. This packet does not rule it out.
* N8: the immediate dyadic parent's successful asymptotic remedy applies
  here more strongly through S17. General OAR prior art already separates
  renormalized continuum behavior from exact raw-scale equations.

E/CONTROL_PROTOCOL.md freezes the diagnostic fixtures, tolerances,
candidate variants and expected discriminating mechanisms. The complete
analytic note and protocol are saved to E/frozen before any mathematical
process is run. All scientific subprocesses receive true process-group
timeouts with complete INNER and OUTER streams, receipts, and before/after
source hashes. Material variants retain every failing and surviving row;
no threshold will be changed in response to outputs. Same-author alternate
arithmetic is a control, not fresh independent review.

No Git state, worktree, publication, audit result, editable prompt, or
physical axiom is changed by this worker. Root owns synthesis and any
subsequent publication action.

## 11. Recorded author controls and final status update

The complete sections 1-10 and protocol were frozen before scientific
execution at 2026-10-12T13:41:52.433952Z. Their SHA-256 hashes are
49cb5895c5d4b6b88256d5a7bdca471a0fd4c59d1a6c585b733007235a7a7f68
and b58a42eea9ffe96fa16493ac95f5013079f8f7fe3a6c1a1b17b6f37223d5051d.
Those exact bytes remain in E/frozen. This section is appended evidence;
no analytic formula, candidate, original checker or threshold was changed.

The three original mathematical runs began at approximately
13:42:06.302Z, each under an INNER 60-second process-group timeout and
an OUTER 70-second recorder. All six original receipts and both later
supplemental receipts were verified against their externally anchored
input manifests and full stdout/stderr hashes before interpreting rows.
No run timed out, every stderr stream is empty, and the longest INNER
elapsed time was 1.306 seconds. These timing facts carry no scientific
weight. All 260 emitted predicates have raw-line pointers in
E/row_inventory.json; every failure and survivor is listed in
E/result_disposition.json.

| Original run | True / false predicates | Interpretation |
|---|---|---|
| Baseline | 85 / 1 | All matrix, state, composition, finite-support diagnostic, energy and Haar tests hold. The exact symbolic dispersion predicate did not reduce to literal zero. |
| Wrong frame sign | 69 / 17 | Sixteen state, diagonalization, polar and defect-formula checks fail, plus the shared symbolic nonreduction. Isometry, reality, composition, translation and all Haar norm tests survive. |
| Omitted continuum unrotation | 84 / 2 | The fine-Haar geometric criterion fails, plus the shared symbolic nonreduction. Finite-scale state compatibility and all other tested mechanisms survive. |

The baseline's largest matrix-identity residual is 3.45e-14, against the
unchanged 2e-10 tolerance. At a=1,N=8 the adapted image of the first
coefficient vector has l^2 mass 0.108627 outside its nominal two children,
and the even-number derivative discrepancy has norm 0.570994. These are
finite periodic controls, not proofs of infinite support or infinite-volume
dynamics. Sections 8-9 give the corresponding analytic witnesses.

The actual infinite-line Haar quadrature at a=1/512 gives cutoff squared
error 0.000509797. Adding the analytic omitted-tail bound 0.000621699
gives the diagnostic norm value 0.033638, below the predeclared .12 gate.
Without continuum unrotation the corresponding value is 0.501254 and
fails that gate. The Gauss-rule comparison is numerical, not an interval
certificate for the finite-cutoff integral; the quoted value with a tail
allowance is therefore still a diagnostic. S7 and S17 are the proofs of
convergence. Reversing both finite and continuum frame signs conjugates
the scalar multiplier and leaves this norm diagnostic unchanged; the
independent actual D covariance is what rejects that material error.

The symbolic failure was preserved and then investigated under a separate
post-observation freeze, E/SUPPLEMENTAL_PROTOCOL.md, sealed at
13:43:59.785485Z. The supplemental run began at 13:44:07.474931Z. It printed
the original unreduced expression

    2 v^2 [-2(1-cos x)^2-4 cos x+cos(2x)+3]/a^2.

An explicit sin(x)=2 sin(x/2) cos(x/2) substitution turns the normalized
residual into -c^2 s^2-s^4+s^2=s^2(1-c^2-s^2), then exactly zero for
c^2=1-s^2. Both separately frozen exact polynomial predicates hold.
This supports classification as a symbolic simplifier nonreduction,
not a false dispersion formula. It does not rewrite the original baseline
as 86/86 or remove the shared false mutant rows. Original streams, source
bytes and the supplemental provenance remain available together.

After the analytic freeze, root communicated complete source-bound
acceptance of the unchanged dyadic parent. The subsequently read
Dyadic_even_refinement_root_review_coverage.json binds its hash
646ad05e... and records no pending root-review item; the accompanying
DYADIC_EVEN_REFINEMENT_MILESTONE_GATE.md opens the regular dependent
review-PR route. Exact copies/hashes are in E/PARENT_STATUS_UPDATE.json.
This updates the historical at-dispatch status in section 1 and does not
claim formal retained or audit status. Root also read this frozen argument
and reported a first direct derivation check. A separate reviewer began
from a frozen neutral plan before this target and without the author
helpers/results. That review and root's acceptance of this new note are
still pending at this author handoff; no review outcome is inferred here.

All six mathematical source pins were rechecked unchanged after the
controls. E/README.md gives evidence navigation and reproduction commands.
The historical manifests bind the original frozen note; recovery and
reproduction manifests point to those exact immutable bytes after this
appendix was added. No editable prompt, Git state, audit result,
publication surface or physical axiom was modified.


## Publication evidence and review record

**Author/checker pairing:** Same selected model family and reasoning effort, separate reviewer context with its disclosed neutral-plan and later formula exposure; not blinded or diverse-family. Root supplied the candidate route and authored the narrow control repair. Packaging and reproduction add no independent science or audit.

The specified finite-scale adapted maps have infinite support and an explicit even-observable energy-intertwining defect. Fixed-spacing exponential coefficient tails and fixed-observable convergence do not imply uniform physical tail constants, operator-unit-ball convergence, Haar H2 rates, or a theorem about all state-compatible refinements.

The frozen original baseline remains 85 true / 1 false with exit 1; the original wrong-frame and omitted-unrotation jobs remain 69/17 and 84/2. The separately frozen two-predicate half-angle supplement remains 2/0. Root then changed only the symbolic dispersion predicate to reduce its actual residual by the exact half-angle unit-circle identity. The separate corrected whole-helper baseline is 86/0; the same two original candidate mutants under that helper are 70/16 and 85/1. All other raw lines remain exact, apart from each derived summary. Original false rows, nonzero exits, full receipts and every survivor are preserved in the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/0d99401253ebf5790b5ac24a2dcb94a74871f874/.claude/science/physics-loops/toe-state-adapted-20261012/EVIDENCE_MAP.json) and [repair source map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/0d99401253ebf5790b5ac24a2dcb94a74871f874/.claude/science/physics-loops/toe-state-adapted-20261012/ARITHMETIC_REPAIR_SOURCE_MAP.json). The historical failed baseline is not counted as a mutation.

The canonical primary executes the corrected 86-row baseline and original two-row supplement. Five separate nonbaseline jobs reproduce the historical failed baseline, both original mutant jobs, and both corrected mutant jobs. No new mutation design or tolerance change is introduced. Original receipts establish the Python/interpreter identities. Later package-version observations remain explicitly post-run observations; no per-run library lock is inferred. The only allowed stream comparison edit is the exact candidate pathname token, with complete originals retained.

Direct mathematical parents are [Concrete Gapped Chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Local Even Continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Continuum Local Boost](CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Microscopic Local Boost Limit](MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Mixed Local Poincare Correlations](MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Dyadic Even Refinement](DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md). Local-even-net-sections is adjacent context only and is not imported. General CAR, operator-algebraic renormalization and inductive-limit machinery are established prior art, explicitly credited above.

Periodic matrices and uncertified finite-cutoff Haar quadrature are diagnostics; the strong limits, local quotient and witnesses rest on the analytic proof and accepted source review when recorded. Source N1–N8 and literal N5 output remain scoped to the specified maps, with no exhaustive no-go or N-gate PASS claimed. The [execution contract](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/0d99401253ebf5790b5ac24a2dcb94a74871f874/.claude/science/physics-loops/toe-state-adapted-20261012/EXECUTION_CONTRACT.md) preserves full INNER/OUTER records. Canonical execution is pending root execution at preparation; actual outcomes must be read from the later verification record. Global combined validation, strict audit lint and independent audit remain landing obligations. No retained promotion, audit verdict, or Lean claim is made.

The separate reviewer integrity fixture preserves an exit-only survivor: the first sentinel child exited 7 while its outer driver exited 0; both child statuses and complete streams remain archived. Outer exit 0 alone is not evidence that every child check passed. Valid, tampered-checker and exit-only fixture records are retained, without rerunning scientific helpers.

The reviewer used a separate many-body Jordan-Wigner route and a direct Fourier strong-limit argument; its numerical strong-limit diagnostic shares a Fourier identity with the author, so implementation separation is not mathematical independence for that subcheck. Finite-cutoff quadrature is not interval-certified. No diverse-family or blinded review is claimed.
