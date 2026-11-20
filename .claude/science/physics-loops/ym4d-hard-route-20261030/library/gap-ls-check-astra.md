# Repo search

<!-- Saved plan
1. Check the prior searches, the registry and the pinned sources for overlap.
2. Identify the precise statements and hypotheses using the outline and account indices.
3. Derive the line-spin transfer spectrum and its physical gap.
4. Verify the finite seed, both bounds on its threshold and the fixed-physical-side limit.
5. Check admissibility and compare each hypothesis in rows 1161, 1179 and 1180.
6. Check the ultraviolet interpretation and the lattice-gap wording in the three cited rows.
7. Record the verdicts and verify the references and the final result.
-->

OpenAI Codex, gpt-6.2-astra at max effort. Cross-provider hand check of Claude Opus 5.5, FINISH row 1234, at `173592579c39d95e548152636df305fe6a6ecba5`. Research text only. These verdicts grant no standing.

The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its nearest outside-lane hit, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PR 10114, lines 106–149, bounds a single plaquette correlation at one time step. LS needs a trace over all excited levels on a growing cube. The digest predates row 1234, and row 1250 names no further “Repo prior work” hit. I checked the YM4D research and soft-route paths and the Wilson and Yang–Mills document names on main `8b11ae2bb` and those four PR heads, also 10144, for the line-spin, neutral-seed, (N-phys) and (NS-gap) labels. This search found no earlier check of LS. The target-specific prior file is absent. The open registry has no matching owner. [November 8 search](prior/repo-search-2026-11-08.md)

Row 1135, lines 164–175, gives the model, transfer spectrum and divergent symmetric-torus excess. Row 1138, lines 338–358, already checks these. Row 1180, R9, and row 1187, line 174, already identify the first-multiplet count obstruction. Row 1234 adds the fixed-coupling seed bounds and compares the quantifiers. The present check concerns that addition and its stated uses. [Row 1135](gap-slab-a-astra.md) · [Row 1138](gap-slab-a-check-opus.md) · [Row 1187](gap-neutral-pair-check-astra.md) · [Text under check](gap-mini-solve-v-opus.md)

## Statements and conventions

LS(a)–(e) are lines 112–150 of row 1234. Fix $m>0$ and $K\ge1$. At spacing $a$, set $\varepsilon=ma$ and hold it fixed when varying $n$. The two explicit size bounds assume $0<\varepsilon\le1$. The spin seed uses $s(u;n^3)=\operatorname{Tr}U^u-1$ for $U=T/\|T\|$. It asks for an **integer** $3\le u\le n/K$ with $s\le1/2$. The least such integer side is $\nu(\varepsilon)$. All logarithms are natural. The mass in lattice units is $-\log(\lambda_1/\lambda_0)$.

Row 1180, lines 35–52 and 95–114, instead takes the periodic **centre-neutral** trace of the gauge-projected Wilson transfer, fixes $K=512$ for its explicit test, and requires $4\mid n$ and $n\ge2^{70}$. Its $\nu'_j$ also restricts $a_jn$ to one common dyadic grid. Its (a) requires a finite seed at each sufficiently fine cutoff. Its (b) requires $\limsup_j a_j\nu'_j<\infty$. The left side of its equivalence requires **one** physical side that passes for **all** sufficiently fine cutoffs. These distinctions matter even when the first excited energy is known exactly. [Row 1180, Step 2.1](gap-mini-neutral-fable.md) · [Row 1187, lines 25–44](gap-neutral-pair-check-astra.md)

The outline index, its neighbouring mass-gap rows and obligations, and the CA-I 4.12–4.19 index contain no line-spin seed estimate under these labels. The outline, lines 588–599 and 31871–31882, distinguishes a spectral support gap from decay of an individual correlation. CA-I, lines 2706–2711, leaves a mass gap outside its assertion. Those scope statements are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. LS uses the spin transfer specified in row 1135. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L588-L599) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2706-L2711)

## Proposition LS

