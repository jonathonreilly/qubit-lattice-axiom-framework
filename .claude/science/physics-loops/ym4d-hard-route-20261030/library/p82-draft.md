# P82°, pass 1 (long draft): the weighted inverse at a curved real critical reference

Submanuscript PR1 (propagators on a background) of our proof of T0. Pass 1 of four: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), one session, 2026-11-04, working in a clone of the planning folder (`library/`, `gates/`); nothing committed. Sources read in bounded ranges: the Sussman–Alpoge outline `ym4.tex` at `31a47c543775` (lines quoted below), the complete account `ca_I.tex` (CA-I) and the three-dimensional account `YM3_I.tex` (Y3), all in the session scratch folder. Research text, not an audit. It grants no status.

Credit. T. Balaban for the whole architecture: background propagators by localization to cubes that carry a small gauge, perturbation from the flat propagators in that gauge, and the random-walk summation (CMP 99 (1985) 389–434, Corollaries 3.5–3.6, (3.35)–(3.47), (3.87)–(3.90)); the regular class and the local-gauge proposition (CMP 99 (1985) 75–102, (1.7)–(1.9), Proposition 6); the flat inputs (CMP 89, 95, 96); the averaging (CMP 98); the background (CMP 102). J. Dimock for the flat-propagator exposition used in FP1 (Dimock II Theorem 2.2; QED₃, arXiv 1712.10029, Section 3). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's setting, the regular-pair class, the straightened rows, the pillar mean \(Q'\), the projection \(R\), the metric \(d_{\mathbf B}\), the kernel conventions (BGR10)–(BGR13), mechanism (f) and Theorem 4; and for the complete account and the three-dimensional account read below. OpenAI Codex for `flat-port.md`, `a3-balaban.md`, `a1-balaban.md` and Sections 1–6 of `a3-derivative.md`, and for the gates `p82-curved-gate.md` and `a3-close-meet-gate.md`. Claude for `p82-curved.md`, `a3-close.md`, the continuation of `a3-derivative.md`, and the gates `flat-port-gate.md`, `a1-balaban-gate.md` and `a3-balaban-reads-gate.md`.

Status words. **Proved** means: every step is written here, from the named imports. **Import** means a statement taken from another library file, with its check record. **Outstanding** means: not proved. No step is computer-assisted. Every argument is finite-dimensional linear algebra, elementary inequalities, geometric series, or discrete potential theory on finite lattices, and is Lean-formalizable in that sense.

---

## 0. Result

**P82° is proved**, as an implication from eight imports (I1)–(I8) of Section 5. Each import has had one check by hand by another provider, with first failing step none (records in Section 5). The proof is Theorem P (Section 3) on the whole real regular class, plus Proposition REG, which puts the critical reference in that class. Constants depend on \(L\) and the Hölder exponent only. They are fixed before \(\kappa_{\rm IN}\) and are independent of the construction size \(M\), of \(\bar\kappa\), of the depth, the mesh, the volume and the region shapes (Section 13, constant by constant).

No step inside P82° is Outstanding. The draft repairs four defects of the earlier texts, all non-breaking: the Nielsen–Olesen heuristic (Codex's D1), the sharp-source decay lemma (Codex's D2), the curl comparison on bare cells (Codex's D3), and a notation clash in `a3-close.md` §1 that, read literally, makes its gap condition unsatisfiable (Section 2.3, item 3). Its consumers still need P81 (row 81), which is not part of P82°.

What P82° does not cover is listed in Section 14.3: complex references, the independent-current system, and the \(\mathbf V_0=\mathbf 1\) periodisation clause. These belong to other PR1 clauses. They are not on the path from P82° to Theorem 4's first paragraph.

---

## 1. The target, exactly

### 1.1 Where P82° is stated

`a3-derivative.md` §12 lists it first among the open items (line 556):

> "(1) **P82°, row 82:** the weighted inverse of \(S^\circ\) at a real, curved, regular critical reference, with the outline's \(R\) and \(K_0\), the Hölder member, \(D(1-R)D^{\mathsf T}:X_w\to F_w\), and BGR11 row sums at rate \(\theta\), uniformly in depth. It is the only quantitative input, and it is where this route fails if it fails."

The verdict table (line 548) rests Theorem 4's first paragraph on "P81, P82° (Lemma 8.1), M1". The precise premise is Lemma 8.1 (line 474):

> "Let \(S^\circ=\begin{pmatrix}D^{\mathsf T}D+DRD^{\mathsf T}&-K_0^{\mathsf T}\\K_0&0\end{pmatrix}\) at the real regular reference. Suppose \(S^\circ\) has the bounds (4) with constant \(C^\circ\), the Hölder member and the member \(D(1-R)D^{\mathsf T}:X_w\to F_w\). Then Sections 6–7 hold with \(S^\circ\) in place of \(S_0\), once \(\kappa\) and \(r\) are small with respect to \(C^\circ\)."

Here \(D^{\mathsf T}D\) is the curl form of the action's quadratic part (the forward curl, or the plaquette curl of SA (PX114); `gates/a3-derivative-gate.md` §7 asks for the plaquette curl). Bound (4) of `a3-derivative.md` (lines 69–74) is

\[
 \|Tf+Hb\|_{X,w}+\|-H^{\mathsf T}f+(C_0^{-1}-1)b\|_{Y,w}\le C^\circ(\|f\|_{F,w}+\|b\|_{Y,w}),
 \tag{1.1}
\]

and Lemma 8.2 (line 478) fixes its meaning: (1.1) must hold for **every** \(w\in\mathcal W_\theta\), the class of positive weights with \(w(y)\le e^{\theta d_{\mathbf B}(y,z)}w(z)\); this is equivalent to the first-line row sums of SA (BGR11) at rate \(\theta\). Lemma 8.1's proof (line 476) moves \((\Delta'-W_0)a\) into the nonlinear remainder, so P82° carries no current correction and no constraint-curvature term.

`st1-draft2.md` §15.2 (line 932) lists P82° first among ST1's open imports: "the weighted inverse at a real curved regular critical reference with the outline's \(R\) and \(K_0\); it is the linear input of TH4, and so of Theorem T and Theorem D4." TH4 (lines 211–217) is SA's Theorem 4 at a real regular critical reference.

### 1.2 The consumer chain

SA Theorem 4 (SA L9734–9740) reads, in its first paragraph: "Let \(\bar\varepsilon\le c(L)/\mathfrak M\), with \(\bar\varepsilon\) chosen after \(\mathfrak M\). … Then on the whole polydisc, over the top \(y\), \(\xi_y|\mathsf h|,\xi_y^2|\nabla\mathsf h|,\xi_y^3|D^{\mathsf T}D\mathsf h|,\xi_y^3|\Delta_{U_0}\mathsf h|,\xi_y^3|\delta J|\le Ce^{-c\delta_0d_{\mathbf B}(y,y_c)}|e|\), together with a Hölder member". `a3-derivative.md` §§6–7 proves it from P81, P82° (through Lemma 8.1) and M1 (line 548; M1 is settled as a convention in `a3-close.md` §4, checked by Codex in `gates/a3-close-meet-gate.md` §C). ST1's Theorem T (`st1-draft2.md` §7.8) reads TH4. ST1's Theorem D4 reads Theorem T. So:

\[
 \text{P82°}\ \xrightarrow{\ \text{Lemma 8.1}\ }\ \text{SA Theorem 4 (TH4)}\ \longrightarrow\ \text{ST1 Theorem T}\ \longrightarrow\ \text{(D4)}.
\]

### 1.3 What the earlier texts did, and what this pass adds

`p82-curved.md` (Claude) proved P82° on a real regular class (its Theorem P). Codex checked it in `gates/p82-curved-gate.md`: three defects D1–D3, all repaired there, "Repaired result: ADVANCE, as an implication only" (line 237). `gates/a3-balaban-reads-gate.md` (Claude) checked every `a3-balaban.md` statement that Theorem P reads: first failing step none (line 24). `gates/flat-port-gate.md` (Claude) checked the flat package: first failing step none. `a3-close.md` §1 (Claude) proved that the critical reference lies in the class; Codex checked it in `gates/a3-close-meet-gate.md` §A: "ADVANCE as an implication", first failing step none.

So the pieces exist and each has one cross-provider check. The library does not yet hold one text with the repairs built in, the reference-class step attached, and the constants checked against IN1's order. `st1-draft2.md` (line 932) still lists P82° as open, without citing `p82-curved.md`. This draft is that one text. Every step is rewritten, the repairs are built in, and three points are new:

1. the parametrix is organised so that the curved commutator never has to be estimated: only the flat model's commutator and a coefficient difference occur (Proposition 8);
2. the bare-cell curl repair is built in from the start, one system for both curls (Sections 6–10);
3. a notation clash in the reference-class step is resolved (Section 2.3), and the order of constants is checked against `c4-order.md` and IN1 (Section 13).

---

## 2. Setting, operators, norms

### 2.1 Geometry (SA L10113–10127, L9593–9602)

Fix an odd \(L\). Work in level-\(k\) units: bare spacing \(\eta=L^{-k}\), level-\(j\) scale \(\xi_j=L^j\eta\). A **separated sequence** \(\mathbf B\) is \(\Omega_0\supset\Omega_1\supset\dots\supset\Omega_k\) in a torus, each \(\Omega_j\) a union of aligned level-\(j\) cubes of side \(M_1\xi_j\), with \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\,\xi_j\), \(\rho=R_1M_1\). The layers are \(\mathcal L_j=\Omega_j\setminus\Omega_{j+1}\). The local scale \(m(x)=\xi_j\) on \(\mathcal L_j\); on bonds take the larger endpoint scale. Tops \(y\) carry pillars \(P_y\) and scale \(m_y=\xi_y\). Rows \(c\) are interior or outward (no inward rows), with assigned top \(y_c\). The metric \(d_{\mathbf B}\) is the infimum over curves \(\Gamma\) of \(\sum_{j\ge1}\xi_j^{-1}{\rm length}(\Gamma\cap\mathcal L_j)+\eta^{-1}{\rm length}(\Gamma\setminus\Omega_1)\) (SA 9602, as checked in `gates/a3-balaban-reads-gate.md` R2).

Pairings: fine \(\langle a,b\rangle=\eta^4\sum_b\operatorname{tr}\), counting row pairing \(\sum_c\operatorname{tr}\), physical top pairing with weight \(m_y^4\). Transposes \({}^{\mathsf T}\) are taken in these pairings.

### 2.2 Operators at a real configuration \(U\)

- \(D=D_U\): scalar covariant gradient with start-point transport, \((D\lambda)(b)=\eta^{-1}[\operatorname{Ad}U(b)\lambda(b_+)-\lambda(b_-)]\); \(\Delta_U=D^{\mathsf T}D\) on sites.
- \(\nabla_U\): covariant start-point differences of the components of 1-forms.
- Two curls. \(d=d_U\): the forward curl \((dA)_{\mu\nu}=\nabla_\mu A_\nu-\nabla_\nu A_\mu\). \(\mathfrak d=\mathfrak d_U\): the plaquette curl of SA (PX114) (SA L11313–11327), \(\mathfrak dA(p)=\eta^{-1}\sum_{r=1}^4\operatorname{Ad}(T_{r-1})A(b_r)\), where \(T_{r-1}=U(b_1)\cdots U(b_{r-1})\) and reversed bonds carry \(A(\bar b)=-\operatorname{Ad}(U(b)^{-1})A(b)\). The two agree at \(U=\mathbf 1\). Write \(\flat\in\{d,\mathfrak d\}\).
- \(Q'=Q'_U\): the outline's pillar mean (SA 9634), with contour-mean transports (SA 7065). It is not the comb projection \(R^{\mathsf c}\).
- \(A_s=D^{\mathsf T}D+Q'^{\mathsf T}m^{-2}Q'\), \(S=A_s^{-1}\), \(N=(Q'S^2Q'^{\mathsf T})^{-1}\), \(R=1-SQ'^{\mathsf T}NQ'S\), \(P=1-R\).
- \(K=K_U\): the derivative at \(A=0\) of the straightened rows \(\mathcal Q^{\rm st}(U;A)\) of \(e^{i\eta A}U\) in the raw (dimensionless) normalization; \(K_0\) of `a3-derivative.md` is \(K_{U_0}\).
- The target operator, for either curl:
\[
 S^\circ_\flat=\begin{pmatrix}\flat^{\mathsf T}\flat+DRD^{\mathsf T}&-K^{\mathsf T}\\ K&0\end{pmatrix},\qquad
 G=(\flat^{\mathsf T}\flat+DRD^{\mathsf T}+K^{\mathsf T}K)^{-1},
\]
with \(C_0=KGK^{\mathsf T}\), \(H=GK^{\mathsf T}C_0^{-1}\), \(T=G-HKG\), so that \(S^{\circ-1}_\flat(f,b)=(Tf+Hb,\,-H^{\mathsf T}f+(C_0^{-1}-1)b)\) (`a3-derivative.md` (27), re-derived in its §11).

Norms (`a3-derivative.md` (2)): for a positive weight \(w\),
\[
 \|a\|_{X,w}=\sup_yw(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla_Ua|_y\},\quad
 \|f\|_{F,w}=\sup_yw(y)\xi_y^3|f|_y,\quad
 \|b\|_{Y,w}=\sup_cw(y_c)|b(c)|,
\]
where \(|\cdot|_y\) is the supremum over the bonds assigned to the pillar of \(y\), stencils included. \(\mathcal W_\theta=\{w>0:\ w(y)\le e^{\theta d_{\mathbf B}(y,z)}w(z)\ \forall y,z\}\).

### 2.3 Three notation clashes, resolved

