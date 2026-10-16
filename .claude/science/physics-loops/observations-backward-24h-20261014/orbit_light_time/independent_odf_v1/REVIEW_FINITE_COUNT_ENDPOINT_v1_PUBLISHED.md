**Focused check of station-clock phase and finite-count endpoint response**

The finite-count identities and stated remainder bound hold under the note's declared phase-transfer, clock-map and coverage hypotheses. The checked code agrees with independent exact calculations. I found and the author corrected one introductory scope error: the archived records were called transmitter ramps before their electronics role had been established. No material mathematical error remains in this focused check. This is an independent derivation/code check, not a formal audit, landing review, mission-mode selection or empirical gravity result.

The final note bound here is `FINITE_COUNT_STATION_TIME_DERIVATION_v1.md`, SHA-256 `74ea5a1bd3304b6bd99b5f35ee6e2f67ba6875c4b2fa91d6160e9eb5a9a06bd1`, preserved as `AUTHOR_FINITE_COUNT_CORRECTED_v1.md`. The checked runner is `finite_count_endpoint_check_v1.py`, SHA-256 `29eb5bf31ebb81b2538679ea66872c1f79eed3f24b311c203166e08fbcc6d955`. Its ramp helper remains SHA-256 `146e7d4cea4998cebae09883e8746fcf8e766c4c8346c60772fcbbfbc72a8acc`, and the helper's inventory dependency is `2dfc9339ca5a962ade99df5a3270e95cff3e97501ce32f198ce51681fcb2d9c8`. Exact initial sources and a rerun are retained in `finite_count_frozen_v1/`.

I read the complete note and runner, the interacting earlier coherent-phase premises, and the relevant local primary-source excerpts from Moyer sections 13.2.4, 13.2.6 and 13.3.2.2. The current note differs from the frozen original SHA-256 `01d7bbf2133f293cdcb41a78ddedb980a8dd24f760e3b0fcff1906416d695f41` by exactly one phrase: “transmitter-ramp records” became “frequency-ramp records.” A byte-level comparison confirmed no formula or other text changed. The original remains preserved, and the unchanged mathematical checks therefore apply to the final note.

Let transmitted phase have derivative f with respect to station time. Applying the chain rule to the coherent phase law gives

    dTheta_received/ds3 = k f(s1) (g1*w1)/(g3*w3) * dt1/dt3.

Integrating in reception station time yields the endpoint phase difference k[F(b)-F(a)]. The proper/station factors are present in the endpoint map and the frequency definition; a second clock multiplier would change the result. I checked this using separately chosen nonlinear coordinate-to-proper and proper-to-station functions, not just the author's total station-time map. Exact symbolic integration agrees with endpoint phase. Additional proper, station and combined multipliers each fail an explicit nondegenerate example.

This is covariance of phase bookkeeping, not absence of physical clock effects, invariance of numerical frequency under arbitrary clock rescaling, or cancellation of scalar effects from the complete measurement. The causal, uniquely chosen retarded map, clock rates, electronics endpoints and calibrated transmitted phase remain inputs. For a physical count interval the maps and supported endpoint intervals must also have the appropriate temporal ordering. The algebra itself can be written with oriented integrals, but the supplied ramp integrator correctly rejects nonpositive forward intervals.

For fixed R, k and positive reception duration T, write E_x(delta)=F(x)-F(x-delta). Direct subtraction gives Delta D=k[E_b(delta_e)-E_a(delta_s)]/T. This fixes both endpoint signs and retains oriented negative shifts. For either sign of delta,

    E_x(delta)-f(x)*delta = integral_0^delta [f(x-u)-f(x)] du.

A Lipschitz constant on the full closed displacement interval bounds this by L*delta^2/2 in magnitude. Applying the triangle inequality yields exactly the stated two-endpoint bound. For an affine frequency, the single-endpoint remainder is -r*delta^2/2, giving the note's signed difference of endpoint remainders. No derivative of the clock map is being neglected: endpoint displacements already describe the specified map change. Changes to the reference, transmitted phase function, k or reception interval require their own terms and are excluded from this fixed-input comparison.

