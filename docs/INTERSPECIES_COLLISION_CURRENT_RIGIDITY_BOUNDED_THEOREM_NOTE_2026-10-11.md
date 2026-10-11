---
claim_id: interspecies_collision_current_rigidity_bounded_theorem_note_2026-10-11
title: Interspecies-only collision invariants and common current coefficients in three dimensions
date: 2026-10-11
claim_type: bounded_theorem
claim_scope: "Classify C1 scalar charges conserved on every local regular interspecies collision shell under full affine span of both velocity images; derive a common quadratic current coefficient only under the additional stated current and individual cubic-symmetry hypotheses."
upstream_dependencies: []
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Prove the common-coefficient collision-invariant step for interspecies-only scattering."
source_of_blocker_text: historical_C1_report_at_d009fb786d36a6cab4a7d410630b9382992faa08
artifact_role: theorem
status: provisional
promotion_path: "Source-bound publication review followed by the independent audit path; a physical application separately requires the named shell-selection, domain and current-identification hypotheses."
runner: scripts/interspecies_collision_current_rigidity_2026_10_11.py
independent_review: completed_for_frozen_I1_I24_source
scoped_lean_status: six_finite_geometry_declarations_compiled_and_independently_statement_reviewed
publication_composition_review: completed_with_root_control_strengthening
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A self-contained mathematical implication under explicit regularity, collision-shell and velocity-image premises, with additional current and symmetry premises for the application."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Interspecies-only collision invariants and common current coefficients

**Status:** provisional. **Current surface:** conditional-support.

The theorem below proves the common-coefficient conclusion under the explicit
regular-shell and full-affine-span hypotheses I1–I3. It uses no AA or BB
collision identity. Connected momentum domains integrate the resulting
gradients; connectedness of the velocity images is not required.

The current corollary additionally supplies the identification
\(J_s=E_s\nabla E_s\), conservation of its components, and individual scalar
cubic symmetry on the specified domains. Its common quadratic coefficient
is nonzero but need not be positive. A physical collision measure and its
selection rule, the domain hypotheses and the current identification remain
conditions to match in an application. No microscopic scattering law,
collision clock, native gravity law or retained-status decision follows here.

The complete I1–I24 source has received a selective independent mathematical
review. Six finite-geometry Lean declarations have separately received a
statement-and-evidence review. Those distinct completed scopes are recorded
in Sections 11–12; neither formalizes the full theorem. Root checked this
publication composition against the frozen sources and strengthened one
finite control after a deliberate wrong-sign mutation survived. The complete
mathematical argument is unchanged; Section 10 records that test limitation.

## 1. Mathematical contract and historical provenance

The mathematical proof is self-contained in Sections 2–9. Its inputs are
two real C1 scalar energies and scalar charges on connected open subsets of
three-dimensional momentum space, full affine span of each velocity image,
and every local regular AB collision-shell charge identity. The conclusion
has one common energy coefficient, one common momentum coefficient, and
independent species constants. Equal velocities, repeated labels and the
exceptional opposite-line configurations are included. Sections 6–8 state
the extra conditions for the measure, symmetry and current consequences.

The proposed scientific base is main
`a13caa4885f547c8d206265b031ba7649e539fd9`. No theorem from candidate PR9476
is a mathematical dependency. The historical C1 report at
`d009fb786d36a6cab4a7d410630b9382992faa08`, lines 136–142, motivated the
interspecies-only step; its earlier same-species argument and its other
cohomology, analytic-band, obstruction and approximation claims are not
imported. No cited collision-invariant theorem from that report is used.
The proof uses finite-dimensional geometry, the C1 regular-level theorem,
continuity and integration of a zero gradient on a connected open set.

The frozen authored source is `INTERSPECIES_CURRENT_RIGIDITY_PROBE.md`,
SHA-256 `ca44d1c852e6cd0437cf9e98913fb5fb106abb1b42567c68fb6bf3e9a60c80b8`.
Sections 2–9 below are copied byte for byte, preserving all I1–I24 arguments
and adverse cases. The source-composition map records the new frontmatter,
this provenance presentation, evidence-link relocation and the updated
review status. Original sources and their historical pending-status text
are preserved as deterministic gzip copies in the evidence packet.

The complete historical C1 report and both referee versions were read in
the derivation and its mathematical review. They identify provenance and
the original unresolved step; they do not enlarge this theorem's premises
or certify the rest of the candidate-law proposal.

## 2. Statement with a precise shell hypothesis

Let \(O_A,O_B\subset\mathbb R^3\) be nonempty connected open sets. Let
\(E_s,F_s\in C^1(O_s;\mathbb R)\), for \(s=A,B\), and put

