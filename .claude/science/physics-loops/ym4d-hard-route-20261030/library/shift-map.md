# The preparatory shift map

Provenance: Codex (serving variant and effort not exposed; requested effort: max); checkout `ada28a0eb`; 2026-11-04; research text, not an audit; grants no status. Source text: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, commit `31a47c543775`. Not yet checked by the other model.

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

## 4. First open input: the actual collar reconstruction

The first missing input is the **matched stage reconstruction**, already at \(n=0\).
On physical backgrounds it must give the old raw datum \(D_1=\mathcal R_n(P,A_j,B_j;\zeta)\) and its return gauge.
Here \(P\) includes the independent current; \(\zeta\) includes every earlier parameter and switch.
On that critical family the field formula would be
\[
 \Delta_n=i^{-1}\Log(\mathcal R_nD_0^{-1}),\qquad
 \Phi(P,A_j,B_j;\zeta)=T_{e_-}(e^{i\Delta_n}D_0)^{r_n}.             \tag{8}
\]
The datum must match all surviving rows. The endpoint configuration must also satisfy the new coarse constraints, including (1).
Its logarithm must have collar support and a small uniform size \(\sigma_j=\sup_{P,\zeta}\|\Delta_n\|_Y\) sufficient for (10).
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

## Result

**Partial proof (first open input), for the shift sketched by the sources.**
Equations (1)–(7) give the correct common system, a local complex restriction identity, and its datum-forcing bound.
They retain the background theorem, admitted charts and weighted response package as explicit inputs.
The first open input is the matched stage reconstruction in section 4: identify the actual \((A_j,B_j)\) collar datum and returned pair on the full parameter domain.
CA-I 54287 only says “Express”; the needed construction and small forcing are not proved here.
No full shift map, stage \(0\to1\) inclusion, or counterexample to that inclusion is claimed.
The layered case is left to row 262. No computation discharges a step.
This text is not yet checked by the other model.
