# Clock and supported-error tradeoffs for a supplied exact two-body loader

2026-10-18. **Conditional theorem with selective source-exposed checks.** The two new implementation alternatives and their scalar premises have the exact scoped reviews identified in Section 9. ROOT read the complete manuscript against its checked source chain; this synthesis is not an additional independent check or a retained audit. The source-exposed correction to one arithmetic comparison in the robustness review is controlling where that comparison is used.

The mathematical parent is [Exact two-body engineered loader](EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md), at the source identity in Section 9. It supplies the positive two-body primitives, ordered global operation, structured coefficient family, and known engineered-clock mechanism. The present result gives two ways to obtain a finite complete-output window for that supplied operation:

| Installation | Coefficient/error contract | Explicit sufficient resources as \(\epsilon\to0\), fixed \(\Lambda>0\) |
|---|---|---|
| Engineered clock with load reserve | Position-dependent nominal hoppings; independent supported block errors bounded by \(\delta\), with positivity and vacuum/conservation conditions | Minimal-window size \(\Theta(1+\log(1/\epsilon))\), time \(\Theta(\Lambda^{-1}[1+\log(1/\epsilon)])\), sufficient allowed-error ceiling \(\Theta(\Lambda\epsilon/[1+\log(1/\epsilon)])\) |
| Uniform ordinary propagation with a weak source | Exact ordinary hopping and matching ratios, equal arms/rails and diagonals, \(\gamma=\rho J\); no independent-error theorem asserted | Size \(\Theta(\epsilon^{-2}\log(1/\epsilon))\), time \(\Theta(\Lambda^{-1}\epsilon^{-2}\log(1/\epsilon))\), weak source \(\gamma=\Theta(\Lambda\epsilon)\) |

These are two literal finite Hamiltonians and two sufficient proofs. The second row does not inherit the first row's runtime or error tolerance. Neither row is an optimality bound, practical device estimate, preparation protocol, or native realization of an active system Hamiltonian. All full-output phases and residual apparatus coordinates are retained below.

## 1. Common supplied operation and inherited exact interface

There are three shared ordinary qubits \(Q,P,R\). The two logical rail bits \(a,b\) label head positions; they are not additional ordinary controls or duplicated copies of \(Q,P\). Supply one head, coherent logical \(b\), \(a=1\), an arbitrary joint state of \(Q,P\) and passive references, \(R=0\), and vacuum on every other head. The data and references have no additional free Hamiltonian in these theorems. Their degeneracy, initial states, isolation and the stated positive local interactions remain premises.

The common full operation is

\[
U_f=I_a\otimes X_R C_P^{(b)}\operatorname{SWAP}_{QP},
\qquad
C_P^{(b)}=|0\rangle\langle0|_P\otimes X_b+
           |1\rangle\langle1|_P\otimes I_b.
\tag{1}
\]

In the computational basis it maps
\[
|b,q,p,0\rangle\longmapsto
|b\mathbin{\oplus}(1-q),p,q,1\rangle .
\tag{2}
\]
The old \(P\) state and any reference correlations move to \(Q\); no environment or old state is discarded. Arbitrary superpositions and passive references are included by the same isometry.

The checked parent has 26 ordered layers, 44 physical diamonds, 296 internal heads and these same three ordinary qubits. A fixed physical arm rotation \(A\) and the ordered rail/data gauge \(W\) give an exact one-head scalar-clock identification for the stated structured coefficient family. Its left prefix is the identity and its right prefix is \(-U_f\). The arm rotation is an exact change of coordinates in the proof, not an additional prepared data resource. Physical internal rail \(a=1\) by itself need not be invariant.

For the matched uniform member, the internal virtual positions are \(x=0,\ldots,73\), and the scalar diagonal is \(2J+\mu\), with \(\mu=(\sqrt2-1)J\). For the finite engineered member, these positions are shifted to \(1,\ldots,74\), and positive onsite compensation gives a different constant diagonal \(C\). Those conventions, onsite terms and phases are kept separate.

The parent’s range-18 embedding, ordinary data degree 20 and selective two-body supports remain. Scalar nearest-neighbor propagation after a coordinate change is not a nearest-neighbor claim for the physical loader. Known square-root-chain perfect transfer is inherited with its original attribution in the parent, rather than asserted as a new transfer mechanism here.

## 2. Engineered clock: positive load reserve and a supported-error theorem

Fix \(0<\epsilon\le1\), \(\Lambda>0\), and an integer \(L\ge296\). Place all four identical nominal rails on positions \(0,\ldots,L\), with source 0, internal positions \(1,\ldots,74\), and external output \(75,\ldots,L\). Use
\[
J_\star=\Lambda/80,\qquad C=4J_\star,\qquad
\alpha=\frac{2J_\star}{L+1},\qquad
\kappa_r=\alpha\sqrt{r(L+1-r)},\quad 1\le r\le L .
\tag{3}
\]
Then \(0<\kappa_r\le J_\star\). The exact physical inventory is \(4L+7\) qubits and \(8L+172\) listed positive blocks.

Use the parent structured prescription: diamond bond parameters are \(a_L=\kappa_{\rm left}/\sqrt2\), \(a_R=\kappa_{\rm right}/\sqrt2\), and contact parameter \(g=\kappa_{\rm middle}\). The positive terminal and equal-arm occupations are
\[
p_L=C-(2a_L+c_L),\quad p_R=C-(2a_R+c_R),\quad
p_A=C-(a_L+a_R+g).
\tag{4}
\]
Here \(c_L,c_R\) are incident cable hoppings. The other Hadamard, permutation and ordinary positions have respectively \(C-(\sqrt2t+c)\), \(C-(t+c)\), and \(C-(\kappa_{\rm left}+\kappa_{\rm right})\), where \(t\) is the mixer/permutation link magnitude and \(c\) the incident cable hopping, with absent endpoint hoppings zero. Each compensating coefficient is at least \((3-\sqrt2)J_\star\). Installed identity contacts and their compensating occupations remain distinct listed blocks. No old \(\mu\) repair is added.

For the nominal Hamiltonian,
\[
(AW)^*H_{\rm one}(AW)
=\left[CI-\sum_{r=1}^L\kappa_r
 (|r\rangle\langle r-1|+|r-1\rangle\langle r|)\right]\otimes I .
\tag{5}
\]
Its exact endpoint profile is
\[
f_x(t)=e^{-iCt}\sqrt{\binom Lx}\,
       [i\sin(\alpha t)]^x[\cos(\alpha t)]^{L-x}.
\tag{6}
\]
The powers of \(i\), the sign of the cosine and \(e^{-iCt}\) are part of the target. There is no additional \(e^{-i\mu t}\). The one-head scalar \(CI\) does not assign energy to the physical head vacuum.

