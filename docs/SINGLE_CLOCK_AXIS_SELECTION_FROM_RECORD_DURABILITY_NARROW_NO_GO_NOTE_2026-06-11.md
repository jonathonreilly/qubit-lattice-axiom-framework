# Single-Clock Axis Selection From Record Durability: Every Retained Candidate Structure Is W-Transportable — Narrow No-Go With a Sharpened Pin

**Date:** 2026-06-11
**Type:** no_go (narrow axis-selection route pruning) + sharpened-pin
support (computed minimal axis-selecting inputs)
**Claim type:** no_go
**Claim scope (narrow):** the single clause left open by the 2026-06-11
hostile re-scope of
[`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
— the **axis-label component of (B-AXIS.2)** (= scope-boundary clause N4):
can the evolution axis be *derived* from some retained structure instead
of declared? This note attacks the two live candidate routes hostilely
and answers **no, with computed witnesses**: every retained candidate
axis-anchoring structure — the OS/GNS reconstruction data, the
record/durability surface, the registration cone, and the
anomaly/chirality chain — is **exactly transported by the conjugated
exchange `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})`** onto an equivalent
structure about the `x_1` axis (transport residuals exactly `0`,
identical spectra, identical positivity status). The compensating
positive content is the **sharpened pin**: the minimal axis-selecting
input is computed to be a single per-axis `Z_2` datum — a
boundary-condition asymmetry (antiperiodic-`τ`/periodic-space breaks `W`
exactly; symmetric BCs restore it exactly) — or an equivalent declared
registration-direction bridge tying the record event order to one
lattice axis. (B-AXIS.1) and (B-AXIS.3) (= N2/N5) are untouched.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; audit verdict and effective status
are set only by the independent audit lane.
**Loop:** science-fix lane 2026-06-11 (B-AXIS follow-up wave).
**Primary runner:**
[`scripts/single_clock_axis_selection_check_2026_06_11.py`](../scripts/single_clock_axis_selection_check_2026_06_11.py)
(expected `TOTAL: PASS=23 FAIL=0`, deterministic, no RNG in any
load-bearing leg, runtime well under 5 minutes).

## 0. Changelog

- **2026-06-11** — initial note. Follow-up to the same-day re-scope that
  demoted axis selection from theorem (old S3) to declared premise
  (B-AXIS). Routes A (record/durability) and B (anomaly/chirality)
  attacked and closed with computed W-transport certificates; sharpened
  pin computed (BC-asymmetry `Z_2` datum suffices; symmetric-BC
  restoration falsification leg; relabeling-invariant kernel-dimension
  discriminator; regulator-extent datum recorded as weaker).

## 1. Question, method, verdict

The re-scoped evolution theorem proved (computed certificate, residual
exactly `0`) that the staggered kinetic surface is invariant under the
axis exchange `W`, so RP-admissibility alone cannot select the temporal
axis; axis selection became the declared premise (B-AXIS). The standing
owner method then demands the hunt: the governing no-gos state their own
escape conditions — find the supplier.

Method: for each retained structure `D_τ` proposed as an axis anchor,
compute its **W-transport** `D_1 := W D_τ W†` on explicit small lattices
and ask whether `D_1` is an *equivalent structure of the same type about
the `x_1` axis*. If yes for every candidate, no retained structure
breaks the exchange and the axis label is underivable from the current
surface (honest narrow no-go); the residual positive deliverable is then
the computed boundary of the no-go — exactly which minimal input breaks
`W`.

**Verdict: narrow no-go.** Every candidate transports exactly
(Sections 3–4). The sharpened pin (Section 5): one per-axis `Z_2`
boundary-condition datum is sufficient and is the minimal computed
axis-selecting input on this surface; a declared registration-direction
bridge is the record-shaped equivalent. B-AXIS.2's axis label therefore
*reduces to* (is derivable given) one such datum, but the datum itself
is not derived here and is not supplied by any retained row.

## 2. Escape-clause mining: what the governing no-gos kill and leave open

Quoted verbatim from the retained boundaries (one hop):

- **`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`**
  (retained_no_go; the row whose clauses became B-AXIS.1–3). Kills:
  "Stone uniqueness is transfer-relative and tau-relative.
  No-second-clock requires a separate axis/transfer uniqueness premise."
  Its named reopening inputs are its checklist clauses:
  - **N2:** "the physical time step / block spacing `tau`;"
  - **N4:** "uniqueness of the reflection-positive axis or transfer
    construction;"
  - **N5:** "exclusion of independent commuting transfer factors if the
    claim says no second clock;"

  This note hunts a supplier for the *axis-label* part of N4 only. It
  supplies none from the retained surface; it sharpens what a supplier
  must contain.
- **`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`**
  (retained_no_go). Kills: deriving a physical boost action from the
  local `M_2(C)` algebra alone; leaves open "derive the
  matter-attachment selector from the framework, or explicitly admit
  it". Relevance here: no boost/Lorentz content may be consumed to
  break the exchange; this note consumes none.
- **`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`**
  (retained_no_go). Kills: SO(4)/continuum-isotropy wording from
  spatial-cubic checks; the salvage premise `c_t = c_s` is now supplied
  by the approved kinetic-isotropy primitive. Relevance: that premise
  makes the surface *more* exchange-symmetric, so it pushes **against**
  any kinetic-coefficient axis discriminator — consistent with this
  note's no-go direction, and no SO(4) wording is used here.
- **`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`**
  (retained_no_go). Kills: clock/rate derivation from record counts —
  "Without the supplied `tau`, the same record history supports many
  inequivalent rates." Leaves open: "a supplied clock can define rates
  for a record stream." Relevance: the post-record event ORDER is
  axis-label-free; tying it to a lattice axis is a supplied bridge —
  this is exactly the record-shaped form of the sharpened pin.

## 3. Inputs (one hop, with exact licenses)

| Input | Where used | License |
|---|---|---|
| The exchange certificate `W M_KS W^T = M_KS` (residual 0) and the declared (B-AXIS.1–3) | the structure under attack; baseline recomputed in runner block [S] | [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) — bounded_theorem, same-lane re-scope; certificate recomputed, not cited blind |
| N2/N4/N5 reopening clauses; transfer-/τ-relativity | Section 2; runner [D] verbatim checks | `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` — retained_no_go |
| Record axiom text: durable registration; supplies no "time metric" | route A; runner [RT-REC] | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — approved axiom memo |
| Formation rule/process not supplied by Record | route A (a forming record does not pick a lattice axis, rate, clock, site selector, or comparable history) | [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) — post-append narrowed no-go |
| Clock map supplied, never derived from counts | route A; the record-shaped pin | [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — retained_no_go |
| (CAP-K) registration cone: (REG-dyn) consumes the framework `H`, (REG-tau) consumes a supplied window | route A circularity check | [`OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md) — bounded_theorem (conditional realization class) |
| Anomaly chain constrains the count `d_t`, "not which axis is temporal" | route B | [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — bounded_theorem (downstream consumer; its own non-circularity text is the kill) |
| Boost-faith and cubic-anisotropy boundaries | Section 2; runner [D] | both retained_no_go, cited above |

No fitted parameters, no observed values, no new axioms, no axiom-file
edits.

## 4. The attack, route by route (computed)

All computations on the antisymmetrized staggered KS hop matrix with
mass `m = 0.3` on the even periodic block `(L_τ, L_1, L_2, L_3) =
(4, 4, 2, 2)` (`N = 64` sites), time-first phases `η_τ = 1, η_1 =
(-1)^{x_τ}, η_2 = (-1)^{x_τ+x_1}, η_3 = (-1)^{x_τ+x_1+x_2}`, exchange
`W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})` (orthogonal; recomputed baseline
residual `0`; the plain swap without the sign field fails by `> 1` —
the certificate is non-trivial).

### 4.1 Route A1 — the OS/GNS asymmetry hypothesis is FALSE (computed)

The strongest version of the record route argued: *the RP reflection of
the retained RP row is temporal by construction of the OS reconstruction
that produces the Hilbert space itself; the spatial "evolution" has no
GNS vacuum/positivity structure unless separately constructed.* The
separate construction is **free, by conjugation**, and the runner
computes it:

- `Θ'_1 := W Θ_τ W^T` is an orthogonal involution supported **exactly**
  on the `x_1` site reflection `x_1 ↦ L−1−x_1` (a *signed* spatial
  reflection — exactly the class staggered RP constructions use);
- the one-particle Euclidean kernel is W-invariant:
  `W M^{-1} W^T = M^{-1}` (residual `~ 2.7e-15`);
- the one-particle OS kernels `G_a := (Θ_a M^{-1})|_{half_a^+}` satisfy
  **exact unitary equivalence** `W_r G_1 W_r^T = G_τ` with `W_r` the
  restriction of `W` to the positive half-spaces (orthogonal, residual
  `~ 1.5e-15`);
- the Hermitian parts have **identical spectra and identical minimum
  eigenvalue**: whatever positivity status the temporal construction
  has, the `x_1` construction has identically.

So the `x_1` axis admits the *same* reflection structure, the *same*
half-space algebra, the *same* OS kernel, and hence (by the fixed note's
Step-3 conjugation argument, of which this is the one-particle computed
instance) the same two-step blocked transfer and GNS reconstruction.
The OS construction anchors nothing: it is built *after* the axis is
chosen, and `W` transports the entire package.

### 4.2 Route A2 — record/durability does not anchor the axis

The Record axiom's durability clause is intrinsically ordered ("Durable
means fixed once registered"). The hostile question: is "the axis along
which records are durable" pinned to the transfer direction by any
retained record row, so that B-AXIS would reduce to "at least one record
exists"? Three kills, one computed and two textual, all at one hop:

1. **Durability is order-relative, and order is unitary-transport
   invariant (computed, class A).** "Fixed once registered, never
   un-registered" is operator-order monotonicity of the registered
   record counter, `N_0 ≤ N_1 ≤ … ≤ N_k`. Operator order is invariant
   under unitary conjugation (`A ≤ B ⟺ UAU† ≤ UBU†`); the runner
   verifies on an explicit register chain that the conjugated counter is
   monotone with identical increment spectra. A W-conjugated world has
   W-conjugated records, durable along `x_1`, with identical durability
   structure. Durability cannot distinguish W-related axes.
2. **The record rows are axis-blind by their own text (one hop).** The
   Record axiom supplies no "time metric" (verbatim exclusion). After the
   2026-07-04 append, generic occurrence is axiom content, but the
   formation rule/process, site selector, clock, rate, and comparability
   relation remain outside Record. The clock/rate interface
   (`retained_no_go`) proves the event order carries no metric and — a
   fortiori — no lattice-axis label: "Without the supplied `tau`, the
   same record history supports many inequivalent rates." The post-record
   surface supplies order, counts, and prefixes; the association of that
   order with a lattice
   axis is a *bridge*, never derived. The sharp-record Fisher row and
   the sector-algebra rows are stated on abstract finite sample spaces
   with no lattice axis anywhere in their hypotheses.
3. **The CAP-K registration cone is axis-conditional, hence circular as
   an axis supplier (textual + computed).** Its (REG-dyn) clause
   consumes the framework hopping `H` — downstream of the
   `(T̂², 2a_τ)` supply that B-AXIS declares — and its (REG-tau) clause
   consumes a supplied clock window ("the clock map itself and the
   window value are supplied"). Citing the cone to select the axis
   would consume B-AXIS to derive B-AXIS. Moreover the cone construction
   itself transports (computed): choosing axis `a` as evolution leaves
   the in-slice hop operator `D^{(a)}`; the runner verifies
   `W_sl D^{(1)} W_sl^T = D^{(τ)}` **exactly** (identical spectra), so
   every Lieb-Robinson velocity, cone constant, and registration
   capacity built on the slice dynamics is equal between the two axis
   choices.

### 4.3 Route B — anomaly/chirality is axis-label-blind (computed + the consumer's own text)

The staggered chirality grading `ε(x) = (-1)^{x_τ+x_1+x_2+x_3}` is
exactly W-invariant (`W E W^T = E`, residual `0`) and the chiral
anticommutation `{D_hop, ε} = 0` is preserved under transport — the
chirality structure cannot tell the axes apart. And the anomaly
consumer's own non-circularity section already states the kill: its
steps "constrain only the *count* `d_t` (parity and positivity), not
which axis is temporal"; the fixed note's B-AXIS "references no anomaly
trace, no chirality content". Route B never had axis-label content.

## 5. The sharpened pin (computed minimal axis-selecting inputs)

What WOULD break the exchange? The runner computes the boundary:

- **(PIN-BC) — sufficient, minimal on this surface.** Antiperiodic-`τ` /
  periodic-space boundary conditions break the exchange **exactly**:
  `||W M_ap W^T − M_ap|| = 2√2 > 0` on the canonical block.
  **Falsification leg:** antiperiodic in *both* `τ` and `x_1` restores
  the exact symmetry (residual `0`) — the selecting datum is the **BC
  asymmetry between the axes** (one `Z_2` choice per axis), not the
  antiperiodic wrap itself. And the discrimination is not an artifact of
  testing one intertwiner: with the BC datum supplied, the temporal hop
  sector has **trivial kernel** while the periodic spatial sector has a
  32-dimensional kernel — a relabeling-invariant, so *no* exchange map
  of any kind can identify the sectors. Repo surfaces that already use
  antiperiodic-`τ`/periodic-space conventions (e.g. the P2 trace-bridge
  row, the `g_bare` obstruction row) carry exactly this datum — as a
  *setup convention chosen after the axis*, not as a derivation of it;
  a future "antiperiodic temporal BC selection row" (named as a
  candidate supplier by the fixed note) would have to derive the
  asymmetry, not assume it.
- **(PIN-REG) — the record-shaped equivalent (declared bridge).** A
  supplied registration-direction bridge: "the realized record history's
  event order is parametrized by lattice axis `μ`". By Section 4.2 this
  is exactly the bridge the clock/rate interface leaves to be supplied;
  given it, the axis label follows trivially. It is record-adjacent but
  **not** an axiom consequence (Record supplies occurrence but no axis,
  clock, rate, or formation rule), so it is a declared input, not an
  axiom change.
- **(PIN-EXT) — weaker, regulator-level.** Asymmetric extents
  `L_τ ≠ L_1` also discriminate (computed: sector spectral radii differ
  on `(6,4,2,2)`), but extents are finite-block regulator data; this
  datum is recorded and downgraded, not proposed.

**What B-AXIS becomes.** Unchanged in count, sharpened in shape:
(B-AXIS.1) (= N2, the supplied `2a_τ`) and (B-AXIS.3) (= N5, no
commuting factor clock) are untouched by this note. (B-AXIS.2) (= N4)
splits into (i) the transfer-construction choice, which remains
declared, and (ii) the **axis label**, which this note proves is
underivable from the retained record/anomaly/RP surface but *derivable
given one per-axis `Z_2` BC-asymmetry datum or one declared
registration-direction bridge* — the computed minimal supplier shape
for any future axis-selection row.

## 6. Consistency with retained no-gos (declared, checked)

- **Scope boundary (retained_no_go):** consumed, not contradicted — its
  N2/N4/N5 clauses are quoted verbatim and remain premises; this note
  prunes candidate N4 suppliers and sharpens the supplier shape, exactly
  the no-go's own discipline ("a separate axis/transfer uniqueness
  premise" is still required; we now know its minimal content).
- **Boost-faith no-go:** respected — no boost action, no Lorentz
  content, no matter-attachment selector is consumed or derived.
- **Cubic-anisotropy gate:** respected — no SO(4) wording; the
  `c_t = c_s` primitive is used only in the direction it licenses
  (more exchange symmetry, supporting the no-go).
- **Clock/rate interface:** respected and consumed — no rate, no clock,
  no axis is derived from record counts; the pin's record-shaped form is
  the *supplied-bridge* opening that the no-go itself names.
- **Record-formation no-go:** respected — nothing here asserts records
  form; route A2 is conditional on records existing and fails anyway.

## 7. No-Go Discipline Gate

**Status:** PASS. The no-go is narrow: it closes only the enumerated
retained candidate routes for the axis-label component of B-AXIS.2 on the
staggered kinetic surface.

**N1 — alternative route enumeration.**

| route | attempt | outcome |
|---|---|---|
| OS/GNS reconstruction | Use RP positivity/GNS data to privilege `tau`. | ATTEMPTED: `W` transports the reflection, covariance, half-space kernel, spectra, and positivity status to `x_1`. |
| Record durability | Use durable record order as the physical axis. | ATTEMPTED: durability is operator-order monotonicity, and unitary transport preserves it; Record supplies no time metric. |
| CAP-K registration cone | Use finite-speed registration capacity as axis selector. | ATTEMPTED: the cone consumes `H` and a supplied clock window, so it is circular as an axis supplier; its slice package transports exactly. |
| Anomaly/chirality | Use chirality/anomaly structure to identify the temporal axis. | ATTEMPTED: `epsilon(x)` and chiral anticommutation are `W`-invariant; the anomaly consumer constrains count, not axis label. |
| BC-asymmetry / registration-direction supplier | Break `W` with an extra datum. | ATTEMPTED: succeeds if supplied, but the per-axis `Z_2` BC asymmetry or registration-direction bridge is not derived by any retained row named here. |

**N2 — wall-independence audit.** The collapsed residual is one wall:
the axis-label datum for B-AXIS.2. The BC-asymmetry form and the
registration-direction form are alternative presentations of the same
axis-label supply, not independent walls. B-AXIS.1 (`2a_tau`) and
B-AXIS.3 (no commuting factor clock) remain outside this note's scope.

**N3 — hidden-wall scan.** Hits on "by construction," "registered,"
"canonical," and "standard" were classified. OS/GNS and CAP-K
construction language is cited or computed; Record/registration language
is bounded by the Record axiom, record-formation no-go, clock/rate
interface, and CAP-K clauses; finite linear algebra and finite GNS/Schur
uses are admitted methodology and additionally computed in-runner. The
BC-asymmetry and registration-direction requirements are explicit walls,
not hidden assumptions.

**N4 — residual matching.** The matched residual is only the axis-label
part of scope-boundary N4. The record/rate no-go matches the absence of
axis label in event order; the anomaly note matches count-not-label; the
boost and cubic-anisotropy no-gos are guardrails against importing
Lorentz/SO(4) content, not witnesses for the axis-label closure.

**N5 — rhetoric audit.** "Underivable" means underivable from the
retained record/anomaly/RP candidate structures enumerated here, on the
tested staggered kinetic surface. It does not mean no future supplier can
derive an axis label, no continuum theorem exists, or no non-lattice
unitary route exists beyond the explicit PIN-BC kernel invariant.

**N6 — partial-closure path scan.** Two partial-closure paths are named:
a derived per-axis BC-asymmetry row and a declared/derived
registration-direction bridge. Either would retire this no-go without a
new axiom if landed and audited. The approved kinetic-isotropy primitive
was checked separately; it strengthens exchange symmetry and does not
select an axis.

**N7 — steelman.** A hostile reviewer could argue that the repo already
uses antiperiodic temporal BCs, so the axis is effectively selected by
existing practice. Response: those rows use the datum as a setup
convention after an axis is named; they do not derive the asymmetry. This
note makes that route precise so a future supplier can retire the wall.

**N8 — cross-cycle echo.** Similar residuals appear in the single-clock
scope boundary, post-record clock/rate interface, cubic-anisotropy gate,
and boost-faith no-go. The kinetic-isotropy primitive is the example of a
prior convention-like residual retired by explicit owner-approved
premise registration; the same mechanism could apply here if a BC or
registration-direction supplier is explicitly approved and audited.

## 8. Honest status

**Narrow no-go.** The negative claim quantifies over the *retained
candidate structures enumerated in Section 4* (OS/GNS reconstruction
data, record/durability rows, the registration cone, the
anomaly/chirality chain) on the staggered kinetic surface — not over
all conceivable future rows. The positive content (the pin) is a
computed sufficiency certificate plus a falsification leg, not a
selection: the BC-asymmetry datum is exhibited as sufficient and
minimal-on-this-surface, never asserted as framework-supplied.

**Not in scope.**

- Deriving the BC asymmetry, the registration-direction bridge, or any
  axis label (that would be the future supplier row).
- B-AXIS.1 (the `τ` value) and B-AXIS.3 (commuting factor clocks) —
  untouched, per the scope boundary.
- Any unconditional no-second-clock claim; any RP positivity
  derivation; any continuum/Wightman content.
- Quantification over non-lattice (fully general unitary) exchange
  maps, except where the kernel-dimension invariant applies (PIN-BC,
  where the discrimination IS fully general).

**Honest claim-status fields (audit-lane handoff):**

```yaml
proposed_claim_type: no_go
proposed_claim_scope: |
  Narrow no-go: on the staggered kinetic surface, every retained
  candidate axis-anchoring structure (OS/GNS reconstruction data,
  record/durability rows, the CAP-K registration cone, the
  anomaly/chirality chain) is exactly transported by the conjugated
  exchange W = P_{tau<->1} diag((-1)^{x_tau x_1}) onto an equivalent
  x_1-axis structure (computed: transport residuals 0, identical
  spectra, identical positivity status, durability order preserved),
  so the axis-label component of B-AXIS.2 (= scope-boundary N4) is not
  derivable from the current retained surface. Sharpened pin
  (computed): one per-axis Z_2 boundary-condition asymmetry datum
  (antiperiodic-tau/periodic-space) breaks the exchange exactly, with
  a relabeling-invariant kernel-dimension discriminator and an exact
  symmetric-BC restoration falsification leg; a declared
  registration-direction bridge is the record-shaped equivalent.
  B-AXIS.1/B-AXIS.3 untouched.
proposed_load_bearing_step_class: C (computed W-transport certificates
  on explicit small lattices; the durability-monotonicity transport is
  class A operator algebra; the textual one-hop kills are class B).
status_authority: independent audit lane only
actual_current_surface_status: no-go (axis-label derivation routes from
  the retained record/anomaly/RP surface) + support (sharpened pin)
trace_class: negative_route_pruning
reachability_to_target: prunes, and specifies the minimal supplier
  shape for the future axis-selection row
conditional_surface_status: exact-support for axis selection GIVEN a
  per-axis BC-asymmetry datum or a registration-direction bridge
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This prunes axis-label derivations from the retained surface and computes the pin; it is not a status promotion proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 9. Reproduction

```bash
python3 scripts/single_clock_axis_selection_check_2026_06_11.py
```

Expected output (matches stdout):

```text
========================================================================
SINGLE-CLOCK AXIS SELECTION: W-TRANSPORT AUDIT (2026-06-11)
========================================================================

Question: does any retained structure (record/durability, OS/GNS,
registration cone, anomaly/chirality) break the tau<->x_1 exchange
W = P_{tau<->1} diag((-1)^{x_tau x_1}), so the evolution axis could be
derived instead of declared (B-AXIS)?  Answer computed below: NO —
every candidate transports exactly; the sharpened pin is one per-axis
Z_2 datum (BC asymmetry) or an equivalent registration-direction bridge.

  surface: block (4, 4, 2, 2), N = 64 sites, mass = 0.3, periodic BCs

------------------------------------------------------------------------
[S] BASELINE: the exact tau<->x_1 exchange certificate (recomputed)
------------------------------------------------------------------------
  [PASS][C] W = P_{tau<->1} diag((-1)^{x_tau x_1}) is orthogonal  -- N = 64 sites, mass = 0.3
  [PASS][C] exact surface invariance: ||W M_KS W^T - M_KS|| = 0 (periodic BCs)  -- resid = 0.00e+00
  [PASS][D] falsifier: plain axis swap WITHOUT the sign field fails  -- resid = 5.6569 >> 0 (the certificate is non-trivial)

------------------------------------------------------------------------
[RT-RP] ROUTE A1: does the OS/GNS construction anchor the axis? (computed: NO)
------------------------------------------------------------------------
  [PASS][C] W theta_tau W^T is an orthogonal involution supported EXACTLY on the x_1 site reflection x_1 -> L-1-x_1 (a signed spatial reflection)  -- involution resid = 0.0e+00, |support - R_1| = 0.0e+00
  [PASS][C] the covariance (one-particle Euclidean kernel) is W-invariant: W M^{-1} W^T = M^{-1}  -- resid = 2.69e-15
  [PASS][C] the x_1-axis OS kernel is EXACTLY unitarily equivalent to the temporal one: W_r G_1 W_r^T = G_tau (W_r = W restricted to halves, orthogonal)  -- ||W_r W_r^T - I|| = 0.0e+00, transport resid = 1.49e-15
  [PASS][C] identical Hermitian spectra and identical minimum eigenvalue: WHATEVER positivity status the tau construction has, the x_1 construction has identically — the 'no spatial GNS structure' escape is FALSE  -- max |spec diff| = 6.7e-16, min eig (both) = -1.648227

------------------------------------------------------------------------
[RT-REC] ROUTE A2: does record durability anchor the axis? (textual + computed: NO)
------------------------------------------------------------------------
  [PASS][B] Record axiom is axis-blind by its own text: a record supplies no 'time metric' (verbatim in the exclusion list)  -- MINIMAL_AXIOMS_2026-06-05.md
  [PASS][B] formation rule/process is not supplied by Record: occurrence is axiom content, but no axis, clock, rate, site selector, or comparable history follows from it  -- post-append formation-rule no-go quoted
  [PASS][B] the clock map is supplied, never derived from records (retained_no_go): 'Without the supplied `tau`, the same record history supports many inequivalent rates' — the event ORDER carries no lattice-axis label  -- clock/rate interface quoted
  [PASS][B] the CAP-K registration cone is axis-CONDITIONAL, not axis-selecting: its dynamics clause (REG-dyn) consumes the framework H and its window (REG-tau) consumes a supplied clock — both downstream of B-AXIS, so citing it for axis selection would be circular  -- CAP-K note clauses present
  [PASS][A] durability ('fixed once registered, never un-registered') is operator-order monotonicity of the record counter, and operator order is unitary-transport invariant: the conjugated counter is monotone with the same increment spectra — durability CANNOT distinguish W-related axes  -- monotone before/after = True/True, max increment-spec diff = 8.9e-16
  [PASS][C] the slice/registration-cone package transports exactly: W maps the x_1-as-evolution in-slice hop operator onto the tau-as-evolution one (W_sl D^(1) W_sl^T = D^(tau), identical spectra) — every cone constant, LR velocity, and CAP-K capacity built on the slice dynamics is equal  -- slice dim = 16, transport resid = 0.0e+00, max |spec diff| = 0.0e+00

------------------------------------------------------------------------
[RT-ANOM] ROUTE B: does the anomaly/chirality chain pick the axis? (NO: count, not label)
------------------------------------------------------------------------
  [PASS][C] the staggered chirality grading eps(x) = (-1)^{sum x_mu} is exactly W-invariant and the chiral anticommutation {D_hop, eps} = 0 is preserved: the chirality structure is axis-label-blind  -- ||W E W^T - E|| = 0.0e+00, ||{A,E}|| = 0.0e+00
  [PASS][B] the anomaly consumer constrains the COUNT d_t, 'not
   which axis is temporal' (its own non-circularity section), and the fixed note's B-AXIS 'references no anomaly content' — route B supplies no axis label by both notes' own text  -- both texts quoted

------------------------------------------------------------------------
[PIN] THE SHARPENED PIN: what WOULD break the exchange (computed witnesses)
------------------------------------------------------------------------
  [PASS][C] antiperiodic-tau / periodic-space BCs break the exchange EXACTLY: ||W M_ap W^T - M_ap|| > 0 — one per-axis Z_2 BC datum suffices to select the axis on this surface  -- resid = 2.828427 (= 2*sqrt(2) on this block)
  [PASS][C] falsification leg: antiperiodic in BOTH tau and x_1 RESTORES the exact exchange symmetry — the axis-selecting datum is the BC ASYMMETRY between the axes, not the antiperiodic wrap itself  -- resid = 0.0e+00
  [PASS][C] relabeling-invariant discriminator: with antiperiodic-tau the temporal hop sector has TRIVIAL kernel while the periodic x_1 sector has a nonzero kernel — no exchange map of any kind (signed, conjugated, or otherwise) can identify the two sectors once the BC datum is supplied  -- dim ker: temporal(apbc) = 0, x_1(pbc) = 32
  [PASS][C] asymmetric extents L_tau != L_1 also discriminate (sector spectral radii differ) — but extents are finite-block regulator data, declared, not framework axioms; recorded as the weaker regulator-level datum  -- max|spec|: temporal = 1.7321, x_1 = 2.0000 on (6,4,2,2)
  [PASS][D] the pin addresses ONLY the axis-label clause of B-AXIS.2 (= N4): B-AXIS.1 (the supplied 2a_tau, = N2) and B-AXIS.3 (no commuting factor clock, = N5) remain declared premises exactly per the scope boundary; the fixed note's candidate-supplier sentence names the BC route this pin sharpens  -- B-AXIS clauses + candidate-supplier sentence present

------------------------------------------------------------------------
[D] COMPOSITION DISCIPLINE (scope boundary consumed, not contradicted)
------------------------------------------------------------------------
  [PASS][D] scope-boundary clauses consumed verbatim: N2 (time step), N4 (axis/transfer uniqueness), N5 (commuting factors), and 'Stone uniqueness is transfer-relative and tau-relative'  -- N2/N4/N5 + repair line present
  [PASS][D] this note is a narrow no-go that does NOT claim the axis is derived: honest-outcome strings present, forbidden closure strings absent  -- wording guards hold
  [PASS][D] no-go is consistent with the boost-faith and cubic-anisotropy boundaries: no boost action is derived (no Lorentz content consumed), and no SO(4) wording is used (the c_t = c_s primitive makes the surface MORE exchange-symmetric, which this note's direction respects)  -- one-hop boundary texts present

========================================================================
TOTAL: PASS=23 FAIL=0
========================================================================
```

A passing run supports only: (i) the recomputed exchange baseline with
its falsifier; (ii) the exact W-transport of the OS/GNS, slice/cone, and
chirality structures and the unitary invariance of durability order;
(iii) the one-hop textual kills; (iv) the pin's sufficiency,
restoration, and invariant-discriminator legs. It does **NOT** derive
the axis, retire B-AXIS, assert the BC datum is framework-supplied, or
promote any row.

## 10. Citations

- target/fixed note (bounded_theorem, same lane):
  [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
- governing boundaries (retained_no_go):
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md),
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md),
  [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
  [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
- record surface consulted:
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md),
  [`OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md),
  [`SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md`](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)
- anomaly consumer (cross-reference; its own text is the route-B kill):
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
- repo rows carrying the BC-asymmetry datum as a setup convention (not a
  derivation):
  [`P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md`](P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md),
  [`G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18.md`](G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18.md)
- standard external references (theorem-grade, no numerical input):
  Osterwalder-Schrader (1973) *Comm. Math. Phys.* 31, 83;
  Sharatchandra-Thun-Weisz (1981) *Nucl. Phys. B* 192, 205;
  Golterman-Smit (1984) (staggered lattice symmetry context).