\[
 v_s=\nabla E_s,\qquad p_s=\nabla F_s,\qquad X=v_A(O_A),\quad Y=v_B(O_B).
 \tag{I1}
\]

Assume

\[
 \operatorname{aff}X=\operatorname{aff}Y=\mathbb R^3.
 \tag{I2}
\]

For every \(a\in O_A,b\in O_B\) with \(v_A(a)\ne v_B(b)\), let \(K=a+b\).
The **local regular-shell hypothesis** is that for every \(q\) sufficiently near
\(a\), with \(q\in O_A,K-q\in O_B\),

\[
 E_A(q)+E_B(K-q)=E_A(a)+E_B(b)
 \quad\Longrightarrow\quad
 F_A(q)+F_B(K-q)=F_A(a)+F_B(b).
 \tag{I3}
\]

The neighborhood may depend on \((a,b)\). A pointwise identity for all normal
AB collisions implies I3. Conservation is for lifted momentum, with no modular
identification or umklapp in this hypothesis. The two domain shapes need not
coincide. Elastic AB collisions preserve one particle of each species.

**Theorem.** Under I1–I3 there are real \(\lambda,c_A,c_B\) and
\(\mathbf b\in\mathbb R^3\) such that

\[
 F_A(k)=\lambda E_A(k)+\mathbf b\cdot k+c_A,\qquad
 F_B(k)=\lambda E_B(k)+\mathbf b\cdot k+c_B.
 \tag{I4}
\]

Conversely, I4 satisfies every energy- and lifted-momentum-conserving elastic
AB collision identity. Thus this is a classification under the stated
hypotheses. The coefficients \(\lambda,\mathbf b\) are unique: two choices
would give \((\lambda-\lambda')x+(\mathbf b-\mathbf b')=0\) for all \(x\in X\),
which is incompatible with I2 unless both differences vanish.

## 3. From regular shells to cross-species parallel secants

Fix the pair \((a,b)\) in I3 and define on the open set
\(O_A\cap(K-O_B)\)

\[
 \Omega(q)=E_A(q)+E_B(K-q),\qquad G(q)=F_A(q)+F_B(K-q).
 \tag{I5}
\]

At \(a\), \(\nabla\Omega=v_A(a)-v_B(b)\ne0\). The C1 implicit-function theorem
gives a local two-dimensional level surface of \(\Omega\), whose tangent plane
is the kernel of \(\nabla\Omega(a)\cdot{}\). I3 makes \(G\) constant on that
surface, so its derivative vanishes on this tangent plane. Its gradient is
therefore a scalar multiple of the normal:

\[
 p_A(a)-p_B(b)=\lambda_{ab}\,[v_A(a)-v_B(b)]
 \quad\text{whenever }v_A(a)\ne v_B(b).
 \tag{I6}
\]

This uses only first derivatives of \(E_s,F_s\). It does not differentiate the
multiplier, invert the velocity map, assume a Hessian is nonsingular, or assert
an equation at an equal-velocity pair. The latter pairs are recovered by the
geometric argument below.

## 4. A labeled complete-bipartite rigidity lemma

Here labels may have identical velocities. Suppose each A label \(a\) carries
vectors \((x_a,P_a)\), and each B label \(b\) carries \((y_b,Q_b)\), in
\(\mathbb R^3\). Assume their velocity images both have full affine span and

\[
 P_a-Q_b\in\operatorname{span}(x_a-y_b)
 \quad\text{for every pair with }x_a\ne y_b.
 \tag{I7}
\]

No assumption is made on \(P_a-Q_b\) when \(x_a=y_b\), and no assumption says
that \(P_a\) or \(Q_b\) is already a function of velocity. Then

\[
 P_a=\lambda x_a+\mathbf b,\qquad Q_b=\lambda y_b+\mathbf b
 \quad\text{for every label},
 \tag{I8}
\]

for a single scalar \(\lambda\) and vector \(\mathbf b\).

### 4.1 Existence and rigidity of one noncoplanar four-cycle

Choose distinct \(x_1,x_2\) from the A image. Choose \(y_1\) outside their
line and \(y_2\) outside the plane through \(x_1,x_2,y_1\). Full affine span of
the B image supplies both choices. These four points are affinely independent,
and in particular all four cross edges are nonzero. Write their four I7
multipliers as \(\lambda_{ij}\). The cycle identity is

\[
 0=\lambda_{11}(x_1-y_1)-\lambda_{21}(x_2-y_1)
    +\lambda_{22}(x_2-y_2)-\lambda_{12}(x_1-y_2).
 \tag{I9}
\]

