# Probe X-L1-MSbar — MSbar Beta-Function Source Check and Incomplete Lattice/`<P>` Rescaling: Open-Gate Source Note

**Date:** 2026-05-10
**Claim type:** open_gate (bounded diagnostic; mostly negative)
**Sub-gate:** Lane 1 (alpha_s) — beta_2, beta_3 scheme-native derivation probe
**Status authority:** independent audit lane only; effective status is
pipeline-derived.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane.

**Primary runner:** [`scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py`](../scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py)

## 0. Probe context

The adjacent running note defines a supplied-input piecewise two-loop `MSbar`
QCD EFT map with `n_f=6` above `m_t`, `n_f=5` below, and supplied identity
matching at the pole-mass threshold
(see [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)).
It does not include optional three- or four-loop coefficients. At `N_f=6`,
`beta_0 = 7` has a conditional upstream re-expression via the S1
Identification Source Theorem
([`SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`](SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md)
companion form `b_3 = (11 N_color − 2 N_quark)/3 = 7` for QCD).
`beta_1 = 102 - 38 N_f/3 = 26` is instead a supplied standard-continuum
QCD coefficient; the Casimirs and matter counts alone do not derive its
scalar weights.

The 3-loop and 4-loop coefficients `beta_2` and `beta_3` are
**scheme-dependent** and currently treated as unaudited "MSbar literature
imports."

This probe asks: can the framework's current source content
(physical Cl(3) local algebra, Z^3 spatial substrate, Casimir algebra,
plaquette structure, Wilson-loop expectation
`<P>`) directly derive the imported MSbar `beta_2` and `beta_3`, or define
them for the stipulated **lattice / `<P>` rescaling**? The displayed
rescaling is not itself a completed renormalization scheme.

## 1. Open Gate (bounded diagnostic, mostly negative)

**Open gate (X-L1-MSbar; bounded diagnostic).** On the physical Cl(3)
local algebra, Z^3 spatial substrate, and current framework source content,
the three-loop and four-loop QCD beta-function coefficients are not
derived for MSbar by current source content, while the stipulated
lattice/`<P>` rescaling does not yet define coefficients at all.
This is not an all-scheme no-go: finite coupling redefinitions can assign
higher beta coefficients in other schemes. Specifically:

1. **(The declared beta_0 and beta_1 coefficients have distinct authority.)** The 1-loop
   coefficient `beta_0 = (11 N_color − 2 N_quark)/3 = 7` at `N_f = 6` and
   the 2-loop coefficient `beta_1 = (34/3) C_A² − (20/3) C_A T_F N_f −
   4 C_F T_F N_f = 26` at `N_f = 6` are the standard coefficients used by
   the adjacent map. The first has the cited conditional upstream
   re-expression. The second is supplied standard-continuum input:
   substituting `(C_F = 4/3, C_A = 3, T_F = 1/2)` verifies `26` but does
   not derive the weights `34/3`, `20/3`, and `4`. Its usual universality is
   limited to the corresponding mass-independent coupling conventions.

2. **(The MSbar beta_2 import requires its perturbative calculation; the
   `<P>` rescaling requires a completed prescription.)**
   At 3-loop, consider the following candidate Casimir-tensor monomials:

   ```
   beta_2  =  c_FFF · C_F³  +  c_FFA · C_F² C_A  +  c_FAA · C_F C_A²
            + c_AAA · C_A³  +  c_FFn · C_F² T_F N_f  +  c_FAn · C_F C_A T_F N_f
            + c_AAn · C_A² T_F N_f  +  c_Fnn · C_F (T_F N_f)²
            + c_Ann · C_A (T_F N_f)²
   ```

   The displayed products of `C_F, C_A, T_F N_f` are a candidate Casimir-
   monomial enumeration, not a derivation of the actual nonzero diagrammatic
   basis. In particular, Casimir algebra alone does not decide which monomials
   occur. The **scalar coefficients `c_FFF, ..., c_Ann`** are scheme-dependent
   3-loop integrals that depend on:
   - choice of regularization and a completed renormalization condition,
   - choice of subtraction (MS-bar vs MOM vs Wilson-loop scheme),
   - 3-loop topology integrals (sunsets, ladders, cross diagrams).

   On current source content, the framework has NEITHER the
   dimensional-regularization machinery (foreign to the lattice
   substrate) NOR the lattice-perturbation-theory machinery (which would
   require explicit Brillouin-zone integrals over the Wilson lattice
   propagator that are not part of the current source stack).

