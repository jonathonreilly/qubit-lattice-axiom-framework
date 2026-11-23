lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T10:47Z

# Row 1456: the Lean flow against the account's first passage

Started 2026-11-23T22:47Z (date -u) on Mac mini worker 2, commit f0ea65331. Port reading. Not checked by another model.

Credit: the Lean release `YM4 Lean` at 3932084a9b82 and the complete account (CA-I, CA-II, CA-III) and outline at 31a47c543775 are by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Short attributed quotes only.

## Plan

1. Read check 1453 (`library/sa-ym4-lean-trajectory-check-astra62.md`) and the row 1451 note it checks; collect what is already established about FlowPassage, IsFirstPassageDatum, run_has_slope.
2. Read the Lean definitions (read only, never build): FlowPassage, IsFirstPassageDatum, run_has_slope, and the blocked Wilson density they read.
3. Read the account: 4.2:lem-first-passage and CA-I 56442-56510.
4. Compare: normalization of g, increments, window width, first-passage sets W_J(g) at matched lattice sizes.
5. Read rows 1332, 1353 and their checks: list the hypotheses of the first-passage seed reductions; decide whether they transfer.
6. Verdict: equal / first incompatible step. Next two rows.

## Repo search

(pending)

Prior on file: check 1453 (`library/sa-ym4-lean-trajectory-check-astra62.md`, lines 57-72) already matched the *form* of CA-I 4.2 (a), (c) with Lean's `passes`, found (b) absent from `IsFirstPassageDatum`, and left "identity of the flows or of their first-passage sets" open. Row 1451 (`prior/sa-ym4-lean-trajectory-opus.md`) and `port/p1-base.md` section 2.2 hold the CA arithmetic port. This row takes up only what check 1453 left open: the increments themselves.

Sources: CA-I and the outline fetched from raw.githubusercontent at 31a47c543775 into `/tmp/row1456.OKfxBS` (CA-I 166711 lines, outline 32992 lines). Lean release read in place at `~/ym4d-papers/sa-ym4-lean-full` (3932084a9b82), read only.

## Step 1. The account's side (CA-I)

Read: CA-I 606-675 (Definitions 1.2:def-couplings, 1.2:def-flow-constants), 3636-3721 (4.2:lem-first-passage and proof), 56342-56510 (Lemma 4.19:lem-flow-bounds, Proposition 4.19:prop-clause-zero).

- **Normalization of g.** CA-I 606-616: $x_0:=g_0^{-2}$, $x_{k+1}:=x_k-\beta_{k+1}$, $g_k:=x_k^{-1/2}$. The bare weight is $\exp(-g_0^{-2}A(U))$ with $A(U)=\sum_p[1-\mathrm{Re}\,\mathrm{tr}\,U(\partial p)]$ and the normalized trace $\mathrm{tr}\,\mathbf 1=1$ (CA-I 657-662, Definition 1.3 uses the same $A$). So $x=2N/g_{\rm std}^2$ in the convention $\beta_{\rm std}=2N/g_{\rm std}^2$, $S=\beta_{\rm std}\sum(1-N^{-1}\mathrm{Re\,Tr}\,U)$.
- **One-loop constant.** CA-I 636: $c_0=\frac{11N^2}{12\pi^2}\log L$. Check by hand: $d(g_{\rm std}^{-2})/d\log\mu=2\beta_0=11N/(24\pi^2)$, times $2N$ gives $11N^2/(12\pi^2)$ per unit $\log$. For $N=2$, $c_0=\frac{11}{3\pi^2}\log L$.
- **Increment.** CA-I 618-623: $\beta_{k+1}$ is Balaban's coupling renormalization, CMP 109 (1.22), identified with CMP 119 (3.61); its construction is CA-I 4.2:def-increment (line 3765, "complete regular part of one step"). It is a function of $g_0,\dots,g_{k}$ only (CA-I 56476-56478) and is torus-independent by input (h).
- **Two-sided bounds.** Lemma 4.19:lem-flow-bounds (CA-I 56342-56368): from the one-loop sum bound $\sum_{i<l\le j}\beta^0_l\ge (j-i)c_0-2c_2$, $|\beta^{\mathfrak A}_l-\beta^0_l|\le c_0/2$, $|\beta^{\mathfrak A}_l|\le C_\beta$, $|\beta^{\mathfrak R}_l|\le\bar\varsigma\le\min(c_0/4,1)$, it gives $\lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i)$ with $\lambda_\sharp=c_0/2-\bar\varsigma\ge c_0/4$, $B_\sharp=C_\beta+\bar\varsigma$, $c_5=2c_2$. Its inputs (the one-loop law 4.2:lem-one-loop and 4.2:lem-unmarked) are stated "with proof incomplete at the step marked $(\ast)$" (CA-I 56370-56385).
- **First passage.** $K(g_0,g)=\min\{k: x_k\le g^{-2}+B_\sharp\}$ (CA-I 662). Window: $g^{-2}\le x\le g^{-2}+B_\sharp$, width $B_\sharp$ in $x$ (CA-I 672-674). Bare range $0<g_0\le g_-(g)$. Lemma 4.2 (CA-I 3636-3664): from the two-sided bounds on every prefix with all earlier $x_i>g^{-2}$, (a) first crossing with $g^{-2}<x_K\le g^{-2}+B_\sharp$, (b) the two-sided bounds through $K$, (c) $\frac{t-g^{-2}}{B_\sharp}-1\le K\le1+\frac{t-g^{-2}-B_\sharp+c_5}{\lambda_\sharp}$. Proof read in full (CA-I 3666-3721): correct.
- **Lattice.** Bare spacing $L^{-K}$ on the torus $\mathbb T_m$; the step's block factor is $L$ (Balaban's $L$, odd and large in CMP 109). Torus exponent $m\ge m_{\mathbb T}(g_-(g))$.

What this side asserts about its own flow: Proposition 4.19 is conditional on inputs (a)-(h), among them Balaban CMP 109 Theorem 3 (cited) and two lemmas with proofs incomplete at one step. So $W_J(g)$ on the account's side is the set $\{g_0\in(0,g_-(g)]: K(g_0,g)=J\}$ for a flow whose increments are defined by Balaban's step, with the two-sided bounds conditional.