**LS(a), lines 102–110, 114 and 130–135 — HOLDS for the energy gap.** One can read the vacuum normalization directly from a rectangular torus. On $n^3\times u$ there are $n^3$ closed lines of length $u$ and $3un^2$ closed lines of length $n$. Integrating once around each line takes the trace of the corresponding power of $C_a$. Hence
$$
Z(n^3,u)=Z_{\rm line}(u)^{n^3}\,Z_{\rm line}(n)^{3un^2}.
$$
For fixed $n,a$, $Z_{\rm line}(u)\to1$ by domination by the convergent heat trace at $u=1$. Thus $\lim_{u\to\infty} Z(n^3,u)^{1/u}=Z_{\rm line}(n)^{3n^2}=\lambda_0$. This also equals $\langle A,A\rangle$ in row 1234, where $A^2$ is the spatial slice weight. Dividing by $\lambda_0^u$ gives exactly $\operatorname{Tr}U^u=Z_{\rm line}(u)^{n^3}$.

The vacuum-normalised slice transfer $U$ is $C_a^{\otimes n^3}$ tensored with the orthogonal projection onto the span of $A$. In row 1135's Laplacian convention the $d$-dimensional irreducible representation has multiplier $\exp[-\varepsilon(d^2-1)/3]$ on its $d^2$ matrix coefficients. All factors have $d=1$ in the unique top vector. The largest excited multiplier is $e^{-\varepsilon}$, with one $d=2$ factor at any site and all others constant. Its multiplicity is exactly $4n^3$. Thus the logarithmic gap is $\varepsilon$ and the gap in physical energy is $m$, on every spatial cube. If “spectral gap of $U$” at line 114 means the difference of its first two eigenvalues, that difference is $1-e^{-\varepsilon}$. The directions orthogonal to $A$ in the perpendicular slice factor have transfer eigenvalue zero and contribute nothing to positive-time traces. [Row 1135, lines 164–175](gap-slab-a-astra.md)

**LS(b), lines 116 and 136–138 — HOLDS.** Put $v=\varepsilon u$. The $d=2$ summand is $4e^{-v}$ at every $v>0$. For $v\ge3$, divide the rest by $e^{-v}$ and bound its $d$th term by $b_d=d^2e^{-(d^2-4)}$. For $d\ge3$, $b_{d+1}/b_d\le(16/9)e^{-7}<1/500$. Small rational bounds suffice here. The exponential series through degree six gives $e>1957/720>1359/500$, whence $e^2>369/50$, $e^5>(369/50)^2(1359/500)>148$ and $e^7>1000$. The tail is therefore less than $(9/148)(500/499)<61/1000$. This verifies even the tighter constant in line 138 and gives $Z_{\rm line}(u)-1\le 4.1e^{-v}$.

**LS(c), lines 118–120 and 139–145 — HOLDS AFTER CORRECTION to the integer endpoint argument.** Both stated bounds hold as printed. Showing that every integer $n\ge B$ passes would by itself give only $\nu\le\lceil B\rceil$. The rounded $10.12$ in line 140 also gives a sufficient threshold. Here is an estimate at $\lfloor B\rfloor$ that proves the advertised real upper bound.

Write $R=K/\varepsilon$, $w=\log R\ge0$, $B=R(4w+12)$ and $n_0=\lfloor B\rfloor$. For every $n\ge n_0$, take $u=\lfloor n/K\rfloor$. Then
$$
\varepsilon u\ge n/R-\varepsilon\ge 4w+10.
$$
In particular $u\ge3$ in the stated range $0<\varepsilon\le1$. The function $x^3e^{-x/R}$ decreases for $x>3R$, and $n_0/R\ge4w+11$. Consequently
$$
 n^3e^{-\varepsilon u}
 \le n_0^3 e^{\varepsilon-n_0/R}
 \le (4w+12)^3e^{-w-10}
 \le 12^3 e^{-10}.
$$
The logarithmic derivative of the preceding majorant in $w$ is $12/(4w+12)-1\le0$. From $41\cdot12^3<4\cdot148^2$ and the bound on $e^5$ above, $4.1\cdot12^3e^{-10}<2/5<\log(3/2)$, where the last inequality follows by integrating $2/(1-t^2)$ from $0$ to $1/5$. Now $n^3\log Z_{\rm line}(u)\le4.1n^3e^{-\varepsilon u}<\log(3/2)$. Every $n\ge n_0$ passes, including $n_0\le B$. Finiteness alone extends to every fixed $\varepsilon>1$ by monotonicity of each heat multiplier in $\varepsilon$.

