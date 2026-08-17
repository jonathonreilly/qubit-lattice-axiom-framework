---
claim_id: admissibility_dirac_kahler_time_dressing_adjointness_wall_bounded_theorem_note_2026-08-17
claim_type: bounded_theorem
claim_scope: "on the certified package at both rational shear fixtures, the time direction is genuinely visible to the quotient (both displayed conjugation families have distinct translates), the monodromy-conjugated family has exactly empty descent while the shift-conjugated family carries at zero momentum a genuine nonzero descending member — identically vanishing leakage and nonzero quotient compression, the first current-derived operator to reach the quotient — which however fails reflection-adjointness exactly, and the joint descent-plus-adjointness solve is empty in both families, their union, and the displayed two-time class, so the observable wall rests on the reflection-adjointness condition alone, isolated as the single blocking axiom for the displayed classes, with the solve lane's leakage-injectivity mechanism refuted as lift-dependent and recorded; and reflection-compatible observable classes, Q-modification, the naturality classification, the curved-carrier dependency, the completed ADM/history transporter, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_spatial_dressing_invisibility_bounded_theorem_note_2026-08-17
runner: scripts/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_spatial_dressing_invisibility_bounded_theorem_note_2026-08-17
target_blocker_text: "Time-smeared and transfer-conjugated dressings for the observable wall; the naturality classification of the swap completion; curved OS positivity on the half-space package."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "The naturality classification of the swap completion; the curved-carrier dependency (the Block 105 common differential); reflection-compatible observable classes."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-125 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact time-translate visibility, exact rank-eight empty descent for the displayed monodromy-conjugated family, exact rank-seven zero-momentum descent with a one-dimensional kernel for the displayed shift-conjugated family, identically vanishing leakage and nonzero quotient compression of its normalized kernel member, exact nonzero reflection-adjointness residual, exact emptiness of every displayed joint descent-plus-adjointness solve, and exact lift-dependence refutation of leakage injectivity on the certified package at both rational shear fixtures; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Time-Dressing Descent And The Adjointness Wall

**Date:** 2026-08-17

**Campaign block:** 126

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.py`](../scripts/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.py)

## 1. Result Up Front

[Block 125](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md)
closed onto the following handoff next gate, anchored byte-exactly at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md:16`
and elaborated in its Next Decision:

> Time-smeared and transfer-conjugated dressings for the observable wall;
> the naturality classification of the swap completion; curved OS positivity
> on the half-space package.

**THE DUAL-FAMILY TIME-DRESSING THEOREM.** Fix either rational shear
fixture $s\in\{5/13,3/5\}$ and a certified momentum block $k$. Let
$D_{k,s}$ be the inherited routed current block, let $M_{k,s}$ be the
displayed monodromy lift, and let $S_{k,s}$ be the displayed time-shift
lift. For $t\in\mathbb Z_8$, put

\[
 D_{k,s}^{M,[t]}
 :=M_{k,s}^{-t}D_{k,s}M_{k,s}^{t},
 \qquad
 D_{k,s}^{S,[t]}
 :=S_{k,s}^{-t}D_{k,s}S_{k,s}^{t}.              \tag{1}
\]

The two displayed eight-weight families are

\[
 \mathcal D_{k,s}^{M}(a)
 :=\sum_{t=0}^{7}a_tD_{k,s}^{M,[t]},
 \qquad
 \mathcal D_{k,s}^{S}(b)
 :=\sum_{t=0}^{7}b_tD_{k,s}^{S,[t]},
 \quad a,b\in\mathbb K_s^8.                    \tag{2}
\]

Both families are genuinely time-visible. In each family at each fixture,
at least two displayed translates have unequal quotient data. Thus the
scalar-phase cancellation which collapsed the spatial family in Block 125
does not recur.

Let $\Lambda_{k,s}^{M}$ and $\Lambda_{k,s}^{S}$ be the exact stacked
null-leakage maps of the two weight vectors. The monodromy-lift certificate
is

\[
 \operatorname{rank}_{\mathbb K_s}\Lambda_{k,s}^{M}=8
 \quad\text{at every certified }(k,s),
 \qquad
 \ker\Lambda_{k,s}^{M}=\{0\}.                  \tag{3}
\]

Therefore Family A contains no nonzero descending member anywhere on the
certified package.

Family B breaks that terminal at zero momentum. Its certified leakage map
obeys

\[
 \operatorname{rank}_{\mathbb K_s}\Lambda_{0,s}^{S}=7,
 \qquad
 \ker\Lambda_{0,s}^{S}
   =\mathbb K_s\kappa_s,
 \qquad \kappa_s\ne0.                           \tag{4}
\]

Define the kernel member and its quotient compression by

\[
 O_{\downarrow,s}:=\mathcal D_{0,s}^{S}(\kappa_s),
 \qquad
 \Lambda_{0,s}^{S}\kappa_s=0,
 \qquad
 \lambda_s:=\mathcal C_{0,s}^{S}\kappa_s\ne0. \tag{5}
\]

Here $\mathcal C_{0,s}^{S}$ is the inherited rank-one quotient-compression
map. Equation (5) is the discovery. The leakage vanishes identically, while
the quotient compression is nonzero. After the harmless exact
normalization $\widehat\kappa_s=\lambda_s^{-1}\kappa_s$,

\[
 \pi_{0,s}\mathcal D_{0,s}^{S}(\widehat\kappa_s)
 =\pi_{0,s}.                                    \tag{6}
\]

Thus descent is achievable. The normalized operator in (6) is a genuine
nonzero observable on the rank-one quotient before reflection-adjointness
is imposed. It is the first current-derived operator in this certified
campaign chain to reach that quotient with nonzero compression.

