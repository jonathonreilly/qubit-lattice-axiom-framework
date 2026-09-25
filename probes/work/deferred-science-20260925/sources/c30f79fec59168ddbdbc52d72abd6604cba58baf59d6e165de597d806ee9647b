# Independent PRE: finite interventions in the autonomous clock construction

This is a bounded independent derivation before root-source release. It is
not an audit verdict or publication. Only the two assigned earlier-main
scientific notes were read. No root checkpoint, `autonomous-process-personal`
artifact, new root derivation/runner, or other checker packet was read.
There was no delegation. Applicable AGENTS/workflow instructions were reused
as unchanged, as specified by the dispatch.

## Sources and outcome

The complete arguments of these sources were read and frozen under `sources/`:

- `AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `8efa6ff1d5b54b9ba7652c5ea43861277721157fb4e07e05c9c3d99ee75ba13e`.
- `FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `fcc928081754cdcfb8522155a54163655be604c5010660ae85ba7cba0fb42a42`.

`SOURCE_PINS.json` records the exact paths and read revision. The instruction
sources already read for this campaign were main
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` and execution instructions
`eb1f1ca8338848cf2046582e13aef372d8540937`. They supply procedure, not physics.

**Result.** A finite-intervention extension is available with an explicit
near-identity unitary completion of the collision isometry and a stronger
joint clock estimate. It does not follow merely by composing the source's
one-time reduced-channel bound. The resulting error below carries the actual
correlated clock and battery through all interventions; no physical reset is
assumed. A separate marked-collision estimate compares binned original marks
to the continuous marked dynamics. It does not compare atomic grid timestamps
to exact continuous timestamps in total variation.

The construction and proof are supplied conditional mathematics. The physical
selection, locality, preparation and resource caveats of both source notes
remain in force.

## 1. Precise operational comparison

Fix a finite-dimensional system, `H>=0`, `h=||H||`, its actual finite list of
resolved or coherent marks `L_j`, `Gamma=sum L_j*L_j`, `g=||Gamma||`, and a
finite horizon T. Fix a finite number m of intervals with deterministic cuts

    0=t_0<t_1<...<t_m=T,      t_l=k_l tau,      tau=T/n.

For a fixed rational observation grid one can refine n through multiples of
its denominator. The theorem is for fixed m; it does not assert a bound
uniform as the number of intervention times diverges.

Allow an arbitrary initial system/reference state. At each cut, the observer
receives the ordered original mark word in the preceding coarse time bin,
with internal event times discarded. The observer can apply any instrument
on the system and its external quantum memory, with outcomes retained and
later choices depending on all earlier outcomes and received mark words.
All branches are included, so the instruments are represented as CPTP maps
on enlarged quantum/classical memory. The observer cannot directly access
the clock, battery, or unexposed future flags. The reference/memory can have
arbitrary finite dimension. Instantaneous observation/intervention operations
are externally scheduled at the specified cuts; their energy cost is not
provided by the autonomous construction.

In the implementation, at a cut one dephases/copies the corresponding batch
of collision flags to the observer and maps the sequence of nonzero labels
to its ordered word. The flags need not be reset afterwards. Their subsequent
physical dynamics is still part of the actual joint autonomous evolution.

The comparison norm is the supremum, over these initial states and adaptive
testers, of the trace norm between the final quantum/classical output states,
including mark records and intervention outcomes. The convention has maximum
distance two. It bounds total variation of any final classical readout by
half this distance. It is an absolute, unconditioned comparison; it does not
give a uniform bound for normalized postselection on rare events.

The target is the standard marked finite-system dynamics with no-event
amplitude

    N_t=exp[t(-iH-Gamma/2)]

and the original jump operators L_j, interrupted by the same testers. This
uses the supplied original instrument, not an energy-filtered or scalar
replacement. A coherent mark remains its original coherent L_j throughout.

## 2. Why the one-time conclusion is insufficient

The source proves closeness after tracing the clock, battery and all flags
for an uninterrupted evolution from their prepared initial state. After an
intervention the actual resources can be correlated with both system and
observer. That hypothesis is different, so restarting its one-time channel
estimate at each cut is not justified.

Even exact equality of one-time channels at the tested times does not fix
the intervention statistics. For example, let a qubit have hidden independent
uniform bits r,r'. In one model the cumulative unitary at both t_1 and t_2 is
`Z^r`; in another it is `Z^r` at t_1 and `Z^r'` at t_2. Both channels at the
two cuts are the same complete dephasing channel on every input. Replace the
system by `|+>` at t_1. The first model leaves it `|+>` afterwards, whereas
the second applies the uniform parity `Z^(r+r')`, giving the maximally mixed
state. Their final trace distance is one. This is a counterexample to the
inference from tested one-time marginals, not a counterexample to the actual
clock construction or a continuous-time no-go theorem.