The four point coefficients are

\[
 \lambda_{11}-\lambda_{12},\quad -\lambda_{21}+\lambda_{22},\quad
 -\lambda_{11}+\lambda_{21},\quad-\lambda_{22}+\lambda_{12}.
 \tag{I10}
\]

They sum to zero. Affine independence forces each to vanish, so all four
multipliers agree. Setting \(\mathbf b=P_1-\lambda x_1\) gives I8 at all four
anchor labels. This replaces the same-species triangle argument; no triangle
edge between two labels of the same species has been used.

### 4.2 What the two opposite anchor lines permit

Let

\[
 L_X=x_1+\mathbb R u,\quad u=x_2-x_1,\qquad
 L_Y=y_1+\mathbb R v,\quad v=y_2-y_1.
 \tag{I11}
\]

The two lines are skew: they are disjoint, their directions are independent,
and they are not coplanar. Subtract the homothety in I8 and write the residuals
as \(r_a=P_a-\lambda x_a-\mathbf b\),
\(s_b=Q_b-\lambda y_b-\mathbf b\).

Comparison with the two known B anchors shows:

\[
 x_a\notin L_Y\Longrightarrow r_a=0,\qquad
 x_a\in L_Y\Longrightarrow r_a\in\mathbb R v.
 \tag{I12}
\]

Indeed, off the line the two nonzero spans \(\mathbb R(x_a-y_1)\) and
\(\mathbb R(x_a-y_2)\) are distinct, with zero intersection. On the line,
at least one edge is nonzero, even if \(x_a\) equals one anchor, and gives
the asserted one-dimensional residual. The same argument gives

\[
 y_b\notin L_X\Longrightarrow s_b=0,\qquad
 y_b\in L_X\Longrightarrow s_b\in\mathbb R u.
 \tag{I13}
\]

This accounts explicitly for the zero cross edges at equal velocities. It
also applies separately to every label at a repeated velocity.

### 4.3 Eliminating every exceptional residual

Choose a B velocity \(y_*\notin L_Y\), which exists by its full affine span.
For an A velocity \(x\in L_Y\), there are two cases.

If \(y_*\notin L_X\), I13 gives \(s_*=0\). I7 then makes \(r_x\) both
parallel to \(v\) and parallel to \(x-y_*\). Since \(y_*\notin L_Y\), these
directions differ; hence \(r_x=0\).

If \(y_*\in L_X\), then \(s_*\in\mathbb R u\), while
\(r_x\in\mathbb R v\). Skewness implies

\[
 x-y_*\notin\operatorname{span}(u,v).
 \tag{I14}
\]

To see this, subtract the line parameters from an alleged inclusion: it would
put \(y_1-x_1\) in \(\operatorname{span}(u,v)\), making all four anchors
coplanar. But I7 places \(r_x-s_*\) in the span of \(x-y_*\), whereas I12–I13
place it in \(\operatorname{span}(u,v)\). Thus \(r_x-s_*=0\). Independence of
\(u,v\) then gives \(r_x=s_*=0\). The pair is regular because skew lines do
not meet.

All A residuals now vanish. Choose an A velocity \(x_*\notin L_X\). For
any remaining B velocity \(y\in L_X\), I7 makes \(-s_y\) parallel to
\(x_*-y\), and I13 makes it parallel to \(u\). Those directions differ, so
\(s_y=0\). All other B residuals had already vanished.

This proves I8, including all equal-velocity labels. No connectedness,
continuity, density, or generic-position claim about the entire images was
needed. Only the finite anchor and the two extra choices entered. Full affine
span of both images is a sufficient condition, not a claimed sharp condition;
some lower-dimensional image pairs also satisfy this finite anchor argument.

## 5. Completion of the collision-invariant theorem

Apply the lemma to the momentum labels and I6. It gives

\[
 \nabla F_s=\lambda\nabla E_s+\mathbf b,\qquad s=A,B.
 \tag{I15}
\]

The function \(F_s-\lambda E_s-\mathbf b\cdot k\) has zero gradient. Any two
points in a connected open subset of Euclidean space can be joined by a
polygonal path in it; integration along its segments makes the function
constant. These constants are \(c_A,c_B\), giving I4. This is the sole use of
connectedness of the momentum domains. Their velocity images are automatically
connected by continuity, but that fact is not needed in Section 4.

The converse follows by inserting I4: the defect is \(\lambda\) times the
energy defect plus \(\mathbf b\) dotted with the momentum defect, and the
two species constants cancel. There is no relation between \(c_A,c_B\) because
the permitted collisions preserve the two species counts separately.

