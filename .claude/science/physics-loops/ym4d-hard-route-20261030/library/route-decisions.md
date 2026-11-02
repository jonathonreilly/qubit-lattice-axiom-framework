lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T02:33Z

# Route decisions (row 73, route-compare), first version

Pinned at `9149a89a7` on `claude/ym4d-hard-route`. Anthropic claude-opus-5-5,
effort high, Mac mini worker, one session, no subagents. Started
2026-11-02T14:33Z. Same-model research text: a decision record, not a gate,
not an audit, no status. Every statement of the outline cited here is
`unchecked` in this folder.

**Credit.** The outline compared here is Ethan Sussman and Levent Alpoge (with
Claude and Codex as authors of their text), `YM4_sketch_500.tex` in
https://github.com/ethanwsussman/Yang--Mills-LLM-experiment at `31a47c543775`
(read from a scratch copy outside the repository, 32,992 lines, sha256
`d7f77d4da3eb...`, matching `library/sa-map.md`). "SA Lx" is a line of that
file. The programme both routes adapt is Balaban's (CMP 95, 96, 98, 99, 102,
109, 116, 119, 122); J. Dimock's arXiv 1712.10029 is credited where
`library/a3-response.md` uses it. Grok's PRs #10133 to #10135 are not used
here. The comparison leans on `library/sa-histories.md` (row 70),
`library/sa-map.md` (row 69), `library/sa-2.8.md` (row 71),
`library/lit-balaban.md` (row 80, with the lead's CMP 102b check), and our
rarity line (rows 56 to 65 and their gates); each is credited where used.

Status: in progress. Sections are written in order; the decision table is
Section 4.

## 1. The decision in brief

**Large field (Package C position): carry the outline's healed-history
mechanism, not our S1 to S6.** Our rarity line keeps three kinds of reusable
lemma and stops being a route. Reason, in one line: both routes stop at the
same analytic statement (nonlinear A3, the outline's (1b) Theorem 2 first
half on localized backgrounds); the outline's two hardest large-field steps
reduce to it (Section 3.3), while ours needs it **plus** five sector stops that
have narrowed five times without closing (Section 2.3), and the outline's
accounting of depth, many marks and the measure is written and is free of the
three inferences our gates refuted.

**Whole chain:** the outline's skeleton for the hard core (backgrounds,
small-field step, histories, sources), our proofs supplying the coercivity,
flat response and gauge lemmas that it lacks; our upper chain, NT1/NT2
witness and reflection positivity for the consumer side, since T1 asks for
less than Theorem 0 there. The interface is UV-CT, which is already the
outline's D1 form. Section 5 has the table by position.

## 2. Our large-field route: `rarity-fresh-c` S1 to S6, `rarity-fresh-x`, rows 60 to 65

Mechanism: read each rare event one level below its own, conditional on the
exterior there (Lemma EX); keep sparse holes as exterior so the hole
recursion (4.1) has an exponent m_* and no factor per level; price lumps by
Theorem VAL through Lemma PER; dense boxes go to Haar parents
(`rarity-fresh-c.md` Sections 1, 4). The x variant: exact positive partition
by active defect set, Peierls deletion (CD), stopping at (SEP)
(`rarity-fresh-x.md`).

### 2.1 Proved and gated

| Statement | Where | Standing |
|---|---|---|
| Lemma EX (integral comparison) | `rarity-fresh-c.md` 2; `sector-values.md` 3A | ADVANCE twice: `gates/lemma-ex-7c12c6981.md`, `gates/rarity-fresh-c-263afacbd.md` |
| Theorem FC (full-law force bound, product form) | `rarity-fresh-c.md` 2 | ADVANCE (c gate); prices packs, not rough fields |
| Lemma PER (telescoping) | same | ADVANCE, under its strong exterior-independent increment hypothesis |
| RANK privacy | same | ADVANCE; RANK (2.4) itself CORRECT-NO-ADVANCE, its `Dlog` constant WRONG |
| Solving the scalar recursion (4.1) once supplied | same, S4 | ADVANCE |
| Local RANK, corrected `Dlog`, fixed-box entropy, normalized hole sum, margin and charging algebra | `rarity-repair.md` 3, 4, 6 | written, ungated |
| (SP) for windows w <= eps/2, gap >= 11 T^2/24 | `sp-decide.md` 2 | written by hand, ungated |
| (QR) with margin 339/1024 given (RC); exact quadratic formula (4.8) | `qr-decide.md` 2-5 | written, ungated |
| Routing with bounded detours for a singleton cubical collar; local charts below an absolute action cutoff; crude supported reference | `sp-nonlinear.md` 2, 5, 6 | written, ungated |

