# Same-day energy-addition source review

2026-09-27. Read-only source investigation with safe path-checked extraction of the four explicitly requested July29 acquisitions into `source/`. No supplied code was executed, no data were fitted, no nearest-row or prediction-based selection was made. `SOURCE_IDENTITIES.json` gives the archive SHA-256 and every extracted member hash. JSON quantities and raw HDF5 axes were inspected directly; `dataset_inventory.txt`, `snapshot_relevant_fields.txt` and `primary_evidence.txt` preserve the selected evidence. A local `read-tools/` dependency directory was used only to read HDF5 metadata/data axes.

## Conclusion

The archive supports a **conditional center-frequency consistency diagnostic**, but does not establish a matched-condition pointwise energy-addition test across these four acquisitions. They have closely matching nominal fields and identical applied gate ranges, yet are separated by hours, use different preparation/readout settings, and exhibit different fitted gate periods and sweet spots. The source explicitly reports charge-offset drift of a gate period in about10minutes. Thus equal applied gate voltage does not establish equal offset charge or parity branch. A failed pointwise sum would not exclude energy addition or a Hamiltonian.

For a fixed Hamiltonian, charge coordinate and parity, f02=f01+f12 by energy subtraction. For parity-averaged centers this remains additive only when the same averaging and underlying conditions are used. Separately fitted sinusoidal gate-scan centers need not realize that exact average under drift, unequal sampling, fitting bias or higher charge harmonics. Their quoted local fit standard errors do not cover those effects.

## Exact acquisitions and measured axes

All four are July29,2022 archive acquisition IDs, not rows chosen by frequency agreement:

| Time / suffix | Observable | Raw axis |
|---|---|---|
|074423-596-6dd5d0|Ramsey01|267 delays40ns–19.99µs,31 gate voltages−.12…+.12V|
|161812-900-75f285|Ramsey12|150 delays40ns–3.765µs, same31 gate voltages|
|173536-429-b495bf|CW f03 spectroscopy|120 frequencies14.600348279882–14.719348279882GHz,1MHz step; same31 gates|
|184407-433-6f4c63|f02/2 spectroscopy|60 frequencies5.073919049795–5.079819049795GHz,100kHz step; same31 gates|

Ramsey raw y axes are I/Q volts. Spectroscopy y axes are S21 W/W and phase degrees. Both spectroscopy `analysis_Basic2DAnalysis/quantities_of_interest.json` files are empty: this archive analysis does **not** supply an independently fitted spectroscopy center or its uncertainty for these acquisitions. A source-independent measured-only extraction would be a separate next step; scan midpoint or generator snapshot frequency is not a measured center. The f03 axis is near14.66GHz, not f03/3. f01 and f12 alone do not predict f03 without an additional f23 measurement or model.

## Frequencies and detuning convention

Use the GateScanAnalysis center frequencies, not the rounded names, nominal microwave settings, or single-linecut BeatingRamseyAnalysis results:

- Ramsey01 center:5,241,050,649.171623Hz; fit standard error9,617.980154Hz.
- Ramsey12 center:4,912,700,039.843716Hz; fit standard error28,433.030948Hz.
- Their arithmetic half-sum is5,076,875,344.507669Hz =5.076875344508GHz. If local center errors were independent, its formal propagated standard error would be15,007.854537Hz; independence and systematic coverage are not established. This is an arithmetic candidate, not a measured spectroscopy comparison or precision test.

The archived convention is actual detuning = fitted oscillation frequency minus artificial detuning; inferred transition frequency = reference frequency minus actual detuning. Artificial detunings are1.573MHz for01 and3MHz for12 (single-linecut fit messages and numerical values). Gate-scan `qubit_frequencies_1 + detunings_1` reproduces fixed references5,241,114,296.51445Hz and4,912,716,410.0384245Hz, respectively, matching snapshot q0.freq_01/q0.freq_12. The positive fitted oscillation frequencies must not simply be added to the microwave reference. No multiphoton divisor applies to either Ramsey01 or Ramsey12; the division by2 enters only when comparing their sum to the two-photon spectroscopy drive axis.

The single-linecut QOI, for example, reports01 branches5,241,155,921.809003 and5,241,073,870.648492Hz, and12 branches4,911,701,176.730598 and4,913,850,140.728479Hz. These are not the scan-center estimates. Branch1/2 labels in separate fits do not establish common physical parity across hours.

## Conditions that match, and those that do not

