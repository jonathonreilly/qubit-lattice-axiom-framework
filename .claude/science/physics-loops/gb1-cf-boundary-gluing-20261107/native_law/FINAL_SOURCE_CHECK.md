# Focused research source check

**Date:** 2026-11-08. **Outcome:** confirmation within the stated conditional
scope; no actionable mathematical or source/runner mismatch found in this
frozen packet. This is not a formal fresh review, audit, landing approval or
axiom adoption.

## Frozen source and read coverage

All four requested files were read completely from
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/`:

| File | SHA-256 checked against dispatch |
|---|---|
| `docs/SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_BOUNDED_THEOREM_NOTE_2026-11-08.md` | `879d7e3195f678a3f37f7d0c32f7ea30d348f86c7d3c7901af5a84dcf4b97915` |
| `docs/SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_SCOPE_CHECK_2026-11-08.md` | `4c263b6439db0d7c29843b9fc838bed9bd0c62cda1a9862a57fa74f85861ba40` |
| `scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py` | `d78f0a745f183341abe319a151c1681c9d386e2b0f6aadd0aff2ba388bbf0bd0` |
| `logs/runner-cache/gb1_cf_neighborhood_record_readout_exact_2026_11_08.txt` | `23a6c0877dade758b746c3114d2551aa066a187d8666dab59e22fe67b641e183` |

Coverage was the entire 236-line theorem note, entire scope sidecar,
entire 422-line runner and entire 30-line cache. The axiom and registry
hashes also remain, respectively,
`93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753`
and `615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37`.
Their unchanged bytes permit reuse of the prior complete premise reads.

The initial shell command was `python3 scripts/lab_ops.py preflight` in
the checker worktree. It returned `preflight: go` (118 GB disk free,
32% memory free, load 3.7, nice functional, origin reachable; no target
model floor checked and memory cap unavailable). The model/effort remained
inherited; exact runtime values were not exposed. No numeric job ran.

## Load-bearing mathematical checks

**Compact electric instrument.** The chronological decoder
`S34,S23,CX12,H1,CX34` sends `J0` to `0100` and `J1` to `-1100`.
The old middle-bit parity is one on every computational component of
`J2,J3,J4`, and the final CNOT writes that parity into site 4. Therefore
the two-bit predicate at sites 1,4 distinguishes exactly `J0` on the
entire five-dimensional code, not merely on the phase-test subspace.

The seven-gate Toffoli in the note and runner has the correct controlled
square-root phases. Its target exponent is `v-(v XOR u)+u=2uv`, and its
last three factors implement remote controlled V by returned SWAP routing.
The negative-control routing, output complement and reversed decoder are
in the correct order. Counting the literal lists gives `4+11+4=19`
adjacent two-site gates and `1+5+1=7` one-site gates. Every pair support
has distance one on the stated five-site native line. There are no work
qubits, hidden resets or discarded data.

The resulting code isometry is exactly
`J0 r0 -> output0 J0 r0` and
`sum_{mu=1}^4 Jmu r_mu -> output1 sum_{mu=1}^4 Jmu r_mu`.
Thus output readout `3b/4` gives the two electric spectral projectors,
preserving coherence throughout the occupied eigenspace. The external
vectors can be arbitrary, so the proof covers external entanglement and
mixed inputs. The runner checks both pointer inputs on every code column;
linearity, rather than additional product-state samples, supplies the
extension to arbitrary code superpositions.

**Distinct two-work electric implementation.** I independently traced the
runner's seven-site circuit. `X6,CX(3,6),H3` sends the normalized `J0`
to the data word `0000`. After negating all four data controls, the three
Toffolis compute their conjunction through work sites 1,2 into output 0;
the next two Toffolis restore both work bits. Undoing the negative controls
and decoder returns the data. This circuit uses the opposite pointer
label: output 1 means electric value 0, as the cache expressly states.

Returned routing has pair cost `2d-1` for endpoint graph distance `d`.
The first work Toffoli costs 7, the second 9, the central output Toffoli
23, and the decoder and inverse together cost 10. Hence the emitted
count is `2*7+2*9+23+10=65` pair gates. The two four-bit negations and
the decoder/inverse supply `8+4=12` one-site gates. The listed sites are
connected by actual unit cubic edges; all three ancillary sites have two
nonzero coordinates modulo five and hence are spectators of the fixed
origin placement. The routing identity allows arbitrary correlated
mediators; no intermediate blank-site assumption is required.

The runner's full clean-work expected map is the direct rank-one projector
map, independent of the gate word: with unnormalized `v=e1+e4`, it is
`2I+(X_output-I)|v><v|`. This explains the subtract-one/add-one coefficients
for native inputs `e1,e4`, and identity times two for the other inputs.
It matches the intended full-space extension and returns both work bits.

**Full-code versus off-code scope.** The compact decoder predicate has
rank four on the 16-dimensional native data space; the two-work circuit's
vacuum predicate has rank one. Their spectral instruments agree on the
whole code after matching opposite output labels. They are not asserted
equal off code. For example the normalized off-code state
`(|0000>+|1001>)/sqrt(2)` is decoded to `0000` by the compact decoder and
is orthogonal to `J0`: compact readout gives energy 0, whereas the
rank-one extension gives `3/4`. The source explicitly limits agreement
to the code and makes no physical selection of either off-code extension.

**Reversal and record-first checks.** The six adjacent transpositions
`12,23,34,12,23,12` reverse four positions. Their controlled routing costs
`11+13+15+11+13+11=74`. Both the direct controlled-permutation comparator
and the two-Hadamard comparator in the runner have correct signs for
either pointer input. Reversal acts on the five columns with signs
`(+,-,-,-,+)`, with no claim that it is gauge invariant at fixed endpoints.

For `(e1+exp(i phi)e4)/sqrt(2)`, the electric vacuum probability is
`(1+cos(phi))/2`, yielding exactly `1,0,1/2` at `phi=0,pi,pi/2`.
Computational data recording first gives the same outcome-labelled
ensemble for the plus and minus states and therefore equal output odds.
The dephased `J3` mixture has code overlap `1/2`: each of `1100,0011`
has projector diagonal `1/2`. The old fixed-zero output sector is
orthogonal to output 1. These are specific instrument comparisons, not
universal limitations on records or a complete framework realization.

## Record relay and physical scope

The neighbor-copy measure is normalized for every positive neighbor count,
depends nontrivially on the recorded contents, and is invariant under
neighbor permutations induced by lattice translations and proper rotations.
Conjugating all rank-one contents also conjugates the measure; the empty
condition's normalized Bloch-sphere area measure is invariant under that
conjugation. Choosing rank-one support and this distribution is explicitly
conditional, not axiom-selected.

With one seed and no other initial records, a self-avoiding adjacent
formation path always has its predecessor recorded. All recorded neighbors
have the same seed content, even when the path approaches itself, so the
conditional measure is the same point mass at every step. This proves
arbitrary finite propagation with no alteration of an existing record.
The supplied formation order is not claimed to follow from the law.

The runner's 64-neighbor checks cover six occupied neighbors with two
possible contents, not all vacancy patterns or all continuous contents.
Its path checks cover lengths 1–32. The note correctly uses the general
permutation/induction proof for continuous contents, empty neighborhoods
and unbounded finite path length instead of extrapolating those tests.

The final electric projectors commute with both endpoint gauge actions
because they select the invariant `(0,0)` and `(1/2,1/2)` summands.
With the explicitly assigned trivial output action, the completed
instrument preserves finite Gauss constraints. Intermediate gates need
not do so. The output-space caveat is explicit: a recorded spectator 1
leaves the original fixed-spectator `C_p`, while the active link code is
restored. Permanence is imposed by the subsequent schedule, and neither
fresh-site allocation nor a program valid on the coherent sum of all
125 origins is constructed.

The record relay and driven quantum experiment are kept as separate
conditional constructions. The source identifies the unresolved
live-state/current-record/history bridge, does not claim an autonomous
homogeneous joint law or plaquette evolution, and does not presume that
the proposed axiom wording is adopted or necessary. The scope sidecar's
record-first exclusions stay instrument-specific.

## Cache interpretation and independence limits

The arithmetic representation consists of exact pairs of rational real
and imaginary parts. `H` is deliberately unnormalized; two Hadamards
give an amplitude factor two, so the runner's expected vectors and
probability denominator `4*input_norm` are consistent. I checked the
assertion comparators and emitted mathematical values against the hand
arguments above, not the aggregate PASS count.

The supplied cache reports exit 0 and embeds the exact runner hash checked
here. It records full 32-column checks for controlled reversal and the
seven-site clean-work subspace, and five code columns with both pointer
inputs for the compact electric circuit. It does not establish a separate
full-native-basis comparison of the two different electric extensions.
No numeric run was repeated in this source-check task. Mutation hooks in
the source are not evidence of executed mutation tests in this cache.

I independently derived the compact circuit before seeing the supervisor's
candidate, but that makes me part of its author lineage. This check can
confirm integration and compare the separately constructed two-work route;
it cannot serve as formal fresh review of my own compact proof. The
independence limitation is not removed by agreement with the exact runner.
Linked contextual history notes were not re-reviewed here; the claimed
circuit, relay and gauge-projector steps have explicit proofs within the
checked packet and the previously checked unchanged code source.

Only this receipt was written. No source, scope, runner, cache, authority,
prompt, or earlier checker artifact was edited; no commit, push, formal
review verdict, audit or landing action was performed.
