---
claim_id: finite_window_microscopic_energy_laws_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Conditional weak convergence of full microscopic energy laws after original finite-window formation
  records; an exact original-law graph counterexample to moment and upper-edge upgrades; no laboratory energy identification.
upstream_dependencies:
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/finite_window_microscopic_energy_laws_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics with a sealed independent PRE and released
source POST; unaudited. The native counterexample in Section 7 is an explicitly
attributed addition from that independent reconstruction.

# What microscopic energy observations survive an original formation event

At a fixed finite graph, the supplied common matter-field limit transfers
bounded continuous spectral-energy responses after a positive-probability
window of original formation records. It also transfers energy-bin probabilities
whose endpoints have zero limiting mass. It does not transfer ordinary means,
variances or upper spectral edges. A complete twelve-dimensional physical graph
under the original compensated law has convergent conditional energy probabilities
but divergent ordinary energy moments.

These are predictions within a specified mathematical model. The measured
energy, physical scale and laboratory detector have not been identified with
these spectral observables, so this is not an experimental fit or confirmation.

## Sources and review provenance

The load-bearing parents are:

- [Bounded Block Diagonal Compensation Target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Local Compensation Common Field Record Limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Local Pair Form And General Graph Magnetic Dynamics](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).


The root's derivation and illustrative four-state control were sealed before
independent reconstruction. The checker independently reconstructed the
distributional bridge and supplied the exact native graph counterexample.
After PRE sealing and complete root review, the author packet was released
for POST comparison. The complete PRE also treats stopped-first-birth
instruments; that additional general theorem is not needed for the deterministic
readout result below.

POST identified a substantive missing restriction in the root's displayed
magnetic sum: only overlapping A stars may be included. The unrestricted
display would give a spurious contribution on disconnected stars. Section 1
below corrects that display to the actual parent Hamiltonian. The bounded
coefficient proof and illustrative control did not use the extra distant terms.
Section 5 also makes “fixed bounded continuous” explicit. The original author
seal and correction record remain intact in the evidence packet.

The primary runner freshly executes the two exact source programs in isolated
temporary directories. This reuses root and checker code; it is not another
independent reconstruction. The independent checks, historical outputs and
final publication correspondence retain their separate scope.

## 1. Exact premises and the gap being addressed

Use the fixed finite graph and all physical matter/field sectors of the
local-compensation common-law parent. The microscopic Hamiltonian and jumps are

    H_(epsilon,S)=delta epsilon^-4 (W+epsilon T_S+epsilon^2 C_S),
    L_(j,epsilon,S)=sqrt(kappa) epsilon^-1 j_S.

W counts A holes, P=1_(W=0), j_S P=0 and [W,j_S]=-j_S. The compensation
commutes with W and is uniformly bounded in S at a fixed graph. The original
full effective jumps B_(j,S) and every original matter output remain.
Fix K,delta,kappa>0, and take the parent's resource scaling

    delta/[epsilon^2 S(S+1)]=K.

The target on the full rotor P space is h=K D+delta H4, with the actual
vacancy-gated D and H4=-2 sum_(a<c, distance(a,c)=2) (F_c F_a P)*(F_c F_a P).
H4 is bounded at fixed graph and D is nonnegative self-adjoint multiplication.
No reduction of D to an empty-matter sum of squares is made after formation.
The weak-field substitution K=g^2/(2 tau), delta=1/(4 tau g^2) is optional
and is held fixed during this first resource limit.

The bounded-block-diagonal-compensation parent supplies an exact unitary
cluster rotation U_(epsilon,S)=I+O(epsilon), uniformly in S. In its P block,

    P U* H_(epsilon,S) U P = h_S + R_(epsilon,S),
    h_S=K D+delta H4_S,  ||R_(epsilon,S)||<=C epsilon^2.       (1)

Here the equality of the electric coefficient is exact under the stated
resource scaling. H4_S includes that parent's canonical fourth-order
compensation expression. The common-law parent proves its uniform boundedness
and strong convergence to H4. Extend H4_S by zero off the physical spin box
and put the same D on the rotor P space; the spin box reduces this extension.
All constants in this note can depend on the fixed graph and K,delta,kappa.

