# Focused independent canonical source confirmation

Reviewer: `/root/localized_history_check`. Date: 2026-10-15 UTC.

I find no unresolved mathematical discrepancy in the five canonical sources below within their explicitly supplied model and regularity hypotheses. The package establishes conditional positive energy bounds and finite specific controls. It does not select an initial history, measure its energy, establish an actual radio-count-to-force calibration, or rule out every alternative theory or initial-data route. This is a focused scientific/source confirmation, not an applied audit verdict, publication approval, or integration review.

## Coverage and final identities

I read the entire initial canonical note and all four source files, then the complete affected additions and formula-sharing repair, and finally every line of the wording-only diff. Thus the complete final 508-line note and four final files are covered; unchanged bodies were not needlessly re-reviewed. The final wording replaces ambiguous references to prior notes with references to the proofs displayed in this note, accurately attributes the 70/133/57 counts to the canonical runner, and repairs spacing. It changes no formula or executable.

All paths in this section are relative to `/Users/jonBridger/.codex/worktrees/observations-backward-24h-20261014/New Axioms Lets Go`.

| Source | Lines | Final SHA-256 |
| --- | ---: | --- |
| `docs/SCALAR_FINITE_WINDOW_INITIAL_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-15.md` | 508 | `059e1ff0ef5ab67e71763a55b022e130348b54e8477b478ecf5e0aaa25f0a74e` |
| `scripts/scalar_finite_window_history_check.py` | 55 | `dc2732e431c4c7427361004681136bc5fb89dbcff7c3c2bbaff58ac65b859b40` |
| `scripts/scalar_temporal_history_controls.py` | 122 | `105db461c83c9d522c9fb3cdc7786b68ef2506ccf3b3e7d126ecc6aad51bdf83` |
| `scripts/scalar_moving_history_controls.py` | 116 | `d968fd3ae26d278cde69e7a6a45d1e93211e17e6c8c97891359731aa51740739` |
| `scripts/scalar_force_energy_controls.py` | 116 | `f178ee6df06f7d391e5b9eae26cb4c665afcde458b9afb1fc9f8abe3683a2353` |

The primary imports only the three displayed scientific helpers. Its literal declared input closure is the canonical note plus those helpers, with a declared 120-second timeout. It returns and writes the three products through the requested output directory and hashes its own source and declared closure. No actual observation, fitted parameter, ancestor runner result, working-note result, or raw mission data enters these calculations. Python and the NumPy/SciPy/SymPy/mpmath numerical stack remain execution dependencies; the numerical comparisons are not interval certificates.

`CANONICAL_FINAL_BINDING_v1.json` mechanically binds the current sources, cache, products, mutation artifacts, adaptation records and checker. Its SHA-256 is `85118a487115a652b5d8560431117952478a8f7ee42cf27ee54cc39f6aec084e`. No science runner or mutation was executed by this reviewer during canonical confirmation.

## Fixed-point temporal functional

I previously derived the Fourier-space energy functional before opening the author's temporal implementation, preserved that precheck, and executed 58 separate controls. The canonical formulas agree with that independent derivation. With unitary spatial Fourier normalization `(2 pi)^(-3/2)` and time transform `W(omega)=integral w(s) exp(i omega s) ds`, the squared norm for a unit-direction, fixed-point gradient is

    C_mu^2 = (1/(6 pi^2)) integral_mu^infinity
             ((omega^2-mu^2)^(3/2)/omega) |W(omega)|^2 d omega.

For a real H1 weight, `C_mu^2 <= ||w'||_2^2/(6 pi)`, with equality when `mu=0`. The real-data constraint does not insert another factor of two: the Fourier Riesz data have the appropriate conjugate symmetry. At a fixed spatial point the vector Gram matrix is `C_mu^2 I`, so the full vector operator norm is also `C_mu`, not `sqrt(3) C_mu`. Finite-energy data are handled by continuous extension of the smeared functional; the result does not assert that every energy-class field has a pointwise gradient.

For the normalized triangular weight, `||w_T'||_2^2=2/T^3`, hence the massless fixed-point bound is `sqrt(2 E/(3 pi T^3))`. My prior checks used an asymmetric H1 weight, exact real-data Riesz/Gram calculations, smooth approximants and time-shift controls, rather than duplicating the author's triangular fixtures.

The rectangular finite-cutoff identity

    C_box,Lambda^2 = [Lambda/2 - sin(2 Lambda T)/(4T)]/(6 pi^2 T^2)

is correct. The canonical note retains specific finite witnesses and their contrasts with the triangular bound. Those witnesses are not an exhaustive negative result over all observation weights or theories. My prior Schwartz witnesses supplement that limited claim; no broader boundary theorem is promoted into the canonical conclusion.

