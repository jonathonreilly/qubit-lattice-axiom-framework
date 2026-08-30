# Independent Preregistration Attack

## Freeze basis and verdict

Review basis: committed Block19 packet 3d35ec5080, comprising
APPROACH_REGISTRY.md, GOAL.md, PANEL_RETURN.md, and
PREFLIGHT_WITNESSES.md.

No Block19 target runner or cache was present in that packet. None was
inspected, created, or executed for this review.

The preregistration verdict is:

    REVISE-BEFORE-EXECUTION

This is an adversarial preregistration artifact, not the post-result N1--N8
release certificate. The corrections below must land before any target runner
is created or executed. If they do not land, neither the positive selector
terminal nor the negative hazard-norm-underselection terminal is eligible.

The packet has a sound local CP-instrument witness and a promising
factorized-jump observation. Its present claim boundary is nevertheless
unstable in four load-bearing places:

1. the full family already admits an arbitrary positive orbit-invariant
   function h, so more than one generator ray is built into the definition;
2. the factorized raw jump operators do not, without an additional membership
   argument, establish an exact finite-delta table-free collision unitary;
3. “QND preservation” is not quantified between preservation of the classical
   pointer observable and identity of an arbitrary quantum condition state;
4. the collision cadence, fresh-ancilla supply, scaling, ordering, and
   diagonal-sector restriction remain selected protocol inputs.

Those issues do not kill the campaign. They force a narrower and more exact
one.

## Claim decomposition that must remain separate

| result surface | exact premise set | possible conclusion | conclusion not licensed |
|---|---|---|---|
| minimal matching-only raw jump family | supplied six-mark ratio p_f proportional to 2 raised to m_f; one common base coupling; one identical matching factor per neighbor; no label-blind factor; phases quotiented only at the diagonal classical-generator level | the raw jump intensities are q_f proportional to 2 raised to m_f and h_raw proportional to Z, unique up to one common positive scale inside this syntax | full-family uniqueness, a physical clock, derivation of the supplied mark ratio, or uniqueness of the quantum instrument |
| label-blind extension | the preceding raw jump grammar plus one common recorded-occupancy factor b per neighbor | either b is excluded by a frozen physical/gate condition, or b not equal to one supplies a dimensionless hazard freedom while leaving p_f fixed | a claim that “minimality” physically derives b=1 |
| arbitrary orbit-controlled collision family | orthogonal seven-state pointer, fresh seven-state ancilla, profile-controlled collision, classical-label QND, append-only one-site target, supplied p_f, range one, translation and proper-cubic covariance | if two exact same-premise nonproportional hazards survive, this stipulated collision family is hazard-norm underselected modulo global scale | all QND dynamics are underselected, no microscopic selector exists, strict-M_2 impossibility, autonomous-bath impossibility, or an axiom amendment |

The phrase “positive conditional selector” in GOAL.md:118 and
APPROACH_REGISTRY.md:9 must be demoted to a conditional raw-weight
realization/classification. The matching factor sqrt(2) is fixed only after
the Block18 probability ratio has been supplied. It is not derived from the
minimal axioms in this block.

The permitted negative terminal remains available only with an immediate
scope qualifier:

    QND-REPEATED-INTERACTION-LIFTS-EXIST-HAZARD-NORM-UNDERSELECTED

means only that the corrected, explicitly named orthogonal-pointer,
fresh-ancilla, range-one controlled-collision family contains at least two
dimensionlessly inequivalent diagonal classical generator rays. It does not
mean that QND, microscopic dynamics, or occurrence laws in general are
underselected.

## Decisive independent desk checks

### The broad h-family cannot produce the advertised positive uniqueness

GOAL.md:163-171 says that every positive bounded function constant on the
diagonal proper-cubic profile orbits is admissible. Under that declaration,
the full family is not a candidate one-ray cone.

For the simultaneous action on six neighbor slots and six nonblank direction
labels, Burnside counting gives:

| proper-cubic rotation class | multiplicity | slot cycle type | fixed profiles per element |
|---|---:|---:|---:|
| identity | 1 | 1+1+1+1+1+1 | 117649 |
| face-axis half turn | 3 | 1+1+2+2 | 441 |
| edge-axis half turn | 6 | 2+2+2 | 343 |
| face-axis quarter turn | 6 | 1+1+4 | 63 |
| body-axis third turn | 8 | 3+3 | 49 |

The Burnside sum is 121800, hence the exact orbit count is 5075. Therefore:

- the declared full positive h-cone has 5075 real parameters and 5074
  dimensionless directions after quotienting one global scale;
- the count-only family has seven positive parameters and six dimensionless
  directions; and
- the displayed h_0 and h_1 pair is already sufficient to refute one-ray
  uniqueness if both exact collisions satisfy the same corrected membership
  contract.

The primary and independent checker must rederive this census independently.
This desk check is a preregistered falsifier, not an output oracle.

The packet must choose one of two honest framings before execution:

1. freeze a stricter finite gate or Hamiltonian grammar whose allowed h-cone
   is genuinely to be derived; or
2. retain arbitrary orbit controls and state in advance that positive
   full-family uniqueness is mathematically unavailable, while testing exact
   realization and the narrow underselection certificate.

Calling arbitrary profile-dependent rotation angles one “fixed architecture”
without stating that the 5075 orbit coefficients are free couplings would
hide the target freedom in the architecture.

### A raw jump factorization is not yet an exact finite collision grammar

For the displayed matching operators J_f,

    sum_f J_f dagger J_f
      = |g|^2 Z(r) P_blank.

Taking K_f equal to sqrt(delta) J_f forces the exact no-jump completion

    K_0
      = P_rec + sqrt(1 - delta |g|^2 Z(r)) P_blank.

This is a valid CP/TP profilewise completion for a common
delta no greater than the reciprocal of the largest |g|^2 Z. But its
no-jump factor is a nonlinear common function of the entire profile.

A fixed interaction generated directly from J has bright-state Rabi
frequency |g| sqrt(Z). At finite interaction time tau its exact jump
probability is proportional to

    sin^2(tau |g| sqrt(Z)) w_f / Z,

not exactly delta |g|^2 w_f for all profiles. The desired raw generator is
recovered to first order in the weak-collision limit, or an exact
profile-dependent rotation angle can be engineered.

The packet must therefore specify one of the following:

- the minimal theorem is only about infinitesimal jump operators and the
  induced generator;
- functional calculus in the derived sum of J_f dagger J_f is an allowed
  table-free CP/unitary completion, with an explicit gate-membership proof; or
- a complete finite gate sequence or Hamiltonian realizes the exact
  finite-delta map without an unregistered profile lookup.

The phrase “no additional common profile gate” at GOAL.md:111-115 is otherwise
ambiguous: the exact no-jump branch requires common Z-dependence even when no
free common occurrence factor is added. Derived normalization must be
distinguished from a freely selectable b-factor.

### Adversarial assessment of the proposed core finite grammar

A concrete correction can remove the arbitrary-profile-control tautology from
the main result. For each candidate mark f, take one identical relation factor
per neighbor,

    P_blank + a P_same(f) + b P_other(f),

and define the target-plus-ancilla transition

    A_f
      = g |f><blank| tensor |f><0|
          product_y [P_blank + a P_same(f) + b P_other(f)].

Let H be the sum over f of A_f plus A_f dagger and set

    U_delta = exp(-i sqrt(delta) H).

This is a genuinely finite relation-factor grammar: a, b, and g are shared
coefficients rather than a profile table. On a profile with n recorded
neighbors and m_f neighbors carrying f, its bright-state coefficient is

    C_f(r) = g a^(m_f) b^(n-m_f).

Writing beta=|b|^2 and gamma=|a/b|^2 gives the first-order intensity

    q_f(r) = |g|^2 beta^n gamma^(m_f).

The supplied conditional law forces gamma=2, while beta remains free:

    h_beta(r) = |g|^2 beta^n Z(r).

Thus beta is exactly the dimensionless label-blind hazard freedom. It cannot
be absorbed into |g|^2 because n varies from profile to profile. The choices
beta=1 and beta=2 are two nonproportional members of the same grammar. This
is a substantially better main underselection attack than arbitrary h_0 and
h_1 controls. The 5075-orbit family should remain only an outer tautology
control and an exhaustive covariance census.

With positive real coefficients, the two concrete settings can be frozen as

    beta=1: b=1 and a=sqrt(2),
    beta=2: b=sqrt(2) and a=2,

with the same nonzero g modulo the one allowed global scale.

For a fixed profile, H couples |blank,0> to one normalized bright state and
annihilates every locked |g,0> input. The exact reduced Kraus coefficients are

    K_0
      = P_rec + cos(sqrt(delta h_beta(r))) P_blank,

    K_f
      = -i sin(sqrt(delta h_beta(r)))
           C_f(r) / sqrt(h_beta(r)) |f><blank|.

