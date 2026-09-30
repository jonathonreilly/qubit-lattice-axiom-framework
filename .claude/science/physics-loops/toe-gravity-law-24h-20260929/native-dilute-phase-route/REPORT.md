# All-particle dimer control and a diverging pair-coherence distance

Author discovery result, 2026-09-30. Actual current-surface status:
**conditional-support** for the explicitly supplied quantum Hamiltonian;
frontier discovery with unknown reachability to a tensor phase. This is not
a formal review or audit receipt. Independent checking of the new lemmas is
pending at this freeze. No axiom, state-selection rule, Born interpretation,
record instrument, continuum rotation group, or gravity identification is
adopted.

## 1. Contract, source and result

The contract was frozen in `CONTRACT.md` before the exact local checks.
Science authority is main `30a9461ee19a49b99fa6628fe942f08e504e8903`, in
particular `docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md`.
Selected procedure remains `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`.
The campaign working HEAD is a distinct pack-bearing commit, not the science
authority; exact observations and file hashes are in `SOURCE_BINDINGS.json`.
The original deadline and runtime stop sentinel remain binding.

The closest load-bearing result is the actual current-main density theorem,
including its full-carrier square decomposition and bare-gradient estimate.
The full frozen N4 threshold argument, its independent check, the strict
positive extension and its independent check were read. They supply the
definition of the fifteen-channel threshold form only in section 8; none is
needed for the new all-particle inequalities in sections 3–6.

Current-main comparisons read in full were the native RK charge-stability
note, the neutral-scale moving-record correlation note and the supplied
free-Fock vacuum note. Their carriers/laws or hypotheses differ. In
particular, classical vacancy domination and a two-sector free-Fock
coherence example are not imported. Targeted current-main searches and the
open-PR metadata refresh found no version of the short-pin argument below;
the only open proposal at that observation was draft PR9008, an ice
covariance diagnostic. This is a scoped prior-art observation, not an
exhaustive historical novelty claim. No external literature is load-bearing.

For every cubic torus L>=5, mu,tau>0, every density matrix on the full
occupation carrier, and a=min(tau,mu/12), the new estimates are

    <V3> <=24 mu Egrad,
    H0 >=(a/72) O,                                          (1)

where O is the actual diagonal number of particles outside isolated
two-vertex components of the eighteen-neighbor occupation graph. In every
ground state of Hnu=H0-nu N, nu>0, they give

    <O>/<N> <=72 nu/a.                                     (2)

For the actual normalized pair fields
R=(Q_E1,Q_E2,Q_T12/sqrt(2),Q_T13/sqrt(2),Q_T23/sqrt(2)), put

    C(r)=V^-1 sum_(x,A)<R_A(x+r)^dagger R_A(x)>, rho=<N>/V.

The ground-state pair correlation obeys

    Re C(r)>=rho[1/2-nu/(2mu)-nu |r|^2/(2tau)].             (3)

Consequently it is at least rho/4 whenever nu<=mu/4 and
|r|^2<=tau/(4nu). Distances are shortest torus representatives. This is a
genuine many-particle, number-conserving coherence statement on the
original carrier. At fixed nu it controls only a finite distance, so it
does not establish off-diagonal long-range order or a condensate.

Two further discriminators are proved: an absolute all-N compression gap
outside isolated dimers, and O(rho) expectation control of the actual pair
commutators for any fixed number of Fourier modes. A four-edge sign cycle
also excludes a simple diagonal occupation-phase route to a matrix with
nonpositive off-diagonal entries. None is a phase no-go.

## 2. Exact supplied Hamiltonian and reused identities

At each site b_x=|0><1|, n_x=b_x^dagger b_x, N=sum_x n_x. Distinct sites
commute. The Hilbert space is the tensor product of these two-dimensional
factors. Quantum states and expectations are supplied, not inferred from
the abstract algebra M2 alone.

Write G={+/-2e_i,+/-e_i+/-e_j:i<j}, with eighteen distinct neighbors,
m_x=sum_(d in G)n_(x+d), and

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d_1-d_2)/sqrt(2),
    Q_E2=(d_1+d_2-2d_3)/sqrt(6),
    Q_Tij=(1/2)sum_(s,t=+/-1)v_ij^(s,t).

The fifteen bare words B_t are the three d's and twelve signed v's. The
unchanged supplied model is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    W=tau sum_(x,k,A) Delta_k Q_A(x)^dagger Delta_k Q_A(x).

