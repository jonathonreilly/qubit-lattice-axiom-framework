# Extracted S2 future center, actual-range product reference, and persistent-gap ledger

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_future_s2_center_reference_ledger_2026_07_12.py`](../scripts/wilson_staggered_future_s2_center_reference_ledger_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_future_s2_center_reference_ledger_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_future_s2_center_reference_ledger_2026_07_12.txt)

## 0. Result

The exact quadratic kernel extracted from the first Schur step has its own
local product-reference counterterm ledger, and the actual bare range from the
previous strong coarse-shadow theorem can be recentered around it. The new
center is positive Hermitian and Laplacian-like; it is not relabeled as the
original anti-Hermitian staggered Dirac form.

Use the exact center extraction and coefficient chart from the
[Gaussian-adapted shortest-center theorem](WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the positive Schur identities from the
[factor-two block theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the local determinant ownership and colored subtraction from the
[joint product-reference theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the actual factor-rooted next-strong range from the
[future-atom strong coarse-shadow theorem](WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md).

On the first coarse lattice write

```text
S^(2)=mu I+R_2,
mu=m+2/m,
R_2=-(1/(4m))sum_mu[V_(X,mu)shift_(+mu)
                    +V_(X-mu,mu)^dagger shift_(-mu)].             (0.1)
```

Then

```text
||R_2||<=2/m,
S^(2)>=mI,
h_2:=||R_2||/mu<=2/(m^2+2)<1.                                   (0.2)
```

The hopping in (0.1) is Hermitian, not anti-Hermitian. A scalar field
rescaling changes its magnitude but cannot restore the original staggered
`*`-structure or the missing even/odd taste carrier.

For the next partition `Lambda_1=K_1 union I_1`, put

```text
A_2=(S^(2))_(I_1I_1),
G_2=G_(A_2),
G_mu=onsite-product normalized Gaussian of mass mu.               (0.3)
```

Principal compression preserves the gap, so `A_2>=mI` and
`det A_2>0`. Keep the existing coefficient weight `eta=m^(-1/2)`;
do not switch to `eta=mu^(-1/2)`. At this `eta`, both `G_2` and `G_mu`
are contractive.

The exact product-reference identity is

```text
B_2=exp[-bar zeta R_(2,II) zeta],
Z_2=G_mu[B_2]=det(A_2)/mu^(3|I_1|)>0,
G_2[F]=G_mu[F B_2]/Z_2.                                           (0.4)
```

The loop expansion of `log Z_2` has only even words. Length two is a
gauge-independent vacuum term; local even words of length at least four give

```text
C_2=product_gamma exp(-psi_gamma^(2)),
D_2(z)=product_gamma exp(z psi_gamma^(2)),
C_2D_2(1)=1.                                                      (0.5)
```

These are a new next-center normalization counterterm and determinant
restore. They are not the old `C_A,D_A` factors, which already canceled in
the first physical preintegration step.

Write the actual Block40 output before recentering as

```text
m bar psi psi+Gamma_40
 =bar psi S^(2)psi+P_1,
P_1=Gamma_40-bar psi(S^(2)-mI)psi.                                (0.6)
```

This note uses the provenance-preserving architecture: retain the Block40
canonical current atoms, change their onsite Gaussian expectation explicitly,
and bound the center shift in the same decorated norm. Let `B_40` be the
proven next-strong base row before recentering and put
`Delta_2=S^(2)-mI`. With `C_*=3+2sqrt(2)`,

```text
B_Delta
 <=C_*(6/m^2)exp(theta_s)
   +8C_*^3(9/(2m^2))exp(2theta_s+Lambda),
B_*<=B_40+B_Delta.                                                (0.7)
```

First apply the complete current product-fiber conditional split to every
coefficient:

```text
P_empty=Delta_empty P_1,
P_nonempty=sum_(S nonempty)Delta_S P_1.                            (0.8)
```

Only `P_empty`, which is independent of every current hidden Haar/Gaussian
coordinate, is further separated into the finite `P_0` local jet and
extended raw lifts. Every hidden-dependent term remains in `P_nonempty`,
including diameter-zero onsite quartic/sextic terms. Write its connected
atoms as `Phi_(X,S)^o`, `S nonempty`.

Exponentiate these atoms in the free provenance-lineage algebra, retaining
one formal root for every `Phi` insertion before evaluation. Define

```text
r_(X,S)=exp(-Phi_(X,S)^o)-1,
K_P=exp(B_*)-1.                                                    (0.9)
```

For weighted carrier factor `w_X>=1`, constant-one Banach algebra
submultiplicativity gives

```text
sum_(X,S nonempty) w_X||r_(X,S)||
 <=sum_(X,S nonempty)[exp(w_X||Phi_(X,S)^o||)-1]
 <=exp(sum_(X,S nonempty)w_X||Phi_(X,S)^o||)-1
 <=K_P.                                                          (0.9a)
```

The local jet is extracted as center/relevant data. Extended empty/raw lifts
are carried separately and gain `exp(-Lambda/2)` under the next factor-two
support map. Products of nonempty lineage factors may fuse to an evaluated
empty atom; the formal root and full spatial carrier still pay that output,
which is carried rather than discarded or reclassified as nonempty.
Equations (0.9)--(0.9a) are therefore an actual factor-row theorem, not an
imported Wilson-only next grammar.

The old and new onsite product Gaussian atoms are close but not identical.
For one three-color coordinate let `E_m,E_mu` be their expectations and let
`r_*=1+sqrt(2)`. On the old centered sector,

```text
delta_mu=||E_mu-E_m||
 <=1-(m/mu)^3,
