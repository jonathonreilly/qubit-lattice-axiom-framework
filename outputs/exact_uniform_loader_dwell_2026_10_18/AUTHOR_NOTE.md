# Adjustable finite dwell for the supplied exact uniform loader

2026-10-18. Claim status: **bounded_theorem**, conditional on the stated supplied Hamiltonian and input. The new asymmetric-length argument has a supporting distinct check at the exact identities below. This manuscript is source-exposed synthesis, not another independent validation or retained audit.

The [clock-tradeoffs parent](EXACT_LOADER_CLOCK_TRADEOFFS_BOUNDED_THEOREM_NOTE_2026-10-18.md) proves a finite complete-output window for an exact matched loader driven by a weak endpoint source and uniform ordinary hopping. Lengthening only its four right output rays permits an arbitrarily large **finite** dwell/arrival ratio while keeping the original source strength and scheduled arrival. The changed device has a separately proved longer-horizon cut and tail estimate; the old window is not simply extrapolated.

For the explicit accuracy length \(\ell(\epsilon)\) below, any integer \(M\ge\ell\) gives the complete-output window

\[
\mathcal I_{\ell,M}=
\left[\frac{3\ell}{4J},\frac{7(\ell+M)}{16J}\right],\qquad J=\Lambda/40.
\tag{1}
\]

The vector error is strictly below \(13\epsilon/256\), with every source, internal head, data qubit and passive reference retained. For a requested ratio \(\mathcal R\ge1/6\), choose

\[
M_{\mathcal R}=\left\lceil\frac{(12\mathcal R+5)\ell}{7}\right\rceil.
\tag{2}
\]

The dwell is then at least \(\mathcal R\) times the unchanged arrival \(3\ell/(4J)\). Qubit and positive-block counts are \(301+4(\ell+M)\) and \(478+8(\ell+M)\). At fixed accuracy these costs grow linearly in \(\mathcal R+1\). This is a sufficient recipe, not an optimality statement, practical device estimate, independent-error tolerance or permanent halt.

## 1. Actual asymmetric device and complete target

Retain the parent's matched 26-layer core: 296 internal heads, 468 positive blocks, shared ordinary data \(Q,P,R\), and four head rails labelled \((a,b)\). Its exact physical arm rotation \(A\) and ordered gauge \(W\) have left prefix identity and right prefix

\[
-U_f,\qquad U_f=I_aX_R C_P^{(b)}\operatorname{SWAP}_{QP},\qquad
C_P^{(b)}=|0\rangle\langle0|_P X_b+|1\rangle\langle1|_P I_b.
\tag{3}
\]

The gate maps \((b,q,p,0)\) to \((b\oplus(1-q),p,q,1)\), preserving old-P/passive-reference information on Q. The rails are head positions, not duplicate data. The unchanged local gate algebra is in the parent and its linked exact global source; no engineered-clock performance is used here.

Set \(\mu=(\sqrt2-1)J\), \(\gamma=\rho J\). Attach \(\ell\) ordinary heads to each left origin and \(M\) to each right origin, with ordinary positive bonds

\[
Q_c(v,w)=c[n_v+n_w-(\sigma_v^+\sigma_w^-+\sigma_v^-\sigma_w^+)],
\qquad\|Q_c\|=2c.
\]

Each of the two left \(a=1\) endpoints receives one additional source \(s\) through the combined positive block

\[
B=Q_\gamma(s,v_\ell)+(2J-\gamma)n_s+(J-\gamma)n_{v_\ell}.
\tag{4}
\]

Its one-head matrix is \(\left(\begin{smallmatrix}2J&-\gamma\\-\gamma&J\end{smallmatrix}\right)\), and its full norm is \(3J\), including the doubly occupied state. The preceding ordinary bond supplies the other J at its neighbor. Cap the other two left rays and all four right rays with \(Jn_v\). Add \(\mu n_v\) on every exterior head, including the sources. Internal matching already supplies the common shift; no additional internal \(\mu\) is installed. Every one-head diagonal is precisely \(2J+\mu\), including capped endpoints. The only nonordinary hopping magnitude is \(\gamma\).