Here P_E and P_T are the respective sums of Q^dagger Q and
Delta_k B(x)=B(x+e_k)-B(x). The main theorem proves exactly

    H0=S+mu D+W,
    D=(1/2)sum_x n_x(m_x-1)(m_x-2),
    S=(2mu/3)sum_x(d_1+d_2+d_3)^dagger(d_1+d_2+d_3)
      +(mu/4)sum_(x,i<j,r<s)(v_ij^r-v_ij^s)^dagger(v_ij^r-v_ij^s),
    <H0> >=mu<D>+a Egrad,
    Egrad=sum_(x,k,t)||Delta_k B_t(x) psi||^2.              (4)

For a mixed state the last expression means its linear extension. The
estimate follows by orthogonal decomposition of the literal three/four
bare amplitudes and the torus inequality sum|Delta f|^2<=12sum|f|^2.
It holds on all particle sectors and for coherent superpositions of
occupation words. These identities, not a bosonic effective Hamiltonian,
are the mathematical inputs used below.

## 3. A two-step hard-core pin controls every triple contact

For distinct d,e in G, consider n_x n_(x+d) n_(x+e). Choose a bare word
B_t(c) whose endpoints are x,x+d, including its actual sign. For
d=2s e_i take c=x+s e_i and t=d_i. For
d=d_i e_i+d_j e_j, i<j, d_i,d_j=+/-1, take c=x+d_i e_i and
t=v_ij^(-d_i,d_j). In both cases one endpoint offset u satisfies c+u=x.

Set z=x+e and shift the center from c to c+e. Since e has l1 length two,
choose a path with exactly two nearest-center steps c,c1,c+e. At its
endpoint one annihilated site is z, and the exact hard-core identity is

    n_z B_t(c+e)=0,
    n_z B_t(c)=-n_z[B_t(c1)-B_t(c)]
               -n_z[B_t(c+e)-B_t(c1)].                    (5)

The sign of the bare word is constant along this translation. At the
starting center z is distinct from both endpoints, so

    ||n_z B_t(c)psi||^2=<n_x n_(x+d)n_(x+e)>.

Write the two differences as A1,A2. Keeping n_z in its stated order until
after taking norms gives

    <n_x n_(x+d)n_(x+e)>
      <=2||A1 psi||^2+2||A2 psi||^2.                      (6)

There is an explicit positive operator certificate for this inequality:

    2 A1^dagger A1+2 A2^dagger A2
       -(n_z B_t(c))^dagger(n_z B_t(c))
      =(n_z A1-n_z A2)^dagger(n_z A1-n_z A2)
       +2 A1^dagger(1-n_z)A1+2 A2^dagger(1-n_z)A2.         (7)

Thus no occupation-diagonal replacement loses coherent interference.
One must not commute n_z through a shifted annihilator; (5) avoids that
invalid step.

Now V3/mu=(1/2)sum_x sum_(d!=e) n_x n_(x+d)n_(x+e). The factor 1/2 cancels
the factor two in (6). For a fixed d and a path step in direction k,
summing over all x gives exactly the full translated bare-gradient sum in
that direction; negative steps give the same sum. This uses an index
bijection, not translation invariance of the state.

For each k, sum_(e in G)|e_k|=12. A fixed axial type is selected by two d's,
and removing e=d for each gives multiplicities 20 in its axial direction
and 24 in either other direction. A fixed signed plane type is selected by
one d and has multiplicities 11 in either plane direction and 12 in the
remaining direction. Every coefficient is at most 24. Summing (6) proves

    V3<=24mu Egrad                                           (8)

as an inequality of quadratic forms on the entire finite carrier.
The translation/index argument works for every L>=5. No paths are
identified as distinct sites when they coincide on a small torus: (5)–(7)
remain actual operator identities. The exhaustive local control includes
L=5,6,7, with the unrestricted integer-coordinate geometry as a fourth
case. The analytic argument supplies all other L, not a numerical
extrapolation.

## 4. Physical isolated dimers dominate low-energy particle number

For each occupation configuration, use its induced graph with edges G.
Let O count its occupied vertices outside components consisting of exactly
two vertices and their connecting edge. This is also a local diagonal
operator. If E_x=1_(m_x=1), then

    N-O=sum_x n_x E_x sum_(d in G)n_(x+d)E_(x+d).            (9)

