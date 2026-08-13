---
claim_id: involution_rank_split_selects_traceless_ratio_axioms_do_not_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A second self-adjoint involution on C^8 has complementary projectors of ranks (4,4) and traceless ratio β=−α, so the May 2 identity for ranks (6,2) is not selected by Lattice, Qubit, Admissibility, or Record, and neither generator is U(1)_Y."
upstream_dependencies:
  - minimal_axioms
  - LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md
  - HYPERCHARGE_IDENTIFICATION_NOTE.md
  - PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md
  - GRAPH_FIRST_SU3_INTEGRATION_NOTE.md
runner: scripts/involution_rank_split_selects_traceless_ratio_axioms_do_not_2026_08_13.py
---

# Involution Rank Split Selects The Traceless Ratio; Axioms Do Not

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact rank-to-ratio mutation from one self-adjoint involution
on `C^8` to another, and the residual that the four axiom sentences do
not select `Y_0` over `Z_0`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/involution_rank_split_selects_traceless_ratio_axioms_do_not_2026_08_13.py`](../scripts/involution_rank_split_selects_traceless_ratio_axioms_do_not_2026_08_13.py)

## Result Up Front

Work on `C^8` with the standard orthonormal basis `e_0,...,e_7`. Two
self-adjoint involutions live on this same space. Their complementary
projectors have different ranks, so tracelessness forces different
eigenvalue ratios.

The first involution is the already-landed rank pair. Write

`Pi_+ = diag(I_6, 0_2)`, `Pi_- = diag(0_6, I_2)`.

Those are complementary orthogonal projectors of ranks `(6,2)`. They are
the spectral projectors of the involution `τ_Y = Pi_+ − Pi_-`. The May 2
note
[`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
already records the identity

`6 α + 2 β = 0  ⇒  β = −3 α`.

