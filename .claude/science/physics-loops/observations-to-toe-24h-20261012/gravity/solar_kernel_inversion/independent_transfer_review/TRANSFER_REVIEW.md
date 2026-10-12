# Independent narrow extension-transfer review

Reviewed 2026-10-12. Parent is the scientific author. No material implementation
or mathematical error was found in the pinned protocol and transfer script.
The complete source and protocol were read, relevant pinned geometry helpers
were rechecked, and the staged execution was exercised with synthetic fields
and synthetic targets. This is not a formal audit or an empirical transfer
verdict. No actual galaxy field was computed, campaign target array opened,
response refitted, author file edited, or parent-owned session3262 touched.

## Source identities and fixed inputs

| Subject | SHA-256 |
|---|---|
| FROZEN_EXTENSION_TRANSFER.md | `0bb46c333a089440082fe38ace469f2a35bea4c0e0c469c3abb022741e804265` |
| direct_extension_transfer.py | `d29a6e9d6d6e00399eefaf28f4ef925ed1db650c01a63fa34bfd062914a771ab` |
| Runtime extension_transfer/FREEZE.json | `1dae3e3888f82c2ced9e07253dcf520bcf744e43e5a31c9e9849618703c90b1f` |
| Original six-fit receipt | `6b0528745ba0e3ebdc081678821355e54d0d41d8e787cf0e904099942926bcb1` |
| Separate margin candidate receipt | `ffa93f9ad0f8a412020eb756bbc996c07caa1b55a4269cbfee865aa7af591ebc` |

The freeze records 2026-10-12T20:38:08.485534 UTC and embeds both full weight
vectors. They agree exactly with the original D_galaxies_external_solar
candidate and the separate margin candidate. Their common Newtonian external
E remains 1.4915242022774435e-10 m/s². There is no optimization or external-field
rescan in the transfer. The source, protocol, operator, boundary validator,
candidate receipts, source and target data identities, original selection,
margin protocol, and six prior source receipts are frozen. The field solver
and inverse protocol are additionally pinned by the operator guard.

The ordered sources agree exactly with the original source-selection receipt,
recorded at 19:01:36.861614 UTC: NGC3949, NGC3972, UGC06667, UGC08837, DDO064,
DDO168. Their processed scored row counts in the existing field receipts are
6, 9, 7, 7, 12, 9. Fresh hashes of all six source receipts match the transfer
freeze. Each names solver SHA
`701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00`
and source NPZ SHA
`217bd10ba3fa8f9972d047081342c023ee7524c16b6d8c685d6d9fa49fd2959f`.

The frozen identities and source-loader code preserve the 64-ring source
profiles, prior stellar ratio U, smoothing width, vertical height, scored
radii and masks, and previous isolated-field domain. The geometry helper
uses the previous source receipt and source NPZ, never a new velocity fit.
The target NPZ identity is carried from the freeze and earlier review; this
review did not reopen its arrays. Ordinary receipt timestamps are a record
of ordering, not a cryptographic proof that no other computation occurred.

## Field stages and prerequisite gates

The original candidate's three-source numerical pass and the margin candidate's
full numerical/rectangle pass are required at source lines 60–65 before either
field stage. Each prerequisite must identify the exact frozen fit or margin
receipt. This matches the protocol: the original candidate's tiny direct
rectangle allowance is not silently made a new acceptance gate or repaired
by changing its weights. That allowance remains in its original result.

Stage1 uses the same base Newtonian geometry for both response projections.
It checks the Newtonian projection against the stored midplane source field
to 0.003 and the previous response against the preserved full Poisson force
to 1e-10. Base forces are marked provisional. There is no target-array access
in this branch or in its geometry helper. `identities()` does hash the target
file's bytes; the narrower claim “no target array read” is accurate. The
candidate vectors are loaded from pinned receipts, checked for shape and
finite nonnegative values, and compared byte-for-byte before each source
receipt is saved.

Stage2 reads each source's prior base forces and verifies the base geometry
hash and radius alignment. It evaluates both response vectors on that
source's doubled radial/angular grid and on the existing boundary extension.
The pinned helpers double nr, nc and lmax for refinement. The boundary helper
preserves interior radii and source vectors and extends both domain ends by
two, as checked independently in the earlier static-validator review.

Finite positive base/refined/boundary forces are required separately for each
candidate/source. The relative denominators are the same candidate's base
force. The refinement limit is 0.005 and boundary limit 0.003. Failed numerical
gates are stored as `passed: false`, with their actual forces, and execution
continues through both candidates and all six sources. It does not borrow
the old response's convergence or select a candidate from extension residuals.
Source-control or provenance assertion failures instead stop execution;
these are integrity failures, not stored numerical gate failures.

