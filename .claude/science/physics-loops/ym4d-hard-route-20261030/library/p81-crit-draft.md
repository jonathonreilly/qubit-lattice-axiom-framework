# P81 and CRIT, pass 1 (long draft): the critical background and the response at criticality

Two imports of ST1 (stage admission, `st1-draft2.md`), in our proof of T0 (continuum four-dimensional SU(2) Yang–Mills with the OS axioms). Pass 1 of four: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), one session, 2026-11-04, working in a clone of the planning folder (`library/`, `gates/`); nothing committed; only this file written. Sources read in bounded ranges in this session: the Sussman–Alpoge outline `ym4.tex` ("SA"), the three-dimensional account `YM3_I.tex` ("Y3"), both at `31a47c543775`, in the session scratch folder. Research text, not an audit. It grants no status. No other model has read it.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline's setting, the determining sets, the straightened rows, the pillar mean $Q'$, the projection $R$, the explicit current continuation $\Delta'_\pi$, the response system (R9), its two remarks (j) and (k), Theorems 1, 3, 4 and 6 of (1b), and for the three-dimensional account whose Propositions I-88-93, I-88-127, Corollary I-88-131 and Lemma II-93-23 are the templates of Section 5. Tadeusz Balaban for the background-field method: the critical orbit with prescribed averages, its analytic chart, the gauge theorem, the background propagators and the straightened variational problem (CMP 95, 96, 98, 99 (75–102 and 389–434), 102). Jonathan Dimock for his expositions of Balaban's renormalization group (arXiv 1108.1335, 1212.5562, 1304.0705), the readable model of the background and its response. OpenAI Codex for `a1-balaban.md`, `flat-port.md`, Sections 1–6 of `a3-derivative.md`, `dec-field.md`, `st1.md` and the gate `a3-derivative-gate.md`. Claude for the continuation of `a3-derivative.md`, `p82-draft.md`, `st1-draft2.md`, `wf-c.md` and the gates `a1-balaban-gate.md`, `flat-port-gate.md`.

Status words. **Proved** means every step is written here, from the named imports. **Import** means a statement of another library file, with its check record quoted. **Specification** means a definition that we fix and a consumer must use; it needs no proof. **Outstanding** means not proved. No step uses a computer. Every argument is finite-dimensional linear algebra, power series on finite products of matrix balls, the holomorphic implicit-function theorem, the identity theorem for holomorphic functions on a connected polydisc, and elementary inequalities. Each is Lean-formalizable in that sense.

Line numbers. "SA L" is a line of `scratchpad/sa/ym4.tex`; "Y3 L" a line of `scratchpad/sa/YM3_I.tex`. Library notes are cited as `note.md:line` or `note.md (eq)`. I quote the line before I say what a source states.

---

## 0. Result

**P81 is proved, as an implication.** Theorem P81 (Section 4) is the regular critical orbit with prescribed averages, its canonical axial representative, its holomorphic chart $\Phi$ with $M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0$ and complex regularity, the identification $\Phi(B)=U^\circ(e^{iB}\mathbf V_0)$ at real $B$, the local regular gauges on every row carrier, exact restriction to subordinate separated sequences (towers and meets included), and agreement of the charts on overlaps. The core existence/uniqueness/holomorphy theorem is the import (I-A1), Codex's `a1-balaban.md` §§3.5–9, checked by Claude (`gates/a1-balaban-gate.md`, "First failing step: none", conditional on F0). F0 is the import (I-F0), Codex's `flat-port.md`, checked by Claude (`gates/flat-port-gate.md`: "Row 81's F0 is discharged, including the level-0 seam check"). The local-gauge clause uses Proposition REG of `p82-draft.md` (I-REG). New here: the exact statement, the carrier-gauge Lemma 81.3, the real-data and uniqueness Lemma 81.2, the tower Lemma 81.4, the overlap Corollary 81.5, and the order of constants with one notation clash resolved (Section 4.8).

**CRIT is proved, as an implication.** Theorem CRIT (Section 5) is the four-dimensional form of SA L5800–5803 and L10446–10458, at $s\equiv\mathbf1$ over a real regular critical pair, with the plain-current boundary clause. It rests on P81, on the gated Lemmas 6.1–6.3 of `a3-derivative.md` (I-6), on the existence of the six propagators at the real critical reference and the contraction uniqueness of the chart system at $s\equiv\mathbf1$ (I-OPS, I-UNQ; both parts of `a1-balaban.md` §§3.9, 4, 9.1), and on one property of the DR specification, resummation at $s\equiv\mathbf1$ (DR1). It needs one specification: the $s\equiv\mathbf1$ values of the nonlinear remainder $\mathsf W_s$ and of the multiplier current $j_s$, which SA leaves unwritten (SA L10566–10569, L5786–5789). Section 5.2 fixes them, by porting Y3 (I-86-62) and (decoupled-current-definition). New here: the four-dimensional gauge identities (Lemma C1), the linear identities (Lemma C2), the reduced-action identity (Lemma C4), the equivalence of the $s\equiv\mathbf1$ system with slice stationarity (Proposition C5), the identification with the background through $\Phi$ (Theorem C6), the current identity (Proposition C7) and the plain-current clause (Proposition C8).

