# s210-3-check: erasure and replay
Provenance: Codex (GPT-6; effort setting not exposed, queue requests xhigh); checkout `ee8a58759`; Sussman–Alpoge `31a47c543775`; not an audit; grants no status.

Queue row 197. Sections 3–6 of `library/s210-3.md` checked line by line by Codex against `s210.md`, Section 5.
Source credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
SA line numbers refer to their pinned `YM4_sketch_500.tex`, fetched once. No computational proof steps.

## 3. Coordinates and supplied rules

| Statement | Verdict; first failing step |
|---|---|
| Definitions 3.1–3.2, reconstruction on the asserted domain | **WRONG.** “Pivots from the constraint” does not define a map on all the stated coordinates. |
| (L1), choice of joined local problem | **CORRECT-NO-ADVANCE**, as a supplied definition; none. Its admission remains an input. |
| (L2), three zones | **CORRECT-NO-ADVANCE**, under the strip margins and an admitted coordinate chart; none. Products and complements preserve (8). |
| (L3), omission of old tests | **CORRECT-NO-ADVANCE**, conditional on (L2.2); none. |
| (L4), never-large record | **CORRECT-NO-ADVANCE**, as a record prescription; none. It does not admit the replacement coordinates. |

SA L7483–7487 gives a **local** pivot chart. Its integral runs over that chart's preimage, not unrestricted nonpivot coordinates.
SA L8287–8295 likewise gives a small-fibre chart with an explicit radius.
Definitions 3.1–3.2 specify neither these preimages nor their agreement after erasure.
Background existence and the strip margins do not supply that agreement.
Thus the blanket assertion that the supplied rules preserve the supported measure is not established.

## 4. Theorem E and its premises

**Theorem E: WRONG.** Checked line by line by Codex; first failing step: case 3 uses the unadmitted reconstruction above.
Case 7 makes the error explicit: a pivot enters “through densities” only.
Solvability and the chosen pivot branch also restrict the coordinate domain.
The sets $G_t$ impose (EX) and (M), not these restrictions.
Case 6 therefore omits an undefined-object failure: the pivot reconstruction itself.
Neither (10) on every branch nor product identity (E) has been proved.
Needed repair, unproved: a common pivot chart containing every supported branch and the fill, with matching domain indicators.

**Premises: CORRECT-NO-ADVANCE as explicit assumptions; first failing step none in treating them as assumptions.**
(SUP), (L2.2), (EX), (M) and (CAR) are cited inputs, not rebuilt results here.
(LAD) additionally assumes support control after replacing factors.
SA L17369–17395 gives implications on carried supports; it does not prove this replacement assertion.
Even granting all six premises does not supply the missing pivot domains.
The fixed-chart, nonpivot strip identities from `s210.md` (8) survive.

## 5. Corollary K, Proposition D and Lemma N

**Corollary K: WRONG.** First failing step: “The supports agree by Theorem E.”
Fixed reference measures do not remove missing chart domains. The normaliser argument cannot repair this failure.

**Proposition D: ADVANCE as a conditional Jacobian obstruction.** Checked line by line by Codex; first failing step none.
For $\Delta\mathbf h\ne0$, the set $\tilde\theta'(\varphi)n\cdot\Delta\mathbf h\ne0$ contains an open set of positive Haar measure.
Thus the two one-bond change-of-variables densities differ under its stated hypothesis $H_h\ne H_{h^-}$.
No actual erased pair satisfying that hypothesis is exhibited; an unconditional counterexample to (5) remains unproved.

**Lemma N, finite telescoping and the $C^1$ estimate: CORRECT-NO-ADVANCE**, conditional on (N1)–(N2); first failing step none.
The triangle inequality first gives $\|H^{(n)}\|\le C_N\varepsilon/(1-e^{-\delta_N})$.
The stated normal-coordinate bound then gives the displayed estimate without circular use of the small ball.

**Lemma N, exact label-local family at formation: WRONG.** First failing step: its consequence $t_n^h=t_n^{h^-}$.
(N1) fixes $W_n$ from the label in $W_{n+1}$; it fixes $W_{n+1}$ only using $W_{n+2}$.
An erased place in $W_{n+2}\setminus W_{n+1}$ can therefore change the chosen next region.
For example, $W_0$ can be fixed while $W_1$ selects either of two regions using a label bit in $W_2$.
This satisfies (N1), but does not identify the two $t_0$ terms after erasure.
A fixed-domain telescoping identity does not supply the required common family of formed terms.
Also, SA Theorem 6(c) compares backgrounds up to a gauge; the asserted common-gauge (N2) remains an input.

**The $F=\log J$ example and its uniform derivative bound: WRONG as stated.** First failing step: using $J\ge1/2$ throughout the nest.
(M) bounds the final $H$, not every $H^{(n)}$.
(N2) controls their size against $\delta$, not against $\operatorname{Lip}(\theta)^{-1}$.
A smooth permitted cutoff can have arbitrarily large slope.
The missing sufficient condition is $\operatorname{Lip}(\theta)\sup_n\|H^{(n)}\|<1/2$.

## 6. Proposition P

**P(a)–(b): ADVANCE.** Checked line by line by Codex; first failing step none.
Nested parents connect each lineage to its root. Added cells touch that connected set.
Each cell contributes at most $3^4=81$ same-weight neighbours, so $W\le81V$.

**P(c), the proposed record encoding: WRONG.** First failing step: “only its fate and its stage count”.
SA L17585–17614 distinguishes failure of the $B$ test from failure of the last-shell test.
Both can have fate drop-out, stage count $\mathsf N_j$, and the same frame.
Their factors are $1-\chi_B$ and $\chi_B(1-\chi_{\rm last})$, respectively. The proposed code does not distinguish them.
The inequality $\mathsf N_j+3\le e^{(MR_j)^4}$ therefore does not count the stated histories.
An extra failure-location symbol is needed; this need not destroy an exponential bound.

**P, complete support read closure with $J=81$: WRONG.** First failing step: its appeal to Theorem E(b)–(c).
The geometric volume estimate does not admit the replay or account for its missing chart-domain reads.
Thus (3), (5), (10) and rank 7 remain open. The first stop precedes (LOC).
