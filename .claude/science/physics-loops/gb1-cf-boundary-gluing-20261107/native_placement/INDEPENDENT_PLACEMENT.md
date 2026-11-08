# Independent native placement probe

Status: FROZEN independent derivation, before any supervisor native-placement
candidate exposure. Final source-identity checks matched the launch identities.
This file is the only write authorized for this probe.
It is a conditional mathematical probe, not a retained claim, landing review,
audit result, or proposal to alter an axiom.

## Source and launch checkpoint

- Checker worktree HEAD and local `origin/main`:
  `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
- Supplied-model worktree HEAD:
  `17f68f575f3de7c1a24a4761e01c8307a9e99955`.
- Read the exact `INDEPENDENT_SPEC.md` first, then the current workflow and the
  three authorized scientific inputs, in full. The combined first read was
  truncated at the boundary note; the entire boundary note was reread separately.
- Input Git blobs, from the supplied-model worktree:
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`:
    `bc23300becfe4e4db57153c0e94cfcdf2338da71`.
  - `docs/audit/data/axiom_premise_nodes.json`:
    `b93959cca4f7e26c673cdccbe601e50c3cb93daa`.
  - `docs/SU2_FINITE_BOUNDARY_FLUX_ASSOCIATIVE_GLUING_BOUNDED_THEOREM_NOTE_2026-11-07.md`:
    `e3e73ee474cbcc7337c481a9bb54e447b7e00208`.
- `python3 scripts/lab_ops.py preflight` exited 0: disk 120 GB free, memory
  31% free, load 4.6, nice works, origin reachable, `preflight: go`.
  It explicitly reported no target/model-floor check and unavailable `ulimit`
  memory protection. This probe launches no numeric job.
- The inherited model/effort was not overridden. No runtime model/effort
  metadata was exposed by preflight; no stronger provenance is claimed.
- The working trees contained pre-existing untracked research artifacts.
  They are not read or changed by this probe. No scripts, commits, pushes,
  authority changes, or external messages are authorized here.
- The workflow and negative-claim scope procedure were read from the pinned
  main checkout. The brief limits scientific reading to the three named
  inputs: no other placement files, campaign history, PR search, or literature
  search was performed. This is not a priority or exhaustiveness claim.

## Exact question and supplied mathematical conditions

Let `G = Z^3 semidirect O` be the native geometric space group, where `O` is
the proper cubic rotation group. Its action below is the literal permutation
of native site tensor factors. No spatial rotation of internal SU(2) indices
is introduced. The supplied link is

\[
R=(V_0^*\otimes V_0)\oplus(V_{1/2}^*\otimes V_{1/2}),\qquad \dim R=5,
\]

with reversal

\[
J=\operatorname{diag}(1,-1,-1,-1,1)
\]

in the real basis `|0>,|1>,|2>,|3>,|4>` of the boundary note. The question is
about an injective quantum encoding, not a noninjective readout, approximate
simulation, or selected small set of gauge states. Both full link Hilbert
space and the complete Gauss-invariant sector are examined.

Tensor products of native two-dimensional Hilbert spaces, the tensor-product
link model, its SU(2) action, its Gauss constraints, and the chosen code
subspaces are explicit mathematical conditions. The Qubit axiom states the
one-site algebra `M_2(C)`; it does not itself state this composition law.
The current registry supplies no omitted axiom that selects this link model,
its register placement, a code initialization, or a dynamics/readout bridge.

Finite tori below have `n >= 3` coarse sites in each direction, so the cubic
graph is simple, with `N=n^3` vertices and `E=3N` undirected edges. Positive
coordinate orientation is a convention; spatial symmetries reverse a link
using `J`. The constructions are local and extend to infinite volume as
compatible local code conditions. Finite-volume dimensions make the resource
statements unambiguous.

## 1. Equal-spacing capacity fails even after imposing Gauss law

**Full-link statement.** An exact encoding into `M` native qubits requires

\[
2^M\ge 5^E.
\]

This follows from injectivity of a linear map between finite Hilbert spaces.
At equal spacing on the cubic torus, `M=N`, `E=3N`, so it is impossible.
Entangling the encoder, overlapping operator descriptions, or changing basis
cannot change this inequality. It counts physical qubits once.

