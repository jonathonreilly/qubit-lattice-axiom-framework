# Pack-family hazards for the audit lane (packsci01-05 triage, 2026-08-06)

Date: 2026-08-05 (part-2 ship 2026-08-06; header added by review-loop regeneration 2026-08-08)
Authority: none
Audit: unset
Claim type: meta
Status: routing guidance, non-evidentiary. This memo carries supervisor triage
hazard notes for the audit lane about rows NOT pulled into intake. It asserts
no claim, confers no verdict, demotion, or effective status, and must not be
consumed as evidence; each entry is provenance pointing at the named surface,
and substantive corrections require their own auditable claim rows.

Provenance (evidence base, pinned):
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/branch09.jsonl` (byte-exact copy of triage_2026-08-05/extracted/branch09.jsonl) — sha256 `4cdd06f9f285fde1bf12e21f0e78de5750fb68035b072555a68520ece7156ebc`
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/packsci01.jsonl` (byte-exact copy of triage_2026-08-05/extracted/packsci01.jsonl) — sha256 `a452f9109ca370f409ffcbdc99fe7733754cc602a39af67c10128b3b9b460d4a`
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/packsci02.jsonl` (byte-exact copy of triage_2026-08-05/extracted/packsci02.jsonl) — sha256 `61c69c2faaca710454a86a5639bf5f28cf2aab6c24a9c626495ce2d6ccb986d9`
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/packsci03.jsonl` (byte-exact copy of triage_2026-08-05/extracted/packsci03.jsonl) — sha256 `180cb0c6d9c0d89fce7a16acb431057121328eb2707b5d9dc47ec0e87397d043`
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/packsci04.jsonl` (byte-exact copy of triage_2026-08-05/extracted/packsci04.jsonl) — sha256 `56226cac23f927c77469ca11f1d37ecba9cad6c48150271dee32e7ba5761aa33`
- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/packsci05.jsonl` (byte-exact copy of triage_2026-08-05/extracted/packsci05.jsonl) — sha256 `46d1b2fe48621b2e164e07c5065b36dfa6218ae9754bb612b18d16f9bafce62d`
- The per-hazard `idx` pointers below refer to rows in these archived
  extraction files and to `triage_2026-08-05/manifests/<stratum>.json` in the
  census worktree.

Items NOT pulled into historic intake (they concern LANDED rows or live lanes),
recorded here so the audit lane sees them when it touches the named surfaces.
idx numbers refer to triage_2026-08-05/manifests/packsci0N.json.

## packsci01 (idx 10000-10309)
- 10111: the landed AXIOM_FIRST_GENERALIZED_SECOND... (GSL) note's formal
  review-loop was DEFERRED to integration time; audit it as unreviewed, not as
  review-passed.
- 10261: landed DM m_DM = N_sites*v = 16v ~ 3.94 TeV row is a
  numerical-coincidence promotion (bounded support, explicitly not
  theorem-grade); audit the coincidence framing.
- 10263: landed string-tension "retention" is retention-with-budget - the
  retained label was obtained by widening the error budget to +/-5%; B2 needs
  N_f = 2+1 dynamical lattice MC.
- 10264: landed Lambda_vac = 3/R^2 budget: the only content that would make
  Lambda a prediction (R2, the numerical R) is unresolved and closes only via
  Axiom* or acceptance.
- 10269: two headline-looking numbers in the landed row are NOT derived
  (coupling hypotheses H2-H4 remain open imports).
- 10067/10092: charged-lepton and neutrino cycle reviews were EMULATED
  review-loops (local stances), not the owner lane; treat as unreviewed.
- 10088 (also pulled): authority runner had gated on the literal string
  "Pfaffian"; check sibling runners for keyword-gating.

## packsci02 (idx 10310-10619)
- 10340: four supplied conventions carry owner-signoff provenance where the
  signoff was shaped by the requesting process; check provenance wording when
  the D1-D4 conventions are cited as owner-ratified.
- 10366: a prior Coulomb row over-read landed content (full atomic-stability
  theorem reading); the over-read is documented in-branch.