N_(mu,r_*)(F)
 <=T_mu N_(m,r_*)(F),
T_mu=1+sqrt(2)delta_mu.                                          (0.10)
```

Sequential re-Hoeffding costs at most `T_mu` per actual Gaussian coordinate.
The Block40 spatial weight pays it by using

```text
theta_2=theta_s-log T_mu>0.                                      (0.11)
```

No silent identification of `G_m` and `G_mu` atoms occurs.

For a next `K_1-I_1` center edge define

```text
j_e^(2)=bar psi_K R_(2,KI)zeta_I+bar zeta_I R_(2,IK)psi_K,
J_2(z)=product_e exp(-z j_e^(2)),
R_P(z)=product_(X,S nonempty)exp(-z Phi_(X,S)^o).                 (0.12)
```

The hidden-dependent actual-range normalized interpolation is

```text
E_z[O]
 =E_HG_mu[O B_2 C_2 D_2(z)J_2(z)R_P(z)]
  /E_HG_mu[B_2 C_2 D_2(z)J_2(z)R_P(z)].                          (0.13)
```

At `z=0`, (0.13) is the combined next-center reference `E_HG_2`. At
`z=1`, (0.5) cancels first, and the integrand is precisely the recentered
hidden-dependent next preintegration action. The factored-out local/raw
sector is then reattached to the output exactly. There is no separately
imported Wilson row: old gauge and determinant effects are owned by `P_1`
once.

With

```text
nu_2=18(1/(4m))eta^2=9/(2m^2),
L_2=theta_2+Lambda,

K_G^(2)=8[exp(C_*nu_2)-1]exp(2theta_2+Lambda),

K_D^(-,2)
 =(3/2)sum_(even r>=4)
   C_*^r h_2^r g(3C_*^r h_2^r/r)exp(rL_2),

K_B^(2)=K_G^(2),
K_D^(+,2)=K_D^(-,2),

K_ref^(2)=K_G^(2)+K_D^(-,2),
K_R^(2)=K_B^(2)+K_D^(+,2)+K_P,
K_T^(2)=K_ref^(2)+K_R^(2)<c.                                    (0.14)
```

The factor cost is `C_*`, not `C_*^3`, because this theorem integrates the
current hidden coordinates into an ordinary weak output; it does not perform
another future-coordinate pullback. The physical row `K_P` is load-bearing.
Dropping it would prove only a center-only model, not the actual bare range.

Let

```text
D=sup_(n integer>=1)n exp[-(c-K_T^(2))n],
tau=K_T^(2)D<1,
A_2^joint=2D K_R^(2)/(1-tau)^3.                                  (0.15)
```

For a provenance-preserving actual-range strong mark centered under
`E_HG_2`, color-preserving subtraction removes the red-free series. The
proved factor-two carrier and raw/center split give the next weak bounds

```text
B_(2,weak)<=68exp(Lambda/2)K_T^(2),
B_(2,split)<=B_(2,weak)+exp(-Lambda/2)B_*,
q_(2,centered)=68exp(Lambda/2)A_2^joint,
q_(2,split)=max{exp(-Lambda/2),q_(2,centered)}.                    (0.16)
```

At

```text
m=2 10^11, beta=0, c=0.2,
Theta=10^(-6), Lambda=1, eta=m^(-1/2),                            (0.17)
```

the runner gives

```text
B_40             =4.064085767704031 10^(-4),
B_Delta           =1.079326085135096 10^(-18),
K_P               =4.064911719247879 10^(-4),
K_G^(2)           =3.173399990699913 10^(-20),
K_D^(-,2)         =2.925685201135801 10^(-84),
K_B^(2)           =3.173399990699913 10^(-20),
K_D^(+,2)         =2.925685201135801 10^(-84),
K_T^(2)           =4.064911719247880 10^(-4)<c,
D                 =1.843139501223258,
tau               =7.492199358731112 10^(-4),
A_2^joint         =1.501812907849134 10^(-3),
B_(2,weak)        =0.0455729636222870<c,
B_(2,split)       =0.0458194628844684<c,
q_(2,centered)    =0.1683728202332358,
q_(2,split)       =0.6065306597126334<1.                          (0.18)
```

Center-only Gaussian elimination also generates

```text
S_next
 =mu I-R_(2,KI)A_2^(-1)R_(2,IK),