Snapshot `Aligned_Vector_Magnet.v1_component` is approximately0.1499988696T for all acquisitions. Its v3 perpendicular component is602.583013585µT for01,602.519937265µT for12, and602.518041497µT for both spectroscopy scans. They are close but not identical; vector and component caches in snapshots are not always internally identical readbacks. This review has no independent field-drift-to-frequency calibration and makes no correction.

01 and12 starts are8h33m49s apart;01 to f02/2 is10h59m44s;12 to f02/2 is2h25m55s. Names establish start times, not acquisition durations or per-point timestamps. GateScanAnalysis fitted periods are157.098994±5.938261mV for01 versus209.774079±2.727908mV for12; fitted sweet spots are+51.432463±3.047258mV versus−118.800812±1.935915mV. Sweet spots are periodic and cannot be compared by raw subtraction alone; nevertheless these fits do not establish a common calibrated charge map. Different apparent periods could reflect drift or fit limitations; no physical cause is inferred here.

The01 snapshot has init_duration67.32µs, readout amplitude.133333V and readout frequency7.546627454GHz. The12 snapshot has81.6µs, .146296V and7.546035272GHz. Both have q0 microwave duration20ns and readout duration720ns, but these are instrument configuration values, not proof of the executed sequence. The12 acquisition is explicitly a qutrit Ramsey analysis; paper AppendixE describes a |1⟩–|2⟩ superposition. Raw snapshot fields alone do not certify state preparation fidelity, equal photon occupation, absence of AC Stark shifts or a full executed pulse schedule. Spectroscopy is a different acquisition mode. Do not infer spectroscopy timing from cached q0.spec_pulse settings or infer Ramsey12 pulse duration from a stale qt0 parameter.

Source arXiv2403.03351v1 AppendixE, local text lines1660–1693, describes two Ramsey parity contributions and reports hysteresis and charge drift of a period in10minutes. SupplementaryIII lines3409–3414 repeats that observation and explains bracketing parity sequences with Ramsey measurements to reject severe drift. Such bracketing is not documented for the proposed cross-acquisition energy-addition pairing. Local fit errors are not inter-acquisition drift bounds.

## Admissible next claim

Retain the exact four acquisitions and conditional half-sum before any spectroscopy extraction. A future measured-only extraction of the full f02/2 gate map can compare fitted centers under a stated center-averaging assumption, keeping all fit failures and covariance/line-assignment limits. Pointwise gate matching, parity-specific energy addition, precision agreement or physical exclusion are unsupported without resolving charge-map/time/preparation correspondence. No target residual was calculated here and no outcome was selected.

## Additional source identities

- `Krause2024.pdf` SHA-256 `538f4b4dc70a2d7879e33b91b9d420c604dc64fe490f97103d2c1ea5e3c63ad6`.
- `Krause2024.txt` SHA-256 `7b4d9318649b159eb37bb7c55b42c18f0309ee8bd9aa98a2da273ac785f2916f`.

The PDF is the locally archived arXiv2024 version; no claim of a fresh final-journal equivalence check is made. Complete raw-member identities are in SOURCE_IDENTITIES.json.

## Same-TUID analysis-version discrepancy (final source follow-up)

An exact timestamp lookup, not nearest-frequency matching, finds this01 acquisition in `df_ramsey_vs_gate_01_incl_disp_shift.csv`, physical zero-based row25, saved dataframe index29. Its center is5,241,116,551.53761Hz with standard error1,254.390225Hz, splitting108,414.550725Hz and gate period.218897627488V. These differ materially from the extracted GateScanAnalysis QOI above for the exact same TUID: center difference65,902.365987Hz, and different splitting/period/error estimates. The table's field and instrument reference agree with acquisition identity; that agreement does not establish which analysis revision or filtering produced the discrepant fit.

The archived JSON and processed CSV must therefore be preserved as distinct source-analysis versions. The reason for the discrepancy is unresolved; no fit should be selected by downstream agreement. The archive-QOI half-sum remains the explicitly chosen source-version arithmetic above, but its narrow formal error is not robust coverage of source analysis choice. Substituting the CSV01 center alone changes the half-sum by32,951.182994Hz. A small target residual cannot resolve this provenance/fit-quality uncertainty. Parent reports a separately frozen prediction and target comparison; this review did not reproduce that comparison or use it to choose a source version.

Processed Ramsey CSV SHA-256: `0a6adbe7046485334e4c840e19d5b5b5225592b9bf663be957476d2353048c3f`.
