# PRE-STATED

Recorded before reading `KFACTOR_OFF55.md` or its check results, on 2026-10-28.
Scope: independent hostile mathematical review of the supplied local source;
no git, no source-file repairs, and no writes outside this file. The requested
reviewer is Codex gpt-6-astra at max effort; the session provides no independent
model-configuration attestation, so this report does not invent one. No audit
or retained-status promotion is attempted.

Let `L/` denote `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The user's description, including the desired mechanism and expected control,
is prior exposure; none of its conclusions is accepted as evidence.

Review order and falsification criteria:

1. **CCP(d):** trace every source entering the composite inverse. Check the
   exact divergence cancellation, root restrictions, operator domains, and
   both implications between fixed points and slice critical points. A
   nonlinear Faddeev–Popov inverse cannot be silently assumed.
2. **HR(iii)–(iv):** derive the routing and telescoping identities, including
   endpoints and mesh factors, independently of the runner.
3. **CB:** derive the complete level sums and their norm weights. Uniformity
   means constants independent of both depth `k` and torus size `T` at each
   fixed `sigma > 0`; distinguish a quadratic upper bound at `sigma = 0`
   from a matching lower bound or actual operator growth.
4. **SG:** check exact factorization through `Theta = exp(rho) - 1`, the
   differentiated factors at arbitrary order, and whether the stated local
   analytic bounds actually transfer the claimed scale decay.
5. **Theorem K:** recompute scale exponents and the ratio `L^(-sigma)` from
   the declared source and output norms. Verify radius/smallness uniformity,
   the precise role of the one remaining input, and the restriction to the
   composite inverse rather than per-level covariances.
6. **OC:** distinguish failure of the displayed estimates from a proof that
   every argument under the named inputs fails. Check matching domains,
   residuals, quantifiers, possible cancellations, and any actual obstruction
   witness.
7. **ko55_1:** inspect its implementation before execution, reproduce exact
   identities on the stated eight lattices, and independently test the
   claimed one-step versus level-by-level routing costs. Finite checks do
   not certify uniform estimates or nonlinear fixed-point equivalence.

All computed arithmetic will use integers, rationals, or exact symbolic
identities; no floating-point tolerance will establish a claim. Every verdict
will be **CONFIRMED**, **NOT-VERIFIED**, or **REFUTED**, with a source file and
locating string. A counterexample must satisfy the stated hypotheses; a proof
gap alone earns NOT-VERIFIED. The report will end with exactly what may be
banked, keeping conditional statements conditional.

---

## Source and scope

This is a review of the local files, not a claim about a git revision or current
main. The complete 684-line target and 372-line runner were read in `sed`
ranges; dependencies were located with `rg` and read in bounded ranges.
The target's appended errata, including the corrected level-`l+1` factor and
Bernoulli threshold, are included. Only this report was written.
The target, runner, criteria, and hashed dependencies below were rechecked
unchanged at the closing source-identity check. The PRE-STATED date uses
the workspace's America/New_York calendar; the closing check was on
2026-10-29 UTC.

SHA-256 identities:

| File under `L/` | SHA-256 |
|---|---|
| `KFACTOR_OFF55.md` | `6a47b6543bfefa31f8eb103ff057c4d64b38a97a48f35a195caa70367a9c3159` |
| `checks/ko55_1.py` | `534469aaefecf6dbe0b6a7c20d21724e03481f4a3fced307f3aa5a628c431e1c` |
| `checks/ko55_1_criteria.md` | `75f6b04a5e5bff858246c3cc6ea0d710c974fde9ef1b1ebd7c14c8b6618632ed` |
| `BFT_A.md` | `8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0` |
| `BFT_B.md` | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| `CODEX_REVIEW_C2.md` | `36180292c9324dfd526404e91b76ef1ee9651db27e91cfabab4a418ded6dcddb` |
| `REVIEW_S22.md` | `e7df10f9dc13220399896e320ece04de19b3f9d6b9865062d1723ab5cc20341f` |
| `PROOF.md` | `02beb7dff29d1e23ae4cd8e890480b4d52d28adb55af457a78c4f9ebca309efd` |

The mathematical review follows the requested order. There are two important
distinctions in its outcome. The routing/preconditioning construction survives.
The literal local estimate `(LA-1)` is false, but its intended replacement has
a local analytic proof, supplied below. The claimed impossibility on the
Feynman/Γ_E route is not established by the displayed upper bounds.

## 1. Proposition CCP(d): the critical-point correspondence survives

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `Proposition CCP` and
`Fixed points are exactly the slice critical points`; inputs: `BFT_A.md`,
`33.3 Lemma CD`, `Lemma FG (gauge-fixed responses)`, and `CODEX_REVIEW_C2.md`,
`CD proves annihilation on that test-function space`.

Write `D_* = D^⊥`, identifying its values with a function extended by zero
at level-k roots, and `C = P^T`. The necessary identities are

    D_* C = I,        H Ξλ = 0,        D_*(NB) = 0,
    D_* 𝔑⁰(x;B) = −(K′_xᵀ ∇F(x;B))_* .

Every λ here is root-pinned. The last identity follows directly by
differentiating (GI): `K_0 = −Ξ`, so `D_*∇F = (K′ᵀ∇F)_*`.
There is no equation at an unpinned root hidden in this calculation.

Consequently, for every input x, including a noncritical input,

    D_*[NB + 𝔑⁰(x;B) − C D_*𝔑⁰(x;B)] = 0.

If `y = 𝓛_Γ⁻¹ S̃`, pair its equation with `Ξλ`. One obtains
`<Γy, ΓΞλ> = 0`. The stipulated surjectivity of ΓΞ onto Ran Γ implies
`Γy = 0`, hence `Hy = S̃`. This proves the source-domain assertion before
using any critical-point conclusion. It is not circular application of a
critical-point estimate to an iterate.

Substitution, with the sign from the root-pinned Ward identity, gives exactly

    Φ̃_Γ(x) = x − 𝓛_Γ⁻¹[(I − C(K′_xᵀ·)_*)∇F + ΓᵀΓx].

### The norm estimate and strict threshold

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `The M_x estimate` and
`Erratum to 3.4 (d)`.

For a link X, the two coefficients of its endpoint generators are

    ψ₋(ad_X) = ad_X/(exp(ad_X)−1),
    ψ₊(ad_X) = ad_X/(1−exp(−ad_X)).

Their nonconstant coefficient absolute sum is `c_Bern`. With `|X|≤1/2`,
`||ad_X||≤2|X|≤1` gives

    |K′_X(a,c)| ≤ 2 c_Bern |X| (|a|+|c|).

Transposition and the `2d` incident links give a level-j charge u_j satisfying
`||u_j||∞ ≤ 4d c_Bern ||x_j||∞ ||g_j||∞`. HR(v) then gives

    J(C ev_jᵀu_j)
      ≤ [M_γ/(L−1)] L^{d(k−j)} 4d c_Bern
         L^{−(k−j)}||x_j^c||∞ L^{−(d−1)(k−j)}π_j(g_j)
      = 2d c_Bern L^{d−1} ||x_j^c||∞ π_j(g_j).

Summing over j proves precisely the stated J→J estimate, with no depth or
volume factor. Removing root values before applying C has no effect, by
HR(i).

The constant can also be bounded independently of the runner's Bernoulli
recurrence. Let `f(t)=1−t cot(t)`. Its even coefficients a_n satisfy

    (2n+1)a_n = 1_{n=1} + Σ_{p+q=n} a_p a_q,

so they are positive. The identity
`ψ₋(2it)=t cot(t)−it` gives
`c_Bern = 1/2+f(1/2) = 3/2−(1/2)cot(1/2)`.
Alternating Taylor bounds give, using rationals only,

    cos(1/2) ≥ 1−1/8+1/384−1/46080,
    sin(1/2) ≤ 1/2−1/48+1/3840,
    c_Bern ≤ 3691/6312 < 59/100.

Thus at d=4, L=3 the certified threshold is
`η′ < 25/3186`; the convenient strictly safe choice
`η′ ≤ 25/6372` makes the operator norm at most `1/2`.
This agrees with the target's corrected threshold, not its original decimal.

At a fixed point, Γx=0 and `M_x∇F=0`. Since J is a norm on the finite chain
space, `||I−M_x||_{J→J}<1` implies `∇F=0`. Conversely, if `∇F=0` and Γx=0,
the Ward identity makes the correction vanish and `S̃=Hx=𝓛_Γx`.

This proves exactly **full critical points of F that lie in Ker Γ** are the
fixed points in the stated small region. It does not by itself identify
stationary points of an arbitrarily restricted functional `F|Ker Γ`, or
prove every nearby gauge orbit meets the nonlinear slice. The source's
separate `(FP♯′)` qualification for uniqueness modulo gauges must remain.
No nonlinear Faddeev–Popov inverse is used in this argument.

## 2. Lemma HR(iii)–(iv): the mesh factors and flux cancellation are correct

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `Lemma HR`, `Sup route`,
`Hölder route (level 0)`, and `V_i(Z) = Σ_μΣ_{lines}`.

The proof works for every odd L≥3, every depth, and periodic tori with the
stated nested block roots. A path from the parent root to Z has divergence
`δ_Z−δ_root`. Summing at level j leaves V_j at its sites and minus the
parent block sum at its root. Placement in level 0 and summation over j
telescopes, leaving

    D(Cu) = u − Σ_X (Σ_{z∈cell X}u(z)) δ_{r_X}.

A charge already at a level-k root has empty paths at every level. A charge
placed at a level-l site has empty paths below l. These establish HR(i)–(ii),
including the endpoint/root conventions used by CCP.

For fixed axial coordinate order, a link in direction μ can have at most
`L^{d−μ−1}(L−1)/2` destinations, numbering directions from zero. The largest
value occurs for the first direction, adjacent to the centre, and is attained:

    M_γ = L^{d−1}(L−1)/2.

For `u=ev_lᵀd*w`, the level-i block contains exactly an
`L^{i−l}`-side box of level-l sites. Summing its divergence cancels internal
links. There are `d L^{(d−1)(i−l)}` entering/exiting pairs, hence

    |V_i| ≤ 2d L^{(d−1)(i−l)} ||w||∞,
    π_i((Cu)_i) ≤ 2d M_γ π_l(w),
    J(Cu) ≤ 2d M_γ (k−l) π_l(w).

For l=0, the entering and exiting links of each line have the same
orientation and are exactly `L^i/n` apart in coarse units. This separation
is at most `1/L`, inside the pointwise Hölder domain. Therefore

    π_i((Cd*w)_i) ≤ d M_γ [w^c]^∞_α L^{−α(k−i)},
    Σ_{i=0}^{k−1}L^{−α(k−i)}
       = (1−L^{−αk})/(L^α−1) ≤ 1/(L^α−1).

This uses a difference of opposing boundary values, not their two separate
suprema. Periodic faces obey the same identity; there is no factor T.
For bare charges HR(v) follows instead from
`|V_i|≤L^{d(i−j)}||v||∞` and
`Σ_{i=j}^{k−1}L^{−(k−i)}≤1/(L−1)`.

## 3. Proposition CB: uniform upper bounds survive; a quadratic lower bound does not follow

**CONFIRMED at quadratic order, and for the corrected full-source estimates
proved in §4 below.** Source: `KFACTOR_OFF55.md`, locating `Proposition CB`,
`Proposition ROW`, and `The Wilson plain row is routed by HR (iv)`;
inputs: `BFT_A.md`, `[RBA1-fix] F6`, `13.5 Lemma CR-1`, and
`REVIEW_BFT_A_S6.md`, `Corollary WR`.

A divergence-form source contributes zero to D. A residual-type source has
full divergence `ev_kᵀd*s_{k−1}` after telescoping, and therefore zero
**off-root** divergence. This terminal qualification matters: the calculation
does not assume `(CC-0)`. Thus only the selected plain rows need routing.

The Wilson quadratic row has

    π_0(R_W) ≤ 36η²,
    [(R_W)^c]^∞_α ≤ C_{W∞}η²,
    C_{W∞}=18(2C_C+4·8^α+2d).

Indeed each link meets six plaquettes, each contributes three commutators
with the one-half factor, and `|ad_yᵀF|≤2|y||F|`. This gives the coefficient
18 before `||x_0^c||∞||f_0||∞`. Translate the factors together and use BL-C
on the antisymmetrized gradient to obtain the stated Hölder constant.
The gradient hypothesis required by WR(a) is present in `𝔐^(σ)`.

Put `a=L^(−σ)` and `m=k−1−l`. The soft quadratic rows satisfy

    π_l(R_l^B) ≤ A_B a^m η²,
    A_B = 2p_L κ_+ L².

HR(iii) charges this row `2dM_γ(m+1)A_B a^mη²`. The exact sum is

    Σ_{m=0}^{k−1}(m+1)a^m
      = [1−(k+1)a^k+k a^{k+1}]/(1−a)²
      ≤ 1/(1−a)²                 (0<a<1).

Combining it with the Wilson Hölder route gives the displayed quadratic
`K_C(σ)`. Bilinearity gives its Lipschitz version; §4 gives the replacement
for the complete nonlinear source. Constants may diverge as σ decreases to
zero, or as α decreases to zero. Uniformity claimed and confirmed is in k,T
at fixed admissible α,σ, not uniformity in these exponents.

**NOT-VERIFIED as actual asymptotic growth of the correction.** Source:
`KFACTOR_OFF55.md`, locating `At σ = 0 the same proof gives`, table N8's
`≍ k² at σ = 0`, and the same wording in §9.
At σ=0 the **majorant** is exactly `k(k+1)/2`. This proves an O(k²η²)
upper bound. Neither simultaneous saturation by actual nonlinear rows nor
a matching lower bound is exhibited. The claim that the correction itself
grows like k², or that no uniform estimate is possible at σ=0, cannot be
banked from this argument. This distinction also applies to the O(k)
unrouted row budget.

## 4. Lemma SG: exact identity confirmed; LA-1 is false as printed

### 4.1 Exact soft-gradient factorization

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `Lemma SG` and
`For every variation`; input: `PROOF.md`, `Lemma NA-alg`, especially
`Stationarity` and `G = H + iθ1`.

The envelope derivative is `Re tr(W₀⁻¹δM)`: the omitted derivative of the
maximizer is a stationary tangent variation. Differentiating the other term
gives `−Re tr(V⁻¹δM)+Re tr(ZV⁻¹M)`. Substitution of
`V⁻¹=exp(ρ)W₀⁻¹` and `V⁻¹M=exp(ρ)G` gives

    δ𝔰_c = κ_l[−Re tr(Θ W₀⁻¹δM)+Re tr(Z Θ G)],
    Θ=exp(ρ)−I.

The discarded term is exactly zero:
`Re tr(ZH)=0` and `Re tr(iθZ)=0`, because Z is anti-Hermitian and traceless.
The use of tracelessness is legitimate on NA-alg's small-log branch.

The decomposition with `Ψ=Π(−Θ*)` is also exact, and
`Ψ=ρ+O(|ρ|³)` because the even powers of an anti-Hermitian ρ are Hermitian.
Every plain coefficient in this decomposition contains Θ. This is a
factorization through the **nonlinear** residual ρ; it is not a claim that
the plain part vanishes whenever the linear residual r vanishes.

### 4.2 A literal false local hypothesis

**REFUTED.** Source: `KFACTOR_OFF55.md`, locating
`|∂(W_0^{-1}M̄_c)/∂x_b − Q_{cb}|` in `(LA-1)`.

At the trivial field,

    M=I,       δM=Qδx,
    W₀=I,      δW₀=Qδx,
    δ(W₀⁻¹M)=−δW₀+δM=0.

The displayed estimate has zero right side there but asserts that this
derivative equals Q. Choose a nonzero direction with `Qδx≠0` to contradict it.
An exact admissible family makes the error especially transparent: in SU(2),
take a direction-constant commuting link field `x_μ=tA`,
`A=diag(i,−i)`, with other directions zero. Every μ-contour has
`M(t)=exp(LtA)` and its maximizer is exactly `W₀(t)=M(t)`. Thus
`W₀(t)⁻¹M(t)=I` for all sufficiently small t, whereas `Qδx=L A≠0`.
This is not a numerical or asymptotic disagreement.

The coefficient used in the SG proof is instead

    A_b(x) = W₀(x)⁻¹ ∂M(x)/∂x_b − Q_cb.                 (LA-1′)

There is **no derivative of W₀** in this expression. It vanishes at zero
and admits the intended O(s_l) estimate. The author's file has not been
edited; `(LA-1′)` is an explicit correction in this review.

### 4.3 Independent local analytic completion, with unspecified finite constants

**CONFIRMED with (LA-1′), after shrinking the fixed local neighbourhood and
enlarging constants.** Sources: `KFACTOR_OFF55.md`, `Local analytic inputs`
and `All orders`; `BFT_A.md`, `3.4 BA-4`, `3.5 BA-5`, `[RBA1-fix] F6`;
`PROOF.md`, NA-alg's equation `Π(e^{-X}M) = 0`.
The following is a review-side proof, not an assertion that the target
already wrote the derivative estimates correctly.

For fixed N,L, a soft term depends on a fixed finite collection of link
variables in its contour words. At `(X,M)=(0,I)`, the derivative in X of
`Π(e^{-X}M)` is minus the identity on su(N). The finite-dimensional analytic
implicit-function theorem therefore gives W₀ analytic on a fixed local
neighbourhood. On the real domain it is the NA-alg maximizer by uniqueness.
Choose a smaller closed polydisc within that neighbourhood. Suprema of the
finitely many derivatives needed below are finite there. Their dimensions,
polydisc, word lengths, and incidence counts depend on N,L, not k,T.
Complexification gives the same assertion on a smaller complex polydisc.

In particular the coefficient maps in SG are analytic,
`A_b(0)=0`, `Z−δx_{l+1}=0` at zero, and `G−I` has no linear term.
Taylor's formula gives their O(s), O(s), and O(s²) bounds, together with
the corresponding first-derivative bounds. Per-link frequency factors
can be kept by differentiating each averaged word before summing; alternatively
their bounded local incidence can be absorbed into a constant depending on L.
This proves the qualitative estimate intended by (LA-1′).

Here is the scale calculation, including derivatives, that mere invocation
of analyticity would otherwise leave unstated. Set `q=k−l=m+1`,
`h=L^(−q)`, and take `||B||_D≤η`. For fixed B let
`δ=||x−x′||_(σ)` with the homogeneous-data difference norm. All local
variables, including the level-l+1 variable, are O_L(hη); their differences
are O_L(hδ). The quadratic part of `ρ−r` obeys the BA-4/F6 bound. The
commutator with `x_{l+1}` is bounded by `|x_{l+1}||r_l|` and its polarized
analogue. Taylor's integral remainder for the cubic-and-higher part has
size O_L(h³η³) and difference O_L(h³η²δ). Thus, for finite constants C,

    |ρ_l−r_l| ≤ C h³η²,
    |(ρ_l−r_l)(x)−(ρ_l−r_l)(x′)| ≤ C h³ηδ,
    |ρ_l| ≤ L^{−(2+σ)m}η + C h³η²,
    |ρ_l(x)−ρ_l(x′)| ≤ L^{−(2+σ)m}δ + C h³ηδ.          (1)

Constants here include a fixed upper bound on η. These are finite Taylor
bounds, not estimates obtained by taking a depth-dependent radius.
For example, the commutator term costs
`L^{−m}η·L^{−(2+σ)m}η ≤ L³h³η²` for σ≥0.

SG, (LA-1′), and the derivative product rule now give, at both output levels,

    π_l(κ_l E_l|_l) + π_{l+1}(κ_l E_l|_{l+1})
      ≤ C [L^{−σm}η² + L^{−q}η³]
      ≤ C′ L^{−σm}η²,                              (2)

and the difference bound `C′ L^{−σm}ηδ`. The last inequality uses
`0≤σ≤1`. The level-k output at the terminal step is omitted because it is
data, not an unknown. Derivatives of Θ are controlled using (1), rather
than incorrectly claiming a differentiated Θ still has a factor Θ.

For the residual source, `Ψ−r=(ρ−r)+(Ψ−ρ)` and `Ψ−ρ=O(ρ³)` give

    L^{(2+σ)m}|κ_l(Ψ_l−r_l)| ≤ Cη²,
    L^{(2+σ)m}|Δ[κ_l(Ψ_l−r_l)]| ≤ Cηδ.              (3)

The least-decaying Taylor error in (3) has factor
`L^{(2+σ)m}h³ = L^{−3}L^{(σ−1)m}≤L^{−3}`.
This is why σ≤1 is sufficient; the residual slot takes a maximum, so no
sum of these endpoint constants is introduced.

For Wilson, write `F_p=dx_0+q_p(x)` with `q_p=O(x²)` and
`∇w(F)=c_wF+O(F³)`. Then exactly

    ∇S_W = d*[∇w(F)] + (Dq_x)ᵀ∇w(F).

In coarse units, `n²q` has size and pointwise Hölder seminorm O(η²):
translate all its finitely many arguments together, use `Dq=O(x)`,
`x=O(η/n)`, and
`|x(b+v)−x(b)|≤dη|v/n|∞/n`.
BL-C gives `n²F` a pointwise C^α bound O(η). The plain Wilson row is a
bounded-overlap sum of products of `nDq=O(η)` and `n²∇w(F)=O(η)`;
both factors have the corresponding pointwise Hölder bounds. The product
inequality and one further local derivative give

    ||G_0^c||∞+[G_0^c]_α ≤ Cη²,
    π_0(j_W)+[(j_W)^c]^∞_α ≤ Cη²,

with difference bounds Cηδ. This supplies precisely the Hölder control
needed for HR(iv) at all orders, not merely its sup analogue.

Equations (1)–(3) and the Wilson estimates prove existence of all required
local constants from the stated finite-word analytic structure and the
banked quadratic cancellation. No numerical values for these new constants
are claimed. In particular they do **not** certify the target's literal
all-order replacements `A_B → A_E+A_E′`: the gradient is κ_l E_l, and the
bound also contains `1+C_ρη`. One safe choice must include
`κ_+(A_E+A_E′)(1+C_ρη_*)` and enlarged Wilson/residual constants, or simply
use the finite constants C above. These changes preserve k,T uniformity.

## 5. The weights, linear input, and corrected contraction theorem

### 5.1 The invariant linear half is a valid conditional implication

**CONFIRMED as an implication of the named lane-A linear inputs.** Source:
`KFACTOR_OFF55.md`, locating `Lemma TOP♯` and `Proposition LIN`;
inputs: `BFT_A.md`, `Corollary FP`, `Lemma TS`, `Corollary LIN0`,
`Theorem CO-upR`; `BFT_B.md`, `29.1 Lemma RT-cc`, `29.2 Lemma FT`;
`CODEX_REVIEW_C2.md`, `(C2-COF)`.

For TOP♯, split S into its G,s part and its plain part. Both parts are cc
in the root-pinned sense; neither need satisfy `(CC-0)`. TS identifies the
unknown components of the top probe with the datum response to
`δ_b/κ_{k−1}`. The datum norm is sup, so its weighted norm, centred at b,
is exactly `1/κ_{k−1}`. FP bounds the tent representative's potentials.
There are `d L^{4(k−l)}` links per coarse cell at level l. The potential
factor `L^{−(k−l)}` leaves `d L^{3(k−l)}`, which cancels the normalization
of π_l(j_l). The remaining exponential sum is bounded by the displayed
`S_4(m_w)`, independently of T. This proves the stated top-residual bound;
there is no plaquette observable's extra n² in this top-link pairing.
The G,s response is separately covered by LIN0. The proof does not consume
the top bound it is establishing.

RT-cc and the straight-transpose column count yield, with `m=k−1−i`,

    L^{(1+σ)m}||r_i^c||∞
      ≤ κ_-⁻¹[||s||_{R(σ)}
          + L^{(σ−1)m}(κ_+||r_{k−1}||∞
                         + ||s_{k−1}||∞ + C_f J)],
    C_f=1+2d/(1−L⁻³).

At d=4,L=3, `C_f=121/13` exactly. Since σ≤1, TOP♯ closes this bound.
For the fine curvature, use (C2-COF), retaining its top-response term until
TOP♯ supplies it. For upper curvatures the relevant factor is

    L^{α(k−j)}L^{−σ(k−1−i)}
      ≤ L^{−σ(j−1−i)}       (i<j, α<σ).

Its sum is bounded by `1/(1−L^(−σ))`.
All these implications retain the analytic hypotheses of their named
linear package; they do not independently certify that entire package.

There is a minor parameter endpoint to state correctly. C2-COF/LIN0 are
quoted for `α<θ<1`, whereas the target allows `θ=σ=1`. At that endpoint
use any `θ₀` with `α<θ₀<1`, for example `(α+1)/2`, in those imported
estimates. The inclusion
`||s||_{R(θ₀)}≤L^{θ₀}||s||_{R(σ)}` supplies them. The transport/source
weight remains σ=1. This repairs the citation's endpoint without assuming
an unproved θ=1 version of C2-COF.

### 5.2 The level ratio is not the Banach Lipschitz constant

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `Exponent bookkeeping`;
`REVIEW_S22.md`, locating `Anti-circularity:`.

The residual source weight and transport give `θ_w^r=2+σ`. Potential
weight `θ_A=1` is supplied for the selected slice by GV; LR-pot supplies
only its potential part in the tent slice. Therefore

    3−θ_A−θ_w^r = −σ,
    4−θ_w^r−2θ_A = −σ,
    A=L^(−σ)<1     for every fixed σ>0.

At σ=1 this is `1/L`; it is `1/3` only when L=3. A is the **geometric
level ratio**. The actual Lipschitz constant of Φ̃ also contains the
linear-response constants, the source constants, and the data/ball size;
it is made at most `1/2` by smallness. It is not identically A.

The only Newton inverse applied is the composite `𝓛_Γ⁻¹`. Routing is an
explicit linear map, and `M_x` is shown injective by its norm estimate;
neither a per-level covariance nor a nonlinear FP inverse is substituted
into the iteration. The anti-circularity clause is respected.

### 5.3 What the contraction statement actually earns

**NOT-VERIFIED from the literal printed LA-1. CONFIRMED as a corrected
conditional theorem using §4.3's local estimates.** Source:
`KFACTOR_OFF55.md`, locating `Theorem K`, `The one OPEN input`, and
`The source map x ↦ S̃(x)`.

The first qualification is substantive: an implication that silently
assumes the false displayed LA-1 is not a nonvacuous construction. Here
is the corrected nonvacuous implication, with its remaining inputs visible.

Keep the stated trivial-background, m=0, `𝒞_glob`, T≥3 setting, fixed
`0<α<θ≤σ≤1` (with the auxiliary θ₀ just described when needed), the named
conditional invariant linear package, and one gauge Γ satisfying the
stated algebraic requirements and `(GV^(σ))_Γ`. Use the actual F and actual
projected map, with local estimates established by §4.3 rather than the
false derivative in LA-1. Then there exist positive constants, independent
of k,T, giving precisely a small invariant ball and a contraction there.

For explicit bookkeeping, let G bound the full cc response in `𝔐^(σ)`.
After enlarging a finite constant K, §3 and §4 give

    N^(σ)(corrected nonlinear source) ≤ K(η+s)²,
    N^(σ)(difference) ≤ K(η+η′+s)||x−x′||_(σ),
    s=||B||_D.

Choose `C₀=max(2,4G)` and `η=C₀s`. Take ε₀ smaller than each of

    η_* /(C₀+1),
    C₀/[4GK(C₀+1)²],
    1/[2GK(2C₀+1)],
    1/[2 C_cc C₀],       C_cc=2d(59/100)L^{d−1},

where η_* is the fixed local analytic radius. The image norm is at most
`Gs+GK(C₀+1)²s²≤C₀s/2`, its Lipschitz constant is at most `1/2`, and
CCP's injectivity is strict. Differences use the homogeneous-data norm;
at fixed B the ball with `r_{k−1}=Qx_{k−1}−B` is an affine convex closed
ball in a finite-dimensional complete space. This avoids treating its
data-dependent residual expression as a norm of x alone.

Banach and CCP now give the unique full critical point in that slice ball.
BA-3 and (1) give BFT-1's weights `(2,2+σ,1)`, with potential size measured
relative to the stated trivial/global centre and controlled by s. The
fixed local analytic extensions and the complexified fixed linear inverse
give the usual uniform analytic contraction and BFT-2 after reducing ε₀
by another fixed factor. The complexification changes constants, not the
depth or volume dependence.

Thus the contraction mechanism does reduce the remaining **new nonlocal
estimate** to GV, relative to the explicitly inherited linear package.
The local analytic completion above is mathematics, not a new physical
premise. No numerical value of its radius or higher Taylor constants is
claimed. The existence of a Γ satisfying GV is still **NOT-VERIFIED**;
neither tent potentials nor removal of one previously known obstruction
proves its gradient estimate. Nonlinear orbit coverage, other backgrounds,
nonzero exponential weights, and constructive Yang–Mills closure are not
consequences of this review.

## 6. Lemma OC and the negative claim on the Γ_E route

### 6.1 The exact splitting is correct

**CONFIRMED.** Source: `KFACTOR_OFF55.md`, locating `Lemma OC` and
`For the rescaled fixing cΓ`.

For `μ=D_*S`, set `S′=S+Γᵀμ`. Then `D_*S′=0` because ΓΞ=−I on the
pinned gauge space. If `x_cc=𝓛_Γ⁻¹S′`, then Γx_cc=0 and Hx_cc=S′.
Direct multiplication yields

    𝓛_Γ(x_cc+Ξμ)=S′−Γᵀμ=S.

For cΓ the same cc source S′ works and the pure gauge is `Ξμ/c²`.
The cc representative is unchanged because the slice is unchanged.
This is an exact statement about the chosen normalization and both parts
of the response, with only the off-root divergence entering.
Taking `Γ_hier=−P` likewise confirms §3.6's description: apply its Feynman
inverse and project the result to Ker Γ; the result is exactly Φ̃_Γ.

### 6.2 The displayed estimates fail to close; impossibility is not proved

**CONFIRMED only as a failure of the displayed sufficient estimate.** Source:
`KFACTOR_OFF55.md`, locating `On the lane's (Feynman, Γ_E) route`;
`BFT_B.md`, `36.4 Proposition GT-ell` and `25.1`'s adjoint bound.
The direct route pays for `n⁴||μ||∞` and `n³ max_X|Q_X(μ)|`.
An unstructured sup bound on a divergence loses one power of n even for
the Wilson current, which has no improved σ level weight. No bound for
those two quantities along actual iterates is supplied in this packet.

