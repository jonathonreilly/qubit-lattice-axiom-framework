# Bounded dynamic implementation and selected-endpoint review

No substantive implementation defect or correction request remains in the
specified scope. The complete C++, setup and dispatch sources implement the
declared finite full-matching generator, and all sixteen prospectively
selected endpoints pass independent decoding and Fourier reconstruction.
This review is separate from the earlier asymptotic proof assessment. It
does not assess the production aggregate results, their analyzer, a phase
claim, or formal retained/audit status.

## Read boundary and independent reconstruction

I first read the corrected transport note and dynamic protocol completely,
reused the earlier proof review at its verified identity, and derived the
rates, uniformization, conserved-key representation and six-field Fourier
signs before accessing dynamic author code or production data.
`PRE_COMPARISON_DERIVATION.md`, the independent control and its full logs
were sealed by `PRE_COMPARISON_SEAL.json`:

`fc1ee4425c5a37fe32980565e2704bfff827a0249b7f8bdffd93438378ff3e37`.

`ENDPOINT_SELECTION.json` fixed literal replicate identifiers **3 and 27**
in each N=16,32,64,128 by winding/irregular cell before implementation or
output access. Those identifiers correspond to the one-based replicate
field in the manifest, not array indices. No selection was changed.

The finite controls independently establish:

- The sharp integer-drive range h2 in [-4,4], actual rate
  c=(22+5h2)/40 in [1/20,21/20], reverse-drive sign and exact actual
  product-current derivative A_i/2. All 14^4 contexts for each positive
  axis were exhausted; negative axes reverse the drive.
- A separately assembled 24-state, four-position key-permutation chain
  is nonreversible with uniform invariant law. Its rational attempt kernel
  satisfies L=Lambda(P-I), Lambda=4(21/20). An 80-term Poisson mixture and
  a separately evaluated matrix exponential agree within 3.89e-16; split
  time intervals compose within 5.00e-16.
- Independent N=8 winding and irregular matchings give exactly 5K=1,280
  channels. The irregular fixture has only 1,104 unordered pair edges:
  deduplicating them would incorrectly change the process. Every context
  is distinct and both record displacements have lattice path length two.
- Exact symbolic current projection gives the Fourier generator
  E'=+(2i/7)Q cross B, B'=-(2i/7)Q cross E, with normalized initial
  covariance I_6. The transverse propagator blocks are
  U_EB=+i sin(theta) C_q and U_BE=-i sin(theta) C_q; both longitudinal
  components are static. The signed cross contraction in the sealed
  derivation equals +sin(theta).

These exact and numerical controls have different roles; the Poisson-sum
roundoff comparison is not described as an exact rational computation.

## Complete implementation inspection

The C++ stores a fixed geometry and a permutation of immutable pair keys.
Its six routing permutations, their inverse/context indices, fixed-point
omission and retained channel multiplicities match the supplied generator.
Every black site has one matched direction, leaving exactly five channels.
The implemented alphabet and tensor have the sealed signs and factors.

Each microscopic channel ceiling is 42/40. On an observation interval,
the Poisson mean is (5K)(42/40)N Delta t; each attempt selects a channel
with an unbiased bounded-integer rejection algorithm and accepts when a
uniform integer in {0,...,41} is below 22+5h2. An accepted event exchanges
keys, including distinct keys with the same color. The color lookup never
changes. `accepted` and `color_changes` correctly distinguish those events.

For the declared sizes and times, the means per interval are exactly
75,264; 1,204,224; 19,267,584; and 308,281,344. The counter types cover
these values and accumulated counts. Ideal Poisson uniformization gives
the exact CTMC observation law. This does not remove finite-arithmetic
or pseudorandom-generator qualifications in a computer implementation.

The observer sums exp(-2pi i coordinate/N) at the **black pair positions**
and divides by sqrt(K). The stored six fields are the unscaled X,Y,
not E=sqrt(7)X and B=sqrt(7)Y/2. The declared analysis scaling must therefore
be applied afterward. No site/pair factor, Fourier sign, or observation-time
mismatch was found. The protocol correctly keeps all modes and times from
one history together as the statistical sampling unit; its future analyzer
was not read or checked in this task.

The setup source uses maximal +x winding or ordinary x-columnar geometry
followed by exactly 8N^3 uniformly proposed plaquette flips. Its irregular
fixture gate rejects zero accepted flips. The production manifest contains
the prescribed 960 distinct jobs and seeds, with 256,128,64,32 histories per
geometry at the four sizes. I authenticated these declarations and all eight
geometry files and independently verified their matching, routing and
four-position context properties. I did not replay all production geometry
flip proposals or treat the irregular fixture as an equilibrium sample.

The dispatch wrapper authenticates its declared inputs, keeps all jobs,
retains per-job stdout/stderr and receipts, and records explicit failure or
deadline statuses. It does not select by the measured outcomes. This review
confirms sixteen selected completed receipts; it does not independently
certify completion or payloads of the other 944 histories.

## Small implementation traces