Let I count degree-zero vertices and T=sum_x n_x binom(m_x,2)=V3/mu.
Every non-dimer degree-one vertex neighbors a vertex of degree at least
two. The number of such higher-degree vertices is at most T, and the
number of degree-one vertices attached to them is at most
sum_(m>=2)m, which is at most 2T. Therefore, configuration by configuration,

    O<=I+3T<=D+3V3/mu<=D+72Egrad<=72H0/a.                (10)

The last inequality uses (4) and a<=mu/12. Since the first comparison is
between diagonal operators and (8) was a full operator estimate, (10)
holds for arbitrary coherent and mixed states. It requires neither
independent pairs nor a chosen matching. The factor three in the graph
bound is attained by a three-vertex path. The finite graph control checks
every labeled simple graph through six vertices; the counting proof covers
all graph sizes and in particular every actual induced torus graph.

The number N-O is even. Hence in a fixed odd-N sector O>=1, yielding

    H0|_(N odd)>=a/72.                                     (11)

In a fixed even-N sector let Q_iso be the diagonal projection onto
configurations with O>0. On that subspace O>=2, so

    Q_iso H0 Q_iso>=(a/36) Q_iso.                          (12)

The same compression lower bound holds on the smaller non-perfect-matching
subspace: every configuration of isolated dimers has a perfect matching.
This extends a closed-channel control to all even N, with a loose constant;
it does not replace the sharper N4 lower bound mu in the threshold work.

These are absolute bounds for H0, not a uniform odd-particle excitation gap
above a finite-density state. The compression can couple to its complement.
In particular, (12) says nothing by itself about a gap for
Q_iso(H0-E_N)Q_iso at the extensive canonical ground energy E_N.

It is instructive why the old N4 degree argument alone did not extend:
two far-separated triangles with vertices {0,2e_1,e_1+e_2} have six particles,
all degrees two, D=0, and no perfect matching. The new gradient pin, not
D>=1, repairs that specific all-N compression estimate.

For any ground state of Hnu=H0-nu N the vacuum trial gives
e:=<H0>/V<=nu rho. The actual uniform pair zero modes ensure <N>>0 for
nu>0. Equation (10) proves (2); the mean number of isolated physical dimers
is consequently at least (1-72nu/a)<N>/2 when the right side is positive.
This is a statement about the original occupation graph, without any pair
Fock-space identification.

## 5. Exact pair weight, finite-distance coherence and large mode weight

The zero-momentum Gram normalization is crucial: the T components are
divided by sqrt(2), whereas the E components are not. With
M_R=sum_(x,A)<R_A(x)^dagger R_A(x)>, the actual energy identity is

    2mu M_R=mu<N>+<V3>+<W>-<H0>.

Using V3>=0,W>=0 and then (8), W<=H0, gives

    <N>/2-<H0>/(2mu)<=M_R<=<N>/2+12<H0>/a.              (13)

If P_edges=sum_(physical G edges {x,y})n_x n_y, then the exact complementary
frame identity is S=2mu(P_edges-sum R^dagger R). It controls collective
frame weight, not an orthogonal five-band projection at every momentum.
Shared plane centers have been included in this identity.

By translation of the sum over x, for every state

    2V[C(0)-Re C(r)]
        =sum_(x,A)||(R_A(x+r)-R_A(x))psi||^2.

Let ell(k)=4sum_j sin^2(k_j/2), k_j=2pi n_j/L represented in [-pi,pi].
The elementary telescoping/Cauchy inequality
|exp(i k.r)-1|^2<=|r|^2 ell(k), together with Parseval, implies

    2V[C(0)-Re C(r)]<=|r|^2 <W>/tau.

This does not need a translation-invariant state. Combining with (13)
proves the stronger arbitrary-state bound

    Re C(r)>=rho/2-e/(2mu)-|r|^2 e/(2tau).                (14)

Equation (3) follows for ground states. On tori much larger than nu^(-1/2),
the controlled distance grows without bound as nu decreases, while the
normalized lower bound Re C(r)/rho remains at least 1/4 inside the stated
window. At fixed nu, sending |r| to infinity is outside this estimate.

There is also a useful precise large-occupation consequence. Define
Rhat_A(k)=V^(-1/2)sum_x exp(-ik.x)R_A(x), and the positive five-by-five
matrix Gamma_AB(k)=<Rhat_A(k)^dagger Rhat_B(k)>. No diagonality between
different momenta is assumed. Equations (13) and W give

    sum_k tr Gamma(k)>=V rho[1/2-nu/(2mu)],
    sum_k ell(k)tr Gamma(k)<=V nu rho/tau.                (15)

