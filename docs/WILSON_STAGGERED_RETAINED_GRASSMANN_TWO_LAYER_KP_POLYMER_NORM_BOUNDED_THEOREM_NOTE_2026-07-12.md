# Simultaneous retained-Grassmann polymer control for constrained Wilson--staggered fibers

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_2026_07_12.py`](../scripts/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_2026_07_12.txt)

## 0. Result

The exact one-step retained gauge--Grassmann logarithm now belongs to one
simultaneous all-degree connected polymer norm in an explicit high-mass,
small-coupling region.

Three prior surfaces are used without changing their scope:

- the [exact retained Schur weight and fixed-background locality](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md);
- the [joint generated-action coefficient space and anchored norm](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md);
- the [two-layer rooted-tree/Kotecky--Preiss lemma and syntactic support map](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md).

The positive body of the retained weight is `det D_II`, not the full
determinant controlled in the last dependency. The proof therefore derives a
new anchored hopping expansion for `det D_II`; it does not insert an
uncontrolled `(det S)^(-1)` reweighting.

Let

```text
h=4/m,
L=theta+2c+lambda,
q=h exp(L),                                                          (0.1)
```

where `c,theta,lambda,eta>0` and `m>4`. Put
`g(t)=(exp(t)-1)/t`, with `g(0)=1`, and define

```text
K_W=12[exp(3 beta/4)-1]exp(4L),                                     (0.2)

K_I=(3/2)sum_(even r>=4)
       h^r g(3h^r/r) exp(rL),                                      (0.3)

K_S=18 eta^2 sum_(r>=2)
       r h^(r-1)
       g(9 eta^2 2^(-r)m^(-(r-1))) exp(rL),                         (0.4)

K_joint=K_W+K_I+K_S.                                                (0.5)
```

Whenever

```text
q=h exp(L)<1,                    K_joint=K_W+K_I+K_S<c,              (0.6)
```

on the declared reflection-compatible periodic regulators with every fine
extent at least four, the finite-volume exact action

```text
Gamma_c(V,bar psi,psi)=-log W_c(V,bar psi,psi)                       (0.7)
```

has a regulator-, hidden-boundary-, and coarse-`V`-uniform connected
decomposition in the generated coefficient space. After removing the
`V,bar psi,psi`-independent vacuum constant,

```text
||Gamma_c||_(lambda/2,theta/2,eta)
 <=68 exp(lambda/2)c+3m eta^2 exp(theta/2).                          (0.8)
```

The bound sums all endpoints, paths, connected supports, color components,
and every balanced Grassmann degree at once. It implies local coefficient
limits and one common complete Reinhardt source domain around the exact
one-step action. The coefficients remain jointly coarse-gauge invariant.

Three strict points with `theta=lambda=0.001` are

| `m` | `beta` | `c` | `eta` | `K_W` | `K_I` | `K_S` | `K_joint` | `c-K_joint` | `q` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 0.0005 | 0.120 | 0.020 | 0.0118493 | 0.0597052 | 0.0185296 | 0.0900840 | 0.0299160 | 0.4245981 |
| 16 | 0.0010 | 0.120 | 0.050 | 0.0237030 | 0.0171894 | 0.0660856 | 0.1069779 | 0.0130221 | 0.3184485 |
| 20 | 0.0025 | 0.125 | 0.040 | 0.0617104 | 0.0070465 | 0.0301263 | 0.0988832 | 0.0261168 | 0.2573192 |

This is one-step mathematical closure for the declared form-migrating
retained variables. `eta` is a convergence coordinate; it is not a physical field normalization. The theorem does not prove an invariant RG neighborhood,
projected/rescaled contraction, taste selection, retained-fermion OS
reconstruction, a critical trajectory, or any Lorentz/QFT/Standard Model/GR
limit.

No negative theorem is shipped. No axiom-update stop is established.

## 1. The correct positive body

The exact retained weight is

```text
W_c(V,bar psi,psi)
 =integral dH exp[-S_W(U)] det D_II(U)
             exp[-bar psi S(U)psi],                                 (1.1)
