# M10 canonical affected-source correspondence, v1

The two canonical adaptations preserve the checked data path and fix the identified phase-coefficient and alias-pairing issues. The exact phase increment now agrees with the independently frozen expression on every matched X row. The deliberately fixed 16000-bin/one-peak search still has the preserved Ka49112 sensitivity; this supplement does not declare complete spectral agreement or a globally optimal/physical carrier.

## Bound sources and read scope

Canonical carrier helper: scripts/cassini_carrier_estimator.py, SHA256314724bf119f71a0bfe678ec5aa5e094efca251a24d871ac23957e80af18899f. Canonical reference helper: scripts/cassini_receiver_reference.py, SHA25672eec75703d5577dc97e20a5e1c96d7e46bca6d1d94c8874b1dd5ec02359c10c. Complete current bytes and complete deltas from the original working sources are preserved under canonical_sources_v1. I read both complete working sources and every canonical difference. This is a scoped composition of that review with the affected deltas, not a fresh global unit audit.

Packaging changes add the 180-second declaration, adjust repository-root location, accept explicit cache/output/protocol arguments, return result objects, and rename the carrier summary. Raw input identities, selection, exact certificate formulas, header/count extraction and retained candidate set are unchanged.

## Alias-frequency and amplitude pairing

For centered times t_n=(n-(N-1)/2)/fs, changing frequency by an integer sampling period multiplies the template by the constant exp(-i*pi*k*(N-1)). For even N=1000 and odd k this factor is -1. Consequently an amplitude computed at the pre-wrap frequency cannot in general be paired unchanged with the returned wrapped frequency. The canonical helper wraps frequency first, then recomputes correlation, amplitude and residual at precisely that returned value; the waveform pair is consistent.

This fixes a mathematical representation issue rather than selecting a physical sideband. Six existing synthetic known-tone controls now also reconstruct the waveform using the returned frequency/amplitude. I inspected those assertions and the algebra; their execution belongs to the separate author/math-check evidence. The fixed observed frequencies are far from the seam, so the change does not switch any data peak. Recalculation at the rounded returned frequency may alter amplitude/residual at floating-point roundoff. I did not rerun all spectra or the helper's broad controls.

## Declared phase polynomial restored

The canonical nco_increment now evaluates P2+P3*(1+2*delta)+P4*(1+3*delta+3*delta^2), exactly the declared difference of the archived cubic P over a one-second interval. It does not infer exact identities from the separately rounded F coefficients. This agrees with my original pre-exposure construction. The historical F-based source/results and the nonzero exact discrepancies remain in the original working correspondence report; they were not relabeled as phase-based results.

For the affected code check, I extracted only the nco_increment function AST, supplied Fraction as Q, and evaluated it using independently frozen header/interval values. All 2400 sign-expanded candidate terms match exactly, representing 1200 distinct X-row/timing terms. No author module was imported; no raw decoding, spectral fit, count extraction or broad numerical suite was repeated. CANONICAL_PHASE_AFFECTED_CHECK_v1.json records source identity and scope.

## Preserved grid sensitivity and pending output binding

The root's immutable working route selects +0.9251746909516783 Hz for Ka49112; the independent route selects -0.5322262786634724 Hz with lower residual. Independent direct correlations confirm the difference and a separate denser diagnostic grid supports the latter basin. The fixed canonical estimator intentionally preserves its declared 16000-grid/one-peak method. This is an explicit sampled-search limitation, not an unreported replacement of one observed value. Original tolerances and the original failed all-row comparison are preserved. The X reference comparison is unaffected by the Ka peak difference; physical carrier selection remains open.

The working-source correspondence report is 0f2c33fbd01bdfffadb5880f847c2f6dd5c2f860c0ccf4c83b64459d9bacc48d; identity219039b8d01beb6b1d36cd59e5bc818700b553b628641548ba73de432976b179. The original independent report and identity also remain unchanged. Final canonical generated products/cache have not yet been bound here; a separate narrow final-envelope confirmation is pending. No source, branch, index, status or lock was edited by this reviewer.
