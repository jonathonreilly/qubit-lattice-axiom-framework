# Check of gap-vortex-astra.md, Sections 2 to 8

- Checker: Claude Opus 5.5 (one session, no subagents). Date: 2026-11-12. Cross-provider check.
- Author checked: Codex gpt-6-astra max, FINISH row 778, source pin `8adccdfdd331`.
- File checked (read-only, read in full, 650 lines):
  `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-vortex-astra.md`.
- Inputs read (same folder): `gap-fusion-astra.md` Sections 1 to 6 (lines 41-573);
  `gap-fusion-check-opus.md` in full; `gap-means-max.md` 4.1-4.7 (Lemmas R1, R2, R3, Theorem R,
  Corollaries); `gap-flux-exercise.md` 3.0-3.1 ((TM-tw), (F1), (S1)-(S3)); `gap-channel-astra.md`
  1.1-1.2 and 3.1-3.4; `gap-skeleton-final.md` 13.16-13.20; `gap-transfer.md` Notation, 8, 9.
- Not read: Kanazawa arXiv:0808.3442 and Seiler arXiv:0901.4246 (the literature boundary in
  Section 3 is not checked against the primary text); `gap-means-max.md` 4.8-6.
- Method: by hand. One pure-Python guide run (`python3 -I`, Monte Carlo, 4x10^5 samples) compared
  the commutator law with (6) and (7) and computed the Q_8 commutator law. It decided nothing.
  Script: `scratchpad/vx-opus/guide/comm.py` (same scratchpad folder as this report).
- Numbering: the note's own (14) is the gauge-averaging identity of 7.1. The target, fusion (14),
  is called (V) in the note. I keep the note's numbering.

## Section 2: parity probabilities (1) and the comparison (2)

**(1).** In frame $r$ with spatial twist $m$, $T=T_{r,m}$ is positive, trace class and commutes
with the flips $C_i$ ((TM-tw)). So $\omega(X)=\operatorname{Tr}(T^{n_r}X)/\operatorname{Tr}(T^{n_r})$
is a state, and on the commutative algebra of the $C_i$ it is a probability measure on signs.
$\operatorname{Tr}(T^{n_r}C_i)=Z^{m+v_{ri}}$ by (TM-tw), so
$q=\omega((1-C_i)/2)=\tfrac12(1-Z^{m+v_{ri}}/Z^m)$. $q\ge0$ by positivity; $q<1/2$ since
$Z^{m+v_{ri}}>0$ (positive integrand). HOLDS.

**$2Q\le D$.** $Z^{m+v}\ge e^{-D}Z^0\ge e^{-D}Z^m$, using (S2) $Z^m\le Z^0$. So
$2q\le1-e^{-D}\le D$. HOLDS. Also $D=\max_k[-\log r(k)]$ equals the fusion quantity
$\max_k|\log(Z^k/Z^0)|$, because $Z^k\le Z^0$ by (S2) (`gap-flux-exercise.md` C2). HOLDS.

**(3).** Let $\epsilon_i$ be the joint signs of the commuting flips under $\omega$.
$Z^{m+e}/Z^m=\omega(C^e)=1-2P(\prod_{i\in e}\epsilon_i=-1)\ge1-2\sum_{i\in e}P(\epsilon_i=-1)
\ge1-2sQ$. HOLDS.

**Chain.** Frame 1: $k=e_1+m_1$, $e_1\subset\{12,13,14\}$ (at most 3 bits),
$m_1\subset\{23,24,34\}$. Frame 2: $m_1=e_2+m_2$, $e_2\subset\{23,24\}$ (at most 2 bits),
$m_2\subset\{34\}$. Frame 3: plane 34 is temporal (1 bit). So
$r(k)=\frac{Z^k}{Z^{m_1}}\frac{Z^{m_1}}{Z^{m_2}}\frac{Z^{m_2}}{Z^0}\ge(1-6Q)(1-4Q)(1-2Q)$.
For $6Q\le1$ all factors are in $[0,1]$ and $(1-x)(1-y)\ge1-x-y$ gives $\ge1-12Q$. For
$12Q\le1/2$: $-\log(1-x)=\int_0^x(1-t)^{-1}dt\le2x$, so $-\log r(k)\le24Q$. So $D\le24Q$ when
$Q\le1/24$. HOLDS. (The intermediate line "$\ge1-12Q$" needs $Q\le1/6$; it is used only under
$Q\le1/24$.) The equivalence of an area bound on $Q$ with (V), up to constants, HOLDS.