## Scoring and units

Scoring first loads all six stage2 receipts and checks their freeze and input
identities. Only after that loop does it open the source mask and target
arrays. Each scored radius must match the stage2 radius exactly. Positive
finite observed V and nonnegative finite processed errors are required.
The same mask indexes R, V and error; no residual-dependent exclusion occurs.

In the inherited field units, F and A = V²/R both have units (km/s)²/kpc.
Thus predicted velocity is sqrt(R F) in km/s, and the velocity log residual
is exactly 0.5 log10(F/A). Independently solving the relaxed inequalities
L_i - t A_i <= F_i <= H_i + t A_i gives

    t_required = max_i max(0, (F_i-H_i)/A_i, (L_i-F_i)/A_i),
    L_i = max(0,V_i-2 error_i)²/R_i,
    H_i = (V_i+2 error_i)²/R_i.

Lines 140–156 implement these formulas for base, refined and boundary fields.
Finite nonpositive forces retain their rectangle allowance but receive no
real circular-speed or log score. A nonfinite force produces null rectangle
and velocity summaries for that method; the individual forces and numerical
failure remain available in the stage2 receipt.

For each candidate and method, the aggregate RMS is
sqrt[(1/6) sum_g RMS_g²], giving each of the six galaxies equal weight despite
unequal scored row counts. The aggregate rectangle allowance is the maximum
over galaxies. Null summaries propagate rather than dropping a failed source.
Each candidate's aggregate numerical flag is the conjunction of its six
source flags. Descriptive scores can still be shown when that flag is false;
the result explicitly qualifies them. The comparison is not certified merely
because the script completed.

## Resume behavior and synthetic evidence

Every entry through main checks the full current input identity dictionary,
the six names and both vectors against the freeze. Completed per-source
records can be skipped only when their freeze SHA and identities match.
New records recheck identities and weight bytes before saving. Stage2 records
also carry the exact base-receipt hash and refined/boundary geometry hashes.
The geometry helpers separately validate cached identity and cache bytes.
Output records are not overwritten. Resume covers complete records; an
incomplete or malformed JSON record is refused by the parser rather than
silently reused or overwritten.

`check_transfer_synthetic.py` loaded the pinned subjects with actual RingField
construction trapped. Its NPZ loader only allowed files in the review fixture
directory. The author stage/readout code ran on toy fields for the same six
names, synthetic masks and targets, and the exact two frozen weight vectors.
Independent scalar-loop calculations supplied score expectations.

All controls passed:

- Missing original/margin prerequisite files stopped the field stage before
  geometry or target access. Premature scoring stopped before target loading.
- A synthetic interruption after two complete base records preserved them.
  Resume computed only the remaining four. Stage1 and stage2 made zero array
  loader calls in these mocked-field fixtures; helper source inspection
  separately confirms that real field construction reads only source arrays.
- A complete rerun of both field stages made zero geometry calls and left all
  twelve source records byte-identical.
- Candidate-specific nonpositive force, NaN force, excessive refinement
  change and excessive boundary change were retained as four separate failed
  candidate/source pairs. Both candidates were still evaluated on all six
  sources, including the final two healthy sources.
- All 36 successful projection calls received the exact frozen weight bytes.
  A deliberate runtime weight mutation was rejected before the first source
  record could be saved. A changed candidate-file identity and a stale resume
  freeze hash were also rejected.
- The six synthetic row counts were 2, 3, 1, 4, 2, 3. Deliberately invalid
  unscored target rows were masked out. All per-method velocities, rectangle
  allowances and equal-galaxy RMS values agreed with independent calculations.
  A positive allowance of 9.99866855977416e-13 remained positive. Nonpositive
  and NaN cases produced the intended null summaries, with no source dropped.

The synthetic run completed in 0.449 seconds with approximately 84.4 MB peak
RSS and numerical thread counts fixed to one. The primary evidence is runtime
`synthetic_transfer_checks_v1.json`, `provenance_checks_v1.json`, the preserved
fixture outputs, and `transfer_review_receipt_v1.json`, under
`gravity/response_inverse/extension_transfer/independent_transfer_review`.
All pinned author sources and original receipts remained unchanged at the
final checkpoint.

This disposition establishes the checked implementation behavior, not actual
candidate convergence, transfer agreement, a full-family exclusion, nuisance
likelihood, pressure correction, or dynamical completion. These are previously
exposed out-of-fit development objects. No full-sphere theorem validation is
claimed. The parent must interpret the actual prerequisite and transfer
receipts; none was manufactured or replaced in this review. The original
campaign deadline and stop markers were checked, and ownership was unchanged.
