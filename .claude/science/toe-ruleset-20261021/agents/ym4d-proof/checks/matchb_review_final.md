# MATCHB affected-fix confirmation — 2026-10-30

**LAND for the stated partial and conditional results. Binding fixes:
none.** Both binding findings in the [initial review](matchb_review.md)
are repaired. The actual history-uniform pinned estimates, cumulant
smallness, quantitative regeneration and subsequent RG estimates remain
OPEN. This is a review disposition, not an actual-model GO, audit verdict,
retained-grade promotion or git landing.

This is confirmation by the same independent reviewer in the same review
session. The initial review was fresh-context, same-family Codex review;
no different-family independence is claimed. I reused its independent
derivations for unchanged arguments and checked the actual source diff,
the affected statements and their downstream normalization/support uses.
No subagent contributed and no numerical computation was performed.

The confirmed `MATCHB.md` has SHA256
`40fc8888735639281dab191124bcacd866b3f5afaf53329d3ddf6ee481cc04d9`.
All line references below refer to this version.

| Finding or interaction | Confirmed source | Disposition |
|---|---|---|
| B1: full versus incident-factor normalizer | 94–127, 151–199 | RESOLVED. MB4 names the full normalizer; the incident product, exterior factor and local normalizer are separately defined. MB7's incident-score estimates now apply to Z_C^loc. |
| B1: ratios and replacement accounting | 212–249 | RESOLVED. MB8–MB9 compare local normalizers, while full ratios retain the exterior ratio and its derivatives/readers. |
| B1: propagation into the next-step obligations | 578–594 | PASS. MB29 identifies local normalizers and separately requires full-reader exterior score/log budgets for full comparisons. |
| B2: connected decorated supports | 332–350, 384–409 | RESOLVED. H and every H_G must be nonempty connected complete cores; an added connected hull is paid at its actual size, including in d. |
| Support-rate clarification | 333, 438–465 | RESOLVED. Nonnegative sigma is explicit both in the comparison input and the cumulant theorem. |
| Unchanged cumulant gas, exact recursion and regeneration diagnostics | 414–574, compared with the initial source | PASS retained. The substantive arguments are unchanged; the initial independent reconstruction remains applicable. |
| Scope and remaining obligations | 575–601 and final status discussion | PASS. Exact ancestry form does not become quantitative closure, and the sign examples remain general-inference diagnostics rather than gauge counterexamples. |

For B1, on every positive fiber the new definitions give exactly

    w_h = F_ext q_C,
    Z_C^full = F_ext Z_C^loc,
    gamma_C = q_C/Z_C^loc.

The Bell-polynomial argument now differentiates the integral of precisely
the weight whose scores are bounded. The original counterexample
`w_h=exp(A y)` has `q_C=1`, `Z_C^loc=1` and `F_ext=exp(A y)`: the zero
incident-score array correctly bounds the local quantities, while the
full log derivative A is retained separately. Pinning still restricts a
uniformly supplied fixed-support score bound; it creates neither a
rare-mass inverse nor derivatives of moving selectors.

For paired full normalizers the exact relation is

    Z_C^(full,+)/Z_C^(full,-)
      = (F_ext^+/F_ext^-)(Z_C^(loc,+)/Z_C^(loc,-)).

Thus the revised local ratio and reciprocal-derivative estimates no
longer omit an exterior factor. MB10 explicitly assigns changed exterior
factors to that separate ratio. MB29 then preserves this distinction at
the next step instead of treating local normalization as payment of the
full comparison. MB3's separate R_h/Z_A is unchanged.

I also checked the separator interaction: allocate factors as
`w_B(eta) product_i q_(C_i)(x_(C_i),eta)`. Its interior integrals are
`Z_(C_i)(eta)=int q_(C_i) dx_(C_i)`, the local normalizers in the new
notation. Substitution gives MB11's lambda and conditional product
exactly. The formula does not multiply the full fiber normalizers, which
would also contain other interiors' factors. Outer separator dependence
and its derivatives remain present.

For B2, the zero-attachment term now has connected support H. Every
surviving attachment K is connected and meets H by the matching condition,
so every union Y is connected. The actual hull size is retained in the
per-core exponential and the definition of d. Therefore the original
derivation of MB20 and the core-root/tail-root estimate
`(1+2 eta)d` applies without changing its constants. The explicit
`sigma>=0` also justifies each union-support weight comparison in MB20
and MB24. No spatial-overlap exclusion was added to the cumulant gas:
its compatibility remains exactly disjointness of the atom-label sets.

The initial review's smallness and regeneration qualifications remain
binding scope. The constant in MB24 is proved only under its supplied
full differentiated cumulant budget. Producing that budget for the actual
law, obtaining common bounds before history sums, paying full comparisons
and reproducing support reserves are still OPEN. No estimate for those
objects is obtained from the sign diagnostics or from this review.

Source preservation was checked directly. The archived first draft has
the original SHA256
`9f5fb403665e154c54427b2cfca25e2387357a2ea96b4706bb532a36352b7e54`.
The initial review remains unchanged at SHA256
`bd891f9cf2aee69a54580e497fb82826ed1db520201cf028d981896d308db4df`.
The saved fix diff has SHA256
`240c650b79dbb6ae0ace70daf3f3a5e758bec3f4739b0bdfdced1f3c9deab3e2`;
an independently displayed diff of the archived draft against MATCHB
contains the same narrow fixes. The hashes of REFMATCH, its review,
MIXSMALL, REALRGA, REALRGB, JMBRA and LIB1 still match the initial report.

The author receipt was read: it says `NOT RUN`, has an empty check list,
and records a preflight stop at available-memory fraction
`0.2461223602294922`, below the registered 30% threshold. Its proof hash
is the original draft, and it supplies no numerical validation of either
version. No test was rerun or guard weakened for this confirmation.

Only this new `checks/matchb_review_final.md` is written. The original
review and all other files are preserved; no commit is made.

VERDICT: LAND
