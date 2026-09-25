# Local charge covariance on a finite observation interval

Personal candidate47, 2026-09-25. Unsealed working derivation, not independently
checked. It extends the personally sealed candidate46, whose independent PRE
is still pending. Candidate46 is an explicit provisional dependency. This is
a finite-graph conditional statement of the supplied common law, not a physical
preparation, detector, calibrated prediction or infinite-volume construction.

Keep every original formation channel and every later number sector. Use
h=KD+delta H4, the vacancy-gated integer electric D, and the unchanged unsigned
matter tensor algebra. No field-only dynamics or one-birth truncation is used.
The common pair-form parent's commuting-electric support observation motivates
the proof below. Prior45 PRE was read before writing this record, but no45
theorem or code is used. No47 checker evidence has been seen.

## 1. Local operators and strengths

Work on the tensor product with A restricted to its two occupied signs, B to
its three states, and one integer rotor per edge. The original composed P
operators have local extensions on this tensor product: constraints on the
unchanged external A factors act as identities. They preserve the physical
Gauss subspace, so tensor-product norm bounds restrict to it. This is a device
for bounding the original operators, not a new physical space or dynamics.

An atom is a matter site or an edge rotor. A star(a) has a, its B neighbors,
and its incident rotors. For degree6 it has13 atoms. Let C be the bounded
generator consisting of the full magnetic Hamiltonian and formation dissipator,
so the state generator is -i[KD,.]+C. Decompose C into:

* One Hamiltonian commutator per unordered overlapping A pair {a,c}, with
  support star(a) union star(c), at most25 atoms. Its norm on bounded operators
  or trace class is at most5184 delta, since ||F_c F_a||<=36 and the Hamiltonian
  term is -2delta (F_cF_a)^*(F_cF_a).
* One formation dissipator group per A star, including all six edge records
  and both original signs, or the six stipulated unnormalized coherent edge
  sums. Its norm is at most600 kappa. For resolved marks ||B||<=5, giving
  12 times2 times25 kappa. Coherent sign outputs on an edge are orthogonal,
  so ||B_++B_-||<=sqrt(50); six times2 times50 gives the same bound. Recycling
  maps are not identified with each other.

For an atom set X define J(X) as the sum of these local norm bounds for groups
whose support intersects X. For O supported in X, locality gives
||C^*O||<=J(X)||O||. It vanishes for each disjoint group. Let X1(X) be X union
all supports of those intersecting groups. Thus C^*O is supported in X1(X).

Write D=sum_e D_e, D_e=(1-n_b)E_e(E_e-q_a), with support {a,b,e}. These are
strongly commuting diagonal self-adjoint operators. If B has support Y, then
alpha_v(B)=exp(ivKD) B exp(-ivKD) has support in

 Y^D=Y union union_{e: {a,b,e} intersects Y} {a,b,e}.

Only those finitely many diagonal terms enter the conjugation. A disjoint term
commutes both with B and every other diagonal unitary, so no iterative halo is
needed. Its operator norm is unchanged, without assuming norm continuity in v.
Set X2(X)=X1(X)^D.

Consequently for every real s,u and every K,

 ||alpha_u C^* alpha_(s-u) C^* O||
       <= J(X2(X)) J(X) ||O||.                         (1)

These bounds involve all sectors and no electric moment assumption.

## 2. Two exact integral identities

For each fixed finite graph the bounded perturbation of the self-adjoint KD
evolution gives the trace-preserving CP propagator. In the interaction picture
its generator is C_t=alpha_t C alpha_-t on trace class, and its dual is
C_t^*=alpha_t C^* alpha_-t. It is strongly continuous on each trace-class input
and uniformly bounded for that graph. Let T(t,0) be its state propagator.
Dual integrals may be interpreted weak-star by pairing with trace class;
no Bochner norm continuity of conjugated rotor shifts is required.

The dual Duhamel equation reads

 T(t,0)^* O = O + integral_0^t T(s,0)^* C_s^* O ds.

For each fixed s insert the same equation for B_s=C_s^*O:

 T(s,0)^* B_s = B_s
       + integral_0^s T(u,0)^* C_u^* B_s du.             (2)

Contractivity of the dual and (1) control the double integral. These identities
are finite-graph identities of the full propagator, not a Dyson truncation
defined by discarding trajectories with later births.

## 3. Scalar first term for arbitrary normal initial field

Supply an arbitrary normal density in the minimum-number matter sector Pmin:
all A plus, all B empty, any compatible normal rotor field. No electric
moment is imposed. Let R_f=sum_x f_x(q_x-1_A(x)), for a finitely supported test
f. It is bounded, supported in the site set Sf, and commutes with D. Put
b_f=2sum_A|f_x|+sum_B|f_x|, so ||R_f||<=b_f.

