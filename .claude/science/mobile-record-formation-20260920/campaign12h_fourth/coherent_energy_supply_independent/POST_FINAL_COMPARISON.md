# Final comparison: coherent supply for actual star outputs

This is a bounded independent source comparison, not an audit or landing
verdict. The released author packet agrees with the sealed PRE reconstruction
on the stationary-output restriction, its sharp trace-norm error, and the
finite coherent carrier that exactly prepares one specified actual output.
The author's additional weighted coherence inequality and classical selector
construction are reconstructed below. No material mathematical correction to
the released author note was found within this scope.

The result remains fixed-input resource mathematics. It neither realizes nor
rules out the full original jump instrument on arbitrary inputs, its no-event
map, event timing, or the microscopic GKLS process. The separate full-instrument
author directory was not read. The original Hamiltonian and jumps stay fixed.

## 1. Source identity and independence boundary

The independent PRE was sealed before any coherent-supply author exposure:

- `PRE_SEAL.json`: `ec6d33b271b05faf74700d9f9346921a5f652fb860c967b631d79b21a8b51d0d`.
- `PRE_COHERENT_ENERGY_SUPPLY.md`: `33420632afe2685ff89ea13ca63d6f0104a06507a218da07adec5700d2bce5ac`.
- Its complete-matrix control: `coherent_supply_check.py`,
  `361ee06c509b8b43644eeb70ae6e5867d21437bc5d7cd87eea5bec4a77b8979c`.

The root explicitly released the following packet only after reading the PRE
and authenticating all its 21 bound artifacts:

- `COHERENT_FUEL_FOR_ONE_ACTUAL_STAR_OUTPUT.md`:
  `93a93b02a37ecb7c804cb9800e144d321476a101130dacac0bb3b2fdbee20e34`.
- `AUTHOR_SEAL.json`:
  `350648ccf962bf0b225e8c0eb8cbe0e101bd80eefe307e064603d61cddbf7d90`.
- Current author control: `coherent_fuel_control.py`,
  `025310de415ec4654f03725b9311ab274882d341c02b08307c2dc8ad339d4c67`.

The complete author note, current and failed controls, development-failure
record, exact result JSON, and raw logs were read. The author seal and all seven
of its artifact bindings were authenticated before and after calculation.
Byte-identical comparison copies, including the seal, are under `post_sources/`;
`POST_SOURCE_BINDINGS.json` records their original paths and hashes.

No author code was imported or executed. Both independent controls use only
the previously sealed independent star engine
`microscopic_star_complete_matrix_check.py`, hash
`6652f0c847d478f0db29b3fc4f9f739c309ce4126be69dd48221ab5d9377892b`.
That engine reconstructs the full physical sector from the local operators;
its prior source isolation, failures and completed checks remain in the
unchanged microscopic-star packet. Reuse of that independently checked model
is explicit: the present resource calculation is not a second independent
derivation of the underlying star matrices.

All PRE bytes remain fixed. Current campaign CHECKPOINT, external
autonomous-reservoir-personal files, and `full_instrument_energy_supply_author`
were not read. The author's external contextual citation was not consulted
and is not needed for any proof below. No bibliographic verification is claimed.

## 2. Shared results and exact matrix comparison

Take delta>0, epsilon>0 and integer S>=1 in the already reconstructed physical
star sector. Let d be the normalized dressed initial state, with Hd=0. For one
specified actual normalized formation output, write

    phi = sqrt(1-p) l + sqrt(p) h,
    H l=0, H h=Omega h,
    Omega=delta epsilon^-4 (1+3epsilon^2),
    p=c epsilon^2/(1+3epsilon^2).

Here c=2, 1, or 3/2 for a plus resolved mark, minus resolved mark, or coherent
edge mark. The three vectors d,l,h are mutually orthonormal: d has N=1 and l,h
have N=3. The physical H is nonnegative. A nonzero original formation event
also requires a positive rate parameter kappa; kappa cancels from these
normalized conditional states and the resource formulas.

Suppose the initial reservoir state is stationary, the joint unitary commutes
with the free total-energy time evolution, and the selected reservoir effect
commutes with reservoir energy. Since dd* is stationary, joint invariance and
partial trace make every nonzero conditional system state stationary. This
argument permits energy degeneracies and arbitrarily rare outcomes. Its
infinite-reservoir version uses the well-defined time-evolution groups and a
bounded effect, not an informal commutator of unbounded operators.

The minimum full trace norm over normalized stationary system states is exactly

    min_sigma ||phi phi* - sigma||_1 = 2 sqrt(p(1-p)).                 (1)

