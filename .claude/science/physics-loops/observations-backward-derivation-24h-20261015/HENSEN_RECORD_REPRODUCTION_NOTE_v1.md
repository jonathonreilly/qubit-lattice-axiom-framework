# Deposited Bell records: fixed-selection reproduction

Personal author: /root, 2026-10-16. Status: conditional-support.
This is an exposed-data reproduction, not an independent empirical test of a
new theory. The aggregate 245 trials, 196 wins and published significance were
known before the archive was downloaded. The pre-download scope is frozen in
HENSEN_DATA_INTAKE_PLAN_v1.json. No record-order search or fitting was performed.

Source: [Hensen et al. 2015 dataset, version1](https://data.4tu.nl/articles/_/12703235/1),
DOI10.4121/uuid:6e19e9b2-4a2d-40b5-8dd3-a660bf3c0a31.
The public 152913-byte data.zip matches the repository's displayed MD5
342f29f8288c46575818acd2acebd535; its SHA256 is
c28eb0f075759aef620a0b2e00a70fd675ce712bc8214d11c103f5a3d29492c0.
Every member hash is in HENSEN_RECORD_REPRODUCTION_v1.json. The data are kept
outside the repo; the original parser/example was read as source material,
not executed. The complete README text and ODS header were read. The 4746-row
CSV was parsed with a new standard-library row-based implementation.

The deposited example fixes the herald windows at channel-dependent starts
5426350 and5425700ps, length52450ps, separated by250000ps, and requires distinct
herald channels. It also applies the specified preceding-invalid-marker and
no-early-excitation-click filters. The local readout window is (10620,14320]ns.
These are adopted calibration/selection inputs, not inferred here. We did not
scan any threshold, change an output label, select a favorable time interval,
or independently re-establish their physical causal ordering.

Successive selection counts are4746 original rows,361 within the original
herald gate,248 also satisfying the invalid-marker condition,245 also lacking
the stated early excitation clicks. There are196 game wins. Setting rows00,01,
10,11 and outcome columns++, +-, -+, -- give respectively

    [23,  3,  4, 23]
    [33, 11,  5, 30]
    [22, 10,  6, 24]
    [ 4, 20, 21,  6].

They yield S=2.42249987046. The original iid-style descriptive error formula
gives0.20382659825; this formula is not used to certify an adaptive-memory
null. The game statistic8*(196/245-1/2)=2.4 differs because setting counts differ.

The deposited original script uses q=3/4+3*(tau+tau^2), tau=1.08e-5, giving
fixed-horizon tail0.03917464356. The tighter conditional-independent-input
bound derived in block08 uses q=3/4+tau-tau^2 and gives0.03910997241. With ideal
uniform fresh inputs the tail is0.03907767139. These are distinct declared
bounds, all rounding to the paper's0.039; the latter two must not be silently
substituted for the original deposited calculation or its assumptions.

The result matters to the neighborhood hypothesis because the causal-game
bound permits arbitrary history and adaptive changes between trials. An
account using only old local memory still faces this observation under the
stated current-input independence and causal-factorization conditions. A
proposal changing those conditions needs a concrete physical mechanism and
predictions. This reproduction does not exclude every evolving network,
prove latent independence from marginal randomness, certify apparatus timing,
or supply a new empirical rejection. It checks the data-to-counts bridge and
preserves the distinction between that bridge and the physical premises.

Reproduce with Python3/mpmath and the exact archive downloaded from the dataset:

    python3 reproduce_hensen_records_v1.py --archive /path/to/data.zip --output /path/to/result.json

The runner refuses a different archive hash. Its own hash and member hashes
are in the output. The120-second bounded receipt completed successfully;
source download fallback and missing-bs4 recovery are recorded in the intake.
The earlier block08 statement that raw data had not yet been opened describes
its frozen earlier scope; this later analysis now exposes the deposited data.
