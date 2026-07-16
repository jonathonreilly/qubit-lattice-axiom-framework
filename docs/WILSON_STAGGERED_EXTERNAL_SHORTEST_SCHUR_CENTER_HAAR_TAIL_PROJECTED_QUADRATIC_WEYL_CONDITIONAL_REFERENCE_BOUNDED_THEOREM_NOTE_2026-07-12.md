# External shortest Schur center, Haar-tail localization, projected-quadratic Weyl reserve, and conditional reference

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_external_shortest_center_tail_quadratic_weyl_reference_2026_07_12.py`](../scripts/wilson_staggered_external_shortest_center_tail_quadratic_weyl_reference_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_external_shortest_center_tail_quadratic_weyl_reference_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_external_shortest_center_tail_quadratic_weyl_reference_2026_07_12.txt)

## 0. Result

The generated full Schur kernel now has an exact shortest-subcenter/path-tail
split.  A further actual-hidden expectation/complement split keeps every
hidden-empty tail path external and every centered tail path residual-owned.
The separately carried local jet gives an actual external base-center update.
A larger Block44-sized onsite update is treated only as a conditional Weyl
budget, because Block44 did not include the correlated-center mixed clusters.
At every fixed external gauge background, the resulting conditional center
has an exact normalized Gaussian-reference ratio and a complete determinant
ownership identity.

The construction uses the exact center and ownership identities from the
[extracted shortest-center theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the enhanced local-jet row from the
[generated-base factor-return theorem](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the actual-hidden ordinary output from the
[site-block marked-response theorem](WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the projective coefficient norm from the
[simultaneous gauge--Grassmann norm theorem](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the normalized fixed-background reference grammar from the
[correlated Berezin locality theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Write

```text
mu=m+2/m,                  k=1/(4m),
A_2=mu I+R_(2,II),         ||R_(2,II)||<=rho:=8k=2/m,
h=rho/mu=2/(m^2+2)<1.                                      (0.1)
```

The current partition is bipartite.  Since the retained sites have one
parity and `R_(2,II)` changes parity,

```text
R_(2,KI) R_(2,II)^(2j+1) R_(2,IK)=0,            j>=0.       (0.2)
```

Consequently

```text
A_2^(-1)=mu^(-1)sum_(n>=0)(-R_(2,II)/mu)^n,

S_next=S_next^(2)-E_(>=4),
S_next^(2)=mu I-mu^(-1)R_(2,KI)R_(2,IK)
          =mu' I-k'A(W),

mu'=mu-8k^2/mu,            k'=k^2/mu,

E_(>=4)=mu^(-1)sum_(j>=1)
 R_(2,KI)(R_(2,II)/mu)^(2j)R_(2,IK).                         (0.3)
```

The shortest term depends only on external coarse `W`.  Terms in `E_(>=4)`
contain at least two internal hops, but they are not all hidden-nonempty:
immediate internal backtracks can reduce to the identity, and longer words can
reduce to external `W` words.  Therefore `S_next^(2)` is an external shortest
subcenter, not the complete external part of the full Schur family.

The exact operator estimates are

```text
||R_(2,KI)||^2<=16k^2=1/m^2,

||E_(>=4)||
 <=[1/(m^2 mu)] h^2/(1-h^2)
 =4/[m^3(m^2+2)(m^2+4)],

S_next>= (mu-1/m^3)I,
gap(S_next^(2))>=mu-1/(m^2 mu)>m.                              (0.4)
```

For internal graph distance `d_I`, the pointwise path bound is

```text
||(A_2^(-1))_(uv)||
 <=mu^(-1) h^(d_I(u,v))/(1-h^2).                               (0.5)
```

At path weight `(theta,lambda)` put `b=h exp(theta+lambda)`.  If
`b<1`, the complete path tail has the explicit anchored coefficient row

```text
B_tail
 <=6sqrt(3) eta^2 [rho^2/mu] exp(3theta+2lambda)
   b^2/(1-b^2),                  eta^2=1/m.                     (0.6)
