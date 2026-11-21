lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T18:12Z

First failing step: mu-radii.md lines 349–353 (§3, the constant $C_Q$). The step misquotes CA-II 35666. It is minor and repaired below (defect 1). No conclusion changes. No other step fails, and the counterexample (21)–(22) and the identities (14), (19), (20) are correct.

# mur-gate: referee of library/mu-radii.md (row 357)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 76a08cb5d. One line-by-line check of `library/mu-radii.md` (Codex, 912 lines), not an audit. Kind: check of our own new text, including a claimed correction of their text. Sources read at commit 31a47c543775, each fetched by URL, with SHA-256 matching the note's §6: CA-I (4cb5cb5e…6e93, 166,711 lines), CA-II (6a1f74b0…2b8f, 145,624 lines) and CA-III (7e36523b…352d, 111,583 lines), all at the lines named below. Bałaban: CMP 109 printed pp. 277–278 (page images rendered from the owner's copy); CMP 102b (277–309) §A and §G, CMP 99a p. 80, CMP 99b (3.21) and CMP 98 Proposition 6 (OCR text). Source authors: Ethan Sussman and Levent Alpoge, with Claude and Codex. The gauge constructions are Tadeusz Bałaban's.

## Verdicts

| Statement in mu-radii.md | Verdict |
|---|---|
| (21)–(22): the block-constant gauge of CA-I 154354–154376, (a) and (c), is false | ADVANCE. Correct; this is a correction of their text (§2 below) |
| (3), (14): corrected relative-gauge identity for (a) on the whole (N1) path | ADVANCE, as an implication (§3) |
| (16)–(19): corrected identity for (c) on every $X$, including wrapping $X$ | ADVANCE, as an implication (§3) |
| (20): the (N2) equality of $f$ values | ADVANCE, as an implication (§3) |
| §2, (4)–(8): stage near pairs, §§4.26 and 4.28 | ADVANCE (read line by line; citations spot-checked, about twenty not traced, §4) |
| §3, (9)–(12): CA-II 35714 | ADVANCE after the repair of defect 1 |
| §5, (23)–(29): CA-II 44422 and 44454 | ADVANCE (§4) |
| Result items 3 and 4 (not covered) | CORRECT-NO-ADVANCE; these are honest non-claims |

## 1. Source check of the claimed defect

These are the quoted passages that decide the counterexample. Each was read in full.

**S1. Their statement (a), CA-I 154354–154376.** "Each $\bar u$ below is a genuine $G^{\mathbb C}$-valued lattice gauge transformation $x\mapsto\bar u(x)$ which is constant on each block." Line (a) reads $U_n(X,M^n\mathbf U[D])=\mathbf U[D]^{\bar u^{-1}}$ on $X^{\sim-2}$, with $|\bar u^{\pm1}|\le1+c_u\beta$. Line (c) is the same with $W$ in place of $\mathbf U[D]$. CA-I 154419–154425 says the identity "corresponding to (a) is [CMP109, (3.38)]" and quotes Bałaban: "…constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $U_j$ at centers of the blocks."

**S2. Bałaban's printed (3.37)–(3.38), CMP 109 pp. 277–278** (page images, not OCR). (3.37): $U_j(\square_0,\exp i\tau Q(\cdot))=(\exp i\xi\mathbf H_j(\square_0,\tau Q(\cdot)))^{u_j}$, $|u_j-1|<B_3^2O(1)M\alpha_0$. (3.38): $U_n(X,M^{\cdot}(\exp i\xi\mathbf H_j))=U_n(X,M^{\cdot}(U_j))^{(\bar u_j)^{-1}}=U_j^{(\bar u_j)^{-1}}=(\exp i\xi\mathbf H_j)^{u_j(\bar u_j)^{-1}}$, "where $\bar u_j$ is a gauge transformation constant on blocks … and equal to $u_j$ at centers of the blocks." So the printed gauge on the Landau field is $u_j(\bar u_j)^{-1}$. Only $\bar u_j$ is block-constant. The CA quote in S1 changes the lower-case $u_j$ (a gauge transformation) into $U_j$ (a configuration).

**S3. Their own §4.7, CA-I 29234–29239,** reads the same display correctly: "We set $g_{\langle3.38\rangle}:=u_j\bar u_j^{-1}$. Here $\bar u_j$ is … 'constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $u_j$ at centers of the blocks'." So the account itself carries the non-block-constant factor in §4.7 and drops it in §4.31.

