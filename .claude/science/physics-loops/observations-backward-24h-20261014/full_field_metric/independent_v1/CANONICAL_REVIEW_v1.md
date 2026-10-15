# M20 focused canonical mathematical source correspondence

This is a post-exposure source comparison with the independently frozen derivation and 34 exact controls. It is not a formal audit, publication approval, fresh independent empirical test, or independent rerun of the author's full-field ODE controls. The original proof, exact results, source snapshots, and freeze remain unchanged.

I read the complete new canonical note, complete mathematical helper, complete primary runner, and complete fixed protocol frozen in `CANONICAL_EXPOSURE_v1.json`. Relevant inherited action and metric context was already read and frozen before deriving the new envelope. No other new parent working source was used as an independent oracle.

## Mathematical and physical correspondence

The supplied Jordan action agrees with the inherited full action after division by f0. In particular the two transverse kinetic coefficients include `(1+s) z²`, the transverse potential factors include `(s+z²)²/(1+s)`, and the potential's y coefficient has the required factor 2/3. The strictly positive parameter domain makes both potential coefficients positive and gives the nonzero logarithmic-derivative gap `2k/(a z)`.

The three metric equations and null differences match the independent derivation. The angular-time relation determines only the logarithmic derivative of X and retains a trial amplitude C. The transverse kinetic remainder T is the *physical* radial gradient energy divided by f0 and includes B. The exact z variation therefore contains `-2T/z`. The simplified residual `LX/(lambda z)+zR-XH/z-P0,z` is equivalent. This also checks the signs, base-potential derivative, and the important below-one regulator qualification: the latter is retained exactly, so the envelope does not require z≥1.

The two potential remainders prove the stated necessary inequalities. Their invertible two-by-two algebra gives the two squares for fixed trials, including the zero-Delta case without division by Delta. The field-square derivative formula has coefficients 1/9 and 1/12 as required. The note correctly distinguishes an isolated amplitude zero from a zero derivative, and retains smooth-root/regularity obligations. The explicit transverse Euler equations include total radial kinetic-coefficient derivatives and the cross-field kinetic derivatives. A single Bianchi contraction does not establish both equations. The note does not assert reconstruction sufficiency, unique parameters, existence, stability, sector selection, preparation, a global solution, or actual observation agreement.

