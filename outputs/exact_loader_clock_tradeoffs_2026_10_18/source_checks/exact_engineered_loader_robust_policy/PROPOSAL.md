# Finite-window error and load-margin policy for the engineered loader

New conditional author derivation, 2026-10-18; a distinct check of this new policy is required. The three premise pairs identified in Section 9 are checked at their stated scopes. This note instantiates their finite-time supported-error lemma with an explicit positive incident-load margin, complete-output error allocation, and both short-window and adjustable-dwell length prescriptions. It does not claim exact gates under arbitrary errors, a fabrication procedure, native precision, an optimal tolerance, or permanent halt.

The nominal clock is slowed by a factor two relative to the earlier full-cap prescription: take \(J_\star=\Lambda/80\). Resolve the desired accuracy \(0<\epsilon\le1\) into nominal accuracy \(\epsilon/2\) and a complete evolution perturbation budget \(\epsilon/32\). For the actual observation horizon \(T_{\rm hor}\), the sufficient per-listed-block tolerance is

\[
\delta\le\min\left\{\frac{\Lambda}{40},
                         \frac{\epsilon}{256T_{\rm hor}}\right\}.
\tag{1}
\]

The performance term will be the smaller one for both explicit policies below. Under the stated error-class and positivity premises, the perturbed installation stays within incident cap \(\Lambda\), has complete-vector error at most \(3\epsilon/32\), unhalved complete-channel error at most \(3\epsilon/16\), and external-output **and** current-record success at least \(1-\epsilon^2/256\), uniformly on the selected finite interval. Normalized conditional conclusions require the probability floor and are stated separately.

## 1. Fixed physical domain and allowable errors

Use exactly the engineered installation of the checked source `b8bbfb7d`: 74 internal virtual positions at \(1,\ldots,74\), a source endpoint at 0, and external output at \(75,\ldots,L\), on all four identical nominal rails \((a,b)\). The 296 physical internal heads and shared ordinary qubits \(Q,P,R\) retain the same 26-layer gate. The input has one head at the left endpoint, \(a=1\), arbitrary coherent \(b\), arbitrary joint \(Q/P\) and passive-reference state, \(R=0\), and every other head vacant. There is no free data/reference Hamiltonian. These states and interactions remain supplied premises.

The desired full output operation is

\[
U_f=I_a\otimes X_R C_P^{(b)}\operatorname{SWAP}_{QP},
\qquad C_P^{(b)}=|0\rangle\langle0|_P\otimes X_b
                       +|1\rangle\langle1|_P\otimes I_b.
\tag{2}
\]

The old \(P\) state and its passive-reference correlations move to \(Q\). The physical output prefix is \(-U_f\). The rail labels are encoded in head positions, not additional ordinary data qubits. All head, data and reference outputs are retained in every complete-state comparison here.

Write the nominal physical Hamiltonian as the fixed listed sum \(H=\sum_b h_b\). Replace each listed block by \(\widetilde h_b=h_b+E_b\), on the **same** one-/two-qubit support, with:

1. \(E_b=E_b^*\), time independent, and \(\|E_b\|\le\delta\) in full-support operator norm.
2. Local head-number conservation and annihilation of local head vacuum for every value of a local data factor. No data-only term, new support, new bypass or vacuum action is admitted.
3. Each \(\widetilde h_b\) positive on its complete physical support, supplied or proved separately. Small norm error alone does not imply this because nominal blocks have zero eigenvalues.

These are deterministic worst-case bounds. Errors may vary independently from block to block; there is no statistical independence, averaging, zero-mean, equal-arm, equal-rail or paired-contact assumption on the errors. They can break the exact structured gauge. Entrywise reality may additionally be imposed to retain real positive matrices; the norm proof itself permits complex self-adjoint supported errors. It does not restore reality automatically.