```

with `S=mI-D_KI D_II^(-1)D_IK`. Its scalar body at zero retained
Grassmann field is

```text
Z_II(V)=integral dH exp[-S_W(U)]det D_II(U)>0.                       (1.2)
```

By contrast, full fermion integration produces the body with
`det D=det D_II det S`. Passing from that measure to (1.2) would require the
factor `(det S)^(-1)`. No volume-uniform local bound for that factor has been
proved, so it is not used.

The eliminated induced graph `I` is bipartite. Its staggered hop `M_II` has at
most eight oriented blocks of norm `1/2` in each row. For `m>4`, the exact
absolutely path-convergent expansion is

```text
log det D_II
 =3|I|log m
  +sum_(r>=1)(-1)^(r+1)Tr[(M_II/m)^r]/r.                             (1.3)
```

Odd `r` vanish by bipartite parity. At fine extent at least four, every closed
length-two word is an immediate reversal, and its transporter is
`U U^dagger=1`; these terms join the extracted vacuum constant. Reverse-pair
the remaining even closed paths at `r>=4`. The excluded extent-two wrap is a
finite-size alias, not part of the theorem.

For a fixed positive fine link, choose its orientation and one of `r` path
positions. The remaining `r-1` steps have at most eight choices. With the
color-trace factor three and the coefficient in (1.3),

```text
sum_(order r paths through fine link e)||psi_gamma^I||_infinity
 <=(3/r)[2r 8^(r-1)]2^(-r)m^(-r)
 =(3/4)h^r.                                                         (1.4)
```

A hidden coordinate has a one- or two-link syntactic footprint. Therefore

```text
sup_a sum_(gamma:a in S_gamma, order r)||psi_gamma^I||_infinity
 <=(3/2)h^r.                                                        (1.5)
```

An individual reverse-paired potential has the safe bound

```text
t_r^I=3h^r/r.                                                       (1.6)
```

The actual individual path coefficient is much smaller; (1.6) is chosen so
that no root, color, or reverse-pair convention is hidden. Since
`exp(x)-1<=x g(t_r^I)` for `0<=x<=t_r^I`, and each syntactic support has
`|S_gamma|,ell(S_gamma)<=r`, equations (1.5)--(1.6) give exactly (0.3).
The Wilson midpoint factors give (0.2) as before.

## 2. Schur paths in the even balanced Banach algebra

For `m>4`, use the direct hopping series

```text
D_II^(-1)
 =m^(-1)sum_(n>=0)(-M_II/m)^n.                                     (2.1)
```

After the two outer hops in the Schur complement, a term with `n` internal
hops is a retained-to-retained path of length `r=n+2`. Its transporter is
unitary and its scalar coefficient obeys

```text
|a_gamma|<=2^(-r)m^(-(r-1)).                                       (2.2)
```

Write the corresponding jointly gauge-invariant even bilinear as

```text
B_gamma
 =a_gamma bar psi_(x_gamma) U_gamma psi_(y_gamma).                  (2.3)
```

The entrywise color sum of a `3 by 3` unitary is at most nine. In the
coefficient norm with weight `eta`,

```text
||B_gamma||_eta
 <=x_r=9 eta^2 2^(-r)m^(-(r-1)).                                   (2.4)
```

Even Grassmann elements commute. Hence the exact Schur exponential factors as

```text
exp[-bar psi(S-mI)psi]=product_gamma exp(B_gamma),                  (2.5)
```

with the path signs absorbed into `a_gamma`. No bilinear truncation is made:
each factor and products of distinct factors contain the balanced quartic and
higher terms allowed by the generated action space. Submultiplicativity gives

```text
||exp(B_gamma)-1||_eta
 <=exp(x_r)-1=x_r g(x_r).                                           (2.6)
```

The same fixed-link word count as in (1.4), now without the trace coefficient,
gives

```text
sum_(length r Schur paths through fine link e)||B_gamma||_eta
 <=9 eta^2 r h^(r-1).                                               (2.7)
