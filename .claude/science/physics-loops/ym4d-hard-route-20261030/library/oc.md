# Own-constant gauge condition: CA-I Lemma 4.13:lem-own-constant

Provenance: Codex, 2026-11-05, checkout `01b0ab934075ccce5b5fc8c1c89fc196d6a11fac`. The target statement and proposed route are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account revision `31a47c543775`; the underlying multiscale gauge framework is due to Tadeusz Balaban. Research text, not an audit; no status granted. Hand arguments only. This note has not received an independent check.

## Current checkpoint

The target is CA-I `4.13:lem-own-constant`, L45203–45234. The Result below is a proof by porting the account's earlier argument, with its standing smallness and volume conditions made explicit. This is a reconciliation of two passages of their text, not a new gauge theorem. The decisive earlier passages are `4.9:prop-real-backgrounds` (a), `4.9:cor-printed-pairs`, and the transport part of `4.9:lem-thin-cube-gradient`. Their analytic input is Balaban's proved minimal-orbit theorem, including (9). No step below assumes the target lemma. The other clauses of the hereditary class, and the later large-field admission problems, remain separate obligations.

## 1. Source identities and comparison

The requested source files were already present at `/tmp/sa_ym4.tex` and `/tmp/sa_ca_{I,II,III}.tex`. Their SHA-256 values agree with the pinned sources recorded in frozen [mu](mu.md):

| File | SHA-256 |
|---|---|
| SA outline | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The source indexes were searched first, including neighbouring rows. The relevant entries are outline chunk 09 (SA L9646–9654, L9684–9691), its obligations, CA `ca-4.12-4.19/chunk-02.md` (L45162–45234), and `ca-full/index.tsv` (§§4.8–4.9). The outline defines the local gauge clause and sketches a local regularity theorem. It does not identify all CA printed pairs. The complete account supplies the closer argument. Its later lemma and open lists (CA-I L166622–166623; CA-III L111213–111214) retain the declaration “proof outstanding”. This note must distinguish those declarations from the earlier argument.

| Frozen text | What it gives | Difference from this target |
|---|---|---|
| [mu](mu.md), §§4–8; [Claude check](../gates/mu-gate.md) | Unique regular real minimizer, fixed axial representative, continued complex map and arbitrary-subdomain nesting in the actual Lemma 4 window | Supplies the minimizer identity and admission where the near-product construction uses them. It does not give the own-constant gradient estimate. |
| [piv](piv.md), §§1, 5–6, Result | A finite holomorphic pivot graph and contour bounds on admitted HMA domains | Uses the outline's averaging convention and primitive AV/CURV inputs. Neither its graph nor its contour bound is CMP 109 (1.12). |
| [st1-r4](st1-r4.md), Lemma 5 | A regular critical orbit, local carrier gauges, and a chart under A1/F0/REG and CV | Its determining rows, mean representative, carrier gauges and admission premises differ from Balaban's actual pairs. It does not assert the exact constant or step reproduction here. |
| [hma](hma.md), D6, Theorem 8, Lemma 9 | A Gaussian identity under PH1–PH4; a physical admission implication under Q-real/F0 and enlarged-box hypotheses | Lemma 9 has a bound with its own `C_pot`, current and collar premises. PH3 is a branch-match input. Neither is the present lemma. |

Thus none of these four frozen texts already proves the target. The appropriate route is a port of the account's §4.9, with mu used for its established minimizer identification. All credit for the cube-gauge construction and the proof mechanism remains with Balaban and Sussman–Alpoge (with Claude and Codex as authors of their text).

## 2. The exact clause and its inputs

Write
\[
 c=c_\square=c_{12},\qquad B=B^{(109)}=B_{12},\qquad
 S=cLM,\qquad \xi_j=L^{-j}.                                      \tag{1}
\]
Here \(B\) is the CMP 109 constant. It differs from the constant called \(B\) in CMP 119 (2.38). CA-I L35286–35290 explicitly identifies \(B_{12}\) with CMP 109's constant.