The counting convention is fixed: an identity-diamond occupation and its compensating occupation are separate listed blocks, and omitted zero contacts are not new error supports. A head meets at most four listed blocks; \(Q/P\) meet twenty contacts each and \(R\) meets eight. Splitting blocks into more independently perturbed terms or adding unlisted interactions would require new bounds. The installation has \(4(L+1)\) head qubits, \(4L+7\) total qubits, and \(8L+172\) listed blocks. Its range-18 placement and data degree 20 are unchanged; it is not a nearest-neighbor or native-hardware claim.

## 2. Nominal clock, scalar phase and load reserve

For any chosen \(L\ge296\), set

\[
J_\star=\Lambda/80,\quad C=4J_\star=\Lambda/20,
\quad\alpha=\frac{2J_\star}{L+1},\quad
\kappa_r=\alpha\sqrt{r(L+1-r)},\quad r=1,\ldots,L.
\tag{3}
\]

The nominal structured coefficients and positive compensating occupations are precisely those of `b8bbfb7d`, scaled uniformly. Thus \(0<\kappa_r\le J_\star\). A diamond uses \(a_L=\kappa_{\rm left}/\sqrt2\), \(a_R=\kappa_{\rm right}/\sqrt2\), \(g=\kappa_{\rm middle}\), and potentials

\[
p_L=C-(2a_L+c_L),\quad p_R=C-(2a_R+c_R),
\quad p_A=C-(a_L+a_R+g)
\tag{4}
\]

on its terminals and equally on both arms. Hadamard, permutation and ordinary sites have respectively \(C-(\sqrt2t+c)\), \(C-(t+c)\), and \(C-(\kappa_{\rm left}+\kappa_{\rm right})\), with missing endpoint bonds zero. All are positive, since the subtracted expressions are at most \((\sqrt2+1)J_\star\) or \(2J_\star\). Identity contacts remain separately installed. No old \(\mu\) repair is added.

The checked physical arm map \(A\) and ordered data/rail gauge \(W\) give the **nominal** identity

\[
(AW)^*H_{\rm one}(AW)=h_L\otimes I,\qquad
h_L=CI-\sum_{r=1}^L\kappa_r
(|r\rangle\langle r-1|+|r-1\rangle\langle r|).
\tag{5}
\]

Its exact source profile is

\[
f_x(t)=e^{-iCt}\sqrt{\binom Lx}
[i\sin(\alpha t)]^x[\cos(\alpha t)]^{L-x}.
\tag{6}
\]

The cosine sign, the powers of \(i\), and the scalar phase are retained. There is no additional \(e^{-i\mu t}\). Formula (5) is a nominal comparator, not an asserted identity for \(\widetilde H\). Duhamel below pays the full physical difference, including any phase error, without fitting a new output phase. Head vacuum still has zero energy in both installations by the local hypotheses; \(CI\) describes the nominal one-head sector only.

Full-support load bounds are

\[
\begin{array}{c|c|c}
\text{vertex}&\text{nominal incident sum}&\text{maximum increase}\\\hline
\text{head}&(5+\sqrt2)J_\star&4\delta\\
Q\text{ or }P&40J_\star=\Lambda/2&20\delta\\
R&16J_\star=\Lambda/5&8\delta.
\end{array}
\tag{7}
\]

Every nominal sum is at most \(\Lambda/2\); hence \(20\delta\le\Lambda/2\) suffices for all full-support perturbed sums to be at most \(\Lambda\). This proves the cap part of (1). The argument uses \(\|h_b+E_b\|\le\|h_b\|+\delta\), not one-head expectations or cancellation of positive blocks. Positivity of changed blocks remains a distinct premise.

More generally, a nominal choice \(0<J_\star<\Lambda/40\) permits the common sufficient margin condition
\(\delta\le(\Lambda-40J_\star)/20\). The half-cap scale is one explicit convenient choice, not an optimal tradeoff. Reducing \(J_\star\) also lengthens the observation horizon and tightens its performance tolerance.

## 3. Why the evolution error has no volume factor

