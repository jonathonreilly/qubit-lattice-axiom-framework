# Repo search

The lead's `prior/repo-search-2026-11-08.md` concerns earlier YM4D work.
Its nearest named hit is `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` on
PR #10114 (the digest also records the identical #10133 copy). I opened
that passage: it constructs a one-step loop correlation, not the thermal
sum enlargement or shape recursion checked here. No proof from it is used.
There is no `prior/gap-sh-astra.md`. An exact-name search of
`open-registry.md` found no competing owner of E2, B3 or SH.
The local prior results are `gap-crux-restate.md` Sections 1 and 3.4:
Lemma A, the deficit/crossing lemmas, and Codex's E'/S3' correction.
They are inputs, not new results of this check. The remote search details
and outline comparison are recorded below, before the verdicts.

## Status and provenance

Written by OpenAI Codex, gpt-6-astra, maximum reasoning effort (the
dispatched model), for FINISH row 722, 2026-11-11. Source revision:
`a867197306ac4eab32466e4ab6fe86e92e9ad89c`. This is a research check,
not an audit, and grants no status. It claims no mass gap at a coupling
of order one. Only this output file is edited.

**Complete.** Each verdict was appended separately. E2, B3, SH's
positive-time conclusions, all five requested thresholds, D-shape (a)–(f)
and Theorem 4' hold on their stated input chain. SH needs explicit positive
integers p,q. The ratio-2 table needs the transformed seed and K=22.2
distinguished from its composed rate constant 1479. The earlier Claude
report was opened only after all my verdicts were saved. Its two false
auxiliary statements are identified and corrected in Section 24.

Scope: Lemma E2; both B3 inequalities and order independence; SH's
recursion, (i)–(iii) and sufficient constant; the stated seed thresholds;
D-shape (a)–(f); Theorem 4', its constants, and a separate hand example.
The transfer-operator construction and the strong-coupling expansion
remain named inputs, not fresh full checks. Sections 3–5 of the source
(including Ising facts, compact Gaussian model and GUIDE values) are not
being certified. No computer-assisted numerical or symbolic calculation
is used as proof.

Credit: Claude Fable 5.2 wrote the shape note and the original deficit
argument. Codex gpt-6-astra supplied E' and S3' in row 699. Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text, wrote
the outline and complete account. Tadeusz Balaban's work underlies the
program's ultraviolet construction; no Balaban estimate enters these
finite-volume thermal-sum arguments.

**Checkpoint.** Check and comparison complete. Source files remain at the
pinned revision. No mathematical obligation of this dispatch remains.
The consumer should use the corrected parameter statements in points 3
and 12. The seed at a coupling of order one remains outside this work.

## Search completion and source boundary

Fetched `origin/main` at `1ddab646213529a1dea97fbca1d3d567d811b573`,
#10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, #10133 at
`89faef229ff6e6bde42baad15ed8270c2f4087d8`, #10134 at
`1e70c7211a2cdbc39001e619f1dd89db45e25851`, and #10141 at
`fb99b4dddc7254e6124ac124887d58eeb3a77802`. A completed search outside
this lane found no exact matches for `gap-seed-shape`, `D-shape`,
`Theorem SH`, `Lemma E2`, `monotone deficit`, or `thermal.sum` in Markdown
and TeX. Word boundaries exclude such false positives as “fixed-shape”.
The broad discovery output was truncated and is not absence evidence.
The completed search is saved at
`/tmp/gap-sh-astra-20261111/repo-hits.txt`. These names do not exclude
differently named work. The lead's digest and its nearest source hit,
described above, supply the method comparison.

Both requested Sussman–Alpoge files were fetched once at `31a47c543775`.
The index README, matching chunk rows and neighbouring rows were read
before SA 588–599 and 2313–2335. Chunk 02:100–101 indexes their positive
trace-class transfer operator and trace identity as proved in detail.
SA 2313–2335 gives that construction for a cubic torus; it is prior
transfer-operator work, not the box-shape recursion. Chunk 01:69–70 and
`obligations.md:24` lead to SA 588–599, which explicitly separates a
positive gap from polynomial clustering. No assertion there supplies SH.
The complete-account index search found only the related CA-III
`10.7:prop-clustering-mass-gap`, not an E2/B3/SH supplier. That CA-III
proof was not read or used. No CA-I item 4.12–4.19 is an input here;
the downloaded CA-I body is therefore not read wholesale or treated as
evidence. This is a bounded source comparison, not an absence theorem.

