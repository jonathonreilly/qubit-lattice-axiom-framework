# Color depolarization (ADM-2): the three mapped mechanisms collapse to two gauge-structure admissions

**Tier (branch-local, audit-pending):** bounded_theorem (consolidation). NO hat discharged.
**Campaign:** gauge-link / color-einselection dynamics (four hats: ADM-1, R1 link
generator, R2 link-measure delivery, blocking isometry).
**Runner:** `scripts/frontier_color_depolarization_adm2_admission_collapse_2026_06_09.py`
(exact finite-dimensional linear algebra on `C^3` and `C^3 (x) C^3`; `TOTAL: PASS=24
FAIL=0`; random unitary / SU(3) witnesses for already-proven identities, no Monte-Carlo
fit in the logic path; memory-safe).

## The question consolidated

The campaign reduced the R2 input of the undelivered gauge-link generator to one matter
question (ADM-2): does the matter dynamics depolarize the single-carrier color density
`rho_color` to the color-blind floor `I3/3` on the `C^3` fundamental carrier? Over blocks
04-08 this input was mapped onto **three** distinct depolarization mechanisms, each gated
by a separately-named admission:

- **TWIRL** (block 05; and the landed reading
  `FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION...`, unaudited): an averaging map
  needing a `>=2`-element complementary-frame / multi-instrument average with a **uniform
  weight** Record does not supply.
- **PRIMITIVITY** (blocks 06/07): a single named record frame `B` interleaved with the
  coherent matter color unitary `U`, depolarizing iff the unistochastic matrix
  `S_ij = |<e_i|U|e_j>|^2` is **primitive**.
- **ENTANGLEMENT** (block 08): the partial trace of a **global-`SU(3)`-invariant** joint
  two-carrier matter state, mixed by **Schur**.

Adding a fourth relocation per block is corollary churn. This note consolidates the three
instead: with exact algebra they **collapse to two** irreducible admissions, and **both
coincide with the gauge-structure objects the campaign is trying to induce** — so neither
is supplied by Lattice + Quantum + Record.

## Collapse step 1 — TWIRL is the same admission as PRIMITIVITY

The twirl's load-bearing element is the **uniform** averaging weight: a depolarizing
average lands the marginal exactly on `I3/3` only if its weight is uniform (block 05
noted a non-uniform finite average misses `I3/3`). That uniform weight is supplied by
Quantum, not by Record:

- For **any** unitary `U`, the induced `S_ij = |U_ij|^2` is **doubly stochastic** — rows
  and columns each sum to 1 because the rows and columns of a unitary are unit vectors
  (G1.1). Consequently the uniform vector `(1/3,1/3,1/3)` is stationary for every
  unitary-induced `S` (G1.2), and is the **unique** stationary vector whenever `S` is
  primitive (G1.3). The uniform weight is **pinned by unitarity**, not chosen.
- This is not free: a generic **non-unitary** primitive column-stochastic kick relaxes to
  a **non-uniform** stationary vector (G2.1, G2.2). Only unitarity (double stochasticity)
  forces the floor to be the uniform `I3/3`.

So the twirl mechanism, once its weight is recognized as Quantum-supplied, has exactly the
**same residual** as the primitivity mechanism: a **named record frame `B`** (against which
`S` is defined; `record_formation_not_unconditionally_forced...` = retained_no_go) **plus a
primitive `U`**. And a primitive `S` requires a generic **non-diagonal** `SU(3)` link
`V != I3`:

- Free **color-diagonal** hopping gives `U = e^{i phi} I3`, hence `S = I3` — not primitive,
  no depolarization — and this holds **frame-independently** (a scalar unitary stays scalar
  in every orthonormal frame, so no record-frame choice rescues primitivity; G3.1, G3.2).
- A generic link `V != I3` gives a primitive `S` whose iteration drives a polarized
  `rho_color` to `I3/3` (G3.3); but that depolarizing object **is** a non-diagonal `SU(3)`
  link — `S = |V|^2 != I3`, i.e. off-diagonal connection content (G3.4). The free lane
  (`V = I3`) leaves `rho_color` polarized (G3.5).
- The continuity is exact: a one-parameter family `U(theta)` running from the scalar
  subgroup (`theta = 0`, no connection content) into generic off-diagonal mixing shows the
  depolarization **onset coincides with `U` leaving the color-diagonal sector** — i.e. with
  acquiring local-connection content (G4.1-G4.3).

**Admission (A):** a presupposed **local `SU(3)` connection `V != I3`** (plus a named
record frame `B`). This is precisely the gauge link the campaign seeks to **induce** —
consuming it to drive depolarization is circular.

## Collapse step 2 — ENTANGLEMENT gates on a global Gauss-law admission

Schur delivers `rho_A = I3/3` from a global-invariant joint state (G5.1-G5.3): the
`q`-`qbar` singlet marginal is `I3/3`, and **any** state on `C^3 (x) C^3bar` invariant
under the **global** action `g (x) conj(g)` has marginal `I3/3`. But the step the mechanism
needs — *the realized matter state is a global `SU(3)` singlet* — is **not entailed** by
*observables are `SU(3)`-invariant*:

- A non-singlet (polarized) joint state has a **polarized** marginal (G5.4, `P = 2/3`);
  invariance of the observable algebra constrains only the commutant and leaves the
  superselection sector free. Selecting the singlet sector is a separate **physical-state
  (color Gauss-law) condition**.
- Total color charge is **conserved** under the global/covariant action: the total-color
  Casimir is `0` on the singlet and `> 0` on a charged state (G5.5), and is invariant under
  `g (x) conj(g)` (G5.6). So a charged matter state is **not driven** to the singlet by the
  dynamics — neutrality is an **initial-condition / state-preparation admission**.
- The route is irreducibly multi-carrier: on a single `C^3` the commutant of the `SU(3)`
  generators is exactly one-dimensional (`= C.I3`; exact null-space check G6.1), so a lone
  fundamental admits no invariant pure state and no invariant projector beyond `0, I3` — a
  single isolated carrier cannot self-depolarize.

**Admission (B):** a **global color-singlet / Gauss-law physical-state condition** (global
color neutrality / confinement). The confinement corpus on main is unaudited and imports
scale-setting (`CONFINEMENT_STRING_TENSION_NOTE`, unaudited: Sommer scale + pure-gauge
Monte-Carlo), not axiom-derived.

## Result

The three mapped mechanisms gate ADM-2 color depolarization on exactly **two** admissions:

| Mechanism(s) | Gating admission | What it is |
|---|---|---|
| TWIRL, PRIMITIVITY | (A) presupposed local `SU(3)` connection `V != I3` (+ named frame `B`) | the gauge link the campaign induces (circular to consume) |
| ENTANGLEMENT | (B) global color-singlet / Gauss-law physical-state condition | global color neutrality / confinement (an import; unaudited corpus) |

Both (A) and (B) are precisely the undelivered gauge-structure objects of the campaign,
and neither is supplied by Lattice + Quantum + Record. The twirl's apparently-separate
"uniform averaging weight" admission dissolves into Quantum (unitarity), leaving the twirl gated by (A);
the entanglement route is distinct from a connection (global action alone leaves a
non-neutral marginal polarized, G7.2) and gates on (B).

This **bounds** ADM-2 depolarization as admission-gated across every mechanism mapped this
campaign, and identifies the two gates with the two gauge-structure objects the campaign
exists to deliver. It is the anti-relocation consolidation: it does not add a fourth
admission — it shows the three collapse to two.

## Honest-auditor read / boundaries

- **NO hat discharged.** ADM-1 (static color-frame redundancy), R1 (link generator),
  R2 (link-measure delivery), and the blocking isometry are untouched. The default
  Lattice + Quantum + Record configuration — free color-diagonal hopping on an arbitrary product matter
  state — depolarizes on **neither** lane (G7.1).
- **Not a no-go.** Supplying the named object (a local link) **does** depolarize (G7.4):
  the wall is a missing object on each lane, not an impossibility. The open paths are
  (i) auditing the local-connection forcing of `H_cov` (PR #3332's premise; **unaudited**,
  verify live before any consumption), (ii) a future structural premise that would deliver
  a color Gauss law from Lattice + Quantum + Record, and (iii) the comparatively unworked blocking-
  isometry hat (`record_formation_to_kraus_isometry_bridge...` = unaudited; its load-bearing
  "persistent record dynamics => isometry W" step is open).
- **Conditionality.** The collapse is stated for the named matter family (the two block-01
  hopping Hamiltonians), the supplied `C^3` color carrier, and a named record frame — the
  same conditionality the per-mechanism notes carry.
- **Weight-leak guard.** Every `I3/3` here is **forced** by unitarity or by invariance
  (invariant/unitary input -> `I3/3`; non-invariant / non-unitary input -> polarized;
  G7.3) — never assigned by fiat, staying on the right side of the Fierz
  weight-not-partition reading.
- **Discipline.** No partition map is claimed for the irreducible color triplet; no
  edge/two-site native-color framing; no `r=1/2` or registered value forced; no ST1/ST2
  ranking; no PDG/fitted value consumed; statuses cited at their **live** ledger tier
  (`graph_first_su3` = retained; `record_formation_not_unconditionally_forced` and
  `record_markov_generator_embeddability_boundary` = retained_no_go; confinement corpus,
  #3332, and the block-04..08 per-mechanism notes = unaudited source proposals).

## Citations (status at draft, verify live before reuse)

- `graph_first_su3_integration_note` — retained (global `SU(3)` = commutant, `N_c = 3`).
- `cl3_color_automorphism_theorem` — retained (color algebra support).
- `record_formation_not_unconditionally_forced_by_minimal_axioms...` — retained_no_go
  (the record frame `B` is a named admission).
- `record_markov_generator_embeddability_boundary_2026-06-06` — retained_no_go (Record
  supplies no continuous generator/rate; the depolarizing step must live on the matter
  side).
- Per-mechanism source proposals (unaudited): block-05 multi-frame dichotomy, block-06
  unistochastic-primitivity criterion, block-07 matter-unitary-primitivity-needs-connection,
  block-08 color-neutrality-entanglement, `FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION...`,
  `CONFINEMENT_STRING_TENSION_NOTE` (cited only to state neutrality is not delivered there;
  not consumed).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [confinement_string_tension_note](CONFINEMENT_STRING_TENSION_NOTE.md)
