# Exact positive two-body loading with an engineered finite clock

Claim status: bounded_theorem. Selectively checked conditional analytical construction and finite-operation theorem. ROOT completed source and integration review; this is not formal retained audit status.

We describe a supplied, time-independent Hamiltonian built from real positive blocks acting on at most two qubits. On its one-head sector, a four-head diamond is exactly equivalent to a scalar chain carrying a prescribed real data involution. A sequence of 26 layers then implements an ordinary (Q/P) swap, a controlled logical-path operation and a record flip on the same shared data qubits. An ordered global unitary identity retains every physical arm and fixes the complete output phase. A correlated family of nonuniform coefficients preserves this identity while changing the scalar propagation.

The finite clock uses established engineered-chain state transfer to choose that scalar propagation. Its checked specialization supplies a complete external-output error at most \(\epsilon/8\), uniformly on a positive-width observation window, with an explicit sufficient apparatus of \(4L+7\) qubits and duration proportional to \(L/\Lambda\), where \(L\ge\max\{296,\lceil4\log(16/\epsilon)\rceil\}\). Current record correctness, external arrival and permanent halt remain different claims.

## 1. Physical premises and the complete operation

The moving head occupies one of four rails labelled \((a,b)\in\{0,1\}^2\). These are head-position labels, not extra physical data qubits. The ordinary qubits \(Q,P,R\) are shared throughout the graph. There is no free data Hamiltonian; arbitrary additional references are passive. The input has exactly one head on a supplied left endpoint, \(a=1\), arbitrary coherent logical path \(b\), arbitrary joint \(Q/P\) and passive-reference state, and \(R=0\). All other heads are vacant. Logical coherence across input endpoints is a supplied state, not an endpoint-preparation theorem.

Define the controlled path flip

\[
C_P^{(b)}=|0\rangle\langle0|_P\otimes X_b
                 +|1\rangle\langle1|_P\otimes I_b,
\qquad
U_f=I_a\otimes X_R C_P^{(b)}\operatorname{SWAP}_{QP}.
\tag{1}
\]

Products act right to left. On basis inputs the operation is

\[
(b,q,p,0_R)\longmapsto
       (b\mathbin{\oplus}(1-q),p_Q,q_P,1_R),
\tag{2}
\]

with \(a\) restored. Linearity preserves arbitrary correlations: the old \(P\) state and its passive-reference correlations move to \(Q\), rather than being discarded. This is not a theorem about loading an actively coupled historical processor or its Hamiltonian.

The premises include exact signed exchange blocks, paired head-data contacts, selective installed interactions, correlated coefficients across arms and rails, and the stated blank input apparatus. Positivity refers to each complete physical support, not merely its one-head restriction. The construction supplies a bounded-range graph; it does not identify these blocks with native microscopic interactions.

## 2. The exact diamond and its matched extension

For two head qubits define

\[
Q_s(i,j;a)=a\bigl[n_i+n_j-s(\sigma_i^+\sigma_j^-+
                                      \sigma_i^-\sigma_j^+)\bigr],
\quad s=\pm1,\quad a>0.
\tag{3}
\]

Its spectrum on the full two-qubit support is \(0,0,2a,2a\). For a real Hermitian involution \(X=X_D\) or \(Z_D\) on one ordinary data qubit, install on heads \(L,u,v,R_d\)

\[
\begin{split}
H_\diamond={}&Q_+(L,u;a)+Q_+(L,v;a)
 +Q_+(u,R_d;a)+Q_-(v,R_d;a)\\
&+g n_u(I+X)+g n_v(I-X),\qquad g>0.
\end{split}
\tag{4}
\]

Each contact is positive of norm \(2g\), on one head and one data qubit. All six blocks conserve head number and annihilate the entire head vacuum for every data state. The terminal \(R_d\) is a head coordinate, distinct from the record qubit \(R\).

In the one-head coordinates \(B=(u+v)/\sqrt2\), \(C=(u-v)/\sqrt2\), the exact matrix is

