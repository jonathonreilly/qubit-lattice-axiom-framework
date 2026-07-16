# Scalar-product reference, completed joint outer-Haar expansion, and actual-output atom return

**Date:** 2026-07-13
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_scalar_product_reference_completed_joint_atom_return_2026_07_13.py`](../scripts/wilson_staggered_scalar_product_reference_completed_joint_atom_return_2026_07_13.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_scalar_product_reference_completed_joint_atom_return_2026_07_13.txt`](../logs/runner-cache/wilson_staggered_scalar_product_reference_completed_joint_atom_return_2026_07_13.txt)

## 0. Result and exact scope

One finite-regulator Wilson--staggered `SU(3)` factor-two step now closes in
the order required by the actual generated orbit.  The current actual-hidden
Haar step is completed first with the Block42 physical residual, the actual
`P_0` quadratic split, the external shortest center, both separately owned
Schur-tail arms, the scalar Gaussian product reference, the full determinant
counterterm/restore, and the boundary source in one factor graph.  Only the
resulting physical output is projected and freshly atomized.  The conservative
witness at `m=10^64` has

```text
K_T=4.808231265303741 10^(-7)<0.01,
q=max(q_centered,q_raw)=0.9048374180359595<1,
B_out=3.613463806021122 10^(-5),
K_out,total^fac=3.613529092410874 10^(-5)<0.01,
theta_atom=0.427240686481831...>0.400001.                 (0.1)
```

Thus this theorem supplies one actual completed joint output and one strict
fresh site-block atom-factor return.  It does not supply a same-domain
invariant ball, an all-horizon recursion, a taste selector, a continuum
trajectory, a dynamics/admissibility law, time, or a probability rule.

