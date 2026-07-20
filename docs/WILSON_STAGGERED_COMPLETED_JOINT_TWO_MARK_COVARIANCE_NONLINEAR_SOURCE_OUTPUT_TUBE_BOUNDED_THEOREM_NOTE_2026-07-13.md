# Completed-joint two-mark covariance and nonlinear source/output tube

**Date:** 2026-07-13
**Type:** open_gate
**Status:** open two-root proof obligation; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_completed_joint_two_mark_nonlinear_tube_2026_07_13.py`](../scripts/wilson_staggered_completed_joint_two_mark_nonlinear_tube_2026_07_13.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_completed_joint_two_mark_nonlinear_tube_2026_07_13.txt`](../logs/runner-cache/wilson_staggered_completed_joint_two_mark_nonlinear_tube_2026_07_13.txt)

## 0. Result and scope

The completed one-horizon Block46 graph supplies the exact Hessian identity,
the vanishing raw Hessian blocks, and a numerical diagnostic for a possible
two-mark covariance bound. It does **not** yet prove that bound: the required
constant-one two-root cluster injection has not paid the meeting-anchor, cut,
support, and routing multiplicities. Consequently the nonlinear residual
source/output tube below is conditional on the explicit open obligation in
Section 2. At the same finite-regulator
Wilson--staggered `SU(3)`, `beta=0`, `m=10^64` witness, every perturbation in
the restricted raw-quadratic/centered source class (1.2a) with strong split
norm at most

```text
delta=0.001                                                     (0.1)
```

fits in the joint expansion. If the unproved pair majorant (2.4) holds with
constant one, the resulting arithmetic is

```text
M_delta=88.82169800480513,
B+q delta+(M_delta/2)delta^2
 =0.0009853829050985733<delta,                                  (0.2)
```

with margin `1.461709490142675 10^(-5)`.  The entire output tube preserves a
quadratic gap, pays the worst three-pair `eta` migration and one fresh
site-block atomization, and lands at

```text
theta_atom(delta)=0.426574016916734>0.400001,
expm1(delta)=0.001000500166708342<0.01.                          (0.3)
```

This is an open proof gate with a reproducible conditional arithmetic
certificate, not a nonlinear one-horizon theorem. Even conditional on the
missing inequality, it is not a same-domain invariant ball: the centered
source uses the full `(Theta+2c,Lambda)=(4.4,0.2)` graph weights, while the
fresh output lands in the weaker `(theta,lambda)=(0.400001,0.1)` atom chart.
It supplies neither an all-horizon running-center recursion nor a critical
continuum, taste, dynamics, time, unitarity, or probability theorem.