```

Here `6sqrt(3)` safely pays both bilinear orientations and the entrywise
`l1` norm of a three-color unitary path.  At `m=10^46` and
`(theta,lambda)=(0.200001,0.2)`,

```text
log10 ||E_(>=4)||_op^bd = -321.397940008672...,
log10 B_tail^bd         = -364.997435900702....                 (0.7)
```

Let `E_hid` average only the actual current hidden Haar coordinates at fixed
external `W`, and put

```text
E_(>=4)^empty=E_hid E_(>=4),
E_(>=4)^o=(1-E_hid)E_(>=4),

E_(>=4)=E_(>=4)^empty+E_(>=4)^o.                               (0.8)
```

Haar expectation is contractive, so the empty part obeys the same rows as
(0.4) and (0.6); the centered complement obeys twice those rows.  Every
already external backtrack lies in `E_(>=4)^empty`.  It is factored and
reattached as a separate external residual; `E_(>=4)^o` is exponentiated as a
current red residual.  Neither tail piece is absorbed into the fresh shortest
Gaussian center below.  This closes the full-Schur ownership split without
falsely classifying the entire tail as hidden-nonempty or falsely treating its
hidden-empty off-diagonal paths as nearest-neighbor center bonds.  Both pieces
retain the nonminimal formal path carrier used in (0.6), even if Haar
evaluation reduces their visible link dependence; no spatial weight is erased
by the split.

## 1. Local quadratic projector and conditional Weyl reserve

Let `Pi_(0,2)` extract the onsite balanced bilinear from the already separated
finite local jet and define

```text
P_(0,2)^sa Phi=(1/2)[Pi_(0,2)Phi+(Pi_(0,2)Phi)^dagger],
delta Q_P0^sa=P_(0,2)^sa P_0.                                  (1.1)
```

Only the Hermitian, gauge-covariant onsite bilinear is moved into the
quadratic center.  The anti-Hermitian part and all higher local terms stay in
the residual.  This is a declared chart projection, not a physical selector.

The coefficient norm is the projective `l1` norm

```text
||bar psi Q psi||_eta=eta^2 sum_(a,b)|Q_ab|.                    (1.2)
```

Pair-degree projection and Hermitian symmetrization are contractive in this
norm.  Hence the coefficient-to-operator incidence is exactly one:

```text
||Q^sa||_op<=sum_(a,b)|Q^sa_ab|
            <=eta^(-2)||bar psi Q psi||_eta.                    (1.3)
```

No extra color factor `3` or `9` is needed.  The size weight of an onsite
term converts an anchored row `B` at exponent `theta` into at most
`exp(-theta)B`.  For the actual carried local jet,

```text
theta_o=9.213736870195430,
epsilon_P0
 <=exp(-theta_o)B_star
 =6.150432380261932 10^(-10).                                  (1.4)
```

The actual external base center after the tail split is

```text
S_base=S_next^(2)+delta Q_P0^sa.                                (1.5)
```

Weyl's inequality and (0.4) give

```text
gap(S_base)
 >=mu-1/(m^2 mu)-m epsilon_P0
 >=0.9999999993849568 m>0               at m=10^46.              (1.6)
```

The separately owned external factor `-E_(>=4)^empty` changes the full
quadratic kernel by at most (0.4), but it is not part of `S_base` or the
reference ledger in Section 2.

Block44 supplies only a fixed-product residual response.  It explicitly does
not include the correlated center/reference, determinant restore, boundary
factor, or their mixed clusters with the actual residual.  Therefore its
ordinary row is not identified here with the physical completed output
quadratic coefficient.  Instead define a conditional Hermitian onsite test
row `delta Q_trial^sa` satisfying

```text
eta^2 sum_(a,b)|(delta Q_trial^sa)_ab|
 <=epsilon_44:=exp(-theta_w)B_weak^(44)
               =0.07036819595670502,
theta_w=0.0000005.                                               (1.7)
```

For the conditional family

```text
S_trial=S_base+delta Q_trial^sa,
epsilon_Q=epsilon_P0+epsilon_44=0.07036819657174825,