## 1. Lemma E2 — HOLDS

Source: `gap-seed-shape.md:60–72`; inputs:
`gap-crux-restate.md:29–45,174–186`. Fix the other two sides throughout.
For positive eigenvalues counted with multiplicity, normalizing by the
largest eigenvalue shows that the Schatten norms decrease with the
exponent. Thus, for every integer `h >= b`,

    log W(t,h) <= (h/b) log W(t,b).

Subtract the bulk term `ell*t*h`. The remainder is

    g(t;B^h) <= (h/b)g(t;B) + t[(h/b)kappa(b)-kappa(h)].

The supplied deficit lemma gives `kappa(h) >= 0`. Crossing at the
**separate** time `t'` gives `(b-t')kappa(b) <= g(t';B)`.
Substitution is exactly E2. No comparison between `t` and `t'` occurs;
`t' > t` is allowed. The domain `3 <= t' < b <= h` supplies every
denominator and every transfer trace used. The two fixed sides can be
different. The case `h=b` is harmless, although the resulting bound is
not tight.

The remarks (i)–(iii) at source line 70 also **HOLD**: setting `t'=t`
gives `h/(b-t)`; general `t` can exceed `b`; and
`g(qa;B) <= log(1+s^q)` follows by expanding the product of nonnegative
excited-state sums. First failing line: none.

## 2. Proposition B3 — HOLDS, both inequalities and every order

Source: `gap-seed-shape.md:74–87`. Put `v_k = product_(i<=k)(h_i/b_i)`
and divide the two thermal logarithms at stage k by `v_k`. E2 bounds
this pair by multiplication by

    M(beta_i) = [[1, (p/q)(beta_i-1)], [0, beta_i]].

The first coordinate is `g(pa)` and the second is `g(qa)`. Direct
multiplication gives `M(u)M(v)=M(uv)=M(v)M(u)`. Consequently the final
pair is at most

    (G_p + (p/q)(Pi-1)G_q, Pi*G_q)

coordinatewise, times `|H|/|B|`. This proves (B3-p) and (B3-q), and
proves order independence without choosing a favourable order. At each
step the changed side is still its original `b_i`; all other sides
have only grown. Hence `qa < min b_i` remains sufficient. Equality
`p=q` is allowed. First failing line: none.

## 3. Theorem SH: domain and recursion — HOLDS AFTER CORRECTION

Source: `gap-seed-shape.md:89–95,106`. In line 89 explicitly require
**positive integers** `p,q`: replace its second sentence by

> Let j be an integer at least 2, and let 1 <= p <= q be integers
> with p dividing j and qa < min_i b_i.

This is the domain already required by B3 at line 74. Without it,
`p=q=-1` satisfies the printed arithmetic conditions but makes
`phi(0)` undefined and calls for negative transfer times. This is a
statement-domain omission, not a failed positive-time argument.
Every listed application already has positive p and q.

On this domain, repeated multiplication of the nonnegative excited
spectral sums gives `S(pa;B) <= s^p` and `S(qa;B) <= s^q`.
B3 multiplies the volume by `j^3`; taking `exp` and then using
`S(ja;jB) <= S(pa;jB)^(j/p)` gives the displayed phi exactly.
The integer exponent `j/p` is essential. Scaling all four sides
preserves every ratio and therefore C and Pi. No unexplained spatial
monotonicity of S is used. For `s=0`, read the gap statements in the
extended sense `m=+infinity`; otherwise assume `s>0` when taking logs.
The rank-one case propagates by E2 and requires no division by zero.

## 4. Theorem SH (i) — HOLDS on the corrected domain

Source lines 95–97,107. Write `Q=Ks<1` and `A=log(1/Q)>0`.
If `K s_k <= Q^(j^k)`, then `s_k <= s <= x_0`, since `Q<1`.
Thus the local bound for phi applies again and

    K s_(k+1) <= (K s_k)^j <= Q^(j^(k+1)).

This includes the initial equality at k=0. The excited spectral sum
contains the largest excited ratio to the power `a_k`, so

    m(B_k) >= [j^k A + log K]/a_k
            = A/a + log K/(j^k a).

Compactness and simplicity of the top eigenvalue ensure a strictly
positive finite-box gap, with `+infinity` allowed if there is no
positive excited eigenvalue. The condition `K x_0 <= 1` is sufficient
but unnecessary: `K s<1` already keeps the actual orbit inside
`[0,x_0]`. The stated result does not need this redundancy removed.
First failing line after the domain correction: none.