Supply one head coherently encoded in the two source endpoints with \(a=1\), arbitrary logical b and joint Q/P/passive-reference state, \(R=0\), and every other head vacant. There is no additional free data or reference Hamiltonian. Exact coefficient ratios, common diagonals, equal paired arms/rails, selective interactions, input coherence and blank apparatus remain premises.

Right terminations commute through \(W=-U_f\) because their four lengths and blocks are identical. Left terminations remain diagonal in a because \(W=I\) there. Equality of right and left lengths is unnecessary. The finite transformed Hamiltonian is a direct sum: the two selected source clocks are identical, while the unused left-capped clocks remain unpopulated. The invariant physical sector is the image under AW of this selected virtual sector, not the set of physical internal a=1 coordinates.

With \(K=74\), \(S=\ell+M\), \(N=S+K-1\) and \(n=x+\ell\), each selected clock is

\[
H_{\ell,M}=B+\sum_{n=0}^{N-1}Q_J(n,n+1)+Jn_N
                +\mu\sum_{v=s,0,\ldots,N}n_v.
\tag{5}
\]

Its source is x=\(-\ell-1\); the ordinary interval ends at x=\(73+M\). The retained external output is exactly

\[
F_M=\{\ell+K,\ldots,S+K-1\}
\quad\leftrightarrow\quad x=74,\ldots,73+M,
\tag{6}
\]

with M sites. The final internal origin is not part of this set.

## 2. Source normalization and explicit accuracy policy

Only the scalar spectral and actual-cutoff interfaces of the parent are reused. Let \(u=Jt\), \(e(k)=2(1-\cos k)\), and

\[
F_{\rm src}(k)=
\frac{-i\sqrt{2/\pi}\rho e^{ik}}{(2-\rho^2)\cot k-i\rho^2},
\qquad \int_0^\pi|F_{\rm src}|^2dk=1.
\tag{7}
\]

Use the parent's real quintic cutoff: one on \(|k-\pi/2|\le h/2\), zero beyond \(3h/4\), and \(1-10z^3+15z^4-6z^5\) on each transition with \(z=4(|k-\pi/2|-h/2)/h\). This particular cutoff is \(C^2\cap W^{3,1}\), with the required matching traces. Put

\[
P=3\rho^2/h,\quad p=\|\chi F_{\rm src}\|_2^2\ge1-P>1/2,
\qquad g=\chi F_{\rm src}/\sqrt p.
\]

The exact normalized filtered half-line state is

\[
\begin{aligned}
\Phi_\chi(t)&=A_\chi(t)|s\rangle+O_tg+I_t\bar g,\qquad\|\Phi_\chi(t)\|=1,\\
(O_tf)_n&=(2\pi)^{-1/2}\int_0^\pi e^{ink-iue(k)}f(k)\,dk,\\
(I_tf)_n&=(2\pi)^{-1/2}\int_0^\pi e^{-ink-iue(k)}f(k)\,dk,\\
A_\chi(t)&=p^{-1/2}\int_0^\pi\chi(k)|F_{\rm src}(k)|^2e^{-iue(k)}\,dk,\\
\||s\rangle-\Phi_\chi(0)\|&\le2\sqrt P.
\end{aligned}                                                       \tag{8}
\]

There is one cutoff factor in the emitter integral. Its norm is not replaced by an unfiltered survival bound. The initial omission is paid once and is independent of M. This is a spectral comparison to the actual endpoint seed, not a physically supplied packet.

For an explicit fixed-constant prescription, set \(a_0=23/100\), \((B_2,B_3,B_4)=(64,512,2048)\), and \((D_0,D_1,D_2,D_3)=(2,24,394,6280)\). Define the same parent constants

