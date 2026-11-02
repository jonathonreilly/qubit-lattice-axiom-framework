lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T09:45Z

# Gate: `library/flat-port.md` (row 99, `flat-port-gate`)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session; statement pinned at commit d9608eeeb on `claude/ym4d-hard-route`; gate by hand of a Codex text (OpenAI Codex, GPT-6, checkout 02c07af23). One cross-provider read, not an audit; grants no status. Sources checked: Balaban CMP 89, 95, 96, 99b OCR in `~/ym4d-papers/` with the cited displays read on the page scans (rendered locally; nothing copied into the repository); Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched to a scratch folder. Credit: T. Balaban for every propagator construction checked here; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline, its default convention and the straightened average.

Status: in progress, written section by section. Verdicts so far are below; later sections are added as they are checked.

## Verdicts per section

| Section | Verdict | Note |
|---|---|---|
| 2.1 level-0 convention, identity QD ker Q' = 0 | ADVANCE | Counterexample to the retained-row identity checked; default identity (2.2) holds at interior, outward and bare rows. |
| 2.2 omitted-bond estimate (2.3), and (2.4) | ADVANCE (as a side estimate) | Constants 2L and 160 L^4 rechecked; the note rightly does not treat (2.3) as the vector theorem. |
| 3 flat K* column bound (3.1)-(3.5) | ADVANCE | Discharges D1 of `gates/a3-profile-gate.md` at U_0 = 1, A = 0 in the consumer's normalization (SA 9811-9812, a3-profile (2), Section 6.2). |
| 4.0, 4.1 scalar Poincaré, free local estimate (4.1)-(4.4) | ADVANCE | Standard Schauder argument, correctly sketched; one wording repair (W1). |
| 4.2 mixed scalar inverse (4.5)-(4.7) | ADVANCE, with repair W1 | Reads `a3-balaban.md` (7.15) and (5.2); both rechecked here in the flat case (see below). |
| 5 scalar Gram and projection kernels (5.1)-(5.6) | ADVANCE | Normalizations rechecked: J = J_s m^{-4} (right factor) is symmetric and >= c; N = m^{-4} J^{-1}; P = I - R identified. |
| 6.1 one-scale Fourier coercivity (6.1)-(6.7) | ADVANCE | Every display rederived; uniform in fine mesh and periodic volume. |
| 6.2 two-scale default seam (6.8)-(6.14) | ADVANCE (given (6.11), Section 7) | Decomposition (6.8), (6.9), contraction (6.10), identity (6.12) and (6.13) rederived; level-0 seam is the case n = 1. |
| 7 block estimate (7.1)-(7.5), strict-axial F4 gap | ADVANCE | Matches CMP 96 Lemma 2.4 on the scan, (2.128): gap (12 d^2)^{-1} L^{-d-1}; the note's row coefficient L^{d+1} is sharper than Balaban's L^{2d-1}, harmless. |
| 8.1 saddle system (8.1)-(8.5) | ADVANCE | Elimination (8.2) gives exactly T = C*C + DRD* + Q*aQ; (8.4) rederived; local bounds on one-scale, two-scale and bare models. |
| 8.2 parametrix (8.6)-(8.10) | ADVANCE | Every commutator block checked (scalar second order, pillar mass, first order, vector curl, row mass, top average); bounded overlap; M chosen before the gap. |
| 8.3 decay and (F0-E) (8.11)-(8.12) | ADVANCE | Walk-length argument gives the localized L^2 kernels; T >= c_L J_E follows from the inverse bound. This is default F0-E, level-0 seam included. |
| 9.1 pointwise derivatives (9.1)-(9.4) | ADVANCE, with repair W1 | Row-mass and projection terms bounded with the stated powers; same small-cube remark as W1. |
| 9.2 row Gram, lift, fibre covariance (9.5)-(9.11) | ADVANCE | Pivot right inverse; Gamma = m J_v m^{-3}; densities match CMP 99b (3.48), (3.132) as confirmed in `gates/a1-balaban-gate.md`; (9.10) cell volume correct; (9.11) checked (K G D R = 0, R D* G D R = R, inverse on the tangent space). |
| 10 F4 actual top support and soft gauge (10.1)-(10.6) | ADVANCE, with repair W2 | Mixed-row identification by composition; (10.1) by the contraction (6.10); fixed-cell gap by compactness (an existence argument, admissible under GOAL); Combes-Thomas for the kernels. |
| 11 F5 locality (11.1) | ADVANCE | Read sets are the local model boxes; geometric walk tail gives the extra exponential; derivative upgrade by the homogeneous local system and (4.1). |
| 12 endpoint and order of constants | ADVANCE | Only lower bounds; order L, exponents -> local constants -> M -> rates and unit gaps -> R -> separation -> cube sizes and floors. Compatible with the outline's order (gap number R_1 after M) and with D2 of `gates/a1-balaban-gate.md`. |

Inputs read from `a3-balaban.md` (ungated Codex text) and rechecked here in the flat case: (5.1)-(5.6) scale-distance and summation; (7.10) pillar Poincaré; (7.13)-(7.15) weighted energy (identity for the weight commutator, gradient and pillar-mass coefficient counts, absorption). These are correct at U = 1. This gate does not check their curved versions.

## Defects (ranked; filled in as found)

**W1 (wording, breaks nothing).** Section 4.2 takes cubes of side r equal to a small multiple of m_y/L, but (4.1) is stated for r >= 16 eta. For the finitely many levels with m_y < C_L eta the cube is too small. Repair: at those levels use the bare-output argument of the next paragraph (|u(x)| <= eta^{-2} ||u||_{2,{x}}, neighbour differences, and (5.2) of `a3-balaban.md` for the scale ratio), with constants depending on L. The conclusion (4.7) is unchanged.

**W2 (identification, breaks nothing).** Section 10 proves (10.4) for the note's own top precision A_k of (10.1), built on straight rows, and then calls it the comparison the consumer needs. The outline's soft-gauge precision (CF13), lines 8605-8613, is built on the plain fibre E_k of (CF11). The repair is one line: on the uniform level-k lattice the two minimisations agree, E_k^plain(a) = E_k^straight(a) for every datum a, because P^[k] w = q_k w - D_k sigma(w) and a fine gauge transformation constant on top blocks moves q_k w (respectively P^[k] w) by an arbitrary coarse gradient without changing ||dw||. So (10.4), and the kernel bound (10.5) through (9.6), hold for (CF13) as written. The outline's own (CF12) gives the lower bound directly.

## Positive findings

- **CMP 96 (2.3) at level 0.** The scan (p. 224) prints Lambda_0 = Omega_1^c "for the sets of sites and the sets of bonds" and then asserts that the conditions (2.6), A = B_0 on Lambda_0, are invariant under the gauge transformations (2.7), lambda = 0 on Lambda_0. That invariance holds only if the bonds of Lambda_0 have both ends outside Omega_1, i.e. in the difference reading: a crossing bond <x', x> with x in Omega_1 changes by lambda(x), which (2.7) leaves free. So the paper's own invariance claim supports the default (no-inward) reading at level 0, against the outline's L9625 reading that CMP 96 keeps the level-0 inward bonds. The note avoids relying on either reading, which is the safe course; this observation only lowers the risk flagged in `gates/a1-balaban-gate.md` D1.
