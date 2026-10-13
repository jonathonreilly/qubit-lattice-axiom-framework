# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading **ANOMALY** is met in the registered, standard-ADM setting,
but not for all of the reasons claimed by the worker.  The decisive result is
the degree-2 improved-generator identity

\[
 \{K_b,P_c\}=\delta_{bc}H+Q_{D,cb}.
\]

It is sufficient to establish failure through degree 3 because the complete
improved Killing generators have identically vanishing degree-1 pieces and a
completion beginning at degree 3 cannot alter the degree-2 coefficient.  The
one-body lattice identity and the small-velocity mass formula are correct.
Material corrections are required: Lemma \(S_\infty\) reverses a Poisson
bracket without reversing its sign; Corollaries N/N' are only narrow no-repair
statements; Theorem A3 is a formal conditional identity, not an established
degree-3 ADM result for the singular dressing; and \(\sqrt{E^2-P^2}\) is a
frame-dependent translation-charge functional, not an invariant mass once the
Poincare algebra has failed.

## Per-item findings

1. **Global charges and degree-1 terms — confirmed, conditional on the stated
   Regge--Teitelboim phase space.**  The differentiable ADM charges are the
   improved bulk constraint generators plus their surface improvements, as the
   report assumes at `R18-8_report.md:43-45`.  At linear order, integration by
   parts rewrites the *complete* scalar and vector generators as the adjoint
   linearized gates acting on the smearing.  They vanish for constant/affine
   lapses and translational/rotational Killing shifts, so the full improved
   generators have no degree-1 term; the argument at
   `R18-8_report.md:72-75` is correct in that form.  This does **not** say that
   the surface integral alone vanishes: on the constraint surface the same
   generator is represented by the nonzero ADM surface charge.  Bracketing the
   surface representative with an unreduced bulk Poisson bracket is therefore
   not interchangeable with bracketing the complete improved generator.  The
   singular completion still lacks a proved common differentiable domain and
   convergent transformed ADM boost, as the packet itself concedes at
   `R18-8_report.md:43-45,144` and the predecessor referee records at
   `C5_R17-2_referee.md:53-67`.  Thus the identification is standard and
   adequate for the fixed setting, but remains a stated phase-space premise of
   this unfinished completion rather than a theorem derived from R17-2.