The dual witness X=|l><h|+|h><l| has operator norm one, vanishes in expectation
on stationary states, and has expectation 2sqrt(p(1-p)) on phi. The dephased
state sigma_*=(1-p)|l><l|+p|h><h| attains the bound. The same witness gives
2q sqrt(p(1-p)) for the distance from q phi phi* to any subnormalized
stationary candidate; q sigma_* attains it. This is the trace norm itself,
not the conventional factor-one-half trace distance.

For the exact finite carrier, choose H_R=Omega|1><1| and
beta=sqrt(1-p)|0>+sqrt(p)|1>. Put

    a=d tensor |0>,  b=l tensor |0>,
    c1=d tensor |1>, f=h tensor |0>,
    U=I-|a-b><a-b|-|c1-f><c1-f|.                                   (2)

Each difference is taken between orthogonal states of the same total energy.
Equation (2) swaps a with b and c1 with f, acts identically elsewhere, is a
self-adjoint unitary on the complete system/carrier space, and conserves total
free energy. It gives U(d tensor beta)=phi tensor |0>. The author's displayed
swap expression expands to exactly (2), not merely the same output on d.

With the ordered support basis d0,d1,l0,l1,h0,h1, the independently sealed and
author six-dimensional matrices agree entry by entry: swaps 0<->2 and 1<->4,
with all other basis states fixed. The total-energy diagonal is
(0,Omega,0,Omega,Omega,2Omega). POST checks also embed (2) in the complete
32-dimensional physical-star/carrier space and verify the identity on the
complement of that six-dimensional support.

The carrier and output have exactly the same energy distribution, hence mean
p Omega=c delta/epsilon^2 and variance p(1-p)Omega^2. Under H_R>=0 and finite
mean energies, conservation requires at least p Omega initial reservoir energy
for a deterministic exact output from d. The construction attains this bound
and consumes the fuel; it is not a catalyst. Replacing beta by its energy
dephasing keeps every energy moment but gives sigma_*, exactly attaining (1).

With finite-dimensional spectral pinching Delta_R and Delta_H, retaining
coherence within degenerate energy spaces, define

    C_R(eta)=||eta-Delta_R eta||_1,
    C_H(rho)=||rho-Delta_H rho||_1.

The fixed-input channel from R to the system intertwines these pinching maps,
so trace-norm contraction gives C_R(eta)>=C_H(phi phi*)=2sqrt(p(1-p)).
The carrier beta attains equality. The proof requires no imported claim about
catalysts or repeated operation. The finite-dimensional pinching inequality
is not asserted for an unexamined continuous-spectrum time-average limit.

## 3. Independent reconstruction of the author's flagged inequality

This section compares an additional statement in the released author note.
It was not part of the original PRE's multi-outcome formulation. The PRE did
independently prove the corresponding single-success-branch contraction.

For the fixed system input d, let Gamma_j be a complete family of covariant
completely positive maps from reservoir states to subnormalized system states.
Completeness means that Phi(eta)=direct_sum_j Gamma_j(eta), with an orthogonal
zero-energy classical outcome flag, is trace preserving. Write
Gamma_j(eta)=q_j rho_j, ignoring zero-probability normalized states.

Covariance and finite-dimensional time averaging give

    Phi(Delta_R eta) = Delta_(H tensor I_flag) Phi(eta).

The output is already block diagonal in the flag. Energy pinching therefore
acts separately inside its flag blocks; it does not remove physical
degeneracy coherence. Consequently,

    sum_j q_j C_H(rho_j)
      = ||Phi(eta)-Delta_(H tensor I_flag) Phi(eta)||_1
      = ||Phi(eta-Delta_R eta)||_1
      <= ||eta-Delta_R eta||_1.                                    (3)

The last step is Hermitian trace-norm contraction of a completely positive
trace-preserving map. This proves the author's weighted inequality. It is a
hypothetical instrument on the reservoir with d fixed, not a claim that the
original system jump instrument has a conserving dilation. The physical
assumptions that establish covariance must hold for each included outcome.

For a single compatible success branch with probability r and exact output
phi, the same reasoning, or direct contraction of the trace-nonincreasing
branch, gives C_R(eta)>=r 2sqrt(p(1-p)). Nonnegative system and reservoir
energies independently give E_R(initial)>=r p Omega: the selected system
energy is part of the nonnegative unconditioned final system energy. The
factor r cannot be dropped for a heralded, possibly rare, output.

## 4. Independent reconstruction of the author's selector

