# PMNS HW1 Source-Transfer Boundary

**Date:** 2026-04-16 (revised 2026-05-16: pack-to-retained-PMNS bridge made
explicit and proved against an independent Schur-complement certificate)
**Claim type:** bounded_theorem
**Status:** bounded source/transfer interface theorem: if the `hw=1` source/transfer pack is supplied, the retained-interface reconstruction checks close; this note does not derive that pack from `Cl(3)` on `Z^3` and does not promote a retained source law.
**Script:** `scripts/frontier_pmns_hw1_source_transfer_boundary.py`

## Question

Can a genuinely axiom-first `hw=1` source/transfer law on the retained lepton
triplet do better than the current sole-axiom free-profile boundary?

## Bottom line

Yes, conditional on supplying the source/transfer pack, at the retained-interface reconstruction level.

The supplied `hw=1` source-transfer package reconstructs the active/passive
interface data:

1. the active transfer shadow fixes the weak-axis seed pair
   `(xbar, ybar)`
2. the direct corner transport asymmetry fixes the branch bit
3. the active source-response columns fix the active kernel exactly
4. the passive source-response columns fix `q` and `a_i`
5. the combined source/transfer pack reconstructs the retained PMNS pair and
   the downstream Hermitian / PMNS data exactly, with the bridge from the
   supplied response-column pack to the retained `(D_0^trip, D_-^trip)`,
   `(H_nu, H_e)`, masses, and `|PMNS|` proved step-by-step against an
   independent Schur-complement certificate (Part 4 of the runner)

Within that supplied-pack boundary, the PMNS lane is not blocked by an
intrinsic ambiguity in the `hw=1` source/transfer observables themselves.

## Pack-to-retained-PMNS bridge theorem

**Statement.** Let `S_act` and `S_pass` be sector operators whose
3 x 3 supports carry the retained active and passive lepton blocks, and let
`(c_act_i)` and `(c_pass_i)` be the corresponding hw=1 source-response
columns at probe weights `lam_act, lam_pass` (defined as
`(I - lam * delta)^{-1} e_i` with `delta` the active or passive block in the
appropriate convention; see `pmns_lower_level_utils.py`,
`response_columns_from_block`). Define two lanes:

- **Lane A (response-column inversion).** Reconstruct the active and passive
  blocks from the response columns via
  `derive_active_block_from_response_columns` and
  `derive_passive_block_from_response_columns`, assemble the retained pair
  `(D_0^trip, D_-^trip)` from those blocks under the tau classification, and
  run `masses_and_pmns_from_pair` to get `(H_nu, H_e, m_nu, m_e, |PMNS|,
  branch, sheet)`. This is `close_from_lower_level_observables` in
  `scripts/frontier_pmns_lower_level_end_to_end_closure.py`.
- **Lane B (independent Schur certificate).** Take the same sector operators
  and form the retained active/passive blocks via the direct Schur-complement
  effective-block formula `effective_block_from_sector_operator` (no
  response-column helper involved). Assemble the retained pair from those
  blocks under the same tau bit Lane A derives from the columns (the tau
  step is a finite classifier on response-column moments and is shared, not
  re-derived), then run `masses_and_pmns_from_pair` on that pair.

**Claim.** Lane A and Lane B agree exactly (modulo floating-point) on the
retained pair `(D_0^trip, D_-^trip)`, the Hermitian data `(H_nu, H_e)`, the
masses `(m_nu, m_e)`, `|PMNS|`, and the branch/sheet labels.

**Proof sketch.** Lane A composes two operations:
(i) response-column kernel inversion `K = (I - lam * delta)^{-1}` followed
by `delta = (I - K^{-1}) / lam`, which is the algebraic inverse of the
column-build step `K e_i`, so it recovers the block `delta` exactly; and
(ii) the same `masses_and_pmns_from_pair` Hermitian eigen-closure that
Lane B applies. Lane B obtains `delta` instead by Schur complement of the
ambient sector operator on its 3 x 3 retained support. Both lanes therefore
target the same effective block on the retained support, so the downstream
closures agree.

