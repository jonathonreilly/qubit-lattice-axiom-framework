## Repo search

The lead's [search](prior/repo-search-2026-11-08.md), §1, covered main and PRs
#10114, #10133, #10134 and #10141. It found conditional PI/GW results,
not a supplier for the whole item-10 domain. `prior/g0-cover.md` is absent
at this checkout. The workflow was read from fetched main.

| Checked hit | Closeness and use |
|---|---|
| #10141, `research/ym4d/library/out-pi.md`, 273–329 | The inverse assumes local gauge admission. This is a consumer, not its supplier. |
| Same PR, `out-gw.md`, 54–64; `layer-thm-part.md`, 1385–1408 | The snapshot expressly retains localized-domain admission. It is this project's prior work. |
| #10114, `RTARGET.md`, 716–725 | Axial gauges for the soft Hessian; its higher-level background hypothesis remains open. Different operator. |
| [g-zero](g-zero.md), [iem-supply](iem-supply.md), G-zero | Exact unresolved seed and complete-read quantifiers. No shift estimate is repeated. |
| [pi-admit](pi-admit.md), §§5.1–5.2 | Supplies the bare-test collar and comb gauge. Reused below. |
| [stage-cubes](stage-cubes.md), [arr](arr.md), §7 | Already supplies transport of assigned cubes. No new proof of that result is attempted. |

The freshly fetched PR heads were `fb99b4dddc7254e6124ac124887d58eeb3a77802`
and `f76f6c649cff7dffbab664d8976e680e8f287fe9`, respectively.
The other PR searches are the lead's recorded searches.
Registry **CA**, owner **ca-claude**, owns completion-collar admission;
that instance is excluded throughout.

Codex; checkout `1a9c11fe67fc7cd4acf432140c02bc6e6cf287b4`.
Research text, not an audit; this grants no scientific status.
Only this file is a repository output. No computational result discharges a step.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text**, and **Tadeusz Bałaban** for the original construction.
The lead authored Lemma A and Fact B in [g0-cover](g0-cover.md).

Source keys are **I** for CA-I and **SA** for the outline, both at
`31a47c543775`, and **Y** for `YM4_1400.tex` at
`2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`. Numbers following these keys are
source lines. Existing `/tmp` copies were reused. The index README, relevant
chunk rows, neighbouring rows and obligations located the outline reads.
Bałaban's CMP **122** (1989), 175–202, pp. 180–182 was checked in the PDF,
not by reconstructing the OCR formulas.

## Step 0: the lead's two statements

**Lemma A: PASS in dimension four.**
For A1, conjugation preserves operator norm. Telescoping four unitary factors
gives the sum of their distances from the identity. Reversing a bond preserves
that distance. Thus the stated $`4a`$ bound is correct without a smallness assumption.

For A2, the comb construction reused from `pi-admit`, (9), fills each bond
loop with at most $`6q`$ plaquettes. The larger constant $`8q`$ is valid.
For an SU(2) matrix within $`1/4`$ of the identity, its principal Hermitian
logarithm has norm at most twice that distance. Therefore

```math
\eta\lVert A\rVert\le16q\varepsilon,\qquad
\eta^2\lVert\nabla A\rVert
=\eta\lVert A(b')-A(b)\rVert\le32q\varepsilon.
```

The neighbouring bonds and both endpoints must be in the same box and gauge.
In the intended small-radius regime $`0<a_\flat^Y\le1`$, with
$`\varepsilon<a_\flat^Y/(32q_B)`$,
the logarithm condition follows from $`8q_B\varepsilon<a_\flat^Y/4\le1/4`$.
The resulting bounds are $`\eta\lVert A\rVert<a_\flat^Y/2`$ and
$`\eta^2\lVert\nabla A\rVert<a_\flat^Y`$.
Necessity uses $`\lVert e^{i\eta A}-1\rVert\le\eta\lVert A\rVert`$.
The corollary also holds without that small-radius convention: for any
SU(2) matrix one can choose a Hermitian traceless logarithm with
$`\lVert-i\log W\rVert\le(\pi/2)\lVert W-1\rVert`$.
Indeed, its eigenvalues are $`e^{\pm i\theta}`$, $`0\le\theta\le\pi`$,
and $`\sin(\theta/2)\ge\theta/\pi`$. At $`-I_2`$ choose an axis for a
logarithm; only existence is used. The comb bound then gives
$`\eta|A|\le4\pi q_B\varepsilon`$ and
$`\eta^2|\nabla A|\le8\pi q_B\varepsilon`$, also sufficient for the corollary.