Label the original conditional marks j. Their probabilities at the dressed
preparation are w_j=1/6 for the six resolved marks or w_j=1/3 for the three
coherent edge marks. The POST control reconstructs these weights from the
actual norms ||j_j Fg||^2, rather than entering the weights as expected data.

All these target states have the same Omega. Give the reservoir a zero-energy
classical selector J and a two-level carrier B with

    H_R=I_J tensor Omega|1><1|,
    eta_R=sum_j w_j |j><j| tensor |beta_j><beta_j|,
    beta_j=sqrt(1-p_j)|0>+sqrt(p_j)|1>.

For each mark use its actual physical l_j,h_j in (2), producing U_j. Then

    U_controlled=sum_j |j><j|_J tensor U_j

is unitary and commutes with the free total energy, block by block. Acting on
the fixed d and eta_R, it gives

    sum_j w_j |j><j|_J tensor |phi_j><phi_j| tensor |0><0|_B.        (4)

Reading J is compatible with H_R. Thus (4) realizes exactly the normalized
conditional marked-output ensemble for this specified preparation. Its
supplied energy is

    sum_j w_j p_j Omega = 3 delta/(2 epsilon^2).                    (5)

For the resolved case the average of c=2 and c=1 is 3/2; for the coherent
case every c=3/2. Because selector blocks are orthogonal, both the input
carrier coherence and flagged output coherence are

    sum_j w_j 2sqrt(p_j(1-p_j)).                                   (6)

Hence this selector saturates (3), as well as the average energy bound. There
is no requirement for the different phi_j to be mutually orthogonal: the
orthogonal classical selector makes the controlled construction well-defined.

The preparation eta_R is an explicitly correlated selector/fuel ensemble. It
already contains the required phase resource and chosen mark probabilities.
Equation (4) specifies no stochastic event time, rate, no-event action, or
arbitrary-input response. Those missing data cannot be inferred from the
agreement of this normalized ensemble.

## 5. Separate contributions already present in the independent PRE

The following explicit witnesses were independently derived and sealed before
the released author packet. They sharpen the scope analysis; they should not
be attributed to the author's shorter note.

First, both heralded lower bounds are simultaneously sharp at every 0<r<=1.
Use reservoir basis s0,sE,f0 of energies 0,Omega,0, prepare

    eta_r=r |beta_s><beta_s|+(1-r)|f0><f0|,
    beta_s=sqrt(1-p)|s0>+sqrt(p)|sE>.

Apply (2) on the success carrier and the identity on the failure flag, and
read the compatible effect |s0><s0|+|sE><sE|. Success is r phi phi*, failure
is (1-r)dd*, initial mean energy is r p Omega, and initial coherence is
2r sqrt(p(1-p)). This gives an explicit sharp attainer, beyond a lower bound.

Second, energy-compatible readout is a real hypothesis. Starting with the
stationary excited reservoir |1>, a conserving unitary can swap d1 with

    v=sqrt(1-p) l1+sqrt(p) h0,

because both have total energy Omega and are orthogonal. Reading the reservoir
effect |+><+|, with |+>=(|0>+|1>)/sqrt(2), produces exactly (1/2)phi phi*.
This effect does not commute with H_R. The witness shows how a noncompatible
readout leaves the stationary theorem's class; it does not provide a free
phase reference inside that class.

Third, the swap witness explicitly fails an arbitrary-input test for the
original jump instrument. On input l with the same beta, its reduced system
output is

    (1-p)dd*+p ll*.

It returns N=1 with probability 1-p. All original star formation jumps kill
the N=3 vector l. This is a concrete counterexample to extending this particular
fixed-input construction to the original arbitrary-input jump instrument.
It is not an impossibility proof for every other proposed dilation.

Finally, exact initial system state dd* cannot hide helpful initial system/
reservoir correlations: a pure system marginal forces the joint state to be
a product dd* tensor eta. The PRE also states the needed positivity and
finite-energy hypotheses of the heralded supply inequality explicitly.

## 6. Computation, coverage correction, and preserved failures

The PRE control completed 139 exact checks. It covers generic symbolic
two-/three-level resources, compatible heralding, incompatible readout, and
all nine actual marked outputs in the complete 32-state space at
epsilon=1/2, delta=7/5. No execution failed in that bounded PRE task.