\[
\begin{pmatrix}
2aI&-\sqrt2aI&0&0\\
-\sqrt2aI&(2a+g)I&gX&0\\
0&gX&(2a+g)I&-\sqrt2aI\\
0&0&-\sqrt2aI&2aI
\end{pmatrix}_{L,B,C,R_d}.
\tag{5}
\]

Conjugation by \(\operatorname{diag}(I,I,X,X)\) makes this a scalar Jacobi matrix tensored with the data identity. This is an exact operator identity at every energy and time. It is an analytical change of basis on the one-head sector, not an installed circuit acting on the full many-head Hilbert space. Physical arms retain both prefix components; they are not themselves completed-gate outputs.

For uniform matching set \(a=J/\sqrt2\), \(g=J\), and \(\mu=(\sqrt2-1)J\). One ordinary \(Q_+(J)\) continuation at each terminal makes its diagonal \(2J+\mu\), equal to the two virtual arm diagonals. Add \(\mu n\) on each ordinary exterior head, with the actual source/cap diagonals treated explicitly; add no further \(\mu\) to diamond heads. A scalar sign change on \(C\) and the right extension makes every hopping \(-J\), and the physical right gate is then \(-X\). With \(h_0\) defined to have diagonal \(2J\), evolution is

\[
e^{-i\mu t}e^{-ith_0},
\tag{6}
\]

or equivalently evolution under \(h_0+\mu I\), with no second shift factor. This uses the corrected matching convention; the earlier ambiguous phase version is historical.

A two-rail Hadamard mixer uses four signed \(Q\) bonds of weight \(J/\sqrt2\), giving hopping matrix \(-JH_2\), with \(H_2=2^{-1/2}\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)\). Its one continuation per port gives the same scalar diagonal without an extra internal \(\mu\). A permutation mixer uses ordinary \(Q_J\) bonds and requires \(\mu n\) on its ports. One intermodule cable is one physical bond and supplies the endpoint occupation contribution at both ends. The identity diamond takes \(X=I\), retains \(2g n_u\), and omits the zero \(v\) contact; it has the same scalar propagation as a gated lane.

## 3. The ordered 26-layer loader

Let \(N_{D,a}=H_a\operatorname{CZ}_{a,D}H_a\), which flips the head label \(a\) when ordinary data \(D=1\). The chronological seven-layer module

\[
H_a,\operatorname{CZ}_{a,D},H_a,
\operatorname{CX}_{a,T},H_a,\operatorname{CZ}_{a,D},H_a
\tag{7}
\]

has logical word \(F_{D,T}=N_{D,a}\operatorname{CX}_{a,T}N_{D,a}\). It restores \(a\) and toggles \(T\) by \(a\oplus D\). Its three diamond layers contribute a fixed common minus. The three modules with \((D,T)=(Q,P),(P,Q),(Q,P)\) therefore implement \(-I_a\otimes\operatorname{SWAP}_{QP}\), for both values of \(a\). Explicitly,

\[
p_1=p\oplus a\oplus q,\qquad
q_2=q\oplus a\oplus p_1=p,\qquad
p_3=p_1\oplus a\oplus q_2=q.
\tag{8}
\]

Append \(H_b,\operatorname{CZ}_{b,P},H_b,X_b\), whose physical word is \(-C_P^{(b)}\), and then a final all-rail \(X_R\) diamond layer. The complete right-side word is exactly \(-U_f\). There are fourteen four-rail Hadamard layers, eleven four-diamond layers and one permutation layer. The graph keeps all 26 layers; no cancellation of adjacent Hadamards is used to alter its delay or inventory.

Rotate the arms of all 44 physical diamonds with a head-coordinate unitary \(A\). The resulting graph has 74 virtual positions \(x=0,\ldots,73\), each with the four-rail/shared-data fiber, and 73 successive links. Each forward block is \(-J V_x\), where \(V_x\) is the prescribed rail/data unitary. Define ordered prefixes

