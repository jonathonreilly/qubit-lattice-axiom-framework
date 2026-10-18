# Independent referee report: F4 and X1 chirality lemmas

Date: 2026-10-17

## Scope and bottom line

I reviewed `F4_ROUTE_REPORT.md`, `F4_TEST_PREREG.md`, `X1_COMBO_REPORT.md`, and the supplied scripts and outputs. The requested verdicts are:

| Lemma | Verdict | Location |
|---|---|---|
| F4-L1 | **CONFIRMED WITH CORRECTIONS** | `F4_ROUTE_REPORT.md:50-63` |
| F4-L2 | **NOT CONFIRMED** | `F4_ROUTE_REPORT.md:65-90` |
| F4-L3 | **NOT CONFIRMED** | `F4_ROUTE_REPORT.md:92-115` |
| X1 Lemma E | **NOT CONFIRMED** | `X1_COMBO_REPORT.md:74-87` (and E6 at `:89-93`) |
| X1 Lemma Z | **CONFIRMED WITH CORRECTIONS** | `X1_COMBO_REPORT.md:125-132` |

The useful result is a **conditional pole-or-zero theorem**, not the unconditional F4-L2 printed in the report. For a fixed, spectrally adequate zero-frequency correlator satisfying the regularity assumptions needed for the interacting Nielsen--Ninomiya construction, a near Weyl pole of index \(\chi\) requires either (i) other massless poles with total index \(-\chi\), or (ii) propagator zeros/other failures of regularity carrying the compensating obstruction. If a zero seen with elementary fields disappears after composite interpolators are added and the enlarged correlator is zero-free and regular, Nielsen--Ninomiya forces a compensating massless pole in that enlarged set. The report does not prove that a particular zero survives every enlargement, that it is “non-kinematical,” or that the compensating state is localized on the far wall.

## F4-L1 — CONFIRMED WITH CORRECTIONS

**Claim audited:** “Local self-energies relocate the mirror; they never remove it,” for a momentum-independent far-wall self-energy (`F4_ROUTE_REPORT.md:50-63`).

### Hypotheses

The stated assumptions are close to those needed for the static claim, but they should additionally say:

1. the unit cell and charge-sector one-particle space are finite dimensional;
2. translation invariance gives a periodic, at least \(C^1\), matrix on \(T^3\);
3. all zero-energy singular components to which a Weyl index is assigned are isolated, or else a precise Fermi-surface charge convention is supplied;
4. after any “infinite eigenvalue” limit, the discarded eigenspace is fixed and momentum independent, and the remaining matrix is finite and smooth.

The phrase “has any frequency dependence” at `:54` is too broad. The proof uses only the finite Hermitian value at zero frequency. A genuinely singular dynamical self-energy, for example one with a \(1/i\omega\) term, can generate a Green-function zero and is not represented by an ordinary finite static Hamiltonian. Treating every such divergence as a harmless projection skips precisely the pole--zero alternative at issue in L2.

### Proof

With the corrected finite/static hypotheses, the proof is the usual Nielsen--Ninomiya/Poincare--Hopf argument. The finite Hermitian periodic field

\[
h(\mathbf k)=H(\mathbf k)+\Sigma(0)
\]

has zero total Weyl charge on the Brillouin torus in each conserved charge sector. Hence an identified near cone of charge \(\chi\) cannot be the only zero-energy charged singularity. The compensating object may be another point node or a charged Fermi surface; “relocates the mirror” is therefore an interpretation, not the theorem's exact conclusion.

Two corrections to the stated scope are material:

- `F4_ROUTE_REPORT.md:58` equates a zero eigenvalue of \(G^{-1}(0,\mathbf k)\) with a propagator pole/gapless state. This requires the spectral regularity assumed in interacting no-go theorems; it is automatic in the free/static test but not for arbitrary frequency dependence.
- `:63` says a working far-wall mechanism must have a momentum-dependent self-energy singular at the mirror node. That does not follow. A momentum-independent but frequency-singular local self-energy can supply Green-function zeros. The safe conclusion is only: a finite, regular, momentum-independent \(\Sigma(0)\) cannot leave one uncompensated pole.

