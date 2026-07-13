# Raw constrained-action response and exponentially local Hessian

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/wilson_staggered_raw_constrained_action_hessian_decay_2026_07_12.py`](../scripts/wilson_staggered_raw_constrained_action_hessian_decay_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/wilson_staggered_raw_constrained_action_hessian_decay_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_raw_constrained_action_hessian_decay_2026_07_12.txt)

## 0. Result

The exact factor-two raw action map now has controlled first and second local
responses in the deep hard-fiber wedge.

Use the constrained hidden Gibbs systems of the direct dependency,
[hard-fiber control and raw action-map directions](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md).
For a finite regulator `Lambda`, fixed coarse configuration `V`, and bounded
real local hidden-gauge perturbations `F,G`, let `Phi` be the real
fermion-integrated gauge-body interaction `S_W-log det D` in the constrained
coordinate chart, whose Boltzmann weight is strictly positive, and define

```text
R_Lambda(Phi)(V)=-log integral dH exp[-Phi(H;V)].                     (0.1)
```

Then ordinary differentiation under the compact integral gives the exact
bilinear response identities

```text
D R_Lambda(Phi)[F]=<F>,
D^2 R_Lambda(Phi)[F,G]=-Cov(F,G).                                    (0.2)
```

Let `C` be the hidden Dobrushin influence matrix. In the deep wedge there is
`lambda>0` such that

```text
q_lambda=sup_h sum_k exp(lambda d(h,k)) C_(h,k)<1.                   (0.3)
```

In short, `q_lambda<1` is the weighted margin used below.

With `D=(I-C)^(-1)`, the Dobrushin covariance estimate and the weighted
geometric series imply

```text
|D^2 R_Lambda(Phi)[F,G]|
 <= (1/4)sum_(h,k) delta_h(F) D_(h,k) delta_k(G),                    (0.4)

sup_h sum_k exp(lambda d(h,k))D_(h,k)<=1/(1-q_lambda).               (0.5)
```

If the hidden-coordinate supports `A,B` of `F,G` are separated by `L`, then

```text
|D^2 R_Lambda(Phi)[F,G]|
 <= exp(-lambda L)/[4(1-q_lambda)]
    ||delta F||_1 ||delta G||_1.                                    (0.6)
