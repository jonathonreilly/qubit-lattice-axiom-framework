## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
Its [digest](prior/repo-search-2026-11-08.md), §§9 and 13, found representation and replay inputs, not this application.
`prior/leaf-jh.md` is absent at the requested pin.

| Hit checked | Relation to this leaf |
|---|---|
| `loc-3.md` and `loc-4.md`, read whole | Claude's Theorem W, corrected by Codex, already gives the conditional replay implication. Its D1/D3 inputs remain. |
| `r2-heal.md` and `gates/r2-heal-check.md`, read whole | The check directs replay back to Theorem W. No replay or vacuum proof is repeated. |
| `leaf-d1.md` and `leaf-d3.md`, read whole | Native operator entry is conditional. The remaining tests concern the source ball and the actual regional branch. |
| `hma.md`, D1–D3, D6 and Theorem 8 | The relative gauge and physical Hessian implication already exist. PH3 still requires the branch match. |
| `st1-r4.md:44–53,347–365,780–807,879–900` | Specifies raw versus reduced data, conditional uniqueness, the stage fibre, and its completed source. These are the closest local inputs. |
| `dr.md:166–213` | Already chooses the full completed-source radius with exponent 64. Its current is ST1's continuation. Only its radius calculation is reused here. |
| PR #10114, `SOFTHARD.md:534–547` | Fetched at `f76f6c649cff7dffbab664d8976e680e8f287fe9`. Requires both adjoining constraints, crossing rows and singular parts. Supplies no regional admission theorem. |

The PR path starts at `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Credit its repository authors, and Claude and Codex for LOC, ST1, DR and HMA.
The workflow was read with git show from main at 43a1fcc374711ca50626eca667441d3ca575c7d1.
The registry retains DR for D1 and HM-A for HMA-BRANCH.
The exact leaf names occur in `hstep-tree2.md`, with this assignment in FINISH 566.
No separate assignment or completed proof of this shared application was found.

# One joined datum and the physical branch

Codex, 2026-11-08. Research base `b7000edcdf91bdb061d1f8998cd1d9f31c427cc0`.
Research text, not an audit. Grants no status. Only this file is an output.
All calculations are written arguments. No numerical run enters the proof.
The checkout advanced concurrently to 60ddc80b975233996a1adbbe6fb44cf2d86f5ab7.
The cited local proof inputs were compared with the research base and were unchanged.
Concurrent FINISH and gate changes were left untouched.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**,
for the source constructions and ports below.
Credit **Tadeusz Bałaban** for the constrained-background and multiscale methods.

Line numbers refer to these pinned texts:

- **SA:** `YM4_sketch_500.tex`, `31a47c543775`.
- **Y:** `YM4_1400.tex`, `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **I:** `theorem_0_complete_account_raw_I.tex`, `31a47c543775`.

The requested `/tmp` copies were reused or fetched only when absent.
The SA index, neighbouring rows and obligations were consulted for the cited objects.
One source locator in the tree needs correction.
Y 16128–16169 describes operators and their conventions.
The explicit reduced-datum inverse is at **Y 10707–10782**.
Its full node diagram is at **Y 34153–34208**; the one-step factor is at **Y 42131–42157**.
SA 9638–9644, 9918 onward and 11183–11202 give the corresponding outline formulas.

## 1. Kill tests, before the application proof

### Outward source

Use one seam of a two-part join, at depth at least two.
An upper row \(c\) has outer endpoint \(z\).
Its finer endpoint block consists of determining interior rows.
This is the source geometry, Y 10719–10723 and 34153–34168.
Use unit lower reference links for this first test.
Put \(B_{\rm raw}(e)=tT\) on one lower interior bond \(e=(z,z+e_1)\), in lower lattice units.
All other raw rows vanish, including \(B_{\rm raw}(c)\).
Here \(T\) is a Pauli matrix.
Let \(r_{\rm raw},C_{\rm cmp}\) be the local radius and completion bound of Y 10735–10747.
Choose \(0<|t|<\min\{r_{\rm raw},s_D/C_{\rm cmp}\}\).
The source's local completion bound then puts the whole completed family in the original source ball.

