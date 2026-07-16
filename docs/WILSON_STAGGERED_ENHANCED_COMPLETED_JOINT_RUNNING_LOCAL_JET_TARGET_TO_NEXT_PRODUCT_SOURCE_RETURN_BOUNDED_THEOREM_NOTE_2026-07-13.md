# Enhanced completed-joint running-local-jet target-to-next-product-source return

**Date:** 2026-07-13
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_enhanced_joint_target_next_product_source_return_2026_07_13.py`](../scripts/wilson_staggered_enhanced_joint_target_next_product_source_return_2026_07_13.py)

## 0. Result and scope

One enhanced finite-regulator completed-joint source ball returns to the next
declared **product-coordinate source bundle** after the raw diameter-zero
local jet is extracted once into running data, the scalar trace of its
quadratic part updates the onsite product Gaussian, and the remaining local
jet stays explicit.  This closes a
target-to-next-product-source return section.  It does not construct the next
correlated scalar-reference split, an autonomous fixed-chart ball, or a
horizon-uniform induction.

The five direct inputs are the running-center and product-reference transition
from the
[extracted `S^(2)` theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the fresh higher-moment actual-orbit recomputation from the
[enhanced generated-factor theorem](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the shortest-center and Schur-tail localization from the
[external-shortest-center theorem](WILSON_STAGGERED_EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the completed physical joint graph and atom return from
[Block46](WILSON_STAGGERED_SCALAR_PRODUCT_REFERENCE_COMPLETED_JOINT_OUTER_HAAR_ACTUAL_OUTPUT_ATOM_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md),
and the exact covariance/Hessian tube from
[Block47](WILSON_STAGGERED_COMPLETED_JOINT_TWO_MARK_COVARIANCE_NONLINEAR_SOURCE_OUTPUT_TUBE_BOUNDED_THEOREM_NOTE_2026-07-13.md).

Use the same Wilson--staggered `SU(3)`, `beta=0` finite-sector grammar, but
rerun every upstream factor and response row at

```text
m=10^96,
c=0.01,
Theta_0=12.4,
Lambda_0=0.4,
delta=0.001.                                                       (0.1)
```

The source centered arm therefore pays
`(Theta_0+2c,Lambda_0)=(12.42,0.4)`.  The enhanced Block42 input is not an old
output relabeled at larger weights: it is freshly evaluated at

```text
theta_dec=Theta_0+2c+Lambda_0=12.82.                              (0.2)
```

After completing the scalar-reference joint graph,

```text
K_T=1.742570618731203 10^(-10)<0.01.                              (0.3)
```

On the whole radius-`delta` ball the conservative two-root bound gives

```text
K_delta=0.001000500340965404<0.01,
tau_delta=0.04089819602043138,
M_delta=98.15422032663670,

B+q delta+(M_delta/2)delta^2
 =0.0008678223362291083<0.001.                                   (0.4)
```

The tube margin is `0.0001321776637708917`.  Projecting and overcharging the
complete local/output ledger gives a bound on the full Hermitian onsite
quadratic, not only its scalar trace:

```text
B_complete=0.001867836809216916,
epsilon_Q=0.000003790646118961634,
gap/m>=0.9999962093538810.                                       (0.5)
```

The fresh site-block atom output has

```text
theta_atom=4.437241454001003,
lambda_atom=0.2.                                                  (0.6)
```

Even if the fields are not rescaled to the new scalar mass chart, the
worst fixed-field onsite-reference comparison costs only

```text
log T_ref=0.00001608234205929530.
```

Consequently

```text
theta_return=theta_atom-log T_ref
            =4.437225371658944>4.4,
