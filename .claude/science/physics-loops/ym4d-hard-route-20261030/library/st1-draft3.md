# ST1, round 3 (long draft): the four repairs M, R, B, F

Provenance: Claude (Opus 5.5), 2026-11-04, pass-1 long draft for round 3, written against `st1-r2.md` (Codex distillation of round 2, 956 lines). Research text, not an audit; it grants no status. Not yet distilled or refereed. Written proofs only; no computer-assisted step. Every argument below is a finite chain of inequalities, contractions, convergent series and set inclusions, so it is Lean-formalizable in the ordinary sense.

Credit. The four-dimensional outline (SA), its complete account I (CA-I) and the three-dimensional manuscript (Y3) are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at commit `31a47c543775`. The averaging, axial and Landau gauges, determining sequences, stage operations, box minimiser and their tests originate with Tadeusz Bałaban. Jonathan Dimock's expositions of Bałaban's renormalization group are the standard secondary account of the same constructions. Source line numbers refer to `ym4.tex` (SA), `ca_I.tex` (CA-I) and `YM3_I.tex` (Y3) in the scratchpad copy of that commit; every source claim below quotes or paraphrases the cited lines, and a source label is never used as a proof.

**How to read this file.** It is a set of additions keyed to `st1-r2.md`. Numbers such as (17), Lemma 9, Theorem 14 refer to `st1-r2.md`. New items carry a prime (Lemma 1′, Lemma 9′) when they replace an st1-r2 item, and a letter (Definition M1, Lemma B2, Theorem F4) when they are new. All definitions and corrections of `st1-r2.md` remain binding; where an addition changes a definition, the change is stated and its consumer effect is stated. Status tags: **[proved]** means proved here from st1-r2's declared inputs and the inputs named in §0.2; **[input]** means a hypothesis, with its source lines; **[Outstanding]** means not proved here.

## 0. Summary and new inputs

### 0.1 Result table

| Repair | What st1-r2 left open | What is done here | Status | Enters st1-r2 at |
|---|---|---|---|---|
| **M** deleted marks | SA 6113–6114 and 17433 let a swallowed mark disappear, so (17) can *increase* at a reset and (13) fails at old indices | Definition M1 (permanent mark ledger). Lemma M2: ledger levels are distinct at each point (from SA's "marks wait" and the monotone waiting depth). Lemma 1′: the range $[c_{\min},1+\beta_s]$ and the drops (18) hold at **every** actual transition, resets included. Lemma M3: the ledger domain is contained in the standing-mark domain. | **proved** (given GEO-mark, which is SA's own geometric statement) | Lemma 1, (13), Lemma 11, Theorem 14 hyp. 2 |
| **R** minimum-lift cores | (62) and core formation with $\inf_X(c\lambda)$ | Proposition R0: (62) is **false**, and core formation with the scalar infimum over $X$ does **not** follow from the tests (58) (explicit counterexample). Definition R1: lifted core (one scalar radius per element, over that element's read set, as §1's rule requires). Lemma 9′ (CORE), Lemma 10′ (formation), Lemma 11′ (half-gap and drift) for lifted cores. | **proved** (counterexample + repair) | §1 core records, (11)–(12), Lemmas 9, 10, 11, Theorem 14 hyp. 2 |
| **B** output and consumers | BOX admission; witness/chain consumers | Lemma B1: output tests (58) and output formation from BOX's $C(M)$ bound, through a lower-growth bound on the lift (RUN-low) and $\gamma$ after $M$. Lemma B2: BOX version of (71), $a_X<1/2$. Lemma B3: output drift relation. Lemma B4: every consumer **inside ST1** of the enlarged witness radii and of the chain reads is verified. | **proved** inside ST1. The external consumer statement **CI** (activities of NL1/LF1 bounded on the ST1 domains) is **Outstanding**, after three attacks (§4.3). | Lemma 10, Lemma 11 (BOX relation), Lemma 13, Theorem 14 hyps. 2–4 |
| **F** collar-variable map | (70) for the actual stage map on its complex contour | Lemma F1 (strip bond map), Lemma F2 (regional fibre chart), Proposition F3 (measure identity: the stage integral **is** an integral over these coordinates), Theorem F4 (the actual map, retained-row/fibre/boundary identities, (70) on the full tube), Lemma F5 (the conditional-mean contour stays in the tube), Lemma F6 (localization discrepancy $h_j\le\delta'_j/8$). | **proved** (given ST-test, which specifies our stage test, and LOC-form or LOC-decay) | Lemma 12, (70), Lemma 13, Theorem 14 hyps. 3, 5 |

**First remaining Outstanding statement.** CI (§4.3): every carried activity supplied by NL1/LF1 is bounded on the ST1 chain domain built from Definitions M1 and R1 and the smoothed lifts $\lambda_\tau$, with its constants fixed before $\kappa$. It is an interface statement on NL1/LF1, not an ST1 lemma; ST1 cannot prove it because it is a property of activities ST1 does not construct. The three attacks that try to reduce it to the printed SA/CA-I domains, and why each fails, are in §4.3.

### 0.2 New inputs (each a hypothesis; source lines quoted)

These are added to st1-r2 §2. None is proved by a source label.

* **GEO-mark** (part of GEO). (i) SA 17440: "*Marks wait*: a mark of level $s$ lying inside a class component of level $t$ satisfies $s<t_\flat$. Hence standing marks that share a part are nested, their windows $(s_\flat,s]$ are disjoint". (ii) SA 17433: "A mark persists until a later healed component or island swallows it", read as: a mark is removed only at the output of an operation whose healed component or island **contains** it (SA 6113–6114: "old marks disappear when swallowed by a healed component or an island"). (iii) SA 6139–6140: $\operatorname{Re}_\sigma(x)$ "consists exactly of the levels of the first $\nu(C)$ stages of each drop-out containing $x$"; islands contribute no levels. (iv) Along every compared transition, each standing mark's $\nu$ does not decrease (this is st1-r2 Lemma 1's hypothesis "unchanged marks at main and output transitions and only added marks at a stage"). (v) Each point lies in at most one class component of a given operation. SA 6115 says these facts "require verification for the actual operation"; they are therefore GEO hypotheses, exactly as st1-r2 §2 requires ("Mark resets and lift formation must be specified, rather than inferred from a partial order").
* **RUN-low** (part of RUN). There are $c_N>0$ and $r>1$, fixed in row 1, with $R_i\ge c_N(\log\theta_i)^r$ for every level $i$, where $R_i$ is the cube-size factor of Lemma 2 and Lemma 10 ($L^{N^0_t-1}=R_{k_\sharp+1}$). Source: SA 17630, "Since $\mathsf N_k=\check R_k\approx(\log x_k)^r$ … so $\mathsf N_k$ is taken large"; SA 17387, "On cubes whose side is proportional to $\check R_k\approx(\log x_k)^r$, this quantity is smaller than every power of $g_k$, because $r>1$". The upper half $R_i\le C_N(\log\theta_i)^r$ is already in RUN.
* **GEO-box** (part of GEO). In an operation of level $t$, every corner of a level-$t$ datum loop that lies within level-$t$ distance $1$ of the box $\Lambda^{\rm pr}$ lies in $\Omega^c_{k_0+1}$ of the operation's input label, $k_0=k_\sharp=t-N^0_t$. Source: CA-I 53788, "$\Lambda:=(\Omega^{\sim4}_{k_0+1})^c\cap Z$", and CA-I 53802 and 53887–53888, "$\Lambda\subset\Omega^c_{k_0+1}\cap Z$". The extension from $\Lambda$ to its distance-$1$ neighbourhood uses the enlargement-width convention already assumed after st1-r2 Lemma 2 (each $\sim$-layer has $\ell^\infty$ width at least one level-$t$ unit).
* **BOX** (refines st1-r2's BOX). Source: SA 17656 (Proposition 2.4): "There exist a radius $a_\Lambda>0$ and a constant $C(M)$, both chosen after $M$ and before $\gamma$ … Suppose the exterior data satisfy $|\partial V_k-\mathbf 1|<\varepsilon$ … In the application $\varepsilon\le C\varepsilon_k$ … it satisfies $|\partial V_\Lambda-\mathbf 1|\le C(M)\varepsilon$ … Moreover, $U_0:=U_{k,X}(V_\Lambda)$ satisfies $J(U_0)=0$ in $\Lambda^{\rm pr}$"; SA 17594–17598: "$V''=e^{ig_kB}V_0$ on the fluctuation bonds … a single test $|B|<\delta'_k/g_k$". We use three clauses. **BOX-bg:** the output real background $U_{\rm out}$ is the canonical real regular critical background of the output datum $D_{\rm out}$; output datum loops meeting the distance-$1$ neighbourhood of $\Lambda^{\rm pr}$ obey $|\partial D_{\rm out}(\tau)-I|\le C_{\rm bx}C(M)\varepsilon_t$, and all other output datum loops obey the tests in force before the output. **BOX-id:** the phase-$N_t$ background equals $(e^{i\eta H}U_{\rm out})^g$ with $g$ real and $(H,K)$ the box response at $s=\mathbf 1$ (the "corresponding BOX relation" of st1-r2 Lemma 11). **BOX-resp:** the box response has $n_b(H,K)\le C(M)E_{\bar\kappa}\delta'_te^{-\mu d_+(b,\Lambda^{\rm pr})}$, in the output layer scales, with the fixed DR rate $\mu$. Here $C_{\rm bx}$ is the fixed constant of "$\varepsilon\le C\varepsilon_k$" (row 2) and $C(M)$ is chosen after $M$ (SA 17612: "Hence $C(M)$ is a constant fixed before $\gamma$").
* **ST-test** (our specification of the stage test). Source: SA 17585, "Before this, tests at the sharper threshold $\delta'_j:=g_jA_1p_1(g_j)$ are made, formed with backgrounds localised in $X$"; SA 17396, "On the support of the tests of a stage, the following tests equal $1$: … those of the single stored step whose fields the stage integrates (the plaquette tests of its two levels, the gauge indicators, the approximate fluctuation tests)". SA does not fix the localization margin or which background is meant. We specify: at the stage of level $j$, every removed free row $b$ satisfies $|i^{-1}\operatorname{Log}(D_{\rm old}(b)V^\sharp(b)^{-1})|<\delta'_j$, where $V^\sharp=M_-(U^\sharp_+)$ and $U^\sharp_+$ is the new (post-stage) background localised in $X^\sharp$, the set of points within $\ell^\infty$ distance $\tfrac14$ of a level-$t$ cell from $X$; on the same support every removed row, pivots included, has logarithm relative to $V^\sharp$ below $c_{\rm ch}/4$ (the approximate fluctuation tests of SA 17396 with $CL\delta'_j\le\frac12\delta_j$, SA 17624). Lemma F7 checks that this test keeps SA's history locality.
* **LOC-form** (for Lemma F6). The localised background $U^\sharp_+$ is the canonical real regular background of a datum $D^\sharp_+$ for the same determining system, with $D^\sharp_+=D_+$ on every row within weighted distance $R_\sharp$ of the stage carriers, $R_\sharp\ge\frac14MR_t$ (the weighted width of the $\frac14$-cell margin of ST-test). **Alternatively LOC-decay:** SA 17387, "The artificial boundary conditions of localised minimisers act only through $e^{-c\delta_0\operatorname{dist}}$", read as $|i^{-1}\operatorname{Log}(V^\sharp(b)V(b)^{-1})|\le C_{\rm loc}e^{-c_{\rm loc}d(b,\partial X^\sharp)}$ with fixed $C_{\rm loc},c_{\rm loc}$. Either suffices for Lemma F6.
* **STRIP** (only for the main-step remark F8). SA 17521–17522: "$V^{\rm bg}_j(V^{\rm loc}_j)^{-1}=e^{i\mathbf H^{(j)}}$, $|\mathbf H^{(j)}|\le C\varepsilon_je^{-\check R_j}$".

### 0.3 Constants (additions to st1-r2's order)

IN1 requires the precision constants, and every uniform background or tower constant feeding them, to be fixed before $\kappa$, independently of $M$ and $\bar\kappa$, with $M$ used only through lower bounds. Each new constant is listed with its row.