\[
\begin{aligned}
P_\star={}&D_3/a_0^3+6B_2D_2/a_0^4
 +(4B_3/a_0^4+15B_2^2/a_0^5)D_1\\
 &+(B_4/a_0^4+10B_2B_3/a_0^5+15B_2^3/a_0^6)D_0,\\
Q_\star={}&D_3/(2a_0^2)+2B_2D_2/a_0^3
 +(4B_3/(3a_0^3)+15B_2^2/(4a_0^4))D_1\\
 &+(B_4/(3a_0^3)+10B_2B_3/(4a_0^4)+3B_2^3/a_0^5)D_0,\\
D_\star={}&4P_\star+20Q_\star.
\end{aligned}                                                       \tag{9}
\]

They are numerical constants, not unspecified functions of accuracy or dwell. For \(0<\epsilon\le1\), choose

\[
\begin{aligned}
h&=10^{-3},\qquad \rho=\epsilon\sqrt h/1024,\\
\ell&=\left\lceil\max\left\{
1000,7500,\frac{192\rho Q_\star}{h^2\epsilon},
\left[\frac{128\rho D_\star}{h^2\epsilon}\right]^{2/3},
\left[\frac{32768\rho Q_\star}{h^2\epsilon^2}\right]^{2/3},
\frac{10}{\rho^2}\log\frac{512\sqrt h}{\rho\epsilon}
\right\}\right\rceil.
\end{aligned}                                                       \tag{10}
\]

Then choose any finite integer \(M\ge\ell\), or (2). The logarithm argument is \(524288/\epsilon^2>1\). This policy guarantees \(\rho\le1/2\), \(\rho^2\le h\), \(P<1/2\) and \(\ell\ge100(K+1)\). Neither \(\rho\) nor \(\ell\) depends on requested dwell.

## 3. The changed cut comparison over the full longer horizon

Set the real comparison scale \(\ell_c=S/2\ge\ell\). It need not be an integer; the physical site indices N and N+1 remain integers. Cutting only the hopping between them changes the infinite scalar operator by

\[
\Delta_H=J(|N\rangle\langle N+1|+|N+1\rangle\langle N|).
\tag{11}
\]

Both diagonals remain 2J. The finite restriction is exactly (5) minus \(\mu I\); deleting a Laplacian bond and its occupations would be a different model. A decoupled tail and the same \(\mu I\) may be included for the norm comparison.

For \(0\le u\le7S/16=7\ell_c/8\), at both cut sites,

\[
2\ell_c\le n\le2.01\ell_c,\qquad
\partial_k[nk-ue(k)]\ge\ell_c/4,\qquad
\partial_k[-nk-ue(k)]\le-2\ell_c.
\tag{12}
\]

First derivative magnitudes are at most \(4\ell_c\), and orders two through four are at most \(2\ell_c\). After \(x=\tan(k-\pi/2)\), the first magnitudes exceed \(.23\ell_c\), while the next three derivatives fit \(4\ell_c,32\ell_c,128\ell_c\). These are below the fixed ceilings in (9).

The exact source pole has auxiliary phase +vx for \(F_{\rm src}\), and -vx for its conjugate. They reinforce the positive outgoing and negative incoming slopes in (12), respectively, for every \(v\ge0\). Therefore the checked favorable pole lemma gives each of the two lead amplitudes at each cut site a bound \(\rho Q_\star/(h^2\ell_c^2)\), from time zero. The resulting integral of norms is

\[
\mathcal E_{\rm cut}
\le\frac{7\sqrt2}{4}\frac{\rho Q_\star}{h^2\ell_c}
<\frac{3\rho Q_\star}{h^2\ell_c}
\le\frac{3\rho Q_\star}{h^2\ell}.
\tag{13}
\]

The time grew as \(\ell_c\), but the cut-site amplitude bound fell as \(\ell_c^{-2}\). This explicit balance justifies the new horizon. No oscillatory cancellation inside Duhamel is assumed. The initial filtered state may already have a beyond-cap tail: applying its one seed error under the cut evolution and Duhamel to the full filtered vector gives

