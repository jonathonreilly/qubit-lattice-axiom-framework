# P5 induction port: one line-by-line check

First failing step: none.

Target: `library/port/p5-induction.md` (826 lines), Codex port of CA-I rows A5, A6 (two statements), A12, A13 (two statements). Source read: `sa/ca_I.tex` (166,711 lines) at the stated ranges, plus the loci each cited input points to. One reading, not a hostile review. Nothing outside this file was edited.

## A5 — 4.6:prop-large-field-bound (port L17–132; CA-I 22860–23036)

- Statement (L24–72): matches CA-I 22860–22908 word for word, labels included. Strip length \(d_{k,\cup Y_i^\sharp}\) kept as printed.
- (a) (L94–99): the bound of P5-H-log with \(d_{\rm out}=d_{k,\cup Y_i^\sharp}\). Same as 22920–22932.
- (b) (L101–117): \(Y_i^\sharp\subset Y_i^\boxplus\subset(Z_k\cup\bigcup Y_j)^\boxplus\); then \(c_1=e^{-p_0}\), core \(X=X\), \(d_{\rm out}\ge d_k\). Island \(X_a\subset X_a^\sharp\subset P\subset X\); \(\check R_k^d\) cubes; tree-cube lemma gives \(d_k\ge5^{-d}\check R_k^d-1\); condition (f) gives \(\log K_{\rm KP}\le\frac12\beta\kappa d_k\); absorption. Every step agrees with 22933–22977.
- A5-F1 (L107): the \(\epsilon\) version replaces "a shortest tree realising \(d_k(X)\)". Correct. On a lattice the infimum is attained anyway; the fill does no harm.
- (c) (L119–126): \((1,0)\) in the domain by the real-slice statement (22980–22984); triangle inequality gives factor 2; with \(2K_{\rm KP}\) in (f), the same absorption. Agrees with 22979–23006. A5-F2 (term-by-term subtraction on the finite system) is correct and does not subtract before the logarithm.
- (d) (L128–132): single activity analytic and local; uniform limit of holomorphic functions. Agrees with 23008–23036. A5-F3 (Cauchy formula interchanged with the compact \(t\)-integral) is correct.
- Inputs: P5-H-real-slice and P5-H-locality are used by the source proof but are not in its hypothesis list. The port names both. That is correct.
- Naming gap (not a failing step). CA-I 23092–23120, `4.6:rem-widened-support`, is marked "Proof outstanding". At 23177–23178 the account says this statement "enters only through the estimates from which its inputs are drawn", that is, through the standing bounds (a),(b) of `4.6:def-standing-bounds` on the cell-made family. The port assumes those bounds (P5-H-standing), so the implication holds. But the port does not name this open supplier. The repository library does not name it either, and it is missing from the account's own open list at 166617–166624. It should join the open-input inventory (L746 onward), together with the own-cube-profile alternative (23139–23176), which the account says is complete but does not adopt.
- Verdict A5: faithful. Proved as an implication from its named hypotheses.

## A6.1 — 4.7:prop-beta-extraction (port L135–293; CA-I 32226–32410)

