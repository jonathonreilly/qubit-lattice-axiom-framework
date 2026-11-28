> **Status:** COMPLETE. Research proof check, not an audit; grants no status.
> Checker: Codex, assigned Astra/high in row 699; no model-setting change made.
> Source: `87508843b17d6b00f3f4afe7c7d365b41259c8f8`, 2026-11-11.
> Author checked: Claude Fable 5.2, row 697. This checker wrote none of that text.
> Completed points: 1–9, saved in order. Theorem S holds conditionally;
> S3 needs the replacement proof below. No seed or mass gap is proved here.

# Repo search

The task-specific `prior/gap-seed-check-astra.md` is absent. The lead's
`prior/repo-search-2026-11-08.md` records searches of main and PRs 10114,
10133, 10134 and 10141. Its closest named hit is the earlier Codex/Astra
`MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 106–149, under
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` on PR 10114.
I fetched that PR and read those lines: they concern a positive one-step
loop correlation, not the thermal doubling criterion. I also read
`MASS_GAP_CONSTRUCTION_ASTRA.md`, lines 1–215, identified by the correction
table of `gap-transfer-check.md`. Its explicit Wilson transfer and simple
vacuum are prior work. Its volume-dependent bound is not Theorem S.
Both files were read at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
The general search digest predates row 697; it is not a target-specific
absence proof. I did not repeat its entire multi-branch search.

The immediate sources are `gap-transfer.md` (notation, Sections 1–5,
9.3, and the general lemmas they use), its check's correction table,
and only Sections 1, 3.1 and 3.4 of `gap-crux-restate.md` (hereafter R).
The searched registry has no `gap-seed`, `gap-crux`, `gap-transfer`,
`doubling` or `thermal` owner entry. Row 699 explicitly assigns this
second check. Row 698 was neither read nor awaited. No existing result
found in these reads covers this assigned check.

I read the index instructions and relevant neighbouring rows in
`sa-index/chunk-02.md`, `chunk-24.md`, and `obligations.md` before the
cited outline passages. Searches included transfer operator, trace class,
thermal sum, ground-state deficit, and doubling criterion. The outline's
GL3 (2195–2243) already supplies positive one-link convolution coefficients;
GL8 (2313–2336) supplies a positive trace-class transfer and its torus trace.
The pressure comparison (26987–27001) already uses trace-power inequalities
successively on rectangular intermediate tori. These are prior methods,
not discoveries of this check. The plateau discussion (3712–3720) expressly
does not prove a spectral gap. These passages do not state Lemma K or S.
Credit: **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text**, at `31a47c543775`.

Both requested source files were fetched once, to `/tmp/sa_ym4.tex` and
`/tmp/sa_ca_I.tex`. The CA 4.12–4.19 and full-account index searches gave
no relevant thermal-transfer supplier; no CA body theorem is used here.
This is a bounded source search, not a claim that the entire account
contains no related theorem. Current workflow rules were read from
`origin/main` at `3b6e5c0baf4295645a07cbfc99813501c8c08c63`; science inputs
remain pinned to the requested checkout. The workhorse procedure was read
for this bounded worker handoff; no further worker or numerical job was launched.

# Check conventions

Final provenance check: another process moved the shared checkout to
`24fdfae1c4e9aec4ef06db8030c07d35fb2599a5` and detached HEAD during this
session. The three proof/check source files above were compared byte for
byte with `87508843b` and all still match. An unrelated deletion of
`library/gap-seed-limit.md` was observed and left untouched. This report
remains uncommitted and unpushed at its assigned path. The filesystem
comparison and whitespace check are bookkeeping, not proof evidence.

A positive operator means self-adjoint and nonnegative, not merely a
pointwise positive kernel. Eigenvalue sums count multiplicities.
For a rank-one operator set the excited spectral radius to zero and the
gap to infinity. A zero thermal sum is treated separately from logarithms.
All arguments below are by hand. Tool use only retrieves and saves text.
Line references to R and `gap-transfer.md` refer to the pinned source.

## 1. Rectangular transfer and axis exchange — HOLDS AFTER CORRECTION

**Correction to the cited domain, not to the construction.** Replace the
cubic slice in N.3 by
$\Lambda=\mathbb Z/b\mathbb Z\times\mathbb Z/c\mathbb Z\times\mathbb Z/d\mathbb Z$,
where $b,c,d\ge3$, and replace $N^3$ by $v=bcd$ throughout the relevant
statements. Use the projected transfer $T_B=P M C_{\mathcal E}M P$, or its
restriction to the invariant space. The unprojected operator alone does
not give the periodic Wilson partition function.

**Every equal-side occurrence in the passages used.** N.3 (line 38) fixes
the cubic graph and the counts of vertices and links. N.4 (40) counts
plaquettes and bounds $V$. N.7–N.8 (46–48) give kernel constants.
Lines 118, 125 and 131 repeat the kernel bound, temporal-plaquette count,
and half-weight bounds. Line 146 gives $|I|=12N^3$. Lines 169–171 and
175 repeat the positivity and vacuum constants. Lines 181, 183–185 and
189 use $N$ to label the gap and give its volume-dependent bound.
Line 192 chooses a four-distinct-link plaquette. None of these steps
uses equality of two different periods. The last step requires each
period to be at least three, which the corrected domain supplies.
The general lemmas A0–A3, the Gram identity (2.2), the trace factorization
3.2–3.3, and the centre-flip argument 9.3 use no equality of periods.
The original temporal-gauge remark 136 needs R1 of the correction table;
it is not used by the slab proof 125–134.

