---
claim_id: admissibility_dirac_kahler_coboundary_healing_family_bounded_theorem_note_2026-08-19
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md
claim_type: bounded_theorem
claim_scope: "on the displayed Block 105 Dirac--Kahler cover atlas at Lx=4, Tphysical=4, Tcover=8, origins=Z2^2, s_x=3/5, s_t=4/5 with symbolic mass m, the uncorrected forward companion coefficient B_i=quotient_action(d_i)[4:8,0:4] has rank 4 on the two cover-time-EVEN charts (0,0),(0,1), with det_(0,0)=-1303(718239375 m^2-253923671672)/689509800000000 and det_(0,1)=4728571336637/7182393750000, and rank 3 with kernel span(0,1,0,0) and determinant 0 on the two cover-time-ODD charts (1,0),(1,1); Block 137's landed W1 stands untouched because its shipped gate was displayed-edge-only and its 'identically' meant identically in the symbolic mass, with no defect in its certified numbers, while its mechanism attribution is corrected here to cover-time support rather than parity, since atlas-wide the selector dressing's companion correction is zero on 14 of 16 ordered edges — 12 of them because the selector Omega itself vanishes there, plus the displayed (1,0)<->(1,1) pair as the only genuine nonzero-Omega/zero-correction miss — and nonzero exactly on (0,0)->(0,1) and (0,1)->(0,0) with values (0,-+1303/750,0,0), parity-oddness being neither necessary nor sufficient; the coboundary family Omega_ij=(x_j-x_i)Omega* with Omega*=d_(0,0)-d_(1,0) and x=(0,0,1/2,-1/3) makes all 16 dressed edges exactly nilpotent, has atlas curvature 0 of 64, heals the companion to rank 4 on 14 of 16 ordered edges with displayed-edge determinant 1303(9049816125 m^2+2180604558616)/10425388176000000 positive for every real m, and is optimal because the exact cocycle converse forces Omega_ii=0 and leaves the two cover-time-odd self-edges at rank 3; the family lies outside Block 137's selector-projected transition-derived class, the whole effect is s_t-only and linear in s_t and collapses at s_t=0, and no reflection positivity of the healed action, curved OS opening, self-edge resolution, admissibility verdict for coboundary dressings, joint-lane completion, completed ADM/history transporter, joint gravity, gravity constraint quotient beyond the displayed carriers, Records result, retention, axiom amendment, obligation retirement, or TOE percentage movement is established."
depends_on:
  - admissibility_dirac_kahler_twisted_scouting_record_bounded_theorem_note_2026-08-19
  - admissibility_dirac_kahler_connection_residual_theorem_bounded_theorem_note_2026-08-17
runner: scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_twisted_scouting_record_bounded_theorem_note_2026-08-19
target_blocker_text: "The general-Z_N charge-kinematic theorem; parity-mixing dressing classes; the joint-lane program."
source_of_blocker_text: next_trace_action
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Reflection positivity of the healed action; the two forced self-edges; the admissibility class of coboundary dressings; the joint-lane program."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-140 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the chart-anchor determinants, the atlas-wide 14-of-16 correction census, the cover-time mechanism with its two explicit witnesses, the sixteen-edge nilpotency, the 0-of-64 atlas curvature, the 14-of-16 healed companion count, and the rank-13 cocycle converse with its Omega_ii=0 corollary are exact symbolic facts on the displayed atlas and fixtures, so the coboundary healing family and its optimality are theorems there; but reflection positivity of the healed action, the two forced self-edges, and the admissibility of coboundary dressings inside the lane's transition discipline are named and untested, and no curved OS opening follows, so the result is bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Coboundary Healing Family

**Date:** 2026-08-19

**Campaign block:** 141

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited
or retired.

