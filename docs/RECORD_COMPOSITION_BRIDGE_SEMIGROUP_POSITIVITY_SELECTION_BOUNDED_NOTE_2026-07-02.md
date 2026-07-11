---
claim_id: record_composition_bridge_semigroup_positivity_selection_bounded_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "Bounded-support witness: under the named unadopted premises C-add, POS, and LOC, three named Z_N candidate objects separate exactly: the spectral exact-Q-gen semigroup is in-class but fails positivity, the spatial wrap is positive but not convolution-closed, and nearest-neighbor heat is a finite-N in-class/POS/LOC witness. This does not prove global uniqueness, adopt premises, select an SU(3) action, or close/retire any wall."
upstream_dependencies:
  - minimal_axioms
  - action_form_no_go_equivalence_premise_continuum_removal_scoped_relocation_note_2026-06-08
runner: scripts/frontier_record_composition_bridge_positivity_2026_07_02.py
---

# Record-Composition Bridge: C-add/POS/LOC Separate Named Semigroup Candidates; Nearest-Neighbor Heat Is the Finite-N Witness (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit-status authority:** independent audit lane only. This note does **not** set or
predict any audit outcome; it records a decomposition and a set of exact facts.
**Actual current surface status:** the action-selection question remains the *well-posed
open physical question* of the parent relocation note; nothing here closes it. The
non-axiom premises it isolates (C-add, POS, LOC) are **not adopted**.
**Primary runner:**
[`scripts/frontier_record_composition_bridge_positivity_2026_07_02.py`](../scripts/frontier_record_composition_bridge_positivity_2026_07_02.py)
**Cached runner output:**
[`logs/runner-cache/frontier_record_composition_bridge_positivity_2026_07_02.txt`](../logs/runner-cache/frontier_record_composition_bridge_positivity_2026_07_02.txt)

## Firewall

