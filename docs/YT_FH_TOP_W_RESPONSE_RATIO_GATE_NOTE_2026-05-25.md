---
claim_id: yt_fh_top_w_response_ratio_gate_note_2026-05-25
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Feynman-Hellmann Top/W Response-Ratio Gate

**Claim type:** bounded_theorem / open-gate support.
**Status:** exact conditional route theorem; current Y_T source-action surface does not
yet close positive Y_T.
**Primary runner:** `scripts/frontier_yt_fh_top_w_response_ratio_gate.py`
**Generated output:** `outputs/yt_fh_top_w_response_ratio_gate_2026-05-25.json`

This note tries the full W/Z plus Feynman-Hellmann route identified in the
lambda-normalization fanout.  The result is useful but not yet retained Y_T
closure:

```text
same source h
  -> M_t(h) and M_W(h) transfer-matrix responses
  -> [dM_t/dh] / [dM_W/dh] cancels source normalization
  -> y_t = (g_2 / sqrt(2)) [dM_t/dh] / [dM_W/dh]
```

The route is the right shape.  It avoids the source/Higgs normalization
freedom that defeated pole-row purity alone.  What remains missing is not the
algebra; it is the same-surface physical premise and strict response evidence.

## Current Repo Authority

The route can reuse one strong upstream theorem:

- `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` is audited
  clean and retained.  It proves the one-doublet tree-level identities
  `M_W = g_2 v / 2` and
  `M_Z = sqrt(g_2^2 + g_Y^2) v / 2` without observed W/Z masses.

It cannot treat the following as already closed:

- The existing audited source-action support note is retained bounded support
  only.  It does not make the Y_T source-action gate the physical neutral
  EW/Higgs surface.
- `ew_coupling_derivation_note` is not retained authority for the v-scale
  numerical value of `g_2`.
- No strict Y_T lane file currently supplies same-source top and W
  Feynman-Hellmann response rows.

## Theorem: Same-Source Top/W Response Ratio

Assume an accepted same-source surface with scalar source coordinate `h`.
Assume that, at fixed renormalized couplings and within the same local model
class, the top and W pole masses depend on a common scalar background `v(h)`:

```text
M_t(h) = y_t v(h) / sqrt(2),
M_W(h) = g_2 v(h) / 2.
```

If `dv/dh` exists and is nonzero, then

```text
dM_t/dh = (y_t / sqrt(2)) dv/dh,
dM_W/dh = (g_2 / 2) dv/dh.
```

Therefore

```text
(dM_t/dh) / (dM_W/dh) = sqrt(2) y_t / g_2,
```

and

```text
y_t = (g_2 / sqrt(2)) (dM_t/dh) / (dM_W/dh).
```

The source normalization cancels.  If `h' = c h`, then both derivatives pick
up the same factor `1/c`, and the ratio is unchanged.

## Transfer-Matrix Feynman-Hellmann Form

On a reflection-positive transfer surface, let `Lambda_0(h)` be the vacuum
eigenvalue and `Lambda_X(h)` the isolated sector eigenvalue for a state `X`.
The finite-volume mass is

```text
M_X(h) = -a_t^{-1} log[Lambda_X(h) / Lambda_0(h)].
```

Differentiating gives

```text
dM_X/dh
  = -a_t^{-1} [
      Lambda_X'(h) / Lambda_X(h)
      - Lambda_0'(h) / Lambda_0(h)
    ].
```

If the transfer matrix is represented by a Hamiltonian and the eigenvalue is
isolated, this is the usual Feynman-Hellmann matrix-element difference
between the target sector and the vacuum.  This note only uses the algebraic
derivative form; it does not assert that the Y_T top and W strict response rows
have been measured.

## Why This Beats The Pole-Row Normalization No-Go

The retained pole-row no-go says that `C_ss/C_sH/C_HH` common-pole purity is
invariant under

```text
s -> mu s,
H -> lambda H.
```

The top/W response ratio is different.  It divides two responses to the same
source coordinate before converting to `y_t`.  The source Jacobian cancels:

```text
dM_t/dh' = (1/c) dM_t/dh,
dM_W/dh' = (1/c) dM_W/dh.
```

The remaining denominator is not the arbitrary scalar source unit.  It is the
gauge coupling `g_2`, supplied by the gauge sector.  Thus this route can retire
the scalar-normalization wall if and only if `g_2` authority and same-source
top/W response rows are available.

## Current Attempt Result

This attempt does not close Y_T today.  It collapses the route to the exact
remaining premises:

1. **Same-source physical EW/Higgs action authority.**  The Y_T source-action lane currently gives
   finite signed-record source/action support, not physical neutral EW/Higgs
   authority.
2. **Strict top and W response rows.**  The route needs transfer-matrix
   responses `dM_t/dh` and `dM_W/dh` on the same source surface, with contact
   subtraction, finite-volume/IR control, and model-class checks.
3. **Gauge-coupling authority.**  The retained EW mass theorem supplies the
   W denominator algebra.  A retained same-scale `g_2` value or a lattice-scale
   version of the route is still required for a numerical `y_t`.
4. **Matching/running.**  After a local readout exists, the usual matching and
   running bridge is still separate.

## Non-Claims

This note does not:

- derive a numerical `y_t`;
- derive `m_t`;
- derive `v = 246 GeV`;
- derive or import `kappa_Y = 0`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, `alpha_LM`, plaquette/u0,
  PDG values, or observed W/Z/top masses as proof inputs;
- promote the Y_T source-action lane beyond support/open-gate status.

## Verification

```text
python3 scripts/frontier_yt_fh_top_w_response_ratio_gate.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

The green result means the top/W response-ratio route is algebraically valid
and that the current repo blockers are narrow.  It does not mean positive Y_T
closure has been obtained.