\[
\|e^{-itH_{\ell,M}}|s\rangle-e^{-i\mu t}\Phi_\chi(t)\|
\le2\sqrt P+\frac{3\rho Q_\star}{h^2\ell_c},
\qquad 0\le t\le7S/(16J).
\tag{14}
\]

No omitted spectral mass is multiplied by time and no absence of finite-chain bound states is presumed.

## 4. Both omitted half-lines and complete normalization

Define \(b_n(t)=(O_tg)_n\) on all integers. Parseval gives \(\sum_{n\in\mathbb Z}|b_n|^2=1\). For all \(u\ge3\ell/4\), the favorable incoming-conjugate lemma has no upper-time restriction and gives

\[
i(t)=\|I_t\bar g\|_{n\ge0}
\le\frac{2\rho Q_\star}{h^2u^{3/2}}
<\frac{4\rho Q_\star}{h^2\ell^{3/2}}.
\tag{15}
\]

This includes n=0 and is a decreasing upper bound, not asserted monotonicity of the actual norm.

For the omitted outgoing left interval, put \(L_-=\ell+K-1\) and \(n=L_--r\), \(r\ge0\). The generic negative-gap lemma requires \(Q_-=1.98u-L_-\ge1\) and \(L_-+u\le16Q_-\). On every later time \(u\ge3\ell/4\),

\[
Q_-\ge.4\ell,\qquad
16Q_--(L_-+u)=30.68u-17L_-\ge5.84\ell>0.
\tag{16}
\]

Thus the ratio condition remains valid on arbitrarily long finite extensions. The old upper bound \(L_-+u\le1.885\ell\) would fail and is not used. The checked low/high auxiliary-frequency estimate gives

\[
d_-\le\frac{4\rho P_\star}{h^2\ell^{3/2}}
 +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\tag{17}
\]

The enumeration includes every negative Fourier index and every physical input/internal ordinary coordinate. The exponential is a whole-sequence high-frequency bound, not a survival-amplitude substitution.

For the right interval \(n=R_++r\), with \(R_+=S+K\), the favorable positive-gap lemma requires \(Q_+=.99R_+-2u\ge1\) and \(R_++u\le16Q_+\). Up to the new latest time,

\[
Q_+\ge.23\ell_c,\qquad
R_++u\le2.885\ell_c<16(.23\ell_c)\le16Q_+.
\tag{18}
\]

The gap improves at earlier times. Its complete half-line norm is

\[
d_+<\frac{20\rho Q_\star}{h^2\ell_c^{3/2}}.
\]

These two intervals exactly exhaust the complement of (6). Combining their norms conservatively,

\[
d_M:=\|(b_n)_{n\notin F_M}\|_2
\le\frac{\rho D_\star}{h^2\ell^{3/2}}
 +\frac{4\sqrt h}{\rho}e^{-\rho^2\ell/10}.
\tag{19}
\]

The actual cutoff's third weak derivative and the scalar coefficient-one cases of the parent pole/half-line lemmas are the required interfaces. No arbitrary-C2, analytic-cutoff or matrix-network estimate is being substituted.

Define the positive norm \(q_M=\sqrt{1-d_M^2}\) and \(z_M=q_M^{-1}\sum_{n\in F_M}b_n|n\rangle\). The policy proves positivity before this target is used. Since \(\Phi_\chi\) is a unit vector whose F_M coordinates are b plus the incoming contribution,

\[
\operatorname{Re}\langle z_M,\Phi_\chi\rangle\ge q_M-i,
\qquad \|\Phi_\chi-z_M\|^2\le2d_M^2+2i.
\tag{20}
\]

If \(q_M\ge i\), its complete complement also obeys \(\|(I-P_{F_M})\Phi_\chi\|^2\le d_M^2+2i\). This pays the actual filtered emitter and every nonoutput coordinate, including beyond the cap. The square-root cost of i is retained.

The unchanged policy (10), now combined with the new-domain estimates, gives uniformly on (1)

