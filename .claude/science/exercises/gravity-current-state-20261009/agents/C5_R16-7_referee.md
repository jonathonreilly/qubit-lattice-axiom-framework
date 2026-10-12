# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's overall answer—**INCONCLUSIVE** for the registered strong-penalty finite-clock N-type problem—is correct, but its subclass label **NOT-PRODUCED-EVIDENCE**, its identification of an optimized sum-rule ratio with the physical metric susceptibility, and its claim that the U(1) control passed are not confirmed. The exact operator results survive in a narrower, explicitly normalized and bridge-conditional form.

## 1. Theorem B, Corollary B2, and the observable

1. **The spectral inequality is correct after a volume-normalization repair.** With
   \(C=E_{TT}(k)/\sqrt V\), the stated spectral conventions give
   \[
   |\langle[C,A]\rangle|^2\le m_1(C)\chi_{AA}.
   \]
   For \(A=[H,C]^\dagger\), one has \(\chi_{AA}=m_1(C)\) and
   \(|\langle[C,A]\rangle|=m_1(C)\), so the normalized ratio is exactly
   \(1/m_1(C)\). This confirms the Cauchy--Schwarz step and current saturation in
   `R16-7_report.md:39-47,141-149`. As written, however, the report first defines
   an unnormalized Fourier sum (`R16-7_report.md:46`) and later replaces its
   double commutator by the per-volume quantity (`R16-7_report.md:143`) without
   changing the commutator normalization in `R16-7_report.md:147`. M2 would then
   give \(1/[V m_1(k)]\), not \(1/m_1(k)\). Use \(V^{-1/2}\)-normalized Fourier
   operators throughout, or replace the displayed ratio by
   \(V\chi_{AA}/|\langle[E_{TT},A]\rangle|^2\).

2. **The \(m_1=O(k^4)\) bound is a valid conditional theorem.** I independently
   checked the load-bearing moment argument rather than accepting N0914's audit
   status. An exactly vector-invariant finite-support shift pattern annihilates
   constant and linear symmetric strains, because those strains are locally
   symmetric gradients; hence its zeroth and first spatial moments vanish.
   Taylor's remainder then gives \(|\widehat m(k)|\le |k|^2\mu_2(m)/2\).
   The stated second-moment summability therefore bounds the per-volume f-sum
   by \(C_Hk^4\). This is precisely the argument recorded in
   `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:225-250`, notwithstanding that note's explicit unaudited status at `:3-9`.
   The result requires the exact integer Gauss law and the summable shift
   expansion in `R16-7_report.md:61-67`; it does not cover merely energetic
   vector constraints or non-lifted mod-\(N\) clock shifts (`N0914:218-223`;
   `R16-7_report.md:224-230`). It also applies only when the normalized
   commutator is nonzero; if \(m_1=0\), all such commutators vanish and the
   quotient is undefined rather than a finite susceptibility.

3. **The quantity bounded is not yet the physical metric susceptibility.** The
   report defines \(\chi_{TT}\) by optimizing over *any* probe normalized by its
   equal-time commutator with \(E_{TT}\) (`METHOD_preregistered.md:10-13`;
   `R16-7_report.md:45-47`). Current saturation proves that optimized ratio is
   \(1/m_1\); it does not prove that the current is a metric operator. For a CCR
   Gaussian, a specified \(h_{TT}\) has the canonical commutator and the two
   coincide. A finite quantum link or clock has no exact Hermitian canonical
   \(h\), and a local curvature character has a commutator vertex that itself
   vanishes as \(k^2\). Dividing that vertex out reconstructs a nonlocal
   conjugate-coordinate proxy. A physical metric/readout theorem selecting an
   operator with the required normalization is therefore missing; the minimal
   axioms explicitly require such extra physical structure to be derived
   (`MINIMAL_AXIOMS_2026-06-29.md:85-90`). Consequently Theorem B excludes an
   Einstein--Hilbert power for the **normalized conjugate-probe ratio**, and for
   any separately supplied physical metric operator satisfying that bridge, but
   not for an otherwise unspecified finite-slot metric susceptibility.

4. **Corollary B2 is correct but conditional.** The spectral moments give
   \(\omega_{\min}^2\le m_1/\chi_{EE}\). Thus, if the actual TT electric
   susceptibility is bounded below, at least one \(E_{TT}\)-connected excitation
   obeys \(\omega\le Ck^2\), as stated at `R16-7_report.md:168-170`. This neither
   proves a gapless phase nor counts its branches, residues, or scalar/vector
   partners. It is an upper bound on one connected excitation, not by itself a
   graviton-spectrum theorem.

