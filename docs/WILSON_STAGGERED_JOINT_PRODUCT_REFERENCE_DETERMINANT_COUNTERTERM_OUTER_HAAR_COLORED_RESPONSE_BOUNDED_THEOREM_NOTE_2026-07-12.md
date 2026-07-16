# Joint product reference, determinant counterterm, and outer-Haar colored response

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_joint_product_reference_counterterm_colored_response_2026_07_12.py`](../scripts/wilson_staggered_joint_product_reference_counterterm_colored_response_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_joint_product_reference_counterterm_colored_response_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_joint_product_reference_counterterm_colored_response_2026_07_12.txt)

## 0. Result

For the original eliminated Wilson--staggered block `A=m1+M_II`, the combined
reference `E_HG_A` has an exact local product-coordinate representation.  Its
pointwise Gaussian denominator becomes an explicitly factorized inverse
determinant-loop counterterm, not a global reciprocal.  Coloring the physical
determinant restore, Wilson plaquettes, and preintegration `K-I/I-K` boundary
sources then gives one joint normalized cluster expansion which controls the
outer Haar partition factor and has an explicit `O(K_R)` response.

Use the exact block/Berezin identity from the
[factor-two Schur theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the determinant-loop and coefficient algebra from the
[retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the product-coordinate atom cost from the
[one-horizon lineage theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the exact Gaussian bond ratio from the
[fixed-background correlated Berezin theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the red-color subtraction envelope from the
[combined-reference interpolation theorem](WILSON_STAGGERED_COMBINED_HAAR_GAUSSIAN_REFERENCE_SPLIT_RESIDUAL_COLORED_INTERPOLATION_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Let

```text
E_0=E_H G_m^prod,
A(U)=m1+M_II(U),
B_G=exp[-bar zeta M_II(U)zeta]=product_e(1+b_e),
Z_A(U)=G_m^prod[B_G]=det A(U)/m^(3|I|)>0.                          (0.1)
```

Then, coefficientwise and at every finite regulator,

```text
E_H G_A[F]=E_0[F B_G Z_A^(-1)].                                   (0.2)
```

Equation (0.2) is pointwise normalization written under one product
expectation.  It is not the false raw-bond identity
`E_HG_m[FB_G]/E_HG_m[B_G]`, which would weight the outer Haar variable by
`Z_A(U)`.

The local determinant expansion is

```text
log Z_A=vacuum+sum_gamma psi_gamma^I,                              (0.3)
```

where odd words vanish, length two is gauge-independent vacuum, and the
remaining words have even length `r>=4`.  Absolute convergence for `m>4`
gives the local counterterm and physical restore

```text
C_A=product_gamma exp(-psi_gamma^I),
D_A(z)=product_gamma exp(z psi_gamma^I).                           (0.4)
```

The vacuum constants cancel from every normalized ratio.  Thus (0.2) is
equivalently `E_0[F B_G C_A]/E_0[B_G C_A]` without ever forming an
uncontrolled global inverse.

For every `K-I` edge group the two orientations into the retained/external
field are

```text
j_e=bar psi_K M_KI zeta_I+bar zeta_I M_IK psi_K.                  (0.5)
```

All `j_e` are even and commute.  Put

```text
J(z)=product_e exp(-z j_e),
W(z)=product_p exp[-z s_p^W],                                     (0.6)
```

and define the joint normalized functional

```text
E_z[O]
 =E_0[O B_G C_A D_A(z)W(z)J(z)]
  /E_0[B_G C_A D_A(z)W(z)J(z)].                                  (0.7)