| Complete-proof quantity | Allowance |
|---|---:|
| Initial filter cost \(2\sqrt P\) | \(<\epsilon/256\) |
| Full longer-horizon cut integral | \(\le\epsilon/64\) |
| Algebraic and exponential parts of \(d_M\) | each \(\le\epsilon/128\) |
| Complete incoming norm i | \(\le\epsilon^2/8192\) |

Thus \(d_M\le\epsilon/64<1\), \(q_M>i\), and the last cost in (20) is at most \(\sqrt3\epsilon/64<\epsilon/32\). The complete scalar result is

\[
\|e^{-itH_{\ell,M}}|s\rangle-e^{-i\mu t}z_M(t)\|
<13\epsilon/256.
\tag{21}
\]

This is a norm bound on actual evolution, without projection or renormalization of that actual state.

## 5. Physical output phase and the actual record event

On F_M the arm rotation is identity and the gauge is \(-U_f\). The normalized physical target is therefore the fixed output-rail embedding of

\[
\mathcal V_M(t)\xi=-e^{-i\mu t}z_M(t)\otimes U_f\xi.
\tag{22}
\]

All heads outside this packet are vacant in the target, and Q/P/R and every passive reference are retained. The Fourier exponent in b_n already includes \(2J\); the source carries its actual \(e^{ik}\) factor. Equation (22) adds \(\mu\) once, not once per site, and preserves the fixed right-prefix minus. Its positive normalization is not a freely chosen phase.

The two selected b clocks have orthogonal rail errors with the same scalar profile, giving the same induced norm rather than a factor \(\sqrt2\). Applying the exact physical unitary yields

\[
\sup_{t\in\mathcal I_{\ell,M}}
\|e^{-itH_{\rm phys}}E-\mathcal V_M(t)\|<13\epsilon/256.
\tag{23}
\]

The unhalved stabilized complete-channel distance is \(<13\epsilon/128\), including mixed inputs by purification. The normalized target lies entirely in external occupancy AND R=1, so their joint success probability is \(>1-(13\epsilon/256)^2\). This is a consequence, not a postselection premise.

The unchanged exact gauge also gives a different, all-time current-record identity. Write f for the exact selected finite scalar evolution without \(\mu I\). Let \(J_{\rm rec}\) map virtual72 to the antisymmetric final-arm pair and x\(\ge73\) to their physical coordinates. With initially blank R,

\[
P_1e^{-itH_{\rm phys}}E
=-e^{-i\mu t}J_{\rm rec}
\left[\left(f_{72}|72\rangle+\sum_{x=73}^{73+M}f_x|x\rangle\right)
\otimes U_f\right].
\tag{24}
\]

Its probability is input-independent and its normalized branch, whenever nonzero, carries exact U_f with that retained clock profile. At zero probability normalization is undefined. External-only output starts at74, whereas this branch includes internal final arms and origin73. Therefore record1 does not assert internal vacancy. Lengthening the rays introduces no earlier R interaction, but later reflections can unset the record and undo the operation. A larger requested dwell changes the device; it does not establish all-time completion for one finite device. No generic perturbation or rare-event robustness theorem is added here.

## 6. Dwell, physical resources and comparison limits

The exact scheduled times and ratio are

\[
t_{\rm arr}=\frac{3\ell}{4J},\quad
D=\frac{7M-5\ell}{16J},\quad
\frac D{t_{\rm arr}}=\frac{7M-5\ell}{12\ell}.
\tag{25}
\]

For (2),

\[
\mathcal R\le D/t_{\rm arr}<\mathcal R+\frac7{12\ell},\qquad
\frac{12}{7}(\mathcal R+1)\ell\le S<\frac{12}{7}(\mathcal R+1)\ell+1.
\tag{26}
\]

Consequently \(\mathcal R t_{\rm arr}\le D<\mathcal R t_{\rm arr}+7/(16J)\), and the endpoint time lies between \((\mathcal R+1)t_{\rm arr}\) and that quantity plus \(7/(16J)\). At \(\mathcal R=1/6\), M=\(\ell\) and the symmetric parent window is recovered exactly.