**TOE accounting:** zero obligation retirement. No axiom amendment is
justified. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py`](../scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py)

## 1. Result Up Front

[Block 137](ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md)
closed onto the following `next_trace_action`:

> The general-Z_N charge-kinematic theorem; parity-mixing dressing classes; the joint-lane program.

This note executes the middle item only. It produces an exact dressing-class
result and a mechanism correction, without importing the
general-\(\mathbb Z_N\) theorem or the joint-lane program.

**THE COBOUNDARY HEALING FAMILY.** On the displayed Block 105 cover atlas
with

\[
 \boxed{
  L_x=4,\qquad T_{\mathrm{physical}}=4,\qquad
  T_{\mathrm{cover}}=8,\qquad
  \mathcal O=\mathbb Z_2^2,\qquad
  s_x=\frac35,\quad s_t=\frac45,\quad m\ \text{symbolic},}
                                                               \tag{1}
\]

there is an exact edge-dressing family that simultaneously keeps every
dressed edge nilpotent, removes the atlas curvature entirely, and heals the
forward companion coefficient on every genuine edge. Six facts give the
bounded result.

1. **The chart anchor.** The uncorrected forward companion coefficient

   \[
    B_i:=\mathrm{quotient\_action}(d_i)[4{:}8,\,0{:}4]        \tag{2}
   \]

   is not uniform across the atlas. It has rank 4 on the two
   **cover-time-even** charts, with the exact determinants

   \[
    \boxed{
     \det B_{(0,0)}
      =-\frac{1303\,(718239375\,m^2-253923671672)}
              {689509800000000}},                              \tag{3}
   \]

   \[
    \boxed{
     \det B_{(0,1)}=\frac{4728571336637}{7182393750000}},      \tag{4}
   \]

   and rank 3 with kernel span(0,1,0,0) and determinant 0 on the two
   **cover-time-odd** charts \((1,0)\) and \((1,1)\). Throughout this note
   "healed" means rank 4 after correction. This anchor is new and
   load-bearing: the rank-3 kernel is a property of two charts, not of the
   atlas.
2. **The anchor correction to Block 137.** Block 137's landed W1 stands.
   Its shipped gate was displayed-edge-only, and its word "identically"
   meant identically in the symbolic mass \(m\); there is no defect in its
   certified numbers. What is corrected here, and credited to this round, is
   the **mechanism attribution**. Atlas-wide, the selector dressing's
   companion correction is zero on 14 of 16 ordered edges — 12 of them
   trivially, because the selector \(\Omega\) itself vanishes on those
   edges, plus the displayed pair
   \((1,0)\leftrightarrow(1,1)\) as the only genuine
   nonzero-\(\Omega\)/zero-correction miss — and is **nonzero exactly on**
   \((0,0)\to(0,1)\) and \((0,1)\to(0,0)\), with values

   \[
    \boxed{(0,\ \mp\tfrac{1303}{750},\ 0,\ 0).}                \tag{5}
   \]
3. **The mechanism is cover-time support, not parity.** Parity-oddness is
   neither necessary nor sufficient. It is not necessary: the
   grading-even
   \(\Omega^{*}=d_{(0,0)}-d_{(1,0)}\) has correction
   \((0,\tfrac{1303}{1500},0,0)\) and heals to rank 4. It is not
   sufficient: the parity-mixing \(d_{(1,1)}-d_{(1,0)}\) leaves the read
   column identically zero and the rank stays 3. The displayed selector
   \(\Omega\) is a pure backward time hop, with 4x4 time-block support
   \(\{(1,2),(3,4),(5,6),(7,0)\}\) including the antiperiodic wrap, whose
   quotient-correction block support omits exactly the \((1,0)\) read
   window that the companion consumes.
4. **The healing family theorem.** Let

   \[
    \boxed{
     \Omega_{ij}:=(x_j-x_i)\,\Omega^{*},\qquad
     \Omega^{*}=d_{(0,0)}-d_{(1,0)},\qquad
     x=\Bigl(0,\ 0,\ \tfrac12,\ -\tfrac13\Bigr).}              \tag{6}
   \]

   Then (a) all 16 dressed edges are exactly nilpotent,
   \((d_i+\Omega_{ij})^2=0\); (b) the atlas curvature is 0 of 64, which is
   structural for any coboundary family, down from the selector's 24 of 64;
   (c) the companion has rank 4 on 14 of 16 ordered edges — the correction
   is nonzero on 10 of the 12 genuine edges, zero on the two even-chart
   edges, which are already rank 4, and the only rank-3 leftovers are the
   two forced self-edges \((1,0)\to(1,0)\) and \((1,1)\to(1,1)\); and (d)
   the displayed-edge healed determinant is exactly

   \[
    \boxed{
     \frac{1303\,(9049816125\,m^2+2180604558616)}
           {10425388176000000}},                               \tag{7}
   \]

   positive for all real \(m\).
5. **The cocycle converse theorem, and the hard maximum.** The four-chart
   nerve carries all 16 ordered transitions — a full simplex. The condition

   \[
    \boxed{C_{ijk}:=\Omega_{ik}-\Omega_{jk}-\Omega_{ij}=0}     \tag{8}
   \]

   on all 64 triples is a rank-13 linear system with three-dimensional
   solution space, solved exactly and constructively by the base-chart
   potential

   \[
    \boxed{\Omega_{ij}=c_j-c_i,\qquad
           c_i=\Omega_{(0,0),\,i}.}                            \tag{9}
   \]

   The \(i=j\) triples force \(\Omega_{ii}=0\) for all four charts. Since
   the two cover-time-odd self-edges then keep their rank-3 \(B_i\), **no
   zero-curvature family can heal more than 14 of 16**. The healing family
   in (6) is therefore optimal.
6. **Out-of-class, and the bounded cut.** \(\Omega^{*}\) is not any
   coordinate mask of the displayed full difference — 32 entries violate
   mask membership — and it is not Block 137's selector projection.
   Block 137's in-class scouting verdict therefore stands untouched, and
   the healing family lives outside the transition-derived class.

The parameter boundary is explicit. The healing effect is \(s_t\)-only and
linear in \(s_t\): the displayed correction is
\((0,\ 1303\,s_t/1200,\ 0,\ 0)\), and it collapses exactly at \(s_t=0\),
like the Block 134 and Block 137 residuals. There are two distinct m-riders.
\(\Omega^{*}\)'s own healed determinant on chart \((0,0)\) vanishes at
\(m^2=253923671672/718239375\), while the displayed-edge healed determinant
(7) of the family has no real roots. All counts and ranks are at the
displayed fixtures \(s_x=3/5\), \(s_t=4/5\), with symbolic \(m\).

Three items are named as open toward curved OS and are **not** claimed here:
reflection positivity of the healed action; the two forced self-edges; and
whether coboundary dressings are admissible in the lane's transition
discipline.

The joint-lane program, general-\(\mathbb Z_N\) charge-kinematic theorem,
completed ADM/history transporter, joint gravity, gravity constraint
quotient beyond the displayed carriers, Records, effective audit retention,
axiom amendment or retirement, obligation retirement, and TOE percentage
movement remain outside this theorem.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md), inherited
content-bound through the certified chain. No newer authority claim is made
here, and no audit verdict is imported.

The exact handoff parent is
[Block 137](ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md).
Its next action contains three semicolon-separated items. This note supplies
the parity-mixing dressing-class item only, and supplies it as a mechanism
correction plus an exact positive family. The
general-\(\mathbb Z_N\) charge-kinematic theorem and joint-lane program
remain live, so the parent action is only partially closed.

The exact construction dependency is
[Block 134](ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md).
The solve retains its displayed 32x32 chart differentials, chart gauges,
cover chart matrices, nonuniform Hodge, and antiperiodic quotient without
modification. Neither dependency is assigned an audit verdict here, and
neither has its status altered.

The executed contract is:

1. the displayed \(L_x=4\), physical-time 4, cover-time 8, four-origin
   \(\mathbb Z_2^2\) carrier with 32x32 exact cover matrices, rebuilt to
   rank 16 with \(d_i^2=0\) and no floating-point entries;
2. the exact fixtures \(s_x=3/5\) and \(s_t=4/5\) with symbolic real mass
   \(m\), and the Block 105 eight-shear nonuniform Hodge inherited through
   Block 134;
3. exact reproduction of Block 137's displayed edge anchor: selector rank
   16, \(\Omega^2=0\), \(\{d_i,\Omega\}=0\), \((d_i+\Omega)^2=0\), and
   dressed rank 16;
4. exact reproduction of Block 137's 24-of-64 rank-16 atlas-curvature
   profile before any new claim is tested;
5. the per-chart uncorrected companion coefficients \(B_i\), their ranks,
   kernels, and the two exact cover-time-even determinants (3)--(4);
6. the atlas-wide census of the selector dressing's companion correction
   over all 16 ordered edges, separating the 12 vanishing-\(\Omega\) edges
   from the displayed genuine miss and the two nonzero edges;
7. the exact closed form of the companion correction contracted with the
   kernel direction, together with its dual functionals and their read
   window;
8. the exact rank of those functionals on the grading-even and
   grading-odd dressing layers, giving parity-oddness as neither necessary
   nor sufficient;
9. the two explicit witnesses: grading-even
   \(\Omega^{*}=d_{(0,0)}-d_{(1,0)}\) with correction
   \((0,1303/1500,0,0)\) and healing, and parity-mixing
   \(d_{(1,1)}-d_{(1,0)}\) with identically zero read column and rank 3;
10. the exact time-block support of the displayed selector \(\Omega\),
    identifying the backward hop and the omitted \((1,0)\) read window;
11. the coboundary family (6), its 16 exact edge nilpotency certificates,
    its 0-of-64 atlas curvature, its 14-of-16 healed companion count with
    the two named self-edge leftovers, and the displayed-edge determinant
    (7);
12. the cocycle converse on the complete four-chart nerve: the rank-13
    system, the three-dimensional solution space, the constructive
    base-chart potential (9), and the forced \(\Omega_{ii}=0\);
13. the corollary that 14 of 16 is the hard maximum for any zero-curvature
    family;
14. the out-of-class certificate for \(\Omega^{*}\) against both a
    coordinate mask of the displayed full difference and Block 137's
    selector projection; and
15. one narrow wall W1, leaving reflection positivity, the two forced
    self-edges, the admissibility class of coboundary dressings, and the
    joint-lane program live.

**Independence disclosure.** This block's round ran on the Claude worker
profile, after the codex worker lane exhausted its quota. The round comprises
an Opus solve worker; a fresh Opus checker on a disjoint route built only
from the committed Block 134 and Block 137 machinery, specified to refute,
which independently reproduced Block 137's 24-of-64 curvature profile and
the displayed-edge support before checking any new claim; the prior
checker's gate-body audit of the Block 137 shipped gate; and a supervisor
referee of the 16-edge nilpotency and the 0-of-64 count via the committed
formula, plus line-by-line review. This is cross-context independence within
the same model family, not cross-family independence. Robustness conditions
apply per the workhorse discipline.

The assigned primary runner is the path recorded in the front matter. This
note does not invent a replay footer or a `TOTAL` line. The eight fixed N5
resolution lines are reproduced in Section 9 as the textual contract
specified for that runner.

The scope is the displayed Block 105 atlas and the fixtures above only. No
arbitrary-carrier dressing theorem, general admissibility classification,
reflection-positivity result, curved OS opening, OS no-go, curved OS no-go,
or joint-gravity result follows.

## 3. The Chart Anchor

Let \(\mathcal O=\{(0,0),(0,1),(1,0),(1,1)\}=\mathbb Z_2^2\) be the ordered
chart-origin set, and let \(d_i\) be the inherited chart differentials in the
common physical cover frame. Write the quotient action of a cover operator
\(X\) as in Block 137,

\[
 \mathrm{quotient\_action}(X)
  :=\mathsf q_{\mathrm{AP}}\!\left[
     mH+i\left(HX+X^{\dagger}H\right)\right],                  \tag{10}
\]

and take its forward 4x4 block (2) from the \(t=0\) columns to the \(t=1\)
rows.

The four charts do not behave alike. The exact outcome is

\[
 \boxed{
 \begin{array}{c|c|c|c}
 \text{chart} & \text{cover-time origin} &
 \operatorname{rank}B_i & \det B_i\\\hline
 (0,0) & \text{even} & 4 &
   -\dfrac{1303(718239375\,m^2-253923671672)}{689509800000000}\\
 (0,1) & \text{even} & 4 &
   \dfrac{4728571336637}{7182393750000}\\
 (1,0) & \text{odd} & 3 & 0\\
 (1,1) & \text{odd} & 3 & 0
 \end{array}.}                                                 \tag{11}
\]

On both cover-time-odd charts the kernel is exactly the one-dimensional odd
direction

\[
 \boxed{\ker B_i=\operatorname{span}\{(0,1,0,0)^{\mathsf T}\}
        \qquad(i=(1,0),(1,1)).}                                \tag{12}
\]

This is the anchor that reorganizes the whole question. Block 137 displayed
the pair \((1,0),(1,1)\), so its rank-3 statement is exact for the charts it
displayed. Equation (11) shows that rank 3 is a property of the two
cover-time-odd charts and not of the atlas: two of the four charts already
have an invertible forward companion coefficient before any dressing is
applied.

Throughout this note the word **healed** means exactly one thing: the
corrected forward companion coefficient has rank 4. No positivity,
reflection, or spectral property is meant by it.

The determinant in (3) carries an m-rider and the determinant in (4) does
not. That asymmetry is used in Section 8; it is not evidence about the
family in (6), whose displayed-edge determinant is (7).

## 4. The Anchor Correction To Block 137

Block 137 recorded

\[
 \Delta_\Omega B_{1\leftarrow0}=0                             \tag{13}
\]

"identically" for its displayed edge, with the diagnosis that the
even-parity dressing misses the odd kernel direction. Two separate
statements have to be distinguished.

**The landed wall stands.** The shipped gate was displayed-edge-only, and
its word "identically" meant identically in the symbolic mass \(m\), as
opposed to numerically at \(m=2/7\). Read that way, (13) is exact and there
is no defect in Block 137's certified numbers. Its W1, its 24-of-64
curvature profile, its rank-8 action tail, and its in-class scouting verdict
are unaffected by anything below.

**The mechanism attribution is corrected here, and that correction is
credited to this round.** The atlas-wide census of the same selector
construction over all 16 ordered edges is

\[
 \boxed{
 \begin{array}{c|c|c}
 \text{edge set} & \text{count} & \Delta_\Omega B\\\hline
 \Omega_{ij}=0\ \text{outright} & 12 & 0\ \text{trivially}\\
 (1,0)\leftrightarrow(1,1)\ \text{(the displayed pair)} & 2 &
   0\ \text{with}\ \Omega_{ij}\neq0\\
 (0,0)\to(0,1)\ \text{and}\ (0,1)\to(0,0) & 2 &
   (0,\ \mp\tfrac{1303}{750},\ 0,\ 0)\neq0
 \end{array}.}                                                 \tag{14}
\]

So the correction is zero on 14 of 16 ordered edges and nonzero on exactly
two. Of the 14 zeros, 12 are trivial: the selector \(\Omega_{ij}\) itself
vanishes on those edges, so there is nothing that could have corrected
anything. Only the displayed pair is a genuine
nonzero-\(\Omega\)/zero-correction miss. The blanket reading "this dressing
class never corrects the companion" is therefore not what the construction
does atlas-wide.

The two nonzero edges are the two edges joining the two cover-time-even
charts. That is the first indication of the mechanism, which Section 5
isolates.

None of this reverses (13). The displayed edge really does have zero
correction. What changes is why.

## 5. The Cover-Time Mechanism

The correction, contracted with the kernel direction of (12), is an exact
real-linear functional of the dressing. Splitting a dressing \(\Omega=X+iY\)
into real and imaginary parts, the exact identity is

\[
 \boxed{
  \Delta_\Omega B\,v
   =i\,L_{+}(X)-L_{-}(Y),\qquad
  L_{\pm}(M)=RHMu\pm RM^{\mathsf T}Hu,}                        \tag{15}
\]

with \(u=e_{17}-e_{1}\) and \(R\) the row selector on rows 20 through 23.
The functionals \(L_{\pm}\) read the dressing only through a narrow window
of columns,

\[
 \boxed{\{1,\,17,\,20,\,21,\,22,\,23\},}                       \tag{16}
\]

component \(k\) reading exactly \(\{1,17,20+k\}\). Any dressing supported
off that window contributes zero, whatever its parity.

**Parity-oddness is not necessary.** The grading-even operator

\[
 \boxed{\Omega^{*}:=d_{(0,0)}-d_{(1,0)}}                       \tag{17}
\]

satisfies \(\Gamma\Omega^{*}\Gamma=\Omega^{*}\), has no parity-mixing block
at all, and yet

\[
 \boxed{
  \Delta_{\Omega^{*}}B\,v
   =\Bigl(0,\ \tfrac{1303}{1500},\ 0,\ 0\Bigr)\neq0,}          \tag{18}
\]

with the corrected coefficient reaching rank 4. A grading-even dressing
heals.

**Parity-oddness is not sufficient.** The operator
\(d_{(1,1)}-d_{(1,0)}\) is genuinely parity-mixing — both mixed blocks are
nonzero — has rank 16, and is edge-exact, but

\[
 \boxed{\Delta_{d_{(1,1)}-d_{(1,0)}}B\,v=0}                    \tag{19}
\]

because it leaves the read column identically zero. The rank stays 3. A
parity-mixing dressing need not heal.

**What the displayed selector actually misses.** The displayed \(\Omega\) is
a pure backward time hop. Its 4x4 time-block support is exactly

\[
 \boxed{\{(1,2),\,(3,4),\,(5,6),\,(7,0)\}},                    \tag{20}
\]

the last pair being the antiperiodic wrap. Its quotient-correction block
support omits precisely the \((1,0)\) read window that the companion
consumes. Both terms of \(L_{\pm}\) then vanish identically in \(s_t\), and
(13) follows.

The operative axis is therefore cover-time support, not parity. Equation
(14)'s two nonzero edges and equations (18)--(19) are three independent
checks of the same conclusion, and the two witnesses are on opposite sides
of the parity classification.

This does not say that parity is irrelevant to every question in the lane.
It says that parity is not the axis that decides whether a dressing corrects
this companion coefficient on this atlas.

## 6. The Coboundary Healing Family

Define the family (6) explicitly: with \(\Omega^{*}\) as in (17), the ordered
chart weights

\[
 \boxed{x_{(0,0)}=0,\quad x_{(0,1)}=0,\quad
        x_{(1,0)}=\tfrac12,\quad x_{(1,1)}=-\tfrac13}          \tag{21}
\]

give the edge dressings \(\Omega_{ij}=(x_j-x_i)\Omega^{*}\). Four exact
statements hold.

**(a) Edge nilpotency on all 16 edges.** Every ordered edge satisfies

\[
 \boxed{\Omega_{ij}^{2}=0,\qquad
        \{d_i,\Omega_{ij}\}=0,\qquad
        (d_i+\Omega_{ij})^2=0,\qquad
        \operatorname{rank}(d_i+\Omega_{ij})=16.}              \tag{22}
\]

The displayed two-step cohomology dimension of each dressed edge is
\(32-2(16)=0\).

**(b) Atlas curvature zero.** The exact count is

\[
 \boxed{
  \#\{(i,j,k):C_{ijk}\neq0\}=0\quad\text{out of }64,}          \tag{23}
\]

down from the selector class's 24 of 64. This is structural rather than
accidental: it holds for any coboundary family, by Section 7.

**(c) Companion rank 4 on 14 of 16 ordered edges.** The exact census is

\[
 \boxed{
 \begin{array}{c|c|c}
 \text{edge set} & \text{count} & \text{outcome}\\\hline
 \text{genuine edges with nonzero correction} & 10 &
   \text{rank }4\\
 \text{the two even-chart edges} & 2 &
   \text{correction }0,\ \text{already rank }4\\
 \text{the forced self-edges }(1,0),(1,1) & 2 &
   \text{rank }3
 \end{array}.}                                                 \tag{24}
\]

The two rank-3 leftovers are exactly the self-edges \((1,0)\to(1,0)\) and
\((1,1)\to(1,1)\). Section 7 proves they cannot be avoided.

**(d) The displayed-edge determinant.** On Block 137's displayed edge, the
healed determinant is exactly (7),

\[
 \frac{1303\,(9049816125\,m^2+2180604558616)}
       {10425388176000000},                                    \tag{25}
\]

which is positive for every real \(m\). The family has no mass exclusion on
that edge.

Facts (a) through (d) hold together. That is the content of the result: edge
nilpotency, zero atlas curvature, and companion healing are simultaneously
achievable on this atlas, which no dressing tested before this block had
achieved.

The word "healed" retains its Section 3 meaning. Equation (25) is a
determinant, not a positivity certificate for the action; no reflection
positivity is claimed anywhere in this note.

## 7. The Cocycle Converse And The Hard Maximum

The four-chart nerve here is a **full simplex**: all 16 ordered transitions
are carried, including the four self-transitions. That completeness is what
makes the converse constructive.

**THE COCYCLE CONVERSE THEOREM.** The condition (8),
\(C_{ijk}=\Omega_{ik}-\Omega_{jk}-\Omega_{ij}=0\) on all 64 ordered triples,
is a linear system of exact rank 13 whose solution space is
three-dimensional. Its general solution is the base-chart potential (9),

\[
 \boxed{\Omega_{ij}=c_j-c_i,\qquad
        c_i=\Omega_{(0,0),\,i},}                               \tag{26}
\]

obtained constructively by reading the potential off the base chart. In
particular the \(i=j\) triples force

\[
 \boxed{\Omega_{ii}=0\qquad\text{for all four charts.}}         \tag{27}
\]

Thus zero atlas curvature and the coboundary form are the same condition on
this nerve, which is why (23) is structural.

**COROLLARY — the hard maximum.** Under (27) the self-edge dressed operator
is \(d_i+\Omega_{ii}=d_i\), so the two cover-time-odd self-edges retain
their rank-3 \(B_i\) from (11). Therefore

\[
 \boxed{\text{no zero-curvature family heals more than }14
        \text{ of }16\text{ ordered edges.}}                   \tag{28}
\]

The healing family (6) attains that bound, so it is optimal within the
zero-curvature class.

The corollary is a maximum, not a no-go. It says that if the atlas curvature
is required to vanish, then two self-edges are unavoidably left at rank 3.
It does not say that those two self-edges are physically obstructed, that a
nonzero-curvature family could not reach 15 or 16, or that the rank-3
self-edges block anything downstream. Deciding the two forced self-edges is
one of the named open items.

## 8. Out-Of-Class Status, Riders, And The Bounded Verdict

**Out-of-class.** The generator \(\Omega^{*}\) of (17) is not a coordinate
mask of the displayed full difference \(d_j-d_i\): exactly 32 entries
violate mask membership, being nonzero in \(\Omega^{*}\) while disagreeing
with the corresponding entry of the full difference. Nor is it Block 137's
selector projection \(\Pi_{ij}(d_j-d_i)\). Two consequences follow, and only
these two.

1. Block 137's in-class scouting verdict stands untouched. Nothing here is a
   counterexample to it, because the healing family is not in its class.
2. The healing family lives **outside** the transition-derived dressing
   class. Whether a dressing that is not transition-derived is admissible in
   this lane's transition discipline is a named open question, not an
   assumption made here.

**Riders.** The healing effect is \(s_t\)-only and linear in \(s_t\). The
displayed correction is exactly

\[
 \boxed{
  \Delta_{\Omega^{*}}B\,v
   =\Bigl(0,\ \tfrac{1303\,s_t}{1200},\ 0,\ 0\Bigr),}          \tag{29}
\]

so the whole effect collapses exactly at \(s_t=0\), in the same way as the
Block 134 and Block 137 residuals. There are two m-riders and they point in
opposite directions:

\[
 \boxed{
 \begin{array}{c|c}
 \text{object} & \text{mass boundary}\\\hline
 \Omega^{*}\text{'s own healed determinant on chart }(0,0) &
   \text{vanishes at } m^2=\dfrac{253923671672}{718239375}\\
 \text{the family's displayed-edge determinant (25)} &
   \text{no real roots}
 \end{array}.}                                                 \tag{30}
\]

All ranks, counts, and determinants above are at the displayed fixtures
\(s_x=3/5\), \(s_t=4/5\), with symbolic \(m\).

**The bounded verdict.** The exact displayed outcome is

\[
 \begin{array}{c|c|c}
 \text{test} & \text{exact outcome} & \text{decision}\\\hline
 \text{chart anchor} &
 \text{rank }4\text{ on }(0,0),(0,1);\ \text{rank }3\text{ on }(1,0),(1,1) &
 \textbf{ANCHORED}\\
 \text{Block 137 gate} &
 \text{displayed-edge-only, symbolic in }m &
 \textbf{STANDS}\\
 \text{mechanism} &
 \text{cover-time support, not parity} &
 \textbf{CORRECTED}\\
 \text{edge nilpotency} &
 (d_i+\Omega_{ij})^2=0\ \text{on }16/16 &
 \textbf{EXACT}\\
 \text{atlas square} &
 0/64\ \text{curvature} &
 \textbf{REMOVED}\\
 \text{companion} &
 \text{rank }4\text{ on }14/16 &
 \textbf{HEALED, OPTIMAL}\\
 \text{reflection positivity} &
 \text{not tested} &
 \textbf{OPEN}
 \end{array}                                                   \tag{31}
\]

and the bounded statement is:

\[
 \boxed{\text{On the displayed atlas and fixtures, a coboundary dressing
 family heals every genuine edge companion with zero atlas curvature and
 exact edge nilpotency.}}                                      \tag{32}
\]

Equation (32) opens the named next step. It does **not** claim the curved OS
pipeline. It is not an OS no-go and not a curved OS no-go. Reflection
positivity of the healed action, the two forced self-edges, and the
admissibility class of coboundary dressings are the three exact questions
that follow, and none is answered here.

## 9. No-Go Discipline Gate

There is exactly one bounded family wall.

- W1 — **DISPLAYED-ATLAS COBOUNDARY HEALING / OPTIMALITY AND SCOPE WALL:**
  on the displayed Block 105 atlas at \(s_x=3/5\), \(s_t=4/5\) with symbolic
  \(m\), the coboundary family \(\Omega_{ij}=(x_j-x_i)\Omega^{*}\) with
  \(\Omega^{*}=d_{(0,0)}-d_{(1,0)}\) and \(x=(0,0,1/2,-1/3)\) makes all 16
  dressed edges exactly nilpotent, has atlas curvature 0 of 64, and heals
  the forward companion coefficient to rank 4 on 14 of 16 ordered edges,
  with displayed-edge determinant
  \(1303(9049816125\,m^2+2180604558616)/10425388176000000\) positive for
  every real \(m\). The count 14 of 16 is the exact maximum for any
  zero-curvature family, because the cocycle converse forces
  \(\Omega_{ii}=0\) and the two cover-time-odd self-edges then retain their
  rank-3 coefficient. Block 137's landed wall stands; only its mechanism
  attribution is corrected, from parity to cover-time support. The healing
  family opens the named next step; the curved OS pipeline is not claimed.

W1 is narrow. It concerns the displayed 32x32, four-origin Block 105 atlas,
the inherited nonuniform Hodge and antiperiodic quotient, the exact fixtures
\(s_x=3/5\) and \(s_t=4/5\) with symbolic \(m\), the specific generator
\(\Omega^{*}\), and the specific weights \(x=(0,0,1/2,-1/3)\). It does not
quantify over arbitrary carriers, arbitrary Hodge operators, arbitrary
generators, or other fixtures.

The positive content remains exact inside W1. The chart anchor determinants
are exact rational functions of \(m\); the 16 edge nilpotency certificates
are exact; the 0-of-64 curvature count is exhaustive over ordered triples;
the 14-of-16 companion census is exhaustive over ordered edges; and the
cocycle converse is an exact rank-13 linear statement with a constructive
three-dimensional solution space.

The correction content is equally exact inside W1. The shipped Block 137
gate was displayed-edge-only, with "identically" meaning identically in the
symbolic mass; there is no defect in its certified numbers, and its W1 is
not weakened. What is corrected, and credited to this round, is the
attribution of the mechanism: the operative axis is cover-time support, with
parity-oddness neither necessary nor sufficient.

W1 does not turn the 14-of-16 count into a claim about the two forced
self-edges, does not assert that coboundary dressings are admissible in this
lane's transition discipline, and does not assert reflection positivity of
the healed action. Those three are named open items.

W1 is not an OS no-go and not a curved OS no-go.

There is zero axiom retirement and zero TOE movement. The standard Records,
retention, constitutional, obligation, and end-to-end accounting firewalls
remain in force, and no axiom amendment is justified.

### N1 — Alternative Route Enumeration

Routes are normalized by \((\text{object},\text{mechanism},\text{terminal})\).
The chart anchor, gate audit, mechanism isolation, healing family, cocycle
converse, class placement, riders, and downstream program remain distinct.

1. **(a) CHART ANCHOR ESTABLISHED — the four uncorrected companion
   coefficients / evaluate \(B_i=\mathrm{quotient\_action}(d_i)[4{:}8,0{:}4]\)
   chart by chart / obtain rank 4 with the two exact determinants on the
   cover-time-even charts and rank 3 with kernel span(0,1,0,0) on the
   cover-time-odd charts.** This localizes the rank-3 phenomenon to two
   charts; it does not by itself supply any dressing.
2. **(b) SHIPPED GATE AUDITED — Block 137's zero companion correction /
   re-read its gate body and re-run the same construction over all 16
   ordered edges / find the gate displayed-edge-only and symbolic in \(m\),
   with the correction zero on 14 of 16 edges and nonzero on exactly two.**
   The landed wall stands; only the attribution changes.
3. **(c) MECHANISM ISOLATED — the correction as a functional of the dressing
   / write the exact closed form with its dual functionals and read window,
   then test the grading-even and grading-odd layers / obtain
   parity-oddness as neither necessary nor sufficient, with two explicit
   opposite-parity witnesses.** The operative axis is cover-time support.
4. **(d) HEALING FAMILY PROVED — the coboundary family (6) / verify
   nilpotency, curvature, and companion rank edge by edge and triple by
   triple / obtain 16-of-16 nilpotency, 0-of-64 curvature, 14-of-16 rank 4,
   and a displayed-edge determinant positive for all real \(m\).** This is
   the exact positive route.
5. **(e) COCYCLE CONVERSE PROVED — the complete four-chart nerve / solve
   \(C_{ijk}=0\) on all 64 ordered triples as a linear system / obtain rank
   13, a three-dimensional solution space, the base-chart potential, and
   forced \(\Omega_{ii}=0\).** The corollary is the hard maximum 14 of 16.
6. **(f) OUT-OF-CLASS CERTIFIED — the generator \(\Omega^{*}\) / compare it
   against a coordinate mask of the displayed full difference and against
   Block 137's selector projection / find 32 mask violations and no
   selector-projected form.** Block 137's in-class verdict is untouched and
   the family sits outside that class.
7. **(g) RIDERS LOCATED — the parameter dependence / track \(s_t\) and
   \(m\) through the correction and the determinants / obtain an
   \(s_t\)-only effect linear in \(s_t\), collapsing at \(s_t=0\), one
   generator-level mass root, and no real root for the family's
   displayed-edge determinant.** No wider parameter theorem is imported.
8. **(h) UNTESTED-LIVE — downstream questions / test reflection positivity
   of the healed action, decide the two forced self-edges, decide the
   admissibility class of coboundary dressings, and execute the joint-lane
   program / determine what survives outside W1.** No downstream terminal
   is imported.

The general-\(\mathbb Z_N\) charge-kinematic theorem, completed ADM/history
transporter, joint gravity, and gravity constraint quotient beyond the
displayed carriers remain downstream of row (h). W1 consumes none of those
routes.

### N2 — Wall-Independence Audit

W1 is logically distinct from Block 137's in-class scouting wall and from
Block 134's connection-residual wall, although both notes are explicit
dependencies.

Block 134 supplies the displayed exact chart matrices, gauges, selector
system, conflict operator, nonuniform Hodge, and antiperiodic quotient. Its
terminal is a bounded connection-residual result. It does not evaluate any
per-chart companion coefficient, any atlas-wide correction census, or any
coboundary family.

Block 137 has the selector-projected transition-dressing class as its
object. Its mechanisms are the selector projection, edge anticommutator,
transported atlas square, action tail, and the parity reading of the
displayed dressing. Its terminal is that this class does not open the curved
OS pipeline. That terminal is in-class and is not contradicted here, because
the healing family is out of class.

Block 141 has the displayed atlas's companion coefficients and coboundary
edge dressings as its object. Its mechanisms are the per-chart anchor, the
exact correction functional and its read window, the coboundary
construction, and the cocycle converse on the full nerve. Its terminal is an
exact optimal healing family with zero atlas curvature.

The walls have distinct objects, mechanisms, and terminals:

\[
 \begin{array}{c|c|c|c}
 \text{block} & \text{object} & \text{mechanism} & \text{terminal}\\\hline
 134 & \text{displayed curved connection-residual fixture} &
       \text{selector matching and conflict operator} &
       \text{bounded connection-residual result}\\
 137 & \text{selector-projected transition dressings} &
       \text{projection, edge square, action tail, parity} &
       \text{in-class pipeline not opened}\\
 141 & \text{companion coefficients and coboundary dressings} &
       \text{read window, coboundary, cocycle converse} &
       \text{optimal healing family, curvature }0/64
 \end{array}.                                                  \tag{33}
\]

There is an intentional chain dependency but no proof substitution. Block
134 does not already prove the chart anchor, the correction census, or the
cocycle converse. Block 137 does not already exhibit a healing dressing, and
its class does not contain one. Conversely, Block 141 does not rederive
Block 134's residual result, does not re-prove Block 137's 24-of-64
curvature as a new fact, and does not modify either dependency's audit
status.

The two mechanism statements also remain independent logical objects. Block
137's exact zero correction on its displayed edge and this note's nonzero
correction on the two even-chart edges hold simultaneously; the first is not
refuted by the second.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.
Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| the coboundary healing family | the title's positive result on one displayed atlas |
| displayed block 105 atlas | the inherited four-origin cover carrier, not an arbitrary carrier |
| lx=4, tphysical=4, tcover=8 | the finite cover dimensions in (1) |
| origins=z2^2 | the four ordered chart origins, hence 16 ordered edges and 64 ordered triples |
| s_x=3/5, s_t=4/5, symbolic m | the exact fixtures, with the mass left symbolic |
| 32x32 exact cover matrices | the displayed chart-differential dimension |
| block 105 eight-shear nonuniform hodge | the inherited displayed Hodge, used unmodified |
| b_i=quotient_action(d_i)[4:8,0:4] | the uncorrected forward companion coefficient |
| cover-time-even charts | the two charts (0,0) and (0,1) |
| cover-time-odd charts | the two charts (1,0) and (1,1) |
| rank 4 on the two cover-time-even charts | the new chart anchor |
| det_(0,0) = -1303(718239375 m^2 - 253923671672)/689509800000000 | the exact even-chart determinant with an m-rider |
| det_(0,1) = 4728571336637/7182393750000 | the exact even-chart determinant with no m dependence |
| rank 3 with kernel span(0,1,0,0) | the odd-chart coefficient and its one-dimensional odd kernel |
| healed means rank 4 after correction | the note's fixed definition of healing |
| block 137's landed w1 stands | the anchor being corrected is not weakened |
| the shipped gate was displayed-edge-only | the exact scope of Block 137's companion gate |
| identically meant identically in the symbolic mass | the reading under which Block 137's statement is exact |
| no defect in certified numbers | the audit finding on Block 137's shipped numbers |
| mechanism attribution corrected here | the change credited to this round |
| zero on 14 of 16 ordered edges | the atlas-wide correction census |
| 12 trivially because the selector omega itself vanishes | the trivial part of that census |
| the displayed pair as the only genuine miss | the single nonzero-Omega/zero-correction edge pair |
| nonzero exactly on (0,0)->(0,1) and (0,1)->(0,0) | the two edges joining the cover-time-even charts |
| values (0,-+1303/750,0,0) | the exact corrections on those two ordered edges |
| the mechanism is cover-time support, not parity | the corrected attribution |
| parity-oddness is neither necessary nor sufficient | the two-sided refutation of the parity axis |
| grading-even omega* = d_(0,0) - d_(1,0) | the grading-even witness that heals |
| correction (0,1303/1500,0,0) | the exact correction of that witness |
| parity-mixing d_(1,1) - d_(1,0) | the parity-mixing witness that does not heal |
| leaves the read column identically zero | the exact reason the parity-mixing witness fails |
| pure backward time hop | the displayed selector's cover-time direction |
| time-block support {(1,2),(3,4),(5,6),(7,0)} | the exact 4x4 time-block support, wrap included |
| the antiperiodic wrap | the (7,0) entry of that support |
| omits exactly the (1,0) read window | the precise reason Block 137's correction vanishes |
| omega_ij = (x_j - x_i) omega* | the healing family's definition |
| x = (0, 0, 1/2, -1/3) | the exact ordered chart weights |
| all 16 dressed edges exactly nilpotent | the exhaustive edge certificate |
| (d_i + omega_ij)^2 = 0 | the exact edge nilpotency identity |
| atlas curvature 0/64 | the exhaustive ordered-triple curvature count |
| structural for any coboundary family | the reason the count is not accidental |
| down from the selector's 24/64 | the comparison with the inherited profile |
| companion rank 4 on 14/16 ordered edges | the exhaustive healed-edge census |
| nonzero on 10 of the 12 genuine edges | the correction census inside the family |
| zero on the two even-chart edges which are already rank 4 | the two edges needing no correction |
| the two forced self-edges (1,0)->(1,0), (1,1)->(1,1) | the only rank-3 leftovers |
| displayed-edge healed determinant 1303(9049816125 m^2 + 2180604558616)/10425388176000000 | the exact healed determinant |
| positive for all real m | the mass reach of that determinant |
| the four-chart nerve carries all 16 ordered transitions | the full-simplex premise of the converse |
| c_ijk = omega_ik - omega_jk - omega_ij = 0 on all 64 triples | the exact zero-curvature condition |
| rank-13 linear system | the exact rank of that system |
| three-dimensional solution space | the exact solution dimension |
| base-chart potential omega_ij = c_j - c_i | the constructive general solution |
| the i=j triples force omega_ii = 0 | the self-edge consequence |
| no zero-curvature family can heal more than 14/16 | the hard maximum corollary |
| the healing family is optimal | attainment of that maximum, not a no-go |
| omega* is not any coordinate mask of the displayed full difference | the out-of-class certificate, with 32 violating entries |
| not block 137's selector projection | the second half of the out-of-class certificate |
| block 137's in-class scouting verdict stands untouched | the class boundary that prevents any contradiction |
| the healing family lives outside the transition-derived class | the exact placement of the new family |
| the healing effect is s_t-only and linear in s_t | the exact parameter reach |
| displayed correction (0, 1303 s_t/1200, 0, 0) | the exact symbolic form of that reach |
| collapses exactly at s_t = 0 | the degeneration shared with Block 134 and Block 137 |
| m^2 = 253923671672/718239375 | the generator-level mass root on chart (0,0) |
| the displayed-edge healed determinant has no real roots | the family-level mass statement |
| reflection positivity of the healed action | named next, not claimed |
| the two forced self-edges | named next, not resolved |
| the admissibility class of coboundary dressings | named next, not decided |
| the joint-lane program | future execution, not a consequence of this theorem |
| general-z_n charge-kinematic theorem | the untouched first item from Block 137's next action |
| curved os is not claimed | the explicit pipeline boundary |
| not an os no-go | explicit prohibition on an OS-wide upgrade |
| not a curved os no-go | explicit prohibition on a curved-OS-wide upgrade |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not completed |
| gravity constraint quotient beyond the displayed carriers | outside the present scope |
| records | no Records claim |
| retention | independent-audit firewall |
| axiom amendment | explicitly not justified |
| zero axiom retirement | no axiom is removed by this theorem |
| obligation retirement | TOE accounting firewall |
| toe percentage movement | TOE accounting firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting statement |
| no toe percentage moves | TOE accounting statement |
| retained-positive end-to-end theory count remains zero | audit accounting |
| cross-context independence, same model family | the exact independence disclosure for this round |
| fresh checker on a disjoint committed-machinery route | the refutation-specified independent check |
| supervisor referee of the 16-edge nilpotency and the 0/64 count | the third review layer |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | the first five N5 keys |
| result decision_cut toe | the final three N5 keys |
| no-go discipline verdict | the adjudication at the end of N8 |
| pass only for narrow w1 | no broader positive or negative terminal |
| block 137's numbers were wrong | forbidden misreading of the displayed-edge-only gate audit |
| the selector class heals the companion | forbidden erasure of the out-of-class certificate |
| parity-mixing dressings heal the companion | forbidden restoration of the refuted parity axis |
| every edge heals, therefore the atlas is healed | forbidden deletion of the two forced self-edges |
| the healed action is reflection positive | forbidden upgrade of a determinant into a positivity certificate |
| the curved os pipeline is open | forbidden upgrade of W1's bounded positive |
| coboundary dressings are admissible | forbidden assumption of the named open admissibility question |

No phrase promotes the 14-of-16 count into a full 16-of-16 healing. No
phrase converts the positive displayed-edge determinant into reflection
positivity, an action-positivity certificate, or a curved OS opening.
Nothing claims that the two forced self-edges are resolved.

Nothing says Block 137's certified numbers were defective, and nothing says
its in-class verdict is contradicted. Nothing restores parity as the
operative axis. Nothing asserts that coboundary dressings are admissible in
the lane's transition discipline, that the general-\(\mathbb Z_N\) theorem is
proved, that the joint lane is executed, that the transporter is completed,
that joint gravity holds, or that a gravity constraint quotient beyond the
displayed carriers exists. Nothing asserts axiom amendment or retirement,
effective audit retention, obligation retirement, or TOE percentage
movement.

### N4 — Residual Matching

The Block 137 `next_trace_action`, quoted exactly, is:

> The general-Z_N charge-kinematic theorem; parity-mixing dressing classes; the joint-lane program.

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 137 next action](ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md) | “The general-Z_N charge-kinematic theorem; parity-mixing dressing classes; the joint-lane program.” | **PARTIALLY DISCHARGED:** the dressing-class item is answered on the displayed atlas by an exact optimal healing family, with parity refuted as the operative axis; the general-\(\mathbb Z_N\) theorem and the joint-lane program remain live |
| [Block 137](ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md) | the companion non-healing gate and its parity diagnosis | **WALL STANDS, MECHANISM CORRECTED:** the shipped gate was displayed-edge-only and symbolic in \(m\), with no defect in its certified numbers; atlas-wide the correction is zero on 14 of 16 edges and nonzero on exactly two, so the operative axis is cover-time support |
| [Block 134](ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md) | the displayed chart matrices, Hodge, and quotient used by the assigned solve | **CONSUMED UNMODIFIED:** the anchor, census, family, and converse are computed on those exact inherited objects, and its audit status is unchanged |
| dressing-class terminal | decide whether some dressing class heals the companion while keeping the edges exact | **ANSWERED ON THE DISPLAYED ATLAS:** a coboundary family attains 16-of-16 nilpotency, 0-of-64 curvature, and 14-of-16 rank 4, which the cocycle converse proves optimal |
| worker solve plus fresh checker and supervisor referee | chart anchor, correction census, read window, family certificates, converse, out-of-class certificate, riders | **INCORPORATED WITH NAMED BOUNDARY:** all positives and the corrected attribution are recorded; reflection positivity, the two forced self-edges, and coboundary admissibility remain explicit open items |

Block 137's parity-mixing dressing-class item — **ANSWERED ON THE DISPLAYED
ATLAS, WITH THE AXIS CORRECTED.** A dressing class that heals the companion
while keeping every edge exact exists and is exhibited; the class that does
it is grading-even, so parity-mixing is not the operative axis.

The closure is partial because the exact source gate has three items. The
general-\(\mathbb Z_N\) charge-kinematic theorem and the joint-lane program
are not executed. The dressing-class item also opens a new bounded branch
rather than closing every question: reflection positivity, the two forced
self-edges, and the admissibility of coboundary dressings remain live.

The exact replacement residual is:

> Reflection positivity of the healed action; the two forced self-edges; the admissibility class of coboundary dressings; the joint-lane program.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the displayed Block 105 atlas at
\(s_x=3/5\), \(s_t=4/5\) with symbolic \(m\), the uncorrected forward
companion coefficient is rank 4 on the two cover-time-even charts and rank 3
with kernel span(0,1,0,0) on the two cover-time-odd charts; Block 137's
landed wall stands, with its gate displayed-edge-only and symbolic in the
mass, while its mechanism attribution is corrected to cover-time support
because atlas-wide the selector correction is zero on 14 of 16 ordered edges
and nonzero on exactly the two edges joining the cover-time-even charts, and
because parity-oddness is neither necessary nor sufficient; the coboundary
family \(\Omega_{ij}=(x_j-x_i)(d_{(0,0)}-d_{(1,0)})\) with
\(x=(0,0,1/2,-1/3)\) makes all 16 dressed edges exactly nilpotent, has atlas
curvature 0 of 64, and heals the companion to rank 4 on 14 of 16 ordered
edges with a displayed-edge determinant positive for every real \(m\), which
the exact cocycle converse proves optimal because \(\Omega_{ii}=0\) is
forced; the family lies outside Block 137's transition-derived class, the
whole effect is \(s_t\)-only and linear in \(s_t\), and reflection
positivity, the two forced self-edges, the admissibility of coboundary
dressings, and the curved OS pipeline are not claimed.”

Forbidden upgrades include:

- “Block 137's certified numbers were wrong”;
- “the selector-projection class heals the companion after all”;
- “parity-mixing is what heals the companion”;
- “the healing family heals all 16 ordered edges”;
- “the positive displayed-edge determinant is reflection positivity of the
  healed action”;
- “the curved OS pipeline is open”; and
- “coboundary dressings are admissible in the lane's transition discipline”.

The first misreads a displayed-edge-only, mass-symbolic gate as a numerical
defect. The second erases the out-of-class certificate for
\(\Omega^{*}\). The third restores the axis refuted by the two
opposite-parity witnesses. The fourth deletes the two forced self-edges and
contradicts the hard maximum. The fifth confuses an invertibility
determinant with a positivity certificate. The sixth upgrades a bounded
edge-and-curvature result into a pipeline claim. The seventh assumes the
named open admissibility question.

Also forbidden are “the two forced self-edges are resolved,” “a
nonzero-curvature family is proved impossible,” “the result holds at other
fixtures or other carriers,” “the general-\(\mathbb Z_N\) theorem is
complete,” “the joint-lane program is complete,” “the ADM/history
transporter is complete,” “the gravity constraint quotient is complete
beyond the displayed carriers,” and any claim of effective audit retention,
obligation retirement, or TOE movement. None is established here.

The runner's eight N5 resolution lines are reproduced verbatim:

```text
N5: per_element: the uncorrected companion B_i=quotient_action(d_i)[4:8,0:4] is rank 4 on the two cover-time-EVEN charts, det_(0,0)=-1303(718239375 m^2-253923671672)/689509800000000 and det_(0,1)=4728571336637/7182393750000, and rank 3 with kernel span(0,1,0,0) and det 0 on the two cover-time-ODD charts
per_site: atlas-wide the selector dressing's companion correction is zero on 14/16 ordered edges -- 12 trivially because Omega itself vanishes there, plus the displayed (1,0)<->(1,1) pair as the only genuine miss -- and nonzero exactly on (0,0)->(0,1) and (0,1)->(0,0) with values (0,-+1303/750,0,0); Block 137's landed W1 stands, its gate having been displayed-edge-only and symbolic in m
per_mode: the mechanism is cover-time support, not parity: the grading-even Omega*=d_(0,0)-d_(1,0) corrects by (0,1303/1500,0,0) and heals to rank 4, the parity-mixing d_(1,1)-d_(1,0) leaves the read column identically zero at rank 3, and the displayed backward-hop selector with time-block support {(1,2),(3,4),(5,6),(7,0)} omits exactly the (1,0) read window
per_block: Omega_ij=(x_j-x_i)Omega* with x=(0,0,1/2,-1/3) gives (d_i+Omega_ij)^2=0 on all 16 edges, atlas curvature 0/64 (down from 24/64), companion rank 4 on 14/16 ordered edges, and displayed-edge det 1303(9049816125 m^2+2180604558616)/10425388176000000 positive for all real m
lattice_wide: on the full four-chart nerve C_ijk=0 on all 64 triples is a rank-13 system with three-dimensional solution space Omega_ij=c_j-c_i, the i=j triples force Omega_ii=0, and the two cover-time-odd self-edges then stay rank 3, so 14/16 is the exact maximum and the family is optimal
RESULT: on the displayed atlas and fixtures a coboundary dressing family heals every genuine edge companion with exact edge nilpotency and zero atlas curvature, lies outside Block 137's transition-derived class, and is s_t-only and linear in s_t
DECISION_CUT: test reflection positivity of the healed action; decide the two forced self-edges; decide the admissibility class of coboundary dressings; execute the joint-lane program; curved OS is not claimed
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The note uses the inherited chart
matrices, gauges, cover frames, nonuniform Hodge, antiperiodic quotient,
companion convention, and exact scalar arithmetic. No dressing-admissibility
axiom, coboundary axiom, positivity axiom, or self-edge axiom is adopted.

