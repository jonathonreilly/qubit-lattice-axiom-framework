# Probe U-L1-Resurgence — QCD Trans-Series and Stokes Structure for β_2, β_3: Bounded-Tier Source Note

**Date:** 2026-05-10
**Claim type:** open_gate (partial attempt: a stipulated leading-asymptotic
ansatz does not determine finite-order coefficients)
**Sub-gate:** Lane 1 (alpha_s) — beta_2, beta_3 resurgence-structure probe
**Status authority:** independent audit lane only; effective status is
pipeline-derived.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane.

**Primary runner:** [`scripts/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.py`](../scripts/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.py)
**Cached output:** [`logs/runner-cache/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.txt`](../logs/runner-cache/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.txt)

## 0. Probe context

Probe X-L1-MSbar ([`KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md`](KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md))
records an open input for the 3-loop and 4-loop QCD beta-function
coefficients in the explicitly considered `MSbar` and stipulated
lattice/`<P>` prescriptions. It does not establish an all-scheme no-go or
an exhaustive Casimir-tensor basis.

A natural follow-on question is:

**Can resurgence / trans-series machinery, applied to QCD running
coupling with the current physical `Cl(3)` local algebra + `Z^3`
spatial substrate inputs, give `beta_2` (and possibly `beta_3`)
structural identities by relating perturbative coefficients to
non-perturbative content via Stokes phenomena?**

Resurgence (Écalle 1980s; for QFT: Marino, Aniceto, Schiappa, Mariño-Reis,
Cherman-Dorigoni-Ünsal, Costin-Dunne) bridges perturbative and
non-perturbative content: a trans-series

```
alpha_s^trans(mu)  =  alpha_s^pert(mu)
                    +  Σ_n  exp(-S_n / alpha_s) · alpha_s^{a_n} · (
                              c_n^(0) + c_n^(1) alpha_s + ... )
```

is connected to a perturbative tail by Stokes data. For this route check only,
stipulate the following formal coefficient ansatz:

```
β_n^pert  ~  (S_IR / (2π)) · Γ(n + b)
              · (β_0 / (4π))^{n+1} · [1 + O(1/n)]
```

Here `b`, `S_IR`, and the finite-order corrections are free ansatz data. The
cited observable-renormalon literature motivates the general asymptotic
notation but does not establish this formula for the QCD beta-coefficient
sequence.

This probe asks only whether the displayed leading data determine finite
`beta_2` or `beta_3` values.

## 1. Open gate (leading-asymptotic data are insufficient at finite order)

**Open gate (U-L1-Resurgence).** If one stipulates the displayed leading
factorial ansatz with supplied `beta_0`, then the ansatz still contains free
normalization, exponent, and finite-order correction data. It therefore does
not determine `beta_2` or `beta_3`. This is an information-sufficiency result
for that ansatz only. The note does not establish that the QCD beta-coefficient
sequence itself has the displayed Borel singularities, and it does not
foreclose a complete resurgent construction or a finite scheme redefinition.

1. **(The stipulated primary location is parameterized by `β_0`.)** In
   the toy ansatz, define the primary and secondary locations

   ```
   z_* = 4π / β_0 = 4π / 7,
   z_n = -4π / (n β_0) = -4π / (7n)
   ```

   after supplying the 1-loop coefficient `β_0 = 7`. These are definitions
   inside the ansatz, not physical IR/UV-renormalon
   claims or evidence about the beta-coefficient sequence.

2. **(The asymptotic factorial form is stipulated, not derived.)** The form

   ```
   β_n^pert  ~  C · Γ(n + b) · (β_0 / (4π))^{n+1}
   ```

   for large `n` is stipulated. The growth-rate base `(β_0/(4π))^n`
   is fixed after supplying `β_0`; the prefactor and exponent remain free.

3. **(The ansatz normalization is free.)** The runner supplies no independent
   value of `S_IR`. Fitting that normalization to a finite coefficient is not
   a prediction of the next coefficient. No claim is made here about whether
   a complete resurgent construction could calculate it.

