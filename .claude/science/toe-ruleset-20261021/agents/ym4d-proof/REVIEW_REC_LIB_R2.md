# Independent hostile rereview of REC-LIB

**LAND for the explicitly conditional library artifact.** The tensor norm
error that caused R1's HOLD is corrected. All four binding items are
satisfied at their stated scope: the source correction is proved, and the
conditions on future reconstruction, consumer, growth and mass-gap claims
remain binding and visibly unfinished. No unconditional REC/N9 completion
or Yang–Mills existence/mass-gap theorem follows from this verdict.

Reviewer: a fresh independent Codex context, 2026-10-29. I authored none of
the reviewed files. No different-model-family independence is asserted.
This is the requested R2 review, not an audit or an integration operation.
Only this file is written; no commits are made.

**Coverage and frozen identities.** Read the complete revised
[REC_LIB.md](REC_LIB.md), [REC_LIB_LOG.md](REC_LIB_LOG.md), and
[REVIEW_REC_LIB.md](REVIEW_REC_LIB.md), including every binding item at
R1 lines 348–373. Checked the cited OSLEAF55 definitions and REC/GROW/tensor
interfaces, its review's F6–F9, ASSEMBLY55 N9/item 18, the SRC producer and
its review's §7, MASS_GAP_TARGET, and the author/approach/reviewer briefs.
Line references below refer to the revised files.

| File | Bytes / lines | SHA-256 |
|---|---|---|
| REC_LIB.md | 74,755 / 1,310 | `3a0052652fd4146fd9803b069624ddc7a5357c1a90ff063875a8514a79ef6ae3` |
| REC_LIB_LOG.md | 20,113 / 415 | `3f667c5b56ff883880e62b6240263b74bb5cb0827f9e39e7508bd48f2456cff0` |
| REVIEW_REC_LIB.md | 27,780 / 416 | `bc3e0605118496656b9757a2ab8008b22a24880dda4a495206f7a10c67f6c286` |

Working HEAD is `4f04b662f4d72d7ef269f6d9693ae9ff6424acf9`; fetched
`origin/main` is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
The relevant local review-loop methodology matches that main revision.
These author artifacts remain untracked candidate material; this review
does not confer main or audit status.

**Provenance — CONFIRMED, preserved through the edits.** The PRE-STATED
block remains statements only. Its first 5,169 bytes still hash to
`8c90178454da5d5a19643cf615105d5aef6d4ebf2bde7650b64098602102809c`.
I reversed the four marked corrections in memory, restoring the quoted
original paragraph, without writing any source file. The result is exactly
68,974 bytes / 1,212 lines with R1's frozen hash
`79e570f5c21c0ceceb4dc076fabb1e7ce696afa1bbd4630da036456d3de53b13`.
Every intermediate source size, line count and hash also matches the
REC-1 through REC-4 log receipts. Thus no other proof text changed.

The log's first 12,761 bytes reproduce its R1 hash exactly, and its
15,951-, 17,281- and 18,694-byte prefixes reproduce all subsequent
pre-append receipts. All nine input hashes in the original log still
match the actual files. These checks preserve R1's first-write provenance
confirmation; I have not independently replayed the historical author
session. The formerly incorrect claim that the boost bound was checked
is expressly superseded at log lines 227–233, rather than silently retained
as current verification.

**Verdict per binding item.**