We use the chapter's closed-cube convention (CA-I L35050–35117, L35281–35367). Let \(\operatorname{bd}Q\) consist of bonds with both endpoints in \(Q\). Let \(\operatorname{pp}Q\) consist of parallel adjacent bonds in \(Q\), including translations in the bond's direction. The widened clause at level \(j\), domain \(X\), and radius \(a>0\) is
\[
\begin{split}
&\text{for every closed cube }Q\subset X
  \text{ of side at most }SL^j\text{ fine steps, there exist }u_Q,A_Q\text{ with}\\
&u_Q:\operatorname{st}Q\longrightarrow G,\quad
 A_Q:\operatorname{bd}Q\longrightarrow\mathfrak g,\quad
 U^{u_Q}=e^{i\xi_j A_Q},\\
&|A_Q(b)|<SBa,\qquad
 \xi_j^{-1}|A_Q(b+e_\nu)-A_Q(b)|<SBa .                         \tag{2}
\end{split}
\]
The second bound ranges over \(\operatorname{pp}Q\). A cube with no bonds imposes no bond condition. This is the reading \((\ell1)=(\mathrm{L}\text{-}12)\). It is a condition on the **unitary factor** in an exhibited decomposition \(\mathbf U=U'U\). The bound is the same for all cube sides. The ambient-intersection reading \((\ell2)\) is a different assertion.

The proof uses the following precise published inputs, in the account's conventions.

1. **Real averaging.** If the global real field has curvature below \(a\xi_k^2\), with \(a<c_{98}(d,L)\), its level-\(k\) averaged plaquettes have defect below \(2a\). This is CMP 98 Proposition 2, (52)–(54), used in CMP 109 (1.2). It is the input of CA-I L36645–36649. No complex version of CMP 109 (1.17) is used for this step.
2. **The minimal-orbit cube gauge.** Balaban's CMP 102b Theorem 1, (7)–(9), is stated in CA-I L35144–35199. Put \(r=R_1M_1\). For real datum with tests below \(\varepsilon_1<a_1\), a minimal configuration has a gauge on each admitted grid cube of side \(2m_*\) in its top-level units, provided \(m_*\) is a multiple of \(r\) and
   \[
       m_*<M(\varepsilon_1)=r a_1/\varepsilon_1.
   \]
   On that cube the potential and its first lattice differences are bounded by \(B_3m_*\varepsilon_1\), in those units. The concentric cube enlarged by \(2r\) on each side must remain in the relevant layer region. For the trivial nest of CMP 109 and CMP 116 this region is the whole torus. The constants precede the localization size \(M\). These are proved regularity conclusions of Balaban's theorem, not the uncalculated response estimates (189)–(190).
3. **The actual representative.** Frozen mu identifies the regular real minimizer, its axial representative, and the continued complex minimizer in the Lemma 4 windows. It supplies the nesting input read at CA-I L33602–33698, with the corrected gauge order recorded in mu §6. Its smallness ceilings are retained. The present gauge clause is invariant under real changes of representative and needs no estimate on that axial gauge. A complex near product is checked on its exhibited representative over \(U=1\), as below.

The statements in items 1–2 were also checked against the supplied OCR: CMP 98 pp.25–26; CMP 102b p.279, with its regularity proof in §F, pp.300–304; and CMP 109 pp.260–263. Damaged OCR is not an exact formula source. The legible account statements above fix the formulas being ported. These published inputs remain inputs of the port; this note does not claim to independently rebuild their full proofs.

## 3. Constants in the account's order

First fix \(d=4,G=SU(N)\) and the early numerical data. Choose odd \(L\) with the account's floors, including
\[
 cL\ge2,\qquad L\ge2(1+\beta),\qquad
 L\ge2\sqrt2(1+\beta)(1+\beta_0).                              \tag{3}
\]
For the volume comparison below also include \(2L^{10}\ge3c\). This floor reads only the fixed cube-size multiple. All these are allowed early floors under CA-I L1400–1415.

Next fix \(R_1,M_1,a_1,B_3,c_{98}\) and the other published gauge constants. Keep the choice \(B=B_{12}\) in CA-I L37914–37919. In particular
\[
                         B\ge2B_3.                            \tag{4}
\]
The maximum there also pays for the other thin-cube branches. Its other entries are fixed before \(M\); none is chosen from a pair's radius. There is no need to enlarge \(B\) during a step.

Choose \(M=L^{m'}\) with the existing floors. The joint thin-cube choice \(M\ge\max\{80,7LR_1M_1\}\) suffices here. We only need
\[
                         M\ge4r,\qquad S\ge4r.                \tag{5}
\]
After these choices, require each real background's printed regularity radius \(\varepsilon_0\) to satisfy
\[
 0<\varepsilon_0<c_{98},\qquad
 2\varepsilon_0<a_1,\qquad 2S\varepsilon_0\le r a_1.            \tag{6}
\]
These are the averaging ceiling and the two ceilings in §4.9's real-background argument, with strict room at \(a_1\). They specify its sufficiently-small radius. They do not replace \(\varepsilon_0\) in the conclusion by a larger radius. The radius may be arbitrarily smaller than these ceilings. When the consumer requests membership at \(\alpha_0\), retain its separate requirement \(2B_3\varepsilon_0\le\alpha_0\) (CA-I L34058–34065, L36830–36835).

Retain the amplitude order and ceilings in mu §8 and CA-I L34745–34883: the amplitude choices follow \(L,B,M\); choose \(\alpha_1,\alpha_0,\alpha_3,\alpha_2\) in that order, with their printed comparisons. The additional bounds (6) are upper bounds by earlier constants. At running radii impose them through the common coupling ceiling. This is possible uniformly in the level: for fixed \(C,q>0\), the schedules \(Cg(\log g^{-2})^q\) tend to zero as \(g\downarrow0\). For the positive integer exponents here, put \(t=\log g^{-2}\); the term of degree \(2q\) in \(e^{t/2}\) gives
\[
  t^q e^{-t/2}\le (2q)!2^{2q}t^{-q}\longrightarrow0.
\]
Thus one ceiling covers the finitely many required amplitude bounds for every \(g_i\le\gamma\). No radius ratio is used to choose \(B\) or \(M\).

Finally require the torus side in the units of every reached level to be at least \(3S\), as in CA-I L36536–36538. This is supplied by H5 with the early floor above. Indeed \(R(g')\ge1\) by its definition (CA-I L667–669), and for \(0\le j\le K\),
\[
 \operatorname{side}_j(T)=2L^{m+K-j}\ge2L^m
 \ge2L^{11}MR(g_-(g))\ge3cLM=3S.                            \tag{7}
\]
Here H1 and H5 are CA-I L1131–1134 and L1169–1175. The argument does not assume a bound on \(K\). In the joint induction it applies to every proposed step with \(k+1\le K\); it does not prove first passage exists. All volume choices follow the coupling choices, as in Stage 9 (CA-I L1695–1703).

The extra conditions have the account's allowed directions: early floors, then amplitude ceilings, then a volume floor. They impose no upper bound on a block size or depth and no lower bound on a coupling.

## 4. Port of the own-constant proof

### 4.1 Small pairs

For the unit pair use \(U=1,U'=1\). For a small pair \((e^{i\xi_j\mathsf Z},J(e^{i\xi_j\mathsf Z}))\), where \(\mathsf Z\) is \(\mathfrak g^c\)-valued, use
\[
                         U=1,\qquad U'=e^{i\xi_j\mathsf Z}.   \tag{8}
\]
The printed small-pair bounds concern the whole \(\mathsf Z\), even if \(\mathsf Z\) is real; see CA-I L35956–35973 and L36840–36851. Thus this is the exhibited admissible decomposition. For every \(Q\), take \(u_Q=1,A_Q=0\). Both strict inequalities in (2) hold for every positive \(a\), hence for the pair's exact printed \(\alpha_0'\).

A small perturbation of an existing representative \(W=U'_WU_W\) has the other printed form
\[
 W e^{i\xi_j\mathsf Z}
   =\bigl(U'_W e^{i\xi_j\operatorname{Ad}_{U_W}\mathsf Z}\bigr)U_W. \tag{9}
\]
This is a bondwise matrix identity. Its unitary factor is \(U_W\), with its unchanged gauge clause. It is a transport case. The current increment does not enter (2).

### 4.2 Real backgrounds, including cubes thin in \(X\)

Let \(U=U_k(V)\in\mathfrak U_k(\varepsilon_0)\) be the printed real background. It is defined on the whole torus. Apply input 1 with \(a=\varepsilon_0\). Its datum has tests below \(\varepsilon_1=2\varepsilon_0<a_1\). Input 2 applies to its minimal orbit. The actual minimizer is that orbit, with the representative convention fixed by mu where needed. Real gauge changes do not change the existence or bounds of a local gauge.

Work in level-\(k\) units and let \(Q\subset X\) have side \(0<s\le S\). The following is the enclosing-cube argument of CA-I L36651–36699, ported without changing its radius. Put
\[
 m_*:=r\left\lceil\frac{s+2M_1}{2r}\right\rceil.              \tag{10}
\]
In each coordinate the smallest interval of the \(M_1\)-grid containing the corresponding interval of \(Q\) has length at most \(s+2M_1\). Extend it by grid intervals to length \(2m_*\). Their product is a grid cube \(Q^a\supset Q\). Since \(r\ge M_1\),
\[
 m_*<\frac{s}{2}+M_1+r\le\frac{s}{2}+2r\le S
       \le\frac{ra_1}{2\varepsilon_0}=M(\varepsilon_1).        \tag{11}
\]
The concentric enlargement of \(Q^a\) by \(2r\) on each side has side
\[
                     2m_*+4r<s+8r\le3S.                     \tag{12}
\]
It embeds in the torus by (7). At the top index of the trivial nest, \(B^k(\Lambda_k)=T\) and the next layer is empty. Thus the enlargement lies in the required layer union and is not contained in the next layer. This verifies both layer conditions of the minimal-orbit theorem, in addition to the grid and size conditions. There is no requirement that this enlargement lie in \(X\).

Input 2 supplies a gauge on \(Q^a\), defined also on a neighbourhood, with
\[
 |A|,\ |\nabla^{\xi_k}A|
   <2B_3m_*\varepsilon_0
   <2B_3(s/2+2r)\varepsilon_0
   \le2B_3S\varepsilon_0
   \le SB\varepsilon_0.                                      \tag{13}
\]
Restrict the gauge and potential to \(Q\). Every bond and parallel adjacent pair required in (2) remains among those already controlled. Equation (13) includes all directions of the ordinary first difference. This proves (2) at
\[
                            \alpha_0'=\varepsilon_0.          \tag{14}
\]
A zero-side cube is harmless. The proof works for arbitrary closed \(X\subset T\), with holes or thin parts. The collar belongs to the ambient torus, where \(U_k(V)\) exists. It is not obtained by extending a field known only on \(X\).

### 4.3 The exact constant after changing level

Let \(1\le j\le k\), \(\mu=L^{-(k-j)}\le1\), and let \(Q\subset X\) have side at most \(S\) in level-\(j\) units. Its side in level-\(k\) units is at most \(\mu S\le S\), so (13) applies. Keep its gauge and set \(A_j=\mu A_k\). Then
\[
 \xi_k=\mu\xi_j,\qquad
 e^{i\xi_k A_k}=e^{i\xi_j A_j},\qquad
 |A_j|<\mu SB\varepsilon_0,
\]
\[
 \xi_j^{-1}|\Delta_\nu A_j|
   =\mu^2\xi_k^{-1}|\Delta_\nu A_k|
   <\mu^2SB\varepsilon_0\le\mu SB\varepsilon_0.               \tag{15}
\]
Thus the single bound is \(SB\alpha_0'\) with
\[
                      \alpha_0'=\mu\varepsilon_0.             \tag{16}
\]
This is the printed lower-level radius in CA-I L36824–36826 and L36873–36886. The potential scales with one power, even though its difference scales with two. These arguments reproduce the proof of the corollary 4.9:cor-printed-pairs for the target's pair classes.

## 5. One-step reproduction on the account's Route

The step needs transport, new seeds, and one common constant; this is its explicit definition of reproduction, CA-I L35380–35441. We port the proof for CMP 109 §§3–5 and CMP 116 §§1–2.

Here are the elementary transport facts, including the gradient member.

* **Restriction and increasing the radius.** Restrict \(u,A\) and the lists of bonds and adjacent pairs. A strict bound below \(SBa\) remains strict below \(SBa'\) when \(a'\ge a\).
* **Descending a level.** For \(i'\le i\), a target cube has side at most \(SL^{i'}\le SL^i\). Apply the source clause there and repeat (15), with \(\mu=L^{-(i-i')}\). The delivered radius is exactly \(\mu a\).
* **Real gauge change.** If \(U^u=e^{i\xi A}\), then \((U^v)^{uv^{-1}}=U^u\). The same \(A\) and its same differences work. This uses the left gauge action also checked in mu §6.
* **Identity factor.** Equation (8) gives the clause at every positive radius. A complex gauge transformation is dealt with by retaining this exhibited representative of the orbit. It is not applied to the real factor as if it were unitary.

These are Lemma 4.9:lem-unitary-moves, CA-I L35842–35893. Their application to the actual step is the following table. The source representatives and radius comparisons are CA-I L35908–36072, L36117–36216; the six memberships being served are L34241–34304.

| Place in the step | Exhibited real factor and gauge proof |
|---|---|
| Near incoming window | Reads the tower condition. It does not create a new gauge factor. |
| Near product, CMP 109 (3.24), (3.53) | The representative is the Landau copy \(\mathcal U=e^{i\xi_jH_j}\), over \(U=1\). Mu supplies the actual minimizer/nesting identification used to obtain that representative. Equation (8) proves its gauge clause. |
| Far incoming restriction from \(k+1\) to \(j\le k\) | Keep \(U\). Its source radius \((1+\beta)\alpha_0\) becomes \(\mu(1+\beta)\alpha_0\le\alpha_0/2\), by (3). |
| Far product \(e^{i\xi_jA}\mathbf U=e^{i\xi_jA''}U\) | Keep \(U\). Its radius \(\alpha_0/2\) fits the target \(\alpha_0\). The factorization is in Proposition 4.8:prop-far-case, CA-I L33839–33892; its other conclusions retain their own premises. |
| Two far-type terms, CMP 109 (3.21)–(3.22) | Use the representative \(e^{i\xi A^\sharp}\mathcal U\) over \(U=1\), as in CA-I L35946–35953. |
| Kernels at \((1,0)\), and absolute small pairs | Equation (8). |
| Small perturbations about an admitted pair | Equation (9); the original unitary factor and gauge radius persist. |
| True real backgrounds | Equations (13)–(16), at their printed radius. |
| Domain change \(Y\subset X\) at level \(k+1\) | Restrict the same gauges; the target radius \((1+\beta)\alpha_0\) is at least \(\alpha_0\). |
| Old-term product string in CMP 116 | The entire twist is in \(U'\); \(U\) is unchanged. Restrict and descend. The running-radius comparison below applies. |
| The real point \((U,0)\), and the operator's glued complex background | Their exhibited unitary factor is the same \(U\). They use the same cube gauges; the operator's other admission conditions remain separate. |

There is no loss from the inner substitution \(M\mapsto M/L,\ B\mapsto LB\). Its requested cubes are smaller and
\[
               cL(M/L)(LB)\,\mu a=SB\,\mu a.                 \tag{17}
\]
The apparently different constants give exactly the same bound. This is the substitution used at CA-I L34119–34138 and L36142–36152.

For completeness, in the running version retain the already-reached flow hypotheses of Lemma 4.4:lem-radii-ratio (CA-I L10224–10260). That proved implication gives
\[
 \frac{\alpha_{0,i}}{\alpha_{0,i'}}
     \le(1+\beta_0)\sqrt{1+n},\qquad n=i-i'\ge1.
\]
Thus the transported enlarged radius obeys
\[
 \frac{(1+\beta)\mu\alpha_{0,i}}{\alpha_{0,i'}}
 \le(1+\beta)(1+\beta_0)\sqrt{1+n}\,L^{-n}\le\frac12.          \tag{18}
\]
To check the last inequality by hand, \(\sqrt{1+n}\le\sqrt2 L^{n-1}\): it is equality at \(n=1\), and the ratio on incrementing \(n\) is at most \(\sqrt{3/2}\le L\). Now use (3). This proves the comparison for every gap. It does not assume that the full flow theorem has already been proved at future steps.

At the new level \(k+1\), the newly admitted real background is \(U_{k+1}(V)\in\mathfrak U_{k+1}(\varepsilon_0)\). Apply §4.2 at that level. Its geometry is again the trivial nest; (6) is unchanged and (7) holds in the new units. New absolute small pairs again use (8). The same \(B\) serves old arguments and new seeds. Repeating the four transport facts proves (2) throughout the step, at each argument's printed radius.

This is the seed and transport part of the proposed thin-cube Route. It proves the own-constant lemma's assertion for the cited small-field one-step analysis. Section 4.9's later branches involving CMP 119/122 nest cubes, gluing and large-field stage backgrounds retain their separate hypotheses. This note does not infer admission of a re-minimized CMP 122b representative from preservation of the old real factor. The account separates those constructions at L36242–36248 and L38108–38144.

## 6. Consumers and verification limits

The full literal-label search found no occurrence of 4.13:lem-own-constant outside its declaration in CA-I. The content searches located the following uses and standing declarations; each cited source range was read.

| Source | What the result supplies |
|---|---|
| CA-I L34058–34100, L34194–34208, Proposition 4.8:prop-small-pairs | The widened real-factor gauge premise at \(\alpha_0'\), including true backgrounds. The separate \(2B_3\alpha_0'\le\alpha_0\) requirement and complex tower estimate (1.17) are unchanged. |
| CA-I L34241–34304, Proposition 4.8:prop-class-reproduction | The gauge component of the displayed six memberships, especially the small and true background clause (e). It does not supply all other hypotheses of this proposition. |
| CA-I L35380–35441, L36806–36906 | Seeds at their own radius, transport, and a common \(B_{12}\). These passages already state the exact content being ported. |
| CA-I L37902–38100 | The trivial-nest seed clause in the thin-cube theorem and its four elementary transport moves. The theorem's other branch hypotheses remain inputs to those branches. |
| CA-I L45203–45234 | The target lemma and its Route. Equations (13), (16) give its exact bound; §5 gives one-step reproduction in its cited analysis. |
| CA-I L56419–56437, hypothesis (a′) of Proposition 4.19:prop-clause-zero | The own-constant small-pair/real-background part of widened reproduction. The complete hypothesis also reads the other branches of §4.9. This note does not prove all of clause (0). |
| CA-I L166622–166623; CA-III L111213–111214 | Lists retaining the missing-proof declaration. These are source standing, not further mathematical uses. They were not edited. |

The successful mechanism is already in the account: use the ambient minimal background to surround a thin cube, apply Balaban's gradient theorem, and restrict the gauge. Curvature alone on a thin \(X\) is not used to derive the gradient. Neither a pivot chart nor uniqueness alone would supply it. The earlier conditional corollary becomes the target in the account's setting once (4)–(7) and the printed representatives are matched. The later missing-proof label does not show that this earlier proof is absent.

All checks here are written mathematical checks: the enclosing-cube inequalities, the strict gauge bound, the two powers in (15), the factor order, the exact identity (17), and the order of constants. No numerical experiment, enumeration, solver, or computer algebra was used. Shell tools served source navigation, source identities and file editing only. The proof retains the published inputs in §2 and the frozen mu result; it is not an independent verification of their full dependency chains. Only the output file library/oc.md was edited. No prompt, audit, ledger or platform instruction was changed.

## Result

**Proof**

In the setting and order of constants of the complete account, the small pairs and real-background pairs whose membership is printed in CMP 109 §§3–5 and CMP 116 §§1–2 satisfy the widened CMP 109 (1.12) at their own printed curvature constant \(\alpha_0'\). On every closed cube contained in their domain, of side at most \(c_\square LM\) in that level's units, there is a real gauge with
\[
              |A|,\ |\nabla A|<c_\square LMB\alpha_0'.
\]
One and the same \(B=B_{12}\), chosen before \(M\), serves all such pairs and the next renormalization step. For a real \(U_k(V)\in\mathfrak U_k(\varepsilon_0)\), the printed radii are \(\varepsilon_0\) at level \(k\) and \(L^{-(k-j)}\varepsilon_0\) at level \(j\le k\). The standing smallness and volume requirements are (3)–(7). Sections 4–5 prove the assertion, including thin cubes and the gradient member, by porting the account's §4.9 and using frozen mu for the actual minimizer identification. This proves CA-I 4.13:lem-own-constant in its stated one-step setting; it is not a new proof of Balaban's gauge theorem or a proof of the remaining T0 obligations. \(\square\)

## Change log (freeze, 2026-11-05)

Written by Codex. Refereed line by line by a fresh Claude session ([oc-gate](../gates/oc-gate.md)): first failing step none; proved as stated and used, in the account's setting and order of constants, with (3)–(7) explicit.

Recorded by the lead (Claude):
1. At a lower level \(j\) the constant is \(\mu\varepsilon_0\) (the account's one-power reading); consumers use \(U_j\) at its own level.
2. §4.2's sentence crediting mu with identifying the global \(U_k(V)\) overreaches: that identification is CMP 109's notation (CA-I 36687–36688), and the gauge condition needs no representative. mu is otherwise used only as proved.
3. (18) holds with \(\beta\) at the product-string locus it serves; the running far-source case (with \(\beta_s\)) is a CMP 119 standing condition outside the lemma.
4. The extra ceiling \(\varepsilon_0<c_{98}\) is in the allowed direction; (7) derives a torus-side condition the account only assumes.

Their text: the label 4.13:lem-own-constant ("Proof outstanding", CA-I 45203) is stale in substance. Their Corollary 4.9:cor-printed-pairs states the content almost word for word, conditional on \(B_{12}\ge2B_3\) and Proposition 4.9:prop-real-backgrounds (a), which Lemma 4.9:lem-thin-cube-gradient (ii)–(iii) supplies in a valid order. No circularity: the chain rests on Balaban CMP 102b Theorem 1 (9), CMP 98 Proposition 2 and elementary §4.9 lemmas; the only inductive link (Lemma 4.4:lem-radii-ratio) is the normal joint induction.

Status: **frozen.**
