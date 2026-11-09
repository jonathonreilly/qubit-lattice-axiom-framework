# CORE-GAPS reading and map

Reading-only note for FINISH row 616. Research text; no proof, audit, or status
grant. Sources read in bounded ranges from Ethan Sussman and Levent Alpoge's
`YM4_1400.tex` (commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`) and the
local `geo-5.md`. Credit Sussman and Alpoge, with Claude and Codex as authors of
their text, for the outline/account material quoted here.

## Repo search

The lead's `library/prior/repo-search-2026-11-08.md` contains no CORE-GAPS,
`prop:large-field-2-3`, or `core-read` hit; targeted searches of that digest
likewise returned no direct match. The task's row 616 names no additional
"Repo prior work" file or line range. The closest repository work is local:

- FINISH row 614 / `library/h-geo.md` proves H-GEO **given CORE-GAPS**. It is a
  consumer of this hypothesis, not a proof of CORE-GAPS.
- FINISH row 615 is the independent check of H-GEO and expressly leaves CORE
  to this row. It is adjacent ownership, not duplicate work.
- `library/open-registry.md` rows 1000–1001 mark H-GEO as holding given
  CORE-GAPS, and CORE-GAPS itself as open and owned by `core-read`; this is
  the exact repository statement being read, not prior evidence for it.
- `library/geo-5.md` sections 3.1–3.3 provide the candidate rule-by-rule
  argument to map; this note compares its stated rules with Y and does not
  assess transfer validity.

The prior digest's broad PR/main comparisons identify no source passage for
CORE-GAPS. No remote file was named by the row, so no additional branch file
was opened. The closest published-outline material is the indexed SA outline
itself: its Proposition 2.3 is indexed as sketched (chunk 16, SA 17398–17407),
and its initial-`Omega_0` rule is indexed as assumed (SA 17317). I then read
those cited source lines. The older outline directly states the one-layer
initialization (SA 17317), eight/ten quiet-class formulas (SA 17578–17580),
the step padding (SA 17319–17325), the fates (SA 17415–17430), and the
stopping sequences (SA 17433–17440). These are the closest source counterparts
and explain `geo-5.md`'s citations. They do not replace the requested check of
the later `YM4_1400.tex` passages, whose scope is marked separately below.

## 1. Status of `prop:large-field-2-3`

Y states the proposition with a citation; it does not prove it in the
proposition. There is no `proof` environment. The proposition body contains
the following quotations (ellipses below mark omissions):

> “The regions are nested, \(T_\ell\supset\Omega_1\supset\Lambda_1\supset\dots\supset\Lambda_k\), with gaps of at least \(cM\check{R}_j\) in level-\(j\) units. Every large-field region and every creation set is a union of cells of its own level. Both statements hold for the regions that the steps produce (119, p. 256). Each operation \(\mathbf{R}\) has stage sequences and prepared sequences (namely the regions that the label has after \(m\) of its stages, and after all \(\mathsf{N}_k\) of its stages; see \cref{sec:large-field-stored-variables-and-integration-in-a-large-field-patch}), on which the backgrounds of \cref{sec:large-field-stored-variables-and-integration-in-a-large-field-patch}, \cref{candidate:large_field} are formed, and drop-outs keep nests. In these sequences and nests the boxes are only unions of \(M\)-cubes, and the only lower bound on the gaps is one \(M\)-cube of the later level:” (Y 62080)

The proposition continues with these conditions and text:

> “\(\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM,\quad
> \Omega_{j+1}\subset\Lambda_j^{\sim-1},\quad
> Z_j^\sim\cap\Omega_{j+2}=\emptyset\)
> (level-\(j\) units; layers of \(M\)-cubes of level \(j\)). The first
> inequality is an equality at the active indices […] where
> \(\Lambda_j=\Omega_j\). […] At \(j=k_0(t)+1\) the gap is instead
> \(w_j-w_{j+1}\) in bare units, which still gives the displayed lower
> bound but can be larger; the reason is that a step places eight layers
> around the old region, and the preparation removes most of them again.
> Consequently the estimates […] must hold with a separation of only one
> \(M\)-cube. […] A history records every outcome: \(P_t\), \(Q_t\),
> \(R_t\), the collars and rims, and the outcomes inside \(\mathbf{R}\).
> […] All later statements of locality rest on this.” (Y 62082–62100; ellipses mark omitted text)

There is no derivation after the citation: the proposition closes at Y 62101,
and the next statement begins at Y 62103. The text gives the cited assertion,
the region formulas and an explanation of the one-cube prepared-gap bound.

## 2. Constants

Y's first parameter passage reads:

> “Fix powers of \(L\) called \(\mathfrak M,M_1',M\), a gap \(\rho=R_1\mathfrak M\)” (Y 638–639); “Take \(L\ge13\) odd, \(R_1\ge L\), \(M_1'\ge R_1\mathfrak M\)” (Y 650–651), and immediately after the requested range, “\(M\ge L^4M_1'\)” (Y 652).

The second requested passage says:

> “fix powers \(\mathfrak M,R_1,\rho\) of \(L\) with \(L\ge13\), \(\mathfrak M\ge\mathfrak m^{\mathrm s}\), \(R_1\ge L\), \(R_1\mathfrak M\ge L^2\rho\), and \(\rho\ge\mathfrak r^{\mathrm s}\)” (Y 14938–14942).

Y also adds: “Every level-\(k\) coordinate circle has at least \(6\rho\)
sites. The gap in \(\eqref{mb:separation}\) is greater than
\(R_1\mathfrak M\xi_j\). The
fixed floors \(\mathfrak m^{\mathrm s},\mathfrak r^{\mathrm s}\) depend on
\(L\). Empty regions and regions equal to the whole torus are allowed”
(Y 14944–14949).

`geo-5.md` says:

> “Choose the fixed lengths … with \(M>\rho\ge2\), \(\mu\ge\rho\), \(M\ge80\mu\), \(L\ge27\), and \(\theta\min(M,\rho)\ge64\log L\).” (`geo-5.md` line 45)

Comparison, inequality by inequality:

| `geo-5.md` choice | Verdict from Y's choices | Basis / limit |
|---|---|---|
| \(M>\rho\ge2\) | **Follows from Y 638–652 alone; does not follow from both passages as a single consistent parameter choice if the two `rho`s are identified.** | Y 638–652 sets \(\rho=R_1\mathfrak M\), \(M_1'\ge R_1\mathfrak M\), and \(M\ge L^4M_1'\), with \(L\ge13\) and positive powers of \(L\); these give \(M>\rho\ge2\). But Y 14941 also says \(R_1\mathfrak M\ge L^2\rho\). If its \(\rho\) is identified with Y 638's \(\rho=R_1\mathfrak M\), the two declarations conflict for \(L\ge13\), \(\rho>0\). Y does not state in these ranges that the two uses are distinct. |
| \(\mu\ge\rho\) | **NOT STATED.** | Neither requested Y parameter passage specifies \(\mu\). |
| \(M\ge80\mu\) | **NOT STATED.** | Y gives \(M\ge L^4M_1'\), but no relation to \(\mu\). |
| \(L\ge27\) | **Does not follow.** | Y states \(L\ge13\); that lower bound alone does not imply 27. |
| \(\theta\min(M,\rho)\ge64\log L\) | **NOT STATED.** | No such \(\theta\)-condition appears in the requested Y choices. |

This records the parameter text only; it does not decide whether the proof of
`geo-5.md` transfers.

## 3. Rule map with source excerpts

The `geo-5.md` statements below are from its §§3.2–3.3 (lines 49–84). Y quotes
are from the requested ranges 62095–62140 and 63716–63811, with Y 62094 used
for its immediately preceding explanation of the step padding.

1. **Live-set two-cell padding.** `geo-5.md`: “Just after step t, the live
   large-field set contains the two-cell enlargement of \(\Omega_t^c\)” (49).
   Y's quiet-component formula is “\(O_i:=\Omega_i^c\cap X=H_i^{[8a_i]}\),
   \(G_i=H_i^{[10a_i]}\)” (63761–63765); the preceding passage defines
   \(a_i=M\check R_iL^i\) as “the side of a level-\(i\) cell” (63748–63749).
   This gives a two-cell shell in that quiet-component construction, but the
   requested Y lines do not state the general post-step live-set containment
   as such. The older SA outline does state the step rule explicitly:
   “\(\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup\widehat{Y}^{\sim8}\)” and
   “\(Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^{\sim})\)” (SA
   17320–17321). That is the direct source counterpart for `geo-5.md`; it
   remains distinct from the later Y verdict in the table.

2. **Quiet class component, eight and ten layers.** `geo-5.md`: “inside a
   quiet class component, the literal formulas
   `Omega_t^c intersect Q=H_t^[8]` and `Q=H_t^[10]`” (55–56). Y:
   “\(O_i:=\Omega_i^c\cap X=H_i^{[8a_i]},\quad G_i=H_i^{[10a_i]},\quad
   G_k=X\)” (63761–63765), with \(a_i\) the level-i cell side as above.
   The layer counts agree; Y writes the layer length explicitly in bare units.

3. **New step: hull plus eight layers.** `geo-5.md`: “The new step puts its
   hull and eight level-t layers into \(\Omega_t^c\)” (61). Y says, “the
   reason is that a step places eight layers around the old region, and the
   preparation removes most of them again” (62093–62094). The local output
   description also says it is “given by the eight-layer hull and by boxing
   the ten-layer hull” (Y 63709–63711); the cell side is \(a_i\) (Y 63748–
   63749). Y's proposition separately warns that the prepared nest can retain
   only one later-level M-cube gap (62089–62094).

4. **Initial region.** `geo-5.md`: “At the initial level,
   `Omega_0=Omega_1` enlarged by one level-1 cell layer” (61). No matching
   initialization rule is stated in Y 62095–62140 or 63716–63811. Y mentions
   \(\Omega_0\) as the domain for bare-field current at 62078, but does not
   define it there. The distinct, older outline explicitly says “A label's
   sequence starts at \\(\\Omega_0=\\Omega_1^\\sim\\), the first region enlarged
   by one layer of level-1 cells” (SA 17317).

5. **Three fates and region formulas.** `geo-5.md`: “Healing fills Q in every
   member. Island formation fills it in every determining member through t
   and in every action member below t; `Lambda_t` retains Q as a hole” (82).
   For a stop after n stages, its changed entries are “`Q minus D_i`,
   `b<i<=b+n`”; the top action member is retained in a drop-out (74, 78).
   Y's fate rules say: “Healed …
   \(\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\)
   for \(l\le t\)” (62105); “Island … the same replacement is made for
   \(l<t\) and for \(\Omega_t,S_t\), but \(\Lambda_t\) is left unchanged”
   (62106); and for a drop-out,
   “\(\Omega_l\cap X=X\setminus Z''_l(X)\)” and
   “\(\Lambda_l\cap X=X\setminus Z''_l(X)\)” over the stated partial range,
   with “all other entries unchanged” (62107–62115). Under the local
   identifications \(Q=X\) and \(D_i=Z''_i(X)\), the region rules agree.

6. **Stopping choices.** `geo-5.md` treats a stop after n stages and later
   “Changing a standing drop-out's stopping choice from n to `nu<=n`” (74,
   84). Y states “some test fails after \(n\le\mathsf N_t\) stages”
   (62107), allows \(0\le\boldsymbol\nu(X)\le n(X)\) and gives the two
   retained-region formulas (62121–62128), then says each such
   \(\Omega^{\boldsymbol\nu}\) is the label obtained by stopping after that
   many stages (62128). The stopping-index range and its region-sequence
   interpretation agree.

## 4. Rule verdict table

| `geo-5.md` rule | Y verdict | Concise comparison |
|---|---|---|
| Live large-field set after step contains a two-cell enlargement of \(\Omega_t^c\) | **NOT STATED in Y** as a general containment | Y gives the two-cell thickness in its quiet-component 8/10 formula, not the general live-set rule. |
| Quiet component: \(\Omega_t^c\cap Q=H_t^{[8]}\), \(Q=H_t^{[10]}\) | **Same** | Same 8/10 layer counts; Y writes the cell side as \(a_i=M\check R_iL^i\). |
| New step adds hull and eight level-t layers into \(\Omega_t^c\) | **Same** | Eight layers in both; Y describes the level-i cell scale explicitly via \(a_i\), then notes preparation removes most of the padding. |
| \(\Omega_0\) is \(\Omega_1\) enlarged by one level-1 cell layer | **NOT STATED in Y** in the requested ranges | SA 17317 states the same rule in the older outline; it is absent from the requested Y ranges. |
| Healed / island / drop-out fates and region formulas | **Same** | Y's union, complement, unchanged-entry, and top-action retention rules match `geo-5.md` with \(Q=X\), \(D_i=Z''_i(X)\). |
| Every permitted stopping choice | **Same** | Y allows partial stage index \(0\le\boldsymbol\nu(X)\le n(X)\) and identifies each sequence with a stopped label. |

## Source handling

Fetched once to the requested `/tmp` paths: the 32,992-line outline, the
166,711-line CA-I account, and the 136,637-line `YM4_1400.tex`. Before the
source reads, I consulted the SA-index README, chunk 16's neighboring rows,
the relevant chunk 17 rows, and `obligations.md`; the CA-I 4.12–4.19 index
README and relevant chunk 06 rows were also consulted. Bounded source ranges
read were SA 17315–17445 and 17575–17583; Y 62076–62140, 63700–63811,
637–652, and 14927–14950; only the bounded `geo-5.md` ranges named above. The
complete account was not read. No proof, computation, test, or audit was run.
