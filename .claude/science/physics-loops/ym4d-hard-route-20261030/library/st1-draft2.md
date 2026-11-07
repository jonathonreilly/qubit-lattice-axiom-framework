# ST1, round 2: intrinsic stage domains and stage admission (D4)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, round-2 long draft of submanuscript ST1. It replaces `st1-draft.md` (round 1) and builds on the Codex distil `st1.md` (511 lines), whose statement, definitions, corrections and Outstanding list are the base. It also uses `os-draft.md` (repairs D1, D2 and the dissolution of Lemma OS) and `shift-map.md`. Research text. It is not an audit and grants no status. No other model has read it. Codex distils it next; a fresh session then referees it.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline `YM4_sketch_500.tex` ("SA"), the complete account `theorem_0_complete_account_raw_I.tex` ("CA-I") and the three-dimensional manuscript `YM3/YM3_I.tex` ("YM3"), all at commit `31a47c543775`: the graded domains, the ambient towers, the response substitution, the re-expansion, the stage tests and the four-dimensional statements of the background theorems. Tadeusz Balaban for the background-field method, the operation **R**, its stages, collars, lifts and thresholds (CMP 98, 99, 102, 109, 119, 122). Jonathan Dimock for his expositions of Balaban's renormalization group (arXiv 1108.1335, 1212.5562, 1304.0705), the readable model of background re-expansion. The library notes cited below are by Codex and Claude; each credits its own sources.

Line numbers. "SA L" is a line of `scratchpad/sa/ym4.tex`, "CA-I L" of `scratchpad/sa/ca_I.tex`, "YM3 L" of `scratchpad/sa/YM3_I.tex`. Library notes are cited as `note.md:line` or `note.md (eq)`. I read in this session every source range I cite, in bounded ranges; where I take a line from a library note I say so.

Status words. **[proved here]**: written in full here, by hand. **[port]**: proved here by following the cited YM3 proof, with every four-dimensional change stated where it enters. **[import X]**: a named hypothesis, stated in Section 3 with its source and status. **[design]**: a definition or a choice that is ours; it needs no proof, but it can change a consumer (Section 14 lists the changes). **[Outstanding]**: not proved.

No step uses a computer. Every argument is a finite chain of inequalities, power-series estimates and set inclusions, of the kind that can be formalised in Lean.

---

## 0. Summary

**The six Outstanding items of the distil, after this draft.**

| Item | Result here | Where |
|---|---|---|
| (a) (T) in four dimensions | **proved** as an implication from the four-dimensional Theorem 4 of SA (SA L9734-9740), proved conditionally in `a3-derivative.md` §§6-7, the averaging import and the profile import. The second-order member, the pillar gauge factor and the row sum are each stated and proved in four dimensions. | Theorem T, Lemmas PG, LV, RS (Section 7) |
| (b) gauge theorem on the remade cube families | **proved** as an implication from the four-dimensional cube gauge G99.F (`a1-balaban.md` §3.2) and the stage tests, for all four CA-I families (CA-I L48527-48565), the large and core cubes, and YM3's containing-cube clause (YM3 L53362-53367). | Theorem G, Proposition 5′ (Section 8) |
| (c) preparatory reconstruction | **proved** on the physical locus: the new datum is a local function of the old one, $M_+=F\circ M_-$ (Lemma DM); the actual old collar datum is $e^{ia_V(u)}V$ with $V=M_-(U_+)$ in the pivot chart SA L8289-8296, for a unique free coordinate $u$ (Lemma FC); every parametrisation of the stage fibre, Balaban's $(A_j,B_j)$ included, factors through $u$ (Corollary FC′); every stored site is either a top or a site of a pinnable top (Lemma ST). Theorem D4 then identifies the composition with the old read, under CRIT, BG and LEV. | Section 11 |
| (d) source level and no-new-mark margin | **proved** with repair D1 (a stage-graded term in the coefficient), using SA's own exponent condition $\mathfrak p_0-\mathfrak p_1>r$ (SA L17630) and the running-minimum waiting depth (SA L19410). The distil's (12) is used; the old (N-growth) is not. | Theorem S (Section 10) |
| (e) changing reads and full-radius gaps | **proved** by a change of design: every read keeps its own function (its own structure's sequence, units, radius index and lift); the domain of a structure imposes the reads of every structure between the record and itself. Real admission of the earlier reads at a later background is proved by summing the physical increments of the intervening transitions (Proposition DR). No comparison between reads of different radii remains, so the distil's truncated-radius objection does not arise. | Section 9 |
| (f) application of ST1* | **proved**: hypotheses 1-5 hold at every main step and every preparatory stage, as implications from the imports of Section 3; hypothesis 6 is the consumer interface to NL1/LF1 and is stated as such. | Section 13 |

**Checks of the round-1 repairs.** D1 (`os-draft.md` §7.2) holds and is used, with its count of stages per level replaced by the running-minimum count (Lemma 2(iv)); its proof of (AMP-st) used (N-growth) and a flow bound, both of which the distil rejects, and is replaced by Theorem S. D2 (`os-draft.md` §7.4) identifies a real factor $L^2/L_\flat^2$ between the stage tests and the layer radius on integrated collars. That factor is a fixed constant of $L$. It is absorbed by the floor $\alpha_0\ge4C_{\rm RA}/c_{\min}$, $C_{\rm RA}=12C_PC_{\rm sm}L^4$ (Proposition RA), so the radius index stays the layer (the distil's convention). What must change is the lift: the distil's $e=m-m^{\rm orig}$ can be as large as the waiting depth and then breaks the absolute radius ceilings; Definition RA caps it by the shell exponent of SA L17624, and Definition 2 smooths it at the decay rate of the profile bound, so that the current can be admitted next to lifted points. Section 14 records both decisions.

**Lemma OS.** It dissolves: every stage sequence is separated by one $M$-cube of the later level (Theorem OS′, from CA-I L53779-53830 and SA L17398-17407; `os-draft.md` Lemma 2.3, rechecked here, with the case across $\partial Z$ proved).

**What remains open.** Nothing internal to ST1. The theorem is an implication from the imports of Section 3. Of these, the four-dimensional forms of CRIT, LEV and the outer-core substitution in CORE remain open, as in the distil; Theorem 4 of SA rests on the inputs P81, P82° and M1 of `a3-derivative.md` §12; and Section 3 names the new import statements this draft needs (AV-it, AX, GEO-Mon, GEO-st, GEO-lift, RUN1, BOX). Section 15 lists them, hardest first.

**Constants.** Every constant introduced here is fixed before $\kappa$, independent of $M$ and $\bar\kappa$; $M$ enters only through lower bounds (Section 4, table). One exception is named and isolated: the box constant $C(M)$ of SA L17612. It belongs to the core operation, it enters ST1 only through the transition from the last stage to the output, and there only through a ceiling on $\gamma$ (SA L17627).

---

## 1. Main statements

**Theorem 1 (ST1*, conditional admission and re-expansion).** [proved here, as an implication] Fix a finite four-dimensional periodic lattice, a finite history, its formation records, and constants chosen in the order of Section 4. Assume the imports of Section 3, with all their stated domains, and the following **application hypotheses**, for every transition and every inherited read, uniformly in the cutoff, volume, history length, earlier parameters, stored tiers and switches.

1. The actual real background has the real admission bounds of Propositions 5′ and DR. Every real and complex tower datum, before and after substitution, satisfies the averaging hypotheses and the half-tube bound of Lemma 4.
2. Each transition has the compatible read data and positive gaps of Definition 4.
3. Every input belongs to the pair, source-cube and pivot domains of DR and AV; every pinned input belongs to LEV's triple domain, including its turning-cell gauges. Each tower read has the ambient Lipschitz estimate (T). The constants $K_{\rm pt},K_{\rm tw},K_{\rm core}$ of Proposition 6 are uniform.
4. The regional shift, and when used its pinned version, satisfy (S) and the endpoint-pillar bounds of Definition 5, on the whole complex parameter domain, and $a_X<1/2$ in (12).
5. On the physical locus, $M_+=F\circ M_-$ locally; the source changes $M_-(U_+)$ into the actual old datum, pivot and return factors included; the constraints and regularity satisfy CRIT; pinned levelling preserves the stored transports as in LEV.
6. NL1 and LF1 supply their activities on these domains, with the properties of Definition 3, and restriction preserves them.

Then every carried composition is defined and holomorphic on each fixed-real-factor fibre for
\[
 s\in\mathbb D(Y),\qquad |\lambda|<\varrho_X=(2a_X)^{-1}>1
 \tag{1}
\]
($\varrho_X=\infty$ if $a_X=0$). Every scalar read keeps at least half its target coefficient gap; core reads lie in the midpoint-radius cores; real gauge witnesses remain valid; stored coordinates stay in their formation tiers; every tower datum has distance at least $\delta_B/8$ from the complement of its intrinsic tube; the actual real background lies in the half-radius domain. For an activity $f$ with formation bound $b_f$,
\[
 |V_f(Y)|\le {2b_f\over\varrho_X}(e^{\bar\kappa}-1)^{-|Y\setminus X^\uparrow|}
 \le{2b_f\over\varrho_X}e^{-(\bar\kappa-1)|Y\setminus X^\uparrow|},
 \tag{2}
\]
and the finite sum of the $V_f(Y)$ is the substituted value minus the unshifted value. On the physical locus the substituted value is the old read. Finite composition gives (D4).

*Proof.* As in the distil (`st1.md:37`): Proposition 5′ gives real admission, Lemma 4 tube room, Proposition 6 inclusion with half the gap, Definition 5 and (1) put the unpinned and pinned shifts inside Proposition 6's bounds, Proposition 7 identifies the real evaluations, and Lemma 8 gives (2) and the resummation. Apply these to the finite ordered transitions, keeping each formation record and its parameter domain. Each inclusion holds for every value of the earlier parameters, so it holds inside the next composition. ∎

**Theorem 2 (application).** [proved here, as an implication] Under the imports of Section 3 and the constants of Section 4, hypotheses 1-5 of Theorem 1 hold at every main step and at every preparatory stage of every finite admissible history, at every stage level, with overlapping collars or not. Hypothesis 6 is the statement that NL1 and LF1 must prove; the domains it refers to are the finite intersections of Definition 2. Hence Theorem 1 applies, and (D4) holds, conditional on hypothesis 6.

The proof is Section 13. It uses Theorem OS′ (Section 6), Theorem T (Section 7), Proposition RA, Theorem G and Proposition 5′ (Section 8), Lemma CR, Proposition 6 and Proposition DR (Section 9), Theorem S (Section 10), and Theorem D4 (Section 11).

The transition from phase $\mathsf N_t$ to the output of an operation is covered by Theorem 2 for its read compatibility and its coefficient gap (Lemma CR, Lemma 2(ii)). Its source is the box of the core operation; its source budget is the import BOX, a statement of the core operation and not of a stage (Section 3).

---

## 2. Definitions

The distil's Definitions 1-6 (`st1.md:45-198`) are kept, with four changes, each marked **[design, round 2]**: the lift (Definition RA), the stage-graded coefficient (in Definition 2), the chain of reads in the domain (Definition 2, (L1)-(L4)), and per-record witness families (L2). Everything not restated below is as in the distil.

**Definition 1 (fields, units and geometry).** As `st1.md:45-78`, verbatim in content: finite periodic four-dimensional lattice; real configurations in $SU(2)$, complex in $SL(2,\mathbb C)$; operator norm; complete bond star of **six** plaquettes; regional action; current (3); plain triples; meshes $\eta_j=L^{-j}$, $\xi_l=L^l\eta$; layers $m(x)=\max\{l:x\in\Omega_l\}$, $l(x)=\xi_{m(x)}$; $\rho$-separation $\operatorname{dist}_\infty(\Omega_{l+1},\Omega_l^c)\ge\rho\xi_l$; weighted distance with density $l(x)^{-1}$; subordinate sequences and meets; $\operatorname{Bd},\operatorname{Bd}^\circ$; localization partitions, $X^\uparrow$, $Z^{\wr p}$; determining rows $\Gamma_l$, $\mathbf B$, $M_{\mathbf B}$; criticality over a datum; nodes, residual gauges, pillars; gauge action $U^v(b)=v(b_-)U(b)v(b_+)^{-1}$; the covariant difference (4) with its mesh denominator; and the change of units (5),
\[
 \rho_X^{u\to v}(U,A',\mathbf J)=(U,L^{-(u-v)}A',L^{-3(u-v)}\mathbf J)|_X .
 \tag{5}
\]

**Definition 2 (structures, coefficients, lifts and domains).**

*Structures.* As `st1.md:80`: a history is a finite ordered list of transitions and formation records supplied by GEO; structures $\sigma=(\mathcal S,\boldsymbol\nu;t,\phi)$; at operation level $t$, $\mathsf N_t\ge1$, $t_\flat:=t-\mathsf N_t\ge0$, and stage $n+1$ ($0\le n\le\mathsf N_t-1$) has stage level
\[
 j_n=t-\mathsf N_t+n,
\]
collar $R_n=Z_{j_n+1}\setminus Z''_{j_n+1}$ (CA-I L53806-53810). The determining sequence uses the completed counts $\boldsymbol\nu$ (SA (R21), SA L6097-6110). The precedence $\preccurlyeq$ is that of SA L6119-6121.

*Coefficient.* With $\varpi_{\rm in}=1$, $\varpi_n=1-n/(2\mathsf N_t)$, $\varpi_{\rm out}=0$, the SA coefficient is (R22) (SA L6124-6135):
\[
 c_\sigma(x|m)=1-\beta_s+\beta_s2^{-(t-m)}+\varpi_\phi g_t(m)
                -\beta_R\sum_{l\in\mathrm{Re}_\sigma(x)}2^{-|m-l|},
 \tag{6}
\]
$g_t(m)=\theta_s\beta_s2^{-(t-m)}$ for $m<t$, $g_t(t)=\beta_s$, $\mathrm{Re}_\sigma(x)$ a **set** of completed marked levels. **[design, round 2; repair D1 of `os-draft.md` Definition 7.2, with a new count]** Let $\mathsf N(\cdot)$ be the waiting-depth function, so that $\mathsf N_t=\mathsf N(\underline\theta_t)$, $\underline\theta_t=\min_{i\le t}\theta_i$ (SA L19410; import RUN). For a level $u$ put
\[
 \bar N(u):=\mathsf N(\theta_u)\ge1,\qquad \kappa(u):={\beta_s\over8\bar N(u)} .
 \tag{6a}
\]
For a structure $\sigma$ of level $t$ and phase $\phi$, let $\mathrm{St}(\sigma)$ be the set of stages completed before $\sigma$: all stages $(t',n')$ of operations at levels $t'<t$, and the stages $(t,n')$ with $n'<n$ if $\phi$ is the phase after $n$ stages ($n'<\mathsf N_t$ if $\phi={\rm out}$; none if $\phi={\rm in}$). Put
\[
 c^\natural_\sigma(x|m):=c_\sigma(x|m)-K_\sigma(m),\qquad
 K_\sigma(m):=\sum_{(t',n')\in\mathrm{St}(\sigma)}\kappa(j_{t',n'})2^{-|m-j_{t',n'}|},
 \tag{6b}
\]
$j_{t',n'}=t'-\mathsf N_{t'}+n'$. The term $K_\sigma$ depends only on the level, the phase and the frame; it is the same at every site. All radii below use $c^\natural$; I write $c$ for $c^\natural$ from now on.

*Radius index and lift.* **[design, round 2]** The radius index is the layer, $m=m_\sigma(x)$, as in the distil. Each structure carries a **raw lift exponent** $\mathcal E_\sigma(x)\ge0$ (formation data; Definition RA inside operations, GEO-lift elsewhere), in place of the distil's $e=m-m^{\rm orig}$. The lift is its smoothing at the rate $\delta/4$ of step 2 of Section 4:
\[
 \lambda_\sigma(x):=\max_\tau L_\flat^{2\mathcal E_\sigma(\tau)}e^{-(\delta/4)d_\sigma(x,\tau)} .
 \tag{6d}
\]
It has three properties, each immediate from (6d) and the triangle inequality: $\lambda_\sigma\ge L_\flat^{2\mathcal E_\sigma}\ge1$; $\lambda_\sigma(\tau)\le e^{(\delta/4)d_\sigma(x,\tau)}\lambda_\sigma(x)$; and $\lambda_\sigma\le\max L_\flat^{2\mathcal E_\sigma}$. The first gives real admission of curvature from the tests, the second of the current from the profile bound (Proposition RA), the third the absolute ceilings.

