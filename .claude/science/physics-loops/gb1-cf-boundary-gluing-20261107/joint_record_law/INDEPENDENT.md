# Independent joint permanent-record proof check

Date: 2026-11-09. Working status: completed bounded hand proof and counterexamples.
Research check only; no audit verdict, retained status, or axiom amendment.

## Contract, provenance, and recovery checkpoint

Question: can a joint permanent-record law realize Bell violations through
the quantum CHSH limit without a stored answer table or setting transmission
between detectors, and can that law obey the current Admissibility clause at
intermediate one-record states? The decisive test is equality of the second
event's conditional kernel in two full record states having the same local
neighborhood. Distinguish an atomic pair kernel from a sequence of locally
causal draws, and from local quantum instruments on an entangled carrier.

Pinned current main: `1e0d3b58dcda7f83152b0bb51729260247454d65`.
Science parent: `c7f096b935e85741ac365341ea550a9d465a37d7`.
Checker worktree HEAD at launch: `f5af11cd0102cfd0b51aef0911f600130bf5beb1`;
its `origin/main` was the pinned main above. No fetch was performed. The
requested first command, `python3 scripts/lab_ops.py preflight`, internally
tested origin reachability; no further network access is used. Its complete
stdout was:

```text
ok      disk: 111 GB free, limit 10
ok      memory: 28% free, limit 25
note    load: 37.8, limit 8
note    model floor: no target named, no floor checked
ok      nice: works here
note    memory cap: ulimit unavailable; a job must watch its own memory
ok      network: origin reachable
preflight: go
```

This is host subagent `/root/joint_record_check`, with a restricted neutral
brief and no supervisor candidate. Pairing provenance is same-family,
separate-context research checking; it is not backend-attested model-family
or audit independence. The assigned model/reasoning setting is the parent's
selected high-reasoning setting, without downgrade. No first-event backend
model slug or reasoning-effort attestation was exposed to this worker, so no
such attestation is claimed. This pure hand proof launches no numeric job.
Two preliminary messages sent the supervisor the joint/sequential distinction
and legacy Busch premise issue before its candidate freeze. No candidate was
read here, but that overlap means the pairing is not described as fully blind.