Here is the full bridge. There are $v$ vertices, $3v$ positive spatial
links, and $3v$ spatial plaquettes. Thus $0\le V\le6\beta v$ and
$e^{-6\beta v}\le K_0\le1$. Set $M=e^{-V/2}$ and

$$
 A_B(u,w)=M(u)M(w)\int_{G^\Lambda}
       \prod_{(x,i)}c\big(u_{x,i}(h\cdot w)_{x,i}^{-1}\big)\,dh.
$$

This is a continuous symmetric kernel, invariant under separate gauge
changes of its arguments, and $e^{-12\beta v}\le A_B\le1$.
Gauge averaging is an orthogonal projection. The spatial action and
simultaneous covariance of $K_0$ show that $M$ and $C_{\mathcal E}$
commute with it. These follow from Haar invariance at each link; no
coordinate-period comparison occurs.

For completeness the same Gram proof works on this graph. With $I$
the $4|\mathcal E|$ matrix-entry indices, write

$$
 K_0(u,w)=\sum_{r\ge0}\frac{e^{-\beta|\mathcal E|}(\beta/2)^r}{r!}
       \sum_{\alpha\in I^r}p_\alpha(u)\overline{p_\alpha(w)}.
$$

Cauchy–Schwarz bounds the absolute sum at degree $r$ by
$(2|\mathcal E|)^r$. Its weighted sum is one. On the diagonal the
sum is exactly one. Define $R\delta_\alpha=\sqrt{w_r}p_\alpha$;
then $\|R\|_{HS}^2=1$, $C_{\mathcal E}=RR^*$, and
$T_B=(R^*MP)^*(R^*MP)$. Hence $T_B\ge0$ and is trace class.
This is the existing proof of `gap-transfer.md` 2.2–3.3 with $v$ in
place of $N^3$, not a new positivity argument.

At time period $k\ge3$, every plaquette is either spatial in a slice
or temporal between consecutive slices. Split each spatial weight into
two halves. Integrating the temporal links independently yields
$\prod_{t\in\mathbb Z/k}A_B(u_t,u_{t+1})$. Its integral is
$\operatorname{Tr}T_B^k$: compose $k-1$ bounded kernels and apply
the Hilbert–Schmidt product trace formula to the last kernel. All
integrals converge absolutely. The operator depends on $B,\beta$,
not on $k$. Thus this is one operator for **every** $k\ge3$.

Compact positivity gives a top eigenvector. Replacing a real maximizer
by its absolute value cannot lower its quadratic form. The strictly
positive kernel makes its image positive everywhere, so the top vector
$\Omega$ can be chosen strictly positive. For simplicity, the ground-state
transform has kernel
$A_B(u,w)/(\lambda_0\Omega(u)\Omega(w))$ relative to $\Omega^2du$.
The eigen-equation gives row integral one, and the compact continuous
positive factors give a positive lower bound $\delta$. Subtracting
$\delta$ times the constant projection leaves $(1-\delta)$ times a
Markov contraction. Its norm on constants' orthogonal complement is
at most $1-\delta$. Therefore the top eigenvalue is simple. This is
A3's argument on the rectangular graph. The positive eigenvector lies
in the gauge-invariant space because the kernel is separately invariant.

Finally exchange two coordinate labels, including their periods, in the
four-torus integral. This bijects vertices, positive links and unoriented
plaquettes. An orientation reversal replaces a plaquette holonomy by
an inverse up to conjugation; its SU(2) trace is unchanged. Product
normalized Haar measure is unchanged. Hence $Z$ is invariant under every
axis permutation, even when the sides differ. Choosing any axis as time
gives the required rectangular (TM). The conclusion of point 1 holds.

## 2. Lemma A(a), (b) — HOLDS AFTER CORRECTION

R37(b) needs $S\ne0$; for $S=0$ its quotient is $0/0$.
Correct it to: for nonzero positive trace-class $S$ and integers $k\ge1$,
$\lambda_0^k\ge\operatorname{Tr}S^{2k}/\operatorname{Tr}S^k$.
Part (a) holds also for the zero operator. All transfers here are nonzero.

Write $A_p=\sum_i\lambda_i^p$. For $q\ge p\ge1$ and $A_p>0$, put
$t_i=\lambda_i/A_p^{1/p}$. Then $0\le t_i\le1$ and $\sum t_i^p=1$.
Consequently $\sum t_i^q\le1$, so $A_q^{1/q}\le A_p^{1/p}$.
Also

$$
 \lambda_0\le A_k^{1/k}
 \le\lambda_0\left(\frac{\operatorname{Tr}S}{\lambda_0}\right)^{1/k}
 \longrightarrow\lambda_0,
$$