**(4).** $P_\chi=\prod_j\frac{1+(-1)^{\chi_j}C_j}{2}\le\frac{1-C_i}{2}$ for any $i$ with
$\chi_i=1$. In the crossed set $\chi_2=0$, so $\chi\ne0$ has $i\in\{3,4\}$. Then
$Z_{\chi,m}\le q_{1,i}(m)Z^m\le Q_FZ^0$ (with $m_2=0$, the crossed condition), and
$Z_{0,0}=\frac18\sum_eZ^e\ge Z^0/8$. So $p_{\chi,m}\le8Q_F$. HOLDS.

**Light group under $Q_F<1/192$.** Twelve heavy weights sum to $\le96Q_F<1/2$. The four magnetic
weights sum to $4-(\text{heavy})>4-96Q_F$ and each is $\le1$ (Lemma R1(b), Lemma R2(a); these
are unconditional, not (ES)). So each is $>1-96Q_F>1/2$, and each heavy one is
$\le8Q_F<1/24$. So $\{p>1/2\}=L_{\rm mag}$. HOLDS.

**(FQ) and the witness version.** $8Q_F\le K\sqrt S$ is literally (F-h) for the twelve heavy
sectors. With $S\ge\eta(\beta)^a\ge\eta_*^a$ (fusion (2), $a\ge3$),
$Q_F\le C_2a^{p_2}\eta_*^{a/2}$ gives $8Q_F\le8C_2a^{p_2}\sqrt S$, and $Q_F<1/192$ for large $a$
since $\eta_*<1/16$. HOLDS. "An area exponent is unnecessary" HOLDS: a decay faster than
$\eta_*^{a/2}$ times a polynomial suffices.

No step of Section 2 assumes (V), (ES) or a gap.

## Section 3: what the light group and the single-state result permit

**Theorem R and (23)-(24) supply no small parameter.** Theorem R and `gap-channel-astra.md` 3.4
take (ES) as hypothesis; (24) is a consequence of $D_A<1/8$, which (23) derives from small
$\Delta_A,\epsilon_A$. The note states this correctly. HOLDS.

**$L_\kappa$ cannot be the light group.** In the coordinates of `gap-means-max.md` 4.2, the
$\alpha_\kappa=(1,1)$ group is $\{x_1=x_3,\ x_2=x_4\}$, i.e. $\chi=m$ on directions 3, 4. For
$m\ne0$, (S1) gives $Z_{m,m}\le Z_{0,m}$, so $p_{0,m}\ge p_{m,m}$. If $\{p>1/2\}=L_\kappa$, then
$p_{m,m}>1/2$ forces $(0,m)\in\{p>1/2\}$, but $(0,m)\notin L_\kappa$. Contradiction. This needs no
(ES). The equivalent form also holds: in the kappa branch of Theorem R, (a) gives
$S_{\rm full}(a;a^3)\le1.28\times10^{-5}$ and (b) gives $S_\kappa(a;a^3)>2$, contrary to
$S_\kappa\le S_{\rm full}$ (C7, from (S1)). So under (ES) the branch is electric or magnetic.
HOLDS. (Credit Codex gpt-6-astra; I did not find this consequence stated in the files read.)

**Electric vs magnetic not distinguished by single-state dominance.** For $m=0$ the centre
labels are real signs and $p=0$ with a one-dimensional little-group irrep is allowed. For
$\chi=q=0$ the shifts in channel (6a) are $\frac12[\sum_j\mathfrak m_{ij}q_j]_2=0$. So the labels
that (24) constrains are compatible with both candidates. HOLDS, as a statement about
information content; it is a failed route, not a theorem that both candidates occur.

**Literature boundary (ARGUED).** The form $|\langle W(C)\rangle|\le2q^{A_C/(L_\mu L_\nu)}$ with
$q=(1-Z^-/Z)/2$ agrees with my recollection of Tomboulis-Yaffe. I did not read Kanazawa or
Seiler. NOT CHECKED against the primary text. The note uses it only to place the target.

## Section 4: the commutator contraction

