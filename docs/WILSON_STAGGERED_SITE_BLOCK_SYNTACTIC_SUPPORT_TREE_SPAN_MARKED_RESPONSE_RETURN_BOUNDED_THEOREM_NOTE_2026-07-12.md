# Site-block syntactic-support tree span and fixed-product marked response with ordinary output

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_site_block_syntactic_support_tree_span_marked_response_return_2026_07_12.py`](../scripts/wilson_staggered_site_block_syntactic_support_tree_span_marked_response_return_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_site_block_syntactic_support_tree_span_marked_response_return_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_site_block_syntactic_support_tree_span_marked_response_return_2026_07_12.txt)

## 0. Result

The missing tree-span/source-incidence bridge from Block43 can be constructed
for the **actual Block42 residual factor system** after the next skeleton
change and regrouping of the actual hidden coordinates into independent
owner-site blocks. This does not identify routed-carrier diameter with hidden
tree span. Instead it declares a new nonminimal syntactic support, exactly as
permitted in the earlier
[two-layer source-polymer theorem](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Use the actual decorated factor row from
[Block42](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the anchored residual section from
[Block43](WILSON_STAGGERED_BLOCK_SATURATED_PRODUCT_REFERENCE_SPLIT_HANDOFF_SCALAR_NEXT_ACTIVITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the physical-hidden/future-external ownership from the
[two-horizon intertwining theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the localized path resolvent from the
[K-retaining marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md).

First make the next skeleton change

```text
V_1=B,                         V_2=B^(-1)W.                         (0.1)
```

The physically integrated hidden variables at fixed retained data are the
first skeleton links `B`, the nonskeleton Haar links, and the onsite Gaussian
variables on the next eliminated set `I_1`. The coarse links `W` and onsite
Grassmann variables on the retained set `K_1` remain external coefficient
variables.

Own a skeleton `B` at the intermediate site joining its two halves, own a
nonskeleton positive link at its positive start, and own an actual eliminated
onsite `G_m` coordinate at its site. Group all actual hidden coordinates with
the same owner into `H_x^hid`; a site with none receives a trivial one-point
block. Distinct blocks are independent. Let `E_x^hid` be their normalized
contractive product expectations and put

```text
E_hid=product_x E_x^hid,
C_hid=L E_hid,                     Q_hid=1-C_hid.                  (0.1a)
```

Marks are centered only when `F^o=Q_hid F`. In particular a function of
external `W` or retained `K_1` variables alone lies in the empty/raw arm; it
is not incorrectly killed by a formal future-coordinate projector.

Pull each actual residual factor through (0.1). If `f_X` has connected routed
carrier `X`, every actual hidden dependency still has an owner in `X`: the
intermediate owner of `B` is an endpoint of the first half and the start of
the second half, while nonskeleton starts and eliminated Gaussian sites were
already retained. Declare the nonminimal hidden-site-block support

```text
S_X=X.                                                               (0.2)
```

Dummy blocks are allowed: enlarging a syntactic support changes neither the
factor nor product integration. Connectedness gives

```text
|S_X|=|X|,                     ell(S_X)<=|X|-1.                     (0.3)
```

Here the factor system is the carrierwise factorization of the connected
residual interaction,

```text
exp[-sum_X Phi_X]=product_X(1+f_X),
f_X=exp(-Phi_X)-1.                                                  (0.3a)
```

Block42's constant-one exponentiation estimate is precisely the safe
anchored decorated row for these connected-carrier local factors; it is not a
single volume-spanning factor silently reassigned to one `X`.
Indeed, at a fixed anchor and weights `w_X>=1`, constant-one coefficient
submultiplicativity and positivity of the scalar majorant give

```text
sum_(X contains z) w_X||exp(-Phi_X)-1||_dec
 <=exp[sum_(X contains z)w_X||Phi_X||_dec]-1.                       (0.3b)
```

This is the carrierwise meaning of the inherited `K_dec^bd` row.

Choose the distinct attachment chart

```text
Theta=0.000001,                 c_att=0.1,
Lambda=0.2,
Theta+2c_att+Lambda=0.400001=theta_s.                              (0.4)
```

The ordinary coefficient norm of `f_X` is bounded by its complete Block42
primitive-atom sum. Therefore the actual strong factor norm of Block42/43
implies the site-block root row

```text
K_blk:=sup_h sum_(X:h in S_X)
 ||f_X|| exp[(Theta+2c_att)|S_X|+Lambda ell(S_X)]
 <=exp(-Lambda) K_dec^bd.                                          (0.5)