Replace each fixed listed block \(h_b\) by \(\widetilde h_b=h_b+E_b\). The error class requires:

1. \(E_b\) is time-independent and self-adjoint on the same listed one-/two-qubit support, with full-support norm \(\|E_b\|\le\delta\).
2. It conserves local head number and annihilates local head vacuum for every value of any local data factor. There is no new support, data-only term or bypass.
3. Each \(\widetilde h_b\) is positive on its complete support, supplied or proved separately. General small matrix errors do not guarantee positivity of a block with nominal zero eigenvalues.

The errors can differ independently between arms, rails and blocks. No equal-error, zero-mean or statistical assumption is made; they may break the exact gauge. Entrywise reality is a separate condition if real changed blocks are desired. Splitting a listed block into more independently perturbed pieces changes the contract.

Full-support nominal incident sums and their worst-case increases are
\[
\begin{array}{c|c|c}
\text{physical vertex}&\text{nominal sum}&\text{increase}\\ \hline
\text{head}&(5+\sqrt2)J_\star&4\delta\\
Q\text{ or }P&40J_\star=\Lambda/2&20\delta\\
R&16J_\star=\Lambda/5&8\delta .
\end{array}
\tag{7}
\]
Thus \(\delta\le\Lambda/40\) preserves the common incident cap. This uses full-support block norms, not cancellation or a one-head expectation. More generally \(0<J_\star<\Lambda/40\) allows the sufficient margin \(\delta\le(\Lambda-40J_\star)/20\); slowing the nominal clock also lengthens the time over which errors accumulate.

Here is the reason the evolution comparison has no volume factor. A head meets at most four listed blocks. On the one-head sector, a head-data or onsite error acts only at its head coordinate; a two-head error contributes a two-by-two head-coordinate matrix whose entries have norm at most \(\|E_b\|\). When the head is outside that support the error vanishes. Self-adjoint row/column Schur bounds therefore give
\[
\|E_{\rm one}\|\le2\max_i\sum_{b\ni i}\|E_b\|\le8\delta .
\tag{8}
\]
The shared data degree affects (7), but does not multiply (8). A vacuum action or an added free data term would invalidate this argument.

For the full input isometry \(E_{\rm in}\), put \(A_t=e^{-itH}E_{\rm in}\) and \(\widetilde A_t=e^{-it\widetilde H}E_{\rm in}\). Both evolutions preserve the one-head sector, so Duhamel gives
\[
\|\widetilde A_t-A_t\|\le8\delta t=:\beta_t .
\tag{9}
\]
It pays all physical differences, including phase, from preparation time zero. It is not a budget only over the eventual window width, and no output phase is fitted afterward.

Suppose the nominal profile on a closed interval \(\mathcal I\subset[0,T_{\rm hor}]\) obeys
\[
q_0(t):=\sum_{x=0}^{74}|f_x(t)|^2\le\epsilon^2/1024 .
\tag{10}
\]
Let \(z_t\) be the positive-norm normalization of the restriction of (6) to \(75,\ldots,L\), and use the complete target
\[
\mathcal V_t\xi=-z_t\otimes U_f\xi .
\tag{11}
\]
All other heads are vacant in the target, and all data and references are retained. The exact nominal external part is \(\sqrt{1-q_0}\,\mathcal V_t\), hence
\[
\|A_t-\mathcal V_t\|^2=2-2\sqrt{1-q_0}\le2q_0,
\qquad \|A_t-\mathcal V_t\|\le\epsilon/16 .
\tag{12}
\]
With the explicit sufficient ceiling
\[
\boxed{\quad
\delta\le\min\!\left\{\frac{\Lambda}{40},
                         \frac{\epsilon}{256T_{\rm hor}}\right\},
\quad}
\tag{13}
\]
we have \(\beta_t\le\epsilon/32\) and therefore, uniformly on \(\mathcal I\),
\[
\|\widetilde A_t-\mathcal V_t\|\le3\epsilon/32<\epsilon/8 .
\tag{14}
\]
The corresponding unhalved stabilized complete-channel distance is at most \(3\epsilon/16<\epsilon/4\). Isometry norm, purification and contraction include arbitrary passive references and mixed inputs.

Let \(\Pi_{\rm ext}\) be physical external occupancy and \(P_1\) the actual record projection \(R=1\). They commute. The target lies in their joint range, and the nominal failure amplitude of that joint event is \(\sqrt{q_0}\). Thus
\[
\|(I-\Pi_{\rm ext}P_1)\widetilde A_t\xi\|
\le\sqrt{q_0}+\beta_t\le\epsilon/16,\qquad
\Pr_{\widetilde A_t\xi}(\text{external and }R=1)
\ge1-\epsilon^2/256 .
\tag{15}
\]
Each marginal probability has the same lower bound. Under the admitted errors, external occupancy need not imply \(R=1\) exactly; the joint estimate pays both failures. Success probabilities can depend on the input.

## 3. Explicit engineered-window, dwell and tolerance policies

For a short window choose
\[
L=L_0(\epsilon):=\max\{296,\lceil4\log(32/\epsilon)\rceil\}.
\tag{16}
\]
Any larger \(L\) also works with its own time and tolerance below. In the angular interval \([\pi/3,2\pi/3]\), the binomial law of (6) has parameter at least \(3/4\); since \(74\le L/4\), its checked exponential tail gives \(q_0\le e^{-L/2}\le\epsilon^2/1024\). Set
\[
\begin{split}
T&=\frac{20\pi(L+1)}{\Lambda},&
\mathcal I_0&=[2T/3,4T/3],\\
T_{\rm hor,0}&=\frac{80\pi(L+1)}{3\Lambda},&
\delta_0&=\frac{3\epsilon\Lambda}{20480\pi(L+1)} .
\end{split}
\tag{17}
\]
Then \(8\delta_0T_{\rm hor,0}=\epsilon/32\), and \(\delta_0<\Lambda/40\). Equations (14),(15) hold throughout this positive-width interval. At \(T\), the nominal endpoint operation has the fixed phase \(-e^{-iCT}i^L\); a perturbed member is bounded by (9), not declared perfect.

At the minimal prescription (16), size and time have the first-row orders in the opening table. The floor \(L\ge296\), hence at least 1191 qubits, remains. For fixed nonzero \(\delta\), this sufficient certificate also requires
\[
L+1\le\frac{3\epsilon\Lambda}{20480\pi\delta}.
\tag{18}
\]
Increasing length reduces the nominal tail but increases elapsed perturbation cost. This is a certificate tradeoff, not a necessary precision limit.