2. **Theorem A and the lattice identity — confirmed at degree 2, with one
   wording correction.**  For
   \(H=\epsilon(k)\), \(P_c=\partial_c(\epsilon^2/2)\), and
   \(K_b=x_b\epsilon\), direct differentiation gives
   \(\{K_b,P_c\}=\epsilon\partial_bP_c=\delta_{bc}\epsilon+
   \Delta_{cb}\); the remaining displayed matter brackets follow likewise.
   This is exactly what the symbolic runner asserts at
   `scripts/r188_vlasov_algebra.py:15-60` and reports at
   `scripts/r188_vlasov_algebra.out:1-12`.  All four worker runners reran with
   unchanged output.  An independent implementation using the unrelated
   nearest-neighbour band
   \(\epsilon^2=m^2+2-2\cos k\), \(P=\sin k\), without importing worker code,
   obtains residuals \(2.1\times10^{-13}\)--\(7.4\times10^{-13}\) for
   \([K,P]=i\epsilon P'=i(H+Q_D)\), while \([K,P]=iH\) fails by
   \(3.2\times10^{-2}\)--\(1.94\) (`referee_r188_independent.py:18-70`;
   `referee_r188_independent.out:1-6`).  The worker's 2048-site computation is
   not a full finite-ring operator-norm identity: it is a packet test away from
   the position seam, as its own code says at
   `scripts/r188_quantum_ring.py:6-9,31-48`.  The exact identity is the
   infinite-lattice/common-domain commutator; the ring evidence approximates
   it on the tested packets.

3. **Lemma \(S_\infty\) — the regulated cancellation is right, but the claimed
   charge sign is wrong.**  The surface runner correctly finds
   \(S_b[B_c]=\Delta_{cb}\) (`scripts/r188_surface.out:1-19`).  With the
   report's convention \(K_{\partial b}=-S_b[h]\) and the completion flow
   \(\delta_\Phi h=B\), however,
   \(\{K_{\partial b},\Phi_c\}=-S_b[B_c]=-\Delta_{cb}\), whereas
   \(\{\Phi_c,K_{\partial b}\}=+\Delta_{cb}\).  The proof at
   `R18-8_report.md:87-91` establishes the latter and then states the former
   charge bracket without the required antisymmetry sign.  The independent
   bookkeeping is recorded at `referee_r188_independent.out:11-13`.  For the
   complete improved boost, the bulk linear constraint cross-term and the
   surface cross-term cancel each other because the complete degree-1
   generator is identically zero.  The surviving \(+Q_D\) in Theorem A comes
   from the degree-2 matter bracket; it is not obtained by assigning the
   opposite sign to the surface term.  Thus the anomaly survives, but the
   report's “one shell term, two opposite roles” explanation must be replaced.

4. **Lemma T — confirmed; Corollaries N and N' require their stated narrow
   scopes.**  From the displayed kernel,
   \[
   B_{ij}=\frac{\Delta_{cb}}{16\pi}\partial_i\partial_j\partial_b r
          -\frac{\Delta_{cb}}{8\pi}\delta_{ij}\partial_b(1/r),
   \]
   the first term is
   \(\partial_i\zeta_j+\partial_j\zeta_i\) for
   \(\zeta_i=\Delta_{cb}\partial_i\partial_b r/(32\pi)\), and the second is
   the Newtonian dipole with \(Ma_b=-\Delta_{cb}\).  Hence
   `R18-8_report.md:102-108` and the numerical curvature check at
   `scripts/r188_surface.out:2-22` are correct off the source.  Corollary N then
   proves only that a **linear ordinary-gauge-invariant metric surface
   functional which must retain the standard response to a genuine energy
   dipole** cannot distinguish and subtract this tail
   (`R18-8_report.md:110`).  Corollary N' correctly excludes the particular
   continuous periodic one-body moment
   \(K'_b=K_b+\int x_bg_b(k)f\): closure would force
   \(g_b=\epsilon(1/P'_b-1)\), singular at a zero of periodic \(P'_b\), and it
   also spoils \(\{K,H\}=P\) (`R18-8_report.md:112-116`).  Neither corollary
   excludes nonlinear or field-dependent boundary terms, singular/discontinuous
   matter generators, multiband cancellations, a deformed asymptotic algebra,
   or boundary terms tied to a globally admissible singular canonical map; the
   report itself acknowledges several of these omissions at
   `R18-8_report.md:204,210-211`.  The broad prose “no boundary term” / “no
   matter-moment redefinition” therefore fails the no-go stress test; the
   narrow versions above survive.

5. **Theorem A3 — algebraically correct only as a formal conditional identity;
   not established for the singular \(W\).**  On a common differentiable
   domain with no boundary cocycle, Jacobi indeed gives
   \[
   \{\{K^0,W\},P^0\}+\{K^0,\{P^0,W\}\}
      =\{\{K^0,P^0\},W\},
   \]
   and therefore the formula
   \(A^{(3)}=\{Q_D,W\}+\{Y,P^0\}-\delta\widetilde w\) at
   `R18-8_report.md:133-140`.  But \(W\sim q^{-2}\), its affine-lapse/boost
   derivative probes \(q=0\), and its transformed ADM boost and common
   distributional domain have never been constructed
   (`R18-8_report.md:141-145`; `C5_R17-2_referee.md:63-85`).  These are the
   hypotheses needed to use Jacobi as a statement about actual asymptotic
   charges, so calling A3 “proved” is too strong.  The honest result is:
   **if** the singular canonical transformation extends to a differentiable
   boundary-preserving symplectomorphism, the dressed-presentation anomaly is
   \(F(Q_D)=Q_D+\{Q_D,W\}\) through degree 3.  The world-line presentation's
   extra \(\{Y,P^0\}\) term remains unevaluated
   (`R18-8_report.md:143-145`).

6. **Observable formula — algebraically confirmed, physically renamed and
   conditioned.**  At a rest point, the degree-2 algebra gives
   \(d^2(E^2-P^2)/d\eta^2=-2(E+Q_{D,bb})Q_{D,bb}\) and
   \(V_b=P_b/E=(1+Q_{D,bb}/E)\eta+O(\eta^2)\).  Therefore, for
   \(E+Q_{D,bb}\ne0\),
   \[
   \frac{M(V)-M(0)}{M(0)}
     =-\frac{Q_{D,bb}V_b^2}{2(E+Q_{D,bb})}+O(V^4),
   \qquad M(V):=\sqrt{E^2-P^2}.
   \]
   This confirms `R18-8_report.md:149-158`; an independent two-particle ODE
   check agrees in the second derivative to \(4.8\times10^{-8}\) and in the
   mass shift to \(2.1\times10^{-18}\) absolute
   (`referee_r188_independent.out:7-11`).  Once the Poincare algebra fails,
   however, \(\sqrt{E^2-P^2}\) is not an invariant rest mass: it is a
   frame-dependent functional of the asymptotic translation charges.  Calling
   it observable is legitimate only under the fixed ADM/source/readout bridge;
   the axioms themselves leave that bridge open
   (`MINIMAL_AXIOMS_2026-06-29.md:85-90,173-190`), and the report prices it at
   `R18-8_report.md:176-179`.  The thermal numbers at
   `R18-8_report.md:167-171` are conditional estimates assuming
   \(a=\ell_P\), a thermal Boltzmann population, the stated phase-space bound,
   Earth's CMB-frame speed, and an implicit \(10^{-8}\) visibility scale.
   They support “thermally tiny below about \(10^{18}\) GeV under those
   assumptions,” not an unconditional observational exclusion; relic edge
   populations remain unbounded.

7. **Fixed reading and degree — ANOMALY is met.**  The registered setting says
   “degree 3 in the Killing sector,” but its ANOMALY criterion asks for a
   refereed failure proportional to \(Q_D\) plus an observable form
   (`TESTS.md:6757-6777`).  A nonzero degree-2 coefficient is already a failure
   through degree 3.  Because the complete improved Killing generators have no
   degree-1 term, no completion first appearing at degree 3 can cancel that
   coefficient.  The formal/unfinished status of A3 changes the degree-3
   dressing of the defect, not the existence of the leading anomaly.  The
   criterion is therefore satisfied by Theorem A plus the conditioned
   translation-charge observable of item 6; an actual degree-3 evaluation of
   the singular \(W\) is not needed to decide between the fixed readings.

8. **Prices — retain with narrower wording.**  `P-W7anom` is supported as the
   price of accepting the leading asymptotic charge-algebra defect on states
   with edge content.  `P-W7edge0` is supported only as an initial-state/domain
   condition preserved by the excluded-interaction, number-conserving model,
   not as a derived physical-state selection rule (`R18-8_report.md:176-182`;
   `MINIMAL_AXIOMS_2026-06-29.md:87-95,181-187`).

## Strongest correct statement

Assuming the standard Regge--Teitelboim asymptotically flat phase space and
the registered free number-conserving current-aligned S(1.4)/G(1.4) matter,
the complete improved Killing generators have vanishing degree-1 pieces, so
their degree-2 algebra is the direct sum of the free-graviton algebra and the
bare matter charge algebra; consequently
\(\{K_b,P_c\}=\delta_{bc}H+Q_{D,cb}\), with the stated defect moments in the
rotation brackets, while \(\{K,H\}\), \(\{K,K\}\), and \(\{P,P\}\) close at
that order.  This exact one-body identity is independently verified on a
different lattice band, and because no degree-3 completion can change a
degree-2 coefficient it is sufficient for the fixed **ANOMALY** reading.  The
tail is, off its source, an ordinary linearized gauge term plus the Newtonian
field of a mass dipole \(Ma=-\Delta\), but the report's surface-sign narrative
is reversed and its no-repair corollaries apply only to the narrow linear
metric and continuous one-body-moment classes.  The singular-dressing formula
\(F(Q_D)\) remains conditional on an unproved global symplectic/boundary
domain.  Finally, the verified small-velocity formula describes variation of
the measurable translation-charge combination \(\sqrt{E^2-P^2}\), not an
invariant mass; its thermal invisibility estimate is conditional on the
Planck-spacing and thermal-population assumptions.
