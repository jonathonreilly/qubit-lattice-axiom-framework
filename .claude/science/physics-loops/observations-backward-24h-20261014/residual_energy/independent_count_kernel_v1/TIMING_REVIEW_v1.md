# Independent nominal timing inventory check

Reviewer: `/root/force_energy_bridge_check`. This is a scoped source/data
consistency check, not a formal audit or a physical gravity test. Root remains
the scientific author. All reviewer writes stay in this independent folder.

## Permitted input and independence

I read `DEVELOPMENT_TIMING_PROTOCOL_v1.json` before opening records. The only
raw products read were its two already-exposed inputs:

- ODF SHA-256 `39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f`, 3,314,304 bytes.
- Label SHA-256 `37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e`, 63,903 bytes.

The exact file is named for day169 but its label extends into the next UTC
day. The permission is tied to these bytes; no later track/product was opened.
The label states that the Doppler time tag is the compression midpoint and
that compression is stored in hundredths of a second. This supports nominal
archive interval construction, not a derived station proper-time map.

`TIMING_PRECHECK_v1.md` froze the parser, static fields, exact arithmetic and
sample-selection procedure. The independent implementation sliced complete
288-bit record strings directly according to the label rather than calling
the new author inventory. It then compared every decoded row with the frozen
published decoder. The new author timing code and results were not opened
until the independent calculation completed and `TIMING_INDEPENDENCE_v1.json`
froze its output identities at 2026-10-15T02:34:32Z.

## Independent result

All 91,863 orbit records agreed field-for-field with the published decoder.
The complete type accounting is:

| Type | Records |
| --- | ---: |
| 11, one-way Doppler | 649 |
| 12, two-way Doppler | 61,459 |
| 13, three-way Doppler | 29,556 |
| 37, range | 199 |

There are 91,664 Doppler records, eight static configuration strata, and 36
strictly adjacent nonoverlapping chains. The exact sorted-neighbor accounting
is 91,628 adjacent pairs and 28 gaps. There are no overlaps, duplicate nominal
intervals or identical duplicate records in those strata. Every Doppler row
has compression 100 centiseconds: one nominal archive second. No bad-flag row
or nonpositive Doppler duration occurs in this particular input; all flags and
all one-way rows were retained rather than selected away.

The chain-length range is 1 through 18,730 records. Summed duration and union
coverage agree within each static stratum; their total is 183,328,000 doubled-
millisecond units. Summing across strata is only an accounting statistic, not
an assertion of independent physical observing time. The independent code
separately computed union coverage and multiplicity overlap, so a nested
interval would not be mistaken for an ordinary neighboring-pair overlap sum.

The exact nominal endpoints are

    start_2ms=2*(1000*time_seconds+time_milliseconds)-10*compression_cs,
    end_2ms=2*(1000*time_seconds+time_milliseconds)+10*compression_cs.

All fifteen static decoded fields are included, excluding only time,
observable, compression and the two delay fields as the protocol specified.
Configuration values are retained without interpreting unexpected values as
invalid or using measurement magnitudes for selection. Chain continuation
requires exact endpoint equality; a gap is not bridged silently.

## Comparison with author timing v2

The author source is `development_timing_v2.py`, SHA-256
`9b41c5a92214cd0cd6ee4e8c0c3c99b89f2af9ef6b06467e5fa72fb7ca6ef5bc`.
Its result SHA-256 is
`a6a50d9e0934ff06f06c4ff63b6b710dee95461170f8c99c7ff847fc384a6f67`;
its full chain ledger SHA-256 is
`cd5ba960fef413f2207056fa3cf39cf674242a51ce87081834953a0aa8a0a813`.

The independent and author implementations sort configuration keys in different
orders. Comparison matched complete configuration dictionaries, not incidental
stream numbers. All eight strata, all 36 chain timing rows, all 28 exact gap
boundaries, type/duration counts and pair accounting agree. For every chain,
the one-second duration makes the recorded 6pi-scaled Gram diagonal 2 and
neighboring off-diagonal -1 wherever those entries exist. Singleton chains
correctly have no adjacent-difference Gram entries.

Four chains were chosen by timing/configuration criteria fixed before observable
selection: the first three chains in the independent static ordering, with
lengths 11,564, 18,730 and 3,147, plus the first one-way chain of length 394.
The longest-chain criterion selected an already chosen chain. No changing-
duration or bad-flag chain existed. For all four, the exact rational weighted
mean and centered raw-frequency sum agree with the author ledger. The independent
computation also verified each centered sum by directly summing rational centered
squares rather than only reusing the raw-moment formula.

The quantities use integer nanohertz f and centisecond duration c:
S0=sum c, S1=sum c*f, S2=sum c*f². The mean is S1/(10^9 S0), and the centered
sum is (S0*S2-S1²)/(100*10^18*S0). These are nominal-time receiver/reference
frequency statistics in Hz and Hz² times seconds. They are not a calibrated
force residual, a scalar-field energy, a physical noise estimate or an exclusion.

The independent decode/invariant run passed 22 recorded checks in 1.3196 seconds.
The subsequent source/result comparison passed 114 checks with zero failures.
Every result, the full independent chain timing ledger, boundaries and exact
sample moments are preserved. These counts describe consistency checks, not
independent empirical experiments.

## Preserved failure and limits

The author's v1 stderr records `ModuleNotFoundError: No module named
'cassini_odf_decode'` at its import, before observation processing. I inspected
that stderr and `SETUP_REPAIR_v1.json`. The v1-to-v2 source comparison confirms
only the repository-parent index and new-version output filenames changed.
The original failure is preserved; it is not relabeled as an executed v1 result.
The independent timing implementation had no failed attempt.

The author code records nonpositive durations separately if encountered; none
occurred here. Its generic edge label combines overlaps and duplicates, but the
independent raw interval reconstruction confirms neither occurs in this input.
This check is specific to the pinned product and does not claim that every
possible archive or instrument exhibits the same timing or overlap behavior.

Actual count-to-velocity calibration, physical clock transformation, direction
and worldline, source dynamics, media, reference ramps and error budgets remain
outside this inventory. There is no new physical fit or initial-state selection.
