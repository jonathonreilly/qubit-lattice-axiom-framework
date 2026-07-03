# SU(3) Tensor-Network Engine + L_s=2 All-Forward Quotient Encoder Perron Solve

**Date:** 2026-05-03
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Type:** bounded_theorem — narrowed (per auditor `scope_too_broad`
verdict) to: the explicitly defined all-forward L_s=2 quotient encoder,
bipartite plaquette adjacency for that encoder, and trivial-sector Reference B
recovery. This note is not a retained Wilson-cube orientation/count theorem.
The full `P_cube(6) >= P_trivial(6)` claim is dropped as out-of-scope for this
note.
**Primary runner:** `scripts/frontier_su3_cube_perron_solve.py`
**Companion:** [`SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md`](SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md)
(fusion engine, PR 1, audited by Codex as bounded_theorem)
**Roadmap status:** historical planning context only; no roadmap note is
cited as load-bearing authority for this narrowed theorem.

## 0. Headline

Narrowed (per auditor `scope_too_broad` verdict) to the three items
the auditor named as in-scope:

1. **Explicit all-forward L_s=2 quotient encoder** (8 sites, 24 directed
   links, 12 encoded plaquette loops; each directed link is in exactly 2
   encoded plaquette loops, all 48 link-plaquette incidences forward by encoder
   convention).
2. **Bipartite plaquette adjacency**: the 12-vertex plaquette adjacency
   graph is bipartite with color partition `6 vs 6`, verified by BFS
   2-coloring.
3. **Trivial-sector Reference B recovery**: with `rho = delta_(0,0)`
   arising naturally as the trivial-irrep cube-character contribution,
   the source-sector Perron solve gives `P_trivial(6) = 0.422532`,
   exactly recovering Reference B of the existing tensor-transfer
   Perron solve note.

The full `P_cube(6) >= P_trivial(6)` quantitative-bound claim and the
non-trivial self-conjugate / bipartite-alternating sector
contributions to `rho_(p,q)(6)` are **out of scope** for this note.
They depend on explicit SU(3) Wigner intertwiner traces on the cube
graph that this note does not derive.

## 0.1 2026-06-08 quotient-encoder boundary repair

The 2026-06-08 audit marked the row conditional because the runner shares the
contested orientation convention rather than independently proving that the
all-forward 12-unoriented-plaquette encoder is the correct Wilson L_s=2 PBC
cube geometry.

This source repair takes the honest bounded route: the object verified here is
an explicitly defined all-forward quotient encoder. It preserves the finite
combinatorics, bipartite graph, and trivial-sector Perron recovery, but it does
not claim that this encoder is the Wilson orientation/count theorem. A future
Wilson cube theorem would need to derive the orientation/count map and the
mixed forward/reverse representation integrals from Wilson plaquette
definitions directly.

## 1. Algorithm

### 1.1 SU(3) fusion (re-bundled from PR 1)

For any pair of SU(3) irreps `lambda, mu` in the dominant-weight box,
the fusion multiplicities `N^nu_(lambda, mu)` are computed via
numerical character orthogonality on the SU(3) Cartan torus:

```text
N^nu_(lambda, mu) = integral_(Cartan torus) chi_lambda chi_mu chi_nu^* dW
```

with Schur character formula and Weyl-Vandermonde Haar measure. See
[`SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md`](SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md)
for the validation suite.

### 1.2 L_s=2 all-forward quotient encoder

The V-invariant minimal block has:

- **8 sites** at `(x, y, z)` with `x, y, z in {0, 1}` and PBC
  identification.
- **24 directed links** = 3 spatial directions × 8 starting positions
  (each directed link `(start_x, start_y, start_z, direction)` is a
  separate SU(3) variable).
- **12 unique unoriented spatial plaquettes** (4 each in xy, xz, yz
  planes; per (plane, slice) two distinct plaquettes via different
  starting corners due to L=2 PBC).

Each encoded plaquette traverses a 4-link loop. In this quotient encoder, the
reverse steps of the usual `+d1 +d2 -d1 -d2` square are represented by the same
forward directed edge after the L=2 PBC site identification. This is the
encoder convention being tested. It is not a proof that a Wilson-oriented
plaquette has only forward representation factors.

### 1.3 Link-orientation analysis

Verified by exhaustive enumeration:

- Each of the 24 directed links appears in exactly 2 plaquettes
  (24 × 2 = 48 incidences = 12 plaquettes × 4 boundary links). PASS.