The chart and supplier limits are explicit: static radial material vacuum, calibrated areal radius, positive lapse and B, nonzero angular denominator, positive X−s, supplied candidate action/parameters, an unknown normalization, and derivatives through N''' and B''. No action normalization is identified with measured Newton G. C, k, Hv and nu remain trial inputs. Ordinary finite data do not become an exact metric interval or an error certificate. No material environment is silently converted to vacuum.

I found no material equation, normalization, proof-domain, or overclaim discrepancy in this frozen canonical argument.

## Implementation and separate correspondence checks

The complete helper's `metric_parts` differentiates the same Einstein components and angular denominator. `invert` receives metric jets, trial k/Hv/nu, and trial X; it does not receive x, y or their derivatives. Its first/second z derivatives, T, Delta, E, envelope slopes and square inversion match the independently derived formulas. The inversion returns diagnostic quantities; it is not a sufficient-solution admission API. In particular negative reconstructed shares must be interpreted through the stated inequalities, not silently treated as a physical field solution.

The finite-real and positive-domain guards precede the scalar square root and geometric inversion. The new domain controls are consistent with those guards. The currently frozen protocol's 50 digits and `1e-35` tolerance match the helper's explicit constants. The helper does not promise general protocol-schema validation or validated rounding enclosures; changing those metadata alone would not change its hard-coded numerical precision/tolerance.

I also checked the full forward construction by equations and source reading. For the explicitly specified auxiliary Einstein metric `gE=X gJ`, the action has half-normalized kinetic coefficients `hzz=2/(lambda X)+6z²/X²`, `hxx=2qx/X`, `hyy=2qy/X`, and potential P/X². The Einstein radial mass/lapse equations, diagonal-field-space connection, and potential-force normalization in `rhs` match that action. The local Taylor recursion obtains derivatives of the autonomous/nonautonomous system through the needed order. It is not a numerical integration of a global spacetime. The Jordan areal coordinate `r=R/sqrt(X)`, lapse logarithm shift, radial B transformation, and derivative-chain formulas match this conformal map; the two case controls explicitly require a positive radial Jacobian. The original-equation residual code includes all three metric components and all three scalar equations, including the z-only curvature term and cross-field kinetic variations. This is a source/derivation check of the generator, not an independently executed forward solution.

For a genuinely separate implementation comparison, `canonical_correspondence_checks_v1.py` extracts only the frozen canonical functions `constants`, `replaced`, `jordan`, `einstein`, `metric_parts`, and `invert` into an isolated namespace. It neither imports the helper as a module nor invokes `rhs`, `local_jets`, `controls`, or the runner. An independently differentiated symbolic metric supplies two exact rational input jets, one with z=3/4 and one with z=7/5. An independently assembled oracle uses the LX residual, while the implementation uses the Lz residual. It compares all twelve inverse outputs and the complete relevant Jordan/Einstein coefficient normalization. These supplied synthetic metrics are algebra fixtures, not claimed candidate solutions or accepted observations. Eleven finite/positive/chart refusals and the fixed protocol's precision/tolerance correspondence are also checked.

The resulting **50 post-exposure checks pass, zero fail**: 38 formula/coefficient comparisons, 11 domain probes, and one protocol/source-constant check. The largest scaled discrepancy is approximately `2.55026e-50`, below the separately fixed `1e-43` comparison tolerance at 50-digit arithmetic. Those numerical comparisons are not interval certificates and are distinct from the original 34 pre-exposure exact checks. No tolerance changed and no failed run was suppressed.

The runner loads only its declared fixed synthetic protocol and helper scientifically, hashes its five declared premise/source inputs, writes paired source-bound products, and reports conditional-support/zero empirical tests. It does not read this review or its independent results as computational evidence. The note's earlier 24-control working execution is an author-reported result; I did not rerun or independently bind that historical execution here. The canonical helper statically adds seven refusal controls to those two twelve-control cases, but this report does not claim a successful canonical aggregate or cache execution that was not supplied/read.

## Exact identities and source preservation

Complete new sources reviewed:

| Source | SHA-256 |
|---|---|
| Canonical full-field note | `493130222fb63c5fef6d21f14ab254288b0fe81b1d0e5e767cf28d98e77d516a` |
| `scalar_full_field_metric.py` | `63ac20cfe19f3e0e681ace4714434f58fef50c82fe5ad95a282d0a9e79268a21` |
| `scalar_full_field_metric_check.py` | `f859afe954b42f75a7a97ef3e51af4ef1761992fbaba0bf5310d518b70078180` |
| `PROTOCOL_v1.json` | `5254a684a8cba9a3ec0787723a9be4663f2e6b04dccfdf70d9e296c4a055d3d4` |

The inherited action note remains `669bae27fc3d80ef82852a4e21068c8667ecf8c68a30e61b8a05cc9da5288bc6`; the inherited M19 note remains `b5b712b90bc4ed62cfbbb11ffded922ce83958b269afc14fcb2ec6322d0d5a00`, as frozen before this block. Those entire-file identities are checked, but the fresh mathematical reading of them is limited to the action/metric sections recorded in the pre-exposure manifest. This is not a new complete review of every inherited extension or its publication history.

All four new live source files matched their frozen exposure copies at the closing check. Every original independent artifact still matches `INDEPENDENT_FREEZE_v1.json`. Detailed correspondence results and code identities are retained separately in `CANONICAL_CORRESPONDENCE_RESULTS_v1.json` and this report's identity receipt. Canonical execution/cache, mutation outcomes, graph/PR integration, and later edits are outside this source-bound assessment until separately supplied. No shared/canonical source, Git state, campaign state, process ownership, or model setting was modified.
