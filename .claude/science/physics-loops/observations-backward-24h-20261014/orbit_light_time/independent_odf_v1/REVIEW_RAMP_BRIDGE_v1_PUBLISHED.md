**Focused ramp decoding and exact phase-integration check — June 18, 2002 development file**

The corrected ramp decoder and phase integrator agree with an independent exact-rational implementation on all 69 exposed ramp records and every one of the 91,664 nominal Doppler reception intervals. No material arithmetic or boundary-handling error remains in the checked source. This is a bounded file-format and integration check, not a mission-mode identification, calibration, gravity test, empirical acceptance or formal audit.

The source bound here is `pds_odf_ramp_bridge_v1.py`, SHA-256 `146e7d4cea4998cebae09883e8746fcf8e766c4c8346c60772fcbbfbc72a8acc`, preserved as `AUTHOR_RAMP_BRIDGE_v1.py`. Its current output `ramp_bridge_results_v1.json` has SHA-256 `1c34fdb5ce4353631fcbc9c511dc6b39a8b922ebedad03eb28a65fe7a5a4edfd`, preserved as `AUTHOR_RAMP_RESULTS_v1.json`. The underlying inventory decoder is the previously checked source SHA-256 `2dfc9339ca5a962ade99df5a3270e95cff3e97501ce32f198ce51681fcb2d9c8`. The product label is `37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e`; the raw ODF is `39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f`. No reserved raw track was opened.

I decoded each record using the label-driven independent unpacker, then represented time in rational seconds and frequency in rational Hertz. Phase was computed by interval partition, unique-coverage checks and endpoint trapezoids. That calculation does not reuse the author's nanosecond/nano-Hertz antiderivative or cursor algorithm. It agrees on all record fields, complete-segment integrals, three clipped intervals per actual segment, all adjacent boundary differences, every nominal reception interval and all seven published Doppler-group summaries.

For integer nanosecond endpoints and start epoch, the author's terms have the correct units: initial nano-Hertz times nanoseconds divided by 10^18 gives cycles, and nano-Hertz/second times squared nanoseconds divided by 2*10^27 gives the affine phase contribution. Signed rate components, fractional start/end times, start-relative rather than absolute epochs, lower and upper clipping and endpoint frequency propagation were checked separately. Exact precision is not an assertion of instrumental accuracy.

The actual station inventory is:

| Station | Ramp records | Gaps | Overlaps | Nonzero endpoint differences at contiguous boundaries |
| --- | ---: | ---: | ---: | ---: |
| 25 | 23 | 1 | 0 | 7 |
| 45 | 26 | 1 | 0 | 5 |
| 54 | 20 | 0 | 0 | 5 |

All 69 records declare sky-level frequency/rate. Each of the 91,664 nominal receiver intervals lies within a single ramp record for its receiving station; none crosses a ramp boundary. This establishes neither coverage at retarded emission times nor that the receiver-station ramps provide the applicable reference or transmitted phase. Every Doppler receiver/exciter-independent flag is one. The electronics role, frequency-conversion convention, clock mapping and emission epochs remain unresolved. The product label describes frequency-ramp tables for tuning receivers **or** transmitters; station and sky-level fields alone do not identify their instrument role.

The author's original label counted endpoint frequency differences across gaps as jumps. That is a real output-scope mistake and remains preserved in runtime `RAMP_INITIAL_LABELING_v1.json`, SHA-256 `2f45ed51a022acfa12c3a10a4c275e12dfdcabbba739e3a40fd6ab16bde152ae`. The initial source hash was `af93097aebdc1700fb56174d501d0d51478fc5b20019cfbe9268fbe7a7eaef18` and initial output hash was `377244546cb7bf2b6c9d1524ea1a1732a622c1d52669d272ca2f955bb9a9e6dd`. The current field `endpoint_frequency_difference_hz` describes all adjacent entries, while `jumps_at_contiguous_boundary` counts only zero-gap nonzero differences. I independently verified the corrected 7/5/5 counts. No arithmetic change or scientific acceptance follows from that wording correction.

The exact checks total 183,893 successful check events and zero failures. These include grouped comparisons; they should not be described as 183,893 independent empirical tests. A separate synthetic probe has 32 checks covering signed ramp decoding, units, exact clipped and partitioned integrals, rejection of gaps, overlaps, mixed station/sky level, unsorted tables, unsupported intervals and nonpositive intervals. Eight retained, deliberate source mutants were all rejected: signed-rate fraction, frequency scale, rate-integral scale, absolute-epoch leakage, upper clipping, overlap guard, mixed-source guard and lower clipping. Positive-case exceptions count as behavioral failures, not unexamined process crashes. Mutation evidence supports these specific checks and is not exhaustive verification.

Reproduction evidence in this directory:

| File | SHA-256 | Scope |
| --- | --- | --- |
| `check_ramp_independent_v1.py` | `442bf49505a85cbaf6986b96de5677efa85d73044a46e17c52678aa2ca32c1f9` | Independent decoding, partition/trapezoid integration and synthetic mutation checks |
| `RAMP_INDEPENDENT_RESULTS_v1.json` | `737eaac0ba7cc347dd35660ccbb69294e74d70839588c69af6dbd4e643465f48` | Exact comparisons, synthetic cases and eight mutant rejection receipts |
| `ramp_mutations_v1/` | Individual hashes recorded in the results | Mutant evidence, not candidate scientific source |

The earlier inventory report and its one genuine padding-label coverage failure remain unchanged. The ramp correction does not erase that failure or settle the label/specification convention discrepancies. All writes were confined to this independent-check directory; canonical science, ownership, branch state, existing reviews and reserved data were unchanged.
