# The Emergent C3 Coupling Scale: Constrained to a 9-Order Window; the Neutrino's Unique Lightness Explains Small-CKM-vs-Large-PMNS — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (quantitative: the predictability-sieve window + explanatory robustness; precise scale left open)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/emergent_coupling_scale_window_runner.py`](../scripts/emergent_coupling_scale_window_runner.py)
**Cached output:** [`logs/runner-cache/emergent_coupling_scale_window_runner.txt`](../logs/runner-cache/emergent_coupling_scale_window_runner.txt)

## Audit context

[`FLAVOR_READOUT_CONTEXT_IS_THE_DERIVABLE_DECOHERENCE_POINTER_BASIS_NARROW_THEOREM_NOTE_2026-06-06`](FLAVOR_READOUT_CONTEXT_IS_THE_DERIVABLE_DECOHERENCE_POINTER_BASIS_NARROW_THEOREM_NOTE_2026-06-06.md)
derived the flavor readout context as the **decoherence pointer basis** (the predictability
sieve): a generation sector is recorded in the **corner** mass-eigenbasis if its mass spread
exceeds the emergent `C3` coupling scale `|K|`, and in the **C3** central-sector basis (→ the
trimaximal column → large mixing) if its spread is below `|K|`. It left one quantitative
piece open: the value of `|K|`. This note computes the **constraint** on `|K|` and shows the
observed flavor pattern is **robust** to its precise value.

## Safe statement

**Theorem.**

1. **The neutrino sits in a vast gap.** From the PDG fermion masses, the generation mass
   spreads are: neutrino `~ 0.05 eV`; charged leptons `~ 1.78 GeV` (`m_τ`, smallest splitting
   `m_μ − m_e ≈ 106 MeV`); down quarks `~ 4.2 GeV` (smallest splitting `m_s − m_d ≈ 92 MeV`);
   up quarks `~ 173 GeV`. The neutrino spread is **~9 orders of magnitude below** the smallest
   mass splitting of any other sector (`92 MeV / 0.05 eV ≈ 2×10⁹`).

2. **The predictability-sieve window for `|K|`.** For the neutrino to be `C3` and all other
   sectors corner, `|K|` must satisfy

   ```text
   Δm_ν  ≪  |K|  ≪  min(other-sector splittings)
   i.e.  0.05 eV  ≪  |K|  ≪  ~92 MeV.
   ```

   This window spans the ~9-order gap of (1).

3. **Robustness (no fine-tuning).** For `|K|` sampled anywhere across that window, the sieve
   assigns **neutrino → C3** (its tiny spread is below `|K|`) and **charged leptons + up +
   down quarks → corner** (their spreads exceed `|K|`). So the observed pattern does **not**
   require a tuned `|K|`; any value in the vast window reproduces it.

4. **Explanation of small-CKM-vs-large-PMNS.** The mechanism predicts that **only sectors
   lighter than `|K|` are `C3`** (large mixing). The neutrino is the unique such sector → it
   alone has large mixing (PMNS); all heavier sectors are corner → small mutual mixing
   (`U_e = I`; small CKM, both quark sectors corner-aligned). The framework's noticed-but-
   underived small-CKM/large-PMNS anti-correlation is thereby **explained**: it is the
   neutrino's unique lightness (its position in the ~9-order gap below all other fermions).

## The genuine open piece (and why the result survives it)

The **precise** `|K|` — the emergent `C3` coupling, i.e. the scale of the native
second-order double-shift coupling `J − I` on the generation triplet — is **not computed
here**; it requires the `LATTICE`+`QUANTUM` emergent-scale calculation (the double-shift
amplitude `~ t²/E_gap`). But the result of (3)–(4) is **robust to its value**: because the
neutrino-to-charged gap is ~9 orders wide, the corner-vs-`C3` assignment — and hence
small-CKM-vs-large-PMNS — holds for any `|K|` in `[0.05 eV, 92 MeV]`. The precise `|K|`
would refine *quantitative* mixing details (e.g. the size of sub-leading admixtures), not
the qualitative pattern.

## Boundary (honest)

- **A constraint + robustness + explanation, NOT a precise `|K|` prediction.** The note
  computes the *window* (from observed masses) and shows the pattern is robust within it; it
  does **not** predict the precise `|K|` (that is the open emergent-coupling computation).
- **Uses observed masses** as the empirical comparator (named as such). The PDG spreads are
  inputs; the framework content is the predictability-sieve mechanism (cited) and the
  consequence that the uniquely-light neutrino is the unique `C3` sector.
- **Which corner basis** the charged sectors take (`U_e = I`) rests on the unaudited `Z_3`
  trichotomy; **why the neutrino is light** (its position in the gap) is a separate question
  (the neutrino-mass mechanism). This note takes the masses as given and derives the
  *readout-pattern* consequence.

## Forbidden imports check

No new axiom. Uses the predictability-sieve mechanism (existing,
`FLAVOR_READOUT_CONTEXT_IS_THE_DERIVABLE_DECOHERENCE_POINTER_BASIS`) and the observed PDG
masses (empirical comparator). The window and the robustness are arithmetic; the precise
`|K|` is named open, not imported.

## Runner check breakdown

Class A: the neutrino spread is uniquely smallest; the gap to the next-smallest fermion
splitting is ~9 orders; the `|K|` window spans it; the sieve is robust across the window
(neutrino → C3, others → corner); the prediction (only sub-`|K|` sectors are C3) yields only
the neutrino and matches the data; the precise `|K|` is documented open. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is arithmetic on the PDG mass spreads plus the cited predictability-sieve
mechanism: the neutrino's spread (`~0.05 eV`) is ~9 orders below the smallest mass splitting
of any other sector (`~92 MeV`), so the sieve window for `|K|` is vast, and any `|K|` in it
gives neutrino → C3 (large PMNS) and all heavier sectors → corner (small CKM, `U_e = I`). The
genuine result is the **robustness + explanation**: the small-CKM/large-PMNS anti-correlation
follows from the neutrino's unique lightness, for any `|K|` in the gap — no fine-tuning. The
note does **not** compute the precise `|K|` (the open emergent-coupling/double-shift scale),
and it takes the masses and the charged corner-basis (trichotomy, unaudited) as given.
Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_coupling_scale_window_runner.py
```