The four direct inputs are the exact common joint colored expansion from the
[joint product-reference theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the actual generated-base row from the
[enhanced-moment factor-return theorem](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the actual-hidden support and `68`-root map from the
[site-block marked-response theorem](WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the shortest-center, tail, and actual-`P_0` split from the
[external-shortest conditional-reference theorem](WILSON_STAGGERED_EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE_BOUNDED_THEOREM_NOTE_2026-07-12.md).

The result is conditional on the supplied four-dimensional Euclidean
Wilson--staggered `SU(3)` action, the factor-two bipartite chart, finite
regulator, `beta=0` independent Haar base, the actual bare orbit already
constructed in Blocks 39--45, fixed `m=10^64`, external retained background
`W`, scalar onsite Berezin product `G_(mu')`, projective coefficient norm,
`C_*=3+2sqrt(2)`, and the displayed weights.  These are declared sector and
chart inputs, not deductions from the four framework axioms.

## 1. Phase order and ownership

The old fixed-product output is not promoted into a new center:

```text
Phi_44^out is not an input.                                      (1.1)
```

Block44 omitted the correlated center, determinant restore, boundary source,
and their mixed clusters with the residual.  It supplies only the proved
site-block support/tree incidence map.  The load-bearing order is instead:

1. start from the Block42 decorated physical residual and actual `P_0` split;
2. carry the Block45 external shortest center and its hidden-empty and
   centered tail arms as distinct owners;
3. run one completed current-hidden joint expansion under the scalar product
   reference;
4. evaluate the current Haar and Gaussian variables completely;
5. extract the physical output vacuum, one Hermitian onsite quadratic, and
   its disjoint residual complement;
6. pay the new gap/Grassmann-weight migration and fresh site-block Hoeffding
   atom cost once.

The hidden-empty tail is factored and reattached outside the normalized joint
ratio.  The centered tail is a current red factor.  Neither tail enters the
shortest reference hopping or its boundary source.  The retained `Q_K` row is
external center data when it is current-hidden independent; otherwise it must
be an explicitly atomized outer-Haar factor.  Higher, offsite, and
anti-Hermitian projected pieces remain residual unless a separate theorem
moves them.

This phase order prevents three double counts: old `Phi_44^out` is not an
actual input; the full determinant is not inserted in addition to its
product-Gaussian factor; and the Schur output is not inserted before the
boundary Gaussian integration that generates it.

## 2. Scalar product reference and full determinant

After the current shortest center and actual onsite quadratic have been
identified, let the next eliminated set be `I` and write

```text
A_3=mu'I+Q_I(W)+R_(II)(W),
B_Q=exp[-bar chi Q_I chi],
B_R=exp[-bar chi R_(II) chi],
Z_A=G_(mu')[B_QB_R]=det A_3/(mu')^(3|I|)>0.               (2.1)
```

Here `Q_I` is the actual Hermitian onsite quadratic, `R_(II)` is only the
external shortest nearest-neighbor internal hopping, and `G_(mu')` is the
fixed scalar onsite product.  A `W`-dependent onsite product covariance is
not used.  The scalar vacuum `(mu')^(3|I|)` is owned once and is never a
polymer activity.

Onsite `Q_I` preserves lattice parity but does not change it.  Consequently
closed words still contain an even number of hopping letters, while their
total length can be odd.  Pure `Q` words and mixed `QRR` words generally
survive.  With

```text
X=(Q_I+R_(II))/mu',
log Z_A=sum_(n>=1)(-1)^(n+1) Tr(X^n)/n,                  (2.2)
```

the determinant counterterm must therefore localize the full all-length
series.  Reusing the old even-total-length formula would delete actual onsite
and mixed determinant owners.  The runner includes an independent positive
three-color fixture for which `Tr X`, `Tr X^3`, and the discrepancy between
the full and even-only series are all nonzero.

Let `E_hid` average the actual new hidden site blocks at fixed retained data
and define coefficientwise

```text
psi=log Z_A,
psi_empty=E_hid psi,
psi_o=(1-E_hid)psi,
C_o=exp(-psi_o),             D_o(z)=exp(z psi_o).          (2.3)
```

At color zero,

```text
Z_A C_o=exp(psi_empty),                                      (2.4)
```

which is independent of the current hidden blocks and cancels from the outer
normalized ratio.  The baseline is therefore the intended fixed-external
`E_H G_(A_3)` reference rather than a determinant-weighted Haar average.  At
color one,

```text
C_oD_o(1)=1.                                                 (2.5)
```

The scalar Gaussian integral then produces the complete determinant and
Schur family automatically.  There is no separate `det A_3`, `det(mu'I+Q)`,
or `V_3` body.  In particular, with `J_3` owning only the shortest `K-I`
boundary source,

```text
(mu')^(3|I|)G_(mu')[B_QB_RJ_3]
 =det A_3 exp[bar psi_K R_(KI) A_3^(-1)R_(IK) psi_K].       (2.6)
```

The hidden-empty part of `psi` is not discarded at color one: it is restored
inside the full determinant supplied by (2.6).  It merely cancels from the
normalized reference at color zero.

## 3. One completed joint graph

Use the independent product `E_H G_(mu')` and one common overlap graph.  The
blue/reference factors are

```text
{B_Q, B_R, C_o},                                               (3.1)
```

and the red/physical factors are

```text
{D_o(z), J_3(z), R_dec(z), P_0^perp(z), E_tail^o(z)}.          (3.2)
```

The separately external `E_tail^empty` is reattached outside the normalized
ratio.  At `z=0`, (2.4) reconstructs the normalized correlated reference.  At
`z=1`, cancel `C_oD_o` first, perform the scalar Gaussian elimination second,
and only then take the outer Haar logarithm.  This includes the determinant,
boundary, center, residual, and mixed center--residual clusters in one
physical output.

Gaussian-only factors cannot be assigned a fictitious incident Haar link.
They root at their owned hidden site blocks.  A factor-two cell has at most
`2^4=16` such owners, whereas the inherited Haar/skeleton carrier bound is
`64+4=68`.  Hence

```text
68K_Haar+16K_Gauss<=68K_T.                                    (3.3)
```

This mixed incidence estimate is the only use made of the Block44 support
map.  Every pulled-back coefficient is freshly Hoeffding-decomposed relative
to the actual new product hidden set.  Old empty/centered tags are provenance,
not permanent next-horizon atom labels.

## 4. Conservative activity ledger

Set

```text
m=10^64, beta=0,
Theta=4.38, c=0.01, Lambda=0.2,
Theta+2c+Lambda=4.6,
C_*=3+2sqrt(2), eta^2=1/m.                                    (4.1)
```

The Block42 actual generated row and carried local potential are

```text
enhanced_rows(m=10^64,c_40=0.2,c_41=0.2,
              theta_dec=4.6,lambda_dec=1.0),
K_dec=4.470322166978306 10^(-7),
B_star=2.413636396219794 10^(-9).                              (4.2)
```

This is a fresh Block42 evaluation at the `4.6` joint source weight, not a
retagging of its old `0.400001` landing row.  Its diameter exponent `1.0` is
then monotonically weakened to the present joint value `0.2`.

For `mu=m+2/m`, `k=1/(4m)`,

```text
k'=k^2/mu=6.25 10^(-194),
mu'=mu-8k^2/mu,
h_0=8k'/mu'=5.0 10^(-257).                                    (4.3)
```

The factor activities are charged once as follows:

```text
K_Q=expm1(B_star)=2.413636399132614 10^(-9),
K_P0=expm1(B_star)=2.413636399132614 10^(-9),

x_Q=(m/mu')B_star,
x_R=C_* h_0 exp(4.6),
B_D^full=3(x_Q+x_R)/(1-x_Q-x_R)=7.240909206136305 10^(-9),
B_D^o=2B_D^full=1.448181841227261 10^(-8),
K_D^-=K_D^+=expm1(B_D^o)=1.448181851713414 10^(-8).            (4.4)
```

The factor `3` in `B_D^full` pays the color trace and the anchored all-length
word sum.  The additional factor `2` is mandatory because `1-E_hid` has norm
at most two; both `C_o` and `D_o` own the centered potential `psi_o`.
The shortest internal reference and boundary activities are positive and
below `1.45 10^(-249)`.  The centered Schur-tail potential is below
`2.7 10^(-500)`; the runner charges it by the visible binary64 envelope
`10^(-20)`, which is larger than one ulp of the aggregate residual row and is
not numerically absorbed.  Its hidden-empty partner stays outside `K_T` and
receives a second, separate `10^(-20)` final-output factor charge.

Thus

```text
K_ref=K_Q+K_G+K_D^-=1.689545491626676 10^(-8),
K_R=K_dec+K_P0+K_J+K_D^++K_tail^o
   =4.639276716141073 10^(-7),
K_T=K_ref+K_R
   =4.808231265303741 10^(-7)<c.                               (4.5)
```

For the integer path resolvent

```text
D=sup_(n integer>=1)n exp[-(c-K_T)n]
 =36.78971300910101,
tau=K_TD=1.768934483319112 10^(-5),
A_joint=2D K_R/(1-tau)^3
       =3.413734336099627 10^(-5).                             (4.6)
```

The actual site-block conversion gives

```text
C_map=68exp(Lambda/2)=75.15162242914404,
B_out=C_map K_T=3.613463806021122 10^(-5),
q_centered=C_map A_joint=0.002565476738999639,
q_raw=exp(-Lambda/2)=0.9048374180359595,
q=max(q_centered,q_raw)<1.                                     (4.7)
```

Here `B_out` is the ordinary retained-coefficient potential row for the
completed physical joint output.  In contrast, `A_joint` controls a centered
marked response.  They have distinct roles and are not substituted for one
another.

## 5. Actual quadratic projection and fresh atom return

After (and only after) the completed joint evaluation, remove the scalar
vacuum and let `P_(0,2)^sa` extract the Hermitian onsite quadratic from the
physical output.  Pair projection and Hermitian symmetrization are contractive
in the projective coefficient norm.  The complementary monomials and the
anti-Hermitian part remain a disjoint residual row bounded by
`B_out,total<=B_out+10^(-20)` after the external tail is reattached.
The already separated actual `P_0` row is carried as a disjoint center account;
the Block44 surrogate is not added.

At the weak weights

```text
(theta_w,lambda_w)=(Theta/2,Lambda/2)=(2.19,0.1),              (5.1)
```

a deliberately conservative Weyl charge is

```text
epsilon_Q<=B_star+exp(-theta_w)B_out+10^(-20)
          =4.046484840559054 10^(-6),
gap_out/m>=1-epsilon_Q
         =0.9999959535151595.                                  (5.2)
```

This is a finite-regulator quadratic-kernel gap, not a pole-mass or continuum
mass claim.  Moving the three-pair Grassmann coefficient weight from
`m^(-1/2)` to `gap_out^(-1/2)` costs

```text
sigma_eta=3log(m/gap_out)=1.213947908245705 10^(-5).            (5.3)
```

Fresh site-block Hoeffding atomization costs `log C_*`.  Therefore

```text
theta_atom=theta_w-log C_*-sigma_eta
          =0.427240686481831>0.400001,
lambda_atom=0.1,
K_out,total^fac
 <=expm1(B_out+10^(-20))
 =3.613529092410874 10^(-5)<0.01.                              (5.4)
```

Equation (5.4) is the positive theorem: one actual generated physical output
returns to the displayed fresh site-block factor domain with strict spatial,
diameter, gap, and activity margins.  The added `10^(-20)` is the separately
reattached hidden-empty Schur-tail factor; it is not part of the normalized
joint graph or silently dropped from the physical output.

## 6. Sharp next-certificate boundary

The theorem does not silently iterate (5.4).  As a falsifiable diagnostic,
reuse the same scalar all-length determinant majorant at source
`(Theta,c,Lambda)=(0.280001,0.01,0.1)` and bound the next `Q` and residual
accounts separately by `B_out`.  The centered determinant again pays the
factor two in (4.4).  Then

```text
K_T^next=0.0005059489201110645<c,
tau_next=0.01960462334917195<1,
q_next=1.487230817637235>1,
B_out^next=0.03616848436496884,
expm1(B_out^next)=0.03683052150750240>c.                        (6.1)
```

Thus its KP logarithm remains convergent, but the unchanged certificate misses
both the next marked-response contraction and the next factor return.
Moreover, literal repeated atomization would pay a fixed positive spatial
surcharge while the spatial exponent is halved.  If `a_j` is the available
spatial reserve and `chi>0` the fixed surcharge, then

```text
a_(j+1)=a_j/2-chi,
a_j=2^(-j)(a_0+2chi)-2chi,
a_*=-2chi<0.                                                    (6.2)
```

Every finite positive `a_0` is exhausted after finitely many literal reuses.
Simultaneously `Lambda_j=Lambda_0/2^j` tends to zero, so the raw-arm factor
`exp(-Lambda_j/2)` tends to one.

**NG46:** the displayed fixed-`m`, unchanged scalar-product-reference
certificate--literal repetition of the same positive per-horizon atom
surcharge and strong-to-weak halving map--has no admissible positive fixed
point and exhausts every finite initial spatial moment.  Therefore that
unchanged certificate alone cannot establish horizon-uniform actual-range
contraction.

`NG46` is not a no-go for an RG action, a scale-indexed norm, a varying-mass
schedule, a lineage estimate, another reference block, or a continuum
trajectory.  Those alternatives remain live.

## 7. Runner contract

Run

```bash
python3 scripts/wilson_staggered_scalar_product_reference_completed_joint_atom_return_2026_07_13.py
```

The runner independently checks a positive hidden-dependent `3x3` scalar
reference, exact hidden-empty/centered determinant normalization, full versus
even-only trace-log series, a finite determinant--Schur identity, mixed
`16/68` root incidence, the complete conservative joint ledger, the actual
quadratic gap and atom return, the next-response/factor-return separation, the
closed form of (6.2), the source contract, and exactly four direct science
dependencies.  It is a finite-dimensional algebra and arithmetic verifier;
the localization and cluster inequalities are analytic content of Sections
2--5.

## 8. No-Go Discipline N1--N8

### N1 — alternative-route enumeration

The negative conclusion is restricted to literal reuse of (6.2).  Six closed
attacks were executed before retaining `NG46`:

| route | status | effect on `NG46` |
|---|---|---|
| Seek a positive fixed point of the unchanged recurrence | `ATTEMPTED` | The unique fixed point is `-2chi`; no positive solution exists. |
| Start with an arbitrarily large finite `a_0` | `ATTEMPTED` | Equation (6.2) still becomes negative at finite horizon. |
| Increase the fixed mass while retaining the same recurrence | `ATTEMPTED` | It reduces activity but does not remove fixed `chi` or halving. |
| Omit the fresh atom surcharge | `ATTEMPTED` | Every new actual hidden product requires fresh atomization; omission changes the certificate under test. |
| Reuse an earlier horizon's atom surcharge | `ATTEMPTED` | The hidden product and site blocks change, so an earlier charge does not bound the new Hoeffding decomposition. |
| Use the base-gap and tiny `eta` migration gain | `ATTEMPTED` | The fixed `log C_*` surcharge remains positive. |

The following routes are deliberately not closed by `NG46`:

| live route | why it lies outside the claim |
|---|---|
| Feed shortest-center squaring into the aggregate scalar row | A sharper scale-dependent ledger changes the recurrence. |
| Scale-index the spatial/diameter norm | It is not literal unchanged reuse. |
| Retain atom lineage instead of re-Hoeffding every horizon | It can replace the fixed surcharge and defeats any broader no-go. |
| Split small and large polymers with distinct carriers | It changes the scalar majorant. |
| Choose a varying mass schedule `m_j` | It changes the per-horizon activities and potentially the chart. |
| Sharpen determinant/path carriers or choose alternate blocks | Both alter (6.1)--(6.2). |

The live routes are why the result is a certificate boundary rather than a
foundational impossibility.

### N2 — wall-independence audit

The residual set is kept atomic:

| wall | exact unresolved target |
|---|---|
| `W1` | A horizon-uniform scale-indexed or lineage-preserving recursion. |
| `W2` | Embedding of a generic generated source, not only the actual bare orbit. |
| `W3` | A same-domain two-mark Hessian/covariance bound. |
| `W4` | An invariant ball or self-map for the nonlinear transformation. |
| `W5` | Physical taste/chart selection rather than a declared Wilson--staggered sector. |
| `W6` | Critical continuum control and observable reconstruction. |

No pair is automatically equivalent.  The full bidirectional audit is:

| pair | close first => second? | close second => first? | independent? | pair-specific reason |
|---|---:|---:|---:|---|
| `W1-W2` | No | No | Yes | Uniform control on the actual orbit does not embed generic sources; generic embedding has no horizon estimate. |
| `W1-W3` | No | No | Yes | A recursion may use one-mark bounds; a one-horizon Hessian has no scale transport. |
| `W1-W4` | No | No | Yes | Scale-indexed transport need not be a same-domain self-map; one invariant ball need not persist across scale charts. |
| `W1-W5` | No | No | Yes | Norm recursion does not select a taste, and taste selection supplies no activity recursion. |
| `W1-W6` | No | No | Yes | Finite-regulator recursion lacks critical convergence; continuum control alone does not pay atom surcharges. |
| `W2-W3` | No | No | Yes | Generic source membership supplies no second derivative; a Hessian on one chart supplies no generic embedding. |
| `W2-W4` | No | No | Yes | Embedding a domain does not show it maps into itself; a ball on the actual orbit need not contain generic sources. |
| `W2-W5` | No | No | Yes | Source-genericity and physical taste selection are different semantic tasks. |
| `W2-W6` | No | No | Yes | A finite generic-source chart need not have a critical limit; a continuum limit need not control every generated source. |
| `W3-W4` | No | No | Yes | A Hessian bound still needs value and first-derivative margins; a self-map may be proved without the displayed Hessian route. |
| `W3-W5` | No | No | Yes | Two-mark covariance control is taste-blind; a taste selector gives no covariance estimate. |
| `W3-W6` | No | No | Yes | A finite-chart Hessian has no uniform critical scaling; continuum convergence need not use this two-mark norm. |
| `W4-W5` | No | No | Yes | An invariant mathematical ball does not identify the physical sector; sector selection does not prove self-mapping. |
| `W4-W6` | No | No | Yes | A fixed-regulator ball can shrink or drift at criticality; a continuum construction can use changing domains. |
| `W5-W6` | No | No | Yes | Selecting one taste does not prove convergence/observables; continuum control does not by itself select the taste chart. |

### N3 — hidden-condition phrase scan

The note before this subsection and the runner were scanned literally.  The
mandatory hidden-premise phrases classify as follows:

| phrase | pre-table hit | classification |
|---|---:|---|
| `we assume` | 0 | absent |
| `by construction` | 0 | absent |
| `as is standard` | 0 | absent |
| `the framework provides` | 0 | absent |
| `bridge context` | 0 | absent |
| `background` | 1 note locus | explicit fixed-external model scope in Section 0, not an inferred premise |
| `naturally` | 0 | absent |
| `obviously` | 0 | absent |
| `standard QFT` | 0 | absent |
| `registered` | 0 | absent before this self-referential scan |
| `canonical` | 0 | absent before this self-referential scan |

Scope-sensitive rhetoric is also bounded explicitly:

| phrase family | permitted meaning here | excluded meaning |
|---|---|---|
| `completed` / `full` | all owners and all determinant word lengths in one displayed finite step | no completion of the TOE or continuum theory |
| `joint` | one common current-hidden Haar/Gaussian factor graph | no universal sector unification |
| `atom return` | membership in the one displayed fresh factor chart | no autonomous iteration |
| `fixed point` | fixed point of recurrence (6.2) only | no physical action/RG fixed-point claim |
| `all-horizon` | the explicitly unresolved reuse target | no negative statement about alternate multiscale routes |

All imports are disclosed in Section 0.  `Fixed`, `scalar`, `actual`, and
`external` identify the chosen finite chart; none converts a supplied model
choice into an axiom consequence.  Positivity is proved from the displayed
finite quadratic gap.  Contractivity is invoked only for the named projective
coefficient projection and conditional expectations.

### N4 — residual matching

| authority and exact source location | residual supplied | use here | match? |
|---|---|---|---:|
| Joint product-reference note, lines 30--67 and 170--194 | local counterterm/restore and joint red response | full all-length scalar-reference variant and response envelope | Yes, with onsite-`Q` correction |
| Enhanced-moment note, source runner return rows `B_star`, `K_P`, `K_decorated_bound` | actual generated-base physical row | `P_0` and residual accounts in (4.2)--(4.5) | Yes |
| Site-block note, lines 92--175 and 200--258 | actual hidden blocks, support routing, conservative `68` map | (3.3), (4.7), and fresh atom provenance | Yes |
| External-shortest note, lines 30--116 and 169--285 | shortest/tail split and conditional-vs-physical warning | starting center/tail ownership and rejection of `Phi_44^out` | Yes |
| Campaign dynamics-selection ledger | law-selection nonuniqueness | not used as a witness for `NG46` | No residual match; dropped |

The first four rows are the only repository dependencies.  The fifth is
listed solely to document why it cannot support this narrow certificate
boundary.

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One finite determinant fixture | Yes | Scalar normalization and all-length words. |
| One actual generated finite-regulator horizon | Yes | Completed joint response and atom return. |
| One literal next reuse of the same certificate | Yes | Marked-response and factor-return certificates both miss. |
| Arbitrary generated source | No | Remains `W2`. |
| Same-domain nonlinear ball | No | Remains `W3-W4`. |
| All horizons or critical continuum | No | Remains `W1,W6`. |

The language `actual` means the displayed constructed bare-orbit row, not a
generic physical theory.  `Return` means membership in one declared factor
chart, not an autonomous flow theorem.

### N6 — partial-closure and primitive scan

This block retires a real ownership/phase-order residual for one horizon:
the old fixed-product output is replaced by a completed joint physical output,
and the new output is projected and atomized exactly once.  The remaining
all-horizon failure has multiple live quantitative and organizational routes
listed in N1.  The Lattice, Qubit, Admissibility, and Record axioms and the
approved primitive registry neither provide nor obstruct those routes.

No axiom-update stop is triggered by failure of one unchanged scalar
certificate.

### N7 — hostile steelman

The strongest attack uses the exact shortest-center recursion
`h_(j+1)=h_j^2/(8-h_j^2)` established at
`docs/WILSON_STAGGERED_BLOCK_SATURATED_PRODUCT_REFERENCE_SPLIT_HANDOFF_SCALAR_NEXT_ACTIVITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md:230-268`,
together with scale-indexed or lineage-preserving norms.  At
`m=10^64`, the fresh shortest hopping and tail activities are effectively
zero compared with the actual output; a ledger that tracks their improving
scale separately need not pay a fixed aggregate surcharge at every horizon.
Block46 itself proves that careful ownership and a fresh atom charge close one
previously open physical step.  This directly defeats any claim that the
framework, the action, or every multiscale construction must fail.

It does not defeat `NG46`, because every such route changes the unchanged
recurrence whose literal reuse is the only subject of the negative claim.

### N8 — cross-cycle echo

| prior wall or path | retirement mechanism | status after this block |
|---|---|---|
| Block42 enhanced local moment | weak retag was insufficient by itself | its actual `P_0` and residual rows are now owned in one completed joint graph |
| Block44 site-block output | lacked correlated center/determinant/mixed clusters | support/`68` map retained; `Phi_44^out` demoted from physical input |
| Block45 conditional Weyl budget | did not produce actual joint output | its phase-order warning is retired for one horizon by Sections 1--5 |
| Block45 external shortest/tail split | shortest and tail owners were separated | mechanism retained unchanged at the start of the completed step |
| `docs/WILSON_STAGGERED_BLOCK_SATURATED_PRODUCT_REFERENCE_SPLIT_HANDOFF_SCALAR_NEXT_ACTIVITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md:250-268,300-324` | fixed-ledger all-horizon boundary with shortest-center and adapted-chart escapes | the same narrow unchanged-ledger residual persists; shortest-center, scale-indexed, and adapted-chart routes remain live |
| Unchanged all-horizon atom surcharge | no positive fixed point under literal halving | remains the narrow `NG46` boundary |
| Campaign dynamics-selection no-go | concerns selecting a physical law | residual mismatch; not echoed into `NG46` |

Earlier negative boundaries were partially retired by explicit ownership,
site-block, and phase-order mechanisms.  That history is positive evidence for
keeping scale-indexed and lineage routes live.

**No-Go Discipline status:** `PASS` for the narrow unchanged-certificate
boundary.

## 9. Claim-strength disposition

`PASS WITH BOUNDED CLAIMS` is the intended review disposition.  The bounded
candidate content is one finite-regulator, ultra-massive, actual-bare-orbit,
scalar-product-reference, completed joint outer-Haar atom return plus a sharp
diagnostic showing why the same certificate cannot simply be repeated.

No axiom-update stop is triggered.
