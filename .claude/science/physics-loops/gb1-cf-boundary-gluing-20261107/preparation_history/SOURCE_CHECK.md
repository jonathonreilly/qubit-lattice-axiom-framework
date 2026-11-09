# Integrated preparation/history source check

Research source check, not a fresh formal review, landing decision or audit.
Checked the four allowed parent files in full; no numerical runner was executed.
Parent directory: `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/preparation_history/`.

| File | SHA-256 |
|---|---|
| `PRIMARY.md` | `a8fea05d74f30c830a9c173652e726fbf6a300468ca5f57ea3631241583e79c2` |
| `PREPARATION_ADDENDUM.md` | `f26912086c7cda3b28be351abfff8b5a17e9858d5021afe1027c38c5f21db104` |
| `RESULT.md` | `84e9507cf17788836a722f15df52eb01eb59860cd92754ca08556d9c0d149531` |
| `check.py` | `5ef10cd243d0eb6ba47b21b097d066171057f6ca7703c7fef6a8f30901394bb0` |

Comparison input: my previously frozen `INDEPENDENT.md`, SHA-256
`d3fa97363d2ed6443942ab33b17984ba7943df72b94d8931e076425f34144e3b`.
It predates these parent reads. Shared model family, shared earlier premises and
the present integrated context limit independence; no cross-provider claim.
Repeated preflight returned `go` (112 GB disk, 36% free memory, load 6.7).
The script was reread after its concurrent timeout-constant addition; its
mathematical fixtures were unchanged. The prose hashes stayed fixed during checking.

## Findings requiring explicit scope

No counterexample was found to §§1–4 on their exact prepared domain. The
following clarifications prevent stronger readings that the algebra would not support.

1. **Specify the post-herald initialization (`RESULT.md` §5, equations 1 and 9).**
The rank-one identity is correct, but “run (1)–(7)” on the remaining slots leaves
the reset implicit. Set sigma_start=P (or rho_alpha=P_alpha), or explicitly include
the herald as the first CP map and condition on its nonzero branch. The latter
works with any reference seed having nonzero P overlap. Simply restarting the
remaining program at an unrelated mixed dictionary state would be wrong: I/2
and P=|0><0| give next P-event probability 1/2 versus the certified value 1.
State that the unknown-input variant's domain begins after the logged success.
Its future predictions need no original density, but its pre-herald trace weights
cannot be taken from a reference seed when the actual input is arbitrary. This
is an initialization/domain clarification, not a failure of the herald identity.

2. **Name the tick's record-registration premise (`RESULT.md` §2, equation 3).**
The deterministic CP map is valid and preserves the old records on compatible
inputs. Applying U and flipping a blank qubit gives the advertised pointer
postcondition; a physical permanent Record additionally requires the supplied
calibrated tick append. Say explicitly that equation (3) is this supplied
record-writing recipe, not a Record-formation theorem from a bare unitary flip
or from the electric reader. Its outcome-1 support/registration must be part
of that recipe. The existing boundary language is consistent with this repair.

3. **Retain the controls' model boundaries (`RESULT.md` §6).**
The magnetic number 192/625 is correct conditional on the stated pair block
B_L=2X and the corner effect P_L/3. Restore `PRIMARY.md`'s explicit sentence
that this is a declared local pair control, not the uniform full cubic H.
The Z0/Y0 example is an exact projective-history order control; it does not
by itself construct a native Y0 reader. Neither example verifies an omitted
commutator or physical identification for the full native dynamics. Their
algebra is useful without transferring them beyond their supplied domain.

## Direct proof checks

**CP recursion and common target.** For positive sigma_h each child is positive;
trace preservation gives sum_b Tr(sigma_hb)=Tr(sigma_h). Multiplication of the
conditional trace ratios telescopes to the cylinder trace. Zero-trace positive
children vanish and are correctly excluded from conditioning. The controller
and spatial prefix decode determine the same next site before b is selected.
Thus (7) is a normalized finite Markov kernel on the prepared record states;
the probability is in content, not an outcome-dependent target selection.