For nu<=mu/2 and eta=8nu/tau<=1, modes with ell(k)<eta carry at least
V rho/8. There are at most (1+L sqrt(eta)/2)^3 such momenta, because
ell(k)>=4|k|^2/pi^2. Thus an actual normalized internal combination at
some such momentum has number weight at least

    rho V/[40(1+L sqrt(eta)/2)^3].                        (16)

If L sqrt(eta)>=2 this is at least rho/(40 eta^(3/2)). Combining with the
landed density lower bound rho>=nu/(A+nu B) yields, for
0<nu<=nu_star and the displayed volume/parameter conditions,

    max_(k,u:||u||=1)<(sum_A u_A Rhat_A(k))^dagger
                         (sum_A u_A Rhat_A(k))>
      >=tau^(3/2) nu^(-1/2)/[640sqrt(2)(A+nu_star B)].      (17)

A=10199347200(182mu+240tau), B=3870720 are exactly the current-main
constants. This limit takes sufficiently large volume before nu decreases.
It gives a diverging actual pair-mode weight in the dilute limit. At fixed
nu the bound is not proportional to V and therefore is not a condensate
fraction. It also does not select E versus T or supply a tensor mode.

### Distant single-particle coherence is small relative to pair weight

The occupation-defect estimate gives a further genuine discriminator
between single-particle and pair correlations. Define local diagonal
projectors I_x onto occupation of x in an isolated dimer, and
D_x=n_x-I_x, so sum_x D_x=O. Put
F_x=1_(sum_(z in x+G)D_z>=1), with F_x<=sum_(z in x+G)D_z.
For y-x outside G+G, in particular for shortest |y-x|_1>4, a nonzero
move b_y^dagger b_x I_x removes x from an isolated dimer {x,z}, fills y,
and leaves z degree zero: y is not a neighbor of z. Therefore the exact
support inclusion on occupation words gives the operator identity

    F_x b_y^dagger b_x I_x=b_y^dagger b_x I_x.             (18a)

This does not require F_x to commute with either annihilator. Since
b_x=b_x(I_x+D_x), Cauchy-Schwarz directly in the stated order gives

    |<b_y^dagger b_x D_x>|<=sqrt(<n_y><D_x>),
    |<F_x b_y^dagger b_x I_x>|<=sqrt(<F_x><I_x>).

The second uses (b_y^dagger b_x I_x)^dagger(b_y^dagger b_x I_x)
=I_x(1-n_y)<=I_x. Summing x with fixed y=x+r and using
sum_x<F_x><=18<O> proves, for arbitrary states,

    |V^-1 sum_x<b_(x+r)^dagger b_x>|
       <=(1+sqrt(18))sqrt(rho <O>/V).                     (18b)

In ground states this is at most
(1+sqrt(18))rho sqrt(72nu/a). Thus along the dilute ground-state family,
the normalized distant single-particle correlator tends to zero uniformly
in the stated r, while the normalized pair correlator stays at least 1/4
inside its growing window. This does not rule out a small single-particle
condensate at fixed nu, prove pair condensation, or identify a tensor
excitation. It proves actual pairing structure and a correlation
separation, without an independent-boson ansatz. The exact finite graph
control also checks the distant-move support inclusion.

## 6. Pair commutators: a weak finite-mode bosonic limit, with its limit

For each unique physical G edge e={x,y}, let B_e=b_x b_y. The literal
hard-core algebra gives

    [B_e,B_e^dagger]=1-n_x-n_y,
    [b_x b_y,(b_x b_z)^dagger]=(1-2n_x)b_z^dagger b_y,
    [B_e,B_f^dagger]=0 if e and f are disjoint.             (18)

For normalized u in C^5, sum_A u_A Rhat_A(k) has a coefficient
V^(-1/2)c_(u,k)(e) on each unique physical edge. Its absolute value satisfies
|c|<=1: the axial E row norm is sqrt(2/3); a plane edge gets its two actual
centers, each of size at most 1/(2sqrt(2)), for a bound 1/sqrt(2).
Thus no independent-edge or independent-center approximation is used.

The vacuum commutator is delta_(k,l) G(k), with

    G(k)=diag(1,1,S12(k)/2,S13(k)/2,S23(k)/2),
    Sij(k)=1+cos(k_i)cos(k_j).

