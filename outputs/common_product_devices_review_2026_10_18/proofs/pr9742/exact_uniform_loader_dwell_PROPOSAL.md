# Adjustable finite dwell for the exact uniform loader with longer output rays

2026-10-18. **New conditional author derivation; distinct check required.** The checked symmetric uniform-loader and scalar-source pairs remain the premises identified in Section 8. This note changes the four right ray lengths and proves the full comparison over the resulting longer horizon. It does not simply extend the old finite-window conclusion.

For the old accuracy prescription \(\ell(\epsilon),\rho(\epsilon)\), keep the four left rays of length \(\ell\), their two selected weak sources, and the same \(J=\Lambda/40\). Give all four right rays any finite integer length \(M\ge\ell\). The proposed theorem proves the same complete-vector ceiling \(13\epsilon/256\) on

\[
\mathcal I_{\ell,M}=
\left[\frac{3\ell}{4J},\frac{7(\ell+M)}{16J}\right].
\tag{1}
\]

For any requested relative dwell \(\mathcal R\ge1/6\), choosing
\[
M_{\mathcal R}=
\left\lceil\frac{(12\mathcal R+5)\ell}{7}\right\rceil
\tag{2}
\]
gives dwell at least \(\mathcal R\) times the unchanged scheduled arrival \(3\ell/(4J)\). The physical counts are \(301+4(\ell+M)\) qubits and \(478+8(\ell+M)\) positive blocks. Thus the selected family costs linearly in \(\mathcal R+1\) at fixed accuracy. This is a sufficient construction under exact coefficient and preparation supplies, not optimality, a generic error tolerance, native active-system realization or permanent halt.

## 1. Literal asymmetric finite installation and input

Use the checked matched 26-layer loader, its 296 internal heads, 468 internal positive blocks and shared ordinary data qubits \(Q,P,R\). The four virtual rail labels are \((a,b)\), encoded in head positions. Put
\[
J=\Lambda/40,\qquad \mu=(\sqrt2-1)J,\qquad
\gamma=\rho J,\qquad 0<\rho\le1/2.
\tag{3}
\]
Attach \(\ell\) ordinary heads to each of the four left origins and \(M\) ordinary heads to each of the four right origins, by respectively \(\ell\) and \(M\) ordinary \(Q_J\) bonds. For two heads define the positive real block
\[
Q_c(v,w)=c[n_v+n_w-(\sigma_v^+\sigma_w^-+
                             \sigma_v^-\sigma_w^+)],\qquad \|Q_c\|=2c .
\tag{4}
\]
At each left \(a=1\) endpoint add one source \(s\), at distance \(\ell+1\), with the combined positive block
\[
B=Q_\gamma(s,v_\ell)+(2J-\gamma)n_s+(J-\gamma)n_{v_\ell}.
\tag{5}
\]
The two unused left rays end with \(Jn_{v_\ell}\), and the four right rays end with \(Jn_{v_M}\). Add \(\mu n_v\) to every added exterior head, including the sources. Do not add this shift again at internal diamond/mixer heads; the eight internal permutation occupations are already in the 468-block inventory.

The source one-head matrix is \(\left(\begin{smallmatrix}2J&-\gamma\\-\gamma&J\end{smallmatrix}\right)\); its determinant is \(2J^2-\gamma^2>0\), and its full two-qubit norm is \(3J\), including the doubly occupied eigenvalue. The preceding ordinary bond supplies the other \(J\) at \(v_\ell\). Caps supply the missing endpoint \(J\). Consequently every scalar one-head diagonal is exactly \(2J+\mu\), and only the source hopping has magnitude \(\gamma\) instead of \(J\). All listed physical blocks are positive on their full support and annihilate head vacuum.

The supplied input \(E\) is a single head coherently encoded in the two \(a=1\) source endpoints, arbitrary logical \(b\), arbitrary joint \(Q/P\) and passive-reference state, \(R=0\), and all other heads vacant. There is no additional free data or reference Hamiltonian. The source coherence, empty apparatus, exact coefficients, selective supports and isolation are explicit supplies.

The checked ordered operation and its right-prefix sign are
\[
U_f=I_a X_R C_P^{(b)}\operatorname{SWAP}_{QP},\qquad
C_P^{(b)}=|0\rangle\langle0|_P X_b+|1\rangle\langle1|_P I_b,
\qquad W_{\rm right}=-U_f .
\tag{6}
\]
Thus \((b,q,p,0)\mapsto(b\oplus(1-q),p,q,1)\), with old \(P\) and its reference correlations moved to \(Q\). Rail labels do not duplicate ordinary data. Every head, all three ordinary qubits and all passive references remain in the output comparison.

### Exact finite scalar identification

