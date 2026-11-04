# The preparatory shift map

Provenance: Codex (serving variant and effort not exposed; requested effort: max); checkout `ada28a0eb`; 2026-11-04; research text, not an audit; grants no status. Source text: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, commit `31a47c543775`. Not yet checked by the other model.

The continuation also credits Balaban's CMP 119 (1988), 243–285, for the conditional Gaussian and strip method.

## 1. Sources and the common problem

Target: input (A) of `stage-resp.md`, then (D4) at stage \(0\to1\) with one collar layer.
SA means [the outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex); CA-I means [the complete account, I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), at the pin above.
Both were fetched once. The index, neighbouring rows and cited excerpts were read first.
The background theorem below is an inherited input, not re-proved here.
The source search reuses `lit-large-field.md:47–51`; Balaban CMP 122a is not in the supplied paper folder.

CA-I 54287 instructs:
> Express $U^{(n)}_k$ through the new background $U^{(n+1)}_k$ and the fluctuation $(A_j,B_j)$ on the collar $R_n$,

This is a cited construction, not its complex proof. CA-I 54248 also requires the pair
\[
 b\longmapsto\bigl(e^{i\eta\mathbb H^{(n)}_k(b)}\mathbb U,
                         \mathbb J+\mathcal J(b)\bigr).
\]
SA 17923 requires: “argument, its gauge factor and its stored data are formed together.”
Thus a critical field alone is not the requested output.

Write \(-=n\), \(+=n+1\), \(j=h+n\), and \(e_\pm=\mathbf B^{(n)},\mathbf B^{(n+1)}\).
The old determining system is the common problem; do not interpolate its row selector.
SA 17415 puts the prepared boxes “in $\Omega_l^c\cap X$”.
SA 17436 prescribes \(\Omega_l^{\boldsymbol\nu}\cap X=X\setminus Z''_l(X)\) at remade levels.
CA-I 53812–53814 replaces “the member of level” \(j+1\); higher members “are still $Z_i$”.
Therefore \(\Omega_q^-\subset\Omega_q^+\) memberwise, with equality unless \(q=j+1\).
This direction matters: the **old** sequence restricts the new one.
SA 9776 includes the “stage sequences” among its separated sequences; that geometry is an inherited hypothesis here.

SA 5616–5617 defines a row by “at least one endpoint lies in $\Omega_j$, and neither lies in $\Omega_{j+1}$.”
It follows directly that
\[
 \Gamma_j^+\subset\Gamma_j^-,\qquad
 \Gamma_{j+1}^-\subset\Gamma_{j+1}^+,
 \qquad \Gamma_q^+=\Gamma_q^-\quad(q\notin\{j,j+1\}).                 \tag{1}
\]
A changed row has an endpoint in \(\Omega_{j+1}^+\setminus\Omega_{j+1}^-\subset R_n\).
Here CA-I 53758–53760 gives \(\Omega_{j+1}\supset\Lambda_{j+1}\), \(Z_{j+1}=\Lambda_{j+1}^c\), and 53809 gives \(R_n=Z_{j+1}\setminus Z''_{j+1}\).
Keep both row levels and their full averaging carriers. SA 9634 calls each carrier the “double block”.

## 2. What restriction gives at complex data

For each fixed \(e\), let \(T_e\) be the canonical map on the intrinsic datum tube.
`intrinsic-dom.md:152–157` states \(T_e(D)=\Phi_V(i^{-1}\Log(DV^{-1}))\), “well-defined and holomorphic”.
Its background and common-radius hypotheses remain in force.
SA 9695 supplies the exact constraint: \(M_e\Phi(B)=e^{iB}V\).

Let \(W=T_{e_+}(D_+)\), and put \(D_0=M_{e_-}(W|_{\Omega_0^-})\).
Work first near an admitted real datum where both maps and these averages exist.
Let \(a_-(W)\) put the restriction in the old canonical gauge, with value one at its nodes.
SA 9667 fixes this gauge by “axial gauge outside the nodes”.
Its recursion, also written in `o1-decoupled.md:328`, is
\[
 a_-(x)=a_-(z)(\mathcal M^qW)(\Gamma_{z,x}),
 \quad x\text{ a non-node of level }q,\quad z\text{ its parent}.     \tag{2}
\]
There are finitely many factors. On an admitted average domain they are holomorphic and invertible.

