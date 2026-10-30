# Squared-alignment price: author checks and handoff

This is an author reconstruction, not independent review. No scientific
numerics, symbolic-evaluation runner, worker, Git mutation, PR action or audit
was used. The source was frozen before this compact metadata was written.

## Prior-art disposition

The proposed inequality is exactly CS10 rearranged. OC3 already consumes it
for all-compact free-link control. A broader search then found that
REVIEW55_ARS r55a-F10 already proves the precise proposed linear threshold
and the stronger gap epsilon^2/(256N). CODEX_REVIEW_KN F4 gives the same
trace-difference mechanism at a weaker threshold. These are matching prior
results, not new discoveries in this unit.

JMBRB B13--B18 still uses the weaker separate trace errors. Its description
of that particular quadratic-threshold estimate is true. This note recovers
the stronger existing result for that consumer and writes the explicit
simultaneous coarse-curvature energy allocation. No claim of global novelty
or exhaustive prior-art search is made. HW's cone minimum bound has separate
conditional multilevel hypotheses; it is not imported here.

## Analytic checks performed by the author

1. Exact chord identity, weighted Hilbert Jensen, and Young's inequality give
   SAP3, while the intermediate inequality gives SAP4. Every conversion
   between normalized HS, HS and operator norm is stated.
2. Actual paired paths have at most 3(L-1)/2 transverse axial steps, each
   sweeping L fine plaquettes. The sharper A_L replaces CS's conservative
   general-loop bound only for these explicitly paired ribbon fillings.
3. The root squares have incidence one; coarse positive links have six
   incident plaquette labels; lifted two-block bricks have fine-plaquette
   incidence at most eight. The far periodic seam is excluded at T=2, while
   opposite labelled faces remain distinct. Readers of the complete words,
   normalizers, source coefficients and square fillings all remain.
4. At eta_lin, the operator mismatch is at least epsilon/8 and the normalized
   mean-square path error is at most epsilon/(32 sqrt(N)); this is one quarter
   of the guaranteed normalized mismatch. SAP4 therefore retains the original
   epsilon^2/(256N) gap. Strict and non-strict versions are both recorded.
5. The five-term Cauchy bound gives coefficients 10L^2,20,40 A_L^2 before
   summation. The one/six/eight incidences yield 10L^2+1920 A_L^2 and120.
   Nonnegative source-weighted bare Wilson and centered kernel energies then
   give SAP15--SAP17 for arbitrary compact U,V, with no branch selection.
6. The finite matrix-entry Haar cover is rebuilt. Its forward probability
   statement expressly requires t>=1 and smooth input on the full F_A.
   Product independence belongs to output links, not coarse plaquettes or
   future-conditioned fields.
7. SAP18 factors off an arbitrary fraction theta in (0,1), retaining the
   remaining positive fraction of every charged numerator and every original
   Ntilde_t. No replacement of t in a normalizer occurs. SAP19 retains the
   unestimated remaining integral divided by the actual reference.
8. RENEW's persistent rough orbit is compatible with the one-time original
   Wilson charge. No uniform renewal, effective-density coercivity, matched
   reference, complex normalized return, nonlinear RG or physical gap is
   concluded.

The source was read completely in two bounded reads. Before freezing, the
author clarified the t>=1 condition, removed an accidental suggestion that
q_geo is positive whenever q_gap is merely positive, and required the real
multiplier H in the pointwise inequality to be nonnegative. These were author
edits before review; no predecessor source changed.

## Mechanical check and next action

The source-freeze record binds its exact SHA256, bytes, line count, UTF-8
decoding and eight existing relative links. These checks say nothing about
proof correctness. The read manifest identifies the exact source ranges and
search limits. The receipt binds this five-file author packet.

A different fresh reviewer should read the complete frozen SAP1--SAP19 source
and reconstruct the ribbon/square/brick incidences and normalizer allocation.
The consumer after review is LFPRICE clause2's actual matched-reference
integral, with its other clauses and RENEW-MATCH still open. Full SU(N), d=4
existence and physical continuum mass gap remain OPEN.
