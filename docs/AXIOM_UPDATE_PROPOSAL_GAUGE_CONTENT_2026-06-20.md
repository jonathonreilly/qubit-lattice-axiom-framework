# Axiom-Update Proposal — Gauge-Content / Particle-Content Primitive (P-HY, P-COMP)

**Date:** 2026-06-20
**Type:** axiom_update_proposal (FOR OWNER GOVERNANCE DECISION — adopts nothing)
**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block01-20260620`.
**Status authority:** independent audit lane / owner only. This note sets NO
audit verdict and promotes NO axiom. Per
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1/§4, the candidate primitive below is
recorded as an **unmade science-level decision waiting on human input**, not an
in-lane amendment of the premise surface.
**Primary runner:**
[`scripts/axiom_update_proposal_gauge_content_2026_06_20.py`](../scripts/axiom_update_proposal_gauge_content_2026_06_20.py)
**Runner cache:**
[`logs/runner-cache/axiom_update_proposal_gauge_content_2026_06_20.txt`](../logs/runner-cache/axiom_update_proposal_gauge_content_2026_06_20.txt)
(**TOTAL: PASS=21 FAIL=0**)

> **`hypothetical_axiom_status` (carried throughout):** *"conditional on accepted
> new axiom; not retained on the actual current surface."* Every "DISCHARGES"
> claim below is a consequence of an **UNADOPTED** candidate primitive. This
> labelling does NOT promote the primitive; only an external owner/governance
> decision can. No bare `retained`/`promoted` appears anywhere in this note.

---

## 0. One-line

The two gauge/particle-content premises of
`ANOMALY_FORCES_TIME_THEOREM.md` — **P-HY** ("the canonical traceless `Y_like`
abelian direction is a *gauged* `U(1)`") and **P-COMP** ("the anomaly-cancelling
completion is the *opposite-chirality* SU(2)-singlet RH template, existence") —
genuinely wall the no-new-axiom surface (the four published gauging
discriminators are blind; the only *native* completions are vector-like, so no
chiral RH template is forced). The **weakest** addition that discharges both is a
single gauge-content primitive **PIN-GAUGE-CONTENT**: *the canonical traceless
`u(1)` direction supplied by the graph-first construction is gauged, and the
matter carrier is completed by an opposite-chirality (RH) SU(2)-singlet template
(chirality stipulated, not the naive CPT mirror).* Conditional on it, the full
one-generation ABJ arithmetic — already banked as exact identities — discharges,
feeding the `anomaly_forces_time` lower bound (`d_t` odd) and thence the (3,1)
signature.

---

## 1. The two walls (exact statements as they stand on `main`)

`ANOMALY_FORCES_TIME_THEOREM.md` is a **bounded** conditional bridge. Its premise
table declares five premises; two of them sit squarely in the
`MINIMAL_AXIOMS_2026-06-05.md` open gate **"gauge group / particle content /
species"** (the Quantum axiom's text explicitly excludes "species
identification, gauge group, particle content"). Those two are this note's
cluster:

| Wall | As declared in the theorem | What the cited source deliberately does NOT supply |
|---|---|---|
| **P-HY** | "`Y_like` is the anomaly-relevant `U(1)` hypercharge of the emergent gauge theory, giving LH content `(2,3)_{+1/3} + (2,1)_{-1}`" | `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md` supplies the traceless eigen-direction with spectrum `{+1/3×6, -1×2}` but its Boundary section **explicitly excludes** "anomaly-complete `U(1)_Y`", electric charge, RH completion. It is a structural eigenvalue surface, *not a claim that the direction is gauged/dynamical.* |
| **P-COMP** | "the anomaly-cancelling completion is opposite-chirality SU(2)-singlet (no anomaly-free extension that avoids a second chirality class is admitted); SM branch `(4/3,-2/3,-2,0)` is the computed existence witness" | The theorem uses only the *existence* of the completion. The completion's **chirality** and its **shape** (RH SU(2)-singlet template) are declared boundaries — the arithmetic is banked, the *template's existence as a chiral object* is not derived. |

**Sibling premises (out of this note's cluster, handled elsewhere in the lane):**
P-ABJ (the ABJ anomaly-to-inconsistency implication; route (c) flagged SK-2 as a
possible no-axiom crack on an imbalanced complex), P-REC (taste/single-Dirac
selector), and the inherited B-AXIS cap (Cluster 1). This note discharges P-HY
and P-COMP and shows how, *together with the already-banked exact arithmetic and
the sibling premises*, the lower-bound half of the `(3,1)` chain follows.

**Fanout.** `anomaly_forces_time_theorem` carries `transitive_descendants = 1049`
(`docs/audit/data/load_bearing_summary.json`); the native-gauge cone is
`native_gauge_closure_note = 1361`. P-HY and P-COMP are the two gauge/content
premises gating the `d_t = 1`, signature-(3,1) conclusion and the
one-generation matter cone. This is the **highest-fanout** cluster of the three
in the block-wide map (`.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`,
Cluster 3).

---

## 2. Skeptical no-new-axiom re-attack FIRST (per "don't believe the no-gos")

Before proposing any axiom, both walls were attacked from the current surface.
The runner's **HALF A** is that attack. It does **not** assume the no-gos; it
tries to crack them and confirms they still wall.

### 2.1 P-HY: can "is-gauged" be derived from the supplied carrier? — NO

`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`
already establishes that, *given* the supplied `C³⊗C²` carrier, the symmetry
**algebra** is `su(3) ⊕ su(2) ⊕ u(1)`, but the **gauging selection** (which
symmetry is dynamically gauged) is an **open gate**: four candidate
discriminators are each blind or one-sided. The runner reproduces all four as a
fresh skeptical re-attack (runner block `[A1]`):

1. **Maximality** is blind: an irreducible action has commutant `C·I` (dim 1)
   for *both* the dim-12 candidate algebra and a full irreducible `u(6)`-type
   set, so maximality cannot pick the gauged subalgebra (runner: `comm(su3)=1`,
   `comm(irr6)=1`).
2. **The `d_{abc}` cubic invariant** is a one-sided *filter*, never a selector:
   `su(2)` has `d_{abc}≡0`, `su(3)` has `d_{abc}≠0` (runner: `|d|_{su2}=0`,
   `max|d|_{su3}=0.289`). It tags which factor *can* be anomalous; it does not
   say a `U(1)` eigen-direction *is gauged*.
3. **The chirality grading** `ε` **commutes with the color generators** (runner:
   `max‖[ε,T]‖ = 0`), so it is blind to which factor is chirally gauged.
4. **The reality bilinear** distinguishes the complex color triplet (`3≠3̄`, not
   self-conjugate) from a real (spin-1) vector (self-conjugate) — runner: color
   not self-conj, spin-1 self-conj — but this separates color from a real
   direction; it does **not** select the `Y_like` `U(1)` as gauged.

**Verdict:** the published discriminators do not force "`Y_like` is gauged." The
gate note is explicit it does *not* assert a no-go (no N1–N8 walk), so this is an
**open gate**, not a proven impossibility — but the natural no-axiom routes fail.
P-HY does not crack from the current surface.

### 2.2 P-COMP: can a native chiral RH template be constructed? — NO (vector-like trap)

This is precisely where **block02 killed the Hamming-odd native-RH candidate**.
The runner reproduces the two traps that defeat a no-axiom completion (runner
blocks `[A2]`, `[A3]`):

- **Vector-like trap #1 (naive CPT mirror).** Completing the LH content by adding
  the CPT image of every LH field (its RH Dirac partner) *does* cancel all six
  anomaly conditions — but the resulting spectrum **equals its own CPT
  conjugate**, i.e. it is **vector-like** (non-chiral). A vector-like completion
  is chirally *inert*: it supplies **no second chirality class** (runner `[A2]`:
  all six vanish AND `is_vectorlike = True`). This is the lesson the task
  flags: *a naive CPT-mirror gives a vector-like, not a chiral, completion.*
- **Vector-like trap #2 (native taste-cube complementation).** The only native
  "RH-like" map on the taste cube is charge conjugation `c(b)=1-b`, which sends
  Hamming level `L_k → L_{3-k}` (runner `[A3]`, from
  `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`
  H7). Its single-bond chirality realization `γ₅ = diag(ω_A, ω_B)` admits a
  **trivial** survivor `ω_A = ω_B` (`γ₅ = ±I`) — vector-like matter — that is
  admissible on `{Lattice, Quantum, Record}` (runner: ≥2 inequivalent classes,
  from `STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06`,
  which proves `ε(x)` is a **free selector** until the chiral anticommutation
  `{D,γ₅}=0` is *imposed*). So an opposite-chirality RH template is **not forced**.

- **The wall is real, not vacuous.** The LH content **alone is anomalous** —
  three nonzero traces `Tr[Y³]=-16/9`, `Tr[SU3²Y]=+1/3`, `SU3³=+2` (runner
  `[A4]`, exact rational arithmetic). So a completion is genuinely *required*;
  but every native completion is vector-like (above), hence no *chiral*
  completion is forced. P-COMP does not crack from the current surface.

---

## 3. The candidate primitive (minimal, weakest sufficient)

> **PIN-GAUGE-CONTENT (candidate framework primitive — UNADOPTED).**
> The emergent matter sector is a **gauged chiral gauge theory** with:
>
> **(i) [P-HY]** the canonical traceless `u(1)` eigen-direction `Y_like` supplied
> by the graph-first construction (`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_…`)
> **is a gauged `U(1)`** of the emergent theory (dynamical, not a global label);
> and
>
> **(ii) [P-COMP]** the matter carrier is completed by an **opposite-chirality
> (right-handed) SU(2)-singlet template** — i.e. the completion's **chirality is
> stipulated to be opposite to the LH doublet content** (it is the chiral
> completion, *not* the vector-like CPT mirror), with the neutral singlet
> `Y_{νR}=0`.
>
> `hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
> the actual current surface."`

