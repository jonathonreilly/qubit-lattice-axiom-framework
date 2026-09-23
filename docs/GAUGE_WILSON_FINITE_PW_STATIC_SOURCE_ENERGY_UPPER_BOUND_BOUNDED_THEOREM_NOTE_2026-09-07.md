---
claim_id: gauge_wilson_finite_pw_static_source_energy_upper_bound_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_pw_compression_shell_and_energy_path_bounds_bounded_theorem_note_2026-09-07
  - gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07
claim_scope: "Actual finite-PW charged path trial has an explicit ambient-volume-independent energy upper bound converging to4d/a for fixed distinct-link path and full physical ground premise."
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

For the actual full-irrep finite Peter–Weyl Hamiltonian, a compressed charged path applied to its full neutral physical ground has a volume-independent energy bound, not merely a state-norm estimate. The bound tends to the full-unitary trial cost4d/a as the cutoff grows for each fixed path. It requires a nonzero acceptance budget and uses the ground of the finite Hamiltonian itself.

The [compression, shell and path theorem](GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md) provides the exact shell leakage and distinct-link projection identity. Its positive compression and path identities are sufficient here; its broader negative certification remains deferred. The present energy estimate supplies the additional kinetic commutator bound. The [uniform weak-window theorem](GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies a unique physical FULL tensor-carrier ground in the stated regime; outside it that full-ground premise remains conditional. The mixed replacement trial need not be gauge invariant, so minimization only inside a constrained singlet space would not suffice.

The [exact support helper](../scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py) performs40 geometry, shell-energy, compression-identity and premise controls. Its abstract3-dimensional compression fixture is explicitly not a SU3 ground simulation. The [exact historical recovery](work_history/repo/review_feedback/pr8032-evidence/README.md) retains every original derivation, prospective contract, normalization correction, restricted-minimum control and historical review/output. Both complete positive energy derivations appear below. Historical reviews and outputs confer no current execution or audit authority.

The [actual R1 helper](../scripts/gauge_wilson_finite_pw_actual_r1_charged_energy_check_2026_09_07.py) independently computes22 exact Haar-contraction and charged-energy controls on one four-link plaquette. Its full proof is appended. The fixed fixture has a projected trial excess strictly between4 and4.01 at a=1: the full-unitary exact-four identity fails. The sharper local-energy theorem succeeds while its optional worst-case replacement-budget condition fails; no parameter was retuned. This finite fixture does not establish the general theorem by sampling.

The complete analytical proof follows. The generator convention is Tr(T_A T_B)=delta_AB; the exact earlier normalization error and its correction remain in the historical recovery. No cutoff or physical parameter was fitted. The result supplies no new lower confinement theorem, infinite-volume charged-minimum convergence or implementation of the nonunitary trial preparation.

# Volume-uniform finite-PW charged trial upper bound

This derivation supplies the form-energy estimate for the supplied finite Peter–Weyl Hamiltonian. Here a>0 is the supplied temporal-scaling kinetic parameter, not a derived spatial lattice spacing. The Wilson dynamics, cutoff, v and ground-state premise remain explicit model inputs; no hardware compiler or physical coupling is derived.

## 1. Model and the necessary full-carrier ground premise

Take a finite ordinary cubic link graph, at most four plaquettes incident to each link. The link Hilbert space is the complete Peter–Weyl sum p+q<=R, R>=1. Let P be its tensor product projection from the full Haar link Hilbert space. Put

 H_R=P(K+V)P on Ran P, K=sum_e K_e,
 K_e=-(3/(2a)) sum_A D_eA^2, V=sum_f V_f,
 V_f=v(1-ReTr U_f/3), 0<=V_f<=2v.

Haar is normalized, a>0,v>=0, and Hermitian generators satisfy Tr(T_A T_B)=delta_AB, sum_A T_A^2=(8/3)I. Full-irrep projection preserves both endpoint actions and commutes with K. Let Omega be a normalized ground vector of H_R on the FULL finite tensor carrier, of ground energy E_0. Assume Omega is neutral physical. The small-av regime of the reviewed uniform-gap theorem supplies a unique full-carrier ground, hence this physical premise. We do not replace minimization on the full carrier by minimization only in an arbitrarily constrained Gauss subspace.

Replace one link in |Omega><Omega| by its normalized Haar vacuum and retain the reduced density matrix on every other link. This is a legitimate mixed trial on the full finite carrier. All other kinetic terms and all nonincident face expectations are unchanged. Its link kinetic energy is zero. Each of at most four changed compressed positive face terms has expectation between0 and2v. Ground minimality therefore gives

 E_e:=<Omega,K_e Omega> <=8v.                 (1)

Thus E_path<=8vd for d distinct path links, and E_face<=32v for a four-link face. No ambient-volume norm appears. The replacement need not itself be gauge invariant; that is harmless precisely because Omega minimizes on the full carrier. At v=0 a restricted subspace excluding the vacuum would invalidate this inference: a positive-energy eigenstate can minimize there, showing why the premise matters.

## 2. Accepted charged trial and exact Rayleigh commutator

Let W be the ordered full fundamental transporter along a path with d distinct links, with inverse factors for reverse orientations. Regard W Omega as a matrix-valued function with Hilbert–Schmidt color norm Tr/3; this is the standard normalized external-source singlet contraction. Define C=P W P. The compression and path theorem’s exact distinct-link projection identity identifies C with the product of the compressed link transporters. Its exact endpoint covariance makes C Omega a vector in the external fundamental/antifundamental charged sector.

For e_R=[R^2-floor(R^2/4)+3R]/a, define

 theta=E_path/e_R, q=||C Omega||^2.

The shell/union bound gives 1-q<=theta. In particular theta<1 suffices for a nonzero charged trial. The charged variational energy excess satisfies

 Delta_R <= <C Omega,(H_R-E_0)C Omega>/q
          = <C Omega,[H_R,C]Omega>/q.         (2)

Every inner product here includes normalized color trace. H_R Omega=E_0 Omega holds in each color column. No derivative of a normalized, postselected output is inferred from a state-norm bound; we estimate the actual commutator in (2).

## 3. Kinetic contribution and its domain

All finite PW functions are smooth on a finite compact product group. Multiplication by the finite path word remains smooth. Therefore all kinetic and commutator expressions below are in their classical operator domains; there is no unbounded-operator limit interchange.

Since P commutes with K,

 [K,C]Omega=P[K,W]Omega.

Consequently its contribution differs from the full path identity by exactly

 <C Omega,[K,C]Omega>
 =<W Omega,[K,W]Omega>-<QW Omega,[K,W]Omega>, Q=I-P.

For each used link, sum_A D_eA^2 W=-(8/3)W. The cross term in the normalized trace of W^*(D_eA W) is zero, because it is a conjugate of plus or minus iT_A. Hence, even for complex scalar Omega,

 <W Omega,[K,W]Omega>=4d/a.                  (3)

The product rule is

 [K,W]Omega=(4d/a)W Omega
             -(3/a)sum_(e,A)(D_eA W)(D_eA Omega).

At each configuration the row operator with entries D_eA W has square

 sum_(e,A)(D_eA W)(D_eA W)^*=(8d/3)I.

Indeed each derivative is a unitary left/right product around plus or minus iT_A. The same identity holds for reverse orientation. Operator Cauchy–Schwarz, also on Hilbert–Schmidt color matrices, and the kinetic quadratic form give

 ||sum_(e,A)(D_eA W)(D_eA Omega)||
 <=sqrt((8d/3) sum_(e,A)||D_eA Omega||^2)
 =sqrt((8d/3)(2a/3)E_path).

Therefore

 ||[K,W]Omega|| <=4d/a+4sqrt(d E_path/a),

and using ||QW Omega||<=sqrt(theta),

 <C Omega,[K,C]Omega>
 <=4d/a+sqrt(theta)[4d/a+4sqrt(d E_path/a)].  (4)

Taking the real part if necessary is implicit in the upper estimate; the total Rayleigh numerator is real. The exact scalar/color-trace identity (3), not an operator identity on arbitrary color states, is the reason the full kinetic cost is exactly4d/a.

## 4. Only incident magnetic faces contribute

Write V_f^R=P V_f P. If f has no link in common with the path, its compressed operator commutes with C: it acts on disjoint link variables and is scalar in the shared color. Such faces contribute zero, exactly.

For a touching face, full scalar multiplication commutes with W. Inserting I=P+Q gives the exact compressed commutator

 [V_f^R,C]=P W Q V_f P-P V_f Q W P.          (5)

Let T_e=P_(R,e)-P_(R-1,e), and let T_f be the projection that at least one of the four face links lies in its top shell. Fundamental or antifundamental multiplication on each face link raises p+q by at most one. Thus Q V_f annihilates the subspace where all four face links are interior, and

 ||Q V_f Omega|| <=||V_f|| ||T_f Omega||
 <=2v sqrt(sum_(e in f)<T_e>)
 <=2v sqrt(E_face/e_R).                      (6)

The scalar part of V_f causes no leakage. This argument uses the actual face word, not arbitrary bounded potentials. In addition ||Q W Omega||<=sqrt(theta), ||P W||<=1 and ||C Omega||<=1. Equation(5) therefore yields

 |<C Omega,[V_f^R,C]Omega>|
 <=2v[sqrt(E_face/e_R)+sqrt(theta)].          (7)

There are at most4d distinct touching faces; double-counting them only weakens the bound. Neither (6) nor (7) uses a total-volume magnetic norm.

## 5. Explicit volume-independent result

Combining (2), (4), (7), for theta<1,

 Delta_R <= {4d/a
 +sqrt(theta)[4d/a+4sqrt(d E_path/a)]
 +sum_(f touching path)2v[sqrt(E_face/e_R)+sqrt(theta)]}/(1-theta). (8)

This is exactly a finite charged trial energy bound, not merely a vector approximation. A completely explicit sufficient version follows from (1). Put h_R=a e_R and theta_0=8avd/h_R. If theta_0<1, then

 a Delta_R <= {4d
 +sqrt(theta_0)[4d+4d sqrt(8av)]
 +8avd[sqrt(32av/h_R)+sqrt(theta_0)]}/(1-theta_0). (9)

For every fixed path and fixed a,v in the stated physical-ground regime, this tends to4d/a as R grows, uniformly over finite ambient graphs containing that path. At v=0 the bound is exactly4d/a already for every R>=1. For growing d at fixed av, h_R/d tending to infinity is sufficient for the relative correction to vanish; h_R grows quadratically in R. No specific numerical weak-coupling threshold is inferred.

The charged sector is nonempty when the trial is nonzero. The weak-regime full neutral ground premise implies a nonnegative charged excess, but no new charged lower bound is derived here. Unused-qubit sectors, a physical implementation of C, repeated-link paths, time evolution or infinite-volume convergence of charged minima remain separate questions. The input is the actual full finite ground, not the projection of an assumed untruncated ground. The result therefore repairs precisely the missing finite-carrier upper-trial bridge while retaining the model and preparation assumptions.


# Exact one-plaquette cutoff-R=1 charged-energy fixture

This prospectively fixed fixture has 22 exact finite predicates. Historical executions are retained in the recovery archive; a current source-bound execution is separate. The fixture corroborates a particular finite case of the local-energy estimate; it does not prove the general volume-uniform bound by sampling.

## Actual neutral full-carrier ground

Take four independent Haar SU3 links around one elementary plaquette, complete PW cutoff R=1, and a=1. Write U for the path link and M for the oriented product of the other three links, so the loop is UM. U and M are independent Haar matrices, but the latter still consists of three distinct kinetic links. Exact Gauss invariance at each bivalent vertex forces all four loop representation labels to agree, with a unique intertwiner at each vertex. The neutral physical space therefore has orthonormal basis1, chi=Tr(UM), bar chi. It has electric energies0,16,16.

Actual fundamental fusion or direct Haar moments gives J=(chi+bar chi)/6 with zero diagonal and every off-diagonal entry1/6 on this basis. The source term is V=v(1-J). Set t=1/100 and v=96t/(1+t-2t^2), with N=1+2t^2. Then

 Omega=[1+t(chi+bar chi)]/sqrt(N), E0=v-vt/3

is an exact eigenvector of the3-by3 neutral Hamiltonian. The remaining eigenvalues are16+11v/6-E0 and16+7v/6, both larger. Further0<E0<v<4. Any nontrivial gauge representation is orthogonal to the global Haar vacuum and has K>=4, while PVP>=0. Thus no nonneutral representation can beat this neutral vector: it is an actual full tensor-carrier ground. This establishes the ground premise directly for the fixture, without assigning a numerical threshold to the separate weak-coupling theorem.

## Literal projected charged state

Use W=U along the single path link and define A=U, B=P(U chi), C=P(U bar chi). Complete-irrep projection of two fundamental coefficients is their antisymmetric part, while fundamental times antifundamental retains its scalar part. In indices0,1,2 this gives

 B_ij=(1/2)sum_(k,l,a,b)epsilon_ika epsilon_jlb bar U_ab M_lk,
 C_ij=bar M_ji/3.

A, B, C occupy distinct electric representation patterns and are orthogonal: respectively one fundamental path link, four nontrivial links with the path conjugated, and the three-link alternative path with the direct link in vacuum. Their electric eigenvalues are4,16,12. Their squared norms in the actual source convention integral Tr(F^*F)/3 are1,1/3,1/9.

The checker constructs these polynomials and evaluates every Gram and magnetic matrix entry by independent U and M Haar integration. It uses only

 integral U_ij bar U_kl=delta_ik delta_jl/3,
 integral U_i1j1 U_i2j2 U_i3j3=epsilon_i1i2i3 epsilon_j1j2j3/6,

the conjugate rule, and exact center-charge zeros. Unsupported moments raise an error rather than guessing zero. The resulting unnormalized J matrix is

 [[0,1/18,1/54],[1/18,0,1/54],[1/54,1/54,0]].

For example the B-J-C contraction contains36 nonzero epsilon products divided by1944, giving1/54. This is an actual SU3 projection calculation, not a freely chosen three-state Hamiltonian. Since A,B,C are already retained, their compressed magnetic matrix equals their full multiplication matrix elements.

## Exact trial energy and the sufficient-bound limitation

The projected charged state is (A+tB+tC)/sqrt(N). Put Qn=1+4t^2/9. Its accepted norm q=Qn/N and its unnormalized J numerator is(4t+t^2)/27. Its normalized energy is exactly

 Etrial=[4+(20/3)t^2+v(Qn-(4t+t^2)/27)]/Qn.

The exact excess Etrial-E0 is strictly greater than4 but less than4.01. This supplies an adverse example to simply copying the full-unitary exact4 energy identity into the finite carrier. It does not imply that this trial minimizes the full charged sector.

The actual local kinetic budgets are E_path=8t^2/N and E_face=32t^2/N, with e_R=4. The norm loss is14t^2/(9N), bounded by theta=E_path/e_R. The checker verifies the local-energy estimate using rational upper enclosures sqrt(theta)<=1/50, sqrt(E_path)<=3/100, and sqrt(E_face/e_R)<=3/100, each certified by squaring positive rational numbers. There is one touching face. Thus the exact trial excess is below the certified rational bound

 [4+(1/50)(4+4(3/100))+2v(3/100+1/50)]/(1-theta).

For this fixed prospective v, the cruder geometry-independent theta_bar=8v/e_R is GREATER than1. The fully explicit sufficient estimate based only on v therefore does not apply to this particular R1 fixture, while the sharper actual-energy version does. The fixture was not retuned to hide this limitation. It validates the useful local-energy theorem and demonstrates the conservatism of its optional worst-case replacement budget.


# Appendix: full alternative local energy-form derivation

This complete alternative derivation uses the same supplied compact Hamiltonian and explicit temporal-scaling kinetic parameter a. Its historical writing and correction provenance is retained in the exact recovery.

## 1. Model, ground-state premise and local energy budget

Let G be a finite cubic link graph with a subset of its elementary plaquettes. Every link belongs to at most4 retained faces. On the full tensor product of actual complete-irrep PW link cutoffs p+q<=R, R>=1, define

 H_R=K_R+sum_f P V_f P, K=sum_e K_e,
 K_e=-3 Delta_e/(2a), V_f=v(1-ReTr(U_f)/3), a>0,v>=0.

Here P is the product cutoff. All V_f are bounded scalar multiplication operators with 0<=V_f<=2v before and after compression. No projection to boundary singlets is included in the carrier definition.

Let Omega_R be a normalized gauge-invariant eigenvector at the lowest energy E0_R of this FULL tensor-carrier Hamiltonian. In particular the existing uniform weak-window theorem supplies a unique such full ground, and its exact gauge covariance plus absence of nontrivial one-dimensional SU3 characters makes it physical. One must not replace this full-carrier premise by an arbitrary minimum solely over the gauge-singlet sector: the replacement trial below need not be gauge invariant. Outside the proven weak window, existence of the required full ground with the stipulated gauge transformation remains an explicit premise.

Write rho=|Omega_R><Omega_R|. Replace one link e by its normalized Haar vacuum while retaining the reduced density on every other link: sigma_e=|1_e><1_e| tensor Tr_e rho. This is an admissible mixed trial in the full cutoff tensor carrier. Every kinetic term other than K_e and every face not containing e has exactly unchanged expectation. The new K_e expectation is0. For an incident face the new potential expectation is at most2v while the old is nonnegative. The variational principle for mixed trials therefore gives

 E_e:=<Omega_R,K_e Omega_R><=2v n_e<=8v.       (1)

This estimate is independent of R and ambient volume; its use of an unrestricted mixed trial is essential. For a d-link path define E_path=sum_path E_e<=8vd. For a face define E_f=sum_(e in f)E_e<=32v. Boundary omissions only decrease these bounds.

## 2. Actual charged trial and its normalization

Take any oriented simple path of d distinct links from x to y. Let W be its full unitary3-by3 transporter matrix, and C=P W P its compression, acting entrywise. Since all individual link cutoffs commute with other-link matrices, C equals the product of compressed distinct-link transporters. Work with matrix-valued functions in Hilbert–Schmidt norm divided by3, so ||W Omega_R||=1. Equivalently this is the9-component static-source vector with entries W_ab Omega_R/sqrt3. Gauge invariance of Omega_R and covariance of P and W put both W Omega_R and C Omega_R in the correct fundamental/antifundamental source sector.

The exact top-shell threshold is e_R=[ceil(3R^2/4)+3R]/a. Let

 theta=E_path/e_R, q=||C Omega_R||^2.

The compression and path theorem’s actual fusion/projector estimate gives 1-q<=theta. Suppose theta<1, so q>0 and the normalized charged trial exists. The stronger actual q may be used; replacing it by1-theta is only a sufficient estimate. The upper bound here concerns the charged sector of the same finite-cutoff Hamiltonian, relative to its own neutral ground E0_R.

Because H_R Omega_R=E0_R Omega_R entrywise, its unnormalized excess-energy numerator is exactly

 N=<C Omega_R,(H_R-E0_R)C Omega_R>
   =<C Omega_R,[H_R,C]Omega_R>.                (2)

This subtracts the vacuum energy BEFORE estimating and avoids an ambient-volume E0_R normalization error. N>=0 since E0_R is the full tensor-carrier minimum. The normalized trial has excess N/q.

## 3. Kinetic commutator in an actual Sobolev norm

Let D_eA be invariant first derivatives with the generator normalization Tr(T_A T_B)=delta_AB and sum_A T_A^2=(8/3)I. Then sum_(e,A)||D_eA Omega_R||^2=(2a/3)E_path when the sum is restricted to path links. Each derivative of W on a path link is a product of unitary prefix and suffix matrices with one generator insertion. Consequently the operator row formed by these insertions satisfies

 sum_(e,A)(D_eA W)(D_eA W)^*=(8d/3)I.

The product rule for K gives a zeroth-order term (4d/a)W and a first-derivative term with coefficient3/a. The row-operator Cauchy–Schwarz estimate therefore proves

 ||[K,W]Omega_R||
 <=4d/a+(3/a)sqrt(8d/3)sqrt((2a/3)E_path)
 =4d/a+4sqrt(d E_path/a)=:B_K.                (3)

The result is a form/derivative calculation, not an inference from vector-norm convergence. PW ground states on the finite graph are finite sums of smooth matrix coefficients, so all derivatives and products used here lie in the relevant operator domains without a limiting-domain argument.

In the same matrix Hilbert–Schmidt inner product, the exact SU3 trace identity gives

 <W Omega_R,[K,W]Omega_R>=4d/a.               (4)

Indeed W is pointwise unitary, the potential is scalar, and Tr(W^* D_eA W)=0 because the inserted generator is traceless. Every cross term containing a derivative of Omega_R vanishes after color trace, with no reality assumption on Omega_R. This is the full-unitary trial identity for the supplied full-unitary static-source trial, now combined with an independent derivative-norm estimate.

Since K commutes with P, [K_R,C]Omega_R=P[K,W]Omega_R. Put Q=I-P. Equations(3)–(4) then imply

 |<C Omega_R,[K_R,C]Omega_R>-4d/a|
 =|<Q W Omega_R,Q[K,W]Omega_R>|
 <=sqrt(theta) B_K.                           (5)

The discarded vector is paired with an explicitly bounded derivative vector. This is the missing energy-form control that norm closeness alone did not provide.

## 4. Only touching face commutators contribute

A compressed face operator whose link set is disjoint from the path commutes with C EXACTLY: their link tensor supports are disjoint and the face operator is a scalar on the source color. Thus only N_touch<=4d faces occur in the potential part of(2).

For any such face, full multiplication satisfies [V_f,W]=0, so the exact compression identity is

 [P V_f P,P W P]=P W Q V_f P-P V_f Q W P.     (6)

Multiplication by a face fundamental or antifundamental character changes each face link label by a single fundamental fusion step. Therefore Q V_f P annihilates the subspace in which all four face links have p+q<=R-1. If B_f is the union projector onto their top shells, then Q V_f P=Q V_f P B_f. The commuting shell union bound and the shell kinetic lower bound give

 ||Q V_f Omega_R||<=2v ||B_f Omega_R||
 <=2v sqrt(E_f/e_R).

Using ||Q W Omega_R||<=sqrt(theta), equation(6) yields

 ||[P V_f P,C]Omega_R||
 <=2v(sqrt(E_f/e_R)+sqrt(theta)).             (7)

In(2) the left vector has norm sqrt(q)<=1, so the absolute potential contribution is no greater than the sum of these bounds. There is no sum over distant faces, no volume-sized potential norm, and no hidden factor of the9 source components: the single normalized Hilbert–Schmidt norm already includes them.

## 5. Result and uniformity statement

Let E_xy,R be the infimum of H_R in the source sector. Combining the charged trial with(2),(5),(7) gives the explicit bound

 0<=E_xy,R-E0_R
 <=[4d/a+sqrt(theta)(4d/a+4sqrt(d E_path/a))
       +sum_(f touches path)2v(sqrt(E_f/e_R)+sqrt(theta))]/(1-theta),  (8)

provided theta=E_path/e_R<1. In particular set theta_bar=8vd/e_R. When theta_bar<1, a fully geometry-independent sufficient bound is

 E_xy,R-E0_R
 <=[4d/a+sqrt(theta_bar)(4d/a+4d sqrt(8v/a))
       +8vd(sqrt(32v/e_R)+sqrt(theta_bar))]/(1-theta_bar).           (9)

For fixed a,v,d, the right side tends to4d/a as R tends to infinity, uniformly over every ambient cubic graph satisfying the full-ground premise. The error is O_(a,v,d)(R^-1); the displayed bound, rather than an unspecified asymptotic constant, is available. It is not uniform in arbitrary d at fixed R: the sufficient normalization budget itself requires e_R>8vd. At v=0, theta_bar=0, the actual vacuum trial lies exactly inside R>=1, and the bound is exactly4d/a for every cutoff.

This repairs a specific model-to-cutoff energy argument. It does not implement C as a deterministic unitary circuit, select R or a physical coupling from the axioms, identify a continuum static potential, establish convergence of infinite-volume charged minima, or remove the weak-window/full-ground premise. A separate sector-resolvent theorem would be needed to claim a new uniform finite-cutoff lower confinement bound; none is silently inferred here.

## Evidence resolution and applicability

The primary runner retains 40 mathematical predicates: 20 shell minima, 9 finite-box incidence/path checks, 6 abstract compression checks, 3 scalar acceptance checks, one 2-by-2 restricted-minimum adverse example and one generator-convention discriminator. The helper retains 22 exact one-plaquette and scalar predicates. Neither executes arbitrary-volume dynamics. Resource and input guards are not counted as mathematical checks.

N1: This is a positive conditional energy theorem with finite adverse examples, not an exhaustive negative classification. Parent negative certification remains deferred; no fifth route or negative-certification PASS is asserted.

N2: The full carrier, distinct-link path, acceptance condition and local-face hypotheses are related proof premises, not independently counted obstructions.

N3: The supplied Haar Wilson operator, kinetic parameter a, coupling v, cutoff and neutral full-ground premise are explicit. Framework axioms and registered primitives do not select these model inputs.

N4: The positive compression and path source is the actual dependency. The finite extra-energy example concerns this trial, not the charged-sector minimum.

N5: Five resolution labels in each runner describe only their listed actual predicates. Per-site dynamics and lattice-wide execution are checked and not executed; their analytic statements rely on the written proof. The exact finite cubic graph enumeration is separately identified under finite blocks.

N6: The historical generator-normalization error and initially weak restricted-ground predicate are retained exactly; the corrected conventions and stronger matrix control remain live.

N7: Better trials, repeated-link arguments, preparation, arbitrary-coupling neutral ground and charged-minimum limits are separate open questions. No impossibility is inferred for those tasks.

N8: Historical review and finite checks do not replace current independent source confirmation or confer audit authority.