Let \(A,W\) be the fixed physical-arm rotation and ordered gauge of the checked global source. Their internal conjugacy is unchanged. On every left extension \(W=I\), so the selected-source and unused-cap terminations remain diagonal in \(a\). On the right \(W=-U_f\) is constant; all four right terminations have the same new length and identical blocks, so they commute through that gauge. There is no requirement that a right length equal a left length.

After conjugation, the finite Hamiltonian is a direct sum of scalar clocks indexed by \(a,b\). The two selected \(a=1\) clocks are identical. The two \(a=0\) clocks have no weak source and a different left endpoint, but are unpopulated by the transformed input. The invariant physical input sector is the image under \(AW\) of the selected virtual sector; it is not the set of physically \(a=1\) internal head coordinates.

The internal virtual positions remain \(x=0,\ldots,73\). Set
\[
K=74,\quad S=\ell+M,\quad N=S+K-1,\quad n=x+\ell .
\tag{7}
\]
The source at \(x=-\ell-1\) is \(s\), the first ordinary left site is \(n=0\), and the cap at \(x=73+M\) is \(n=N\). The actual external output is
\[
F_M=\{\ell+K,\ldots,S+K-1\},
\tag{8}
\]
with exactly \(M\) sites. It is \(x=74,\ldots,73+M\), not the final internal origin.

Each selected scalar clock is the literal operator
\[
H_{\ell,M}
=B+\sum_{n=0}^{N-1}Q_J(n,n+1)+Jn_N
                 +\mu\sum_{v=s,0,\ldots,N}n_v .
\tag{9}
\]
It has \(S+K+1\) head coordinates and \(S+K\) source-to-cap edges. The identification includes the actual source, cap, shift and every unused physical coordinate. At the selected source \(AW=I\), and on \(F_M\), \(AW=-U_f\). The proof below treats (9) directly.

## 2. Reused exact source, cutoff and numerical constants

For the corresponding semi-infinite one-head operator \(H_\infty^0\) with no \(\mu I\), put \(u=Jt\), \(e(k)=2(1-\cos k)\), and
\[
F_{\rm src}(k)=
\frac{-i\sqrt{2/\pi}\rho\,e^{ik}}
     {(2-\rho^2)\cot k-i\rho^2},\qquad
w(k)=|F_{\rm src}(k)|^2,\qquad \int_0^\pi w(k)\,dk=1.
\tag{10}
\]
The checked standalone spectral identity is
\[
\begin{split}
e^{-itH_\infty^0}|s\rangle&=A(t)|s\rangle+
                              O_tF_{\rm src}+I_t\overline{F_{\rm src}},\\
(O_tf)_n&=(2\pi)^{-1/2}\int_0^\pi e^{ink-iue(k)}f(k)\,dk,\\
(I_tf)_n&=(2\pi)^{-1/2}\int_0^\pi e^{-ink-iue(k)}f(k)\,dk,\quad n\ge0,\\
A(t)&=\int_0^\pi e^{-iue(k)}w(k)\,dk .
\end{split}
\tag{11}
\]
This is a complete normalized source identity, including the emitter and exact spatial phase. It is not a normalized incoming-state assumption.

Use the same real cutoff: \(\chi=1\) on \(|k-\pi/2|\le h/2\), \(\chi=0\) beyond \(3h/4\), and \(\chi=1-10z^3+15z^4-6z^5\) on each width-\(h/4\) transition, with \(z=4(|k-\pi/2|-h/2)/h\). It is \(C^2\cap W^{3,1}\), with the required matching traces. Assume \(\rho^2\le h\le10^{-3}\) and \(P:=3\rho^2/h<1/2\). The exact positive normalization and filtered state are
\[
\begin{split}
p&=\|\chi F_{\rm src}\|_2^2\ge1-P>1/2,\qquad
g=\chi F_{\rm src}/\sqrt p,\qquad \|g\|_2=1,\\
\Phi_\chi(t)&=e^{-itH_\infty^0}\chi(H_\infty^0)|s\rangle/\sqrt p\\
 &=A_\chi(t)|s\rangle+O_tg+I_t\bar g,\qquad \|\Phi_\chi(t)\|=1,\\
A_\chi(t)&=p^{-1/2}\int_0^\pi \chi(k)w(k)e^{-iue(k)}\,dk,\\
\||s\rangle-\Phi_\chi(0)\|&\le\sqrt P+P\le2\sqrt P .
\end{split}
\tag{12}
\]
The actual emitter integrand contains one \(\chi\). This seed comparison is paid once; it is not integrated over the longer horizon, and its source state and constant are independent of \(M\).