**NOT-VERIFIED as a no-go theorem.** Source: `KFACTOR_OFF55.md`, locating
`NOT boundable with present inputs`, table N5, and the same assertion in
§8–§9. A growing upper bound is not a lower bound on the actual response.
The finite axial-routing control is not Γ_E, nor a realized nonlinear
four-dimensional source in the contraction ball. There is no matched
counterexample, and no proof exhausting signed pairings, Ward cancellations,
or more economical representations of the same Γ_E response. The source's
own admission that attainment for generic rows is merely argued reinforces
this limitation. The accurate status is: **the supplied Γ_E estimates do
not establish the required uniform bound**.

### 6.3 Two errors in the stated list of what that route needs

**NOT-VERIFIED as a sufficient alternative:** `KFACTOR_OFF55.md`, locating
`or (GT-sup) ⟸ (Y-sup^loc)` and `needs exactly the lane's named inputs`.
For the curvature remainder, the coarse normalization gives

    |remainder(p)| ≤ n² ||D_*S||₁
                         sup_{supp D_*S}|λ_*^{Γ_E}(p)|.

GT-sup controls only the second factor. It does not bound
`n²||D_*S||₁`, or an equivalent localized product. This omission is already
explicit in `REVIEW_BFT_B_S9_S10.md`, locating `S9-15 The missing n²` and
`requires a third input`. A full response bound also needs the corresponding
residual-probe estimates. Neither source factor nor the pure-gauge norm
is supplied merely by GT-sup. The alternative cannot be advertised as
exactly one sufficient missing input.