| R1 item | R2 verdict | Revised source, log, and scope finding |
|---|---|---|
| REC-1: repair arbitrary-direction tensor boost bound | **RESOLVED — correct as scoped.** | REC_LIB lines 893–948 give the direction-dependent and universal bounds for every real unit direction and every complex rapidity, in the fixed Cartesian basis. Lines 1104–1111 propagate the correction to the assembled tensor theorem. Log lines 257–295 accurately describe the correction. The old inequality survives only inside an expressly false, superseded quotation. |
| REC-2: supply R-CONT before claiming completed REC/N9 | **RESOLVED as a binding scope condition; R-CONT remains OPEN.** | Lines 328–384, 1081–1119 and 1244–1258 retain the conditional theorem and explicitly require all-gap/product-domain construction, overlap compatibility, exhaustion, quantitative propagation through unbounded insertion degree, spatial control and desmearing. Log lines 297–335 correctly say no such proof was supplied. Single-cut analyticity and the budget inequalities are not promoted to completion. This meets R1 item 2's express acceptance of an honestly conditional artifact. |
| REC-3: retain the consumer repairs and exact hypotheses | **RESOLVED within this library; external repairs remain OPEN.** | Lines 209–222 retain the insertion count; 264–296 retain separated Euclidean insertions. Lines 1191–1211 and 1265–1310 preserve normalization, reality, absent clustering/unique-vacuum assumption, proper-orthochronous output, mixed-label RP and explicit tensor dictionaries. R-CONSUMERS at line 1260 names the outstanding OSLEAF55/ASSEMBLY55 edits. Log lines 337–375 agree. OSLEAF55 lines 240–241 still print the defective translation weight; this library explicitly does not claim to have repaired that file or closed REC(e)/N9. |
| REC-4: preserve growth and mass-gap producer hypotheses | **RESOLVED as a binding reuse condition; producers remain OPEN.** | Lines 959–1053 and 1215–1239 require Z=1 and uniform unconditional moments with b_0=p+2; use of the cumulant route additionally requires its all-order outer-cumulant and singleton inputs. MG0 requires the complete matching hierarchy and identified full H; MG1–MG4 require actual dense-family decay, a common positive physical rate, controlled common limits and a nonzero excited sector. Log lines 377–415 agree. R-SRC/R-MG remain explicit; no producer result is manufactured by the reconstruction implication. |

For REC-1, an independent norm argument verifies the changed constant.
Put `a=||v||_1` and let `x(t)=exp(t u K(v))x(0)` for real `0≤t≤1`.
Directly from the two block equations,

```text
||K(v)x||_1 = |v·x_spatial| + a|x_0| ≤ a||x||_1,
D⁺||x(t)||_1 ≤ |u| a ||x(t)||_1.
```

Integrating this differential inequality yields `||exp(uK(v))||_1≤e^(a|u|)`
also for complex u. On a tensor block the generator is the sum of its
slot generators; on n field slots its norm is at most `n r_max a`.
Taking the largest direct-sum block gives the asserted
`exp(n r_max ||v||_1 |u|)≤exp(sqrt(3) n r_max |u|)`.
The cases u=0, n=0 and rank zero, and the inverse boost u→−u, are covered.
Coordinate-axis directions have a=1, including the complex boosts used
in locality. The original witness remains exact: v=(3/5,4/5,0), u=log 2
has time-column sum 23/10>2, so reverting to the old universal exponent
would fail. Columnwise Cauchy–Schwarz also verifies the retained real
O(4) bound 2; diagonal phases verify the retained J/C norm-one factors
and `bar C J=C`. No representation beyond the stated finite Cartesian
tensor class is included in this confirmation.

**Earlier confirmations after the edits.** I read the unchanged arguments
as well as the new text and checked their interactions. The recovered
R1 hash establishes preservation, while the following mathematical
checks establish that the correction introduces no lost premise or new
unconditional conclusion. CONFIRMED always retains the printed hypotheses.

