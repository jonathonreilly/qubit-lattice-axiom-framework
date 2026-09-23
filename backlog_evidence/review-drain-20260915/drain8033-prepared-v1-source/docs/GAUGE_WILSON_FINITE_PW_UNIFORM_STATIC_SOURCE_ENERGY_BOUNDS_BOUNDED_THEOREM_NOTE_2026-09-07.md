---
claim_id: gauge_wilson_finite_pw_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07
  - gauge_wilson_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07
  - gauge_wilson_selected_infinite_static_source_sector_bounded_theorem_note_2026-09-07
  - gauge_wilson_finite_pw_static_source_energy_upper_bound_bounded_theorem_note_2026-09-07
claim_scope: "Actual full-irrep PW charged lower bound for distinct connected endpoints, uniform in R>=1, volume and separation; compatible finite-energy upper envelope and separately fixed-R selected-sector consequence under acceptance condition."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The actual full-irrep finite Peter–Weyl carrier has a static-source energy lower bound linear in graph distance, with a common sufficiently small coupling window independent of cutoffR>=1 and ambient volume. The proof reapplies the sector-preserving ground-coordinate argument to each cutoff Hamiltonian, centered on its OWN vacuum energy. It does not subtract two separate variational inequalities.

The [uniform local-dimension gap theorem](GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the unchanged local hypotheses. The [charged coordinate theorem](GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the explicit sector-resolvent method, whose mathematical input remains Yarotsky0411042 Section2. The [finite energy upper theorem](GAUGE_WILSON_FINITE_PW_STATIC_SOURCE_ENERGY_UPPER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the upper envelope only when its acceptance budget is positive. SendingR²/d to infinity at fixedu narrows the upper envelope to the full-unitary trial cost; it does not force the actual charged cost to converge to that value.

A separate EACH-fixed-R consequence uses the [selected-GNS construction](GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md). Under the same positive-acceptance condition the selected charged sector is nonempty and inherits both bounds. No finite charged-minimum convergence, R/volume interchange, representation independence or bottom eigenvector is asserted.

The [canonical helper](../scripts/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.py) performs18 exact controls. It enumerates all243 necessary R1 center flows for each of two cube endpoint pairs, checks ghost and boundary adverse cases, and constructs a positive-perturbation Ritz example where subtracting two increased energies decreases the gap. Center conservation is necessary, not a claim that every flow has a full SU3 intertwiner. Finite controls do not prove the imported coordinate constants. The [exact historical recovery](work_history/repo/review_feedback/pr8033-evidence/README.md) retains every original proof, prospective contract, review, parser failure, flow fixture and output. Both complete positive proofs are given below. Historical reviews, audit/status records and prospective planning are not current theorem or execution authority.

The complete finite-cutoff proof and alternative derivation follow. Their original writing and correction provenance remains in the exact historical recovery. This is a cutoff extension of an explicitly imported perturbative theorem for a supplied model, not a new generic confinement theorem or a hardware construction.

# Uniform finite-PW charged lower bound and its compatible upper estimate

Here a>0 is the supplied temporal-scaling kinetic parameter, not a derived spatial spacing; v, the Wilson dynamics and the source tensor remain supplied model data. This is a reapplication of the explicitly imported charged-coordinate argument to the actual cutoff carrier. It is not a variational comparison between different vacuum energies and is not a new general confinement theorem.

## 1. Exact cutoff model and statement

Let G be a finite oriented cubic-lattice link graph with a subset of its elementary plaquettes, and impose Gauss transformations at every incident vertex, including boundary vertices. Let distinct endpoints x,y lie in the same connected component, with finite graph distance d=d_G(x,y)<infinity. If the endpoints are in different components, the center argument below makes the combined charged fixed space zero; no nonempty finite-energy sector is asserted in that case. Every actual link carries the complete Peter–Weyl sum

 H_(e,R)=directsum_(p+q<=R) V_(p,q) tensor V_(p,q)^*, R>=1.

On the FULL tensor carrier put H_R=K_R+sum_f P_R V_f P_R, with K_e=-3Delta_e/(2a), V_f=v[1-ReTr(U_f)/3], a>0,v>=0. Tr(T_A T_B)=delta_AB, so the one-link electric energies are [p²+pq+q²+3p+3q]/a. Introduce the external source tensor E=C³_x tensor conjugate(C³)_y, or its dual according to the path covariance convention. Let E_0,R be the full-carrier ground energy and E_xy,R the lowest energy in the combined link/source fixed space.

There are positive constants delta,c depending on the fixed cell interaction geometry but not R,G,d or endpoint location, such that, with u=av, r=3u/4 and kappa=3cr, sufficiently small r<delta and kappa<1 imply

 E_xy,R-E_0,R >= (4/a)(1-kappa)d.             (1)

The full ground is unique and gauge invariant in this same regime, so it is the neutral physical ground. The charged sector is nonempty for everyR>=1 independently of the interacting acceptance estimate: the bare fundamental shortest-path transporter times the global Haar vacuum lies in that cutoff source sector.

## 2. Why the imported constants remain uniform in R

The mathematical input is Yarotsky, arXiv:math-ph/0411042, Section2 equations(8)–(15), not merely its unlabelled spectral circles. The paper's local hypotheses allow arbitrary finite or infinite Hilbert spaces and nonnegative onsite operators with a unique vacuum and gap at least1. Theorem1 states range-dependent constants; Section2 uses operator norms, vacuum/excitation projectors and sums over site sets. Its estimates do not count basis vectors, require an onsite upper spectral bound or use representation dimensions. In particular the inverse of a free nonempty-site Hamiltonian is bounded by the reciprocal number of sites, uniformly over the choices of local spectrum. Fix its auxiliary decay parameter once. The resulting unweighted column estimate has the same range-dependent c for all the cutoff models:

 sum_J ||F_(JI) w_I|| <= c r |I| ||w_I||.     (2)

This is the explicit dimension-independent coordinate estimate explicitly imported in the linked uniform-gap and static-source arguments. The current argument retains this mathematical import; it does not infer sector information from a theorem about the full spectrum alone.

Group three outgoing finite link carriers into each cubic cell z. Set h_(z,R)=(a/4)sum_(e tail z)K_e,R. The unique cell vacuum is unchanged and the gap is exactly1 for everyR>=1, because the fundamental and antifundamental remain. Complete-irrep compression preserves Gauss covariance and cannot increase the norm of a centered face interaction. The three plaquettes anchored at z therefore give a centered scaled perturbation of norm at most3u/4 and support within the same Lambda0={0,e1,e2,e3}. The local dimension grows with R, but none of these estimates does.

No comparison E_0,R versus E_0,infinity is made. The coordinate renormalization subtracts the actual ground energy of each cutoff Hamiltonian separately.

## 3. Charged free floor inside the actual cutoff

The cutoff retains whole irreducible representation blocks, including both endpoint matrix indices. Its link label projectors commute with Gauss and K. Fix such a label assignment and call a link occupied when its label is nontrivial. For any connected component of occupied links apply the same SU3 center element to all its vertices. Internal link center factors cancel, and crossing links are trivial. If that component contains exactly one external endpoint, the source tensor acquires a nontrivial center phase, so no invariant vector is possible in that block. Isolated endpoint vertices are included in this argument.

Thus every nonzero charged label block connects x to y with occupied links. It contains at leastd occupied links, each of energy at least4/a even at finiteR. Therefore the charged free floor is at least4d/a. It is attained by a shortest simple fundamental path on the vacuum; each path link carries(1,0) or(0,1), both available for everyR>=1. Branching and triality-zero nontrivial labels do not invalidate the component argument. It is not an assumption that each occupied edge has nonzero triality.

In scaled units, H_0 has floor d on the charged space. Omitting boundary Gauss conditions or allowing extra occupied ghost links would change this argument and is not permitted.

## 4. Equivariant finite creation coordinates and source norm

For the fixed finite cutoff and finite cell set, the imported unique ground has nonzero vacuum overlap. Normalize that overlap to one and write it uniquely as S Omega_0, where

 S=exp(sum_(nonempty I) hat v_I),
 hat v_I=|v_I><Omega_(I,0)| tensor I_(outside I),
 v_I in tensor_(z in I)(H_(z,R) minus vacuum).

These creation operators commute, overlapping products vanish, and the finite sum is nilpotent. Thus S and its inverse are bounded finite polynomials. All spaces here are finite dimensional, so domains introduce no new cutoff difficulty; importantly their similarity norms need not be uniform in volume or R.

Every gauge assignment factors across cells and fixes each cell vacuum. Bare excitation projectors Q_I therefore commute with gauge. Gauge invariance of the overlap-normalized ground and uniqueness of its creation logarithm imply invariance of eachv_I. Hence every hat v_I, S and S^-1 commutes with Gauss, not just their action on the vacuum. The coordinate identity is

 S^-1[(a/4)(H_R-E_0,R)]S=H_0+F.

Tensor with the9-dimensional endpoint space. Expanding one coefficient vector in an orthonormal source basis and applying (2), triangle inequality and Cauchy–Schwarz gives

 sum_J ||(F_(JI) tensor I_E)w_I||
 <=3cr |I| ||w_I||.

The factor3=sqrt9 is independent of every link representation dimension. For coefficient norm ||w||_1=sum_I||w_I||, since H_(I,0)>=|I|,

 ||Fw||_1 <= kappa ||H_0w||_1.               (3)

Each Q_I commutes with combined Gauss, so the charged fixed space decomposes into invariant coefficient blocks. S preserves this space. H_0 has floor d on each nonzero charged block by Section3; the vacuum block is absent for distinct endpoints. The exact fixed-space constraint is preserved even though F can mix the excitation subsets I.

## 5. Restricted resolvent and actual ghost padding

For real0<=z<(1-kappa)d,

 ||F(H_0-z)^-1||_1 <= kappa d/(d-z)<1.

For z<0 the ratio is at mostkappa. A Neumann inverse exists on the charged coefficient space at every such z. Finite-dimensional norm equivalence and bounded similarity transfer invertibility to the actual selfadjoint charged restriction, with no uniform equivalence constant required. This proves (1). It is spectral exclusion, not an assertion that a nonunitary similarity preserves a quadratic form.

For an arbitrary actual finite graph, complete its outgoing cell registers with finite PW ghost links of the SAME R and include enough cells for all retained interaction supports. Retain only actual face perturbations; the enlarged operator is the actual Hamiltonian plus independent ghost electric terms, up to the disclosed centering scalar. Inhomogeneous finite interactions of this shape are allowed by the imported estimate.

Its unique ground factors as actual ground times ghost vacuum. Each bare excitation projection preserves every ghost-vacuum projector. The unique creation logarithm has ghost vacuum in every ghost factor it touches; its rank-one creation map consequently commutes with that ghost-vacuum projector. S, S^-1, H_0 and F preserve their joint range. Apply the restricted resolvent jointly with Gauss and ghost vacuum. Ghost links then cannot create shortcuts, and the free floor is the ACTUAL graph distanced. This finite padding does not assert a thermodynamic result for graph-dependent interaction families.

## 6. Combining the finite energy upper bound without a false limit claim

Choose a shortest distinct-link path of lengthd. The reviewed local-energy theorem applies to this cutoff's full neutral ground. Set

 h_R=R²-floor(R²/4)+3R, theta_bar=8ud/h_R.

When theta_bar<1, combining its upper bound with (1) gives

 1-kappa <= (E_xy,R-E_0,R)/(4d/a)
 <= [1+sqrt(theta_bar)(1+sqrt(8u)+2u)
          +2u sqrt(32u/h_R)]/(1-theta_bar).  (4)

For fixedu in the stated regime, h_R/d tending to infinity makes the right side tend to1, uniformly in the ambient finite graph. Therefore the lower and upper asymptotic envelopes are1-kappa and1. This does NOT prove convergence of the charged minimum, nor equality to the full-unitary path cost. In particular the lower envelope does not approach1 merely by sendingR to infinity at fixedu.

For fixedR the lower bound (1) is uniform for arbitrarily large separation. The sufficient upper normalization budget in (4) is not: it requires h_R>8ud. Thus the theorem does not give a fixed-R upper bound uniform in all d. At u=0, the bare path realizes the exact free threshold for everyR>=1; this is a separate exact control, not an interacting limit argument.

## 7. Optional fixed-R selected infinite-sector consequence

This paragraph uses the fixed whole-range finite-volume family and the explicit weak-resolvent construction of0411042 Theorems2–3, as in the previously reviewed selected-sector theorem. It does not takeR to infinity or identify different cutoffs' GNS states. For EACH fixedR, local algebras are finite dimensional, so local normality and strong continuity of finite-vertex gauge implementations are automatic. The neutral selected state is invariant; its implementing gauge unitaries fix the cyclic vector and commute with the limiting resolvent. The combined source fixed space is closed and reducing.

Every local vector is fixed outside finitely many gauge vertices. Averaging its finite set of relevant gauge transformations yields a bounded local covariant source tuple. Such tuples are dense in the combined fixed space: approximate a fixed vector by local vectors and use the contractive finite average, which leaves the target vector unchanged. Their finite-volume spectral measures have support at or above(4/a)(1-kappa)d by (1), once a fixed shortest path is included. Theorem3 passes their resolvents; testing nonnegative continuous functions compactly supported below the floor and using density passes that spectral exclusion to the infinite fixed space.

If additionally theta_bar<1, the compressed path matrix C_R is a fixed bounded local operator. Its finite ground norms converge by local state convergence and are bounded below by1-theta_bar. Thus the limiting charged vector is nonzero. The normalized finite trial spectral measures converge weakly to its limiting measure by Theorem3, the convergent positive norms and their uniform first-moment bound (4). Portmanteau for the nonnegative energy function gives a limiting form-energy upper bound no larger than that same explicit bound. Hence the selected fixed-R charged sector is nonempty and has both bounds (4) under this acceptance condition.

No charged eigenvector is asserted. No finite charged minima convergence, R/volume interchange or boundary-state identification follows. The lower spectral exclusion remains meaningful whenever the selected fixed space is nonempty; outside the stated acceptance condition this paragraph makes no separate general nonemptiness claim.

## 8. Provenance and limit of the result

This is an explicit dimension-uniform mathematical import applied to a specific finite gauge-covariant carrier, combined with actual center-flow and local-energy arguments. The original charged result's sector proof, rather than its global spectral-circle conclusion, is the load-bearing antecedent. No unused hardware states are included. No native compiler, physical source identification, continuum static potential or axiom-selected coupling is derived. Primary source: https://arxiv.org/pdf/math-ph/0411042, assumptions/Theorem1 and Section2 equations(8)–(15); optional Section7 uses Theorems2–3.


# Appendix: complete alternative two-sided finite-cutoff energy proof

This alternative proof composes the linked charged-coordinate, uniform-gap and finite-cutoff upper-energy arguments for the same supplied lattice Hamiltonian. The full writing history is preserved in exact recovery.

## 1. A separate cutoff argument is necessary

For the full compact Hamiltonian H and cutoff H_R=P_R H P_R, the ordinary variational inequalities E_xy,R>=E_xy and E0_R>=E0 do NOT imply E_xy,R-E0_R>=E_xy-E0. The two subtracted quantities both change. The following lower bound therefore reapplies the quantitative ground-state theorem to H_R itself, rather than transporting an uncut spectral difference by subtraction.

Take a finite cubic link graph with retained elementary faces, complete PW cutoffs p+q<=R, R>=1, and H_R=K_R+sum_f P_R v(1-ReTr U_f/3)P_R. Impose full Gauss transformations at every actual vertex, including boundary vertices. Put u=av and use the same source tensor D=C3 tensor conjugate(C3) of dimension9 used in the charged-coordinate theorem. Source locations x,y are distinct and connected, with actual graph distance d.

## 2. Uniform cell hypotheses and exact gauge preservation

Complete each outgoing cell with three links as in the uniform-gap and charged-coordinate arguments, using decoupled vacuum ghost links where needed. On a cell put h_z=(a/4)sum_(e tail z)K_e,R. The constant Haar vector is its unique zero state. Every nontrivial retained irrep costs at least4/a, and a fundamental irrep is present for every R>=1, so the normalized onsite gap is exactly1 at every R.

Group at most three centered face perturbations per cell. Their compressed norm is at most r=3u/4, because orthogonal compression never enlarges the multiplication norm. The fixed four-cell interaction range is unchanged. The quantitative perturbative theorem of Yarotsky0411042, in the applicability map given in the linked uniform-gap and charged-coordinate arguments, uses a unique local vacuum, a gap lower bound, bounded interaction norm and fixed geometry. It permits arbitrary local Hilbert spaces; its stated smallness and coordinate constants do not depend on their dimensions or on an upper bound on onsite energy. Consequently the same geometric constants c and r_* apply to all R>=1. These are imported existence constants, not a computed physical threshold.

Full-irrep cutoffs commute with both endpoint actions on every link. Local gauge transformations factor over outgoing cells, preserve each cell vacuum and its orthogonal complement, and commute with h_z. The interacting neutral full-carrier ground is unique and has nonzero product-vacuum overlap in the small window. Overlap normalization makes it invariant under all gauge transformations. Its unique creation-log coefficients and the resulting similarity S_R inherit that invariance, by the charged-coordinate argument.

## 3. Charged free floor survives the cutoff

In the PW decomposition an occupied link has a nontrivial retained representation. Consider a connected component of occupied links. Apply the SAME central SU3 element at every vertex of that component. Every internal link coefficient has cancelling endpoint center factors, while trivial incident links are unchanged. An isolated external fundamental or antifundamental source would contribute a nontrivial center phase, contradicting combined Gauss invariance. Therefore x and y must lie in the same occupied component.

An occupied component connecting them contains at least d distinct actual links, each of normalized electric energy at least1. Hence the charged free operator H0=(a/4)K_R obeys H0>=d on the combined fixed source sector, regardless of how many additional representations the cutoff retains. This is an all-representation center argument, not a restriction to fundamental path states or a count of occupied cells alone.

The charged sector is nonempty for every R>=1 and every finite coupling: a fundamental transporter on a simple path, acting on the product Haar vacuum, is a nonzero normalized source vector, with every used link in a fundamental or antifundamental summand retained already at R1. This witness is only a nonemptiness proof here; its total potential energy is not used to claim a volume-uniform upper bound.

## 4. Same coordinate-resolvent exclusion, centered on the cutoff vacuum

For the finite-cutoff Hamiltonian itself, the imported creation-log construction gives the similar centered operator

 S_R^-1 [(a/4)(H_R-E0_R)] S_R=H0+F_R.

In the direct sum of cell-excitation coordinates, equip vectors with the sum of their component Hilbert norms. The quantitative column estimate bounds the perturbation by c r times H0 in this norm. Tensoring by D and bounding its9 components by Cauchy–Schwarz costs sqrt9=3, so on the charged source sector

 ||F_R z||_1<=kappa ||H0 z||_1, kappa=3c r.

S_R commutes with the combined gauge projection, so this is the appropriate charged restriction of the centered operator. Every space is finite-dimensional at finite graph and R, and the coordinate norm is equivalent to its Hilbert norm; no hidden closure issue is involved. For real z<d the charged free floor yields

 ||H0(H0-z)^-1||_1<=d/(d-z) for0<=z<d,
 ||H0(H0-z)^-1||_1<=1 for z<0.

If r<r_* and kappa<1, the Neumann inverse therefore exists for every real z<(1-kappa)d. Similarity preserves the spectrum. The lower bound is

 E_xy,R-E0_R >= (4/a)(1-kappa)d,              (1)

uniform in R>=1, graph volume and source separation. In a common smaller window kappa<=1/2 this gives2d/a. The centering is explicitly E0_R, not E0 of the uncut model.

For irregular actual boundaries, include only actual plaquette interactions and decouple padded ghosts. The physical and ghost-vacuum projectors commute with H0, the interacting ground similarity and F_R. Restrict their intersection throughout the argument. The charged free floor then uses actual occupied links and actual d, so a ghost cannot shorten the path. The decoupled ghost ground energy is zero and leaves E0_R unchanged. Dropping boundary Gauss conditions would invalidate the component-center argument and is not permitted.

## 5. Compose with the separate finite-cutoff energy-form upper bound

In the common weak window, the finite-cutoff upper-energy theorem applies to this same full neutral cutoff ground and gives its local-energy charged trial estimate. Its geometry-only form uses h_R=a e_R=ceil(3R^2/4)+3R and theta=8ud/h_R. For theta<1, combining the upper-energy theorem with(1) yields

 1-kappa <= (E_xy,R-E0_R)/(4d/a) <= B(u,d,R),

 B(u,d,R)=[1+sqrt(theta)(1+sqrt(8u)+2u)
                  +2u sqrt(32u/h_R)]/(1-theta).                 (2)

At u=0 the actual charged minimum is exactly4d/a: the free floor and the fundamental path witness coincide. At positive fixed u, for any sequence of finite graphs and source distances with h_R/d tending to infinity, B tends to1. Thus the charged cost per distance stays between a strictly positive lower coefficient and a finite upper coefficient along that controlled cutoff scaling. This does not force a limit of the ratio or identify it with1; the actual charged minimum can lie below the full-unitary trial cost.

At a fixed finite R the lower bound(1) holds for every d, but theta<1 eventually fails as d increases. Neither(2) nor the upper-energy theorem supplies a fixed-R uniform all-distance upper bound. R^2/d tending to infinity is a sufficient scaling, not a necessary or optimal hardware cost.

## 6. Optional fixed-R selected infinite representation

Fix one R once and for all. Use the same fixed-interaction, whole-range finite restrictions and neutral infinite ground representation supplied by0411042. The local link algebra is now a matrix algebra, so local normality and continuity of the finite gauge actions are immediate. The ground representation and Hamiltonian carry combined gauge actions after tensoring the external source space. Finite-vertex Haar averaging of bounded local vectors yields a dense charged subspace, as in the selected-GNS construction.

The finite charged spectral supports lie above L=(4/a)(1-kappa)d for sources fixed in the bulk. Weak-resolvent convergence of the ground representations transfers this support exclusion for fixed local charged test vectors; density gives the same lower bound on the selected charged Hamiltonian. This does not infer convergence of finite charged minima.

For theta=8ud/h_R<1, the local bounded compressed path operator has norm squared at least1-theta in every finite ground. Its local expectation converges, so the infinite trial is nonzero with the same lower norm bound. The finite-cutoff upper theorem’s normalized trial spectral measures have first moments bounded by(4d/a)B(u,d,R). Weak convergence and lower semicontinuity of the nonnegative first moment therefore put the infinite trial in the energy form domain and give the same upper bound for the selected charged bottom. There is no claim of an eigenvector at that bottom, representation independence, a joint R/volume limit, or a temporal Wilson-loop potential.

The finite theorem(1)–(2) does not rely on this optional extension. Neither version derives the supplied gauge action, coupling, clock, source meaning or state preparation from the four axioms, and neither describes a qubit implementation of nonunitary postselection.

## Evidence scope and import boundary

N1: This is a positive conditional energy theorem. Exact Ritz, ghost and boundary adverse examples do not establish an exhaustive negative classification or a five-route certificate.

N2: No wall-independence count is asserted. Connected endpoints, full boundary Gauss action, weak coupling and acceptance are explicit related hypotheses.

N3: The supplied Haar Wilson carrier, temporal kinetic parameter a, coupling v and external color sources are not selected by framework axioms or registered primitives.

N4: Linked mathematical arguments, including the finite-cutoff upper-energy proof, are load-bearing; review verdicts are not theorem premises. The Yarotsky coordinate and GNS statements remain explicit mathematical imports.

N5: All 18 finite controls remain: eight cube flow/connectivity/energy predicates, three ghost predicates, two boundary-Gauss predicates, four Ritz predicates and one retained-orientation predicate. No site-resolved dynamics or lattice-wide execution is claimed. The dimension-uniform and selected-sector arguments are analytical, not established by enumerating finite flows.

N6: Original parser failure, raw fixtures and adverse outcomes remain recoverable. Resource and input guards are not mathematical check counts.

N7: Better trials and other limiting mechanisms remain open; no impossibility or new-axiom necessity is inferred.

N8: Both complete proofs remain live; historical and prospective campaign material has no current authority. Source review and finite controls do not confer an audit verdict.