- 10368: two recurring laundering patterns named for the charged-lepton
  open-gate map (map-as-derivation; Q/delta/sign from the map alone).
- 10407/10408: dm_leptogenesis transport row has 246 descendants; the interval
  witness shows the imported transport functional CROSSES eta/eta_obs, and the
  row self-declares a numerical-match hazard.
- 10418/10419: dynamics/records campaign packs document a real grounding error
  and a review-caught universally-phrased overclaim (both repaired in-pack);
  the pass-after-repair totals are supervisor re-runs.
- 10429: a previously reported T -> 0 continuum reading on the retained-bounded
  Richardson diagnostic is unjustified on the tested sequence.
- 10441: a runner NAMED for uniqueness refutes uniqueness by its own multiple
  solutions; do not cite it as a uniqueness proof.
- 10447/10609: fragility class - retained rows whose evidence scripts are
  attached to OTHER rows (mutating the script silently changes both).
- 10454: alpha_3/alpha_em = 9 is suggestive-looking and formal assumed-input
  only; not a prediction.
- 10466: an arbitrary-data lemma was missing the z_(0,0) != 0 hypothesis
  (now explicit in-branch); check consumers that cite the unconditional form.
- 10472: catalogue of eight known-false or over-strong plaquette assertions
  that read plausibly; useful as an anti-citation list.
- 10480: cluster-cap PROCEED record flags a landed theorem whose grounds
  overlap the reopening basis; check independence when both are cited.
- 10519: alpha = 1/3 in the module/central-direction algebra looks derived but
  is convention-bearing.
- 10594: species-uniform physical reuse of the lane3 machinery overshoots m_b
  by 35x - a hard wall against species-blind reuse of landed quark rows.
- 10598: the celebrated 5/6 near-match (0.8329 vs 0.8333) holds in ONE scale
  convention and misses another by 15%; landed note carries the boundary -
  do not cite the match without the convention.
- 10615: the landed positive reading at two spacings coexists with a FAIL row
  at h = 0.125 (later closed by the pulled 10618); check which state a citing
  row consumed.
- 10616: self-declares review_loop_disposition: block and supersedes orphan
  commit d0e61efc whose runner is weak; do not treat the superseded orphan as
  independent support.

## packsci03 (idx 10620-10929)
- 10627: the LH-doublet anomaly-cancellation landing description carries an
  internal inconsistency between its ledger row and prose.
- 10639: a prior cached PASS=59 FAIL=3 result was standing as evidence on the
  4pi magnitude row before the repair.
- 10670: a prior CLEAN AUDIT on the topN row was invalidated; the reclean is
  in-branch.
- 10690: the microcausality lane terminal references "the family's earlier
  false-green incident" - locate and verify that incident before citing the
  early family PRs as always-green.
- 10716/10717: a frozen row log had been standing in for the completed
  evidence packet on the basin rows; audit must run the primary verifier.
- 10729/10758: the numerical value 0.5934 recurs across lanes as a
  free-floating comparator; do not let it launder into a derived value.
- 10734: proposed_retained for four A1=M_2(C) rows includes a critical
  rank-#1 row with 870+ descendants; audit that one first.
- 10768: two concrete character-expansion errors (truncated-box partition
  function; ...) were present in prior work and are now forbidden wording.
- 10776: a carrier definition (free carrier := I_3) was AUDITED AS RENAMING;
  same defect class as the PR #228 finding (pulled at 10756).
- 10790/10791/10837/10839: blocks admitted to "retained-only" campaigns while
  their own dependency retained-status was still PENDING.
- 10806: a docs/ completion note from 2~ is cited by the quark-CP no-go as
  carrying a fitted route; check before reuse.
- 10810: a legacy Monte Carlo 8/9 statistic appears in the R_conn support
  surface; the exact 8/9 is algebraic - keep provenances separate.
- 10840: a 582-candidate retention-outcome prediction exists in-pack; it is a
  prediction, not authority - never cite it as audit evidence.
- 10841/10842/10843/10846/10847: one-line certificates document SUBSTANTIVE
  reclassifications (incl. g_bare = 1 admitted-not-derived and EWSB
  identification dropped) with no scope text; verify the edited landed notes
  say what the certificates claim.
