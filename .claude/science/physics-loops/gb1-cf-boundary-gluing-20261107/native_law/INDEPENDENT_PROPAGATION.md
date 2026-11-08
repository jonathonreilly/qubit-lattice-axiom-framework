# Independent adjacent-operation propagation probe

**Claim type:** bounded_theorem. **Support:** conditional-support.
This is an independent research probe, not a review, audit, authority edit,
or claim that the four axioms select ordinary quantum dynamics.

## Current checkpoint and source identity

Hand derivation frozen on 2026-11-08 before reading any supervisor candidate
for this probe. Only the three scientific sources named by the dispatch
were read before this derivation. The source note's explicit code is the
input; its existing status labels supply no mathematical evidence here.

- Checker worktree: `/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics`.
- Checker HEAD and fetched main at launch:
  `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
- Research head named by the dispatch:
  `febb4c812b1d38e9b33f2c97149ff2b8f0f363ea`.
- Configured model and reasoning effort: inherited, exact values not exposed.
  No override or substitute was requested.
- First shell command attempted `python3 tools/lab_ops.py preflight` and
  failed because that path does not exist. The corrected
  `python3 scripts/lab_ops.py preflight` returned `preflight: go`: disk
  120 GB free; memory 35% free; load 2.9; nice works; origin reachable;
  no target/model floor checked; memory cap unavailable. No numeric job ran.
- The current main methodology matched the checker copy after fetching.
  Its `SCIENCE_WORKFLOW.md` SHA-256 is
  `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`.

Scientific sources were read at the following absolute source root:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/`.

