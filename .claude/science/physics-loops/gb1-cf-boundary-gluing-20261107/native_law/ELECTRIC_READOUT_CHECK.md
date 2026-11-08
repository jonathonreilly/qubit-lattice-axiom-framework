# Independent electric-energy readout construction

**Claim type:** bounded_theorem. **Support:** conditional-support.
Hand construction frozen on 2026-11-08 without reading the supervisor's
new candidate. This is a research probe, not a formal review or audit.
The initial frozen-file SHA-256 was
`6eb4a41b7e0f77195868f4d7a0470580ff74648476f31a71dc91a69e574b30d7`.
Subsequent edits clarify notation, the output gauge convention and the
post-freeze comparison; the decoder, gate list and counts are unchanged.

## Current checkpoint and input identity

The focused target is a fresh-record, adjacent-site measurement of
`E^2=(3/4) sum_{mu=1}^4 |mu><mu|` on the entire five-state active code,
including entanglement with other systems. A constructive route closes it
under the same explicitly supplied quantum-circuit and record-instrument
conditions as the preceding probe. No work qubits are needed.

The checker worktree is
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair-check/Physics`.
Its HEAD and local `origin/main` are
`f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
The methodology and three scientific inputs retain their previously read
bytes, verified again before this write. Source root:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/`.

| Source | SHA-256 |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753` |
| `docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md` | `0d457372fe995529ad1fc13e3c9d6f696fe27b9a5ee3b1ef78852214a928604c` |
| `docs/audit/data/axiom_premise_nodes.json` | `615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37` |

The unchanged checker `SCIENCE_WORKFLOW.md` SHA-256 is
`1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`.
The first shell command of this extension was
`python3 scripts/lab_ops.py preflight`; it returned `preflight: go`, with
118 GB free disk, 41% free memory, load 3.4, working nice and reachable
origin; no named model floor was checked and memory cap was unavailable.
The exact runtime model/effort remains unexposed and inherited; no override
was requested. There is no numeric job or numeric-lease use.

## Exact statement

Place the four code qubits at native cubic sites
`x_j=(j,0,0)`, `j=1,2,3,4`, and a fresh output at `x_0=(0,0,0)`.
Prepare the output in `|0>` without a record. Supply ordinary tensor-product
quantum kinematics, the one-site gates and adjacent two-site gates defined
below, an external schedule, and a final computational-basis Born
instrument on the output. After that instrument the output is permanent
and is not acted on again.

There is a circuit on these five actual sites, with **19 adjacent two-site
gates, 7 one-site gates, and one final one-site instrument**, whose action
on every code state is the exact Lüders measurement

\[
P_0=|0\rangle\langle0|,\qquad
P_1=\sum_{\mu=1}^4|\mu\rangle\langle\mu|,
\]

with output content `b=0,1` read as `3b/4`. The four-qubit code is restored
before the output is read. The result holds with arbitrary external
entanglement and preserves coherence within the four-dimensional
`E^2=3/4` eigenspace. There are **zero clean work qubits** to restore.
All routing uses the existing five sites and is undone coherently.

The readout scale `3/4` comes from the supplied SU(2) link model, not from
the circuit or the four axioms. The original full lattice code fixes every
spectator to `|0>`; an output of `1` leaves that full code even though the
active data code is restored. Thus this is an input/output construction on
the same native qubits, not invariance of the original fixed-spectator code.

## A two-bit flag for all five code vectors

As in the source, write `e1=|1000>`, `e2=|0100>`, `e3=|0010>`,
`e4=|0001>` and

\[
\begin{aligned}
J|0\rangle&=(e_1+e_4)/\sqrt2,&
J|1\rangle&=(e_1-e_4)/\sqrt2,\\
J|4\rangle&=(e_2+e_3)/\sqrt2,&
J|2\rangle&=(e_2-e_3)/\sqrt2,\\
J|3\rangle&=(|1100\rangle-|0011\rangle)/\sqrt2.
\end{aligned}
\]

The isometry of `J` was checked from these columns in the preceding probe;
the unchanged source identity permits reuse of that check.

All gate lists below are **chronological**. `S(a,b)` is SWAP;
`CX(a,b)` has control `a` and target `b`; `H(a)` is Hadamard on `a`.
Define the data decoder `W` by

`S(3,4), S(2,3), CX(1,2), H(1), CX(3,4)`.

Its first two swaps send a computational word `|a b c d>` to
`|a d b c>`: the old endpoints are at sites 1,2 and the old middle bits
are at sites 3,4. On `J|0>` and `J|1>`, the next CNOT and Hadamard decode
the two endpoint Bell phases:

\[
WJ|0\rangle=|0100\rangle,\qquad
WJ|1\rangle=-|1100\rangle.
\]

