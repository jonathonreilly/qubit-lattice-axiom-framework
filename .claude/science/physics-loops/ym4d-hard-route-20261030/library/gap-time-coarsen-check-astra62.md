# Repo search

Row 1401. OpenAI Codex, assigned gpt-6.2-astra xhigh, reading Claude Fable 5.2 medium's row 1396 at `ec4075dfcdeb4df468982f37418d0b52f2e0c874`. This is a research check and grants no status. Unqualified line numbers refer to [row 1396](gap-time-coarsen-fable.md).

Searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). Time coarsening, geometric time decimation, neutral grid comparison, zero-gain carry, (M-neutral), and centered insertion near “vacuum” returned no lines. Searches on the methods found these precedents.

- **Main.** `research/mass-gap/library/gap-crux-restate.md` 192–203 gives $S'\le[(1+S)^{64}-1]^2$, a full-trace contraction from $0<S<1/5041$. In the same directory, `prior/gap-vir-lit.md` 31 reports Karsch's weak-coupling derivative sum at isotropy, and `gap-vir-sc.md` 200 leaves the band anisotropy response open.
- **PRs 10114 and 10133.** `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–138 gives $\bar K_B W_C=r_f^{|C|}W_C$ and a rank-one lower bound for a centred simple loop. This supplies an electric eigenfunction. It compares no excited traces.
- **Lane.** [Check 1393](gap-dim-carry-check-astra62.md), 65–77 and 122–132, proves (1) near Haar on each fixed box and proposes the centered derivative. Row 863 §3.2 and check 879 give END's count at $P=1$. Row 1145 (22) seeds a strip at fixed temporal coupling. The November 8 search digest covers earlier construction and witness problems. Row 1401 has no target-specific prior or separate “Repo prior work” entry. The registry's TC-DILATION concerns a holomorphic layer response (CA-II 13933 ff.). No other owner of this check surfaced.
- **Sussman–Alpoge and Bałaban.** At the supplied snapshot `31a47c543775`, outline index chunks 02 and 06 and the obligations locate GL3–4 and GL8 (2195–2227, 2241–2257, 2313–2335), the positive electric multipliers and gauge-projected transfer trace. Lines 7008–7014 concern an ultraviolet plane-weight derivative. CA-III 68448–68524 changes units on one bare lattice. CA-I 2699–2713 leaves the mass gap outside Theorem 0. Bałaban's CMP 122b Theorem 1 assumes the small-coupling sequence (`lit-balaban.md` 147). Credit the outline and account to Sussman and Alpoge with Claude and Codex.

**Verdict — HOLDS AFTER CORRECTION.** Close check 1393's time-coarsening line with no proof row for (M-neutral). USE establishes that this comparison alone supplies neither first entry nor a coupling increment. Its gain version gives a forward implication on matched grids. The converse claimed at 215–217 does not follow. Inequality (1) in the band remains open.

## Saved plan (completed)

Read the target-specific prior first, then the goal and requested finish rules. Check the registry, repository refs, index and cited primary sources before deriving. Record the evidence and verdict for each item in order.

1. Proposition USE (b) through (e).
2. Lemma END, including the vacuum bound, pointwise cancellation and the A2 count.
3. The constant in Proposition CHAIN.
4. Proposition FREE.
5. Lemma KER (b).
6. The gate table in §3.2, then the guide in §3.1. Distinguish recalled input from derivation.
7. Rank any defects, identify the first failing line and give the disposition of check 1393.

## Proposition USE, in the requested order

With $q=\lfloor n/1024\rfloor$, write $I(n,b)=s_{n^3}(2q;b,b)$ and $A(n,b)=s_{n^3}(q;2b,b/2)$. Here $s_B(t;b_s,b_t)=\sum_{a\ge1}(\lambda_a/\lambda_0)^t$ uses the vacuum at those very couplings. Inequality (1) asks for $I(n,b)\le A(n,b)$ at $b\in[2.3,2.6]$ for all sufficiently large $n$ divisible by four. The threshold for (M-neutral) is $s_*=4/21$ in zero spatial twist after the electric centre projection. Row 1367 requires one admissible physical side with the estimate at **every** sufficiently late cutoff. [Row 1367, §§1–2](gap-seed-astra62.md)

**(b), 196–201 — HOLDS on the common range.** For $n=1024\,2^m$, $m\ge1$, both $A(n,b)$ and $I(n/2,b)$ use $2^m$ steps. Assuming (1) and (R) there gives $I(n,b)\le A(n,b)\le I(n/2,b)$. Iteration is valid down to any base for which every intervening link is covered. “All large $n$” in line 38 does not license the last link down to an arbitrary small base. Spatial transport is an additional hypothesis. Theorem S compares two full isotropic traces at a different aspect ratio. It does not prove (R), even below its own threshold. Its bound holds for all seeds in its domain, but gives the cited strict contraction only in its small-seed range. [Theorem S, row 697](gap-crux-restate.md)

**(c), 203–206 — HOLDS for the no-rate conclusion.** Every arrow from (b) stays at $b$. A chain starting at $\beta_w$ cannot supply a seed at any $b>\beta_w$. Abstractly, assigning both sides the same number $h(b)$, small at $\beta_w$ and large above it, satisfies all the zero-gain comparisons. This tests exactly the logical inference. Theorem T actually requires $5041S(N;(2N)^3;b)\le q_0<1$ for the **full** trace, with $N\le C_1e^{c(b-\beta_w)}$ and $c<C_*=(\log L+\tfrac14\log(1/q_{\rm UV}))/\kappa$. A uniform increment $\delta$ per doubling gives the exponent $\log 2/\delta$ on its iteration ladder. Line 205's $0.173$ uses the guide $C_*\simeq4$ and is no exact lower bound in Theorem T. [Row 1332, 152–181](gap-shrink-box-fable.md)

**(d), 208–211 — HOLDS for no entry, with a domain correction at 208–209.** The assignment in (b) concerns dyadic sides in the band. An admissible $n_j$ in row 1367 need only be divisible by four, and $\beta_j$ need not be in the band. Even **granting** extension along all the proposed halvings at $\beta_j$, the right endpoint still needs a seed at that very coupling. On a fixed periodic box every fixed-index neutral ratio tends to one as $b\to\infty$ by row 1215 (5). Taking arbitrarily many fixed indices gives divergence at each fixed positive time. Row 1227 (11) bounds the first neutral energy above by $C_n b^{-1/4}(1+\log b)$. Neither statement decides a growing base $n_j/2^k$. The existing neutral enlargement from (N-phys) also requires a seed. No named consumer obtains first entry or the coupling rate from the zero-gain comparison alone. [Row 1215](gap-solve23-astra62.md) · [Row 1227](gap-solve25-astra62.md) · [Check 1355, 55](gap-mini-neutral-step-check-astra.md)

**(e), 213–219 — HOLDS AFTER CORRECTION for the forward implication. The asserted equivalence FAILS.** The shift needed for composition is $A(n,b+d')\le I(n/2,b)$. Apply $(1_d)$ at $b+d'$ to get $I(n,b+d'+d)\le A(n,b+d')\le I(n/2,b)$. Both premises must cover the intermediate coupling. This transfers **any given neutral threshold** across this pair of grids. The first unjustified identification is line 215, “This is (STEP)”. The general step needs its coupling and size range, its seed and a sufficiently large total increment. One $d+d'>0$ on dyadic sides in a window does not supply these. Iterating one increment from one base only covers its coupling ladder without a separate interval argument.

Lines 216–217 also lack the converse. A threshold bound along a trajectory implies no ordering of two excited sums below threshold and gives no value at the anisotropic midpoint. Even if all isotropic sums were $s_*/2$, freely choosing the intermediate value either side of $s_*/2$ would preserve every isotropic seed and could violate a directional comparison. This separates the logical data, without purporting to construct another Wilson theory. The consistency remark cited via row 1386 §4.1 gives an **existential** size bound on first-passage data, with rate fit under an extra pinching condition. It gives neither the directional quotient order nor a uniform step from each seed. The figure $d\simeq0.064$ is a matching heuristic. [Row 1386, 269–282](gap-mech-direction2-fable.md) · [Row 1332, 179–181](gap-shrink-box-fable.md) · [Check 1335, Theorem T](gap-shrink-box-check-astra.md)

**Disposition of check 1393.** Close its time-coarsening line as a proof task for (M-neutral). The implications needed for that decision, (c) and (d), survive. Inequality (1) itself stays open in the band. The failure of the converse in (e) removes an equivalence claim about *positive* gains. It supplies no consumer of a zero-gain carry and no next proof row.

## Lemma END — HOLDS AFTER CORRECTION

**Full-space bound, 85–101 — HOLDS.** Use probability Haar and $P\ge0$ nonzero as an $L^\infty$ class, so $Z_P=\int P>0$. On the constants $K_b=1$, and its restriction to their orthogonal complement is positive by the Bessel spectrum. Thus $K_b\ge|1\rangle\langle1|$. Conjugating gives $T\ge|\sqrt P\rangle\langle\sqrt P|$ and $\lambda_0\ge Z_P$. This also verifies the Rayleigh quotient at 92–93 with exactly the stated normalization.

In the projected diagonal kernel at 94–96 fix *every* link field $U$. For a leaf $x$ the only nonconstant factor involving $g_x$ is $f(a g_x^{-1})$ or $f(a g_x b')$, with all other variables held fixed (cyclic conjugation is harmless). Inversion and translations preserve Haar, so its integral is $\int f=0$. The character bound $|\chi_j|\le 2j+1$ gives $|f|\le\epsilon$. Every surviving component has minimum degree two, hence contains a cycle. A simple cubic torus of side lengths at least four has no cycle of length below four.

The count is imported from row 863 §3.2 and explicitly justified in check 879. The link adjacency graph has maximum degree ten. For a fixed root link, the labelled-tree bound for $m\ge4$ links is $10^{m-1}m^{m-2}/(m-1)!\le(10e)^{m-1}$ (use $m!\ge(m/e)^m$ and $m\ge e$). Summing over $3|B|$ roots overcounts. Dropping exclusions between distinct components gives an upper bound by the exponential of the sum of absolute component weights. Its exponent is bounded by
$$
3|B|\sum_{m\ge4}(10e)^{m-1}\epsilon^m
=\frac{3|B|(10e)^3\epsilon^4}{1-10e\epsilon}
\le 6|B|(10e)^3\epsilon^4 .
$$
This bound holds before integration over $U$, the extra fact needed for arbitrary $P$. The positive trace equals $\int P(U)K_b(U,U)\,dU$ by the squared-kernel factorization of the electric trace, also for bounded measurable $P$. Divide by $\lambda_0$ and remove the vacuum. Finally $\epsilon=k_b(1)-1=e^b/\int e^{bx}-1\le e^b-1\le2b$ in the stated range, by $\int x=0$, Jensen, and the exponential series. The Bessel-series upper bound in line 100 also follows by comparing factorials term by term. [Row 863, 148–153](gap-crux-skeleton-max.md) · [Check 879, 29–39](gap-crux-skeleton-check-astra.md)

**Neutral clause, first failing line 91, used at 99.** Gauge invariance alone does not preserve the neutral subspace. If $W$ winds once around a spatial cycle, $P=1+\operatorname{tr}(W)/4$ is positive and gauge invariant. The corresponding centre flip reverses the trace. At $b=0$, $T=|\sqrt P\rangle\langle\sqrt P|$ maps the neutral constant out of the neutral space. The failure persists for small positive $b$ by norm continuity of the integral kernels. Require invariance of $P$ under all electric centre flips for the neutral restriction. Then the positive top eigenfunction on the essential support of $P$ is simple (the electric kernel there is strictly positive), and each flip fixes that normalized positive function. Projection keeps the vacuum and deletes nonnegative spectral terms. Every Wilson plaquette weight used in CHAIN satisfies this condition. The extension in 102–103 needs a normalized positive-type convolution and a summable nonconstant character majorant on the chosen compact group, and the graph count for the chosen dimension.

## Proposition CHAIN — bound and constant HOLD

Lines 107–116. Write $2q=2^K=n/512$. At each link the step count halves. At the terminal link $b_t=\beta/(2q)$ and the Wilson spatial factor with $b_s=2^K\beta$ preserves the centre. Hence $\epsilon\le2\beta/(2q)$ and $10e\epsilon\le1/2$ under line 109. END gives line 111 with coefficient $6\cdot2^4=96$. The last power is $n^3/(2q)^4=512^4/n$. For a hand bound use $e<11/4$, $96(55/2)^3<2\cdot10^6$ and $512^4=2^{36}<7\cdot10^{10}$. Their product is strictly below $1.4\cdot10^{17}$. When $n\ge10^{18}\beta^4$ and $n\ge1024$, $512\beta/n\le512/(10^{4}n^{3/4})<1/(40e)$. The exponent is at most $7/50$, and $e^{7/50}-1\le7/43<4/21$. Thus the conditional polynomial-size **neutral** seed holds on the indicated dyadic sides.

**First failing interpretation, 117–118.** A polynomial size bound allows $C_c e^{c(\beta-\beta_w)}$ for **each fixed $c>0$**, with $C_c$ depending on $c$. Setting $c=0$ would require a uniform bound on size. This is actually excluded for a nonvacuous seed at arbitrarily large $\beta$ by row 1215 (5), applied to the finitely many candidate sides and their fixed times. Also (A2) uses the full trace, a specified margin and a different aspect ratio. CH assumes comparisons only in the neutral sector. The printed argument reaches the polynomial neutral seed on the dyadic family. Identifying it directly with (A2), or with every admissible cutoff in (M-neutral), needs additional sector or size arguments. Lines 120–125 give a conjectural failure of CH at $n$ of order $\beta^4$. Even row 1215's joint-limit (19) assumes $\beta\ge n^{32}$, disjoint from that proposed witness regime at large $\beta$.

## Proposition FREE — HOLDS for the physical transverse modes

Lines 69–81. Work on the gauge-reduced Gaussian space with the flat constant modes removed. If line 72 is read on *all* real link variables, nonconstant longitudinal gradients also have zero curl and require projection or gauge fixing to obtain this oscillator trace. For a nonzero transverse momentum put $h=|\hat p|$, $a=b_t+b_sh^2/2$, $v=b_t$, $\gamma=\sqrt{a^2-v^2}$. The kernel is $\exp[-a(x^2+y^2)/2+vxy]$. Integrating it against the Hermite generating function $e^{-\gamma y^2/2}\exp(2\sqrt\gamma yz-z^2)$ gives a constant times the same function at $x$ with $z$ replaced by $rz$, $r=v/(a+\gamma)$. Thus the complete oscillator levels divided by the vacuum are $r^k$, $k\ge0$, and $\cosh(-\log r)=a/v$.

Set $x=(b_s/b_t)h^2>0$. Then $\cosh(2\omega)=1+2x+x^2/2>1+2x=\cosh\Omega$. Each occupation on the fine side has weight at most its coarse counterpart, strictly less for positive occupation. Multiplication over real modes and summation over nonvacuum occupations prove the trace inequality at every halving. At the first step $2\omega=4\operatorname{arsinh}(h/2)$ and $\Omega=2\operatorname{arsinh}h$, giving $(2\omega-\Omega)/(2\omega)=h^2/8+O(h^4)$. This is the relative difference of frequencies. It proves the splitting sign for the free model. No estimate for the interacting splitting at band coupling follows.

## Lemma KER (b) — HOLDS

Lines 54–62. One can check the coefficient without a Bessel table. By GL3 and the fundamental character, $u=I_2(b)/I_1(b)$ is the tilted SU(2) mean of $x=\operatorname{tr}U/2$. With $t=1-x$ the density is proportional to $e^{-bt}t^{1/2}(1-t/2)^{1/2}$ on $[0,2]$. Expand the last factor as $1-t/4+O(t^2)$ on $[0,1]$. The remaining interval is exponentially small, and the integral of the error is bounded by the corresponding gamma moment. Dividing the first moment by the zeroth gives
$$
1-u=\frac{3}{2b}\frac{1-5/(8b)+O(b^{-2})}{1-3/(8b)+O(b^{-2})}
=\frac{3}{2b}-\frac{3}{8b^2}+O(b^{-3}).
$$
Thus $u(b)^2-u(b/2)=3/(2b^2)+O(b^{-3})$ and $-\log u(b)=3/(2b)+3/(4b^2)+O(b^{-3})$. The relative excess of $-\log u(b/2)$ over $-2\log u(b)$ is $1/(2b)+O(b^{-2})$. Line 58's “wider” has this precise meaning for the fundamental multiplier. For U(1) the corresponding factor is $t^{-1/2}(1-t/2)^{-1/2}$, giving $1-u=1/(2b)+1/(8b^2)+O(b^{-3})$ and the log in line 59. The equalities at 56 and 59 are asymptotic to the displayed orders. The opposite small-$b$ sign follows from $u(b)=b/4+O(b^3)$, so continuity ensures a crossing. Its location and the tabulated values at 63–66 are guides. The sign for one representation does not compare the interacting neutral traces.

## Gate table §3.2 — HOLDS AFTER CORRECTION

Read each test as posed in row 1386 §4.5. Row 1396 explicitly grades the SU(2) and U(1) predictions as guides. The first pass lacking a proof is line 172. The Hartree assumptions explain its proposed abelian sign, while the five-dimensional discussion leaves even the sign unspecified. [The filter and Remark PAIR](gap-mech-direction2-fable.md)

| Row and lines | Checked verdict |
|---|---|
| (t1), 172 | **Open for the Wilson quotient.** The abelian one-loop running coefficient vanishes. That passes the group check on that coefficient. The sign of the compact U(1) trace at finite anisotropy, much less its sign across the band, requires additional input. Even FREE gives a strict finite-momentum difference at zero interaction. |
| (t2), 173 | **Open.** The absence of the four-dimensional running logarithm leaves the five-dimensional quotient sign undetermined. A single temporal change multiplies the two types of bare weight by the same factors $2,1/2$ in either dimension. The filter tests the *composite* step. |
| (t3), 174 | **HOLDS as a compatibility check.** The comparison can be formulated for SU(3) using its centre projection, and the putative nonabelian coefficient is present for SU(3). Neither observation proves its trace comparison. |
| (t4), 175 | **Inapplicable to the band-only one-step question as a seed trigger.** Fixed side and $\beta\to\infty$ leave its stated domain. On extending the question, row 1215 (5) proves divergence of the fixed-side isotropic sum but gives no ordering against its anisotropic counterpart. At fixed $n$, END's hypothesis for the last link of CH also eventually fails. The proposed failure at a *growing* side is a separate conjecture. |
| (t5), 176 | **The bare comparison fails to supply a proof of the seed. Equivalence is unproved.** See USE (e). Nonnegativity of the centered derivative at *each* interpolation point is a sufficient test. Its *integral* is the endpoint log ratio, up to the factor $q$. Line 176 equates the two tests. For example with $q=2$ take endpoints $\mathrm{diag}(1,1/2,1/8)$ and $\mathrm{diag}(1,1/8,3/4)$. The vacuum stays 1, the trace $\operatorname{Tr}(H_z^2)$ increases between the endpoints, yet its derivative at zero is $2[-3/16+5/64]<0$. This tests the logic of the interpolation. It is no Wilson counterexample. [Check 1393, 124–130](gap-dim-carry-check-astra62.md) |

**PAIR, 178–184 — HOLDS only for the bare-coupling bookkeeping.** If all four comparisons exist and compose as in (R), they return to an isotropic grid at the same four-dimensional bare coupling. Their conclusion is $I(2n,b)\le I(n,b)$ on the common range. PAIR's $x$ is a *running inverse coupling*. Lines 181–182 identify a trace order with $x(2L)\le x(L)$ without a definition and order comparison connecting these observables. Equal bare endpoint couplings do give zero **bare increment**. Inferring the sign of a physical gain from this quotient would require a further theorem.

## One-loop guide §3.1 — conditional algebra HOLDS, spectral signs are OPEN

**Input at isotropy, 129–134.** Karsch's weak-coupling matching for a fixed $3+1$ anisotropy and the isotropic derivative sum $c'_\sigma(1)+c'_\tau(1)=b_0=11N/(48\pi^2)$ are literature inputs. The SU(2) derivatives $0.11403,-0.06759$ were recalled by row 1066. Row 1067 subsequently recorded them from Karsch's paper. Neither derivative gives $c_i(1/2)$. No value of those finite-asymmetry coefficients was verified here. [Row 1066, 62](gap-aniso-trajectory.md) · [Row 1067, 23](prior/gap-aniso-read-luna.md)

**Derived under matching, 135–145.** Write $G=g_{\rm eq}^{-2}$, $\xi_0=1/2$, and let $\xi$ be the matched $a_s/a_t$. Equate $\beta/\xi_0=4(G+c_\sigma)/\xi$ and $\beta\xi_0=4\xi(G+c_\tau)$ to one-loop accuracy. Multiplication gives $4G=\beta-2(c_\sigma+c_\tau)+O(\beta^{-1})$. Division gives $1/\xi=2[1+2(c_\tau-c_\sigma)/\beta+O(\beta^{-2})]$, with the coefficients evaluated at $1/2$ to this order. These are the algebraic contents of line 138.

**First unsupported finite-step inference, 140–145.** The quarter-step is obtained by *postulating* $c_i(\xi)=c'_i(1)\log\xi$ down to $1/2$, or at least this law for their sum. It gives $\Delta\beta=2b_0\log2$, a quarter of $8b_0\log2$ for SU(2). Adding $C(\log\xi)^2$ preserves the derivative sum at one and changes the finite shift by an arbitrary amount. Thus the geometric-mean cutoff and $2^{-1/4}$ size ratio are extrapolations. Line 145 uses linearity in $\xi$ for the *difference*, giving a shape coefficient $c'_\sigma-c'_\tau\simeq0.182$ in $1+0.182/\beta$. Using log-linearity for both coefficients gives $2(c'_\sigma-c'_\tau)\log2\simeq0.252$ instead. Using $\xi$-linearity for both gives $\Delta\beta=b_0$. The $0.90$ estimate at 151 mixes the two continuation choices. Neither the predicted margin nor its sign at band coupling is data from Karsch.

| Guide | What the argument supports |
|---|---|
| S1, 148–154 | If the two lowest neutral energies converge to $m_F,m_D$ and the logs of the excited multiplicity factors $\sum_{a\ge1}e^{-t(E_a-E_1)}$ are $o(n)$ at the relevant times, then $m_D<2m_F$ suffices for eventual (1), and eventual (1) implies $m_D\le2m_F$. A gap alone supplies no such count. The scale law, matching and $5$–$16$ percent margin are predictions. |
| S2, 155–157 | A smaller matched spatial box and a weaker coupling in box units do not determine two complete normalized spectra. The physical time aspect also changes. There is no derived sign here, at fixed lattice or growing lattice. |
| S3, 158–165 | The quoted Hartree plaquette averages and the compact-U(1) finite-volume trace response were not derived in row 1396. If the reductions of the effective couplings are $1-0.155/\beta$ and $1-0.38/\beta$, their square-root ratio gives a *conditional* relative frequency shift $(0.38-0.155)/(2\beta)$ to first order. Comparing with FREE requires $h^2/8$ below that shift, a scale of order $1/\beta$ without the asserted sharp cutoff. Extending a low-mode calculation to the whole compact neutral trace needs control of the remaining states and errors. Check 1393's fixed-box near-Haar sign is a different, proved regime. |
| S4, 166 | The four-dimensional logarithmic mechanism is absent in the five-dimensional power counting used by PAIR. This gives no ordering of the two five-dimensional spectra. |

**Overall guide verdict.** The sign predictions remain guides. Calling the statement selective in lines 232–239 exceeds what the table establishes. The free sign and the fundamental electric multiplier test two different models or factors. Their signs do not combine into a band estimate for the Wilson quotient at lines 223–228.

## Defects ranked by what they break

| Rank | First line | Consequence |
|---|---:|---|
| 1 | 215 | The shifted composition gives a directional neutral seed implication. Its identification with the full rate-qualified STEP and the converse from the target at 216 do not follow. |
| 2 | 117 | CH supplies a polynomial-size dyadic neutral seed. Line 118 substitutes the full-trace hypothesis (A2) and sets its exponential rate to zero, which would require bounded size. |
| 3 | 91 | END needs electric centre invariance for its neutral restriction. Its full-space estimate and the Wilson application survive. |
| 4 | 208 | Applying the dyadic band comparison directly to an arbitrary late cutoff exceeds its domain. Even the extended comparison needs entry at the new coupling. |
| 5 | 181 | Identifying the neutral trace order with an order on PAIR's running stiffness requires a separate comparison. |
| 6 | 176 | A pointwise sign along the interpolation is stronger than its integrated endpoint test. |
| 7 | 140 | The finite anisotropy, spectral estimates and selectivity calls at 148–175 exceed the isotropic derivative data. This also affects the reported numerical margin and the fixed-side trigger test. |

**RESULT — Row 1401. HOLDS AFTER CORRECTION.** Checked line by line by Codex. In the requested order, the first application outside the hypotheses is USE (d), lines 208–209. The first failed identification of the gain step is USE (e), line 215. USE (c) and the no-entry conclusion of (d) hold. Close check 1393's time-coarsening line with no further proof row for the neutral seed. The band inequality (1) and (M-neutral) remain open. The check uses written hand arguments. No numerical or Lean computation was used as a proof step.