**REFUTED as a description of the cited review:** `KFACTOR_OFF55.md`,
locating `whose reduction is NOT-VERIFIED, REVIEW_BFT_B_S9_S10 S10-14`.
That review explicitly **confirms** the implication
`(Y-sup^loc) ⇒ (GT-sup)` with constant 20. What it marks NOT-VERIFIED is
the headline that this makes the problem cease to be a spike/support
question, and the claimed availability of its sufficient antecedent.
The legitimate implication, an unproved antecedent, and the separate
missing charge factor must not be conflated.

### 6.4 Negative-claim discipline, scoped to this review

| Check | Result relevant to the proposed negative claim |
|---|---|
| N1: alternative routes | Examined the direct adjoint sup bound, the signed dual pairing, and the Ward/source structure. None exhausts all estimates for the prescribed Γ_E map. Hard-slice rescaling and hierarchical projection are useful changes of problem/map, not in-domain counterexamples to a Γ_E-specific theorem. No five-family exhaustive packet is claimed. |
| N2: independence | No independence of NEUT-box, charge-size estimates, and GT-sup is proved. They are sufficient-route obligations, not a certified count of necessary independent walls. |
| N3: hidden assumptions | The missing `n²||D_*S||₁` factor and the passage from a sufficient bound to a necessary condition are exposed above. |
| N4: residual matching | OC matches the actual remainder. A4′ matches an axial-routing proxy only; it does not match Γ_E or the nonlinear source map. |
| N5: resolution | HR is proved at arbitrary lattice depth. The control is d=2,T=1 at five depths; it does not certify a nonlinear d=4,T≥3 response lower bound. |
| N6: partial closure | The projected iteration avoids this response problem. It does not prove the unmodified Γ_E problem impossible, and no new physical axiom is implicated. |
| N7: strongest opposing route | Retain the signed kernel pairing with `D_*𝔑⁰=−(K′ᵀ∇F)_*`, exploit its local source structure, and bound the product instead of its separate absolute factors. A matching estimate is not supplied, but no cited argument rules it out. |
| N8: prior echo | `CODEX_REVIEW_C2.md`, locating `the exact error in the old refutation`, already rejects inferring response growth from one separated root-charge term whose companion can cancel. The present negative claim must not repeat that inference. |

