## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
`prior/repo-search-2026-11-08.md`, section 1, records the relevant results.
I fetched PR #10141 at `c73ad7b177d94f89ff37b77386936e3d52b48b05` and checked these passages:

| Hit | Relation to this leaf |
|---|---|
| `research/ym4d/library/layer-thm-part.md`, 698–703 and 1385–1408 | Already states the missing boundary gauge and continuation reads. This is the same supply problem, not a new diagnosis. |
| `research/ym4d/library/out-pi.md`, 324–329 | Proves interior S1-loc under thickness. Boundary gauges remain additional. It does not identify the cut. |

These snapshot passages are prior work by the repository's Claude and Codex contributors.
They are copies of this route's work, not independent confirmations.
The lead's soft-route hit concerns a different operator and supplies no BZ dictionary.
`prior/leaf-bz.md` is absent at the requested pin.
The registry assigns PI-ADMIT to `pi-admit`; row 538 authorizes this supplier leaf.
No separate BZ-CUT owner was found.

# The literal BZ cut and its boundary read

Codex. Research base `aa33ce362bd8d213bfd6ab6ee9386e5d42caf544`.
FINISH row 538. Research text, not an audit. This note grants no scientific status.
Only this file is changed. All mathematical tests below are written arguments.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the localization, graded partition and gauge methods.
**I** denotes their complete account I at `31a47c543775`.
**SA** denotes their outline at that commit.
**Y** denotes `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
All three requested scratch copies existed; none was fetched again.

## 1. Kill test, before the proof attempt

Use the actual PI whole-action convention from `c0-sup.md`, section 3.
At a flat face write the proposed cut as \(Z=\{x_1\le0\}\), locally.
All opposite faces and torus identifications are far away.
Consider the square

\[
 p=[0,\eta e_1,\eta e_1+\eta e_2,\eta e_2],\qquad
 b_+=[\eta e_1,\eta e_1+\eta e_2].
\]

Its edge \([0,\eta e_2]\) is a PI field bond.
Thus its opposite edge \(b_+\) belongs to the coefficient read.
This is the existing witness of `c0-sup.md`, section 5; no Hessian calculation is repeated.

**Positive parent stratum.** Apply the *candidate* graded splice of `bz-geom.md`, section 3.
Its first two grades have the following normal section:

```text
interior        D2        D1 \ D2        D0 \ D1       outside Z
grade           >=2          1               0
                                                    | x1 = 0
                                                    |---- eta ---- b+