The four direct repository inputs are the exact response/split identities
from the
[split-derivative boundary](WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the strong split and one-mark rerooting architecture from the
[K-retaining marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the two-layer joint majorant `H` from the
[joint product-reference theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the actual completed graph, output, gap, and atom-return ledger from the
[scalar-product joint atom-return theorem](WILSON_STAGGERED_SCALAR_PRODUCT_REFERENCE_COMPLETED_JOINT_OUTER_HAAR_ACTUAL_OUTPUT_ATOM_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md).

All action, chart, regulator, mass, background, norm, and reference choices
remain the explicit imports of Block46.  No value in (0.1)--(0.3) is claimed
to follow from the four framework axioms alone.

## 1. Map, reference split, and exact Hessian

Fix the completed Block46 scalar-product joint graph, its color-zero normalized
correlated reference `E_ref`, its scalar Gaussian center, and its chart.  They
remain frozen while differentiating.  Let `L` lift retained coarse
interactions as hidden-fiber constants.  Since `E_ref L=I`, define

```text
C_ref=L E_ref,                 Q_ref=1-C_ref.                     (1.1)
```

The strong source norm is the direct-sum norm

```text
||F||_strong
 =||P_quad C_ref F||_center
  +||(1-P_0)C_ref F||_(fine lift; theta_w=2.19,lambda_w=0.1)
  +||Q_ref F||_(joint mark; Theta+2c=4.4,Lambda=0.2).             (1.2)
```

Throughout, `||.||_center` means the coefficient norm induced by the weak
retained chart `(theta_w,lambda_w)=(2.19,0.1)` after the Hermitian onsite
quadratic projection.  Thus the center arm, its radius-`delta` shift, and the
`exp(-2.19)` coefficient-to-Weyl conversion in Section 4 use one declared
normalization.

Here `P_0` is the full diameter-zero projector of the declared RG chart and
`P_quad=P_(0,2)^sa` is the Block46 Hermitian onsite quadratic projector after
the scalar vacuum is removed.  The declared tube source class obeys

```text
(P_0-P_quad)C_ref F=0.                                            (1.2a)
```

Thus raw diameter-zero perturbations are restricted to the owned quadratic
center.  Arbitrary onsite nonquadratic raw inputs are not silently assigned a
contractive factor.  Centered inputs may still generate onsite higher or
anti-Hermitian residual output, and those terms remain in the residual
response bound.  The definition charges the actual centered component
directly; it does not pretend that `1-C_ref` is contractive in an ambient
unsplit norm.

For the finite-regulator relative action map

```text
R(Phi)=-log E_ref exp(-Phi),                                      (1.3)
```

ordinary commutative Banach-algebra differentiation gives

```text
DR_Phi[F]=E_Phi[F],
D^2R_Phi[F,G]=-Cov_Phi(F,G).                                     (1.4)
```

The contracted transformation in this open-gate diagnostic is the quadratic-center-
complement residual map on the restricted class (1.2a):

```text
T_res=(1-P_quad)D_(2,1)R.                                        (1.4a)
```

For the raw arm, (1.2a) leaves only `P_quad C_refF`, which is removed into the
center ledger, and `(1-P_0)C_refF`, which receives the exact diameter gain
`exp(-0.1)`.  The centered arm receives the marked response bound and may land
in any residual coordinate, including diameter zero.  Hence the inherited
`q=max(q_raw,q_centered)` is valid for `T_res` on this restricted class.  The
complementary Hermitian onsite quadratic is owned by a separate running-center
ledger.

There is no factor two in the mixed coefficient: differentiating first in
`s` and then in `t` gives the coefficient of `st` once.  Along one diagonal
direction Taylor's theorem supplies the separate factor `1/2` multiplying
`D^2R[H,H]`.

Fiber-constant lifts have zero covariance under every normalized hidden
functional:

```text
Cov_Phi(Lf,Lg)=0,                 Cov_Phi(Lf,Q_ref G)=0.           (1.5)
```

Therefore the raw/raw and raw/centered Hessian blocks vanish exactly, at the
actual base and throughout the perturbation ball.  Only the
centered/centered block requires a cluster bound.  Product centering does not
make that block vanish: already two zero-mean marks can have a nonzero direct
pair `E_ref(F^oG^o)`.

## 2. Open two-root majorant obligation

Let the base graph have total rooted activity `K`, hard-core allowance `c`,
and

```text
D(K)=sup_(n integer>=1)n exp[-(c-K)n],
tau=K D(K)<1.                                                     (2.1)
```

The prior two-layer marked proof uses

```text
H(t)=t(2-t)/(1-t)^2=sum_(n>=1)(n+1)t^n.                          (2.2)
```

For a single reference-centered mark, the mark-alone term is zero and `H`
bounds all base-attached outputs.  For two centered marks, the connected
covariance has an additional `n=0` direct-pair term.  On either ordered marked
side, distributing `n` path steps between the factor-to-polymer and hard-core
layers has `n+1` nonnegative allocations.  Off-path subtrees are already paid
by the same rooted row and the two `c` reserves used in `H`.  Therefore one
complete, possibly uncentered, rooted side is bounded by

```text
P_side(tau)<=1+H(tau)
            =sum_(n>=0)(n+1)tau^n
            =(1-tau)^(-2).                                      (2.3)
```

For the ordered bilinear pair `(F,G)`, one would need to split the connected objects into a
direct overlap, two marks in one first-layer polymer, and marks in distinct
hard-core polymers.  Root the first side at `F` and the second at `G`.  In the
same-polymer case, cut the unique factor-tree path at its first meeting edge;
in the distinct-polymer case, also cut the unique hard-core path at its first
meeting polymer. Retaining that labeled meeting anchor and cut is a proposed
map, not a proved constant-one injection. The present construction does not
show that the meeting-anchor/cut sum, common-path assignment,
same-polymer/distinct-polymer split, and mark-support convolution are already
paid by the two scalar side series. Therefore the following inequality is the
exact open obligation, not a conclusion:

```text
P_2(tau)<=P_side(tau)^2<=(1-tau)^(-4).                           (2.4)
```

The mixed derivative receives no external factor two. If (2.4) and its
once-only output routing are proved, then for unit strong directions,

```text
||D^2T_Phi[F,G]||_weak
 <=M(K)||F||_strong||G||_strong,

M(K)=68exp(Lambda/2)/(1-KD(K))^4.                                (2.5)
```

Equation (2.5) is conditional on (2.4). Here `T_res` includes the contractive quadratic-center-complement projection.
Hermitian quadratic projection and symmetrization belong to the separate
center ledger.
The constant-three product estimate for the full direct-sum algebra is not
inserted into (2.5): the raw Hessian blocks vanish before multiplication, and
the centered/centered bilinear mark convolution uses the declared projective
mark norm with constant one.

## 3. Conditional radius-0.001 arithmetic

Let `Phi_46` be the actual completed base.  Block46 gives

```text
K_T=4.808231265303741 10^(-7),
c=0.01,
B=3.613463806021123 10^(-5),
q=0.9048374180359595.                                            (3.1)
```

If `||H||_strong<=delta`, write the fixed-reference split

```text
H=Lf+H^o,                    E_ref H^o=0.                          (3.1a)
```

Even commutativity gives `exp(-H)=exp(-Lf)exp(-H^o)`.  The fiber-constant
factor `exp(-Lf)` cancels exactly between the numerator and denominator of
every normalized hidden response, so it does not enter the joint activity
row.  Carrierwise exponentiation of the centered arm gives
`K(H^o)<=expm1(||H^o||)<=expm1(delta)`.  Uniformly along the segment from zero
to `H`, use

```text
K_delta=K_T+expm1(delta)
       =0.001000980989834872,

c-K_delta=0.008999019010165128,
D_delta=sup_(n integer>=1)n exp[-(c-K_delta)n]
       =40.87992417946649             (attained at n=111),

tau_delta=K_delta D_delta
         =0.04092002696953689<1.                                  (3.2)
```

At `Lambda=0.2`, equations (2.5) and (3.2) give

```text
M_delta=68exp(0.1)/(1-tau_delta)^4
       =88.82169800480513.                                       (3.3)
```

Conditional on (2.4), this would be a uniform Hessian bound on the whole
radius-`delta` strong ball, not the smaller base-only value `75.154...`.
The independently established source analyticity margin is

```text
r_src=log(1+c-K_T)=0.009949854790553249>delta.                    (3.4)
```

Thus every base on the segment stays in the same zero-free joint logarithm
branch; it obeys (2.5) only if the open two-root obligation is discharged.

## 4. Conditional nonlinear-tube diagnostic

If (2.4) supplies the uniform Hessian estimate (3.3), Taylor's theorem gives

```text
||T_res(Phi_46+H)||_weak
 <=B+q||H||_strong+(M_delta/2)||H||_strong^2.
```

At the boundary `||H||_strong=delta=0.001`,

```text
B+q delta+(M_delta/2)delta^2
 =0.0009853829050985733
 <0.001=delta.                                                    (4.1)
```

Convexity of the scalar majorant gives the same conditional arithmetic
throughout the ball. This does not prove a residual source/output
Banach-bundle tube. Here `B`
is a safe upper bound for the actual base residual output; it is not a
same-space displacement from a fixed point.

The residual weak output potential is at most `delta`.  The complementary raw
onsite response can shift the running center by at most `delta`.  To avoid any
overlap or disjoint-budget assumption, charge the complete center/output ledger
by the raw radius, the full residual-tube envelope, and one additional base
output row for the separately projected center,

```text
B_complete(delta)<=delta+0.0009853829050985733
                         +0.00003613463806021123
                 =0.002021517543158784.                           (4.2)
```

After the scalar vacuum is removed, project the Hermitian onsite quadratic
once and leave the disjoint complement residual.  Coefficient-to-operator
incidence one gives

```text
epsilon_Q(delta)
 <=B_star+exp(-2.19)B_complete(delta)+10^(-20)
 =0.0002262440843396182,

gap_delta/m>=0.9997737559156604.                                  (4.3)
```

The worst three-pair Grassmann-weight migration and fresh site-block atom cost
are

```text
sigma_eta(delta)=3log[1/gap_delta]
                =0.0006788090441796472,

theta_atom(delta)=2.19-log C_*-sigma_eta(delta)
                 =0.4265740169167342>0.400001.                   (4.4)
```

Finally `expm1(delta)=0.001000500166708342<0.01`, so every output in the tube
belongs to the displayed fresh target factor chart.  The target chart is
weaker than the source chart; (4.1)--(4.4) do not authorize literal next-step
reuse as the same source ball.

## 5. Runner contract

Run

```bash
python3 scripts/wilson_staggered_completed_joint_two_mark_nonlinear_tube_2026_07_13.py
```

The runner independently checks: exact vanishing of fiber-constant Hessian
blocks in a nontrivially tilted finite model; a nonzero centered/centered
covariance; the mixed derivative sign and absence of an extra factor two; the
two-layer `n+1` one-side series and the conditional
`[1+H]^2=(1-tau)^(-4)` scalar pair series; all uniform
ball, conditional Hessian/Taylor, gap, `eta`, atom, and factor rows; an independent
80-digit Decimal reconstruction of the activity, optimizer, Hessian, and tube;
the source contract;
and exactly four dependencies. It does not check the general rooted-side
injection. That constant-one inequality is the open proof gate in Section 2.

## 6. No-Go Discipline N1--N8

This open-gate note contains a named same-domain/all-horizon boundary, so the full
stress test is recorded even though no new physical impossibility is claimed.

**NG47:** this finite one-horizon cross-norm two-mark residual tube does not by
itself furnish an invariant RG ball, because it supplies neither a same-space
endomorphism nor certified reuse on a second horizon. `NG47` is only a
logical non-implication from the displayed conditional diagnostic, not a
physical RG no-go.

### N1 — alternative-route enumeration

| route | status | outcome |
|---|---|---|
| Identify the target atom chart directly with the next source chart | `ATTEMPTED` | Fails: `(0.400001,0.1)` is not `(4.4,0.2)`. |
| Infer invariance from the scalar inequality (4.1) | `ATTEMPTED` | Rejected: the domain and codomain norms/charts differ. |
| Invoke Banach's theorem from `q<1` | `ATTEMPTED` | Rejected: `q` is a strong-to-weak residual operator bound, not an endomorphism norm. |
| Iterate `M_delta,q` unchanged | `ATTEMPTED` | Rejected: Block46's literal next ledger fails and no second-horizon source membership is proved. |
| Reuse the frozen reference at a running center | `ATTEMPTED` | Rejected: center/reference derivatives and determinant ownership would need a new transport theorem. |
| Promote the restricted class (1.2a) to a generic ambient ball | `ATTEMPTED` | Rejected: arbitrary raw onsite nonquadratic inputs are deliberately outside the source domain. |

Live constructive continuations are scale-indexed source charts, retained
atom lineage, a block-saturated next-source section, a varying-m schedule,
multi-horizon bundle composition, and alternate taste-faithful blocks.

### N2 — wall-independence audit

Keep six residuals atomic:

| wall | unresolved target |
|---|---|
| `W1` | A same-domain nonlinear return/invariant-ball package for one declared transition, including return embedding and center/base update but not identifying later horizons. |
| `W2` | A horizon-uniform scale-indexed or lineage-preserving recursion. |
| `W3` | Extension from the restricted class (1.2a) to the required generic ambient interactions. |
| `W4` | Select a physical taste/chart rather than declare this sector. |
| `W5` | A controlled critical/continuum limit with Lorentz, unitary QM/QFT, SM, and GR recovery. |
| `W6` | A physical dynamics/admissibility law including time and probability. |

| pair | close first => second? | close second => first? | independent reason |
|---|---:|---:|---|
| `W1-W2` | No | No | One declared same-domain transition does not identify the physical graphs, centers, or lineage at later horizons; an all-horizon induction may instead use changing bundle charts. |
| `W1-W3` | No | No | A self-map on the restricted class does not embed generic interactions; generic membership alone gives no self-map. |
| `W1-W4` | No | No | An invariant mathematical ball is taste-blind; taste selection gives no self-map. |
| `W1-W5` | No | No | A massive ball need not survive criticality; a continuum route may use changing domains. |
| `W1-W6` | No | No | A self-map supplies no law/time/probability semantics; those semantics give no cluster estimate. |
| `W2-W3` | No | No | All-horizon control on the actual class does not embed generic sources; generic control supplies no scale recursion. |
| `W2-W4` | No | No | Scale induction does not select taste; a selector supplies no induction. |
| `W2-W5` | No | No | Massive all-horizon estimates are not critical convergence; a critical construction may use another recursion. |
| `W2-W6` | No | No | A Euclidean recursion supplies no physical law/time/probability rule. |
| `W3-W4` | No | No | Generic analytic control is sector-blind; taste selection does not bound arbitrary sources. |
| `W3-W5` | No | No | A generic massive ball need not have a critical limit; continuum control need not be generic in this norm. |
| `W3-W6` | No | No | Ambient interaction control and physical law selection are separate. |
| `W4-W5` | No | No | Taste selection does not prove continuum recovery; a continuum limit may retain multiple tastes. |
| `W4-W6` | No | No | A sector selector is not a dynamics/time/probability law. |
| `W5-W6` | No | No | Recovering continuum sectors does not select the fundamental law or probability rule; the converse supplies no limit. |

### N3 — hidden-condition phrase scan

The pre-N3 note and pre-scan runner prefix were scanned literally:

| phrase | hit count | classification |
|---|---:|---|
| `we assume` | 0 | absent |
| `by construction` | 0 | absent |
| `as is standard` | 0 | absent |
| `the framework provides` | 0 | absent |
| `bridge context` | 0 | absent |
| `background` | 1 | declared finite-sector import only |
| `naturally` | 0 | absent |
| `obviously` | 0 | absent |
| `standard QFT` | 0 | absent |
| `registered` | 0 | absent before this self-referential table |
| `canonical` | 0 | absent before this self-referential table |

`Uniform`
means uniform on the radius-`0.001` strong ball, not uniform across all scales.
`Nonlinear tube` means (4.1) between two different norm bundles.  `Hessian`
means the finite-regulator Banach derivative (1.4).  `All-horizon`,
`invariant`, `continuum`, `unitarity`, and `probability` occur only as explicit
nonclaims or residuals.

### N4 — residual matching

| exact authority | residual supplied | present use | match? |
|---|---|---|---:|
| Split-derivative note, lines 23--72 and 142--194 | exact derivative/covariance and nonideal centered split | (1.1)--(1.5), direct pair | Yes |
| K-retaining note, lines 9--121 and 264--318 | strong split, one-mark `q`, conditional Taylor diagnostic | source norm, linear row, tube architecture | Yes |
| Joint product-reference note, lines 314--358 | common two-layer graph and `H(t)` majorant | conservative pair series (2.2)--(2.5) | Yes |
| Block46 note, Sections 3--6 | actual completed graph, base rows, output gap and atom return | all numerical and ownership inputs | Yes |
| Framework dynamics-selection no-go | physical law underdetermination | not used | Residual mismatch; dropped |

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One finite two-coordinate covariance fixture | Yes | Sign, raw-block vanishing, direct pair, no factor two. |
| One completed finite-regulator graph | Partial | Base identities and conditional radius-`0.001` arithmetic; the pair bound is open. |
| Whole restricted strong ball at one horizon | Partial | Worst activity, conditional Hessian, gap, and atom rows are recomputed. |
| Same-domain next-scale ball | No | `W1` remains. |
| All horizons / running center | No | `W1-W2` remain. |
| Taste / continuum / Lorentzian theory | No | `W4-W6` remain. |

### N6 — partial closure and primitive scan

The two-mark attempt does not retire the old two-mark wall: it retains the
small activity and rooted marked paths but leaves the constant-one cut/support
sum open. It therefore does not yet upgrade Block46's single output into a
nonzero nonlinear tube. The target/source chart mismatch
and running-center/all-horizon tasks still have multiple live mechanisms from
N1.  The Lattice, Qubit, Admissibility, and Record axioms and the approved
primitive registry neither provide nor obstruct those analytic mechanisms.

No axiom-update stop is triggered.

### N7 — hostile steelman

The strongest objection is that a source/output tube is not yet an RG
invariant ball.  The objection is correct: Block46's target atom chart has
smaller spatial and diameter exponents than this note's centered source
chart, and no identity embeds it back.  A scale-indexed Banach bundle or
lineage-preserving section could nevertheless turn the conditional tube, if
proved, into one step of an all-horizon induction. That live route defeats any broader no-go
but does not discharge the prior two-root proof obligation.

### N8 — cross-cycle echo

| prior wall/path | earlier status | mechanism applied here | disposition |
|---|---|---|---|
| Raw Hessian | Local bosonic pair covariance only | Completed joint Banach graph and strong split | Retired for the displayed actual all-degree graph. |
| Unlocalized Cauchy certificate | Absolute bound above 68 | Actual `K_delta`, direct pair, proposed two-side rooted envelope | Not retired; constant-one injection remains open. |
| K-retaining one-mark theorem | Strong-to-weak linear contraction only | Conditional two-mark arithmetic plus Taylor | Not upgraded without the open inequality. |
| Block43 unchanged-ledger wall | Same fixed chart could not iterate | Target/source mismatch remains explicit | Not retired; scale-indexed/lineage escapes stay live. |
| Block46 unchanged next reuse | Response and factor certificates both missed | The conditional diagnostic perturbs the first completed horizon, not the failed next ledger | Preserved; no contradictory iteration claim. |

**No-Go Discipline status:** `PASS` for the named bundle-versus-same-domain
boundary.

## 7. Claim-strength disposition

`OPEN GATE` is the intended review disposition. The proved content is the
finite-regulator Hessian identity, vanishing raw blocks, source analyticity,
and conditional arithmetic. A restricted-class radius-`0.001` nonlinear
residual tube remains conditional on the constant-one two-root cluster
majorant. Even if that obligation is closed, it is not an
autonomous RG ball, physical fixed point, all-horizon construction, continuum
limit, or derivation of dynamics, time, unitarity, or probability.

No axiom-update stop is triggered.
