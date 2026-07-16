# Combined Haar--Gaussian reference split and residual-colored interpolation

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_combined_reference_split_residual_interpolation_2026_07_12.py`](../scripts/wilson_staggered_combined_reference_split_residual_interpolation_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_combined_reference_split_residual_interpolation_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_combined_reference_split_residual_interpolation_2026_07_12.txt)

## 0. Result

For the fixed original eliminated Wilson--staggered quadratic block, combined
Haar--Gaussian centering has an exact two-arm split.  The pointwise
Gaussian-centered arm also has a fixed-background residual-colored cluster
bound with an explicit `O(K_R)` prefactor while the Gaussian
reference-bond row is held fixed.  These statements isolate the two exact
interfaces needed by a future combined-reference theorem without pretending
that outer Haar normalization or a generic source embedding has already been
controlled.

Use the normalized correlated Gaussian and its locality suppliers from the
[fixed-background correlated Berezin theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the marked-tree majorants from the
[K-retaining attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the determinant/Schur factor ownership from the
[retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the actual two-horizon atom and weak-spatial boundary from the
[two-horizon intertwining theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Fix

```text
A(U)=m1+M_II(U),                 G_A(U)[1]=1,
E=E_H G_A(U),                   m>4.                              (0.1)
```

This is the original `A=m1+M_II`, not the extracted future `S^(2)` center.
Let `L` lift a gauge-only coefficient to the full gauge--Grassmann algebra,
so `G_A(U)Lh(U)=h(U)`.  If `E O=0`, put

```text
g(U)=G_A(U)O,
O=[O-Lg(U)]+Lg(U),
G_A(U)[O-Lg(U)]=0,              E_H g=0.                          (0.2)
```

Thus the advertised identity is exactly

```text
O=[O-Lg(U)]+Lg(U).                                                  (0.3)
```

It is not an interchange of Haar and correlated-Gaussian atoms.  On the
globally centered subspace define the declared graph-domain norm

```text
||O||_split
 =||O-Lg||_(correlated-Gaussian marked provenance)
  +||g||_(Haar marked provenance).                                (0.4)
```

This is the **conditional split source norm** used below.  It is a genuine
norm on its declared domain because the split is unique.  No bound embedding
a generic ambient source into (0.4) is asserted.

There is also an exact law of total covariance.  For any two admissible even
balanced coefficients `O,F`, with `g_O=G_AO` and `g_F=G_AF`,

```text
Cov_E(O,F)
 =E_H[Cov_(G_A(U))(O,F)]+Cov_(E_H)(g_O,g_F).                       (0.5)
```

The first term is the fixed-background cross-Wick arm.  The second is a Haar
marked covariance only when `g_O,g_F` have the required canonical Haar
provenance.  Equation (0.5) therefore exposes rather than erases the missing
provenance-evaluation estimate.

For the pointwise arm, represent `G_A` by the normalized onsite-product bond
system.  Atomize only the one hidden Haar link carried by each nearest-
neighbor Gaussian bond; the two Grassmann endpoint sites remain reference
support and are not charged as future Gaussian atoms.  With

```text
C_*=3+2sqrt(2),
K_G^tag
 =8[exp(C_* 9/m)-1]exp[2Theta+4c+Lambda],                          (0.6)
```

the `C_*` charge occurs inside the exponential because re-Hoeffding is
applied to the bond potential before exponentiation.  It is neither an
external factor `C_*[exp(9/m)-1]` nor the `C_*^3` future-provenance row which
would additionally atomize two Gaussian endpoint coordinates.

Now let `{r_a}` be a finite residual factor family in the same decorated
coefficient algebra, colored by `z`.  If `S_a` is its declared hidden support,
define the common support/overlap-weighted row

```text
v_a=||r_a||_eta exp[(Theta+2c)|S_a|+Lambda ell(S_a)],
K_R=sup_h sum_(a:h in S_a)v_a,
R_z=product_a(1+z r_a),        K_sum=K_G^tag+K_R<c,
D=sup_(n integer>=1)n exp[-(c-K_sum)n],
tau=K_sum D<1.                                                       (0.7)
```

For fixed `U`, let `B(U)=product_e(1+b_e)` be the Gaussian reference-bond
product and define the normalized finite-volume marked ratio

```text
Phi_U(z)
 =G_m^prod[O^G B(U)R_z]/G_m^prod[B(U)R_z],
