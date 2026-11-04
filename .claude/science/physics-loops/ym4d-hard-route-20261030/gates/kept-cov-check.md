lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T03:38Z

# Check of `library/kept-cov.md` (row 252, `kept-cov-check`)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 64c6f500c. Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL to a scratch folder. One line-by-line reading of Codex's note by the other model. Not an audit. No status. No numeric job was run; every step below is algebra done by hand.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for every outline construction read here: the kept chains and carriage rule (SA 17550-17564), the pivot chart (QC1)-(QC25) (SA 7955-8360), the coarea identity and z^(j) (SA 7481-7487, 17534), the adapted contours (SA 6397-6400), the representatives, node factor and invariant extension (SA 7185, 7747, 7913), the decoupled response (R9) (SA 10354-10401), and the operation R (SA 17585-17640, 17903-17925).

Kind: check of our own new text (Codex). The note proves a covariance step that the outline sketches (SA 17558, 7747, 10401).

Moves: (R-cov), (Gamma), (FG).

## 1. Verdicts

| Statement | Verdict | First failing step |
|---|---|---|
| (1)-(4), kept forms | ADVANCE for the kept form built from A^rel | None. The same steps fail for the outline's absolute-Hessian form (Defect 1). |
| (5)-(8), elimination factors | ADVANCE | None. |
| (9)-(10), the recorded action d_g | ADVANCE | None. |
| (11)-(13), returns | ADVANCE as an implication | None. The starting-node step is one sentence in the note. Section 3.2 supplies it. The native action h_f is presupposed (Defect 2). |
| (14) and the response paragraph | ADVANCE | None, given covariance of the decoupled operators (cited from `gamma-bx.md` Lemma 2 and `a2-full.md` Section 10 item 5). |
| (15), the complete integrand | ADVANCE as an implication | None, with Defects 1-2 written in, older activities invariant by induction, and domain admission. |
| Use for `r-cov-reads.md` (5) | ADVANCE | None. (5) is settled as framed there, with h_f supposed. |
| Use for `r-cov-a.md` (10) | ADVANCE as an implication | None, from the inputs listed in Section 4. |

## 2. Defects

Neither defect breaks a statement once its clause is written in. Defect 1 does break the claim if the outline's own kept form is meant.

**1. The note changes the carried kept form and does not say so.** Equation (2) uses A_j = C_V^T (G^(2),rel_V + Delta_j) C_V. The outline's Delta^(j) contains G^(2)_V, the quadratic part of its soft axial factor (SA 10200-10204, 17531). `gamma-bx.md` Section 1 says the large-field moves keep that absolute factor. `gates/gamma-bx-check.md` Section 4 reads the large-field contour Hessians as absolute.

*Failure without the change.* Step (14) applies (4) at the native action h_f. This action need not be constant on blocks. In the flat witness of Section 3.3, h_f(x) = g(x) at a non-centre site. For the absolute form, the contour Hessian at 1^g is cos(eps), not 1, on the fibre direction at x (`gamma-bx.md` Remark; `r-cov-a.md` (8)). So (4) fails for the outline's form, and so does the invariance of its read.

*Why the change is admissible.* The kept Gaussian is formed once, on Omega_{j+1}. There no block contains a node other than its centre (SA 9783), and the background is block axial (SA 7875). On that slice the two factors are equal as functions of the integration field (`gamma-bx.md` Lemma 1(b)). Later evaluations enter only through carriage differences. These telescope to the value at formation (`r-cov-a.md` (9)). So the measure does not change. Only its split into localised pieces changes. SA 7747 permits the covariant extension from a slice.

*Repair, no new proof.* Add a clause to the corrected carriage prescription: Delta^loc_k and the rejected chains are carried as A^rel pair functions. Correct the sentence in `gamma-bx.md` Section 1: the large-field moves keep the absolute factor G_j of the stored V_j on Omega^c_{j+1}, not inside the carried form. For the kept form, this supplies the "identification with each move's consumed Gaussian" that `gamma-bx-check.md` Section 4 lists as missing: agreement on the slice at formation is enough.