3. **(beta_3 status: MSbar import and incomplete `<P>` rescaling.)** At 4-loop, a
   candidate monomial list extends with quartic Casimir tensors `(C_F⁴,
   C_F³ C_A, C_F² C_A², C_F C_A³, C_A⁴)` plus mixed `T_F N_f` terms; for
   QCD the higher-rank invariants `d_F^{abcd} d_F^{abcd} / N_R` and
   `d_F^{abcd} d_A^{abcd} / N_R` enter as Casimir
   algebra. The runner does not derive which candidate monomials occur or their
   scalar weights. MSbar requires its perturbative calculation; the `<P>`
   rescaling first requires a completed prescription.

4. **(The stipulated `<P>` rescaling differs from the bare coupling.)**
   The runner evaluates

   ```
   alpha_<P>(beta)  =  alpha_bare(beta) / <P>(beta)
   ```

   where the displayed `<P>(beta)` is supplied by the cited heat-kernel limit
   `<P>_HK = 1 - exp(-(4/3) s_t)` per
   [`C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md`](C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md)).
   This is a stipulated coupling convention in this probe; by itself it does
   not define a complete renormalization condition, an MSbar conversion, or a
   beta function.

5. **(No beta_2 follows from the stipulated rescaling.)** A separately
   completed lattice renormalization prescription and calculation could use:
   - 3-loop self-energy diagrams on a lattice (Wilson action),
   - tadpole-improved propagator integrals over the Brillouin zone,
   - mixing with the lattice-specific zero-mode and gauge fixing.

   None is performed here, so no `beta_2` for the `<P>` rescaling is defined
   or inferred.

## 2. What this closes vs. does not close

### Closed (positive observations)

- **The declared beta coefficients are reproduced with explicit authority.**
  `beta_0=7` has the cited conditional upstream re-expression; `beta_1=26`
  is reproduced from the supplied standard-continuum formula and Casimir
  values, without claiming a framework-native derivation of its weights.
- **Candidate Casimir monomials are evaluated algebraically.** The runner
  evaluates a finite monomial list but does not establish the actual nonzero
  three- or four-loop diagrammatic basis.
- **The stipulated `<P>` rescaling differs algebraically from the bare
  coupling.** This is a convention check only; it does not establish a full
  renormalization scheme or its higher beta coefficients.

### Open inputs and undefined rescaling data

- **beta_2 closed-form derivation in `MSbar`.** The scalar
  3-loop integral primitives that fix the candidate-monomial occurrences and coefficients
  `c_FFF, ..., c_Ann` are not in the current source content; they must be either
  (a) imported from MSbar literature [Tarasov-Vladimirov-Zharkov 1980,
      Larin-Vermaseren 1993], or
  (b) imported from lattice perturbation theory literature
      [Lüscher-Weisz 1995, Christou-Feo-Panagopoulos-Vicari 1998],
  or computed on a NEW perturbation-theory primitive layer outside
  current source content. A beta coefficient for the stipulated `<P>`
  rescaling remains undefined until a full prescription is supplied.
- **beta_3.** The MSbar coefficient is an
  external comparator [van Ritbergen-Vermaseren-Larin 1997], while current
  source content contains neither a completed `<P>` prescription nor the
  perturbative data needed to calculate its coefficient.
- **MSbar conversion from the stipulated `<P>` rescaling.** A separately
  defined renormalization condition and matching calculation are required;
  no conversion coefficient is inferred here.

### Final bounded statement

