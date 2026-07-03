# The First d=3 Decimation Datum on the Framework's Cubic Lattice: Step-1 Closed Form (diag − 6t²/μ; Face-Diagonal −2t²/μ; Axial −t²/μ; Nothing Beyond) and the Parity Lemma in Three Dimensions (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d3_checkerboard_step1_parity_lemma_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d3_checkerboard_step1_parity_lemma_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=12 FAIL=0`.

## Findings

On the framework's own `Z³` adjacency (simple cubic, `L ∈ {6,8}`): the odd-parity
sublattice has no internal NN bonds (`h_oo = μI` — the `d = 1, 2` property persists),
giving the exact step-1 closed form `diag′ = μ − 6t²/μ`, face-diagonal (`d² = 2`)
matrix element `−2t²/μ` (two shared odd neighbors), axial (`d² = 4`) element
`−t²/μ` (one) — signed values stated (the earlier magnitudes-only phrasing was
panel-corrected),
and **nothing beyond** (`10⁻¹²`, `L = 6` vs `8` wraparound-gated). The step is
E-covariant (`μ → μ−E`) and resolvent-exact. **The parity lemma holds in `d = 3`**:
`Σdᵢ² ≡ Σdᵢ (mod 2)`, since each `d_i^2 - d_i = d_i(d_i-1)` is even. The runner
also exhaustively checks `|d|∞ ≤ 4`, so even-`d²` kept bands cannot couple the
parity sublattices — operationally gated (`10⁻¹⁴`).

## Scope

Free, one orbital, `E = 0` (+ one `E` probe), on the Lattice axiom's cubic
`Z³` nearest-neighbor adjacency
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)); step-2 range
behavior is the named follow-on. Cross-references to the `d = 2` notes are
in-review context only, not graded authorities for this claim. No new
axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
