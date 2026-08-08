---
claim_id: common_frame_pair_generator_exchange_class_bounded_theorem_note_2026-07-25
claim_type: bounded_theorem
claim_scope: "Under four SUPPLIED hypotheses -- (H1) one M_2(C) site domain on the Z^3 nearest-neighbour graph; (H2) an autonomous time-independent self-adjoint pair generator; (H3) a sum of identical two-site terms; (H4) COMMON-frame SU(2) covariance, one and the same U acting on both sites of an edge -- the commutant of the diagonal frame action on two qubits has complex dimension exactly 2 and equals span{I, SWAP}, so every admissible pair generator is h = a I + b SWAP with a, b real. The licensed quotient (h, t) -> (alpha h + beta I, t/alpha) with alpha > 0 removes a and |b| and leaves exactly sign(b), and the separating invariant is the GROUND-SECTOR DEGENERACY: 1 for b > 0 (the singlet) and 3 for b < 0 (the triplet). RECORDED EXPLICITLY AS A NEGATIVE RESULT: the one-excitation band minimum is NOT a valid separator, because Z^3 nearest-neighbour adjacency is bipartite by the parity of x + y + z, the sublattice relabeling D = diag((-1)^parity) gives D A D = -A, hence spec(A) = -spec(A), and the +J and -J one-excitation bands are identical as multisets after the licensed energy shift; the separator works only on a non-bipartite graph such as the triangle, and Z^3 is not one. THREE LIMITATIONS ARE PART OF THE CLAIM, NOT CAVEATS TO IT. (L1) H4 is a PREMISE THAT CREATES the two-point menu: under INDEPENDENT onsite covariance the commutant is only the scalars, SWAP is not invariant, and no nontrivial pair law survives without a further supplied object (a connection, link variable, shared frame, or symmetry reduction). (L2) 'Exactly two' holds only for the two-site edge class under the supplied identical-pair-term ansatz H3: at three sites H_1 = SWAP_01 + SWAP_02 and H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01 satisfy the same Hermiticity, neighbour-exchange, and common-frame covariance hypotheses, and H_1 + eta H_2 carries a dimensionless eta moving the gap ratio (E1-E0)/(E2-E1) from 2 at eta = 0 to 1 at eta = 1/3, which a gap RATIO argument shows is removable by neither clock rescaling nor energy shift. (L3) The 'inert' identity shift is NOT inert on a record-conditioned active-edge set: on a supplied convention where an edge is active when neither endpoint carries a record, two record sectors with different active-edge counts acquire a relative phase that moves an interference term on a coherent superposition of those sectors, so the energy shift may not be discarded before the domain is fixed. NOT claimed: any selection of sign(b), of |b|, of a rate, or of a time unit; derivability of H2-H4 from Lattice/Qubit/Admissibility/Record; PAIRWISE INDEPENDENCE OF H1-H4 (none is claimed and none is audited here); a well-defined discrete update on overlapping edges; a strict light cone; any record formation rule, formation trigger, instrument, Born weight, sampling rule, actuality, or realized outcome; the general reversible-record obstruction; continuity of a disagreement minimizer; and any relativistic, chiral, fermionic, gauge, species, matter, clock-metric, or gravitational consequence. This note sets no audit verdict and asserts no PASS."
upstream_dependencies:
  - minimal_axioms
runner: scripts/common_frame_pair_generator_exchange_class_2026_07_25.py
---

# Common-Frame Pair Generator: The Exchange Class And Its Three Limitations