For \(x\in B_L(z)\), let \(p_x\) be the fraction of its prescribed coordinate paths using \(e\).
Each such use has positive orientation.
Thus \(0\le p_x\le1\), and \(p_{z+e_1}=1\).
All products commute in this test. The prescribed contour mean is exactly

\[
 T_{zx}(e^{iB_{\rm raw}})=e^{itp_xT},\qquad
 v_z(B_{\rm raw})=e^{it\nu T},\qquad
 \nu=L^{-4}\sum_{x\in B_L(z)}p_x\ge L^{-4}>0.                 \tag{1}
\]

These identities use the actual exponential of averaged relative logarithms,
not a replacement averaging rule; see Y 42131–42143.
All logarithms use their branch at one.
Consequently the required completed row is

\[
 b_J(B_{\rm raw})(c)=t\nu T\ne0.                              \tag{2}
\]

ST1 (7) supplies precisely (2) to the response equations.
The native joined row supplies the same value.
**Outcome: the actual completed-row convention passes.**
The substitution \(S(c)=B_{\rm raw}(c)=0\) fails this written test.
That substitution is already excluded by ST1; it is not a new counterexample to the construction.

For the radius test, let \(S=tE_c\), where \(\|E_c\|_Y=1\) and \(0<t<s_D\).
The norm tends to \(s_D\).
Hence the full independent ball fits \(\|S\|_Y<r_{\rm DF}\) exactly when \(s_D\le r_{\rm DF}\).
A common radius \(s_D\le b_*<r_{\rm DF}\) needs strict inequality.
Section 3 checks this without replacing the original ball by a minimum.

### Noncommuting lower reference and the cut action

Keep the same native join and take its admitted real physical reference \(U_+\).
Set its current to the derivative of its native inner-plaquette action.
The following test holds for every such reference, including nonflat references with noncommuting lower data.
It does not choose an independent current.

Vary only the highest active datum, at level \(k\), through the actual outer pivot graph.
An old outward row has level \(j\le k\).
Its block factor reads level \(j-1\), whose relative increments are zero.
This remains true for a noncommuting lower reference.
For each of these old-row block transports, the factor in Y 42136–42137 is

\[
 T_{zx}(W)T_{zx}(W)^{-1}=I.                                  \tag{3}
\]

Thus each old outward reduced-datum factor is exactly one throughout this variation.
It does not contain an absolute logarithm of the fixed lower reference.
The accumulated fine-field node gauge need not be one.
It is retained and removed by ST1 (34), with the prescribed values at the nodes.
Confusing these two factors would invalidate the test.
A new outward next row has level \(k+1\), so its lower block can vary.
Its factor is retained inside the actual plain outer mean.
The pivot equation, not (3), fixes that next row; see (16)–(19).

This includes, for example, lower matrices \(X=e^{i\alpha\sigma_1}\) and \(Y=e^{i\beta\sigma_2}\).
For \(0<\alpha,\beta<\pi/4\),
\(XY-YX=-2i\sin\alpha\sin\beta\,\sigma_3\ne0\).
Their commutator plaquette is nontrivial.
Equation (3) holds for these references as well.
The test uses any admitted physical realization; it does not assert that arbitrary stored data can be inserted into a fixed history.

At a newly cut face both native problems use the plaquettes wholly inside \(\Omega_0^J\).
For every allowed variation \(a\), their action differentials are the same finite sum

\[
 \delta A_J[a]=\sum_{p\subset\Omega_0^J}\delta a_p[a].           \tag{4}
\]

Neither side includes an ambient plaquette crossing that face.
The fixed boundary links and bare determining rows are the same on both sides.
This checks the boundary action separately from the row equation.
**Outcome: no node or boundary mismatch on the common native problem.**
Using an ambient restriction in place of that native problem would not establish this comparison.
Section 4 identifies the actual maps and also checks their next constraint.

## 2. Fix the common join and identify its source

Use the first two-part collared join from a3-close Lemma J.
Apply it to the longer sequence through the next level.
Write