They are exactly CP/TP, preserve the conditional mark probability
2^(m_f)/Z at every finite delta, and have generator q_f above. This correction
also exposes a required packet change: its exact finite jump mass is
sin^2(sqrt(delta h_beta)), not delta h_beta. The two forms agree at first
order, but GOAL.md equations (1)--(3) and the exponential-Hamiltonian grammar
cannot both be asserted as the same exact finite collision.

The corrected preregistration must choose the exponential grammar as primary
and derive its first-order generator, or retain the engineered linear-in-delta
Kraus family as a separate outer control. It may not silently substitute one
for the other.

A cleaner same-Z Record-order fixture isolates beta from the supplied mark
weights. Choose two blank target sites A and B with disjoint radius-one
neighborhoods. Give A exactly two recorded neighbors carrying the same label,
and give B exactly three recorded neighbors carrying three distinct labels.
Then

    n_A=2, Z(A)=2^2+5=9,
    n_B=3, Z(B)=3 times 2 + 3=9.

In the continuous-time generator limit, conditional on the next tested site
being A or B, the B odds are

    beta / (1 + beta).

They are 1/2 for beta=1 and 2/3 for beta=2. This gives the familiar
dimensionless values without importing the old n=0/n=6 hazards and without
letting Z create the difference. A separated finite-torus fixture and its
local/cylinder infinite-volume reading must be specified as carefully as in
Block18.

As a secondary hostile control, an n=0 site has Z=6 while an n=6 site with one
of each neighbor label has Z=12, giving odds
2 beta^6/(1+2 beta^6), not beta/(1+beta). This control must reject any runner
that prints 1/2 and 2/3 from the old fixture without deriving the actual
beta-family rates.

### QND must be stated at the correct quantum resolution

A controlled unitary of the form sum_r P_r tensor U_r commutes with each
neighbor label projector and preserves every classical basis label. It need
not act as the identity channel on a coherent superposition of different
neighbor profiles; after the ancilla or target is discarded it can dephase
off-diagonal neighbor coherences.

Block19 must freeze one of these non-equivalent meanings:

- classical-label/observable QND: the projectors are conserved and diagonal
  Record configurations are unchanged as conditions; or
- complete-state QND: the entire condition density operator, including an
  arbitrary reference, is preserved.

The displayed profile-sensitive control supports the first meaning. The
second would require a separate channel theorem and directly reopens the
Block11 no-information-without-disturbance boundary. “Neighbor controls are
not changed” in GOAL.md:52-56 may not be used as complete-state rhetoric.

### The target is a diagonal generator ray, not a unique quantum instrument

Covariant phases can be invisible on the diagonal pointer algebra while
changing action on coherent states. If phases are not classified, the output
can be uniqueness of h and of the induced diagonal classical generator only.
It cannot be uniqueness of the full instrument or unitary dilation.

Likewise, one-site event arity is stipulated by the single-target,
vacuum-to-single-mark architecture in GOAL.md:21. The block may verify that
the stipulated architecture induces one-site append events; it may not report
that microscopic physics selected one-site rather than compound arity.

## N1 preregistration: normalized alternative-route registry

The following are materially distinct in primary object, load-bearing
mechanism, or terminal obligation. None has an ATTEMPTED or
RULED-OUT-BY-PRIOR honesty marker yet because this is a pre-execution review.
The final landed N1 packet must replace every preregistration status with one
of those two allowed markers and retained evidence.

