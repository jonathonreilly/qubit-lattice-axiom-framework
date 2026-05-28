# Gravity Sign Well/Hill Diagnostic

**Date:** 2026-04-10; narrowed 2026-05-27; lapse-floor narrowed 2026-05-28
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_gravity_sign_well_hill_diagnostic.py`
**Historical runner:** `scripts/frontier_correct_coupling.py`
**Status authority:** independent audit lane only

---

## Status

This row is narrowed to a configured finite 1D diagnostic. It does not claim a
framework derivation of physical gravity sign, a derivation of the staggered
scalar/lapse coupling from the baseline axioms, or any irregular-graph
portability result.

The 2026-05-28 repair further narrows the bounded claim to the **identity
(negative control) and parity** finite-sign reproduction only. The **lapse**
coupling's well/hill split is **open** (see below): it does not close against
the cited lapse form because the configured well drives the lapse
`N = 1 + Phi/m` deeply negative and the result depends on flooring `N`.

The retained-bounded one-hop support available here is
[`STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md),
which certifies the displayed finite operator forms only. It does not prove
that the baseline framework forces those forms.

## Bounded Claim

In the configured 1D external-potential test:

```text
n = 61
mass = 0.30
dt = 0.12
steps = 20
mass point = 38
initial packet center = 30
well: V(x) < 0
hill: V(x) > 0
```

the stipulated **parity** Hamiltonian form, together with the **identity**
negative control, distinguish well from hill:

```text
identity: well -> TOWARD, hill -> TOWARD   (negative control)
parity:   well -> TOWARD, hill -> AWAY
```

The identity and parity couplings are pure on-site Hamiltonian modifications.
Their code path applies **no** regularization: it never takes `sqrt(N)` and
never floors any quantity. The diagnostic is defined by the final centroid
displacement relative to the initial packet center:

```text
disp > 0  => TOWARD the mass point
disp < 0  => AWAY from the mass point
```

The runner verifies that the identity and parity evolutions conserve norm to
numerical tolerance and that the signs above hold.

## Open: Lapse Closure (Does Not Close Against The Cited Lapse Form)

The lapse coupling builds `sqrt(N) H sqrt(N)` with the lapse `N = 1 + Phi/m`.
For the configured well potential the lapse is **non-positive over a band of
sites**: `N` reaches about `-79` near the mass point, with 15 sites at
`N <= 0`. Taking `sqrt(N)` on this profile requires regularizing `N`.

A previous version of the runner silently floored `N` to `0.01` before taking
`sqrt(N)`. That floor was **unstated and load-bearing**: the lapse well/hill
split depended on it. This is the defect identified by the audit, whose verdict
was that the parity/identity finite signs reproduce but **the lapse part does
not close against the cited lapse form**.

The 2026-05-28 repair makes the regularization **explicit** and removes it from
the bounded claim:

- The runner now floors the lapse with an **explicit, stated** constant
  `N -> max(N, 0.01)` and **prints the floor and the count of non-positive
  `N` sites** for each case. No floor is applied silently anywhere.
- The lapse case is reported as an explicitly labelled diagnostic only and is
  **not counted** in the bounded PASS/FAIL accounting.
- The well/hill directional signal exists only in the strong-field regime where
  the lapse is non-positive and floored. In the genuine weak-field regime
  (`N > 0` everywhere, no floor needed) the well/hill split collapses: every
  coupling reads `TOWARD` for both well and hill. A weak-field domain
  restriction therefore cannot honestly preserve the lapse split; the split is
  a strong-field, floor-dependent artifact.

Consequently the **lapse-closure part is open**. It is not part of the bounded
claim and carries no bounded verdict. Closing it would require a lapse form (or
a domain) under which `N = 1 + Phi/m > 0` throughout while still producing the
claimed well/hill direction — which the present configured potential does not
supply.

## What This Note Does Not Claim

- No derivation of the parity or lapse coupling from A1/A2/minimal axioms.
- No claim that either coupling is physically selected by the framework.
- No claim that the lapse well/hill split closes (it is open; see above).
- No graph self-gravity result.
- No irregular-graph directional observable closure.
- No statement about Part 1 force-sign language from the historical runner.
- No retained verdict and no direct ledger retag.

## Relation To The Historical Runner

`scripts/frontier_correct_coupling.py` remains a historical broad diagnostic.
It prints graph/self-gravity sections and older direction labels that are not
part of this repaired row. The audit blocker specifically asked to narrow the
source to the Part 4 well/hill diagnostic and remove the stale broader graph
and lapse-direction claims. This note and its new runner do that.

## Verification

Run:

```bash
python3 scripts/frontier_gravity_sign_well_hill_diagnostic.py
```

Expected result (bounded claim = identity + parity; lapse is an open,
explicitly floored diagnostic printed separately and not counted):

```text
Gravity sign well/hill diagnostic: PASS
PASS=17 FAIL=0
```

The lapse section prints the explicit floor `N -> max(N, 0.01)` and, for the
well case, `FLOOR ACTIVE: 15 sites with N<=0, min N=-79.0000`, making the
load-bearing regularization visible rather than silent.

## Audit Request

Please re-audit only the bounded configured diagnostic above (identity negative
control plus parity well/hill split). The intended safe scope is this finite
well/hill separation if the auditor agrees the runner closes the stated signs
without any regularization. The lapse-closure part is **open** and is excluded
from the bounded claim. Broader gravity-sign physics remains out of scope. Any
effective status is assigned only by the independent audit lane.