**LS(d), lines 122 and 146–148 — HOLDS AFTER CORRECTION to the last decimal comparison.** For all $v>0$, Bernoulli's inequality and the first multiplet give $s(u;n^3)\ge4n^3e^{-v}$. Thus a passing pair has $n\ge3K$ and $z=n/R\ge\log(8n^3)=3w+\log(8z^3)$. In particular $z\ge\log216>5$. Line 148 rounds $\log(8\cdot5^3)$ upward to $6.91$. An exact bootstrap avoids the rounding. First $z>\log1000>6$, then $z>3w+\log1728>3w+7$. For these comparisons, the exponential series gives $e\le5/2+(1/6)/(1-1/4)<11/4$, so $e^2<8$, $e^5<192$, $e^6<729$ and $e^7<1536$. This proves the claimed lower bound $\nu\ge R(3w+6.9)$.

**LS(e), lines 124–128 and 149–150 — HOLDS for the spin trace.** For any $a_j\to0$ at fixed $m>0$, (d) implies $a_j\nu(ma_j)\ge (K/m)[3\log(K/(ma_j))+6.9]\to\infty$. More directly, at **each** fixed admissible $L>0$, every permitted integer $u\le n_j/K$, $n_j=L/a_j$, satisfies
$$
s_j(u;n_j^3)\ \ge\ 4 (L/a_j)^3 e^{-mL/K}\ \longrightarrow\ \infty .
$$
Thus every sufficiently fine cutoff fails at that side, uniformly in the choice of $u$. Under $4\mid n$ and $n\ge2^{70}$ a sufficient passing side is $\max\{2^{70},4\lceil B/4\rceil\}$. On a common dyadic physical grid take the next admissible grid side above this threshold in physical units. At each cutoff it exists, and the least passing grid side is at least $a_j\nu(ma_j)$. For instance $a_j=\ell_1/(4b^j)$ for any integer $b\ge2$, including an odd blocking factor, admits every grid side $2^i\ell_1$ with $i\ge0$. Thus the failure occurs on the very grid used in row 1180.

**Leading coefficient, lines 217–219 and 253 — HOLDS for the stated $\nu$, with an extra argument.** The two bounds alone allow leading coefficients between 3 and 4. Fix $\delta>0$ and take $n=\lceil R(3+\delta)w\rceil$ as $w\to\infty$. Then $\varepsilon\lfloor n/K\rfloor\ge(3+\delta)w-1$, and $n^3e^{-\varepsilon\lfloor n/K\rfloor}\le e[(3+\delta)w+1]^3e^{-\delta w}\to0$. Hence this $n$ passes eventually. By (d) and then $\delta\downarrow0$, $\nu/(R\log R)\to3$. In particular $a\nu(ma)\sim(3K/m)\log(1/(ma))$ for fixed $K,m$. Rounding up by fewer than four sites preserves this limit. A fixed dyadic grid may round the physical side up by a factor approaching two. Its divergence suffices for (e).

The GUIDE at lines 152–157 supplies no step above. For fixed $\lfloor n/K\rfloor$ the trace increases with $n$, so a bisection in $n$ alone would need a separate argument to certify the *least* passing side.

## Admissibility and the three Wilson rows

**Structural assumptions, lines 102–107 — HOLDS.** The weight is a product of nearest-neighbour bonds on four compact spins per site. Translations and axis permutations act on sites and spin types together. Reversing an axis preserves the bond weight since $p(g^{-1}h)=p(h^{-1}g)$. This gives hypercubic symmetry. For a bond reflection normal to $\mu$, factor each crossing heat kernel on both seams as $C_a^{1/2}C_a^{1/2}$. Given the intermediate Haar spins, the integrals of a half-torus test and its reflected conjugate multiply to an absolute square. For a site reflection, conditioning on the fixed slices gives the same square with their positive boundary weight. This proves coordinate reflection positivity in every transfer direction. LS(a) gives the required simple finite-volume vacuum.

**The equivalence for the spin trace — HOLDS.** There is even a direct propagation proof. If $n,u$ pass then $n^3[Z_{\rm line}(u)-1]\le1/2$ and $e^{-\varepsilon u}\le1/(8n^3)$. For any integer $h\ge2n$, put $q=\lfloor h/n\rfloor$. The time $qu$ is admissible at $h$. Each nonconstant line eigenvalue is at most $e^{-\varepsilon}$, hence
$$
 h^3\log Z_{\rm line}(qu)
 \le \frac{(q+1)^3}{2}(8n^3)^{-(q-1)}
 \le \frac{27}{16n^3}<\log(3/2).
