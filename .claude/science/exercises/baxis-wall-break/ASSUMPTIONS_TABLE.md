# Exercise One — Assumptions From Axioms Up (B-AXIS wall)

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` • **Slug:** baxis-wall-break
**Slice:** Exercise One (assumption ledger axioms→blocker + route cluster)
**Date:** 2026-06-20
**Posture:** wall-breaking. Even framework premises are marked as assumptions
for this exercise. Goal is genuinely NEW attack vectors, not defence of the
current no-go.

## Refresher surfaces read (stated per skill requirement)

- `docs/MINIMAL_AXIOMS_2026-06-05.md` (Lattice/Quantum/Record; open gates list)
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `docs/audit/data/axiom_premise_nodes.json` (READ-ONLY) — **4** approved nodes:
  `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive`
- `docs/audit/data/tier_a_admissions.json` (READ-ONLY)
- `docs/ai_methodology/skills/review-loop/SKILL.md`
- `docs/repo/CONTROLLED_VOCABULARY.md`
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`,
  `docs/EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md`,
  `docs/KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md`,
  `docs/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`
- Wall/campaign surfaces: `.claude/science/exercises/baxis-wall-break/EXERCISE.md`,
  `docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`,
  `.claude/science/physics-loops/single-clock-baxis-wall/NO_GO_LEDGER.md`,
  the keystone `docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`,
  `docs/SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`,
  `docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`,
  `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
- Campaign runner `scripts/single_clock_baxis_obstruction_unified_2026_06_20.py`
  (read the N2b gauge block directly)

## Headline of this slice (the load-bearing discovery)

**The B-AXIS campaign scoped itself to *bare A_min* and never loaded two of the
four approved primitives — `kinetic_isotropy_primitive` (`c_t = c_s`) and
`realized_state_primitive`.** Verified mechanically: `0` of the campaign's
`single_clock_*` runners mention kinetic isotropy or the realized state; the
unified no-go note mentions `c_t` once (only inside a cited title). The
exercise rule is explicit that approved primitives "chain-satisfy dependencies
without making downstream rows `retained_bounded`" and are legitimate premises
(not new axioms). So a B-AXIS clause that is *underivable from A_min* but
*derivable from A_min + an already-approved primitive* is a genuine open route
the campaign could not see by construction.

The richest instance is **N2b**: the campaign's "exact 1-parameter gauge"
`a_τ→c·a_τ, Ĥ→Ĥ/c` is, read in unit-bearing terms, the global ruler change
`(a_τ,a_s)→(c·a_τ,c·a_s)` that holds the *dimensionless graining ratio*
`ρ := a_τ/a_s` fixed (verified: `T̂²` depends only on `ρ`; distinct `ρ` give
genuinely distinct transfers, `Δ=0.236`, NOT a gauge orbit). `c_t=c_s` is
precisely the statement that `ρ` is pinned to the isotropic value; the
scale-reference primitive pins the absolute `a_s=1/M_Pl`. Two approved
primitives the campaign never combined plausibly pin the absolute `2a_τ`.

---

## Assumption Ledger

Columns: **ID | Layer | Assumption | E/I (Explicit/Implicit) | Current source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Confidence**

Confidence = my confidence the assumption *as stated/used by the campaign* is
correct & complete (High/Med/Low). Low confidence = juicy.

### Layer 0 — Axioms & approved primitives

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| A0-1 | axiom | **Lattice** = `Z^3`, nearest-neighbor cubic adjacency; supplies NO dynamics/BC/metric/spacing/cone/time | E | `MINIMAL_AXIOMS_2026-06-05` | the whole carrier | If Lattice is read as `Z^3` *spatial only* (no 4th coord), the "which-of-4-axes" question (N4) is mis-posed: time is not a lattice coordinate | N4 is an artifact of the Euclidean-block *reconstruction*, not of A_min | native-on-`Z^3` reframe (see §Routes R-NAT); already partly in campaign §7 but treated as relocation-only | build `U(t)` directly on `⊗_{x∈Z^3}C^2`, ask if N4 even *exists* | Med |
| A0-2 | axiom | **Quantum** = one qubit/site, `A_x≅M_2(C)≅Cl(3,0)`; NO dynamics/measurement/Born/gauge | E | same | per-site carrier | If `Cl(3,0)` real structure (not the complexified `M_2(C)`) is load-bearing, the carrier is NOT axis-symmetric: `Cl(3,0)` has a distinguished grading | N4 selector could live in the *real* Clifford grading the campaign discards by complexifying | check whether the staggered carrier's reality/CPT grading is W-transportable in the **real** algebra (campaign tested complexified) | rebuild E1 (reality grading) in `Cl(3,0)` real form, recompute joint stabilizer | Low |
| A0-3 | primitive | **scale_reference_primitive**: `a^{-1}=M_Pl`, units conversion only, zero dimensionless content | E | `SCALE_REFERENCE_PRIMITIVE_NOTE` | fixes the one dimensionful scale (the SPATIAL edge `a_s`) | Campaign treats N2b as "no observable carries 1/time"; but this primitive ALREADY carries 1/length for the SPATIAL edge. If time/space edges are linked, time unit inherits it | **N2b half-derivable**: absolute `a_s` is supplied; only the *ratio* `a_τ/a_s` is missing | combine with A0-4 (`c_t=c_s`) to pin `a_τ` | `/tmp/kin_iso_units.py` logic → repo runner | **Low** |
| A0-4 | primitive | **kinetic_isotropy_primitive**: `c_t=c_s` (OS0 hypercubic kinetic form); "one tick is one edge in FORM" | E | `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09` | declared for the framework's emergent time direction | **The campaign NEVER USES IT (0 runner hits).** It pins the dimensionless time/space graining ratio `ρ=a_τ/a_s` to the isotropic value | **N2b**: with `ρ` pinned by `c_t=c_s` and `a_s` pinned by scale-ref, absolute `2a_τ` is pinned. **N4**: the primitive is FRAMED with a distinguished "tick" (presupposes an axis label) | see Routes R-KIN-N2b and R-KIN-N4 | repo runner deriving `2a_τ=2/M_Pl` from the two primitives; honesty test: does `c_t/c_s` (kinetic FORM) literally equal `a_τ/a_s` (spacing)? | **Low** |
| A0-5 | primitive | **realized_state_primitive**: pointwise eval at a law-admissible realized state; NO measure/typicality/weight | E | `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11` | (newer than the 2026-06-06 fence the campaign leans on) | Campaign NEVER USES IT. A realized *history* (record order) is a single object that could pin the N5 clock-ray | **N5**: relocate the `(L_s−1)`-param clock-ray choice onto the realized record-ORDER | see Route R-RS-N5 | probe done (`/tmp/n4_n5_probes.py`): a single realized *state* does NOT pin a ray (joint eigenstate); a realized *history* might, but reading "one stream" is the open gate | Med |
| A0-6 | axiom | **Record**: durable realized-outcome registration, finite additive scalar `I`; NO time metric/occupancy/probability/within-sector data | E | `MINIMAL_AXIOMS_2026-06-05` | the readout layer | If "durable" + finite additivity already imposes a *total order* on records, that order IS a one-parameter structure (candidate single clock) | N5/N4: record total-order could be the native one-parameter group | check: does Record additivity + durability force a *total* (not partial) order on the realized record set? | finite countermodel: 2 commuting record streams — is their joint record set totally ordered by A_min? | Med |
| A0-7 | meta | The four approved primitives are **mutually independent** and may be **combined** freely as premises | E (registry) | `axiom_premise_nodes.json`; PRIMITIVE_REGISTRY_CHECK rule 3 | licences combining scale-ref × kinetic-iso for N2b | If some combination is implicitly disallowed (owner scope), the N2b route dies | the N2b derivation is conditional on the combination being licit | route depends on this | confirm with owner / `AXIOM_MINIMALITY_POLICY.md §6` that joint use is in-scope | Med |

### Layer 1 — Definitions & equivalence choices

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| D1-1 | def | "Evolution axis" (N4) = a choice among **4 Euclidean directions** of the reconstructed block `Λ=Z_τ×(Z/L)^3` | E | EXERCISE.md; keystone S3′ | frames N4 as a labelling among 4 | If time is NOT a 4th coordinate but a 1-param group on `Z^3`, there is no "4th direction" to label | N4 dissolves as a *question* (no axis to permute ⇒ W/S₄ act on nothing) | R-NAT (native framing): is the Euclidean 4-block a *reconstruction artifact* the wall inherits but A_min does not own? | construct the transfer/clock natively on `Z^3` w/o ever forming a 4-torus; check if S₄ even has a representation to act with | Med |
| D1-2 | def | "Absolute clock unit" (N2b) = a number carrying `1/time` units | E | unified note §4 | states what N2b needs | The campaign demands a `1/time` *observable*; but a *unit* is supplied by a *primitive*, not an observable | N2b's framing ("no observable carries 1/time") is a category error: units come from the scale/kinetic primitives, not observables | R-KIN-N2b | show the unit is pinned by primitives (A0-3×A0-4), not by needing a unitful observable | **Low** |
| D1-3 | def | "Second clock" (N5) = an independent commuting transfer factor admitted as physical evolution | E | unified note §6 | states N5 | The 4-part "physical-clock-admission" definition requires check (4) "source consumes it as THE clock" — that is a *bookkeeping* firewall, not a physical exclusion | N5's wall is partly definitional/admission-bookkeeping, not a physics no-go | examine whether check (4) can be *derived* from Record's single-durable-stream reading | re-read the admission def; test if Record forces one durable stream | Med |
| D1-4 | def | `T̂²` (two-step blocked transfer) is THE object dynamics is read from | E | keystone (R-RP2)/(R-SC2) | supplies the generator | The wall reads dynamics off the *transfer*; the generator `Ĥ` is the more fundamental object and the factorization `Ĥ=Σ E(p)n_p` is the SAME for the transfer and the group | the maximal-factorization that kills N5-irreducibility is a property of the *free* `Ĥ`; an *interacting* `Ĥ` need not factor | R-INT (interacting sector): does N5's maximal factorization survive `U≠1`? campaign is explicitly free-`U=1` only | build a small interacting staggered `Ĥ`, test commuting-factor span dim | Med |

### Layer 2 — Representation / algebra / topology / symmetry / regularity

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| S2-1 | symmetry | `W=P_{τ↔1}·diag((−1)^{x_τx_1})` exists and `S₄` acts **transitively** on the 4 axes | E | unified §5; runner [N4] | the core N4 wall (transitive ⇒ no axis derivable) | **Holds only on EVEN cubic-symmetric blocks** (odd-L falsifier resid 6.0). On generic finite/odd lattices `W` is NOT a symmetry | N4 wall is surface-specific; an A_min-admissible odd or non-cubic finite block could break S₄ *intrinsically* | R-ODD: is there an A_min-legitimate finite block (odd extent, or open BC from a record region) on which no signed exchange is a symmetry, so the axis is forced? | recompute G_bare on odd-L AND on open/Dirichlet boundary blocks; if `|axis-image|<S₄`, axis is selected | **Low** |
| S2-2 | symmetry | The relevant symmetry group is `W`/`S₄` (signed hyperoctahedral `B₄`, 384) | E | unified §5 | defines "transportable" | The block also carries a **staggered spin-taste** structure (Kawamoto-Smit): the *physical* symmetry is the staggered remnant `Γ`, a subgroup, NOT full `B₄` | N4: the spin-taste remnant may already break the τ↔x symmetry the bare hop has | R-TASTE: compute the joint stabilizer of the hop AND the spin-taste interpretation operators; is it sub-S₄? | build the KS taste generators, test if W commutes with the taste structure | Med |
| S2-3 | topology | Time enters as a **product** carrier `C^V⊗Cl(3,0)` with a Euclidean `Z_τ` factor | E (leaned-on) | EXERCISE.md "currently leaned on" | the reconstruction surface | A *fibered* or *crossed-product* carrier (time as automorphism, `Cl(3,0)⋊_α Z`) is not axis-symmetric: the crossed product distinguishes the acting `Z` | N4: crossed-product `A⋊_α Z` has a canonical generator (the dual action) — a built-in time direction | R-CROSS (math-sector): model the transfer as a C*-crossed-product; the dual `Ẑ` action / Connes-Takesaki module may select the axis | build the smallest crossed-product transfer, check if its modular/dual structure is axis-asymmetric | Med |
| S2-4 | regularity | Exact-zero residuals (W-transport, factorization) are framework-wide | I→corrected | unified N5-check | rhetoric | The campaign already bounds these to even cubic blocks; but downstream readers may over-read | (already handled) but signals the wall is fragile to surface choice | leverages S2-1/R-ODD | n/a | High (campaign honest here) |
| S2-5 | algebra | The `M_2(C)` per-site factor (complexification) is the physical carrier, NOT the real `Cl(3,0)` | E | keystone "physical carrier one summand" | picks the operative algebra | The complexification `Cl(3,0)⊗C≅M_2⊕M_2` *adds* an `i` and a swap symmetry that the real algebra lacks; W may be a complexification artifact | N4: the real-algebra grading could be the non-transportable selector (ties to A0-2) | R-REAL: redo the W-invariance test in the real `Cl(3,0)` before complexifying | recompute E1/E3/E5 enrichment stabilizers over `Cl(3,0)_R` | Low |

### Layer 3 — Readout / record / probability / measure / normalization / scale / time / dynamics / selector

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| T3-1 | scale | No A_min observable carries `1/time` units ⇒ `a_τ` is a free gauge | E | unified §4; runner N2b block | the whole N2b no-go | True for *observables*, but the **graining ratio `ρ=a_τ/a_s` is fixed by `c_t=c_s` (a primitive)**, and `a_s` by scale-ref. The "gauge" is just the ruler the scale-ref primitive already owns | **N2b derivable from primitives** | R-KIN-N2b (top route) | repo runner: `T̂²(ρ)` invariant only along `ρ=const`; primitives fix `ρ=1`,`a_s=1/M_Pl` | **Low** |
| T3-2 | time | The campaign N2b "malformed rescaling" (a_τ scaled, Q not) is the only discriminator | E | runner N2b block | proves gauge zeros are real | There is a SECOND malformed rescaling the campaign omits: `a_τ` scaled, `a_s` NOT (the kinetic-isotropy violation). It MOVES `T̂²` (Δ=0.236) | confirms `a_τ/a_s` is physical, not gauge — the campaign's own discriminator logic, applied to the missing primitive | R-KIN-N2b | add the `(a_τ, a_s-fixed)` discriminator to the runner; show it moves `T̂²` exactly like the campaign's `(a_τ,Q-fixed)` moves the count | **Low** |
| T3-3 | dynamics | Generator `U(t)` of the one-parameter group is "not axiom-supplied"; lands in emergent-dynamics open gate | E | unified §7 | relocation target | The single-clock keystone DOES supply `U(t)=exp(-itH)` with `H=-(1/2a_τ)log(T̂²/M_T)` from retained/retained_bounded rows. The generator IS supplied (given the transfer); only N2b/N4/N5 are open | the relocation "no generator" is too strong; the generator exists, sharpening exactly which sub-piece is missing | n/a (sharpens, doesn't open) | re-read keystone S1′ | High |
| T3-4 | record | The arrow/orientation is wholly outside A_min (carried by past hypothesis) | E | unified §7; arrow note | firewall | Arrow *direction* IS record-formation-derived (arrow note (3)); only the *existence* of a low-record boundary is the residual. So Record DOES source orientation given a boundary | the past-hypothesis residual is "universal-floor", not framework-specific — it is shared by ALL physics. Using it as a premise is not an exotic admission | R-ARROW-N4: does the record-formation arrow (a derived *direction*) select the evolution AXIS, not just its sign? | extend arrow runner: on a `Z^3×Z_τ` block, does monotone record accumulation single out τ vs x as the accumulation *direction*? (campaign R-N4-REGDIR said "ball not cone" — re-test WITH a realized low-record boundary state) | Med |
| T3-5 | selector | N4 needs a *non-transportable* structure to select the axis | E | unified §5.2 | classifies the search | "Non-transportable" presumes the surface is the symmetric block. A *realized state* (A0-5) or a *record region* (open BC) is generic data that need not be W-symmetric | N4: the realized state breaks W generically (a generic occupation pattern is not exchange-symmetric) | R-RS-N4: evaluate W-invariance AT the realized state, not on the bare operator. A generic realized state has no τ↔x symmetry | finite check: pick a generic realized occupation, compute whether any signed exchange fixes it | Med |
| T3-6 | normalization | `M_T` (transfer normalization) and vacuum subtraction are inert to N2b | I | (R-SC2); runner | needed for `H≥0` | `M_T=‖T̂²‖` carries units of the transfer; the normalization `T̂²/M_T` is dimensionless but `M_T` itself encodes `exp(-2a_τ·E_max)` — a unit-bearing object | possible hidden `1/time` carrier inside `M_T` | inspect whether `M_T` or `E_max` is a unit-bearing observable the campaign's "no 1/time observable" claim missed | trace units of `M_T` and the spectral gap through the construction | Med |

### Layer 4 — Retained/bounded repo surfaces reused

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| R4-1 | retained_bounded | (R-RP2) RP supplies `T̂²` only on **2-step, staggered-only, fixed-background, free `A_+^(2)`** sector | E | keystone Inputs | the transfer source | The whole wall lives on the FREE sector. N5 maximal factorization, N4 W-symmetry are free-sector facts | interacting/gauged sector may break factorization (N5) and W (N4) | R-INT: push the wall into the interacting sector where the campaign has no result | small interacting transfer; test factor-span dim and W-resid | Med |
| R4-2 | retained_bounded | `EMERGENT_POINCARE_...KINETIC_ISOTROPY` builds free-continuum SO(4)/boost from `c_t=c_s` | E | that note | shows kinetic-iso ⇒ time-space mixing | A boost MIXES time and space. If the free sector is boost-covariant (SO(4)→SO(3,1)), then "which axis is time" is **frame-dependent**, which is the OPPOSITE of N4 being a fixed undetermined label | N4 reframe: in a boost-covariant theory the axis is not a discrete selector at all; it is gauge-fixed by a frame choice (an observer/record), not by A_min | R-BOOST-N4: is N4 the wrong question because the free sector already has continuous boost freedom mixing the candidate axes? | use the emergent-Poincaré runner: do boosts connect the τ-axis transfer to a spatial-axis transfer continuously? if so N4 ≈ frame gauge | Med |
| R4-3 | retained | (R-STONE) finite-dim Stone uniqueness is transfer- and τ-relative | E | keystone | gives unique `H` given `(T̂²,τ)` | correctly scoped | n/a | underpins T3-3 | n/a | High |
| R4-4 | retained_bounded | `FREE_BILINEAR_QUASILOCAL_LR_BRIDGE` gives a finite cone with speed `v_μ=4W_μ/μ` for `0<dμ<η<arcsinh(m)` | E | keystone (R-FBQL) | propagation clause | **A finite LR speed `v_μ` is a `length/time` object.** Combined with the spatial edge `a_s` (scale-ref), a speed fixes a time unit: `a_τ ~ a_s/v` | **N2b**: the LR cone speed is a candidate `1/time`-carrying structure the campaign's "no 1/time observable" overlooked | R-LR-N2b: does the retained_bounded LR envelope's velocity pin `a_τ` given `a_s`? | trace units of `v_μ=4W_μ/μ`; is `W_μ` (weighted overlap) unit-bearing? | Med |

### Layer 5 — Runner / model / boundary choices

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| M5-1 | boundary | All-PBC (periodic) on the block; the only axis-selecting datum is a per-axis Z₂ BC asymmetry, which is "outside A_min" | E | unified §5.5 | the N4 sharpened pin | A_min supplies NO boundary condition — but a *record region* (a recorded subvolume) imposes an effective open/Dirichlet boundary that IS A_min-sourced (Record axiom). A record is a physical boundary | N4: the record itself supplies the BC asymmetry the campaign declared external | R-RECBC: model a recorded subregion as a boundary; is the induced BC axis-asymmetric and A_min-sourced? | finite block with a "recorded" frozen face; compute axis image of the automorphism group | Med |
| M5-2 | model | Even extent `L=(4,4,4,4)` chosen for exact zeros | E | unified §10 | exactness | (same as S2-1) odd/irregular extents break the exact W-symmetry | N4 via R-ODD | recompute on odd/mixed extents | High (known) |
| M5-3 | model | The 2-qubit / per-mode `[C-2CLK]` countermodel is "the" realizable second clock | E | unified §3 W-1 | proves N5 non-vacuous | It proves a second clock is *mathematically* realizable; it does NOT show the realized *history* admits two independent durable streams | N5: the gap between "mathematically realizable factor" and "Record-admissible second durable stream" | R-RS-N5: does any A_min-legal realized history actually exhibit two independent record orders? | finite simulation of record formation under two factor clocks; is the joint record set totally ordered? | Med |

### Layer 6 — Problem-local implicit / "obvious" steps

| ID | Layer | Assumption | E/I | Source/evidence | Why needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact | Conf |
|---|---|---|---|---|---|---|---|---|---|---|
| P6-1 | implicit | "A_min" for the wall = **the three axioms ONLY**, excluding approved primitives | I | unified note scopes to "A_min = Lattice+Quantum+Record only" | defines the no-go's universe | **This is the load-bearing implicit error.** The exercise + registry say approved primitives are legitimate premises. A clause underivable from 3 axioms but derivable from 3 axioms + an approved primitive is OPEN, not walled | N2b (via kinetic-iso + scale-ref), N5 (via realized-state) | the whole new-vector portfolio | confirm the wall's "A_min only" scoping is narrower than the framework's actual premise set | **Low** |
| P6-2 | implicit | The 1-parameter group `U(t)` has parameter `t∈R` with a metric already | I | unified §7 | needed to even speak of a "rate" | If `U(t)` is only defined up to reparametrization (a *flow*, not a *clock*), then N2b is the statement that A_min gives the orbit but not the parametrization. `c_t=c_s` is exactly a *parametrization* fixing (it grades the tick like the edge) | N2b reframe: clock = parametrization of a given orbit; primitive supplies it | R-KIN-N2b | n/a | Med |
| P6-3 | implicit | "One tick is one edge in FORM, not only in spacing" means `c_t=c_s` does NOT fix the spacing ratio | I | kinetic-iso note wording (the load-bearing ambiguity) | honesty boundary on R-KIN | If "form" isotropy does NOT imply "spacing" isotropy, then `c_t=c_s` does not pin `a_τ/a_s` and R-KIN-N2b FAILS | this is the single failure mode of the top route — must be resolved first | **first test of R-KIN-N2b**: does the dimensionless kinetic-form ratio `c_t/c_s` equal the lattice graining ratio `a_τ/a_s`, or only relate to the dispersion coefficient? | derive `c_t,c_s` from the staggered action's quadratic form and compare to `a_τ/a_s`; read `SPATIAL_CUBIC_TIME_ANISOTROPY` (it writes `Q(p)=c_t p_τ²+c_s|p_s|²` — these ARE spacing-linked coefficients) | **Med-Low** |
| P6-4 | implicit | Time-translation generator and "second clock" generators are compared in `span{I,Ĥ}` | E | unified N5 | gauge test | The comparison space ignores that a *physical* clock must be **monotone on records** (an arrow constraint). Of the `(L_s−1)`-param ray, only the *positive, record-monotone* sub-cone is admissible | N5: the admissible clock-ray cone may be much smaller (or a single ray) once record-monotonicity (arrow note) is imposed | R-MONO-N5: intersect the factor-clock ray space with the record-monotone cone; is the survivor unique? | finite check: which rays in `span_{≥0}{n_p}` produce a *monotone* durable record under the realized past-hypothesis boundary? | Med |
| P6-5 | implicit | The three clauses N2b/N4/N5 are genuinely **independent** missing data | E | unified §8 N2 | shippable no-go needs independence | If `c_t=c_s` couples them (it ties the time tick to the spatial edges AND distinguishes "the tick"), then pinning the ratio for N2b may also constrain N4 (the distinguished tick is the axis) | a single primitive could collapse two clauses at once — higher leverage | R-KIN-joint: does `c_t=c_s`+scale-ref attack N2b AND supply the "distinguished tick"framing that reframes N4? | analyze whether the primitive's "the evolution tick" wording is an axis commitment | Med |

---

## Route Cluster (from the "what if wrong?" entries)

Columns: **Route | Assumptions challenged | Why it might open the wall | Expected artifact | Risk | First test**

| Route | Assumptions challenged | Why this might open the wall | Expected artifact | Risk | First test |
|---|---|---|---|---|---|
| **R-KIN-N2b** ★ top | A0-3, A0-4, T3-1, T3-2, D1-2, P6-1, P6-2 | The campaign's N2b "gauge" is the scale-ref ruler in disguise; `T̂²` depends only on `ρ=a_τ/a_s`; `c_t=c_s` pins `ρ`, scale-ref pins `a_s` ⇒ absolute `2a_τ=2/M_Pl` derived from two APPROVED primitives the campaign never loaded | repo runner: (i) `T̂²` invariant only along `ρ=const`, distinct `ρ` distinct transfers; (ii) `(a_τ,a_s-fixed)` rescaling moves `T̂²` exactly as campaign's own malformed discriminator moves the count; (iii) `c_t=c_s`⇒`ρ=ρ*`, scale-ref⇒`a_s`, ⇒ `a_τ` pinned. A `bounded_theorem` "N2b discharged by kinetic-isotropy+scale-reference primitives" | **P6-3**: "form vs spacing" — if `c_t/c_s` (kinetic FORM) does not literally equal `a_τ/a_s` (spacing) the pin is only of the *form* coefficient, not the *clock unit*. Must resolve first. Also A0-7 (combination licit?) | Run `SPATIAL_CUBIC_TIME_ANISOTROPY` quadratic-form derivation: confirm `c_t,c_s` are the `p_τ²,p_s²` coefficients and relate them to `a_τ,a_s`. If they ARE spacing-linked, route is live |
| **R-RS-N4** | A0-5, T3-5, M5-1, S2-1 | Evaluate W/S₄ invariance AT the realized state / recorded region, not on the bare operator. A generic realized occupation (realized-state primitive) or a record-induced boundary (Record axiom) is NOT exchange-symmetric, so it breaks W *from inside A_min+primitive* | finite runner: pick a generic law-admissible realized occupation; show no signed exchange fixes it; show the induced effective BC is axis-asymmetric and A_min/primitive-sourced | The realized state breaks W but may break it *symmetrically* (no single axis) like the cubic-Laplacian E2/E8. Must show it selects ONE axis | finite check: realized occupation `n=(1,0,1,0)`-type on a `4^4` block; compute its stabilizer under `B₄`; is it sub-S₄ fixing one axis? |
| **R-ODD / R-RECBC** | S2-1, M5-1, M5-2, A0-6 | The exact W/S₄-transitivity is bounded to EVEN cubic-symmetric blocks. An A_min/Record-legitimate finite block — odd extent, or open/Dirichlet boundary induced by a record region — may have NO signed-exchange symmetry, forcing the axis intrinsically | runner: recompute `G_bare` axis-image on (a) odd extents, (b) open-BC blocks, (c) a recorded-face block; if `|axis-image|<S₄` the axis is selected | A_min may not privilege any particular finite block (campaign's "even cubic" is also a choice); need the block to be A_min/Record-FORCED not just allowed | recompute axis image on odd-L (already known resid 6) AND on a Dirichlet-face block; check if the asymmetry is record-sourced |
| **R-RS-N5 / R-MONO-N5** | A0-5, D1-3, M5-3, P6-4 | The `(L_s−1)`-param clock-ray freedom is over GENERATORS; impose two physical constraints the campaign omits — (a) record-monotonicity (arrow note: only positive record-monotone rays are clocks), (b) a single realized record-ORDER (realized-state). Intersection may be a single ray | runner: intersect `span_{≥0}{n_p}` with the record-monotone cone under a past-hypothesis boundary; simulate record formation under two factor clocks and test whether the realized history is totally ordered by one ray | The intersection may still be multi-dimensional; "one durable stream" reading is the open gate. Likely RELOCATES not closes — but a SHARPER relocation (onto realized record-order) is still progress | finite: which rays in `span_{≥0}{n_p}` give a monotone durable record under the arrow-note low-record boundary? count survivors |
| **R-INT** | D1-4, R4-1, S2-2 | The entire wall (N5 maximal factorization, N4 W-symmetry) is a FREE `U=1` fact. Push into the interacting/gauged staggered sector where commuting per-mode factorization generically fails and W need not be a symmetry | runner: small interacting staggered `Ĥ`; measure commuting-factor span dim (expect <`L_s`) and W-residual (expect >0) | A_min's transfer is currently only retained_bounded on the free sector; interacting RP is not supplied — so this may just move to a different open gate. But it could DISSOLVE N5 (no factorization ⇒ irreducible ⇒ single clock) | build a 2-mode interacting transfer; check if `[T_factor_A,T_factor_B]≠0` (factorization destroyed) |
| **R-CROSS** (math-sector seed) | S2-3, D1-1 | Model the evolution as a C*-crossed product `Cl(3,0)^{⊗Z^3}⋊_α Z` instead of a product `C^V⊗Cl(3,0)` block. A crossed product has a CANONICAL generator (dual action `Ẑ`) and a Connes-Takesaki modular structure that is intrinsically axis-asymmetric — the acting `Z` is distinguished | a smallest crossed-product transfer; check whether its dual/modular structure selects the time axis (N4) and/or fixes a parametrization (N2b) | Heavy machinery; the crossed product PRESUPPOSES the `Z`-action (the time direction), so may smuggle N4. Must check it is A_min-sourced | construct `M_2⋊_α Z` for a single site shift; inspect the dual action's fixed-point structure |
| **R-BOOST-N4** | R4-2, D1-1, S2-1 | The free sector built from `c_t=c_s` is boost-covariant (emergent-Poincaré note: SO(4)→SO(3,1)). Boosts MIX time and space continuously, so "which axis is time" is a *frame* choice, not a discrete undetermined selector — N4 may be the wrong question | analysis + runner: do continuous boosts connect the τ-axis transfer to spatial-axis transfers? If yes, the axis is gauge-fixed by an observer/record frame, not by A_min | If boosts only act on the free continuum limit (not the finite lattice), the finite-lattice N4 wall is untouched. Reframe, not closure | use emergent-Poincaré runner: check if a boost generator continuously rotates the τ-transfer into an x-transfer |
| **R-NAT** (sharpen campaign §7) | A0-1, D1-1, P6-1 | The campaign's §7 native-on-`Z^3` framing DISSOLVES N4 but claims it only "relocates". Re-examine: if the Euclidean 4-block is purely a reconstruction artifact, A_min never owned a "4th axis", so N4 is not a *missing* premise but a *non-question*. Combined with R-KIN-N2b (clock unit) and R-MONO-N5 (monotone ray), the residual may shrink to ONLY the past hypothesis (universal-floor) | a reframing note: B-AXIS = {past hypothesis (universal-floor, shared by all physics) + the two approved primitives}, with N4 dissolved and N2b/N5 supplied | The campaign already argued §7 relocates rather than derives; the burden is showing the relocation target is EMPTY (already supplied) for N2b/N5 and VOID (non-question) for N4 | assemble R-KIN-N2b + R-MONO-N5 results; if both close, show the ONLY residual is the universal-floor past hypothesis |

★ = highest-value new route.

## Cross-route reading

- **R-KIN-N2b is the single highest-value vector**: it is concrete, finite,
  testable today, challenges the most load-bearing implicit assumption (P6-1:
  "A_min = 3 axioms only"), and if it survives the P6-3 "form vs spacing" test
  it is an actual *derivation* of N2b from already-approved premises — the
  exercise's definition of a win. The `SPATIAL_CUBIC_TIME_ANISOTROPY` no-go
  already writes the kinetic form as `Q(p)=c_t p_τ²+c_s|p_s|²`, which are
  spacing-linked coefficients, so the omens are good.
- **R-RS-N4 and R-ODD/R-RECBC** jointly attack the N4 transitivity wall from
  its only soft spot: the wall is exact ONLY on even cubic PBC blocks with the
  bare operator. A realized state, a record-induced boundary, or an odd block
  each breaks W from a source the campaign declared "outside A_min" but which is
  actually Record- or realized-state-primitive-sourced.
- **R-MONO-N5 / R-RS-N5** convert N5 from "infinite ray freedom" to "ray ∩
  monotone-cone ∩ realized-order", a much smaller object — likely a sharper
  relocation, possibly a closure.
- **R-NAT** is the synthesis frame that, IF R-KIN-N2b and R-MONO-N5 close,
  reduces all of B-AXIS to the universal-floor past hypothesis (not a
  framework-specific gap).

## What NOT to do (do not re-walk these — already pruned in NO_GO_LEDGER)

OS/GNS, record-durability-as-axis, finite-speed cone-as-selector (circular),
anomaly/chirality label, KMS/APBC, APBC-alone, per-axis Z₂ BC as
*non-transportable*, reality/CPT grading *in the complexified algebra*, Wilson
temporal-gauge, crossing-link/η-curvature cocycle, the bare two-qubit `[C-2CLK]`
algebraic countermodel, transfer-spectrum/Stone for the absolute unit, counts
alone for the rate. The four block01 fresh attempts (R-N5-IRR, R-N4-REGDIR,
R-N2b-JOINT, R-N4-AUT) are done — do not rebuild them; the new routes here
attack the assumptions those attempts held FIXED (bare-A_min scoping; bare
operator instead of realized state; even cubic block; generator-space instead of
monotone cone).