## 3. An explicit controlled completion of the actual collision gate

Assume `tau g<=1/2`. Decompose one system-plus-flag space into the blank sector
`S tensor |0>` and the nonzero-mark sector `S tensor C^q`. Define

    J_tau psi = sqrt(tau) sum_j L_j psi tensor |j>,
    J_tau* J_tau = tau Gamma.

Choose the following full unitary, not merely unspecified extra columns:

    C_tau = [ sqrt(I-J_tau*J_tau)    -J_tau*                ],
            [ J_tau                  sqrt(I-J_tau J_tau*) ].       (1)

The functional-calculus identity
`sqrt(I-J*J) J* = J* sqrt(I-JJ*)` proves that both cross blocks of
`C_tau*C_tau` vanish and that both diagonal blocks equal the identity.
Its blank column is exactly the required collision isometry. Thus choosing

    U_l = (exp(-iH tau) tensor I_flags) C_tau,l

on the l-th fresh flag retains the source's collision instrument exactly.
No labels internal to an originally coherent L_j are resolved.

A singular-value decomposition of J_tau splits (1) into two-dimensional
rotations with cosine `sqrt(1-s^2)` and sine s, plus identities on unused
subspaces. Therefore

    ||C_tau-I||
      = sqrt[2(1-sqrt(1-tau g))] <= sqrt(2 tau g).                  (2)

The equality is interpreted as zero if g=0. This controls the gate on the
ENTIRE flag space, including nonblank states. Closeness only on blank flags
would not be enough for the joint clock argument below. The source's arbitrary
unitary-completion freedom did not itself supply (2).

Let the unlifted interaction-picture gates and their prefixes be

    B_l = exp(+iH l tau) U_l exp(-iH(l-1)tau)
        = exp(+iH(l-1)tau) C_tau,l exp(-iH(l-1)tau),
    P_k = B_k ... B_1.

Every B_l is within `sqrt(2 tau g)` of identity in operator norm.

Retain the source's actual battery lift V, interaction-picture W_l, and G_k:

    W_l=exp(+iH l tau)V(U_l)exp(-iH(l-1)tau),
    G_k=W_k ... W_1.

On complete total-label blocks, `W_l` is unitarily identified with B_l; on
incomplete blocks the lift is identity and W_l equals `exp(+iH tau)` restricted
there. Consequently the exact full-space bound

    ||W_l-I|| <= epsilon_tau := sqrt(2 tau g)+h tau                 (3)

holds without discarding a boundary sector. The h tau term is deliberately
retained for the source's incomplete-sector rule. It could be avoided by
instead lifting B_l directly on all blocks, but that would be a separate
boundary implementation choice and is not needed here.

Unitary telescoping now yields, for every p,q in 0,...,n,

    ||G_p-G_q|| <= epsilon_tau |p-q|,                              (4)

and the same inequality for their adjoints. This is independent of the state
of the system, past flags, battery, and reference.

## 4. Joint clock control at a cut

Use the source's same finite path, prepared sine packet chi, clipping
`k(x)=min(n,max(0,x))`, w, R, J, and positive history Hamiltonian. In particular
the initial clock support has k(x)=0, so the initial preparation is a product.
Set

    theta=pi/(w+1),       2J cos(theta)=1/tau,
    a=2JT,
    r_R=min(2,2 exp(a) a^R/R!),
    D_n=w+(T/tau) tan(theta)/sqrt(w+1),
    e_n=epsilon_tau D_n+2 r_R.                                    (5)

Here r_R is a vector error for the finite/infinite clock comparison; it is
not a scalar probability. The source's endpoint-corrected velocity variance
is essential for the following estimate.