S_next>=mI.                                                       (0.19)
```

The exact shortest part closes in the same enlarged Hermitian center family:

```text
R_(2,KI)R_(2,IK)=k^2[8I+A(W)],
mu'=mu-8k^2/mu,
k'=k^2/mu,
S_next^(2)=mu'I-k'A(W),
gap(S_next^(2))>=mu-16k^2/mu>m.                                  (0.20)
```

Equations (0.13)--(0.18) prove an actual bare range next-center
**strong-to-weak** step. They are not a same-domain perturbation theorem: the
weak output cannot be reused as the next strong factor row by identity, and
no same-norm Hessian or invariant ball follows.

## 1. Positive center and the exact next Gaussian reference

The coordinate-free identity from the predecessor is

```text
S^(2)=mI+m^(-1)M_KI M_KI^dagger.                                 (1.1)
```

It proves (0.2) and gauge covariance directly. Formula (0.1) is its complete
two-hop evaluation: eight backtracks give the onsite `2/m`, and eight
straight paths give the Hermitian coarse-link hopping. All retained
first-coarse sites had even original staggered parity. Consequently (0.1)
belongs to an enlarged positive quadratic-center chart, not the original
staggered nearest-neighbor chart.

On the next factor-two partition, no nearest neighbors both lie in `K_1`, so
`(S^(2))_(K_1K_1)=mu I`. Every `I_1-I_1` center bond is nonskeleton. Every
`K_1-I_1` boundary bond is skeleton and is written either as `V=B` or
`V=B^(-1)W` under the next straight-link disintegration.

For any balanced hidden `p`-pair monomial, the covariance-minor estimate for
`A_2>=mI` is `m^(-p)`. Its input weight is
`eta^(2p)=m^(-p)`, proving norm-one contractivity. The onsite product
covariance gives `mu^(-p)<=m^(-p)`. Thus the reference change does not
require the unproved `eta=mu^(-1/2)` chart.

For one onsite product coordinate the nonzero contraction ratios change from
`1` to `(m/mu)^p`, `0<=p<=3`. This proves the first inequality in (0.10).
Writing an old split as `F=L E_mF+Q_mF`, use

```text
E_muF=E_mF+(E_mu-E_m)Q_mF,
Q_muF=Q_mF-L(E_mu-E_m)Q_mF.                                      (1.2)
```

Then

```text
N_(mu,r)(F)
 <=||E_mF||+[r+delta_mu(1+r)]||Q_mF||.                            (1.3)
```

At `r=r_*`, `1+1/r_*=sqrt(2)`, proving (0.10). Tensoring (1.2)
coordinate by coordinate and lowering the spatial weight by `log T_mu`
proves (0.11).

## 2. New determinant ownership and boundary phase order

Relative to the onsite `mu` reference,

```text
log Z_2
 =sum_(r>=1)(-1)^(r+1)Tr[(R_(2,II)/mu)^r]/r.                      (2.1)
```

The next coarse lattice is bipartite and the principal site compression
commutes with its parity operator, so odd traces vanish. Since `R_2` is
Hermitian, the even terms carry the negative determinant sign. A two-site,
three-color bond therefore has

```text
det[[mu,-kV],[-kV^dagger,mu]]/mu^6
 =[1-(k/mu)^2]^3,                 k=1/(4m),                       (2.2)
```

not the plus sign of the original anti-Hermitian block. The runner checks
(2.2) directly. Backtracking length-two words are gauge-independent; after
their vacuum extraction, the local length-at-least-four potentials give
(0.5) with the row in (0.14).

The ownership ledger is:

| object | color | exact role | forbidden duplicate |
|---|---:|---|---|
| `mu^(3|I_1|)` and next length-two loop | none | new center vacuum | never an activity |
| `B_2` center bonds | blue/uncolored | normalized next Gaussian reference | not a physical red factor |
| `C_2` | blue/uncolored | new local inverse normalization | not the old `C_A` |
| `D_2(z)` | red | new determinant restore | do not insert `det A_2` separately |
| `J_2(z)` | red | next center boundary coupling | do not insert generated `S_next` paths |
| `R_P(z)` | red | nonempty first-step residual factors once | no separate old Wilson/determinant rows |
| local/raw empty sector | external | exact factor carried to output | never a hidden root |
| `mu bar psi psi` | none | external center data | not a KP activity |
| `S_next` | output only | generated next Schur center | never a simultaneous input |

At physical color one first use `C_2D_2(1)=1`. Only then evaluate the current
onsite Gaussian coordinates:

```text
mu^(3|I_1|)G_mu[B_2J_2]
 =det(A_2)
  exp[bar psi R_(2,KI)A_2^(-1)R_(2,IK)psi].                       (2.3)