| Earlier item | R2 verdict and checked content |
|---|---|
| Step 1: L-DOM/L-HILB/L-INS | **CONFIRMED** (lines 147–296). Flat reflected products are admissible; the displacement squared is r u². Iterated Cauchy–Schwarz with polynomial growth gives contraction, including null vectors. The translated pairing gives a dense adjoint for the separated insertion. |
| Step 2: L-TIME | **CONFIRMED** (298–326), only for single cuts and bounded chains. The spectral estimate gives holomorphy; no domain theorem for products of unbounded insertions is asserted. |
| Step 3: L-CONT disposition | **CONFIRMED as OPEN** (328–384, 1244–1258). The unbounded-degree budget is not an iteration or an exhaustion proof. |
| Step 3: L-BV | **CONFIRMED** (386–452). Interior-direction Taylor integration with order greater than A gives a uniform distribution bound; differentiation in imaginary directions gives the all-approach limit. The assumed tube bound remains essential. |
| Step 4: scalar Lorentz covariance | **CONFIRMED** (454–490). Uniqueness on the maximal totally real slice continues the infinitesimal identities; real boosts stay inside the tube. The tensor constant correction does not enter the scalar argument. |
| Step 5: L-ID/SPEC | **CONFIRMED** (748–780). Analytic continuation of the OS shift identifies the full time-translation group and its generator; Lorentz invariance of spectral support plus H≥0 gives the future cone. |
| Step 6: L-LOCAL | **CONFIRMED** (492–569). The two coordinate-axis boost germs match their original tube sides, agree on the Euclidean spectator slice, and have equal boundary limits by L-BV's uniform estimate. Those axis boosts retain their valid original factor. |
| Step 7: finite scalar labels | **CONFIRMED** (824–845). Mixed-word RP, simultaneous label permutation and the sum norm remain explicit; conversion to a maximum norm costs at most m^n. |
| Step 7: Cartesian tensors | **CONFIRMED after REC-1** (847–957). Wick/reflection identities, phased positive kernels and finite representation factors remain valid with (15.3). The arbitrary-representation bridge remains open. |
| Step 8: flat test domain | **CONFIRMED** (147–201, 1081–1102). The cutoff/Taylor density argument is in the flat space; rotations determine its hierarchy from ordered data. No density in full Euclidean Schwartz space or unique Euclidean contact extension is claimed. |
| L-KERNEL | **CONFIRMED** (571–625). Mixed difference quotients and Cauchy estimates continue vectors; their pairings with the original dense family fix path independence. Full product-domain kernels are an input. |
| L-POS | **CONFIRMED** (627–691). The mixed middle imaginary gap is future timelike. Independent bra/ket regulator limits make boundary vectors Cauchy, and boundary uniqueness proves density in the original OS space. |
| L-GNS | **CONFIRMED** (693–746). Positivity makes the null space a left ideal; fields have a common invariant domain, cyclic vacuum and covariance/locality on that domain. |
| L-GAP | **CONFIRMED** (782–822). Decay annihilates low-energy spectral projections on a dense centered family; Lorentz covariance converts the full Hamiltonian gap to an invariant-mass bound. No decay estimate is derived. |
| L-GROW | **CONFIRMED** (959–1053). Taylor orders 5n and 4n+1 control the separated and near-diagonal regions for Z=1. The resulting order is bounded by 11n. The two partition counts yield p+2 only with the explicit probabilistic inputs; absorbing C^n costs the further factorial. |
| L-VAC | **CONFIRMED** (1055–1077). The two evaluation coordinates are independently attainable, translations act trivially on C², and the hierarchy obeys the stated bounds. This refutes automatic vacuum uniqueness only. |
| Assembled theorem and consumers | **CONFIRMED, conditional** (1079–1119, 1191–1310). Matching tube functions and their bound remain supplied hypotheses; uniqueness of reconstruction is distinct from uniqueness of the invariant vector. All reuse restrictions survive. |

**Residue and import check.** The complete open-residue table at lines
1256–1263 names R-CONT (analytic construction and estimates), R-TENSOR
(general representation dictionary and its analytic input), R-CONSUMERS
(external source repairs), R-SRC (actual unconditional/all-order source
bounds), R-MG (physical dense-family decay, limits, vacuum and nontrivial
excited sector), and R-REVIEW (independent checking). None is claimed as
an author-proved closure. R1 and this report provide independent checking
of the listed conditional lemmas; the conservative author-side R-REVIEW
entry supplies no audit status. Physical identification and the complete
Yang–Mills observable hierarchy remain outside the established result.
Sharp time-zero fields, general spinor representations, disconnected
Poincaré extensions and a Euclidean contact extension are not asserted.

The declared functional-analysis background remains explicit. No specialized
reconstruction or gluing theorem has been smuggled in to discharge
R-CONT. As formulation checks only, the flat tests/radial norms agree with
[Adamo–Moriwaki–Tanimoto §2.5](https://arxiv.org/html/2407.18222v2#S2.SS5),
and the all-degree growth/continuation distinction agrees with
[Kravchuk–Qiao–Rychkov §9.2.2–§9.2.4](https://arxiv.org/html/2104.02090v2#S9.SS2).
These comparisons supply no missing proof. Neither the incomplete
continuation nor the two-state uniqueness witness is used as a no-go for
reconstruction or Yang–Mills theory.

**Checks and disposition.** A recursive, hidden-file-inclusive inventory
found no `checks/rec_*` files, hence no `rec_*_v2*` source, output or runner
to rerun. This agrees with the source and correction log; there was no sandbox
failure and no numerical PASS is claimed. Executed checks were read-only
hash/prefix/source-recovery checks. Mathematical verification was analytic,
including the independent differential-inequality argument above.
One R2 pass is complete: the prior concrete error is resolved, all three
reuse conditions remain enforced, and there are no new binding findings.
No source fixes, commits, formal audit, or landing pipeline were performed.
The verdict admits this conditional library with its named residue.

VERDICT: LAND