## 6. Precisely when an almost-everywhere amplitude statement suffices

Use variables \((K,a,c)\in\mathbb R^9\), with
\(a,c\in O_A\), \(b=K-a,d=K-c\in O_B\), and define

\[
 \Phi(K,a,c)=E_A(a)+E_B(b)-E_A(c)-E_B(d),\qquad
 \Delta F=F_A(a)+F_B(b)-F_A(c)-F_B(d).
 \tag{I16}
\]

Let \(\mathcal M_{rr}\) be the set \(\Phi=0\) on which both
\(v_A(a)\ne v_B(b)\) and \(v_A(c)\ne v_B(d)\). It is an eight-dimensional
C1 manifold: already the \(a\) derivative of \(\Phi\) is the first nonzero
relative velocity. It contains the diagonal collision \((c,d)=(a,b)\) at
each regular incoming pair, and all sufficiently close collisions on its
local shell remain in \(\mathcal M_{rr}\).

Assume a Borel measure \(\mu\) has full support on \(\mathcal M_{rr}\): every
nonempty relatively open subset has positive measure. Also assume a measurable
amplitude \(T\) obeys the actual charge-conservation selection rule

\[
 T\,\Delta F=0\quad\mu\text{-almost everywhere},\qquad
 T\ne0\quad\mu\text{-almost everywhere}.
 \tag{I17}
\]

Then \(\Delta F=0\) almost everywhere. Its continuity upgrades this to
\(\Delta F=0\) at every point of \(\mathcal M_{rr}\): a nonzero value would
give an open neighborhood where its absolute value is bounded below, in
contradiction with full support. I3 follows by restricting to each local shell.
No continuity of \(T\) is needed. A matrix amplitude is also allowed if
\(\Delta F\) is scalar and the matrix is nonzero almost everywhere.

For example, induced eight-dimensional surface measure, or a locally positive
chart density equivalent to it, has this support property. The argument uses
the joint collision manifold and continuity, so a separate assertion about
almost every fixed shell is unnecessary. If a physical formulation starts with
conditional shell measures, it must show that the resulting joint measure
has the required support. Ambient twelve-dimensional Lebesgue measure would
be inappropriate: the constrained collision manifold has zero ambient measure.

C1 H4's phrase “nonzero almost everywhere on the normal on-shell set” must be
interpreted relative to such a measure. H3 must supply I17 as a valid
asymptotic charge selection rule. This note proves the implication from these
precise statements; it does not derive either statement from a microscopic
law, or infer them merely from a nonzero sampled amplitude. Open sets of zero
amplitude or a collision measure with deficient support leave I3 unproved.

## 7. What cubic covariance does and does not supply

### 7.1 A sufficient symmetry hypothesis

Let \(O\) be a nonempty connected open set invariant under the 24 proper cubic
rotations, and let a single scalar band satisfy
\(E\in C^1(O)\), \(E(Rk)=E(k)\), and be nonconstant on \(O\). Then

\[
 \nabla E(Rk)=R\nabla E(k),\qquad
 \operatorname{aff}(\nabla E(O))=\mathbb R^3.
 \tag{I18}
\]

Proof: nonconstancy on a connected open set implies a nonzero gradient somewhere.
The velocity image contains the proper cubic orbit of that nonzero vector.
The orbit average is zero, since the only vector fixed by the three half-turns
about the coordinate axes is zero. The orbit's linear span is all of
\(\mathbb R^3\): for a vector with a nonzero first coordinate, adding it to its
half-turn about that axis isolates a nonzero multiple of the first axis;
proper rotations carry this to the other axes. A coordinate permutation first
handles whichever original coordinate is nonzero. Since zero is the orbit
average, its affine span equals its linear span. This proves I18.

There is another sufficient condition when the displayed regular set is not
invariant. Suppose \(E\) is defined and cubic invariant on the entire invariant
open cube \(U\), and \(O=U\setminus S\) is connected and dense in \(U\), with
\(E\in C^1(O)\) nonconstant there. At any \(k\in O\), symmetry supplies a C1
extension to \(RO\), with derivative \(R\nabla E(k)\) at \(Rk\). Density of
\(O\) gives a sequence from \(O\cap RO\) tending to \(Rk\), so this rotated
velocity belongs to the closure of \(\nabla E(O)\). An affine subspace of
\(\mathbb R^3\) is closed. It must therefore contain the entire nonzero orbit,
and again has full affine span. Here density follows, for instance, if the
closed exceptional set has empty interior. Global symmetry means equality of
the actual function on \(U\), not an unrelated extension chosen afterward.