**S4. Which representative is $\exp i\xi\mathbf H$.** CMP 102b §G, p. 305: "At first we fix the Landau gauge for the configuration $U_k(V'V_0)U_0^{-1}=U_1'$ and we have $U_1=\exp i\eta\mathcal H(B)$" (173). P. 307: "we transform the configuration in the Landau gauge back to the axial gauge". Proposition 9: "The function $U_k(V'V_0)U_k(V_0)^{-1}$ transformed to the Landau gauge is, by the definition, equal to $\exp i\eta\mathcal H(B)$." The Landau space is CMP 102b (19)–(21), p. 281, with (21) $R(U_0)D^*_{U_0}A=0$; Proposition 2 maps its critical configurations one-to-one to the axial ones by gauges $u$ normalised by block averages, $R_0u_j=1$ on $\Lambda_j$ ("thus $u=1$ on $\Lambda_0$"). CA-I 154193–154230 calls $\mathbf U[D]=e^{i\xi\mathcal H_j(\square_0;D,\mathbf 1)}$ "the local form of the construction of the complex background field", unique under "the normalisation of the global construction". CA-I 155098–155112 defines $W_{V_0}(B)=e^{i\eta\mathcal H(B;U_0)}U_0$ the same way. Neither passage names a gauge, so the cited construction fixes it: Landau.

**S5. Axial condition on the local minimiser.** CA-I 32896–32897: "$U_n^{\mathfrak r}(Z;\cdot)$ [is] the axial-gauge minimiser of the depth-$n$ problem". CA-I 130021–130052 (HBA): for every $m<n$ and every $(m+1)$-block $B'$ inside a structure block of level $>m$, $[M^mU](b)=1$ on every bond $b$ of the gauge tree $\mathcal T_m(B')$. At $m=0$ this is $U(b)=1$ on the fine tree bonds of each 1-block. CA-I 29240–29242: Bałaban's $n$ in (1.15)–(1.16) runs over $1,\dots,j$, so $n\ge1$ is allowed.

**S6. What the consumers read.** (N1) at CA-I 156008–156038 and (N3) at CA-I 155387–155429 use only $|\bar u^{-1}||\bar u|\le1.21$, the plaquette conjugation $U^h(\partial p)=h(x)U(\partial p)h(x)^{-1}$ (stated there for a general gauge $h$), and $|\operatorname{Ad}(\bar u^{-1})Y|\le|\bar u^{-1}||\bar u||Y|$. Block-constancy is not used. (N2) at CA-I 156045–156060 uses only equality of the values of $f$.

## 2. The counterexample (21)–(22), mu-radii lines 648–725

**Verdict: correct.** It refutes the block-constant requirement in (a) and (c) of CA-I 154354–154376 under the normalisation that their text cites. Each step was redone.

1. *Averages of (21) (lines 656–670).* The field is abelian and flat, so every transport between fixed endpoints is $e^{ia\Delta x_1T}$. Each block average is then the unitary value $e^{isaT}$, and no projection to $G$ changes it. Correct.
2. *Landau membership (lines 671–682, 692–697).* In Bałaban the Landau condition is $R(U_0)D^*_{U_0}A=0$, where $R$ is the orthogonal projection onto $\Delta_{U_0}N(Q')$ (CMP 99a p. 80; CMP 99b (3.21)). At base point $\mathbf 1$, $D^*A=0$ at every site whose incident bonds all lie in the box, because $A$ is constant. Every $\lambda\in N(Q')$ vanishes on the level-0 shell $\Lambda_0$, since there $Q'_0\lambda=\lambda$ (the linear form of "$u=1$ on $\Lambda_0$", CMP 102b p. 281). So $\Delta\lambda$ is supported within one site of $\Omega_1$, where $D^*A=0$. Hence $\langle D^*A,\Delta\lambda\rangle=0$ and $RD^*A=0$. The size bounds of CMP 102b (19) hold for small $|a|$ because all differences vanish. (20) holds by the choice of constraint value. $J=0$, so the field is critical; its action is zero, so it is the minimum. The note says this in one sentence ("zero lattice divergence on the variable region"). The detail above confirms it.
3. *Identification $\mathbf U[D_a]=\mathcal U_a$ (lines 698–703).* CMP 102b p. 281 (Proposition 2 and the text after it) gives exactly one critical configuration in the Landau space (19)–(21) for small data. CMP 102b p. 281 and p. 307 map it one-to-one to the axial minimiser by a normalised gauge. With S4, $\mathcal U_a$ is the CA's $\mathbf U[D_a]$. The note credits this uniqueness to "§G". It is stated in §A (p. 281), which §G reuses, so this is a citation detail only.
4. *The datum (lines 683–690).* Bałaban normalises the Landau-to-axial gauge by averages, $R_0u_j=1$ (CMP 99a p. 80; CMP 102b p. 281), not by root values. So the averages of $\mathcal U_a$ and of $W_a$ can differ by a coarse gauge. Defining $D_a$ from $W_a$ is the right care. The contradiction does not depend on it: $U_n(X,\cdot)$ is axial for every datum.
5. *Axiality of the inner minimiser (lines 705–706).* By S5, for every $n\ge1$, $U_n(X,M^n\mathbf U[D_a])(b)=1$ on every level-0 tree bond $b$ of a 1-block inside a structure block of level $\ge1$. A gauge tree spans the sites of its 1-block (CA-I 129550–129552), so it has a bond in direction 1. Both ends of that bond lie in the 1-block, and the 1-block lies in every larger block of the nested family (CA-I 129530 (B2), 129539 (c5)). Choose $X$ with $X^{\sim5}\subset\square_0$ large enough that $X^{\sim-2}$ meets the level-$\ge1$ region of the $X$-tower. Any block-constant $v$ then acts on $b$ by conjugation.
6. *(22).* $v e^{ihaT}v^{-1}=1$ would give $e^{ihaT}=1$, which is false for $0<|ha|<\pi$. Correct for both sign conventions.
7. *(c) (lines 717–725).* $V_0=\mathbf 1$ lies in $\mathcal V_s(w_s)$ and $U_k(\mathbf 1)=\mathbf 1$. A small constant real top datum $B$ in direction 1 gives the constant flat field. The torus has no boundary, so $D^*A=0$ everywhere. Fine and coarse readings share one lattice (CA-I 155274–155280), so the same tree-bond argument applies. Correct.

