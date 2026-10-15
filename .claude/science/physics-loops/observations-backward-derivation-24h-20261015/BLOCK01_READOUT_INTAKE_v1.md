# Observation-channel intake after the relative-field inverse

Root calculation, 2026-10-15. Exploratory observation-map check; no raw data
newly opened, no independent empirical result, no conclusion against all radio
experiments or against scalar gravity. The v5 inverse still needs independently
identified clock ratio R, radar slowness S, circular-orbit response and areal r.

## Provenance and what was actually inspected

The prior campaign count-source note was read in full at source SHA256
`7665d29d78d2ce302c445bb3f8878e50cb75d89d20bbd14cdb0c4f8d673a0bde`.
Its prior numerical comparisons have not been rerun in this campaign. Its
coherent-phase and clock-transfer formulas are inherited conditional inputs,
not measured ideal R(r), S(r) and orbital functions. Prior raw development
products remain exposed development data; no reserved product was opened.

[Moyer, JPL Publication 00-7](https://descanso.jpl.nasa.gov/monograph/series2/Descanso2_all.pdf),
sections 13.2.2–13.2.4 and 13.5.3, was consulted directly. It distinguishes
phase-coherent turnaround from the spacecraft's one-way transmitter model;
range calibration includes electronics and transponder delays. These are
measurement definitions and calibration obligations, not a scalar action or
independent static clock comparison. Read scope: PDF pages 428–432 and
481–484 (zero-based web page indices); no blanket verification of the monograph.

## Personally derived ideal limit: coherent turnaround is not an extra clock

In a static physical metric, photon Killing frequency is conserved along each
vacuum ray. Between static endpoints r0 and r this gives nu_up(r)=nu_emit(r0)/R,
where R=N(r)/N(r0). Suppose an immediate ideal coherent transponder multiplies
its locally received frequency by a prescribed constant k. The return photon
then gives

    nu_return(r0) = R * [k * nu_emit(r0)/R] = k * nu_emit(r0).

Thus its static carrier frequency ratio is independent of the remote lapse.
This proof assumes static endpoints, constant emission frequency, no media and
that ideal coherent transfer; it does not describe moving Cassini data or erase
gravity's propagation and dynamical effects. With a prescribed time-dependent
emission phase, the returned phase is its delayed, rescaled value; delay and
endpoint motion then matter, as the earlier count note already states.

This is why a coherent turnaround phase cannot simply be substituted for the
independent remote-clock ratio in equation (15). An independently characterized
one-way onboard oscillator could carry different information, but its nominal
frequency field is not itself a proof of proper-frequency accuracy or stability.

For a concrete metric-level ambiguity, take r0=1, N=r^p and B=r^(-2p) on
1<r<2, with any fixed 0<p<1. All these metrics give S=1 and rho=r-1 under
the ideal radial-radar map, and the same constant coherent carrier ratio k.
They have different R=r^p and local circular-orbit speed squared p. Therefore
those radar/carrier functions alone do not uniquely identify R within the
kinematic metric class. This example does not assert that all those geometries
solve one healthy scalar action, or establish a global metric completion.
An independent orbit/clock channel can distinguish them; imposing one without
measurement would be precisely the new assumption to avoid.

## Next decisive step

Construct the primitive clock/radar/orbit error map with shared-clock and
areal-radius uncertainty, then identify a feasible observed channel set. For
Cassini specifically, first determine actual available range, one-way oscillator,
trajectory and calibration content from pinned documentation and metadata.
Do not relabel the existing coherent Doppler comparison as a measurement of R.
If the independent inputs are unavailable, keep this inverse conditional and
pivot to coupled material/scalar response or a preregistered receiver-transfer
test. No blanket impossibility or exhausted-search claim follows.