```

Equation (2.3) is the center-only identity `R_P=1`. With `R_P` present, the
same `det A_2` normalizes the center measure and the residual expectation
dresses the connected output; no factorization of the full residual
integrand is claimed. Together with the external
`exp[-mu bar psi psi]`, (2.3) generates (0.19)
and its determinant exactly once. Old determinant factors are already
coefficients of `P_1`; new determinant factors are generated only by (2.3).

## 3. Actual residual factorization and joint response

The Block40 theorem supplies the first output as connected canonical
product-coordinate atoms with next-strong spatial weight
`theta_s=Theta+2c`. Recenter its complete quadratic coefficient at (0.1).
The plain coefficient norm of the onsite shift is at most `6/m^2` per site;
the safe `C_*` factor pays its one Gaussian provenance coordinate. The
Hermitian bond has grouped two-orientation norm `9/(2m^2)`, incidence at most
eight, and two-site span one. The safe `C_*^3` charge pays its current Haar,
endpoint, and Gaussian atom slots. This proves `B_Delta` in (0.7) in the same
decorated norm as `B_40`.

The canonical split before (0.8) is load-bearing. A current-fiber-constant
factor multiplies numerator and denominator of the normalized hidden
functional by the same external coefficient, so it is factored out and
reattached to the unnormalized output. The local `P_0` jet is extracted; the
extended raw sector uses the exact support lift. Every remaining insertion has
a nonempty formal current provenance root and an actual spatial anchor, so
(0.9)--(0.9a) form a lineage-rooted row. Evaluation may fuse its visible atom
to empty without erasing that paid lineage or carrier.

The new center bond and boundary potential both have coefficient norm
`nu_2`: each orientation has coefficient `1/(4m)`, there are two
orientations and at most nine color entries, and `eta^2=1/m`. Their hidden
site/link incidence is bounded by eight. Determinant words use the relative
row `h_2`. These facts prove every term in (0.14).

All factors in (0.13) are expanded in one common hidden Haar/Gaussian overlap
graph. The standard `2c` already present in `theta_s` pays factor grouping
and the hard-core logarithm. Under `K_T^(2)<c`, the normalized series is
absolutely convergent for `|z|<=1`. At `z=0`, a mark centered under `E_HG_2`
kills the complete red-free marked series. Every hidden-dependent survivor at
`z=1` contains `D_2`, `J_2`, or an actual residual factor from `R_P`.
Freezing `D` at the total row and differentiating the two-root envelope gives
(0.15).

The output is deliberately weak. It uses the same factor-two support shadow
with half spatial weights, so `diam X<=ell(Y)+1` costs `exp(Lambda/2)` and the
proved routed anchor multiplicity is `68`. No canonical atom statement at a
third horizon is made.

## 4. Persistent base gap and the remaining same-domain wall

For any block decomposition of a positive matrix `C>=mI`, its principal
hidden block obeys `C_II>=mI`. The Schur inverse identity gives

```text
S_C^(-1)=(C^(-1))_KK<=m^(-1)I,
```

hence `S_C>=mI`. Applying this to `C=S^(2)` proves (0.19), uniformly in the
allowed next gauge background and finite regulator.

At shortest path length the hidden propagator is `mu^(-1)I`. The same exact
two-step classification gives eight backtracks and eight straight coarse
paths, hence (0.20). Its lower spectral edge is
`mu'-8k'=mu-16k^2/mu>m`. This proves closure of the shortest positive-center
family even though the full Schur remainder is longer range.

These gaps belong to the exact base center. General residual interactions can
update the projected quadratic coefficient. A perturbative center theorem
must define that projection and prove a Weyl reserve such as
`||delta Q||<m`; it is not inferred from (0.19) or (0.20).

The spatial mismatch also remains exact. Block40's base orbit was measured in
a stronger source row and landed at `theta_s`; the present actual-range step
consumes that strong row and lands at half weights. Neither center migration
nor the tiny atom-transition cost restores the missing spatial reserve. The
live next routes are:

1. prove enhanced decay for the actual generated factor orbit;
2. split small and large clusters and spend unused massive KP slack;
3. combine the exact empty/raw sector with quantitative nonempty-atom density;
4. use a scale-indexed multiscale norm carrying center and spatial reserves;
5. prove a generic enhanced interaction-to-factor map and same-norm two-mark
   Hessian.

These are constructive chart and stability problems. No axiom-update stop is
established.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_future_s2_center_reference_ledger_2026_07_12.py
```

The runner checks the exact center enclosure and relative row, old/new product
Gaussian contractivity and atom transition, a first-principles two-site
three-color Hermitian determinant sign, the even-loop counterterm, a direct
matrix Schur-gap identity, the shortest-center recursion, the parametric
activity gain, actual residual factorization, the strict joint witness,
red-factor cancellation, and the source/dependency contract. Arbitrary-
regulator loop localization, cluster resummation, and carrier bounds are
analytic statements.

## 6. Preliminary boundary map

This is the non-authoritative design history that preceded Section 7. Status
words in this section are planning labels, not No-Go Discipline honesty
markers or verdicts.

### P1 — alternative-route enumeration

| route | disposition | exact residual |
|---|---|---|
| Relabel `S^(2)` as `m'1+M` | scalar route closed in design | `S^(2)` has Hermitian Laplacian hopping and only even original staggered parity. |
| Restore the old form by scalar `rho` | `ATTEMPTED` | A scalar changes magnitude, not `*`-structure or taste. |
| Keep only the onsite `m` center | predecessor-tested | Leaves the dominant exact two-hop quadratic coefficient in the interaction. |
| Use `G_mu` at `eta=mu^(-1/2)` | `ATTEMPTED` | Rejected: the correlated gap is only certified at `m`. |
| Identify `G_m` and `G_mu` atoms | `ATTEMPTED` | Rejected and repaired by (0.10)--(0.11). |
| New `S^(2)` product-reference counterterm | `ATTEMPTED` | Sections 1--2 prove the exact local ledger and Hermitian determinant sign. |
| Center-only next response | `ATTEMPTED` | Exact but insufficient; Section 3 adds the actual residual row `K_P`. |
| Guess new Wilson/determinant/path primitive counts | `ATTEMPTED` | Rejected: the generated residual is exponentiated from its complete canonical coefficient row. |
| Actual residual exponentiation | `ATTEMPTED` | Equations (0.7)--(0.9) prove the factor row after the empty/raw split. |
| Reuse Block40 strong output as its next superstrong input | certificate mismatch | The certified weights differ; actual enhanced decay remains live. |
| Actual-orbit enhanced factor decomposition | not foreclosed | Highest leverage route to same-domain return. |
| Empty/raw plus nonempty density | not foreclosed | May close the sectorwise spatial reserve. |
| Scale-indexed multiscale norm | not foreclosed | May carry center, atom, and spatial shifts without a fixed numerical norm. |
| Perturbative projected-center gap | not foreclosed | Requires a declared projection and operator-norm reserve. |
| Taste-faithful multicomponent block | not foreclosed | Changes the block/carrier, not the axioms. |

