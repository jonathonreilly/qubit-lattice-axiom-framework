# Spectroscopy drive source review

2026-09-27. Source-only bounded inspection of exact July29 acquisitions173536 (f03) and184407 (f02/2), their archived snapshots/raw axes, local Krause2024 arXiv text, and archive analysis-notebook/code inventory. No fit, drive correction, target-center-based calibration or model simulation. Existing source identities and extracted raw files are preserved.

## Outcome

These archived sources do **not yet fix an executed Hamiltonian drive strength or finite-pulse duration independently of the observed03 line**. They support a source-based list of instrument settings and CW acquisition context. The f03 snapshot has substantial inconsistencies with the raw acquisition axis, so it cannot simply be promoted to a complete executed-setting record. A hypothetical drive-response sensitivity calculation remains possible, but an empirically calibrated AC-Stark correction is not established by this packet. This is a limitation of the bounded available evidence, not a universal impossibility claim.

## Exact snapshot settings

All power values below are instrument-level dBm, not device power or Hamiltonian coupling:

| Field |173536 f03 snapshot|184407 f02/2 snapshot|
|---|---:|---:|
|sgs_fridge.frequency|5.079819049795GHz|5.076519049795GHz|
|sgs_fridge.power|−8.279640859dBm|−10.279640859dBm|
|sgs_fridge.status|on|on|
|vna.center_frequency|7.547331401546GHz|7.547304021932GHz|
|vna.power|−54.383250243dBm|−59.383250243dBm|
|vna.status|off|on|
|vna.bandwidth|10Hz|20Hz|
|vna.npts|3|3|
|vna.sweep_time|.28806s|.14406s|

The f03 raw frequency axis is14.600348279882–14.719348279882GHz; the f02/2 raw axis is5.073919049795–5.079819049795GHz. Thus the f03 generator snapshot frequency is outside its raw swept range, while equaling the last bin of the f02/2 range. Its VNA is also off despite the stored measured S21 map. These facts establish that the snapshot is not a self-sufficient synchronized account of every executed f03 setting; they do not prove when/why the discrepancy arose or that its power alone is wrong. Possible caching, later settings, routing or frequency-extension metadata must be resolved rather than assumed. Fig.6 includes an SGU100A extension device, so a generator-to-output frequency mapping cannot be invented from one cached field.

The f02/2 generator frequency lies within its raw scan and the VNA is on. This is stronger consistency, not proof of constant executed power throughout the sweep or of the device field amplitude. A single snapshot does not log per-point drive amplitude, switching history or settling.

The VNA settings concern the cavity/readout measurement near7.547GHz. They are not qubit spectroscopy power at5.077 or14.66GHz. The separately recorded signal_hound frequency/power is a spectrum-analyzer reading, not a spectroscopy drive command. Substituting either for the qubit drive would be a convention error.

## Cached pulse calibration is not spectroscopy calibration

Both spectroscopy snapshots retain q0 fields: mw_amp180=.464074281821, mw_ef_amp180=.525995685962, mw_pulse_duration20ns, q0.freq_01=5.241234956743GHz, q0.freq_12=4.912603142846GHz. They also retain spec_pulse_duration1µs, spec_pulse_frequency5.4405GHz and spec_pulse_amp.1, while qt0.mw_pulse_duration_12 is20.48µs. The source names and contexts do not establish that these fields describe the executed CW gate maps; the5.4405GHz cached spectroscopy frequency in particular matches neither scan. Do not assign the1µs cached duration to these data or equate the20.48µs qt0 field with an actual Ramsey/control pulse duration.

The time-domain microwave sources rs_100a_q0, rs_100a_q0_12 and rs_100a_ro are recorded off in the spectroscopy snapshots. Their stored LO powers and frequencies are not a calibration of the independent spectroscopy path. The source paper AppendixA (local text1173–1184) describes DRAG controls, predominantly20ns pi/pi/2 gates, amplitudes optimized by Rabi measurements, frequencies by Ramsey, and DRAG by XY sequences. That gives a calibration procedure, not the executed waveform area, measured Rabi rate or calibrated volts-to-device-drive transfer for these spectroscopy runs.

