---
claim_id: original_formation_and_field_response_budget_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Exact conditional common-law aggregate impulse-response/count budget with full matter dynamics and the original formation instrument; no measured probe identification, photon lifetime or microscopic derivative transfer."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24
runner: scripts/original_formation_and_field_response_budget_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics with scoped independent PRE/POST checks; no retained audit status.

# Original formation and the field-response budget

In the supplied common matter/rotor model, each original formation event reduces
a particular aggregate field-response strength by the same amount. Summing both
Wilson-loop quadrature impulse responses over every elementary cubic plaquette
gives a bounded response operator proportional to the number of vacant B sites.
Exact number balance then fixes its complete preparation-time change from the
original formation count. The normalized relation cancels the supplied electric
coefficient K. This is a joint restriction on precisely defined model
observables, with their experimental identification still open.

The response strength is the initial-lag slope of an impulse experiment made
at each actual preparation time. The state at that time includes all prior
births and subsequent matter/field evolution. A statement at arbitrary finite
preparation time does not determine a finite-lag propagation kernel, stationary
frequency spectrum, photon attenuation or microscopic derivative limit.

The root personally derived the argument and primitive controls below, before
reading a separate sealed PRE reconstruction. Released-source POST found no
required mathematical repair. The author's sufficient fourth-electric-moment
domain and its preservation proof are retained unchanged. The independent PRE
also gives a stronger moment-free response result by a bounded strong-quotient
argument, a positive quadrature-response matrix and an explicit stationary
unsaturated example with nonzero response. Those additions remain separately
attributed in the complete review report; this publication's root response
proof does not rely on them. The bounded count identity itself already holds
for every normal initial state in the root argument.

Loop-family conventions matter: the cubic coefficients use ordinary elementary
plaquettes. On L=4, counting every graph four-cycle would add winding cycles
and change the coefficient. All terms of the full Hamiltonian remain present
regardless of the selected response-loop family. The degree-three cube uses
its own coefficient and is not a surrogate for a degree-six torus.

The earlier initial electric-noise and Wilson-acceleration calculations are
prior photon-bridge results, not new conclusions of this unit. Native probe,
state, scale and readout identification, and uniform control for transferring
an initial-lag derivative from finite microscopic resources, remain open.

## Complete personal argument

### Original formation and a finite-time field-response budget

Personally derived conditional result, 25 September 2026. Separate scoped
PRE and POST checks are complete; no retained audit status. The exact initial electric noise and Wilson
acceleration in the earlier photon-observation work are prior results; they
are not reintroduced as new. The present question is whether anything about
field response can be followed for a finite preparation duration while keeping
the changing matter state and the original formation instrument.

The answer below is a sum of infinitesimal response strengths at each actual
preparation time. It is not a finite-lag propagation kernel, an optical
attenuation law or a stationary radiation spectrum. It concerns the common
rotor law; it does not assume microscopic derivatives converge to rotor
derivatives or identify the probe with an observed electromagnetic measurement.

#### 1. Model and a bounded response operator

Keep the full common Gauss-physical P space: all A sites occupied by unsigned
tensor hard-core charges q_a=+/-1, B sites vacant or charged, and every legal
integer electric configuration including circulation and winding. Edges are
oriented A to B. Gauss law is div E=q-1_A. Use the unchanged supplied law

    h=K D+delta H4,
    D=sum_(e=(a,b),q_b=0) E_e(E_e-q_a),
    L rho=-i[h,rho]+kappa sum_j D[B_j]rho,
    B_(ab,sigma)=P j_(ab,sigma)F_aP.

The coherent alternative is precisely the unnormalized sign sum on each
fixed edge. K,delta,kappa>0 are supplied constants. H4 is the overlapping-star
Gram Hamiltonian of the parent. Every term in H4 and B_j is a finite sum of
matter operators times unit rotor translations. There is no electric-field
dependent coefficient in these bounded terms. All vacancy gates remain in D.

Let v be any integer divergence-free loop vector and W_v its unitary rotor
translation, W_v|q,E>=|q,E+v>. It preserves the physical space. Define its two
bounded Hermitian quadratures

    C_v=(W_v+W_v*)/2,    S_v=(W_v-W_v*)/(2i).

On finite electric words, the electric second difference gives

    W_v* h W_v+W_v h W_v*-2h
      =[W_v*,[h,W_v]]
      =2K sum_e 1_(q_b=0) v_e^2 =: F_v.                 (1)

Indeed E_e(E_e-q_a) evaluated at E+v and E-v minus twice its value at E
leaves 2v_e^2. The q_a-linear term cancels. Matter gates commute with W_v.
Every rotor translation commutes with W_v, so the complete magnetic term
cancels, irrespective of its matter permutations or the current record sector.
Equation (1) extends to the displayed bounded positive operator F_v. It does
not require actual energy to control electric flux on occupied links.