```

The hidden footprint factor two and (2.6) give

```text
sup_a sum_(gamma:a in S_gamma, length r)
 ||exp(B_gamma)-1||_eta
 <=18 eta^2 r h^(r-1)g(x_r).                                       (2.8)
```

Again `|S_gamma|,ell(S_gamma)<=r`; weighting (2.8) produces exactly (0.4).
This is the load-bearing simultaneous sum. It counts all retained endpoints
because fixing the traversed fine link and the word position determines the
start once the other steps are chosen.

The hidden-independent onsite mass factor is extracted from (2.5):

```text
Phi_mass=m sum_(X,a) bar psi_X^a psi_X^a.                            (2.9)
```

It contributes `3m eta^2 exp(theta/2)` to (0.8) and requires no KP smallness.

## 3. Banach-algebra two-layer expansion

Use the coefficient algebra

```text
A_X=[C(SU(3)^(E_X)) tensor
     Lambda_even,balanced(bar psi_X,psi_X)]^(G_X),                  (3.1)
```

with

```text
||Phi_X||_eta
 =sum_(p,P,Q;|P|=|Q|=p)
   eta^(2p)||phi_(X;P,Q)||_infinity.                                (3.2)
```

This weighted coefficient `l1` norm is submultiplicative. The even sector is
commutative, and coefficient-wise Haar integration is contractive. Thus the
interaction factors from Sections 1--2 can be grouped by hidden-support
overlap exactly as scalar factors were grouped in the prior two-layer lemma.

For a connected factor collection `Gamma`, its activity is now an element of
the even balanced Banach algebra:

```text
w_Gamma(V,bar psi,psi)
 =integral product_(a in Gamma) f_a dH_(Y_Gamma),
||w_Gamma||_eta<=product_(a in Gamma)||f_a||_eta.                   (3.3)
```

The rooted-tree recursion and the final hard-core exclusion proof use only
nonnegative norm majorants. Replacing absolute value by `||.||_eta` therefore
gives the same sufficient condition

```text
sup_h sum_(a:h in S_a)
 ||f_a||_eta exp[(theta+2c)|S_a|+lambda ell(S_a)]<c.                (3.4)
```

Equations (0.2)--(0.5) are the three contributions to its left side. Under
(0.6), the hard-core connected logarithm converges absolutely in the Banach
algebra. Its body is positive, so this convergent branch equals the exact
finite Grassmann logarithm in (0.7).

The same norm proof remains valid after multiplying any finite local family of
additional even balanced sources whose total weighted activity fits inside
the strict margin `c-K_joint`. Hence the logarithm has a common complete
Reinhardt source domain and every finite-order coefficient derivative is a
connected marked cluster. Unlike coefficient-by-coefficient scalar disks,
this one estimate sums every Grassmann degree simultaneously.

Useful closed envelopes are

```text
K_I<=(3/2)exp(3h^4/4) q^4/(1-q^2),                                 (3.5)

K_S<=18 eta^2 exp(9eta^2/(4m))
       exp(L) q(2-q)/(1-q)^2.                                      (3.6)
```

The runner evaluates the actual series at the three displayed points and
checks both envelopes.

The abstract scalar polymer theorem is R. Kotecky and D. Preiss,
*Cluster expansion for abstract polymer models*, Communications in
Mathematical Physics **103** (1986), 491--498, DOI
`10.1007/BF01211762`. The Banach-algebra extension used here is proved by the
same displayed norm majorant and absolutely convergent combinatorial series;
no separate model theorem is imported.

## 4. Hidden-to-coarse joint norm

Use the nonminimal syntactic supports before any `A A^(-1)V` cancellation.
Every retained-to-retained Schur path begins and ends with a fine link in an
outgoing or incoming skeleton pair. Adding both endpoints of each charged
skeleton coordinate therefore includes both fermion endpoints as well as
every exposed coarse link.

For a connected hidden polymer `Y`, the resulting coarse support `X(Y)` obeys

```text
X(Y) connected,
|X(Y)|<=2|Y|,
diam X(Y)<=ell(Y)+1.                                                 (4.1)
```

At most 64 positive fine-link anchors and four incoming skeleton endpoints
charge one coarse cell, so the safe conversion multiplicity remains 68.
Grouping all joint clusters with the same coarse support and using (4.1)
gives

```text
sup_z sum_(connected X contains z)
 exp[(lambda/2)diam X+(theta/2)|X|] ||Phi_X||_eta
 <=68 exp(lambda/2)c                                                 (4.2)