All scientific inputs below were read completely from
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics` and compared byte-for-byte
with the pinned commits. The forthcoming `joint_record_law` candidate was not
read. Existing dirty files in the checker worktree are preserved. The only
deliverable and only file edited is this file.

| Input | SHA-256 | Revision match |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | `301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc` | main and science parent |
| `.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/foundational_bell/RESULT.md` | `b408820a8e38f969a21f70d6d8a53c05172cddfc52dfeba2f74ecb9c964ee321` | science parent; absent from main |
| `docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` | `18f535e625cc7da0198c0d15cb80c551a6b4acdd2b11d41e5dd071bc188cdbb1` | main and science parent |
| `docs/NATIVE_PARITY_ENTANGLER_AND_CHSH_NOTE_2026-09-08.md` | `717244104b90bdbb15a6383f6cf966afc2ad5497045085594b7908237f0384b0` | main and science parent |
| `docs/ai_methodology/SCIENCE_WORKFLOW.md` | `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca` | main and science parent |
| `docs/ai_methodology/skills/workhorse/SKILL.md` | `e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8` | main and science parent |
| `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` | `b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0` | read from pinned main |
| `docs/ai_methodology/skills/no-go-discipline/SKILL.md` | `9020ba5c2797d8f026ddb72871b13f18a18cad4e0ec326c0f4653ceb438751bc` | read from pinned main |

Applicable procedure is the pinned-main workflow/workhorse, with freshness
and negative-claim discipline read at the same revision. The initially read
installed workhorse copy was stale; pinned-main instructions replaced it.
The preexisting checkout's workflow was also superseded by the completely read
pinned-main version. No editable prompt file was changed. This bounded check
reuses the supplied sources' prior-art record (Bell/CHSH, Tsirelson,
Busch/CFMR, and the native conditional preparation); no new literature or PR
search was run under the explicit no-network instruction. The arguments
below are hand verifications of elementary probability and finite operator
algebra, not novelty or experimental claims.

Current checkpoint: complete hand argument below. Sources are pinned; the
atomic construction, CHSH bound, PR alternative, and intermediate-state
contradiction are closed within their stated domains. No supervisor candidate
has been read. The remaining scientific decision is which formation and
conditional-probability meaning is intended physically; no new physical
premise or axiom interpretation is silently adopted here.

## 1. Three different claims must be separated

The current axioms supply one-site `M_2(C)`, a fixed covariant neighborhood
distribution, permanent supported record contents, and record-only states.
They do not supply a composite state space, a Born assignment, quantum
instruments, a production schedule, or a physical propagation speed. The
following are therefore different assertions:

1. A law on complete record configurations has a **joint pair transition**,
   whose one-site marginals obey Admissibility. This has an affirmative
   conditional construction below.
2. The two outcomes are generated by a **classically local causal mechanism**
   with setting-independent common causes. Its CHSH bound is 2, whether or
   not any physical answer table exists.
3. Local quantum instruments on a **supplied entangled composite carrier**
   give the joint law without a setting message. This is standard quantum
   measurement theory. Identifying its conditional quantum state with the
   future odds of a record-only process requires a separate locality check.

For that check, write `R` for the complete record configuration and `N_i(R)`
for all record slots in the specified neighborhood of site `i`, excluding
the site itself. The natural state-kernel reading of Admissibility is

    P(new content at i in C | full R, i forms next) = F(N_i(R))(C).   (K)

For a joint event, replace `i forms next` by the specified event containing
`i`, and take its `i` marginal. The interpretation being tested must specify
whether a joint-event selection can itself alter that marginal. The
construction below has only one possible outcome event at its ready state,
so this ambiguity does not arise there. A weaker statement concerning only
`P(content | local records)` or only an average over unread remote outcomes
is different from (K). The final contradiction applies to (K), not to every
possible weaker interpretation of the English axiom.

## 2. Explicit finite atomic construction

This is a supplied conditional law on a stated apparatus domain. Its
probability and support claims are proved here; its identification with a
real laboratory or with an axiom-derived formation mechanism is not claimed.

### 2.1 Contents and one fixed neighborhood rule

Let `I` be the `2 x 2` identity. Choose local setting alternatives

    H_A0, H_A1, H_B0, H_B1 in Herm(M_2),
    Tr(H)=0, H^2=I,

with the two alternatives within each wing distinct. These are supplied
calibration data. Put `S(H)=2I+H`, `T=10I`, and `V_v=(20+v)I`, where
`0<=v<=1` is a supplied preparation parameter. Outcome record contents are
`+I` and `-I`. The native readout can be matrix identity; assigning the
outcome number `s` to content `sI` depends on that content alone. A site's
role in trial analysis does not alter its readout. Setting labels `x,y`
denote the actually recorded menu choices; no blank site is read.

Define `F` for **every** six-neighbor record pattern, using all six slots:

* If precisely two neighbor slots are occupied, with contents `{T,S(H)}`
  for a traceless Hermitian involution `H`, return
  `(delta_I + delta_(-I))/2`.
* Otherwise, if at least one slot is occupied, return the empirical measure
  of all occupied neighbor contents, with multiplicity.
* If no slot is occupied, return `delta_0`.

This is a probability kernel on the full local possibility domain, with
unambiguous branches and nonnegative normalized weights. The predicates are
algebraic/Borel. It varies with the neighborhood and is covariant under
translations and proper cubic rotations because it depends on a multiset,
not a preferred direction. Its local algebra predicates are invariant
under unitary conjugation; scalar contents and the matrix identity provide
no fixed eigenbasis. The inter-wing comparison used below additionally
requires the explicitly supplied common calibration of the two local
matrix presentations.

### 2.2 Geometry, support, and genuinely record-only progress

Use a prepared oriented frame `e_1,e_2,e_3`. The allowed domain includes all
translations and proper cubic rotations of this entire configuration.
Let detector centers be `d_A=0`, `d_B=20e_1`. For wing `D=A,B`, prepare:

| Sites relative to `d_D` | Record content |
|---|---|
| `-2e_1`, `-3e_1` | `S(H_D0)` at both |
| `-e_1+e_2`, `-e_1+2e_2` | `S(H_D1)` at both |
| `e_1`, `2e_1` | `T` at both |

The setting port `d_D-e_1` and detector center `d_D` start blank. Prepare
the two source records `V_v` at `10e_2` and `10e_2+e_3`. Every other site
is blank. The spatial template, including the distinct source and trigger
tags, identifies the roles and frame from records, up to the simultaneous
translations/rotations already included. The wing closest to the source is
`A`; the trigger ray fixes `+e_1`, the option-1 ray fixes `+e_2`, and the
ordered source distances from `d_A` fix the source offset `+e_3`. There is
no externally stored phase counter or privileged absolute site.

The law's supplied domain consists of these preparations and their prefixes:
zero, one, or two filled setting ports, followed by a single event filling
**both** detector centers, then absorption. Each setting port can contain
either of its two menu contents. A state with exactly one detector outcome
is excluded from this atomic protocol's domain. The domain is an explicit
structural condition, not a list of favored outcome values.

The next-event rule is a function of the records:

1. With two blank setting ports, choose either port with probability `1/2`
   and draw its content from `F`.
2. With one blank setting port, fill it from `F`.
3. With both setting ports filled and both centers blank, make the joint
   outcome event in section 2.3.
4. With both centers filled, leave the state unchanged.

At a setting event the port's complete occupied neighborhood consists of
its two option records, so each alternative has probability `1/2`. The
order-selection probability is independent of their values. Summing over
the two possible orders gives `P(x,y | v)=1/4`. Thus the choices are
independent of the source parameter and each other in this model. The
scheduler is supplied; the lattice axioms do not derive its timing or its
knowledge that both ports are occupied. In this model its choice of setting
port depends on occupancy, not on a remote setting's content.

At a ready detector the complete occupied neighborhood is exactly
`{T,S(H_Dx)}`. Thus its required one-site marginal is fair. All permanent
records remain supported at every visited state: each initial menu,
trigger, and source record keeps its same-content buddy; the setting port
keeps both options among its neighbors after an outcome is added; and a
formed detector keeps its unchanged `{T,S}` neighborhood. No initial
record's neighborhood ever satisfies the special `{T,S}` branch. The
gadgets and source are separated enough that there are no omitted
cross-gadget neighbors. Every update adds records at blank sites and never
changes a prior content. There are 14 prepared records, two setting records,
and two outcome records, hence at most 18 records in a trial.

These checks use the full neighborhoods, including the effect of newly
formed records on old neighbors. They do not rely on interpreting an
unsupported permanent record as legal.

### 2.3 Analytic joint kernel, normalization, and CHSH

Given the now recorded choices, put

    c_xy = (1/2) Tr(H_Ax H_By),
    p_v(s,t | x,y) = (1 - v s t c_xy)/4,    s,t in {+1,-1}.       (J)

The common matrix identification/calibration in this formula is supplied.
The Hilbert-Schmidt inequality and `Tr(H^2)=2` give `c_xy` real and
`|c_xy|<=1`. Consequently (J) is nonnegative, normalized, and satisfies

    sum_t p_v(s,t | x,y) = 1/2,
    sum_s p_v(s,t | x,y) = 1/2,
    E_xy = sum_(s,t) s t p_v(s,t | x,y) = -v c_xy.               (2)

The joint event locks `sI` at `d_A` and `tI` at `d_B`. Its marginals exactly
match `F` at both sites, conditional on the complete pre-event record
configuration. There is no intermediate single-outcome state in this event.
All earlier and later support and permanence checks above still apply.

The rule computes (J) from the actually chosen local direction records and
the source parameter. It does not store the four outcome distributions,
sample a future outcome table, or route setting-content records between
the detectors. The two stored menu alternatives at each wing are apparatus
settings, not responses to future settings. The claim is about this literal
implementation of the stochastic law, not about the impossibility of
mathematically rewriting a finite probability distribution as a table.

Write `H_Ax=a_x dot sigma`, `H_By=b_y dot sigma`, with unit real vectors.
Then `c_xy=a_x dot b_y`, and

    S/v = |a_0 dot (b_0+b_1) + a_1 dot (b_0-b_1)|
        <= ||b_0+b_1|| + ||b_0-b_1||
        <= sqrt(2[||b_0+b_1||^2 + ||b_0-b_1||^2])
        = 2 sqrt(2),                                           (3)

where `v=0` is treated directly by `S=0`, rather than dividing by zero.
Take `a_0=z`, `a_1=x`, `b_0=-(z+x)/sqrt(2)`,
`b_1=-(z-x)/sqrt(2)`. Equation (2) becomes

    (E_00,E_01,E_10,E_11) = (v/sqrt(2))(1,1,1,-1),
    S=2 sqrt(2) v.

Thus this one analytic family attains every score in `[0,2sqrt(2)]`, with
violations for `v>1/sqrt(2)`. These are exact distributions, not claims about
a finite-sample score, and the direction choices are supplied rather than
predicted. Equation (3) is the standard inner-product form of the Tsirelson
bound, independently checked here rather than inferred from a numeric test.

The standard quantum realization is

    rho_v = v |psi^-><psi^-| + (1-v) I_4/4,
    |psi^-> = (|01>-|10>)/sqrt(2),
    P_s^x=(I+s H_Ax)/2, Q_t^y=(I+t H_By)/2,
    p_v(s,t|x,y)=Tr[rho_v(P_s^x tensor Q_t^y)].                 (4)

For the singlet, the one-site Pauli means vanish and
`<sigma_j tensor sigma_k>=-delta_jk`: same-axis products act as `-I`
on the singlet and off-axis products have zero expectation, directly from
the two displayed basis vectors. Expanding the product effects gives (J).
`rho_v` is positive and normalized as a convex combination. This verifies
the quantum representation; it does not derive the operational Born
identification from the record axioms. In the record-only construction
`rho_v` is a calculational function of the recorded `v` and the supplied
preparation convention, not an independently evolving hidden state.

### 2.4 What this construction says about locality

It contains a **spatially extended atomic stochastic event**. No setting
message travels through a sequence of lattice records, and all one-wing
outcome marginals are independent of the other setting. This is a precise
operational no-signalling statement for the declared trial. It is not a
derivation of a locally causal formation mechanism, a light cone, or
relativistic simultaneity. A centralized sampler of (J) would need both
settings; calling that sampler a local mechanism would be false.

If the atomic event is represented as one causal node with parents `x,y`
and children `s,t`, that graph has setting-to-opposite-output paths. If it
is left as a primitive joint transition, it has not supplied the separate
local causal nodes required by the Bell factorization theorem. Therefore
the construction does **not** pass the stronger no-directed-path test in
the foundational Bell source. It answers the weaker question of a joint
record law with no explicit detector-to-detector message. The distinction
is physical, not merely a choice of notation.

### 2.5 Same records and local rule also permit a PR joint law

Keep the complete initial preparation, local setting process, `F`, record
contents, and atomic event schedule above fixed. Replace only (J) by

    p_PR(s,t | x,y) = [1 + s t (-1)^(x y)]/4.                  (5)

The setting labels are recovered from the actual setting records and their
two stored menu positions. Formula (5), like (J), stores no answer table.
It is normalized and nonnegative; both marginals equal `1/2`. The same
record-support proof applies without any change. It gives
`E_xy=(-1)^(xy)` and `S=4`.

This is a matching-premises counterexample to the implication "the current
one-site Admissibility and permanent records, plus no-signalling output
marginals and no stored table, select the quantum bound." It is not a
physical PR-box prediction. The geometric/Born **joint** probability
condition in (J), absent from those premises, is doing the quantum-bound
work. The setting menu itself does not enforce it.

## 3. Exact intermediate-record counterexample

Now request a different protocol: after both settings are recorded, Alice
forms her permanent outcome first; Bob subsequently forms his outcome
without any change in Bob's six-neighbor record pattern. Both Alice
outcomes occur with probability `1/2`, and Bob is formed next for either
outcome, with no outcome-dependent filtering or intervening relay.

For a fixed `x,y`, let `R^+` and `R^-` be the resulting full record states.
Their Bob neighborhoods are identical to the pre-outcome neighborhood, so
(K) requires

    P(t=+1 | full R^+, B forms next)
      = P(t=+1 | full R^-, B forms next) = 1/2.                 (6)

But retaining the joint distribution (J) in a two-step realization requires,
by ordinary conditional probability,

    P(t | x,y,s) = (1 - v s t c_xy)/2.                         (7)

For the displayed CHSH settings, `c_00=-1/sqrt(2)`. At `x=y=0`, the two
probabilities of `t=+1` in (7) are

    (1+v/sqrt(2))/2 and (1-v/sqrt(2))/2.                        (8)

For every `v>0`, they differ; for `v=1`, both first branches and every
joint outcome still have positive probability. Thus there is no
zero-probability conditional or support-boundary loophole. Equations
(6) and (8) directly contradict one another.

This kills the precise assertion that the atomic law's Born probabilities
extend unchanged to these accessible one-outcome states while retaining
(K), unchanged Bob neighborhoods, and guaranteed next formation at Bob.
It does **not** kill the atomic law, a different physical meaning of
Admissibility, a process that changes Bob's local conditions, or a model
with extra nonrecord quantum state. Simply declaring a singly completed
state absorbing avoids Bob's event and therefore fails to realize the
requested two-outcome sequential trial. Merely averaging over Alice's
unread result recovers `1/2` but does not satisfy a condition on each full
record state. Local unreadability of a remote record is not its absence
from the record-only state.

The example also shows why order independence of commuting quantum
instruments is insufficient. They give equal **joint distributions** in
either order; neither order has a second, full-history conditional equal
to its unconditioned marginal. An atomic pair rule and either sequential
instrument realization agree on completed trials but have different
intermediate-state requirements.

For comparison, the broader Bell/CHSH bound under local causal
factorization follows without a physically stored answer table. If the
complete causal mechanism, including scheduler and stopping, supplies

    p(s,t|x,y)=integral mu(dlambda) p_A(s|x,lambda) p_B(t|y,lambda),
    mu(dlambda|x,y)=mu(dlambda),                               (9)

put `A_x=E[s|x,lambda]`, `B_y=E[t|y,lambda]`, each in `[-1,1]`.
Pointwise,

    |A_0(B_0+B_1)+A_1(B_0-B_1)|
       <= |B_0+B_1|+|B_0-B_1|
       = 2 max(|B_0|,|B_1|) <= 2.

Integrating proves `S<=2`. The mathematical response kernels in (9) need
not be stored or read anywhere. Shared correlations in stochastic inputs
must be included in `lambda`; a new indivisible joint outcome noise law is
not an implementation of the factorization. The foundational Bell source
correctly derives (9) only from additional complete causal and setting
independence hypotheses, including all non-setting exogenous inputs. The
present proof does not replace those hypotheses with marginal locality.

## 4. What local quantum instruments do and do not establish

Supply the tensor carrier and `rho_v` of (4). The local projective
instruments have branch maps

    A_s^x(X) = (P_s^x tensor I) X (P_s^x tensor I),
    B_t^y(X) = (I tensor Q_t^y) X (I tensor Q_t^y).

They are completely positive. Summing over a wing's outcomes preserves
trace. Each map is specified with its own setting only, and the wing maps
commute. Taking the trace of either order's composite branch gives (4).
This is an explicit quantum-local implementation in the usual operational
sense, conditional on the quantum carrier, preparation, and instruments.

For any Bob effect `G`, the nonselective Alice channel satisfies

    sum_s Tr[(P_s^x tensor I) rho_v (P_s^x tensor I)
             (I tensor G)]
       = Tr[rho_v(I tensor G)].                               (10)

The equality uses cyclic trace, commutation across factors, and
`sum_s P_s^x=I`. It extends to any trace-preserving local quantum channel
by its adjoint sending `I` to `I`. Thus Alice's choice of setting or of
whether to make this unreported measurement cannot signal to Bob through
his local outcome statistics. The corresponding statement holds in the
other direction. No setting transmission is needed to specify either
instrument.

After **selecting** Alice's permanent outcome, however,

    rho_(B|s,x) = [I - v s H_Ax]/2,
    Tr[rho_(B|s,x) Q_t^y] = (1 - v s t c_xy)/2.                (11)

This follows by partially tracing the Pauli expansion of `rho_v`, not by
an assumption that Bob receives Alice's record. Bob's unconditioned
description remains `I/2` until the result is available to him. The
selective conditional and the unconditioned local statistics are different
mathematical objects; no contradiction with operational no-signalling
arises.

A record-only account can reconstruct the normalized conditional operator
from preparation and the entire record history rather than treat it as
an independent ontic state. That is a legitimate calculational
representation, provided the history has actually been retained. It does
not make (11) neighborhood-local: it explicitly depends on Alice's distant
permanent record. It therefore reproduces the same incompatibility with
(K) when one-outcome histories are real states. Conversely, making the
quantum carrier an additional independent state evades that particular
record-only demand but is an additional physical state premise. Neither
move is silently licensed by the one-site algebra axiom.

### Irreversible readout and preparation

Attach the classical branch label `s` or `t` to a fresh record site, store
the matrix content `sI` or `tI`, and never overwrite it. This retains every
outcome and obeys content-determined readout. Later measurement channels
act on the remaining quantum carriers, not by rotating or erasing the
already formed record. Absence of a record is a blank slot, not a readable
third outcome. Both the instrument-to-record identification and the
irreversible registration rule are supplied; unitary algebra alone does
not select them. Repeating an incompatible terminal setting requires
fresh prepared carriers and fresh record sites. The Bell statistic does
not demand measuring all four setting combinations on one consumed pair.

The present 18-record construction starts from a supported prepared
configuration. It does not derive the formation history or physical
entanglement capability of that preparation. Encoding `v` in a source
record gives a compact source label, not a preparation theorem. The native
parity note offers a conditional alternative: its explicit signed-pulse
and middle-record protocol prepares a Bell resource with probability
`1/2`, retaining the failure record as well. Its carrier, pulse controls,
Born/Lueders instrument, placement, and schedule remain supplied. A
successful herald preceding independent setting choices can define an
event-ready population without a setting-dependent outcome filter; a
herald chosen after settings or outcomes needs a new causal analysis.
The existing native note does not by itself settle (K) for the full
conditional record histories considered here.

## 5. Exactly what selects quantum joint probabilities

Ordinary probabilities on local possibilities do not automatically give
an effect probability functional. A probability measure `mu` on the space
`M_2(C)` is a measure on sets of matrix-valued possibilities. A quantum
effect functional `m(E)` assigns a probability to an operator representing
an event; it must identify operator addition with operational
coarse-graining across all allowed POVMs. These are additional
identifications. For a simple mathematical counterexample, `mu=delta_I`
is a normalized measure on matrix contents. The naive assignment
`m(E)=mu({E})` has `m(I)=1` but `m(I/2)+m(I/2)=0`, although the two labeled
effects `{I/2,I/2}` sum to `I`. Normalization of a measure on contents does
not imply POVM additivity.

The Busch/CFMR statement can be checked directly at dimension four, but
its **hypotheses** must be supplied there. Suppose one supplies:

* a composite effect algebra `0<=E<=I` in `M_4(C)`;
* a single context-independent `m` on all those effects, taking values in
  `[0,1]`, with `m(0)=0`, `m(I)=1`, and `sum_i m(E_i)=1` for every finite
  POVM `sum_i E_i=I`;
* the operational identification that the actual joint record event in a
  pair of local settings is the product effect `P_s^x tensor Q_t^y`, with
  probability `m(P_s^x tensor Q_t^y)`.

Here is a complete finite-dimensional representation argument, credited to
the standard Busch/CFMR effect-Gleason mechanism rather than claimed new.
The two-outcome complement POVM and a three-outcome POVM give partial
additivity `m(E+G)=m(E)+m(G)` whenever `E+G<=I`. This gives monotonicity and
rational homogeneity. For real `0<=t<=1`, squeeze `t` between increasing
and decreasing rational sequences; monotonicity then gives
`m(tE)=t m(E)` without an independent continuity hypothesis.

For any positive matrix `A`, choose `c>0` with `c>=||A||` and define
`L_+(A)=c m(A/c)`, with `L_+(0)=0`. If `c' >= c`, homogeneity gives the
same value at `c'`, so the definition is independent of the scale. Choosing
one scale exceeding `||A+B||` proves additivity on the positive cone;
the same scaling argument proves nonnegative real homogeneity. Define
`L(A-B)=L_+(A)-L_+(B)` for positive `A,B`. If `A-B=A'-B'`, then
`A+B'=A'+B`, and cone additivity makes this definition independent of
decomposition. It is a real-linear functional on `Herm(M_4)`.

