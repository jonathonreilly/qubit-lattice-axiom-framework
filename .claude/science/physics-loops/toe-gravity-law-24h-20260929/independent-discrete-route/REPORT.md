# Independent discrete-calculus route pass

Selected main source revision: `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`; the mathematical working bytes read match it. Campaign HEAD included separate pack-only commits and is not identified with this source revision. Relevant provisional proposal: PR9363 at `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`. This is discovery, not a review PASS, audit, adoption, or claim of new foundation content. Scope: mathematical constructions conditional on supplied classical canonical variables; nothing is registered or promoted. The root campaign owns all integration decisions.

```yaml
actual_current_surface_status: open
target_claim_type: open_gate
trace_class: frontier_discovery
reachability_to_target: supports
conditional_surface_status: exact cochain moment-map algebra; nonlinear gravitational completion remains open
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Result.** A generalized contraction algebra supplies exact Jacobi and exact first-class cotangent generators on a finite lattice, without pretending a lattice difference is a pointwise derivation. Its nearest-neighbour vector-field subspace does not close: an explicit phase point makes every constraint in that subspace zero while one bracket equals one. Geometry-dependent generators or connection fields can evade this toy witness; their mixed brackets are essential. A separate homogeneous-sector invariant rules out obtaining block112's kinetic lapse constraint by a translation-equivariant canonical reparametrization/recombination of the derivative-only linear constraints. Neither statement is a no-go on nonlinear lattice gravity. No new nonlinear lapse constraint is supplied here.

## 1. Exact target and conventions

The parent target is a nonlinear first-class completion of block112 preserving block62's six independent symmetric strains per cell, the declared site/face placements and standard symplectic pairing, a specified lapse placement, and the seed kinetic and linear potential coefficients. First-classness requires all brackets `{C[N],C[M]}`, `{G[xi],C[N]}` and `{G[xi],G[eta]}` to close on the same constraint ideal for every phase-space point in a stated neighbourhood and every lapse/shift, including zero modes. The required success witness is explicit constraints, structure functions and an exact proof or valid finite exhaustive certificate for a specified finite ansatz. A Ward identity for a supplied matter operator, constant-parameter closure, a flat-strain coefficient, or an enlarged internal gauge algebra alone does not count as closure.

Take independent canonical entries `{h_A(x),P_B(y)}=delta_AB delta_xy`; an off-diagonal matrix momentum is P_ij/2. At beta=-alpha the supplied kinetic density is

`T0(P) = [sum_j P_jj² - (sum_j P_jj)²/2]/(4 alpha) + sum_(i<j)P_ij²/(8 alpha)`.

Take the Hamiltonian sign `C=T-KR` and `G[xi]=sum_A P_A delta_xi h_A`. The independently checked block112 bond field must then be the negative of the source's displayed field:

`xi_j(N,M;x) = K/(4 alpha) [N_x M_(x+e_j)-N_(x+e_j)M_x]`.

This sign is fixed by the supplied action and `{h,P}=+1`; choosing it does not fix K/alpha. The calculations below do not tune either number. Four-corner mean is the representative face timing when referring to the seed. No additional adoption of dynamics is inferred from the primitive registry: scale reference is units, kinetic isotropy is the named matter kinetic-form ratio, and realized state is pointwise evaluation; none identifies this new calculus with the seed constraints.

## 2. Approach-family tuples and dispositions

| Family | Mathematical tuple (object; mechanism; terminal obligation) | Result | Strength of remaining terminal vs parent target |
|---|---|---|---|
| Generalized cochain Cartan algebra | `(degree-minus-one endomorphisms; d²=0 and commutator quotient; a bounded-range physical subalgebroid plus nonlinear normal generators matching the six-strain seed)` | Exact enlarged first-class kinematics; physical restriction open | Requiring a full Cartan/Hodge realization is stronger than the unrestricted parent target; within this route, the final completion lemma is target-equivalent |
| Endpoint link gauge calculus | `(invertible edge transports; endpoint covariance and local cotangent moment maps; normal-deformation and metric identification)` | Exact local internal gauge action, stated directly below | Full identification/completion is unknown/comparable to parent target, not a small terminal step |
| Canonical pullback of the linear theory | `(linear derivative constraint ideal; translation-fixed locus and Poisson invariance; manufacture T0 by a regular equivariant reparametrization)` | Exact failure of this restricted route including homogeneous modes | Refutes only this route; adding a starting global scalar constraint changes the premise and remains open |

There are related existing cochain results on main. The cochain mechanism is not claimed as novel. The concrete contribution of this pass is the explicit constraint-surface witness, the homogeneous canonical-pullback test, and the exact open anchor equation that a field-dependent escape must solve. This is suitable route evidence, not a new milestone source packet.

## 3. Shifted products fix one identity, not all gauge brackets

On a periodic line of side n>=4, or on Z with finite support, put `(Tf)_x=f_(x+1)` and `d=T-1`. Then

`d(fg) = (df)(Tg)+f(dg) = (Tf)(dg)+(df)g`.

With endpoint average `a f=(Tf+f)/2`, also

`d(fg) = (a f)(dg)+(df)(a g)`.

These are exact two-endpoint identities. They can be represented by the bimodule rule `dx f=(Tf)dx`; they do not say that d is an ordinary derivation of the sitewise product. Indeed for a finite set any ordinary derivation of its real function algebra vanishes: with site idempotent e, D(e)=D(e²)=2eD(e), which vanishes both at e=0 sites and at its e=1 site. This elementary observation does not exclude cochain or shifted bimodule calculus.

For the scalar action `L_xi=M_xi d`, exact multiplication gives

`[L_xi,L_eta] = M_(xi T eta-eta T xi) T d`.

For xi=delta_0, eta=delta_1, the commutator has row zero entries `-1` in column 1 and `+1` in column 2. A matrix `M_zeta d` has row zero support only in columns 0 and 1. Thus the restricted action misses one distance-two entry. Constant/proportional parameters can have zero commutator and are not counterexamples to this statement. On very small periodic lattices support aliases, so the displayed support comparison uses n>=4; the check uses n=7. A one-dimensional witness embeds along any axis of a higher-dimensional cubical lattice for this same scalar action, but is not a witness for every staggered tensor action.

A stronger check uses canonical scalar q,p and `J_x=p_x(q_(x+1)-q_x)`. At q_2=1,p_0=1 and all other coordinates zero, every J_x vanishes. Direct differentiation gives `{J_0,J_1}=p_0(q_2-q_1)=1`. Therefore the fixed finite set J_x is not even weakly first-class at that point. Arbitrary phase-space-dependent structure coefficients multiplying only these J_x cannot change 0 into 1. This fact is about the fixed toy constraints, not about adding geometry-dependent terms to them.

## 4. An exact closed cochain construction

Let V be any finite-dimensional graded cochain space, d:V^k->V^(k+1), d²=0. For any degree-minus-one endomorphism I, define

`D_I=dI+Id`.

Associativity and nilpotency imply `[d,D_I]=0`, and a direct expansion gives

`[D_I,D_J] = D_(I D_J-D_J I)`.

Thus the image of I->D_I is a Lie subalgebra of degree-preserving endomorphisms. Quotienting contractions by ker(I->D_I) transfers the commutator bracket and its Jacobi identity to that quotient. No pointwise Leibniz identity is used. The displayed contraction bracket itself need not be antisymmetric before quotienting in higher degree; its symmetric part lies in the kernel. This qualification matters.

For the 0+1 cochain complex of an n-cycle, write its incidence matrix as d=T-1. A contraction is an arbitrary n by n matrix I:C¹->C⁰, and

`D_I = diag(I d, d I)` on `C⁰ direct_sum C¹`.

Now

`[I,J]_d = I d J-J d I`

is already an honest Lie bracket on all contractions: the product `I star J=I d J` is associative. Moreover

`[D_I,D_J]=D_[I,J]_d`.

Choose canonical coordinates q,p on the full cochain vector space and define `J_I=p^T D_I q`. With `{q_a,p_b}=delta_ab`, exact symplectic differentiation gives

`{J_I,J_J}=p^T[D_I,D_J]q=J_[I,J]_d`.

Consequently the entire family `J_I=0` is first-class; its constraint surface is nonempty (e.g. p=0), though the constraints can be reducible and need not be regular everywhere. This establishes exact finite-dimensional constrained kinematics, not gravitational degrees of freedom. It holds at every q,p and for arbitrary matrices I,J, without a momentum or strain truncation.

The nearest-neighbour diagonal contractions of section 3 are not a closed subalgebra. For n=7, I=E_00,J=E_11 give `[I,J]_d=E_01`; admitting this contraction repairs that exact commutator. Iterated closure can require further supports. This algebra changes the size and type of the gauge family. It is not the original three shifts plus one lapse per cell, and its cotangent phase space is not block62's six strain coordinates. Declaring the extra generators to be gauge constraints requires checking the resulting degrees of freedom, not merely counting a Jacobi identity.

The known operator-Hodge orbit also follows algebraically. If U is a chain map, `[d,U]=0`, `H'=exp(-U^T) H exp(-U)` gives