**THE DISCOVERY: DESCENT IS ACHIEVABLE.** Block 122's descent obstruction
was a wall for the routed density and Block 125 extended it across the
displayed spatial family. Equation (5) does not weaken either result. It
exhibits a different, time-dressed operator whose leakage is exactly zero
and whose compression is exactly nonzero.

**THE WALL: ADJOINTNESS BLOCKS IT.** Let $\sharp_s$ denote the inherited
reflection-adjoint operation supplied by the reflection completion. The
exact residual of the normalized descending member is

\[
 \begin{aligned}
 \mathfrak a_s
 &:=\bigl(\mathcal D_{0,s}^{S}(\widehat\kappa_s)\bigr)^{\sharp_s}
       -\mathcal D_{0,s}^{S}(\widehat\kappa_s)\\
 &=\sum_{t=0}^{7}
   \left\{
    \overline{\widehat\kappa_{s,t}}
       \bigl(S_{0,s}^{-t}D_{0,s}S_{0,s}^{t}\bigr)^{\sharp_s}
    -\widehat\kappa_{s,t}S_{0,s}^{-t}D_{0,s}S_{0,s}^{t}
   \right\}
 \ne0
 \end{aligned}                                  \tag{7}
\]

at both fixtures. The equality in (7) is the exact algebraic residual, not
a floating-point norm surrogate. Consequently the descending member is not
reflection-adjoint.

The full joint solve confirms that this is not an accident of the chosen
kernel normalization. There is no nonzero-compression member satisfying
both null descent and reflection-adjointness in Family A, Family B, their
displayed union, or the displayed two-time class. In symbols, with
$\mathfrak J(\mathscr F)$ denoting that joint candidate set,

\[
 \mathfrak J(\mathscr F^M_{k,s})
 =\mathfrak J(\mathscr F^S_{k,s})
 =\mathfrak J(\mathscr F^M_{k,s}\cup\mathscr F^S_{k,s})
 =\mathfrak J(\mathscr F^{(2)}_{k,s})
 =\varnothing.                                  \tag{8}
\]

Equation (8) isolates the wall. Descent itself is no longer the blocker:
(5)--(6) solve it with nonzero compression. Among the jointly tested
requirements for the displayed classes, reflection-adjointness is the
single condition which removes that solution. The displayed observable
wall therefore rests on the inherited reflection-adjointness axiom alone.

The footing correction is equally important. A solve-lane argument tried
to elevate leakage injectivity into a lift-independent obstruction. The
two families refute that mechanism directly: the monodromy lift gives rank
eight, while the shift lift gives rank seven and a genuine nonzero
descending compression. Leakage injectivity is lift-dependent here. It
cannot support an absolute obstruction without first fixing and justifying
the lift.

This theorem is deliberately narrow. Reflection-compatible observable
classes, modification of $Q$, the naturality classification, the
curved-carrier dependency, the completed ADM/history transporter, joint
gravity, the gravity constraint quotient beyond the displayed carrier,
Records, audit retention, axiom amendment, obligation retirement, and TOE
percentage movement remain outside it.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at the authority
snapshot inherited by Block 125:
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. No newer authority claim is
made here.

The exact stacked parent is
[Block 125](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md)
commit `ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d`, content-bound through
note blob `4968f83c5b31d80f6fba31b45460491273f72bb6`. Its inherited
routed-density wall comes from
[Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md),
and its reflection-adjoint structure and positive rank-one quotient come
from
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
No audit verdict is imported from any note.

The executed contract is:

1. the certified package at both rational shear fixtures $s=5/13$ and
   $s=3/5$, with its inherited current block, rank-one quotient, reflection
   adjoint, monodromy lift, and time-shift lift;
2. the two full displayed eight-translate conjugation families in (1)--(2),
   with independent root-field weights and no identification of their
   lifts;
3. exact quotient visibility in each family, certified by unequal quotient
   data for at least two translates at each fixture;
4. exact rank eight and empty nonzero descent for the monodromy-conjugated
   family at every certified momentum and fixture;
5. exact rank seven at zero momentum for the shift-conjugated family, its
   one-dimensional kernel, and the kernel member's identically zero
   leakage;
6. exact nonzero quotient compression, including the normalized identity
   compression (6), proving that a current-derived operator reaches the
   quotient;
7. the exact nonzero reflection-adjointness residual (7) and the empty
   joint solve in both families, their union, and the displayed two-time
   class;
8. isolation of reflection-adjointness as the single blocking axiom among
   the displayed jointly tested requirements;
9. the lift-dependence refutation of leakage injectivity, with checker
   discipline credited for finding the descending member during the
   refutation hunt; and
10. one narrow wall W1, with reflection-compatible classes, $Q$
    modification, naturality, and curved-carrier dependence left live.

The assigned primary runner is the path recorded in the front matter. This
note does not invent a replay footer or a `TOTAL` line: under the supplied
note-only contract, its scientific content is the supervisor-verified
certificate stated above. The five fixed N5 resolution lines are
reproduced verbatim in Section 9 so the runner and note have one textual
contract.

The scope is the two displayed conjugation families, their certified
weight spaces, the inherited lifts used to define them, the zero-momentum
kernel member, the displayed two-time subclass, and the quotient and
reflection tests at the two fixtures. No classification of every lift,
every reflection-compatible observable, a modified $Q$, the Block 127
moduli, curved reconstruction, history transporter, joint-gravity
construction, or gravity quotient beyond the displayed carrier follows.

## 3. The Two Families

Fix $(k,s)$ and write $V_{k,s}$ for the certified prequotient carrier,

