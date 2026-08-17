---
claim_id: admissibility_dirac_kahler_momentum_population_definiteness_bounded_theorem_note_2026-08-16
claim_type: bounded_theorem
claim_scope: "on the certified package at both rational shear fixtures, the spatial shift commutes with the action exactly and its routed current obeys the off-shell divergence-commutator identity with per-sector reduction to the invertible phase i^k times the U(1) commutator; the closed-carrier population question splits exactly on charge definiteness — the U(1) total charge operator is the identity, so its expectation is the norm and never vanishes on a nonzero positive state, while the quotient momentum charge diag(0,1,2,-1) is indefinite and the displayed nonzero certified-positive state occupying the paired momenta has vanishing expected total momentum under either sign convention (though the charge does not annihilate it — the zero is an expectation value), so the momentum-constraint source admits closed-carrier Gauss solutions; the local-observable wall transfers verbatim under the invertible sector phase; no per-slice time-translation symmetry exists and the per-period energy statement is vacuous beyond the already-certified contractivity; and the momentum-sourced quotient execution, non-local dressings, the naturality classification, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_quotient_observable_obstruction_bounded_theorem_note_2026-08-16
runner: scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_quotient_observable_obstruction_bounded_theorem_note_2026-08-16
target_blocker_text: "Pose the stress-tensor source and non-local current dressings on the open/background carrier; then the naturality classification and curved OS positivity."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Execute the momentum-sourced Gauss quotient on the closed carrier with the vanishing-expectation state class; then non-local dressings, the naturality classification, and curved OS positivity."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-122 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact shift-action commutation, exact routed-current divergence identity and sector-phase reduction, exact identity-versus-indefinite charge split, exact positive-state zero-momentum expectation under both sign conventions, exact closed-carrier Gauss-image compatibility, exact transfer of the local-observable obstruction, and explicit Floquet-energy vacuity on the certified package at both rational shear fixtures; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Momentum Population Break And The Charge-Definiteness Split

**Date:** 2026-08-16

**Campaign block:** 123

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py`](../scripts/admissibility_dirac_kahler_momentum_population_definiteness_2026_08_16.py)

## 1. Result Up Front

[Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md:16`
and elaborated in its Next Decision:

> Pose the stress-tensor source and non-local current dressings on the
> open/background carrier; then the naturality classification and curved OS
> positivity.

**THE DEFINITENESS THEOREM.** On the certified package at each rational
shear fixture $c=5/13$ and $c=3/5$, the closed-carrier population question
splits exactly by the definiteness of the total charge. The quotient U(1)
charge and dimensionless quotient momentum charge are

\[
 \mathcal Q_{\mathrm{U(1)}}^{\rm phys}
   =\left.\sum_zE_z\right|_{\rm phys}=I_4,
 \qquad
 \widetilde P_x^{\rm phys}
   =\operatorname{diag}(0,1,2,-1),                 \tag{1}
\]

where $P_x^{\rm phys}=(\pi/2)\widetilde P_x^{\rm phys}$ in the signed
principal convention. Thus every nonzero positive quotient state $v$
obeys

\[
 \langle v,\mathcal Q_{\mathrm{U(1)}}^{\rm phys}v\rangle
 =\lVert v\rVert^2>0.                              \tag{2}
\]

That identity-valued charge cannot satisfy the zero-total-source condition
for a periodic Gauss equation. The momentum charge in (1), however, is
indefinite. For the nonzero certified-positive state

\[
 v_\star=e_1+e_3=(0,1,0,1)^{\mathsf T},            \tag{3}
\]

the $+\pi/2$ convention gives

\[
 \widetilde P_x^{\rm phys}(e_1+e_3)=e_1-e_3,
 \qquad
 \langle v_\star,\widetilde P_x^{\rm phys}v_\star\rangle
 =1-1=0.                                           \tag{4}
\]

The equivalent mod-$4$ convention labels the $k=3$ charge by $3$ instead of
$-1$, and gives $1+3=0\pmod4$. Thus the expected total momentum vanishes in
both the signed-integer and mod-$4$ conventions. Equation (4) states an
**EXPECTATION-VALUE ZERO**, not an operator kernel: the charge does not
annihilate $v_\star$. This caveat and the population break are one result.
The corresponding momentum source has zero total in its coefficient group
and therefore lies in the image of the closed-carrier incidence operator.
Closed-carrier Gauss solutions are admitted at the source-compatibility
level; the sourced OS quotient itself is not executed here.

This reframes
[Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md).
Its U(1) population wall was never a failure of microscopic conservation.
It was a definiteness wall: an identity-valued total charge cannot cancel
inside a nonzero positive state. Momentum supplies the positive break
because its quotient charge has both signs.

The spatial shift also commutes with the action exactly. Its routed current
obeys

\[
 \Delta_t^-T_{tx,z}+\Delta_x^-T_{xx,z}
 =\bar\phi[E_z,R_x]\psi,
 \qquad R_x=U_xQ=QU_x,                             \tag{5}
\]