| Source | SHA-256 at derivation freeze |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753` |
| `docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md` | `0d457372fe995529ad1fc13e3c9d6f696fe27b9a5ee3b1ef78852214a928604c` |
| `docs/audit/data/axiom_premise_nodes.json` | `615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37` |

The supervisor reports a separate proposed clarification PR for multi-step
local propagation. This derivation uses the current text above and does not
presume that clarification adopted.

## Exact target and conditional result

Use five consecutive native sites `0,1,2,3,4` on an oriented lattice line.
Sites `1,2,3,4` hold one link's four-qubit code. Site `0` is a fresh,
recordless output prepared in `|0>`. Give all five sites the ordinary tensor
product Hilbert space, allow the explicit one-site and adjacent two-site
unitaries below, and supply a final computational-basis Born instrument on
site `0`. Regard that final outcome as the site's permanent record and never
act on site `0` afterward.

Under these conditions, there is an exact finite adjacent-gate circuit that
measures the code's orientation-reversal observable

\[
K=\operatorname{diag}(1,-1,-1,-1,1)
\]

and preserves the active four-qubit code after each outcome. Its result is
sensitive to a relative complex phase of a code state. It uses 74 adjacent
two-site gates, two one-site Hadamards, and one final one-site instrument;
this is an explicit upper bound, not an optimization claim.
The quantified data domain is the full five-state link space before regional
Gauss constraints. This probe does not claim that `K` is an independently
gauge-invariant physical observable at fixed endpoints of a constrained
lattice model. This boundary-register readout does not implement physical
plaquette dynamics.

The circuit closes this finite communication/readout question. It does not
construct the SU(2) Hamiltonian's evolution, a fixed covariant native law,
an in-code infinitesimal nearest-neighbor generator, or an identification of
the quantum state with a configuration of permanent records. It also does
not preserve the original full lattice code's fixed spectator condition when
the output is `1`: it preserves the active link code inside a larger
input/output space on the same native qubits.

## Hand proof: code and phase witness

Write `e1=|1000>`, `e2=|0100>`, `e3=|0010>`, `e4=|0001>`.
The source encoding is

\[
\begin{aligned}
J|0\rangle&=(e_1+e_4)/\sqrt2,&
J|1\rangle&=(e_1-e_4)/\sqrt2,\\
J|4\rangle&=(e_2+e_3)/\sqrt2,&
J|2\rangle&=(e_2-e_3)/\sqrt2,\\
J|3\rangle&=(|1100\rangle-|0011\rangle)/\sqrt2.
\end{aligned}
\]

All columns have norm one; distinct one-excitation pairs are orthogonal,
and the last column has two excitations. Thus `J` is an isometry. Let `F`
reverse the four site positions. It exchanges `e1,e4`, exchanges `e2,e3`,
and exchanges `|1100>,|0011>`. Direct substitution gives `FJ=JK`.
Consequently the geometric permutation is a Hermitian involution and its
restriction is exactly the stated code observable.

For every real `phi`,

\[
|\psi_\phi\rangle=(e_1+e^{i\phi}e_4)/\sqrt2\in J(R),\qquad
\langle\psi_\phi|F|\psi_\phi\rangle=\cos\phi.
\]

The membership follows because `e1,e4` span `J|0>,J|1>`. The expectation
is `(exp(i phi)+exp(-i phi))/2`. Every computational-basis population is
independent of `phi`, so this is genuine relative-amplitude phase
sensitivity, not a change of populations or a reference to the grid-origin
sector label.

## Hand proof: an entirely adjacent circuit

All gate lists in this section are **chronological**, acting left to right
as written. A controlled gate is defined by its action on computational
basis control states and extended linearly. No intermediate gate is read or
declared to form a record.

Let

\[
V=\frac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}.
\]

Its eigenvectors are the `X` eigenvectors, with eigenvalues `1,i`, so `V`
is unitary and `V^2=X`. `CX(a,b)` means controlled `X` with control `a`
and target `b`; `CV` and `CVdagger` have the analogous meaning. `S(a,b)`
is SWAP. All these are supplied mathematical gates, not derived dynamics.

For any two sites `a,b` distance two apart through `t`, the chronological
list

`S(a,t), CX(t,b), S(a,t)`

implements `CX(a,b)` and restores the state at the intermediate site,
including correlations. This is just conjugation by the tensor-factor
permutation; it does not copy an unknown quantum state. Each operation is
on adjacent sites.

For distinct sites `c,a,b`, the chronological list

`CV(b,a), CX(c,b), CVdagger(b,a), CX(c,b), CV(c,a)`

is Toffoli with controls `c,b` and target `a`. To check it, put the two
controls in basis states `c,b in {0,1}` and allow an arbitrary target state.
The three controlled-`V` target operations give total exponent

\[
b-(b\mathbin{\oplus}c)+c=2bc
\]

of `V`, while the two `CX(c,b)` operations restore `b`. The target therefore
undergoes `X` exactly for `b=c=1`; basis linearity proves the identity even
for entangled inputs.

Place `c,a,b` at three consecutive sites in that order. The two `CX(c,b)`
gates have distance two and each is replaced by the three adjacent gates
above, using `a` as the intermediate site. `CV(b,a)` and `CV(c,a)` are
already adjacent. The Toffoli therefore uses `1+3+1+3+1=9` adjacent
two-site gates exactly.

Now the chronological list

`CX(a,b), Toffoli(c,b;a), CX(a,b)`

is controlled SWAP of `a,b`, controlled by `c`. For `c=0` the CNOTs cancel.
For `c=1`, a basis pair `(a,b)` becomes
`(a,a XOR b)`, then `(b,a XOR b)`, then `(b,a)`.
Linearity again proves the complete unitary identity. This supplies a
controlled swap on three consecutive sites in 11 adjacent two-site gates.

For `i=1,2,3`, controlled `S(i,i+1)` with control site `0` is implemented
as follows:

1. Apply `S(0,1), S(1,2), ..., S(i-2,i-1)`. The list is empty for `i=1`.
   The output/control tensor factor is now at site `i-1`, and the two
   target factors at `i,i+1` have not moved.
2. Apply the preceding 11-gate controlled-SWAP circuit on the consecutive
   triple `(i-1,i,i+1)`.
3. Undo the swaps from step 1 in reverse order.

This is exactly the desired controlled swap, restores all routed factors,
and uses `11+2(i-1)` adjacent two-site gates. The routing swaps are
unconditional, so the proof holds when the control is in superposition.

Reversal of four factors is the chronological list of adjacent
transpositions

`S(1,2), S(2,3), S(3,4), S(1,2), S(2,3), S(1,2)`.

Indeed, the labels evolve

`1234 -> 2134 -> 2314 -> 2341 -> 3241 -> 3421 -> 4321`.

Replace each swap by its controlled version with the same output/control
site `0`. The product is `C_F`: identity on the data for control `0`, and
`F` for control `1`. Its adjacent-gate count is
`11+13+15+11+13+11=74`.

## Hand proof: fresh permanent output

Apply `H` to site `0`, then `C_F`, then `H` again. For every pure data state
`|psi>` the final joint state is

\[
|0\rangle\Pi_+|\psi\rangle+|1\rangle\Pi_-|\psi\rangle,
\qquad \Pi_\pm=(I\pm F)/2.
\]

The two projectors are orthogonal and sum to identity because `F` is a
Hermitian involution. The supplied final Born instrument at site `0`
therefore reads `0` or `1` with the corresponding squared norms. On the
active code,

\[
\Pi_+J=J(|0\rangle\langle0|+|4\rangle\langle4|),\qquad
\Pi_-J=J\sum_{a=1}^3|a\rangle\langle a|.
\]

Thus both conditional data states remain in the five-state code whenever
their probabilities are nonzero. The result extends to mixed code states
and external entanglement by the same operator identities. No intermediate
code-preservation claim is needed.

For the explicit phase family,

\[
\Pr(0\mid\psi_\phi)=\frac{1+\cos\phi}{2},\qquad
\Pr(1\mid\psi_\phi)=\frac{1-\cos\phi}{2}.
\]

The exact cases are `phi=0: (1,0)`, `phi=pi: (0,1)`, and
`phi=pi/2: (1/2,1/2)`. In particular `J|0>` and `J|1>` are perfectly
distinguished and each is unchanged after its result. All distributions
here use the explicitly supplied Born instrument, not the axiom's
unspecified admissibility distribution.

After the instrument, only the output is read. Its content `0` or `1`
determines the readout and the schedule never changes that site again.
This realizes permanence by an imposed schedule restriction. The gate
construction does not derive a persistence dynamics or prove future
immunity against arbitrary interventions.

If site `0` was a native spectator, then outcome `1` changes its originally
fixed quantum state `|0>`. The relevant output subspace is
`C_data tensor span{|0>,|1>}_output`; it is not the original `C_p` with
every spectator fixed. Fresh outputs also consume available space; this
finite one-output construction makes no indefinite-resource claim.

## A direct data-record test

Supply a different instrument: form permanent computational-basis records
on the four data sites before the phase circuit. With outcomes forgotten,
its quantum channel is complete dephasing

\[
\Delta(\rho)=\sum_{z\in\{0,1\}^4}|z\rangle\langle z|\rho
 |z\rangle\langle z|.
\]

For every `phi`,

\[
\Delta(|\psi_\phi\rangle\langle\psi_\phi|)
=\tfrac12|e_1\rangle\langle e_1|+
 \tfrac12|e_4\rangle\langle e_4|.
\]

Even retaining the classical data-record outcomes does not distinguish the
two phases: their full outcome-labelled ensembles agree. Since
`<e1|F|e1>=<e4|F|e4>=0`, the quantum phase circuit applied formally to this
mixture produces `(1/2,1/2)`, including for the formerly deterministic
`phi=0,pi` inputs. Moreover its changing gates would not be allowable on
already locked data under the specified permanence interpretation. The
fair result is the comparison for the dephased quantum channel, not a
claim that overwriting permanent records is permitted.

This is one instrument-specific example. It does not prove that every
record destroys every quantum observable. Recording an observable compatible
with the state, recording after the computation, or using fresh output
sites is a different case. The fresh-output construction above supplies the
explicit positive comparison.

## Finite communication versus a generator and a law

Each elementary operation acts on one site or one adjacent pair, while the
composed result depends on amplitudes originally separated by three native
edges. Intermediate gates can leave the code. For example `S(2,3)` sends
`J|3>` to `(|1010>-|0101>)/sqrt(2)`, orthogonal to all five
code columns. A finite compiled operation whose final action preserves the
code therefore need not arise from a generator preserving that code at
each infinitesimal step. This witness neither constructs nor excludes a
fixed nearest-neighbor generator for the desired Hamiltonian.

The circuit chooses an oriented link, an output, a computational basis,
specific gates and an external schedule. Translating or properly rotating
the complete apparatus produces the same construction on the translated
or rotated segment. That covariance of a supplied experiment is weaker
than deriving a single autonomous covariant admissibility/formation law.
In particular no transition probabilities on configurations of permanent
records have been supplied or proved to depend only on neighbor records.

No stronger locality axiom is required for this conditional example:
nearest-neighbor elementary operations already compose across a path. The
following physical interpretations remain supplied conditions: ordinary
multisite tensor composition and entangled density operators; recordless
coherent data and output preparation; the chosen five-state code and origin;
the allowed reversible gates; the schedule and its stopping rule at a
recorded site; computational-basis instruments with Born probabilities;
and interpreting instrument outcomes as permanent readable records. The
one-site `M_2(C)` presentation alone supplies none of these identifications.
The literal framework statement that a state is a configuration of records
does not identify distinct recordless quantum preparations with distinct
framework states. Establishing that bridge is still an open task, rather
than a contradiction or a derived no-go.

## Bounded method search and credit

After freezing the hand derivation, a targeted method search was run on
2026-11-08. Its timing is recorded explicitly: this was a restricted-input
independent probe, not a fresh novelty campaign. There is no novelty claim
for the circuit primitives or the interference test. No supervisor candidate
or open-PR candidate was read; open-PR comparison remains outside this
probe's coverage.

The landed-repo search at `f5af11cd0102cfd0b51aef0911f600130bf5beb1` was
`git grep -n -i -E 'swap test|hadamard test|fredkin' origin/main -- 'docs/*.md'`.
It returned existing Fredkin/compiler notes, including
`FULL128_TWO_RAIL_FIXED_LAW_COMPOSITIONAL_INDUCTION_BOUNDED_THEOREM_NOTE_2026-07-24.md`
and
`PHYSICAL_M2_TYPED_RADIUS_ONE_COMPILER_TOURNAMENT_CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md`.
These search excerpts were not used as proved results or fully reviewed;
their broader physical/compiler claims are not imported. The finite
five-state readout obligation here is checked explicitly above.

The live literature queries were
`site.arxiv.org quantum fingerprinting Buhrman Cleve Watrous de Wolf controlled swap test 2001`
and
`site.arxiv.org Barenco elementary gates quantum computation controlled square root NOT Toffoli 1995`.
The accessible primary PDFs were opened, and the relevant exact passages
were inspected:

- Adriano Barenco, Charles H. Bennett, Richard Cleve, David P. DiVincenzo,
  Norman Margolus, Peter Shor, Tycho Sleator, John Smolin and Harald
  Weinfurter, [Elementary gates for quantum computation](https://arxiv.org/pdf/quant-ph/9503016),
  Lemma 6.1, PDF pages 14–15, give the controlled-square-root decomposition
  of a doubly controlled one-qubit unitary. The required case is `U=X`,
  with `V^2=X`; the basis/exponent proof above rechecks that case and its
  exact phases. The adjacent routing and the 74-gate count are separately
  proved here. Their general universality theorem is not needed.
- Harry Buhrman, Richard Cleve, John Watrous and Ronald de Wolf,
  [Quantum fingerprinting](https://arxiv.org/pdf/quant-ph/0102001), PDF page 3,
  use Hadamard, controlled SWAP, Hadamard and a final control measurement.
  The present test uses a different Hermitian involution, the four-site
  reversal `F`, and rechecks its projector instrument directly. Their
  fingerprinting bounds are not used.

These are standard quantum-circuit methods, with their mathematical
hypotheses checked here. The published methods do not establish any
framework-to-quantum-state or record-formation bridge.

## Verification state and next decision

Closed by hand: code isometry and `FJ=JK`; phase expectations; exact
controlled-square-root/Toffoli identity; Fredkin identity; adjacent routing;
reversal order; instrument probabilities and code preservation; the
data-dephasing comparison. These arguments use computational-basis algebra
and tensor-permutation conjugation, not imported simulator output.

This worker has not read the supervisor's candidate, run a numeric job,
committed, pushed, edited an authority or prompt file, or performed formal
review/audit. After the freeze the supervisor reported reading the entire
proof and hand-checking the `V` exponents, routed Toffoli, Fredkin and 74-gate
count, with consistent results. That research check is distinct from the
planned focused review of integrated source and runner. The next decision is whether
the larger program wants this finite readout construction with explicitly
supplied quantum-state/instrument premises, or must first derive a native
record-process bridge. No general impossibility claim is established.