The necessity and sufficiency statements have different constants. They are not an equivalence
between a gauge on a smaller read and smallness on a strictly larger box.

**Fact B: PASS for the test and exclusion mechanism; WRONG in its data-domain sentence.**
In the actual (1.20), the two data restrictions are

```math
U^{(n)}_{k,Z}
=U\!\left(\mathbb B^{(n)}_k(Z),
 (M(Q_k^{s*}V_k))|_{Z\cap\Omega_k},\quad
 V|_{Z\cap\Omega_k^c}\right).
```

Thus the original determining data are kept on the complement of
$`\Omega_k`$ inside $`Z`$. The substituted data are on $`Z\cap\Omega_k`$.
The lead's sentence reverses those regions. Both restrictions in the display
are inside $`Z`$. This matters at a raw determining bond.

Equations (1.22) and (1.23) do test the localized background itself.
The split is componentwise. Failed components leave the running $`Z`$ and
retain their large-field treatment. Equation (1.24), continued on p. 182,
also carries powers of $`L_0^2`$ on overlapping shells; these cannot be dropped.

## Step 1: the port is present

The searches in both pinned accounts included `B-CMP122a`, `(1.22)`,
`(1.23)`, `decomposition of unity`, `new large field`, `characteristic
function`, `chi^{(0)}` and `regularity conditions by a factor`.
The decisive passages are these:

* **I 54241–54258, 54289–54303:** the stage recursion imports the
  determining sets, localized backgrounds and characteristic functions of
  (1.14)–(1.27). Its integral explicitly contains $`\chi_k^{(n+1)}`$.
* **I 131947–132023:** the nine exits retain the appropriate old tests,
  $`\chi^{(0)}`$, $`\chi^{(n)}`$, $`\chi^{(n+1)}`$ or final tests.
  **I 132163–132174** identifies such exits with new large-field creation.
* **I 105752–105787:** each component carrying the failing factor is removed
  before the next stage integral. The remaining $`Z`$ is renamed.
* **Y 63836, 63864–63876:** the preparation uses localized backgrounds,
  sharper tests, geometric margins and the overlap powers from (1.24).
  **Y 63862** is the failed-test/drop-out rule.
* **SA 17336–17346, 17585, 17610–17630:** the corresponding outline
  construction and stage ladder. The index describes the ladder as sketched,
  not a completed all-domain admission theorem.

Here is the actual plaquette inventory. All regions in the preparation are
intersected with the component being tested. Put $`j=h+n`$ and
$`\eta_i=L^{k-i}\eta`$. These are bounds on fine plaquette holonomies,
not bounds on the logarithm divided by the fine spacing.

