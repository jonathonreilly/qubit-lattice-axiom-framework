# Joint-boundary canonical future atoms and superstrong-to-strong coarse shadow

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_joint_boundary_future_atom_superstrong_coarse_shadow_2026_07_12.py`](../scripts/wilson_staggered_joint_boundary_future_atom_superstrong_coarse_shadow_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_joint_boundary_future_atom_superstrong_coarse_shadow_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_joint_boundary_future_atom_superstrong_coarse_shadow_2026_07_12.txt)

## 0. Result

The actual original-center preintegration factor grammar now has a canonical
future-atom coarse shadow in a strict massive wedge.  Measuring the input in
a genuinely stronger shadow norm pays the full next strong spatial weights
for both empty and nonempty future atoms.  This closes one bare-range spatial
handoff without asserting a universal tag-density law or a same-norm RG map.

Use the exact determinant-counterterm and boundary-source grammar from the
[joint outer-Haar theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the evaluated future-atom intertwining from the
[two-horizon theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the product-coordinate atom algebra from the
[one-horizon theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the support dilation and raw-lift suppression from the
[declared RG-chart theorem](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the exact limitation of weak support retagging from the
[current-chart handoff boundary](WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Keep the target next product-coordinate strong weights

```text
theta_s=Theta+2c_s,                 lambda_s=Lambda.               (0.1)
```

Let `c_h>0` be the current joint KP margin and measure every input
factor/mark in the future-decorated shadow-superstrong row

```text
theta_h=2(Theta+2c_s),              lambda_h=Lambda,
a_s=theta_h+2c_h,
L_s=a_s+lambda_h.                                                  (0.2)
```

The two copies of `c_h` in `a_s` pay the standard factor-to-polymer and
hard-core layers.  The doubled `theta_h` pays the coarse size inequality,
while the unchanged `lambda_h=Lambda` pays diameter with one additive
`exp(Lambda)` constant.

After substituting the next skeleton into every full primitive coefficient,
use the safe current/future coordinate counts

```text
Gaussian I-I reference bond:       (current Haar,future Haar,future G)=(1,0,0),
determinant word of length r:       (r,0,0),
grouped K-I/I-K boundary source:    (1,<=1,<=1),
Wilson plaquette:                   (4,2,0).                       (0.3)
```

Current onsite Gaussian sites are overlap coordinates and are evaluated
contractively; they are not charged again as canonical future atoms.  A
future Gaussian coordinate means an endpoint in the actual next eliminated
set `I_1`; an endpoint in `K_1` remains an external coefficient variable.
The boundary row pays the worst case `<=1`, whether or not that endpoint is
actually eliminated.  With
`C_*=3+2sqrt(2)`, `h=4/m`, and `g(x)=(exp(x)-1)/x`, define

```text
K_G^s
 =8[exp(9C_*/m)-1]exp(2a_s+lambda_h),

K_D^(-,s)
 =(3/2)sum_(even r>=4)
   C_*^r h^r g(3C_*^r h^r/r)exp(rL_s),

K_B^s
 =8[exp(9C_*^3/m)-1]exp(2a_s+lambda_h),

K_D^(+,s)=K_D^(-,s),

K_W^s
 =12[exp((3beta/4)C_*^6)-1]exp(4L_s).                             (0.4)
```

The uncolored and physical-red rows are

```text
K_ref=K_G^s+K_D^(-,s),
K_R=K_B^s+K_D^(+,s)+K_W^s,
K_T=K_ref+K_R<c_h.                                                 (0.5)
```

For a connected preintegration factor collection `Gamma`, evaluate all
current hidden Gaussian and Haar coordinates, substitute the next skeleton,
and only then take canonical future projections.  The actual surviving
coarse carrier is contained in a declared connected shadow `X(Gamma)`.  If
`Y(Gamma)` is its connected fine carrier,

```text
|X(Gamma)|<=2|Y(Gamma)|,
diam X(Gamma)<=ell(Y(Gamma))+1.                                   (0.6)
```

The joint Gaussian-to-Haar rerooting lemma proved below preserves the existing
anchor multiplicity `68`.  Therefore

```text
exp[theta_s|X|+Lambda diam X]
 <=exp(Lambda)
   exp[theta_h|Y|+lambda_h ell(Y)].                               (0.7)
