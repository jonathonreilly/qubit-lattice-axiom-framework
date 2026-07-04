# DM Leptogenesis PMNS Reduction-Exhaustion Theorem

**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_dm_leptogenesis_pmns_reduction_exhaustion_theorem.py`

## Question

After the PMNS-assisted `N_e` closure selector theorem, a natural review
question remained:

> Do we still need a separate uniqueness theorem about all possible closure
> components beyond the exact reduced surface already used by the selector
> theorem?

This note addresses that question for the scoped `N_e` closure claim on the
refreshed branch.

## Exact theorem

On the PMNS-assisted charged-lepton-active `N_e` route:

1. the exact closure problem already factors through the active reduced domain

   \[
   S_{\rm seed}
     = \{(x,y,\delta)\;|\;x_i>0,\ y_i>0,\ \sum_i x_i = 3\bar x_{N_e},\
        \sum_i y_i = 3\bar y_{N_e},\ \delta\in[-\pi,\pi]\},
   \]

   with \((\bar x_{N_e}, \bar y_{N_e})\) the exact native seed pair already
   derived on branch;

2. the active chart used on the branch is exact and surjective onto the
   positive interior of that surface;

3. the full PMNS-assisted baryogenesis map factors exactly as

   \[
   D \to D_- \to dW_e^H \to H_e \to |U_e|^2{}^T \to i_* \to \eta,
   \]

   so there is no additional passive-sector or transport state outside that
   reduced domain;

4. therefore every admissible PMNS-assisted `N_e` closure component already
   lives on the exact fixed native seed surface.

So the phrase “components beyond the exact closure surface we reduced to” is
not a live loophole for the scoped `N_e` closure claim. The remaining selector
question is internal to **that exact reduced surface**.

## What this changes for review

Before this theorem, the strongest Nature-style caveat was:

- the branch had sampled selector support on the fixed native seed surface,
  but not a separately stated theorem about hypothetical components outside
  that surface.

After this theorem, that caveat is narrowed away:

- the exact reduction chain already proves that the fixed native `N_e` seed
  surface is the whole admissible PMNS-assisted closure domain on this route;
- so no separate theorem about components “beyond” it is needed.

This does **not** change the internal selector theorem itself. It changes the
scope question: the selector theorem no longer has to rule on a larger domain
that the exact reduction chain already excludes.

## Upstream authorities

The runner imports six PMNS-side modules; each has a framework wrapper note:

- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md) — flavor-column functional theorem.
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md) — active-projector reduction.
- [DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md) — multistart selector support.
- [DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md) — observable-relative action law.
- [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md) — relative-action stationarity theorem.
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md) — projector interface supplying `canonical_h`, `monomial_h`, `pmns_projector_packet`.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_reduction_exhaustion_theorem.py
```