and momentum sector $k$ reduces (5) to the invertible factor $i^k$ times
the U(1) commutator identity. That same invertible factor transfers Block
122's local-observable wall verbatim: every site residual remains nonzero,
and null descent and reflection-adjointness still fail. The momentum
population break does not break the observable wall.

There is no per-slice time-translation symmetry on the periodically driven
microscopic package. The only cell object is the Floquet generator
$h_k=-\log(\rho_k^2)$ with
$B_{\rm phys}=\operatorname{diag}(\rho_k^2)=e^{-h}$. Its descent is by
construction and adds no theorem beyond the certified contractivity of
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
The per-period energy statement is therefore **VACUOUS**, and no per-slice
energy conservation is claimed.

This theorem is deliberately narrow. The momentum-sourced quotient
execution, non-local dressings, naturality, curved OS positivity, the
completed ADM/history transporter, joint gravity, the gravity constraint
quotient, Records, audit retention, axiom amendment, obligation retirement,
and TOE percentage movement remain outside it.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The authority snapshot is
unchanged from Block 122.

The exact stacked parent is
[Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
commit `f067b99be7eb49fc46ea8dffccab5e20e6052d88`, content-bound through
note blob `ef9f1b2037c8b470c821ed27572a81c6cb9ac9a4`. Its relevant inherited
microscopic current comes from
[Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md),
and its positive half-space quotient and contractive transfer come from
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
No audit verdict is imported from any note.

The executed contract is:

1. the certified package at both rational shear fixtures $c=5/13$ and
   $c=3/5$, with quotient momenta $k=0,1,2,3$;
2. exact commutation of the spatial shift $U_x$ with the action $Q$ and the
   routed off-shell divergence-commutator identity for $R_x=U_xQ$;
3. sector reduction of the shift current to $i^k$ times the U(1) current,
   including the inherited matrix-generic routing identity;
4. the exact quotient operators $I_4$ and
   $\operatorname{diag}(0,1,2,-1)$ in units $\pi/2$;
5. the displayed nonzero certified-positive paired-momentum state, the
   signed-integer and mod-$4$ momentum conventions, and the distinction
   between zero expectation and charge annihilation;
6. the zero-sum image of the closed-carrier incidence operator and the
   compatibility of the displayed momentum source row;
7. transfer of Block 122's local-observable residual, null-descent, and
   reflection-adjointness failures under the invertible sector phase;
8. absence of a microslice time-translation symmetry and classification of
   the Floquet-generator statement as vacuous beyond inherited
   contractivity; and
9. one narrow population-definiteness wall with one positive momentum break,
   leaving the sourced quotient execution, non-local dressings, naturality,
   curved OS positivity, and gravity open.

The supplied scientific scratch computation was replayed and ends with
`TOTAL: PASS=1595 FAIL=0`. The scratch handoff records an approximately
`324` second final run. The completed primary runner was then replayed and
ends with `TOTAL: PASS=8 FAIL=0`. Runtime is not theorem content.

The primary replay's decision footer is reproduced exactly:

```text
RESULT: the momentum constraint is populatable on the closed carrier because its charge is indefinite — the first population break of the campaign — while the local-observable wall transfers verbatim under the invertible sector phase and the only energy object is the already-certified per-period contraction
DECISION_CUT: execute the momentum-sourced gauss quotient with the vanishing-expectation state class; reject per-slice energy constructions
TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves
TOTAL: PASS=8 FAIL=0
```

The scope is the displayed package, both fixtures, the four quotient
momenta, the identity-valued U(1) charge, the displayed momentum operator and
paired state, and the closed-carrier incidence equation. A source-compatible
row is exhibited, but no momentum-sourced OS quotient is formed. No non-local
dressing, naturality classification, curved reconstruction, or gravity
constraint quotient follows.

## 3. The Shift Symmetry And Its Current

Let $U_x$ be the one-step spatial shift on the displayed lift, with
$U_x|t,x\rangle=|t,x+1\rangle$. The exact action commutator vanishes at both
fixtures:

\[
 [U_x,Q]=0,
 \qquad
 R_x:=U_xQ=QU_x.                                  \tag{6}
\]

The matrix $R_x$ is the insertion generated by the spatial shift. Localize
that transformation with the fine-site projector $E_z$ and route every
matrix element between its endpoints. The resulting temporal momentum
density $T_{tx,z}$ and spatial momentum flux $T_{xx,z}$ obey

\[
 \Delta_t^-T_{tx,z}+\Delta_x^-T_{xx,z}
 =\bar\phi[E_z,R_x]\psi.                          \tag{7}
\]

Equation (7) is an off-shell divergence-commutator identity. It is exact,
not a fitted small residual and not a quotient-only equality. The on-shell
continuity consequence has the same status as Block 121's U(1) consequence;
the present population question does not weaken it.

The exact finite certificates are:

| fixture | sector residual ranks | $T_{tx}$ nnz | $T_{xx}$ nnz | hash |
|---|---|---:|---:|---|
| $5/13$ | $(2,2,2,2)$ | 176 | 240 | `888b798cf7b74ede0c7a` |
| $3/5$ | $(2,2,2,2)$ | 176 | 240 | `77f7227e6baa15e2ca45` |

All 32 sites, including the antiperiodic seam, enter each fixture row.
Both inherited local routing orders were recomputed; each telescopes to the
same endpoint commutator at every site.

The routing proof is inherited without a charge-specific shortcut. For a
matrix $M$, a routed hop from $u$ to $v$ contributes signed crossings along
its path. Taking the discrete divergence telescopes those crossings to the
endpoint difference,

\[
 \operatorname{div}j_M(z)
 =\bar\phi(E_zM-ME_z)\psi.                         \tag{8}
\]

Block 121 applied (8) to $M=Q$. The argument is matrix-generic, so applying
it to $M=R_x$ proves (7). Two allowed local routings differ by a discrete
curl and therefore have the same divergence. No new routing assumption is
introduced by the momentum insertion.

This is the contentful symmetry statement: the spatial shift commutes with
the action, and its resolved current has the exact local identity (7).
Population is a separate question about the total charge and the image of a
closed incidence operator.

## 4. The Sector Phase Reduction

Use the momentum embeddings $F_k$ in the order $k=0,1,2,3$. The spatial
shift and its quotient representative are

\[
 F_k^\dagger U_xF_k=i^kI,
 \qquad
 U_x^{\rm phys}=\operatorname{diag}(1,i,-1,-i).    \tag{9}
\]

All structures entering the sector calculation are momentum diagonal.
Together with (6), this gives

\[
 F_k^\dagger R_xF_k=i^kQ_k,
 \qquad
 \widehat{[E_z,R_x]}_k
   =i^k\widehat{[E_z,Q]}_k.                       \tag{10}
\]

The same reduction holds componentwise for the routed current kernels:

\[
 \widehat T_{tx,k}=i^k\widehat J_k,
 \qquad
 \widehat T_{xx,k}=i^k\widehat S_k.               \tag{11}
\]

Here $J$ and $S$ are the U(1) routed components of Blocks 121--122 in the
same cut and route convention. Thus the momentum Ward residual in every
sector is

\[
 \mathcal W^{(x)}_{k,z}
 =i^k\mathcal W^{(\mathrm{U(1)})}_{k,z}.           \tag{12}
\]

Each phase $i^k$ is invertible. It can rotate or reverse a value, but it
cannot create a zero, restore null descent, or repair an adjointness defect.
This exact phase mechanism is why the population answer may change while
the local-observable answer does not.

## 5. The Definiteness Split

Microscopic site completeness gives $\sum_zE_z=I_{32}$ exactly; compression
to the normalized four-line positive quotient gives $I_4$.

The exact U(1) operator and the two equivalent momentum-charge assignments
on the four-sector physical quotient are

\[
 \mathcal Q_{\mathrm{U(1)}}^{\rm phys}
   =\left.\sum_zE_z\right|_{\rm phys}=I_4,
 \qquad
 \widetilde P_x^{\mathbb Z}
   =\operatorname{diag}(0,1,2,-1),
 \qquad
 \widetilde P_x^{\mathbb Z_4}
   =\operatorname{diag}(0,1,2,3)\pmod4.            \tag{13}
\]

The Hermitian principal operator $\widetilde P_x^{\mathbb Z}$ is in units
$\pi/2$ and is the signed-integer convention. The mod-$4$ assignment records
the same phases as residues in $\mathbb Z_4$; it is not a second physical
operator. Both exponentiate to the exact shift:

\[
 \exp\!\left(\frac{i\pi}{2}\widetilde P_x^{\mathbb Z}\right)
 =\exp\!\left(\frac{i\pi}{2}\widetilde P_x^{\mathbb Z_4}\right)
 =\operatorname{diag}(1,i,-1,-i)=U_x^{\rm phys}.   \tag{14}
\]

The U(1) operator is positive definite. For every nonzero positive quotient
state $v$,

\[
 \langle\mathcal Q_{\mathrm{U(1)}}\rangle_v
 :=\langle v,I_4v\rangle=\lVert v\rVert^2>0.       \tag{15}
\]

The momentum operator is indefinite: its displayed spectrum contains the
positive values $1,2$, the negative value $-1$, and zero. The paired-momentum
state $v_\star=e_1+e_3$ is nonzero and certified-positive. Put
$P_x:=\widetilde P_x^{\mathbb Z}$. Directly,

\[
 \begin{aligned}
 P_x(e_1+e_3)&=e_1-e_3\ne0,\\
 \langle v_\star,P_xv_\star\rangle
   &=1-1=0,\\
 \widetilde P_x^{\mathbb Z_4}(e_1+e_3)&=e_1+3e_3\ne0,\\
 \langle v_\star,\widetilde P_x^{\mathbb Z_4}v_\star\rangle
   &=1+3=0\pmod4.
 \end{aligned}                                    \tag{16}
\]

The same displayed state also obeys
$\langle v_\star,U_x^{\rm phys}v_\star\rangle=i-i=0$. This unitary
expectation is a consistency certificate for the paired sectors; the
Hermitian momentum expectation in (16) is the Gauss-source quantity.

Moreover, $e_1-e_3$ is not proportional to $e_1+e_3$. Thus $v_\star$ is
not an eigenstate of $P_x$, and in particular it is not annihilated by that
charge.

This is the exact split. Equation (15) forbids cancellation for an
identity-valued charge on a nonzero positive state. Equation (16) permits
cancellation for the indefinite signed charge, equivalently for its mod-$4$
assignment. Neither line says that the state is in the kernel of the
momentum charge. Indeed, the first and third lines of (16) display the
opposite. The zero is only the expected total momentum.

## 6. The Gauss Population

Let $D_{\rm cl}$ be the oriented incidence operator on the closed
$\mathbb Z_4$ carrier. As in Block 121, its image is exactly the zero-sum
subspace in either coefficient convention:

\[
 \begin{aligned}
 \operatorname{im}D_{\rm cl}^{\mathbb Z}
   &=\{s:\mathbf1^{\mathsf T}s=0\},\\
 \operatorname{im}D_{\rm cl}^{\mathbb Z_4}
   &=\{s:\mathbf1^{\mathsf T}s=0\pmod4\}.
 \end{aligned}                                    \tag{17}
\]

For the state $v_\star$, the sector-population row and the two momentum
source rows are

\[
 n_\star=(0,1,0,1)^{\mathsf T},
 \qquad
 p_\star^{\mathbb Z}=(0,1,0,-1)^{\mathsf T},
 \qquad
 p_\star^{\mathbb Z_4}=(0,1,0,3)^{\mathsf T}.     \tag{18}
\]

Consequently,

\[
 \mathbf1^{\mathsf T}n_\star=2,
 \qquad
 \mathbf1^{\mathsf T}p_\star^{\mathbb Z}=0,
 \qquad
 \mathbf1^{\mathsf T}p_\star^{\mathbb Z_4}=4=0\pmod4. \tag{19}
\]

In the runner's oriented signed-lift convention, one exact incidence-level
solution is

\[
 g_\star=(0,1,1,0)^{\mathsf T},
 \qquad
 D_{\rm cl}^{\mathbb Z}g_\star=p_\star^{\mathbb Z}. \tag{20}
\]

The first row is the U(1)-definiteness wall in concrete form: no closed
Gauss field can have $n_\star$ as its divergence. More generally, (15)
excludes every nonzero positive state, not only $v_\star$.

The second and third rows are the **POSITIVE MOMENTUM POPULATION BREAK**.
Each belongs to the corresponding image in (17), so the c-number momentum
source admits closed-carrier Gauss solutions in either convention. Changing
from the signed lift to the mod-$4$ labels changes notation, not
solvability.

This is source compatibility, not the execution of the constraint quotient.
No Gauss field is coupled back to the OS transfer package, no constrained
state space is formed, and no gravity dynamics is propagated. The
operator-level constraint question also remains open because expectation
zero is weaker than charge annihilation.

## 7. The Pin Transfer

Block 122 pinned its local quotient-observable failure to the compressed
site commutator $\widehat{[E_z,Q]}_k$. Equation (10) gives the momentum pin

\[
 P_k^{\rm OS}\widehat{[E_z,R_x]}_kP_k^{\rm OS}
 =i^k
  P_k^{\rm OS}\widehat{[E_z,Q]}_kP_k^{\rm OS}.    \tag{21}
\]

Since $i^k\ne0$, every contentful Block 122 failure transfers verbatim to
the shift current on this package:

1. the site-resolved Ward residual is nonzero at all 32 sites in every
   momentum sector at both fixtures;
2. both routed current components fail left and right OS-null-space descent,
   with exact score `0/32` in every sector;
3. both components fail reflection-adjointness, again with exact score
   `0/32` in every sector; and
4. alternate local routings differ by a discrete curl and cannot alter the
   pinned divergence.

Multiplication by an invertible scalar preserves nonzero witnesses and
preserves failure to map the null space into itself. The reflected-sector
calculation likewise includes the conjugate phase and leaves every
adjointness failure nonzero. These are exact certificates at both fixtures,
not genericity arguments.

The exact residual and operator-witness summaries are:

| fixture | residual hashes for $k=0,1,2,3$ | $T_{tx}$ witness | $T_{xx}$ witness |
|---|---|---|---|
| $5/13$ | `015c0ca77d7f24d6`, `2c00d2a740052e4d`, `10ae89306f94b5d6`, `00ba62c446192264` | `790c9f7324da9627` | `57c6cbcb2abeb6ba` |
| $3/5$ | `5ee669c4c61180cb`, `1e5a9006bd3a7c5f`, `b2a4bf5f2ad74469`, `97861afaa6819fa7` | `2ffde5a0ec067e6c` | `eb9b0a256b5640df` |

For each residual-hash row, the exact zero count is `(0,0,0,0)` out of 32
in momentum order. For each component and sector, both left/right null
descent counts are zero; the best reflection-adjoint zero count is also zero.

The local-observable wall is therefore momentum-blind in precisely this
sense: replacing the U(1) insertion by the commuting shift insertion changes
each sector only by $i^k$. The population wall is not momentum-blind because
population tests the definiteness of the total charge, and (13) changes that
spectrum. The momentum break opens a source class; it does not produce a
local conserved quotient observable. Non-local dressings remain the named
repair route.

## 8. The Energy Scope

There is no one-microslice time shift commuting with the displayed action.
If $V$ denotes the antiperiodic microslice shift, the exact tests give

\[
 [Q,V]\ne0,
 \qquad
 [Q,V^4]\ne0.                                    \tag{22}
\]

Both fixtures have `208` nonzero entries in $[Q,V]$ and `112` in
$[Q,V^4]$. Thus neither a one-slice shift nor its four-step power supplies a
Noether current $T_{tt}$ or a per-slice energy conservation law on this
package. The one-step failure-witness hashes in fixture order are
`fb3bc40eec4d5671` and `121a3eb8abec6bc7`.

The certified physical cell transfer is diagonal,

\[
 B_{\rm phys}=\operatorname{diag}(\rho_0^2,\rho_1^2,
                                   \rho_2^2,\rho_3^2),
 \qquad 0<\rho_k^2<1.                              \tag{23}
\]

One may define its exact Floquet generator by functional calculus,

\[
 h=\operatorname{diag}(h_0,h_1,h_2,h_3),
 \qquad h_k=-\log(\rho_k^2),
 \qquad B_{\rm phys}=e^{-h},
 \qquad [h,B_{\rm phys}]=0.                       \tag{24}
\]

The exact cell forms are $T_{tt}^{\rm cell}(a)=a^\dagger ha$. The fixture
certificate hashes are `1e21e90244c98ad2` at $c=5/13$ and
`fd299e49340a0ee3` at $c=3/5$.

The object $h$ descends because it is defined directly from the already
descended diagonal transfer. Its commutation with $B_{\rm phys}$ is automatic
functional calculus. It does not reconstruct a missing microslice symmetry
and does not add an independent conserved-energy theorem.

Sector by sector, the certified quotient is one-dimensional and its cell
transfer is the scalar $\beta_k=\rho_k^2$. A scalar spectral label $h_k$
could not fail to descend or commute with that transfer. The only contentful
inequality is

\[
 0<\beta_k<1
 \quad\Longrightarrow\quad
 h_k=-\log\beta_k>0,                               \tag{25}
\]

which is precisely the inherited contractivity certificate.
The imported pinned-interval hashes in fixture order are
`e7d0e5c7a9778c6e` and `bf06c92a87275672`.

Accordingly, the per-period energy statement is labeled **VACUOUS**. The
contentful residue is exactly the contractivity certified in
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
and displayed in (23). No checker credit is assigned twice: contractivity
remains contentful, whereas defining $h=-\log B_{\rm phys}$ and observing
$[h,B_{\rm phys}]=0$ is bookkeeping on that result.

## 9. No-Go Discipline Gate

There is exactly one bounded population-definiteness wall, and its honest
statement includes a positive break.

- W1 — **U(1)-DEFINITENESS WALL / MOMENTUM POPULATION BREAK:** an
  identity-valued U(1) total charge has strictly positive expectation on
  every nonzero positive quotient state and therefore cannot populate the
  zero-sum image of the closed-carrier incidence operator. The quotient
  momentum charge is indefinite, and the displayed paired-momentum state has
  zero expected total momentum under either sign convention. Its c-number
  source row is in that image and admits closed-carrier Gauss solutions.

The U(1)-definiteness half is the wall. The momentum half is **POSITIVE**
bounded-theorem content, not a second wall. W1 covers only the displayed
certified package, the fixtures $c=5/13$ and $c=3/5$, the exact charge
operators in (13), the state $v_\star$, and the closed incidence form (17).
It does not classify every positive state with zero expected momentum, form
the sourced quotient, impose an operator-level constraint, construct a
non-local observable, or couple gravity.

W1 is not a conservation obstruction. The shift-action commutator vanishes
and the off-shell identity (7) is exact. Nor is the momentum population break
an observable-descent theorem. By (21), Block 122's local-observable wall
survives the change of charge.

W1 is not an OS no-go and is not a curved OS no-go. It distinguishes one
definite charge from one indefinite charge on one certified finite quotient.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). Charge population,
microscopic continuity, quotient-observable descent, and energy scope remain
separate.

