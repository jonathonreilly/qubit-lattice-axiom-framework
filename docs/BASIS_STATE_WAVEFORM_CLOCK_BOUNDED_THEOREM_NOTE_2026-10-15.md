---
title: Basis-state waveform clock with a conditional nearest-neighbor controller
claim_id: basis_state_waveform_clock_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: finite basis-start clock and prepared one-port nearest-neighbor controller with complete retained outputs and explicit growing resource costs
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: supplied finite computable waveform and plant, prepared computational-basis controller or quantified Gibbs marginal, paid coefficients, isolation and release; no native source, common cap or reuse
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15"]
runner: scripts/basis_state_waveform_clock_2026_10_15.py
next_trace_action: execute the separately reviewed source-integrity integration gates, then regular publication before independent retained audit
---

Claim type: bounded_theorem

A supplied finite waveform can be approximated by a static weighted-path clock that starts in the known bit string `|10...0>`. The comparison retains the entire plant, every reference, the moving clock and, in the one-port completion, every auxiliary qubit. The clock needs no initially supplied spatial wavepacket. Its pure starting bit string still has energy coherence relative to the runtime Hamiltonian and remains a supplied resource.

Primary-runner role: source integrity only. The unexecuted 60-second primary checks exact bodies, recovery, canonical-parent bytes and actual binding evidence. It performs no simulation, pulse search, scientific fixture or proof test. The historical source proposal remained unexecuted. This separately bound version requires actual root publication-review and selected-base receipts. Primary, cache, mutation, graph, publication and retained-audit outcomes are separate actual records; binding alone does not certify them.

Qualified scientific source acceptance is `174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0`. The complete root derivation `0fc2b704…`, pre-exposure independent derivation `84f03ca0…`, and subsequent source-exposed comparison `8c3ba783…` follow unchanged. Their historical pending statements remain visible. This wrapper applies the accepted corrections and explicitly adopts the comparison's positive-edge substitution. That substitution and the sharper combined estimate are post-exposure synthesis, not part of the protected independent derivation. Root has separately accepted this publication interpretation at exact review eb31fa43c503cfc659e3e5d18c7eafe3ed2927ee3efb45810c5ab4371a8d2708; this adds no new scientific check or retained-audit decision.

## 1. The finite clock and complete target

Let the plant be any finite-dimensional system with a supplied Hermitian Hamiltonian `H_P`, including all original memory and filler factors; arbitrary retained references may be correlated with it. Supply a Hermitian waveform `C:[0,tau]→End(P)`, `tau>0`, with operator Lipschitz constant `L_C` and finite norm allowance. Its exact time-ordered propagator satisfies `i U_C'(t)=[H_P+C(t)]U_C(t)`. No commutation is required. Effective synthesis additionally requires certified computable sample evaluation and finite parameter bounds. A noncomputable existing waveform is not an algorithmic input certificate.

For integer `n>=1`, place `n+1` clock qubits on an open path. Write `n_j=|1><1|_j`, `S_j=(X_j X_(j+1)+Y_j Y_(j+1))/2`, `N_X=sum_j n_j`, and `Omega=pi/(2tau)`. The adopted clock is

```
K_X'=sum_(j=0)^(n-1) Omega[(n-j)n_j+(j+1)n_(j+1)
                          -sqrt((j+1)(n-j))S_j].
```

Each physical edge block has spectrum `{0,0,Omega(n+1),Omega(n+1)}` on the full two-qubit space. There are `n` positive edge blocks. The onsite coefficients contained inside these blocks remain physical. The exact full-clock norm, block-norm sum and normalized trace scalar are

```
B_X'=Omega n(n+1),       s_X'=B_X'/2.
```

The all-occupied state attains the norm. Thus positivity and full-space prices are established without restricting to the intended single excitation.

Let `|j>` be the bit string with its only one at site `j`; `|0>` here is `|10...0>`, not the all-zero vacuum. On that input the free clock is exactly

```
chi_n'(t)=exp(-iOmega n t) sum_j sqrt(binomial(n,j))
                  cos(Omega t)^(n-j)[i sin(Omega t)]^j |j>,
chi_n'(tau)=|n>.
```

The proof uses the symmetric subspace of `n` virtual spins only as a representation identity. Those spins are not additional physical resources. The endpoint phase cancellation is exact; intermediate phases are retained.

Store `C_j=C(t_j)` at `t_j=Omega^(-1)arcsin sqrt(j/n)`, and first consider the abstract occupation-control interface

```
H_tar'=K_X'+H_P+sum_j n_j C_j.
```

For arbitrary matrix `C_j`, this interface is not automatically a two-local or geometrically nearest-neighbor plant coupling. The local completion below requires the stated one-qubit-port form. If `H_P>=0` and `C_j>=0`, the displayed interface is positive; signed inputs require additional actual reserves. The independent body gives one signed-interface recipe with plant reserve `hI` and clock number potential `B N_X`, including their phases and costs. That recipe is not silently included in the positive one-port specialization.

## 2. Uniform error, including endpoints and every output

The free-clock position has law `J~Bin(n,p(t))`, with `p(t)=sin^2(Omega t)`. The square-root variance argument in the complete bodies, using the chord bound on angles at most `pi/2`, gives the finite, endpoint-uniform estimate

```
E|t_J-t|^2 <= tau^2/(2n),                  0<=t<=tau.
```

At `p=0,1` the law is deterministic; no singular division is used. The residual of `chi_n'(t) tensor U_C(t)` under `H_tar'` consists of orthogonal clock components `[C_j-C(t)]U_C(t)`. Therefore Duhamel integration gives, on the complete plant input space and every reference extension,

```
||exp(-it H_tar')J_0-chi_n'(t) tensor U_C(t)||
    <= L_C tau t/sqrt(2n) <= eta_X:=L_C tau^2/sqrt(2n).
```

Here `J_0` appends the pure endpoint bit string. The actual interacting clock is not assumed to follow the free law or remain factorized. For any input density operator the complete output trace norm error is at most `min(2,2eta_X)`. No successful trajectory is selected or renormalized. A sufficient choice is `n>=max(1,ceil[L_C^2 tau^4/(2eta_X^2)])` for a prescribed positive clock-error allowance.

If `C=0` on `[T,tau]`, the ideal plant evolves there as `exp[-i(t-T)H_P]U_C(T)`, while the clock continues to move. The horizon must include the desired window. The clock is periodic and revisits program sites; this is not permanent stopping. Any separately compiled endpoint target may be substituted only at its own actual elapsed time/window, with its own scalar phase and error. It does not prescribe the intermediate plant history.

## 3. Literal one-port completion and geometric counts

For the physical completion assume a nonempty finite plant in a nonnegative-coordinate lattice box, accessible corner `p=(0,0,0)`, unchanged finite ordinary-NN/onsite two-qubit `H_P>=0`, and samples

```
C_j=a_j I+b_j X_p+c_j Y_p,
sqrt(b_j^2+c_j^2)<=a_j<=g,      a_j,b_j,c_j real.
```

Whole positivity of `H_P` does not supply a positive decomposition of each old local term. A consumer requiring that stronger block contract must supply and price it separately.

Put `c_j=(j,-1,-2)` and `u_j=(j,-1,-1)` for `0<=j<=n`; add auxiliary tail sites `a=(-1,0,0)`, `v_1=(-1,0,-1)`, `v_2=(-1,-1,-1)`. The auxiliary path is `a-v_1-v_2-u_0-...-u_n`. Declared edges are the clock path, auxiliary path, `c_j-u_j`, and `p-a`. They are all ordinary nearest neighbors outside the fixed old plant; no original factor is moved or assumed clean.

There are `n+1` clock sites, `m=n+4` auxiliaries, `2n+5` new sites and `3n+5` declared geometric edges; maximum new degree is three. This is a layout count, not a universal count of nonzero couplings. For zero endpoint samples or a scalar-only waveform, some or all source edges have zero coefficient. The declared layout can be connected while the nonzero interaction graph is not. The proof does not require universal dynamic connectedness.

For these coordinates the only new-to-old adjacency is `p-a`, and the displayed new-new adjacencies are the declared ones. The safe enlarged incidence allowance `6(|P|+2n+5)` is not an isolation certificate. All unlisted fields, environment couplings and faults must be absent, compensated or bounded on the actual full Hilbert space throughout preparation, release and runtime.

## 4. Response, nonscalar counterterm and bare-vacuum residual

On the full auxiliary space set `L_A=sum_v n_v-(1/12)sum_edges S_vw`. Its positive edge/onsite decomposition gives unique vacuum kernel and `L_A>=g_0 N_A`, with conservative `g_0=3/4` (the path supports `5/6`). Its exact norm is `m`, scalar `m/2`; the conservative allowance `ell_A=m+(n+3)/12` also suffices. The inverse `R` is the reduced inverse on every nonvacuum sector, not only one excitation.

On one excitation write `T_A=(I-Adj_A/12)^(-1)`, `t_j=(T_A)_(a,u_j)>=12^(-(j+3))`, and `gamma_a=(T_A)_(a,a)`, `gamma_j=(T_A)_(u_j,u_j)<=1/g_0`. For any supplied `q>0`, define

```
z_j=-(b_j+i c_j)/(2q t_j),
V=q(X_p X_a+Y_p Y_a)+sum_j n_(c_j)[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)],
C_ct=4q^2 gamma_a n_p+sum_j |z_j|^2 gamma_j n_(c_j),
A'=H_P+K_X'+sum_j a_j n_(c_j)+C_ct.
```

The port creation amplitude is `D=q(X_p+iY_p)`, with adjoint product `D†D=4q^2 n_p`. The actual counterterm is therefore an onsite operator, not an omitted scalar. With `J_A` appending auxiliary vacuum on the complete plant/one-clock-excitation domain,

```
J_A* V R V J_A=C_ct-W,        W=sum_j n_(c_j)(b_j X_p+c_j Y_p).
```

Distinct source-projector products vanish on `N_X=1`; on multiple heads they need not vanish. The complex sign and both port/source self-terms are retained.

Let `h>=||H_P||`, `v=2q+sum_j|z_j|`, `c_ct=4q^2 gamma_a+sum_j|z_j|^2 gamma_j`, `x=v/g_0`, `y=v^2/g_0^2`, and

```
a_*'=h+B_X'+(n+1)g+c_ct,        b_*'=h+B_X'+2(n+1)g,
F_1'=2x+tau[(a_*'+b_*')x+v y],  F_2'=2y+tau(a_*'+b_*')y.
K_Delta'=Delta L_A+sqrt(Delta)V+A'+R_pos I,   R_pos=sqrt(Delta)v.
```

The scalar reserve splits into positive shifted NN port/source blocks with reserves `2q sqrt(Delta)` and `sqrt(Delta)|z_j|`. All new terms have positive local decompositions. The full generator is positive with every auxiliary/clock sector included.

Set `epsilon=Delta^(-1/2)`, `X=RVJ_A`, `Y=RVX`, `Z=J_A-epsilon X+epsilon^2Y`. `Y` includes two auxiliary excitations. The exact residual is

```
(K_Delta'-R_pos I)Z-ZH_tar'
 =epsilon[VY-A'X+XH_tar']+epsilon^2[A'Y-YH_tar'].
```

All noncommuting products are kept. The two endpoint corrections cost `2(epsilon x+epsilon^2y)`. The full bare-input estimate is `eta_A'=F_1'/sqrt(Delta)+F_2'/Delta`, uniformly over the horizon. For prescribed `eta_med>0`, `Delta>=max(1,(2F_1'/eta_med)^2,2F_2'/eta_med)` suffices. This is a vacuum-input theorem, not a hidden dressed-state preparation.

The complete target at actual time `t` is

```
exp(-it R_pos)|vac_A> tensor chi_n'(t) tensor U_C(t),
eta_total'=L_C tau^2/sqrt(2n)+F_1'/sqrt(Delta)+F_2'/Delta.
```

Every plant, filler, reference, clock and auxiliary output is retained. Isometry error is at most `eta_total'`, and full trace error at most `min(2,2eta_total')`. At `tau` the mediator reserve phase remains; the adopted clock phase cancels exactly.

## 5. The exposed substitution changes the physical ledger

The root clock instead uses `K_X=Lambda N_X+sum_j w_j S_j`, `Lambda=Omega(n+1)`, with positive edges and separate `d_j n_j`. Its exact norm is `B_X=Omega(n+1)^2`, scalar `B_X/2`, and endpoint phase is `-i(-1)^n`. Those equations and its original `F_1,F_2` remain valid historical alternatives.

For the odd-site phase operator `Q=product_(j odd) Z_j`, the adopted clock satisfies `K_X'=Q K_X Q-Omega N_X`; the complete installed generators obey the same relation. The subtraction is a full-space number potential, not a free global scalar subtraction. Positivity of `K_X'` follows directly from the new positive edge blocks. Its source coefficients and geometry are unchanged, but its target, full norm, scalar, mean and residual constants are those explicitly primed above. If `Delta` is reselected, use the new `F_1',F_2'` and recompute all affected prices. An arbitrary correlated delivered input need not be `Q`-invariant; its replacement cost below applies before using the pure comparator.

The complete full-space norm allowance and normalized trace scalar are

```
B_full'=h+B_X'+(n+1)g+c_ct+Delta ell_A+sqrt(Delta)v+R_pos,
s_full'=s_(H_P)+B_X'/2+(sum_j a_j)/2+Delta m/2
                 +2q^2 gamma_a+(sum_j|z_j|^2 gamma_j)/2+R_pos.
```