4. **(Resurgence relation is ASYMPTOTIC, not exact for small n.)** The
   stipulated relation `β_n ~ Γ(n+b) (β_0/(4π))^{n+1} S_IR / (2π)` is
   an ASYMPTOTIC formula valid for large `n`. For finite `n = 2` (3-loop)
   and `n = 3` (4-loop), corrections to the leading asymptotic form are not
   parametrically controlled and cannot be assumed small. A precise computation
   of `β_2` and `β_3` would require additional finite-order or complete
   Borel data not present in this route check.

5. **(No physical Borel map is supplied.)** The route does not identify a
   physical observable or beta-coefficient sequence whose Borel transform is
   the toy ansatz.

## 2. What this closes vs. does not close

### Toy-ansatz arithmetic

- **The defined locations are determined algebraically by `β_0 = 7`.**
  They are `z_*=4π/7` and `z_n=-4π/(7n)` for the toy ansatz only.
- **Factorial growth rate `(β_0/(4π))^n = (7/(4π))^n` is fixed within
  the same stipulated ansatz.**
  This sets the asymptotic scale for `β_n` at large `n`.
- **Resurgence/renormalon theory is an imported mathematical toolkit for
  this open route check, not a framework axiom or audit-status
  surface.**

### Open inputs for this partial attempt

- **Stokes constant `S_IR`.** Not supplied or computed by this route.
- **Constant `b` (subleading exponent in `Γ(n+b)`).** Free ansatz data;
  no QCD operator formula is asserted.
- **Finite-order corrections.** Not supplied by the leading ansatz.
- **Closed-form derivation of `β_2` or `β_3`.** The leading ansatz alone
  is underdetermined; complete-data and scheme-redefinition routes remain open.

### Final open-gate statement

```
[STIPULATED LEADING-ANSATZ OBSERVATIONS]
Toy primary location z = 4π / β_0 = 4π / 7
Toy secondary locations z_n = −4π / (β_0 n) = −4π / (7n)
Asymptotic factorial growth: β_n ~ Γ(n + b) · (β_0/(4π))^{n+1} · const
Asymptotic ratio: β_{n+1} / β_n  ~  (β_0/(4π)) · (n + b)  for n → ∞

[OPEN INPUTS]
Normalization S_IR: not supplied

Exponent b in Γ(n+b): not supplied

1/n corrections at finite n=2, 3: not supplied by this leading ansatz

β_2 finite value: not determined by the leading asymptotic ansatz; the
formula gives only ~ Γ(2+b) · (7/(4π))^3 · S_IR with free data

β_3 finite value: likewise not determined; leading asymptotic
~ Γ(3+b) · (7/(4π))^4 · S_IR

[NUMERICAL DIAGNOSTIC]
Evaluating the stipulated formula at finite n shows explicit dependence on
the free normalization and exponent. No comparison is promoted as evidence
for a beta-series Borel geometry.

[DIAGNOSTIC RESULT]
Net contribution to Lane 1 from this probe:
  - evaluates Borel-plane locations and scaling inside the stipulated ansatz
  - shows that free S_IR, b, and finite-n corrections prevent a finite-order
    prediction from those leading data alone
  - leaves complete-resurgence and finite-scheme-redefinition routes open
```

## 3. Supplied and imported context

This open diagnostic uses the named supplied context and imported
resurgence notation:

- `g_bare = 1` per [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md)
- S1 Identification Source Theorem per [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
- SU(3) Casimir authority per [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
- N_f = 6 above all SM thresholds (asymptotic regime)
- `β_0 = 7` via the cited conditional one-loop re-expression; `β_1=26`
  is supplied by the standard-continuum formula, as clarified in probe X-L1

**Imported mathematical toolkit (route-check scope; not a new axiom):**

- **Resurgence theory** (Écalle 1980s; Costin 2009; Mariño 2014;
  Aniceto-Basar-Schiappa 2019). Borel-Laplace transform, Stokes
  phenomena, trans-series construction.
- **Renormalon literature** (t'Hooft 1977; Mueller 1985; Beneke 1998),
  used only to motivate generic asymptotic notation; it does not supply a
  beta-coefficient Borel map here.

**Imported authorities (numerical comparators only, NOT load-bearing):**

- Tarasov-Vladimirov-Zharkov 1980, MS-bar `β_2(N_f=6) = -65/2 = -32.5`
  in the displayed convention.
- van Ritbergen-Vermaseren-Larin 1997, MS-bar `β_3(N_f=6) ≈ 2472.28`
  in the displayed convention.
- Mariño 2014, *Lectures on non-perturbative effects in large N gauge
  theories, matrix models and strings*, Fortschritte der Physik 62, 455.

These are external context only; the runner does not verify or fit the
literature beta coefficients.

## 4. Implementation overview

The runner [`scripts/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.py`](../scripts/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.py)
implements:

1. **ANSATZ arithmetic check 1**: Toy locations `z_* = 4π/β_0 = 4π/7`
   and `z_n = -4π/(7n)` after supplying `β_0 = 7`.

2. **ANSATZ arithmetic check 2**: The stipulated growth base
   `(β_0/(4π))^{n+1}` after supplying `β_0`.

3. **ANSATZ arithmetic check 3**: The ratio formula
   `β_{n+1}/β_n → (β_0/(4π))(n+b)` is evaluated symbolically.
   Finite literature coefficients are not used as evidence.

4. **OPEN-INPUT check 4**: Stokes constant `S_IR` is not supplied by this
   route; no impossibility or required new identification is inferred.

5. **OPEN-INPUT check 5**: Subleading exponent `b` in `Γ(n+b)` is not
   fixed by the supplied `beta_0,beta_1` values alone.

6. **NUMERICAL ansatz check 6**: Compute the leading asymptotic
   resurgence prediction
   ```
   β_n^asymp  =  (S_IR / (2π)) · Γ(n + b) · (β_0/(4π))^{n+1}
   ```
   for `n = 2, 3` at two explicitly chosen normalizations to show that the
   finite values vary with free ansatz data. No literature match is claimed.

7. **HONEST verdict**: open gate; leading asymptotic data alone do not
   determine finite `beta_2, beta_3`, while complete-data and scheme routes
   remain open.

## 5. Dependencies

- [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) —
  physical `Cl(3)` local algebra + `Z^3` spatial substrate baseline.
- [`SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`](SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md)
  for the structural form of `β_0` (companion form for QCD: `β_0 = 7`).
- [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
  for the S1 Identification Source Theorem.
- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  for retained `(C_F, C_A, T_F)` Casimir authority.
- [`KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md`](KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md)
  for the parent X-L1 open diagnostic (this probe adds only a
  leading-asymptotic information-sufficiency check).
- [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
  for the supplied-input piecewise two-loop `MSbar` QCD EFT map (`n_f=6`
  then `n_f=5`, with supplied identity matching at `m_t`) treated as bounded
  standard infrastructure. It does not supply a boundary value, target match,
  or higher-order remainder bound.

These are supplied/imported context for an open diagnostic.

## 6. Boundaries

This note does NOT claim:

- **A universal no-go for `β_2` or `β_3` via resurgence.** The note only
  shows that the stipulated leading ansatz, with free normalization, exponent,
  and finite-order corrections, is insufficient by itself.
- **Promotion of any current MS-bar or lattice import to retained.** The
  literature values for `β_2, β_3` remain external numerical inputs.
- **A physical Borel map.** No observable-to-beta-series identification is
  supplied by this toy ansatz.
- **Direct contribution to closing Lane 1 alpha_s(M_Z).** Currently
  Lane 1 uses the supplied-input piecewise two-loop MSbar QCD map via
  [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md);
  this probe does NOT change Lane 1 status.
- **A claim about all resurgent reconstructions.** This leading ansatz supplies
  no finite-order data; complete resurgent routes remain open.

## 7. Resurgence and renormalon literature

- **Écalle J.** (1981), *Les fonctions résurgentes (3 volumes)*, Publ.
  Math. d'Orsay. Foundational treatise on resurgent functions, alien
  calculus, Stokes phenomena.
- **t'Hooft G.** (1977), *Can we make sense out of "Quantum
  Chromodynamics"?*, in *The Whys of Subnuclear Physics*, ed. A.
  Zichichi. Original IR renormalon proposal.
- **Mueller A.H.** (1985), *On the structure of infrared renormalons in
  physical processes at high energies*, Nucl. Phys. B 250, 327. IR/UV
  renormalon classification.
- **Beneke M.** (1998), *Renormalons*, Phys. Rep. 317, 1-142. Standard
  reference on QCD renormalons.
- **Costin O.** (2009), *Asymptotics and Borel summability*, Chapman &
  Hall. Mathematical foundation of resurgent analysis.
- **Mariño M.** (2014), *Lectures on non-perturbative effects in large N
  gauge theories, matrix models and strings*, Fortsch. Phys. 62, 455.
- **Aniceto I., Basar G., Schiappa R.** (2019), *A primer on resurgent
  transseries and their asymptotics*, Phys. Rep. 809, 1. Modern
  pedagogical review.
- **Cherman A., Dorigoni D., Ünsal M.** (2015), *Decoding perturbation
  theory using resurgence: Stokes phenomena, new saddle points and
  Lefschetz thimbles*, JHEP 10, 056. Application to gauge theories.
- **Costin O., Dunne G.V.** (2019), *Resurgent extrapolation: rebuilding
  a function from asymptotic data*, J. Phys. A 52, 445205.

## 8. Status summary

| Quantity | Status | Source |
|---|---|---|
| `β_0 = 7` (N_f=6) | supplied with conditional upstream re-expression | S1/matter-count note, probe X-L1 |
| `β_1 = 26` (N_f=6) | supplied standard-continuum formula | probe X-L1 |
| Stipulated Borel location `z = 4π/7` | ansatz arithmetic only | This probe |
| Stipulated secondary toy locations `z = -4π/(7n)` | ansatz arithmetic only | This probe |
| Stipulated growth base `(β_0/(4π))^n = (7/(4π))^n` | ansatz arithmetic only | This probe |
| Asymptotic form `Γ(n+b) (β_0/(4π))^{n+1}` | supplied ansatz | This probe |
| Stokes constant `S_IR` | open input | This probe |
| Subleading exponent `b` in `Γ(n+b)` | open input | This probe |
| Finite-`n` corrections at n=2, 3 | open input | This probe |
| `β_2` finite value via leading ansatz | not determined | This probe |
| `β_3` finite value via leading ansatz | not determined | This probe |
| Literature-coefficient asymptotic trend | not asserted | wrong-sign/value legacy check removed |

## 9. Falsifiable diagnostic claims

1. Substitution of supplied `β_0=7` into the stipulated location formulas
   gives `4π/7` and `-4π/(7n)`.
2. The stipulated leading form depends on free `S_IR` and `b`.
3. Two distinct choices of those free data give distinct finite `n=2,3`
   values while preserving the same supplied `β_0`.
4. Therefore the leading ansatz and `β_0` alone do not determine finite
   `β_2` or `β_3`; no broader resurgence or scheme no-go follows.
5. Complete Borel data, a justified observable-to-beta-series map, and finite
   scheme transformations remain untested routes.

## 10. Reproduction

```bash
python3 scripts/cl3_koide_u_L1_resurgence_2026_05_08_probeU_L1_resurgence.py
```

Expected: arithmetic checks inside the stipulated leading ansatz, explicit
open-input lines for its free parameters, and a final `open_gate` summary that
does not treat finite literature coefficients as asymptotic evidence.
