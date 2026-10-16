# Focused adaptive-connection check, frozen v1

One narrow source-domain finding requires correction: harmonic identification must require omega>0 (or nonzero frequency with an explicit convention). V1 excludes resonance but leaves omega=0 admitted. At zero frequency, q=A is constant, so fundamental and third harmonic are the same line. With C=tau=g=A=1 and lambda4=1/4, a stable potential, the static cubic force is 1/2 while the displayed B3(0)=1/8. The rational continuation is mathematically valid; it is not a separately observable third-harmonic coefficient there. Root was informed and accepted a narrow v2 amendment. This finding and v1 sources are preserved.

No other material defect found in the stated conditional model. Complete source was read and independent derivation recorded in derivation_before_code.md before implementation inspection. It checks the iff boundedness/coercivity argument including equality, positive kinetic energy and autonomous trajectory boundedness, exact hidden-coordinate signs, shared-preparation amplitude cancellation and its nonzero/distinct-square amplitude restrictions, ramp orders and coefficient ratio, persistent homogeneous modes and resonant exclusion, fractional-linear susceptibility degeneracies, and hidden-coordinate normalization.

The action, quartic coefficient, imposed q trajectory, force/readout calibration and preparation remain supplied. Stability selects an allowed family, not the equality coefficient or a physical law. Harmonic lines require the periodic particular branch; conservative homogeneous modes need not decay and can even overlap the measured third harmonic. Static cancellation describes relaxed hidden w, not arbitrary preparation. The w rescaling convention is distinct from actual q/force/time/energy calibration. No quantum-statistical, scalar-scale, empirical or universal no-go conclusion is established.

Independent check.py uses ODE coefficient recurrence instead of the author's closed-form series, a direct Fourier projection at a positive nonresonant frequency, exact stable/unstable valley checks and the zero-frequency counterexample. Eleven independent assertions passed, including full author output reproduction: 12 passing primary families. Source finding remains despite those passing controls, which use a positive omega symbol. Actual commands and 120-second limits, successful return codes, timings and stdout/stderr are preserved. No computational failure or timeout occurred; the source-domain counterexample is recorded separately from execution success.

All frozen v1 source hashes remained unchanged. Exact binding:

- NETWORK_EVOLUTION_BLOCK15_v1.md: e49f0c56743bee61a46e16ca619b3994fe11c783380c176e4e578270aabaa3b9
- probe_adaptive_connection_v1.py: d4e272d771d6ea30cb01dad878174ab47f00b275961c08224f0738205e8dc80b
- ADAPTIVE_CONNECTION_CONTROLS_v1.json: 02736e8677c0f1415d2984b4497da4925927223342938416ae49fbf04c0ed7c8

This is an independent conditional source check, not an audit verdict. No author/canonical files were edited. V2 confirmation remains separate.