Let \(E=\sum_bE_b\) and \(d_i=\sum_{b\ni i}\|E_b\|\) for a physical head \(i\). On the global one-head sector, an onsite/head-data term contributes only at that head coordinate. A two-head term has a two-by-two head-coordinate block with each operator entry bounded by \(\|E_b\|\). When the head is outside its support the term vanishes, including its action on shared data. Thus each operator-valued head row of \(E_{\rm one}\) has sum of entry norms at most \(2\max_i d_i\). Self-adjointness gives the corresponding column bound, and the Schur/quadratic-form estimate yields

\[
\|E_{\rm one}\|\le2\max_i d_i\le8\delta.
\tag{8}
\]

This is the checked structured-source lemma with its hypotheses verified for this fixed block inventory. In particular, the shared data degree does not multiply (8), while it does enter the separate load margin (7). A data action on local head vacuum would invalidate the volume-independent reduction; it is expressly excluded.

Both evolutions preserve the one-head sector. With \(E_{\rm in}\) the supplied input isometry, Duhamel on that sector gives

\[
\|\widetilde A_t-A_t\|\le8\delta t=:\beta_t,
\quad \widetilde A_t=e^{-it\widetilde H}E_{\rm in},
\quad A_t=e^{-itH}E_{\rm in}.
\tag{9}
\]

This induced norm includes arbitrary passive references. It holds from preparation time 0, not only over the width of the eventual output window. For \(0\le t\le T_{\rm hor}\), (1) gives \(\beta_t\le\epsilon/32\). This is a coherent worst-case bound; no error rate, random walk or statistical cancellation is assumed.

## 4. Complete-output allocation and probability floor

Let an interval \(\mathcal I\subset[0,T_{\rm hor}]\) satisfy the **nominal** scalar tail condition

\[
q_0(t):=\sum_{x=0}^{74}|f_x(t)|^2\le\epsilon^2/1024,
\qquad t\in\mathcal I.
\tag{10}
\]

Both explicit recipes below obtain this by running the checked nominal certificate at accuracy \(\eta=\epsilon/2\). Let \(z_t\) be (6) restricted to \(75,\ldots,L\) and divided by its positive norm. The normalized complete target is the physical external-head embedding

\[
\mathcal V_t\xi=-z_t\otimes U_f\xi.
\tag{11}
\]

It retains the rail encoding, full phase, all ordinary data and arbitrary passive references. Every source/internal head is blank in the comparator. The nominal external part is \(\sqrt{1-q_0}\,\mathcal V_t\), with orthogonal complement, so

\[
\|A_t-\mathcal V_t\|^2
=2-2\sqrt{1-q_0}\le2q_0,
\qquad \|A_t-\mathcal V_t\|\le2\sqrt{q_0}\le\epsilon/16.
\tag{12}
\]

Consequently, uniformly on \(\mathcal I\),

\[
\|\widetilde A_t-\mathcal V_t\|
\le\epsilon/16+\epsilon/32=3\epsilon/32<\epsilon/8.
\tag{13}
\]

The unhalved stabilized complete-output channel distance is at most twice the isometry difference, hence \(3\epsilon/16<\epsilon/4\). This includes mixed inputs by purification and contraction. No physical postselection is used in this complete-channel conclusion.

Let \(\Pi_{\rm ext}\) project onto the physical external heads \(75,\ldots,L\), \(P_1\) onto actual record \(R=1\), and \(\Pi_{\rm joint}=\Pi_{\rm ext}P_1\). They commute. In the nominal blank-record evolution every external head has \(R=1\), so
\(\|(I-\Pi_{\rm joint})A_t\xi\|=\sqrt{q_0(t)}\)
for a unit encoded input, including a reference. Projection contraction and (9) prove

\[
\|(I-\Pi_{\rm joint})\widetilde A_t\xi\|
\le\sqrt{q_0}+\beta_t\le\epsilon/16,
\quad
\langle\Pi_{\rm joint}\rangle_{\widetilde A_t\xi}
\ge1-\epsilon^2/256.
\tag{14}
\]