lambda_return=0.2,                                                (0.7)
```

and `expm1(delta)=0.001000500166708342<0.01`.  After the next raw local jet is
moved into running data, the residual therefore belongs to a next
product-coordinate source bundle at weights `(4.4,0.2)`, numerically matching
the centered weights used by Block47, with potential norm at most `delta` and
a strict spatial margin `0.03722537165894391`.  The traceless Hermitian
quadratic and the higher local jet are carried in the running ledger; they are
not absorbed into the scalar product Gaussian.  Membership in Block47's
correlated `C_ref=L E_ref` split is not inferred.

The price is explicit.  The same enhanced source moments fail the upstream
Block40/42 activity test at `m=10^64`; this theorem uses `m=10^96`.  The input
weights `(12.42,0.4)` are also stronger than the returned weights
`(4.4,0.2)`.  No fixed-m or all-horizon claim is made.

## 1. Enhanced completed joint graph and uniform tube

Let `Phi_46^(enh)` denote the complete Block46 graph rebuilt at (0.1)--(0.2),
with the same phase order:

1. recompute the actual generated decorated base at the enhanced moment;
2. install the scalar product reference and its inverse normalization;
3. expand the full all-word onsite-`Q` plus shortest-hopping determinant;
4. complete the common hidden Haar/Gaussian graph;
5. project the physical output once;
6. reattach the hidden-empty arm and atomize the output once.

The enhanced generated factor row is

```text
K_dec=1.620107585289108 10^(-10),
B_star=8.747359510122899 10^(-13).                                (1.1)
```

The shortest relative-hopping contribution and the actual Gaussian/boundary
and Schur-tail rows are positive but far below the aggregate binary64
resolution.  The runner evaluates them with 120-digit Decimal arithmetic.
It then assigns each hidden Gaussian/boundary and tail arm its own visible
outward charge `10^(-20)>ulp(K_T)`.  The full determinant is converted by an
outward binary64 rounding, so its sub-ulp shortest term remains owned.  The
declared visible rows are deliberately much larger than the analytic values;
they are not set to zero or absorbed into an unrelated row.

With `D(K)=sup_(n>=1)n exp[-(c-K)n]`, the base graph gives

```text
D=36.78794475820014       (n=100),
tau=6.410559165914614 10^(-9),
B=1.447298780805873 10^(-8),
q=max(exp(-0.2),q_centered)=0.8187307530779818.                   (1.2)
```

For `||H||_48<=delta`, raw fiber constants cancel from the normalized
functional and the centered activity rises by at most `expm1(delta)`.  The
two-root proof of Block47 applies on the enhanced graph with

```text
P_2<=(1-tau_delta)^(-4),
M_delta=68exp(0.2)P_2.                                           (1.3)
```

Equations (0.4) follow.  An independent 80-digit Decimal reconstruction uses
the exact integer optimizer `n=111`; it does not call the binary64 Hessian
row as its arithmetic oracle.

## 2. Whole-local-jet split and running base

The earlier restricted tube separated only the Hermitian onsite quadratic
center.  A return section must also handle empty future atoms in the onsite
quartic/sextic jet.  Let `P_0` be the complete diameter-zero projector after
the scalar vacuum is removed and declare

```text
P_rel=P_0,
P_quad=P_(0,2)^sa subset P_rel.                                  (2.1)
```

For the current normalized hidden functional, let `L` lift retained
coefficients as hidden-fiber constants.  Keep the raw non-onsite arm that is
present in the Block47 source class.  The type-correct split is

```text
j=P_rel E_ref H,                 g=(1-P_rel)E_ref H,
h^o=(1-L E_ref)H,

H=Lj+Lg+h^o,                    E_ref h^o=0.                     (2.2)
```

The three coordinates have different jobs.  The local coefficient `j` moves
into the running base.  The raw non-onsite coefficient `g` remains in the
residual map and receives the exact support gain.  Only `h^o` is a centered
mark charged to the joint cluster expansion.

Every retained coefficient lifted by `L` is hidden-fiber constant.  Therefore

```text
R(Phi+L(j+g)+h^o)=L(j+g)+R(Phi+h^o),                             (2.3)
Cov_Phi(Lu,F)=0.                                                  (2.3a)
```

The local jet is a neutral running coordinate, while `D_(2,1)Lg` still pays
the support rescaling.  The nonlinear estimate is applied to

```text
T_res=(1-P_rel)D_(2,1)R.                                         (2.4)
```

This enlarges the Block47 domain only in the raw diameter-zero direction.  A
convenient direct-sum source norm is

```text
||H||_48=||j||_local+||g||_raw+||h^o||_joint<=delta.             (2.4a)
```

Because `j` cancels from normalized responses and
`||g||_raw+||h^o||_joint<=delta`, the enhanced Block47 activity, Hessian, and
Taylor rows remain valid without charging `j` as a polymer activity.

At the output, first change to the next product dictionary.  Let `E_1` be its
product expectation, `L_1` its retained-coefficient lift, and
`C_1=L_1E_1`, `Q_1=1-C_1`.  Project coefficients, not already lifted
interactions:

```text
j_1=P_rel E_1 Gamma_out,        g_1=(1-P_rel)E_1 Gamma_out,
gamma_1^o=Q_1 Gamma_out,