The last CNOT leaves these two words unchanged. For each of `J|2>`,
`J|3>`, `J|4>`, every contributing computational word has **exactly one
old middle bit equal to 1**. The endpoint CNOT and Hadamard do not change
those middle bits. The last `CX(3,4)` writes their parity into site 4,
so site 4 is exactly `|1>` on all three decoded vectors, including
arbitrary coherent superpositions of them.

Therefore the complete flag table is

| Input | Decoded site 1 | Decoded site 4 | Energy bit |
|---|---|---|---|
| `mu=0` | 0 | 0 | 0 |
| `mu=1` | 1 | 0 | 1 |
| `mu=2` | unrestricted | 1 | 1 |
| `mu=3` | unrestricted | 1 | 1 |
| `mu=4` | unrestricted | 1 | 1 |

Here unrestricted permits coherent superposition and entanglement, not a
measurement or hidden classical choice. Let

\[
P=|0\rangle\langle0|_1\otimes I_2\otimes I_3
\otimes |0\rangle\langle0|_4.
\]

The table proves the full operator identities

\[
PWJ=WJP_0,\qquad
(I-P)WJ=WJP_1,
\]

equivalently `W^dagger P W J=JP_0` and
`W^dagger(I-P)WJ=JP_1`. No assumption about basis-state-only data is used.

## Adjacent implementation of the flag, without work qubits

Set

\[
V=\frac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix},
\qquad V^2=X.
\]

The `X` eigenvectors have `V` eigenvalues `1,i`, verifying unitarity and
the square. Write `CV` and `CVdagger` for the corresponding controlled
two-site gates.

On three consecutive sites 0,1,2, the following **seven adjacent two-site
gates** implement Toffoli with controls 1,2 and target 0:

`CV(1,0), CX(2,1), CVdagger(1,0), CX(2,1),`
`S(2,1), CV(1,0), S(2,1)`.

Proof: the final three factors route the logical control at site 2 to site
1, apply its controlled `V` on site 0, and restore the routing, so they
equal `CV(2,0)` exactly. With computational control values `u` at 2 and
`v` at 1, the effective target exponent is

\[
v-(v\mathbin{\oplus}u)+u=2uv.
\]

The two CNOTs restore `v`. Hence the target changes by `X` precisely when
both controls are 1. Extension by linearity proves the unitary on arbitrary
entangled inputs and retains all phases. Routing is tensor permutation
conjugation, not measurement, resetting or copying.

Starting with decoded data and fresh output `|0>`, apply this flag circuit:

1. `X(1), X(4)` to turn the zero-controls into one-controls.
2. `S(3,4), S(2,3)` to route the site-4 control to site 2. Site 1 and the
   output at 0 are untouched.
3. The seven-gate Toffoli above on sites 0,1,2.
4. `S(2,3), S(3,4)` to undo the routing.
5. `X(1), X(4)` to undo the negative-control changes.
6. `X(0)` to complement the copied vacuum indicator into the energy bit.

This is a fully specified finite list, not an appeal to universality. It
has 11 adjacent two-site gates and 5 one-site gates. On every decoded
computational word it preserves the data and writes
`b=1 XOR ((1-r1)(1-r4))=r1 OR r4` to the output. Hence its action on an
arbitrary decoded data vector `|chi>` is

\[
|0\rangle_{\rm out}\,P|\chi\rangle
+|1\rangle_{\rm out}\,(I-P)|\chi\rangle.
\]

Now undo `W` by the chronological list

`CX(3,4), H(1), CX(1,2), S(2,3), S(3,4)`.

Both `W` and its inverse use four adjacent two-site gates and one
Hadamard. The complete count is thus `4+11+4=19` two-site gates and
`1+5+1=7` one-site gates. These are counts of the explicit list; no
optimality claim is made. The final record instrument follows the inverse.

## Exact instrument, external entanglement, and gauge covariance

Let `A` be any external Hilbert space and write an arbitrary input vector
in the code as

\[
|\Psi\rangle=\sum_{\mu=0}^4J|\mu\rangle|r_\mu\rangle_A.
\]

The external vectors need not be normalized or orthogonal. The full
unitary circuit takes the fresh-output input exactly to

\[
|0\rangle_{\rm out}J|0\rangle|r_0\rangle_A
+|1\rangle_{\rm out}\sum_{\mu=1}^4J|\mu\rangle|r_\mu\rangle_A.
\]

Thus its final Born instrument has Kraus operators `JP_bJ^dagger` on
the active code, tensored with identity on `A`. It is the Lüders
instrument, including on mixed inputs. In particular it reveals no
`mu` label within the four-dimensional energy eigenspace and preserves
its internal coherence. The output probabilities are
`||r0||^2` and `sum_{mu=1}^4 ||r_mu||^2` for normalized input.
All routing factors have been returned; nothing is discarded or reset.