The existing trace-norm density and finite classical-register limit alone
does not control unbounded energy means. Nor does it directly justify
epsilon^-1 j_S acting on a trace-close density at one exact birth time.
The latter is a failed shortcut: j_S P=0 on a bare initial P state even when
the effective B_j is nonzero. We instead use the cluster rotation for energy
test functions and the actual finite-window record law for conditioning.

## 2. Bare P vectors have convergent energy characteristic functions

Let iota_S be the natural physical spin-to-rotor embedding. If psi_S is
P-supported and iota_S psi_S->psi in norm, then for every real t,

    iota_S exp(-it H_(epsilon,S)) psi_S -> exp(-it h) psi.  (2)

The right side is embedded in the full physical space. To prove this, exact
block diagonalization and unitarity give, on P,

    ||exp(-it H)psi_S-exp(-it h_S)psi_S||
       <=[2||U-I||+|t| ||R_(epsilon,S)||] ||psi_S||.       (3)

The comparison treats the small high-cluster component of the bare input in
norm, without expanding its arbitrarily fast phase. The large high-cluster
energies therefore do not invalidate (3). A bounded-perturbation Duhamel/Dyson
argument with the common K D propagator gives strong convergence of
exp(-it h_S) to exp(-it h), uniformly on compact time intervals for each
fixed vector. It uses strong H4_S convergence, uniform boundedness, and the
compactness of each continuous fixed-vector orbit on a compact interval.
Combining this with (1),(3) proves (2).

Consequently, for normal P-supported densities rho_S with
iota_S rho_S iota_S* ->rho in trace norm,

    Tr[rho_S exp(it H_(epsilon,S))] -> Tr[rho exp(it h)].   (4)

Finite-rank approximation proves the passage from vectors to trace-class
densities; all test operators have norm one. The characteristic-function
continuity theorem then proves weak convergence of the corresponding energy
probability measures. In particular the expectation of every fixed bounded
continuous real energy response f converges. An interval probability converges
when the limiting measure assigns zero mass to its endpoints. Neither all
spectral projectors nor total variation nor energy moments are asserted.

## 3. Actual positive-window conditioning

Start with P-supported microscopic densities converging to a fixed normal
rotor density rho. Add a finite classical register recording an event E in
a finite list of specified positive time bins. The register reads original
marks without changing their action on the physical state. For example E
can require exactly one specified resolved mark during [0,b], with no other
marks in that interval; all original channels remain enabled in the dynamics.
The parent register construction also allows flags for at least one mark.
This note does not condition on a prescribed isolated time of probability zero.

Fix the bins and final time T. The parent full density/register convergence
implies convergence in trace norm of the positive subnormalized event blocks

    iota_S eta_(epsilon,S,E)(T) iota_S* -> eta_E(T).       (5)

Suppose p_E=Tr eta_E(T)>0. Then p_(epsilon,S,E)->p_E and the normalized
conditional microscopic density sigma_(epsilon,S,E) converges in trace norm
to sigma_E=eta_E/p_E, which is P-supported. Indeed the normalized error is
at most twice the subnormalized error divided by p_(epsilon,S,E).

Equation (4) still applies to the energy expectation on these actual
conditional densities even though they are not exactly P-supported. Choose
P-supported spin-box compressions of sigma_E converging in trace norm to it.
Replacing sigma_(epsilon,S,E) by these approximants costs at most the trace
distance, because exp(it H_(epsilon,S)) has norm one. Apply (4) to the
approximants. Thus

    Tr[sigma_(epsilon,S,E) exp(it H_(epsilon,S))]
                     -> Tr[sigma_E exp(it h)].           (6)

The actual microscopic energy measure after the finite-window event therefore
converges weakly to the full common-law conditional energy measure. It is the
energy of the state at the specified final measurement time, after all the
Hamiltonian evolution and original births admitted by E. It is not an energy
change evaluated at an exact microscopic jump or a heat/work definition.
The same argument gives joint finite-register/energy-bin probabilities at
continuity bins; zero-probability limiting events have vanishing joint mass
but no asserted normalized conditional limit.

## 4. A controlled diagonal to the actual effective birth output

Fix an original resolved mark B_j and normal rho with

    r=Tr(B_j rho B_j*)>0.

For the effective process let E_b be exactly one original mark, of type j,
during [0,b], with no other marks. Put Gamma=kappa sum B_l* B_l and
V(t)=exp[t(-ih-Gamma/2)]. Its unnormalized conditional state is exactly

    eta_b=kappa integral_0^b V(b-s) B_j V(s) rho V(s)*
                                      B_j* V(b-s)* ds.   (7)