## 5. Theorem SH (ii) — HOLDS on the corrected domain

Source lines 98–100,108. The maximal integer k gives
`j^k max b_i <= L < j^(k+1) max b_i`. At time `a_k` E2 with
`t'=t=a_k`, applied to each spatial direction, therefore has product
of exponents

    product_i L/[j^k(b_i-a)]
      <= [j rmax/(rmin-1)]^3 = E.

Every side is enlarged, and every denominator is positive. This
proves `1+S(a_k;L^3) <= (1+s_k)^E`. If `E s_k <= 1`, then
`S(a_k;L^3) <= exp(E s_k)-1 <= e E s_k`, proving the stated lower
bound after (i). If `E s_k>1`, put `D=log(eE/K)`. From (i),

    exp(-j^k A) = Q^(j^k) >= K s_k > K/E,
    j^k A < log(E/K) < D.

Hence `[A-j^(-k)D]/a` is negative and the already positive finite-box
gap supplies the bound. This verifies the additional case in the
lead note directly. The argument covers every integer L in the
interval; it never assumes that L is an integer multiple of a seed
side. First failing line after the domain correction: none.

## 6. Theorem SH (iii) — HOLDS on the corrected domain

Source lines 102,109. With A and D as above, (ii) tends to `A/a`.
For `D<=0` the bound is already at least `A/a`; choose `k_0=0`.
For `D>0`, any nonnegative integer `k_0` with `j^k_0 >= 2D/A`
gives `m(L^3)>=A/(2a)` for all `L>=j^k_0 max b_i`. There are only
finitely many integer sides between `max b_i` and this cutoff. Each
has positive gap, so their minimum together with `A/(2a)` is
positive. This proves both the infimum and the liminf assertions.
No uniformity in coupling or in the seed is inferred. First failing
line after the domain correction: none.

## 7. SH's sufficient constant — HOLDS

Source line 104 and its proof at line 110. Put
`u=j^3[log(1+x^p)+C log(1+x^q)]`. Positivity of p,q gives C>=0 and

    0 <= u <= j^3 x^p (1+C x_0^(q-p)),   u <= u_0.

Since `exp(u)-1 <= u exp(u_0)`, raising to `j/p` gives exactly the
printed expression for `K^(j-1)`. The conditions on `K x_0` and
`K s` remain to be checked; the formula alone does not supply them.

For the following arithmetic I use a different, elementary bound:

    exp(u)-1 <= u/(1-u/2),             0 <= u < 2.          (R)

Indeed `n! >= 2^(n-1)` for n>=1; sum the resulting geometric series.
This is a hand proof, with rational operations below. If `u <= D x^p`
and `0<=x<=t` with `D t^p<2`, (R) gives
`phi(x) <= [D/(1-D t^p/2)]^(j/p) x^j`.
No calculator, script, interval enclosure or floating-point output
is evidence for any inequality below.
Strict comparisons involving a positive power of x below take `0<x<=t`;
at x=0 every map vanishes and the required non-strict bound is equality.

## 8. Ratio 3, threshold 1/100 — HOLDS

Source lines 122,133. With `(j,p,q)=(2,1,2)`:
`beta_i=3`, `Pi=27`, `C=13`, `j^3 C=104`. Thus
`phi=[(1+x)^8(1+x^2)^104-1]^2`. For `x<=1/100`,

    u <= (8+104/100)x = 9.04 x,     u <= 0.0904 < 1/10.

By (R), `exp(u)-1 <= (9.04/0.95)x < 9.6x`, since
`9.6*0.95=9.12>9.04`. Therefore `phi<92.16x^2<98x^2`.
The printed `K=98` works and `Kt=0.98<1`; equality at the stated
threshold is permitted. This also proves the weaker printed bound
`phi<=97.94x^2` without depending on its rounded exponentials.
The interpolation constant is `E=(2*3/(3-1))^3=27`.

## 9. Ratio 4, threshold 1/25 — HOLDS

Source lines 123,134. With `(j,p,q)=(2,2,3)`:
`beta_i=4`, `Pi=64`, `C=42`, so `j^3 C=336` and `j/p=1`.
For `x<=1/25`,

    u <= (8+336/25)x^2 = 21.44 x^2,
    u <= 21.44/625 = 0.034304 < 0.035.