This is a limitation of the negative proof, not evidence that Γ_E's
unmodified iteration does satisfy the desired bound.

## 7. ko55_1: exact reproduction and independent mechanism check

**CONFIRMED within its advertised finite/model scope.** Sources:
`checks/ko55_1_criteria.md`, `AMENDMENT 1`; `checks/ko55_1.py`,
`CASES`, `Part A4'`, `Part B`, and `Part C`;
`KFACTOR_OFF55.md`, `What ko55_1 does` (the scope paragraph in §7).

The script was inspected completely before execution. It writes no files.
I executed its unchanged verdict computations under `python3 -I -B`,
replacing only calls used for floating-point **display** in memory by an
exact rational formatter. Thus no floating-point arithmetic was executed.
The wrapper asserted every entry of RESULTS; every entry was true:
A1, A1-ctl, A2, A3, A4′, B, C. The author script prints an overall failure
but does not itself exit nonzero on a failed boolean; an exit code alone
would not be a reliable certificate.

An independent implementation routed charges by one-dimensional prefix
sums, eliminating axes in reverse order and passing remaining charges to
the next level. It did not enumerate root-to-destination paths or call
the author's lattice helpers. Divergence was formed by signed incidence
at edge endpoints. It verified the identity on fresh integer data in all
eight cases, with zero mismatches:

| d | k | T | Number of sites |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 9 |
| 2 | 2 | 1 | 81 |
| 2 | 2 | 2 | 324 |
| 2 | 3 | 1 | 729 |
| 2 | 3 | 2 | 2916 |
| 2 | 4 | 1 | 6561 |
| 4 | 1 | 1 | 81 |
| 4 | 2 | 1 | 6561 |

All 81 delta-source basis vectors on the d=4,k=1,T=1 lattice were also
checked exactly. This is exhaustive for that finite linear identity, not
for nonlinear Yang–Mills configurations.

For the amended triangular-wave control the reproduced ratios are:

| k | n | ρ_hier | ρ_single |
|---:|---:|---:|---:|
| 1 | 3 | 1 | 1 |
| 2 | 9 | 5/3 | 3 |
| 3 | 27 | 17/9 | 12 |
| 4 | 81 | 53/27 | 39 |
| 5 | 243 | 161/81 | 120 |

There is also a direct all-depth explanation for this **d=2 proxy**.
Let `s=3^i`. A line sum over a size-s block is
`A_s(X)=tri(sX−1)−tri(sX+s−1)` and
`V_i(X,Y)=s[A_s(X)+A_s(Y)]`. Summing the transverse line for the first
axial direction gives maximum current `6s²` for i<k−1 and `3s²` at
i=k−1. The second direction is no larger. The independent prefix-sum
implementation reproduced exactly these maxima at all five depths.
Therefore

    ρ_hier = [Σ_{i<k−1} 3^{k−i}·6·3^{2i}
                   + 3·3^{2k−2}·3]/n²
            = 2−3/n = 2−3^{1−k}.