1. **\(\kappa\).** `a3-derivative.md` writes \(\kappa=C_L\mathfrak M\bar\varepsilon\) for the curvature size of the reference (line 56). IN1 and `c4-order.md` row 8 write \(\kappa\) for the decay rate of the induction. Here \(\kappa_{\rm A3}\) is the first and \(\kappa_{\rm IN}\) the second. "Fixed before \(\kappa\)" in the brief means before \(\kappa_{\rm IN}\).
2. **Three lengths called \(M\).** \(M_P\) is the tile size of the parametrix (`p82-curved.md` calls it \(M\); `c4-order.md` row 4 calls it \(m_w\)). \(M_1=\mathfrak M\) is the cube size of the separated sequences (`c4-order.md` row 6; SA L9599: "distinct from localisation size"). \(M\) is the construction cube size (`c4-order.md` row 12). Theorem P uses only \(M_P\), and needs \(M_P\mid M_1\).
3. **\(W\) in `a3-close.md` §1.** That text puts "\(W:=R_1M_1\) the walk length of Balaban's propagator theorems used in the gauge theorem of `a1-balaban.md` §3.8" and requires \(\rho_0'\ge4LW+2L\). If \(R_1M_1\) meant the outline's gap \(\rho=R_1M_1\), this would read \(\rho\ge4L\rho+2L\), which no \(\rho\) satisfies. The construction it cites (`a1-balaban.md` lines 708–711: "Around its cube choose successively larger cubes with gaps \(R_1M_1s_n\) … Apply the gauge theorem to this field with reference 1. Its inverse inputs are the flat ones") builds an **auxiliary** nested family around one cube and applies the gauge theorem at reference \(\mathbf 1\). That application needs only the flat package on the auxiliary family. The flat package holds on every separated sequence whose gap is above its own floor (`flat-port.md` §8.2, line 550: "Choose \(\rho>C_LML\)"; §12: only lower bounds). So the auxiliary gap can be any fixed number \(W_\natural\) above the flat floor, chosen with \(L\) alone. `c4-order.md` row 4 lists exactly such a constant ("collar/reset widths \(W\)"), before row 6, where \(\rho\) is chosen. Below, \(W_\natural\) is that constant, and \(\rho\ge4LW_\natural+2L\) is a lower bound on \(\rho\) by a number already fixed. Codex's check of `a3-close.md` §1 (`gates/a3-close-meet-gate.md` §A.2) accepted the condition without comment. This is a notation defect, not a gap.

---

## 3. The statements

**Hypothesis (Reg\(_\alpha\)).** For every \(j\ge0\) and every cube \(Z\) of side \(c_{\rm reg}M_P\xi_j\) with \(Z\subset\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\), there is a real gauge \(g\) on \(Z\) with \(U^g=e^{i\eta A}\) on the bonds of \(Z\) and
\[
 \xi_j|A|+\xi_j^2|\nabla A|\le\alpha\quad\text{on }Z,
\]
\(\nabla\) the ordinary difference. This is the gauge clause of the outline's regular pairs (SA L10129–10137: "on every cube of side \(O(M_1\xi_j)\) contained in \(\mathcal L_j\cup\mathcal L_{j+1}\), to admit a real gauge \(U=e^{i\eta A}\) with \(\xi_j|A|,\xi_j^2|\nabla A|\le\alpha_0\). In this condition the bound is \(\alpha_0\) on the entire cube"), with the cube side \(c_{\rm reg}M_P\xi_j\) in place of \(O(M_1\xi_j)\). Since \(M_P\le M_1\), Reg\(_\alpha\) asks less. No criticality and no current bound is assumed: \(S^\circ\) contains no current.

**Theorem P (P82° on the real regular class).** Fix \(L\ge L_0\) and \(\alpha_{\rm H}\in(0,1)\). There are \(M_P\) (a power of \(L\)), \(c_{\rm reg},\rho_P,\alpha_*,\theta_0>0\) and \(C^\circ\), depending only on \(L\) and \(\alpha_{\rm H}\), such that the following holds for both curls \(\flat\in\{d,\mathfrak d\}\), for every separated sequence with \(M_P\mid M_1\) and \(\rho\ge\rho_P\), of any depth, mesh, volume and region shape above the torus floors, and for every real \(U\) satisfying Reg\(_\alpha\) with \(\alpha\le\alpha_*\).

- (a) \(S^\circ_\flat\) is invertible, \(K\) is onto, and \(\Delta_U:\ker Q'\to\operatorname{ran}R\) is an isomorphism.
- (b) For every \(0\le\theta\le\theta_0\) and every \(w\in\mathcal W_\theta\), the bound (1.1) holds with \(C^\circ\).
- (c) For \(a=Tf+Hb\): \(\sup_yw(y)\,\xi_y^{2+\alpha_{\rm H}}[\nabla_Ua]_{\alpha_{\rm H},y}\le C^\circ(\|f\|_{F,w}+\|b\|_{Y,w})\), the Hölder quotient taken at separations at most \(\xi_y\), with the covariant comparison along a straight path.
- (d) \(\|D(1-R)D^{\mathsf T}a\|_{F,w}\le C^\circ\|a\|_{X,w}\).
- (e) Every block of \(S^{\circ-1}_\flat\), the gradient output components included, has the first-line BGR11 row sums at rate \(\theta\).

**Proposition REG (the critical reference is in the class).** Let \(\mathbf V_0\) be a real \(\varepsilon_1\)-regular datum on a separated sequence with \(\rho\ge\max\{\rho_P,4LW_\natural+2L\}\), and let \(U_0=U^\circ(\mathbf V_0)\) be the axial representative of A1 (`a1-balaban.md` (8.2)). There are \(C_{\rm reg}\) and \(a_{\rm reg}>0\), depending on \(L\) only, such that if \(C_{\rm reg}M'\varepsilon_1\le a_{\rm reg}\), \(M'=c_{\rm reg}M_P+2W_\natural\), then \(U_0\) satisfies Reg\(_\alpha\) with \(\alpha=C_{\rm reg}M'\varepsilon_1\).

**Theorem P82 (P82° at the curved real critical reference).** Under the hypotheses of Proposition REG and \(\varepsilon_1\le\varepsilon_P:=\min\{\alpha_*,a_{\rm reg}\}/(C_{\rm reg}M')\), conclusions (a)–(e) of Theorem P hold at \(U=U_0\), with \(K=K_0\), for both curls, with the constants of Theorem P. In particular the premise of `a3-derivative.md` Lemma 8.1 holds with \(C^\circ\) and with any rate \(\theta\le\theta_0\); the consumer's \(\theta=\delta_0/8\) is admissible with \(\delta_0:=2\theta_0\).

*Proof of Theorem P82, given Theorem P and Proposition REG.* Proposition REG gives Reg\(_\alpha\) at \(U_0\) with \(\alpha=C_{\rm reg}M'\varepsilon_1\le\alpha_*\). Theorem P applies. \(\square\) The rest of this draft proves Theorem P (Sections 6–10) and Proposition REG (Section 11).

---

## 4. What changes at a curved real critical reference

### 4.1 The checked cases

At \(U=\mathbf 1\) the flat package FP1 is checked (`ym4-assembly.md` FP1, status [C]; `gates/flat-port-gate.md`, "first failing step none"). It gives the inverse of the enlarged local system, and through it P82° at the flat reference (`flat-port.md` §§8–9; gate: "The flat part of P82 (row 98) is supplied"). A single layer has no seams, rows of one height and no outward rows. The curved real case on many layers differs in exactly seven places. Each is handled by one named step.

| # | What changes | Why it could break uniformity | Where it is handled |
|---|---|---|---|
| C1 | Coefficients \(d,\mathfrak d,D,K,Q'\) depend on \(U\); no global gauge makes \(U\) close to \(\mathbf 1\) | a global perturbation from FP1 has an \(O(1)\) or growing perturbation (Attack A below) | cell gauges from Reg\(_\alpha\), localized parametrix (Proposition 8) |
| C2 | Rows of height \(j\) are \(j\)-fold compositions of curved one-step averages | relative errors \(O(\alpha)\) per step would multiply to \(e^{Cj\alpha}\) | one gauge per cell, telescoping (Lemma 5) |
| C3 | Positivity is no longer given by Fourier analysis | the field block could lose its gap | flat local models plus small form perturbation (Lemma 6, Proposition 8); bare cells at any unitary \(U\) (Lemma 7) |
| C4 | Pointwise bounds need a covariant local estimate | drift and Weitzenböck terms of size \(\alpha/r\), \(\alpha/r^2\) | Kato's inequality at real \(U\), two absorptions (Lemma 10) |
| C5 | The two curls differ by the holonomy | on bare cells the holonomy is not small (Codex's D3) | both curls carried from the start; bare cells exact (Lemma 7) |
| C6 | \(R\) depends on \(U\) and is nonlocal | a nonlocal coefficient defeats localization | \(R\) is never a coefficient: the scalar block is unfolded (Lemma 2) |
| C7 | The reference must lie in Reg\(_\alpha\), with the derivative member | curvature alone does not bound \(|\nabla A|\) uniformly (Test T3) | the current bound of the critical background (Proposition REG) |

C7 is the one place where criticality enters. C2 is the one place where depth could have entered.

### 4.2 Tests for a counterexample, run first

The target failure is a real regular \(U\) at which (1.1) needs a constant growing with the depth \(k\), the mesh or the volume.

**T1 (global holonomy).** A flat connection with nontrivial holonomy around a torus cycle or a hole of \(\Omega_0\) has every plaquette equal to \(\mathbf 1\) and is not gauge equivalent to \(\mathbf 1\). It lies in Reg\(_0\): every cube in \(\Omega_0\) is simply connected and carries a gauge with \(A=0\). A proof that compares with one global flat inverse fails here (Attack A). The proof below uses only cell gauges, and cells near \(\Omega_0^c\) are bare, where no gauge is needed (Lemma 7). Holonomy does not enter. No counterexample.

**T2 (depth accumulation in the rows).** If each of the \(j\) one-step averages of a row of height \(j\) were compared with the flat step in a gauge chosen afresh at its level, the errors would multiply to \(e^{Cj\alpha}\), a genuine depth factor. In one gauge on the whole read set of the row, the level-\(m\) averaged field is within \(C_L\alpha L^{m-j}\) of flat, and the site-factor transports telescope (Lemma 5). The product is \(\exp(C_L\alpha/(L-1))\). No counterexample. (The earlier text added an inference from per-level errors to a necessary plaquette size; Codex's check, `gates/p82-curved-gate.md` line 30, deletes it, since a locally pure gauge changes coefficients without changing plaquettes. It is not used.)

**T3 (a curvature-only class).** If only plaquettes were bounded, the axial gauge on a cube of side \(M_P\xi\) gives \(\xi|A|\le CM_P\alpha\), but only \(|\nabla A|\le CM_P\alpha/(\eta\xi)\): a transverse difference of an axial potential is a ladder of \(|x|/\eta\) plaquettes, a factor \(\xi/\eta=L^j\). In any gauge, a field with \(|\partial U-1|\le\varepsilon\eta^2\xi^{-2}\) can have transverse differences of size \(\varepsilon\xi^{-2}\log(\xi/\eta)\) (the \(L^\infty\) failure of the Calderón–Zygmund bound; `a3-close.md` line 22). The derivative member enters twice below: in Lemma 6(iii) and in Lemma 10. So the method needs the derivative member of Reg\(_\alpha\). This is not a counterexample to P82°. At the critical reference the current bound supplies the derivative member (Proposition REG).

**T4 (bare cells and the plaquette curl; Codex's D3, `gates/p82-curved-gate.md` lines 202–216).** Take \(\Omega_1=\emptyset\) and \(\Omega_0\) one small cube. There is no cube to test in Reg, so Reg\(_0\) holds for arbitrary real links on \(\Omega_0\). One noncentral link \(H\) on a \(\nu\)-edge and \(a=v\) on the \(\mu\)- and \(\nu\)-edges from one site, with \(\operatorname{Ad}(H^{-1})v\ne v\), give \(da=0\) and \(\mathfrak da\ne0\) on their common plaquette. So \(\mathfrak d^{\mathsf T}\mathfrak d-d^{\mathsf T}d\) is not \(O(\alpha)\) on the class. This refutes a global comparison of the two curls, not P82° for \(\mathfrak d\): on bare cells \(K\) fixes the field. The proof below carries \(\mathfrak d\) from the start (Lemma 7, Proposition 8).

**T5 (Nielsen–Olesen; Codex's D1).** The earlier text claimed a negative bottom for \(d^{\mathsf T}d+DD^{\mathsf T}\) in a constant abelian field. That is false: \(\langle a,(\flat^{\mathsf T}\flat+DD^{\mathsf T})a\rangle=\|\flat a\|^2+\|D^{\mathsf T}a\|^2\ge0\) for every real \(U\). The Nielsen–Olesen negative direction belongs to the full Wilson Hessian \(F''(0)=\mathfrak d^{\mathsf T}\mathfrak d+\Delta'\), whose curvature term \(\Delta'\) is not in \(S^\circ\). `a3-derivative.md` Lemma 8.1 moves \((\Delta'-W_0)a\) into the nonlinear remainder and pays for it with \(C^\circ C_2\kappa_{\rm A3}\le1/8\) (line 476). So the Nielsen–Olesen direction is paid by the smallness of \(\kappa_{\rm A3}\) against the P82° constant \(C^\circ\). This is why \(C^\circ\) must be fixed before \(\kappa_{\rm A3}\), which it is (Section 13). No counterexample.

**T6 (sharp sources; Codex's D2, `gates/p82-curved-gate.md` lines 101–107).** A pillar indicator is unbounded on the dual energy space: at \(U=\mathbf 1\) on a fixed physical torus with fixed pillars and \(\eta\to0\), a constant 1-form \(v\) has bounded energy, while \(\mathbf 1_Pv\) has squared gradient norm at least \(c/\eta\). So a decay lemma stated as an operator norm \(\|\mathbf 1_y\mathbb M^{-1}\mathbf 1_z\|_{\mathcal X^*\to\mathcal X}\) cannot hold uniformly. The decay lemma below (Lemma 9) is stated for sources already supported over \(z\). That is all the later steps use.

**No numerics.** A run cannot test uniformity in depth: one more layer multiplies the number of sites by \(L^4\). No step rests on a computed value.

### 4.3 Three attacks, and why the first two do not work

**Attack A: a global Neumann series from the flat weighted inverse.** Write \(S^\circ(U)=S^\circ(\mathbf 1)+V\) in some global gauge and expand \((1+S^\circ(\mathbf 1)^{-1}V)^{-1}\) in the weighted norms. *Why it fails.* It needs \(\|S^\circ(\mathbf 1)^{-1}V\|_{X_w\oplus Y_w}<1\) with \(V\) controlled by the potential of \(U\) in that gauge. (i) Under T1 there is no global gauge with \(U\) near \(\mathbf 1\): some link is at distance \(O(1)\) from \(\mathbf 1\), so \(V\) has an entry of size \(\eta^{-1}\) at a bond of layer 0, and \(\|V\|_{X\to F}\) is of order one. (ii) Take a constant abelian field of size \(B=\alpha\xi^{-2}\) in one layer of scale \(\xi\). The boundary loop of a square of side \(\ell\) in its plane has holonomy angle \(B\ell^2\). For \(B\ell^2\le\pi\), unitarity gives \(c\,B\ell^2\le|{\rm hol}-1|\le\sum_{b\in\partial}|U(b)-1|\le(4\ell/\eta)\,\eta\sup|A|\) in every gauge, so \(\xi\sup|A|\ge c\alpha\ell/\xi\). So the bound \(\xi|A|\le C\alpha\) holds only on cubes of side \(O(\xi)\); on a cube of side \(\xi(\pi/\alpha)^{1/2}\) every gauge has \(\xi\sup|A|\ge c\sqrt\alpha\). A global comparison loses the factor \(\ell/\xi\). The perturbation is \(O(\alpha)\) only on cubes of side \(O(M_P\xi)\). That is the localization below.

**Attack B: port the CA-I 4.14 operator theorem.** CA-I Theorem 4.14 (L46035–46066) concerns the fluctuation form \(\mathsf Q\) at free current on prepared nests of Balaban's CMP 122a, with clause (A): "on \(\mathcal U(\varepsilon_1)\) the inverse \(\mathsf C=\mathsf A^{-1}\) exists … \(\mathsf A\mathsf C=1\) on all of \(\mathcal U(\varepsilon_1)\)". Its positivity step reads "\(\mathsf Q(U,0)\ge\gamma_0/2\) for every \(U\in\mathcal U_{\mathbb R}\)" and "\(\operatorname{Re}\mathsf Q\ge m_1\) on \(\mathcal U(\varepsilon_1)\)" (L47703–47704), and its proof begins "Put \(\ell:=M/12d\). We use the unit box system: the cubes \(\mathsf b\) of side \(\ell\)" (L47728–47729). Its hypotheses include "The floors on \(M_1\), on \(M_1^\sharp\), on \(M\) and on \(L\)" (L46046–46047). *Why it does not fit.* (i) It is a different operator: the fluctuation form on a prepared box, not the multilayer saddle \(S^\circ\) with the outline's \(R\) and \(K_0\). (ii) Its box scale is \(\ell=M/12d\), the construction size. A port would put \(M\) into the P82° constants, which IN1 forbids (`in1-draft.md` E.3, remark 2: "If the layered case could only be proved with constants depending on \(M\) or \(\bar\kappa\), the cycle would reappear"). (iii) The index marks its positivity step "sketched" (`sa-index/ca-4.12-4.19/chunk-04.md` row 47703). *What ports.* The pattern "real positivity at real references, then a sector bound \(\operatorname{Re}\ge\gamma/2\) on a complex ball, then \(AC=1\) by the identity theorem" is the right template for the complex extension of P82° (Section 14.3). It is not needed for P82°.

**Attack C: a localized parametrix from flat local models (Balaban's architecture; SA mechanism (f)).** SA L10533–10546 states the mechanism: "the operators \(R\), \(\Delta'_\pi\), \(\mathsf S^{\mathsf T}\Delta^{(2)}\mathsf S\) and the constraint are combined into a single system \(\mathbb K\) of finite range … On such a cube, in the gauge of the class, \(\mathbb K_\varkappa\) equals the flat system plus \(O(\alpha_0+\alpha_1+\gamma_0)\), and this perturbation need only be small compared with flat constants." The three-dimensional account carries it out: Y3 Theorem I-65-83 (Y3 L21262–21286), "Local gauges reduce the constrained system to the small-field inverse … Near the boundary of the ambient region, the local system instead has only the bare scale; its two massive operators can be inverted directly. A partition of unity combines these local inverses" (Y3 L21187–21194), with "constants depending only on \(L\)" (L21265) and a gauge class on "cubes … of side at most \(12\mathfrak M\xi_n\)" in \(\mathcal L_n\cup\mathcal L_{n+1}\) with "\(\xi_n|A|\le\alpha_0\), \(\xi_n^2|\nabla^\xi A|\le\alpha_0\)" (L21212–21226). *This attack works.* Sections 6–10 carry it out in four dimensions. Where four dimensions change the Y3 proof:

1. Y3 uses local inverses with pointwise exponential decay in supremum seminorms (Y3 L21851–21856, from its small-field inverse I-65-40). No four-dimensional pointwise local inverse is imported. We use the energy-norm local inverse of FP1 (`flat-port.md` (8.5), §9.2) and a separate pointwise upgrade (Lemma 10). Its value step uses Kato's inequality, which needs a real reference.
2. Y3 makes the parametrix remainder small by local decay across the cutoff, \(q_{\mathfrak M}=C_q\mathfrak M^{-1}e^{-\delta D_0}\) (Y3 L22500–22506). Here the remainder is small by the commutator factor \(C_L/M_P\) alone (`flat-port.md` (8.8)). Both work.
3. Top counts. In four dimensions a metric ball of radius \(t\) holds at most \(C_L(1+t)^5\exp(8t\log L/\rho)\) tops (`a3-balaban.md` (5.3), `gates/p82-curved-gate.md` line 180), so the sum over tops needs \(\rho\ge32\log L/\delta_w\).
4. The Weitzenböck commutator has \(\binom42=6\) plaquettes per bond and four components (Lemma 10, Proposition 11).
5. The curl. The Wilson Hessian's main part is the plaquette curl (PX114), which differs from the forward curl by the holonomy (T4).

---

## 5. Imports

Each import is a statement of another library file. Its check record is quoted. Nothing below counts as more than its label.

**(I1) Flat local inverse for the enlarged local system.** `flat-port.md` (8.5) (lines 534–535) for the system (8.1) (lines 478–488) on the one- and two-scale periodic models of §8.2 and on bare boundary models (line 539), enlarged by the counting-row multiplier of §9.2 (line 666: "The local inverse bound follows from (8.5), the local gap just proved, and the formula solving that Schur complement"):
\[
 \|\mathbb M_i^{\rm fl\,-1}F\|_{\mathcal X_i}\le B_L\|F\|_{\mathcal X_i^*},
\]
uniformly in the fine mesh, the box size and the copied interface shape. Written by Codex; checked by Claude in `gates/flat-port-gate.md` (sections 8.1, 9.2: ADVANCE). FP1 status [C] (`ym4-assembly.md` line 177).

**(I2) Cutoffs and the flat commutator.** `flat-port.md` (8.6) (lines 543–548): cutoffs \(\chi_i\) with \(\sum_i\chi_i^2=1\), \(|D\chi_i|\le C_L/(M_Ps_i)\), \(|D^2\chi_i|\le C_L/(M_P^2s_i^2)\), bounded overlap \(N_L\) independent of \(M_P\) (line 550); and (8.8) (lines 569–571): \(\|[\mathbb M^{\rm fl},\chi_i]X\|_{\mathcal X^*}\le(C_L/M_P)\|X\|_{\mathcal X_i,{\rm read}}\), including the row-multiplier commutator (line 666). The assembly bounds (8.9) (lines 573–580). Same check record as (I1).

**(I3) Free local estimate and free Green function.** `flat-port.md` (4.1)–(4.2) (lines 148–165): for \(\Delta u=D^*g+F\) on an enlargement of a cube of side \(r\ge16\eta\), on a smaller cube, \(|Du|+r^\beta[Du]_\beta\le C_{\epsilon,\beta}\{r^{-3}\|u\|_{2,\rm outer}+|g|+r^\epsilon[g]_\epsilon+r|F|\}\), \(0<\beta<\epsilon<1\); and \(|D^qG(x)|\le C_q(1+|x|_\infty)^{-2-q}\), \(q\le3\). Checked by Claude in `gates/flat-port-gate.md` (4.1: ADVANCE, with gloss W3, closed there).

**(I4) Summation on the outline's metric.** `a3-balaban.md` (5.3)–(5.5) (lines 121–135): if \(\rho\ge\max\{1,2(8+p_0)\log L/\tau\}\), then \(\sup_y\sum_z(s_z/s_y)^pe^{-\tau d(y,z)}\le C(L,p_0,\tau)\) for \(|p|\le p_0\). Written by Codex; checked by Claude in `gates/a3-balaban-reads-gate.md` (R2: ADVANCE) and re-derived by Codex in `gates/p82-curved-gate.md` §7 (lines 177–184). Only \(p=0\) is used.

**(I5) One-step averaging facts.** `a3-balaban.md` §§8.4–8.6: the one-step contour-mean map is holomorphic on a fixed ball, its derivative at \(W=\mathbf 1\) is the unit straight-path matrix \(Q_0\) with row sum \(L\) and column sum \(L^{-3}\) ((8.3), line 594), the exact composition of straightened rows (§8.5), bounded read width, and the outward reduced row (8.10). Written by Codex; checked by Claude in `gates/a3-balaban-reads-gate.md` (R4–R6: ADVANCE; "P82 uses only the identity-reference case", line 110).

**(I6) The A1 background.** `a1-balaban.md` (8.2) (lines 2426–2433): conditional on F0, the default constraint problem has one regular critical residual orbit, with \(|\partial U(p)-1|\le B\varepsilon_1\eta^2\mathsf L(p)^{-2}\) and \(|J(U)(b)|\le B\varepsilon_1\mathsf L(b)^{-3}\). Written by Codex; checked by Claude in `gates/a1-balaban-gate.md` ("Every gated section is ADVANCE … conditional on the flat input F0"). F0 is FP1.

**(I7) Balaban's local gauge, ported.** `a1-balaban.md` §3.8 last paragraph (lines 708–723): Balaban's CMP 99 (75–102) Proposition 6, applied with reference \(\mathbf 1\) to an auxiliary nested family around one cube, with flat inverse inputs only; it gives a gauge with value, derivative and Laplacian bounds \(CM\alpha_0\) when \(M\alpha_0\) is small, "exactly as in (1.128)–(1.138)". Same check record as (I6) (gate §2, 3.8: ADVANCE conditional on F0). The auxiliary gap is \(W_\natural\) (Section 2.3, item 3).

**(I8) The real covariant value estimate.** `a3-balaban.md` (7.19) and its proof (lines 436–445 and following): Kato's inequality \(\Delta|u|\le|\Delta_Uu|\) at real \(U\), and the Green–Poisson comparison \(\sup_{Q'/2}|u|\le C(r'^{-2}\|u\|_{2,Q'}+r'^2\sup_{Q'}|\Delta_Uu|)\) on cubes \(Q'\) of side \(r'\ge16\eta\); and the Poisson gradient bound from the free Green function. Written by Codex; checked by Claude in `gates/a3-balaban-reads-gate.md` (R3: ADVANCE), and its inputs re-checked by Codex in `gates/p82-curved-gate.md` line 122 ("reflection bounds the Poisson kernel by \(Cr^{-3}\), the positive quadratic barrier bounds the Green sum by \(Cr^2\), and one of the disjoint boundary shells has squared \(L^2\) norm at most \(Cr^{-1}\|u\|_2^2\)").

**Dependency check: no cycle.** (I6)–(I7) rest on F0 = FP1 and on `a1-balaban.md` §3.9 (Balaban's flat-to-curved step, gated "ADVANCE, conditional on F0", `gates/a1-balaban-gate.md` line 47). None of them reads Theorem P. Theorem P reads only (I1)–(I5), (I8). So Theorem P, then Proposition REG, then Theorem P82 is a linear chain. The assembly records the PR1–BG1 pair as "one argument at a real critical reference … not a cycle in the order of constants" (`ym4-assembly.md` line 469); the chain above shows it is not a logical cycle either.

---

## 6. Algebra of the unfolded system

**Definition (the unfolded system).** Unknowns \(X=(A,h,\lambda,\mu,\nu)\): a 1-form on the bonds of \(\Omega_0\), two site functions, a function on tops, a function on rows. Put \(B_\flat=\flat^{\mathsf T}\flat+DD^{\mathsf T}+K^{\mathsf T}K\) and
\[
 \mathbb M_\flat(U)=\begin{pmatrix}
 B_\flat&-D&0&0&-K^{\mathsf T}\\
 -D^{\mathsf T}&1&A_s&0&0\\
 0&A_s&0&-Q'^{\mathsf T}&0\\
 0&0&-Q'&0&0\\
 -K&0&0&0&0
 \end{pmatrix},
 \tag{6.1}
\]
all operators at \(U\), Dirichlet outside \(\Omega_0\). It is symmetric in the pairings of Section 2.1. This is `flat-port.md` (8.1) with the row multiplier of its §9.2, formed at \(U\), and with either curl. Its norm, with covariant differences at \(U\):
\[
 \|X\|_{\mathcal X}^2=\|\nabla_UA\|_2^2+\|m^{-1}A\|_2^2+\|h\|_2^2
 +\|m^{-2}\lambda\|_2^2+\|m^{-1}D\lambda\|_2^2+\textstyle\sum_{\alpha,\beta}\|D_\alpha D_\beta\lambda\|_2^2
 +\|m^2\mu\|_{\rm top}^2+\|\nu\|_{\rm count}^2 .
 \tag{6.2}
\]
Write \(\|A\|_E^2=\|\nabla_UA\|^2+\|m^{-1}A\|^2\) and \(\|\lambda\|_{H^2_m}^2\) for the \(\lambda\) part. \(\mathcal X^*\) is the dual space of sources \(F=(f,g_1,g_2,g_3,g_5)\): \(f\in E^*\), \(g_1\in L^2\), \(g_2\in(H^2_m)^*\), \(g_3\) in the top dual norm, \(g_5\) in the counting dual norm. All five unknown norms have the same scaling when \(h\sim DA\), \(\lambda\sim mA\), \(\mu\sim m^{-3}A\) (`flat-port.md` line 515).

**Lemma 1 (the scalar block).** Let \(U\) be real and regular (the contour means exist). (i) \(A_s>0\) and \(Q'\) is onto. (ii) \(N\) exists, \(R\) is the orthogonal projection onto \(\ker(Q'S)=\Delta_U\ker Q'\), and \(R\) does not depend on the positive top mass. (iii) The scalar system \(\mathbb S\) (rows and columns 2–4 of (6.1)) is invertible: for sources \((g_1,g_2,g_3)\),
\[
 \mu=N(Q'Sg_1-Q'S^2g_2+g_3),\qquad h=S(g_2+Q'^{\mathsf T}\mu),\qquad \lambda=S(g_1-h),
 \tag{6.3}
\]
and its \(h\leftarrow g_1\) block is \(P=1-R\).

*Proof.* (i) \(\langle\lambda,A_s\lambda\rangle=\|D\lambda\|_2^2+\|m^{-1}Q'\lambda\|_{\rm top}^2\ge0\). Suppose it vanishes. Then \(D\lambda=0\) on every bond, so \(\lambda\) is parallel: \(\operatorname{Ad}(V_\gamma)\lambda(x)=\lambda(y)\) for every lattice path \(\gamma\) from \(x\) to \(y\) inside the pillar, \(V_\gamma\) its transport. If \(\lambda(x)=0\) for one \(x\) of a pillar, \(\lambda=0\) on the pillar, since the pillar is connected and each \(\operatorname{Ad}V\) is injective. Otherwise \(\lambda(x)\ne0\) and its stabilizer \(\mathcal S=\{V:\operatorname{Ad}(V)\lambda(x)=\lambda(x)\}\) is a one-parameter abelian subgroup of SU(2). Fix one path \(\gamma_1\) and write \(V_\gamma=V_{\gamma_1}s_\gamma\) with \(s_\gamma\in\mathcal S\); regularity puts the \(V_\gamma\) near each other, so the \(s_\gamma\) are near \(\mathbf 1\). Put \(\bar s=\exp(N_\gamma^{-1}\sum_\gamma\log s_\gamma)\in\mathcal S\). Since \(\mathcal S\) is abelian, \(\log(V_\gamma(V_{\gamma_1}\bar s)^{-1})=\operatorname{Ad}(V_{\gamma_1})(\log s_\gamma-\log\bar s)\), and these sum to zero. The contour mean is the unique solution near the \(V_\gamma\) of \(\sum_\gamma\log(V_\gamma V^{-1})=0\) (SA 7065), so it equals \(V_{\gamma_1}\bar s\), and it carries \(\lambda(x)\) to \(\lambda(y)\). By induction over the levels of the iterated mean, every averaged transport \(W(y,x)\) in \(Q'\) carries \(\lambda(x)\) to \(\lambda(y)\). The weights of \(Q'\) sum to one, so \((Q'\lambda)(y)=\lambda(y)\) at each top. Now \(Q'\lambda=0\) gives \(\lambda(y)=0\), contradicting \(\lambda(x)\ne0\) on that pillar. So \(\lambda=0\), and \(A_s>0\).

\(Q'\) onto: pillars are disjoint, and the top's own coefficient is \(Q'(y,y)=w_y\operatorname{Ad}(W(y,y))=w_y\mathbf 1\) with \(w_y>0\), because \(W(y,y)=\mathbf 1\) at every level. Given a top vector \(t\), the site function equal to \(t(y)/w_y\) at each top and zero elsewhere has \(Q'\lambda=t\).

(ii) \(Q'^{\mathsf T}\) is injective, and \(S\) is invertible and symmetric, so \(\langle b,Q'S^2Q'^{\mathsf T}b\rangle=\|SQ'^{\mathsf T}b\|^2>0\) for \(b\ne0\), and \(N\) exists. With \(T_s=Q'S\), \(SQ'^{\mathsf T}NQ'S=T_s^{\mathsf T}(T_sT_s^{\mathsf T})^{-1}T_s\) is symmetric, idempotent, and fixes \(\operatorname{ran}T_s^{\mathsf T}\); it is the orthogonal projection onto \((\ker T_s)^\perp\). So \(R\) projects onto \(\ker(Q'S)\). If \(Q'\chi=0\), then \(A_s\chi=\Delta_U\chi\), so \(Q'S\Delta_U\chi=Q'\chi=0\). Conversely, if \(Q'Sf=0\), put \(\chi=Sf\); then \(Q'\chi=0\) and \(\Delta_U\chi=A_s\chi-Q'^{\mathsf T}m^{-2}Q'\chi=f\). So \(\ker(Q'S)=\Delta_U\ker Q'\). This set and the fine pairing do not involve the top mass. (Checked by Claude, `gates/a3-balaban-reads-gate.md` R1.)

(iii) Rows 2–4 of (6.1) read \(h+A_s\lambda=g_1\), \(A_sh-Q'^{\mathsf T}\mu=g_2\), \(-Q'\lambda=g_3\). The second gives \(h=S(g_2+Q'^{\mathsf T}\mu)\), the first \(\lambda=S(g_1-h)\). The third becomes \(Q'Sh=Q'Sg_1+g_3\), that is \(Q'S^2Q'^{\mathsf T}\mu=Q'Sg_1+g_3-Q'S^2g_2\), which gives \(\mu\). At \(g_2=g_3=0\), \(h=SQ'^{\mathsf T}NQ'Sg_1=Pg_1\). \(\square\)

**Lemma 2 (Schur complement).** Let \(U\) be real and regular. (i) \(\mathbb M_\flat(U)\) is invertible if and only if
\[
 \Sigma_\flat=\begin{pmatrix}\flat^{\mathsf T}\flat+DRD^{\mathsf T}+K^{\mathsf T}K&-K^{\mathsf T}\\-K&0\end{pmatrix}
\]
is, and then the \((A,\nu)\) outputs of \(\mathbb M_\flat(U)^{-1}\) on sources \((f,0,0,0,g_5)\) are \(\Sigma_\flat^{-1}(f,g_5)\). (ii) \(S^\circ_\flat\) is invertible if and only if \(\Sigma_\flat\) is, and \(S^{\circ-1}_\flat(f,b)=\Sigma_\flat^{-1}(f+K^{\mathsf T}b,\,-b)\).

*Proof.* (i) The scalar block \(\mathbb S\) is invertible (Lemma 1). The coupling between \((A,\nu)\) and \((h,\lambda,\mu)\) is \(-D\) from \(h\) into row 1 and \(-D^{\mathsf T}\) from \(A\) into row 2. The Schur complement with respect to \(\mathbb S\) replaces \(B_\flat\) by \(B_\flat-D\,(\mathbb S^{-1})_{h\leftarrow g_1}D^{\mathsf T}=B_\flat-DPD^{\mathsf T}\), and \(B_\flat-DPD^{\mathsf T}=\flat^{\mathsf T}\flat+DRD^{\mathsf T}+K^{\mathsf T}K\). A block matrix with an invertible diagonal block is invertible if and only if its Schur complement is. With sources only in the \(A,\nu\) slots, rows 2–4 give \(h=PD^{\mathsf T}A\), row 1 becomes the first row of \(\Sigma_\flat\), and row 5 is \(-KA=g_5\). This is `flat-port.md` (8.2); it uses no flatness. (ii) If \(S^\circ_\flat(a,\lambda)=(f,b)\), then \(Ka=b\), and adding \(K^{\mathsf T}\) times it to the first equation gives \(\Sigma_\flat(a,\lambda)=(f+K^{\mathsf T}b,-b)\). The converse is the same computation backwards. (Checked by Codex, `gates/p82-curved-gate.md` §3, lines 36–44: "Both signs and the added row mass are needed.") \(\square\)

**Lemma 3 (gauge covariance).** For a real gauge transformation \(g\), let \(\mathcal G\) act by \(\operatorname{Ad}g\) at base points: at \(b_-\) on bonds, at sites, at tops, and at \(c_-\) on rows. Then \(\mathbb M_\flat(U^g)=\mathcal G\,\mathbb M_\flat(U)\,\mathcal G^{-1}\), and \(\mathcal G\) is an isometry from \(\mathcal X(U)\) to \(\mathcal X(U^g)\), from \(\mathcal X(U)^*\) to \(\mathcal X(U^g)^*\), and between the consumer norms of Section 2.2 at \(U\) and at \(U^g\).

*Proof.* With start-point transport, \((e^{i\eta A}U)^g=e^{i\eta\operatorname{Ad}(g)A}U^g\). The operators \(D,D^{\mathsf T},\nabla_U,d\) intertwine \(\operatorname{Ad}g\) by direct substitution. For \(\mathfrak d\): the transports \(T_{r-1}\) become \(g(x_0)T_{r-1}g(x_{r-1})^{-1}\), and the insertion \(\operatorname{Ad}(g(x_{r-1}))A(b_r)\) at the start of \(b_r\) is conjugated back, so \(\mathfrak d_{U^g}\operatorname{Ad}g=\operatorname{Ad}g(x_0)\,\mathfrak d_U\). The contour variables transform as \(W(y,x)\mapsto g(y)W(y,x)g(x)^{-1}\), since the Federbush mean is left and right equivariant (SA 7065–7080). So \(Q'\) intertwines \(\operatorname{Ad}g\) at sites and tops. For the rows use the exact composition (I5): \(\mathcal M^m(e^{i\eta A}U)=v_me^{ia_m}W_mv_m^{-1}\), \(a_{m+1}=S_{W_m}(a_m)\), \(v_{m+1}=v_m\mathsf v_m(a_m)\). The block means of the ratios \(W(y,x)W_0(y,x)^{-1}\) transform by conjugation with \(g(y)\). By induction on \(m\), \((\operatorname{Ad}(g)a_m,gv_mg^{-1})\) solves the recursion at \((U^g,\operatorname{Ad}(g)A)\), and by uniqueness of each finite step it is the solution. So \(\mathcal Q^{\rm st}(U^g;\operatorname{Ad}(g)A)(c)=\operatorname{Ad}(g(c_-))\mathcal Q^{\rm st}(U;A)(c)\). Differentiating at \(A=0\) gives \(K_{U^g}\operatorname{Ad}g=\operatorname{Ad}(g|_{c_-})K_U\). The masses are scalar. Every norm is built from \(|\cdot|\), which is \(\operatorname{Ad}\)-invariant, and from covariant differences. (Checked by Codex, `gates/p82-curved-gate.md` line 48, including "its own-level outward endpoint factors".) \(\square\)

**Lemma 4 (locality).** There is \(a_L\), depending on \(L\) only, such that a row of \(\mathbb M_\flat(U)\) located over a top \(y\) reads only components within one fine stencil, the pillar of \(y\), and the double blocks of the rows meeting that pillar, with the outer blocks at outward rows, all within Euclidean distance \(a_Lm_y\) of \(P_y\) and \(d_{\mathbf B}\)-distance \(C_L\). Call this the read set of the row.

*Proof.* \(\flat,D,D^{\mathsf T},\nabla_U\) are nearest-neighbour stencils. \(Q'\) at \(y\) reads \(P_y\) and the contour transports inside it, which lie in the block \(B^j(y)\). A row \(c\) of height \(j\) reads the double block of \(c\) and, through the straightening, the bounded read neighbourhood of width \(a_Ls_j\) (I5, §8.5). At an outward row the outer block is one level finer, by separation. Distances of order \(m_y\) inside a layer, or crossing one seam, have \(d_{\mathbf B}\)-length at most \(C_L\). \(\square\)

Status of Section 6: proved, from (I5) for the composition of rows.

---

## 7. Near-flat coefficients in one cell gauge

**Lemma 5 (rows and pillar means in a common gauge).** Let \(Z\) be a cube carrying a real gauge in which \(U=e^{i\eta A_0}\), \(\sup_Zm|A_0|\le\delta\le\delta_0(L)\). For every row \(c\) of height \(j\) whose read set lies in \(Z\), and every top \(y\) whose pillar lies in \(Z\),
\[
 \begin{gathered}
 \textstyle\sum_b|K_U(c,b)|\le C_Ls_j,\qquad \sum_{c\text{ of height }j}|K_U(c,b)|\le C_L\eta^4s_j^{-3},\\
 \textstyle\sum_b|K_U(c,b)-K_1(c,b)|\le C_L\delta s_j,\qquad \sum_{c\text{ of height }j}|K_U(c,b)-K_1(c,b)|\le C_L\delta\,\eta^4s_j^{-3},\\
 \textstyle\sum_x|Q'_U(y,x)-Q'_1(y,x)|\le C_L\delta,\qquad \max_x|Q'_U(y,x)-Q'_1(y,x)|\le C_L\delta\,\eta^4m_y^{-4}.
 \end{gathered}
 \tag{7.1}
\]
Here \(K_1\) is the flat straightened row, the straight-segment average \(n^{-4}\sum_{v\in P_-}\sum_{t<n}\eta A_\mu(v+t\eta e_\mu)\), \(n=s_j/\eta\) (`flat-port.md` (2.1), \(K=sQ\)), and \(Q'_1\) is the plain pillar mean. Entries are operators on the colour space, measured in norm. Moreover, at any unitary \(U\) with the contour means defined, \(\sum_x|Q'_U(y,x)|=1\) exactly.

*Proof.* *Step 1 (value recursion at reference \(\mathbf 1\)).* Straighten \(U\) itself at the reference \(\mathbf 1\): \(\mathcal M^m(U)=t_me^{ib_m}t_m^{-1}\), \(b_0=\eta A_0\), \(t_0=\mathbf 1\), \(t_{m+1}=t_mz_m\), where \(z_m\) is the block factor at level \(m\). On the read set, \(u_m:=\sup|b_m|\) obeys \(u_{m+1}\le L(1+C_Lu_m)u_m\) (one step of (I5) at reference \(\mathbf 1\): the linear part has row sum \(L\), and the remainder is quadratic on a fixed ball), with \(u_0=\eta\sup|A_0|\le\delta\eta/m=\delta L^{-j}\) for an interior row of height \(j\), since the local scale is \(m=\xi_j=s_j\) on its read set (outward rows: Step 4). Bootstrap: suppose \(u_m\le2\delta L^{m-j}\) for \(m<m_1\). Then \(u_{m_1}\le\delta L^{m_1-j}\prod_{m<m_1}(1+2C_L\delta L^{m-j})\le\delta L^{m_1-j}\exp(2C_L\delta\sum_{m<j}L^{m-j})\le\delta L^{m_1-j}\exp(2C_L\delta/(L-1))\le2\delta L^{m_1-j}\) once \(\delta\le\delta_0(L)\). By induction \(u_m\le2\delta L^{m-j}\) for \(m\le j\). The block factor is the exponential of the mean logarithm of quantities of size \(O(u_m)\) (SA 7092), so \(|z_m-\mathbf 1|\le C_Lu_m\le C_L\delta L^{m-j}\), and \(|t_m-\mathbf 1|\le\exp(\sum_{m'<m}C_L\delta L^{m'-j})-1\le C_L\delta\). (This is the check written by Codex, `gates/p82-curved-gate.md` line 54: "bootstrap this bound in \(u_{m+1}\le L(1+C_Lu_m)u_m\): the correction product is bounded by \(\exp(C_L\sum u_m)\)".)

*Step 2 (one-step Jacobians).* The one-step straightened Jacobian \(S'_{e^{ib}}\) at \(W=e^{ib}\) is holomorphic in \(b\) on a fixed ball and equals \(Q_0\) at \(b=0\) (I5: "the endpoint contour derivatives cancel against the block factors"). Cauchy's estimate on the fixed ball gives \(S'_{e^{ib}}=Q_0+E\) with \(\|E\|_{\rm row}\le C_L|b|L\), \(\|E\|_{\rm col}\le C_L|b|L^{-3}\). (The finite step has a fixed finite number of inputs at fixed \(L\), so this costs a power of \(L\) only.)

*Step 3 (composition in one gauge).* By Lemma 3, \(S'_{W_m}=\operatorname{Ad}(t_m)|_{m+1}\,S'_{e^{ib_m}}\,\operatorname{Ad}(t_m)^{-1}|_m\). In the product \(S'_{W_{j-1}}\cdots S'_{W_0}\), the transports at each intermediate level combine to \(\operatorname{Ad}(t_{m+1})^{-1}\operatorname{Ad}(t_m)=\operatorname{Ad}(z_m^{-1})\), a site-diagonal factor within \(C_L\delta L^{m-j}\) of \(1\). So
\[
 K_U/\eta=\operatorname{Ad}(t_j)\prod_{m}(Q_0+E_m)(1+O(C_L\delta L^{m-j})),\qquad \epsilon_m:=\text{relative error of factor }m\le C_L\delta L^{m-j}.
\]
Row and column norms are submultiplicative. \(Q_0\) has row sum \(L\) and column sum \(L^{-3}\). Write \(\prod(Q_0+E'_m)-Q_0^j\) as the sum over \(m\) of the products with exactly one factor replaced by its difference, the factors before it curved and after it flat. Each summand has row norm at most \(L^je^{\sum\epsilon}\epsilon_m\) and column norm at most \(L^{-3j}e^{\sum\epsilon}\epsilon_m\). Since \(\sum_m\epsilon_m\le C_L\delta/(L-1)\), the difference has row norm \(\le C_L\delta L^j\) and column norm \(\le C_L\delta L^{-3j}\). The outer factor \(\operatorname{Ad}(t_j)-1=O(C_L\delta)\) costs the same once. Multiplying by \(\eta\): \(\eta L^j=s_j\), \(\eta L^{-3j}=\eta^4s_j^{-3}\). This is the second line of (7.1). The first line follows from the second and the flat sums: the flat composition has row sum \(s_j\) and fixed-height column sum \(\eta^4s_j^{-3}\), since the base coordinates and path indices run once through their base-\(L\) digits (`gates/p82-curved-gate.md` line 64).

*Step 4 (outward rows).* At an outward row the outer block lies one level finer, by separation. Its gauge bound is \(\sup m|A_0|\le\delta\) at the finer scale, a factor \(L\) in Step 1. Only that adjacent height and the height of the bond read a given fine bond, so the loss is a fixed power of \(L\), with no sum over \(j\).

*Step 5 (pillar means).* Each level's contour mean for \(e^{ib_m}\) is within \(C_L|b_m|\) of \(\mathbf 1\), and consecutive levels meet through \(z_m^{\pm1}\). So each averaged transport \(W(y,x)\) is within \(C_L\delta\) of \(\mathbf 1\) (the same geometric series). Every fine site enters one pillar mean, with weight \(\eta^4m_y^{-4}\). So \(|Q'_U(y,x)-Q'_1(y,x)|\le\eta^4m_y^{-4}|\operatorname{Ad}W(y,x)-1|\le C_L\delta\eta^4m_y^{-4}\), and the sum over the \(m_y^4\eta^{-4}\) sites of the pillar is \(\le C_L\delta\). Finally \(\sum_x|Q'_U(y,x)|=\sum_x\eta^4m_y^{-4}|\operatorname{Ad}W(y,x)|=1\) because \(\operatorname{Ad}\) of a unitary is an isometry of \(\mathfrak{su}(2)\). \(\square\)

Status: proved, from (I5). (Checked in its earlier form by Codex, `gates/p82-curved-gate.md` §4: ADVANCE.)

**Lemma 6 (coefficient comparison).** Let \(Z\) be a cube with a real gauge in which \(U=e^{i\eta A_0}\), \(m|A_0|+m^2|\nabla A_0|\le\delta\le\delta_0(L)\) on \(Z\). Let \(Z^\circ\subset Z\) be the set of components whose read sets lie in \(Z\). Then:

- (i) for \(X\) supported in \(Z\), \((1+C_L\delta)^{-1}\|X\|_{\mathcal X(\mathbf 1)}\le\|X\|_{\mathcal X(U)}\le(1+C_L\delta)\|X\|_{\mathcal X(\mathbf 1)}\);
- (ii) for \(X\) supported in \(Z\) and \(Y\) supported in \(Z^\circ\), for both curls,
\[
 |\langle Y,(\mathbb M_\flat(U)-\mathbb M_\flat(\mathbf 1))X\rangle|\le C_L\delta\,\|Y\|_{\mathcal X}\|X\|_{\mathcal X}.
 \tag{7.2}
\]

*Proof.* Write \(D_U=D_1+\mathcal A\) on sites, \((\mathcal A\lambda)(b)=\eta^{-1}(\operatorname{Ad}e^{i\eta A_0(b)}-1)\lambda(b_+)\). Since \(|\operatorname{Ad}e^{iX}-1|\le2|X|\) for small \(X\), \(\mathcal A\) is a bond-local multiplication by a coefficient bounded by \(2|A_0|\le2\delta/m\). The same holds for \(\nabla_U-\nabla_1\), \(d_U-d_1\) and the adjoints. For \(\mathfrak d\): \(\mathfrak d_U-\mathfrak d_1\) has coefficients \(\eta^{-1}(\operatorname{Ad}T_{r-1}-1)\) with \(|T_{r-1}-\mathbf 1|\le3\eta\sup|A_0|\), so it is a local multiplication bounded by \(C\delta/m\) too. The coefficient \(c(b)=\eta^{-1}(\operatorname{Ad}e^{i\eta A_0(b)}-1)=i\operatorname{ad}A_0(b)+O(\eta|A_0|^2)\) has first differences bounded by \(C|\nabla A_0|(1+\eta|A_0|)\le C\delta/m^2\), by the derivative member and the convergent exponential series.

(i) First differences change by \(O(\delta/m)\) times the field, which \(\|m^{-1}\cdot\|_2\) controls. A second difference changes by \(D_1\mathcal A+\mathcal AD_U\); by the product rule, \(D_1(\mathcal A\lambda)\) is bounded by \(C\delta(m^{-2}|\lambda|+m^{-1}|D\lambda|)\). So each term of (6.2) changes by \(C_L\delta\) times the norm.

(ii) *Vector block.* \(\langle B,(\flat_U^{\mathsf T}\flat_U-\flat_1^{\mathsf T}\flat_1)A\rangle=\langle(\flat_U-\flat_1)B,\flat_UA\rangle+\langle\flat_1B,(\flat_U-\flat_1)A\rangle\le C\delta\|B\|_E\|A\|_E\), since \(\|\flat A\|\le C\|A\|_E\) and \(\|(\flat_U-\flat_1)A\|\le C\delta\|m^{-1}A\|\). The same for \(DD^{\mathsf T}\). For \(K^{\mathsf T}K\) write \(\langle K_UB,(K_U-K_1)A\rangle+\langle(K_U-K_1)B,K_1A\rangle\). By Schur's test with the row and column sums of (7.1), \(\|(K_U-K_1)A\|_{\rm count}^2\le(C_L\delta s)(C_L\delta\eta^4s^{-3})\eta^{-4}\|A\|_2^2=C_L^2\delta^2\|s^{-1}A\|_2^2\), summed over the bounded number of heights meeting a bond (the factor \(\eta^{-4}\) converts the fine pairing; `gates/p82-curved-gate.md` lines 68–75 check this cancellation). The same Schur bound with the first line of (7.1) gives \(\|K_UA\|_{\rm count}\le C_L\|m^{-1}A\|_2\).

*Scalar second-order blocks* \(A_s:H^2_m\to L^2\) and, by duality, \(L^2\to(H^2_m)^*\). \(D_U^{\mathsf T}D_U-D_1^{\mathsf T}D_1=D_U^{\mathsf T}\mathcal A+\mathcal A^{\mathsf T}D_1\). Here \(|\mathcal A^{\mathsf T}D_1\lambda|\le C\delta m^{-1}|D_1\lambda|\), and \(|D_U^{\mathsf T}(\mathcal A\lambda)|\le C\delta(m^{-2}|\lambda|+m^{-1}|\nabla\lambda|)\) by the product rule with \(|\nabla A_0|\le\delta/m^2\). **This is where the derivative member of Reg\(_\alpha\) is used (T3).** So \(\|(D_U^{\mathsf T}D_U-D_1^{\mathsf T}D_1)\lambda\|_2\le C\delta\|\lambda\|_{H^2_m}\).

*Pillar blocks.* \((Q'^{\mathsf T}\nu)(x)\) is the transport of the top value to \(x\), so in the physical pairings \(\|Q'^{\mathsf T}\nu\|_2^2=\sum_ym_y^4|\nu_y|^2\) (each site lies in exactly one pillar; `gates/p82-curved-gate.md` line 66). Schur's test on each pillar with the third line of (7.1) gives \(\|m^{-2}(Q'_U-Q'_1)\lambda\|_{\rm top}\le C_L\delta\|m^{-2}\lambda\|_2\). The transposed block and the mass \(Q'^{\mathsf T}m^{-2}Q'\) follow, so \(\|(A_s(U)-A_s(\mathbf 1))\lambda\|_2\le C_L\delta\|\lambda\|_{H^2_m}\).

*First-order and row blocks.* \(|\langle B,\mathcal Ah\rangle|\le2\delta\|m^{-1}B\|_2\|h\|_2\); \(\|(K_U-K_1)A\|_{\rm count}\le C_L\delta\|m^{-1}A\|_2\) and its transpose. The identity block does not change.

Every block reads only its read set; for \(Y\) supported in \(Z^\circ\) the pairing reads \(X\) only on \(Z\). Summing the blocks gives (7.2). \(\square\)

Status: proved, from Lemma 5. (Checked in its earlier form, forward curl only, by Codex, `gates/p82-curved-gate.md` line 77: "These exhaust (3.1); the identity block has zero error. The derivative premise is doing real work here." The plaquette-curl case is the one-line addition above.)

---

## 8. Cells, local models, parametrix, decay

### 8.1 Tiles, cutoffs and cells

Use the tiles and cutoffs of `flat-port.md` §8.2 (I2) with tile size \(M_P\): cubes of side \(M_Ps_j\) tiling each layer (possible since \(M_P\mid M_1\)), a bare tiling outside \(\Omega_0\), cutoffs \(\chi_i\) with \(\sum_i\chi_i^2=1\) on each component, \(|D\chi_i|\le C_L/(M_Ps_i)\), \(|D^2\chi_i|\le C_L/(M_P^2s_i^2)\), overlap \(N_L\). On a bond component evaluate \(\chi_i\) at \(b_-\), on a top at the top, on a row at \(y_c\).

Let \(Z_i\) be the concentric cube of side \(c_LM_Ps_i\) that contains \(\operatorname{supp}\chi_i\), two read widths \(a_Ls_i\) around it (Lemma 4), and a margin; \(c_L\) depends on \(L\) only. Let \(\tilde\chi_i\) be a second smooth cutoff of the same kind, equal to \(1\) on the read closure of \(\operatorname{supp}\chi_i\) and supported in \(Z_i^\circ\). Choose \(\rho\ge\rho_P\ge C_LM_PL\). Then (the check of `flat-port.md` line 550 and `gates/p82-curved-gate.md` line 89): reaching a layer two levels away crosses a complete collar of width at least \(\rho s_i/L\), while \(Z_i\) has radius at most \(c_LM_Ps_i\); so each \(Z_i\) meets at most two adjacent layers, and if it meets \(\Omega_1\) it lies inside \(\Omega_0\), by the first gap \(\rho\eta\).

- *Bare \(i\):* \(Z_i\cap\Omega_1=\emptyset\). Then every site of \(Z_i\cap\Omega_0\) is a level-0 top whose pillar is itself, and every bond there is a level-0 row. The local model \(\mathbb M_i\) is (6.1) on \(Z_i\cap\Omega_0\) **at the actual \(U\)**, with the actual curl, Dirichlet outside \(\Omega_0\) and at the outer edge of \(Z_i\).
- *Interior \(i\):* \(Z_i\cap\Omega_1\ne\emptyset\). Then \(Z_i\subset\Omega_0\), and \(Z_i\subset\mathcal L_{j'}\cup\mathcal L_{j'+1}\) for some \(j'\in\{j_i-1,j_i\}\), \(j_i\) the level of the tile. Its side \(c_LM_Ps_i\le c_LLM_P\xi_{j'}=c_{\rm reg}M_P\xi_{j'}\) with \(c_{\rm reg}:=c_LL\). (If \(Z_i\) is smaller than the Reg cube, enlarge it inside \(\mathcal L_{j'}\cup\mathcal L_{j'+1}\cap\Omega_0\); the room exists by the same gap count.) So Reg\(_\alpha\) gives a real gauge \(g_i\) on \(Z_i\) with \(U^{g_i}=e^{i\eta A_i}\), \(\xi_{j'}|A_i|+\xi_{j'}^2|\nabla A_i|\le\alpha\). On \(Z_i\) the local scale is \(\xi_{j'}\) or \(L\xi_{j'}\), so \(m|A_i|+m^2|\nabla A_i|\le L^2\alpha=:\delta\). Let \(\mathbb M_i^{\rm fl}\) be the flat local model of (I1) for tile \(i\): the enlarged system on the periodic box \(\Lambda_i\) that copies the geometry of \(Z_i\) (`flat-port.md` line 552). Extend \(g_i\) arbitrarily to the sites of \(\Lambda_i\) and put \(\mathbb M_i=\mathcal G_i^{-1}\mathbb M_i^{\rm fl}\mathcal G_i\). By Lemma 3 this is the local model at the pure gauge \(\mathbf 1^{g_i^{-1}}\). At a pure gauge every holonomy is \(\mathbf 1\), so the two curls coincide there, and \(\mathbb M_i\) is the same for both curls. On the copy of \(Z_i^\circ\),
\[
 \mathcal G_i(\mathbb M_\flat(U)-\mathbb M_i)\mathcal G_i^{-1}=\mathbb M_\flat(e^{i\eta A_i})-\mathbb M_\flat(\mathbf 1),
 \tag{8.1}
\]
because the flat local model has the global flat coefficients on the read closure of \(\operatorname{supp}\chi_i\) (`flat-port.md` (8.7), line 554).

**Lemma 7 (bare models at any unitary \(U\)).** For bare \(i\) and either curl, \(\|\mathbb M_i^{-1}\|_{\mathcal X^*\to\mathcal X}\le B_0\), an absolute constant, for every unitary \(U\).

*Proof.* Here \(m=\eta\). \(Q'\) and \(Q'^{\mathsf T}\) are the identity (in the physical pairings with weight \(\eta^4\)). The level-0 raw row is the bond logarithm, so \(K=\eta\cdot{\rm id}\) in counting coordinates, \(K^{\mathsf T}=\eta^{-3}{\rm id}\), \(K^{\mathsf T}K=\eta^{-2}\). Unitarity of the transports gives \(|\nabla_\mu A_\nu(x)|\le\eta^{-1}(|A_\nu(x+e_\mu)|+|A_\nu(x)|)\), so \(\|\nabla_UA\|_2\le4\eta^{-1}\|A\|_2\), and likewise \(\|D\lambda\|_2\le4\eta^{-1}\|\lambda\|_2\), \(D^{\mathsf T}D\le16\eta^{-2}\) (each site meets eight bonds). Hence \(\|\cdot\|_E\), \(\|\cdot\|_{H^2_m}\), \(\|m^2\cdot\|_{\rm top}\) are within absolute factors of \(\eta^{-1}\|\cdot\|_2\), \(\eta^{-2}\|\cdot\|_2\), \(\eta^2\|\cdot\|_2\). Both curls satisfy \(0\le\flat^{\mathsf T}\flat\le24\eta^{-2}\): \(|\flat A(p)|^2\le\eta^{-2}(\sum_{r}|A(b_r)|)^2\le4\eta^{-2}\sum_r|A(b_r)|^2\), each insertion being a unitary transport of one edge variable, and each bond lies in six plaquettes. Lemma 1(iii) with \(Q'=1\): \(S=(D^{\mathsf T}D+\eta^{-2})^{-1}\in[\eta^2/17,\eta^2]\), \(N=S^{-2}\), \(R=1-S\cdot S^{-2}\cdot S=0\), \(P=1\). So \(\Sigma_\flat=\begin{pmatrix}\flat^{\mathsf T}\flat+\eta^{-2}&-\eta^{-3}\\-\eta&0\end{pmatrix}\), with the explicit inverse \(A=-g_5/\eta\), \(\nu=\eta^3[(\flat^{\mathsf T}\flat+\eta^{-2})A-f]\). In the scaled norms: \(\|A\|_E\le C\eta^{-1}\|A\|_2=C\eta^{-2}\|g_5\|_2=C\|g_5\|_{\rm count}\), and \(\|\nu\|_{\rm count}=\eta^{-2}\|\nu\|_2\le\eta(25\eta^{-2}\|A\|_2+\|f\|_2)\le C(\|A\|_E+\|f\|_{E^*})\), since \(\|f\|_{E^*}\) is comparable to \(\eta\|f\|_2\) here. The scalar unknowns follow from (6.3) with \(S\sim\eta^2\), \(N\sim\eta^{-4}\): each block is bounded by an absolute constant in the scaled norms. Collect: \(\|\mathbb M_i^{-1}\|\le B_0\). No smallness of \(U\), no boundary smoothness and no holonomy assumption is used. \(\square\)

Status: proved. (The forward-curl case is checked by Codex, `gates/p82-curved-gate.md` line 91; the plaquette-curl case is its repair at line 218, "\(0\le\mathfrak d^{\mathsf T}\mathfrak d\le24\eta^{-2}\) exactly as in Lemma 5.0".)

### 8.2 The parametrix

**Proposition 8 (curved parametrix).** For either curl put \(\mathbb B=\sum_i\chi_i\mathbb M_i^{-1}\chi_i\), transplanting \(\chi_iF\) into the model space and the output \(\chi_i\mathbb M_i^{-1}\chi_iF\) (supported in \(\operatorname{supp}\chi_i\)) back. Then \(\mathbb M_\flat(U)\mathbb B=1+\mathbb R\) with
\[
 \mathbb R=\sum_i\Big([\mathbb M_i,\chi_i]+(\mathbb M_\flat(U)-\mathbb M_i)\chi_i\Big)\mathbb M_i^{-1}\chi_i,\qquad
 \|\mathbb R\|_{\mathcal X^*\to\mathcal X^*}\le C_1N_L\max\{B_L,B_0\}\Big(\frac{C_L}{M_P}+C_LL^2\alpha\Big)\le\frac14,
 \tag{8.2}
\]
under the order of constants of Section 13. Hence \(\mathbb M_\flat(U)\) is invertible,
\[
 \mathbb M_\flat(U)^{-1}=\mathbb B\sum_{n\ge0}(-\mathbb R)^n,\qquad
 \|\mathbb M_\flat(U)^{-1}\|_{\mathcal X^*\to\mathcal X}\le\tfrac43\|\mathbb B\|\le B_\sharp:=2C_1N_L\max\{B_L,B_0\}.
 \tag{8.3}
\]
The same holds for the scalar system \(\mathbb S\) with the scalar local models (`flat-port.md` line 588: "the same construction, omitting the first row and column").

*Proof.* *The identity.* Let \(Y_i=\mathbb M_i^{-1}\chi_iF\), a field on the model space. The field \(\chi_iY_i\) is supported in \(\operatorname{supp}\chi_i\), identified with its copy in \(Z_i\). Both \(\mathbb M_\flat(U)(\chi_iY_i)\) and \(\mathbb M_i(\chi_iY_i)\) are supported in the read closure of \(\operatorname{supp}\chi_i\), which lies in \(Z_i^\circ\) (Lemma 4 and the choice of \(Z_i\)). So
\[
 \mathbb M_\flat(U)(\chi_iY_i)=\mathbb M_i(\chi_iY_i)+(\mathbb M_\flat(U)-\mathbb M_i)(\chi_iY_i)
 =\chi_i\mathbb M_iY_i+[\mathbb M_i,\chi_i]Y_i+(\mathbb M_\flat(U)-\mathbb M_i)\chi_iY_i,
\]
and \(\chi_i\mathbb M_iY_i=\chi_i^2F\). Summing over \(i\) and using \(\sum\chi_i^2=1\) gives \(\mathbb M_\flat(U)\mathbb B=1+\mathbb R\) with \(\mathbb R\) as in (8.2). For bare \(i\), \(\mathbb M_i=\mathbb M_\flat(U)\) on \(Z_i^\circ\), so the second term vanishes. The curved commutator \([\mathbb M_\flat(U),\chi_i]\) never occurs.

*Three bounds.*

(1) *Commutators.* For interior \(i\), \(\chi_i\) is scalar, so \([\mathbb M_i,\chi_i]=\mathcal G_i^{-1}[\mathbb M_i^{\rm fl},\chi_i]\mathcal G_i\), and (I2) with Lemma 3 gives \(\|[\mathbb M_i,\chi_i]Y\|_{\mathcal X^*(\mathbf 1^{g_i^{-1}})}\le(C_L/M_P)\|Y\|_{\mathcal X(\mathbf 1^{g_i^{-1}}),\rm read}\). For bare \(i\), the model is at the actual \(U\) with \(m=\eta\), \(Q'=1\), \(K=\eta\); the commutators are the covariant product rule \(D_U(\chi\lambda)(b)=\chi(b_-)D_U\lambda(b)+(D\chi)(b)\operatorname{Ad}(U(b))\lambda(b_+)\) and its analogues for \(\nabla_U\), \(\flat\) and \(D^{\mathsf T}D\), with unitary transports. Each term carries one factor \(D\chi\) or \(D^2\chi\), of size \(C_L/(M_P\eta)\) or \(C_L/(M_P^2\eta^2)\), times a field or one difference. With the scaled norms of Lemma 7 this is \(\le(C_L/M_P)\|Y\|_{\mathcal X,\rm read}\). The row and pillar blocks are diagonal on a bare cell (\(Q'=1\), \(K=\eta\)); their commutators with \(\chi_i\) are the oscillation of \(\chi_i\) over one bond, at most \(C_L/M_P\), times the field.

(2) *Coefficients.* For interior \(i\), pair \((\mathbb M_\flat(U)-\mathbb M_i)(\chi_iY)\) with a global test field \(Y'\). The output is supported in the read closure of \(\operatorname{supp}\chi_i\), where \(\tilde\chi_i=1\), so \(\langle Y',\cdot\rangle=\langle\tilde\chi_iY',\cdot\rangle\), and \(\tilde\chi_iY'\) is supported in \(Z_i^\circ\). Lemma 6(ii), in the gauge \(g_i\) through (8.1) and Lemma 3, gives \(|\langle\tilde\chi_iY',(\mathbb M_\flat(U)-\mathbb M_i)\chi_iY\rangle|\le C_LL^2\alpha\|\tilde\chi_iY'\|_{\mathcal X}\|\chi_iY\|_{\mathcal X}\). Smooth cutoff multiplication is bounded on all five spaces (`flat-port.md` line 573), so \(\|\tilde\chi_iY'\|_{\mathcal X}\le C_L\|Y'\|_{\mathcal X,Z_i}\) and \(\|\chi_iY\|\le C_L\|Y\|_{\mathcal X(\Lambda_i)}\). No sharp indicator is used (T6).

(3) *Local inverses.* \(\|Y_i\|_{\mathcal X(\Lambda_i)}\le B_L\|\chi_iF\|_{\mathcal X^*(\Lambda_i)}\) by (I1) and Lemma 3 for interior \(i\), and \(\le B_0\|\chi_iF\|\) by Lemma 7 for bare \(i\). The norms at \(U\) and at \(\mathbf 1^{g_i^{-1}}\) agree on \(Z_i\) within \(1+C_LL^2\alpha\le2\) (Lemma 6(i)).

*Assembly.* The map \(F\mapsto(\chi_iF)_i\) is bounded from \(\mathcal X^*\) into \(\bigoplus_i\mathcal X^*(\Lambda_i)\) with norm \(\le C_LN_L^{1/2}\): it is the transpose of \((X_i)_i\mapsto\sum_i\chi_iX_i\), which is bounded by the product rule and bounded overlap (`flat-port.md` line 580). For a global test field \(Y'\),
\[
 |\langle Y',\mathbb RF\rangle|\le\sum_iC_L\Big(\frac{C_L}{M_P}+C_LL^2\alpha\Big)\|Y'\|_{\mathcal X,Z_i}\max\{B_L,B_0\}\|\chi_iF\|_{\mathcal X^*(\Lambda_i)},
\]
and Cauchy–Schwarz with \(\sum_i\|Y'\|_{\mathcal X,Z_i}^2\le N_L\|Y'\|_{\mathcal X}^2\) and \(\sum_i\|\chi_iF\|^2\le C_L^2N_L\|F\|^2\) gives (8.2), with \(C_1\) collecting the \(C_L\)'s. By the order of constants (Section 13), \(C_1N_L\max\{B_L,B_0\}C_L/M_P\le1/8\) and \(C_1N_L\max\{B_L,B_0\}C_LL^2\alpha_*\le1/8\). So \(\|\mathbb R\|\le1/4\) and the Neumann series converges in operator norm; \(\|\mathbb B\|\le C_1N_L\max\{B_L,B_0\}\) by the same assembly. In finite dimension the right inverse \(\mathbb B(1+\mathbb R)^{-1}\) of the square matrix \(\mathbb M_\flat(U)\) is its inverse. The scalar system: the same proof, with the scalar flat models of (I1) and Lemma 7 without the vector row. \(\square\)

Status: proved, from (I1), (I2), Lemmas 3, 6, 7. (Codex's check of the earlier form, `gates/p82-curved-gate.md` lines 93–99: "\(\|\mathbb R\|\le C_LB_LN_L(M^{-1}+\alpha)\) … This proves (5.1) as a conditional perturbation result." The present form uses the flat model's commutator, so the curved-commutator transfer that the earlier text needed is not needed.)

### 8.3 Decay for supported sources

**Lemma 9 (decay).** Let \(F\in\mathcal X^*\) be supported over the pillar of \(z\), rows based there included (or over a bounded union of pillars near \(z\)). For a top \(y\), let \(\|X\|_{\mathcal X,y}\) be the restriction of the squared sum (6.2) to components over the pillar of \(y\) and its stencil neighbours. Then
\[
 \|\mathbb M_\flat(U)^{-1}F\|_{\mathcal X,y}\le C_2\,e^{-\delta_wd_{\mathbf B}(y,z)}\|F\|_{\mathcal X^*},\qquad \delta_w=\frac{\log2}{D_LM_P},
 \tag{9.1}
\]
with \(C_2\) depending on \(L\) only. The same holds for \(\mathbb S^{-1}\).

*Proof.* Each \(Z_i\) has \(d_{\mathbf B}\)-diameter at most \(D_LM_P\): side \(c_LM_Ps_i\), and only scales \(s_i/L\) and \(s_i\) occur. If a field \(G\) is supported in a set \(\mathcal S\), then \(\mathbb RG\) and \(\mathbb BG\) are supported in the \(D_LM_P\)-neighbourhood \(\mathcal S^{+D_LM_P}\): the \(i\)-th summand depends only on \(\chi_iG\), which vanishes unless \(\operatorname{supp}\chi_i\) meets \(\mathcal S\), and is supported in \(Z_i\). By induction \(\mathbb B\mathbb R^nF\) is supported in \(\{x:d_{\mathbf B}(x,z)\le(n+1)D_LM_P+C_L\}\). So its local norm at \(y\) vanishes for \(n<n_0:=d_{\mathbf B}(y,z)/(D_LM_P)-1-C_L\). Restricting an evaluated output norm is contractive. Hence
\[
 \|\mathbb M_\flat(U)^{-1}F\|_{\mathcal X,y}\le\sum_{n\ge n_0}\|\mathbb B\|4^{-n}\|F\|\le\tfrac43\|\mathbb B\|4^{-n_0}\|F\|\le C_2e^{-(\log4)d_{\mathbf B}(y,z)/(D_LM_P)}\|F\|.
\]
The rate \(\log4/(D_LM_P)\) is at least \(\delta_w\). No sharp projection of an arbitrary dual vector occurs (T6), and no count of walks is needed. \(\square\)

Status: proved. (This is Codex's repair, `gates/p82-curved-gate.md` lines 109–116, "ADVANCE".)

---

## 9. Pointwise outputs

**Lemma 10 (curved local estimate).** Let \(Q\) be a cube of side \(r\ge16\eta\) and \(Q^+\) its concentric double. Suppose that on \(Q^+\) the real \(U\) has a gauge with \(U=e^{i\eta A}\), \(r|A|+r^2|\nabla A|\le a\le a_0\), \(a_0\) absolute. Let \(u=(u_1,\dots,u_n)\), \(n\le4\), be adjoint-valued site functions on \(Q^+\) with
\[
 \Delta_Uu_\mu=g_\mu+(Eu)_\mu,\qquad |(Eu)_\mu(x)|\le a\,r^{-2}\max_\nu\max_{|x'-x|\le2\eta}|u_\nu(x')|,
\]
where \(\Delta_Uf(x)=\eta^{-2}\sum_\nu[2f(x)-\operatorname{Ad}U(x,x+\eta e_\nu)f(x+\eta e_\nu)-\operatorname{Ad}U(x,x-\eta e_\nu)f(x-\eta e_\nu)]\). Then on \(Q\), for \(0<\beta<1\),
\[
 |u|+r|\nabla_Uu|+r^{1+\beta}[\nabla_Uu]_\beta\le C_\beta\big(r^{-2}\|u\|_{2,Q^+}+r^2|g|_{\infty,Q^+}\big),
 \tag{10.1}
\]
the Hölder quotient taken at separations at most \(r\) with the covariant comparison along a straight path.

*Proof.* *Step 1 (values).* Kato's inequality \(\Delta|u_\mu|\le|\Delta_Uu_\mu|\) holds pointwise: at \(u_\mu(x)\ne0\), pair the equation with \(e=u_\mu(x)/|u_\mu(x)|\) and use \(\langle e,\operatorname{Ad}(V)v\rangle\le|v|\), valid since \(\operatorname{Ad}V\) is orthogonal on \(\mathfrak{su}(2)\) for real \(U\); then \(\eta^{-2}\sum_\nu[2|u_\mu(x)|-|u_\mu(x+\eta e_\nu)|-|u_\mu(x-\eta e_\nu)|]\le\langle e,\Delta_Uu_\mu(x)\rangle\le|\Delta_Uu_\mu(x)|\). At \(u_\mu(x)=0\) the left side is \(\le0\). With (I8): on any cube \(Q'\subset Q^+\) of side \(r'\ge16\eta\), \(\sup_{Q'/2}|u_\mu|\le C(r'^{-2}\|u_\mu\|_{2,Q'}+r'^2\sup_{Q'}|\Delta_Uu_\mu|)\). Put \(\Phi=\sup_{x\in Q^+,\mu}(d(x)/r)^2|u_\mu(x)|\), \(d\) the distance to \(\partial Q^+\). Where \(d(x)<32\eta\): \(|u_\mu(x)|\le\eta^{-2}\|u_\mu\|_{2,\{x\}}\) gives \((d/r)^2|u_\mu(x)|\le32^2r^{-2}\|u\|_2\). Otherwise take \(Q'\) of side \(d(x)/2\) about \(x\). On \(Q'\) and its \(2\eta\)-neighbourhood \(d\ge d(x)/8\), so \(|u_\nu|\le64(r/d(x))^2\Phi\) there, \(|Eu|\le64ar^{-2}(r/d(x))^2\Phi\), and
\[
 (d(x)/r)^2|u_\mu(x)|\le C(r^{-2}\|u\|_{2,Q^+}+r^2|g|)+C'a\Phi .
\]
Taking the supremum and \(a\le a_0=1/(2C')\): \(\Phi\le2C(r^{-2}\|u\|_2+r^2|g|)\). On the intermediate cube \(Q^{(1)}\) of side \(3r/2\), \(d\ge r/4\), so \(|u|\le16\Phi\) there.

*Step 2 (gradients).* In the gauge, \(\operatorname{Ad}e^{\pm i\eta X}-1=\pm i\eta\operatorname{ad}X+R_2(X)\), \(|R_2(X)|\le C\eta^2|X|^2\). Pairing the two opposite shifts in \(\Delta_U\) gives \(\Delta_U=\Delta+B\cdot\nabla+C''\), \(\nabla\) ordinary differences, with \(|B|\le C|A|\le Ca/r\) and \(|C''|\le C(|\nabla A|+|A|^2)\le Ca/r^2\). So \(\Delta u_\mu=g_\mu+(Eu)_\mu-B\cdot\nabla u_\mu-C''u_\mu\). Let \(d_1\) be the distance to \(\partial Q^{(1)}\) and \(\Psi=\sup_{Q^{(1)}}d_1|\nabla u|\). At a point \(x\) with \(d_1(x)\) above a fixed number of mesh steps, apply the free Poisson gradient bound \(|\nabla v({\rm centre})|\le C(\ell^{-1}\sup|v|+\ell\sup|\Delta v|)\) on the cube of side \(\ell=d_1(x)/4\) ((I3), (4.2); (I8)). On that cube \(d_1\ge7d_1(x)/8\), so \(|\nabla u|\le8\Psi/(7d_1(x))\); and \(|u|\le C\Phi\) by Step 1. So \(d_1(x)|\nabla u(x)|\le C(\Phi+r^2|g|)+C'a\Psi\). Within a fixed number of mesh steps of \(\partial Q^{(1)}\) use \(|\nabla u|\le2\eta^{-1}\sup|u|\). Decreasing \(a_0\) once, \(\Psi\le C(\Phi+r^2|g|)\), and \(|\nabla u|\le4\Psi/r\) where \(d_1\ge r/4\), in particular on the cube of side \(5r/4\). Finally \(|\nabla_Uu-\nabla u|\le C|A||u|\le Ca\,r^{-1}|u|\).

*Step 3 (Hölder).* By Steps 1–2, \(|\Delta u|\le C(r^{-4}\|u\|_2+|g|)\) on the cube of side \(5r/4\). (I3), second line, with \(g=0\) and \(\epsilon=(1+\beta)/2\), bounds \(|Du|+r^\beta[Du]_\beta\) on \(Q\) by \(C_\beta(r^{-3}\|u\|_2+r\sup|\Delta u|)\). The covariant correction \(\nabla_Uu-\nabla u=\mathcal A_\nabla u\) is a bond-local multiplication with coefficient \(O(|A|)\); between points at distance \(t\le r\), \(|\mathcal A_\nabla u(x)-\mathcal A_\nabla u(x')|\le C(|\nabla A||u|+|A||\nabla u|)t\). The covariant comparison along the straight path is a product of \(t/\eta\) links each within \(C\eta a/r\) of \(\mathbf 1\), so it differs from the identity by \(Cat/r\). Both corrections are at most \(Ca\,t^\beta r^{-1-\beta}\) times the right side of (10.1). \(\square\)

Status: proved, from (I3) and (I8). (Codex's check, `gates/p82-curved-gate.md` lines 120–142: "ADVANCE for Lemma 6.1"; its gloss on the bounded-forcing Hölder step, lines 135–141, is the content of (I3) with \(g=0\).)

**Proposition 11 (pointwise kernels).** Let \((a,\lambda)=S^{\circ-1}_\flat(f,b)\) with either (I) \(b=0\), \(f\) supported in the pillar of \(z\), \(|f|\le m_z^{-3}\); or (II) \(f=0\), \(b\) supported at one row \(c\) with \(y_c=z\), \(|b(c)|\le1\). Then for all tops \(y\) and rows \(c'\),
\[
 m_y|a|_y+m_y^2|\nabla_Ua|_y+m_y^{2+\alpha_{\rm H}}[\nabla_Ua]_{\alpha_{\rm H},y}\le C_3e^{-\delta_wd_{\mathbf B}(y,z)},\qquad
 |\lambda(c')|\le C_3e^{-\delta_wd_{\mathbf B}(y_{c'},z)} .
 \tag{11.1}
\]
Moreover, for \(g\) supported in the pillar of \(z\) with \(|g|\le m_z^{-2}\),
\[
 m_y^3|D(1-R)g|_y\le C_3e^{-\delta_wd_{\mathbf B}(y,z)} .
 \tag{11.2}
\]

*Proof.* *The source.* By Lemma 2, \((a,\lambda)\) are the \((A,\nu)\) components of \(X=\mathbb M_\flat(U)^{-1}F\) with \(F=(f+K^{\mathsf T}b,0,0,0,-b)\). In case (I), \(\langle B,f\rangle\le\|m^{-1}B\|_2\|mf\|_2\) and \(\|mf\|_2\le m_z\cdot m_z^{-3}\cdot(m_z^4)^{1/2}=1\) (a pillar has physical volume \(m_z^4\)). In case (II), \(|K^{\mathsf T}b|\le C_Ls^{-3}\) on the carrier, by the column sum of (7.1) and the fine conversion \(\eta^{-4}\); the same computation gives \(\|K^{\mathsf T}b\|_{E^*}\le C_L\); and \(\|b\|_{\rm count}\le1\). So \(\|F\|_{\mathcal X^*}\le C_L\), and \(F\) is supported over a bounded union of pillars near \(z\). By Lemma 9, every local norm of \(X\) on a bounded union of pillars near \(y\) is at most \(Ce^{-\delta_wd_{\mathbf B}(y,z)}\), with \(C\) absorbing \(e^{\delta_wC_L}\).

*Outputs with \(m_y\le64L\eta\).* Use \(|u(x)|\le\eta^{-2}\|u\|_{2,\{x\}}\): \(m_y|A(x)|\le m_y^2\eta^{-2}\|m^{-1}A\|_{2,\rm loc}\le(64L)^2Ce^{-\delta_wd}\); similarly \(|\nabla_UA(x)|\le\eta^{-2}\|\nabla_UA\|_{2,\rm loc}\), so \(m_y^2|\nabla_UA|\le(64L)^2Ce^{-\delta_wd}\); the Hölder quotient at separations \(t\le m_y\) is at most \(2\sup|\nabla_UA|\,t^{-\alpha_{\rm H}}\) for \(t\ge\eta\), giving \(m_y^{2+\alpha_{\rm H}}[\nabla_UA]_{\alpha_{\rm H}}\le C_L\cdot(64L)^{\alpha_{\rm H}}e^{-\delta_wd}\). All constants depend on \(L\) only. This covers bare outputs at the arbitrary boundary.

*Outputs with \(m_y>64L\eta\).* Take \(r=m_y/(4L)\ge16\eta\) and \(Q\) of side \(r\) about the output point. \(Q^+\) lies in the cell \(Z_i\) of the tile containing \(y\), which is interior (\(m_y>\eta\) means \(y\in\Omega_1\)), so the gauge \(g_i\) applies, with \(a\le L^2\alpha\cdot C\le a_0\) by the order of constants. \(Q^+\) is inside \(\Omega_0\) at distance at least \(2\eta\) from \(\Omega_0^c\), and the pillars it meets have scales between \(m_y/L\) and \(Lm_y\).

- *The \(h\) component.* Row 3 of (6.1) has zero source, so \(A_sh=Q'^{\mathsf T}\mu\), i.e. \(\Delta_Uh=Q'^{\mathsf T}\mu-Q'^{\mathsf T}m^{-2}Q'h\) on sites. Pointwise \(|Q'^{\mathsf T}\mu|\le\max|\mu|\le m^{-4}\|m^2\mu\|_{\rm top,loc}\) and \(|Q'^{\mathsf T}m^{-2}Q'h|\le m^{-2}\cdot m^{-2}\|h\|_{2,P}\) (Cauchy–Schwarz over the pillar, weight \(\eta^4m^{-4}\), and \(\sum_x|Q'(y,x)|=1\)). Lemma 10 with \(E=0\) gives \(|Dh|\le C(r^{-3}\|h\|_{2,Q^+}+r\cdot Cm^{-4}e^{-\delta_wd})\le Cm_y^{-3}e^{-\delta_wd}\).
- *The \(A\) component.* Row 1 gives \((\flat^{\mathsf T}\flat+DD^{\mathsf T})A=g_A:=f+K^{\mathsf T}b+Dh-K^{\mathsf T}KA+K^{\mathsf T}\nu\). At bonds whose stencil lies in \(\Omega_0\), the lattice Weitzenböck identity (`a3-derivative.md` (40), checked in `gates/a3-derivative-gate.md` §7.2) gives \(d^{\mathsf T}d+DD^{\mathsf T}=\Delta_U+\mathcal W\), \((\mathcal WA)_\mu=\sum_{\nu\ne\mu}[\nabla_\mu,\nabla_\nu^{\mathsf T}]A_\nu\), and \([\nabla_\mu,\nabla_\nu^{\mathsf T}]f(x)=\eta^{-2}[\operatorname{Ad}(T_1)-\operatorname{Ad}(T_2)]f(x+e_\mu-e_\nu)\), with \(T_1,T_2\) the two transports around one plaquette. In the gauge \(|\partial U(p)-1|\le C\eta^2(|\nabla A|+|A|^2)\le C\eta^2a r^{-2}\), so \(|\mathcal WA|\le Car^{-2}\max|A|\) over a \(2\eta\)-neighbourhood. For \(\mathfrak d\), \(\mathfrak d^{\mathsf T}\mathfrak d=d^{\mathsf T}d+V\) with \(V=d^{\mathsf T}E_{\mathfrak c}+E_{\mathfrak c}^{\mathsf T}d+E_{\mathfrak c}^{\mathsf T}E_{\mathfrak c}\), \(E_{\mathfrak c}=\mathfrak d-d\), whose entries are at most \(C\eta^{-1}|\mathbf 1-\operatorname{Ad}\partial U(p)|\le Ca\eta r^{-2}\) with fixed finite support; with \(|d_{pq}|\le C/\eta\), \(|VA|\le Car^{-2}\max|A|\) (`gates/p82-curved-gate.md` line 220). So Lemma 10 applies with \(E=-\mathcal W\) (forward curl) or \(E=-\mathcal W-V\) (plaquette curl), and \(g=g_A\). Every term of \(g_A\) is at most \(Cm_y^{-3}e^{-\delta_wd}\): the source terms appear only if \(Q^+\) meets their support, and then \(d_{\mathbf B}(y,z)\le C_L\) and \(m_z\) is comparable to \(m_y\); \(|Dh|\) is bounded above; \(|K^{\mathsf T}KA(b)|\le Cs^{-4}\|A\|_{2,\rm carrier}\le Cs^{-3}\|m^{-1}A\|_{2,\rm carrier}\) by (7.1) and Cauchy–Schwarz on the carrier; \(|K^{\mathsf T}\nu|\le Cs^{-3}\max|\nu|\) and \(|\nu|\le\|\nu\|_{\rm count,loc}\). Since \(r^{-2}\|A\|_{2,Q^+}\le Cr^{-2}m_y\|m^{-1}A\|_2\le Cm_y^{-1}e^{-\delta_wd}\) and \(r^2|g_A|\le Cm_y^{-1}e^{-\delta_wd}\), (10.1) gives (11.1) for \(a\) on \(Q\). Hölder separations between \(r\) and \(m_y\) follow from twice the gradient bound, with a factor \((4L)^{\alpha_{\rm H}}\).
- *The multiplier.* \(|\lambda(c')|=|\nu(c')|\le\|\nu\|_{\rm count,loc}\le Ce^{-\delta_wd_{\mathbf B}(y_{c'},z)}\).
- *(11.2).* By Lemma 1(iii), \((1-R)g\) is the \(h\) output of \(\mathbb S^{-1}(g,0,0)\), and \(\|g\|_2\le m_z^{-2}(m_z^4)^{1/2}=1\). Row 3 of \(\mathbb S\) still has zero source, so the \(h\) step above applies verbatim, with Lemma 9 for \(\mathbb S\): \(m_y^3|Dh|\le Ce^{-\delta_wd}\). At outputs with \(m_y\le64L\eta\) use the pointwise \(\ell^2\) bound and one difference. \(\square\)

Status: proved, from Lemmas 1, 2, 5, 9, 10. (Codex's check, `gates/p82-curved-gate.md` lines 144–161: "ADVANCE … after the supported-source repair"; plaquette-curl case lines 218–220.)

---

## 10. Proof of Theorem P

**(a)** Proposition 8 and Lemma 2 give invertibility of \(\mathbb M_\flat(U)\), \(\Sigma_\flat\) and \(S^\circ_\flat\). If \(K\) were not onto, \(S^\circ_\flat(a,\lambda)=(0,b)\) with \(b\notin\operatorname{ran}K\) would have no solution; so \(K\) is onto. By Lemma 1(ii), \(\Delta_U\) maps \(\ker Q'\) onto \(\operatorname{ran}R\). It is injective on \(\ker Q'\): \(\Delta_U\chi=0\) and \(Q'\chi=0\) give \(\langle\chi,A_s\chi\rangle=0\), hence \(\chi=0\) (Lemma 1(i)). The named blocks exist: the field operator \(\flat^{\mathsf T}\flat+DRD^{\mathsf T}+K^{\mathsf T}K\) is a sum of nonnegative forms; a vector in its kernel has \(\flat a=0\), \(RD^{\mathsf T}a=0\), \(Ka=0\), so \((a,0)\) is a null vector of the invertible \(\Sigma_\flat\), and \(a=0\). So \(G\) exists, \(C_0=KGK^{\mathsf T}\) is positive definite since \(K^{\mathsf T}\) is injective, and \(H,T\) exist (`gates/p82-curved-gate.md` line 175).

**(b)** Fix \(w\in\mathcal W_\theta\), \(\theta\le\theta_0=\delta_w/2\). Assign each bond to the pillar of its base point and split \(f=\sum_zf\mathbf 1_{P_z}\), with \(|f\mathbf 1_{P_z}|\le m_z^{-3}\|f\|_{F,w}/w(z)\); split \(b=\sum_cb(c)e_c\), with \(|b(c)|\le\|b\|_{Y,w}/w(y_c)\). These are pointwise splittings of the force and the datum; the operator is applied to each supported piece, as Proposition 11 requires. By linearity, (11.1), and \(w(y)/w(z)\le e^{\theta d_{\mathbf B}(y,z)}\),
\[
 w(y)\big(m_y|a|_y+m_y^2|\nabla_Ua|_y\big)\le C_3\Big(\sum_ze^{-(\delta_w-\theta)d_{\mathbf B}(y,z)}\Big)\big(\|f\|_{F,w}+C_L\|b\|_{Y,w}\big),
\]
using that at most \(C_L\) rows have a given base top. The same with centre \(y_{c'}\) bounds \(w(y_{c'})|\lambda(c')|\). For \(\delta_w-\theta\ge\delta_w/2=:\tau\), (I4) with \(p=0\) bounds the sum by \(C(L,0,\delta_w/2)\), because \(\rho\ge\rho_P\ge32\log L/\delta_w=2\cdot8\log L/\tau\). This is (1.1) with \(C^\circ:=C_3C_L\,C(L,0,\delta_w/2)\) (enlarged below for (c), (d)).

**(c)** Repeat (b) with the Hölder member of (11.1).

**(d)** For \(a\in X_w\), \(g=D^{\mathsf T}a\) is a sum of transported backward first differences of \(a\). The \(X\) norm includes their forward versions on the neighbouring stencils; scales differ by at most \(L\) and weights by \(e^{\theta C_L}\). So \(|D^{\mathsf T}a|_z\le C_Lm_z^{-2}w(z)^{-1}\|a\|_{X,w}\). At a Dirichlet boundary \(m=\eta\) and the zero-extension difference is bounded by the value member. Split \(g\) into pillar pieces, apply (11.2) to each, and sum as in (b): \(w(y)m_y^3|D(1-R)D^{\mathsf T}a|_y\le C^\circ\|a\|_{X,w}\). (`gates/p82-curved-gate.md` lines 186–192.)

**(e)** (b) holds for every \(w\in\mathcal W_\theta\). By `a3-derivative.md` Lemma 8.2 with the finite-colour argument (`gates/a3-derivative-gate.md` §8, "ADVANCE with the finite-colour argument"; written out in `gates/p82-curved-gate.md` lines 194–200), this is equivalent, up to a fixed colour factor, to the first-line BGR11 row sums at rate \(\theta\). The argument: use the amplitudes \(s_f=m^{-3}\), \(s_a=m^{-1}\), \(s_{\nabla a}=m^{-2}\), \(s_b=s_\lambda=1\), the fine input measure \(\eta^4\) and the raw row measure \(1\). For a fixed output \(i\) choose \(w_j=e^{-\theta d(i,j)}\in\mathcal W_\theta\) (triangle inequality). Fix an output colour coordinate \(e_r\) and choose each input vector of magnitude \(s_j/w_j\) so that \(e_r^*A_{ij}v_j\) is nonnegative with maximal modulus. The all-weight bound then controls \(\sum_j\mu_js_i^{-1}s_j\|A_{ij}^*e_r\|e^{\theta d(i,j)}\). Sum over the fixed number of output colour and direction coordinates and use \(\|A_{ij}\|\le\sum_r\|A_{ij}^*e_r\|\). Apply this separately to the differentiated output operator. This gives the row sums; no column conclusion follows, and P82° does not need one. If a consumer writes the row kernel with physical row cell weights, divide its entries by those weights before applying BGR10; the operator and its row sum are unchanged (SA L11892–11947).

Both curls are covered: every step above was written for \(\flat\in\{d,\mathfrak d\}\). One constant \(C^\circ\) serves both. \(\square\)

Status of Theorem P: proved, from (I1)–(I5), (I8).

---

## 11. Proof of Proposition REG

This is `a3-close.md` §1 (Claude; checked by Codex in `gates/a3-close-meet-gate.md` §A, "ADVANCE as an implication", first failing step none), rewritten with \(W_\natural\) in place of the clashing \(W\) (Section 2.3, item 3).

*(i) Balaban's class.* (I6) gives at every plaquette and bond of \(\Omega_0\): \(|\partial U_0(p)-1|\le B\varepsilon_1\eta^2\mathsf L(p)^{-2}\) and \(|J(U_0)(b)|\le B\varepsilon_1\mathsf L(b)^{-3}\). Balaban's class \(\mathcal U_k(\{\Omega_j\},\alpha_0)\) (CMP 99 (75–102), (1.7)–(1.9), p. 77, read on the scan in `a3-close.md` and again in `gates/a3-close-meet-gate.md` §A.1) is \(|U(\partial p)-1|<\alpha_0L^{-2j}\) for \(p\in\Omega_j\), and \(|(D^{\eta*}_U\partial U)(b)|<\alpha_0L^{-2j}(L^j\eta)^{-1}\) for \(b\in\Omega_j\), where \(p\in\Omega_j\) means some corner lies in \(\Omega_j\). In level-\(k\) units \(L^j\eta=\xi_j\), \(L^{-2j}=\eta^2\xi_j^{-2}\). A corner in \(\Omega_j\) has scale at least \(\xi_j\), so \(\mathsf L(p),\mathsf L(b)\ge\xi_j\). The curvature half gives (1.7) with \(\alpha_0=B\varepsilon_1\). For (1.9): \(\eta^{-2}D^*_U\partial U\) has anti-Hermitian part \(J(U)\) at every bond whose six plaquettes lie in \(\Omega_0\), and Hermitian part bounded by \(CB^2\varepsilon_1^2\mathsf L^{-3}\), through \(\operatorname{Re}W-1=-\frac12(W-1)^*(W-1)\) for unitary \(W\). So (1.9) holds there with \(\alpha_0=C(B\varepsilon_1+B^2\varepsilon_1^2)\le2CB\varepsilon_1\). Only such bonds are read below.

*(ii) Geometry for \(j\ge1\).* Let \(Z\subset\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\) be a cube of side \(c_{\rm reg}M_P\xi_j\). Let \(\square\) be the union of the cubes of side \(W_\natural\xi_j\), aligned with the level-\(j\) blocks, that meet \(Z\). It is a cube of side \(M''\xi_j\le M'\xi_j\), \(M'=c_{\rm reg}M_P+2W_\natural\). Balaban's enlargement \(\tilde\square\) (the cover of the outermost auxiliary nested cube, whose boundary lies at distance \(2W_\natural\xi_j\) from \(\square\); total enlargement \(W_\natural\xi_j/(1-L^{-1})\le2W_\natural\xi_j\), `a1-balaban.md` lines 709–711) satisfies \(\tilde\square\subset Z+4W_\natural\xi_j\). Since \(Z\subset\Omega_j\) and \(\operatorname{dist}_\infty(\Omega_{j-1}^c,\Omega_j)>\rho\xi_{j-1}=\rho\xi_j/L\), the condition \(\rho\ge4LW_\natural+2L\) gives \(\rho\xi_j/L\ge(4W_\natural+2)\xi_j\). So \(\tilde\square\subset\Omega_{j-1}\), at distance more than \(2\xi_j\ge2\eta\) from \(\Omega_{j-1}^c\). Every plaquette and every bond with its six plaquettes meeting \(\tilde\square\) lies in \(\Omega_0\).

*(iii) Proposition 6 at level \(j\).* Balaban's proof of CMP 99 (75–102) Proposition 6 (pp. 98–99) first drops the members \(\Omega_{j'}\), \(j'>j\): the class conditions at a coarser scale are stronger, so \(U_0\) lies in the class of the truncated sequence with the same \(\alpha_0\). After rescaling \(\xi_j=1\), the hypotheses are used only on \(\tilde\square\subset\Omega_{j-1}\), at scale \(\xi_{j-1}\), which costs \(L^2\) (curvature) and \(L^3\) (current); this is his (1.128) and (1.132). (I7) gives, under \(7dL^2M''\alpha_0\le c_1\), a gauge \(u\) on \(\tilde\square\) with \(U_0^{u^{-1}}=e^{i\eta A}\) and, on \(\square\supset Z\), in level-\(j\) units (his (1.134), (1.136)), \(\xi_j|A|+\xi_j^2|\nabla A|<14dL^2B_1M''\alpha_0\le28CdL^2B_1BM'\varepsilon_1\), \(\nabla\) the ordinary difference. This is Reg\(_\alpha\) on \(Z\). The auxiliary nested family has gap \(W_\natural\) above the flat floor, so the flat inputs of (I7) apply to it.

*(iv) \(j=0\), no current needed.* Let \(Z\subset\Omega_0\cap(\mathcal L_0\cup\mathcal L_1)\) have side \(n\eta\), \(n=c_{\rm reg}M_P\). In complete axial gauge from a corner of \(Z\) (\(U_1\equiv1\); \(U_2=1\) on \(x_1=0\); \(U_3=1\) on \(x_1=x_2=0\); \(U_4=1\) on \(x_1=x_2=x_3=0\)), each link \(U_\mu(x)\) is the holonomy of a loop bounding a staircase of at most \(3n\) plaquettes of \(Z\). By unitarity \(|U(b)-1|\le3nB\varepsilon_1\) (since \(\mathsf L(p)\ge\eta\)). For \(U=e^{i\eta A}\) with eigenvalue angles \(\pm\theta\), \(|\theta|\le\pi\), \(|U-1|=2|\sin(\theta/2)|\ge(2/\pi)|\theta|\), so \(\eta|A|\le\frac{3\pi}2nB\varepsilon_1\) and \(\eta^2|\nabla A|\le2\sup\eta|A|\le3\pi nB\varepsilon_1\). This is Reg\(_\alpha\) at \(j=0\) with \(\alpha=5\pi c_{\rm reg}M_PB\varepsilon_1\).

Take \(C_{\rm reg}\) the larger of the two constants and \(a_{\rm reg}\) from the smallness condition of (I7). \(\square\)

Status: proved, from (I6), (I7). The curvature-only base case (iv) and the current-based case (iii) together are where criticality enters (C7).

---

## 12. Theorem P82 and its consumers

Theorem P82 is proved in Section 3 from Theorem P and Proposition REG. Here is how it meets each consumer.

**`a3-derivative.md` Lemma 8.1.** Its premise: (1.1) for \(S^\circ\) with a constant \(C^\circ\), for every \(w\in\mathcal W_\theta\) (Lemma 8.2's reading), the Hölder member, and \(D(1-R)D^{\mathsf T}:X_w\to F_w\), at the real regular critical reference, with the outline's \(R\) and \(K_0\), in the curl convention of the action (plaquette curl, `gates/a3-derivative-gate.md` §7). These are Theorem P82 (b), (c), (d), with \(\flat=\mathfrak d\) (or \(d\)). Its rate \(\theta=\delta_0/8\) is admissible with \(\delta_0:=2\theta_0=\delta_w\), since \(\delta_w/8\le\theta_0=\delta_w/2\). Its smallness conditions "\(C^\circ C_2\kappa_{\rm A3}\le1/8\) and \(C^\circ C_Nr\le1/8\)" (line 476) are ceilings on \(\kappa_{\rm A3}=C_L\mathfrak M\bar\varepsilon\) and \(r\), chosen after \(C^\circ\). That is SA Theorem 4's own form "\(\bar\varepsilon\le c(L)/\mathfrak M\), with \(\bar\varepsilon\) chosen after \(\mathfrak M\)" (SA L9734).

**Multiplier normalization (M1).** The multiplier output of (b) is the counting multiplier, the one `a3-derivative.md` (34) uses and `a3-close.md` §4 settles (checked by Codex, `gates/a3-close-meet-gate.md` §C, with the wording repair "in counting normalization; not uniformly for physical cell weights tending to zero").

**Joined and meet sequences.** Theorem 6(c) (`a3-derivative.md` §10) and TH4 "on every subordinate separated meet with an erosion tower" (`st1-draft2.md` line 211) apply P82° at the references of joined or meet sequences. Theorem P covers every separated sequence with \(M_P\mid M_1\) and \(\rho\ge\rho_P\), whatever its shape. The auxiliary joined sequence of `a3-close.md` Lemma J is separated with gap \(\rho\) and cube size \(\mathfrak M\) (Lemma J(b), checked in `gates/a3-close-meet-gate.md` §B, "J(b): none fails"). So P82° holds there. Whether that auxiliary sequence is the outline's joined sequence is a separate premise (`gates/a3-close-meet-gate.md` D1). It is not a P82° premise.

**TH4 constants.** With P82°, TH4 holds with \(\theta_4=\delta_w/8\) and \(C_4\) a function of \(C^\circ\), \(C_N\), \(C_b\) and \(L\) (`a3-derivative.md` (34) and §7), conditional on P81. These enter ST1's step 2 (`st1-draft2.md` line 237) and the rate \(\delta=\min\{\delta_P,\theta_4\}\) of its (19a).

**What Theorem T and (D4) still need from PR1 beyond P82°.** Nothing linear at the real critical reference. They need P81 (row 81: \(\Phi\) holomorphic, critical at real data, regular, uniform in depth; `a3-derivative.md` line 556 item (2)) and the items ST1 itself lists (`st1-draft2.md` §15.2). Those are outside P82°.

---

## 13. Order of constants, constant by constant

The rows are those of `c4-order.md`. IN1 requires that "the constants of the stage, background and response bounds be fixed before \(\kappa\) and be independent of \(M\) and \(\bar\kappa\), with \(M\) entering only as a lower bound" (`st1-draft2.md` line 253, quoting `in1-draft.md` lines 807–808), and that the (I-1) constants be row-7 constants (`in1-draft.md` E.3, remark 2). \(\kappa_{\rm IN}\) is row 8, \(\bar\kappa\) row 9, \(M\) row 12. No P82° constant reads rows 8 or later. No P82° constant reads the depth, the mesh, the volume or the region shapes.

| Constant | Defined by | Depends on | Row | Before \(\kappa_{\rm IN}\) | Free of \(M\), \(\bar\kappa\) |
|---|---|---|---|---|---|
| \(L\), \(\alpha_{\rm H}\) | free data | — | 1, 3 | yes | yes |
| \(B_L,C_L,N_L,D_L,a_L,c_L\) | (I1), (I2), Lemma 4, cells | \(L\) | 3 | yes | yes: (I1) is uniform in the local box size (`flat-port.md` line 582) |
| \(B_0\) | Lemma 7 | absolute | 3 | yes | yes |
| \(\delta_0(L)\) | Lemma 5 | \(L\) | 3 | yes | yes |
| \(a_0\), \(C_\beta\) | Lemma 10 | absolute, \(\beta=\alpha_{\rm H}\) | 3 | yes | yes |
| \(C_1\) | Proposition 8 | \(L\) | 3 | yes | yes |
| \(M_P\) | \(C_1N_L\max\{B_L,B_0\}C_L/M_P\le1/8\) | \(L\) | 4 (\(m_w\)) | yes | yes |
| \(c_{\rm reg}=c_LL\) | Section 8.1 | \(L\) | 4 | yes | yes |
| \(\alpha_*\) | \(C_1N_L\max\{B_L,B_0\}C_LL^2\alpha_*\le1/8\), \(CL^2\alpha_*\le a_0\), \(L^2\alpha_*\le\delta_0(L)\) | \(L\); not \(M_P\), not \(M_1\) (as SA L10307 asks: "fixed before \(M_1\) and … independent of \(M_1\)") | 4 | yes | yes |
| \(\delta_w=\log2/(D_LM_P)\), \(\theta_0=\delta_w/2\) | Lemma 9, Theorem P(b) | \(L\) | 4 | yes | yes |
| \(C_2,C_3\) | Lemma 9, Proposition 11 | \(L,\alpha_{\rm H}\) | 4–5 | yes | yes |
| \(C(L,0,\delta_w/2)\) | (I4) | \(L\) (uniform in \(\rho\) once (5.4) holds) | 5 | yes | yes |
| \(C^\circ\) | Section 10 | all the above | 5 | yes | yes |
| \(W_\natural\) | flat floor for (I7)'s auxiliary family | \(L\) | 4 ("collar/reset widths \(W\)") | yes | yes |
| \(C_{\rm reg},a_{\rm reg}\) | Proposition REG | \(L\), \(B\) of (I6), Balaban's \(B_1,c_1\) | 4–7 | yes | yes |
| \(M_1\) | power of \(L\), \(M_P\mid M_1\), other row-6 floors | earlier rows | 6 | yes | yes |
| \(\rho_P\) | \(\max\{C_LM_PL,\ 32\log L/\delta_w,\ \text{flat-port floors}\}\) | \(L\) | 6 (lower bound on \(R_1\)) | yes | yes |
| \(\rho=R_1M_1\) | \(\rho\ge\max\{\rho_P,4LW_\natural+2L\}\) | lower bounds by earlier numbers | 6 | yes | yes |
| \(\varepsilon_P=\min\{\alpha_*,a_{\rm reg}\}/(C_{\rm reg}M')\), \(M'=c_{\rm reg}M_P+2W_\natural\) | Theorem P82 | \(L\) only (not \(M_1\)) | 7 (part of \(\bar\varepsilon\)) | yes | yes |
| \(\kappa_{\rm A3}=C_L\mathfrak M\bar\varepsilon\), \(r\), \(r_B\) | consumer Lemma 8.1: \(C^\circ C_2\kappa_{\rm A3}\le1/8\), \(C^\circ C_Nr\le1/8\) | \(C^\circ\), \(M_1\), \(L\) | 7 | yes | yes |
| \(\theta_4=\delta_w/8\), \(C_4\) | TH4 | \(C^\circ\), \(L\) | 7 | yes | yes |

Three remarks.

1. **Non-circularity at row 6.** \(\rho_P\) needs \(\delta_w\), which needs \(M_P\) only. \(\rho_P\cdot\delta_w\) does not involve \(M_1\). So \(R_1\) is chosen after the rates, as `c4-order.md` row 6 and SA L9916 require, and ST1's (19a), \(\delta\rho_0\ge64\log L\), is again a lower bound on \(R_1\).
2. **\(M_1\) does not enter \(\varepsilon_P\).** The Reg cubes have side \(c_{\rm reg}M_P\xi_j\), not \(M_1\xi_j\). SA's Theorem 4 allows \(\bar\varepsilon\le c(L)/\mathfrak M\); P82° itself needs less. The consumer's \(\kappa_{\rm A3}\) does carry \(\mathfrak M=M_1\), as SA states.
3. **No decoupling parameter.** P82° involves no decoupling polydisc, so \(\bar\kappa\) cannot enter. The construction size \(M\) does not occur in any P82° statement. Attack B shows the one route (CA-I 4.14) that would have put \(M\) in.

---

## 14. Status of every step, and what P82° does not cover

### 14.1 Status table

| Step | Statement | Status | Rests on |
|---|---|---|---|
| Section 2.3 | notation: \(\kappa_{\rm A3}\), \(\kappa_{\rm IN}\); \(M_P,M_1,M\); \(W_\natural\) | proved (a reading of `a1-balaban.md` lines 708–723 and `flat-port.md` §§8.2, 12) | — |
| Lemma 1 | scalar block, \(R\), \(\Delta_U\ker Q'=\operatorname{ran}R\) | proved | definitions; regularity of \(U\) |
| Lemma 2 | Schur complements | proved | Lemma 1 |
| Lemma 3 | gauge covariance | proved | (I5) |
| Lemma 4 | locality | proved | (I5) |
| Lemma 5 | rows and pillar means in one gauge | proved | (I5) |
| Lemma 6 | coefficient comparison, both curls | proved | Lemma 5, Reg's derivative member |
| Lemma 7 | bare local models at any unitary \(U\), both curls | proved | — |
| Proposition 8 | parametrix | proved | (I1), (I2), Lemmas 3, 6, 7 |
| Lemma 9 | decay for supported sources | proved | Proposition 8 |
| Lemma 10 | curved local estimate | proved | (I3), (I8) |
| Proposition 11 | pointwise kernels, both curls | proved | Lemmas 1, 2, 5, 9, 10; Weitzenböck (40) |
| Theorem P | (a)–(e) on Reg\(_\alpha\) | proved | (I1)–(I5), (I8) |
| Proposition REG | \(U_0\in\) Reg\(_\alpha\) | proved | (I6), (I7) |
| Theorem P82 | P82° at \(U_0\) | proved | Theorem P, Proposition REG |
| Section 13 | order of constants | proved (each condition is a lower bound or a ceiling by earlier numbers) | `c4-order.md` rows 1–7 |

**Outstanding inside P82°: none.**

### 14.2 What the imports rest on

(I1)–(I3) are FP1 ([C], checked by Claude in `gates/flat-port-gate.md`). (I4), (I5), (I8) are `a3-balaban.md` reads, checked by Claude in `gates/a3-balaban-reads-gate.md`. (I6), (I7) are `a1-balaban.md`, checked by Claude in `gates/a1-balaban-gate.md`, conditional on F0 = FP1. Each import has had one cross-provider check by hand. The flat package FP1 itself rests on Balaban CMP 89, 95, 96 as ported in `flat-port.md` (gate defect D1 of `gates/a1-balaban-gate.md`: "F0 also rests on CMP 89"). None of this is changed here.

### 14.3 Not covered by P82° (other PR1 clauses)

1. **Complex references.** P82° is real. For \(U=e^{i\eta A'}U_r\) with \(U_r\) in the class and \(m|A'|+m^2|\nabla A'|\le\alpha_1\), Lemmas 5–6 are analytic in the complex cell potential, so Proposition 8 and Lemma 9 hold and \(\mathbb M(U)^{-1}\) is holomorphic in \(A'\), as a uniform limit of holomorphic partial sums. But Lemma 10's value step uses Kato's inequality, which needs a real reference. The complex pointwise members would follow from the real ones by a resolvent identity in the weighted norms. That is not written. This is the template of CA-I 4.14 (real positivity, then a sector bound, then \(AC=1\) on the complex ball), which ports here; it is PR1(2) on the complex datum polydisc, not P82°.
2. **The independent-current system (M2)** and the second paragraph of SA Theorem 4: `a3-derivative.md` §9.1 says the outline does not yet specify the operator ("an independent-current extension is an additional specified operator", SA 11798).
3. **The \(\mathbf V_0=\mathbf 1\) periodisation clause:** flat and linear (`a3-derivative.md` §9.2); FP1.
4. **Layered stage pairs** (PR1(5), ⟦open: PR-lay⟧): a different family of references, owned by the (D4) lanes. IN1 records that their constants must be row-7 constants (`in1-draft.md` E.3, remark 2). Theorem P supplies the real part of that requirement for every real reference in Reg\(_\alpha\); whether the layered stage references are in Reg\(_\alpha\) is the layered admission question, not P82°.

### 14.4 Defects of earlier texts, ranked by what each breaks

1. *`a3-close.md` §1, notation (breaks the literal gap condition).* "\(W:=R_1M_1\)" with "\(\rho_0'\ge4LW+2L\)" is unsatisfiable if \(R_1M_1\) is the outline's gap. Repair: \(W_\natural\), the auxiliary gap of (I7), a row-4 constant (Section 2.3). The mathematics is unchanged.
2. *`p82-curved.md` §§2.1, 5, 7(f) (Codex's D1–D3).* Repaired as Codex proposed; built in here (T5; Lemma 9; Lemma 7 and Proposition 11 with both curls).
3. *`st1-draft2.md` line 932 (status).* It lists P82° as open with `a3-derivative.md:556` as source and does not cite `p82-curved.md`, its gate, or `a3-close.md` §1. With this draft, the line should read: P82° proved as an implication from FP1 and the A1 port (this draft, Theorem P82).
4. *`a3-derivative.md` §12 (status).* Same as 3.

---

## 15. Sources read in this session

| Source | Lines | What was read |
|---|---|---|
| SA `ym4.tex` | 9734–9740 | Theorem 4, statement and \(\bar\varepsilon\le c(L)/\mathfrak M\) |
| SA | 10129–10137 | regular pairs; gauge clause "bound is \(\alpha_0\) on the entire cube" |
| SA | 10287, 10307 | Statements 2 and 4 of (1c); "ceiling … independent of \(M_1\)" |
| SA | 10533–10546 | mechanism (f): unfolding and parametrix |
| SA | 11313–11327 | (PX114), the plaquette Hessian and its curl |
| SA index | chunk-09, chunk-10, chunk-11 rows | locations of the above, BGR10–BGR13 (11892–11947) |
| CA-I | 46035–46066 | Theorem 4.14, hypotheses (floors on \(M\)) and clause (A) (\(AC=1\)) |
| CA-I | 47703–47704, 47728–47729 | positivity and sector bound; unit box side \(\ell=M/12d\) |
| CA-I index | `ca-4.12-4.19/README.md`, chunk-03, chunk-04 | status "sketched" of the positivity step |
| Y3 | 1205–1235 | method summary for the background inverse |
| Y3 | 20764–20790 | Theorem I-28-75, the three-dimensional regular cube gauge |
| Y3 | 21184–21292 | Section "The inverse for regular configurations", class \(\mathfrak P^\natural_t\), Theorem I-65-83 |
| Y3 | 21840–21875, 22493–22530 | the regular local inverse lemma; parametrix constants |
| library | `a3-derivative.md` whole; `p82-curved.md` whole; `a3-close.md` whole; `gates/p82-curved-gate.md` whole; `gates/flat-port-gate.md` whole; `flat-port.md` 144–165, 472–721; `a1-balaban.md` 568–727, 2421–2433; `a3-balaban.md` 120–136, 436–445; `ym4-assembly.md` 160–214; `st1-draft2.md` 196–275; `in1-draft.md` 57–62, 800–812; `c4-order.md` rows 1–22; `gates/a3-close-meet-gate.md` 1–60; `gates/a3-balaban-reads-gate.md` (verdicts); `gates/a1-balaban-gate.md` (verdict lines) | as cited |

Nothing was copied from Balaban's papers. Claims about his text are taken from the library notes and gates named at each use, which read the scans.

**Method.** No numeric job, no subagent, no commit. Only this file was written.

## Result

P82° is proved (Theorem P82): at the curved real critical reference \(U_0=U^\circ(\mathbf V_0)\) of A1, on every separated sequence with \(M_P\mid M_1\) and \(\rho\ge\max\{\rho_P,4LW_\natural+2L\}\), for \(\varepsilon_1\le\varepsilon_P\), the operator \(S^\circ\) with the outline's \(R\) and \(K_0\), for the forward and the plaquette curl, is invertible with \(K_0\) onto; its inverse obeys (1.1) for every \(w\in\mathcal W_\theta\), \(\theta\le\theta_0\), with the Hölder member, the member \(D(1-R)D^{\mathsf T}:X_w\to F_w\), and the BGR11 row sums; all constants depend on \(L\) and \(\alpha_{\rm H}\) only and are fixed at rows 3–7 of `c4-order.md`, before \(\kappa_{\rm IN}\), independent of \(M\), \(\bar\kappa\), depth, mesh, volume and region shape. The proof is an implication from FP1 and the A1 port, each import checked once by another provider. No step is Outstanding.
