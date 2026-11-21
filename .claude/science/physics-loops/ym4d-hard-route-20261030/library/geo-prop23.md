# geo-prop23: the geometric premises of A3/2.8 (queue row 118)
Provenance: Codex (GPT-6; effort: xhigh), checkout `a3df81a6f60efabdd48d5b75ffbbfb8158e8b4ea`; Sussman–Alpoge outline `31a47c543775`; research text, not an audit, grants no status.

**Result: REFUTED as a universal implication from the outline's supplied data.** Sections 3–4 give an explicit geometric configuration and an admissible one-cell profile violating GEO5(a),(b). Section 5 proves a narrower replacement profile rule. This does not refute a result that assumes GEO5.

## 1. Target and source conventions

The target is the assertion that the outline's large-field construction supplies GEO1–GEO6, EXT and the W3 nest gap used by `sa-2.8-terms.md` §3, Lemma W, `meet-6c.md` [SA], and `a3-close-meet-gate.md` §B. A counterexample to one required premise refutes this conjunction; it does not refute Yang–Mills existence or the analytic implications conditional on the premises. The consequence would be to retain the missing geometric condition explicitly, or change the corresponding consumer.

Credit: the outline's regions, tests, class, nests, healing and preparation are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA line numbers below refer to their `YM4_sketch_500.tex` at the stated revision, fetched once to `/tmp/sa_ym4.tex`. The repository's Definition A and its repairs are separate adopted conventions. Only written arguments will be used; no run discharges a statement.

The initial reading covered GOAL, FINISH's working rules and row 118, all eight target premises, Lemma W, the meet's [SA], and the explicit W3 clearance. Proposition 2.3 (SA 17398–17407) asserts the interlevel gaps for step and prepared sequences. It does not specify a quantitative profile rule: SA 6331–6334 makes the interpolation rule supplied data. These two sources of hypotheses must be distinguished.

## 2. Construction being tested

Use level-k units, with `xi_j=L^(j-k)`, and a torus large enough that the boxes and their neighbourhoods do not wrap. Write `a=k-N_k`, `C=X intersect Z_a`, and `Lambda=Lambda^pr`. In a class component, SA 17576–17583 prescribes, for `a<i<=k`,

`H_i = hull_i(X intersect Z_(i-1))`,
`Omega_i^c intersect X = H_i^[8]`,
`Z_i intersect X = H_i^[10]`.

The class requires one small component at every level in the window, no joining or creation in its interior levels, and no operation at levels `[a,k)`. SA 17415–17437 describes increasing prepared boxes `Z''_i(X) subset Omega_i^c intersect X`; healing adds X to every determining and action member. Preparation changes the action members only for `a<i<=k`, by

`Lambda_i^p=Lambda_i union (X minus Z''_i)`;

for `i<=a` they stay `Lambda_i`. The final box Lambda is `Z''_k` plus one layer of level-k M-cubes (SA 17598, 17630–17638).

For localisation I use Definition A with all the repairs of `a2-full-gate.md`, assign-adopt sections: `M_1'>=rho`, the explicitly adopted cut meet, second-rule collar separation `(n_s-n_c)mu>max(rho,3M_1')`, and the extension to test grids. Thus changing an unspecified localisation rule is not an admissible counterexample here.

## 3. A single quiet component, with well-separated prepared shells

Here is explicit geometric data for the single-creation example admitted at SA 17583. The counterexample below concerns the supplied profiles, so the boxes will satisfy even the asserted prepared gaps; no failure of a gap is assumed.

Choose an odd integer `L>=27`, then the construction sizes in the order of (2e), with `mu=M_1'>=rho` and `M>=L^2 M_2>=L^3 mu`. Fix an integer `h>=2`, put `R=L^h`, `N_i=R` throughout the window, `a=1`, and `k=R+1`. Take a torus of level-k side `2L^J`, with `J` large enough that its side is more than `100MR`. Increase J if any of the source's earlier torus floors demands it. All grids divide this side. Set

\[
 m_i=M L^{i-k},\qquad s_i=R m_i.
\]

These are respectively the side of an M-cube and a cell at level i. Choose a window of the coupling frame on which its rounded value stays R. This is possible at arbitrarily large R: for example take exponent `r=2`, a fixed allowed slope `lambda>0`, and

\[
 \theta_i=\exp\sqrt{R/2}+\lambda(k-i),\qquad 0\le i\le k.
\]