Runtime action is at most `tau B_full'`. Positive-block, collected Pauli, scalar and state-energy budgets are distinct. At fixed `Delta`, the prepared clock mean decreases from the root form by `Omega`, its scalar by `Omega(n+1)/2`, and its exact full-clock norm by `Omega(n+1)`. An equal exact decrease of the interacting generator's norm is not asserted.

If `C(0)=0`, let `D_P=H_P+4q^2 gamma_a n_p`. On the ideal bare product input the exact static moments are

```
mean=Omega n+Tr(rho_P D_P)+R_pos,
variance=Var_rho(D_P)+Omega^2 n+4Delta q^2 Tr(rho_P n_p).
```

The covariance inside `Var_rho(D_P)` remains. The two fluctuations occupy orthogonal clock/auxiliary sectors. For nonzero initial sample add `a_0+|z_0|^2 gamma_0` to the diagonal mean operator and `Delta|z_0|^2` to the fluctuation term. Actual total moments are conserved by the static Hamiltonian; approximate comparator moments are not exact actual moments for imperfect controller inputs. The penalty estimate `Delta ell_A eta_A'^2` need not vanish.

The elementary bound `|z_j|<=g12^(n+3)/(2q)` permits potentially exponential mediator costs. The new clock does not make those old inverse-entry costs polynomial. No alternate polynomial-path construction is used. At fixed horizon the clock norm also grows quadratically in `n`; no fixed coupling cap, efficient search/synthesis, or resource refund follows.

## 6. Supplied thermal bit pattern and exact old marginal

Write `k=2n+5` and distinguish the preparation gap `nu_p>0` from runtime `Omega`. The disjoint onsite Hamiltonian

```
G_prep=nu_p[(I-n_(c_0))+sum_(j=1)^n n_(c_j)+sum_(v in A)n_v]
```

has the desired full controller bit string as its unique ground state, norm `nu_p k`, scalar `nu_p k/2` and gap `nu_p`. For a supplied full controller Gibbs marginal at `beta>0`, its exact infidelity is `delta_G=1-(1+exp(-beta nu_p))^(-k)<=k exp(-beta nu_p)`. Its unhalved marginal trace distance from the pure target is exactly `2delta_G`, even when the controller is correlated with the old plant/reference. Using that number as the full joint replacement cost additionally requires product independence. This corrects the root body's overly restrictive sentence about the marginal itself.

For completeness the general joint lemma is proved here, with no Markov premise. Let `sigma_CY` be arbitrary, `P_C=|c><c|`, `delta=1-Tr[(P_C tensor I)sigma]`, and `omega_Y=Tr_C sigma` the exact unconditioned old/reference marginal. Purify `sigma` and split the purification into orthogonal good/bad components of squared norms `1-delta,delta`. Subtract the unnormalized good block. On their span the difference has matrix `[[0,sqrt(delta(1-delta))],[sqrt(delta(1-delta)),delta]]`, of trace norm `sqrt(delta(4-3delta))`. After tracing the purifying reference, the additional difference between that good block and `P_C tensor omega_Y` is positive up to sign, with trace norm `delta`. Thus

```
||sigma_CY-P_C tensor omega_Y||_1
 <= g(delta):=delta+sqrt(delta(4-3delta)).
```

The endpoints are included. No normalized-success conditional marginal is substituted. A coherent purification of the full Gibbs diagonal, with an old reference copying each controller bit string, attains `g(delta_G)` and disproves extending `2delta_G` to arbitrary full correlated states. Product structure of the controller marginal is not independence from the old system.

If the delivered controller marginal is within half-trace distance `d` of that Gibbs state, use `delta_bar=min(1,k exp(-beta nu_p)+d)`. The full output price is `g(delta_bar)+2eta_total'` plus the actual physical perturbation, timing and release prices, capped at two. For exact delivery, `beta nu_p>=log(9k/epsilon_prep^2)` suffices for joint replacement allowance `epsilon_prep`, since `g(delta)<=3sqrt(delta)`. The weaker `log(2k/epsilon)` prescription addresses only marginal trace error. Fixed temperature/gap cannot keep the full growing controller arbitrarily pure.

If `e_prep=g(delta_bar)`, the exact ideal moment formulas above approximate actual imperfect-input moments only with errors at most `B_full' e_prep` for the mean, `B_full'^2 e_prep` for the second moment and `3B_full'^2 e_prep` for variance. These are full-norm-weighted bounds. They do not provide uniform rare-reference-conditioned moment control, returned energy or reuse.

## 7. Release, timing, work and whole-lifetime errors

The Gibbs clause supplies an equilibrium marginal for `G_prep`; it is not a cooling device or equilibration-time theorem. Runtime interactions must be absent, isolated or actually compensated while that source premise is asserted. Changing to the runtime generator is a separately supplied, priced operation.

In the principal positive case write `K_Delta'=H_P+F'`, with `F'>=0` through the displayed new blocks. A supplied smooth monotone release profile `u` on an actual interval of duration `s` can implement

```
H_rel(r)=H_P+(1-u(r))G_prep+u(r)F'.
```

This path is positive. Comparing it on the ideal pure controller to the fixed bit pattern and old state aged under `H_P` costs isometry error at most `||F'|| integral_0^s u(r)dr`. Charge the correlated replacement first. At runtime start the comparator old state is `exp(-is H_P)omega_Y exp(is H_P)`, and the later plant target is `U_C(t)exp(-is H_P)` on that marginal. Ignoring the release duration would omit real elapsed evolution. A nominal earlier old marginal is not restored by the exact-marginal lemma.

The release profile, finite slew, scalar action and work remain supplied. For monotone ideal closed-system release, drive work has magnitude at most `||F'-G_prep||`. General faults need their own endpoint or variation contract. The instantaneous switch is only a comparator; at `C(0)=0` its ideal energy jump is `Omega n+4q^2 gamma_a Tr(rho_P n_p)+R_pos`. A Gibbs-correlated actual input can have additional contributions bounded with the full operators. These mathematical work bounds do not identify a laboratory energy source or actuator.

An actual full-space perturbation `E(r)` adds `integral||E(r)||dr` in isometry norm and twice that in trace norm. For parameter calibration, comparison report(C8a) separately charges changes in `Delta`, `L_A`, `sqrt(Delta)V`, `A'` and `R_pos`. Leakage-producing faults require full-space bounds; sample errors have safe full-space sum `sum_j||Delta C_j||`, not just their maximum on one head. Fixed-target timing defects cost the actual full-generator norm times the timing error (or a separately justified invariant-sector norm). Positivity under calibration needs actual reserve margins. Scope includes all preparation/release/runtime isolation and every retained output.

## 8. Dependencies, evidence and remaining obligations

The one direct mathematical parent is the [single-port program/controller note](SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md), specifically its controller derivation `0e91f936…` and separate review `52eb2e2d…`. The actual 136,036-byte canonical note has SHA256 `9b08b7a78f21390d065322150d1fe6a222343323cc76dfe7f3b065a624d5a18e`; its proof occupies bytes `[79110,103180)` and its separate review `[103344,136036)`. It is published in regular PR 9617 at head `86eac8cc4523f7f15c8d84824f462f9a5c037806`. Their full-sector inverse/corrector and one-port contraction are reused at those exact intervals; this note proves the new clock, coordinates and changed constants. The parent's unrelated compiler or unary-clock ancestry is not a new direct import. Canonical parent identity and actual publication/attachment evidence are recorded in DEPENDENCIES and the parent binding, separately from this new note's future Git-base choice.

The earlier correlated-memory note `12bd18b0…` is provenance for the comparison's general `g` lemma; the complete argument is given in Section6 here. No Markov law, memory compression, finite-bank, Gibbs frontier or polynomial-mediator theorem is a mathematical dependency of this publication. Git ancestry creates no theorem edge.

The standard engineered spin-transfer mechanism is prior art. The original root reports reading the full four-page Christandl et al. paper, with failed publisher/screenshot attempts preserved; the protected author read only its public abstract after fixing the route. This wrapper performs no new literature search and claims no novelty for spin transfer. Its finite algebra and error proofs are supplied in the preserved sources. Prior source exposure and the same selected model/effort limit independence; the comparison is explicitly source exposed. This packaging adds no independent proof check, scientific execution or retained audit.

The vacuum clock fails to launch; multiple heads change the source algebra; wrong linear sample times change the waveform; deleting the root onsite potential without the explicit positive-edge replacement changes its motion; dropping the nonscalar counterterm changes the plant; an arbitrary matrix control is not literally two-local; a finite endpoint is not a permanent halt. These narrow witnesses remain, with no broader impossibility claim.

Native purity/cooling, known basis and initial energy coherence, installed positive interactions, calibration, release, isolation, detector/readout, physical energy identification, common caps, efficient synthesis and restoration/recycling remain open. A basis-state launch is a simpler supplied initialization contract within a finite Hamiltonian theorem, not a self-starting reusable apparatus. The scientific source acceptance and separately captured publication review remain distinct from actual integration, regular publication and independent retained audit. The selected stack base is PR 9618 on physics-loop/toe-local-gibbs-controller-source-20261015, used only as Git ancestry; it adds no theorem or state-supplier premise.


---

## Immutable source body: root_author

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# A finite waveform clock launched from a computational-basis state

Root analytic proposal, 2026-10-15. Not yet independently accepted or published. The independent worker received the target before this text and must freeze its own proof before reading this folder. Shared prior campaign context and the same model family limit independence. No numerical, symbolic or Lean science program is evidence for this note.

This uses the established engineered spin-transfer chain. The new task here is an explicit waveform-sampling estimate and its conditional controller interface, not a claim to have invented spin-transfer dynamics. Christandl, Datta, Ekert and Landahl, *Perfect state transfer in quantum spin networks*, arXiv:quant-ph/0309131v2, https://arxiv.org/abs/quant-ph/0309131v2, supplies relevant prior context. Root read the four-page PDF text through its references in two tool calls; the publisher fetch and a screenshot attempt failed and are not credited as successful reads. All finite algebra used below is supplied explicitly. No global novelty search or empirical realization is claimed.

## 1. Supplied waveform and complete target

Let P be a finite plant, with any retained reference B. H_P is a fixed self-adjoint plant Hamiltonian. Supply a self-adjoint waveform C:[0,tau]->End(P), tau>0, with operator Lipschitz constant L_C and finite norm bound. Let U_C solve i U_C'=(H_P+C(t))U_C, U_C(0)=I. The principal positive-control application has H_P>=0 and C(t)>=0. A signed H_P or signed sample needs an additional explicitly charged reserve if physical positivity is required.

Choose an integer n>=1 and L=n+1 clock qubits on an open nearest-neighbor path, indexed j=0,...,n. Write n_j=|1><1|_j and S_j=s_j^+s_(j+1)^-+s_j^-s_(j+1)^+=(X_j X_(j+1)+Y_j Y_(j+1))/2. The notation |j> means the full L-qubit computational basis vector with exactly one occupied site j. The initial clock is the known product state |0>, not the all-zero vacuum; in explicit bits it is |1,0,...,0>. No coherent wavepacket is supplied at the start.

The theorem concerns the complete isometry from arbitrary P and B inputs, including every clock output. It does not merely assert a reduced plant channel. Initial clock purity, installed coefficients and isolation are supplied conditions. Section9 states a separate finite-temperature product-source certificate, without claiming a cooling device.

## 2. Positive clock blocks on the entire qubit space

Set Omega=pi/(2 tau), Lambda=Omega(n+1),

    w_j=Omega sqrt((j+1)(n-j)),              0<=j<n,
    w_(-1)=w_n=0,
    d_j=Lambda-w_(j-1)-w_j,                 0<=j<=n.

Because each w_j<=Omega(n+1)/2, d_j>=0. Define

    K_X=sum_(j=0)^(n-1) w_j(n_j+n_(j+1)+S_j)
          +sum_(j=0)^n d_j n_j
       =Lambda N_X+sum_j w_j S_j.                              (1)

On a two-qubit edge the first block has eigenvalues0,0,2w_j,2w_j: the vacuum has0, the one-excitation symmetric/antisymmetric vectors have2w_j and0, and |11> has2w_j. It is positive with full-pair norm2w_j. The d_j n_j blocks are positive onsite terms. This is a physical sum of positive NN two-qubit and onsite blocks, not positivity proved only on a prepared sector.

The sum of their full-space norms is

    B_X=2 sum_j w_j+sum_j d_j=Lambda(n+1).                       (2)

The all-occupied state has K_X energy Lambda(n+1); hence ||K_X||=B_X exactly. The actual scalar, namely normalized full-qubit trace, is s_X=Lambda(n+1)/2. The absolute Pauli coefficient sum is B_X+sum_j w_j. Indeed the edge expansion is w_j I-w_j(Z_j+Z_(j+1))/2+w_j(XX+YY)/2, with absolute coefficient sum3w_j, and d_j n_j has coefficient sum d_j. These physical norms/scalars cannot be replaced by the smaller one-excitation norm or by a removed identity phase. The incident block load at an interior clock site is at most2(w_(j-1)+w_j)+d_j<=2Lambda; endpoints obey the same bound. There are n edge and n+1 onsite blocks.

## 3. Exact clock motion from the endpoint