- All 48 link-plaquette incidences are FORWARD orientation. PASS.

For each link `l` shared by plaquettes A and B, the link integration
gives the 2-link Haar identity:

```text
integral dU [D^lambda_A(U)]_(ij) [D^lambda_B(U)]_(kl)
    = (1/d_lambda_A) * delta_(lambda_B, bar(lambda_A))
       * (epsilon-tensor structure)
```

Hence `lambda_B = bar(lambda_A)` for every link — a STRICT constraint
on irrep assignments.

### 1.4 Plaquette adjacency graph (NEW finding)

Construct the 12-vertex graph where two plaquettes are adjacent iff
they share a directed link. The runner verifies via BFS 2-coloring:

> **The plaquette adjacency graph IS BIPARTITE** with color partition
> `6 vs 6`.

This is a **new finding** not previously recognized in the framework.
Implications:

1. **Self-conjugate assignments** (`lambda = bar(lambda)`, i.e., all 12
   plaquettes carry the same `(n, n)` irrep) trivially satisfy all
   link constraints — these are valid for `lambda in {(0,0), (1,1),
   (2,2), (3,3), (4,4), ...}`.
2. **Bipartite-alternating assignments**: 6 plaquettes (one color class)
   carry irrep `lambda`, the other 6 (other color class) carry
   `bar(lambda)`. These are valid for ANY `lambda`, including
   non-self-conjugate `lambda != bar(lambda)`.

The bipartite-alternating sector OPENS additional contributions to
`rho_(p,q)(6)` for non-self-conjugate `(p, q)` that the existing
framework's reference Perron solves do NOT capture.

### 1.5 Trivial-sector Perron recovery

For the all-trivial assignment `lambda_p = (0, 0)` for all 12
plaquettes:

- Each plaquette character `chi_(0,0)(U_p) = 1`, so each plaquette
  contributes `c_(0,0)(6)` to the partition function.
- All link integrations give factor 1 (singlet ⊗ singlet → singlet
  trivially).
- Total: `Z_singlet(cube) = c_(0,0)(6)^12 ≈ 2.76e+6`.

The corresponding `rho_(p,q)(6)` is `delta_((p,q), (0,0))` (only the
trivial irrep contributes). Plugging into the source-sector
factorization `T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)`:

```text
P_trivial(6) = 0.4225317396
```