### 3.1 Why chirality must be stipulated precisely (the block02 caveat)

The runner's **falsification leg F3** verifies the load-bearing subtlety: the
naive CPT-mirror completion **cancels all six anomalies but is chirally inert**
(vector-like). Therefore "the completion exists" is **not enough** — a primitive
that only asserted "a completion exists" would be satisfied by the vector-like
mirror, which gives **no second chirality class** and hence **no `d_t`-odd lower
bound**. The primitive must say **opposite-chirality**. This is exactly the
specification block02 showed is required (naive CPT-mirror → vectorlike). The
runner's **B2** confirms the stipulated RH template is genuinely chiral (its
spectrum ≠ its CPT conjugate) and differs from the inert mirror.

### 3.2 Minimality — what PIN-GAUGE-CONTENT does and does NOT grant

- **It grants only:** (i) one abelian factor's *gauged* status, and (ii) the
  *chirality and SU(2)/SU(3) template class* of the completion. Both land in the
  single open gate "gauge group / particle content / species" that the minimal-
  axioms memo already declares **outside** axiom content (so this is not a §1
  reword of an existing axiom — it adds content the memo says is absent).
- **It does NOT grant:** the *values* of the RH hypercharges (those are **forced
  by the SHIFT relation and banked exactly** — see §4; the primitive supplies
  only the *template class*, not the numbers); the branch convention `Y_{νR}=0`
  vs `Y_{eR}=0` (a named **discrete convention**, runner F2, not part of the
  axiom); the number of generations; `n_color = 3` (graph-first SU(3) lane); the
  non-abelian content (already retained in `NATIVE_GAUGE_CLOSURE_NOTE.md`); P-ABJ
  (sibling, possibly SK-2-crackable); P-REC; any coupling, mass, or mixing.