\[
W_0=I,\qquad W_{x+1}=V_xW_x,\qquad
W=\bigoplus_x W_x.
\tag{9}
\]

Then \(W_{x+1}^*(-JV_x)W_x=-JI\), so the entire matched one-head operator obeys

\[
(AW)^*H_{\rm one}(AW)=(h_0+\mu I)\otimes I.
\tag{10}
\]

This proof uses ordered products on the actual shared \(Q,P,R\); no control is duplicated and no noncommuting data gates are exchanged. Extend \(W=I\) on the left rays and \(W=-U_f\) on the right. For a scalar profile \(f=e^{-ith_0}|\text{source}\rangle\), the complete physical state is

\[
e^{-i\mu t}A\sum_x f_x(t)|x\rangle\otimes W_x\xi.
\tag{11}
\]

For example, inside a diamond with prefix \(W_{\rm pre}\), its physical arm amplitudes are

\[
\psi_u=(f_BW_{\rm pre}-f_CXW_{\rm pre})\xi/\sqrt2,
\quad
\psi_v=(f_BW_{\rm pre}+f_CXW_{\rm pre})\xi/\sqrt2.
\tag{12}
\]

All arm states and their correlations remain in (11). On matched infinite rays the exact eight-port scattering matrix, for \(0<k<\pi\), is

\[
S(k)=-e^{73ik}
\begin{pmatrix}0&U_f^*\\ U_f&0\end{pmatrix},
\qquad E(k)=\mu+2J(1-\cos k).
\tag{13}
\]

Reverse passage carries the adjoint ordered word. The delay is 73 graph edges, not the spatial separation of the installed qubits. The exact operator identity also applies to finite boundaries with their actual diagonal and hopping terms; (13) alone does not provide a finite transfer probability.

## 4. Correlated nonuniform coefficients preserve the gate

The checked structured family replaces uniform scalar matching by position-dependent positive hoppings and potentials. On every diamond in one layer, use the same \(a_L,a_R,g>0\) and nonnegative \(p_L,p_A,p_R\), with equal arm bonds at each end and the paired contacts \(g n_u(I+X),g n_v(I-X)\). The two ends may have different strengths. With actual adjacent cable weights \(c_L,c_R\), the transformed diagonal is

\[
d_L=2a_L+c_L+p_L,\quad
d_A=a_L+a_R+g+p_A,\quad
d_R=2a_R+c_R+p_R,
\tag{14}
\]

and the scalar segment has hoppings \(-\sqrt2a_L,-g,-\sqrt2a_R\) and diagonal \((d_L,d_A,d_A,d_R)\). Equal potentials on the two physical arms and the same parameters on all four lanes are part of the sufficient construction. Identity and gated diamonds have identical scalar segments.

A Hadamard link with parameter \(t\) uses bonds \(t/\sqrt2\) and endpoint diagonal \(\sqrt2t+c+p\). A permutation link uses bonds \(t\) and diagonal \(t+c+p\). Cables and ordinary onsite potentials are scalar and common across rails. Therefore, after the same \(A,W\),

\[
(AW)^*H_{\rm one}(AW)=h_{\rm str}\otimes I,
\quad
h_{\rm str}=\sum_xd_x|x\rangle\langle x|
-\sum_xw_x(|x+1\rangle\langle x|+\mathrm{h.c.}).
\tag{15}
\]

Every \(w_x>0\); the diagonals are those actually supplied by (14) and the other blocks. This is not a realization theorem for arbitrary independently prescribed Jacobi diagonals. Identical scalar endpoints on all four rails give the literal tensor product. Permitted unequal unused-rail terminations require the qualified direct-sum statement in the source, rather than (15) on all rails.

The full scalar phase now belongs in \(f=e^{-ith_{\rm str}}|\text{source}\rangle\). A common shift may be extracted once if it is actually present. The output prefix remains \(-U_f\), but arbitrary members can reflect or trap amplitude and need not retain the transmission phase (13). Exact gate factorization does not supply useful success probability by itself.