```

for the cluster part. Adding (2.9) proves (0.8).

Every scalar determinant path is gauge invariant. Every Schur path factor
contracts its open transporter with retained endpoint fields and is jointly
gauge invariant. Haar integration, multiplication, and the connected
logarithm preserve that invariance. Balanced degree is likewise preserved
term by term.

The uniform pinned expansion also constructs local infinite-volume
coefficients: every finite cluster stabilizes once the regulator contains it,
while the omitted diameter tail is uniformly summable. This is a local
coefficient limit, not an iterated critical RG trajectory.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_2026_07_12.py
```

The runner checks the three strict joint KP points, both closed envelopes, the
fixed-link determinant and Schur word-incidence factors, the bipartite
length-two constant floor, coefficient-norm submultiplicativity, and a
coefficient-exact two-hidden-coordinate Banach-valued factor-to-polymer
identity. The latter has overlapping bilinear path factors and a nonzero
balanced quartic connected logarithm. It also checks coarse support and the
source/dependency contract. The infinite rooted-tree and thermodynamic-limit
steps are analytic statements.

## 6. Honest boundary and next theorem

This theorem closes membership of the exact one-step form-migrating retained
action in the declared joint norm at the displayed points. It does not say
that the norm ball maps into itself after field/geometric rescaling, or that
the same `eta` is a physical normalization.

The next theorem must define symmetry-adapted vacuum, mass, kinetic, gauge,
and other relevant/marginal coordinates; extract them; apply factor-two
geometric and field rescaling; and bound the derivative of the remaining map
strictly below one on an invariant neighborhood. The exact raw unit directions
make that projection load-bearing.

Taste-faithful hypercube variables, auxiliary-field reorganizations, and
alternative block kernels remain live. Failure of this sufficient inequality
outside the displayed region would not establish failure of joint locality.

## 7. No-Go Discipline N1--N8

No negative theorem or route foreclosure is shipped. The boundary statements
are scope limits. The checks are retained conservatively because the theorem
advances a prior no-go-sensitive RG campaign.

### N1 — alternative-route enumeration

| Route | Status | Executed test | Result |
|---|---|---|---|
| Full-determinant reweighting | `ATTEMPTED` | Section 1 compares the exact bodies. | Rejected as an input because `(det S)^(-1)` has no local bound. |
| Direct eliminated-determinant hopping expansion | `ATTEMPTED` | Equations (1.3)--(1.6). | Supplies the correct positive-body activity row for `m>4`. |
| Schur path expansion | `ATTEMPTED` | Equations (2.1)--(2.8). | Sums endpoints, paths, colors, and supports. |
| Banach-valued two-layer KP | `ATTEMPTED` | Section 3 replaces scalar absolute values by the submultiplicative norm. | Sums all balanced degrees simultaneously. |
| Coefficientwise complex disks | `ATTEMPTED` | Compared with the common margin after (3.4). | Strictly weaker than the simultaneous algebra estimate. |
| Direct exterior-algebra regrouping | `ATTEMPTED` | Runner evaluates the exact finite identity and logarithm. | Confirms higher connected degree generation. |
| Hidden-to-coarse support conversion | `ATTEMPTED` | Section 4 and runner. | Preserves endpoints and the safe 68 multiplicity. |
| Auxiliary-field/taste-faithful reorganizations | `UNTESTED / LIVE` | Not used in the positive proof. | Remain live routes to larger or more physical regions. |

### N2 — wall-independence audit