Thus actual external probability and actual current-record probability are each at least this same floor as well. This does not identify the two events: record 1 can also occur in the internal final arms/origin, and perturbed external occupancy need not imply record 1 exactly. The joint bound explicitly pays both failures. Perturbed probabilities may depend on the logical/data input.

## 5. Explicit short-window policy

Choose any integer

\[
L\ge L_0(\epsilon):=\max\{296,\lceil4\log(32/\epsilon)\rceil\}.
\tag{15}
\]

For the nominal angular interval \([\pi/3,2\pi/3]\), the binomial position law has success parameter at least \(3/4\), and \(74\le L/4\). The checked centered-Bernoulli exponential estimate gives \(q_0\le e^{-L/2}\le\epsilon^2/1024\), establishing (10). With (3), the actual requested times and sufficient tolerance are

\[
\begin{split}
T&=\frac{\pi}{2\alpha}=\frac{20\pi(L+1)}\Lambda,\\
\mathcal I_0&=[2T/3,4T/3]
=\left[\frac{40\pi(L+1)}{3\Lambda},
        \frac{80\pi(L+1)}{3\Lambda}\right],\\
T_{\rm hor,0}&=\frac{80\pi(L+1)}{3\Lambda},\\
\delta_0(\epsilon,L)&=
\frac{3\epsilon\Lambda}{20480\pi(L+1)}.
\end{split}
\tag{16}
\]

For \(0\le\delta\le\delta_0\), the performance part of (1) is exactly satisfied. Also \(\delta_0<\Lambda/40\) for \(L\ge296\), \(\epsilon\le1\), so the load condition is automatic. There is no implicit maximum over unobserved future times. At \(T\), the nominal operation is exact with physical phase \(-e^{-iCT}i^L\); the perturbed operation is only bounded by (9), not declared perfect.

Taking \(L=L_0(\epsilon)\) gives this sufficient recipe:

\[
\begin{array}{c|c}
\text{quantity}&\text{chosen-family order as accuracy varies}\\\hline
\text{qubits and listed blocks}&\Theta(1+\log(1/\epsilon))\\
T,\ T_{\rm hor,0},\ |\mathcal I_0|
&\Theta(\Lambda^{-1}[1+\log(1/\epsilon)])\\
\delta_0&\Theta\!\left(\dfrac{\Lambda\epsilon}
                                  {1+\log(1/\epsilon)}\right).
\end{array}
\tag{17}
\]

The explicit floor 296 and counts \(4L+7\), \(8L+172\) remain in force; the least floor installation has 1191 qubits. These are orders of an explicit sufficient allowed-error ceiling, not lower bounds on required precision or upper bounds on errors a device could actually survive. For a fixed nonzero error ceiling \(\delta\), this particular certificate requires both (15) and
\(L+1\le3\epsilon\Lambda/(20480\pi\delta)\). More clock sites do not automatically improve a worst-case finite-time error certificate: the nominal tail decreases, while the elapsed perturbation budget grows.

## 6. Explicit adjustable-dwell policy

At nominal accuracy \(\eta=\epsilon/2\), the checked mean-threshold certificate uses

\[
m=\max\{148,8\log(1024/\epsilon^2)\},\quad
L\ge\max\{296,\lceil2m\rceil\},\quad
\theta=\arcsin\sqrt{m/L}\le\pi/4.
\tag{18}
\]

For \(X\sim\operatorname{Bin}(L,p)\), Markov applied to \(e^{-X}\) gives
\(\Pr(X\le74)\le\exp[74-(1-e^{-1})Lp]\le e^{-Lp/8}\)
when \(Lp\ge148\). Hence (10) holds throughout the closed interval below, because \(\sin^2(\alpha t)\ge m/L\):

\[
\begin{split}
t_{\rm arr}&=\frac{40(L+1)\theta}\Lambda,\\
t_{\rm end}=T_{\rm hor,d}
&=\frac{40(L+1)(\pi-\theta)}\Lambda,\\
D&=\frac{40(L+1)(\pi-2\theta)}\Lambda,
\qquad \mathcal I_d=[t_{\rm arr},t_{\rm end}],\\
\delta_d(\epsilon,L)
&=\frac{\epsilon\Lambda}
        {10240(\pi-\theta)(L+1)}.
\end{split}
\tag{19}
\]