## 5. Current record, external arrival and return

Only the final four diamonds touch \(R\). In the original unshifted coordinates their virtual positions are \(70=L,71=B,72=C,73=R_d\), with

\[
W_{70}=W_{71}=G_{\rm pre},\qquad
W_{72}=W_{73}=-U_f,
\quad G_{\rm pre}=I_a\otimes C_P^{(b)}\operatorname{SWAP}_{QP}.
\tag{16}
\]

For initially blank \(R\), projection onto \(R=1\) removes the unfinished \(f_{71}\) arm term exactly. Let \(\mathcal J_{\rm rec}\) embed virtual position 72 as the physical antisymmetric final-arm combination \((|u\rangle-|v\rangle)/\sqrt2\) on each output rail, and positions \(x\ge73\) as their physical heads. Using the full structured scalar phase in \(f\),

\[
P_{R=1}e^{-itH}E_{\rm in}
=-\mathcal J_{\rm rec}
 \left[\left(f_{72}|72\rangle+\sum_{x\ge73}f_x|x\rangle\right)
 \otimes U_f\right].
\tag{17}
\]

Here the rail label remains part of the physical head encoding; it is not traced away. The branch probability is \(|f_{72}|^2+\sum_{x\ge73}|f_x|^2\), independent of the supplied data/reference state. Whenever it is nonzero, its normalized complete encoded branch has exactly the operation \(U_f\), even if the event is rare. This exact factorization uses blank \(R\), no earlier record contact, no free record dynamics and the stated coefficient correlations.

The **external-only** event instead begins at \(x\ge74\). It has its own common scalar profile and exactly the same logical word, while also placing the head outside every internal module. The event \(R=1\) may occupy the final internal arms or origin, so it does not certify that external-only apparatus state. At zero event probability its normalized conditional state is undefined. Returns can erase the record and undo the operation: neither event establishes permanent halt, capture, reset or reuse.

## 6. A finite engineered clock with positive compensation