`M(H')=exp(-U^T) M(H) exp(-U)`, where `M(H)=Hd+d^T H`.

This finite-matrix identity holds exactly. For banded U its exponential can have arbitrarily long support; the existing Aug14 note already tracks the radius-two quadratic term. I did not derive a bounded-radius nonlinear gravitational action from this identity.

## 5. The field-dependent escape has an explicit equation

The fixed-action witness must not be extrapolated to a dynamical geometry. Suppose the supplied geometry variables are h,P, matter cochains q,p, and a shift generator is

`G_xi = P_A R_xi^A(h) + p^T L_xi(h) q`.

A direct canonical bracket yields the geometry coefficient

`R_B = (d R_xi)_h[R_eta] - (d R_eta)_h[R_xi]`

and matter coefficient

`L_B = [L_xi,L_eta] + (d L_xi)_h[R_eta] - (d L_eta)_h[R_xi]`.

These signs use the convention in section 1. The second and third terms can cancel the distance-two term of section 3; simply inspecting `[L_xi(0),L_eta(0)]` omits them. The precise next sublemma is:

**Anchor sublemma.** Construct R_xi(h), L_xi(h), and a bracket B_h(xi,eta) with a specified finite support, cubic covariance and reality, such that both displayed equations hold for arbitrary fields and shifts, with `R_xi(0)` equal to block62's staggered symmetrized difference and with an explicitly justified cochain action at h=0. The equations must be checked on the actual six-component h carrier, or the carrier change must be declared.