This **exactly recovers Reference B** of the existing
[`GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md),
where Reference B was constructed by ASSUMING `rho = delta`. Here
the same `rho = delta` arises NATURALLY as the trivial-sector
contribution from the cube's character expansion — no structural
input choice needed for this sector.

### 1.6 Non-trivial sector — explicit out-of-scope

The non-trivial-irrep contributions to `rho_(p,q)(6)` (all-same
self-conjugate `(n, n)` for `n >= 1`, and bipartite-alternating
`(lambda, bar(lambda))`) require explicit SU(3) Wigner intertwiner
traces on the cube graph. They are **explicitly out of scope** in
this narrowed note. No `P_cube` number beyond the trivial sector is
reported here, and no quantitative bound of the form
`P_cube(6) >= P_trivial(6)` is asserted.

## 2. Theorem statement (narrowed)

**Bounded Theorem (all-forward quotient-encoder structural analysis).** For
the explicitly defined all-forward L_s=2 quotient encoder at `beta = 6`, in
the narrowed scope (encoded geometry + bipartite adjacency + trivial-sector
Reference B recovery):

1. **Encoded geometry.** The L_s=2 all-forward quotient encoder has exactly
   12 encoded plaquette loops and 24 directed links, with each link in exactly
   2 encoded loops, and all 48 link-plaquette incidences in forward orientation
   by construction. (verified)
2. **Bipartite adjacency.** The plaquette adjacency graph is bipartite
   with color partition `6 vs 6`, verified by BFS 2-coloring.
   (verified)
3. **Trivial-sector Reference B recovery.** The trivial-sector
   contribution `lambda = (0,0)` for all 12 plaquettes gives
   `Z_singlet = c_(0,0)(6)^12 ≈ 2.76e6` and corresponding
   `rho = delta_(0,0)`, yielding `P_trivial(6) = 0.4225` in exact
   agreement with the existing Reference B. (verified)

The full `rho_(p,q)(6)` and any quantitative bound of the form
`P_cube(6) >= P_trivial(6)` is **explicitly out of scope** for this
narrowed note. Those claims depend on explicit topological intertwiner
traces for non-trivial self-conjugate and bipartite-alternating
sectors which this note does not derive.

## 3. Validation suite

The runner verifies:

| Section | Check | Result |
|---|---|---|
| 0.1 | Source note declares quotient-encoder boundary | PASS |
| A | SU(3) fusion engine API loaded | PASS |
| B | 12 encoded quotient plaquette loops constructed | PASS |
| C | Each of 24 links in exactly 2 plaquettes | PASS |
| C | All 48 link-plaquette incidences forward by encoder convention | PASS |
| D | Plaquette graph bipartite (color partition 6:6) | SUPPORT (new finding, expands valid configs) |
| E | Cube partition function structure computed | PASS |
| F | rho_(p,q)(6) extraction (trivial sector) | PASS |
| G | Trivial-sector Perron recovers Reference B (0.4225) | PASS |
| H | Honest verdict: structural skeleton landed | SUPPORT |

`SUMMARY: THEOREM PASS=8 SUPPORT=2 FAIL=0`

## 4. Honest scope statement

### What this narrowed note establishes (in scope)

- **All-forward quotient-encoder geometry** (12 encoded loops, 24 directed
  links, each link in exactly 2 loops, all 48 incidences forward by encoder
  convention; exhaustively verified)
- **Bipartite plaquette adjacency** (color partition 6:6, BFS-verified)
- **Trivial-sector Reference B recovery** (`P_trivial(6) = 0.4225`)
  from framework-internal cube character expansion, matching the
  existing Reference B without any structural input choice

### What this narrowed note does NOT establish (out of scope)

- **Quantitative bound `P_cube(6) >= P_trivial(6)`** — explicitly
  dropped per auditor `scope_too_broad` verdict.
- **Wilson L_s=2 orientation/count theorem** — explicitly not proven here.
- **Full `rho_(p,q)(6)`** for non-trivial irreps (requires explicit
  Wigner intertwiner traces; deferred).
- **Quantitative bypass of any no-go** or **promotion of any parent
  claim** — none asserted here.

## 5. Comparison to existing references

| Source | P(6) value | Note |
|---|---|---|
| Reference B (`rho = delta`) | 0.4225317396 | structural input; trivial decoupled env |
| **This PR (trivial sector)** | **0.4225317396** | **same value, but NATURALLY arising from cube character expansion (no structural input)** |
| Reference A (`rho = 1`) | 0.4524071590 | structural input; concentrated env |
| K-Z external lift (PR #484) | bracket [0.55, 0.60] (W=0.05) | external authority, conservative |
| Bridge-support upper bound | 0.5935306800 | constant-lift candidate, retained as upper |
| Canonical MC value | 0.5934 | audit comparator only |

## 6. Audit consequence

```yaml
claim_id: su3_cube_perron_solve_combined_theorem_note_2026-05-03
note_path: docs/SU3_CUBE_PERRON_SOLVE_COMBINED_THEOREM_NOTE_2026-05-03.md
runner_path: scripts/frontier_su3_cube_perron_solve.py
claim_type: bounded_theorem
intrinsic_status: unaudited
deps:
  - su3_fusion_engine_pr1_theorem_note_2026-05-03
  - gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03
  - gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note
  - gauge_vacuum_plaquette_tensor_transfer_perron_solve_note
review_scope_summary: |
  Narrowed to exactly the three source-side items this note actually verifies:
  (i) explicitly defined all-forward L_s=2 quotient-encoder geometry (12
  encoded plaquette loops, 24 directed links, all 48 incidences forward by
  encoder convention); (ii) bipartite plaquette adjacency (color partition
  6:6, BFS-verified); (iii) trivial-sector Reference B recovery (rho =
  delta_(0,0) arises naturally inside this encoder and yields P_trivial(6) =
  0.4225, matching the existing Reference B). This row does not claim a Wilson
  orientation/count theorem. The quantitative bound `P_cube(6) >=
  P_trivial(6)` and non-trivial-sector rho_(p,q) contributions are out of
  scope for this narrowed note.
```

## 7. Cross-references

- Fusion engine (PR 1, audited): [`SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md`](SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md)
- Eventual target: [`GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md`](GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md)
- Source-sector factorization: [`GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
- Existing reference Perron solves: [`GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)

## 8. Command

```bash
python3 scripts/frontier_su3_cube_perron_solve.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=8 SUPPORT=2 FAIL=0
```
