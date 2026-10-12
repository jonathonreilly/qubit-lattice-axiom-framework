# Backward reasoning (B1, B2, supervisor): referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-09)

Paths point to the referee's scratch copy; the same files are in `agents/` and `scripts/B1`, `scripts/B2`.

**Supervisor note on item 11:** B2's √3 is the ratio of hop distance to Euclidean distance along the body diagonal relative to the axis; the referee's 3 is the raw hop count to (1,1,1) against (1,0,0). Both describe the same ℓ¹ anisotropy.

## Verdicts

- **B1: CONFIRMED WITH CORRECTIONS.** The group-theory calculations, numerical arithmetic, power counting, and c5 simulation are reproducible. The main corrections concern the scope of “only gauge redundancy,” the rubber argument, Property N’s alleged necessity, the Planck-record heating bound, and several class-wide conclusions.
- **B2: CONFIRMED WITH CORRECTIONS.** The response-exponent arithmetic and invariant counts are sound conditionally. Lemma Q is false as written, the shot-noise-to-response bridge needs an additional fluctuation–dissipation hypothesis, and S1–S5 are a design programme rather than a proved necessity theorem.
- **Supervisor thread: CONFIRMED WITH CORRECTIONS.** Its intersection is a good naturalness-based synthesis, but “GR follows,” “fluidity is necessary,” and “records help only as events” must remain conditional statements.

I reran all supplied scripts. The short-script outputs reproduced exactly. Both c5 runs reproduced numerically; only timings changed. I also independently finite-differenced one c5 realization and recovered the analytic first and second derivatives to about \(10^{-9}\).

## Itemized findings

1. **B1 c2 — mostly correct; scope needs narrowing.**  
   [B1_report.md:74](B1_report.md:74), `B1_c2_mass_invariants.py:100–135`.

   - Taken over all \(q\) and \(\xi\), \(q_{(\mu}\xi_{\nu)}\) spans \(\mathrm{Sym}^2\): diagonals follow from \(q=\xi=e_i\), off-diagonals from \(q=e_i,\xi=e_j\). At fixed nonzero \(q\), however, the gauge directions have only dimension \(d\); the report needs the “for every \(q\)” quantifier.
   - Consequently, a momentum-independent, \(h\)-only local mass tensor satisfying the Ward identity for every \(q\) vanishes.
   - No Lorentz or point group forbids every quadratic mass: \(h_{\mu\nu}h^{\mu\nu}\), \(h^2\), or the Euclidean Frobenius form remain invariant.
   - The reported counts are correct for the representations used: SO(3) \(2/1\), proper cubic \(O\) \(3/2\), icosahedral \(I\) \(2/1\); SO(4) \(2\), \(W(B_4)\) \(3\), SO(3,1) \(2\).
   - “Only a gauge redundancy forbids it” is too strong. The demonstrated statement is: ordinary point/Lorentz symmetry alone does not forbid an \(h\)-only local nonderivative quadratic form. Exact shift symmetries, compensators/Stückelberg fields, supersymmetric or other custodial identities, topological constraints, and nonlocal mechanisms are outside the calculation. A Stückelberg massive theory can even be gauge-invariant while remaining massive.

2. **B1 c1 — arithmetic and normalization confirmed.**  
   [B1_report.md:97](B1_report.md:97), `B1_c1_tt_bound.py:4–19`.

   From \(S_{\rm kin}=\bar M_{\rm Pl}^2(\partial h)^2/8\) and \(S_{\rm mass}=-\mu h^2/2\), the convention used gives
   \[
   m_g^2=4\mu/\bar M_{\rm Pl}^2.
   \]
   For \(m_g=1.27\times10^{-23}\,\mathrm{eV}\), \(\mu=2.39\times10^8\,\mathrm{eV}^4\), or \(1.08\times10^{-104}M_{\rm Pl}^4\) using the non-reduced Planck mass.

   `SUMMARY.md:79–87` is compatible only after stating its different convention: relative to \(c\bar M_{\rm Pl}^4\) with \(c\simeq1.2\times10^{-3}\), the ratio is \(5.7\times10^{-99}\), conventionally described as “about one part in \(10^{98}\).” Relative to \(M_{\rm Pl}^4\), it is not \(10^{-98}\). The numerical physics is consistent; the prose should identify the denominator.