**CRIT does not need the quantitative content of P82°.** It uses only the algebraic part of P82(a) (Lemma 6.3's scalar isomorphism), which the gate of `a3-derivative.md` proves by finite-dimensional algebra.

**Outstanding inside P81 or CRIT: none.** No lemma is stopped, so no attacks are recorded. Each import has had one check by hand by the other provider.

**One correction for ST1.** `st1-draft2.md` Theorem D4, item 3, says "$H=0$ on the bare determining rows". The exact statement is $H(b)=\eta^{-1}B(b)$ on every bare row (Theorem CRIT (iv)). So $H=0$ on the bare rows outside the source. At a stage of level $j=0$ the removed rows are bare rows and $H\ne0$ there. What D4 uses, $K=0$ at incomplete stencils, needs only that the source misses the bare rows within $2\eta$ of $\Omega_0^c$ (Theorem CRIT (vii)). Section 6 lists this and the other consumer changes.

**Constants.** Every constant used here is a row-7 constant of `c4-order.md` or earlier: fixed before $\kappa$ (row 8), independent of $M$ (row 12) and of $\bar\kappa$ (row 9). Tables in Sections 4.8 and 5.13.

---

## 1. The targets, exactly

### 1.1 P81

`a3-derivative.md:56` states the premise:

> "**P81, cited-pending.** Row 81 must supply the regular real critical orbit at the actual determining datum, its local regular gauges and current bound, and the analytic averaging/critical charts of CMP 102 Theorem 1, Proposition 8 and the analyticity part of Proposition 9. On a row carrier these give a small local potential with size \(\kappa/\xi\), first difference \(\kappa/\xi^2\), and curvature \(\kappa\eta^2/\xi^2\), where \(\kappa=C_L\mathfrak M\bar\varepsilon\) is small."

Lemma 6.3 (`a3-derivative.md:409`) uses it "in the form used here: \(\Phi\) is holomorphic, \(\Phi(0)=U_0\), \(M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0\), and \(\Phi(B)\) is critical for real \(B\)". Lemma 10.2 uses "A1's uniqueness for \(\mathbf B'\) (P81)". The open list (`a3-derivative.md:556`) reads: "(2) **P81, row 81:** \(\Phi\) holomorphic, critical at real data, regular, uniform in depth." The verdict table (`a3-derivative.md:548`) rests Theorem 4's first paragraph on "P81, P82° (Lemma 8.1), M1".

The gate (`gates/a3-derivative-gate.md:224`) sets the strength: "**P81 at its actual strength.** It must supply the regular real critical orbit and uniqueness, the local gauges/current bounds used in Section 4 and the collar recursion, and the holomorphic \(\Phi\) with its complex regularity and uniform chart radius. … Only the local gauge-fixing neighbourhood in 6.3 is allowed to be nonuniform."

`st1-draft2.md:936` lists it among ST1's open imports: "**P81** (BG1: regular critical orbit, holomorphic chart, restriction identity; `a1-balaban.md`, conditional on F0)". `p82-draft.md:506`: "They need P81 (row 81: \(\Phi\) holomorphic, critical at real data, regular, uniform in depth …)".

The outline's statements are SA Theorem 1 (SA L9660–9668), the first paragraph of SA Theorem 3 (SA L9693–9697: "There is exactly one holomorphic map \(\Phi=\Phi_{\mathbf V_0}\) on \(\mathcal B\) that agrees with \(U^\circ(e^{iB}\mathbf V_0)\) for real \(B\). Throughout \(\mathcal B\) its complex averages are defined and \(M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0\), and \(\Phi(B)\) is regular at the radius \(C(\varepsilon_1+\sup|B|)\).") and the restriction identity of Theorem 6(b) (SA L9776–9780, as cited in `st1-draft2.md` §15.3).

### 1.2 CRIT

The binding statement is `st1.md:215`:

> "**CRIT:** at \(s=1\) over a real regular critical pair, the response solves the actual shifted constraint, yields the shifted current, and is regular enough for BG uniqueness. It also supplies the invariance under the plain-current boundary correction when used. The correction is supported on bare determining rows, not on all bonds outside the stage collar. SA 5800–5803 and 10446–10464 sketch this identification. Its required four-dimensional form remains an open import."

ST1's hypothesis 5 (`st1.md:15`) reads it: "The constraints and regularity satisfy CRIT." `st1-draft2.md:221` adds: "CRIT includes the current at incomplete stencils, where in four dimensions at most five of the six plaquettes of a star remain". `st1-draft2.md:933` lists "**CRIT** in four dimensions …, including the plain-current boundary clause on bare rows."

The outline's sketches. SA L5800–5803: "At \(s=1\) and real background data its shifted pair is the old background and its own current, up to the recorded node gauge factor. Existence, uniqueness and these properties of (R9) are substantive response inputs." SA L10446–10458: "At \(s=1\) over a critical real background, the first solution satisfies \(\mathcal Q(\mathbf H)=B',\ RD^{\mathsf T}\mathbf H=0,\ F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda\). For real data near zero, invariance gives all missing gauge directions transverse to the slice; hence the slice equation has a multiplier for the averages alone. Holomorphy extends the identities to the full polydisc. They characterize the background response there." SA L10580 ff., remark (k): "(I) is equivalent to the constraint, the Landau condition and \(\mathsf z:=F'(\mathbf H)-K_{\mathbf H}^{\mathsf T}\lambda\in DR(\text{site functions})\) … Therefore \(\mathsf z=0\) on this neighbourhood, and by the identity theorem also on the whole polydisc." SA statement 3 (SA L10296–10305) asserts the gauge identities \(QD\lambda=\bar DQ'\lambda\) and \(\Delta^{\rm W}_{\mathbf U}-\Delta'_\pi[J(\mathbf U)]=\mathsf S^{\mathsf T}\Delta^{\rm W}_{\mathbf U}\mathsf S\), and "On shell, the defect is zero, \(RD^{\mathsf T}\mathsf H_{(1)}=0\)". None of these sketches writes a proof; SA L5802 calls them "substantive response inputs".

### 1.3 Where they are read

- P81 → TH4 (SA Theorem 4; `a3-derivative.md` §§6–7) → ST1 Theorem T → (D4). P81 → BG in ST1 (`st1.md:205`): orbit, axial representative, chart, overlaps, restriction. Proposition REG of `p82-draft.md` reads two ingredients of P81 ((8.2) and §3.8 of `a1-balaban.md`), not P81 as stated here, so there is no cycle (Section 3).
- CRIT → ST1 Theorem D4 (items 1–3 and the regularity step) → Proposition 7 (physical identification) and Proposition DR (drift of earlier reads).

---

## 2. Setting and notation

Binding definitions are those of `st1.md` Definition 1 and of SA (1b)–(1c). I recall what is used.

**Geometry (SA L9593–9599, L9611–9620).** Level-$k$ units, $\eta=L^{-k}$, $\xi_j=L^{j-k}$. A separated sequence $\mathbf B$: $\Omega_0\supset\cdots\supset\Omega_k$, each $\Omega_j$ a union of cubes of side $\mathfrak M\xi_j$, $\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\xi_j$, $\rho=R_1\mathfrak M$. Layers $\mathcal L_j=\Omega_j\setminus\Omega_{j+1}$. Tops: sites of $\mathbb T^{(j)}$ in $\mathcal L_j$. Pillars: the blocks $B^j(y)$ of the tops; SA L9599: "they form a partition of \(\Omega_0\)". A level-0 top is a bare site of $\Omega_0\setminus\Omega_1$; its pillar is the site itself. Rows: $\Gamma_j$ = bonds of $\mathbb T^{(j)}$ in $\Omega_0$ with an endpoint in $\Omega_j$ and none in $\Omega_{j+1}$, interior or outward; no inward bonds (default convention). Nodes = endpoints of rows = tops (SA L9614). $\mathcal G^{\rm res}=\{u:u=\mathbf1$ at the nodes$\}$. **Bare rows** $\Gamma_0$: bonds with both endpoints in $\Omega_0$ and none in $\Omega_1$.

**Two elementary facts used repeatedly.** (G-a) Every bond of $\Omega_0$ either touches $\Omega_1$ or is a bare row. (G-b) A bond within $\infty$-distance $2\eta$ of $\Omega_0^c$ is a bare row, and every plaquette through it has all its bonds bare rows: by separation, $\operatorname{dist}_\infty(\Omega_0^c,\Omega_1)>\rho\eta\ge4\eta$.

**Action, chart, current (SA L9616–9630).** $A_{\Omega_0}$ sums the inner plaquettes (all corners in $\Omega_0$). At a real $U_0$: $F(A)=A_{\Omega_0}(e^{i\eta A}U_0)$ on 1-forms $A$ on the bonds with both ends in $\Omega_0$; $J:=F'(0)$, $\Delta:=F''(0)=\Delta^{\rm W}_{U_0}$; $R_F(A):=F(A)-F(0)-\langle J,A\rangle-\tfrac12\langle A,\Delta A\rangle$, $\mathcal V:=R_F'$. $J^\circ(U)$ is the left-variation gradient of $A_{\Omega_0}$ (the regional current); at a bond whose six plaquettes are inner it equals the full current $J_\eta(U)$ (SA L10137). The plain current $J_+$ of a real $U$ is $J_\eta(U)$ on complete stars and $0$ on incomplete stars (`st1.md` Definition 1). A bond with an incomplete star is within $\eta$ of $\Omega_0^c$, so by (G-b) it is a bare row.

**Pairings.** Fine: $\langle a,b\rangle=\eta^4\sum_b\tfrac12\operatorname{tr}(a(b)b(b))$, bilinear. Rows: the counting pairing $\sum_c\tfrac12\operatorname{tr}$ (`a3-derivative.md` §3; this is the M1 convention). Sites: $\eta^4\sum_x\tfrac12\operatorname{tr}$. Every ${}^{\mathsf T}$ is taken in these fixed pairings. They are nondegenerate.

**Straightened rows (SA L9630–9646).** $\mathcal M^j(e^{i\eta A}U_0)(c)=v_j(c_-)e^{i\mathcal Q^{\rm st}(A)(c)}\mathbf V_0(c)v_j(c_+)^{-1}$; $K_A:=(\mathcal Q^{\rm st})'(A)$; $\widehat Q:=K_0$; $\mathcal Q^{\rm st}=\widehat Q+\mathsf C$, $\mathsf C=\mathsf C^{(2)}+\cdots$. SA's $Q$ is the per-unit-length row, $\widehat Q=\mathsf mQ$ (SA L10139). The reduced datum $\mathsf b(B)$ (SA L9638–9646): $\mathsf b(B)=B$ at interior rows, $e^{i\mathsf b(B)(c)}=e^{iB(c)}\operatorname{Ad}(\mathbf V_0(c))\mathsf v_z(B)$ at an outward row; holomorphic, local, triangular, $\sup|\mathsf b(B)|\le C_{\mathsf b}\sup|B|$. With node factors of each node's own level, `a3-derivative.md` (35) reads
\[
 m(A)(c)=v[A](c_-)\,e^{i\tilde q(A)(c)}\,\mathbf V_0(c)\,v[A](c_+)^{-1},\qquad
 \tilde q(A)=B\iff\mathcal Q^{\rm st}(A)=\mathsf b(B),
 \tag{2.1}
\]
with $D\tilde q_A=\mathcal T_AK_A$, $\mathcal T_A$ invertible (identity plus a part nilpotent of order two), so $\ker D\tilde q_A=\ker K_A$. Checked: `gates/a3-derivative-gate.md` §6.1, "ADVANCE".

**At a bare row** $b\in\Gamma_0$ the zero-fold average is the bond itself, so $\mathcal Q^{\rm st}(A)(b)=\eta A(b)$ exactly. Hence $\mathsf C(A)(b)\equiv0$ and $\widehat Q(b,\cdot)=\eta\,\mathrm{ev}_b$. (This is Y3 L54464–54467 in three dimensions: "On these rows \(\mathcal Q(A)=\xi A\); hence the nonlinear averaging remainder \(\mathsf C\) and all its derivatives vanish.")

**Scalar operators (SA L10140–10145).** $D=D_{U_0}$, $(D\lambda)(b)=\eta^{-1}[\operatorname{Ad}U_0(b)\lambda(b_+)-\lambda(b_-)]$; $\Delta_{\mathbf U}$ the scalar Laplacian; $Q'$ the pillar mean, site functions → tops; $a$ the fixed mass weights; $G'=(\Delta_{\mathbf U}+Q'^{\mathsf T}aQ')^{-1}$; $R=1-G'Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G'$; $\lambda_A:=G'RD^{\mathsf T}A$; $\Pi:=1-DG'RD^{\mathsf T}$ (SA's $\mathsf S$; I write $\Pi$ to free the letter, as Y3 does). Slice $\mathrm{Sl}:=\ker(RD^{\mathsf T})$.

**Vector operators (SA L10146–10160, L10200).** With $\hat a:=\mathsf m^{-1}a\,\mathsf m^{-1}$ on rows, so that $Q^{\mathsf T}aQ=\widehat Q^{\mathsf T}\hat a\widehat Q$:
\[
\begin{gathered}
 G_0=(\Delta+DRD^{\mathsf T}+\widehat Q^{\mathsf T}\hat a\widehat Q)^{-1},\quad
 G=(G_0^{-1}-\Delta'_\pi[\mathbf J])^{-1},\quad
 G_1=(G^{-1}-\Pi^{\mathsf T}\Delta^{(2)}[\ell^{\mathsf T}\mathbf J]\Pi)^{-1},\\
 \ell=G\widehat Q^{\mathsf T}\Sigma,\ \ \Sigma=(\widehat QG\widehat Q^{\mathsf T})^{-1},\qquad
 \ell_1=G_1\widehat Q^{\mathsf T}(\widehat QG_1\widehat Q^{\mathsf T})^{-1},\qquad
 \mathfrak G=G_1-G_1DRD^{\mathsf T}G_1-\ell_1\widehat QG_1 .
\end{gathered}\tag{2.2}
\]
$\ell,\ell_1$ are SA's $H,H_1$ (raw-row normalization, SA L10212: "slanted \(H,H_1\) stand for \(\mathsf H\mathsf m^{-1},\mathsf H_1\mathsf m^{-1}\)"). $\Delta^{(2)}[\zeta]$ is the symmetric operator with $\langle A,\Delta^{(2)}[\zeta]A\rangle=2\langle\zeta,\mathsf C^{(2)}(A)\rangle_{\rm row}$ (SA L10156). $\Delta'_\pi[\mathbf J]$ is the explicit current continuation (SA L10185–10190):
\[
 \langle A,\Delta'_\pi[\mathbf J]C\rangle=\tfrac12\big\langle
 i[\lambda_A,C]+i[\lambda_C,A]-i[A,\lambda_C^+]-i[C,\lambda_A^+]
 -i[\lambda_A,D\lambda_C]-i[\lambda_C,D\lambda_A],\ \mathbf J\big\rangle,
 \tag{2.3}
\]
with $\lambda^+(b)=\operatorname{Ad}U_0(b)\lambda(b_+)$ and unsuperscripted $\lambda$ at $b_-$. Put $\Delta_\pi:=\Delta-\Delta'_\pi[\mathbf J]$, $\Delta_1:=G_1^{-1}-DRD^{\mathsf T}-\widehat Q^{\mathsf T}\hat a\widehat Q$, and $\mathcal K:=\ker\widehat Q\cap\mathrm{Sl}$.

**Notation clashes resolved.** (1) SA's $\mathsf S=1-DG'RD^{\mathsf T}$ is $\Pi$ here; Y3's $S=(QGQ^{\mathsf T})^{-1}$ is $\Sigma$ here. (2) SA's $H,H_1$ are $\ell,\ell_1$ here; $\mathbf H$ is always the response field. (3) $\kappa$ in `a3-derivative.md` is the reference curvature size $\kappa_{\rm A3}$; IN1's decay rate is $\kappa_{\rm IN}$ (as `p82-draft.md` §2.3). (4) The letter $R_1M_1$ denotes two different lengths in `a1-balaban.md` §6 and in the outline (Section 4.8).

---

## 3. Imports

Each import is a statement of another library file. Its check record is quoted. Nothing below counts as more than its label.

**(I-A1) Balaban's critical orbit, ported.** `a1-balaban.md` §§3.5–9, by Codex: on every separated sequence of the outline's default determining set (inward bonds omitted), with the actual contour-mean averages and straightened rows (§7, §8: "The actual-row constructions of Section 7 supply the hypotheses of Sections 4–6"), conditional on F0:
- (8.2), `a1-balaban.md:2426–2433`: "conditional on F0, the default constraint problem has one regular critical residual orbit, with \(|\partial U(p)-1|\le B\varepsilon_1\eta^2\mathsf L(p)^{-2},\ |J(U)(b)|\le B\varepsilon_1\mathsf L(b)^{-3}\), and a larger uniqueness radius fixed before the depth and volume."
- §9.1, (9.1)–(9.2), `a1-balaban.md:2452–2546`: the chart contraction on $\|B\|_\infty<r_B$, its holomorphic limit, the unique axial representative ("This proves existence and uniqueness of the representative"), conjugators of norm and inverse norm at most $\exp(C\|B\|_\infty/(1-L^{-1}))$, and $M_{\mathbf B}\Phi_{V_0}(B)=e^{iB}V_0$, $r(\Phi_{V_0}(B))\le C(\varepsilon_1+\|B\|_\infty)$; "On real overlaps the canonical representatives agree by orbit uniqueness and the unique axial gauge."
- §9.2, (9.3), `a1-balaban.md:2547–2612`: exact restriction to a separated subsequence $\Omega'_q\subset\Omega_q$.
- G99.D, `a1-balaban.md:198–207`: "the equation replacing \(RD^*A=0\) by \(RD^*A=f\) … has a unique small gauge solution … Consequently a slice critical point is critical with respect to all constraint-preserving variations."

Check record: Claude, `gates/a1-balaban-gate.md:8`: "**Result: no step fails.** Every gated section is ADVANCE (9.3 is CORRECT-NO-ADVANCE), conditional on the flat input F0." Its D1 (F0 provenance and level-0 seam) is closed by (I-F0). Its D2 (order of choice) is resolved in Section 4.8. Its D3 (one identity-theorem sentence for the second-order part of (9.1)) does not touch what P81 uses. Its positive finding (c), `gates/a1-balaban-gate.md:143`: "The complex regularity of Phi on the datum polydisc, which the a3-derivative gate kept inside P81, is supplied by (9.2)."

**(I-F0) The flat package.** `flat-port.md` (Codex), F0 of `a1-balaban.md` (3.21)–(3.23) with its energy and Gram forms in the default convention, level-0 seam included. Check record: Claude, `gates/flat-port-gate.md:8`: "first failing step none", and line 50: "Row 81's F0 is discharged, including the level-0 seam check of `gates/a1-balaban-gate.md` D1." FP1 status [C] (`ym4-assembly.md:98`).

**(I-REG) The critical reference is in the regular class.** `p82-draft.md` Proposition REG (§3 and §11): for $\rho\ge\max\{\rho_P,4LW_\natural+2L\}$ and $C_{\rm reg}M'\varepsilon_1\le a_{\rm reg}$, every cube $Z$ of side $c_{\rm reg}M_P\xi_j$ with $Z\subset\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})$ carries a real gauge with $U_0^g=e^{i\eta A}$ on the bonds of $Z$ and $\xi_j|A|+\xi_j^2|\nabla A|\le\alpha:=C_{\rm reg}M'\varepsilon_1$, $\nabla$ the ordinary difference. Constants depend on $L$ only. It reads only (I-A1)'s (8.2) and Balaban's Proposition 6 as ported in `a1-balaban.md` §3.8 ((I6), (I7) of `p82-draft.md`). Check record: `p82-draft.md` §11: "This is `a3-close.md` §1 (Claude; checked by Codex in `gates/a3-close-meet-gate.md` §A, 'ADVANCE as an implication', first failing step none)".

**(I-6) The Landau identification lemmas.** `a3-derivative.md` §6.1 (Claude), as repaired by Codex in `gates/a3-derivative-gate.md` §6.1:
- (2.1) and the triangular reduced datum: "ADVANCE".
- Lemma 6.1, $\frac d{dt}v[A_t](y)|_{t=0}=i(\chi(y)-(Q'\chi)(y))$ along the pure gauge $e^{i\eta A_t}U_0=U_0^{e^{it\chi}}$, at every node: "ADVANCE".
- Lemma 6.2 as repaired ("Repair of Lemma 6.2 (proved)"): if $A$ is in the chart, $K_A$ onto, and $e^{i\eta A}U_0$ critical for its datum, then $F'(A)=K_A^{\mathsf T}\omega$ for exactly one $\omega$.
- Lemma 6.3 (`a3-derivative.md:409`): given $\Phi$ as in P81(b), there is a real neighbourhood $N$ of $0$ and a real-analytic pair $(H_N,u_N)$, value $(0,\mathbf1)$ at $0$, with $\Phi(B)=(e^{i\eta H_N}U_0)^{u_N}$, $RD^{\mathsf T}H_N=0$, $u_Nv[H_N]=\mathbf1$ at the tops; unique near $(0,\mathbf1)$. Gate: "ADVANCE, conditional on P81 and the stated scalar isomorphism". The gate proves that isomorphism: "\(Q'\) is onto: its pillars are disjoint and the coefficient of the top in each average is a nonzero scalar times the identity. On \(\ker Q'\), \(R\Delta=\Delta\) … Injectivity follows from positivity of the real site Laplacian."
- The spanning-forest repair (gate, §6.1): "Use **one rooted tree per connected component**, rooted at a top."

**(I-OPS) The six propagators at the real critical reference.** `a1-balaban.md` §3.9, conditional on F0: at a real regular reference the curved operators $G',G_0,G,G_1$ and the Gram inverses $(\widehat QG_{(1)}\widehat Q^{\mathsf T})^{-1}$ exist, are symmetric (real pairs: positive), with first-order and Hölder bounds. Gate: "**3.9 (CMP 99b, curved from flat): ADVANCE, conditional on F0.**" SA statement 4 (SA L10307) asserts the same: "At every regular pair all the inverses exist … At real pairs \(\mathsf G_0,\mathsf G,\mathsf G_1>0\)".

**(I-UNQ) The chart system at $s\equiv\mathbf1$.** `a1-balaban.md` §4, (4.1) and (4.5), and §9.1: the straightening fixed point $\mathcal D(A')=\mathsf C(A'-\ell\mathcal D(A'))$ is unique in a fixed ball $|X|\le r/B_0$; the slice equation $A_1=-\mathfrak G_1J-\mathfrak G_1V'(A_1+\ell_1B)$ has a unique solution in a fixed ball $\|A_1\|_X\le r_*$, holomorphic in $B$ on $\|B\|_\infty<r_B$ ("The larger uniqueness ball was fixed before the smaller existence ball"). Gate: "**4 (CMP 102 Propositions 2-6): ADVANCE, conditional on Section 3 and F0.**" Section 5.7 shows this is the $s\equiv\mathbf1$ instance of (R9).

**(DR1) Resummation at $s\equiv\mathbf1$ (a property of the DR specification).** The decoupled maps of DR are holomorphic in the cube parameters, and at $s\equiv\mathbf1$ they equal the undecoupled maps of the fixed system. This is how a decoupled walk expansion is defined: at $s\equiv\mathbf1$ every factor $s^\omega$ equals one (Y3 L33440–33442: "The complete expansions therefore sum to the operators of \cref{I-88-53}"). Together with regional consistency (`st1.md` Definition 5) it says that at the physical locus the regional response is the response of the fixed system. ST1 imports DR; DR1 is part of DR, not proved here.

**Dependency check: no cycle.** (I-F0) reads no curved statement. (I-A1) reads (I-F0) only. (I-REG) reads (I-A1)'s (8.2) and §3.8 only. (I-6) reads P81(b) and finite-dimensional algebra. Theorem P81 reads (I-A1), (I-F0), (I-REG). Theorem CRIT reads P81, (I-6), (I-OPS), (I-UNQ), DR1. P82° (`p82-draft.md`) reads (I-A1)'s (8.2) and §3.8 but not P81 or CRIT. So the chain F0 → A1 → {REG, P81} → CRIT is linear.

---

## 4. P81

### 4.1 The statement

**Theorem P81 (the critical background; BG1(2); SA Theorems 1, 3 first paragraph, 6(b)).** [proved here, as an implication from (I-A1), (I-F0), (I-REG)] Fix $L$ and the constants of rows 1–7 of `c4-order.md`. Let $\mathbf B$ be a separated sequence with cube size $\mathfrak M$ and gap $\rho=R_1\mathfrak M$ above the floors of Section 4.8, of any depth, mesh, volume and region shape above the torus floors, with the default determining set and the outline's actual averages. Then:

(a) *Orbit.* For every real $\varepsilon_1$-regular datum $\mathbf V$ with $\varepsilon_1\le\bar\varepsilon$, the critical configurations of $C(\mathbf B,\mathbf V)$ that are regular at the radius $a_0$ form exactly one nonempty $\mathcal G^{\rm res}$-orbit $U_{\mathbf B}(\mathbf V)$. Every element obeys
\[
 |\partial U(p)-\mathbf1|\le B\varepsilon_1\eta^2\mathsf L(p)^{-2},\qquad |J(U)(b)|\le B\varepsilon_1\mathsf L(b)^{-3}.
 \tag{4.1}
\]
Exactly one element $U^\circ(\mathbf V)$ is in the axial gauge outside the nodes.

(b) *Chart.* For every such $\mathbf V_0$ there is exactly one holomorphic map $\Phi=\Phi_{\mathbf V_0}$ on $\mathcal B=\{B:\mathbf B\to\mathfrak g^c,\ \|B\|_\infty<r_B\}$ with $\Phi(B)=U^\circ(e^{iB}\mathbf V_0)$ for real $B$. On all of $\mathcal B$: $M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0$, $\Phi(0)=U^\circ(\mathbf V_0)$, and
\[
 |\partial\Phi(B)(p)-\mathbf1|\le C_\Phi(\varepsilon_1+\|B\|_\infty)\eta^2\mathsf L(p)^{-2},\qquad
 |J(\Phi(B))(b)|\le C_\Phi(\varepsilon_1+\|B\|_\infty)\mathsf L(b)^{-3}.
 \tag{4.2}
\]
In particular $\Phi(B)$ is real, regular and critical for real $B$. For $w\in\mathcal G^{\rm res}$ real, $\Phi^w(B):=\Phi(B)^w$ has the same properties with $\Phi^w(0)=U^\circ(\mathbf V_0)^w$, except axiality.

(c) *Local gauges on row carriers.* For every row $c\in\Gamma_j$, $j\ge1$, there is a real gauge $g$ on its carrier $S_c$ (the bonds of the double block $B^j(c_-)\cup B^j(c_+)$) with $U^\circ(\mathbf V)^g=e^{i\eta A}$ on $S_c$ and
\[
 \xi_j|A|\le\kappa,\qquad \xi_j^2|\nabla A|\le\kappa,\qquad |\partial U(p)-\mathbf1|\le\kappa\eta^2\xi_j^{-2}\ (p\subset S_c),\qquad
 \kappa:=L^2\max\{C_{\rm reg}M',B\}\,\varepsilon_1 .
 \tag{4.3}
\]
For $j=0$ the carrier is one bond and $A=0$ in a suitable gauge.

(d) *Restriction.* If $\mathbf B'$ is a separated sequence with $\Omega'_q\subset\Omega_q$ for every $q$, each $\Omega'_q$ a union of level-$q$ blocks, and $U\in U_{\mathbf B}(\mathbf V)$, then $U|_{\Omega'_0}\in U_{\mathbf B'}(M_{\mathbf B'}(U|_{\Omega'_0}))$, and its datum is $CL^2\varepsilon_1$-regular. This applies to the subordinate erosion towers and meets of ST1 (Lemma 81.4).

(e) *Overlaps.* For real $\mathbf V,\mathbf V'$ as in (b) and $D$ with $\|i^{-1}\operatorname{Log}(D\mathbf V^{-1})\|_\infty<\delta_B$, $\|i^{-1}\operatorname{Log}(D\mathbf V'^{-1})\|_\infty<\delta_B$, $\delta_B\le r_B/40$:
\[
 \Phi_{\mathbf V}\big(i^{-1}\operatorname{Log}(D\mathbf V^{-1})\big)=\Phi_{\mathbf V'}\big(i^{-1}\operatorname{Log}(D\mathbf V'^{-1})\big).
 \tag{4.4}
\]

(f) *Uniformity.* $B,C_\Phi,a_0,\bar\varepsilon,r_B$ and $\kappa/\varepsilon_1$ depend on $L$ and the fixed flat and local data only. They are independent of the depth, the mesh, the volume, the regions, the datum, of $M$ and of $\bar\kappa$.

This is P81 "at its actual strength" in the sense of `gates/a3-derivative-gate.md:224`: orbit and uniqueness (a); local gauges and current bounds (a), (c); holomorphic $\Phi$ with complex regularity and a uniform chart radius (b). It is also BG's orbit, chart, overlap and restriction clauses in `st1.md:205`.

### 4.2 Tests for a counterexample, run first

The target failure is a separated sequence on which some constant of (a)–(c) must grow with the depth, the volume or the shape.

**T1 (flat holonomy).** A flat connection with nontrivial holonomy around a torus cycle has every plaquette $\mathbf1$ and is not a gauge of $\mathbf1$. Every test loop of its datum is contractible, so its datum is $0$-regular. (a) asserts an orbit, not a field, and uniqueness of orbits under $\mathcal G^{\rm res}$; the orbit of such a field is one orbit. (c) asks gauges only on carriers of diameter $2\xi_j$, which are simply connected. No counterexample. (`intrinsic-dom.md` §2's pure-gauge family $U_t$ is the reason (a) speaks of orbits.)

**T2 (depth).** A reset that loses $CL^3$ per level would give $e^{Ck}$. (I-A1)'s two resets ((8.1), and the reset of the enlarged datum class) are depth-uniform; the gate redid both ("Both resets of Section 8 are depth-uniform"). No counterexample.

**T3 (complex gauge at bare sites).** For complex $B$, a Landau representative's gauge $u_B$ at non-node sites is not controlled uniformly (`gates/a3-derivative-gate.md`, 7.6: "The unbounded complex bare-site gauge cannot be dropped from curvature/current value norms"). (b) claims (4.2) only for the axial representative, whose conjugators are bounded by $\exp(C\|B\|/(1-L^{-1}))$ ((I-A1) §9.1). No claim is made for other representatives at complex $B$. No counterexample.

**T4 (disconnected $\Omega_0$).** SA allows any $\Omega_0$ (SA L9599: "no condition is imposed on the shape or the connectivity"). Every statement of (a)–(e) is a statement per site, bond or row; the axial recursion runs pillar by pillar; nothing needs connectivity. No counterexample.

### 4.3 Proof of (a)

(I-A1) (8.2) gives the orbit, its nonemptiness, uniqueness among regular critical orbits in a fixed larger neighbourhood, and (4.1). Take $a_0$ to be that uniqueness radius. (I-A1) §9.1 gives the axial element: "At a node keep its gauge value equal to 1. In the block below a fixed parent, the equation fixing a contour to its reference value determines the child's gauge by multiplication and inversion of that contour transport. Repeat down the pillars. Every nonnode has a unique parent; no gauge value is assigned twice." With the mean contour variable this is SA's remark after Theorem 1 (SA L9669–9676: "each orbit again has exactly one element in it"); with the comb it is SA L9667. Both satisfy the three properties SA L9670–9673 lists. (I-A1) §9.1 states that either works. $\square$

### 4.4 Proof of (b)

**Lemma 81.2 (the chart).** [proved here from (I-A1)] (i) The map $\Phi_{\mathbf V_0}$ of (I-A1) §9.1 is holomorphic on $\mathcal B$, satisfies $M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0$ and (4.2), and equals $U^\circ(e^{iB}\mathbf V_0)$ at real $B$. (ii) It is the only holomorphic map on $\mathcal B$ with the last property. (iii) For real $w\in\mathcal G^{\rm res}$, $\Phi^w$ is holomorphic, $M_{\mathbf B}\Phi^w(B)=e^{iB}\mathbf V_0$, and $\Phi^w(B)$ is real, regular and critical at real $B$, with (4.2) at real $B$.

*Proof.* (i) Holomorphy and the datum identity are (9.2). For (4.2): (9.2) states $r(\Phi_{V_0}(B))\le C(\varepsilon_1+\|B\|_\infty)$, where for complex fields $r$ denotes "the same two matrix-norm inequalities" (`a1-balaban.md:2521–2524`); this is (4.2) with $C_\Phi:=C$. The gate's positive finding (c) confirms the conjugator bound behind it. At real $B$ the chart solution is real (every ingredient of the contraction is real on real arguments, so the iterates are real), slice critical, hence critical by G99.D; it is regular by (4.2); so it lies in $U_{\mathbf B}(e^{iB}\mathbf V_0)$ by (a); and it is axial by construction. By uniqueness of the axial element, $\Phi(B)=U^\circ(e^{iB}\mathbf V_0)$. (This uses that $e^{iB}\mathbf V_0$ is $\bar\varepsilon$-regular for real $B\in\mathcal B$, which is SA Theorem 3's choice of $\varepsilon_1,r_B$, SA L9693–9694.)

(ii) Let $\Psi$ be holomorphic on $\mathcal B$ with $\Psi(B)=U^\circ(e^{iB}\mathbf V_0)$ at real $B$. Then $\Psi-\Phi$ is holomorphic on the polydisc $\mathcal B$, which is convex, hence connected, and vanishes on the real points of $\mathcal B$, a nonempty open subset of $\mathbb R^N$. At a real point all real partial derivatives of $\Psi-\Phi$ vanish; for a holomorphic function these are its complex partial derivatives, so its power series there is zero and it vanishes near that point. The set where all derivatives vanish is open and closed in $\mathcal B$, hence all of $\mathcal B$. This is the identity theorem in the form used throughout (IT).

(iii) $w$ is real and equals $\mathbf1$ at the nodes. The averages are covariant, $\mathcal M^q(U^u)=(\mathcal M^qU)^{u|_{\mathbb T^{(q)}}}$ (AV-it, `st1-draft2.md` §3), and the rows have nodes as endpoints, so $M_{\mathbf B}(U^w)=M_{\mathbf B}(U)$. Gauge transformation maps $C(\mathbf B,\mathbf V)$ onto itself and preserves the inner action, so it preserves criticality. Unitary conjugation preserves the plaquette and current norms in (4.2). $\square$

### 4.5 Proof of (c): local gauges on row carriers

**Lemma 81.3.** [proved here from (I-REG), (a) and separation] Assume $\rho\ge\rho_{81}:=2L(c_{\rm reg}M_P+4)$ and the hypotheses of (I-REG). Let $c\in\Gamma_j$, $j\ge1$, and $S_c$ its carrier. Then $S_c$ lies in a cube $Z$ of side $c_{\rm reg}M_P\xi_{j'}$ with $Z\subset\Omega_0\cap(\mathcal L_{j'}\cup\mathcal L_{j'+1})$, for $j'=j-1$ or $j'=j$. Consequently (4.3) holds.

*Proof.* *Size.* $S_c$ lies in the box $B^j(c_-)\cup B^j(c_+)$, of $\infty$-diameter at most $2\xi_j$. Since $c_{\rm reg}=c_LL$ and $c_LM_P\ge2$ (p82 row 4), $2\xi_j\le c_{\rm reg}M_P\xi_{j-1}\le c_{\rm reg}M_P\xi_j$. So a cube of either side can contain $S_c$.

*$S_c$ misses $\Omega_{j+1}$ by at least $\xi_j/2$.* $\Omega_{j+1}$ is a closed union of level-$(j+1)$ cubes, whose corners are sites of $\mathbb T^{(j+1)}\subset\mathbb T^{(j)}$. A site of $\mathbb T^{(j)}$ outside it has $\infty$-distance at least $\xi_j$ from it. The endpoints of $c$ are such sites. Their blocks have half-side $\xi_j(L-1)/(2L)<\xi_j/2$.

Let $y$ be the endpoint of $c$ in $\Omega_j$. It lies in its own block, so $y\in S_c$ in the sense that $S_c$ contains bonds at $y$. Put $s:=c_{\rm reg}M_P\xi_{j-1}$. A cube $Z$ of side $s$ containing $S_c$ contains $y$, so every point of $Z$ is within $\infty$-distance $s$ of $y$.

*Case A: $\operatorname{dist}_\infty(y,\Omega_{j+1})>s$.* Take $Z$ of side $s$ containing $S_c$. Then $Z\cap\Omega_{j+1}=\varnothing$. By separation, $\operatorname{dist}_\infty(y,\Omega_{j-1}^c)>\rho\xi_{j-1}\ge s$, since $\rho\ge\rho_{81}\ge c_{\rm reg}M_P$. So $Z\subset\Omega_{j-1}\setminus\Omega_{j+1}=\mathcal L_{j-1}\cup\mathcal L_j$, and $Z\subset\Omega_0$. Here $j'=j-1$.

*Case B: $\operatorname{dist}_\infty(y,\Omega_{j+1})\le s$.* The other endpoint $z$ of $c$ is within $\xi_j$ of $y$. If $c$ were outward, then $z\notin\Omega_j$ and $\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})\le s+\xi_j=(c_{\rm reg}M_P/L+1)\xi_j<\rho\xi_j$, contradicting separation. So $c$ is interior. Every point of $S_c$ is within $s+2\xi_j$ of $\Omega_{j+1}$, so its distance to $\Omega_j^c$ exceeds $\rho\xi_j-s-2\xi_j=(\rho-c_{\rm reg}M_P/L-2)\xi_j\ge c_{\rm reg}M_P\xi_j$, by $\rho\ge\rho_{81}$. Take $Z$ of side $c_{\rm reg}M_P\xi_j$ containing $S_c$; every point of $Z$ is within $c_{\rm reg}M_P\xi_j$ of $S_c$, so $Z\subset\Omega_j$. By the previous step $S_c\subset\Omega_{j+1}^c$, and $\operatorname{dist}_\infty(\Omega_{j+1}^c,\Omega_{j+2})>\rho\xi_{j+1}\ge c_{\rm reg}M_P\xi_j$, so $Z\cap\Omega_{j+2}=\varnothing$. Thus $Z\subset\mathcal L_j\cup\mathcal L_{j+1}$ and $Z\subset\Omega_0$. Here $j'=j$.

Cases A and B cover all $c$.

*The bounds.* (I-REG) on $Z$ gives $U^\circ(\mathbf V)^g=e^{i\eta A}$ with $\xi_{j'}|A|+\xi_{j'}^2|\nabla A|\le\alpha$. Since $\xi_j\le L\xi_{j'}$: $\xi_j|A|\le L\alpha$, $\xi_j^2|\nabla A|\le L^2\alpha$. A plaquette $p\subset S_c$ has $\mathsf L(p)\ge\xi_{j-1}=\xi_j/L$, so (4.1) gives $|\partial U(p)-\mathbf1|\le B\varepsilon_1L^2\eta^2\xi_j^{-2}$. With $\kappa$ as in (4.3) all three bounds hold. For $j=0$, $S_c=\{c\}$; the gauge $g(c_+)=\mathbf1$, $g(c_-)=U(c)^{-1}$ makes $U^g(c)=\mathbf1$, and no plaquette lies in $S_c$. The torus floors (SA L9658: cubes on which gauges are chosen are shorter than half the torus) hold for $Z$ by the first floor. $\square$

**Remark.** `a3-derivative.md:56` writes $\kappa=C_L\mathfrak M\bar\varepsilon$. Lemma 81.3 gives the smaller $\kappa=C(L)\varepsilon_1$: the REG cubes have side $c_{\rm reg}M_P\xi_j$, not $\mathfrak M\xi_j$ (`p82-draft.md` §13, remark 2). Either value is allowed by Theorem 4's ceiling $\bar\varepsilon\le c(L)/\mathfrak M$ (SA L9734). `a3-derivative.md` §4.1 uses only that $\kappa$ is small and fixed before the depth. The "current bound" of `a3-derivative.md:56` is the second half of (4.1).

### 4.6 Proof of (d), and the subordinate sequences of ST1

(I-A1) (9.3) is (d) for a separated subsequence with $\Omega'_q\subset\Omega_q$; its proof (`a1-balaban.md` §9.2) uses block alignment of the members ("by alignment of the region with the block partition") and the first gap of $\mathbf B'$; the datum radius $CL^2\varepsilon_1$ comes from "The converse averaging bound gives datum radius at most \(CL^2\varepsilon_1\)". The gate's repair of the base case of the similar Lemma 10.2 (`gates/a3-derivative-gate.md`, "At level zero, *every* bond in \(W\) with no endpoint in \(\Omega'_1\) is a determining row and is fixed") is already the argument of (9.3), whose level-zero step reads "At level zero the old fixed links do not touch \(\Omega_1\), whereas every varying link touches \(\Omega'_1\subset\Omega_1\)".

**Lemma 81.4 (towers and meets).** [proved here] The following are separated sequences in the sense of Theorem P81, so (a)–(e) hold on them with the same constants: (i) memberwise meets of separated sequences; (ii) a tower of the first erosion rule; (iii) a tower of the second rule; (iv) the truncation of any of them at a depth $n$.

*Proof.* (i) `st1.md` Lemma 2: "Meets of separated sequences are separated with the smaller gap." Each member of a meet is an intersection of unions of level-$j$ $\mathfrak M$-cubes of aligned partitions, hence such a union. (ii) SA L9650–9651: "The first uses cubes of side \(\mathfrak M\) in the unit of their own level, with a gap exceeding \(\rho\) in the unit of the outer member." This is the definition of separation. (iii) SA L9651–9652: "The second uses cubes of side \(M_1'\) and requires a gap no smaller than \(M_1'\), measured in the unit of the inner member." $M_1'\ge R_1M_1=\rho$ (SA L10212: "\(M_1'\ge R_1M_1\), which is the second cube size"), and $M_1'$ is a power of $L$ divisible by $\mathfrak M$, so an $M_1'$-cube is a union of $\mathfrak M$-cubes, and a gap $M_1'\xi_{j+1}\ge\rho\xi_{j+1}>\rho\xi_j$. (iv) Truncation sets $\Omega_q=\varnothing$ beyond depth $n$; separation is a condition on consecutive members only. Memberwise inclusion in the ambient sequence holds in all four cases by construction, so (d) applies to the ambient background restricted to them. $\square$

Whether ST1's actual towers and meets satisfy these rules is GEO's statement (`st1.md:204`), not P81's.

### 4.7 Proof of (e): agreement on overlaps

**Corollary 81.5.** [proved here from (b)] Assume $r_B\le1/16$ (a ceiling, decrease $r_B$ if needed). Then (4.4) holds.

*Proof.* Write $X=D\mathbf V^{-1}$, $X'=D\mathbf V'^{-1}$; $\|X-\mathbf1\|,\|X'-\mathbf1\|\le e^{\delta_B}-1\le2\delta_B$. Then $\mathbf V'\mathbf V^{-1}=X'^{-1}X$ is unitary and within $2\delta_B+2\delta_B(1+2\delta_B)\le5\delta_B$ of $\mathbf1$. Its series logarithm $B_0:=i^{-1}\operatorname{Log}(\mathbf V'\mathbf V^{-1})$ is real (traceless Hermitian) with $\|B_0\|\le5\delta_B/(1-5\delta_B)\le6\delta_B\le r_B/6$; the traceless branch is selected by the determinant, as in `st1.md` Lemma 4. On $\mathcal B'=\{\|B\|_\infty<r_B/2\}$ put $\beta(B):=i^{-1}\operatorname{Log}(e^{iB}e^{iB_0})$, bond by bond. By `st1.md` (25) with $|iB|+|iB_0|\le\tfrac23r_B\le\tfrac14$: $\|\beta(B)\|\le\tfrac23r_B+12(\tfrac23r_B)^2<r_B$. So $\Psi_1(B):=\Phi_{\mathbf V'}(B)$ and $\Psi_2(B):=\Phi_{\mathbf V}(\beta(B))$ are holomorphic on the polydisc $\mathcal B'$. For real $B$, $\beta(B)$ is real and $e^{i\beta(B)}\mathbf V=e^{iB}\mathbf V'$, so both equal $U^\circ(e^{iB}\mathbf V')$ by (b). By (IT), $\Psi_1=\Psi_2$ on $\mathcal B'$. Now take $B:=i^{-1}\operatorname{Log}X'$, $\|B\|<\delta_B<r_B/2$. Then $e^{i\beta(B)}=X'\mathbf V'\mathbf V^{-1}=X$, and both $\beta(B)$ and $i^{-1}\operatorname{Log}X$ lie in the ball $\|\cdot\|<r_B<1$ on which $\exp$ is injective with inverse $\operatorname{Log}$. So $\beta(B)=i^{-1}\operatorname{Log}X$ and $\Psi_1(B)=\Psi_2(B)$ is (4.4). $\square$

So the intrinsic tube map $T_e(D)=\Phi_V(i^{-1}\operatorname{Log}(DV^{-1}))$ of `st1.md` (15) does not depend on the centre $V\in\mathcal R_e$ and is holomorphic on $\mathcal T_e$. This is the common-branch clause of BG ("agrees on the specified overlaps", `st1.md:205`).

### 4.8 Constants and the order of choice

The order of `c4-order.md`: rows 3 ($L$, flat constants), 4 (local inverse/gauge constants $B_0,B_1,B_3$, collar/reset widths $W$; $m_w,c_{\rm reg},\alpha_*$), 5 (rates), 6 ($M_1=\mathfrak M\to R_1\to\rho$), 7 (A1 constants $C_\downarrow,B$, uniqueness/reset radii $a_5,a_0,a_1,\bar\varepsilon,r_B$).

**The clash in `a1-balaban.md` §6, resolved.** That section writes "Choose \(R_1M_1\) sufficiently large that \(B_3e^{-aR_1M_1/2}\le1/2\)" (`a1-balaban.md:1265–1266`) and calls it "the localization length \(R_1M_1\)" (`a1-balaban.md:1344`). The gate (D2, `gates/a1-balaban-gate.md:128–137`) requires the outline's gap to exceed "a multiple, depending on L, of the reset length R_1M_1 of (163) … So CMP 102 (1) needs roughly R >= 6L R_1". If "$R_1M_1$" in §6 meant the outline's gap $\rho=R_1\mathfrak M$, the condition $\rho\ge6L\rho$ would be unsatisfiable. It does not mean that. The reset length is Balaban's localization length: the distance of the artificial boundary of the localized problem from its centre. Call it $\ell_R$. Its only requirement is $B_3e^{-a\ell_R/2}\le1/2$, with $a$ the F0 rate and $B_3=72d^3L^3B_0S_*$, where $S_*$ is bounded uniformly once the gap of the auxiliary sequence exceeds the floor $\rho_{\rm sum}$ of (3.13) (`a1-balaban.md:1267–1268`: "There is no circular choice: \(S_*\) was bounded uniformly over every gap above its previously fixed minimum"). So $\ell_R$ is a row-4 constant ("collar/reset widths $W$" of `c4-order.md` row 4), depending on $L$ and F0 only. The outline's gap then needs $\rho\ge6L\ell_R$, a lower bound by an earlier number, chosen at row 6. This is the same kind of clash as `p82-draft.md` §2.3 item 3 ($W_\natural$), and is resolved the same way. The mathematics of (I-A1) is unchanged.

| Constant | Source | Depends on | Row | Before $\kappa_{\rm IN}$ | Free of $M$, $\bar\kappa$ |
|---|---|---|---|---|---|
| F0 constants, rate $a$ | (I-F0) | $L$ | 3 | yes | yes |
| $B_0,B_1,B_3$, $S_*$, $\ell_R$ | (I-A1) §§3.8, 6 | $L$, F0 | 4 | yes | yes |
| $M_P,c_{\rm reg},W_\natural$ | (I-REG) | $L$ | 4 | yes | yes |
| $\rho_{\rm sum},\rho_P$, $6L\ell_R$, $4LW_\natural+2L$, $\rho_{81}=2L(c_{\rm reg}M_P+4)$ | floors on $\rho$ | earlier rows | 6 (lower bounds) | yes | yes |
| $\mathfrak M=M_1$ | power of $L$, $M_P\mid\mathfrak M$ | earlier rows | 6 | yes | yes |
| $B$, $C_\downarrow$, $a_5,a_0,a_1,\bar\varepsilon,r_B$ | (I-A1) §8, §9.1 | rows 3–6 | 7 | yes | yes |
| $C_\Phi$ | (9.2) | rows 3–7 | 7 | yes | yes |
| $C_{\rm reg},a_{\rm reg},M'$ | (I-REG) | $L$, $B$ | 4–7 | yes | yes |
| $\kappa/\varepsilon_1=L^2\max\{C_{\rm reg}M',B\}$ | Lemma 81.3 | $L$, $B$ | 7 | yes | yes |
| $\delta_B\le\min(1/40,r_B/40)$, $r_B\le1/16$ | Corollary 81.5, `st1.md` (15) | $r_B$ | 7 | yes | yes |

No constant of P81 reads $\kappa_{\rm IN}$ (row 8), $\bar\kappa$ (row 9) or $M$ (row 12). The construction size $M$ does not occur in any P81 statement: Balaban's local-gauge cube of side $M$ in (2.2) and §6 of `a1-balaban.md` is a local length chosen there with $M\varepsilon_0$ small; P81(c) does not use it, since Lemma 81.3 uses the REG cubes of side $c_{\rm reg}M_P\xi_j$. P81 involves no decoupling polydisc, so $\bar\kappa$ cannot enter.

### 4.9 Four dimensions

Balaban's CMP 98–102 are four-dimensional papers. (I-A1) is written with $d$ and evaluated at $d=4$ (its counts: "at most six adjacent plaquettes in dimension four", `a1-balaban.md:96–97`; "$4d^2\alpha_0$", "$72d^3L^3B_0S_*$"). (I-F0) is four-dimensional (FP1). Lemma 81.3 and Corollary 81.5 use only $\infty$-distances and matrix series, which do not depend on the dimension. The three-dimensional account Y3 is not used for P81.

### 4.10 What P81 does not include

1. The pointed-core admission clause (10.2) of `a1-balaban.md` §10. `wf-c.md` Theorem A treats it on the box-first route. It is not a premise of TH4.
2. The variant with kept inward bonds (`a1-balaban.md:2722–2729`). The consumers use the default.
3. Regularity of non-axial representatives at complex $B$ (T3).
4. Whether a given datum of ST1 is $\varepsilon_1$-regular. That is AV-conv and GEO in ST1.

**Status of P81: proved**, as an implication from (I-A1), (I-F0), (I-REG). Inside P81 nothing is Outstanding.

---

## 5. CRIT

### 5.1 The statement

Let $\mathbf B$ be a separated sequence as in Theorem P81. Let $U_0$ be real, regular at a radius $\le a_0$ and critical for $C(\mathbf B,\mathbf V_0)$, with $\mathbf V_0:=M_{\mathbf B}(U_0)$ real and $\varepsilon_1$-regular, $\varepsilon_1\le\bar\varepsilon$. By P81(a) there is a real $w\in\mathcal G^{\rm res}$ with $U_0=U^\circ(\mathbf V_0)^w$. Put $\Phi^w:=\Phi_{\mathbf V_0}^w$ (P81(b)(iii)); so $\Phi^w(0)=U_0$. Let $\mathbf J$ be an independent current on the bonds of $\Omega_0$ such that
\[
 \delta:=\mathbf J-J^\circ(U_0)\quad\text{vanishes on every bond that touches }\Omega_1
 \tag{5.1}
\]
("on shell" in SA's sense, SA L10137: "the pair satisfies \(\mathbf J=J(\mathbf U)\) at the bonds that touch \(\Omega_1\)"). The plain current $J_+$ of $U_0$ satisfies (5.1): bonds touching $\Omega_1$ have complete stars, where $J_+=J_\eta=J^\circ$; and $\delta=-J^\circ(U_0)$ on the incomplete-star bonds, $0$ elsewhere.

For a row datum $B'$, let $\mathbf H(B';\mathbf J)$ and $j_1(\cdot\,;\mathbf J)$ be the $s\equiv\mathbf1$ first-system response of DR at the pair $(U_0,0,\mathbf J)$ and its current increment, with the specification (S1) of Section 5.2. Let $r_D$ be the datum radius of (I-UNQ) and put
\[
 r_C:=\min\{r_B,\ r_D/C_{\mathsf b}\},\qquad \mathfrak B_C:=\{B:\mathbf B\to\mathfrak g^c,\ \|B\|_\infty<r_C\},\qquad
 \mathbf H(B):=\mathbf H(\mathsf b(B);\mathbf J).
\]

**Theorem CRIT (response at criticality).** [proved here, as an implication from P81, (I-6), (I-OPS), (I-UNQ), DR1 and (S1)] On $\mathfrak B_C$:

(i) *Constraint, slice, multiplier.* $\mathcal Q^{\rm st}(\mathbf H(B))=\mathsf b(B)$, $RD^{\mathsf T}\mathbf H(B)=0$, and $F'(\mathbf H(B))=K_{\mathbf H(B)}^{\mathsf T}\omega(B)$ with $\omega(B):=\omega_1(\mathbf H(B);J^\circ(U_0))$ holomorphic and $\omega(0)=\lambda_0$, where $J^\circ(U_0)=\widehat Q^{\mathsf T}\lambda_0$.

(ii) *The background.* There is a holomorphic gauge $u_B$ with $u_0=\mathbf1$ such that
\[
 \Phi^w(B)=\big(e^{i\eta\mathbf H(B)}U_0\big)^{u_B},\qquad u_B\,v[\mathbf H(B)]=\mathbf1\ \text{at the tops}.
 \tag{5.2}
\]
$(\mathbf H,u)$ is SA Theorem 3's Landau pair relative to $U_0$ (SA L9697–9702), and it is the unique holomorphic pair with these properties and value $(0,\mathbf1)$ at $0$.

(iii) *Real data.* For real $B\in\mathfrak B_C$: $\mathbf H(B)$ and $u_B$ are real; $E:=e^{i\eta\mathbf H(B)}U_0$ is critical for $C(\mathbf B,(e^{iB}\mathbf V_0)^{v})$, $v:=v[\mathbf H(B)]$ at the nodes; for every real gauge $g$ with $g=v^{-1}$ at the nodes, $E^g\in U_{\mathbf B}(e^{iB}\mathbf V_0)$; and $E$ obeys (4.2), so it is regular at the radius $C_\Phi(\varepsilon_1+\|B\|_\infty)$.

(iv) *Bare rows.* $\mathbf H(B)(b)=\eta^{-1}B(b)$ at every bare row $b$. So $\mathbf H(B)=0$ on the bare rows outside $\operatorname{supp}B$.

(v) *Current.* At every bond of $\Omega_0$,
\[
 \mathbf J+j_1(\mathbf H(B);\mathbf J)=J^\circ(E)+f_{\mathbf H}^{-1}\delta,\qquad f_A:=f(-i\eta\operatorname{ad}A),\ f(z)=\frac{e^z-1}z .
 \tag{5.3}
\]
If $\mathbf H=0$ on $\operatorname{supp}\delta$, the last term is $\delta$. In particular $J^\circ(U_0)+j_1(\mathbf H;J^\circ(U_0))=J^\circ(E)$ everywhere.

(vi) *Plain-current boundary clause.* $\mathbf H(B';\mathbf J)=\mathbf H(B';J^\circ(U_0))$, and $j_1(\mathbf H;\mathbf J)-j_1(\mathbf H;J^\circ(U_0))=f_{\mathbf H}^{-1}\delta-\delta$.

(vii) *Incomplete stencils.* Take $\mathbf J=J_+$ (plain). If $B$ vanishes on every bare row within $\infty$-distance $2\eta$ of $\Omega_0^c$, then $K:=j_1(\mathbf H;J_+)$ vanishes at every incomplete-star bond, $J_++K=J_\eta(E)$ at every complete-star bond, and $(U_0,\mathbf H,J_++K)$ has the pair $(E,J_+(E))$: the substituted plain triple is the plain triple of $E$.

(viii) *Units.* Under the change of units (5) of `st1.md`, $(U,A',\mathbf J)\mapsto(U,L^{-m}A',L^{-3m}\mathbf J)$, (i)–(vii) hold with $\eta A'$, $\eta^3\mathbf J$ and $\eta^3j_1$ fixed. At a main step, with the reference triple recorded in level-$t$ units and the response in level-$(t-1)$ units, (v) reads $L^{-3}J_+^{(t)}+K=J(E)$ at complete stencils.

All constants are those of P81 and (I-UNQ): row 7, fixed before $\kappa_{\rm IN}$, independent of $M$ and $\bar\kappa$.

### 5.2 The specification at $s\equiv\mathbf1$

SA leaves two maps unwritten. For $\mathsf W_s$: "this expression *defines* \(\mathsf W_s\) for every \(s\) and every pair (it is a gradient only at \(s\equiv1\) and on shell)" (SA L10566–10569), without the expression. For the current: "The reduced current is a second component of this input, obtained from the constraint multiplier. … the multiplier construction and its uniform bounds are required independently" (SA L5786–5789). DR1 says the $s\equiv\mathbf1$ values of the decoupled maps are the undecoupled ones; so CRIT needs only these values. I fix them by porting Y3.

**Specification (S1).** At $s\equiv\mathbf1$, at the pair $(U_0,0,\mathbf J)$, with the operators (2.2) formed with $\mathbf J$:

1. *The straightening.* For small $A'$, $X=\mathcal D(A')$ is the small solution of $X=\mathsf C(A'-\ell X)$; $\mathcal L(A'):=A'-\ell\mathcal D(A')$; $\mathfrak D(A'):=\mathcal D'(A')$.
2. *The reduced action and remainder* (Y3 (I-86-62), Y3 L26804–26816, and (critical-reduced-action), Y3 L28439–28446, with $I\to\hat a$ and Y3's $S\to\Sigma$):
\[
\begin{split}
 V_{\mathbf J}(A')={}&-\langle\ell^{\mathsf T}\mathbf J,\ \mathcal D(A')-\mathsf C^{(2)}(A')\rangle-\langle\widehat QA',(\Sigma-\hat a)\mathcal D(A')\rangle\\
 &+\tfrac12\langle\mathcal D(A'),(\Sigma-\hat a)\mathcal D(A')\rangle+R_F(\mathcal L(A')),
 \qquad \mathsf W_1:=V_{\mathbf J}' ,
\end{split}\tag{5.4}
\]
that is,
\[
 \mathsf W_1(A')=-(\mathfrak D^{\mathsf T}-\mathsf C''[A']^{\mathsf T})\ell^{\mathsf T}\mathbf J-\widehat Q^{\mathsf T}(\Sigma-\hat a)\mathcal D-\mathfrak D^{\mathsf T}(\Sigma-\hat a)\widehat QA'+\mathfrak D^{\mathsf T}(\Sigma-\hat a)\mathcal D+\mathcal V(T)-\mathfrak D^{\mathsf T}\ell^{\mathsf T}\mathcal V(T),
 \tag{5.5}
\]
$T=\mathcal L(A')$, $\mathsf C''[A']:=\frac d{dt}\mathsf C'_{tA'}|_{t=0}$. The six terms follow from (5.4) by differentiation: the derivatives of $\mathcal D$, $\mathsf C^{(2)}$ and $\mathcal L$ are $\mathfrak D$, $\mathsf C''[A']$ and $1-\ell\mathfrak D$, and $\Sigma-\hat a$ is symmetric.
3. *The system (R9) at $s\equiv\mathbf1$* (SA L10356–10363, L5770–5776):
\[
 A_\bullet=\ell_1B'+\mathbf A,\qquad \mathbf A+\mathfrak G\,\mathsf W_1(A_\bullet)=0,\qquad X=\mathcal D(A_\bullet),\qquad \mathbf H=A_\bullet-\ell X .
 \tag{5.6}
\]
4. *Multiplier and current* (Y3 (decoupled-current-definition), Y3 L33225–33230, with $H^\circledast$ replaced by its $s\equiv\mathbf1$ value $\ell^{\mathsf T}(F'(A)-F'(0))$, which is Y3's energy identity at Y3 L33196: "\(H^{\mathsf T}(F'(A)-J)=H^\circledast(A)\)"):
\[
 \Psi_A:=(1+\ell^{\mathsf T}\mathsf C_A'^{\mathsf T})^{-1},\qquad
 \omega_1(A;\mathbf J):=\Psi_A\,\ell^{\mathsf T}\big(F'(A)-F'(0)+\mathbf J\big),\qquad
 j_1(A;\mathbf J):=f_A^{-1}K_A^{\mathsf T}\omega_1(A;\mathbf J)-\widehat Q^{\mathsf T}\ell^{\mathsf T}\mathbf J .
 \tag{5.7}
\]
DR's current increment at the physical locus is $K:=j_1(\mathbf H;\mathbf J)$.

*Why (S1) is admissible.* (a) It is defined by explicit finite formulas from the operators of SA's (1c) and the action, so it is a specification, not a hypothesis. (b) It agrees with Y3's construction at $s\equiv\mathbf1$, which is the construction SA (R9) follows. (c) The form of $\mathsf W_1$ is that of SA (j): the second-order term $\Delta_\pi\ell$ is moved onto row operators by $\Delta_\pi\ell=\widehat Q^{\mathsf T}(\Sigma-\hat a)$ (Lemma C2(vi)); the remaining terms need first-order norms only. (d) The current is built from the multiplier, as SA L5786 and SA L10414–10418 require. (e) For the identification only the pairing of $\mathsf W_1(A')$ with $\mathcal K$ at slice points $A'$ matters (Proposition C5). So any other specification whose $s\equiv\mathbf1$ value differs from (5.5) by a map into $\mathcal K^\perp=\operatorname{ran}\widehat Q^{\mathsf T}+\operatorname{ran}DR$ at slice points gives the same $\mathbf H$; for instance `a1-balaban.md` (4.3), which uses $V_0$ in place of $R_F$ (these agree on $\mathrm{Sl}$). The DR lane must use a decoupled specification whose $s\equiv\mathbf1$ value is (S1) in this sense.

### 5.3 Tests for a counterexample, run first

**T1 (off shell at a bond touching $\Omega_1$).** If $\delta\ne0$ at a bond $b$ touching $\Omega_1$, then $\lambda_A(b_\pm)$ need not vanish, $\Delta'_\pi[\delta]\ne0$ in general, and the defect $G_{(1)}\Delta'_\pi[\mathbf J-J(\mathbf U)]DG'R$ of SA statement 3 (SA L10302) is nonzero. Then $RD^{\mathsf T}\ell_{(1)}\ne0$ in general and Proposition C5 fails. CRIT assumes (5.1). ST1's plain triple satisfies it (Section 5.1). No counterexample to CRIT as stated.

**T2 (stage of level zero).** At a preparatory stage with $j=0$ the removed rows are bare rows with $B\ne0$. Then (iv) gives $\mathbf H\ne0$ there; `st1-draft2.md` D4(3)'s "$H=0$ on the bare determining rows" is false at such a stage. D4 needs only $K=0$ at incomplete stencils, which (vii) gives whenever the source misses the $2\eta$-neighbourhood of $\Omega_0^c$. This corrects the consumer, not CRIT.

**T3 (away from $s\equiv\mathbf1$).** SA (j), SA L10563–10566: "on the cubes around a row where \(s\) vanishes, every term is absent, so that \(Q\mathsf H(s)\) equals \(0\) there and not \(1\)." So no constraint identity holds at general $s$. CRIT claims nothing there.

**T4 (nonuniform neighbourhood).** The real neighbourhood $N$ of Lemma 6.3 depends on the finite geometry. Theorem C6 uses it only to start an identity-theorem argument on the uniform polydisc $\mathfrak B_C$. No constant reads $N$.

**T5 (the current at incomplete stars in four dimensions).** A bond at $\partial\Omega_0$ can keep up to five of its six plaquettes (`st1.md:425`), so $J^\circ(U_0)$ and $J_+$ differ there by a nonzero amount, of size at most $5a_m\xi_0^{-3}$. (vi) shows this does not change $\mathbf H$ and changes $j_1$ by exactly $f^{-1}\delta-\delta$. No counterexample.

### 5.4 Lemma C1: gauge identities at a real critical reference

**Lemma C1.** [proved here; Y3 L28245–28362 is the three-dimensional model; SA L10296–10301 states (C1.3) and (C1.5)] Let $U_0$ be real and critical, $J=F'(0)=J^\circ(U_0)$, $\Delta=F''(0)$, and $\mathcal N:=\ker Q'$.

(C1.1) $D^{\mathsf T}J=0$, and for all 1-forms $X$ and site functions $v$,
\[
 \langle X,\Delta Dv\rangle=\tfrac12\big\langle i[v,X]-i[X,v^+],\ J\big\rangle .
\]
(C1.2) For $\mu\in\mathcal N$: $\mu$ vanishes at every level-0 top; $\Delta_{\mathbf U}\mu=D^{\mathsf T}D\mu$; $R\,\Delta_{\mathbf U}\mu=\Delta_{\mathbf U}\mu$; $\lambda_{D\mu}=\mu$; $\Pi D\mu=0$. Moreover $\operatorname{ran}R=\Delta_{\mathbf U}\mathcal N$, and $\chi_f:=G'Rf\in\mathcal N$ with $\Delta_{\mathbf U}\chi_f=Rf$.

(C1.3) $\widehat QD\mu=0$ for $\mu\in\mathcal N$. More precisely $(D\tilde q_0D\chi)(c)=\operatorname{Ad}(\mathbf V_0(c))(Q'\chi)(c_+)-(Q'\chi)(c_-)$ for every site function $\chi$ and row $c$.

(C1.4) $\Delta-\Delta'_\pi[J]=\Pi^{\mathsf T}\Delta\Pi$.

(C1.5) $(\Delta-\Delta'_\pi[J])D\mu=0$ for $\mu\in\mathcal N$.

*Proof.* (C1.1) For a site function $v$ define $A^v$ near $(A,v)=(0,0)$ by $e^{i\eta A^v}U_0=(e^{i\eta A}U_0)^{e^{iv}}$ on every bond with both ends in $\Omega_0$. With $U^g(b)=g(b_-)U(b)g(b_+)^{-1}$: $e^{i\eta A^v(b)}=e^{iv(b_-)}e^{i\eta A(b)}e^{-iv^+(b)}$, $v^+(b)=\operatorname{Ad}U_0(b)v(b_+)$. The quadratic part of $\log(e^Xe^Ye^Z)$ is $\tfrac12([X,Y]+[X,Z]+[Y,Z])$ (expand the three exponential series and the logarithm series; the quadratic terms of $\log(1+W)$ are $W-\tfrac12W^2$). With $X=iv_-$, $Y=i\eta A$, $Z=-iv^+$ and $v^+-v_-=\eta Dv$:
\[
 A^v=A-Dv+\tfrac12N(A,v)+O\big((|A|+|v|)^3\big),\qquad N(A,v)=i[v_-,A]-i[A,v^+]-i[v_-,Dv],
\]
which is Y3 (critical-gauge-expansion), Y3 L28337–28341. Every inner plaquette transforms by conjugation, so $F(A^v)=F(A)$ identically. Compare homogeneous terms of degree one and two in $(A,v)$ in $F(A^v)=F(0)+\langle J,A^v\rangle+\tfrac12\langle A^v,\Delta A^v\rangle+O(3)$. Degree one: $\langle J,Dv\rangle=0$ for all $v$, so $D^{\mathsf T}J=0$. Degree two:
\[
 \langle A-Dv,\Delta(A-Dv)\rangle=\langle A,\Delta A\rangle-\langle N(A,v),J\rangle .
 \tag{5.8}
\]
The part of (5.8) bilinear in $(A,v)$ is $-2\langle A,\Delta Dv\rangle=-\langle i[v,A]-i[A,v^+],J\rangle$. This is (C1.1). The invariance holds for every site function: the inner action reads only bonds with both ends in $\Omega_0$, and a gauge at a site of $\Omega_0$ changes only such bonds.

(C1.2) A level-0 top $y$ has pillar $\{y\}$ (SA L9599), so $(Q'\mu)(y)=\mu(y)$; $\mu\in\mathcal N$ gives $\mu(y)=0$. If $\Delta_{\mathbf U}$ differs from $D^{\mathsf T}D$, it does so by a diagonal term at sites with a missing neighbour in $\Omega_0$ (Y3 L28276–28279: "\((\Delta^\circ-D^{\mathsf T}D)\chi(x)=\xi^{-2}(6-n(x))\chi(x)\)"; in four dimensions $8-n(x)$). Such a site is within $\eta$ of $\Omega_0^c$, hence outside $\Omega_1$ by separation, hence a level-0 top, where $\mu=0$. So $\Delta_{\mathbf U}\mu=D^{\mathsf T}D\mu$ in either convention. $G'$ is symmetric, so $P:=G'Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G'$ is a symmetric idempotent and $R=1-P$ is the orthogonal projection onto $(\operatorname{ran}G'Q'^{\mathsf T})^\perp=\ker(Q'G')$. For $\mu\in\mathcal N$: $G'^{-1}\mu=\Delta_{\mathbf U}\mu+Q'^{\mathsf T}aQ'\mu=\Delta_{\mathbf U}\mu$, so $G'\Delta_{\mathbf U}\mu=\mu$ and $Q'G'\Delta_{\mathbf U}\mu=Q'\mu=0$; thus $\Delta_{\mathbf U}\mu\in\operatorname{ran}R$ and $R\Delta_{\mathbf U}\mu=\Delta_{\mathbf U}\mu$. Then $\lambda_{D\mu}=G'RD^{\mathsf T}D\mu=G'R\Delta_{\mathbf U}\mu=G'\Delta_{\mathbf U}\mu=\mu$, and $\Pi D\mu=D\mu-D\lambda_{D\mu}=0$. For $f$ a site function: $Q'\chi_f=Q'G'Rf=0$, and $G'^{-1}\chi_f=Rf$ gives $\Delta_{\mathbf U}\chi_f=Rf-Q'^{\mathsf T}aQ'\chi_f=Rf$. So $\operatorname{ran}R\subset\Delta_{\mathbf U}\mathcal N$; the converse inclusion was just shown.

(C1.3) Let $e^{i\eta A_t}U_0=U_0^{e^{it\chi}}$, so $\dot A_0=-D\chi$ (the first-order part of $A^v$ at $A=0$, $v=t\chi$). Covariance of the averages gives $m(A_t)(c)=e^{it\chi(c_-)}\mathbf V_0(c)e^{-it\chi(c_+)}$. Differentiate (2.1) at $t=0$, using $v[0]=\mathbf1$, $\tilde q(0)=0$ and Lemma 6.1 of (I-6), $\dot v(y)=i(\chi(y)-(Q'\chi)(y))$ at every node:
\[
 i\chi(c_-)\mathbf V_0-i\mathbf V_0\chi(c_+)
 =i(\chi-Q'\chi)(c_-)\mathbf V_0+i\big(D\tilde q_0(-D\chi)\big)(c)\mathbf V_0-i\mathbf V_0(\chi-Q'\chi)(c_+).
\]
Cancel the common terms $i\chi(c_-)\mathbf V_0$ and $-i\mathbf V_0\chi(c_+)$, divide by $i$, and multiply on the right by $\mathbf V_0^{-1}$: $(D\tilde q_0D\chi)(c)=\operatorname{Ad}(\mathbf V_0(c))(Q'\chi)(c_+)-(Q'\chi)(c_-)$. At an outward row the outer end is a node of the lower level; (2.1) and Lemma 6.1 use that node's own level, so the same computation applies. For $\mu\in\mathcal N$ the right side is zero, so $D\tilde q_0D\mu=0$ and, since $D\tilde q_0=\mathcal T_0K_0$ with $\mathcal T_0$ invertible, $\widehat QD\mu=K_0D\mu=0$. This is SA's "\(QD\lambda=\bar DQ'\lambda\)" (SA L10299) and Y3 (critical-row-gradient), Y3 L28283–28318.

(C1.4) Put $v=\lambda_A$ in (5.8). Then $A-D\lambda_A=\Pi A$ and $\langle N(A,\lambda_A),J\rangle=\langle i[\lambda_A,A]-i[A,\lambda_A^+]-i[\lambda_A,D\lambda_A],J\rangle$. By (2.3) with $C=A$ this is $\langle A,\Delta'_\pi[J]A\rangle$. So $\langle\Pi A,\Delta\Pi A\rangle=\langle A,(\Delta-\Delta'_\pi[J])A\rangle$ for all $A$. Both sides are quadratic forms of symmetric operators ((2.3) is symmetric in $(A,C)$ by inspection). Polarization gives (C1.4). (This also shows that SA's symmetrized formula (2.3) and Y3's form (bg-current-form), Y3 L26243–26248, agree on the physical current.)

(C1.5) $(\Delta-\Delta'_\pi[J])D\mu=\Pi^{\mathsf T}\Delta\Pi D\mu=0$ by (C1.4) and (C1.2). $\square$

*Four-dimensional changes.* None in the algebra. The boundary term is $8-n(x)$, not $6-n(x)$, and vanishes on $\mathcal N$ for the same reason. The projection is SA's $R$ with the pillar mean $Q'$ (SA L10141), not Y3's mean-Landau $\mathsf R_{\mathsf m}$; the argument uses only that $R$ is the orthogonal projection onto $\ker(Q'G')$.

### 5.5 Lemma C2: linear identities

**Lemma C2.** [proved here; Y3 (critical-linear-identities), Y3 L28374–28398, and `a1-balaban.md` (3.27) are the models] At a real critical reference, with $\mathbf J$ satisfying (5.1):

(i) $G_{(1)}DR=DG'R$ (for $G$ and for $G_1$).
(ii) $RD^{\mathsf T}\ell=RD^{\mathsf T}\ell_1=0$.
(iii) $\widehat QG_1DR=0$ and $RD^{\mathsf T}G_1DR=R$.
(iv) $\mathfrak G$ is symmetric; $\widehat Q\mathfrak G=RD^{\mathsf T}\mathfrak G=0$; $\mathfrak G\widehat Q^{\mathsf T}=\mathfrak GDR=0$.
(v) $\mathfrak GG_1^{-1}\delta'=\delta'$ for $\delta'\in\mathcal K$. If $t\in\mathcal K$ and $\langle G_1^{-1}t,\delta'\rangle=0$ for all $\delta'\in\mathcal K$, then $t=0$. If $f\perp\mathcal K$, then $\mathfrak Gf=0$.
(vi) $\Delta_\pi\ell=\widehat Q^{\mathsf T}(\Sigma-\hat a)$ and $\ell^{\mathsf T}\Delta_\pi\ell=\Sigma-\hat a$.
(vii) $\langle X,\Delta'_\pi[\mathbf J]Y\rangle=0$ if $X,Y\in\mathrm{Sl}$. Hence $\langle X,\Delta Y\rangle=\langle X,\Delta_\pi Y\rangle$ and $\langle X,\Delta^{(2)}[\zeta]Y\rangle=\langle X,\Pi^{\mathsf T}\Delta^{(2)}[\zeta]\Pi Y\rangle$ for $X,Y\in\mathrm{Sl}$.

*Proof.* First reduce to $\mathbf J=J$. By (5.1) and (C1.2), every bond $b\in\operatorname{supp}\delta$ has both endpoints at level-0 tops, where $\lambda_A$ vanishes ($\lambda_A=G'RD^{\mathsf T}A\in\mathcal N$ since $Q'G'R=0$). Every term of (2.3) at $b$ contains $\lambda_A(b_-)$, $\lambda_A^+(b)$, $\lambda_C(b_-)$, $\lambda_C^+(b)$ or $D\lambda(b)=\eta^{-1}(\lambda^+(b)-\lambda(b_-))$. So $\Delta'_\pi[\delta]=0$ and $\Delta'_\pi[\mathbf J]=\Delta'_\pi[J]$, $G$ is unchanged. Proposition C8 below shows $\Delta^{(2)}[\ell^{\mathsf T}\delta]=0$, so $G_1$ is unchanged too. We may therefore take $\mathbf J=J$.

(i) Let $\chi=\chi_f=G'Rf\in\mathcal N$. By (C1.5), (C1.2), (C1.3): $(\Delta-\Delta'_\pi)D\chi=0$; $\Pi D\chi=0$; $\widehat QD\chi=0$; $DRD^{\mathsf T}D\chi=DR\Delta_{\mathbf U}\chi=DRRf=DRf$. Hence $G^{-1}D\chi=DRf$ and $G_1^{-1}D\chi=DRf-\Pi^{\mathsf T}\Delta^{(2)}\Pi D\chi=DRf$. So $G_{(1)}DRf=D\chi=DG'Rf$.

(ii) $(RD^{\mathsf T}G_{(1)}\widehat Q^{\mathsf T})^{\mathsf T}=\widehat QG_{(1)}DR=\widehat QDG'R=0$ by (i) and (C1.3), since $G'R$ maps into $\mathcal N$ and $G_{(1)}$, $R$ are symmetric. Multiply on the right by $\Sigma$, respectively $(\widehat QG_1\widehat Q^{\mathsf T})^{-1}$.

(iii) $\widehat QG_1DR=\widehat QDG'R=0$. $RD^{\mathsf T}G_1DR=RD^{\mathsf T}DG'R=R\Delta_{\mathbf U}G'R=RR=R$, using $D^{\mathsf T}D=\Delta_{\mathbf U}$ on $\mathcal N$ and $\Delta_{\mathbf U}\chi_f=Rf$.

(iv) $G_1$ and $G_1DRD^{\mathsf T}G_1$ are symmetric, and $\ell_1\widehat QG_1=G_1\widehat Q^{\mathsf T}(\widehat QG_1\widehat Q^{\mathsf T})^{-1}\widehat QG_1$ is symmetric. Then
$\mathfrak G\widehat Q^{\mathsf T}=G_1\widehat Q^{\mathsf T}-G_1DR(RD^{\mathsf T}G_1\widehat Q^{\mathsf T})-G_1\widehat Q^{\mathsf T}=0$ by (ii), and
$\mathfrak GDR=G_1DR-G_1D(RD^{\mathsf T}G_1DR)-\ell_1(\widehat QG_1DR)=G_1DR-G_1DR-0=0$ by (iii). Transpose for the other two.

(v) $\mathfrak GG_1^{-1}\delta'=\delta'-G_1DRD^{\mathsf T}\delta'-\ell_1\widehat Q\delta'=\delta'$ for $\delta'\in\mathcal K$. If $f\perp\mathcal K$: $\mathfrak Gf\in\mathcal K$ by (iv), and $\langle\mathfrak Gf,g\rangle=\langle f,\mathfrak Gg\rangle=0$ for every $g$, since $\mathfrak Gg\in\mathcal K$; nondegeneracy of the pairing gives $\mathfrak Gf=0$. If $t\in\mathcal K$ and $G_1^{-1}t\perp\mathcal K$, then $t=\mathfrak GG_1^{-1}t=0$.

(vi) $G^{-1}\ell=\widehat Q^{\mathsf T}\Sigma$ by definition. So $\Delta_\pi\ell=\widehat Q^{\mathsf T}\Sigma-DRD^{\mathsf T}\ell-\widehat Q^{\mathsf T}\hat a\widehat Q\ell=\widehat Q^{\mathsf T}(\Sigma-\hat a)$ by (ii) and $\widehat Q\ell=1$. Then $\ell^{\mathsf T}\Delta_\pi\ell=(\widehat Q\ell)^{\mathsf T}(\Sigma-\hat a)=\Sigma-\hat a$.

(vii) For $X\in\mathrm{Sl}$, $\lambda_X=G'RD^{\mathsf T}X=0$. Every term of (2.3) contains $\lambda_X$ or $\lambda_Y$. The second claim follows from $\Pi X=X$, $\Pi Y=Y$. $\square$

### 5.6 Lemma C3: the straightening

**Lemma C3.** [proved here from (I-UNQ); Y3 Proposition I-86-52, Y3 L26770–26800, and `a1-balaban.md` (4.1)–(4.2) are the models] On the ball of (I-UNQ):

(i) $\mathcal Q^{\rm st}(\mathcal L(A'))=\widehat QA'$ and $RD^{\mathsf T}\mathcal L(A')=RD^{\mathsf T}A'$.
(ii) $K_{\mathcal L(A')}\mathcal L'(A')=\widehat Q$ and $RD^{\mathsf T}\mathcal L'(A')=RD^{\mathsf T}$, where $\mathcal L'=1-\ell\mathfrak D$.
(iii) $\mathcal L'(A')$ is invertible, with inverse $1+\ell\mathsf C'_T$, $T=\mathcal L(A')$, and maps $\mathcal K$ onto $\mathcal K_T:=\ker K_T\cap\mathrm{Sl}$.
(iv) $\mathfrak D=(1+\mathsf C'_T\ell)^{-1}\mathsf C'_T$ and $\mathfrak D^{\mathsf T}=\mathsf C_T'^{\mathsf T}(1+\ell^{\mathsf T}\mathsf C_T'^{\mathsf T})^{-1}$.
(v) If $T$ is small, $X:=\mathsf C(T)$ and $A':=T+\ell X$, then $\mathcal D(A')=X$ and $\mathcal L(A')=T$.

*Proof.* (i) $\mathcal Q^{\rm st}(T)=\widehat QT+\mathsf C(T)=\widehat QA'-\widehat Q\ell\mathcal D+\mathcal D=\widehat QA'$, using $\widehat Q\ell=1$ and $\mathcal D=\mathsf C(T)$. $RD^{\mathsf T}T=RD^{\mathsf T}A'$ by Lemma C2(ii). (ii) Differentiate (i). (iv) Differentiate $\mathcal D=\mathsf C(A'-\ell\mathcal D)$: $\mathfrak D=\mathsf C'_T(1-\ell\mathfrak D)$; solve; the inverse exists because $\|\mathsf C'_T\ell\|\le\tfrac12$ on the ball ((I-UNQ): the Lipschitz constant $9C_2B_0r\le\tfrac12$). Transpose. (iii) $(1-\ell\mathfrak D)(1+\ell\mathsf C'_T)=1+\ell\mathsf C'_T-\ell(1+\mathsf C'_T\ell)^{-1}\mathsf C'_T(1+\ell\mathsf C'_T)=1+\ell\mathsf C'_T-\ell\mathsf C'_T=1$, using $(1+\mathsf C'\ell)^{-1}\mathsf C'(1+\ell\mathsf C')=\mathsf C'$. By (ii), $\delta'\in\mathcal K$ gives $\mathcal L'\delta'\in\mathcal K_T$. Conversely for $\tau\in\mathcal K_T$, $\delta':=(1+\ell\mathsf C'_T)\tau$ has $\widehat Q\delta'=\widehat Q\tau+\mathsf C'_T\tau=K_T\tau=0$ and $RD^{\mathsf T}\delta'=RD^{\mathsf T}\tau=0$. (v) $X=\mathsf C(A'-\ell X)$ holds by construction; $X$ and $A'$ are small when $T$ is; uniqueness in (I-UNQ)'s ball gives $X=\mathcal D(A')$, so $\mathcal L(A')=A'-\ell X=T$. $\square$

### 5.7 Lemma C4: the reduced-action identity

**Lemma C4.** [port of Y3 (I-88-75)–(I-88-76), Y3 L28439–28470; four-term form `a1-balaban.md` (4.3)] At a real critical reference with $\mathbf J=J$, for $A'\in\mathrm{Sl}$ in the ball of (I-UNQ),
\[
 F(\mathcal L(A'))=F(0)+\langle J,A'\rangle+\tfrac12\langle A',\Delta_1A'\rangle+V_J(A'),
 \tag{5.9}
\]
and for every $\delta'\in\mathrm{Sl}$,
\[
 \langle F'(\mathcal L(A')),\mathcal L'(A')\delta'\rangle=\langle J+\Delta_1A'+\mathsf W_1(A'),\delta'\rangle .
 \tag{5.10}
\]

*Proof.* Write $T=\mathcal L(A')=A'-\ell\mathcal D$. By the definition of $R_F$, $F(T)=F(0)+\langle J,T\rangle+\tfrac12\langle T,\Delta T\rangle+R_F(T)$.

*Linear term.* $\langle J,T\rangle=\langle J,A'\rangle-\langle\ell^{\mathsf T}J,\mathcal D\rangle$. Split $\mathcal D=\mathsf C^{(2)}(A')+(\mathcal D-\mathsf C^{(2)}(A'))$. By the definition of $\Delta^{(2)}$, $\langle\ell^{\mathsf T}J,\mathsf C^{(2)}(A')\rangle=\tfrac12\langle A',\Delta^{(2)}[\ell^{\mathsf T}J]A'\rangle$. So
$\langle J,T\rangle=\langle J,A'\rangle-\tfrac12\langle A',\Delta^{(2)}A'\rangle-\langle\ell^{\mathsf T}J,\mathcal D-\mathsf C^{(2)}(A')\rangle$.

*Quadratic term.* $A'\in\mathrm{Sl}$ and $\ell\mathcal D\in\mathrm{Sl}$ (Lemma C2(ii)), so $T\in\mathrm{Sl}$. By Lemma C2(vii), $\langle T,\Delta T\rangle=\langle T,\Delta_\pi T\rangle$. Expand, using symmetry of $\Delta_\pi$ and Lemma C2(vi):
$\langle T,\Delta_\pi T\rangle=\langle A',\Delta_\pi A'\rangle-2\langle\widehat QA',(\Sigma-\hat a)\mathcal D\rangle+\langle\mathcal D,(\Sigma-\hat a)\mathcal D\rangle$.

*Collect.* By Lemma C2(vii), $\langle A',\Delta^{(2)}A'\rangle=\langle A',\Pi^{\mathsf T}\Delta^{(2)}\Pi A'\rangle$. So the quadratic form in $A'$ is $\tfrac12\langle A',(\Delta_\pi-\Pi^{\mathsf T}\Delta^{(2)}[\ell^{\mathsf T}J]\Pi)A'\rangle=\tfrac12\langle A',\Delta_1A'\rangle$, by (2.2): $G_1^{-1}=\Delta_\pi+DRD^{\mathsf T}+\widehat Q^{\mathsf T}\hat a\widehat Q-\Pi^{\mathsf T}\Delta^{(2)}\Pi$. The rest is $V_J(A')$ of (5.4). This is (5.9).

(5.10): both sides of (5.9) are holomorphic on the open subset of the linear space $\mathrm{Sl}$; differentiate along $\delta'\in\mathrm{Sl}$. The left derivative is $\langle F'(T),\mathcal L'\delta'\rangle$. On the right, $\Delta_1$ is symmetric, and the derivative of $V_J$ along $\delta'$ is $\langle V_J'(A'),\delta'\rangle=\langle\mathsf W_1(A'),\delta'\rangle$. $\square$

### 5.8 Proposition C5: the $s\equiv\mathbf1$ system is slice stationarity

**Proposition C5.** [proved here; Y3 Theorem I-88-93 (forward) and the converse of Y3 Proposition I-88-127, Y3 L33522–33555, are the models; SA L10580–10582, remark (k), states it] At a real critical reference with $\mathbf J$ satisfying (5.1):

(Forward) If $(A_\bullet,\mathbf A,X,\mathbf H)$ solves (5.6) in the balls of (I-UNQ), then $\mathcal Q^{\rm st}(\mathbf H)=B'$, $RD^{\mathsf T}\mathbf H=0$, and $\langle F'(\mathbf H),\tau\rangle=0$ for every $\tau\in\mathcal K_{\mathbf H}$.

(Converse) Let $\mathbf H$ be small, with $RD^{\mathsf T}\mathbf H=0$ and $\langle F'(\mathbf H),\tau\rangle=0$ for every $\tau\in\mathcal K_{\mathbf H}$ (in particular, if $F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda$ for some $\lambda$). Put $B':=\mathcal Q^{\rm st}(\mathbf H)$, $X:=\mathsf C(\mathbf H)$, $A_\bullet:=\mathbf H+\ell X$, $\mathbf A:=A_\bullet-\ell_1B'$. If these lie in the balls of (I-UNQ), then $(A_\bullet,\mathbf A,X,\mathbf H)$ solves (5.6), and so $\mathbf H=\mathbf H(B';\mathbf J)$ by uniqueness.

*Proof.* By Lemma C2's first paragraph and Proposition C8, (5.6) is the same system for $\mathbf J$ and for $J$. Take $\mathbf J=J$.

(Forward) $\widehat QA_\bullet=\widehat Q\ell_1B'+\widehat Q\mathbf A=B'-\widehat Q\mathfrak G\mathsf W_1=B'$ (Lemma C2(iv)). $RD^{\mathsf T}A_\bullet=RD^{\mathsf T}\ell_1B'-RD^{\mathsf T}\mathfrak G\mathsf W_1=0$ (Lemma C2(ii), (iv)). So $A_\bullet\in\mathrm{Sl}$ and $\mathbf A\in\mathcal K$. Since $X=\mathcal D(A_\bullet)$, $\mathbf H=\mathcal L(A_\bullet)$, and Lemma C3(i) gives $\mathcal Q^{\rm st}(\mathbf H)=\widehat QA_\bullet=B'$ and $RD^{\mathsf T}\mathbf H=0$. Let $\tau\in\mathcal K_{\mathbf H}$, and $\delta':=\mathcal L'(A_\bullet)^{-1}\tau\in\mathcal K$ (Lemma C3(iii)). By (5.10),
\[
 \langle F'(\mathbf H),\tau\rangle=\langle J,\delta'\rangle+\langle\Delta_1A_\bullet,\delta'\rangle+\langle\mathsf W_1(A_\bullet),\delta'\rangle .
\]
$J=\widehat Q^{\mathsf T}\lambda_0$ (Lemma 6.2 of (I-6) at $A=0$; $K_0=\widehat Q$ is onto since $\widehat Q\ell=1$), so $\langle J,\delta'\rangle=\langle\lambda_0,\widehat Q\delta'\rangle=0$. Next, $\langle DRD^{\mathsf T}A_\bullet,\delta'\rangle=\langle RD^{\mathsf T}A_\bullet,D^{\mathsf T}\delta'\rangle=0$ and $\langle\widehat Q^{\mathsf T}\hat a\widehat QA_\bullet,\delta'\rangle=\langle\hat a\widehat QA_\bullet,\widehat Q\delta'\rangle=0$, so $\langle\Delta_1A_\bullet,\delta'\rangle=\langle G_1^{-1}A_\bullet,\delta'\rangle$. And $\langle G_1^{-1}\ell_1B',\delta'\rangle=\langle\widehat Q^{\mathsf T}(\widehat QG_1\widehat Q^{\mathsf T})^{-1}B',\delta'\rangle=0$. So $\langle\Delta_1A_\bullet,\delta'\rangle=\langle G_1^{-1}\mathbf A,\delta'\rangle=-\langle G_1^{-1}\mathfrak G\mathsf W_1,\delta'\rangle=-\langle\mathsf W_1,\mathfrak GG_1^{-1}\delta'\rangle=-\langle\mathsf W_1,\delta'\rangle$ by symmetry of $\mathfrak G$, $G_1$ and Lemma C2(v). The three terms sum to $0$.

(Converse) $X=\mathsf C(A_\bullet-\ell X)$ by construction, so Lemma C3(v) gives $X=\mathcal D(A_\bullet)$ and $\mathcal L(A_\bullet)=\mathbf H$. $\widehat QA_\bullet=\widehat Q\mathbf H+X=\mathcal Q^{\rm st}(\mathbf H)=B'$; $RD^{\mathsf T}A_\bullet=RD^{\mathsf T}\mathbf H+RD^{\mathsf T}\ell X=0$. So $A_\bullet\in\mathrm{Sl}$, $\widehat Q\mathbf A=0$, $RD^{\mathsf T}\mathbf A=-RD^{\mathsf T}\ell_1B'=0$: $\mathbf A\in\mathcal K$. For $\delta'\in\mathcal K$, (5.10) and Lemma C3(iii) give $\langle J+\Delta_1A_\bullet+\mathsf W_1(A_\bullet),\delta'\rangle=\langle F'(\mathbf H),\mathcal L'\delta'\rangle=0$. As in the forward step, $\langle J,\delta'\rangle=0$ and $\langle\Delta_1A_\bullet,\delta'\rangle=\langle G_1^{-1}\mathbf A,\delta'\rangle$. So $\langle G_1^{-1}\mathbf A+\mathsf W_1(A_\bullet),\delta'\rangle=0$ for all $\delta'\in\mathcal K$. Put $\mathbf A':=-\mathfrak G\mathsf W_1(A_\bullet)\in\mathcal K$; then $\langle G_1^{-1}\mathbf A',\delta'\rangle=-\langle\mathsf W_1,\delta'\rangle$. So $t:=\mathbf A-\mathbf A'\in\mathcal K$ has $G_1^{-1}t\perp\mathcal K$, and $t=0$ by Lemma C2(v). Thus $\mathbf A+\mathfrak G\mathsf W_1(A_\bullet)=0$: (5.6) holds. If $F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda$, then $\langle F'(\mathbf H),\tau\rangle=\langle\lambda,K_{\mathbf H}\tau\rangle=0$ for $\tau\in\ker K_{\mathbf H}$. $\square$

**The $s\equiv\mathbf1$ system is (I-UNQ)'s chart system.** On $\mathrm{Sl}$, $V_J$ of (5.4) and $V$ of `a1-balaban.md` (4.3) are the same function: their first three terms coincide after $\langle A',\Delta_\pi\ell\mathcal D\rangle=\langle\widehat QA',(\Sigma-\hat a)\mathcal D\rangle$ and $\langle\ell\mathcal D,\Delta_\pi\ell\mathcal D\rangle=\langle\mathcal D,(\Sigma-\hat a)\mathcal D\rangle$ (Lemma C2(vi)) and $\mathcal D_{\ge3}=\mathcal D-\mathsf C^{(2)}$; and $V_0(T)=R_F(T)$ for $T\in\mathrm{Sl}$ by Lemma C2(vii). So $\mathsf W_1-V'$ annihilates $\mathrm{Sl}\supset\mathcal K$ at slice points, and $\mathfrak G(\mathsf W_1-V')=0$ there (Lemma C2(v)). Also $\mathfrak G_1J=\mathfrak G\widehat Q^{\mathsf T}\lambda_0=0$. So the $\mathbf A$-equation of (5.6) is `a1-balaban.md` (4.5) at the critical reference, and its straightening is (4.1). (I-UNQ) supplies existence, uniqueness in fixed balls and holomorphy in $B'$ on $\|B'\|_\infty<r_D$. With DR1, the DR response at $s\equiv\mathbf1$ is this solution. So $\mathbf H(B';\mathbf J)$ is well defined, unique in those balls and holomorphic.

### 5.9 Theorem C6: the response is the background

**Theorem C6.** [proved here from P81(b), (I-6), (I-UNQ), Proposition C5; port of Y3 Corollary I-88-131, Y3 L33594–33640; SA L10450–10454] Items (i)–(iv) of Theorem CRIT hold.

*Proof.* *Step 1 (near real zero).* $\Phi^w$ is holomorphic on $\mathcal B$, $\Phi^w(0)=U_0$, $M_{\mathbf B}\Phi^w(B)=e^{iB}\mathbf V_0$, and $\Phi^w(B)$ is critical for real $B$ (P81(b)(iii)). This is the form of P81 that Lemma 6.3 uses. Lemma 6.3 gives a real neighbourhood $N$ of $0$ and a real-analytic $(H_N,u_N)$ with $(H_N,u_N)(0)=(0,\mathbf1)$, $\Phi^w(B)=(e^{i\eta H_N}U_0)^{u_N}$, $RD^{\mathsf T}H_N=0$, $u_Nv[H_N]=\mathbf1$ at the tops.

*Step 2 (the multiplier on $N$).* For real $B\in N$, $E_N:=e^{i\eta H_N}U_0=\Phi^w(B)^{u_N^{-1}}$ is critical for its own datum: a gauge maps constraint sets onto constraint sets and preserves the inner action. $K_{H_N}$ is onto because $K_{H_N}\ell=1+\mathsf C'_{H_N}\ell$ is invertible for small $H_N$. Lemma 6.2 (repaired) gives $F'(H_N)=K_{H_N}^{\mathsf T}\omega_N$.

*Step 3 (the datum on $N$).* By covariance and (5.2)'s normalization, at a row $c$:
$m(H_N)(c)=M_{\mathbf B}(\Phi^w(B)^{u_N^{-1}})(c)=u_N(c_-)^{-1}e^{iB(c)}\mathbf V_0(c)u_N(c_+)=v[H_N](c_-)e^{iB(c)}\mathbf V_0(c)v[H_N](c_+)^{-1}$. Comparing with (2.1), $e^{i\tilde q(H_N)(c)}=e^{iB(c)}$. Both logarithms are in the injectivity ball, so $\tilde q(H_N)=B$ and $\mathcal Q^{\rm st}(H_N)=\mathsf b(B)$.

*Step 4 (identification on a smaller $N'$).* By Steps 2–3, $H_N$ satisfies the hypotheses of the converse of Proposition C5 with $B'=\mathsf b(B)$. All the auxiliary quantities are continuous in $B$ and vanish at $B=0$. So on a smaller real neighbourhood $N'\subset N$ they lie in the balls of (I-UNQ), and $H_N(B)=\mathbf H(B)$ for $B\in N'$.

*Step 5 (the gauge on all of $\mathfrak B_C$).* $\mathbf H(B)$ is holomorphic on $\mathfrak B_C$ ($\mathsf b$ is holomorphic with $\|\mathsf b(B)\|\le C_{\mathsf b}\|B\|<r_D$). In each connected component of the site graph of $\Omega_0$ (sites of $\Omega_0$, bonds with both ends in $\Omega_0$) choose a top $y_0$ and a rooted spanning tree. Each component contains a top: every site lies in a pillar, the pillars lie in $\Omega_0$ (SA L9599), and the ascent of a site stays in its pillar. Define $u_B$ by $u_B(y_0):=v[\mathbf H(B)](y_0)^{-1}$ and, along each tree bond $b$ from $x=b_-$ to $x'=b_+$,
\[
 u_B(x'):=\Phi^w(B)(b)^{-1}\,u_B(x)\,\big(e^{i\eta\mathbf H(B)}U_0\big)(b),
\]
and reversed bonds by inversion. It is holomorphic on $\mathfrak B_C$: a finite product of holomorphic matrices and their inverses ($\Phi^w(B)(b)\in SL(2,\mathbb C)$). On $N'$, $u_N$ satisfies the same recursion and root value, because $\Phi^w=(e^{i\eta H_N}U_0)^{u_N}$ on every bond means $\Phi^w(b)=u_N(b_-)E_N(b)u_N(b_+)^{-1}$, and $u_Nv[H_N]=\mathbf1$ at $y_0$. By induction along the tree, $u_B=u_N$ on $N'$. The identities $\Phi^w(B)(b)=u_B(b_-)(e^{i\eta\mathbf H}U_0)(b)u_B(b_+)^{-1}$ on the non-tree bonds and $u_Bv[\mathbf H]=\mathbf1$ at the other tops are holomorphic in $B$ and hold on $N'$. By (IT) on the polydisc $\mathfrak B_C$ they hold everywhere. This is (5.2). Uniqueness of the pair: a holomorphic pair with value $(0,\mathbf1)$ at $0$ and these properties is near $(0,\mathbf1)$ for small real $B$, so it equals $(H_N,u_N)$ there by Lemma 6.3's uniqueness, and equals $(\mathbf H,u)$ everywhere by (IT). This is (ii).

*Step 6 (item (i)).* By the forward direction of Proposition C5, $\mathcal Q^{\rm st}(\mathbf H)=\mathsf b(B)$ and $RD^{\mathsf T}\mathbf H=0$ on all of $\mathfrak B_C$. Put $\hat\omega(A):=\Psi_A\ell^{\mathsf T}F'(A)=\omega_1(A;J)$ and $Z(B):=F'(\mathbf H(B))-K_{\mathbf H(B)}^{\mathsf T}\hat\omega(\mathbf H(B))$, holomorphic on $\mathfrak B_C$. On $N'$, $F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\omega_N$, so $\ell^{\mathsf T}F'(\mathbf H)=(K_{\mathbf H}\ell)^{\mathsf T}\omega_N=(1+\ell^{\mathsf T}\mathsf C_{\mathbf H}'^{\mathsf T})\omega_N$ and $\hat\omega(\mathbf H)=\omega_N$; hence $Z=0$ on $N'$, and on $\mathfrak B_C$ by (IT). At $B=0$: $\mathbf H=0$, $\Psi_0=1$, $\hat\omega(0)=\ell^{\mathsf T}J=\ell^{\mathsf T}\widehat Q^{\mathsf T}\lambda_0=\lambda_0$.

*Step 7 (item (iii)).* For real $B$, (5.6) has real data and real operators (I-OPS), so its iterates and $\mathbf H(B)$ are real. $\Phi^w(B)$ is real. The recursion of Step 5 then gives a real $u_B$. By (5.2), $E=\Phi^w(B)^{u_B^{-1}}$. $\Phi^w(B)$ is critical for $C(\mathbf B,e^{iB}\mathbf V_0)$, so $E$ is critical for $C(\mathbf B,(e^{iB}\mathbf V_0)^{u_B^{-1}})$, and $u_B^{-1}=v[\mathbf H]$ at the nodes (tops). For real $g$ with $g=v^{-1}$ at the nodes, $E^g=\Phi^w(B)^{h}$ with $h=g\,u_B^{-1}$ in the composition convention $(U^a)^b=U^{ba}$; $h=v^{-1}v=\mathbf1$ at the nodes, so $h\in\mathcal G^{\rm res}$ and $E^g\in U_{\mathbf B}(e^{iB}\mathbf V_0)$. The norms in (4.2) are invariant under real gauges, so $E$ obeys (4.2) by P81(b)(iii).

*Step 8 (item (iv)).* At a bare row $b$, $\mathcal Q^{\rm st}(\mathbf H)(b)=\eta\mathbf H(b)$ (Section 2), and $\mathsf b(B)(b)=B(b)$: a bare row is an interior row of level $0$. So (i) gives $\mathbf H(b)=\eta^{-1}B(b)$. $\square$

*Four-dimensional changes.* Y3's identification uses its mean-Landau pair and the datum twist $B_\natural$; here it is SA's $R$-slice Landau pair (SA L9697–9702) of `a3-derivative.md` §6.1 and the reduced datum $\mathsf b$ of SA L9638–9646. The spanning forest is the gate's repair. Nothing else changes.

### 5.10 Proposition C7: the current

**Proposition C7.** [proved here; Y3 Proposition I-88-127, Y3 L33530–33540, is the model] Item (v) of Theorem CRIT holds. In particular, at the natural current, $J+j_1(\mathbf H;J)=J^\circ(E)$ at every bond of $\Omega_0$, and $\omega_1(\mathbf H;J)=\omega(B)$.

*Proof.* *The chart derivative.* For a bond $b$ and matrices $X$, $d/d\epsilon|_0\,e^{i\eta(A+\epsilon X)}e^{-i\eta A}=f(i\eta\operatorname{ad}A)(i\eta X)$, $f(z)=(e^z-1)/z$ (differentiate the exponential series: the derivative of $e^{Y}$ in direction $Z$ is $\int_0^1e^{sY}Ze^{(1-s)Y}ds$, and $\int_0^1e^{s\operatorname{ad}Y}ds=f(\operatorname{ad}Y)$). With the left-variation gradient $J^\circ$ and the fine pairing, $\langle F'(A),X\rangle=\langle J^\circ(e^{i\eta A}U_0),f(i\eta\operatorname{ad}A)X\rangle$. The trace pairing is $\operatorname{ad}$-skew, so $f(i\eta\operatorname{ad}A)^{\mathsf T}=f(-i\eta\operatorname{ad}A)=f_A$ and
\[
 F'(A)=f_A\,J^\circ(e^{i\eta A}U_0)\quad\text{at every bond of }\Omega_0 .
 \tag{5.11}
\]
This is `a3-derivative.md` 7.3 ("\(F'(a)=\Xi_a^{\mathsf T}J(U_a)\)") and Y3 L33529–33531 ("the local action derivative identity, at every bare bond, including incomplete boundary stars"). $f_A$ is invertible for $\eta|A|\le1/16$: $\|f(z)-1\|\le1/14$ for $|z|\le1/8$ (the series $\sum_{n\ge1}z^n/(n+1)!$), and $|\operatorname{ad}X|\le2|X|$.

*The multiplier.* By Theorem C6(i), $F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\omega(B)$, and Step 6 there shows $\omega(B)=\omega_1(\mathbf H;J)$. Then $K_{\mathbf H}^{\mathsf T}\omega_1(\mathbf H;J)=F'(\mathbf H)$, and $\widehat Q^{\mathsf T}\ell^{\mathsf T}J=\widehat Q^{\mathsf T}(\widehat Q\ell)^{\mathsf T}\lambda_0=\widehat Q^{\mathsf T}\lambda_0=J$. So $J+j_1(\mathbf H;J)=f_{\mathbf H}^{-1}F'(\mathbf H)=J^\circ(E)$ by (5.11).

*General $\mathbf J$.* By Proposition C8, $j_1(\mathbf H;\mathbf J)=j_1(\mathbf H;J)+f_{\mathbf H}^{-1}\delta-\delta$. Add $\mathbf J=J+\delta$: $\mathbf J+j_1(\mathbf H;\mathbf J)=J^\circ(E)+f_{\mathbf H}^{-1}\delta$. If $\mathbf H=0$ on $\operatorname{supp}\delta$, $f_{\mathbf H}=1$ there ($f_A$ acts bond by bond), so $f_{\mathbf H}^{-1}\delta=\delta$. $\square$

### 5.11 Proposition C8: the plain-current boundary clause

**Proposition C8.** [four-dimensional port of Y3 Lemma II-93-23, Y3 L54449–54528] Let $\delta$ satisfy (5.1). Replacing $\mathbf J$ by $\mathbf J+\delta$ leaves $\Delta'_\pi$, $G$, $\ell$, $\Sigma$, $G_1$, $\ell_1$, $\mathfrak G$, $\mathcal D$, $\mathcal L$ and $\mathsf W_1$ unchanged, so $\mathbf H$ is unchanged. It changes $\omega_1$ by $\zeta:=\ell^{\mathsf T}\delta$ and $j_1$ by $f_{\mathbf H}^{-1}\delta-\delta$. This is item (vi).

*Proof.* (1) $\Delta'_\pi[\delta]=0$: shown in the first paragraph of the proof of Lemma C2 (every $b\in\operatorname{supp}\delta$ has both endpoints at level-0 tops, where every $\lambda\in\mathcal N$ vanishes). So $G$, $\ell$, $\Sigma$ are unchanged. Y3 L54468–54473 gives the same argument in three dimensions ("the site field \(v=\mathsf VA\) … vanishes at the bare sites outside \(\Omega_1\)").

(2) $\zeta=\ell^{\mathsf T}\delta$ lives on bare rows. For a row vector $X$ and a bare row $c$, $(\widehat Q\ell X)(c)=X(c)$ and $\widehat Q(c,\cdot)=\eta\,\mathrm{ev}_c$, so $(\ell X)(c)=\eta^{-1}X(c)$. $\operatorname{supp}\delta$ consists of bare rows by (G-a). Hence $\langle\zeta,X\rangle_{\rm row}=\langle\delta,\ell X\rangle=\eta^4\sum_{c\in\operatorname{supp}\delta}\tfrac12\operatorname{tr}(\delta(c)\eta^{-1}X(c))$: $\zeta(c)=\eta^3\delta(c)$ on $\operatorname{supp}\delta$ and $0$ elsewhere. Also $\langle\widehat Q^{\mathsf T}\zeta,A\rangle=\sum_c\tfrac12\operatorname{tr}(\zeta(c)\eta A(c))=\langle\delta,A\rangle$, so $\widehat Q^{\mathsf T}\zeta=\delta$.

(3) $\mathsf C$ vanishes identically at bare rows (Section 2). So $\mathsf C_A'^{\mathsf T}\zeta=0$ and $\mathsf C''[A']^{\mathsf T}\zeta=0$ for all arguments, and $\langle A,\Delta^{(2)}[\zeta]A\rangle=2\langle\zeta,\mathsf C^{(2)}(A)\rangle=0$, so $\Delta^{(2)}[\zeta]=0$. Hence $G_1$, $\ell_1$, $\mathfrak G$ are unchanged. $\mathcal D$, $\mathcal L$ use only $\mathsf C$ and $\ell$.

(4) In (5.5) only the first term contains $\mathbf J$ explicitly. Its change is $-(\mathfrak D^{\mathsf T}-\mathsf C''[A']^{\mathsf T})\zeta$. By Lemma C3(iv), $\mathfrak D^{\mathsf T}\zeta=\mathsf C_T'^{\mathsf T}(1+\ell^{\mathsf T}\mathsf C_T'^{\mathsf T})^{-1}\zeta=\mathsf C_T'^{\mathsf T}\zeta=0$, because $(1+\ell^{\mathsf T}\mathsf C_T'^{\mathsf T})\zeta=\zeta$. So $\mathsf W_1$ is unchanged, (5.6) is the same system, and $\mathbf H$ is unchanged. (Y3 L54499–54506: "Its change is \(-\mathsf C'_{\mathcal L}{}^{\mathsf T}\Psi_{\mathcal L}\zeta+\mathsf C''[A']^{\mathsf T}\zeta=0\)".)

(5) By (5.7), $\omega_1$ changes by $\Psi_{\mathbf H}\zeta=\zeta$ (as $\mathsf C'^{\mathsf T}\zeta=0$), and $j_1$ by $f_{\mathbf H}^{-1}K_{\mathbf H}^{\mathsf T}\zeta-\widehat Q^{\mathsf T}\zeta=f_{\mathbf H}^{-1}(\widehat Q^{\mathsf T}\zeta+\mathsf C_{\mathbf H}'^{\mathsf T}\zeta)-\delta=f_{\mathbf H}^{-1}\delta-\delta$. $\square$

### 5.12 Corollary C9: what ST1 reads

**Corollary C9.** [proved here] Items (vii) and (viii) of Theorem CRIT hold.

*Proof.* (vii) Take $\mathbf J=J_+$; $\delta=J_+-J^\circ(U_0)$ is supported on the incomplete-star bonds, which lie within $\eta$ of $\Omega_0^c$. Let $b$ be such a bond. Every plaquette through $b$ has all its bonds within $2\eta$ of $\Omega_0^c$, hence bare rows by (G-b). By hypothesis $B=0$ on them, so $\mathbf H=0$ on them by (iv); in particular $\mathbf H=0$ on $\operatorname{supp}\delta$. By (v), $J_++K=J^\circ(E)+\delta$ everywhere. At an incomplete-star bond $b$: $E=U_0$ on every inner plaquette through $b$, so $J^\circ(E)(b)=J^\circ(U_0)(b)$, and $J_+(b)+K(b)=J^\circ(U_0)(b)+J_+(b)-J^\circ(U_0)(b)=J_+(b)$: $K(b)=0$. At a complete-star bond, $\delta=0$ and $J^\circ=J_\eta$, so $J_++K=J_\eta(E)$. So the current of $(U_0,\mathbf H,J_++K)$ is $J_\eta(E)$ on complete stars and $0=J_+(b)$ on incomplete stars, where $J_+(E)$ is also $0$: this is the plain current $J_+(E)$, and the pair is $(E,J_+(E))$.

(viii) In (5.6)–(5.7) the quantities $\eta A$ (bondwise group elements), $\eta^2\nabla A$, $\eta^3\mathbf J$, the rows $\mathcal Q^{\rm st}$ (dimensionless) and the pairings are invariant under the change of level units: $\eta\mapsto L^m\eta$, $A\mapsto L^{-m}A$, $\mathbf J\mapsto L^{-3m}\mathbf J$ (`st1.md` (5): "Thus \(\eta A'\), \(\eta^2\nabla A'\), and \(\eta^3\mathbf J\) are invariant"). The fine pairing of a current with a potential is $\eta^4\sum_b\tfrac12\operatorname{tr}(\mathbf J A)=\sum_b\tfrac12\operatorname{tr}\big((\eta^3\mathbf J)(\eta A)\big)$, also invariant. So every identity of Sections 5.4–5.11 holds in either unit system with the same group elements. At a main step the reference triple is recorded at level $t$, the old system at level $t-1$; converting the triple to level-$(t-1)$ units multiplies its current by $L^{-3}$, and (vii) reads $L^{-3}J_+^{(t)}+K=J(E)$ at complete stencils. $\square$

**How ST1 uses this.** In `st1-draft2.md` Theorem D4, take $\mathbf B$ the old system, $U_0=U_+$ (critical for the old system by Lemma DM, regular at a smaller radius since $\mathsf L^-\le\mathsf L^+$), $\mathbf V_0=V=M_-(U_+)$, $B:=i^{-1}\operatorname{Log}(D_{\rm old}V^{-1})$, so that ST1's $B'_Y=\mathfrak b_V(D_{\rm old})=\mathsf b(B)$ (`st1-draft2.md` (44)). Then CRIT (iii) is D4(1); (vii) is D4(2) and the current part of D4(3); (iii)'s bound is D4's regularity step, now proved without a separate uniqueness argument; (vii)'s support hypothesis is ST1's statement that the source rows are "all interior to \(\Omega^-_0\)". Proposition DR's current relation $J(U_{\sigma_k})=J(U_{\sigma_{k-1}}^{g_k^{-1}})-K_k$ is (vii) read backwards. CRIT says nothing about whether $D_{\rm old}$ is in the chart; that is FL's complex contour bound in ST1.

### 5.13 Constants

| Constant | Source | Row | Before $\kappa_{\rm IN}$ | Free of $M$, $\bar\kappa$ |
|---|---|---|---|---|
| $a_0,\bar\varepsilon,r_B,C_\Phi$ | P81 | 7 | yes | yes |
| $r_D$, the contraction balls, $B_0$, $C_2$, $C_4$ | (I-UNQ) | 4–7 | yes | yes |
| $C_{\mathsf b}$ | reduced datum, SA L9646 | 3 | yes | yes |
| $r_C=\min\{r_B,r_D/C_{\mathsf b}\}$ | (5.1) ff. | 7 | yes | yes |
| the bound $1/14$ on $f_A-1$, $\eta|A|\le1/16$ | Proposition C7 | absolute | yes | yes |

No constant is introduced by Lemmas C1–C4, Proposition C5 or C8: they are identities. The neighbourhoods $N,N'$ of Theorem C6 are not constants and enter no bound (T4). At $s\equiv\mathbf1$ there is no decoupling polydisc, so $\bar\kappa$ cannot enter, and $M$ occurs nowhere.

### 5.14 Four dimensions, collected

1. Six plaquettes per bond in four dimensions, four in three. This enters no identity. It enters DR's natural-class radius for the regional current at incomplete stars ($\le5a_m\xi_0^{-3}$), which is ST1's business (`st1-draft2.md` D4, "radius \(6a_m\)").
2. The scalar boundary term $8-n(x)$; it vanishes on $\ker Q'$ (Lemma C1(C1.2)).
3. SA's $R$-slice with the pillar mean $Q'$ and contour transports, in place of Y3's mean-Landau projection; counting row pairing (M1) in place of Y3's $\xi_c^{-1}$-weighted rows. All identities are pairing-consistent and use only that $R$ is the orthogonal projection onto $\ker(Q'G')$.
4. Outward rows and the reduced datum $\mathsf b$ (SA L9638–9646); handled by (2.1) with node factors of each node's own level.
5. SA leaves $\mathsf W_s$ and $j_s$ unwritten; (S1) fixes their $s\equiv\mathbf1$ values from Y3.
6. The identification through P81's $\Phi$ (Balaban's background, four-dimensional) and `a3-derivative.md` Lemma 6.3, in place of Y3's I-88-131 inputs.

**Status of CRIT: proved**, as an implication from P81, (I-6), (I-OPS), (I-UNQ), DR1, with (S1) as its specification. Inside CRIT nothing is Outstanding.

---

## 6. What changes elsewhere (for the lead; no other file edited)

1. `st1-draft2.md` §15.2, item 2 (CRIT) and item 5 (P81): both proved as implications here. ST1's open list then starts at LEV and CORE (its items 3, 4). Item 1 (P82°) is drafted in `p82-draft.md`.
2. `st1-draft2.md` Theorem D4, item 3: replace "$H=0$ on the bare determining rows (no endpoint in $\Omega_1$)" by "$H=\eta^{-1}B'$ on the bare rows; $H=0$ on the bare rows outside the source, in particular within $2\eta$ of $\partial\Omega^-_0$" (Theorem CRIT (iv), (vii); test T2). D4's proof step (2) can cite Proposition C8 for "the potential is the same, and the current increments are equal", and step (4) can cite CRIT (iii) for regularity and orbit membership directly.
3. The DR lane (`dec-field.md`, `nl-r9.md`, `ym4-assembly.md` PR1(2)): the decoupled specification of $\mathsf W_s$ and $j_s$ must have the $s\equiv\mathbf1$ value (S1), up to maps into $\mathcal K^\perp$ at slice points (Section 5.2(e)). Y3's six-term $\mathsf W_s$ and (decoupled-current-definition) satisfy this. DR1 (resummation at $s\equiv\mathbf1$) is part of DR.
4. `a3-derivative.md` §12, open item (2) (P81), and the verdict table (line 548): TH4's first paragraph now rests on P81 (Theorem P81 here), P82° (`p82-draft.md` Theorem P82) and M1 (a convention, `a3-close.md` §4). With these, Theorem 4's first paragraph is an implication from FP1 and the A1 port.
5. `a3-derivative.md:56`: $\kappa=C_L\mathfrak M\bar\varepsilon$ can be sharpened to $\kappa=C(L)\varepsilon_1$ (Lemma 81.3); nothing downstream needs the sharpening.
6. `a1-balaban.md` §6 and §8: the "localization length $R_1M_1$" is $\ell_R$, a row-4 constant, distinct from the outline's gap $\rho=R_1\mathfrak M$; the gap needs $\rho\ge6L\ell_R$ (Section 4.8). Notation only.

---

## 7. Status table

| Step | Statement | Status | Rests on |
|---|---|---|---|
| §4.3 | P81(a) orbit, bounds, axial element | proved | (I-A1) (8.2), §9.1 |
| Lemma 81.2 | P81(b) chart, real-data identification, uniqueness, residual-gauge covariance | proved | (I-A1) §9.1, G99.D; (IT) |
| Lemma 81.3 | P81(c) gauges on row carriers, $\kappa=C(L)\varepsilon_1$ | proved | (I-REG), (4.1), separation |
| §4.6, Lemma 81.4 | P81(d) restriction; towers, meets, truncations | proved | (I-A1) (9.3); SA L9650–9652, L10212 |
| Corollary 81.5 | P81(e) overlaps; $T_e$ well defined | proved | P81(b); `st1.md` (25); (IT) |
| §4.8 | P81 constants; the $\ell_R$ clash | proved (each condition a lower bound or ceiling by earlier numbers) | `c4-order.md` rows 3–7 |
| Lemma C1 | gauge identities at a real critical reference | proved | (2.1), Lemma 6.1 of (I-6) |
| Lemma C2 | linear identities on shell | proved | Lemma C1, (I-OPS) |
| Lemma C3 | straightening | proved | (I-UNQ) |
| Lemma C4 | reduced-action identity | proved | Lemmas C2, C3 |
| Proposition C5 | (R9) at $s\equiv\mathbf1$ ⟺ slice stationarity; = (I-UNQ)'s chart system | proved | Lemmas C2–C4, Lemma 6.2 at $0$ |
| Theorem C6 | CRIT (i)–(iv) | proved | P81(b), Lemmas 6.2, 6.3, Proposition C5, (I-UNQ), (IT) |
| Proposition C7 | CRIT (v) | proved | Theorem C6, (5.11), Proposition C8 |
| Proposition C8 | CRIT (vi) | proved | Section 2, Lemma C3(iv) |
| Corollary C9 | CRIT (vii), (viii) | proved | Propositions C7, C8, (G-b) |
| §5.13 | CRIT constants | proved | P81, (I-UNQ) |

**Outstanding inside P81 and CRIT: none.**

What the imports rest on. (I-A1) and (I-OPS), (I-UNQ) are Codex's `a1-balaban.md`, checked once by Claude (`gates/a1-balaban-gate.md`), conditional on F0. (I-F0) is Codex's `flat-port.md`, checked once by Claude (`gates/flat-port-gate.md`); it rests on Balaban CMP 89, 95, 96 as ported there. (I-REG) is Claude's `a3-close.md` §1 as rewritten in `p82-draft.md` §11, checked once by Codex (`gates/a3-close-meet-gate.md` §A). (I-6) is Claude's continuation of `a3-derivative.md`, checked once by Codex with the repairs used here (`gates/a3-derivative-gate.md` §6.1). DR1 is a property of the DR specification. This draft has had no check.

---

## 8. Sources read in this session

| Source | Lines | What was read |
|---|---|---|
| SA `ym4.tex` | 5730–5830 | (R7)–(R11): triples, shift law, (R9), the reduced current, the s=1 sentence (5800–5803) |
| SA | 9593–9668 | (1b) setting, variational problem, chart, reduced datum, complex fields, towers, Theorem 1 |
| SA | 9669–9745 | contour-mean remark, Theorems 2, 3, 4 |
| SA | 9886–9896 | mechanism 7 (as located; not needed in the end) |
| SA | 10103–10212 | (1c) setting, regular pairs, on shell, operators, (explicit-current-continuation), $\mathfrak G$, notation |
| SA | 10296–10308 | statements 3 and 4 |
| SA | 10340–10470 | "The response and its independent current", the s=1 identification (10446–10458) |
| SA | 10558–10582 | remarks (j) operators as data, (k) slice to multiplier |
| Y3 `YM3_I.tex` | 26236–26256 | (bg-current-form) |
| Y3 | 26770–26816 | Proposition I-86-52, (I-86-62) |
| Y3 | 28228–28470 | Theorem I-88-93, gauge identities, action on the slice, (I-88-75)–(I-88-76) |
| Y3 | 33100–33290 | multiplier estimate, energy identity, (decoupled-current-definition) |
| Y3 | 33440–33640 | resummation at one, Proposition I-88-127, Corollary I-88-131 |
| Y3 | 54441–54530 | Lemma II-93-23 |
| library | `st1-draft2.md` 1–71, 196–274, 640–851, 906–983; `st1.md` whole; `a3-derivative.md` 1–250, 290–562; `p82-draft.md` 1–208, 476–616; `a1-balaban.md` 1–141, 196–212, 690–707, 725–1104, 1186–1356, 2339–2777; `dec-field.md` 1–20, 225–365; `wf-c.md` 1–50, 110–126, 233–274; `ym4-assembly.md` 160–215; `in1-draft.md` 800–812 and the A.5–A.7 lines; `c4-order.md` table | as cited |
| gates | `a1-balaban-gate.md` whole; `a3-derivative-gate.md` 1–50, 214–230; `flat-port-gate.md` whole | as cited |

CA-I was not needed: no CA-I statement is consumed by P81 or CRIT. Nothing was copied from Balaban's papers; claims about his text are taken from the library notes and gates named at each use, which read the scans.

**Method.** No numeric job, no subagent, no commit. Only this file was written.

## Result

**P81 is proved** as an implication (Theorem P81): on every separated sequence of the default determining set, every real $\varepsilon_1$-regular datum has one regular critical $\mathcal G^{\rm res}$-orbit with the bounds (4.1) and one axial element; its chart $\Phi$ is holomorphic on a uniform polydisc with $M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0$, complex regularity (4.2) and $\Phi(B)=U^\circ(e^{iB}\mathbf V_0)$ at real $B$; every row carrier has a regular local gauge with $\kappa=C(L)\varepsilon_1$; restriction is exact on subordinate separated sequences, towers and meets included; and the charts agree on overlaps. It rests on Balaban's critical orbit as ported in `a1-balaban.md` (one check, by Claude), on F0 (`flat-port.md`, one check, by Claude) and on Proposition REG (one check, by Codex).

**CRIT is proved** as an implication (Theorem CRIT): at $s\equiv\mathbf1$ over a real regular critical pair on shell, the response of (R9) with the specification (S1) solves the straightened constraint, the Landau condition and the multiplier equation on the whole uniform polydisc; it is the potential of SA Theorem 3's Landau pair, so the shifted field is a gauge transform of the old background by the recorded node factors, real and regular at real data; its multiplier current gives the shifted regional current exactly; and replacing the regional current by the plain current changes neither the potential nor anything but the explicit boundary term, which vanishes when the source misses the bare rows at $\partial\Omega_0$. It rests on P81, `a3-derivative.md` Lemmas 6.1–6.3 (one check, by Codex), the operators and chart contraction of `a1-balaban.md` §§3.9, 4, 9.1, and DR's resummation at $s\equiv\mathbf1$.

No Outstanding statement remains inside either part. One consumer statement is corrected (`st1-draft2.md` D4(3)). All constants are row-7 constants or earlier, fixed before $\kappa$, independent of $M$ and $\bar\kappa$.

This is research text. It grants no status, and no other model has checked it.