**2. The native action h_f is presupposed, not proved.** Section 5 begins: "For a native factor let p̂_f transform by h_f." Equation (15) needs this for every native pair in the integrand. `r-cov-reads.md` (5) makes the same supposition, so (5) is settled as framed. For (10) it is an input. It holds for the argument p (h_f = g). It holds for the interpolated pairs by the note's (R9) paragraph. It holds for each critical background whose data enter through returns or lifts, by uniqueness of its critical orbit (SA 7747, 9783(c); Proposition 2.4 for V_Lambda, as in `r-cov-a.md` Section 3). Repair: name it as an input with these sources.

## 3. Steps redone

### 3.1 Kept forms and elimination factors

- (2): Lemma 1(c) of `gamma-bx.md` (trace identities at real g), covariance of Delta_k and C_V (`a2-full.md` Section 10 item 5, used in Lemma 2, which Codex checked), and (6) for C_V. Masks are scalar per bond. D_j(g) preserves each compressed space, so inverses intertwine. Walk terms are covariant by Lemma 2(iii). (3) is algebra.
- (4): the keep rule reads only the cells a chain meets and the regions Omega_{j+1}, Z_{j+1}. These are history data, and T_g fixes the history. Normal convergence passes (3) to the sum.
- (5): differentiate (QC10) at a = 0; the pivot column of K_V gives the J_c rule. Ad(g) is in SO(3), so det J_c is invariant.
- (6): from (QC19), pivot rows by the J_c rule, nonpivot rows zero, and iota D_F = D_E iota.
- (7): D_C d_V(t) solves the transformed (QC22). D_E and D_C preserve the sup-norm balls, so the uniqueness of (QC22)-(QC23) applies. The straightening derivative is block triangular (SA 8344), so its pivot blocks are conjugate. The Haar density reads (1/2) tr a^2.
- (8): by SA 7481-7487 and (QC25), z^(j)(c) is (det J_c)^{-1} times fixed constants, and it reads V = M^j U only. It is invariant under every admitted frame change of its own pair, so it needs no return identity.

### 3.2 The starting node of a return

The note says only: "An interior root inherits its action through (9) or (10)." Here is the step. Let y be the top of the recorded tower of a stored site x in a level-k component X, and let d = d_g.

- (a) The native pair is the argument p, or an Ax° representative (SA 7185). Then r_f(y) = 1. Also h_f(y) = g(y) = d(y), since y is a level-k site.
- (b) The native pair is a Landau representative U_L = U_A^{u^{-1}}, where U_A is the Ax° representative. Its averages are the datum moved by the node factor n = u^{-1} (SA 7747). So the return at a node is r_f = n^{-1}. The new datum is V^d. By SA 7185 the new Ax° representative is U_A^{d~}, with d~ the lift of d. The new Landau representative is (U_A^{d~})^{u'^{-1}} = U_L^{h_f}, with h_f = u'^{-1} d~ u. At the nodes h_f = n' d n^{-1}. Hence r'_f h_f r_f^{-1} = n'^{-1}(n' d n^{-1}) n = d.
- (c) A junction y_J is reached from a top z by an inward bond b. The return makes the reduced average R(b) equal to the datum V(b): r(y_J) = V(b)^{-1} r(z) R(b). Under the substitution V(b) goes to d(z) V(b) d(y_J)^{-1}, and R(b) goes to h(z) R(b) h(y_J)^{-1}. With the identity at z, this gives r'(y_J) h(y_J) = d(y_J) r(y_J).
- (d) At the tree root o, r_f(o) = 1 and h_f(o) = g(o) = d(o). By (10), the composite action is g(o) on the box interior.

Then (12) carries the identity down each pillar, because d_g is constant on level-k blocks and on each refixed box.

