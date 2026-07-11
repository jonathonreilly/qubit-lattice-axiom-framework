# Occupancy from Locked Record Outcomes: Flavor Piece (i) Bridge (Bounded Note)

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets no audit
outcome and changes no registry row.
**Current-main posture (2026-07-07):** the Tier-A admission count is already
zero on main. This note is banked only as bounded historical/supporting science
for the flavor occupancy bridge; it does not reopen, modify, or supply
authority for any admission or retirement record.

**Repair update:** 2026-07-11 — an independent audit (2026-07-10) failed the
companion orbit-occupancy note for an arithmetic error in its `rho`-map. This
note **inherited** the same contaminated arithmetic in its T2 negative control
(the Result T2 negative-control passage and runner CHECK 13). The `rho`-map r-attribution is
withdrawn and replaced by the equipartition-granularity framing;
`Z_sector/Z_orbit = 2` is retained as a normalization / determinant-power fact
**decoupled from `r`**. Companion to PR #5162 (the 2026-06-09 note's source-side
repair). The T1 localization and the T2 slot-counting collision exhibit are a
separate, uncontested argument and are unchanged. See the
**Repair (2026-07-11)** section below.

**Primary runner:**
[`scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py`](../scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.txt`](../logs/runner-cache/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.txt)

## Repair (2026-07-11): inherited `rho`-map r-attribution withdrawn

An independent audit (2026-07-10) failed the companion orbit-occupancy note
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
for an arithmetic error in its `rho`-map. Verbatim finding:

> "The holomorphic Gaussian integral does not yield the claimed one-slot
> equipartition moment: with Z=pi/g and g=6 beta, it gives &lt;|b|^2&gt;=1/(6 beta),
> hence r=1, not 1/2. The runner obtains r=1/2 by hard-coding a per-slot quantum
> rather than deriving it from that integral."

**The inheritance.** This note reproduced the same withdrawn `rho` arithmetic in
its T2 negative control. The passage revised below, and the runner's CHECK 13,
carried the `rho`-map `r = 1/(2ρ)` with `ρ = (π/g)/Z_d`, reading `r = 1` and
`r = 1/2` off the partition-normalization ratio `Z_sector/Z_orbit = 2`. That
attribution is withdrawn here for the same reason the audit gave on the source
side: the honest Gaussian moment is **normalization-independent** — the `Z`
ratio cancels in the moment ratio — and gives `r = 1` for *both* bookkeepings,
so `Z_d` does not set `r`.

**What changed, and what did not.**

- **Withdrawn:** the `rho`-map `r = 1/(2ρ)` and every statement that the
  `Z`-ratio *sets* the `r`-ratio (runner CHECK 13 rewritten; the lines below
  rewritten).
- **Retained as a true fact, relabeled:** `Z_sector/Z_orbit = 2` is a
  normalization / determinant-power fact only, decoupled from `r` (runner
  CHECK 12, now paired with an honest `sympy` moment check confirming the
  second moment `⟨|b|²⟩` is the same under both bookkeepings, so the moment
  `r` is invariant to that choice — mirroring the companion runner's O3A).
- **Corrected r-attribution:** the two `r`-endpoints are exact solutions of two
  realized-state equipartition **laws** differing only in granularity — per
  **real mode** (sector cell: `E_s = ε`, `E_d = 2ε` ⟹ `r = 1`) versus per
  **outcome cell** (orbit cell: `E_s = E_d` ⟹ `r = 1/2`, and `Q = 2/3` via
  `Q = (1+2r)/3`). The quantum `ε` cancels in `r`; nothing is hard-coded on a
  derivation path.
- **Untouched:** the T1 K-real-section localization (Result T1) and the T2
  slot-counting collision exhibit against the two Record sentences (Result T2's
  collision passage). That collision argument — one locked complex outcome
  assigned two slots by the Re/Im split versus one slot by the locked outcome —
  is a separate argument, is not contested by the audit, and is not weakened,
  expanded, or re-editorialized here. Only the downstream `r`-attribution step
  was contaminated.

This repair is the companion to the 2026-06-09 note's **Repair (2026-07-11)**
section (in-flight as PR #5162), which withdrew the `rho`-map on the source side
and recharacterized the two witnesses as realized-state equipartition laws
differing only in granularity. This note sets no audit status; the audit lane
owns the re-check. Runner after repair: `TOTAL: PASS=13 FAIL=0`.

## Question

Does the generation-sector statistical measure attach to locked
record-outcomes, with one slot per locked admissible possibility, rather than
to the real-analytic mode count of the fluctuation energy?

The bridge candidate tested here is narrow:

> The generation-sector statistical measure is graded by locked
> record-outcomes, one slot per locked admissible possibility, hence one
> K/CPT orbit, not by the real-analytic mode count of the fluctuation energy.

The question is downstream of the first-order determinant construction in
[`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md),
the static-readout walls in
[`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md),
and the sector-versus-orbit occupancy atom in
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md).
The two live Record sentences are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), and the runner
guards them at runtime:

> "When present, a record locks exactly one admissible local possibility."

> "A readout value is determined by record content
> alone."

## Result

**T1: channel-generality for the localization.** For a family of exact real
small-matrix channels
`A_X(a,b,c) = a I + b X + c X^T`, the runner computes the determinant formulas
symbolically. With `c` independent, every determinant is harmonic in
`(Re b, Im b)` and has no `bbar` coefficient. On the K-real section
`c = conj(b)`, the mixed `b,bbar` term appears exactly:

```text
cycle:        d_b d_bbar det = -3a
two_step_path d_b d_bbar det = -2a
single_edge:  d_b d_bbar det = -a
two_edge_star d_b d_bbar det = -2a
```

The runner also includes a conjugate-contaminated negative control. If a channel
imports `bbar` before the K-real restriction, the off-line mixed curvature is
nonzero, so the localization test is not vacuous.

This closes the 2026-06-11 note's declared residual only at this bounded level:
the localization is not special to one hand-picked rotation channel inside this
reciprocal real-channel family.

**T2: two-records collision exhibit.** Under the stated reading

```text
one record = one locked admissible local possibility = one statistical slot,
```

the sector grading requires one complex locked value `b` to be read as two
independent registered data, `(Re b, Im b)`. That is a collision exhibit with
the two Record sentences above: one locked possibility is assigned two slots,
and the slot multiplicity is changed by the real-coordinate split rather than
by record content alone. The orbit grading assigns one slot to the locked
outcome and respects both sentences under the same reading.

The runner's T2 negative control separates a true partition-normalization fact
from the `r`-attribution. `Z_sector / Z_orbit = 2` is a genuine normalization /
determinant-power fact (the two-registered-data bookkeeping changes the doublet
partition by the fiber-count factor 2), but it does **not**, by itself, set the
doublet `r`: the honest Gaussian moment is normalization-independent — the `Z`
ratio cancels — and gives `r = 1` for both bookkeepings. The two `r`-endpoints
arise instead as exact solutions of two realized-state equipartition laws
differing only in granularity: per real mode (sector cell: `E_s = ε`,
`E_d = 2ε` ⟹ `r = 1`) versus per outcome cell (orbit cell: `E_s = E_d` ⟹
`r = 1/2`, and `Q = 2/3` via `Q = (1+2r)/3`). See the **Repair (2026-07-11)**
section above and the companion 2026-06-09 note's Repair section (in-flight as
PR #5162).

The honesty boundary is sharp. T2 is not a full derivation unless the
one-record-one-slot identification is supplied. The remaining bridge is:

> one record locking one admissible local possibility is one statistical slot,
> and the relevant locked possibilities for the generation doublet are the
> K/CPT record-outcome orbits rather than the real components of the
> fluctuation coordinate.

## Boundaries

Wall 1 from the static-readout no-go is avoided by counting record-outcomes,
not by counting algebraic components:

> "Transferring an operator-symmetry onto "the energy counts `b` once" is a category slip and is **circular** (it assumes the asymmetric `(1,1)` split it claims to derive)."

This note never argues that `b` counts once because it is one complex number.
It argues only the conditional Record-side claim: if one locked admissible
possibility is one statistical slot, then the slot follows the locked outcome,
not the real-coordinate split of the fluctuation energy.

Wall 2 from the static-readout no-go is avoided by not using the native complex
structure as a selector:

> "A static complex structure that commutes with `M` and preserves every measure can **define** a holomorphic readout but provably cannot **select** it — both `(1,1)` and `(1,2)` are `J_cs`-invariant."

The runner does not invoke `J_cs` to choose the count. T1 uses the exact
independent-channel versus K-real-section distinction; T2 uses the live Record
sentences plus the explicitly named one-record-one-slot reading.

This note does not derive the generation Yukawa form, species content, the
R-eta construction, or a physical horn. It does not change audit data or any
registry entry. It does not consume PDG values, fitted numbers, or empirical
comparators.

## Residues

- The remaining supplied bridge is: one record locking one admissible local
  possibility is one statistical slot, and the relevant locked possibilities
  for the generation doublet are the K/CPT record-outcome orbits rather than
  the real components of the fluctuation coordinate.
- The R-eta atoms A1/A2 are untouched.
- The species piece is untouched.
- The audit lane owns statuses.

## Primary Runner

Run:

```bash
python3 scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py
```

Expected terminal form: `CHECK NN: PASS/FAIL -- <description>` lines followed
by the five-line summary whose final line is `TOTAL: PASS=13 FAIL=0`.