| Constant | Defined in | Row | Before $\kappa$? Independent of $M,\bar\kappa$? |
|---|---|---|---|
| $c_N,r$ (RUN-low) | §0.2 | 1 | yes, yes |
| $C_{\rm bx}$; $C'_A=(1+2C_vL)C_{\rm ch}L^4$; $C_A=9/4$ | §0.2, Theorem F4 | 2 | yes, yes |
| $C_{\rm loc},c_{\rm loc}$ (if LOC-decay) | §0.2 | 2 | yes, yes |
| $K^\flat=e^{\delta}(1+\beta_s)K^\sharp/c_{\min}$ | Lemma 9′ | 4 | yes, yes |
| $\tau_0(i)=\tfrac25d_*(i)$ | Lemma 11′ | 1–4 (fixed fractions) | yes, yes |
| $K_{\rm core}=8L^3C_{\rm os}K^\flat(1+c_\natural)/c_{\min}$, $r_*$ | Lemma 11′ | 6 | yes, yes |
| $C_{\rm out}=16C_{\rm lev}/(\theta_s\beta_s\alpha_0r_*)$ | Lemma B2 | 6 | yes, yes |
| $C(M)$ (BOX) | SA 17656 | after 8 | **no**: depends on $M$; enters only the $\gamma$ ceilings $\gamma_B(M)$, $\gamma'_B(M,\bar\kappa)$ of row 10 |
| $\gamma_B,\gamma'_B,\gamma_F$ | Lemmas B1, B2, F6 | 10 | ceilings on $\gamma$, chosen last |

No new constant enters the IN1 precision constants $(a,H,\mu_0)$. The floor $\alpha_0\ge16\max(1,C_{\rm mb})C_{\rm RA}/c_{\min}^2$ of row 5 is unchanged; Lemmas 10′ and B1 use it as it stands.

## 1. Repair M: deleted marks

**What fails in st1-r2.** In (17) the term $-\beta_R\sum_{u\in\operatorname{Re}_\sigma(x)}2^{-|m-u|}$ is a debt. When a mark is swallowed at the output of a later operation, SA removes it (SA 6113–6114, 17433). Then $c_+(x|m)-c_-(x|m)$ gains $+\beta_R\sum_{u\in D}2^{-|m-u|}$, which at $m=u\ll t$ is not paid by the output drop $\frac12\theta_s\beta_s2^{-(t-m)}$. So (13) fails for records that read a swallowed point. We do not try to pay this increase. We remove it.

