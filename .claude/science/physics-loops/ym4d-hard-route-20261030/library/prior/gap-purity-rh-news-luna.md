# Repo search

The pinned checkout is `f616e5e922e7b230408f5f031a0504b9924af9ee`.
The task says the lead searched `origin/main` and YM4D PRs #10114, #10133,
#10134 and #10141 before queueing this item. The row has no named file or
line hit under “Repo prior work” to open.

`library/prior/repo-search-2026-11-08.md` exists. It is a retroactive digest
for FINISH row 531, not this RH task. Its search covers Yang–Mills lemmas and
notes. It reports no newly found result for its November 8 target. It does not
search for Alpoge’s Riemann proof. The lane registry and its Sussman–Alpoge
index also have no RH-specific entry in the terms searched. These records do
not identify an RH proof or duplicate source in this checkout. I did not repeat
the lead’s repository-branch search.

## Scope and source baseline

I read the lane goal and the requested sections of `FINISH.md`. I also read
`SCIENCE_WORKFLOW.md` from the pinned Git object because this sparse checkout
does not contain the file. The queue is a reading task. I wrote no proof and
ran no mathematical computation.

I fetched the pinned Sussman–Alpoge YM4 outline and CA-I once each to a new
scratch directory. The index README says it covers the YM4 outline. Exact
searches found no Riemann-hypothesis entry. The matches for “zeta” are the
outline’s Greek source variable, not the zeta function. This YM4 material does
not bear on the RH question. I import no result from it. Credit for this index
and account belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text.

The comparison baseline is Michael O. Rubinstein, *The Alpöge–Claude proof of
the Riemann hypothesis explained for the Riemann zeta function*, version 2,
working draft, 22 November 2026, 265 pages. His current index still lists that
same version and date. It says v2 adds the construction, a reduction to thirteen
classical hypotheses, a full lemniscate example, and a census of Lean inputs.
It also says none of the thirteen hypotheses is proved outright. I found no
v3 or later revision of this zeta-function explainer. Thus there is no v2-to-v3
diff to report. [Rubinstein’s index](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/),
lines 10–17; v2, Part I, §§1–2 and 12, and Part III, §1.

## New formal proof and guide