Strong continuity of V, boundedness of B_j and finite-rank approximation
give eta_b/(kappa b)->B_j rho B_j* in trace norm. Hence

    p_b/(kappa b)->r,
    sigma_b -> sigma_birth=B_j rho B_j*/r.                (8)

No energy-domain or initial derivative assumption on rho is needed for (8).
At each fixed b>0, choose the microscopic resource sufficiently far along
the permitted scaling that the event-block error is small compared with p_b
and the bounded energy tests in (6) are accurate. A successive diagonal with
b->0 then gives weak convergence of the actual finite-window microscopic
conditional energy law to the h-energy law of sigma_birth. One rigorous
choice uses a countable convergence-determining set of bounded continuous
functions, with each successive finite list controlled before reducing b.
This asserts existence of such a diagonal, not every joint epsilon/b schedule,
a necessary detector bandwidth, or a numerical laboratory error certificate.

This statement uses the actual B_j output with its full electric and matter
content. It does not assert a narrow line, an energy eigenstate, equality of
ordinary means, or convergence of the extreme support of energy distributions.
Small tails can change means and spectral edges without changing weak limits.
Any subsequent weak-g, large-volume or long-time use requires its own order
of limits and error control. In particular there is no uniformity in g here.

## 5. Exact finite counterexample to upgrading weak energy laws to means

The following four-state example is an illustrative member of the general
bounded compensation hypotheses. It is not a truncation, numerical simulation
or replacement of the original lattice formation instrument. It tests the
logical distinction in (6), rather than supplying new native physics.

Take basis (p0,p2,q0,q2), P=span(p0,p2),
W=diag(0,0,1,1), N=diag(0,2,0,2). In number sector n=0,2, let T couple p_n
to q_n with a_n>0, and C have diagonal values a_n^2 on p_n and c_n on q_n.
Take delta=1 and the sole bare jump j=|p2><q0|. Then jP=0, [W,j]=-j,
[N,j]=2j, and C commutes with W and N. The two Hamiltonian blocks are

    H_n=epsilon^-4 [[a_n^2 epsilon^2, a_n epsilon],
                   [a_n epsilon, 1+c_n epsilon^2]].       (9)

H2^C=0, H4^C=diag(c0 a0^2,c2 a2^2), and B=-a0|p2><p0|.
An actual jump always produces p2. No further jump acts in the N=2 sector;
its subsequent evolution preserves its H_2 energy distribution. Conditional
on the event having positive probability in ANY positive interval, the final
energy law is therefore exactly the spectral law of the bare vector p2.

For a=a2, c=c2>0, set z=1+(a^2+c)epsilon^2 and
d=sqrt(z^2-4ca^2 epsilon^4). The two exact energies and the high weight are

    E_low=2ca^2/(z+d), E_high=(z+d)/(2epsilon^4),
    w_high=(a^2/epsilon^2-E_low)/(E_high-E_low).           (10)

Thus E_low->ca^2, w_high~a^2 epsilon^2 and the energy measure converges
weakly to the atom at ca^2. But its ordinary mean and variance are exactly

    mean=a^2 epsilon^-2,  variance=a^2 epsilon^-6.          (11)

These follow directly from the p2 diagonal and off-diagonal entry in (9).
They diverge. A fixed bounded continuous energy-response function sees the common
limit, while the ordinary energy budget is dominated by a vanishing high tail.
For a fixed energy interval containing ca^2 in its interior the probability
tends to one; a projector with an endpoint at that limiting atom need not
converge. The example preserves rather than removes the failed mean upgrade.

The separate root control code uses
80-digit arithmetic to compare the exact spectral formulas with a direct
2x2 eigensystem, moments and no-event probabilities. It is root-authored
numerical corroboration, not an independent scientific reconstruction.

## 6. Claim scope and the observation bridge

