# SU(3) single-plaquette coefficient diagnostics and unresolved derivation

**Claim type:** open_gate
**Primary runner:** `scripts/cl3_c_iso_su3_nlo_2026_05_08_su3nlo.py`
**Current scope:** finite numerical quadrature/fit diagnostics and conditional arithmetic on supplied coefficients. The asserted analytic Wilson coefficient derivation and Hamilton-limit error bound remain unverified here.

## Current evidence boundary (2026-10-21)

The two historically cited artifacts are absent from this checkout:

- `outputs/action_first_principles_2026_05_08/c_iso_su3_nlo_closure/RESULTS.md`
- `outputs/action_first_principles_2026_05_08/c_iso_su3_nlo_closure/SU3_NLO_DERIVATION.md`

These are unavailable provenance paths, not working citations or recovered proofs.
The second was explicitly load-bearing for the claimed Vandermonde-Gaussian
moment derivation and cancellation `<Q W_1>_0 = 0`. This note does not now
assert that derivation as verified. No archived document has been substituted.
The runner evaluates a finite truncated-grid Weyl integral and fits coefficients;
a tolerance check on that fit is numerical support, not an exact asymptotic
proof or a certified quadrature/remainder bound. Its computations and thresholds
are preserved. A successful process does not discharge these open obligations.

For clarity, `P` in these single-plaquette formulas is the action deficit
`1 - Re Tr(U)/3`, not the trace-plaquette mean used as the historical Hamilton
scenario input. Supply the normalized SU(3) heat-kernel character expectation
`E[Re Tr(U)/3] = exp(-4s/3)` and the Wilson-series hypothesis
`P_W(β) = 4/β - 1/β² + c_3/β³ + O(β^-4)`, with `β = 3/s`.
Then the following conditional algebra is retained:

```
P_HK = 1 - exp(-4s/3) = 4s/3 - 8s²/9 + 32s³/81 + O(s⁴)
P_W = 4s/3 - s²/9 + c_3 s³/27 + O(s⁴)
P_W - P_HK = 7s²/9 + O(s³)
(P_W - P_HK)/P_HK = 7s/12 + O(s²)
(7/12)/(1/4) = 7/3
```

The Wilson coefficient `-1`, the series hypotheses and controlled remainders
are obligations here, not conclusions of the finite fit. The supplied
`c_3 = -4.33` is a historical numerical fit value, not an exact coefficient.
This conditional calculation alone does not transfer a one-plaquette discrepancy
to a multiplaquette Hamilton observable.

The corrected [epsilon-witness note](EXACT_TIER_EWITNESS_BOUNDED_NOTE_2026-05-07_ewitness.md)
reports that the preserved fast JSON has 400 measurement sweeps and
`0.4434036474783343 ± 0.00042693896349384414` at finite `4³×16`, ξ=4.
It does not establish the old `0.4410 ± 0.0006` thermodynamic-limit value,
1500-sweep/three-volume provenance or Hamilton-limit convergence.
Path B and Path C still calculate historical supplied scenarios using that
`0.4410`, statistical `0.0002`, volume `0.0006`, and the additional assumed
transfer rule `absolute shift = relative single-plaquette shift × 0.4410`.
Their tables, projected ξ≈430, and quadratic error combinations are conditional
arithmetic, not validated physical error budgets. The old multi-ξ MC values
`0.40949 ± 0.00050` and `0.28350 ± 0.00069` are preserved reports without
recovered logs; their provenance and physical interpretation remain open.

Needed before a stronger claim: recover or independently supply a checked
Wilson asymptotic derivation and remainder control, validate quadrature error,
recover the ensemble evidence, and justify the multiplaquette/limit transfer.
No theorem or audit status is promoted by this correction.

## Preserved historical argument — superseded scope

The discussion below preserves the former formulas, numerical reports, admissions
and references for diagnosis. Its words “derived”, “closure”, “bound”, “retained”,
and “verified” do not state the current claim. In particular its exact Wilson
coefficient derivation and Hamilton-limit conclusions are not current verified
results. The current claim is the open gate above. Original recovery is
`f24d17d97d372df977476e4a69674577f31af575:docs/C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md`.

## 0. Audit context

The Convention C-iso boundary on the temporal-step convention
`a_τ = a_s` was kept as an admitted discretization in
[`C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md`](C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md).