**Luke Sernau, colleagues at Anthropic, and Claude, “GRH for Dirichlet
L-functions, in Lean 4,” repository release, 25 November 2026, commit
`72fead10`.** The repository has a readable edition and a compact edition.
Both prove the same five headline statements as Alpöge’s archive. Sutherland’s
MIT page records 803 files and 477,124 lines for the readable edition, and 794
files and 112,827 lines for the compact edition. It reports that both compile,
use only Lean’s three standard axioms, and pass kernel and independent-checker
runs. This is a separate, shorter formalization of the same theorem statements.
It is not a new version of Rubinstein’s 265-page v2. Sernau’s README says the
shorter proof is based on Alpöge’s work, was produced with Anthropic colleagues
and Claude, and comes without a paper or human reading of the full proof. It
gives no search narrative. [Sernau’s repository](https://github.com/lsernau/grh-lean),
README; [Sutherland’s short-proof report](https://math.mit.edu/~drew/shortgrh/),
updated 27 November, §§Summary and checks.

**Michael O. Rubinstein, “An outline of the shortened proof of the Riemann
Hypothesis,” version 1.5, 27 November 2026, 45 pages.** I downloaded its PDF
and TeX source to the new, empty directory
`~/ym4d-papers/alpoge-rh/news-after-2026-11-22.NITxIv/`.
The files are `rh-outline-v1.5.pdf` and `rh-outline-v1.5.tex`.
This is a new guide to Sernau’s shorter proof, not an update to v2. The guide
organizes the work into fifteen steps. It reduces RH to an inert-prime sum,
then explains the use of theta lifts and divisibility. It replaces some of the
older account’s route: an explicit local formula gives divisibility, Poisson
summation gives a sieve estimate, and a Gram determinant replaces the earlier
lattice-slope comparison. The Vandiver-type cohomology bound is avoided.

The guide proves the first three analytic steps and the deduction from its
three central theorems, A, B, and C. It outlines the zero-density step. It
states and outlines A, B, and C, but does not prove them. The formal proof still
supplies these hard steps. So this guide adds a clearer reduction and worked
examples. It does not close the hypotheses that v2 left open. Useful passages:
§0 and Steps 1–15, PDF pp. 1–3; the changed mechanism, §0, PDF p. 3; statements
of what the guide proves and leaves to Lean, [Rubinstein’s page](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/),
lines 5–15. The author says the guide used Claude, Codex, and Gemini to extract
the proof and reshape it as a classical-analytic-number-theory study guide
(PDF p. 3, lines 143–147 in the text extraction). This is an account of the
exposition, not of how the original discovery happened.

**Verification update.** Andrew Sutherland’s MIT page for the original archive
was updated on 27 November. It now reports all checks finished, including a
full Lean-kernel replay and end-to-end Comparator run completed by 25 November.
The separate short-proof page, also updated on 27 November, reports completed
checks for both Sernau editions. This strengthens the machine-check record. It
does not add a human-readable proof. [Original archive checks](https://math.mit.edu/~drew/grh/),
lines 4–11 and check table; [short-proof checks](https://math.mit.edu/~drew/shortgrh/),
lines 2–13. The joint Lean FRO and Mathlib Initiative statement is dated
21 November, before this search window.

## New expositions and collaboration

**Tokuhiro Eto, “Reading Alpöge’s Proof of the Riemann Hypothesis,” version 1,
25 November 2026, Hexagon preprint 2611.01087.** This is an illustrated guide
for readers outside number theory. It interprets the argument through
Chebyshev’s principle, divisibility, amplification, and cost control. It gives
a separate Lean-checked conditional reduction to six statements. It says it
aims at understanding, not completeness or independent verification. It does
not prove RH. Against v2, it adds conceptual pictures, toy models, a different
explanation of the arithmetic ingredients, and four open questions; it is not
a revised v2. Its account of the discovery points back to Alpöge’s note and
timeline; the new paper offers no new discovery history. See §§1.1–1.3 and
Appendix A, especially pp. 1–3. [Eto’s paper](https://hexagonmath.org/pdf/2611.01087v1).

**Jimmie Adriazola, “The Alpöge–Claude Argument for the Riemann Hypothesis,”
working manuscript, 26 November 2026, 117 pages; and “On the Riemann Hypothesis,”
conditional specialization, 27 November, 59 pages.** The author’s repository
says the 117-page account follows Sernau’s readable refactor. It reduces GRH
to a signed determinant criterion, proves the converse, and leaves construction
estimates open. The 59-page specialization is explicitly incomplete and
conditional. It records a node-spacing mismatch in Section 7. These drafts add
a passage map and a more concrete statement of what remains. They are not
complete human proofs and are not independent verification. The repository
says the priority belongs to Alpöge and Claude. See the README and linked
manuscripts, §§1–7 and status note. [Adriazola’s reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction),
README lines 187–204.

**Terence Tao, with Anurag Sahay, Will Sawin, and Lior Silberman, “G.R.H.
Polymath,” 24 November 2026.** The post launches a public project to bring
separate reading efforts together, produce a readable RH/GRH account, check
related literature, and explore wider versions. It reports no new proof or
check. It is a new coordination effort, not a revision of v2. Lines 13–27.
[Tao’s post](https://terrytao.wordpress.com/2026/11/24/g-r-h-polymath/).

Robin Zhang’s institutional page reports his note as updated on 22 November.
Sinisa Slijepcevic’s outline is dated 21 November. I do not count either as
post-window work. I found no complete, human-readable proof in the post-window
sources. The new papers remain guides, reductions, or conditional drafts.

## Author account and correction

Alpöge’s four-page note is dated 20 November, so it is not a new publication in
this window. It remains the clearest source on how he says the result was
found. On p. 1, he says he brought together two ideas from a toy setting and
guided Claude to the analogous setting; he says Claude supplied much of the
technical work near the end. He describes the key move as adapting Stepanov’s
function-field method without its multiplicity, using a chain of theta lifts
of length about the square root of the prime-sum scale (p. 1). On p. 3, he says
the plan was his, and the theta-lift chain was Claude’s suggestion. The rough
timeline runs from 6 October to 16 November. It lists the Stepanov determinant,
inert-prime divisibility, the sum over prime powers, the theta-lift chain, and
the final GRH step (pp. 3–4). He warns that Claude supplied some timeline
language from a search and that he may need to correct it (p. 3, footnote 4).
[Alpöge’s note](https://alpo.ge/remark.pdf), pp. 1, 3–4.

**Alpöge, X post, 23 November 2026, “Stupid things I did.”** This is a new
author clarification. Item 1 says the 250,000-page figure was a joke, not a
readable proof. Item 2 says the Lean archive contains unnecessary, untidy work;
he accepts this criticism. Item 4 says he views such arguments as raw material
for finding better definitions, and says number fields lack the expected
“H¹ object.” This corrects the page-count impression and clarifies his view of
the purpose of the result. It does not correct a mathematical step in the Lean
proof. The author also says he guided the search and gives Claude substantial
technical credit. [Author’s post](https://x.com/__alpoge__/status/2124987173439209561);
items 1, 2, and 4. The source is his own post; the searchable copy was available
through post mirrors.

**Objection and correction status.** Parker Emmerson submitted an unreviewed
preprint on 23 November and posted it on 24 November: “Alpöge’s Certified Lean
Derivation Does Not Prove the Riemann Hypothesis.” It accepts that Lean derived
the stated theorem, but disputes what the derivation means. It argues from
consistency, the definition of zeta, and a proposed missing geometric witness.
The paper’s own check-status snapshot stops on 23 November. MIT later reported
the outstanding full-kernel and Comparator runs complete. This preprint is a
posted objection, not an accepted correction. I found no official or author
response accepting it as a correction. I found no post-window correction to an
RH theorem, Lean statement, or v2 hypothesis in the trusted sources searched.
[Preprint](https://www.preprints.org/manuscript/202611.2463),
metadata lines 15–25, abstract lines 63–70, and limitations of its snapshot
lines 714–729; [MIT’s later record](https://math.mit.edu/~drew/grh/), updated
27 November.

A separate editorial repair appeared in Adriazola’s own draft: an issue on
27 November proposes adding an explicit condition to fix an overlap in a
definition in that reconstruction. The maintainer notes that a theorem in the
source archive supplies the condition for its concrete family. This corrects
the exposition’s definition. It does not correct the Lean proof. [Issue 8](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/issues/8),
27 November.

## Talks

I found no talk by Alpöge after 22 November that explains how he found the
proof. Two future university talks are listed. Jack Thorne is
scheduled to speak at Cambridge on 1 December about the proof’s status and
ideas. Julian Külshammer is scheduled at Uppsala on 3 December to explain Lean
on simpler examples; that talk says it will not detail the RH proof or its Lean
implementation. These are future events, not published talks or new discovery
accounts. [Cambridge listing](https://www.dpmms.cam.ac.uk/talk/274363),
lines 111–138; [Uppsala listing](https://www.uu.se/en/department/mathematics/events/archive/2026-12-03-seminar-at-uppsala-mathematics-association-s-fall-meeting-what-does-it-mean-that-lean-has-verified-the-proof-of-the-riemann-hypothesis),
lines 11–32.

## Search terms and limits

I searched authors’ pages, Rubinstein’s Waterloo page, Lean FRO and Mathlib
pages, Sutherland’s MIT pages, university listings, and arXiv/Hexagon records.
Searches included: `Alpoge Riemann hypothesis Lean November 2026`, `Alpoge Claude
how found proof`, `site:leanprover-community.github.io Alpoge Riemann`,
`site:math.mit.edu/~drew/grh Alpoge`, `site:arxiv.org Alpöge Riemann
hypothesis November 2026`, `shortened proof Sernau GRH`, `Rubinstein
rh-outline version`, `Riemann proof correction`, `node-spacing incompatibility
Alpoge`, and `Alpoge Riemann talk November 2026`.

I did not find a v3 of Rubinstein’s original v2 guide, a complete human-readable
proof, a post-window mathematical correction accepted by the proof authors or
Lean/Mathlib, or a recorded talk by Alpöge about the discovery. I found two
future university talks, but neither is an account of the proof search. The
latest author account remains Alpöge’s 20 November note, with the 23 November
clarification above. This is a literature note only. It gives no proof or
status.