Nothing in the route's conclusion, (RAR^1) or (RAR^ch) at every depth, is
proved: S1 to S6 are an implication (`rarity-fresh-c.md` 8), and the c gate
found S1, S2, S3, S5, S6 CORRECT-NO-ADVANCE and three WRONG (S3(a)
`(1+p)^N <= 2`, S4 zero parent influence, RANK `Dlog`).

### 2.2 Open steps, hardest first

1. **Uniform pricing of a sparse hole's influence (repaired S4).** The c gate's
   Defect 5 (`rarity-repair.md` (2.1)): excluding r of N lines moves the
   parent by q (a_R - a_H), q = r/N. So (4.1)'s mechanism against Proposition
   HOLES, "a sparse hole does not move a parent", is false, and (4.1) now needs
   a conditional bound on the parent's law near each threshold, uniform over
   every hole pattern below it, at every depth. At d = 4 holes are everywhere
   at a fine enough level, so this is the place where HOLES can return. Only
   the margin algebra is written.
2. **The signed sector comparison at all depths, marks and hole shapes**
   ((SEP); its test form (SP); S1's multiplier bound for a label change,
   `rarity-repair.md` (5.1)-(5.2)). Proved only for two steps, one sparse
   core, one mark, one window family, and then only for w <= eps/2; above that
   it reduces to (QR), then to (RC), then to (AR) plus a sharp reference.
   Row 68 (`rarity-skeleton`), which was to check how each test-case result
   scales in depth, number of marks, hole shape and volume, was stopped
   unfinished.
3. **Nonlinear chart:** the sharp supported reference (energy at most
   E(H_0 y) + 1/64, `qr-decide.md` (6.3)), the numerator extension, and (AR)
   with C_AR independent of the radius (`sp-nonlinear.md` 7).
4. **The order of constants** m_* >= C_D b_2^2 (x gate D2, needed by both of
   our variants) together with m_* << L^2 b_2^2 (S5). Never checked together.
5. **The regular package read by every step:** (I_k), (Loc_k) with its
   first-order tail, Theorem VAL (reads FALL, hence (UP)), (ADD_k). (UP) at
   the nonlinear level stops at (REL)/(REL-D), the shared A3 (Section 3.3).
6. **Consumers that change:** (FF_j)(U) restated as a moment, and (MD*)
   either kept with boundary data (so (I^d), (VAL^d), Lemma ST uniform in the
   data) or Prop 20.4 rewritten (`rarity-fresh-c.md` 6). Neither is done.

### 2.3 Evidence on the hardest step (items 1 and 2 together)

*For.* No counterexample to Wilson rarity has been built in four gates and
two kill lanes: labelled cells, Haar towers, instantons, lumps
(`gates/rarity-fresh-x-0e8a5a4e7.md`), the explicit regular-top face
construction crossing a threshold (`rarity-repair.md` 2, no proved non-rare
mass). The low-window (SP) is proved with an explicit gap. (SEP) is the
classical action excess plus a same-residual fill, not a new obstacle
(x gate). A crude estimate supports item 1: a parent pushed across threshold
by q (a_R - a_H) must already sit within that distance of threshold, an event
whose conditional density is itself exponentially small in x T^2 if a
near-threshold density bound holds uniformly in holes; so item 1 is plausible,
but that density bound is the unproved statement.

*Against.* (a) Each lane since row 60 has ended STOPPED at a narrower
statement: (SP) -> (QR) -> (RC) -> (AR) and sharp reference, five reductions
with no closure of the general statement; How we work item 4 says stop after
two. (b) The gate showed (SEP) is **stronger** than the consumers need (a
finite example has full-law product rarity without (SEP)), so this line was
narrowing toward a statement it need not prove. (c) The zero-influence
failure removed the one mechanism that made (4.1) beat HOLES. (d) A central
-I twist on a cut costs zero action and defeats period charts
(`sp-nonlinear.md` 4), so every chart step must be local, and the local window
change does not settle the original global windows.