The quadrature identity is

    [C_v,[h,C_v]]+[S_v,[h,S_v]]=F_v.                     (2)

Expansion gives half the sum of [W_v*,[h,W_v]] and its adjoint counterpart;
these coincide since [W_v,W_v*]=0. No small-angle replacement is involved.
Further, [B_j,W_v]=[B_j*,W_v]=0, including the stipulated coherent channels.
Thus the formation dissipator annihilates C_v, S_v and W_v on the full space.
It does not annihilate F_v: that operator contains the evolving vacancy gates.

#### 2. What response (2) measures

Let T_t be the full original common semigroup and rho_t=T_t rho_0 the actual
state at preparation time t. Apply a Hamiltonian impulse with integrated
strength +eta V, for V=C_v or S_v, giving the state

    rho_(t,eta)=exp(-i eta V) rho_t exp(i eta V).

This defines a response function of the existing model; it is not a proposal
to adopt a new fundamental interaction or an assumed native laboratory probe.
Measure the same V after a lag s under the unchanged full generator. Its
linear response is

    R_V(s;t)=d/deta Tr[V T_s(rho_(t,eta))] at eta=0
            =i Tr rho_t [V,T_s*V].                      (3)

When the derivative in lag is justified as below, R_V(0;t)=0 and

    d R_V(s;t)/ds at s=0+
       =-Tr rho_t [V,[h,V]].                            (4)

The minus sign follows from the specified positive impulse convention.
The dissipator on V is zero, but the state rho_t in (4) still contains all
actual prior births and subsequent matter dynamics. Combining the two
quadratures defines the nonnegative response strength

    -d/ds [R_(C_v)(s;t)+R_(S_v)(s;t)] at s=0+
       =Tr rho_t F_v.                                  (5)

This is an initial-lag slope at any finite preparation time t. A frequency
integral of a stationary susceptibility would require additional stationarity,
transform and convergence assumptions; no such spectral interpretation is
silently supplied. Nor does (5) determine response at a nonzero lag.

##### A sufficient domain class, preserved by the full evolution

Put M=I+sum_e E_e^2. A sufficient, deliberately nonminimal assumption is
Tr(M^2 rho_0)<infinity. This is a total-electric fourth-moment condition,
stronger than a finite expectation of the gated D. Finite electric inputs
and the usual fixed finite-dimensional smooth field packets meet it.
The earlier scratch explored a second-moment formulation; the present proof
uses this stronger explicit condition to justify both response derivatives.
The bounded identities (1) and the count budget below need no such condition.

Here is preservation at every fixed finite time on a fixed finite graph.
The diagonal H0=KD commutes with M, and its unitary group is an isometry
for the graph norm ||M psi||. For any fixed translation by d,

    1+|E+d|^2 <= 2(1+|d|^2)(1+|E|^2).

Matter matrices and charge/occupancy gates commute with M. Therefore every
finite rotor-path sum, including H4, every sqrt(kappa)B_j, and their loss
Gamma=kappa sum B_j*B_j, is bounded in this graph norm. In particular
||h psi||<=c||M psi|| on Dom M. The same holds after multiplying by either
quadrature, and exp(-i eta V) is bounded in the graph norm locally uniformly
in eta by its power series.

The no-event propagator generated by H0+delta H4-i Gamma/2 obeys
||M V_t M^-1||<=exp(c_0 t) by its interaction-picture Dyson series on this
graph-norm space. Set c_j=||M sqrt(kappa)B_j M^-1||. In the original
positive history expansion, an r-jump term is bounded in weighted trace
by exp(2c_0 t) times the product of c_j^2. Summing its ordered time integrals
gives

    Tr(M^2 rho_t)
      <=exp[(2c_0+sum_j c_j^2)t] Tr(M^2 rho_0)<infinity. (6)

These are existence bounds at fixed graph/couplings, not volume-uniform or
weak-coupling error estimates. The history expansion also applies to the
weighted trace norm of perturbations generated by the bounded graph-norm
operator V. Since h rho and rho h are trace class on this class, the initial
lag derivative exists in trace norm. Differentiating the impulse there
justifies (3)-(4); equivalently one can first compute on finite electric
cores and use the displayed weighted bounds. No cap on actual h energy
is substituted for this moment hypothesis.

#### 3. Summing the response on the cubic torus

Take an even simple cubic torus of side L>=4. Let n=|A|=|B|=L^3/2, and take
each ordinary elementary plaquette once. Every edge belongs to four of these
plaquettes, with squared loop coefficient one in each. Every B site has
six incident edges. On P, the total number operator satisfies

    N=n+number of occupied B sites.

