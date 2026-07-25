# Phase 1 / TASK A — registering the 2026-07-14 material as a citable authority

Worker report. Worked against `origin/main` @ `f865c14cd4` (fetched after
`git remote prune origin` cleared two stale ref locks). All four target
surfaces and all four runners are byte-identical to `origin/main`
(`git diff --quiet origin/main -- <path>` clean for each).

**Nothing outside this file was edited.** No commit, no push, no PR. No audit
verdict is set or predicted anywhere below. The draft note carries no status
value.

## Mandatory framework refresher — surfaces actually read

| surface | read | what it changed in this report |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | full, 194 lines | `:103-111` "Admissibility is not a dynamics axiom… It does not choose a Hamiltonian or transfer operator" — this is why the continuous-generator premise below is **supplied**, never derived. `:170` names "source/action and physical-observable identification" as an open gate outside the axioms. |
| `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` | full, 47 lines | Only three approved primitives (`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`). None of them supplies a pair generator, a covariance reading, a sign, or a rate. Rule 6: anything absent from the registry is unapproved. |
| `docs/audit/README.md` | lines 1-120 + field schema | `claim_type` / `claim_scope` / `audit_status` / `effective_status` are **auditor-owned**. `meta` = "non-claim infrastructure rows". Exactly two premise types chain-satisfy: axioms and registered primitives. |
| `docs/audit/data/axiom_premise_nodes.json` | full, 52 lines | `canonical_ids` = `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`. `minimal_axioms` node note explicitly ends: "…supplies no … source/action bridge, physical observable bridge…". |
| `docs/ai_methodology/skills/review-loop/SKILL.md:809-820` | churn-guard paragraph | "note hashes are source-content hashes… If the change would reset or requeue already-audited rows solely due to non-semantic churn, do not land the broad source sweep." Drives every cost line below. |

---

## 1. Why these four surfaces were invisible — measured, not inferred

The campaign asked whether the failure is (a) science never entering the
pipeline, (b) prose/ledger divergence, (c) pipeline gaps, or (d) registry
integrity. For **this** lane the answer is decisive and it is **(c) causing
(a)** — but not as a missing lint. It is an **explicit exclusion glob plus a
runner-extraction blind spot**, and the two compound.

### Defect 1 — `docs/work_history/**` is a configured ledger sink

`docs/audit/data/excluded_source_patterns.txt` contains the line
`docs/work_history/**`. `seed_audit_ledger.py:214 should_gate_node()` drops any
graph node under an excluded pattern that is an "unaudited unknown". So a
work_history note becomes a **citation-graph node** (it gets a `claim_id`) but
**never a ledger row**.

Reproduce:

```bash
python3 - <<'PY'
from fnmatch import fnmatchcase
pats=[l.strip() for l in open('docs/audit/data/excluded_source_patterns.txt')
      if l.strip() and not l.startswith('#')]
p='docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md'
print([pat for pat in pats if fnmatchcase(p,pat)])   # -> ['docs/work_history/**']
PY
```

**Size of the sink (measured):**

| quantity | count |
|---|---:|
| `.md` notes under `docs/work_history/` | **465** |
| …that name a runner | **364** |
| …whose runner file **exists on disk** | **364** |
| …that have a ledger row | **0** |
| `review_feedback/*2026-07-14*` batch alone | **134** notes, **111** with an existing runner |

So the four surfaces the campaign found are **4 of 364**. This is the single
largest quantified finding in this brief.

### Defect 2 — `## Verification` is not a runner section

`build_citation_graph.py:129-133`:

```python
RUNNER_SECTION_RE = re.compile(
    r"^#{2,6}\s+(?:(?:Primary|Key|Audited|New|Source|Validated|Corrected(?:\s+live)?)\s+)?"
    r"(?:Artifact(?:\s+chain)?|Artifacts|Script|Scripts|Runner|Runners|Files|Surfaces|What\s+was\s+tested)\b.*$",
    re.IGNORECASE | re.MULTILINE,
)
```

`Verification` is absent. All four target notes put their runner **only** under
a trailing `## Verification` heading
(e.g. `QUBIT_SYMMETRY_…:141-147`), so `extract_runner()` returns `None`:

```
QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md
   claim_id        = work_history.repo.review_feedback.qubit_symmetry_exchange_law_reduction_probe_note_2026-07-14
   claim_type_hint = meta          <- from "**Type:** meta"
   runner_path     = None          <- despite scripts/qubit_symmetry_..._2026_07_14.py existing and passing
   n_md_link_deps  = 0
```

(identical shape for the other three; `n_md_link_deps` = 3, 4, 2).

**Repo-wide blast radius (measured):** 808 notes use `## Verification` to name
a runner — it is the dominant house convention. 52 of them resolve to
`runner_path=None`; the other 756 are saved only because they *also* carry a
`**Primary runner:**` label.

### Consequence, stated plainly