### 2.4 What covers depth, many marks and the measure mu

Only implications that read the broken steps: S4's recursion (reads zero
influence), S5's product (4.2) (reads S4 and rough-parent accounting the c
gate found absent), S6 under mu (terminal comparison absent). The test-case
results (SP), (QR), (RC), local windows, local chart, (AR) are all one mark,
two steps, one hole; their general forms were never written (row 68 stopped).
Volume: window extension costs Q^2 unless local windows are used
(`qr-decide.md`).

### 2.5 Distance to the consumers (our upper chain)

The rarity statements (RAR^1), (RAR^ch) feed (A1'), Theorem OS, (20.2),
Lemma 22.2 and Theorem 10.7 of the mapped hard core, which must then deliver
UV-CT (or UV-OS) to `parts/upper-chain.md`. On top of the open steps above,
the mapped route still needs (UP) at the nonlinear level ((GLUE-E), (NL-pay);
(PATCH) not needed per `seam-nonlinear-c.md`), (MD*) or its rewrite, the
regular package, and CT1-CT3, which need holomorphy in complex sources: "No
hard-core attempt of ours is holomorphic in sources" (`sa-map.md`, Package D;
mapped Text 5.8). So even a closed rarity would leave our hard core one
analyticity rebuild short of UV-CT.

## 3. The outline's large-field route: Package C, healed histories

Mechanism (SA L17251-19812, read through `sa-histories.md`): `T` stores the
variables of wild regions; the R operation integrates a prepared box and
replaces its law by a normalized small-field reference with Wilson weight;
healed history clusters are erased; component masses carry a supremum
**inside** the integral over a fibre depending on stored variables; a
genealogy count with waiting pays renewed creations. This is Balaban's
CMP 122 structure with named additions (SA L17290-17313).

### 3.1 Proved, and gated here

**Nothing of Package C is proved or gated here, and the outline's own index
keeps 2.8, 2.10, 2.12, 2.13 open** (SA L32891-32914). What is written as a
conditional deduction (a finite argument from displayed hypotheses,
`sa-histories.md` 3-5): the measure/formula separation (L17499-17517), the
volume, skeleton, waiting and reserve inequalities with no factor per
unmarked level (L18416-18670), literal-history entropy by owned volume
(L18672-18715), the forest sum exp(N_k/M^4) (L19131-19148), OSF5-OSF7,
OSF9-OSF10, and the ordinary-stability deductions OH1-OH8 (L23385-23620).
The genealogy count is complete, with proof, in Sussman-Alpoge YM3_I
(Props II-75-45, II-75-106) and in Dimock III (`lit-large-field.md` 5).
The energy of the averages (L18209-18336) is argued in full from one stated
one-step inequality (`sa-map.md` 3, item 6). Balaban's published R operation
(CMP 122a, b; CMP 119) covers most of the construction, but, by the raw
accounts' reading, prints without proof 122a pp. 178-179 and (1.70),
122b p. 375, 119 p. 276 and CMP 109 Theorem 2; its 122b Theorem 1 assumes all
g_j in (0, gamma], which a first-passage trajectory with g small satisfies if
the flow is monotone, so that hypothesis looks harmless here (my reading,
unchecked) (`lit-balaban.md` 3-4).

### 3.2 Open steps, hardest first

1. **Renewed test outside the old floor** (floor screening; SA L18334-18415,
   item (4) after Lemma 2.5, drop-out mass L18130-18205). `sa-map.md` rank 1:
   new relative to Balaban, who removes failed components.
2. **2.8, the signed ten-term cancellation** (SA L17854-17935): the ten terms
   are described, not displayed; stops at (L) of `sa-2.8.md`, one plaquette of
   the relative holonomy of two admitted backgrounds decaying like e^(-m D).
3. **Analytic inputs to the common envelope** (`sa-histories.md` 7): actual
   triangular charts and Jacobians (L18773), positivity of the reference
   denominator (dangling pointer at L17508), the erasure read/support identity
   (L17958-17982, L18877-18949).