```

At `z=0`, the normalized `B_GC_A` density under `E_0` reconstructs
`E_HG_A`.  At `z=1`,
`C_AD_A(1)=1` factor by factor, and the numerator becomes the original
preintegration block integrand with the retained onsite term
`m bar psi_K psi_K` extracted as external center data.  Integrating the
boundary factors generates the Schur complement; the Schur paths are not
inserted again as simultaneous input factors.

Use one joint factor-overlap graph on the independent hidden Haar links and
onsite Gaussian sites.  Gaussian sites participate in overlap geometry and
their normalized onsite expectation is contractive at `eta=m^(-1/2)`.  The
displayed factor rows re-Hoeffding only the actual current hidden Haar links;
the standard `Theta+2c` weight already pays the factor-to-polymer and
hard-core allowances in this single joint graph.  There is no second nested
Gaussian-then-Haar expansion requiring another `2c` reserve.

Two carriers are kept distinct.  The hidden overlap set `H_a` of a factor
contains only the hidden Haar-link coordinates and hidden onsite Gaussian
sites used to decide factor connectivity.  Its weighted geometric carrier
`S_a` contains the fine endpoint sites and link span charged by
`exp[(Theta+2c)|S_a|+Lambda ell(S_a)]`.  For a nearest-neighbor bond,
`|S_a|=2` and `ell(S_a)=1`; the hidden Haar coordinate is paid by its `C_*`
atom cost and is not counted as a third spatial site.

The coefficient algebra is the total-even, total-balanced projective
Grassmann algebra over hidden `(bar zeta,zeta)` and retained
`(bar psi,psi)` generators, with weight `eta` per generator, tensored with
continuous hidden-link coefficients and restricted to joint gauge invariants:

```text
A_X^joint
 =[C(SU(3)^(E_X)) tensor
   Lambda_even,total-balanced(bar zeta,zeta,bar psi,psi)]^(G_X).   (0.7a)
```

This algebra contains the individual boundary orientations even though they
are not balanced in the retained variables alone.  Total-even elements
commute and the projective coefficient norm is submultiplicative.  At
`eta=m^(-1/2)`, every onsite `G_m^prod` contraction contributes `1/m` while
removing exactly one barred/unbarred hidden pair of weight `eta^2=1/m`;
hence onsite Gaussian evaluation is contractive with norm one.

With

```text
C_*=3+2sqrt(2),                 L=Theta+2c+Lambda,

K_G=8[exp(9C_*/m)-1]exp[2(Theta+2c)+Lambda],

K_D^-=(3/2)sum_(even r>=4)
       C_*^r(4/m)^r g(3C_*^r(4/m)^r/r)exp(rL),

K_B=8[exp(9C_*/m)-1]exp[2(Theta+2c)+Lambda],

K_D^+=K_D^-,

K_W=12[exp((3beta/4)C_*^4)-1]exp(4L),                             (0.8)
```

where `g(x)=(exp(x)-1)/x`, the uncolored and red rows are

```text
K_ref=K_G+K_D^-,
K_R=K_B+K_D^++K_W,
K_T=K_ref+K_R<c.                                                   (0.9)
```

The equality of the safe `K_G` and `K_B` envelopes has different ownership:
`K_G` is uncolored `I-I` reference transport; `K_B` is the grouped physical
boundary-source row.  Each group has potential norm at most `9/m`, is charged
by one current Haar coordinate, has two endpoint supports and diameter one,
and has incidence at most eight.  The hidden Gaussian site is integrated in
the common product reference and is not charged as a future Gaussian atom.
In the declared first-layer overlap graph, each eliminated boundary midpoint
is incident to at most two grouped `K-I` edges and each skeleton hidden
coordinate occurs in the two fine halves of one coarse path.  The hidden
rooted incidence is therefore at most two; factor eight is a conservative
envelope and does not treat the external retained endpoint as hidden.

For

```text
D=sup_(n integer>=1)n exp[-(c-K_T)n],       tau=K_T D<1,           (0.10)
```

the selected joint KP logarithm is absolutely convergent for every
`|z|<=1`.  If `E_HG_A[O]=0` and `O` belongs to the declared **joint
superstrong source norm**, normalized color subtraction removes the complete
red-free marked series coefficientwise.  Every survivor contains at least
one factor from `K_R`; neither `B_G` nor `C_A` counts as red.  The prior
two-root envelope therefore gives

```text
||E_1[O]||_joint-weak
 <=A_joint ||O||_joint-superstrong,
