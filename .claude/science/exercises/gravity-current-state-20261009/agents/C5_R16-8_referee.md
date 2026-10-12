# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading remains **OPEN**.  The continuum kernel, its asymptotic
coefficients, the Bianchi-fixed non-TT curvature, the defect/velocity
numerics, and the restricted box-mode decoupling are sound.  The corrections
are material: the curvature is invariant under the *ordinary linearized
spatial-diffeomorphism* ambiguity but is not a Dirac observable of the
completed constraint; Lemma A is not a general auxiliary-field no-go; Lemma
D's (alpha)/(beta) list is not proved exhaustive; and Lemmas P, S, and F have
only local-germ, kinematic-sector, and boundary-limit scope, respectively.

## Per-item findings

1. **Kernel, curvature, and physicality — mathematics confirmed; physical
   inference corrected.**  For
   `s_ij=q_i q_j-q^2 delta_ij`, `|s|^2=2q^4` in three dimensions and
   `B=s D/|s|^2` exactly solves `s.B=D`; direct substitution in the linearized
   Ricci tensor gives, up to the report's overall sign convention,
   `R_ij=-(D/4)(qhat_i qhat_j+delta_ij)`.  Thus `B~q^-1` and its nonlocal
   curvature `R~q`, giving `r^-2` and `r^-4` in three dimensions.  The worker
   runner reproduces byte-for-byte, including the axis coefficients and torus
   trends (`scripts/r168_kernel.out:3-24`).  A separate implementation gives
   residuals `8.9e-16` for `s.B=D`, `4.4e-16` for the Ricci formula, and
   `3.8e-15` for TT-independence (`r168_independent_checks.out:1-6`).  The
   Bianchi identity fixes the non-TT projection, so neither an ordinary
   `Kill(zeta)` addition nor a TT addition can cancel that projection
   (`R16-8_report.md:169-195`).  But this does **not** make it physical: the
   tail is itself part of the completed momentum-constraint gauge generator,
   and the report correctly calculates that `R^(1)(h)` changes under that tail
   (`R16-8_report.md:263-270`).  Calling `R[B]` the "gauge-invariant content"
   at `R16-8_report.md:177-180` is therefore too strong.  It is invariant under
   the undeformed linear `Kill` ambiguity, not under the putative completed
   gauge symmetry, and no bounded Dirac observable follows from Bianchi.
   The forward/global charge `Q_D=sum_k epsilon(k)A(k)n_k` is indeed carried
   only by modes with `A=Hess(epsilon^2/2)-I` nonzero, hence not by the S/G
   zero-defect boxes (`R16-8_report.md:208-222`; `scripts/r168_jets.out:39-46`).
   What is not unique is the off-diagonal density whose divergence sources the
   tail: the Killing jets fix its forward value, and the edge-edge support is
   the sector-respecting placement chosen in Lemma S.

2. **Lemmas P, S, F, and A.**

   - **P: confirmed only as a Killing-jet/local-germ statement.**  With
     `P=partial(epsilon^2/2)`, the SS global brackets close algebraically and
     the remaining forward defects are built from
     `epsilon(partial P-I)`, hence occur in JS/JJ (`R16-8_report.md:130-147`).
     On the `p_xi=0` and rotational Killing slices this forces the singular
     degree-two repair into the momentum-constraint completion.  It does not
     prove that a global completion has no singular scalar-constraint term:
     R12-1's independent verdict retained only the local-germ necessity and
     explicitly found the global JS/JJ kernels, phases, Hermiticity, cubic
     covariance, invariant domain, and gravity seed unconstructed
     (`C5_R12-1_referee_verdict.md:3-15`).  Accordingly
     `R16-8_report.md:137-148` should say "no singular scalar completion is
     forced by the checked Killing jets," not that all singular terms have
     been globally confined.

   - **S: confirmed as a chosen kinematic placement, not as a physical
     domain.**  For the R14-1 S/G profiles, `A<=0` and the flat Gevrey endpoints
     make the factorized edge-edge kernel in `R16-8_report.md:210-216` smooth
     and cubic-covariant.  It annihilates the zero-defect box-mode Fock
     subspace and commutes with the algebra generated solely by those modes.
     However, R12-1 did not construct an invariant physical sector
     (`C5_R12-1_referee_verdict.md:11-15`), and the degree-three evolution that
     would preserve this restriction is precisely unbuilt.  "Inert on the
     chosen box-mode algebra" is proved; "inert on R12-1's physical domain" is
     not.

   - **F: confirmed with localization and limiting qualifications.**  The
     summation-by-parts identity moves the affine-charge contribution to the
     cutoff shell because the second derivative of the regulated affine lapse
     vanishes in its interior (`R16-8_report.md:199-205`).  Exact equality to
     `-Q_D` requires the defect source to lie where the regulator is affine;
     for noncompact wave packets it is an `R -> infinity` statement with
     decay assumptions, not "for every R."  This is an ADM-like boundary
     representation of a global generator, not a bounded observable or a
     demonstration of physical action at infinity.

   - **A: not confirmed as stated.**  The calculation shows that if `phi_dot`
     must be a quasi-local phase-space function in the particular canonical
     class, then generic moving current requires an inverse bi-Laplacian
     (`R16-8_report.md:224-239`).  A nondynamical elliptic auxiliary can instead
     be introduced by a local action/Hamiltonian with primary `pi_phi=0` and
     the secondary Gauss constraint; Dirac consistency fixes its multiplier
     nonlocally on each time slice without adding propagating modes.  The same
     possibility exists when `phi` is eliminated as a genuinely auxiliary
     field, in which case there is no independently prescribed local
     `phi_dot` to preserve.  This does not establish LOCAL-EQUIVALENT—the
     reduced evolution may remain instantaneous—but it defeats the broad
     claim that no local nondynamical-auxiliary formulation exists for moving
     defects.  Even within the displayed equation, "whenever the defect
     moves" must be narrowed to generic currents with
     `q_a q_b J_ab` not divisible by `q^4`.