For the freely evolved infinite packet at a cut `t_l=k_l tau`, its second
moment obeys

    sqrt(E |k(X(t_l))-k_l|^2)
      <= sqrt(E |X(t_l)-t_l/tau|^2)
      <= w+(t_l/tau)tan(theta)/sqrt(w+1) <= D_n.                  (6)

The final inequality follows from `X(t)=X+tV`, the mean velocity `1/tau`,
the source's `sd(V)=(1/tau)tan(theta)/sqrt(w+1)`, and
`||X chi||<=|<X>|+sd(X)<=w`. It makes no position/velocity independence
assumption.

Write `D_clock=sum_x |x><x| tensor G_{k(x)}`, extending the clipped definition
to the infinite line for analysis. If phi_l is the freely evolved finite
packet, (4)-(6) give for every unit joint vector xi, including references,

    ||[D_clock-I_clock tensor G_{k_l}](phi_l tensor xi)|| <= e_n,   (7)

and identically for adjoints. Indeed the squared infinite-packet norm is
bounded by `epsilon_tau^2 E|k(X)-k_l|^2`. Replacing that packet by the finite
one costs at most `2 r_R`, since the difference of the two controlled
unitaries has norm at most two. Scalar clock phases are irrelevant.
At the initial cut the actual error in (7) is exactly zero because k=0 on
the support of chi; the uniform e_n is just a convenient bound later.

Unlike the source's reduced-channel time-mismatch argument, (7) controls
the full joint state. It is the new estimate that allows interventions.

## 5. Carrying the battery and clock through interventions

Pass to the interaction picture for `H+H_R`. Testers still act only on the
system, exposed flags and observer memory; conjugating them by the known
system free evolution preserves complete positivity and trace norm. The
reference battery vector is then the fixed beta_L. This avoids accidentally
treating a freely rotated beta_L as having the same unphased translation
overlaps.

Between two cuts s=t_(l-1), t=t_l, the exact history propagator is

    D_clock [C_(t-s) tensor I] D_clock*,                          (8)

where C is free finite-clock propagation. Starting with a product reference
state `phi_(l-1) tensor xi`, compare (8) with

    phi_l tensor (G_(k_l) G_(k_(l-1))* xi).

First replace D_clock* by the constant `G_(k_(l-1))*` using (7), then propagate
the free clock, then replace D_clock by `G_(k_l)`. The vector difference is
at most `e_(l-1)+e_l`, with each e_l<=e_n and e_0=0. The joint channel trace
distance is at most twice that number. This statement is uniform over xi,
so it remains valid for any observer/reference state.

For the next comparison take xi with battery beta_L and otherwise arbitrary
state. Such inputs lie in complete total-label blocks. On those blocks,

    G_(k_l) G_(k_(l-1))*
      = V(P_(k_l) P_(k_(l-1))*).

The source's joint isometry proof, before discarding any battery or flags,
therefore compares this segment to
`P_(k_l) P_(k_(l-1))* tensor I_battery` with trace distance at most

    eta_L=min(2,8 sin(pi/[2(L+1)])).                             (9)

It is independent of the number of collisions in this segment and permits
arbitrary correlations among system, old flags and observer memory in the
reference input. The reference future flags for the ideal ordered program
are still blank, as required for that program's collision interpretation.

To compose the estimates, maintain the ACTUAL joint state with all its
clock/battery/record correlations. Compare it to an ideal reference whose
clock is phi_l and whose battery is beta_L after each ideal segment.
An actual segment applied to the previous discrepancy contracts its trace
norm. On the product reference input only, the preceding two comparisons
cost at most `2(e_(l-1)+e_l)+eta_L`. The intervening tester, including copying
and dephasing records, is CPTP and also contracts the discrepancy.

Induction gives the following uniform distance from the ideal discrete
collision process under m intervals and its testers:

    error <= min(2, m eta_L + 4m e_n).                            (10)

The product reference in this hybrid proof is not a physical reset. The
actual resource state is never replaced or assumed independent. In particular
this proof does NOT reapply a channel bound to a correlated real battery as
if it were freshly prepared. The price allowed here is m eta_L; the source's
single eta_L for an uninterrupted gate product is not silently promoted to
an arbitrary-intervention statement.

The actual clock need not have the free packet distribution after a tester.
Only the product REFERENCE used in the hybrid has that packet. The norm
estimate keeps any tester-induced clock disturbance in the carried error.

## 6. A separate binned marked-collision estimate