| Stage/test | Tested plaquettes | Tested real field | Threshold |
|---|---|---|---|
| Bare $`P_0`$ | Every $`p\subset\square^\sim`$ of a passing bare density cube | Original $`U_{\rm bare}`$ | $`\varepsilon_0`$. Y 61973–61991; `pi-admit` (7)–(8). |
| $`\chi_k^{(0)}`$, (1.22) | $`\Omega_h\setminus\Omega_{h+1}`$ | $`U^{(0)}_{k,Z}`$ | $`(1-\beta/2)\varepsilon_h\eta_h^2`$. CMP 122a p. 181, imported at I 54245–54246. |
| $`\chi_k^{(1)}`$, first row of (1.23) | $`Z''_{h+1}\cap\Omega_h`$ | $`U^{(1)}_{k,Z}`$ | $`[1-\beta(1/2+1/4)]\varepsilon_h\eta_h^2`$. Same sources. |
| $`\chi_k^{(1)}`$, second row | $`\Omega_{h+2}^c\setminus Z''_{h+1}`$ | Same $`U^{(1)}_{k,Z}`$ | $`(1-\beta/2)\varepsilon_{h+1}\eta_{h+1}^2`$. Same sources. |
| $`\chi_k^{(n)}`$, processed shells | $`S_h=Z''_{h+1}\cap\Omega_h`$; $`S_i=Z''_{i+1}\setminus Z''_i`$, $`h<i<j`$ | $`U^{(n)}_{k,Z}`$ | $`[1-\beta(1-2^{-(j-i+1)})]L_0^{2(i-k_0-1)_+}\varepsilon_i\eta_i^2`$. (1.24), pp. 181–182; Y 63876. |
| Unprocessed part, $`j\le k_0`$ | $`\Omega_{j+1}^c\setminus Z''_j`$ | Same $`U^{(n)}_{k,Z}`$ | $`(1-\beta/2)\varepsilon_j\eta_j^2`$. The nonoverlapping version of (1.24); Y 63876. |
| Compressed residual, $`j>k_0`$ | $`\Omega_{k_0+1}^c\setminus Z''_j`$ | Same field | $`(1-\beta/2)L_0^{2(j-k_0-1)}\varepsilon_j\eta_j^2`$. (1.24). |
| Compressed ordinary shells | $`\Omega_l\setminus\Omega_{l+1}`$, $`k_0<l<j-1`$ | Same field | $`(1-\beta/2)L_0^{2(j-l-1)}\varepsilon_j\eta_j^2`$. (1.24). |
| Last ordinary part | $`\Omega_{j-1}\setminus\Omega_{j+1}`$ | Same field | $`c(1-\beta/2)\varepsilon_j\eta_j^2`$, $`c=1`$ for $`j<k`$, $`c=3`$ for $`j=k`$. (1.24). |

Empty ranges contribute no condition. The ordinary old tests remain where
the current stage has no clause; I 136926–136934 specifies that use of
(1.3)–(1.4). The tests on fluctuation variables are additional bond tests;
their thresholds $`\delta_j,\delta'_j`$ are not plaquette thresholds for
an arbitrary analytic source reference.

The distinction between two fields is explicit in the account's own use.
I 136906–136920 first bounds the **localized** background of the frozen test.
I 136936–136950 then compares the current minimizer with that background.
The second field is not renamed as the first in this report. That comparison
is not another proof of G0-SEED, and no estimate on its shift is attempted.

The absence of a new test on the old core is explicit in **Y 63836–63853**:
the carried core factor contains its failed tests and is not unfolded.
The new shell tests and the last-shell test have their separate carriers.
Consequently locating this port does not locate a test of every raw
plaquette of a new response box.

## Step 2: what the tests cover on the original sources

The real-factor definitions must be kept literally:

```math
\begin{array}{ll}
\text{original ambient pair:}&\mathcal W=e^{i\eta A'}U
       \quad\text{(I 110264–110276)},\\
\text{arrested source:}&(\mathbb U,\mathbb J)=(e^{i\eta A'}U,\mathbb J)
       \quad\text{(I 132999–133039)},\\
\text{physical real point:}&(U(\mathfrak B,V),\mathcal J(U))
       \quad\text{(I 136846–136853)}.
\end{array}
```

In the first two rows, $`U`$ is the prescribed unitary factor of the pair.
It is not defined to be $`U^{(n)}_{k,Z}(V)`$ on characteristic-function support.
I 125630–125633 requires an ambient continuation of a stage pair and imposes
the direct clauses on $`Y^+`$. I 103374–103394 separately defines the analytic
stage domain and its physical real points.