3. **Lemma D and the (alpha)/(beta) fork — candidate obstruction confirmed,
   dichotomy not confirmed.**  Given the proposed tail and the defect
   continuity equation, its bracket with the free matter Hamiltonian does
   produce the displayed nonanalytic `E.(B*dot O_D)` transport term
   (`R16-8_report.md:246-250`).  A nonlocal scalar/Hamiltonian completion and a
   compensating singular momentum-constraint completion are two real routes.
   The report itself labels the bookkeeping suggested and leaves the JJ and
   remaining degree-three brackets open (`R16-8_report.md:254-259`).  It also
   has not exhausted higher momentum-constraint terms, field-dependent
   structure functions/constraint-proportional cancellations, canonical
   relocations, or local auxiliary/second-class formulations.  The no-go
   stress test therefore fails the broad "only alpha or beta" assertion; the
   correct result is an explicit uncancelled term plus two candidate repairs,
   with the full degree-three algebra still required.

4. **Fixed readings — neither terminal reading is met; OPEN is confirmed.**
   PHYSICALLY NON-LOCAL requires a bounded gauge-invariant observable with an
   instantaneous response, and none is constructed (`TESTS.md:5354-5357`;
   `R16-8_report.md:261-275`).  The proposed curvature fails gauge invariance
   under the completed tail, while the proposed momentum-constraint
   observable depends on the unbuilt `P^(1,h)`.  LOCAL-EQUIVALENT also fails:
   the box-mode annihilation is not a constructed closed completion with an
   invariant physical domain.  Option alpha would be physically nonlocal only
   after such an observable and its completed gauge dressing are constructed;
   option beta is likewise not yet a local-equivalence construction.

5. **Relation to P-pf1 — confirmed with scope and terminology corrections.**
   Both mechanisms expose the same integrated derivative obstruction,
   `integral(P'-1)=-2pi`, but they are different objects: P-pf1 puts a `1/n`
   tail in the one-body momentum symbol, whereas W7 puts a `1/r^2` kernel in a
   gravity constraint generator (`R16-8_report.md:277-296`;
   `C5_R16-5_report.md:175-183`).  The sawtooth removes the degree-two Killing
   defect only on sectors/vertices that do not cross the Brillouin face; the
   face delta and no-umklapp restriction remain.  One numerical wording is
   wrong: the SLAC **momentum symbol** jumps by `2pi`, but
   `epsilon=sqrt(m^2+sum k_i^2)` has equal limits on both sides and is
   continuous (though not differentiable) at the identified face
   (`R16-8_report.md:76-81`; `r168_independent_checks.out:12-14`).

6. **The v_max table — confirmed numerically.**  Independent global
   differential-evolution searches give `4.1209098267`, `0.9926955738`,
   `0.9938642348`, and `0.9984836383` for L-box, S(1.4), G(1.4), and SLAC,
   respectively (`r168_independent_checks.out:7-11`), agreeing with
   `R16-8_report.md:74-81` and `scripts/r168_jets.out:3-8`.  These checks also
   preserve the important distinction that S/G are whole-zone subluminal and
   the L-box law is not.

## Strongest correct statement

Within free number-conserving separable S/G matter and R12-1's still-local-germ
completion ansatz, the current-aligned choice `P=partial(epsilon^2/2)` removes
the SS Killing defects and leaves an off-box JS/JJ defect density
`Delta=epsilon(Hess(epsilon^2/2)-I)`; its minimal scalar-curvature solution
`B=s D/|s|^2`, with `D=div Delta`, has a `1/r^2` kernel in three dimensions and
a Bianchi-fixed non-TT linear spatial Ricci tail `1/r^4` that ordinary
linearized `Kill` freedom or TT additions cannot cancel.  A smooth chosen
placement makes this operator vanish on the zero-defect box-mode algebra, and
for localized sources its affine charge can be represented by a cutoff shell
at infinity.  None of this yet makes the tail physical: that Ricci tensor
itself varies under the completed momentum constraint, no global
degree-three-closed constraints or invariant physical domain have been built,
and no bounded gauge-invariant observable has been shown to respond
instantaneously.  Lemma A and the asserted exhaustive alpha/beta fork do not
close.  Thus W7 remains **OPEN**, meeting neither fixed terminal reading;
P-pf1 shares the zone-mean obstruction and removes it away from the Brillouin
seam only by moving the nonlocality into a discontinuous `1/n` matter
generator with a face delta and no-umklapp restriction.