**Date:** 2026-07-25
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** two qubits on one edge of the `Z^3` nearest-neighbour graph under
four supplied hypotheses; the axioms supply no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/common_frame_pair_generator_exchange_class_2026_07_25.py`](../scripts/common_frame_pair_generator_exchange_class_2026_07_25.py)
**Runner cache:**
[`logs/runner-cache/common_frame_pair_generator_exchange_class_2026_07_25.txt`](../logs/runner-cache/common_frame_pair_generator_exchange_class_2026_07_25.txt)

**Upstream authority:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

## Purpose

A symmetry classification that reduces an arbitrary Hermitian two-site
generator to one physical coefficient has been recomputed more than once in
this repository without ever becoming citable. This note states it once, with
its limitations attached rather than dropped, and gates every constant in a
single runner.

The classification is genuinely useful: an arbitrary Hermitian operator on
`C^2 ⊗ C^2` carries 16 real parameters, and under the stated hypotheses it
collapses to two, then to one after the licensed quotient. The limitations are
equally load-bearing, and they are the part that a summary tends to lose: the
covariance reading is what *creates* the two-point menu rather than a
notational convenience; the count does not survive enlarging the support past
one edge; and the identity term is inert only on a fixed active-edge set.

This note claims a **classification**, not a law. It selects no sign, no rate,
no formation rule, no instrument, and no actual history.

**Prior exploratory surfaces.** Four working notes dated 2026-07-14 under
`docs/work_history/repo/review_feedback/` explore this route:
`QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md`,
`RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md`,
`SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md`, and
`FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md`. They are named
here as **route inputs only** and are deliberately referenced in backticks
rather than as markdown links: they each carry `Authority: none`, they are not
consumed as evidence anywhere below, and nothing in this note inherits status
from them. Every algebraic step is recomputed natively in this note's runner,
which reads none of those files. Their runners are **not** reused, for reasons
stated under Verification.

## Hypotheses (all supplied; none derived)

The Qualification in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) requires a
retained derivation, bridge, or registered primitive before any of these could
be treated as framework content, and none of them has one. That memo states
that Admissibility "is not a dynamics axiom" and that it "does not choose a
Hamiltonian or transfer operator", so H2–H4 cannot be read off the axioms; it
also lists "source/action and physical-observable identification" among the
open gates outside axiom content, and H2–H4 sit on that gate.

- **(H1) Domain.** One `M_2(C)` possibility domain per site on the cubic `Z^3`
  nearest-neighbour graph. *This much is axiom content.*
- **(H2) Autonomous generator.** Between-record evolution is generated by a
  time-independent self-adjoint operator. Time-independence is essential and is
  not implied by strong continuity: the covariant family `h(t) = J(t) SWAP` is
  pointwise covariant and retains an arbitrary coefficient function.
- **(H3) Identical two-site terms.** The generator is a sum of identical
  nearest-neighbour two-site terms. This is an **ansatz**, and L2 below is
  precisely the cost of it.
- **(H4) COMMON-frame covariance.** One and the same `U ∈ SU(2)` acts on both
  sites of an edge. This is the decisive premise; see L1.

**No pairwise independence of H1–H4 is claimed**, and the runner attempts no
independence audit of them. They are stated as a conjunction and consumed as a
conjunction.

## Results

**R1 (classification).** Under H1 and H4 the commutant of the diagonal action
`U ⊗ U` on `C^2 ⊗ C^2` has complex dimension exactly 2 and equals
`span{I, SWAP}`. Hence under H1–H4 every admissible pair generator is

```text
h = a I + b SWAP
  = (a + b/2) I + (b/2)(X⊗X + Y⊗Y + Z⊗Z),