because $\lambda_i^k\le\lambda_0^{k-1}\lambda_i$. This proves every
claim of (a), including $A_{jk}\le A_k^j$. For (b), sum
$\lambda_i^{2k}\le\lambda_0^k\lambda_i^k$ and divide by $A_k>0$.

R39–43 also follow. At fixed other sides, $F/k=\log A_k/k$ decreases,
including between nonmultiples. There are six plaquettes per four-volume,
with action terms in $[0,2]$. Thus
$-12\beta\le F/|n|\le0$, and $f$ is finite. Its infimum definition
gives (LB). Subtracting the exactly extensive term $f|n|$ from
$F(\ldots,jn_\mu,\ldots)\le jF(n)$ proves the stated bound on $\Delta$.

In R45, $r_i\in[0,1)$ by point 1, and the trace-class condition makes
all displayed sums finite. The diagonal terms in
$\sum_{i,j\ge1}r_i^k r_j^{k'}$ give
$S(k+k';B)\le S(k;B)S(k';B)$. The first summand gives
$r_1^k\le S(k;B)$. Counting each eigenvector separately is essential;
arbitrary weights less than one would not give this argument.

## 3. Theorem D(a), (b), (c) — HOLDS

Use the rectangular (TM) of point 1. Denote
$Q=Z(n,n,n,n)$, $A=Z(n,2n,2n,2n)$, and $D=Z(2n,2n,2n,2n)$.
The three spatial applications of Lemma A are exactly

$$
 A\le Z(n,n,2n,2n)^2
   \le Z(n,n,n,2n)^4
   \le Q^8.
$$

The first inequality uses the direction-2 transfer with fixed sides
$(n,2n,2n)$; the next uses direction 3 with $(n,n,2n)$; the last
uses direction 4 with $(n,n,n)$. All are admissible rectangular boxes.
The time-direction inequality gives $D\le A^2\le Q^{16}$.
Taking logs proves $\Phi\ge0$, including when all logarithms are negative.

For the single operator on $B_2=(2n)^3$, Lemma A(b) gives
$\lambda_0^n\ge D/A$. All quantities are positive. Therefore

$$
 1+S(n;B_2)=\frac{A}{\lambda_0^n}
       \le\frac{A^2}{D}\le\frac{Q^{16}}D=e^{\Phi(n)}.
$$

No inequality reverses direction in these divisions. The lower bound
on $\lambda_0^n$ concerns this same box throughout. Finally
$e^{-nm}=r_1^n\le S\le e^\Phi-1$. If $0<\Phi<\log2$, taking
logs gives D(c), with a positive lower bound. For $\Phi=0$, the thermal
sum is zero and the gap is infinite under the rank-one convention.
The backwards form follows by monotonicity of $\log(1+x)$.
Neither (TM-c) nor (LB) is used in D(a)–(c).

**Other lines of Section 3.1, checked to delimit the inputs.** D(d) follows
by summing $r_i^n\ge e^{-nE}$ over the counted states. D(f) follows by
differentiation under a finite compact integral. Axis and translation
symmetry make all six plaquette orientations have the same mean.
There are $6n^4$ plaquettes on the smaller torus and $96n^4$ on the
larger one. Hence $\Phi'=96n^4(\bar a_{2n}-\bar a_n)$ and $\Phi(0)=0$.
The integral formula follows.

D(e) holds with the **normalized** centre-twist identity. The flip is
Haar-preserving, commutes with gauge averaging, $M$, and $C_{\mathcal E}$,
and preserves positive functions. Simplicity forces $C_\nu\Omega=\Omega$.
Thus its odd projection annihilates the vacuum and its trace contribution
is at most $\lambda_0^{2n}S(2n;B_2)$. Divide by $Z\ge\lambda_0^{2n}$
and use point 2's thermal inequality to obtain D(e).
The correction table's removal of the vacuum from the all-plus sector
is respected here.

There is a normalization correction to R35's words “sign of beta
changed.” The boundary flip replaces a crossed factor
$e^{-\beta(1-w_p)}$ by $e^{-\beta(1+w_p)}$. It changes the sign of
$w_p$, leaving $e^{-\beta}$ intact. Literally replacing $\beta$ by
$-\beta$ in the whole action term instead gives
$e^{\beta(1-w_p)}=e^{2\beta}e^{-\beta(1+w_p)}$.
With $M$ plaquettes in the stack that literal partition function is
$e^{2\beta M}\operatorname{Tr}(T^k C_\nu)$, not the stated trace.
Use the former, normalized twist to make (TM-c) correct. To see the
trace identity, compose the slab kernels around time with the last
spatial slice replaced by its centre flip. Only the temporal plaquettes
in the $(\mu,\nu)$ stack change holonomy by $-1$. This is a positive
Wilson integral. Axis exchange sends that stack to the exchanged one,
so the normalized twisted partition function has the claimed symmetry.
This repair does not enter Theorem S.

D2(i) uses $e^x-1\le2x$ on $0\le x\le1$. Indeed convexity bounds it
by $(e-1)x$, and the exponential series gives $e<3$ (use
$j!\ge2^{j-1}$ for $j\ge2$, with strict inequality for $j\ge3$).
D2(ii) is conditional on its separately stated (Phi-step). Writing
$q=K\Phi_0<1$, induction gives $K\Phi_k\le q^{2^k}$ and
$\Phi_k\le\Phi_0<\varepsilon_0$, so each application is allowed.
Then $\log(1/(2\Phi_k))\ge2^k\log(1/q)+\log(K/2)$, and $K\ge2$
gives the displayed bound. Zero seeds again use the rank-one convention.
This check does not prove (Phi-step).

## 4. Lemma K(a)–(d) — HOLDS AFTER CORRECTION

The only statement correction is the endpoint domain: the three-term
convexity inequality is for $b\ge4$, since the functions are defined
only for integers at least three. Monotonicity in (d) is for $b\ge3$.
No assertion about $e(2)$ is needed. All four substantive claims hold.

**(a).** At each fixed $b$, point 2 applied to $T_b$ gives
$e(b)=\lim_{a\to\infty}\log W(a,b)/a=\inf_{a\ge3}\log W(a,b)/a$.
Nonzero $T_b$ follows from $W(a,b)>0$. The limit is finite because
$0<\lambda(b)<\infty$.

**(b).** Symmetry identifies $W(a,jb)$ with $\operatorname{Tr}T_a^{jb}$.
Lemma A(a) gives $W(a,jb)\le W(a,b)^j$. Divide the logarithm by $a$
and take its limit: $e(jb)\le je(b)$. Further,

$$
 \ell=\inf_{b\ge3}\frac1b\inf_{a\ge3}\frac{\log W(a,b)}a
      =\inf_{b\ge3}\frac{e(b)}b.
$$

This only interchanges two infima; it does not exchange an infimum
with an unjustified uniform limit. Thus $\kappa(b)\ge0$. This is
subhomogeneity under integer multiplication, not a proof of the more
general assertion $e(b+c)\le e(b)+e(c)$; the latter is not used.

**(c), including the crossed limit.** Fix $a$. If $\mu_i$ are the
eigenvalues of $T_a$, Cauchy–Schwarz on the two square-summable sequences
$\mu_i^{(b-1)/2}$ and $\mu_i^{(b+1)/2}$ gives, for $b\ge4$,

$$
 W(a,b)^2\le W(a,b-1)W(a,b+1).
$$

Take logarithms and divide by the positive integer $a$. For each of
the three fixed arguments $b-1,b,b+1$, part (a) supplies a finite limit
as $a\to\infty$. Taking these three limits in this single inequality
gives $2e(b)\le e(b-1)+e(b+1)$. Uniform convergence is unnecessary:
only three convergent real sequences occur. Subtracting the affine
function $\ell b$ preserves this inequality. Therefore the successive
increments of $\kappa$ are nondecreasing starting at the increment
from 3 to 4.

**(d).** Suppose an increment at $b_0\ge3$ is $c>0$. Convexity implies
$\kappa(b)\ge\kappa(b_0)+c(b-b_0)\ge c(b-b_0)$ for every integer
$b\ge b_0$. For $b\ge2b_0$ this gives $e(b)/b\ge\ell+c/2$.
The infimum formula in (b) supplies an integer $b_1\ge3$ with
$e(b_1)/b_1<\ell+c/2$. Yet for every positive integer $j$,
$e(jb_1)/(jb_1)\le e(b_1)/b_1<\ell+c/2$. Choose $j$ so that
$jb_1\ge2b_0$, contradicting the earlier bound. Hence no positive
increment exists. This proves (d); no limit in $b$ was assumed.

For the Wilson application with fixed sides $c,d$, the action bound
from point 2 gives $-12\beta cd\le\log W(a,b)/(ab)\le0$. Thus the
finiteness hypothesis on $\ell$ is actually supplied for every fixed
pair, even when that pair changes between uses of Lemma E.

## 5. Lemma X — HOLDS

The two expressions for $\log W$ give

$$
 a e(b)+g(a,b)=b e(a)+g(b,a).
$$

Since $e(t)=\ell t+\kappa(t)$, the identical terms $\ell ab$ cancel.
For $3\le a<b$, rewrite the result as

$$
 g(a,b)=(b-a)\kappa(b)
       +b\big(\kappa(a)-\kappa(b)\big)+g(b,a).
$$

The last two terms are nonnegative by K(d) and
$W(b,a)\ge\lambda(a)^b$. Dropping them proves
$(b-a)\kappa(b)\le g(a,b)$. This also shows exactly why the argument
requires $a<b$; it supplies no bound on $\kappa(b)$ when $a=b$.

## 6. Lemma E and its exponent — HOLDS

For $3\le a<b$, symmetry and Lemma A give
$W(a,2b)\le W(a,b)^2$. Divide by the positive $\lambda(2b)^a$:

$$
 \begin{aligned}
 g(a,2b)&\le2g(a,b)+a\big(2e(b)-e(2b)\big)\\
 &=2g(a,b)+a\big(2\kappa(b)-\kappa(2b)\big)\\
 &\le2g(a,b)+2a\kappa(b)\\
 &\le\left(2+\frac{2a}{b-a}\right)g(a,b)
   =\frac{2b}{b-a}g(a,b).
 \end{aligned}
$$

The third line uses $\kappa(2b)\ge0$, not an unproved bound on
$e(2b)$ from below. The fourth uses Lemma X. Exponentiation gives the
printed statement. For $b=2a$, the exponent is exactly four. All
free-energy densities here use the same two fixed spectator sides;
there is no comparison of different choices of $\ell$.

## 7. Theorem S, constants, induction and gap — HOLDS

This verdict concerns the conditional theorem, with the rectangular input
proved in point 1 and the endpoint conventions stated above. It proves
no seed. In the Wilson setting $\beta>0$, `gap-transfer.md` 5.3–5.7
also gives a positive excited eigenvalue, so the thermal sum is nonzero.

**The three uses of E (R202).** All use time direction 1 and $a=n$.
They successively use the following crossed direction and fixed sides:

| Crossed direction | Its old/new period | Spectator periods | Result |
|---|---|---|---|
| 2 | $2n,4n$ | directions 3,4: $2n,2n$ | $1+S(n;4n,2n,2n)\le(1+s)^4$ |
| 3 | $2n,4n$ | directions 2,4: $4n,2n$ | $1+S(n;4n,4n,2n)\le(1+s)^{16}$ |
| 4 | $2n,4n$ | directions 2,3: $4n,4n$ | $1+S(n;(4n)^3)\le(1+s)^{64}$ |

Each use defines its own finite $\ell$ at those spectator periods.
Only the final thermal inequality from one use feeds the next. No bulk
density is identified across different spectator pairs. The powers are
$4$, $4\cdot4=16$, and $4^3=64$.

On the **same final box**, let $x_i=r_i^n$. Then
$S(2n;B)=\sum_{i\ge1}x_i^2\le(\sum_{i\ge1}x_i)^2$.
This is the missing explicit algebra behind “multiplicity at least one.”
The sums are finite and nonnegative; expansion of their product or
monotone convergence from finite sums justifies the inequality. Therefore

$$
 S(2n;(4n)^3)\le\big((1+s)^{64}-1\big)^2.
$$

**Constants, by rational estimates.** The needed domain in R203 is
$0\le x\le1/640$; nonnegativity is automatic for a thermal sum.
Since $\log(1+x)\le x$ and $e^t-1\le te^t$ for $t\ge0$,

$$
 (1+x)^{64}-1\le64xe^{64x}\le64e^{1/10}x<71x.
$$

For the last strict inequality, $j!\ge2\,3^{j-2}$ for $j\ge2$ gives

$$
 e^{1/10}\le1+\frac1{10}
       +\frac{1/100}{2(1-1/30)}=\frac{641}{580}.
$$

Now $64\cdot641=41024<41180=71\cdot580$.
Squaring gives $71^2=5041$. Also $5041>640$, so a seed below
$1/5041$ is inside the interval where this bound applies.

Let $s_k=S(2^k n;(2^{k+1}n)^3)$ and $q=5041s_0<1$.
For $s_0>0$, the induction starts with $5041s_0=q$. If
$5041s_k\le q^{2^k}$, then $s_k<1/5041<1/640$, so the one-step
bound applies and

$$
 5041s_{k+1}\le(5041s_k)^2\le q^{2^{k+1}}.
$$

Thus every subsequent use is admissible. Simplicity identifies the
largest excited ratio, and

$$
 m((2^{k+1}n)^3)\ge\frac{\log(1/s_k)}{2^k n}
 \ge\frac{\log(1/q)}n+\frac{\log5041}{2^k n}
 \ge\frac{\log(1/q)}n.
$$

If $s_0=0$, the recursion gives $s_k=0$ for all $k$ and all these
operators have no positive excited eigenvalue. Their gaps are infinite.
This treats that abstract case without taking an undefined real logarithm.

**The decimal seed (R200,203).** For $0\le t<1$ the exponential series
gives $e^t\le1/(1-t)$. Hence

$$
 e^{19/100000}-1\le\frac{19}{99981}
     <\frac{191}{1000000}<\frac1{5041}.
$$

The first strict comparison is
$19000000<191\cdot99981=19096371$; the second is
$191\cdot5041=962831<1000000$. Thus the claimed sufficient threshold
$1.9\times10^{-4}$ is correct, including equality at that threshold.
No numerical evaluation supplies any step.

**Remaining assertions in R211–218.** The finite theorem gives dyadic
finite-volume gaps. It does not itself construct or prove properties of
an infinite-volume state. Its applicability to another group or model
means that the same rectangular, symmetric, positive-transfer hypotheses
hold there; reflection positivity by itself is not a replacement for them.
The recollected U(1) and $\mathbb Z_2$ spectral estimates and the two
reported computer runs in R215,218 are not used or verified in this check.
The qualitative interpretation in R216–217 does not prove a separate
confinement or continuum statement.

The numerical alternative in R214 is sound: if every $s_n\ge1/5041$,
D(b) gives $\Phi(n)\ge\log(1+1/5041)\ge1/5042>198/1000000$.
Here $\log(1+t)\ge t/(1+t)$ follows by integrating $1/(1+x)$,
and $5042\cdot198=998316<1000000$.
For R213's integer-multiple bound, E's proof with $j$ in place of 2
gives exponent $jb/(b-a)$; three sides at $b=2a$ give exponent $8j^3$.
If $14j^3s_k<1$, put $y=8j^3s_k<4/7$. The series and
$r!\ge2^{r-1}$ for $r\ge1$ give
$e^y-1\le y/(1-y/2)\le(7/5)y<14j^3s_k$.
Thus the stated multiple-box gap follows by the same largest-ratio bound.
The assertion that other cube sizes need a block of seeds is unnecessarily
restrictive; point 8 supplies the missing interpolation argument.

## 8. Corollaries S2 and S3 — HOLDS; HOLDS AFTER CORRECTION

### S2 — HOLDS under its stated symmetric trace-family hypotheses

There is one spatial doubling, so E gives exponent four, followed by
time-squaring. For $0\le x\le1/20$,

$$
 \frac{(1+x)^4-1}{x}=4+6x+4x^2+x^3
 \le\frac{34481}{8000}<\frac{108}{25}=4.32
$$

when $x>0$, and the inequality at zero is immediate. Moreover
$(108/25)^2=11664/625<11875/625=19$. Hence $s_{k+1}\le19s_k^2$.
Since $19s_0\le19/20<1$, induction gives
$19s_k\le(19s_0)^{2^k}$ and $s_k\le s_0\le1/20$, keeping the
estimate valid. The gap calculation of point 7, with 19 in place of
5041, proves the printed rate. In the abstract setting the seed itself
forces a simple top eigenvalue on each circle reached: a second top
state would contribute at least one to $S$, whereas $S<1$.
For $s_0=0$ the infinite-gap convention applies. Application to any
named lattice model still requires the full hypotheses on $W$, not
only the words “reflection positive.” No O(3) model construction was
checked here.

### S3 — its conclusion holds, but R209's integer argument fails

The first inequality, for integers $3\le a\le b/2$, is correct:
$2b/(b-a)\le4$, and the same relation holds for $(2a,2b)$.
The three spatial doublings and time-squaring therefore apply unchanged.

The next sentence of R209 is false. For $N=3$, take $L=13$.
There is no integer $b\in[6,12)$ with $13=2^k b$: $k=0$ would give
$b=13$, and $k\ge1$ would make $L$ even. This refutes the proof step,
not the final spectral assertion. The following replacement proves the
assertion with no extra physical input.

**Arbitrary-period version of E.** For integers $h\ge b>a\ge3$,

$$
 1+S(a;h)\le(1+S(a;b))^{h/(b-a)}.                 \tag{E'}
$$

Proof: the decreasing trace root of $T_a$ gives
$W(a,h)\le W(a,b)^{h/b}$, even when $h/b$ is not an integer.
Therefore

$$
 \begin{aligned}
 g(a,h)&\le\frac hb g(a,b)
       +a\left(\frac hb e(b)-e(h)\right)\\
 &=\frac hb g(a,b)
       +a\left(\frac hb\kappa(b)-\kappa(h)\right)\\
 &\le\frac hb\big(g(a,b)+a\kappa(b)\big)
 \le\frac{h}{b-a}g(a,b).
 \end{aligned}
$$

The last two inequalities use K(b) and X. This proof compares only
integers as periods. The fractional exponent is an ordinary real power
of the positive scalar $W$, not a lattice of fractional length.

In fact E' gives the stronger corrected assertion:

> If $s=S(N;(2N)^3)<1/5041$, then **every integer** $L\ge2N$ obeys
> $m(L^3)\ge\log(1/(5041s))/N$.

For $s>0$, put $q=5041s<1$. Choose the unique $k\ge0$ such that
$D=2^{k+1}N\le L<2D$, and put $a=2^kN=D/2$.
Theorem S gives $S(a;D^3)=s_k\le q^{2^k}/5041$.
Apply E' three times, replacing one spatial side $D$ by $L$ each time.
The spectator pairs are $(D,D)$, $(L,D)$, and $(L,L)$.
Each exponent is $L/(D-a)=2L/D<4$, so

$$
 S(a;L^3)\le(1+s_k)^{64}-1
       \le71s_k\le\frac{q^{2^k}}{71}.
$$

The point-7 constant bound applies since $s_k<1/5041<1/640$.
It follows that

$$
 m(L^3)\ge\frac{\log(1/S(a;L^3))}{a}
       \ge\frac{\log(1/q)}N+\frac{\log71}{2^kN}
       \ge\frac{\log(1/q)}N.
$$

If any sum vanishes, interpret that bound as an infinite gap; if the
seed vanishes, E' propagates vanishing to all these boxes.
The proof also makes the top eigenvalue simple there when simplicity
was not separately assumed, since the resulting thermal sum is below one.

For S3 as printed, the block includes $b=2N$, so
$S(N;(2N)^3)\le s_{\max}<1/5041$. The stronger assertion gives

$$
 m(L^3)\ge\frac{\log(1/(5041s_{\max}))}{N}
       \ge\frac{\log(1/(5041s_{\max}))}{2N}.
$$

Thus the original S3 conclusion survives. Replace its integer
factorization sentence by E' and this argument. Seeds at the other
block sizes are unnecessary for that conclusion. This repairs a proof;
it does not establish any seed for Wilson SU(2).

## 9. Hand-solvable attempts to break K and S — HOLDS on the test families

This verdict records the outcome of the requested counterexample attempt,
not additional evidence that can replace the general proofs. No run was used.

**Independent one-dimensional rings in all four directions.** Fix
$0<q<1$ and a real $f$. For periods $n_\mu\ge3$, define

$$
 Z(n_1,n_2,n_3,n_4)
 =e^{fV}\prod_{\mu=1}^4(1+q^{n_\mu})^{V/n_\mu},
 \qquad V=\prod_\mu n_\mu.
$$

This is the partition function of independent two-state rings in each
direction, with eigenvalues $1,q$ per bond transfer, and an extensive
scalar weight. It is symmetric under all axes. Explicitly, for
$B=(b,c,d)$, $v=bcd$, set

$$
 \lambda_B=e^{fv}(1+q^b)^{cd}(1+q^c)^{bd}(1+q^d)^{bc},\qquad
 K=\frac12\begin{pmatrix}1+q&1-q\\1-q&1+q\end{pmatrix},\qquad
 T_B=\lambda_B K^{\otimes v}.
$$

The eigenvalues are $\lambda_B q^j$, with multiplicities
$\binom vj$, $0\le j\le v$. The top is simple, and the matrix has
strictly positive entries. Directly,
$\operatorname{Tr}T_B^a=\lambda_B^a(1+q^a)^v=Z(a,b,c,d)$.
Thus this is a genuine full rectangular trace family, not invented
independent spectra that violate axis symmetry.

For fixed $c,d$, both sides of K are explicit:

$$
 \begin{aligned}
 \ell_{c,d}&=fcd+d\log(1+q^c)+c\log(1+q^d),\\
 e(b)&=b\ell_{c,d}+cd\log(1+q^b),\\
 \kappa(b)&=cd\log(1+q^b),\qquad
 g(a,b)=bcd\log(1+q^a).
 \end{aligned}
$$

The infimum giving $\ell_{c,d}$ is verified by dividing $\log Z$ by
$ab$: the two remaining nonnegative terms are
$cd\log(1+q^a)/a+cd\log(1+q^b)/b$, and they tend to zero.
The deficit strictly decreases. Its discrete convexity is equivalent to

$$
 (1+q^{b-1})(1+q^{b+1})-(1+q^b)^2
       =q^{b-1}(1-q)^2\ge0.
$$

Its integer-multiple inequality follows from
$1+q^{jb}\le1+q^b\le(1+q^b)^j$.
X becomes
$(b-a)\log(1+q^b)\le b\log(1+q^a)$, true since $a<b$ and $q<1$.
This test has a nonzero deficit, so it does not trivialize K by setting
all ground-state corrections to zero.

For S, write $y=q^n$ and $v=(2n)^3=8n^3$. Then

$$
 s=(1+y)^v-1,\qquad
 S(2n;(4n)^3)=(1+y^2)^{8v}-1,\qquad m(B)=-\log q.
$$

Put $M=8v$. Expanding the square of
$\sum_{j=1}^M\binom Mj y^j$, its diagonal terms dominate
$\sum_{j=1}^M\binom Mj y^{2j}$ because
$\binom Mj^2\ge\binom Mj$. Hence

$$
 S(2n;(4n)^3)\le\big((1+y)^{8v}-1\big)^2
       =\big((1+s)^8-1\big)^2
       \le\big((1+s)^{64}-1\big)^2.
$$

The theorem survives even though the number of available excited states
grows exponentially with the spatial volume. This is an exact binomial
identity and inequality, not an enumerated computation.

To test the actual seed regime **in this toy model only**, take $n=3$,
$q=1/1000$. Then $v=216$ and $y=1/10^9$.
Using $\binom{216}{j}\le216^j$ gives
$s\le216/(10^9-216)<1/5041$, since
$216\cdot5042=1089072<10^9$. The predicted lower bound is positive
and smaller than the exact $\log1000$: indeed
$5041s\ge5041\cdot216q^3>q^3$, so
$\log(1/(5041s))/3<\log1000$. The all-cube correction in point 8
has that same rate and also survives. This is not a Wilson seed proof.

**Degenerate-top test.** Take $Z(n)=d e^{fV}$ with integer $d\ge2$,
and $T_B=e^{fv}I_d$. This is symmetric, positive and trace class in
every direction, though not positivity improving. Here $\kappa=0$,
$S=d-1$, and $m=0$. K, X, E and the one-step inequality hold, while
the small seed fails. Thus allowing a vacuum multiplicity cannot
produce a false positive from the criterion.

**A tempting invalid counterexample.** The nonnegative convex sequence
$\kappa(b)=(b-4)^2$ has infimum $\kappa(b)/b=0$ and increases for
$b\ge4$. It would refute K(d) if only convexity and the infimum were
used. But $\kappa(8)=16>2\kappa(4)=0$ violates K(b). It cannot be
the deficit of the required symmetric trace family. This checks that
the integer-multiple step in K's proof is essential, not decorative.
No counterexample to K or S satisfying their complete hypotheses was
found by these hand constructions.

## Final verdict table

| Point | Statement checked | Verdict | Correction or boundary |
|---|---|---|---|
| 1 | Rectangular transfer, all time periods, simple top, axis symmetry | HOLDS AFTER CORRECTION | State the rectangular domain; replace $N^3$ by $bcd$; keep the gauge projection. |
| 2 | Lemma A(a), (b) | HOLDS AFTER CORRECTION | Require a nonzero operator in (b); (a) already holds. |
| 3 | Theorem D(a), (b), (c) | HOLDS | All sixteen powers and the top-eigenvalue lower bound are valid. (TM-c) is unnecessary. |
| 4 | Lemma K(a)–(d) | HOLDS AFTER CORRECTION | Three-term convexity starts at $b=4$; monotonicity starts at $b=3$. |
| 5 | Lemma X | HOLDS | $3\le a<b$; same spectator pair throughout. |
| 6 | Lemma E | HOLDS | Exponent $2b/(b-a)$ is correct. |
| 7 | Theorem S | HOLDS | Conditional on the exact inputs below; zero sums use the infinite-gap convention. |
| 8a | Corollary S2 | HOLDS | For the symmetric trace family stated before K; named model applications require that family. |
| 8b | Corollary S3 | HOLDS AFTER CORRECTION | R209's integer decomposition is false; E' proves the conclusion, even from one seed. |
| 9 | Hand-solvable counterexample attempts | HOLDS on the tested families | Nonzero deficit, volume-growing multiplicities, and degenerate vacua were tested exactly. No universal absence claim. |

Additional normalization finding: (TM-c), R35, holds only when the twist
changes the plaquette trace sign and retains the constant part of the
Wilson weight. Literal sign reversal of the entire $\beta$ action term
needs the factor explained in point 3. It affects neither D(a)–(c) nor S.

## Exact inputs Theorem S needs

1. **One common rectangular partition family.** A positive scalar
   $Z(n_1,n_2,n_3,n_4)$ for every integer side at least three, invariant
   under exchange of any two axes. All comparisons use this same family
   and normalization, at the same coupling.
2. **Positive trace representations in every direction.** For each fixed
   triple $B$ and chosen time direction, one nonzero self-adjoint
   nonnegative trace-class $T_B$, independent of the time period, with
   $Z(k;B)=\operatorname{Tr}T_B^k$ for all integers $k\ge3$.
   Eigenvalues are counted with their actual integer multiplicities.
   For Wilson theory these are the projected operators of point 1.
3. **Finite two-direction bulk infima.** For every fixed spectator pair
   $c,d$ used in the comparisons,
   $\inf_{a,b\ge3}\log Z(a,b,c,d)/(ab)>-\infty$.
   The Wilson bound $-12\beta cd$ supplies this. The infimum is finite
   above because each partition function is finite and positive.
4. **The spectral meaning of the thermal sum and gap.** Normalize by the
   largest eigenvalue. Subtract one top state in $S$ and take the
   largest remaining ratio for $m$. A simple top is supplied for every
   Wilson box by point 1. In the abstract small-seed implication,
   simplicity on the boxes reached also follows from $S<1$; no separate
   positivity-improving hypothesis is then needed for those boxes.
5. **The unproved seed.** For some integer $n\ge3$,
   $S(n;(2n)^3)<1/5041$. This is an additional condition, not a result
   of inputs 1–4. D(b) gives the sufficient alternative
   $16\log Z(n^4)-\log Z((2n)^4)\le19/100000$.
   No such inequality is proved here for Wilson SU(2).
6. **Ordinary mathematical tools.** The compact positive spectral theorem,
   absolutely convergent nonnegative sums, Cauchy–Schwarz, elementary
   limits, exponential and logarithm inequalities, and induction.
   The particular compact-operator construction was checked through the
   existing hand proofs in `gap-transfer.md`; no numerical certificate,
   computer experiment or Lean run is an input.

The one-step inequality uses 1–3 and the eigenvalue interpretation in 4;
it does not need a small seed. The uniform dyadic gap additionally needs
5. The sufficient $\Phi$ condition uses D(a)–(c). Neither (TM-c), an
odd-flux estimate, an RG construction, a continuum limit, a prescribed
infinite-volume state, nor the existence of a physical mass gap is an
input to this finite conditional theorem.

## What this check did not cover

The unrequested sections of R and the parallel row-698 check were not
read. The text's named-model spectral recollections, computer runs,
and literature priority claims were not checked. No proof of the seed,
continuum theorem, confinement statement, or infinite-volume correlation
limit was attempted. The general group's or O(3) model's transfer
construction was not checked; point 1 concerns the specified Wilson SU(2)
model. No assertion of novelty against the entire Sussman–Alpoge account
is made. No audit, ledger edit, source-proof edit, commit, push, or outward
post was performed. Only this report was written in the checkout.

Checked line by line by Codex within the specified sections: the central
K–X–E–S chain has no substantive failing step. The material failing line
in S3 is R209, repaired in point 8. The minor domains and the separate
centre-twist normalization require the corrections above. **No mass gap
is proved by this file, whatever these conditional verdicts.**