Even a known pi pulse would require its envelope/integrated area and convention to infer the drive coefficient. Relating that control to CW spectroscopy requires calibrated attenuation/gain and routing at the relevant frequency. A01 pi calibration near5.24GHz cannot directly set the charge-drive coefficient near14.66GHz without frequency-dependent line/cavity transfer and appropriate matrix-element mapping. No such calibration was located. The source archive's July29 inventory contains no Rabi-named acquisition members; this does not prove that calibration was never performed.

## Duration, preparation and line transfer

The f03 acquisition name explicitly says CW; the source describes two-tone spectroscopy with an extra microwave source and VNA (Fig.6/text1140–1142) and routes both control pulses and CW tones through the cavity input (text1179–1182). The f02/2 dataset is likewise a frequency/gate S21 scan. Neither raw HDF5 file stores a verified qubit-drive envelope or per-point on-time. VNA sweep times and IF bandwidths describe readout acquisition/filtering; they are not by themselves qubit pulse durations or a complete statement of settling/transient preparation. Do not substitute them as a finite rectangular pulse without an executed schedule or timing log.

Fig.6 lists nominal attenuators/filters and hardware. A wiring attenuation count is not a measured transfer function at the chip across5–15GHz: mixer/extension conversion, cable/filter/cavity response, port coupling and amplification must be distinguished. Readout photon number would additionally require cavity input coupling, losses and detuning/power calibration; its AC-Stark effect is separate from the direct spectroscopy-drive effect.

The archive code inventory contains analysis/figure notebooks and model helpers; bounded source-text searches found no executed acquisition script or a source-power-to-Hamiltonian-amplitude calibration for these exact TUIDs. Prior fit-only linewidths must not be turned into Rabi rates without independently justified dephasing, relaxation and response assumptions. Fitting a drive amplitude to remove the03 center residual would be target-based correction, not an independent prediction.

## What would close the obligation

An executed per-acquisition drive/routing record, waveform or CW timing/settling description, and independent drive-transfer/Rabi calibration on the appropriate path and frequency could fix the Hamiltonian coefficient. A controlled same-transition power series extrapolated to zero drive could alternatively establish an operational frequency correction, provided its extraction/control selection is declared independently of the desired residual. Neither has been established here. Until then, retain drive strength, duration/steady-state assumption and dissipative preparation as explicit unknowns; do not report a quantitative measured AC-Stark correction from the present snapshots alone.

## Source identities

| Source | SHA-256 |
|---|---|
| ../koeln-two-junction/Krause2024.txt | 7b4d9318649b159eb37bb7c55b42c18f0309ee8bd9aa98a2da273ac785f2916f |
| ../koeln-two-junction/Krause2024.pdf | 538f4b4dc70a2d7879e33b91b9d420c604dc64fe490f97103d2c1ea5e3c63ad6 |
| ../koeln-two-junction/Krause2024_Quasiparticle.zip | a8272b6cbe92ddc083d2a22b94bdb7743b19c50debbe89f4106baf817c69c574 |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-173536-429-b495bf-CW_spectroscopy_gate_voltage_scan_f03_q0_at_Boop_602_uT_Bip1_149_mT/snapshot.json | dbbfdb9f965701912b5e7a2b4faf052ea6c597c149ce838cc1a2db6d2810a597 |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-184407-433-6f4c63-spectroscopy_gate_voltage_scan_f02o2_q0_at_Boop_602_uT_Bip1_149_mT/snapshot.json | 5ab8c600f23c6f074c6c3d71c7af88f12234a1bd3b37a555a2997dd75596fd13 |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-173536-429-b495bf-CW_spectroscopy_gate_voltage_scan_f03_q0_at_Boop_602_uT_Bip1_149_mT/dataset.hdf5 | e53727072e8689c63332eebd8094888f6ee4d6ea9d66281f5f7efc56db0bf7cf |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-184407-433-6f4c63-spectroscopy_gate_voltage_scan_f02o2_q0_at_Boop_602_uT_Bip1_149_mT/dataset.hdf5 | d11dcdfbbc6fb3b5052aae9492ad4c204dd0698ecd34370c11f43a3184d62f7f |

Paper references concern the preserved arXiv2403.03351v1 source, not a new final-journal version check. No scientific input or editable prompt file was changed.