\[
 \pi_{k,s}:V_{k,s}\longrightarrow L_{k,s},
 \qquad
 N_{k,s}:=\ker\pi_{k,s},                         \tag{9}
\]

where $L_{k,s}$ is the inherited rank-one quotient. Choose only for
coordinate display a section $\iota_{k,s}:L_{k,s}\to V_{k,s}$. For an
operator $O$ define its leakage, compression, and adjointness residual by

\[
 \begin{aligned}
 \mathscr L_{k,s}(O)&:=\pi_{k,s}O|_{N_{k,s}},\\
 \mathscr C_{k,s}(O)&:=\pi_{k,s}O\iota_{k,s},\\
 \mathscr A_{k,s}(O)&:=O^{\sharp_s}-O.
 \end{aligned}                                  \tag{10}
\]

The descent condition is $\mathscr L_{k,s}(O)=0$. When it holds,
$\mathscr C_{k,s}(O)$ is independent of the displayed section because $O$
preserves $N_{k,s}$. Since $L_{k,s}$ is one-dimensional, that compression
is a scalar endomorphism.

The monodromy-conjugated translates and their full weighted family are

\[
 D_{k,s}^{M,[t]}=M_{k,s}^{-t}D_{k,s}M_{k,s}^{t},
 \qquad
 \mathcal D_{k,s}^{M}(a)
 =\sum_{t=0}^{7}a_tD_{k,s}^{M,[t]},
 \quad a\in\mathbb K_s^8.                       \tag{11}
\]

The shift-conjugated translates and their full weighted family are

\[
 D_{k,s}^{S,[t]}=S_{k,s}^{-t}D_{k,s}S_{k,s}^{t},
 \qquad
 \mathcal D_{k,s}^{S}(b)
 =\sum_{t=0}^{7}b_tD_{k,s}^{S,[t]},
 \quad b\in\mathbb K_s^8.                       \tag{12}
\]

These are definitions in the certified representatives. No equivalence of
$M_{k,s}$ and $S_{k,s}$ is inserted. That distinction is not bookkeeping:
the different leakage ranks below make the lift choice theorem content.

Vectorizing the exact residual entries in the inherited basis gives the
linear maps

\[
 \begin{aligned}
 \Lambda_{k,s}^{M}a
  &:=\operatorname{vec}\mathscr L_{k,s}
       \bigl(\mathcal D_{k,s}^{M}(a)\bigr),\\
 \Lambda_{k,s}^{S}b
  &:=\operatorname{vec}\mathscr L_{k,s}
       \bigl(\mathcal D_{k,s}^{S}(b)\bigr),\\
 \mathcal C_{k,s}^{F}c
  &:=\mathscr C_{k,s}\bigl(\mathcal D_{k,s}^{F}(c)\bigr),\\
 \mathcal A_{k,s}^{F}c
  &:=\operatorname{vec}\mathscr A_{k,s}
       \bigl(\mathcal D_{k,s}^{F}(c)\bigr),
 \qquad F\in\{M,S\}.
 \end{aligned}                                  \tag{13}
\]

The displayed two-time class is the nearest-time shift subclass

\[
 \mathcal D_{k,s}^{(2)}(u,v)
 :=uD_{k,s}^{S,[0]}+vD_{k,s}^{S,[1]},
 \qquad (u,v)\in\mathbb K_s^2.                 \tag{14}
\]

It is named separately because two unequal time translates are the minimum
visibility witness. Its joint failure will not be upgraded into a failure
of every two-time construction.

For any displayed class $\mathscr F$, define the nontrivial joint candidate
set

\[
 \mathfrak J(\mathscr F)
 :=\{O\in\mathscr F:\mathscr L_{k,s}(O)=0,
      \ \mathscr A_{k,s}(O)=0,
      \ \mathscr C_{k,s}(O)\ne0\}.              \tag{15}
\]

The nonzero-compression clause removes the zero operator and
zero-observable weight cancellations. Accordingly, “the joint solve is
empty” below always means that the set (15) is empty, not that the zero
operator has ceased to satisfy homogeneous equations.

The two lifts may encode the same intended time direction at a coarser
level, but their conjugation orbits on the prequotient carrier are not
interchangeable. Equations (11)--(13) preserve that dependence rather than
quotienting it away before it is tested.

## 4. The Visibility

Block 125 proved that a fixed-momentum spatial shift acts by a scalar phase.
Its inverse phase cancels under conjugation, so all displayed spatial
translates have identical momentum-diagonal quotient data. Time conjugation
does not have that form on the certified prequotient carrier.

For each lift $F\in\{M,S\}$, define the ordered quotient profile

\[
 q_{k,s}^{F,[t]}
 :=\mathscr C_{k,s}\bigl(D_{k,s}^{F,[t]}\bigr),
 \qquad t=0,\ldots,7.                            \tag{16}
\]

The exact profile comparison gives, at both rational shear fixtures,

\[
 \begin{aligned}
 &\exists\,t_M\ne u_M:
   q_{k_M,s}^{M,[t_M]}\ne q_{k_M,s}^{M,[u_M]},\\
 &\exists\,t_S\ne u_S:
   q_{k_S,s}^{S,[t_S]}\ne q_{k_S,s}^{S,[u_S]}.
 \end{aligned}                                  \tag{17}
\]

Thus each displayed family contains genuinely distinct time translates as
seen by the quotient. Equation (17) asserts the needed nonequality; it does
not assert that all eight profiles are pairwise distinct or that the two
lifts give the same profile set.

The contrast with Block 125 is exact:

\[
 \underbrace{q_{k,s}^{X,[r]}=q_{k,s}^{X,[0]}}
             _{\text{spatial scalar-phase invisibility}}
 \quad\not\Longrightarrow\quad
 \underbrace{q_{k,s}^{F,[t]}=q_{k,s}^{F,[0]}}
             _{\text{time conjugation}},
 \qquad F\in\{M,S\}.                            \tag{18}
\]

The quotient therefore has enough information to distinguish time
dressings. Visibility alone does not imply descent: Family A below is
visible but has no nonzero leakage kernel. Nor does it imply
reflection-adjointness: the Family B kernel member reaches the quotient and
then fails that additional condition.

This is visibility on the displayed quotient data. It is not a
classification of all time lifts, all transfer powers, or all choices of
section and carrier.

## 5. Family A: Empty Descent

Stack the exact leakage entries of the eight monodromy-conjugated
translates as the columns of $\Lambda_{k,s}^{M}$. The certified reduction
gives

\[
 \operatorname{rank}_{\mathbb K_s}\Lambda_{k,s}^{M}=8
 \quad\text{for every certified }k
 \quad\text{and for }s=5/13,3/5.                \tag{19}
\]

Because the domain is $\mathbb K_s^8$, equation (19) is equivalent to

\[
 \ker\Lambda_{k,s}^{M}=\{0\}.                  \tag{20}
\]

Hence

\[
 \mathscr L_{k,s}\bigl(\mathcal D_{k,s}^{M}(a)\bigr)=0
 \quad\Longleftrightarrow\quad a=0.            \tag{21}
\]

Family A has exactly empty nonzero descent across the certified package.
Its time translates are distinct by (17), but their leakage columns admit
no nontrivial cancellation. Time visibility has removed the spatial
collapse without guaranteeing a descending combination.

The conclusion in (21) is about the monodromy lift in (11). It does not
show that every lift of the same intended time direction has injective
leakage. Family B is an explicit counterexample to that upgrade.

Family A also has an empty joint descent-plus-adjointness solve, but no new
reflection mechanism is needed to prove that subcase: descent already
forces $a=0$. Its role in isolating the final wall comes from comparison
with Family B, where descent succeeds.

## 6. The Descending Member

At zero momentum the shift-conjugated residual matrix loses exactly one
rank at each fixture:

\[
 \operatorname{rank}_{\mathbb K_s}\Lambda_{0,s}^{S}=7,
 \qquad
 \dim_{\mathbb K_s}\ker\Lambda_{0,s}^{S}=1.    \tag{22}
\]

Let $\kappa_s$ be the certified nonzero kernel vector. Then

\[
 \ker\Lambda_{0,s}^{S}=\mathbb K_s\kappa_s,
 \qquad
 O_{\downarrow,s}
 =\sum_{t=0}^{7}\kappa_{s,t}
     S_{0,s}^{-t}D_{0,s}S_{0,s}^{t}.            \tag{23}
\]

The first half of the positive certificate is exact null descent:

\[
 \mathscr L_{0,s}(O_{\downarrow,s})
 =\pi_{0,s}O_{\downarrow,s}|_{N_{0,s}}
 =0                                             \tag{24}
\]

identically over $\mathbb K_s$. There is no residual tail being rounded to
zero.

The second half prevents (23) from being a zero-observable cancellation:

\[
 \mathscr C_{0,s}(O_{\downarrow,s})
 =\lambda_s I_{L_{0,s}},
 \qquad \lambda_s\in\mathbb K_s\setminus\{0\}. \tag{25}
\]

Because the quotient is rank one, rescaling the kernel generator by the
exact nonzero scalar $\lambda_s^{-1}$ gives

\[
 \widehat O_{\downarrow,s}
 :=\lambda_s^{-1}O_{\downarrow,s},
 \qquad
 \pi_{0,s}\widehat O_{\downarrow,s}=\pi_{0,s}. \tag{26}
\]

Equations (24)--(26) are the positive discovery. The operator preserves the
null kernel and acts nontrivially—after normalization, identically—on the
quotient. The quotient is reachable by a current-derived time dressing.

This is the first such reachability certificate in the displayed campaign
chain. Block 122 excluded the routed density. Block 125 excluded every
nonzero-compression member of the displayed spatial dressing. The shift
kernel member is not in those classes and therefore does not contradict
their walls.

The discovery changes the logical footing of the observable obstruction.
One can no longer attribute the displayed time-dressing failure to
unavoidable leakage. There exists a nonzero-compression operator for which
leakage vanishes exactly. Any surviving wall must be located in an
additional condition.

Equation (26) is not yet an OS observable theorem. Reflection-adjointness
has not been imposed there. Nor does a normalized scalar compression prove
naturality, curved-carrier compatibility, conservation outside the
displayed descent test, or compatibility with another reflection
completion.

## 7. The Adjointness Wall

Apply the inherited reflection adjoint $\sharp_s$ to the normalized
descending member. Its exact operator residual is

\[
 \begin{aligned}
 \mathfrak a_s
 &:=\widehat O_{\downarrow,s}^{\sharp_s}
       -\widehat O_{\downarrow,s}\\
 &=\sum_{t=0}^{7}
   \overline{\widehat\kappa_{s,t}}
    \bigl(S_{0,s}^{-t}D_{0,s}S_{0,s}^{t}\bigr)^{\sharp_s}
   -\sum_{t=0}^{7}
    \widehat\kappa_{s,t}S_{0,s}^{-t}D_{0,s}S_{0,s}^{t}
 \ne0,
 \end{aligned}                                  \tag{27}
\]