4. **C4, one simultaneous order of constants** (Theorem 2.11, L19435-19470;
   the catalogue says listing its clauses does not discharge it).
5. **2.13 and 2.10 activities** (actual own-variable majorants, vacuum
   matching, connected expansion), given 2.8 and item 3; the counting around
   them is written.
6. **2.12, the aged comparison**: only for consumers that need the stronger
   tuned branch; not on T1's path (`sa-map.md` rank 11).

### 3.3 Evidence on the hardest step

My reading of SA L18334-18415, unchecked: the renewed-test witness argues by
contraposition. If the unspent energy in the new window is below
c l_m^(2p_1-8r), the energy of the averages makes the stored plaquettes at
most varsigma = C g_m l_m^(p_1-4r) ("the unknown field in the floor does not
enter this estimate"); then "the background locality estimate through the
waiting collar" bounds |dU(p) - 1| outside the floor by
C(varsigma + R_m^2 eps_m e^(-delta_0 M R_m)) L^(-2j(p)); then an elementary
shell-loop lemma (holonomy within C n s^2 varpi, telescoping unitary
products, written there) gives the bond test. So the step has three links:
energy of averages (argued in full there), a shell-loop lemma (elementary,
written), and **a weighted-distance decay of the localized background through
a collar of fixed width with arbitrary data in the excluded floor**. The last
is A3 on multiscale regions (catalogue A3, SA L3864-3896: "the corresponding
non-Abelian background and multiscale response estimates remain to be
proved") together with A1 on nested families.

*For.* The two hardest items of Package C, rank 1 and rank 2, therefore
both reduce to the same analytic statement, nonlinear A3 in the profile form
(the outline's (1b) Theorem 2 first half, on localized families), which our
seam chain also needs ((REL)/(REL-D), `a3-response.md` 8 item 3). Its flat
linear part is proved here by hand (Theorem FL, Theorem E,
`a3-response.md`; gate pending), and A1 is Balaban's CMP 102b Theorem 1,
uniform in depth (lead's check of the scan). The structural defects our gates
found in our route are absent from theirs (`sa-histories.md` 7, second
table): no zero-influence claim, product link ball instead of one Euclidean
ball, forest sum paid by an explicit reserve, supremum inside the integral.
The heavy-wall examples placed in their old floor produced no violating
history (`gates/share-check-199fac1cb.md`).

*Against.* The profile form of (1b) Theorem 2 is not in Balaban
(`lit-balaban.md` 4 item 3) and his nonlinear response (189)-(190) is printed
without proof, so A3 curved is new work on either route. Floor screening
asks for decay with **arbitrary** data in the floor; if the localized
background only exists for data regular on the whole window, the
contraposition has no background to test, and the "existence and extension
tests also pass" sentence (SA L18393-18397) carries the weight. The ten
terms of 2.8 are undisplayed, and a signed remainder can fail where every
absolute bound holds (our x gate D1). Thresholds there depend on the coupling
(eps_j = g_j p_0(g_j)), so no zero-temperature limit tests it the way
(3.1) of `rarity-fresh-x.md` tested ours (`sa-histories.md` 3.4).

### 3.4 What covers depth, many marks and mu

Written into the construction, conditionally: Theorem 2.1's induction over
all levels; the owned-volume genealogy with waits, joins and renewed creations
(Prop 2.6, L17719-17797, L18475); disjoint action shares so gains add without
double spending (L18950-19199, L18405-18415); component masses with an
exponential stored-volume reserve (Prop 2.7); the measure is the torus Gibbs
law at first passage, with the positive-label floor OH5-OH6 for the real
lower bound. None is gated here; all read 2.8 and the background theorems.

### 3.5 Distance to the consumers

Theorem 0 reads 358 statements (`sa-ledger.md`); Package C feeds D1
(sources, (ST5)-(ST6)), which is the form our UV-CT already copies
(`sa-map.md` 3 item 1). For **our** T1 the consumer is our upper chain, so the
distance is: Package C closed, plus D1 with 4.11 (holomorphy in sources) and
OH1-OH6, plus the small-field step B1, B2, B4, Prop 1.6 as a holomorphic map,
plus E1/B3 (one-loop). The outline's F2, F3, 7.5, 7.6, Package G and the
reconstruction chain Z are not needed for T1 (Section 5).

## 4. Large-field decision

### 4.1 Side by side

| Question | Ours (S1-S6, rows 56-65) | Outline (Package C) |
|---|---|---|
| Conclusion proved? | No; implication with three WRONG steps found by gate | No; outlined, index keeps 2.8-2.13 open |
| Gated pieces | EX, FC, PER, RANK privacy, scalar recursion (all lemmas, none a producer) | none here |
| Hardest open step | uniform near-threshold pricing of hole influence plus the signed sector comparison, general depth | renewed test outside the floor, then 2.8 |
| What it reduces to | A3 curved (via (UP), (REL)) **plus** (SEP)/(SP) general, S1 multiplier, sharp reference, (AR), m_* order | A3 curved on localized families (both top items), plus undisplayed ten terms, charts, denominator, C4 |
| Depth, many marks, mu | implications reading the broken S4; general forms never written | written conditional count, shares, reserve, floor |
| Published backing | none (new kernel with Haar parents) | Balaban CMP 122, 119 with named unproved pages; count proved in YM3_I and Dimock III |
| Output form | real coupling; UV-CT still needs a holomorphic rebuild | holomorphic in sources by design (D1, 4.11) |
| Recent trend | five narrowing STOPs | untested here except 2.8 (STOPPED at A3) and share-check (no violating history) |

### 4.2 Recommendation

**Carry the outline's Package C as the large-field route.** By the owner's
test ("only follow their route if its better than ours"), it is better on
the evidence in hand: (i) it adds no hard analytic statement beyond the
shared A3 at its two hardest steps, where ours adds at least four; (ii) it
covers depth, marks and the measure with written accounting where ours has
only implications through a refuted step; (iii) it is holomorphic in sources,
which UV-CT needs and our route is not; (iv) its gaps are named, page by
page, against a published construction.

**Retire as route obligations:** (SEP), (SP) beyond its proved window,
(QR), (RC), (AR), the sharp reference, S1's label-change multiplier bound,
the m_* order, and the repaired S4. They are not obligations of Package C
(`sa-histories.md` 6.1-6.9). Do not open further lanes on them.

**Keep and port as lemmas into Package C** (each must be rechecked against
the outline's operators before use): Lemma EX and Theorem FC (integral
comparisons); fixed-box entropy and normalized hole integration
(`rarity-repair.md` 4) for the 2.13 checks; the exact changed-fibre
decomposition and signed-minimum formula (`sp-decide.md` (4.1), (4.8)) and
the Gram perturbation estimates (`qr-decide.md` 2-5) as diagnostics for the
2.8 ten terms; local small-action charts with summed Taylor errors
(`sp-nonlinear.md` 5) for the chart Jacobians; Lemma U
(`lattice-uhlenbeck.md`, gated) and the flat response (`a3-response.md`) for
A1, A3.

**Next lanes on this position, in order:** (1) nonlinear A3 in profile form
on localized families (the shared blocker; continues row 77 and row 81);
(2) floor screening checked on its own: does the localized background exist
and decay with arbitrary data in the excluded floor (SA L18353-18397)?
(3) display and bound the ten terms of 2.8 with the signed-minimum
diagnostics; (4) C4, which is cheap to decide.

### 4.3 What would reverse it

- **A counterexample in Package C's floor screening:** a history whose
  energy outside the old floor is below c l_m^(2p_1-8r) but whose localized
  background fails a test outside the floor, for example a heavy wall in the
  floor whose influence through a fixed-width collar is not
  R_m^2 eps_m e^(-delta_0 M R_m)-small. That would kill rank 1, and our route
  (which has no floor) would return as the candidate.
- **2.8 refuted:** a prepared component on which the signed ten-term
  remainder is not small although each term's absolute bound holds.
- **A3 curved in profile form refuted** on localized families with
  arbitrary excluded data, while a weaker form that only our (REL-D) needs
  (an l^1 shell sum in the admissible gauge) still holds. Then the outline's
  top items fail and ours keep their input.
- **Our hardest step closed in general form:** a proof of uniform
  near-threshold pricing of hole influence and of (SP) at every depth with
  many marks. Then ours is a complete rarity route and the comparison should
  be rerun on cost to UV-CT.
- **C4 inconsistent:** no single order of constants satisfies Theorem 2.11's
  clauses together.

## 5. The whole chain, position by position

Positions are the thirteen of `sa-ledger.md` (L, M, G, E, N, P, C, T, R, K,
H, V, Z), plus the two that only our target has (the interface and the
NT1/NT2 witness). "T1 needs" says whether GOAL.md's T1 reads the position
(existence of a non-trivial, reflection-positive, hypercubic limit on R^4
along a chosen trajectory). All outline rows are `unchecked` here; "gated"
means a gate of this folder, one cross-provider read, no status.

| Pos. | T1 needs | Ours: proved / gated | Theirs (outline) | Carry | Reason | Reverses if |
|---|---|---|---|---|---|---|
| **L** Gibbs laws, reflections | RP across planes only | upper chain Lemma 1.1, site-plane RP after Osterwalder-Seiler, proof written | G1, all coordinate and diagonal mirrors, every periodic DLR state; link symmetry (ledger 11, 12) | **ours** | T1 asks for hypercubic invariance and plane RP; diagonal mirrors serve their rotations and source transfer, off our path | we adopt their D1/R chessboard transfer verbatim and it reads diagonal mirrors (then take G1 with it) |
| **M** constrained linear block estimates (A2, A3 flat) | yes | flat and curved D-coer chain (`fan-ext`, `fd-local`, `lc-u`, `c0-loc`, gated); quadratic (LC) and Lemma U gated (`gates/share-check-199fac1cb.md`); Theorem FL and Theorem E by hand (`a3-response.md`, gate pending) | flat kernels only (CF18, WI15; A2, A3 open in their own catalogue) | **ours, into their skeleton** | we hold the only curved coercivity and the only multiscale flat response with a hand proof; port onto their block average and gauge (row 78 for A2) | the A3 gate (row 77) finds Theorem FL or E WRONG, or row 78 shows our class map's coercivity does not transfer to their conditioning sets |
| **G** nonabelian backgrounds (A1, (1b) Theorems 1-6) | yes | (R2), (R3) of mapped Text 5.3 open; Lemma PG; r3-global stopped; a1-orbit fixed-geometry A1 (Codex, ungated) | Balaban CMP 102b Theorem 1 (p. 279), unique orbit uniform in depth, proof in Sects. C-G (lead checked the scan); (1b) Theorem 2 second half = CMP 99a Prop 6 | **theirs (Balaban's), ported by us** | a published depth-uniform proof exists; ours has none; row 81 ports it | row 81 finds his average, axial gauge or uniqueness class (a)-(c) of `lit-balaban.md` 4 does not match, and the gap cannot be bridged |
| **G** nonlinear response (A3 curved; (1b) Thm 2 first half, Thms 4, 6(c)) | yes | Theorem CL (curved linear, implication), Lemma LR flat; nonlinear Theorem E open | outlined, open (catalogue A3); Balaban's (189)-(190) printed without proof; profile form not in Balaban | **one statement, both routes; ours to prove** | the shared blocker; no published proof to port | none: whoever proves it supplies both |
| **E** marginal action, coefficient | yes (one-loop rate for NT2, flow) | Theorem P1 (one-loop telescoping), p1-gate CORRECT-NO-ADVANCE with one WRONG (higher-derivative bound (E)); already adopts their S(T,M) and Ward spin coefficient, credited | B3, heat-kernel trace (L3986, ledger 9); Balaban's Theorem 8 stated without proof | **both, merged into P1** | P1 is nearest closure and already uses their pieces; their B3 is an alternative proof of the same number | P1's Lemma 3.2 or massless-inverse step fails and B3's route closes first |
| **N** exact local nonlinear step (B1, B2, B4, Prop 1.6, WF room) | yes | real-coupling one-step theorems (`one-step-closure.md`, gate `closure-bad958abb`; `sector-values.md`; `analytic-lift.md`); independent Texts 4-5 with WRONG at (GOOD) | holomorphic one-step map (Prop 1.6) and substitution room (ledger 4), open, Balaban-type (CMP 109, 116, 119) | **theirs** | UV-CT reads complex sources; ours is real only | a holomorphic version of our one-step closure is written and gated first |
| **P** free Gaussian curvature term | for NT2 | `nt2-free-value-by-hand.md` (a different free computation) | free curvature model (L1379, L1670) | **ours** for NT2; theirs only feeds V | NT2 is defined by our witness, not by their 0(c) | NT2's definition is changed to their F2/F3 form |
| **C** continuum limits | yes | upper chain: volume-free local bounds, joint limit on R^4 (`parts/upper-chain.md`; status: 41 discharged, 25 implication, 11 gap) | spectral cones, mirror inheritance, 0(a)-(b), 0' | **ours** | reads UV-CT, which is their D1 form; T1 needs separated tests only, not their cones | the upper chain's conditional theorems fail on a clause that D1 does not supply and their C does |
| **T** running coupling, first passage | yes | mapped Lemma FLOW uses their first-passage datum (duplicate, credited) | first passage K(beta, g); E1, E2; stronger tuning E3, E4 | **theirs** for the flow statement; E3, E4, 2.12 **not carried** | same definition; tuned whole-sequence branch is off T1's path | T1's trajectory is changed to need matched cutoffs |
| **R** sources, normalized response (D1, 4.11, OH1-OH8) | yes, as the interface | UV-CT is the consumer copy (CT1-CT4; gate `uv-ct-upper-chain-41489e4876.md`: implications hold, UV-CT open); no holomorphic producer | D1 (ST5)-(ST6): holomorphic point counterterms, localized source energies, normalized upper stability and unsourced floor, uniform in cutoff and torus; OH1-OH8 written conditionally | **theirs as producer, ours as consumer** | the form is already shared; their producer is analytic | a clause-by-clause check finds UV-CT reads something D1 lacks (e.g. CT4's volume floor at side 2a_*, or the cutoff-free tau of CT3), with no cheap bridge |
| **K** components, clustering | no | none | canonical decomposition, unique component vacuum (0') | **neither** | T1 does not ask for a phase decomposition | T1 is strengthened to a unique vacuum |
| **H** histories, partition bounds (Package C) | yes | Section 2: lemmas only | Section 3: outlined, conditional accounting written | **theirs** (Section 4) | Section 4.2 | Section 4.3 |
| **V** interacting two-point law, transfer (F2, F3, 7.5, 7.6, 7a.1.8, 4.14) | NT2 needs a UV law across scales | witness line (`parts/witness.md`, Text 8.1; status: 18 discharged, 12 implication, 8 gap); 7.5 is not an interaction witness in NT2's sense | F2, F3 (ledger 8, 15), 7.6 (ledger 13) | **ours** for NT1, NT2; F2/F3 **kept as a candidate supplier**, not carried | NT2 is a positive identification that their 0(c) does not state; F2 may supply its leading coefficient | `parts/witness.md` shows NT2's leading-order clause is exactly F2 at its scales; then carry F2 |
| **Z** rotations, reconstruction, assembly | reconstruction on separated tests, hypercubic only | upper chain reconstruction on separated tests | Package G (optional), angular route, AK gluing, AC divisibility, H3 OS theorem (ledger 17-20) | **ours** | O(4) is a later target; their Z serves O(4) and 0' | O(4) is brought onto the path |
| **Interface** UV-CT / UV-OS | yes | UV-CT drafted (GOAL.md), UV-OS alternative | D1 | **UV-CT = D1 form** | already credited as theirs; keeps the hard core swappable | as for R |
| **Witness** NT1, NT2 | yes | ours only | none (no interaction witness, `sa-map.md` 3) | **ours** | no alternative | none |

**Net:** the hard core (G, N, H, R producer, T flow) is carried on the
outline's skeleton, which is Balaban's, with our M lemmas, our A3 work and our
Lemma U supplying what it lacks; the consumer side (L, C, Z, witness) is ours
because T1 is smaller than Theorem 0 there; E is merged; K, E3/E4, 2.12,
Package G, 7.5 and the outline's Z beyond reconstruction are not carried.
Every carried outline statement still has to be re-derived here and gated
before it counts (FINISH, How we work item 2).

