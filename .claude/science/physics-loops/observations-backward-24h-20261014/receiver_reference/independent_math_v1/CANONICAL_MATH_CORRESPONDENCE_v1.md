# M10 final canonical mathematical correspondence v1

The five canonical files identified below agree with the independently derived finite-voltage geometry within their stated conditional domain. No unresolved mathematical or critical source-correspondence discrepancy was identified at these exact bytes. The original working estimator had a real frequency/amplitude alias defect; that finding is preserved, and the canonical correction is checked here. The new competing-peak disclosure is consistent with a local estimator and prevents a global-frequency interpretation.

This is a focused post-exposure mathematical and source check, not a formal audit, empirical validation, cache/product attestation or publication approval. Root remains scientific author. The historical receiver calibration is not independently derived here. This report supplements the preserved pre-exposure proof, controls and original working-source finding.

## Exact source and read scope

All five files were read completely. Initial full-source reading was followed by complete affected-diff inspection. Before this report was written, all current files matched the hashes below and their exact snapshots in this directory. The final note differs from the prior d751b57e snapshot only by clarifying that all matched endpoint variants and selected decoded quality/slip fields are retained, rather than every ATDF field. That exact delta was read and saved. It agrees with the explicit `wanted` field subset in the receiver-reference helper; no equation or code changed.

| Repository-relative source | Bytes | SHA256 |
|---|---:|---|
| docs/CASSINI_CARRIER_REFERENCE_FEASIBILITY_BOUNDED_THEOREM_NOTE_2026-10-15.md | 18934 | `79bcdf128d8b0570cc248576ddda09d5f50edbf9851fb9dad0cd920a24f68cd9` |
| scripts/cassini_carrier_estimator.py | 7933 | `314724bf119f71a0bfe678ec5aa5e094efca251a24d871ac23957e80af18899f` |
| scripts/cassini_carrier_geometry_controls.py | 4839 | `b1b25068e1b05487049a1f5e072de329139315816c58db4ec3d96e02b6a74232` |
| scripts/cassini_receiver_reference.py | 6752 | `72eec75703d5577dc97e20a5e1c96d7e46bca6d1d94c8874b1dd5ec02359c10c` |
| scripts/cassini_carrier_reference_check.py | 5914 | `58a388ebc2a288d5535fa33a0dcb29bfc3b3dbe5e16ce3c22669211a0c7697b4` |

The complete primary was read for its assertions, mathematical integration, declared dependencies, acquisition boundary and hashing structure. It declares 13 source/protocol inputs besides its own source identity. I did not extend this review into a new read of all imported decoders, manifests, raw products or external historical documents. No network source was accessed. Their empirical applicability is outside this check.

The first attempt to freeze this report stopped at its hash guard because root concurrently made the endpoint-wording correction. No report or identity had yet been created. `CANONICAL_NOTE_WORDING_RECEIPT_v1.json` preserves this event, the old/new hashes and the reason. The revised snapshot is `CANONICAL_FINAL_v2_CASSINI_CARRIER_REFERENCE_FEASIBILITY_BOUNDED_THEOREM_NOTE_2026-10-15.md`; the old snapshot remains unchanged. The report therefore binds the current note directly, without silently substituting bytes beneath an earlier final review.

## Independent evidence and exposure

`PRECHECK_v1.md`, SHA256 `d2ea6c4e74ace3104f74f5f2b1930f53bfeff07dfdaafd1e1bb7229a97bc9b4a`, and `INDEPENDENT_REVIEW_v1.md`, SHA256 `7856e3180052664bc56036e9a8aa9f9bcf8d32ea51d34d1184d053b91e75c99a`, were frozen before opening an M10 author derivation or implementation. Root had supplied candidate target formulas. Independence concerns separately deriving them and writing controls before author-source exposure, not blindness to the proposed answer.

