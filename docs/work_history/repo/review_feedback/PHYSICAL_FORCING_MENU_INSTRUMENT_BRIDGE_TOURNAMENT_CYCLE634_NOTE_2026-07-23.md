# Physical forcing-menu instrument bridge tournament — Cycle 634

Classification: **positive bounded fixed-menu M2 instrument compiler; menu genesis, physical grade, occurrence, Record, and Born meaning remain supplied/open**

Authority: **none**

Audit: **unset**

## Decisive result

Cycle 634 constructs the physical menu layer that Cycle 625 left open for a
declared finite family.  For a supplied qubit POVM `E_0,...,E_(m-1)`, `2 <= m <=
7`, one system M2 occupies the center of a cubic star and `m-1` blank apparatus
M2s occupy distinct nearest-neighbor ports.  At stage `j`, the compiler forms
`F_j=A_j^(-dagger) E_j A_j^(-1)` and applies the two-M2 unitary

```text
U(F) = sqrt(I-F) x |0><0| - sqrt(F) x |0><1|
     + sqrt(F) x |1><0| + sqrt(I-F) x |1><1|.
```

Every gate runs in the fixed schedule.  No pointer value controls a later gate
and no host selects an outcome.  Summing `K_p^dagger K_p` over the orthogonal
pointer patterns whose first `1` is `j` gives exactly `E_j`; the all-zero
pattern gives the final effect.  This is a physical fixed-menu dilation and a
local pointer-port identity.  It is not a physical rule selecting which menu
nature deploys.

| family | outcomes | system+apparatus M2 | binary NN macros | literal one-/two-M2 calls | effect residual | all24 unitary covariance | minimum deletion residual |
|---|---:|---:|---:|---:|---:|---:|---:|
| ternary_trine | 3 | 3 | 2 | 12 | 3.187e-16 | 7.617e-16 | 6.667e-01 |
| scaled_axis_cancellation | 4 | 4 | 3 | 18 | 1.039e-15 | 2.389e-15 | 4.226e-01 |
| mixed_projective_merge | 2 | 2 | 1 | 6 | 1.241e-16 | 9.554e-16 | 8.536e-01 |
| held_size5_split_trine | 5 | 5 | 4 | 24 | 9.216e-16 | 2.872e-15 | 2.222e-01 |

The held five-outcome split-trine case uses five M2 and four central-neighbor
gates.  Thus the construction has constant overhead per compiled coarse menu
cell and maximum literal support two.  It uses no global parity string,
preferred lattice ordering, nonlocal service, or runtime outcome control.
Each binary macro is lowered exactly to four supplied one-M2 rotations and two
nearest-neighbor CNOTs; the maximum observed lowering residual is
`3.343e-16`.
The Moore-Penrose support extension also passes the singular intermediate
remainder control `{P_z,0.4P_-z,0.6P_-z}` with effect residual
`1.110e-16`.

The apparatus code constraint is the product of one-site `|0><0|` input
projectors.  Each constraint is locally checkable at support one and every
nonblank basis input is refused by the declared compiler domain.  Blank genesis
and renewal are supplied; the constraints are not misreported as a persistent
gauge law after the ports become pointers.  Daggering the fixed unitary gives
the inverse and restores blanks when the retained output is uncomputed.

## Ternary, scaled-projector, and mixed-projective probes

The ternary menu is the equatorial trine `E_j=(2/3)P(n_j)`.  The scaled menu
uses `c=2/(1+sqrt(3))` and
`{c P(111), c/sqrt(3) P(-x), c/sqrt(3) P(-y), c/sqrt(3) P(-z)}`; the vector
parts cancel and the effects sum to identity.  Every ordering of the ternary
and scaled menus is compiled (6 and 24 orderings respectively), and labeled
effect recovery is unchanged although the dilation embedding and post-state
map may change.

For `E_0=(P_z+P_x)/2`, two separate three-M2 physical presentations were
constructed.  Presentation A prepares an equal coherent coin, analyzes `z` on
coin zero and `x` on coin one, and writes a local pointer.  Presentation B uses
the spectral weights `lambda_plus=0.853553390593` and
`lambda_minus=0.146446609407` with analyzers along
`u=(x+z)/sqrt(2)` and `-u`.  After summing over the retained coin, their effect
identity residual is `4.163e-16`.
Their post-state channel difference is `2.500e-01`:
same effects do **not** imply the same instrument.  A direct canonical
positive-root dilation supplies a third covariant representative.

## Proper-cubic covariance and physical controls

The exact proper-cubic group has 24 frames and
576 ordered products.  Each reference port ray
is transported with the frame.  Spinor conjugation transports every effect,
and functional calculus transports every compiled binary gate.  The largest
observed unitary covariance residual is
`2.872e-15`.
The reference chart and menu orientation remain supplied genesis, not a
preferred physical frame.

Negative, nonnormalized, non-Hermitian, and eight-outcome-on-six-port menus are
refused.  Omitting every binary gate changes at least one induced effect.  The
full unitary is norm-preserving on the blank-port code and has no unused local
levels.  A generic independent two-level spectator factor commutes with every
instrument at residual
`0.000e+00`.
It is **not** called the committed Cycle523 coin/mass fixture.  Cycle523's
`0.453405654174885` rest-mass result and `2.220446049250313e-16` fixture residual
are pinned comparison-only; Cycle634 does not reexecute or claim preservation
of that object.  No wrapped phase is called energy and no generator is called a rate.

## Prior-art and novelty boundary

