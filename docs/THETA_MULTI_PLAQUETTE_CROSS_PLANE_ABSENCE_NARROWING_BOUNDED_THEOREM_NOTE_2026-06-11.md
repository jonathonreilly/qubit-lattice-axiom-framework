# Theta Multi-Plaquette Cross-Plane Absence Narrowing Under the Adjacency License

**Date:** 2026-06-11
**Claim type:** bounded_theorem (finite enumeration + symbolic coefficient
checks under the explicit unit-neighborhood link-support license)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_theta_multi_plaquette_cross_plane_narrowing_2026_06_11.py`](../scripts/frontier_theta_multi_plaquette_cross_plane_narrowing_2026_06_11.py)
(SCORECARD: PASS=26, FAIL=0; cached:
[`logs/runner-cache/frontier_theta_multi_plaquette_cross_plane_narrowing_2026_06_11.txt`](../logs/runner-cache/frontier_theta_multi_plaquette_cross_plane_narrowing_2026_06_11.txt))

---

## Statement

The landed cross-plane result
([`THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md`](THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md))
proves that single-plaquette action terms carry no local cross-plane
`F tilde F` slot, and names its own boundary: "Multi-plaquette terms, clover
products, or any other action term with cross-plane support are outside this
theorem and reopen the slot." This note presses that boundary **inside the
adjacency-licensed class** of the landed license note
([`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md)),
whose verbatim condition is: for every target link `l=(a,b)` in the support,
every endpoint `p` of every support link must obey
`min(d(p,a), d(p,b)) <= 1` with `d` cubic graph distance.

Three layers, each finite and exhaustively checked by the runner:

1. **(V) Verbatim composite lift — the licensed class is closed at single
   plaquettes.** Applying the license condition unchanged to the *total* link
   support of a candidate local term:
   - a distance lemma (license implies every pair of support sites is at
     graph distance `<= 2`; triangle inequality through the link partner,
     checked exhaustively on a window) makes the classification finite at
     **all** loop lengths;
   - the complete enumeration of rooted simple closed loops inside that
     bound gives **exactly the plaquettes** — 24 rooted licensed loops in
     `d=3`, 48 in `d=4`, none of any other length (this extends the license
     note's length-4/length-6 domain to all lengths);
   - a neighborhood-intersection lemma: the set of sites within distance 1
     of all four edges of a plaquette is exactly that plaquette's four
     sites, and the only lattice links among them are its four edges (no
     diagonals on the 6-NN lattice) — so a licensed support containing a
     plaquette *is* that plaquette;
   - an exhaustive two-plaquette scan (all plane pairs, all relative
     translations `|t|_inf <= 4`, window-complete by the offset bound
     `|o|_inf <= 1`): **zero** two-plaquette unions pass — including
     same-plane dominoes and stacked pairs.

   Consequence: within the verbatim-licensed class, every local
   gauge-invariant term is a single-plaquette term, so the landed
   cross-plane absence covers the whole class — the multi-plaquette
   cross-plane reopening is **empty inside the verbatim license**.

2. **(W) Pairwise-proximity weakening — the absence is robust, not an
   artifact of (V)'s strictness.** Weakening to: each plaquette factor
   individually licensed, every factor *pair* mutually unit-proximate
   (every site of each factor within distance 1 of the other factor's
   sites). Genuine multi-plaquette products now exist (domino, bent, and
   stacked witnesses all pass), but:
   - complementary-plane plaquette pairs (planes sharing no direction —
     exactly the `F_{01}F_{23}`, `F_{02}F_{13}`, `F_{03}F_{12}` ingredients)
     fail at **every** relative translation. Projection lemma: the
     `(mu,nu)`-projection of one factor is the four corners of a unit
     square, the complementary factor projects to a single point, and no
     integer point lies within L1 distance 1 of all four unit-square
     corners (window-exhaustive; tail monotone);
   - every W-licensed plane pair shares a direction (exhaustive scan), and
     in `d=4` distinct coordinate planes share a direction XOR are
     complementary;
   - symbolic criterion: a product of one-plane factors carries a
     cross-plane monomial iff its plane set contains a complementary pair
     (all pairwise-direction-sharing plane sets of size `<= 3` give
     identically zero cross-plane coefficients; complementary-containing
     sets give nonzero — positive control);
   - because the W condition is **pairwise**, the exclusion holds at every
     factor order: a complementary pair inside any W-licensed term would be
     a W-licensed complementary plaquette pair, which does not exist
     (belt-and-braces anchored scan of all 2- and 3-factor clusters).

3. **(X) Honest complement — what reopens the slot, exhibited.**
   - The corner-touching `01 x 23` pair (the cross-plane ingredient of the
     2026-06-07 clover construction) fails both (V) and (W), yet its
     *unrestricted* product carries a nonzero `F01*F23` coefficient: the
     clover reopening of
     `STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md`
     is **preserved**, relocated to: license-external.
   - Chain-connected clusters (connectivity instead of pairwise proximity)
     reopen the slot: an explicit 3-factor chain with plane set
     `{01, 12, 23}` has both adjacent pairs W-licensed, the end pair not,
     and its product carries a nonzero `F01*F23` coefficient. The pairwise
     condition is load-bearing; the chained weakening is the named open
     complement.

`d=3` corollary: among the three spatial coordinate planes no complementary
pair exists at all — the cross-plane pairing needs four distinct lattice
directions, so it intrinsically involves the emergent temporal direction.

## What this narrows

Within the adjacency-licensed surface, the gauge-side residual of the
registered theta admission — "multi-plaquette / large-gauge-winding
account" — narrows: the *local multi-plaquette* part of that account is now
derived-absent under the verbatim license (empty class) and under its
pairwise-proximity weakening (nonempty class, slot still absent at every
factor order). What remains on the gauge side, as the next paths this
opens:

- **chain-connected, non-pairwise-proximate cluster terms** — explicitly
  license-external (the (X) witnesses), the same locus where the 06-07
  clover lives;
- **genuinely global winding-sector data** — the emergent-Q bridge named by
  `THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  (context; unaudited): whether the derived effective action / scaling
  limit produces an emergent integer sector functional with nonvacuous
  weighting. This note tightens that bridge's local edge: a licensed
  effective action that stays within pairwise-proximate plaquette
  composites cannot populate the cross-plane slot at any order.

## Hostile-guard record

Candidate cross-plane-generating combinations constructed and tested
against the licensed class (runner sections E, H, K, L, M):

| candidate | verbatim (V) | pairwise (W) | cross-plane coefficient (unrestricted) |
|---|---|---|---|
| same-plane domino / stacked pair | FAIL | PASS | zero (plane set shares direction) |
| bent pair (planes share one direction) | FAIL | PASS | zero |
| corner-touching `01 x 23` (clover ingredient) | FAIL | FAIL | **nonzero** (`b0*b1`) |
| complementary pair, every translation `|t|_inf <= 4` | FAIL | FAIL | nonzero where unrestricted |
| 3-factor chain `{01,12,23}` | FAIL | end pair FAIL (chain-connected only) | **nonzero** (`a1*b0*b2`) |

The two nonzero rows are the honest boundary: both live outside the
licensed class (V and W). No licensed combination with a nonzero
cross-plane coefficient was found, and for (V) and (W) the absence is
proven for the whole class (complete loop classification; pairwise
projection lemma), not just the scanned window.

## Boundaries

- The unit-neighborhood link-support license is the **consumed input**, as
  in the license note. This note does not derive the license from the
  axioms, Record, or any primitive, and does not derive per-plaquette or
  pairwise-proximate minimality of the physical action.
- The (W) lift is one explicit, natural weakening (mutual unit-proximity of
  factor site sets). Other weakenings — in particular chain-connectivity —
  are shown to reopen the slot and are named open, not excluded.
- Single-trace terms over longer loops are handled only by (V) (where they
  are excluded at all lengths); under (W) the class is defined as products
  of licensed plaquette factors, and longer single traces are outside it.
- Nothing here sets `theta_QCD = 0`, retires the strong-CP Tier-A
  admission, chooses an action functional, fixes a coupling, supplies
  dynamics, a probability rule, a measure, a continuum limit, or an
  empirical match. Global winding-sector / emergent-Q questions are
  untouched.
- The 06-07 clover admissibility result is preserved, not contradicted:
  the clover is admissible in the unrestricted local class and is here
  located outside the licensed class.
- This note does not change any audit status or effective status.

## Honest-auditor read

"Within the adjacency-licensed action class — an input with retained_bounded
finite-enumeration support, not a derived wall — local multi-plaquette
composites cannot populate the cross-plane `F tilde F` slot: the verbatim
composite license admits only single plaquettes (complete classification, all
loop lengths), and the natural pairwise weakening admits genuine
multi-plaquette products whose plane sets provably never contain a
complementary pair. The reopenings that survive are exactly the
license-external ones the framework already names: chained clusters / clover
terms, and global winding-sector data. The theorem is conditional on the
license; it derives nothing about whether physical dynamics respects it."

## Dependencies (citation-graph visible)

- [`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — `per_plaquette_from_adjacency_license_bounded_theorem_note_2026-06-09`,
  effective_status **retained_bounded** (origin/main ledger, checked
  2026-06-11). Supplies the verbatim license condition (pinned by the
  runner) and the length-4/6 anchor counts reproduced here.
- [`THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md`](THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — `theta_cross_plane_term_absent_in_supplied_per_plaquette_class_bounded_theorem_note_2026-06-09`,
  effective_status **retained_bounded** (origin/main ledger, checked
  2026-06-11). Supplies the single-plaquette cross-plane absence this note
  extends and the multi-plaquette boundary sentence this note narrows
  (pinned by the runner). The mixed-derivative core is reproven here.

Context (not load-bearing; both **unaudited** on the origin/main ledger,
named for boundary fidelity only — no content is consumed from them in the
derivation):

- `STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md`
  — the clover reopening, preserved here as license-external.
- `THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  — the emergent-Q bridge whose local edge this note tightens.
- `STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md` — the registered
  admission whose gauge-side residual wording this note addresses.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only
status authority.

## Verification

```bash
python3 scripts/frontier_theta_multi_plaquette_cross_plane_narrowing_2026_06_11.py
```

Expected: 26 `[PASS]` lines, `TOTAL: PASS=26 FAIL=0`, then the bounded
verdict paragraph. Exit code 0 iff FAIL=0. Deterministic; peak memory
~60 MB (small combinatorics + sympy polynomials, nothing dense).