**(6).** $\rho([A,B])=\rho(A)\rho(B)\rho(A)^*\rho(B)^*$. Schur: $\int\rho(A)X\rho(A)^*dA=
(\operatorname{tr}X/d)I$; with $X=\rho(B)$ this is $\frac{\chi_\rho(B)}{d}\rho(B)^*$. Then
$\big(\int\chi_\rho(B)\rho(B)^*dB\big)_{ij}=\sum_k\int\rho_{kk}\overline{\rho_{ji}}=\delta_{ij}/d$.
So $\int\rho([A,B])=I/d^2$. HOLDS. Guide: $E[\tfrac12\operatorname{tr}[A,B]]=0.2494$
(predicted $1/4$); $E[\chi_3]=0.330$ ($1/3$); $E[\chi_4]=0.243$ ($1/4$).

**(5).** On a matrix coefficient $f=\langle u,\rho(\cdot)v\rangle$, $Kf=d^{-2}f$. The centre acts
by $(-1)^{d-1}$ on $\operatorname{Sym}^{d-1}$. Odd means $d$ even; the largest eigenvalue is
$1/4$ at $d=2$. $\mu$ is symmetric ($[A,B]^{-1}=[B,A]$), so $K$ is self-adjoint and its norm on
the odd subspace is $\sup_{d\ \rm even}d^{-2}=1/4$. The Peter-Weyl sketch (irreducibility via
weights, Clebsch-Gordan, Stone-Weierstrass on entries and conjugates) is standard and correct.
HOLDS.

**(7).** $\tfrac12\operatorname{tr}[A,B]=\langle ABA^{-1},B\rangle_{\mathbb R^4}=\cos^2\phi+u\sin^2\phi$,
$u$ uniform on $[-1,1]$. Conditional density $1/(2\sin^2\phi)$ on $[\cos2\phi,1]$; times
$(2/\pi)\sin^2\phi$ and integrated over $\{\phi:\cos2\phi\le\cos\theta\}=[\theta/2,\pi-\theta/2]$
gives $(\pi-\theta)/\pi$. Haar density of $x=\cos\theta$ is $(2/\pi)\sin\theta$. Ratio
$w=(\pi-\theta)/(2\sin\theta)$; the law is conjugation invariant, so $w$ is its Haar density.
Normalization: $\frac1\pi\int_0^\pi(\pi-\theta)\sin\theta\,d\theta=1$. $w\ge1/2$ iff
$\sin\theta=\sin(\pi-\theta)\le\pi-\theta$. HOLDS. Guide: ten bins of $x$ agree with
$(\pi-\arccos x)/\pi$ to within $0.0013$.

**Bounded-function contraction.** $\mu-\tfrac12dg\ge0$ with mass $1/2$, so
$\mu=\tfrac12dg+\tfrac12\mu'$. Odd bounded $f$ has Haar mean $0$, so
$\|Kf\|_\infty\le\tfrac12\|f\|_\infty$. HOLDS.

**(8).** A link of a 4D torus with sides $\ge3$ lies in exactly 6 plaquettes. The two links
together meet at most 12 (11 if they share a plaquette). Each term
$\beta\eta_p\tfrac12\operatorname{tr}U_p$ has oscillation $2\beta$. So the oscillation is
$\le24\beta$ and the normalized conditional density lies in $[e^{-24\beta},e^{24\beta}]$.
HOLDS. Loop holonomies $A,B$, each using its own selected link once and not the other, are
Haar-preserving changes of variables at fixed $\xi$ (left and right multiplication by
$\xi$-measurable elements, possibly inversion). So the same bounds hold for $(A,B)$, and the
law is $\delta\,dA\,dB+(1-\delta)\nu_\xi$. HOLDS.