```

No future-tag density enters (0.7).

Let

```text
D=sup_(n integer>=1)n exp[-(c_h-K_T)n],
tau=K_TD<1,
A_joint=2D K_R/(1-tau)^3.                                        (0.8)
```

The evaluated double-decorated cluster algebra maps contractively to genuine
canonical future atoms.  Let `O^o` be a factor-rooted, future-decorated
shadow-superstrong mark satisfying the actual combined-reference condition

```text
E_H G_A[O^o]=0.                                                    (0.8a)
```

The connected noncenter/base-defect shadow, after extracting the vacuum and
the retained onsite mass center, and the centered marked response obey

```text
B_strong<=68exp(Lambda)K_T,

||response_centered||_(theta_s,Lambda,eta;future atoms)
 <=q_centered^shadow ||O^o||_shadow-superstrong,

q_centered^shadow=68exp(Lambda)A_joint.                            (0.9)
```

Canonical evaluation may fuse all future tags to the empty atom.  Equation
(0.7) applies unchanged: **empty future atoms are paid spatially**, not
reclassified as nonempty lineages.  For the extended fiber-constant raw-lift
component, after projecting the finite diameter-zero sector with `P_0`, the
exact support dilation gives `exp(-Lambda)`.  When that raw component is
already measured in the same future-atom-decorated shadow-superstrong norm,
let `L_0` lift a retained coefficient to the current joint algebra and put

```text
C_0=L_0 E_HG_A,                    Q_0=1-C_0.                      (0.9a)
```

For a source in the declared direct-sum domain, write its centered component
as `O^o=Q_0F` and identify the exact rescaled coarse lift of `C_0F` as
`L_1Phi`.  Declare the projected split source

```text
F=(1-P_0)L_1 Phi+O^o,
||F||_shadow-split
 =||(1-P_0)L_1 Phi||_shadow-superstrong
  +||O^o||_shadow-superstrong,                                    (0.9b)
```

where `L_1 Phi` is exactly constant under the next hidden fiber and `O^o`
satisfies (0.8a).  The projected split map has

```text
q_shadow=max{exp(-Lambda),68exp(Lambda)A_joint}.                   (0.10)
```

At

```text
m=2 10^9, beta=0, c_h=c_s=0.2,
Theta=10^(-6), Lambda=1, eta=m^(-1/2),                             (0.11)
```

the runner evaluates

```text
theta_s       =0.400001,
theta_h       =0.800002,
a_s           =1.200002,
K_G^s         =6.287193876629760 10^(-6),
K_D^(-,s)     =1.837433539648439 10^(-28),
K_B^s         =2.135796064442925 10^(-4),
K_D^(+,s)     =1.837433539648439 10^(-28),
K_W^s         =0,
K_R           =2.135796064442925 10^(-4),
K_T           =2.198668003209222 10^(-4)<c_h,
D             =1.841420429643656,
tau           =4.048672179113286 10^(-4),
A_joint       =7.875358564567945 10^(-4),
B_strong      =0.04064087510357815<c_s,
q_centered^shadow=0.1455706197349176,
q_shadow      =exp(-1)=0.3678794411714423<1.                      (0.12)
```

Thus the actual original-center bare range and one declared stronger-source
mark have a strict **superstrong-to-next-strong** canonical-future-atom
handoff.  This is not a same-norm result: an arbitrary next perturbation known
only at `theta_s` need not possess the input decay `a_s`.

## 1. Phase-separated evaluation and actual coarse carrier

At physical color one first use the exact identity

```text
C_A D_A(1)=1.                                                      (1.1)
```

Only then evaluate the current onsite Gaussian sites.  For fixed current
gauge background,

```text
G_m^prod[B_G J]
 =Z_A exp[bar psi_K M_KI A^(-1)M_IK psi_K].                        (1.2)