gap(S_trial)>=0.929631803428252 m>0.                             (1.8)
```

This is a Weyl-budget theorem for any completed joint expansion whose
projected Hermitian onsite row satisfies (1.7).  The Block44 scalar row shows
that this budget is numerically plausible; it does not prove that the missing
mixed clusters satisfy it.  The gaps in (1.6)--(1.8) are finite-regulator
quadratic-kernel gaps, not physical pole masses, Osterwalder--Schrader
spectral gaps, or continuum mass theorems.

If the full residual coefficient chart were changed from `eta=m^(-1/2)` to
`eta_trial=gap(S_trial)^(-1/2)`, the worst balanced three-pair charge would be

```text
sigma_eta=3log[m/gap(S_trial)]=0.218900044560628....             (1.9)
```

This is below the earlier enhanced decorated reserve `0.400001` but above the
already landed weak size exponent `theta_w=0.0000005`.  Therefore (1.7) does
not manufacture an identity embedding of the full Block44 weak output into a
new strong domain.  The center-only conditional reference below may use
`eta_trial`; a newly paid joint expansion and atomization are still required
for the full residual.

## 2. Fresh conditional correlated-reference ledger

Fix the external gauge background, any member `S_trial` of (1.8), and a next
partition `K_2 union I_2`.
Let

```text
C_trial=S_trial,
A_3=(C_trial)_(I_2I_2),
M_3=direct-sum_x (A_3)_(xx),
R_3=A_3-M_3.                                                     (2.1)
```

Every principal onsite block of `M_3` is at least the trial gap in (1.8), and
`R_3` contains only the nearest-neighbor `k'` hopping of the external shortest
center.  At a fixed external gauge background define the normalized onsite
product Gaussian `G_(M_3)` and

```text
B_3=exp[-bar chi R_3 chi],
Z_3=G_(M_3)[B_3]=det(A_3)/det(M_3)>0,
G_(A_3)[F]=G_(M_3)[F B_3]/Z_3.                                  (2.2)
```

This is a normalized Berezin reference, not a probability rule.  Since

```text
h_3:=8k'/gap(S_trial)<1,                                        (2.3)
```

the determinant logarithm converges absolutely.  Bipartite parity again
removes odd loop words.  Localize every even loop, including the generally
non-vacuum length-two row, into `psi_gamma^(3)` and put

```text
C_3=product_gamma exp[-psi_gamma^(3)],
D_3(z)=product_gamma exp[z psi_gamma^(3)],
C_3D_3(1)=1.                                                    (2.4)
```

For a new `K_2-I_2` shortest-center boundary edge define `j_e^(3)` and

```text
J_3(z)=product_e exp[-z j_e^(3)].                               (2.5)
```

The product-block determinant is a separate external coefficient:

```text
V_3(W):=det M_3(W)>0,
V_3 G_(M_3)[B_3J_3]
 =det(A_3) exp[bar psi R_(3,KI)A_3^(-1)R_(3,IK)psi].             (2.6)
```

Thus `C_3,D_3` own only the normalized determinant ratio `Z_3`; they do not
erase or duplicate `V_3`.  If `M_3` depends on external `W`, the Haar
provenance/atomization of `V_3(W)` remains an explicit next-step factor.

The old `C_2,D_2,J_2` ledger is consumed before (2.1).  It generated the
current Schur output once and is never relabeled as `C_3,D_3,J_3`.  The new
ledger belongs only to the fresh partition.  At physical color one,
`C_3D_3(1)=1` is used before the `G_(M_3)` evaluation; the full determinant
identity is then (2.6), with `V_3` present exactly once.

With `C_*=3+2sqrt(2)`, the conservative three-coordinate boundary row at
`(theta,lambda)=(0.200001,0.2)` is

```text
K_B3^bd
 <=8 exp(2theta+lambda)
   [exp(18 C_*^3 eta_trial^2 k')-1]
 =3.50 10^(-181)<0.1,                                          (2.7)
```

and the even determinant series has

```text
log10 K_D3^bd<-366.18.                                          (2.8)
```

Thus the normalized center-only conditional ratio, restore, and boundary rows
close with enormous room, while (2.6) owns the missing product-block
determinant explicitly.  If the onsite projected coefficient depends on
external `W`, (2.1)--(2.8) are uniform at each fixed external `W`; they do not
yet supply the Haar-provenance atoms of either `W -> G_(A_3(W))` or `V_3(W)`.
That outer atomization and the ordinary residual factor must be paid afresh
rather than inferred from center positivity.

## 3. Exact claim boundary and next leverage

This theorem proves four things:

1. the full conditional Schur family splits into an external shortest
   subcenter, a separately reattached hidden-empty tail, and a centered
   residual tail with explicit convergent path rows;