Subsequent work in
[`EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md`](EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md)
(PR #674) and the open `EXACT_TIER_EWITNESS_BOUNDED_NOTE_2026-05-07_ewitness.md`
(PR #685, branch `claude/exact-tier-ewitness-push-2026-05-07`,
commit 68aec765d) quantified the C-iso correction at LO and NLO using an
**SU(2) proxy** (the SU(2) Bessel-determinant single-plaquette form
` <P>_W = 1 - I_2(β)/I_1(β)` as a stand-in for the SU(3) calculation,
on the explicit understanding that "the SU(3) coefficient is
qualitatively the same... with slightly different leading coefficient").

**This work** replaces the SU(2) proxy with the actual SU(3)
Vandermonde-Gaussian moment derivation, deriving the closed-form
single-plaquette C-iso bound for SU(3) at NLO and verifying it against
direct numerical Weyl integration of the SU(3) Cartan torus.

## 1. Theorem (bounded, SU(3) NLO closed-form C-iso)

**Theorem (W3 SU(3) NLO Convention C-iso closure).** At canonical
operating point `g² = 1, ξ`, with `s_t := g²/(2ξ) = 1/(2ξ)`:

1. **(SU(3) heat-kernel single-plaquette, exact closed form.)**

   ```
   <P>_HK_SU(3)(s_t) = 1 - exp(-(4/3) s_t)
                     = (4/3) s_t - (8/9) s_t²  +  (32/81) s_t³  - O(s_t⁴)
   ```

   Derived from `<χ_R(U)>_HK = d_R · exp(-s_t · C_2(R))` with
   `C_2(fund SU(3)) = 4/3`. **Exact** (no perturbative truncation).

2. **(SU(3) Wilson single-plaquette, NLO closed form.)**

   ```
   <P>_W_SU(3)(β_W) = 4/β_W  -  1/β_W²  +  c_3/β_W³  +  ...
   ```

   with `c_3 ≈ -4.33` (numerical asymptotic fit; analytic closed form
   is documented frontier sub-task). In `s_t` (with `β_W = 3/s_t`):

   ```
   <P>_W_SU(3)(s_t) = (4/3) s_t  -  (1/9) s_t²  +  (c_3/27) s_t³  +  ...
   ```

   Derived via consistent expansion of both the action and the SU(3)
   Vandermonde-Haar measure to NLO, with key cancellation
   `<Q · W_1>_0 = 0` arising from the structure of the
   Vandermonde-modulated Gaussian (see analytic derivation note for
   details).

3. **(Convention C-iso single-plaquette discrepancy at NLO.)**

   ```
   (P_W - P_HK)_SU(3)(s_t) = (-1/9 + 8/9) s_t²  +  O(s_t³)
                          = (7/9) s_t²  +  O(s_t³)
   ```

   The leading `(4/3) s_t` term cancels exactly between Wilson and HK
   forms.

4. **(Relative shift, leading order.)**

   ```
   rel_shift_SU(3)(s_t) = (P_W - P_HK)/P_HK
                        = (7/12) s_t  +  O(s_t²)
                        ≈ 0.5833 s_t
   ```

5. **(Comparison to SU(2) proxy used in PR #685.)** The SU(2) proxy
   gave `rel_shift_SU(2) = 0.25 s_t`. The SU(3) result is therefore

   ```
   rel_shift_SU(3) / rel_shift_SU(2) = (7/12)/(1/4) = 7/3 ≈ 2.33
   ```

   The SU(2) proxy **underestimated** the C-iso correction by a factor
   2.33. This work upgrades the prior bounded theorems to use the
   actual SU(3) value.

## 2. What this closes vs. does not close

### Closed (bounded, this work)

- **SU(3) NLO single-plaquette C-iso analytic closed form**: derived in
  closed form via Vandermonde-Gaussian moment computation,
  cross-checked numerically against direct Weyl integration to 5+
  significant figures (asymptotic intercept c_2 = -1.00000 ± 0.00001).
- **Replacement of SU(2) proxy used in PR #685**: explicit factor-of-2.33
  correction identified.
- **Multi-ξ MC verification** (4³×16 lattices at ξ=8, 16) showing the
  path-integral spatial plaquette is xi-dependent, confirming the
  single-plaquette weight discrepancy is the relevant systematic
  (rather than multi-ξ extrapolation of `<P_σ>(ξ)`).

### Not closed (frontier remaining)

- **Exact-tier ε_witness `~3×10⁻⁴` on the full Hamilton-limit `<P>_KS`**:
  the SU(3) NLO bound is

  ```
  ε_C-iso(absolute on <P>_KS) ≈ 0.1287 / ξ
  ```

  (using `<P>_KS_∞ = 0.4410`). This requires `ξ ≳ 430` to drop below
  `ε_witness`. Compared to the prior PR #685 projection (ξ = 16–32
  based on SU(2) proxy), this is a **named compute frontier**: closure
  requires either:

  1. **GPU-accelerated MC at ξ ~ 500** on `16³ × T_t` lattices.
  2. **Analytic SU(3) NNLO** (`s_t³` coefficient `c_3` in closed form),
     extending the Vandermonde-Gaussian moment computation to higher
     order.
  3. **Direct heat-kernel-action MC** to eliminate the C-iso correction
     at the source.

- **Total error budget on Hamilton-limit `<P>`**:

  | ξ | `ε_total` | Note |
  |--:|:--:|:--|
  | 4 | 0.0317 | dominated by C-iso (99% of budget) |
  | 16 | 0.00805 | dominated by C-iso (99%) |
  | 32 | 0.00407 | dominated by C-iso (98%) |
  | 64 | 0.00211 | dominated by C-iso (95%) |

  At `ε_witness ~3×10⁻⁴`, even with `ε_C-iso = 0` the stat+vol budget
  `√(0.0002² + 0.0006²) = 6.3×10⁻⁴` is **above target**; tightening
  stat+vol is also part of the compute frontier.

### Final exact-tier numerical statement

```
<P>_σ(H_KS, g²=1) = 0.4410 ± 0.0006_stat-vol ± 0.0317_C-iso(ξ=4)
                  = 0.4410 ± 0.0006_stat-vol ± 0.00805_C-iso(ξ=16, projected)
                  = 0.4410 ± 0.0006_stat-vol ± 0.00211_C-iso(ξ=64, projected)
```

(C-iso error reported using SU(3) NLO formula; previous PR #685 numbers
underestimated this by factor 2.33.)

## 3. Conditional admissions

This bounded theorem inherits the conditional admissions of the
underlying framework, plus the named compute frontier above:

- `g_bare = 1` per [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md)
- `N_F = 1/2` per [`G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`](G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md)
- Convention C-iso temporal-step boundary per [`C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md`](C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md);
  this work upgrades the LO+NLO bounds to the correct SU(3) values.
- Anisotropic-coupling Trotter dictionary T-AT for the path-integral
  parameterization.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews the claim and
dependency chain.

## 4. Implementation overview

The runner [`scripts/cl3_c_iso_su3_nlo_2026_05_08_su3nlo.py`](../scripts/cl3_c_iso_su3_nlo_2026_05_08_su3nlo.py)
implements:

1. **SU(3) heat-kernel single-plaquette closed form**:
   `<P>_HK = 1 - exp(-(4/3) s_t)`, derived from character orthogonality
   on SU(3). Includes truncated Taylor series for cross-check.

2. **SU(3) Wilson single-plaquette numerical Weyl integration**: 2D
   trapezoidal quadrature over `(θ_1, θ_2)` with adaptive range
   truncation `min(π, 10/√β_W)` and `4·ngauss²` grid points. Numerically
   stable across `β_W ∈ [3, 10000]`, agreeing with the analytic NLO to
   `O(1/β_W²)` accuracy.

3. **SU(3) Wilson NLO analytic closed form**:
   `<P>_W = 4/β_W - 1/β_W² + (c_3/27) s_t³ + ...` with c_3 from numerical
   asymptotic fit. Used directly when `β_W > 5000` (where Weyl
   quadrature loses precision).

4. **Self-test**: cross-checks the analytic NLO derivation against the
   numerical Weyl integration via the asymptotic fit
   `(P_W·β - 4)·β = c_2 + c_3/β + c_4/β² + ...` returning
   `c_2 = -1.000` to 5 significant figures.

5. **Path A**: tabulates `<P>_HK`, `<P>_W` (numerical), and `rel_shift`
   across `ξ ∈ {1, 2, 4, 8, 16, 32, 64, 128}`. Polynomial fit extracts
   the LO/NLO/N²LO coefficients, verifying the analytic
   `(7/12) s_t = 0.583 s_t` LO.

6. **Path B**: combines the prior PR #685 thermodynamic-limit MC
   value `<P>_KS_∞ = 0.4410 ± 0.0006` with the SU(3) NLO
   `rel_shift_SU(3) = (7/12) s_t` to compute the absolute C-iso shift
   on the Hamilton-limit `<P>_KS` at canonical ξ values.

7. **Path C**: combined error budget showing C-iso dominates the total
   at all canonical ξ values currently accessible, and projecting
   ξ ≈ 430 to drive `ε_C-iso < ε_witness`.

The Path B verification used the inherited PR #685 runner
`scripts/cl3_exact_tier_ewitness_2026_05_07_ewitness.py` (on branch
`claude/exact-tier-ewitness-push-2026-05-07`, commit 68aec765d) to
run extended ξ=8 and ξ=16 MC ensembles on 4³×16:

| ξ | `<P_σ>` (this work) | wall time |
|:--:|:--:|:--:|
| 8 | 0.40949 ± 0.00050 | 2.5 min |
| 16 | 0.28350 ± 0.00069 | 2.5 min |

confirming the path-integral spatial plaquette is xi-dependent (the
analytic single-plaquette weight discrepancy is the relevant
systematic, not lattice-`<P_σ>` extrapolation).

## 5. Dependencies

- [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md)
  for `g_bare = 1`.
- [`C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md`](C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md)
  for the underlying C-iso temporal-step boundary.
- [`EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md`](EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md)
  (PR #674) for the prior LO bound that this work upgrades.
- `EXACT_TIER_EWITNESS_BOUNDED_NOTE_2026-05-07_ewitness.md`
  (PR #685, branch `claude/exact-tier-ewitness-push-2026-05-07`, commit
  68aec765d) for the multi-seed thermodynamic-limit `<P>_KS_∞ = 0.4410`
  input, and the SU(2) proxy NLO that this work supersedes.

These are imported authorities for a bounded theorem.

## 6. Boundaries

This note does NOT claim:

- **Exact-tier `ε_witness ~ 3×10⁻⁴`** on the full Hamilton-limit
  `<P>_KS`. The SU(3) NLO C-iso shift at xi=64 is `0.00211`, still
  ~7× above target.
- **Closed-form analytic c_3** (NNLO). The c_3 coefficient is
  numerically extracted (-4.33 ± 0.05); its closed form requires
  extending the Vandermonde and cosine series to `t⁸`, which is
  mechanically tractable but is left as a documented sub-frontier.
- **Full lattice multi-plaquette propagation**. The C-iso bound here
  is a **single-plaquette weight discrepancy**; the propagation to the
  full lattice `<P>` may pick up multi-plaquette factors of order
  unity, but the leading systematic is correctly captured at LO in
  `s_t`.
- **Tightening of stat+vol** below `ε_witness`. The current stat+vol
  budget `√(0.0002² + 0.0006²) ≈ 6.3×10⁻⁴` is above `ε_witness ~
  3×10⁻⁴`; further MC statistics or larger volumes are required even
  if C-iso were zero.

## 7. Standard lattice gauge theory references

- **Cabibbo N., Marinari E.** (1982), *A new method for updating SU(N)
  matrices in computer simulations of gauge theories*, Phys. Lett. B
  119, 387.
- **Drouffe J.M., Zuber J.B.** (1983), *Strong coupling and mean field
  methods in lattice gauge theories*, Phys. Rep. 102 — strong-coupling
  expansion / character form.
- **Menotti P., Onofri E.** (1981), *The action of SU(N) lattice gauge
  theory in terms of the heat kernel on the group manifold*, Nucl.
  Phys. B 190, 288 — heat-kernel action characterization.
- **Karsch F.** (1982), *SU(N) gauge theory couplings on asymmetric
  lattices*, Nucl. Phys. B 205, 285 — anisotropic SU(N) framework.
- **Klassen T.R.** (1998), *The anisotropic Wilson gauge action*, Nucl.
  Phys. B 533, 557 — anisotropic SU(3) tuning.
- **Engels J., Karsch F., Satz H.** (1990), *A finite-size analysis of
  the SU(3) deconfinement phase transition*, Nucl. Phys. B 342, 7 —
  SU(3) plaquette benchmarks.
- **Boyd G., Engels J., Karsch F., Laermann E., Legeland C., Lütgemeier
  M., Petersson B.** (1996), *Thermodynamics of SU(3) lattice gauge
  theory*, Nucl. Phys. B 469, 419 — modern-benchmark anisotropic SU(3)
  thermodynamics scaling.
- **Brower R.C., Rebbi C., Soni S.** (1981) — single-plaquette
  one-loop expansion for SU(N).
- **Kennedy A.D., Pendleton B.J.** (1985), *Improved heat bath method
  for Monte Carlo calculations in lattice gauge theories*, Phys. Lett.
  B 156, 393.
- **Lüscher M., Wolff U.** (1990), *How to calculate the elastic
  scattering matrix in two-dimensional quantum field theories by
  numerical simulation*, Nucl. Phys. B 339, 222.