For completeness, the unchanged scalar pole constants are the following fixed numbers:
\[
a_0=23/100,\quad (B_2,B_3,B_4)=(64,512,2048),\quad
(D_0,D_1,D_2,D_3)=(2,24,394,6280),
\]
\[
\begin{split}
P_\star={}&D_3/a_0^3+6B_2D_2/a_0^4
 +(4B_3/a_0^4+15B_2^2/a_0^5)D_1\\
 &+(B_4/a_0^4+10B_2B_3/a_0^5+15B_2^3/a_0^6)D_0,\\
Q_\star={}&D_3/(2a_0^2)+2B_2D_2/a_0^3
 +(4B_3/(3a_0^3)+15B_2^2/(4a_0^4))D_1\\
 &+(B_4/(3a_0^3)+10B_2B_3/(4a_0^4)+3B_2^3/a_0^5)D_0,\\
D_\star={}&4P_\star+20Q_\star .
\end{split}
\tag{13}
\]
They are the scalar-coefficient \(1\) specialization; their \(D_r\) arise from the derivative tuple \((1,2,7,30)\) and the actual quintic cutoff. They contain no \(\ell,M,\rho\) dependence.

The real-axis pole mechanism fixes the two signs. With \(x=\tan(k-\pi/2)\), \(A_0=2-\rho^2\), \(b_0=\rho^2/A_0\),
\[
F_{\rm src}(k(x))=
\frac{i\sqrt{2/\pi}\rho e^{ik(x)}}{A_0(x+ib_0)},\qquad
(x+ib_0)^{-1}=-i\int_0^\infty e^{ixv-b_0v}\,dv .
\tag{14}
\]
The outgoing \(F_{\rm src}\) adds \(+vx\), while its incoming conjugate adds \(-vx\). The cutoff amplitude has third weak derivatives in \(L^1\), bounded by \(D_r/h^2\). Three real integrations by parts have absolute coefficients \(1,6,4,15,1,10,15\); integrating a favorable auxiliary derivative bound \(a_0L+v\) gives \(\rho Q_\star/(h^2L^2)\). An adverse sign is split at half the proved gap, with complete Fourier Parseval on the high-auxiliary-frequency sequence. These are the checked component lemmas; all new phase-gap hypotheses are verified below. No network inverse, biased channel or analytic-cutoff assumption is used.

## 3. Far-cut comparison over the entire new horizon

Define the real comparison scale
\[
\ell_c=S/2=(\ell+M)/2\ge\ell .
\tag{15}
\]
It may be a half-integer. It is only a scale in inequalities, not a replacement lattice length or an invocation of the old theorem at a noninteger geometry. The actual sites \(N,N+1\) are integers.

Extend the finite space by a decoupled tail. The sole difference from \(H_\infty^0\) is
\[
\Delta=J(|N\rangle\langle N+1|+|N+1\rangle\langle N|).
\tag{16}
\]
The cap in (9) keeps both diagonals equal to \(2J\). Extend the common \(\mu I\) to both components for the comparison; this is harmless on the actual finite state.

