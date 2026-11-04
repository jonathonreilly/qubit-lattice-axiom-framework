lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T03:38Z

# Check of `library/kept-cov.md` (row 252, `kept-cov-check`)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 64c6f500c. Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL to a scratch folder (sha256 d7f77d4d...). One line-by-line reading of a Codex note by the other model. Not an audit. No status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline constructions read here: the kept chains and carriage rule (SA 17550-17564), the pivot chart (QC1)-(QC25) (SA 7955-8360), the coarea identity and z^(j) (SA 7481-7487, 17534), the adapted contours (SA 6397-6400), the node factor and invariant extension (SA 7747-7754), and the operation R (SA 17585-17640).

Status: in progress. Sections below are written as each step is checked.

## 1. Kept forms, Section 3, equations (1)-(4)

| Step | Verdict | Note |
|---|---|---|
| (1), orthogonality of D_j(g), masks commute | ADVANCE | Ad(g) is orthogonal for the trace pairing at real g. Masks are scalar per bond. |
| (2) for A_j built with G^(2),rel | ADVANCE, given its inputs | Lemma 1(c) of `gamma-bx.md` (trace identities, real g), covariance of Delta_k and C_V (cited there, checked by Codex in `gates/gamma-bx-check.md` Section 1), and (6) below for C_V. |
| Compression, inverse, walk terms, (3) | ADVANCE | Masks commute with D_j(g); D_j(g) preserves each compressed space. Walk-term covariance is Lemma 2(iii), checked by Codex. (3) is algebra. |
| Selector and (4) | ADVANCE | The keep rule reads only the cells met and the regions Omega_{j+1}, Z_{j+1}. These are history data, fixed by T_g. Normal convergence passes (3) to the sum. |

Scope of (2) and (4). They hold for the kept form built from A^rel (Rule (REL')). The kept form that SA writes uses SA's soft axial factor, with quadratic part G^(2)_V (SA 10200-10204, 17531). On the block-axial slice the two agree (`gamma-bx.md` Lemma 1(b)). Off the slice they differ: at the flat pair 1^g with g = e^{i eps T} at one non-centre site, the absolute contour Hessian is cos(eps) on the fibre direction, not 1 (`gamma-bx.md` Remark; `r-cov-a.md` (8)). So (4) is false for the absolute kept form as a pair function. The note's choice is the covariant extension from the slice. SA 7754 permits it ("a function constructed on a slice ... has a unique invariant extension"). The note does not say that it changes the pair function. Section 5 of this check records what this choice requires.

## 2. Elimination factors, Section 4, equations (5)-(8)

| Step | Verdict | Note |
|---|---|---|
| (5) | ADVANCE | Differentiate (QC10) at a = 0. The pivot column of K_V gives the J_c rule; D_E is diagonal in bonds. |
| det J_c invariant | ADVANCE | Ad(g) is in SO(3), and in SO(3,C) for complex g. |
| (6) | ADVANCE | Checked from (QC19): pivot rows by the J_c rule, nonpivots zero, and iota D_F = D_E iota. |
| (7) | ADVANCE | D_C d_V(t) solves the transformed (QC22). D_E and D_C preserve the sup-norm balls, so uniqueness in (QC22)-(QC23) applies. |
| Pivot blocks, Haar density | ADVANCE | The straightening derivative is block triangular (SA 8342-8346). Its pivot blocks are conjugate. sigma reads (1/2) tr a^2. |
| (8) | ADVANCE | SA 7481-7487 and (QC25): z^(j)(c) is (det J_c)^{-1} times fixed constants. It reads V = M^j U only. |

Equation (8) needs no return identity: z^(j) is invariant under any admitted frame change, real or complex, of its own pair.