The separate implementation `independent_receiver_controls_v2.py`, SHA256 `3f6ade4a7a621d98b51b7d3271532fb474061d131213407de70f0bc59e98a801`, passed 76 exact synthetic checks. Results SHA256 is `3ed6bf25845a99beae30880711490de4ade799185c8057aa81373d7cc530764b`. Those are mathematical fixtures, not independent observation tests. No author code was imported or executed by that implementation.

The original v1 run failed on a wrong handwritten expected answer in an auxiliary interval-distance fixture. For intervals [0,1], [3,4], [5,6], the algorithm correctly returned minimum 8 at amplitude 3. Version 2 corrected the expectation and added a distinct interior-minimum fixture; the algorithm and proof did not change. Failed source, stdout/stderr, execution record and exact repair remain untouched. This was neither a suppressed failure nor an empirical physics result.

Only after that freeze did I read the complete working `carrier_development_v1.py`, SHA256 `feadce5547ce028d1e0e6ce46ffe9c23b953ec6e945ec0db4d11696ff0fd3f83`. Its exact snapshot and `AUTHOR_WORKING_CORRESPONDENCE_v1.md` preserve the resulting finding. Every canonical inspection in this report is post-exposure. Exposure receipts, full snapshots, the estimator adaptation diff and narrow alias/phase witnesses remain separately identified.

## Projection, discrepancy and phase

For N>=1, the template has squared norm N. With the stated Hermitian convention, the residual at `c_hat=u_f^*z/N` is orthogonal to `u_f`, giving exactly

`||z-c*u_f||² = E(f) + N|c-c_hat|²`.

A supplied B>=0 therefore gives the exact frequency-feasibility condition `E(f)<=B²` when zero amplitude is allowed, and the disk radius `sqrt((B²-E)/N)`. Removing the origin is the correct additional condition for a nonzero carrier; a singleton zero disk supplies none. The boundary B²=||z||² with zero correlation cannot be counted as a nonzero-carrier solution. N=1, repeated times and exact sampled aliases can prevent uniqueness even with zero error.

A calibrated lower amplitude gives the correct minimum `E+N*max(0,a_min-|c_hat|)²`. This supplier is not inferred from the fit. At a true frequency, residual measures only the discrepancy orthogonal to the template; its parallel component is absorbed in fitted amplitude. Thus fitted residual is required discrepancy, not an upper physical error bound. The constructive choice `eta=z-c*u_f` reproduces the same samples for arbitrary f and nonzero c when error is unrestricted. This is a class-specific nonidentification result, not a no-go after a physical error class, waveform dynamics or calibration is supplied.

A bound B_phys before ideal quantization yields the outer center-vector bound `B_phys+sqrt(2N)` by the triangle inequality. The final note correctly states that this ball loses cell geometry and is not an exact physical-plus-quantizer equivalence. It does not assume independence of physical error and quantizer displacement.

For nonzero c_hat and rho<|c_hat|, the origin-to-disk tangent gives the sharp `asin(rho/|c_hat|)` phase bound. At rho=|c_hat|>0, nonzero points fill an open semicircle; limiting tangent directions occur only at zero amplitude and are not attained by a nonzero point. For rho>|c_hat| every phase is present. At zero center, positive radius permits all phases, while zero radius permits only zero amplitude with undefined phase.

The final note now uses `|Arg(c/c_hat)|`, the relative circular separation, rather than subtracting principal arguments. This resolves the branch-cut witness c_hat=-1, c=-1-0.1i, rho=1/4: circular separation is small although separately reported principal arguments differ by more than six radians. The final geometry source contains that witness, and `PHASE_BRANCH_WITNESS_v1.json` remains unchanged. These are phase statements about candidate amplitude at the chosen time origin, not automatically physical endpoint phases or integer cycle lifts.

## Exact cells and the restricted negative result

The constant-modulus center-distance minimum follows from the reverse triangle inequality and minimization in r>=0. It is `S-(sum r_n)²/N`. Integer ceilings upper-bound the sum of radii, giving the weaker lower bound `S-C²/N`. This lower bound may be negative; it is never treated as a nonnegative energy estimate without qualification.