| route | present status | remaining terminal |
|---|---|---|
| chart \((0,0)\) companion | rank 4, determinant (3) | its own mass root is a generator-level rider, not a family statement |
| chart \((0,1)\) companion | rank 4, determinant (4), no \(m\) dependence | no claim about other charts follows |
| chart \((1,0)\) companion | rank 3, kernel span(0,1,0,0) | dressing is required before this coefficient is invertible |
| chart \((1,1)\) companion | rank 3, kernel span(0,1,0,0) | same, and it is one of the two forced self-edges |
| Block 137 shipped gate | **DISPLAYED-EDGE-ONLY, SYMBOLIC IN m** | no defect in its certified numbers; its W1 is unchanged |
| atlas-wide correction census | zero on 14 of 16, nonzero on exactly two | the census is exhaustive on this atlas only |
| correction functional | exact closed form with read window \(\{1,17,20,21,22,23\}\) | no claim about other blocks of the quotient action |
| parity as the axis | **REFUTED IN BOTH DIRECTIONS** | parity remains relevant to other questions, not to this one |
| cover-time support as the axis | exhibited by two opposite-parity witnesses and the displayed hop support | no general theorem about other carriers' time supports |
| edge nilpotency of the family | exact on all 16 ordered edges | no claim about dressings outside the family |
| atlas curvature of the family | 0 of 64 | structural for coboundary families on this nerve |
| companion healing of the family | rank 4 on 14 of 16 | the two forced self-edges remain rank 3 |
| displayed-edge determinant | (7), positive for all real \(m\) | positivity of a determinant is not action positivity |
| cocycle converse | rank 13, three-dimensional solution space, \(\Omega_{ii}=0\) forced | nonzero-curvature families are not classified here |
| hard maximum | 14 of 16 for any zero-curvature family | this is a maximum, not an impossibility result |
| out-of-class certificate | 32 mask violations; not the selector projection | Block 137's in-class verdict is untouched |
| parameter dependence | \(s_t\)-only and linear in \(s_t\) | everything collapses at \(s_t=0\) |
| reflection positivity of the healed action | **UNTESTED-LIVE** | test without importing a curved OS opening |
| the two forced self-edges | **UNTESTED-LIVE** | decide whether they obstruct anything downstream |
| admissibility of coboundary dressings | **UNTESTED-LIVE** | decide inside the lane's transition discipline |
| joint-lane program | **UNTESTED-LIVE** | execute without importing transporter or gravity completion |
| general-Z_N theorem | **UNTESTED-LIVE** | prove for its stated range of \(N\) |
| actual ADM/history transporter | not executed | complete beyond the displayed packages |
| gravity constraint quotient | displayed carriers only | execute beyond those carriers |

