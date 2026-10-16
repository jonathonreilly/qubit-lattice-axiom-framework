# Sharp error-envelope controls: independent derivation and source correspondence

This is a narrow supplement to the canonical mathematics review. It checks only the two new supplied-rational witnesses and the added assertions. It is not a new uncertainty model, observational test, full helper run, mutation-suite validation or formal audit.

## Independent witness result

The complete calculations were frozen before reading the added source controls in SHARP_ENVELOPE_PRECHECK_v1.md, SHA256 `f9b544607b9f2ad8c61b90f2de4e2bc0acade7e0a62c1181774c89af049a0d50`. Nine independent exact checks passed.

For the matrix case, P=(2,4,6), rhat=(0,0,1/3), zhat=(9/10,1/2,1), d=1/100 and er_i=2d/P_i give ||Lhat^-1||_infinity=4 and eta=1/25. Holding M fixed and shifting r by (-er1,+er2,-er3) gives

    z-zhat=(-1/32,-1/48,+1/24).

The actual infinity error is 1/24, exactly the correct state bound. Replacing 1-eta by 1+eta would give 1/26, which fails. The rank-one perturbation calculation and exact inverse both establish this result.

For the ratio case, P=(-7/3,2/3,5/3), rhat=(6/7,0,6/5), zhat=(1,1/2,1), e=1/100 and delta M=e(1,-1,1) give

    z-zhat=(1/300,+1/25,-1/25),
    qhat=1/2, q=9/16.

The actual ratio error is 1/16, exactly epsilon(1+|qhat|)/(|yhat|-epsilon), with epsilon=1/25. The deliberately wrong plus denominator gives 3/52<1/16. The true R,q are positive and y is nonzero. These witnesses are attained bounds, so they expose the two denominator mutations that conservative fixtures could miss.

## Exact source comparison

After the independent freeze I copied the current canonical domains helper:

    scripts/scalar_dynamical_domains.py
    SHA256 595eb5d19ad4891021078f377464583f722bc4b8e8646a8dd13d3b5e136ba1c1
    7,656 bytes.

The complete diff adds the two sharp controls to checks(). AST comparison confirms every non-control function, including error_envelope and inverse, is unchanged from the previously reviewed canonical version. The two new assertions compare the independently computed actual errors with both their exact expected values and the implemented bounds. Consequently the wrong plus denominators fail those assertions; no envelope formula was changed to accommodate a test.

A focused post-exposure probe called only the two copied APIs on the two specified fixtures, not checks(). It reproduces actual_error=state_error=1/24 and actual_q_error=q_error=1/16. Together with API-AST and failed-source-delta checks, four source-correspondence checks pass in SHARP_ENVELOPE_SOURCE_RESULTS_v2.json.

## Preserved failures and limits of mutation evidence

The failed author fixture source is preserved separately, SHA256 `7d0010c499bd650dd26ec97b310e40f15a5b6d3011dccab84b57f0bc04d4b335`, 7,657 bytes. Its only difference from the corrected source is Rational(-6,7) becoming Rational(6,7) in the first ratio r entry. I checked that exact full-source delta. I did not rerun the failed author baseline. Root reported its 25-pass/1-fail result and explicitly invalidated the v2 mutation run because that baseline failed; this review does not count any of those mutation rejections as evidence.

My first post-exposure source-comparison probe had a separate mechanical mistake: it searched for the equivalent spelling -Rational(6,7), whereas the preserved source uses Rational(-6,7). The two mathematical API checks already passed; the literal source comparison failed. The original source, 3-pass/1-fail result and exact diff remain immutable. Version 2 corrects only that literal pattern and passes 4/4. No mathematical formula, fixture value, source under review or tolerance changed in that repair.

The fresh v3 mutation run and its baseline guard are root-owned and have not been validated here. The independent sharp calculations do not rely on any mutation-run result. The earlier full review and affected-source reports remain unchanged; this supplement binds only the displayed domains-helper update.

## Scoped conclusion

Both added witnesses are mathematically sharp, correctly implemented and decisive against their stated wrong denominators. No substantive discrepancy was found. They certify sensitivity of these exact controls, not an observational noise envelope, a full observable-chart certificate or a general proof about every possible implementation mutation.