N1: energy measurements other than this supplied spectral observable,
physical source/reservoir completions and other microscopic laws remain open.
N2: weak energy measures, support edges, moments, conditional energies and
energy changes are different objects. N3: the fixed graph, fixed couplings,
positive-probability finite bins, retained original instrument and ordered
resource/window limits are explicit. N4: all original outputs and channels
remain in (5)--(8). N5: neither an observed experiment nor the framework is
excluded or confirmed. N6: bounded energy-bin observations now have a precise
conditional bridge, while an ordinary energy ledger still needs tail control.
N7: identifying h with a measured energy and calibrating its scale is not
derived by a spectral convergence theorem. N8: no prior energy-spread result
is erased, and no count, density or weak-measure result is promoted to energy
conservation, absorbed photon energy, native vacuum selection or TOE closure.

The conditional theorem and illustrative counterexample have a sealed independent
PRE and released-source POST within the scope recorded above. No retained audit
status or physical energy identification is inferred.

## 7. Independent native counterexample

This section is adapted from the sealed independent PRE, with its provenance retained.


Take the disjoint union of an A-centred two-leaf star and a single A--B edge. This is an admissible fixed finite simple bipartite graph of the common-law and local-pair parents. It is not a cube or a connected-volume construction, and no conclusion about a separate cube moment asymptotic is inferred from it. Every field is fixed by Gauss law on these trees: for an A-to-B edge, E_b=-q_b and the charge sum in each connected component is one.

The two-leaf component has exactly six full physical charge words:

    (-,+,+), (0,0,+), (0,+,0), (+,-,+), (+,0,0), (+,+,-).

The single-edge component has exactly two, (0,+) and (+,0). Thus the full physical Hilbert space has dimension twelve for every S>=1; all legal matter and electric words are retained. Every permitted hop or birth shifts a zero link to +/-1 with normalized spin weight one. These matrices are therefore exactly independent of S. No field box truncation of a larger physical tree space is used.

There is only one A site per component, so all compensation gates equal one, D_(a,S)=D_(a,infinity) on these words, and C_a=F_a*F_a. On the full P space the gated D vanishes. Distinct A stars are disconnected, hence the local-pair identity gives H4=0; direct computation of all terms in the bounded-compensation parent's coefficient agrees. The common target Hamiltonian is exactly h=0.

In the single-edge spectator, let u=(+,0) and v=(0,+). Both original signed creation operators vanish identically on its complete physical space: there is no legal word with both endpoints empty. The absence of its births is therefore a property of the original instrument, not a deleted channel. In basis (u,v),

    H_spectator = delta epsilon^(-4) [[epsilon^2,-epsilon],[-epsilon,1]].

Its eigenvalues are 0 and E_high=delta epsilon^(-4)(1+epsilon^2). A bare u input has high-energy weight w=epsilon^2/(1+epsilon^2). This component evolves unitarily, so this spectral weight is constant at every time.

In the birth star let u_1=(+,0,0). Its outgoing symmetric one-vacancy vector is v_sym=[(0,0,+)+(0,+,0)]/sqrt(2). The actual Hamiltonian on their span is

    H_birth = delta epsilon^(-4) [[2epsilon^2,-sqrt(2)epsilon],
                                [-sqrt(2)epsilon,1]].

Every resolved mark from u_1 has effective intensity kappa; total effective intensity is 4kappa. Fix one resolved edge/sign j and require its first event in I=(a,b], 0<a<b<T. Its limiting probability is

    p = [exp(-4kappa a)-exp(-4kappa b)]/4 > 0.

At any actual occurrence of that mark the star lands in its uniquely specified fully occupied word. That word is exactly dark and has zero full microscopic energy. No later original birth is possible there. The spectator has no birth channel and is statistically independent of this first-star event. Consequently, at any deterministic T>=b, and also for an energy measurement immediately after the stopped first mark, the exact conditional full-energy law is

    mu_S = (1-w) delta_0 + w delta_(E_high).

The energy measurement is of the whole physical Hamiltonian, so the untouched spectator's energy is part of it. No claim that this energy was absorbed or created by the selected birth is made.

For delta=K=1, Cspin=S(S+1), the formulas reduce to

    w=1/(Cspin+1),       E_high=Cspin(Cspin+1),
    mean(H_S)=Cspin,
    second moment=Cspin^2(Cspin+1),
    variance(H_S)=Cspin^3.

Thus mu_S tends to delta_0 in total variation while its ordinary mean and variance diverge. Its upper support edge is E_high tending to infinity although the limit support is {0}. Every finite-S moment exists. The input is the exact fixed bare P vector u_1 tensor u, with no varying contaminating preparation. The event has a fixed positive limiting probability. This disproves a general implication from the supplied finite-bin distributional bridge to full ordinary moments or upper support-edge convergence, within the actual compensated graph class.