The exact Block 137 next action is therefore partially closed. Its
dressing-class item has an exact positive answer with a corrected mechanism,
while its general-\(\mathbb Z_N\) and joint-lane items remain live, and the
new open items are explicit rather than silently absorbed.

### N7 — Steelman

**Hostile steelman: this note contradicts its own anchor, since Block 137
proved the companion correction vanishes identically.** A later block cannot
exhibit a nonzero correction from the same construction.

Rejected by reading the shipped gate. That gate is displayed-edge-only, and
its "identically" is identically in the symbolic mass \(m\). Under that
reading it is exact, and this note reproduces it: the displayed edge really
does have zero correction. The atlas-wide census (14) adds edges the gate
never covered. Both statements hold simultaneously, and Block 137's
certified numbers are untouched.

**Hostile steelman: the healing family is a counterexample to Block 137's
in-class verdict.** It heals a companion that Block 137 said the dressing
could not heal.

Rejected by the out-of-class certificate. \(\Omega^{*}\) is not a coordinate
mask of the displayed full difference — 32 entries violate mask membership —
and it is not \(\Pi_{ij}(d_j-d_i)\). Block 137's verdict is quantified over
its selector-projected class, and the healing family is not in that class.
Nothing here is a counterexample to it.

**Hostile steelman: the corrected mechanism is a distinction without a
difference, since the healing dressing could just be described as
parity-mixing.** Any operator with a nonzero correction can be relabeled.