**Definition M1 (mark ledger) [design, round 3].** Fix a finite history. For a drop-out mark $C$ created by the operation of level $s$, with $n(C)$ completed stages, let $\operatorname{St}(C)=\{s-N_s+n':0\le n'<n(C)\}$ be its stage levels (these are the $j_{s,n'}$ of (17)). For a structure $\sigma$ and a site $x$ put
\[
 \operatorname{Re}^*_\sigma(x)=\operatorname{Re}_\sigma(x)\ \cup
 \bigcup\{\operatorname{St}(C):\ C\ni x\text{ a drop-out mark swallowed at or before }\sigma\}.
 \tag{M1}
\]
Define $c^*_\sigma(x|m)$ by (17) with $\operatorname{Re}_\sigma(x)$ replaced by $\operatorname{Re}^*_\sigma(x)$. Every record, chain domain and gap of st1-r2 §1 is formed with $c^*$ in place of $c$. Base radii, lifts and functions are unchanged.

Thus a swallowed mark's debt is never returned; at the moment of swallowing it is even enlarged from its first $\nu(C)$ levels to all $n(C)$ of them.

**Lemma M2 (the ledger has no repeated level) [proved].** Assume GEO-mark and RUN. For every structure $\sigma$ and site $x$ the sets $\operatorname{St}(C)$, over drop-out marks $C\ni x$ created at or before $\sigma$, are pairwise disjoint. Consequently $\operatorname{Re}^*_\sigma(x)$ is a set of integers and
\[
 \sum_{u\in\operatorname{Re}^*_\sigma(x)}2^{-|m-u|}\le\sum_{u\in\mathbb Z}2^{-|m-u|}=3 .
 \tag{M2}
\]

*Proof.* Write $t_\flat=t-N_t$. RUN gives $N_t=N(\min_{u\le t}\theta_u)$ with $N$ nondecreasing; the running minimum is nonincreasing in $t$, so $N_t$ is nonincreasing (as SA 17449 also states: "since $\mathsf N_t=\check R_t$ is non-increasing"). Hence $t\mapsto t_\flat$ is strictly increasing: $(t+1)-N_{t+1}\ge t+1-N_t>t_\flat$.

Let $C\ne C'$ be drop-out marks containing $x$, created by operations of levels $s$ and $s'$. By GEO-mark(v) an operation creates at most one mark containing $x$, so $s\ne s'$; say $s<s'$. We show $s\le s'_\flat$.

*Case (a): $C$ is standing when $C'$ is created.* Then $C$ and $C'$ are standing marks sharing $x$. GEO-mark(i) says their windows $(s_\flat,s]$ and $(s'_\flat,s']$ are disjoint. Since $s<s'$ and $s'\in(s'_\flat,s']$, disjointness forces $s\le s'_\flat$.

*Case (b): $C$ was swallowed before $C'$ was created.* By GEO-mark(ii), $C$ was swallowed at the output of an operation of some level $i$, by a healed component or island $X_i$ of that operation which contains $C$. If $i=s'$, then $x$ lies in $X_i$ and in the drop-out $C'$ of the same operation, two different class components, against GEO-mark(v). So $s<i<s'$. At operation $i$, $C$ was standing and lay inside the class component $X_i$; GEO-mark(i) gives $s<i_\flat$. Strict monotonicity gives $i_\flat<s'_\flat$. So $s<s'_\flat$.

In both cases $\max\operatorname{St}(C)\le s-1<s\le s'_\flat=\min\operatorname{St}(C')$ (the stage levels of $C'$ start at $s'-N_{s'}$). So the two sets are disjoint. Each $\operatorname{St}(C)$ is a set of distinct integers. (M2) is the geometric series $1+2\sum_{k\ge1}2^{-k}=3$. ∎

**Lemma 1′ (stage reserve with the ledger) [proved].** Replace $c$ by $c^*$ in Lemma 1. Then $c_{\min}\le c^*_\sigma\le1+\beta_s$ with the same $c_{\min}=1-11\beta_s/8-3\beta_R\ge39/64$, and the drops (18) hold at every actual transition $-\to+$ of the history: main steps, stages, outputs, and outputs at which marks are swallowed.

*Proof.* Range. The first three terms of (17) lie in $[1-\beta_s,1+\beta_s]$. The stage debt is at most $3\beta_s/8$ (st1-r2 Lemma 1, unchanged). The ledger debt is at most $3\beta_R$ by (M2). This is the same arithmetic as Lemma 1, whose only use of the marks was that they form a set without repeated level.

Drops. Across any compared transition $-\to+$, $\operatorname{Re}^*_-(x)\subset\operatorname{Re}^*_+(x)$. Indeed: a standing mark at $-$ either stands at $+$ with no smaller $\nu$ (GEO-mark(iv)), so its levels persist; or it is swallowed at this transition, and then (M1) records all its $n(C)$ levels, which contain its first $\nu_-(C)$ levels; or it was already swallowed, and its ledger entry is unchanged. New marks only add levels. Hence
\[
 c^*_-(x|m)-c^*_+(x|m)=\bigl[\text{the drop of Lemma 1 with the marks of }-\text{ held fixed}\bigr]
 +\beta_R\!\!\sum_{u\in\operatorname{Re}^*_+(x)\setminus\operatorname{Re}^*_-(x)}\!\!2^{-|m-u|}
\]
and the last sum is nonnegative. The bracket is exactly the computation in Lemma 1, which gives (18). ∎

The deleted-mark term that st1-r2 found missing is therefore absent: no reset comparison is needed, because no record's coefficient ever increases.

**Lemma M3 (consumer inclusion for M) [proved].** For a fixed record (function, read set, base radius, lift), the condition with radius $c^*_\sigma R$ implies the condition with radius $c_\sigma R$ (st1-r2's standing-mark coefficient (17)), which implies the condition with SA's coefficient (R22) of SA 6124–6134. Hence, with the same lifts and base radii, $\mathcal D^*_{a|\sigma}\subset\mathcal D_{a|\sigma}\subset\mathcal D^{\rm SA}_{a|\sigma}$.

*Proof.* Pointwise $c^*\le c\le c^{\rm SA}$: the ledger contains the standing marks, and (17) differs from SA's (R22) only by the subtracted stage debt. Every record condition is of the form "quantity $<$ coefficient $\times$ positive radius", or a real-potential gauge bound that carries no coefficient (SA 6145, "except for the real-potential gauge bounds"). Both kinds are monotone in the coefficient. ∎

So the ledger never enlarges a consumer domain. A consumer needs a *lower* bound on its domain only through $c\ge c_{\min}$ (Cauchy room and formation), which Lemma 1′ keeps.

**Where M enters st1-r2.** Lemma 1 is replaced by Lemma 1′. The compatibility (13) now holds at every actual transition, so the clause "Theorem 14 assumes the actual gaps (13); the same-marks calculation does not establish them at a reset" is discharged: Theorem 14 hypothesis 2's gaps are Lemma 1′. Lemma 11's drift telescope uses only $c^*\in[c_{\min},1+\beta_s]$, so its total "at most $1+\beta_s-c_{\min}\le41/64$" is unchanged. No constant changes.

## 2. Repair R: minimum-lift cores

### 2.1 The scalar-infimum core cannot be formed

st1-r2 §1 defines a core radius as $b_\iota=\alpha_\iota\varepsilon_i\inf_{X_r}[c_\sigma(x|i)\lambda_\tau(x)]$, one scalar for the whole address $X$. Outstanding R asks for (62). We show that (62) is false, and that the core so defined is not admitted by the tests.

**Proposition R0 (counterexample) [proved].** Fix rows 1–8 and any $K\ge1$. Assume A1/F0/REG, AV/CURV, RUN-low, GEO-box and Lemma 10's output rule. For every sufficiently small $\gamma$ there exist an output structure of an operation of level $t$, a core address $X\subset\Omega_t$ of level $i=t$, and a real datum satisfying (58), such that:

1. some $x_1\in X$ with $m(x_1)=t$ has $\lambda(x_1)\varepsilon_t\ge K\varepsilon_t\inf_X\lambda$; so (62) fails for every fixed $C_{\rm c}$;
2. the actual real background violates the scalar core's curvature clause $|\partial U-I|<b_0\eta_t^2$ with $b_0=K\alpha_0\varepsilon_t\inf_X(c\lambda)$; so no fixed formation multiplier admits it.

*Proof.* *Geometry.* Take a history whose only nontrivial event near a region of the torus is one component $X_h$ healed at the output of an operation of level $t$. Such histories exist: SA 17583 says "For $k>\mathsf N_k$ the class is non-empty: a single cell created at step $k-\mathsf N_k$, with nothing else, belongs to it." Take the declared formation exponent $0$ at every point never raised (Lemma 10 allows any declared exponents obeying (56)). By GEO-box every corner within distance $1$ of $\Lambda^{\rm pr}$ has original layer at most $k_\sharp$, so Lemma 10's output rule gives it the newly set exponent $e_{t-1}+1=(t-1-k_\sharp-1)+1=N^0_t-1$. Write $E_0=N^0_t-1$. By RUN-low,
\[
 L^{E_0}=R_{k_\sharp+1}\ge c_N(\log\theta_{k_\sharp+1})^r\ge c_N(2\log\gamma^{-1})^r ,
\]
so $E_0\to\infty$ as $\gamma\to0$.

Choose $D_0=(8E_0\log L_\flat+4\log2)/\delta$, a point $x_{\rm far}$ in the top layer at weighted distance at least $D_0$ from every raised point, and a connected union $X$ of level-$t$ cubes in $\Omega_t$ containing $x_{\rm far}$ and the read set of one level-$t$ datum loop $\tau_1\subset\Lambda^{\rm pr}$. (The torus is finite but arbitrary; take it large.) Then (56) gives $\lambda(x_{\rm far})=\max\{1,\max_zL_\flat^{2E_0}e^{-\delta d(x_{\rm far},z)/4}\}=1$, since $L_\flat^{2E_0}e^{-\delta D_0/4}=\frac12$ and the exponent at $x_{\rm far}$ itself is $0$; while $\lambda(x_1)\ge L_\flat^{2E_0}$ at a corner $x_1$ of $\tau_1$. So $\lambda(x_1)/\inf_X\lambda\ge L_\flat^{2E_0}$, which exceeds $K$ for small $\gamma$. Since $m(x_1)=t=i$, the left side of (62) at $x_1$ is $\lambda(x_1)\varepsilon_t$. This proves 1.

*Datum.* Let $c_1$ be a level-$t$ row of $\tau_1$ whose double block lies in $\Lambda^{\rm pr}$. Put the datum equal to $I$ on every row except $c_1$, and $e^{i\varphi\sigma_3}$ on $c_1$, with $2\sin(\varphi/2)=\frac12C_{\rm te}L_\flat^{2E_0}\varepsilon_t$. The ceiling (56), $L_\flat^{2E_0}\le C_R^2(\log\theta)^{2r_R}$, makes $\varphi$ small for small $\gamma$. A datum loop containing $c_1$ has holonomy $e^{\pm i\varphi\sigma_3}$ up to conjugation, so $|\partial V(\tau)-I|=2\sin(\varphi/2)\le C_{\rm te}L_\flat^{2E(\tau)}\varepsilon_t$; every other loop has $\partial V=I$. So (58) holds, strictly, and the datum is real and regular. A1/Lemma 5 gives its real regular critical background $U$.

*Lower bound.* Let $v$ be the largest normalized real curvature $l^2\eta^{-2}|\partial U(\pi)-I|$ over the plaquettes read by $\tau_1$. If $v$ exceeds the AV/CURV ceiling, 2 holds trivially for small $\gamma$. Otherwise AV/CURV's test bound ("$2\epsilon$ inside a layer", read as in Lemma 10: if the normalized background curvature on the plaquettes read by a datum loop is at most $\epsilon$, below the fixed ceiling, the loop's normalized curvature is at most $2\epsilon$; after healing, $\Lambda^{\rm pr}$ is one layer, so no seam) gives $|\partial V(\tau_1)-I|\le2v$, hence
\[
 v\ge\tfrac14C_{\rm te}L_\flat^{2E_0}\varepsilon_t=\tfrac32C_{\rm sm}L^4L_\flat^{2E_0}\varepsilon_t .
\]
In level-$t$ units $l=1$ on layer $t$, so the core clause reads $v<b_0$, while $b_0=K\alpha_0\varepsilon_t\inf_X(c\lambda)\le K\alpha_0\varepsilon_t(1+\beta_s)\lambda(x_{\rm far})\le\frac54K\alpha_0\varepsilon_t$. For $\gamma$ so small that $\frac32C_{\rm sm}L^4L_\flat^{2E_0}>\frac54K\alpha_0$, the clause fails. The read set of $\tau_1$ lies in $X$, so this is a violation of the core at $X$. ∎

The counterexample refutes the implication "hypotheses of Lemma 10 $\Rightarrow$ scalar-core formation". It uses only data that (58) admits; since all its test inequalities are strict, an open set of data has the same property, but we do not need that. It shows that st1-r2's scalar core is not a formable record at arbitrary addresses, whatever comparison one tries. It does not contradict SA: SA 6143–6145 multiplies "the layer-$m$ radii" by the pointwise lift, and SA 6150–6151 imposes "the simple, tower and small-field-core clauses with those layer radii". The scalar infimum over $X$ was introduced in distillation so that Lemma 9 could use a constant $b_0$. We now make Lemma 9 work with per-element radii.

### 2.2 The lifted core

**Definition R1 (lifted core) [design, round 3].** Let $i\ge1$, $X$ a core address of level $i$, $\tau$ the birth structure of the record, $\sigma$ the current structure. The **lifted core** $\mathcal U^\lambda_{i}(X)$ is the family of the following read records, each with its own read set $\operatorname{Rd}(e)$ (the contained stencil of the element $e$, of weighted diameter at most $1$) and its own **single scalar** radius
\[
 b_\iota(e)=\alpha_\iota\varepsilon_i\inf_{\operatorname{Rd}(e)}\bigl[c^*_\sigma(\cdot|i)\lambda_\tau\bigr],\qquad\iota=0,1 .
 \tag{R1}
\]
(a) For each fine bond $b$ of $X$: $|A'(b)|,|\nabla^UA'(b)|<b_1(b)$ and $|\mathbf J(b)|<b_0(b)$.
(b) For each plaquette $\pi\subset X$: $|\partial U(\pi)-I|,|\partial\mathbf U(\pi)-I|<b_0(\pi)\eta_i^2$.
(c) For each contained cube $Q$ of side at most $C_{\rm box}LM$: a real gauge with $|A|,|\nabla A|<C_{\rm pot}M\Lambda_Q\alpha_0\varepsilon_i$, $\Lambda_Q=\sup_{Q^+}\lambda_\tau$ (st1-r2's witness rule $g_Q\Lambda_Q\alpha_0\varepsilon_i$ for the core family, with no coefficient, as SA 6145 prescribes for real-potential gauge bounds).
(d) For each allowed subdomain $Z\subset X$ of level $p\le i$, both erosion rules, each $1\le n\le p$, and each complete element $e$ of $Z^{\wr p}$: the tower (8) exists on its open continuation domain and, with $G$ as in st1-r2 Lemma 9 and $\lambda_p=L^{-(i-p)}$,
\[
 |G_n(e)|<b_0(e)\lambda_p ;
 \tag{R2}
\]
also at $A'=0$.

Each record of (R1) is a single scalar over its read set, formed as the infimum of the whole coefficient–lift product, exactly as st1-r2 §1 requires of a core radius. What changes is the read set: an element's stencil, not the whole address. Its effective coefficient is $c^{\rm eff}_\sigma(e)=\inf_{\operatorname{Rd}(e)}(c^*_\sigma\lambda_\tau)/\inf_{\operatorname{Rd}(e)}\lambda_\tau\in[c_{\min},1+\beta_s]$.

**Lemma R2 (slow variation of the radii) [proved].** (i) If $\operatorname{Rd}(e)\cap\operatorname{Rd}(e')\neq\varnothing$, then $b_\iota(e')\le e^{\delta/2}\frac{1+\beta_s}{c_{\min}}b_\iota(e)$. (ii) Let $d^\circ$ be the metric of any tower's ambient sequence in (d). For elements $e,e'$ with base sites $x_e,x_{e'}$, $b_\iota(e')\le\frac{1+\beta_s}{c_{\min}}e^{\delta/2}e^{\delta_Td^\circ(x_e,x_{e'})}b_\iota(e)$.

*Proof.* (57) gives $\lambda_\tau(z)\le e^{\delta d_\tau(x,z)/4}\lambda_\tau(x)$. Stencils have $d_\tau$-diameter at most $1$, so $\lambda_\tau$ varies on $\operatorname{Rd}(e)\cup\operatorname{Rd}(e')$ by at most $e^{\delta/2}$ in (i). The coefficient lies in $[c_{\min},1+\beta_s]$ by Lemma 1′; it is not slowly varying, which is why the ratio $(1+\beta_s)/c_{\min}$ appears. For (ii), the ambient sequence of (d) is a meet of the frozen sequence of $\tau$ with an erosion tower, truncated at $p$. Its scale is at most $l_\tau$, so its density is at least $1/l_\tau$ and $d^\circ\ge d_\tau$ (st1-r2 (21), first inequality). Then $\lambda_\tau(x_{e'})\le e^{\delta d^\circ(x_e,x_{e'})/4}\lambda_\tau(x_e)$, and $\delta/4=\delta_T$. Add the two stencil diameters. ∎

The rate is not a coincidence. st1-r2 smoothed the lift at rate $\delta/4$ and set $\delta_T=\delta/4$; (49) bounds a tower difference by a **maximum** weighted at rate $\delta_T$, not a sum. A radius that grows at most at that rate therefore passes through (49) with no loss, as the next proof shows.

**Lemma 9′ (CORE for the lifted core) [proved].** Let $i\ge1$, $0<\tau_0<1$, $c_\natural\ge1$, and radii (R1) with $\sup_e2(b_0+b_1)(e)\le a^\sharp$. Suppose $P$ lies in the lifted core with every radius multiplied by $1-\tau_0$, and the shift obeys, at each bond $b$,
\[
 |H(b)|,|\nabla^{\mathbf U}H(b)|<s(b):=\frac{\tau_0b_0(b)}{18K^\flat(1+c_\natural)},\qquad
 |\mathbf J+K|(b)<b_0(b),\qquad K^\flat=e^{\delta}\frac{1+\beta_s}{c_{\min}}K^\sharp .
 \tag{R3}
\]
Then $P\dotplus h$ lies in the lifted core with radii (R1), with the stated pair and fixed real factor, holomorphically on its fixed-real-factor fibre.

*Proof.* *Local clauses (a), (b).* Fix an element $e$ and let $s_e=\max\{s(b):b\in\operatorname{Rd}(e)\}$. Lemma R2(i) gives $s_e\le e^{\delta/2}\frac{1+\beta_s}{c_{\min}}\frac{\tau_0b_0(e)}{18K^\flat(1+c_\natural)}\le\frac{\tau_0b_0(e)}{18K^\sharp(1+c_\natural)}$. Apply (46) with $s=s_e$ on the contained stencil of $e$: potential increments are at most $2s_e$ and the curvature increment at most $4s_e\eta_i^2$. Both are less than $\tau_0b_0(e)$, which is the room between $(1-\tau_0)b(e)$ and $b(e)$; for (a) use $b_0\le b_1$. The current clause is the hypothesis $|\mathbf J+K|<b_0$. The hypotheses of (46), $|A'|,|\nabla A'|\le\beta_1$, $|\partial\mathbf U-I|\le\beta_0\eta^2$, $\beta_0,\beta_1,s\le1/60$, hold because $\sup(b_0+b_1)\le a^\sharp/2\le1/120$.

*Witness clause (c).* The real factor $U$ is fixed, so the real gauge witnesses are unchanged and their old bounds are stricter.

*Towers (d).* Fix $Z,p,n$ and a complete element $e$ with base $x_e$. As in Lemma 9, on $Z\subset\Omega_i$ the ambient sequence truncated at $p$ has scale $\lambda_p$, and (R2) is the tower condition. Both $A'$ and $A''$ satisfy Lemma 8's absolute hypotheses by (46) and $\sup2(b_0+b_1)\le a^\sharp$; Lemma 8's open-domain statement gives existence. Put $D=A''-A'$. By (46) and Lemma R2(i), $\max\{|D(b)|,|\nabla^UD(b)|\}\le2s_b$ with $s_b=\max_{\operatorname{Rd}(b)}s$. By (49) and the site-to-top factor,
\[
 |\Delta G(e)|\le e^{4\delta_T}K_T\max_b e^{-\delta_Td^\circ(x_e,b_-)}\lambda_p\,2s_b .
\]
Lemma R2(ii) gives $s_b\le\frac{1+\beta_s}{c_{\min}}e^{\delta/2}e^{\delta_T(d^\circ(x_e,b_-)+2)}\frac{\tau_0b_0(e)}{18K^\flat(1+c_\natural)}$, where $+2$ pays for moving from $b_-$ to the stencil of $b$. The exponential weights cancel:
\[
 |\Delta G(e)|\le e^{4\delta_T}K_T\cdot2\lambda_p\frac{(1+\beta_s)e^{\delta}}{c_{\min}}\cdot\frac{\tau_0b_0(e)}{18K^\flat(1+c_\natural)}
 =\frac{e^{4\delta_T}K_T}{9K^\sharp(1+c_\natural)}\tau_0b_0(e)\lambda_p<\tau_0b_0(e)\lambda_p ,
\]
since $K^\sharp\ge e^{4\delta_T}K_T$ and $\delta_T\le\delta/2$ was used in $e^{2\delta_T}\le e^{\delta/2}$. The input obeys $|G(e)|<(1-\tau_0)b_0(e)\lambda_p$, so the output obeys (R2). The case $A'=0$ is the same computation. Holomorphy follows from the logarithm in (10) and the continued towers, as in Lemma 9. No bound on $b_1^2/b_0$ is used. ∎

**Lemma 10′ (formation of lifted cores) [proved].** Under the hypotheses of Lemma 10, at the real plain triple of the actual background, every record of the lifted core is admitted with base multiplier $c_{\min}/4$, at every core address, with no comparison of lifts at distant points.

*Proof.* Fix an element $e$ with base $x$. Write $m=m(x)\ge i$ for points of $X\subset\Omega_i$, and use level-$i$ units, so $l(x)=L^{m-i}\ge1$.

(a) $A'=0$. By (59), $|\mathbf J|=|J_+|\le l^{-3}C_{\rm RA}\lambda(x)\varepsilon_m\le C_{\rm RA}\lambda(x)\varepsilon_i(2L^{-3})^{m-i}\le C_{\rm RA}\lambda(x)\varepsilon_i$, using $\varepsilon_m\le2^{m-i}\varepsilon_i$ (Lemma 1). The target is $\frac{c_{\min}}4b_0(e)\ge\frac{c_{\min}^2}4\alpha_0\varepsilon_ie^{-\delta/4}\lambda(x)$, because $x\in\operatorname{Rd}(e)$ and $\operatorname{Rd}(e)$ has diameter at most $1$. Row 5 gives $\frac{c_{\min}^2}4\alpha_0\ge4C_{\rm RA}>e^{1/4}C_{\rm RA}$, and $\delta\le1$.

(b) The same with $L^{-2(m-i)}$ in place of $L^{-3(m-i)}$, and $\partial\mathbf U=\partial U$ at $A'=0$.

(c) Equation (60) with the core family's quotient $16L^3B_*(s+2)/(C_{\rm pot}M)\le C_{\rm mb}$ and row 5, as in Lemma 10; the carrier conditions (61) are those of Lemma 10.

(d) Restriction makes the real tower a real gauge transform of the restricted background, on the settled eroded interior (Lemma 8, last paragraph; Lemma 5's restriction assertion). Hence $|G_n(e)|$ equals the background's normalized curvature or current at scale $\lambda_p$, which is at most $\lambda_p$ times the corresponding quantity at the background's own scale $l(x)\ge1\ge\lambda_p$. The comparison of (a)–(b) then gives $|G_n(e)|<\frac{c_{\min}}4b_0(e)\lambda_p$. AV and P81 give the open datum domain and tube room, as in Lemma 10. ∎

**Lemma 11′ (core part of the half-gap substitution and of drift) [proved].** In Lemma 11 replace the core paragraph by the following. For a lifted-core element $e$, put $b^\pm_\iota(e)$ for its radii at the two structures, $b^{\rm mid}_\iota(e)=\frac12(b^-_\iota+b^+_\iota)(e)$, $\tau_e=(b^-_0-b^+_0)/(b^-_0+b^+_0)(e)$. Then
\[
 \tau_e\ge\tau_0(i):=\frac{d_*(i)}{2(1+\beta_s)}\ge\tfrac25d_*(i),\qquad b_0^{\rm mid}(e)\ge c_{\min}\alpha_0\varepsilon_i ,
\]
and with $K_{\rm core}=8L^3C_{\rm os}K^\flat(1+c_\natural)/c_{\min}$ in (64), $r=\|h\|_w\le r_*$ implies the hypotheses of Lemma 9′ at the midpoint radii with $\tau_0(i)$. Drift of lifted-core records is the drift of Lemma 11 applied element by element.

*Proof.* $\inf_{\operatorname{Rd}(e)}(c^*_-\lambda)\ge\inf_{\operatorname{Rd}(e)}((c^*_++d_*(i))\lambda)\ge\inf(c^*_+\lambda)+d_*(i)\inf\lambda$ by Lemma 1′, and each infimum is at most $(1+\beta_s)\inf\lambda$. This gives $\tau_e\ge\tau_0(i)$, uniformly in $e$; and $P\in$ core$((1-\tau_e)b^{\rm mid})\subset$ core$((1-\tau_0)b^{\rm mid})$. The lower bound on $b^{\rm mid}_0$ uses $\lambda\ge1$ and $c^*\ge c_{\min}$. As in Lemma 11, incident boundary bonds may start in layer $i-1$; restriction and (66) bound each shift quantity by $4L^3rw(i)=2L^3rd_*(i)\alpha_0\varepsilon_i$. For $r\le r_*\le(8K_{\rm core})^{-1}$ this is at most $\frac{d_*(i)c_{\min}\alpha_0\varepsilon_i}{32C_{\rm os}K^\flat(1+c_\natural)}<\frac{\tau_0(i)b^{\rm mid}_0(e)}{C_{\rm os}K^\flat(1+c_\natural)}$ with $C_{\rm os}=18$, which is (R3) at the midpoint. The current stays below $b^{\rm mid}_0$ as in Lemma 11. Drift: the increment estimates used in Lemma 11's drift paragraph are the estimates just proved, applied to the real reverse shift on each fixed element; the telescope is unchanged. ∎

**Where R enters st1-r2.** In §1, the core record is replaced by the lifted core (Definition R1); the read-record rule ("a core radius is a single scalar … the infimum of the whole product over its read set") is kept and applied per element. (11)–(12) become (a)–(d) of R1. Lemma 9 is replaced by Lemma 9′; its constant $K^\sharp$ becomes $K^\flat$ in (55) and in (64)'s $K_{\rm core}$. Lemma 10's sentence "The core records require the additional comparison described below" and Outstanding R are replaced by Proposition R0 and Lemma 10′. Lemma 11's core paragraph is Lemma 11′. Theorem 14 hypothesis 2 ("all required working cores") now refers to lifted cores. The lifted core contains st1-r2's scalar core (radii $\ge$ scalar infimum), so the consumer domain grows; that consumer change is part of CI (§4.3).

## 3. Constants check for R and M

$K^\flat$ is a fixed multiple of $K^\sharp$ (row 4), with factor $e^\delta(1+\beta_s)/c_{\min}\le e\cdot\frac54\cdot\frac{64}{39}<6$. $\tau_0(i)$ is a fixed fraction of $d_*(i)$. $K_{\rm core}$ and $r_*$ (row 6) are increased by that fixed factor. The floor on $\alpha_0$ is unchanged. Nothing depends on $M$, $\bar\kappa$ or $\gamma$. The ledger (M1) changes no constant.

## 4. Repair B: admission of the output and of the changed consumers

### 4.1 Output admission

**Lemma B1 (output tests and output formation) [proved].** Consider the output of an operation of level $t$ with a healed component $X$ (for an island, the same proof applies to the output records it forms, provided BOX-bg holds for that output). Assume BOX-bg, GEO-box, RUN-low, (56) for newly set exponents, and the hypotheses of Lemma 10 before the output. There is $\gamma_B(M)>0$, depending on $C(M)$ and fixed constants, such that for $\gamma\le\gamma_B(M)$: every output datum loop $\tau$ satisfies (58) with the same $C_{\rm te}=6C_{\rm sm}L^4$ and with Lemma 10's output exponents; consequently (59) holds for $U_{\rm out}$ with the same $C_{\rm RA}$, and Lemma 10 and Lemma 10′ admit every output record (pointwise, absolute, tower, lifted-core, witness) with base multiplier $c_{\min}/4$.

*Proof.* *Loops near the box.* Let $\tau$ meet the distance-$1$ neighbourhood of $\Lambda^{\rm pr}$. By GEO-box its corners have original layer at most $k_\sharp$, and they are newly healed, so Lemma 10's output rule gives $E(\tau)=e_{t-1}+1=N^0_t-1$. BOX-bg gives $|\partial D_{\rm out}(\tau)-I|\le C_{\rm bx}C(M)\varepsilon_t$. So (58) at $\tau$ follows from
\[
 C_{\rm bx}C(M)\le C_{\rm te}L_\flat^{2(N^0_t-1)} .
 \tag{B1}
\]
By RUN-low, $L^{N^0_t-1}=R_{k_\sharp+1}\ge c_N(2\log\gamma^{-1})^r$, and $L_\flat^{2(N^0_t-1)}=(L^{N^0_t-1})^{2\log L_\flat/\log L}$ with $2\log L_\flat/\log L>0$ because $L_\flat\ge2$. So (B1) holds for $\gamma\le\gamma_B(M)$. This is a ceiling on $\gamma$ chosen after $M$; SA 17612 says the same order ("$C(M)$ is a constant fixed before $\gamma$").

*Other loops.* By BOX-bg they obey the tests in force before the output. A newly healed point raised at an earlier stage $j<t-1$ had exponent $e_j+1\le e_{t-1}+1$ ($e_j$ is nondecreasing in $j$ by its definition in Lemma 10), so an inherited test (58) remains (58) with the output exponent. Loops whose tests read $2\varepsilon_t$ satisfy (58) because $C_{\rm te}\ge2$.

*Formation.* $U_{\rm out}$ is a real regular critical background (BOX-bg), so PROF applies to it. The proof of (59) in Lemma 10 then applies word for word; the formation arguments of Lemma 10 and Lemma 10′ use only (59), (60)–(61) and the ceilings of row 10. The global lift ceiling (57) holds because the newly set exponent obeys (56). ∎

Remark. The displayed BOX condition of st1-r2, $C(M)\le c_{\min}\alpha_0L_\flat^{2(N^0_t-1)}/4$, is neither needed nor sufficient; (B1) is the inequality that the formation proof actually uses, and RUN-low is the lower-growth bound that makes $\gamma$ enforce it. An upper bound on $N^0_t$ could not.

**Lemma B2 (output source budget; BOX version of (71)) [proved].** Assume BOX-resp. At the output transition, with the input (output-structure) metric and layers in (71), and $S=\Lambda^{\rm pr}$,
\[
 a_X\le C_{\rm out}C(M)E_{\bar\kappa}\frac{A_1}{A_0}(\log\theta_t)^{-(p_0-p_1)}
 +C(M)E_{\bar\kappa}\frac{A_1}{A_0}\frac{K_{\rm pin}}{\epsilon_{\rm lev}}\varepsilon_t ,
 \qquad C_{\rm out}=\frac{16C_{\rm lev}}{\theta_s\beta_s\alpha_0r_*},
 \tag{B2}
\]
with $C_{\rm out}$ fixed in row 6, before $\kappa$, independent of $M,\bar\kappa$. Hence $a_X<1/2$ for $\gamma\le\gamma'_B(M,\bar\kappa,A_1/A_0)$, and Lemma 13's conclusions (levelling on $|z|<\rho_X$, (72)) hold at the output.

*Proof.* In (71) replace $D_{\rm src}$ by $C(M)E_{\bar\kappa}\delta'_t$ (BOX-resp), and recall $\delta'_t=(A_1/A_0)(\log\theta_t)^{-(p_0-p_1)}\varepsilon_t$ (SA 17624: "The ratio $\delta'_j/\varepsilon_j=(A_1/A_0)(\log x_j)^{-(\mathfrak p_0-\mathfrak p_1)}$"). At the output, (18) gives $d_*(m)=\frac12\theta_s\beta_s2^{-(t-m)}$, so $w(m)=\frac14\theta_s\beta_s2^{-(t-m)}\alpha_0\varepsilon_m\ge\frac14\theta_s\beta_s4^{-(t-m)}\alpha_0\varepsilon_t$, using $\varepsilon_m\ge2^{-(t-m)}\varepsilon_t$. In the output sequence every point of the healed component has layer $t$, so a read bond of layer $m$ has $d_+(b,\Lambda^{\rm pr})\ge\rho_0(t-m-1)_+$ by (20). With $\nu=t-m$,
\[
 Q_X\le\frac{4}{\theta_s\beta_s\alpha_0\varepsilon_t}\sup_{\nu\ge0}4^\nu e^{-(\mu\rho_0/2)(\nu-1)_+}\le\frac{16}{\theta_s\beta_s\alpha_0\varepsilon_t},
\]
because row 3 gives $\mu\rho_0/2\ge\log16$, so $4^\nu e^{-(\mu\rho_0/2)(\nu-1)}\le4\cdot4^{-(\nu-1)}\le4$ for $\nu\ge1$. Also $E_X\le1$. Insert in (71). For the second claim, $(\log\theta_t)^{-(p_0-p_1)}\le(2\log\gamma^{-1})^{-(p_0-p_1)}$ and $\varepsilon_t\to0$ as $\gamma\to0$; $\gamma$ is chosen after $\bar\kappa$ (row 7), $M$ (row 8) and $A_1/A_0$ (row 9). The proof of Lemma 13 from (71) to (72) uses only Lemma 4 and the bound $a_X<1/2$. ∎

There is no factor $2^{N_t}$: the source sits at layer $t$ of the output sequence, where the output gap is largest.

**Lemma B3 (output drift) [proved].** Under BOX-id and Lemma B2, the output transition satisfies the hypothesis of Lemma 11's drift paragraph: the successive real backgrounds are related by a real gauge and the physical response with $\|h\|_w<r_*/2$.

*Proof.* BOX-id gives the relation. Lemma B2 gives $\rho_X>1$ and (72) at $z=1$, which is $\|h\|_w<r_*/2$. ∎

### 4.2 Consumers inside ST1

**Lemma B4 (ST1-internal consumers) [proved].** (i) *Enlarged witness radii.* The witness bounds $W_Q=g_Q\Lambda_Q\alpha_0\varepsilon_i$ ($g_Q=\mathsf oLMB^{cg},BM,C_{\rm pot}M$; natural cubes $a_\flat$) are consumed in st1-r2 and in this file only at: Lemma 5 (carrier gauges required by OPS/REG, which need the gauge potential below a fixed ceiling $c_{\rm rg}$); Lemmas 9 and 9′ (unchanged real witnesses, any bound); Lemma 11's drift paragraph (needs $|A|,|\nabla A|$ below a fixed ceiling for the logarithm, and $W_Q\ge g_Q\alpha_0\varepsilon_i$ to absorb a change $Cr_*d_*(i)\alpha_0\varepsilon_i$); Theorem 14's Borel witness argument (any strict bound). Each requirement holds: the upper ceilings by (61) and row 10 ($W_Q\le g_QC_\lambda(\log\theta_i)^{2r_R}\alpha_0\varepsilon_i\ll1$ after $M$); the lower bound because $\Lambda_Q\ge1$.
(ii) *Retained chain of reads.* Every record of every working chain domain $\mathcal D_{a|\sigma}$ is admitted, with half its declared radius, at every real background of the history support at every later structure: main steps, stages, outputs and resets.

*Proof.* (i) is the inspection just listed; the inequalities are (61), row 10 and $\lambda\ge1$.
(ii) A chain domain is the intersection of frozen records (st1-r2 §1). Formation of every record type: Lemma 10 (pointwise, absolute, tower, witness), Lemma 10′ (lifted cores), Lemma B1 (output). Gaps at every transition: Lemma 1′. Half-gap substitution: Lemmas 11 and 11′. Drift requires, at each transition, the physical relation with $\|h\|_w<r_*/2$: stages, Lemma 12 with Theorem F4 and Lemma 13; main steps, Lemma 12's main-step clause and Lemma 13; outputs, Lemma B3. Then Lemma 11's drift paragraph, whose telescope uses only $c^*\in[c_{\min},1+\beta_s]$ (Lemma 1′), gives admission with half radii. ∎

### 4.3 The external consumer interface CI [Outstanding]

**Statement CI.** For every carried activity $f$ supplied by NL1/LF1 at a structure $\sigma$, its declared domain contains the ST1 chain domain $\mathcal D_{a|\sigma}$ formed from: coefficient $c^*$ (Definition M1); simple and tower records with smoothed lifts $\lambda_\tau$ (Lemma 10); lifted cores (Definition R1); witness bounds $g_Q\Lambda_Q\alpha_0\varepsilon_i$. On it $|f|\le b_f$, with the interface of st1-r2 §1, and the constants of $b_f$ are fixed in an order compatible with rows 1–10 (fixed before $\kappa$ and independent of $M,\bar\kappa$, except declared amplitude factors such as $C(M)$ or $E_{\bar\kappa}$ entering later ceilings).

CI is the statement that st1-r2 abbreviates as "A carried activity $f$ is bounded by $b_f$ on its declared domain", with the declared domain now made explicit. ST1 constructs no activity, so ST1 cannot prove CI. What ST1 can do is try to reduce CI to the domains on which SA and CA-I state their bounds. Three attacks:

*Attack 1: include the ST1 domain in SA's raw-lift domain.* SA multiplies layer radii by the raw lift $L_\flat^{2e_\sigma(x)}$ (SA 6143–6145). Lemma 10's raw exponent satisfies $\mathcal E\le e_\sigma$ (check of the three cases: for $l(x)\le k_\sharp$, $\mathcal E=j-k_\sharp\le j+1-l(x)$; for $k_\sharp<l(x)\le j$, $\mathcal E=(j-l-1)_++1\le j+1-l$). But $\lambda(x)=\max_zL_\flat^{2\mathcal E(z)}e^{-\delta d(x,z)/4}$ exceeds $L_\flat^{2e_\sigma(x)}$ at unlifted points within weighted distance $8\mathcal E(z)\log L_\flat/\delta$ of a lifted point $z$. **Why it fails:** the only bound on the real background at such a point is PROF, $C_P\max_\tau e^{-\delta_Pd(x,\tau)}|\partial V(\tau)-I|$, which with a near-threshold lifted loop at distance $d$ is $C_PC_{\rm te}L_\flat^{2\mathcal E}\varepsilon e^{-\delta_Pd}$; this exceeds the raw-lift radius $\alpha_0\varepsilon$ for $d<(2\mathcal E\log L_\flat-\log(\alpha_0/(C_PC_{\rm te})))/\delta_P$, and $\mathcal E\to\infty$ as $\gamma\to0$. So formation in the raw-lift domain is not provable from PROF, which is why round 2 smoothed the lift. Inclusion of the ST1 domain in the raw-lift domain is false as a domain inclusion, since $\lambda>L_\flat^{2e_\sigma}$ there.

*Attack 2: compare family by family with CA-I's printed witness bounds.* CA-I 48527–48565 prints, for the four families, exponents $e(Q)=(m-k_0)_+,(p-k_0)_+,p-\bar m,0$ (CA-I 48573: "$e(Q)=\max\{0,m-k_0\}$ in (G1) and (G2), $e(Q)=p-\bar m$ in (G3), and $e(Q)=0$ in (a) and (G4)"). Within one operation, every exponent set by Lemma 10 obeys $\mathcal E(z)\le(m(z)-k_0)_+$ (same case check), and (20) gives $m(z)\le m(x)+1+d(x,z)/\rho_0$; with $\delta\rho_0\ge64\log L$ (row 3) this yields $\lambda(x)\le L_\flat^2L_\flat^{2(m(x)-k_0)_+}$, hence $\Lambda_Q\le L_\flat^4L_\flat^{2(m_Q-k_0)_+}$. So for (G1) and (G2) the enlarged witness radius is a fixed multiple $L_\flat^4$ of the printed one. **Why it fails for (G3) and (G4):** there the printed exponent is smaller than $(m-k_0)_+$, and $\Lambda_Q\le K\,L_\flat^{2e(Q)}$ with fixed $K$ would need every point $z$ with $\mathcal E(z)>e(Q)$ to lie at weighted distance at least $(8\log L_\flat/\delta)(\mathcal E(z)-e(Q))-C$ from $Q^+$. The available geometry gives only one $M$-cube: SA 17398–17407, "the only lower bound on the gaps is one $M$-cube of the later level", and CA-I 53781, "$Z''_i$ and $Z''_{i-1}$ are 'separated by one layer' of level-$i$ $M$-cubes". $M$ is fixed in row 8 before $\gamma$, while $\mathcal E$ reaches $N^0_t-1\to\infty$ as $\gamma\to0$. (SA 17407 adds: "A smallness $e^{-c\check R_j}$ from a separation is available only at regions produced by steps.") Unless a further geometric lemma places the lifted set at distance $\gtrsim(\log L_\flat/\delta)N^0_t$ from every (G3)/(G4) cube, the comparison fails.

*Attack 3: absorb the excess into the radius constant, or change the smoothing rate.* (a) Rescaling: the excess factor $\sup_Q\Lambda_Q/L_\flat^{2e(Q)}$ is, under the available geometry, as large as $L_\flat^{2(N^0_t-1)}e^{-\delta(M+2)/4}$, a power of $R_{k_\sharp+1}\approx(\log\theta)^r$; it is not bounded by any constant fixed before $\kappa$, and $\alpha_0$ is fixed in row 5 (IN1). (b) Faster smoothing, $\lambda'(x)=\max_zL_\flat^{2\mathcal E(z)}e^{-\delta'd(x,z)}$ with $\delta'>\delta_P$: then (59) fails next to lifted points, because PROF decays only at rate $\delta_P$; and Lemma 9′ needs $\delta'\le\delta_T$. So the smoothing rate must be at most $\delta_P$ (formation next to lifted points, through PROF) and at most $\delta_T$ (Lemma 9′, through (49)); st1-r2's rate $\delta/4=\delta_T$ meets both, and any admissible rate leaves the excess of Attack 1.

**Status.** CI is the first remaining Outstanding statement of this file. Its exact content is: NL1/LF1 must prove their activity bounds on the ST1 domains with smoothed lifts, lifted cores and enlarged witness radii (or a geometric lemma must supply the separation named in Attack 2). It is an obligation on NL1/LF1's declared domains. Inside ST1 nothing further is needed: Lemma B4 verifies every ST1-internal consumer, and Lemma M3 shows that the mark ledger never enlarges a domain.

**Where B enters st1-r2.** Lemma 10's sentence "output boxes are addressed separately below" and Outstanding B are replaced by Lemma B1. Lemma 13's last sentence ("BOX needs its own version of (71)") is Lemma B2. Lemma 11's "including a corresponding BOX relation" is Lemma B3. Theorem 14's final paragraph is replaced by Corollary 14′ (§6). Theorem 14 hypothesis 4's "declared domain" is CI.

## 5. Repair F: the actual collar-variable map

### 5.1 The stage integral

We first say exactly which integral the stage performs, because the map is the change of variables of that integral.

*Source.* SA 17585 describes stage $j$ of an operation of level $t$: "the stored variables of the outer shell of $Z_{j+1}\cap X$ are integrated out as in a small-field step." The small-field step is SA's $\mathbf T$ on a label (SA 17516): "First the multi-scale background … is formed … Next, a change of variables is made on the strip. Then a conditional Gaussian integral is taken over $\Lambda_{j+1}$." Its integral operation (SA 17531) is $\int dV_j|_{\Omega_{j+1}^c}\delta(\mathcal M(V_j)V_{j+1}^{-1})\cdots$, and at a pivot "the value of $V_j$ is taken from the constraint $\mathcal M(V_j)=V_{j+1}$" (SA 17526). CA-I 54287–54288 says: "Express $U^{(n)}_k$ through the new background $U^{(n+1)}_k$ and the fluctuation $(A_j,B_j)$ on the collar $R_n$, and call the resulting configuration the *shifted background* $\mathbb U^{\rm sh}$." The two changes of SA 7601 ("The term $\mathsf W^{(k)}$ is left over from a change of variables on the strip") and SA 7614 ("the Gaussian measure conditioned on the exterior fluctuation field, and its mean is linear in that field") are the strip substitution and the conditional mean. CA-I and SA cite Bałaban (CMP 122 (1989) 175, (1.55)–(1.60)) for the formulas; we do not read Bałaban's paper here and do not rely on it. We construct the map from SA's displayed formulas and Y3's three-dimensional template, and we prove each property.

*Setting.* Let $M_-,M_+$ be the determining maps before and after the stage (Lemma 12), $\Gamma^{\rm rm}$ the removed level-$j$ rows (the rows of the outer shell $R_n$), $\Gamma^{\rm ad}$ the added level-$(j+1)$ rows. By SA 8170–8176 (QC support), "only $b_0(c)$ occurs in the support of $q_{V,c}$": each added row $c$ has one pivot $b_0(c)\in\Gamma^{\rm rm}$. Let $\mathfrak F=\Gamma^{\rm rm}\setminus\{b_0(c)\}$ be the free removed rows. For a new datum $D_+$ in the admitted complex chart, let $U_+=\Phi(D_+)$ be its canonical continued background (Lemma 5) and $V=M_-(U_+)$; $V$ is holomorphic in $D_+$. The stage integral, in the form of SA 17531 restricted to the shell, is, for Borel $\Upsilon\ge0$ (or complex with $|\Upsilon|$ integrable),
\[
 \mathcal I[\Upsilon](D_+)=\int_{G^{\Gamma^{\rm rm}}}\prod_{b\in\Gamma^{\rm rm}}dV_j(b)\ \prod_{c\in\Gamma^{\rm ad}}\delta\bigl(F_c(V_j)D_+(c)^{-1}\bigr)\ \chi_{\rm st}(V_j)\,\Upsilon(V_j),
 \tag{F0}
\]
where $F_c$ is the one-step average (5) of the removed rows, with retained rows of the double block held at their values, $dV_j(b)$ is Haar probability, and $\chi_{\rm st}$ is the stage test of ST-test. The stored step's earlier tests equal $1$ on its support (SA 17396).

### 5.2 One stored bond: the strip map

This lemma is needed when a removed row is a stored (not integrated) variable with a strip coordinate, which happens at main steps (SA 17518–17526) and is recorded here for completeness. It is a single-bond statement and is dimension-free; it is Y3's Lemma II-26-71 (Y3 46472–46559) for $G=SU(2)$, which is the gauge group in both manuscripts.

**Lemma F1 (strip bond map) [proved; port of Y3 46490–46559].** Let $0<\delta\le1$, $\vartheta:[0,\infty)\to[0,1]$ smooth, $0$ on $[0,4/3]$ and $1$ on $[5/3,\infty)$, $H\in\mathfrak{su}(2)$. In the cutoff case assume $8\|\vartheta'\|_\infty|H|\le\delta$ and put $\theta(e^{iA'})=\vartheta(|A'|/\delta)$ ($|A'|<\pi$), $\theta(-1)=1$; in the plain case $\theta\equiv1$. Put
\[
 \Psi_H(W')=W'e^{-i\theta(W')H}e^{iH},\qquad f_H(A')=i^{-1}\log\bigl(e^{iA'}e^{-i\theta(e^{iA'})H}\bigr).
\]
Then $\Psi_H$ is a diffeomorphism of $G$ with Haar Jacobian $1$ in the plain case and $J_H(e^{iA'})=1-\frac{\vartheta'(|A'|/\delta)}{\delta|A'|}\langle A',H\rangle\in[7/8,9/8]$ in the cutoff case; $f_H(A')=A'$ for $|A'|\le4\delta/3$; and $\bigl||f_H(A')|-|A'|\bigr|\le\theta(e^{iA'})|H|$ wherever $f_H$ is defined.

*Proof.* Let $\alpha_{W'}(X)=\frac d{ds}\theta(W'e^{isX})|_{s=0}$. Differentiating $\frac12\operatorname{tr}(e^{iA'}e^{isX})$ gives $\alpha_{e^{iA'}}(X)=\frac{\vartheta'(|A'|/\delta)}{\delta|A'|}\langle A',X\rangle$; the cutoff is locally constant near $\pm1$, so $\theta$ is smooth. With $T=e^{-i\theta(W')H}e^{iH}$, the right-trivialized differential of $\Psi_H$ is $X\mapsto T^{-1}(X-\alpha_{W'}(X)H)T$. Conjugation preserves Haar volume and the rank-one factor has determinant $1-\alpha_{W'}(H)$, with $|\alpha_{W'}(H)|\le\|\vartheta'\|_\infty|H|/\delta\le1/8$. Bijectivity: $\Psi_H(W')=W$ iff $W'=T_W(W'):=We^{-iH}e^{i\theta(W')H}$. The cutoff has Lipschitz constant $2\|\vartheta'\|_\infty/\delta$ in the group distance (the derivative of $2\arcsin(s/2)$ is below $2$ on the nonconstant interval), and $|e^{icH}-e^{ic'H}|\le|c-c'||H|$, so $T_W$ is a contraction of the complete space $G$ with constant at most $2|H|\cdot2\|\vartheta'\|_\infty/\delta\le1/2$. Its unique fixed point is the preimage; the differential is invertible, so the inverse is smooth. If $|A'|\le4\delta/3$ then $\theta=0$ and $f_H(A')=A'$. The last estimate is the triangle inequality for the bi-invariant distance applied to $e^{if_H(A')}=e^{iA'}e^{-i\theta H}$. ∎

For a stored removed row $b$ with new variable $W'=e^{iA'}$, SA 17521–17523 give $D(b)=W'e^{-i\vartheta H}e^{iH}V^{\rm loc}(b)=W'e^{-i\vartheta H}V^{\rm bg}(b)$. With $V^{\rm bg}=V$ (the average of the new background), $i^{-1}\operatorname{Log}(D(b)V(b)^{-1})=f_H(A')$. In the cutoff zone $\theta$ is not holomorphic; those bonds are near variables (SA 6163: "Near bonds are the bonds in collars, rims and the nonanalytic cutoff zone"), which the activity interface treats as Borel and which Theorem 14 holds fixed.

### 5.3 The fibre chart and the measure identity

**Lemma F2 (regional fibre chart in four dimensions) [proved from CH; SA 8257–8296, Y3 46258–46347].** Assume CH, i.e. the pivot linear maps (QC19)–(QC20) and the contraction (QC22)–(QC23) of SA, under the curvature condition (QC18). For $u\in(\mathfrak{su}(2)\otimes\mathbb C)^{\mathfrak F}$ with $\|u\|_\infty<c_{\rm ch}L^{-9}$ there is a unique $a=a_V(u)$ on $\Gamma^{\rm rm}$ with
\[
 a|_{\mathfrak F}=u,\qquad q_V(a)=0,\qquad \|a\|_\infty+\|D_ua\|\,\|u\|_\infty\le C_{\rm ch}L^4\|u\|_\infty ,
 \tag{F1}
\]
holomorphic in $(u,V)$, real for real $(u,V)$; here $q_V(a)=0$ means $F(e^{ia}V)=F(V)$ on $\Gamma^{\rm ad}$. Conversely, a real $D$ on $\Gamma^{\rm rm}$ with $F(D)=F(V)$ and $|i^{-1}\operatorname{Log}(D(b)V(b)^{-1})|<c_{\rm ch}/2$ on all removed rows equals $e^{ia_V(u)}V$ with $u=i^{-1}\operatorname{Log}(DV^{-1})|_{\mathfrak F}$.

*Proof.* This is SA's (QC24), "the actual small fibre chart", with its estimate "$\|a(u)\|_\infty+\|D_ua(u)\|\|u\|_\infty\le CL^4\|u\|_\infty$" (SA 8287–8292) and its converse "any sufficiently small solution of $q_V(a)=0$ has this form" (SA 8293–8296). We record the argument, since CH is an input only for the linear pivot data. Put $d=R_V(t-h_Vd)$, $\Psi_V(t)=t-h_Vd(t)$ (QC22). On $\|t\|<cL^{-5}$, the map $d\mapsto R_V(t-h_Vd)$ sends the ball $\|d\|\le CL^2\|t\|^2$ into itself with Lipschitz constant at most $CL^5\|t\|<\frac12$ (SA 8262–8266), using $\|h_V\|\le2L^3$ (QC20). The fixed point is holomorphic in $(t,V)$ as a uniform limit of holomorphic iterates, and $q_V(\Psi_V(t))=K_Vt$ (QC23). Take $t=\mathsf C_Vu$; then $K_V\mathsf C_V=0$ and $(\mathsf C_Vu)|_{\rm free}=u$ (QC20), so $a(u)=\Psi_V(\mathsf C_Vu)$ solves $q_V(a)=0$, $a|_{\mathfrak F}=u$ (only pivot values change, SA 8279). The bound follows from $\|\mathsf C_V\|\le CL^4$ and (QC23). Converse: for a small solution $a$, $t=a+h_VR_V(a)$ satisfies $K_Vt=0$, hence $t=\mathsf C_V(a|_{\rm free})$, and uniqueness in (QC23) gives $a=a(u)$ (SA 8293–8296). Reality: at real $V$ all maps are real. Each equation uses only its own pivot and the nonpivot data of its double block (SA 8289–8290), so the chart is local. ∎

**Proposition F3 (measure identity: the stage integral in chart coordinates) [proved; port of Y3 II-26-53/55, Y3 46258–46387].** Let $g=g_j>0$, $\mathfrak b=\delta'_j/g$, and suppose the real $W\mapsto V_W$ is a Borel family of references with $F(V_W)=W$, in the chart domain. For Borel $\Upsilon(V_j,W)\ge0$ vanishing unless every free removed row has $|i^{-1}\operatorname{Log}(V_j(b)V_W(b)^{-1})|<g\mathfrak b'$ and every removed row has logarithm below $c_{\rm ch}/2$, with $g\mathfrak b'\le c_{\rm ch}L^{-9}$,
\[
 \int\Upsilon\bigl(V_j,F(V_j)\bigr)\prod_bdV_j(b)
 =(\sigma_{\rm H}g^3)^{\#\mathfrak F}\int dW\,e^{\sum_c\mathsf z_c(V_W)}
 \int_{|B|<\mathfrak b'}e^{\mathsf J_W(B)}\Upsilon\bigl(e^{ia_{V_W}(gB)}V_W,W\bigr)dB ,
 \tag{F2}
\]
where $dW$ is Haar on $G^{\Gamma^{\rm ad}}$, $\mathsf z_c(V)=-\log\det n_c(V)$ with $n_c(V)$ the right-trivialized derivative of $F_c$ in its pivot (SA (QC16)–(QC17): $J_c(I)=L^{-3}I_3$, $\|J_c^{-1}\|\le2L^3$), $\mathsf J_W(B)=\sum_c\log\det(1-\mathsf{Jb}_c(V_W,gB))+\sum_{b\in\mathfrak F}\log\sigma_1(g^2|B(b)|^2)$, $\sigma_{\rm H}\sigma_1(|X|^2)dX$ is Haar measure in exponential coordinates, and $\mathsf{Jb}_c$ is the relative change of the pivot derivative along the chart. The same identity holds for complex $\Upsilon$ when either side is finite with $|\Upsilon|$. Disintegrating in $W$, the fibre integral at $W=D_+$ is (F0) with $\Upsilon(V_j)=\chi_{\rm st}(V_j)\Upsilon_0(V_j)$.

*Proof.* Fix the free values $w=V_j|_{\mathfrak F}$. By Lemma F2's converse, every nonzero value of the integrand has pivots given by the chart, so the pivot-to-average map $\pi\mapsto(F_c(w,\pi))_c$ is injective on the small-curvature pivot domain. Its differential is block diagonal over $c$, each block being $n_c$, because each average uses only its own pivot (SA 8289–8290); $\det n_c>0$ at real backgrounds, since $n_c(I)=L^{-3}I_3$ and $\|n_c(V)-L^{-3}\operatorname{Ad}\|\le CL^2\epsilon$ (SA after (QC17)) keeps the determinant away from $0$ along a path from $I$. So the pivot Haar integral becomes a $dW$ integral with factor $\prod_c(\det n_c)^{-1}$, evaluated along the chart. Tonelli interchanges this with the free integral; for each $W$ substitute $w(b)=e^{igB(b)}V_W(b)$, whose Haar density is $\sigma_{\rm H}g^3\sigma_1(g^2|B(b)|^2)dB(b)$ ($\dim\mathfrak{su}(2)=3$). Writing $\det n_c$ along the chart as $e^{-\mathsf z_c(V_W)}\det(1-\mathsf{Jb}_c)$ gives (F2). All maps are Borel; Tonelli needs no finiteness. The complex case follows by applying the positive case to $|\Upsilon|$, then Fubini and linearity. The only dimension-dependent inputs are the pivot coefficient $L^{-3}$ and the count of pivots, both from SA's four-dimensional (QC16)–(QC20). ∎

So the stage's collar variables are, by construction, the chart coordinates $B\in\mathfrak{su}(2)^{\mathfrak F}$ (scaled by $g$), with the explicit density (F2). Any other coordinates used by NL1/LF1 for the same integral (Bałaban's $(A_j,B_j)$, a strip coordinate, a translated Gaussian variable) differ from $B$ by a change of variables whose properties are checked in Lemma F5 and Remark F8.

### 5.4 The actual map and its bounds

Let $V^\sharp=M_-(U^\sharp_+)$ be the test reference of ST-test, and
\[
 h_j=\max_{b\in\Gamma^{\rm rm}}\bigl|i^{-1}\operatorname{Log}(V^\sharp(b)V(b)^{-1})\bigr| ,
 \tag{F3}
\]
the localization discrepancy at the removed rows. Lemma F6 proves $h_j\le\delta'_j/8$. Put $C_A=\frac94$ and define the **full tube** as the complex polydisc
\[
 \mathcal T_j=\Bigl\{B\in(\mathfrak{su}(2)\otimes\mathbb C)^{\mathfrak F}:\ g|B(b)|<C_A\delta'_j\ \ (b\in\mathfrak F)\Bigr\},
 \tag{F4}
\]
with $|\cdot|$ the complex extension of the norm, which satisfies $|X+iY|\le|X|+|Y|$. It contains the real support of the stage test (ST-test and the triangle inequality give $g|B(b)|<\delta'_j+h_j\le\frac98\delta'_j$ there) and every point used by the conditional-mean contour estimate (Lemma F5).

**Theorem F4 (the actual collar-variable map) [proved].** Assume CH, ST-test, Lemma F6's conclusion $h_j\le\delta'_j/8$, and $\gamma$ so small that $C_A\delta'_j<c_{\rm ch}L^{-9}$ and $C'_A\delta'_j$ is below DR's source threshold $\epsilon_De^{-c_D\bar\kappa}$ (row 10). For $D_+$ in the admitted complex chart and $B\in\mathcal T_j$ put $u=gB$ and
\[
 D_{\rm old}(B;D_+)=e^{ia_V(u)}V\ \text{on }\Gamma^{\rm rm},\qquad D_{\rm old}(B;D_+)=D_+\text{'s retained values on all other rows of }M_-.
 \tag{F5}
\]
Then:

1. *(holomorphy)* $D_{\rm old}$ is holomorphic in $(B,D_+)$ on $\mathcal T_j\times$(chart), and real at real $(B,D_+)$.
2. *(fibre and retained-row identities)* $F(D_{\rm old})=D_+$ on $\Gamma^{\rm ad}$; $D_{\rm old}$ equals $V$ on every retained row; only removed rows are varied, and on free removed rows $i^{-1}\operatorname{Log}(D_{\rm old}V^{-1})=u$ exactly.
3. *(it is the actual old datum)* At real $D_+$, every point of the support of (F0) is $D_{\rm old}(B;D_+)$ for exactly one real $B\in\mathcal T_j$, and (F0) equals the $W=D_+$ fibre of (F2). So $D_{\rm old}(\cdot;D_+)$ is the actual stage map, the "shifted background" datum of CA-I 54287–54288.
4. *(the bound (70) on the full tube)* For $B\in\mathcal T_j$,
\[
 \|u\|_\infty<C_A\delta'_j;\qquad
 \|a_V(u)\|_\infty\le C_{\rm ch}L^4C_A\delta'_j;\qquad
 \|b_V(a_V(u))\|_\infty\le C'_A\delta'_j,\quad C'_A=(1+2C_vL)C_{\rm ch}L^4C_A .
 \tag{F6}
\]
5. *(boundary identities)* The source $B'=b_V(a_V(u))$ fed to DR is supported on $\Gamma^{\rm rm}$ and on the outward rows whose outer-endpoint block contains a removed row; all of its carriers lie in the double blocks of rows of the shell. If the stage system is periodic, the boundary buffer of Lemma 12 is vacuous; if it is regional, the buffer holds whenever $\Omega_0\supset(\text{shell})^{+2\xi_{j+1}+3\eta}$ (GEO, st1-r2 Theorem 14 hyp. 5).
6. *(Lemma 12 applies)* For real $B$ in the support, $D_{\rm old}$ satisfies every hypothesis placed on the actual old datum in Lemma 12, with $u$ of (68) equal to $gB$; hence the physical identification of Lemma 12 holds on the real support, and every substituted quantity of Theorem 14 continues holomorphically to $\mathcal T_j$.

*Proof.* 1. $V=M_-(\Phi(D_+))$ is holomorphic by Lemma 5 and the finite formula (5); $a_V(u)$ is holomorphic in $(u,V)$ by Lemma F2, since $\|u\|<C_A\delta'_j<c_{\rm ch}L^{-9}$; reality at real data is Lemma F2's.
2. Lemma F2 gives $q_V(a)=0$, i.e. $F(e^{ia}V)=F(V)$. Since $V=M_-(U_+)$, (67) gives $F(V)=F(M_-(U_+))=M_+(U_+)=D_+$ on $\Gamma^{\rm ad}$, the last equality because $U_+$ is the canonical background of $D_+$ (Lemma 5 at real data; at complex data by the identity theorem on the connected chart). Retained rows are not in $\Gamma^{\rm rm}$ and are set to their values; the chart changes only pivots of removed rows (SA 8279: "Only the pivot values are changed"), and $a|_{\mathfrak F}=u$.
3. Let $V_j$ be in the support of (F0). By ST-test, every free removed row has $|i^{-1}\operatorname{Log}(V_jV^{\sharp-1})|<\delta'_j$, and every removed row has logarithm relative to $V^\sharp$ below $c_{\rm ch}/4$. The bi-invariant triangle inequality and (F3) give logarithms relative to $V$ below $\delta'_j+h_j\le\frac98\delta'_j$ on free rows and below $c_{\rm ch}/4+h_j<c_{\rm ch}/2$ on all rows. The delta functions give $F(V_j)=D_+=F(V)$. Lemma F2's converse gives $V_j=e^{ia_V(u)}V$ with $u=i^{-1}\operatorname{Log}(V_jV^{-1})|_{\mathfrak F}$; put $B=u/g$, which is real with $g|B|<\frac98\delta'_j$, so $B\in\mathcal T_j$. Uniqueness: $B$ is determined by $V_j$ through the logarithm on free rows. The identification of (F0) with the fibre of (F2) is Proposition F3 with $V_W$ the canonical $M_-(\Phi(W))$ (real-analytic, hence Borel, in $W$).
4. The first bound is the definition (F4). The second is (F1). For the third, on interior rows $b_V(a)=a$; on an outward row $c$ with outer endpoint $z$, (7) gives $e^{ib(c)}=e^{ia(c)}\operatorname{Ad}(V(c))v_z(a)$, where $v_z$ is the one-step block factor formed from the interior lower-level rows of $B(z)$. Lemma 3's block-factor estimate ("Each block-factor logarithm is at most $CL|a_n|$") gives $|v_z^{\pm1}-I|\le C_vL\|a\|_\infty$ on the fixed small ball, and for small $X$ and $Y$ near $I$, $|i^{-1}\operatorname{Log}(e^{iX}Y)|\le|X|+2|Y-I|$ (log series). So $|b(c)|\le(1+2C_vL)\|a\|_\infty$. The constants $C_{\rm ch},C_v$ are fixed in row 2 and depend only on $L$; they are independent of $M,\bar\kappa$ and fixed before $\kappa$.
5. $a_V(u)$ is supported on $\Gamma^{\rm rm}$; $b_V(a)$ differs from $a$ only on outward rows whose block factor reads a changed interior row. Each such carrier is a double block of a row of the shell or of an adjacent outward row. In a periodic system there is no boundary. In a regional system the stated enlargement places every carrier at $\ell^\infty$ distance more than $2\eta$ from $\partial\Omega_0$, which is Lemma 12's buffer.
6. Lemma 12 requires: $F(D_{\rm old})=M_+(U_+)$ (item 2), agreement with $V$ on retained rows (item 2), membership in the restricted CH chart ($\|u\|<c_{\rm ch}L^{-9}$, item 4), and then defines $u$ by (68), which is $gB$ by item 2. Its response hypotheses (regularity and uniqueness balls, specification at one) hold because the source (F6) is below DR's threshold (row 10). The physical identification follows. Holomorphic continuation: every map in (75) is holomorphic in $B$ on $\mathcal T_j$ by item 1 and by DR's holomorphy in its complex source on its ball. ∎

**Lemma F5 (the conditional mean stays in the tube) [proved].** Let the stage's Gaussian be written with a conditional mean, in the form of Y3 II-114-16 (Y3 51938–51948), $\exp\{-\frac12(B-\mathbf m+\mathbf C\boldsymbol\Gamma\mathbb X,S(B-\mathbf m+\mathbf C\boldsymbol\Gamma\mathbb X))\}$, under Y3's hypotheses (Y3 51920–51933): $|m_{\rm r}(b)|\le\theta_{\mathbf m}\mathfrak b_b$, $|\mathbf m(b)-m_{\rm r}(b)|\le\varepsilon_{\mathbf m}\mathfrak b_b$, $\theta_{\mathbf m}+\varepsilon_{\mathbf m}<1$, with $m_{\rm r}$ real. Take $\mathfrak b_b=\frac98\delta'_j/g$. (a) Y3's contour estimate (Y3 51984–51996) evaluates the integrand on the tube where "$|\operatorname{Im}B(b)|<\varepsilon'\mathfrak b_b$ … and where additionally $|\operatorname{Re}B(b)|+|\operatorname{Im}B(b)|<\mathfrak b_b$ on $\mathfrak S$"; every such point lies in $\mathcal T_j$. (b) If instead the mean is removed by the translation $B=B''+\mathbf m$, with $\operatorname{Re}B$ in the real test region, every point of the translated contour lies in $\mathcal T_j$.

*Proof.* On the stage support every integrated free row carries the strict small-field test (ST-test), so Y3's failed set $\mathfrak e$ is empty and $\mathfrak S=\mathfrak F$. A failing stage makes a drop-out, which keeps its earlier stages and does not perform this substitution: SA 17419, "Drop-out (some test fails after $n\le\mathsf N_t$ stages): $X$ remains in $Z_t$ and retains … the operations carried out up to that point"; SA 17654, the drop-out retains "the bare integrals … of the levels already treated; the core; and the functions present together with the failing factor $1-\chi$". (a) On $\mathfrak S$, $g|B(b)|\le g(|\operatorname{Re}B(b)|+|\operatorname{Im}B(b)|)<g\mathfrak b_b=\frac98\delta'_j<C_A\delta'_j$. (b) $g|\operatorname{Re}B|<\frac98\delta'_j$ on the test region, and $g|\operatorname{Im}B|=g|\operatorname{Im}(\mathbf m-m_{\rm r})|\le\varepsilon_{\mathbf m}g\mathfrak b_b<\frac98\delta'_j$; so $g|B|<\frac94\delta'_j=C_A\delta'_j$. ∎

So (70) holds at every point that the conditional-mean contour estimate uses. This is the "full complex contour" of st1-r2's F.

**Lemma F6 (localization discrepancy) [proved].** Assume LOC-form, RUN-low with $r>1$, P82°/M1 in the form (15), and (22). Then for $\gamma\le\gamma_F$ (row 10),
\[
 h_j\le\tfrac18\delta'_j .
 \tag{F7}
\]
Under LOC-decay instead of LOC-form, (F7) holds with the same proof's last step.

*Proof.* By LOC-form, $V^\sharp=M_-(\Phi(D^\sharp_+))$ and $V=M_-(\Phi(D_+))$, where $D^\sharp_+$ and $D_+$ agree on every row within weighted distance $R_\sharp\ge\frac14MR_t$ of the stage carriers, and both lie in the real regular datum ball. Let $B_\Delta=B_{D_+}(D^\sharp_+)$ be the raw coordinate (6); it is supported on rows $c$ with $d(c,\text{carriers})\ge R_\sharp$ and $\|B_\Delta\|\le r_B$. Along $D_s=e^{isB_\Delta}D_+$, $0\le s\le1$, (15) bounds the derivative of the response and node gauge at a top $y$ by $C_4\sum_ce^{-\theta_4d(y,y_c)}|B_\Delta(c)|$, and AV's row bound (st1-r2 §2, "$|B(c)|\le C_Q\xi_q\sup_{D(c)}|A|$") converts this into a bound on the derivative of $i^{-1}\operatorname{Log}V_s(b)$ at a removed row $b$, with a fixed factor $C_QC$ for the read set $D(b)$ of weighted diameter at most $2$. Hence
\[
 h_j\le C_QC\,C_4\,r_B\sum_{c:\,d(c,b)\ge R_\sharp}e^{-\theta_4d(b,y_c)}
 \le C_QCC_4r_Be^{-aR_\sharp}S_4(a),\qquad a=\min(1,\theta_4/2),
\]
since $e^{-\theta_4d}\le e^{-aR_\sharp}e^{-ad}$ on the summed rows, by (22); (22)'s conditions $a\le1$ and $a\rho_0\ge16\log L$ hold since $\theta_4\ge\delta$, $\delta\le1$ and $\delta\rho_0\ge64\log L$ (row 3). The weighted distance across the localization margin is at least its $\ell^\infty$ width divided by the largest scale present, $\xi_t$, because all layers of the level-$t$ label are at most $t$; a level-$t$ cell has side $MR_t$ in level-$t$ units, so $R_\sharp\ge\frac14MR_t\ge\frac14c_N(\log\theta_t)^r$ (RUN-low, $M\ge1$). Since $r>1$, $e^{-c(\log\theta)^r}$ is smaller than every power of $\theta^{-1}$ for $\theta$ large; in particular it is below $\frac18(A_1/A_0)(\log\theta_j)^{-(p_0-p_1)}\theta_j^{-1/2}(\log\theta_j)^{p_0}/(C_QCC_4r_BS_4)$ for $\theta_j\ge\gamma^{-2}$ and $\gamma\le\gamma_F$. Here $t-j\le N_t\le C_N(\log\theta_t)^r$ and RUN's bounded frame increments give $\theta_j\le\theta_t+C_\theta N_t\le2\theta_t$ for $\theta_t\ge\gamma^{-2}$ large, so a bound in $\theta_t$ transfers to $\theta_j$. The right side is $\frac18\delta'_j$ up to the fixed normalization of $\varepsilon_j$. Under LOC-decay, $h_j\le C_{\rm loc}e^{-c_{\rm loc}R_\sharp}$ and the same last step applies. ∎

$\gamma_F$ depends on fixed constants and $A_1/A_0$ (row 9), and uses $M$ only through $M\ge1$; it is a ceiling in row 10.

**Lemma F7 (the localised test keeps history locality) [proved].** ST-test's reference is formed from data in $X^\sharp$, the $\frac14$-cell neighbourhood of $X$. If two class components of an operation do not touch, $X_1^\sharp\cap X_2=\varnothing$; so the test of one component reads no variable that the other component's stages change, and SA's locality argument applies unchanged.

*Proof.* SA 17449(i): "two regions made of level-$t$ cells that do not touch are separated by at least one cell". So $\operatorname{dist}_\infty(X_1,X_2)\ge$ one cell, and the $\frac14$-cell margin stays at distance at least $\frac34$ cell from $X_2$. A stage of $X_2$ changes determining rows only in its own shells, which lie in $X_2$. SA's "a margin beats a reach" (same line) needs the reach of each test to be less than one cell; ours is $\frac14$ cell plus the fixed ranges of bond tests, pivots and collars, which is less than one cell once $M$ exceeds a fixed floor (row 8 lower bound). ∎

**Remark F8 (main steps and the strip) [proved for the map; source size as in Lemma 13].** At a main step the removed rows are all level-$(t-1)$ rows of $\Omega_t$; those touching $\Lambda_t$ are integrated, the others are stored with strip coordinates $A'$ (SA 17518–17528). Define $D_{\rm old}$ by (F5) with $u=gB$ on integrated free rows and $u=f_H(A')$ (Lemma F1) on stored free rows. Items 1–3, 5 and 6 of Theorem F4 hold with the same proofs, holomorphy being in the integrated variables and the non-cutoff stored variables, and Borel in cutoff-zone variables, which are held fixed as near stored coordinates. Item 4 holds with $\delta'_j$ replaced by the largest removed-row threshold of the step plus $\max|H|$; by STRIP, $|H|\le C\varepsilon_{t-1}e^{-R_{t-1}}$, which is below every power of $\theta^{-1}$ by RUN-low. Lemma 13's main-step source $\delta_{\rm src}=(A_1/A_0)\varepsilon_{t-1}$ must dominate that threshold; that comparison is Lemma 13's own hypothesis and is not changed here. F as stated in st1-r2 is the stage map, which Theorem F4 supplies.

**Where F enters st1-r2.** Lemma 12's hypothesis "If the actual old datum satisfies $F(D_{\rm old})=M_+(U_+)$, agrees with $V$ on retained rows, and is in the restricted CH chart" is now a conclusion (Theorem F4 items 2–3), with $u=gB$. Outstanding F is replaced by Theorem F4, Proposition F3 and Lemmas F5–F7: (70) is (F6) with $C_A=\frac94$, $C'_A=(1+2C_vL)C_{\rm ch}L^4C_A$. Lemma 13's "Take $C_A$ to include both fixed completion and reduced-datum losses in (70)" uses these values. Theorem 14 hypothesis 3 ("The actual completed source has the FL bound") and hypothesis 5 ("the actual map (70)") are discharged by Theorem F4. The FL input of st1-r2 §2 is reduced to CH (pivot data), ST-test (our test), and LOC-form or LOC-decay.

## 6. Theorem 14 in round-3 form

**Amendments to Theorem 14.**

* Hypothesis 1: add GEO-mark, GEO-box, RUN-low, BOX (bg, id, resp), ST-test, and LOC-form or LOC-decay.
* Hypothesis 2: the actual gaps (13) are Lemma 1′ at every actual transition, resets included; "all required working cores" are lifted cores (Definition R1); the admission of the input point and of all working records is Lemma B4(ii).
* Hypothesis 3: "The actual completed source has the FL bound" is Theorem F4(4) at stages and Lemma B2 at outputs; $a_X<1/2$ is Lemma 13 (stages, main steps) and Lemma B2 (outputs).
* Hypothesis 4: unchanged in form; its "declared domain" is CI.
* Hypothesis 5: "the actual map (70)" is Theorem F4; the boundary buffer is Theorem F4(5).

The conclusions are unchanged, with Lemma 9′ in place of Lemma 9 in the first bullet's proof and Theorem F4 in the second bullet's.

**Corollary 14′ (application at every actual transition) [proved, except CI].** Assume st1-r2's declared inputs, the inputs of §0.2, and CI. Then Theorem 14 applies at every actual transition of every finite history: every main step, every preparatory stage at every stage level, and every output, including outputs at which marks are swallowed.

*Proof.* At each transition the hypotheses of Theorem 14 are supplied as listed in the amendments. Formation and chain admission of every record at every real background is Lemma B4(ii), which uses Lemmas 10, 10′, B1 (formation), 1′ (gaps), 11, 11′ (substitution and drift) and the physical relations of Lemma 12 with Theorem F4 (stages), Lemma 12 (main steps) and Lemma B3 (outputs). The source budgets are Lemma 13 and Lemma B2. The only remaining premise, the bound of the carried activities on the declared domains, is CI. ∎

This replaces the final paragraph of Theorem 14 ("If formation, FL, BOX and all reset comparisons hold … The present drafts do not establish those additional premises at Outstanding M, R, B and F").

## 7. Corrections to round 2 made in this draft

1. The deleted-mark term is removed by a ledger, not paid: Definition M1, Lemmas M2, 1′, M3. No reset comparison is needed and none is claimed.
2. (62) is false and the scalar core over $X$ is not formable from (58): Proposition R0. The core is redefined per element (Definition R1), within §1's read-record rule, and CORE, formation and the half-gap step are reproved for it (Lemmas 9′, 10′, 11′). The binding single-scalar rule is kept.
3. The BOX admission inequality is (B1), enforced through RUN-low and $\gamma$ after $M$; st1-r2's displayed BOX condition is not used. BOX's version of (71) is Lemma B2.
4. The witness/chain consumer verification is separated into the ST1-internal part (Lemma B4, proved) and the external interface CI (Outstanding).
5. The stage map is constructed (Theorem F4), its integral identity proved (Proposition F3), and (70) proved on the full conditional-mean tube (Lemma F5). The localization discrepancy between the test background and the actual background is bounded (Lemma F6) and the specified test is shown to keep history locality (Lemma F7).
6. Overlapping free variables: Lemma F2 is a single chart for the whole fibre; equations for different added rows share no pivot but may share free rows, and no product decomposition of the free variables is used anywhere (st1-r2's correction 10 is respected).

## 8. Source checks for this draft

| Source lines | Used for |
|---|---|
| SA 6111–6115 | Marks disappear when swallowed; "These geometric facts require verification for the actual operation" (so GEO-mark is a hypothesis). |
| SA 6124–6148 | (R22) coefficient; $\operatorname{Re}_\sigma(x)$ = levels of the first $\nu(C)$ stages of drop-outs; pointwise lift $L_\flat^{2e_\sigma(x)}$ multiplying layer radii, except real-potential gauge bounds. |
| SA 6150–6158 | Spaces impose "the simple, tower and small-field-core clauses with those layer radii"; inclusions are hypotheses. |
| SA 6163 | Near bonds include the nonanalytic cutoff zone. |
| SA 7601, 7614 | Strip change of variables; conditional Gaussian with mean linear in the exterior field. |
| SA 8170–8254, 8257–8296 | Pivot support, (QC15)–(QC21) linear pivot data, (QC22)–(QC24) fibre chart, its bound and converse. |
| SA 17387 | Localised minimisers' boundary effects decay as $e^{-c\delta_0\operatorname{dist}}$; $\check R\approx(\log x)^r$, $r>1$. |
| SA 17396 | On a stage's support the stored step's tests equal 1. |
| SA 17398–17407 | Stage sequences: the only lower bound on gaps is one $M$-cube; $e^{-c\check R}$ only at step-produced regions. |
| SA 17415–17440 | Three fates; drop-outs; marks persist until swallowed; "Marks wait". |
| SA 17449 | Locality: one-cell margin; window lemma; $\mathsf N_t$ non-increasing. |
| SA 17516–17531 | $\mathbf T$ on a label: strip substitution $V_j(b)=W'e^{-i\vartheta H}e^{iH}V^{\rm loc}_j(b)$, $|\mathbf H^{(j)}|\le C\varepsilon_je^{-\check R_j}$, pivot from constraint, conditional Gaussian. |
| SA 17575–17598 | Class conditions; stages; tests at $\delta'_j$ localised in $X$; box $\Lambda^{\rm pr}$ of side $\le CM$; $V''=e^{ig_kB}V_0$, single test $|B|<\delta'_k/g_k$. |
| SA 17610–17630 | Drop-out repetition; $C(M)$ fixed before $\gamma$; localised stage backgrounds $U^{(n)}_{k,X}$; shell relaxations and $k_\sharp$; $\delta'_j/\varepsilon_j$; $\mathsf N_k$ taken large. |
| SA 17654–17656 | What a drop-out retains; Proposition 2.4 ($C(M)$, $|\partial V_\Lambda-\mathbf 1|\le C(M)\varepsilon$, $J(U_0)=0$ in $\Lambda^{\rm pr}$). |
| CA-I 48527–48573 | Four gauge families and printed exponents $e(Q)$. |
| CA-I 53776–53802, 53880–53890 | Prepared sequence; $Z''_k=(\Omega^{\sim5}_{k_0+1})^c\cap Z$; $\Lambda=(\Omega^{\sim4}_{k_0+1})^c\cap Z\subset\Omega^c_{k_0+1}\cap Z$; one-layer separation. |
| CA-I 54246, 54287–54288 | Thresholds $\delta_j,\delta'_j$; "Express $U^{(n)}_k$ through the new background $U^{(n+1)}_k$ and the fluctuation $(A_j,B_j)$ on the collar $R_n$". |
| Y3 46104–46233 | Free coordinates, completion, reference measure (3D template). |
| Y3 46258–46387 | Regional fibre chart and measure identity II-26-53/55 (template for Lemma F2, Proposition F3). |
| Y3 46408–46559 | Strip zones; strip bond map II-26-71 (ported as Lemma F1). |
| Y3 51852–52014 | Gaussian structure with conditional mean; contour tube and estimate II-117-69 (used in Lemma F5). |

The 3D line numbers are templates; each 4D statement above is proved here, and the only dimension-dependent quantities (pivot coefficient $L^{-3}$, $\dim\mathfrak{su}(2)=3$, six-plaquette stars, four-coordinate counts) are taken from SA's four-dimensional text or from st1-r2.

## Result

Of the four repairs named by `st1-r2.md`:

* **M is proved.** A permanent mark ledger (Definition M1) makes every coefficient monotone along the history. SA's own "marks wait" statement and the monotone waiting depth show that ledger levels never repeat at a point (Lemma M2), so $c_{\min}$ and the drops (18) survive every reset (Lemma 1′), and the ledger only shrinks domains (Lemma M3).
* **R is proved,** as a counterexample plus a repair. (62) is false, and the scalar-infimum core is not admitted by the tests at arbitrary addresses (Proposition R0). Per-element lifted cores satisfy CORE, formation, the half-gap step and drift with constants fixed before $\kappa$ (Lemmas 9′, 10′, 11′), because the smoothed lift varies at exactly the rate $\delta_T$ that the maximum-type tower bound (49) tolerates.
* **B is proved inside ST1.** Output admission is (B1), enforced by RUN-low with $\gamma$ after $M$ (Lemma B1); BOX's source budget and drift relation are Lemmas B2–B3; all ST1-internal consumers of the enlarged witness radii and of the chain reads are verified (Lemma B4). **The external consumer interface CI is Outstanding** (§4.3): NL1/LF1 must bound their activities on the ST1 domains. Three attacks (raw-lift inclusion; family-by-family comparison with CA-I's printed exponents; rescaling or faster smoothing) fail for the reasons recorded: PROF's fixed decay rate against a polylogarithmic lift, a single $M$-cube of stage separation with $M$ fixed before $\gamma$, and $\alpha_0$ fixed before $\kappa$.
* **F is proved.** The stage integral is an integral over the chart coordinates (Proposition F3). The actual collar-variable map is constructed (Theorem F4) with the fibre, retained-row and boundary identities, and (70) holds on the full conditional-mean tube with $C_A=\frac94$, $C'_A=(1+2C_vL)C_{\rm ch}L^4C_A$ (Theorem F4, Lemma F5). The localization discrepancy is at most $\delta'_j/8$ (Lemma F6), and the specified test keeps history locality (Lemma F7).

New inputs: GEO-mark, GEO-box, RUN-low, BOX (bg, id, resp), ST-test, and LOC-form or LOC-decay. Each is quoted from SA or CA-I, or is a specification of our own construction (ST-test). Every new constant is fixed before $\kappa$ and is independent of $M$ and $\bar\kappa$, except $C(M)$, which enters only ceilings on $\gamma$. This is research text and grants no status. It has not been distilled or refereed.
