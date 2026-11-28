import sys
p=sys.argv[1]; t=open(p,encoding='utf-8').read()
def rep(a,b):
    global t
    assert t.count(a)==1, (t.count(a), a[:60])
    t=t.replace(a,b)
rep("""subagent of the lead session (no subagents of its own; `--subagents 0`,
context-isolated passes by the one writer). Lane commit `061d46c6f`
(branch `claude/ym4d-hard-route`).""",
"""subagent of the lead session (no subagents of its own; `--subagents 0`,
context-isolated passes by the one writer). Lane commit `061d46c6f`
(branch `claude/ym4d-hard-route`); the lead pulled the checkout to
`a4ebff848` during step 3 (it brought `library/prior/gap-face-alt-read-luna.md`).""")
rep("""| N4 | **Two-dimensional O(N) and principal chiral models.** Gap for small $\\beta$: THM (high-temperature expansion). $N=2$: no gap at large $\\beta$ (Kosterlitz-Thouless phase): THM, Fröhlich-Spencer, CMP 81 (1981). $N\\ge3$, all $\\beta$: **open**. Large $N$ at fixed $\\beta$: gap for $N>N_0(\\beta)$: THM, Kupiainen, CMP 73 (1980). SU(2) principal chiral = O(4). | THM / open | as named | all recalled. |""",
"""| N4 | **Two-dimensional O(N) and principal chiral models.** Gap for small $\\beta$: THM (high-temperature expansion). $N=2$: no gap at large $\\beta$ (Kosterlitz-Thouless phase): THM, Fröhlich-Spencer, CMP 81 (1981). Large $N$ at fixed $\\beta$: gap for $N>N_0(\\beta)$: THM, Kupiainen, CMP 73 (1980). SU(2) principal chiral = O(4). $N\\ge3$, all $\\beta$: this run first wrote "**open**" from recall. **Corrected 2026-11-17 after step 3**, from the reading of row 1104: see N4c. | THM | as named | all recalled. |
| N4c | **Two-dimensional O(4), every finite $\\beta$** (added after step 3). (1) O(n), $n\\ge3$: for every finite $\\beta$, every finite subgraph of the square lattice and every bond strengths in $[0,\\beta]$, $0\\le\\langle\\sigma_x\\cdot\\sigma_y\\rangle\\le Ae^{-m|x-y|}$, no field, no fixed spins. (2) O(4), homogeneous periodic squares: a unique periodic local limit and a full transfer gap $m_{\\rm lat}(\\beta)\\ge c\\exp\\{-\\pi\\beta-C\\sqrt{(1+\\beta)\\log(2+\\beta)}\\}>0$ for every finite $\\beta$; for $\\beta\\ge\\beta_0$, $c\\sqrt\\beta e^{-\\pi\\beta}\\le m_{\\rm lat}\\le C\\sqrt\\beta e^{-\\pi\\beta}$. Its Theorem 3.1 gives uniform mixing for bond strengths $0\\le\\beta_e\\le\\beta$ on unpinned tori and free subgraphs. No theorem with external fields, pins, or several coupled copies. | THM (research preprints, September 2026) | OpenAI Math preprints *Exponential decay in two-dimensional classical O(n) models* (Thm 1.1, Cor 1.2) and *Sharp mass bounds for the two-dimensional O(4) model* (Thm 1.1, Cor 1.2, Thm 3.1) | **read by gpt-6-luna (row 1104, `library/prior/gap-face-alt-read-luna.md` section 2), not by this run.** Standing: argued (published by its authors); not checked by the reading or by this run. |
| N1b | **A wider strong-coupling range** (added after step 3). SU(2), $0\\le\\beta<1/3$: unique gauge-invariant local limit of free-boundary boxes, transfer gap $m\\ge-\\log(3\\beta)$. A larger range ($\\beta\\le0.345$) in the same paper rests on machine interval certificates and is not usable here (S4). | THM (research preprint) | Bhattacharjee-Bhattacharya-Lockwood-Romanov, hexagonmath 2610.00341v5, Thm 1.1 | read by gpt-6-luna (row 1104 file, section 4), not by this run; unchecked. The same file confirms N1a ($\\beta<1/12$ from Shen-Zhu-Zhu Cor 1.6; it prints the assumption once as $1/[16N(d-1)]$ and then uses $1/48$ for $N=2$, $d=4$; the abstract seen by this run says $1/(16(d-1))$). |""")
rep("""34-plaquettes couple them. For $\\beta_{34}=0$ the gap is exactly the gap of
the two-dimensional O(4) model, **open** at window couplings (N4).
*(argued reduction; the open part is N4.)*
So a face at infinity is never a free end-point. Uses N3, N4, N8b.""",
"""34-plaquettes couple them. For $\\beta_{34}=0$ the gap is exactly the gap of
the two-dimensional O(4) model. *(argued reduction.)* **Corrected after
step 3 (N4c):** that gap is positive at every finite coupling by a
September 2026 preprint (read by luna, not by this run), for homogeneous
periodic squares, and of order $e^{-\\pi\\beta}$: about $4\\cdot10^{-4}$ times a
constant at $\\beta=2.5$. So this face is a proved end-point given N4c, with
an exponentially small rate; and the rate tends to 0 only as the sheet
couplings tend to infinity. The first text of this run said "open".
So a face at infinity is either false (a, b) or a proved end-point with a
very small rate that rests on N4c (c). Uses N3, N4c, N8b.""")
rep("""| E6 sheet faces ($\\beta_{12}=\\infty$) | needs N4 | **an open problem** (two-dimensional O(4)); and the rate tends to 0 at the face | lower one coupling from infinity |""",
"""| E6 sheet faces ($\\beta_{12}=\\infty$, $\\beta_{34}=0$, the four mixed orientations at $\\beta$) | N4c (corrected after step 3; first written as "an open problem") | none for homogeneous sheets, **given N4c** (a preprint, read by luna, unchecked). Rate of order $e^{-\\pi\\beta}$: very small. Sheets coupled to each other, or in fields, are not covered by N4c | lower $\\beta_{12}$ from infinity to $\\beta$ and raise $\\beta_{34}$ from 0 to $\\beta$: two singular moves, from a start rate near $10^{-3}$ |""")
rep("""- **C5** (N3, N4, N8b): faces at infinity give rate 0 or an open problem.""",
"""- **C5** (N3, N4c, N8b): faces at infinity give rate 0 (a, b) or, for the
  sheet face, a rate of order $e^{-\\pi\\beta}$ that rests on N4c (corrected
  after step 3).""")
open(p,'w',encoding='utf-8').write(t)
print('ok')
