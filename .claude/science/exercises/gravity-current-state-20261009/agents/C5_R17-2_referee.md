# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's fixed reading **OPEN** is correct.  Lemmas D and H survive an
independent one-mode reconstruction, but three material qualifications are
required: the singular generator selects one Coulomb/comoving GR dressing (it
is not a unique "GR's own dressing"), Lemma H reclassifies rather than removes
the strong non-locality of `H'`, and the proposed `O_F` is not a Dirac
observable through the quadratic gravitational constraints.  The B3 loophole
is real as a loophole in its ansatz, but no escape closes the registered global
degree-3 brackets.

## Per-item findings

1. **Lemma D: confirmed in the stated bulk, leading-order normalization, with
   a naming/sign qualification.**  I reconstructed the G(1.4) mode
   `k=(2.6,0.1,-0.4)`, `qhat=(0.36,-0.48,0.80)`, `c=0` by adaptive quadrature
   and the closed helicity formulas, without importing the worker's
   translation solver (`R17-2_independent_checks.py:37-63,119-158`).  It gives
   `s:Xi_E=-i eps` and `Xi_h q=eps v/2` exactly at displayed precision, while
   `delta h_T/h_T^GR`, `delta h_TT/h_TT^GR`, and
   `delta E_TT/E_TT^GR` are all `-1`: the corresponding `|ratio+1|` errors are
   `0`, `3.9e-15`, and `1.1e-14`
   (`R17-2_independent_checks.out:2-8`).  This independently confirms the
   signs and improves on the sampled `6.4e-8` floor at
   `R17-2_report.md:57-68`.  The minus sign means that the displayed flow adds
   the *inverse/undressing* field relative to the conventional sourced GR
   solution; reversing the canonical-map orientation calls the inverse map the
   dressing.  GR dressings are not unique: gauge pieces, homogeneous TT
   radiation, and boundary conditions remain free.  The exact safe statement
   is that `W` is a particular Coulomb plus uniformly-comoving linearized-GR
   dressing/undressing in these conventions, for `q != 0`, not a unique GR
   object.  Within that scope the W7 tail is indeed the lattice fake-translation
   action on this field (`R17-2_report.md:59-70`).