O^G=O-Lg,
Phi_U(0)=G_A(U)O^G=0.                                              (0.8)
```

Admissibility of the factor family includes the common KP construction under
(0.7): it supplies an absolutely convergent denominator logarithm on
`|z|<=1`, selected continuously from `z=0`, and hence a nonzero denominator
on that branch.  Coefficientwise interpolation and normalized vacuum cancellation
force every cluster in `Phi_U(1)-Phi_U(0)` to contain at least one colored
residual vertex.  Reference Gaussian bonds may transport connectivity but do
not discharge that requirement.  The two-rooted connected envelope is

```text
H(t)=t(2-t)/(1-t)^2=sum_(n>=1)(n+1)t^n,
H'(t)=2/(1-t)^3.                                                    (0.9)
```

Coloring at least one of the vertices and applying the mean-value bound at
`t=tau` gives

```text
||Phi_U(1)||
 <=A_corr ||O^G||_(correlated-Gaussian marked provenance),
A_corr=2D K_R/(1-tau)^3.                                          (0.10)
```

The bound is uniform in the allowed fixed background and regulator whenever
the displayed rows are uniform.  In particular `A_corr=0` at `K_R=0` with
`K_G^tag` fixed.  This is the load-bearing improvement over inserting
`K_G^tag+K_R` into an uncolored marked estimate, which would leave a false
nonzero response when the physical residual is removed.

At

```text
m=25000, c=0.2, Theta=10^(-6), Lambda=1, beta=0,
eta=m^(-1/2),                                                        (0.11)
```

reusing the scalar determinant/Schur series only as an arithmetic
compatibility diagnostic gives

```text
K_G^tag =0.10165541081452999,
K_I      =3.067847158922814 10^(-10),
K_S      =4.2483819339334975 10^(-6),
K_R      =4.248688718649390 10^(-6),
K_sum    =0.10165965950324864<c,
D        =3.740359343746328,
tau      =0.3802436573050462,
A_corr   =1.3351660987564906 10^(-4).                              (0.12)
```

The familiar geometric conversion then has the scalar value

```text
68exp(1/2)A_corr=0.014968953879175233,
q_arith=max{exp(-1/2),68exp(1/2)A_corr}
       =0.6065306597126334<1.                                     (0.13)
```

Equation (0.13) is arithmetic compatibility only.  It is not a full combined
contraction: this theorem neither identifies the displayed `K_R` series with
the required preintegration red-factor family in the strong marked domain,
nor controls the outer Haar-normalized partition factor, nor bounds the map
`O -> g` in canonical Haar provenance.

## 1. Exact combined split and total covariance

Since `G_A(U)Lg(U)=g(U)`, the first equality in (0.2) gives

```text
G_A(U)[O-Lg(U)]=G_A(U)O-g(U)=0.                                   (1.1)
```

Applying `E_H` to the definition of `g` gives `E_Hg=EO=0`.  This proves the
split without assuming that `G_A(U)` commutes with any product-Haar atom
projection.  Conversely, adding the two arms reconstructs `O` exactly.

For (0.5), expand the two right-hand covariances:

```text
E_H[G_A(OF)-g_O g_F]
 +E_H[g_Og_F]-E_H[g_O]E_H[g_F]
 =E[OF]-E[O]E[F].                                                  (1.2)
```

No positivity or probability interpretation is used.  These are normalized
coefficient functionals in the finite algebra.  The identity remains true
for Grassmann-valued external coefficients because the even balanced sector
is commutative.

A gauge-only scalar factor `F(U)` has zero first covariance in (0.5), because
`G_A(U)F=F`.  It acts through the Haar arm.  A factor containing eliminated
Grassmann variables can act through the pointwise cross-Wick arm.  This
separation prevents scalar determinant/Wilson factors from being mislabeled
as Gaussian attachments.

## 2. Tagged Gaussian reference bonds

For an eliminated nearest-neighbor bond `e={x,y}`, write

```text
H_e=bar zeta_x M_xy(U_e)zeta_y+bar zeta_y M_yx(U_e)zeta_x,
b_e=exp(-H_e)-1.                                                    (2.1)
```

The onsite-product identity is

```text
G_A(U)[F]
 =G_m^prod[F product_e(1+b_e)]
  /G_m^prod[product_e(1+b_e)].                                    (2.2)