**Definition RA (the raw stage lift).** [design, round 2; the exponents are those of SA L17624, shifted by one] Inside the component of an operation, from its first stage until the next main step, $\mathcal E_\sigma$ is given by the rule below. At every other structure and point, $\mathcal E_\sigma$ is the formation datum supplied by GEO-lift (GL1), equal to $0$ where no relaxed test is in force. Fix an operation at level $t$ acting on a class component $Z$ (CA-I L53747-53753), with $k_\sharp$ defined by $M\check R_{k_\sharp+1}L^{k_\sharp+1-t}=M$ (SA L17624; this is CA-I's $k_0$, CA-I L53765-53771). For a level $j$ and a point $x\in Z$ of **original** layer $l(x)$ (its layer in the label at the start of the operation), let $e_j(x)$ be SA's exponent:
\[
 e_j(x)=\begin{cases}0,&j\le k_\sharp,\\
 (j-l(x)-1)_+,&j>k_\sharp,\ k_\sharp<l(x)\le j,\\
 j-k_\sharp-1,&j>k_\sharp,\ l(x)\le k_\sharp .\end{cases}
\]
At the stage $n+1$, with stage level $j=j_n$, put on the **raised set**
\[
 C^{(n+1)}:=(Z\setminus Z''_{j+1})\setminus\Omega_{j+1}
\]
(the points of $Z$ whose layer is $j+1$ after the stage and was at most $j$ in the label) $\mathcal E(x)=e_j(x)+1$, and inherit $\mathcal E$ elsewhere. Thus a point keeps the value set at the last stage that raised it; the points of the shells $Z''_{i+1}\setminus Z''_i$ keep the value of the stage at level $i-1$, or their inherited value if their original layer is $i$. At the output of the operation (after the box), every point of a healed component $Z$ lies in the top member $\Omega_t$ of the new sequence (import GEO-Mon); put there $\mathcal E(x)=e_{t-1}(x)+1$ if $x$ is not in the label region $\Omega_t$, and inherit $\mathcal E$ otherwise. A drop-out after $n$ stages keeps the values after $n$ stages (SA L6088).

Since $e_j\le j-k_\sharp-1$ for $j>k_\sharp$ and $e_j=0$ for $j\le k_\sharp$, every value set by an operation at level $t$ is at most $t-k_\sharp-1=\mathsf N^0_t-1$, where $\mathsf N^0_t=t-k_\sharp$ is the number of top levels (CA-I L53765-53774). Hence, inside an operation at level $t$,
\[
 L_\flat^{2\mathcal E_\sigma}\le L_\flat^{2(\mathsf N^0_t-1)}\le L^{2(\mathsf N^0_t-1)}=R_{k_0+1}^2 ,
 \tag{6c}
\]
by CA-I L53769. Import GEO-lift (GL2) turns (6c), and the formation data outside operations, into a polynomial bound in $\log\theta$.

*Radii.* The formation table is $r_\iota(m)=\alpha_\iota\varepsilon_m$, $\alpha_0\le\alpha_1$ (distil's simplified design, `st1.md:92`, with SA's level-zero and unfinished-top conventions SA L6146-6148 kept as a separate table entry). Put
\[
 R^{p,\iota}_\sigma(x)=c_\sigma(x|m)\lambda_\sigma(x)r_\iota(m)L^{-pm},\qquad m=m_\sigma(x).
\]
A triple $P=(U,A',\mathbf J)$ has $U$ real and pair $\mathbf p(P)=(\mathbf U,\mathbf J)$, $\mathbf U=e^{i\eta A'}U$; one splitting serves every record.

*The domain.* **[design, round 2: chain reads]** For $\sigma'\preccurlyeq\sigma$, let $\mathrm{Ch}(\sigma'|\sigma)$ be the finite set of structures $\sigma^\circ$ of the history with $\sigma'\preccurlyeq\sigma^\circ\preccurlyeq\sigma$. The domain $\widetilde U_{\sigma'|\sigma}(Y)$ is the finite intersection, over all $\sigma^\circ\in\mathrm{Ch}(\sigma'|\sigma)$, of the following clauses, all strict. In every clause the **function read and its base radius belong to $\sigma^\circ$**; only the coefficient belongs to $\sigma$.

- **(L0) absolute real clause.** On $\operatorname{Bd}_{\mathcal S}(Y)$: $L^{2m_{\sigma^\circ}(x)}|\partial U-I|<a_T/4$. This is a clause on the real factor alone.
- **(L1) simple reads.** On $\operatorname{Bd}_{\mathcal S}(Y)$, with $m=m_{\sigma^\circ}(x)$, $\lambda=\lambda_{\sigma^\circ}(x)$:
 $|\partial U-I|,|\partial\mathbf U-I|<c_\sigma(x|m)\lambda r_0(m)L^{-2m}$, $\eta^3|\mathbf J|<c_\sigma(x|m)\lambda r_0(m)L^{-3m}$, $\eta|A'|<c_\sigma(x|m)\lambda r_1(m)L^{-m}$, $\eta^2|\nabla^UA'|<c_\sigma(x|m)\lambda r_1(m)L^{-2m}$.
- **(L2) witnesses, per record.** For each $\sigma''\preccurlyeq\sigma'$ and each cube $Q$ of a witness family **recorded by $\sigma''$** (the large cubes $Q\subset Y\cap\Omega^{\sigma''}_l$ of side $\le\mathsf oLM$ in level-$l$ units; the four CA-I families with their lift exponents, CA-I L48527-48565, as in `st1.md:114`; the core cubes of side $\le C_{\rm box}LM$; and the natural cubes of side $\le12\mathfrak M$ of YM3 L53362-53367), $U$ has a real gauge $U^v=e^{i\eta_lA}$ on the inner bonds of $Q$ with the bound recorded by $\sigma''$: $|A|,|\nabla^{\eta_l}A|<\mathsf g_Q\Lambda_Q\alpha_0\varepsilon_l$, where $\mathsf g_Q$ is the family's gauge factor ($\mathsf oLMB^{cg}$ for large cubes, $BM$ for the CA-I families, $C_{\rm pot}M$ for core cubes) and $\Lambda_Q$ is the maximum of $\lambda_{\sigma''}$ over the side-$(s+6)$ enlargement of $Q$, recorded with the cube; and, for each natural cube $q$, a containing cube $q\subset q'\subset Y_{\mathcal S}$ with a real gauge of index $l$ at most $a_\flat$. (For the CA-I families this replaces the printed bound $\mathsf L_0^{2e(Q)}BM\alpha_{0,m}$, Section 8.3.)
- **(L3) tower reads.** At each tower address $(\sigma'',i,Z,\mathfrak r)$ with $\sigma''\preccurlyeq\sigma'$, the tower of the meet $(\Omega^{\sigma^\circ}_l\cap\Omega^{\mathfrak r}_l(Z))_{l\le q}$ exists, and at settled elements on $Z^{\wr p}$, with $\ell=\min\{m_{\sigma^\circ}(x),i\}$ and $\lambda=\lambda_{\sigma^\circ}(x)$,
 \[
 |\partial T_q-I|<L^{i-p}c_\sigma(x|\ell)\lambda r_0(\ell)L^{-2\ell},\quad
 \eta_q^3|J_q(T_q)|<L^{i-p}c_\sigma(x|\ell)\lambda r_0(\ell)L^{-2\ell-\min(q,\ell)},
 \tag{7}
 \]
 for both erosion rules, $1\le q\le p\le i$, with complete stencils, and the same with $\mathbf U$ replaced by $U$.
- **(L4) cores.** At each core address $(\sigma'',i,X')$, $X'\subset Y\cap\Lambda_i$, $\rho_{X'}P\in\mathcal U^\circ_i(X';b_0,b_1)$ with $b_\iota=c_\sigma(i)\lambda_{\sigma^\circ}r_\iota(i)$ (infimum of $\lambda$ over the read set, so that a core radius is constant on its address), in the sense of `st1.md:110` (SA (R4)-(R6)).

The half-radius domain halves every base radius, every witness bound, $a_\flat$ and $a_T$, with $c$ unchanged. The real factor of a general domain point is **not** assumed critical.

*Why chain reads.* The distil's tower clause used the current sequence $\Omega^\sigma$; enlarging a determining member then changed the function read (`st1.md:460`). In (L1)-(L4) each read is a function fixed by its own structure $\sigma^\circ$. When the current structure moves from $\sigma^-$ to $\sigma^+$, every read imposed by the target $\widetilde U_{\sigma'|\sigma^-}$ is imposed by the input $\widetilde U_{\sigma'|\sigma^+}$ as the **same function with the same base radius**, since $\mathrm{Ch}(\sigma'|\sigma^-)\subset\mathrm{Ch}(\sigma'|\sigma^+)$; only the coefficient changes, from $c_{\sigma^-}$ to $c_{\sigma^+}$. This is Definition 4's compatibility, by construction. The price is that real admission must now hold for the reads of every $\sigma^\circ$ in the chain at the current background; Proposition DR supplies it.

**Definition 3 (substitution, activities and physical locus).** As `st1.md:116-128`: $P\dotplus h=(U,A'',\mathbf J+K)$, $A''=(i\eta)^{-1}\log(e^{i\eta H}e^{i\eta A'})$ on the active bonds, unchanged elsewhere; carried activities are bounded, holomorphic on fixed-$U$ fibres, Borel in $U$ and near stored variables, analytic in far stored variables and switches, invariant under simultaneous real gauges of pair and stored variables; real ties versus pair functions; stored slots with bond, initial site, formation level, range and near/far class (SA L6160-6173); the physical locus ($U$ real, $s=\mathbf1$, $\lambda=1$, physical current with the plain-current boundary convention).

**Definition 4 (compatible read data and room).** As `st1.md:130-141`, with $c^+_a=c_{\sigma^+}$, $c^-_a=c_{\sigma^-}$ at the read's index, base radius $R_a$ of the read's own structure, $\Delta_a=(c^-_a-c^+_a)R_a$, $b^{\rm mid}_a=(c^-_a+c^+_a)R_a/2$. By Definition 2 every target read is the same function as an input read with the same base radius; every target witness requirement is imposed at the input with the same bound; every target core is imposed at the input at $(1-\tau_a)b^{\rm mid}$ by the coefficient arithmetic of Lemma 2.

The shift norm is the distil's (10) with the layer scale $l(b)$ of the **input** structure:
\[
 \|h\|_w=\max_b{\max\{l(b)|H(b)|,\ l(b)^2|\nabla^UH|(b),\ l(b)^3|K(b)|\}\over w(b)} ,
 \tag{10}
\]
all stencil neighbours included. The profiles are
\[
 w(m)=\tfrac12d_*(m)\alpha_0\varepsilon_m,\qquad
 d_*(m)=\begin{cases}(1-\theta_s)\beta_s2^{-(t-m)},&\text{main step }(t-1,{\rm out})\to(t,{\rm in}),\\
 \kappa(j)2^{-|m-j|},&\text{stage }(t,n)\to(t,n+1),\ j=j_n,\\
 \tfrac12\theta_s\beta_s2^{-(t-m)}\ (m\le t),&(t,\mathsf N_t)\to(t,{\rm out}).\end{cases}
 \tag{11}
\]
For the stage line this is D1's profile; for the main step it is the distil's.

**Definition 5 (regional response and interpolation radius).** As `st1.md:157-192`: source $\mathcal S_v$ (the changed rows with their averaging carriers); pivot completion; the regional shift (DR at the restricted input pair and source, in one system of units); hypothesis (S),
\[
 \mathfrak n(h_Y)(b)\le C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{\rm src}e^{-\mu d(b,\mathcal S_v)},
 \tag{S}
\]
where I separate from the distil's $C_{\rm src}$ the factor $E_{\bar\kappa}\ge1$ that the complex decoupling polydisc costs (Section 3, DR); pinned bound with $C_{\rm lev}$; $Q_X$, $E_X$; and
\[
 a_X=C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{\rm src}
     \max\Bigl\{{C_{\rm lev}Q_X\over r_*},{K_{\rm pin}E_X\over\epsilon_{\rm lev}}\Bigr\}.
 \tag{12}
\]
Localized compositions (13), Boolean brackets (14), $V_f(Y)$, regional consistency and component locality as in the distil.

**Definition 6 (thresholds and auxiliary constants).** As `st1.md:194-198`, with: $\delta_l=(A_1/A_0)\varepsilon_l$ at a main step and $\delta'_l=(A_1/A_0)(\log\theta_l)^{-(\mathfrak p_0-\mathfrak p_1)}\varepsilon_l$ at a stage (SA L17624); $\delta_{\rm src}$ is the threshold at the **actual** source level; pillars, tops, pinnability, read sets and levelling as in `st1.md:198` (YM3 L54646-54709).

---

## 3. Imports

All imports are hypotheses. A source label or a three-dimensional proof supplies no four-dimensional verification. The distil's list (`st1.md:200-242`) is kept; items marked **new** are statements this draft needs and states precisely for the first time. "Status" reports the library's status, not a status granted here.

- **GEO (LF1).** As `st1.md:204`: nested regions, separated label sequences, the two erosion assignments, torus floors, row and carrier geometry, persistence of records, disjoint standing waiting windows (SA L6111-6113). In addition:
  - **GEO-prep** (the prepared sequence): the facts of CA-I Definition 4.18, CA-I L53737-53830, read in this session: $Z''_i$ for $i\in I_M=\{k_0+1,\dots,k\}$ is a union of level-$i$ $M$-cubes, and $Z''_i$, $Z''_{i-1}$ are "separated by one layer" of level-$i$ $M$-cubes (L53779-53782); $Z''_i=(\Omega_i^{\sim5})^c\cap Z$ for $h<i\le k_0$ (L53783); $Z''_i=Z_i$ for $i\le h$ (L53784); $Z''_1\subset\cdots\subset Z''_k\subset\Lambda\subset Z$, $Z''_{h+1}\supset Z_h$ (L53794-53795); $\Lambda\subset\Omega^c_{k_0+1}\cap Z$ and $\{x\in Z:\operatorname{dist}_\infty(x,Z''_k)<M\}\subset\Lambda$ (L53800-53803); $Z_t\supset(Z_{t-1})^{+10a_t}$ and $\Omega_t^c\supset(Z_{t-1})^{+5La_t}$ (L53823-53829); $Z''_l\subset\Omega_l^c\cap Z$ (SA L17415, as quoted in `os-draft.md:56`). The "layers" of $S^{\sim\ell}$ have width at most one cell of their level; `os-draft.md:100` flags this reading, and either reading gives the bounds used below.
  - **GEO-Mon (new).** Along the precedence order of one history, determining sequences increase memberwise: $\sigma^-\preccurlyeq\sigma^+$ implies $\Omega^{\sigma^-}_q\subset\Omega^{\sigma^+}_q$ for every $q$ up to the depth of $\sigma^-$. At a stage only the member of level $j+1$ changes (CA-I L53812-53814; `shift-map.md:30-35`); at a main step a new top member is added; at the output of an operation the healed component lies in the new top member $\Omega_t$ (SA L6086-6087, "a healed component leaves the label"; SA L9776, "healed sequences"). A drop-out keeps its stages (SA L6088).
  - **GEO-st (new; YM3 Lemma II-84-18, YM3 L55202-55260, is the model).** A stored slot of level $l$ that is not yet integrated at a structure $\sigma$ has its initial site $x$ outside $\Lambda_{l+1}$ and at $\infty$-distance more than $2\xi_{l+1}+2\eta$ from the member $\Omega^\sigma_{l+2}$; it is integrated by the stage at level $l$ of the operation acting on its component, if that stage occurs, and then disappears.
  - **GEO-lift (new).** (GL1) At every structure and point outside the rule of Definition RA, the formation data supply a raw exponent $\mathcal E_\sigma\ge0$ such that every test in force bounds its datum loops by $2L_\flat^{2\mathcal E_\sigma}\varepsilon$ at their level, and the background by $3L_\flat^{2\mathcal E_\sigma}\varepsilon_m\eta_m^2$ (the layer-radius formation data of SA L6141-6148 are the source of these exponents; drop-outs keep the values of their stages, SA L6088). (GL2) $L_\flat^{2\mathcal E_\sigma(x)}\le C_R^2(\log\theta_{m_\sigma(x)})^{2r_R}$ for fixed $C_R,r_R$. Inside operations (GL2) follows from (6c), $L^{\mathsf N^0_t-1}=R_{k_0+1}$ (CA-I L53769) and $R_{k_0+1}\le C_R(\log\underline\theta_t)^{r_R}$, the waiting-depth form of SA L17630 and L19410, since $\underline\theta_t\le\theta_m$ for $m\le t$. The distil allows exactly such a bound (`st1.md:260`).
- **BG (BG1).** As `st1.md:205-211`: on each admitted separated determining system $e$ (gap at least the floor $\rho_{\rm floor}$, cube size $M_1$), real data in $\mathcal R_e$ have one regular critical orbit and one canonical axial representative $\Phi_V$, holomorphic on $\|B\|<r_B$, real at real data, with the restriction identity for memberwise nested separated sequences (SA L9776-9780); the intrinsic tube (15) of radius $\delta_B$. Status: [C] as an implication on separated sequences (`a1-balaban.md` §§8-9, conditional on F0).
- **AV (averaging).** As `st1.md:212`. In addition:
  - **AV-it (new).** The averages are iterated: $\mathcal M^{q+1}U=\mathcal A_{q+1}(\mathcal M^qU)$, where the one-step average $\mathcal A_{q+1}$ of a level-$(q+1)$ bond $c$ reads only the level-$q$ bonds of the double block $D(c)$ (SA L9634, "double block", as quoted in `shift-map.md:42`), and is covariant: $\mathcal M^q(U^u)=(\mathcal M^qU)^{u|_{\mathbb T^{(q)}}}$.
  - **AV-row.** For complex $A$ in the weighted value ball of radius $c_4$, $\mathcal M^q(e^{i\eta A}U)(c)=e^{i\beta_q(c)}\mathcal M^qU(c)$ with $\beta_q$ holomorphic, $\beta_q(0)=0$, $|\beta_q(c)|\le C_Q\xi_q\sup_{D(c)}|A|$ (`a1-balaban.md` §3.1, P98.4-5, (3.1); "rebuilt in Section 3.5").
  - **AV-conv.** If $|\partial U-I|\le\epsilon\le cL^{-2}$ on the carriers, the tests of $M_{\mathbf B}(U)$ are within $2\epsilon$ of $\mathbf 1$ inside a layer and within $C_{\rm sm}L^2\epsilon$ across a seam (SA L9667, read here). The constant $C_{\rm sm}$ replaces the distil's unproved exact value $2L^2$.
- **AX (axial representative; new statement of SA's definition).** The representative $\Phi$ is in the axial gauge outside the nodes: for a bare site $x$ that is not a node, of level $n$, with block centre $z\in\mathbb T^{(n+1)}$, $(\mathcal M^n\Phi)(\Gamma_{z,x})=\mathbf 1$, $\Gamma_{z,x}$ the comb (SA L9667, read here; the comb is defined at SA L7065). At a top $y$ of level $q$ the Landau pair has $u_B(y)v_q[\mathcal H(B)](y)=\mathbf1$ (SA L9702), and the node factor obeys $|v_q[\mathcal H]^{\pm1}(y)-\mathbf 1|\le K_v\,\xi_q\sup_{B^q(y)}|\mathcal H|$ with $v_q$ a holomorphic function of $\mathcal H|_{B^q(y)}$ alone (`a3-derivative.md` §7.5, "a product of $j$ block means"). Status: definition (SA) plus [C] conditional (`a3-derivative.md`).
- **TH4 (SA Theorem 4; new as a named import).** On every admitted separated determining system, and on every subordinate separated meet with an erosion tower, at a real regular critical reference $U_0$ over $V_0$: for a datum direction $e$ at a bond $c$, placed at its top $y_c$, the derivatives $\mathsf h=\partial_s\mathcal H(B+se_c)$ and $\delta J=\partial_sJ(e^{i\eta\mathcal H}U_0)$ obey, on the whole polydisc $\|B\|<r_B$ and over every top $y$,
  \[
  \xi_y|\mathsf h|,\ \xi_y^2|\nabla\mathsf h|,\ \xi_y^3|D^{\mathsf T}D\mathsf h|,\ \xi_y^3|\delta J|\le C_4e^{-\theta_4d_{\mathbf B}(y,y_c)}|e|,
  \qquad |\dot u(y)|\le C_4e^{-\theta_4d_{\mathbf B}(y,y_c)}|e| ,
  \tag{TH4}
  \]
  with $C_4$, $\theta_4=c\delta_0$ independent of depth, volume and regions (SA L9734-9740, read here). Status: proved conditionally on P81, P82° and M1 in `a3-derivative.md` §§6-7 (verdict table `a3-derivative.md:548`). The current member is stated "at every bond where the current is defined" (SA L9740).
- **PROF (PR1).** As `st1.md:213`: at a real regular critical background on a separated sequence, $\eta^{-2}l(x)^2|\partial U-I|$ and $l(x)^3|J(U)|$ are at most $C_P\max_\tau e^{-\delta_Pd(x,\tau)}|\partial V(\tau)-\mathbf 1|$ (SA L9681; `a3-profile.md`), constants independent of depth, volume and region shapes (`a3-profile.md:34-37`).
- **RCG4 (four-dimensional regular cube gauge; new as a named import).** Let $q$ be a cube of side $s$ in level-$i$ units whose concentric enlargement of side $s+6$ embeds in the torus, and suppose that on the plaquette stars of that enlargement $|\partial U-I|<wL^2\eta_i^2$ and $|D_U^{\mathsf T}\partial U|<2L^3w\eta_i^2$, with $(s+2)L^3w\le c_{\rm rg}$. Then $U^v=e^{i\eta_iA}$ on the inner bonds of $q$ for a real gauge $v$, with $|A|,|\nabla^{\eta_i}A|<4L^3B_*(s+2)w$. This is the statement used at YM3 L53091-53121 (its three-dimensional source YM3 I-28-75). The four-dimensional statement is Balaban's CMP 99 Section F, Propositions 6-7, transcribed as G99.F at `a1-balaban.md:208-220` ("a small local potential with first, Hölder, and second-difference bounds of size $CM\varepsilon_0$"), "reduction rebuilt in Section 3.8, conditional on F0". Status: [C] conditional.
- **DR (PR1/NL1).** As `st1.md:214`. The weighted bound on the decoupling polydisc $\mathbb D(Y)=\{|s_c|<e^{\bar\kappa}\}$ is the source of the factor $E_{\bar\kappa}$ in (S): in the YM3 form it is $E_{\bar\kappa}=e^{C_b\bar\kappa}$ (YM3 L53837-53858, as used in `st1-draft.md:413`); $C_{\rm src}$ and $\mu$ are independent of $M$ and $\bar\kappa$. If IN1 requires the response bound itself to be free of $\bar\kappa$, the needed form is **DR-κ**: $E_{\bar\kappa}\le2$ whenever $M\ge C_{\rm DR}\bar\kappa$, the mechanism of `in1-draft.md:240,260` ((A.5)-(A.6)). ST1 does not need DR-κ; Section 4 explains why.
- **CRIT, CORE, LEV, FL.** As `st1.md:215-230`. CRIT includes the current at incomplete stencils, where in four dimensions at most five of the six plaquettes of a star remain (`st1.md:425`).
- **RUN.** As `st1.md:231`, with three precise additions:
  - **RUN1 (new).** On the frame class, $\tfrac12\le\varepsilon_{n+1}/\varepsilon_n\le2$ for every $n$. It follows from bounded frame increments $|\theta_{n+1}-\theta_n|\le C_\theta$ (SA L19410, "a frame can go up by as much as $c_5$"; SA L9767, "$-C\le x_q-x_{q'}\le C(q'-q)$") and the floor $\theta_n\ge\gamma^{-2}$, for $\gamma\le\gamma_1(C_\theta,\mathfrak p_0)$: with $\varepsilon=g\,p_0(g)$, $g=\theta^{-1/2}$ and $p_0$ a power of $\log\theta$, both factors of $\varepsilon_{n+1}/\varepsilon_n$ tend to one uniformly as $\theta_n\to\infty$. RUN1 is a ceiling on $\gamma$.
  - **RUN-N (new).** $\mathsf N_t=\mathsf N(\underline\theta_t)$ with $\mathsf N$ nondecreasing, $1\le\mathsf N(\theta)\le C_N(\log\theta)^r$ (SA L17630: "$\mathsf N_k=\check R_k\approx(\log x_k)^r$"; SA L19410: the waiting depth is "made instead with the running minimum").
  - **RUN-p (SA's exponent condition).** $\mathfrak p_0-\mathfrak p_1>r$. SA L17630 states the stronger "$\mathfrak p_1<\mathfrak p_0-Cr$" as a condition on the exponents.
- **BOX (core operation; new as a named interface).** The background after the box of an operation at level $t$ obeys $|\partial U-I|\le C(M)\varepsilon_t\eta_t^2$ within distance $M$ of $\Lambda^{\rm pr}$ and $\le(2+c)\varepsilon_t\eta_t^2$ elsewhere in the component (SA L17612, L17624, read here), and the box response obeys (S) with source in the box and threshold $\delta'_t$, with a constant $C(M)$. SA L17612: "$C(M)$ is a constant fixed before $\gamma$". BOX is a statement of the core operation (SA Proposition 2.4, SA L17656, as quoted in `os-draft.md:228`), not of a stage.

**(T) is no longer an import.** Theorem T proves it from AV, AX, TH4, PROF and BG.

---

## 4. Constants in order of choice

The order is the distil's (`st1.md:244-260`) with the new entries in their places. Each step uses only quantities fixed earlier. The coupling ceiling $\gamma$ is last.

1. $0<\beta_s\le1/4$, $0<\theta_s<1$, $0<c_R\le(1-\theta_s)/16$, $\beta_R=c_R\beta_s$; the logarithmic exponents $\mathfrak p_0,\mathfrak p_1,r$ with RUN-p; odd $L\ge13$, integer $2\le L_\flat<L/2$.
2. The import constants and rates: $C_Q,c_4,C_{\rm sm}$ (AV); $K_v$ (AX); $C_4,\theta_4$ (TH4); $C_P,\delta_P$ (PROF); $B_*,c_{\rm rg}$ (RCG4); $r_B,\bar\varepsilon,\rho_{\rm floor}$ (BG); $C_{\rm src},\mu$ (DR); $C_{\rm os},K^\sharp,c_\natural$ (CORE); $C_{\rm lev},K_{\rm pin},\epsilon_{\rm lev},c_{rt}$ (LEV); $C_{\mathcal A}$ (FL); $C_N$, $C_R$, $r_R$ (RUN-N, GEO-lift). Put $\delta:=\min\{\delta_P,\theta_4\}$ and $\delta_T:=\delta/4$.
3. The gap number $R_1$ (a power of $L$) and $\rho_0:=R_1M_1$ with
   \[
   \rho_0\ge\rho_{\rm floor},\quad \rho_0\ge4L^2,\quad
   \delta\rho_0\ge64\log L,\quad \rho_0\min\{\delta_T,\mu/2\}\ge\log16 .
   \tag{19a}
   \]
   These are lower bounds by numbers already fixed (`os-draft.md` Lemma 3.4). Then the minimum localization size $M'_1\ge\rho_0$ (a power of $L$; the distil's $M'_1$, `st1.md:196`).
4. $\delta_B\le\min(1/40,r_B/40)$; the constants of Theorem T: $C_u$ (Lemma PG), $S_4(\cdot)$ (Lemma RS), $C_{\rm X},C_{\rm h},C_{\rm R},C_\chi,C_{\rm far},K_a,K_T,r_w,\bar a,a_T$ (Section 7); $\hat a\le\min\{a_T/4,2^{-12}L^{-2},c_4,c_{rt},a_{\mathfrak h},a^\sharp/16,\delta_B/(4C_QL)\}$.
5. The radius constants: $\alpha_1\ge\alpha_0\ge\alpha_{\rm floor}:=4\max\{1,C_{\rm mb}\}C_{\rm RA}/c_{\min}$, with $c_{\min}=1-\tfrac{11}8\beta_s-3\beta_R$ (Lemma 2), $C_{\rm RA}=12C_PC_{\rm sm}L^4$ (Proposition RA) and $C_{\rm mb}$ of Theorem G. This floor contains the factor $L^2/L_\flat^2$ found by D2 (Section 14).
6. $K_{\rm pt},K_{\rm tw},K_{\rm core}$ of Proposition 6 and $r_*$ of (18).
7. $\bar\kappa\ge1$ (NL1's choice; it enters ST1 only through $E_{\bar\kappa}$ and (2)).
8. $M$: a power of $L$ with $M_1\mid M$ (aligned partitions), $LM\ge\rho_0$, $M\ge L^4M'_1$, every imported torus and cube floor, and $M\ge C_{\rm DR}\bar\kappa$ if DR-κ is used. All are **lower** bounds.
9. $A_1/A_0$: the main-step condition (40) of Theorem S.
10. $\gamma$: RUN1; the stage condition (41) of Theorem S; the absolute ceilings $c\lambda r_\iota\le\hat a$, $\lambda\alpha_1\varepsilon\le a_T/16$, $C_{\rm RA}\lambda\varepsilon\le c_{\min}a_T/16$, the gauge ceilings (31), $b_1^2\le c_\natural b_0$, $2(b_0+b_1)\le a^\sharp$, $C_{\mathcal A}\delta_{\rm src}<\epsilon_{\mathfrak h}$, $C_{\mathcal A}\delta'_j\le cL^{-9}$ (pivot chart); the real-admission ceilings of Propositions RA and 5′; and BOX's $C(M)\le\tfrac14c_{\min}\alpha_0L_\flat^{2(\mathsf N^0_t-1)}$.

**The IN1 requirement, constant by constant.** IN1 (`in1-draft.md:807-808`) requires that the constants of the stage, background and response bounds be fixed before $\kappa$ and be independent of $M$ and $\bar\kappa$, with $M$ entering only as a lower bound.

| Constant introduced here | Depends on | Independent of $M$, $\bar\kappa$ | Fixed before $\kappa$ |
|---|---|---|---|
| $\kappa(u)=\beta_s/(8\mathsf N(\theta_u))$ | $\beta_s$, the frame value $\theta_u$ | yes | it is formation data of the frame, like $\varepsilon_u$ |
| $c_{\min}=1-\tfrac{11}8\beta_s-3\beta_R$ | $\beta_s,c_R$ | yes | yes (step 1) |
| $\rho_0=R_1M_1$ | rates, $L$, $\rho_{\rm floor}$ | yes ($M_1$ is the cube size, fixed before $M$, SA L9599) | yes (step 3) |
| $C_u=8C_Q+2K_v$ (Lemma PG) | $C_Q,K_v$ | yes | yes |
| $S_4(a)$ (Lemma RS) | $L$, $a$ | yes | yes |
| $K_a,K_T,a_T,\delta_T,\bar a,r_w$ (Theorem T) | $L,\rho_0,C_Q,K_v,C_4,\theta_4,C_P,\delta_P,C_{\rm sm},r_B,\bar\varepsilon$ | yes | yes (step 4) |
| $C_{\rm RA}=12C_PC_{\rm sm}L^4$ (Proposition RA) | $L,C_P,C_{\rm sm}$ | yes | yes |
| smoothing rate $\delta/4$ in (6d) | $\delta_P,\theta_4$ | yes | yes |
| $C_{\rm mb}$ (Theorem G) | $L,\mathfrak M=M_1,B_*,B^{cg},B,C_{\rm box},C_{\rm pot}$ | yes: the factor $M$ cancels in the normalised bound (proof of Theorem G) | yes |
| $\alpha_{\rm floor}$ | $L,c_{\min},C_{\rm mb},C_{\rm RA}$ | yes | yes (step 5) |
| $K_{\rm pt},K_{\rm tw},K_{\rm core},r_*$ | the above, $C_{\rm os},K^\sharp,c_\natural$ | yes | yes (step 6) |
| $M'_1\ge\rho_0$ | $\rho_0$ | yes | yes (step 3) |
| conditions $M_1\mid M$, $LM\ge\rho_0$, $M\ge L^4M'_1$ | — | lower bounds on $M$ only | — |

Two quantities are not in the table, and I name them. (i) $E_{\bar\kappa}$ of (S) depends on $\bar\kappa$. It enters only $a_X$, and $a_X<1/2$ is made a condition on $A_1/A_0$ (main steps) and on $\gamma$ (stages), both chosen after $\bar\kappa$ (SA L19469-19470 put $A_1,A_0$ after $\bar\kappa$, as cited at `st1-draft.md:543`). No constant fixed before $\kappa$ depends on $\bar\kappa$ through ST1. Under DR-κ, $E_{\bar\kappa}\le2$ and even this dependence disappears, at the cost of the lower bound $M\ge C_{\rm DR}\bar\kappa$. (ii) $C(M)$ of BOX depends on $M$. It enters only the ceiling on $\gamma$ in step 10, chosen after $M$. Neither enters the fibre-precision constants $(a,H,\mu_0)$ of IN1's (I-1).

---

## 5. Elementary lemmas

**Lemma 2 (coefficient, count, geometry and profile arithmetic).** [proved here]

(i) *Range.* For every structure, site and index, $c_{\min}\le c^\natural_\sigma(x|m)\le1+\beta_s$, with $c_{\min}=1-\tfrac{11}8\beta_s-3\beta_R\ge39/64$.

(ii) *Gaps.* With the same marks:
\[
\begin{aligned}
 &c^\natural_{(t-1,{\rm out})}(m)-c^\natural_{(t,{\rm in})}(m)=(1-\theta_s)\beta_s2^{-(t-m)}\quad(m\le t-1);\\
 &c^\natural_{(t,n)}(m)-c^\natural_{(t,n+1)}(m)={g_t(m)\over2\mathsf N_t}+\kappa(j_n)2^{-|m-j_n|}+\beta_R\sum_{l\in E_n}2^{-|m-l|};\\
 &c^\natural_{(t,\mathsf N_t)}(m)-c^\natural_{(t,{\rm out})}(m)=g_t(m)/2 .
\end{aligned}
\tag{20}
\]
In each case the gap is at least $d_*(m)$ of (11).

(iii) *Stage count.* For each level $u$, at most $\bar N(u)$ operations have a stage at level $u$, and each has at most one.

(iv) *Size of the stage term.* $K_\sigma(m)\le3\beta_s/8$.

(v) *Geometry.* Meets of separated sequences are separated with the smaller gap. On a sequence separated with gap $\rho$, $|m(x)-m(z)|\le1+d(x,z)/\rho$. For an ambient sequence and a subordinate tower of depth $p$, with $\varsigma=l/\xi'$, $d'\ge d^\flat$, $d'(x,z)\ge\xi_p^{-1}|x-z|_\infty$ and $\varsigma(x)/\varsigma(z)\le L^{2+2d'(x,z)/\rho}$; at a settled element with $\varsigma(x)>1$ the tower has ended at $p$, and outside the Euclidean $l(x)$-neighbourhood $d'(x,z)>\varsigma(x)$.

(vi) *Profiles.* Under RUN1, for each profile of (11) and all $n,n'$, $w(n')\le4^{|n'-n|}w(n)$; hence $w(n+\nu)L^{-p\nu}\le w(n)$ for $p\ge1$, $\nu\ge0$, and $e^{-\omega(\nu-1)}w(n+\nu)\le4w(n)$ for $\nu\ge1$, $\omega\ge\log4$.

(vii) *Monotone inclusion.* For identical read functions, base radii and witness requirements, increasing every coefficient enlarges the domain.

*Proof.* (iv) uses (iii). Group the stages in $\mathrm{St}(\sigma)$ by stage level $u$. By (iii) at most $\bar N(u)$ of them have level $u$, each contributing $\kappa(u)2^{-|m-u|}$, so at most $\tfrac{\beta_s}82^{-|m-u|}$ per level; summing over $u\in\mathbb Z$ gives $\tfrac{\beta_s}8\cdot3$.

(iii) An operation at level $t$ has stage levels $t-\mathsf N_t,\dots,t-1$, one each, so it has a stage at level $u$ only if $t-\mathsf N_t\le u\le t-1$; there is one operation (one phase sequence) per level $t$, acting on all its components at once. Then $t-u\le\mathsf N_t=\mathsf N(\underline\theta_t)\le\mathsf N(\theta_u)=\bar N(u)$, because $u\le t$ gives $\underline\theta_t\le\theta_u$ and $\mathsf N$ is nondecreasing (RUN-N). So $t\in\{u+1,\dots,u+\bar N(u)\}$.

(i) As `st1.md:307`: the first three terms of (6) lie in $[1-\beta_s,1]$ for $m<t$ and in $[1-\beta_s,1+\beta_s]$ at $m=t$; the mark sum over a set of distinct levels is at most $3$, so the mark term is at most $3\beta_R$; subtract (iv). Then $c_{\min}\ge1-\tfrac{11}{32}-\tfrac3{64}=\tfrac{39}{64}$ for $\beta_s\le1/4$, $c_R\le1/16$.

(ii) Subtract. At a main step, $\mathrm{St}$ does not change (phase out of level $t-1$ and phase in of level $t$ have completed the same stages), and the distil's computation (20) applies (`st1.md:270-274`). At a stage, $\varpi$ drops by $1/(2\mathsf N_t)$, the mark set gains $E_n$, and $\mathrm{St}$ gains exactly the stage $(t,n)$ of level $j_n$. From phase $\mathsf N_t$ to output, $\varpi$ drops from $1/2$ to $0$ and nothing else changes. In each case the right side is at least $d_*(m)$, by inspection of (11).

(v) As `st1.md:309`; it uses only strips of width $\rho\xi_q$ and densities.

(vi) RUN1 gives $\varepsilon_{n'}/\varepsilon_n\le2^{|n'-n|}$. The factors $2^{-(t-m)}$ and $2^{-|m-j|}$ change by at most $2^{|n'-n|}$. Multiply. Then $w(n+\nu)L^{-p\nu}\le(4/L)^\nu w(n)\le w(n)$, and $e^{-\omega(\nu-1)}4^\nu=4(4e^{-\omega})^{\nu-1}\le4$.

(vii) Each scalar or core inequality persists when its radius increases; witnesses are unchanged. ∎

**Lemma 3 (local substitution estimates).** [proved here] The distil's Lemma 3 (`st1.md:313-361`), statement and proof unchanged: (25)-(28), with $|\ell(X,Z)|\le12(|X|+|Z|)^2$ for $|X|+|Z|\le1/4$, the Lipschitz bounds (26), the potential and difference bounds (27), and the plaquette bound
\[
 |\partial(e^{i\eta H}\mathbf U)-\partial\mathbf U|\le2^{12}\{\eta^2g+\eta h(\eta h+\eta a+|\partial\mathbf U-I|)\}
 \tag{28}
\]
under $\eta|H|,\eta|A'|\le1/64$. Two consequences are used below. *Real perturbation:* for a real potential $g$ and the ambient normalisation $\epsilon_U(e)=\eta^{-2}l^2|\partial U(e)-I|$, $\mathsf n(g)=\max\{l|g|,l^2|\nabla_Ug|\}$, if $\mathsf n(g),\epsilon_U\le2^{-13}$ then
\[
 \epsilon_{e^{i\eta g}U}\le2\epsilon_U+2^{13}\mathsf n(g),
 \tag{28a}
\]
because $\eta^{-2}l^2\cdot\eta h\cdot|\partial U-I|=(lh)(\eta/l)\epsilon_U\le lh\,\epsilon_U$ and the other terms are $l^2g$ and $(lh)^2$. *Increment of a fixed read under a fixed shift:* each of the five simple reads changes by at most $2^{13}$ times the corresponding normalised shift, at the base scale of the shift's own layer.

**Lemma 4 (intrinsic tube room).** [proved here] The distil's Lemma 4 (`st1.md:365-376`), unchanged: if $V=M_e(U)\in\mathcal R_e$ and $D=M_e(\mathbf U)=e^{i\beta}V$ with $\|\beta\|<\delta_B/2$, then $T_e(D)$ exists, is holomorphic in the fixed-$U$ fibre, and $\operatorname{dist}(D,\mathcal T_e^c)\ge\delta_B/8$ in $SL(2,\mathbb C)^e$.

**Lemma RS (the four-dimensional row sum).** [proved here] Let a separated sequence have gap $\rho\ge8$, let $d$ be its weighted distance, and let every row $c$ be assigned the top $y_c$ of its initial endpoint. If $a\rho\ge16\log L$ and $a\le1$, then for every site $x$
\[
 \sum_ce^{-a\,d(x,y_c)}\le S_4(a):=2000\,L^{9}\sum_{r\ge0}(r+2)^5e^{-ar/2}<\infty .
\]
*Proof.* Fix $r\ge0$ and the tops $y$ with $r\le d(x,y)<r+1$. Take a path from $x$ to $y$ of weighted length less than $r+1$. Every point $z$ on it has $d(x,z)<r+1$, so by Lemma 2(v) its layer differs from $m(x)$ by at most $1+(r+1)/\rho$; its density is at least $\xi_{m(x)+1+(r+1)/\rho}^{-1}$. Hence the Euclidean length of the path, and so $|x-y|_\infty$, is at most $(r+1)\xi_{m(x)+1+(r+1)/\rho}$. The same bound on layers gives the level $q$ of $y$ within $1+(r+1)/\rho$ of $m(x)$; there are at most $3+2(r+1)/\rho\le3(r+2)$ such levels. Level-$q$ tops are sites of the level-$q$ lattice, of spacing $\xi_q\ge\xi_{m(x)-1-(r+1)/\rho}$, so an $\infty$-ball of radius $R$ contains at most $(2R/\xi_q+1)^4$ of them. With $R=(r+1)\xi_{m(x)+1+(r+1)/\rho}$, $2R/\xi_q\le2(r+1)L^{2+2(r+1)/\rho}$, so there are at most $(3(r+1))^4L^{8+8(r+1)/\rho}$ tops of level $q$ in this shell. Each site is the initial endpoint of at most four positive bonds of its lattice. So the shell contributes at most
\[
 4\cdot3(r+2)\cdot81(r+1)^4L^{8+8(r+1)/\rho}e^{-ar}\le1000L^{8}(r+2)^5L^{8/\rho}e^{-(a-8\log L/\rho)r}.
\]
Since $a\rho\ge16\log L$, $a-8\log L/\rho\ge a/2$; and $L^{8/\rho}\le L$. Sum over $r$. ∎

The constant replaces YM3's $\mathsf S(a)=54L^3\sum_r(2r+1)^3e^{-a(r-1)/2}$ (YM3 L55518), whose exponent $3$ is the dimension. The proof above is dimension-explicit; the price of the mixed scales is the condition $a\rho\ge16\log L$, implied by (19a) for $a\ge\delta/4$.

---

## 6. Lemma OS dissolves: the stage sequences are separated

**Theorem OS′.** [proved here, from GEO-prep] Fix an operation at level $t=k$ on a class component $Z$, with $h=t_\flat$, $I_M=\{k_0+1,\dots,k\}$ and prepared sequence as in GEO-prep. For $0\le n\le\mathsf N_t$, let $S^{(n)}$ be the determining sequence after $n$ stages: inside $Z$, $\Omega^{(n)}_i\cap Z=Z\setminus Z''_i$ for $h<i\le h+n$ and $\Omega^{(n)}_i\cap Z=\Omega_i\cap Z$ otherwise; outside $Z$, the label. Then for every $i$,
\[
 \operatorname{dist}_\infty(\Omega^{(n)}_{i+1},(\Omega^{(n)}_i)^c)\ge LM\quad\text{(level-$i$ units)},
\]
and every member is, inside $Z$, a union of level-$i$ $M$-cubes. The same holds for every $\nu$-sequence (R21) with $\nu\le n$, for every meet of these with an erosion tower of gap at least $\rho_0$, and for the old/new pair of each stage, which is memberwise ordered.

*Proof.* Work in level-$k$ units; $u_i=L^{i-k}$, a level-$(i+1)$ $M$-cube has side $LMu_i$, and $a_i=MR_iu_i\ge Mu_i$ is a cell side. Since $Z''_l\subset\Omega_l^c\cap Z$, $(\Omega^{(n)}_i)^c\cap Z\subset Z''_i\cup\Omega_i^c$. Five cases, as in `os-draft.md` Lemma 2.3, which I rechecked line by line.

(a) $i,i+1\le h+n$ and $i+1\in I_M$: $(\Omega^{(n)}_i)^c\cap Z=Z''_i$ and $\Omega^{(n)}_{i+1}\cap Z=Z\setminus Z''_{i+1}$; one layer of level-$(i+1)$ $M$-cubes separates $Z''_{i+1}$ from $Z''_i$ (CA-I L53780-53782), so the distance is at least $LMu_i$.

(b) $i,i+1\le h+n$ and $h<i+1\le k_0$: $Z''_{i+1}=(\Omega_{i+1}^{\sim5})^c$ and $Z''_i\subset Z_i$. A point $y\notin Z''_{i+1}$ is within $5a_{i+1}$ of $\Omega_{i+1}$; since $\Omega_{i+1}^c\supset(Z_i)^{+5La_{i+1}}$, $\operatorname{dist}(y,Z_i)\ge5(L-1)a_{i+1}\ge LMu_i$.

(c) $i=h+n<i+1$: $(\Omega^{(n)}_i)^c\cap Z=Z''_i\subset Z_i$ (for $i\in I_M$ because $Z''_i\subset\Lambda\subset\Omega^c_{k_0+1}\subset Z_{k_0+1}$, otherwise by (b)), and $\Omega^{(n)}_{i+1}=\Omega_{i+1}$, so the distance is at least $5La_{i+1}\ge LMu_i$.

(d) $i,i+1>h+n$: label members, separated by at least $5La_{i+1}$ (and by $cM\check R_i$, SA L17398).

(e) Across $\partial Z$. If $i+1\le h$, both members are label members and (d) applies. Otherwise $i\ge h$, the margins of GEO-prep hold at level $i+1$, and we argue as follows. Let $y\in\Omega^{(n)}_{i+1}\cap Z$ and $z\in(\Omega^{(n)}_i)^c\setminus Z=\Omega_i^c\setminus Z$. Since $\Omega_i^c\subset Z_i\subset Z_k$ and $Z$ is a component of $Z_k$ (CA-I L53747-53753), $z$ lies in another component of $Z_k$. Iterating $Z_{t'}\supset(Z_{t'-1})^{+10a_{t'}}$ gives $(Z_i)^{+10a_{i+1}}\subset Z_{i+1}\subset Z_k$. If $|y-z|_\infty<10a_{i+1}$, the $\infty$-ball about $z$ of that radius is connected, lies in $Z_k$, and contains $y\in Z$; then $z$ and $y$ are in one component, a contradiction. So $|y-z|_\infty\ge10a_{i+1}\ge LMu_i$. Points with both ends outside $Z$ fall under (d).

Cube structure: CA-I L53779-53784 and the cell structure of the $Z_i$ (CA-I L53816-53819). The $\nu$-sequences are $S^{(\nu)}$ on the remade levels (SA L17436-17440). Meets: Lemma 2(v). Old/new pair: only the member of level $j+1$ changes, from $\Omega_{j+1}\cap Z$ to $Z\setminus Z''_{j+1}\supset\Omega_{j+1}\cap Z$. ∎

**Consequences.** (1) Under $M_1\mid M$ (aligned) and $LM\ge\rho_0$ (step 8), every determining sequence that ST1 reads, at every stage level, with overlapping collars or not, belongs to the class on which BG, PROF, TH4, RCG4 and DR are imported, with the constants at the floor $\rho_0$ (`os-draft.md` §3.3: a theorem stated for every sequence with gap at least $\rho_0$ applies to larger gaps with the same constants). (2) Overlap of collars is overlap of integration regions; it is not a defect of any sequence. The distil's correction of the round-1 attacks (`st1.md:473`) stands, and so does `os-draft.md` Proposition 6.1 (disjoint collars would force a box of side at least $MR_{k-1}/L$). (3) In every crossing of $\nu-1$ complete layers the weighted distance grows by at least $\rho_0(\nu-1)$, so each crossed layer costs a factor $e^{-\mu\rho_0}$ for any rate $\mu$ of step 2.

---

## 7. Item (a): the ambient tower estimate (T) in four dimensions

This section proves (T) (`st1.md:233-240`) in four dimensions. The model is YM3 Proposition I-95-61 and Corollary I-95-81 (YM3 L55448-55930, read in full in this session). The distil's objection (`st1.md:242`) names three four-dimensional statements that the round-1 proof used without supplying: the Landau-difference norm with its second-order member, the pillar gauge derivative, and a weighted row sum. They are Lemma LV, Lemma PG and Lemma RS (Section 5). The remaining steps of YM3's proof are dimension-free; I rewrite them with the four-dimensional constants, so that the proof can be read without YM3.

### 7.1 Setting

Fix an ambient separated sequence $\Omega^\flat_0\supset\cdots\supset\Omega^\flat_i$ and a subordinate separated sequence $\Omega'_0\supset\cdots\supset\Omega'_p$, $1\le p\le i$, $\Omega'_q\subset\Omega^\flat_q$, both with gap at least $\rho_0$ (by Theorem OS′, every determining sequence, meet and erosion tower that ST1 reads is of this kind). Write $Z=\Omega'_0$, $\mathsf Z=\operatorname{Bd}^\circ(Z)$, and as at YM3 L55467-55471
\[
 \lambda^\flat(x),\ \lambda'(x),\quad l(x)=\xi_{\lambda^\flat(x)},\quad \xi'(x)=\xi_{\lambda'(x)},\quad\varsigma(x)=l(x)/\xi'(x)\ge1,
\]
with weighted distances $d^\flat,d'$. An inner plaquette or full bond $e$ of $Z$ is *settled* when $\lambda'(x_e)=\min\{\lambda^\flat(x_e),p\}$. For a real $U$ and a complex form $w$,
\[
 \epsilon_U(e)=\eta^{-2}l(x_e)^2|\partial U(e)-I|,\qquad \mathsf n_b(w)=\max\{l(x_b)|w(b)|,\ l(x_b)^2|\nabla_Uw|_{\mathsf Z}(b)\},
\]
$\mathcal Q^{\rm T}(a)=\{\epsilon_U<a,\ \mathsf n(w)<a\}$, $E^\delta_U(x)=\max_ee^{-\delta d^\flat(x,x_e)}\epsilon_U(e)$, $E^\delta_w(x)=\max_be^{-\delta d^\flat(x,x_b)}\mathsf n_b(w)$. The tower configuration is
\[
 U^{\rm tw}(U,w)=\Phi_{V_0}(B(w)),\qquad V_0=M_{\mathbf B'}U,\qquad B(w)=\mathfrak b_{V_0}\bigl(M_{\mathbf B'}(e^{i\eta w}U)\bigr),
\]
where $\mathbf B'$ is the determining set of $\Omega'$ and $\mathfrak b_{V_0}$ is BG's datum coordinate about $V_0$ (the row datum with its endpoint correction, `a1-balaban.md:196-200`). No average is replaced by its linearization. At a settled $e$, with $n=\lambda^\flat(x_e)$, $n'=\lambda'(x_e)$,
\[
 G(U,w;e)=L^{2n}(\partial U^{\rm tw}(e)-I)\ (\text{plaquette}),\qquad G(U,w;e)=L^{2n+n'}\eta^3J(U^{\rm tw})(e)\ (\text{full bond}).
\]
Let $\mathcal F(B;e)$ be the same quantity in the tower scale, so that $G=\varsigma(x_e)^2\mathcal F$; let $\mathcal F^{\rm L}(B;e)$ be the same quantity for the Landau configuration $W_B:=e^{i\eta\mathcal H(B)}U_0$, where $U_0=\Phi_{V_0}(0)$ is the real critical representative and $(\mathcal H,u)$ is the Landau pair (SA L9697-9703).

### 7.2 Geometry

**Lemma TG.** [proved here] (i) Lemma 2(v) holds for $(\Omega^\flat,\Omega')$. (ii) If $|x-z|_\infty\le3l(x)$ then $|\lambda^\flat(x)-\lambda^\flat(z)|\le1$ and $d^\flat(x,z)\le12L$. (iii) If $b$ lies in the averaging carrier $\mathsf P^q(c)$ of a level-$q$ row $c$ of $\mathbf B'$, then $d'(x_b,y_c)\le6L$ and $\xi_q\le L\xi'(x_b)$. (iv) A site and its pillar top are within weighted distance $3/2$.

*Proof.* (ii) Since $\rho_0\ge4L^2>3L$, the $3l(x)$-ball lies within $\rho_0\xi_{\lambda^\flat(x)-1}$ of $x$, so it meets only layers $\lambda^\flat(x)\pm1$. The coordinate path from $x$ to $z$ has $\ell^1$-length at most $4\cdot3l(x)$ and density at most $L/l(x)$ on it. (iii) The two endpoint blocks of $c$ lie in $\Omega'_{q-1}$ (no inward rows), so the tower layer on the carrier is at least $q-1$ and the tower density there is at most $L/\xi_q$; the carrier has $\ell^1$-diameter at most $4\cdot\tfrac32\xi_q$ about $c_-=y_c$. (iv) As YM3 L55661. ∎

### 7.3 The real estimate

**Lemma TR.** [proved here, from AV-conv, BG and PROF] Put $c^\natural=C_{\rm sm}L^2$ and $C_{\rm R}=C_Pc^\natural L^4e^{6L\delta_P}$. If $W$ is real with $\epsilon_W<\alpha$ and $c^\natural\alpha\le\bar\varepsilon/2$, $L^2\alpha\le cL^{-2}$, then $M_{\mathbf B'}W\in\mathcal R_{\mathbf B'}$ with margin, its real critical representative $U^W_0$ exists, and in the tower scale, at every element $e$,
\[
 \varsigma(x_e)^2\,\mathsf e_{U^W_0}(e)\le C_{\rm R}\max_fe^{-\delta d'(x_e,x_f)/2}\epsilon_W(f),
 \tag{T1}
\]
where $\mathsf e$ is the curvature, or the current, in the tower block scale.

*Proof.* A tested plaquette of order $q$ averages bare plaquettes in $\Omega'_{q-1}$; there $\eta^{-2}\xi'^2|\partial W-I|=\varsigma^{-2}\epsilon_W<\alpha$. By AV-conv the tested holonomy is at most $c^\natural\max\varsigma^{-2}\epsilon_W$ over these plaquettes, which lie within tower distance $6L$ of a corner of the test (Lemma TG(iii)). The datum is therefore in $\mathcal R_{\mathbf B'}$ with margin, and BG gives $U^W_0$. PROF on the separated tower sequence gives $\mathsf e_{U^W_0}(e)\le C_P\max_\tau e^{-\delta_Pd'(x_e,\tau)}|\partial V(\tau)-\mathbf1|\le C_Pc^\natural e^{6L\delta_P}\max_fe^{-\delta_Pd'(x_e,x_f)}\varsigma(x_f)^{-2}\epsilon_W(f)$. Multiply by $\varsigma(x_e)^2$ and use Lemma 2(v): $\varsigma(x_e)^2/\varsigma(x_f)^2\le L^4e^{4(\log L)d'/\rho_0}\le L^4e^{\delta d'/16}$, since $\delta\rho_0\ge64\log L$. As $\delta_P\ge\delta$, $\delta-\delta/16\ge\delta/2$. ∎

At $w=0$ the tower is $U^U_0$ itself, so (T1) bounds $|\mathcal F(0;e)|\varsigma^2$ by $C_{\rm R}E^{\delta/2}_U(x_e)$. Combined with Lemma 3, (28a): for real $g$ with $\mathsf n(g),\epsilon_U\le2^{-13}$,
\[
 |G(U,g;e)|\le C_{\rm R}\{2E^{\delta/2}_U(x_e)+2^{13}\mathsf n(g)\},\qquad |G(U,0;e)|\le C_{\rm R}E^{\delta/2}_U(x_e).
 \tag{T1′}
\]

### 7.4 The Landau variation and its second-order member (Lemma LV)

**Lemma LV.** [proved here, from TH4 and Lemma 3] Let $\theta_4$ and $C_4$ be TH4's constants and $\Sigma(\beta;x)=\sum_ce^{-\theta_4d'(x,y_c)}|\beta(c)|$. On the polydisc $\|B\|<r_B$, for every element $e$ with base point $x$,
\[
 \xi'(x)\,|\mathcal H(B_1)-\mathcal H(B_0)|(b),\ \ \xi'(x)^2|\nabla(\mathcal H(B_1)-\mathcal H(B_0))|(b)\le LC_4e^{2\theta_4}\Sigma(B_1-B_0;x)
 \tag{T2a}
\]
for the bonds $b$ of the star of $e$, and
\[
 |\mathcal F^{\rm L}(B_1;e)-\mathcal F^{\rm L}(B_0;e)|\le C_{\rm L}\Sigma(B_1-B_0;x),\qquad C_{\rm L}:=2^{14}LC_4e^{2\theta_4},
 \tag{T2b}
\]
provided $\sup_{\rm star}\xi'|\mathcal H(B_s)|\le1/64$ and $|\mathcal F^{\rm L}(B_s;e)|\le2$ along the segment $B_s=B_0+s(B_1-B_0)$. Moreover $\xi'(x)|\mathcal H(B)|\le LC_4e^{2\theta_4}S_4(\theta_4)\sup|B|$.

*Proof.* The segment lies in the polydisc. Write $\mathcal H(B_1)-\mathcal H(B_0)=\int_0^1\sum_c\partial_{e_c}\mathcal H(B_s)[(B_1-B_0)(c)]\,ds$, a finite sum. TH4 bounds each term at the top $y$ of the bond by $C_4e^{-\theta_4d'(y,y_c)}|(B_1-B_0)(c)|$ in the scale $\xi_y=\xi'(x_b)$; the bonds of a star have tops within weighted distance $2$ of $x$ (Lemma TG(iv) and one step), and $\xi'$ changes by at most a factor $L$ on a star; this gives (T2a) with the factor $Le^{2\theta_4}$. For the current, TH4's current member gives directly
\[
 \xi'(x)^3|J(W_{B_1})-J(W_{B_0})|(e)\le LC_4e^{2\theta_4}\Sigma(B_1-B_0;x).
\]
This is where the second-order field control enters: TH4's current member is proved from its $D^{\mathsf T}D$ member and the critical equation (`a3-derivative.md` §§7.1, 7.3, (39)); no bound on $D^{\mathsf T}D\mathcal H$ is inferred from bounds on $\mathcal H$ and $\nabla\mathcal H$. For the curvature, differentiate along the segment: by (28) with $A'=\mathcal H(B_s)$ and $H=\epsilon\,\partial_s\mathcal H$, divided by $\epsilon\to0$,
\[
 |\partial_s\,\partial W_{B_s}(e)|\le2^{12}\bigl\{\eta^2|\nabla\partial_s\mathcal H|+\eta|\partial_s\mathcal H|\,(\eta|\mathcal H|+|\partial W_{B_s}(e)-I|)\bigr\}.
\]
Multiply by $\eta^{-2}\xi'^2$. The last term becomes $(\xi'|\partial_s\mathcal H|)\{\xi'|\mathcal H|\,(\eta/\xi')+|\mathcal F^{\rm L}|(\eta/\xi')\}\le3\,\xi'|\partial_s\mathcal H|$. Integrate in $s$ and use (T2a): the curvature change is at most $2^{12}\cdot4\,LC_4e^{2\theta_4}\Sigma$. The last assertion is (T2a) at $B_0=0$ with Lemma RS. ∎

### 7.5 The pillar gauge factor (Lemma PG)

**Lemma PG.** [proved here, from AX and AV-row] Let $x$ be a bare site of the pillar with top $y$ of level $q$ in the tower system, and put $\tau_x(\mathcal H)=\xi_q\sup_{\mathsf P(B^q(y))}|\mathcal H|$. Then $u_B(x)$ is a holomorphic function of $\mathcal H(B)|_{\mathsf P(B^q(y))}$ alone, and if $\tau_x\le\tau_0:=\min\{1/(8C_Q),1/K_v,1/(8C_u)\}$,
\[
 |u_B(x)^{\pm1}-\mathbf1|\le C_u\tau_x,\qquad C_u:=8C_Q+2K_v .
\]
Consequently $\operatorname{cn}(u_B(x))\le(9/8)^2<3/2$, and for two data in the half-ball $\tau_x\le\tau_0/2$,
\[
 |u_{B_1}(x)u_{B_0}(x)^{-1}-\mathbf1|\le4C_u\,\xi_q\sup_{\mathsf P(B^q(y))}|\mathcal H(B_1)-\mathcal H(B_0)| .
 \tag{T3}
\]

*Proof.* $\Phi(B)=W_B^{u_B}$ (SA L9700). By AV-it, $\mathcal M^n(W^u)=(\mathcal M^nW)^{u|_{\mathbb T^{(n)}}}$. Let $x$ be a non-node of level $n$ with block centre $z$. AX for $\Phi(B)$ and for $U_0=\Phi(0)$ gives $u(z)(\mathcal M^nW_B)(\Gamma_{z,x})u(x)^{-1}=\mathbf 1$ and $(\mathcal M^nU_0)(\Gamma_{z,x})=\mathbf1$. Hence
\[
 u_B(x)=u_B(z)\,(\mathcal M^nW_B)(\Gamma_{z,x}).
\]
Ascending through block centres $x=z_0,z_1,\dots$ reaches the top $y$ after at most $q$ steps, at strictly increasing levels $n_0<n_1<\cdots<q$; so $u_B(x)=u_B(y)\Pi$, $\Pi$ the ordered product of the comb transports $(\mathcal M^{n_k}W_B)(\Gamma_{z_{k+1},z_k})$. Each comb has at most $4\cdot\tfrac{L-1}2=2(L-1)$ bonds of level $n_k$, inside $B^{n_k+1}(z_{k+1})\subset B^q(y)$, and their double blocks lie in $B^q(y)$ (blocks are nested). By AV-row, each bond factor is $e^{i\beta}V$ with $V=(\mathcal M^{n_k}U_0)(b)\in SU(2)$ and $|\beta|\le C_Q\xi_{n_k}\sup_{B^q(y)}|\mathcal H|$. Move the unitary factors to the right: $\prod_m e^{i\beta_m}V_m=\prod_me^{i\beta'_m}\cdot\prod_mV_m$ with $\beta'_m=\operatorname{Ad}(V_1\cdots V_{m-1})\beta_m$, $|\beta'_m|=|\beta_m|$, and $\prod_mV_m=(\mathcal M^{n_k}U_0)(\Gamma)=\mathbf1$. The exponential series gives $|\prod e^{i\beta'_m}-\mathbf 1|\le e^{\sum|\beta'_m|}-1$. Summing over the levels, $\sum_k2(L-1)C_Q\xi_{n_k}\le2C_Q\xi_q(L-1)\sum_{m\ge1}L^{-m}=2C_Q\xi_q$. So $|\Pi^{\pm1}-\mathbf1|\le e^{2C_Q\tau_x}-1\le4C_Q\tau_x$ for $2C_Q\tau_x\le1/4$. At the top, $u_B(y)=v_q[\mathcal H](y)^{-1}$ (SA L9702) and AX gives $|u_B(y)^{\pm1}-\mathbf1|\le K_v\tau_x$. Then $|u_B(x)-\mathbf1|\le|u_B(y)||\Pi-\mathbf1|+|u_B(y)-\mathbf1|\le(1+K_v\tau_x)4C_Q\tau_x+K_v\tau_x\le(8C_Q+2K_v)\tau_x$, and the same for the inverse, $u_B(x)^{-1}=\Pi^{-1}u_B(y)^{-1}$. Holomorphy and locality: every factor is a holomorphic function of $\mathcal H|_{\mathsf P(B^q(y))}$ (AV-row, AX).

For (T3), $\varphi(\mathcal H):=u(x)[\mathcal H]$ is holomorphic on the ball $\xi_q\sup|\mathcal H|<\tau_0$ with $|\varphi-\mathbf1|\le C_u\tau_0\le1/8$. On the concentric half-ball, Cauchy's estimate on complex lines bounds the derivative of $\varphi$ by $C_u\tau_0/(\tau_0/2)=2C_u$ in the norm $\xi_q\sup|\cdot|$, so $|\varphi(\mathcal H_1)-\varphi(\mathcal H_0)|\le2C_u\,\xi_q\sup|\mathcal H_1-\mathcal H_0|$; and $|\varphi(\mathcal H_0)^{-1}|\le8/7<2$. ∎

The comb is the single path of SA L9667. If the tower representative is instead fixed by the averaged contour variables of SA L7185 (a Federbush mean over at most $4!$ shortest paths, SA L7065), the same proof applies with one more factor: the mean of transports $e^{i\beta_\Gamma}V_\Gamma$ about a family $V_\Gamma$ close to each other differs from the mean of the $V_\Gamma$ by a factor $e^{i\gamma}$ with $|\gamma|\le2\max_\Gamma|\beta_\Gamma|$ for small arguments, by the implicit function theorem applied to $\sum_\Gamma\log(V_\Gamma'V^{-1})=0$. Then $C_u$ doubles.

### 7.6 The combined Lipschitz estimate in the datum

**Lemma TC.** [proved here] Put $C_{\rm X}=3C_{\rm L}$, $C_{\rm h}=64LC_uC_4e^{4\theta_4}$ and
\[
 r_{\rm T}=\min\Bigl\{{r_B\over2},\ {\tau_0\over2L^2C_4e^{2\theta_4}S_4(\theta_4)},\ {1\over128LC_4e^{2\theta_4}S_4(\theta_4)},\ {1\over4C_{\rm L}S_4(\theta_4)}\Bigr\}.
\]
If $\sup|B_0|,\sup|B_1|<r_{\rm T}$ and $|\mathcal F(0;e)|\le1/2$, then
\[
 |\mathcal F(B;e)|<3/2,\qquad |\mathcal F(B_1;e)-\mathcal F(B_0;e)|\le[C_{\rm X}+C_{\rm h}|\mathcal F(B_0;e)|]\,\Sigma(B_1-B_0;x_e).
 \tag{T4}
\]

*Proof.* By Lemma LV, along every segment in the $r_{\rm T}$-ball $\xi'|\mathcal H|\le1/128$ and $\tau\le\tau_0/2$. Since $\mathcal F(B)=\operatorname{Ad}(u_B(x))\mathcal F^{\rm L}(B)$ (curvature is conjugated by the gauge at the base point; the current by $\operatorname{Ad}u(b_-)$), and $\mathcal F^{\rm L}(0)=\mathcal F(0)$ ($u_0=\mathbf1$), (T2b) gives $|\mathcal F^{\rm L}(B)|\le1/2+C_{\rm L}S_4(\theta_4)r_{\rm T}\le3/4$, hence $|\mathcal F(B)|\le\operatorname{cn}(u)\cdot3/4<9/8<3/2$; the hypothesis $|\mathcal F^{\rm L}|\le2$ of Lemma LV is thereby maintained along the segment. For the difference, write $g=u_0^{-1}u_1$ (at $x$) and
\[
 \mathcal F_1-\mathcal F_0=\operatorname{Ad}(u_1)(\mathcal F^{\rm L}_1-\mathcal F^{\rm L}_0)+\operatorname{Ad}(u_0)\bigl[\operatorname{Ad}(g)-1\bigr]\mathcal F^{\rm L}_0 .
\]
The first term is at most $\tfrac32C_{\rm L}\Sigma$. For the second, $\operatorname{Ad}(g)X-X=(g-\mathbf1)Xg^{-1}+X(g^{-1}-\mathbf1)$, so, with $|g^{\pm1}|\le2$ and $|g^{-1}-\mathbf1|\le2|g-\mathbf1|$, it is at most $\tfrac32\cdot4|g-\mathbf1||\mathcal F^{\rm L}_0|$, and $|\mathcal F^{\rm L}_0|\le\tfrac32|\mathcal F_0|$. By (T3) and $|u_0^{\pm1}|\le9/8$, $|g-\mathbf1|\le(9/8)^2\cdot4C_u\xi_q\sup_{\rm pillar}|\Delta\mathcal H|\le6C_u\xi_q\sup_{\rm pillar}|\Delta\mathcal H|$, and (T2a), with the pillar within weighted distance $2$ of $x$, bounds $\xi_q\sup_{\rm pillar}|\Delta\mathcal H|$ by $LC_4e^{4\theta_4}\Sigma$. The second term is therefore at most $54LC_uC_4e^{4\theta_4}|\mathcal F_0|\Sigma\le C_{\rm h}|\mathcal F_0|\Sigma$. ∎

### 7.7 The datum as a function of the potential

**Lemma TD.** [proved here, from AV-row and BG] Let $c_Q'\ge C_Q$ be the constant in $|B(w)(c)|\le c_Q'\xi_q\sup_{\mathsf P^q(c)}|w|$ (AV-row composed with BG's datum coordinate, which is a holomorphic function of the averaged bonds with derivative at most $c_Q'/C_Q$ near $V_0$). Put $\|w\|'=\max_b\mathsf L_-(b)|w(b)|$, $\mathsf L_-(b)$ the smaller endpoint block side in the tower, and $r_w=\min\{r_{\rm T}/(c_Q'L^2),\ c_4/(2L^2)\}$. On $\|w\|'<r_w$, $B(w)$ is holomorphic with $\sup|B(w)|<r_{\rm T}$, and on the half-ball
\[
 |B(w_1)(c)-B(w_0)(c)|\le2c_Q'L\max_{b\in\mathsf P^q(c)}\varsigma(x_b)^{-1}l(x_b)|w_1(b)-w_0(b)| .
 \tag{T5}
\]
In particular the tower exists and is holomorphic in $w$ on that ball.

*Proof.* For $b\in\mathsf P^q(c)$, $\xi_q\le L\xi'(x_b)$ (Lemma TG(iii)), and $\mathsf L_-(b)\ge\xi'(x_b)/L$ because tower layers change by at most one across a bond. Hence $\xi_q\sup_{\mathsf P^q(c)}|w|\le L^2\|w\|'$, which on $\|w\|'<r_w$ is below $c_4/2$ (AV-row applies) and gives $\sup|B(w)|\le c_Q'L^2\|w\|'<r_{\rm T}$. For (T5), apply Cauchy's estimate to the holomorphic map $w\mapsto B(w)(c)$ in the row norm $\xi_q\sup_{\mathsf P^q(c)}|\cdot|$, on the half of AV-row's ball: its derivative is at most $2c_Q'$ there, so $|B(w_1)(c)-B(w_0)(c)|\le2c_Q'\xi_q\max_{b\in\mathsf P^q(c)}|w_1(b)-w_0(b)|$, and $\xi_q\le L\xi'(x_b)=L\varsigma(x_b)^{-1}l(x_b)$. The tower is $\Phi_{V_0}\circ B$, a composition of holomorphic maps (BG). ∎

### 7.8 Theorem T

**Lemma RI (real and imaginary parts).** [proved here; YM3 (I-95-60), YM3 L55800-55809] Let $F$ be holomorphic and bounded by $M_0$ on the ball of radius $r$ about $0$ of a complex Banach space with a real structure for which $\|{\rm Re}\,z\|,\|{\rm Im}\,z\|\le\|z\|$. For $\|z\|\le r/2$,
\[
 |F(z)|\le3|F(0)|+|F({\rm Re}\,z)|+|F({\rm Im}\,z)|+6M_0\|z\|^2/r^2 .
\]
*Proof.* Write $F(v)=F(0)+DF(0)v+\mathcal R(v)$. For $\|v\|\le r/2$, the remainder bound below gives $|\mathcal R(v)|\le2M_0\|v\|^2/r^2$. Since $DF(0)$ is complex linear, $DF(0)z=DF(0){\rm Re}\,z+i\,DF(0){\rm Im}\,z$, and $DF(0){\rm Re}\,z=F({\rm Re}\,z)-F(0)-\mathcal R({\rm Re}\,z)$, similarly for ${\rm Im}\,z$. Collect the three remainders. ∎

The remainder bound: for $|\zeta|\le r$ the function $\phi(\zeta)=F(\zeta e)$, $\|e\|=1$, is bounded by $M_0$; its Taylor coefficients satisfy $|\phi^{(k)}(0)/k!|\le M_0r^{-k}$, so $|\phi(s)-\phi(0)-s\phi'(0)|\le M_0\sum_{k\ge2}(s/r)^k\le2M_0s^2/r^2$ for $s\le r/2$.


**Theorem T ((T) in four dimensions).** [proved here, as an implication from AV, AX, TH4, PROF and BG] Put
\[
\begin{gathered}
 C_\chi=1+L^2,\qquad C_{\rm far}={8c_Q'L^3\over\delta}e^{2\theta_4\cdot6L}S_4(15\delta/32),\\
 K_a=\max\Bigl\{7C_{\rm R},\ \bigl(2^{14}C_{\rm R}+9L^4/(2r_w)\bigr)C_\chi e^{12L\delta_T}+(C_{\rm X}+C_{\rm h})C_{\rm far}\Bigr\},\qquad
 K_T=(C_{\rm X}+C_{\rm h})C_{\rm far}+4K_aC_\chi e^{12L\delta_T},\\
 \bar a=\min\Bigl\{{\bar\varepsilon\over2c^\natural},\ {cL^{-4}},\ 2^{-13},\ {r_w\over4L^2},\ {\delta_B\over4C_QL},\ {1\over2K_a},\ {1\over2C_{\rm R}}\Bigr\},\qquad a_T={\bar a\over5C_\chi^2},
\end{gathered}
\]
with $\delta_T=\delta/4$. All are independent of depth, volume, number of layers, $M$ and $\bar\kappa$. On $\mathcal Q^{\rm T}(a_T)$:

(i) the tower $U^{\rm tw}(U,w)$ and its current exist, are holomorphic in $w$ for fixed $U$, and the complex datum has distance at least $\delta_B/8$ from the complement of the intrinsic tube;

(ii) at every settled element,
\[
 |G(U,w;e)|\le K_a\{E^{\delta_T}_U(x_e)+E^{\delta_T}_w(x_e)\}\le1,\qquad
 |G(U,w_1;e)-G(U,w_0;e)|\le K_TE^{\delta_T}_{w_1-w_0}(x_e);
 \tag{T}
\]

(iii) at real $w$ the tower is the real axial representative of its averaged datum; the construction is covariant under real gauges (extended from the tops) and under complex conjugation.

*Proof.* Fix a settled $e$, $x=x_e$, $l=l(x)$, $\varsigma=\varsigma(x)$, $F(w)=G(U,w;e)$.

*Existence and tube room.* On $\mathcal Q^{\rm T}(\bar a)$: Lemma TR with $\alpha=\bar a$ admits $V_0$. Since $\mathsf L_-(b)\le L\xi'(x_b)\le Ll(x_b)$, $\|w\|'\le L\bar a<r_w$, and Lemma TD gives the holomorphic tower with $\sup|B(w)|<r_{\rm T}$. AV-row gives $M_{\mathbf B'}(e^{i\eta w}U)=e^{i\beta}V_0$ with $\|\beta\|\le C_QL\bar a\le\delta_B/4<\delta_B/2$, and Lemma 4 gives the tube room. This proves (i).

*Real values.* By (T1′) and $\bar a\le1/(2C_{\rm R})$, $|\mathcal F(0)|\le|F(0)|\le C_{\rm R}\bar a\le1/2$, so Lemma TC applies.

*Near part.* Let $\chi(b)=1$ for $|x_b-x|_\infty\le l$, $0$ for $|x_b-x|_\infty\ge2l$, linear between. Call bonds within $3l$ near. As $|\chi(b^+)-\chi(b)|\le\eta/l$ and, on near bonds, $l(x_b)\in[l/L,Ll]$ (Lemma TG(ii)),
\[
 \mathsf n(\chi v)\le C_\chi\mathsf n^{\rm nr}(v),\qquad \|\chi v\|'\le L^2\varsigma^{-1}\mathsf n(\chi v),\qquad \mathsf n^{\rm nr}(v)\le e^{12L\delta_T}E^{\delta_T}_v(x).
 \tag{T6}
\]
The middle inequality: if $\varsigma>1$, the tower has ended at $p$ (Lemma 2(v)), so $\mathsf L_-(b)\le L\xi_p=L\xi'(x)=Ll/\varsigma\le L^2l(x_b)/\varsigma$; if $\varsigma=1$, $\mathsf L_-(b)\le L\xi'(x_b)\le Ll(x_b)$. The last inequality is Lemma TG(ii). Apply Lemma RI to $F$ on the $\|\cdot\|'$-ball of radius $r_w$, where $|F|=\varsigma^2|\mathcal F|\le\tfrac32\varsigma^2=:M_0$, at $z=\chi w$ with $\|z\|'\le L^2\varsigma^{-1}\bar a\le r_w/2$:
\[
 |F(\chi w)|\le3|F(0)|+|F({\rm Re}\,\chi w)|+|F({\rm Im}\,\chi w)|+6M_0\|\chi w\|'^2/r_w^2 .
\]
The factor $\varsigma^2$ of $M_0$ cancels against $\|\chi w\|'^2\le L^4\varsigma^{-2}\mathsf n(\chi w)^2$, and $\mathsf n(\chi w)\le r_w/2$, so the last term is at most $(9L^4/(2r_w))\mathsf n(\chi w)$. The real and imaginary parts are real potentials with $\mathsf n\le\mathsf n(\chi w)$; (T1′) bounds them. Hence
\[
 |F(\chi w)|\le7C_{\rm R}E^{\delta_T}_U(x)+\bigl(2^{14}C_{\rm R}+9L^4/(2r_w)\bigr)C_\chi\,\mathsf n^{\rm nr}(w).
 \tag{T7}
\]
(Here $E^{\delta/2}\le E^{\delta_T}$.)

*Far part.* Let $u=w-\tilde w$ vanish within distance $l$ of $x$. For a bond $b$ in the support, $D_b:=d'(x,x_b)$. By settlement, $\varsigma\le1+D_b$ (Lemma 2(v)); and $\varsigma/\varsigma(x_b)\le L^2e^{2(\log L)D_b/\rho_0}\le L^2e^{\delta D_b/32}$. For $b\in\mathsf P^q(c)$, Lemma TG(iii) gives $d'(x,y_c)\ge D_b-6L$ and $D_b\ge d'(x,y_c)-6L$. By (T4), (T5) and $G=\varsigma^2\mathcal F$, $|\mathcal F(\tilde w)|\le|F(\tilde w)|$,
\[
 |F(w)-F(\tilde w)|\le[C_{\rm X}+C_{\rm h}|F(\tilde w)|]\,2c_Q'L\sum_ce^{-\theta_4d'(x,y_c)}\max_{b\in\mathsf P^q(c)}\varsigma^2\varsigma(x_b)^{-1}l(x_b)|u(b)| .
\]
Now $\varsigma^2\varsigma(x_b)^{-1}\le(1+D_b)L^2e^{\delta D_b/32}$ and $e^{-\theta_4d'(x,y_c)}\le e^{6L\theta_4}e^{-\theta_4D_b}$. Since $\theta_4\ge\delta$, split $\theta_4D_b\ge\delta D_b=(\tfrac1{32}+\tfrac8{32}+\tfrac8{32}+\tfrac{15}{32})\delta D_b$: the first part cancels $e^{\delta D_b/32}$, the second gives $(1+D_b)e^{-\delta D_b/4}\le4/\delta$, the third is the output decay $e^{-\delta_TD_b}$, and the fourth, with $D_b\ge d'(x,y_c)-6L$, gives $e^{(15/32)\delta6L}e^{-(15/32)\delta d'(x,y_c)}$, summed over $c$ by Lemma RS on the tower sequence ($\tfrac{15}{32}\delta\rho_0\ge16\log L$ by (19a)). Hence
\[
 |F(w)-F(\tilde w)|\le[C_{\rm X}+C_{\rm h}|F(\tilde w)|]\,C_{\rm far}\max_be^{-\delta_Td'(x,x_b)}l(x_b)|u(b)| .
 \tag{T8}
\]

*Size.* For $C_\chi\mathsf n(w)\le\bar a$, (T7) and $\bar a\le1/(2K_a)$ give $|F(\chi w)|\le1$. Apply (T8) with $\tilde w=\chi w$, $u=(1-\chi)w$, and $d'\ge d^\flat$: $|F(w)|\le|F(\chi w)|+(C_{\rm X}+C_{\rm h})C_{\rm far}E^{\delta_T}_w(x)$. With (T6) and the definition of $K_a$ this is the first inequality of (T), and $K_a(E_U+E_w)\le2K_a\bar a\le1$.

*Lipschitz.* Let $v=w_1-w_0$, $w_0,w_1\in\mathcal Q^{\rm T}(a_T)$. Split $F(w_1)-F(w_0)=[F(w_1)-F(w_0+\chi v)]+[F(w_0+\chi v)-F(w_0)]$. The first bracket is a far change: by (T8) it is at most $(C_{\rm X}+C_{\rm h})C_{\rm far}E^{\delta_T}_v(x)$. For the second put $n_v=C_\chi\mathsf n^{\rm nr}(v)$ and $E=E^{\delta_T}_U(x)+E^{\delta_T}_{w_0}(x)$. If $n_v=0$ it vanishes. Otherwise, for $|z|\le R:=1+E/n_v$, $C_\chi\mathsf n(w_0+z\chi v)\le C_\chi(a_T+Rn_v)\le C_\chi(a_T+2C_\chi a_T+2a_T)\le5C_\chi^2a_T=\bar a$, so the size bound holds on that disc: $|F(w_0+z\chi v)|\le K_a(E+Rn_v)\le2K_aRn_v$. The function $z\mapsto F(w_0+z\chi v)-F(w_0)$ vanishes at $0$ and is bounded by $4K_aRn_v$; Schwarz's lemma (`st1.md:338`) at $z=1$ gives at most $4K_an_v$. If $E=0$, take $R=1$ and the same bound follows. With (T6), $n_v\le C_\chi e^{12L\delta_T}E^{\delta_T}_v(x)$, and the definition of $K_T$ gives the second inequality of (T).

*(iii).* At real data, uniqueness of the regular critical orbit and of its axial representative (BG); covariance and conjugation follow first at real data and then on the connected complex domain by holomorphy. ∎

**Corollary T′ (localized towers; the distil's (T)).** [port of YM3 Corollary I-95-81, YM3 L55869-55929] Let $\Omega^\flat$ have depth $t$, $1\le p\le i\le t$, $X$ a localization region of level $i-1$, $M'_1\ge\rho_0$ the minimum localization size (YM3's $M_1$, the distil's $M'_1$; not the cube size $\mathfrak M$), $M\ge L^4M'_1$, and localize by $\Omega'_q=\Omega^\flat_q\cap X_{[q]}$, $q\le p$, under either erosion rule. Put $n_i(x)=\min\{\lambda^\flat(x),i\}$ and $l_i=\eta L^{n_i}$. On $\mathcal Q^{\rm T}(a_T)$ with $l=l_i$, for every inner plaquette or full bond $e$ with base within $2\xi_p$ of $X^{\wr p}$, the element is settled, and
\[
 |G_{p,X}(U,A'_1;e)-G_{p,X}(U,A'_0;e)|\le e^{3\delta_T}K_T\max_be^{-\delta_Td_{\mathbf B^\flat}(y_e,y_b)}\max\{l_i(x_b)|A'_1-A'_0|(b),\ l_i(x_b)^2|\nabla_U(A'_1-A'_0)|_{\mathsf Z}(b)\},
\]
with $G_{p,X}$ as at YM3 L55882-55889 and the tops and distance of the full ambient sequence. This is the distil's (T), with its truncated ambient scale.

*Proof.* The truncation $\Omega^\flat_{\le i}$ is separated with the same gap. The localized sequence is separated (its complement is the union of two complements; Lemma 2(v)). The accumulated inward erosion to level $q$ is at most $2\rho_0\sum_{r<q}\xi_r\le2\rho_0\xi_q/(L-1)\le M'_1\xi_q$ under the first rule and $2M'_1\sum_{1\le r\le q}\xi_r\le3M'_1\xi_q$ under the second (geometric sums, YM3 L55911-55914). Also $\operatorname{dist}_\infty(X^{\wr p},X^c)\ge2M\xi_{p-1}$, and $(2M/L-2)\xi_p>3M'_1\xi_p$ because $M\ge L^4M'_1$. So a site within $2\xi_p$ of $X^{\wr p}$ is in every $X_{[q]}$, the localized and ambient memberships agree there, and the element is settled. The scale-invariant current is $\eta^3J$, which gives the power of $L$. Apply Theorem T(ii) to the truncated ambient sequence; passing to the full ambient sequence only decreases the weighted distance; moving each endpoint to its pillar top costs $e^{3\delta_T}$ (Lemma TG(iv)). ∎

**What changed from three to four dimensions.** (1) The current member: YM3 used its (I-93-47) with a Landau norm including $D^{\mathsf T}D\mathcal H$ and the local expansions (I-10-121)-(I-10-122) with a Lipschitz constant $600$ (YM3 L55739-55760). Here the current change is taken directly from TH4's current member, which a3-derivative proves from the $D^{\mathsf T}D$ member and the critical equation; no local expansion of the current is needed (Lemma LV). (2) The pillar gauge: YM3's bound $(\kappa_6+3)\tau$ (YM3 L55714-55737) used a three-dimensional comb count; Lemma PG uses the four-dimensional comb (at most $2(L-1)$ bonds per level, SA L7065) and gives $C_u\tau$. (3) The row sum: Lemma RS replaces $54L^3\sum(2r+1)^3$ by $2000L^9\sum(r+2)^5$, at the price $a\rho\ge16\log L$. (4) Local geometry: $12L$ in place of $9L$, $6L$ in place of $5L/2$, and $L^2\varsigma^{-1}$ in place of $L\varsigma^{-1}$ in (T6). (5) The averaging constant: $c^\natural=C_{\rm sm}L^2$ from SA L9667, not the imported value $2L^2$ (`st1.md:212`). None of these changes the form of the argument.

---

## 8. Item (b): real admission and the gauge theorem on every cube family

The distil's Proposition 5 (`st1.md:378-398`) is a correct implication from (30)-(31) and from "imported cube-gauge estimates" at every address. Its Outstanding note (`st1.md:400`) asks for those estimates on the remade families, with all ceilings and with YM3's containing-cube clause. This section supplies them, at every actual structure, from the tests that define the support of a history.

### 8.1 The tests in force

**Lemma TE (datum bounds on the support).** [proved here, from the stage tests of SA L17624, the label tests and AV-conv] Let $\sigma$ be a structure of a history and restrict to the support of its tests. Put $C_{\rm te}:=6C_{\rm sm}L^4$. Then every test loop $\tau$ of the determining datum of $\sigma$ satisfies
\[
 |\partial V(\tau)-\mathbf1|\le C_{\rm te}\,L_\flat^{2\mathcal E_\sigma(\tau)}\varepsilon_{m_\sigma(\tau)},
 \tag{TE}
\]
in the dimensionless units of its level, where $\mathcal E_\sigma$ is the raw lift exponent (Definition 2).

*Proof.* Three kinds of rows. (1) Rows of the label that no stage of a running operation has replaced: the label tests give $|\partial V-\mathbf 1|<2\varepsilon$ at their level (the carried tests "provide only $2\varepsilon_k$", SA L17624; GL1 of GEO-lift for inherited relaxations). (2) Rows of level $j+1$ on the raised set after the stage at level $j$. These are averages of the background $U^{(n+1)}$. On the support, SA L17624 bounds it there by $(1-\tfrac12\beta_s)c_lL_\flat^{2e_j}\varepsilon_j\eta_j^2$ with $c_l\le3$. In level-$(j+1)$ units this is at most $3L^2(\varepsilon_j/\varepsilon_{j+1})L_\flat^{-2}L_\flat^{2(e_j+1)}\varepsilon_{j+1}\le6L^2L_\flat^{2\mathcal E}\varepsilon_{j+1}$ (RUN1, $\mathcal E=e_j+1$). AV-conv (applicable for $\gamma$ small, since the radius is $O(L^2L_\flat^{2\mathcal E}\varepsilon)\le cL^{-2}$ by GEO-lift) multiplies by at most $C_{\rm sm}L^2$. (3) Rows on the shell of level $i$: SA L17624 bounds the background there by $(1-\beta_s(1-2^{-(j-i+1)}))L_\flat^{2(i-k_\sharp-1)_+}\varepsilon_i\eta_i^2$. Its exponent is at most $\mathcal E$ at those points: for $i>k_\sharp+1$ every point of the shell has original layer at most $k_\sharp$ (since $Z''_{i+1}\subset Z''_k\subset\Lambda\subset\Omega^c_{k_0+1}$, GEO-prep) and was raised at the stage of level $i-1>k_\sharp$, so $\mathcal E=e_{i-1}+1=i-k_\sharp-1$; for $i\le k_\sharp+1$ the exponent is $0$. AV-conv again costs $C_{\rm sm}L^2$. At the output, BOX bounds the background by $C(M)\varepsilon_t\eta_t^2$ near the box, where every point has original layer at most $k_\sharp$ (GEO-prep: $\Lambda\subset(\Omega^{\sim4}_{k_0+1})^c$, so points within $M$ of $\Lambda$ lie in $\Omega_{k_0+1}^c$) and hence $\mathcal E=\mathsf N^0_t-1$; the ceiling $C(M)\le\tfrac14c_{\min}\alpha_0L_\flat^{2(\mathsf N^0_t-1)}$ of step 10 makes this case no worse than (2); elsewhere BOX gives $(2+c)\varepsilon_t\eta_t^2$. ∎

### 8.2 Pointwise real bounds

**Proposition RA.** [proved here, from Lemma TE, PROF, Theorem OS′ and Definition 2] On the support of a history, at every structure $\sigma$, the actual background $U_\sigma$ (the real critical background of the determining datum of $\sigma$, BG) satisfies, at every site $x$ with $m=m_\sigma(x)$,
\[
 \eta^{-2}l(x)^2|\partial U_\sigma-I|,\quad l(x)^3|J_\eta(U_\sigma)|\ \le\ C_{\rm RA}\,\lambda_\sigma(x)\,\varepsilon_m,\qquad C_{\rm RA}:=2C_PC_{\rm te}=12C_PC_{\rm sm}L^4 ,
 \tag{30$\lambda$}
\]
at every complete element (complete plaquette, complete six-plaquette star) of $\operatorname{Bd}^\circ(\Omega^\sigma_0)$.

*Proof.* The determining sequence of $\sigma$ is separated with gap at least $\rho_0$ (Theorem OS′), so PROF applies: the left side is at most $C_P\max_\tau e^{-\delta_Pd_\sigma(x,\tau)}|\partial V(\tau)-\mathbf1|$. By (TE) and the two properties of the smoothed lift, $L_\flat^{2\mathcal E(\tau)}\le\lambda_\sigma(\tau)\le e^{(\delta/4)d_\sigma(x,\tau)}\lambda_\sigma(x)$. By RUN1 and Lemma 2(v), $\varepsilon_{m(\tau)}\le2^{|m(\tau)-m|}\varepsilon_m\le2\cdot2^{d_\sigma(x,\tau)/\rho_0}\varepsilon_m\le2e^{(\delta/4)d_\sigma(x,\tau)}\varepsilon_m$, since $\delta\rho_0\ge4\log2$. As $\delta_P\ge\delta$, the product of the three exponentials is at most one. ∎

This is the distil's (30) with the lift: (30) itself (`st1.md:381`) cannot hold without $\lambda$ on integrated collars, which is the content of D2 (`os-draft.md` §7.3). The lift costs nothing below, because the radii carry the same $\lambda$.

### 8.3 The gauge theorem on every family

**Theorem G (real gauges on all recorded cubes).** [proved here, as an implication from RCG4 and Proposition RA] Put
\[
 C_{\rm mb}:=24L^3B_*\max\Bigl\{12\mathfrak M+2,\ {3\over2B^{cg}},\ {C_{\rm box}L+2\over C_{\rm pot}},\ {3\over2B}\Bigr\}.
\]
Let $Q$ be a cube of side $s$ in level-$l$ units, recorded by a structure $\sigma$ in one of the families of (L2): a large cube ($s\le\mathsf oLM$, $Q\subset\Omega^\sigma_l$), a CA-I family cube ($s=M$ at index $m$, CA-I L48527-48565), a core cube ($s\le C_{\rm box}LM$ at index $i$), or a natural cube ($s\le12\mathfrak M$). Let $\Lambda_Q$ be the maximum of $\lambda_\sigma$ over the side-$(s+6)$ enlargement of $Q$ (recorded with the cube). Assume the torus floor $s+6\le$ (torus side), and the ceilings
\[
 8L^3(s+2)C_{\rm RA}\Lambda_Q\varepsilon_{l-1}\le c_{\rm rg},\qquad C_{\rm mb}C_{\rm RA}\Lambda_Q\varepsilon_l\le a_\flat/2 .
 \tag{31}
\]
Then the actual background $U_\sigma$ has a real gauge $U_\sigma^v=e^{i\eta_lA}$ on the inner bonds of $Q$ with
\[
 |A|,|\nabla^{\eta_l}A|<\Bigl({\rm gauge\ factor\ of\ the\ family}\Bigr)\times C_{\rm mb}C_{\rm RA}\Lambda_Q\varepsilon_l ,
\]
where the gauge factor is $\mathsf oLMB^{cg}$ for large cubes, $BM$ for CA-I family cubes, $C_{\rm pot}M$ for core cubes, and $1$ for natural cubes. Every natural cube $q$ has the containing cube $q'=q$, with a real gauge of index $l$ at most $a_\flat$: this is YM3's containing-cube clause (YM3 L53362-53367). The constant $C_{\rm mb}$ does not depend on $M$ or $\bar\kappa$.

*Proof.* (YM3 L53091-53135 in three dimensions.) Choose a cube $q^+\supset Q$ of integer side $\ell=\lceil s\rceil+1<s+2$; its concentric enlargement of side $\ell+4$ lies within distance $4$ of $Q$. By Theorem OS′ (gap at least $LM\ge\rho_0>4L$ in level-$(l-1)$ units) the plaquette stars there lie in layers at least $l-1$. By (30λ) and RUN1, with $w:=2C_{\rm RA}\Lambda_Q\varepsilon_{l-1}$, the curvature there is less than $wL^2\eta_l^2$ (the factor $L^2$ converts level $l-1$ to level $l$; $\varepsilon_{m}\le\varepsilon_{l-1}2^{m-l+1}$ and $L^{-2(m-l+1)}2^{m-l+1}\le1$ for $m\ge l-1$). The matrix divergence obeys
\[
 |D_U^{\mathsf T}\partial U|\le\eta_l^{-1}(wL^2\eta_l^2)^2\cdot6+\eta_l^2|J^{(l)}(U)|<2L^3w\eta_l^2,
\]
because the current part of the divergence at a bond is a sum over its six plaquettes (four dimensions; the factor $6$ replaces YM3's count) and $6w^2L^4\eta_l^3\le L^3w\eta_l^2$ when $6wL\eta_l\le1$, which holds for $L\eta_l\le1$, $w\le1/6$; the current term is at most $L^3w\eta_l^2$ by (30λ) converted to level-$l$ units. The first ceiling of (31) is RCG4's smallness $(\ell)L^3\cdot2w\le c_{\rm rg}$. RCG4 gives the gauge with $|A|,|\nabla A|<4L^3B_*(s+2)w=8L^3B_*(s+2)C_{\rm RA}\Lambda_Q\varepsilon_{l-1}\le16L^3B_*(s+2)C_{\rm RA}\Lambda_Q\varepsilon_l$ (RUN1). Divide by the family's gauge factor: for large cubes $(s+2)/(\mathsf oLMB^{cg})\le3/(2B^{cg})$ when $\mathsf oLM\ge4$; for CA-I cubes $(M+2)/(BM)\le3/(2B)$; for core cubes $(C_{\rm box}LM+2)/(C_{\rm pot}M)\le(C_{\rm box}L+2)/C_{\rm pot}$; for natural cubes $s+2\le12\mathfrak M+2$. In each case the factor $M$ cancels, and the result is at most $C_{\rm mb}C_{\rm RA}\Lambda_Q\varepsilon_l$ times the gauge factor. The containing-cube clause: take $q'=q$; its gauge has size at most $C_{\rm mb}C_{\rm RA}\Lambda_q\varepsilon_l\le a_\flat/2$ by the second ceiling of (31). Both ceilings are conditions on $\gamma$, since $\Lambda_Q$ is bounded by a power of $\log\underline\theta$ (GEO-lift) and $\varepsilon_l\to0$; the first one, for large cubes, involves $M$, and $\gamma$ is chosen after $M$. ∎

**On the remade families.** A stage remakes the determining member of level $j+1$, and with it the families of the new structure. Theorem G holds for **every** structure, so each new structure's families are supplied at its own background, with its own $\Lambda_Q$. The families of earlier structures are not re-made: (L2) imposes them per record, with their recorded bounds. At a later background they are supplied by Proposition DR below (drift), not by a new application of Theorem G. A gauge witness at the real factor of a general complex domain point is never needed: substitution does not change the real factor, and every target witness requirement is an input requirement (Definition 2).

**The four CA-I families.** Their cases G1-G4 (CA-I L48527-48565, read here) carry the printed lift exponents $(m-k_0)_+$, $(p-k_0)_+$, $p-\bar m$ and $0$. With $k_0=k_\sharp$ and the stage exponents of SA L17624 the test relaxation at the points of such a cube is at most $L_\flat^{2\cdot(\text{printed exponent})}$: in G1 the cube lies in the shell of index $m$ and its neighbours, whose exponent is $(m-k_\sharp-1)_+\le(m-k_0)_+$; in G2 the cube lies in the raised set at stage level $p$, exponent at most $p-k_\sharp-1<(p-k_0)_+$; in G3 the points have original layer at least $\bar m$, exponent at most $p-\bar m-1$; in G4 the cube lies in the label, exponent $0$. The witness bound of Theorem G uses $\Lambda_Q$, the smoothed lift, which can exceed the printed lift by the factor $L_\flat^2e^{(\delta/4)d}$ from lifted points at weighted distance $d$. The domain therefore imposes the CA-I families with the bound of Theorem G. This is a consumer change (Section 14, item 5).

### 8.4 Real admission at formation

Write $\widetilde U^{1/4}_{\sigma'|\sigma}$ for the domain with every base radius, $a_\flat$ and $a_T$ multiplied by $c_{\min}/4$ (coefficients unchanged), and with only the reads of $\sigma^\circ=\sigma$ in (L0)-(L4).

**Proposition 5′ (real admission at formation).** [proved here, the distil's Proposition 5 with lifts] Assume $\alpha_0\ge4\max\{1,C_{\rm mb}\}C_{\rm RA}/c_{\min}$, the ceilings (31) for every recorded cube, and $C_{\rm RA}\lambda\varepsilon_m\le c_{\min}a_T/16$ (a ceiling on $\gamma$). Then, on the support of a history, at every structure $\sigma$ and every $\sigma'\preccurlyeq\sigma$ and region $Y$, the plain triple $\mathbf P_{Y|\mathcal S}(U_\sigma)=(U_\sigma|_{\operatorname{Bd}(Y)},0,\mathbf J)$, $\mathbf J=J(U_\sigma)$ at complete stars and $0$ at incomplete ones, lies in $\widetilde U^{1/4}_{\sigma'|\sigma}(Y)$. Moreover every tower datum read by these clauses is admitted with tube room $\delta_B/8$.

*Proof.* (L0): (30λ) and the last ceiling. (L1): (30λ) gives $|\partial U-I|\le C_{\rm RA}\lambda\varepsilon_mL^{-2m}\le\tfrac14c_{\min}\lambda r_0(m)L^{-2m}\le\tfrac14c_\sigma\lambda r_0(m)L^{-2m}$, and the same for $\mathbf U=U$ and for the current at complete stars; $A'=0$; $\mathbf J=0$ at incomplete stars. (L2): Theorem G and $\alpha_0\ge4C_{\rm mb}C_{\rm RA}/c_{\min}$. (L3): the meet sequence is separated and subordinate to $\Omega^\sigma$ (Theorem OS′, Lemma 2(v)); its datum is admitted by AV-conv from (30λ), with margin, for $\gamma$ small; by BG's restriction identity the real tower is a real gauge transform of $U_\sigma$ restricted to the meet's region (SA L9776-9780), so its curvature and current at a settled element are those of $U_\sigma$. At the index $\ell=\min\{m,i\}\le m$, RUN1 gives $\varepsilon_mL^{-2m}\le\varepsilon_\ell L^{-2\ell}(2/L^2)^{m-\ell}\le\varepsilon_\ell L^{-2\ell}$ and $\varepsilon_mL^{-3m}\le\varepsilon_\ell L^{-2\ell-\min(q,\ell)}$; with $L^{i-p}\ge1$ this is (7) at a quarter of the radius. The complex tower at $\mathbf U=U$ is the real one; tube room is Lemma 4 with $\beta=0$. (L4): for $X'\subset\Lambda_i\subset\Omega_i$ the stars are complete; the subtower bounds follow from the same restriction identity as in the distil's proof (`st1.md:398`), with $2i\ge i+p$ and $3(i-q)\ge i+p-2q$; the core cubes are Theorem G. ∎

---

## 9. Item (e): changing reads and full-radius gaps

### 9.1 Compatibility by construction

**Lemma CR.** [proved here] Let $\sigma^-\preccurlyeq\sigma^+$ be consecutive structures (one transition), and $\sigma'\preccurlyeq\sigma^-$. Every clause of $\widetilde U_{\sigma'|\sigma^-}(Y)$ is a clause of $\widetilde U_{\sigma'|\sigma^+}(Y)$ with the same function, the same units, the same index, the same lift and the same base radius; only the coefficient differs, $c_{\sigma^+}$ in place of $c_{\sigma^-}$, and $c_{\sigma^-}-c_{\sigma^+}\ge d_*$ at every index (Lemma 2(ii)). The witness clauses (L2) and the absolute clause (L0) are identical.

*Proof.* $\mathrm{Ch}(\sigma'|\sigma^-)\subset\mathrm{Ch}(\sigma'|\sigma^+)$, and in (L0)-(L4) everything except the coefficient is attached to $\sigma^\circ$ or $\sigma''$. ∎

This is the distil's hypothesis 2, including "target tower maps, lifts, gauge cubes and core addresses are compared as functions, not just as addresses" (`st1.md:12`): they are the same functions. Enlarging a determining member at a stage changes the reads of the **new** structure only; the reads of the old one are still imposed, unchanged. The objection of `st1.md:460` ("Estimate (T) compares two inputs to one function") is met: (T) is applied to each read's own function, Theorem T applying to every ambient separated sequence, in particular to each $\Omega^{\sigma^\circ}$.

### 9.2 The half-gap substitution with chain reads

**Proposition 6 (half-gap substitution).** [proved here] Let $\sigma^-\to\sigma^+$ be a transition with profile $w$ of (11), $P\in\widetilde U_{\sigma'|\sigma^+}(Y)$ and $h$ a shift with $r=\|h\|_w\le r_*$, where
\[
 r_*={1\over8\max\{8L^2,K_{\rm pt},K_{\rm tw},K_{\rm core}\}},\qquad
 K_{\rm pt}=2^{15},\quad K_{\rm tw}=2^5e^{3\delta_T}K_T,\quad K_{\rm core}=8L^3C_{\rm os}K^\sharp(1+c_\natural)/c_{\min} .
 \tag{18}
\]
Then $P\dotplus h\in\widetilde U_{\sigma'|\sigma^-}(Y)$, and every read of the target keeps at least half its gap: $|F_a(P\dotplus h)|<b^{\rm mid}_a$. The same holds for a pinned shift satisfying the same bounds.

*Proof.* By Lemma CR it suffices, for each read $a$ of a structure $\sigma^\circ\in\mathrm{Ch}(\sigma'|\sigma^-)$, to show $|F_a(P\dotplus h)-F_a(P)|\le\Delta_a/16$, with $\Delta_a=(c_{\sigma^-}-c_{\sigma^+})(m^\circ)R_a\ge d_*(m^\circ)R_a$ at the read's index $m^\circ$. Since $R_a\ge\alpha_0\varepsilon_{m^\circ}L^{-pm^\circ}$ (lift at least one), it suffices to bound the change by $\tfrac1{16}\cdot2w(m^\circ)L^{-pm^\circ}$ in the read's units. By GEO-Mon, $m^+(x)\ge m^\circ(x)$, where $m^+$ is the layer of $\sigma^+$, in which the shift norm (10) is taken.

*Logarithms.* By the ceiling $c\lambda r_\iota\le\hat a\le2^{-12}L^{-2}$ and $r\le1$, $\eta|H|,\eta|A'|\le1/64$ on the active bonds; Lemma 3 applies.

*Simple reads.* By (27)-(28), the five simple reads change by at most $2^{13}$ times the normalised shift at the layer $m^+(x)$ (a fixed stencil, neighbouring layers within one, Lemma 2(v)). In the units of index $m^\circ$ (multiplied by $L^{pm^\circ}$) this is at most $2^{13}\cdot rw(m^+)L^{-p(m^+-m^\circ)}\cdot4\le2^{15}rw(m^\circ)$ by Lemma 2(vi) (the factor $4$ pays the neighbouring layer). So $K_{\rm pt}r\le1/8$ gives at most $w(m^\circ)/8$, while $\Delta_aL^{pm^\circ}\ge2w(m^\circ)$; the change is at most $\Delta_a/16$.

*Tower reads.* The tower of the read is the meet of $\Omega^{\sigma^\circ}$ with the erosion tower of $Z$, truncated at $i$. By (L0) and (L1) of $\sigma^\circ$, $(U,A')$ and $(U,A'')$ lie in $\mathcal Q^{\rm T}(a_T)$ with $l=l_i^\circ$ (the ceiling $\hat a\le a_T/4$). Corollary T′ bounds the change of $G_{p,X}$ by $e^{3\delta_T}K_T\max_be^{-\delta_Td^\circ(y_e,y_b)}\mathsf n^\circ_b$, where $\mathsf n^\circ_b$ uses the scale $l^\circ_i(x_b)\le l^+(x_b)$. Hence $\mathsf n^\circ_b\le L^{-(m^+(b)-n^\circ_i(b))}rw(m^+(b))\le rw(n^\circ_i(b))$ by Lemma 2(vi). On the separated truncated sequence of $\sigma^\circ$, Lemma 2(v)-(vi) give $e^{-\delta_Td^\circ(x,b)}w(n^\circ_i(b))\le4^{1+d^\circ/\rho_0}e^{-\delta_Td^\circ}w(n^\circ_i(x))\le4w(n^\circ_i(x))$, since $\delta_T\rho_0\ge\log4$ by (19a). The normalised read is $L^{p-i}G_{p,X}$, $|L^{p-i}|\le1$. So the change is at most $4e^{3\delta_T}K_Tr\,w(\ell)\le w(\ell)/64$ by (18), below $\Delta_a/16$ in the read's units.

*Cores.* As in the distil's proof (`st1.md:410-419`). The midpoint core is imposed at $(1-\tau_a)b^{\rm mid}$ with $\tau_a=(c^--c^+)/(c^-+c^+)\ge\tfrac25d_*(i)$ and $b^{\rm mid}_0\ge c_{\min}\alpha_0\varepsilon_i$. Restriction to $X'$ at level $i$ costs the factors $L,L^2,L^3$ of (5), and one neighbouring layer costs $4$ (Lemma 2(vi)); so the restricted potential, derivative and current increment are at most $4L^3rw(i)=2L^3rd_*(i)\alpha_0\varepsilon_i$. CORE's condition (16) at the midpoint radii requires this to be below $\tau_ab^{\rm mid}_0/(C_{\rm os}K^\sharp(1+c_\natural))$, which is implied by $2L^3r\le\tfrac25c_{\min}/(C_{\rm os}K^\sharp(1+c_\natural))$, that is by $K_{\rm core}r\le1/8$ with room. The current increment stays below $\tau_ab^{\rm mid}_0$, so the current stays below $b^{\rm mid}_0$.

*Witnesses and (L0).* Unchanged: the real factor is unchanged (Definition 3), and (L0), (L2) involve the real factor only.

*Restriction and pinning.* Restriction commutes with (8) by (4)-(5). For a pinned shift with the same bounds, the same estimates apply. ∎

The constants $K_{\rm pt},K_{\rm tw},K_{\rm core}$ depend on $L$, $\delta_T$, $K_T$, $C_{\rm os}$, $K^\sharp$, $c_\natural$, $\beta_s$ only; they are fixed before $\kappa$ and are independent of $M$ and $\bar\kappa$.

### 9.3 Real admission of earlier reads at later backgrounds (drift)

Chain reads move the radius comparison out of the substitution and into real admission: the current background $U_\sigma$ must satisfy the reads of every $\sigma^\circ\in\mathrm{Ch}(\sigma'|\sigma)$. These reads were admitted at $U_{\sigma^\circ}$ (Proposition 5′). Between $\sigma^\circ$ and $\sigma$ the actual background changes by the physical responses of the intervening transitions. The next proposition sums them. It makes real admission of the earlier reads depend on the physical identification of Section 11, hence on CRIT and LEV (and on BOX at output transitions); the round-1 design and the distil used these imports only for Proposition 7.

**Proposition DR (drift).** [proved here, as an implication from Theorem D4 at each transition, Theorem S and Proposition 6] On the support of a history, for $\sigma^\circ\preccurlyeq\sigma$, every read of $\sigma^\circ$ at the plain triple of $U_\sigma$ satisfies
\[
 |F_a(\mathbf P(U_\sigma))|<\tfrac14c_{\min}R_a+\tfrac1{32}(c_{\sigma^\circ}-c_\sigma)(m^\circ)R_a\le\tfrac12c_\sigma(m^\circ)R_a ,
\]
every recorded witness of $\sigma^\circ$ holds at $U_\sigma$ with at most $\tfrac12$ of its bound, and (L0) holds at $\tfrac12a_T$. Hence $\mathbf P(U_\sigma)\in\widetilde U^{1/2}_{\sigma'|\sigma}$, chain reads included.

*Proof.* Let $\sigma^\circ=\sigma_0\to\sigma_1\to\cdots\to\sigma_N=\sigma$ be the transitions. At the $k$-th, Theorem D4 (Section 11) gives, on the physical locus, $U_{\sigma_{k-1}}=(e^{i\eta H_k}U_{\sigma_k})^{g_k}$ with $g_k$ real and $H_k$ the real response at $s=\mathbf1$, $\lambda=1$; and Theorem S gives $\|H_k\|_{w_k}\le a_{X}r_*$ with $a_X<1/2$, so $\|H_k\|_{w_k}<r_*/2$. Every read is invariant under real gauges (curvature and current are conjugated by unitary matrices; towers are covariant, Theorem T(iii); witnesses are gauge-equivariant). So the read at $U_{\sigma_k}$ equals the read at $e^{-i\eta H'_k}U_{\sigma_{k-1}}$, $H'_k=\operatorname{Ad}(g_k)H_k$ real with the same norm. Proposition 6's estimates, applied to the real potential $-H'_k$ at the real triple of $U_{\sigma_{k-1}}$ (with $r<r_*/2$, so with $\Delta_a/32$ in place of $\Delta_a/16$), bound the change of each read by $\tfrac1{32}(c_{\sigma_{k-1}}-c_{\sigma_k})(m^\circ)R_a$. For the current of the plain triple, Theorem D4(2) gives $J(U_{\sigma_k})=J(U_{\sigma_{k-1}}^{g_k^{-1}})-K_k$ at complete stencils, so its change is the current part $K_k$ of the physical shift, bounded in the same norm; at the transition from phase $\mathsf N_t$ to the output, BOX supplies the relation and the bound in place of Theorem D4. These estimates require the read's input conditions at $U_{\sigma_{k-1}}$, which hold by induction on $k$ (the bound being proved is stronger). Sum over $k$: the coefficient differences telescope to $(c_{\sigma^\circ}-c_\sigma)(m^\circ)\le1+\beta_s-c_{\min}\le41/64$ (Lemma 2(i)-(ii); $c^\natural$ decreases at every transition). With the formation bound $\tfrac14c_{\min}R_a$ (Proposition 5′) the total is below $(\tfrac14c_{\min}+\tfrac1{32}\cdot\tfrac{41}{64})R_a<\tfrac12c_{\min}R_a$, because $\tfrac1{32}\cdot\tfrac{41}{64}<0.021<\tfrac14\cdot\tfrac{39}{64}$.

*Witnesses.* Let $B_Q$ be the recorded witness bound of a cube $Q$ (its gauge factor times $\Lambda_Q\alpha_0\varepsilon_l$; Theorem G with $\alpha_0\ge4C_{\rm mb}C_{\rm RA}/c_{\min}$ puts the formation gauge below $B_Q/4$). Apply the gauge $v$ of $U_{\sigma_{k-1}}$ on $Q$ to $e^{-i\eta H'_k}U_{\sigma_{k-1}}$: it gives $e^{i\eta_lA_k}$ with $A_k$ the logarithm of a product, and (27) bounds $|A_k-A_{k-1}|$ and its difference by $14$ times the shift in level-$l$ units. Since the layers on $Q$ are at least $l-1$, Lemma 2(vi) bounds the shift in level-$l$ units by $4L^2r_kw_k(l)=2L^2r_kd_{*,k}(l)\alpha_0\varepsilon_l$. Relative to $B_Q\ge\alpha_0\varepsilon_l$ the change is at most $28L^2r_kd_{*,k}(l)\le14L^2r_*d_{*,k}(l)$. Summing, $\sum_kd_{*,k}(l)\le41/64$, and $r_*\le1/(64L^2)$ (18) gives a total below $B_Q/4$.

*(L0).* By the simple-read computation, the change of $L^{2m^\circ}|\partial U-I|$ at one transition is at most $2^{15}r_kw_k(m^\circ)\le2^{14}r_*d_{*,k}\alpha_0\varepsilon_{m^\circ}$; the sum is at most $2^{14}r_*\alpha_0\varepsilon_{m^\circ}\le\alpha_0\varepsilon_{m^\circ}$, which is below $a_T/8$ by the ceiling $\alpha_1\varepsilon\le a_T/16$ of step 10. With the formation value $c_{\min}a_T/16$ the clause holds at $a_T/4$. ∎

**Consequence: no full-radius comparison is needed.** The distil's Outstanding item asks for "the actual full-radius comparison, including every truncation and lift" (`st1.md:467`). In the chain design no read is ever compared with a read of a different radius: the substitution compares a read with itself (Lemma CR), and real admission at a later background compares a read with its own value at formation (Proposition DR). The arithmetic error that the distil found in the round-1 truncated-layer estimate ($\tfrac54C_{\rm run}(1+\sqrt\nu)2^{-\nu}L^{-(p-1)\nu}$, `st1.md:462-467`) therefore does not arise. For completeness: with RUN1 the corrected comparison would read $R^+/R^-\le(2/L^p)^\nu$ for $\nu$ levels of truncation, and at $p=\nu=1$ the gap is at least $(\tfrac12-\tfrac54\cdot\tfrac2{13})R^-\ge0.3R^-$; it is not used.

---

## 10. Item (d): the source level and the no-new-mark margin

### 10.1 Where the source lies

**Lemma SL (source layers).** [proved here, from Theorem OS′ and AV-it] (i) At the stage $n\to n+1$ of the operation at level $t$, with $j=j_n$, every changed row and every bond of its averaging carrier lies in layers $j-1$, $j$ or $j+1$ of the old sequence $S^{(n)}$. (ii) At the main step $(t-1,{\rm out})\to(t,{\rm in})$ they lie in layers $t-2$, $t-1$ of the old sequence. Consequently, with $\nu(b)=|m^-(b)-j|$ at a stage and $\nu(b)=t-1-m^-(b)$ at a main step,
\[
 d^-(b,\mathcal S_v)\ge\rho_0(\nu(b)-2)_+ .
\]

*Proof.* (i) The changed rows are the old level-$j$ rows with an endpoint in $C_n=\Omega^+_{j+1}\setminus\Omega^-_{j+1}$, which have old layer $j$, and the new level-$(j+1)$ rows with an endpoint in $C_n$ (`shift-map.md` (1), `shift-map.md:28-33`). A carrier is a double block (AV-it), within $\infty$-distance $2\xi_{j+1}=2L\xi_j$ of its row. Since $\rho_0\ge4L^2$, separation puts it within one layer of the row's layer. (ii) The same with the new top member $\Omega_t$. The distance bound is Lemma 2(v). ∎

This corrects round-1's Corollary E′, which placed the source in layer at least $t-1$ (`st1.md:444`); `os-draft.md` §7.1 found the same correction.

### 10.2 The interpolation radius at every transition

**Theorem S.** [proved here, as an implication from DR, FL, LEV and RUN] Assume (S) with rate $\mu$ and the pinning bounds of Definition 5, and $\rho_0\mu\ge2\log16$ (19a). Then at every transition the number $a_X$ of (12) satisfies:

(i) at a main step,
\[
 a_X\le{2^{7}C_{\rm src}E_{\bar\kappa}C_{\mathcal A}C_{\rm lev}\over(1-\theta_s)\beta_s\alpha_0r_*}\,{A_1\over A_0}+C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{t-1}{K_{\rm pin}\over\epsilon_{\rm lev}};
\]

(ii) at a preparatory stage $(t,n)\to(t,n+1)$, $j=j_n$,
\[
 a_X\le{2^{10}C_{\rm src}E_{\bar\kappa}C_{\mathcal A}C_{\rm lev}\over\beta_s\alpha_0r_*}\,\bar N(j){\delta'_j\over\varepsilon_j}
     +C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta'_j{K_{\rm pin}\over\epsilon_{\rm lev}},
 \qquad \bar N(j){\delta'_j\over\varepsilon_j}\le C_N{A_1\over A_0}(\log\theta_j)^{r-(\mathfrak p_0-\mathfrak p_1)} .
\]

Hence $a_X<1/2$ at every main step if
\[
 2^{9}C_{\rm src}E_{\bar\kappa}C_{\mathcal A}C_{\rm lev}(A_1/A_0)\le(1-\theta_s)\beta_s\alpha_0r_*,
 \tag{40}
\]
a ceiling on $A_1/A_0$, together with the pinning term (a ceiling on $\gamma$); and at every preparatory stage, at every stage level, if
\[
 2^{12}C_{\rm src}E_{\bar\kappa}C_{\mathcal A}C_{\rm lev}C_N(A_1/A_0)(\log\theta_j)^{-(\mathfrak p_0-\mathfrak p_1-r)}\le\beta_s\alpha_0r_*\quad\text{for all }j,
 \tag{41}
\]
which holds for $\gamma\le\gamma_S$, because $\theta_j\ge\gamma^{-2}$ and $\mathfrak p_0-\mathfrak p_1-r>0$ (RUN-p).

*Proof.* (ii) The profile is $w(m)=\tfrac12\kappa(j)2^{-|m-j|}\alpha_0\varepsilon_m$ on the layers $m^+$ of $\sigma^+$ (11). For a bond $b$ read by $X$, $m^+(b)\in\{m^-(b),m^-(b)+1\}$ (only $C_n$ changes layer), so $|m^+(b)-j|\le\nu(b)+1$. Then $\varepsilon_j/\varepsilon_{m^+(b)}\le2^{\nu+1}$ (RUN1) and, by Lemma SL and since $d^-\ge d^+$ is the metric of the system on which DR acts,
\[
 {e^{-\mu d(b,\mathcal S_v)/2}\over w(b)}\le{2\cdot2^{\nu+1}\cdot2^{\nu+1}\over\kappa(j)\alpha_0\varepsilon_j}e^{-(\mu\rho_0/2)(\nu-2)_+}
 \le{2^3\cdot16\over\kappa(j)\alpha_0\varepsilon_j}\bigl(4e^{-\mu\rho_0/2}\bigr)^{(\nu-2)_+}\le{2^{7}\over\kappa(j)\alpha_0\varepsilon_j},
\]
using $4^{\nu}\le16\cdot4^{(\nu-2)_+}$ and $\mu\rho_0\ge2\log4$. So $Q_X\le2^7/(\kappa(j)\alpha_0\varepsilon_j)$, and with $\kappa(j)=\beta_s/(8\bar N(j))$ the first term of (12) is at most $2^{10}C_{\rm src}E_{\bar\kappa}C_{\mathcal A}C_{\rm lev}\bar N(j)(\delta'_j/\varepsilon_j)/(\beta_s\alpha_0r_*)$. Since $E_X\le1$, the second term is at most $C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta'_jK_{\rm pin}/\epsilon_{\rm lev}$. Finally $\bar N(j)=\mathsf N(\theta_j)\le C_N(\log\theta_j)^r$ (RUN-N) and $\delta'_j/\varepsilon_j=(A_1/A_0)(\log\theta_j)^{-(\mathfrak p_0-\mathfrak p_1)}$ (Definition 6).

(i) The profile is $\tfrac12(1-\theta_s)\beta_s2^{-(t-m)}\alpha_0\varepsilon_m$; the source level is $t-1$, $\delta_{\rm src}=\delta_{t-1}=(A_1/A_0)\varepsilon_{t-1}$; $\varepsilon_{t-1}/\varepsilon_m\le2^{\nu+1}$ with $\nu=t-1-m^-(b)$, and the same computation gives $Q_X\le2^7/((1-\theta_s)\beta_s\alpha_0\varepsilon_{t-1})$. ∎

**Why this closes the distil's (34).** The distil computed, with the old profile $w(j)=\theta_s\beta_s\alpha_0\varepsilon_j2^{-(t-j)}/(4\mathsf N_t)$ at the source layer, the ratio $\mathsf N_t2^{t-j}\delta'_j/\varepsilon_j$, which at the first stage is $\mathsf N_t2^{\mathsf N_t}\delta'_j/\varepsilon_j$ and is not controlled by any logarithmic saving (`st1.md:446-458`). D1's stage-graded term gives every index $m$ the gap $\kappa(j)2^{-|m-j|}$, centred at the **actual** source level $j$; the factor $2^{t-j}$ disappears, and $\mathsf N_t$ is replaced by $\bar N(j)$. Two points of the distil's objection are met exactly. (1) The count: Lemma 2(iii) bounds the number of operations with a stage at level $j$ by $\mathsf N(\theta_j)$ using the **running minimum** of the frame (SA L19410), not a comparison $x_j\ge x_t$ of density weights, which the distil rejects (`st1.md:458`). (2) The saving: (41) needs $\mathfrak p_0-\mathfrak p_1>r$, which is SA's own condition on the exponents (SA L17630: "$\mathfrak p_1<\mathfrak p_0-Cr$"). The old (N-growth) inequality and its proof via $\mathsf N_t^{3/2}$ (`st1-draft.md:459-463`) are not used. `os-draft.md` Corollary 7.5 used a flow bound $x_{t+1}-x_t\le C_{\rm fl}$ and (N-growth); both are replaced by Lemma 2(iii).

**The no-new-mark margin.** The gap at a stage is at least $\kappa(j)2^{-|m-j|}$ at every index, whether or not the read carries a new mark (Lemma 2(ii)); the shift fits it by Theorem S and Proposition 6. This is the "no-new-mark margin" of the distil's Outstanding heading, and of the assembly's ⟦ST-phase⟧ (`ym4-assembly.md` (a)5).

**The price of D1.** The coefficient falls by at most $3\beta_s/8$ over the whole history (Lemma 2(iv)); $c_{\min}=1-\tfrac{11}8\beta_s-3\beta_R\ge39/64$ keeps every radius above half its table value. The stage-graded term is formation data of the frame (it depends on $\theta_u$ through $\mathsf N(\theta_u)$), fixed with the coefficient table before any coupling-dependent choice of a step; it does not depend on $M$ or $\bar\kappa$.

**The transition from phase $\mathsf N_t$ to the output.** Its gap is $g_t(m)/2$ (Lemma 2(ii)) and its profile is the third line of (11). Its source is the box of the core operation, at the top level, with threshold $\delta'_t$ and constant $C(M)$ (BOX). The same computation as in (i) gives $a_X\le2^{8}C(M)C_{\mathcal A}C_{\rm lev}(A_1/A_0)(\log\theta_t)^{-(\mathfrak p_0-\mathfrak p_1)}/(\theta_s\beta_s\alpha_0r_*)+\ldots$, which is below $1/2$ for $\gamma$ small, $\gamma$ being chosen after $M$. This is the only place where $C(M)$ enters, and it enters a ceiling on $\gamma$ only.

---

## 11. Item (c): the preparatory reconstruction

The design matches the composition with the actual old read only on the physical locus (Definition 3; `st1-draft.md` §3.2, kept by the distil, `st1.md:128`). The distil's Outstanding note (`st1.md:425`) asks for four things: the joint map of the actual collar variables $(A_j,B_j)$ of CA-I L54287 to the old determining rows, including changed outward rows and return factors; that the one-step pivot chart of SA L8289-8296, which covers one homogeneous fibre, is enough; that every stored site is pinnable for the stage; and the four-dimensional current factor at incomplete stars. Lemmas DM, FC, ST and Theorem D4 supply them.

Throughout this section: a preparatory stage $n\to n+1$ of the operation at level $t$, $j=j_n$; old and new sequences $\Omega^\mp$, with $\Omega^-_q=\Omega^+_q$ for $q\ne j+1$ and $\Omega^-_{j+1}=\Omega_{j+1}\cap Z\subset\Omega^+_{j+1}=Z\setminus Z''_{j+1}$ inside $Z$ (GEO-Mon, Theorem OS′); rows $\Gamma^\mp_q$ as in SA L5612-5617, so that (`shift-map.md` (1), read here)
\[
 \Gamma^+_j\subset\Gamma^-_j,\qquad\Gamma^-_{j+1}\subset\Gamma^+_{j+1},\qquad\Gamma^+_q=\Gamma^-_q\ (q\ne j,j+1).
\]
Call $\Gamma^{\rm rm}:=\Gamma^-_j\setminus\Gamma^+_j$ the removed rows and $\Gamma^{\rm ad}:=\Gamma^+_{j+1}\setminus\Gamma^-_{j+1}$ the added rows. A main step is the same with $j+1$ replaced by the new top level $t$ (YM3 L54530-54557 treats that case in three dimensions).

### 11.1 The new datum is a local function of the old one

**Lemma DM.** [proved here, from AV-it and GEO] For every added row $c$, the double block $D(c)$ consists of old level-$j$ rows: $D(c)\subset\Gamma^-_j$. Define $F$ on old data by $F(D)(c)=D(c)$ for $c\in\Gamma^+\setminus\Gamma^{\rm ad}$ and $F(D)(c)=\mathcal A_{j+1}(D|_{D(c)})$ for $c\in\Gamma^{\rm ad}$. Then, wherever the averages are defined,
\[
 M_+(U)=F(M_-(U)),
 \tag{42}
\]
and $F$ is invariant under the residual gauges of the old system. Consequently $\ker DM_-\subset\ker DM_+$.

*Proof.* Let $c\in\Gamma^{\rm ad}$, a level-$(j+1)$ bond with an endpoint in $\Omega^+_{j+1}$ and, since $c\notin\Gamma^-_{j+1}$, no endpoint in $\Omega^-_{j+1}$. The member $\Omega^-_{j+1}$ is a closed union of level-$(j+1)$ cells (SA L17398), so a level-$(j+1)$ site outside it has $\infty$-distance at least one level-$(j+1)$ step from it. The blocks of the endpoints have radius $(L-1)/(2L)<1/2$ in those units, so no bond of $D(c)$ has an endpoint in $\Omega^-_{j+1}$. The endpoint of $c$ in $\Omega^+_{j+1}$ has distance at least $LM\ge\rho_0$ (level-$j$ units) from $(\Omega_j)^c$ (Theorem OS′), and $D(c)$ has diameter at most $3L/2$ in those units, so every bond of $D(c)$ has both endpoints in $\Omega_j$. Hence each bond of $D(c)$ has an endpoint in $\Omega_j$ and none in $\Omega^-_{j+1}$: it is in $\Gamma^-_j$. By AV-it, $\mathcal M^{j+1}U(c)=\mathcal A_{j+1}(\mathcal M^jU|_{D(c)})$, which is (42) on added rows; on the other rows of $\Gamma^+$, which are rows of $\Gamma^-$ with the same averaging map, (42) is the identity. The endpoints of added rows are level-$(j+1)$ sites, hence level-$j$ sites in $\Omega_j\setminus\Omega^-_{j+1}$, hence endpoints of old level-$j$ rows, hence old nodes; an old residual gauge is $\mathbf1$ there, and AV-it's covariance gives the invariance. The kernel inclusion is the chain rule applied to (42). ∎

This is the four-dimensional form of "fixing the shorter determining datum imposes all the constraints of the longer one" (YM3 L54560-54561), for the preparatory stage.

### 11.2 The actual old datum in the pivot chart

Let $U_+$ be the new real background on the physical locus (BG, for the new datum $D_+$), $V:=M_-(U_+)$, and $D_{\rm old}$ the actual old datum. Let $q_V(a)(c):=i^{-1}\operatorname{Log}\bigl(\mathcal A_{j+1}(e^{ia}V|_{D(c)})\,\mathcal A_{j+1}(V|_{D(c)})^{-1}\bigr)$ for $c\in\Gamma^{\rm ad}$, and use the pivot chart of SA L8289-8296 (QC24, read here):
\[
 a_V(u)=\Psi_V(\mathsf C_Vu),\qquad q_V(a_V(u))=0,\qquad a_V(u)|_{\rm free}=u,\qquad\|u\|_\infty<cL^{-9},
\]
with $\|a_V(u)\|_\infty+\|D_ua_V(u)\|\|u\|_\infty\le CL^4\|u\|_\infty$, and with the uniqueness of the pivot graph (SA L8257-8299, as read in `shift-map.md:1338-1340`): there is $c_{\rm ch}>0$ such that $q_V(a)=0$, $\|a\|_\infty<c_{\rm ch}$ imply $a=a_V(a|_{\rm free})$. Call this import **CH**.

**Lemma FC (fibre chart).** [proved here, from Lemma DM and CH] (i) $F(V)=D_+=F(D_{\rm old})$. (ii) $D_{\rm old}=V$ on every row of $\Gamma^-\setminus\Gamma^{\rm rm}$. (iii) Put $a:=i^{-1}\operatorname{Log}(D_{\rm old}V^{-1})$ on $\Gamma^{\rm rm}$ and $a=0$ elsewhere. Then $q_V(a)=0$. (iv) If $\|a\|_\infty<c_{\rm ch}$, then $u:=a|_{\rm free}$ satisfies $\|u\|_\infty<cL^{-9}$ for $c_{\rm ch}$ small, and
\[
 D_{\rm old}=e^{ia_V(u)}V\quad\text{on }\Gamma^{\rm rm},\qquad D_{\rm old}=V\quad\text{elsewhere}.
 \tag{43}
\]
Conversely every $u$ in the chart gives an old datum $e^{ia_V(u)}V$ in the fibre $F^{-1}(D_+)$. The map $(D_+,u)\mapsto D_{\rm old}$ is real-analytic, and on the fibre it is inverse to $D_{\rm old}\mapsto u$.

*Proof.* (i) $F(V)=F(M_-(U_+))=M_+(U_+)=D_+$ by (42) and BG (the new background has datum $D_+$). The stage defines the new block variables on the collar as level-$(j+1)$ averages of the stored level-$j$ field (SA L17585, as quoted at `os-draft.md:52`: the stored variables are "integrated out as in a small-field step"), that is $D_+=F(D_{\rm old})$. (ii) A row of $\Gamma^-\setminus\Gamma^{\rm rm}$ is a row of $\Gamma^+$ which is not added; there $D_{\rm old}=F(D_{\rm old})=D_+=M_+(U_+)=M_-(U_+)=V$, the last equality because the two averaging maps agree on such rows. (iii) By (i)-(ii), $\mathcal A_{j+1}(D_{\rm old}|_{D(c)})=\mathcal A_{j+1}(V|_{D(c)})$ for each added row, and $D_{\rm old}|_{D(c)}=e^{ia}V|_{D(c)}$. (iv) Uniqueness of the pivot graph. ∎

**Corollary FC′ (the actual collar variables).** [proved here] Let $\xi\mapsto D_{\rm old}(\xi;D_+)$ be any real-analytic parametrisation of the stage fibre $F^{-1}(D_+)$ near $V$, for instance Balaban's fluctuation fields $\xi=(A_j,B_j)$ on the collar $R_n$, with their Gaussian forms $\tfrac12\langle A_j,C^*\Delta^{(j)}_{\Lambda_{j+1}}CA_j\rangle$ and $\tfrac12\langle B_j,C^*\Delta^{(j)}CB_j\rangle$ (CA-I L54247-54251, L54295-54298, read here; Balaban CMP 122a (1.55)-(1.60)). Then
\[
 \mathfrak u(\xi):=\Bigl(i^{-1}\operatorname{Log}\bigl(D_{\rm old}(\xi)V^{-1}\bigr)\Bigr)\Big|_{\rm free}
\]
is real-analytic, $\mathfrak u(0)=0$ when $\xi=0$ is the background point, and $D_{\rm old}(\xi)=e^{ia_V(\mathfrak u(\xi))}V$. The joint map of the collar variables to the old determining rows is therefore
\[
 (D_+,\xi)\longmapsto\bigl(e^{ia_V(\mathfrak u(\xi))}M_-(U_+(D_+))\ \text{on }\Gamma^{\rm rm},\ \ M_-(U_+(D_+))\ \text{elsewhere}\bigr).
\]

*Proof.* Lemma FC (iii)-(iv) at each $\xi$; analyticity of $\operatorname{Log}$ near $\mathbf1$ and of the restriction to free bonds. ∎

This is exactly what CA-I L54287 instructs ("Express $U^{(n)}_k$ through the new background $U^{(n+1)}_k$ and the fluctuation $(A_j,B_j)$ on the collar $R_n$"), at the level of the datum: the old background is $U_{\mathbf B^-}(D_{\rm old}(\xi))$. The objection of `shift-map.md:181-183` ("These facts do not justify setting $u=g_j(A_j+B_j)$ without that identification") is met: no formula $u=g_j(A_j+B_j)$ is assumed; whatever the conditional-mean shift and strip change of variables in $\xi$ are (SA L7601, L7614), they are absorbed in $\mathfrak u$, which is defined from $D_{\rm old}(\xi)$. What remains is a bound on $\mathfrak u$ on the complex integration contour; it is FL's complex contour bound, $|\mathfrak u|<C_{\mathcal A}\delta'_j$ (`st1.md:230`), now stated for the function $\mathfrak u$.

**The one-step chart suffices.** The fibre $F^{-1}(D_+)$ near $V$ is a product over the added rows of one-step fibres (each added row constrains only $D(c)$, and distinct added rows have distinct pivot bonds in the chart of SA L8257-8299), together with the free removed rows outside every $D(c)$. So the single homogeneous fibre chart of SA L8289-8296, applied block by block with the background $V$, covers the stage fibre. This answers "The one-step pivot chart SA 8289-8296 supplies a chart for a single homogeneous fibre" (`st1.md:425`).

**The source, changed outward rows and return factors.** The DR source is the old datum in BG's datum coordinate about $V$:
\[
 B'_Y:=\mathfrak b_V\bigl(e^{ia_V(u)}V\bigr),\qquad \mathfrak b_V(V)=0 .
 \tag{44}
\]
The coordinate $\mathfrak b_V$ includes the endpoint (block-factor) correction of the row datum (`a1-balaban.md:196-200`: "it is not generally $i^{-1}\log(VV_0^{-1})$ at a seam"), so $B'_Y$ may be nonzero on the outward rows whose outer endpoint block contains a removed row: these are the **changed outward rows**. They lie within one block of $\Gamma^{\rm rm}$, hence in the layers of Lemma SL, and $|B'_Y|\le C_{\mathfrak b}CL^4\|u\|$. The **return factors** are CRIT's site factors $v$ (Theorem D4), removed by the gauge $g=v^{-1}$ at the old nodes.

### 11.3 Every stored site is a top or a site of a pinnable top

**Lemma ST.** [proved here, from GEO-st and GEO-prep] At every structure $\sigma$ of a history, every stored slot of level $l$ that is not yet integrated has an initial site $x$ that is either a top of $\sigma$'s determining sequence (its stored transport is then trivial) or a site of the pillar of a **pinnable** top $y$ of level $l+1$.

*Proof.* (YM3 Lemma II-84-18, YM3 L55202-55260, in three dimensions.) First the label. By GEO-st, $x\notin\Lambda_{l+1}$ and $\operatorname{dist}_\infty(x,\Omega_{l+2})>2\xi_{l+1}+2\eta$, so the layer of $x$ is at most $l+1$. If it is at most $l$, $x$ is a site of the level-$m(x)$ lattice in layer $m(x)$, hence a node and its own top. If it is $l+1$, $x$ lies in the pillar of the level-$(l+1)$ top $y=$ the centre of its level-$(l+1)$ block. For $l\ge1$, $y$ has level at least two and is pinnable by definition (YM3 L54649). For $l=0$, the pillar $B^1(y)$ lies within $\xi_1$ of $x$, so every bare site within $2\eta$ of it is within $\xi_1+2\eta<2\xi_1+2\eta$ of $x$, hence outside $\Omega_2$, hence in a pillar of level zero or one: $y$ is pinnable.

Now a stage sequence $S^{(n)}$ of an operation at level $t$ on a component $Z$, after $n$ stages: the stage levels $h,\dots,h+n-1$ are integrated and the members of levels $h+1,\dots,h+n$ are remade. Let $x$ be the site of a slot of level $l$ that is still stored; by GEO-st, $x\in Z_{l+1}=\Lambda_{l+1}^c$. Three cases.

(1) $l\ge h+n$. The members of levels $l+1$ and $l+2$ are the label's, so the label argument applies verbatim.

(2) $h\le l<h+n$. The stage at level $l$ has occurred, and it integrated the stored variables of level $l$ in its collar $Z_{l+1}\setminus Z''_{l+1}$ (CA-I L53806-53810). So $x\in Z''_{l+1}$. By nesting, $x\in Z''_i$ for every $i\ge l+1$, so $x\notin\Omega^{(n)}_i=Z\setminus Z''_i$ for the remade levels $i\ge l+1$; and $x\in Z''_{l+1}\subset\Omega_{l+1}^c$, so $x$ is in no label member of level at least $l+1$. Hence the layer of $x$ is at most $l$, and $x$ is its own top.

(3) $l<h$. The members of levels at most $h$ are the label's. If $l+2\le h$, the label argument applies. If $l+2=h+1$, the member of level $l+2$ is remade, $Z\setminus Z''_{h+1}$, and $x\in Z_h\subset Z''_{h+1}$ (GEO-prep). The distance from $Z_h$ to $Z\setminus Z''_{h+1}$ is at least $5(L-1)a_{h+1}$ if $h+1\le k_0$ (Theorem OS′, case (b)) and at least one level-$(h+1)$ $M$-cube if $h+1\in I_M$ (case (a), with $Z''_h=Z_h$); both exceed $2\xi_{l+1}+2\eta$. The label argument then applies with this member. ∎

So the pinned levelling of LEV preserves every stored transport that a carried term reads (YM3 L54741-54745: "At a pinnable levelled top it also preserves every stored transport"), provided the tops are levelled. Levelling at the physical point holds by the pin term of (12): $|\lambda|<\varrho_X$ gives pin size below $\epsilon_{\rm lev}/2$ (Definition 5, Theorem S).

### 11.4 Identification on the physical locus

**Theorem D4 (identification).** [port of YM3 Proposition II-93-38 (YM3 L54530-54625) and Lemma II-93-23 (YM3 L54449-54528), for main steps and preparatory stages in four dimensions; an implication from CRIT, BG, DR, LEV and Lemmas DM, FC, ST] Let $U_+$ be in the regular critical orbit of $D_+$ for the new sequence, axial on the source pillars, $P_+$ its plain triple, $u$ the fibre coordinate of the actual old datum (Lemma FC), real and in the chart, and $(H,K)=\mathfrak h(\mathbf1;P_+,B'_Y)$ the regional response to the source (44), $E=e^{i\eta H}U_+$. If the regular critical orbit of $(\mathbf B^-,D_{\rm old})$ exists (BG), then:

1. $E^g$ is in that orbit, for the real gauge $g=v^{-1}$ at the old nodes and $g=\mathbf1$ at the other bare sites, $v$ the site factors of CRIT;
2. at every complete current stencil in $\Omega^-_0$, $J(E)=L^{-3}J(U_+)+K$ in the units (5) (main step), respectively $J(E)=J(U_+)+K$ (preparatory stage, same level);
3. $H=0$ on the bare determining rows (no endpoint in $\Omega_1$), and $K=0$ at incomplete current stencils.

*Proof.* (1) By Lemma DM, $U_+$ is critical for the old system over $V=M_-(U_+)$, with zero multipliers on the constraints that the new system lacks: the first variation of the regional action vanishes on $\ker DM_+\supset\ker DM_-$. (2) Its reduced current $J^\circ(U_+)$ equals the full current at complete stencils. At an incomplete stencil, by separation no corner of its plaquettes is in $\Omega_1$; in four dimensions at most **five** of the six plaquettes of the star remain (`st1.md:425`), each with curvature less than $a_m$, so $|J^\circ(U_+)(b)|<5a_m\xi_0^{-3}$, and $(U_+,J^\circ(U_+))$ is in DR's natural class at radius $6a_m\le a_{\rm D}$ (a ceiling of step 4, replacing YM3's $3a_m$). The current of this pair agrees with the plain current off the bare rows. CRIT's plain-current boundary clause (the four-dimensional form of YM3 Lemma II-93-23, whose algebra uses only that the averaging is linear on bare rows, $\mathcal Q(A)=\xi A$, YM3 L54464-54468) identifies the responses: the potential is the same, and the current increments are equal because, at a real critical first pair, $\mathcal Q(H)=B'_Y$ vanishes on the bare rows, so $H=0$ there. (3) The row source is $B'_Y$ of (44), supported on removed and changed outward rows, all interior to $\Omega^-_0$; its twisted datum in DR is $B'_Y$ itself. CRIT gives: $E$ is critical with datum $(\mathfrak b_V^{-1}(B'_Y))^v=(D_{\rm old})^v$ by (43). Gauge covariance makes $E^g$ critical with datum $D_{\rm old}$, and CRIT's current identity gives 2. At an incomplete stencil every adjacent bond is a bare row, so $E=U_+$ on its plaquettes and $K=0$. (4) Regularity, checked rather than inferred: with $\beta_*=\sup|B'_Y|\le C_{\mathfrak b}CL^4C_{\mathcal A}\delta'_j$, (S) at $s=\mathbf1$ gives $l(b)|H|,l(b)^2|\nabla H|\le C_{\rm src}E_{\bar\kappa}\beta_*$ and $l(b)^3|K|\le C_{\rm src}E_{\bar\kappa}\beta_*$ at the layer of the base point. Lemma 3, (28), bounds the curvature of $E$ by that of $U_+$ plus $2^{13}C_{\rm src}E_{\bar\kappa}\beta_*$ in the layer scale; with (30λ) at $U_+$, both curvature and current of $E$ are within BG's regularity radius $\varepsilon_{\rm v}$ for $\gamma$ small (a ceiling of step 10). Regularity is gauge invariant, so $E^g$ is regular, and uniqueness of the regular critical orbit (BG) puts it in the orbit. ∎

**Proposition 7 (physical identification).** [proved here, as an implication from Theorem D4, LEV, Lemma ST and Definition 3] On the physical locus, for every carried term $f$ formed on an earlier structure, the pinned composition at $s=\mathbf1$, $\lambda=1$ equals the actual old read $f(\mathbf P(U_{\rm old});\mathfrak q)$, with the stored variables fixed in their recorded coordinates.

*Proof.* By Theorem D4, $E^g$ is in the regular critical orbit of $D_{\rm old}$, and by item 2 the substituted triple $P_+\dotplus h=(U_+,H,\mathbf J_++K)$ has the pair $(E,J(E))$. LEV's pinned levelling replaces $h$ by $h^\delta$, the pair by its transform (17) under a gauge $u_\delta$ which is $\mathbf1$ off the endpoints of $\operatorname{Bd}(Y)$ and satisfies $u_\delta(y)v^\sharp_q(y)=\mathbf1$ at levelled tops (YM3 L54737), and it preserves the stored transports at pinnable levelled tops (YM3 L54741-54745). At the physical point every top read by $f$ is levelled, by the pin term of Theorem S. The pinned pair is a gauge transform of $(E,J(E))$, hence (Theorem D4(1) and BG uniqueness) a gauge transform of the old pair by a gauge $\varrho$ which is $\mathbf1$ at the old nodes. LEV's content, in the form the distil requires (`st1.md:229`: it "must preserve the actual stored transports at their pinnable sites and give the common-center continuation"), is that $\varrho$ fixes every stored transport at the sites of levelled pinnable tops. By Lemma ST every stored site read by $f$ is either a top (transport trivial) or such a site. So $\varrho$ fixes every stored transport read by $f$, and the stored coordinates, recorded relative to these transports (YM3 L54647-54710 convention, `st1.md:198`), are the same before and after. Joint real-gauge invariance of $f$ (Definition 3) gives equality of values. This holds at every point of the real integration domain, so the represented integrand is unchanged. No uniqueness of holomorphic extensions off the locus is used. ∎

**Status of item (c).** Proved, as an implication from CRIT, BG, DR, LEV, FL, CH, GEO-st and GEO-prep. CRIT and LEV remain open four-dimensional imports, as the distil records (`st1.md:215, 223-229`). Within ST1 nothing remains: the joint map is (43) and Corollary FC′; the one-step chart suffices; stored sites are pinnable (Lemma ST); the incomplete-star factor is six.

---

## 12. Localized excess, resummation and (D4)

**Lemma 8 (localized excess and exact finite resummation).** [proved here] The distil's Lemma 8 (`st1.md:427-440`), statement and proof unchanged: if the compositions (13) are admitted and bounded by $b_f$ on $\mathbb D(Y)\times\{|\lambda|<\varrho_X\}$ with $\varrho_X>1$, and the zero shift, regional consistency and component locality hold, then (2) holds and
\[
 \sum_{Y\supseteq X^\uparrow}V_f(Y)=\Phi_T[f](\mathbf1,1)-f(\rho_XP;\mathfrak q_X).
 \tag{33}
\]
*Proof.* $G(s,\lambda)=\Phi(s,\lambda)-\Phi(s,0)$ vanishes at $\lambda=0$ and is bounded by $2b_f$; Schwarz gives $|G(s,1)|\le2b_f/\varrho_X$. The starred bracket vanishes at zero cube parameters; iterating the fundamental theorem of calculus writes $[K|N]G$ as the integral of its mixed derivative over the unit cube, and Cauchy circles of radius arbitrarily close to $e^{\bar\kappa}-1\ge e^{\bar\kappa-1}$ in each variable of $K$ give (2). For (33), the coefficient of the corner $N\cup A$ in $\sum_K[K|N]$ is $\sum_{A\subseteq K\subseteq T\setminus N}(-1)^{|K|-|A|}$, which is $1$ if $A=T\setminus N$ and $0$ otherwise; the subtracted value occurs only for $K=\varnothing$. ∎

The unshifted summand keeps its bound $b_f$; a bound on $\sum_Y|V_f(Y)|$, its summability over stages and the stored-field majorant SA L18108-18128 are NL1/LF1 inputs (`st1.md:440`). Exact resummation proves none of them.

**(D4).** [proved here, from Theorem 1] Order the finitely many transitions of a history. At each, Theorem 2 supplies hypotheses 1-5 of Theorem 1, so every carried term formed so far, evaluated at the composition of the substitutions applied after its formation, lies in its formation domain, with interpolation disc $|\lambda|<\varrho_X$, $\varrho_X>1$, for every value of the earlier parameters, fluctuations, switches and stored variables. The inclusion at one transition holds for every input of the domain, so it holds inside the next composition; the coefficients spent at distinct transitions are distinct terms of the telescoping sum $c_{\sigma^\circ}-c_\sigma$, so no gap is spent twice, and $c^\natural\ge c_{\min}$ throughout (Lemma 2). This is (D4) of `ym4-assembly.md` (a) with its full quantifiers, conditional on hypothesis 6.

---

## 13. Item (f): the application hypotheses at every actual stage

**Proof of Theorem 2.** Fix a history, a transition $\sigma^-\to\sigma^+$ (a main step, a preparatory stage at any stage level, or the transition from phase $\mathsf N_t$ to the output), and an inherited read. Every sequence involved is separated with gap at least $\rho_0$ (Theorem OS′), so every import applies with its constants at the floor.

*Hypothesis 1.* Real admission: Propositions RA, 5′ and DR put the actual real background in the half-radius domain of $\sigma^+$, chain reads included, with all witnesses of Theorem G and the containing-cube clause. Averaging hypotheses and tube room: for every tower datum read by the domain, the real datum is admitted by AV-conv from (30λ) or from (L0)-(L1) at complex points (Lemma TR), and the complex datum differs by $e^{i\beta}$ with $\|\beta\|\le C_QL\hat a\le\delta_B/4$ (AV-row and the ceiling $\hat a\le\delta_B/(4C_QL)$); Lemma 4 gives tube distance $\delta_B/8$, before and after substitution (the substituted potential is in $\mathcal Q^{\rm T}(a_T)$ by Proposition 6's logarithm step).

*Hypothesis 2.* Compatible read data: Lemma CR. Positive gaps: Lemma 2(ii), at least $d_*(m)$ at every index, with D1's term at stages.

*Hypothesis 3.* Domains of DR, AV, LEV: the absolute ceilings of step 4 and step 10 ($c\lambda r_\iota\le\hat a\le\min\{c_4,c_{rt},a_{\mathfrak h},a^\sharp/16\}$, $C_{\mathcal A}\delta_{\rm src}<\epsilon_{\mathfrak h}$, the natural-class radius $6a_m\le a_{\rm D}$), with the containing-cube gauges of Theorem G for DR's and LEV's cube clauses and the turning-cell gauges of LEV's (eq:levelling-regular-triple) supplied by restricting the natural-cube witnesses (each turning cell, a block of side one in its own level's units, lies in a recorded natural cube; YM3 L54668-54670). (T): Theorem T and Corollary T′. Uniform $K_{\rm pt},K_{\rm tw},K_{\rm core}$: Proposition 6.

*Hypothesis 4.* (S) on the whole complex parameter domain is DR's bound with source (44) (pivot completion, Lemma FC) and FL's contour bound; the endpoint-pillar bound is LEV's; $a_X<1/2$ is Theorem S, under (40) at main steps, (41) at stages, and BOX at the output transition.

*Hypothesis 5.* $M_+=F\circ M_-$: Lemma DM. The source changes $M_-(U_+)$ into the actual old datum: (43)-(44). Pivot and return factors: Corollary FC′ and Theorem D4(1). CRIT: the import, applied in Theorem D4. Pinned levelling and stored transports: Proposition 7 with Lemma ST.

*Hypothesis 6.* It is the statement that NL1 and LF1 must prove on the domains of Definition 2. Nothing in ST1 supplies it; Section 14 lists what changed in those domains. ∎

**What the overlapping collars change.** Nothing in this proof distinguishes stage levels $j\le k_\sharp$ from $j>k_\sharp$. The overlap enters only through the lifts: the raw exponents of Definition RA grow by one per overlap (SA L17624), and the absolute ceilings absorb them through GEO-lift. The constants of every bound are those of separated sequences at the floor $\rho_0$, independent of the number of overlapping collars (`os-draft.md` Corollary 3.5: at most $\mathsf N^0+2$, never used).

---

## 14. Repairs D1, D2 and the consumer changes

**D1 (`os-draft.md` §7.2).** The stage-graded coefficient is correct and is used, in (6a)-(6b). Two parts of `os-draft.md` are replaced. (1) Its count $\kappa(u)=\beta_s/(8\#W(u))$ needed $\#W(u)$ to be known at formation; here $\bar N(u)=\mathsf N(\theta_u)$ is a function of the frame value at $u$ and bounds $\#W(u)$ by Lemma 2(iii), through the running minimum. (2) Its Corollary 7.5 proved (AMP-st) from (N-growth) and a flow bound; Theorem S proves $a_X<1/2$ from (12), RUN-N and RUN-p. Lemma 7.3 of `os-draft.md` (the range) is Lemma 2(iv) here.

**D2 (`os-draft.md` §7.4).** The defect is real: on an integrated collar the stage tests bound the background in the scale of the stage, $L^2L_\flat^{-2}$ above the layer scale with the shifted lift (Lemma TE (2)). It is a fixed factor of $L$, and the floor $\alpha_0\ge4C_{\rm RA}/c_{\min}$ with $C_{\rm RA}=12C_PC_{\rm sm}L^4$ absorbs it; so the radius index stays the layer and D2's change of index (Definition 7.6 of `os-draft.md`) is not made. D2's observation is also why the distil's (30) needs the lift, which (30λ) carries. What D2 did not note, and what does change, is the size of the distil's lift $e=m-m^{\rm orig}$: at the output of an operation a core point is raised by up to $\mathsf N_t$ levels, and $L_\flat^{2\mathsf N_t}$ is not a polynomial in $\log\theta$ when $r\ge1$, so the absolute ceilings fail. Definition RA caps the exponent at $\mathsf N^0_t-1$, the overlap count of SA L17624, and (6c) gives a polynomial bound.

**Consumer changes** [design], for NL1, LF1 and the assembly:

1. *Chain reads.* $\widetilde U_{\sigma'|\sigma}$ imposes the reads of every structure between $\sigma'$ and $\sigma$, each with its own function, units, index and lift. Activities formed on these domains see more clauses, never larger radii.
2. *Lift.* The lift is the smoothed, capped stage lift (6d), Definition RA, in place of $L_\flat^{2(m-m^{\rm orig})}$.
3. *Coefficient.* $c^\natural=c-K_\sigma$ (6b), with $K_\sigma\le3\beta_s/8$.
4. *Witnesses per record.* (L2) imposes the recorded families of every $\sigma''\preccurlyeq\sigma'$ with their recorded bounds; the containing-cube clause is $q'=q$.
5. *CA-I families.* Imposed with the bound of Theorem G, $C_{\rm mb}C_{\rm RA}\Lambda_Q\varepsilon_m$ times the gauge factor, where $\Lambda_Q$ may exceed the printed $\mathsf L_0^{2e(Q)}$ by the smoothing.
6. *(L0).* A new absolute clause on the real factor, $L^{2m}|\partial U-I|<a_T/4$, so that (T) applies on the whole domain.
7. *Source.* The stage fluctuation enters through the fibre coordinate $\mathfrak u(\xi)$ of Corollary FC′; FL's contour bound must be stated for $\mathfrak u$.
8. *Constants.* $\alpha_0\ge4\max\{1,C_{\rm mb}\}C_{\rm RA}/c_{\min}$; $r_*$ of (18) with the factor $8L^2$; (40) on $A_1/A_0$; (41) and RUN1 on $\gamma$; RUN-p on the exponents (SA's own condition).

---

## 15. Status, open imports, sources

### 15.1 Status

| Item | Status here |
|---|---|
| Theorem 1 (ST1*) | [proved here], as an implication |
| Theorem 2 (application; hypotheses 1-5 at every main step and stage) | [proved here], as an implication from Section 3 |
| Lemma 2 (coefficients with D1, stage count, geometry, profiles) | [proved here] |
| Lemmas 3, 4 (substitution, tube) | [proved here] (distil) |
| Lemma RS (four-dimensional row sum) | [proved here] |
| Theorem OS′ (stage sequences separated; Lemma OS dissolved) | [proved here], from GEO-prep |
| Lemmas TG, TR, LV, PG, TC, TD, RI; Theorem T; Corollary T′ — item (a) | [proved here], from AV, AX, TH4, PROF, BG |
| Lemma TE, Proposition RA, Theorem G, Proposition 5′ — item (b) | [proved here], from the tests, PROF, RCG4, BOX |
| Lemma CR, Proposition 6, Proposition DR — item (e) | [proved here] |
| Lemma SL, Theorem S — item (d) | [proved here], from DR, FL, LEV, RUN |
| Lemmas DM, FC, Corollary FC′, Lemma ST, Theorem D4, Proposition 7 — item (c) | [proved here] / [port], from CRIT, BG, DR, LEV, CH, GEO |
| Lemma 8, (D4) | [proved here] |
| Section 13 — item (f) | [proved here]; hypothesis 6 is NL1/LF1's |

**No statement internal to ST1 is Outstanding.** In particular none of (a)-(f) ends at a stopped lemma, so no attacks are recorded.

### 15.2 Open imports, hardest first

These are hypotheses of Theorem 2. None is proved here; none is promoted by a citation.

1. **P82°** (`a3-derivative.md:556`): the weighted inverse at a real curved regular critical reference with the outline's $R$ and $K_0$; it is the linear input of TH4, and so of Theorem T and Theorem D4. `a3-derivative.md` calls it "the first point of failure".
2. **CRIT** in four dimensions (SA L5800-5803, L10446-10464 sketch it), including the plain-current boundary clause on bare rows.
3. **LEV** in four dimensions (YM3 L54627-55124 is the three-dimensional model).
4. **CORE**'s outer-core substitution in four dimensions (YM3 L42287-42325 in three).
5. **P81** (BG1: regular critical orbit, holomorphic chart, restriction identity; `a1-balaban.md`, conditional on F0) and M1 (multiplier normalisation, `a3-derivative.md:556`).
6. **BOX**: the box output bound and the box response bound with $C(M)$ (SA L17612, L17624, L17656).
7. **RCG4** (G99.F, `a1-balaban.md:208-220`, conditional on F0) and **CH** (the pivot chart's uniqueness, SA L8257-8299).
8. Geometry: **GEO-prep** (CA-I Definition 4.18, with the "layers" reading of `os-draft.md:100`), **GEO-Mon**, **GEO-st**, **GEO-lift**.
9. Running: **RUN1** (bounded frame increments), **RUN-N**, **RUN-p** (SA L17630).
10. Optional: **DR-κ**, only if IN1 requires the response bound itself to be free of $\bar\kappa$ (Section 4).

### 15.3 Source concordance (new citations of this draft)

All line numbers refer to the files at `31a47c543775`, read in bounded ranges in this session; the distil's concordance (`st1.md:477-492`) is kept.

| Citation | Reading |
|---|---|
| SA L9734-9745 (Theorem 4) | Exponential decay of the response: potential, gradient, $D^{\mathsf T}D$, Laplacian, current members, Hölder, $\dot\omega$, $\dot u$, "on the whole polydisc". Used as TH4. |
| SA L9696-9717, L9722-9732 (Theorem 3, comb remark) | Landau pair $(\mathcal H,u)$, $u_Bv_j[\mathcal H]=\mathbf1$ at tops, $\|\mathcal H\|_X,|D^{\mathsf T}D\mathcal H|\le C\sup|B|$; the comb slice and $\sup_x|h-\mathbf1|\le C\sup|B|$ at all sites. |
| SA L9667 | Axial gauge outside the nodes: $(\mathcal M^nU)(\Gamma_{z,x})=\mathbf1$; the converse "within $2\varepsilon$ ... within $CL^2\varepsilon$ across a seam". Used as AX and AV-conv. |
| SA L7065, L7185 | The comb (order $4,3,2,1$) and the averaged contour variable; tower axial gauge. |
| SA L9746-9755 (Theorem 5) | The four-dimensional statement of (T): "Lipschitz functions of $A'$ in first-order norms, with a weight $e^{-c\delta d^\flat}$" at settled elements. Proved here as Theorem T. |
| SA L9776-9789 (Theorem 6) | Separation of stage sequences (a); restriction identity (b); localized backgrounds with $\xi_y^3|D^*Df|$ (c). |
| SA L8289-8296 | The pivot chart (QC24) on $\|u\|_\infty<cL^{-9}$ with the bound $CL^4\|u\|$. |
| SA L17398-17407 | Stage sequences: "the only lower bound on the gaps is one $M$-cube of the later level". |
| SA L17606-17632 | Stage tests, overlap relaxation $L_\flat^2$ per overlap, $k_\sharp$, the exponents $e$, $c_l$, the $\gamma$-condition, $\mathsf N_k\approx(\log x_k)^r$, "$\mathfrak p_1<\mathfrak p_0-Cr$". |
| SA L19410 | Frame; waiting depth "made instead with the running minimum". |
| SA L6080-6150 | Operation, (R21), phases, (R22), lifts as formation data, unfinished-top conventions. |
| CA-I L53737-53832 | Definition 4.18: component, label, $N_0$, $k_0$, prepared sequence, collars, margins. |
| CA-I L48520-48568 | The four gauge families G1-G4 with printed lift exponents. |
| CA-I L54236-54330 | Profile-freeness; the fluctuation fields $A_j,B_j$ and their Gaussian forms; L54287. |
| YM3 L55448-55930 | Proposition I-95-61 and Corollary I-95-81 (template of Section 7). |
| YM3 L52979-53135 | Proposition II-90-39: $C_{\rm mb}$, the regular cube gauge argument (template of Theorem G). |
| YM3 L53330-53400 | Definition II-86-20, including the containing-cube clause (L53362-53367). |
| YM3 L54441-54626 | Lemma II-93-23 and Proposition II-93-38 (template of Theorem D4). |
| YM3 L54627-54790 | Pinned levelling: pinnable tops, levelled tops, Proposition II-85-34 statement. |
| YM3 L55200-55262 | Lemma II-84-18: stored sites are tops or sites of pinnable tops (template of Lemma ST). |
| `a3-derivative.md` §§7, 12 | TH4 proved conditionally on P81, P82°, M1; (39) the $D^{\mathsf T}D$ member; §7.3 the current member; §7.5 the top factor. |
| `a1-balaban.md` §§3.1-3.2 | P98.4-5 (3.1) averaging; G99.2 (3.3) with $|D^*DA|_{-3}$; G99.F local potentials. |
| `in1-draft.md:807-808` | The IN1 requirement on constants. |

---

## Result

Round 2 closes the six Outstanding items of the distil as implications from named imports. (a) (T) holds in four dimensions (Theorem T, Corollary T′): the second-order control is TH4's current member, the pillar gauge factor is Lemma PG from the axial definition SA L9667, and the row sum is Lemma RS. (b) The gauge theorem holds on every recorded cube family, the CA-I families and YM3's containing-cube clause included (Theorem G), from the pointwise real bounds (30λ), which carry the lift. (c) The preparatory reconstruction is (42)-(44): the new datum is a local function of the old one, the actual old datum is $e^{ia_V(u)}M_-(U_+)$ in the one-step pivot chart, every parametrisation of the stage fibre (Balaban's $(A_j,B_j)$ included) factors through $u$, and every stored site is pinnable; Theorem D4 and Proposition 7 then identify the composition with the old read. (d) D1's stage-graded coefficient, counted with the running minimum, gives $a_X<1/2$ at every stage under SA's own exponent condition (Theorem S). (e) Chain reads make every read compatible with itself, and the drift of earlier reads along the physical history is summed by the coefficient telescope (Proposition DR); no full-radius comparison is needed. (f) Hypotheses 1-5 of ST1* hold at every main step and every preparatory stage, at every stage level (Theorem 2); hypothesis 6 is the interface to NL1 and LF1.

Lemma OS dissolves (Theorem OS′). D1 holds and is used with a new count. D2's defect is a constant factor absorbed by $\alpha_0$; the lift is capped and smoothed instead.

Every constant introduced is fixed before $\kappa$ and is independent of $M$ and $\bar\kappa$; $M$ enters only through lower bounds. The factor $E_{\bar\kappa}$ of the decoupling polydisc and the box constant $C(M)$ enter only ceilings on $A_1/A_0$ and $\gamma$, chosen after $\bar\kappa$ and $M$.

This is research text. It grants no status, and no other model has checked it.