The finite-dimensional real trace inner product represents this functional
uniquely as `L(H)=Tr(rho H)` for a Hermitian `rho`. Normalization gives
`Tr rho=1`; nonnegativity on every rank-one projector gives
`<u|rho|u> >= 0` for every vector `u`, hence `rho>=0`. Therefore

    m(E)=Tr(rho E)                                            (12)

for a unique density matrix. This proof establishes the conditional
representation theorem. It supplies neither the composite algebra nor the
effect/event identification or POVM additivity as physics premises.

In particular, one-site effect-Gleason alone does not determine any of the
joint correlators. Every `rho_v` in (4) has the same two one-site
functionals `m_A(E)=Tr(E)/2`, `m_B(G)=Tr(G)/2`, while its correlations
vary with `v`. The PR table (5) also has those marginals for the declared
binary settings; it is not claimed to extend to a global positive
POVM-additive functional on `M_4`. That is exactly the missing joint
requirement that excludes it.

Once (12), the product-event identification, and local binary effects are
supplied, the **general** quantum CHSH upper bound follows without a
projective-measurement restriction. Put `A_x=E_+^x-E_-^x` and
`B_y=F_+^y-F_-^y`, self-adjoint contractions on the two factors. In the
Hilbert-Schmidt real inner-product space let

    u_x=(A_x tensor I) sqrt(rho),
    w_y=(I tensor B_y) sqrt(rho).