2. **Lemma H: the weak identity is confirmed; “overturns non-local `H'`” is
   too strong.**  Direct tensor substitution gives a largest forbidden
   projection of `({W,H0}+H_int)/max|sigma| = 3.6e-15`, with nonzero allowed
   linear-constraint projections (`R17-2_independent_checks.out:9-10`).  Thus
   the displayed T3 equations really imply
   `{W,H0}=-H_int+C^(1)[lambda(matter)]` in the same weak, leading-order bulk
   sector (`R17-2_report.md:72-81`).  Consequently the inverse canonical image
   is weakly `H0`, and the non-local terms are phase-space-dependent lapse/shift
   multipliers.  But R16-12's literal statement that `H'` is non-local remains
   true off the constraint surface (`C5_R16-12_report.md:219-227`): the new
   result identifies its non-local part with the constraint ideal, rather than
   deleting it.  Calling that part “only gauge” is conditional on a completed
   first-class constraint system, admissible singular canonical map, invariant
   domain, and boundary prescription, all still missing.  Lemma C is correctly
   read as absence of an *active* Cherenkov zero, not strict subluminality as a
   necessary condition (`C5_R16-12_referee.md:82-98`;
   `R17-2_report.md:87-90`).

3. **The B3 gap is real, but it is not a completed escape.**  B3's rigidity
   step permits only the translation-covariant constraint-proportional
   additions in its linear-bilinear symbol ansatz
   (`C5_R16-12_report.md:234-249`).  An affine-lapse moment of a singular
   constraint multiplier differentiates both the multiplier and the
   longitudinal/transverse projectors; it is not one of those additions.
   Canonical covariance therefore gives a sound *formal bulk* argument that
   `F(K0)` closes weakly with `F(H0)`, and replacing `F(H0)` by `H` changes a
   Dirac bracket only by constraints (`R17-2_report.md:92-100`).  This shows
   that B3 does not exclude the route.  It does not construct it: `K0` has
   affine smearing, while `W~q^-2` is singular precisely at the global
   `q=0`/boundary limit; the needed ADM boost term and its algebra are absent
   (`R17-2_report.md:101-104`).  Hence x-weighted constraint terms are a valid
   missing class in B3, but P-W7mult does not yet buy the registered global
   boost closure.

4. **Escape 2's Jacobi reduction is algebraically valid only conditionally;
   its premises are not established for this packet.**  If one assumes a
   full `K` with `{K,H}≈P`, commuting translations, exact lower-order closure,
   and a common distributional domain, Jacobi does imply
   `{H0,{P,K}-delta H}≈0`; the off-shell kernel calculation then leaves only
   constraint directions away from `q.v=0` and the graviton shell
   (`R17-2_report.md:116-126`; `scripts/r172_dressing.out:26-32`).  However:
   (i) only the forced helicity-0 part of `{K,H}` is built, not a full `K`;
   (ii) R12-1's referee retained merely local-germ necessity, explicitly not an
   exact degree-2 operator closure (`C5_R12-1_referee_verdict.md:3-15`);
   (iii) products and derivatives of `PV(1/(q.v))+C delta(q.v)` require a
   prescription and common domain; and (iv) the rotation-smeared completion
   needed for `{K,K}` is admittedly absent (`R17-2_report.md:127-128`).  The
   uncomputed `q.v=0` shell is not a small remainder—it is exactly the support
   on which the proposed escape is ambiguous.  Therefore the Jacobi lemma is a
   useful conditional localization of the remaining obstruction, not degree-3
   closure.

5. **`O_F` has linear dressed-gauge invariance, not the claimed completed
   constraint invariance; the GR-control criticism must be narrowed.**
   Canonical covariance proves
   `{F(C^(1)),F(R^(1))}=F({C^(1),R^(1)})=0`, so the matter-dressed curvature is
   invariant under the dressed *linear* bulk constraints.  It does not prove
   invariance under `F(C^(1)+C_g^(2))`, as asserted at
   `R17-2_report.md:144-150`.  In the matter vacuum `F` is the identity.  A TT
   perturbation `h_yy=cos x`, `h_zz=-cos x` satisfies the linear constraints,
   yet a spatial diffeomorphism locally equal to `xi^x=1` gives
   `(L_xi R^(1))_yy=-1/2` at `x=pi/2`; this is the nonzero action of the
   quadratic gravitational momentum constraint
   (`R17-2_independent_checks.py:170-175`;
   `R17-2_independent_checks.out:11-12`).  A gravitational relational dressing
   (and, at the same order, the appropriate nonlinear curvature correction) is
   still needed.  Thus `O_F` cannot satisfy the R17 fixed requirement of a
   bounded observable invariant under the *completed* constraints, and its
   claimed non-response is not a physical-locality certificate.  The worker is
   right that equal-time power-law commutators of gravitationally dressed
   operators also occur in linearized GR, so that fact alone does not diagnose
   superluminal response.  But R13-4's registered test asks what the
   gauge-invariant commutator measures (`TESTS.md:4655-4662`), while R17 asks
   for an actual instantaneous response of the same physical observable
   (`TESTS.md:5773-5780`).  The correct conclusion is that a bare
   dressed-commutator comparison is nondiscriminating, not that the operational
   response criterion is invalid.

6. **Fixed reading: OPEN is mandatory; neither terminal reading is met.**
   `LOCAL-EQUIVALENT` requires a closed degree-3 completion and invariant
   physical domain (`TESTS.md:5778-5781`).  The bulk canonical identity is not
   that completion: `{P,K}`, `{K,K}`, general smearings, the singular-map
   domain/boundary charges, and a completed Dirac observable remain open
   (`R17-2_report.md:101-104,116-142,198-204`).
   `PHYSICALLY NON-LOCAL` requires a bounded completed-constraint invariant
   responder, instantaneous response, and size in a class containing escapes
   2, 3, and 5; no such responder or class-wide proof exists
   (`R17-2_report.md:144-170,200-205`).  The suggested statement that the
   lattice-specific residue is *only* in boundary Poincare charges is therefore
   premature: boundary charges are one live location, while non-Killing
   completion, the zero-frequency shell, degree 4, auxiliaries, and the
   readout bridge are unresolved (`R17-2_report.md:172-192`).

## No-go discipline check

The packet considers at least six genuinely distinct route families—world-line
distribution, affine constraint multiplier/canonical relocation, degree-4
shell, nondynamical elliptic auxiliary, boundary-charge completion, and a
deformed HDA—but closes none globally.  P-W7mult and P-W7bdy are not proved
independent because the same singular map generates both the multiplier and
the boundary-domain problem; P-W7ro is a separate observable bridge.  The
hidden premises are exact degree-2 operator closure and a valid global domain
for the singular canonical map.  The strongest steelman is precisely the
canonical route: a suitable boundary extension and relational observable may
turn the formal bulk equivalence into LOCAL-EQUIVALENT.  R16-8's local
nondynamical auxiliary is another unclosed prior-wall retirement mechanism
(`C5_R16-8_referee.md:79-93`).  Accordingly no class-wide no-go or physical
non-locality claim passes; OPEN is the only justified negative-status wording.

## Strongest correct statement

At leading order in smearing momentum, in the bulk and for free number-conserving current-aligned S/G matter with no active Cherenkov zero, R16-12's forced translation generator is the inverse of a particular Coulomb/comoving linearized-GR dressing: it solves the linear energy and momentum constraints and its Newtonian and TT shifts have ratio `-1` to the conventional sourced field; the same T3 equations give `{W,H0}=-H_int` modulo the linear constraints, so the displayed W7 term is canonically relocatable into non-local matter-dependent gauge multipliers and is not by itself evidence of an instantaneous physical interaction.  This does not close degree 3 or prove locality: B3 omits affine/x-weighted constraint terms but their singular global boundary algebra is unbuilt, the world-line route remains undecided on `q.v=0`, R12-1 does not supply exact lower-order operator closure, and `O_F` is only linearly gauge invariant rather than a completed Dirac observable.  No bounded invariant responder or invariant physical domain exists in the packet, so neither **LOCAL-EQUIVALENT** nor **PHYSICALLY NON-LOCAL** is met and the strongest reading remains **OPEN**.