2. the actual carried `P_0` quadratic projection preserves the base gap, and
   any additional onsite Hermitian row satisfying the declared conditional
   budget preserves a strict Weyl reserve;
3. the old determinant/boundary ledger is consumed exactly once; and
4. the fresh fixed-external-background normalized Gaussian ratio exists with a
   tiny center-only activity, while `det M_3(W)` is separately owned.

It does not prove an autonomous iteration.  In particular it does not provide
the new Haar-provenance atomization of a `W`-dependent onsite block, return the
full ordinary Block44 output to the strong domain, control a generic source
ball, select the taste carrier, or take a critical continuum limit.  The next
highest-leverage theorem is the fresh outer-Haar/site-block atomization of
`G_(A_3(W))` together with a completed joint residual expansion, followed by
the same-domain two-mark Hessian and invariant ball.

No axiom-update stop is established.  The remaining work is reference
atomization, support ownership, nonlinear analysis, and later physical
selection/continuum control inside the supplied theory surface.

## 4. Runner contract, inputs, and falsifiers

Run:

```bash
python3 scripts/wilson_staggered_external_shortest_center_tail_quadratic_weyl_reference_2026_07_12.py
```

The runner independently constructs a scalar-color `4^4` periodic fixture at
`m=7`; checks `||R_KI||^2`, parity cancellation, the length-four tail, full
and shortest gaps, and pointwise resolvent locality; verifies the projective
coefficient/operator inequality on a complex `3x3` fixture; freshly evaluates
the Block42 and Block44 rows at `m=10^46`; checks the Weyl reserve and chart
boundary; evaluates the subnormal tail and determinant rows with 100-digit
decimal arithmetic; checks an explicit hidden-empty/centered tail fixture; and
checks an exact positive two-site correlated Gaussian ratio together with the
missing product-block determinant identity.

The bounded witness inherits the Wilson--staggered SU(3), four-dimensional
factor-two, `beta=0`, finite-regulator setup of its dependencies.  The mass
`m=10^46` and all displayed norm exponents are declared theorem-chart choices,
not observed values or physical parameter matches.  No Standard Model datum,
continuum observable, time rule, or probability rule is imported.

The theorem is falsified within its scope if any of the following occurs:

- an odd internal Neumann sandwich survives the declared bipartite partition;
- the finite or analytic length-four tail exceeds (0.4);
- Hermitian onsite projection violates the coefficient incidence in (1.3);
- the actual `P_0` row exhausts the base-center gap or the conditional trial
  row exhausts its declared Weyl budget;
- `Z_3<=0` for an allowed fixed external background; or
- the identity (2.6) fails, or the fresh relative row has `h_3>=1` or fails
  its determinant convergence.

## 5. Authoritative No-Go Discipline N1--N8

The only negative boundary shipped here is

```text
NG45: the same current-hidden-dependent full Schur family cannot be inserted
      simultaneously and directly as an external input factor in the same
      integration step; its shortest hidden-independent part may be external,
      while the remaining path family must be residual-owned once.          (5.1)
```

This is an ordering and ownership statement, not a no-go against constructing
a full next-center grammar.

### N1 — alternative-route enumeration