```

In the `eta=m^(-1/2)` coefficient norm, `||H_e||<=9/m`.  Each `H_e`
depends on one hidden Haar link.  Applying the one-coordinate Hoeffding
projective bound to the potential and then exponentiating gives

```text
||b_e||_(one-Haar-tag)<=exp(C_* 9/m)-1.                            (2.3)
```

Charging the two endpoint sites, their full marked site allowance, and the
bond diameter gives (0.6).  Normalized Haar and onsite Gaussian evaluations
are contractive on the decorated coefficient algebra.  This proves the
factor-row estimate needed inside the fixed-`U` colored majorant.

It does not by itself prove that `g(U)=G_A(U)O` has a bounded canonical Haar
atom expansion.  That further statement must expand the normalized bond
ratio, evaluate/fuse its product coordinates, re-Hoeffding the resulting
`U`-function, and control empty as well as nonempty Haar atoms.  Global
centering removes only the total Haar mean of `g`; it supplies no tag-density
bound.

## 3. Residual-colored normalized interpolation

Work first with finite bond and residual families.  Expand the numerator and
denominator in (0.8) on their common absolutely convergent branch.  The
normalized connected expansion cancels vacuum components.  At `z=0`, all
remaining reference-only marked components sum to `G_A(U)O^G=0`.

Differentiate by coloring only the residual factors.  Every monomial of the
derivative has one distinguished red occurrence; integrating `z` from zero
to one reconstructs the difference.  Gaussian reference bonds remain
uncolored.  Hence every survivor has at least one residual occurrence even
when arbitrarily many reference bonds dress its connecting path.

To connect this envelope to the prior K-retaining marked recursion, freeze
`D` at the total row `K_sum` and write

```text
a_0(K,c)=sup_(n>=1)exp(-cn)[exp(Kn)-1]
        <=K sup_(n>=1)n exp[-(c-K)n]
        <=KD.                                                       (3.1)
```

The prior two-layer marked-path bound is therefore no larger than

```text
[tau+tau/(1-tau)]/(1-tau)
 =tau(2-tau)/(1-tau)^2=H(tau).                                    (3.2)
```

The connected series has nonnegative norm majorants.  Its color-preserving
subtraction removes the all-reference series coefficientwise, so the red
part is bounded by the same frozen-`D` envelope at the total row minus that
at `K_sum-K_R`.  Consequently

```text
H(DK_sum)-H(D(K_sum-K_R))
 <=D K_R sup_(0<=s<=tau)H'(s)
 =2D K_R/(1-tau)^3.                                                (3.3)
```

This proves (0.10) for finite families.  Absolute convergence under (0.7)
permits the regulator and family limits coefficientwise.  The proof is a
colored activity interpolation, not physical time and not an RG trajectory.

The theorem is fixed `U`.  For a globally normalized perturbed functional,
one instead encounters schematically

```text
E_R[O^G]
 =E_H[Z_R(U) Phi_U(1)]/E_H[Z_R(U)].                                (3.4)
```

The `U`-dependent coefficient `Z_R(U)` is not a positive scalar weight in the
full coefficient algebra.  A uniform bound on `Phi_U` cannot therefore be
passed through (3.4) by a probabilistic averaging shortcut.  A direct joint
Haar--Gaussian colored expansion or a controlled inverse-partition lemma is
still required.

## 4. Determinant and residual ownership

The following ownership is mandatory for any later instantiation.

| object | role here | may be counted as red? | prohibition |
|---|---|---:|---|
| `m^(3|I|)` | extracted onsite vacuum normalization | no | do not call it an interaction |
| normalized bond ratio in (2.2) | definition of the reference `G_A` | no | its `K_G^tag` bonds transport connectivity but are not physical residuals |
| `det A/m^(3|I|)` | scalar body needed to reconstruct the full Berezin integral | only in the future joint/outer-Haar red family, exactly once after an explicit factor map; not in fixed-`U` `K_R` | do not drop it or count it both as a body and as determinant loops |
| scalar Wilson/determinant factors outside the chosen quadratic center | candidate physical residuals for the joint Haar arm | only after their actual supports and marked weights are proved; not in fixed-`U` `K_R` | at fixed `U` they cancel from the Gaussian marked ratio |
| fermionic boundary/Schur factors outside the chosen quadratic center | candidate physical residuals for the fixed-`U` Gaussian arm | yes, after their actual supports and marked weights are proved | do not import their scalar row without the factor-level identification |
| newly generated Schur family after integrating a boundary source | output of that integration | no at the same step | do not insert it again as an input residual |

Indeed,

```text
integral dbar zeta dzeta exp(-bar zeta A zeta)F=det(A)G_A[F].       (4.1)
```

The Gaussian reference denominator and the physical determinant multiplier
can algebraically cancel when both are expressed relative to the onsite
product map, but their ownership remains distinct.  The numeric `K_I,K_S`
row in (0.12) reuses prior scalar formulas to test room in the inequalities;
this note does not provide the factor-level identification needed to promote
that diagnostic to an actual combined map.

## 5. Scope and next exact target

The retained result consists of:

1. the exact split (0.2)--(0.4);
2. the exact total-covariance identity (0.5);
3. the one-Haar-tag Gaussian reference-bond row (0.6); and
4. the fixed-background colored response theorem (0.7)--(0.10).

It does not prove an outer-Haar normalized colored resummation, canonical
Haar provenance for `g`, an ambient-to-split norm embedding, actual residual
factor instantiation in the required strong domain, a strong-spatial return,
future-center migration, a same-norm Hessian, an invariant ball, a critical
trajectory, or a continuum result.  The scalar `q_arith` is not promoted to
a contraction theorem.

The next exact attack is a direct joint product-Haar/Gaussian colored cluster
expansion with explicit determinant ownership.  Its two marked arms must
reconstruct (0.2), keep at least one red physical factor in every response
cluster, and prove the canonical Haar provenance evaluation of `g`.  Only
after that theorem can the actual future `S^(2)` factor grammar and the weak-
to-strong spatial handoff be composed.

No probability rule, physical time law, Born rule, or axiom choice is made in
this construction.  No axiom-update stop is established.

## 6. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_combined_reference_split_residual_interpolation_2026_07_12.py
```