### 3.3 The flat witness of `r-cov-a.md` (8) passes through the returns

Take p = (1,0). Put g = e^{i eps T} at one non-centre site x of level j < k inside X, and g = 1 elsewhere. Then d_g = 1. Let the kept form's native pair be p, and let a stored bond b start at x. Its pillar top y has g(y) = 1.

- Before: r_f(x) = tau[1](y,x) = 1.
- After: r'_f(x) = tau[1^g](y,x) = g(y) g(x)^{-1} = e^{-i eps T}.
- So r'_f(x) h_f(x) r_f(x)^{-1} = e^{-i eps T} e^{i eps T} = 1 = d_g(x). This is (13).

By (14) the native coordinate turns by Ad(g(x)). The A^rel form is covariant under g, so the read does not change. The absolute form is not covariant (cos eps), so its read changes. The returns move the witness from the coordinate to the form, and the clause of Defect 1 removes it there.

### 3.4 Recorded action, tests and the response paragraph

- (9): (W^v)^{u'} = W^{u'v} = (W^u)^l. u' fixes coarse sites, since l = v there. Left and right translation preserve Haar measure. l is constant on each gauge block, so the absolute factor is unchanged.
- (10): the path product telescopes. Refixing with the root fixed leaves the constant v(o).
- d_g is the level-k lift inside X and the root value on refixed boxes. So d_g is constant on every gauge block of level at most k. This also covers the absolute factors at node pairs inside one level-k block.
- Tests: averages depend on a gauge only at their coarse endpoints. So a fluctuation logarithm at a stored bond needs (13) only at the bond's endpoints. Plaquette tests conjugate at their base site. The strip map conjugates, since its cutoff reads only |log W'|. The tree delta, the B-test, the last-shell test and the reference law conjugate by g(o) (`r-cov-a.md` (3)-(5), redone).
- Response: each decoupled operator intertwines, the walk parameters are scalars, and the weighted norms are invariant under real conjugation. So uniqueness of the small solution of (R9) gives covariance at every (s, lambda) (SA 10401).

## 4. What the consumers get

- **`r-cov-reads.md` (5): settled.** For every factor f and every stored site x it reads, r'_f h_f r_f^{-1} = d_g(x). The action d_g is real and the same for all factors. It does not depend on a background, an integration variable or a localisation parameter.
- **`r-cov-a.md` (10): holds as an implication** from Rule (REL') with the clause of Defect 1, native-orbit covariance (Defect 2), `gamma-bx.md` Lemma 2's operator and walk inputs (checked by Codex), covariance of the (R9) operators, invariance of older activities by induction, and domain admission of every lifted and stage core.
- **Corrected carriage prescription, read against SA:** one recorded frame per stored coordinate, kept at its original site (SA 17923); the tree entrances of the operation frame (SA 17598, 17604); returns at every localisation parameter by adapted transport of the factor's own pair, pinned at former tops (SA 6399, 7913). These agree with the outline at physical parameters and fill what it leaves open. The fourth clause of Defect 1 must be added.
- **So (R-cov), (Gamma) and (FG) reduce to domain admission** (the note's named open input, as in `gamma-bx-check.md` Section 4) once the two clauses are written. The row 249 expectation stands with that addition.

What this check does not show. I did not redo Lemma 2's walk covariance, the covariance of the six propagators, or the uniqueness of each native critical orbit; these are cited. I used the integrand inventory of `r-cov-reads.md` Section 4 and did not list the factors of SA's R independently.

## Result

Checked line by line by Claude, first failing step none: (4) for the A^rel kept form, (8), (13) and (15) hold as implications, and they settle `r-cov-reads.md` (5) and `r-cov-a.md` (10). Two clauses must be written in. First, kept forms are carried as A^rel pair functions; for the outline's absolute form, (4) is false off the block-axial slice. Second, the native action h_f is an input that follows from orbit uniqueness. Open: domain admission of every lifted and stage core.