A_joint=2D K_R/(1-tau)^3.                                        (0.11)
```

Here the joint superstrong norm is the projective marked coefficient norm at
full weights `(Theta+2c,Lambda,eta)` on the combined hidden-coordinate
overlap graph, with the current-Haar canonical atom weight `r_*=1+sqrt(2)`.
The codomain keeps the corresponding connected output at the half spatial
weights.  This is a declared graph domain, not an embedding theorem for every
ambient generated source.

At

```text
m=2 10^6, beta=2 10^(-10), c=0.2,
Theta=10^(-6), Lambda=1, eta=m^(-1/2),                             (0.12)
```

the runner-evaluated rows are

```text
K_G       =1.269376642763024 10^(-3),
K_D^-     =7.489754131643805 10^(-18),
K_B       =1.269376642763024 10^(-3),
K_D^+     =7.489754131643805 10^(-18),
K_W       =5.617316072359065 10^(-4),
K_ref     =1.269376642763032 10^(-3),
K_R       =1.831108249998938 10^(-3),
K_T       =3.100484892761970 10^(-3)<c,
D         =1.868134495408053,
tau       =5.792122780660176 10^(-3),
A_joint   =6.961784176120600 10^(-3).                             (0.13)
```

The old hidden-to-coarse scalar conversion would give

```text
68exp(1/2)A_joint=0.7805068324171649<1.                            (0.14)
```

Equation (0.14) is arithmetic compatibility only.  The exact result is the
joint response (0.11).  A new coarse-shadow/provenance theorem must show that
the preintegration boundary/reference graph obeys the prior conversion with
the required future atoms before (0.14) can be called an RG contraction.

## 1. Exact local normalization counterterm

For fixed `U`, the correlated normalized Gaussian is

```text
G_A[F]=G_m^prod[F B_G]/Z_A(U).                                    (1.1)
```

Applying `E_H` proves (0.2) directly.  The determinant word expansion follows
from

```text
log det A=3|I|log m
 +sum_(r>=1)(-1)^(r+1)Tr[(M_II/m)^r]/r.                            (1.2)
```

The eliminated graph is bipartite, so odd `r` vanish.  At the admitted
regulators the length-two words are immediate reversals and their transport
is the identity.  After extracting those constants, the absolutely summable
length-`r>=4` potentials in (0.3) factorize both signs in (0.4).  The negative
sign changes no coefficient-norm majorant, hence `K_D^-=K_D^+`.

This is a local inverse-partition lemma: every inverse coefficient is
generated by the same support-decaying determinant potentials and the common
KP logarithm selects its branch uniformly.  It is not the bare global object
`1/E_H Z`, a volume lower bound, or an inverse of the retained Schur
determinant.

At color one,

```text
B_G C_A D_A(1)=B_G.                                                (1.3)
```

Thus the physical determinant is restored exactly once.  Writing `B_G`
without `C_A` would already include the determinant body; adding `D_A` to
that raw representation would double count it.  Equation (0.7) avoids that
trap by fixing one ledger throughout the interpolation.

## 2. Actual preintegration red factor grammar

The block quadratic form before eliminating `I` is

```text
bar zeta A zeta
 +bar psi_K m psi_K
 +bar psi_K M_KI zeta+bar zeta M_IK psi_K.                          (2.1)