The following table gives the verified coverage. It deliberately does not
turn a missing certificate into an **F** classification.

| Source/read | Verified plaquette classification and its limit |
|---|---|
| Bare tested reference on the box of `pi-admit` §5.1 | **T on every plaquette of that box.** The five-layer exclusion and one-layer hull give (8), including the first-difference padding. |
| A restriction agreeing with that reference on the whole box | **T on every plaquette**, by equality of the four bond values. Equality only of block averages does not suffice. |
| A stage or T-step retaining the source's real factor | Each plaquette inherits its source's classification on the same pulled-back read. Use `g-zero`'s established identities, I 131577, 117492–117508 and 136538–136555. No new T certificate is created by this transport. |
| Physical localized stage background | **T precisely on the Step-1 sets**, with that stage's thresholds. An arbitrary raw box is not one of those sets: the preparatory ladder starts at $`h\ge1`$. |
| A newly introduced constrained minimizer | **M only where the data hypothesis is supplied.** I 43113–43139 requires smallness on every determining plaquette, $`\varepsilon_1\le a_1`$ and $`B_3\varepsilon_1\le\varepsilon_0`$. Its conclusion is $`\lVert\partial U-1\rVert<B_3\varepsilon_1\eta^2\ell_{\mathfrak B}^{-2}`$ (I 43140–43155). It does not certify unspecified raw data. |
| Original analytic stage, arrested, stored-birth and later-image sources at an unmatched raw read | The cited source clauses supply no **full-box T** test for their prescribed $`U`$. The minimizer theorem supplies no unconditional **M** classification there. No legal one-bond freedom on a complete native read has been proved here, so **F is not asserted**. |

This last row has an exact textual location. Item 10 lists its ambient
conditions at **I 131725–131739**. The original ambient class at
**I 110264–110276** requires (3.35), (3.37) and a current bound. The original
raw rider lists the same members at **I 133022–133039**. The stage's seven
direct inequalities start at $`m=1`$ (**I 131340–131364**).
The account expressly explains this index-zero omission at
**I 140938–140968**. The cube clause has its class-hull restriction,
**I 52471–52527**. None of these definitions inserts the required test on
every plaquette of $`B(\widehat q)`$ for the real factor of an arbitrary source pair.

In particular, the apparent all-location notation for the direct clauses
at I 119467–119495 cannot silently supply an extra raw-curvature clause:
**I 136211–136223, 136253–136277** expressly identifies the original raw
source/consumer clause as $(3.35)_0$, $(3.37)_0$ and the current member,
and says that stages create no clause at a raw point. The inherited-domain
definition **I 119652–119720** adds lettered and diminished term clauses;
it does not identify its generic unitary factor with a field on the
physical characteristic-function support.

The account also contains a **later, explicit repair**, which must be credited:
**I 140979–141054** defines the never-averaged collar, its pinned plaquettes
and the real-curvature entry $`Q_5`$. **I 141135–141161** imposes

```math
Q_5(y)<\mathsf f_0(d)\alpha_{0,0},\qquad
\mathsf f_0(d)=4-\mathfrak s(d)\le4.
```

It explicitly replaces the old index-zero kernel-class clause. This is not
a proof that every point of the original domain already satisfied it.
It controls pinned plaquettes **of** $`\Omega_0`$; plaquettes with a corner
in $`\Omega_1`$ use the positive-level clauses. It does not assign exterior
values or test a padding plaquette outside $`\Omega_0`$.
Y 1251–1283 likewise explicitly requires raw curvature and the response's
whole gauge cubes as structured-domain hypotheses.
Importing either strengthened domain would change the original-domain question.

For example, on a box consisting entirely of these pinned plaquettes,
the later clause suffices once
$`128q_B\alpha_{0,0}\le a_\flat^Y`$.
This follows directly from Lemma A. It is an implication on that strengthened
domain, not the missing original-domain inclusion.

## Step 3: the located omission and the cost of adding the test