```

with `a, b` real. The exchange identity `SWAP = (I + X⊗X + Y⊗Y + Z⊗Z)/2` is
exact. Gates `G1a`–`G1g`; the containment is checked in **both** directions and
paired with a negative control (`X⊗I` is not in the commutant), so the
equality is not read off a dimension count alone.

**R2 (quotient).** On a **fixed** active-edge set, the map
`(h, t) ↦ (α h + β I, t/α)` with `α > 0` leaves the generated channel unchanged
up to a global phase. Taking `α = 1/|b|` and `β = −α a` carries `h` to
`sign(b)·SWAP`, so `a` and `|b|` are removed. The sign is **not** removed: the
two-parameter system `α SWAP + β I = −SWAP` has the unique solution
`(α, β) = (−1, 0)`, which is not licensed. Positivity of `α` is exactly what
makes the sign physical — dropping it identifies the two signs. Gates
`G3a`–`G3f`, with the mutation probe `G3f` supplying the identification that
the constraint blocks.

**R3 (the separator).** The relabeling-proof invariant separating the two signs
is the **ground-sector degeneracy**. `SWAP` has spectrum `{+1 (×3), −1 (×1)}`,
so for `h = a I + b SWAP`:

- `b > 0` has a **one-dimensional** ground sector (the singlet);
- `b < 0` has a **three-dimensional** ground sector (the triplet).

The degeneracy of the lowest eigenvalue is invariant under every `α > 0`
rescaling, every `β I` shift, and every common frame change, so it survives the
whole licensed quotient of R2. Gates `G4a`–`G4f`. `G4f` records the reason a
weaker invariant will not do: `+SWAP` and `−SWAP` have the **same eigenvalue
set** `{±1}` and differ only in the multiplicities, so a set-valued spectral
invariant cannot separate them.

**R4 (the band minimum is NOT a separator — recorded explicitly).** The
one-excitation band minimum must **not** be used in place of R3. `Z^3`
nearest-neighbour adjacency is bipartite by the parity of `x + y + z`. Let `D`
be the diagonal sublattice relabeling `D_xx = (−1)^{parity(x)}`. Then for the
adjacency matrix `A`

```text
D² = I,    D A D = −A,    hence  spec(A) = −spec(A).
```

In the one-excitation sector the exchange sum restricts to `A + (|E|·I − Deg)`,
which on a regular graph is `A` plus a constant; `Z^3` is 6-regular, so after
the R2 energy shift the `+J` and `−J` one-excitation bands are **identical as
multisets**. The band minimum, the band width, and the whole band shape are
therefore sign-blind on `Z^3` and separate nothing. The separator works only on
a **non**-bipartite graph — the triangle has `spec(A) = {2, −1, −1}`, no
diagonal `±1` relabeling reverses it, and its shifted `+J` and `−J` bands do
differ — and `Z^3` is not one. Gates `G5a`–`G5h`: the one-excitation block is
**assembled by applying the actual edge permutations**, not asserted from a
formula, and is verified against the full `2^n` space on two instances;
`D A D = −A` is checked on the `L = 4` periodic `Z^3` chunk (64 sites, 192
edges) as well as on `C4`, `Q3`, `K_{3,3}`, and `P3`; the triangle is the
breaking mutation. `G5h` adds the independent point that the band minimum is
not even invariant under the `β I` shift, whereas the ground-sector degeneracy
does not move at all.

## Limitations (all three are part of the claim, not caveats to it)

**L1 — common-frame covariance is a PREMISE that CREATES the two-point menu.**
H4 is not a notational convenience; it is the physics. Under **independent**
onsite covariance — separate `SU(2)` actions on the two sites — the commutant
collapses to complex dimension **1**, the scalars alone; `SWAP` is not
invariant there. Solving directly, `a I + b SWAP` is independent-onsite
invariant only for `b = 0`. So under independent onsite covariance **no
nontrivial pair interaction survives at all** without a further supplied
object: a connection, a link variable, a shared frame, or a symmetry reduction.
The axiom sentence "No possibility is privileged" does not choose between the
two readings. Adopting the exchange class therefore imports a physical premise;
it does not read one off a symmetry slogan. Gates `G2a`–`G2d`.

**L2 — "exactly two parameters" holds only for the two-site edge class under
the supplied identical-pair-term ansatz.** The count is a statement about one
edge under H3, and it does not survive enlarging the support. On three sites
with a centre and two equivalent neighbours, both

```text
H_1 = SWAP_01 + SWAP_02,
H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01
```

are Hermitian, invariant under exchanging the two equivalent neighbours, and
invariant under the common-frame diagonal `SU(2)` — they satisfy exactly the
same symmetry hypotheses. `I`, `H_1`, `H_2` are linearly independent, so the
family `H_η = H_1 + η H_2` carries a genuinely independent **dimensionless**
coefficient `η`, and it moves a spectral gap ratio

```text
(E_1 − E_0)/(E_2 − E_1) = 2   at η = 0,
                        = 1   at η = 1/3.
