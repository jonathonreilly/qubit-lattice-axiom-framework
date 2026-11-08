# Repo search

Retroactive rule-9 digest for FINISH row 531, 2026-11-08. Codex
(`gpt-6.1-sol`). Research text, not an audit; this grants no status.
Only this file is a repository output. No proof was attempted or discharged.

**Top flags:** the external-location copies of posted PI #13 and GW #14 are
identical to our notes. The earlier M3 diagnostic is already in the snapshot.
No newly found proof, refutation or conflict overturns a posted note's stated
restricted conclusion. Useful older soft-route steps are listed for citation,
with their actual-model gaps retained.

## Source identity and search boundary

The lane is pinned at `5b818235ddae07ec1f6249073df1d41e73ce30ff`.
Neither `prior/repo-search.md` nor this date's digest existed initially.
GOAL, the requested FINISH sections, and the actual source notes were read.
The workflow is absent in this sparse checkout; its rule 2.9 was read from
`origin/main` in `/Users/jonreilly/Projects/Physics`.

All five requested refs were searched in that repository:

| Ref | Commit |
|---|---|
| `origin/main` | `43a1fcc374711ca50626eca667441d3ca575c7d1` (final refresh; initially `f5af11cd0102cfd0b51aef0911f600130bf5beb1`) |
| `pr/10114` | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| `pr/10133` | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| `pr/10134` | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| `pr/10141` | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

Searches use `git grep -l/-n -i -E`, `*.md` and `*.tex`, excluding
`.claude/science/physics-loops/ym4d-hard-route-20261030/**` on every ref.
Hits are read with bounded `git show <ref>:<path> | sed -n ...p`.
Broad capped discovery searches are locators, not evidence of absence.
Targeted follow-ups and their limits are recorded below.
No history patch search, blame, numerical proof, external posting, or source
edit was performed.

Path abbreviations below:

* **S/** = `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
* **R/** = `research/ym4d/` on `pr/10141`.
* **SA** = `YM4_sketch_500.tex`, supplied at `31a47c543775` in
  `/Users/jonreilly/ym4d-lead/sa/`.
* **I** = `theorem_0_complete_account_raw_I.tex` at that same source revision.

R/ is a snapshot of this hard-route project, not an independent proof.
S/ is the older soft-kernel project. Shared vocabulary does not identify
its fields, probability laws, boundary operators, or history rules with ours.
Credit the named source authors and the model provenance printed in those
files. In particular, Sussman and Alpoge's text, authored with Claude and
Codex, and Balaban's methods remain credited to them.

## Flags: proofs, refutations, conflicts and duplicate sources

**No newly located result establishes or refutes an entire November 8 target.**
This is the outcome of the searches below, not an absence theorem. There are
important existing restrictions and exact copies:

| Surface | Relevant outside-lane finding | Consequence |
|---|---|---|
| Posted PI, issue #13 | `pr/10141:R/library/out-pi.md:273–303,324–356` is byte-identical to our note. Theorem PI assumes S1-loc/S2/S2+; Prop. 3.1 leaves boundary gauges additional; Props. 3.2–3.3 refute the broader S1–S2 implication. | Already our result. Cite/reuse it; do not count the snapshot as independent support. PI-ADMIT and C0-ETA remain actual-entry supply problems. |
| Posted GW, issue #14 | `pr/10141:R/library/out-gw.md:54–64,190–222` is byte-identical to our note. Its frame bound is supplied on the PI class; general localized/completion admission and graph bounds for G_pi^J/G_1^J are excluded. | No newly found conflict. Keep these limits in every application. |
| Posted GW1, issue #19 | `pr/10141:R/library/layer-thm-part.md:1344–1355` retains the earlier GW import; R/library/out-gw.md:64 excludes the G_1^J graph member. The snapshot has no GW1 proof note. | Earlier imports are not a proof of the November 8 J7 port. No outside-lane duplicate of that port was found. |
| Posted M3, issue #20 | `pr/10141:R/library/layer-thm-part.md:1440–1463` already gives the zero-switch failure of the untagged candidate and explicitly says relocalizing the mass changes a definition. | This diagnostic is prior work and must be credited. It does not construct the later tagged assignment, and agrees with m3.md's off-one limitation. |
| Posted TPI, issue #21 | `pr/10141:R/library/tp1.md:71–88,342–358` assumes the exact residual estimate and retains its terminal term. `R/library/fp1.md:246–258` excludes a fine-mesh density claim. | The consumer and a useful flat step already exist; neither passage proves the new pointwise retained-background estimate. |
| GEOH/live-strip application | `pr/10141:R/library/st1-r4.md:1703–1707` already rejects literal GEO-slot at the outer interface and requires SLOT-ST plus SLOT-CA/FM-match for identification. | Do not conflate this known slot mismatch with geoh-o1.md's later thin-selector mismatch. Neither permits unconditional transfer of live-strip geometry. |

The seven R/ proof files checked by blob identity—out-pi, out-gw,
layer-thm-part, tp1, in1, fp1 and st1-r4—are all identical to this checkout.
R/README.md:25–38 identifies its source as hard-route commit
`af80bc9a5f58cd5b2f62c218fcdb8e2105aed972`. This is explicit recovery lineage.
It is not a second derivation. The posted issue numbers above are the supplied
task's identification; this search did not fetch live issues or comments.

## Search record

Each item below was searched on **all five pinned refs**, outside the excluded
lane. The following four completed global passes are reusable:

* **L, labels/statements, 91 matching lines, cap 100:**
  `S1-loc([^a-z]|$)|PI-ADMIT|C0-SUP|C0-ETA|terminal covariance|retained free covariance|tagged current|bare mass words|GEOH|UO2-geo|H-C-MARK|HCM-R|HCM-SC|HC-WEIGHT|SC-HESS|healed restriction`.
* **M, methods, 448 matching files, cap 600:**
  `winding carrier|collar ownership|read ownership|reserve volume|live.strips|birth collar|level ceiling|preparation nest|renewed mark|fresh payment|rim test|face lift|common envelope|joint reference bound|spectator row|carrier oscillation|plaquette witness|fluctuation witness|cut island|comb averag|mean.{0,20}comb|saddle operator|healed restriction|vacuum slot|boundary gauge|locali[sz]ed set|coarse covariance|curvature lift|reduce.before.switch|mass word`.
* **A, averaging/erasure/counting variants, 179 matching files, cap 350:**
  `healed.{0,40}(eras|replay)|eras.{0,40}heal|vacuum slots|change of averaging|averaging.scheme|mean.{0,30}comb|comb.{0,30}mean|saddle.{0,30}(Hessian|operator)|Hessian.{0,30}saddle|rooted.address|collar.ownership|read.ownership|code.count|renewed.mark|constrained.minimi[sz]er.{0,30}rim`.
* **G, geometric/current variants, 283 matching files, cap 300:**
  `winding.{0,25}carrier|carrier.{0,25}winding|strip.{0,25}disjoint|disjoint.{0,25}strip|birth.{0,20}collar|collar.{0,20}owner|spectator.{0,20}row|row.{0,20}spectator|tagged.{0,20}current|mass.{0,15}locali[sz]|constrained.minimi[sz]er.{0,30}rim|rim.{0,30}minimi[sz]`.

M's per-ref file counts are 69, 116, 116, 69, 78 in the ref-table order.
A's are 31, 40, 40, 31, 37. These are retrieval counts, not proof evidence.
G's are 55, 59, 59, 55, 55. None of these four passes reached its cap.

**Concurrent-main refresh:** origin/main moved from f5af11cd0 to 43a1fcc37
during this session. All four PR refs remained unchanged. L was rerun at
the full final main hash: its sole line remains the unrelated LHCM backlog
match. The union M|A|G was rerun there with `-l`, head 250: 137 files,
the identical main path set, with no added or removed hit. Of these,
136 hit-file blobs are identical between the two main commits. The changed
file is `docs/ai_methodology/skills/audit-loop/SKILL.md`; its refreshed hit,
lines 744–754, concerns a panel's “top-level ceiling”, not a strip's level
ceiling. That bounded process passage was read as a false positive, not
invoked. The workflow and the four specifically cited main documents were
separately blob-compared and are identical. Thus the mathematical evidence
recorded here survives this refresh. The refresh uses
the displayed commit hash, so a later ref movement does not change it.

The command template is:

```sh
git -C /Users/jonreilly/Projects/Physics grep -l -i -E '<expression>' \
  origin/main pr/10114 pr/10133 pr/10134 pr/10141 \
  -- '*.md' '*.tex' \
  ':!.claude/science/physics-loops/ym4d-hard-route-20261030/**' | head -600
```

L uses `-n` and head 100; A uses head 350; G uses head 300. Follow-ups used `-n` on
identified files and bounded source excerpts. Initial broader searches with
`P_W`, `retained free`, bare `M3`, or unqualified `replay` produced unrelated
matches or hit their caps. A broader geometric/joint query also hit head 350
within origin/main; G and scoped YM follow-ups replace it. They are not used
for negative conclusions. The scoped joint-reference follow-up used
`joint.{0,20}reference|reference.{0,20}joint`, and the nonwrapping follow-up
used `nonwrapp`, on S/ and R/. Its combined head-130 output was narrowed
to primary source files, not treated as absence evidence for later refs.
Examples include Wilson probability P_W, Koide projectors, and software replay.
No truncated discovery list is treated as completed coverage.

For each ledger entry, “same statement” means the actual quantified statement,
including its hypotheses. “Supplies a step” may still require a separate
identification before use. Source assertions and historical checker verdicts
are reported as such; this digest independently certifies none of them.

## 1. PI-ADMIT; C0-SUP and C0-ETA

Targets: pi-admit.md:9–18,187–239 and c0-sup.md:142–166,536–554.
The latter requires one parameter-independent small real boundary gauge and
twist bounds on the actual first exterior read throughout the prescribed domain.
It remains open at I 131725–131746.

Terms: L's PI/C0/S1-loc terms; M's `boundary gauge`,
`locali[sz]ed set`; targeted `boundary|localized|Schur` in R/layer-thm-part.
Refs: all five, with detailed hits on pr/10141.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| R/library/out-pi.md:273–303 | S1-loc, S2 and S2+ on literal rows imply invertibility, scaled decay and an absolute local walk expansion for q_0. | Supplies the consumer theorem; exact copy, already cited. Use, do not reprove. |
| R/library/out-pi.md:324–329 | Thick aligned towers give S1-loc from S1 only where N(x) is contained in Omega_0; boundary gauges remain additional. | Same interior admission step. Cite; it does not solve C0-ETA. |
| R/library/out-pi.md:331–356 | Thin fingers or a touching boundary bond permit S1/S2/S2+ with singular Delta_a under the stated whole-action convention. | Same existing counterexamples. They do not identify reached histories. |
| R/library/layer-thm-part.md:698–703,1385–1408 | Interior thickness does not provide boundary-crossing gauges; localized continuation reads beyond Y+. | Same open supply issue. Cite this earlier formulation rather than claim the issue is new. |
| R/library/out-gw.md:54–64 | The double-block frame follows on the admitted PI class; no boundary gauge-gluing or all-domain admission theorem is claimed. | Supplies a step after admission. No additional boundary supplier. |
| S/RTARGET.md:716–725 (pr/10114 and pr/10133) | Local axial gauges and Dirichlet-compression walks are proposed for the soft Hessian; higher-level background-Hessian supply remains open. | Related method, different operator. Cite only as route history; do not import as C0-ETA. |

No outside-lane C0-SUP, C0-ETA or PI-ADMIT result was found in L.
Their absence under these names does not exclude a differently named theorem.
The inspected method hits do not supply the actual localized exterior pair.

## 2. TPI: coarse covariance of the retained free background

Target: tpi.md:27–53: R_j=P_{W_j}, W_j=E orthogonally minus (E intersect ker A_j),
and R_j(p,p)<=C L^(-4j), uniformly through j=K, with the terminal term retained.
Terms: L's terminal/retained covariance; M's `coarse covariance`,
`curvature lift`; targeted `terminal|coarse.*covariance|curvature|retained`.
Refs: all five. R/ hits below are on pr/10141; S/ hits occur identically
on pr/10114 and pr/10133.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| R/library/tp1.md:71–88 | P=sum_{i<=j}G_i+R_j and abs(R_j(p,q))<=C(a/a_j)^4 are FREE hypotheses; the residual bound is additional to slice bounds. | Same requested estimate, **assumed**, not proved. Cite as consumer. |
| R/library/tp1.md:342–358 | Retaining R_{k_1} gives the additional kernel error (D L^(-n))^4 in (5.4). | Supplies the terminal-use step. Already part of TP1, not a new TPI proof. |
| R/library/fp1.md:142–168 | The flat plain-fibre energy equals the straight-fibre minimum and lies between norm_2(da)^2 and 256 norm_2(da)^2. | Supplies a flat comparison step. Use with its actual conventions. |
| R/library/fp1.md:246–258 | Fixed-current-scale covariance kernels decay exponentially; general nonlocal conditioning and fine-mesh density bounds are not asserted. | Related free estimate, different readout. Does not imply TPI by relabeling scale. |
| S/WITNESS.md:505–547 | Actual reverse conditional increments sum with D_K=Cov(G_K,H_K); PL-1L_Sigma remains an open interacting matching bound. | Same terminal-retention principle, different law and reference. Cite the earlier caution; not the retained free projection bound. |
| S/CODEX_REVIEW_SEAM.md:21–46 | Total covariance keeps the coarse means; its written example has zero conditional covariance but total covariance 70/27. | Supplies a diagnostic against dropping coarse terms. No contradiction with TPI, which retains them. |
| S/LIMIT.md:365–380,520–538 | Coarse covariance remains in the rotation decomposition; conditional fine sums plus terminal oscillation control imply SEAM. | Related conditional reduction, not P_{W_j}. Cite only where that reduction is used. |
| S/K4MATCH.md:545 | Free/reference scale summation is conditional; interacting four-source matching stays open and retains terminal cumulants. | Related higher-cumulant consumer, not the diagonal bound. No import needed. |

Additional terminal-word hits are restatements of the S/WITNESS or SEAM
contracts: S/COMBO.md:543,587; REALONLY.md:38; REALRGA.md:577,615;
REVIEW_N5B.md:393; REVIEW_REALONLY.md:189; REVIEW_TQ2.md:292;
REVIEW_WITNESS.md:272; checks/combo_review.md:318;
checks/n5b_criteria.md:14–15; checks/n5b_review.md:86–91,264;
checks/realonly_review_initial.md:38;
checks/realonly_witness_flow_read.md:25;
checks/realrga_review_source_v1.md:566,604.
Their exact common statement is “retain the terminal covariance”; none states
the TPI pointwise free-background bound. These were located in L; the primary
formulas were read in WITNESS and LIMIT, rather than counting each echo as
another theorem.

No outside-lane proof of the full TPI estimate was found. The Abelian and
native Green-function word matches are classified in the screening section.

## 3. M3: reduced tagged current

Target: m3.md:16–33,383–418: define the mass-inclusive reduced words, get
component locality and primitive exp(16 kappa_1) bounds, agree at one, and
explicitly change the off-one assignment.
Terms: L's `tagged current|bare mass words`; M's
`reduce.before.switch|mass word`; follow-ups `current.word`,
`tagged.{0,20}current`, `mass.{0,15}locali[sz]`, and R/layer's `mass|switch`.
Refs: all five; direct target hits are on pr/10141.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| R/library/layer-thm-part.md:49–50,91–106 | Reduce before switching; switched words are assigned composites, not inverses continued from one. | Same construction rule. Cite/use as prior method. |
| R/library/layer-thm-part.md:1440–1463 | At zero switches the candidate m_c=-Q^T a ell^(-1) is nonzero although empty-region locality requires zero; reduced P_1(s),m_H(s) remain to be defined. | Same diagnostic, already done. m3.md should credit it; do not redo the zero-switch test. |
| R/library/layer-thm-part.md:1453–1463 | No proved account step is refuted; relocalizing the mass changes a definition and needs matching. | Same scope restriction as m3.md. No conflict and no tagged-construction duplicate. |
| R/library/out-gw.md:214–222 | Complete footprints and the identity partition fix the switched assignment for its specified primitives. | Supplies a word-localization step, not the whole current rider or its mass family. Use with its inputs. |
| S/LFPRICE.md:200–237 | Its label “M3” means one-use raw Wilson-action allocation with the normalized comparison still owed. | Different object with the same label. Do not cite as a current theorem. |

No outside-lane construction of m3.md's six-item current contract was found.
Bare M3 hits also name jets, tasks and per-history laws; they are not this M3.

## 4. GEOH-O6: Lift and winding carriers

Target: geoh-o6.md:292–303, LIFT-ONE: complete nonzero actual piece reads
must fit one bounded covering box, with sides below half the torus periods.
Terms: L's `GEOH`; M's `winding carrier`; follow-ups `nonwrapp`,
`winding.{0,25}carrier|carrier.{0,25}winding`; S/ `winding` on bounded hits.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/open-registry.md:230 | Uniform Lift for CLS's complete constructed-carrier/read family is open, owned by GEOH. | Same statement, already assigned. Keep the existing owner; this search starts no attack. |
| pr/10141:R/library/assembly-status.md:127,186 | GEOH includes actual genealogy, coding, slots and Lift as hypotheses on actual histories. | Same unresolved interface. Cite its scope. |
| S/LOCOP.md:51–70 | Local extraction assumes a nonwrapping container containing every read; wrapping supports and frozen exterior reads are excluded. | Same kind of prerequisite, not its supply. Cite as an earlier complete-container caution. |
| S/CODEX_REVIEW_ALIGN2.md:196–212 | One-path-per-periodic-node spline details cannot annihilate constants for the displayed torus example, even with winding choices. | Different winding construction; does not refute or prove CLS Lift. No transfer of its numerical certificate is used. |
| S/CODEX_REVIEW_C2.md:140 | Harmonic/winding currents need not be plaquette boundaries; only the separately zero-winding dipole is filled. | Different current/filling object. Retain the warning, not a Lift theorem. |

The S/ hits are on pr/10114 and pr/10133. No source inspected supplies
spans of all actual CLS carriers. The symbolic winding obstruction in our
note is not upgraded to an actual-history counterexample by these hits.

## 5. GEOH-O2; UO2-geo and FCO

Targets: geoh-o2.md:135–170 and uo2-geo.md:209–232. Bound actual charge
incidences, local codes and the original reserve using owners whose collars
contain every elementary stencil. A union count cannot erase multiplicity.
Terms: L's GEOH/UO2; M's `collar ownership|read ownership|reserve volume`;
A's `rooted.address|code.count`; follow-ups `collar.{0,20}owner`.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/open-registry.md:226 | Complete actual code/read ownership and reserve matching is open, owned by GEOH. | Same target, not a proof. Keep that owner. |
| R/library/in1.md:66–74,157–159 | The cut genealogy counts ordinary nodes once and cut boundaries at most twice; coding and source-volume comparison are extra H-G hypotheses. | Supplies the ledger convention and states the missing application. Already used. |
| R/library/in1.md:534–538 | A degree-D rooted address set has at most D^(2(N-1)) canonical tree codes; normalized frames and a supplied local code bound give the entropy estimate. | Same conditional counting step. Use/cite, do not rederive it as FCO. |
| S/ROUGH.md:390–414 | Complete root charging and Q23 imply a small rooted sum; long readers require Q24, and uniform actual encoding remains open. | Supplies a conditional method, not actual collar ownership. Worth citing in geoh-o2's counting/repeated-read discussion. |
| S/MEAN_READER_RETURN_ASTRA.md:117–143 | Complete-reader substitution assumes q_Y<=k abs(Y) and a common weighted envelope Q, then yields a connected marked norm bound. | Related conditional combinatorics. Does not construct FCO's owners or give its reserve comparison. |

S/ rows occur on pr/10114 and pr/10133. No UO2-geo/FCO supplier was found
outside the lane. Do not reopen the already proved rooted-code arithmetic.

## 6. GEOH live strips

Target: geoh-live-ab.md:25–33 and 481 onward: birth-strip disjointness,
own collar, level ceiling and survival through interrupted preparation,
conditional on the specified CA preparation.
Terms: M's `live.strips|birth collar|level ceiling|preparation nest`;
follow-ups `strip.{0,25}disjoint|disjoint.{0,25}strip|birth.{0,20}collar`.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:157–159 | Actual genealogy and waiting/coding rules remain imports. | Related remaining history input; no persistent-strip theorem. |
| R/library/st1-r4.md:1703–1707 | Collar/rim coordinate identification requires the separately matched SLOT-ST/SLOT-CA conventions. | Supplies a caution about actual integration sites, not strip disjointness. |
| R/library/open-registry.md:225,227 | Revised-operation/quarantine matching and the lower preparation convention are separate open GEOH rows. | Same boundary on application; preserve their owners. |

No outside-lane proof of the all-move live-strip invariant was found.
The actual CA statement was checked at I 85575–85621: it calls its geometry
“Proof outstanding” and uses clauses (a)–(e) as hypotheses. Our note's
conditional proof is not independently reproduced by the snapshot.

## 7. GEOH-O1 selector and quarantine

Target: geoh-o1.md:117–150,275–294: compare the adopted thin selector
with the CA/N prepared nest on the same eligible core; do not equate their
P moves or transfer the latter's collar constant.
Terms: L's GEOH; M's `preparation nest`; targeted `quarant|preparation`
and the geometry variants above. Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/open-registry.md:225,227 | O1 realization/quarantine and O3 lower preparation are separate open assignments. | Same interfaces, no selector equality or counterexample. Do not take over O3. |
| R/library/st1-r4.md:1703–1707 | The old GEO-slot identification fails at the outer interface; a coordinate bijection preserving transports, constraints and pivots is required. | Supplies a different existing mismatch. Cite separately; it does not duplicate thin versus CA selection. |
| R/library/in1.md:44,159 | Hereditary domains and actual genealogy are supplied hypotheses, not consequences of curvature bounds. | Related premise restriction. No realization theorem. |

No outside-lane proof or refutation of the specific thin-selector equality
was found. S/ uses of “quarantine” concern analytic slice dependence,
for example BFT_B.md:3835, not this history selector.

## 8. H-C-MARK; HCM-R, literal rim test and smooth repair

Targets: hc-mark.md:6–18, hcm-false.md:7–10 and hcm-repair.md:6–16.
The weighted renewed-mark continuation remains open. The literal rim example
does not itself prove a history-mass lower bound. The smooth constrained
minimizer replacement still needs HCM-SC and compatible consumers.
Terms: L's H-C-MARK/HCM-R/HCM-SC; M's
`renewed mark|fresh payment|rim test|face lift`; A's constrained-minimizer/rim
pattern; follow-ups `rim.{0,30}minimi[sz]` and S/ `renew|payment` contexts.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:171–173 | A renewed mark's P_t/2 gain must come from a new window outside the old floor; actual renewed-window payment remains to be established. | Same desired payment, explicitly an input. Cite as consumer. |
| R/library/open-registry.md:237 | H-C-MARK is open, with no proof owner at that snapshot. | Same assignment, no closure. |
| S/LFPRICE.md:202–237 | Assign each original action term once; multiplicity-m windows get fraction 1/m, and the normalized ratio integral W_rest/Z_A is still owed. | Supplies exact raw allocation; useful citation for why a fresh payment needs an actual unused payer. Not HCM-R. |
| S/LFPRICE.md:350–362 | A finite normalized seam bound can grow with coupling and history length; actual matched all-cut logarithms remain open. | Related normalization warning, not a rim-history lower bound. |
| S/ROUGH.md:503–539 | The persistent-flux family remains rough with zero kernel gap; original-volume fractions can pay under C9–C11, but general complete-reader/envelope supply remains open. | Different actual soft-history witness. Cite as prior warning against treating every persistent failure as a fresh gap. It does not refute HCM-R. |
| S/INDUCT.md:486–504 | Uniform length-m contraction, or one summable common lag envelope, bounds both lifetime and fixed-terminal sums; per-birth summability alone does not. | Supplies an abstract continuation criterion. Could guide HCM-R; actual rim hypotheses are not supplied. |
| S/BOTTOM_SECOND_CURVATURE_ASTRA.md:353–364 | “Face lifts” are overlapping momentum-torus charts used to glue an alias formula. | Different object with the same words; not a small-curvature boundary interpolant. Do not cite as HCM-SC. |
| pr/10141:R/library/out-mu.md:8–32,69–82,189 | Admitted regular window data have a unique axial minimizer and a holomorphic nesting identity using literal Balaban averages; derivative-decay and other background conclusions are excluded. | Supplies an existing minimizer/nesting step, conditional on its published inputs and window geometry. Cite if used; it does not insert a smooth rim with different prescribed boundary data. |

S/ rows occur on pr/10114 and pr/10133. No outside-lane HCM-R,
RIM-LB or HCM-SC theorem was found. The earlier raw allocation and persistence
arguments should be cited as methods, with their normalizers and domains kept.
They neither turn one failed evaluation into a mass lower bound nor repair the
literal rim test. No new refutation of hcm-false.md's careful stopping result.

## 9. H-E and SJ: stopped joint reference domination

Target: lfi-he.md:116–164: one common positive reference bound for the full
stopped joint graph, with actual masks, pivots, spectators and deterministic
relations, before an external or drop-out supremum.
Terms: M's `common envelope|joint reference bound|spectator row`;
follow-ups `joint.{0,20}reference|reference.{0,20}joint|spectator.{0,20}row|row.{0,20}spectator`.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:175–195 | H-E requires one Borel envelope before supremum; sup_p integral G_p does not bound integral sup_p G_p, as Gaussian translates demonstrate. | Same required distinction. Cite as prior reduction, not SJ supply. |
| R/library/in1.md:459–482 | Injective triangular shifted coordinates and coercivity give a fixed-evaluation Gaussian bound; one uniform envelope is still required. | Same elementary integration step. Already available; do not redo it. |
| R/library/st1-r4.md:1705–1707 | Actual independent collar/rim slots and pivots require a matched coordinate partition/bijection. | Supplies a matching prerequisite. It is not a common joint chart for all stopped histories. |
| S/MEAN_READER_RETURN_ASTRA.md:117–143 | A supplied complete-reader family with common analytic envelope admits a connected substitution bound. | Conditional method for formed functions, different reference integral. No SJ proof. |
| S/ROUGH.md:406–414 | Rooted counting cannot create factorization on an interacting reference; common joint majorants remain hypotheses. | Same methodological restriction. Cite in the joint-reference discussion. |
| S/GLOBAL_RETURN_HISTORY_ASTRA.md:43–65 | The exact conditional identity keeps all outside-only factors; two-level history numerators must be compared to their actual joint all-cut reference. | Supplies a finite measure-identity step. It explicitly does not supply locality or jets from positivity. Useful method citation. |
| S/JMBRA.md:680–689 | Exact ancestral replacement/factorization is finite algebra; the charged joint bound, uniform nonzero reference and quantitative full-reader budgets remain open. | Supplies finite algebra and weighted sufficient criteria, not SJ's actual stopped-row estimate. Cite if that algebra is reused. |
| S/JMBRB.md:689–698 | Integrated complete-overlap algebra is available, but actual joint atoms, matched references and renewal norms are missing. | Alternative related construction, conditional. No SJ closure or contradiction. |
| S/RD4.md:448–460,687–694 | A mixed majorant plus exact overlap-component gluing yields the connected log; actual-model reference/chart instances remain open. | Supplies a conditional gas-integration method. Scalar history prices do not establish its gluing input. |
| S/RD3.md:565–575 | The same reference must bound inherited interaction, joint failure masses and contour total variations; a mandatory-event normalization can cancel its nominal rare price. | Closely related normalization diagnostic, different reference. Do not import an unnormalized gain into SJ. |
| S/RD.md:1017–1025; S/MATCHA.md:535–559 | A local joint-failure/reference budget and a common pinned joint majorant remain the next targets; renaming them does not solve them. | Related open suppliers, not prior closures of H-E or HCM-R. |
| S/CHARGE.md:549–556; S/RENEW.md:514–524; S/LFPRICE.md:694–711 | The one-time original charge still needs a same-reference joint comparison and complete readers; finite renewal debit is not contraction. | Relevant to both items 8 and 9. Cite these restrictions when using their raw charge/lifetime mechanisms. |
| S/SOFTHARD.md:534–547,584–598 | Hard return is a joint disintegration retaining both adjoining Dirac kernels and any singular remainder; HRT requires a joint-support analytic output, not fixed-exterior a.e. densities. | Supplies a precise representation contract, explicitly open. Useful for R2/reference-law matching; not the actual CA stopped construction. |

No inspected outside-lane result supplies SJ. Finite-mixture envelopes in
S/COMBO.md:196,228 and its review echoes concern mixtures of continuum states,
not stopped constraint rows. Their matching words do not close H-E.
Related primary reminders are S/BARE_CUT_WHITE_ASSEMBLY_ASTRA.md:423–430
(its output does not supply RGA14's joint reference/regulator estimate),
S/MANUSCRIPT_RG.md:53–65 (H2/H3 require one-use fractions and exact complete-reader
factorization), and S/SQUARED_ALIGNMENT_PRICE_ASTRA.md:371–383 (the matched
reference ratio remains unestimated). S/APPROACH_REGISTRY.md:1031,
HANDOFF.md:1020, JMBRA_LOG.md:30, LFPRICE_LOG.md:47, SOFTHARD_LOG.md:670,
PROOF.md:1140 and SESSION25_RESULTS.md:3265 are pointers or status echoes,
not further independent suppliers. The reviews at REVIEW_RD3.md:39,266,
REVIEW_JMBRA.md:306,347, REVIEW_LFPRICE.md:49, REVIEW_REALRGA.md:196,
REVIEW_HOLEPAY.md:213 and REVIEW_RENEW.md:275 retain those same open
joint-reference/full-reader conditions. Their primary contracts above were
read; no extra proof or new status is inferred from the review counts.

## 10. H-O: carrier oscillation and collar bound

Target: lfi-ho.md:7–17,296–328: retain the actual per-carrier weighted
primitive sum HC-WEIGHT; an unweighted total does not bound its carrier norm.
Terms: L's HC-WEIGHT; M's `carrier oscillation|common envelope`;
targeted R/in1 `oscillation` and S/ full-reader weighted sums.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:86–90,197–203 | H-O is the fixed-creation-domain carrierwise oscillation bound (18), with B_Phi fixed before the ceiling; mass or Re(Psi) bounds do not prove it. | Same desired conclusion, explicitly open. Cite as consumer. |
| R/library/in1.md:571 | The class induction invokes H-O to return its missing oscillation clause. | Same use site, not a supplier. |
| S/MEAN_READER_RETURN_ASTRA.md:121–143 | The rooted sum Q has individual suprema and exponential complete-reader weights inside the sum before substitution. | Related weighted analytic method. Cite where useful, but match actual collar carriers and copy weights before use. |
| S/ROUGH.md:406–414 | Long original readers require the complete weighted sum Q24; deleting readers to use a shorter estimate is forbidden. | Same warning about weakening a norm, different family. No HC-WEIGHT supply. |

No outside-lane HC-WEIGHT proof was found. Our note's corrected open collar
supplier is not contradicted by the older H-O hypothesis or its mass induction.

## 11. W1/W2/W5 witness matching

Target: w125-match.md:8–13,39–60: port the precise plaquette,
fluctuation-plus-gauge and cut-island certificates, retaining their actual
cones, old rows, separate carrying action and history matching.
Terms: M's `plaquette witness|fluctuation witness|cut island`;
targeted `nonwrapping|bad.plaq` and original-witness ownership in S/.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:161–173 | The ordinary, fluctuation and cut-island gains require the actual maps, owned cones and an unused last cut witness excluded from the island mass. | Same contracts, stated as hypotheses. Use/cite; no new actual-history match. |
| R/library/in1.md:419–457 | Assuming the nonlinear one-step estimate, four-dimensional cone counting and energy iteration give the plaquette gain; renewed marks remain separate. | Same existing counting/iteration step. Do not rederive it as the certificate supplier. |
| S/LFPRICE.md:202–237 | Distinct original plaquettes pay an owned action fraction; overlapping windows require divided shares and a remaining normalization comparison. | Supplies the raw ownership algebra. Cite as prior method; not the complete W5 match. |
| S/CODEX_REVIEW_STEP.md:317–318 | Bad-plaquette implies a selected soft-link price (1-theta_y) epsilon_cl^2/(128N) only under the stated nonwrapping and smallness hypotheses. | Related conditional witness, different soft kernel/test. Cannot replace W1 or W2. |
| S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149 | A simple Wilson loop in a transfer kernel has a positive one-step centered correlation via a rank-one convolution inequality. | Different meaning of “plaquette witness”: nontriviality, not a failed-test payment. Do not cite as W1. |

The S/ files occur on pr/10114 and pr/10133. No outside-lane complete
W1/W2/W5 actual-history matching theorem was found. GEOH-O1 remains the
existing operation-matching owner; this search does not reopen it.

## 12. A4.1: mean versus comb averaging and the saddle operator

Target: a41-avg.md:7–10,164–204: compare the actual completed physical
forms and weighted readouts, not merely their linear rows or flat fibres.
SC-HESS remains a separate supplier on already admitted charts.
Terms: M's `comb averag|mean.{0,20}comb|saddle operator`;
A's averaging-scheme and saddle/Hessian variants; targeted S/RTARGET and BALX.
Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/fp1.md:142–168 | Plain and straight flat fibre minima agree by curvature-preserving gradients; no bound on the correcting gradients is claimed. | Supplies a flat step only. Cite/use; not a nonlinear completed-form identification. |
| R/library/out-pi.md:358–363 | Its literal one-contour rows are not the symmetric contour-family rows used in parts of the outline. | Same convention distinction. Must remain explicit in every attempted transfer. |
| R/library/layer-thm-part.md:1333–1341 | Match actual rows, spaces, whole-action Hessian, boundary coefficients and metrics; an inner-plaquette action gives no boundary equality for free. | Same missing identification issue. Cite as prior premise statement. |
| S/RTARGET.md:695–711 | A saddle-point Combes–Thomas approach concerns the soft fluctuation form on ker h; the later pointer claims a trivial-background result only. | Related method, different saddle. A pointer marked unreviewed is not an SC-HESS proof. |
| S/BARE_COUPLING_MATCH_ASTRA.md:362–375 | Its H_c is the local SU(N) Haar-normalizer saddle Hessian in a fixed-domain prefactor identity. | Different Hessian with the same words. No mean/comb transfer. |
| S/CODEX_REVIEW_BALX.md:150 | The exact historical averaging map/hypotheses cannot be recovered from the allowed secondary corpus; that import stays pending. | Prior caution about unverified Balaban transfer. Cite only at that limited scope. |

S/ rows are on pr/10114 and pr/10133. No outside-lane SC-HESS theorem
was found. A4.1 should reuse FP1's flat comparison and cite the convention
restriction; no new inverse or flat-fibre derivation is warranted.

## 13. R2: healed restriction, replay and vacuum slots

Target: r2-heal.md:61–65,471–500: exact retained reference laws,
formed-entry replay and signed common vacuum cancellation, conditional on
the separately owned complete-read formation inputs.
Terms: L's `healed restriction`; M's `vacuum slot`;
A's healed-erasure/replay variants; targeted `healed|erasure|vacuum slots`
in S/ after excluding software-replay matches. Refs: all five.

| Hit, exact lines | Exact statement in one line | Closeness and disposition |
|---|---|---|
| pr/10141:R/library/in1.md:66–74 | Inner island histories and old drop-outs are not replayed in the outer genealogy; ordinary nodes occur once and cut boundaries at most twice. | Supplies the counting convention, not equality of formed functions. Use as already available. |
| R/library/in1.md:205–216 | Exact healing, a loaded-label bound and normalized stability are distinct H-SUM hypotheses. | Same consumer boundary. It does not supply complete-read replay or vacuum identities. |
| R/library/st1-r4.md:1705–1707 | Stage collar/rim coordinates must be matched, with constraints and pivots preserved. | Supplies a necessary reference-slot prerequisite, not all-history R2. |
| S/SOFTHARD.md:584–598 | A next-step density must be represented on the actual joint constrained support, keeping its singular remainder and external measure. | Related replay/representation precaution, not equality of CA formed entries. Cite if adopting this disintegration method. |

No actual healed-erasure/replay or signed-vacuum-slot supplier was found in
the older soft-route hits. “Replay” in its HANDOFF/APPROACH_REGISTRY and
check files describes rerunning software and is a different object.
R2 should continue to use its existing Sussman–Alpoge restriction proof;
CLS-READ/CLS-HISTORY and CI-FORMATION keep the unresolved supply. No new
attack or reassignment is justified by this digest.

## Outline/account cross-check and limits

The SA-index README, matching chunk rows, their neighbours, and obligations
were consulted before the following bounded SA source reads. They confirm
the distinctions used above; they do not independently validate entire proofs.

| Object | Index locator | Source read and exact relevant statement |
|---|---|---|
| Averaging transfer | chunk-04:14–21; obligations:115 | SA 3898–3906 requires uniform nonflat Hessian/inverse/constraint transfer and says identity-linearization agreement is insufficient. |
| PI entry and boundary | chunk-10:21–32 | SA 10256–10264 and 10287–10288 distinguish layered-domain local gauges and compressed-Hessian plaquettes protruding outside Omega_0. |
| Free retained covariance | chunk-24:17–22 | SA 26020–26037 gives nested projection/slice algebra; 26141–26148 describes the curvature lift and differing tree/soft constraints. |
| Preparation and marks | chunk-16:48–54 | SA 17407–17414 and 17433–17449 retain the determining/action sequences, quarantine and original birth spaces. |
| W1/W2 | chunk-16:166–178 | SA 18270–18301 gives the conditional energy contrapositive and explicitly needs gauge energy for approximate-fluctuation failure. |
| Ownership | chunk-17:11–17 | SA 18436–18460 proves genealogy multiplicity and an owned-site union count; it does not identify every analytic charge incidence with a distinct site. |
| H-E | chunk-17:45–54; obligations' reference-integral entry | SA 18757–18791 uses actual complete kept forms, coordinates and chart Jacobians. |
| R2 | chunk-17:57–62,67–70 | SA 18878–18942 requires full move reads before erasure/reinsertion; 19065–19086 requires the identical signed vacuum number on both lists. |

For CA statements, existing source-note locators were reused and the exact
needed passages were read: I 72720–72728 requires component-local P_1/m_H;
I 15446–15453 restricts the first and last explicit identities to switches
one, leaving the response identity unqualified; I 85575–85621 calls
live geometry outstanding and uses it as hypotheses. The account's actual
label is `4.22:not-live-region-geometry`; an informal neighbouring label in
a lane note is not used as a source identifier here.

No expanded-outline file outside the allowed source directories was opened.
References to YM4_1400 in the local notes are their existing provenance,
not fresh source checks in this digest. Balaban's original papers were not
read or imported. No new literature assertion rests on unavailable pages.

## Screening of other matches

These examples explain why a broad word match is not a usable supplier:

| Ref/path and lines | Exact statement | Disposition |
|---|---|---|
| origin/main:docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:4,79–94 | The model is isotropic finite-Z_N Villain on equal even periodic tori, with exact/coexact/harmonic two-form projections. | Different measure and coupling regime; not TPI's blocked SU(2) free-background law. No import. |
| origin/main:docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145 | A supplied noncompact determinant-weighted Dirichlet Maxwell law has Hessian between (beta-alpha)C*C and (beta+alpha)C*C and the resulting covariance lower bound. | Related covariance-score method, different law/boundary and not a retained projection estimate. No direct use. |
| origin/main:docs/NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md:20–32 | Supplied three-dimensional dispersion scalars are accompanied by saved interval/arithmetic certificates. | Different dimension/object and computer-assisted evidence; cannot discharge any present step. |
| origin/main:docs/AUDIT_BACKLOG_NOTE_2026-05-02.md:162 | “LHCM-related rows” counts another backlog family. | Substring HCM-R, not the renewed-rim continuation. No relevance. |
| S/BOTTOM_SECOND_CURVATURE_ASTRA.md:353–364 | Face lifts cover momentum charts. | Different object; see item 8. |
| S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149 | A plaquette-loop transfer correlation is positive at one time step. | Different witness; see item 11. |
| pr/10141:R/library/open-registry.md:212–213; assembly-status.md:132,190 | FCON is FC-mean-match/FC-test for moved stage contours, including Gaussian, seam, slot and indicator admission. | A substring match for FCO, but a separately owned analytic contour problem. It does not supply full geometric collar ownership. |

Other M/A file-list names concern finite clocks, bus code counts, CAR
formation records, Regge reactions, generic common envelopes or process text.
These are filename-level triage exclusions, not full argument reads or an
absence theorem about their contents. None was used as a YM4D premise.
The 448/179/283 file lists and bounded follow-up
outputs are in `/tmp/ym4d-repo-search-20261108-codex/` for recovery. The actual
reusable statements, paths, lines and queries are recorded here rather than
depending on those temporary lists.

## Reuse and recovery decision

Continue only the named missing suppliers. The useful citation additions are
S/LFPRICE's one-use raw allocation, S/INDUCT's common-lag criterion,
S/ROUGH's complete-reader/root requirement and S/MEAN_READER_RETURN's weighted
substitution premise. Each is conditional or a different soft-route object;
none may be silently inserted as actual hard-route admission or formation.
Use R/ only as explicit lineage for the already available notes.

The S/ primary files compared by Git blob identity are identical on
pr/10114 and pr/10133: WITNESS, LIMIT, COMBO, K4MATCH, REALONLY, REALRGA,
the four terminal reviews listed above, CODEX_REVIEW_SEAM/ROTDEF, ROUGH,
LFPRICE, INDUCT, MEAN_READER_RETURN_ASTRA, LOCOP, CODEX_REVIEW_ALIGN2/BALX/STEP,
MASS_GAP_LOCAL_BLOCK_ASTRA and BOTTOM_SECOND_CURVATURE_ASTRA. Reading those
identical sources again on pr/10133 would add no evidence.
The additional joint-reference primary files JMBRA, JMBRB, RD/RD3/RD4,
CHARGE, RENEW, GLOBAL_RETURN_HISTORY_ASTRA, MATCHA, SOFTHARD,
BARE_CUT_WHITE_ASSEMBLY_ASTRA, MANUSCRIPT_RG and SQUARED_ALIGNMENT_PRICE_ASTRA,
plus CODEX_REVIEW_C2, RTARGET and BARE_COUPLING_MATCH_ASTRA, were also
blob-compared and are identical on those two refs.

The posted-note scope comparisons also read our out-gw1.md:31–77,1108–1144,
out-m3.md:7–59, and out-tpi.md:414–434. They retain, respectively, the PI/GW
domain and assignment inputs, the changed off-one current definition, and the
trivial-periodic free specialization. The prior results above do not supply
those missing applications or contradict those stated restrictions.

No editable prompt, source note, registry, ledger, audit, FINISH row or remote
ref was changed. Outstanding questions retain their existing owners. This
digest is a retroactive search record, not a new proof check or a status grant.

Digest by Codex (gpt-6.1-sol).