Sum (1) over all plaquettes p. There is the exact bounded operator identity

    F=sum_p F_p=48K sum_(b in B)1_(q_b=0)
              =48K(2n I-N).                             (7)

No translation-invariant state, product field state or chosen winding fiber
is needed. A local subset of plaquettes generally has nonuniform link
incidences and does not obey (7); its weights must be retained explicitly.
The eight-vertex cube has degree three and two faces per edge, giving
F_cube=12K(2n I-N). It must not be assigned the degree-six coefficient.

More generally, on an equal-sized regular bipartite graph of degree z, if a
specified loop family has sum_v v_e^2=r for EVERY edge, the coefficient in
(7) is 2Krz. Equal incidence is a hypothesis, not an inference for a boundary
region or an arbitrary graph.

#### 4. Original records determine the entire response-sum budget

Let C(t) count all original formation marks on [0,t], and use the actual
resolved or stipulated coherent instrument. The unchanged full common law
has [h,N]=0 and [N,B_j]=2B_j. Its exact balance gives

    <N>_t-<N>_0=2 E C(t),
    d<N>_t/dt=2 Tr(Gamma rho_t).                         (8)

Define f(t)=Tr(F rho_t). Equations (7)-(8) imply, for every finite t>=0,

    f(t)+96K E C(t)=f(0),
    f'(t)=-96K Tr(Gamma rho_t)<=0.                       (9)

This bounded-operator conclusion holds for every initial trace-one positive
state, including field, number and charge coherences. The full h is allowed
to move already born records. It conserves their total number, so it cannot
alter this aggregate response strength. For the equal-incidence family the
count coefficient is 4Krz, and for the cube it is 24K.

For a definite initial N=N0, every positive-probability original history
containing r marks lands in the exact sector N0+2r; the no-event maps commute
with N. Therefore the normalized conditional state has response strength

    f_history=48K(2n-N0-2r).                             (10)

This does not say that its detailed field response or its energy depends
only on r. If the initial number is not definite, (9) remains valid while
(10) must not replace the posterior weights of the initial sectors.

For the all-A-plus/B-empty reference N0=n, f(0)=48Kn and

    f(t)/f(0)=1-2 E C(t)/n.                              (11)

Thus the unknown K cancels from this normalized joint prediction once the
model's complete response sum and original count are identified. No requirement
that all sites eventually fill follows: unsaturated dark stationary states
can retain a positive f. Number balance alone is insufficient to infer a
particular late-time limiting value. Similarly a decrease of this sum does
not imply equal attenuation of every mode or destruction of every photon.

#### 5. Verification and the remaining observation bridge

The accompanying controls construct oriented cube and L=4,6 torus geometries,
check loop divergence and squared incidences, and test the electric second
difference on every one of the cube's 65 physical charge words and selected
degree-six words at several exact Gauss flows. The noncube controls include
nonzero noncontractible electric circulation. Original F_a then j paths are
executed with all intermediate/output charges and fluxes; they test the
response decrement, +2 number, and resolved/coherent loss on basis columns.
These checks supplement the displayed operator proof. They are not a
finite-time simulation, independent confirmation, or a substitute for domains.

Equations (9)-(11) are falsifiable joint restrictions of this supplied common
model and the precisely defined impulse responses. They do not yet predict
an observed laboratory or astronomical number. The missing identification is
specific: what physical source applies each C_p/S_p perturbation, which
measured field observable corresponds to those quadratures, what collection
realizes the complete plaquette sum, and which records count the original
formation events. Native preparation, physical length/time/couplings and a
finite-parameter microscopic response error are also not established.

Weak-field dispersion and initial electric-noise identities cannot answer
these questions by themselves. Nor does weak convergence of a bounded
finite-time register imply convergence of a lag derivative without an
additional uniform estimate. No comparison with data, selected vacuum, new
axiom, field-only postbirth law, energy reservoir or TOE completion is claimed.

## Reproduction, sources and review scope

The primary runner executes an exact copy of the sealed personal integer
program in a temporary directory. The full scientific output and both streams
are retained, and the original sealed writer is never run in its source
directory. Geometry, electric second differences and actual primitive birth
columns are controls for the displayed proof; they are not a finite-time
simulation, a microscopic response experiment or a comparison with data.

The evidence packet retains the personal seal, separate independent PRE and
POST, their controls and full source/exposure records. A final released-source
publication correspondence check is distinct from the blind PRE; no extra
independence is inferred from a source-hash or cache match. Failed routes and
the author's switch from exploratory second moments to a sufficient fourth
moment remain recoverable. No audit verdict or merge is part of this unit.

The three direct parents are:

- [Original local-pair instrument and magnetic dynamics](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Full compensated common matter/field law](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Formation number balance and unsaturated dark states](FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md).