The source supplies the endpoint representation
`R=(0,0) direct-sum (1/2,1/2)`. Consequently `P_0` and `P_1` are the
projectors onto its two invariant summands and commute with both endpoint
gauge actions. In the supplied lattice gauge model, the final link
instrument therefore commutes with gauge transformations at both endpoints
and, tensored with identity on other links, preserves the Gauss-invariant
subspace when the initial state lies there. On the extended input/output
space the output is assigned the trivial gauge action. This uses the
supplied representation identification and output convention. It is not a claim that the individual
native gates are gauge invariant or preserve the code/Gauss subspace at
intermediate steps. It implements an electric-energy **measurement**, not
the electric or magnetic Hamiltonian evolution or physical plaquette
dynamics.

## Phase witness and permanent-record scope

For the explicit code family

\[
|\psi_\phi\rangle=(e_1+e^{i\phi}e_4)/\sqrt2,
\]

the vacuum and occupied-sector amplitudes are `(1+exp(i phi))/2` and
`(1-exp(i phi))/2`. Hence

\[
\Pr(E^2=0)=\frac{1+\cos\phi}{2},\quad
\Pr(E^2=3/4)=\frac{1-\cos\phi}{2},\quad
\mathbb E[E^2]=\frac38(1-\cos\phi).
\]

At `phi=0` the readout is exactly 0; at `phi=pi` it is exactly `3/4`.
These states have identical computational-basis populations. Forming
computational-basis records on data first gives the same mixture
`(|e1><e1|+|e4><e4|)/2` for both, so that different instrument loses the
phase information. Existing permanent data records also prohibit changing
their locked possibilities under the imposed interpretation. The present
construction keeps data recordless and only forms the final fresh-output
record.

The output is readable solely through its final content `b`. Permanence is
imposed by never acting on that recorded site again; this is not a derived
persistence law. No extra spectator work qubits were introduced. If the
output is a spectator of the original native code `C_p`, result `1`
violates that code's fixed-`|0>` spectator condition. The final subspace is
instead the active code tensor the used output register, with every other
untouched spectator still fixed. A native law must still account for this
input/output extension and the availability of fresh recordless sites.

## Method reuse, comparison boundary, and verification state

This uses the same controlled-square-root identity verified in
`INDEPENDENT_PROPAGATION.md`; its exact source and hypotheses have not
changed. The method credit is Barenco and colleagues,
[Elementary gates for quantum computation](https://arxiv.org/pdf/quant-ph/9503016),
Lemma 6.1. The previous primary-source search and passage check are reused;
no novelty claim is made for that identity or for coherent flag/uncompute
measurement. The new load-bearing fact is the two-bit flag table for this
particular five-column encoding, proved above. No supervisor candidate was
read before freezing it, and no numerical simulation was used.

The closure is conditional on ordinary tensor quantum states, the given
code and SU(2) representation, selected basis/preparation, controlled gates,
schedule, Born instruments, and identification of their outcomes with
permanent records. None is derived here from the four framework axioms.
No one-step total range limit is assumed; the construction explicitly
composes nearest-neighbor operations.

The full five-column flag proof, square-root gate phases, routing,
uncomputation, counts, external-entanglement identity and gauge-commutation
argument are written out for the supervisor's independent check.
No authority/prompt files were edited; no commit, push or audit was run.

## Post-freeze comparison with the supervisor's route

After this construction was frozen, the supervisor described a different
candidate: Bell decode `J|0>` to `|0000>`, compute the four-bit zero
predicate with two clean work spectators, then uncompute. The supervisor
reported 65 pair gates, 12 one-site gates and exact checks. Those candidate
files and outputs were not read or rerun by this worker; those figures are
reported provenance, not independently verified evidence here.

The constructions agree on the entire five-state code: any unitary decoder
mapping `J|0>` to `|0000>` maps its four orthogonal companions away from
`|0000>`, so a clean coherent zero predicate gives precisely the same
two projectors `P_0,P_1` after uncomputation. The present route exploits
the code's middle-bit parity to use a two-bit predicate and no work qubits.

They have different native extensions outside the code. The present
predicate `P` has rank 4 on the native 16-dimensional data space; the
four-bit zero predicate has rank 1. The explicit normalized off-code state

\[
|\chi\rangle=W^\dagger|0000\rangle
=\frac{|0000\rangle+|1001\rangle}{\sqrt2}
\]

is orthogonal to all five columns of `J`. This circuit gives energy bit 0
on `chi`; the rank-one vacuum test `|J0><J0|` gives energy bit 1. Thus an
all-native-basis comparison between the two **extensions** would correctly
disagree; their exact agreement is on the quantified code domain and all
its external entanglements. Neither extension is claimed to be an axiom-
selected off-code law.