**Gauss-invariant statement.** For any finite cubic subgraph, decompose the
link tensor product by its occupied-edge set `A`, where occupied means
`j=1/2`. At each vertex, regroup the incident endpoint factors. Their singlet
multiplicity is zero for odd degree and, for degrees `0,2,4,6`, is respectively
`1,1,2,5`. These numbers follow from the spin-half weight counts:

\[
m_0(2k)=\binom{2k}{k}-\binom{2k}{k-1}
\quad(k=0,1,2,3),
\]

with the out-of-range binomial coefficient zero. Only integer spins occur
for an even number of half-spin factors. Each integer spin `j>0` contributes
one weight-zero and one weight-one state, while spin zero contributes only
weight zero, proving the difference formula. Dual factors do not change the
count because the fundamental SU(2) representation is self-dual.

Consequently the exact dimension on a closed graph is

\[
D_G=\sum_{A:\,d_A(v)\ {\rm even}\ \forall v}
       \prod_v m_0(d_A(v)).
\tag{1}
\]

Distinct occupied-edge sets are orthogonal. Every even-degree set contributes
at least one singlet, obtained by pairing half-spin ends at each vertex.
For a connected graph, even-degree sets form the kernel of its incidence
matrix over `F_2`, whose rank is `V-1`: a spanning tree gives the lower bound
on rank, and the sum of all rows vanishes. Hence

\[
D_G\ge 2^{E-V+1}.
\tag{2}
\]

On the cubic torus this is `2^(2N+1) > 2^N`. The complete gauge sector also
cannot be encoded into the same `N` site qubits. A second lower bound on the
torus is `D_G >= 5^N`, from the single fully occupied configuration, which
has six half-spin ends and five independent singlets at every vertex.
These are compatible lower bounds, not counts of disjoint extra sectors to
be added without correcting overlap.

This is not only a periodic-boundary artifact. In an `n by n by n` open cube,
`V=n^3` and `E=3(n-1)n^2`; the even-subgraph lower bound has exponent
`2n^3-3n^2+1`, exceeding `n^3` for every `n>=3`. Even if a bounded-support
encoding uses a fixed-radius native boundary halo, it has only
`n^3+O(n^2)` physical qubits; the lower bound has exponent
`2n^3-O(n^2)`. It therefore fails for sufficiently large cubes. Extending
these states by empty exterior links preserves their Gauss constraints.

The quantified obstruction is exact encoding of the entire indicated model
at equal asymptotic site density, with supplied quantum composition. It says
nothing against a restricted low-energy sector, a nonfaithful readout, an
approximation, increased spacing, or a different substrate/model.

## 2. Coarse spacing removes the dimension obstruction, but not all geometry

At integer spacing `s`, `M=s^3 N` native qubits are available. Full-link
capacity requires `s^3 >= 3 log_2(5)`. In particular `s=2` passes dimension
counting, since `5^3=125 < 2^8=256`. An abstract full-link isometry exists at
that volume. Grouping the three positive outgoing links in a cell into seven
qubits is also a finite-support encoding respecting the coarse translation
subgroup, but this grouping does not establish proper-rotation covariance.
No claim that spacing two is sufficient for all requested structure follows.

For Gauss-only encoding the necessary bound is `s^3 N >= log_2 D_G`, with
`D_G` given by (1); it is weaker than the full-link requirement. The two
lower bounds above still exclude spacing one, and neither excludes spacing
two. An actual tensor factor for each logical link is an additional encoding
condition; it must not be silently imposed on a Gauss-only encoding.

Without geometric reversal, a separate link register needs at least three
qubits. Disjoint such registers require at least `9N` physical sites. But
three are insufficient if the native geometric link reversal must preserve
each register and induce exactly `J`:

**Reversal lemma.** An involution of three physical sites is either the
identity or one transposition. Its permutation action on three qubits has
minus-eigenspace dimension at most two: a swap has one antisymmetric
two-qubit state, tensored with the remaining qubit. The target `J` has a
three-dimensional minus eigenspace. An injective intertwiner cannot exist.