`check_instrumented_events.py` creates two independently chosen N=8 fixtures
and compiles a copy of the frozen C++ with only three logging insertions.
It writes the complete channel catalog and records the already-required
channel and acceptance draws, without adding RNG draws. The exact text
insertions and source identities are retained in
`small_event_controls/INSTRUMENTATION.json`.

The instrumented and frozen production binaries, run with the same small
fixtures and seeds, agree byte-for-byte on final state files and exactly on
RNG state, counters and all five stored snapshots; only wall time is ignored.
The independent decoder reconstructs both full 1,280-row catalogs. It then
checks every logged attempt against its own evolving key permutation,
features, context drive, rate numerator and acceptance threshold.

There are 225 winding and 224 irregular attempts, with 109 and 115 accepted
events. Seven and three accepted events, respectively, exchange different
keys of the same color; those physical moves are correctly retained.
Independent FFT reconstruction of all five small-run snapshots agrees
within 4.97e-16. This is a bounded event-level validation, not replay of
any production trajectory or a general statistical audit of the RNG.

## Selected production endpoint reconstruction

Only the sixteen preselected binary states were decoded. The script first
reconstructed their results without opening their history JSON or receipt
payloads. That output and the decoder were separately sealed by
`SELECTED_RECONSTRUCTION_SEAL.json`:

`0ea9a06a72d246d5025f89266ddc0a9d6a667e15a69555ddf29acdf385885bb4`.

For every selected state, the checks cover all keys and the complete fixed
color lookup, not a prefix. A separate integer implementation of the seeded
initial color generator reproduces every lookup entry. Across the selection,
4,792,320 pair keys and 9,584,640 physical record identities are checked.
Each final key array is a permutation; color counts are conserved; assigning
record IDs 2k and 2k+1 to the two endpoints preserves both distinctness and
the antipodal partner involution. The test concerns abstract immutable keys
and their finite-color projection, not unsampled physical qubit states.

Initial and final vector fields are reconstructed through integer
coordinate/color histograms followed by a one-dimensional FFT for each
axis. This differs from the simulator's sitewise complex summation and
from the setup helper's phase-weighted color sums. Comparison afterward
against the selected saved fields gives maximum complex error
**5.6504244306134954e-14** across all sizes, both endpoints, all three modes
and all six components. The selected results' source/job identities,
time grid, parameter values, channel/count flags and complete payload
hashes match their receipts; all selected stderr files are empty.

The intermediate production snapshots have no separately saved intermediate
key arrays and were not independently reconstructed. Endpoint conservation
does not prove every unobserved move was valid. The small logged controls
provide the separate limited event-level evidence described above.

## Source provenance and limits

Complete current primary source identities:

| Source | SHA-256 |
| --- | --- |
| Corrected transport note | `dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873` |
| Dynamic protocol | `d8cbfed1ba55a4a11048c7d68135f0ee7f6d0c98c38dc685e43bb43ead90952d` |
| C++ implementation | `473e2981132f06bbf1fcf5f1b4dbf28e004d391485dc468d4dd93cc7c63f9dcb` |
| Setup | `ef662a36150dd8db8ea6831062c4f18cbb11b95397056c7e5fa16b60343b50dd` |
| Dispatch wrapper | `ba650514d868c9fa6b6e4d023534243d99a78f19221c19a3a4276f82faa1c46b` |
| Frozen production binary | `4e00276a24fe77c1a6aa899aafeeff86eb0d7b8b271637695c2289cc19d18131` |
| Production manifest | `4db87d1484554a0173ca07a43c82fdd6148604416b2674da7fe7a57b930acc00` |

The dispatch was frozen before the gamma-scope prose correction. Its
construction identity is the original `5fd0f707...691f479`, authenticated
against both its frozen snapshot and the preserved reviewed note. The
already sealed F1 acknowledgment establishes the sole difference from the
current note. Since this screen fixes gamma=1, that qualification changes
neither its generator nor its targets. This is a historical source binding,
not a newly refreshed manifest or an unexplained identity mismatch.

The complete paths, byte counts and hashes, including selected endpoint
payloads and small-control files, are in the final source manifest and seal.
All independent checks completed on their first execution with empty stderr;
there are no failed attempts or changed selections to omit. Earlier review
packets and primary/production files were not modified.

For reproduction, use a fresh sibling evidence directory under the same RAW
parent: copy the four Python check/decoder files and `ENDPOINT_SELECTION.json`,
then run `independent_precheck.py`, `check_instrumented_events.py`, and
`check_selected_endpoints.py reconstruct`. Seal that fresh reconstruction
before `check_selected_endpoints.py compare`; the required seal is simply
the `artifacts` identity list shown in the preserved selected reconstruction
seal. The scripts deliberately refuse to overwrite their small-run directory.
Do not rerun into this sealed packet. All actual commands, stdout, stderr
and execution receipts from this review are preserved.

No aggregate outcomes, production analyzer, confidence intervals, monotone
finite-size trend, thermodynamic conclusion, quantum realization or
propagating geometric Gauss field was inspected or inferred.
