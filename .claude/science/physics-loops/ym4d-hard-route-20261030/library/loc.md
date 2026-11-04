# LOC: locality through later steps and R stages
Provenance: Codex (GPT-6 family; runtime effort not exposed; requested effort: max); checkout `7441090e1`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; grants no status.

## 1. Target and source boundary

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Their pinned outline supplies the step and R-stage definitions, especially SA L17541–17558 and L17951–17980.
All arguments below are by hand.

For a formed slot on a domain \(Y\), (LOC) requires equality under agreement of label and data on \(Y\).
This includes the rule that selects the slot and its domain, not only evaluation on a fixed domain.
The same requirement applies to each correction \(V_{\mathfrak X}(Y)\), at every depth.

`gates/s210-3-check.md` rejects Theorem E, Corollary K, and Lemma N's claimed local family.
I therefore do not use those claims as proved inputs.
The finite telescoping identity and its conditional derivative estimate survive that check.

## 2. The available locality statement

The checked inputs give locality **in the pair** \(P=(\mathbf U,\mathbf J)\).
They do not identify two physical pairs from agreement of stored data on a smaller domain.

For the intrinsic potential, Theorem U' gives
\[
 (P,y)|_Y=(\widetilde P,\widetilde y)|_Y
 \quad\Longrightarrow\quad
 V^{G,A}(Y;P,y)=V^{G,A}(Y;\widetilde P,\widetilde y).
 \tag{1}
\]
Its inputs remain [R9], [D+], [S-loc'], (F), [RT], [ID], [QC] and [Core].
Codex checked this implication in `b4-step.md`, Section 9.
Its scope is the single-scale, node-free interior; `um1-fix.md` does not extend it to layered regions.

Here is the support argument behind (1).
Set the Definition D parameters to zero outside \(Y\).
Every surviving walk has its full read hull in \(Y\).
Corollary R' includes the untagged local stencils and their collars.
Thus the bracket integrands agree at equal restrictions to \(Y\).
Differentiating that identity in its retained parameters and integrating over their common cube preserves equality.
Summing the plaquette and gauge anchors proves (1).

The stored carrier series has the same property before substitution of the physical background.
Use its adopted definition in `carrier-adopt.md`, Section 4, and the checked full-hull premise [RT].
In a grouped inverse entry, a path with fewer than \(n\) steps of length at most \(r\) stays within \(nr\).
Each precision factor adds at most its prescribed read collar \(R_h\).
Hence the grouped entry reads only its carrier of radius \(R_*=nr+R_h\), including membership in the integrated set.
Equal data on that carrier give identical paths, coefficients and sums.
For a chain, its carrier contains every factor carrier and contracted coordinate.
Products, symmetrisation and convergent sums over these common, supported chains preserve equality.
This argument adds no collar at each later depth; it uses the carriers already assigned to those factors.

`wf7-bf.md`, Section 4, proves the corresponding box composition with the ambient sequence fixed.
Rule W supplies containment of its tower, under the premises of `cond-c.md`, Theorem C2.
It does not identify the physical background from the data in that box.
Definition R fixes the representative through the comb transport in `inn-213.md`, Section 7a.
The checked estimates in `inn-fix.md` concern (Inn); they explicitly leave the stored forms and (Act) outside their scope.

For a carried coefficient \(a_R\), the next required operation is already
\[
 a_R(P^\sharp(h,v))-a_R(P^\flat(h,v)),                 \tag{2}
\]
as in SA L17558–17564.
Locality of \(a_R\) in its pair argument does not localise the maps \((h,v)\mapsto P^\sharp,P^\flat\).
Equation (2) needs an exact common family of local pieces before any induction through later moves can start.

## 3. First missing input: the local family at formation

The proposed input is `s210-3.md`, Lemma N's family
\[
 t_n(h)=F(H^{(n+1)}_h)-F(H^{(n)}_h),\qquad
 \operatorname{domain}(t_n)=W_{n+1}(h).
 \tag{3}
\]
Its first failed inference is that (N1) makes this a common family determined inside \(W_{n+1}\).
(N1) determines \(W_{n+1}\) from the label in \(W_{n+2}\), which is larger.
The following hand example tests the selection and increment conditions alone.
Its assigned evaluations are not asserted to be Yang–Mills backgrounds.

Fix nested regions \(W_0\subset A\subset B\subset C\subset T\).
Put one label bit \(e\in\{0,1\}\) at a site \(q\in C\setminus B\).
The two labels and their data agree on \(B\).
Choose
\[
 W_1(0)=A,\quad W_1(1)=B,\quad W_2=C,\quad W_3=T.
\]
This satisfies (N1): only the choice of \(W_1\) reads a bit, and that bit lies in \(W_2\).
At one fixed bond in \(W_0\), assign local evaluations
\[
 V_{W_0}=V_A=V_C=V_T=\mathbf1,\qquad V_B=e^{ia\sigma_3}.
\]
Each fixed-domain evaluation is constant, so it reads no exterior data.
Take \(0<a<\min\{C_N\varepsilon e^{-\delta_N},\delta/12,1/2\}\), with (N2)'s smallness condition retained.
The successive logarithmic increments are \(0,0,0\) when \(e=0\), and \(a\sigma_3,-a\sigma_3,0\) when \(e=1\).
Their norms satisfy (N2) at each index.
With \(V^{\rm loc}=\mathbf1\), use the convention \(V=e^{iH}\), and take \(F(H)=\tfrac12\operatorname{tr}(H\sigma_3)\).
This is a linear \(C^1\) function with \(F(a\sigma_3)=a\).

Index (3) by its declared domain, assigning zero to an absent slot.
The first slot on \(B\) is then
\[
 t_0(B;e)=a e.                                          \tag{4}
\]
Thus equal labels and data on \(B\) give different coefficients there.
The next term equals \(-ae\), so the total still telescopes to zero exactly.
An exact total and a decay bound therefore cannot justify Lemma N's locality step.
This does not refute the existence of a suitable Yang–Mills localisation.

The missing input is an admitted strip localisation whose **domain selection and coefficients** are fixed by the same local trace.
The comparison bounds and pair locality in Section 2 do not supply that selection rule.
At row 204's checkout, `s210-fix.md` contained only its work-in-progress header.
That reading stopped before applying (3) to later steps or R stages.

### Earlier result (row 204)

**(LOC) is not proved.** The first unusable input is Lemma N's claimed common local family at formation.
Its selection condition permits the exterior read in (4); the cited checked inputs do not supply the stronger condition needed.
Theorem U' and the stored carrier series retain their conditional locality in the pair.
They do not supply the missing family for (2), or the healed correction identity of SA L17964–17980.
No induction uniform in depth, rank 7 closure, or (Act) conclusion follows.
The argument above is by Codex and has not been checked by the other model.

## 4. Row 211: check of Claude's `s210-fix.md`

Provenance: Codex (GPT-6; runtime effort not exposed; requested effort max), checkout `04c4e8873`; research, not an audit; no status granted.
Checked line by line against the pinned SA outline and the named repository inputs.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
All new arguments below are by hand.

### 4.1 Lemma G

**ADVANCE, conditional on the stated block map and its small analytic contour mean. First failing step none.**
The rectangular lift is essential: it excludes additional periodic bonds and pivots.
There are exactly \(L\) axial sites. Their contributions vanish.
Thus the non-axial weights sum to \(1-a\), where \(a=L^{-3}\).
Comb slides use at most \(CL\) plaquettes; telescoping their products proves the gauge bound used in Step 1.
Path lengths then give \(a(X)\le\sigma\) and \(a(u)\le3\sigma\).

Here is the global part of the uniqueness check.
For \(T=e^{iZ}\), \(\|Z\|\le\pi/2\), the logarithm estimate gives

\[
 \|m+(1-a)Z\|\le2\sigma,
 \qquad \mathcal M(V_g)=u\ \Longrightarrow\ a\|Z\|\le5\sigma.
 \tag{5}
\]

For \(\|Z\|>\pi/2\), a pivot plaquette excludes the analytic rule.
The rule \(\mathcal M=T\) cannot give the small target.
Under the remaining rule, a solution has \(\|Z\|<(1-a)\pi+3\sigma\).
Along the logarithm comparison paths its derivative is at most \(\pi/a\).
Hence \(a\|Z\|\le(\pi/a+3)\sigma\le4\sigma/a\), which forces
\(\sigma>\pi a^2/8\), contrary to \(\sigma\le a^2/8\).

On \(a(T)\le8\sigma/a\), the map \(T\mapsto e^{-im(T)}u\) stays inside that ball.
Its Lipschitz constant is at most \(1-3a/4\).
Iteration is Cauchy, with error bounded by a geometric series, and gives the unique solution.
For two data sets, subtract their fixed-point equations and divide by \(3a/4\).
The contour-mean equation has derivative \(I+E\), \(\|E\|\le1/2\); its inverse has norm at most \(2\).
Telescoping each contour product therefore gives \(\|m_V-m_R\|\le CL\eta\).
This proves \(d(g,R(b_0))\le CL^4\eta\), and continuity follows from the same estimate.
These arguments check Steps 0–5; no machine calculation enters.

### 4.2 Coordinates, supports and records

**Checked line by line by Codex; first failing step none in these conditional implications.**

| Statement | Verdict and scope |
|---|---|
| Definitions 3.1′–3.2′, including (L0) and (G-e) | **ADVANCE**, with (EX′), (M), (S) and the supplied rules. |
| Lemma C(a)–(d) | **ADVANCE** under those inputs and the stated test geometry. |
| Theorem E′; Corollary K′ | **ADVANCE** for supports and reference measures, with (SUP), (L2.2), (LAD), (CAR) still supplied. |
| Proposition P(c) | **ADVANCE** for the frame-weighted record count. |
| Proposition P, support read closure | **ADVANCE** under Theorem E′; P(a)–\(b\) remain unchanged. |

The boundary gap in (G-e) is \(1-2L^{-2}>1/2\).
Thus a boundary-crossing coarse average reads raw or fully shifted bonds, not an unresolved interior pivot.
For an interior double block, every nonpivot is fixed before its unique pivot is solved.
The value \(1\) off its chart completes a Borel map; it need not satisfy the constraint there.

For Lemma C, the surviving tests bound an (F2) coordinate by \(\delta_k\).
They bound an (F3) radius by \(23\delta_k/10\), using the strip identity and (M).
Consequently its distance from the true background is less than

\[
 (23/10+1/6)\delta_k=37\delta_k/15<5\delta_k/2=\eta_*.
 \tag{6}
\]

The same inequalities hold for failed outcomes and the fill: only the stated surviving pass tests enter.
Inverting the nonpivot exponential or strip map recovers every coordinate.
Lemma G then recovers each pivot; its contraction also makes the pivot differential invertible.
Distinct equations have distinct pivots. Thus the admitted change of variables has no extra support restriction.

Theorem E′ now compares the same coordinate tests, including their complements and undefined-object branches.
The common chart reads only coordinates already read by those tests.
(LAD) supplies equality of the full products off the good exterior sets; it remains an assumption.
Fixed Haar or Lebesgue reference measures and the retained component's own normalisers give K′.
No Jacobian or action density is covered by this conclusion.

P(c)'s extra symbol distinguishes the extension, \(B\), last-shell and normaliser failures.
Together with the stage failures and two terminal fates, this gives \(\mathsf N_j+6\) possibilities.
For \(x=M\check R_j\ge2\), \(\mathsf N_j+6\le x+6\le x^4\le e^{x^4}\).
The frame weights sum to one. The tests' existing one-cell reads therefore still give \(J=81\).

### 4.3 Lemma N′ and (N1′)–(N3′)

**ADVANCE as a formation implication from an admitted stopping nest and (N2′)–(N3′).**
The stopping condition fixes \(W_{n+1}\), \(W_n\), and \(W_0\) from the label on \(W_{n+1}^+\).
Their joined problems must use the same prescribed local rules, including the representatives.
Equal local data then give equal backgrounds and equal increments. This repairs the exterior-bit error in (4).

Write \(L_\theta={\rm Lip}(\theta)\) and \(s=\varepsilon_N/(1-e^{-\delta_N})=h_*/2\).
The group triangle inequality gives \(a(V^{(n)}V^{{\rm loc}\,-1})\le s\) directly.
On the cut-off zone, \(\theta\) rises by one over a radial interval shorter than \(\delta_k\).
Thus \(L_\theta\ge1/\delta_k\), and (N3′) implies \(s<\delta_k/4<1\).
The ball is geodesically convex. Lemma G's logarithm bound gives

\[
 \|H^{(n+1)}-H^{(n)}\|\le2\varepsilon_Ne^{-\delta_Nn},\quad
 J\ge1-L_\theta h_*>1/2,\quad \|d\log J\|\le2L_\theta.
 \tag{7}
\]

Integrating along the segment between the two logarithms proves the stated bound \(4L_\theta\varepsilon_Ne^{-\delta_Nn}\).
The finite sum telescopes. On the full-shift zone \(J=1\); its contribution is zero without intermediate logarithms.
This also avoids the unjustified \(h_*+\varepsilon_N<1\) inference there, where \(L_\theta=0\).

The exact support proved is \(W_{n+1}^+\), including its selection, not the smaller \(W_{n+1}\).
Use that full support when assigning a term to a domain.
The distance consequence follows by iterating the upper growth bound; it measures distance from \(W_0\), not from \(b\).
**First unproved input: admission of the nest in (N1′).** Neither (N2′) nor (N3′) is established for actual nests.
The full-shift simplification and support assignment above are the only corrections to this conditional check.

## 5. First failed input: the admitted nest (N1′)

**(N1′) is not available on general histories as written.**
The adopted comparison requires
\(W\subset\Omega_0\), \(\Omega'_0=W\), and \(\Omega'_q\subset\Omega_q\)
(`a3-close.md`, Lemma J; `a3-derivative.md`, Lemma 10.1).
But (N1′) requires \(W_N=T\), while histories have \(\Omega_0=\Omega_1^\sim\), possibly strictly smaller than \(T\) (SA L17317).
Thus its terminal localised problem need not belong to the cited comparison theorem.

Here is a hand witness to the hole; no numerical search is needed.
On a sufficiently large torus, set every fine bond to \(1\), except one internal nonpivot bond set to \(-1\).
Choose that bond off the coarse straight axes, with two nonzero transverse coordinates.
Every coarse straight transport is \(1\).
On an affected double block a plaquette is \(-1\), so the block map uses a crude rule.
Every contour product is \(\pm1\): either all relevant loops are \(1\), or the third rule applies.
Both give \(V_1=\mathcal M(V_0)=1\).
The normalized block gauge insertion has a supported representative and preserves these coarse data.
Its internal plaquette remains \(-1\); telescoping its four factors forces some nonpivot deviation to be at least \(1/2\).
If the approximate tests there are reached, their local backgrounds are \(1\), so one fails since \(1/2>2\delta_0\).
Then \(Q_1\ne\varnothing\); if an earlier test already marked it large, the old live region supplies the hole instead.
Either padding leaves a nonempty hole even after enlarging \(\Omega_1\) once.
This proves \(\Omega_0\ne T\) on an allowed failure branch.
This rules out the literal terminal admission on that branch; Lemma N′ remains a conditional implication.

The relevant precedent agrees with this domain restriction.
Sussman–Alpoge's YM3_I, L46926–46940, uses \(Z_t\cap\Lambda_k\cap\Omega_0^\diamond\).
Its L46732–46824 assumes the single-layer collars before proving comparison.
Balaban CMP 119, pp. 252–253, supplies the strip method, not an exhaustion by such collars.
QED3, L7440–7468, localises operators by walks; that does not select a nonabelian background nest.
These are credited methods, not imported proofs of (N1′).

**Smaller statement, proved.** After clipping the initial region to its ambient domain, stopping exhaustions exist as sets.
Start with the component of \((\Lambda_t^c\cap\Lambda_k)\cap\Omega_0\) containing \(b\).
Repeatedly add its adjacent cells which belong to \(\Omega_0\).
For the \(n\)-th set \(E_n\), agreement on \(E_n^+\) fixes the initial component and each of the first \(n\) additions.
Induction therefore proves the stopping property.
Each enlargement adds at most one layer. Finiteness ends the process at the ambient component containing \(b\).

This does not prove collar admission.
A box expanding across a flat seam has a connected outer boundary meeting two layers.
In a collared representation, distinct part boundaries are separated; one connected boundary cannot switch between them.
Its controlling part would therefore need a collar in two layers, contrary to SA Theorem 6(c).
So even this elementary stopping exhaustion can leave the admitted class.
A repaired terminal convention and a rule selecting admissible intermediate collars are still needed.

## 6. What (N2′) needs in the common gauge

The gauge conversion is elementary once its anchors are controlled.
This is the method of Sussman–Alpoge YM3_I, L47086–47125 and L47185–47240, rebuilt here at one level.
For a block field \(B\), let \(a_B(x)=B(y(x),x)\) be its contour transport from the prescribed anchor.
At an endpoint which is already a node, put \(a_B(x)=1\) and \(y(x)=x\).
Set

\[
 D_B(b)=a_B(b_-)B(b)a_B(b_+)^{-1}.
 \quad D_{B^w}(b)=w(y_-)D_B(b)w(y_+)^{-1}.
 \tag{8}
\]

The second identity follows by cancelling the two endpoint gauge factors in each transport.
If two fields differ by at most \(q\) on the double block, each contour product differs by at most \(2Lq\).
The contour-mean inverse bound from Section 4.1 then gives \(d(D_B,D_C)\le C_Lq\).
Now let \(q=\sup_{D_c}d(B^w,C^{w'})\) in two admitted gauges, with \(w'(y_\pm)=1\). Then

\[
 d(D_B,D_C)\le C_Lq+d(w(y_-),1)+d(w(y_+),1).
 \tag{9}
\]

The last two terms cannot be discarded.
Take \(C=1\), with \(w\) constant on each of two adjacent blocks, equal to \(1\) and \(e^{ia\sigma_3}\).
Then \(B=C^w\) is flat and block axial, but a crossing bond is \(e^{-ia\sigma_3}\).
The comparison field can be zero while the representative difference is \(a>0\).
This refutes conversion from gauge equivalence and axiality alone; the two coarse root data here differ.

SA Theorem 6(c) controls \(w\) only at tops away from the collars.
For (N2′), every averaging read and anchor must lie in that controlled interior at every \(n\).
One also needs distance to the changed rows at least \(R+vn\), with \(v>0\), and uniform bounds through the iterated averages.
These would give \(\varepsilon_N=C\varepsilon e^{-\alpha R}\), \(\delta_N=\alpha v\), and then the explicit (N3′) test.
(N1′)'s upper growth bound supplies neither this distance lower bound nor the anchor condition.
Thus (9) proves the conversion step, but does not prove (N2′) for an actual nest.

## 7. Continuation to later steps and \(\mathbf R\)

There is a precise conditional preservation argument.
Assign each formation term its full read support, including the stopping rule and collar.
Products read unions of those supports. Derivatives and integrals preserve equality when their domains and measures agree.
An absolutely convergent sum preserves equality when its indices and summands agree.
At a retained component, E′ and K′ supply the required equality for the support and reference layer.
Subtracting two such equal local coefficients preserves equality as well.

Induction therefore preserves locality **if every move supplies an admitted common formation family on those supports**.
This applies also to a disappeared slot evaluated on the erased history: equal local traces give the same completed slot.
For SA's correction identity, \(Y\) must also contain each healed component whose operation the term reads.
Then \(\mathfrak X'(Y)=\mathfrak X(Y)\), with fixed exterior data, identifies every input to the completed terms.
Subtracting their equal values gives \(V_{\mathfrak X'}(Y)=V_{\mathfrak X}(Y)\).
This containment is another requirement on the formation family, not a consequence of the telescoping identity.
The argument does not depend on the number of steps, but it does not bound or admit their read supports.

For the actual construction the premise already fails at the first use of (N1′).
The strip logarithm has no admitted family to insert into the later difference (2).
The same missing family is needed for the carried forms and elimination factors at SA L17541–17558.
Theorem U′ retains its single-scale pair locality; `wf7-bf.md` and `cond-c.md` retain their stated contained-box implications.
None supplies these stopping collars, their anchor bounds, or the layered formation families at all later stages.

## Result

**(LOC) remains unproved. First failed input: admission of (N1′)'s nest for general histories.**
Its torus endpoint exceeds the domain of the cited localised problem when \(\Omega_0\ne T\).
Clipping and an exact terminal convention repair that domain issue only; admissible intermediate collars remain open.
The common-gauge bound (N2′), its distance growth, and (N3′) for the resulting family also remain open.
Lemma G and the support/reference repairs pass the conditional check above; Lemma N′ supplies conditional formation locality.
No uniform later-step or \(\mathbf R\)-stage locality, rank 7 closure, or (Act) conclusion follows.
The new constructions and obstructions here are by Codex, not yet checked by the other model.