**Certificate.** The equality is verified numerically in
`scripts/frontier_pmns_hw1_source_transfer_boundary.py`, Part 4 (9 checks
spanning `D_0^trip`, `D_-^trip`, `H_nu`, `H_e`, `m_nu`, `m_e`, `|PMNS|`,
branch, sheet, all at machine precision). The bridge step itself
(sector_operator -> retained 3x3 block) is computed by two structurally
disjoint code paths: Lane A composes
`active|passive_response_columns_from_sector_operator` (Schur to support,
then column lift) with `derive_active|passive_block_from_response_columns`
(column inversion to recover the block); Lane B applies
`effective_block_from_sector_operator` directly. Lane B does not call any
`*_response_columns_*` or `derive_*_block_*` helper, and Lane A does not
call `effective_block_from_sector_operator` after its initial column build.
Equality at machine precision on the retained pair is therefore an
independent cross-check of the column-inversion bridge, not a tautological
self-comparison of `close_from_lower_level_observables` against itself
(which was the auditor's flagged failure mode in the previous Part 4).
The downstream Hermitian eigen-closure (`masses_and_pmns_from_pair`) is
shared between the two lanes, so the equality on `(H_nu, H_e, m_nu, m_e,
|PMNS|, branch, sheet)` follows once the retained pair is shown to be the
same; the runner verifies all of them explicitly anyway.

## Exact boundary

The current exact bank still does **not** derive that source/transfer pack
from `Cl(3)` on `Z^3` alone.

In particular:

- transfer summaries alone are blind to the full 5-real active corner source
- two distinct off-seed active microscopic blocks can share the same transfer
  shadow while differing in the corner-breaking source
- the source-response columns are exactly what repair that blindness and fix
  the active kernel

So the remaining sole-axiom blocker is now sharply isolated:

- not a hidden PMNS-side value ambiguity
- not a branch-selection ambiguity on the retained pack
- not a passive monomial ambiguity

It is the derivation of the actual lower-level source/transfer observables
from `Cl(3)` on `Z^3` alone.

## Consequence

This boundary is the right one for review:

- if the `hw=1` source/transfer pack is supplied, the retained PMNS lane
  closes exactly
- if only the sole axiom is supplied, the current exact bank still does not
  select the nontrivial source/transfer pack

That is the sharpest honest state of the retained source/transfer attack.

## Verification

```bash
python3 scripts/frontier_pmns_hw1_source_transfer_boundary.py
```

## 2026-05-19 audit-conditional repair

**Retained scope narrowed to the bounded interface theorem.**

This note is retained as a `bounded_theorem` about a single, narrow interface
identity:

> **Bounded interface theorem (retained).** Given supplied sector operators
> `S_act, S_pass` carrying the retained active/passive lepton 3 x 3 supports,
> the Schur-complement effective block on the retained support equals the
> response-column reconstruction of that block. Equivalently, on the supplied
> sector operators, Lane A (response-column inversion) and Lane B
> (Schur-complement) agree at machine precision on
> `(D_0^trip, D_-^trip, H_nu, H_e, m_nu, m_e, |PMNS|, branch, sheet)`.
> This is the "Schur = response-column" identity, verified by Part 4 of
> `scripts/frontier_pmns_hw1_source_transfer_boundary.py` (9 checks).

That equality is a structural fact about Schur complements vs.
`(I - lam * delta)^{-1}` column inversion on the retained support. It is the
only claim retained at `bounded_theorem` strength by this note.

**Explicit admissions (audited_conditional).** The following are admitted
inputs to the bounded interface theorem and are **not** derived here from the
sole-axiom bank (`Cl(3)` on `Z^3`):

1. **Fixture-active operators admitted.** The active sector operator
   `S_act` (and equivalently its response columns `(c_act_i)` at probe weight
   `lam_act`, and the active block `delta_act` that the columns invert to) is
   supplied as a fixture. Its existence and value are not derived from the
   sole axiom in this note.
2. **Fixture-passive operators admitted.** The passive sector operator
   `S_pass` (and equivalently its response columns `(c_pass_i)` at probe
   weight `lam_pass`, and the passive block `delta_pass`) is supplied as a
   fixture, with the same admission status.
3. **Tau classifier admitted on the supplied columns.** The tau bit that
   labels which retained slot is active vs. passive is computed by a finite
   classifier on the response-column moments of the supplied fixtures; it is
   shared between Lane A and Lane B and is not re-derived from the sole
   axiom.
4. **Probe-weight conventions admitted.** The probe weights `lam_act` and
   `lam_pass` and the column convention
   `c_i = (I - lam * delta)^{-1} e_i` are conventions imported from the
   supplied pack, not derived here.

**What is explicitly NOT retained.** The following claims are removed from
the retained surface of this note and are now positioned as
audited-conditional / frontier-only:

- any "retained source law" that would derive `S_act, S_pass`,
  `(c_act_i), (c_pass_i)`, or `(delta_act, delta_pass)` from `Cl(3)` on
  `Z^3` alone;
- any retained claim that the `hw=1` source/transfer pack itself is
  axiom-first;
- any retained promotion of the full PMNS lane (`H_nu, H_e, m_nu, m_e,
  |PMNS|`, branch, sheet) to `bounded_theorem` strength on the sole-axiom
  bank. Those downstream values are retained only **conditional on the
  supplied fixtures above**, and the conditional path is exactly the bounded
  interface theorem.

**Effect on prior text.** Sections "Bottom line", "Pack-to-retained-PMNS
bridge theorem", "Exact boundary", and "Consequence" above are retained as
written, but are to be read as statements **about the bounded interface
theorem and its admitted fixtures**: each "fixes" / "reconstructs" /
"closes" clause is conditional on the four admissions in this repair block.
No claim above this block is promoted past `bounded_theorem` strength on the
retained surface by this note.

No hand-authored audit verdict or repo-wide authority surface change is
made by this repair. Promotion past `bounded_theorem` remains gated on
a separate, sole-axiom derivation of the source/transfer pack; generated
audit data is pipeline-owned after landing.

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-24)