```

No second atom surcharge occurs in (0.5): skeleton substitution is
sup-norm contractive, `f_X` is the sum of its already paid primitive atoms,
and triangle inequality drops their `r_*^|S|>=1` weights. The mark norm is a
newly declared actual-hidden site-block norm after (0.1); no claim embeds
Block43's entire formal future-atom arm into `Q_hid`.

A factor-two support conversion remains available. Map a site block to its
factor-two cell and, for a second skeleton half `A^(-1)W`, add the other coarse
endpoint. A site has at most one such second half: its parity has exactly one
odd coordinate. Hence for a connected site-block polymer `Y`,

```text
X_2(Y) connected,
|X_2(Y)|<=2|Y|,
diam X_2(Y)<=ell(Y)+1.                                             (0.6)
```

At a fixed coarse anchor there are `2^4=16` owner sites in its cell and at
most four incoming second-half endpoints. Thus the exact multiplicity is at
most `20`; retaining the predecessor's conservative `68` is valid.

At `m=10^46`, a fresh Block42 evaluation gives

```text
K_dec^bd=0.001143660626665446,
K_blk^bd=exp(-0.2)K_dec^bd
        =0.0009363501261354373<c_att.                              (0.7)
```

For the same integer path resolvent as the marked theorem,

```text
D=3.713402581794853,
tau=0.003477044975855269,
a_0=0.003460817008042905,
A_att=0.006974243768515832.                                       (0.8)
```

The conservative support conversion then gives

```text
B_weak<=68exp(0.1)K_blk^bd=0.07036823114081178,
K_weak^bd=exp(B_weak)-1=0.07290318488718554<c_att,
q_centered<=68exp(0.1)A_att=0.5241257344203125,
q_raw=exp(-0.1)=0.9048374180359595,
q_sw<=max(q_raw,q_centered)=0.9048374180359595<1.                 (0.9)
```

Thus one actual-generated residual factor system has a strict actual-hidden
fixed-product marked response and an **ordinary retained-coefficient** factor
envelope from the site-block strong chart
`(Theta+2c_att,Lambda)=(0.200001,0.2)` to the weak coarse chart

```text
(theta_w,Lambda_w)=(Theta/2,Lambda/2)=(0.0000005,0.1).             (0.10)
```

This is a genuine positive response theorem for the displayed product
expectation on the actual hidden variables at fixed external `W,K_1`. It is
not Block43's previously conditional same-`K` substitution: (0.2)--(0.6)
supply the missing support and incidence map, and (0.5) changes the activity
to `K_blk`. The factor envelope in (0.9) is in the ordinary retained
`W,K_1` coefficient carrier norm. A new future re-Hoeffding charge and next
atom-factor return are not claimed.

The result is deliberately narrower than an actual next RG step. The weak
diameter exponent `0.1` is below Block43's stronger `0.5` empty arm. The
physical next center is correlated `S_next`, whereas `E_hid` uses the fixed
onsite product `G_m` only on `I_1`; the missing center/reference factors are
not hidden in the residual. The local jet `P_0`, quadratic center update,
determinant/boundary ownership, normalization, future atomization, and Weyl
reserve remain separate. No autonomous iteration, generic source ball, taste
selection, or continuum follows.

At the lower-depth point the **inherited aggregate certificate** does not
close; this is not a statement about the physical response. At `m=10^44`,

```text
K_blk^bd=0.09917144609957677<c_att,
tau=44.03230263790677>1,
exp[68exp(0.1)K_blk^bd]-1=1723.849489211310>c_att.                 (0.11)
```

These are upper majorants. Their failure says that aggregate factor membership
alone does not certify the marked response by this resolvent; it does not
prove that the actual `m=10^44` response fails. The ultra-deep activity
reduction is load-bearing for the positive certificate in (0.9).

## 1. Actual-hidden site blocks and no duplicate atom cost

The skeleton pair in (0.1) has one integrated Haar coordinate `B`, not two.
Owning it at the intermediate site places its owner in the routed carrier
whether the factor contains the first or second half. Every nonskeleton
positive link remains owned by its start. Only an endpoint in `I_1` supplies
an integrated onsite `G_m`; a `K_1` endpoint stays external. Thus

```text
H_x^hid={owned B and nonskeleton Haar coordinates}
        x {G_(m,x) if x in I_1},