The relevant geometric involution is available in the allowed group: for
the edge `0 -> s e_x`, `(x,y,z) -> (s-x,y,-z)` reverses its ends and squares
to the identity. Thus a covariant allocation of disjoint per-edge registers
with the exact per-link intertwining equation `rW=WJ` must use at least four
qubits per edge, not merely `ceil(log_2 5)=3`. It needs at least `12N` data
sites. This is a bound on that allocation class, not on joint encodings,
constrained gauge-only codes, or encodings with a different supplied on-site
symmetry action.

**Phase caveat, with a counterexample to a broader statement.** If only the
conjugation action on observables is required, `J` and `-J` are equivalent.
Three collinear qubits have a two-dimensional odd eigenspace and a
six-dimensional even eigenspace under reversal. Encode `|0>` and `|4>` as
the outer-pair singlet tensored with middle-qubit zero and one; encode
`|1>,|2>,|3>` as any three orthonormal even vectors, for example `|000>`,
`|111>`, and `(|001>+|100>)/sqrt(2)`. This gives `rW=-WJ`. It fits on the
three interior sites at spacing four and has the same operator conjugation
law. Thus the four-qubit minimum is not an obstruction to projective or
observable-only equivariance. The construction below uses four qubits to
meet the exact supplied `J`, avoiding that additional choice of meaning.

## 3. A finite-support placement respecting the coarse geometric group

Take coarse vertices `5Z^3`. Assign the four interior native sites of each
coarse edge to that edge, in order along its positive orientation. These
blocks are disjoint: perpendicular grid edges can meet only at coarse
vertices, and all endpoints were excluded. Put every unused native qubit
in `|0>`. Encode one link by

\[
\begin{aligned}
W|0\rangle&=|0000\rangle,& W|4\rangle&=|1111\rangle,\\
W|1\rangle&=(|0001\rangle-|1000\rangle)/\sqrt2,\\
W|2\rangle&=(|0010\rangle-|0100\rangle)/\sqrt2,\\
W|3\rangle&=(|0011\rangle-|1100\rangle)/\sqrt2.
\end{aligned}
\tag{3}
\]

These are five orthonormal vectors, so `W` is an isometry. Let `r` reverse
the four physical positions. The first and last vectors are fixed; the
other three change sign. Therefore `rW=WJ` exactly.

A proper cubic rotation preserving an oriented axis fixes the four collinear
positions individually. A proper rotation taking a positive edge to a
negative one reverses their order and induces exactly `J`; it does not rotate
the internal labels `1,2,3` as spatial components. Every coarse translation
and proper cubic rotation permutes the collection of blocks, preserving the
unused sites. Thus the product isometry intertwines the actual native
geometric action of

\[
G_5=5\mathbb Z^3\rtimes O
\]

with the supplied gauge model's geometric action. Proper rotations about
coarse sites are included by composing these translations and rotations.
The same conclusion holds after imposing the model's Gauss projectors.

Any link operator is encoded as `W A W*` on that four-qubit support; a gauge
unitary is extended by the identity on its orthogonal complement. The
intertwining of reversal is enough to preserve the supplied endpoint-action
convention. Explicitly, `J P_a J=-P_a` for `a=1,2,3` and `J P_4 J=P_4`,
so `J U J=U^dagger`, as required for link reversal. Coarse gauge vertices
and plaquettes therefore have finite-support encoded operators. Neither a
nearest-neighbor native generator nor a Record law has been produced.

This explicit placement disproves a blanket claim that the five-state model
cannot fit into one native qubit per site with any finite coarse spacing.
It is not an optimal-spacing theorem: spacing three or four with joint or
differently arranged registers has not been excluded.

## 4. A periodic code and its translation orbit are different objects

Let `C_0` be the spacing-five product code just constructed. It is not
invariant under a native unit translation. For a witness, put `|4>` on the
coarse edge from `0` to `5 e_x` and `|0>` on every other link. Its four data
qubits at positions `1,2,3,4` along that edge are all one. Translating by
`e_x` puts a one at the coarse vertex `5 e_x`, whereas every state of `C_0`
has that unused qubit fixed to zero. The translated state is outside `C_0`.

The orbit is indexed by translates `C_t=T_t C_0`, with phase labels in
`(Z/5Z)^3`. A covariant *family* of these codes does not make its
selected member invariant. They are not automatically orthogonal sectors:
the all-zero physical vector belongs to every one of them. Nor is their
set-theoretic union a code Hilbert space; a finite union of distinct
equal-dimensional complex subspaces is not a vector subspace.