- Statement (L142–205): matches 32226–32289 word for word, (A1)–(A4) and both displays included.
- Reduction (L226–241): composition via CMP 109 (4.2), chain rule, the second term removed by CMP 109 (4.14). Same as 32291–32323. Both cited inputs are named (P5-H-compose, P5-H-stationary).
- Radii and norm (L243–254): \(\rho_b=c_Tr_je^{\delta_0{\rm dist}(b,X)}/(2C_{\mathsf h})\); the triangle inequality gives \(N_j(\cdot\lceil X)\le c_Tr_j\). Agrees with 32336–32346. Minor point: the source applies (A2) to a bound on the restriction \(\cdot\lceil X\), and (A2) is stated for \(N_j(\mathsf Z)\). Locality of the kernel on \(X\) with its collar closes that gap. The port says this in one clause ("Locality, the prescribed local norm (including its required collar)"). It is correct, but it is not a named input.
- A6-F1 (L256–266): interior bidisc \(u<1\), then \(u\uparrow1\); \(|\partial_s\partial_tf(0,0)|\le\sup|f|/(\rho_b\rho_{b'})\). That gives the printed prefactor \(4C_{\mathsf h}^2S_j/(c_Tr_j)^2\). The case \(b=b'\) is handled correctly.
- (A4) step (L268–272): matches 32362–32371.
- **A6-C1 (L274) is a real correction.** CA-I 32383 attributes \((\log g_j^{-2})^q\ge1\) to \((\Gamma4f)\). The printed (f) at 31823 is \(\bigl(1+(C_\beta+1)\gamma^2/\log\gamma^{-2}\bigr)^q\le2\), a ratio bound. Both repairs are valid. (e) \(\gamma\le e^{-q}\) together with \(g_j\le\gamma\) gives \(\log g_j^{-2}\ge2q\ge1\); CA-I 1365 and 10282 confirm that \(q_0,q_1\) are integers greater than 1. Also \(\gamma\le\frac12\) (CA-I 1726) gives \(\log g_j^{-2}\ge\log4>1\) for every \(q>0\). The constants do not change.
- A6-F2, A6-F3 (L276–293): the arithmetic is right. \(r_j=c_*g_j(\log g_j^{-2})^q\) with \(c_*=\min\{C_0,C_1\}\) (CA-I 29084–29090). \(g_k\le\gamma\le1\) and \(\kappa_0-7>0\). The last ceiling \(\gamma\le[\min\{c_0/4,1\}/C']^{1/(\kappa_0-8)}\) gives \(\bar\varsigma\le\min\{c_0/4,1\}\) with no circularity, as at 32405–32409.
- **Unrooted (A4) sum: a real issue in their text.** The display at 32256–32258, \(\sum_X(Md_j(X)+c)^2e^{-\kappa d_j(X)}\le C_A\), has no anchor. \(C_A\) appears only at 32255–32369, and no convention fixes the sum. Over \(\mathbb Z^4\), every translate of a single \(M\)-cube has \(d_j=0\) and contributes \(c^2\), so the sum as printed diverges. The weight \(e^{-\delta_0[{\rm dist}(b,X)+{\rm dist}(b',X)]}\) in the premise is presumably meant to supply the anchor. The port is right to record this as unresolved inside P5-H-moment and not to repair it.
- Verdict A6.1: faithful, with correction A6-C1. Proved as an implication from (A1)–(A4), composition and first variation. (A4) cannot be used as printed until its summation is fixed.

## A6.2 — 4.7:prop-coupling-increment (port L296–414; CA-I 32412–32496)

- Statement (L303–349): matches 32412–32458 word for word.
- **Missing (A4): a real issue in their text, correctly caught.** The second bullet of the statement assumes only (A3) of the extraction proposition. The proof of (b) (32464–32466) invokes that proposition, which also needs (A4); (A1) and (A2) come from the corollary and the true-pair statement, which are listed. The port carries (A4) explicitly (L368).
- (a) (L374–376): marked/unmarked theorem (a) plus linearity. Like the source, no existence or site-freeness claim at the new site.
- (c) (L378–407): A6-F5 checked against CA-I 29522–29528. The reference index \(i+1\) gives \(\eta=L^{-i}\) and \(\ell_i=1\). The difference bounds (1, 2, \(4d\), \(8(d-1)\) times powers of \(h^{-1}\)) are right, and their maximum is \(\le8dh^{-3}\|A\|_\infty\). A6-F6: \(c_T\le1/8\) (29532–29535) and \(r_i=\alpha_{0,i}\) (29088–29093) give \(a\le r_i/(64d)\le\alpha_{0,i}\). The step "replace the true current by an independent current" is the source's own reading of the class (second condition of (1.14)). It is kept as stipulated.
- A6-F4 ordering (L372): consistent with the source, where (b) is proved from the corollary at \(k+1\) and then extraction.
- (b) (L409–414): same as 32464–32470.
- Γ6(vi): the statement says the member "carries the factor \(86d\)", and the printed (vi) at 31836 has \(172d\). The port reads this as a margin of 2. No step depends on it.
- Verdict A6.2: faithful. Proved as an implication, with (A4) correctly added to the carried inputs.

## A12 — 4.19:prop-clause-zero (port L417–561; CA-I 56419–56524)

- Statement (L424–465): matches 56419–56460 word for word, (a), (a′), (b)–(h) and the prefix-representation hypothesis included.
- **One-loop status discrepancy: a real issue in their text.** Under the convention at CA-I 27–46, the heading of `4.2:lem-one-loop` (3901–3903) is in the "citation with its locus" form, and 3930–3931 says "used here as stated in" CMP 109 (1.22), Theorem 3 and CMP 116 (2.41). The lemma has no step marked \((\ast)\): the only \((\ast)\) marks in 3880–4080 belong to `4.2:lem-unmarked` (4032, 4072). The account's own open list at 166617–166624 names lem-unmarked but not lem-one-loop. Yet A12 (b) (56433–56435), its proof (56466–56467) and the flow-bounds remark (56361) all call the one-loop lemma "proof incomplete at one step". Part (b) of the lemma is also an outline (3949 onward) that rests on a comparison \(|B_k-B_k^{\rm ref}|\le\frac12C_{\rm cmp}\) and on a lattice determinant computation, both asserted at 3967–3988. The port is right to carry P5-H-loop as an open, named input.
- Step 1 and A12-F1 (L500–504): the order prefix → stand-in families → coefficient → \(x_n\) matches 56462–56484. `4.38:thm-torus-independence` (58219–58275) confirms that \((H_j)\)(a)–(c\(^+\)) concern levels below \(j\) and that (d) uses the stand-in \(\tilde g=g_{j-1}\).
- Step 2 (L506–523): the one-loop telescoping matches 56361–56368 and `4.19:lem-flow-bounds` (56342–56399), which is in checked p1. The constants \(\lambda_\sharp,B_\sharp,c_5,g_-\) and \(c_0=11N^2\log L/(12\pi^2)\) match `1.2:def-flow-constants` and 3897–3899.
- Step 3 and A12-F2 (L525–546): checked in full. \(K=\min\{k:x_k\le h+B\}\) as at CA-I 667. Finiteness comes from the lower drift and the Archimedean property. For \(K>0\): \(x_K\ge x_{K-1}-B>h\). \(K=0\) exactly when \(t=h+B\). The bounds \(K\ge(t-h)/B-1\) and \(K\le1+(t-h-B+c_5)/\lambda\) are right. \(\gamma_H^{-2}\ge\gamma^{-2}+c_5+1\) is H3 (1159–1162), as the port says.
- A12-F3 (L554–559): the direct derivation of \(\check R_K\le R(g_-(g))\) is correct. By `4.15:not-cube-sizes`, \(\check R_K\) is the least \(L^b\ge(\log\check x_K)^r\), with \(1<\check x_K\le x_K\le g_-^{-2}\). This avoids the "(H1)–(H7)" citation at 57123. \(\check R_i\le L^{K-i}\check R_K\) is correctly kept as the named cell-comparison input; monotonicity gives only the opposite direction.
- A12-F4 (L561): finite induction on equality of the two sequences. Correct.
- Verdict A12: faithful. Proved as an implication from every hypothesis (a)–(h), H1–H6, the prefix representation and the second cell comparison. All of these are named in the port's table (L474–488).

### (a)–(h): current supplier

| Item | CA label | Supplier now |
|---|---|---|
| (a) | CMP 109 Theorem 3 | Published theorem, cited. No repository proof. Open as a repository result. |
| (a′) | widened CMP 109 (1.12) and its one-step reproduction | Partly supplied: frozen [oc](../library/oc.md) supplies the seed part (small pairs and real backgrounds at their own constant, common \(B_{12}\), one-step reproduction). Its §6 says the full hypothesis also reads the other §4.9 branches (the transport clause (a) of 35392–35408 at every derived membership). That remainder is open. |
| (b) | `4.2:lem-one-loop`, `4.2:lem-unmarked` | Open, both. P3 (free-field algebra) does not supply either. The status discrepancy of the one-loop lemma is recorded above. |
| (c) | `4.7:prop-coupling-increment` | This port, A6.2: a conditional implication. Its inputs P5-H-E (`4.7:cor-kernel-power-bound`), (A3), (A4) with its unrooted sum, and P5-H-membership/1.17 are open. |
| (d) | `4.4:cor-localised-independence` | Checked p4 (A3). Its input `4.4:prop-local-real-base` comes from frozen lrb, on lrb's premises (a)–(d) and CMP 116 (2.14). Supplied conditionally. |
| (e) | `4.5:thm-operator-bounds` | Checked p4 (A4, with repairs). `4.5:lem-uniform-increment` comes from checked ui. p4's retained Balaban frontier remains. Supplied conditionally. |
| (f) | `4.6:prop-large-field-bound` | This port, A5: a conditional implication. `4.6:prop-logarithm-convergence` is in checked p1. Activity supplier, format, prepared sequences, positivity dichotomy (outstanding, 166624), standing bounds (through the outstanding `4.6:rem-widened-support`), common domain, real slice and locality: all open. |
| (g) | one-power hereditary class (`4.8:def-one-power-class`, `4.8:prop-class-reproduction`) | Partly supplied: frozen mu (minimizer uniqueness and locality) and frozen oc (gauge component). Restriction/near membership, nesting at the use radii, and CMP 109 (1.17) at complex pairs: open. |
| (h) | `4.38:thm-torus-independence` | Open. Not ported; its seven hypotheses are named in the port (L486). |

## A13.1 — 4.19:prop-containment (port L564–601; CA-I 56530–56566)

- Statement: matches 56530–56547. The proof (L595–599) matches 56549–56566. A13-F1 (\(K=0\) gives \(g_0=g_-(g)<g\)) is correct. CMP 122b Theorem 1 is kept as a cited theorem; only its coupling hypothesis is checked.
- Verdict: faithful. Proved as an implication from A12, H4 and H3.

## A13.2 — 4.19:cor-windows (port L604–671; CA-I 56568–56630)

- Statement: matches 56568–56582. The window inequality (L634–648) matches 56584–56607.
- A13-F2: integer depth is implicit in the source. Correct.
- A13-F3: bisection compactness. Correct.
- A13-F4: the diagonal \(i_n=J_n(n)\) is strictly increasing because \(J_{n+1}(n+1)\ge J_n(n+1)>J_n(n)\). The bound \(|x^{-1/2}-y^{-1/2}|\le|x-y|/(2g^{-3})\) holds on \(I_s\). Both correct, and both fill steps that 56609–56629 states briefly.
- Verdict: faithful. Proved as an implication from A12.

## Frontier and standing (port L674–826)

- Spot-checked the P5-P01–P5-P16 bundles against CA-I 166579–166613: each matches in Balaban locus and content. The positivity dichotomy is listed as outstanding at 166624, as the port says.
- **Standing stale (no proof effect).** The port credits [oc](../library/oc.md) as "being refereed" (L11, L478, L761, L824) and p3/p4 as plain "ports". At this checkout oc is **frozen** (oc-gate), and p3-free and p4-operator are **checked ports** (p3-free-gate, p4-operator-gate). The port was written at baseline c86830eb5, and these lines should be updated.
- Missing open input: `4.6:rem-widened-support` (proof outstanding, CA-I 23092–23120), as recorded under A5.

## Result

First failing step: none. All six statements match the source word for word. Each proof follows the source route; every filled step (A5-F1..F3, A6-F1..F6, A12-F1..F4, A13-F1..F4) is correct; correction A6-C1 is correct. Both recorded input issues are real in their text: the one-loop status discrepancy, and the unrooted (A4) sum, which diverges as printed. Three additions, none of which changes a proof: (1) name `4.6:rem-widened-support` as the open supplier behind P5-H-standing; (2) update the standing of oc (frozen) and of p3/p4 (checked); (3) optionally name kernel locality with its collar as the input that moves (A2) from \(N_j(\cdot\lceil X)\) to the class (A6.1). Verdict: all six statements faithful as conditional implications.

Checked line by line by Claude (fresh session).