The first POST control completed 198 checks with no failed assertion. It
matched all nine author embedding rows: three mark types at epsilon=1/2,
1/5,1/17 with delta=1. It verified the complete abstract U, full physical
unitarity, total-energy commutation, exact target output, support complement,
and the announced gaps, probabilities, energies and distances. It also checked
selector block norms and energy/coherence sums. However, its selector loop
used edge 1 as the representative state for edges 2 and 3, whose scalar
quantities agree by star symmetry. That limited its direct labeled-state
coverage despite the valid scalar results.

This coverage issue was preserved and corrected before sealing. The first
runner is `post_compare_run01.py`, hash
`2f4187793d7b918776e180528d682f4332d3607237641492d7a23b5f6892c568`,
with its original `POST_RESULTS_01.json` and logs. The current runner accepts
the actual edge label and checks every selector block's full unitary,
conservation, exact original marked state and controlled output. Run 02
completed 234 checks with no failed assertion. The final runner hash is
`d1baa1a9c3e9c05ef72c081bc70027afacdfb6565ed67561da5f35233ccb472c`.
Counts include provenance checks and repeated source authentication; they
are not counts of independent theorems or evidence of independence by volume.

At epsilon=1/5, delta=1, the reconstructed selector values are:

| Selector | Weights | Mean supplied energy | Input and flagged-output coherence |
|---|---|---:|---:|
| Six resolved marks | 1/6 each | 75/2 | 3sqrt(3)/28 + sqrt(13)/14 |
| Three coherent edge marks | 1/3 each | 75/2 | sqrt(159)/28 |

The final control checks each 32-dimensional block exactly. The direct-sum
argument establishes the controlled operator on the 192-dimensional resolved
or 96-dimensional coherent selector/system/carrier space without needlessly
forming a dense larger matrix. No floating tolerance is used. Exact symbolic
proof establishes the all-parameter assertions; finite rational samples
corroborate their physical embedding and do not replace that proof.

The author's preserved initial failure was structural symbolic equality:
`1-r/(1+r)` and `1/(1+r)` were compared without simplification. The failed
source and failure description remain in `post_sources/`. POST reproduces
that expression-form mismatch and verifies their simplified difference is
zero. The current author control's exact simplification also covers physical
low/high orthogonality. No physical formula or tolerance was changed. Earlier
independent microscopic-star failures remain in their sealed source packet;
they were not erased by this resource calculation.

Reproduce from this directory with fresh attempt identifiers:

    python3 coherent_supply_check.py --attempt pre_reproduction
    python3 post_compare.py --attempt post_reproduction

The POST runner authenticates live author sources against the released seal
before and after computation and uses only the independent star engine for
calculation. If live source bytes change, it refuses those bindings. Archived
copies preserve the exact compared revision. Existing result files are never
overwritten by these runners.

## 7. Limits, correction decision, and final state

No correction is required to the author's finite-parameter mathematical claims
as stated. Its phrase about not generating a Poisson waiting law is a scope
disclaimer: this comparison does not identify the exact microscopic waiting
law with a Poisson law. All timing and no-event dynamics remain outside the
resource construction. The author note's historical "independent reconstruction
pending" status is not silently changed by editing its sealed bytes.

The source constraints do not forbid exact formation using every imaginable
reservoir. They exclude exact coherent conditional output from the stated
stationary-reservoir, conserving-unitary, compatible-readout class. The
explicit coherent and incompatible-readout witnesses demonstrate why those
hypotheses must remain attached to the statement.

At joint scaling epsilon^2 S(S+1)=delta/K with delta,K>0 fixed, the sharp
distance in (1) tends to zero as S(S+1)^(-1/2), even though the required mean
fuel energy is c K S(S+1). The two-level carrier has dimension two for each
finite parameter value, but its gap grows as
(K^2/delta)[S(S+1)]^2+3K S(S+1). Thus neither a uniform positive density-error
floor nor a uniformly bounded energy carrier follows. Density convergence
does not control these microscopic energy moments.

No locality, bounded coupling, clock construction, reservoir replenishment,
catalytic reuse, full original-instrument implementation, GKLS implementation,
or universal autonomy no-go is proved here. The N1-N8 scope stress test is
retained in the PRE packet. It is not a formal publication/landing-schema
PASS, and this comparison does not adopt an audit status.

All changes are confined to the assigned independent folder. No editable
prompt, current-main scientific source, author source, commit, publication,
or other worker file was changed. The campaign deadline remains
2026-09-24 04:59:48 UTC. `FINAL_STATUS.md` is the current checkpoint; frozen
`STATUS.md` remains the historical PRE checkpoint. The final comparison seal
binds all PRE artifacts, all released-source copies, controls, results,
failure/coverage records, and this report.