\[
 \Omega_q^J=\Omega_q\cap T^1_{\min(q,j_1)}
                         \cap T^2_{\min(q,j_2)}.             \tag{5}
\]

Retain that lemma's separation, aligned blocks and collar hypotheses.
The old and next native problems use the same first member \(W=\Omega_0^J\).
Their determining maps are denoted \(M_-^J,M_+^J\).
The former stops at level \(k\); the latter includes the actual next member.
Write \(U_-^J(D)\) for the construction's level-\(k\) background on this system, with its entire datum \(D\).
The notation includes its stored rows; it does not denote an ambient background restricted to \(W\).
Keep \(k\ge2\), so this is not the zero-depth test of leaf-d3.
One may take both collared parts in layer \(k\), away from the next member.
The proof uses the complete row sets, including the two collars.

This is a native problem on (5).
It is not either original part's inverse, or the compression of an ambient critical problem.
The actual localized background is defined this way at SA 9783.
A3-close Lemma J supplies its geometry and row assignment.
It copies the old group datum on retained rows and supplies the prescribed lift on new rows.
A retained row can change from interior to outward without changing its group datum.

At the ordinary birth on this joined problem, use the actual next datum \(D_+^J\).
It includes those retained stored rows and their original field versions.
Let \(U_+\) be its admitted next regular critical background, and set

\[
 \mathbf V_+=M_-^J(U_+),\qquad V=\mathcal M^kU_+|_{\text{complete outer reads}}.
                                                               \tag{6}
\]

The field \(V\) includes the fixed surrounding level-\(k\) rows read by the outer mean.
Only its active rows will vary.
Thus the reference on a newly exposed old row is the average of this very \(U_+\).
It is not an independently chosen lift of another field.
The retained lower rows in (6) are the stored rows of \(D_+^J\).
This is the physical-reference prescription of ST1 Lemma 12 and F4.
No stored row is overwritten by a convenient reference value.

For J, let \(P\) vary over the original admitted independent-current pair domain on this same join.
Write \(\mathbf V_0^J(P)\) for the reference datum actually passed by that caller.
At the physical birth (6), it is \(\mathbf V_+\).
It can be complex at other admitted pairs.
The following identities are pointwise group identities on the common branches.
The independent current does not enter the completion map.

For any target datum \(D\) on the old joined row set, the caller uses

\[
 B_{\rm raw}(c)=i^{-1}\Log[D(c)\mathbf V_0^J(c)^{-1}],
 \qquad S=b_{\mathbf V_0^J}^J(B_{\rm raw}).                    \tag{7}
\]

ST1 (6)–(8) explicitly sends the raw coordinate to the background chart,
and the reduced coordinate to the response.
ST1 Lemma 12 and F4 retain this rule on changed outward rows.
The same dictionary applies to a localization call with another prescribed reference;
one must replace that reference on both sides of (7), not identify the two references.

Port the exact node diagram, Y 34153–34208.
Let \(u_\pm\) be the one-step factor at a lower outward endpoint, and one otherwise.
The completed row obeys

\[
 e^{iS(c)}\mathbf V_0^J(c)
 =u_-(B_{\rm raw})^{-1}
       \{e^{iB_{\rm raw}(c)}\mathbf V_0^J(c)\}u_+(B_{\rm raw}).
                                                               \tag{8}
\]

For \(c_+=z\) outward, (8) gives precisely

\[
 S(c)=i^{-1}\Log\!\left[
 e^{iB_{\rm raw}(c)}
 \operatorname{Ad}(\mathbf V_0^J(c))v_z(B_{\rm raw})\right].     \tag{9}
\]

For \(c_-=z\) outward it gives \(e^{iS(c)}=v_z(B_{\rm raw})^{-1}e^{iB_{\rm raw}(c)}\).
Interior rows have \(S(c)=B_{\rm raw}(c)\).
Every factor uses the native finer block, its stored reference and all its interior rows.
A row's old interior classification is not carried into (8).
This proves J-OUTWARD-ID for the literal caller.

There is no hidden iteration over outward rows.
Y 10719–10782 proves that the factor reads interior rows only.
It gives the explicit inverse and a uniform local chart.
In its derivative notation, \(Db=D+T\) and \(TD^{-1}T=0\).
We use that proved source result; no new depth estimate is needed.

