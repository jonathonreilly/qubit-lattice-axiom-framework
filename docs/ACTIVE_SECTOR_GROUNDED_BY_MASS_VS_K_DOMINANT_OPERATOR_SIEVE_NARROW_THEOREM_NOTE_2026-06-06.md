# Conditional Mass-vs-|K| Dominant-Operator Sieve for an Active-Sector Assignment — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (conditional structural grounding; conditional on the energy-monitoring pointer principle)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/active_sector_mass_vs_k_sieve_grounding_runner.py`](../scripts/active_sector_mass_vs_k_sieve_grounding_runner.py)
**Cached output:** [`logs/runner-cache/active_sector_mass_vs_k_sieve_grounding_runner.txt`](../logs/runner-cache/active_sector_mass_vs_k_sieve_grounding_runner.txt)

## Audit context

The historical companion
`CKM_SMALL_VS_PMNS_LARGE_FROM_RECORD_READOUT_CONTEXT_NARROW_THEOREM_NOTE_2026-06-06`
is context rather than a load-bearing graph dependency here. This note independently evaluates a
conditional model in which a supplied mass-vs-`|K|` dominant-operator rule chooses between two
finite bases. It also records the elementary aligned-basis identity
`U_up = U_dn = I => V_CKM = I`. It neither derives the dominant-operator rule nor excludes any
position-observable, carrier, detection, or readout route.

## Safe statement

The `hw=1` generation triplet
([`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md))
carries two competing operators: the **mass** `M`, diagonal in the **corner**
(position/BZ) basis, and the emergent `C3` coupling `K = |K|·(J − I)`, diagonal in the **`C3`**
(DFT) basis. The pointer/active basis is the eigenbasis of the **dominant** of `{M, K}`.

**Theorem (conditional on energy-monitored pointer selection).**

1. **The dominant operator sets a mass-graded pointer basis.** For `|K| ≪` the generation
   mass-split, the pointer is the **corner** basis (mass eigenbasis); for `|K| ≫` the split, it is
   an eigenbasis approaching the **`C3` singlet-plus-doublet decomposition**. It contains the
   `C3`-singlet `W = (1,1,1)/√3` and hence a **trimaximal** column; the degenerate doublet does
   not select a unique full DFT basis.
2. **PMNS large.** Charged leptons (heavy, split `≫ |K|`) record in the corner basis (`U_e = I`);
   the neutrino (split `≪ |K|`) has an eigenbasis containing the `C3` singlet.
   `PMNS = U_e† U_ν` then carries a trimaximal column and `O(1)` mixing in the supplied example.
3. **CKM small.** The supplied mass-dominated up/down matrices give a near-identity mixing matrix.
   Exact identity follows only under the separately supplied aligned-basis hypothesis
   `U_up = U_dn = I`; it is not derived from finite dominance alone.
4. **Displayed finite comparison.** The supplied diagonal mass matrix has three **distinct**
   eigenvalues. The separately supplied real-symmetric `C3` matrix `aI+b(J-I)` has the exact
   spectrum `(a+2b,a-b,a-b)`. This is a property of the displayed comparison matrix only; it is
   not a theorem about position observables and supplies no carrier/readout exclusion.
5. **Sampled crossover.** On the five supplied ratios, the classification changes from a basis
   containing a near-trimaximal singlet column at small split/`|K|` to a corner-like basis at large
   split/`|K|`. This finite sample is not a proof of a unique or sharp monotone threshold. With
   `|K|` the emergent `C3` coupling at the massless-gravity scale
   ([`DELTA_MAGNITUDE_REDUCES_TO_MASSLESS_GRAVITY_SCALE_NARROW_THEOREM_NOTE_2026-06-06`](DELTA_MAGNITUDE_REDUCES_TO_MASSLESS_GRAVITY_SCALE_NARROW_THEOREM_NOTE_2026-06-06.md)),
   the supplied sector hierarchy places only the neutrino on the small-split side of the displayed
   sample while the heavier sectors lie on the corner-like side. This is the
   [`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26`](PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md)
   structure, here evaluated under the supplied dominance hypotheses.

Thus the large-PMNS/small-CKM contrast follows inside this supplied model once the sector-dependent
dominance hypotheses and the energy-monitoring pointer rule are assumed.

## The genuine open piece (the residual)

The grounding is **conditional on the energy-monitoring pointer principle** — that the records
register the eigenbasis of the dominant (energy) operator. This is the einselection **monitor
identity**, the open slot named in
[`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md).
This note does not derive monitor identity from the minimal axioms and does
not compare its supplied conditional model with other possible carrier or readout constructions.

## Boundary (honest)

- **Conditional, not unconditional.** It holds *given* energy-monitored pointer selection; that
  principle is the residual (the monitor slot).
- **No mass values forced.** The mass hierarchy (neutrino lightest) is the registered input; the
  sieve converts it into the active-sector assignment. No `r`/`Q`/Koide value is touched (this is
  about mixing angles, not mass ratios — it does **not** depend on the firewalled `r=1/2`).
- **No fitted mixing used as input.** The trimaximal column and near-identity CKM matrix are
  outputs of the displayed finite examples; no PDG mixing value enters.
- **No route exclusion.** The displayed mass and real-symmetric `C3` matrices do not imply a
  theorem about position observables or foreclose another carrier, detector, or readout route.

## Forbidden imports check

No new axiom. The corner/`C3` operator structure, the dominant-operator pointer, and the PMNS/CKM
matrix elements are finite matrix calculations on the supplied `hw=1` triplet. `|K|` is the emergent `C3`
coupling already characterized on `main`. The energy-monitoring pointer principle is the framework's
existing (open-slot) einselection mechanism, applied — flagged as the conditional, not imported as a
new axiom.

## Runner check breakdown

Class A: (1) the supplied eigenbasis approaches corner form for heavy split and contains a
near-trimaximal singlet column for light split; (2) charged-corner + neutrino-singlet-column →
trimaximal PMNS column + large mixing in the displayed example; (3) the supplied mass-dominated
quark matrices give near-identity mixing; (4) the displayed diagonal mass spectrum is simple,
the displayed real-symmetric `C3` spectrum has its stated doublet, and the supplied `C3` coupling
has the exact singlet/doublet eigenspaces; (5) the five sampled ratios separate into the reported
near-trimaximal and corner-like sides.
Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is finite linear algebra on the `hw=1` triplet. The sampled eigenbasis of
`M + |K|(J−I)` approaches the corner basis when `M` dominates and contains a vector approaching
the singlet `W` when `|K|` dominates; the degenerate doublet is not a unique full DFT basis. The
supplied examples give near-identity CKM and a trimaximal PMNS column. The exact spectrum comparison
concerns only the two displayed matrices, the crossover statement is limited to the sampled ratios,
and neither carries a position-observable or route-exclusion conclusion. The result is
**conditional on the energy-monitoring pointer principle** (the open monitor slot); it forces no
mass value and uses no fitted mixing. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/active_sector_mass_vs_k_sieve_grounding_runner.py
```
