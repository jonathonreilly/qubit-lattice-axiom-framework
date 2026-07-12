# DM Leptogenesis PMNS Reduction-Exhaustion Theorem

**Claim type:** bounded_theorem
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_dm_leptogenesis_pmns_reduction_exhaustion_theorem.py`

## Question

After the conditional PMNS-assisted `N_e` closure calculation, a natural review
question remained:

> Do we still need a separate uniqueness theorem about all possible closure
> components beyond the supplied reduced parameterization already used by the
> calculation?

This note closes that question for the scoped `N_e` closure claim on the
refreshed branch.

## Exact theorem

On the PMNS-assisted charged-lepton-active `N_e` route:

1. the exact closure problem already factors through the active reduced domain

   \[
   S_{\rm seed}
     = \{(x,y,\delta)\;|\;x_i>0,\ y_i>0,\ \sum_i x_i = 3\bar x_{N_e},\
        \sum_i y_i = 3\bar y_{N_e},\ \delta\in[-\pi,\pi]\},
   \]

   with \((\bar x_{N_e}, \bar y_{N_e})\) the supplied seed pair used by this
   conditional route;

2. the active chart used on the branch is exact and surjective onto the
   positive interior of that surface;

3. the full PMNS-assisted baryogenesis map factors exactly as

   \[
   D \to D_- \to dW_e^H \to H_e \to |U_e|^2{}^T \to i_* \to \eta,
   \]

   so there is no additional passive-sector or transport state outside that
   reduced domain;

4. therefore every closure component in this supplied PMNS-assisted `N_e`
   route parameterization lives on the fixed seed surface.

So the phrase “components beyond the exact closure surface we reduced to” is
not a live loophole for the scoped conditional calculation. Any uniqueness
claim is relative to that reduced surface; this theorem does not derive a
physical selector on it.

## What this changes for review

Before this theorem, the strongest Nature-style caveat was:

- the branch had a conditional selector calculation on the fixed seed
  surface, but not a separately stated theorem about hypothetical components
  outside that surface.

After this theorem, that caveat is narrowed away:

- the reduction chain shows that the supplied fixed `N_e` seed surface is the
  whole parameter domain used by this conditional PMNS route;
- so no separate theorem about components “beyond” it is needed.

This does **not** supply an internal selector theorem. It changes only the
conditional scope question: a supplied selector need not be evaluated outside
the reduced parameterization used by this route.

## Upstream authorities

The runner imports six PMNS-side modules; each has a framework wrapper note:

- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md) — flavor-column functional theorem.
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md) — active-projector reduction.
- [DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md) — multistart selector support.
- [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md) — conditional relative-action objective/calculator.
- [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md) — relative-action stationarity theorem.
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md) — projector interface supplying `canonical_h`, `monomial_h`, `pmns_projector_packet`.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_reduction_exhaustion_theorem.py
```