```

The retained mass term is the extracted external center.  Group the last two
terms by undirected `K-I` edge as in (0.5).  Since each group is even,

```text
exp[-sum_e j_e]=product_e exp(-j_e).                               (2.2)
```

With `eta=m^(-1/2)`, the two orientations together have coefficient norm at
most `9/m`.  A grouped edge uses one hidden skeleton Haar link and one hidden
Gaussian site; its retained endpoint and coarse link are external
coefficient/support data.  Each eliminated boundary midpoint and each
skeleton hidden link meets at most two grouped boundary factors in the
declared hidden overlap graph.  Bounding that incidence by eight gives `K_B`
in (0.8) without reclassifying the retained endpoint as hidden.  The same
one-link atom estimate and eight-bond hidden-site incidence applied to the
`I-I` potential proves `K_G`.

The ownership ledger is therefore:

| object | color | exact role | forbidden duplicate |
|---|---:|---|---|
| `m^(3|I|)` and length-two determinant constant | none | extracted vacuum normalization | never an activity |
| `B_G` `I-I` bonds | blue/uncolored | normalized Gaussian reference transport | never a physical red factor |
| `C_A=Z_A^(-1)` loop factors | blue/uncolored | local pointwise-normalization counterterm | never a second physical determinant |
| `D_A(z)=Z_A^z` loop factors | red | physical outer-Haar determinant restore | do not also insert `det A` as a body |
| Wilson plaquettes | red | physical scalar gauge weight | do not count in the fixed-`U` Gaussian arm |
| grouped `K-I/I-K` sources | red | physical preintegration fermionic coupling | do not also insert their generated Schur paths |
| retained `m bar psi psi` | none | extracted center data | do not put it in KP smallness |
| Schur complement and `S^(2)` | output only | generated after boundary integration | never simultaneous input factors |

This is an actual factor-level instantiation for the original center.  It is
not an instantiation of the next `S^(2)` input chart.  The present residual
after the next pullback is certified only at weak future spatial weights, so
it cannot be exponentiated as the next strong red family here.

## 3. One joint colored cluster expansion

Work at finite regulator and expand all factors in (0.7) in one common
product-coordinate algebra (0.7a).  Two factors overlap when their hidden
sets `H_a` share a Haar coordinate or onsite Gaussian site.  The determinant
and Wilson factors have only Haar overlap coordinates; the Gaussian and
boundary factors additionally use onsite Gaussian sites.  Spatial weights
are carried separately by `S_a`.  All coefficient elements are total-even
and commute.

The weighted rooted incidence rows are exactly (0.8)--(0.9).  Under
`K_T<c`, factor-to-polymer grouping and the normalized hard-core logarithm
converge absolutely.  The two copies of `c` visible in `Theta+2c` are the
standard allowances for those two combinatorial layers.  The construction is
one joint grouping, not a nested conditional-Gaussian expansion followed by a
second outer-Haar expansion reusing either allowance.

Let `H(t)=t(2-t)/(1-t)^2`.  The K-retaining marked envelope obeys

```text
a_0(K,c)<=KD,
A_att(K,c)<=H(DK),                                                 (3.1)
```

when `D` is frozen at the total row.  At `z=0`, the entire normalized
red-free marked sum is `E_HG_A[O]=0`.  Color-preserving subtraction between
the `z=1` and `z=0` joint series therefore removes every cluster without a
physical red factor.  With `H'(t)=2/(1-t)^3`,

```text
H(DK_T)-H(D(K_T-K_R))
 <=D K_R H'(DK_T)
 =2D K_R/(1-tau)^3.                                                (3.2)
```

This proves (0.11).  Global combined centering is sufficient because the
subtraction occurs after constructing the complete joint normalized series;
it is never replaced by pointwise `G_A` centering or coordinatewise Haar
centering.

The scalar body at finite retained field is positive at zero Grassmann
degree, selecting the physical logarithm branch.  Bounds on the retained
nilpotent coefficients come from the connected Banach-algebra expansion, not
from ordering Grassmann coefficients or averaging a fixed-`U` supremum.

## 4. What closes and what remains

This theorem closes three items at the original center:

1. an exact local product representation of the combined reference;
2. exact physical ownership of determinant, Wilson, and boundary red factors;
3. a globally normalized joint response with `A_joint(0)=0` on the declared
   source graph domain.

It bypasses, rather than proves, a separate generic embedding of
`g(U)=G_A(U)O` into the split Haar provenance norm.  Such an evaluation lemma
is still useful for modular scale iteration, but it is not needed for the one
joint expansion in Section 3.  The theorem also does not prove a generic
ambient-to-joint source embedding, the new coarse-shadow/strong-spatial
handoff, next-center migration, persistent gap, same-norm Hessian, invariant
ball, fixed point, critical trajectory, or continuum limit.

The next exact target is the coarse-shadow theorem for the joint boundary
grammar: evaluate the hidden Gaussian sites, canonically re-Hoeffding the
resulting Haar coefficients, split genuine empty future atoms from nonempty
atoms, and land in the next strong spatial norm.  Only then can the same
counterterm ledger be instantiated around the extracted `S^(2)` center.