For sufficiently large h, `R/L < (log theta_i)^2 < R` throughout. Indeed `log(theta_i)` is between `sqrt(R/2)` and `sqrt(R/2)+lambda k exp(-sqrt(R/2))`; the latter added quantity tends to zero, whereas `sqrt R-sqrt(R/2)` tends to infinity. Thus the smallest power of L above `(log theta_i)^2` is exactly R. Choose lambda within the allowed frame slope interval and h large enough for the coupling ceiling. This is an existence argument with a stated order of choice, not a numerical check.

All step boxes are centred at the origin; the prepared boxes below need not be. At the creation step take the cell hull of the plaquette-test failures to be the central cell `E_a`, and take no approximate-fluctuation, third-test, collar or rim failures outside its excluded margin. The rule of SA 17317–17332 gives

\[
 \Omega_a^c=E_a^{[4]},\qquad C=Z_a=E_a^{[6]}.
 \tag{3.1}
\]

Thus C has side `13s_a`. This is a single-cell creation record, with no older marks. The data tested outside its margin can be the identity; the failed datum stays in the excluded core. The geometric argument does not assert any lower bound on the weight of this record or use one.

For `a<i<=k`, take no new failures and no other component. The hull of the preceding box is the central level-i cell E_i: at the first step `13s_(i-1)<s_i`, and thereafter `21s_(i-1)<s_i`, because `L>=27`. Hence the literal quiet-step formulas are

\[
 \Omega_i^c=E_i^{[8]},\qquad Z_i=E_i^{[10]}.
 \tag{3.2}
\]

Every Z_i is one box, with 21 cells along each side; the initial box has 13. Boxing changes none of these sets. No joining is possible. At levels `<k=R+1` the waiting window cannot contain this level-1 creation, so the component has had no earlier operation. Consequently `X=Z_k` satisfies the single-box, quiet and quarantine clauses. The ordinary label is `Lambda_i=T minus Z_i`, `Omega_i=T minus Omega_i^c`, with `Omega_0=Omega_1^~`. Its tests and all absent creation sets have the required cell alignment.

For completeness specify a nest that even has the equality of gaps mentioned in Proposition 2.3. Let `D_i=[alpha_i,beta_i)^4`, initially `D_a=C`. The level-i grid's face coordinates form `F_i=m_i(Z+1/2)`. Because R is divisible by L, both initial faces are in F_(a+1). Designate the lower face initially. For `i>a`, use these two alternating rules:

\[
\begin{array}{ll}
\text{designated lower face:}&
 \alpha_i=\alpha_{i-1}-m_i,\quad
 \beta_i=\min\{u\in F_{i+1}:u\ge\beta_{i-1}+m_i\};\\
\text{designated upper face:}&
 \beta_i=\beta_{i-1}+m_i,\quad
 \alpha_i=\max\{u\in F_{i+1}:u\le\alpha_{i-1}-m_i\}.
\end{array}                                                    \tag{3.3}
\]

Designate the opposite face for the next step. The grid F_(k+1) is just an auxiliary aligned grid for this last rounding; choose the torus to admit it too. Inductively the designated old face is in F_i, the new opposite face is in F_(i+1), and both new faces are in F_i because the grids are nested. Thus every D_i is a union of level-i M-cubes. Each face moves at least m_i, and the designated one moves exactly m_i. The other moves less than `m_i+m_(i+1)`. Consequently

\[
 d_i:=\beta_i-\alpha_i
 <13R m_a+(L+2)\sum_{u=a+1}^i m_u
 <13R m_a+(L+4)m_i.                         \tag{3.4}
\]

The last bound uses `(L+2)L/(L-1)=L+3+3/(L-1)<L+4`. Each face's absolute position is less than `13R m_a/2+(L+3)m_i`. For `i>a`, this divided by s_i is at most `13/(2L)+(L+3)/R<1/2`: it suffices that `R>=L^2`, and at `L>=27` the upper bound is `13/54+30/729<1/2`, decreasing thereafter. Hence `D_i subset E_i subset Omega_i^c intersect X`. Use `Z''_i=D_i`. Its gap, measured between carriers, is exactly

\[
 d_\infty(D_{i-1},D_i^c)=m_i=M\xi_i.         \tag{3.5}
\]

This is an explicit choice of stage-box data satisfying the source's box, shell and gap clauses, not a claim that its qualitative wording uniquely specifies this recursion. At level k, `13R L^(-R)<1` (already true for `R>=L^2`, and the ratio decreases as the integer R grows). Thus

\[
 d_k<(L+5)M,\qquad
 \Lambda=[\alpha_k-M,\beta_k+M)^4,
 \quad\operatorname{side}(\Lambda)<(L+7)M.   \tag{3.6}
\]

In particular the final box has the required side `O(M)`, with the named constant `L+7` fixed before the coupling. Its faces lie at distance less than `(L+4)M` from the origin.