The helper uses exact Python integer squares, integer-square-root ceilings, the sum C and the strict condition `N*S-C*C>2*N*N`. Any point in the closed halfwidth-one cells is within squared distance 2N of the centers. The strict condition consequently excludes every closed-cell constant-modulus waveform, including any constant-amplitude tone. Floors are invalid, and equality cannot be rejected; both orientation/boundary cases were checked independently. The synthetic centers (1+i,1001+i) give S=1002004, C=1004 and numerator 995992, which is the final source value. Root's earlier incorrect fixture expectation is not reclassified as a successful run here.

The squared radius endpoints are correct. The magnitude image of a connected compact square is its complete closed interval between those extrema. Intersection of the intervals is necessary and sufficient for arbitrary independent sample phases with a common modulus. It is only necessary for a coherent tone, whose phases must follow the same frequency progression. The final note explicitly restricts the iff statement to closed enclosures: half-open actual cells can exclude an equality-only boundary solution, while strict closed-cell rejection is safe for every subset.

Root did not adopt the optional stronger active-set distance extension in my independent proof as a new canonical claim. This report does not add it. The declared exact-cell rejection concerns constant total analog modulus with ideal quantization alone; it cannot distinguish modulation, other signals, gain, propagation or noise and cannot exclude a carrier mixed with unrestricted discrepancy.

## Correlation, periodic covering and estimator repair

The termwise Lipschitz proof is correct for the time coordinates assigned to the complex correlation. A time shift rephases that correlation. A centered derivative constant is valid for the rephased complex correlation and original magnitude differences, but not automatically for uncentered complex differences. The final note explicitly preserves this qualification.

For nominal uniformly sampled times, the correlation magnitude is periodic in frequency with period f_s. The centered complex correlation may acquire a phase at the seam, which does not alter the magnitude. A complete grid on one such period has circular magnitude covering radius f_s/(2*grid_size). Combining the nearest grid point with the Lipschitz bound gives the stated maximum-magnitude enclosure. The implementation's additional Cauchy upper bound `sqrt(N*energy)` is valid. Arbitrary times do not make a finite FFT band cover the whole real axis.

The floating FFT, derivative evaluation and residual subtraction are not outward interval arithmetic. The final note correctly calls `numerical_global_residual_lower_bound` a diagnostic evaluation of an analytic inequality rather than a numerical certificate. It does not assert the bounded local refinement finds the global peak. Source correspondence is in the declared positive-f_s, nonzero-energy, N=1000 and grid_size=16000 domain. A generic grid_size<N call truncates samples in the FFT and lies outside that all-samples grid argument.

The working estimator computed amplitude at the unwrapped optimizer frequency and then returned a wrapped frequency with that amplitude unchanged. At centered times `(n-(N-1)/2)/f_s`, an m*f_s shift changes the template by `(-1)^(m*(N-1))`. Even N with odd m requires a corresponding phase change. The preserved exact two-sample alias witness gives squared returned-waveform discrepancy 8 instead of 0, although frequency and power checks can look correct.

The final canonical estimator wraps f before recomputing correlation, complex amplitude and direct residual, and returns that same f. The known-tone controls reconstruct the complete waveform from the returned pair, including both +/-499.98 Hz seam examples. This closes the actual source defect algebraically. I did not rerun the author's FFT/optimizer aggregate. The complete working-to-canonical estimator adaptation was inspected; the other differences are root-path adjustment, timeout declaration, callable output wrapper, summary naming and CLI parameters. The original working bytes and finding remain unchanged; their old amplitude outputs are not relabeled correct.

## Reference arithmetic and physical imports

The final reference helper uses the declared archived P coefficients in

`P(1+delta)-P(delta)=P2+P3*(1+2*delta)+P4*(1+3*delta+3*delta²)`.