Both statements require scalar covariance of the individual species. Covariance
that merely permutes several species need not give each individual velocity
image full span. For example, the three smooth bands \(E_j(k)=k_j^2\) form a
cubic-covariant family under permutation of axes, but each velocity image lies
on a single line. This is a hypothesis discriminator, not a claim about a
specific physical multiplet.

### 7.2 The literal connected-domain statement is insufficient by itself

C1 H5 states that \(S\) is closed and \(U\setminus S\) connected. It does not
expressly state that the regular domain is rotation invariant or that \(S\)
has empty interior. Neither follows solely from connectedness and closedness.
Nonconstancy in Section 7.1 is understood on the regular domain. In an
intended application where \(S\) is an invariant cone or
crossing set, Section 7.1 may supply the needed geometry, but that fact should
be stated for the actual domain.

An explicit counterexample to the unqualified domain-to-image inference is as
follows. Choose \(q=(1,2,3)/5\) in \(U=(-\pi,\pi)^3\). Its 24 cubic images
are distinct, and their minimum squared separation is \(6/25\). Let
\(r=1/100\), \(D=B(q,r)\), and choose a smooth radial cutoff \(\chi\), equal
to one on the radius-\(r\) ball and zero outside the radius-\(2r\) ball.
All rotated support balls are disjoint and lie in \(U\). Set

\[
 E(k)=10+\frac12\sum_{R\in\mathcal O}
 \chi(R^{-1}k-q)\,[(R^{-1}k)_1]^2.
 \tag{I19}
\]

This is a globally smooth, nonconstant, cubic-invariant real function. On
\(D\) it is exactly \(10+k_1^2/2\), so its velocity image there is an interval
of the first coordinate axis. Taking \(S=\mathbb R^3\setminus D\) gives a
closed set with \(U\setminus S=D\) connected and with all the displayed
regularity. Thus those domain clauses alone do not imply I2. The cutoff may
be made with the usual smooth plateau obtained from \(e^{-1/t}\) for \(t>0\)
and zero for \(t\le0\); no analytic regularity is asserted.

This construction does not refute the full C1 physical theorem: it isolates a
geometric inference about a chosen regular domain. In this example the actual
maximal smooth domain is larger, and a separate physical scattering hypothesis
on that larger domain may restore the needed constraints. It shows exactly why
one must specify the regular domain used for the collision theorem.

## 8. Conditional common-coefficient energy-current corollary

In addition to the theorem's hypotheses for the two energies, suppose
\(E_s^2\in C^2(O_s)\), and the vector charges

\[
 J_s=E_s\nabla E_s=\tfrac12\nabla(E_s^2)
 \tag{I20}
\]

satisfy I3 componentwise for AB collisions. This is the current-symbol and
additive-conservation input from the C1 reduction, taken explicitly as a
conditional premise here. It is not rederived from the lattice axioms.

Apply I4 to each of the three components. The common scalar and momentum
coefficients for each component form a common vector \(a\) and a common
matrix \(B\), while the species constants form vectors \(c_s\):

\[
 J_s(k)=a E_s(k)+Bk+c_s,\qquad s=A,B.
 \tag{I21}
\]

Symmetry of the Jacobian of \(J_s=\nabla(E_s^2/2)\) gives

\[
 a_i(v_s)_j-a_j(v_s)_i+B_{ij}-B_{ji}=0.
 \tag{I22}
\]

Subtract at two momenta. If \(a\ne0\), every difference of two velocities
would be parallel to \(a\); this contradicts full affine span. Hence \(a=0\)
and \(B\) is symmetric. Integration on each connected domain gives

\[
 E_s(k)^2=k^T Bk+2c_s\cdot k+e_s.
 \tag{I23}
\]

Now also suppose each \(O_s\) is invariant under proper cubic rotations and
each scalar \(E_s\) is invariant under them. The polynomial obtained by
subtracting I23 at \(Rk\) and \(k\) vanishes on a nonempty open set. Its
coefficients therefore vanish: \(R^TBR=B\), \(R^Tc_s=c_s\). Half-turns remove
the off-diagonal entries of \(B\) and all entries of \(c_s\); quarter-turns
equate the three diagonal entries. Thus

\[
 E_A(k)^2=e_A+\beta |k|^2,\qquad
 E_B(k)^2=e_B+\beta |k|^2,\qquad J_s(k)=\beta k.
 \tag{I24}
\]