| route | marker | executed/evidence result relative to `NG45` |
|---|---|---|
| Reinsert the complete conditional `S_next` as a simultaneous blue input | `ATTEMPTED` | Rejected by the output-only phase ledger in the [extracted shortest-center theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 350--364: it duplicates the same Gaussian/Schur generation in the same step. |
| Factor the `W`-only shortest subcenter and split/localize the tail | `ATTEMPTED` | Executed in (0.2)--(0.8); the hidden-empty part is a separately reattached external residual and the centered part is current-residual-owned once. |
| Keep Haar fixed until after the correlated Gaussian step | `ATTEMPTED` | Executed as the fixed-background conditional ratio in (2.1)--(2.8), consistent with the [fixed-background correlated theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 300--448.  It does not make the same conditional family external during the current joint step. |
| Integrate Haar first and project the quadratic part of the resulting cumulant | `ATTEMPTED` | Scope-tested against the [site-block response boundary](WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 169--183 and 304--312.  It remains a live way to create a *new* external coefficient, so Section 1 demotes the Block44-sized row to a conditional budget; it does not license identity reuse. |
| Retain current hidden Haar data in an enlarged coarse state | `ATTEMPTED` | Scope-tested against the direct-sum state declaration in the [generated-base factor return](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 157--164 and 270--289.  It is live only after changing the declared RG state, so it cannot defeat the same-state simultaneous-reuse boundary. |
| Use the shortest subcenter and actual `P_0` projector while keeping both tail arms outside the center | `ATTEMPTED` | Executed positively in (0.8)--(1.6); the larger Block44-sized update remains conditional in (1.7)--(1.9). |

### N2 — wall-independence audit

After the positive results, the atomic open-condition set is: `W1` fresh
outer-Haar/provenance atomization, `W2` strong factor return, `W3` a generic
two-mark Hessian, `W4` invariant-ball synthesis, `W5` taste selection, and
`W6` critical continuum control.

| pair | left closes right? | right closes left? | independent? |
|---|---:|---:|---:|
| `W1--W2` | No | No | Yes; atoms may still carry weak spatial weight, while a strong norm does not create provenance atoms. |
| `W1--W3` | No | No | Yes; one-horizon atoms do not give a two-mark derivative, and a Hessian does not construct atoms. |
| `W1--W4` | No | No | Yes; atomization does not prove self-mapping, and ball invariance does not define atom ownership. |
| `W1--W5` | No | No | Yes; a valid atom grammar can be taste-wrong, and taste selection does not retro-prove it. |
| `W1--W6` | No | No | Yes; finite-scale atomization is not a critical limit, and a continuum match does not supply provenance. |
| `W2--W3` | No | No | Yes; strong membership is a one-mark bound, not a Hessian; a Hessian need not restore lost weights. |
| `W2--W4` | No | No | Yes; same-domain membership does not imply self-mapping, and a ball theorem can use a different norm. |
| `W2--W5` | No | No | Yes; strong decay neither selects taste nor follows from taste selection. |
| `W2--W6` | No | No | Yes; one finite-scale return is not a critical trajectory, and a continuum construction does not retro-prove this return. |
| `W3--W4` | No | No | Yes; a Hessian estimate still needs radius/self-map arithmetic, while ball invariance can be certified by another nonlinear route. |
| `W3--W5` | No | No | Yes; nonlinear stability and taste selection are distinct operator questions. |
| `W3--W6` | No | No | Yes; a massive Hessian neither supplies critical tuning nor follows from a continuum identification. |
| `W4--W5` | No | No | Yes; an invariant massive ball can be taste-wrong, and a selected taste does not prove invariance. |
| `W4--W6` | No | No | Yes; a massive ball is not a controlled critical trajectory, and a limit does not retro-prove this ball. |
| `W5--W6` | No | No | Yes; taste selection does not prove convergence, and a continuum limit can retain multiple tastes. |

The hidden-Haar dependence, normalized-ratio provenance, and `det M_3(W)`
atomization are all parts of `W1`, not three inflated walls.  No pair above
collapses automatically, so the atomic set remains six.

### N3 — hidden-condition phrase scan

The source and runner were scanned for `we assume`, `by construction`,
`as is standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.
`Background` occurs only in the explicitly fixed-external-background theorem
scope.  `Canonical` occurs only in inherited atom terminology.  Neither is a
hidden premise.  All numerical and chart conditions are declared in Section 4.

### N4 — residual matching

| authority and exact witness | residual supplied | present use | match? |
|---|---|---|---:|
| [Extracted shortest-center theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 257--277 and 350--364 | `S_next` output-only ledger, exact shortest term, base gap | N1 direct-reuse rejection, starting split, old-ledger consumption | Yes |
| [Generated-base factor return](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 122--164 and 270--289 | Separate `P_0`, enhanced local row, ordinary output exponent | Actual local-jet bound, enlarged-state scope test, no duplicate intermediate row | Yes |
| [Site-block marked response](WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 137--183 and 268--312 | Actual-hidden fixed-product ordinary output and weak chart | Conditional `B_weak^(44)` Weyl-budget witness, not physical joint output | Yes, after conditional demotion |
| [Simultaneous gauge--Grassmann norm](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 92--116 | Projective coefficient `l1` norm | Incidence-one operator estimate | Yes |
| [Fixed-background correlated locality](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 224--342 | Exact normalized correlated Berezin ratio and outer-Haar boundary | Conditional `B_3/Z_3` grammar only; `det M_3` kept separate | Yes |

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One internal path | Yes | Odd internal length vanishes; even length is residual-owned. |
| One finite partition | Yes | Exact Schur split, gap, and determinant ratio. |
| One fixed external gauge background | Yes | Fresh conditional correlated reference and normalization. |
| Complete displayed actual-orbit quadratic row | Yes | Projected onsite Hermitian row preserves the center gap. |
| Outer Haar atom family | No | Remains `W1`; no impossibility claim. |
| Generic ball/all horizons | No | Remains `W3--W4`; no impossibility claim. |
| Physical continuum | No | Remains `W5--W6`; no impossibility claim. |

Thus `NG45` is restricted to simultaneous direct reuse in the same step.

### N6 — partial-closure and primitive-registry scan

The Lattice, Qubit, Admissibility, and Record baseline and the approved
registry primitives do not supply or obstruct the estimates above.  The
shortest-center split, Hermitian projector, Weyl estimate, and conditional
reference are chart mathematics.  Existing pathwise and post-Haar projection
routes already partially close the apparent ownership issue, so it is not
classified as a missing axiom or proposed primitive.

### N7 — steelman

The strongest attack is N1's post-step route: after the current integration is
completely finished, the generated full `S_next` may be declared the next
step's external input.  The strongest authority for that attack is the
[extracted shortest-center theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md), lines 350--364, which explicitly calls `S_next` output-only rather than forbidden forever.  The attack is correct and is why no broad no-go is claimed.  It does not defeat `NG45`: during the *same* integration, before current hidden variables have been removed, inserting the conditional output again duplicates its generating determinant/Schur paths.  N1's next-horizon route is therefore live outside, and consistent with, the narrow phase-order boundary.

### N8 — cross-cycle echo

| prior wall / path | retirement status and mechanism | applicability here | disposition |
|---|---|---|---|
| `docs/WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md:350-364` — generated Schur output cannot be simultaneous input | Partially retired here by shortest/tail and hidden-empty/centered splitting; next-horizon full reuse remains live | Same determinant/Schur phase-order residual | Mechanism applied in (0.8), not an axiom wall |
| `docs/WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:300-342,442-448` — fixed-background normalization does not commute through outer Haar | Not retired; narrowed to an exact conditional ratio plus explicit outer-Haar task | Same normalized-ratio residual | Preserved as atomic `W1` |
| `docs/WILSON_STAGGERED_COMBINED_HAAR_GAUSSIAN_REFERENCE_SPLIT_RESIDUAL_COLORED_INTERPOLATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:166-180,338-342` — combined split does not supply outer normalization/strong return | Partly retired in later cycles by actual-hidden ownership; strong return remains separate | Warns against promoting the Block44 row to physical joint output | Applied by conditional demotion in Section 1 |
| `docs/WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md:169-183,304-312` — fixed-product output lacks correlated-center grammar | Tree-span incidence retired there; correlated mixed clusters remain open | Exact source of the conditional-vs-physical distinction | Preserved as `W1`, not called an axiom gap |
| `.claude/science/physics-loops/record-faithful-dynamics-completion-20260711/NO_GO_LEDGER.md` — framework-level dynamics-selection nonuniqueness | Not retired; it concerns selection of physical dynamics, not this RG ownership identity | Residual does not match `NG45` | Dropped as a witness for this theorem |

The cross-cycle record shows that explicit split/phase-order mechanisms can
retire parts of this wall while leaving constructive routes open.  No similar
retirement mechanism has been ignored, and none requires an axiom update.

**No-Go Discipline status:** `PASS` for the narrow `NG45` ownership boundary.

## 6. Claim-strength disposition

`PASS WITH BOUNDED CLAIMS` is the intended review disposition.  The positive
content is a finite-regulator, ultra-massive, fixed-external-background
normalized-reference theorem with an actual `P_0` base gap and a conditional
Block44-sized Weyl budget.  It is not an
autonomous RG theorem, a dynamics/admissibility selection law, a time or
probability rule, a Standard Model identification, a gravity limit, or a
Lorentz/unitary continuum construction.

No axiom-update stop is triggered.