For O=R_f or R_f^*R_g, one has O Pmin=0. Candidate46's branch-isometry argument,
restated here, gives a scalar compression of C^*O: for a mark(a,b,sigma) and
outward destination c!=b the original charge increment is

 w_f=f_c-f_a+sigma(f_a-f_b).

Its branch map is a rotor translation with distinct outgoing matter word.
For diagonal charge O all off-diagonal branch matrix elements vanish, including
between the two coherent signs. Summing both signs and all b,c gives

 Pmin C^*R_f Pmin = m_f Pmin,
 m_f=2kappa sum_a(d_a-1)sum_{b~a}(f_b-f_a),

 Pmin C^*(R_f^*R_g) Pmin = N_fg Pmin,
 N_fg=4kappa sum_a(d_a-1)sum_{b~a}conj(f_b-f_a)(g_b-g_a). (3)

The magnetic and loss anticommutator terms vanish in this compression because
O annihilates Pmin and the Hamiltonian preserves it. Pmin commutes with D.
Therefore Pmin C_s^*O Pmin equals exactly the same scalar for every s, despite
the actual prebirth field evolution and arbitrary input electric tails.

Since O commutes with D, its Schrödinger expectation equals its interaction-
picture expectation. Equations(1)-(3) and normality give, with X=Sf union Sg,

 |<R_f^*R_g>_t - t N_fg|
       <= (t^2/2) J(X) J(X2(X)) b_f b_g.                (4)

The one-integral equation also gives
|<R_f>_t|<=t J(Sf)b_f, because its initial expectation is zero. Hence the
connected covariance Cov_fg=<R_f^*R_g>-conj(<R_f>)<R_g> obeys

 |Cov_fg(t)-t N_fg| <= t^2 M_fg,
 M_fg=b_f b_g [J(X)J(X2(X))/2 + J(Sf)J(Sg)].           (5)

This is a finite-time, arbitrary-normal-field remainder, independent of K.
No second time derivative, uniform norm-continuity or electric moments were
used. Coarse M may be large. The initial scalar N is independent of delta and
K; the finite-time bound retains delta through the local magnetic strength.

## 4. Uniformity of the local estimate and its meaning

At degree at most6, each A has at most30 overlapping partners. An atom lies
in at most6 formation stars and at most180 magnetic-pair supports. Thus
J(X)<=j|X| with j=933120delta+3600kappa. At most186 local groups meet any atom;
each has at most25 atoms. Therefore |X1(X)|<=4651|X|. Each atom belongs to at
most6 D terms of at most3 atoms, so |X2(X)|<=19|X1(X)|<=88369|X|.
These intentionally loose constants prove that (5) can be uniform over finite
volumes for fixed local support and fixed delta,kappa. Exact support counting
should be used for numerical readout windows. The result supplies a bound on
each finite graph; it does not construct or identify an infinite-volume state
or semigroup, prove boundary convergence, or transfer microscopic errors.

A full Fourier test has support proportional to volume, so these local bounds
do not establish a volume-uniform normalized Fourier covariance remainder.
This limitation is not bypassed by dividing (5) by the number of sites.

## 5. A dimensionless, before-fit local consequence

On a degree6 simple torus, take an adjacent A site a and B site b. Their
relative charges have initial means -60kappa t and +60kappa t, respectively,
to first order. Equation(3) gives

 N_aa=N_bb=120kappa, N_ab=-20kappa.

At any t>0 with t M_bb<120kappa, (5) guarantees a positive Var_b and

 |Cov_ab(t)/Var_b(t)+1/6|
   <= t (M_ab+M_bb/6)/(120kappa-t M_bb).                (6)

This ratio cancels the charge unit and the amplitude kappa in its leading
value. It is calculated before fitting data, for this supplied initial matter
preparation and site-resolved readout. The error bound still depends on model
time and couplings. For kappa=0 its denominator premise fails; no ratio law is
asserted there. Sites not connected by an edge have N_xy=0; this first-order
fact is not permanent absence of correlations.

To compare (6) with observation still requires a justified identification of
the A/B charges with measurable quantities, access to the prescribed preparation
and spatial smearing/readout, and a time interval satisfying the bound in
physical units. No actual detector or natural vacuum has been derived. The
result does not predict photon absorption, heat, a noise spectrum or an observed
particle mass. It closes a particular time-error obligation inside the supplied
model rather than establishing experimental agreement.

## Pending checks

Personally review the weak-star integral argument and support counts, construct
exact finite-graph support-count controls and separate arithmetic/error checks,
then seal the candidate before any neutral independent reconstruction request.
Retain the provisional46 dependency and any failed bound or geometry attempt.