N_X is conserved. On its one-excitation subspace K_X is Lambda I plus the tridiagonal matrix with entries w_j. Introduce a proof-only space of n spin-1/2 factors, and normalized symmetric vectors D_j with j occupied factors. The sum Omega sum_(r=1)^n X_r has matrix element Omega sqrt((j+1)(n-j)) between D_j and D_(j+1): count the n-j choices of an unoccupied factor and the binomial normalizations. Its symmetric subspace is invariant, so the map |j>->D_j intertwines the two tridiagonal matrices. This is a proof device, not n additional physical qubits or a performed nonlocal unitary.

Since the proof-only X_r commute,

    exp[-it Omega sum_r X_r]|0>^tensor n
       =[cos(Omega t)|0>-i sin(Omega t)|1>]^tensor n.

Thus the actual physical free-clock vector is

    chi_n(t)=exp(-it K_X)|0>
      =exp(-it Lambda) sum_(j=0)^n sqrt(binomial(n,j))
          [cos(Omega t)]^(n-j)[-i sin(Omega t)]^j |j>.           (3)

For0<=t<=tau its position law is Bin(n,p(t)), p(t)=sin^2(Omega t), and at tau,

    chi_n(tau)=exp(-i Lambda tau)(-i)^n |n>.                    (4)

All phases in(3)-(4) belong to the full isometry. They are not dropped by identifying a clock probability distribution. The single-site endpoint product state at the end is a useful special case; during the run the full coherent clock vector is retained.

## 4. Sampling a continuous waveform: a uniform finite bound

Define sample times

    t_j=Omega^(-1) arcsin sqrt(j/n),       C_j=C(t_j),
    V_XP=sum_(j=0)^n n_j tensor C_j,
    H_tar=K_X tensor I_P+I_X tensor H_P+V_XP.                   (5)

For arbitrary plant matrices, (5) is an explicitly supplied occupation-controlled interface. The clock itself is local two-qubit; (5) alone does not make arbitrary C_j local or physically adjacent. The later single-port specialization addresses this distinction.

Here is the load-bearing mean-square estimate, uniform even at the two endpoint times. Let J~Bin(n,p), X=J/n, and theta=arcsin sqrt(p). For x,p in[0,1], the unit vectors v(x)=(sqrt(1-x),sqrt(x)) and v(p) subtend angle |arcsin sqrt(x)-theta|<=pi/2. Their chord length is2 sin(angle/2). On[0,pi/4], concavity gives sin u>=(2sqrt(2)/pi)u, so

    |arcsin sqrt(x)-theta|^2 <=(pi^2/8)||v(x)-v(p)||^2.

For0<p<1,

    E(sqrt(X)-sqrt(p))^2 <= E(X-p)^2/p=(1-p)/n,
    E(sqrt(1-X)-sqrt(1-p))^2 <= E(X-p)^2/(1-p)=p/n.

The denominators arise from (sqrt(X)+sqrt(p))^2>=p and its complement, so these inequalities require no Gaussian approximation or large-n limit. At p=0 or1 the binomial is deterministic and the time error is zero. Therefore

    E|t_J-t|^2 <= pi^2/(8 Omega^2 n)=tau^2/(2n),
    for every0<=t<=tau.                                         (6)

Let J_0 embed plant inputs as |0> tensor input. The comparison map F(t)=chi_n(t) tensor U_C(t) obeys

    (i d/dt-H_tar)F(t)
      =sum_j <j|chi_n(t)> |j> tensor [C(t)-C_j]U_C(t).

Orthogonality of physical |j> and the operator Lipschitz hypothesis yield norm at most L_C sqrt(E|t_J-t|^2)<=L_C tau/sqrt(2n). Integrate the exact Duhamel identity against the unitary propagator of H_tar, with F(0)=J_0, to obtain

    ||exp(-it H_tar)J_0-chi_n(t) tensor U_C(t)||
       <= L_C tau t/sqrt(2n) <= L_C tau^2/sqrt(2n).             (7)

This is an operator norm on maps from the entire plant space; tensoring any reference identity preserves it. For any input density matrix, the complete output trace error is at most twice(7), capped at2. There is no assumption that the actual joint evolution stays factorized, and no replacement of actual clock trajectories by classical random control. The proof directly bounds the joint vector.

Any n>=max(1,ceil(L_C^2 tau^4/(2 eta_X^2))) gives uniform isometry error eta_X. If L_C=0, the waveform is constant, all C_j equal, and the factorization is exact on N_X=1. One can allow a known modulus of continuity instead, but no such extension is needed for this claim. An arbitrary discontinuous waveform is not asserted to satisfy(7).

If C(t)=0 on[T,tau], then the ideal plant ages exactly as exp[-i(t-T)H_P]U_C(T) throughout that interval, with the actual clock chi_n(t) still retained. This gives a paid finite output window if tau>T. It does not halt the free clock at tau: the spin rotation recurs and then reverses its position sweep. Extending the theorem beyond tau requires a separate schedule/error argument. There is no permanently frozen output or free clock recycling.

## 5. Positivity, physical norms, moments and calibration at the interface

If H_P>=0 and each C_j>=0, H_tar>=0. A generic supplied signed matrix needs a sufficient real reserve, added as an actual physical term and included in the scalar/norm/work ledger. For ||H_P||<=h and C_*>=max_j||C_j||,

    ||H_tar|| <= h+B_X+sum_j||C_j|| <=h+B_X+(n+1)C_* .           (8)

For a single plant-qubit sample C_j=a_j I+b_j X_p+c_j Y_p, with0<=a_j<=g and sqrt(b_j^2+c_j^2)<=a_j, its norm is at most2g and the whole physical scalar in(5) is s_(H_P)+s_X+(1/2)sum_j a_j. Each n_j C_j is positive and two-qubit, but geometrically nonlocal to one common port; this geometric obligation is not hidden by its algebraic support count.

At initial clock |0>, the exact interface moments are

    mean(H_tar)=Lambda+Tr rho_P(H_P+C_0),
    Var(H_tar)=Var_rho(H_P+C_0)+Omega^2 n.                       (9)

To verify this, apply H_tar to |0> tensor input: its clock0 component is (Lambda I+H_P+C_0)input, and its sole orthogonal clock1 component is w_0 input. Since w_0^2=Omega^2 n, the second moment splits as asserted. Correlations inside rho_P or with a reference are unrestricted. In a static realization the actual total moments are conserved. These are moments of the written Hamiltonian, not a microscopic energy or detector identification.

A perturbation E(t) of the entire installed generator adds at most integral_0^t||E(s)||ds in isometry norm and twice that in complete-state trace norm. With sample errors Delta C_j, the full-space budget is sum_j||Delta C_j||, although their restriction to N_X=1 is only max_j||Delta C_j||; a hardware or number-leakage certificate must use the relevant full space. Edge and onsite errors have their own actual norm sums. Reserves needed to restore positivity of faulty blocks are physical costs. Timing error relative to a fixed nominal endpoint is bounded by ||H_actual|| |Delta t| in vector norm, with all scalars retained; a finite waveform window does not erase clock timing or old-system aging.

No common fixed coupling cap is claimed: Lambda grows like n/tau, B_X like n^2/tau, and increasingly accurate simulation may require larger n and more precise coefficients. At fixed local peak cap one must change the duration/design and re-evaluate(7); holding tau fixed while increasing n is not free.

## 6. Explicit outside-plant geometry for the single-port interface

This section is an adaptation of the separately checked single-port mediator source0e91f936/assessment52eb2e2d/root acceptance134cbee6. Those remain provisional scientific sources until their regular milestone is published and independently audited. The changed clock/geometry is proved here; no new original-plant locality or positive-local-decomposition premise is inferred.

Suppose the finite plant sits in a nonnegative-coordinate lattice box, with accessible corner p=(0,0,0), and its unchanged H_P has allowed onsite/nearest-neighbor two-qubit terms and whole-space positivity. Its other/filler/old-reference factors are arbitrary. Place clock sites c_j=(j,-1,-2), auxiliary sites u_j=(j,-1,-1), j=0,...,n, and extra auxiliary sites

    a=(-1,0,0), v_1=(-1,0,-1), v_2=(-1,-1,-1).

The auxiliary path is a-v_1-v_2-u_0-u_1-...-u_n, so m=n+4 auxiliary sites and e_A=n+3 auxiliary edges. The clock is its parallel open path; the occupation-controlled source edges are c_j-u_j; the sole plant-controller edge is p-a. Every declared edge is ordinary nearest neighbor. Every new site lies outside the plant box. The declared new graph has2n+5 sites,3n+5 edges and maximum new degree3. All unused geometric adjacency and onsite drifts are either absent, compensated or charged by a supplied actual full-space isolation certificate; a safe edge count for the enlarged occupied set is6(|P|+2n+5). This count is an upper bound, not permission to ignore a physical coupling.

Let B_A=I-Adj_A/12 on the auxiliary one-excitation space, and T_A=B_A^(-1). Since the path degree is at most2, B_A>=5I/6 and the conservative g_0=3/4 is valid. The positive Neumann series gives

    t_j=(T_A)_(a,u_j)>=12^(-(j+3)),
    gamma_a=(T_A)_(a,a), gamma_j=(T_A)_(u_j,u_j)<=1/g_0.

On the full auxiliary spin space define

    L_A=sum_v n_v-(1/12)sum_(v,w) S_vw.

The operator inequality +/-S_vw<=n_v+n_w proves L_A>=g_0 N_A, with unique zero vector |vac_A>. It has a positive two-qubit/onsite decomposition: edges (n_v+n_w-S_vw)/12 and onsite (1-deg(v)/12)n_v. Its scalar is m/2; a conservative full norm bound is ell_A=m+e_A/12. In fact its positive-block norm sum is m, but the conservative ell_A bound can be used consistently below. The full reduced inverse R=(L_A|_(vac_A perpendicular))^(-1)Q has norm at most1/g_0. This is not an inverse restricted only to one excitation.

Choose q>0, and for each sampled control let

    z_j=-(b_j+i c_j)/(2q t_j),
    V=q(X_p X_a+Y_p Y_a)
        +sum_j n_(c_j)[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)],
    C_ct=4q^2 gamma_a n_p+sum_j |z_j|^2 gamma_j n_(c_j),
    H_b=H_P+K_X+sum_j a_j n_(c_j),        A=H_b+C_ct.             (10)

V is a sum of physical NN two-qubit terms. The counterterm C_ct is an actual positive onsite operator, not an identity subtraction. Let J_A append the auxiliary vacuum and restrict the clock to N_X=1. Auxiliary creation at the port is q(X_p+iY_p); at u_j it is z_j n_(c_j). Multiplying the resolvent matrix elements gives exactly

    J_A^* V R V J_A=C_ct-W,
    W=sum_j n_(c_j)(b_j X_p+c_j Y_p).                            (11)

The port square is4q^2 gamma_a n_p, not a scalar. Distinct clock-projector products vanish on N_X=1. The complex cross term is2q t_j[Re z_j X_p+Im z_j Y_p]=-(b_j X_p+c_j Y_p). These calculations fix both the Y sign and the counterterm. On several clock excitations cross terms need not vanish; that sector is not claimed to implement the sampled program.

Set

    v=2q+sum_j |z_j|,
    c_ct=4q^2 gamma_a+sum_j |z_j|^2 gamma_j,
    a_*=h+B_X+(n+1)g+c_ct,
    b_*=h+B_X+2(n+1)g,
    x=v/g_0, y=v^2/g_0^2,
    F_1=2x+tau[(a_*+b_*)x+v y],
    F_2=2y+tau(a_*+b_*)y.                                      (12)

All these numbers are finite and computable from the promised inputs. For example |z_j|<=g12^(n+3)/(2q) is a crude sufficient bound, demonstrating explicitly that the nearest-neighbor completion can be extremely costly.

For Delta>0 form the actual static generator

    K_Delta=Delta L_A+sqrt(Delta)V+A+R_pos I,
    R_pos=sqrt(Delta)v.                                         (13)

It is positive on the full qubit space. V can itself be implemented by positive shifted edge blocks, with reserves2q sqrt(Delta) at p-a and sqrt(Delta)|z_j| at c_j-u_j, summing to R_pos. The preexisting H_P is only assumed whole-positive; separate positive blocks for its old terms require their own supplied decomposition/cost. The new L_A, K_X, a_j and counterterm terms already have positive local decompositions.

## 7. Bare-input mediator estimate and complete waveform result

For clarity, the finite corrector proof is repeated. With epsilon=Delta^(-1/2), X=R V J_A, Y=R V X and Z=J_A-epsilon X+epsilon^2Y, vacuum number parity implies X has one auxiliary excitation and Y has two. In particular the vacuum part of VX is exactly J_A(C_ct-W), and R removes it. The identities L_A X=VJ_A and L_A Y=QVX give

    (K_Delta-R_pos I) Z-Z H_tar
       =epsilon[VY-AX+XH_tar]
          +epsilon^2[AY-YH_tar].                               (14)

Here H_tar is precisely(5) on the clock-one-excitation/plant space. A preserves the auxiliary vacuum and N_X. Use ||X||<=x, ||Y||<=y, ||A||<=a_*, ||H_tar||<=b_*; boundary corrections cost2(epsilon x+epsilon^2y). Integrating the residual with the two unitary groups proves, uniformly0<=t<=tau,

    ||exp(-itK_Delta)J_A
       -exp(-itR_pos)J_A exp(-itH_tar)||
       <= eta_A:=F_1/sqrt(Delta)+F_2/Delta.                      (15)