The collapsed downstream conditions are `projected/rescaled invariant RG
neighborhood`, `physical taste-carrier identification`, and `critical
trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| projected/rescaled invariant RG neighborhood | physical taste-carrier identification | No | No | Yes |
| projected/rescaled invariant RG neighborhood | critical trajectory/observable identification | No | No | Yes |
| physical taste-carrier identification | critical trajectory/observable identification | No | No | Yes |

Joint norm membership is now an input to the first condition, not a separate
remaining wall.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Fixed gauge background is an explicit Schur variable. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical Grassmann` | Ordering is algebraic bookkeeping only. |
| `standard CAR` | No CAR/Fock import occurs. |

### N4 — citation/residual matching

| Witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| [Exact Schur block](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Fixed-background locality; no joint norm | Exact weight, positivity, covariance, and hopping matrices | Yes |
| [Generated-action space](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Finite-volume membership only | Target algebra and norm | Yes |
| [Scalar two-layer KP](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Full-determinant gauge body only | Abstract two-layer lemma and support conversion, not its body | Yes |
| Kotecky--Preiss 1986 | Abstract scalar hard-core convergence | Norm-majorized combinatorial series | Yes |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Every finite regulator at the three points | Yes | Exact joint connected logarithm and uniform norm. |
| Local infinite-volume coefficients | Yes | Pinned cluster limits. |
| Every balanced Grassmann degree simultaneously | Yes | One `eta`-weighted sum is finite. |
| All `m>4` or the whole Block28 region | No | Only points/parameters satisfying (0.6). |
| One rescaled RG self-map | No | Next theorem. |
| Iterated critical trajectory | No | No existence or impossibility claim. |
| Retained-fermion OS/CAR/QFT reconstruction | No | Not inferred from Euclidean polynomial closure. |

### N6 — partial-closure and primitive scan

The Wilson--staggered action, formal Grassmann variables, and straight
factor-two block are previously declared regulator data. Haar/Gibbs
integration is mathematical measure machinery, not a Born probability or
record-formation law. `eta` is a convergence coordinate. No action, time,
probability, CAR, field-normalization, taste, scale, or state primitive is
added.

The registered scale-reference, kinetic-isotropy, and realized-state
primitives neither supply nor obstruct this estimate. The remaining
projection/rescaling problem is ordinary constructive mathematics.

### N7 — hostile steelman

A hostile reviewer should first reject importing the full-determinant fiber
measure. Correct; Section 1 builds the correct `det D_II` expansion instead.
The price is the stricter `m>4` hopping region.

A second hostile reviewer should demand that every endpoint, path position,
orientation, color coefficient, support, and Grassmann degree be paid once.
Correct; equations (1.4), (2.4), (2.7), and (2.8) expose those factors, while
the Banach exponential pays all powers of each bilinear.

A third should object that small `eta` may hide a physical field rescaling.
Correct as a physical criticism; the theorem claims Banach membership for a
declared convergence coordinate, not a selected normalization or invariant
RG domain.

### N8 — cross-cycle echo

| Earlier surface | Earlier residual | Retired here? | Treatment |
|---|---|---:|---|
| Fixed-background Schur locality | No hidden cumulants or joint norm | Yes, in (0.6) | Direct path activities enter one algebra-valued cluster expansion. |
| Generated-action space | Finite-volume algebra only | Yes, at the displayed points | Exact action has a uniform connected decomposition. |
| Full-determinant gauge-body KP | Wrong positive body for retained fields | No, as a body | Its two-layer lemma is reused after a new `det D_II` row. |
| Raw action unit directions | No unprojected contraction | No | Projection/rescaling remains the next theorem. |
| One-even-site Schur block | Not taste faithful | No | No physical taste label is promoted. |

No partial closure is relabeled as contraction or continuum physics, and no
axiom update is requested.

**No-Go Discipline status: PARTIAL ATTEMPT.** The seven explicit algebraic
routes above were exercised, but the auxiliary/taste reorganization is live
and untested and does not count toward an N1 PASS.
