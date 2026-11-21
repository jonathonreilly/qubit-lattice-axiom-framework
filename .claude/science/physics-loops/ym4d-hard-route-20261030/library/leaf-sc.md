# Repo search

The lead's search is `prior/repo-search-2026-11-08.md`, §12.
It searched main and PRs #10114, #10133, #10134 and #10141.
It found no outside-lane theorem for the mean/comb completed operators.
`prior/leaf-sc.md` is absent at the requested pin.
The registry search found no separate owner of SC-NATIVE.
FINISH row 541 assigns this leaf; DR-LIFT and PI-ADMIT keep their owners.

I fetched PR #10141 and checked these passages at
`c73ad7b177d94f89ff37b77386936e3d52b48b05`:

| Prior result | What it supplies here |
|---|---|
| `research/ym4d/library/fp1.md:142–168` | Plain and straight flat fibre minima agree by curvature-preserving gradients. This is an energy identity, without a bound on the correcting gradient. We reuse it. |
| `research/ym4d/library/out-pi.md:352–359` | PI uses literal single-contour rows. Calling symmetric rows by the same name is insufficient. |
| `research/ym4d/library/layer-thm-part.md:1333–1341` | Rows, spaces, whole-action Hessian, boundary coefficients and metrics must match. An inner action cannot replace the whole action at a boundary. |

These are prior results of this repository, not new results of this leaf.
I also checked the three soft-route passages on PR #10114 at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`:
`RTARGET.md:695–711` concerns a trivial-background soft saddle;
`BARE_COUPLING_MATCH_ASTRA.md:362–375` concerns a Haar normalizer;
`CODEX_REVIEW_BALX.md:148–151` leaves a historical averaging import pending.
None identifies the present operator.
The additional local hit `print-inverse-r2.md:403–412` already states
the native bare-inverse implication. Section 2 reuses it.
Main supplied `SCIENCE_WORKFLOW.md`. The research pin is
`5e09ceb63dee6bb25006f5c51006f8552f6a481f`.
The shared checkout advanced during this session.
The nine proof inputs used below were compared with that pin and are unchanged.
Only `library/leaf-sc.md` was edited by this worker.

# SC-NATIVE: the native symmetric rows

Checked line by line by Claude (Opus 5.5), gates/leaf-sc-check.md: ADVANCE; minor repairs applied.