The same \(\beta\) occurs for both species without self-scattering. It is
nonzero when the energies are nonconstant on their connected domains: otherwise
each continuous real energy has constant square and hence is constant there.
The real constants \(e_s\) are not assigned an interpretation beyond I24.

Cubic symmetry does not fix the sign of \(\beta\). For example,
\(E_s(k)=\sqrt{C_s-|k|^2}\) on a sufficiently small ball has \(\beta=-1\)
and \(J_s=-k\), which is conserved in every momentum-conserving AB collision.
Positivity of the quadratic coefficient requires an additional minimum or
curvature premise. Extension through excluded singular points requires
continuity there. No claim concerning every mediator, nonscalar scattering
blocks, gapless non-particle sectors, or a finite-network obstruction follows
from this note alone.

## 9. Adverse cases and routes that were not used

**Collinear images can support extra actual collision invariants.** On any
common connected open domain take \(E_A=E_B=10+k_1^2/2\) and \(F_A=F_B=k_1^3\).
For a normal AB collision, conservation of the first momentum component and
of energy fixes the unordered pair of first coordinates: their sum and sum
of squares fix the two roots of a quadratic. Thus the cubic charge sum is
also conserved. Yet on an open set \(k_1^3\) cannot equal
\(\lambda(10+k_1^2/2)+\mathbf b\cdot k+c_s\). Both velocity images are
connected intervals, showing that image connectedness alone is inadequate.
This does not show that full three-dimensional span is a necessary condition;
the theorem asserts sufficiency only.

**A deficient measure cannot supply pointwise identities.** For
\(E_A=E_B=|k|^2/2\), \(F_A=F_B=k_1^3\), the collision
\((a,b)=((1,0,0),0)\) to
\((c,d)=((1/2,1/2,0),(1/2,-1/2,0))\) conserves momentum and energy, with
charge defect \(3/4\). A measure supported only on the regular diagonal
collision with incoming \((a,b)\) has \(T=1\) and \(T\Delta F=0\) almost
everywhere, while the pointwise conclusion fails elsewhere. This is a precise
missing-full-support witness, not a physical choice of scattering measure.

**A same-species triangle proof was unavailable.** The source's triangle
edges would require relations between two A labels or two B labels. The
four-cycle proof above supplies a different mechanism. A coplanar K2,2 alone
does not fix one homothety: opposite vertices of a square admit independent
stretching in the two coordinate directions. The finite controls retain this
example. Likewise one cannot skip the exceptional-line extension; an added
A point on the B anchor line has an extra degree of freedom until further
B velocities constrain it.

**Differentiating an unknown velocity map was unnecessary.** The gradient map
need not be injective, open, or have nonsingular Hessian. The proof uses
momentum labels throughout, so it does not assume that a charge gradient was
already a single-valued function of velocity. All equal-velocity labels are
forced to agree only at the conclusion.

No theorem in two dimensions, no classification of all deficient-affine-span
configurations, and no result for merely measurable charges is claimed.
There is no quantitative stability estimate for approximately conserved
charges; the noncoplanar anchor can become ill-conditioned. These are distinct
extensions, rather than hidden premises in the exact statement.

## 10. Exact finite controls and publication replay

The [control source](../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/interspecies_current_rigidity/rigidity_controls.py) uses
only Python's standard library and exact rational arithmetic. It constructs
the full constraint matrix of
\((P_a-Q_b)\times(x_a-y_b)=0\), omitting equal-velocity edges, and computes
its rank by rational Gaussian elimination. This is a different finite
formulation from the geometric proof, authored in this same derivation task;
it is not an independent reviewer or a continuum proof.

| Finite configuration | Unknowns | Exact nullity | Meaning |
|---|---:|---:|---|
| Noncoplanar K2,2 | 12 | 4 | Three translations and one dilation |
| One anchor edge deleted | 12 | 6 | Incomplete cross information leaves freedom |
| Added A point on the opposite anchor line | 15 | 5 | Exceptional residual is real |
| Added points on both opposite anchor lines | 18 | 4 | Their skew cross edge kills both residuals |
| Full spans, equal velocities, repeated label | 27 | 4 | Equal-edge omissions do not enlarge the kernel |
| Full spans, disjoint velocity images | 24 | 4 | No overlap premise is needed |
| Two collinear image samples | 18 | 8 | Extra invariant gradients remain |
| Coplanar square K2,2 | 12 | 5 | Explicit anisotropic stretch survives |