$$
The middle bound takes $q=2$ because the majorant decreases for $q\ge2$, $n\ge3$. Thus every side $h\ge2n$ passes. If $a_j\nu_j$ is bounded on a tail, choose one admissible physical grid side at least twice that bound. It passes on the whole tail. Conversely, a common passing $L$ gives $a_j\nu_j\le L$ by minimality. This works also with $\nu'_j$ on the grid. On the fixed-$m$ family **both** sides of that equivalence are false, while the seed exists separately at every coupling.

**Independence, lines 125–128, 178–183 and 217–220 — HOLDS AFTER CORRECTION of scope and direction.** The example proves $(a)\nRightarrow(b)$ among these local, hypercubic, reflection-positive spin families, even with fixed physical gap $m$. With a missing seed assigned $\nu'_j=\infty$, (b) itself implies eventual (a). Two-way logical independence therefore **FAILS**. The restricted assertion that (b) is an extra requirement beyond (a) holds.

| Source at the pin | Verdict and hypothesis comparison |
|---|---|
| Row 1161, lines 17–23, 44–46, 146–150, 215 and 335 | **HOLDS** as a comparison of the ordinary thermal test. A literal Wilson application **FAILS**. This row uses a gauge-projected plaquette transfer, the three electric centre flips and the magnetic twists, with sector energies in units of the periodic vacuum. The spin trace has none of these Wilson identifications. Its short-period bound holds at a fixed coupling on large enough cubes and fails along the cutoff at every fixed side. The Wilson implication starts with that bound. [Row 1161](gap-solve9-astra62.md) |
| Row 1179, lines 174–191, 253–259 and 304–324 | **HOLDS** that LS leaves Theorem BP intact. BP assumes (TM-tw), (S) and the cutoff-uniform neutral bound. Ordinary trace and shape identities are available for the spins. The Wilson twisted family and its centre-blind observable algebra are additional data, and the spin version of the uniform bound is false. The continuum statement also reads matched reflected correlators, totality and time continuity. LS supplies no instance of those identifications. [Row 1179](gap-mini-branch-fable.md) |
| Row 1180, lines 35–52 and 95–114 | **HOLDS** for the full-trace counterpart proved above. A claim of non-implication *within pure Wilson SU(2)* **FAILS as a deduction from this example**. The reverse implication in the cited Wilson equivalence uses the Pfaffian seed, S-w and B3 to reach a common side. The spin proof reaches a common side directly. The integer, divisibility and grid constraints can all be met. [Row 1180](gap-mini-neutral-fable.md) · [Row 1187, lines 25–44](gap-neutral-pair-check-astra.md) |

There is an explicit test of the Wilson domain restriction. Treat the four site spins as outgoing links and start with all links equal to $1$ on a torus of side at least four. A Wilson gauge transformation equal to $-1$ at one site and $+1$ elsewhere flips the incoming and outgoing links there. On each of four lines this leaves two adjacent negative spins between positive spins, replacing two $p(1)$ bonds by $p(-1)$. The weight changes since $p(1)-p(-1)=2\sum_{d\in 2\mathbb N}d^2e^{-\varepsilon(d^2-1)/3}>0$. The Wilson action is invariant under that transformation. One may take the trivial sector action in the spin comparison, so its neutral projection is the identity. The upper bound of a sector trace by the full trace at line 107 only passes *smallness* to a sector. For example, projection onto the vacuum commutes with $U$ and has zero excited trace at every side, even when the full trace diverges. For a group acting solely by constant central signs on whole spin lines, the $d=3$ coefficients on each time line are even. Its invariant trace still has an excited contribution of at least $9n^3 e^{-(8/3)\varepsilon u}$. This optional spin projection has its own symmetry action.

## The two readings