For routing directly to the final root, the first-direction current on
the central row is n times a one-dimensional cumulative divergence.
Its maximum is `n·max(1,(n−3)/2)`; the second-direction currents are no
larger. Hence `ρ_single=1` at k=1 and `(n−3)/2` for k≥2.
Thus the hierarchy tends to 2 and single-level routing is asymptotic to
n/2, with the same `Lip_c=n²` normalization. Neither formula describes
Γ_E's Neumann kernel.

The Bernoulli threshold was reproduced exactly and independently bounded
in §1. For the series check,
`Σ_{m≥0}(m+1)3^(−m)=9/4`, and the tested radical bound uses
`(329/250)^4=11716114081/3906250000<3` and
`250/79<633/200`, all exact.

Six additional in-memory mutations were detected by their intended checks:
the sign of the final root charge (A1), the multiplicity formula (A2),
the boundary-flux sign (A3), removal of the hierarchical coarse-weight
normalization (A4′), a Bernoulli threshold of 1/2 (B), and replacement of
the geometric ratio by 1/2 (C). Each produced an overall false result.
No runner, criteria, cached output, or other source file was changed.

## Exactly what may be banked

1. **CONFIRMED:** HR(i)–(v), including the exact root-supported telescoping
   remainder, the sup and Hölder routes, and their stated k,T-independent
   constants. Source: `KFACTOR_OFF55.md`, `Lemma HR`; independent derivation
   and exact checks are in §§2 and 7 of this report.