```

For maximum grade one, \(D_2=\varnothing\).
The retained core lies beyond its prescribed inset.
By the existing Lemma 3.1, positive rows miss a crossing patch when its stated gap holds.
If the ambient domain contains this one-spacing read, the outward edge is also admitted geometrically.
**Outcome:** this case does not kill the candidate. The positive parent grade is not a positive localized rim.

**Raw parent boundary.** Test the unbuffered candidate \(X_{\mathfrak a}=Z\).
Put both first positive grades away from the face, or take them empty.
The same section is bare at the face, but \(b_+\not\subset X_{\mathfrak a}\).
**Outcome:** this candidate fails \(E\subset X_{\mathfrak a}\), even with a bare rim and all inner gaps.
This is the geometric inference already rejected in `c0-sup.md`, section 6.3.
It is not yet a counterexample at an item-10 entry: that requires its literal cut.

The test leaves one discriminator: identify the actual cut and its ambient buffer.
It neither refutes BZ-TRACE nor licenses replacing the prescribed cut.

## 2. The port and the exact remaining lemma

The outline index, its neighbouring rows, and its obligations locate the consumer.
SA 10262 sketches layered gauge supply on its stated trace.
SA 10287 expressly includes protruding plaquettes for the compressed Hessian.
SA 10505 places crossing models in a bare collar.
None of those passages identifies the item-10 cut.

Keep the proved inputs in bz-geom, section 3, and c0-sup, Propositions 3.1 and 4.1.
Claude's c0-sup check confirms the latter implications.
Its finding 6 permits one gauge for each real reference.
Its suggested non-bare reading of CMP 119 was corrected by bz-geom; it is not used here.

The source dictionary has the following limits.

| Source | What can be ported |
|---|---|
| Bałaban, CMP 119, pp. 256–257, (2.13)–(2.15); ym4d-papers/cmp119.txt, 683–719 | The minimal graded tower and the localization rule with its provisos. The OCR loses the displayed splice; I 92517–92533 supplies that display. |
| I 94755–94812 | The proved proviso check for the named sets \(\mathfrak B^0,\mathfrak B^C\). Its cut is \(C\); it uses \(d_k(\Lambda_C^\sim,C^c)\ge9\check R_k\). |
| I 131568, 131725–131746 | Item 10 is an input. It names \(\mathfrak B_Z\) by a reference to CMP 122b (2.14). |
| I 137565–137583 | This set is “outside the geometry” of the stage spaces. The localized layer assertion is used with its proof incomplete. |
| Y 35857–35908, 37070–37119 | A constructed erosion or intersection tower is separated. The response conclusion retains its protected, settled, complete-stencil conditions. |

The CMP 122a/b downloads returned publisher access pages, not paper text.
No paywall was passed. The supplied CMP 119 text was read in the bounded range above.
The missing paper is not used as a mathematical stopping reason.
The three routes below test possible deductions from the available definitions and statements.

**Remaining lemma: BZ-CUT.** For every literal item-10 call, including later images, identify
\[
 (Z,C,\mathfrak B_{\rm par}),\qquad
 \mathfrak B_Z=
 (\mathfrak B_{\rm par}\restriction C)
 \cup\bigl(\mathbf B_j(Z)\restriction(Z\setminus C)\bigr).
\]
The formula must describe the prescribed blocks, with the required interface conventions.
Their tower must obey PI's aligned-block and gap conditions (out-pi, 60–77).
It must also satisfy
\[
 d_\infty(\Omega_1(\mathfrak B_Z),Z^c)>2L(r_N+2)\eta,
 \qquad E\subset X_{\mathfrak a}.
 \tag{BC}
\]
Here \(E\) includes the outward plaquette and the reference-norm reads.
This is the tree's existing leaf, not a new registry task.

## 3. Three routes to BZ-CUT

### A. Recover the cut from the literal birth operation

Follow the occurrence of \(H_Z^{(j)}\), rather than choosing a convenient localization.
I 80920–80929 and 81446–81523 transport the change of variables to the large-field stage.
They cite Bałaban for dependence on the configuration restricted to \(Z\).
I 131946–131977 names the class region \(Z\) and makes \(X_{\mathfrak a}\) one of its components.
For exit (e4), I 137320–137340 identifies the changed bonds:
\[
 S^P=(\Omega_{j+1}^c\setminus Z''_{j+1})^{(j)*}\cap X_{\mathfrak a}.
\]
These are operation reads, not the outer boundary of a PI tower.
I 137392–137410 retains \(H_Z^{(j)}\) and its original parameter domain.
It does not give a retained core or a boundary distance for its determining set.

Try to recover that boundary from locality of \(H_Z^{(j)}\).
This implication fails even for a known holomorphic function.
If \(F(P)=f(P|_S)\) and \(S\subset D_1\subset D_2\), then
\[
 F(P)=f((P|_{D_1})|_S)=f((P|_{D_2})|_S).
\]
Thus locality on \(D_2\) does not say whether the prescribed construction uses \(D_1\) or \(D_2\).
Bounds on \(F\) do not distinguish them either.
No minimal-support assertion is supplied at this birth.

The literal birth formulas locate the class, component and changed bonds.
They still do not give the localized partition, its retained core, or an exterior buffer inside \(X_{\mathfrak a}\).
In particular, \(X_{\mathfrak a}\subset Z\) is not the required \(E\subset X_{\mathfrak a}\).
Identifying the PI outer region with a buffered inset would add an equality.
The CMP 119 template cannot supply that equality.
This route fails at the first identity in BZ-CUT.
It makes no claim that the cited Bałaban construction lacks an identity.

### B. Use the account's general determining-set rule

I 42985–43006 gives a more explicit candidate:
\[
 b_{p,D}(x)=\min\{p,c(x),t_D(x)\},\qquad
 d(x,\partial D)\ge2M_1\ell_m\Longrightarrow t_D(x)\ge m.
 \tag{G}
\]
I 43055–43064 calls these prescribed properties a hypothesis of that chapter.
Its abstraction includes several different constructions.
It does not identify this partition with item 10.

Even granting that identification would not derive the first gap from (G).
Here is an exact test of the displayed geometric properties.
Take depth \(k=1\), a proper aligned box \(D\), and
\[
 p=1,\qquad c(x)=1,\qquad t_D(x)=1\quad(x\in D).
\]
Partition \(D\) into level-one blocks. Choose its side to be a multiple of \(M_b\ell_1\).
Then (G) holds for both possible indices \(m=0,1\).
Adjacent blocks have equal levels. Constant-level regions are unions of blocks.
The boundary tower depends only on the domain, as required for this instance.
But
\[
 \Omega_0=\Omega_1=D,\qquad \Omega_2=\varnothing.
\]
There is no bare rim. The first gap is zero for geometric regions, or at most \(\eta\) for site sets.
A level-one outward row at a face belongs to a crossing patch.
Hence the required gap in (BC) fails.

This refutes deduction of BZ-CUT from these displayed properties alone.
It does not refute the full determining-set hypothesis or the literal item-10 construction.
The missing information is an upper bound on grades near the *specified* cut.
The existing graded-splice lemma supplies it only after the partition is identified.

### C. Identify the cut by uniqueness of the regular background

Try to recover the geometry by matching its constrained minimizer to the ambient pair.
This would avoid reading the partition directly.
The flat configuration rules out that inference.

Fix a proper aligned ambient box \(A=X_{\mathfrak a}\).
Compare a bare partition on \(D_{\rm touch}=A\) with one on a strictly inset box \(D_{\rm in}\).
Choose the inset by whole blocks, with \(d_\infty(D_{\rm in},A^c)>2\eta\).
Keep the torus large enough to avoid wrapping.
Prescribe identity data on both partitions.

The average is normalized: \(M_{\mathfrak B}(1)=1\), I 43018–43027.
Thus \(U=1\) satisfies both constraints.
Each Wilson plaquette term is nonnegative for \(SU(2)\):
its normalized trace is \(\cos\theta\le1\).
The identity field has action zero and is a minimizer on both domains.
Uniqueness of a regular minimizing orbit, if invoked, selects this same flat orbit on each.
It cannot decide which domain was prescribed.

The example defines a constant family on any prescribed parameter polydisc.
Use the identity reference and zero twist there.
Every gauge can be the identity. All the gauge and twist smallness bounds hold.
Nevertheless the boundary read for \(D_{\rm touch}\) leaves \(A\), by section 1.
The corresponding read for \(D_{\rm in}\) stays in \(A\).
This uses the old outward-edge witness; the failed inference here is reconstruction of a cut from its minimizer.
Neither configuration is asserted to be an arrested history.

The newer theorem does not distinguish these choices.
Y 37070–37119 constructs a chosen intersection tower and proves its separation.
Y 36707–36753 and 36859–36877 restrict its field conclusions to inner, settled outputs.
Those are valuable ported results. They do not identify item 10's cut.
Using uniqueness would also require the same constrained problem, which these two cuts do not share.
This route therefore fails before any estimate of the missing exterior trace.

## 4. Transfer and supplier outcome

BZ-CUT has not closed. BZ-TRANSFER therefore has no identified birth trace on which to start.
The following existing steps remain available; they are not proved again here.

I 119603–119650 keeps the unitary reference and uses the pair's own ambient continuation.
I 49120–49160 supplies a single hull gauge only on its stated trace.
I 49502–49518 retains the restriction \(Q\cap\Omega_0\).
I 134745–134780 gives chronological raw-stratum heredity, with no level lowered.
As bz-geom explains, that does not identify a new grade-lowering localization with a chronological move.

Once the birth trace is identified, bz-geom, section 5.2, gives the exact conversion:
\[
 \eta|A|<\max_{n\ {\rm met}}L^{-n}\mathfrak a_n,\qquad
 \eta|a|<\max_{n\ {\rm met}}L^{-n}t_n.
\]
The two maxima must meet \(\tfrac14L^2a_0^*\) and \(\tfrac14a_1^*\), respectively.
The actual supplying pair must agree on every required bond throughout the original domain.
No radius was reduced here. No nonzero-twist test at that radius has been passed.

**Result: stop (c), at BZ-CUT.**
The three failed routes are birth-locality reconstruction, the general grade rule, and inverse identification from the minimizer.
Their counterexamples refute only those proposed deductions.
They do not refute the literal leaf or the localized layer assertion.
The unavailable paper is not one of these counterexamples.

This supplies no new unconditional input to BZ-TRACE or to c0-sup Proposition 4.1.
It rules out replacing the missing construction identity by the three weaker pieces of information above.
After BZ-CUT closes, the next leaf is only the unsupplied trace, pair and original-radius clauses of BZ-TRANSFER.
Their conclusion would feed BZ-TRACE, then the existing conditional boundary proof for PI.
The new arguments in section 3 have not been checked by another model.

## 5. Status table

| Statement | Result here |
|---|---|
| Earlier boundary-gauge diagnosis and interior PI admission | Prior repository work, reused with its scope. |
| Graded splice has a bare rim under the stated margins | Existing bz-geom proof; not repeated. |
| Positive-parent kill case | Candidate survives; no literal identification follows. |
| Raw, unbuffered kill case | Candidate fails at the outward bond; no reached-entry claim. |
| Recover the cut from birth locality | Route A fails: locality does not specify the construction's domain. |
| Derive the first gap from the displayed general grade properties | Route B refuted by the depth-one example. |
| Recover the cut from its regular minimizing field | Route C fails even at the identity field. |
| Literal BZ-CUT | Open after three distinct routes; stop (c). |
| Missing BZ-TRANSFER clauses | Not supplied; depend first on the actual birth trace. |
| BZ-TRACE and PI boundary admission | Remain conditional. No scientific status is granted. |

**First open input: BZ-CUT.**
Give the literal \((Z,C,\mathfrak B_{\rm par})\) for each item-10 call.
Prove its partition identity, PI gaps, and \(E\subset X_{\mathfrak a}\).
The certificate must include the outermost touching plaquette before the localized layer theorem is used.
