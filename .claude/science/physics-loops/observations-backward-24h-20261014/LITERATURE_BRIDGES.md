# Literature and data roles

Use primary observational publications and data products. Published Cassini gamma summary is already exposed from the previous campaign. New reading will be logged by source, retrieval, hash where possible, role and exact use. No external result is an axiom supplier. No independent empirical test is registered yet.

- Bertotti, Iess and Tortora (2003), nature01997: previously exposed gamma summary 2.1+-2.3 times 10^-5; observational comparator only. Primary Nature page retrieval failed once through web redirect; indexed primary abstract accessible. It does not supply the measurement forward model.
- Dyadina/Labazova, arXiv:2111.13900v1: literature comparison on mass calibration in massive scalar light time; does not establish our circular-force derivative or selected action. Primary PDF acquired/read where available, source hashes in runtime/sources.
- Ashby/Bertotti arXiv:0912.2705v1: primary warning about enhanced higher-order light-time terms in the actual Cassini geometry. No error number is imported without calculation.
- NASA PDS CO-SS-RSS-1-SCE1-V1.0: original Cassini 2002 radio data exist, with ODF/ATDF/RSR plus ancillary ephemerides and calibrations. Metadata and labels inspected; only the preregistered June 18 development ODF values have now been decoded. No gravitational fit has been performed. This reopens a concrete observational route. Archive metadata are source/format information, not physical priors.

Initial Python HTTPS fetches failed certificate validation; retained original error receipts and retried with the installed certifi CA bundle, without disabling TLS verification.

Source receipts are under the local runtime sources folder. Primary PDF hashes: Cassini RSS guide 2018 4feb3072681da0f3026889d41864cef0c92c0beb91926278fc2d907e607c1d76; Dyadina/Labazova2111.13900v1 abccb5726a987cff7f13016878cedcfb5b232a6f8162f25ca3e9798bf2c7a457. The pypdf extraction of the guide emitted object-reference warnings; no layout claim relies on that extraction. Raw development ODF hash 39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f; its label hash 37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e. Large raw files remain local.

Count/clock extension: Moyer2000 sections13.2.4,13.2.6,13.3.2.2; TRK-2-18 June2000 AppendixA; the PDS ATDF interpretation guide Table5/AppendixB; and Morabito/Asmar1995 sectionIII.C now support the receiver count reconstruction. Exact URL/length/SHA pins are in scripts/cassini_doppler_development_inputs.json. The same-track ATDF was registered in RAW_DATA_PROTOCOL_v2_ATDF.json before download. It is exposed development, not a new independent experiment. The PDS guide corrects the erroneous high-part scale in the original label; the failed literal-label result remains preserved.

## Radio-link and atmospheric supplier context

Armstrong2006 sections4.3–4.6 and the Cassini2018 radio guide section3.6.2.2
supply the known three-link architecture and calibration context. DORS-002
defines PD1/PD2 as retrieved wet/dry path delays and quality flags, while the
Cassini RSS SIS section3.3 defines RSR transmitter/receiver filenames.
Exact retrieved identities and exposure roles are in
physical_link/METADATA_SUPPLIER_REVIEW_v1.json. No published precision is
imported as a campaign error bound, and none of these sources derives the
candidate scalar action or field state.

## Receiver instrument references, current block

Primary sources distinguish X/X 880/749, X/Ka 3344/749 and Ka/Ka 14/15 ideal turnaround ratios from an operational cross-uplink relation. Armstrong 2006 (revised 2016), section 4.6, and the DESCANSO ground-system sections are pinned in channel_quotient/independent_instrument_v1. The Kliore scope uses an author-uploaded text extraction; no original PDF identity is asserted. Asmar 2005 supports the standard dual-frequency contrast with common-ray qualifications.

The original 2001 DSN 0159-Science PDF has SHA256 1161d5d7f50134cf3994c52674af4a2d8984990b7a7c64551b6c17d5964fe32d. Root personally read and visually verified PDF pages 17–18. It separates start-of-millisecond phase from midpoint frequency; the archive label prints midpoint for both. The specification supplies sample timing, pipeline compensation and a nominal sky-frequency relation. The reviewed sections do not fix the I+jQ frequency orientation or actual analog LO phase fluctuations. Recorded NCO predictions are distinct from measured sky phase.