The independent computation uses explicit polynomial primitives, rational values and a nondifferentiable but Lipschitz frequency f(s)=10+2*abs(s). It covers positive, negative and zero displacements; signed and zero k; constant, affine, quadratic, cubic and quartic frequencies; and continuous kink crossings. The derivative bounds for the polynomials are analytic triangle bounds over the whole interval, not values sampled on a grid. No author helper is imported in this computation.

The jump counterexample is correct. With frequency 10 before zero and 30 after zero, integration from -0.1 to 0.1 yields 4 cycles, while the endpoint linear approximation gives 6. Zero slopes on the segments cannot imply a zero remainder across the discontinuity. Exact piecewise phase integration remains meaningful across a contiguous jump, while uncovered gaps must be rejected. Neither a finite number of stored decimals nor agreement of an affine integrator establishes a physical clock/error budget.

The common/differential decomposition is exact algebra. A common endpoint displacement cancels exactly for constant frequency. On a single affine ramp its exact count response is k*r*(b-a)*delta/T, so it generally survives. A simultaneous translation of the clock origin, endpoints and ramp ledger preserves phase; moving endpoints against a fixed ledger is a different operation. The independent checks distinguish these operations and also confirm that numerical frequency changes under nonlinear clock relabeling even though phase is preserved.

Reference cancellation is confined to comparisons with the same reference phase. The transformation (P,R) -> (P+h,R+k*h) preserves the declared D, whereas changing R alone does not. This exhibits underidentification if every sample is allowed its own arbitrary unknown reference. It is not a proof against calibrated tracking or a claim that references shared across a physical model can always absorb arbitrary changes.

The conventional form is consistent with [Moyer's primary formulation](https://descanso.jpl.nasa.gov/monograph/series2/Descanso2_all.pdf), particularly Eq. 13-50 and the endpoint/media relations in Eqs. 13-52 through 13-58. There the receiver reference may have a separate multiplier and uses receiver electronics times, while transmitted phase uses transmitter electronics times; the note leaves that distinction inside R rather than silently equating it with k. The accessed PDF SHA-256 is `23b302fd2b47b6adfadac4c2b01301396ebc54bcefb269cf7126270a3d5d87ce`, and the extracted frequency/Doppler text is `6094c62287a78fd3f33228cc48d6989b02ab80a2efa63d77ddf01a8f01279ff8`. Agreement with that conditional form does not select the actual June 2002 archive-processing convention. This check does not adopt a later ODF definition.

The wording correction is supported directly by the exposed product label, which describes its ramp groups as tuning receivers or transmitters. All 69 records being at sky level does not establish which electronics role applies to this observation. The final wording now preserves this distinction. The separate ramp check establishes only the stated nominal receiver coverage. No new raw track or ATDF data was opened for this finite-count check.

Evidence:

| File | SHA-256 | Result and scope |
| --- | --- | --- |
| `check_finite_count_independent_v1.py` | `d3fe5e82bc70f69f9de7770c96bd114c68dc7dedd6291f9f6c4d6fb2f4391e7d` | Independent symbolic and rational path |
| `FINITE_COUNT_INDEPENDENT_RESULTS_v1.json` | `1b58c19e3ef501e0f8352a6f8f1c205e9c2582666e3567d46f6967271420bc03` | 2,417 successful synthetic check events; no failures |
| `finite_count_frozen_v1/AUTHOR_ENDPOINT_RERUN_v1.json` | `ec27bcab6e173b779f064f9ee43adcaaa5dad9320813cc3590a18d88cc2a73a1` | Frozen author's 526 controls rerun successfully; no failures |

The count totals describe correlated mathematical controls, not independent empirical tests or exhaustive software verification. The author's runner mostly exercises affine cases; the separate calculation extends the checked examples to non-affine Lipschitz functions without claiming a finite test set proves the general bound. The general bound follows from the explicit integral inequality above.

This block derives a conditional measurement operator and its error domain. It does not derive the scalar action, potential, initial state or scales; does not establish the archive receiver mode, clock accuracy, propagation corrections or emission coverage; and does not fit or validate a scalar gravity model. All new writes were confined to the assigned independent-check directory.