No probability rule, physical time law, or action-selection principle is
derived here.  No axiom-update stop is established.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_joint_product_reference_counterterm_colored_response_2026_07_12.py
```

The runner checks a first-principles two-site, three-color anti-Hermitian
hopping determinant against its product-Gaussian bond ratio, a finite exact
counterterm representation of `E_HG_A`, color-one cancellation and recovery
of the physical integrand, the failure of naive outer averaging, the colored
generating derivative, the strict activity witness, exact zero-red
cancellation at fixed envelope, and the source/dependency contract.  The
arbitrary-regulator determinant and joint cluster bounds are analytic
statements.

## 6. No-Go Discipline N1--N8

This is a positive bounded theorem with named nonclosures.  The audit prevents
the local counterterm from being mislabeled as a global reciprocal or the
joint response from being promoted to an autonomous RG map.

### N1 — alternative-route enumeration

| route | disposition | exact residual |
|---|---|---|
| Exact combined split and total covariance | `ATTEMPTED` | Algebraically closed earlier; modular Haar provenance remained open. |
| Fixed-`U` residual coloring | `ATTEMPTED` | Closed an abstract pointwise arm but not the outer partition factor. |
| Raw `B_G` under global normalization | `ATTEMPTED` | Rejected: its baseline is determinant-weighted Haar, not `E_HG_A`. |
| Pass a fixed-`U` bound through Haar by positivity | `ATTEMPTED` | Invalid for coefficient/Grassmann-valued outer weights. |
| Bare global inverse partition | `ATTEMPTED` | Insufficient for uniform locality and forbidden without a support-decaying inverse. |
| Local inverse determinant-loop counterterm | `ATTEMPTED` | Sections 1--3 prove the exact product ledger and joint colored response. |
| Positive-body determinant/Wilson telescoping | `LIVE` | Alternative modular architecture if separate split-arm iteration is needed. |
| Nested Gaussian then Haar expansion | `LIVE` | Requires distinct inner and outer reserves; not used by the one-joint proof. |
| Canonical post-evaluation provenance for `g` | `LIVE` | Still needed for modular split-arm reuse and the next strong handoff. |
| Import weak future atoms as strong next factors | `RULED OUT BY PRIOR` | The two-horizon theorem explicitly lands at weak spatial weights. |
| Future `S^(2)` counterterm chart | `LIVE` | Waits for strong factor membership and new determinant/boundary ownership. |

### N2 — wall-independence audit

Keep six walls after the present partial closure:

```text
W1 coarse-shadow strong-spatial tag-density/empty-atom handoff,
W2 generic joint-source embedding and modular g provenance,
W3 future-center migration/update/gap/normalization,
W4 same-norm Hessian and invariant ball,
W5 physical taste/chart selection,
W6 critical trajectory and observables.                            (N2.1)
```

All fifteen pairs remain independent.

| pair | why neither wall absorbs the other |
|---|---|
| W1--W2 | A joint graph-domain response does not embed generic sources or prove tag density. |
| W1--W3 | Center migration changes carriers but does not provide strong spatial return. |
| W1--W4 | Same-norm nonlinear closure separately requires a strong codomain. |
| W1--W5 | Taste assignment needs physical carriers, not only atom downshift. |
| W1--W6 | Critical iteration cannot reuse a weak output as its own domain. |
| W2--W3 | The source evaluation and determinant ledger change with the center. |
| W2--W4 | A one-mark domain embedding is not a Hessian or invariant ball. |
| W2--W5 | Provenance control does not select a taste sector. |
| W2--W6 | Massive response supplies no critical tuning path. |
| W3--W4 | Ball invariance needs both a running center and nonlinear control. |
| W3--W5 | Center form and normalization affect the physical field chart. |
| W3--W6 | A persistent gap/normalization trajectory is independently needed. |
| W4--W5 | Nonlinear closure must separately preserve the physical symmetry/taste sector. |
| W4--W6 | Autonomy is a prerequisite, not a critical trajectory. |
| W5--W6 | Physical observables require a selected physical chart. |

### N3 — hidden-condition phrase scan

| phrase | meaning in this note |
|---|---|
| `joint` | One coefficient-cluster expansion on the combined product-coordinate graph, not a probabilistic mixture. |
| `combined reference` | `E_HG_A`, distinct from the determinant-weighted raw-`B_G` model. |
| `counterterm` | The local factorization of negative determinant-loop potentials, not a bare global reciprocal. |
| `positive` | Used only for the zero-Grassmann scalar body and branch selection. |
| `red` | A physical factor outside the declared reference; the determinant is owned once. |
| `actual` | The original-center preintegration factor map in Section 2, not a scalar-row analogy. |
| `global response` | A finite-regulator normalized coefficient functional controlled by connected expansion. |
| `joint superstrong source norm` | The declared graph domain at full marked weights, not a generic ambient equivalence. |
| `weak` | The connected half-weight output, not the next strong domain. |
| `interpolation` | Auxiliary activity color `z`, not time or RG flow. |
| `arithmetic compatibility only` | Equation (0.14); the coarse conversion is not yet proved for this grammar. |
| `uniform` | Uniform in the displayed original-center massive wedge and admitted regulators, not center- or critical-uniform. |

### N4 — citation/residual matching

| dependency | load-bearing use | residual matched? |
|---|---|---:|
| [Factor-two Schur theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact preintegration block, determinant positivity, and Schur output | Yes |
| [Retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Local determinant loop row and even balanced coefficient algebra | Yes |
| [One-horizon lineage theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Current-Haar `C_*` factor costs and support counts | Yes |
| [Fixed-background correlated Berezin theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact `B_G/Z_A` reference identity and determinant separation | Yes |
| [Combined-reference interpolation theorem](WILSON_STAGGERED_COMBINED_HAAR_GAUSSIAN_REFERENCE_SPLIT_RESIDUAL_COLORED_INTERPOLATION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Color-preserving `H'` envelope and outer-normalization boundary | Yes |