Their norms are at most one and
`E_xy=Re Tr(u_x^dagger w_y)`. Cauchy-Schwarz and the parallelogram identity
give

    S <= ||w_0+w_1|| + ||w_0-w_1||
      <= sqrt(2[2||w_0||^2+2||w_1||^2]) <= 2sqrt(2).          (13)

This is another standard Tsirelson proof, checked here for mixed states
and general binary POVMs. It addresses the quantum class defined by the
supplied hypotheses, not every admissible record law. Saturation still
needs an appropriate entangled preparation and calibrated settings.

The June 5 Busch source retains a legacy sentence in section 1 presenting
the tensor carrier as Lattice + Quantum content. That wording is not
imported into the current argument: the current June 29 axiom memo supplies
the one-site `M_2` domain and explicitly leaves Born/measurement/update
bridges outside its content. The present composite carrier and physical
probability identifications remain separately supplied. This report does
not change that source note or any source/audit status.

## 6. Assumption ledger and final research result

The following choices are explicitly supplied, not claimed independent of
one another and not newly adopted framework axioms:

| Choice | Where it is used and what it does not establish |
|---|---|
| Finite prepared apparatus, exact matrix menu contents, source label `v`, common calibration, and content-to-outcome interpretation | Defines a legal conditional trial. It does not derive preparation, a physical detector, or the setting angles. |
| Explicit extensional neighborhood rule `F` | A compatible candidate function with full-neighborhood support checks. The axioms require a fixed rule but do not choose this rule. |
| Record-dependent event selector and stopping rule | Completes the finite process without a hidden phase counter. It supplies no time metric, rate, light cone, or physical distributed scheduler. |
| Independent local setting draws, source independence, and an unfiltered declared trial population | Justifies the setting-conditioned statistics. This is checked for the finite law, not inferred for a laboratory. |
| Spatially extended atomic pair event, with no accessible one-outcome prefix in its domain | Allows a nonfactorizable joint law while keeping full-pre-state one-site marginals local. It is the explicit escape from the sequential contradiction; it is not a local causal implementation. |
| Singlet inner-product kernel (J), including the quantitative coefficient and common inter-wing operator identification | Enforces the displayed quantum bound. PR kernel (5) shows this is extra joint probability content. |
| Positive composite quantum state, tensor/product effects, and a single POVM-additive event probability functional, when the general quantum class is invoked | Gives the general bound (13). One-site `M_2` or one-site effect-Gleason alone does not supply it. |
| Entangled preparation plus calibrated settings | Gives saturation. Generic positive composite states need not violate CHSH. |
| Local completely positive instruments and permanent registration of each branch, when a sequential quantum implementation is invoked | Gives ordinary no-signalling quantum operations. Their full-history conditional probabilities fail (K) in the exhibited intermediate states. |
| Fresh records/preparations for repeated trials and a bridge from formal probabilities to measured frequencies | Needed for an empirical claim. No experiment or finite-sample inference is made here. |