Their linear span is a full-space-group invariant subspace, because the
group permutes the translates. On a finite torus its dimension is strictly
larger than `dim C_0`, by the explicit translated witness above. This is a
valid invariant subspace, but calling it the same encoded model requires
an additional algebra/sector argument: overlapping copies do not give a
specified direct sum, and a link operator defined for one copy need not
preserve the span. No such implication follows from taking an orbit or a
linear span alone.

## 5. Explicit full-space-group invariant code with translation sectors

There is also a constructive answer to the weaker, but genuine, request for
a full native space-group invariant code carrying translated copies of the
coarse model. It uses markers on existing native sites; it does not add a
local Hilbert-space factor. The construction is included so that absence of
invariance of `C_0` cannot be mistaken for a general symmetry obstruction.

Use coarse spacing nine. On the edge `9v -> 9v+9 e_i`, put the four data
qubits at `9v+k e_i`, `k=3,4,5,6`, and use (3). In the residue group
`(Z/9Z)^3`, define the data and marker sets

\[
D=\{k e_i:i=1,2,3,\ k\in\{3,4,5,6\}\},\qquad
M=\{-1,0,1\}^3.
\tag{4}
\]

They are disjoint. Fix marker qubits at residues in `M` to `|1>` and all
other nondatum qubits to `|0>`. Call this product code `K_0`. It has the
same link dimension as the earlier code and is invariant under
`9Z^3 semidirect O`: `M` is a cube, `D` is invariant under signed axis
permutations, and reversal takes `3,4,5,6` to `6,5,4,3`.

**Local phase-separation lemma.** For every nonzero residue translation
`t`, there is a site in `(M+t) \ (M union D)`.

To prove this, suppose instead `M+t` were contained in `M union D`. Write
`B={-1,0,1}` and `A_i=t_i+B`. For any coordinate `i` and any `a in A_i`,
choose nonzero values in each of the other two three-element coordinate
sets. The resulting point of `A_1 times A_2 times A_3` lies off all
coordinate axes, hence is not in `D`. It must lie in `M`, so `a in B`.
Therefore `A_i=B` for all `i`. The only translation preserving `B` in
`Z/9Z` is zero: the translation must itself lie in `B`, and either nonzero
choice sends an endpoint to `2` or `-2`. Thus `t=0`, a contradiction.

At a witness site from this lemma, every state of `T_t K_0` has qubit one,
and every state of `K_0` has qubit zero. Therefore the 729 translated
subspaces are pairwise orthogonal. On a finite torus define

\[
K_{\rm inv}=\bigoplus_{t\in(\mathbb Z/9\mathbb Z)^3} T_t K_0.
\tag{5}
\]

Native unit translations permute these sectors, with a coarse translation
of logical links when a residue wraps. Proper cubic rotations send the
sector `t` to `Rt` and act by the already checked link reversal convention.
Thus (5) is invariant under the *full* native geometric space group,
including proper cubic rotations about every native site. Its dimension is
`729 * 5^(3N)` before Gauss projection and `729 * D_G` afterward.

This is more than an invariant-span assertion. The phase can be recognized
by bounded-support projectors. In any box containing one representative of
each residue modulo nine, let `P_t` test the prescribed one and zero
qubits of phase `t`, ignoring that phase's data qubits. The separation
lemma gives

\[
P_t|_{T_uK_0}=\delta_{tu}I.
\]

For a finite-support encoded data operator `A_t` in that phase, the
operator `P_t A_t P_t` acts as `A_t` on its sector and as zero on the
others, and preserves (5). The marker tests never constrain the phase's
own data. Taking the test box near the data support bounds the operator's
range independently of total system size. Their geometric translates
therefore give a covariant family of finite-range operators on (5).
There is no claim that these operators are nearest-neighbor.

The construction has an explicit cost: (5) contains a translation-phase
sector in addition to the coarse gauge model. Selecting one sector returns
a periodic code; keeping all sectors gives an invariant code whose states
can break translation symmetry. These are distinct mathematical statements.
An invariant code need not have every one of its states invariant.