| route | primary object/formulation | mechanism or invariant | attack on the prospective negative | preregistration status |
|---|---|---|---|---|
| R1 arbitrary controlled Kraus family | profile-controlled CP instrument | exact completeness and orbit covariance for arbitrary h | certify that both h_0 and h_1 really lie in one frozen family, rather than in two architectures | mandatory in scope |
| R2 minimal matching jump grammar | product jump operators J_f | one identical matching-label gain per neighbor | derive h proportional to Z up to scale and test whether a true one-ray subfamily exists | mandatory conditional-positive branch |
| R3 label-blind occupancy extension | product jump grammar with b | common recorded-neighbor gain cancels from p_f but changes h | produce a low-complexity nonproportional ray or prove that a frozen grammar excludes it | mandatory robustness attack |
| R4 fixed Hamiltonian weak-collision family | one delta-independent local interaction plus fresh ancilla | bright-state norm, centering, and weak-coupling limit | test whether unitarity and a fixed interaction constrain h more strongly than arbitrary Kraus controls | mandatory if “microscopic coupling norm” is retained |
| R5 exact finite collision completion | isometry/unitary at each delta | nonlinear no-jump functional calculus and common delta domain | determine whether the raw jump grammar extends to the advertised exact table-free collision | mandatory construction attack |
| R6 coherent-condition QND | channel on pointer conditions plus arbitrary reference | nondemolition observable versus full-state identity | test whether the QND quantifier silently excludes every profile-sensitive control | mandatory scope attack |
| R7 finite-volume collision protocol | ordered reduced maps or one simultaneous many-ancilla unitary | first-order generator and commutator/remainder control | test whether order, reset, or weak scaling changes the generator at order delta | mandatory dynamics attack |
| R8 proper-cubic orbit classification | diagonal group action on slots and labels | Burnside or direct orbit enumeration | test missed covariance constraints and the true projective h dimension | mandatory classification attack |
| R9 action/transfer selection | positive history measure or transfer generator cone | action, balance, or reflection-positivity condition | a derived extra physical condition could select one h ray | live outside the narrow family |
| R10 autonomous reusable bath | translation-covariant many-body unitary without reset | bath state, collision emergence, and physical cadence | could select a coupling and clock without fresh-ancilla freedom | live outside the narrow family |
| R11 strict-M_2 or distributed carrier | nonorthogonal qubit contents or a larger encoded pointer | alternative readout and nondemolition semantics | could realize a different microscopic family not covered here | live outside the narrow family |
| R12 compound or correlated occurrence | multi-target instrument or non-Markov history object | atomic multi-site jump or memory kernel | can change event arity and hazard classification | live outside the narrow family |

R1, R2, and R3 are not three votes for one calculation. R1 classifies an
arbitrary diagonal control function, R2 classifies a restricted product jump
syntax, and R3 tests a distinct common occupancy invariant within an extended
product syntax. R4 and R5 are also distinct: a fixed Hamiltonian limit need
not coincide with an engineered exact Kraus family.

## N2 wall-independence and collapse

The packet currently presents several witnesses as if they were independent
walls. They collapse as follows:

- the full orbit census, count-only census, h_0/h_1 pair, and b-family all
  address one family-membership/classification wall;
- CP/TP, isometry normalization, explicit unitary completion, target lock,
  and pointer readability are one exact-collision realization wall;
- product-order expansion, continuous-time convergence, exact generator
  identity, and Block18 Harris inheritance are one dynamics-bridge wall;
- the raw matching-only theorem is a separate positive branch, not an
  independent wall supporting full-family underselection.

The collapsed wall set is:

- W_F: freeze the family grammar, equivalence relation, and same-family
  membership of two candidate hazards;
- W_C: construct the exact collision and prove the stated classical-label QND,
  lock, locality, covariance, and common delta domain;
- W_L: derive the ordering-independent diagonal generator and bind it exactly
  to the scoped Block18 process;
- W_D: prove nonproportionality modulo one global scale with an exact local
  Record-order discriminator.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---:|---:|---:|
| W_F, W_C | no | no | yes |
| W_F, W_L | no | no | yes |
| W_F, W_D | no | no | yes |
| W_C, W_L | no | no | yes |
| W_C, W_D | no | no | yes |
| W_L, W_D | no | no | yes |

Block18 local-infinite existence is not a fifth independent Block19 wall once
W_L proves exact generator and initial-law equality; it is inherited at that
point and only at its retained local/cylinder scope. Similarly, the
label-blind b witness is a particularly simple witness for W_F, not an
additional negative theorem.

## N3 hidden-wall scan