1. **PROVED — strongest definiteness theorem — closed-carrier charge
   population / identity-valued charge versus indefinite momentum charge /
   U(1) is blocked while the displayed momentum expectation populates the
   zero-sum Gauss image.** The distinction is exact at both fixtures.
2. **PROVED — shift symmetry and current / exact $[U_x,Q]=0$, the
   matrix-generic routing telescope, and momentum-diagonal reduction /
   off-shell divergence identity with sector factor $i^k$.** Every phase is
   invertible.
3. **PROVED — positive population break with caveat / paired $k=1,3$
   occupations and opposite signed momenta / $1+(-1)=0$ in the integer
   convention and $1+3=0\pmod4$ in the mod-$4$ convention, but no charge
   annihilation.** This is the c-number source condition required by (17).
4. **PROVED — local-observable pin transfer / multiply the compressed
   $[E_z,Q]$ witnesses by $i^k$ / every Block 122 residual, null-descent,
   reflection-adjointness, and routing-curl failure survives.** Population
   and observable descent have different answers.
5. **PROVED — checker-discipline exposure / distinguish microslice symmetry
   from Floquet functional calculus / the per-period energy statement is
   labeled vacuous beyond Block 119's certified contractivity.** This earns
   discipline credit, not a new conservation theorem.
6. **UNTESTED-LIVE — momentum-sourced quotient and observable repair /
   execute the closed-carrier Gauss quotient with the vanishing-expectation
   class and construct non-local dressings / test the actual constraint and
   dressed observable.** Naturality and curved OS positivity remain
   downstream.

