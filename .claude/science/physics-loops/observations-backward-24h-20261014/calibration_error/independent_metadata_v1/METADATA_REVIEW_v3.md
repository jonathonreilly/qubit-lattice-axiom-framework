# Day-169 ATDF status/slip metadata: independent focused report v3

Date: 2026-10-15. Reviewer: /root/localized_history_check. Root remains campaign author. This is a documentary and byte-decoding check, not a formal audit, calibration fit or physical-error certification.

## Result

Items 19 and 24 record qualitative status; item 87 records an unsigned cycle-count quantity. They do **not**, on the evidence checked here, supply a signed slip correction, guaranteed phase continuity, or a deterministic physical-error bound. The later TRK-2-34 J-1 text cannot silently supply those missing properties to this ATDF.

## What is established for this product

The registered TDF label identifies c32easc2002_169_0000xmmmv0.tdf, fixed 288-byte records, 160,888 total records and 160,870 tracking records beginning at file record 3. Its tracking-format definition explicitly covers format 8 and says its layout is incorrect for format 4. Every decoded tracking record has format 8; spacecraft 82 and year 2002 are consistent throughout. The label's field names, widths and positions match the relevant SFOC-NAV table entries.

| Item | Product label location | Zero-based record bit offset / width | Justified interpretation |
|---|---|---|---|
| 19 | Lines 844-850; status block begins byte 28 | 216 / 1 | Doppler good/bad status. Under the interface's single-bit convention, 0 is the good assertion and 1 the bad assertion. |
| 24 | Lines 886-892; same block | 238 / 1 | Receiver-loop lock status. Under the same convention, 0 is the affirmative lock assertion and 1 the negative assertion. This is not a proof of uninterrupted lock over a whole count. |
| 87 | Lines 1661-1668; Doppler block begins byte 183 | 1466 / 10 | Unsigned total slipped-cycle metadata during the Doppler count, in cycles. The storage has no signed-correction field or supplied correction rule. |

The [1996 SFOC-NAV-TRK-2-25 scan](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/dsn_trk-2-25.1996-07-31.pdf) is legible on the actual page images: PDF page 13 / printed 3-5, Table 3-3 defines items 19/24; PDF page 17 / printed 3-9 defines item 87 as I10. PDF page 21 / printed 4-1, notes 1-4, defines unsigned versus signed packing and the status polarity. Crucially, it also says nonapplicable fields are zero. Therefore zeros in Range, Ramp or noise-summary records cannot be treated as Doppler lock/quality evidence. The page images and their hashes are preserved; embedded PDF text extraction was empty. No OCR guess is being treated as a definition.

The source is a 1996 reissue with a 1997 fax stamp, while the product label discusses the 1997 format transition. The agreement above is checked for these named fields and actual format 8 records; it is not a blanket validation of every historical TRK-2-25 variant.

## Direct metadata check

The independent parser derives field positions from the actual PDS label, decodes only selected identification/status metadata, and checks 168 values by a separate bit-string extraction. It passed on its first execution. No Doppler measurement values, other empirical products or author decoder were used.

The allowed product extends into DOY 170; its filename is not a strict single-day filter. Restricting explicitly to DOY 169 and Doppler sample IDs 1/2 gives 132,881 tracking records. Of these, 46,100 have item 87 > 0. **5,790 records simultaneously have item 19 = 0, item 24 = 0 and item 87 > 0.** Thus even the recorded good-plus-lock combination demonstrably does not imply zero recorded slipped cycles. These are record counts, not independent scientific observations or a holdout test. Full-file summaries keep DOY 169 and 170 separate in the result JSON. Non-Doppler records were classified separately.

No assertion is made that each nonzero item 87 is an uncorrected physical error, that its value is an absolute sum versus another accumulated detector quantity, or that zero means no undetected slips. The available definition does not resolve those questions. The 10-bit storage range is not a physical-error limit; observed values reaching 10 do not establish a saturation rule.

## Later-format comparison, kept separate

The requested [TRK-2-34 Revision J-1](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-34/dsn_trk-2-34.2008-02-29.pdf), PDF page 70 / printed 3-52, defines slipped_cycles as a four-byte integer with range -10 through 10. This differs from the ATDF unsigned I10 storage. At PDF page 121 / printed A-5, note 31 describes a frequency-residual/software-loop estimate that can degrade in high noise. Note 36 defines a running total-phase observable with an explicitly recorded start point that changes after events breaking lock.

Those notes support caution about detector completeness and phase-arc resets **in that format**. They neither document an ATDF item 87 conversion nor establish that the registered ATDF or accompanying ODF uses J-1's signed field, sample interval, phase-start labels or correction convention. I did not pair ATDF with ODF observations or establish a common uninterrupted phase origin. The J-1 paragraphs and table were checked on complete page images as well as extracted text.

## Consequence for an error budget

Quality/lock/slip fields can define declared screening categories. Treating them as a deterministic bound requires additional evidence: applicable detector and correction semantics, sign and observable-unit conversion, count/phase-origin mapping, treatment of resets, and a bound on unrecorded error. Even a conditional N/T frequency bound would require N to bound the relevant total phase error in the correct observable units; that premise is not supplied here. No physical error bound has been inferred from these flags, and no correction was applied to data.

## Reproducibility and limits

Only the four registered c32easc2002_169 products/labels were read or hashed; only TDF metadata was decoded. The ODF and its label were inventoried, not used to infer an ATDF-to-ODF correction map. External access was read-only primary documentation. The first web PDF open failed and urllib encountered a local certificate-chain error; verified-TLS system curl succeeded, with headers and retrieval identities preserved. The relevant scan was reviewed visually. The separately retrieved 2021 revision R was not used as authority. No source, lock, branch, index, PR or audit state was changed.

`SOURCE_PAGE_NOTES_v1.json` pins exact pages and visual evidence. `DAY169_METADATA_RESULTS_v1.json` pins the parser, label, raw file, layouts and counts. `METADATA_REVIEW_IDENTITY_v3.json` binds this report, all evidence and exact source identities.

Revision note: v2 improves spacing and changes “derived ODF” to “accompanying ODF,” avoiding any implied provenance mapping. No source, decoding, count or substantive conclusion changed; v1 and its identity remain preserved.

Revision note: v3 completes spacing cleanup only. The v2 report and its identity are preserved.