**A failed shortcut to removing the sectors.** Define the naive coherent
average `W_av psi = 729^(-1/2) sum_t T_t W_0 psi`, using the same logical
state in every phase. This is an isometry because the sectors are orthogonal.
It is not in general a translation-invariant image. Translating by `e_x`
cycles the phase labels; when `t_x=8` wraps to zero, that branch acquires
one coarse logical translation, while branches without a wrap do not.
For a state with `|4>` on one localized link and `|0>` elsewhere, those
logical branch states differ. Orthogonality of phases prevents cancelling
the discrepancy. Restricting to coarse-translation-invariant logical states
would avoid this witness, but discard most of the original model.
More elaborate coherent encodings have not been excluded by this example.

## 6. Answer, scope stress-test, and remaining decision

The proved result is a placement sandwich. At equal spacing, exact faithful
full-link and complete-Gauss-sector encodings fail dimension counting.
At coarse spacing there is an explicit finite-support, coarse-space-group
equivariant embedding. Full native space-group invariance is attainable by
an explicit larger code with locally distinguishable translation sectors.
Thus neither a blanket obstruction nor an unqualified claim that a fixed
periodic allocation is already homogeneous is correct.

The unresolved question is whether the intended physical use permits these
translation sectors, or instead requires one exact copy of the whole coarse
model with a full native geometric action and finite-support observable
encoding. No obstruction or construction for the latter general problem is
claimed here. In either case, the present finite-range code construction
does not provide the axiom's fixed nearest-neighbor admissibility probability
law or its permanent, content-readable records. Code basis, code domain,
initialization, tensor composition, and the SU(2) model remain supplied
conditions. The axioms are not changed or shown to select these conditions.
The new mathematical placement closes a representation question; it does
not establish that this framework describes physics.

The repository negative-claim procedure was used for scope scrutiny, with
the following explicit limits. This bounded proof handoff is not a complete
negative-claim submission packet and claims no procedural PASS.

- N1: full-link dimension and Gauss reduction are the two actual resource
  routes checked. Coarse blocks and invariant translation sectors are
  constructive counter-routes, not failures to be relabelled to meet a
  five-failed-route quota. No fifth distinct failure is manufactured.
- N2: no pairwise-independent physical wall count is asserted. Global
  capacity and a single register's reversal character are different checks:
  three qubits pass the latter's raw dimension test but fail its character
  test; passing a four-qubit character test does not supply equal-density
  storage for three links per vertex.
- N3: composition, exact faithfulness, actual permutation action, full
  retained state sector, block factorization where used, exact versus
  projective reversal, basis/marker initialization, and the distinction
  between code and physical law are all explicit. Internal SU(2) is never
  identified with spatial rotation.
- N4: no historical no-go or unmatched residual is used as evidence.
- N5: per-link reversal, per-cell volume, finite-graph gauge dimension,
  bounded-halo limits, and lattice-wide code invariance are distinguished.
  None of their narrow failures is promoted to a failure at every scale.
- N6: changing a mathematical encoding or adding coarse code sectors is
  not declared an axiom change. Supplying a physical law is a separate
  unresolved identification; no new primitive is silently registered.
- N7: the strongest objection to a blanket no-go is explicit here: exploit
  spare sites at coarse spacing, match reversal by antisymmetric codewords,
  and restore group invariance by a locally marked translation orbit. This
  mechanism works, so the blanket no-go is rejected. Joint encodings remain
  a further unexcluded route to improving spacing or removing phase sectors.
- N8: historical/cross-cycle search and publication-packet checks were not
  performed because this brief restricts sources and forbids commits and
  extra artifacts. No completeness or submission-readiness claim follows.

## Final recovery checkpoint

One coherent proof package is complete: (1) and (2) give the exact gauge
count and capacity bounds; (3) is a checked geometric intertwiner; (4) and
(5) supply an explicit invariant code with a proved local sector test.
The naive single-sector and naive coherent-average rescues have concrete
counterexamples. There was no numerical job and no supervisor-candidate
exposure. The completed document was read in full, and the source-identity
refresh matched all three scientific blobs and both pinned worktree HEADs;
the read methodology files had no differences from the pinned main. The
final content hash is reported in the handoff message. The residual is the
physical nearest-neighbor/Record realization and, if required, removal of
the extra phase sector while keeping the entire model, locality, and native
symmetry. This independent artifact is now frozen.