For \(\delta\le\delta_d\), the performance budget is again exactly \(8\delta T_{\rm hor,d}\le\epsilon/32\). Since \(3\pi/4\le\pi-\theta<\pi\),

\[
\frac{\epsilon\Lambda}{10240\pi(L+1)}
<\delta_d\le
\frac{\epsilon\Lambda}{7680\pi(L+1)}<\Lambda/40.
\tag{20}
\]

Thus the load condition is automatic. The interval contains \(\mathcal I_0\) for the same \(L\). Its first endpoint is the first time this sufficient nominal mean condition holds, not an optimal or exact hitting time for the perturbed device. It is a time schedule certified for all admitted perturbations by the uniform comparison, without shifting the schedule to each particular realization.

For a requested relative dwell \(\mathcal R\ge2\), choose

\[
L_{\mathcal R}
=\left\lceil\max\left\{296,
 \frac{m}{\sin^2[\pi/(\mathcal R+2)]}\right\}\right\rceil,
\quad \theta_{\mathcal R}=\arcsin\sqrt{m/L_{\mathcal R}}.
\tag{21}
\]

This implies \(D/t_{\rm arr}=\pi/\theta_{\mathcal R}-2\ge\mathcal R\). The ratio describes the guaranteed output interval and its scheduled beginning, not continuous monitoring or the actual first successful detection. Concavity bounds on sine give

\[
\frac{m(\mathcal R+2)^2}{\pi^2}
\le L_{\mathcal R}
\le\frac{m(\mathcal R+2)^2}{4}+1.
\tag{22}
\]

Together with \(y\le\arcsin y\le\sqrt2y\) for \(y\le1/\sqrt2\), these prove the sufficient-recipe tradeoff

\[
\begin{split}
L_{\mathcal R}&=\Theta(m(\mathcal R+2)^2),\\
t_{\rm arr}&=\Theta(m(\mathcal R+2)/\Lambda),\\
D,\ T_{\rm hor,d}&=\Theta(m(\mathcal R+2)^2/\Lambda),\\
\delta_d(\epsilon,L_{\mathcal R})
&=\Theta\!\left(\frac{\Lambda\epsilon}
                         {m(\mathcal R+2)^2}\right).
\end{split}
\tag{23}
\]

Here \(m=\Theta(1+\log(1/\epsilon))\), including its fixed floor. The exact inventory gives qubits at most \(m(\mathcal R+2)^2+11\) and listed blocks at most \(2m(\mathcal R+2)^2+180\). In place of evaluating the exact \(\theta_{\mathcal R}\) tolerance, the simpler closed ceiling

\[
\delta\le\frac{\epsilon\Lambda}
 {2560\pi\,[m(\mathcal R+2)^2+8]}
\tag{24}
\]

is sufficient for the selected \(L_{\mathcal R}\). Indeed (22) implies
\(T_{\rm hor,d}<10\pi[m(\mathcal R+2)^2+8]/\Lambda\),
and substituting this upper bound in (1) proves (24). This closed formula does not automatically certify a still larger length: use the actual horizon in that case.

At fixed accuracy, increasing relative dwell costs quadratically more sites, a linearly later scheduled arrival, a quadratically larger horizon, and a quadratically smaller worst-case absolute error allowance. With a fixed nonzero \(\delta\), (24) can equivalently be read as the sufficient feasibility condition
\(m(\mathcal R+2)^2+8\le\epsilon\Lambda/(2560\pi\delta)\).
Neither this condition nor the exact tolerance in (19) is a necessary hardware or precision limit. Failure of this certificate does not refute operation of a particular perturbed installation.

## 7. Actual record normalization on the certified interval

The nominal record event has probability