For a specified eta_med>0 it suffices to take Delta>=max(1,(2F_1/eta_med)^2,2F_2/eta_med). This uses bare vacuum input, not a hidden dressed low-energy encoding. The finite two-excitation corrector is included rather than discarded on a one-excitation-only argument.

Combining(7),(15), the complete physical map from the supplied product input |vac_A>|0> is within

    eta_total=L_C tau^2/sqrt(2n)+eta_A                           (16)

of exp(-itR_pos)|vac_A> tensor chi_n(t) tensor U_C(t), uniformly at the same actual elapsed t. All original plant/reference outputs and clock/auxiliary outputs remain. At tau the ideal clock is the known endpoint bit vector with phase exp(-i Lambda tau)(-i)^n. Trace error is at most2 eta_total, capped at2. Any separately checked external compiler target can be substituted for U_C only at its stipulated actual time/window with its own error and scalar phases; this theorem does not retroactively assert its intermediate plant history.

The full-space bound and physical scalar in this realization are

    B_full=h+B_X+(n+1)g+c_ct+Delta ell_A+sqrt(Delta)v+R_pos,
    s_full=s_(H_P)+Lambda(n+1)/2+(1/2)sum_j a_j+Delta m/2
             +2q^2 gamma_a+(1/2)sum_j |z_j|^2 gamma_j+R_pos.     (17)

A runtime action bound is tau B_full, and each installed block/Pauli channel has its own positive reserve and full-space norm as displayed above. These bounds include all auxiliary and clock sectors, even though the valid program input lies in one clock sector. Strong couplings, calibration precision, lifetime isolation and finite occupied size are not treated as free.

If C(0)=0, then a_0=b_0=c_0=z_0=0. On the bare product clock/auxiliary input, put D_P=H_P+4q^2 gamma_a n_p. The exact actual initial moments are

    mean(K_Delta)=Lambda+Tr rho_P D_P+R_pos,
    Var(K_Delta)=Var_rho(D_P)+Omega^2 n
                      +4Delta q^2 Tr rho_P n_p.                (18)

The first additional variance comes from the clock edge |0>->|1>; the second from creating an auxiliary excitation at a. They occupy orthogonal clock/auxiliary sectors, so no cross term is suppressed by an independence assumption. Covariance inside Var_rho(D_P) is retained. For a nonzero starting sample, use the complete diagonal A block at clock0 and add Delta[4q^2 Tr rho n_p+|z_0|^2] instead. The actual static total moments are conserved. Small leakage probability does not imply negligible penalty energy: the probability bound eta_A^2 gives at most Delta ell_A eta_A^2 for the associated penalty contribution, which need not vanish as Delta grows.

## 8. Counterexamples and scope boundaries

The all-zero clock is an eigenstate of K_X and makes every n_j C_j zero; it does not launch the waveform. The correct initial bit at the first site matters. Multiple clock excitations change the sampled-source cross terms, so arbitrary clock states are not covered by a clock-one-sector simulation claim. Even with correct input, the free spin chain is periodic and does not provide a permanent halt. Starting with a clock probability distribution matching(3) but without its coherence does not imply the full isometry target; the derivation uses the exact unitary amplitude vector.

Omitting the onsite d_j terms generally adds a nonuniform clock potential, invalidating the binomial formula. Dropping Lambda N_X changes the actual positive generator and its physical scalar/phase, even though it is a scalar on one valid sector. Likewise omitting C_ct leaves a real plant n_p detuning. The previously preserved single-port counterterm and XX-only/complex-drive witnesses apply to the same source algebra(11). These are narrow shortcut failures, not a general no-go theorem for other clocks or controllers.

The scalar reserve R_pos is substantial and real. An approximate vector output does not erase it from energy moments, full-space calibration or work. Switching any of these installed generators, or removing/preparing the clock, requires its own actual schedule and endpoint Hamiltonians. None of the constructions changes physical axioms, assigns a microscopic energy observable, manufactures a finite detector, or supplies unlimited reset/reuse.

## 9. A simpler supplied preparation state, with explicit purity cost

The complete nominal controller input in(16) is a computational-basis product over L+m=2n+5 qubits. It is the unique ground vector of the positive onsite Hamiltonian

    G_prep=nu[(I-n_(c_0))+sum_(j=1)^n n_(c_j)+sum_(v in A) n_v],
    nu>0.                                                       (19)

For a supplied full Gibbs marginal of this disjoint onsite Hamiltonian at beta>0, the exact correct-bit probability is[1+exp(-beta nu)]^(-(2n+5)), and its total infidelity delta is at most(2n+5)exp(-beta nu). Its full marginal trace error from the ideal product is2delta. All controller-sector errors are accounted for by this probability, rather than postselecting N_X=1.

For arbitrary initial correlations with the old plant/reference, use the separately accepted complete retained-marginal lemma from correlated-memory note12bd18b0: a pure-controller overlap1-delta implies full joint replacement error at most g(delta)=delta+sqrt(delta(4-3delta)), with delta capped at1 and the exact unconditioned old marginal retained. A delivered marginal half-trace error d adds at most d to the infidelity before applying g. Then add2eta_total and actual physical perturbation errors. The smaller2delta marginal bound is valid for an independently supplied product input, not for arbitrary old-reference correlations.

G_prep has full norm nu(2n+5), scalar nu(2n+5)/2 and all-sector gap nu; its ground energy is0. For a target marginal trace error epsilon, beta nu>=log(2(2n+5)/epsilon) suffices. This is an elementary finite product-Gibbs certificate, not an autonomous preparation or cooling process. Runtime interactions must be absent, isolated or physically compensated while asserting that Gibbs marginal, and their release must preserve actual chronology with paid error/work. The actual product-state source is substantially simpler than a specified coherent Fourier packet, but it remains a supplied resource. This note establishes no bath, equilibration time, native actuator or self-initializing cycle.

## 10. Verification status and next decision

The root derivation is analytic. Its critical new claim is the full-isometry sampling bound(6)-(7) for a positive engineered clock starting in a known bit pattern. Existing spin-transfer machinery is proved in the finite representation used here; the mediator completion is checked algebraically with explicit changed geometry and retained provisional source identities. The independent worker is deriving the clock target without access to this candidate. No acceptance is inferred before its complete proof and subsequent comparison are read. The remaining decision is whether the sampling constants, full-space positivity and interface adaptation survive that check; actual state supply, physical identification, common caps and reusable detection remain open.


---

## Immutable source body: independent_author

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# A positive weighted-path clock from a computational-basis endpoint

Status: independent pre-exposure derivation for a supplied finite Hamiltonian interface. This is an author proof, not an independent audit or a claim of native initialization. The root basis-state-clock candidate has not been opened, listed, hashed, searched, or read. Earlier accepted unary-clock and controller sources were already known; the elementary construction and estimates below are derived here. No scientific program was run.

## 1. Quantified question and precise conclusion

Let the plant Hilbert space P have finite dimension d, let H0 be any supplied Hermitian operator on P, and let tau>0. Let C:[0,tau]->Herm(P) be supplied with

    ||C(t)|| <= B,     ||C(t)-C(s)|| <= L |t-s|,
    C(0)=C(tau)=0,     B,L < infinity.

Norms are operator norms unless explicitly stated otherwise. The Hermitian condition is necessary for the claimed unitary Hamiltonian simulation; “arbitrary matrix waveform” cannot include non-Hermitian generators without changing the target. No commutation among H0 and the matrices C(t) is assumed. Denote the exact time-ordered plant propagator by

    i dU(t)/dt = [H0+C(t)] U(t),     U(0)=I.

For every integer m>=1 there is an explicitly given positive clock Hamiltonian on a path of m+1 physical qubits, with m nearest-neighbor two-qubit positive terms. Its initial state is the known computational-basis product state |10...0>. On the supplied static occupation-control interface, a positive time-independent joint generator K realizes the complete output isometry V(t), and an explicitly phased comparison isometry Vref(t), with

    ||V(t)-Vref(t)|| <= L tau t / sqrt(m),    0<=t<=tau.       (1)

At time tau the reference clock is the computational-basis product state |0...01>. Both the clock and the entire plant, together with every untouched reference, remain in the comparison. The induced full-output channels have diamond-norm difference at most

    2 L tau t / sqrt(m).                                      (2)

In particular, m=max(1,ceil[(2 L tau^2/epsilon)^2]) suffices for unperturbed full-output trace/diamond error epsilon at every time in the horizon. This is a sufficient recipe, not a minimum-size claim. A calibrated implementation has the additional explicitly paid errors in Section 8.

The clock terms themselves are positive nearest-neighbor two-qubit operators. For arbitrary matrix C_j on a general plant, the supplied couplings sum_j n_j tensor C_j are not automatically two-local or geometrically nearest-neighbor. A further gadget or routing theorem is needed for that stronger whole-device claim. The present theorem answers the clock-interface question and does not silently assert the stronger locality contract. Section 10 gives an exact distinction.

Pure computational-basis initialization is still supplied. The result removes a supplied coherent spatial wavepacket from this clock interface; it does not derive purity, preparation work, a native controller, a spatial basis reference, permanent stopping, or reuse from the axioms.

## 2. Explicit positive nearest-neighbor clock

Label the clock qubits j=0,...,m along a path. Write

    n_j=(I-Z_j)/2,
    S_j=(X_j X_{j+1}+Y_j Y_{j+1})/2,
    N=sum_{j=0}^m n_j,
    nu=pi/(2 tau),
    a_j=nu sqrt[(j+1)(m-j)],              0<=j<m.

Define the physical edge terms

    G_j=nu[(m-j)n_j+(j+1)n_{j+1}
               -sqrt((j+1)(m-j)) S_j],
    G=sum_{j=0}^{m-1} G_j.                                  (3)

Every G_j acts on exactly the two adjacent clock qubits; the one-site operators displayed in (3) are embedded in that two-qubit block. On |00>, G_j is zero. On the ordered basis |10>,|01>, its matrix is

    nu [ m-j                    -sqrt((j+1)(m-j)) ]
       [ -sqrt((j+1)(m-j))       j+1              ].

This matrix has determinant zero and trace nu(m+1), so its eigenvalues are 0 and nu(m+1). On |11> the eigenvalue is nu(m+1). Thus

    spec(G_j)={0,0,nu(m+1),nu(m+1)},
    G_j>=0,     ||G_j||=nu(m+1).                            (4)

This proves positivity on every local sector, not only in the one-excitation sector. Summing the diagonal coefficients gives exactly m at every path vertex: at an internal vertex j, the two contributions are j and m-j, and each endpoint receives m. Therefore

    G=nu m N - sum_{j=0}^{m-1} a_j S_j.                     (5)

It commutes with N. Its norm on the full 2^(m+1)-dimensional clock space is exactly

    ||G||=nu m(m+1).                                        (6)

The sum of the m local norm bounds gives the upper bound; the all-ones computational state attains it because every G_j has eigenvalue nu(m+1) there. The vacuum is a zero-energy state. These facts avoid an inference of full-clock positivity or norm from a favorable restricted sector.

The initial physical clock is |e_0>=|10...0>. Let |e_j> denote the single-excitation basis state with its one at vertex j. Restricted to N=1,

    G_1=nu m I - nu T_m,
    <e_{j+1}|T_m|e_j>=sqrt((j+1)(m-j)),                     (7)

with all other nonadjacent entries zero. The initial clock is a pure product in the computational basis, but is not an energy eigenstate. Its energy coherence is a resource relative to G; calling the state a basis state does not remove that resource.

## 3. Exact free evolution without a wavepacket premise

For an elementary proof of the restricted propagator, use m virtual two-level factors only as a mathematical representation. They are not extra physical clock qubits. Let |D_j> be the normalized sum of virtual computational strings with Hamming weight j. Directly counting the raising and lowering incidences gives

    <D_{j+1}| sum_{r=1}^m X_r |D_j>
        =sqrt((j+1)(m-j)).                                  (8)

For example, each weight-j string has m-j possible upward flips, each weight-(j+1) string has j+1 predecessors, and normalization by the two binomial counts gives (8). The symmetric subspace is invariant. The map |D_j> -> |e_j> identifies its sum-X operator with T_m.

Since distinct virtual X_r commute,

    exp(i nu t sum_r X_r)|0...0>
        = [cos(nu t)|0>+i sin(nu t)|1>] tensor-power m.

Consequently the exact physical free clock state is

    |g_t> = exp(-iGt)|e_0>
      = exp(-i nu m t) sum_{j=0}^m sqrt(binomial(m,j))
           cos(nu t)^(m-j) [i sin(nu t)]^j |e_j>.           (9)

For 0<=t<=tau the trigonometric factors are nonnegative before the written powers of i. The position variable J_t has exactly the law

    J_t ~ Binomial(m,p_t),     p_t=sin^2(nu t).              (10)

This is not a presumed law for the interacting clock. It is the exact freely evolving comparison state used in a Duhamel estimate below. Back-action is included in the resulting joint error bound.

At the endpoint nu tau=pi/2. The phase exp(-i nu m tau) exactly cancels i^m, and hence

    |g_tau>=|e_m>.                                          (11)

No clock phase has been discarded. Intermediate phases in (9) are also retained. The restricted spectrum is {0,2nu,...,2nu m}, by diagonalizing sum_r X_r on its symmetric subspace; in particular

    ||G_1||=2nu m.                                         (12)