**Marker geometry.** In coarse coordinates the marker occupies the three arms
of lengths 1,2,3; word sites are (2j,4,0), 1<=j<=M. Since n>=2M+8 and M>=2,
the marker has no periodic extra edges. Word-to-word coordinate differences
are nonzero even numbers at most 2M-2<=n-10, so cannot be +/-1 modulo n.
Every word site differs in its second coordinate from every marker site by
at least 2 and at most 4; n>=12 prevents wrap adjacency. Consequently all word
sites are isolated and the seven-site marker is the unique nontrivial component.
Its sole degree-three vertex and distinct arm lengths uniquely recover anchor
and signed axes. Restricting to proper transported domains gives a right-handed
frame. There is no hidden insertion order or second description with a different
dictionary interpretation. The records remain entirely on V_p; F_p stays frozen.

**Radius (8).** For next index j=d+k+1<=M, a previous word v_l has distance
10(j-l)<=10(M-1). The marker distances are bounded respectively by
10j+20, 10j+15, 10j+15, 10j+10, 10j+25, 10j+30, 10j+35.
Hence every existing record lies in B(x,10M+35); torus distance only decreases.
Within this exact domain there are no unrelated records outside the packet.
Equal ball record conditions at eligible targets therefore determine the same
entire decoded input; translation/proper-rotation covariance supplies the same
conclusion for matching relative conditions. This is a correct finite-radius
lookup theorem. It is not a uniform-range mediated circuit, a time-of-flight
bound, a locally implemented decoder, or a universal law on arbitrary records.

**Native preservation and ticks.** Every selected slot is a fresh true-phase
vertex, with blank pointer and no old records in the link detector support.
The original reader's guard consequently permits the event. Its projectors
preserve Gauss, and the supplied H intertwiner fixes all output pointers.
Equation (3), interpreted as the supplied append above, also fixes every old
record and logs the known unitary step. No unrecorded continuous-time interval
is inferred; the source correctly confines both conventions to event transitions.

**Herald with reference.** In a basis beginning with psi, multiplication by
P=|psi><psi| retains only the psi-psi block. This proves PXP=Tr(PX)P and
(P tensor I)X(P tensor I)=P tensor X_ref, where X_ref=<psi|X|psi> is positive.
Dividing by its nonzero trace gives P tensor a normalized reference state.
Singlet invariance makes P commute with Gauss. A degenerate projector does not
have this conclusion: two orthogonal vectors in its range remain distinguishable.
Unknown inputs P and an orthogonal pure state give the same pre-herald records
but success probabilities 1 and 0. The note correctly does not claim to fix
those odds, guarantee success, or derive the full-graph verifier's locality.

**Effects and omission controls.** Equation (11) is precisely the future-effect
criterion in the independent derivation. Same allowed controls and successor
updates are essential and explicitly retained. For B_L=2X, cos(tau)=3/5 gives
sin^2(2tau)=576/625, hence the stated corner probability 192/625. Starting at
|0>, Z0 then Y0 has mass 1/2 and final Y0; Y0 then Z0 has mass 1/4 and final Z0.
Their future Z1 probabilities are therefore 1/2 and 0. The source correctly
allows known hidden edge branches and null loops to be marginalized.

The initial admissibility/support of the seven markers, header bits and blank
pointers, actual preparation, calibrated event maps, dictionary and controller
remain premises. The finite lookup does not discharge their physical realization.
No numerical PASS count was used as evidence for these general statements.

## Confirmation of the three clarification hunks

Checked the exact delta against `RESULT_before_clarifications.md`, whose hash
matches the reviewed baseline above. Final `RESULT.md` SHA-256:
`65dcdeec4d83b3eda61ebd5b96fb17e7ce31cf9626caa9495dd14bbb0eec56ad`.
All three findings are resolved: the herald variant starts after its logged
success at sigma_start=P_alpha, consumes one slot, and has no remaining recipe
when N=1, so absorption is correct. No arbitrary pre-herald odds are assigned.
The tick now explicitly supplies calibrated permanent append, registration and
outcome-1 support. The pair witness is explicitly local rather than the uniform
full cubic Hamiltonian, and the order witness does not assert a native Y0 reader.
The delta contains exactly those three hunks; the other parent source hashes
above are unchanged. This is a selective integrated-source confirmation, with
the same conditional premises and context limits, not a new formal review.