**Scope.** The refutation reads $\mathbf U[D]$ and $W$ as Bałaban's $\exp i\xi\mathbf H$, the Landau representative (S4). The CA's §4.31 never names a gauge. If the authors meant the axial representative, (a) and (c) could hold with $\bar u$ block-constant, but then every bound of CA-I 154193–154230 would have to be re-derived for the axial copy. The note says this (lines 457–458, 721–724). The internal evidence of S2 and S3 decides the question: their §4.7 already writes $g_{\langle3.38\rangle}=u_j\bar u_j^{-1}$, and the §4.31 quote changes $u_j$ to $U_j$. So this is a transcription error in their §4.31, not a reading we chose.

**Effect on their proof.** None. All three consumers (S6) read only norm bounds or values of $f$, and the corrected gauges satisfy those bounds ((14), (18), §3 below). So this is a correction of a statement, not of a theorem.

## 3. The corrected identities (14), (19), (20)

**(3) and (14), lines 31–111 and 448–517: correct, as an implication.**

- The setup matches CA-I 154193–154230: $\sup|D|\le\beta\le\beta_W$, $X^{\sim5}\subset\square_0$, the domain $X^{\sim-2}$, and $|\mathcal H_j|\le2C_{19}B_0\beta$ on $\square_0^{\sim-2}\supset X^{\sim3}$.
- The proof does not need the Landau reading. It needs three facts from CA-I 154193–154230: $\mathbf U[D]$ is holomorphic in $D$, small on the carriers, and in the real minimal orbit at real $D$. Real refinement (CA-III 36939–37000, "Refinement of the determining set", read: it is the fibre-inclusion lemma the note describes), then inner axialisation, then continuation give $U_n(X,M^n\mathbf U[D])=\mathbf U[D]^{g_X}$, where $g_X$ is the inner axialising gauge. So (14) holds under any normalisation of $\mathbf U[D]$.
- The tree bound is correct. A tree path has at most $d(L-1)$ bonds per level (CA-I 129550–129558); the note uses $dL$, which is larger. Also $\sum_{m<n}L^m\xi\le s_n/(L-1)$, and the product of exponentials gives $\|g^{\pm1}\|\le e^{C_tK_W\beta}$. Finally $e^x\le1+2x$ for $0\le x\le1/2$, because $e^x-1\le xe^x\le1.65x$.
- The (N1) path radius matches CA-I 155965–155967. The factor 1.21 is the one used at 156017–156038.
- In the CA, $c_u$ and $\beta_W$ are fixed constants depending on $(d,L,M)$ (154187–154190, 154358–154359). The note enlarges $c_u$ and lowers $\beta_W$ before $w_s,r_s$. The CA's conditions that read them ((S1) and the path minimum) are one-sided and are imposed again. No cycle arises.