```

All constants are uniform in `Lambda` and in the complete coarse
configuration `V`. Thus the raw map has a volume-uniform exponentially local
Hessian on local bosonic coefficient directions throughout
`alpha(beta,m)<1/2`.

This does not establish third or higher derivative bounds, a uniform complex
source neighborhood, a connected joint polymer logarithm, or contraction of
a projected and rescaled RG map. Equation (0.1) is a finite-volume relative action;
no infinite extensive raw action is silently normalized.

It is also an unnormalized raw fiber action, not `-log p_Delta(V|omega)` for a
normalized coarse conditional kernel. Differentiating the latter would also
differentiate its normalization over interior coarse `V` and add subtraction
terms to (0.2). Retained-Grassmann directions and a simultaneous all-degree
coefficient norm are excluded from the present positive-measure theorem.

No axiom-update stop is established.

## 1. Exact response identities

For real parameters `t,s`, compactness and boundedness make

```text
Z(t,s;V)=integral dH exp[-Phi(H;V)-tF(H)-sG(H)]                       (1.1)
```

strictly positive and smooth. Differentiating `R=-log Z` gives

```text
partial_t R=<F>_(t,s),
partial_s partial_t R=-[<FG>_(t,s)-<F>_(t,s)<G>_(t,s)].              (1.2)
```

At the origin this is (0.2). The signs are fixed by the minus sign in both
`R=-log Z` and the source insertion in (1.1). A coarse-local lifted direction
has zero hidden oscillations and passes with the unit first derivative found
previously; the present theorem is consistent with that exact raw direction.
More explicitly, for `Lf=f(V)`,

```text
D R_Lambda(Phi)[Lf]=f(V),             D^2 R_Lambda(Phi)[Lf,G]=0.     (1.3)
```

The same identities extend by dominated convergence to perturbations with
summable hidden-coordinate oscillations. The explicit separation statement
below is made first for finite support.

## 2. Weighted covariance control

For a bounded function `F`, write

```text
delta_h(F)=sup{|F(H)-F(H')|: H,H' differ only at h}.                  (2.1)
```

The continuous-spin Dobrushin covariance inequality, with full single-site
oscillations (2.1) and the half-`L1` total-variation convention, is

```text
|Cov(F,G)|<=(1/4)sum_(h,k) delta_h(F)D_(h,k)delta_k(G),
D=sum_(n>=0)C^n.                                                     (2.2)
```

The factor `1/4` matches this oscillation/variation convention. The direct
dependency supplies a uniform weighted row below one. Triangle inequality
for the hidden graph distance makes weighted matrix row norms
submultiplicative, so

```text
||C^n||_lambda<=q_lambda^n,
||D||_lambda<=sum_(n>=0)q_lambda^n=1/(1-q_lambda).                   (2.3)
```

For `h in A,k in B`, `d(h,k)>=L`; (2.3) gives the pointwise bound
`D_(h,k)<=exp(-lambda L)/(1-q_lambda)`. Substitution in (2.2) proves (0.6).
This is a response bound
for the exact constrained model, not an inference from coarse image
correlation decay.

The external mathematical result used in (2.2) is H. Follmer, *A covariance
estimate for Gibbs measures*, Journal of Functional Analysis **46** (1982),
387--395, DOI `10.1016/0022-1236(82)90053-2`. It is not a new physical premise.

## 3. Infinite-volume meaning and exact boundary

The first derivative of an extensive raw action contains its expected volume
term, so this note does not declare an infinite scalar `R(Phi)(V)`. Instead,
(0.2)--(0.6) apply uniformly to finite-volume relative responses. For fixed
local `F,G`, constrained-fiber uniqueness makes their expectations and
covariances converge as the regulator grows. The limiting local derivatives
obey the same estimates and are independent of hidden boundary conditions.

The Hessian result is the correct second-order input for a future action-space
map, but it is not source analyticity. An all-order theorem still needs a
common complex neighborhood and bounds of factorial/tree form for
`D^n R[F_1,...,F_n]`, together with the lattice-animal and Grassmann-degree
accounting required by the generated-action norm.

Even all-order locality would not by itself select relevant coordinates,
field rescaling, counterterms, or a physical critical trajectory.

## 4. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_raw_constrained_action_hessian_decay_2026_07_12.py
```

The runner checks a deep-wedge point, the exact first- and mixed-second-
derivative signs in a finite positive model, the weighted resolvent geometric
sum, a positive exponential separation rate, and the source/dependency
boundary. Infinite-volume Dobrushin comparison is analytic mathematics.

## 5. No-Go Discipline N1--N8

No negative theorem is shipped. The higher-response and contraction sentences
are scope disclaimers, not impossibility claims. All eight checks are retained
conservatively; N1 records the proof routes actually attempted for the
positive Hessian theorem.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live |
|---|---|---|---|
| Direct compact-integral differentiation | `ATTEMPTED` | Section 1 proves both response identities. | It fixes the algebraic signs without a mixing theorem. |
| Finite-difference response check | `ATTEMPTED` | The runner tests first and mixed-second derivatives in a positive model. | It independently catches sign mistakes. |
| Follmer covariance estimate | `ATTEMPTED` | Section 2 matches its oscillation and half-`L1` conventions. | It converts fiber control into a Hessian bound. |
| Bernoulli saturation stress test | `ATTEMPTED` | The runner saturates the `1/4` factor for one unbiased spin. | It pins the convention rather than relying on rhetoric. |
| Weighted influence resolvent | `ATTEMPTED` | Equation (2.3) sums the geometric series. | It supplies the exponential kernel. |
| Separated-support extraction | `ATTEMPTED` | Equation (0.6) follows from the pointwise weighted-resolvent bound. | It is the claimed locality statement. |
| Infinite-fiber local-response passage | `ATTEMPTED` | Section 3 uses uniform comparison for fixed local directions. | It avoids declaring an infinite extensive action. |
| Fiber-constant compatibility | `ATTEMPTED` | Equation (1.3) recovers the exact unit direction and zero mixed Hessian. | It cross-checks the prior raw identity. |

### N2 — wall-independence audit

The open conditions are `all-order source/polymer bound`, `declared
projected/rescaled irrelevant-map contraction`, and `physical critical
trajectory`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| all-order source/polymer bound | declared projected/rescaled irrelevant-map contraction | No | No | Yes |
| all-order source/polymer bound | physical critical trajectory | No | No | Yes |
| declared projected/rescaled irrelevant-map contraction | physical critical trajectory | No | No | Yes |

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Hidden boundary conditions are variables, not premises. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | No unqualified use. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Hard-fiber control and raw directions](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Uniform weighted hidden comparison; only exact raw unit directions | General local first/second response and Hessian locality | Yes | Sole direct dependency. |
| Follmer 1982 covariance estimate | Covariance controlled by the Dobrushin influence resolvent | Verify the weighted resolvent and apply it to raw derivatives | Yes | External mathematical theorem. |
| Complete analyticity | Complex/all-order source control | `n>=3` derivatives | No | Context only. |
| Banach contraction theorem | Consequences after a self-map and `q<1` exist | Constructing that projected map | No | Context only. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Every finite regulator and fixed `V` in the deep wedge | Yes | Exact first/second response identities. |
| Separated bounded local perturbations | Yes | Uniform exponential Hessian bound. |
| Infinite-volume local response | Yes | Boundary-independent limit of local derivatives. |
| Third and higher derivatives | No | No cumulant/tree claim. |
| Complex source neighborhood | No | No analyticity claim. |
| Connected joint polymer action | No | Remains open. |
| Projected/rescaled RG map | No | No contraction or eigenvalue claim. |
| Critical continuum trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The source parameters are mathematical perturbations of the previously
declared regulator action. They are not new physical couplings, axioms,
probability rules, or time laws. Differentiation and Dobrushin covariance add
no framework primitive. The result therefore advances the supplied map
without changing the premise registry.

### N7 — hostile steelman

A hostile reviewer can object that exponential covariance decay is much
weaker than a convergent polymer RG. Correct: this block proves only the exact
Hessian rung and states the all-order source theorem separately. Follmer's
1982 covariance estimate is intrinsically second order; the stronger
complete-analyticity conditions and their all-order equivalents are treated
by Dobrushin and Shlosman, *Journal of Statistical Physics* **46** (1987),
983--1014, and their hypotheses are not claimed here.

A second reviewer can object that relevant and marginal directions should not
contract. Correct: the theorem does not test contraction at all. It provides
local derivative data needed before a relevant/irrelevant projection is
declared.

### N8 — cross-cycle echo

| Earlier cycle | Earlier residual | Was that wall retired? | Does its mechanism apply here? | Present treatment |
|---|---|---:|---:|---|
| Hard-fiber Dobrushin control | Uniform comparison existed without action derivatives | Yes, for comparison only | Yes | The same influence resolvent now controls the raw Hessian. |
| Raw unit directions | One exact first derivative passed unchanged | Yes, for that direction | Yes | Equation (1.3) embeds it in the general response formula. |
| Coarse-gauge Gibbsianness | A summable representative existed without a uniform RG norm | No | No | No uniform representative norm is inferred here. |
| Factor-two block map | Exact integration existed without multiscale stability | No | Partly | Only local second-order stability is added; multiscale closure remains open. |

No wall is retired by relabeling and no axiom update is requested.
