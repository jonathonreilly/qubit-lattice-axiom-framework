# Block 13 Report — GVP infinite-hierarchy obstruction (U(1) sharpening)

**Branch:** `physics-loop/gauge-vacuum-plaquette-infinite-hierarchy-block13-2026-05-17`
**Target row:** `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`
  (briefed as "unaudited"; ledger reality is `audited_clean` /
  `retained_no_go` per 2026-05-12 judicial third-pass audit)
**Status delivered:** scope-bounded **positive narrow theorem**
(`positive_theorem`) sharpening the parent retained no-go on U(1).
Parent row unchanged.

## What landed

1. **Source theorem note:**
   `docs/GAUGE_VACUUM_PLAQUETTE_U1_DENSITY_SIGN_ALTERNATION_NARROW_NOTE_2026-05-17.md`
   Positive narrow theorem: on U(1), the diagonal generator
   `K_1(t) = log I_0(t)` has Taylor expansion `Σ c_n t^n` with
   - (D1) `c_{2k-1} = 0` for every k ≥ 1
   - (D2) `c_{2k} ≠ 0` for every k ≥ 1
   - (D3) `sign(c_{2k}) = (-1)^(k+1)` for every k ≥ 1.

2. **Paired runner:**
   `scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py`
   `SUMMARY: THEOREM PASS=7 SUPPORT=5 FAIL=0`. Verifies (D1)-(D3) at
   exact-rational precision through k = 20 (order t^40), reproduces
   the Riccati recurrence from sympy Taylor, checks the explicit
   `c_{2k} = a_{k-1}/(2k)` identity, cross-validates via the alternative
   `log(1+g)` series for k = 1..10, and confirms numerically at
   k = 25, 30, 40, 50 via mpmath.

3. **Cached output:**
   `logs/runner-cache/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.txt`
   (SHA-pinned, status ok, exit_code 0, elapsed ~8s).

4. **Control-plane wiring** (the new note + runner appended to existing
   rows next to the parent obstruction note in):
   - `docs/CANONICAL_HARNESS_INDEX.md`
   - `docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP.md`
   - `docs/publication/ci3_z3/DERIVATION_ATLAS.md`
     (both the dedicated obstruction row and the bridge-support stack row;
     the dedicated row's authority line now also names the sharpening)

5. **Block artifacts** (this directory):
   - `V1_V5_SCRATCH.md` — distinct-angle scratch
   - `BLOCK_REPORT.md` — this file

## V1-V5 chosen angle

- V1 — quantitative uniform truncation-error bound: rejected
  (decoration of L4 in the companion lemmas note).
- V2 — extend to SU(2), SU(3): rejected (requires Weingarten / higher
  character-orthogonality machinery beyond parent BA admissions; not
  A_min-compatible).
- V3 — global generating recurrence for finite-volume K_L: rejected
  (would close analytic P(6); out of scope).
- V4 — strengthen "K_1 → ∞" to "K_1 > 0": rejected (trivial decoration
  of L2.b).
- **V5 (chosen)** — Riccati-derived density and sign-alternation theorem
  on U(1). The diagonal generator's derivative `r(t) = I_1/I_0`
  satisfies the Riccati equation `t r' + r + t r² = t`, which yields
  the exact recurrence `a_n = -(1/(2(n+1))) Σ_{j+k=n-1} a_j a_k` for
  n ≥ 1 with `a_0 = 1/2`. An elementary induction proves
  `sign(a_n) = (-1)^n` and `a_n ≠ 0`, hence the claim on c_{2k}.

## Distinct from parent and sister notes

- **Parent** (`infinite_hierarchy_obstruction`) proves "K_1 is not a
  polynomial". V5 proves "every even-order coefficient is strictly
  nonzero with explicit alternating sign". Strictly stronger no-go
  structure on the U(1) instance.
- **Companion** (`hierarchy_obstruction_lemmas`) supplies BA-1..BA-4
  endpoint, analyticity, finite-Taylor-support, and polynomial-growth
  lemmas. V5 uses none of those; it uses only the Bessel ODE and an
  elementary parity argument. Different proof structure.
- The structural escape "maybe sparse / gap-pattern truncation closes
  the hierarchy" is foreclosed by (D2)+(D3) on the U(1) instance.

## Hard rules

A_min only:
- A1 = Cl(3) local algebra, A2 = Z^3 substrate (framework baseline).
- U(1) plaquette F(U) = cos θ and Z_1(t) = I_0(t) already in parent
  BA-1 / BA-3.
- Bessel ODE and even/odd parity of I_0/I_1: textbook special-function
  calculus, no new framework primitive.

## Honest scope

- Parent row remains `retained_no_go` (audit lane sole authority).
- This new note is a **source-note proposal**; its `effective_status`
  is set by the independent audit lane.
- Does NOT close analytic `P(6)`, `chi_L(beta)`, an explicit
  nonpolynomial solution of the connected hierarchy, or extend the
  sign-alternation to SU(2)/SU(3).
- Sharpens the U(1) one-plaquette block obstruction only.

## Verification command

```bash
cd /private/tmp/physics-loop-2026-05-17/block13-gvp-infinite-hierarchy
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py
```

Expected: `SUMMARY: THEOREM PASS=7 SUPPORT=5 FAIL=0`.