Codex, 2026-11-08. FINISH row 541. Research text, not an audit.
This note grants no status. No numerical calculation supplies a proof.
No independent check of this note has occurred.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every port below. Credit Tadeusz Balaban for the
averaging, relative-gauge and multiscale inverse methods.
Y denotes `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
SA and I denote the outline and complete account I at `31a47c543775`.
The existing `/tmp` copies have the prescribed line counts.
Source navigation used `sa-index/README.md`, neighbouring chunk rows,
and `obligations.md` before reading bounded source ranges.
The permitted Balaban paper directory is absent.
His method is read through these existing ports and the account;
no new reading of his original papers is claimed.

## 1. Kill test, before the proof

### Flat two-layer tower: the coordinate test passes

Use odd \(L\), fine spacing \(\eta\), and two levels, \(k=2\).
Put \(\ell_j=L^j\eta\) and

\[
 h_j=\tfrac12(L^j-1)\eta(1,1,1,1).
\]

Apply the fine permutation \(x\mapsto x-h_2\).
Relabel each level-\(j\) row separately by \(y\mapsto y+h_j-h_2\).
Thus level 2 rows do not move; level 1 rows move by

\[
 h_1-h_2=-\tfrac12L(L-1)\eta(1,1,1,1).
\]

This is a level 1 lattice translation. A translated corner block is
exactly the centred block about its relabelled row site.
Translate the regions, their complete reads and the boundary block too.
Every retained field bond and every outward row has the same membership.
Fine weights remain \(\eta^4\); row weights remain \(\ell_j^4\).
Flat differential operators translate with fine coordinates.

At identity both straightened field rows equal the long straight average;
both site rows equal the block mean. The permutations therefore conjugate
the flat mixed operators and their inverses, including boundary entries.
This is the existing proof in `out-pi.md`, Lemma 4.5, lines 618–669.
It is ported here, not reproved as a new flat inverse theorem.
FP1's flat fibre energy identity is also retained with its own conventions.

A fine translation alone fails the test: \(h_2\notin\ell_1\mathbb Z^4\).
Dropping an outward read also fails. Neither operation is used here.

### Noncommuting seam: equality of curved maps fails

Here is a hand calculation using SA 7065–7097's actual local mean.
It isolates the contour choice on common blocks and common endpoints.
It is not a counterexample to an estimate after base-site transport.
Let \(r=(L-1)/2\), \(X=e^{i\epsilon\sigma_1}\) and

\[
 Y=e^{i\epsilon\sigma_2},\qquad
 a=i\epsilon\sigma_1,\quad b=i\epsilon\sigma_2,\quad
 w=(r/L)^2\in(0,1).
\]

Take adjacent centred blocks in direction 3. In the left block put \(X\)
on direction 1 bonds crossing the plane \(x_1=0\), and \(Y\) on direction 2
bonds crossing \(x_2=0\). All other bonds are identity, including the seam
and the right block. Coordinates are relative to the left centre.
For \(x_1,x_2>0\), half the coordinate orders give \(XY\), half give \(YX\).
Other endpoints give \(X\), \(Y\), or identity. Direction 3 segments are identity.

The exponential and logarithm series give

\[
 \log(XY)=a+b+\tfrac12[a,b]+O(\epsilon^3),\qquad
 \log(YX)=a+b-\tfrac12[a,b]+O(\epsilon^3).
\]

The defining equation for the Federbush mean gives
\(\log\operatorname{av}(XY,YX)=a+b+O(\epsilon^3)\).
Consequently, relative to the single contour ordered (1,2),

\[
 \log\mathcal M_m(W)(c)-\log\mathcal M_c(W)(c)
   =-\tfrac w2[a,b]+O(\epsilon^3)
   =wi\epsilon^2\sigma_3+O(\epsilon^3)\ne0
\]

for all sufficiently small nonzero real \(\epsilon\).
Reversing the comb order reverses the leading sign.
The nonzero Taylor coefficient proves this assertion without a numerical run.

In this particular example the difference lies in the lower node factor:
\(\mathcal M_\sigma(W)(c)=u_\sigma(c_-)\), while \(u_\sigma(c_+)=1\).
Thus the straightened row relative to identity is zero in both schemes.
One must not misreport this as a failure of their straightened row estimates.
It refutes the equality of the curved plain constraints and their node factors.
The native route retains each factor and never uses that equality.

The straightened maps can also be distinguished.
Put \(Z_t=e^{ti\sigma_1}\) on the direction 3 crossing links with
\(x_1,x_2>0\), and leave the other crossing links equal to identity.
Each segment then has \(Z_t\) precisely on that quadrant.
Internal contours and both node factors are independent of \(t\).
Write \(A_x^\sigma=\log T^\sigma(y,x)\),
\(\bar A^\sigma=\operatorname{avg}_x A_x^\sigma\), and
\(z_x=ti\sigma_1\,1_{\{x_1,x_2>0\}}\).
The straightened group logarithm is

\[
 \mathcal L_\sigma(t)=
 \log\!\left(e^{-\bar A^\sigma}
       e^{\operatorname{avg}_x\log(e^{A_x^\sigma}e^{z_x})}\right).
\]

Its term bilinear in \(A_x^\sigma,z_x\) is
\(\tfrac12\{\operatorname{avg}[A_x^\sigma,z_x]
                 -[\bar A^\sigma,\bar z]\}\).
Here \(A_x^m-A_x^c=-\tfrac12[a,b]1_{\{x_1,x_2>0\}}
+O(\epsilon^3)\).
The terms quadratic in the linear part of \(A_x^\sigma\) are common.
Thus direct expansion to degree three gives

\[
 \partial_t(\mathcal L_m-\mathcal L_c)(0)
 =-\frac{w(1-w)}4[[a,b],i\sigma_1]+O(\epsilon^3)
 =-i w(1-w)\epsilon^2\sigma_2+O(\epsilon^3)\ne0.
 \tag{K}
\]

This also rejects equality of the curved straightened maps.
It still gives no failure of an estimate. The perturbation can be made
arbitrarily small on this finite seam, including its difference stencils.

## 2. Exact scope and the existing native input

**Claim.** On the admitted PI/GW frames, the PI, GW and GW1 proofs apply
to the prescribed symmetric mean. They give the same types of bounds.
Constants may increase by fixed amounts, and common radii may decrease.
These choices precede the tower, depth, volume and history.
Fix \(SU(N)\), odd \(L\ge3\), and \(0<\beta_0<1\) as in those proofs.
The claim holds for every finite admitted tower and every pair in the
common complex domain, after the fixed choices in (8).

Here “admitted” retains PI's (S1-loc), (S2), (S2+), complete reads,
flat and actual separation floors, and torus room.
Use its touching field bonds, zero extensions and no-inward row convention.
Keep the compressed whole Wilson action, including protruding plaquettes.
Translate the whole tower by the coordinate identification in §1.
Every frame is the supplied frame on that translated read.
No new frame, boundary gluing assertion, or admission from S1 is assumed.

The independent current satisfies GW1's fixed ceiling.
All operators use the symmetric mean throughout: field average, site
average, straightening, accumulated node factors and relative slice.
This claim concerns the existing inverse and word consumers.
It does not assert a nonlinear equivalence of the two fibres.

There is further prior work: `print-inverse-r2.md:403–412` already states
the native bare-inverse implication, with a possible read enlargement.
It says the proof uses only Lemma 4.4's five row properties.
The later `b98p5.md:255–370,394–436` supplies the symmetric prescription
on the exact double-block read. We use this sharper existing input.
Thus the bare inverse is not a new theorem of this note.
What remains is its literal normalization and its use by GW/GW1.

The qualitative six axioms alone do not give numerical derivative bounds.
We use them together with the quantitative bounds for this prescribed mean.
Y 4007–4028 lists the axioms and the flat linear identification.
SA 7065–7116 defines the mean, straightening and site average.
SA 11508–11548 proves their finite analytic recursion and factorization.
These steps are Sussman and Alpoge's, authored with Claude and Codex.
The supplied-frame proof and its complex extension are the repository's
`b98p5.md` §§2.1–2.5. Its full-account admission lemma is not used.

Here is the check of the six axioms for that mean.
Endpoint covariance follows from the mean's uniqueness, after anchoring
all paths at one path. Every path stays in its block and uses fewer
than \(L\) edges per direction. Coarse translations preserve the path multiset.
For real links the near-identity logarithm equation stays in the real Lie
algebra, so its solution is group valued.
The contraction is holomorphic and has the arithmetic mean as its derivative.
For commuting links its equation is linear in the logarithms.
These are exactly the properties proved in `b98p5.md:394–436`,
for Sussman and Alpoge's SA 7065–7073 prescription.

## 3. The row premises, with their measures

Write \(s=\ell_j=L^j\eta\), \(n=L^j\).
Let \(\widehat q_c\) be the raw straightened logarithm and
\(q_c=s^{-1}\widehat q_c\). Put \(Q_c=Dq_c(0)\).
Let \(Q'_y\) be the derivative of the actual averaged gauge transformation.
All entry sums below use counting coordinates and colour operator norms.
Fine pairings have weight \(\eta^4\); row pairings have weight \(s^4\).
The transposes are bilinear on the entire complex domain.

| Premise used | Native mean bound or identity |
|---|---|
| Flat field row | \(Q_c(1)A=n^{-5}\sum_{x\in B^j(c_-)}\sum_{t=0}^{n-1}A_\mu(x+t\eta e_\mu)\). |
| Flat site row | \(Q'_y(1)\lambda=n^{-4}\sum_{x\in B^j(y)}\lambda(x)\). |
| Flat row and column sums | Each row sums to \(1\). Each full fixed-height column sums to \(n^{-4}\). Deleting rows can only reduce these sums. |
| Curved rows and their flat errors | Row norms are at most \(C_L\); column norms at most \(C_Ln^{-4}\). The errors are at most \(C_L\varepsilon\) and \(C_L\varepsilon n^{-4}\). |
| Complete reads | A field row reads its two endpoint blocks, including all internal bonds. A site row reads its one block. |
| Column multiplicity over heights | A fine variable meets at most two adjacent heights; at each height at most \(2d\) field carriers. Site carriers have one block per height. Thus \(4d\) is a common bound. |
| Outward rows | Retain the whole double block and the endpoint node factor. Scales on a carrier differ by at most \(L\). Its layer diameter is at most \(4dL\). |
| Second jet | \(\sup_b\sum_{b'}\|D_bD_{b'}q_c\|\le C_Ls(\eta/s)^4\), with the same bound after interchanging legs. |
| Raw fine density | With the other leg bounded in \(\sup m|A|\), \(D^2\widehat q_c[A,\cdot]\) has density at most \(C_Ls^{-3}\). Counting entries are \(\eta^4\) times this density. |

Here \(\varepsilon\) bounds the supplied local potential in the row's units.
In a PI model it is at most \(C_{N,L}(a_0+a_1)\).
Flat errors and family column sums use one common frame on the union of reads.
They do not subtract separately gauged rows from one global flat operator.
The notation \(C_L\) permits dependence on the fixed group and endpoint spaces.
All statements hold on the common larger complex ball, not just at real centres.
At height zero, both maps are identities and their second derivatives vanish.

The flat field formula follows from cancellation of both node derivatives.
The remaining straight segments compose exactly.
The flat site formula follows by partitioning a block into its subblocks.
These are `out-pi.md:498–609`, with the symmetric cancellation proved in
`b98p5.md:224–254,423–436`; see also SA 11525–11538.
Neither calculation uses a curved equality between prescriptions.

For clarity, the depth argument is already a port, not a new induction.
At intermediate level \(i<j\) put \(t_i=L^{i-j}\).
The one-step raw field sums are \(L(1+C\varepsilon t_i)\) and
\(L^{-3}(1+C\varepsilon t_i)\). The ordered node factors have the
same summable errors. Therefore the existing argument uses

\[
 \sum_{i<j}t_i<\frac1{L-1},\qquad
 \prod_{i<j}(1+C\varepsilon t_i)
       \le \exp\!\left(\frac{C\varepsilon}{L-1}\right).
 \tag{1}
\]

After multiplying by \(\eta/s=n^{-1}\), this gives the field sums above.
Telescoping against the flat factors gives their error bounds.
This is SA 11583–11610 and `b98p5.md:255–319`.
The proof is on a complex potential tube in the supplied unitary frame.
It does not continue an inequality from real fields by an identity theorem.

For the site row, replace each comb transport in `out-pi.md:597–609`
by the prescribed level-\(m\) mean transport at background \(M^m(U)\).
Endpoint covariance is exact by `b98p5.md:394–422`.
The reference factors are bounded by `b98p5.md` (12)–(13).
Its distance from identity at level \(m\) is at most \(C_L\varepsilon t_m\).
The node products obey (1), so the full transported colour coefficient
differs from identity by at most \(C_L\varepsilon\).
The weights are \(n^{-4}\), with one block containing each fine site.
Their row sum is one. Their column error is \(C_L\varepsilon n^{-4}\).
This proves the required site assertion with no additional height factor.

The multiplicities use the existing retained-row geometry.
A row's outer block lies in the preceding region; both blocks avoid the next.
The no-inward convention excludes all other heights.
Within one height, only incident double blocks can contain a fixed bond.
Taking all coordinate orders changes no block in that read.
This is SA 11606–11610 and `b98p5.md:351–370`.
It includes outward rows; it is not an interior-only count.

The second-jet bound is SA 11612–11639 (PX151–PX154).
Its proof uses a column sum on the fixed leg and a row sum on the other.
The remaining sum is geometric in the insertion height.
Multiplying by \(s\) for the raw output, dividing by \(\eta^4\),
and bounding the other leg by \(C_L/s\), gives the displayed density.
The larger-ball third derivative and its extra increment factor are
already proved in `b98p5.md:323–370`.

### Hölder differences and cutoff differences actually used

GW does not differentiate an averaging density.
Its strong comparison says this explicitly at `walks-gw.md:316–327`.
The required Hölder quantities are those of scalar inverse outputs,
fine gradients, differentiated sources and smooth cutoffs.
They use the fixed gap \(\alpha_\beta-\beta=(1-\beta_0)/2>0\).
GW's flat Poisson bounds and their endpoint spaces remain unchanged,
because the flat mixed matrix is the same after the levelwise relabelling.

For a cutoff \(h\) on a tile of size \(M_ts\), the actual row commutator is

\[
 [Q,h](c,b)=Q(c,b)\{h(b_-)-h(y_c)\}.
 \tag{2}
\]

The same formula holds for site rows and physical transposes.
On its complete carrier the brace is at most \(C_L/M_t\).
The row and column sums above therefore give GW's commutator bound.
For a row mass, insert the cutoff at the intermediate row and use (2) twice.
This is precisely `walks-gw.md:399–439`.
Moving the row reference from a corner to its centre changes only that
fixed distance bound.

For \(0<\alpha<1\), the cutoff estimates also give
\([h]_\alpha\le C(M_ts)^{-\alpha}\) and
\([\nabla h]_\alpha\le C(M_ts)^{-1-\alpha}\).
Indeed bound a difference by the smaller of its two suprema
and its derivative bound times the distance.
These are the multipliers needed by GW1; sharp indicators are not differentiated.
The local identity pieces retain the smooth partition and its full reads.

Where a consumer takes a spatial difference of an averaged field itself,
write \(\widehat q(A)\) for its raw map of the complete local potential.
Translation covariance and differentiation give the exact integral identity

\[
 \widehat q(\tau_hA)-\widehat q(A)
 =\int_0^1D\widehat q(A+t(\tau_hA-A))(\tau_hA-A)\,dt.
 \tag{3}
\]

Use it only on a common supplied read. Applying it twice gives one term
with \(D\widehat q\,\Delta_h^2A\) and one with
\(D^2\widehat q[\Delta_hA,\Delta_hA]\).
The raw bounds are \(Cs\) and \(Cs^2\).
This is the existing argument in `b98p5.md:655,677–688`.
It introduces neither a new seam frame nor a derivative of the current.

## 4. Substitution into PI, GW and GW1

First use the relabelling at every height, not just in the two-layer test.
Translate fine coordinates by \(-h_k\); relabel level-\(j\) rows by
\(y'=y+h_j-h_k\). The integer identity is

\[
 \frac{L^k-1}{2}
 =L^j\frac{L^{k-j}-1}{2}+\frac{L^j-1}{2}.
 \tag{4}
\]

It identifies every translated corner block with its centred block.
Translate regions, collars, cutoffs and coefficient reads by the same fine map.
Row endpoints remain in their corresponding blocks.
Thus the retained rows, physical measures and flat mixed systems match.
The flat inverse and energy constants in `out-pi.md:618–669` apply.
For localization, keep the corresponding labelled tile graph and full footprints.
A row reference stays within its own endpoint block.
Every cutoff oscillation and carrier-diameter estimate therefore has the
same fixed \(L\)-dependent bound. No translation is iterated once per level.

Here is the energy comparison required by `out-pi.md:688–735`.
Work in one local model's supplied unitary frame on its full read.
For \(T=Q_m(U)-Q_m(1)\), weighted Cauchy–Schwarz gives

\[
 \begin{split}
 \sum_c s_c^2|(TA)_c|^2
 &\le\sum_c s_c^2
       \left(\sum_b|T(c,b)|\right)
       \sum_b|T(c,b)|\,|A_b|^2\\
 &\le C_L\varepsilon^2
              \sum_b\eta^4m_b^{-2}|A_b|^2 .
 \end{split}
 \tag{5}
\]

The last step uses both sums in §3, the two-height count and \(m_b\le s_c\)
on the carrier (layers \(j-1,j\)).
The site version gives
\(\|s^{-2}(Q'_m(U)-Q'_m(1))\lambda\|_{\rm rows}
\le C_L\varepsilon\|m^{-2}\lambda\|_{\rm fine}\).
Expand each row mass by replacing its two factors separately.
Duality gives the transpose blocks with their physical weights.
The differential and Wilson blocks have not changed.
Their existing estimates retain every protruding plaquette.
This proves the native mixed energy comparison.

The strong comparison also survives.
Indeed a column error \(C\varepsilon(\eta/s)^4\), after transposition,
cancels the fine pairing volume \(\eta^4\).
For example \(K=sQ\), into counting rows, gives
\[
 |(K_m(U)^T-K_m(1)^T)\nu|
       \le C_L\varepsilon m^{-3}|\nu|_{\rm near}.
 \tag{6}
\]
Together with (5), this covers every averaging block of GW's \(V\to Z\)
comparison. The other blocks are the existing differential stencils.
This is the block-by-block proof in `walks-gw.md:295–397`.
Its Hölder source bounds and reversed words use §3's unchanged endpoint spaces.
Equations (2) and (6) also supply every cutoff transition.
Hence the local-model inverse, parametrix and bare word proofs run with
the native rows. We reuse those proofs; we do not infer pointwise bounds
from an energy-dual estimate.

For GW1, retain the physical current branch.
Let \(w=H^{J,T}J\), with \(H^J\) the native raw-datum lift constructed by GW.
The reversed words give \(s_c^4|w(c)|\le Cj_*\).
For each current-leaf word use its own majorant \(h_\gamma(c,u)\).
Pair the raw second-jet density with that word and the row volume:

\[
 s_c^4|w_{c,\gamma,u}|\,C s_c^{-3}\|A\|_{V_1}
       \le C h_\gamma(c,u)j_*\,s_c^{-3}\|A\|_{V_1}.
 \tag{7}
\]

This is GW1 §3.2, lines 284–337, with the native coefficient from §3.
Summing uses the same \(4d\) carrier count.
Interchanging the two Hessian legs gives the physical column bound.
The current side branch remains attached and is not interchanged with a fine leg.
The Ward-current vertex uses only the native scalar inverse, slice map
and the same finite commutator formula; see §5.
GW's existing differentiated-source allocation applies to it.
No derivative of \(J\) is introduced.

Each insertion therefore belongs to GW1's normalized cell algebra,
including its reversed readouts and spare tree exponential.
Joining words uses the same inequality
\(t_{uv}\le t_u+t_v+17c_\iota\).
The complete mean carrier is already the double-block carrier used there.
Thus no extra junction occurs for each contour or each height.
The existing geometric inverse sums for \(G_1^J,q_{1,J},H_1^J\) apply.
This is `gw1.md:223–283,427–528,529–825`, now with verified native inputs.
It preserves the stated exclusion of a Laplacian estimate for \(G_1^J\).

Choose constants in the existing order.
Fix the common flat bounds, Hölder gap, row constants and tile size first.
Then choose the common background ceilings so that
\[
 B_FC_E\varepsilon\le\tfrac18,\qquad
 B_ZC_Z\varepsilon\le\tfrac18,\qquad
 C_{\rm cut}\varepsilon\le(16M_t)^{-1},
 \tag{8}
\]
and every row tube lies inside the larger ball of `b98p5.md` (11).
All constants in (8) are finite by §§3–4.
Next decrease \(j_*\) so each existing current-series ratio is at most \(1/4\).
Finally choose the switch parameters and separation floors as in GW1 §8.
These are fixed common choices for the entire admitted class.
None depends on depth or on the particular frame.

Expand the native words at switches one, with all node and current reads.
Assign the existing union tags to their complete footprints.
The same absolute majorants give local holomorphy, common-footprint
compatibility and separation at zero switches.
This reuses `gw1.md:826–960`. It does not assert inverse identities away
from switches one, or equality with a separately assigned switched family.

## 5. The completed physical form, without a change of action

Suppress the subscript \(m\) in this section: every object is native.
Use exactly PI's physical pairings and its scalar Dirichlet space.
The native mixed operators define

\[
 \begin{split}
 G'&=(D^TD+Q'^Ts^{-2}Q')^{-1},\\
 R&=I-G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G',\\
 \Lambda&=G'RD^T,\qquad \Pi=I-D\Lambda,\\
 \Delta_a&=\Delta_U^W+DRD^T+Q^TaQ,\qquad a=s^{-2}.
 \end{split}
 \tag{9}
\]

These are `out-pi.md:175–200` and SA 10139–10161.
Their inverses are supplied by §4's native mixed systems.
Redundant gauge directions are removed by the same scalar construction.
No comparison with a comb site Gram matrix is needed.

Differentiated gauge covariance of the straightened recursion gives its
field/site intertwining. On a mixed tower this implies
\(QD\lambda=0\) whenever all the prescribed site rows \(Q'\lambda\) vanish.
At an outward endpoint, iterate the same gauge average over its lower
blocks; zero lower site values remain zero.
This uses the common contour prescription in both maps.
It follows by differentiating SA 7092–7116 and 11540–11548,
not by deleting the outward endpoint factor.

The finite identities \(Q'G'R=0\), \(R^T=R\), \(R^2=R\) now give
\[
 Q\Pi=Q,\qquad RD^T\Pi=0,\qquad \Pi^2=\Pi .
 \tag{10}
\]
For the second identity use
\(D^TD=G'^{-1}-Q'^Ts^{-2}Q'\).
These are bilinear identities, also on the admitted complex ball.
The relative gauge block in (9) is \(DRD^T\).
It is not an absolute contour gauge evaluated at a different reference.

Specify the independent-current extension explicitly.
Let \(\lambda_A=\Lambda A\) and
\(\lambda_A^+(b)=\operatorname{Ad}(U_b)\lambda_A(b_+)\).
Define \(\Theta'_J\) by

\[
 \begin{split}
 \langle A,\Theta'_JC\rangle_{\!f}
 =\frac12\big\langle
 &i[\lambda_A,C]+i[\lambda_C,A]
 -i[A,\lambda_C^+]-i[C,\lambda_A^+]\\
 &-i[\lambda_A,D\lambda_C]-i[\lambda_C,D\lambda_A],
 J\big\rangle_{\!f}.
 \end{split}
 \tag{11}
\]

This is Sussman and Alpoge's SA 10163–10198, from Balaban's Ward correction.
It is the correction used by GW; it contains no derivative of \(J\).
Construct \(G_\pi^J=(\Delta_a-\Theta'_J)^{-1}\),
\(q_J=(QG_\pi^JQ^T)^{-1}\), and
\(H^J=G_\pi^JQ^Tq_Js^{-1}\), in that order.
Since \(QH^Js=I\), the raw multiplier is \(w=H^{J,T}J\).
Define
\[
 \langle A,\Theta_J C\rangle_f
       =\langle w,D^2\widehat q(0)[A,C]\rangle_{\rm rows}.
 \tag{12}
\]
Thus (12) is twice the raw quadratic Taylor coefficient in GW1 (2).
No row-length factor has been suppressed.
The native completed operator actually inverted by GW1 is
\[
 E_{1,J}=\Delta_U^W+DRD^T+Q^TaQ-\Theta'_J-\Pi^T\Theta_J\Pi .
 \tag{13}
\]

Here is the physical match on this boundary convention.
Set \(S_{\rm var}\) equal to the whole Wilson action with exterior links fixed.
A gauge transformation equal to identity outside \(\Omega_0\) changes
only links touching \(\Omega_0\). These are exactly PI's field variables.
Every plaquette trace, including a protruding one, remains invariant.
Thus the Ward identity in `b99-w.md:185–218` applies to \(S_{\rm var}\)
with its own current and compressed whole-action Hessian.
This checks the hypothesis of that existing algebraic identity.
It does not identify an inner-action Hessian with a whole-action Hessian.

At \(J=j_U=DS_{\rm var}(0)\), that identity says
\(\Delta_U^W-\Theta'_{j_U}=\Pi^T\Delta_U^W\Pi\).
At an admitted constrained critical point, stationarity gives
\(j_U=Q^T\omega\), as in SA 11143–11155.
Because \(QH^Js=I\), one has \(\omega=sw\).
Since \(\widehat q=sq\), (12) is precisely
\(\langle\omega,D^2q\rangle\).
Consequently (13) becomes the actual relative completion
\[
 E_{1,j_U}
 =\Pi^T\!\left(\Delta_U^W-\langle\omega,D^2q\rangle\right)\Pi
                   +DRD^T+Q^TaQ .
 \tag{14}
\]
This is SA 11152–11165 (PX94–PX96), with the whole-action match just checked.
For independent \(J\), (11)–(13) specify the operator; physical stationarity
is not assumed. No positivity at arbitrary independent current follows.

The outward datum retains its native endpoint factor.
For per-length coarse coordinates \(B\), retain its literal map
\[
 e^{is_cb(B)(c)}
   =e^{is_cB(c)}\operatorname{Ad}_{V_0(c)}
                  v_z((sB)_{\rm int}) .
 \tag{15}
\]
With \(q_{1,J}=(QE_{1,J}^{-1}Q^T)^{-1}\), the physical coarse Hessian is
\[
 D^2\mathcal A_{\rm eff}
   =Db^T(q_{1,j_U}-a)Db+\langle\omega,D^2b\rangle .
 \tag{16}
\]
Equations (15)–(16) are SA 11167–11202 (PX97–PX100).
They retain both endpoint derivatives.
Only the stated active-datum condition \(Db\,\iota=\iota\),
\(D^2b[\iota\cdot,\iota\cdot]=0\) removes the last term.
This note imposes no such condition on arbitrary outward data.
The next nonlinear fibre and its actual gauge functional have their own
Hessians; (14) is not a replacement for them.
Y 23838–23915 makes exactly this distinction and supplies the existing
multiplier block-inverse identities.

## 6. Closure and handoff

**Result: stopping alternative (a).** SC-NATIVE holds as the stated
implication on the common admitted PI/GW class.
The proof above verifies the contour-dependent premises of the existing
proofs and identifies the native completed form.
It uses their prior flat, inverse and word proofs with credit.
It is not an independent check of those proofs or of this note.

It supplies SC-HESS's remaining inverse consumer directly.
The symmetric mean has the required bare mixed inverses, current-corrected
inverse and lift bounds, physical columns, and complete-carrier word bounds.
There is no special comb identity left in these uses.
SC-GAUGE is therefore unnecessary for this restricted consumer.
No nonlinear fibre congruence or general all-history A4 assertion follows.

The next application is PI-ADMIT, already owned by `pi-admit`.
Its registry entry leaves C0-SUP: supply the common boundary frames and
exterior twist bounds on actual reached entries.
An actual caller must also use the whole-action convention of this proof.
This leaf stops at that existing owner. It does not create a duplicate lane.

| Item | Status in this note | What it supplies |
|---|---|---|
| Flat two-layer boundary test | Pass, by the existing coordinate identity | Exact normalization and retained outward reads. |
| Noncommuting seam test | Curved equality refuted by the written coefficient (K) | Rejects an equality shortcut; no native estimate is refuted. |
| Field and site rows | Existing estimates ported; native site substitution verified | Row sums, column sums, flat errors and two-height multiplicity. |
| Hölder and carrier uses | Verified for the actual PI/GW/GW1 uses | Smooth cutoff differences, fixed source gap and complete carriers. |
| PI native bare inverse | Prior implication reused | Same flat normalization and whole-action boundary convention. |
| GW/GW1 native application | Proved implication from those admitted inputs | Current words, reversed readouts, coarse inverse and lift. |
| Completed physical form | Identified in (11)–(16) | Independent-current extension, relative gauge and outward datum derivatives. |
| SC-NATIVE | Complete at its stated restricted scope; not independently checked | Supplies the admitted inverse consumer of SC-HESS/A4.1. |
| Actual-history admission | Open, existing owner | PI-ADMIT/C0-SUP; no scientific status changed. |

**First open input:** PI-ADMIT/C0-SUP on actual reached entries, with
the caller's literal action, rows, complete reads and translated region geometry
matched to this class.