**Ultraviolet count, lines 159–167 and 221–225 — HOLDS for the model.** There are $4n^3$ orthogonal states at the single energy $m$, or $4/a^3$ states per unit physical spatial volume. The divergence counts multiplicity. Put $x=mL=\varepsilon n$ and $\ell(x)=\log[1+\sum_{d\ge2}d^2e^{-x(d^2-1)/3}]$. On a symmetric torus $F_a(n)=4n^3\ell(x)$ and the pressure $\lim_{n\to\infty}F_a(n)/n^4$ at fixed $a$ is zero. Thus $D_a(n)=4n^3\ell(x)$. For any integer enlargement $r\ge2$,
$$
\Phi_r(n)=r^4F_a(n)-F_a(rn)
         =4r^3n^3[r\ell(x)-\ell(rx)]
         \ge4r^3(r-1)n^3\ell(x).
$$
At $r=2$ this gives exactly line 166. At fixed $L$ both excesses are positive constants depending on $mL$ times $n^3$. For $x\ge3$, $\log(1+4e^{-x})\le\ell(x)\le4.1e^{-x}$ gives the stated large-$mL$ dependence. At fixed coupling and $n\ge3/\varepsilon$, $D_a(n)\le16.4 n^3e^{-\varepsilon n}\to0$. The two orders of limits have different answers.

**Attribution to the cutoff comparison, lines 164–170, 221–226 and 233–235 — HOLDS AFTER CORRECTION.** On the sequence $a\mapsto a/2$ at fixed $L$, $\Phi_r$ increases by a factor eight at each step. This rules out summable upper increments of the *physical defect*, and a decomposition into a part with summable increments plus a uniformly bounded remainder. The spin measure specifies no chapter 9 stop part. For example, writing $\Phi_r=0+\Phi_r$ gives a first term with identically zero increments. Divergence alone does not locate the failure in that first term.

For Wilson, row 1233, Proposition 3.7, gives a **conditional** route. As corrected by row 1242, use matched first-passage edges on both tori, consistent stop representatives, and either the physical normalization or a bound on the change of its relative two-torus defect. If $P$ has successive upper increments $b_i$ with finite sum, the counterterm defect is bounded in absolute value by $\eta$, and the remaining normalization defect grows by at most $\sigma$ from base to endpoint, telescoping gives
$$
 \Phi(d)\le\Phi(d_0)+\sum_{i=K_0}^{K-1}b_i+2\eta+\sigma .
$$
The first edge counts. One needs the base inequality with this margin for every base datum reached by the chosen chains. The all-data version includes every datum at $K_0$. A seed at one arbitrary coupling or some unspecified size does not establish this premise. The physical matching, determinant and last-lattice comparison inputs, including the outstanding blind-site expansion, are conditions of that route. A direct uniform Wilson trace estimate could establish (b) by another argument. Lines 169–170 and 233–235 give no necessity theorem for the account's particular comparison method. [Row 1233, clauses 3.5–3.7](gap-mini-solve-u-opus.md) · [Row 1242, lines 52–70](gap-onek-check-astra.md) · [Base-set quantifiers](gap-chain-ce-check-astra.md)

**Fixed-coupling count, lines 171–176, 199–206 and 227–229 — HOLDS with the sector specified.** Row 700's (NS-gap) concerns the **ordinary periodic Wilson** spectrum at one $\beta$. Assume the cubes of side $2n$, on an infinite set of $n$, have logarithmic gap $m_0>0$ or larger. The proposed conclusion is that some $0\le\theta<1$ and $A_n>0$ satisfy
$$
 N_{2n}(E)\le A_n e^{\theta n E}\quad(E\ge m_0),
 \qquad \liminf_n n^{-1}\log A_n<(1-\theta)m_0 .
$$
Here $N$ counts excited eigenvalues with multiplicity and the lower limit is along that set. Integrating each excited Boltzmann factor gives $S(n)=n\int_{m_0}^\infty N_{2n}(E)e^{-nE}\,dE\le A_n e^{-(1-\theta)nm_0}/(1-\theta)$. This yields an ordinary thermal seed on a subsequence. Row 700, N3, makes this a sufficient converse input. The seed-to-gap direction uses the finite-volume propagation hypotheses. If only a centre-neutral gap is given, the count must be supplied on the trace and time scale being tested, or linked to it by a proved comparison. In particular, a neutral seed gives a centre-even gap in row 1179. Row 1161, (22), allows two branches, only one of which is the ordinary periodic seed. [Row 700, lines 212–234](gap-seed-limit.md) · [Row 1161, lines 325–335](gap-solve9-astra62.md)