Additional exact checks enumerate the 24 proper cubic rotations, verify their
closure and zero group average, find the vector fixed space to be zero and
the matrix commutant to be scalar, and check the closed-current constraints
that force \(a=0\). The publication also checks six independent symmetric
matrix modes in the kernel, identifying the full claimed symmetric family.
They verify the \(3/4\) collision defect and the disjoint
orbit-ball separation in I19. These are algebraic controls, not a simulation
or empirical evidence for a physical amplitude. The deleted-edge and
collinear cases are intentional adverse inputs, not claims that separate
mutated-source executions were performed.

The original author helper's first formal run completed successfully under a 30-second timeout; its
full output and environment are preserved in
[controls.log](../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/interspecies_current_rigidity/controls.log) and
[execution.json](../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/interspecies_current_rigidity/execution.json).
The [receipt](../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/interspecies_current_rigidity/receipt.json) binds all source and
output identities and records reading/search limits and initial truncated
displays. No frozen input or repository file was edited.

The mathematical common-coefficient step is proved under I1–I3, with I24
as an additional current-and-symmetry corollary. Its independent mathematical
review is complete at the frozen identities in Section 11. Matching a
particular species/domain/measure construction to Sections 6–8 remains
an application obligation. The result makes no retained-status decision
and does not import the other C1 claims into a native-gravity conclusion.

The publication primary preserves the complete executable author-control
body without dynamic-code wrapping. Its added metadata declares the note
as the checked claim contract. Its summary counts fourteen completed finite
check families: eight matrix configurations and six algebraic families.
That count is not a count of proof obligations or assertions.

The frozen external packaging replay completed thirteen families. In root's
first seven whole-primary semantic mutations, changing the closed-current
curl sign survived: rank six and vanishing energy coefficient alone did not
distinguish symmetric from antisymmetric off-diagonal coefficients. The final
primary appends six explicit symmetric basis modes and checks their linear
independence and membership in the kernel. Together with the original rank,
these checks identify that finite kernel. The I1–I24 analytic proof and the
entire original helper body are unchanged. Both the surviving execution and
the strengthened-source mutation runs are preserved. They are finite tests,
not a replacement for the continuum argument or independent mathematical
review. The separate delivery record gives final canonical-cache,
mutation and repository-conformance outcomes.

## 11. Completed mathematical review

`INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md`, SHA-256
`78c3bc3c8f223b988713cb5bd5210c1a801e8cdc5f428ee648d6284c400d97d6`,
read all 559 source lines and reconstructed the I1–I24 argument before
opening the author's finite-control source and logs. It found no
consequential mathematical defect under the explicit hypotheses and requested
no source repair. It did not certify a physical measure or current law.

The review used a nonorthogonal tetrahedron and parameterized skew-line
calculation, and separately derived the charge constraints from actual
quadratic interspecies collisions with distinct masses. Its fifteen exact
controls used SymPy; they were not a rerun of the standard-library author
helper and do not replace the unrestricted C1 proof. The proof text and its
finite expected outcomes were visible during reconstruction, so the review
does not claim blind discovery. Its preserved receipt is
`interspecies_current_rigidity_review/receipt.json`, SHA-256
`1c3c02926c6c35277fdde7a4b174b85d2471c3c3ec4da9d39681a3c9f2f68de7`.

The review's remaining application conditions are exactly the supplied
individual scalar bands and regular domains, the velocity-image hypothesis
or the checked cubic-domain alternatives, a full-support collision measure
with the selection identity, and the current identification and conservation.
Positivity of the common coefficient and extension across excluded points
need their additional hypotheses in Section 8.

## 12. Scoped Lean evidence and its independent statement review

`RigidityGeometry.lean`, SHA-256
`c72e7a9a961d1eec1ff60842ac3e8a5530c8b71dfc1505dc098d7cab780044df`,
contains six general finite-geometry theorems over an arbitrary field and
module. They cover the four-point affine coefficient adapter, equality of
the four cross-edge multipliers, the four-anchor homothety, elimination of
residuals on parameterized opposite skew lines, exclusion of their cross
direction from the two-direction span, and disjointness of those lines.
The residual-elimination theorem assumes explicit line parameterizations
and residual-direction equations; the last two are consequences for those
parameterized lines.

This covers the chosen four-anchor cycle of I9–I10, the specified exceptional
branch around I14 and those finite consequences. It does not formalize
anchor extraction, off-line confinement I12–I13, the other exceptional-case
branch, final propagation to all labels, or the full I7–I8 lemma. Shell
differentiation, the measure upgrade, integration, cubic symmetry, current
identification and the remainder of I1–I24 also remain outside its scope.