for $s=5/13$ and $s=3/5$. Reflection-adjointness is the exact equation
$\mathfrak a_s=0$; (27) fails that equation exactly. A nonzero compression
does not make the descending member reflection-adjoint.

For a coefficient class with leakage map $\Lambda$, adjointness map
$\mathcal A$, and compression map $\mathcal C$, absence of a nonzero joint
candidate is equivalently the kernel containment

\[
 \ker
 \begin{pmatrix}
  \Lambda\\ \mathcal A
 \end{pmatrix}
 \subseteq\ker\mathcal C.                       \tag{28}
\]

The certified joint reductions give (28) for the monodromy-conjugated
family, the shift-conjugated family, and the two-time class:

\[
 \begin{aligned}
 \ker\binom{\Lambda_{k,s}^{M}}{\mathcal A_{k,s}^{M}}
   &\subseteq\ker\mathcal C_{k,s}^{M},\\
 \ker\binom{\Lambda_{k,s}^{S}}{\mathcal A_{k,s}^{S}}
   &\subseteq\ker\mathcal C_{k,s}^{S},\\
 \ker\binom{\Lambda_{k,s}^{(2)}}{\mathcal A_{k,s}^{(2)}}
   &\subseteq\ker\mathcal C_{k,s}^{(2)}.
 \end{aligned}                                  \tag{29}
\]

Therefore

\[
 \begin{aligned}
 \mathfrak J(\mathscr F_{k,s}^{M})&=\varnothing,\\
 \mathfrak J(\mathscr F_{k,s}^{S})&=\varnothing,\\
 \mathfrak J(\mathscr F_{k,s}^{M}\cup
              \mathscr F_{k,s}^{S})&=\varnothing,\\
 \mathfrak J(\mathscr F_{k,s}^{(2)})&=\varnothing
 \end{aligned}                                  \tag{30}
\]

throughout the displayed certified tests. The union line is stated
explicitly to prevent a family-by-family wording gap; it follows from the
first two lines because the union adds no mixed linear combinations. The
separate two-time line tests the displayed nearest-time linear class.

Family A reaches (30) because its leakage map is already injective. Family
B is decisive: its descent kernel at zero momentum is nontrivial, its
compression on that kernel is nonzero, and (27) is the condition which
removes the candidate. Hence reflection-adjointness is not merely one
failure among several for the discovered member. It is the single blocking
axiom among the displayed joint conditions.

The isolation statement is correspondingly exact:

\[
 \boxed{\text{descent and nonzero quotient compression are jointly
 achieved; inherited reflection-adjointness alone blocks the displayed
 candidate classes}.}                           \tag{31}
\]

The word “alone” is local to the executed contract. It does not assert that
every possible observable satisfies every other physical requirement, or
that reflection-adjointness is dispensable. It says that, for the displayed
families and tests, removing only that equation admits the certified member
(26), while retaining it makes every nonzero-compression joint solve empty.

This result converges onto the reflection structure supplied in Blocks
118--119. The completion which made the positive quotient meaningful also
provides the adjoint operation that rejects the first current-derived
descending operator. That convergence does not show that every member of a
different reflection completion rejects it.

## 8. The Footing Correction

The solve lane proposed the following mechanism as footing for a broader
observable obstruction:

\[
 \text{for a time lift }L,
 \quad \Lambda_{k,s}^{L}\text{ is injective},
 \quad\text{so no nonzero time-dressed current descends}.    \tag{32}
\]

Family A satisfies the displayed injectivity premise:

\[
 \operatorname{rank}\Lambda_{k,s}^{M}=8.        \tag{33}
\]

Had the monodromy lift been examined alone, (33) could have looked
structural. The shift lift supplies the exact refutation:

\[
 \operatorname{rank}\Lambda_{0,s}^{S}=7,
 \qquad
 \ker\Lambda_{0,s}^{S}=\mathbb K_s\kappa_s,
 \qquad
 \mathcal C_{0,s}^{S}\kappa_s\ne0.             \tag{34}
\]

Equations (33)--(34) use the same inherited current, quotient target, and
fixtures. Their change of rank follows the change of lift. Leakage
injectivity is therefore lift-dependent on the displayed carrier; it is
not a lift-free theorem of the quotient.

The correction is substantive. The refuted mechanism would have placed the
wall at descent and could have licensed an upgrade from Family A to all
time dressings. Equation (34) makes that upgrade false. The surviving wall
must instead use the reflection-adjointness residual (27).

The checker discipline deserves explicit credit. The discovery in Section
6 arose during the attempt to refute the claimed injectivity footing. The
rank-seven case was not discarded as a convention artifact or repaired
back to full rank. Its kernel was followed through leakage, compression,
and adjointness. That refutation hunt exposed both the positive descending
member and the narrower, correctly located wall.

The correction does not say that the monodromy calculation is wrong.
Family A remains exactly full rank. It says that full rank in one lift
cannot serve as a lift-independent obstruction. Nor does it say that every
other lift has a kernel, that all kernels compress nontrivially, or that a
preferred lift has already been selected by naturality.

## 9. No-Go Discipline Gate

There is exactly one bounded observable wall. It is narrower than the
solve-lane footing and contains a positive descent result.

- W1 — **TIME-DRESSING REFLECTION-ADJOINTNESS WALL:** no member of the
  displayed monodromy-conjugated or shift-conjugated time-dressing families
  with nonzero quotient compression satisfies null descent and inherited
  reflection-adjointness jointly. The same joint solve is empty for their
  displayed union and for the displayed two-time class.

W1 is narrow to the certified package at the two rational shear fixtures,
the specific monodromy and shift lifts in (11)--(12), their eight-weight
conjugation families, the inherited quotient and reflection adjoint, and
the two-time subclass (14).