There are 296 internal heads, 4S ordinary exterior heads and two sources: total \(298+4S\) heads and \(301+4S\) qubits. Exterior blocks are 4S ordinary bonds, two combined B blocks, six caps and 4S+2 separate shift occupations. Including the 468 internal blocks gives \(478+8S\). Counting B as one supplied positive two-body block is explicit; splitting its three summands changes block bookkeeping, not the Hamiltonian. For the requested ratio,

\[
\begin{aligned}
301+\tfrac{48}{7}(\mathcal R+1)\ell
&\le\text{qubits}<305+\tfrac{48}{7}(\mathcal R+1)\ell,\\
478+\tfrac{96}{7}(\mathcal R+1)\ell
&\le\text{blocks}<486+\tfrac{96}{7}(\mathcal R+1)\ell.
\end{aligned}
\tag{27}
\]

Extending a ray changes no local incidence. Full-support loads remain 40J at Q/P, 16J at R, below5J at internal heads, and respectively \(3J+\mu,5J+\mu,4J+\mu,3J+\mu\) at source, source neighbor, ordinary and cap. These obey \(\Lambda\). The eight disjoint vertical rays of the checked cube embedding may have these different finite lengths without intersections. Internal range18, exterior range1 and data degrees20,20,8 remain. This is not a cubic nearest-neighbor realization, and uninstalled geometric adjacency supplies no coupling.

The policy has \(\ell=\Theta(\epsilon^{-2}\log(1/\epsilon))\) as \(\epsilon\to0\). For the selected finite \(\mathcal R\ge1/6\),

| Quantity | Sufficient-family order |
|---|---|
| Qubits and blocks | \(\Theta((\mathcal R+1)\epsilon^{-2}\log(1/\epsilon))\) |
| Scheduled arrival | \(\Theta(\Lambda^{-1}\epsilon^{-2}\log(1/\epsilon))\) |
| Dwell | \(\Theta(\Lambda^{-1}\mathcal R\epsilon^{-2}\log(1/\epsilon))\) |
| End of certified interval | \(\Theta(\Lambda^{-1}(\mathcal R+1)\epsilon^{-2}\log(1/\epsilon))\) |
| Source strength | \(\Theta(\Lambda\epsilon)\), independent of \(\mathcal R\) |

At fixed accuracy the linear-in-ratio length extension contrasts with the parent's engineered-clock dwell recipe, which pays quadratic length and a later arrival. These are different sufficient families with different supplied coefficient contracts. The uniform recipe's much larger accuracy-dependent constants and scaling remain; this is not a proof of dominance at equal hardware, accuracy, time or tolerance, nor an optimality lower bound. The engineered supported-error allowance is not inherited. Here the nominal Q/P load reaches the cap, and exact matching, arms/rails and diagonals remain premises. Coefficient magnitude is not tolerated error.

The theorem does not supply coherence preparation, blank heads/R, active system dynamics, cooling, native interactions, an environmental record, capture or reset. No active-energy or reference-assisted construction is transferred into this result.

## 7. Exact evidence closure and synthesis exposure

The canonical destination is `docs/EXACT_UNIFORM_LOADER_DWELL_BOUNDED_THEOREM_NOTE_2026-10-18.md`. Its new packet is `outputs/exact_uniform_loader_dwell_2026_10_18/`, containing the following two complete bodies unchanged:

| New source or check | Bytes | SHA256 |
|---|---:|---|
| [Asymmetric dwell proposal](../outputs/exact_uniform_loader_dwell_2026_10_18/source_checks/exact_uniform_loader_dwell/PROPOSAL.md) | 34564 | `96660b9eaf719aac01d4b8e29cdde3661ed6d2b710745ceacccce286e5b4d031` |
| [Distinct dwell check](../outputs/exact_uniform_loader_dwell_2026_10_18/source_checks/exact_uniform_loader_dwell_check/REVIEW.md) | 17747 | `af641f89b7759889d2e76b0a57564b56f381d155a0fb014ef86fd4bfadb4be41` |