For the initial-time limitation, on time s=theta epsilon^4/delta the loss term is negligible to leading order and the first-star one-vacancy amplitude is sqrt(2)epsilon(1-exp(-i theta)). A chosen resolved intensity therefore tends to

    kappa |1-exp(-i theta)|^2,

which ranges from zero to 4kappa rather than the effective initial value kappa. The integrated probability of this fast initial layer still vanishes. This is consistent with fixed-window convergence and obstructs a uniform inference about microscopic time-density values down to the initialization layer.

The independent primitive_energy_control.py builds every word, hop, compensation and original jump directly. It retains all six resolved channels and all three coherent channels, including the identically zero spectator channels. Structural identities are checked for both instruments. The event/energy example and time-density table use the stated resolved mark; no separate coherent numerical event simulation is claimed. Six spins S=1,2,4,8,16,32 are checked. The complete results include six structural rows, six energy/event rows with three bounded energy tests each, and 24 initial-layer rows. The bounded test values evaluate the analytically specified two-atom law; the separate matrix checks concern its high-energy spectral weight and direct moments. Those formula evaluations are illustrative, not additional independent verification of the law.

All structural residuals are exactly zero in the stored arithmetic. At S=32, the actual event probability is 0.0920628360861927 versus limit 0.0922814585308593; the exact high-energy probability is 1/1057, its energy is 1116192, its mean is 1056, and its variance is 1177583616. The largest relative moment diagnostic residual is 9.74222991840868e-11, including the full fast unitary's floating error. These floating computations are not interval enclosures; the displayed exact matrix/eigenvector calculation supplies the all-S counterexample. The sealed independent PRE run completed in 0.44775387505069375 external seconds, exit 0, empty stderr; its internal scientific time is separately recorded as 0.0126952501013875 seconds.


## Evidence and remaining physical obligations

The [root history](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/fa81cd2a2c6038a97e862e8ff1ec83bda18084b9/.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/author_history/)
and [independent PRE](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/fa81cd2a2c6038a97e862e8ff1ec83bda18084b9/.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/review/independent/)
contain `FINITE_WINDOW_MICROSCOPIC_ENERGY_MEASURES_ROOT.md` and `PRE.md`, preserving their exact original arguments. The
[POST](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/fa81cd2a2c6038a97e862e8ff1ec83bda18084b9/.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/review/independent/)
and [magnetic-sum correction](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/fa81cd2a2c6038a97e862e8ff1ec83bda18084b9/.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/review/)
contain `POST.md` and `FINITE_WINDOW_ENERGY_MAGNETIC_SUM_CORRECTION.md`, recording the necessary repair without changing either seal. The
[primary runner](../scripts/finite_window_microscopic_energy_laws_2026_09_25.py) and
[complete fresh result](../outputs/finite_window_energy_20260925/FINITE_WINDOW_ENERGY_PUBLIC_RESULTS.json) distinguish the generic four-state
control from the native full-graph control. Historical failures and limitations
are retained in the review packet; source bindings distinguish omitted duplicate
snapshots from scientific evidence actually included.

An energy distribution can now be compared through bounded responses under
the stated ordered limits. Converting that into a prediction for a measured
experiment still requires physical identification and scale calibration,
preparation, and error control at the actual resource, volume and readout time.
An ordinary energy ledger additionally needs uniform integrability or another
valid tail bound. This result supplies none of those missing physical inputs,
and does not reinterpret the spectator's initial energy as energy created by
the observed birth.

## Landing-review boundary and No-Go Discipline Gate

N1: the supplied model and stated preparation only. N2: other physical routes remain open. N3: no new premise or parameter identification is adopted. N4: Fixed bounded continuous spectral responses and positive-probability finite windows are retained. Conditional normalization precedes a selected shrinking-window diagonal. Native disconnected-tree counterexample forbids moment and upper-support upgrades, without claiming energy was created by a birth. N5: independent exact or explicitly numerical controls supplement the written argument. N6: no universal framework exclusion or empirical confirmation follows. N7: source, stable response and measurement identification remain obligations. N8: later audit is separate; historical author checks are provenance only.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Complete original source remains recoverable at PR #9192's frozen head. No audit verdict or retained grade is applied.
