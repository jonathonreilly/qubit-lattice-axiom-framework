# Line-by-line check of `library/gap-channel-astra.md`

Checker: Claude Opus 5.5 (cross-provider; the note's author is Codex gpt-6-astra max).
Source: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-channel-astra.md`, 1010 lines, read in full.
Inputs read: `gap-transfer.md` N.1–N.8, Sections 8, 9, 10; `gap-flux-exercise.md` 3.0, 3.1, 8.2–8.4;
`gap-es1-opus.md` Sections 1, 2, 3, 5, 6; `gap-es1-opus-check.md` verdicts and Section 1;
`gap-crux-fp.md` 3b.3; `gap-means-max.md` line 150 ((TM-tw)) and Step 0 of Theorem R.
Method: every constant and inequality re-derived by hand. No run, no enumeration.
This is a check only. No repository file was edited.

## Section 1. Symmetry labels

**(1) normalization.** $R_{B,m}=T_{B,m}/\lambda_0(B)$ with the periodic $\lambda_0$.
(TM-tw) gives $T_{B,m}\ge0$ trace class; (S3) gives every eigenvalue at most $\lambda_0(B)$.
So $0\le R_{B,m}\le1$. HOLDS.

**1.1 group and (2).** Translation by $x$ conjugated by a signed permutation $R$ (about a site) is translation by $Rx$. HOLDS.
For the flips: a quarter turn about a site axis maps the flip plane of $C_1$ (links $(x,1)$, $x_1=0$) exactly onto that of $C_2$.
But a reflection $x_k\mapsto-x_k$ maps the $k$-links at $x_k=0$ to the reversed $k$-links at $x_k=-1$.
So $U_RC_sU_R^{-1}=C_{Rs}$ holds only up to a site centre gauge, that is, on $\mathcal H_{\rm inv}$.
I checked the plane-translation step: with $h(x)=-1$ on $x_k=1$, $(h\cdot u)$ flips exactly the $k$-links at $x_k=0$ and $x_k=1$.
So two flip planes differ by a site gauge. The note proves this in its covariance proof but prints (2) without the restriction.
Verdict: HOLDS AFTER CORRECTION. State the $C_s$ half of (2) on $\mathcal H_{\rm inv}$ (the transfer space), not on $L^2(X)$.
Translation–flip commutation on $\mathcal H_{\rm inv}$: HOLDS. Group $(A_B\times\mathbb F_2^3)\rtimes K_B$, with $K_B$ acting on $\mathbb F_2^3$ by its permutation part: HOLDS.

**(3), (4), labels.** $U_RQ_pU_R^{-1}=|A|^{-1}\sum_xe^{-ip\cdot x}U_{Rx}=Q_{Rp}$ since $p\cdot R^{-1}y=(Rp)\cdot y$. Same for $P_q$. HOLDS.
The normal subgroup $A_B\times\mathbb F_2^3$ is abelian and the extension is split, so Mackey's little-group method applies with ordinary (not projective) little-group irreps. HOLDS.
Inversion fixes $p$ iff $p_i\in\{0,\pi\}$. HOLDS. Ten $O_h$ labels at $p=q=0$. HOLDS. The counting warning (per pair vs induced) is correct.

**Charge conjugation.** With $U=\begin{pmatrix}a&-\bar b\\ b&\bar a\end{pmatrix}$, I computed $JUJ^{-1}=\begin{pmatrix}\bar a&-b\\ \bar b&a\end{pmatrix}=U^*$.
So $\mathcal C$ is the constant site gauge $h\equiv J$. It acts as $1$ on gauge-invariant functions. A twist $(-1)^{b_p}\operatorname{tr}U_p$ is unchanged, and the gauge group is the same. HOLDS. $(1-\mathcal C)/2=0$: HOLDS.

**1.2 stabilizer.** A permutation maps the class $m$ to its permuted image; $(1,0,0)\mapsto(0,1,0)$ under $1\leftrightarrow2$. Only the stabilizer of $[b]$ acts on a fixed twisted space. HOLDS.

**(5), (6).** Link signs $(-1)^{\eta}$ change $\operatorname{tr}U_p$ by $(-1)^{(d\eta)_p}$. They leave $u_\ell v_\ell^{-1}$ (temporal kernel), Haar measure and gauge projection unchanged (centre commutes).
If $g[b]=[b]$, then $b+gb$ is exact, so $\eta$ exists. HOLDS.
Composition $(g,\eta)(h,\xi)=(gh,\eta+g\xi)$: checked by applying $(h,\xi)$ then $(g,\eta)$. HOLDS.
Exact cochains $d\theta$ are site centre gauges and form a normal subgroup: $(g,\eta)(1,d\theta)(g,\eta)^{-1}=(1,d(g\theta))$. HOLDS.
Kernel: $(1,\eta)$ with $d\eta=0$, modulo exact, is $H^1(B;\mathbb F_2)\cong\mathbb F_2^3$ (winding flips). Surjectivity from existence of $\eta$. HOLDS.

**(6a).** $b$ is the stack $x_i=L_i-1,\ x_j=L_j-1$, all $x_k$; it is closed (each cube on the stack holds two of its plaquettes).
$d\eta_i$: a $j$-link at $(x_i=0,x_j=L_j-1)$ lies in the $ij$-plaquettes based at $x_i\in\{L_i-1,0\}$, $x_j=L_j-1$. These are the two rows of $b+\tau_ib$. In $jk$-planes the $j$-links of $\eta_i$ come in adjacent pairs along $k$, so they cancel. The $jk$ part of $b$ is $\tau_i$-invariant. HOLDS.
Commutator: $\eta_i+\tau_i\eta_j+\eta_j+\tau_j\eta_i$. The $k$-link parts cancel because each is invariant under the other shift. The $ij$ part is the four links in the $ij$-plane at the site line $x_i=x_j=0$, which is $d\theta$ for $\theta$ the indicator of that line ($k$-links inside the line contribute zero). HOLDS.
$S_i^{L_i}=(1,\sum_{r<L_i}\tau_i^r\eta_i)$ flips all $j$-links at $x_j=L_j-1$, which is $C_j$ up to a site gauge. HOLDS.
Phase: $e^{ip_iL_i}=(-1)^{\sum_j\mathfrak m_{ij}q_j}$ and the half-shift formula follow. HOLDS.
Idempotence of $L^{-1}\sum_{r<L}e^{-ipr}S^r$ when $S^L=e^{ipL}$: the sum over $r+r'$ is periodic mod $L$. HOLDS.
Lift ambiguity by closed $\xi$ multiplies $S_i$ by $C_\xi$, a centre character at fixed $q$. HOLDS.
This matches 't Hooft's fractional momentum in charged twisted sectors.

## Section 2. Channel projectors and density

**(7) centre charges.** $C_s$ multiplies each crossed link by the central $-1$. A loop crosses the plane $x_k=0$ a net $w_k$ times, and backtracking crossings come in pairs. So $C_sW_\ell=(-1)^{s\cdot w}W_\ell$. HOLDS.

**(8) Schur identities.** I substituted $h=g^{-1}k$ and used $D^\gamma_{kl}(g^{-1}k)=\sum_m\overline{D^\gamma_{mk}(g)}D^\gamma_{ml}(k)$.
Then $\sum_g\overline{D^\alpha_{ij}(g)}D^\gamma_{mk}(g)=(|G|/d_\alpha)\delta_{\alpha\gamma}\delta_{im}\delta_{jk}$ gives $E^\alpha_{ij}E^\gamma_{kl}=\delta_{\alpha\gamma}\delta_{jk}E^\alpha_{il}$.
$(E^\alpha_{ij})^*=E^\alpha_{ji}$ follows from $U_g^*=U_{g^{-1}}$ and $D(g^{-1})=D(g)^\dagger$. HOLDS.
The $U_g$ must be a genuine representation. For (6) this holds because the action factors through the quotient by site gauges. HOLDS.

**(9) and signs.** $O_h=O\times\{1,\mathcal I\}$, so separate $O$ and $\mathcal I$ projectors are legitimate. $Q_0$, $P_0$ commute with all $U_R$.
The sign of the matrix coefficient depends on whether $U_RW_\ell=W_{R\ell}$ or $W_{R^{-1}\ell}$. The other convention replaces $\overline{D_{ij}(R)}$ by $D_{ji}(R)$, still an element of the same isotypic block. Not an error. $c=-1$ gives zero. HOLDS.
Omitting the parity projector when $\mathcal I$ does not fix $p$: correct. Twisted loop images carry the signs $(-1)^{\eta(g\ell)}$: correct.

**Cubic table.** Characters on $O$: $xyz$ has $\chi(C_4)=-1$, $\chi(C_3)=1$, $\chi(C_2)=1$, $\chi(C_2')=-1$, which is $A_2$.
On $(yz,zx,xy)$ a quarter turn about $z$ has trace $-1$; on $(x,y,z)$ it has trace $+1$. So $T_2\neq T_1$.
The Klein subgroup $\operatorname{diag}(\pm1,\pm1,\pm1)$, $\det=1$, has three distinct characters on each $T$ basis, and permutations are transitive, so both are irreducible.
$E$ is the standard irrep of $S_3$ on $x^2,y^2,z^2$ modulo constants. $1+1+4+9+9=24$. HOLDS.

**Plaquette sums.** $\operatorname{tr}U^{-1}=\operatorname{tr}U$, so $L_i$ transforms like $x_i^2$ (permutation, signs irrelevant). Inversion fixes each $L_i$. So $A_1^+\oplus E^+$, and the displayed $E^+$ basis matches $(2z^2-x^2-y^2,x^2-y^2)$.
All gauge-invariant one-plaquette functions are class functions of $U_p$; at $p=0$ they give the same permutation representation. So no $T$ and no odd parity. HOLDS.

**(9a).** Each clover plaquette based at $x$ transforms by $h(x)\cdot h(x)^{-1}$. Under $x_1\mapsto-x_1$: $B_1\mapsto B_1$ and $B_2,B_3\mapsto-B_2,-B_3$ (orientation of the 12 and 13 plaquettes reverses), so $B$ is axial.
$B_iB_j$ then transforms like $x_ix_j$ under all of $O_h$, parity even. Off-diagonal part is $T_2^+$. HOLDS.

**(9b).** Gauge covariance: $U_j(x)B_k(x+e_j)U_j(x)^{-1}\mapsto h(x)(\cdot)h(x)^{-1}$; the backward term the same. Checked.
Under inversion the forward and backward transports exchange, so $\nabla_j\mapsto-\nabla_j$ at $-x$; $B$ is unchanged. Under a general $R\in O_h$, $\varepsilon_{ijk}R_{ia}R_{jb}R_{kc}=\det R\,\varepsilon_{abc}$, with $\det R$ from each $B$, so the total factor is $(\det R)^3=\det R$. Pseudoscalar: $A_1^-$. HOLDS.
Only the transformation law is claimed; non-vanishing is not claimed. Correct scope.

**(10) and $\Omega_m$.** The twisted transfer has a strictly positive kernel by (TM-tw) as stated in `gap-flux-exercise.md` 3.0. The Perron–Frobenius argument of `gap-transfer.md` A2–A3 then gives a simple positive top eigenvector.
Configuration symmetries map positive functions to positive functions, so they fix $\Omega_m$. Pullbacks are multiplicative, so $U_g(W\Omega_m)=(U_gW)\Omega_m$ and (10) follows. HOLDS.
Note: the summary of (TM-tw) in `gap-es1-opus.md` Section 1 does not list positivity of the twisted kernel; the source 3.0 does. The note cites only "simplicity". Cite 3.0. Not a gap.

**Separation of orbits.** $\operatorname{tr}V_j=2s_j$. $\operatorname{tr}V_iV_j=2(s_is_j-v_i\cdot v_j)$. $\operatorname{tr}[(a\cdot\sigma)(b\cdot\sigma)(c\cdot\sigma)]=2i\,a\cdot(b\times c)$, so length-three words give the triple products.
Equal Gram matrices give an orthogonal map on the span. With full span the triple product of a basis fixes $\det=+1$; otherwise extend with $\det=+1$. Lift $SO(3)\to SU(2)$. HOLDS.

**Density and limits.** The loop-trace algebra is real (SU(2) traces are real), unital and separating on the compact orbit space. Stone–Weierstrass applies. Gauge-averaging of $C(X)$ gives density of continuous invariant functions in $\mathcal H_{\rm inv}$.
$\Omega_m$ is continuous with $\Omega_m\ge c>0$ (eigen-equation with a kernel bounded below). So $\|W\Omega_m-f\|\le\|\Omega_m\|_\infty\|W-f/\Omega_m\|$. Bounded projectors keep density. HOLDS.
Limit: density says nothing about a finite basis or about overlaps. Correctly stated. HOLDS.

## Section 3. Channel forms and conditional single-state dominance

**(11).** $E\ge0$ by (S3). $F_{z,\alpha}(t)=\operatorname{Tr}(\Pi_{z,\alpha}R^t)$ is finite for $t\ge1$ (trace class). The isotypic block is $V_\alpha\otimes M_\alpha$ and commuting operators are $1\otimes A$, so the trace is $d_\alpha\operatorname{Tr}_MA^t$. HOLDS.
If $\alpha$ runs over (individual $p$, irrep of $K_{B;p,q}$), the projectors resolve the identity. So every eigenvector is counted once. HOLDS.

**(12).** $\Omega$ is fixed by every $U_g$, so it lies in the trivial block. HOLDS.

**(13).** $S_{\rm ev}(a;a^3)=\operatorname{Tr}(P_0R^a)-1$, and the vacuum contributes exactly $1$. All terms are $\ge0$. HOLDS.

**(14).** Matches `gap-means-max.md` line 29 and Step 0. $\epsilon\ge0$ trivially; $\delta\ge0$ by Lemma K (b) applied to each $\Delta_i$. HOLDS.

**(15), (16).** $Z_z(a;A)/\lambda_0(A)^a=\sum_\alpha F_{z,\alpha}(a;A)$ and $Z_0(a;A)/\lambda_0(A)^a=1+\epsilon_A$. So $p_z=\sum_\alpha w_{z,\alpha}$. $H_L$ equals the $H_L$ of `gap-es1-opus.md` Section 1. HOLDS.
Orbit caution (no automatic factor 24 or 48; $A$ need not be a cube; $X$ is not cube-invariant): HOLDS.

**(17), (18).** $Z_z(2a;A)=\operatorname{Tr}(P_qT_{A,m}^{2a})=\sum_{\alpha,j}\lambda^{2a}$. Dividing by $\lambda_0(A)^{2a}$ turns Lemma 2.1 into (17). Lemma 2.1 was checked HOLDS in `gap-es1-opus-check.md`. The sum in (18) is $\ge1/4$ (vacuum term), so the logarithm is defined. HOLDS.

**(19).** With $e(a,2a,a)=e(2a,a,a)$ by (S3):
$4\Delta_{A_1}+2\Delta_{A_2}+\Delta_{A_3}=8a\,e(a^3)-4a\,e(2a,a,a)+4a\,e(2a,a,a)-2a\,e(2a,2a,a)+2a\,e(2a,2a,a)-a\,e((2a)^3)=a\{E_0((2a)^3)-8E_0(a^3)\}=\delta$. HOLDS.
"The logarithm must stay": correct.

**(20), (21).** $\sum_{\alpha,j}v=p_z\le1$ gives $v\in[0,1]$, $D_{z,\alpha}\ge0$. $\sum_{z,\alpha,j}v=4$, so $\sum v^2=4-D_A$.
(17) reads $e^{-\Delta}(1+\epsilon')=\tfrac14(1+\epsilon_A)^2\sum v^2=(1+\epsilon_A)^2(1-D_A/4)$. Both forms of (21) follow. HOLDS.

**(22).** $Q_A=4-\sum p_z^2$; $\sum_zJ_z=\sum p_z^2-\sum v^2$. Sum: $4-\sum v^2=D_A$. $J_z=\sum_{i\neq k}v_iv_k\ge0$. HOLDS.
Theorem V (a) is exactly $\sum v^2\le\sum p_z^2$, i.e. $D_A\ge Q_A$. So "the Opus bound drops these terms" is correct. HOLDS.

**(23).** From (21) and $\epsilon'\ge0$: $1-D_A/4\ge e^{-\Delta}(1+\epsilon_A)^{-2}$. Then $1-e^{-x}\le x$ with $x=\Delta+2\log(1+\epsilon_A)\le\Delta+2\epsilon_A$. HOLDS.
Remark: $\Delta_A\ge0$ is cited but not needed; $1-e^{-x}\le x$ holds for all real $x$.

**(24).** $\sum v_i^2\le v_{\max}p_z$ gives $J_z\ge p_z(p_z-v_{\max})$. So $p_z-v_{\max}\le J_z/p_z$; then $p_z>1/2$ gives $J_z/p_z<2J_z\le2D_A$ (as $Q_A\ge0$, all $J\ge0$). HOLDS.
$v_{\max}$ exists: the block is nonzero ($p_z>0$) and the eigenvalues of a compact operator accumulate only at $0$. HOLDS.

**Multiplicity at least two.** Two eigenvectors of weight $v_{\max}$ give $2v_{\max}\le p_z$. Then $J_z\ge p_z(p_z-v_{\max})\ge p_z^2/2>1/8$. So $D_A\ge J_z>1/8$. Contrapositive: $D_A\le1/8$ forces simplicity. HOLDS.
A simple eigenvalue of an operator commuting with the sector's symmetry group spans a one-dimensional representation. HOLDS.

**$A_1$ under (ES).** $\Delta_{A_2},\Delta_{A_3}\ge0$ give $\Delta_{A_1}\le\delta/4\le2.5\cdot10^{-8}$. Then $D_{A_1}\le4(2.5\cdot10^{-8}+2\cdot10^{-7})=9\cdot10^{-7}$. HOLDS.
That exactly four sectors have $p_z>1/2$ is cited from prior work. I re-derived it here: $Q\le D\le9\cdot10^{-7}$ puts each $p_z$ within about $10^{-6}$ of $0$ or $1$; $\sum p_z=4$ over sixteen sectors then forces exactly four near $1$. HOLDS.
The claim is limited to $A_1$. This is correct: $\epsilon_{A_2},\epsilon_{A_3}$ are not bounded by (ES).
No step assumes (ES) silently: the hypothesis is stated, and the paragraph says it gives no seed. HOLDS.

## Section 4. Doubling the box

**4.1 kinematic inclusion.** On $\mathbb Z_{2a}^3$, $p_i=\pi n_i/a$. $e^{ip\cdot x}$ is invariant under $x\mapsto x+ae_i$ iff $e^{i\pi n_i}=1$ iff $n_i$ even. The pullback $f\mapsto2^{-3/2}f(x\bmod a)$ is isometric ($8$ copies, factor $1/8$). HOLDS.
(25): on mode $n$, $\mathsf Q_r$ gives $\tfrac18\sum_s(-1)^{(r+n)\cdot s}=[n\equiv r]$. Each class has $a^3$ modes. Classes by Hamming weight $3,3,1$ with smallest $|p|$ equal to $\pi/a$, $\sqrt2\pi/a$, $\sqrt3\pi/a$. HOLDS.

**No Hilbert-space identification.** The $r=0$ subspace of the $2a$-box space is half-translation-invariant functions of $24a^3$ links. It is not the $a$-box space. Repeating a configuration is a null set; restricting to a sub-box does not intertwine across seams. No $T_{2a}J=JT_a$ follows. HOLDS (as a non-implication; no claim is made that such a map cannot exist with estimates).

**4.2 which channel carries $\delta$.** Both ground states carry the label (12), by positivity. So $\delta$ is a difference of two vacuum-label energies of two different spaces. It is not identified with new nonzero-momentum energies. Through (19)–(21) it is expressed by all sixteen crossed sectors. HOLDS.
Selection rule: $A\Omega$ invariant when $A$ commutes and $\Omega$ is invariant. $V\otimes V^*\ni\sum_ie_i\otimes e_i^*$. $q+q=0$ in $\mathbb F_2^3$; $p+(-p)=0$; $(\pm)(\pm)=+$; odd $n$ plus the same odd $n$ pattern gives $r=0$. HOLDS as representation theory. The physical reading is marked ARGUED. Correct.

## Section 5. Channel positivity and conditional bounds

**(26).** $R\ge0$ self-adjoint and commuting with $\Pi_\alpha$. $\langle\psi,R^t\psi\rangle=\sum_j|\langle j,\psi\rangle|^2e^{-tE_j}\ge0$; kernel vectors contribute $0$ for $t\ge1$. Mixed blocks vanish. Gram matrix: $\sum\bar c_ic_j\langle\psi_i,R^{t_i}R^{t_j}\psi_j\rangle=\|\sum_jR^{t_j}c_j\psi_j\|^2$. HOLDS.
Remark: on the transfer space only $R\ge0$ is used; reflection positivity enters only through the construction of $R$.

**(27).** $(\sum\lambda^t)^2-\sum\lambda^{2t}=\sum_{i\neq k}\lambda_i^t\lambda_k^t\ge0$. $\sum x_\alpha^2\le(\sum x_\alpha)^2$ for $x_\alpha\ge0$. HOLDS.
Crossing remark: Lemma K needs $W(a,b)=W(b,a)$. A spatial projector involving the direction $b$ breaks this symmetry, and the crossing identity (17) is proved only for flux sums. So no per-channel Lemma K or Theorem R follows from (27). HOLDS as a statement of what the route does not give (not a no-go).

**(28).** $\sum_je^{-aE_j}=\sum_je^{-t_0E_j}e^{-(a-t_0)E_j}\le e^{-(a-t_0)m_\alpha}B_\alpha$, summed over $\alpha$. HOLDS. **(29)** the same, with energies relative to the periodic $\lambda_0(A)$ and the factor $(1+\epsilon_A)^{-1}$. HOLDS.
Both are conditional on an energy bound $m_\alpha$ and a state count $B_\alpha$. These are mass-gap-type and count inputs. They are stated as hypotheses, not assumed silently.

**(30).** $R=rI+(1-r)J/N$ has entries $r\delta_{ij}+(1-r)/N>0$, eigenvalue $1$ on constants (simple) and $r$ on the rest. $\operatorname{Tr}R^a-1=(N-1)r^a$. Unbounded in $N$ at fixed gap. HOLDS. The scope sentence (not a Wilson counterexample) is correct.

**Multiplicity.** $\epsilon\ge ge^{-aE}$, so $\epsilon\le10^{-7}$ needs $aE\ge\log(g\,10^7)$. HOLDS.

**Variational direction.** Compressed top Rayleigh quotient $\le$ the channel norm, so $-\log$ of it is an upper bound on the lowest channel energy. A lower bound needs a form bound on a dense set of the whole channel. HOLDS.

**5.3 rescaling.** $T_{B,m}\mapsto e^{-c_B}T_{B,m}$ for all $m$ at one box keeps all normalized data. $E_0\mapsto E_0+c_B$; $\delta$ changes by $a(c_{(2a)^3}-8c_{a^3})$. HOLDS.
Scope remark: crossing $Z_0(a;A')=\tfrac14\sum_zZ_z(2a;A)$ forces $c_{A'}=2c_A$ for each doubling, and then $\delta$ is unchanged. Indeed (21) writes $\Delta_A$ purely in normalized data ($D_A$, $\epsilon_A$, $\epsilon'_A$). The note says the rescaling is not a counterexample under crossing. So the statement HOLDS. It should be read as: the cross-volume comparison is supplied by crossing itself; what is missing are estimates on $D_A$, $\epsilon'_A$.

**(31).** $Z_z(a;A)=\mu_z^a(1+s_z)$ and $Z_0(a;A)=\lambda_0^a(1+\epsilon_A)$ give $p_z=e^{-ad_z}(1+s_z)/(1+\epsilon_A)$. HOLDS. Internal gaps do not fix $d_z$ or $s_z$: HOLDS as a non-implication.

**(32).** Identical to Theorem V (b) with $u_A=\eta_L$; Theorem V (b) was checked HOLDS in `gap-es1-opus-check.md` Section 1, and I re-traced it ($p^2(1-2s)\ge2p-1-2s$). HOLDS.

**OPEN paragraph.** $e^{-aE}=e^{-\ell(E/h)}$ with $a=\ell/h$. Correct. Nothing is claimed.

## Section 6. U(1) tests and the scalar obstruction

**Free model.** $\sum_{n\in\mathbb Z^3\setminus0}e^{-t2\pi|n|/a}<\infty$. With two polarizations, $\log\prod(1-x)^{-1}\le(1-x_{\max})^{-1}\sum x$, $x_{\max}=e^{-2\pi t/a}<1$. So the trace is finite. HOLDS.
RP: $\sum\bar c_ic_je^{-\omega(t_i+t_j)}=|\sum c_ie^{-\omega t_i}|^2$; a Gaussian measure with reflection-positive covariance is reflection positive (standard). Equivalently $e^{-tH}\ge0$. HOLDS.

**Two-photon state.** For transverse $\varepsilon,\varepsilon'$: $(p\times\varepsilon)\cdot(p\times\varepsilon')=|p|^2\varepsilon\cdot\varepsilon'$. So the two-creation part of $\sum_{|p|=2\pi/a,i}B_i(p)B_i(-p)$ is $-|p|^2\sum_{p,\lambda}a^\dagger_{p\lambda}a^\dagger_{-p\bar\lambda}|0\rangle\neq0$ (bosonic terms add). Total momentum $0$; centre-neutral (zero flux sector); $C=+$ ($B\mapsto-B$ twice); parity $+$ ($B$ axial, $p\leftrightarrow-p$ in the sum); $A_1$ (contracted, orbit-summed). Energy $2\cdot2\pi/a=4\pi/a$. HOLDS.
**(33).** $\epsilon\ge e^{-a\cdot4\pi/a}=e^{-4\pi}$. $4\pi<14$, $e<3$, $3^{14}=2187^2=4\,782\,969<10^7$. So $e^{-4\pi}>10^{-7}$ for every $a$ (scale invariance). HOLDS.

**Table rows.**
1. Symmetry + temporal positivity $\Rightarrow$ seed: refuted by the free model, which has both. HOLDS. Scope: the free continuum model is outside the lattice class of `gap-crux-fp.md` 3b.3 (compact group, plaquette weight). So this refutes the abstract inference by T1 logic, not a tool whose class is the 3b.3 class. The note marks the U(1) Wilson reading GUIDE, so it does not overclaim.
2. No $C=-$ removes the obstruction: the obstruction state is $C=+$. HOLDS.
3. Lowest energy alone suffices: refuted by (30). HOLDS.
4. Energy bound plus summed counts: valid conditional estimate, (28)–(29). HOLDS.
5. Internal twisted gaps bound $\delta$: missing inputs, by (31) and (18). HOLDS as a non-implication; no counterexample within the Wilson class is given, and none is claimed.
6. $p=0$, $A_1^+$ suffices: omitted channels are nonnegative and unbounded; (33) sits in the retained channel. HOLDS.
7. (24) proves a seed: circular, as it needs small $D_A$. HOLDS.

## Quiet assumptions of (ES) or a mass gap

None found. The conditional statements say so: 3.2 ("under Theorem R's smallness hypothesis"), 3.4 ("under (ES)"), 5.2 (energy bounds $m_\alpha$ and counts $B_\alpha$ as hypotheses), (32) ($u_A<1$ as hypothesis).
Positivity and simplicity of finite-volume ground states (periodic and twisted) are used. They come from the strictly positive kernels in (TM-tw) and `gap-transfer.md` Section 4. They do not depend on (ES) or a uniform gap.
The only citation to tighten is the twisted-box simplicity in 2.2: cite `gap-flux-exercise.md` 3.0 (strictly positive kernel) with `gap-transfer.md` A2–A3.

## Verdict table

| # | Statement | Verdict |
|---|---|---|
| 1 | (1) normalization $0\le R_{B,m}\le1$ | HOLDS |
| 2 | (2) covariance; group $(A_B\times\mathbb F_2^3)\rtimes K_B$ | HOLDS AFTER CORRECTION: the $C_s$ part of (2) holds on $\mathcal H_{\rm inv}$ only (reflections shift a flip plane by one site; gauge-equivalent) |
| 3 | (3) projectors, (4) little groups, $O_h$ labels, parity remark | HOLDS |
| 4 | $\mathcal C=1$ for SU(2), also with twist ($JUJ^{-1}=U^*$) | HOLDS |
| 5 | Fixed twist: only its stabilizer acts | HOLDS |
| 6 | (5), (6) extension by $H^1(B;\mathbb F_2)$ | HOLDS |
| 7 | (6a) lifts, commutator, $S_i^{L_i}$, twisted momenta, projector | HOLDS |
| 8 | (7) centre charge = winding mod 2 | HOLDS |
| 9 | (8) Schur projector identities | HOLDS |
| 10 | (9) projected loops, signs, $c=-1$ gives zero | HOLDS |
| 11 | Cubic irrep table and completeness | HOLDS |
| 12 | Plaquette sums: $A_1^+\oplus E^+$, no $T$, no odd parity | HOLDS |
| 13 | (9a) $T_2^+$, (9b) $A_1^-$ (transformation law only) | HOLDS |
| 14 | (10), invariance of $\Omega_m$ | HOLDS (cite strictly positive twisted kernel, flux-exercise 3.0) |
| 15 | Loop traces separate gauge orbits | HOLDS |
| 16 | Density of projected loop polynomials; no finite-basis claim | HOLDS |
| 17 | (11) channel traces, $d_\alpha$ factor | HOLDS |
| 18 | (12) vacuum label | HOLDS |
| 19 | (13) $\epsilon$ as channel sum | HOLDS |
| 20 | (14) definition and nonnegativity | HOLDS |
| 21 | (15), (16) $p_z$, $H_L$; orbit caution | HOLDS |
| 22 | (17), (18) | HOLDS |
| 23 | (19) $\delta=4\Delta_{A_1}+2\Delta_{A_2}+\Delta_{A_3}$ | HOLDS |
| 24 | (20), (21) | HOLDS |
| 25 | (22) $D_A=Q_A+\sum J_z$ | HOLDS |
| 26 | (23) | HOLDS ($\Delta_A\ge0$ not needed) |
| 27 | (24) | HOLDS |
| 28 | Multiplicity $\ge2$ gives $J_z\ge p_z^2/2>1/8$; simple top eigenvalue | HOLDS |
| 29 | $A_1$ under (ES): $D\le9\cdot10^{-7}$, four light sectors single-state | HOLDS (conditional on (ES), stated) |
| 30 | 4.1 kinematic inclusion, (25), Hamming table | HOLDS |
| 31 | 4.1 no Hilbert-space or spectral identification | HOLDS (non-implication) |
| 32 | 4.2 $\delta$ carried by the vacuum label; pair selection rule | HOLDS |
| 33 | (26) channel positivity and Gram matrices | HOLDS |
| 34 | (27) and the crossing remark | HOLDS |
| 35 | (28), (29) conditional thermal bounds | HOLDS (conditional on $m_\alpha$, $B_\alpha$, stated) |
| 36 | (30) counterexample | HOLDS |
| 37 | Multiplicity necessary condition; variational direction | HOLDS |
| 38 | 5.3 rescaling insufficiency | HOLDS (only without crossing; with crossing (21) fixes $\Delta_A$ from normalized data, as the note concedes) |
| 39 | (31), (32) | HOLDS |
| 40 | Free Maxwell model: finite trace, RP | HOLDS |
| 41 | Two-photon $A_1^+$ state and (33), arithmetic $3^{14}<10^7$ | HOLDS |
| 42 | Section 6 table rows 1–7 | HOLDS (row 1: free model is outside the 3b.3 lattice class; it refutes the abstract inference only) |
| 43 | Quiet use of (ES) or a mass gap | NONE FOUND |

RESULT: all 42 checked statements HOLD (one, (2) for the centre flips, after the correction "on $\mathcal H_{\rm inv}$ only"); no statement fails, no step silently assumes (ES) or a mass gap, and the note proves no seed, as it says.