2. **CONFIRMED:** CCP(a)–(d), for full critical points lying in the slice,
   with strict smallness as above and only root-pinned CD plus (GI). Every
   inverse source is cc; no nonlinear FP hypothesis or `(CC-0)` is used.
   Source: `KFACTOR_OFF55.md`, `Proposition CCP`.
3. **CONFIRMED:** the SG identity and its exact factor Θ, and the uniform
   full-source bounds after replacing the false LA-1 by LA-1′ and using
   the finite local analytic estimates proved in §4.3. Source:
   `KFACTOR_OFF55.md`, `Lemma SG`, `Local analytic inputs`, `Proposition ROW`.
   The printed LA-1 is **REFUTED**; its literal all-order numerical
   constants are not certified.
4. **CONFIRMED:** CB's k,T-uniform upper and Lipschitz bounds for each fixed
   `0<α<σ≤1`, with the corrected full-source constants. At σ=0 bank only
   the upper-budget identity `Σ_{m<k}(m+1)=k(k+1)/2`; actual k² growth is
   **NOT-VERIFIED**. Source: `KFACTOR_OFF55.md`, `Proposition CB`.
5. **CONFIRMED, conditionally:** TOP♯, LIN^(σ), and the corrected Theorem
   K^(σ) of §5.3: relative to the named lane-A linear inputs, one Γ
   satisfying GV suffices for a k,T-independent nonlinear contraction
   radius and smallness threshold, slice-selected critical-point uniqueness,
   and the stated BFT-1/2 conclusions on `𝒞_glob`. The local correction and
   analytic completion in this report must accompany that statement.
   `A=L^(−σ)` is the level ratio; the Banach constant is made ≤1/2.
   GV itself and nonlinear gauge-orbit coverage remain **NOT-VERIFIED**.
   Sources: `KFACTOR_OFF55.md`, `Theorem K`, `The one OPEN input`, `Scope`;
   `REVIEW_S22.md`, `Anti-circularity:`.
6. **CONFIRMED:** OC's algebraic split, its c⁻² normalization, and the
   hierarchical-gauge interpretation. Bank only failure of the supplied
   Γ_E estimates to close, with the missing charge factor retained; the
   assertion of impossibility at every σ is **NOT-VERIFIED**. Source:
   `KFACTOR_OFF55.md`, `Lemma OC`, `NOT boundable with present inputs`;
   `REVIEW_BFT_B_S9_S10.md`, `S9-15 The missing n²`.
7. **CONFIRMED:** ko55_1's finite exact identities, active controls, and
   d=2 axial-routing mechanism with the ratios above. They supply no test
   of GV, no nonlinear Γ_E obstruction, and no constructive 4D Yang–Mills
   closure. Sources: `checks/ko55_1.py`, `CASES`, `Part A4'`;
   `KFACTOR_OFF55.md`, `What ko55_1 does` (the scope paragraph in §7).