| packet phrase or construction | classification | required correction |
|---|---|---|
| supplied p_f equals 2 raised to m_f divided by Z | explicit downstream input | keep “supplied” on every positive and negative terminal; do not attribute it to Block19 |
| orthogonal seven-state pointer decodes rho_f | explicit enlarged carrier, not strict M_2 | state that no physical encoder from the six qubit states is derived |
| mutually orthogonal profile projectors permit controlled rotations | hidden resource grammar | define whether arbitrary orbit tables, projector polynomials, or only bounded-factor gates are allowed |
| “table-free” | undefined syntactic/physical condition | freeze an allowlist, coefficient-sharing rule, and whether functional calculus in Z is allowed |
| fresh ancilla initialized in vacuum | explicit bath/reset import | keep reset, preparation, and ancilla supply outside minimal-axiom and autonomous-dynamics claims |
| one fresh ancilla per site and step | hidden cadence/regulator | state the collision schedule and common uncalibrated parameter; never call it a derived clock |
| delta-dependent exact rotation | hidden scaling choice | distinguish an engineered collision family from one fixed Hamiltonian weak-coupling limit |
| no-jump square root | hidden common profile dependence in the minimal grammar | prove it is a derived allowed completion or demote the exact table-free claim |
| neighbor Record condition “unchanged” | ambiguous QND quantifier | restrict to conserved pointer projectors/diagonal labels or prove complete-state preservation |
| phases do not alter the generator | valid only on the diagonal algebra | claim generator-ray, not instrument or unitary uniqueness |
| one-site append event | selected architecture premise | do not report one-site arity as selected against compound events |
| proper-cubic covariance | explicit rotations-only symmetry | rotate both slots and labels; do not silently add reflections or initial-law invariance |
| positive h | explicit strict-formation restriction | keep zero-hazard, sign-indefinite, and non-Markov families outside the result |
| “standard finite-dimensional product convergence” | proof placeholder in PREFLIGHT_WITNESSES.md:29-35 | provide the exact norm, finite-volume dependence, and product bound; a citation label is insufficient |
| Block18 inheritance | cited prior theorem with premise match still required | bind the exact generator, initial state/law, diagonal sector, local query, and rate bound |
| Born sampling or tracing of the ancilla | operational step not fully named | state the reduced-channel/instrument convention and whether the ancilla is traced, read, or retained |
| profile-dependent h is a coupling norm | terminology depends on realization | call h an infinitesimal hazard coefficient unless it is derived as the norm of one fixed microscopic interaction |

Any correction that promotes one of these conditions into an additional
physical premise must update W_F through W_D and the terminal scope. It may
not be added only after seeing a hostile witness.

## N4 residual matching and N8 cross-cycle echo

Citation keys below refer to committed sibling artifacts:

- B02C:
  ../toe-source-eta-ownership-block02-action-native-record-dilation-20260828/CLAIM_STATUS_CERTIFICATE.md
- B02L:
  ../toe-source-eta-ownership-block02-action-native-record-dilation-20260828/NO_GO_LEDGER.md
- B09C:
  ../toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/CLAIM_STATUS_CERTIFICATE.md
- B09L:
  ../toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/NO_GO_LEDGER.md
- B10C:
  ../toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829/CLAIM_STATUS_CERTIFICATE.md
- B10L:
  ../toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829/NO_GO_LEDGER.md
- B11C:
  ../toe-source-eta-ownership-block11-record-past-causal-gate-20260829/CLAIM_STATUS_CERTIFICATE.md
- B11L:
  ../toe-source-eta-ownership-block11-record-past-causal-gate-20260829/NO_GO_LEDGER.md
- B17C:
  ../toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/CLAIM_STATUS_CERTIFICATE.md
- B17L:
  ../toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/NO_GO_LEDGER.md
- B18C:
  ../toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829/CLAIM_STATUS_CERTIFICATE.md
- B18L:
  ../toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829/NO_GO_LEDGER.md

| prior cycle and exact lines | prior residual | Block19 residual | exact match? | echo disposition |
|---|---|---|---:|---|
| Block02, B02C:7-15 and B02L:12-16 | an orthogonal blank/write/lock CP-QND writer exists, but input attachment, formation rate, and persistent history are not supplied | construct a selected fresh-ancilla occurrence collision and classify its hazard norm | no | use only as a pointer/writer template; it does not support hazard selection |
| Block09, B09C:12-17 and B09L:6-14 | a conditional fourteen-outcome direction/corner kernel and source moment exist while ownership, history, rate, and clock remain open | a supplied six-mark 2 raised to m_f kernel is lifted and its scalar hazard is classified | no | the conditional-law-versus-rate seam echoes, but Block09 is not authority for the Block19 six-mark kernel |
| Block10, B10C:12-17 and B10L:6-15 | a joint action/quadrupole condition carrier exists; causal update, gain/instrument, permanent Record, history, and rate remain open | an enlarged orthogonal pointer collision addresses one gain/instrument seam | no | different carrier and update object; do not claim the Block10 physical ownership problem retired |
| Block11, B11C:19-23 and B11L:5-9 | exact separate-copy programming is empty only for product-density strict quantum conditions with complete joint prefix preservation | orthogonal label projectors control a classical-pointer collision | no | Block19 takes a named classical-pointer exit; it neither contradicts nor broadens the Block11 boundary |
| Block17, B17C:15-30 and B17L:5-13 | one compiler fails; pure-Record and microscopic repeated-interaction routes remain live; compiler depth supplies no rate or time | execute one repeated-interaction route with supplied cadence and pointer carrier | no as evidence, yes as route provenance | do not transfer the compiler failure or strict-M_2 quotient theorem into Block19 |
| Block18, B18C:23-45 and B18L:8-15 | two complete seven-state one-site Markov laws have hazards h_0 and h_1, local histories, and 1/2 versus 2/3 Record-order odds; microscopic QND selection remains open | determine whether both exact generators arise from one corrected microscopic collision family | yes only after exact generator and premise equality | this is the sole exact process residual Block19 may inherit |