The full independent source is \(S\), not the physically generated subset of (7).
On its original ball every \(S\) has the source's inverse raw coordinate,
once the early radius lies in that inverse chart.
This is an identity on that ball, not merely on real sources.
The granted complete-read admission supplies the reference patches and their branches, uniformly over this pair domain.
The local inverse uses the same complex reference on both sides.
It does not project that reference onto its physical locus.
Section 3 puts the original ball inside the inverse chart.

All rows here are raw angles.
ST1's array norm and TD's assigned row norm are their maximum norm:

\[
 \|S\|_{\rm src}=\sup_{c\in\mathbf B_-^J}|S(c)|=\|S\|_Y.       \tag{10}
\]

Use leaf-d1 (4)–(5): \(K^J=m_JQ^J\) and \(H^J=\mathsf H^Jm_J^{-1}\).
The row lengths are the native lengths on (5).
The diagonal stays \(-a_0I\).
No length factor is silently moved into (10).
Nor is the force anchor or any switch tag changed by this source identity.

## 3. Compare the unchanged radius

The pin leaves the early multiplicative radius constants existential.
It fixes their order of choice.
DR Theorem 4 already supplies the exponent \(c_D=64\) and the following radius.
This is closer than the purely symbolic comparison in leaf-d1.

Let \(C=C_{\rm op}\ge1\) be the common early bound for the granted native operators and their paired columns.
In DR's notation take \(b_0=t_0=C\); enlarging an early upper bound is allowed before choosing its radius.
Let \(C_R\) include the native row constant, finite incidences and the granted absolute coefficient majorant.
The same row estimate, independent of the current anchor, gives

\[
 C_{\rm der}(r)\le2C_Rr.                                     \tag{11}
\]

This is DR 198–200 and d3-local §3's integral of the row second derivative.
The force anchor remains \(J_*=F'_U(0)\).
Only the inverse \(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T}\) is estimated here.
It is the same inverse for either anchor; their returned currents are not identified off shell.

Let \(r_{\rm red}>0\) be the admitted completed-datum inverse-chart radius from §2.
Fix, before \(\bar\kappa\),

\[
\begin{split}
 0<c&\le\min\{r_0/4,(16C_W)^{-1},(16C_C)^{-1},r_{\rm red}\},\\
 c_*&=c/4,\\
 \epsilon_D&=\min\{c_*C^{-4},(32C_RC^2)^{-1},r_R/(4C)\},\\
 c_D&=64,\qquad s_D=\epsilon_De^{-64\bar\kappa}.              \tag{12}
\end{split}
\]

These are DR (9)'s original choices, with an explicit strict reserve in its free constant \(c_*\).
This instantiates the existing existential contract.
It is not a replacement of an already fixed ball.
Any additional early ceilings in that contract can be met by choosing \(c\) smaller at this same step.
No lower bound on \(c_*\) or \(\epsilon_D\) is imposed in TD or TD2.

Put \(B=Ce^{16\bar\kappa}\) and choose the common bound \(b_*=2s_D\).
Then, on the entire original source ball,

\[
 s_D\le\tfrac14cC^{-4}e^{-64\bar\kappa}
       =\tfrac14r_{\rm DF},\qquad
 s_D<b_*<r_{\rm DF}.                                        \tag{13}
\]

The original comparison J1 is therefore
\(\epsilon_DC^4e^{(64-c_D)\bar\kappa}\le c/4<c\).
Also \(s_D\le r_{\rm red}/4\), so §2's inverse chart covers the full ball.
Its centre is \(b_J(0)=0\); no recentering occurs.

Put \(R_*=2Bb_*\).
The retained floor \(\bar\kappa\ge1\) also gives
\(2R_*=8Bs_D\le2r_Re^{-48\bar\kappa}<r_R\), since \(e^{48}>1+48>2\).
Thus the whole common field ball lies within the local row and \(R_h\) chart.
Equation (11) gives the required paired-current estimate:

\[
 BC_{\rm der}(2R_*)\le8C_RB^2b_*
       =16C_RC^2\epsilon_De^{-32\bar\kappa}\le\tfrac12.       \tag{14}
\]

The last inequality uses (12) and \(\bar\kappa\ge0\).
It is uniform in depth, volume and the two parts.
The operator and row bounds remain the explicitly granted leaf-d1/D2 inputs.

Check the remaining order, rather than changing the source radius later.
TD 426–437 and TD2 169–182 choose all constants in (12) before \(\kappa,\bar\kappa,M\).
They impose lower bounds on the later rates.
They fix \(s_D\) only after \(\bar\kappa\).
Their source and Cauchy requirements are then late coupling ceilings.

For completeness, their possibly sensitive Cauchy ratio has the following exact scale.
At fixed earlier constants put

\[
 d=\min\{s_D/2,C_Ac_{\rm ch}L^{-9}/2\}>0,\quad
 \varrho=\frac{d}{c_TC_Ae^{\bar\kappa}g},\quad
 A_V=C_DE_{\bar\kappa}C_Ag(3A_1\ell^{p_0}+c_Te^{\bar\kappa}\ell^q).
\]

Here \(q>p_0\), \(g=e^{-\ell/2}\), and \(A_R\) is already fixed.
Since \(K_1=\max\{1,4A_R/A_V\}\), the two alternatives in
\(\vartheta=4K_1A_1\ell^{p_0}/(\delta\varrho)\) are bounded by

\[
 C_1g\ell^{p_0},\qquad C_2\ell^{p_0-q},                     \tag{15}
\]

with finite constants depending on the fixed positive \(d\).
Both tend to zero.
For the first limit, \(e^{\ell/2}\ge(\ell/2)^n/n!\) with any integer \(n>p_0\).
The second follows from \(q>p_0\).
The source ceiling \(C_AA_1g\ell^{p_0}<s_D/2\) and the chart ceiling follow in the same order.
TD Theorem 10 and TD2's feasibility argument already handle the other amplitudes.
They are reused, not derived again.
Thus (12) is compatible with their Cauchy budget.

The radius kill test consequently passes for this one original constant choice.
For a separately fixed larger ball, (13) cannot be asserted.
Its test remains J1; failure would refute that inclusion, not nonlinear existence.

## 4. H-ROWS on this same birth

Keep the inputs granted by the tree: PH1, PH4 and their admitted common physical neighbourhood.
Keep PH2's base criticality at \(U_+\).
Use the P81/REG regular uniqueness class already supplied to ST1 Lemma 5.
We prove the remaining row and fibre identification.
No assertion about all independent-current pairs is made.

The relevant source standing is as follows.

| Source | What is used |
|---|---|
| Y 10707–10782; 34153–34208 | Proved reduced-datum identities and inverse; ported in §2. |
| Y 35634–35649, 35747–35822 | Proved regular-orbit uniqueness and local physical continuation, on their admitted class. Reuse their mechanism through ST1 Lemma 5. |
| SA 9776–9783 | The native restriction and next-background prescription; sketched there. ST1 Lemmas 5 and 12 supply the existing conditional repository implementation. |
| Y 92576–92598 | Physical covariance identification on the same critical graph. HMA Theorem 8 already gives the repository implication. |
| I 45162–45201 | The older account labels its general constrained-minimizer uniqueness/locality lemma “Proof outstanding”. No unrestricted CA admission or locality claim is imported. |

### The actual next determining map

Let \(E\) be the old top rows used by the next constraints.
Include every prescribed pivot and all fixed rows read by those constraints.
Let \(R\) be the retained determining rows of all levels.
The old datum \(D\) is a single family on \(\mathbf B_-^J\).
It has one value on a shared row.

The actual map from old determining data to next determining data is

\[
 \mathcal F_J(D)(r)=D(r)\quad(r\in R),\qquad
 \mathcal F_J(D)(d)=\mathcal M(D_k)(d)
                         \quad(d\text{ a new level-}(k+1)\text{ row}).
                                                               \tag{16}
\]