### Script evidence

`F4_scripts/t_f4_1_slab_index.py:27-47,55-85` is a competent free finite-matrix check of selected perturbations. I reran it: its printed values reproduce the archived output, with peak RSS 48,720 KB. As the preregistration itself says (`F4_TEST_PREREG.md:21-23`), this is an instrument check forced by Nielsen--Ninomiya and is not evidence for interacting SMG.

One numerical sentence should be weakened. The report says the random \(\lambda=3\) far term has a Fermi surface that “carries the index” (`F4_ROUTE_REPORT.md:210`). The follow-up never obtained a gapped enclosing sphere: `F4_scripts/t_f4_1_followup2_output.txt:2-3` returns `Chern=None`. The run supports metallicity, but does not numerically measure that pocket's compensating Chern charge.

### Prior art

This is not new. Its finite-matrix content is the Nielsen--Ninomiya theorem: H. B. Nielsen and M. Ninomiya, *Absence of Neutrinos on a Lattice I/II* (1981), and the general no-go formulation [Phys. Lett. B 105, 219 (1981)](https://doi.org/10.1016/0370-2693(81)91026-1). The interacting zero-frequency-effective-Hamiltonian extension also predates this report; see Y. Shamir, [*Constraints on the Existence of Chiral Fermions in Interacting Lattice Theories*](https://arxiv.org/abs/hep-lat/9306023) (1993).

## F4-L2 — NOT CONFIRMED

**Claim audited:** successful symmetric gapping of the far wall forces a non-kinematical propagator zero of total index \(-\chi\) for every finite-support interpolator set (`F4_ROUTE_REPORT.md:65-90`).

### Hypotheses

The stated hypotheses do not support the quantifier “for every finite-support interpolator set” at `:73`.

- An arbitrary set can omit the operator that overlaps with the near Weyl pole. The report concedes this as an open step at `:83`; it is actually a load-bearing hypothesis.
- An arbitrary set can be linearly dependent or overcomplete and have kinematical zeros unrelated to physical states.
- A finite set need not interpolate all massless elementary and composite states in the charge sector.
- Unique ground state plus locality does not by itself give the differentiability properties used at `:77`. One also needs the assumptions familiar from the interacting no-go theorem: unbroken charge symmetry, no troublesome massless bosons, relativistic primary singularities, and sufficient smoothness across secondary singularities.
- Zero surfaces are left open at `:81-82`. A codimension-one zero surface is not automatically a Weyl monopole with a well-defined integer charge; “flux through an enclosing surface” needs a precise construction and regularity statement.

### Proof defects

1. The Stokes step at `:77` is valid only for a **fixed** finite matrix whose negative-eigenvalue bundle has constant rank on the punctured Brillouin zone and whose singularities admit well-defined enclosing surfaces. Those conditions are not proved.
2. Step 4 at `:79` is false as a general matrix statement. A zero of a principal correlator block need not remain a zero after adding interpolators: off-diagonal correlators can make the full matrix invertible. Algebraically, a block matrix of the form

   \[
   \begin{pmatrix}A(\mathbf k)&I\\ I&0\end{pmatrix}
   \]

   is invertible even where the restricted block \(A(\mathbf k)\) vanishes. Physical spectral constraints may restrict examples, but the report supplies no theorem that converts those constraints into the asserted monotonicity under enlargement. Golterman--Shamir explicitly emphasize that omitting fields can create spurious/kinematical zeros.
3. “Non-kinematical” is not established. Topological compensation for one fixed correlator does not show that the zero survives passage to a more complete operator set.
4. The biconditional at `:87` is invalid. Success of a slab, together with all regularity and completeness assumptions, would challenge the Golterman--Shamir no-zero/composite conjecture for that model. Falsity of their conjecture does not construct or gap the slab, so the reverse implication does not hold.
5. Even the valid alternative does not locate the compensating object on the far surface. It could occur elsewhere in momentum or real-space support, or as a non-particle singular continuum.

### Strongest correct statement of L2

Here is the strongest statement justified by the topology and the cited interacting no-go machinery.

> **Conditional pole--zero alternative.** Fix a charge sector \(q\) and a finite square matrix \({\cal R}_q(\mathbf k)\), obtained as the zero-frequency boundary value of retarded/advanced anticommutators of a fixed local interpolator set. Assume: (a) translation invariance and a finite on-site Hilbert space; (b) \({\cal R}_q\) is Hermitian, periodic, and sufficiently smooth away from isolated singular sets; (c) every massless relativistic charge-\(q\) fermion has nonzero overlap with the set and gives a primary singularity; (d) no massless boson, secondary continuum, or rank-changing surface invalidates the \(C^1\) effective Hamiltonian construction; and (e) all pole and zero charges are well defined. Then the total topological charge of the singularities of \(H_{\rm eff}={\cal R}_q^{-1}\) on \(T^3\) vanishes. Thus a near Weyl pole of index \(\chi\) implies either additional massless poles of total index \(-\chi\), or zeros/other nonregular singularities supplying the compensating obstruction. If there are no other poles and the only remaining singularities are isolated zeros, their total index is \(-\chi\).
>
> If the zero in an elementary-field matrix is removed by adding composite interpolators and the enlarged matrix is zero-free while retaining the assumptions above, Nielsen--Ninomiya forces compensating massless poles in the enlarged set. Those poles may be interpolated by composites. Conversely, absent a compensating massless state, no such zero-free regular complete set can exist.

This statement proves the requested “zero **or** gapless composite” alternative only conditionally. It does **not** prove “a protected non-kinematical zero for every interpolator set.”

### Prior art

The corrected statement is substantially prior art, not a new slab theorem:

- Y. Shamir, [*Constraints on the Existence of Chiral Fermions in Interacting Lattice Theories*](https://arxiv.org/abs/hep-lat/9306023) (1993), applies Nielsen--Ninomiya to a zero-frequency inverse retarded propagator.
- M. Golterman and Y. Shamir, [*Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories*](https://arxiv.org/abs/2505.20436) (2025, revised 2026), formulate the complete-interpolator/no-zero conditions and explicitly conjecture that elementary-field zeros may be removed by composite fields.
- Their proceedings summary, [arXiv:2603.15985](https://arxiv.org/abs/2603.15985), states the same conditional vector-like conclusion.
- V. Gurarie, [*Single particle Green's functions and interacting topological insulators*](https://arxiv.org/abs/1011.2273) (2011), develops the pole-versus-zero topological accounting at interacting boundaries.

The report's useful specialization is to the slab bookkeeping, not a new proof of the operator-set-independent assertion.

## F4-L3 — NOT CONFIRMED

**Claim audited:** an exhaustive gauge-locality dichotomy for every inflow geometry without symmetric far-wall gapping (`F4_ROUTE_REPORT.md:92-115`).

### Hypotheses

The heading is much broader than the setting. The report does not define the class of allowed regions \(W\), whether they must be fibre bundles, the permitted position dependence of the gauge kinetic operator, boundary gauge terms, emergent/topological gauge sectors, or the meaning of “slaved” beyond three examples. Without those definitions, the three cases do not form a proved exhaustive classification.

### Proof defects

- **Case (a), `:96-100`.** A constant light mode along each fibre is true for the standard connected slab with an unbroken local bulk gauge action and ordinary boundary conditions. It is not derived for every inflow geometry or every allowed gauge action. The opposite-orientation surface statement is standard for a two-ended slab, but the passage to “vector-like at gauge resolution” requires both ends to couple to the same normalized zero mode and requires a controlled low-energy reduction.
- **Case (b), `:101-104`.** The assertion that confinement/Higgsing destroys the \(C_2\) band structure and leaves independent local 3D layers is not proved. The displayed mirror-mass estimate comes from a single-barrier toy (`F4_scripts/t_f4_2_ir_price.py:16-19`), not from the hypotheses of L3. It cannot support a universal bound.
- **Case (c), `:105-112`.** The plateau, \(|k|\) kernel, and \(1/L\) penalty are properties of specified extensions. Positivity and strict noncancellability of a coefficient \(c>0\) are asserted, not derived for a general unitary qubit Hamiltonian with all permitted local counterterms and charged sectors. The supplied `t_f4_4b_spread.py` checks \(1/L\) only in one free folded model (`F4_ROUTE_REPORT.md:236-239`); it does not prove the general polarizability statement.
- The \(10^{46}\)-layer estimate at `:113-115` is arithmetic conditional on a particular gradient-flow/light-cone decoupling model and a photon-mass length scale. It is not a lower bound for all local inflow constructions.

Accordingly, L3 may be retained as a heuristic case analysis for the listed implementations, with the individual “suggested” labels preserved. It cannot be cited as a no-go theorem covering “every inflow geometry.” E6 in X1 (`X1_COMBO_REPORT.md:89-93`) therefore does not follow as a proved corollary.

### Prior art

The component constructions and objections are known:

- Grabowska--Kaplan's gradient-flow proposal is [arXiv:1511.03649](https://arxiv.org/abs/1511.03649).
- Golterman--Shamir analyze unwanted conserved currents in five-dimensional flow and disk proposals in [arXiv:2404.16372](https://arxiv.org/abs/2404.16372).
- Kaplan's finite-boundary proposal is [arXiv:2312.01494](https://arxiv.org/abs/2312.01494), with a finite-lattice spectral example in [arXiv:2312.04012](https://arxiv.org/abs/2312.04012).

I found no established prior-art theorem with the universal trichotomy and quantitative consequences claimed by L3. The absence of such a citation matters because the report itself labels major branches only “proved skeleton” or “suggested.”

## X1 Lemma E — NOT CONFIRMED

**Claim audited:** the equivalence ladder making the symmetric disentangler statement \(S^*\) target-equivalent to the desired chiral theory (`X1_COMBO_REPORT.md:63-87`).

### Hypotheses and proof

The report is commendably explicit that E3 is “open in general,” E4 is “suggested,” and E5 has open gauge-dynamics and propagator-zero steps (`:82-85`). Those admissions preclude a confirmed equivalence theorem.

More specifically:

- **E1 (`:78-80`)** is plausible for an exact finite-depth symmetric circuit, or for a uniformly controlled quasi-local automorphism together with a theorem that its spatial truncation leaves a stable gap. As written, the estimates for quasi-local tails and near-wall stability are explicitly open. Mapping a ground state to a product state also needs to be connected carefully to a local parent Hamiltonian and a rigorously gapped cut. These are not merely cosmetic details in a gapless-near-wall geometry.
- For \(G_{SM}\) alone, the admitted \(\nu^c\nu^c\) mass changes the claimed 16-Weyl near spectrum. It can be phenomenologically acceptable as a seesaw ingredient, but it is not “harmless” if the theorem's target is exactly 16 massless Weyl fields.
- **E2 (`:81`)** is definitional and is fine once \(H_{DI}\) exists.
- **E3 (`:82`)** is the missing bulk--boundary/completeness theorem. Stating the result “modulo BBC-inv” is a conditional reduction, not a proof of target equivalence.
- **E4 (`:83`)** is a conditional stacking argument. It needs the target model as a permitted boundary ancilla and an explicit representation-compatible bilinear. It does not establish the target.
- **E5 (`:84-85`)** correctly observes that treating the layer coordinate as on-site payload avoids a geometrically extended gauge field. But gauging an arbitrary quasi-local generator generally gives quasi-local Wilson-line-dressed terms, not automatically finite-range terms; gauge dynamics and the effect of Green-function zeros remain open exactly as the report says.
- **E6 (`:89-93`)** relies on the unconfirmed universal L3 and is therefore not proved.

The defensible result is a conditional construction: if \(S^*\) is strengthened to an explicitly controlled symmetric finite-depth/quasi-local phase equivalence whose half-space cut is uniformly gapped, it supplies a candidate symmetric far boundary; if an appropriate lattice bulk--boundary converse is also assumed, the target and boundary obligations can be related. This is an obligation map, not an equivalence lemma.

### Prior art

The central mechanism is known and is accurately acknowledged by the report. J. Wang and X.-G. Wen, [*A Non-Perturbative Definition of the Standard Models*](https://arxiv.org/abs/1809.11171) (2020), propose the Spin(10) lattice construction using cobordism triviality and existence of a symmetric gapped boundary. That paper itself describes the completeness/existence step as proposed/assumed in its general form. X1's cut-disentangler bookkeeping is useful, but it does not close that prior open step.

## X1 Lemma Z — CONFIRMED WITH CORRECTIONS

**Claim audited:** a path realizing \(S^*\) must encounter bulk propagator zeros because the 4+1D Green-function winding changes from 16 to 0 (`X1_COMBO_REPORT.md:125-132`).

### Hypotheses and corrected proof

The homotopy argument is sound after four corrections.

1. \(N_5\) is the full frequency--momentum Green-function winding, not merely an invariant of \(G(0,\mathbf k)\). It is defined only while the chosen Green matrix is nonsingular on compactified \((\omega,\mathbf k)\) space.
2. Fix a complete microscopic canonical-fermion (or appropriate Nambu) basis throughout the path. Operator projection or enlargement can introduce or remove kinematical zeros and changes the object being compared.
3. Replace “a product state has \(N_5=0\)” with “an atomic product **Hamiltonian** has \(N_5=0\).” A Green function depends on excitation energies and matrix elements, not only on the ground-state vector. From a sufficiently strong exact \(S^*\), one can repair this: conjugate a gapped parent Hamiltonian along the local-unitary path, then connect the endpoint, which has the same symmetric product ground state, to a positive on-site parent Hamiltonian. Uniform locality and gap control in the thermodynamic limit must be assumed or proved.
4. The conclusion is that a zero occurs at **some intermediate point** of such a gapped Hamiltonian path. The standard Lehmann/causality argument rules out Green zeros away from the real-frequency axis; with the many-body gap excluding a zero-frequency pole, the required singular event is a zero of \(G(0,\mathbf k)\). This does not show a zero in the final product Hamiltonian.

Under these conditions, \(N_5=16\) for sixteen same-sign free \(C_2=1\) copies and \(N_5=0\) for the atomic endpoint. Homotopy invariance then requires a singular Green function along the path. Since the many-body path stays gapped, the singularity is a Green-function zero rather than a physical gap-closing pole. This proves the core of Z.

The speculative GS consequence at `:129-132` is not part of the confirmed lemma. Extending their “kinematical zero” conjecture to all gapped 4+1D bulks and promoting \(N_5\) to a beyond-cobordism invariant of states are additional conjectures.

### Prior art

The pole/zero homotopy mechanism is known:

- V. Gurarie, [*Single particle Green's functions and interacting topological insulators*](https://arxiv.org/abs/1011.2273) (2011), establishes Green-function winding invariants and their change through zeros without a spectral gap closing.
- Y.-Z. You, Z. Wang, J. Oon, and C. Xu, [*Topological number and Fermion Green's function of Strongly Interacting Topological Superconductors*](https://arxiv.org/abs/1403.4938) (2014), explicitly finds \(G(i\omega)\sim\omega\) zeros where interactions gap a free topological transition.

X1 applies this known mechanism to the proposed 4+1D disentangling path; that application is reasonable, but not a new general theorem.

## Computational record

All substantive local commands were run serially through `capped.sh` with `OMP_NUM_THREADS=2`; because the checked-in wrapper is not executable, it was invoked as `zsh ./capped.sh`. No process exceeded 0.3 GB.

- Reran `F4_scripts/t_f4_1_slab_index.py`: archived values reproduced; watchdog peak RSS 48,720 KB.
- Reran `X1_scripts/sm16_arith.py`: the charge sums, singlet-pairing result, and divisibility arithmetic reproduced.
- Reran `X1_scripts/di_z8.py`: T1--T3 reproduced; watchdog peak RSS 115,568 KB. This verifies the finite 1D toy and its linear propagator zero (`X1_COMBO_REPORT.md:193-205`), not Lemma E or Z in 4+1D.
- Inspected the F4 flux scripts and archived outputs. `t_f4_4b_spread.py` supports the stated \(1/L\) scaling for that one free folded Hamiltonian only.

No `REFEREE_VERDICT.md` was created.
