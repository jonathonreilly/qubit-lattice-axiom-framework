lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T18:12Z

# mur-gate: referee of library/mu-radii.md (row 357)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 76a08cb5d. One line-by-line check of `library/mu-radii.md` (Codex, 912 lines), not an audit. Kind: check of our own new text, including a claimed correction of their text. Sources read: CA-I (`theorem_0_complete_account_raw_I.tex` at 31a47c543775, fetched by URL, SHA-256 4cb5cb5e…6e93, 166,711 lines) at the lines named below; Bałaban CMP 109 printed pp. 277–278 (rendered page images of the owner's copy) and CMP 102b (277–309) §A and §G (OCR text). Source authors: Ethan Sussman and Levent Alpoge, with Claude and Codex; the gauge constructions are Tadeusz Bałaban's.

(Report in progress; sections are added as they are checked.)

## 1. Source check of the claimed defect

These are the quoted passages that decide the counterexample. Each was read in full.

**S1. Their statement (a), CA-I 154354–154376.** "Each $\bar u$ below is a genuine $G^{\mathbb C}$-valued lattice gauge transformation $x\mapsto\bar u(x)$ which is constant on each block." Line (a) reads $U_n(X,M^n\mathbf U[D])=\mathbf U[D]^{\bar u^{-1}}$ on $X^{\sim-2}$, with $|\bar u^{\pm1}|\le1+c_u\beta$. Line (c) is the same with $W$ in place of $\mathbf U[D]$. CA-I 154419–154425 says the identity "corresponding to (a) is [CMP109, (3.38)]" and quotes Bałaban: "…constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $U_j$ at centers of the blocks."

**S2. Bałaban's printed (3.37)–(3.38), CMP 109 pp. 277–278** (page images, not OCR). (3.37): $U_j(\square_0,\exp i\tau Q(\cdot))=(\exp i\xi\mathbf H_j(\square_0,\tau Q(\cdot)))^{u_j}$, $|u_j-1|<B_3^2O(1)M\alpha_0$. (3.38): $U_n(X,M^{\cdot}(\exp i\xi\mathbf H_j))=U_n(X,M^{\cdot}(U_j))^{(\bar u_j)^{-1}}=U_j^{(\bar u_j)^{-1}}=(\exp i\xi\mathbf H_j)^{u_j(\bar u_j)^{-1}}$, "where $\bar u_j$ is a gauge transformation constant on blocks … and equal to $u_j$ at centers of the blocks." So the printed gauge on the Landau field is $u_j(\bar u_j)^{-1}$. Only $\bar u_j$ is block-constant. The CA quote in S1 changes the lower-case $u_j$ (a gauge transformation) into $U_j$ (a configuration).

**S3. Their own §4.7, CA-I 29234–29239,** reads the same display correctly: "We set $g_{\langle3.38\rangle}:=u_j\bar u_j^{-1}$. Here $\bar u_j$ is … 'constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $u_j$ at centers of the blocks'." So the account itself carries the non-block-constant factor in §4.7 and drops it in §4.31.

**S4. Which representative is $\exp i\xi\mathbf H$.** CMP 102b §G, p. 305: "At first we fix the Landau gauge for the configuration $U_k(V'V_0)U_0^{-1}=U_1'$ and we have $U_1=\exp i\eta\mathcal H(B)$" (173). P. 307: "we transform the configuration in the Landau gauge back to the axial gauge". Proposition 9: "The function $U_k(V'V_0)U_k(V_0)^{-1}$ transformed to the Landau gauge is, by the definition, equal to $\exp i\eta\mathcal H(B)$." The Landau space is CMP 102b (19)–(21), p. 281, with (21) $R(U_0)D^*_{U_0}A=0$; Proposition 2 maps its critical configurations one-to-one to the axial ones by gauges normalised at the roots. CA-I 154193–154230 calls $\mathbf U[D]=e^{i\xi\mathcal H_j(\square_0;D,\mathbf 1)}$ "the local form of the construction of the complex background field", unique under "the normalisation of the global construction". CA-I 155098–155112 defines $W_{V_0}(B)=e^{i\eta\mathcal H(B;U_0)}U_0$ the same way. Neither passage names a gauge, so the cited construction fixes it: Landau.

**S5. Axial condition on the local minimiser.** CA-I 32896–32897: "$U_n^{\mathfrak r}(Z;\cdot)$ [is] the axial-gauge minimiser of the depth-$n$ problem". CA-I 130021–130052 (HBA): for every $m<n$ and every $(m+1)$-block $B'$ inside a structure block of level $>m$, $[M^mU](b)=1$ on every bond $b$ of the gauge tree $\mathcal T_m(B')$. At $m=0$ this is $U(b)=1$ on the fine tree bonds of each 1-block. CA-I 29240–29242: Bałaban's $n$ in (1.15)–(1.16) runs over $1,\dots,j$, so $n\ge1$ is allowed.

**S6. What the consumers read.** (N1) at CA-I 156008–156038 and (N3) at CA-I 155387–155429 use only $|\bar u^{-1}||\bar u|\le1.21$, the plaquette conjugation $U^h(\partial p)=h(x)U(\partial p)h(x)^{-1}$ (stated there for a general gauge $h$), and $|\operatorname{Ad}(\bar u^{-1})Y|\le|\bar u^{-1}||\bar u||Y|$. Block-constancy is not used. (N2) at CA-I 156045–156060 uses only equality of the values of $f$.