```

Together with the extracted vacuum factor `m^(3|I|)` and
`exp[-m bar psi_K psi_K]`, equation (1.2) generates
`det A exp[-bar psi S psi]` exactly once.  It is an output identity after
convergence of the joint preintegration expansion.  No post-Schur path factor
or future `S^(2)` kernel is inserted as a simultaneous input.

For a connected factor collection `Gamma`, let `R_Gamma` be the retained
`K` endpoints carrying surviving external Grassmann generators, and let
`L_Gamma` be the coarse `V` links surviving skeleton substitution and exact
coefficient cancellation.  Its actual external carrier is

```text
X_actual(Gamma)=R_Gamma union endpoints(L_Gamma).                  (1.3)
```

It may be empty for a scalar vacuum coefficient.  A grouped boundary source
contributes at most one `V` and one retained endpoint.  A fine unit plaquette
contributes at most two `V` links: among each parallel pair at most one side
can be skeleton.  Reference `I-I` bonds and eliminated determinant words
contain no skeleton link and add no `V` directly.  Algebraic cancellations
can only shrink (1.3).

Keep two fine carriers.  The spatial carrier `Y_sp(Gamma)` contains the fine
endpoint sites/links, including current Gaussian sites, and pays the
`theta_h` weight.  The Haar-root carrier contains only positive hidden-Haar
link anchors.  Define `X(Gamma)` from the coarse cells of those positive link
starts, the endpoints of skeleton/coarse-`V` links, and retained fermion
endpoints.  Do not independently project every Gaussian endpoint into `X`:
an incoming nonskeleton `I-I` bond can end in a neighboring cell from its
positive link start and would otherwise create an extra uncounted anchor.

Every Gaussian-bearing factor has an incident Haar link, and Gaussian-site
overlap makes the incident link carriers adjacent.  Therefore the routed
shadow remains connected, contains `X_actual`, and obeys

```text
|X(Gamma)|<=2|Y_sp(Gamma)|,
diam X(Gamma)<=ell(Y_sp(Gamma))+1.                                (1.4)
```

This is the `Y` used in (0.6)--(0.7).  The shadow is only an upper membership
carrier, never a genuine tag-density witness.

## 2. Gaussian-to-Haar rerooting and the factor 68

The older anchor count has 64 positive fine-link starts per `2^4` cell and
four incoming skeleton endpoints.  The joint grammar additionally contains
onsite Gaussian overlap coordinates, so importing `68` without a routing
lemma would be invalid.

Every actual base factor containing a current Gaussian site also contains a
hidden Haar link:

- an `I-I` Gaussian reference bond contains its nonskeleton link;
- a grouped boundary source contains its skeleton link.

When two factors share a Gaussian site, their incident link carriers are
geometrically adjacent.  Canonically root or reroot every nonempty connected
base collection at one such incident Haar coordinate.  Its Haar-root row is
bounded by the joint row `K_T`.  In a centered response every survivor has a
physical red factor, and every red family has Haar support.  Thus no
Gaussian-only survivor needs another coarse anchor.

The original `64+4=68` multiplicity therefore applies to this actual grammar.
This is a carrier-routing statement, not Gaussian tag creation.  A genuinely
Gaussian-only ambient source is outside the declared factor-rooted shadow
domain unless supplied with an explicit canonical incident-link anchor.

## 3. Final canonical future atoms

The current integration coordinates and the future product-reference
coordinates are distinct.  Current hidden Gaussian/Haar evaluation therefore
commutes with every future conditional expectation and complement.  Decorate
the primitive factors using (0.3), retain the full coefficient through joint
cluster multiplication, evaluate current variables, and then apply final
canonical future re-Hoeffding.  The constant-one projective atom algebra makes
this map contractive.

The counts in (0.3) are actual safe counts:

- an `I-I` bond is nonskeleton and has no external coarse `V`;
- an eliminated determinant word uses only nonskeleton `I-I` links;
- a boundary group has one current hidden Haar link, at most one future Haar
  coordinate from `V=B` or `B^(-1)W`, and at most one actual future Gaussian
  coordinate when its endpoint lies in the next eliminated set `I_1`; an
  endpoint in `K_1` remains external;
- a unit plaquette has four current links and at most two skeleton/coarse
  links, hence at most two future Haar coordinates.

The worst cases give `C_*`, `C_*^r`, `C_*^3`, and `C_*^6` respectively in (0.4).
The current Gaussian endpoint in a boundary source is integrated
contractively and is not counted twice.

The final empty atom is genuine.  It can arise from reference/determinant
outputs, Gaussian means of boundary backtracks, endpoint-balanced products,
or future-link fusion such as `V_1V_2=B B^(-1)W=W`.  A coefficient may depend
on external future-retained fields or `W` and still be empty relative to all
next hidden coordinates.  Conversely, a straight offsite bilinear can have
nonempty future link and endpoint atoms.  No Boolean tag-survival rule is
used.

Because (0.7) already pays every canonical atom, empty and nonempty sectors
both land at the next strong weights.  No claim that a nonempty atom occurs
with density proportional to support is needed or made.

## 4. Strong shadow bound and remaining iteration wall

The target shadow inequality is immediate from (0.2) and (0.6):

```text
theta_s|X|<=2theta_s|Y|=theta_h|Y|,
Lambda diam X<=Lambda ell(Y)+Lambda.                               (4.1)
```

The two hidden cluster layers spend the `2c_h` reserve included in the factor
row `a_s`.  Applying the rerooting multiplicity proves the base bound in
(0.9).  Color-preserving subtraction from the exact joint reference leaves at
least one physical red factor.  The two-root derivative envelope from the
predecessor gives `A_joint` in (0.8), and (4.1) gives the marked bound in
(0.9).

For the empty future atom, split the diameter-zero local algebra with `P_0`.
That algebra is finite-dimensional but may contain onsite quartic/sextic
coordinates as well as the quadratic center.  No physical relevance claim is
made for the whole finite jet.  The extended empty part is an exact next-
fiber-constant raw lift in the declared support chart and gains
`exp(-Lambda)`.  The raw source is required to carry the same future-atom-
decorated shadow-superstrong weights, so no uncharged atomization is hidden in
(0.10).

The theorem does not map the ordinary next strong ball back into its own
domain.  The source pays `a_s=2theta_s+2c_h`, whereas the output pays only
`theta_s`.  Iteration still requires either:

1. invariance of the enhanced-decay actual factor grammar;
2. an empty/raw plus nonempty quantitative-density decomposition; or
3. another multiscale norm/chart which carries the missing reserve.

The product-coordinate output also has not been migrated to a correlated
future `S^(2)` reference.  Choosing/extracting the generated quadratic center,
proving its next gap/counterterm ledger, and controlling a same-norm Hessian
remain separate.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_joint_boundary_future_atom_superstrong_coarse_shadow_2026_07_12.py
```