Within a proposed cochain representation this is a necessary spatial-algebra step, weaker than the full route target. Its solution would not provide C[N], `{G,C}`, `{C,C}`, or the homogeneous scalar constraint. The full remaining lemma is the existence of those normal generators with the seed kinetic/potential coefficients and correct physical constraint reduction; that is target-equivalent within the route, and stronger than the unrestricted parent target if one insists on this particular cochain representation. It is not a routine compatibility check.

## 6. Endpoint link variables: a constructive local control

For invertible internal matrices U_(xy) on edges and vectors psi_x at vertices, define

`(D_U psi)_(xy)=U_(xy)psi_y-psi_x`.

For arbitrary invertible g_x,

`psi'_x=g_x psi_x`, `U'_(xy)=g_x U_(xy) g_y^(-1)`

implies `(D_(U')psi')_(xy)=g_x(D_U psi)_(xy)` exactly. Infinitesimally `delta_lambda U_xy=lambda_x U_xy-U_xy lambda_y`. The local vertex gauge group has an exact Lie algebra and its cotangent moment maps are first-class by the same symplectic calculation as section 4. Locality survives because the parameter acts at endpoints; no ordinary lattice Leibniz rule is needed.

This is a useful positive control on overly broad claims that all nonlinear finite-lattice symmetries fail. It does not supply spatial relabellings. For an orthogonal internal action on a frame E_x, the Gram metric E_x^T E_x is invariant, so its linear gauge action is zero, not `delta h=symgrad xi`. Pure-gauge links `U_xy=g_x g_y^-1` also have trivial plaquette holonomy; independent curved links introduce additional physical data. A derivation of normal deformations and the six-strain seed from these variables is unprovided. Neither pure-gauge nor curved links are adopted foundation content.

## 7. A homogeneous-sector test for the canonical-transformation route