Finite-outcome POVM/Naimark dilation, sequential binary decompositions, and the
nonuniqueness of instruments realizing a fixed POVM are standard mechanism
classes.  Cycle634 claims no general novelty or priority for them.  The bounded
repo-specific contribution is the declared forcing-menu cubic-star
compilation, its exact proper-cubic/held/deletion/domain controls, and its typed
candidate-only interfaces to committed Cycle625 Routes B and C.  No external
theorem is used as runner evidence; the closed Born heads remain comparison-only.

## Six-layer separation

| layer | status | closed here | remaining import |
|---|---|---:|---|
| conditional_form_forcing_theorem | COMPARISON_ONLY_NO_BACK_CREDIT | no | none consumed as a premise |
| physically_supplied_menu_eligibility | POSITIVE_FOR_DECLARED_FIXED_COMPILED_MENUS | yes | which menu/family and its physical parameter genesis |
| effect_functionality_candidate_grade_w | ALGEBRAIC_DIAGNOSTIC_ONLY | no | physical grade output and state/calibration genesis |
| occurrence_selector_sigma | OPEN_POINTER_SECTORS_REMAIN_COHERENT | no | objective occurrence selector sigma |
| Record_and_permanence | OPEN_POINTER_IS_NOT_RECORD | no | Record identification, permanence, readability, renewal |
| frequency_and_Born_meaning | OPEN_HOST_DIAGNOSTIC_COUNTS_ONLY | no | realized corpus, frequency law, Born meaning |

The exact effect identity is derived before any grade is introduced.  For the
supplied diagnostic state `rho=(I+0.2X-0.3Y+0.4Z)/2`, Cycle634 later evaluates
the algebraic candidate `w(E)=Tr(rho E)` and confirms presentation
independence.  This is not a physical numeric grade output and is never used to
justify or select the dilation.

The Cycle625 Route-B adapter maps every pointer first-hit label to one supplied
six-direction one-hot candidate.  Coherent inputs retain multiple orthogonal
pointer sectors, so this is a candidate correlation and not `sigma`.  Pointer
basis states are not Records.  The Route-C adapter embeds the candidate `w`
values into eight labels using a supplied host-side largest-remainder
denominator-64 quantizer.  Those counts are not realized frequencies or Born
probabilities.

## Supplied / derived / open

Supplied: effect matrices and labels, compile order, finite star chart, blank
ports, gate constants, mixed-presentation coin/analyzer data, diagnostic rho,
and the Route-B/C adapters.  The closed PR5472/5476/5479 heads are immutable
comparison-only objects with no back-credit.

Derived: the bounded local unitaries and inverses, exact pointer effects,
ternary/scaled/mixed/held compilers, all24/all576 covariance, deletion and
malformed controls, presentation-independent effect identity, and executable
candidate interfaces into Cycle625.

Open: autonomous menu/family parameter genesis, physical grade output,
objective selector `sigma`, Record identification and permanence, reset and
renewal, realized corpus/frequency/Born meaning, infinite noisy deployment, and
gravity/source integration.

## N1–N8 no-go discipline

N1 normalizes six families.  Three constructive families were attempted:
sequential positive-root dilation, coherent-coin mixed splitting, and
canonical spectral/direct presentation.  Autonomous menu-program QCA,
objective dissipative actualization, and renewable Record-corpus calibration
remain open and do not count.  Three is below the required five attempts, so
the broad-negative gate is **FAIL / DO NOT SHIP**.

N2 collapses six walls and audits all 30 directed pairs.  N3 inventories every
menu, blank, chart, order, coin, grade, and adapter import.  N4 contains eight
exact same-scope residual rows and three dropped closed-head comparisons.  N5
contains six five-resolution rhetoric rows.  N6 contains six structured
`file` / `status` / `what_closes` paths.  N7 gives an actionable autonomous
apparatus-QCA steelman.  N8 gives seven row-wise exact cross-cycle echoes.

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle634 movement | residual |
|---|---|---|
| `C_ref` | fixed reference-star menus acquire transported physical M2 dilations | star/menu orientation and parameter genesis remain supplied; no preferred physical frame is claimed |
| `C_num` | exact ternary, scaled, mixed, held-size5 effects and algebraic candidate `w` | no physical grade output, general precision law, realized frequencies, or Born meaning |
| `C_wrap` | local pointer ports and exact coarse effect identities are physical | no objective `sigma`, Record identification, permanence, reset, renewal, or realized history |
| `C_int` | system-apparatus coupling is a literal support-two unitary instrument | its gate constants are compiled from a supplied menu; no new matter interaction law or generator/rate claim |
| `C_local` | one cubic star, up to seven outcomes, all24/all576, inverse/deletion/malformed/held controls | infinite tiling, overlapping apparatus, noise, and autonomous blank enforcement remain open |
| `C_source` | blank apparatus capacity and retained mixed-presentation coin exhaust are explicit | no energy/stress/source/gravity meaning or autonomous resource genesis |

## Disposition

**PASS** for a literal bounded physical M2 compiler of the declared fixed-menu
families and for exact effect identities at local pointer ports.

**FAIL / DO NOT CLAIM** for autonomous menu eligibility across nature's menu
family, a physical grade, objective occurrence, Record/permanence, realized
frequency, Born probability, universal instrument equivalence, shared
obstruction, minimum content, or axiom pressure.

The optimal next campaign is the autonomous menu-program and blank-renewal
bridge: encode the menu parameters in a bounded covariant physical program,
prepare/refurbish local ports without a host, feed the resulting pointer
sectors into the unchanged Cycle625 Route-B interface, and require retained
exhaust plus a blinded sigma/Record/frequency test before any probability
interpretation.