**(9).** $K_\xi=\delta K+(1-\delta)K_{\nu'}$ with $\nu'$ the commutator image of $\nu_\xi$.
Right convolution by a probability measure is an $L^2$ contraction and commutes with $J$
($-1$ is central). On $J=-1$: $\|K_\xi\|\le\delta/4+1-\delta=1-\tfrac34\delta$. Sup-norm
version: law $\ge(\delta/2)dg$ gives $1-\delta/2$. Monotone in $\beta$, so $\beta_+$ is the worst
case on $I$. HOLDS. Uniform in $\xi$, volume and twist: HOLDS (the twist only changes signs
$\eta_p$, not oscillations or incidences).

**U(1) failure.** In U(1) every commutator is $1$, so $K_\xi=I$, including on
$f(-g)=-f(g)$ (e.g. $f(e^{i\theta})=e^{i\theta}$). (5) and every strict (9) fail. HOLDS.
*Remark (ARGUED, not a correction).* "The distinction is noncommutativity" is right for U(1),
but noncommutativity alone does not track confinement. For the quaternion group $Q_8$, with
centre $\{\pm1\}$, the commutator law is $\tfrac58\delta_1+\tfrac38\delta_{-1}$ (guide count:
$P([A,B]=-1)=0.375$), so $K$ acts on odd functions as exactly $1/4$, the same as (5) (its odd
irrep has $d=2$). (6), (8), (9) and the area bound (10) hold verbatim for 4D $Q_8$ Wilson
theory. (7) and (12) need restating, since the commutator law sits on the centre, but the sign
comparison of (13) has the same form. At large $\beta$, $Q_8$ theory is ordered, and a Pf$=1$
twist ($k=12+34$) cannot be carried by a flat $Q_8$ connection (two non-commuting holonomies
generate $Q_8$, so the remaining two would be central and commute). So its twist free energy is
expected to grow like $\beta a^2$ and (V) to fail. This is a standard low-temperature
expectation; I did not prove it here. If it holds, the contraction plus conditional
independence, which $Q_8$ shares, cannot by themselves yield (V); all the content must sit in
(CF). This agrees with the note's Section 7 and strengthens it.

## Section 5: the loop word $W_a$ and the area bound (10)-(11)

**Geometry.** Base coordinates $4j$, $0\le j<\lfloor a/4\rfloor$, so the largest is
$\le a-4$. For $j\ne j'$ the periodic distance is $\min(4|j-j'|,a-4|j-j'|)\ge4$. A plaquette's
links have base points within distance $1$ in each axis, so no plaquette holds selected links
of two bases. HOLDS. Given all unselected links $\xi$, the conditional density factorizes over
pairs. HOLDS.

**Holonomies.** $A_x$, the 13-plaquette at $x$ through $(x,x+e_1)$, uses no direction-2 link;
$B_x$, the 24-plaquette through $(x,x+e_2)$, uses no direction-1 link. Neither meets another
base's selected link. The transports run in the layer $x_3=1$ (direction-1,2 links there are
unselected) with one direction-3 link down to each base; all are $\xi$-measurable. So each
factor $P_x[A_x,B_x]P_x^{-1}$ depends only on pair $x$ and $\xi$. HOLDS. $W_a$ is a based loop at
the root, so its half-trace is gauge invariant, real, and $|W_a|\le1$. HOLDS.

**Bound.** $\|E(P_x[A_x,B_x]P_x^{-1}\mid\xi)\|_{\rm op}\le\delta/4+(1-\delta)=\rho_\beta$ by (6)
with $d=2$ and (8). For conditionally independent matrices, $E\prod X_x=\prod EX_x$ in the fixed
order (multilinearity). Submultiplicativity gives $\rho_\beta^N$, and
$|\tfrac12\operatorname{tr}M|\le\|M\|_{\rm op}$. Integrating $\xi$ against any twisted measure
keeps the bound. $\rho_\beta\le\rho_{\beta_+}$. For $a\ge8$,
$\lfloor a/4\rfloor\ge a/4-3/4\ge a/8$ (true for $a\ge6$), so $N\ge a^2/64$. Every constant in
(10) HOLDS.

**Scope.** Zero net traversal: HOLDS. $W_a\equiv1$ in U(1): HOLDS. Centre invariance: HOLDS,
and in fact for *every* centre change on links, closed or not: each based loop changes by a
central sign and each sign cancels in its commutator; the transport signs cancel in
$P_x\cdots P_x^{-1}$. *Correction (precision, harmless):* "every closed centre change" can be
"every centre change". *Remark:* the exponent $a^2$ counts independent factors, not a minimal
surface. Placing pairs in a 4D sublattice would give decay in $a^4$. (10) holds at every $\beta$,
every twist and in any phase, including ordered ones (see the $Q_8$ remark). So it is not a
confinement estimate, as the note says.

No step of Section 5 assumes (V), (ES) or a gap.

## Section 6: the endpoint comparison (12)-(13) and (CF)