The runner checks current-evaluation/future-atom commutation and
reconstruction, explicit fusion into a genuine empty future atom, the doubled
site-weight and retained-diameter shadow inequality, the strict atom-decorated
activity/base/marked witness, a strict-domain guard, and the source/dependency
contract.  The arbitrary-regulator cluster, routing, and shadow bounds are
analytic statements.

## 6. No-Go Discipline N1--N8

The positive theorem uses a stronger actual-range row.  Its boundary language
is audited so that it cannot be mistaken for a weak-to-strong embedding of the
whole completion or a same-norm contraction.

### N1 — alternative-route enumeration

| route | disposition | exact residual |
|---|---|---|
| Support-only weak-to-strong retagging | `RULED OUT BY PRIOR` | Long centered nonskeleton loops make the norm ratio diverge on the full weak completion. |
| Optimistic parent-shadow size collapse | `ATTEMPTED` | The prior even-chain witness retains an `exp(cN)` divergence. |
| Full block/origin-cell saturation | `ATTEMPTED` | The tested saturation breaks reflection covariance. |
| Mere red or nonempty tag as strong gain | `ATTEMPTED` | One tag cannot pay unbounded support and final re-Hoeffding can erase it. |
| Formal lineage density | `RULED OUT BY PRIOR` | Exact tag creation/erasure and empty future atoms forbid Boolean survival. |
| Canonical future atoms plus quantitative tag density | `LIVE` | Still useful for a same-norm sectorwise route, but not needed for present membership. |
| Empty atom to finite jet plus extended raw lift | `ATTEMPTED` | Section 4 gives the exact classification and raw suppression for the declared source. |
| Shadow-superstrong actual-range KP | `ATTEMPTED` | Equations (0.1)--(0.12) prove next-strong base and marked membership. |
| Small/large cluster split using unused activity decay | `LIVE` | Possible route to reduce the stronger source gap. |
| Gaussian-adapted next elimination | `ATTEMPTED BY PRIOR` | Repairs coefficient contractivity, not spatial self-mapping. |
| Import predecessor factor `68` without matching | `ATTEMPTED` | Rejected and repaired by Section 2's Gaussian-to-Haar rerooting lemma. |
| Future `S^(2)` counterterm chart | `LIVE` | Waits for center ownership, gap, and strong factor grammar. |

### N2 — wall-independence audit

The actual-base spatial handoff is closed only in the stronger domain.  Keep
six iteration/physics walls:

```text
W1 enhanced-decay or sectorwise same-domain return,
W2 generic joint-source embedding and modular provenance,
W3 future-center migration/update/gap/normalization,
W4 same-norm Hessian and invariant ball,
W5 physical taste/chart selection,
W6 critical trajectory and observables.                            (N2.1)
```

All fifteen pairs remain independent.