\[
p_1^0(t)=|f_{73}(t)|^2+\sum_{x=74}^L|f_x(t)|^2
\ge1-q_0(t)\ge1-\epsilon^2/1024.
\tag{25}
\]

Coordinate 73 embeds as the antisymmetric physical arms of the final record diamonds, while 74 is their final origin. Its full normalized nominal branch is the positively normalized profile on these coordinates, carrying the same \(-U_f\) and the full phase of (6). This profile differs from the external comparator (11). An actual record event is not a test for internal vacancy.

For any normalized purified input let \(b=P_1A_t\xi\) and \(a=P_1\widetilde A_t\xi\). Then \(\|b\|=\sqrt{p_1^0}\), \(\|a-b\|\le\beta_t\), and (14) already gives the actual statewise floor \(\|a\|^2\ge1-\epsilon^2/256\). Adding and subtracting \(a/\sqrt{p_1^0}\), and using the reverse triangle inequality, yields

\[
\left\|\frac a{\|a\|}-\frac b{\sqrt{p_1^0}}\right\|
\le\frac{2\beta_t}{\sqrt{p_1^0}}
\le\frac{\epsilon}{16\sqrt{1-\epsilon^2/1024}}
<\epsilon/8.
\tag{26}
\]

Its unhalved trace-norm consequence is at most
\(\epsilon/[8\sqrt{1-\epsilon^2/1024}]<\epsilon/4\),
including retained passive references. The same reasoning for external-only or joint external/record projection compares to (11), since those nominal branches have probability \(1-q_0\). All these are statewise normalized-branch bounds on the certified interval. They do not define a linear normalized-postselection channel when the perturbed success probability depends on input; the channel bound in Section 4 concerns the unconditional complete output instead.

Outside the certified interval there is no uniform nominal probability floor from this policy. The general bound would be \(2\beta_t/\sqrt{p_1^0(t)}\) only when \(\beta_t<\sqrt{p_1^0(t)}\). No exact or uniformly accurate normalized rare-event theorem is inherited for independent errors, and a zero-probability nominal conditional state is undefined. The nominal member of the permitted class still returns at \(\pi/\alpha\); this finite-window policy supplies no permanent halt, capture, readout, reset or reuse mechanism. Exact recurrence at that precise time is not asserted for a general perturbed Hamiltonian.

## 8. Coefficient magnitudes versus sufficient error tolerances

The minimum nominal virtual hopping remains

\[
\kappa_{\min}=\frac{2J_\star\sqrt L}{L+1}
=\frac{\Lambda\sqrt L}{40(L+1)}.
\tag{27}
\]

It is an energy scale, not a tolerated error. For the exact performance ceilings (16) and (19), direct division gives

\[
\frac{\delta_0}{\kappa_{\min}}
=\frac{3\epsilon}{512\pi\sqrt L},\qquad
\frac{\delta_d}{\kappa_{\min}}
=\frac{\epsilon}{256(\pi-\theta)\sqrt L}.
\tag{28}
\]

Thus the allowed full-block absolute perturbation shrinks faster with clock length than the smallest hopping magnitude does. At the minimal short-window length its ratio to this magnitude is of order \(\epsilon/\sqrt{1+\log(1/\epsilon)}\); at the prescribed relative dwell it is of order \(\epsilon/[\sqrt m(\mathcal R+2)]\). These are properties of this sufficient norm certificate, not a necessity statement about manufacturing or optimal precision.

For errors that change only a fixed operator's scalar coefficient, the actual norm conversions are

\[
\|\Delta Q_s\|=2|\Delta a|,\qquad
\|\Delta[g n(I\mathbin{\pm}X)]\|=2|\Delta g|,
\qquad \|\Delta[p n]\|=|\Delta p|.
\tag{29}
\]

The contact formula includes an installed identity occupation \(2g n\); an omitted zero contact stays omitted. Consequently it suffices to keep each independently changed bond/contact coefficient within \(\delta/2\), and each compensating occupation within \(\delta\). Mixer bonds are individual signed \(Q\) blocks for this statement; their equality or original Hadamard ratio need not survive. Errors changing the target axis or other matrix entries must instead satisfy the full operator-norm hypothesis directly. A bound on one displayed scalar coefficient is not a bound on an arbitrary support matrix.