- **It is the weakest sufficient addition** because the *arithmetic* and the
  *non-abelian algebra* are already on the surface; only the **gauged predicate**
  and the **chirality-class predicate** are missing, and PIN-GAUGE-CONTENT
  supplies exactly those two predicates and nothing numerical.

### 3.3 Splittability

PIN-GAUGE-CONTENT can be split into **P-HY-gauging** (clause (i)) and
**P-COMP-chirality** (clause (ii)) if the owner wants finer granularity; they sit
in the same gate and are naturally one science-level decision ("the emergent
matter is the chiral SM-shaped gauged sector"). The block-wide map (Cluster 3)
records the further option of folding the sibling P-REC/FS statistics premises
into the same content decision; this note keeps the cluster to the two
gauge/content predicates it can discharge cleanly.

### 3.4 Consistency with retained no-gos (no contradiction)

A new axiom must **add**, never contradict a retained result. PIN-GAUGE-CONTENT
is consistent with every retained no-go in the chain:

- `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (per-site `γ₅` impossible in
  `M₂(C)`): PIN-GAUGE-CONTENT does **not** assert per-site chirality; the chiral
  grading it stipulates is realized on the *taste-reconstructed* Dirac factor
  (the P-REC sibling), exactly the structural opening the staggered grading uses.
- `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` (the naive `ε`-index
  vanishes on equal even tori): PIN-GAUGE-CONTENT touches the **gauge content /
  chirality template**, not the lattice index route; it neither asserts nor
  needs a nonzero square-block `ε`-index, so no collision.
- `REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07` (Record cannot source
  chirality): consistent — PIN-GAUGE-CONTENT supplies chirality as a *gauge-
  content* primitive, **not** via the Record axiom; it explicitly does the thing
  Record is forbidden to do, which is why a *separate* primitive is the right
  vehicle.
- `FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_PHYSICAL_NARROW_THEOREM_NOTE_2026-06-08`
  (absolute flavor handedness is gauge): consistent and orthogonal — that result
  is about the *generation-sector* orientation `sign(Δ)`; PIN-GAUGE-CONTENT is
  about the *matter-content chirality class* (LH-doublet vs RH-singlet), a
  distinct `Z₂` (cf. `CHIRAL_CONTENT_IS_THE_EPSILON_D_CHIRALITY_IMPORT…_2026-06-08`,
  which proves these orientation data are distinct objects).

---

## 4. Conditional derivation (the runner's HALF B) — what discharges

**All results in this section carry `hypothetical_axiom_status: conditional on
accepted new axiom; not retained.`** They re-bank, on the conditional surface,
exact identities that already exist as theorems
(`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10`,
`RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_NOTE_2026-05-02`); the *novelty here is
the discharge of the two content premises*, not the arithmetic.

**B1 — the chiral RH template cancels all six exactly.** Given (ii), the SM-branch
RH template `(Y_{uR},Y_{dR},Y_{eR},Y_{νR}) = (4/3,-2/3,-2,0)` makes every one of
the six conditions vanish in exact rational arithmetic:
`Tr[Y]=0`, `Tr[Y³]=0`, `Tr[SU3²Y]=0`, `Tr[SU2²Y]=0`, `SU3³=0`, Witten even
(runner B1).

**B2 — the completion is genuinely chiral.** The full one-generation content is
**not** vector-like (spectrum ≠ its CPT conjugate) and is a *different* completion
from the inert mirror — so a genuine second chirality class exists (runner B2).
This is the load-bearing distinction §3.1.

**B3 — closed-form, parametric, existence witness.** The SHIFT relation
`Y_{uR}=a+1, Y_{dR}=a-1, Y_{eR}=b-1, Y_{νR}=b+1` (with `a=1/n_color`, `b=-1`)
yields the SM branch at `n_color=3`, and the color-anomaly closed form
`Y_{uR}+Y_{dR}=2a` holds for all `n_color` (runner B3, `nc∈{2,3,5,7}`) — the
completion **exists** parametrically; `n_color=3` returns the witness.

**B4 — gauging makes cancellation a consistency demand → lower bound.** With (i)
[`Y_like` gauged], the three nonzero LH traces are **gauge** anomalies (not
global decorations), so their cancellation is a genuine **consistency**
requirement — this is the conditional upgrade that lets the sibling P-ABJ bite.
The runner verifies LH-only gauge anomalies are nonzero while the completed gauge
anomalies are zero (B4). Combined with the genuine second chirality class (B2),
the retained even-dimension Clifford theorem
(`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`) forces
`d_s + d_t` even; with `d_s = 3`, **`d_t` is odd (≥ 1)** — the lower-bound half of
`ANOMALY_FORCES_TIME_THEOREM.md`. (The `d_t ≤ 1` cap is supplied separately by
the single-clock B-AXIS premise / Cluster 1; intersecting gives `d_t = 1`,
signature `(3,1)`.)

**Conditional derivation sketch the runner verifies (end to end):**

```text
PIN-GAUGE-CONTENT (i): Y_like gauged
   => the three computed LH anomaly traces (Tr[Y^3]=-16/9, Tr[SU3^2 Y]=+1/3,
      SU3^3=+2) are GAUGE anomalies => their nonvanishing is an inconsistency
      (with the sibling P-ABJ implication) => a completion is MANDATORY.
PIN-GAUGE-CONTENT (ii): opposite-chirality RH SU(2)-singlet template
   => the completion is the CHIRAL template (not the vector-like CPT mirror),
      so a genuine second chirality class exists;
   => its banked closed form (SHIFT) cancels all six conditions exactly
      (SM branch (4/3,-2/3,-2,0) at n_color=3, existence witness);
   => [retained EVEN Clifford theorem] d_s + d_t even; with d_s = 3, d_t ODD => d_t >= 1.
Intersect with the single-clock cap d_t <= 1 (B-AXIS / Cluster 1) => d_t = 1,
signature (3,1).
hypothetical_axiom_status: conditional on accepted new axiom; not retained.
```

**Falsification legs (so the discharge is non-vacuous).**
F1: a wrong completion (`Y_{νR}=1`) FAILS cancellation (runner: `Tr[Y]=-1`).
F2: the `e_R ↔ ν_R` relabelling is the *only* other anomaly-consistent branch —
a named discrete convention, **not** a second axiom.
F3: the vector-like mirror cancels anomalies but is chirally **inert** → no
second chirality class → no `d_t`-odd lower bound (this is *why* the primitive
must stipulate chirality, §3.1).

---

## 5. Walls discharged + fanout unlocked (conditional)

| Wall | Discharged by | Fanout unlocked (conditional) |
|---|---|---|
| **P-HY** (`Y_like` is gauged) | PIN-GAUGE-CONTENT clause (i) | the gauge-content half of `anomaly_forces_time_theorem` (`td=1049`); the native-gauge matter cone (`native_gauge_closure_note td=1361`, abelian/charge half) |
| **P-COMP** (RH-template existence, chiral) | PIN-GAUGE-CONTENT clause (ii) | the completion / chirality half of `anomaly_forces_time_theorem`; the one-generation matter-content cone (RH singlet template, electric-charge set downstream) |

Together these are the two gauge/content premises gating `d_t = 1` / signature
`(3,1)` and the one-generation matter cone — the **largest** of the three
clusters in the block-wide map. The sibling P-ABJ (route (c), SK-2), P-REC, and
B-AXIS premises remain; this note discharges only the two content predicates it
can clear cleanly while showing the lower-bound half follows.

---

## 6. Policy conformance (`docs/audit/AXIOM_MINIMALITY_POLICY.md`)

- **§1 disallowed moves — not triggered.** This is **not** a reword of Lattice /
  Quantum / Record (it adds content the minimal-axioms memo declares *outside*
  axiom content), and it is **not** an in-lane "if we just accept X, lane Y
  closes" adoption — it is recorded here as an **unmade science-level decision**
  per §1 final bullet and §4.
- **§4 workflow — followed.** The work lands as a bounded boundary note
  documenting *what would close under the proposed primitive* (this note), the
  proposed primitive is recorded as an explicit decision awaiting human input,
  and **nothing is added to `axiom_premise_nodes.json`** by this lane.
- **§6 — owner approval required.** PIN-GAUGE-CONTENT chain-satisfies nothing
  until an explicit owner approval is recorded in §6 of the policy and in the
  machine registry. This note requests that governance decision; it does not make
  it.

---

## 7. What this note does NOT do

- Does **not** adopt PIN-GAUGE-CONTENT, set any audit verdict, or promote any
  downstream surface.
- Does **not** derive P-ABJ (sibling; SK-2 names a possible no-axiom crack on an
  imbalanced/curved complex), P-REC (taste selector), `n_color=3`, the number of
  generations, the branch convention, or any coupling/mass/mixing.
- Does **not** claim the SM gauge group is *forced from the axioms*; it isolates
  the **gauged predicate** and the **chirality-template predicate** as the
  precise missing content and shows their consequences conditionally.
- Does **not** consume any PDG value, fitted constant, or empirical comparator.

---

## 8. Sources read (load-bearing for the argument, not adopted)

- `ANOMALY_FORCES_TIME_THEOREM.md` — P-HY, P-COMP rows; LH traces; SM branch.
- `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md` — `Y_like`
  eigenvalue surface (explicitly not anomaly-complete / not gauged).
- `NATIVE_GAUGE_CLOSURE_NOTE.md` — retained non-abelian content (context).
- `GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`
  — the four gauging-selection discriminators (P-HY skeptical re-attack).
- `STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md` —
  `ε(x)` is a free selector; the vector-like (`γ₅=±I`) survivor.
- `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`
  — charge conjugation `c: L_k → L_{3-k}` (vector-like trap #2 / block02 lesson).
- `ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`,
  `RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_NOTE_2026-05-02.md` — the exact
  banked arithmetic re-verified conditionally.
- `CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md` —
  retained EVEN theorem (the `d_t`-odd lower-bound step).
- `MINIMAL_AXIOMS_2026-06-05.md`, `docs/audit/AXIOM_MINIMALITY_POLICY.md` —
  current surface and policy.

---

## 9. Reproduce

```bash
python3 scripts/axiom_update_proposal_gauge_content_2026_06_20.py
# expect: TOTAL: PASS=21 FAIL=0
```

numpy + stdlib (`fractions`), deterministic, finite-dimensional throughout. HALF
A re-attacks the no-axiom surface (the walls are genuine); HALF B verifies the
conditional discharge; the falsification legs confirm non-vacuity and that
chirality must be stipulated. The runner adopts **no axiom** and sets **no
status**.