The completed ADM/history transporter and joint gravity remain downstream of
row 6. W1 consumes none of those routes.

### N2 — Wall-Independence Audit

W1 is distinct from Block 122's wall, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md:587-618`.

Block 122 studied **observable descent**. Its object was the local routed U(1)
density/current family; its mechanism was the nonzero quotient compression
of $[E_z,Q]$, failure to preserve the OS null space, and failure of
reflection-adjointness. That obstruction is already present before a closed
Gauss population equation is imposed.

The present W1 studies **source population**. Its object is the total charge
entering the closed-carrier incidence equation; its mechanism is definiteness.
An identity-valued charge has norm-valued expectation and cannot have zero
total on a nonzero positive state. An indefinite momentum charge can, as
(16)--(19) show. This proof does not use null descent or
reflection-adjointness.

There is an honest shared pin. The shift-current residual is exactly $i^k$
times Block 122's inherited $[E_z,Q]$ residual. That pin transfers the
observable wall to the momentum current. It does no work in the population
break, which follows from the spectra in (13) and the incidence image in
(17).

Conversely, a zero-total source need not define a quotient observable, and a
descending observable need not satisfy a closed-carrier zero mode. The
present calculation exhibits the first separation directly: momentum
populates the c-number Gauss image while its displayed local routed current
still fails observable descent. Neither wall implies the other.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.
Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| certified package | the inherited finite quotient package only |
| both rational shear fixtures | exactly $c=5/13$ and $c=3/5$ |
| spatial shift commutes with the action exactly | equation (6) on that package |
| routed current | the displayed $T_{tx}$ and $T_{xx}$ kernels only |
| off-shell divergence-commutator identity | equation (7), before equations of motion |
| per-sector reduction | equations (10)--(12) for $k=0,1,2,3$ |
| invertible phase i^k | a nonzero scalar in every sector |
| u(1) commutator | the inherited $[E_z,Q]$ pin only |
| closed-carrier population question | image test (17), not quotient execution |
| charge definiteness | the mechanism distinguishing (15) and (16) |
| u(1) total charge operator is the identity | the first operator in (13) |
| expectation is the norm | equation (15) on positive quotient states |
| never vanishes on a nonzero positive state | the strict inequality in (15) |
| quotient momentum charge diag(0,1,2,-1) | dimensionless plus convention in (13) |
| indefinite | positive, negative, and zero eigenvalues are displayed |
| nonzero certified-positive state | $v_\star=e_1+e_3$ only |
| paired momenta | the occupied $k=1$ and $k=3$ sectors |
| vanishing expected total momentum | the scalar equalities in (16) |
| either sign convention | signed-integer and mod-$4$ assignments in (13) |
| charge does not annihilate it | the vector inequalities in (16) |
| zero is an expectation value | explicit operator-level caveat |
| momentum-constraint source | the c-number rows in (18) |
| closed-carrier gauss solutions | existence from the image criterion only |
| local-observable wall transfers verbatim | the four failures in Section 7 |
| observable wall is momentum-blind | only under the sector-phase mechanism |
| positive momentum population break | W1's momentum half, not quotient execution |
| no per-slice time-translation symmetry exists | no microslice $T_{tt}$ theorem |
| per-period energy statement is vacuous | functional calculus in (24) |
| already-certified contractivity | inherited content from Block 119 |
| momentum-sourced quotient execution | untested-live next construction |
| non-local dressings | outside the local routed class |
| naturality classification | untested-live downstream classification |
| curved os positivity | explicit reconstruction firewall |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not completed |
| gravity constraint quotient | explicitly unexecuted |
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
| gravity constraint quotient remains unexecuted | constraint-execution firewall |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | five N5 keys |