Gamma_out=L_1j_1+L_1g_1+gamma_1^o,
Gamma_1^res=Gamma_out-L_1j_1=L_1g_1+gamma_1^o.                  (2.5)
```

Consequently `P_rel E_1 Gamma_1^res=0`.  No second lift is applied.  The
Hermitian quadratic part `P_quad j_1` and the complement
`(P_rel-P_quad)j_1` remain explicit running local data.  On the next fiber
they are lifted once by `L_1`; only the `Q_1` component is centered.

The `B_complete` row in (0.5) bounds the total running local/output potential;
its `epsilon_Q` row separately bounds the Hermitian quadratic operator.  This
does not make the local jet contractive: translating it into the next base is
part of the bundle chart.  A fixed-base Banach theorem is not inferred.

## 3. Scalar reference, traceless ledger, and product-chart transport

The quadratic output obeys the operator bound in (0.5).  In dimensional
coefficients this means
`||P_quad j_1||_op<=epsilon_Q m`; equivalently, the normalized coefficient
`widehat Q_1=m^(-1)P_quad j_1` has operator norm at most `epsilon_Q`.  The
Hermitian onsite projector is not identified with a scalar mass.  On each
three-color onsite block define

```text
P_sc Q=(tr_color Q/3)I,          P_tl Q=Q-P_sc Q.                 (3.1)
```

With the sign convention in which `j_1` is added to the quadratic action, the
scalar trace updates the product-Gaussian coefficient,
`m_1=m[1+tr_color(widehat Q_1)/3]`.  Since
`|tr_color Q|/3<=||Q||_op`, the full Weyl row implies

```text
(1-epsilon_Q)m<=m_1<=(1+epsilon_Q)m.                              (3.2)
```

The traceless part `P_tl P_quad j_1` is not put into the product Gaussian.  It
stays in the running local ledger together with
`(P_rel-P_quad)j_1`.  The full local ledger is already paid by (0.5), so this
split neither discards a coefficient nor spends a second output budget.

There are two honest scalar-reference chart routes.

First, use the mass-adapted field torsor with

```text
rho=sqrt(m/m_1),
eta_1=m_1^(-1/2).                                                 (3.3)
```

The field dilation conjugates the old scalar product reference to the new one.
All non-scalar local coefficients are transported by pair degree and remain in
the explicit running ledger; Haar coordinates are unchanged.

Second, retain the old field variables and pay an explicit comparison.  On a
three-color onsite coordinate, every balanced `p`-pair contraction changes
by at most

```text
delta_ref<=(1-epsilon_Q)^(-3)-1
          =0.00001137202457157649,

T_ref=1+sqrt(2)delta_ref
     =1.000016082471381.                                         (3.4)