**Located absence:** the original item-10 source definitions do not contain
the same-reference, complete-box plaquette test. The claim that the account
has no port of $`\chi_k^{(n)}`$ is false. The absent condition is the extra
coverage condition on the analytic source, not the physical stage test.
This is a located omission in the source definitions, not a proof or a
counterexample to G0-SEED on its unchanged domains. It also does **not**
meet the narrower third alternative in `g0-cover`, which requires absence
of the $`\chi_k^{(n)}`$ port: that port is present.

The exact domain repair is as follows. Fix the complete pulled-back boxes
before taking any parameter path or supremum. Keep their actual prescribed
bond values, including any stored exterior values. For the original domain
$`D(g)`$, define

```math
\begin{split}
\rho_B&:=\frac{a_\flat^Y}{32q_B},\\
\chi_{0,B}(U)&:=
 \mathbf1\{U\text{ is defined on every bond of }B,
       \ \lVert\partial U(p)-1\rVert<\rho_B\text{ for every }p\subset B\},\\
D_{\rm cov}(g)&:=
 \{P\in D(g):\chi_{0,B}(U_P)=1
        \text{ for every required noncompletion box }B\}.
\end{split}
```

Restate item 10 with its original determining sets, constants and complex
parameters, replacing its source by $`D_{\rm cov}(g)`$ in the domain inclusion.
Keep the prescribed unitary factor fixed in each analytic chart.
The characteristic function restricts the allowed real centers; it is not
inserted as a holomorphic function of the complex field.
Lemma A supplies G0-SEED on this restated domain, with the constants checked
in Step 0. It does not prove the other assertions of the layer theorem.

The threshold comparison for an existing stage test is, exactly,

```math
C_{n,i}\varepsilon_i(L^{k-i}\eta)^2
   <\frac{a_\flat^Y}{32q_B}.
```

Here $`C_{n,i}`$ includes both the overlap power and the possible factor $`3`$.
Since $`\eta=L^{-k}`$, its left side is
$`C_{n,i}\varepsilon_iL^{-2i}`$, not $`C_{n,i}\varepsilon_i\eta^2`$.
The overlap ratio is $`(L_0/L)^2<1/4`$ per compensated level.
For the bare test this comparison is simply
$`32q_B\varepsilon_0<a_\flat^Y`$.
A coupling ceiling used for all reads must be chosen after a uniform bound
on their box sizes and the other constants; it cannot be chosen separately
after an unmatched read appears.

### Consumer check

The complete later-operation list is I 132280–132301. It requires containment
of the **image of the source**, not merely admission of its physical points.
The item-10 formula, its named localized-layer input and their uses were
searched throughout I. The direct use is the interrupted-change lemma;
the later consumers are its stored terms and the arrest theorem.

| Consumer | Only actual tested fields? | Consequence of the repair |
|---|---|---|
| Physical identification of $`H_\sigma`$ at $`\sigma=1`$, I 131740–131749; original real comparison, I 137560–137566 | Yes for this identification, on the stated real support. It tests the specified localized field and regions, not automatically every new $`B`$. | Supply the full-box comparison above before claiming G0. |
| Holomorphic lift and shifted arguments, I 137569–137613 | **No.** The assertion is on $`\widehat{\mathfrak D}^{\flat}_{n+1}`$; the real range is discussed separately at 137615–137617. | The domain of the lift and the resulting $(\beta3)$ terms must change at birth. |
| Frozen $(\beta3)$ terms, I 137404–137419 and 137732–137742 | **No.** These are functions on prescribed analytic domains, with an ambient continuation. | Their full-box real-center restriction must travel with the stored birth domain. |
| O1, sibling stages; O3, T-steps; O4 and O4$'$, later stages, I 132285–132295, 137674–137693 | **No.** The theorem quantifies over every member of each arrested source. | Preservation of the unitary factor transports an existing certificate only on the same complete read. The source must supply every newly required box. |
| O2, completion elsewhere; O5, dissolution, I 132287–132299 | **No.** These also require source-image inclusion. | On their noncompletion reads, the same domain requirement applies. The completion-collar instance stays with CA. |
| Later bounds and auxiliary arguments, I 139108–139123, 139241–139248, 139350–139356 | **No.** Rim parameters and lifted variables range in stored domains; the $(\beta3)$ field domain is inherited. | Restricting only the final physical evaluation cannot justify these suprema and substitutions. |
| Numerical ceilings involving $`H_{\max}`$, I 131827–131839, 131867–131898 | No field evaluation occurs here. | A smaller domain preserves a supremum bound already proved there; these ceilings do not prove the omitted domain inclusion. |