### P2 — wall-independence audit

Keep six walls:

```text
W1 enhanced-decay or sectorwise same-domain return,
W2 generic generated-factor/source/provenance closure,
W3 perturbative center update, gap, and normalization,
W4 retained-algebra same-norm Hessian and invariant ball,
W5 physical taste/chart selection,
W6 critical trajectory and observables.                            (N2.1)
```

All fifteen pairs remain independent.

| pair | why neither wall absorbs the other |
|---|---|
| W1--W2 | Actual bare enhanced decay would not embed generic perturbations. |
| W1--W3 | Spatial return neither selects nor gaps the projected center. |
| W1--W4 | Same-domain membership is not a two-mark Hessian or ball. |
| W1--W5 | Decay cannot restore the missing staggered taste carrier. |
| W1--W6 | An ultra-massive return supplies no critical trajectory. |
| W2--W3 | Source and factor charts change with the running center. |
| W2--W4 | A generic one-mark factor map is not nonlinear invariance. |
| W2--W5 | Generated-factor closure does not select taste. |
| W2--W6 | Generic locality supplies no tuning path. |
| W3--W4 | A ball needs both center persistence and nonlinear control. |
| W3--W5 | A gapped center can remain taste-wrong; taste does not prove a gap. |
| W3--W6 | One base gap is not a tuned gap trajectory. |
| W4--W5 | Nonlinear closure must preserve the selected physical carrier. |
| W4--W6 | Autonomy is prerequisite, not criticality. |
| W5--W6 | Continuum observables require a selected physical chart. |

### P3 — hidden-condition phrase scan

| phrase | meaning in this note |
|---|---|
| `S^(2) center` | Exact positive Hermitian base kernel, not the original staggered Dirac form. |
| `migration` | Explicit atom, determinant, boundary, and residual-ledger change, not relabeling. |
| `persistent gap` | Exact base quadratic Schur gap, not a generic interaction gap. |
| `actual bare range` | Block40 base output recentered and factorized by (0.7)--(0.9). |
| `product reference` | Onsite mass `mu` at coefficient weight `eta=m^(-1/2)`. |
| `new determinant` | `det A_2`, distinct from first-step determinant coefficients. |
| `strong-to-weak` | Different source and codomain weights, not same-domain iteration. |
| `factor row` | Exponentiated complete connected potentials, not a guessed primitive grammar. |
| `empty atom` | Current-fiber-constant coefficient carried in the local/raw split, not zero. |
| `centered` | Combined `E_HG_2` centering in the complete normalized series. |
| `Hessian` | A retained coefficient-algebra two-mark estimate; absent here. |
| `taste` | Physical carrier information not supplied by the even-site block. |
| `uniform` | Uniform in the declared strict massive base wedge and finite regulators. |

### P4 — citation/residual matching