Assume \(\ell\ge1000\) and \(\ell\ge100(K+1)\), as the final policy will. Then \(K\le0.01\ell_c\). For both \(n=N,N+1\), on the **entire** interval
\[
0\le u\le7S/16=7\ell_c/8
\]
we have
\[
2\ell_c\le n\le2.01\ell_c,\qquad
\partial_k[nk-ue(k)]\ge\ell_c/4,\qquad
\partial_k[-nk-ue(k)]\le-2\ell_c .
\tag{17}
\]
The first derivative magnitudes are at most \(4\ell_c\), and the second through fourth \(k\)-derivatives are at most \(2\ell_c\). On the cutoff support,
\(k'(x)\ge.999\), \(|k''(x)|\le.002\), \(|k'''(x)|\le3\), \(|k''''(x)|\le.1\). The \(x\)-phase first derivative therefore has magnitude \(>.23\ell_c\), and the next three derivatives have ceilings \(4\ell_c,32\ell_c,128\ell_c\), dominated by (13).

The outgoing \(+vx\) strengthens its positive derivative, and the incoming \(-vx\) strengthens its negative derivative, for every \(v\ge0\). The favorable pole bound applies to both components from time zero:
\[
|(O_tg)_n|,\ |(I_t\bar g)_n|
\le\frac{\rho Q_\star}{h^2\ell_c^2},\qquad n=N,N+1.
\tag{18}
\]
Consequently the integral of norms is
\[
\begin{split}
\mathcal E_{\rm cut}
&:=\int_0^{7S/(16J)}\|\Delta\Phi_\chi(t)\|\,dt\\
&\le\frac{7\sqrt2}{4}\frac{\rho Q_\star}{h^2\ell_c}
 <\frac{3\rho Q_\star}{h^2\ell_c}
 \le\frac{3\rho Q_\star}{h^2\ell}.
\end{split}
\tag{19}
\]
The longer integration time is explicitly paid: it grows as \(\ell_c\), whereas the cut-site amplitude bound falls as \(\ell_c^{-2}\). Replacing only the old horizon without moving and re-estimating the cut would not justify (19).

The filtered state need not have zero initial tail beyond \(N\). Use (12) once and Duhamel for the two exact full-space evolutions, giving for \(0\le t\le7S/(16J)\)
\[
\|e^{-itH_{\ell,M}}|s\rangle-e^{-i\mu t}\Phi_\chi(t)\|
\le2\sqrt P+\frac{3\rho Q_\star}{h^2\ell_c}.
\tag{20}
\]
No omitted spectral mass is multiplied by the duration, no oscillatory cancellation is invoked inside Duhamel, and no finite-spectrum absence of bound states is assumed.

## 4. All output-complement tails on the longer interval

For the full integer sequence \(b_n(t)=(O_tg)_n\), Parseval gives \(\sum_{n\in\mathbb Z}|b_n|^2=1\). We will bound its complete complement of \(F_M\), including negative Fourier indices, rather than just its physical interior.

### Incoming conjugate half-line

The favorable conjugate lemma requires \(u\ge1\) and has no upper-time restriction. On \(u\ge3\ell/4\), its scalar constant is dominated by \(Q_\star\), so
\[
i(t):=\|I_t\bar g\|_{n\ge0}
\le\frac{2\rho Q_\star}{h^2u^{3/2}}
<\frac{4\rho Q_\star}{h^2\ell^{3/2}} .
\tag{21}
\]
The displayed upper bound includes \(n=0\) and decreases as time increases; no monotonicity of the exact norm is assumed. The input term has the actual conjugate sign from (11),(14).

### Translated outgoing left half-line

Set \(L_-=\ell+K-1\). Every omitted integer \(n\le L_-\) is uniquely \(n=L_--r\), \(r\ge0\), with phase \(-rk+L_-k-ue(k)\). The checked negative-gap lemma has hypotheses
\[
Q_-=1.98u-L_-\ge1,\qquad L_-+u\le C_{\rm gap}Q_- .
\tag{22}
\]
For all \(u\ge3\ell/4\), not merely for the old symmetric window,
\[
Q_-\ge.485\ell-K+1\ge.4\ell\ge1 .
\tag{23}
\]
Moreover \(L_-\le1.01\ell\), and
\[
16Q_--(L_-+u)
=30.68u-17L_-
\ge(30.68\cdot.75-17\cdot1.01)\ell
=5.84\ell>0 .
\tag{24}
\]
Thus \(C_{\rm gap}=16\) remains valid however large the finite output length is. The old bound \(L_-+u\le1.885\ell\) would fail over this enlarged horizon and is not used.

The scalar negative-gap estimate therefore gives
\[
\begin{split}
d_-&:=\|(b_n)_{n\le L_-}\|_2\\
&\le\frac{\rho P_\star}{h^2Q_-^{3/2}}
 +\frac{4\sqrt h}{\rho}
    e^{-\rho^2Q_-/[2(2-\rho^2)]}\\
&\le\frac{4\rho P_\star}{h^2\ell^{3/2}}
 +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\end{split}
\tag{25}
\]
Here \(.4^{-3/2}<4\) and \(2(2-\rho^2)\le4\). The exponential term is a bound on the complete high-auxiliary-frequency sequence, obtained by Parseval before integration; it is not a substituted emitter-survival estimate.

### Outgoing right half-line

The omitted right interval starts at \(R_+=N+1=S+K\). Writing \(n=R_++r\), \(r\ge0\), the favorable outgoing lemma requires
\[
Q_+=.99R_+-2u\ge1,\qquad R_++u\le16Q_+ .
\tag{26}
\]
For every \(u\le7S/16\),
\[
Q_+\ge.115S+.99K\ge.23\ell_c,\qquad
R_++u\le2.875\ell_c+K\le2.885\ell_c
                  <16(.23\ell_c)\le16Q_+ .
\tag{27}
\]
All hypotheses hold on the full interval, including its right endpoint. The complete right tail is therefore
\[
d_+:=\|(b_n)_{n\ge N+1}\|_2
\le\frac{2\rho Q_\star}{h^2Q_+^{3/2}}
<\frac{20\rho Q_\star}{h^2\ell_c^{3/2}} .
\tag{28}
\]

The two intervals in (25),(28) are exactly the complement of (8). With \(d_M=\|(b_n)_{n\notin F_M}\|_2\), their combined norm satisfies
\[
\begin{split}
d_M
&\le\frac{4\rho P_\star}{h^2\ell^{3/2}}
   +\frac{20\rho Q_\star}{h^2\ell_c^{3/2}}
   +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}\\
&\le\frac{\rho D_\star}{h^2\ell^{3/2}}
   +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\end{split}
\tag{29}
\]
Every input and all 74 internal scalar coordinates are included. Equations (19),(21),(29) are the required new-horizon estimates; only the exact source identities and generic component lemmas were reused.

## 5. Normalized complete target and the unchanged accuracy prescription

Define the positive norm and output packet by
\[
q_M(t)=\left(\sum_{n\in F_M}|b_n(t)|^2\right)^{1/2}
       =\sqrt{1-d_M(t)^2},\qquad
z_M(t)=q_M(t)^{-1}\sum_{n\in F_M}b_n(t)|n\rangle .
\tag{30}
\]
The following policy proves \(q_M>0\) before that normalized target is used. This normalization fixes no new phase.

Because \(\Phi_\chi\) has norm one and its \(F_M\) coordinates equal \(b+I_t\bar g\),
\[
\operatorname{Re}\langle z_M,\Phi_\chi\rangle\ge q_M-i,\qquad
\|\Phi_\chi-z_M\|^2\le2(1-q_M)+2i\le2d_M^2+2i .
\tag{31}
\]
If \(q_M\ge i\), the complete residual also satisfies
\[
\|(I-P_{F_M})\Phi_\chi\|^2
\le1-(q_M-i)^2\le d_M^2+2i .
\tag{32}
\]
In particular this pays the actual filtered source \(A_\chi\), every input/internal coordinate and every beyond-cap coordinate. It uses neither an unfiltered survival bound nor an assumed eventual success. The square-root incoming cost in (31) is explicit.

For any \(0<\epsilon\le1\), keep exactly the old scalar policy at \(K=74\):
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
\right\}\right\rceil .
\end{split}
\tag{33}
\]
The constants (13) are fixed before this choice. The logarithm argument is \(524288/\epsilon^2>1\). This ensures \(\rho\le1/2\), \(\rho^2\le h\), \(P<1/2\), the cap geometry and all positive gaps used above.

For every finite integer \(M\ge\ell\), throughout (1), the simultaneous bounds are
\[
2\sqrt P<\epsilon/256,\qquad
\mathcal E_{\rm cut}\le\epsilon/64,\qquad
d_M\le\epsilon/128+\epsilon/128=\epsilon/64,\qquad
i\le\epsilon^2/8192 .
\tag{34}
\]
Thus \(q_M>0\) and \(q_M>i\), justifying (30)–(32). Inserting these bounds in (20),(31) gives the full scalar result
\[
\begin{split}
\|e^{-itH_{\ell,M}}|s\rangle-e^{-i\mu t}z_M(t)\|
&\le2\sqrt P+\frac{3\rho Q_\star}{h^2\ell_c}
                      +\sqrt{2d_M(t)^2+2i(t)}\\
&<\epsilon/256+\epsilon/64+\epsilon/32
=13\epsilon/256 .
\end{split}
\tag{35}
\]
The square-root term is at most \(\sqrt3\,\epsilon/64<\epsilon/32\). All bounds are uniform over the complete new interval, including both endpoints. No actual physical state has been projected or renormalized in (35).

## 6. Full physical output, actual record and phases

On \(F_M\) the physical arm map is the identity and the ordered gauge is \(-U_f\). Define the physical external target by
\[
\mathcal V_M(t)\xi=-e^{-i\mu t}z_M(t)\otimes U_f\xi
\tag{36}
\]
with the appropriate output rail/head embedding. All heads outside that external packet are vacant in the target. \(Q,P,R\), the old \(P\) information moved to \(Q\), and arbitrary passive-reference correlations are retained.

The integrand defining \(z_M\) contains \(e^{-iJt\,2(1-\cos k)}F_{\rm src}(k)\), including \(e^{ik}\). It therefore already contains the \(2J\) scalar phase. The physical \(\mu\) shift appears once in (36), regardless of the number of exterior heads: the complete matched scalar operator, including its unchanged internal matching and the exterior occupations, has the common term \(\mu I\) on the one-head sector. It is not \(\mu\) times the site count. The sign from \(W_{\rm right}\) is also retained. There is no freely fitted comparison phase.

The two selected \(b\) channels have the same scalar error. Their orthogonal direct sum has the same operator norm as a single scalar error, not a factor \(\sqrt2\) larger. Applying the exact unitary \(AW\) then gives
\[
\sup_{t\in\mathcal I_{\ell,M}}
\|e^{-itH_{\rm phys}}E-\mathcal V_M(t)\|
<13\epsilon/256<\epsilon/16 .
\tag{37}
\]
The induced norm is unchanged after adjoining passive references. The unhalved stabilized complete-output channel distance is consequently \(<13\epsilon/128<\epsilon/4\). This also covers mixed inputs by purification and contraction.

The target is in the joint range of external occupancy and actual record \(R=1\). Projecting the full-vector error onto the complement proves, uniformly in the input,
\[
\Pr(\text{external output and }R=1)>
1-(13\epsilon/256)^2 .
\tag{38}
\]
This is a conclusion of the complete-state estimate, not a postselection premise.

There is also an unchanged exact current-record identity for this exact finite installation. Let \(f_x^{\ell,M}(t)\) be its selected scalar evolution without \(\mu I\), in the original \(x\) coordinates. Let \(J_{\rm rec}\) send virtual coordinate 72 to the antisymmetric pair of final physical arms and \(x\ge73\) to the corresponding physical head, retaining output rails. With blank initial \(R\),
\[
P_1e^{-itH_{\rm phys}}E
=-e^{-i\mu t}J_{\rm rec}\!
\left[
\left(f_{72}^{\ell,M}(t)|72\rangle+
 \sum_{x=73}^{73+M}f_x^{\ell,M}(t)|x\rangle\right)\otimes U_f
\right].
\tag{39}
\]
The proof is the same final-layer algebra: earlier prefixes leave \(R=0\), the antisymmetric final-arm prefix and the final-origin/right prefixes carry \(-U_f\); changing only the exterior right lengths introduces no earlier \(R\) interaction. The actual probability
\[
p_{\rm rec}(t)=|f_{72}^{\ell,M}(t)|^2+
                     \sum_{x=73}^{73+M}|f_x^{\ell,M}(t)|^2
\tag{40}
\]
is input-independent. Whenever it is nonzero the normalized complete record branch factors with exact \(U_f\), including its clock profile and phase. At zero probability the normalized branch is undefined.

The external-only event starts at \(x=74\) and has a different profile. Record 1 can occur on the internal final arms or origin; it does not certify internal vacancy. Neither the all-time factorization when defined nor the long finite window supplies permanent completion, capture, reset or reuse. A larger requested interval changes the finite device by adding heads; it is not an all-time theorem for one fixed device. No generic perturbation statement is attached to (39).

## 7. Dwell recipe, counts, cap and geometry

The scheduled arrival, end and dwell are exactly
\[
t_{\rm arr}=\frac{3\ell}{4J},\qquad
t_{\rm end}=\frac{7(\ell+M)}{16J},\qquad
D=\frac{7M-5\ell}{16J}.
\tag{41}
\]
Since \(M\ge\ell\), \(D\ge\ell/(8J)>0\). The relative dwell is
\[
\frac{D}{t_{\rm arr}}
=\frac{7(\ell+M)}{12\ell}-1
=\frac{7M-5\ell}{12\ell}.
\tag{42}
\]
For \(\mathcal R\ge1/6\), the coefficient \((12\mathcal R+5)/7\ge1\), so the integer choice (2) is admissible and gives
\[
\mathcal R\le\frac{D}{t_{\rm arr}}
<\mathcal R+\frac7{12\ell}.
\tag{43}
\]
The ceiling changes only the small explicit upper slack. No later or realization-dependent hitting time is substituted for \(t_{\rm arr}\).

Writing \(S_{\mathcal R}=\ell+M_{\mathcal R}\), the exact useful bounds are
\[
\frac{12}{7}(\mathcal R+1)\ell
\le S_{\mathcal R}
<\frac{12}{7}(\mathcal R+1)\ell+1,
\tag{44}
\]
\[
(\mathcal R+1)t_{\rm arr}
\le t_{\rm end}
<(\mathcal R+1)t_{\rm arr}+\frac7{16J},\qquad
\mathcal R\,t_{\rm arr}\le D<
\mathcal R\,t_{\rm arr}+\frac7{16J}.
\tag{45}
\]

The physical heads comprise 296 internal heads, \(4\ell+4M\) ordinary exterior heads and two sources. Thus
\[
\text{heads}=298+4S,\qquad
\text{qubits}=301+4S .
\tag{46}
\]
Exterior blocks comprise \(4S\) ordinary \(Q_J\) bonds, two combined \(B\)'s, six caps and \(4S+2\) separate \(\mu n\) terms. Including the 468 internal blocks,
\[
\text{positive blocks}=478+8S .
\tag{47}
\]
These count every unused ray and both source heads. As before, \(B\) is counted as one supplied positive two-body block; splitting its three positive summands changes the block count and any perturbation convention, not the operator. For the choice (2), (44) gives
\[
\begin{split}
301+\frac{48}{7}(\mathcal R+1)\ell
&\le\text{qubits}<
305+\frac{48}{7}(\mathcal R+1)\ell,\\
478+\frac{96}{7}(\mathcal R+1)\ell
&\le\text{blocks}<
486+\frac{96}{7}(\mathcal R+1)\ell.
\end{split}
\tag{48}
\]

The full-support incident sums are unchanged by extending a ray: \(40J\) at \(Q/P\), \(16J\) at \(R\), below \(5J\) at internal heads, and \(3J+\mu,5J+\mu,4J+\mu,3J+\mu\) respectively at an exterior source, its ordinary neighbor, another ordinary site and a cap. They are all at most \(\Lambda\) under (3). No expected occupancy or cancellation is used in this cap.

Keep the checked injection of the 299 internal qubits into the \(7^3\) cube. The eight ports have different horizontal coordinates; extend their separate vertical rays to the stated lengths. Increasing the four right lengths preserves disjointness. Internal interactions have Manhattan range at most 18, exterior bonds range one, and data degrees remain \(20,20,8\). This is a finite-range selectively coupled graph, not a physical cubic nearest-neighbor realization. The source and empty-head preparation and absence of undeclared couplings remain supplies.

For the explicit old policy (33), \(\ell=\Theta(\epsilon^{-2}\log(1/\epsilon))\) as \(\epsilon\to0\), with its large fixed constants retained. Uniformly for the selected finite \(\mathcal R\ge1/6\),
\[
\begin{split}
\text{qubits, blocks}
 &=\Theta\!\left((\mathcal R+1)\epsilon^{-2}\log(1/\epsilon)\right),\\
t_{\rm arr}
 &=\Theta\!\left(\Lambda^{-1}\epsilon^{-2}\log(1/\epsilon)\right),\\
D
 &=\Theta\!\left(\Lambda^{-1}\mathcal R\,\epsilon^{-2}\log(1/\epsilon)\right),\\
t_{\rm end}
 &=\Theta\!\left(\Lambda^{-1}(\mathcal R+1)\epsilon^{-2}\log(1/\epsilon)\right),\\
\gamma&=\Theta(\Lambda\epsilon).
\end{split}
\tag{49}
\]
The source strength and scheduled arrival do not depend on \(\mathcal R\). At \(M=\ell\), the interval and counts reduce exactly to the checked symmetric installation; no discontinuous special case is hidden at \(\mathcal R=1/6\).

At fixed accuracy this extension is linear in requested relative dwell, while the separately checked engineered-clock dwell recipe has quadratic size and a later arrival. These are comparisons of particular sufficient constructions under different coefficient contracts, not optimality bounds or a proof that the uniform family dominates at fixed accuracy, hardware or tolerated errors. The uniform family keeps exact ratios, equal diagonals and exact arms/rails. Its nominal \(Q/P\) load already reaches the cap. The engineered supported-error allowance is not imported.

## 8. Exact premises, source exposure and the new check obligation

All research paths below are relative to
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

| Direct source | Bytes | SHA-256 | Role |
|---|---:|---|---|
| [Symmetric uniform physical source](../exact_uniform_physical_loader/PROPOSAL.md) | 9952 | `809d39e07806cc05af1c715f58ebde90209a07b2dfc2e86bce481fe629c0629f` | Exact matched installation, selected-source input, supplies and local cap conventions. Its old window is not the new conclusion. |
| [Its distinct review](../exact_uniform_physical_loader_check/REVIEW.md) | 11913 | `b9b897fc8dbce257a2bbe7895d5413d30d6f8cc289efb83b14ff7d465f5277c0` | Support for that symmetric transfer at its stated scope. |
| [Literal scalar finite-source proof](../exact_uniform_chain_finite_launch/PROPOSAL.md) | 28149 | `bda916e331d0bf3863feac8e0b7dce279df6f2eaa94f0dd17daf651cad51545a` | Normalized source/filter, fixed constants, full-state closure and unchanged accuracy prescription. |
| [Its distinct review](../exact_uniform_chain_finite_launch_check/REVIEW.md) | 12769 | `0ef35c231f3550f196bd1f8df8b5b3773ebfa6314232931ea9470ca1f00a5bac` | Support for the literal symmetric scalar proof, not automatic acceptance of this extension. |
| [Generic scalar half-line estimates](../common_product_resonant_halfline_tails/PROPOSAL.md) | 15197 | `43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1` | Favorable conjugate incoming and positive-gap outgoing estimates and exact pole/IBP constants. Only coefficient \(1\), \(k_a=k\) is used. |
| [Their distinct review](../common_product_resonant_halfline_tails_check/REVIEW.md) | 9812 | `1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b` | Support for those component interfaces. |
| [Generic translated negative-gap estimate](../common_product_resonant_late_tails/PROPOSAL.md) | 13034 | `a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9` | Arbitrary \(L,u\) under its actual gap/ratio conditions, not only its example time windows. |
| [Its distinct review](../common_product_resonant_late_tails_check/REVIEW.md) | 7992 | `ef27352b742abe064e5b8d71d09d7904182cea49c9dce2c77187aab8494b34cd` | Support for the generic translated-tail proof. |
| [Exact global physical composition](../exact_two_body_direct_loader_composition/PROPOSAL.md) | 23893 | `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946` | Ordered \(A,W\), actual record projection, internal blocks, phase and range-18 placement. The new unequal left/right boundaries are checked explicitly here. |
| [Its distinct review](../exact_two_body_direct_loader_composition_check/REVIEW.md) | 14485 | `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6` | Support for the exact global operator and physical inventory. |

These five pairs have scoped distinct support and ROOT acceptance. Complete reads from the immediately preceding coherent tasks are reused at these unchanged identities. For the enlarged-horizon judgment, the full generic late-tail proof through its domains and the complete incoming/positive-half-line proof were reread directly; the finite source, physical boundary and global record formulas were also inspected in their exact arguments. Hash matching is only the identity check, not a substitute for those reads.

The scalar ancestry is explicit and unchanged: `common_product_endpoint_launch/PROPOSAL.md`, SHA `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, with review `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1`, supplies (10),(11); its standalone spectral-measure calculation is `bandcenter_reference_measure_check/REVIEW.md`, SHA `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`. The actual-cutoff/pole ancestry is `common_product_outgoing_pole_tail/PROPOSAL.md`, SHA `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80`, review `0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00`. Their complete preceding reads are reused. No earlier network coefficient, biased calibration, approximate-loader runtime or active-energy construction is a premise.

The physical ancestry is the corrected matched-extension source `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e` / review `36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f` and the diamond source `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33` / review `da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945`, through the checked global source. The corrected single-\(\mu\) convention is used throughout. These exact local identities do not themselves supply a finite probability; Sections 3–5 pay that obligation.

For the comparison in Section 7 only, the engineered dwell pair is `exact_engineered_clock_dwell_tradeoff/PROPOSAL.md`, SHA `d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25`, and its review `7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46`. It is not a proof dependency of (1)–(49). Its previously fully read argument has a different scalar clock and sufficient recipe.

ROOT proposed the asymmetric-output candidate and initial target interval. This author wrote the scalar finite-source proof and subsequent synthesis manuscript, so this is exposed author development with shared ancestry, not a distinct check or blind discovery. The parent suggestion is not evidence for its desired conclusion. The new proof work is the extended cap integral, late-tail phase-ratio verification for unbounded later \(u\), exact target endpoints and finite boundary identification, plus the resulting resource/dwell bookkeeping.

The unchanged manuscript `exact_loader_clock_tradeoffs_publication_draft/NOTE.md` remains frozen at 50554 bytes, SHA `34a8ba3eb1fb64b1f7ca32aced642af27c7fc159cb6fbe8353da5b3e734b8b59`. It is context, not a new premise or a publication claim for this proposal.

### Scope and decisive review targets

The source status is `conditional-support` and the intended claim type is `bounded_theorem`; this new result awaits distinct review and any later integration/audit. Its contribution supports an adjustable finite complete-output window for the exact uniform-loader family. It does not retire the supplied coefficient, preparation, isolation or native-identification conditions.

A distinct check should reconstruct the following new steps, rather than infer them from the accepted symmetric case:

1. The finite \(A,W\) identity with unequal left/right lengths, including the two unused left caps and all four equal right terminations.
2. The cap estimate (17)–(20) with real \(\ell_c\), both source signs, actual unchanged diagonals and the entire longer Duhamel integral.
3. The left phase-ratio inequality (24) for all later \(u\), and the right gap/ratio (27) at the enlarged horizon.
4. The complete normalized packet, single initial filter cost, actual \(A_\chi\) residual and square-root incoming allocation in (30)–(35).
5. The full sign/phase/record distinction, exact counts/cap and ceiling/ratio arithmetic in (36)–(49).

If a cap diagonal, matching coefficient, prepared state or admissible error class is changed, these exact statements need their own new proof. No physical supplier or permanent framework Record is identified merely by naming the current qubit \(R\).

### Source scope and work record

The local statement search used `rg` on the relevant exact-loader/uniform-clock note names for asymmetric output and dwell terms. It found the already read engineered dwell comparison above, not a same-operator longer-horizon result. A broader phrase search also returned unrelated record-law/history notes; those hits were not imported as proof or represented as a complete literature search. This note makes no global novelty claim about ballistic storage or Fourier-tail methods.

The current local instruction identities were refreshed: W/AGENTS.md `febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0` and SCIENCE_WORKFLOW.md `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`. The canonical physics-loop entry was read at SHA `e6874cdae5d2a69ad60bac6b9d67346025a086e10a0a247137ea14bf6fca34a0`; the installed entry differed, so it was not treated as freshness authority. Its discovery/claim-status/delivery references matched the canonical local files and were read, with truncated portions repaired by bounded rereads. The current primitive registry was inspected; no registered primitive is being called a missing premise or extended by this supplied-Hamiltonian theorem. No Git freshness check was performed under the no-Git task scope.

Only this proposal is written. Work is analytical derivation, bounded source reads, deterministic byte/hash bookkeeping and text editing. No scientific executable, propagation experiment, numerical sweep, canonical runner, new agent, model/effort override, W/Git/PR/checkpoint/audit/axiom/editable-prompt mutation occurred. The broader skill's campaign/PR artifacts are outside this explicit one-source assignment. Source checks and this author argument do not stand in for the pending distinct review.