Thus the price of the analytic repair is an explicit change to the source,
birth-domain and substitution assertions. Physical tests alone do not pay
that price. In particular, restricting a final integral to its test support
does not establish a holomorphic bound over the old full source domain.

### Failed components: the available small factor and its restriction

For a physical summand, insert $`1=\chi_{0,B}+(1-\chi_{0,B})`$ before using
that box. Group these splits by component and freeze a failed component,
as in I 105752–105787 and 131947–132023. The split preserves the integral
algebraically. No small factor follows from that identity alone.

The account already locates its payment in **SA 17676–17713** and, more
fully, **Y 71592–71603, 72126–72146**. Ordinary creations have the stated
factor $`e^{-c p_0(g_t)^2}`$. Operation failures have the stated factor

```math
e^{-c\check R_j^{-C}p_1(g_j)^2}\le e^{-p_0(g_j)},
\qquad 2\mathfrak p_1-Cr>\mathfrak p_0.
```

The remaining stored integrations cost $`e^{C\#_t(D)}`$.
These are their stated estimates on their witness classes; they are not
newly proved by this note. Y 72134 expressly requires the full averaging
and contour carriers to match the configuration carrying the Wilson weight.
Y 72142–72146 forbids using a previously spent old-core plaquette for a
new drop-out payment.

For a test of the **same** SU(2) plaquette as an available Wilson weight,
the additional price can be stated exactly. With their normalized plaquette
action, diagonalizing the SU(2) matrix gives

```math
a_p(U)=1-\tfrac12\operatorname{Re}\operatorname{tr}\partial U(p)
      =\tfrac12\lVert\partial U(p)-1\rVert^2.
```

A failure at $`p`$ implies $`a_p(U)\ge\rho_B^2/2`$.
If $`x_p a_p`$ is an unspent Wilson exponent and at most $`D_*`$ failures
claim it, allocating half its exponent gives, per assigned failure,

```math
\exp\!\left[-\frac{x_p\rho_B^2}{4D_*}\right]
=\exp\!\left[-\frac{x_p(a_\flat^Y)^2}{4096D_*q_B^2}\right].
```

This is a hand calculation, conditional on the explicitly named allocation.
It is not a fresh gain when that plaquette has already paid for an older
failure. Nor does it apply to a different localized reference merely because
the two fields have the same spatial address. Thus the exact cost is the
displayed action share **plus** the domain changes in the consumer table;
the old large-field bound cannot be cited without its same-field and unspent-share
hypotheses.

## Disposition

The physical $`\chi_k^{(n)}`$ port is located, including its thresholds,
field identities and failed-component rule. The required complete-box
test is absent from the **original analytic-domain clauses** inspected above.
Its exact addition and cost are given here. The later collar replacement
already in the account is credited and is not silently imposed on the old domains.

No all-source T/M cover or legal F plaquette is certified by this report.
Consequently the existing $`-I_2`$ construction in `g-zero` is not promoted
to an actual-source counterexample. G0-SEED on the unchanged original
domains remains unproved and unrefuted. The new domain gives the stated
conditional seed implication. This source-location result grants no status.
The requested closure has not been reached: the table does not classify
every required plaquette as T, M or F. In particular, neither the absence
of an explicit test nor freedom outside the class hull alone verifies an
original source and a required native read containing the proposed defect.