Boxes are understood as the corresponding aligned site sets; using their geometric carriers in the displays changes a distance to a plaquette midpoint by at most one bare spacing `eta=L^(-k)`. All inequalities used below leave a larger margin.

The prepared label has `Omega_i^p=Lambda_i^p=T minus D_i` for `a<i<=k`, and retains the original members at `i<=a`. This is exactly the union formula in §2 because `D_i subset Z_i subset X`. The healed label has every `Omega_i^h=Lambda_i^h=T` for `i<=k`. The prepared and healed action regions agree outside Lambda at **every** level: their differences are C at level a and D_i at later levels, all contained in Lambda. Their determining rows and exterior data also agree there when the same exterior field is used. Thus a failure below cannot be blamed on a difference of these regions outside Lambda.

The geometric data in (3.3) can be replaced by any of the source's thin nests in this one component. The counterexample only needs the final box of size `O(M)` and the surrounding region of size `MR`; it does not depend on identifying (3.3) with a particular analytic integration kernel.

## 4. REFUTED: the source's supplied-profile conditions do not imply GEO5

The exact quantifier matters. GEO5 is explicitly labelled a **premise on supplied data** in `sa-2.8-terms.md`. The assertion refuted here is that this premise follows from the outline's definitions (or from Proposition 2.3). It is not a claim that an implication assuming GEO5 is false. Here is a supplied rule and a configuration, rather than a list of missing conditions.

For every level i and every small-field region A, supply the rule

\[
 \varphi_i[A](p)=\min\{1,d_\infty(p,A^c)/s_i\},\qquad s_i=M\check R_i\xi_i,
 \tag{4.1}
\]

with `d(p,empty)=infinity`. Use cubical geometric carriers for this formula; p is a plaquette midpoint. Prescribe the interior of A to be `{p:d(p,A^c)>=s_i}`. This is the one-cell interior. The rule is zero off A, one on its prescribed interior, real, between zero and one, and has Lipschitz constant `1/s_i`. It is invariant under translations and hypercubic isometries and uses only one cell of range. It is one rule on all tori and agrees on common lifts with room for this range. Thus it meets the supplied-profile conditions at SA 6331–6334, as well as the one-cell interior statement at SA 21040–21047. The exact Wilson bookkeeping identity at SA 6354 is unchanged for every such choice. No condition in those profile definitions imposes a three-quarter-cell transition width.

This choice is also compatible with the extra interior-tent clause mentioned at SA 21017–21019: the supplied regular index map can put its base points far enough inside the prescribed interior that their tents are supported there. Then `varphi_i h_z=h_z` for each retained base point. That clause does not force the profile to become one earlier in the unretained boundary layer. This observation is about the permitted geometric/profile data, not an assertion that arbitrary effective activities solve the induction of (2e).

Apply (4.1) to the prepared and healed regions of §3. At level k they are respectively

\[
 A_p=T\setminus D_k,\qquad A_h=T.
\]

Put `s=s_k=MR`. Choose the bare plaquette in directions 2 and 3 whose midpoint is

\[
 p=(n\eta,\eta/2,\eta/2,0),\qquad
 n=\left\lceil\frac{\beta_k+7s/8}{\eta}\right\rceil,
 \tag{4.2}
\]

This specifies a plaquette without enumeration. Its distance delta to the positive first-coordinate face of D_k obeys

\[
 \frac{7s}{8}\le\delta=n\eta-\beta_k
 <\frac{7s}{8}+\eta<\frac{15s}{16}<s.
 \tag{4.3}
\]

The penultimate inequality uses `s>16eta`. The other three coordinates lie well within the transverse faces, and the torus has side greater than 100s, so no other face or periodic copy is closer. Since Lambda adds an M-layer to D_k,

\[
 d(p,\Lambda)=\delta-M>\frac34s.
 \tag{4.4}
\]

Indeed `7s/8-M-3s/4=M(R/8-1)>0`. Even if distances are taken to the site sets instead of the cubical carriers, subtracting one additional eta leaves this strictly positive. The point lies inside X, far from its outer boundary: `beta_k<(L+4)M`, and `R>=L^2>16(L+4)` gives `p_1<s/16+15s/16=s`, whereas that face of X is at `21s/2`.

For every allowed `C_p<=3/4`, write `w_k=C_p s`. The restrictions of A_p and A_h to `B_infty(p,w_k)` are identical: this ball misses D_k, and even misses Lambda, by (4.4). Nevertheless (4.1) gives

\[
 \varphi_k[A_h](p)=1,\qquad
 \varphi_k[A_p](p)=\delta/s\in[7/8,15/16).
 \tag{4.5}
\]

This proves two failures on the same explicit configuration:

* **GEO5(a) fails:** identical region restrictions on the required ball give different profile values.
* **GEO5(b) fails:** `d(p,A_p^c)=delta>w_k`, but the prepared profile is strictly less than one.

All constants and the witness midpoint have been specified. Enlarging M, the torus or the coupling floor does not fix this: both distances and the profile width scale with `s=MR`. The obstruction is the coefficient in the required width, not a rounding error or an insufficiently large constant.

There is also a direct check of what the invalid inference in Lemma W would do. At every earlier level the prepared hole is contained in D_k and `s_i<=s/L`, so its profile at p is one; the healed profiles are all one. Therefore the two Wilson weights obey the exact identity

\[
 v(p)-w(p)=-b_k(1-\delta/s).                 \tag{4.6}
\]

For any nonzero increment b_k this contradicts the conclusion `v=w` at distance greater than `3MR/4` from Lambda. Equation (4.6) is an algebraic consequence, not an assertion that an arbitrarily prescribed increment is produced by the RG. The failure of GEO5 itself does not require b_k to be nonzero. This witness lies where the cutoff chi is one; it does **not** by itself show that the integrated term R2 is nonzero or that Proposition 2.8 cannot be repaired.

## 5. The smaller repair, proved

Here is a complete repair of the precise profile failure just exhibited. It is an additional choice of supplied data, not a consequence of Proposition 2.3. For every i define

\[
 \widehat\varphi_i[A](p)
   =\min\{1,2d_\infty(p,A^c)/s_i\}.
 \tag{5.1}
\]

**Locality and plateau lemma.** With the cubical-carrier distance convention of (4.1), rule (5.1) satisfies GEO5(a),(b) with the named constant `C_p=1/2`. If `A triangle B subset Lambda`, the two profiles agree whenever `d(p,Lambda)>s_i/2`.

**Proof.** The value is zero off A and one when the distance to the complement is at least `s_i/2`. Let `r=s_i/2`. If the complement meets the open ball `B(p,r)`, the distance to the whole complement is the infimum of the distances to its points in this ball: all other points are at distance at least r. Thus the value is determined by the restriction of A to this ball. If the complement does not meet the open ball, the value is one, including the equality case where a complementary point is exactly r away. This proves locality with radius r and the claimed plateau. Finally `A triangle B subset Lambda` and `d(p,Lambda)>r` imply that A and B coincide throughout the ball. Apply the just-proved locality. The same argument works on the periodic torus, using its periodic distance. There is no assumption of convexity. QED.

If GEO5 is instead read on bare site sets, keep formula (5.1) on their cubical carriers and use `C_p=3/4`, with `s_i>=4eta`. Passing from sites to their carriers costs at most eta: all carrier data within `s_i/2` are determined by sites within `s_i/2+eta<=3s_i/4`, and a site-complement distance greater than `3s_i/4` gives carrier-complement distance greater than `s_i/2`. These two inequalities prove the same locality and plateau conclusions in that convention. The required floor follows from `s_i>=M eta` and `M>=4`.

For the configuration of §3, all action-region differences lie in Lambda and `max_(i<=k)s_i=s_k`. Thus the repaired profiles agree at every midpoint farther than `MR/2` from Lambda. In particular they agree at (4.2). This closes the smaller statement rather than leaving a proposed repair unchecked. It proves neither GEO5(c) for arbitrary marked histories nor the whole geometric package.

## 6. Disposition

**REFUTED:** the conjunction GEO1–GEO6, EXT and the W3 gap is **not a consequence of the outline's stated geometric and supplied-profile definitions**. The explicit one-cell profile (4.1), on the single quiet component and thin nest of §3, violates GEO5(a),(b). Even granting Proposition 2.3 does not exclude it: that proposition asserts nesting, alignment and interlevel gaps, and says nothing about profile interpolation radii. The defect affects the claimed extraction of the hypotheses from SA, not results that continue to list GEO5 as an assumption.

The attempted shell and exterior-region counterexamples did not supply the failure: in this configuration the W3 clearance follows from `C subset D_(q-1)` and (3.5), and the prepared/healed action regions coincide outside Lambda. The adopted localisation cannot change (4.5), because it does not change the supplied action-profile rule. The repair (5.1) is proved for locality and the plateau; it remains a choice the consumer must explicitly make.

Scope of what remains: no universal proof or counterexample for GEO1–GEO4, GEO6, EXT or all admissible W3 nests is claimed here, and no claim is made about positive measure or an RG solution for arbitrary supplied profiles. A profile already required to satisfy GEO5 is outside this counterexample's domain. Row 118's universal derivation is refuted by the explicit counterexample to GEO5 above.