W1 does not say that time dressing cannot descend. Equations (22)--(26)
positively prove the opposite: the zero-momentum shift family contains a
nonzero descending member with nonzero quotient compression. W1 begins
only when inherited reflection-adjointness is added.

W1 does not cover a different natural reflection adjoint, another member of
the prospective Block 127 completion moduli, a different lift taxonomy,
arbitrary mixtures of the two families, modification of $Q$, or an
observable class outside (11)--(14). It is not an OS no-go and is not a
curved-carrier no-go.

Equivalently: the time route reaches the quotient, but the displayed
reflection-adjointness equation rejects every nonzero-compression candidate
which also descends.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). Descent,
adjointness, family emptiness, visibility, and the footing correction remain
separate.

1. **PROVED — strongest adjointness wall / exact joint residual solve on the
   two displayed families, their union, and the displayed two-time class /
   no nonzero-compression member satisfies descent and inherited
   reflection-adjointness jointly.** This is narrow W1 and the shipped wall.
2. **PROVED / POSITIVE — descending member / rank-seven zero-momentum shift
   leakage with a one-dimensional kernel / identically vanishing leakage
   and nonzero quotient compression.** Descent is achievable; the
   normalized member acts as the identity on the rank-one quotient.
3. **PROVED — Family A emptiness / exact rank eight of the
   monodromy-conjugated leakage map at every certified momentum and fixture
   / no nonzero Family A weight descends.** This result is lift-specific.
4. **PROVED / POSITIVE — time visibility / unequal quotient profiles among
   the translates in each displayed conjugation family / both families are
   genuinely visible to the quotient.** Block 125's spatial scalar-phase
   collapse does not recur.
5. **CORRECTED / CHECKER CREDIT — footing correction / compare the
   monodromy and shift leakage ranks under the two displayed lifts / refute
   lift-independent leakage injectivity.** The discovery came from following
   the rank-seven counterexample through compression and adjointness during
   the refutation hunt.
6. **UNTESTED-LIVE — reflection-compatible observable classes, naturality,
   and curved dependency / vary the reflection completion, classify the
   lift and swap naturality, and insert the Block 105 common differential /
   test whether a nonzero descending current-derived observable survives.**
   No result on those terminals is imported here.

Modification of $Q$, the completed ADM/history transporter, joint gravity,
and the gravity constraint quotient beyond the displayed carrier remain
downstream of row 6. W1 consumes none of those routes.

### N2 — Wall-Independence Audit

W1 is independent of Block 125's spatial-dressing invisibility wall,
anchored in its No-Go Discipline Gate.

[Block 125](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md)
asked whether spatial translates of the routed density could create a
nonzero descending observable. Its mechanism was scalar-phase cancellation:
all displayed spatial translates presented the same momentum-diagonal data,
and the descent kernel equalled the zero-compression kernel.

The present W1 uses neither equality of translate profiles nor equality of
the descent and zero-compression kernels. Both displayed time families have
distinct quotient profiles. More decisively, Family B has a descent kernel
which is not a zero-compression kernel: $\kappa_s$ has zero leakage and
nonzero compression. Its obstruction is the nonzero
reflection-adjointness residual (27).

The walls therefore have different objects and mechanisms:

\[
 \begin{array}{c|c|c}
 \text{block} & \text{mechanism} & \text{terminal}\\ \hline
 125 & \text{spatial invisibility} &
       \text{descent only by zero compression}\\
 126 & \text{reflection-adjointness} &
       \text{nonzero descending member rejected by }\sharp_s
 \end{array}                                    \tag{35}
\]

There is an honest shared carrier and current ancestry. That does not merge
the walls. Block 125 stops the displayed spatial class before it reaches
the quotient. Block 126 proves that the displayed shift-time class reaches
the quotient and is stopped by the inherited adjointness equation.

Together the pair brackets the wall's true nature on the displayed classes:
spatial translation supplies no new quotient information, while time
translation supplies enough information to solve descent but not the
selected reflection-adjointness condition. The pair does not bracket every
possible observable class.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.
Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| certified package | the inherited finite quotient package only |
| both rational shear fixtures | exactly $s=5/13$ and $s=3/5$ |
| time direction is genuinely visible to the quotient | quotient-profile nonequality (17) only |
| both displayed conjugation families have distinct translates | at least one unequal pair in each family, not pairwise distinctness |
| monodromy-conjugated family has exactly empty descent | rank-eight statement (19)--(21) for Family A only |
| shift-conjugated family carries at zero momentum a genuine nonzero descending member | the kernel member (23) at $k=0$ only |
| identically vanishing leakage | exact equality (24), not a tolerance claim |
| nonzero quotient compression | exact root-field nonequality (25) |
| first current-derived operator to reach the quotient | first in the displayed certified campaign chain only |
| fails reflection-adjointness exactly | nonzero algebraic residual (27) |
| joint descent-plus-adjointness solve is empty | no nonzero-compression candidate as defined in (15) |
| both families | exactly the families (11) and (12) |
| their union | set union only, with no untested mixed span |
| displayed two-time class | the nearest-time class (14) only |
| observable wall rests on the reflection-adjointness condition alone | isolation (31) within the executed joint tests |
| single blocking axiom for the displayed classes | inherited adjointness, not every possible completion |
| solve lane's leakage-injectivity mechanism | the proposed footing (32), not an adopted theorem |
| refuted as lift-dependent and recorded | rank contrast (33)--(34) |
| reflection-compatible observable classes | untested-live alternative adjointness route |
| q-modification | untested-live change of quotient or carrier |
| naturality classification | untested-live lift and swap classification |
| curved-carrier dependency | the Block 105 common differential remains uninserted |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not completed |
| gravity constraint quotient beyond the displayed carrier | outside scope |
| records | no Records claim |
| retention | independent-audit firewall |
| axiom amendment | explicitly not justified |
| obligation retirement | TOE accounting firewall |
| toe percentage movement | TOE accounting firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting statement |
| no toe percentage moves | TOE accounting statement |
| retained-positive end-to-end theory count remains zero | audit accounting |
| actual adm/history transporter remains | standard partial-close statement |
| gravity constraint quotient remains unexecuted | constraint-scope firewall |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | five N5 keys |