By (R), `phi <= (21.44/0.9825)x^2 <22x^2<22.2x^2`, since
`22*0.9825=21.615>21.44`. Thus `K=22.2=111/5` works and
`Kt=111/125=0.888<1`. The interpolation constant is
`E=(8/3)^3=512/27`. The printed intermediate `22.19` bound also
follows from the stronger bound 22 above. As a separate check of
B3's mixed term, `4*(4+16+64)=336`, exactly as at source line 134.

## 10. Ratio 6, threshold 1/10 — HOLDS

Source lines 124,135. With `(j,p,q)=(2,2,5)`:
`beta_i=6`, `Pi=216`, `C=(2/5)*215=86`, `j^3 C=688`.
For `x<=1/10`,

    u <= (8+688/1000)x^2 = 8.688x^2,
    u <= 0.08688 < 0.09.

By (R), `phi <= (8.688/0.955)x^2 <9.1x^2<9.48x^2`, since
`9.1*0.955=8.6905>8.688`. Thus the stated `K=9.48=237/25`
works with `Kt=0.948<1`. The printed intermediate `9.477` bound
also follows. Here `E=(12/5)^3=1728/125`.

## 11. Ratios at least 24, threshold 3/10 — HOLDS

Source lines 125,136. With `(j,p,q)=(6,6,12)` and `r>=24`:
`beta_i=r/(r-12)<=2`, `Pi<=8`, `C<=(1/2)*7=7/2`.
Thus `j^3=216`, `j^3 C<=756`, and `j/p=1`.
For `x<=3/10`, `x^6<=729/10^6` and

    u <= 216[1+(7/2)(729/10^6)] x^6 = D x^6,
    D < 216*1.0026 = 216.5616 < 217,
    u < 217*(729/10^6) = 0.158193 < 0.16.

By (R), `phi <(217/0.92)x^6<236x^6`, since
`236*0.92=217.12`. Meanwhile

    (3.03)^5 = 3^5(1+1/100)^5 >243*(1+5/100)=255.15>236.

So `K=3.03` works and `Kt=0.909<1`. This supplies, in particular,
the weaker printed `253.62x^6` bound without its decimal exponential
estimate. For cube interpolation retain `E=(6r/(r-1))^3`, bounded
above by `(144/23)^3` for all these ratios.

## 12. Ratio 2, threshold 1/1650 — HOLDS; table parameters need correction

Source lines 116,121,138. E2 three times from `(a,(2a)^3)` to
`(a,(4a)^3)` gives `1+s' <= (1+s)^64`: each exponent is
`4a/(2a-a)=4`. If `s<=1/1650`, (R) gives

    s' <= 64s/(1-32s) <= (52800/809)s <66.6s,
    s' <= 32/809 <1/25                     (800<809).

The ratio-4 result applies with **seed s' and K'=22.2**. Moreover

    K's' <=22.2*66.6s =1478.52s <1479s,
    1479/1650 =493/550 <1.

Thus the threshold, including equality, and rate
`A/a=log(1/(1479s))/a` hold. The claimed improvement over the earlier
ratio-2 threshold is valid.

**HOLDS AFTER CORRECTION for the blanket table description at line 116.**
The number 1479 is a composed rate constant, not SH's normalization
constant for the new shape. Replace the two-stage row's parameter
promise by:

> Set B'=(4a)^3 and s'=S(a;B'). Apply SH with j=2, K'=22.2,
> x_0=1/25 and seed s'. Since K's'<=1479s, for k>=0,
> S(2^k a;2^k B')<= (1479s)^(2^k)/22.2 and
> m(2^k B')>=A/a+log(22.2)/(2^k a). For L>=4a, take the
> corresponding k and E=512/27 in (ii). The liminf is at least A/a.
> The infimum over all integer L>=2a is positive, including the
> finitely many smaller cubes by their simple top eigenvalues.

Reading line 116 literally with the listed K=1479, the original
seed s, and the reached sides of line 121 would assert `s'<=s`
at k=0. That is false. A hand example makes the distinction concrete.
For `0<z<1`, define the symmetric model

    Z(n)=product_mu (1+z^(n_mu))^(|n|/n_mu).

For spatial box B of volume V its transfer operator is
`c_B diag(1,z)^(tensor V)`, where
`c_B=product_(mu in B)(1+z^(b_mu))^(V/b_mu)`.
It is positive, finite rank and has a simple top eigenvalue;
`Tr T_B^a=Z(a,B)` and `S(a;B)=(1+z^a)^V-1`.
For each fixed spectator pair, ell is finite because
`0<=log Z(n)/|n|<=4 log(2)/3` on the domain of sides at least 3.
Take `a=3`, `B=(6,6,6)`, `V=216`, `z=1/100`. Then

    0<s<216/999892<1/1650,
    s'=(1+s)^8-1>s.

The first bound follows from (R) with `u=216/10^6`; the last
comparison is `216*1650=356400<999892`. This refutes only the
literal unchanged-seed normalization. It does not refute SH or the
1/1650 criterion. The source's actual two-stage proof uses the
correct s', so Theorem 4' below is unaffected.

## 13. The other two ratio-2 entries — HOLD with strict seed bounds

Source lines 120,129–132 and the lead note's point 4.
For `(j,p,q)=(2,1,1)`, `Pi=8`, `C=7`, hence the exponent is 64.
Put `t=31/131072` and `K=1/t`. The standard bound
`exp(u)-1<=u exp(u)` yields

    phi(x)/x^2 <=4096 exp(128x)
                 <=4096 exp(128t)<1/t.

For the last inequality, `4096t=31/32` and `128t=31/1024<1/32`;
`log(1-y)<-y` with `y=1/32` proves `(31/32)exp(1/32)<1`.
Also `t>1/4229`, since `31*4229=131099>131072`.
Using the printed K requires `s<t`; at `s=t` its condition `Ks<1`
is not satisfied. No endpoint claim is imported from the table.

For `(j,p,q)=(3,1,1)`, the exponent is `27*8=216`. At
`x<=1/3500`, `u<=216x<1/16`, so (R) gives

    exp(u)-1 <=(216*32/31)x <223x,
    phi(x)<223^3 x^3=11089567 x^3<12250000 x^3=3500^2 x^3.

Thus K=3500 is valid, again using `s<1/3500` with that K.
The interpolation exponents are respectively E=64 and E=216.
These proofs replace the source's rounded exponential evaluations.

## 14. Large-ratio family and unequal boxes — HOLD

Source lines 126,137,144–148. For `r>=4j`, `(p,q)=(j,2j)` gives
`Pi<=8`, `C<=7/2`, and
`u<= (9/2)j^3 x^j` when `0<=x<=t<1`. Since
`j^3 t^(j-1)->0`, choose j with `9j^3 t^(j-1)<1`.
Then `u<1`, so (R) gives `phi<=9j^3 x^j`. Taking
`K=(9j^3)^(1/(j-1))` gives `Kt<1`. The limit of the sequence used
here follows, for example, because the ratio of successive terms is
`t(1+1/j)^3`, eventually bounded by a number less than 1. This
proves the lower-threshold limit in Section 1.5. It makes no claim
about an optimal fixed ratio or the separate Ising ceiling.

For `B=(2a,4a,4a)`, `(j,p,q)=(2,1,1)` gives
`Pi=32/9` and exponent `8Pi=256/9`. At `x<=1/880`,
`u<=(256/9)x<=16/495`. Thus (R) gives

    exp(u)-1 <=[14080/487]x <29x,
    phi<841x^2.

Choosing `K=841` proves the stated threshold `1/880`, including
its endpoint, with `Kt<1`. The interpolation constant can be
`E=(2*4/(2-1))^3=512`. The shape enters phi only through Pi;
it also enters E in SH (ii). Read the sentence at line 146 about
“Pi only” as referring to the recursion, not the interpolation cost.
Section 1.7's restriction to `p=q=1` when `1<r<=2` follows from
`1<=p<=q<r`. Section 1.8 is explicitly GUIDE; no verdict about
its run or its reported number is supplied here.

## 15. Theorem D-shape (a) — HOLDS

Source lines 163–168,176. In `F(t,B)=t e(B)+g(t;B)`, the term
linear in t cancels from `2F(a,B)-F(2a,B)`. Since
`0<=g(2a;B)<=g(a;B)`, the result lies between g(a;B) and
2g(a;B). Exponentiation gives precisely both displayed bounds for
S. No small-seed hypothesis is needed. First failing line: none.

## 16. Theorem D-shape (b) — HOLDS

Source lines 163,170,176. Cancellation gives
`Psi=g(a)+g(2a)-g(3a)`. Monotonicity gives the lower bound g(a).
Dropping the last, nonnegative term gives the upper bound, since
`S(2a)<=S(a)^2`. In particular,

    S(a) <= exp(Psi)-1 <= S(a)+S(a)^2+S(a)^3.

Thus the corrected loss factor is `1+t+t^2` when `S(a)<=t`.
The factor `1+t` would omit the cubic term from the product
`(1+S(a))(1+S(a)^2)`. First failing line: none.

## 17. Theorem D-shape (c) — HOLDS

Source lines 171,176. The bulk term cancels because
`a-(a/k)((k+l)-l)=0`. The remainder is the stated
`g(a)+(a/k)[g(l)-g(k+l)]`. Its excess over g(a) is nonnegative
and at most `(a/k)g(l)`. The domain supplies positive k and
valid trace times a,l,k+l. First failing line: none.

## 18. Theorem D-shape (d) — HOLDS for the Wilson normalization

Source lines 172,176 and `gap-crux-restate.md:31`.
There are `6t|B|` plaquettes on the four-torus. Normalized Haar
measure gives F(0)=0, and differentiating its finite compact-group
integral gives `F'(t,B)=-6t|B| abar_(t,B)`. Therefore

    Phi'_B(a)=12a|B|[abar_(2a,B)-abar_(a,B)].

Integration from 0 to beta proves the formula with its sign and
factor 12. This clause is specific to this action and normalized
measure; it is not an identity for an arbitrary abstract Z without
those definitions. First failing line: none.

## 19. Theorem D-shape (e) — HOLDS

Source lines 173,176. The largest excited ratio contributes
`exp(-a m(B))` to S(a;B). Hence
`Phi_B(a)>=g(a;B)>=log(1+exp(-a m(B)))`. The formula also holds
with m=+infinity in the rank-one case. First failing line: none.

## 20. Theorem D-shape (f) — HOLDS

Source lines 174,176. The large torus term cancels exactly in
`Phi(n)-Phi_B(n)`, leaving `16F(n^4)-2F(n,(2n)^3)`.
Schatten monotonicity in each of the three spatial directions gives
`F(n,(2n)^3)<=8F(n^4)`. This proves the sign, independently of
the sign of either free energy. Combining (a) and (f) also recovers
the required input `S(n;(2n)^3)<=exp(Phi(n))-1`.
First failing line: none.

## 21. The free-energy seed criteria and numbers — HOLD

Source lines 178–182, with the already stated strictness for rows
whose printed Kt equals 1, and the two-stage interpretation above.
By D-shape (a),(b), either `Phi_B<=log(1+t)` or
`Psi_B<=log(1+t)` gives `S(a;B)<=t`. SH then applies on exactly
the domains checked above. The loss factor `1+t+t^2` follows from
point 16. The source's gas comparison is GUIDE and is not used.

The quoted logarithmic cutoffs also admit short rational proofs.
For x>0, `log(1+x)>x-x^2/2`; for x=1/10 its alternating expansion
through the negative fourth term gives a lower bound. Thus

    log(1+1/1650)>3299/5445000>121/200000=0.000605,
    log(1.01)>0.00995>0.0099,
    log(1.04)>0.0392,
    log(1.1)>0.1-0.005+1/3000-1/40000>0.0953.

For the first rational comparison the cross-products are
659800000>658845000. The fourth follows because
`1/3000-1/40000=37/120000>0.0003`.

## 22. Theorem 4' — HOLDS given its named strong-coupling input

Source lines 294–302. I opened `gap-seed-sc.md:30–47,57–61,140–148`.
Its Theorem 1 (iii) is the input, including the radius `R=1/12800`
and its periodic polymer hypotheses. Its coefficient is
`2048/12800=0.16`: the two logarithmic remainders have weights
`16*6+96=192`, and `192*(32/3)=2048`. The polymer constant
32/3, the radius 1/12800 and the zero order 4n are supplied
premises here, not newly checked expansion estimates. The input
requires n>=4 for order 4n; Theorem 4' respects that restriction.

Let `theta=12800 beta` and `P=0.16(n theta^n)^4`.
If `n theta^n<=247/1000`, then the exact arithmetic is

    (247/1000)^4=0.003722098081<0.00373,
    0<=Phi<=P<0.0005968<0.000597.

By (R),

    s<=exp(Phi)-1<=Phi/(1-Phi/2)<1.0004 Phi
      <0.0005972388<0.000598<1/1650.

The factor 1.0004 is valid because
`1.0004*(1-0.000597/2)>1`. Now `s'<=66.6s<1/25`, and
SH applies with `a=n`, `B'=(4n)^3`, `K'=22.2`.
The volume interpolation constant and rate coefficient are

    E=512/27<19,
    eE/K'=e*(2560/2997)<2.33,
    K's'<=1479s<=1479*1.0004*0.16 n^4 theta^(4n)
                    =236.734656 n^4 theta^(4n)
                    <237 n^4 theta^(4n).

Here is a hand certificate for the only exponential constants.
Summing the exponential series through degree four, and bounding
its remaining tail geometrically, gives
`e<=65/24+1/100<68/25=2.72`. Hence
`e*(2560/2997)<174080/74925<233/100`.
Also the series for `exp(17/20)` through degree four is
`8967761/3840000>233/100`, so `log(2.33)<0.85`.
All denominators are positive.

For the maximal k with `2^k 4n<=L`, SH (ii) therefore gives

    m(L^3) >= [log(1/(K's'))-0.85*2^(-k)]/n
      >=4 log(1/theta)
        -(4 log n+log 237+0.85*2^(-k))/n.

This is the stated conclusion. It uses 22.2, rather than 1479,
in `log(eE/K')`; the source's proof does so correctly.
First failing line in this conditional theorem: none.

## 23. Independent hand test and Section 6 consequences — HOLD as scoped

For the source's example `theta=1/2`, choose n=5:
`n theta^n=5/32<247/1000`. Instead of rounding three logarithms
separately, combine them exactly:

    4 log 2-(4 log 5+log 237)/5
      =(1/5)log[1048576/148125].

The previous hand bound `e<68/25` and `exp(1/20)>21/20` give

    exp(39/20)<92480/13125<1048576/148125.

The last comparison is the integer inequality
`13698600000<13762560000`. Thus the common term is strictly
greater than 0.39. Theorem 4' gives **m>0.22** for `20<=L<40`,
**m>0.305** for `L>=40`, and liminf at least the exact common
term, which is **greater than 0.39**. This hand test uses one exact
rational logarithm, not the source's decimal evaluation route.
Also `4*(1/2)^4=1/4>247/1000`, so n=4 is correctly excluded.
These are consequences of the named input theorem, not measurements
of the Wilson spectrum.

The comparison with the old constant is consistent:
`5041*2*0.16=1613.12<1614`, using `s<=2Phi` and upstream S3'.
The new constant is 237 with the explicitly retained interpolation
term. The enlarged range of seeds and the change from `L>=2n`
to `L>=4n` are both real; neither changes the coefficient
`4 log(1/theta)`.

The last bullet at source line 310 **HOLDS given the additional
Theorem 2 input and n>=5**, as the lead note specifies. For fixed
n, that input says
`Phi=192n^3(beta/4)^(4n)(1+O(beta))`. Since
`s<=exp(Phi)-1=Phi(1+o(1))` and `K's'<=1479s`, the same bound
gives the stated liminf after subtracting `4 log(4/beta)`;
`192*1479=283968`. Neither the strong-coupling leading coefficient
nor the recalled physical mass is independently proved by this check.
The n=4 coefficient differs in the input and is not covered by this
last asymptotic bullet. No statement here supplies the seed at
couplings of order one.

## Own-verdict checkpoint, before the earlier Claude report

All verdicts above were written before opening
`gap-seed-shape-check.md`. The scope has been completed: E2; both
B3 inequalities; SH's recursion, (i)–(iii) and sufficient constant;
all requested thresholds and adjacent used specializations;
D-shape (a)–(f); free-energy criteria; Theorem 4' and its hand test.
There is no failed positive-time theorem or failed threshold among
these. Two parameter statements need the explicit corrections in
points 3 and 12. The transfer construction, the periodic polymer
expansion and the Section 3–5 model claims remain outside this check.
Next and only remaining scientific task: read the earlier Claude
check and record every disagreement in this scope with source lines.

## 24. Comparison with the earlier Claude check

Only after point 23 and its checkpoint were on disk did I open
`gap-seed-shape-check.md:1–242`, written by Claude Opus 5.5 high.
The SHA-256 of this report **before that reading** was
`9eed5d9599a287beb73e7c155800d824af8c1e0fd07c1250c8ea4d9eb1f176a1`.
The source lead note had already disclosed its summarized verdicts;
this ordering does not claim blindness to that requested note.

I agree with Claude's E2/B3 derivations (lines 46–52), its SH
positive-time argument (54–65), the five requested thresholds
(76–81), D-shape (93–103), and Theorem 4' (161–172), subject to
the precise qualifications below. I also agree with the scope,
strict-endpoint, free-energy loss-factor and n>=5 corrections
already in the source lead note. I make no comparison verdict on
the Ising/Gaussian claims outside the present task's coverage.

### 24.1 SH's parameter domain: an additional correction

Claude labels the recursion HOLDS at lines 54 and 189 without
noting the omitted `1<=p` in source line 89. The counterexample
`p=q=-1` in point 3 shows why the literal statement needs correction.
**The corrected positive-integer statement is right.** Claude's
argument establishes that statement, and all its numerical uses
have the correct domain. There is no disagreement about those uses.

### 24.2 The two-stage K: agreement in the proof, correction to the table

Claude explicitly uses **K=22.2** at line 76 and calls 1479 a rate
constant at lines 38 and 196. That is right and agrees with point 12.
The source table at lines 116,121 still promises SH (i)–(iii) with
the listed K=1479 and does not state the changed seed normalization.
Its literal unchanged-seed version is false by point 12's finite
trace example. **Claude is right about the actual two-stage proof;
the table needs my displayed parameter correction.** This is not a
new disagreement about the threshold or Theorem 4'.

### 24.3 Claude line 22: the general power-series claim FAILS

This is a new disagreement with an auxiliary claim in the earlier
check, not with SH. A positive real power of `1+x^q` need not
have nonnegative Taylor coefficients. Take the admissible SH data
`a=3`, `B=(6,9,51)`, `j=2`, `p=q=1`. Then

    Pi=2*(3/2)*(17/16)=51/16,
    phi(x)=[(1+x)^(51/2)-1]^2
          =(1+x)^51-2(1+x)^(51/2)+1.

The coefficient of x^52 in phi, and hence of x^50 in phi/x^2,
is `-2 binom(51/2,52)<0`. The binomial product has 26 positive
and 26 negative factors, so it is strictly positive. Thus the
first sentence at Claude line 22 is false. **This counterexample
settles that sentence in favour of the present correction.**

Corrected text: “For the two integer-exponent maps tested below,
phi/x^j is a polynomial with nonnegative coefficients, so its
maximum on the seed interval is at the endpoint. General SH data
need a separate monotonicity argument.” The fixed-point estimates
for those two maps are not refuted by this error. Their decimal
values remain unnecessary to the rational certificates here.

### 24.4 Claude line 163: the intermediate 1.0003 bound FAILS

Claude claims `(exp(x)-1)/x<=1.0003` for `x<=6*10^(-4)`.
At `x=6*10^(-4)`, the first three terms already give

    (exp(x)-1)/x >1+x/2 =1.0003.

Even its stated upper expression `1+x/2+x^2/2` exceeds 1.0003
there. **The displayed auxiliary bound is wrong; the needed
1.0004 is right.** Replace it by

    (exp(x)-1)/x <=1/(1-x/2)<1.0004,
                       0<x<=0.0006.

At the endpoint this uses `1.0004*(1-0.0003)=1.00009988>1`.
Alternatively retain the smaller actual range `x<0.000597` to
justify 1.0003. Point 22 already proved the required 1.0004 before
this comparison. Theorem 4' and its constant 237 are unaffected.

These are all disagreements in the checked scope. The two false
auxiliary sentences in the earlier report do not invalidate any
of the five requested thresholds or the named positive-time
conditional theorems.

## 25. Source integrity and delivery

At final verification the shared checkout had moved externally from
`a867197306ac4eab32466e4ab6fe86e92e9ad89c` to
`ee962db5bfa8d69490f6973818aac2e17df49b67`, with an unrelated change
in `library/exercise-skill-v2.md`. I did not edit that file or move the
checkout back. The three mathematical source hashes remained unchanged:

| File | SHA-256 |
|---|---|
| gap-seed-shape.md | 8b033032a09cb2acd7ee0958d9d6969b09b32b88bbc41609174865225c9c43f3 |
| gap-crux-restate.md | ee7a5935c32f7e32bf58d189429a5572933e1275505cce7d8e1a9750e0142649 |
| gap-seed-sc.md | 4a95984b7cc7a4c94aea0c54279cd1bb89384d7918871403ac919105f5ed8f93 |

This report is preserved on `work/gap-sh-astra-a86719730`, based on
the requested pin, using the isolated worktree
`/tmp/gap-sh-astra-20261111/worktree`. The requested output also remains
in the original checkout. No source, registry, FINISH row, audit record
or status ledger was edited. No scientific computation or automated
proof was run. File searches, hashes and diff checks are bookkeeping.