The proof through virtual spins is a representation identity, not a physical assumption of m independent clocks.

## 4. Nonlinear sample times and a uniform concentration bound

Store the waveform at the finite set of times

    s_j=(1/nu) arcsin sqrt(j/m)
       =(2 tau/pi) arcsin sqrt(j/m),     C_j=C(s_j).         (13)

Thus s_0=0, s_m=tau, C_0=C_m=0. Linear times tau*j/m would not follow the actual motion; Section 10 supplies a narrow failure witness.

The load-bearing probability estimate is

    E |s_{J_t}-t|^2 <= tau^2/m,    0<=t<=tau.               (14)

Here is a direct proof, including the endpoints. Write p=p_t and Q=J_t/m. For 0<p<1, Var(Q)=p(1-p)/m and

    E (sqrt(Q)-sqrt(p))^2
      = E (Q-p)^2/(sqrt(Q)+sqrt(p))^2 <= (1-p)/m,

    E (sqrt(1-Q)-sqrt(1-p))^2 <= p/m.                       (15)

The two unit vectors u(q)=(sqrt(1-q),sqrt(q)) lie in the first quadrant. Their angle difference is

    delta=|arcsin sqrt(q)-arcsin sqrt(p)| <= pi/2.

Their squared chord length is 4 sin^2(delta/2). The elementary concavity bound sin x >= 2x/pi on [0,pi/2] gives

    delta^2 <= (pi^2/4) ||u(q)-u(p)||^2.                    (16)

Combining (15) and (16) yields E delta^2 <= pi^2/(4m). Dividing by nu^2 proves (14), since nu=pi/(2tau). At p=0 or p=1, Q=p deterministically and the left side is zero, so no division by zero is used. This proof does not assume stationarity, a supplied mixing time, a central-limit limit, or an asymptotic approximation at the endpoints.

The singular derivative of arcsin sqrt(q) at q=0,1 therefore does not spoil this mean-square estimate. A crude global Holder estimate would give a weaker power; (15) uses the corresponding vanishing binomial variance. The stated constant is conservative and sufficient.

## 5. Positive static joint generator and complete output target

Choose a supplied scalar h>=max(0,-lambda_min(H0)); h=||H0|| is one safe finite choice. Choose B>=sup_t||C(t)|| as above. Set

    K=G tensor I_P + I_C tensor (H0+hI_P)
         + sum_{j=0}^m n_j tensor (C_j+B I_P).              (17)

Every term displayed in (17) is positive: the clock terms by (4), the plant block by the choice of h, and each controlled term because C_j+B I_P>=0. Thus K>=0 on the entire clock/plant Hilbert space. Its static coefficients encode the supplied waveform; after initialization no runtime externally timed drive occurs in this finite model.

The assertion H0+hI>=0 concerns the whole supplied plant block. It does not certify that a previously chosen decomposition of H0 into individual local terms has positive members. A consumer requiring separately positive local plant blocks needs that decomposition and its own local reserves, with the corresponding scalar and action costs.

For later comparison absorb the constant B number shift into the free clock:

    |kappa_t>=exp[-it(G+B N)]|e_0>
             =exp(-iBt)|g_t>.

The operator G+B N is itself a positive nearest-neighbor clock Hamiltonian. If all clock terms must be presented as two-qubit blocks rather than with separate on-sites, distribute B n_j equally among its one or two incident path edges. Adding these positive on-site parts to G_j preserves positivity and changes no operator. The controlled blocks in (17), rather than the signed bare C_j pieces separately, are the positive joint decomposition. This accounting adds B N exactly once.

Let J:P->C tensor P be J|psi>=|e_0> tensor |psi>. Define the actual and reference isometries

    V(t)=exp(-itK)J,
    Vref(t)|psi>=exp(-iht)|kappa_t> tensor U(t)|psi>.         (18)

Both use the same actual elapsed time t and the complete supplied H0. No part of H0 is silently paused, omitted, or commuted through the drive. The reference is a phased full-clock state, not just a position distribution or an expectation of n_j.

At t=tau,

    Vref(tau)|psi>
       =exp[-i(h+B)tau]|e_m> tensor U(tau)|psi>.             (19)

The scalar part of C(t), if present, remains in the exact time-ordered U(t), including its phase. It is not absorbed into an unspecified equivalence. The constant h and B phases in (18)-(19) are also explicit. A comparison of channels can be insensitive to a common phase; the stronger isometry statement here does not use that insensitivity.

## 6. Dimension-independent error derivation with all outputs retained

The reference isometry solves the time-dependent equation with generator

    Kref(t)=G+B N+(H0+hI_P)+I_C tensor C(t).

On its clock support N=1, sum_j n_j=I. Its residual under the actual generator is therefore

    [K-Kref(t)]Vref(t)
      =exp(-iht) sum_j <e_j|kappa_t>|e_j>
           tensor [C_j-C(t)]U(t).                          (20)

For any plant vector psi, the clock summands are orthogonal. Thus

    ||[K-Kref(t)]Vref(t)psi||^2
      =sum_j Pr(J_t=j) ||[C(s_j)-C(t)]U(t)psi||^2
      <=L^2 E|s_{J_t}-t|^2 ||psi||^2
      <=(L^2 tau^2/m)||psi||^2.                            (21)

The same calculation holds after tensoring every operator with the identity on an arbitrary finite reference; no dimension factor is introduced. It does not replace an operator by its mean. In particular it does not assume that the actual interacting clock remains in (9).

Differentiating exp[-iK(t-s)]Vref(s) and integrating gives the exact variation-of-constants identity. Since the left propagator is unitary and V(0)=Vref(0)=J,

    ||V(t)-Vref(t)||
      <= integral_0^t ||[K-Kref(s)]Vref(s)|| ds
      <= L tau t/sqrt(m),                                  (22)

which proves (1). Noncommuting H0, C(s), and C(t) are already covered by U(t) and its unitarity; no scalar or commuting approximation enters this proof.

For any reference R and any density operator rho_PR, including entangled or classically correlated inputs,

    || (V(t) tensor I_R) rho_PR (V(t)^* tensor I_R)
      -(Vref(t) tensor I_R) rho_PR (Vref(t)^* tensor I_R) ||_1
       <=2 ||V(t)-Vref(t)||.                               (23)

For example, expand the difference into one factor V-Vref on each side and use trace norm submultiplicativity and isometry norm one. This proves the factor c_ch=2 in the full-output diamond bound. Trace distance defined with a prefactor 1/2 would instead be bounded by the isometry error. We use unhalved trace norm throughout (2) and (23).

The plant includes all memory and filler systems on which the stated H0 and C act. No plant subsystem, clock output, measurement record, or reference is discarded in (23). At the endpoint, the amplitude outside the final clock basis state is bounded by eta=L tau^2/sqrt(m):

    ||[(I-|e_m><e_m|) tensor I_P]V(tau)||<=eta.              (24)

Hence the unconditional probability of a non-final clock position is at most eta^2, for every input. This is not a postselection argument. The complete joint state, including the unsuccessful amplitude, is the state compared in (23).

## 7. Endpoint guards and an optional final idle interval

Zero endpoints give C_0=C_m=0 exactly. At both endpoint comparison states the nonscalar plant-drive coupling vanishes; B n_j at that endpoint is only a clock potential. The interaction has no dependence on the plant there. At time tau the reference clock is exactly |e_m>, and the actual residual coupling/back-action is included in (22), not assumed absent.

If C(t)=0 for T<=t<=tau, choose the same sample times (13). All samples with s_j>=T are zero. Let p_T=sin^2(nu T). For any s>T with p_s>p_T, the comparison probability on potentially nonzero program sites obeys

    Pr(s_{J_s}<T)
       <= Var(J_s/m)/(p_s-p_T)^2
       <= 1/[4m(p_s-p_T)^2],                               (25)

with the trivial upper bound 1 understood. This is Chebyshev's inequality applied to the actual free binomial law. At s=tau it is zero exactly. It is only a supplementary guard estimate; the uniform full-output error remains (22), even near T where (25) is uninformative. The actual state has projected amplitude at most sqrt(the free probability)+L tau s/sqrt(m), by the isometry bound.

The clock has not been permanently stopped. Its N=1 propagator returns at 2tau, and it will revisit program sites if allowed to continue. An arbitrary subsequent time interval is not covered by calling the final basis state an idle state. To guarantee a later finite interval, include that interval in the specified horizon and set C=0 there, or supply and price a justified isolation/switching mechanism. The theorem alone supplies neither indefinite idling nor reset or recycling.

## 8. Finite precision, timing, and static coefficient prices

Existence for a supplied waveform needs only its finite sample values and valid finite B,L. An algorithmic construction needs an evaluation/certification interface that supplies those values to the chosen precision. An arbitrary mathematically existing noncomputable waveform does not become algorithmically synthesizable by this statement.

Let an actual self-adjoint static implementation be K+E, with full-space operator bound ||E||<=delta_K. Duhamel's formula gives the additional isometry error t delta_K, whether or not E preserves N. If the prepared clock/plant/reference state is only within unhalved trace norm epsilon_init of |e_0><e_0| tensor rho_PR, add epsilon_init directly to the channel-output trace error. This is a preparation premise, not a conclusion of the clock construction.

If the perturbations preserve N and the one-head sector, one may instead use the proven sector bound ||E|_(N=1)||. In particular, pure program errors

    Eprog=sum_j n_j tensor delta C_j

have exact sector norm max_j||delta C_j||, whereas a safe full-space bound is sum_j||delta C_j||. Clock edge errors with bounds ||delta G_j||<=e_j, plant error e_H, and reserve errors delta h, delta B admit the conservative full-space budget

    delta_K <= sum_j e_j + e_H + |delta h|
                  +(m+1)|delta B|+sum_j||delta C_j||.       (26)

One must not use the favorable one-head estimate for arbitrary leakage-producing errors. Sample-time errors can be included by ||delta C_j||<=L|delta s_j| plus matrix evaluation error. Number-preserving program tolerances therefore need not be divided by the number of samples; other physical coefficient or timing tolerances are separate contracts.

Positivity also needs calibration margins. The exact edge blocks in (3) have a zero eigenvalue, so arbitrary entry perturbations need not preserve their positivity. One explicit finite prescription is to implement a positive finite approximation nu_tilde and an off-diagonal coefficient rounded downward from sqrt((j+1)(m-j)), while retaining the exact nonnegative integer diagonal weights. The determinant is then nonnegative, and the difference from (3) is charged in (26). Alternatively add an explicit positive local reserve covering the negative perturbation and pay its norm and scalar phase. Approximate plant/program matrices require h and B margins sufficient for their actual spectra. No unpriced “calibration preserves positivity” premise is used.

If readout occurs at actual time t+delta_t instead of the prescribed t, a safe additional error against the prescribed coherent full-output target is |delta_t| ||K+E||. If the actual generator conserves the one-head sector, its norm on that sector suffices. In the ideal model,

    ||K|_(N=1)|| <= ||H0+hI|| + 2nu m + 2B.               (27)

The time error is charged against one fixed target and cannot be removed merely by saying the schedule was evaluated at a different time. If one elects an actual-time comparator instead, its changed clock and plant target must be stated explicitly.

Combining the safe versions gives, for example,

    full-output trace error
      <= epsilon_init + 2[L tau t/sqrt(m)
                          +t delta_K+|delta_t| ||K+E||].    (28)

For an epsilon budget, set the ideal clock term at most epsilon/4, the total calibration/time term at most epsilon/4, and charge any initialization allowance separately. These are sufficient finite choices, not a claim that all tolerances are independent of m or that physical coefficients have a common cap.

## 9. Full scalars, moments, and work accounting

There are m+1 physical clock qubits and m nearest-neighbor clock edges. Each edge has norm nu(m+1); the full clock norm is exactly nu m(m+1). The largest hopping amplitude is at most nu(m+1)/2. In the Pauli expansion the XX and YY coefficient on an edge is -a_j/2.

The full scalar and on-site content of the clock is

    G= [nu m(m+1)/2] I - [nu m/2] sum_j Z_j
         -sum_j [a_j/2](X_jX_{j+1}+Y_jY_{j+1}).            (29)

The identity term in (29) is not thrown away. In the one-head sector the on-site contribution combines with it to give nu m I, whose phase is retained in (9). Its endpoint cancellation is an exact algebraic cancellation with i^m, not a phase convention that omits energy or action. The B N term has full-space scalar B(m+1)/2 and is not a global scalar on arbitrary excitation sectors; only its action on N=1 is B I. The plant reserve hI is a true global scalar.

With normalized plant trace tr_d(A)=Tr(A)/d, the identity component of the complete K is

    nu m(m+1)/2 + h + tr_d(H0)
        +(1/2) sum_j [B+tr_d(C_j)].                        (30)

All those terms remain in (17). The formula distinguishes local positive-block budgets from collected scalar coefficients and from an energy expectation in a particular state.

A useful full-space norm allowance is

    ||K|| <= ||H0+hI|| + nu m(m+1)+2B(m+1).                (31)

This is a finite-Hamiltonian allowance, not an identification with microscopic controller work or a lab energy standard. It includes all sectors even though the state theorem uses N=1.