For adjustable dwell let
\[
m=\max\{148,\,8\log(1024/\epsilon^2)\},\qquad
L\ge\max\{296,\lceil2m\rceil\},\qquad
\theta=\arcsin\sqrt{m/L}\le\pi/4 .
\tag{19}
\]
For \(X\sim\operatorname{Bin}(L,p)\), exponential Markov gives
\(\Pr(X\le74)\le e^{74-(1-e^{-1})Lp}\le e^{-Lp/8}\) when \(Lp\ge148\). Thus (10) holds on the entire interval
\[
\begin{split}
t_{\rm arr}&=\frac{40(L+1)\theta}{\Lambda},\\
t_{\rm end}=T_{\rm hor,d}&=\frac{40(L+1)(\pi-\theta)}{\Lambda},\\
D=t_{\rm end}-t_{\rm arr}
 &=\frac{40(L+1)(\pi-2\theta)}{\Lambda},\\
\mathcal I_d&=[t_{\rm arr},t_{\rm end}],\qquad
\delta_d=\frac{\epsilon\Lambda}
 {10240(\pi-\theta)(L+1)} .
\end{split}
\tag{20}
\]
Again \(8\delta_dT_{\rm hor,d}=\epsilon/32\), and the load condition is automatic. This is a fixed schedule valid for every admitted perturbation, not a realization-dependent hitting time.

For a requested ratio \(\mathcal R\ge2\), choose
\[
L_{\mathcal R}=
\left\lceil\max\left\{296,\,
\frac{m}{\sin^2[\pi/(\mathcal R+2)]}\right\}\right\rceil .
\tag{21}
\]
It ensures \(D/t_{\rm arr}=\pi/\theta-2\ge\mathcal R\) and
\[
\frac{m(\mathcal R+2)^2}{\pi^2}
\le L_{\mathcal R}
\le\frac{m(\mathcal R+2)^2}{4}+1 .
\tag{22}
\]
Consequently this chosen family has size \(\Theta(m(\mathcal R+2)^2)\), arrival time \(\Theta(m(\mathcal R+2)/\Lambda)\), dwell and horizon \(\Theta(m(\mathcal R+2)^2/\Lambda)\), and allowed-error ceiling \(\Theta(\Lambda\epsilon/[m(\mathcal R+2)^2])\). The explicit simpler condition
\[
\delta\le\frac{\epsilon\Lambda}
 {2560\pi\,[m(\mathcal R+2)^2+8]}
\tag{23}
\]
is sufficient for the selected \(L_{\mathcal R}\), by bounding its actual horizon. It does not automatically certify a still larger length. The ratio concerns a scheduled finite interval, not monitoring, capture or an irreversible record.

## 4. Actual record normalization and coefficient size are separate questions

For the nominal engineered installation, the current \(R=1\) branch includes position 73 in the antisymmetric arms of the final record diamonds and positions \(74,\ldots,L\). Its probability is
\[
p_1^0(t)=|f_{73}(t)|^2+\sum_{x=74}^L|f_x(t)|^2
\ge1-q_0(t)\ge1-\epsilon^2/1024 .
\tag{24}
\]
It carries the same \(-U_f\) with the complete profile and phase on those positions. This positively normalized profile differs from (11), whose support starts at 75.

For a normalized purified input, set \(a=P_1\widetilde A_t\xi\), \(b=P_1A_t\xi\). Then \(\|a-b\|\le\beta_t\), \(\|b\|=\sqrt{p_1^0}\), and (15) gives the actual probability floor \(\|a\|^2\ge1-\epsilon^2/256\). The reverse triangle inequality yields
\[
\left\|\frac a{\|a\|}-\frac b{\sqrt{p_1^0}}\right\|
\le\frac{2\beta_t}{\sqrt{p_1^0}}
\le\frac{\epsilon}{16\sqrt{1-\epsilon^2/1024}}
<\epsilon/8 .
\tag{25}
\]
Its unhalved trace-distance consequence is below \(\epsilon/4\), with references retained. Analogous external-only or joint projections compare to (11). These are statewise normalized comparisons on the certified interval; input-dependent normalization does not define a linear postselection channel. The complete-channel bound (14) uses no postselection.

There is no blanket exact or uniformly accurate rare-event assertion for independent errors outside that interval. A general normalization comparison requires a nonzero nominal branch and \(\beta_t<\sqrt{p_1^0(t)}\). The nominal clock returns at \(\pi/\alpha\); exact recurrence at that same time is not asserted for arbitrary perturbed members, and no permanent-halt mechanism is supplied.

The smallest nominal virtual hopping and the actual error ceilings satisfy
\[
\kappa_{\min}=\frac{\Lambda\sqrt L}{40(L+1)},\qquad
\frac{\delta_0}{\kappa_{\min}}=
\frac{3\epsilon}{512\pi\sqrt L},\qquad
\frac{\delta_d}{\kappa_{\min}}=
\frac{\epsilon}{256(\pi-\theta)\sqrt L}.
\tag{26}
\]
A coefficient's magnitude is not a tolerated error. For the scalar-coefficient subclass with each original positive operator form retained,
\[
\|\Delta Q_s\|=2|\Delta a|,\qquad
\|\Delta[g\,n(I\pm X)]\|=2|\Delta g|,\qquad
\|\Delta[pn]\|=|\Delta p| .
\tag{27}
\]
Here \(Q_s\) denotes a fixed-sign bond of amplitude \(a\), with its original hopping sign retained. The contact conversion also covers an installed identity occupation \(2gn\), while an omitted zero contact remains omitted. Coefficient changes at most \(\delta/2\) for each bond/contact and \(\delta\) for each compensation suffice. Nominal nonzero bond weights are at least \(\kappa_{\min}/\sqrt2\), contact parameters at least \(\kappa_{\min}\), and compensations at least \((3-\sqrt2)J_\star\); the stated tolerances keep each scalar weight strictly positive. General matrix-valued errors still need their separate positivity premise.

The frozen review's Section 5 incorrectly compares \(\delta_0\) with \(\epsilon\Lambda/[7680\pi(L+1)]\): their ratio is \(9/8\), not less than one. The [root arithmetic correction](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_engineered_loader_robust_policy_check/ROOT_ARITHMETIC_CORRECTION.md) supplies the valid common bound for both policies,
\[
\frac{\delta}{J_\star}
\le\frac{3\epsilon}{256\pi(L+1)}
<3-\sqrt2,\qquad L\ge296,\quad0<\epsilon\le1 .
\tag{28}
\]
Thus the positive-compensation conclusion and all performance formulas remain unchanged. The original review is preserved with this explicit qualification; no source revision is implied.

## 5. Uniform ordinary propagation: the actual finite physical installation