Both have scoped support and ROOT acceptance. The frozen author's historical pending label remains unchanged; the review supplies the disposition for that exact identity. The mathematical parent note is 50515 bytes, SHA256 `e89aadfcfb49096cdf7cd9831d1317d7063a5cc9d229b16f200761dadb39e23c`, linked at the start. Parent publication context supplied for this task is regular PR9741 head `d27a365724c544edeb1374f7c32ac9667168db55`; no fresh remote/Git verification was performed by this drafting worker.

Unchanged proof bodies are linked in their existing packets, not recopied recursively. The direct closure for this extension is:

| Inherited exact interface | Source SHA256 / check SHA256 |
|---|---|
| [Uniform physical interface](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_physical_loader/PROPOSAL.md) / [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_physical_loader_check/REVIEW.md) | `809d39e07806cc05af1c715f58ebde90209a07b2dfc2e86bce481fe629c0629f` / `b9b897fc8dbce257a2bbe7895d5413d30d6f8cc289efb83b14ff7d465f5277c0` |
| [Scalar normalized finite-source proof](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_chain_finite_launch/PROPOSAL.md) / [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/exact_uniform_chain_finite_launch_check/REVIEW.md) | `bda916e331d0bf3863feac8e0b7dce279df6f2eaa94f0dd17daf651cad51545a` / `0ef35c231f3550f196bd1f8df8b5b3773ebfa6314232931ea9470ca1f00a5bac` |
| [Half-line norms](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_halfline_tails/PROPOSAL.md) / [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_halfline_tails_check/REVIEW.md) | `43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1` / `1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b` |
| [Translated negative-gap norm](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_late_tails/PROPOSAL.md) / [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_resonant_late_tails_check/REVIEW.md) | `a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9` / `ef27352b742abe064e5b8d71d09d7904182cea49c9dce2c77187aab8494b34cd` |
| [Global physical gauge and record](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition/PROPOSAL.md) / [check](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_two_body_direct_loader_composition_check/REVIEW.md) | `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946` / `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6` |

The unchanged scalar closure is also already preserved in the parent packet: [endpoint source](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_endpoint_launch/PROPOSAL.md) `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_endpoint_launch_check/REVIEW.md) `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1`; [standalone source measure](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/bandcenter_reference_measure_check/REVIEW.md) `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`; and [pole/IBP source](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_outgoing_pole_tail/PROPOSAL.md) `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80` / [check](../outputs/exact_loader_clock_tradeoffs_2026_10_18/source_checks/common_product_outgoing_pole_tail_check/REVIEW.md) `0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00`. Their unrelated older network applications are not imported. The corrected diamond/matching ancestry is pinned by the linked global source and the parent's exact source map; no new local-gate claim is made here.

For comparison only, the [engineered dwell source](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff/PROPOSAL.md) `d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25` and its [check](../outputs/exact_two_body_engineered_loader_2026_10_18/source_checks/exact_engineered_clock_dwell_tradeoff_check/REVIEW.md) `7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46` establish a different sufficient family. They are not proof dependencies of (21)–(23).

The drafting worker read the complete changed dwell proposal and review and the complete parent note, repairing truncated aggregate displays by bounded rereads. Prior full reads of unchanged scalar/gauge premises are reused at their stated scopes. The worker authored some earlier scalar tail and engineered-dwell results and checked the symmetric uniform and global constructions; the new source author and reviewer likewise have disclosed campaign ancestry. This is selective source-exposed same-model synthesis, not blind replication, a new independent check or retained audit. The new review specifically checks the extended cap integral and late-tail domains; accepted symmetric windows alone would not establish them.

Only this draft NOTE.md was created. No scientific executable, new numerical experiment, source revision, Git/canonical/checkpoint/axiom/editable-prompt/model change, delegation, packet installation or publication occurred. No editable prompt changed. ROOT owns integration and publication, including actual base metadata and mechanical packaging verification.
