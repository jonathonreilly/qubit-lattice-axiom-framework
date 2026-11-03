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
`s210-fix.md` contains only its work-in-progress header at the pinned commit.
Hence no repaired formation family is available here. I stop before applying (3) to later steps or R stages.

## Result

**(LOC) is not proved.** The first unusable input is Lemma N's claimed common local family at formation.
Its selection condition permits the exterior read in (4); the cited checked inputs do not supply the stronger condition needed.
Theorem U' and the stored carrier series retain their conditional locality in the pair.
They do not supply the missing family for (2), or the healed correction identity of SA L17964–17980.
No induction uniform in depth, rank 7 closure, or (Act) conclusion follows.
The argument above is by Codex and has not been checked by the other model.