```

A gap **ratio** is invariant under both `α > 0` rescaling and `β I` shift, so
neither clock rescaling nor an energy-zero choice removes `η`. Symmetry
licenses the term; it does not fix it. Gates `G6a`–`G6j`. The common-frame
covariance of `H_1` and `H_2` is **computed** here (`G6c`, `G6d`) — that is the
property which makes `η` an independent invariant and therefore makes the
counterexample bite — and `G6e` supplies the negative control (`Z_0 Z_1` is
Hermitian but fails both symmetry checks) so the covariance gate is not a
tautology.

**L3 — the "inert" identity term is NOT inert on a record-conditioned
active-edge set.** R2's removal of `a` is conditional on a **fixed** active-edge
set. Supply the convention that an edge is active when neither endpoint carries
a record. Two record sectors then differ in their active-edge count, adding
`β I` per active edge contributes `β N_active`, and that is not a common scalar
across sectors of different `N_active`. On a coherent superposition of two such
sectors the relative phase moves an interference term, which is therefore not a
removable global phase. The active-edge convention is itself **supplied** — the
axioms give no formation rule — so L3 is a conditional: *if* record formation
changes which edges are active, the energy shift may not be discarded before
the domain is fixed, and a record-dependent active graph needs an explicit
vacuum/edge energy convention or a superselection argument. Gates `G7a`–`G7e`,
with `G7d` mutating the record configuration to equal active-edge counts (the
term becomes inert again) and `G7e` confirming that R2 holds exactly on a fixed
set, so L3 is a boundary rather than a contradiction.

## Non-Claims

This note does **not** claim, and its runner does not gate:

- any selection of `sign(b)`, of `|b|`, of a rate, or of a time unit;
- that H2–H4 are derivable from Lattice/Qubit/Admissibility/Record — the axiom
  memo says the opposite for dynamics;
- pairwise independence of H1–H4;
- a well-defined discrete update: on overlapping edges the pair terms do not
  commute, so a product update still needs an ordering/layering rule or a
  causal-invariance theorem;
- a strict light cone. A finite-range continuous generator gives a quasilocal
  cone with tails, not the exact cone of a layered circuit; the two have
  different exact causal semantics and one must be chosen and its continuum
  interpretation proved separately;
- any record formation, formation trigger, instrument, Born weight, sampling
  rule, actuality, or single realized outcome. Entanglement **capability** is
  not sampling and supplies no outcome;
- the general reversible-record obstruction (that `R ≤ U†RU` forces equality by
  equal trace and rank). It is left to its exploratory source and is **not**
  gated here;
- continuity of any disagreement minimizer over all rank-one projectors;
- any relativistic, chiral, fermionic, gauge, species, matter, clock-metric, or
  gravitational consequence. A cubic exchange system has a parity-even
  quadratic magnon dispersion, not a Weyl sector;
- any audit verdict. Independent audit remains required.

## No-Go Discipline Gate

The licensed negative content is bounded to L1–L3 and R4:

> Under H1–H4 the two-site pair generator class is exactly `span{I, SWAP}` and
> the licensed quotient leaves exactly `sign(b)`. Under independent onsite
> covariance no nontrivial pair term survives. The two-parameter count does not
> extend past the two-site edge class under H3. The identity term is not inert
> on a record-conditioned active-edge set. The one-excitation band minimum is
> not a valid sign separator on the bipartite `Z^3` graph.

No universal no-go against a pair law, an exchange dynamics, or a deeper
theorem deriving H2–H4 is made.

**Status: the items below were ATTEMPTED and are recorded for the audit lane.
No closure is claimed and no `PASS` is asserted. Judgement belongs to the
independent audit lane.**

- **N1 alternative-route enumeration — ATTEMPTED.**

  | route | strongest attempted form | outcome |
  |---|---|---|
  | common-frame `SU(2)` covariance | commutant of `U ⊗ U` | dimension 2, `span{I, SWAP}` — the stated class |
  | independent onsite covariance | commutant of separate `SU(2)` actions | dimension 1, scalars only — L1 |
  | enlarge support to three sites | `H_1 + η H_2` under the same symmetries | independent dimensionless `η` survives — L2 |
  | remove `a` by energy shift | `β I` on a fixed active-edge set | succeeds on a fixed graph, fails on a record-conditioned graph — L3 |
  | remove `sign(b)` by rescaling | `α > 0` clock rescaling | fails; only an unlicensed `α < 0` identifies the signs |
  | separate signs by band minimum | one-excitation dispersion | **fails on `Z^3`** by the bipartite relabeling — R4 |
  | separate signs by ground sector | lowest-eigenvalue degeneracy | succeeds, 1 vs 3 — R3 |
  | drop autonomy | strongly continuous covariant `h(t) = J(t) SWAP` | an arbitrary coefficient function returns; H2 is load-bearing |
  | discrete layered update instead of a generator | product of overlapping pair terms | ordering/layering rule required; not supplied |

- **N2 wall separation — ATTEMPTED.** Finite controls that keep one wall from
  being silently renamed as another: covariance reading vs class size (common
  frame gives dimension 2, independent onsite gives dimension 1); class size vs
  support (dimension 2 on one edge, `η` appears at three sites); scale freedom
  vs sign (`α > 0` removes `|b|`, never `sign(b)`); energy zero vs sector
  (`β I` is inert at fixed `N_active`, not across `N_active ∈ {1,2}`); spectrum
  vs degeneracy (`+SWAP` and `−SWAP` share the eigenvalue set `{±1}`; only the
  multiplicities differ); band minimum vs ground sector (the bipartite
  relabeling moves the band, not the ground degeneracy). A later theorem may
  tie several rows together. **These controls are not an independence proof,
  and no claim is made that H1–H4 are pairwise independent.**
- **N3 hidden-wall scan — ATTEMPTED.** Exposed rather than hidden: the
  common-versus-independent frame reading; autonomy/time-independence; the
  identical-pair-term ansatz; the two-site support restriction; the
  fixed-versus-record-conditioned active-edge set and the supplied
  active-edge convention itself; the sign of `b`; the magnitude `|b|` and its
  time unit; the dimensionless interaction angle; overlapping-edge ordering;
  continuous-versus-circuit causal semantics; the absence of any formation
  trigger, instrument, weight, or realized member; and the absence of any
  matter, chirality, clock-metric, or gravity content. Also exposed: the
  ground-sector invariant reads the `(3,1)` multiplicity split, and it is
  `G1` — not `G4` — that pins the operator carrying that split to be `SWAP`.
- **N4 dependency roles, per citation — ATTEMPTED.**
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): the H1
    domain sentence, and the no-dynamics boundary that makes H2–H4 supplied
    rather than derived. Nothing else is consumed; the memo is not modified.
  - The four 2026-07-14 exploratory surfaces named in Purpose: **route inputs
    only**, referenced in backticks so they seed no citation-graph edge. They
    carry `Authority: none`, they are not modified, and no result below rests
    on them. Every step is recomputed natively.
- **N5 resolution and rhetoric audit — ATTEMPTED.**
  - "Commutant is `span{I, SWAP}`" is a statement about a **two-qubit pair
    generator under common-frame covariance**, not about a general qubit
    automaton.
  - "Exactly two" means two real parameters `a, b` on **one edge under H3**,
    and L2 states where that stops.
  - "Inert identity" is true only on a **fixed** active-edge set (L3).
  - "Ground sector" means the lowest-eigenvalue eigenspace and its
    **dimension**, not the eigenvalue.
  - "Band minimum is not invariant" is a positive computation (R4), not a
    rhetorical hedge.
  - Entanglement **capability** is not sampling, an outcome, or a record, and
    no entanglement claim is gated here at all.
- **N6 partial-closure path — ATTEMPTED.** (1) Test whether the common-frame
  reading is forced by, or merely compatible with, the Admissibility covariance
  sentence. (2) Classify the full low-support invariant term basis past one
  edge, so the L2 `η` family is enumerated rather than exhibited. (3) Search for
  a conservation or index theorem fixing `sign(b)` rather than registering it.
  (4) Fix the active-edge/vacuum energy convention, or prove the superselection
  that makes L3 vacuous. (5) Only then ask whether the generator compiles into
  a homogeneous nearest-neighbour update on `Z^3`.
- **N7 strongest steelman — ATTEMPTED.** The strongest opponent is a theorem
  deriving H2–H4 from the exact admissibility law, so that the pair class
  becomes theorem content rather than an ansatz, simultaneously fixing
  `sign(b)` by a conservation or index argument and supplying the active-edge
  convention that retires L3. Such a theorem would convert most of this note
  into a corollary and would defeat its bounded framing. Nothing here excludes
  it; it is not constructed.
- **N8 cross-cycle echo — ATTEMPTED.** The commutant computation appears in
  prior exploratory runners by two different methods and agrees. What is new
  here relative to those surfaces: (i) the sign quotient is gated by
  construction rather than by a vacuous literal; (ii) the common-frame
  covariance of the three-site `H_1`, `H_2` is actually computed, which is what
  makes `η` an independent invariant; (iii) the active-edge non-inertness is
  built from a record-conditioned sector pair rather than a hand-written
  diagonal; and (iv) R4 is new — the band-minimum separator is positively
  refuted on the bipartite `Z^3` graph and the ground-sector degeneracy is put
  in its place.

## Verification

Primary runner:
[`scripts/common_frame_pair_generator_exchange_class_2026_07_25.py`](../scripts/common_frame_pair_generator_exchange_class_2026_07_25.py)

```bash
python3 scripts/common_frame_pair_generator_exchange_class_2026_07_25.py
```

Result on this note's content: **`PASS=46`, `FAIL=0`** (about 0.7 s). The PASS
total is a **gate count**, not a count of independent scientific facts.

**Why a new runner rather than the four existing ones.** The 2026-07-14
runners cannot serve this note: three of its load-bearing constants are
ungated there. The `sign(b)` quotient is "gated" only by the vacuous literal
`{-1, 1} == {sign(v) for v in (-3, 5)}`, which never touches `a`, `b`, `α`,
`β`, or `SWAP`; the common-frame covariance of `H_1` and `H_2` is asserted but
only Hermiticity and mutual commutation are checked; the active-edge phase is a
hand-built `sp.diag(1, 2)` with no record-conditioned edge set constructed; one
pair of their gates is the same check under two labels; and about 34% of one
runner's PASS lines are prose-needle greps on its own text. R4 exists in none
of them. Those four surfaces and their runners are left untouched.

**Design rules this runner honours.**

- Exact `sympy` throughout: no float is an input to any load-bearing
  comparison, no numeric tolerance is used, and eigenvalue ordering goes
  through an exact three-way comparison that refuses anything it cannot decide
  symbolically.
- **No prose-needle gates.** The runner reads no markdown and greps no text,
  including its own, so the PASS total is entirely mathematical. No gate is
  self-referential, and none is vacuous: each has a negative control or a
  mutation partner that makes it fail.
- **An ordered label manifest with a drift detector.** `EXPECTED_LABELS` fixes
  the gate sequence; renaming, reordering, adding, or dropping a gate fails the
  run.
- **A construction-mutation probe for every claimed constant.** Probes rebuild
  the object from a changed construction — they do not flip an assertion.
  `G1e` (a non-invariant candidate must leave the commutant), `G2a` (swap the
  covariance construction; the dimension must fall to 1), `G3f` (drop the
  positivity constraint; the two signs must become identified), `G4c` (flip the
  sign in the construction; the ground degeneracy must move 1 → 3), `G5g`
  (swap the bipartite graph for a triangle; sign-symmetry must break and the
  bands must differ), `G6e` and `G6i` (a non-covariant decoy must fail the
  symmetry gates; sweeping `η` must move the ratio), `G7d` (rebuild the record
  configuration with equal active-edge counts; the identity term must become
  inert).

Selected gate lines, verbatim:

```text
PASS G1a common-frame (diagonal SU(2)) commutant has complex dimension 2 :: dim=2
PASS G1e MUTATION non-invariant candidate X(x)I is NOT in the commutant (so G1d is not a tautology) :: rank=3
PASS G2a MUTATION independent-onsite covariance collapses the commutant to complex dimension 1 :: dim=1
PASS G3e NO positive rescaling plus energy shift maps +SWAP to -SWAP: the only solution has alpha = -1 :: solutions=[{alpha: -1, beta: 0}] positive=[]
PASS G4b b > 0: ground sector of a*I + b*SWAP is 1-dimensional (the singlet) :: deg=1
PASS G4c MUTATION flip the sign IN THE CONSTRUCTION: the ground sector becomes 3-dimensional (the triplet) :: deg=3
PASS G5c Z^3 nearest-neighbour adjacency is bipartite: x + y + z parity is a proper 2-colouring of every edge (L = 4 chunk, 192 edges) :: edges=192 sites=64
PASS G5e hence spec(A) = -spec(A) as multisets: A is similar to -A through D, so the band is sign-symmetric :: C4:[-2, 0, 0, 2]; Q3:[-3, -1, -1, -1, 1, 1, 1, 3]; K3,3:[-3, 0, 0, 0, 0, 3]; P3:[-sqrt(2), 0, sqrt(2)]
PASS G5g MUTATION swap the bipartite graph for the non-bipartite triangle ... :: spec=[-1, -1, 2] +J band=[-1, -1, 2] -J band=[-2, 1, 1]
PASS G6c both COMMUTE with all three diagonal SU(2) generators, i.e. both are common-frame covariant -- the check the source runners asserted but never computed
PASS G6g gap ratio (E1 - E0)/(E2 - E1) = 2 at eta = 0 :: levels=[-1, 1, 2] ratio=2
PASS G6h gap ratio = 1 at eta = 1/3 :: levels=[-4/3, 2/3, 8/3] ratio=1
PASS G7c on a coherent superposition of the two record sectors the identity term MOVES the interference term ... :: witness 1 -> 1/2
PASS G7d MUTATION ... EQUAL active-edge counts: the same identity term becomes a genuine global phase ... :: N_active=1 vs 1, witness 1 -> 1
```

**Gate coverage, stated plainly.** `G1`/`G2` are the classification and its
covariance contrast; `G3` is the quotient; `G4` is the invariant; `G5` is the
negative result R4 and is the only group that touches graph structure; `G6` is
the three-site counterexample defeating completeness; `G7` is the
record-conditioned active-edge boundary. **No gate composes R1–R3 with a
formation rule, an instrument, a weight, or a realized outcome — nothing in
this runner touches those, and nothing above claims them.**

No axiom, primitive, registry, ledger, queue, or generated audit surface is
edited by this note or its runner.