The adjacent velocity-average identity is exact for the stated absolutely continuous velocity. It produces the triangular acceleration average, with a constant additive velocity bias cancelling. Under the separately stipulated leading count law, nonnegative absolute count-error budgets give `(dN_plus+dN_minus)/(|kappa f0| T^2)`. The final note explicitly supplies the nonnegative-budget interpretation requested in the temporal review. No actual ODF or mission processing chain has been shown to satisfy this model.

## Moving paths and changing direction

I previously derived the distributional two-integration-by-parts identity independently and executed 61 separate controls. The canonical version preserves its domain: stable flat frozen KG, nonnegative mass, initially smooth rapidly decreasing real data followed by energy completion, a compact continuous weight with BV derivative, a prescribed sufficiently smooth path with a uniform speed gap `delta=1-v_star>0`, bounded acceleration and jerk, and bounded first and second direction derivatives where needed.

For `psi=Omega s-k.x(s)` and `d=psi'/Omega`, the identity is

    integral w exp(-i psi)
      = -Omega^(-2) integral exp(-i psi)
        [w''/d^2 - 3 w' d'/d^3 - w d''/d^3 + 3 w (d')^2/d^4].

Here `w''` is a signed measure. Its jump atoms are essential. The derivative budgets give

    B = W2/delta^2 + 3 A W1/delta^3
        + J W0/delta^3 + 3 A^2 W0/delta^4,
    |I| <= min(W0, B/Omega^2).

The radial split and angular normalization give the fixed-projection envelope `C_path^2 <= 2 B^(3/2) W0^(1/2)/(9 pi^2)`. Both frequency signs are required. Their integrated contributions are related by spatial Fourier inversion; equality is not assumed at each individual wavevector. The same envelope controls the full vector norm by taking a supremum over unit directions, without an extra `sqrt(3)`. The actual moving-path Gram matrix need not be isotropic.

For a rotating direction, differentiating the amplitude gives `W2+2 N1 W1+N2 W0` in the first term and `W1+N1 W0` in the acceleration term. The loss of fixed angular isotropy gives the stated `2/(3 pi^2)` conservative constant. My separate controls included a signed asymmetric polygonal weight, an unexpanded integration-by-parts calculation, a cubic path, inversion to a phase coordinate, complex Fourier/Riesz tests and a pure geometric readout.

The exact scalar readout derivative is `d(n.v)/ds = n.a + n'.v`. Consequently the adjacent averages include a triangular geometric term. Omitting it is a real error; `N1 V` is the stated simple bound for normalized nonnegative triangular weights. None of this reconstructs an actual spacecraft worldline or observation direction. My earlier null-path gradient controls lie outside the theorem's speed-gap domain and do not establish a null-path result for the complete conformal force.

## Conditional conformal force and energy bridge

I checked the integrated force algebra directly and read the separate force review in full. That reviewer reports 253 independent controls derived before opening the author implementation and six targeted symbolic confirmations for canonical additions; these are separately attributed evidence, not controls executed by me.

For the ideal test-particle action with `L=-m A sqrt(1-v^2)` and `ell=log A`, differentiating the canonical momentum gives

    d(A gamma v)/ds = -A gamma^(-1) grad ell,
    a = -(1-v^2) [grad ell + v partial_s ell].

The time derivative is partial at fixed position. The inverse of `I+gamma^2 vv^T` is `I-vv^T`, which yields the displayed result and makes the indispensable time-force term explicit. The subsequent free-field force functional is a leading linearization along a supplied reference path, not the exact response of a self-consistent gravitating extended body.

The definitions `P=(1-v^2)n` and `R=(1-v^2)n.v`, their first and second derivative budgets, and `C_r=P_r+R_r` correctly bound the amplitudes `w(P.k/Omega +/- R)` for both Fourier signs. The resulting `L0,L1,L2` and `Bjet` give the displayed envelope `Cjet^2 <= 2 Bjet^(3/2) L0^(1/2)/(3 pi^2)`. Summing independently normalized modes under a single total mathematical energy budget gives `sqrt(2 q E_tot) Cjet`, where `q=sum alpha_j^2`; it is not a sum of separately maximal energies.

For the constant-velocity massless example I checked the added antiderivatives by the substitution `t=1-u z`. With `L=1-u^2`, they are

    integral_-1^1 (z-u)^2/(1-u z)^3 dz
        = [log((1+u)/(1-u))-2u]/u^3,
    integral_-1^1 (1-z^2)/(1-u z)^3 dz
        = [2u/L-log((1+u)/(1-u))]/u^3.

They give the note's parallel and transverse squared norms, including the rest limit `1/(3 pi T^3)`. In this complete conformal-force example both norms tend to zero as `|u|` approaches one because the speed factor and partial-time contribution matter. It would be incorrect to transfer the earlier pure-gradient null-path witness to this different functional.

The adopted quadratic kinetic normalization `-Q sum (partial h)^2` implies `E_phi,E=2 Q E_math,E`. Under a constant background conversion `x_J=A_b x_E, s_J=A_b s_E`, the relations `E_math,J=A_b E_math,E`, `Q_J=Q/A_b^2`, `E_phi,J=E_phi,E/A_b`, `mu_J=mu_E/A_b`, and `Cjet,J=A_b^(-3/2) Cjet,E` are consistent. Thus the conditional force bound transforms as an acceleration and can be written `sqrt(q E_phi,J/Q_J) Cjet,J`, or `sqrt(8 pi G_bare q E_phi,J) Cjet,J` with `G_bare=A_b^2/(8 pi Q)`.

These are natural-unit relations with the note's specified convention. They are not a license to insert SI joules and an SI value of G without restoring units. The separate review's presentation concern is resolved by the canonical unit restriction. The positive energy is the frozen local free-scalar energy, not an already established positive energy for the complete coupled gravity/matter system.

For the restated candidate branch, `0<k<1/3`, `a=(1-k)(1+3k)/4`, `Z=exp(2 sqrt(a) u)`, `F=1+sigma Z`, `J=1+(1-3a)sigma Z`, `K_uu=J/F^2`, and `A^2=(1+sigma)Z/F` give `partial_u log A=sqrt(a)/F` and `q=a/J`. Since `1/3-a=(1-3k)^2/12` and `J>1`, the stated conditional ceiling `0<q<1/3` follows. Using a measured gravitational value additionally requires the same-background relation `G_meas=G_bare(1+q_geom)` and `q_geom>=0`. Only under those conditions does `G_bare q<=G_meas/3` follow. No environment, coupling scale or actual energy budget is inferred by this algebra.

## Adaptation, execution and preserved failures

The AST and complete diff comparisons are recorded in `CANONICAL_CORRESPONDENCE_v2.json`, SHA-256 `7ed1ebe81b8e9e7ed83d696fb0a5381427c793c6cd38f0aa7a1cfe68b5fa0e45`. The temporal and moving scientific bodies agree with their reviewed working implementations after wrapper changes. The force implementation preserves its calculations, adds eight angular-antiderivative comparisons, and uses a shared exact mode-energy function in both the random-budget and aligned-attainment fixtures. The functions return products rather than writing working files. The old working force calculation has 49 controls; the final canonical helper has 57. I checked the affected additions and repair, not a second copy of every unchanged calculation.

An initial correspondence pass encountered a stale force hash while the author was adding the eight controls. Its partial result and technical identity failure remain in `CANONICAL_CORRESPONDENCE_ATTEMPT_v1.json`; the subsequent comparison binds the corrected final executable. This was concurrent source movement, not a failed mathematical assertion. The later wording-only note change is separately preserved and bound; the older correspondence record is not restamped.

The first mutation pass had 28 assertion rejections and one genuine survivor: removing factor two from the random shared-mode budget did not fail those finite samples, while the attainment fixture evaluated a separately written formula. The author repaired this test weakness by defining `mode_energy_bound(alpha,energies)` and using it in both places. The mathematical bound itself did not change. Eleven force-family mutations were rerun on the repaired source; 18 temporal/moving cases were reused because their source bytes were unchanged. The final record has 29 actual `AssertionError` rejections. I reconstructed every final mutant from its stated one-occurrence source edit, checked its stored bytes, read its stored error identity, and matched it to the original v1/v2 receipt. The repaired shared-budget mutant now fails `joint_mode_budget_attainment`. None of these observations implies mutation completeness or a formal correctness proof.

The original survivor is retained in `HISTORY_MUTATIONS_v1.json`; the targeted rerun is `HISTORY_MUTATIONS_v2.json`; their final combination is `HISTORY_MUTATIONS_FINAL_v1.json`, SHA-256 `4f0e777bba86f11a86927dce318355d5973f0abbaf8672e5197cec8b6fe2bfc3`. The historical repair receipt's pending verification text is superseded by those separately preserved final results, not silently edited.

The author executed the canonical runner and refreshed its cache after the wording-only input hash changed. The final cache has exit 0, status `ok`, declared cap 120 seconds, reported elapsed 1.38 seconds and empty stderr. Its SHA-256 is `a512eae1939d384402fd5ec633d0b9238d66733fc7a938d4895d5a1dad05ed5e`. I independently reconstructed its declared-input fingerprint as `2fbab4a4f5dbdfcd344f2f45154bccf6693fa889aaa4ef131ce8acd764b3303d`, checked its stdout against the summary, and verified all five source hashes. The three products are byte-identical to those preceding the wording refresh. Their recorded counts equal both their check-list lengths and their distinct check-name counts: 70 temporal, 133 moving, 57 force/energy, 260 total.

| Canonical product | SHA-256 |
| --- | --- |
| `outputs/scalar_finite_window_history/temporal.json` | `5f735c2c9b3210301686b9e47438ccdf5007f7f69095be0086d693ca13e54b1c` |
| `outputs/scalar_finite_window_history/moving.json` | `343e521a5b4fa81ee0d6c5c951d749aa6c3a81908786d90b6176f3dcf4902811` |
| `outputs/scalar_finite_window_history/force_energy.json` | `e268f5779357059665ac9d6cc8ba806c298067f6bb2d55ca207c2cfa29a548a9` |
| `outputs/scalar_finite_window_history/summary.json` | `c6a0fc8a2b3952d3837a32af5bb984e8aab35d89f8a9ca3be2dd80c2ba3c2177` |

The 260 author controls are distinct from this reviewer's previously executed 58+61 independent controls and from the separate force reviewer's 253+6 controls. No count is an empirical sample size or an independent-test data set. I did not rerun the canonical runner, mutations, or unchanged independent programs during this binding.

## Independent evidence and remaining boundary

The following reports were read and their identities checked. Paths are relative to this campaign's `finite_time_environment` directory. Associated scripts, prechecks and results are transitively identified in these reports and in the final identity JSON.

| Evidence | SHA-256 |
| --- | --- |
| `independent_temporal_v1/TEMPORAL_REVIEW_v1.md` | `a1eff40d8c53d2d0fd37d4aa9e2e1e6f0f8ab61722ead80ad43db30effd07dd5` |
| `independent_temporal_v1/INDEPENDENT_TEMPORAL_RESULTS_v1.json` | `dc99933002abdf9a9717a70f8d03371b4ec07c3a6979eaec9757d8d4394e12e1` |
| `independent_moving_v1/MOVING_REVIEW_v1.md` | `e6562c3c4e30749f5d524064f532e8c1bc018511416a291be231426a6327eb3c` |
| `independent_moving_v1/INDEPENDENT_MOVING_RESULTS_v1.json` | `f61a79f3b81fe34c1f05797fe28a117f319cea8c67efc7560c6aa5ab3de1dc7b` |
| `independent_force_bridge_v1/REVIEW_FORCE_ENERGY_BRIDGE_v1.md` | `6243e8b238304bd4a9f791a5cff8db1766df6132599d424216f4c13ef42a7d15` |
| `independent_force_bridge_v1/CANONICAL_FORCE_ENERGY_CONFIRMATION_v1.md` | `8a4adfd9e1559679b8af5864cd5ff968e1031057b3ddc739e59c01ae5b7d305a` |
| `independent_force_bridge_v1/CANONICAL_ALGEBRA_CONTROLS_v1.json` | `60bbcc11e9ee6cb1b68ba65c6897ff1def9bf9a5a6b7d56e49b66aaa66cf2b87` |

The force review binds the earlier `6b9610...` note and the final unchanged force helper. This reviewer independently read the entire subsequent wording diff and binds `059e1f...`; the peer report is not represented as having reviewed bytes it did not name.

The remaining physical imports are material: the action and candidate branch, stable frozen free operator, separation of homogeneous data from source forcing, prescribed regular subluminal path, direction and weight budgets, linearization and nonlinear remainder control, ideal test-particle coupling, constant-background frame conversion, quantitative physical scalar-energy input, environment-specific gravitational normalization, and actual clock/ray/count calibration. No supplied selector is counted as a derivation, and finite energy is not counted as a measured upper budget. A local positive free-energy estimate does not fix the initial state or solve the full sourced coupled problem.

The canonical note accurately keeps its actual current surface status at conditional support. The final summary reports zero measured-gravity tests and zero fitted parameters. The source proof is self-contained for the supplied formulas; provenance notes are context for those supplied premises, not imported retained-grade authority or ancestor-output evidence. The graph-manifest delta, Git index, publication tree, current PR heads and combined landing state have not been reviewed in this five-source confirmation; they require a separately frozen delivery binding if requested.

`CANONICAL_ORIGINAL_DISPOSITIONS_v1.json` supplies reviewer-owned inclusion mappings for exactly these five frozen science postimages. Inclusion means this scoped source coverage and identity mapping, not an audit verdict or empirical validation. No source, state, lock, branch, index or external message was changed by this review.
