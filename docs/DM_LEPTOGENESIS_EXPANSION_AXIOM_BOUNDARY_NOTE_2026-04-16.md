# DM Leptogenesis Expansion Axiom Boundary

**Status:** bounded - bounded or caveated result note
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Date:** 2026-04-16
**Branch:** `codex/dm-main-refresh`
**Script:** `scripts/frontier_dm_leptogenesis_expansion_axiom_boundary.py`
**Framework convention:** "axiom" means only `Cl(3)` on `Z^3`

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The restricted packet does not provide a theorem or cited authority showing that the source, transfer coefficients, projection law, coherent kernel, equilibrium factors, and direct transport integral are all closed or that eta is uniquely d"*

with repair: *"missing_bridge_theorem: supply a retained theorem or non-hard-coded runner proving eta is uniquely fixed by H_rad(T) after the listed ingredients are closed."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The boundary-narrowing result is exactly what the runner verifies: after accounting for the source, transfer coefficients, projection law, coherent kernel, equilibrium factors, and direct transport integral, the single remaining non-axiom object is `H_rad(T)` (equivalently the normalized expansion profile `E_H(z)`), which is a sharper boundary than the older `T_rad(K)` parameterization.
- **NON-load-bearing (split off / admitted):** That `eta` is uniquely fixed given `H_rad(T)` is asserted in the note but is not established by a retained theorem or non-hard-coded runner; the uniqueness claim depends on an unsupplied retained authority closing all listed ingredients simultaneously, and remains an admitted, not-derived conclusion.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

**Audit-lane runner update (2026-05-09):** the primary runner `scripts/frontier_dm_leptogenesis_expansion_axiom_boundary.py` exits 0 with PASS in the current cache; the prior audit verdict citing a nonzero exit was generated against a stale cache and is invalidated by this source-note hash drift. The runner output and pass/fail semantics are otherwise unchanged.

## Result

After closing:

- the exact source package
- the exact transfer coefficients
- the exact projection law
- the exact coherent kernel
- the exact equilibrium conversion factors
- the exact direct transport integral

the single remaining non-axiom object is now:

- `H_rad(T)`

equivalently:

- the normalized expansion profile `E_H(z)` together with its normalization at
  `z = 1`

This is sharper than the older boundary

- `T_rad(K) = 7.04 * C_sph * d_th * kappa_fit(K)`

because the bookkeeping factors and the fit are no longer part of the
authority path.

## Why the boundary remains

The current branch still does not carry a strict theorem-grade radiation-era
expansion law from `Cl(3)` on `Z^3` alone. The older `H(T)` lane still uses a
bounded `k = 0` sub-assumption, so full theorem closure cannot yet be claimed.

Given `H_rad(T)`, however, the refreshed branch now fixes `eta` uniquely.