The runner checks a finite exact combined-reference split, the finite total-
covariance identity, pointwise normalized residual cancellation, the
coefficient derivative `H'(t)=2/(1-t)^3`, the scalar compatibility row, the
distinguished-red prefactor at a fixed total envelope, and the
source/dependency contract.  The infinite colored
tree estimate and provenance boundaries are analytic statements.

## 7. No-Go Discipline N1--N8

This is a bounded positive supplier with named walls.  The following audit is
included so those walls cannot be silently upgraded into a global no-go or a
full RG theorem.

### N1 — alternative-route enumeration

| route | disposition | exact residual |
|---|---|---|
| Treat combined centering as pointwise `G_A` centering | `RULED OUT BY PRIOR` | `E_HG_AO=0` does not imply `G_A(U)O=0`. |
| Exact split `O=(O-Lg)+Lg` | `ATTEMPTED` | Section 1 closes the algebraic split; the two provenance maps remain separate. |
| Fixed-background direct cross-Wick attachment | `ATTEMPTED` | Supplies all-degree locality for the first arm, but not exponential physical-factor resummation. |
| Product-Haar K-retaining marked attachment | `ATTEMPTED` | Applies to the second arm only after `g` is in the required Haar marked norm. |
| Normalized product-Gaussian bond polymer | `ATTEMPTED` | Section 2 supplies reference transport and normalized cancellation. |
| Generic complex-source Cauchy disk | `ATTEMPTED` | It loses forced `O(K_R)` attachment and remains spatially unlocalized. |
| Move or invert the determinant through the reference normalization | `RULED OUT BY PRIOR` | Equation (4.1) and the retained-Grassmann body forbid the shortcut. |
| Fixed-`U` residual-colored interpolation | `ATTEMPTED` | Section 3 proves the abstract `O(K_R)` bound. |
| Direct joint outer-Haar colored expansion | `LIVE` | Needed to control (3.4), canonical `g` provenance, and actual factor ownership together. |
| Future-center factor grammar plus strong return | `LIVE` | Must follow the joint theorem; it is not licensed by the present fixed center. |

### N2 — wall-independence audit

Keep six walls:

```text
W1 strong-spatial tag-density/empty-atom handoff,
W2 outer-Haar combined provenance and actual red-factor resummation,
W3 future-center migration/update/gap/normalization,
W4 generic generated-factor domain, same-norm Hessian, and invariant ball,
W5 physical taste/chart selection,
W6 critical trajectory and observables.                            (N2.1)
```

All fifteen pairs remain independent.

