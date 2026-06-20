# block03 — Section: NODIAG — can the no-diagonal clause derive `a_tau/a_s`
(the B-AXIS N2b metric residual) with no new axiom?

**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block03-20260620`.
**Target:** the residual of B-AXIS **N2b** after block02 — the single metric time
edge `a_tau` (equivalently the dimensionless spacing ratio `a_tau/a_s`; block02
showed the factor 2 in `2 a_tau` is no-axiom structural). Test the **last**
untested no-axiom lead: the **no-diagonal clause** that
`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09` names as the spacing-ratio supplier
("the spacing ratio (derived from the no-diagonal clause)"), flagged in
`block02_section_SK1.md` §6.
**Scope:** A_min (Lattice + Quantum + Record) + the four approved primitives
(`axiom_premise_nodes.json`: `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) ONLY. A crack = derive
`a_tau/a_s` with NO new axiom/primitive and NO mis-citation (registry rule 5;
`AXIOM_MINIMALITY_POLICY.md` §6).
**Posture:** OWNER-authorized "don't believe the no-gos."

**Deliverables**
- Note: `docs/BAXIS_N2B_ATAU_NO_DIAGONAL_CRACK_ATTEMPT_NOTE_2026-06-20.md`
- Runner: `scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py`
- Runner cache: `logs/runner-cache/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.txt`
  — **TOTAL: PASS=17 FAIL=0** (sympy + numpy + a tiny BFS; deterministic; no RNG
  in any load-bearing leg; clean under `python3 -W error`; no empirical import).

---

## 1. The no-diagonal clause, exactly, and its A_min-native status

The clause IS the **Lattice axiom** (`MINIMAL_AXIOMS_2026-06-05`): "The site set
is `Z^3` with standard translation action and **nearest-neighbor cubic
adjacency**" — read by the min-time-step companion as "6-NN, **no diagonals**":
only the 6 axis neighbors are adjacent; the 12 face + 8 body diagonal offsets are
forbidden. **It is A_min-native** (part of the Lattice axiom, not a separate
primitive/admission). But the same axiom **verbatim** disavows metric content:
"does not supply a ... **metric scale, lattice spacing**, ... **causal cone**,
... or physical unit conversion." So the clause is **topological** (which sites
are neighbors), and the axiom that gives it forbids reading a metric out of it.

## 2. The crux, and the runner that tests it

The crux mirrors SK-1 but for **adjacency**, not kinetic **form**: does forbidding
diagonal hops FIX `a_tau/a_s = 1` (crack), or is adjacency metric-blind (wall)?
`scripts/baxis_n2b_no_diagonal_spacing_crack_2026_06_20.py`, five blocks:

- **A** — state the clause: A_min-native, topological, with the Lattice axiom's
  verbatim metric disavowal (A1–A3).
- **B (decisive)** — adjacency metric-blindness. The no-diagonal edge SET is
  **identical** for `a_tau/a_s = 1, 10, 0.137` (B1) while the metric time-edge
  length moves freely (B2); the adjacency predicate `|dx|+|dy|+|dz| = 1` has free
  symbols `{dx,dy,dz}` only — `a_tau, a_s` absent (B3). Forbidding diagonals
  constrains `a_tau/a_s` **not at all** (B4).
- **C** — count vs metric. BFS reproduces "one tick reaches 6 sites / 26 with
  diagonals" (C1); but the hop **count** per tick is 1 for any temporal metric
  weight while the **metric** reach varies (C2), so "Euclidean reach 1.000 edge"
  is a tautology of setting `a_s = a_tau = 1` — it **assumes** `a_tau/a_s = 1`,
  it does not derive it (C3).
- **D** — the min-time-step note's other inputs. Its tick/time identification is
  **`audited_renaming`** (a naming bridge, the note says the ratio closes "only
  after that tick/time identification is accepted") (D1), and its `c` is the SI
  `299792458 m/s` admission (D2). Neither is A_min-native (D3).
- **E** — verdict logic (E1–E4).

## 3. Verbatim disavowal / mis-citation check (registry rule 5)

> **Lattice axiom** (`MINIMAL_AXIOMS_2026-06-05`). GRANTS: "nearest-neighbor
> cubic adjacency." DISAVOWS: "does not supply a ... metric scale, lattice
> spacing, ... causal cone, ... or physical unit conversion."

> **`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09`.** Names the no-diagonal clause
> as the spacing supplier but "supplies only the kinetic-**form** isotropy."

The no-diagonal clause grants an **adjacency topology**, not a metric. The only
path from it to a metric `a_tau/a_s = 1` reads the topological **count** (1
hop/tick) **as** a metric spacing — the same laundering `AXIOM_MINIMALITY_POLICY`
§6 forbids (a clause chain-satisfies **only for what it grants**; registry rule
5). This attempt does **not** mis-cite; it shows exactly **why** the wall stands.

## 4. Verdict — WALL STANDS

The no-diagonal clause is **adjacency metric-blind**: A_min-native but
topological, invariant under every `a_tau/a_s`. It supplies the **conformal
class** (one hop per tick), not the **conformal factor** (the metric spacing).
The "one tick = one edge" count assumes `a_tau = a_s`; the only metric closure
rests on an `audited_renaming` bridge + the SI `c` admission. **`a_tau/a_s` is
NOT derivable from A_min + the four approved primitives via the no-diagonal
clause.**

## 5. Consequence for the proposal set

- **N2b is NOT removed.** This was the last untested no-axiom lead (SK-1 §6).
  With SK-1's `scale x kinetic_isotropy` join already walled, the proposal set is
  **confirmed complete** on this axis.
- The genuine N2b residual is one dimensionful `a_tau` (= `a_tau/a_s`); its
  weakest sufficient supplier is a **minimal spacing primitive** (one
  dimensionless `a_tau/a_s`), **strictly weaker** than the C1 RP-DYN dynamics
  axiom and **disjoint** from `kinetic_isotropy`'s FORM content and
  `scale_reference`'s single anchor.
- Confirms the C1/N2b division of labor: the dynamics-side step existence (C1)
  and the metric clock unit (`a_tau`) are genuinely separate residuals.

## 6. Status discipline / policy

- Reports a **wall** (no axiom proposed, no candidate adopted) + a bounded
  metric-blindness no-go for the no-diagonal route.
- No bare `retained` / `promoted`; no audit verdict set; nothing written to
  `docs/audit/data/` (read-only this lane); no `axiom_premise_nodes.json` edit.
- The independent audit lane / owner is the sole status authority.

## 7. One-line outcome

NODIAG **walls**: the no-diagonal clause (Lattice axiom adjacency, A_min-native)
is topological — its predicate `|dx|+|dy|+|dz| = 1` carries no `a_tau, a_s`, so it
is metric-blind to the spacing ratio (the mirror of SK-1's FORM blindness); the
"one tick = one edge" count assumes `a_tau = a_s` and the only metric closure
rests on an `audited_renaming` bridge + SI `c`; so `a_tau/a_s` is not derivable
from A_min + the four approved primitives, N2b is confirmed in the proposal set,
and the metric residual `a_tau` needs a minimal spacing primitive strictly weaker
than C1 (runner `PASS=17 FAIL=0`).