No phrase upgrades c-number source compatibility into execution of the
constraint quotient, expectation zero into charge annihilation, shift
continuity into quotient-observable descent, Floquet functional calculus into
per-slice conservation, or the finite quotient into gravity. Nothing asserts
naturality, curved OS positivity, completion of the ADM/history transporter,
joint gravity, axiom amendment, audit retention, obligation retirement, or
TOE percentage movement.

### N4 — Residual Matching

The supplied historical Block 105 result line, carried by Block 122, is:

> Block 105 §12 item 4 moves on exact source conservation and constraint
> preservation, but not on propagating $d=2$ gravity or gravity-transfer
> selection.

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 122 next gate](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md:16` | “Pose the stress-tensor source and non-local current dressings on the open/background carrier; then the naturality classification and curved OS positivity.” | the stress/momentum route is opened and split: its shift current and population charge are solved on the displayed package, but quotient execution, non-local dressings, naturality, and curved OS positivity remain |
| [Block 121 population wall](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md) | the norm-valued U(1) total charge cannot populate the zero-sum closed-carrier Gauss image | reframed exactly as a definiteness wall; its scope is identity-valued charge on nonzero positive states, while indefinite momentum supplies the displayed expectation-zero break |
| Block 105 §12 item 4 | exact source conservation and constraint preservation, without propagating gravity or gravity-transfer selection | the momentum constraint is the first populatable gravity constraint at the c-number source-compatibility level; its quotient execution and all gravity propagation remain open |

This is a partial closure of Block 122's next gate. “The momentum constraint
is the first populatable gravity constraint” means only equations (17)--(19)
on the displayed finite package. It does not mean that a momentum-sourced OS
quotient, constraint algebra, or gravity transfer has been constructed.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the certified package at both
rational shear fixtures, identity-valued U(1) charge cannot populate the
closed-carrier Gauss image on a nonzero positive state, whereas the displayed
indefinite momentum charge has a nonzero certified-positive paired-momentum
state with zero expected total momentum under either sign convention, so its
c-number source row admits closed-carrier Gauss solutions, while the local
observable wall transfers unchanged under the invertible phase $i^k$.”

Forbidden upgrades include “the constraint quotient is executed,” “the state
is annihilated by the charge,” “energy is conserved per-slice,” and “the
observable wall is broken.” The first confuses incidence-image compatibility
with forming the sourced OS quotient. The second replaces the expectation
equalities in (16) by the vector statement that (16) explicitly refutes. The
third invents a microslice symmetry that does not exist. The fourth ignores
the invertible pin transfer in (21).

Also forbidden are “every momentum state populates the closed carrier,”
“zero momentum is convention-dependent,” “the stress tensor descends,”
“non-local dressings are unnecessary,” “naturality is classified,” “curved
OS positivity holds,” “gravity is coupled,” “an axiom amendment is required,”
and “audit retention follows.” None is established by this calculation.

The runner specification's five resolution lines are reproduced verbatim:

```text
N5: per_element: exact shift-commutation, routed-identity, phase-reduction, definiteness, gauss-image, pin-transfer, and vacuity certificates are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: every momentum sector's shift residual is the invertible phase i^k times the u(1) residual while the quotient momentum charge is indefinite diag(0,1,2,-1)
per_block: the closed-carrier population wall is a definiteness statement — the identity-valued u(1) charge can never vanish on a positive package but the indefinite momentum charge admits nonzero states of vanishing expected total momentum
lattice_wide: checked and not executed — the momentum-sourced gauss quotient execution, non-local dressings for the observable wall, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The result changes the available
closed-carrier source class without weakening Block 122's observable wall.

| route | present status | remaining terminal |
|---|---|---|
| spatial shift-action commutator | exactly zero at both fixtures | none for displayed package |
| routed shift-current identity | exact off-shell equation (7) | none for displayed routing class |
| sector phase reduction | exact $i^k$ multiple of U(1) identity | none for four displayed sectors |
| U(1) total charge | identity-valued and definite | cannot populate closed carrier |
| momentum total charge | exact spectrum $0,1,2,-1$ | no classification beyond displayed quotient |
| paired-momentum state | nonzero and certified-positive | no claim of charge annihilation |
| expected total momentum | exactly zero in both displayed conventions | none for displayed state |
| closed incidence image | exactly the zero-sum subspace | none for displayed carrier |
| momentum source row | in the closed incidence image | execute the sourced OS quotient |
| operator-level constraint | not executed | impose and solve beyond expectation value |
| local momentum observable | same pinned failures as Block 122 | none inside local routed class |
| non-local dressing | untested-live | cancel pin and prove descent/adjointness |
| microslice energy current | no slice symmetry | requires a different action/package |
| Floquet generator | exact but vacuous functional calculus | no new conservation credit |
| transfer contractivity | inherited certified content | none for displayed scalar transfer |
| naturality classification | untested-live | classify surviving sourced package |
| curved OS route | not executed | prove positivity on honest curved carrier |
| gravity constraint quotient | not executed | couple the momentum source and form quotient |

The scan finds no axiom-amendment route. The stress/momentum part of Block
122's handoff is answered only through shift continuity, charge
definiteness, and c-number Gauss-image compatibility. Sourced quotient
execution, non-local dressings, naturality, curved OS positivity, the
completed transporter, and joint gravity remain open.

### N7 — Steelman

**Hostile steelman: expectation-zero is weaker than eigenstate-zero.** The
displayed state is not annihilated by momentum, so it does not solve an
operator constraint $\widetilde P_xv=0$. Why call this a population break?

Agreed about the distinction. Block 121's closed-carrier Gauss population
test is a c-number source equation: solvability asks whether the expected
total source lies in the zero-sum incidence image. For that question,
$\langle\widetilde P_x\rangle=0$ is the right object, and (18)--(19) provide
it exactly. The stronger operator-level constraint is not executed and is
named as the next-layer question. The theorem never substitutes one for the
other.

**Hostile steelman: momentum units and charge conventions are conventional.**
The entry $-1$ can instead be written as the residue $3$. Does the
cancellation depend on which representation is chosen?

The principal Hermitian operator is displayed in units $\pi/2$, and both
the signed-integer and mod-$4$ assignments are shown in (13), (16), and
(18)--(19). The former gives $1+(-1)=0$ as an ordinary integer equality.
The latter gives $1+3=0\pmod4$. Both exponentiate to the same shift phase.
Thus the convention is exposed rather than hidden, and the cancellation is
certified in the coefficient group appropriate to each representation.

**Hostile steelman: the quotient is tiny.** A four-sector, rank-one-per-sector
package can expose a cancellation that does not survive a richer carrier, a
different action, or an operator-level constraint.

Agreed. W1 and its break apply only to the displayed finite quotient, both
fixtures, the exact charges in (13), and $v_\star$. A richer quotient must
recompute its charge spectrum, positive cone, incidence image, and local
observable tests. The present result supplies a certified existence witness
for this package, not a universal momentum-population theorem.

These steelmen preserve narrow W1 while keeping the positive result honest:
expectation-zero solves the posed c-number compatibility condition, the sign
and units are explicit, and no inference is exported beyond the tiny
certified quotient.

### N8 — Cross-Cycle Echo

The immediate campaign chain first built the positive carrier, then separated
continuity, population, and observable descent. This block resolves the
charge-definiteness fork without collapsing those layers.

| campaign block | narrowing that leads to W1 and the positive break |
|---|---|
| [Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | supplied the certified rank-one positive half-space quotient and contractive scalar transfer |
| [Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md) | proved microscopic routed-current continuity and found the norm-valued U(1) closed-carrier population wall |
| [Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | proved that the local routed U(1) current does not descend to a conserved quotient observable and named stress/momentum as the next source route |
| Block 123 | proves exact shift continuity, identifies the U(1) wall as definiteness, exhibits the positive momentum population break, and transfers the observable pin |

The present result does not reuse observable descent to prove population.
It uses the exact charge spectra and zero-sum incidence image. Conversely, it
does not reuse population to repair observable descent. It uses the
invertible $i^k$ relation to preserve that wall.

**No-Go Discipline verdict:** **PASS** only for narrow W1: on the certified
package at both rational shear fixtures, no identity-valued total charge can
populate the closed carrier on a nonzero positive state. The displayed
indefinite momentum charge and paired-momentum state are a **POSITIVE** break
at the c-number expectation level, under either sign convention. The local
observable wall remains exact under the sector phase. The per-period energy
statement is **VACUOUS** beyond inherited contractivity. **FAIL** for “the
constraint quotient is executed,” “the state is annihilated by the charge,”
“energy is conserved per-slice,” “the observable wall is broken,” a non-local
dressing, naturality, curved OS positivity, a completed ADM/history
transporter, joint gravity, axiom necessity, audit retention, obligation
retirement, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. Shift-action commutation, the routed
divergence identity, momentum-sector reduction, the charge spectra, the
paired-state expectations, the closed-incidence image, the transferred
observable witnesses, and the Floquet functional-calculus classification are
finite consequences of the displayed action, carrier, fixtures, and
certified quotient. No new primitive is assumed.

This is bounded route closure, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. execute the momentum-sourced Gauss quotient on the closed carrier with
   the vanishing-expectation state class, keeping expectation-level and
   operator-level constraints explicit;
2. construct non-local dressings for the local-observable wall and test Ward
   compatibility, null descent, and reflection-adjointness; and
3. classify naturality and execute curved-carrier OS positivity on whichever
   honest sourced and dressed package survives.

The actual ADM/history transporter remains unexecuted beyond the displayed
half-space positive package, its contractive scalar transfer, the microscopic
routed-current identities, the local quotient-observable obstruction, and
the c-number momentum population break.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted on a momentum-populated
carrier.