Cross-cycle retirement audit:

- Block02 retired conditional readable-writer existence, not occurrence,
  physical attachment, rate, or history.
- Block09 retired one conditional capacity/source-moment seam, not dynamic
  gain, ownership, formation, or clock.
- Block10 retired joint condition-carrier existence, not a causal Record
  instrument or occurrence selector.
- Block11 retired one complete-product-density prefix-preserving copy route
  only; orthogonal classical Records were an explicit live exit.
- Block17 retired no broad locality or microscopic route. Its pure-Record exit
  was exercised in Block18; microscopic repeated interaction remained live.
- Block18 retired finite and local-infinite existence for two named classical
  hazards and retained their bounded underselection under the smaller ansatz.
  It explicitly left QND/action selection live. Block19 can narrow that live
  route only if it adds a genuine microscopic restriction rather than simply
  re-encoding arbitrary h as a controlled rotation.

No earlier cycle licenses “no microscopic selector,” “QND cannot select,” or
“a new axiom is required.”

## N5 rhetoric and resolution gate

Nothing in Block19 has yet been executed. Every row below is therefore a
future evidence obligation, not a result.

| resolution | evidence that must later be executed | strongest potentially licensed statement |
|---|---|---|
| per-element | every profile/mark radicand, Kraus completeness term, covariance image, and hostile mutation | exact local algebra for the declared profiles and marks |
| per-site | blank jump/no-jump channel, full recorded-subspace lock, classical-label QND controls, and h_0/h_1 local hazards | one-site diagonal generator membership and permanence in the selected pointer sector |
| per-mode | six mark channels, all 5075 proper-cubic profile orbits, count-only subcone, scale quotient, and phase treatment | projective dimension or at least two rays of the declared diagonal hazard cone |
| per-block | finite-torus products, all declared orderings, explicit remainder norm, and exact local-cylinder Record-order statistic | ordering-independent finite-volume diagonal generator and dimensionless discriminator |
| lattice-wide | only exact inheritance of Block18 local/cylinder Harris dynamics after generator and initial-law equality | a local-infinite classical process for the two named hazards; no global quantum collision unitary, global next event, common completion time, or physical clock |

The primary cached stdout must eventually contain substantive lines beginning
exactly with:

- per_element:
- per_site:
- per_mode:
- per_block:
- lattice_wide:

Any unexecuted resolution must say “checked and not executed” and why. A
negative terminal is forbidden until the final landed N1--N8 checklist and
those five cache lines both exist.

Required rhetoric:

> Within the frozen orthogonal-pointer, fresh-ancilla, range-one
> profile-controlled collision family, two exact admissible diagonal
> generator rays are not related by one common positive scale and give
> different local Record-order probabilities.

Forbidden rhetoric includes:

- QND does not select an occurrence law;
- microscopic dynamics is underselected;
- no unique microscopic selector exists;
- the full quantum instrument is nonunique, unless coherent-sector phases and
  channels were actually classified;
- the lattice-wide microscopic dynamics was constructed;
- Block19 derives a physical clock, autonomous bath, compound arity, strict
  M_2 readout, gravity source, axiom change, or TOE movement.

## N6 partial-closure paths