## 2. Theorem D, its corollaries, and stoquasticity

1. **The orbit-graph diamagnetic argument is sound with standard domain
   qualifications.** Exact scalar-shift symmetry permits a Bloch decomposition
   over the quotient orbit graph. Stoquastic matrix elements imply
   \(|(H_\rho)_{ab}|\le -(H_0)_{ab}\) off diagonal and
   \(\operatorname{Re}(H_\rho)_{aa}\ge(H_0)_{aa}\); applying this to
   \(|\psi|\) gives \(E_0(\rho)\ge E_0(0)\). This confirms
   `R16-7_report.md:180-185` on finite clocks and finite-volume rotor fibers,
   provided the rotor Hamiltonian is self-adjoint, bounded below, and the orbit
   sums define the advertised fibers. Redundant scalar generators restrict the
   allowed Bloch characters (the report's neutrality condition), but do not
   reverse the inequality.

2. **D1 is correct in its stated differentiable, translation-invariant response
   setting.** A twice-differentiable function minimized at \(\rho=0\) has a PSD
   Hessian, so its Fourier-diagonal kernel obeys \(W(k)\ge0\). This excludes a
   pure core-minus-unscreened-Newtonian form \(c-a/k^2\) at sufficiently small
   \(k\). It does not show that every attractive real-space component is absent,
   and it does not make a sign problem the unique escape: violating the exact
   scalar law or changing the physical source-sector bridge also escapes, as the
   report itself later concedes at `R16-7_report.md:263-266`. The screening-length
   formula at `R16-7_report.md:188` is inverted: for
   \(W=c-a/(k^2+m^2)\), positivity requires
   \(m^2\ge a/c\), hence range \(m^{-1}\le\sqrt{c/a}\), not
   \(\sqrt{a/c}\). The slogan “the sign problem and gravitational attraction are
   the same obstruction” at `R16-7_report.md:27` is therefore too broad.

3. **D2 supports only a bounded small-source kernel.** In the additional exact
   vector-law class, a real Perron ground state and the phase trial state give an
   \(O(|\rho|^2)\) upper bound because \(\widehat m=O(k^2)\) while a solution of
   \(S h_\rho=\rho\) scales as \(h_\rho=O(\rho/k^2)\). Together with D1 this
   yields \(0\le W(k)\le O(1)\), under the quasi-locality and differentiability
   assumptions (`R16-7_report.md:191-195`). It rules out a \(1/k^2\) divergence;
   it does not prove that \(W\) itself is analytic or literally a contact delta.
   The finite-clock large-blob extension is correctly labelled only “suggested”
   at `R16-7_report.md:190`.

4. **N0914's displayed Hamiltonian is stoquastic in the X/E basis.** Its
   \(Z\)-characters occur as positive multiples of \(1-\operatorname{Re}Z^m\),
   giving nonpositive off-diagonal entries, while the \(X\)-characters are real
   diagonal (`N0914:151-160`; `R16-7_report.md:125-130`). This is an L-type
   candidate, not the target N-type completion (`R16-7_report.md:132-135`), so
   it establishes an adjacent sign-free model rather than a sign-free N-type at
   strong penalty.

## 3. Registered control and fixed reading

**The control does not pass in the registered sense, so the only allowed fixed
reading is INCONCLUSIVE.** The registration requires the same method to run a
U(1) spin-ice analogue and reproduce the *emergent photon's* physical
\(\chi\sim k^{-2}\) (`TESTS.md:5276-5284`). Instead, the report's optimized
definition makes \(\inf_A\chi_{AA}/|\langle[E,A]\rangle|^2=1/m_1\) identically.
For a plaquette shift, the geometric f-sum has a \(k^2\) symbol, so this proxy
has \(k^{-2}\) whether the model contains a photon or is confined. Indeed the
actual ED control is explicitly a two-dimensional confining compact U(1) model
(`scripts/s2_qlm_ed_inequalities.py:9-10`), while s1 inserts the Maxwell Gaussian
inverse by hand (`scripts/s1_fsum_symbols.py:95-107`). No three-dimensional
spin-ice physical susceptibility, deconfined phase, thermodynamic scaling, or
error bar was computed; the report admits these limitations at
`R16-7_report.md:246-249`. Because control passage is a conjunct of both fixed
non-inconclusive readings, `TESTS.md:5284` selects **INCONCLUSIVE**, including
for the proposed \(\mathcal Q_E\) subclass. The worker's
NOT-PRODUCED-EVIDENCE assignment at `R16-7_report.md:290-293` is not allowed by
the fixed rubric.

## 4. Numerical checks

- `scripts/s1_fsum_symbols.py` reproduces `scripts/s1_fsum_symbols.out`
  byte-for-byte. Its displayed slopes correctly check the midpoint-symbol
  geometry: invariant tensor examples scale as \(k^4\), the selected
  non-invariant quadratic symbol as \(k^2\), and U(1) plaquette symbols as
  \(k^2\) (`scripts/s1_fsum_symbols.out:1-53`). These are not interacting-state
  measurements: the code sets every character expectation to one
  (`scripts/s1_fsum_symbols.py:13`), samples only constructed invariant patterns
  (`:48-57`), and the two “CCR saturation” lines multiply a formula by its own
  inverse (`:82-83`). They validate algebra and powers, not a phase or physical
  susceptibility.
- I reran `scripts/s2_qlm_ed_inequalities.py 4 0.0`; every printed scientific
  value reproduces `scripts/s2_qlm_ed_L4_V0.out:1-6`, including both f-sums,
  current saturation, the softness bounds, and the minimum twist cost
  \(1.52\times10^{-4}\). An independent \(L=3\) run also passed all four checks.
  The stored \(V=-0.5\) output is internally consistent with the same code
  (`scripts/s2_qlm_ed_L4_Vm0.5.out:1-6`). The 20 random twists are examples, not
  a proof of the diamagnetic theorem, and this 2D calculation is not the tensor
  model or a photon-phase control (`R16-7_report.md:202-204,319-321`).

## 5. Dual class, remaining window, and dressing

The dual f-sum statement is correct under its exact scalar-shift and moment
hypotheses: scalar invariance gives \(\widehat r=O(k)\), hence
\(m_1(h_{TT})=O(k^2)\); if a specified physical \(h_{TT}\) susceptibility is at
least \(c/k^2\), the moment bound forces an \(h_{TT}\)-connected excitation with
\(\omega\le Ck^2\) (`R16-7_report.md:208-220`). It does not establish that such
a dual finite-slot phase exists. The “only window” wording at
`R16-7_report.md:30,261-269` is too strong. Besides microscopic vector-law
violation, E-basis nonstoquasticity/scalar-law violation, and non-lifted small
\(N\), the proof leaves open the missing metric and matter-source bridges,
non-summable/nonlocal interactions, extra or gapless fields, singular canonical
or Berry structure, approximate rather than exact emergent constraints,
fermionic slots, and the other exclusions already listed at
`R16-7_report.md:82-88`. The dressing transfer at `R16-7_report.md:264` remains a
conditional suggestion: it needs an exact locality-preserving unitary with a
uniformly summable second moment and a proof that the physical metric/readout is
carried to the theorem's normalized probe. No such unitary or observable
transport is constructed here, so “RG-accidental, not dressed” is not proved.

## 6. Strongest correct statement

For a self-adjoint, bounded-below, translation-invariant rotor or quantum-link Hamiltonian whose actual local shifts obey an exact integer vector Gauss law and a uniformly summable second-moment bound, the consistently normalized TT-electric f-sum is \(O(k^4)\); consequently every specified probe with a nonzero normalized commutator obeys the Bogoliubov lower bound, the optimized conjugate-probe ratio has infimum \(1/m_1\), and—if \(\chi_{EE}^{TT}\) stays nonzero—at least one TT-electric-connected excitation satisfies \(\omega\le Ck^2\). Separately, an E-basis-stoquastic Hamiltonian with an exact scalar-shift symmetry has its lowest Bloch-sector energy at zero charge, so a differentiable translation-invariant source Hessian is PSD; with the vector-law moment bound it is also bounded at small \(k\). N0914's explicit L-type clock Hamiltonian is stoquastic. None of these facts identifies the optimized ratio with the physical finite-slot metric susceptibility, passes the registered three-dimensional emergent-photon control, or reaches the non-lifted, microscopically constraint-violating N-type regime at \(U\sim J\sim g\); therefore whether that registered model has Einstein--Hilbert TT stiffness remains **INCONCLUSIVE**.