3. **B1 §2.3 — trichotomy useful but not exhaustive; rubber claim is false as a necessity.**  
   [B1_report.md:118](B1_report.md:118), `R3_price.md:10–21`.

   Explicit labels, spontaneously materialized labels, and no physical labels are useful EFT cases, but not a theorem-level exhaustive classification. Protected/tuned explicit structures and relational or gauge-redundant labels lie between the headings.

   A fixed-connectivity network does **not** necessarily have nonzero shear. Undercoordinated, floppy, Maxwell, or pentamode networks can have exact zero shear; `R3_price.md:17–21` gives a fixed diamond central-force example with all five traceless shear moduli zero. Generic stable cross-linked rubber does possess shear, and angle/frame couplings often lift floppy modes, but neighbor rearrangement is sufficient rather than necessary for vanishing shear.

4. **B1 §2.4–2.8 — broadly accurate summaries, but their conclusions are stronger than the cited theorems.**  
   [B1_report.md:138](B1_report.md:138).

   - **Weinberg–Witten:** The listed Lorentz invariance, covariant conserved stress tensor, particle state, and forward-matrix-element assumptions are essential. The theorem says at least one assumption fails; it does not uniquely mandate geometric gauge redundancy. Holography, emergent spacetime, nonlocality, absence of a conventional stress tensor or particle pole, and Lorentz violation are genuine exits. [Original theorem](https://www.sciencedirect.com/science/article/pii/0370269380902129).
   - **Marolf is important and should be stated more precisely:** universal gravitational coupling plus a boundary Hamiltonian is in tension with ordinary microscopic local kinematics; this is stronger and different from merely saying positions are not gauge-invariant. [Marolf](https://arxiv.org/abs/1409.2509).
   - **Weinberg soft theorem:** It establishes leading soft-graviton universality under a Lorentz-invariant S-matrix and pole-factorization assumptions. It does not alone establish the full strong equivalence principle or finite-momentum coupling. [Weinberg](https://doi.org/10.1103/PhysRev.135.B1049).
   - **Deser/Wald:** GR follows only given a single massless spin-2 field, local consistent gauge deformation, universal self-coupling, and usually a two-derivative action, modulo field redefinitions and a cosmological constant. Extra fields, higher derivatives and restricted nonlinear theories remain possible. [Deser](https://arxiv.org/abs/gr-qc/0411023), [Wald](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.33.3613).
   - **Collins et al.:** This is a generic radiative-naturalness argument for perturbative local QFT with unsuppressed Lorentz-violating UV data, not a no-go against every preferred-frame completion. Custodial symmetry, strong RG attraction, sequestering, tuned cancellations, and Hořava-type constructions are loopholes. [Collins et al.](https://arxiv.org/abs/gr-qc/0403053).
   - **Bombelli–Henson–Sorkin:** Correct for a Poisson sprinkling and a measurable Lorentz-equivariant intrinsic neighbor map. It does not prove the same statement for every Lorentz-invariant point process or a structure carrying additional marks/state. [BHS](https://arxiv.org/abs/gr-qc/0605006).
   - Hořava gravity, no-S-matrix cosmologies, higher-derivative/multifield theories and holographic boundary constructions deserve explicit placement among the loopholes.

5. **B1 §2.9/c3 — power table confirmed; Property N is sufficient, not necessary.**  
   [B1_report.md:196](B1_report.md:196), `B1_c3_noise_thresholds.py:1–14`.

   For independent, order-one, cell-scale fluctuations coarse-grained over a wavelength, the exponents are correct:

   - frozen 3D: mass type \(p=-1/2\), kinetic type \(p=3/2\);
   - white 4D: mass type \(p=0\), kinetic type \(p=2\).

   The random-phase arithmetic is also correct for its assumptions. Those assumptions are restrictive: weak/Born phase shifts, independent wavelength cells, a ray approximation, no transverse averaging, no long-range correlations, and a direct identification of microscopic coefficient noise with the wave operator. The mass-noise example quickly leaves its own weak-phase regime.

   Property N—dimension-\(\ge4\) noise, bounded gain, per realization—is a conservative sufficient criterion under a local analytic EFT with independent short-range order-one fluctuations. It is not necessary. Small amplitude, hyperuniform or anticorrelated noise, exact coboundaries/conservation laws, gaps and thresholds, annealing, nonlocal filtering, or coherent quantum states can also suppress propagation effects. Per-realization gauge invariance forbids a mass term but still permits random kinetic/curvature terms, so it does not by itself guarantee bounded noise gain.

6. **B1 c5 — numerical result confirmed; interpretation must remain bounded.**  
   [B1_report.md:204](B1_report.md:204), `B1_c5b_euclid4d_noise.py:1–36`, `B1_c5b_euclid4d_noise.out:1–6`.

   The reproduced values give \(\mathrm{sd}\sqrt N\simeq0.05\)–0.08 over \(N=255\)–4087. A weighted log fit to the printed results gives representative slopes \(-0.46\) to \(-0.52\), consistent with \(N^{-1/2}\). The mean response remains near zero. The c5 derivative formula also passed an independent finite-difference check.

   Caveats:

   - This is a total box stiffness estimator, not a direct measurement of the nonzero-\(k\), \(k\to0\) structure factor.
   - The graph has finite random degree almost surely, not a uniform valency bound.
   - Euclidean proper-distance kernels are only O(4)-symmetric at fixed metric; this is not microscopic Lorentzian covariance.
   - The result covers one compact kernel family, one free scalar, two tested masses, finite boxes and a quenched Poisson construction.
   - Turning the dimensionless \(0.06\) into physical graviton noise requires an unprovided normalization and self-energy map.

   Thus the reported **bounded FAIL** is fair; a class-wide exclusion is not.

7. **B1 §2.10 — Landau-style kinematics basically right, “records quench” only conditional.**  
   [B1_report.md:237](B1_report.md:237).

   In a translation-invariant Lorentz-invariant state satisfying the spectrum condition, a null incoming momentum cannot deposit momentum into a positive-mass vacuum excitation. If the vacuum is gapless and all species share one cone, a sum of future-directed causal momenta can equal a null vector only in the all-null, collinear case. Hence ordinary noncollinear elastic scattering from the vacuum is absent.

   In interacting gapless vacua, however, collinear splitting, massless continua, infrared dressing and the absence of isolated asymptotic poles need treatment. A Lorentz-invariant self-energy can also contain local cosmological and \(p^2\) counterterms; only the renormalized nonlocal stress response commonly begins at \(p^4\log p^2\).

   “Records quench” is fair only if a record fixes a microconfiguration for longer than the probe transit. Branch-relative decoherence does not automatically create static disorder, and an evolving recorded spacetime history need not be quenched.

8. **B1 §2.11 — mapping theorem confirmed; gravity interpretations are heuristic.**  
   [B1_report.md:248](B1_report.md:248).

   A Poisson process with intensity measure \(\rho\,\mathrm{vol}\) is invariant in law under any measurable volume-preserving bijection: its push-forward has the same intensity measure. That is an exact application of the Poisson mapping theorem. It applies to the point process; arbitrary volume-preserving maps need not preserve a metric, causal order, kernel, or dynamics. See the [Poisson mapping theorem treatment](https://www.math.kit.edu/stoch/~last/seite/lehrbuch_poissonp/media/lastpenrose2017.pdf).

   Fixed density/counting does not by itself produce unimodular gravity. In unimodular formulations, \(\Lambda\) appears as an integration constant; conjugacy to four-volume depends on the formulation. “Everpresent \(\Lambda\), \(\Delta\Lambda\sim V^{-1/2}\)” is a causal-set-inspired stochastic ansatz rather than a theorem or clean prediction. [Ahmed et al.](https://arxiv.org/abs/astro-ph/0209274).

9. **B1 c4 — arithmetic mostly correct; the quoted disturbance threshold uses the wrong matched bound.**  
   [B1_report.md:258](B1_report.md:258), `B1_c4_records_arith.py:1–22`.

   - The Planck-event density per nucleon-sized volume per second is correct: about \(1.1\times10^{103}\).
   - The quoted \(3\times10^{-135}\) per-event threshold imports an internal bound of roughly \(2\times10^{-5}\) successful births kg\(^{-1}\)s\(^{-1}\) for \(a=10^{-19}\) m, based on an Earth-heating allowance near \(7\times10^{-12}\) W/kg and an assumed \(3.8\times10^{-7}\) J per successful event.
   - It is therefore not the matched Planck-spacing heating bound. Using the same viability map at Planck spacing gives about \(3\times10^{-21}\) births kg\(^{-1}\)s\(^{-1}\), hence a per-event fraction nearer \(4\times10^{-151}\). Both bounds disappear if “locking” carries no corresponding dissipative/nonconserved energy cost.
   - The \(J^2/\Gamma\) Zeno scaling is correct for strong Markovian monitoring/dephasing of an observable that fails to commute with the Hamiltonian. It is not a generic consequence of every record.
   - The solar-mass volume-cell/area-entropy ratio \(2.4\times10^{38}\) is correct. The entropy conclusion additionally assumes each Planck cell is an independent \(O(1)\)-entropy record.

10. **B2 c1 — structural bridge and exponent arithmetic are conditional; damping convention needs clarity.**  
    [B2_report.md:93](B2_report.md:93), `B2_c1_response_exponent.py:1–47`.

    \(\Pi_{\rm TT}\sim16\pi G\,G_T\) is structurally correct up to strain/stress and TT-normalization conventions. A static real part produces a mass-like term. If \(\operatorname{Im}G_T=\eta\omega\), the wave equation contains a friction coefficient \(16\pi G\eta\), while the underdamped **amplitude** decay rate is \(8\pi G\eta\). The report and script should distinguish them.

    Given a single unit-coefficient power law over the full frequency range, the exponent arithmetic is correct: the mass constraint gives approximately \(n>2.52\)–2.63 and the damping constraint \(n>2.49\)–2.59. For \(n>0\), however, the true static mass is zero; this is a finite-frequency dispersive self-energy comparison. Coefficients, crossovers, and Kramers–Kronig relations matter.

    “A Lorentz-invariant vacuum gives \(n=4\)” is too broad. A renormalized nonlocal stress correlator in a gapless four-dimensional conformal or massless QFT behaves schematically as \(p^4\log p^2\). A gapped vacuum instead has no sub-threshold dissipation and analytic contact terms. Lorentz invariance alone does not select \(n=4\).

11. **B2 c2 — counts confirmed; hop-count conclusion overgeneralized.**  
    [B2_report.md:107](B2_report.md:107), `B2_c2_invariant_tt_forms.py:1–26`.

    For the embeddings used, the TT-form counts are correct: proper cubic \(O:2\), tetrahedral \(T:2\), axial \(D_4:4\), icosahedral \(I:1\).

    An unweighted axial nearest-neighbor cubic graph has exact \(\ell^1\) hop distance; the body-diagonal ratio is therefore \(3\), not \(\sqrt3\). This does not generalize to every crystalline model: weighted or extended links, triangulations, spectral distances, diffusion metrics, and wave propagation can converge to Euclidean/Lorentzian effective geometry.

12. **B2 Lemma Q — false as written; corrected theorem leaves a narrower use intact.**  
    [B2_report.md:140](B2_report.md:140).

    Correct statement:

    > If a connected topological group \(G\) acts continuously and a locally finite set \(X\) is invariant under \(G\), then each connected orbit \(Gx\subset X\) is a singleton. Hence \(X\subseteq\mathrm{Fix}(G)\).

    A nontrivial one-parameter translation has no fixed points, so it admits no nonempty locally finite invariant set. A boost or shear may have a fixed subspace, so locally finite sets contained in that subspace are counterexamples to the original wording. For the full translation group there are no fixed points; for full SL(\(d\)) or the full linear Lorentz group the common fixed set is only the origin, so a set with at least two points is impossible.

    B2’s use survives when the protecting group is the full spacetime group with a common fixed set too small to support the configuration. It does not exclude continuous internal/gauge symmetries acting on fields or relations while the underlying point set stays fixed.

13. **B2 dilute-hopper lemma — variance conditional; \(n=1\) does not follow from shot noise alone.**  
    `B2_report.md:247–253, 303–308`.

    \[
    \operatorname{Var}(N_x-N_y)=4r\rho VT
    \]
    is correct if \(r\) denotes the rate for each directed \(+x,-x,+y,-y\) channel and the channel counts are independent Poisson variables. If \(r\) is instead the total rate per axis, the factor is 2. The rate convention must be stated.

    The accumulated count difference has white shot noise with \(S(0)>0\). That is noise exponent zero. A dissipative response \(\operatorname{Im}G_T\propto\omega\), i.e. \(n=1\), additionally requires an equilibrium classical fluctuation–dissipation relation and Markovian low-frequency dynamics. It is not automatic at zero temperature or out of equilibrium.

14. **Necessity chains — conditional core survives; S1–S5 and G+C are not unconditional necessities.**  
    `B2_report.md:144–182`, `B1_report.md:269–305`, `backward_comparison.md:9–39`.

    Theorem-backed within their stated hypotheses are:

    - the local \(h\)-only mass Ward-identity result;
    - the invariant counts;
    - Poisson mapping invariance;
    - the corrected connected-group lemma;
    - BHS for an intrinsic finite-valency neighbor map on a Poisson sprinkling;
    - Weinberg–Witten, soft universality, and the spin-2 bootstrap with their explicit assumptions.

    Naturalness-backed but not logically mandatory are:

    - generic fixed physical labels produce a dangerous shear response;
    - microscopic time and space must be exactly equivalent;
    - gauge invariance must hold per realization rather than only statistically;
    - “gauge or coherent” exhausts all quiet-noise mechanisms;
    - records can help only as spacetime events;
    - S1–S5 and B1’s G+C are individually necessary for every UV completion.

    Exact gauge identities are the cleanest known protection, but tuning, extra symmetries, nonlocality, holography, constrained sectors, correlations, strong RG flows and absence of a local graviton variable remain logical alternatives.

15. **B1 class table — several entries need downgrading to “open” or “model-dependent.”**  
    [B1_report.md:292](B1_report.md:292).

    - **CDT:** a preferred foliation is part of the regulator/causal construction, but the continuum recovery of Lorentz invariance and diffeomorphism symmetry is a dynamical question, not simply \(C=\times\). [CDT review](https://arxiv.org/abs/1905.08669).
    - **Spin foams:** local SL(2,\(\mathbb C\)) covariance is not the same as demonstrating a recovered spacetime light cone, continuum diffeomorphism invariance or GR dynamics. [EPRL covariance](https://arxiv.org/abs/1012.1739), [large-spin propagator](https://arxiv.org/abs/0905.4082).
    - **Canonical LQG:** G/C checkmarks are too strong; they are established kinematically more than dynamically.
    - **Hořava gravity:** GW170817 severely constrains the tensor-speed parameter but does not eliminate the theory; viable parameter subspaces remain, while matter-sector naturalness and extra modes remain concerns. [Post-GW170817 constraints](https://arxiv.org/abs/1802.04303).
    - **String theory:** the massless spin-2/GR entry is broadly fair, but “not a discrete qubit substrate” is an interpretation, not a theorem.
    - **Holography:** it is specifically a Weinberg–Witten/Marolf loophole; boundary Lorentz violation need not survive in the IR.
    - **Fractons:** not all have \(\omega\sim k^2\) or \(k^3\); tensor-gauge models have varied dispersions and mode content. Even the early Gu–Wen constructions included both cubic and potentially linear examples. [Gu–Wen](https://arxiv.org/abs/0907.1203).
    - **Causal sets:** Lorentz invariance in distribution should not be marked as per-realization geometric gauge protection.
    - **Perfect crystals:** absence of stochastic noise does not eliminate coherent anisotropic dispersion.

16. **Record tension — real if “lock” means a local nonconserved matter projection.**  
    `B2_report.md:186–205`, `B1_report.md:258–265`, `backward_comparison.md:25–33`.

    The two reports conflict if every Planck-density event performs a durable physical measurement/projection of an arbitrary local matter alternative. Heating and Zeno constraints then apply, with the matched Planck-density fraction closer to \(10^{-151}\) than \(10^{-135}\) for the assumed energetic lock.

    They can be reconciled if:

    - the event locks only its occurrence, causal relation, or a gauge-invariant/conserved variable;
    - “record” means branch-relative unitary decoherence, not collapse with energy injection;
    - microgeometry remains coherent and unrecorded;
    - matter records are sparse/coarse rather than one independent matter measurement per Planck event.

    B2’s candidate axiom B should explicitly adopt one of these readings.

17. **Owner-thought verdicts — insightful, but several are overclaims.**  
    `B1_report.md:322–339`, `B2_report.md:247–275`, `supervisor_thread.md:151–169`.

    - B1 overreaches when moving from its bounded examples to “mobile records are harmful,” “records help exactly as events,” or “counting yields \(\Lambda\).”
    - B2’s “coherent and only this way” is not exhaustive; its hopper \(n=1\) conclusion requires FDT, and FR3 covers only three bounded scalar models.
    - The supervisor overstates “GR comes free,” exclusion of fluid/frozen alternatives, and the conversion of T1-style numerical evidence into a general necessity result.
    - Their strongest shared insight is nevertheless sound: physical reference labels and frozen disorder generically introduce relevant, radiatively dangerous responses unless an exact identity or a quantitatively demonstrated alternative protection suppresses them.

18. **Test readings — T1/E1′ is the decisive discriminator; several fixed PASS/FAIL readings need narrowing.**  
    `B1_report.md:343–383`, `B2_report.md:279–311`.

    The fixed readings are sound only as bounded-model verdicts. In particular, arbitrary thresholds such as relative rms \(<0.1\) or numerical mass \(<10^{-6}\) are not substitutes for physical normalization, continuum scaling, or an exact Ward identity. A failed kernel or scalar matter model excludes that implementation, not an entire substrate class.

## Strongest correct combined statement

In a local weakly coupled \(3+1\)-dimensional effective theory with a single long-range massless helicity-2 pole, a Lorentz-invariant S-matrix, ordinary factorization, universal coupling, no compensator or custodial sector, and a local analytic description in terms of \(h_{\mu\nu}\), an exact linearized diffeomorphism Ward identity forbids an \(h\)-only nonderivative mass; generic physical reference labels instead permit shear responses that require protection or extreme tuning. Under the additional soft-theorem and consistent two-derivative self-coupling hypotheses, leading universality and the GR nonlinear structure follow. Therefore a discrete substrate must either realize the relevant Ward identities—possibly relationally or per realized history—or quantitatively demonstrate another mechanism suppressing mass, Lorentz violation and low-frequency noise. These derivations do not prove that the microscopic grain must be event-like, fluid, coherent or unbounded; BHS establishes only the narrower impossibility of a Lorentz-equivariant intrinsic finite-valency neighbor map on a Poisson sprinkling.

## Ranked next tests

1. **Combined B1 Test 1 / B2 T-1: exact link-noise propagation with matter.**  
   Measure phase, amplitude, timing residuals and the retarded TT self-energy, not just a fitted spatial rms. Include tensor/gauge diagnostics and at least one frame-sensitive matter field. This most directly tests whether “per-realization gauge protection” actually makes the grain invisible.

2. **B1 Test 2: interacting hypercubic TT Ward-identity/self-energy test.**  
   Separate mass, kinetic anisotropy and higher-derivative terms. PASS should mean an exact symmetry identity or systematic zero under size/precision improvement—not merely a coefficient below \(10^{-6}\).

3. **B1 Test 3: c5 extension and estimator repair.**  
   Cheapest immediate work: compute direct windowed/nonzero-\(k\) spectra, fixed-\(N\) versus Poisson-\(N\), a second kernel, fermionic/frame-sensitive matter and one interaction. This can decisively test the current Euclidean random-lattice implementation, though not every finite-valency construction.

4. **B2 T-3: hopper response spectrum.**  
   Measure the noise spectrum and retarded response separately; invoke FDT only after demonstrating equilibrium and temperature assumptions. A result \(S(0)>0\) alone is not \(n=1\).

5. **B2 T-2: coherent-versus-frozen scalar control.**  
   Useful as a mechanism demonstration but least decisive for gravity: a translation-invariant gapped ground state is already expected to suppress sub-threshold scattering, and critical or gapless failures would not rule out other coherent substrates.