Let I_lin be the ideal generated by block62's linear scalar curvature constraints `C1_x=R1_x(h)` and linear momentum constraints `G1_b`, both built only from finite differences. On a periodic torus they vanish identically on the entire translation-fixed phase-space locus H: h and P constant on each component's placement. This includes every constant symmetric P, not just P=0.

Let Phi be any regular translation-equivariant map of this same phase space (a local canonical transformation is a special case). If z is in H, then translation equivariance gives `tau Phi(z)=Phi(tau z)=Phi(z)`, so Phi(z) is in H. Therefore every pullback `Phi* F`, F in I_lin, vanishes on H. Any regular field-dependent recombination of these pullbacks still vanishes there. This proof does not use locality or canonicity, so neither can weaken the invariant.

But the desired seed with h=0 and uniform P_11=epsilon, P_22=-epsilon, other P_A=0 has

`C_x = epsilon²/(2 alpha)+O(epsilon³)`

at each site, since R1(0)=0 and the specified DeWitt kinetic coefficient is nonzero. For sufficiently small nonzero epsilon this cannot vanish identically on H. If the target is fixed only through quadratic order, the nonzero coefficient already contradicts equality of Taylor series. Thus it cannot arise from the stipulated equivariant pullback/recombination of I_lin.

This is a restricted route obstruction, not a failure of the gravitational seed. Its meaning is that the nonlinear homogeneous Hamiltonian constraint is new relative to the derivative-only linear constraint ideal. Adding it before applying a canonical map, adding embedding/clock variables with a different starting constraint surface, allowing singular maps, or excluding homogeneous modes changes the starting problem and requires a fresh analysis. The last option would also fail the parent target's stated zero-mode requirement. A canonical transformation of an already nonclosing nonlinear seed likewise preserves its Poisson-bracket defect; it cannot make that defect vanish while preserving the same ideal and domain.

## 8. Prior-art and source coverage

Complete mathematical reads: block112 (2026-09-24), block62 (2026-09-21), block63 (2026-09-21), the independent seed check, current minimal axioms and complete primitive registry plus all three registered primitive notes. The Aug14 Dirac–Kähler/Hodge note was read through its mathematical construction and gravity-interface sections 1–11 and the inspected negative-scope sections; its OS implementation and archived parent sources were not independently verified. Main block150's T1/T5 and necessary premises/proofs were read for the exact finite-range placement scope; its sea-inertia implementation was not independently checked. PR9363's viability-map A1 proposal and associated summary entries were read as prior-art claims, not its entire unrelated science collection. This pass imports no unverified OS, sea, or scalar-alias theorem.

Searches used current main's exact tree for `(shifted.product|twisted.Leibniz|discrete.Lie|cup.product|cochain|holonomy|canonical.transform)`, then `(commutator.*(radius|support|shift)|finite.*(Lie algebra|diffeomorphism)|canonical.transformation.*constraint|twisted.Leibniz)`, then `(linearization.instability|linearisation.instability|canonical.transform.*(linear|abelian)|abelian.*canonical|homogeneous.*constraint.*(ideal|canonical))`. The last search found no matching canonical homogeneous-ideal argument, but is not an exhaustive novelty proof. A too-broad pack search was interrupted and discarded; it supplies no absence claim. `gh pr list --state open --limit 100 --json number,title,headRefOid` was inspected, and PR9363's returned head matched the supplied revision. Other open titles did not identify a matching nonlinear-constraint proposal; their full science was not read.

Closest matched hits:

- Main block63: generic second-neighbour support for the **specified** walker deformation i[H,G_xi]. It already defeats any novelty claim for the mere idea of support growth. Our explicit constraint-surface witness uses different fixed scalar cotangent constraints; it does not supersede that note.
- Main Aug14 cochain-Hodge block103: Cartan identity, Hodge orbit and radius-two quadratic support already exist. The closed contraction quotient is a direct algebraic elaboration, not a new gravity closure.
- Main block150: its T5(d) excludes specified finite-range energy placements of the supplied time-reversal invariant walker against block112's nearest-bond shift structure; it leaves larger shift supports and mixed member/walker brackets open. PR9363's phrase “common to all fixed-lattice gravity” does not follow from that scope. This report does not adopt that broader summary.
- PR9363 A1: a proposed finite-range second-order closure search, whose monomial/support/placement basis is explicitly not yet fixed. Its preregistered expectation supplies no premise or falsification of this route.