The fields in the second formula include their fixed surrounding rows.
For each new row, separation puts its complete double block inside \(\Omega_k^J\).
The old system is truncated at \(k\).
Thus every constituent level-\(k\) bond in that block is an old determining row.
There is no omitted inward row in this computation.
This includes a new outward next row: its outer endpoint block is also inside \(\Omega_k^J\).
Consequently iteration of the actual mean gives

\[
                  M_+^J=\mathcal F_J\circ M_-^J.             \tag{17}
\]

This is ST1 Lemma 12 (67), applied with the native row sets of (5).
Its proof and the node convention are reused.
Equation (16) spells out the application at the changed collar.
It does not average two independently solved parts.

Let \(\Phi_V(u)\) be the actual outer pivot graph, with all fixed rows retained in its read.
The old datum of the step is

\[
 D(u)=e^{iB(u)}\mathbf V_+,\qquad B(u)=\iota\Phi_V(u).         \tag{18}
\]

Here \(\iota\) writes only the active highest-level rows.
It is zero on every retained row.
This is the literal datum curve in ST1 Lemma 12 and F4, now on (5).
It is also HMA's stipulated active injection, not a new support mask.

The graph equation says that the second part of (16) is unchanged.
The first part is unchanged by the zero entries of \(\iota\).
Using (6) and (17) gives

\[
       \mathcal F_J(D(u))=D_+^J,\qquad
       M_+^J(U_-^J(D(u)))=D_+^J.                            \tag{19}
\]

Thus the actual next determining map is constant on this fibre.

### The complete old rows and their node factors

The following comparison uses the same row address and field version in both maps.

| Native row | Its raw datum in both maps | Its reduced datum in both maps |
|---|---|---|
| Lower retained row | Its stored \(\mathbf V_+(c)\), unchanged | Zero relative increment, with its prescribed endpoint factors |
| Retained top row | Its stored \(\mathbf V_+(c)\), unchanged | Zero |
| Active top interior row | \(e^{i\Phi_V(u)(c)}\mathbf V_+(c)\) | \(\Phi_V(u)(c)\) |
| Active top outward row, if present | The same group datum | The same \(\Phi_V(u)(c)\), because its lower increments are zero |
| Row whose type changed at the join | The entry assigned on the native row set in §2 | Formula (8), using its new type and complete native lower block |

For the last two lines it is essential that “zero” means zero **relative increment**.
It does not mean that the stored field equals the identity.
Every outward factor reads a strictly lower interior block.
All increments in that block vanish on (18).
Therefore (3) gives, exactly on the admitted graph,

\[
                b_{\mathbf V_+}^J(B(u))=B(u).               \tag{20}
\]

There is no expansion in \(u\) here.
Equation (20) retains noncommuting lower reference data.
It also retains the lower version of every stored row; none is recomputed from a different background.

The P81 chart takes the raw datum (18) and solves with the reduced forcing (20).
Its literal representative includes the node return in ST1 (34).
The step background \(U_-^J(D(u))\) takes the same raw determining datum.
Thus both sides of H0 have every row of (18), not just their active rows.
For independent sources with changed lower rows, one must instead use (8).
The nonzero correction in the first kill test cannot be discarded there.

### Criticality and the boundary variation space

Both old constructions use \(A_J\), the inner-plaquette action on \(W\).
The definition of the localized background at SA 9783 fixes that action and its determining problem.
The chart in PH1 uses the same native problem, as PH4 requires for its rows.
The variation space fixes the same exterior links and imposes the derivative of the complete old constraint.
Equation (4) therefore compares all its boundary terms.
The ambient crossing action, if retained elsewhere in the full representation, is not silently added to this native variational problem.

At zero, (17) gives
\(\ker DM_-^J(U_+)\subset\ker DM_+^J(U_+)\).
PH2's base criticality therefore makes \(U_+\) critical for the old datum \(\mathbf V_+\).
This uses the same action on both kernels.
ST1 Lemma 5's uniqueness identifies its orbit with \(U_-^J(\mathbf V_+)\).