The reduced-channel error in the sources is not by itself a bound on marked
outcomes. Here is an independent local marked estimate. It uses the same
original L_j and has no extra assumption on h tau.

Let `U_t(rho)=exp(-iHt)rho exp(+iHt)` and `Ncal_t(rho)=N_t rho N_t*`.
Both are completely contractive; Ncal is trace-nonincreasing. Write the marked
jump CP map as

    Jcal(rho)=sum_j |j><j| tensor L_j rho L_j*,
    ||Jcal||_diamond=g.

For one fine cell of length tau, retain the full ordered mark word but
integrate its event times within the cell. The exact empty branch is Ncal_tau;
the combined single-mark branch is

    integral_0^tau (Ncal_(tau-s) tensor id_marks) Jcal Ncal_s ds.

Higher branches have two or more original marks. The collision instrument
has empty amplitude `exp(-iH tau)sqrt(I-tau Gamma)` and single-mark map
`tau (U_tau tensor id_marks) Jcal`, with zero weight in higher branches.

The following estimates use the output direct sum over mark words.

**Empty branch.** The contractive Lie-product integral and
`||[-iH,-Gamma/2]||<=hg` give

    ||N_tau-exp(-iH tau)exp(-tau Gamma/2)|| <= tau^2 hg/2.

For `0<=x<=1/2`, the scalar bounds on the square-root and exponential
remainders give `|exp(-x/2)-sqrt(1-x)|<=5x^2/8`. Thus the amplitude error is
at most `tau^2(hg/2+5g^2/8)`. Both amplitudes are contractions, so their CP
map difference is bounded by twice this, namely

    tau^2 (hg+5g^2/4).                                         (11)

For clarity the Lie-product bound follows by differentiating
`exp((tau-s)(A+B))exp(sA)exp(sB)` with `A=-iH`, `B=-Gamma/2`, bounding the
commutator by `s||[A,B]||`, and integrating; all surrounding factors are
contractions.

**Single-mark branches.** Duhamel gives
`||Ncal_t-U_t||_diamond<=gt`. Replacing the two no-event factors in the
single-mark integrand by their unitaries costs at most `g^2 tau` at every s.
The remaining placement of the jump differs from the collision placement by

    ||(U_(tau-s) tensor id)Jcal U_s-(U_tau tensor id)Jcal||
      <=4hg s.

This follows by differentiating the unitary conjugation of Jcal, using
`||-i[H,.]||_diamond<=2h` and `||Jcal||_diamond=g`.
Integration gives a total single-mark error at most

    tau^2 (g^2+2hg).                                          (12)

**Multiple marks.** The CP Dyson terms are bounded by `(g tau)^q/q!`
for q marks. Hence the entire q>=2 branch has diamond norm at most
`(g tau)^2 exp(g tau)/2 <=g^2 tau^2` when tau g<=1/2. This is the probability
mass of the missing branch uniformly on entangled inputs, not a signed
cancellation with another output branch.

Adding (11)-(12) and the multiple-mark bound gives the sufficient local
classical/quantum instrument estimate

    ||Exact_binned_cell-Collision_cell||_diamond
      <= tau^2 (13g^2/4+3hg)
      <= tau^2 c_mark,       c_mark=4g^2+4hg.                   (13)

The exact marked channel is the norm-convergent no-event/jump Dyson expansion
with the original marks. Summing its branches discards the record and gives
the original GKLS evolution. Thus this estimate compares that specified
marked dynamics, not just some dilation of its reduced channel.

Concatenating n cells with all flag history retained, and inserting the same
adaptive CPTP testers at the selected cell boundaries, costs at most

    n tau^2 c_mark = T tau c_mark.                            (14)

Classically grouping fine-cell words into the fixed coarse observation bins
is a channel and cannot increase this distance. In the ideal ordered
collision program, dephasing old flags can be deferred to their next readout:
later gates act on fresh flags. This deferral is used only for the IDEAL
program. It is not asserted for the autonomous backtracking implementation.

## 7. Quantitative sufficient theorem and resource choice

Combining (5), (10), and (14), the finite-intervention operational distance
defined in section 1 is bounded by

    min(2, m eta_L
           +4m [ (sqrt(2 tau g)+h tau)
                  (w+(T/tau)tan(theta)/sqrt(w+1)) +2r_R ]
           +T tau (4g^2+4hg)).                                (15)

