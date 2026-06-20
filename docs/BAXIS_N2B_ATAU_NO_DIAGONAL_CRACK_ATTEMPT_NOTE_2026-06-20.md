# B-AXIS N2b: the no-diagonal-clause crack attempt for the metric time edge `a_tau`

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-20
**Claim type:** bounded_theorem (a metric-blindness no-go for the no-diagonal
spacing-ratio route; the wall it confirms is a minimality statement).
**Status:** unaudited candidate. Graph-visible only so the independent audit lane
can decide. No audit verdict is set here; the owner / independent audit lane is
the sole status authority. No bare `retained` / `promoted`.
**Posture:** OWNER-authorized "don't believe the no-gos." A genuine crack here
would retire candidate N2b entirely. I attacked the last untested no-axiom lead
(the no-diagonal clause SK-1 flagged in `block02_section_SK1.md` section 6) and
report the result honestly.
**Primary runner:** `scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py`
**Cached output:** `logs/runner-cache/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.txt`
(**TOTAL: PASS=17 FAIL=0**; sympy + numpy + a tiny BFS; deterministic, no RNG in
any load-bearing leg; clean under `python3 -W error`; no empirical import).

---

## 1. The target residual and the lead

block02 (SK-1, `scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py`,
`PASS=28 FAIL=0`) banked two facts about the Stone denominator of the 2-step
blocked staggered transfer
`H_hat = -log(T_hat^2) / (2 a_tau)`:

1. the factor **2** in `2 a_tau` is the structural staggered 2-step block count
   (single-step transfer non-positive; `T_hat^2 = T_odd . T_even`, eigenvalues
   `exp(+-2 E)`) — **no axiom**; and
2. `scale_reference x kinetic_isotropy` supply the absolute anchor `a^{-1} = M_Pl`
   and the dimensionless kinetic-**FORM** ratio `c_t/c_s = 1`, but **not** the
   dimensionless metric **SPACING** ratio `a_tau/a_s`.

So the residual that walled is precisely the single metric time edge `a_tau`
(equivalently `a_tau/a_s`). `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09` names a
**different** supplier for that spacing ratio than itself or the scale reference:

> "It does not supply the absolute scale (`scale_reference_primitive`) or the
> **spacing ratio (derived from the no-diagonal clause)**; it supplies only the
> kinetic-form isotropy."

SK-1 section 6 flagged this no-diagonal clause as an **untested** no-axiom lead.
This note tests it. The crux mirrors SK-1's metric-blindness test, but for
**adjacency** instead of kinetic **form**: does the no-diagonal clause FIX
`a_tau/a_s = 1` (a crack), or is it metric-blind (adjacency is topological, so it
cannot fix a metric spacing ratio; a wall)?

---

## 2. The no-diagonal clause, exactly, and its A_min-native status

The "no-diagonal clause" is the **Lattice axiom** itself
(`MINIMAL_AXIOMS_2026-06-05`):

> "The site set is `Z^3` with standard translation action and **nearest-neighbor
> cubic adjacency**."

Read by the companion min-time-step note as "6-NN, **no diagonals**": the only
adjacent sites are the 6 axis neighbors; the 12 face-diagonal and 8 body-diagonal
offsets are forbidden. **It is A_min-native** — part of the Lattice axiom, not a
separate primitive or admission (A1, A2 in the runner).

But the same Lattice axiom, **verbatim**, disavows any metric content:

> "It does not supply a dynamics, boundary condition, **metric scale, lattice
> spacing**, continuum or infrared limit, **causal cone**, ... or physical unit
> conversion."

So the very axiom that supplies the no-diagonal clause forbids reading a metric
spacing out of it (A3). The clause is a **topological** adjacency statement: it
lists which ordered site pairs are neighbors.

---

## 3. What the runner computes

`scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py`, five blocks:

**Block A — state the clause precisely.** A_min-native (Lattice), topological
(6 axis offsets allowed; 12 face + 8 body diagonals forbidden), with the Lattice
axiom's verbatim metric disavowal (A1–A3).

**Block B — adjacency metric-blindness (decisive).** Assign an arbitrary metric
edge length to the temporal vs spatial direction and ask whether the no-diagonal
**property** (which offsets are edges) depends on it. It does not: the edge SET
is **identical** for `a_tau/a_s = 1, 10, 0.137` (B1), while the metric time-edge
length moves freely with the ratio (B2). Symbolic clincher: the adjacency
predicate `|dx|+|dy|+|dz| = 1` has free symbols `{dx,dy,dz}` only — `a_tau, a_s`
**do not appear** (B3). Hence forbidding diagonal hops constrains `a_tau/a_s`
**not at all**; the spacing ratio is free for every nearest-neighbor-only
adjacency (B4). This is the exact mirror of SK-1's kinetic-FORM metric-blindness.

**Block C — count vs metric.** The min-time-step note's load-bearing number is
"one tick reaches Euclidean **1.000 edge**." The BFS reproduces it (6-NN: 6 sites
at graph-distance 1; 26-NN: 26 sites) (C1). But the **hop count** per tick is 1
for *any* temporal metric weight `lambda` (count is topological), while the
**metric** reach `= lambda` varies (C2). So "Euclidean reach 1.000 edge" is a
**tautology** of setting `a_s = a_tau = 1` — it **assumes** `a_tau/a_s = 1`, it
does not derive it (C3). The "one tick = one edge" tie fixes the conformal
**class** (one hop per tick), not the conformal **factor** (the metric spacing).