Rejected by the two explicit witnesses. \(\Omega^{*}\) satisfies
\(\Gamma\Omega^{*}\Gamma=\Omega^{*}\) with no parity-mixing block at all, and
it heals. The genuinely parity-mixing \(d_{(1,1)}-d_{(1,0)}\) has rank 16 and
is edge-exact, and it does not heal. The two witnesses sit on opposite sides
of the parity classification with opposite outcomes, so parity is neither
necessary nor sufficient. The read window (16) and the displayed hop support
(20) identify the axis that does decide.

**Hostile steelman: 14 of 16 is an admission of failure dressed up as
optimality.** Two edges are still rank 3.

Rejected by the converse. On the full four-chart nerve, zero atlas curvature
forces \(\Omega_{ii}=0\), so the self-edge dressed operator is \(d_i\)
itself, and the two cover-time-odd charts keep their rank-3 coefficient by
the anchor (11). Fourteen is therefore the exact maximum available to any
zero-curvature family, and the exhibited family attains it. This is a
maximum, not a proof that those two edges can never be handled by other
means; deciding them is a named open item.

**Hostile steelman: a determinant positive for all real \(m\) is a
positivity result, so reflection positivity follows.** The healed action has
a positive invariant.

Rejected as a category error. Equation (25) is the determinant of one 4x4
forward companion block; it certifies invertibility on that edge for every
real mass. Reflection positivity is a statement about the healed action and
its reflection, and it is not tested anywhere in this note. It is listed as
the first named open item precisely because it does not follow.