| path | what it could close | correct classification |
|---|---|---|
| freeze one finite Hamiltonian/gate grammar and derive its coupling cone | could remove arbitrary orbit controls and possibly select one ray | explicit import, then bounded theorem, then later import-retirement audit; not automatically a new axiom |
| derive b=1 from a physical normalization, balance, or reuse condition | could turn the matching-only lift into a robust selector within a stronger family | added or newly derived physical condition; report as a separate conditional selector |
| declare b=1 by “minimality” or choose h constant by convention | can define a model or canonical representative | convention/model choice, not physical selection and not evidence against underselection |
| quotient by one common positive factor | removes the uncalibrated global time unit | legitimate convention already in scope; a profile- or site-dependent factor is not the same quotient because it changes local race odds |
| action, detailed balance, DLR/OS, or transfer positivity | could select a generator ray | live conditional-physics route, not refuted by Block19 |
| autonomous bath or reusable environment | could derive reset/cadence and constrain coupling | stronger microscopic construction, not refuted by a fresh-ancilla result |
| strict-M_2, distributed pointer, compound, correlated, or non-Markov law | changes carrier, readout, arity, or history object | live route outside this family, not a loophole that the narrow terminal must close |

No primitive-registry audit was performed in this preregistration attack.
Consequently the result may not say “no retained primitive supplies this” or
any equivalent, and no axiom conclusion is available.

## N7 strongest hostile steelman

> The alleged underselection may be an artifact of calling a set of arbitrary
> profile-indexed rotation angles one microscopic architecture. A genuine
> repeated-interaction model would freeze one local Hamiltonian or finite gate
> grammar before inspecting h. Its bright-state normalization, exact no-jump
> branch, bath centering, and weak-collision scaling could force h proportional
> to Z—or another single ray—even though arbitrary controlled Kraus maps allow
> 5075 orbit coefficients. The label-blind b-factor is a second physical
> interaction, not automatically a parameter of the first. Unless both b
> values, or both h_0 and h_1, are proved members of one independently frozen
> grammar with the same ancilla preparation, cadence, QND quantifier, event
> arity, initial law, and scaling, the negative conclusion merely restates
> that unspecified couplings are unspecified.

The answer to this steelman cannot be rhetoric about symmetry. Before
execution, the packet must define the grammar and its equivalence relation.
After execution, two complete membership certificates and one local
dimensionless discriminator are required. Even a successful answer supports
only the named family boundary.

## Mandatory corrections before any runner execution

1. Replace the ambiguous “fixed architecture” language with an exact
   admissible gate/Kraus/Hamiltonian grammar and identify every free
   coefficient.
2. Choose whether arbitrary 5075-orbit profile controls are allowed. If they
   are, acknowledge that the positive full-family one-ray terminal is
   unavailable by definition. If they are not, state the stricter grammar and
   derive, rather than assume, its h-cone.
3. Define “table-free” operationally: allowed projectors, products, sums,
   functional calculus, coefficient sharing, and whether an orbit lookup in
   the unitary is forbidden.
4. Separate the minimal matching raw-jump theorem from exact finite-delta
   collision realization. Prove membership of the forced no-jump square root,
   or state that the theorem is generator-level only.
5. Freeze the QND quantifier as conserved classical label projectors/diagonal
   Record states, or add the stronger complete-state channel test. Do not
   alternate between them.
6. State explicitly that p_f and its doubling ratio are supplied. Rename the
   minimal result so it cannot be read as deriving that conditional law.
7. Freeze the collision protocol: ancilla initialization, trace/read
   convention, fresh reset, one-collision-per-site regulator, common delta
   domain, ordered reduced maps versus simultaneous unitary, and the
   uncalibrated time parameter.
8. For a simultaneous microscopic unitary and for each declared product
   ordering, specify the norm and prove the first-order remainder at the
   resolution actually claimed. Do not transfer an O(delta squared) reduced
   map statement to overlapping O(sqrt(delta)) unitaries without proof.
9. Require two same-premise membership certificates: identical carrier,
   ancilla dimension/state, QND meaning, support, covariance, event arity,
   collision protocol, scaling, initial law, and a shared positive delta
   interval.
10. Freeze the equivalence relation to one global positive multiplier.
    Profile-dependent or site-dependent time changes are not quotiented away.
11. Reproduce the 5075-orbit census, full projective dimension 5074, and
    count-only projective dimension six independently, rotating slots and
    labels together.
12. Bind the h_0/h_1 comparison to the exact Block18 local fixture or local
    right-derivative event that yields 1/2 versus 2/3. State all conditioning
    and initial-law data; never use a global next-event construction.
13. Use the frozen same-Z profiles A=(n=2, two equal labels, Z=9) and
    B=(n=3, three distinct labels, Z=9), with beta=1 and beta=2, as the primary
    relation-factor discriminator. Prove the common-delta bound,
    nonproportionality, and B-first odds 1/2 versus 2/3. The old n=0/n=6
    fixture is a hostile control, not an oracle for these rates.