SA 9776 assumes “a real $\varepsilon_1$-regular $\mathbf V$” with \(CL^2\varepsilon_1\le\bar\varepsilon\).
Its conclusion, SA 9779–9780, is
\[
 U_{\mathbf B'}(M_{\mathbf B'}(U_{\mathbf B}(\mathbf V)|_{\Omega'_0}))
 =U_{\mathbf B}(\mathbf V)|_{\Omega'_0}
 \quad\text{modulo }\mathcal G^{\rm res}(\mathbf B').
\]
Apply it with \(\mathbf B'=e_-\), \(\mathbf B=e_+\), using (1).
Canonical uniqueness gives, at real data,
\[
                       T_{e_-}(D_0)=W^{a_-(W)}.                   \tag{3}
\]
Both sides are holomorphic on a small common neighbourhood of that real datum.
Their difference vanishes on a real open box. Every real Taylor coefficient there vanishes.
The holomorphic Taylor series is therefore zero. Continue this equality through overlapping admitted neighbourhoods.
This proves (3) on the connected common domain reached from that box.
It does not prove that the required stage domain lies there.
This is the method already used in `o1-decoupled.md:326–330`, now applied to the stage sequences.

For an old-row logarithm \(\Delta\), define the local orbit path
\[
 D_t=e^{it\Delta}D_0,\qquad
 \widehat\Phi_t(W,\Delta)=T_{e_-}(D_t)^{a_-(W)^{-1}},\quad 0\le t\le1. \tag{4}
\]
Its domain requires \(D_+\) in the common domain of (3), and every \(D_t\) in the admitted old tube.
Then \(\widehat\Phi_0=W\). If \(D_1\) is the reconstructed old datum, \(\widehat\Phi_1\) is in its old critical orbit.
An equality with the prescribed representative still requires its assigned return gauge.
Equation (4) is not yet a map of \((A_j,B_j)\), nor a map of independent-current pairs.

## 3. The forcing of this restricted path

Use the raw-row norms of `a3-derivative.md:49–51`:
\[
 \|f\|_{F,w}=\sup_y w(y)\xi_y^3|f|_y,\qquad
 \|b\|_{Y,w}=\sup_c w(y_c)|b(c)|.
\]
In a local real-reference chart write \(B_t=i^{-1}\Log(D_tV_-^{-1})\).
Freeze the old action, rows and slice on that chart.
SA 9708–9709 gives \(F'(A)=K_A^{\mathsf T}\lambda\), \(\mathcal Q^{\rm st}(A)=\mathsf b(B_t)\).
Differentiate these equations, including the multiplier-paired constraint Hessian.
The full forcing for **this** system is exactly
\[
                    f_t=0,\qquad b_t=D\mathsf b(B_t)\dot B_t.       \tag{5}
\]
This is SA 11780–11781, not an omission of the constraint curvature.
SA 11794 requires parameter differentiation “before substituting the solution”.

For \(\|D_tV_-^{-1}-I\|\le1/2\) and \(\|D_tV_-^{-1}\|\le2\), the logarithm series gives
\[
                         \|\dot B_t\|_{Y,w}\le4\|\Delta\|_{Y,w}.    \tag{6}
\]
Indeed its derivative norm is at most \(\sum_{r\ge1}(1/2)^{r-1}=2\), and \(\dot D_t=i\Delta D_t\).
This argument is rowwise, so it preserves support and every scalar row weight.

SA 9929–9935 gives \(e^{i\mathsf b(B)(c)}=e^{iB(c)}Z_c(B_{\rm int})\), where the second factor reads one finer block.
SA 9978–9979 states \(D\mathsf b=D+T\), \(TD^{-1}T=0\).
SA 9987–9997 says “both row and column counts are bounded at fixed $L$”, independently of the number of layers.
These are the detailed finite-datum estimates; they include the outward block factor.
Thus, under their admitted-chart hypotheses, \(D\mathsf b\) has a uniform weighted norm \(C_b\).
If \(\Delta\) is supported on rows \(K\), let \(K^+\) also contain each outward row reading an interior row of \(K\).
No further propagation occurs in this derivative. Hence
\[
 \operatorname{supp}b_t\subset K^+,\qquad
              \|f_t\|_{F,w}+\|b_t\|_{Y,w}\le4C_b\|\Delta\|_{Y,w}. \tag{7}
\]
The enlargement is by the actual row carriers, not by all bonds of a shell.
With \(w=e^{\theta d_{e_-}(\cdot,K^+)}\), a weighted A3 inverse gives decay from \(K^+\).
No count of collar bonds enters. The inverse remains a named input.
Likewise `dec-field.md:247` says “Assume [PW], [NL]”; its (5.2) differentiates with the operators fixed.
Equation (7) has no small stage size until \(\Delta\) has one.

## 4. The reconstruction problem at the start of this continuation

The first missing input was the **matched stage reconstruction**, already at \(n=0\).
Sections 6–9 record the first continuation. Sections 10–13 correct its coordinate objection.
Sections 14–18 continue the attack. They also correct the demand for a common Gaussian between stages.
On physical backgrounds it must give the old raw datum \(D_1=\mathcal R_n(P,A_j,B_j;\zeta)\) and its return gauge.
Here \(P\) includes the independent current; \(\zeta\) includes every earlier parameter and switch.
On that critical family the field formula would be
\[
 \Delta_n=i^{-1}\Log(\mathcal R_nD_0^{-1}),\qquad
 \Phi(P,A_j,B_j;\zeta)=T_{e_-}(e^{i\Delta_n}D_0)^{r_n}.             \tag{8}
\]
The datum must match all surviving rows. On the physical locus, the endpoint must satisfy the new coarse constraints.
At general decoupling parameters, use the specified R9 equations instead; they do not assert those constraints.
The newly released raw datum must have collar support and a small uniform size
\(\sigma_j=\sup_{P,\zeta}\|\Delta_n\|_Y\) sufficient for (10).
An earlier conditional mean need only have a controlled exponential tail; its inverse need not have finite range.
Include any enlargement from the switch radii in \(\sigma_j\); a real test at size \(\delta'_j\) does not bound that supremum.
The path must be admitted; the prescribed gauge and current must be identified, with their own bounds.
Neither \(\mathcal R_n\) nor \(r_n\) in (8) is supplied by defining \(T_{e_-}\).
Thus (8) specifies the missing map; it does not assert its construction.
For general independent pairs, (8) is not asserted: the prescribed decoupled response need not be a critical background.
One must match its actual fixed system or comparison identity, including its current.
The exact warning is `a3-derivative.md:33`:
> without a common restriction problem, matched collar rows, and an admitted interpolation.

There is a useful existing chart, so the missing input is not a generic inverse-function theorem.
SA 8289–8296 proves
\[
 a(u)=\Psi_V(\mathsf C_Vu),\quad q_V(a(u))=0,\quad a(u)|_{\rm free}=u,
 \qquad \|a(u)\|+\|D_ua(u)\|\|u\|\le CL^4\|u\|.
\]
It is a detailed local proof on \(\|u\|<cL^{-9}\).
To use it here, identify its free coordinate \(u\) with the actual stage coordinates, including the conditional mean and boundary returns.
SA 7614 says the conditional Gaussian “mean is linear in that field”; it also retains a strip change of variables.
SA 7601 says seam contributions “remain in the boundary exponent and require its separate estimates”.
These facts do not justify setting \(u=g_j(A_j+B_j)\) without that identification.
The next calculation must construct this identification on the collar, then compute \(\Delta_n\) in (8).

The current is a further part of the same match, not a free choice.
`wf-room-2.md:290–295` assigns
\[
 \mathsf j=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}\lambda^{\rm I}
                 -K_0^{\mathsf T}\lambda^{\rm I}_0,
 \qquad\text{and carries }\mathbf J+\mathsf j.
\]
Its exact words are “the independent current”, carried “additively”.
Replacing it by \(J(\widehat\Phi_t)\) is not the specified extension.
SA 5800–5803 gives background recovery only “At $s=1$ and real background data”.
That locus does not determine a holomorphic function of the independent variables.
For example, \(c(s-1)\ell(\Delta)\), with \(\ell\) any nonzero linear functional, vanishes there and at \(\Delta=0\).
It has arbitrary size for a different fixed \(s\) as \(c\) varies.
This is a failure of the proposed identity-theorem inference, not a counterexample to the prescribed response.
SA 11798–11805 accordingly requires the “complete gauge and current normal form” to “be matched”.

For any genuine bridge with changing coefficients, (5) must be replaced by the full forcing:
\[
 f=-\partial_pF'_p(A)\dot p+
             (\partial_p\mathcal C_A\dot p)^{\mathsf T}\lambda,
 \qquad b=-\partial_p\mathcal C\dot p.                            \tag{9}
\]
This is SA 11785–11791 with \(\mathcal E=F'_p-\mathcal C_A^{\mathsf T}\lambda\).
It does not include a moving slice. SA 11748–11751 also requires \((\dot R D^{\mathsf T}+R\dot D^{\mathsf T})A\) in that case.
No bound for (9) on the actual stage family has been proved here.
In particular, (7) gives no uniform estimate over the earlier compositions or switch discs.

## 5. Consequence for stage \(0\to1\)

Here is the precise conditional use of `stage-resp.md` (5)–(8).
Suppose the missing reconstruction supplies, for every complete returned read, its section 4 bound
\[
 \|\dot F_a\|\le Cr_a\sum_{l\in E_0}u_l\sqrt{1+|m-l|}e^{-D|m-l|},
 \qquad D\ge\log4,\quad Cu_l<\beta_R/2.                          \tag{10}
\]
The conversion from (7) to (10) still requires the actual source, shell distance, radius conversion and return bounds.
`stage-resp.md:131` explicitly requires “the shell distance must bound $|m-l|$”.
SA 17621 supplies the sketched real-curvature size \(C(\delta'_j/\varepsilon_j)(1+\sqrt{j-i})e^{-c(M/M_1)(j-i)}\); it is not an estimate for all returned complex entries.

For an integer \(q\ge0\), induction gives \(q+1\le4^q\): equality holds at zero, and \(q+2\le4(q+1)\) proves the step.
Thus each term of (10) integrates to less than \(\beta_Rr_a2^{-|m-l|}/2\).
Sum only over the actual recorded marks \(E_0\); two changed row levels do not automatically give two marks.
On reads with no new mark, one still needs `stage-resp.md` (6), with allowance \(g_k(m)r_a/(4N)\).
For an estimate made before return, its (8) instead charges
\(r_a\{(e^{2A}-1)c_*+e^{2A}E\}\); this charge also needs a proved budget.
These are the source's explicit allowances, not bounds furnished by (7).

If those expenditures are below \(d_0(m)r_a/2\), its first-exit argument gives
\[
              q_a(X_t)<c_0(m)r_a-d_0(m)r_a/2.
\]
`stage-resp.md:163` also requires “tube membership, real gauge witnesses and stored-slot domains” to “retain room”.
Under those hypotheses, \(S_0(D_1^{\rm int};\zeta)\subset D_0^{\rm int}\), with half the numerical margin left.
There is no unconditional (D4) conclusion, even in the single-layer case.

## 6. Reconstruction in the unconditioned free coordinates

This section computes (8) in free coordinates. It does not yet identify the stage's Gaussian coordinates.
All claims retain the admitted background charts of sections 1–3.
Credit for the block map, pivots and nonlinear graph belongs to the authors named above.

Use the no-inward-bond convention. Take the single-layer change in (1), with the same first domain.
Put
\[
 K=\Gamma_j^-\setminus\Gamma_j^+,\qquad
 C=\Gamma_{j+1}^+\setminus\Gamma_{j+1}^- .                       \tag{11}
\]
Here \(C\) is a set of rows, not a covariance.
Let \(V=\mathcal M^jW\), in a common gauge, on the required carriers.
The exact row used below is SA 7992–7994:
\[
 q_{V,c}(a)=i^{-1}\Log\{\mathcal M(e^{ia}V)(c)\mathcal M(V)(c)^{-1}\}.
\]
Thus it uses the actual group average, not its straightened derivative.

**Carrier condition.** Each \(c\in C\) has its complete one-step carrier among the old level-\(j\) rows.
Its pivot belongs to \(K\). These conditions hold for a global aligned single-layer change with the stated gaps.
Here alignment means that each member is a union of whole blocks on the nested centered grids.
Take the fixed gap larger than \(2L\) in level-\(j\) units, as the large-gap hypotheses permit.
Here is the geometric check. Neither endpoint of an added row belongs to \(\Omega_{j+1}^-\).
Both endpoint blocks therefore miss that region, since it is a union of whole aligned blocks.
At least one endpoint belongs to \(\Omega_{j+1}^+\).
The separation from \((\Omega_j)^c\) puts both blocks in \(\Omega_j\).
Every bond of their rectangular carrier is therefore an old level-\(j\) row.
The crossing pivot has an endpoint in \(\Omega_{j+1}^+\), so it is removed from that row set.
The source anchors are SA 9593, “union of cubes”, SA 9596, \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\xi_j\),
and SA 9599, “form a partition”. Use their nested-grid alignment, not an arbitrary translated partition.
SA 9607 gives “no end point in $\Omega_{j+1}$”.
SA 7947–7955 gives the carrier \(D_c=B(y)\cup B(y')\).
SA 8167–8174 gives its pivot and the fact that no other row's pivot occurs in its formula.
For a localized earlier read, this carrier check must be made on that read's actual rows.
It is not a consequence of an endpoint being in the global collar.

Remove the pivots \(b_0(c)\), \(c\in C\), from \(K\), and call the remaining set \(F\).
Give \(F\) the coordinates \(u\). Set all other nonpivot increments to zero.
Use the pivot graph only for the rows in \(C\).
Its proof in SA 8257–8299 applies unchanged to this subset: the pivot equations are independent.
In particular, SA 8224 and 8230–8233 give
\[
 \mathsf C_V=\iota-h_VK_V\iota,\quad K_Vh_V=1,\quad
 K_V\mathsf C_V=0,\quad \|\mathsf C_V\|\le C_L,
 \qquad C_L\le C L^4 .
\]
The nonlinear correction changes pivots only. Consequently
\[
 a_V(u)=\Psi_V(\mathsf C_Vu),\quad
 \operatorname{supp}a_V(u)\subset K,\quad
 q_{V,c}(a_V(u))=0\ (c\in C),\quad a_V(u)|_F=u.                 \tag{12}
\]
The bounds are \(\|a_V(u)\|\le C_L\|u\|\) and \(\|D_ua_V(u)\|\le C_L\).
Choose \(\|u\|<\min\{cL^{-9},(8C_L)^{-1}\}\), and use a smaller open ball when necessary.
The derivative bound at zero follows by continuity from SA 8295–8296.
The case \(C=\varnothing\) has no pivot correction.

Define the old datum by
\[
 D(u)(b)=
 \begin{cases}
 e^{ia_V(u)(b)}D_0(b),&b\in K,\\
 D_0(b),&b\notin K.
 \end{cases}                                                   \tag{13}
\]
On its admitted domain put \(W(u)=T_{e_-}(D(u))\).
It satisfies every surviving old row, by definition of \(T_{e_-}\).
It also satisfies every added new row.
Indeed, on that row's complete carrier its level-\(j\) average equals the datum (13).
Applying one more average and (12) gives \(\mathcal M^{j+1}W(u)(c)=D_+(c)\).
Every other new row is an old surviving row. This proves all the new constraints.
At zero, (3) identifies \(W(0)\) with the restricted new background, in the old canonical gauge.
This proves a local parametrization of the old critical backgrounds in the new constraint fibre.
For the converse, take an admitted old critical background in that fibre with the fixed surviving datum.
Its level-\(j\) raw logarithm on \(K\) solves the same added-row equations.
The uniqueness in SA 8297–8299 identifies it with (12) at its free restriction.
Uniqueness of the old canonical background then gives (13).
It does not say that these backgrounds are critical for the new problem.

The small logarithm in (8) is now explicit:
\[
                  \Delta(u)|_K=a_V(u)|_K,\qquad
                  \Delta(u)|_{e_-\setminus K}=0.                \tag{14}
\]
There is no extra Baker–Campbell–Hausdorff term: \(D(u)D_0^{-1}=e^{ia_V(u)}\) row by row.
Although two row levels change, the raw source in this construction lies at level \(j\) only.
The reduced source can still reach the outward rows described in (7).

Use the path \(D(tu)\), not \(e^{it\Delta(u)}D_0\), if the new constraints must hold along the path.
The two paths have the same endpoints. In general their intermediate points differ.
The derivative of the exponential gives
\[
 \|\partial_tD(tu)D(tu)^{-1}\|_{Y,w}
 \le 2\|\partial_t a_V(tu)\|_{Y,w}.
\]
To verify the factor, write its left logarithmic derivative as
\(i\int_0^1 e^{isa}(\partial_ta)e^{-isa}\,ds\), and use \(\|a\|\le1/8\).
Each pivot depends on one double block only.
For a weight of rate \(\theta\), transferring the weight within that carrier costs at most \(e^{\theta\rho_L}\).
Here \(\rho_L\) bounds its diameter in the old metric, in layer-\(j\) units.
Thus \(\|\partial_ta_V(tu)\|_{Y,w}\le C_{L,w}\|u\|_{Y,w}\), with no collar-volume factor.
Equations (5)–(7) give, on this fixed physical system,
\[
 f_t=0,\qquad
 \|b_t\|_{Y,w}\le8C_bC_{L,w}\|u\|_{Y,w}.                       \tag{15}
\]
This is a proved bound for the free-coordinate path, conditional on its stated charts and inverse inputs.
It acquires a stage size only after the actual stage coordinates have been matched to \(u\).

## 7. The mean and strip terms in that coordinate

The conditional mean has a definite sign. Its absence from the earlier calculation was substantive.
SA 17528 gives the exponent's cross term \(-\langle A,\Delta^{(j)}A'\rangle\).
CA-I 47943–47957 gives its full block square and Schur complement.

In a specified free-coordinate basis, write the Gaussian precision and field as
\[
 Q=\begin{pmatrix}P&R\\R^{\mathsf T}&S\end{pmatrix},\qquad
 y=(y_I,e),\qquad C_I=P^{-1},\qquad M=-C_IR.                    \tag{16}
\]
The index sets \(I,E\) refer to this basis. Transposes use its actual pairings, and \(Q=Q^{\mathsf T}\).
For a real Gaussian assume \(Q>0\). For the algebra at complex data, assume only that \(P\) is invertible.
Set \(y_I=b+Me\). Direct expansion gives
\[
 \tfrac12\langle y,Qy\rangle
 =\tfrac12\langle b,Pb\rangle
  +\tfrac12\langle e,(S-R^{\mathsf T}C_IR)e\rangle.              \tag{17}
\]
The cross term cancels because \(PM=-R\).
The remaining exterior term is \(S-R^{\mathsf T}C_IR\), since \(P,C_I\) are symmetric.
Thus the conditional mean of the uncentered interior coordinate is \(Me\), not zero.
This proves the square completion by hand.
It does not identify an arbitrary stage matrix with \(Q\).
CA-I 47931–47936 and 47960–47967 make the identification with Balaban's conditional integral on
\(\mathfrak G=\{J=J(\mathbf U)\}\); the block algebra itself holds on the larger stated domain.

The order matters. SA 17516 puts “a change of variables” before “a conditional Gaussian integral”.
SA 17521–17523 specifies, on a strip bond,
\[
 V^{\rm bg}=e^{ih}V^{\rm loc},\qquad
 V^{\rm old}=W'e^{-i\vartheta(W')h}e^{ih}V^{\rm loc}.
\]
For \(W'=e^{iv}\), this gives the following **exact** free physical logarithm relative to \(V^{\rm bg}\):
\[
        \mathcal L(v,h,\vartheta)
        :=i^{-1}\Log(e^{iv}e^{-i\vartheta h}).                   \tag{18}
\]
The adjacent factors \(e^{ih}e^{-ih}\) cancel. No commutation with \(W'\) is used.
On a declared split of the free coordinates, the reconstruction is therefore
\[
 u_I=g_j(b+Me),\qquad
 u_E(b')=
 \begin{cases}
 \mathcal L(g_je(b'),h(b'),\vartheta(b')),&b'\text{ in the strip},\\
 g_je(b'),&\text{otherwise}.
 \end{cases}                                                   \tag{19}
\]
One must apply (19) in the free basis which was used for (16).
Section 10 identifies that basis from the source, rather than from the Gaussian form alone.
Equation (19) describes one conditional read. It does not identify its two blocks with the two stage integrals.
The pivots are reconstructed afterwards by (12).
The strip's changes to the original exponent remain in its boundary term.
They are not silently absorbed into \(P,R,S\).
Balaban's supplied CMP 119 text, lines 453–457, 473–493 and 1361–1372, gives the same order and sign.
Its formulas (1.22) and (3.22) are the sources cited at SA 17526.

Here are usable derivative bounds, not only an identification at one point.
For \(\|v\|+|\vartheta|\|h\|\le1/4\), the exponential series puts
\(e^{iv}e^{-i\vartheta h}\) within distance \(1/2\) of the identity.
The logarithm derivative has norm at most two there.
The exponential derivative has norm at most \(e^{\|X\|}\) at \(X\).
Integration on the segment from zero therefore gives
\[
 \|\mathcal L\|\le4(\|v\|+|\vartheta|\|h\|),\qquad
 \|\dot{\mathcal L}\|
 \le4(\|\dot v\|+|\vartheta|\|\dot h\|+|\dot\vartheta|\|h\|).
                                                                    \tag{20}
\]
These estimates are bondwise and preserve scalar weights.
Here \(\vartheta\) is a scalar parameter, or a differentiable cutoff evaluated on real variables.
The formula does not evaluate that cutoff on complex variables.
For moving Gaussian coefficients, differentiating \(PC_I=1\) gives
\[
 \dot C_I=-C_I\dot P C_I,\quad
 \dot M=C_I\dot P C_IR-C_I\dot R,\quad
 \dot u_I=g_j(\dot b+M\dot e+\dot M e),                          \tag{21}
\]
with \(g_j\) fixed. If the coupling moves, add \(\dot g_j(b+Me)\).
In particular the size of the stored exterior field multiplies the coefficient derivative.
This term is absent from the replacement \(u=g_j(A_j+B_j)\).

**Seams.** SA 7601 retains “constant and linear terms”; SA 7866 retains “fluctuation variations”.
Write its Taylor expansion as \(B_{\partial}(y)=B_{\partial}(0)+\ell_{\partial}(y)+B_{\partial,\ge2}(y)\).
The convention (16)–(19) leaves all three terms in that exponent.
If instead one moves \(\ell_{\partial,I}\) into the Gaussian, the center changes by \(C_I\ell_{\partial,I}\).
This follows by expanding the square with cross source \(Re-\ell_{\partial,I}\).
Hence dropping the seam term and recentering are different operations.
The physical critical equation in section 6 still uses the restricted Wilson action.
It does not become stationarity for the full boundary exponent.

**Local inverse of the real strip map.** This part of SA 17526 can also be proved directly.
Take \(v,h\) Hermitian, so the map takes values in the same real Lie algebra.
Suppose \(0\le\vartheta\le1\), \(\|D_v\vartheta\|\le C_\vartheta/\delta\), and \(0<\delta\le1\).
A fixed smooth cutoff rescaled by \(\delta\) has this property, with fixed \(C_\vartheta\).
Keep \(h\) fixed and \(\|v\|+\|h\|\le1/4\).
First differentiate with \(\vartheta\) fixed.
On \(\|E\|\le1/2\), the second derivative of \(\Log(1+E)\) has norm at most
\(\sum_{n\ge2}(n-1)2^{-(n-2)}=4\).
This follows by differentiating each monomial in its convergent series twice.
For \(E=e^{iv}e^{-i\tau\vartheta h}-1\), the three derivative norms
\(\|D_vE\|,\|\partial_\tau E\|,\|D_v\partial_\tau E\|\)
are at most \(2,2\|h\|,2\|h\|\), respectively.
The chain rule thus bounds \(D_v\partial_\tau\mathcal L\) by \(20\|h\|\).
Integrate from \(\tau=0\), where \(\mathcal L(v,0,\vartheta)=v\).
Allowing \(\vartheta\) to vary adds at most \(4\|h\|C_\vartheta/\delta\), by (20).
Consequently
\[
 \|D_v\{\mathcal L(v,h,\vartheta(v))-v\}\|
 \le(20+4C_\vartheta)\|h\|/\delta .
\]
If the right side is below \(1/2\), write the map as \(v\mapsto v+R(v)\).
On a closed ball about \(v_0\), solve \(v=z-R(v)\).
For \(z\) within half that ball's radius of \(v_0+R(v_0)\), this is a contraction into the ball.
Its iterates converge geometrically to a unique inverse value.
Subtracting two fixed-point equations bounds the inverse's Lipschitz constant by two.
The inverse derivative is \((1+DR)^{-1}\), by the same convergent series.
Thus the real local change of variables is justified with an explicit smallness condition.
This does not identify the stage coordinates or prove admission on their complex discs.

**Real cutoffs and complex switches.** SA 17526 specifies a “smooth cut-off”, equal to zero and one on open ranges.
It has no nonconstant holomorphic extension through the whole transition range.
Indeed a holomorphic extension would equal zero near the first range, then everywhere on its connected domain.
Thus \(\vartheta(e^{ig_j\mu e})\) is not a permitted use of (18) for complex \(\mu\).
This is no counterexample to the source: SA 6166 says “Borel”; SA 6167 says “jointly analytic”.
The latter applies to the pair, far variables and switches on the domains of SA 6167–6168.

For one real stored coordinate \(e\), a possible analytic switch interpolation is
\[
 u(\mu,e)=u_{\rm base}+\mu\{u_{\rm end}(e)-u_{\rm base}\},
 \qquad u_{\rm base}=u_{\rm end}(0),                            \tag{22}
\]
where the endpoint formula uses the real cutoff. Hold all other coordinates fixed.
It has both zero identities, directly by substitution.
Its endpoint increment costs \(\lambda_j^{\rm st}\|u_{\rm end}(e)-u_{\rm base}\|\) on the switch disc.
It is a possible prescription, not an identification with the carried stage function.
The source's prescribed switching and returns must be matched before (22) can replace them.

## 8. The full reduced forcing and the assigned current

The physical forcing (15) cannot be used as the forcing of every decoupled read.
SA 10369–10372 says “before the parameters are inserted”.
SA 10462–10464 says “no constraint identity” at arbitrary complex decoupling parameters.
Here is the exact replacement for the first system; it includes changes of its coefficients.

Write its two reduced equations as
\[
 a+G_pW_p(a)=H_{1,p}b_p,\qquad h+H_p\mathcal C_p(h)=a .          \tag{23}
\]
These are SA 10362–10365, with \(h=\mathbf H\) and \(G=\mathfrak G\).
Fix the geometry and identify the bond and row spaces before using these formulas.
They do not differentiate a discrete row selector.
Here \(b_p\) is the specified reduced raw-row datum, not automatically \(\Delta\).
At a fixed physical reference with datum \(D_0\), use \(b_t=\mathsf b(\Delta(tu))\).
SA 9929–9935 gives \(e^{i\mathsf b(B)(c)}=e^{iB(c)}Z_c(B_{\rm int})\) on an outward row.
Use the assigned expression [RED] in `nl-r9.md:212–231` when reading that library theorem.
All partial derivatives below are taken at fixed unknowns.
Direct differentiation gives
\[
 \begin{aligned}
 (1+G_pW'_p(a))\dot a&=F_1,\\
 (1+H_p\mathcal C'_p(h))\dot h&=\dot a+F_2,\\
 F_1&=H_{1,p}\dot b_p+(\partial_pH_{1,p}\dot p)b_p
       -(\partial_pG_p\dot p)W_p(a)-G_p\partial_pW_p(a)\dot p,\\
 F_2&=-(\partial_pH_p\dot p)\mathcal C_p(h)
       -H_p\partial_p\mathcal C_p(h)\dot p .
 \end{aligned}                                                  \tag{24}
\]
The nonlinear Jacobians belong on the left. This implements SA 11794–11796's differentiation order.
Under the admitted [PW] and [NL] bounds, let their weighted norms be at most \(q,q_C<1\).
The convergent geometric series for the two inverses proves
\[
 \|\dot h\|_{X,w}\le
 \frac{(1-q)^{-1}\|F_1\|_{X,w}+\|F_2\|_{X,w}}{1-q_C}.           \tag{25}
\]
For fixed coefficients, (24) reduces exactly to `dec-field.md:274–279`.
For a moving earlier read, the other five terms cannot be omitted.
Uniform bounds for operators alone do not bound their derivatives along that read.

The current assignment also has an exact derivative.
Put \(T=(K_h-K_0)H_p\), \(N=1+T^{\mathsf T}\), and use the adopted formula
\[
 \lambda=N^{-1}H_p^{\mathsf T}F'_p(h),\quad
 \lambda_0=H_p^{\mathsf T}F'_p(0),\quad
 j=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0.           \tag{26}
\]
This is `wf-room-2.md:290–295`, without replacing the independent baseline current.
The operators can depend on that baseline; holding the decoupling parameters fixed does not freeze a moving pair.
Differentiating the defining equations gives
\[
 \begin{aligned}
 N\dot\lambda={}&\dot H_p^{\mathsf T}F'_p(h)
 +H_p^{\mathsf T}\{F''_p(h)\dot h+\partial_pF'_p(h)\dot p\}
 -\dot T^{\mathsf T}\lambda,\\
 \dot\lambda_0={}&\dot H_p^{\mathsf T}F'_p(0)
                   +H_p^{\mathsf T}\partial_pF'_p(0)\dot p,\\
 \dot j={}&\dot R_hK_h^{\mathsf T}\lambda
 +R_h\dot K_h^{\mathsf T}\lambda+R_hK_h^{\mathsf T}\dot\lambda
 -\dot K_0^{\mathsf T}\lambda_0-K_0^{\mathsf T}\dot\lambda_0 .
 \end{aligned}                                                  \tag{27}
\]
The complete current derivative is \(\partial_t(\mathbf J_p+j)=\dot{\mathbf J}_p+\dot j\).
The baseline term vanishes only when the input pair is fixed.
No physical stationarity identity is used here.
For fixed coefficients, move the two derivatives in \(H_p^{\mathsf T}D^{\mathsf T}D\dot h\)
onto the two factors: \((DH_p)^{\mathsf T}D\dot h\).
The weighted row sums (O1), `wf-room-2.md:328–335`, then use only the first-order norm of \(\dot h\).
More explicitly, put \(r=\|h\|_X\) and \(L_\lambda=\|\lambda\|_Y\).
The Wilson remainder estimate and (O1) give
\[
 \|H_p^{\mathsf T}F''_p(h)v\|_{Y,w}
 \le CC_H(1+\alpha_0+r)\|v\|_{X,w},\qquad
 \|H_p^{\mathsf T}(D_hK_h[v])^{\mathsf T}\lambda\|_{Y,w}
 \le CC_H L_\lambda\|v\|_{X,w}.
\]
The second inequality uses the local row derivative bound in `wf-room.md` (5.1).
At fixed coefficients \(\dot T=(D_hK_h[\dot h])H_p\).
Hence (27) and \(\|N^{-1}\|\le2\) give
\(\|\dot\lambda\|_{Y,w}\le CC_H(1+\alpha_0+r+L_\lambda)\|\dot h\|_{X,w}\).
Formula (5.6) of `wf-room.md:232–238` then gives
\(\|\dot j\|_{F,w}\le C_J\|\dot h\|_{X,w}\).
The uniform bound for \(L_\lambda\) is (6.3) of `wf-room-2.md:315–319`.
This proof retains (O1), the local Wilson and row derivative estimates, and the small response ball.
For moving coefficients the extra terms in (27) remain.

One can see the failed physical identification algebraically.
Set \(E=F'_p(h)-K_h^{\mathsf T}\lambda\). Then (26) implies
\[
                  H_p^{\mathsf T}E=(1-K_0H_p)^{\mathsf T}\lambda. \tag{28}
\]
Expand \(K_hH_p=K_0H_p+T\) to check this identity.
The right side is not set to zero by the decoupled prescription.
Even if it vanished, testing against \(H_p\) alone would not test every slice direction.
Thus matching (26) does not license replacing (23) by the physical saddle equations.

Finally a return gauge also contributes to the derivative.
For \(\widetilde U(b)=r_-U(b)r_+^{-1}\), put \(\rho_\pm=\dot r_\pm r_\pm^{-1}\).
Product differentiation gives
\[
 \dot{\widetilde U}\widetilde U^{-1}
 =\rho_-+\operatorname{Ad}_{r_-}(\dot U U^{-1})
           -\operatorname{Ad}_{\widetilde U}\rho_+,\qquad
 \partial_t J^r=\operatorname{Ad}_{r_-}\dot J+[\rho_-,J^r].       \tag{29}
\]
Equations (24), (27) and (29) are the complete derivatives of this proposed read.
They do not give numerical budgets for an unassigned return.

## 9. The remaining lemma and three attacks

The remaining assertion concerns the actual conditional coordinates and their transport.
The primitive chart is now explicit. Its use for the stage is not yet proved.

**Lemma M — uniform matching of the stage coordinates (unproved).**
Fix a finite admissible single-layer history at stage \(0\to1\), and its complete roster of earlier reads.
Use the stage's actual free-coordinate spaces, Gaussian forms, strip substitutions, and recorded returns.
For every input \(P\in D_1^{\rm int}\), every allowed \((A_j,B_j)\), and every earlier parameter and switch value \(\zeta\),
there is a matched endpoint \(u_\star(P,A_j,B_j;\zeta)\) in the ball of (12).
It is holomorphic in the permitted complex variables and Borel in the near real variables.
At physical data the actual old raw datum is exactly \(D(u_\star)\) of (13).
Its assigned return gives the prescribed old representative, not just its orbit.
For the initial raw datum use \(u_t=tu_\star\). For an earlier conditional read use its actual coordinate path.
Such a read can have a nonzero coordinate at the initial endpoint; section 10 gives its relative datum.
The full path, including stored slots and assigned returns, must start at the input \(P\).
Its endpoint is the actual stage read \(S_0(P;\zeta)\).
At other parameters its extension is (23), with current (26), using the same matched datum.
After the returns and each earlier read, the derivatives calculated in (24), (27), and (29) obey
\[
 \|\partial_tF_a\|
 \le C r_a\sum_{l\in E_0}v_l\sqrt{1+|m-l|}\,e^{-D|m-l|},
 \qquad D\ge\log4,\qquad Cv_l<\beta_R/2,                       \tag{30}
\]
uniformly in the listed variables.
For a read with no new mark, replace the integrated right side by \(g_k(m)r_a/(4N)\).
The path stays in the primitive, Gaussian and return charts, with strict room for continuation.
Stored near variables remain real; their Borel and switch dependence has the two zero identities of SA 6169–6170.
Here \(F_a,r_a,E_0,g_k(m),N\) are exactly those of `stage-resp.md:104–163`.
Thus the lemma specifies one transport assertion on a fixed roster; it does not choose new domains or currents.

**Attack 1: reconstruct the free coordinate directly.**
Equations (12)–(15) solve the group constraints and compute \(\Delta\), including the carrier support.
Equations (16)–(21) then give the conditional and strip corrections in any specified free basis.
The failed step in the first continuation was to identify that basis and its two injections with the actual \(A_j,B_j\) of CA-I 54249–54250.
Those lines give \(\tfrac12\langle A_j,C^*\Delta^{(j)}_{\Lambda_{j+1}}CA_j\rangle\) and
\(\tfrac12\langle B_j,C^*\Delta^{(j)}CB_j\rangle\).
Those two lines alone do not supply that map. However, CA-I 45283–45292 fixes the free bond coordinates.
SA 7484 and 8224 fix their embedding. Section 10 removes the arbitrary-basis objection for each such read.
A Gaussian form alone cannot identify coordinates: a change \(y=Oz\) replaces its precision by \(O^{\mathsf T}QO\).
Even transformations preserving a Gaussian form can change a supremum norm or the support of a coordinate.
For example \(O=2^{-1/2}\left(\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\right)\) preserves \(Q=1\).
It sends \((1,1)\) to \((\sqrt2,0)\). Both changes are visible by multiplication.
This example is therefore not evidence of an ambiguity in the source's specified free coordinates.
The stage still needs the actual slot and return match, beyond the fixed-read formula (19).
The direct graph therefore proves (15), but not that its right side is the source size of the requested stage.

**Attack 2: infer the transition by Gaussian elimination.**
Nested elimination is consistent for the complete quadratic form.
Assume the two successive eliminated blocks are invertible.
For three disjoint sets \(I,C,E\), first eliminate \(I\) by (17).
The remaining precision on \(C\cup E\) is its Schur complement.
Eliminating \(C\) next solves the two original linear equations for \((y_I,y_C)\), with \(y_E\) fixed.
Eliminating \(I\cup C\) at once solves those same equations.
Invertibility makes the solution unique. The centers and remaining forms are therefore equal.
This proves associativity, including the centers, without a determinant or numerical argument.
The claim concerns the center and quadratic form, not the normalization or the boundary interactions.

It does not apply to an arbitrary kept conditional form.
SA 17550–17558 assigns chains to components and says “not a Schur complement”.
Let \(\widetilde P,\widetilde R\) be the blocks of that other form, and \(\widetilde M=-\widetilde P^{-1}\widetilde R\).
Subtracting \(PM=-R\) and \(\widetilde P\widetilde M=-\widetilde R\) gives
\[
 M-\widetilde M
 =-P^{-1}\{(R-\widetilde R)+(P-\widetilde P)\widetilde M\}.       \tag{31}
\]
The failed step is a small weighted bound on this **actual** expression after the stage returns.
Its factors must be the matched complete and kept forms, including their seam and independent-current terms.
Positivity alone cannot supply the required supremum bound.
For example take \(v=N^{-1/2}(1,\ldots,1)\) and
\[
 Q_N=\begin{pmatrix}I_N&v/2\\v^{\mathsf T}/2&1\end{pmatrix}.
\]
Its eigenvalues are \(1\) on \(v^\perp\), and \(1\pm1/2\) on the remaining two-dimensional subspace.
Yet conditioning its last coordinate on \(e=(1,\ldots,1)\) gives mean \(-\sqrt N/2\).
This hand example rejects a spectral-gap-only proof; it is not a lattice stage counterexample.
The local weighted bounds and the actual coordinate comparison remain essential.

**Attack 3: avoid coordinates by differentiating the critical equations.**
The physical fixed-system route gives (15). It is exact on its admitted physical family.
Trying the same route for the independent-current family meets the defect (28).
I therefore differentiated the specified reduced system instead, obtaining (24)–(27).
This repairs that algebraic step and includes all coefficient derivatives.
It leaves the terms \((\partial_pH_1\dot p)b\), \((\partial_pG\dot p)W\),
\(G\partial_pW\dot p\), \((\partial_pH\dot p)\mathcal C\), and \(H\partial_p\mathcal C\dot p\).
They include the conditional-mean derivative in (21) once the stage is inserted.
The failed step is to give their weighted source size and collar localization for every earlier read.
A Cauchy bound on an operator ball of radius \(r\) gives a factor proportional to \(\|\dot p\|/r\).
It does not bound \(\dot p\), which is the transported earlier read that this argument must control.
Applying the physical restriction identity or the fixed-coefficient response bound here would assume the missing comparison.
Complex return tangents in (29) and the switch amplification in (22) must be included in that comparison.

These are three distinct routes to Lemma M: local fibre reconstruction, Gaussian elimination, and differential response.
Each reaches a written formula. None establishes the asserted uniform matched transport.
No example above refutes the actual stage, its kept-form estimate, or its inclusion.

## 10. The fixed-read coordinate match

This continuation read the source definitions omitted in the first coordinate attack.
CA-I 45283–45292 specifies the “free unit bonds” and says the “pivot bonds are removed”.
It also specifies the two coordinate projections.
In its notation take \(F=\mathbb B^+\), \(I=\mathbb B\), and \(E=\mathbb B'\).
The choice of \(I\) is part of the integral; it is not inferred from a covariance.
In particular, the sets with both endpoints inside and with at least one endpoint inside differ by crossing bonds.
CA-I 45290–45292 uses “both end-points” and “at least one end-point”, and defines their difference as \(\mathfrak x\).

**The embedding is unique.** Use the same averaging row, pivots, orientation and gauge on both sides.
Suppose \(C:F\to\ker K_V\) leaves the free values unchanged.
Then \(Cu-\iota u\) is supported on the pivots and
\(K_V(Cu-\iota u)=-K_V\iota u\).
The pivot inverse in SA 8221–8224 gives
\[
                 C=\iota-h_VK_V\iota=\mathsf C_V.              \tag{32}
\]
This proves uniqueness by solving each pivot equation.
SA 7484 uses precisely the free-coordinate coarea integral
\(F(e^{i\psi^{\rm lin}(\mathsf C\mathcal A')}V^{\rm bg})\).
SA 7481 says it “changes only the variables on the pivot bonds”.
SA 8278–8299 says “Only the pivot values are changed” and proves uniqueness for \(\Psi_V\).
Thus their physical free coordinate is exactly \(u=g_jy\), before the strip substitution.
There is no orthogonal change of basis to choose.
This identifies the source's two charts when their rows and gauges agree.
It does not identify charts of different determining systems without that agreement.

The conditional split is also specified.
CA-I 47937–47946 writes \(A_k=\varphi\oplus A'\). Our notation is \(y=\varphi\oplus e\), with blocks \(P,R,S\).
Its square in 47952–47957 gives the centered variable
\(b=\varphi+C_IR e\), so \(\varphi=b+Me\).
SA 17523–17528 then gives exactly (19) on this fixed free set.
The strip map is applied to the free values; the pivots follow from the constraint.
This agrees with Balaban CMP 119, text lines 329–344 and 452–499:
the free variables are fixed before the strip substitution and the conditional integral.
No Gaussian rotation or unspecified injection remains in this **one-read** formula.

**Two kinds of stage slot must remain distinct.**
SA 17528 stores \(V_j\) outside \(\Omega_{j+1}\), but stores a fluctuation form inside
\(\Omega_{j+1}\setminus\Lambda_{j+1}\).
The old level-\(j\) determining rows have neither endpoint in \(\Omega^-_{j+1}\), by SA 5615–5618.
Consequently a stored fluctuation bond lying in that interior is not an old level-\(j\) raw row.
The stage collar can include both types: CA-I 53758–53760, 53806–53814 gives
\(Z_{j+1}=\Lambda_{j+1}^c\) and \(R_n=Z_{j+1}\setminus Z''_{j+1}\).
Its two integrals, CA-I 54294–54298, have the different displayed precisions
\(C^*\Delta^{(j)}_{\Lambda_{j+1}}C\) and \(C^*\Delta^{(j)}C\).
Thus identifying their names \((A_j,B_j)\) with \((b,e)\) in an arbitrary single block square is unjustified.
An earlier integrand must retain its stored slots as well as its background.
The raw-row calculation (12)–(15) covers the latter component.
It cannot encode an independent interior stored slot by changing a raw row that does not exist there.

**The anchor need not be coordinate zero.**
On a constant-one strip, (18) gives \(\mathcal L(0,h,1)=-h\).
If an earlier exterior field \(e_*\) remains stored, the interior center is \(g_jMe_*\).
Both assertions follow by substitution; neither is a smallness estimate.
For two readings in the same background chart the correct raw increment is
\[
 \Delta(u_1,u_0)=i^{-1}\Log\{e^{ia_V(u_1)}e^{-ia_V(u_0)}\}.       \tag{33}
\]
Equation (14) is its special case \(u_0=0\).
One must not use that special case for every earlier conditional read.
On a convex free-coordinate ball with \(\|a_V\|\le1/8\), (12) implies
\[
                  \|\Delta(u_1,u_0)\|_{Y,w}
                  \le8C_{L,w}\|u_1-u_0\|_{Y,w}.               \tag{34}
\]
To prove this, put \(u_s=u_0+s(u_1-u_0)\).
Differentiate the product in (33), then the logarithm, along this segment.
The exponential product stays within \(e^{1/4}-1<1/2\) of one.
The logarithm derivative costs at most two; the exponential factors cost at most two.
The bound in (12) and integration prove (34), with room in the stated constant.
Only double blocks that read \(u_1-u_0\) contribute.
This also explains why the global radial path does not describe every earlier coordinate path.

**A switch can be inserted without complexifying a real cutoff.**
For one stored bond set \(\theta_e=\vartheta(e^{ig_je})\), evaluated at real \(e\), and
\[
 \begin{split}
 \Gamma(P,e)&=\mathcal L(g_je,h(P),\theta_e)
                         -\mathcal L(0,h(P),\theta_0),\\
 u_E(P,e,\mu)&=\mathcal L(0,h(P),\theta_0)+\mu\Gamma(P,e),\\
 u_I(P,b,e,\mu)&=g_jb+g_jM(P)(\mu e).
 \end{split}                                                   \tag{35}
\]
Use a separate diagonal switch for each stored bond in the last line.
At \(\mu=1\), this is the actual fixed-read reconstruction (19).
At \(\mu=0\), it does not read \(e\); at \(e=0\), it does not read \(\mu\).
These are the two identities required at SA 6169–6170.
For fixed real \(e\), the formula is holomorphic in \(P,\mu,b\) on its logarithm domain.
It is Borel in \(e\). No cutoff is evaluated at a complex field.

Use the \(1/4\)-ball of (20) for the whole real segment.
Suppose the cutoff has \(\|D_v\vartheta(e^{iv})\|\le C_\vartheta/\delta\),
and \(\|h\|\le\delta\), as in section 7.
Integrate (20) along the real segment from zero to \(g_je\). This gives
\[
 \|\Gamma(P,e)\|\le4g_j(1+C_\vartheta\|h\|/\delta)\|e\|.
\]
Hence on \(|\mu|<\lambda\), the increment from the same zero-slot anchor obeys
\[
 \|u-u(P,0,0,\mu)\|_{Y,w}
 \le g_j\|b\|_{Y,w}
 +g_j\lambda\{\|M\|_w+4(1+C_\vartheta)\}\|e\|_{Y,w}.          \tag{36}
\]
There is no collar-volume factor.
This extends the coordinate expression with the required switch identities.
It admits the primitive chart only if the zero-slot anchor plus the bound (36) stays within (12).
It does not replace an earlier assigned switch extension by fiat.
The required stage match must identify the actual extension, or prove that this choice preserves its full construction.

## 11. Moving coefficients: cancellation and a usable weighted estimate

The large individual terms in (27) cancel at zero response.
Write \(v_\lambda=\lambda-\lambda_0\), \(F_0=F'_p(0)\), and \(L_h=R_hK_h^{\mathsf T}-K_0^{\mathsf T}\).
Subtract the anchor equation from (26). The result is
\[
 \begin{split}
 Nv_\lambda&=H_p^{\mathsf T}\{F'_p(h)-F_0\}-T^{\mathsf T}\lambda_0,\\
 j&=L_h\lambda_0+R_hK_h^{\mathsf T}v_\lambda .
 \end{split}                                                   \tag{37}
\]
Every term on the right vanishes at \(h=0\), for every allowed independent pair.
Thus \(D_pj(p,0)=0\). This follows by differentiating an identity on the pair domain.
It does not follow by identifying \(\mathbf J\) with the physical current.
The operators can depend on \(\mathbf J\); the contrary sentence at `wf-room-2.md:299` is not used.

Here is the precise local hypothesis under which this cancellation gives a weighted bound.
It states the extra information needed beyond an unweighted Cauchy estimate.
Use normalized cell variables, with SA 11892–11945's “actual fine, coarse and pillar pairings”.
For a pair tangent \(v=(v_U,v_J)\), fix the norm
\[
 \|v\|_{\mathcal P,w}=\sup_x w(x)
       \max\{\xi_x|v_U|,\xi_x^2|\nabla_{\mathbf U}v_U|,\xi_x^3|v_J|\}.
\]
The norm and difference operator are frozen at the point of differentiation.
Let \(T(p)=\sum_\omega T_\omega(p)\), and let \(C_\omega\) be the full set read by its term.
Assume each term is holomorphic on a pair ball of radius \(0<\rho\le1\) about the point in question.
Its local ball must admit the restriction of each pair tangent, measured in the displayed norm.
Its read set includes every bond used by those local differences.
Suppose its kernel has a majorant \(A_\omega(x,y)\) there, with
\[
 \sup_x\sum_{\omega,y}A_\omega(x,y)
       e^{\theta\sup_{z\in C_\omega}d(x,z)}\le B_T.             \tag{38}
\]
Use the corresponding column bound when a transpose is needed.
The sum includes the cell weights. Empty read sets have zero derivative.

For every weight of rate at most \(\theta\), scalar Cauchy's formula proves
\[
       \|D_pT(p)[v]z\|_w
       \le {B_T\over\rho}\|v\|_{\mathcal P,w}\|z\|.            \tag{39}
\]
Indeed, a term reads at most \(\sup_{C_\omega}|v|\) of the direction.
Its scalar Cauchy radius is \(\rho/\sup_{C_\omega}|v|\).
Also \(w(x)/w(z')\le e^{\theta d(x,z')}\) for \(z'\in C_\omega\).
Multiply the Cauchy bound by \(w(x)\), sum its kernel against the input, and apply (38).
Absolute summability justifies termwise differentiation on a smaller ball.
This proves (39) by hand. The weight is on the moving pair, not on the old stored field.

The source has a place for these hypotheses.
`o1-decoupled.md:105–116` assigns the full walk read sets and the parameter monomials.
`pw-bridge.md:314–337` retains its four named inputs and gives the tree majorants (6.2).
Those majorants can pay the exponential in (38) if the assigned carrier diameter is charged to that tree.
This observation is conditional: a bound for a kernel alone does not supply the pair ball or its read set.
It also does not identify two different stage systems.

For example, (39) gives the missing coefficient estimate for a **matched conditional form**.
Assume \(\|C_I\|_w\le B_C\), \(\|M\|\le B_M\), and apply (39) to the blocks of \(Q\).
Differentiating \(PM=-R\), then multiplying by \(C_I\), gives
\[
 g_j\|D_pM[v]e\|_{Y,w}
 \le {g_jB_CB_Q(1+B_M)\over\rho}
                  \|v\|_{\mathcal P,w}\|e\|_Y.                \tag{40}
\]
Switching \(e\) costs at most \(\lambda_j^{\rm st}\).
This controls the term \(g_j\dot M e\) of (21), including an exterior field with no collar support.
The formula uses the actual block projections. It is not a spectral-gap-only argument.

The same mechanism makes the reduced forcing small in the old datum.
Assume (39) for \(H_1,G,H\), and its local multilinear versions for \(W,\mathcal C\).
In particular assume
\(\|\partial_pW(a)[v]\|_{F,w}\le C\rho^{-1}\|a\|_X^2\|v\|_{\mathcal P,w}\),
and the corresponding quadratic bound for \(\partial_p\mathcal C(h)[v]\).
These powers are required: `nl-r9.md:332–335` gives \(W(0)=DW(0)=0\) for [RED], at fixed pair.
When its coefficient balls and carrier majorants are uniform, Cauchy differentiation preserves those zero coefficients.
Use the small response ball \(\|b\|_Y\le1\) and \(\|a\|_X+\|h\|_X\le C\|b\|_Y\) in (24).
One obtains
\[
 \|F_1\|_{X,w}+\|F_2\|_{X,w}
 \le C\left\{\|\dot b\|_{Y,w}
              +{\|b\|_Y\over\rho}\|\dot p\|_{\mathcal P,w}\right\}. \tag{41}
\]
Each operator derivative multiplies \(b\), \(W(a)=O(a^2)\), or \(\mathcal C(h)=O(h^2)\).
The explicit derivatives of the two nonlinearities are quadratic by the stated hypothesis.
These are all five moving-coefficient terms in (24).
For \(q,q_C\le1/2\), (25) gives the same bound for \(\|\dot h\|_{X,w}\).

For the assigned current, use (37) in its integrated-by-parts form (6.2) of `wf-room-2.md:310–335`.
Its anchor is \(\lambda_0=(D^{\rm lat}H_p)^{\mathsf T}\mathcal F(p)\).
Here \(D^{\rm lat}\) is the covariant plaquette derivative, not a derivative in the parameter \(p\).
Then
\[
 \dot\lambda_0=
  \{\dot D^{\rm lat}H_p+D^{\rm lat}\dot H_p\}^{\mathsf T}\mathcal F
       +(D^{\rm lat}H_p)^{\mathsf T}\dot{\mathcal F}.             \tag{42}
\]
The plaquette variation \(\dot{\mathcal F}\) uses one covariant difference of the moving potential.
No second difference of that potential occurs in (42).
For completeness, differentiating (37) gives every remaining term:
\[
 \begin{split}
 N\dot v_\lambda={}&\dot H_p^{\mathsf T}(F'_p(h)-F_0)
 +H_p^{\mathsf T}\big[F''_p(h)\dot h
       +(\partial_pF'_p(h)-\partial_pF'_p(0))\dot p\big]\\
 &-\dot T^{\mathsf T}(\lambda_0+v_\lambda)-T^{\mathsf T}\dot\lambda_0,\\
 \dot j={}&\dot L_h\lambda_0+L_h\dot\lambda_0
       +\partial_t(R_hK_h^{\mathsf T})v_\lambda+R_hK_h^{\mathsf T}\dot v_\lambda .
 \end{split}
\]
In the first line, move the plaquette derivative onto \(H_p\) or \(\dot H_p\) before estimating.
For example, \(\dot H_p^{\mathsf T}(D^{\rm lat})^{\mathsf T}D^{\rm lat}h
=(D^{\rm lat}\dot H_p)^{\mathsf T}D^{\rm lat}h\).
The base derivative of this quadratic term differentiates one covariant difference at a time.
Each such change is multiplication by the moving potential, paired with a first difference of \(h\) or \(H_p\).
Apply the column version of (39), the local row bounds, and the stated Wilson remainder bounds.
In the first line of (37), a coefficient derivative multiplies \(h\), \(h^2\), or \(T=O(h)\).
In its second line, \(L_0=0\), so a base derivative of \(L_h\) also carries \(h\).
The derivative of \(N^{-1}\) is \(-N^{-1}\dot N N^{-1}\), with both inverses bounded by two.
Product differentiation therefore gives
\[
 \|\dot j\|_{F,w}
 \le C\left\{\|\dot h\|_{X,w}
              +{\|h\|_X\over\rho}\|\dot p\|_{\mathcal P,w}\right\}. \tag{43}
\]
Here the local bounds include their base derivatives on the same balls; this is a stated hypothesis of this implication.
For the complete current add \(\dot{\mathbf J}\), as in (27).
Thus the independent-current anchor does not create an unsuppressed extra force.
Equations (40)–(43) are uniform over parameters only when (38) and the pair balls are uniform there.

## 12. What a return estimate must retain

A large fixed unitary return is harmless. A changing node value is not removed by axial recursion.
This can be seen without estimating any field equation.
Let a fixed return path have factors \(T_1(t),\ldots,T_m(t)\) and initial node factor \(g_*(t)\).
Fixed unitary factors between them can be included without changing the following proof.
Set \(g(t)=g_*(t)T_1(t)\cdots T_m(t)\), and let \(G_i=g_*T_1\cdots T_i\).
Product differentiation gives the exact identity
\[
 \dot g g^{-1}=\dot g_*g_*^{-1}
       +\sum_{i=1}^m\operatorname{Ad}_{G_{i-1}}
                                      (\dot T_iT_i^{-1}).       \tag{44}
\]
Thus if every prefix has condition number at most \(K_*\), then
\[
 \|\dot g g^{-1}\|
 \le\|\dot g_*g_*^{-1}\|+K_*\sum_i\|\dot T_iT_i^{-1}\|.        \tag{45}
\]
This is also a weighted estimate when the path lies in a set of bounded weighted diameter.

For a single-layer pillar, suppose its level-\(q\) factors and inverse factors have norms at most
\(e^{cL^{q-j}a}\), and tangents at most \(cL^{q-j}v\).
These are explicit hypotheses on the actual factors.
Since \(\sum_{q\le j}L^{q-j}\le(1-L^{-1})^{-1}\), multiplication bounds every prefix by
\(\operatorname{cond}(g_*)e^{2ca/(1-L^{-1})}\).
Equations (44)–(45) then bound the non-node contribution by a constant times \(v\), with no depth factor.
`o1-decoupled.md:328–332` gives these factors for its physical inner Landau map.
Its proof uses the actual iterated averages, including bonds that are not determining rows.
That is a useful supplied case, not a proof for all stage returns.

The remaining node term is prescribed, rather than free to set to zero.
SA 9700–9702 fixes the physical return by \(u_Bv_j[\mathcal H(B)]=1\) at the tops.
SA 5800–5803 states recovery at \(s=1\) and real data, “up to the recorded node gauge factor”.
SA 17923 requires the argument, gauge and stored data to be formed together.
Therefore (45) cannot be applied to an arbitrary complex stage return by dropping \(\dot g_*g_*^{-1}\).
Equation (29) then gives exact field and current transport.
Its current commutator costs at most \(2\|\dot g g^{-1}\|\|J^g\|\) pointwise.
A field estimate in physical units needs more than a pointwise gauge-tangent bound.
It needs the covariant difference of that tangent divided by the mesh, and its first difference.
Attack A in section 18 writes this requirement and refutes the pointwise shortcut.

The seam exponent also stays assigned throughout this calculation.
It is not part of the return gauge and is not zeroed by a node choice.
SA 7601 retains “constant and linear terms”; SA 7866 retains “fluctuation variations”.
If its interior linear term is absorbed in the Gaussian instead, (19) changes by \(g_jC_I\ell_{\partial,I}\)
when \(\ell_{\partial,I}\) is written in the Gaussian coordinate convention of (17).
Its derivative then includes \(g_j\dot C_I\ell_{\partial,I}+g_jC_I\dot\ell_{\partial,I}\).
Leaving that term in the exponent, as this note does, avoids this recentering; it does not estimate the exponent.

## 13. The stage match: three further attacks and the precise stopping point

The assertion still under attack is Lemma M in section 9, with its corrected conditional-coordinate paths.
In particular, it asserts a match to the actual stage, not just existence of a convenient substitute.
Its quantifiers include every earlier parameter and every allowed switch value.
The following attacks use the new calculations rather than the former arbitrary-basis objection.

**First attack: reconstruct the actual two types of stage slot.**
For the newly integrated raw rows, the direct candidate is
\[
 u^{\rm raw}_t=tg_jB^{\rm raw},\qquad
 D_t=D(u^{\rm raw}_t),\qquad
 (\mathbf U_t,\mathbf J_t)
   =\big(e^{i\eta h_t}\mathbf U,\ \mathbf J+j_t\big),            \tag{46}
\]
where (23) reads the reduced datum of \(D_tD_0^{-1}\), and (26) fixes \(j_t\).
On the physical locus, (12)–(15) verify all surviving and added constraints.
SA 10446–10458 starts “At $s=1$ over a critical real background” and identifies that field with the background response.
The separate stage slots formerly stored inside \(\Omega^-_{j+1}\) are then inserted into their old integrands.
For each old conditional integral, (19), (32) and (33) specify the coordinate in its own frame.
Its center, strip correction and nonzero anchor are all retained.

This gets further than simply setting \(u=g_j(A_j+B_j)\).
But it does not finish the match in CA-I 54287.
The failed step is identifying, for each earlier read, its actual interior/exterior projections and node return
after the prepared collar changes the determining member.
The sets \(I=\mathbb B^*\) and \(I=\mathbb B^{K1}\), for example, differ by \(\mathfrak x\), not just notation.
Changing this set changes the conditional problem and its exterior read.
Equation (31) compares means only after their spaces have been identified; it does not supply those identifications.
Likewise the old stored slot is not a row of (46), as the disjointness argument in section 10 proves.
I have not proved that the full substitution obtained from these local candidates is the prescribed stage read
on all earlier discs. Thus (46) is a matched physical raw-row construction, not the complete stage substitution.

**Second attack: use one complete Gaussian to identify every conditional coordinate.**
This was a sufficient route, not a condition imposed by the carriage rule.
Section 14 removes the common-form requirement for a carried Gaussian factor.
This route can remove the projection ambiguity when all reads come from one fixed form.
Split its free coordinates into disjoint sets \(I,C,E\), and write
\[
 Q=\begin{pmatrix}P&R&U\\R^{\mathsf T}&B&V\\U^{\mathsf T}&V^{\mathsf T}&S\end{pmatrix},
 \quad \bar B=B-R^{\mathsf T}P^{-1}R,
 \quad \bar V=V-R^{\mathsf T}P^{-1}U .
\]
Assume \(P\) and \(\bar B\) invertible.
Complete the \(I\)-square, then the \(C\)-square, using (17).
The exact inverse coordinate change is
\[
 \begin{split}
 y_E&=e,\qquad y_C=c-\bar B^{-1}\bar V e,\\
 y_I&=b-P^{-1}Rc-P^{-1}(U-R\bar B^{-1}\bar V)e .
 \end{split}                                                   \tag{47}
\]
For verification, substitute the second line into
\(y_I+P^{-1}(Ry_C+Ue)=b\), and the first into
\(y_C+\bar B^{-1}\bar Ve=c\).
Both identities reduce to cancellation of equal terms.
Thus the centered variables are related by a definite triangular map, including their exterior mean.
This is stronger than an equality of quadratic forms.
Equation (40) bounds its moving coefficients whenever its actual full-form inputs satisfy (38).

The failed step is applying (47) to the forms actually kept by the history.
SA 17550–17558 defines a chain selection and calls the kept form “not a Schur complement but a truncated series”.
SA 17558–17564 evaluates that fixed pair function at different backgrounds before and after a stage.
The identity for one \(Q\) therefore does not identify those two evaluations with two eliminations of that \(Q\).
Once their spaces are identified, their center difference is (31), with the actual projections and transports included.
It has not been proved to vanish or to obey the stage budget.
Neither completion of squares nor associativity bounds the changed row, current and seam coefficients in this expression.
The needed identification and uniform local derivative bounds for those transported coefficients remain unproved.
No failure of positivity or of the actual stage is inferred from this obstruction.

**Third attack: bypass a common Gaussian through the complete differential equations.**
The physical saddle route would give (9). For an independently decoupled read it instead leaves the exact defect (28).
Thus I used (24), retained every coefficient derivative, and canceled the current anchor by (37).
Equations (40)–(43) now give the desired forcing estimates on a matched set of local coefficient balls.
Equation (45) treats the non-node part of a matched return.
This removes an algebraic problem; it does not supply those balls or that matching for the actual earlier read.

I also tried to obtain the needed localization from bounded holomorphy and ordinary kernel decay alone.
Here is an exact failure of that inference.
Let sites \(0,N\) have distance \(N\). On \(\|p\|_\infty<\rho\), define
\[
        (T_N(p)z)(0)=(p(N)/\rho)z(0),\qquad
        (T_N(p)z)(x)=0\quad(x\ne0).                            \tag{48}
\]
Its operator norm is at most one. Its input-output kernel is diagonal, so it has perfect input-output locality.
But take \(v(N)=1\), zero elsewhere, \(z(0)=1\), and \(w(x)=e^{\theta d(x,N)}\).
Then \(\|v\|_w=\|z\|=1\), whereas
\(\|D_pT_N[v]z\|_w=e^{\theta N}/\rho\).
This is checked by one substitution. It is not an example of a Yang–Mills operator.
It proves why the full read sets in (38), including the transport of their pair variables, are necessary.
They cannot be replaced by an operator norm and input-output decay.

The attempted repair uses the full walk hulls of `o1-decoupled.md:105–116`.
When (38) holds on common local balls, (39) gives exactly the missing kind of derivative estimate.
For the stage comparison, however, the hypothesis must hold after its slot and node transport.
`o1-decoupled.md:173–184,188–197` requires common enlarged regions, a specified common expansion,
and separate pair and node comparisons before making such a comparison.
The first and second attacks above have not established those premises for this prepared-stage read.
Nor does the physical identity determine them off the physical current graph, by (28) and SA 11798–11805.
This is the exact failed step of the differential route.

**Remaining lemma, in the form needed for the next calculation.**
Lemma M asserts the following one uniform compatibility statement.
For every admitted single-layer stage \(0\to1\), every \(P\in D_1^{\rm int}\),
and every earlier parameter and switch value, the actual stage substitution has the fixed-read normal form
(19), (23), (26), (29), with the source's free bond projections and assigned returns.
Its initial conditional coordinates are retained, as in (33), rather than reset to zero.
On the entire stage path the transported coefficient maps have common neighborhoods and full read-set majorants
sufficient for (38)–(43); their node factors obey the corresponding weighted bound in (45).
After the source's unit conversions, their complete returned derivatives obey (30), and the no-new-mark
reads spend less than \(g_k(m)r_a/(4N)\).
The primitive, Gaussian, intrinsic-tube and stored-slot domains retain strict continuation room.
All constants are independent of the earlier history length, mesh and volume.
This is a precise assertion about the assigned stage map. The three attacks have not proved it.

The direct coordinate attack fails at the actual slot and return identification.
The complete-square attack fails at the common-form identification.
The differential attack fails at the transported read sets and uniform neighborhoods needed for its weighted estimate.
These are three routes to the same compatibility statement, not three counterexamples to the stage.

## 14. Carriage does not require a common Gaussian

This continuation uses the same checkout and source pin as the preceding sections.
The source files were fetched once in this session.
Their SHA-256 values are `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` (SA)
and `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` (CA-I).
The original note and numbered source excerpts are in `/tmp/shift-map-cont-20261104-r3/`.
The requested workflow file `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this checkout.
This continuation follows the task and the supplied research instructions; it invokes no audit or status process.

The index entries used next are SA chunks 05, 07, 10, 11 and 16;
CA-I chunks 03–05 and 10; and the matching entries of `sa-index/obligations.md`.
They led to the source passages quoted below.
Credit for the source constructions remains with Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text, and with Balaban for the cited method.

SA 17508 says unused variables are “carried along unchanged”.
SA 17558 says the carried forms are “constructed once and for all”.
SA 17561 displays their difference at the same \(A'\):
\[
 -\tfrac12\langle A',
       [\Delta^{\rm loc}_{\mathfrak k}(U^\sharp)
        -\Delta^{\rm loc}_{\mathfrak k}(U^\flat)]A'\rangle .
\]
SA 17564 specifies that both backgrounds are “written in the new variables”.
These lines assign a fixed coordinate read and a changing coefficient.
They do not require redoing the old conditional integral at every stage.

Here is its exact algebra, including the return.
Fix one carried factor and its recorded real coordinate \(a\).
Write \(D_t=\operatorname{Ad}(r_t^{-1})\) for the map from recorded coordinates to its native coordinates.
The symbol \(D_t\) in this section is a coordinate transport, not the determining datum of (4).
Let \(K_t\) be its symmetric kept precision in those native coordinates. Put
\[
 \widehat K_t=D_t^{\mathsf T}K_tD_t,\qquad
 Q_t(a)=\tfrac12\langle a,\widehat K_ta\rangle .
 \tag{49}
\]
Transposes use the fixed bilinear trace pairing and its cell weights.
No unitarity is assumed for \(r_t\).
With the coordinate, tests and measure fixed, the integrand identity is
\[
 e^{-Q_1(a)+B_1(a)}
 =e^{-Q_0(a)+B_1(a)-[Q_1(a)-Q_0(a)]}.
 \tag{50}
\]
It follows by adding the two exponents.
It needs neither a Schur-complement identity nor a change of integration variables.
Any seam constant, linear term and strip Jacobian stays in \(B_1\).
SA 7601 explicitly retains seam “constant and linear terms”.
SA 17541 includes “the Jacobians together with the differences” in the boundary interpolation.
Equation (50) implements that assignment for the quadratic factor.
It does not estimate \(B_1\) or its difference.

For completeness, consider an earlier integral before its interior variable was integrated out.
Its recorded free-bond split is the one in CA-I 45283–45292: “pivot bonds are removed”.
In (51)–(52), pull the blocks to this recorded frame first.
Do not combine native blocks with a coordinate held fixed in another frame.
CA-I 47937–47959 gives, in our notation,
\[
 \tfrac12\langle\varphi,P_t\varphi\rangle+
 \langle\varphi,R_te\rangle+\tfrac12\langle e,S_te\rangle
 =\tfrac12\langle\varphi-M_te,P_t(\varphi-M_te)\rangle
   +\tfrac12\langle e,(S_t-R_t^{\mathsf T}P_t^{-1}R_t)e\rangle,
 \quad M_t=-P_t^{-1}R_t.
 \tag{51}
\]
Suppose its uncentered recorded coordinates \((\varphi,e)\) stay fixed.
Its centered coordinate is then \(b_t=\varphi-M_te\), so
\[
 \dot b_t=-\dot M_te,\qquad
 \partial_t\{g_j(b_t+M_te)\}=0.
 \tag{52}
\]
Thus the two mean derivatives cancel in the reconstruction of that same coordinate.
If instead \(b_t\) is held fixed, the physical coordinate changes by \(g_j\dot M_te\).
These are different paths. Equation (21) is correct for the latter choice.
It is not a compulsory extra field shift for every carried factor.
CA-I 47964–47967 identifies the conditional integral for each specified interior bond set.
Neither set has to be substituted for the other during carriage.

Once the old interior integration has been performed, \(b_t\) is no longer an integration slot.
One carries its resulting function and its exterior coordinate, using (49)–(50).
This removes the common-Gaussian obstacle in the second attacks of sections 9 and 13.
It does not identify the two new integrals in CA-I 54294–54298 with one another.
Their displayed forms remain
\(C^*\Delta^{(j)}_{\Lambda_{j+1}}C\) and \(C^*\Delta^{(j)}C\).

The return derivative in (49) is also explicit.
Set \(\sigma_t=r_t^{-1}\dot r_t\) and \(B_t=\operatorname{ad}\sigma_t\) on the native bond forms.
Then \(\dot D_t=-B_tD_t\).
Trace invariance gives \(B_t^{\mathsf T}=-B_t\):
\(\operatorname{tr}([\sigma,x]y)=-\operatorname{tr}(x[\sigma,y])\).
Hence
\[
 \dot{\widehat K}_t
 =D_t^{\mathsf T}\{\dot K_t+[B_t,K_t]\}D_t.
 \tag{53}
\]
The term \([B_t,K_t]\) cannot be discarded.
For a covariant carried form, it cancels a change of native frame when that change is only a gauge change.
The relative-form hypothesis for this statement is retained in Attack A below.
It does not cancel a change of the physical pair.
This distinction will be used in section 18.

**Near slots.** No real stored coordinate needs complexification for (49)–(50).
SA 6166–6173 requires Borel dependence near tests and analytic dependence on the switches.
Let \(F(p,a,\mu)\) be the already assigned extension of one such factor.
For fixed \(p,a\), the path \(\mu=t\), \(0\le t\le1\), runs from its zero-field read to its actual read.
The two switch identities give these endpoints exactly.
If \(|F|\le B_F\) on \(|\mu|<\lambda\), Cauchy's formula gives
\[
 |\partial_\mu F(p,a,t)|\le {B_F\over\lambda-1},\qquad
 |F(p,a,1)-F(p,a,0)|\le {B_F\over\lambda-1}.
 \tag{54}
\]
Use circles of radius less than \(\lambda-|t|\), then take their limiting radii.
This argument holds uniformly in other parameters wherever the same supremum bound holds.
It uses the assigned extension; it does not replace it with (35).
For a group of newly integrated slots, set all their switches to the same scalar \(t\).
The resulting function is analytic on \(|t|<\min_b\lambda_b\).
Apply the same one-variable proof. There is no factor counting the slots in the group.
This comparison has endpoint switches equal to one.
It does not assert the same small gain at arbitrary switch values near their disc boundaries.
SA 17946–17947 prescribes field-zero evaluation after integration and removal of the switch.
Equation (54) explains that step without a path through complex near fields.
For a moving pair one must still add \(D_pF\dot p\).

## 15. Native local balls and the mean derivative

The local coefficient balls in section 11 have a source construction.
They are not supplied by an operator norm alone.
CA-I 46800–46931 proves the local-ball lemma at cutoff distance \(M/(2L)\).
Its hypotheses include a globally given real \(U\in\mathcal U_{\mathbb R}\), an admitted nest,
the stated coefficient expansion, and the local weighted first-order norm.
It uses
\[
 \chi(x)=\max\{0,1-(2L/M)\tau(\{x\},[\nu])\}.
\]
The geometric part puts its support in the one-cube collar.
The analytic part proves
\[
 \|(\chi A',\chi J)\|_\star
 \le (1+2L/M)\|(A',J)\|_{\star,[\nu]^\approx},\qquad M>2L.
 \tag{55}
\]
The source's words at CA-I 46925–46931 are “linear” and “analytic on the local ball”.
This is a detailed conditional proof. We use it as a cited input, with its hypotheses.
We do not assert its real-background or nest hypotheses for a newly transported read.

There is a definite margin for a native read.
CA-I 45500–45507 requires
\[
 (\alpha_1,\alpha_0^J)\le
       \tfrac14\varepsilon_1(a_1^\oplus,a_0^\oplus),
 \qquad U\in\mathcal U_{\mathbb R}.
\]
Use its normalized coordinates and set \(r=\varepsilon_1\).
In (56)–(59), \(\mathcal P\) denotes this frozen native coordinate norm.
Conversion to a left logarithmic field velocity also costs the norm of the local coordinate derivative.
The displayed factor \(4/r\) is before that conversion, which must be admitted separately after a return.
At a point of local norm at most \(r/4\), a perturbation of local norm less than \(r/4\)
stays in the local \(r/2\)-ball.
Equation (55) admits this whole ball to the coefficient's global \(r\)-domain.
In particular, if a term has a uniform normalized kernel majorant \(A_\nu(x,y)\) there, then
\[
 |D T_\nu(p)[v](x,y)|
 \le {4\over r} A_\nu(x,y)
                    \|v\|_{\mathcal P,[\nu]^\approx}.
 \tag{56}
\]
Proof: apply scalar Cauchy to
\(z\mapsto T_\nu(p+zv)(x,y)\) on radius
\(r/(4\|v\|_{\mathcal P,[\nu]^\approx})\).
The assertion at a zero direction follows by linearity.
All coordinates and the real factor are fixed during this differentiation.
This proves a derivative estimate at every quarter-ball point, not just at zero.

To pass to a spatial weight, the enlarged read set must still be counted.
Suppose the actual normalized majorants satisfy
\[
 \sup_x\sum_{\nu,y} A_\nu(x,y)
       \exp\{\theta\sup_{z\in[\nu]^\approx}d(x,z)\}\le B_* .
 \tag{57}
\]
For \(w(x)/w(z)\le e^{\theta d(x,z)}\), (56) and this sum give
\[
 \|D T(p)[v]z\|_w
 \le {4B_*\over r}\|v\|_{\mathcal P,w}\|z\|.
 \tag{58}
\]
Indeed, multiply (56) by \(w(x)\), bound the local direction by
\(\|v\|_{\mathcal P,w}\sup_{[\nu]^\approx}w^{-1}\), and sum.
Absolute convergence permits differentiation term by term on every smaller ball.
This proves (58) from the source's native balls and the full-carrier moment (57).

Here is how a walk bound can pay that moment.
For a walk of length \(n\), let \(\ell(\omega;x,y)\) be a path length joining its input,
output and all its carriers.
If every enlarged read lies within distance \(R_*\) of such a path, then
\[
 \sup_{z\in C_\omega}d(x,z)\le\ell(\omega;x,y)+R_* .
\]
Consequently a majorant \(a_\omega e^{-\tau\ell(\omega;x,y)}\) loses at most
\(e^{\theta R_*}\), and retains rate \(\tau-\theta\).
This is a pointwise inequality before summation.
`o1-decoupled.md:105–116` specifies full walk read sets;
its lines 205–208 use a local complex path with radius proportional to the inverse local perturbation.
CA-I 46158–46168 explicitly reads distances on the “enlarged domain lists”.
Thus native walks have a stated way to supply (57).
An input-output decay bound without these read sets still does not suffice, by (48).
We have not replaced the walk premises of those results with a new unconditional theorem.

For a fixed native conditional split, apply this estimate to its blocks \(P,R\).
Suppose \(\|P^{-1}\|_w\le B_C\), \(\|M\|\le B_M\), and their native majorants meet (57)
with constant \(B_Q\).
Differentiate \(PM=-R\). The exact equation and estimate are
\[
 P\dot M=-\dot R-\dot PM,\qquad
 g_j\|\dot M e\|_w
 \le {4g_j B_C B_Q(1+B_M)\over r}
                         \|\dot p\|_{\mathcal P,w}\|e\|.
 \tag{59}
\]
This proves (40) with a definite native radius \(r/4\).
If exterior coordinates carry diagonal switches of modulus at most \(\lambda\), replace \(\|e\|\) by \(\lambda\|e\|\).
No number of exterior bonds appears.
If \(\dot p\) is localized at the collar in the weighted norm, so is this mean derivative.
It can have a nonzero tail. Finite support is not asserted for \(P^{-1}\).

The proof applies to a fixed carried coefficient map because that map is formed once.
It needs no comparison between two separately chosen walk expansions.
For the returned coefficient in (49), however, (53) adds its return term.
The native local-ball lemma does not place \(p^{r_t}\) in a quarter ball.
That is the precise scope left after this improvement.

## 16. The chart derivative when its reference also moves

Equation (33) uses one fixed background chart.
A complete earlier read can move that chart too.
We now compute the additional term rather than including it in an unspecified constant.

Let \(V=V(z)\) be an admitted local background chart for the finite block average.
The coordinates \(z\) include all its carrier data, with its real gauge fixed.
SA 8257–8299 supplies the unique pivot graph, with
\(a_{V(z)}(u)|_F=u\) and \(q_{V(z)}(a_{V(z)}(u))=0\).
Write \(\iota_P\) for the pivot injection and \(\iota_F\) for the free injection.
Let
\[
 J_{z,a}=D_aq_{V(z)}(a)\iota_P .
\]
This pivot block is invertible on the smaller chart used for (12).
SA 8276–8281 gives it by “inverting \(1+DR_Vh_V\)” and supplies the explicit inverse of the graph map.
Differentiating the constraint and the free-value identity gives exactly
\[
 \dot a=\iota_F\dot u-
 \iota_PJ_{z,a}^{-1}
       \{D_aq_{V(z)}(a)\iota_F\dot u+D_zq_{V(z)}(a)\dot z\}.
 \tag{60}
\]
The last term is the moving-reference term.
Since \(q_{V(z)}(0)=0\) for every \(z\), it vanishes at \(a=0\).
This is an identity of the exact group average, not an identity for a linearized substitute.

There is a useful bound with explicit room.
Suppose the background coordinates have a complex ball of radius \(r_z\) on the full carrier.
Assume the free-coordinate derivative bound of (12) holds throughout that ball.
At its concentric half-ball, apply Cauchy's formula to
\(D_ua_{V(z)}(u)[v]\) in a background direction.
It gives
\[
 \|D_zD_ua_{V(z)}(u)[\dot z,v]\|_w
 \le {2C_{L,w}\over r_z}\|\dot z\|_{\rm loc}\|v\|_w.
\]
Integrate along \(su\), using \(a_{V(z)}(0)=0\). Thus
\[
 \|\dot a\|_w\le C_{L,w}\|\dot u\|_w
       +{2C_{L,w}\over r_z}\|u\|_w\|\dot z\|_{\rm loc}.
 \tag{61}
\]
The local norm reads the same double block as the pivot.
For different weights on the two inputs, charge the maximum weight ratio on that double block.
This changes the finite constant, not the number of collar bonds.
The ball in this statement is a hypothesis about the actual background chart.
The finite graph theorem supplies the estimate once that chart is admitted.

Let \(D_t^0\) now denote the reference raw datum and let
\(D_t^{\rm old}=e^{ia_{V_t}(u_t)}D_t^0\) on the affected rows.
Put \(\kappa_t^0=\dot D_t^0(D_t^0)^{-1}\).
Product differentiation gives
\[
 \dot D_t^{\rm old}(D_t^{\rm old})^{-1}
 =i\int_0^1 e^{isa_t}\dot a_t e^{-isa_t}\,ds
             +\operatorname{Ad}(e^{ia_t})\kappa_t^0 .
 \tag{62}
\]
The raw comparison to the initial reading is therefore
\[
 \Delta_t={1\over i}\Log\!\left\{
 e^{ia_{V_t}(u_t)}D_t^0(D_0^0)^{-1}e^{-ia_{V_0}(u_0)}\right\}.
 \tag{63}
\]
This is the complete version of (33) when the reference moves.
For a fixed reference and \(u_0=0\), it reduces to (14).
For a fixed reference and nonzero \(u_0\), it reduces to (33).
On the same \(1/2\)-logarithm ball as before, (6), (61) and (62) bound its derivative.
In particular, the term \(\kappa_t^0\) must be bounded; it does not carry a factor \(u_t\).

For an uncentered stored read held fixed, (52) removes the fictitious mean-motion term in \(\dot u\).
For a centered slot actually held fixed, (59) supplies that term instead.
On a strip bond, retain all three terms in (20), with its real cutoff kept in the assigned switch representation.
For the pair response use (24), the assigned current (26)–(27), and the return (29).
For its carried quadratic factor use (53), including the commutator.
These formulas specify where each derivative enters.
They do not turn a small native fluctuation into a bound for \(\kappa_t^0\) after an earlier composition.

## 17. A scale contraction can control a long earlier composition

There is a stronger possible route than the product bound in `d4-incr.md` (6).
That bound treats every unit change as having norm at most one.
In unnormalized physical-coordinate norms a strict lowering of level has a contraction.

SA 5738–5746 gives the exact unit change
\((A',J)\mapsto(L^{-m}A',L^{-3m}J)\).
The first covariant difference scales by \(L^{-2m}\), because its mesh also changes by \(L^m\).
Thus on the maximum of these three component norms a one-level change \(S\) satisfies
\(\|S\|\le L^{-1}\).
The two endpoint norms here are in their respective level units; they are not the weighted ambient norm of (38).

Consider a specified chain of maps in these units,
\[
 p_i=\mathcal F_i(p_{i+1}),\qquad \mathcal F_i=G_i\circ S,
 \qquad G_i(q)=q+R_i(q),\qquad
                    \|D R_i\|\le\epsilon_i .
 \tag{64}
\]
The coordinates in this formula are local pair coordinates, so addition is in a chart.
The chart conversion is included in \(R_i\).
The chain rule gives
\[
 \|D(\mathcal F_a\circ\cdots\circ\mathcal F_{b-1})\|
 \le L^{-(b-a)}\prod_{i=a}^{b-1}(1+\epsilon_i)
 \le (2/L)^{b-a}\quad\hbox{if }\epsilon_i\le1.
 \tag{65}
\]
The first inequality is just submultiplicativity at each link.
It does not require \(\sum_i\epsilon_i<\infty\).
Since \(L\ge5\), the last bound decays with the number of links.

Radius conversion must still be made.
For example, suppose the source and target radii satisfy
\(r_b/r_a\le C\sqrt{1+b-a}\), with their lifts already included.
For \(d=b-a\), the hand inequality \(\sqrt{1+d}\le2^d\) used in section 5 gives
\[
 {r_b\over r_a}(2/L)^d\le C(4/L)^d\le C.
 \tag{66}
\]
This is a sufficient uniform estimate for a strictly descending chain with those radii.
It is stronger than estimating every link by a constant greater than one in a common norm.
It is not yet an estimate for every chain in the stage history.

Equations (41)–(43), (59) and (61) can give \(\epsilon_i\le C\sigma_i/r_i^{\rm loc}\)
for a matched response with its datum and coefficients on fixed local balls.
They do so because a coefficient derivative multiplies the small response or datum.
They do not bound an assigned return term in (29), or the reference velocity in (62), by that quantity.
Also, a same-level return or conditional read has no factor \(L^{-1}\).
One must identify the actual chain before assigning a factor of \(S\) to any link.
SA 17923–17925 keeps stored data at their recorded sites; it does not give (64) for every returned read.

## 18. The remaining returned-pair lemma and three completed attacks

The new results remove two unnecessary obstacles: re-centering every carried Gaussian and demanding a common complete form.
They also supply native coefficient balls and the missing moving-chart derivative.
The first unresolved part of the stage match is now stated as one response lemma.
It is a necessary estimate for the route through (24), not a claim that the stage fails without this route.

**Lemma R — uniform response in the recorded frames (unproved).**
Fix an admissible finite history with one collar layer at stage \(0\to1\).
Let \(K^+\) be the enlarged raw collar carrier of sections 3 and 6.
For each earlier read \(\tau\), use its recorded geometry, free-bond projections, units,
return prescription, and assigned earlier parameters \(\zeta\).
Let \(\widehat p_{\tau,t}=(\widehat U_{\tau,t},\widehat J_{\tau,t})\)
be its actual pair read on the stage path, expressed in its recorded frame.
The lemma asserts a matched local representation of this path, starting at the retained zero-fluctuation read.
Its endpoint must be the old read expressed in the actual stage variables.
Retain every near real slot; use its assigned switch as in (54).
The field component follows the actual reconstruction (19), (60)–(63) where those coordinates are used.
The independent-current component is (26), with its additive baseline and its assigned return.

Let \(\sigma_j^{\rm sw}\) be the maximum size of the actual new free datum on all its switch discs,
measured in raw level-\(j\) units, including its strip correction.
There are constants \(C,\theta>0\), independent of history length, mesh and volume, such that
every one of these reads has the following bound before a possible first exit:
\[
 \left\|
 \left({1\over i\eta_\tau}\dot{\widehat U}_{\tau,t}
                   \widehat U_{\tau,t}^{-1},\quad
                \dot{\widehat J}_{\tau,t}\right)
 \right\|_{\mathcal P,w_\tau}
 \le C\sigma_j^{\rm sw},\qquad
 w_\tau(x)=e^{\theta d_{e_-}(x,K^+)} .
 \tag{67}
\]
All components in (67) are first converted to the old ambient units and the norm of section 11.
The statement includes the covariant first difference of the displayed potential velocity.
On the same path, each read remains on native local balls of the form used in (55)–(59),
after its specified return, with a fixed positive fraction of their radii left.
The constants are uniform in every earlier parameter and allowed switch.
These are part of this one local response assertion; they are not inferred from a bound on the seven scalar clauses.

The source does not supply (67) as a consequence of covariance.
SA 17908–17911 invokes “response and hereditary-domain estimates”.
CA-I 54337–54339 assigns the descending spaces and evaluation at the current background.
Those are the required domains, not a proof of this response bound.

**Attack A: transport the recorded frames by the gauge cocycle.**
The checked implication in `kept-cov.md` (13) is
\[
 r'_f h_f r_f^{-1}=d_g
\]
at each shared stored site.
`gates/kept-cov-check.md`, sections 2 and 4, retains the relative kept-form prescription,
native-orbit covariance, and domain admission as its hypotheses.
The latter is not dropped here.
This identity fixes the action at every shared coordinate under a bare gauge change.
It does not require two factors to use the same interior transport path.

Differentiate it along a differentiable gauge orbit, with the recorded coordinate frame fixed.
The corresponding native coefficient derivative in (53) is
\(\dot K=-[B,K]\); therefore \(\dot{\widehat K}=0\).
This proves exact cancellation of the pure gauge part, including the node contribution.
It also shows why a large fixed unitary return is harmless.
SA 7913's continuation of \(\mathsf n^{-1}\) by a bump protects former stored sites under the node correction.
It does not identify the non-gauge part of a stage change with such a correction.

For the actual stage, the endpoint pair can change curvature and independent current.
Then the leftover in (53) is \(\dot K+[B,K]\), and (29) has the returned physical velocity.
The cocycle provides an equality under gauge transformations, not a bound on either leftover.
In particular, differentiating the cocycle does not bound \(\kappa_t^0\) in (62).

The direct contour attempt gives a more precise failed estimate.
On a fixed pillar, (44) expresses the tangent as its initial node tangent plus a sum of transported link tangents.
The geometric scale sum in section 12 can bound that sum pointwise.
But write \(\rho=\dot r r^{-1}\) in the recorded frame and define the edge difference
\(\delta_{\widehat U}\rho(b)=\rho(b_-)-\operatorname{Ad}(\widehat U(b))\rho(b_+)\).
Equation (29), in physical units, reads
\[
 \widehat v(b)=\operatorname{Ad}(r(b_-))v(b)
                     +{1\over i\eta}\delta_{\widehat U}\rho(b),
 \qquad v={1\over i\eta}\dot U U^{-1}.
 \tag{67a}
\]
To control its first-order norm, the return must satisfy bounds for
\[
 \sup_x w(x)\left\{
  \xi_x\left|\eta^{-1}\delta_{\widehat U}\rho\right|
  +\xi_x^2\left|\nabla_{\widehat U}
                    (\eta^{-1}\delta_{\widehat U}\rho)\right|\right\}.
\]
There are also the product-rule terms from \(\operatorname{Ad}(r)v\).
The pointwise estimate (45) does not bound this expression across two different pillars or a seam.
It leaves the difference between their prescribed node tangents.

Here is an exact check of that distinction.
Take the input field \(U=1\), current zero, ambient scale \(\xi=1\), and three collinear mesh sites.
Use the matrix operator norm in this example, and \(0\le t\le1\).
Let \(s(x)\) have values \(1,-1,1\) at those sites and set
\[
 T=\operatorname{diag}(1,-1),\qquad
 r_t(x)=e^{t\epsilon s(x)T},\qquad 0<\epsilon<1/10.
 \tag{67b}
\]
Extend \(s\) by values of modulus at most one on the finite lattice.
These are determinant-one complex gauges. Their norms and inverse norms are at most \(e^\epsilon\).
Their tangents obey \(\|\rho\|_\infty\le\epsilon\).
The returned links on the two edges are \(e^{2t\epsilon T}\) and \(e^{-2t\epsilon T}\).
Equation (67a) gives velocity norm \(2\epsilon/\eta\) and first-difference norm \(4\epsilon/\eta^2\).
Both conclusions follow by subtracting the three displayed values of \(s\).
Every plaquette remains the identity, by cancellation of endpoint factors.

The large potential cannot be removed by choosing a different real splitting of that link.
Right multiplication by a unitary matrix leaves its norm \(e^{2t\epsilon}\) unchanged.
If that product equals \(e^{i\eta A'}\), the exponential series gives
\(e^{2t\epsilon}\le e^{\eta\|A'\|}\), hence \(\|A'\|\ge2t\epsilon/\eta\).
Thus a small pointwise complex return does not give a mesh-uniform potential bound.
SA 5732–5735 already says the core is “not saturated by complex gauge transformations”.
This example refutes a shortcut in this note, not the source's assigned stage return.

Attack A therefore proves the vertical cancellation of scalar carried coefficients,
but fails to bound the required covariant return differences in (67a).
Those differences, together with the remaining pair directions, are the exact failed step toward (67).

**Attack B: use the native local balls and contract each change of units.**
Equations (55)–(59) admit native local directions with a fixed Cauchy radius.
Equations (60)–(62) give the complete primitive derivative.
Equations (41)–(43) then bound the derivative of one matched response by
\[
 C\left(\|\dot b\|_w+
             {\|b\|\over r^{\rm loc}}\|\dot p\|_{\mathcal P,w}\right).
 \tag{68}
\]
This includes the assigned independent current and, when present, the conditional mean derivative.
For a strictly descending chain, (65)–(66) remove the former exponential loss in its length.

The failed step is verifying (64) with \(\epsilon_i\le1\) for each link of the actual returned chain.
In (62), \(\kappa_t^0\) is the velocity of the earlier pair's own reference datum.
In (29), the node and endpoint velocities come from the prescribed returns.
Neither is a coefficient derivative multiplied by the new small \(b\).
For a same-level link there is also no unit contraction.
The native balls control a coefficient as a function of its input; they do not control the input's derivative.
Thus substituting (68) repeatedly leaves these terms unbounded and does not prove (67).
This is a specific missing estimate in the attempted recursion, not a missing Gaussian basis.

One cannot repair this step by changing to the box comparison theorem alone.
`o1-decoupled.md:173–184` assumes both the transported-pair estimate (H-pair)
and the prescribed node comparison (H-node).
Those assumptions are the very estimates needed at this link.
The theorem also requires geometry agreement on the enlarged read sets.
Its proof does not construct the stage return that would supply them.

**Attack C: replace the whole chain by one physical restriction problem.**
At a real critical input, the restriction identity (3) and the pivot construction (12)–(14)
give the reconstructed old physical datum.
On an admitted physical path the fixed-system force is (15).
At \(s=1\), the multiplier calculation in `wf-room-2.md` (S4) makes (26) equal the physical current.
This gives a direct route on that locus without multiplying earlier derivatives.

The extension needed in (67) has independent current and all earlier decoupling parameters.
For it, the actual system is (23).
Its assigned multiplier leaves the exact residual
\[
 H_p^{\mathsf T}\{F'_p(h)-K_h^{\mathsf T}\lambda\}
                 =(1-K_0H_p)^{\mathsf T}\lambda,
 \tag{69}
\]
already derived in (28).
SA 10369–10372 says that undecoupled identities “are not imposed on their decoupled sums”.
SA 10462–10464 explicitly says the two systems “define separate functions” away from physical pairs.
Thus the single physical saddle cannot be substituted for the full returned program.

Nor does equality on the physical current graph determine the extension.
In a local pair chart, the holomorphic covariant function
\(c\{J-J(U)\}\) vanishes on that graph for every scalar \(c\).
Its derivative in the independent-current direction is \(c\) times the identity.
This is a hand check of the failed identity-theorem argument, not an alternative to the assigned current (26).
For that assigned current, one must return to the full equations (24), (27) and (29).
The unbounded terms from Attack B then remain.
This is the exact failed step of Attack C.

These attacks concern the same statement (67): gauge transport, native analytic estimates with scale contraction,
and physical variational reduction.
None supplies the returned pair velocity uniformly on the required earlier-parameter domains.
No counterexample to that statement or to the actual stage inclusion has been established.

## Result

**Partial proof.** This extends a stage step sketched or cited by the sources. It grants no status.
The continuation proves the fixed-coordinate carriage identities (49)–(53).
They remove the unnecessary common-Gaussian requirement and distinguish two different centered-coordinate paths.
It uses the complete account's native local-ball proof to obtain (56)–(59), under the stated operator premises.
It computes the moving-reference contribution to the raw datum in (60)–(63).
It also proves a uniform derivative bound for the strictly descending chains specified in (64)–(66).
The hand example (67b) corrects the earlier pointwise return shortcut: physical potential bounds need covariant return differences.

The first open step is Lemma R, the actual returned-pair response (67).
Section 18 attacks it through the gauge cocycle, local analytic balls with scale contraction,
and one physical restriction problem. Each attack states its exact failed step.
Native coefficient estimates do not yet bound the prescribed reference and return velocities after every earlier read.
The local derivative formulas retain the full forcing.
Their identification and uniform bounds on the complete stage family remain unproved.
Equation (10) and `stage-resp.md` (5)–(8) still do not prove single-layer stage \(0\to1\) inclusion.
No computation discharges a step. This text is not yet checked by the other model.