**Closed result.** A record-only law can have an analytic atomic joint
transition attaining `2sqrt(2)` with fresh permanent outcomes and no stored
answer table or explicit setting-message relay. The displayed construction
is finite, covariant, and support-consistent. Its quantum cap is enforced
by the supplied joint inner-product/Born condition. The same records,
local rule, setting independence, and no-signalling marginals also support
an explicit PR alternative if that joint condition is changed.

**Closed incompatibility test.** The quantum joint law cannot extend to the
specified one-outcome prefixes with unchanged Bob neighborhoods and (K):
the two positive-probability states require unequal next-outcome
conditionals where (K) requires equality. This is a counterexample to that
specific extension claim, not a universal impossibility theorem for
record-only laws or an argument that an axiom amendment is necessary.

**Unresolved physical issue.** An atomic nonfactorizable pair event and
ordinary local quantum instruments are two mathematically coherent ways
to state the joint probabilities, but they impose different requirements
on real intermediate record states. The current sources do not derive an
operational formation process that both reproduces those quantum
conditionals and satisfies strict full-state neighborhood locality at each
accessible one-record stage. The precise meaning and domain of the local
distribution clause must be kept explicit in any proposed physical model.

## 7. Negative-claim scope check and verification limits

This is an explicit construction plus two counterexamples, not a submitted
general no-go packet. The pinned-main no-go discipline was applied to avoid
inflating the sequential counterexample into a global obstruction.

