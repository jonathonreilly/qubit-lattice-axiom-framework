# Beta=6 SU(3) Wilson Plaquette Campaign — Synthesis Capstone Frontier Note

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**trace_class:** frontier_discovery
**Scope:** campaign-level frontier map / synthesis. This note reconciles the
beta=6 SU(3) Wilson single-plaquette campaign into one honest
PROVEN / CONDITIONAL / OPEN boundary. It is **not** a closure of beta=6,
introduces no value, no new authority, no new axiom, no new vocabulary, and
sets no audit status. It is a backward-looking synthesis of already-landed
narrow content plus the live no-go ledger.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome for any cited claim_id; every status quoted
below is a read-off from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on 2026-05-30.

## 0. Scope and what this note is for

The thermodynamic SU(3) Wilson single-plaquette expectation at the framework
point beta=6,

```text
<P>(beta=6, L->infinity) ~= 0.594   (canonical lattice-QCD comparator),
<P> := <(1/N_c) Re Tr U_p>,  N_c = 3,
```

is the single most-cited open quantitative gate in the framework: it feeds
`u_0 = <P>^(1/4)`, then `alpha_s`, then the v / y_t / m_t / m_H chain. The
number is currently available **only** as a Monte-Carlo finite-size-scaling
comparator
([`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md),
`P_inf = 0.59400 +/- 0.00037`, `plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`,
retained_bounded) — never an analytic from-primitives derivation.

This capstone reconciles four lanes of the campaign:

- **The closure research map** (campaign reference #2245), the consolidated
  20-route blocked ledger and the doubly-walled lane-killer
  ([`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md));
