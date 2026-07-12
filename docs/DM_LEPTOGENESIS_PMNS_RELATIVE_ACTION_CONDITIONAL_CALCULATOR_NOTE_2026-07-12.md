# DM Leptogenesis PMNS Relative-Action Conditional Calculator

**Date:** 2026-07-12
**Status:** bounded conditional calculation; independent audit owns effective
status.
**Claim type:** bounded_theorem
**Primary runner:**
[`scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`](../scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py)

## Scope

This note preserves the operational calculation formerly bundled with the
physical-selector claim in
[`DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md).
That parent now proves the exact negative boundary: Legendre duality does not
derive physical minimum-action selection.

The narrow conditional statement here is:

> Given the fixed seed parameterization, imported transport/projector stack,
> observed closure comparator, and the supplied law “minimize `S_rel` on the
> favored-column closure surface,” the deterministic calculator returns the
> reported off-seed local solution.

This is useful executable support. It is not a framework derivation of the
seed, transport normalization, closure condition, selector law, or observed
baryon ratio.

## Supplied and imported inputs

| Input | Class | Role |
|---|---|---|
| `XBAR_NE`, `YBAR_NE`, fixed active parameterization | supplied static parameterization | defines the source family |
| Projector interface and active-projector reduction | conditional helper machinery | maps the source to `H_e` and the packet |
| Flavor-column transport functional | conditional helper machinery | evaluates the three column outputs |
| `ETA_OBS = 6.12e-10` | observational comparator | defines the closure level |
| `PLAQ_MC = 0.5934` | measured lattice input | enters the imported exact-package calculation |
| `G_WEAK = 0.653` | fitted phenomenology | enters the imported weak/transport normalization |
| Sphaleron, thermal, and entropy factors | standard conditional factors | transport normalization |
| Scale-reference primitive | approved units primitive | units conversion only |
| `W(K)=log det(I+K)` and `S_rel` | supplied static algebra | objective construction |
| constrained minimum-`S_rel` law | explicit non-derived condition | selects the reported local source |

The helper authorities are
[`DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md),
[`DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md),
and
[`DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md).
Their current audit status is not promoted by this note.
The units-only primitive is documented in
[`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md).

## Conditional output

The runner returns

- `x_rel = (0.471675, 0.553811, 0.664514)`;
- `y_rel = (0.208063, 0.464383, 0.247554)`;
- `delta_rel approximately -1.23e-6`;
- `S_rel = 0.240906701369`; and
- `eta/eta_obs = (1.0, 0.75917896, 0.48458840)`.

The same runner verifies that the unconstrained relative-action minimum is the
seed, where column-0 closure is missed. The off-seed result therefore tracks
the supplied observed-closure condition.

## Downstream citation rule

Notes and runners that reuse the formula, constants, functions, or numerical
source should cite this conditional calculator—not the parent no-go—as their
positive computational dependency. They must call the objective a supplied
candidate or conditional law, never a framework-derived physical selector.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py
```