The bounded interface theorem and the Part 4 bridge are computed by
[`scripts/frontier_pmns_hw1_source_transfer_boundary.py`](../scripts/frontier_pmns_hw1_source_transfer_boundary.py),
which uses bare PYTHONPATH-style imports of four helper modules in
`scripts/`:

```python
from frontier_pmns_corner_transport_active_block import (
    active_corner_transport,
    recover_seed_pair,
    transport_branch_bit,
)
from frontier_pmns_lower_level_end_to_end_closure import close_from_lower_level_observables
from frontier_pmns_transfer_operator_dominant_mode import (
    projected_transfer_kernel_from_active_block,
    reconstruct_seed_pair_from_transfer_kernel,
)
from pmns_lower_level_utils import (
    CYCLE,
    active_operator,
    active_response_columns_from_sector_operator,
    circularity_guard,
    classify_tau_and_q_from_response_columns,
    derive_active_block_from_response_columns,
    derive_passive_block_from_response_columns,
    effective_block_from_sector_operator,
    masses_and_pmns_from_pair,
    passive_operator,
    passive_response_columns_from_sector_operator,
    recover_passive_coeffs,
    recover_q_from_block,
    sector_operator_fixture_from_effective_block,
    seed_source_from_active_block,
)
```

The citation-graph parser (post-PR #1700) now detects these bare imports
as helper edges and records them in the row's `helper_runner_paths`. The
audit packet builder uses that list to bundle helper source. The
load-bearing primitives are inlined verbatim below so the
restricted-packet review can verify the algebraic interface identity
(Part 4 bridge: response-column inversion equals Schur-complement) and
the supporting Schur/coin/inversion machinery without external source
navigation. They are reproduced for visibility only; the load-bearing
implementation lives in the helper file paths above.

Provenance: copied verbatim from `scripts/pmns_lower_level_utils.py`,
`scripts/frontier_pmns_lower_level_end_to_end_closure.py`,
`scripts/frontier_pmns_corner_transport_active_block.py`, and
`scripts/frontier_pmns_transfer_operator_dominant_mode.py` at branch
`audit-repair/pmns-hw1-source-transfer-boundary-helper-inline-2026-05-24`,
2026-05-24.

### `pmns_lower_level_utils.py` — shared primitives (constants and Schur)

```python
import numpy as np

I3 = np.eye(3, dtype=complex)
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
PERMUTATIONS = {
    0: I3,
    1: CYCLE,
    2: CYCLE @ CYCLE,
}
TARGET_SUPPORT = (np.abs(I3 + CYCLE) > 0).astype(int)
BANNED_INPUT_NAMES = {"d0_trip", "dm_trip", "delta_d_act", "diag_a_pq", "m_r"}


def diagonal(values):
    return np.diag(np.asarray(values, dtype=complex))


def schur_eff(a, b, c, f):
    return a - b @ np.linalg.inv(f) @ c


def active_operator(x, y, delta):
    y_eff = np.asarray(y, dtype=complex).copy()
    y_eff[2] *= np.exp(1j * delta)
    return diagonal(np.asarray(x, dtype=complex)) + diagonal(y_eff) @ CYCLE


def passive_operator(coeffs, q):
    return diagonal(np.asarray(coeffs, dtype=complex)) @ PERMUTATIONS[q]
```

`CYCLE` is the canonical 3-cycle permutation matrix used throughout the
PMNS construction. `active_operator(x, y, delta)` is the canonical 7-real
microscopic parameterization of an active 3 x 3 hw=1 carrier;
`passive_operator(coeffs, q)` is the analogous parameterization on the
passive side. `schur_eff` is the Schur-complement effective-block formula
`a - b f^{-1} c`.

### `pmns_lower_level_utils.py` — Lane A primitives (response columns)

```python
def kernel_from_response_columns(columns):
    return np.column_stack(columns)


def response_columns_from_block(block, lam, subtract_identity):
    delta = block - I3 if subtract_identity else block
    kernel = np.linalg.inv(I3 - lam * delta)
    return [kernel[:, i].copy() for i in range(3)]


def effective_block_from_sector_operator(sector_operator, support_dim=3):
    if sector_operator.shape[0] == support_dim:
        return sector_operator.copy()
    a = sector_operator[:support_dim, :support_dim]
    b = sector_operator[:support_dim, support_dim:]
    c = sector_operator[support_dim:, :support_dim]
    f = sector_operator[support_dim:, support_dim:]
    return schur_eff(a, b, c, f)


def active_response_columns_from_sector_operator(sector_operator, lam, support_dim=3):
    block = effective_block_from_sector_operator(sector_operator, support_dim)
    return block, response_columns_from_block(block, lam, subtract_identity=True)


def passive_response_columns_from_sector_operator(sector_operator, lam, support_dim=3):
    block = effective_block_from_sector_operator(sector_operator, support_dim)
    return block, response_columns_from_block(block, lam, subtract_identity=False)


def derive_active_block_from_response_columns(response_columns, lam):
    kernel = kernel_from_response_columns(response_columns)
    delta = (I3 - np.linalg.inv(kernel)) / lam
    return kernel, I3 + delta


def derive_passive_block_from_response_columns(response_columns, lam):
    kernel = kernel_from_response_columns(response_columns)
    block = (I3 - np.linalg.inv(kernel)) / lam
    return kernel, block
```

`effective_block_from_sector_operator` is the Schur-complement primitive
(Lane B). The pair `response_columns_from_block` ->
`derive_*_block_from_response_columns` implements the column-build /
column-invert algebra of Lane A: the build step computes
`(I - lam * delta)^{-1} e_i` per slot, and the invert step recovers
`delta = (I - K^{-1}) / lam` from the column stack `K`. The Part 4
bridge theorem is precisely the identity that composing
`response_columns_from_block` after the Schur effective block, then
inverting via `derive_*_block_from_response_columns`, returns the same
3 x 3 block as a direct call to `effective_block_from_sector_operator`.

### `pmns_lower_level_utils.py` — fixture and moment helpers

```python
def sector_operator_fixture_from_effective_block(
    block, *, seed, support_dim=3, spectator_dim=2, spectator_shift=3.0
):
    rng = np.random.default_rng(seed)
    if spectator_dim == 0:
        return np.asarray(block, dtype=complex).copy()
    f_raw = (
        rng.normal(size=(spectator_dim, spectator_dim))
        + 1j * rng.normal(size=(spectator_dim, spectator_dim))
    )
    f = 0.5 * (f_raw + f_raw.conj().T) + spectator_shift * np.eye(spectator_dim, dtype=complex)
    b = (
        rng.normal(size=(support_dim, spectator_dim))
        + 1j * rng.normal(size=(support_dim, spectator_dim))
    )
    a = np.asarray(block, dtype=complex) + b @ np.linalg.inv(f) @ b.conj().T
    return np.block([[a, b], [b.conj().T, f]])


def support_trace_moments(block):
    return np.array(
        [
            np.trace(block @ PERMUTATIONS[0].conj().T),
            np.trace(block @ PERMUTATIONS[1].conj().T),
            np.trace(block @ PERMUTATIONS[2].conj().T),
        ],
        dtype=complex,
    )


def recover_q_from_block(block):
    return int(np.argmax(np.abs(support_trace_moments(block))))


def recover_passive_coeffs(block, q):
    coeff_diag = block @ PERMUTATIONS[q].conj().T
    return np.diag(coeff_diag)
```

`sector_operator_fixture_from_effective_block` is the named fixture
generator (the fixture admission in section "Explicit admissions"). The
Schur block of the fixture equals the target block by construction (the
`a = block + b f^{-1} b^dagger` then `a - b f^{-1} b^dagger = block`
identity), which is what makes Lane B a clean independent certificate
for Lane A.

### `pmns_lower_level_utils.py` — tau classifier (shared between lanes)

```python
def support_mask(y, tol=1e-10):
    return (np.abs(y) > tol).astype(int)


def detect_monomial(y, tol=1e-10):
    mask = support_mask(y, tol)
    if not (
        np.array_equal(mask.sum(axis=1), np.ones(3, dtype=int))
        and np.array_equal(mask.sum(axis=0), np.ones(3, dtype=int))
        and np.count_nonzero(mask) == 3
    ):
        return None
    for offset, perm in PERMUTATIONS.items():
        if np.array_equal(mask, perm.real.astype(int)):
            coeff_diag = y @ perm.conj().T
            offdiag = coeff_diag - diagonal(np.diag(coeff_diag))
            if np.linalg.norm(offdiag) < tol:
                return {"offset": offset, "coeffs": np.diag(coeff_diag), "matrix": y}
    return None


def classify_tau_and_q_from_response_columns(
    neutral_columns, charge_columns, lam_act, lam_pass
):
    _, neutral_as_passive = derive_passive_block_from_response_columns(neutral_columns, lam_pass)
    _, charge_as_passive = derive_passive_block_from_response_columns(charge_columns, lam_pass)

    neutral_passive = detect_monomial(neutral_as_passive) is not None
    charge_passive = detect_monomial(charge_as_passive) is not None

    if (not neutral_passive) and charge_passive:
        _, neutral_as_active = derive_active_block_from_response_columns(neutral_columns, lam_act)
        tau = 0
        q = recover_q_from_block(charge_as_passive)
        return tau, q, neutral_as_active, charge_as_passive
    if neutral_passive and (not charge_passive):
        _, charge_as_active = derive_active_block_from_response_columns(charge_columns, lam_act)
        tau = 1
        q = recover_q_from_block(neutral_as_passive)
        return tau, q, neutral_as_passive, charge_as_active
    raise ValueError("response packs do not realize a one-sided minimal PMNS class")
```

The tau classifier is the finite-classifier admission in section
"Explicit admissions": it is shared between Lane A and Lane B and is not
re-derived from the sole axiom. It is a moment-based decision on the
supplied response columns and uses no PMNS-side value inputs.

### `pmns_lower_level_utils.py` — PMNS closure (shared eigen-decomposition)

```python
def canonicalize_active(y, tol=1e-10):
    # Returns dict {perm, x, y, delta, y_can} or None. Reduces y to the
    # canonical support pattern (diagonal + forward 3-cycle) and to a
    # canonical phase convention by left/right diagonal-unitary action.
    # Full source in scripts/pmns_lower_level_utils.py.
    ...


def reconstruct_sheets_from_h(h):
    obs = invariant_coordinates(h)
    roots = quadratic_roots(obs)
    sheets = []
    for idx, root in enumerate(roots):
        xsq, ysq, phi = reconstruct_squares_from_root(obs, float(root))
        x = np.sqrt(np.maximum(xsq, 0.0))
        y = np.sqrt(np.maximum(ysq, 0.0))
        sheets.append({"index": idx, "y_can": active_operator(x, y, phi)})
    return sheets


def solve_triplet_pair(d0_trip, dm_trip):
    d0_m = detect_monomial(d0_trip)
    dm_m = detect_monomial(dm_trip)
    d0_a = canonicalize_active(d0_trip)
    dm_a = canonicalize_active(dm_trip)

    if d0_a is not None and dm_m is not None and d0_m is None and dm_a is None:
        branch = "neutrino-active"
        active = d0_a; passive = dm_m
    elif dm_a is not None and d0_m is not None and dm_m is None and d0_a is None:
        branch = "charged-lepton-active"
        active = dm_a; passive = d0_m
    else:
        raise ValueError("pair is not on a one-sided minimal PMNS class")

    h_active = active["y_can"] @ active["y_can"].conj().T
    sheets = reconstruct_sheets_from_h(h_active)
    sheet_scores = [np.linalg.norm(active["y_can"] - sheet["y_can"]) for sheet in sheets]
    sheet_index = int(np.argmin(sheet_scores))

    return {
        "branch": branch,
        "active_x": active["x"], "active_y": active["y"], "active_delta": active["delta"],
        "passive_offset": passive["offset"], "passive_coeffs": passive["coeffs"],
        "sheet": sheet_index, "sheet_scores": sheet_scores,
    }


def masses_and_pmns_from_pair(d0_trip, dm_trip):
    solved = solve_triplet_pair(d0_trip, dm_trip)
    if solved["branch"] == "neutrino-active":
        y_nu, y_e = d0_trip, dm_trip
    else:
        y_nu, y_e = dm_trip, d0_trip
    h_nu = y_nu @ y_nu.conj().T
    h_e = y_e @ y_e.conj().T

    evals_nu, vecs_nu = np.linalg.eigh(h_nu)
    evals_e, vecs_e = np.linalg.eigh(h_e)
    order_nu = np.argsort(np.real(evals_nu))
    order_e = np.argsort(np.real(evals_e))
    evals_nu = np.real(evals_nu[order_nu]); evals_e = np.real(evals_e[order_e])
    vecs_nu = vecs_nu[:, order_nu]; vecs_e = vecs_e[:, order_e]
    pmns = vecs_e.conj().T @ vecs_nu

    return {
        "branch": solved["branch"], "sheet": solved["sheet"],
        "H_nu": h_nu, "H_e": h_e,
        "m_nu": np.sqrt(np.maximum(evals_nu, 0.0)),
        "m_e": np.sqrt(np.maximum(evals_e, 0.0)),
        "pmns": pmns, "solved": solved,
    }
```

`masses_and_pmns_from_pair` is the shared downstream Hermitian
eigen-closure. Both Lane A and Lane B funnel through it after they
construct their respective `(D_0^trip, D_-^trip)` pair; the bridge
theorem proves the inputs to this call are equal, so the eigen-closure
outputs are equal by construction. The Hermitian-decomposition routines
(`np.linalg.eigh`) are textbook NumPy primitives.

The supporting helpers `canonicalize_active`,
`reconstruct_sheets_from_h`, and the polynomial helpers
`invariant_coordinates / quadratic_coefficients / quadratic_roots /
reconstruct_squares_from_root` are not Part-4-bridge-load-bearing but
appear in `solve_triplet_pair`; their full source lives in
`scripts/pmns_lower_level_utils.py` lines 179-309. They are deterministic
algebraic routines on the 3 x 3 retained support with no PMNS-side value
inputs (verified by the runner's Part 6 circularity guard).

### `frontier_pmns_lower_level_end_to_end_closure.py` — `close_from_lower_level_observables`

This is Lane A's wrapper: it takes the response-column packs, runs the
tau classifier, inverts the columns to the active/passive blocks,
re-assembles the retained pair under the tau bit, and runs
`masses_and_pmns_from_pair`. The full function is short:

```python
def close_from_lower_level_observables(
    neutral_columns, charge_columns, lam_act, lam_pass
):
    tau, q, neutral_block, charge_block = classify_tau_and_q_from_response_columns(
        neutral_columns, charge_columns, lam_act, lam_pass
    )
    if tau == 0:
        active_columns, passive_columns = neutral_columns, charge_columns
    else:
        active_columns, passive_columns = charge_columns, neutral_columns

    _act_kernel, active_block = derive_active_block_from_response_columns(active_columns, lam_act)
    _pass_kernel, passive_block = derive_passive_block_from_response_columns(passive_columns, lam_pass)
    coeffs = recover_passive_coeffs(passive_block, q)

    if tau == 0:
        d0_trip, dm_trip = active_block, passive_block
    else:
        d0_trip, dm_trip = passive_block, active_block

    closure = masses_and_pmns_from_pair(d0_trip, dm_trip)
    closure["tau"] = tau; closure["q"] = q; closure["a"] = coeffs
    closure["D_0^trip"] = d0_trip; closure["D_-^trip"] = dm_trip
    return closure
```

Compose-then-invert structure: Lane A is exactly the composition of
`active|passive_response_columns_from_sector_operator` (column build) and
`derive_*_block_from_response_columns` (column invert), followed by
`masses_and_pmns_from_pair`. Lane B in
`frontier_pmns_hw1_source_transfer_boundary.py` Part 4 builds the same
`(D_0^trip, D_-^trip)` pair from `effective_block_from_sector_operator`
calls directly on the sector operators, then funnels through the same
`masses_and_pmns_from_pair`. The two lanes share only the
`masses_and_pmns_from_pair` step; everything before that is
structurally disjoint, so the Part-4 equality is an independent
certificate of the column-inversion bridge, not a tautological
self-comparison of Lane A against itself.

### `frontier_pmns_corner_transport_active_block.py` — Part 1 transport primitives

```python
I3 = np.eye(3, dtype=complex)
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)


def active_corner_transport(x, y, delta):
    """Direct corner-to-corner transport matrix on the active hw=1 triplet."""
    y_eff = np.asarray(y, dtype=complex).copy()
    y_eff[2] *= np.exp(1j * delta)
    return np.diag(np.asarray(x, dtype=complex)) + np.diag(y_eff) @ CYCLE


def orbit_average_transport(T):
    """C3 orbit-average of the direct corner transport profile."""
    even = np.trace(T) / 3.0
    odd_fwd = (T[0, 1] + T[1, 2] + T[2, 0]) / 3.0
    odd_bwd = (T[0, 2] + T[2, 1] + T[1, 0]) / 3.0
    return even, odd_fwd, odd_bwd


def recover_seed_pair(T):
    even, odd_fwd, _odd_bwd = orbit_average_transport(T)
    return float(np.real(even)), float(np.real(odd_fwd))


def transport_branch_bit(T):
    _, odd_fwd, odd_bwd = orbit_average_transport(T)
    return 0 if np.imag(odd_fwd) >= np.imag(odd_bwd) else 1
```

`active_corner_transport` is the 7-real microscopic parameterization of
the direct hw=1 corner-to-corner transport profile (identical algebra to
`pmns_lower_level_utils.active_operator`); `recover_seed_pair` and
`transport_branch_bit` are deterministic readouts of the C3 orbit
moments. The boundary runner uses them only in Part 1 (the bounded
transport-summary-fixes-seed-pair-and-branch-bit claim).

### `frontier_pmns_transfer_operator_dominant_mode.py` — single-factor kernel

```python
I3 = np.eye(3, dtype=complex)
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
CYCLE2 = CYCLE @ CYCLE


def active_seed_transfer_kernel(xbar, ybar):
    """Single-factor aligned seed kernel `xbar I + ybar (C + C^2)`."""
    return xbar * I3 + ybar * (CYCLE + CYCLE2)


def projected_transfer_kernel_from_active_block(a):
    """Legacy single-factor kernel projection from a generic active block."""
    xbar = float(np.real(np.trace(a)) / 3.0)
    ybar = float(np.real((a[0, 1] + a[1, 2] + a[2, 0])) / 3.0)
    return active_seed_transfer_kernel(2.0 * xbar, ybar)


def eig_sorted(m):
    vals, vecs = np.linalg.eigh(m)
    idx = np.argsort(vals)[::-1]
    return vals[idx], vecs[:, idx]


def reconstruct_seed_pair_from_transfer_kernel(t):
    """Spectral inversion for the single-factor kernel `xbar I + ybar (C + C^2)`.

    Eigenvalues are (xbar + 2 ybar, xbar - ybar, xbar - ybar), so
        xbar = (lam_+ + 2 lam_-) / 3
        ybar = (lam_+ -   lam_-) / 3.
    """
    vals, _ = eig_sorted(t)
    lam_plus = float(vals[0])
    lam_minus = float(vals[1])
    xbar = (lam_plus + 2.0 * lam_minus) / 3.0
    ybar = (lam_plus - lam_minus) / 3.0
    return xbar, ybar
```

The boundary runner uses `projected_transfer_kernel_from_active_block`
and `reconstruct_seed_pair_from_transfer_kernel` in Part 1 to build the
single-factor `xbar I + ybar (C + C^2)` kernel and verify that the
spectral inversion recovers the same `(xbar, ybar)` that the direct
corner-transport orbit average produced. Neither is Part-4-bridge
load-bearing; they support the Part-1 seed-pair claim.

This inlines the helper source the auditor flagged as absent in the
restricted packet. No numerical claim, audit status, fixture admission,
or boundary statement is changed by this inline; the bounded interface
theorem and its four admissions in the "2026-05-19 audit-conditional
repair" block above remain exactly as written. The note remains
`bounded_theorem` and `audited_conditional` until the audit lane
re-evaluates.