P1 cancels. Independent expansion and rational fixtures at delta=0, 1/2000 and -3/7 match this expression without importing author code. The implementation converts stored values to Fractions and performs the large nominal subtraction before adding fitted floating frequency. Separately rounded F and P fields need not obey the ideal derivative relations exactly: `Fraction(.1/3)` differs from `Fraction(.1)/3`. The added source witness detects this. The original F-based working route remains a preserved protocol mismatch. The empirical reviewer found it; this reviewer checked the mathematical repair.

The midpoint-held versus continuously integrated quadratic-frequency difference `F3*h³/12` is correct with the stated sign. It demonstrates a genuine model distinction; it does not reconstruct actual hardware phase loading.

The exact arithmetic `880/221=(11/3)*(240/221)` and `(880/221)*2117064000=1863016320000/221` is correct. So is `mean f_R=reference-D` under the supplied counter equation. The primary now explicitly asserts these reference values. I checked arithmetic and source consistency, not historical selection of the Moyer branch, station and band identities, field decoding, sign applicability or actual physical receiver transfer. They remain instrument premises requiring their own external-source and data evidence. No transmitter-ramp substitution, extra multiplier, physical error budget or scalar response is derived here.

The note retains limitations on counter lifts, resets/slips, timestamp/phase transfer, alternate phase arguments, phase-loading dynamics and replacement of an interval phase increment by a fitted slope. The final selected-fields wording accurately matches the helper's explicit field subset. Small development residuals do not retire these imports.

## Control accounting, empirical boundary and conclusion

Static source inspection gives 42 geometry checks, 9 carrier control groups and 12 development checks: 63 in the primary total. This is a source count, not an execution claim by this reviewer. I did not run the canonical aggregate, read a final source-bound cache, or bind regenerated empirical ledgers. The independently executed 76 exact synthetic checks are separate evidence. Neither count is an independent empirical gravity-test count.

The primary checks registered block counts, flags, ideal-cell exclusions, interval matching, fixed reference, slip diagnostics, dependent storage agreement, sign/timing alternatives and zero fitted bias/time shift. I checked them as source conditions. Whether the final raw-data execution satisfies them and whether outputs/cache bind the final bytes remain author/empirical obligations. The acquisition branch returns before scientific execution; the ordinary branch uses local pinned inputs. Neither branch was executed here.

The complete final note discloses the Ka second-49112 competing peak, the 1199/1200 frequency comparison, both candidates and the unresolved physical choice. I did not recompute the raw block, read a new empirical ledger or independently verify those numeric observations. The disclosure is logically appropriate: a correct least-squares identity does not certify the implemented local search as globally optimal, and lower residual alone does not identify a physical carrier. No tolerance relaxation or per-row override is presented as independent agreement. The integer-cell formulas do not depend on the chosen frequency, but this logical separation is not an independent verification of all 1200 actual integer certificates. The stated all-X agreement and unchanged X comparison table also remain empirical claims outside this check.

The N1–N8 boundary remains finite and constructive: declared sampled tone/constant-modulus and discrepancy domains, explicit cell premises, unrestricted-error countermodels, a positive theorem for a supplied bound, and routes reopened by calibrated references or waveform dynamics. It makes no no-go claim for full radio tracking or the revised scalar theory. The useful result is an exact feasible set into which justified information can enter and an exact rejection criterion for an overly restrictive total-voltage class. It does not choose a physical error radius, field state, scalar action, scale or environment.

All scoped mathematical findings have concrete dispositions: canonical alias coherence repaired; relative phase text and branch-cut witness corrected; B>=0 and closed-cell boundaries stated; archived P used without assuming exact rounded P/F equivalence; real local-search discrepancy preserved. No further mathematical/source change is requested at these hashes. Final empirical/cache binding and publication decisions remain outside this report.

The accompanying identity pins the five sources, snapshots, this report and earlier local evidence. All writes were confined to this reviewer directory. No raw observations, shared source/state/lock/index/Git files or another agent's work were changed. No formal verdict or new scientific authority is asserted.