| pair | why neither wall absorbs the other |
|---|---|
| W1--W2 | Bare-range enhanced decay does not embed arbitrary generated sources. |
| W1--W3 | Spatial return does not choose or gap the future correlated center. |
| W1--W4 | Strong membership from a stronger source is not a same-norm Hessian. |
| W1--W5 | Atom carriers do not select physical taste. |
| W1--W6 | An ultra-massive handoff supplies no critical trajectory. |
| W2--W3 | Source evaluation changes with the running reference. |
| W2--W4 | A generic one-mark embedding is not nonlinear invariance. |
| W2--W5 | Provenance control does not select a physical sector. |
| W2--W6 | Generic locality supplies no tuning path. |
| W3--W4 | A ball requires both center persistence and nonlinear control. |
| W3--W5 | Center form and normalization affect the field/taste chart. |
| W3--W6 | A persistent center/gap trajectory remains separate. |
| W4--W5 | Nonlinear closure must preserve the selected symmetry/taste sector. |
| W4--W6 | Autonomy is prerequisite, not criticality. |
| W5--W6 | Physical observables require a selected chart. |

### N3 — hidden-condition phrase scan

| phrase | meaning in this note |
|---|---|
| `coarse shadow` | Evaluated support upper carrier with proved geometry, not syntactic tag density. |
| `canonical future atom` | Post-evaluation Hoeffding coefficient, not inherited lineage. |
| `empty atom` | Independent of all next hidden product coordinates, not zero or vacuum. |
| `raw lift` | Exact next-fiber-constant lift after final canonical evaluation and local projection. |
| `superstrong-to-next-strong` | Stronger spatial domain to ordinary product-coordinate strong codomain, not same norm. |
| `tag density` | A quantitative atom-count/support inequality; not proved or assumed. |
| `base range` | Fixed original-center bare preintegration grammar only. |
| `factor 68` | Rerooted `64+4` shadow multiplicity proved for factors with incident Haar links. |
| `contraction` | Only the displayed stronger-domain projected split number; no ball self-map. |
| `uniform` | Uniform in the displayed massive original-center regulators, not center/critical uniformity. |

### N4 — citation/residual matching

| dependency | load-bearing use | residual matched? |
|---|---|---:|
| [Joint outer-Haar theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Actual `B_G,C_A,D_A,W,J` grammar, common joint KP, and explicit-red subtraction | Yes |
| [Two-horizon theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Evaluation-commuting future re-Hoeffding and atom fusion/erasure | Yes |
| [One-horizon theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Constant-one product atom algebra, `C_*` cost, and original `68` coarse-anchor conversion matched anew in Section 2 | Yes |
| [Declared RG-chart theorem](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Factor-two support geometry, `P_0`, and extended raw suppression | Yes |
| [Current-chart handoff boundary](WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact scope of the full weak-completion obstruction | Yes |

### N5 — rhetoric and resolution audit

The theorem fixes the original center, actual bare preintegration factors,
one future pullback, canonical product-coordinate atoms, a declared
factor-rooted shadow-superstrong domain, and a next strong product-coordinate
codomain.  The source and output norms differ.  The empty sector is not called
zero; the shadow is not called tag density; `68` is not imported without a
routing proof; and no future correlated center or generic perturbation ball is
claimed.

### N6 — partial-closure and primitive scan

The result closes actual-base strong membership by constructive norm
refinement.  The enhanced-decay, generic-source, center, and nonlinear walls
are mathematical chart/stability problems.  No primitive grants or forbids
the shadow weights.  Activity color and the raw/center split are not physical
time or probability.  No axiom-update stop is established.

### N7 — hostile steelman

A hostile reviewer should insist that Block39 weak is not strong; this theorem
recomputes every row at `a_s`.  They should reject red as a tag, one tag as
density, and empty as vacuum; Sections 2--4 do.  They should reject dummy
shadows as contraction gain; the shadow is only an upper membership carrier.
They should demand all local empty coordinates, not only the quadratic center,
be isolated before raw suppression; `P_0` does so.  They should demand future
atom costs on the raw source, matched `68` geometry, and refusal to call a
stronger-source estimate same norm; all are explicit.  No broad no-go follows,
because sectorwise and invariant-enhanced-decay routes remain live.

### N8 — cross-cycle echo

The theorem preserves the weak-completion obstruction's narrow scope, the
finite-horizon multi-index atom repair, exact atom creation/erasure, raw-lift
geometric suppression, Gaussian-adapted coefficient weight, and Block39's
local determinant ownership.  It follows the campaign pattern of replacing a
failed broad certificate with a narrower actual-range norm that keeps the
load-bearing provenance.