The four notes carry `**Type:** meta` (`QUBIT_SYMMETRY_…:5`) and
`**Authority:** none` (`:7`). Combined with defect 1 (no row) and defect 2 (no
runner), they are *triply* invisible: not a claim, not audited, not runnable
from metadata. Nothing can cite them as authority, which is exactly why two
campaigns re-derived their contents.

---

## 2. (a) What is PROVED-AND-GATED vs merely ASSERTED

I ran all four runners on `origin/main` content. All pass:

| runner | PASS | FAIL |
|---|---:|---:|
| `scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py` | 44 | 0 |
| `scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py` | 122 | 0 |
| `scripts/relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py` | 167 | 0 |
| `scripts/full_law_inventory_adversarial_reduction_probe_2026_07_14.py` | 96 | 0 |
| **total** | **429** | **0** |

That 429 is **not** an evidence count, and all four notes say so themselves
(e.g. `QUBIT_SYMMETRY_…:149-150`: "The PASS total contains related checks and
is not an independent evidence count."). Breaking it down:

### PROVED AND GATED (survives into the claim)

| result | gate | independent recomputation |
|---|---|---|
| Commutant of the diagonal (common-frame) `SU(2)` action on two qubits has complex dimension 2 = span{I, SWAP} | `qubit_…py:87` (nullspace of the direct commutator system); `relational_…py:173` and `single_…py:194` (vectorized superoperator, `rank == 14`) | **Yes — twice, by two different methods.** Strongest item in the set. |
| Under **independent onsite** covariance the commutant collapses to dimension 1 (scalars only) | `qubit_…py:108`, `:111`, `:114` | single method |
| `SWAP = (I + XX + YY + ZZ)/2` exactly | `qubit_…py:98` | — |
| `SWAP` spectrum `{+1: 3, −1: 1}`; `+SWAP` ground sector = rank-1 singlet, `−SWAP` ground sector = rank-3 triplet | `qubit_…py:121,127,128` | `relational_…py:197` |
| Three-site `H_η = H_1 + η H_2` moves a gap ratio 2 → 1 at `η = 1/3` | `single_…py:233-239` | — |
| Adjacent exchange terms do not commute; nested commutator reaches site three at second order | `qubit_…py:143,159,160` | `FULL_LAW_…:111-128` |
| Quarter exchange is Bell-capable, `CHSH = 2√2` exactly with four explicit correlators | `qubit_…py:192,193`; `relational_…py:300` | two independent constructions |
| Lüders vs random-phase instruments share one averaged channel but carry different weights `(2/3,1/3)` vs `(1/2,1/2)` | `relational_…py:321,322`; `single_…py:377,378` | — |
| Four disagreement measures (overlap, infidelity, HS, regularized rel-entropy) co-order, unique minimum at `Q=P` | `relational_…py:228-237` | — |

### ASSERTED, NOT GATED (must not enter the claim as proved)

1. **The sign(b) quotient is not actually tested.** `RELATIONAL_…:158-169` and
   `SINGLE_INVARIANT_…:158-160` claim positive scaling plus a global shift
   removes `a` and `|b|` but not `sign(b)`. The only runner line that purports
   to gate it is `relational_…py:198`:

   ```python
   check("B positive rescaling and identity shift leave only the nonzero exchange sign",
         {-1, 1} == {sp.sign(value) for value in (-3, 5)})
   ```

   This is **vacuous** — it asserts `{sign(−3), sign(5)} == {−1, 1}` and never
   touches `a`, `b`, `α`, `β`, or `SWAP`. The load-bearing quotient claim is
   ungated. I rebuilt it (§5, G2).

2. **`H_1` and `H_2` covariance is asserted, not checked.**
   `SINGLE_INVARIANT_…:165-170` says both are "Hermitian, neighbor-exchange
   invariant, and common-frame invariant". `single_…py:238` checks **only**
   Hermiticity and mutual commutation:

   ```python
   check("B two independent invariant interaction terms survive the same symmetries",
         h_one.H == h_one and h_two.H == h_two and h_one * h_two == h_two * h_one)
   ```

   Covariance — the very property that makes `η` an *independent invariant* and
   therefore makes the counterexample bite — is never computed. I rebuilt it
   (§5, G5b–G5d); both are in fact covariant, so the claim survives, but on a
   gate I supplied rather than one the repo had.

3. **The active-edge phase is illustrated, not derived.** `relational_…py:377-382`
   hand-builds `active_edge_count = sp.diag(1, 2)` and a matching phase matrix.
   No record-conditioned edge set is constructed. Correct in content, weak as a
   gate. Rebuilt (§5, G6).

4. **The reversible-record obstruction is proved by instance only.**
   `QUBIT_SYMMETRY_…:85-94` argues generally that `R ≤ U†RU` forces equality by
   equal trace and rank. `qubit_…py:196-208` only checks one unitary at `θ=π/7`
   and one specific super-projection. The general theorem is prose.
   **Excluded from the claim below.**

5. **Continuity of the `Q=P` minimizer.** `RELATIONAL_…:126-129` asserts the
   result holds for all rank-one projectors; `relational_…py:226-237` tests six.
   Kept out of the claim's Results.

### Runner hygiene defects found in passing

- `qubit_…py:143` and `:144` are the **same check** with two different labels
  (both `not exact_equal(s12 * s23, s23 * s12)`), inflating PASS by one.
- Sections A and G of `qubit_…py` (and the corresponding `documentation_contract`
  sections of the other three) are **prose-needle greps** on the note text, not
  mathematics. Of the 44 PASS in `qubit_…py`, **15** are needle/contract checks
  (4 in section A, 11 in section G) — i.e. ~34% of that runner's PASS total is
  self-referential.
- Two notes **award themselves a status**: `SINGLE_INVARIANT_…:803` and
  `RELATIONAL_…:736` both read `**No-go-discipline status:** PASS`. The draft
  below deliberately does not.

---

## 3. (b)(c)(d) THE DRAFT NOTE

Proposed path: `docs/COMMON_FRAME_PAIR_GENERATOR_EXCHANGE_CLASS_BOUNDED_THEOREM_NOTE_2026-07-25.md`

**The path is load-bearing.** It must be at `docs/` root. Anywhere under
`docs/work_history/` it is swallowed by defect 1 and registers nothing.

Vocabulary check: every term used below (`bounded_theorem`, `common-frame`,
`pair generator`, `exchange`, `ground sector`, `active edge`, `no-go discipline
gate`) already appears in the source surfaces or the canonical templates. No new
axiom, primitive, class, or tag is introduced.

---

````markdown
---
claim_id: common_frame_pair_generator_exchange_class_bounded_theorem_note_2026-07-25
claim_type: bounded_theorem
claim_scope: "Under four supplied hypotheses (one M_2(C) site domain on the Z^3 nearest-neighbour graph; an autonomous time-independent self-adjoint pair generator; a sum of identical two-site terms; and COMMON-frame SU(2) covariance), the commutant of the diagonal frame action on two qubits is exactly span{I, SWAP}, so every admissible pair generator is h = a I + b SWAP. Positive clock rescaling and a global energy shift remove a and |b| and leave exactly sign(b), which is separated by the GROUND-SECTOR DEGENERACY (1 for +SWAP, 3 for -SWAP). Three stated limitations bound the result: under INDEPENDENT onsite covariance the commutant is only the scalars and no nontrivial pair law survives; 'exactly two' holds only for the two-site edge class under the supplied identical-pair-term ansatz, since at three sites H_1 + eta H_2 carries a dimensionless eta moving a gap ratio 2 -> 1 at eta = 1/3 that neither clock rescaling nor energy shift removes; and the identity term is NOT inert on a record-conditioned active-edge set. The one-excitation band minimum is recorded as NOT a valid separator: Z^3 nearest-neighbour adjacency is bipartite, the sublattice relabeling D gives D A D = -A, and the band is therefore sign-blind. No formation rule, sign selection, rate, instrument, or actuality is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/common_frame_pair_generator_exchange_class_2026_07_25.py
---

# Common-Frame Pair Generator: The Exchange Class and Its Three Limitations

**Date:** 2026-07-25
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set,
forecast, or imply an audit verdict, and edits no axiom, primitive, registry,
queue, or generated audit surface.
**Primary runner:**
[`scripts/common_frame_pair_generator_exchange_class_2026_07_25.py`](../scripts/common_frame_pair_generator_exchange_class_2026_07_25.py)

**Upstream authority:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Prior exploratory surfaces** (route inputs only; carry `Authority: none`, no
claim id, and no ledger row — nothing below inherits status from them, and every
algebraic step is recomputed in this note's runner):
[`QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md`](work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md),
[`RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md`](work_history/repo/review_feedback/RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md),
[`SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md`](work_history/repo/review_feedback/SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md),
[`FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md`](work_history/repo/review_feedback/FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md)

## Purpose

Convert a symmetry classification that has been recomputed twice in the repo
into one citable bounded theorem, with its limitations attached rather than
dropped. The classification is genuinely useful: it takes an arbitrary
Hermitian two-site generator (15 real parameters beyond trace) down to one
physical coefficient. The limitations are equally load-bearing, and a prior
campaign lost all three of them.

This note claims a **classification**, not a law. It selects no sign, no rate,
no formation rule, no instrument, and no actual history.

## Hypotheses (all supplied; none derived)

Each is supplied. The Qualification at
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) requires a
retained derivation, bridge, or registered primitive before any of these could
be treated as framework content, and none of them has one. In particular that
memo states that "Admissibility is not a dynamics axiom" and that it "does not
choose a Hamiltonian or transfer operator", so H1–H3 cannot be read off the
axioms.

- **(H1) Domain.** One `M_2(C)` possibility domain per site on the cubic `Z^3`
  nearest-neighbour graph. *This much is axiom content.*
- **(H2) Autonomous generator.** Between-record evolution is generated by a
  time-independent self-adjoint operator. Time-independence is essential and is
  not implied by strong continuity: the covariant family `h(t) = J(t) SWAP` is
  pointwise covariant and retains an arbitrary coefficient function.
- **(H3) Identical two-site terms.** The generator is a sum of identical
  nearest-neighbour two-site terms. This is an **ansatz**, and Limitation 2
  below is precisely the cost of it.
- **(H4) COMMON-frame covariance.** One and the same `U ∈ SU(2)` acts on both
  sites of an edge. This is the decisive premise; see Limitation 1.

**No pairwise independence of H1–H4 is claimed.** They are stated as a
conjunction, and the runner does not attempt an independence audit of them.

## Results

**R1 (classification).** Under H1 and H4 the commutant of the diagonal action
`U ⊗ U` on `C^2 ⊗ C^2` has complex dimension exactly 2 and equals
`span{I, SWAP}`. Hence under H1–H4 every admissible pair generator is

```text
h = a I + b SWAP
  = (a + b/2) I + (b/2)(X⊗X + Y⊗Y + Z⊗Z),
```

with `a, b` real. The exchange identity `SWAP = (I + X⊗X + Y⊗Y + Z⊗Z)/2` is
exact.

**R2 (quotient).** On a **fixed** active-edge set, the map
`(h, t) ↦ (α h + β I, t/α)` with `α > 0` leaves the generated channel unchanged
up to a global phase. It removes `a` (take `β = −α a`) and removes `|b|` (take
`α = 1/|b|`). It does **not** remove `sign(b)`: no pair `(α > 0, β)` carries
`+SWAP` to `−SWAP`. Positivity of `α` is exactly what makes the sign physical —
with an unconstrained scale the two signs are identified.

**R3 (the separator).** The relabeling-proof invariant separating the two signs
is the **ground-sector degeneracy**. `SWAP` has spectrum `{+1 (×3), −1 (×1)}`,
so:

- `+SWAP` has a **one-dimensional** ground sector (the singlet);
- `−SWAP` has a **three-dimensional** ground sector (the triplet).

Degeneracy of the lowest eigenvalue is invariant under every `α > 0` rescaling,
every `β I` shift, and every unitary conjugation, so it survives the whole
licensed quotient of R2 and any change of frame or site labelling.

**R4 (the band minimum is NOT a separator — recorded explicitly).** The
one-excitation band minimum must **not** be used in place of R3. `Z^3`
nearest-neighbour adjacency is bipartite by the parity of `x + y + z`. Let `D`
be the diagonal sublattice relabeling `D_xx = (−1)^{parity(x)}`. Then for the
adjacency matrix `A`

```text
D A D = −A,     hence  spec(A) = −spec(A).
```

In the one-excitation sector the generator restricted to one flipped site is
`(E·I − Deg) + A` with `E` the edge count, so after the R2 energy shift removes
the `(E·I − Deg)` piece on a regular graph, the `+J` and `−J` one-excitation
bands are **identical as sets**. The band minimum is therefore sign-blind on
`Z^3` and separates nothing. It separates only on a **non**-bipartite graph
(a triangle has `spec(A) = {2, −1, −1}`, not sign-symmetric), and `Z^3` is not
one. This is the reason R3 is stated in terms of ground-sector degeneracy.

## Limitations (all three are part of the claim, not caveats to it)

**L1 — common-frame covariance is a PREMISE that CREATES the class.**
H4 is not a notational convenience; it is the physics. Under **independent**
onsite covariance — the same `SU(2)` acting separately on each site — the
commutant collapses to complex dimension **1**, the scalars alone. `SWAP` is not
invariant there. So under independent onsite covariance **no nontrivial pair
interaction survives at all** without a further supplied object: a connection, a
link variable, a shared frame, or a symmetry reduction. The axiom sentence "No
possibility is privileged" does not choose between the two readings. Adopting
the exchange class therefore imports a physical premise; it does not read one
off a symmetry slogan.

**L2 — "exactly two parameters" holds only for the two-site edge class under
H3.** The count is a statement about one edge under the identical-pair-term
ansatz, and it does not survive enlarging the support. On three sites with a
centre and two equivalent neighbours, both

```text
H_1 = SWAP_01 + SWAP_02,
H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01
```

are Hermitian, invariant under exchanging the two equivalent neighbours, and
invariant under the common-frame diagonal `SU(2)` — i.e. they satisfy exactly
the same symmetry hypotheses. The family `H_η = H_1 + η H_2` therefore carries a
genuinely independent **dimensionless** coefficient `η`, and it moves a spectral
gap ratio

```text
(E_1 − E_0)/(E_2 − E_1) = 2   at η = 0,
                        = 1   at η = 1/3.
```

A gap **ratio** is invariant under both `α > 0` rescaling and `β I` shift, so
neither clock rescaling nor an energy-zero choice removes `η`. Symmetry licenses
the term; it does not fix it.

**L3 — the "inert" identity term is NOT inert on a record-conditioned
active-edge set.** R2's removal of `a` is conditional on a **fixed** active-edge
set. If record formation changes which edges are active, then adding `β I` per
active edge contributes `β N_active`, which is not a common scalar across
sectors of different `N_active`. Two record sectors with one and two active
edges acquire a relative phase `exp(−i β t)`, which moves an interference term
on a coherent superposition of those sectors and is therefore not a removable
global phase. A record-dependent active graph needs an explicit vacuum/edge
energy convention or a superselection argument; the energy shift may not be
discarded before the domain is fixed.

## Non-Claims

This note does **not** claim, and its runner does not gate:

- any selection of `sign(b)`, of `|b|`, of a rate, or of a time unit;
- that H2–H4 are derivable from Lattice/Qubit/Admissibility/Record — the axiom
  memo says the opposite for dynamics;
- pairwise independence of H1–H4;
- a well-defined discrete update: on overlapping edges the pair terms do not
  commute, so a product update still needs an ordering/layering rule or a
  causal-invariance theorem;
- a strict light cone. A finite-range continuous generator gives a
  Lieb–Robinson quasilocal cone with tails, not the exact cone of a layered
  circuit; the two have different exact causal semantics and one must be chosen
  and its continuum interpretation proved separately;
- any record formation, formation trigger, instrument, Born weight, sampling
  rule, actuality, or single realized outcome. Bell **capability** at exchange
  angle `π/4` is not Bell sampling and supplies no outcome;
- the general reversible-record obstruction. The trace/rank argument that
  `R ≤ U†RU` forces equality is left to its exploratory source and is **not**
  gated here;
- continuity of the `Q = P` disagreement minimizer over all rank-one
  projectors;
- any relativistic, chiral, fermionic, gauge, species, matter, clock-metric, or
  gravitational consequence. A cubic exchange system has a parity-even
  quadratic magnon dispersion, not a Weyl sector.

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

### N1 — Alternative-route enumeration (attempted)

| route | strongest attempted form | outcome |
|---|---|---|
| common-frame `SU(2)` covariance | commutant of `U ⊗ U` | dimension 2, `span{I, SWAP}` — the stated class |
| independent onsite covariance | commutant of separate `SU(2)` actions | dimension 1, scalars only — L1 |
| enlarge support to three sites | `H_1 + η H_2` under the same symmetries | independent dimensionless `η` survives — L2 |
| remove `a` by energy shift | `β I` on a fixed active-edge set | succeeds on fixed graph, fails on record-conditioned graph — L3 |
| remove `sign(b)` by rescaling | `α > 0` clock rescaling | fails; only an unlicensed `α < 0` identifies the signs |
| separate signs by band minimum | one-excitation dispersion | **fails on `Z^3`** by bipartite relabeling — R4 |
| separate signs by ground sector | lowest-eigenvalue degeneracy | succeeds, 1 vs 3 — R3 |
| drop autonomy | strongly continuous covariant `h(t) = J(t) SWAP` | arbitrary coefficient function returns; H2 is load-bearing |
| discrete layered update instead of a generator | product of overlapping pair terms | ordering/layering rule required; not supplied |

### N2 — Wall-independence audit (attempted)

| wall pair | finite control that separates them |
|---|---|
| covariance reading vs class size | common frame gives dimension 2, independent onsite gives dimension 1 |
| class size vs support | dimension 2 on one edge, `η` appears at three sites |
| scale freedom vs sign | `α > 0` removes `|b|`, never `sign(b)` |
| energy zero vs sector | `β I` is inert at fixed `N_active`, not across `N_active ∈ {1,2}` |
| spectrum vs degeneracy | `+SWAP` and `−SWAP` have the same eigenvalue set `{±1}`; only the multiplicities differ |
| band minimum vs ground sector | bipartite relabeling moves the band, not the ground degeneracy |

A later theorem may tie several rows. These controls only prevent one row from
being silently renamed as another. **No claim is made that H1–H4 are pairwise
independent.**

### N3 — Hidden-wall scan (attempted)

Exposed rather than hidden: the common-versus-independent frame reading;
autonomy/time-independence; the identical-pair-term ansatz; the two-site support
restriction; the fixed-versus-record-conditioned active-edge set; the sign of
`b`; the magnitude `|b|` and its time unit; the dimensionless interaction angle;
overlapping-edge ordering; continuous-versus-circuit causal semantics; the
absence of any formation trigger, instrument, weight, or realized member; and
the absence of any matter, chirality, clock-metric, or gravity content.

### N4 — Exact residual matching (attempted)

The residual this note closes is narrow: *what is the pair-generator class, and
what survives the licensed quotient?* R1–R3 answer it. The residuals it does
**not** close, and does not re-count as evidence, are the sign selection, the
rate, the occurrence/formation rule, the instrument and weights, the realized
member, and every matter/clock/gravity interface. L2 shows the classification
residual itself reopens as soon as the support grows past one edge.

### N5 — Resolution and rhetoric audit (attempted)

- "Commutant is `span{I, SWAP}`" is a statement about a **two-qubit pair
  generator under common-frame covariance**, not about a general qubit QCA.
- "Exactly two" means two real parameters `a, b` on **one edge under H3**, and
  L2 states where that stops.
- "Inert identity" is true only on a **fixed** active-edge set (L3).
- "Ground sector" means the lowest-eigenvalue eigenspace and its **dimension**,
  not the eigenvalue.
- "Band minimum is not invariant" is a positive computation (R4), not a
  rhetorical hedge.
- Bell **capability** is not Bell sampling, an outcome, or a record.
- The prior 2026-07-14 surfaces are exploratory route inputs with
  `Authority: none`; nothing here inherits status from them.

### N6 — Partial-closure path (attempted)

1. Test whether the common-frame reading is forced by, or merely compatible
   with, the Admissibility covariance sentence.
2. Classify the full low-support invariant term basis past one edge, so the L2
   `η` family is enumerated rather than exhibited.
3. Search for a conservation or index theorem fixing `sign(b)` rather than
   registering it.
4. Fix the active-edge/vacuum energy convention, or prove the superselection
   that makes L3 vacuous.
5. Only then ask whether the generator compiles into a homogeneous
   nearest-neighbour update on `Z^3`.

### N7 — Strongest steelman (attempted)

The strongest opponent is a theorem deriving H2–H4 from the exact admissibility
law, so that the pair class becomes theorem content rather than an ansatz, and
simultaneously fixing `sign(b)` by a conservation or index argument and
supplying the active-edge convention that retires L3. Such a theorem would
convert most of this note into a corollary and would defeat its bounded
framing. Nothing here excludes it; it is not constructed.

### N8 — Cross-cycle echo (attempted)

The commutant computation appears independently in three prior runners, by two
different methods, and agrees. The new content of **this** note relative to
those exploratory surfaces is: (i) the sign quotient is gated by construction
rather than by a vacuous literal; (ii) the covariance of the three-site `H_1`,
`H_2` is actually computed, which is what makes `η` an independent invariant;
(iii) the active-edge non-inertness is built from a record-conditioned sector
pair instead of a hand-written diagonal; and (iv) the band-minimum separator is
positively **refuted** on the bipartite `Z^3` graph, and the ground-sector
degeneracy is put in its place.

## Verification

Run:

```bash
python3 scripts/common_frame_pair_generator_exchange_class_2026_07_25.py
```

The runner recomputes every constant above from primitives with exact `sympy`
arithmetic, and pairs each claimed constant with a **construction-mutation
probe** that must move it. The PASS total is a gate count, not a count of
independent scientific facts.

No axiom, primitive, registry, ledger, queue, or generated audit surface is
edited by this note or its runner.
````

---

## 4. (e) Do the two existing runners suffice? — **No. A new consolidated runner is required.**

The campaign brief named two runners; there are in fact **four**. None of them,
and no combination of them, can serve as this note's runner. Three blocking
reasons:

1. **Three of the note's load-bearing constants are ungated today** — the
   `sign(b)` quotient (vacuous literal at `relational_…py:198`), the covariance
   of `H_1`/`H_2` (never computed, `single_…py:238`), and the record-conditioned
   active-edge phase (hand-built diagonal, `relational_…py:377-382`).
2. **R4 does not exist anywhere in the repo.** The bipartite relabeling
   `D A D = −A`, the resulting sign-blindness of the one-excitation band, and the
   `Z^3` bipartiteness witness are new. `FULL_LAW_…:335-337` gets close — it warns
   that "Checking only the minimum energy does not certify this reversal" — but
   it neither proves why nor supplies the relabeling.
3. **A single note must have a single primary runner.** `extract_runner()`
   returns one path; four runners would need three of them registered as
   helpers, and each of the four also greps *its own* note text for phrases that
   the new note does not contain, so all four would fail against it.

### Runner design — gates, with a construction-mutation probe per constant

**I have already written and run this runner.** It is at
`<scratchpad>/verify_pair_law.py` and reports **PASS=44, FAIL=0**. It should be
landed at `scripts/common_frame_pair_generator_exchange_class_2026_07_25.py`.
Gate groups:

| group | gates | claimed constant | CONSTRUCTION-MUTATION probe |
|---|---|---|---|
| **G1** commutant | 5 | `dim = 2`, `span{I, SWAP}` | mutate common-frame → **independent onsite**; `dim` must drop to **1** and `SWAP` must fail to commute *(G1d, G1e)* |
| **G2** quotient | 5 | `a` removable, `\|b\|` removable, `sign(b)` **not** | mutate `α > 0` → unconstrained `γ`; the two signs must become identified *(G2e)*. Replaces the vacuous `relational_…py:198`. |
| **G3** separator | 6 | ground degeneracy **1** (`+SWAP`) vs **3** (`−SWAP`) | mutate the sign; degeneracy must move. Invariance re-verified across 9 `(α>0, β)` pairs and under an explicit unitary conjugation *(G3e, G3f)* |
| **G4** band minimum | 15 | band is **sign-blind** on `Z^3` | mutate bipartite → **non-bipartite triangle**; sign-symmetry of `spec(A)` must **break** *(G4d, G4e)*. Verified on four bipartite graphs (P3, C4, Q3, K2,3) plus a `4×4×4` periodic `Z^3` bipartiteness witness *(G4f)* |
| **G5** three-site `η` | 8 | ratio **2** at `η=0`, **1** at `η=1/3` | mutate `η`; ratio must move. Adds the covariance checks the repo runner omits *(G5b, G5c, G5d)*, plus an `α>0`/`βI` mutation showing the ratio is quotient-invariant *(G5h)* |
| **G6** active edge | 5 | identity term **not** inert | mutate to **equal** active-edge counts; the same term must become inert *(G6e)* |

Measured output:

```text
PASS=44
FAIL=0
```

Selected gate lines, verbatim:

```text
PASS G1a common-frame commutant has complex dimension 2 :: dim=2
PASS G1d MUTATION independent-onsite covariance collapses commutant to dim 1 :: dim=1
PASS G2d NO positive rescaling + shift maps +SWAP to -SWAP :: solutions=[]
PASS G2e MUTATION dropping alpha>0 would identify the two signs :: [{gamma: -1}]
PASS G3b +SWAP ground sector is the 1-dim singlet :: deg=1
PASS G3c -SWAP ground sector is the 3-dim triplet :: deg=3
PASS G4a[cube Q3] bipartite relabeling gives D A D = -A
PASS G4b[cube Q3] hence spec(A) = -spec(A): the band is sign-blind :: [-3,-1,-1,-1,1,1,1,3]
PASS G4d MUTATION non-bipartite triangle: spec(A) is NOT sign-symmetric :: spec=[-1.0,-1.0,2.0]
PASS G4f Z^3 nearest-neighbour adjacency is bipartite by x+y+z parity
PASS G5b H1 is common-frame (diagonal SU(2)) invariant
PASS G5e gap ratio is 2 at eta=0 :: spec=[-1, 1, 2]
PASS G5f gap ratio is 1 at eta=1/3 :: spec=[-4/3, 2/3, 8/3]
PASS G6d it moves an interference (off-diagonal) term between record sectors :: offdiag=I/2
PASS G6e MUTATION with EQUAL active-edge counts the identity term is inert
```

Design rules honoured: **no prose-needle gates.** Unlike all four existing
runners, this one never greps its own note text, so its PASS total is entirely
mathematical. Every gate is exact (`sympy`, no floats in any load-bearing
comparison; the only `float()` calls are inside a non-load-bearing sort key and
a display).

---

## 5. Prioritized, batched repair plan with churn costs

Churn priced against the **live** ledger shards in `docs/audit/data/ledger/`,
never against prose. Requeue counts come from a read-only simulation of the
patched extractor over all 4485 discovered notes.

### Batch A1 — TOOLING: teach `extract_runner` the `## Verification` heading

- **Type:** tooling fix. **Files:** `docs/audit/scripts/build_citation_graph.py`
  (one regex alternation).
- **Design constraint (measured, important):** `Verification` must be tried
  **after** the existing routes, not merged into `RUNNER_SECTION_RE` in place.
  Merging it in place changes `runner_path` on **5** notes that currently
  resolve correctly via another route (all 5 under `work_history/`, all naming a
  *predecessor* script in their Verification block). Trying Verification **last**
  gives **gains = 52, changes = 0**.
- **Requeue cost: 4 rows.** Every one is `audit_status = unaudited`:
  - `docs/ANOMALY_FORCES_TIME_ADMISSION_III_NOTE_2026-05-17.md` — `(unaudited, meta, meta)`
  - `docs/CKM_FIVE_SIXTHS_EXPONENT_DISCRIMINATOR_SUPPORT_NOTE_2026-07-02.md` — `(unaudited, unaudited, bounded_theorem)`
  - `docs/DM_SIGMA_HIER_CLOSURE_PACKET_NOTE_2026-04-20.md` — `(unaudited, unaudited, positive_theorem)`
  - `docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` — `(unaudited, unaudited, positive_theorem)`
- **Verdicts risked: 0.** Nothing audited is touched. The remaining 48 gains are
  under `docs/work_history/**` and have no ledger rows at all.
- **Why worth it:** three of those four rows are `positive_theorem` /
  `bounded_theorem` that would otherwise be **audited with no runner attached**.
  This is strictly corrective, costs zero verdicts, and permanently closes the
  defect class for the 808 notes that use the `## Verification` convention.
- **Priority: 1.** Highest value-per-churn in the brief.

### Batch A2 — CONTENT: land the registration note + consolidated runner

- **Type:** content (new science surface). **Files:** 1 new note at `docs/` root
  + 1 new runner at `scripts/`.
- **Requeue cost: 0 rows.** A new file seeds a **new** row; it edits no existing
  note, so no existing hash moves. The four 2026-07-14 sources are **not
  modified** — they stay exploratory, which is both correct and free.
- **Verdicts risked: 0.**
- **Why worth it:** it is the only action that makes this material citable.
  Nothing can depend on an `Authority: none` note with no claim id.
- **Priority: 1** (parallel with A1; independent of it).

### Batch A3 — TOOLING: lint rule "runner-gated note in an excluded sink"

- **Type:** tooling fix. **Files:** `docs/audit/scripts/audit_lint.py` (new
  notice), no source-note edits.
- **Rule:** emit a notice when a note under an `excluded_source_patterns.txt`
  path names a runner that **exists on disk** and whose runner **passes**. That
  is the exact signature of unregistered science.
- **Requeue cost: 0 rows.** A lint notice sets no field and moves no hash.
- **Verdicts risked: 0.**
- **Current population it would surface: 364 notes** (of 465 under
  `docs/work_history/`). That is a backlog, not a to-do list — the notice should
  be advisory, and triage should be owner-prioritised, not drained blind.
- **Why worth it:** this is the rule whose absence let two campaigns waste a
  wave each. It converts an invisible sink into a measured queue at zero audit
  cost.
- **Priority: 2** (after A1, because A1 is what makes `runner_path` resolvable
  for 52 of them in the first place).

### Batch A4 — CONTENT: repair the two defective gates in the 2026-07-14 runners

- **Type:** content fix. **Files:** `scripts/relational_…_2026_07_14.py:198`
  (vacuous `{sign(-3), sign(5)}` literal), `scripts/qubit_…_2026_07_14.py:143-144`
  (duplicated check), optionally `scripts/single_…_2026_07_14.py:238` (add the
  omitted covariance check).
- **Requeue cost: 0 rows** — these runners are paired with notes under
  `docs/work_history/**`, which have no ledger rows.
- **Verdicts risked: 0.**
- **Why worth it / why NOT first:** a vacuous gate that passes is worse than a
  missing one, so this is real. But A2 already supersedes all three checks with
  properly constructed gates, so this batch is **hygiene on an exploratory
  surface**, not a correctness dependency.
- **Priority: 4 (lowest).** Explicitly **do not** bundle this with a broader
  sweep of the other 360 work_history runners; that would be exactly the mass
  cosmetic sweep the churn guard forbids, and it would buy nothing since none of
  them has a ledger row.

### Explicitly NOT recommended

- **Do not** move the four 2026-07-14 notes out of `docs/work_history/`. Moving
  them would create four new ledger rows for exploratory prose that correctly
  carries `Authority: none`, and would orphan the inbound links from their own
  runners (which read the note text by absolute path and would break).
- **Do not** remove `docs/work_history/**` from `excluded_source_patterns.txt`.
  That single line would seed **~465** new ledger rows at once — the largest
  possible audit-capacity burn available in this repo, for a directory that is
  correctly a working-history sink. The right fix is A3's advisory notice plus
  A2-style selective promotion.
- **Do not** hand-fix the 52 `## Verification` notes individually. A1 fixes all
  of them for zero churn.

---

## 6. Answer to the campaign's diagnostic question, for this lane

Proportions, as measured on this lane only:

- **(c) pipeline gaps: dominant.** Two independent mechanisms — a ledger
  exclusion glob covering 465 notes, and a runner-extraction blind spot covering
  52 — jointly guarantee that runner-gated science written into
  `docs/work_history/` is unfindable. Neither is a "missing lint"; one is an
  explicit configuration line and the other is a regex omission.
- **(a) science never entering the pipeline: large, and fully caused by (c).**
  364 notes with existing runners and zero ledger rows.
- **(b) prose/ledger divergence: not the mechanism here.** These notes do not
  carry *false* status labels. They carry *honest* ones — `Authority: none`,
  `Type: meta` — that are accurate and precisely why nothing cites them. The
  divergence problem is real elsewhere in the corpus but it is not what hid this
  material.
- **(d) registry integrity: one confirmed instance touching this lane.**
  `MINIMAL_AXIOMS_2026-06-29.md:170` names "source/action and
  physical-observable identification" as an open gate; it appears in no node of
  `axiom_premise_nodes.json` (which lists exactly four `canonical_ids`) and has
  no ledger row. The pair-generator premises H2–H4 sit squarely on that
  unregistered gate.

This **confirms the supervisor's recorded prediction** — (c) enabling (a),
with the highest-value repair being a lint/tooling rule plus a targeted
registration pass rather than a mass prose sweep — and sharpens it: the toolchain
does not merely *fail to require* registration, it *actively excludes* the
directory where the science was written.