The second installation retains the matched 26-layer network at
\[
J=\Lambda/40,\qquad \mu=(\sqrt2-1)J .
\tag{29}
\]
Its internal inventory is 296 heads, \(Q,P,R\), and 468 positive blocks. All ordinary virtual hoppings are \(-J\), with the exact diamond/mixer matching ratios and equal arms and rails. The common scalar diagonal is \(2J+\mu\).

Attach \(\ell\) ordinary heads and \(\ell\) positive \(Q_J\) bonds to each of the eight origins. For heads \(v,w\), write
\[
Q_c(v,w)=c[n_v+n_w-(\sigma_v^+\sigma_w^-+
                             \sigma_v^-\sigma_w^+)],\qquad \|Q_c\|=2c .
\tag{30}
\]
At each of the two left \(a=1\) endpoints attach a source \(s\) by the combined block
\[
B=Q_\gamma(s,v_\ell)+(2J-\gamma)n_s+(J-\gamma)n_{v_\ell},
\qquad \gamma=\rho J,\quad 0<\rho\le1/2 .
\tag{31}
\]
The other six rays have cap \(Jn_{v_\ell}\). Add \(\mu n_v\) at every exterior head, including both sources. Do not add \(\mu\) again to the internal diamonds/mixers; the eight internal permutation potentials are already included in the 468-block count.

The source block is positive on its full two-qubit support. Its one-head matrix on \((s,v_\ell)\) is
\[
\begin{pmatrix}2J&-\gamma\\-\gamma&J\end{pmatrix},
\tag{32}
\]
and its doubly occupied eigenvalue and full norm are \(3J\). The adjacent ordinary bond provides the missing \(J\) at \(v_\ell\). Every one-head diagonal, including sources and capped endpoints, is therefore \(2J+\mu\). The cap and the source cannot be replaced by ordinary bonds without changing the operator.

Supply a single head coherently in the two \(a=1\) source endpoints, with the input of Section 1. The capped \(a=0\) left rays remain part of the physical apparatus. Under the exact finite \(A,W\), all internal links and diagonals are scalar. On the left, \(W=I\), so the unequal selected/unused terminations remain diagonal in \(a\). On the right, \(W=-U_f\) is constant, and the four identical caps/bonds commute through it. The transformed finite operator is thus a direct sum of scalar clocks indexed by \(a,b\). Only the two identical \(a=1\) clocks are populated. Their invariant physical image is \(AW\) of that selected space, not the set of physical internal \(a=1\) coordinates.

For either selected clock set \(n=x+\ell\). The source at \(x=-\ell-1\) is \(s\), the first ordinary site is \(n=0\), and
\[
K=74,\qquad N=2\ell+73,\qquad
F=\{\ell+74,\ldots,2\ell+73\}.
\tag{33}
\]
The \(\ell\) positions in \(F\) are precisely the physical external output \(x=74,\ldots,73+\ell\). The literal selected scalar operator is
\[
H_{\rm fin}=B+\sum_{n=0}^{N-1}Q_J(n,n+1)
                  +Jn_N+\mu\sum_{v=s,0,\ldots,N}n_v .
\tag{34}
\]
At the source, \(AW\) is the identity; on \(F\) it is \(-U_f\). This verifies the finite scalar-to-physical interface including all boundaries and phases. It uses the matched/global parent identities, not the engineered propagator (6).

## 6. The distinct scalar finite-source proof

We give the proof and explicit constants used by this installation. In this section \(K\ge1\) may be fixed generally, \(0<\rho\le1/2\), \(N=2\ell+K-1\), \(\ell\ge100(K+1)\), and \(F=\{\ell+K,\ldots,2\ell+K-1\}\). The physical transfer in Section 5 uses \(K=74\).

### 6.1 Exact source and a single spectral omission

Let \(H_\infty^0\) be the semi-infinite one-head operator on \(s,0,1,\ldots\), with diagonal \(2J\), source hopping \(-\rho J\) and all ordinary hoppings \(-J\). Put \(u=Jt\), \(e(k)=2(1-\cos k)\), and
\[
F_{\rm src}(k)=
\frac{-i\sqrt{2/\pi}\,\rho\,e^{ik}}
     {(2-\rho^2)\cot k-i\rho^2},\qquad
w(k)=|F_{\rm src}(k)|^2,\qquad
\int_0^\pi w(k)\,dk=1 .
\tag{35}
\]
We write \(F_{\rm src}\) to distinguish this spectral function from the output set \(F\). The checked endpoint spectral calculation gives the exact spatial identity
\[
\begin{split}
e^{-itH_\infty^0}|s\rangle
 &=A(t)|s\rangle+O_tF_{\rm src}+I_t\overline{F_{\rm src}},\\
(O_tf)_n&=\frac1{\sqrt{2\pi}}\int_0^\pi
             e^{ink-iue(k)}f(k)\,dk,\\
(I_tf)_n&=\frac1{\sqrt{2\pi}}\int_0^\pi
             e^{-ink-iue(k)}f(k)\,dk,\qquad n\ge0,\\
A(t)&=\int_0^\pi e^{-iue(k)}w(k)\,dk .
\end{split}
\tag{36}
\]
The phase \(e^{ik}\) is essential. Neither lead term alone is a normalized half-line state. Their interference and the emitter coordinate make (36) an exact unit vector.

The spectral normalization is the standalone half-line calculation, not an assumption about a finite device. For the centered ordinary lead, the physical Weyl branch is \(m(z)=[z-\sqrt{z^2-4J^2}]/(2J^2)\), and the source resolvent is \([z-\gamma^2m(z)]^{-1}\). With \(a_0=2-\rho^2\), the cotangent change of variables integrates (35) to one. The positive spectral density exhausts the cyclic source mass for \(\rho>0\); no additional source atom is omitted. This statement is not applied to the finite capped spectrum.

Use \(0<h\le10^{-3}\), \(\rho^2\le h\), and the actual real cutoff \(\chi\): it equals one on \(|k-\pi/2|\le h/2\), zero on \(|k-\pi/2|\ge3h/4\), and in each transition is
\[
\chi=1-10z^3+15z^4-6z^5,\qquad
z=4(|k-\pi/2|-h/2)/h .
\tag{37}
\]
It is \(C^2\cap W^{3,1}\), with the required first and second derivative traces at joins; an arbitrary \(C^2\) cutoff would not supply the third weak derivative used below. Require \(P=3\rho^2/h<1/2\), as the final policy will ensure. The density then gives
\[
P=3\rho^2/h,\qquad
p=\|\chi F_{\rm src}\|_2^2\ge1-P>1/2,\qquad
g=\chi F_{\rm src}/\sqrt p,\quad \|g\|_2=1 .
\tag{38}
\]
For example, writing \(q=k-\pi/2\),
\[
w(k)=\frac{2\rho^2/\pi}{(2-\rho^2)^2\tan^2q+\rho^4}
\]
and extending the \(q^{-2}\) bound beyond \(|q|>h/2\) proves the displayed omitted-mass ceiling.

