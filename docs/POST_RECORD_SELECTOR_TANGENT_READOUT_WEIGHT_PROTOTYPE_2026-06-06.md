# Post-Record supplied finite weights and quadratic-form diagnostic

**Date:** 2026-06-06; scope separated 2026-10-24
**Type:** open_gate
**Claim type:** open_gate
**Status:** conditional supplied-data diagnostic; no status promotion
**Primary runner:** [finite diagnostic](../scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py)

## Supplied mathematics

Take a finite carrier with nonnegative rational weights and positive total.
For `W=sum_i w_i>0`, define `p_i=w_i/W`. Then `p_i>=0` and
`sum_i p_i=1` by distributivity. This arithmetic does not derive the carrier,
weights, readout context, probabilities or physical realization. The runner
keeps exact Fraction examples `(1,3)->(1/4,3/4)` and
`(1,15)->(1/16,15/16)`, and rejection of a negative supplied weight. Its
normalization function rejects nonpositive totals; this is a required premise,
not an inferred normalization law for nature.

For a symmetric real 2x2 matrix `M=((a,b),(b,d))`, positive definiteness is
equivalent to `a>0` and `ad-b^2>0`. Indeed
`x^T M x = a*(x1+(b/a)*x2)^2 + ((ad-b^2)/a)*x2^2`, which is positive for
nonzero `x` under these hypotheses. Conversely, positive definiteness gives
`a>0` at `(1,0)` and `(ad-b^2)/a>0` at `(-b/a,1)`. Thus the two scalar
conditions are equivalent only with the stated symmetry premise.

The supplied fixture `((3,1),(1,2))` has determinant `5` and quadratic value
`9/2` at `(1,1/2)`. The original determinant-only helper omitted symmetry.
Preserve its decisive counterexample `M=((1,10),(0,1))`: the old two conditions
hold, yet `(1,-1)^T M (1,-1)=-8`. The corrected helper explicitly requires
symmetry and rejects this matrix. It does not generalize the finite examples
to a derived physical metric or Hessian.

Two Boolean flags classify supplied examples: the string
`conditional_selector_ready` is returned when both flags are true, otherwise
`blocked_missing_selector`. These are stipulated labels. In particular,
`bool(weights)` certifies neither a physical selector nor a general weighting
construction. The two original finite Boolean predicates remain, labelled as
classification checks rather than authority.

## Physical and documentary boundary

The carrier, weights and symmetric metric are assumptions. They are supplied finite packet data.
This diagnostic is not selector/tangent/readout authority and does not derive selector/readout/tangent authority from Record.
Does not derive a selector, a tangent metric, a Hessian, a Born law or a physical
measure. Record-derived selector/readout/tangent authority remains open.
These statements delimit this construction; they do not prove that a larger
framework cannot supply such structures.

The [conditional quartic bridge](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)
supplies a separate positive quartic law and explicitly leaves physical
interpretation open. The runner reads that scope as documentary context, not
as a physical readout theorem. The finite weight/metric calculations import
no theorem or data from that bridge. Constant-false firewall declarations are
unscored information; no PASS is awarded merely for disclaiming authority.

## Historical census disposition and recovery

No current ledger census is performed or claimed. The historical 17-row census
was a different documentary contract, dependent on the genuine old
`docs/audit/data/audit_ledger.json` and the measure subdivision helper. That
ledger is absent at this source. No replacement, status repinning, successful
census or audit verdict is supplied. The old note's 12-row statements, later
17-row runner constant, stale source needles and reported prior failures are
preserved without reconciling them into fabricated success.

The complete original note, runner, cache and imported helper source are
byte-preserved as historical text under
`archive/source-history/selector-weight-census-withdrawal-2026-10-24/`, with `manifest.json` recording original paths, source commit and
SHA256 hashes. These copies are outside active note/runner discovery and are
not current primary evidence. The original commit also preserves the full
repository context needed to investigate the missing-ledger route. The live
measure helper remains unchanged for unrelated consumers, but is genuinely
unused and unimported by this finite default runner. No optional census is
executed from this packet.

## Verification boundary

The seven original finite predicates are retained, with the SPD helper's
necessary symmetry correction, plus two exact counterexample controls. Text
checks bind only the documentary scope. A literal120-second future cap and the
two actual note inputs are declared. This revised source awaits independent
argument/source confirmation and a fresh capture; the old cache is historical
until replaced by that actual run. It is not an audit or whole-packet approval.