**Hostile steelman: zero atlas curvature plus edge nilpotency plus a healed
companion is exactly the curved OS pipeline, so the pipeline is open.** All
three obstructions Block 137 recorded have been removed.

Rejected by scope. Block 137's three in-class obstructions were the atlas
square, the action tail, and the companion. This note removes the curvature
and heals the companion within a different class on the displayed atlas. It
does not establish reflection positivity, does not resolve the two forced
self-edges, and does not decide whether coboundary dressings are admissible
in this lane's transition discipline. W1 is a bounded positive on one
displayed atlas, not a pipeline claim; it is not an OS no-go and not a
curved OS no-go either.

**Hostile steelman: the whole effect is an artifact of the fixtures, since
it collapses at \(s_t=0\).** A result that vanishes on a parameter slice is
not structural.

Rejected as a correctly stated rider rather than a defect. The
\(s_t\)-linearity in (29) is disclosed exactly, and the collapse at
\(s_t=0\) is shared with the Block 134 and Block 137 residuals, so it is a
property of the inherited construction rather than of this dressing. All
ranks and counts are stated at the displayed fixtures with symbolic \(m\),
and no wider parameter theorem is claimed.

**Hostile steelman: a same-model-family checker is not independence, so the
round is unaudited self-confirmation.** The disclosure concedes the point.