The exact normalized filtered state is
\[
\begin{split}
\Phi_\chi(t)&=e^{-itH_\infty^0}\chi(H_\infty^0)|s\rangle/\sqrt p\\
 &=A_\chi(t)|s\rangle+O_tg+I_t\bar g,\\
A_\chi(t)&=\frac1{\sqrt p}\int_0^\pi
                 \chi(k)w(k)e^{-iue(k)}\,dk,\qquad \|\Phi_\chi(t)\|=1 .
\end{split}
\tag{39}
\]
The source integrand contains one \(\chi\), not \(\chi^2\). The seed comparison is paid once:
\[
\||s\rangle-\Phi_\chi(0)\|
\le\sqrt P+P\le2\sqrt P .
\tag{40}
\]
It remains this small under a common later unitary. No omitted spectral component is multiplied by a long Duhamel time.

### 6.2 Explicit scalar pole constants and the two signs

Only scalar coefficient \(M=1\) is used from the checked pole and half-line lemmas. Put
\[
a=23/100,\quad B_2=64,\ B_3=512,\ B_4=2048,\qquad
(D_0,D_1,D_2,D_3)=(2,24,394,6280).
\]
The coefficient derivative tuple before the cutoff is \((1,2,7,30)\). Define fixed numerical constants
\[
\begin{split}
P_\star={}&\frac{D_3}{a^3}+\frac{6B_2D_2}{a^4}
 +\left(\frac{4B_3}{a^4}+\frac{15B_2^2}{a^5}\right)D_1\\
 &+\left(\frac{B_4}{a^4}+\frac{10B_2B_3}{a^5}
                         +\frac{15B_2^3}{a^6}\right)D_0,\\
Q_\star={}&\frac{D_3}{2a^2}+\frac{2B_2D_2}{a^3}
 +\left(\frac{4B_3}{3a^3}+\frac{15B_2^2}{4a^4}\right)D_1\\
 &+\left(\frac{B_4}{3a^3}+\frac{10B_2B_3}{4a^4}
                         +\frac{3B_2^3}{a^5}\right)D_0,\\
D_\star={}&4P_\star+20Q_\star .
\end{split}
\tag{41}
\]
There is no hidden accuracy-dependent constant in this definition.

The real substitution \(x=\tan(k-\pi/2)\), \(A_0=2-\rho^2\), \(b_0=\rho^2/A_0\) gives
\[
F_{\rm src}(k(x))=
\frac{i\sqrt{2/\pi}\rho\,e^{ik(x)}}{A_0(x+ib_0)},\qquad
\frac1{x+ib_0}=-i\int_0^\infty e^{ixv-b_0v}\,dv .
\tag{42}
\]
The conjugate denominator instead gives \(+i\int_0^\infty e^{-ixv-b_0v}dv\). Thus the outgoing source adds \(+vx\); the incoming conjugate adds \(-vx\). They cannot be interchanged on the basis of equal moduli.