**(15)–(19), lines 519–610: correct, as an implication.**

- (15) matches CA-I 155098–155146, with $\rho_s=2B_3w_s+8B_0r_s$.
- *One chart radius for all real bases.* CMP 102b (172) gives radius $C_1\varepsilon_1$. A base with tests at most $\varepsilon_*/2$ also satisfies CMP 102b (7) with $\varepsilon_*$, so one radius serves every base. CA-I 38505–38570 records this chart family. Correct.
- *(16).* CMP 98 Proposition 6 allows complex twists ("$A'$ with values in the complexified algebra") on a real base. It is used correctly as a cited input.
- *(18).* $U_0=U_k(V_0)$ is the axial minimiser on the torus (CA-I 38524–38525, 155103). It is block-axial on every tree, because the blocks are fixed $L$-adic blocks of one lattice (CA-I 129523–129552) and the scale-$j$ reading is the same lattice (CA-I 155274–155280). So the inner tree values of $U_0$ are one. The twisted values have logarithm at most $C_As_mC_{19}\rho_s$. Each tree product stays inside one inner structure block, so the bound does not depend on $|X|$ or on wrapping.
- *(19).* The consumer (N3), CA-I 155387–155429, reads only the norm bounds. Correct.

**(20), lines 612–639: correct, as an implication.**

- $f$ is invariant under all $G^{\mathbb C}$ gauges (CA-I 153964–153967). The datum bound on the whole $4r_s$-ball is CA-I 155930–155956. The (N2) consumer, CA-I 156045–156060, uses only the equality of values of $f$.
- The phrase "one-function property … identifies this chart with that orbit" relies on the gauge extension (d) of CA-I 38579–38625, Bałaban's (181). The CA records (d) as Bałaban's statement and does not reproduce its proof (38628–38634). The note cites "I 38550 onward", which includes (d), and its §6 (line 896) names the orbit extension as an input. So the step is valid from that input.
- A second route needs no orbit extension. It is their own reduction at CA-I 154397–154405: the left side equals $f(W,J(W))$ by gauge invariance, so it is holomorphic in $B$. The right side is holomorphic because $D(B)$ is (CA-I 155944–155946) and $\sup|D|<\beta_W$ strictly; the note's stronger (S4) ceiling (lines 634–635) supplies the strictness. The two sides agree at real $B$ by real nesting, and the identity principle 4.31:eq-complex-background-c finishes the proof.

## 4. The other sections

- **Source checkpoint (lines 5–29).** The hits I checked are correct: I 29235/29237 (§4.7), 121436–121443, 123126–123132, 154420, II 35714, II 44422 and II 44454. The hashes in §6 match my own fetches.
- **§1 (lines 31–111).** Read line by line. The argument is mu.md §6 plus the refinement lemma (CA-III 36939–37000) and block-axiality (CA-I 130021–130052). At depth zero $g=1$ (line 104), which is correct.
- **§2 (lines 113–322).** Read line by line, citations spot-checked. Datum (4) matches CA-I 117396–117451 and 121226–121232. The note writes the $\tau$-radius as $\mathsf w_0/(K^{\rm nr}\vartheta)$, while the source writes $\mathsf w_0r^{\rm nr}_\square$; I did not trace that identity. (5) matches CA-I 117206–117209 exactly. (7) matches 117732–117744; its second bound uses $K^{\rm nr}\vartheta\le\mathsf w_0/6$, as there. The relative factor $\bar u_\ell^{-1}u_\ell$ appears at CA-I 121436–121443 and 123129, and the sharp bound $G'_\square$ is a separate hypothesis there, "whose proof is incomplete at one step". The radii $C_0e^{-t/2}t^q$ and "$\gamma$ is chosen last" match 124430–124473. The derivative bound $-1/2+q/t\le-1/4$ for $t\ge4q$ is correct, and so is the arithmetic of (8). **Not traced:** the other §2.2 citations (about twenty line ranges) and the frame and AX2-poly steps behind (6).
- **§3 (lines 323–445).** (9) is CA-II 35731–35733 exactly. (10) is CA-II 35737. (12) is CA-II 35712, "modulo gauge". The arithmetic of (11), $2d\cdot(10dM/t_p)\cdot c_1a_Qt_p^2=20d^2Mc_1a_Qt_p$, is correct. The note's ordering remark (lines 360–383) is right: the inner-chart radius has to come before the identity theorem. One defect, at line 349 (defect 1).
- **§5 (lines 736–878).** (23) matches CA-II 44420, 44454 and 44459. (26): $1.2/(100L)=0.012/L<0.002$ needs $L>6$, and the note has $L\ge8$. (28): $28.8/220<29/220<0.14$. (29): $e^t\le1+t+t^2/(2(1-t))$, since $m!\ge2$ for $m\ge2$; at $t=7/25$ this gives $1201/900$, and $1201\cdot101\cdot29=3{,}517{,}729<3{,}600{,}000$. The collar sum needs $2L(L-1)>6$. The two "literal limits" are described accurately: CA-II 44438 puts $\gamma_x\subset\mathfrak r_v^\flat$ "for $x\in\mathfrak r_v$", and 44456 states an unweighted bound.
- **Result (lines 901–912).** Each item is supported by the text checked above. Item 3 makes no claim either way about the bound 2 in (b), and none is needed.