As a **separate fixed-form corollary**, these coefficient tolerances also preserve positivity if each block retains its original positive operator form. Every nominal bond weight is at least \(\kappa_{\min}/\sqrt2\), every nonzero contact parameter is at least \(\kappa_{\min}\), and every compensating occupation is at least \((3-\sqrt2)J_\star\). Equations (16), (19), and (28), with \(L\ge296\), \(\epsilon\le1\), give \(\delta/2<\kappa_{\min}/\sqrt2\) and \(\delta<(3-\sqrt2)J_\star\). Thus the changed scalar weights remain positive, their original fixed signs/supports remain, and local vacuum/conservation conditions follow from the forms. This verifies that the scalar-coefficient subclass is nonempty without presuming exact correlations. It does not establish positivity for general matrix-valued \(E_b\); that broader theorem retains the independent positivity premise in Section 1.

No extra free data terms, active historical Hamiltonian, passive-reference evolution, environmental coupling, input-state error or measurement apparatus is hidden in this tolerance. Each would require a separately paid extension. Known engineered-chain transfer is inherited and attributed in the checked parent; no new transfer mechanism or native coefficient-generation claim is made here.

## 9. Exact sources, exposure and open check

All paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`. These are the direct checked inputs; their frozen historical pending labels do not override the completed exact reviews and ROOT dispositions.

| File | Bytes | SHA-256 |
|---|---:|---|
| `exact_loader_structured_coefficients/PROPOSAL.md` | 23193 | `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2` |
| `exact_loader_structured_coefficients_check/REVIEW.md` | 13688 | `273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8` |
| `exact_engineered_clock_operation/PROPOSAL.md` | 11631 | `b8bbfb7d40c491aff6b893df6423b98e68edad91ef6596124dac10f3620c53f8` |
| `exact_engineered_clock_operation_check/REVIEW.md` | 15460 | `8351f91d29bbb570f8e9970962c2e0e24ea0db8dd06744d2180df761eae9272a` |
| `exact_engineered_clock_dwell_tradeoff/PROPOSAL.md` | 13645 | `d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25` |
| `exact_engineered_clock_dwell_tradeoff_check/REVIEW.md` | 5655 | `7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46` |

These six files were read completely and their byte counts/hashes refreshed for this derivation. An initial aggregate display truncated portions of the structured source/review and engineered source; the affected passages/files were reread in smaller untruncated outputs before use. The accepted global source `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946` and review `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6`, together with their diamond/corrected-matching ancestry, are transitive premises through these inputs. Their immediately preceding complete reads are reused; no older approximate-loader performance is imported.

ROOT proposed investigating a half-cap scale and applying the checked finite-horizon error lemma. The present author previously wrote the synthesis manuscript and separate approximate-loader/uniform-chain material. This new derivation is therefore source-exposed same-model author work with shared campaign ancestry, not an independent check of its premises. The new contribution is the explicit half-cap and accuracy allocation, supported-error success/record floors, two exact tolerance policies, and their length/dwell/coefficient tradeoff. The underlying norm lemma, exact scalar solution, binomial tail estimates and physical inventory are reused at their checked scopes.

A distinct check is still required for this **new** theorem, especially the budget constants, joint external/record probability estimate, normalization statement, half-cap scaling, and length-dependent tolerances. No acceptance of this source is inferred from the accepted parents or their number. The broader physical supply and realization gaps remain as stated.

Only this `PROPOSAL.md` was written. Work consisted of analytical derivation, complete source inspection, deterministic byte/hash bookkeeping, and text editing. No scientific executable, simulation, sweep, external search, delegation, Git/W/checkpoint/axiom/editable-prompt/model change, publication or retained-audit action occurred. No editable prompt file changed. The previously frozen manuscript was left unchanged.