Rejected as a misreading of what is claimed. The disclosure states
cross-context independence within the same model family, explicitly not
cross-family independence, and it names the disjoint committed-machinery
route, the refutation specification, the reproduction of Block 137's
24-of-64 profile before any new claim was checked, the prior checker's
gate-body audit, and the supervisor referee. No audit verdict is imported
and no retention is asserted; independent audit alone may assign one.

These steelmen preserve narrow W1. They keep the gate-reading, class
placement, mechanism axis, optimality bound, positivity boundary, parameter
rider, and independence scope visible.

### N8 — Cross-Cycle Echo

The curved transition chain now moves from Block 134's displayed
connection-residual fixture through Block 137's in-class scouting record to
an explicit out-of-class family that heals what the in-class dressing could
not. The parent's wall stands; what changes is the reason it stood, and the
discovery that a different class does better.

| source | narrowing that leads to W1 and the next decision |
|---|---|
| [Block 134](ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md) | supplies the displayed exact chart, gauge, Hodge, and quotient data, consumed unmodified |
| [Block 137](ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md) | names parity-mixing dressing classes as the next class, supplies the 24-of-64 curvature profile and the companion gate, and remains the exact trace target |
| per-chart companion anchor | localizes rank 3 to the two cover-time-odd charts and exhibits the two even-chart determinants |
| atlas-wide correction census | shows the correction zero on 14 of 16 edges and nonzero on exactly the two even-chart edges |
| exact correction functional | supplies the read window that decides which dressings can contribute at all |
| two opposite-parity witnesses | refute parity as necessary and as sufficient in the same round |
| displayed hop support | identifies the backward time hop and the omitted read window as the reason the parent gate read zero |
| coboundary construction | supplies 16-of-16 edge nilpotency, 0-of-64 curvature, and 14-of-16 healed companions |
| cocycle converse on the full nerve | forces \(\Omega_{ii}=0\) and proves 14 of 16 is the hard maximum |
| out-of-class certificate | keeps Block 137's in-class verdict intact and places the family outside the transition-derived class |
| fresh independent checker and supervisor referee | reproduce the inherited profile on a disjoint route, audit the parent gate body, and referee the new counts |