- **The exact strong-coupling series** of `Delta(beta) = P_full - P_1plaq`
  through order `beta^7` (campaign references #2255 / #2365 / #2374), with the
  tadpole/geometric continuation falsified
  ([`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md),
  [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md));
- **The analytic-continuation class characterization** (campaign reference
  #2395): finite-volume positivity proven, thermodynamic class conditional, the
  `beta^8` d-log-Pade activation as a class-independent rank floor
  ([`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md),
  [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md));
- **The rho-selection survey** (campaign reference #2410), whose spirit — that
  enumerating the missing object's structure is not the same as supplying it —
  is independently corroborated on-disk by the closure map's 0-of-5 route
  pruning (Section 4 below).

**Bottom line, stated once.** beta=6 `<P>` is **OPEN**. This capstone is a
frontier characterization with named walls, **not** a closure. `0.594` stands
only as a Monte-Carlo comparator. The campaign has rigorously located and
walled the missing object; it has not supplied it, and no single new axiom is
admissible or needed to supply it.

**Provenance discipline.** The campaign references above are plain-text
pointers, not citation-graph dependencies. The on-disk artifacts this note
reconciles end the **exact series at order `beta^7`**
(`d_5, d_6, d_7`); the on-disk analytic-class note's own decisive next step is
to compute `d_8` (Section 7 there), and it records `d_8` as **at/past** the
contraction ceiling, not as computed. This capstone is written against that
on-disk state. Any campaign content that asserts coefficients beyond `d_7`, a
formed `[1/1]` d-log-Pade on physical data, or a "singularity lives in the
later support class" conclusion is **not** part of the load-bearing record here
and is explicitly not asserted (Sections 3, 6, 7 state why).

## 1. Engagement with the no-go ledger (the three-fold wall, one object)

The campaign's own retained no-gos and retained-bounded under-determination
results jointly establish that the missing object is a single thing seen from
three sides. All statuses are 2026-05-30 ledger read-offs.

- **Real-space side — under-determination by local data.**
  `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` (Theorem 3,
  **retained_bounded**): the boundary character measure `rho_{p,q}(6)` is **not**
  fixed by `c_lambda(6)` + SU(3) intertwiner data plus any tested 1-parameter
  `rho`-family. Three admissible families give a **combined Perron-value spread
  >= 0.1937**, straddling the comparator with nothing in the local input class
  canonically selecting it. (Honest scope, per that note's own 2026-05-04
  narrowing: this rules out 1-parameter local closures, **not** 0-parameter
  derivations — but the only computed 0-parameter case, the L_s=2 Schur cube,
  gives `0.4291`, not the comparator.)
- **Observable-bridge side — escape needs a new primitive.**
  `gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03`
  (**retained_no_go**): the observable bridge only **pins** the missing
  nonperturbative number; escape "requires a NEW independently-audited
  primitive."
- **Series side — no finite truncation closes it.**
  `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`
  (**retained_no_go**): `log Z_L` is exactly nonpolynomial on the finite Wilson
  surface, so the connected hierarchy **cannot truncate at any finite order**;
  closure "requires either an exact nonpolynomial solution of the full
  connected hierarchy, or some new exact generating object equivalent to that
  hierarchy."

**These are three views of one missing object.** Whether approached in real
space (`rho_{p,q}(6)`), via the observable bridge (the pinned nonperturbative
number), or in series space (the nonpolynomial-hierarchy solution / its
generating object), the same gap is restated. This is the unified wall
statement the capstone leans on, and it is stronger and less attackable than
"engineering plus one import": **closing beta=6 requires a genuinely new
from-primitives object that the current A1+A2 primitive packet demonstrably
does not yet yield.** No finite coefficient count, and no analytic-class result
alone, supplies it.

## 2. The exact series (PROVEN, through `beta^7`)

Writing `Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n`,
the campaign computed the exact connected strong-coupling coefficients

```text
d_5 = 1/472392     (= 4/18^5),
d_6 = 7/5668704,
d_7 = 5/17006112,
```

all positive, two-engine verified to exact rationals (the optimized
invariant-projector contraction reproduces the sympy engine's `d_5, d_6` before
computing `d_7`). The contiguous ratios are

```text
d_6/d_5 = 7/12 ~= 0.583,    d_7/d_6 = 5/21 ~= 0.238.
```

**Mechanism.** Connected-cumulant linked-cluster expansion + exact SU(3) Haar
invariant-projector single-link integrals + a GF(3) cycle-space certificate.
The certificate shows that no color-closable distinct support of size 6 or 7
through the marked plaquette exists, so `d_6` and `d_7` are pure four-cube-shell
multiplicity sums (each of the four cube shells contributes `5/68024448` at
order 7). This is the on-disk extent of the certificate: it is exact **through
`d_7`**.

**What the ratios do and do not say.** The two ratios `7/12, 5/21` are
**decreasing and non-geometric**. That is enough to falsify the single-ratio
geometric/tadpole continuation (Section 3). It is **not** a proof that the
cube-shell sector is an entire function: two (or three) decreasing ratios from a
known pre-asymptotic regime are equally consistent with a finite-radius series
whose early ratios have not yet settled. Indeed the analytic-class note's own
constant-amplitude single-pair fit to `(1, 7/12, 5/36)` returns radius
`R ~ 1.16`, not the conjectured `~5.5-5.7` — direct evidence the low orders do
**not** pin the radius. Accordingly this capstone records only "the contiguous
ratios are decreasing," and does **not** assert "entire-like / super-geometric"
as a theorem, nor does it locate the function's dominant singularity in any
particular graph-support class. (Singularity location is a global property of
the whole coefficient sequence — `limsup |d_n|^{1/n}` — not a property of which
graph topology first contributes a coefficient at a given order. Conflating the
two is the recurring beta=6 finite-vs-thermodynamic failure mode the
analytic-class note's own cross-cycle audit warns against.)

## 3. Falsified single-singularity continuations (PROVEN)

Two cheap analytic-continuation ansatze are falsified on the exact data:

1. **Single-ratio geometric / tadpole — FALSIFIED.** A single-ratio geometric
   continuation predicts `d_7^pred = (d_6/d_5) d_6 = 49/68024448`, but
   `d_7^exact = 5/17006112`. The relative miss is `1.45` against the exact
   value — far outside the 5% support window
   (`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`).
2. **Positive-real divergent algebraic branch point on `(0,6]` — EXCLUDED,
   exponent-independently.** From the single dimensionless bracket invariant
   `u = c2/c1^2 = 20/49` (with `c1 = 7/12`, `c2 = 5/36`): for any singularity
   `A(1 - beta/B)^{-g}` with `B,g > 0`, one has
   `c2/c1^2 = 1/2 + 1/(2g) > 1/2` for all `g > 0`; since `u = 20/49 < 1/2`, no
   such positive-real divergent branch point lies on `(0,6]`. The minimal
   `[0/2]` Pade of the bracket has discriminant `-67/144 < 0`, a
   **complex-conjugate pair**.

**Honesty about what (1) and (2) buy (carried over verbatim from the
analytic-class note).** Facts (1)-(2) are **not two independent
corroborations**: both are deterministic functions of the **same** scalar
`u = 20/49`. Three coefficients constrain only this **type-discriminating**
quantity; the **location** `|beta_c|` is a one-parameter family `R(g)` spanning
`~0.6` to `~8.8` as the assumed exponent sweeps. So the exact-coefficient data
corroborates the analytic **class** (complex-pair-favored, single-real-pole and
positive-real-branch-point excluded) but **measures no location**.

**On the broader "single-pair vs multi-pair" question.** The on-disk record
falsifies the **single-real-pole / geometric** continuation and excludes a
positive-real divergent branch point. It does **not**, on the on-disk
`d_5..d_7` data, falsify a single off-axis complex pair, nor does it
establish a multi-pair structure as "the surviving hypothesis." A sharper
single-pair test (the sign/magnitude of `d_8`) is exactly the decisive next
step (Section 7), and on the on-disk state that test has **not** been run. This
capstone therefore does **not** assert "single-complex-pair falsified" or
"multi-pair surviving"; those are forward claims awaiting `d_8`.

## 4. The rho-selection survey and the closure map's route pruning (PROVEN/CONDITIONAL)

The campaign's rho-selection survey (reference #2410) asked whether any
candidate selection mechanism dynamically pins `rho_{p,q}(6)`. Its spirit is
independently corroborated on-disk by the closure research map
(`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`), which pruned **five candidate
analytic/structural routes to zero closure-ready routes** (Section 5 there) and
identified the common obstruction: every route that needs genuine
multi-plaquette content collides with either the under-determination by local
data (Theorem 3) or the exact-contraction infeasibility at `L_s >= 3`.

One identity that looked like a derivation is foreclosed:

- **`rho = kappa/a^4` ("all-weight convolution identification") is
  audited_renaming** (`gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17`,
  **audited_renaming** on the live ledger). The audit flags it as a
  definition/packaging of the stripped residual eigenvalue sequence, **not** an
  independent derivation of the environment boundary class function. Any closure
  route leaning on it is circular.

**Net:** the survey/pruning leaves the physical question "what dynamically pins
`rho_{p,q}(6)`" genuinely open. Enumerating the missing object's structure
(which supports contribute at which order; which families are admissible)
characterizes the **problem**, not the **solution**.

## 5. The analytic class (PROVEN finite-L; CONDITIONAL thermodynamic)

From the reduction-existence theorem (`gauge_vacuum_plaquette_reduction_existence_theorem_note`,
**retained**), `Z_L(beta)` is entire, so `P_L` and `Delta_L` are meromorphic.

**Finite-volume positivity (PROVEN, rigorous, finite-L).** For any finite
periodic SU(3) Wilson `L^4` surface and all real beta,
`0 < Z_L(beta) <= exp(|beta| N_plaq)` (strictly-positive real integrand against
positive Haar; `|S_L| <= N_plaq`). Hence `Z_L` has **no real zero**, so `Delta_L`
is **real-analytic on `[0,6]`** with **no real Lee-Yang zero**, and — real
Taylor coefficients force conjugate zeros — its nearest singularity is a
**complex-conjugate pair off the real axis**. This is verified for the
single-plaquette layer: the nearest zero of the entire `Z_1plaq` is at
`beta_c = 3.3175 +/- 7.5047 i`, `|beta_c| = 8.205`, residual against the true
Bars `Z` decreasing to `~1e-34` (a genuine entire-function zero, not a
truncation artifact); `beta = 6` sits inside this single-plaquette disk
(`6/|beta_c| = 0.73`), and `P_1plaq(6) = 0.4225317396` exactly.

**The finite-volume caveat (carried over, decisive).** This is a **finite-volume
statement** — the textbook Yang-Lee template, using nothing about
SU(3)/beta=6/`Delta` beyond compactness + positivity. It does **not** commute
with `L->infinity`: a real bulk transition at `beta* <= 6` would appear as
complex Lee-Yang zeros pinching the real axis in the limit, while every finite-L
`Z_L` stays strictly positive (the Yang-Lee pinch). So the rigorous content
covers `P_1plaq` and every finite-L truncation; the **infinite-volume**
real-analyticity of `Delta` at beta=6 is **not** established by positivity
alone. A second, finer mismatch: finite-L `P_L` has simple **pole** pairs,
whereas d-log-Pade applicability concerns **branch-point** pairs that emerge
only as poles condense onto a cut in the limit.

**Thermodynamic class (CONDITIONAL).** The thermodynamic `Delta(beta)` being of
the complex-conjugate-pair, no-real-branch-point-on-`[0,6]` class is
**conditional** on the physics import that SU(3) pure-gauge has no real bulk
transition below beta=6 (smooth crossover; literature Fisher zeros
`5.54 +/- i0.10` off-axis; SU(N<=4) crossover-only). This premise is
**physically near-certain but unproven in-repo**: the analytic-class note files
a from-primitives proof of it under OPEN, and finite-L positivity does not
transfer across the limit. See Section 6 for why this premise is honestly an
undischarged dynamical input, not a clean methodology import.

**The `beta^8` d-log-Pade requirement is a class-INDEPENDENT rank floor
(PROVEN).** A complex-conjugate pair is a degree-2 d-log denominator. The three
known `Delta` coefficients give only **two** coefficients of `H = (log h)'`
(`H_0 = 7/12`, `H_1 = 2c2 - c1^2 = -1/16`), one short of the three needed to
form even a balanced `[1/1]`. So the minimal d-log-Pade that resolves the pair
and makes a falsifiable next-coefficient prediction needs `>= 4` contiguous
coefficients `d_5..d_8` (= `beta^8`). **Proving the analytic class supplies zero
coefficients and therefore cannot relax this floor.** On the on-disk state this
floor is **not yet met** (only `d_5..d_7` exist), so no `[1/1]` is formed on
physical data, and no spurious-real-pole / `<P>(6) ~ 1.62` readout is computed
by any committed runner; any such number would be a forward claim awaiting `d_8`
and is not asserted here.

**No achievable error bound from the known coefficients (PROVEN).** The three
known coefficients are pre-asymptotic. If `|beta_c| ~ 5.5-5.7` holds, beta=6
lies **past** the disk of convergence (`6/5.54 ~ 1.08`), so the bare truncation
carries no Cauchy bound at 6; there is no Stieltjes bracketing either (a complex
pair is not a real cut; positivity buys `P_1plaq` monotonicity, not a Stieltjes
property of the bracket). The closest realistic literature precedent (2D
O(N=3) sigma-model d-log-Pade, Campostrini-Pelissetto-Rossi-Vicari
arXiv:hep-lat/9602011, a methodology import) tracked Monte-Carlo only **up to**
— not far past — the radius even at 14-21 orders. The forward three-term
truncation `<P>(6)_trunc ~ 0.579` is a partial sum recorded as a sensitivity
datum, not a controlled estimate.

## 6. The two named walls, honestly labeled

The campaign's "minimal required input" framing is two halves. Each is
re-labeled here to survive a hostile referee, **dropping the word "only."**

### 6a. Half 1 — exact high-order coefficients (contraction wall, NOT a proven barrier)

Reaching the `~15-40` exact coefficients a genuine resummation would need
collides with the SU(3) contraction cost: the connected cluster count grows
like the lattice-animal constant (`mu ~ 8`), and each non-closed cluster's exact
Haar weight is a 3nj-network contraction whose cost rises with cluster area. The
sharpest stated cost barrier is the L_s=3 link-adjacency graph treewidth.

**Honest status of the treewidth barrier (corrected).** The treewidth-29 figure
is an **upper bound from two greedy heuristics (min-degree, min-fill) on one
graph**, recorded in `su3_wigner_l3_treewidth_infeasible_2026-05-04` — which is
**unaudited** on the live ledger (the on-disk closure note's Section 2 table
records it as "audited_conditional," but that is a stale read-off; the live
2026-05-30 ledger says **unaudited**). That source note explicitly states it
"does **not** prove a global treewidth lower bound or rule out all possible
elimination/path-optimization strategies," and that "the true treewidth could be
lower." So Half 1 is honestly **engineering against a heuristic upper bound, not
a proven foreclosure.** The source note itself nominates a rank-aware contractor
(keep the rank-8 `P^G` decomposition, never materialize the full link tensor) as
a plausible escape, estimated at days of engineering — i.e., a softer, more
route-dependent wall than "blocked ONLY by treewidth-29."

This is corroborated by the campaign's own coefficient frontier: the on-disk
series reached `d_7` by exploiting the GF(3) cube-shell structure and an
optimized invariant-projector contraction, **not** by defeating treewidth. That
the engine advanced by exploiting symmetry is direct evidence the cost wall is
route-dependent. Conversely, the on-disk analytic-class note records `d_8` as
**at/past** the practical contraction ceiling for the current engine — so Half 1
is real and binding at the next order, but as an **engineering** ceiling, not a
proven barrier.

### 6b. Half 2 — the no-real-bulk-transition certificate (an UNDISCHARGED DYNAMICAL premise, not a clean import)

The licence to analytically continue past the convergence radius to beta=6
requires that the thermodynamic `Delta` be real-analytic on `(0,6]` with its
dominant singularity an off-axis complex pair (the `L->infinity`
no-real-bulk-transition clause).

**Honest status (corrected).** This is **not** a methodology/comparator import
in the sense Bars (a computational identity) or the Fisher-zero literature (a
corroborator) are — those touch no derivation. It is a **load-bearing,
infinite-volume, dynamical** statement about phase structure, and it is the
**licence** for the continuation. The A_min primitives — A1 (Cl(3) per-site
algebra) and A2 (Z^3 substrate) — are **kinematic**; nothing shown in-repo
derives an infinite-volume no-bulk-transition theorem from them. The
analytic-class note files a from-primitives proof of this premise explicitly
under **OPEN**, and notes finite-L positivity "does **not** transfer across
`L->infinity`."

Therefore the "import -> bounded -> retire" framing is **not** applied to this
premise in this capstone, because that framing presupposes a reachable in-repo
retirement, and the retirement **is** the open problem — it is the doubly-walled
`rho_{p,q}(6)` restated in the beta-plane (the analytic-class note's own line:
"the location ... is exactly the open `rho_{p,q}(6)` object restated in the
beta-plane"). The honest classification is: **an undischarged dynamical premise,
A1+A2-underivable as of this capstone, sitting on the open frontier alongside
`rho_{p,q}(6)`.** "Physically near-certain" is a confidence statement, not a
derivation; the same scrutiny applied to no-gos applies here — a closure that
leans on an undischarged import is as suspect as a wrongly-scoped no-go.

## 7. No new axiom (PROVEN by policy + the no-go trinity)

**No single new axiom is admissible or needed; A_min stays A1+A2.** This is true
in the precise sense that the legitimate path never *extends* A_min by fiat. But
the substantive content that is missing is **not free**: per the three-fold wall
of Section 1, closing beta=6 requires a **new from-primitives dynamical object**
— concretely **either** an exact nonpolynomial solution / closed generating
representation of the connected hierarchy (forced by the retained_no_go
infinite-hierarchy obstruction, which proves no finite coefficient count
closes the value), **or** an in-repo `L->infinity` no-real-bulk-transition /
off-axis-pair analyticity theorem (the Half-2 premise), **or** the real-space
`rho_{p,q}(6)` itself (under-determined by all local data per Theorem 3, and
exact-contraction-infeasible at `L_s >= 3`). These are the same object from
three sides. So "no new axiom needed" is true in the labeling sense; the honest
reading is that a **genuinely new from-primitives dynamical theorem is missing**,
and A1+A2 do not currently yield it.

This is the load-bearing correction to the campaign's "no new axiom — only a
contractor plus a bounded import" framing: the word **"only"** is dropped, and
the no-bulk-transition premise is **not** waved through as a clean import.

## 8. Scientific boundary: PROVEN / CONDITIONAL / OPEN

**PROVEN (rigorous, this synthesis + cited source inputs):**

- `Z_L(beta)` entire and strictly positive on all of R at every finite L
  (`0 < Z_L <= exp(|beta| N_plaq)`); hence `Delta_L` real-analytic on `[0,6]`
  with no real Lee-Yang zero, nearest singularity a complex-conjugate pair —
  **a finite-volume statement** (textbook Yang-Lee template).
- Single-plaquette `P_1plaq` analytic on all of R; nearest singularity a
  complex-conjugate pole pair at `beta_c = 3.3175 +/- 7.5047 i`,
  `|beta_c| = 8.205`, residual `-> 1e-34`; beta=6 inside its disk;
  `P_1plaq(6) = 0.4225317396`.
- Exact connected coefficients `d_5 = 1/472392`, `d_6 = 7/5668704`,
  `d_7 = 5/17006112`, all positive (two-engine verified); contiguous ratios
  `7/12, 5/21` (decreasing, non-geometric). GF(3) certificate: `d_6, d_7` are
  pure four-cube-shell multiplicity sums (exact through `d_7`).
- Single-ratio geometric/tadpole continuation **falsified** (`d_7/d_6 != d_6/d_5`,
  relative miss 1.45); no positive-real divergent algebraic branch point on
  `(0,6]` (`u = 20/49 < 1/2`, exponent-independent); minimal `[0/2]` Pade a
  complex pair (`disc = -67/144 < 0`).
- The `beta^8` (`d_5..d_8`) d-log-Pade activation is a **class-independent rank
  floor** (degree-2 d-log denominator needs 3 coeffs of `H`; three `Delta`
  coeffs give 2); proving the class supplies no coefficients.
- No achievable from-primitives error bound on `Delta(6) / <P>(6)` from the
  known coefficients (beta=6 past the conjectured radius; no Cauchy/Stieltjes
  bracketing).
- `rho_{p,q}(6)` under-determined by local character+intertwiner data + any
  tested 1-parameter `rho`-family (Theorem 3, retained_bounded; combined Perron
  spread `>= 0.1937` straddling the comparator).
- `rho = kappa/a^4` is **audited_renaming** = circular packaging (ledger-confirmed).

**CONDITIONAL (corroborated, not derived):**

- The thermodynamic `Delta(beta)` is of the complex-conjugate-pair,
  no-real-branch-point-on-`[0,6]` class — conditional on the (physically
  near-certain, unproven in-repo) import that SU(3) pure-gauge has no real bulk
  transition below beta=6. Finite-volume positivity does not transfer across
  `L->infinity`.
- IF that class holds, d-log-Pade is the methodologically correct continuation
  tool — but only as a high-order method; three or four coefficients give no
  convergent estimate and no provable error bar. The favorable-end convergence
  evidence is a constant-amplitude Gegenbauer proxy whose amplitude is **tuned**
  to the physical `Delta(6) ~ 0.171` = the comparator; recovering a tuned number
  is not a demonstration that the method reaches beta=6.

**OPEN (the lane-killer, unchanged):**

- The single missing from-primitives dynamical object — equivalently
  `rho_{p,q}(6)` (real space), the pinned nonperturbative number (observable
  bridge), the nonpolynomial-hierarchy solution / its generating object (series
  space), or the `L->infinity` off-axis-pair analyticity certificate (beta-plane
  location `|beta_c|`, surrogate estimates spanning `~2.2` to `~8.2`). Doubly
  walled: under-determined by local data **and** exact-contraction-infeasible at
  `L_s >= 3`. No analytic-class result and no finite coefficient count supplies it.
- A from-primitives proof of no-real-bulk-transition for SU(3) on `(0,6]` (the
  Half-2 premise): currently a literature import, not an in-repo derivation.
- Exact coefficients `d_8` and beyond (past the current contraction ceiling),
  and whether any continuation reliably reconstructs `<P>(6) ~ 0.594`
  (undemonstrated even in principle past the radius).

### Boundary discipline gate (N1-N8)

This is a campaign-level frontier map with named walls, not a no-go on beta=6.
The negative boundary is only: the campaign's landed content (exact series
through `d_7`, finite-L analytic class, under-determination) does **not** produce
a controlled beta=6 closure, and the missing content is a new from-primitives
dynamical object, not a coefficient cycle or a clean import.

**N1 — Alternative route enumeration.** The closure map pruned five routes to
zero closure-ready; the analytic-class note checked five closure shortcuts; this
capstone adds no sixth and ranks none as closure-ready.

**N2 — Wall-independence audit.** The walls are: thermodynamic
no-real-transition undischarged; `d_8`+ at the contraction ceiling; continuation
past the radius unbounded; `rho_{p,q}(6)` under-determined. Closing any one does
not close the others.

**N3 — Hidden-wall scan.** Fisher-zero and O(N) precedents are
methodology/comparator imports; Bars is a computational identity; `0.594` is
comparator-only. The no-real-bulk-transition statement is **not** treated as a
free import — it is filed OPEN (Section 6b). None is used as a derived beta=6
value.

**N4 — Residual matching.** Lee-Yang localization is used only for analytic-class
characterization (honoring the standalone-closure foreclosure). The treewidth
result is restated as a heuristic-upper-bound contraction ceiling and the
beta-plane location wall, not as a proven foreclosure.

**N5 — Rhetoric audit.** "Not a closure" is checked at finite-L,
single-plaquette, thermodynamic, d-log-Pade, and contraction resolutions. No
positive finite-L or single-plaquette result is promoted to thermodynamic
closure. The word "only" is removed from the closure-requirement framing.

**N6 — Partial-closure path scan.** Legitimate future partial closures remain:
derive no-real-bulk-transition in-repo; compute `d_8` with a rank-aware
contractor; build a controlled high-order continuation. None is called
impossible; none requires a new axiom.

**N7 — Steelman.** A hostile reviewer would argue that the "no new axiom — only
engineering + a bounded import" headline smuggles a new dynamical input past
A_min: the no-bulk-transition premise is dynamical, infinite-volume,
A1+A2-underivable, and load-bearing for the continuation, so consuming it is
functionally a new dynamical input regardless of label. **This capstone concedes
the objection** and adopts the honest framing (Sections 6b, 7): the premise is
undischarged and on the open frontier; "only" is dropped.

**N8 — Cross-cycle echo.** Prior beta=6 routes failed when finite/local evidence
was promoted to thermodynamic closure, or when a graph-support bookkeeping fact
was read as a singularity-location conclusion. This capstone keeps finite-volume,
single-plaquette, and thermodynamic claims separated, and does **not** infer the
function's singularity location from which graph supports first contribute at a
given order.

## 9. The single decisive next step

**Compute the exact order-`beta^8` connected coefficient `d_8` of `Delta(beta)`**,
via a contraction engine that defeats the per-link invariant-projector cost the
cycle-2 engine already pushed to `beta^7` — concretely, a **rank-aware SU(3)
contractor** that maintains the rank-8 `P^G` decomposition rather than
materializing full link tensors (the escape the treewidth note itself
nominates).

`d_8` is the decisive next datum because it is simultaneously **(a)** the
`beta^8` **activation** coefficient for the d-log-Pade predictive test — the
first contiguous coefficient that lets a balanced d-log-Pade form on physical
data and make a falsifiable `d_9` prediction — and **(b)** a clean
sign/magnitude **falsifier** of the constant-amplitude single-pair hypothesis,
whose fit to `d_5, d_6, d_7` predicts a specific `d_8`. Either outcome is a
source-level bounded result on cited source inputs.

**Honest caveats (load-bearing, not omitted).**

1. **This is a falsification probe, NOT a closure step.** The retained_no_go
   infinite-hierarchy obstruction proves no finite coefficient count closes the
   thermodynamic value, so no single coefficient — `d_8`, `d_9`, or any other —
   can be decisive *for closure*. `d_8` is decisive for the next **falsification
   test**, not for the value.
2. **The engine is demonstrated to bind at this order.** The cube-shell /
   invariant-projector engine that reached `d_7` is recorded as at/past its
   contraction ceiling at `d_8`; reaching `d_8` requires either a Munster-style
   graphical strong-coupling bookkeeping or the rank-aware contractor. **No such
   contractor that defeats the cost wall is known**; the only engine that reached
   `d_7` is not known to extend. The treewidth barrier it must beat is a
   heuristic **upper** bound (unaudited; not a proven lower bound), so a better
   contraction order or rank decomposition might help — which is itself an
   admission the wall is softer and more route-dependent than a foreclosure.
3. **Even if `d_8`+ land, closure is not assured.** Reliable continuation past
   the radius to beta=6 needs far more than four coefficients (the literature
   precedent failed past the radius even at 14-21 orders), and closing `<P>(6)`
   **still** requires the new from-primitives dynamical object of Section 1/7 —
   either the no-real-bulk-transition certificate (Half 2) or the
   nonpolynomial-hierarchy solution or `rho_{p,q}(6)` — which no coefficient cycle
   supplies. The alternative direct route (exact `rho_{p,q}(6)` by `L_s >= 3`
   contraction) is the same contraction wall.

This is **engineering within the existing A1+A2 Haar primitive — not new physics
and not a closure.** No single new axiom is admissible or needed; A_min stays
A1+A2.

## 10. Closure-reachability statement (honest)

beta=6 `<P>` closure is reachable **in principle**, but **not** via "only
engineering plus one bounded import," and **with no guarantee of success even
then.** The honest statement, stripped of the word "only," is:

> Closing beta=6 requires **(A)** a NEW from-primitives dynamical object not
> currently derivable from A1+A2 — equivalently the doubly-walled `rho_{p,q}(6)`,
> or the nonpolynomial-hierarchy solution / its generating object (forced by the
> retained_no_go infinite-hierarchy obstruction), or an in-repo `L->infinity`
> no-real-bulk-transition / off-axis-pair analyticity theorem; these are one
> object seen from three sides. **(B)** A contraction advance past a cost barrier
> that is currently only a heuristic upper bound (unaudited; not a proven lower
> bound), to supply the exact high-order coefficients a controlled continuation
> would consume. **And even with both (A) and (B), closure is not assured:** the
> closest realistic literature precedent failed to continue past the radius even
> at 14-21 orders, and the favorable in-repo convergence evidence is a proxy
> tuned to the comparator.

A_min is **not** extended by fiat (no new axiom), and the campaign's computable
runway on the cube-shell sector ends at `d_7` on-disk with `d_8` at the engine's
ceiling. This is honestly a hard, multi-session frontier — decisively **not** a
one-axiom fix and **not** a closure today. `0.594` stands only as a Monte-Carlo
comparator.

## 11. What this note claims / does not claim

Claims:
- the campaign-level reconciliation above (PROVEN/CONDITIONAL/OPEN of Section 8);
- the three-fold wall as one missing from-primitives object (Section 1), grounded
  in the live no-go ledger;
- the exact series through `d_7`, the two falsifications, and the
  class-discriminant facts (Sections 2-3);
- the finite-L positivity / single-plaquette Lee-Yang localization (Section 5);
- the corrected, honest labels for the two walls (Section 6) and the dropped
  "only" (Sections 7, 10);
- the decisive next step as a `d_8` falsification probe, not a closure step
  (Section 9).

Does NOT claim:
- any value of `<P>(beta=6)`, `beta_eff(6)`, `u_0`, or `alpha_s`;
- the thermodynamic real-analyticity of `Delta` at beta=6 (undischarged
  dynamical premise, OPEN);
- the location of `Delta`'s thermodynamic nearest singularity;
- any coefficient beyond `d_7`, any formed `[1/1]` d-log-Pade on physical data,
  any spurious-real-pole / `<P>(6) ~ 1.62` readout, or that the function's
  singularity lives in any particular graph-support class — none is on the
  on-disk record and none is asserted;
- "single-complex-pair falsified" or "multi-pair surviving" (forward claims
  awaiting `d_8`);
- the treewidth-29 figure as a proven barrier (it is a heuristic upper bound,
  unaudited) or as a clean "import -> bounded -> retire" of the no-bulk-transition
  premise;
- closure or repinning of the canonical same-surface plaquette value;
- any audit status (independent audit lane only);
- any new axiom, tag, vocabulary, or meta-framing.

## 12. Key files / cross-references

- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md) (20-route blocked ledger; 0-of-5 route pruning; doubly-walled lane-killer; reference #2245)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md) (exact `d_6`; GF(3) cube-shell certificate; reference #2255)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md) (exact `d_7`; tadpole/geometric falsified; references #2365 / #2374)
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md) (finite-L positivity; Lee-Yang localization; `beta^8` rank floor; d-log-Pade verdict; reference #2395)
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md) (d-log-Pade complex-pair proxy; activation thresholds)
- [`GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md) (Theorem 3 under-determination; Perron spread `>= 0.1937`)
- [`GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md`](GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md) (bridge pins the number; escape needs a new audited primitive)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md) (nonpolynomial hierarchy; no finite truncation closes the value)
- [`GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md) (entire `Z_L`; `P_L = Z'/Z`)
- [`SU3_WIGNER_L3_TREEWIDTH_INFEASIBLE_2026-05-04.md`](SU3_WIGNER_L3_TREEWIDTH_INFEASIBLE_2026-05-04.md) (treewidth-29 heuristic UPPER bound; unaudited; rank-aware contractor nominated as escape)
- [`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md) (`P_inf = 0.59400 +/- 0.00037`, Monte-Carlo comparator only)

**External imports (methodology/comparator only, never derivation inputs):**
Denbleyker-Du-Meurice-Velytsky arXiv:0710.5771 (SU(3) Fisher zeros
`5.54 +/- i0.10`); Meurice group arXiv:0810.1792 / 1112.2734 (infinite-volume
off-axis stabilization); Campostrini-Pelissetto-Rossi-Vicari
arXiv:hep-lat/9602011 (2D O(N) d-log-Pade-vs-MC past-radius caveat); Bars 1980
(Bessel-determinant identity for SU(N) Wilson character integrals). The
`L->infinity` no-real-bulk-transition statement is **not** in this list: it is a
load-bearing dynamical premise filed OPEN (Section 6b), not a free import.

This note is a campaign-level frontier map / synthesis and asserts no closure of
the beta=6 lane. Campaign references #2245 / #2255 / #2365 / #2374 / #2395 /
#2410 are plain-text pointers, not citation-graph dependencies.