For the spin model one can verify the count itself. Fix $\varepsilon>0$ and take $\theta=1/2$. On a cube of side $2n$ every excited energy $E_i\le E$ contributes at least $e^{-nE/2}$ to $S(n/2)$. The explicit spectrum makes this trace finite also at real positive time. Hence
$$
 N_{2n}(E)e^{-nE/2}\le S(n/2)
   =Z_{\rm line}(n/2)^{(2n)^3}-1\longrightarrow0 .
$$
For the last limit, LS(b) bounds its logarithm $\log(1+S(n/2))$ by $4.1(2n)^3e^{-\varepsilon n/2}$ for large $n$. Thus $A_n=\max\{1,S(n/2)\}$ is eventually 1, and $0<\varepsilon/2$ is the strict margin. The fixed-coupling conclusion of the spin analogue of (NS-gap) holds. It poses no counterexample to the Wilson conjecture.

**The three attributions, lines 85–89, 171–173 and 227–229 — HOLDS AFTER CORRECTION.**

- **Row 1225, lines 133–151 and 190–192.** Line 137 derives a centre-neutral fixed-coupling gap. Line 139 starts the other implication from a **seed** with a carry. Those implications leave a gap-to-count step between them. The summary at 148 needs the finite-volume trace qualification. [Row 1225](gap-mini-solve-r-fable.md)
- **Row 1233, lines 119–126 and 147.** The phrase “equivalently the lattice gap” at 126 and 147 needs the count in the correct sector, matching of the seed to the prescribed two-torus defect, and the base margin just described. The proposed (NS-gap) is a fixed-coupling input. It cannot by itself transport a seed across cutoffs or match every base datum. [Row 1233](gap-mini-solve-u-opus.md)
- **Row 1238, lines 25–26, 39–42, 251 and 277.** The blanket attribution to this row **FAILS** at 41–42. It explicitly says “with a finite seed” and keeps the carry separate at 25–26 and 39–40. The later shorthand at 251 and 277 identifies (N-phys) with a seed at one coupling. Restore the conditional carry and its base quantifier there. [Row 1238](gap-mini-solve-x-opus.md)

**The $m_0/64$ criterion, lines 185–206 — HOLDS as a sufficient condition.** The prior derivation in row 727, line 106, takes $n=2a$, $\theta=1/2$, $A_n=\exp(64D(a))$ in N3, using the excited-trace bound on the cube of side $4a$. Its lower-limit condition becomes exactly $\liminf_a D(a)/a<m_0/64$, as in row 720, Corollary Z2. Row 1234's all-large-sides bound with $c<m_0/64$ is stronger as a premise.

To check lines 187–193 directly, take even $b$, put $t=b/2$, and write $x(t;C)=\log(1+S(t;C))$ on a cross-section $C$ of a one-direction doubling. Monotonicity of log partition function per site gives $F(t,C)-f t|C|\le (|C|/t^3)D(t)\le64D(t)$, where $f$ is the bulk pressure. Sending the time length to infinity in that same monotonicity gives $\log\lambda_0(C)\ge f|C|$, so $x(t;C)\le64D(t)$. The assumed gap on each of these rectangular sections gives $x(b;C)\le S(b;C)\le e^{-m_0t}S(t;C)$. Each doubling costs $2x(b;C)-x(2b;C)\le2x(b;C)$, with successive weights $8,4,2,1$. Hence $\Phi(b)\le30e^{-m_0b/2+64D(b/2)}$. Telescoping $16D(b)-D(2b)=\Phi(b)$ has zero limiting remainder since $D(h)/h^4\to0$. If $D(t)\le ct$ on a tail, it gives $D(b)\le2e^{-(m_0-64c)b/2}$ on even sides there. Monotonicity of $D(h)/h^4$ extends exponential decay to the intermediate odd sides. The converse from the gap alone for Wilson remains open. [Row 727](gap-phys-seed-check.md) · [Row 720, lines 306–309](gap-phys-seed.md)

RESULT: Proposition LS HOLDS for the spin trace with the printed bounds after the proof repairs in (c) and (d). The exact physical gap and finite seeds coexist with failure at every fixed physical side. This proves the one-way non-implication (a) ⇏ (b) in the comparison class. The Wilson fixed-coupling count, the physical cutoff comparison, (N-phys) and the Yang–Mills mass gap remain open.