- **Three named premises carry all non-axiom weight; NONE is adopted.** **C-add**
  (dynamics-**family**): a one-step process composes so the two-step class-weight kernel
  is the *convolution* of the one-step kernels — tri-partitioned into (i) disjoint-union
  growth, (ii) class-surface `(a+b) mod N` addition, (iii) kernel convolution, all inside
  this one premise, none axiom-supplied (check 03). **POS** (branch): entrywise-
  nonnegative weights — the memo **withholds** weights, signed weights a live branch.
  **LOC** (branch): single-step nearest-neighbor structure (**review-pending** PR #4825).
- **The named-candidate separation has a genuine finite-N witness.** Composition + POS
  + LOC leave, among the named candidate objects tested here, the **nearest-neighbor
  heat** family `L_NN=circulant(-2,1,0,0,1)` — off-diagonals literally `1` (Metzler),
  a convolution semigroup, single-step local. Its
  **un-taken** `a→0` limit is the heat-kernel / wrapped Gaussian; that label belongs to
  the **un-taken** limit, not the finite-N object (no continuum-limit equivalence
  on-baseline).
- **No action is adopted or adjudicated** (Wilson, HK, Manton, exact-Q-gen). The
  separation is **candidate-level** among *named* candidates; a hostile *unnamed*
  positive local convolution-semigroup member is **not** generically excluded.
- **Scope honesty.** The exact facts live on abelian `Z_N` toy surfaces; the parent
  wall is **SU(3)**. The toys witness the **premise structure** (composition /
  positivity / locality), **not** the SU(3) selection itself.
- **The parent relocation note is unaudited; its caveat is inherited.** All campaign
  citations are **review-pending**; siblings are cited by number, **not read or
  matched** — every recomputation here is self-contained.
- **Nothing here edits axioms, policy, primitives, or registries; this note sets no
  audit status.** The independent audit lane owns all statuses.

## Purpose

The parent relocation note (2026-06-08) converted action-selection from a foreclosed
no-go into a *well-posed open physical question* on the physical-lattice baseline. This
note **decomposes** that question into exact floats-free arithmetic facts plus **three
named premises** — C-add, POS, LOC — carrying the remaining dynamics, positivity, and
locality weight, then **maps** C-add's candidate homes without taking them. The earlier
draft's single-premise framing is corrected: this carries a genuine finite-N witness
(the nearest-neighbor heat family) inside the named candidate list, not a one-premise
reduction and not a global uniqueness theorem.

## Supplied Surface `[checks 1-4]`

From `docs/MINIMAL_AXIOMS_2026-06-29.md`:

- Objects: *"A state is a configuration of records."*
- Readout additivity (the axiom-supplied half of C-add): *"For any finite
  collection of pairwise-disjoint records, scalar readout `I` is additive, with
  `I(empty)=0`."*
- The dynamics disclaimer (why C-add's kernel half is **not** supplied): Admissibility
  *"does not choose a Hamiltonian or transfer operator, supply transition
  probabilities or weights, select a scalar or nonzero kinetic branch, assert a
  Dirac-square carrier, define a time metric, or provide a record-production
  process or physical persistence dynamics."*
- Law shape: *"A law privileges no states. Its domain is a supplied condition, and
  at every state where the condition holds it gives exactly one answer."*

The runner guards each sentence (whitespace-normalized) against drift.

## Composition Premise C-add `[checks 5-9]`

**Definition.** *C-add:* two admissible steps compose by (i) **disjoint union** of the
new records, (ii) **class-surface addition** — the `(a+b) mod N` identification — and
(iii) the two-step **class-weight kernel is the convolution** of the one-step kernels.
Vocabulary is **weight-matrix** throughout: `W[a][b]` is a weight matrix (not a "joint
law"), its **row/column sums** are the one-step weights (not "marginals"), the
**class-weight vector** collects weight over `(a+b) mod N` (not a "distribution"). The
toy is an **external independence model** and is **normalization-independent**.

*"A state is a configuration of records"* supplies the objects, and Record additivity
makes the **readout** additive over the disjoint union (check 05). Clause (iii) is
process content: the axioms do not *"provide a record-production process"*, so it is not
an axiom consequence. **Exact `Z_3` toy:** with `p=(1/2,1/4,1/4)`, the independent matrix
`W[a][b]=p_a p_b` has two-step class-weight vector `p * p` (check 06); a correlated matrix
(second increment = first) has **identical one-step row and column sums** (check 07) and
**also satisfies readout additivity** — computed, not asserted, on every supported cell
(check 08) — yet its class-weight vector `≠ p * p`, including for unnormalized weights
(check 09). Additivity plus one-step sums do **not** force convolution; clause (iii) is
genuine, extra content. **C-add is named, not adopted.**

## Semigroup Class Boundary `[checks 10-12]`

The spectral wrapped-Gaussian family `c_n=q^(bal(n)^2)` is convolution-closed: the
runner convolves its **position-space** kernels exactly in `Q[sqrt(5)]`,
`K_{1/2} * K_{1/3} = K_{1/6}` (check 10). The Fourier multiplicativity
`c_n(t+s)=c_n(t)c_n(s)` is the *same* fact as `q^a r^a=(qr)^a` — a **consistency
identity that cannot fail by construction** (the exponential law), recorded honestly,
not as independent evidence (check 11). But C-add selects the **class, not a member**:
an off-family symbol `c=(1,1/2,1/2,1/2,1/2)` is a genuine convolution-semigroup symbol
— its self-convolution kernel, built by an actual position-space convolution, carries
symbol `c^2` — yet `c_2=1/2 ≠ c_1^4=1/16`, off the `q^(n^2)` curve (check 12). The class
is strictly larger than that curve (**review-pending** PRs #4819/#4824);
Wilson/Manton exclusion is stated, not re-derived.

## Named Candidate Separation `[checks 13-26]`

All legs are exact in `Q[sqrt(5)]`, with `cos(2π/5)=(sqrt(5)-1)/4`,
`cos(4π/5)=-(sqrt(5)+1)/4`. Sanity: `4c^2+2c-1=0` for `c=cos(2π/5)` (check 13);
`2cos(2π/5)+2cos(4π/5)=-1` (check 14); `sum_{n} cos(2πn/5)=0` (check 15). The earlier
draft used "wrapped Gaussian" for **two** different `Z_5` objects, separated here.

**(a) Spectral / exact-Q-gen — in-class, fails positivity `[checks 16-19]`.** The
spectral family `c_n=q^(bal(n)^2)` is identically `exp(tL)` for the balanced quadratic
generator (eigenvalues `{0,-1,-4,-4,-1}`): it **is** the exact-Q-gen semigroup member.
Its generator is not Metzler — `L_{0,1}=1/2+(3/10)sqrt5>0` (check 16) but
`L_{0,2}=(5-3sqrt5)/10<0` strictly (check 17). And its **kernel really goes negative**:
from `K(j)=(1/5) sum_n q^(bal(n)^2) cos(2πnj/5)`, at `q=9/10, j=2`,
`K(2)=(4439-2439·sqrt5)/100000<0` exactly (`4439^2=19,704,721 < 5·2439^2=29,743,605`,
check 18). The sign is `q`-dependent — at `q=1/2` the same `K(2)=(23-7sqrt5)/160>0`
(check 19), consistent with check 17 (at small `t`, `q` near `1`, `K` inherits the sign
of `t·L_{0,2}<0`); sampling only `q=1/2,1/3` misses the flip. The class contains this
member; positivity excludes it.

**(b) Spatial wrap — POSITIVE, but NOT in-class `[checks 20-21]`.** With
`K_t(j)=sum_{m∈Z} q^((j+5m)^2)` truncated at `|m|≤3` under an exact geometric tail
bound, the `m=0` term `q^(j^2)` alone certifies `K_t(j)≥S_M(j)>0` for `q=1/2,1/3`
(check 20). But it is **not convolution-closed**: by an exact low-order `q`-coefficient
comparison (bounded `m`-window, certified tail), `(W_q * W_q)(0)` carries a `q^2` term
(coeff `2`), while `W_{q^2}(0)` — and every single wrap `W_s(0)=1+2s^25+...` — has no
`q^2` term (coeff `0`), so `2≠0` (check 21). The spectral=spatial identification is a
Jacobi-theta `a→0` limit fact — exactly the **un-taken** limit the parent bars on the
baseline. So the positive object here is off-class.

**(c) Nearest-neighbor heat family — in-class, Metzler-positive, single-step local
`[checks 22-23]`.** The object simultaneously in-class, POS, and LOC at finite `N` is
`L_NN=circulant(-2,1,0,0,1)`: off-diagonals literally `1` (Metzler, exact integers),
row-sum `0`, distance-2 entries `0` (single-step local), a convolution semigroup by
construction (check 22). Its eigenvalues `λ_n=-4 sin^2(πn/5)` are exact in `Q[sqrt(5)]`
and the `n=1` magnitude is the PR #4825 locality-deficit quantity `(5-sqrt5)/2`
(check 23). These eigenvalues are the cosine `-4 sin^2(πn/5)`, **not** the quadratic
`-bal(n)^2` — the explicit **non-quadratic** (cos-vs-`n^2`) corrections; PR #4828's
"non-quadratic corrections" phrasing is cited by number, not read or matched. This is
the named-candidate witness.

**Canonicity of the balanced labels `[checks 24-25]`.** Own the representative
relativity: with **literal** labels `0..4` the generator is fully Metzler (off-diagonals
`3/2 ∓ sqrt5/5`, both `>0`, check 25) — so the (a) violation is representative-relative.
**But** balanced labels are **forced** by the quadratic exponent, not convention-shopped:
the literal-label eigenvalue multiset is `{0,-13/2,-13/2,-17/2,-17/2}` — **not**
`-bal(k)^2={0,-1,-1,-4,-4}` — and `bal(n)^2` is even in `n mod 5` while literal `n^2` is
not (check 24). Only balanced labels give the `q^(n^2)` family; this recomputation is
**self-contained**.

**Locality leg `[check 26]`.** The single-step deficit `4 sin^2(π/5)=(5-sqrt5)/2≠0`
equals `|λ_1|` of `L_NN` (check 26) — PR #4825's single-step exclusion of the exact
`Q`-gen. Full-step `Z_N` matching then needs signed weights (PR #4825's trichotomy),
**review-pending**. The witness stays **within the named candidate family** (Firewall):
it narrows the named field, not global uniqueness.

## Residue And Governance Map `[checks 27-28]`

The question reduces to **three named premises** plus the exact facts: **C-add**
(dynamics-family, clauses i–iii), **POS** (entrywise-nonnegative weights; the memo
withholds weights), **LOC** (single-step nearest-neighbor structure; review-pending
PR #4825). "One dynamics-shaped premise" was false. The complete **residue**: the three
premises + parent caveat + sibling audits (review-pending) + the balanced-labels
**canonicity** note (check 24). C-add's candidate homes, recorded **without adoption**:

1. **A narrow record-composition primitive** — a registered framework primitive, if
   the convolution clause is to be admitted as structure.
2. **The banked Dynamics-axiom proposal (on main; formerly PR #4843,
   docs-only/provenance, no adopted premise status)** — whose law +
   realized-branch content would *supply* C-add; provenance only.
3. **Remain a named conditional premise** — carry C-add as "if C-add, then ...".

Choosing among (1)–(3), and whether to admit POS or LOC, is an **owner decision**, not
a worker or audit call. This note maps the homes, takes none, and flags the residue
for owner review.

## Action-Wall End-State `[checks 27-28]`

Under C-add + POS + LOC, the named object witnessed **at finite N** among the tested
candidate objects is the **nearest-neighbor heat** family. The earlier "in-class AND
positive AND local" chain selected the *empty* intersection by conflating objects (a)
and (b); restated:

> `{C-add}` → convolution-semigroup **class** → `POS` (Metzler) + `LOC` (single-step)
> → **nearest-neighbor heat** finite-N witness; its **un-taken** `a→0` limit is
> the heat-kernel / wrapped Gaussian (the cos-vs-`n^2` corrections made explicit in
> check 23).

**No wall is closed.** The no-go is not retired; the relocation note's caveat is
inherited; every campaign citation is review-pending; the three levers (C-add, POS, LOC)
are **not adopted**. The end-state is a sharpened conditional and a named-candidate
witness — nothing is adjudicated.

## Negative-Scope Discipline Gate

This section gates the conditional wall language. It does not ship a no-go and does
not close the action wall.

- **N1 route enumeration:** deriving C-add from Record additivity fails by the
  correlated-weight toy; using spectral exact-Q-gen as the positive object fails
  positivity at `q=9/10`; using the spatial wrap fails convolution closure; claiming
  nearest-neighbor heat as globally unique is not proven and is narrowed to a
  named-candidate witness; lifting the `Z_N` toy witness to the SU(3) action wall is
  outside this note.
- **N2 wall independence:** C-add, POS, and LOC remain separate named premises. C-add
  supplies convolution, not positivity or locality; POS supplies nonnegative weights,
  not convolution or locality; LOC supplies single-step support, not positivity or
  convolution.
- **N3 hidden-wall scan:** "by construction" appears only for the explicitly supplied
  semigroup generator; "review-pending" campaign references are context only; no
  sibling result is imported as retained authority.
- **N4 residual matching:** the parent residual is the open action-selection question
  after the relocation note. This note addresses only exact `Z_N` candidate facts and
  does not claim the SU(3) residual is closed.
- **N5 rhetoric audit:** "fails positivity" is scoped to the spectral exact-Q-gen
  kernel witness; "not in-class" is scoped to the spatial wrap coefficient witness;
  "nearest-neighbor heat" is a named-candidate survivor/witness, not a global selector.
- **N6 partial-closure path scan:** possible homes for C-add are explicitly listed as
  available options: approved primitive, banked Dynamics proposal, or named conditional
  premise. None is adopted here.
- **N7 steelman:** a positive local convolution semigroup outside the named list, an
  asymmetric nearest-neighbor generator, or an SU(3)-specific action could evade the
  named-candidate separation. The note keeps those routes open.
- **N8 cross-cycle echo:** the parent no-go was already relocated into an open question;
  this note sharpens the conditional structure without retiring that open wall.

## Consequence (governance map)

The output is the map, not a verdict: the campaign now hangs on **three** named premises
(C-add + POS + LOC), with C-add carrying three homes in the governance map; every other
moving part is an axiom-supplied or exact recomputed fact on `Z_N` toys, not the SU(3)
wall.

## Does NOT

- Does **not** derive, adopt, or register C-add, POS, or LOC; does not claim the axioms
  supply a record-production process or a two-step convolution kernel.
- Does **not** select or adjudicate any action or claim uniqueness beyond the named
  candidate family; does **not** close, retire, or contradict any no-go — **no wall is closed**.
- Does **not** re-derive the PR #4819/#4824/#4825/#4828/#4829 results or read/match sibling
  conventions — self-contained recomputation of the isolated exact instances only; the
  wrapped Gaussian is named only as the **un-taken** limit.
- Does **not** edit axioms, policy, primitives, or registries, and sets **no** audit status.

## Dependencies

- Supplied surface: [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  (Record additivity; state
  definition; dynamics-section disclaimer; law sentence).
- Parent (unaudited, caveat inherited):
  [`ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md`](ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md).
- Campaign context (**review-pending**, cited by number, not read here):
  #4819, #4824, #4825, #4828, #4829.
- Banked proposal context: former PR #4843 is now on main as
  docs-only/provenance with no adopted premise status.

## No-Promotion Statement

This note promotes nothing. C-add, POS, and LOC are named, unadopted premises; the
candidate separation is family-level among named candidates and lives on `Z_N` toys, not the SU(3)
wall; the parent's caveat is inherited; citations are review-pending; the audit lane
alone sets status. The residue is an **owner decision**.

---

### Summary

- Final runner: **28 exact checks, all PASS** (Fraction + `Q[sqrt(5)]`; no floats).
- Corrected named-candidate separation: `{C-add}` → convolution-semigroup **class**,
  then **POS** + **LOC** → the **nearest-neighbor heat** finite-N witness; the wrapped
  Gaussian is only its
  **un-taken** `a→0` limit (check 23). The earlier "in-class ∧ positive ∧ local" chain had
  selected the *empty* intersection by conflating spectral (a, `K(2)<0` at `q=9/10`) with
  spatial wrap (b, positive, off-class) — both witnessed exactly.
- Residue: the **three named premises** (C-add, POS, LOC) + parent caveat + sibling
  audits (review-pending) + the balanced-labels **canonicity** note.
- **No wall is closed**; nothing adopted; citations review-pending; audit lane owns status.