| dependency | load-bearing use | residual matched? |
|---|---|---:|
| [Gaussian-adapted shortest-center theorem](WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact `S^(2)`, gap, coefficient weight, and product atoms | Yes |
| [Factor-two block theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Positive block/Schur determinant and inverse identities | Yes |
| [Joint product-reference theorem](WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Local counterterm ownership and color-preserving response envelope | Yes |
| [Future-atom strong coarse-shadow theorem](WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Actual first output row, support carrier, atoms, and strong norm | Yes |

### P5 — rhetoric and resolution audit

The theorem fixes the original bare action, one first output recentered at the
exact `S^(2)` kernel, one next partition, the existing `eta=m^(-1/2)` chart,
one new determinant/counterterm ledger, and a strict ultra-massive witness. It
proves an actual-range strong-to-weak response and base-center Schur gap. It
does not claim original staggered form, taste restoration, generic
perturbation closure, perturbative gap persistence, same-domain return,
Hessian, invariant ball, fixed point, criticality, continuum, time law, or
probability rule.

### P6 — partial-closure and primitive scan

The exact form mismatch rules out only scalar relabeling inside the declared
even-site chart. The spatial mismatch rules out only composition by the
certified identity embedding. Enlarged positive quadratic centers,
taste-faithful blocks, actual enhanced rows, auxiliary first-order
factorizations, and multiscale norms remain live. Center selection,
counterterms, atoms, and gap estimates are constructive chart mathematics;
none is promoted to an axiom. No axiom-update stop is established.

### P7 — hostile steelman

A hostile reviewer should demand the Hermitian determinant minus sign, the
even-parity/taste boundary, the `G_m`--`G_mu` atom transition, separation of
old and new determinant ownership, inclusion of every generated residual
factor, the explicit empty/raw split, refusal to import `S_next`, and the
distinction between a base gap and perturbative persistence. Sections 1--4
make each explicit. They should also reject calling a strong-to-weak estimate
same-domain or calling a one-mark response a Hessian; neither is asserted.

### P8 — cross-cycle echo

The theorem preserves the factor-two action-form/taste boundary, the exact
shortest-center extraction, fixed-center-only correlated-Gaussian scope, the
local inverse-determinant ownership rule, canonical atom creation/erasure,
Block40's stronger-source boundary, and the field-torsor nonselection. It
advances the campaign by replacing the future-center placeholder with an
actual recentered next-step ledger while keeping the horizon, same-domain,
nonlinear, taste, and continuum walls visible.

**Preliminary boundary-map status:** superseded by the authoritative N1--N8
execution in Section 7.

## 7. Authoritative No-Go Discipline N1--N8

The positive theorem contains two narrow negative boundaries:

```text
NG-A: no scalar relabeling/rescaling converts the displayed S^(2) kernel into
      the original anti-Hermitian staggered form in this declared even-site
      chart;

NG-B: the certified strong-to-weak estimates do not supply a same-domain
      composition by the identity map.                            (7.1)
```

Neither statement says that a broader local transformation is impossible or
that the actual orbit lacks unproved enhanced decay.

### N1 — alternative-route enumeration

Every closed-route marker below is one of the required honesty markers. The
attacks are executed against the two exact boundaries in (7.1).

#### N1-A: attacks on the scalar same-form boundary

| attack | marker | executed result |
|---|---|---|
| Choose a new scalar mass `m'` | `ATTEMPTED` | Matching the onsite coefficient sets `m'=mu`, but the offsite term remains Hermitian while the original `M` is anti-Hermitian. |
| Apply a positive scalar field torsor `rho` | `ATTEMPTED` | It multiplies both offsite orientations by the same real magnitude and cannot change the adjoint sign. |
| Apply one global complex field phase | `ATTEMPTED` | The phase cancels between barred and unbarred fields in the quadratic form, leaving `R_2^dagger=R_2`. |
| Kinetic-normalize by one scalar | `ATTEMPTED` | It can set the magnitude `k`, but not convert the symmetric `V+V^dagger` orientation pair to the antisymmetric staggered pair. |
| Reparameterize mass and hopping by two scalars | `ATTEMPTED` | Independent magnitudes still preserve Hermiticity and do not restore the lost original even/odd taste carrier. |
| Add a scalar gauge conjugation | `ATTEMPTED` | Unitary gauge conjugation preserves the Hermitian `*`-class of the kernel. |

#### N1-B: attacks on certified identity composition

| attack | marker | executed result |
|---|---|---|
| Identity-embed the weak output into the next strong input | `ATTEMPTED` | On support size `N`, the certified norm ratio contains the missing positive spatial weight as `exp[(theta_2/2)N]` and is unbounded. |
| Compose only the displayed scalar `q_(2,split)<1` | `ATTEMPTED` | The number multiplies different domain/codomain norms and therefore is not an operator self-contraction. |
| Spend the `G_m`--`G_mu` atom-transition gain | `ATTEMPTED` | `log T_mu` is paid in (0.11); it changes the Gaussian chart but does not replace the missing half spatial weight. |
| Treat one red/provenance root as support-density gain | `ATTEMPTED` | One formal root can carry arbitrarily large support, and evaluated lineage products can fuse to the empty atom. |
| Identify empty atoms with vacuum | `ATTEMPTED` | Hidden-independent retained-field and extended raw coefficients are nonzero and are carried by the split term in (0.16). |
| Use the base gap to manufacture spatial decay | `ATTEMPTED` | `S_next>=mI` controls covariance, not the support-weight difference between the certified spaces. |
| Apply a scalar field normalization after the step | `ATTEMPTED` | It changes Grassmann coefficient weights, not the geometric carrier exponent. |

The following routes are **not foreclosed** by either boundary:

| live route | why it remains outside the executed attacks |
|---|---|
| Coarse-parity/site-dependent phase transform | It may change the hopping `*`-presentation and must be tested with reflection, gauge covariance, seams, and taste. |
| Enlarged Hermitian or general gapped quadratic center | The theorem already uses one such center and does not require original-form return. |
| Taste-faithful hypercube or multicomponent block | It changes the declared carrier rather than applying a scalar relabeling. |
| Auxiliary local first-order factorization | It enlarges variables and needs a new determinant/locality ledger. |
| Actual-orbit enhanced factor decomposition | It may prove better decay than the present certificate records. |
| Small/large cluster split using massive KP slack | It may recover a spatial reserve without embedding the whole completion. |
| Scale-indexed or multiscale norm | It may make the scale shift part of the domain definition. |
| Quantitative nonempty-density plus empty/raw split | It may close a sectorwise same-domain theorem. |

### N2 — wall-independence audit

Use six deliberately nonabsorbing walls:

```text
W1 certified same-domain membership/return,
W2 generic generated-factor/source/provenance closure,
W3 perturbative center update, gap, and normalization,
W4 independent retained-algebra two-mark/nonlinear estimate,
W5 physical taste/chart selection,
W6 chart-relative critical trajectory and observable construction. (7.2)
```

`W4` does not include ball invariance, and `W6` is explicitly relative to a
declared chart, so neither definition silently absorbs another wall.

| pair | close left => right? | close right => left? | independence reason |
|---|---:|---:|---|
| W1--W2 | No | No | Actual-orbit membership does not embed generic sources; a generic factor map need not recover the spatial reserve. |
| W1--W3 | No | No | Spatial return neither selects/gaps a center nor follows from a gapped center. |
| W1--W4 | No | No | Same-domain membership is not a two-mark bound; a two-mark estimate does not embed the codomain. |
| W1--W5 | No | No | Decay does not select taste; taste selection does not prove norm return. |
| W1--W6 | No | No | Massive norm return supplies no critical path; a chart-relative critical construction need not prove this norm embedding. |
| W2--W3 | No | No | Factor/source coordinates change with the center; a center update does not exponentiate generic interactions. |
| W2--W4 | No | No | One-mark factor closure is not a two-mark estimate; a Hessian bound does not supply factor provenance. |
| W2--W5 | No | No | Generated-factor closure does not select a carrier; taste does not supply a Banach factor map. |
| W2--W6 | No | No | Generic locality gives no tuned path; a chart-relative path need not cover generic perturbations. |
| W3--W4 | No | No | Center persistence and nonlinear response are separate estimates. |
| W3--W5 | No | No | A gapped center can be taste-wrong; a taste carrier does not prove a gap. |
| W3--W6 | No | No | One base/perturbative gap is not a tuned trajectory; a chart-relative trajectory does not prove the generic center theorem. |
| W4--W5 | No | No | Nonlinear control does not identify taste; taste does not bound two marks. |
| W4--W6 | No | No | A local two-mark estimate does not tune observables; a chart-relative construction need not be uniform on a ball. |
| W5--W6 | No | No | Physical selection is stronger than a chart-relative construction; the latter may be studied conditionally before selection. |

### N3 — hidden-condition phrase scan

The scan covered the theorem statement, Sections 1--7, the primary runner and
cache, the campaign-local state/backlog surfaces, the campaign-local
`record-faithful-dynamics-completion-20260711/NO_GO_LEDGER.md`, and the related
`staggered-dirac-a1a2-realization-closure-20260710/NO_GO_LEDGER.md`. The local
ledger records four-axiom kinetic nonselection and then preserves live
instrument, larger-carrier, multicomponent, and continuum escapes. Its
kinetic/corner result is a prior unaudited campaign candidate, not retained
authority and not an automatic axiom-stop trigger.

| actual phrase hit | surface | classification | action in this theorem |
|---|---|---|---|
| `canonical` | atom and fiber splits | defined mathematical construction | Conditional expectations and atom projectors are written explicitly; no physical selector is hidden. |
| `background` | gap/locality scope | hidden condition promoted to scope | Uniformity is only over allowed fixed next gauge backgrounds; W3 and W5 remain open. |
| `actual bare range` | headline/result | hidden condition promoted to scope | Fixed to the original Block40 base orbit; generic perturbations remain W2. |
| `strict ultra-massive witness` | numerical certificate | hidden condition promoted to scope | `m=2 10^11` is displayed; no critical or light-mass extrapolation is claimed. |
| `standard 2c` | cluster proof | cited/defined authority | Its two combinatorial uses are named; it is not a physical premise. |
| `physical` | determinant/red factors and taste | non-load-bearing label with ownership definition | “Physical red” means outside the reference ledger, not experimentally selected dynamics. |
| `persistent gap` | title/result | scope-sensitive phrase | Restricted to the exact base center; perturbative persistence remains W3. |
| `same-domain` | boundary statements | negative scope phrase | Means identical certified Banach domain/parameters, not equality of bare formulas. |
| `by construction` | full scanned packet | no hit | No proof is replaced by this phrase. |
| `generic` | exclusions | negative scope phrase | Used only to name unproved perturbation/source extensions. |

No new hidden condition collapses the N2 table.

### N4 — witness and residual matching

| dependency | witness path + line | witness residual | present residual | match? |
|---|---|---|---|---:|
| Gaussian-adapted shortest center | `docs/WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md:71` | Exact two-hop classification, `S^(2)` formula, and `S^(2)>=mI` | New center form and starting gap in (0.1)--(0.2) | Yes |
| Factor-two block/Schur theorem | `docs/MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md:138` | Positive hidden determinant and Schur inverse identity | `A_2>0`, `S_next>=mI`, and determinant phase order | Yes |
| Joint product-reference theorem | `docs/WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md:33` | Local inverse determinant potentials and color-one restore | New Hermitian-sign `C_2,D_2` ledger and response envelope | Yes, after sign recomputation |
| Future-atom strong shadow | `docs/WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md:129` | Actual first output row, empty/raw split, routed factor `68` | `B_40`, current provenance, raw contribution, and strong-to-weak carrier | Yes |
| Related campaign no-go ledger | `.claude/science/physics-loops/staggered-dirac-a1a2-realization-closure-20260710/NO_GO_LEDGER.md:1` | Minimal axioms do not select a kinetic law | Present scalar form mismatch is only chart mathematics, not kinetic nonselection evidence | No positive dependency; boundary preserved |

The present Hermitian determinant minus sign, atom transition, residual
factorization, and shortest recursion are proved anew rather than imported.

### N5 — rhetoric and resolution audit

#### Resolution of NG-A

| resolution | tested? | exact statement supported |
|---|---:|---|
| One oriented edge | Yes | A scalar cannot change the symmetric adjoint pairing into the original antisymmetric pairing. |
| One site / onsite coefficient | Yes | `m'=mu` matches the onsite scalar but leaves the edge mismatch. |
| One momentum mode | Yes | The Hermitian symbol is real/Laplacian-like; a global scalar similarity does not make it the original anti-Hermitian symbol. |
| One factor-two block | Yes | All retained original sites have even staggered parity and the exact kernel is (0.1). |
| Arbitrary finite regulator in the declared chart | Yes | Scalar rescaling and gauge conjugation preserve the `*`-class blockwise. |
| Site-dependent/multicomponent/auxiliary transformations | No | Explicitly not foreclosed and not included in NG-A. |

#### Resolution of NG-B

| resolution | tested? | exact statement supported |
|---|---:|---|
| One factor | Yes | The factor rows close at the declared strong input weight. |
| One connected polymer | Yes | The output estimate pays half spatial weights and the exact raw split. |
| Arbitrarily large support in the certified completion | Yes | The direct identity ratio grows exponentially with the missing support weight. |
| Actual generated base orbit | Partly | One strong-to-weak step is proved; enhanced decay beyond the certificate is untested. |
| Generic perturbation completion | No | W2 and W4 remain open. |
| Same-domain invariant ball | No | Not claimed; membership and a two-mark estimate are still separate. |

The correct rhetoric is epistemic: the certified estimates do not supply a
same-domain composition. They do not prove that the underlying actual map
cannot possess stronger decay or admit another norm.

### N6 — partial closure and primitive scan

The positive closure is substantial: exact `S^(2)` reference migration, new
determinant ownership, actual residual exponentiation, one next
strong-to-weak response, full base Schur gap, and shortest-center recursion.
NG-A removes only scalar same-form relabeling; NG-B removes only composition
by the displayed identity certificate. The live transformations and norm
routes in N1 remain mathematical work, not missing axioms. Activity color,
Gaussian normalization, and the center/raw split are not physical time or a
probability rule.

### N7 — hostile steelman

The strongest objection to NG-A is a coarse-parity-dependent phase or a
multicomponent/taste-faithful change of variables. A bipartite site phase can
alter the apparent Hermitian/anti-Hermitian orientation structure, while a
hypercube carrier can restore information discarded by the even-site block.
An auxiliary first-order factorization may also represent the positive center
locally. These routes defeat any claim broader than **scalar** relabeling in
the declared chart; accordingly NG-A makes no broader claim.

The strongest objection to NG-B is that the actual ultra-massive orbit may
have far more decay than the certified strong norm records. The unused KP
slack, a small/large-cluster decomposition, quantitative nonempty-atom
density, or a scale-indexed norm may close iteration without embedding the
whole weak completion. These routes defeat any claim that same-domain closure
is impossible; accordingly NG-B says only that the present estimates do not
supply it.

### N8 — cross-cycle echo

| prior wall/search hit | retired here? | retirement mechanism | applicability now |
|---|---:|---|---|
| Factor-two taste/form migration wall | No | Taste-faithful/multicomponent block remains live | Prevents calling `S^(2)` the original staggered carrier. |
| Gaussian shortest-center placeholder | Partly | New `G_mu`, atom transition, determinant ledger, and gap recursion | Fixed-base center migration is closed; perturbative update remains W3. |
| Block40 future-center placeholder | Yes at the actual bare base | Recenter `Gamma_40`, exponentiate `P_1`, and construct (0.13) | Same-domain/horizon closure remains W1/W2. |
| Block40 stronger-source boundary | No | Present theorem consumes strong and returns weak | Preserves the non-self-map warning. |
| Fixed-background/reference-provenance wall | Partly | Blocks39--41 give local counterterms and explicit product-atom transition | Generic sources and perturbations remain W2. |
| Field-torsor physical-selection wall | No | No physical normalization is chosen | Preserves W5 and the dynamics-selection residual. |
| Campaign-local record-faithful kinetic-selection ledger | No | `.claude/science/physics-loops/record-faithful-dynamics-completion-20260711/NO_GO_LEDGER.md` was read through its live-escape clauses | Its four-axiom nonselection row has the shape of a possible future selection trigger but remains an unaudited candidate, not retained proof. |
| Related staggered-A1/A2 kinetic/corner ledger | No | `.claude/science/physics-loops/staggered-dirac-a1a2-realization-closure-20260710/NO_GO_LEDGER.md` was searched separately | It is not used as positive evidence for this center theorem. |

The axiom-update stop has an explicit positive trigger. Discussion is required
only after a no-go-discipline-complete result eliminates enlarged gapped
centers, site-dependent and taste-faithful/multicomponent blocks, auxiliary
local first-order/factorized representations, actual enhanced-decay routes,
and scale-indexed/multiscale norms for a reference-independent reason; or if
it proves that physically inequivalent dynamics remain law-admissible while a
unique physical choice is required. Neither condition is established here.
The campaign-local kinetic-nonselection candidate resembles the second shape
but is unaudited and, by its own ledger, leaves live routes; Block41 itself
establishes neither trigger.

**No-Go Discipline status: PASS.**