No phrase upgrades the displayed adjointness wall into an absolute
observable no-go. Nothing turns the descending member into an OS observable
or exports the selected $\sharp_s$ to every reflection completion. Nothing
asserts that the monodromy lift is preferred, that the shift lift is
natural, that every time lift has a kernel, or that the two families exhaust
time dressing.

Nothing asserts a reflection-compatible class, $Q$ modification, naturality
classification, curved-carrier compatibility, transporter completion,
joint gravity, axiom amendment, audit retention, obligation retirement, or
TOE percentage movement.

### N4 — Residual Matching

The Block 125 handoff next gate, quoted byte-exactly, is:

> Time-smeared and transfer-conjugated dressings for the observable wall;
> the naturality classification of the swap completion; curved OS positivity
> on the half-space package.

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 125 next gate](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md:16` | “Time-smeared and transfer-conjugated dressings for the observable wall; the naturality classification of the swap completion; curved OS positivity on the half-space package.” | the time half is decided for the displayed families with a discovery: shift-conjugated descent and nonzero quotient compression are achievable, while inherited reflection-adjointness blocks the joint solve; naturality and the curved dependency remain |
| [Block 122 observable wall](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | the routed local density fails null-space descent on the certified quotient | its descent half is now known achievable for the displayed zero-momentum shift-dressed member; the local-density wall itself is unchanged |
| Blocks 118--[119 reflection structure](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | the reflection action, swap completion, and inherited adjoint operation make the rank-one quotient meaningful | the wall converges onto exactly that supplied structure: the first nonzero current-derived descending member fails its inherited reflection-adjointness equation |

This is a partial closure of Block 125's next gate. The displayed time half
has been executed and contains a positive descent discovery, but its joint
observable terminal remains blocked by the selected reflection adjoint.
Naturality, the curved-carrier dependency, and alternative
reflection-compatible classes are untouched.

The phrase “the time half is decided” means only the families (11)--(14) on
the certified carrier. It does not classify arbitrary transfer sandwiches,
mixed lifts, time-dependent counterterms, another completion's adjointness,
or a modified quotient $Q$.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the certified package at both
rational shear fixtures, both displayed time-conjugation families have
distinct quotient translates; the monodromy family has exact rank-eight
empty descent, while the zero-momentum shift family has an exact rank-seven
kernel member with identically vanishing leakage and nonzero quotient
compression, proving that a current-derived operator reaches the quotient,
but its reflection-adjointness residual is exactly nonzero and every
displayed joint descent-plus-adjointness solve is empty, so inherited
reflection-adjointness is the single blocking axiom for those classes.”

Forbidden upgrades include:

- “the observable wall is absolute”;
- “no reflection-compatible observable exists”; and
- “the descending member is an OS observable.”

The first exports W1 beyond the displayed classes and selected reflection
adjoint. The second erases the live alternative-completion route. The third
omits the exact nonzero residual (27).

Also forbidden are “all time lifts have injective leakage,” “the shift
lift is the natural lift,” “the two families exhaust time dressing,”
“changing $Q$ cannot help,” “naturality is classified,” and “the
curved-carrier dependency is solved.” Equations (22)--(25) refute the
first; none of the remaining statements is tested here.

The five N5 resolution lines fixed for the runner are reproduced verbatim:

```text
N5: per_element: time-visibility, monodromy-rank-eight, shift-rank-seven, descending-kernel, zero-leakage, nonzero-compression, adjointness-residual, joint-emptiness, and footing-correction certificates are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: at zero momentum the shift-conjugated rank-seven leakage map has a one-dimensional kernel with identically vanishing leakage and nonzero quotient compression, but its reflection-adjointness residual is nonzero
per_block: both displayed time-conjugation families are quotient-visible; the monodromy family has empty descent, the shift family has one genuine descending member, and no nonzero-compression member satisfies descent and reflection-adjointness jointly in either family, their union, or the displayed two-time class
lattice_wide: checked and not executed — reflection-compatible observable classes, Q-modification, the naturality classification, the curved-carrier dependency, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The result executes the displayed
time-dressing branch without weakening descent or reflection-adjointness.

| route | present status | remaining terminal |
|---|---|---|
| one monodromy translate pair | distinct quotient profiles | visibility does not imply descent |
| full monodromy family | exact rank eight everywhere | empty nonzero descent |
| one shift translate pair | distinct quotient profiles | minimum time visibility only |
| zero-momentum shift family | exact rank seven | one-dimensional leakage kernel |
| kernel member leakage | identically zero | descent achieved |
| kernel member compression | exact nonzero scalar | quotient reached |
| normalized kernel member | identity quotient compression | impose reflection-adjointness |
| inherited adjointness residual | exactly nonzero | displayed member rejected |
| Family A joint solve | empty for nonzero compression | descent already blocks it |
| Family B joint solve | empty for nonzero compression | adjointness blocks the discovered member |
| displayed family union | empty joint candidate set | mixed linear span not classified |
| displayed two-time class | empty joint candidate set | other two-time classes remain live |
| leakage-injectivity footing | refuted as lift-dependent | classify natural lift choice |
| alternative reflection adjoint | untested-live | test Block 127 completion moduli |
| reflection-compatible observable class | untested-live | seek a descending adjoint member |
| $Q$ modification | untested-live | change quotient or carrier explicitly |
| naturality classification | untested-live | classify swap completion and lifts |
| curved-carrier dependency | not executed | insert the Block 105 common differential |
| gravity constraint quotient | displayed carrier only | execute beyond that carrier |

The scan finds no axiom-amendment route. The time-dressing part of Block
125's first next-gate clause is discharged for the displayed classes, with
positive descent and a narrower adjointness wall. The remaining terminals
are reflection-compatible observable classes, naturality, curved-carrier
dependence, the completed transporter, and gravity beyond the displayed
carrier.

### N7 — Steelman

**Hostile steelman: the descending member might satisfy a different natural
adjointness.** In particular, another reflection completion in the Block
127 moduli could define $\sharp'_s$ with
$\widehat O_{\downarrow,s}^{\sharp'_s}=\widehat O_{\downarrow,s}$.

Agreed. Equation (27) tests the inherited $\sharp_s$ supplied by the
displayed completion. It does not classify the completion moduli or prove
failure for every natural adjoint. Whether any Block 127 moduli member's
adjointness admits the descending member is open and is the first next
decision.

**Hostile steelman: lift-dependence makes the family taxonomy
convention-laden.** Calling one orbit monodromy-conjugated and another
shift-conjugated may encode a representative choice rather than physics.

Agreed, and displayed. The rank contrast (33)--(34) is precisely why the
taxonomy is kept explicit in the statement. This block neither chooses the
preferred lift nor treats the two orbits as invariant classes. Naturality
must decide whether one family, an equivalence class, or a different
construction is canonical.

**Hostile steelman: two families are not all families.** Mixed conjugations,
longer-time insertions, transfer sandwiches, counterterms, and modified
quotients could have different joint kernels.

Agreed. W1 covers (11)--(14), not the linear span of every monodromy and
shift word and not every time-dressed current. Even the union in (30) is a
set union, not an untested mixed span. Those broader classes remain live.

These steelmen preserve narrow W1. The inherited adjoint rejects the
displayed descending member, while other natural adjoints, the preferred
lift taxonomy, and other time-dressing families remain open by name.

### N8 — Cross-Cycle Echo

The immediate campaign chain separated reflection completion, observable
descent, spatial invisibility, and time-dressing adjointness.

| campaign block | narrowing that leads to W1 and the live route |
|---|---|
| [Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | supplied the certified rank-one-per-sector quotient, swap completion, and reflection structure whose inherited adjoint is tested here |
| [Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | proved that the routed density fails null descent and left non-local repair open |
| [Block 125](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md) | extended the wall across the displayed spatial family by quotient invisibility and certified time as the visible route |
| Block 126 | proves that time visibility yields a genuine nonzero descending compression, refutes lift-independent leakage injectivity, and locates the remaining displayed wall exactly at inherited reflection-adjointness |

The present result does not infer descent from visibility. Family A is a
counterexample to that inference. Nor does it infer an observable from
descent alone. The exact residual (27) is a counterexample to that upgrade.
The positive theorem needs both (24) and (25); the wall needs their
combination with (27) and the full joint reductions (29).

**No-Go Discipline verdict:** **PASS** only for narrow W1. No
nonzero-compression member of the displayed monodromy-conjugated or
shift-conjugated families, their set union, or the displayed two-time class
satisfies null descent and inherited reflection-adjointness jointly at
either fixture. **POSITIVE** for genuine time visibility and for the
zero-momentum descending member with identically zero leakage and nonzero
quotient compression. **CORRECTED** for the leakage-injectivity footing,
which is refuted as lift-dependent. **FAIL** for an absolute observable
wall, nonexistence of reflection-compatible observables, promotion of the
descending member to an OS observable, a preferred natural lift, exhaustion
of time-dressing families, $Q$-modification failure, naturality, curved
compatibility, a completed ADM/history transporter, joint gravity, a
quotient beyond the displayed carrier, axiom necessity, audit retention,
obligation retirement, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. Time-translate visibility, the two exact
leakage ranks, the one-dimensional kernel, identically vanishing leakage,
nonzero compression, the inherited-adjoint residual, the joint emptiness
certificates, and the lift-dependence correction are finite consequences of
the displayed quotient, current, reflection structure, lifts, and fixtures.
No new primitive is assumed.

Calling reflection-adjointness the single blocking axiom in (31) diagnoses
the displayed joint solve. It is not authorization to delete, weaken, or
replace that axiom. A different natural adjoint must be constructed and
tested before any constitutional question could arise.

This is bounded route closure, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. classify reflection-compatible observable classes: does any Block 127
   moduli member's adjointness admit the descending member
   $\widehat O_{\downarrow,s}$?;
2. execute the curved-carrier dependency by inserting the Block 105 common
   differential into whichever descended reflection-compatible class
   survives; and
3. classify the naturality of the swap completion and of the lift choice on
   that surviving package.

The actual ADM/history transporter remains unexecuted beyond the displayed
half-space positive package, its contractive parity-paired transfer, the
balanced sourced Gauss graph modulo constant gauge, and the bounded
time-dressing adjointness wall.

Reflection positivity on the curved carrier remains unexecuted; in
particular, the Block 105 common differential has not been propagated
through a reflection-compatible descended observable class.

The gravity constraint quotient remains unexecuted beyond the displayed
balanced carrier.