* **N1, alternative routes:** three genuinely different formulations were
  checked: atomic record transitions, sequential full-record local kernels,
  and local quantum instruments. Atomic transitions succeed; the stated
  sequential extension fails by (6)-(8); quantum instruments succeed as
  operational quantum models while their selected histories fail (K).
  The PR variant tests a changed joint probability assumption within the
  atomic family and is not counted as a new route family. No five-family
  exhaustion or formal packet PASS is claimed.
* **N2, independence:** the negative result has one exact incompatibility,
  namely equality demanded by (K) versus unequal Born conditionals. No
  collection of allegedly independent open walls is claimed. The ledger
  above makes no pairwise independence claim for its physical choices.
* **N3, hidden premises:** the complete pre-state, conditional-on-formation
  reading, guaranteed second event, unchanged neighborhood, positive
  conditioning branches, source/setting independence, event domain,
  calibration, quantum probability bridge, preparation, and irreversible
  readout have all been stated. Removing or weakening any premise is a
  different proposition, not a hidden repair of the contradiction.
* **N4, residual match:** foundational Bell section 3 concerns the complete
  causal factorization (9), not arbitrary record-only laws; its section 4
  concerns the supplied quantum class. The Busch source concerns effect
  representation given POVM hypotheses, not deriving those hypotheses.
  The native parity source concerns a supplied preparation/instrument, not
  a general intermediate-record locality theorem. Those are exactly the
  roles for which they are used here; no audit authority is inferred.