| pair | why neither wall absorbs the other |
|---|---|
| W1--W2 | Weak future atoms do not put `g` in Haar provenance or control outer normalization. |
| W1--W3 | A center migration changes the atom carriers but does not prove strong spatial return. |
| W1--W4 | A generic same-norm map requires strong return in addition to factor grammar. |
| W1--W5 | Taste assignment needs correct future carriers, not merely a weight downshift. |
| W1--W6 | Critical iteration cannot use a one-step weak codomain as its own domain. |
| W2--W3 | The reference split and determinant ownership change when `A` changes. |
| W2--W4 | A conditional split domain is not a generic embedding or a Hessian bound. |
| W2--W5 | Combined response control assigns no physical taste carrier. |
| W2--W6 | Massive colored response supplies no critical tuning trajectory. |
| W3--W4 | Ball invariance needs both center update and nonlinear same-norm control. |
| W3--W5 | The quadratic form and normalization affect the physical field chart. |
| W3--W6 | A persistent gap/normalization trajectory is needed for iteration. |
| W4--W5 | Nonlinear closure must separately preserve the required symmetry/taste sector. |
| W4--W6 | Autonomous local dynamics is a prerequisite, not a critical trajectory. |
| W5--W6 | A physical chart is required before continuum observables can be identified. |

### N3 — hidden-condition phrase scan

| phrase | meaning in this note |
|---|---|
| `combined reference` | `E_HG_A`, not the full physical measure and not a probability postulate. |
| `combined centered` | `EO=0`, not pointwise Gaussian or coordinatewise Haar centering. |
| `conditional split source norm` | The graph domain (0.4), not an ambient norm equivalence. |
| `fixed-U` | The background is held fixed before outer Haar averaging. |
| `interpolation` | Auxiliary activity color `z`, not time or RG flow. |
| `colored` / `red` | Combinatorial provenance requiring at least one residual factor, not a physical charge. |
| `residual` | The abstract family and common weighted overlap row in (0.7); the numeric prior row is diagnostic only. |
| `O(K_R)` | The response vanishes at `K_R=0` with reference rows fixed. |
| `attachment` | At least one red factor; a Gaussian reference bond alone does not qualify. |
| `contraction` | Not claimed; (0.13) is scalar arithmetic only. |
| `uniform` | Uniform only in the fixed-center allowed background/regulator wedge. |
| `selected branch` | The denominator logarithm continuously selected from `z=0` by the common KP construction on `|z|<=1`; no arbitrary inverse is assumed. |

### N4 — citation/residual matching

| dependency | load-bearing use | residual matched? |
|---|---|---:|
| [Fixed-background correlated Berezin theorem](WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact normalized `G_A`, bond representation, cross-Wick arm, and combined-centering boundary | Yes |
| [K-retaining attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Rooted marked-tree activity and forced-attachment mechanism | Yes |
| [Retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Determinant/Schur ownership and simultaneous factor algebra | Yes |
| [Two-horizon intertwining theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md) | `C_*` atom cost, actual future-coordinate boundary, and weak-spatial limitation | Yes |

### N5 — rhetoric and resolution audit

The positive theorem is confined to the original fixed center, one combined-
centered mark already in the declared split domain, and a fixed-background
abstract residual family.  It proves exact algebraic splitting and a pointwise
colored response, not the global normalized response.  Reference bonds do not
count as red.  The determinant is neither discarded nor automatically placed
in `K_R`.  The selected nonzero denominator branch is part of the declared
factor-family admissibility.  The current residual arithmetic is not an
instantiation theorem.

### N6 — partial-closure and primitive scan

The exact split and total-covariance law are meaningful partial closure: they
reduce the combined-reference problem to two named marked arms.  The colored
bound closes the fixed-background first-arm resummation in the abstract
factor grammar.  Outer normalization, factor identification, provenance,
center migration, and spatial return are constructive analysis/chart
problems.  No new physical primitive is required by any result here.  No
axiom-update stop is established.

### N7 — hostile steelman

A hostile reviewer should object that the split is tautological unless its
two norm maps are bounded; correct, so (0.4) is a declared conditional domain.
They should object that `E_Hg=0` is not coordinatewise centering; correct, so
no tag-density claim is made.  They should reject any response surviving at
`K_R=0`; (0.10) vanishes exactly.  They should demand explicit determinant
ownership; Section 4 supplies it.  They should reject replacing the original
`A` by future `S^(2)`; the theorem does not.  They should reject one mark as a
Hessian and half-weight arithmetic as same-norm contraction; neither upgrade
is made.  Finally, they should note that a direct joint expansion may still
close W2; therefore no negative theorem is licensed.

### N8 — cross-cycle echo

The result preserves the earlier `O(K)` forced-attachment mechanism, the
one-/two-horizon creation and erasure of atoms, the fixed-background-only
scope of correlated Berezin locality, the retained-Grassmann determinant
body, and the prior rejection of unlocalized generic Cauchy closure.  It
advances the combined-reference lane by an exact split plus an `O(K_R)`
pointwise theorem while leaving the global, center, spatial, nonlinear, and
continuum walls explicit.