```
[POSITIVE]
beta_0 = (11 N_color − 2 N_quark)/3 = 7  (conditional upstream re-expression)
beta_1 = ((34/3) C_A² − (20/3) C_A T_F N_f − 4 C_F T_F N_f) = 26 at N_f=6
        (supplied standard-continuum formula; substitution check, not weight derivation)

[ALGEBRAIC DIAGNOSTICS]
Candidate Casimir monomials: evaluated, not an exhaustive beta-function basis
<P>(beta) heat-kernel expression: stipulated coupling rescaling for this probe

[OPEN INPUTS]
beta_2 and beta_3 for the stipulated <P> rescaling: UNDEFINED here;
        a completed prescription is required before matching or direct
        perturbative data can determine them

[FALSIFIABLE PREDICTION]
Total framework-native gain on Lane 1 bridge from this probe:
  - records the conditional upstream re-expression of β_0 and supplied
    standard-continuum authority of β_1; it does not turn the observed
    one-loop-to-two-loop shift into a remainder bound
  - MSbar β_2, β_3 remain external comparators; the stipulated <P>
    rescaling defines no beta coefficients;
    no claim is made for schemes defined by other finite coupling redefinitions
```

## 3. Supplied and imported context

This open gate uses the named supplied context and scheme-conversion
frontier above:

- `g_bare = 1` per [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md)
- S1 Identification Source Theorem per [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
- SU(3) Casimir authority per [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
- N_f = 6 above all SM thresholds (asymptotic regime)
- `<P>_HK_SU(3)` closed form per [`C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md`](C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md)

**Imported authorities (numerical comparators only, NOT load-bearing):**

- MSbar `beta_2 = 2857/2 − 5033 N_f / 18 + 325 N_f² / 54` per
  Tarasov-Vladimirov-Zharkov 1980; at `N_f = 6`: `beta_2 = 2857/2 −
  5033·6/18 + 325·36/54 = 2857/2 − 5033/3 + 650/3 = 2857/2 − 4383/3 =
  2857/2 − 1461 = -65/2`. The magnitude is `65/2`; the canonical
  sign in the usual `beta(g) = -beta_0 g^3/(16 pi^2) - ...`
  convention is negative at `N_f = 6`.
- MSbar `beta_3 = 149753/6 + 3564 zeta_3 − (1078361/162 + 6508 zeta_3 / 27)
  N_f + (50065/162 + 6472 zeta_3 / 81) N_f² + 1093/729 N_f³` per
  van Ritbergen-Vermaseren-Larin 1997; at `N_f = 6` numerically the
  VVL formula in convention `beta(g) = -beta_0 g^3/(16 pi^2) - ...`
  evaluates to `beta_3 ≈ 2472.28`. This comparator remains tied to the
  displayed formula and convention; no unrelated `643.83` value is treated
  as an alternate normalization of it.
- Christou-Feo-Panagopoulos-Vicari 1998 computes the three-loop
  bare-lattice beta-function coefficient for Wilson fermions and the
  two-loop MSbar-to-bare-coupling relation. That fixed Wilson bare-lattice
  result does not complete or define the different stipulated `<P>`
  prescription used by this probe.

These are imported numerical comparators for this open diagnostic; the
runner verifies them at the level of literature-cross-check, NOT
framework-native derivation.

## 4. Implementation overview

The runner [`scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py`](../scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py)
implements:

1. **CONDITIONAL source check 1**: `beta_0 = (11 N_color − 2 N_quark)/3 = 7`
   at `N_f = 6` from the cited S1/matter-count re-expression. Direct from
   `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`
   companion form for QCD.

2. **SUPPLIED-FORMULA check 2**: `beta_1 = (34/3) C_A² − (20/3) C_A T_F
   N_f − 4 C_F T_F N_f = 26` at `N_f = 6`. The runner verifies the
   substitution in the supplied standard-continuum formula; it does not derive
   the scalar weights from the Casimirs.

3. **ALGEBRAIC diagnostic 3**: A nine-element candidate Casimir-monomial
   list is evaluated. The runner does not enumerate Feynman topologies or
   establish that this is the actual nonzero three-loop basis.

4. **CONVENTION diagnostic 4**: `<P>_HK_SU(3)(s_t) = 1 - exp(-(4/3)
   s_t)` is used as a stipulated coupling rescaling. This does not by itself
   constitute a complete renormalization condition.

5. **OPEN-INPUT check 5**: For each candidate Casimir monomial, document
   that its occurrence and scalar weight in MSbar are not
   established by the monomial arithmetic.

6. **NUMERICAL comparator check 6**: Verify via direct rational
   arithmetic that the published MSbar values reproduce literature
   numbers at `N_f = 6`:
   - `beta_2^MSbar(N_f=6) = -65/2 = -32.5`
   - `beta_3^MSbar(N_f=6) ≈ 2472.28` in the displayed convention
   These are reported as literature-comparator only, NOT as framework
   derivations.

7. **SOURCE-CONTENT check 7**: Cite the fixed Wilson bare-lattice
   perturbative calculation without treating it as the coefficient of the
   incompletely specified `<P>` prescription. Current source content supplies
   neither that conversion nor a completed `<P>` renormalization condition.

8. **HONEST verdict**: open diagnostic for the MSbar source-content gap and
   incomplete `<P>` rescaling;
   coefficient substitution and candidate-monomial arithmetic do not close
   higher-loop coefficients.

## 5. Dependencies

- Framework baseline: physical Cl(3) local algebra and Z^3 spatial substrate
  (repo baseline; not a new premise in this note).
- [`SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`](SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md)
  for the SM gauge `b_2, b_3, b_QED` 1-loop trio in S1-structural form
  (companion `b_3 = 7` for QCD reused as `beta_0` here).
- [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
  for the S1 Identification Source Theorem.
- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  for upstream `(C_F, C_A, T_F)` Casimir authority.
- [`YT_P3_MSBAR_TO_POLE_K2_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`](YT_P3_MSBAR_TO_POLE_K2_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md)
  and [`YT_P3_MSBAR_TO_POLE_K3_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`](YT_P3_MSBAR_TO_POLE_K3_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md)
  for related color-factor bookkeeping; they do not establish an exhaustive
  beta-function channel basis here.
- [`C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md`](C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md)
  for the `<P>_HK_SU(3) = 1 - exp(-(4/3) s_t)` expression used in the
  stipulated rescaling diagnostic.
- [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
  for the supplied-input piecewise two-loop `MSbar` QCD EFT map (`n_f=6`
  then `n_f=5`, with supplied identity matching at `m_t`) treated as bounded
  standard infrastructure. It does not supply a boundary value, target match,
  or higher-order remainder bound.

These are imported authorities for a bounded diagnostic.

## 6. Boundaries

This note does NOT claim:

- **Framework-native closed form for `beta_2` or `beta_3` in `MSbar`, or
  any beta coefficient for the stipulated `<P>` rescaling.**
  Candidate-monomial arithmetic does not supply the MSbar perturbative data,
  and the rescaling is not a completed prescription. Other schemes are not
  excluded.
- **Promotion of any current MSbar import to retained.** The MSbar
  values for `beta_2, beta_3` remain external numerical inputs.
- **Direct contribution to closing Lane 1 alpha_s(M_Z).** Currently
  Lane 1 uses the supplied-input piecewise two-loop MSbar QCD map via
  [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md);
  the declared `beta_0, beta_1` formulas cover that bridge,
  so this probe does NOT change Lane 1 status.
- **Closed-form derivation of the lattice → MSbar scheme conversion.**
  No matching coefficient is inferred from the stipulated rescaling.

## 7. Standard QCD beta-function literature

- **Tarasov O.V., Vladimirov A.A., Zharkov A.Yu.** (1980), *The Gell-Mann-Low
  function of QCD in the three-loop approximation*, Phys. Lett. B 93, 429.
  Original 3-loop MSbar `beta_2` in QCD.
- **Larin S.A., Vermaseren J.A.M.** (1993), *The three-loop QCD beta-function
  and anomalous dimensions*, Phys. Lett. B 303, 334. Refined 3-loop MSbar.
- **van Ritbergen T., Vermaseren J.A.M., Larin S.A.** (1997), *The four-loop
  beta function in quantum chromodynamics*, Phys. Lett. B 400, 379. 4-loop
  MSbar `beta_3`.
- **Czakon M.** (2005), *The four-loop QCD beta-function and anomalous
  dimensions*, Nucl. Phys. B 710, 485. 4-loop MSbar verification.
- **Lüscher M., Weisz P.** (1995), *Computation of the relation between the
  bare lattice coupling and the MSbar coupling in SU(N) gauge theories to
  two loops*, Nucl. Phys. B 452, 234. Lattice → MSbar matching at 2-loop.
- **Christou C., Feo A., Panagopoulos H., Vicari E.** (1998), *The
  three-loop beta-function of SU(N) lattice gauge theories with Wilson
  fermions*, Nucl. Phys. B 525, 387 (with erratum). Three-loop
  bare-lattice coefficient and two-loop MSbar-to-bare relation.
- **Bode A., Weisz P., Wolff U. (ALPHA collaboration)** (2000), *Two-loop
  computation of the Schrödinger functional in lattice QCD*, Nucl. Phys.
  B 576, 517. Schrödinger-functional scheme at 2-loop.
- **Heitger J., Sommer R.** (2004), *Non-perturbative heavy quark effective
  theory*, JHEP 02, 022. Non-perturbative scheme.

## 8. Status summary

| Quantity | Scheme | Review status | Source |
|---|---|---|---|
| `beta_0 = 7` (N_f=6) | standard one-loop convention | conditional upstream re-expression | S1/matter-count note + this probe |
| `beta_1 = 26` (N_f=6) | supplied standard-continuum formula | substitution check only | standard QCD formula + Casimir values |
| Candidate 3-/4-loop Casimir monomials | diagnostic only | not an exhaustive diagrammatic basis | This probe |
| `<P>_HK_SU(3)` expression | stipulated rescaling | supplied by cited bounded note | C_ISO_SU3_NLO bounded note |
| `<P>` vs bare coupling | algebraic convention difference | not a full renormalization-scheme derivation | This probe |
| `beta_2^MSbar(N_f=6) = -65/2` | MSbar | bounded import/comparator | Tarasov-Vladimirov-Zharkov 1980 |
| `beta_3^MSbar(N_f=6) ≈ 2472.28` | MSbar | external comparator | van Ritbergen et al. 1997 |
| `beta_2`, `beta_3` for the `<P>` rescaling | incomplete stipulated prescription | not defined by this rescaling | This probe |
| `<P>` to MSbar conversion coefficient | conversion | open; not computed | This probe |

## 9. Falsifiable structural claims

1. `beta_0 = (11 N_color − 2 N_quark)/3 = 7` at upstream `N_quark = 6`,
   `N_color = 3`, `N_f = N_quark = 6`.
2. `beta_1 = (34/3) C_A² − (20/3) C_A T_F N_f − 4 C_F T_F N_f` evaluated
   at upstream `(C_F = 4/3, C_A = 3, T_F = 1/2, N_f = 6)` gives
   `(34/3)·9 − (20/3)·3·(1/2)·6 − 4·(4/3)·(1/2)·6 = 102 − 60 − 16 = 26`.
3. The displayed candidate Casimir monomials have the runner's stated values;
   no exhaustive QCD beta-function basis is inferred from that arithmetic.
4. The stipulated `<P>` rescaling changes `alpha_bare`; no MSbar conversion
   or higher beta coefficient follows from that algebraic fact.
5. The stipulated `<P>` rescaling uses `<P>_HK = 1 - exp(-(4/3) s_t)`;
   the runner does not derive a complete renormalization condition from it.

## 10. Reproduction

```bash
python3 scripts/cl3_koide_x_l1_msbar_2026_05_08_probeX_L1_msbar.py
```

Expected: coefficient-substitution and candidate-monomial arithmetic checks,
explicit OPEN lines for missing MSbar data and the incomplete rescaling, and a final
`open_gate` summary. No exhaustive loop basis or all-scheme no-go is claimed.
