# NCO phase-continuity attempt and its limitation

The original2001 receiver specification evaluates phase at msec/1000 and frequency at the millisecond midpoint. The day169 label writes the midpoint in both descriptions. Both are preserved; this is a real documentation discrepancy.

Root froze NCO_CONTINUITY_PROTOCOL_v1.json after exposure to the first receiver diagnostic and before this new continuity computation. All17880 adjacent-record pairs across the two registered products were evaluated with exact rational arithmetic applied to the archivedIEEE doubles. There was no phase unwrap, fitted offset, quality clipping or new product exposure.

At the original-spec zero shift, maximum absolute polynomial discontinuity is9.701276819193579e-12cycles forX and2.425319205857186e-12cycles forKa. At the label'shalf-millisecond shift they are1.2085462609361324e-11 and1.1486178882641445e-11cycles. Both remain tiny; the test does not identify the physical sample phase timestamp.

Why this attempted discriminator is insufficient: a polynomial stream continuous and smooth at joins can remain almost continuous after a common small time translation. Comparing oldP(1+delta) withnewP(delta) does not fix an absolute sampling origin. A smaller residual atdelta=0 is not a physical timing calibration. No convention has been selected from these values.

The first600 paired records have P2=F1,2P3=F2,3P4=F3 under floating evaluation, consistent with the documented integrated-polynomial construction. This is metadata consistency, not independently measured oscillator phase.

The recorded nominal carrier predictions nearly satisfy19X−5Ka but that predictor relation is not a new observed gravity or plasma residual. Root inspected its NCO coefficients to understand the data chain; no physical fit or frequency-commensurability assertion follows.

Next: resolve sample/NCO timing from authoritative implementation provenance or a correctly calibrated carrier/reference-phase measurement. The I+jQfrequencyorientation and analogLOphase map also require an explicit supplier. Retain both documented conventions meanwhile. Continuity alone failed as the intended discriminator; do not repeat it as a successful physical calibration.