**Measure bounds.** Pushing forward the two-sided density of $(A,B)$ by the commutator map
gives $\delta\mu\le\nu'\le\delta^{-1}\mu$; conjugation by the fixed transport preserves $\mu$.
HOLDS.

**$\mu*\mu$.** Its Fourier coefficients are $d^{-4}I$. The class function $\sum c_d\chi_d$ has
coefficient $c_d/d$ (characters are real, $\int\chi_d\rho_d=I/d$), so $c_d=d^{-3}$. Since
$|\chi_d|\le d$, the series converges uniformly and is bounded by $\sum d^{-2}=\pi^2/6\le2$.
Lower bound: $\mu\ge\tfrac12dg$ gives $\mu*\mu\ge\tfrac12dg$. HOLDS. So
$\delta^2/2\le w_2\le2\delta^{-2}$. HOLDS.

**Contraction of the odd part.** Right convolution by a probability measure keeps a lower bound
$c$ on a density. $\nu_j\ge\delta\mu\ge(\delta/2)dg$, so for odd bounded $h$,
$\|h*\nu_j\|_\infty\le(1-\delta/2)\|h\|_\infty$. The odd part
$o_N(g)=w_N(g)-w_N(-g)=o_2*\nu_3*\cdots*\nu_N$. $\|o_2\|_\infty\le2\delta^{-2}-\delta^2/2$; the
note's $4\delta^{-2}$ is a valid, loose bound. So $|o_N|\le4\delta^{-2}s^{N-2}$ and, dividing by
$w_N\ge\delta^2/2$, $|w_N(-g)/w_N(g)-1|\le8\delta^{-4}s^{N-2}$ a.e. (12) HOLDS (the constant 8
could be 4).

**(13).** $\int F(-g)w_N(g)\,dg=\int F(g)w_N(-g)\,dg$ by Haar invariance under $g\mapsto-g$; then
apply (12) pointwise. Uniform in $F\ge0$ and $\xi$. A common nonnegative exterior weight
preserves a ratio bound that holds slice by slice. $|\log(1+x)|\le2|x|$ for $|x|\le1/2$.
HOLDS.

**(CF) implies (V).** If (CF) holds for every frame $r$, spatial $i$ and spatial twist $m$, then
$|Z^{m+v_{ri}}/Z^m-1|\le\varepsilon_N$, so $q_{r,i}(m)\le\varepsilon_N/2$ and
$Q\le\varepsilon_N/2$. Once $\varepsilon_N\le1/12$, (2) gives $D\le12\varepsilon_N$. With
$N\ge ca^2$, $\varepsilon_N\le8\delta^{-4}e^{\delta}\exp(-c\delta a^2/2)$ (using
$s^{N-2}\le e^{-(\delta/2)(N-2)}$). That is (V) with $p=0$ and $\sigma=c\delta/2$, uniform on $I$
through $\beta_+$. HOLDS as a conditional implication.

**Is (CF) stated correctly?** Yes, as a sufficient condition. Two points of precision: (i) it
must hold for *all* pairs $(m,m+v_{ri})$ in all four frames, as the note's "for each pair"
says; (ii) the weight $w_{\xi,N}$ need only satisfy (12) with $N\ge ca^2$, not be a commutator
law. There is a structural reason why the commutator law cannot itself carry the sign. Every
centre change on links fixes each commutator, so no link-sign change of variables maps
$F_\xi(g)$ to $F_\xi(-g)$ on the commutator product. A proof of (CF) would need another
mechanism. The note says this in 7.3. HOLDS.

No step of Section 6 assumes (V), (ES) or a gap. (CF) is labelled OPEN and is not used as a fact.

## Section 7: the three failures

**7.1, the note's (14).** On the gauge-invariant space $\Gamma_x(h)\psi=\psi$ for every $h$, so any
average of $\Gamma_x([A,B])$ fixes $\psi$. Electric-flux sectors are subspaces of the
gauge-invariant space, distinguished by the winding flips $C_i$, which are not site gauge
transformations. A spatial Polyakov trace in direction $i$ meets the flip slice once, so it is
odd under $C_i$ and gauge invariant. HOLDS. The conclusion is an obstruction to this
implementation only, as stated.

