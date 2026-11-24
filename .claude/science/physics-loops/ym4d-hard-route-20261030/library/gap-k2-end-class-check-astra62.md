# Repo search

Row 1473, OpenAI/Codex, gpt-6.2-astra max, checkout `0c5f04b82`. Cross-provider research check of Claude Fable 5.2 medium's [row 1471](gap-k2-end-class-fable.md). This report grants no status.

The lead's [November 8 search](prior/repo-search-2026-11-08.md) predates Q2. I checked the YM4D research and soft-route trees on main (`8b11ae2bb`) and PRs 10114, 10133, 10134 and 10141 (`f76f6c649`, `89faef229`, `1e70c7211`, `a2f6a430e`) for the endpoint and entry labels. None matched. The hit in row 1468 §9, PR 10114's `checks/review_massgap_block_literature.md`, lines 112–122 and 163–170, separates twisted-sector control from entry into strong coupling and supplies no entry theorem. Here [Theorem E](gap-mini-nphys-fable.md) uses a centre split and product reference, [END-D](gap-mini-neutral-step-fable.md) gives a two-period bound for box windows, and [BS](gap-blockstep-fable.md) assumes block mixing. [Row 1468, §§3.1–3.2 and 4.2](gap-k2-tool-design-fable.md) supplies the field spaces, Q2 and the weighted rule. Among the library sources only rows 1468 and 1471 contain END-K2. The target-specific prior note is absent. The open registry names no other owner for this check.

R. Kotecký and D. Preiss supply the abstract polymer criterion (Commun. Math. Phys. **103**, 491–498). The outline's chunk 01 and its obligations point to the finite rooted estimate. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, prove it under an explicit activity hypothesis. Their complete account imports Tadeusz Bałaban's two-block locality and gauge covariance. The side-two contour geometry here comes from row 1468. The strong-coupling gauge-theory expansion is due to Konrad Osterwalder and Erhard Seiler. [Outline, lines 1271–1366](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1271-L1366) · [CA-I, lines 43013–43074](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L43013-L43074)

## Verdict

**HOLDS AFTER CORRECTION.** The weighted end class gives purity at least $457/625$. At design strength $\kappa=\beta$, the listed $\beta=1/40000$ is certified, and $v=242$ is the least integer satisfying (E-v) for $r=0.7$, $m=512v$. With the repaired E1 parameters the largest entry allowed by those two inequalities lies between $0.0000255038036$ and $0.0000255038037$. Over all positive strengths and free parameters the sharp supremum for this criterion is $\log(1+1/(42e))$, strictly between $0.008720$ and $0.008721$. In particular $\beta=0.00871$ is admissible. This corrects the claimed strict ceiling $0.0087$.

## Check plan

1. Check prior coverage and the indexed source passages.
2. Verify the norm loss, the abstract criterion, the twisted-period comparison and the end constants.
3. Derive the Q2 counts, verify formation of the coarse rule and bound the entry arithmetic exactly.
4. Determine the range in coupling that the stated criterion certifies.

## Weighted rule and polymer expansion

**Step 3, lines 85–103. HOLDS.** Counting bond–plaquette incidences gives $4\,\#p(X)\le6|X|$ and hence $E_X\le3|X|$ for the normalized quaternion trace. For loss $h>0$, each term in the supremum norm at rate $r-h$ costs at most $M=\sup_{n\ge1}(1+3\theta x n)e^{-hn}$ times its weighted term at rate $r$. The bound $M\le1+3\theta x/(eh)$ follows by maximizing $u e^{-hu}$ on the positive reals. This uses bond count for size. Lines 105–109 illustrate how the norm scales on Wilson actions. Inclusion of such actions in a ball leaves their purity unresolved.

**KP-F, lines 115–161. HOLDS for real functions.** For complex functions the conclusion is nonvanishing and a distinguished logarithm. For example, one constant $f=i/100$, $a=1/10$, $d=0$, satisfies (CR) and has mass $1+i/100$. For real functions self-touch gives $\phi_E\le a(E)e^{-2a(E)}\le1/(2e)<1$, so every factor is positive. Both applications have real weights. Taking real parts also preserves the realization inequality for a positive density.