product_x E_x^hid=E_hid.                                           (1.1)
```

The expectations commute, factorize, and are contractive in the certified
even-balanced coefficient norm. The centered-mark proof uses only these
facts, commutativity of the even algebra, and nonnegative norm majorants; it
does not require positivity of the Berezin functional.

The distinction from a full formal product expectation is load-bearing. For
`F=F(W)` independent of all actual hidden variables,

```text
E_hid F=F,                         Q_hid F=0.                       (1.1a)
```

A complement projection in the external `W` coordinate would instead call
such an `F` centered and would make the mark-alone term survive physical
hidden integration. That invalid hybrid is not used.

Let `Delta_A^prim f_X` be the already paid primitive atom decomposition.
Since it reconstructs `f_X`,

```text
||f_X||
 <=sum_A ||Delta_A^prim f_X||
 <=sum_A r_*^|A| ||Delta_A^prim f_X||.                             (1.2)
```

Equations (0.3)--(0.5) now follow carrier by carrier. This is a contraction
from the stronger existing bookkeeping to an ordinary base-factor row, not a
claim that regrouped atom norms dominate primitive atom norms in every
direction.

For an actual-hidden site-block mark, use `Delta_empty=E_x^hid` and
`Delta_nonempty=1-E_x^hid`.
The same one-coordinate projective proof gives coefficient-atom product
constant one at `r_*=1+sqrt(2)`. Empty fusions are retained. The base factor
is not re-Hoeffding-charged because the attachment theorem uses its ordinary
coefficient norm in (0.5).

## 2. Factor-two site-block support conversion

Write a site as `y=2z+epsilon`, with `epsilon in {0,1}^4`. The declared
straight factor-two skeleton has four first halves starting at `epsilon=0`.
A second half starts only when `epsilon` has exactly one nonzero coordinate,
and then its direction is uniquely that coordinate. Sites with two or more
odd coordinates own no skeleton half. Consequently one owner block adds at
most one other coarse endpoint.

Nearest-neighbor site-block adjacency maps to equal or nearest-neighbor
factor-two cells. Adding the endpoint of a second half attaches one adjacent
cell. More precisely, a base cell is `floor(y/2)`, while the added endpoint
for a parity-one second-half start is `ceil(y/2)`. Coordinatewise floor and
ceil are each `1`-Lipschitz in lattice `l1`: base--base and attached--attached
distances are at most `d(y,t)`, while a mixed floor/ceil pair costs at most
`d(y,t)+1`. Since `d(y,t)<=ell(Y)`, this proves the diameter part of (0.6)
without paying two endpoint edges.
For a pinned coarse `z`, roots arise from the sixteen owner sites in `2z+
{0,1}^4` or from one incoming second half in each of four directions. This
proves multiplicity `20<=68` without treating the four links inside one block
as four independent root rows.

Applying the K-retaining two-layer and marked-path majorants with this support
map yields

```text
B_weak<=68exp(Lambda/2)K_blk,
||(E_Phi^hid-E_hid)F^o||_weak
 <=68exp(Lambda/2)A_att(K_blk,c_att)||F^o||_mark.                  (2.1)