## 5. Defects

Only one defect breaks a step.

1. **Lines 347–353, the constant $C_Q$.** The note says the last inequality of CA-II 35662–35667 bounds $5.6K_hK_{ax}MC_M^{av}w_Q\alpha_Q$ by $K_{loc}\mathsf A_w$. The printed inequality, CA-II 35666, is $5.6K_{ax}MC_M^{av}w_Q\alpha_Q\le K_{loc}\mathsf A_w(\gamma)$, with no $K_h$. The $K_h$ form is CA-II 35681, which is a different bound. Dividing the printed inequality gives $w_Q\alpha_Q\le K_{loc}\mathsf A_w/(5.6K_{ax}MC_M^{av})$. CA-II 35697–35698 forces $K_{loc}\ge11.2K_hK_{ax}MC_M^{av}$, so the maximum in the note's $C_Q$ is not 1, and the note's $C_Q$ is the proved constant divided by $K_h$. The account does not give $K_h\le1$. If a constant potential is admitted, then $\ell_p|\mathcal H|=|B|$ there, which forces $K_h\ge1$. *Failure:* "$w_Q\alpha_Q\le C_Q\mathsf A_w(\gamma)$" does not follow as written when $K_h>1$. The note needs this comparison because $\mathsf A_w$ is a supremum of products (CA-II 34833), while $w_Q\alpha_Q$ is a product of maxima. *Repair (checked):* $C_Q:=\max\{1,K_{loc}/(5.6K_{ax}MC_M^{av})\}$. Then (11) is the same ceiling on $\mathsf A_w(\gamma)$ with a larger fixed constant, still chosen before $\gamma$. Nothing downstream changes.

Notes that break nothing:

- Line 698: the uniqueness of the small Landau critical configuration is stated in CMP 102b §A (p. 281), and §G reuses it.
- Lines 616–619: name item (d), CA-I 38579–38625, as the input used for (20), or use the second route of §3.
- Line 78: the refinement lemma ends at CA-III 37000, not 37007.

## 6. For the lead: what the correction is worth to them

Their §4.7 (CA-I 29234–29239) and §4.26 (CA-I 121436–121443, 123129) already use the correct gauge, $u_j\bar u_j^{-1}$, or its conjugate $\bar u_\ell^{-1}u_\ell$. The slip is local to §4.31: the statements (a) and (c), and the quote at 154423, which has $U_j$ where Bałaban has $u_j$. Its consumers (N1)–(N3) read only norm bounds and values of $f$, so their proof does not change. By FINISH item 6, this is a false statement in their text, shown by a hand example, with no effect downstream. This is a fact for the lead, not a recommendation to post.

## 7. Verdict

mu-radii.md stands after one repair (defect 1). The counterexample (21)–(22) is correct. It refutes the block-constant gauge of CA-I 154354–154376 in (a) and (c), at arbitrarily small real data, for Bałaban's Landau representative, which is the one their text cites. The corrected identities (14) and (19), with the bounds (14) and (18), are proved as implications on the whole (N1) path and on every allowed $X$, including wrapping $X$. So is the (N2) equality (20). Each consumer reads only what these give.

Inputs that remain inputs: frozen mu.md; CMP 98 Proposition 6 (complex twist); CMP 102b (172), §G and (181), with the orbit extension recorded at CA-I 38505–38634 without proof; and the account's own source bounds named in the note. Still open, as the note says: the bound 2 in (b), which is not needed; the whole-rim unweighted reading of CA-II 44422/44454, which is not needed; and the uses of 4.13 that this note does not cover (rows 363–364).

No numeric job was run. Every step above was checked by hand. Page images of CMP 109 were rendered only to read the printed formula.

Checked line by line by Claude (Mini worker).