14. Emit three separately named results: matching-only conditional raw-weight
    theorem; b-extension robustness verdict; arbitrary-orbit-family
    classification/underselection verdict.
15. Restrict uniqueness to the diagonal classical generator unless all
    coherent-sector phases and channels are classified. Restrict QND to the
    declared pointer observable unless complete-state preservation is proved.
16. State that one-site arity, orthogonal pointer enlargement, fresh bath, and
    reset are family premises, not minimal-axiom derivations.
17. Bind Block18 inheritance by exact generator, sector, rate bound,
    initial-law, and local/cylinder equality. No lattice-wide quantum
    repeated-interaction process is inherited.
18. Freeze a terminal matrix covering positive uniqueness, narrow
    underselection, conditional-only raw theorem, construction failure, and
    inconclusive classification.
19. Require independent reconstruction without importing primary output or
    treating the anticipated h-pair, orbit count, or desired terminal as a
    test oracle.
20. Land a final N1--N8 checklist and the five substantive N5 cache lines
    before any negative terminal ships.

## Kill criteria and terminal matrix

| observed result | required disposition |
|---|---|
| family grammar or QND quantifier remains ambiguous | stop before execution; REVISE-BEFORE-EXECUTION |
| either candidate fails CP/TP, explicit unitary completion, lock, stated QND, locality, covariance, or common-delta membership | construction-specific failure at the first exact gate; no underselection inference |
| ordered or simultaneous protocol changes the diagonal generator at first order, or no controlled limit is proved | scaling/protocol construction failure; no microscopic impossibility claim |
| exact generator does not equal the named Block18 generator | no Harris inheritance and no reuse of the 1/2 versus 2/3 certificate |
| two hazards differ only by one global positive factor | no underselection; classification remains open unless the entire cone is proved one ray |
| two nonproportional hazards survive but differ in carrier, bath, schedule, arity, initial law, or scaling | invalid comparison; no same-premise terminal |
| one local dimensionless Record-order event differs after all common premises pass | narrow family underselection becomes eligible, subject to final N1--N8 and N5 |
| minimal matching family is one ray but b survives | ship the conditional raw-weight subtheorem and the separate b-robustness failure; do not ship a full selector |
| b is excluded only by syntax called “minimal” | conditional matching-only theorem only; physical robustness unresolved |
| the complete corrected family is independently proved one ray modulo global scale and every construction/limit gate passes | positive generator-selection theorem inside the explicitly imported collision family; no physical clock or full-instrument uniqueness unless separately proved |
| enumeration or classification is incomplete | INCONCLUSIVE or construction-specific partial result; do not infer uniqueness from one example |
| final N1--N8 artifact or any N5 resolution line is absent | negative terminal blocked regardless of numerical output |

Hard release kill criteria are:

- any hidden profile table counted as a derived selector;
- any raw weight normalized by Z and then reported as if occurrence hazard
  were fixed;
- any exact-unitary claim based only on generic Stinespring existence;
- any “unchanged neighbor” claim tested only on basis labels but stated for
  arbitrary quantum conditions;
- any finite scan order or collision count called physical time;
- any environment reset or weak-coupling scaling attributed to the minimal
  axioms;
- any h-pair compared on different delta domains or different protocols;
- any slot-only or label-only cubic action;
- any local finite-volume result promoted to a global infinite-lattice jump
  chain or quantum unitary;
- any strict-M_2, compound-event, autonomous-bath, action-selection,
  gravity-source, foundation, axiom, audit, obligation, or TOE upgrade.

## Frozen preregistration disposition

The corrected campaign can still produce a worthwhile two-part result:

1. a positive conditional theorem that the supplied 2 raised to m_f ratios
   have a simple matching-only raw jump lift with h proportional to Z; and
2. a narrow negative theorem that one explicitly frozen orthogonal-pointer
   collision grammar admits at least two dimensionlessly inequivalent hazard
   rays.

Those conclusions are logically compatible and must remain separately
scoped. The first does not prove full-family robustness. The second does not
erase the first and does not reach other microscopic families.

Until all twenty corrections above land, the execution gate remains:

    BLOCK19-PREREG-REVISE-BEFORE-EXECUTION

This review freezes only the adversarial correction record. It makes no
runner, cache, claim-status, axiom, audit, or repository-history mutation.