The corresponding integrated norm allowance over the horizon is tau||K||, bounded by tau||H0+hI||+(pi/2)m(m+1)+2B tau(m+1). Staticity does not make this action or the stored energy zero.

For any plant state rho (possibly the marginal of an entangled reference input), C_0=0 gives exactly

    <K>_initial=Tr(rho H0)+h+nu m+B,
    Var(K)_initial=Var_rho(H0)+nu^2 m.                     (32)

Indeed K acting on |e_0> tensor psi has the component

    |e_0> tensor [H0+h+nu m+B]psi
         -nu sqrt(m)|e_1> tensor psi,

and those two clock components are orthogonal. This proves both moments without assuming a plant energy eigenstate. The first two total energy moments are exactly conserved by the time-independent K.

For fixed finite B,L,tau,H0 and small target error epsilon, the stated recipe has

    m=O(epsilon^-2),
    max clock-block norm=O(epsilon^-2),
    full clock/joint norm allowance=O(epsilon^-4),
    initial clock mean=O(epsilon^-2),
    initial clock variance=O(epsilon^-2).                 (33)

The exact formulas, rather than these fixed-parameter exponents, govern cases such as L=0 or changing tau. For L=0 and the endpoint condition, C is identically zero and the simulation is exact for every m>=1. For tau=0 the task is the identity channel and can be handled without a moving clock; the construction above assumes tau>0.

There is no explicit time-dependent external work after the static model is initialized: dK/dt=0. That statement does not price preparation, fabrication, installation, starting/stopping, clock isolation, or a physical realization of the supplied positive terms. The clock exchanges energy with the driven plant. For an absolutely continuous Lipschitz C with zero endpoints, the ideal plant bare-energy change is

    Delta<E0> = integral_0^tau Tr[rho(t) dot C(t)] dt,
    |Delta<E0>| <= min(2||H0||, L tau).                    (34)

Here rho(t)=U(t)rho U(t)^*, and the identity follows from differentiating the expectation of H0+C(t) almost everywhere. The actual plant bare-energy differs from this ideal final expectation by at most 2||H0|| L tau^2/sqrt(m), before other errors.

Trace closeness of the complete final state does not imply that the clock's energy has been returned with an m-independent error. The full norm grows with m, and an O(epsilon) state error can carry a finite energy difference. In particular the reference final product in (19) can have a different mean under K from the initial product when U(tau) performs work on H0; exact total-energy conservation holds for the actual state, not for the comparison product. The usual bound on that total-energy discrepancy contains ||K||. There is no contradiction and no energy/refund/recycling claim.

## 10. Narrow failure routes and boundaries

**Linear sampling is the wrong clock contract.** If one stores C(tau j/m), the site law concentrates at p_t rather than t/tau. The same orthogonal-residual estimate shows convergence to the schedule C(tau p_t), with residual at most L tau/(2sqrt(m)). It need not converge to C(t). For a two-level plant with H0=0 and C(s)=s(tau-s) Z, the requested integrated angle is tau^3/6, while the linear-sampled limiting angle is tau^3/8, since p_t(1-p_t)=(1/4)sin^2(pi t/tau). The difference tau^3/24 can be chosen away from any phase equivalence. The inverse-arcsine samples fix this specific mismatch; the witness is not an obstruction to other clocks or compressors.

**The selected basis state is essential.** A clock initially in the computational vacuum has N=0 and no occupation-controlled drive. An arbitrary computational-basis product is not covered by the one-head theorem. At multiple excitations the drive sums active samples and no longer equals one selected matrix. The full Hamiltonian remains positive, but the waveform theorem has a stated input-domain restriction.

**Literal whole-device two-locality does not follow for arbitrary matrices.** For example, if a three-qubit plant has C(s)=f(s)Z_1Z_2Z_3, the term n_j tensor C_j contains a nonzero four-body Pauli coefficient when f(s_j)!=0. Orthogonality of Pauli strings under Hilbert-Schmidt inner product rules out expressing that exact operator as a sum of only one- and two-qubit terms on the same qubits. Auxiliary simulation can change this conclusion only with its own hypotheses and errors. Even for a one-qubit plant, edges from every clock site to that plant need not form a bounded-degree spatial nearest-neighbor geometry. The positive NN result proved here is for the clock path and the supplied abstract occupation-control interface.

**No non-Hermitian target is implicit.** A generator C(t)=i f(t)I with nonzero real f would give a non-norm-preserving prescribed propagator. Such a map is outside the unitary Hamiltonian target. This is a domain qualification, not an obstruction for the stated Hermitian class.

**No exact arbitrary finite waveform or permanent stop is asserted.** A finite static unitary has analytic matrix entries in time; exact agreement with every merely Lipschitz prescribed full-output waveform is not a consequence of this construction. The theorem is finite approximation with an explicit bound. The free clock returns after 2tau; a final endpoint occupation is not a latch. These statements do not rule out different stopping mechanisms with additional resources.

**The physical preparation obligation remains.** A pure computational-basis clock state must be supplied, known in the chosen computational basis, and initially independent of the arbitrary plant/reference input. It has energy variance nu^2 m and is not a thermal stationary state of G. Its mathematical simplicity does not imply preparation from an arbitrary mixed state, a cold source, a native coherence reservoir, or a common energy/control cap.

## 11. Composition and what has actually been checked

Equations (18)-(23) are the complete operator/channel interface for composing this clock with an already proved simulator. If a future construction approximates this same K on the same input isometry by an all-output error delta_sim, the triangle inequality adds delta_sim to (22), with every scalar and auxiliary output included. If one instead inserts the new clock into an existing mediator proof, its hypotheses and norm-dependent residual constants must be rechecked for G and for the actual program coefficients. The previous unary-clock theorem does not automatically certify such a replacement just because both clocks preserve N.

After time tau, applying the same specified future channel to both complete outputs preserves their trace-distance bound. That does not by itself compare the continuing autonomous device to a different desired future plant evolution: the program can reactivate unless the horizon/idle/isolation conditions in Section 7 are met.

The proof checks the load-bearing steps directly: the two-qubit spectra and all-sector norm, the exact symmetric-space evolution and endpoint phase, the endpoint-uniform arcsine concentration estimate, the orthogonal full-isometry residual and reference-stable factor 2, and the full initial moments. No numerical fitting, finite science fixture, prior scientific replay, forced pass count, or audit status was used. The separate residual and representation calculations use different elementary mechanisms, but they remain one author's proof and require a separate review before substantial downstream reliance.