The cutoff amplitude \(\chi(k(x))e^{\pm ik(x)}k'(x)\) has weak derivative \(L^1\) bounds \(D_r/h^2\) through order three. Three real integrations by parts have absolute coefficients \(1,6,4,15,1,10,15\). With first derivative magnitude at least \(aM_0+v\) and subsequent bounds \(B_2M_0,B_3M_0,B_4M_0\), integration in \(v\) gives the favorable pointwise ceiling \(\rho Q_\star/(h^2M_0^2)\), including the normalization allowance from \(p>1/2\). For an adverse pole sign, split at half the negative gap, bound the low range by these derivatives, and apply Parseval to the whole high-range Fourier sequence before integrating \(v\). The latter step is essential: an infinite half-line norm is not obtained by summing a uniform pointwise ceiling.

These are the checked real-axis estimates for the actual cutoff. Fubini is legitimate first at each \(\rho>0\), with finite majorant proportional to \(\|\text{amplitude}\|_1/b_0\); the uniform estimates follow afterward. No analytic cutoff, network inverse or biased-momentum coefficient enters.

### 6.3 Fixed-diagonal far cut, from time zero

Extend the finite space by a decoupled half-line beyond \(N\). Removing only the far hopping changes \(H_\infty^0\) by
\[
\Delta=J(|N\rangle\langle N+1|+|N+1\rangle\langle N|).
\tag{43}
\]
Every diagonal remains \(2J\), precisely because the physical cap in (34) is present. The finite restriction is the stated operator without \(\mu I\), and the initial physical source has no component in the other piece.

For \(0\le u\le7\ell/8\) and \(n=N,N+1\),
\[
2\ell\le n\le2.01\ell,\qquad
\partial_k[nk-ue(k)]\ge\ell/4,\qquad
\partial_k[-nk-ue(k)]\le-2\ell .
\tag{44}
\]
After changing to \(x\), the first derivative magnitudes exceed \(0.23\ell\), and the next three derivatives have ceilings \(4\ell,32\ell,128\ell\), dominated by (41). The \(+vx\) sign strengthens the outgoing derivative, and the \(-vx\) sign strengthens the incoming derivative. Both are favorable from time zero. At each cut site, each lead component of (39) is at most \(\rho Q_\star/(h^2\ell^2)\). Hence
\[
\int_0^{7\ell/(8J)}\|\Delta\Phi_\chi(t)\|\,dt
\le\frac{7\sqrt2}{4}\frac{\rho Q_\star}{h^2\ell}
<\frac{3\rho Q_\star}{h^2\ell}.
\tag{45}
\]
This is an integral of norms. It neither assumes a zero initial filtered tail beyond the cut nor cancels oscillations inside Duhamel. Together with (40),
\[
\|e^{-itH_{\rm fin}}|s\rangle-e^{-i\mu t}\Phi_\chi(t)\|
\le2\sqrt P+\frac{3\rho Q_\star}{h^2\ell},
\quad 0\le t\le7\ell/(8J),
\tag{46}
\]
using the zero extension of the finite vector. There is no artificial early-contact interface.

### 6.4 Full packet, both omitted half-lines, and the actual emitter

On all integer \(n\), let \(b_n(t)=(O_tg)_n\). Parseval after zero extension of \(g\) to a full Fourier period gives \(\sum_{n\in\mathbb Z}|b_n|^2=1\). Define
\[
d(t)=\|(b_n)_{n\notin F}\|_2,\qquad
q_F(t)=\sqrt{1-d(t)^2},\qquad
z(t)=q_F(t)^{-1}\sum_{n\in F}b_n(t)|n\rangle .
\tag{47}
\]
The policy below proves \(q_F>0\) before this target is used. Its normalization is positive real, with no phase adjustment.

On \(u\in[3\ell/4,7\ell/8]\), the complete incoming half-line, including its origin, obeys
\[
i(t):=\|I_t\bar g\|_{n\ge0}
<\frac{4\rho Q_\star}{h^2\ell^{3/2}} .
\tag{48}
\]
For the omitted left outgoing interval, write \(n=(\ell+K-1)-r\), \(r\ge0\). This includes every negative Fourier index as well as all physical input and interior coordinates. The actual negative gap and translation satisfy
\[
Q_{\rm left}=1.98u-(\ell+K-1)\ge0.4\ell,\qquad
(\ell+K-1)+u\le16Q_{\rm left}.
\]
The checked low/high auxiliary-frequency estimate gives
\[
d_{\rm left}\le
\frac{4\rho P_\star}{h^2\ell^{3/2}}
 +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\tag{49}
\]
For the right interval \(n=(2\ell+K)+r\), \(r\ge0\),
\[
Q_{\rm right}=0.99(2\ell+K)-2u\ge0.23\ell,\qquad
(2\ell+K)+u\le16Q_{\rm right}.
\]
The favorable estimate gives \(d_{\rm right}<20\rho Q_\star/(h^2\ell^{3/2})\). Combining these two norm bounds,
\[
d(t)\le\frac{\rho D_\star}{h^2\ell^{3/2}}
       +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\tag{50}
\]
The endpoints are exactly one site below and above \(F\); no fixed interior coordinates are omitted from the budget.

Finally, exact normalization of \(\Phi_\chi\), rather than a substituted survival estimate, closes the full apparatus comparison:
\[
\operatorname{Re}\langle z,\Phi_\chi\rangle\ge q_F-i,\qquad
\|\Phi_\chi-z\|^2\le2(1-q_F)+2i\le2d^2+2i .
\tag{51}
\]
When \(q_F\ge i\), its complete complement also satisfies
\(\|(I-P_F)\Phi_\chi\|^2\le d^2+2i\). This pays the actual filtered emitter \(A_\chi\), every source/input/interior coordinate and the beyond-cap tail. An estimate on the different unfiltered \(A(t)\) is not used. The square-root cost of \(i\) in (51) is retained.

Combining (46),(51) gives the complete finite scalar bound
\[
\|e^{-itH_{\rm fin}}|s\rangle-e^{-i\mu t}z(t)\|
\le2\sqrt P+\frac{3\rho Q_\star}{h^2\ell}
                           +\sqrt{2d(t)^2+2i(t)} .
\tag{52}
\]
No normalization or projection of the actual physical state occurs in this inequality.

## 7. Uniform-loader policy, complete output and physical resources

For \(0<\epsilon\le1\), take the constants (41) and
\[
\begin{split}
h&=10^{-3},\qquad \rho=\epsilon\sqrt h/1024,\\
\ell&=\left\lceil\max\left\{
\begin{gathered}
1000,\quad7500,\quad\frac{192\rho Q_\star}{h^2\epsilon},\\
\left[\frac{128\rho D_\star}{h^2\epsilon}\right]^{2/3},
\quad\left[\frac{32768\rho Q_\star}{h^2\epsilon^2}\right]^{2/3},\\
\frac{10}{\rho^2}\log\frac{512\sqrt h}{\rho\epsilon}
\end{gathered}
\right\}\right\rceil,\\
t_-&=\frac{3\ell}{4J},\qquad
t_+=\frac{7\ell}{8J},\qquad J=\Lambda/40 .
\end{split}
\tag{53}
\]
Here \(7500=100(K+1)\) for \(K=74\), and the log argument equals \(524288/\epsilon^2>1\). All choices are made before \(\ell\); the policy is noncircular. It guarantees \(\rho\le1/2\), \(\rho^2\le h\), \(P<1/2\), both actual phase gaps exceeding one, and
\[
\begin{array}{c|c}
\text{quantity in the full-state proof}&\text{allowance}\\ \hline
2\sqrt P&<\epsilon/256\\
3\rho Q_\star/(h^2\ell)&\le\epsilon/64\\
\text{algebraic part of }d&\le\epsilon/128\\
\text{exponential part of }d&\le\epsilon/128\\
i&\le\epsilon^2/8192 .
\end{array}
\tag{54}
\]
Thus \(d\le\epsilon/64<1\), proving the positive normalization in (47); also \(q_F>i\). The final term of (52) is at most \(\sqrt3\,\epsilon/64<\epsilon/32\). The normalized complete scalar error is consequently \(<13\epsilon/256\) throughout the closed window.

Let \(z(t)\) be precisely (47), with \(K=74\). The physical target is
\[
\mathcal V_{\rm unif}(t)\xi
=-e^{-i\mu t}z(t)\otimes U_f\xi
\tag{55}
\]
on the external right-head embedding. All other physical heads are vacant in this comparator, with \(Q,P,R\) and every passive reference retained. The Fourier integrand already contains \(e^{-iJt\,2(1-\cos k)}\); its \(2J\) phase is not counted again. Equation (55) has one additional \(\mu\) phase and the fixed minus sign from the global gauge.

The two selected \(b\)-clock errors have identical scalar profile and orthogonal rail labels. Their direct sum has the same operator norm as one scalar error, with no \(\sqrt2\) multiplier. The physical \(AW\) preserves that norm. Hence for the actual selected input isometry \(E\),
\[
\sup_{t_-\le t\le t_+}
\|e^{-itH}E-\mathcal V_{\rm unif}(t)\|
<13\epsilon/256<\epsilon/16 .
\tag{56}
\]
The unhalved stabilized complete-channel distance is \(<13\epsilon/128<\epsilon/4\). Since (55) lies entirely in physical external output and \(R=1\),
\[
\Pr(\text{external and }R=1)
>1-(13\epsilon/256)^2 .
\tag{57}
\]
The weaker \(1-\epsilon^2/64\) floor is also valid. These probabilities follow from the full norm theorem; no postselection is used to prove it.

For this exact installation, a separate global-gauge identity also determines the actual current \(R=1\) branch at every time. Write \(f_x^{\rm fin}(t)\) for the exact selected scalar evolution without \(\mu I\), and let \(J_{\rm rec}\) embed virtual 72 as the antisymmetric final-arm pair and \(x\ge73\) as their physical coordinates. With blank initial \(R\),
\[
P_1e^{-itH}E
=-e^{-i\mu t}J_{\rm rec}
\left[
\left(f_{72}^{\rm fin}(t)|72\rangle+
      \sum_{x=73}^{73+\ell}f_x^{\rm fin}(t)|x\rangle\right)
\otimes U_f
\right].
\tag{58}
\]
Its probability is input-independent. Whenever that probability is nonzero, the positively normalized complete branch carries exact \(U_f\), with its retained head profile and phase. A zero-probability normalized branch is undefined. External output begins at \(x=74\), so its profile and event differ from (58). Internal final-arm or origin occupancy can already have \(R=1\). This exact factorization uses the supplied coefficient identities and absence of earlier/free \(R\) terms; it is not an assertion about the independently perturbed family of Section 2.

The physical counts of the uniform installation are
\[
\text{heads}=298+8\ell,\qquad
\text{qubits}=301+8\ell,\qquad
\text{positive blocks}=478+16\ell .
\tag{59}
\]
The external blocks are \(8\ell\) ordinary \(Q_J\) bonds, two combined source blocks, six caps, and \(8\ell+2\) separate \(\mu n\) occupations, added to the 468 internal blocks. Counting \(B\) as one supplied positive two-body block is explicit; splitting its three summands changes block and perturbation bookkeeping, though not the Hamiltonian.

The full-support incident loads are \(40J\) on \(Q/P\), \(16J\) on \(R\), and below \(5J\) on internal heads. Exterior source, source-neighbor, ordinary and cap loads are respectively \(3J+\mu\), \(5J+\mu\), \(4J+\mu\), \(3J+\mu\). They all obey \(\Lambda\) under (29). No scalar subtraction reduces this accounting. The 299 internal qubits fit the inherited \(7^3\) cube with maximum Manhattan interaction range 18, and the eight distinct vertical rays have range-one bonds. The two source rays are one site longer. Data degree 20 and absence of undesired interactions remain supplied; this is not cubic nearest-neighbor hardware.

For fixed \(K=74\) and \(h\), the entries in (53) have orders \(1,1,\epsilon^{-2/3}\), and \(\epsilon^{-2}\log(1/\epsilon)\), apart from fixed geometric floors. The last term controls the asymptotic order of this explicit prescription:
\[
\ell=\Theta(\epsilon^{-2}\log(1/\epsilon)),\qquad
t_\pm=\Theta(\Lambda^{-1}\epsilon^{-2}\log(1/\epsilon)),\qquad
\gamma=\Theta(\Lambda\epsilon).
\tag{60}
\]
The window has width \(\ell/(8J)>0\), one sixth of its scheduled arrival time. The large explicit constants (41), the floor 7500 and the full maximum (53) remain the quantitative recipe. No practical numerical runtime follows from suppressing those constants.

## 8. What the tradeoff establishes

The engineered alternative obtains a short logarithmic-size sufficient family by supplying a position-dependent clock. Its cap margin allows arbitrary independently varying supported errors within the stated norm and positivity class, at an explicit cost proportional to elapsed time. The adjustable-dwell version pays quadratic length and horizon in the requested dwell/arrival ratio, and a correspondingly smaller sufficient error allowance.

The uniform alternative supplies constant ordinary propagation and a weak endpoint source, while keeping exact matching ratios, equal arms/rails and common diagonals. Its high-success finite window follows from the distinct normalized-source, pole-tail and fixed-diagonal-cut proof. It is not a robustness theorem for independently uncertain controls. In particular \(J=\Lambda/40\) saturates the nominal \(Q/P\) load; the half-cap margin and error policy of the other installation cannot be transferred to this one without separately checking the changed prescription.

Both retain the current-record/external-output distinction and all old-state/reference outputs. The exact member can return and unset its record; the finite window does not furnish permanent completion, capture, autonomous readout, reset or reuse. The exact normalized record identity in (58) and the probability-floor-based approximate identity (25) have different hypotheses and must not be conflated.

The positive blocks, selective supports, coefficient correlations or bounded supported errors, supplied endpoint coherence, head vacuum, blank record, passive references and freely degenerate data remain explicit. No active old-system Hamiltonian, energy-reference supplier, environmental stability, cooling or preparation mechanism is identified here. Separate product-reference rotation and active-energy constructions are not mathematical dependencies or claims of this manuscript.

## 9. Exact sources, recovery map and review exposure

The canonical destination is `docs/EXACT_LOADER_CLOCK_TRADEOFFS_BOUNDED_THEOREM_NOTE_2026-10-18.md`. The new evidence root is `outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/`. The exact complete bodies linked below are preserved there. Their original relative paths resolve under

`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

Historical pending labels in frozen proposals are interpreted through their corresponding completed reviews and ROOT dispositions, never silently rewritten. The packet manifest pins the new sources and unchanged inherited bodies separately.

### 9.1 New implementation arguments and the controlling correction

| Source / preserved packet link | Bytes | SHA-256 |
|---|---:|---|
| [Robustness proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_engineered_loader_robust_policy/PROPOSAL.md) | 25568 | `e69fa0e34d3fdb8d205cd1a8a5e26ea2efd3f3963a279b0d5edcf5d12ddbdc06` |
| [Robustness distinct review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_engineered_loader_robust_policy_check/REVIEW.md) | 13243 | `040de776f54dd19c241837eef77338aec6e2480a4e25b3d3009c9341a1d8a460` |
| [Root arithmetic correction](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_engineered_loader_robust_policy_check/ROOT_ARITHMETIC_CORRECTION.md) | 1412 | `0376cf28e128a19750d5a72676afd1a4b9a60817369dea40a1711e90d3ef5455` |
| [Uniform physical transfer proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_physical_loader/PROPOSAL.md) | 9952 | `809d39e07806cc05af1c715f58ebde90209a07b2dfc2e86bce481fe629c0629f` |
| [Uniform physical transfer distinct review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_physical_loader_check/REVIEW.md) | 11913 | `b9b897fc8dbce257a2bbe7895d5413d30d6f8cc289efb83b14ff7d465f5277c0` |
| [Literal uniform scalar finite-source theorem](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_chain_finite_launch/PROPOSAL.md) | 28149 | `bda916e331d0bf3863feac8e0b7dce279df6f2eaa94f0dd17daf651cad51545a` |
| [Uniform scalar distinct review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_chain_finite_launch_check/REVIEW.md) | 12769 | `0ef35c231f3550f196bd1f8df8b5b3773ebfa6314232931ea9470ca1f00a5bac` |

The robustness source, its distinct review and the root correction govern Sections 2–4. The correction fixes the review's reversed \(9/8\) comparison only; its source policy is unchanged. The uniform physical pair checks the selected invariant subspace, actual finite boundaries, common phase, counts and cap in Sections 5,7. Its complete performance premise is the separate scalar pair, whose proof is exposed in Section 6. These pairs have scoped support and root acceptance. That acceptance is conditional mathematics, not a physical experiment or retained audit; ROOT has read the complete synthesis and its source chain; that integration does not add an independent scientific review.

### 9.2 Bounded scalar proof closure

| Source / preserved packet link | Bytes | SHA-256 |
|---|---:|---|
| [Endpoint launch proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_endpoint_launch/PROPOSAL.md) | 14099 | `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4` |
| [Endpoint launch review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_endpoint_launch_check/REVIEW.md) | 12312 | `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1` |
| [Outgoing pole/IBP proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_outgoing_pole_tail/PROPOSAL.md) | 17300 | `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80` |
| [Outgoing pole/IBP review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_outgoing_pole_tail_check/REVIEW.md) | 12246 | `0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00` |
| [Half-line norm proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_halfline_tails/PROPOSAL.md) | 15197 | `43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1` |
| [Half-line norm review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_halfline_tails_check/REVIEW.md) | 9812 | `1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b` |
| [Late translated-tail proposal](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_late_tails/PROPOSAL.md) | 13034 | `a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9` |
| [Late translated-tail review](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_late_tails_check/REVIEW.md) | 7992 | `ef27352b742abe064e5b8d71d09d7904182cea49c9dce2c77187aab8494b34cd` |
| [Standalone source spectral measure calculation](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/bandcenter_reference_measure_check/REVIEW.md) | 8876 | `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae` |

The endpoint pair supplies the exact spatial source columns and their phases. The final table row is its self-contained Weyl-resolvent/density/mass premise: it is preserved as a proof body, not counted as an additional independent check of the new finite theorem. The pole, half-line and late-tail pairs supply the actual-cutoff third-derivative estimates, the conjugate-incoming and positive-outgoing norm estimates, and the translated negative-gap estimate respectively. Only their scalar \(M=1\), band-center, ordinary-dispersion cases are used. The actual hypotheses are instantiated in (35)–(50).

Those older complete texts also discuss network matrix coefficients and previous finite policies. Those applications are not premises of this manuscript. They need not pull a recursive archive of old inverses, biased calibrations, approximate routers or resource substitutions into this packet. The absolute-derivative alternative `common_product_narrow_cutoff_derivative` is likewise not used.

For definition provenance only, Section 1 of `endpoint_bandcenter_reference/PROPOSAL.md` was inspected: 11112 bytes, SHA-256 `510d5b1b51a152f90a8c2054fab382f74fb3f31159359e9c723e89d557380b2c`. Its combined positive block is explicitly reconstructed in (31),(32), and the spectral leaf above defines the operator it analyzes. That older source's remaining calibration, parity and device discussion is not imported or claimed fully reread here. It is not a required recovery body for the present proof.

### 9.3 Unchanged parent machinery, linked in place

The canonical parent is 31454 bytes, SHA-256 `43558ea59ebee23bf539d27ba1818a06b914fff52bb87d251b959b4889f3b868`. Its saved [publication observation](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_loader_publication/PUBLISHED.json), 356 bytes, SHA-256 `67e7830958c8a8dfed42764f21291e0abbd762fb7d3b0c2fa24e384e588b3d82`, records regular OPEN PR9737 at head `0de2d6c9d0ac308bccd5c721217150cb63dfcf26` and verification time `2026-10-18T07:05:04.467758+00:00`. This is an actual saved parent observation, not a fresh remote or checkout-state verification for this publication.

The following source bodies already belong to the parent packet. They are linked in place and pinned separately; their complete archive is not duplicated into this packet.

| Exact inherited argument and check | Source SHA-256 / review SHA-256 |
|---|---|
| [Diamond](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_diamond/PROPOSAL.md), 5208 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_diamond_check/REVIEW.md), 12143 bytes | `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33` / `da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945` |
| [Corrected matched extension](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_matched_extension/PROPOSAL.md), 5733 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_matched_extension_check/REVIEW.md), 10895 bytes | `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e` / `36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f` |
| [Global ordered composition](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition/PROPOSAL.md), 23893 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition_check/REVIEW.md), 14485 bytes | `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946` / `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6` |
| [Structured coefficient family](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients/PROPOSAL.md), 23193 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients_check/REVIEW.md), 13688 bytes | `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2` / `273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8` |
| [Engineered finite clock](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_operation/PROPOSAL.md), 11631 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_operation_check/REVIEW.md), 15460 bytes | `b8bbfb7d40c491aff6b893df6423b98e68edad91ef6596124dac10f3620c53f8` / `8351f91d29bbb570f8e9970962c2e0e24ea0db8dd06744d2180df761eae9272a` |
| [Engineered dwell certificate](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff/PROPOSAL.md), 13645 bytes; [review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff_check/REVIEW.md), 5655 bytes | `d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25` / `7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46` |

The robustness route imports the structured supported-error lemma and engineered/dwell scalar certificates. The uniform route imports the corrected matched/global physical identity and the new literal scalar finite proof. The latter does not depend on the engineered runtime. Earlier approximate-loader results and genealogical PR ancestry are not performance premises of either new argument.

### 9.4 Exposure and work performed

The drafting worker authored the robustness proposal and the uniform scalar finite-source proposal, and previously assembled the parent manuscript. It also checked the separate product-reference rotation source; that exposure is disclosed, but the rotation result is not a dependency. This is source-exposed synthesis within the same research campaign and model lineage, not an independent check of the worker's own proofs or blind replication of the parent.

All changed implementation arguments, their distinct reviews, the scalar finite pair, all four scalar component pairs, the standalone spectral-measure body and the root arithmetic correction were read completely. The immediately preceding complete reads of unchanged parent machinery were reused at the hashes above. The canonical parent was compared with the previously fully read author manuscript: the changes concern source/publication status and provenance wording, with the mathematical exposition unchanged. Exact identities of the inherited source pairs were refreshed. The older endpoint-definition source was read only at the explicitly identified Section 1; its other claims were not needed.

The packet selection is therefore a bounded recovery closure for these two arguments, not an assertion that every historical citation has been independently revalidated. Frozen source/check status is preserved. The review arithmetic correction is explicit, and neither a metadata match nor the number of review files is proof of physics.

The drafting work consisted of source inspection, analytical synthesis, deterministic byte/hash and link-mapping checks, and editing the author manuscript. ROOT then read the complete manuscript and final integration changes, preserved the exact source bodies, and performed the mechanical publication checks recorded in the packet. These checks establish source identity and integration consistency, not a new scientific execution, physical experiment or retained audit. No axiom or editable-prompt files were changed.