```

Here `F^o=Q_hid F`, and `E_Phi^hid` is the residual-tilted expectation over
the same actual hidden variables with external `W,K_1` held fixed. The raw
fiber-constant arm is the declared factor-two lift with diameter-zero part
removed, so it contributes `exp(-Lambda/2)`. Equations (0.8)--(0.9) therefore
prove the response and ordinary retained-coefficient factor bounds.

## 3. Exact scope boundary and next target

The output in (0.10) is weaker than the Block43 handoff in diameter weight:

```text
0.1<0.5.                                                           (3.1)
```

There is no bounded identity embedding from a generic `Lambda=0.1` carrier
row into `Lambda=0.5` on unbounded diameters. The positive theorem therefore
does not close a fixed strong/weak cycle. It does, however, remove the earlier
incidence ambiguity for one honest product-block chart and proves that the
marked response is quantitatively attainable once the activity is deep
enough. The ordinary output still needs a newly paid future re-Hoeffding step
before it can be called a next atom-factor row.

The next high-leverage construction is the full `S_next`-relative grammar:

1. localize `A_2^(-1)` paths in
   `S_next=mu I-R_(2,KI)A_2^(-1)R_(2,IK)`;
2. own `det A_2`, restore, and boundary factors once;
3. project the local quadratic part of `P_0` into the center;
4. spend a Weyl reserve to preserve the center gap;
5. repeat the site-block support proof in that correlated reference;
6. only then ask for a same-norm two-mark Hessian and invariant ball.

No axiom-update stop is established. Site-block regrouping, syntactic support,
and scale-indexed norm choice are constructive mathematics inside the current
axioms.

## 4. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_site_block_syntactic_support_tree_span_marked_response_return_2026_07_12.py
```

The runner checks actual-hidden versus external coordinate ownership, the
external-`W` centering counterfixture, contractivity after skeleton
substitution, primitive-to-block coefficient domination, block-atom
multiplication, connected support fixtures, the exact `20<=68` anchor count,
fresh Block42 rows at both masses, the tree-span root bound, exact integer
path-resolvent arithmetic, the strict response/ordinary-factor envelope, the
lower-mass separator, the diameter-codomain boundary, and the
source/dependency contract.

## 5. Authoritative No-Go Discipline N1--N8

The only negative boundary is

```text
NG44: the displayed actual-hidden product Lambda_w=0.1 response and ordinary
      output do not by identity supply a future-atom Lambda_w=0.5 or
      correlated-S_next next input.                                           (5.1)
```

It is not a no-go against lineage-sensitive, scale-indexed, correlated-center,
or taste-faithful closure.

### N1 — alternative-route enumeration

| route | marker | executed result |
|---|---|---|
| Identify Block42 diameter with the old hidden tree span | `ATTEMPTED` | Rejected in Block43; they are different norms. |
| Center with the full formal future-coordinate expectation | `ATTEMPTED` | Rejected: an external `F(W)` would be falsely centered although physical hidden integration leaves it unchanged. |
| Regroup only actual hidden coordinates into owner-site blocks | `ATTEMPTED` | Positive: (0.1)--(0.6) prove a physical-fiber syntactic-support bridge. |
| Retain the predecessor factor `68` | `ATTEMPTED` | Safe because the new anchor count is `20<=68`. |
| Use the aggregate `m=10^44` certificate | `ATTEMPTED` | Equation (0.11) has `tau>1`; this certificate fails without implying any physical-response verdict. |
| Move deeper in the same actual-bare family | `ATTEMPTED` | Positive at `m=10^46` in the weaker codomain. |
| Retain the smaller `K_T2` lineage into a stronger chart | `ATTEMPTED` | Numerically promising in Block43, but no lineage transfer theorem yet. |
| Build atoms relative to correlated `S_next` | `ATTEMPTED` | Not supplied by the fixed-product dictionary; queued constructively in Section 3. |
| Use scale-indexed diameter weights | `ATTEMPTED` | Not foreclosed; (3.1) makes this a natural live route. |

### N2 — wall-independence audit

Keep five walls: W1 correlated-`S_next` factor/reference grammar, W2 strong or
scale-indexed return after (0.10), W3 projected quadratic/positive-gap update,
W4 generic two-mark invariant ball, and W5 taste/critical continuum.

| pair | left=>right? | right=>left? | reason |
|---|---:|---:|---|
| W1--W2 | No | No | A reference grammar may have weak decay; a scale norm does not construct the reference. |
| W1--W3 | No | No | Factor ownership and quadratic gap preservation are separate estimates. |
| W1--W4 | No | No | One actual center does not control a generic ball; a Hessian does not define ownership. |
| W1--W5 | No | No | A correlated center can be taste-wrong; continuum matching does not retro-prove it. |
| W2--W3 | No | No | Spatial return does not preserve the center gap; a gap does not pay spatial weights. |
| W2--W4 | No | No | Actual-orbit return is not generic two-mark control. |
| W2--W5 | No | No | Massive return neither selects taste nor supplies critical tuning. |
| W3--W4 | No | No | Weyl stability at one center is not nonlinear ball invariance. |
| W3--W5 | No | No | A positive center need not have the physical taste carrier. |
| W4--W5 | No | No | A massive invariant ball is not a controlled critical continuum. |