At real \(u\), the step background is critical for \(A_J\) with datum (18), by its definition.
PH1's P81 chart is critical for that same action and datum.
Both start at the just identified orbit.
The base lies strictly inside the supplied regular uniqueness class.
Continuity gives a real neighbourhood of \(u=0\) where both remain in that class.
This is a neighbourhood for testing equality, not a replacement of their original common domain.

Regular uniqueness now identifies the two real orbits.
Use their common mean-contour representative under CV to compare them.
The canonical representatives coincide; the Landau representatives are related by their specified node returns.
Consequently

\[
 [U_-^J(e^{i\Phi_V(u)}V;\text{stored rows})]
       =[\Phi_{\rm ch}^J(\iota\Phi_V(u))],\qquad
 [U_-^J(V;\text{stored rows})]=[U_+].                        \tag{21}
\]

This proves H-ROWS and the real form of H0 on the stated birth.
The proof applies to any two-part native join with these supplied hypotheses.
It makes no assertion that every history meets those hypotheses.

### Continue the identity and transport the gauge

The two canonical representatives are holomorphic on the originally supplied connected common chart.
Their difference vanishes on a real open \(u\)-ball.
At any point of that ball, all real coordinate derivatives of the difference vanish.
Its holomorphic Taylor coefficients are those derivatives divided by factorials.
They therefore vanish.
The holomorphic identity theorem extends the equality throughout that connected common domain.
This proves H0 there without requiring an open set of independent currents.

A real gauge transforms all determining rows, stored values and node returns together.
The actual mean is gauge covariant and \(A_J\) is gauge invariant.
It takes the common real variational problem to the same transformed problem.
Uniqueness identifies the transformed real orbits.
The preceding holomorphic argument then identifies their continuations.
Thus (21) commutes with real gauge transport.

The current throughout this physical comparison is \(J=dA_J\).
We did not replace the force-anchored independent-current continuation by ST1's different continuation.
At a physical pair their anchors coincide; away from that locus their equality is not asserted.

## 5. Result and next input

This closes the requested **fixed-join leaf as an implication from the tree's granted inputs**.
J-OUTWARD-ID uses the actual completed source on the full independent ball.
The original existential constant choice can be made once as (12), with both required margins.
H-ROWS and H0 hold on the supplied common physical chart of the same native birth.
The source background theorem, inverse theorem, LOC implication and HMA Hessian theorem have not been rederived.

The closure is the application just written, not a proof of its admission inputs.
HMA Theorem 8 can use (21) wherever its other hypotheses hold.
In particular, its D6 is stated for a complete physical pair with \(\Omega_0\) the torus.
A proper-region application must retain its regional physical hypotheses;
this note does not erase that qualification or identify a restricted ambient current with \(dA_J\).

The next leaf is **HMA-DOM on this join**: supply the original whole-domain admission for the actual regional caller.
That includes its full reference reads, unchanged stored rows and common connected chart.
Its owner remains HM-A, with DR retaining native response admission.
The stored-gauge and activity formation match remains HMA-FORM afterward.
No competing lane is opened.

| Item | Status here | Scope or remaining input |
|---|---|---|
| Outward kill test | Passes for the literal caller; raw-row substitution explicitly fails | Equations (1)–(2), checked by hand |
| Noncommuting-reference and cut-action test | Exact agreement on the native physical problem | Equations (3)–(4); all prescribed node returns retained |
| J-OUTWARD-ID | Proved by applying the source's complete datum diagram | Original completed row coordinates and granted chart admission |
| Unchanged source-ball comparison | Proved for one joint original choice | Equations (12)–(14); not a theorem about a separately fixed larger ball |
| H-ROWS and H0 | Proved on the supplied common physical chart | Same native rows, action, variations, regular class and next map |
| Physical Hessian | Existing HMA implication can consume this branch identity | All remaining HMA hypotheses, including its physical/regional scope |
| Full D1, D3, H_step | Not closed | Original admission and formation suppliers remain |
| Independent check | Not performed | This is author research text; no status granted |

**First open input:** HMA-DOM's actual whole-domain supply on this same join,
together with the native complete-read admission that the J leaf was instructed to grant.
Do not repeat the row completion, uniqueness mechanism, or radius comparison to address that input.