**Block D — the min-time-step note's other inputs are not A_min-native.** Its
tick/time identification (record tick = the physical time coordinate, hence
`a_tau` as a metric time edge) is **`audited_renaming`** — a naming bridge, not a
retained A_min derivation; the note itself states the ratio closes "only after
that tick/time identification is accepted" (D1). Its `c`-normalization is the SI
`c = 299792458 m/s` admission, and the note says it "does not derive the
emergent-Lorentz-to-physical-`c` bridge" (D2). So the conditional Planck-time
closure `a_tau = l_P/c = t_P` rests on (i) the admitted tick/time bridge and
(ii) the admitted SI unit — **neither A_min-native** — and the ratio it
identifies is the metric-blind count ratio (D3).

**Block E — verdict.** Assembles the chain to the wall (E1–E4).

---

## 4. Verdict — WALL STANDS (the no-diagonal clause does not crack N2b)

A crack would require the no-diagonal clause (A_min) to force `a_tau/a_s = 1`
with **no admitted metric input**. The runner shows:

- the clause is A_min-native but **topological**; the Lattice axiom that supplies
  it verbatim disavows metric scale / spacing / causal cone (A1–A3);
- the no-diagonal **property** is invariant under every `a_tau/a_s`; the
  adjacency predicate carries no `a_tau, a_s` — **adjacency is metric-blind**
  (B1–B4);
- "one tick = one edge / Euclidean reach 1.000" is a **count** in edge units that
  **assumes** `a_tau = a_s`; it does not derive it (C1–C3);
- the only route from the clause to a metric `a_tau/a_s = 1` reads the
  topological **count** (1 hop/tick) **as** a metric spacing — which needs either
  the time edge declared metric-equal to the space edge (an extra spacing datum)
  or the `audited_renaming` tick/time bridge + SI `c` (D1–D3). **None of these is
  supplied by A_min + the four approved primitives.**

Reading the count as a metric is the **same mis-citation pattern** SK-1 found for
the kinetic FORM ratio: it cites a clause for content it does not grant
(`AXIOM_MINIMALITY_POLICY.md` §6 no-laundering discipline; a primitive/axiom
chain-satisfies **only for what it grants**; registry rule 5). The no-diagonal
clause grants the **conformal class** (one hop per tick), not the **conformal
factor** (the metric spacing).

**Therefore the no-diagonal clause does NOT crack N2b. The wall stands.**
`a_tau/a_s` is not derivable from A_min + the four approved primitives.

---

## 5. Consequence for the proposal set

- **N2b is NOT removed by the no-diagonal route.** This was the last untested
  no-axiom lead the SK-1 section flagged; attempting it shows it is the conformal
  **class** (metric-blind), not the conformal **factor**. With SK-1's
  `scale x kinetic_isotropy` join already walled, the proposal set is
  **confirmed complete** on this axis.
- **The genuine N2b residual** is a single dimensionful temporal edge `a_tau`
  (equivalently the dimensionless `a_tau/a_s`). Its weakest sufficient supplier
  is a **minimal spacing primitive**: one dimensionless number `a_tau/a_s`,
  **strictly weaker** than the C1 RP-DYN dynamics axiom and **disjoint** from the
  FORM content `kinetic_isotropy` supplies and the single anchor
  `scale_reference` supplies.
- RP-DYN (C1) proposes only the dynamics-side **existence** of a step (a rate /
  well-defined half-life), never the dimensionful value `2 a_tau`. This wall
  confirms that division of labor: the dynamics-side tick (C1) and the metric
  clock unit (N2b / `a_tau`) are genuinely separate residuals.

---

## 6. Status discipline / policy

- This note reports a **wall** (no axiom proposed, no candidate adopted); the
  metric-blindness result is a bounded no-go for the no-diagonal route.
- No bare `retained` / `promoted`; no audit verdict set; nothing written to
  `docs/audit/data/` (read-only this lane); no `axiom_premise_nodes.json` edit.
- The independent audit lane / owner is the sole status authority.

## 7. One-line outcome

The no-diagonal clause (Lattice axiom's nearest-neighbor cubic adjacency,
A_min-native) is a **topological** statement whose adjacency predicate
`|dx|+|dy|+|dz| = 1` carries no `a_tau, a_s`; it is **metric-blind** to the
spacing ratio (the mirror of SK-1's kinetic-FORM blindness), the "one tick = one
edge" tie is a count that **assumes** `a_tau = a_s`, and the only metric closure
rests on an `audited_renaming` bridge + the SI `c` admission — so the route
**walls**, N2b is confirmed in the proposal set, and the metric residual `a_tau`
needs a minimal spacing primitive strictly weaker than C1
(runner `PASS=17 FAIL=0`).

## 8. Runner

```bash
python3 scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py
```

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Lattice
  axiom supplying the nearest-neighbor cubic adjacency (the no-diagonal clause)
  and its verbatim metric disavowal.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — names the no-diagonal clause as the spacing-ratio supplier; supplies only
  the kinetic FORM isotropy.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  single dimensionful anchor; zero dimensionless content.
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  — the `audited_renaming` tick/edge tie whose "one tick = one edge" count this
  note shows is metric-blind.
- [MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md)
  — the conditional Planck-time closure resting on the tick/time bridge + SI `c`.