The same author as the source proof supplied this formalization and its
eight rational control theorems. The preserved successful compiler evidence
uses Lean 4.35.0-rc4 and mathlib
`939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716`. The final inventory for all
six principal and eight control theorems lists exactly `propext`,
`Classical.choice` and `Quot.sound`. It does not contain accepted `sorry`
or `admit` proofs, custom axioms, `unsafe` or `native_decide`. The ordinary
cached upstream library was reused, not fully rebuilt or manually verified.

The independent `LEAN_RIGIDITY_STATEMENT_REVIEW.md`, SHA-256
`14d5a11bf7476975b8067fd5d9c7f9e91381804a1b926fb324ff5b9bfd57b519`,
read the complete statements, proof source, controls, scope maps and compiler
history, with the stated pinned library definitions. It found no
consequential statement mismatch or proof defect in the six declarations
and requested no repair. It did not rerun Lean. Its receipt is
`interspecies_rigidity_lean_review/receipt.json`, SHA-256
`974549d47ca67a1f82591d5cef2ab3fa3a2d5854b3b2404dfa58f265364c00a6`.
This is independent statement-and-evidence inspection with the preserved
author compiler runs, not an independent repeat compilation or a complete
formalization of the collision theorem.

The complete recorded compiler history has nine executions: two successful
principal versions, one failed initial positive-control version, one
successful corrected control version, one successful axiom inventory and
four deliberate false-statement rejections. The initial control attempt
omitted an explicit `Finset.univ` argument; its type error, unsolved goal
and printed `sorryAx` dependencies remain in `logs/controls01.*` as failed
evidence. The correction did not change the principal geometry proof.
The four false statements reach their intended mathematical `False` goals
with exit 1 after importing verified witnesses; they are not mutations of
the entire primary or the principal Lean source. A rejected preliminary
runtime-identity command created no process or artifact and is separately
recorded in the scope report. No runtime or installed dependency is copied
into this publication packet.

## 13. Source identities, reproduction and remaining scope

The intended evidence root is
`.claude/science/physics-loops/toe-interspecies-rigidity-20261011/`.
`SOURCE_COMPOSITION.json` maps exact historical fragments, replacement
presentation, original and publication line ranges and byte identities.
`reconstruct.py` rebuilds the frozen external note and primary from those
local fragments and preserved originals; `receipt.json` records the author's
external composition checks. `PUBLICATION_EDITS.json` then maps every root
publication edit to the final repository note and strengthened primary.
Gzip source copies decode to exact historical Markdown bytes, including
obsolete pending-review text. `ROOT_COMPOSITION_REVIEW.md` distinguishes
source preservation from mathematical review and documents the test repair.

| Evidence | Preserved relative path under the evidence root | Scope |
|---|---|---|
| Original full I1–I24 proof | `historical/INTERSPECIES_CURRENT_RIGIDITY_PROBE.md.gz` | All mathematics and original evidence/status prose |
| Mathematical review | `historical/INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md.gz` | Complete selective independent analytic review |
| Author finite controls | `historical/interspecies_current_rigidity/` | Original helper, full output, execution record and receipt |
| Independent finite controls | `historical/interspecies_current_rigidity_review/` | Distinct helper, full output, reconstruction and receipt |
| Scoped author Lean | `historical/interspecies_rigidity_lean/` | Sources, statement map, logs, receipts and failed history; compiled objects omitted |
| Lean statement review | `historical/LEAN_RIGIDITY_STATEMENT_REVIEW.md.gz` and `historical/interspecies_rigidity_lean_review/` | Completed independent scope/statement/evidence review |
| Historical C1 provenance | `historical/repo_sync_rc_2045/` | Exact report/referee copies and original extraction manifest |

Run the standard-library primary from the repository root:

```sh
python3 scripts/interspecies_collision_current_rigidity_2026_10_11.py
```

The algebraic controls alone establish neither the continuum theorem nor a
physical collision amplitude. The theorem remains conditional on its
explicit shell, regularity and full-affine-span premises; the current
corollary retains its further current, symmetry, sign and domain conditions.
No collision clock, loss of coherence, many-body closure or exact
gravitational dynamics is derived by this publication.


## Publication delivery

The [delivery record](../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/DELIVERY_CHECKS.md)
binds source identities, independent review scopes, canonical execution,
actual primary mutations and final repository checks. This main-based note
has no science dependency on the campaign's excluded-walk or transport PRs.
The independent audit path retains responsibility for effective retained
status; this publication applies no audit verdict.

The quantitative companion in this same milestone supplies a stability estimate
for the extension left open by Section 9 of this preserved exact argument.
Its explicit anchor conditioning and derivative-defect premises are separate
from the exact collision identity used here.