**7.2, tensor example.** $f=\operatorname{tr}g_1$ is $J_{\rm all}$-odd with
$K^{\otimes N}f=\tfrac14f$. A product of matrix coefficients with dimensions $d_j$ has
eigenvalue $\prod d_j^{-2}$ and is $J_{\rm all}$-odd iff an odd number of $d_j$ are even. So
the odd-subspace norm is $1/4$ for every $N$. HOLDS. The Polyakov trace in direction 3 uses no
selected link (selected links are in directions 1, 2), so it is $\xi$-measurable, untouched by
the pair integrations, and odd under $C_3$. HOLDS. This is the relevant charge for $Q_F$
($i\in\{3,4\}$), so the observation is on point.

**7.3, (15).** Fubini with the factorization of Section 5: plaquettes meeting no selected link
give $C_k(\xi)$, those meeting pair $x$ give $f_{k,x}$, and the Haar changes of variables have
Jacobian one. So $Z^k=\int d\xi\,C_k\prod_xz_{k,x}$. HOLDS. The reading is right: Sections 4-6
bound the normalized laws $f_{k,x}/z_{k,x}$ for each $k$ separately and say nothing about
$C_k\prod z_{k,x}$ versus $C_0\prod z_{0,x}$. The centre-change remark HOLDS, and is
strengthened by the Section 6 point: $W_a$ and each commutator are invariant under every
link-sign change, so no such change of variables can relate a twist to the sign of the word.
"Not an obstruction theorem against other factorizations, or a counterexample to (V)": correct
scope.

## Section 8: the missing statement and the U(1) claim

**(16).** The left side is $\max_{m_2=0,i=3,4}q_{1,i}(m)$ on $(a,a,c,d)$ with time $a$, which is
$Q_F$. So (16) is $8Q_F\le K\sqrt S$, i.e. (FQ), together with $Q_F<1/192$. Stated correctly.
HOLDS. The alternative, the area bound on $Q$ for all frames and backgrounds, is equivalent to
(V) by (2). HOLDS.

**(CF).** Stated correctly as a sufficient, not necessary, representation. HOLDS (see Section 6).

**U(1) failure of the mechanism.** Right: commutators are trivial, the contraction is the
identity, and $W_a\equiv1$. HOLDS. *Remark (ARGUED):* the mechanism passes the U(1) test, but
by the $Q_8$ remark of Section 4 it is shared by a non-abelian model whose ordered phase is
expected to violate (V). So passing the U(1) test is not evidence that the contraction tracks
confinement. The note does not claim it does.

**Table rows.** The labels PROVED for (2), (4)/(FQ), (5)-(9), (10)-(13), (14)/tensor/(15) match
what I re-derived. OPEN for (CF), (FQ) at order one and (V) is correct. The RESULT line is
accurate.