For any state, the error in a normalized bilinear commutator is bounded by

    |< [sum_A u_A Rhat_A(k),
             (sum_B v_B Rhat_B(l))^dagger] >
           -delta_(k,l) v^dagger G(k)u| <=324 rho.         (19)

Proof: the identical-edge correction from (18) is at most
V^-1 sum_edges <n_x+n_y>=18rho. For one-end overlaps, Cauchy-Schwarz and
the unitary 1-2n_x give

    |<(1-2n_x)b_z^dagger b_y>|<=sqrt(<n_y><n_z>)
                                  <=(<n_y>+<n_z>)/2.

There are eighteen choices of y and seventeen distinct choices of z at
each common x. Summing the last bound over ordered overlaps gives 306rho.
This proves (19), including off-momentum entries and inhomogeneous states.
The literal three overlap classes are separately checked by exact bit
actions. At equal momenta ||G(k)-I||<=|k|^2/4, so the identity-commutator
error is at most 324rho+|k|^2/4. For a fixed set of m Fourier modes the
corresponding block-matrix norm error is at most 324m rho, plus their
vacuum Gram correction.

This is an expectation estimate for finitely many modes. The number of
modes cannot grow like V while retaining that bound. It is not an operator
norm canonical commutation relation, a Fock-space embedding, control of
products of many pair operators, or a replacement of the hard-core carrier.
Together with (17) it is useful evidence of a controlled dilute collective
observable, but the missing many-body replacement theorem is still missing.

## 7. A distinct sign-gauge approach fails a four-edge test

An elementary route toward positive-ground-state machinery would seek a
diagonal phase change of the occupation basis making every off-diagonal
matrix entry real and nonpositive. It already fails on four literal N2
states of the supplied model.

Let |c,i> denote occupation of {c-e_i,c+e_i}. For nearest centers x=0 and
y=e_3 the hopping block is -tau P_E, with
(P_E)_ij=delta_ij-1/3. This follows directly from the two cross terms of
the W square: one directed hopping matrix element is -tau P_E, not
-2tau P_E. The attraction, V3, and on-center W terms do not connect these
distinct centers; plane annihilators do not act on these axial edges.

The cycle

    |x,1> -> |y,1> -> |x,2> -> |y,3> -> |x,1>

has edge entries tau times (-2/3,1/3,1/3,1/3). Their product is
-2tau^4/81. A diagonal phase gauge preserves the product around a cycle,
whereas four nonzero real nonpositive entries have positive product.
These are distinct physical configurations on every L>=5. Thus that
diagonal gauge does not exist for tau>0, for any mu.

This excludes only the stated simple sign-gauge hypothesis. A non-diagonal
change of variables, other positivity methods, reflection positivity with
new verified hypotheses, and a finite-density phase are not excluded.
No theorem depending on those stronger mechanisms is imported here.

## 8. What the full threshold form still does not determine

The checked N4 work constructs the actual compact-source zero-energy
relaxed form T0 on Sym^2(C^5), using the exact nine-dimensional bond cell,
the physical occupation quotient, matching/nonmatching elimination, and
the transient three-dimensional exterior Green form. The strict-positive
extension proves T0>0 in all fifteen channels. It is not the pulse quartic:
for example, its E-channel bare form is 104mu+240tau, and relaxation
subtracts a strictly positive term, whereas the corresponding pulse energy
coefficient is 52mu+120tau. No pulse coefficient is relabeled as T0 here.

The new estimate (12) retires one potential obstruction to extending the
zero-energy compression: the elementary absolute closed-channel gap need
not vanish merely because N exceeds four. It does not give a many-body
effective Hamiltonian at its extensive ground energy.

To see the precise scale failure, at canonical N~rho V the landed
coercivity gives E_N>=c rho^2 V+o(V). Therefore the absolute lower bound
Q_iso H0 Q_iso>=a/36 cannot certify invertibility or a useful uniform bound
for Q_iso(H0-E_N)Q_iso. The inequality
||Q_iso psi||^2<=72<H0>/a is itself O(rho^2 V) and becomes vacuous at fixed
positive density. A small *fraction* of defect particles does not imply
large overlap with the global isolated-dimer subspace.