That identity is recomputed here and is not claimed new.
[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
supplies the same `(6,2)` multiplicities on the doubled weak-fiber
surface. The name-free parent
[`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
writes the generator as `Y_0 = P_sym − 3 P_anti`. In the coordinates of
this note that generator is

`Y_0 := Pi_+ − 3 Pi_-`,

with spectrum `{+1 × 6, −3 × 2}` and trace `6 − 6 = 0`.

The second involution is extra. Define

`σ = diag(+1,+1,+1,+1, −1,−1,−1,−1)`.

Then `σ^2 = I` and `σ^* = σ`. The complementary projectors

`Qi_+ = (I+σ)/2`, `Qi_- = (I−σ)/2`

have ranks `(4,4)`. Tracelessness is now `4 α + 4 β = 0`, so `β = −α`.
The generator

`Z_0 := Qi_+ − Qi_-`

has spectrum `{+1 × 4, −1 × 4}` and trace `0`. It is not a scalar
multiple of `Y_0`: the eigenvalue multisets
`{1,1,1,1,1,1,−3,−3}` and `{1,1,1,1,−1,−1,−1,−1}` differ.

The four axiom sentences in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
are quoted only as premises and are not edited. Lattice names the sites
of `Z^3`. Qubit names a one-site possibility domain with no privileged
possibility. Admissibility names a nearest-neighbor-determined
distribution. Record locks one admissible possibility and supplies an
additive scalar `I` with `I(empty)=0`. None of those sentences name `τ`,
`SWAP_23`, a `C^8` taste cube, or the rank pair `(6,2)` versus `(4,4)`.
They do not select `Y_0` over `Z_0`.

The scale `α = 1/3` is a convention. Cycle 692
[`PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md`](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md)
already records that the tested mechanisms do not derive it. The
rescaling `Y_like = Y_0/3` is that same convention and is not identified
with `U(1)_Y`. P-HY and anomaly-complete `U(1)_Y` remain open.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "A second self-adjoint involution on C^8 has ranks (4,4) and ratio -1. Lattice, Qubit, Admissibility, and Record do not select the (6,2) generator Y_0 over Z_0."
trace_class: negative_route_pruning
target_claim_id: involution_rank_split_selects_traceless_ratio
target_blocker_text: "axioms select the (6,2) LH split and the 1:(-3) ratio"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The (6,2) split is an extra involution choice. Axioms do not select Y_0 over Z_0. Do not identify Y_like with U(1)_Y. Do not adopt axiom text."
conditional_surface_status: "exact for the (4,4) involution mutation and the axiom non-selection; P-HY remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `H = C^8` with the standard orthonormal basis `e_0,...,e_7`. All
operators below are diagonal in this basis, so adjoints are complex
conjugates of the diagonal entries and every spectrum is read off the
diagonal.

The **landed rank pair** is the complementary pair of projectors

`Pi_+ = diag(1,1,1,1,1,1,0,0)`,
`Pi_- = diag(0,0,0,0,0,0,1,1)`.

Equivalently, they are the spectral projectors of the self-adjoint
involution

`τ_Y := Pi_+ − Pi_- = diag(+1,+1,+1,+1,+1,+1,−1,−1)`,

via `Pi_± = (I ± τ_Y)/2`. Ranks are `(6,2)`. A central two-value
operator on this split is `Y(α,β) := α Pi_+ + β Pi_-`. Tracelessness
is the linear equation `6α + 2β = 0`. The May 2 generator is the
`α = 1` point of that line:

`Y_0 := Pi_+ − 3 Pi_- = diag(1,1,1,1,1,1,−3,−3)`.

The **mutated rank pair** is the complementary pair of projectors of a
different self-adjoint involution on the same `H`:

`σ = diag(+1,+1,+1,+1, −1,−1,−1,−1)`,
`Qi_+ = (I+σ)/2 = diag(1,1,1,1,0,0,0,0)`,
`Qi_- = (I−σ)/2 = diag(0,0,0,0,1,1,1,1)`.

Ranks are `(4,4)`. A central two-value operator on this split is
`Z(α,β) := α Qi_+ + β Qi_-`. Tracelessness is `4α + 4β = 0`. The
normalized generator used here is the `α = 1` point of that line:

`Z_0 := Qi_+ − Qi_- = σ = diag(1,1,1,1,−1,−1,−1,−1)`.

Discriminating exact witnesses:

```text
tr(Y_0)=0, spec_multiset(Y_0) = {1,1,1,1,1,1,-3,-3}
tr(Z_0)=0, spec_multiset(Z_0) = {1,1,1,1,-1,-1,-1,-1}
4α+4β=0 ⇒ β=−α
σ^2=I, σ^*=σ
```

The four axiom sentences used as premises, quoted and not edited:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.
>
> No possibility is privileged. Possibilities are distinguished by the supplied
> algebraic structure alone.
>
> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.
>
> When present, a record locks exactly one admissible local possibility.
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

## Exact Target And Obligation Graph

**Exact target.** Recompute the May 2 identity for ranks `(6,2)`, exhibit
the involution `σ` of ranks `(4,4)` with ratio `−1`, and record that the
quoted axiom sentences do not select `Y_0` over `Z_0`.

| Obligation | Role | Disposition |
|---|---|---|
| pin May 2 `6α+2β=0 ⇒ β=−3α` and its SM non-claim | premise | quoted; recomputed; not claimed new |
| pin GRAPH_FIRST `(6,2)` multiplicities | premise | cited as the landed rank pair |
| pin the four axiom sentences | premise | quoted from the axiom memo |
| pin cycle 692 scale convention | premise | `α=1/3` is not derived |
| exhibit `σ` and ranks `(4,4)` | Theorem 2 | computed here |
| show the axiom sentences do not name the split | Theorem 3 | scoped residual |
| identify `Y_like` with `U(1)_Y` | non-claim | open; Theorem 5 |
| edit an axiom to name `τ` or `σ` | non-claim | not required |

## Theorem 1 — Ranks (6,2) Force β=−3α (Recompute Only)

**Claim.** `Pi_+` and `Pi_-` are complementary orthogonal projectors of
ranks `6` and `2`. Tracelessness of `Y(α,β)=α Pi_+ + β Pi_-` is
`6α+2β=0`, hence `β=−3α` whenever `α ≠ 0`. The generator `Y_0` has
spectrum `{+1 × 6, −3 × 2}` and trace `0`. This is the May 2 identity.
It is not claimed new.

**Proof.** Each diagonal entry of `Pi_+` is `0` or `1`, and
`Pi_+^2 = Pi_+`. The number of ones is `6`, so `rank(Pi_+)=6` and
`tr(Pi_+)=6`. The complementary matrix `Pi_- = I − Pi_+` is likewise a
projector of rank `2`. The product `Pi_+ Pi_-` is zero, so the pair is
orthogonal. Self-adjointness is immediate from the real diagonal.

On the six-dimensional plus sector `Y` acts by `α`. On the
two-dimensional minus sector it acts by `β`. The trace is therefore
`6α+2β`. Setting the trace to zero and dividing by `2` gives
`3α+β=0`, so `β=−3α`. The same ratio is recovered for every nonzero
sample `α` in `{1, 2, −5, 7/11}`: the solution line is one-dimensional.

Substituting `(α,β)=(1,−3)` produces `Y_0=Pi_+−3 Pi_-`, whose diagonal
is six ones followed by two copies of `−3`. The trace is
`6·1 + 2·(−3) = 0`. The eigenvalue multiset is
`{1,1,1,1,1,1,−3,−3}`.

May 2 already states this identity and already excludes identification
with Standard Model hypercharge `Y`. The present theorem only recomputes
the same linear algebra on the same rank pair.

## Theorem 2 — The Involution σ Has Ranks (4,4) And Ratio −1

**Claim.** `σ = diag(+1^4, −1^4)` is a self-adjoint involution.
`Qi_± = (I±σ)/2` are complementary orthogonal projectors of ranks
`(4,4)`. Tracelessness of `Z(α,β)=α Qi_+ + β Qi_-` is `4α+4β=0`, hence
`β=−α`. The generator `Z_0=Qi_+−Qi_-` has spectrum `{+1 × 4, −1 × 4}`
and is not a scalar multiple of `Y_0`.

**Proof.** Each diagonal entry of `σ` is `±1`, so `σ^2 = I`. The entries
are real, so `σ^* = σ`. The standard involution calculus then gives

`Qi_+ + Qi_- = I`, `Qi_+ Qi_- = 0`, `Qi_±^2 = Qi_±`, `Qi_±^* = Qi_±`.

The plus projector is `diag(1,1,1,1,0,0,0,0)` and the minus projector is
`diag(0,0,0,0,1,1,1,1)`. Each has four ones, so the ranks are `(4,4)`.

The trace of `Z(α,β)` is `4α+4β`. Setting the trace to zero and dividing
by `4` gives `α+β=0`, so `β=−α`. The same ratio is recovered for every
nonzero sample `α` in `{1, 2, −5, 7/11}`.

Substituting `(α,β)=(1,−1)` produces `Z_0=Qi_+−Qi_-`. That operator
equals `σ` itself. Its diagonal is four ones followed by four copies of
`−1`. The trace is `4−4=0`. The eigenvalue multiset is
`{1,1,1,1,−1,−1,−1,−1}`.

If `Y_0` were a scalar multiple of `Z_0`, there would exist `q` in `Q`
with `Y_0 = q Z_0`. Both operators are diagonal and `Z_0` has no zero
entries, so each ratio of corresponding eigenvalues would equal `q`.
Those ratios are

`1/1, 1/1, 1/1, 1/1, 1/(−1), 1/(−1), (−3)/(−1), (−3)/(−1)`,

which evaluate to `1,1,1,1,−1,−1,3,3` and are not constant. The
multisets `{1^6,(−3)^2}` and `{1^4,(−1)^4}` therefore distinguish the
two generators.

The mutation is the rank change. Replacing ranks `(6,2)` by `(4,4)`
replaces the traceless ratio `−n_+/n_-` from `−3` to `−1`.

## Theorem 3 — The Axiom Sentences Do Not Select Y_0 Over Z_0

**Claim.** Lattice, Qubit, Admissibility, and Record, as quoted above,
do not name `τ`, `SWAP_23`, a `C^8` taste cube, or the rank pair
`(6,2)` versus `(4,4)`. They do not select `Y_0` over `Z_0`.

**Proof.** Read each governing sentence against the named objects.

Lattice says that physical sites are the points of the cubic lattice
`Z^3`, with nearest-neighbor adjacency, translations, and proper cubic
rotations, and that no site is privileged. That sentence names a
spatial lattice. It does not name an eight-dimensional taste space, an
involution on that space, or a rank pair of projectors.

Qubit says that each site has a domain of local possibilities, that the
full one-site domain has algebraic presentation `M_2(C)`, and that no
possibility is privileged. A non-privileged `M_2(C)` does not name a
preferred involution on `C^8` and does not name `SWAP_23`.

Admissibility says that there is one fixed nearest-neighbor
admissibility rule, and that for each site the probability distribution
over the possibilities is determined by, and varies with, the
nearest-neighbor conditions. A nearest-neighbor distribution on `Z^3`
does not name a taste-cube swap and does not fix ranks `(6,2)`.

Record says that records form; that when present a record locks exactly
one admissible local possibility; that only records are readable; that
a readout value is determined by record content alone; and that for any
finite collection of pairwise-disjoint records, scalar readout `I` is
additive, with `I(empty)=0`. Additivity of a scalar on record
collections does not name a projector rank and does not equate `6α+2β`
with `4α+4β`.

The objects that do name the landed split sit outside those sentences.
GRAPH_FIRST supplies the `(6,2)` multiplicities from a residual
complementary-axis swap on a taste cube. May 2 consumes that rank pair.
`SWAP_23` is the involution used by the name-free parent to build
`P_sym` and `P_anti`. Those are extra selectors. They are not Lattice,
Qubit, Admissibility, or Record.

Because both `Y_0` and `Z_0` are well-defined traceless operators on the
same `C^8`, and because the axiom sentences do not mention either
involution, those sentences do not select one generator over the other.

## Theorem 4 — The Scale α=1/3 Is A Convention

**Claim.** The value `α=1/3` is a convention. It is not derived here.
The rescaling `Y_like = Y_0/3` is that convention and is not identified
with `U(1)_Y`.

**Proof.** Theorem 1 determines only the ratio `β/α`. The overall scale
remains a free nonzero rational. Cycle 692 already tested a finite menu
of scale-fixing mechanisms on the landed two-value surface and recorded
that the only tested condition selecting `1/3` is the stipulation that
the minus sector reads `−1`. That stipulation is a choice of unit, not
a consequence of tracelessness.

Dividing `Y_0` by `3` produces the diagonal
`{1/3,1/3,1/3,1/3,1/3,1/3,−1,−1}`. That is the conventional
normalization used by the May 23 left-handed abelian surface note. The
present note does not re-derive that scale and does not identify the
rescaled operator with physical hypercharge.

## Theorem 5 — Scoped Residual

**Claim.** `σ` is an extra involution. The quoted axiom sentences do
not select `Y_0` over `Z_0`. This note does not identify either
operator with anomaly-complete `U(1)_Y`, does not close P-HY, and does
not edit an axiom.

**Proof.** Theorems 1 and 2 compute two different traceless ratios from
two different rank pairs on the same `C^8`. The hypotheses that produce
those rank pairs — a choice of self-adjoint involution, equivalently a
choice of complementary projectors — are not Lattice, Qubit,
Admissibility, or Record. Theorem 3 reads those four sentences and finds
none of the named objects.

The attempted one-involution substitutes fail for independent reasons:

- forcing ranks `(6,2)` from the axiom memo fails because the memo
  never names a `C^8` involution;
- forcing the same ranks from Record additivity fails because `I` is a
  scalar on collections, not a projector rank;
- forcing the same ranks from Admissibility fails because a
  nearest-neighbor distribution does not name `τ` or `SWAP_23`;
- identifying `Z_0` with `Y_0` fails because the eigenvalue multisets
  differ;
- naming either operator as anomaly-complete `U(1)_Y` is P-HY, which
  remains open.

Declaring `σ` makes the `(4,4)` split well-defined. That declaration is
the extra object. It is not forced by the quoted axiom sentences. An
axiom edit that named `τ`, `σ`, or the rank pair `(6,2)` is not required
by the linear algebra of either split.

The residual is scoped. It does not say that a later physical selector
cannot prefer one involution, and it does not say that a later bridge
cannot identify a named generator with physical hypercharge.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- claim uniqueness of `β=−3α` as a new result (May 2 already has it);
- derive `α=1/3`;
- identify `Y_0`, `Z_0`, or `Y_like` with `U(1)_Y`;
- close P-HY, anomaly cancellation, or a charge formula
  `Q = T_3 + Y/2`;
- reopen two-plane uniqueness of a hypercharge-like generator;
- exhaust every self-adjoint involution on `C^8`.

The scope is the exact rank-to-ratio mutation from `(6,2)` to `(4,4)`,
together with the residual that the four axiom sentences do not select
`Y_0` over `Z_0`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice, Qubit, Admissibility, and Record sentences | premise | quoted; no edit |
| May 2 ratio `6α+2β=0 ⇒ β=−3α` and SM non-claim | scope pin | quoted; recomputed; not reversed |
| GRAPH_FIRST `(6,2)` multiplicities | landed rank pair | cited; not re-derived as new |
| name-free `Y_0 = P_sym − 3 P_anti` | landed generator | cited |
| cycle 692 scale convention | scope pin | `α=1/3` not derived |
| involution `σ` and generator `Z_0` | declared algebra | computed here |
| axiom non-selection of `Y_0` over `Z_0` | Theorem 3 | computed here |
| P-HY / anomaly-complete `U(1)_Y` | residual | live, not derived |

The exact advance is a finite rank-to-ratio mutation on `C^8`. Independent
audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | May 2 already forces `β=−3α` from ranks `(6,2)` and already excludes SM hypercharge identification. GRAPH_FIRST already supplies those ranks. The named residual is whether the four axiom sentences themselves select that rank pair and that ratio. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for involution rank-split, ranks `(4,4)` versus `(6,2)`, `σ=diag(+1^4,−1^4)`, `Qi_±`, and a `Z_0` generator on `C^8`. Hits: May 2 and the name-free parent ship the `(6,2)` identity `β=−3α`; May 23 constructs `Y_like` on the same `(6,2)` projectors; cycle 692 is scale freedom on that line; a CKM Brocard identity `β=−α` is a polynomial-coefficient alternative, not an involution on `C^8`. No landed theorem mutates the rank pair `(6,2)` to `(4,4)` and records the ratio change `−3 → −1`. Unmerged siblings are not premises. |
| V3 | Independently checkable? | Textbook spectral calculus of a self-adjoint involution produces complementary projectors and does not mention Record or `Y_0`. The runner builds both involutions as exact diagonal operators, recomputes ranks by counting ones, and solves the two trace equations in `Fraction`. |
| V4 | More than a restatement? | Yes. The witnesses `tr(Y_0)=0` with multiset `{1^6,(−3)^2}`, `tr(Z_0)=0` with multiset `{1^4,(−1)^4}`, and `4α+4β=0 ⇒ β=−α` are not restatements of the May 2 ratio sentence. |
| V5 | One-step relabel? | No. The May 2 identity is the algebra of one rank pair. A mutation to a second involution with a different rank pair is not a relabel of that identity. |

## No-Go Discipline Gate (Theorems 3–5 only)

The negative claim is restricted to this: the quoted Lattice, Qubit,
Admissibility, and Record sentences do not select `Y_0` over `Z_0`, the
scale `α=1/3` is not derived, and neither operator is anomaly-complete
`U(1)_Y`. The gate does not ship a global non-existence theorem against
a later physical selector, and it does not ship a hypercharge
identification.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| force `(6,2)` from the four axiom sentences | read Lattice, Qubit, Admissibility, and Record for a `C^8` involution or rank pair | Theorem 3: those sentences name `Z^3`, `M_2(C)`, a nearest-neighbor distribution, and an additive scalar `I` | **ATTEMPTED** |
| force `(6,2)` from Record additivity | set projector ranks equal to a Record readout | `I` is a scalar on finite collections; `I(empty)=0` does not name `rank(Pi_+)` | **ATTEMPTED** |
| force `(6,2)` from Admissibility | read the nearest-neighbor distribution as a taste-cube swap | Admissibility names a sitewise law on `Z^3`, not `τ` or `SWAP_23` | **ATTEMPTED** |
| identify `Z_0` with `Y_0` | declare the two generators equal or scalar-equivalent | Theorem 2: eigenvalue multisets `{1^6,(−3)^2}` and `{1^4,(−1)^4}` differ | **ATTEMPTED** |
| axiom edit naming `τ` or `(6,2)` | add an involution sentence to an axiom | not required by the linear algebra; see N6 | **ATTEMPTED** |
| P-HY naming | call `Y_0` or `Y_like` anomaly-complete `U(1)_Y` | Theorem 5: identification remains open | **ATTEMPTED** |

### N2 — wall independence

Theorem 5 closes only the claim that the quoted axiom sentences select
`Y_0`. It does not close the May 2 identity (Theorem 1, already landed),
the `(4,4)` mutation (Theorem 2), a later physical selector among
involutions, or P-HY. Those walls remain independent. Existence of two
traceless generators on `C^8` does not by itself make either generator
an axiom output.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| standard basis of `C^8` | declared working space |
| `Pi_±` of ranks `(6,2)` | landed objects, recomputed |
| involution `σ` and `Qi_±` | explicit construction |
| tracelessness `n_+ α + n_- β = 0` | explicit linear algebra |
| eigenvalue-multiset witnesses | explicit diagonals |
| four axiom sentences | quoted premises |
| axiom edit naming `τ` or `σ` | live governance path; not required |
| P-HY / `U(1)_Y` identification | open; not assumed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice `Z^3`; Qubit non-privilege; Admissibility nearest-neighbor distribution; Record lock and `I(empty)=0` | quoted as premises only; no edit |
| [`docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md) | `6α+2β=0 ⇒ β=−3α`; SM identification out of scope | recomputed only; not claimed new |
| [`docs/HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md) | `Y_0 = P_sym − 3 P_anti`; name-free two-value algebra | cited; not renamed as `U(1)_Y` |
| [`docs/PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md`](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md) | `α=1/3` not derived by the tested mechanisms | scale remains a convention |
| [`docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | `(6,2)` multiplicities on the doubled weak-fiber surface | cited as the landed rank pair |

No unmerged sibling is used as a parent. The `(4,4)` witnesses are
computed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | diagonals of `Y_0` and `Z_0` and the two trace equations | no classification of every involution on `C^8` |
| per site | one copy of `C^8`; no lattice site is assigned a taste cube | no spatial-lattice hypercharge field |
| per mode | two-value central operators, not spectral modes of a Hamiltonian | no harmonic-mode exhaustion |
| per split | ranks `(6,2)` versus `(4,4)` and the axiom residual | no `U(1)_Y` identification and no axiom edit |
| lattice-wide | checked and not executed | no lattice-wide electroweak statement |

The residual is an involution-selection gap. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that a physical selector on the taste cube prefers
   one self-adjoint involution and that the preferred rank pair is
   `(6,2)`.
2. A later selector that uses more than the four axiom sentences — for
   example a declared residual swap — to name `τ_Y` without editing an
   axiom.
3. A later dimensionless derivation of the unit choice `α=1/3`, which
   cycle 692 left open.
4. An owner-approved typed axiom addition that named an involution.
   The linear algebra of either split does not require that addition.

The quoted axiom sentences already name `Z^3` sites, a non-privileged
possibility domain, a nearest-neighbor distribution, a lock, and an
additive scalar `I`. They do not name `τ`, `σ`, or the rank pair. No
axiom sentence is required by Theorem 5.

### N7 — hostile steelman

> The axioms already pick the graph-first taste cube, so they pick `τ`
> and ranks `(6,2)`. Uniqueness of the traceless ratio on that split
> then means the axioms selected `Y_0`.

**Answer.** Uniqueness of `β=−3α` is conditional on the rank pair
`(6,2)`. That rank pair is supplied by GRAPH_FIRST and consumed by
May 2. Lattice names `Z^3` sites, not a `C^8` taste cube. Qubit names
`M_2(C)` with no privileged possibility, not a preferred involution.
Admissibility names a nearest-neighbor distribution. Record names a
lock and an additive scalar. Theorem 2 exhibits a second involution on
the same `C^8` whose traceless ratio is `−1`. Theorem 3 is exactly the
gap between “unique if ranks are `(6,2)`” and “selected by the axiom
sentences.”

### N8 — cross-cycle echo

May 2 already removed SM hypercharge identification from its
load-bearing claim and already recorded `β=−3α` for ranks `(6,2)`.
Cycle 692 already recorded that `α=1/3` is not derived by the tested
mechanisms. The name-free parent already wrote `Y_0` without a physical
species label. The present mutation does not reverse those non-claims.
It answers a different question: among self-adjoint involutions on
`C^8`, the traceless ratio tracks the rank pair; among axiom sentences,
that rank pair is still extra.

**Gate disposition.** PASS for the `(4,4)` rank-to-ratio mutation and
for the scoped residual that the axiom sentences do not select `Y_0`
over `Z_0`. FAIL / DO NOT SHIP for “`β=−3α` is new,” “`α=1/3` is
derived,” “`Y_like` is `U(1)_Y`,” or “an axiom edit is required.”

## Primary Runner

[`scripts/involution_rank_split_selects_traceless_ratio_axioms_do_not_2026_08_13.py`](../scripts/involution_rank_split_selects_traceless_ratio_axioms_do_not_2026_08_13.py)
rebuilds both involutions as exact diagonal operators, recomputes ranks
by counting ones, solves the two trace equations in `Fraction`, checks
that `Y_0` is not a scalar multiple of `Z_0`, and pins the May 2 ratio
sentence together with the Admissibility and Record sentences. Identity
gates call `ratio_from_ranks()` and `z0()`. Replacing ranks `(6,2)` by
`(4,4)` must change the ratio `−3` to `−1`. Replacing `Z_0` by `Y_0`
must fail the eigenvalue-multiset witness. A constant ratio `−3` must
fail on ranks `(4,4)`.