The engineered-chain transfer mechanism is established work: Christandl, Datta, Ekert and Landahl identify square-root couplings with a spin rotation in equations (12)–(15) of [*Perfect state transfer in quantum spin networks*, Phys. Rev. Lett. 92, 187902 (2004)](https://arxiv.org/pdf/quant-ph/0309131). We use that mechanism with the negative-hopping convention below. Its positive-block realization in this loader, full-output window and physical inventory are the separate checked adaptation; no novelty is claimed for engineered perfect transfer itself.

Fix \(0<\epsilon\le1\), an incident cap \(\Lambda>0\), and an integer

\[
L\ge\max\{296,\lceil4\log(16/\epsilon)\rceil\},\quad
J_\star=\Lambda/40,\quad
\alpha=\frac{2J_\star}{L+1},\quad C=4J_\star,
\qquad
\kappa_r=\alpha\sqrt{r(L+1-r)},\quad r=1,\ldots,L.
\tag{18}
\]

These are supplied exact positive coefficients, with \(0<\kappa_r\le J_\star\). Shift the 74 internal positions to \(1,\ldots,74\), add one left endpoint at 0 and a right output chain at \(75,\ldots,L\), on **all four rails**. The four scalar chains are identical, including unused input rails. The actual input is the endpoint seed at 0 with the logical/data embedding of Section 1. There is no weak emitter, preformed momentum packet or timed loading step in this installation.

Assign each virtual link its corresponding \(\kappa_r\) through the structured family: diamond outer bonds use \(a_L=\kappa_{\rm left}/\sqrt2\), \(a_R=\kappa_{\rm right}/\sqrt2\), its paired contacts use \(g=\kappa_{\rm middle}\), a Hadamard mixer uses \(t=\kappa_{\rm link}\), and a permutation or cable uses its corresponding ordinary weight. Repeat each layer's parameters over all four rails. Add one physical occupation potential per head:

| Head type | Added positive occupation coefficient |
|---|---|
| Diamond left/right terminal | \(p_L=C-(2a_L+c_L)\), \(p_R=C-(2a_R+c_R)\) |
| Both arms of a diamond | \(p_A=C-(a_L+a_R+g)\), equal on \(u,v\) |
| Hadamard port | \(p=C-(\sqrt2t+c)\) |
| Permutation port | \(p=C-(t+c)\) |
| Ordinary head, including endpoints | \(p=C-(\kappa_{\rm left}+\kappa_{\rm right})\), with a missing bond set to zero |

Every subtraction in this definition is smaller than \(C\): the largest module expression is at most \((\sqrt2+1)J_\star\), and ordinary sites require at most \(2J_\star\). Thus all installed potentials are strictly positive. Identity diamonds retain their separate \(2g n_u\) contact and omitted zero \(v\) contact before the common arm compensation is added. The former eight permutation \(\mu\) repairs are replaced by these potentials, not added again.

The exact full one-head reduction is consequently

\[
(AW)^*H(AW)=h_L\otimes I,\qquad
h_L=CI-\sum_{r=1}^L\kappa_r
(|r\rangle\langle r-1|+|r-1\rangle\langle r|).
\tag{19}
\]

Here \(C\) is the entire scalar diagonal. There is **no additional** \(e^{-i\mu t}\) factor from the uniform-matching example. Head vacuum still has zero energy because every physical block annihilates it; \(CI\) in (19) is a one-head statement.

To solve the scalar problem, identify \(|x\rangle\) with the normalized symmetric weight-\(x\) vector of \(L\) mathematical spins. On that symmetric subspace, \(\sum_jX_j\) has neighboring matrix element \(\sqrt{(x+1)(L-x)}\), so \(h_L=CI-\alpha\sum_jX_j\). These spins are an algebraic representation, not installed ancillas. The commuting factors give the exact common profile

\[
f_x(t)=e^{-iCt}\sqrt{\binom Lx}
       [i\sin(\alpha t)]^x[\cos(\alpha t)]^{L-x}.
\tag{20}
\]

The sign of \(\cos(\alpha t)\) is retained in the amplitude, including the second half of the observation window. The coefficients have total squared norm one. At

\[
T=\frac{\pi}{2\alpha}=\frac{10\pi(L+1)}{\Lambda},
\tag{21}
\]

the only nonzero coefficient is \(f_L(T)=e^{-iCT}i^L\). The complete physical endpoint amplitude is therefore \(-e^{-iCT}i^L U_f\), with the fixed global minus and all data/reference outputs retained.

## 7. Complete output throughout a positive-width window

Use the closed interval

\[
\mathcal I=\left[\frac{\pi}{3\alpha},\frac{2\pi}{3\alpha}\right]
          =[2T/3,4T/3].
\tag{22}
\]

For every \(t\in\mathcal I\), the scalar position law is binomial with \(p=\sin^2(\alpha t)\ge3/4\). External output begins at 75; all source and internal coordinates are in the bad set \(0,\ldots,74\). Since \(L\ge296\), this set lies below \(L/4\), at least \(L/2\) below the mean. The centered log moment generating function of a Bernoulli variable has second derivative at most \(1/4\), hence is at most \(s^2/8\). Markov's bound at \(s=-2\) therefore gives, uniformly on the entire window,

\[
q(t):=\sum_{x=0}^{74}|f_x(t)|^2
\le e^{-L/2}\le\epsilon^2/256.
\tag{23}
\]

This includes all internal arms after the unitary map \(A\); it is not a bound only on a selected successful component. No source residual or localized spectral part is omitted.

Let \(z_t\) be the restriction of (20) to \(75,\ldots,L\), divided by its positive norm \(\sqrt{1-q(t)}\). It includes the full phase \(e^{-iCt}\), the powers of \(i\), and the signs of the cosine. On those physical external heads \(A\) is the identity and \(W=-U_f\). The normalized complete comparison isometry is the fixed physical embedding of

\[
\mathcal V_t\xi=-z_t\otimes U_f\xi.
\tag{24}
\]

This notation retains the output rail as the logical head encoding. It does not trace all head degrees of freedom away. All source/internal heads are vacant in the comparator, and every ordinary data qubit and passive reference is retained.

The actual external part equals \(\sqrt{1-q}\,\mathcal V_t\xi\); its complement is orthogonal in head support. Thus, for every normalized encoded input and arbitrary passive reference,

\[
\|(e^{-itH}E_{\rm in}-\mathcal V_t)\xi\|^2
=q+(1-\sqrt{1-q})^2=2-2\sqrt{1-q}\le2q.
\tag{25}
\]

In particular the conservative isometry-norm bound is \(2\sqrt q\le\epsilon/8\), and the unhalved stabilized complete-channel distance is at most \(\epsilon/4\). External success probability is at least \(1-\epsilon^2/256\). These are complete-state and channel estimates, not normalized rare-branch approximations. At \(T\) the external transfer is exactly complete. The comparator's positive normalization is a mathematical definition, not a physical postselection or preparation step.

The shifted actual-record formula has the antisymmetric arm coordinate at 73 and the final origin at 74. Its probability is

\[
p_{R=1}(t)=|f_{73}(t)|^2+\sum_{x=74}^L|f_x(t)|^2,
\tag{26}
\]

with the same exact \(U_f\) branch factorization as (17). It is at least the external probability during \(\mathcal I\). At other times the record branch is still exact whenever nonzero under the exact-family premises, but can be rare or absent; its apparatus profile includes the internal arms/origin. The finite coherent clock returns and can undo the prefix, so (22) is a finite observation window, not permanent storage.

All resource counts below are for the installed physical qubits and separate positive blocks:

| Quantity | Exact count or sufficient bound |
|---|---|
| Fixed interior | 296 heads and 3 ordinary data qubits |
| Interior blocks before compensation | 392 head-head bonds, 48 head-data contacts, 20 identity occupations: 460 total |
| Interior after one compensation per head | 756 blocks |
| Exterior heads, bonds, and potentials | \(4L-292\) of each |
| Complete apparatus | \(4(L+1)\) heads, \(4L+7\) qubits, \(8L+172\) blocks |
| Full-support incident load at a head | at most \((5+\sqrt2)J_\star\) |
| Full-support incident load at \(Q,P\) | at most \(40J_\star=\Lambda\) each |
| Full-support incident load at \(R\) | at most \(16J_\star\) |

For example a compensated diamond endpoint has incident load \(4a+2c+p=C+2a+c\); an arm has \(C+a_L+a_R+g\). The same head ceiling covers Hadamard ports, while permutation and ordinary heads require at most \(6J_\star\). The \(Q/P\) loads count all twenty contacts per qubit even though only one head is present. Scalar cancellations do not reduce physical load accounting.

The 299 interior qubits fit in the explicitly checked \(7^3\) cube with eight reserved top-face ports. Distinct vertical exterior rays preserve noncollision; new ray bonds have range one, and unchanged interior pairs have Manhattan range at most 18. This is a supplied range-18 embedding, not an unchanged nearest-neighbor realization: \(Q/P\) still have degree 20. Uninstalled spatial adjacency does not create a coupling.

Taking the least allowed integer \(L\) gives sufficient size \(O(1+\log(1/\epsilon))\) and window times \(O(\Lambda^{-1}[1+\log(1/\epsilon)])\), with the explicit floor 296. At that floor there are 1191 physical qubits. The window width is \(2T/3>0\). These are upper-bound recipes for the newly supplied exact clock, not optimal exponents, measured operation times or evidence that previous approximate resource bounds were necessary.

## 8. A tunable finite dwell interval

A checked extension permits a longer completed-output interval relative to its first certified arrival, while paying for a larger clock and a later arrival. Define

\[
m_\epsilon=\max\{148,8\log(256/\epsilon^2)\},\qquad
L\ge\max\{296,\lceil2m_\epsilon\rceil\},\qquad
\theta=\arcsin\sqrt{m_\epsilon/L}\le\pi/4.
\tag{27}
\]

For \(X\sim\operatorname{Bin}(L,p)\) and \(m=Lp\), Markov applied to \(e^{-X}\) gives
\(\Pr(X\le74)\le\exp[74-(1-e^{-1})m]\le e^{-m/8}\) when \(m\ge148\). Thus the same complete target (24), vector/channel errors and external-success bound hold uniformly on

\[
[t_{\rm arr},t_{\rm end}]
=\left[\frac\theta\alpha,\frac{\pi-\theta}\alpha\right],
\qquad
D=\frac{\pi-2\theta}\alpha,\qquad
\frac D{t_{\rm arr}}=\frac\pi\theta-2.
\tag{28}
\]

This interval contains the base window (22). Its first endpoint is the first time this sufficient mean condition is met, not the exact earliest high-success time.

For a requested relative ratio \(\mathcal R\ge2\), an explicit choice is

\[
L_{\mathcal R}=\left\lceil\max\left\{296,
 \frac{m_\epsilon}{\sin^2[\pi/(\mathcal R+2)]}\right\}\right\rceil.
\tag{29}
\]

It ensures \(D/t_{\rm arr}\ge\mathcal R\) with the same incident cap and physical family. In particular,

\[
\frac{m_\epsilon(\mathcal R+2)^2}{\pi^2}
\le L_{\mathcal R}\le\frac{m_\epsilon(\mathcal R+2)^2}{4}+1.
\tag{30}
\]

The exact arrival and dwell are (28). The inequalities
\(y\le\arcsin y\le\sqrt2y\) for \(y\le1/\sqrt2\), and
\(\pi(L+1)/(4J_\star)\le D<\pi(L+1)/(2J_\star)\), give the sufficient-recipe orders

\[
\begin{split}
L_{\mathcal R}&=\Theta(m_\epsilon(\mathcal R+2)^2),\\
t_{\rm arr}&=\Theta(m_\epsilon(\mathcal R+2)/J_\star),\\
D&=\Theta(m_\epsilon(\mathcal R+2)^2/J_\star).
\end{split}
\tag{31}
\]

Here \(m_\epsilon=\Theta(1+\log(1/\epsilon))\) and \(J_\star=\Lambda/40\). Substitution into the exact inventory gives at most \(m_\epsilon(\mathcal R+2)^2+11\) qubits and \(2m_\epsilon(\mathcal R+2)^2+180\) blocks. At fixed accuracy the hardware and dwell grow quadratically in the requested ratio, while certified arrival grows linearly. This is not a speedup at fixed arrival or hardware, and the endpoint hopping decreases as the clock grows. These sufficient costs are not optimality bounds.

The same clock returns exactly at \(t=\pi/\alpha\): its scalar state is \(e^{-iC\pi/\alpha}(-1)^L|0\rangle\), with zero external-output probability and identity source gauge. The interval (28) ends \(t_{\rm arr}\) before that return. Arbitrarily large finite relative dwell is therefore compatible with recurrence, not permanent halt. A fixed finite \(L\) can still transfer exactly at \(T\) even if a more stringent broad-window prescription fails; this certificate does not rule out narrower windows.

## 9. Precision, suppliers and excluded conclusions

The minimum engineered hopping is \(2J_\star\sqrt L/(L+1)\). That is a coefficient magnitude, not a manufacturing tolerance. The square-root values, equality of scalar rails, equality of both arms at each end, paired contact coefficients and compensating potentials are supplied exactly. The structured family allows correlated changes that preserve the gauge, but their new scalar propagation need not preserve this observation window. Independent asymmetries generally destroy the exact gate identity.

A separately checked finite-horizon perturbation statement is available only under its actual hypotheses: self-adjoint changes on the same listed supports, local head-number conservation, annihilation of local head vacuum for every data value, independently supplied positivity of changed blocks, and incident-load margin. With at most four blocks at a physical head and error at most \(\delta\) per listed block, it gives complete vector error at most \(8\delta T_{\rm hor}\), and a cap margin \(20\delta\) suffices. The nominal choice \(J_\star=\Lambda/40\) supplies no such extra margin by assertion. Small unstructured errors do not preserve exact all-time rare-event correctness; normalized approximate branch bounds require a success-probability floor. No generic fabrication or native-precision guarantee is claimed here.

The theorem does not supply endpoint coherence, blank heads or \(R=0\), active historical system dynamics, autonomous cooling, environment capture, an irreversible readout, reset/reuse or permanent halt. Its new performance follows from the explicit exact scalar identity and engineered coefficients, not from an earlier approximate scattering theorem. Separate uniform-chain, active-energy and environment continuations are outside this manuscript's theorem and evidence scope.

## 10. Source map, proof status and exposure

The canonical destination is `docs/EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md`. The following links resolve from this canonical note into `outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/`. Each row identifies the complete original file to preserve unchanged. The local originals lie under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/` at the directory and filename in the link.

| Complete source or analytical check | Bytes | SHA-256 |
|---|---:|---|
| [Diamond proposal](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_diamond/PROPOSAL.md) | 5208 | `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33` |
| [Diamond review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_diamond_check/REVIEW.md) | 12143 | `da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945` |
| [Corrected matched-extension proposal](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_matched_extension/PROPOSAL.md) | 5733 | `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e` |
| [Matched-extension review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_gate_matched_extension_check/REVIEW.md) | 10895 | `36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f` |
| [Global 26-layer composition](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition/PROPOSAL.md) | 23893 | `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946` |
| [Global-composition review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition_check/REVIEW.md) | 14485 | `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6` |
| [Structured coefficient family](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients/PROPOSAL.md) | 23193 | `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2` |
| [Structured-family review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_loader_structured_coefficients_check/REVIEW.md) | 13688 | `273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8` |
| [Engineered finite-clock operation](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_operation/PROPOSAL.md) | 11631 | `b8bbfb7d40c491aff6b893df6423b98e68edad91ef6596124dac10f3620c53f8` |
| [Engineered-clock review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_operation_check/REVIEW.md) | 15460 | `8351f91d29bbb570f8e9970962c2e0e24ea0db8dd06744d2180df761eae9272a` |
| [Finite dwell tradeoff](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff/PROPOSAL.md) | 13645 | `d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25` |
| [Dwell-tradeoff review](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff_check/REVIEW.md) | 5655 | `7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46` |

The load-bearing dependency order is local diamond, corrected matching and ordered global composition, structured scalar family, engineered finite clock, then its dwell certificate. The local matched identity alone does not prove the global word; stationary transmission alone does not prove the finite-window estimate. The structured family supplies the physical coefficient prescription, and the explicit finite scalar propagator supplies the new performance. The corrected matched source and its review control the scalar phase; the earlier matching draft is historical and is not an operative premise. PR9734 is genealogical ancestry only, with no earlier approximate performance imported into this theorem.

All six pairs have scoped support and ROOT acceptance at their exact pinned identities. The reviews establish conditional mathematical claims for the stated blocks and inputs, not native realization, preparation, experiment or retained audit status. They are source-exposed reviews within a shared research campaign, including shared authorship of earlier premises; they are not claimed to be blind or independent of that ancestry. Historical pending labels in frozen source bodies are superseded only for the exact source/check identities above. ROOT fully read the assembled manuscript and compared it with the accepted argument/check pairs; this integration check adds no independent proof evidence.

For this manuscript, the drafting worker read all twelve files above completely, including the corrected matching argument, the full global physical-arm and phase identities, the structured-family restrictions, and the two finite-clock reviews. The primary Christandl–Datta–Ekert–Landahl paper was inspected specifically at its engineered-chain construction and transfer equations (12)–(15), not represented as a full-paper review. Its known transfer mechanism is attributed in Section 6. The writer also has authorship exposure to earlier approximate-loader and separate uniform-chain work; none of those separate performance claims is used here.