```

The projective split-algebra estimate therefore costs `log T_ref` per actual
site.  Paying the larger fixed-field route gives (0.7); the torsor route is
no worse.

For the fixed-field route, apply the next site-block atom decomposition to
`Gamma_1^res` after the coefficient split (2.5).  Its potential is at most
`delta`; constant-one factor exponentiation gives

```text
K_1^fac<=expm1(delta)<c.                                         (3.5)
```

Equations (0.6)--(0.7) pay the next source weights.  The returned residual has
no raw `P_0` arm, its `Q_1` arm lies at `(4.4,0.2)`, and its raw non-onsite arm
is bounded by the stronger diameter gain `exp(-0.2)`.  Together with the
separate running coefficient `j_1`, this is the claimed
target-to-next-product-source return section.

It is not yet a second physical RG theorem.  That requires rebuilding the
next correlated scalar-reference determinant, proving its marked and
two-mark constants on the returned ball, and controlling the next local-jet
update.  Those operations are not identified with the present return map.

## 4. Exact finite-horizon boundary

The return uses enhanced input moments.  Without the enhancement, the
original Block47 output has only

```text
(theta_atom,lambda_atom)=(0.4265740169,0.1),                     (4.1)
```

which cannot be embedded by identity into `(4.4,0.2)` on unbounded supports.
Enhancing `Theta` without enhancing `Lambda` still leaves the diameter
exponent at `0.1`.

At the other end, the same enhanced moment request at `m=10^64` fails before
the completed joint graph: the fresh Block40 factor activity exceeds its
allowance.  The positive witness moves to `m=10^96`.  This is a finite massive
certificate, not a critical trajectory.

The black-box site/diameter bookkeeping has the schematic recurrence

```text
Theta_(j+1)=Theta_j/2-log C_*-sigma_eta,j,
Lambda_(j+1)=Lambda_j/2.                                         (4.2)
```

At fixed input moments both reserves decay.  Holding a prescribed positive
output instead requires the source moments to grow backward with the horizon,
which in turn pushes the massive activity witness outward.  The theorem does
not establish a horizon-uniform moment/mass schedule, a same-chart fixed
point, or a continuum limit.

## 5. Runner contract

Run

```bash
python3 scripts/wilson_staggered_enhanced_joint_target_next_product_source_return_2026_07_13.py
```

The runner checks: a fresh enhanced Block42 composition; the 120-digit
shortest, Gaussian/boundary, determinant, and tail rows; visible outward
ownership above the aggregate ulp; the completed joint activity; the uniform
two-mark/Taylor tube; an independent 80-digit optimizer and tube
reconstruction; a finite-model three-way source split with both raw non-onsite
and centered arms; the coefficient-valued next-product output split; a
non-scalar Hermitian quadratic fixture with scalar/traceless reconstruction;
the gap and fixed-field reference transition; returned source weights and
factor activity; the `m=10^64` enhanced-moment failure; the finite-horizon
fixed-weight boundary; the source contract; and exactly five dependencies.
The arbitrary-regulator cluster bounds and the operator inequality
`|tr Q|/3<=||Q||_op` remain analytic content of Sections 1--3.

## 6. No-Go Discipline N1--N8

The positive return leaves a named all-horizon boundary, so the complete
stress test is recorded.  The negative statement is only:

**NG48:** this one enhanced finite-horizon return section does not itself
supply a fixed-m, fixed-chart, all-horizon RG induction.  It is a logical
non-implication from the displayed certificate, not a physical RG no-go.

### N1 — alternative-route enumeration

| route | marker | executed outcome |
|---|---|---|
| Identity-retag the original Block47 target as its next source | `ATTEMPTED` | Fails in both site and diameter weights: `(0.426574...,0.1)` is not `(4.4,0.2)`. |
| Enhance only the site moment | `ATTEMPTED` | Fails: halving `Lambda_0=0.2` still returns diameter exponent `0.1`. |
| Treat the whole raw onsite jet as contractive residual | `ATTEMPTED` | Rejected: its normalized response is affine with derivative one. Section 2 instead translates it into the running base. |
| Ignore the old/new onsite reference change | `ATTEMPTED` | Rejected: Section 3 either uses the exact field torsor or pays the fixed-field `T_ref` row. |
| Keep `m=10^64` at the enhanced moments | `ATTEMPTED` | Fails the freshly recomputed upstream activity, before any return inference. |
| Freshly recompute at enhanced moments and larger finite mass | `ATTEMPTED` | Positive at `m=10^96`; equations (0.3)--(0.7) close. |
| Iterate the black-box moment recurrence unchanged | `ATTEMPTED` | Rejected: both moments halve after fixed surcharges, and a prescribed output forces growing backward moments/mass. |

Live outside NG48 are a lineage-sensitive carrier that avoids the full site
charge, a small/large-polymer split, a shortest-center-relative activity
schedule, a scale-indexed norm with uniform chart margins, and an alternative
physical block.  None is ruled out here.

### N2 — wall-independence audit

| wall | atomic unresolved statement |
|---|---|
| `W1` | A horizon-uniform moment, activity, gap, and mass schedule for the returned bundle. |
| `W2` | A second-horizon correlated-reference graph with uniform one-mark and two-mark constants on the returned ball. |

| pair | left implies right? | right implies left? | reason |
|---|---:|---:|---|
| `W1-W2` | No | No | Uniform scalar schedules do not construct the correlated graph; one second graph does not control every horizon. |

Generic-source embedding, taste selection, a critical continuum, and a
physical law are broader out-of-scope programs.  They are not counted as
independent walls of the narrow all-horizon non-implication `NG48`.

### N3 — hidden-condition phrase scan

The note before this subsection and the runner before its phrase list are
scanned case-insensitively for the mandatory phrases.

| phrase | hits before scan | disposition |
|---|---:|---|
| `we assume` | 0 | absent |
| `by construction` | 0 | absent |
| `as is standard` | 0 | absent |
| `the framework provides` | 0 | absent |
| `bridge context` | 0 | absent |
| `background` | 0 | absent |
| `naturally` | 0 | absent |
| `obviously` | 0 | absent |
| `standard QFT` | 0 | absent |
| `registered` | 0 | absent before this self-referential table |
| `canonical` | 0 | absent before this self-referential table |

`Return` means membership in the next declared source bundle after a running
base/reference chart change.  `Uniform` means uniform on the displayed
radius-`0.001` finite-horizon ball.  `Enhanced` means the moments and every
dependent activity are freshly recomputed.  None means all-horizon,
fixed-point, critical, physical-law, or continuum closure.

### N4 — residual matching

| exact authority | residual supplied | present use | match? |
|---|---|---|---:|
| Extracted-`S^(2)` note, equations (0.8)--(0.11) and (3.1)--(3.2) | local/raw split, center transition, field chart | Sections 2--3 | Yes |
| Enhanced-factor note, equations (0.4)--(0.10) | fresh higher-moment generated-factor row | enhanced base in Section 1 | Yes |
| External-shortest-center note, Sections 1--4 | Decimal tail, scalar reference, Weyl ownership | micro rows and gap ledger | Yes |
| Block46, Sections 3--6 | completed joint phase order and physical atom return | enhanced parameter rerun | Yes |
| Block47, Sections 1--4 | exact Hessian, conservative pair bound, nonlinear tube | equations (0.4), (1.3) | Yes |
| Framework dynamics-selection result | law/time/probability underdetermination | not used | Residual mismatch; dropped |

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One enhanced finite-regulator generated graph | Yes | Base activity and all visible micro rows close. |
| Whole restricted radius-`0.001` ball | Yes | Uniform pair/Taylor, gap, atom, and return rows close. |
| Full diameter-zero local jet | Yes | Exact affine factorization and one output projection/recentering. |
| One old/new scalar product reference transition | Yes | Exact torsor route and conservative fixed-field cost. |
| Second physical hidden integration | No | `W2` remains. |
| All horizons at fixed or controlled mass | No | `W1-W2` remain. |
| Generic sources, taste, continuum, law/time/probability | No | Outside the subject of `NG48`; no negative inference is made. |

### N6 — partial closure and primitive scan

The theorem closes one target/source chart mismatch by spending enhanced
moments and translating the full local jet.  It does not close the next
correlated graph, a uniform schedule, or a critical trajectory.  Lattice,
Qubit, Admissibility, and Record and the approved primitive registry neither
supply nor obstruct the remaining analytic schedules and cluster bounds.

No axiom-update stop is triggered.

### N7 — hostile steelman

The strongest objection is that moving from `m=10^64` to `m=10^96` and from
source weights `(4.4,0.2)` to `(12.42,0.4)` is not an autonomous return.  The
objection is correct.  This theorem proves a scale-indexed return section, not
fixed-chart invariance.  A sharper lineage/root-carrier norm could lower the
site surcharge and a shortest-center-relative schedule could make later
activities cheaper.  Those routes defeat any broader impossibility claim but
are not supplied by the displayed certificate.

### N8 — cross-cycle echo

| prior wall/path | earlier status | mechanism used here | disposition |
|---|---|---|---|
| Weak-to-strong identity handoff | Unbounded on long loops | Fresh enhanced moments and full recomputation | Retired for one displayed return only. |
| Product Gaussian tensor explosion | Old fixed `eta` cost | Mass-adapted torsor or explicit `T_ref` payment | Retired for one reference transition. |
| Empty future onsite atoms | Violated raw-quadratic-only source restriction | Three-way source split and coefficient-valued next-product projection | Retired for one bundle handoff. |
| Block42 finite-horizon moment recurrence | Source moments grow backward | One `m=10^96` enhanced witness | Preserved as the all-horizon boundary. |
| Block46 unchanged reuse failure | Fixed source missed response/factor return | Different enhanced source chart | Not contradicted; original fixed-chart failure remains. |
| Block47 source/output tube | Target weaker than source | Paid site, diameter, and reference margins | Upgraded to one target-to-next-source section. |

**No-Go Discipline status:** `PASS` for NG48 at the displayed finite-horizon
resolution.

## 7. Claim boundary

The result is one finite-regulator, fixed-sector, enhanced-moment,
restricted-class radius-`0.001` nonlinear tube whose running-local-jet output
returns to the next declared product-coordinate source bundle.  It is not an
autonomous invariant ball, a second physical RG step, an all-horizon
construction, a continuum limit, or a derivation of dynamics, time, unitarity,
or probability.  Its effective status is set only by the independent audit
lane and dependency closure.

No axiom-update stop is triggered.