### N3 — hidden-condition phrase scan

The note and runner are scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.
`canonical` appears only for the already defined atom/projector language;
`background` appears only in fixed-reference dependency titles or this scan.
No hidden admission is load-bearing.

### N4 — residual matching

| dependency | witness residual | present use | match? |
|---|---|---|---:|
| Two-layer source polymer | Nonminimal hidden syntactic supports and factor-two anchor conversion | Dummy owner-site support and support geometry | Yes |
| Block42 | Actual generated residual factor row and complete formal atom bound | `K_dec^bd`, carrierwise factors, and ordinary-norm domination after skeleton substitution | Yes, without integrating external atoms |
| Block43 | Anchored `M_s` split and explicit diameter/tree-span mismatch | Starting norm and boundary being repaired | Yes |
| Two-horizon intertwining | Physical hidden integration leaves future links and retained endpoints external | Definition of `E_hid`, `Q_hid`, and the mark domain | Yes |
| K-retaining marked attachment | Physical-hidden rooted path resolvent and raw/centered split | Equations (0.8)--(0.9) after the new support bridge | Yes, with `E_hid` and external `W,K_1` fixed |

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One primitive coordinate | Yes | An actual hidden coordinate has one owner; external coordinates are not averaged. |
| One owner-site block | Yes | It contains owned skeleton/nonskeleton Haar coordinates and `G_m` only on `I_1`. |
| One connected routed carrier | Yes | `S_X=X` and (0.3). |
| One actual residual factor system | Yes | Equations (0.7)--(0.10). |
| One correlated next-center preintegration | No | `S_next` grammar remains W1. |
| Every horizon | No | W2 remains open. |
| Generic perturbation ball | No | W4 remains open. |
| Critical continuum | No | W5 remains open. |

### N6 — partial-closure and primitive scan

The site-block dictionary, dummy syntactic support, attachment chart, and
factor-two support map are definitions and proved estimates, not new axioms or
framework primitives. The approved axiom/premise registry supplies no silent
`S_next`, taste, time, probability, or continuum theorem. No convention-only
repair is mislabeled as new physics, and no proposed primitive is used.

### N7 — hostile steelman

A hostile reviewer should reject any claim that (3.1) is an all-horizon wall:
the much smaller predecessor root row, the exact shortest-center squaring,
and a scale-indexed diameter moment could pay the lost spatial exponent, while
an `S_next`-adapted block atomization could avoid comparing fixed-product
charts at all. They are right. NG44 is only the failure of identity embedding
from this displayed weak codomain.

### N8 — cross-cycle echo

| earlier wall | repair mechanism | present effect | residual |
|---|---|---|---|
| Hidden/coarse incidence | nonminimal syntactic supports and pinned conversion | Supplies (0.6) | Must be repeated for correlated `S_next`. |
| Formal/physical centering mismatch | restrict `E_hid` to actual hidden variables and leave `W,K_1` external | Mark-alone cancellation is valid | Full future atomization remains separate. |
| Gaussian/Haar root mismatch | route actual eliminated Gaussian sites through owned hidden-site blocks | Product blocks have one root row | Correlated-center sources remain outside. |
| Weak-to-strong completion | enhanced actual-orbit moments | Supplies the deep base factor | Output diameter weight is still weaker. |
| Diameter/tree mismatch | site-block syntactic support | Supplies (0.5) without identifying the norms | Stronger/lineage chart remains open. |
| Running-center wall | shortest-center extraction | Supplies a candidate center and path gain | Full factor/reference grammar remains W1/W3. |

**No-Go Discipline verdict:** PASS WITH BOUNDED CLAIMS for the actual-hidden
site-block support bridge, one actual-residual marked response/ordinary factor
envelope, and the narrow identity-embedding boundary. Fail any reading as a
future-atom return, correlated-center RG step, all-horizon contraction,
generic invariant ball, taste selection, continuum theorem, or axiom-
sufficiency theorem.