**Hidden assumptions.** None found. No step uses (V), fusion (14), (ES), Theorem R's hypothesis
or a mass gap as an input. Section 3 cites the (ES)-conditional results only to say what they
do not give.

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1 | $D$ equals the fusion (14) quantity; $Z^k\le Z^0$ (93-96) | HOLDS | (S2) by the three-frame chain |
| 2a | (1): $q\in[0,1/2)$, formula (122-136) | HOLDS | Trace state on commuting flips |
| 2b | (2) lower: $2Q\le D$ (143-146) | HOLDS | |
| 2c | (3): $Z^{m+e}/Z^m\ge1-2sQ$ (148-155) | HOLDS | Union bound on joint signs |
| 2d | (2) upper: $D\le24Q$ for $Q\le1/24$ (157-168) | HOLDS | Bits 3, 2, 1; needs $Q\le1/6$ at the middle line, used only under $Q\le1/24$ |
| 2e | (4): $p_{\chi,m}\le8Q_F$ (179-190) | HOLDS | $P_\chi\le(1-C_i)/2$, $Z_{0,0}\ge Z^0/8$ |
| 2f | $Q_F<1/192$ identifies $L_{\rm mag}$ without (ES) (192-196) | HOLDS | $1-96Q_F>1/2$, $8Q_F<1/24$ |
| 2g | (FQ) gives (F-h); witness form (198-210) | HOLDS | |
| 3a | Theorem R, (23)-(24) give no small parameter (214-218) | HOLDS | |
| 3b | $L_\kappa$ cannot be the light group (220-228) | HOLDS | (S1); also $S_\kappa\le S_{\rm full}$ vs Theorem R(b); no (ES) needed for the direct form |
| 3c | Single-state result does not separate electric and magnetic (230-239) | HOLDS | Information statement; (6a) shifts vanish at $q=0$ |
| 3d | Tomboulis-Yaffe/Kanazawa form (241-254) | NOT CHECKED | Primary texts not read; consistent with my recollection |
| 4a | (6): $\int\rho([A,B])=I/d^2$ (272-283) | HOLDS | Guide agrees |
| 4b | (5): norm $1/4$ on $J=-1$ (266-309) | HOLDS | $K$ self-adjoint, eigenvalues $d^{-2}$ |
| 4c | (7): $w=(\pi-\theta)/(2\sin\theta)\ge1/2$ (311-337) | HOLDS | Normalization and guide agree |
| 4d | (8): $\delta_\beta=e^{-24\beta}$ (339-354) | HOLDS | 12 plaquettes, oscillation $2\beta$ each |
| 4e | (9): $\rho_\beta=1-\tfrac34e^{-24\beta}$; sup version $1-\tfrac12e^{-24\beta}$ (355-369) | HOLDS | |
| 4f | U(1) failure of (5), (9) (371-376) | HOLDS | Remark: $Q_8$ shares (5), (6), (8)-(10); argued to violate (V) at large $\beta$ |
| 5a | Base geometry, conditional independence (394-401) | HOLDS | Separation $\ge4$ |
| 5b | $W_a$ construction (11), gauge invariance (403-416) | HOLDS | |
| 5c | (10): $\rho_{\beta_+}^{\lfloor a/4\rfloor^2}\le e^{-(-\log\rho)a^2/64}$, $a\ge8$ (380-432) | HOLDS | Every constant re-derived |
| 5d | Scope test (434-441) | HOLDS AFTER CORRECTION (precision) | Invariant under every centre change on links, not only closed ones; $a^2$ counts factors, not area |
| 6a | (12): $w_N\ge\delta^2/2$, $\varepsilon_N=8\delta^{-4}s^{N-2}$ (449-493) | HOLDS | $\mu*\mu=\sum d^{-3}\chi_d$; $4\delta^{-2}$ valid but loose ($2\delta^{-2}$ suffices) |
| 6b | (13) and the common-weight statement (495-509) | HOLDS | |
| 6c | (CF) implies (V), $Q\le\varepsilon_N/2$, $D\le12\varepsilon_N$ (511-531) | HOLDS | Conditional; $\sigma=c\delta/2$, $p=0$ |
| 7a | Note's (14): gauge averaging fixes flux states (537-552) | HOLDS | |
| 7b | Tensor example, norm $1/4$ for all $N$; direction-3 Polyakov trace (556-574) | HOLDS | |
| 7c | (15) and the normalizer gap (578-610) | HOLDS | |
| 8a | (16) equals (FQ) with $Q_F<1/192$ (624-641) | HOLDS | |
| 8b | (CF) stated correctly as sufficient (511-531, 621) | HOLDS | Must hold for all pairs in all frames |
| 8c | U(1) failure of the mechanism (618) | HOLDS | Passing the U(1) test does not show the mechanism tracks confinement ($Q_8$ remark, argued) |
| 8d | No hidden use of (V), (ES) or a gap | HOLDS | |

Checked line by line by Claude Opus 5.5. Nothing FAILS. One precision correction (5d). Two
loose but valid constants (6a). Credit Codex gpt-6-astra for the parity reduction (2), the
weaker test (FQ), the exclusion of $L_\kappa$, the finite-beta commutator contraction, the
word $W_a$ with its area bound, the endpoint comparison (12)-(13), and the three obstructions.

RESULT: Sections 2-8 of gap-vortex-astra.md HOLD (Claude Opus 5.5, line by line, cross-provider): (1)-(4), (FQ), the L_kappa exclusion, (5)-(13) and the obstructions (14), tensor, (15) are correct with every constant re-derived; one precision correction (W_a is invariant under every centre change, not only closed ones) and one loose constant in (12); the literature form in Section 3 is not checked; no step assumes (V), (ES) or a gap; (CF), order-one (FQ) and (V) stay OPEN, and an argued Q_8 test suggests the contraction alone cannot give (V), so all content must sit in (CF).