All constants and operators refer to the same fixed supplied model. The
implemented Hamiltonian is the source's finite positive time-independent
history Hamiltonian, with the completion (1) now specified. The sum of its
positive history and free energies, exact free-energy commutator, initial
resource energy, and finite dimensions retain the source's justification.

For fixed h,g,T,m, take n through grid-compatible integers, set

    tau=T/n,    w=max(2,ceil(n^(2/5))),
    R=ceil(8n/cos(pi/(w+1))),    L -> infinity.

Then `D_n=O(n^(2/5))`, `r_R<=2 exp[-7n/cos(theta)]`, and

    epsilon_tau D_n
      =O(sqrt(gT) n^(-1/10)+hT n^(-3/5)).                     (16)

Equation (15) tends to zero. For example L=n also makes the battery error
vanish. The clock dimension remains O(n), its coupling and initial
clock/program energy are O(n/T), and the construction still includes n
prepared zero-energy flags and the finite spectral battery. These are
sufficient resources, not optimality statements.

The parameters of a changing microscopic family must be inserted into (15),
not held fixed by rhetoric. In particular, the source's sample star choices
`g=O(C), h=O(C^2), n=O(C^5), w=O(C^2)` make the leading square-root term in
this sufficient JOINT estimate only O(1). That does not refute a sharper
process estimate, but these resource choices do not prove convergence by
the argument above. Larger resources can be chosen: for example
`n` of order C^10 and w of order C^4 give the displayed clock term O(C^-1/2)
when the stated upper bounds hold, before any desired additional energy
weight is imposed. A microscopic energy conclusion still requires multiplying
the relevant trace error by the growing observable norm. No such new
microscopic energy conclusion is claimed in this PRE.

## 8. Records, energy and remaining boundaries

- A finite history clock can move backwards. Its backwards hopping applies
  inverse program gates and can change previous program flags. Neither this
  construction nor (15) makes those flags physically irreversible. External
  copied records persist only because the autonomous Hamiltonian does not
  act on the observer's memory. The operational comparison controls their
  finite-grid statistics, including the effect of actual earlier readouts.
- One may not replace a continuous timestamp by a grid atom and infer total
  variation convergence on unbinned timestamp space. A continuous nonzero
  event-time distribution and an atomic grid distribution can remain
  singular. The target here deliberately integrates timestamps inside fixed
  bins. Ordered mark words, counts and their system correlations are retained.
- The testers can supply energy and disturb the interaction Hamiltonian at
  their intervention instants. Exact system/battery free-energy balance from
  autonomous evolution between cuts does not account for that external work.
  There is no claimed closed-system autonomous generation of the tester.
- The result has a fixed finite horizon and fixed finite intervention count.
  It proves no uniform infinite-time, arbitrary-frequency intervention,
  adaptive continuous stopping-time, spatial-locality, bounded-strength,
  catalyst-return, replenishment, or native-physics-selection theorem.
- Completion (1) is an explicit sufficient implementation choice. The PRE
  does not prove failure for every other completion. It also does not claim
  that the same uninterrupted-prefix battery constant must survive without
  the m factor for arbitrary interventions.

## Verification boundary and release questions

The load-bearing new steps were derived directly here: the full-space
completion bound, the second-moment clock dressing bound, the joint-state
hybrid with its correlation bookkeeping, and the separate marked local
estimate. They are analytic arguments, not conclusions from a numerical
sample. No new numerical computation was required or run. The first source
read command did not start because its new output cwd did not exist; it was
retried after creating only the assigned directory. This operational failure
is preserved in `OPERATIONS.log`; no scientific failure was suppressed.

After sealing, a released-source comparison should check whether the root
construction specifies enough of the unitary completion, controls the full
joint state at every cut, keeps actual resource correlations, treats marked
binning separately from reduced-channel convergence, and refrains from
irreversible-record and unbinned-timestamp claims. If it uses another route
such as programmed clock plateaus, that route needs its own endpoint and
timing estimates; those conditions cannot be inferred from the one-time
theorem alone.

All original imports remain conditional. No scientific source, branch,
premise, audit state, or publication surface was changed. The immutable
`PRE_SEAL.json` binds this argument, its source pins/copies, and the operation
log before root-source release.