- 10849: a runner describes its own role with a class-label mismatch vs the
  ledger.
- 10861: a landed bridge theorem's load-bearing step is shown to be a BUNDLE
  (algebraic half + semantic half); audit the halves separately.
- 10868: the closing synthesis PR's own certificate flags [scope]; treat the
  full-chain replay as evidence for composition only, not for the semantic
  identifications.

## packsci04 (idx 10930-11239)
- Block-number collisions run through the s3-route2 chain (Block76, Block83,
  Block85, Block89, Block97, Block100, Block103, Block104, Block107, Block113,
  Block115 each name TWO different blocks); never cite "Block N" without the
  pack path.
- Byte-identical boilerplate no-go ledgers recur (10963/10973/11069/11092/
  11103/11127/11188); their row counts overstate independent evidence.
- 11040: one certificate marks NO audit-required flag (unusual in the
  stratum); treat as unset, not as waived.
- 10943: a narrow tolerance was applied in the density-square PR body.
- 11029: the review disposition records a defect in the source note itself.
- 11163: the queue-exhaustion certificate is exhaustion over the ENUMERATED
  queue only.
- 11199: an earlier audit rejected a named derivative as evidence; the prior
  version's defect is documented in the review-caution ledger.

## branch09 (idx 2736-3073; July autopilot sweep - Authority: none throughout)
- 2738: the CKM lane index declares "closed"/"airtight" on a SELF-AUTHORED
  audit runner; canonical CKM-style failure, do not cite the lane index.
- 2755: the B2 import states an 11% PDG discrepancy (0.125 vs 0.~); the B1
  radian bridge rests on an asserted (not proven) escape from a standing
  no-go.
- 2775/2798/2813: header "Status: PASS" sits above failed primary targets in
  three notes; read gate dispositions, not headers.
- 2766: an unchanged external decoder returned a law name that was not an
  expected oracle; rows 8-11 of its control matrix are marked NO~.
- 2976: a retracted 215-gate detector figure and an embedded upstream
  provenance flag live in the same note.
- 2995: a 4/3 operator-vs-graph discrepancy is unresolved; its static Green
  surface is consumed downstream.
- 2970: 2.46e12 bus SWAPs/cell is labelled feasibility-only; not a physical
  resource claim.
- 3063: an upstream construction's resource non-conservation (1 -> 3) is
  inherited and exposed, not repaired.
- 2887: the four theta_2 values scatter 0.278-0.300 across fixtures and THREE
  of four rows were later withdrawn (see the pulled correction 2832).

## packsci05 (idx 11240-11548)
- 11530: invents a status tier ("convention_retained") that exists nowhere in
  the vocabulary, and the convention is chosen because it matches PDG; never
  let the invented tier or the PDG-match justification reach the ledger.
- 11515: a PDG match is used as "killer evidence" to select the period-1-rad
  convention; that is comparator-as-selector, not derivation.
- 11543: the AFT-conditional convention forcing carries an UNAUDITED
  load-bearing hypothesis and admits a 4/9-vs-2/9 trace-normalization
  ambiguity mid-proof.
- 11482: a tuned family scan against the 0.9176 objective is recorded and
  forbidden as evidence.
- 11517/11546: persistent-memory "retained" claims (axiom-chain-closure,
  Brannen-CH, corrected propagator) trace to a NEVER-LANDED write-up (11546)
  and are unverified on main; the dynamics lane cannot assume its own memory.
- Dynamics lane: five mutually-contradicting same-day verdicts (pun vs
  structural) exist with no in-pack terminal adjudication; the pulled arc
  (11538 -> 11534 -> 11539) is the citable ordering.
- 11536: runner paths live in ephemeral .claude/tmp/ - evidence not
  reproducible from the committed tree.
- 11458: self-reviewed only; 11492/11509 are cert-only families with no
  ledger file in the manifest.
- 11547: a stochastic-collapse positive exponent was retracted as a k-band
  artifact; the 4D gravity champion config uses 5x hand-scaled field
  strength.