The spin-chain transport mechanism is standard prior art. After fixing this route, I consulted the public abstract of [Christandl, Datta, Ekert and Landahl, “Perfect state transfer in quantum spin networks”](https://arxiv.org/abs/quant-ph/0309131), which describes fixed unequal-coupling linear chains. I do not claim novelty for that mechanism or infer this full waveform, positivity, concentration, or resource statement from the abstract. The relevant formulas are proved above. The exact web response and source-exposure record are archived separately.

The disposition is a positive conditional clock-interface construction with an explicit finite error recipe and explicit geometry/supply/calibration boundaries. It is not a full NN realization of arbitrary plant matrices, a native state-supply theorem, an efficiency or common-cap theorem, an independent audit, or retained scientific status.


---

## Immutable source body: comparison

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# Source-exposed comparison of the basis-state waveform clock

Disposition: the root construction's finite clock-interface bound, positive clock, changed nearest-neighbor mediator realization, bare-input estimate, and supplied product-Gibbs certificate are mathematically supported at the inspected bytes, with the scope corrections below. The sharper factor 1/sqrt(2n) is valid. A separately labeled exposed synthesis can replace the root clock by the simpler positive edge clock from the frozen independent derivation, with all phases and constants explicitly changed as in Section 9. Neither original proof is modified.

This is a source-exposed analytical check after a protected pre-exposure derivation. It is not an audit, a native state-source theorem, or an independent model-family replication. No scientific program, numerical sweep, prior scientific replay, or new delegation was used.

## 1. Exact sources, chronology, and comparison scope

The root candidate is `basis_state_clock_root_candidate/DERIVATION.md`, 23256 bytes, SHA256 `0fc2b7046b24c535ebd9549449601c42d8af6e3a9f95ca3e5a45a16eabb5eb46`; its proposal freeze is `a24ea21b2c89a80554f09ca0038ef4ed61461ecca51e4a088dad6df4ce30fbea`. I read the entire candidate and its exact source pins after the protected proof was frozen and root had read it.

The independent derivation is `basis_state_clock_independent/DERIVATION.md`, 29173 bytes, SHA256 `84f03ca0de42477399e9a797f659b971e6beb88505d59fce6aaca5c6147acf39`; its 35-member freeze is `e77e7efe17a30c4444b0de48a0d88d2bc6711d34549e7106153208a2da58566d`. It remains unchanged, including its weaker but valid constant. Root's actual pre-exposure read record is 1620 bytes, SHA256 `5e81e709bc47249ee678ec7296b7b5d0b2a5ca32197503c19b7f1448f7b36149`, recorded at 19:21:11 UTC. The actual `runs/review_frontiers_1926/EXECUTION.json` has SHA256 `75f6082dd4b7c31737a3fe426a714647f83299be418c7f339729de6b3b74158e`. The directory label is not substituted for its recorded execution time.

The unchanged mediator source/review/decision are respectively `0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d`, `52eb2e2dcd9fc56a7be490e193b57754bd85bfad5d585244d4a9fce947b4465d`, and `134cbee6390a6f999813dd0234fe869bdd0bec2dddbd5d47a2209091c0dcbe5f`. Their previous complete reading and source-exposed checking are reused only for unchanged premises; the new coordinates, graph, clock, constants and initial moments are reconstructed below.

The pure-factor replacement lemma is in the canonical correlated-memory note, 203198 bytes, SHA256 `12bd18b0d2a1939639027ed51204a066744eab77d2b105a870f89bdb286b4d89`. Its current wrapper and complete relevant lemma/proof passages were read again. The lemma applies to any state and does not import the Markov or Gibbs-memory compression mechanics. The comparison does not import any newer Gibbs-parent or finite-bank result.

The two authors share prior unary-clock/controller context and the same model family. Both selected the standard engineered spin-transfer mechanism. The protected proof was not a fresh-context independent invention of that mechanism, and the post-exposure improvements below are not relabeled pre-exposure work. Root reports a complete four-page primary-paper read; my own earlier lookup covered only the public Christandl et al. abstract. Those different literature-read scopes remain distinct. No novelty claim for spin transfer is made.

## 2. Clock blocks, full-space norm, and phases

Use the root notation Omega=pi/(2tau), Lambda=Omega(n+1), L=n+1, w_j=Omega sqrt((j+1)(n-j)), and d_j=Lambda-w_(j-1)-w_j. The arithmetic-geometric mean inequality gives w_j<=Omega(n+1)/2, including every edge. Therefore d_j>=0 at interior sites and endpoints.

On the single-excitation part of a pair, n_j+n_(j+1)+S_j is I+X and has eigenvalues 0,2. On vacuum and double occupation its eigenvalues are 0,2. Thus every root edge block is positive on the full pair and has norm 2w_j. Its onsite block has norm d_j. Since sum_j d_j=Lambda(n+1)-2sum_j w_j,

    sum of physical block norms = Lambda(n+1)=B_X.

The all-occupied state attains B_X, so this is the exact full-clock norm, not merely an upper bound. The normalized full-clock trace is B_X/2. The collected absolute Pauli coefficient sum is B_X+sum_j w_j: the identity and Z terms contribute B_X, and the XX/YY pairs contribute sum_j w_j. The incident block norm at site j is Lambda+w_(j-1)+w_j<=2Lambda. These root statements are correct. A favorable one-head restriction cannot replace any of these full-space prices.

The root one-head matrix is Lambda I+Omega T_n. Its proof-only symmetric-spin representation gives the binomial law exactly, with the amplitude phase (-i)^j and the common phase exp(-iLambda t). At the horizon its full clock phase is

    exp(-iLambda tau)(-i)^n
       =exp[-i pi(2n+1)/2] = -i(-1)^n.                 (C1)

It is generally not one. The candidate retains it. The independent proof instead has Omega n I-Omega T_n, whose endpoint phase is exactly one. Agreement of position laws does not identify these two full-clock vectors or their scalar ledgers.

The root principal positive application has H_P>=0 and C(t)>=0. Its generic signed interface is conditional on additional actual reserves. The independent proof provides one explicit signed-interface recipe, using hI on the plant and B N on the clock, but that extension is not silently attributed to the root candidate's positive mediator specialization. Whole positivity of H_P alone still does not supply a separately positive decomposition of each old plant term.

## 3. The sharper constant and complete retained-output comparison

The independent proof used sin u>=2u/pi, which was sufficient but loose over the interval actually needed. Root uses the secant on [0,pi/4]:

    sin u >= (2sqrt(2)/pi)u.

For delta=|arcsin sqrt(x)-arcsin sqrt(p)|<=pi/2 and unit vectors v(x)=(sqrt(1-x),sqrt(x)), this gives

    ||v(x)-v(p)||^2=4sin^2(delta/2)
       >=(8/pi^2)delta^2.

For X=J/n, J~Bin(n,p), each square-root difference is bounded by its squared numerator divided by p or 1-p. Their expectations sum to at most 1/n. Thus

    E delta^2 <= pi^2/(8n),
    E |t_J-t|^2 <= tau^2/(2n).                         (C2)

At p=0 or 1 the binomial is deterministic, so those endpoints are handled directly without dividing by zero. This is a uniform finite-n bound. No Gaussian approximation, supplied mixing process, or limiting spatial wavepacket is needed.

For the freely evolving comparison map chi_n(t) tensor U_C(t), the residual consists of orthogonal clock components [C(t)-C_j]U_C(t). Its norm is at most L_C tau/sqrt(2n). Integration against the actual static unitary yields

    ||exp(-itH_tar)J_0-chi_n(t) tensor U_C(t)||
       <=L_C tau t/sqrt(2n).                           (C3)

This is an operator bound on all plant inputs, including all plant memory/fillers. Tensoring the identity on any reference does not alter it. The actual interacting clock is not assumed to have the free binomial law; that law is used only to bound the reference-map residual. Back-action remains in the error. The arbitrary noncommutation of H_P and the different C(t) is retained through the exact time-ordered U_C.

For two isometries V,W, expansion of V rho V*-W rho W* gives unhalved trace norm at most 2||V-W||, also with arbitrary reference. Thus c_ch=2 is correct. It is not a square-root probability conversion, a reduced-clock comparison, or a projection onto a successful trajectory. The complete clock vector, plant output and reference remain. The size prescription n>=max(1,ceil[L_C^2 tau^4/(2eta_X^2)]) is sufficient. Neither proof establishes an optimal n or a common-cap implementation.

The independent proof's nonlinear-sampling witness remains useful: with linear samples C(tau j/n), the asymptotic schedule is C(tau sin^2(Omega t)). For H_P=0 and C(s)=s(tau-s)Z, its integrated angle is tau^3/8 instead of tau^3/6. The inverse-arcsine sampling is therefore load-bearing for this particular clock. This is a narrow counterexample to linear sampling, not a no-go for other clock families.

The finite existence statement uses the supplied sample values and certified bounds. Effective coefficient synthesis additionally requires a computable evaluation/certification interface for C and its parameters; arbitrary mathematically existing Lipschitz functions are not automatically computable. This is the same distinction made explicitly in the independent proof.

## 4. Changed exterior geometry and graph bounds

The root clock c_j=(j,-1,-2), auxiliary row u_j=(j,-1,-1), and three auxiliary tail sites a=(-1,0,0), v_1=(-1,0,-1), v_2=(-1,-1,-1) are distinct and outside the nonnegative plant box. The auxiliary path is a-v_1-v_2-u_0-...-u_n. Each consecutive displacement, each c_j-u_j displacement, and p-a has Manhattan length one.

Counts follow directly:

    clock sites n+1; auxiliary sites m=n+4;
    clock edges n; auxiliary edges e_A=n+3;
    clock-source edges n+1; port edge 1;
    new sites 2n+5; declared geometric edges 3n+5.       (C4)

The maximum declared new degree is 3: interior clock sites have two path neighbors and one source neighbor, interior u sites have two path neighbors and one source neighbor, and all tail sites have at most two incidences. The old port gains only the exterior p-a neighbor. No old plant coordinate is moved or assumed clean.

For the stated nonnegative box, the only new-to-old nearest-neighbor adjacency is p-a. Among the displayed new coordinates, the nearest-neighbor pairs are exactly the declared path/source pairs. For example v_2-c_0 and v_1-u_0 have Manhattan distance two, and u_j is distance at least two from the old box. This checks the changed tail rather than importing the old cycle-and-tail count. The conservative 6(|P|+2n+5) incidence allowance remains safe for an enlarged finite occupied inventory. It is not a certificate that unlisted physical fields/couplings vanish; any outside environment or unknown coupling still needs the supplied isolation/error contract.

**Count qualification:** 3n+5 counts declared geometric edges. It need not count nonzero installed interaction coefficients. Zero endpoints imply z_0=z_n=0; a zero or scalar-only waveform can have every z_j=0 and make the runtime clock dynamically uncoupled from the auxiliary/plant component. The declared layout is connected, but universal connectedness of the nonzero Hamiltonian interaction graph does not follow. No proof step requires that stronger statement. Both source texts remain unchanged; future wrappers should use the declared-geometric wording.

The auxiliary adjacency has degree at most 2. Consequently B_A=I-Adj_A/12>=5I/6. Its inverse has a convergent nonnegative Neumann series, and the path from a to u_j has length j+3, yielding

    (B_A^-1)_(a,u_j)>=12^(-(j+3)).                      (C5)

The diagonal inverse entries are at most 6/5 and hence at most 1/g_0 for the root's conservative g_0=3/4. The lower bound proves strictly positive response and finite source coefficients, not efficient or polynomial resource scaling; an individual programmed coefficient can be zero.

On the complete auxiliary qubit space, +/-S_vw<=n_v+n_w gives L_A>=5N_A/6>=g_0 N_A. Equivalently use the stated positive edges and onsite residuals. The vacuum is the unique zero vector. Thus the complete reduced inverse R on all nonvacuum sectors has norm at most 1/g_0; it is not a one-excitation-only inverse. The positive block norm sum is m and the all-occupied state attains m, so ||L_A||=m exactly. Root's ell_A=m+e_A/12 is a valid larger allowance; it is consistently an upper bound, not an equality claim. The scalar m/2 is correct.

## 5. All-source contraction and finite bare-input corrector

The geometric completion is for a supplied single-port waveform whose samples have the form

    C_j=a_j I+b_j X_p+c_j Y_p,
    0<=sqrt(b_j^2+c_j^2)<=a_j<=g,

with real coefficients. The general matrix interface of Section 4 is not thereby made local for every plant matrix. The special form and the accessible nonempty port must remain explicit.

Using Y|0>=i|1>, the creation amplitudes from auxiliary vacuum are q(X_p+iY_p) at a and z_j n_(c_j) at u_j. The port square is

    q^2(X_p-iY_p)(X_p+iY_p)=4q^2 n_p.                 (C6)

It is not a scalar. For the real inverse entry t_j>0, the port/source cross contribution is

    q t_j[(X_p-iY_p)z_j+z_j* (X_p+iY_p)]n_(c_j)
       =2q t_j[Re(z_j)X_p+Im(z_j)Y_p]n_(c_j).

The root z_j=-(b_j+i c_j)/(2q t_j) therefore gives the negative desired X/Y term with the stated Y sign. Source-source cross terms contain n_(c_j)n_(c_k), which vanish for j!=k only on N_X=1. The source self-squares are |z_j|^2 gamma_j n_(c_j). Hence the exact restricted contraction is C_ct-W, including the nonscalar 4q^2 gamma_a n_p. No part of this identity is asserted on arbitrary clock sectors.

The source norm v=2q+sum_j|z_j| is a valid full-space bound: the port block has norm 2q and each source block norm |z_j|. The counterterm bound c_ct and the full background bounds a_*,b_* follow from positive sums and ||C_j||<=2g. Their use is conservative, including all clocks, not merely the prepared head. The crude exponential lower bound (C5) gives the stated finite |z_j| allowance. It does not make the physical NN completion polynomial in waveform accuracy.

To rederive the residual independently of an assumed effective-Hamiltonian formula, set epsilon=Delta^-1/2, X=RVJ_A, Y=RVX, Z=J_A-epsilon X+epsilon^2Y. V changes auxiliary excitation parity. X has one excitation; after the vacuum part is removed by R, Y has two. The full-sector inverse in Section 4 is precisely what permits this step.

Expanding (epsilon^-2 L_A+epsilon^-1V+A)Z gives:

    order epsilon^-1: -L_A X+VJ_A=0;
    order 1: L_A Y-VX+AJ_A
               =-J_A(C_ct-W)+J_A A=J_A H_tar;
    order epsilon: VY-AX;
    order epsilon^2: AY.

Subtracting Z H_tar leaves exactly

    epsilon(VY-AX+XH_tar)+epsilon^2(AY-YH_tar).           (C7)

No commutator among H_P, K_X, n_p, C_ct or W has been discarded. With x=v/g_0, y=v^2/g_0^2, the residual norm is at most epsilon[v y+(a_*+b_*)x]+epsilon^2(a_*+b_*)y. The two bare-versus-corrected endpoint differences cost 2(epsilon x+epsilon^2y). Integration proves the root F_1,F_2 and eta_A exactly. The sufficient Delta recipe makes each of the two terms at most eta_med/2. This is a bare-vacuum input theorem, not an assumed physically prepared dressed state or a global spectral approximation.

The reserve R_pos=sqrt(Delta)v makes sqrt(Delta)V+R_pos I positive on every sector. Distributing 2q sqrt(Delta) to the port edge and sqrt(Delta)|z_j| to each source edge gives actual positive shifted local blocks. Their identity coefficients add to R_pos once. Other new terms have positive local decompositions. Whole positivity of the old H_P still needs a separate local-block contract if a consumer asks for one.

## 6. Combined target, scalars, norms, and exact moments

Applying the clock estimate after the mediator estimate yields the root full-isometry error

    eta_total=L_C tau^2/sqrt(2n)+F_1/sqrt(Delta)+F_2/Delta.

The target is exp(-itR_pos)|vac_A> tensor chi_n(t) tensor U_C(t), at the same actual t, for all original plant/reference inputs. Clock and auxiliary outputs are retained. At tau the extra root clock phase is (C1), and the reserve phase remains exp(-iR_pos tau). A density-matrix comparison can forget a common phase only after that physical operator/scalar accounting has been made. A separately compiled endpoint U_C(t) can be substituted only at that compiler's actual-time window and with its own error and phase; it does not certify a desired intermediate trajectory.

The root B_full is the triangle bound a_*+Delta ell_A+sqrt(Delta)v+R_pos. It includes all auxiliary and clock sectors. The full normalized scalar is correct term by term: s_(H_P), B_X/2, (sum_j a_j)/2, Delta m/2, 2q^2 gamma_a, (sum_j |z_j|^2 gamma_j)/2, and R_pos. V is traceless on the full space. The corresponding action allowance is tau B_full. None of these is automatically a microscopic energy, actuator-work, or detector identification.

For C(0)=0 the actual generator applied to a bare input has three orthogonal components: (i) clock0/auxiliary vacuum with plant operator D_P+Lambda+R_pos, D_P=H_P+4q^2 gamma_a n_p; (ii) clock1/auxiliary vacuum with amplitude w_0; (iii) clock0/auxiliary a excitation with plant amplitude sqrt(Delta)q(X_p+iY_p). Their orthogonality gives exactly

    mean=Lambda+Tr(rho_P D_P)+R_pos,
    variance=Var_rho(D_P)+Omega^2 n
                        +4Delta q^2 Tr(rho_P n_p).       (C8)

This retains the H_P/n_p covariance and arbitrary correlations within the old plant/reference. For a nonzero starting sample, the diagonal block also includes a_0+|z_0|^2 gamma_0 and the fluctuation adds Delta|z_0|^2, as the source specifies. The two distinct auxiliary creation sites give no missing cross term. These identities hold on the stated ideal bare product input; they are not exact formulas for a finite-temperature imperfect controller input.

The leakage estimate only bounds the auxiliary penalty contribution by Delta ell_A eta_A^2; it need not vanish. Likewise full-output trace closeness does not establish returned clock energy, conserved subsystem energy, or controller reuse. Static total moments are conserved under the actual K_Delta; approximate comparison-product moments can differ because the operator norms grow with the chosen parameters.

Physical calibration must bound the written installed generator. For positive Delta' and actual L_A',V',A',R_pos', one safe comparison is

    ||K_actual-K_Delta||
      <=|Delta'-Delta|ell_A+Delta'||L_A'-L_A||
        +|sqrt(Delta')-sqrt(Delta)|v
        +sqrt(Delta')||V'-V||+||A'-A||+|R_pos'-R_pos|.      (C8a)

Here |sqrt(Delta')-sqrt(Delta)|=|Delta'-Delta|/[sqrt(Delta')+sqrt(Delta)]. Source coefficient errors have full bound ||V'-V||<=2|q'-q|+sum_j|z_j'-z_j| when those are the only source changes. Counterterm and graph/inverse calibration errors remain in A' and the supplied coefficient certificates; they are not deleted by recomputing a favorable effective response. The isometry price is the time integral of this full-space norm, doubled for full trace error. Scalar and reserve errors are included. Clock-number leakage prevents replacing it by a prepared-sector estimate. A fixed-target timing defect costs |Delta t| times the actual full generator norm, or a certified invariant-sector norm on its explicitly restricted input domain. Restoring faulty-block positivity requires actual priced margins.

## 7. Product-Gibbs supply and arbitrary old/reference correlations

Write k=2n+5 and distinguish the preparation coefficient nu_p from the runtime Omega. The root preparation Hamiltonian is a sum of k disjoint positive onsite projectors, each penalizing the wrong bit by nu_p. Its unique ground state is exactly the complete runtime bit string, with one at c_0 and all other clock/auxiliary bits zero. Its norm, normalized scalar and gap are nu_p k, nu_p k/2 and nu_p.

For beta>0, the supplied controller Gibbs marginal has exact ground probability

    p_good=(1+exp(-beta nu_p))^-k,
    delta_G=1-p_good<=k exp(-beta nu_p).                  (C9)

Its unhalved marginal trace distance from the target pure bit string is exactly 2delta_G. This follows from the diagonal eigenvalues, and holds regardless of whether that marginal has correlations with another system in a joint extension.

**Mandatory wording correction:** the root sentence restricting the “smaller 2delta marginal bound” to independent product input is literally too narrow. The marginal bound itself holds with arbitrary correlations. What requires independence is using 2delta as the full joint replacement error with the old/reference marginal retained. The historical candidate wording is left untouched; this correction must govern a current wrapper.

For arbitrary joint sigma_controller,Y, Y containing the complete old plant and references, let delta=1-Tr(P sigma) for the desired pure-controller projector P, and let omega_Y=Tr_controller sigma. The general canonical lemma applies directly:

    ||sigma-P_controller tensor omega_Y||_1
        <=g(delta)=delta+sqrt(delta(4-3delta)).            (C10)

It is independent of Markov structure. To check applicability, purify sigma and split it into orthogonal good/bad components. The difference from the unnormalized good block has 2 by 2 matrix [[0,sqrt(delta(1-delta))],[sqrt(delta(1-delta)),delta]], trace norm sqrt(delta(4-3delta)). The difference between the pure-controller tensor exact old marginal and that good block is positive with trace delta. Their sum gives (C10), including the endpoints. No normalized conditional old marginal is substituted.

A sharp admitted witness is a coherent purification of the entire product-Gibbs diagonal, with an old reference copying each controller bit string. It has the exact Gibbs controller marginal, yet its full replacement distance is g(delta_G), not 2delta_G. Its bad-reference subspace supplies the extra delta_G term. Thus neither a product controller marginal nor a correct ground-state population proves controller/old-system independence.

If the delivered controller marginal is within half-trace distance d of the stipulated Gibbs marginal, the actual bad-event probability is at most

    delta_bar=min(1,k exp(-beta nu_p)+d).                  (C11)

Applying (C10) with the actual complete old marginal and then the same actual runtime unitary gives the full trace budget

    g(delta_bar)+2eta_total+physical perturbation,
    timing, and release allowances.                     (C12)

The root thermal prescription beta nu_p>=log(2k/epsilon) correctly targets only marginal error epsilon. A simple sufficient correlated-joint preparation prescription is instead beta nu_p>=log(9k/epsilon_prep^2), with d=0, because g(delta)<=3sqrt(delta). Delivery error d consumes the same infidelity budget. At fixed beta nu_p, increasing k eventually spoils whole-controller purity; no fixed-temperature/common-gap arbitrary-accuracy result is established.

For an imperfect joint input with replacement error e_prep=g(delta_bar), the exact bare-input moments (C8) are comparison moments. A safe bound on their actual scalar mean error is B_full e_prep, on second-moment error B_full^2 e_prep, and on variance error 3B_full^2 e_prep. These growing norm factors cannot be omitted by importing the smaller state-error budget. One can use centered bounds if a justified center/radius is separately supplied. No claim about exact conditional moments on every rare reference event follows.

## 8. Release, elapsed time, and what remains supplied

The Gibbs clause is an equilibrium marginal contract for G_prep, not a cooling or autonomous preparation algorithm. Runtime hopping and mediator interactions do not generally commute with the target bit projector or preserve its Gibbs law. Asserting the product-Gibbs marginal therefore requires those interactions to be absent, isolated, or actually compensated during preparation. The subsequent change to K_Delta is a distinct physical operation.

A precise optional release allowance illustrates the required chronology; it is an exposed conditional observation, not a source of native controls. In the principal positive case write K_Delta=H_P+F, where the new controller/mediator sum F is positive with the displayed shifted-block decomposition. Given a supplied smooth monotone envelope u on a release interval of duration s, the path

    H_rel(r)=H_P+(1-u(r))G_prep+u(r)F

is positive, starts at H_P+G_prep, and ends at K_Delta. On the ideal pure controller input G_prep annihilates the clock/auxiliary factor. Comparing the release to that fixed controller and the actual H_P-aged old state gives isometry error at most ||F|| integral_0^s u(r)dr, by the same residual identity. The initial correlated replacement price g(delta_bar) is charged first. Thus a finite fast release can be allowed with a supplied finite slew/control contract, but its duration s ages the old plant and its error is not zero.

The runtime theorem must then start with the H_P-aged old input at the release endpoint, or carry a different explicitly justified actual-time target. Starting U_C(t) on the old pre-release state would discard real elapsed evolution. If source and release faults alter the actual old marginal, the exact-marginal lemma retains that actual marginal; it does not restore a nominal earlier one.

The scalar action and work of such a release are also real. For a monotone ideal closed-system interpolation the drive-work magnitude is bounded by ||F-G_prep||; arbitrary faults need their own endpoint/variation bounds. An ideal instantaneous switch on the pure bit input, if used only as a comparator, has energy jump

    Lambda+4q^2 gamma_a Tr(rho_P n_p)+R_pos

when C(0)=0 and the old H_P is the same. For the alternative clock below replace Lambda by Omega n. A Gibbs-correlated actual state can have further penalty/control contributions, bounded using the full operators. None of this identifies a laboratory work source or makes the switch, installation, or purification native.

The runtime clock remains periodic. An optional C=0 interval gives the specified finite plant-aging window, with the actual clock state continuing to evolve; it does not permanently halt the clock. A later same specified channel preserves a trace-distance comparison, but an unmodeled continuing runtime generator can revisit samples. Release, final isolation, reset, and reuse need separate supplied mechanisms and prices.

## 9. Explicit exposed synthesis with the independent positive-edge clock

This section is new after root-candidate exposure. It combines the independent positive-block clock with root's sharper sampling estimate and newly checked mediator geometry. It is not a change to either original body or an additional pre-exposure check.

Keep n, Omega, the root sample times, all physical coordinates, and all auxiliary/source coefficients. Replace only K_X by

    K_X'=sum_(j=0)^(n-1) Omega[(n-j)n_j+(j+1)n_(j+1)
                              -sqrt((j+1)(n-j))S_j]
        =Omega n N_X-sum_j w_j S_j.                       (C13)

Each edge has eigenvalues 0,0,Omega(n+1),Omega(n+1), so there are n positive NN clock blocks and no separately needed clock d_j blocks. The full block-norm sum and exact full-clock norm are

    B_X'=Omega n(n+1),     s_X'=B_X'/2.                    (C14)

The collected absolute Pauli coefficient sum is B_X'+sum_j w_j. Interior incident block load is 2Omega(n+1), endpoint load Omega(n+1). The onsite terms contained inside the positive edge blocks remain physical; “no separate onsite blocks” does not mean no onsite coefficients.

Let Q be the product of Z_j over odd clock sites. Then Q n_j Q=n_j, Q S_j Q=-S_j, and

    K_X'=Q K_X Q-Omega N_X.                               (C15)

The sign change is a clock gauge, while the subtraction is a number potential on the full clock space, not a full-space scalar. Positivity of K_X' follows from its new local blocks, not from unjustifiably subtracting a positive term from an old positive operator.

Its exact free vector is

    chi_n'(t)=exp(-iOmega n t)sum_j sqrt(binomial(n,j))
          cos(Omega t)^(n-j)[i sin(Omega t)]^j |j>,
    chi_n'(tau)=|n>.                                      (C16)

The same binomial law gives the sharper bound (C2)-(C3). Thus the new target at tau carries the actual mediator phase exp(-iR_pos tau) but no additional clock phase. This is an explicit phase change from the root target, not permission to identify the old target with it.

The operator Q commutes with every source n_j, with V, C_ct and L_A. N_X commutes with the entire runtime generator. Hence, at the same Delta and R_pos,

    K_Delta'=Q K_Delta Q-Omega N_X,
    exp(-itK_Delta')=exp(iOmega N_X t)Q exp(-itK_Delta)Q.    (C17)

This is an exact algebraic relation on the full space. On the input sector the extra phase is exp(iOmega t). The map J_A and both correctors are Q-equivariant. The complex-source sign, port square, counterterms and geometry are unchanged. One can either use (C17) to transfer the old error at its old constants, or use the following rederived, smaller norm allowances.

The ideal initial clock |0> is Q-invariant. An arbitrary correlated Gibbs extension need not be Q-invariant even though its diagonal controller marginal is; its replacement is handled by (C10), not by silently conjugating the actual input.

Define

    a_*'=h+B_X'+(n+1)g+c_ct,
    b_*'=h+B_X'+2(n+1)g,
    F_1'=2x+tau[(a_*'+b_*')x+v y],
    F_2'=2y+tau(a_*'+b_*')y.                              (C18)

The auxiliary g_0,t_j,gamma_j, v,c_ct,x,y are unchanged. Repeating the literal expansion (C7) with A' and H_tar' proves the bare error F_1'/sqrt(Delta)+F_2'/Delta. Taking Delta>=max(1,(2F_1'/eta_med)^2,2F_2'/eta_med) is sufficient. At fixed old Delta the earlier larger bounds remain safe, but a smaller Delta must be chosen from the new formula, not assumed.

The new physical allowances are

    B_full'=h+B_X'+(n+1)g+c_ct+Delta ell_A+sqrt(Delta)v+R_pos,
    s_full'=s_(H_P)+B_X'/2+(sum_j a_j)/2+Delta m/2
              +2q^2 gamma_a+(sum_j |z_j|^2 gamma_j)/2+R_pos.

The exact ideal bare-input moments at C(0)=0 become

    mean=Omega n+Tr(rho_P D_P)+R_pos,
    variance=Var_rho(D_P)+Omega^2 n+4Delta q^2 Tr(rho_P n_p).
                                                               (C19)

The variance stays the same at fixed Delta because the first hopping magnitude is unchanged and the clock diagonal changes only by Omega on N_X=1. The prepared-input mean, full normalized scalar, and exact full-clock norm decrease by Omega, Omega(n+1)/2, and Omega(n+1), respectively, before any optional Delta reselection. The joint norm allowance B_full also decreases by Omega(n+1); an equal exact decrease of the interacting generator's actual norm is not asserted. These are different quantities and cannot be substituted for one another.

The complete uniform isometry error is now L_C tau^2/sqrt(2n)+F_1'/sqrt(Delta)+F_2'/Delta, with reference target exp(-itR_pos)|vac_A> tensor chi_n'(t) tensor U_C(t). The full output trace factor remains 2. Product-Gibbs preparation uses the same k=2n+5 bits and same G_prep, so its pure-state/marginal contracts do not change. All physical calibration and release bounds must use K_Delta', its actual scalar, and B_full' if this substitution is adopted.

This gives a concrete conditional substitution, not a new efficient-controller theorem. The inverse-entry source costs are still potentially exponential in n, the waveform and controls remain supplied, and no preparation/reuse or common-cap obligation is discharged.

## 10. Counterexamples and domain limits retained

The independent wrong-linear-sampling example, arbitrary-matrix two-locality obstruction without auxiliaries, and energy/return caveat remain valid. The root vacuum-input failure, multiple-head cross terms, lost clock phase, omitted d_j potential, omitted nonscalar counterterm, one-XX-axis limitation, and bare-versus-dressed input distinction remain valid under their stated scopes. In the independent clock substitution d_j is replaced by a different proved positive decomposition; simply deleting root's d_j without that replacement is still an invalid shortcut.

The product-Gibbs purification witness above is a concrete counterexample to using its marginal 2delta as the full correlated replacement price. It does not refute the root g(delta) theorem. Zero program coefficients clarify geometric counts and dynamic connectedness, without refuting the waveform approximation. A small state error gives only a norm-weighted energy error, and a finite final idle interval does not prove permanent stopping. None of these narrow witnesses is a universal impossibility claim.

## 11. Coverage and actual verification limits

All ten root sections were covered: the complete-input contract; full-space positive clock blocks and coefficient counts; exact motion and phase; the sharpened concentration and Duhamel bound; norms/moments/calibration; the changed graph and every new adjacency; all complex sources and the two-excitation corrector; the full target/physical prices; the product-Gibbs/arbitrary-reference source and release limits; and the claimed verification scope. The independent proof remains an intact source and the sharper bound/substitution remain separately attributed.

The initial broad search of the canonical correlated-memory note produced truncated discovery output. That output is not credited as a complete read. The exact relevant wrapper and complete proof passages were then read in bounded ranges and used only for the general pure-factor replacement lemma. Their selected coverage is recorded with the source identities. Old unchanged mediator context was reused by exact identities; new clock/geometry and all load-bearing substitutions were derived explicitly here.

Metadata capture and verification record actual source bytes, recovery, source-at-launch, stdout, stderr and exit statuses. They do not execute a physics model or certify the mathematics. The actual root pre-exposure record and its recorder/source/streams are preserved as provenance; no separate historical LAUNCH file is invented. No model/effort override, new agent, W/Git/PR/audit/lock/checkpoint/prompt/axiom mutation occurred.

## 12. Justified disposition

No blocking algebraic defect was found in the root finite construction at the inspected revision. Conditional source support is justified with two explicit current-scope corrections: use declared geometric edge counts, and distinguish the universally valid controller marginal 2delta from its independence-dependent extension to a full joint error. The correlated source budget uses g(delta) and the exact unconditioned old marginal; thermal state accuracy does not alone certify precise runtime energy moments or a release process.

The positive-edge replacement in Section 9 is a reviewable exposed synthesis with its own full scalar/norm/phase/corrector ledger. It can be adopted only as that explicit result, rather than silently altering the frozen root or independent candidate. Root review of this complete comparison and any later publication wrapper remains a separate decision. Native state preparation, geometric supply of the required interactions, release/installation, physical energy identification, a reusable finite controller/detector, common caps and efficient synthesis remain open.