* **N5, resolution:** the support proof checks every occupied site and all
  six neighbor slots in this finite apparatus; the bounds are analytical
  for every parameter in their displayed domains. No numerical, timing,
  macroscopic lattice, arbitrary apparatus, or empirical execution is
  claimed. The counterexample concerns two distant detector sites and a
  specified accessible intermediate history, not all laws on the lattice.
* **N6, partial closure:** the atomic law is already an affirmative
  conditional route. Weakening (K), changing the record-state ontology,
  changing the physical event domain, or allowing local conditions to
  change are distinct possibilities. None is here asserted to require or
  constitute an approved axiom change. Calling the conditional state a
  calculational object alone does not remove its remote dependence.
* **N7, steelman:** a hostile reviewer can correctly say that distant
  selective quantum conditionals are inference, not a transmitted signal,
  and that an atomic pair law never visits the states in (6). Both
  observations are incorporated. They prevent a broad no-go; they do not
  make a kernel conditioned on each complete record state equal to its
  remote-outcome average. The remaining actionable route is to specify
  which states and which conditional probabilities the physical formation
  law actually uses.
* **N8, prior scope:** the three supplied prior-result sources were checked
  for these same residual distinctions, including the old tensor-content
  wording in the Busch note. No broad ledger or historical campaign search
  was performed under this bounded read-only brief. Formal submission and
  any broader negative-claim packet remain outside this report.

Verification consisted of complete source reading, exact source identity
comparison, the full hand proofs above, explicit checks of every occupied
site type in the 18-record construction, and direct comparison of two
positive-probability histories. No numerical job, source runner, formal
checker, backend-independent model audit, or laboratory test was run.
The standard Born/CHSH/effect-Gleason mathematics is prior art. Its
rederivation here checks the load-bearing steps but grants no audit status,
novelty, or axiom consequence.
At freeze, all six live input files in the source table were rehashed and
remained identical to the recorded digests. The target directory contained
only `INDEPENDENT.md`; no other deliverable, numerical job, source edit,
commit, push, or audit action was made. This is the frozen independent
phase; any later source-exposed comparison must be separately identified.
