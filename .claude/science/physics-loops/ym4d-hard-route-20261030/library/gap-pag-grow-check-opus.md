# Check of gap-pag-grow-astra.md

- Checker: Claude Opus 5.5. Date: 2026-11-12. Cross-provider check: the author is Codex gpt-6-astra.
- Source: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-pag-grow-astra.md`, 887 lines, read in full.
- Context read: `gap-pag-corner-astra.md` (all 569 lines), `gap-pag-corner-check-opus.md` (all 80 lines), `gap-crux-exercise-astra.md` lines 749-984 (8.1) and 1194-1354 (8.4).
- Method: by hand only. No code was run. No numerical value decides anything below.
- Not read: the PR sources and SA/CA-I lines cited in the "Repo search" and Section 1 source paragraphs. I did not read SA 2773-2883 (AM2, AM5). Instead I re-derived the diagonal reflection positivity used in Lemma R myself (Section 5 below). So my verdict on Lemma R rests on my derivation, not on the SA text.
- Credit: every statement marked HOLDS is the author's result.

## Sections 0-1. Contract, notation, imported input, new scope

- Notation. For equal intervals of length $L$, the block interval at an endpoint is $[x_i-q,x_i+q]$ with $q=\lfloor 2L/3\rfloor$. Its side is $2q+1$. Correct.
- Imported input (1/49 quadratic correlation, (7) of the predecessor, $\beta_0(L)$ with no bound). This matches the checked predecessor and its Opus check. HOLDS.
- Source-scope paragraphs (lines 64-90) are ARGUED reading records. I did not re-read those sources. Not checked.
- Scope (1): $N=32(L+1)$, $H=2^{16}N^{20}$; the claim that $\beta\ge H^{100}$ makes the three errors at most $10^{-4}$. Checked through Sections 2-4 below. HOLDS.

## Section 2. Lemma G and Lemma T

Lemma G.
- Box side. For a §8.1 pair the union in one coordinate spans at most $\lfloor 2s_{i-1}/3\rfloor+s_i+\lfloor 2s_{i+1}/3\rfloor+1\le 14L/3+1$ sites, since $s\le 2L$. With a collar this is $\le 14L/3+3\le 8(L+1)$. So the patch embeds without wrapping in the auxiliary $N$-torus, $N=32(L+1)$. At identity exterior the conditional law depends only on $S$ and its touching plaquettes, which are local. So the embedding preserves the law. Correct.
- Base point $r$ with all four coordinates outside the bounding intervals: exists since $N>8(L+1)$. The exterior-graph connectivity is the predecessor's argument; it transfers to the auxiliary torus unchanged (complement of a proper box is connected; boundary vertices in $D$ attach by an incoming exterior link). Correct.
- Walk length. Exterior path $\le N^4-1$, forest path $\le N^4-1$, twice, plus $e$: at most $4N^4-3\le 4N^4+1\le 5N^4=M$. Correct (the note's bound is slightly loose).
- Transport of the walk in the slice is $U_e$, since forest links and exterior links are $I$. Correct.
- Sorting. A stable sort of a word of length $\le M$ into four direction groups needs at most $M(M-1)/2\le M^2$ adjacent swaps. Each swap of different directions inserts a conjugated plaquette loop, so the transport changes by at most $\|U_p-I\|$ in operator norm. After sorting and cancelling reversals, each one-direction block has net displacement $\equiv 0 \bmod N$, since the walk is closed. So the walk returns to $r$ after each block and each block winds around the coordinate circle through $r$. Those circles lie outside the bounding box in the other three coordinates, so they are exterior and have transport $I$. Correct.
- $\|U_p-I\|=2\sin(\theta_p/2)=\sqrt{2(1-x(U_p))}\le\sqrt{2\mathcal S}$. Non-touching plaquettes have all links exterior, so defect zero. Correct.
- $2\sin(a/2)\ge 2a/\pi\ge a/2$ on $[0,\pi]$. So $|A_e|^2\le 8M^4\mathcal S$. With at most $4N^4$ links: $|A|^2\le 32\cdot 625\,N^{20}\mathcal S=20000N^{20}\mathcal S\le H\mathcal S$, since $2^{16}=65536$. And $m\le 12N^4\le H$. HOLDS.

Lemma T.
- Lower bound $Q\ge |A|^2/H$: scale $A\to tA$ in (2) and use $\mathcal S(tA)=Q(tA)+O(t^3)$. Correct.
- Upper bound: a plaquette curl has at most 4 terms, so $(CA)_p^2\le 4\sum_{e\in p}A_e^2$; each link is in 6 plaquettes. So $\|CA\|^2\le 24|A|^2$, $Q\le 12|A|^2$. Correct.
- Quadratic term. To second order $\prod_k e^{iX_k}=I+i\sum X_k-\tfrac12\sum X_k^2-\sum_{j<k}X_jX_k$, so $1-x=\tfrac12|\sum_k A_k|^2$ per colour sum. This is $Q$ per plaquette. Correct.
- Remainder. Each $t$-derivative brings down a factor $iA_k\cdot\sigma$ of norm $|A_k|$, so $|f'''|\le(\sum|A_e|)^3$. Taylor gives $\le(\sum|A_e|)^3/6$ per plaquette. Hölder gives $(\sum_1^4 a_i)^3\le 16\sum a_i^3$. Six plaquettes per link: total $\le 16\sum_e|A_e|^3\le 16|A|^3$. HOLDS.

## Section 3. Lemma M and Corollary M1

Lemma M.
- Haar density in exponential coordinates is $(\sin|A|/|A|)^2$. Correct. $Q(Y)=\beta Q(A)$ by homogeneity.
- On $|Y|\le R=\beta^{1/12}$: $|A_e|\le\beta^{-5/12}\le 1$. From $\sin a/a\ge 1-a^2/6$ and $\log(1-s)\ge -2s$: $\log j\ge -\tfrac23\sum a_e^2\ge -|A|^2$, so $|\log j|\le\beta^{-5/6}$. Also $\beta|\mathcal S-Q|\le 16|Y|^3\beta^{-1/2}\le 16\beta^{-1/4}$. Sum $\le 17\beta^{-1/4}\le 17H^{-25}$. With $|e^s-1|\le 2|s|$ for $|s|\le1/2$: $|w/g-1|\le 34H^{-25}\le H^{-23}$. Correct.
- Tails: $w\le e^{-\beta\mathcal S}\le e^{-|Y|^2/H}$ (using $j\le1$ and (2)); $g\le e^{-|Y|^2/H}$ by (3). $G\ge(\pi/12)^{m/2}$ from $Q\le 12|Y|^2$. On $|Y|>R$ split $e^{-|Y|^2/H}\le e^{-R^2/(2H)}e^{-|Y|^2/(2H)}$; the comparison integral is $(2\pi H)^{m/2}[1+H^2m(m+2)]$. With $m\le H$ the bracket is $\le 4H^4$. This gives (5). The log of the prefactor is $\le 2H^2$; the exponent is $\le -H^{15}/2$ since $\beta^{1/6}\ge H^{100/6}\ge H^{16}$. So $\tau=H^{-30}$ is safe. Correct.
- Gaussian covariance norm $\le H/2$ (from $Q\ge|Y|^2/H$). $\mu_g(1+|Y|^4)\le 1+(H/2)^2m(m+2)\le 4H^4$. Difference of integrals over $G$: $\le 4\epsilon H^4+2\tau\le 5H^{-19}$; normaliser: $|\int w/G-1|\le\epsilon+2\tau\le 2H^{-23}$. My own combination gives an expectation error $\le 5H^{-19}(1+3H^{-23})+4H^4\cdot 3H^{-23}\le 13H^{-19}$. The note's $26H^{-19}$ is looser and also valid. $26H^{-19}\le H^{-17}$. HOLDS.

Corollary M1.
- $0\le q_e\le|Y_e|^2/2$ and $|q_e-q_e^0|\le|Y_e|^4/(24\beta)$, by $0\le 1-\cos a\le a^2/2$ and $|1-\cos a-a^2/2|\le a^4/24$. Correct. Readouts and products are bounded by $1+|Y|^4$, so (4) applies.
- Product readout error $\le 2\cdot\frac{|Y|^4}{24\beta}\cdot\frac{|Y|^2}{2}=|Y|^6/(24\beta)$. Gaussian moments: $|Y|^2\le(H/2)|Z|^2$ pointwise after diagonalising, so $\mathbb E|Y|^4\le(H/2)^2m(m+2)\le 3H^4$ and $\mathbb E|Y|^6\le(H/2)^3m(m+2)(m+4)\le 15H^6$ for $m\le H$. Readout error $\le H^{-94}$. Correct.
- Gaussian means $3a/2,3b/2\le 3/4$ (three colours, $a,b\le 1/2$ from the checked predecessor). Variance/covariance error $\le 2H^{-17}+2H^{-17}(3/2+2H^{-17})\le 6H^{-17}\le 10^{-4}$. Correct.
- $\beta^2\operatorname{Var}x(p_U)=\operatorname{Var}q_U$, and $V_U=3a^2/2$ is the Gaussian variance of $q_U^0$. So (6) is exactly the predecessor's premise in §4.1. HOLDS.
- This is a full compact-law statement: the tail of the compact measure is bounded, not truncated. No mass-gap input.

## Section 4. Theorem P and the explicit rate (7)

- Theorem P: (6) plus the predecessor's implication (7) gives correlation $\ge 1103/61397>1/64$ at identity exterior. Continuity in the finitely many exterior links of touching plaquettes gives an open set of positive Wilson marginal measure. HOLDS. The open set depends on $\beta$, the cover and the pair, as stated.
- Rate (7): $\beta\ge 2^{30000}$ gives $L=\lfloor\beta^{1/4000}\rfloor\ge\lfloor 2^{7.5}\rfloor=181\ge12$. $H^{100}=2^{1600}\cdot 32^{2000}(L+1)^{2000}=2^{11600}(L+1)^{2000}$. With $L+1\le 2L$: $\le 2^{13600}\beta^{1/2}$, which is $\le\beta$ once $\beta\ge 2^{27200}$. Correct. $H$ is increasing in $L$, so every $12\le L\le\beta^{1/4000}$ works. HOLDS.
- OPEN/limitation paragraph: correct; Theorem P alone says nothing about fast growth or order-one $\beta$.

## Section 5. Symmetric geometry and Lemma R

Geometry (8).
- B's coordinate-1 interval $[-L,2q-L]$ and C's $[0,2q]$ are neighbouring block intervals (centres differ by $L$); overlap $[0,2q-L]$ has $2q-L+1\ge 4$ sites for $L\ge12$ ($2q-L\ge L/3-4/3>2$). Same in coordinate 2 with roles swapped. So C is right of B in coordinate 1 and below it in coordinate 2: the GC1/face-corner pattern.
- $v=(0,0,a_3,t)$, $z=v-e_1$ in B only, $w=v-e_2$ in C only, $u$ in neither. Checked coordinate by coordinate. Correct.
- $\theta(x_1,x_2,x_3,x_4)=(x_2,x_1,x_3,x_4)$ maps $[-L,2q-L]\times[0,2q]$ to $[0,2q]\times[-L,2q-L]$, so $\theta B=C$. $\theta z=w$, and $\theta$ maps the positive link $(z,1)$ to the positive link $(w,2)$. So $\theta U=V$. Assignment by base commutes with $\theta$. $e_0$ is fixed. Correct.
- All-torus construction: $N=nL+r$, $n\ge12$; $n-1$ intervals of $L$ and one of $L+r<2L$, all in $[L,2L]$; at least 11 consecutive length-$L$ intervals contain the three read intervals in each of coordinates 1 and 2. $K,J$ are arbitrary common intervals. Correct.
- HOLDS.

Lemma R. My own derivation of the diagonal reflection positivity (I did not read SA AM2/AM5):
- Height $h=x_1-x_2$. Direction-1 links change $h$ by $+1$, direction-2 links by $-1$, directions 3,4 by 0. So no link joins $h>0$ to $h<0$. Direction-3,4 links at $h=0$ are fixed pointwise by $\theta$.
- A $(1,2)$ plaquette at base height $h$ has vertex heights $h,h+1,h,h-1$. It meets both strict halves iff $h=0$. $(1,3),(1,4)$ plaquettes use heights $\{h,h+1\}$; $(2,3),(2,4)$ use $\{h,h-1\}$; $(3,4)$ use $\{h\}$. So every other plaquette lies in a closed half.
- At $h=0$ base $x$: $P_+=(x,1)(x+e_1,2)$ through height $+1$ and $P_-=(x,2)(x+e_2,1)$ through height $-1$, and $\theta P_+=P_-$. Since $\tfrac12\operatorname{tr}(AB^{*})=a\cdot b$ for unit quaternions, the factor is $e^{-\beta}\exp[\beta s(P_+)\cdot s(P_-)]$. Its Taylor expansion is a sum, with nonnegative coefficients, of products $f_\alpha(\text{upper})f_\alpha(\theta\,\text{upper})$. The half actions are $\theta$-images of each other because $S$, its exterior (all $I$) and the touching-plaquette set are $\theta$-invariant, and plaquette traces are orientation-blind. So $\int G\,(G\circ\theta)\,d\mu\ge0$ for real upper-half $G$: the standard argument.
- Deleted plaquettes. $u$ has height 0, so $p$ (base $u$) is a crossing plaquette with $P_+=(u,1)V$, $P_-=(u,2)U$; its factor is $e^{\beta u\cdot v}$. $p_U$ has vertex heights $-1,0,0,-1$: closed lower half. $p_V=\theta p_U$: closed upper half. So deleting $\{p,p_U,p_V\}$ removes one crossing factor and a reflected pair of half factors. Positivity survives. $U$ is in the lower half (heights $-1\to0$), $V$ in the upper half. Testing with $G=\varphi(V)$ gives $\iint\varphi(u)\varphi(v)K(u,v)\,du\,dv\ge0$ for the deleted two-link kernel $K$. Correct.
- $K=\text{const}\cdot R_\beta$: after deleting $p,p_U,p_V$, the remaining factors are the eight $U,V$-dependent plaquettes and the $U,V$-independent ones, exactly the predecessor's (8). Correct.
- Continuity ($R_\beta$ is a finite compact integral of a smooth integrand) turns integral positivity into pointwise Gram positivity. Symmetry from $\theta$. Simultaneous conjugation (a constant gauge) fixes the exterior $I$. HOLDS.
- Positivity is proved only at the $\theta$-invariant identity exterior. The note uses it only there and then uses continuity. Correct use.

Immediate consequence (artificial factor). With Haar marginals, $\mathbb E_v[v\,e^{-\beta u\cdot v}]=-c(\beta|u|)\,u$ with $c>0$, so the form on $u_1$ is $-\mathbb E[c\,u_1^2]<0$. HOLDS.

## Section 6. Lemma V and Theorem R1

Lemma V.
- One-link law: the six plaquettes containing a link each give $\beta\,x(US_p)=\beta\,u\cdot w_p$ with $w_p$ a unit quaternion. So the density is $\propto e^{\kappa h\cdot u}$, $\kappa h=\beta\sum_p w_p$, $0\le\kappa\le 6\beta$. Haar on SU(2) is the uniform law on $S^3$, invariant under all of O(4). Correct.
- $u_0=t$ has density $\propto(1-t^2)^{1/2}$ on $S^3$. Transverse moment: $\mathbb E u_1^2=\mathbb E[(1-t^2)/3]=J_3/(3J_1)$. Correct.
- IBP 1: $\frac{d}{dt}[e^{\kappa t}(1-t^2)^{3/2}]=\kappa e^{\kappa t}(1-t^2)^{3/2}-3te^{\kappa t}(1-t^2)^{1/2}$; boundary terms vanish; so $\kappa J_3=3J_1'$. Correct.
- IBP 2: $\frac{d}{dt}[te^{\kappa t}(1-t^2)^{3/2}]=e^{\kappa t}(1-t^2)^{3/2}+\kappa te^{\kappa t}(1-t^2)^{3/2}-3t^2e^{\kappa t}(1-t^2)^{1/2}$, and $\int t^2e^{\kappa t}(1-t^2)^{1/2}=J_1-J_3$. So $0=J_3+\kappa J_3'-3J_1+3J_3$, i.e. $3J_1=4J_3+\kappa J_3'$. Correct.
- So the transverse moment is $1/(4+\kappa b)$ with $b=J_3'/J_3$ the mean of $t$ under weight $e^{\kappa t}(1-t^2)^{3/2}$. $b\le1$ since $|t|\le1$; $b\ge0$ by pairing $\pm t$ since $\kappa\ge0$. Correct.
- Longitudinal moment $=1-3T\ge T$ iff $T\le 1/4$, true. For a unit direction $e$, $\mathbb E(e\cdot u)^2=(e\cdot h)^2\mathbb E t^2+(1-(e\cdot h)^2)T\ge T$ (cross terms vanish by transverse symmetry). So every coordinate second moment is $\ge 1/(4+6\beta)$. Averaging over the other links gives (9). The bound holds for every exterior.
- Zero vector means from conjugation (SO(3) acts on the vector part with no fixed vector). $\mathbb E u_1^2=\mathbb E v_1^2$ from $\theta$. HOLDS.

Theorem R1.
- $k_{UV}$ lower-bounds the invariant angle: functions of $U$ alone (resp. $V$) are invariant under interior gauges (all endpoints of $U,V$ are boundary vertices) and lie in $\operatorname{ran}E_C$ (resp. $\operatorname{ran}E_B$); for such mean-zero $f,g$, $\langle g,(E_BE_C-E_S)f\rangle=\langle g,f\rangle$. Correct.
- (11): $p\propto e^{\beta(u_0+v_0)}e^{\beta u\cdot v}R_\beta$ from the predecessor's (8) with $x(U)=u_0$, $x(UV^{-1})=u\cdot v$. For $t\le\beta$, $e^{(\beta-t)u\cdot v}$ is a nonnegative-coefficient Gram series; Schur products and one-body factors preserve pointwise positivity. So $K_t$ is positive semidefinite. Correct.
- (12): $C(h)\ge0$ by positivity of $p$ on $h-m(h)$; $C(h)\le k_{UV}\operatorname{Var}_m h$ by definition. Correct.
- Expansion: $\mathbb E_p[u_1v_1e^{-tu\cdot v}]=\sum_n\frac{(-t)^n}{n!}\sum_{|I|=n}\mathbb E_p[h_I(u)h_I(v)]=J_t+\sum_n\frac{(-t)^n}{n!}\sum_I C(h_I)$. Correct.
- (13): given $u_0=a$, $v_0=b$ under $m\otimes m$, directions are independent uniform on $S^2$; $\mathbb E[n_1n_1'\mid n\cdot n'=z]=z/3$, $z$ uniform on $[-1,1]$. So the conditional integral is $e^{-tab}\frac{rs}{3}\mathbb E[ze^{-trsz}]=-e^{-tab}\frac{rs}{3}\mathbb E[z\sinh(trsz)]\le -e^{-t}\frac{t\,r^2s^2}{9}$, using $z\sinh(kz)\ge kz^2$, $\mathbb E z^2=1/3$, $e^{-tab}\ge e^{-t}$. With $m(r^2)=3a_1$: $J_t\le -te^{-t}a_1^2$. Correct.
- Odd terms are $\le0$ and dropped. Even terms: $C(h_I)\le k\,m(h_I^2)$ and $\sum_{|I|=n}h_I^2=u_1^2|u|^{2n}=u_1^2$, giving $k\,a_1\cosh t$. Absolute convergence: total $\le a_1e^t$. Correct.
- $0\le -te^{-t}a_1^2+k a_1\cosh t$ gives $k\ge a_1\cdot 2t/(e^{2t}+1)$; with (9) this is (10). Uniform in $L$. HOLDS.

## Section 7. Theorem R2 and the witness family (14)

- $1\le\beta\le4$, $t=1$: $e^2+1<10$, so $k>\frac{2}{10(4+6\beta)}=\frac1{5(4+6\beta)}\ge\frac1{140}$. $1/2\le\beta\le1$, $t=\beta$: $2\beta/(4+6\beta)\ge 1/7$ (increasing), $e^{2\beta}+1<10$, so $k>1/70$. $e<3$ from $n!\ge 2^{n-1}$. HOLDS.
- Count: $1+4^2+4^4=273$ ordered words (with repeats as functions). Correct.
- Witness argument with $t=\min(\beta,1)\le1$: if every listed $h_I$ has correlation $\le1/160$, the even part is $\le a_1[\frac1{160}(1+\frac12+\frac1{24})+\sum_{n\ge6\text{ even}}\frac1{n!}]$. $\frac{37}{24\cdot160}=\frac{37}{3840}<\frac1{100}$ ($3700<3840$). Even-term ratio $t^2/((n+1)(n+2))\le 1/56$ for $n\ge6$, so the tail is $\le\frac{1}{720}\cdot\frac{56}{55}=\frac{7}{4950}<\frac1{700}$ ($4900<4950$). Sum $<\frac{8}{700}=\frac{2}{175}<\frac1{84}$ ($168<175$). Correct.
- Needed: $te^{-t}a_1>1/84$. For $1\le\beta\le4$: $e^{-1}/28>1/84$. For $1/2\le\beta\le1$: $te^{-t}\ge\frac12e^{-1/2}>0.3$ and $a_1\ge1/10$, so $>1/60$. Then $0\le J_t+\dots<0$, a contradiction. Correct. The family is fixed (independent of $\beta\in[1/2,4]$ and of $L$). Positive variances: each $h_I$ is nonconstant and the marginal density is positive ($R_\beta\ge e^{-8\beta}$). HOLDS.
- Gauge quantifier: functions of $U$ or $V$ alone are interior-gauge invariant. Correct.
- Decorated loops. The three $(1,2)$ plaquettes at $(-2,-2,a_3-3,t+3j)$ have all links with third coordinate $a_3-3\notin K$, so they are exterior; any plaquette containing a modified link has third coordinates in $\{a_3-4,\dots,a_3-2\}$ and contains no link of $S$. So the conditional law on $S$ is unchanged. The paths (down two exterior direction-3 links from $z$ or $w$, across the layer $x_3=a_3-2$, down one link) avoid the modified direction-1 links and have transport $I$. With $U=u_0+i\,u\cdot\sigma$: $\tfrac12\operatorname{tr}(-i\sigma_jU)=u_j$. A global sign convention would flip $u_j$ for both $U$ and $V$ alike and leave every correlation unchanged. Correct.
- Open neighbourhood: bounded continuous functions; conditional density continuous in the finitely many exterior links read. HOLDS.
- OPEN/distinction paragraph: correct; R2 does not bound the elementary traces $x(p_U),x(p_V)$.

## Section 8. Lemmas I, W and Theorem R3

Lemma I.
- Reduction to the one-link law $e^{\kappa h\cdot u}/Z_\kappa$, $\kappa\le6\beta$, then average. Correct.
- Direction. $(1-u_0^2)^{-1}=\sum_j u_0^{2j}$ a.e.; the odd part of $e^{\kappa h\cdot u}$ integrates to zero against even functions. Gaussian check: $\mathbb E\exp(sG_0+t\,h\cdot G)=\exp(\tfrac12|se_0+th|^2)=e^{s^2/2}e^{t^2/2}e^{h_0st}$. The $s^{2j}t^{2k}$ coefficient has only even powers $h_0^c$ ($2a+c=2j$), all with positive coefficients. Dividing by $\mathbb E R^{2j+2k}>0$ gives the spherical moments. Each is maximal at $h_0^2=1$; $Z_\kappa$ does not depend on the direction; monotone convergence handles the nonnegative double series. Correct.
- Aligned case. $\frac{d}{dt}[t\sqrt{1-t^2}e^{\kappa t}]=2\sqrt{1-t^2}e^{\kappa t}-(1-t^2)^{-1/2}e^{\kappa t}+\kappa t\sqrt{1-t^2}e^{\kappa t}$, using $t^2(1-t^2)^{-1/2}=(1-t^2)^{-1/2}-(1-t^2)^{1/2}$. Boundary terms vanish. So $J_{-1}=2J_1+\kappa J_1'$ and $J_{-1}/J_1\le 2+\kappa$. Correct.
- Sanity: at $\beta=0$, $\mathbb E_{\rm Haar}r^{-2}=\frac2\pi\int_0^\pi d\theta=2$, the bound's value. HOLDS. Uniform in $L$ and in the exterior.

The sign in (18).
- Conjugation invariance: $(L_i^u+L_i^v)R_\beta=0$ for each $i$. Apply $L_i^u$ and sum: $\Delta_uR_\beta=-\sum_iL_i^uL_i^vR_\beta$. So (18) has the right sign.
- Positivity of $L^uL^vR$ for one generator: it is the limit of the second mixed difference $[R(gu,gv)-R(gu,v)-R(u,gv)+R(u,v)]/\delta^2$, $g=e^{\delta L}$. For points $u_j$ and coefficients $a_j$ this is the Gram form of $R$ on the $2n$ points $\{gu_j,u_j\}$ with coefficients $\{a_j/\delta,-a_j/\delta\}$, hence $\ge0$. $R_\beta$ is smooth, so the limit exists. (Equivalently, $\iint\varphi\varphi\,L^uL^vR=\iint(L\varphi)(L\varphi)R\ge0$, since $L$ is antisymmetric for Haar.) Correct. This step genuinely needs Lemma R.

Lemma W.
- Schur product with $e^{\beta u\cdot v}$ keeps positivity. Test function $\varphi=e^{\beta u_0}f(u_0)$.
- Integration by parts with a merely bounded radial $f$ is valid: $L_i$ generates rotations $g_s$ fixing $u_0$, $\varphi\circ g_s=\varphi$ exactly, and Haar is $g_s$-invariant. So $\int\varphi\,\psi\,L^2R=\int\varphi\,(L^2\psi)\,R$ with $\psi=e^{\beta u\cdot v}$ smooth. No derivative of $f$ appears. Correct.
- With $L_ib=e_i\times b$: $L_i(b\cdot c)=e_i\cdot(b\times c)$, so $\sum_i[L_i(b\cdot c)]^2=|b\times c|^2=r^2s^2-(b\cdot c)^2$. And $L_i^2(b\cdot c)=b_ic_i-b\cdot c$, so $\Delta(b\cdot c)=-2\,b\cdot c$. Correct.
- $\Delta_ue^{\beta u\cdot v}=e^{\beta u\cdot v}[-2\beta\,b\cdot c+\beta^2(r^2s^2-(b\cdot c)^2)]$. Then $0\le-\iint\varphi\varphi R\,\Delta_ue^{\beta u\cdot v}$, and $\varphi(u)\varphi(v)e^{\beta u\cdot v}R\propto f(u_0)f(v_0)\,p(u,v)$. This gives $2\beta\,\mathbb E[ff\,b\cdot c]\ge\beta^2\mathbb E[ff(r^2s^2-(b\cdot c)^2)]$. Sign correct.
- Singular limit $f=(r^2+\epsilon)^{-1}$: the right integrand is $\le r^2s^2/((r^2+\epsilon)(s^2+\epsilon))\le1$; the left is $\le 1/(rs)\le(r^{-2}+s^{-2})/2$, integrable with integral $\le M<\infty$ by (16) and symmetry. Pointwise limits hold off the null set $\{rs=0\}$. Dominated convergence gives (17). Correct.
- Sanity: at small $\beta$, $R_\beta=1+O(\beta^2)$ (each of the eight plaquettes has a free link occurring once), so $p\approx1+\beta(u_0+v_0+u\cdot v)$. Then the left side of (17) is $\beta\,\mathbb E_{\rm Haar}(n\cdot n')^2=\beta/3$ and the right side is $\frac\beta2(1-\frac13)=\beta/3$. So (17) is sharp at first order; the sign and constant are consistent. HOLDS.

Theorem R3.
- $m(A_i)=0$ and $m(B_{ij})=\delta_{ij}/3$ by conjugation invariance of $m$. $\sum_i\operatorname{Var}A_i=m(r^{-2})=M$. $\sum_{ij}\operatorname{Var}B_{ij}=1-3\cdot\frac19=\frac23$. Correct.
- If all twelve correlations are $\le k$: $\mathbb E\frac{b\cdot c}{r^2s^2}=\sum_i\operatorname{Cov}(A_i(U),A_i(V))\le kM$ and $\mathbb E(n\cdot n')^2\le\frac13+\frac{2k}3$. Then (17) gives $kM\ge\frac\beta2\cdot\frac23(1-k)$, so $k\ge\beta/(3M+\beta)\ge\beta/(6+19\beta)$. Correct. So the maximum of the twelve correlations is $\ge\beta/(6+19\beta)$, and so is $k_{UV}$.
- Variances: $M/3\ge1/3$ since $r\le1$; $m(n_i^4)=1/5$, $m(n_i^2n_j^2)=1/15$, so $4/45$ and $1/15$. Correct. $160\beta>6+19\beta\iff\beta>6/141=2/47$. Correct.
- Large-$\beta$ sanity: the bound tends to $1/19$, below the quadratic-model canonical correlation $c/\sqrt{ab}\ge1/7$. No conflict. HOLDS.
- The functions $A_i$ are unbounded but in $L^2$; PA_g's norm is over all invariant $L^2$ functions. Correct.

Bounded witness (20).
- One-link density $\le e^{2\kappa}\le e^{12\beta}$ (loose: $Z_\kappa\ge1$ by Jensen gives $e^{6\beta}$). The marginal inherits the bound. Correct.
- Haar error for $A_i$: integrand $\le\epsilon^2/(r^2(r^2+\epsilon)^2)$; Haar angle density $\frac2\pi\sin^2\theta$; result $\le\frac{4}{\pi}\int_0^\infty\frac{\epsilon^2\,d\theta}{(\theta^2/4+\epsilon)^2}=\frac{8\sqrt\epsilon}{\pi}\int_0^\infty\frac{dt}{(1+t^2)^2}\le\frac{16\sqrt\epsilon}{\pi}\le8\sqrt\epsilon$. For $B_{ij}$ the squared error is $\le\epsilon^2/(r^2+\epsilon)^2\le$ the same integrand. Correct.
- $\delta=\sqrt8\,e^{6\beta}\epsilon^{1/4}\le3e^{6\beta}\epsilon^{1/4}=3\cdot2^{-40}e^{-6\beta}(1+\beta)^{-2}<2^{-38}$. Normalized-vector error $\le2\delta/\sigma$ with $\sigma\ge1/\sqrt{15}$; correlation error $\le4\sqrt{15}\,\delta<16\delta<2^{-34}$. At $\beta\ge1/2$, (19) $\ge1/31$, and $1/31-2^{-34}>1/32$. Correct.
- Correction. Lines 51 and 738-740 call this "a fixed family of twelve" functions. The functions depend on $\beta$ through $\epsilon(\beta)$, which tends to zero as $\beta\to\infty$. They are explicit and independent of $L$, not independent of $\beta$. A $\beta$-independent $\epsilon$ is not supplied (at large $\beta$ the marginal concentrates at $r\sim\beta^{-1/2}$). HOLDS AFTER CORRECTION: read "an explicit, $L$-independent family of twelve functions for each $\beta\ge1/2$".
- Fully invariant realization, $2/47<\beta<1/2$ by small $\epsilon$, open exterior sets and the essential-supremum bound: each follows from $L^2$ convergence $A_i^\epsilon\to A_i$ (dominated by $|A_i|$) and continuity in the exterior. HOLDS.

## Section 9. The exact cover quantifier

What is refuted.
- For every $\beta>2/47$ and every integer $L\ge12$, on every torus side $N\ge12L$, there is a §8.1 cover at scale $\ell=L$ (equal intervals, or the one-remainder partition of §5) with an interacting pair (8), and a positive-measure open set of exteriors, on which the invariant pair norm exceeds $1/160$. The bound $\beta/(6+19\beta)$ does not depend on $L$, so any function $L(\beta)$ is allowed, including the trajectory $\ell_h=\lceil R/h\rceil$ with any $\beta_h>2/47$. So PA_g in the form "for every §8.1 cover, every pair, every (or almost every) exterior, uniformly in torus and $h$" is refuted. HOLDS.
- Both the every-exterior and the essential-supremum versions fail. HOLDS.

What is not refuted.
- PA_g for a cover family that contains no pair with the $\theta$-symmetry. PA_g with another link assignment, another boundary-gauge class, or a certificate over larger groups of blocks. The note says so. Correct.
- The elementary-trace correlation of $x(p_U),x(p_V)$ at growing $L$ and order-one $\beta$. OPEN, as the note says.
- Any statement about a mass gap. None is made.

Checker observations on scope (not new routes; they only sharpen the quantifier):
1. The proofs of Lemma R, R1, Lemma W and R3 use only the $\theta$-invariance of $S$ with $\theta U=V$. The note restricts to (8), which is safe. Any §8.1 face pair whose two coordinate data are $\theta$-symmetric is covered by the same proof; equal triples $(s_{i-1},s_i,s_{i+1})=(t_{j-1},t_j,t_{j+1})$ give such pairs. The note claims less than it proves here; this is not an error.
2. "Exists a cover" readings. On a torus of side $N\in[12\ell,12\ell+3]$ every §8.1 partition at scale $\ell$ has exactly 12 intervals (13 would need $13\ell>N$), and at most 3 of them exceed $\ell$. A 12-cycle with at most 3 marked positions has 3 consecutive unmarked ones. So coordinates 1 and 2 both contain an equal triple of length $\ell$, and the pair (8) is forced. At such sides even the reading "some §8.1 cover satisfies PA_g" fails. For $N\gg\ell$ a cover choice might avoid every symmetric pair; I did not decide this. The note's OPEN for such covers is correct.
3. No step uses a mass gap, clustering, an infinite-volume limit, or a Wilson association/monotonicity inequality. All estimates are finite-volume and local at a fixed exterior.

Obligations and failed routes (lines 861-875): consistent with what is proved. HOLDS.

## Verdict table

| # | Statement | Verdict |
|---|---|---|
| 1 | §0 imported face-pair input (1/49, predecessor (7), $\beta_0(L)$ unbounded) | HOLDS |
| 2 | §1 source-scope reading paragraphs | Not checked (sources not read) |
| 3 | §1 scope claim (1): $\beta\ge H^{100}$ gives errors $\le10^{-4}$ | HOLDS |
| 4 | Lemma G, (2) | HOLDS (walk length $4N^4-3$; stated bound loose but valid) |
| 5 | Lemma T, (3) | HOLDS |
| 6 | Lemma M, (4), (5) | HOLDS (final constant $26H^{-19}$ is loose; $13H^{-19}$ suffices) |
| 7 | Corollary M1, (6) | HOLDS |
| 8 | Theorem P | HOLDS |
| 9 | Explicit rate (7) | HOLDS |
| 10 | §5 geometry (8) and the all-torus construction | HOLDS |
| 11 | Lemma R (deleted-plaquette reflection positivity) | HOLDS (by my own derivation; SA AM2/AM5 not read) |
| 12 | Artificial factor $e^{-\beta x(UV^{-1})}$ is not positive | HOLDS |
| 13 | Lemma V, (9), one-link law, $J_1,J_3$ identities | HOLDS |
| 14 | Theorem R1, (10)-(13) | HOLDS |
| 15 | Theorem R2 constants ($1/140$, $1/70$) | HOLDS |
| 16 | Witness family (14), bound (15) | HOLDS |
| 17 | §7 gauge quantifier, decorated loops, open exterior sets | HOLDS |
| 18 | Lemma I, (16) | HOLDS |
| 19 | Sign of (18) and positivity of $\sum_iL_i^uL_i^vR_\beta$ | HOLDS |
| 20 | Lemma W, (17), including the singular-weight limit | HOLDS |
| 21 | Theorem R3, (19), failure for $\beta>2/47$ uniformly in $L$ | HOLDS |
| 22 | "Fixed family of twelve" bounded functions (lines 51, 738-740) | HOLDS AFTER CORRECTION (the twelve functions depend on $\beta$ through $\epsilon(\beta)$; fixed in $L$ only) |
| 23 | Bounded witness (20): error bounds and correlation $>1/32$ | HOLDS |
| 24 | §8 fully invariant realization, $2/47<\beta<1/2$, essential supremum | HOLDS |
| 25 | §9 growing-block decision (every $L(\beta)$, symmetric family) | HOLDS |
| 26 | §9 quantifier boundary (what is and is not refuted) | HOLDS (conservative: the proof covers every $\theta$-symmetric pair; on sides $N\in[12\ell,12\ell+3]$ the pair is forced in every §8.1 cover) |
| 27 | Hidden mass-gap assumption | None found |

RESULT: gap-pag-grow-astra.md HOLDS (credit Codex gpt-6-astra), with one wording correction: the twelve bounded witnesses for $\beta\ge1/2$ depend on $\beta$ through $\epsilon(\beta)$. Checked by hand by Claude Opus 5.5: Lemmas G, T, M, V, R, I, W and Theorems P, R1, R2, R3. PA_g fails, at every growth rate $L(\beta)$, on every §8.1 cover that contains the $\theta$-symmetric face pair (8). The pair angle is at least $\beta/(6+19\beta)>1/160$ for $\beta>2/47$, on a positive-measure open set of exteriors, uniformly in $L$ and the torus. The slow-growth rescaled-moment estimate holds for $\beta\ge[2^{16}(32(L+1))^{20}]^{100}$. Covers with no symmetric pair, the elementary-trace correlation at growing $L$, and any mass-gap statement remain OPEN; no step assumes a gap.