## 9. Negative-claim discipline and limits

This route return is a partial attempt with named untested routes; it is not a publication-ready no-go packet. Under the current no-go skill, the five-distinct-family packet minimum is not satisfied and no N-gate PASS is claimed. The two exact restricted witnesses remain inspectable mathematical evidence; neither is generalized to a target-wide exclusion.

- **N1.** Actual tested objects are the fixed nearest-neighbour scalar cotangent action and the equivariant linear-constraint pullback. General contractions give an affirmative escape. Field-dependent anchors, endpoint links with a geometric identification, and an augmented starting homogeneous constraint are live alternatives. They are not dishonestly counted as five defeated families.
- **N2.** The two restricted obstructions concern different construction classes. No independence count or combined wall count is asserted; implication between target-wide repairs is unresolved.
- **N3.** Supplied canonical coordinates, fixed incidence, finite periodic domains, translation equivariance, regularity, fixed local action, and the seed kinetic coefficient are all explicit. “Canonical” names the chosen mathematical pairing, not a framework primitive.
- **N4.** Block63 support growth matches only the support mechanism, not the cotangent phase point. Cochain block103 matches the Cartan/Hodge mechanism, not lapse closure. Block150 does not match a gravity-only nonlinear constraint obstruction. None is used as an authoritative proof of this pass's negatives.
- **N5.** `results.txt` records exact element/site/block checks. The zero-mode coefficient is symbolic; no arbitrary nonzero-mode gravitational algebra is tested. General statements are proved above rather than inferred from samples.
- **N6.** Current primitive sources were checked. They are not counted as walls. These constructions are conditional mathematical tools; no new axiom is demanded by their incomplete physical identification.
- **N7.** Strongest counter-route: use a geometry-dependent L_xi(h) so the two mixed derivatives in section 5 cancel the distance-two commutator, and start with the required nonlinear homogeneous scalar constraint rather than attempting to create it by reparametrizing a derivative-only ideal. No equation above excludes that mechanism. The exact next calculation is to solve the anchor equation with the staggered six-strain R_xi(0) before claiming spatial closure.
- **N8.** Main already turned the fixed radius-one Hodge failure into an affirmative radius-two construction. Apply the same lesson here: support growth chooses a larger candidate carrier; it does not itself prove physical failure. No blanket finite-range, cochain, fixed-lattice, or gravity no-go is made.

## 10. Verification and next action

Run `python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-discrete-route/check.py`. Actual result: exit 0, `TOTAL: PASS=7 FAIL=0`; this means seven named exact check groups, not seven independent proofs. The script imports SymPy only, not any primary science runner. It checks shifted and midpoint product identities, d², Cartan representation and contraction Jacobi on exact integer matrices, direct canonical bracket sign, the all-constraints-zero witness, and the homogeneous kinetic coefficient. Finite matrix checks corroborate the algebraic proofs; they are not evidence of nonlinear gravitational closure.

The best next action is the field-dependent anchor sublemma in section 5. Its linear geometry dependence creates terms absent in the fixed-stencil commutator, so it is materially different from repeating the already-known finite-range support calculation. If that sublemma succeeds, freeze its exact carrier and proceed to mixed lapse/spatial brackets. The remaining full nonlinear normal-constraint lemma is target-equivalent and cannot be booked as a minor remaining task.

Current-main refresh at handoff: read-only `git ls-remote origin refs/heads/main` returned `d84eacf1cb9388f424f7037b5bbdf18f9be8fca7`. The object was already available locally. The complete `git diff --name-only 7146fe17... d84eacf1...` inventory had 33,720 paths; all but the exercise command, exercise skill and its agent configuration were under `docs/work_history/`. None of this pass's mathematical sources, primitive sources or selected physics-loop procedures changed. The selected source/procedure revision stays `7146fe17...`; no rebase, fetch/ref mutation or adoption of the new exercise workflow was performed. The full-body current mathematical search domain used here is unchanged by that transition. No finding depends on the removed archival objects.