### N5 — rhetoric and resolution audit

The theorem is fixed to the original `A=m1+M_II`, one globally combined-
centered mark in the declared joint graph domain, the actual preintegration
determinant/Wilson/boundary grammar, and one weak response.  The local inverse
counterterm is explicitly factorized and its determinant restore is colored
once.  No coefficient-valued positivity, global reciprocal, raw-bond reference
migration, post-Schur double count, future-center import, generic source
closure, or same-norm claim is used.

### N6 — partial-closure and primitive scan

The joint counterterm route genuinely closes the outer partition factor and
actual original-center red-factor ownership on its declared source domain.
The remaining source, spatial, center, and nonlinear walls are constructive
norm/chart problems.  Activity color is not physical time, Haar/Berezin
normalization is not a Born rule, and choosing the Wilson--staggered action is
not an axiom derivation.  No axiom-update stop is established.

### N7 — hostile steelman

A hostile reviewer should demand that `E_HG_A` be distinguished from raw
`B_G`; equations (0.2) and (1.3) do so.  They should reject a standalone
`Z_A^(-1)`; Section 1 factorizes it locally with a selected KP branch.  They
should forbid determinant double counting and boundary-plus-Schur input;
Section 2 does both.  They should reject positivity on retained Grassmann
coefficients; Section 3 uses connected Banach-algebra normalization instead.
They should reject global centering as coordinate centering, generic source
embedding, a one-mark Hessian, weak-as-strong reuse, and `q_arith` as an RG
theorem; none is asserted.  A nested split-arm route remains live, so no broad
no-go is licensed.

### N8 — cross-cycle echo

The result preserves the earlier explicit-red `O(K_R)` cancellation, the
fixed-background determinant separation, the retained-Grassmann positive body
and ban on uncontrolled inverse Schur reweighting, the one-/two-horizon atom
creation/erasure boundary, and the K-retaining strong-to-weak limitation.  It
advances the lane by replacing the outer-normalization wall with an exact
local counterterm and actual preintegration factor map, while leaving future
spatial, center, nonlinear, and continuum walls visible.