The expansion into touching components factors under product Haar. Put $u_E=\phi_E e^{a(E)+d(E)}$. Deleting a root element from a connected set gives unordered components each with a possible touching child. Summing all child choices and dropping disjointness overcounts. The $k!$ orderings cancel the $1/k!$. Thus the rooted sum with the root weight removed is at most $e^{a(E)}$ by induction and (CR). For a polymer $S$, use the **field-independent** activity majorant $w_S=e^{d(S)}\prod_{E\in S}\phi_E$. The sum of $w_{S'}e^{a(S')}$ over polymers touching $S$ is at most $a(S)=\sum_{E\in S}a(E)$. In the outline's rooted criterion mark one occurrence of an incompatible $S'$ in the cluster, then sum the root estimate multiplied by $w_{S'}$. This bounds the unmarked touching sum by $a(S)$, including repetitions. For a link use the same argument over polymers through that link, bounded by $a_0$. These bounds dominate the sum of the individual suprema over the external field, as EN requires.

## Twists and the two-period estimate

**§4.2, lines 174–191. HOLDS with a common-lift restriction in (c).** On a lift of a short element, the sign of a crossed cut is the coboundary of the parity of the number of cut planes passed in each twisted spatial direction. Multiply these site signs over the three directions. Translation covariance and centre gauge invariance make the element independent of its period representative. On distinct links modulo the time period the change of variables is a deterministic central sign on each Haar variable. A support with no time winding lifts isomorphically to the cylinder, so its integral on that torus is twist independent. To compare two tori the same elements and overlaps must project injectively to both. For an example even with full gauge invariance, take $v=8$, $m=16$, $z=0$. Let $P_j$ be the holonomy of the same spatial plaquette at time $j$. Join consecutive plaquettes by a time bond to form connected elements, and put $f_j=h(P_j)h(P_{j+1})$ for $0\le j<8$, with $h(g)=\tfrac12\operatorname{Re}g$. Then $\Phi_j=-\log(1+f_j)$ defines translated real local functions. Distinct slices give independent Haar plaquette holonomies. On the longer torus the end variables occur once, so the polymer activity is zero. On the shorter torus $P_8=P_0$, and the activity is $(\int h^2)^8>0$. The short-cluster cutoff below supplies the restriction needed by END-K2.

**END-K2, lines 195–248. HOLDS for the stated realization.** For each time side $\tau=v,2v$, let $Z_+(\tau)=\tfrac18\sum_z Z^z(\tau)$ on the spatial torus of side $m$, and let $P=Z_+(2v)/Z_+(v)^2$. The sixteen densities realize one rule with a common site constant and wrap error $\eta$. Write $q=r-2\alpha-t>0$. With $\epsilon_*=\alpha e^{-\alpha}/M(\theta x,q)$, the bond sum of $(e^{\|\Phi_X\|_\infty}-1)e^{(2\alpha+t)|X|}$ is at most $\alpha e^{-\alpha}\exp(\alpha e^{-\alpha})\le\alpha$. A projected element through a fixed bond has a unique lift through its chosen representative because its extent is below half the shortest side. Summing over its bonds gives (CR). A cluster of total bond count $N<v/2$ has time extent below $v/2$ on the cylinder. If $m<v$, both tori impose the same spatial diameter cutoff. If $v\le m$, the bound on $N$ meets the smaller cutoff. Thus the cover has exactly two lifts per short cluster, with identical activities and Ursell multiplicities, even when the cluster winds spatially. Those contributions cancel between $2v$ and two copies of $v$. At period $\tau$ the absolute long-cluster tail is at most $4m^3\tau\alpha e^{-tv/2}$ by the link bound. The three tails give $16\alpha m^3v e^{-tv/2}$, the site constant cancels, and the realization errors cost $3\eta$. Comparing two twists at one period gives $2\eta+8\alpha m^3\tau e^{-tv/2}$ in the logarithm. Taking minima and maxima over twists also bounds the averaged masses.

For $\eta\le1/100$, (E-v) is $16\alpha m^3v e^{-tv/2}\le283/1000$. It suffices because $e^{313/1000}<625/457$. Since $v e^{-tv/4}\le4/(et)$, a sufficient threshold is $v_E(m)=(4/t)\bigl(3\log m+\log(64\alpha/(0.283et))\bigr)$, together with $v\ge4$. With $\alpha=r/8,t=r/2$, the additive log constant is $\log(16/(0.283e))<3.04$. The least integer calculated below uses (E-v) itself.

### End constants, §4.4

For $w=\theta x$, the successive ratios of $(1+3wn)e^{-rn/4}$ decrease with $n$. Testing the two neighbours determines the integer maximum. For the default parameters the exact radius is $(r/8)e^{rn/4-r/8}/(1+3wn)$. On the consumer's shape put $H_r(v)=2r\,512^3v^4e^{-rv/4}$. In the following table each value of $M,\epsilon_*,H_r$ is the **lower endpoint** of an interval one unit wide in its last printed place. The column headed “safe radius” gives the value that may be used in the theorem.

| $r$ | $w$ | maximizing $n$ | $M$ | $\epsilon_*$ | safe radius | least $v$ | $H_r(v-1)$ | $H_r(v)$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3 | 2.3 | 13 | 34.21134 | 0.001055783 | 0.00105 | 601 | 0.2987 | 0.2790 |
| 0.7 | 2.3 | 6 | 14.83736 | 0.005403194 | 0.0054 | **242** | 0.3059 | 0.2611 |
| 1 | 2.3 | 4 | 10.52135 | 0.010484594 | 0.0104 | 165 | 0.3034 | 0.2421 |
| 1 | 1 | 4 | 4.78243 | 0.023066108 | 0.0230 | 165 | 0.3034 | 0.2421 |
| 2 | 2.3 | 2 | 5.44461 | 0.035760135 | 0.0357 | 78 | 0.3593 | 0.2294 |
| 4 | 2.3 | 1 | 2.90624 | 0.104349447 | 0.104 | 37 | 0.4183 | 0.1717 |

All six printed upper bounds for $M$ and all six safe radii pass. The threshold is exactly $283/1000$. Since $H'_r/H_r=4/v-r/4$, the function increases up to $16/r$ and then decreases. In these rows $H_r(4)>0.283$ already, using $e^4<81$. The adjacent tests therefore prove minimality. The sufficient default size is $(8/r)(3\log m+3.04)$, and rounding $8/r$ upward as in §4.4 is safe. At $r=1$, $24\log m+25$ is safe as well. At $r=0.7$ on the line $m=512v$, the sufficient formula first passes at 459, or 462 with its printed prefactor 11.5. For these last two tests $v/c-3\log(512v)-3.04$ first decreases, then increases for $v>3c$, and is negative at 4. The smaller **242** comes directly from (E-v).

Line 276's large-$r$ assertion needs deletion or a cap on the *chosen* sufficient radius. With fixed $w>0$ the maximizing $n$ is 1 for all sufficiently large $r$, and $\epsilon_*=(r/8)e^{r/8}/(1+3w)$ grows without bound.

## The Q2 step

**§5.1, lines 283–311. HOLDS.** For $c=(y,\mu)$, each endpoint cube has $4\cdot2^3=32$ internal edges. A prefix of a coordinate-order path reaches any chosen lower endpoint and takes the chosen edge. Reversal gives the same coverage in the other cube. The two-step straight runs cross the common face on $2^3=8$ parallel edges and use 8 internal $\mu$-edges in each cube. These three disjoint sets give $|B_c|=72$. An internal fine link belongs to the eight coarse bonds incident to its cube's base, while a crossing link determines one coarse bond. A fine plaquette meets itself and five other plaquettes at each of its four edges, giving 21. Its coarse corners occupy one, two, or four cubes. The touching coarse bonds then number 8, $8+8-1=15$, or 4. A coarse bond meets the two endpoint stars (15 including itself) and at most $72\cdot6=432$ plaquettes by incidence. Each fine link lies in six plaquettes and at most eight bond supports. The number 432 is an upper bound with repeated incidences. For the kernel, $1\le Z_c(t)\le e^{t^2/8}$ follows termwise from $(j+1)!\ge2^j$. The lower factor bound used in line 291 follows from $e^{-\kappa-\kappa^2/8}\ge1-\kappa-\kappa^2/8\ge2-e^\kappa$.

**EN, lines 313–371. HOLDS for the translation-covariant rule with centre gauge invariance.** Fix the external coarse field. The preceding counts give (CR) with the two row sums $21A+15B,432A+15B$ and fine link bound $a_0=6A+8B$. Under projection onto coarse cubes a fine plaquette gives a site, an edge, or a square. Touching elements share a coarse site. Thus a mixed cluster has a connected coarse bond set $X$ of size at most $n_c+4n_p$, with multiplicities counted on the right. Each edge of $X$ is either a bond element or is traversed by a crossing fine link of a plaquette. In both cases the cluster touches that bond's $B_c$. Its exponential weight pays $\lambda e^{r|X|}$. At lines 338–348, taking a pointwise bound alone would exchange a supremum and a sum in the wrong direction. Apply KP-F instead to the common $w_S$ above. This gives $\sup_c\sum_{X\ni c}e^{r|X|}\|\Phi_X\|_\infty\le a_c/\lambda$ on increasing boxes. Absolute uniform convergence gives continuity. Extending a coarse gauge change to the fine corner bases proves full gauge invariance under the Haar integrals. The original design's extra reflection covariance is outside the stated variant.

For the wrap estimate, $|X|<s/2$ gives an injective coarse lift, and every fine variable lies in its endpoint cubes. The fine and coarse cut signs agree on corners by the sign identity in row 1468 §3.2 (Lemma TW). Short torus clusters therefore give exactly the same local functions. The large-size tail of the infinite rule and the large-size torus tail each cost $4m^3\tau(a_c/\lambda)e^{-rs/2}$. For a connected cluster of $n$ fine plaquettes, lift successively across shared edges along a spanning tree. Each added square extends any coordinate by at most one. For $n<2s$ the resulting box is injective in the fine torus, including all overlap relations. Let $k$ sum pure infinite-lattice shapes with their lexicographically first site at the origin. The site constant in the coarse action is $e=-16k$. Per fine site its omitted tail is at most $4a_0 e^{-8rs}$ because summing the link bound over four orientations counts each translation orbit at least once. There are $16m^3\tau$ fine sites and $64m^3\tau$ fine links. The two pure tails together cost $128m^3\tau a_0 e^{-8rs}$, as in line 328. EN-K2 retains the explicit hypothesis that both wrap errors are at most $1/100$. Line 369 needs a numerical check of the error for the chosen parameters. Twist-wise mass preservation gives the same purity for the fine Wilson measure. For its neutral spectrum write $s=\sum_{i>0}r_i^{2v}$ with $0\le r_i\le1$. Then $P\le1/(1+s)$ gives $s\le168/457<1$, and $P\le(1+s^2)/(1+s)^2$ gives $s\le4/21$ by monotonicity on $[0,1]$. This verifies the corollary's time index.

### Wilson entry arithmetic, §5.3

Use $A=(e^\beta-1)e^{2a_p+4r}$, $B=\lambda(e^\kappa-1)e^{2a_c+r}$ and **exactly** $\lambda=a_c/\epsilon_E$ with the safe radius. For E1 and E2 the displayed decimal $\lambda$ rounded down and violates the claimed equality, even putting $a_c/\lambda$ above the stated safe radius. E3 rounded up. The following bounds use the exact fractions. Each of the last five columns gives a lower rational endpoint with upper endpoint $10^{-8}$ higher.

| Entry | $(r,a_p,a_c)$ | $(\beta,\kappa)$ | $\lambda$ | $A$ | $B$ | $21A+15B$ | $432A+15B$ | $a_0$ |
|---|---|---|---:|---:|---:|---:|---:|---:|
| E1 | $(0.7,0.2622,0.5)$ | $(1/40000,1/40000)$ | $2500/27$ | 0.00069456 | 0.01267133 | 0.20465589 | 0.49012284 | 0.10553806 |
| E3 | $(0.3,0.2622,0.5)$ | $(10^{-4},9\cdot10^{-6})$ | $10000/21$ | 0.00056094 | 0.01572562 | 0.24766423 | 0.47821201 | 0.12917068 |
| E2 | $(0.3,0.5,9.5)$ | $(1/500,3\cdot10^{-15})$ | $190000/21$ | 0.01806808 | 0.00653941 | 0.47752113 | 7.90350573 | 0.16072387 |

For E1, line 388's upper bound fails already at $x+x^2/2$ for $x=1/40000$. The correct enclosure is $0.000025000300<e^x-1<0.000025000313$. The common factor $e^x-1$ multiplies $e^{8311/2500}$ in $A$ and $(2500/27)e^{17/10}$ in $B$. Thus the first sum is below $20465590/10^8<1311/5000$ and the second below $49012285/10^8<1/2$. All three rows satisfy (CR-EN), also at smaller couplings with the same strength ratios by monotonicity. For both periods at $m=512v$, the bound $\eta\le16m^3v(\epsilon_E+16a_0)e^{-rv/2}$ is below $e^{-40}$ at 242 in E1 and at 601 in E3 and E2. It decreases thereafter.

At these fixed E1 parameters with $\kappa=\beta$, both row sums increase as $e^\beta-1$. The coarse-bond constraint reaches equality first. The exact largest $\beta$ supplied by this instance is

$$
 \log\!\left(1+\frac{1/2}{432e^{8311/2500}+15(2500/27)e^{17/10}}\right)
 \ \in\ (0.0000255038036,\;0.0000255038037).
$$

The plaquette constraint is still strict at the upper endpoint. There $a_0<0.108$, which also gives the stated wrap bound at $v=242$ throughout this interval. The simpler $1/40000$ survives every repair. E3 and E2 likewise retain their stated sufficient couplings. Optimizing over all choices at the fixed strength ratio $\kappa/\beta=1$ is a different extremum from the one computed in this display.

## Strength-independent ceiling

**Lines 392–395. HOLDS AFTER CORRECTION.** Since $B>0$,

$$
 e^\beta-1<e^{-4r}\frac{a_p e^{-2a_p}}{21}
 \le\frac{e^{-4r}}{42e}.
$$

The sharp supremum over the positive strengths and the free parameters of (CR-EN) is therefore $\beta_{\rm sup}=\log(1+1/(42e))$. To see sharpness, fix any $0<\beta<\beta_{\rm sup}$ and take $a_p=1/2$, $a_c=11$. At $r=0,B=0$ both constraints are strict since $21(e^\beta-1)e<1/2$ and $432(e^\beta-1)e<432/42<11$. Choose $r>0$ small, then $\lambda\ge\max(1,11/\epsilon_*)$, then $\kappa>0$ small. Continuity preserves both strict inequalities. All constants are now fixed. Along $m=512v$ the two wrap errors and the (E-v) left side vanish as $v\to\infty$. Thus any such $\beta$ gives a finite-size entry, although equality at the supremum is impossible. For an explicit violation of $0.0087$, use $\beta=871/100000$, $r=1/10000$, $a_p=1/2$, $a_c=11$, $\lambda=10^{12}$, $\kappa=10^{-30}$, $w=2.3$. The two row sums are strictly below $0.49958$ and $10.277$. Here $M<276001$ and $(r/8)e^{-r/8}>1/160000$, so $\epsilon_*>1/(160000\cdot276001)>11/10^{12}$. Large enough $v$ meets the two finite-size conditions. The sharp supremum bounds this strong-coupling criterion. Entry from Wilson coupling near 2.3 is still open.

## Exact arithmetic and replay

Every displayed decimal endpoint is a rational number. For $0\le u\le1$, put $T_{14}(u)=\sum_{j=0}^{14}u^j/j!$. The omitted positive terms have successive ratios at most $1/16$, so $T_{14}(u)\le e^u\le T_{14}(u)+2u^{15}/15!$. All arguments of the exponential routine below lie in $[0,64]$. It halves until the argument is at most one, then squares each nonnegative interval, rounding its lower endpoint down and its upper endpoint up to multiples of $10^{-16}$. For $e^x-1$ the lower bound is $P=x+x^2/2+x^3/6+x^4/24$. The upper bound adds $x^5/[120(1-x/6)]$, by the same ratio argument, for every $0\le x<6$ used here. Multiplication and division of positive intervals preserve the indicated ordering.

Lean 4.36.0 (commit `611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9`) checked the rational inequalities in the following source. Its three theorems use `decide +kernel`, without `native_decide` or a compiled proof oracle. The axiom report for each lists `propext`, `Classical.choice` and `Quot.sound`. The real-exponential enclosures and the polymer arguments are the written proofs above. Python helped locate rational endpoints. The source replays with `lean -j1 Check1473.lean` and Lean's standard library.

<details>
<summary>Standalone Lean source for the two tables, wrap bounds and coupling limits</summary>

```lean
import Std

set_option maxRecDepth 100000
set_option maxHeartbeats 0

abbrev Box := Rat × Rat
def pt (x : Rat) : Box := (x, x)
def scaleB (x : Rat) (b : Box) : Box := (x*b.1, x*b.2)
def mulB (a b : Box) : Box := (a.1*b.1, a.2*b.2)
def addB (a b : Box) : Box := (a.1+b.1, a.2+b.2)
def overB (x : Rat) (b : Box) : Box := (x/b.2, x/b.1)

def hor (x : Rat) : Nat → Rat → Rat
  | 0, s => s
  | n+1, s => hor x n (1+x*s/((n+1 : Nat) : Rat))
def small (x : Rat) : Box :=
  let p := hor x 14 1
  (p, p + 2*x^15/1307674368000)
def squareB (b : Box) : Box :=
  let d : Rat := 10^16
  (((d*b.1^2).floor : Rat)/d, ((d*b.2^2).ceil : Rat)/d)
def expAux : Nat → Rat → Box
  | 0, x => small x
  | n+1, x => if x ≤ 1 then small x else squareB (expAux n (x/2))
def ex (x : Rat) : Box := expAux 6 x
def em (x : Rat) : Box :=
  let p := x+x^2/2+x^3/6+x^4/24
  (p, p+x^5/(120*(1-x/6)))

def binOK (b : Box) (n d : Nat) : Bool :=
  decide ((n : Rat) ≤ d*b.1 ∧ d*b.2 < (n : Rat)+1)
def H (r v : Rat) := overB (2*r*512^3*v^4) (ex (r*v/4))
def endRow (r w : Rat) (n v mi ei prev curr : Nat) : Bool :=
  let q := r/4
  let a := r/8
  let c := 3*w
  let j : Rat := n
  let f := 1+c*j
  let peak := decide ((1+c*(j-1))*(ex q).2 ≤ f ∧ 1+c*(j+1) ≤ f*(ex q).1)
  peak && binOK (overB f (ex (q*j))) mi 100000 &&
    binOK (scaleB (a/f) (ex (q*j-a))) ei 1000000000 &&
    binOK (H r (v-1 : Nat)) prev 10000 && binOK (H r v) curr 10000

def sums (r b k ap ac lam : Rat) : List Box :=
  let A := mulB (em b) (ex (2*ap+4*r))
  let B := scaleB lam (mulB (em k) (ex (2*ac+r)))
  [A, B, addB (scaleB 21 A) (scaleB 15 B),
   addB (scaleB 432 A) (scaleB 15 B), addB (scaleB 6 A) (scaleB 8 B)]
def bins (xs : List Box) (ns : List Nat) : Bool :=
  xs.length == ns.length && (List.zipWith (fun x n => binOK x n 100000000) xs ns).all id
def e1 (b : Rat) := sums (7/10) b b (1311/5000) (1/2) (2500/27)
def wrapOK (r v ep a0 : Rat) : Bool :=
  decide (16*(512*v)^3*v*(ep+16*a0) < (ex (r*v/2-40)).1)
def sideCross (c : Rat) (v : Nat) : Bool :=
  let h (u : Rat) := overB ((512*u)^3) (ex (u/c-76/25))
  decide (1 < (h (v-1 : Nat)).1 ∧ (h v).2 < 1)
def threshold (b : Rat) := scaleB 42 (mulB (ex 1) (em b))

theorem checkedEnd :
    [endRow (3/10) (23/10) 13 601 3421134 1055783 2987 2790,
     endRow (7/10) (23/10) 6 242 1483736 5403194 3059 2611,
     endRow 1 (23/10) 4 165 1052135 10484594 3034 2421,
     endRow 1 1 4 165 478243 23066108 3034 2421,
     endRow 2 (23/10) 2 78 544461 35760135 3593 2294,
     endRow 4 (23/10) 1 37 290624 104349447 4183 1717,
     sideCross (80/7) 459, sideCross (23/2) 462,
     decide ((ex (313/1000)).2 < 625/457 ∧ 16 < 283/1000*(ex (404/100)).1)].all id = true := by decide +kernel
#print axioms checkedEnd

theorem checkedEntry :
    [bins (e1 (1/40000)) [69456,1267133,20465589,49012284,10553806],
     bins (sums (3/10) (1/10000) (9/1000000) (1311/5000) (1/2) (10000/21))
       [56094,1572562,24766423,47821201,12917068],
     bins (sums (3/10) (1/500) (3/10^15) (1/2) (19/2) (190000/21))
       [1806808,653941,47752113,790350573,16072387],
     wrapOK (7/10) 242 (27/5000) (108/1000),
     wrapOK (3/10) 601 (21/20000) (161/1000),
     decide (250003/10000000000 < (em (1/40000)).1 ∧ (em (1/40000)).2 < 25000313/10^12)].all id = true := by decide +kernel
#print axioms checkedEntry

theorem checkedLimits :
    let lo := e1 (255038036/10^13)
    let hi := e1 (255038037/10^13)
    let w := sums (1/10000) (871/100000) (1/10^30) (1/2) 11 (10^12)
    w[2]!.2 < 49958/100000 ∧ w[3]!.2 < 10277/1000 ∧
      hi[2]!.2 < 1311/5000 ∧ hi[4]!.2 < 108/1000 ∧ lo[3]!.2 < 1/2 ∧ 1/2 < hi[3]!.1 ∧
      (threshold (872/100000)).2 < 1 ∧ 1 < (threshold (8721/1000000)).1 := by decide +kernel
#print axioms checkedLimits
```

</details>