The echo is bounded and positive. The parent's in-class negative and this
block's out-of-class positive are compatible, and the mechanism correction
explains both at once. The next branch must decide positivity, the two
forced self-edges, and admissibility, not restate the healing counts as a
pipeline.

**No-Go Discipline verdict:** **PASS** only for narrow W1. **ANCHOR
ESTABLISHED** for the per-chart companion profile, rank 4 with the two exact
determinants on the cover-time-even charts and rank 3 with kernel
span(0,1,0,0) on the cover-time-odd charts. **PARENT WALL STANDS** because
Block 137's shipped gate was displayed-edge-only with "identically" meaning
identically in the symbolic mass, with no defect in its certified numbers.
**MECHANISM CORRECTED** to cover-time support, with the correction zero on
14 of 16 ordered edges, nonzero on exactly the two even-chart edges with
values \((0,\mp1303/750,0,0)\), and parity-oddness neither necessary nor
sufficient. **FAMILY PROVED** for
\(\Omega_{ij}=(x_j-x_i)(d_{(0,0)}-d_{(1,0)})\) with \(x=(0,0,1/2,-1/3)\):
16-of-16 exact edge nilpotency, 0-of-64 atlas curvature, companion rank 4 on
14 of 16 ordered edges, and displayed-edge determinant positive for every
real \(m\). **OPTIMALITY PROVED** by the rank-13 cocycle converse and its
forced \(\Omega_{ii}=0\). **OUT-OF-CLASS** for \(\Omega^{*}\) against both a
coordinate mask of the displayed full difference and the selector
projection. **BOUNDARY** for the displayed Block 105 atlas, the fixtures
\(s_x=3/5\) and \(s_t=4/5\) with symbolic \(m\), and the \(s_t\)-only,
\(s_t\)-linear reach that collapses at \(s_t=0\). **LIVE** for reflection
positivity of the healed action, the two forced self-edges, the
admissibility class of coboundary dressings, the general-\(\mathbb Z_N\)
theorem, and the joint-lane program. **FAIL** for “Block 137's numbers were
defective,” “the selector class heals,” “parity-mixing is the operative
axis,” “all 16 edges are healed,” “the determinant is reflection
positivity,” “the curved OS pipeline is open,” “coboundary dressings are
admissible,” an OS no-go, a curved OS no-go, a completed joint lane or
transporter, joint gravity, a gravity constraint quotient beyond the
displayed carriers, axiom necessity or retirement, effective audit
retention, obligation retirement, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment or retirement is justified. The chart matrices, gauges,
cover frames, nonuniform Hodge, antiperiodic quotient, companion convention,
and exact scalar arithmetic are inherited data. Exhibiting a coboundary
dressing family inside those data uses exact matrix algebra, ranks,
determinants, supports, and one finite linear system; it adds no dressing
axiom.

The corrected mechanism is not elevated into an axiom either. Cover-time
support is identified as the operative axis for this companion coefficient
on this atlas, by an exact read window and two opposite-parity witnesses. No
principle is adopted that cover-time support governs other blocks, other
carriers, or other questions in the lane.

The healing family is not adopted as a preferred connection. It is an exact
exhibit that attains the zero-curvature maximum on the displayed atlas.
Whether such a dressing is admissible in this lane's transition discipline
is left open, and no admissibility convention is amended to accommodate it.

Nor is the hard maximum turned into a no-go. The corollary constrains
zero-curvature families only; it does not decree that the two forced
self-edges are physically obstructed or that no other construction can
address them.

The positive displayed-edge determinant likewise requires no constitutional
change. It certifies invertibility for every real mass on that edge and
nothing more. Reflection positivity of the healed action is untested, so no
positivity claim enters the accounting.

This is bounded route closure, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero axiom retirement;
- zero obligation retirement;
- zero TOE movement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

Axiom retirement is zero, TOE movement is zero, the standard firewalls are
unchanged, and no axiom amendment is justified.

## 11. Next Decision

The shortest high-value sequence is:

1. test reflection positivity of the healed action for the exhibited
   coboundary family, without importing a curved OS opening from the edge,
   curvature, and companion results already proved;
2. decide the two forced self-edges \((1,0)\to(1,0)\) and
   \((1,1)\to(1,1)\), which the cocycle converse shows no zero-curvature
   family can heal, and determine whether they obstruct anything downstream;
3. decide whether coboundary dressings are admissible in this lane's
   transition discipline, since the healing family is not transition-derived
   and sits outside Block 137's selector-projected class; and
4. execute the joint-lane program without assuming positivity, self-edge
   resolution, admissibility, the general-\(\mathbb Z_N\) theorem,
   transporter completion, a gravity quotient, or joint gravity.

The exact next gate is: “Reflection positivity of the healed action; the two
forced self-edges; the admissibility class of coboundary dressings; the
joint-lane program.”

Block 137's parity-mixing dressing-class item is answered on the displayed
atlas: a healing class exists, it is optimal among zero-curvature families,
and the operative axis is cover-time support rather than parity. Block 137's
landed wall stands, and its certified numbers are unaffected. The
general-\(\mathbb Z_N\) charge-kinematic theorem and the joint-lane program
remain untouched.

The actual ADM/history transporter remains unexecuted beyond the displayed
packages. Nothing in the chart anchor, correction census, edge nilpotency,
zero atlas curvature, healed companion counts, or cocycle converse supplies
its completion.

The gravity constraint quotient remains unexecuted beyond the displayed
carriers.