An equally concrete difficulty occurs in trying to put an independent N4
answer into boxes. A usual smooth localization bound for gradient
amplitudes has an error of order tau rho/ell_box^2 per volume. Even granting
this favorable error to a proposed physical-state localization, making it
o(rho^2) by that bound asks for ell_box much larger than rho^(-1/2).
A box with a uniformly few particles instead asks for rho ell_box^3 of
order one or smaller, hence ell_box at most of order rho^(-1/3). Those two
requirements do not overlap in the dilute limit. This diagnoses that
particular few-particle-box proof budget; it is not a lower bound on every
possible localization error or a no-go for other methods.

A concrete remaining leading-energy obligation can be stated without
silently presuming coherent polarization. First construct an actual
many-pair comparison, with matching Gram/overlap control and local
elimination errors uniform in N,V, whose leading interaction is the full
T0 and whose total unaccounted contribution is o(rho^2 V) as
V->infinity followed by rho->0. Both the upper variational embedding and
lower energy comparison are required. Only then determine the minimum
energy of the resulting multicomponent interacting pair gas, including
the possibility of fragmentation and its anisotropic band kinetics.

For a single coherently polarized candidate z, ||z||=1, identical-pair
normalization would give pair density n=rho/2 and leading trial expression

    (1/2) T0[z tensor z] n^2 =T0[z tensor z] rho^2/8.       (20)

Equation (20) is a target coefficient with explicit conventions, not an
established upper bound after all many-body errors, not a ground-state
equation of state, and not a proof that minimization over coherent z is the
correct spinor minimization. Strict positivity of the fifteen-channel
form supplies neither that identification nor an SO(3) symmetry.

Formally, let T_EOS be existence and identification of
lim_(rho->0) lim_(V->infinity) E_floor(rho V)/[rho^2 V]
by a correctly defined many-pair T0 functional. A uniform comparison
theorem with an actual state/observable embedding and o(rho^2 V) energy
errors is a **stronger** sufficient lemma: it would imply T_EOS after the
effective variational problem is solved, while a scalar energy limit does
not reconstruct that embedding or correlation control. Merely asserting
the energy limit itself with coefficient (20) is target-equivalent and
would be renaming the unresolved target.

For condensation at a fixed small nu, the concrete missing statement is a
volume-extensive eigenvalue of the full pair correlation matrix, for
example liminf_(V->infinity) lambda_max(Gamma_full)/<N>>0 for an explicitly
specified ground-state family. This is target-equivalent to the chosen
pair-condensation criterion. Equations (3), (16), and (19) are genuinely
weaker: they give a growing finite distance, a subextensive weight bound
at fixed nu, and finitely many weak commutators. They do not close that
lemma. Ground-state selection, phase structure, dispersion of excitations,
two linear tensor polarizations and a readable record remain further
obligations even if such pair condensation were established.

## 9. Approach synthesis, checks and next discriminating action

The materially distinct family tuples and strength tests are recorded in
`APPROACH_REGISTRY.md`. The successful mechanism is a local hard-core pin,
translated-gradient counting, and a positive correlation-matrix estimate.
The second positive family controls the literal overlap algebra. The
many-body elimination family gains a genuine all-N absolute gap but still
lacks a relative/local elimination theorem. The simple diagonal sign-gauge
family has the exact cycle counterexample above.

`check_local.py` imports no helper from prior author implementations. It
checks all 306 ordered d!=e pairs in four geometries (infinite coordinates,
L=5,6,7), for 1,224 full sparse local SOS identities; largest support six
sites and dimension 64. It verifies the translated multiplicities and
their maximum 24, all 33,867 labeled graphs through six vertices, three
literal commutator overlap classes, the distant single-move support
inclusion and the exact axial sign cycle. Actual wall/CPU/RSS measurements
are in `local_checks.json`; the job uses only tens of MB and seconds,
with all thread limits one. Deadline and
sentinel were checked at startup and inside loops. No torus Fock-space
enumeration, parameter scan or heavy job was used. The all-N proof is
analytic; these finite controls do not purport to enumerate all N or prove
a thermodynamic phase.

The exact next action is an independent focused check of (5)–(10), the
shared-center normalizations in (13)/(19), and the quantifiers in
(14)–(17). Only after that check should these high-fanout bounds be reused.
A further deep target would be a *local, background-relative* pair-defect
elimination estimate with a uniform linked error o(rho^2 V), or a distinct
direct lower/upper variational proof of T_EOS. Repeating an N2 dispersion,
a pulse quartic, a positive threshold eigenvalue, or the new absolute
compression gap is not that theorem.
