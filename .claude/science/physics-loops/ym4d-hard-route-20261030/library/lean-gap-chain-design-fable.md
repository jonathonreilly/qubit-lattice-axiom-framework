lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-24T11:05Z

# Lean design of the conditional gap chain on the YM4 Lean library (row 1457)

Worker: Claude Fable 5.2, high, Mac mini worker 1. Started 2026-11-23T23:05Z (`date -u`). Pin: aefd4ca20.
Status of this file: a design note. No Lean text here was built. Each claim carries one mark:
**proved** (argument on file and checked, row cited), **sketched** (argument on file, unchecked, or my own outline),
**guessed** (my estimate), **read** (I opened the declaration in the release and quote it).

Credit. The Lean library is Ethan Sussman and Levent Alpoge's `YM4 Lean` release at 3932084a9b82 (with Claude and
Codex as authors of their text). The chain to formalize is the lane's (rows cited at each step). Mathlib is cited
by declaration name.

## 0. Plan (written first, per the save protocol)

1. Read the row's named inputs: `library/sa-ym4-lean-trajectory-check-astra62.md` (statement of (M-neutral-all)),
   checks 1450 and 1453, `library/gap-os-equiv.md` Statement (5), and the files of Lemma DT, Proposition BP,
   P-ev, P'-ev, Corollary M2 (row 1356), Lemma FE.
2. Inventory the release: file list, the final theorem, the definitions of the trajectory, the continuum
   hierarchy, the OS data, any transfer operator. Declaration names with file and line.
3. Inventory Mathlib (at the release's pin, read from the release's `.lake` if present; else by name, marked guessed).
4. Write the Lean statement of (M-neutral-all) and of the conditional theorem.
5. Dependency list of lemmas with size estimates; the hardest step.
6. What to state and check first.
7. The next two rows and their decisive outcomes.

Status log (times from `date -u`):

- 2026-11-23T23:05Z file created with the plan.
- between 23:05Z and 23:15Z (the time of this step was not read; an earlier typed time was wrong and is removed) inputs read: row 1457 brief; rows 1449 (`prior/sa-ym4-lean-inputs-opus.md`, whole), 1450
  (`sa-ym4-lean-faithful-astra62.md` L14-93), 1453 (`sa-ym4-lean-trajectory-check-astra62.md`, whole);
  `gap-mini-branch-fable.md` L167-336 (A-cl, L3-ev, P-ev, P'-ev, BP); `gap-mini-mneutral-fable.md` L76-125 (M1, M2).
  Section 1 written.
- 2026-11-23T23:15Z (`date -u`) Section 2 (inventory of the release, 2.1-2.6) written from the source files.

## 1. The chain to formalize, as it stands on file (no new claim)

Notation. b = the release's odd blocking factor (their `L`); a_K = b^(-K); l = the physical side of the seed
cube (in 4N); n_K = l b^K; beta_K = g_K^(-2) the least-root Wilson coupling of the release at cutoff K and
response parameter g_0; nu_j = the release's infinite-volume lattice state at the extracted cutoff K_j; S = the
release's continuum limit (a mixture). A = centre-blind local functions (`gap-mini-branch-fable.md` 5.0).

The hypothesis (check 1453, L101-105; proved there to be the right target given BND, BND-1, BND-2):

(M-neutral-all). For the constructed b, M, delta and a fixed 0 < g_0 < delta there are l in 4N and K_0 such that
for every K >= K_0 there are an integer 1 <= w_K <= n_K/1024, a unit vector phi_K and c_K > 0 with
norm_HS(c_K^(-1) P_0 T_K^(w_K) - |phi_K><phi_K|) <= 2/5, where T_K is the Wilson transfer operator of the
n_K^3 spatial slice at beta_K and P_0 the electric-neutral projection.

The chain from it to the gap, in the order of use. Each node is a hand statement on file; "std" marks whether
the node is lattice-only (L), soft functional analysis (F), or reads the release (R).

| Node | Statement (short) | Where | Checked by | Kind |
|---|---|---|---|---|
| N1 | Lemma M1, Corollary M2: the 2/5 test at time w holds iff s(2w) <= 4/21 | `gap-mini-mneutral-fable.md` 2.1-2.2 (row 1356) | row 1359 | F (finite spectral) |
| N2 | (N-phys) with u = max(3, 2w) <= n/512, s_+(u) <= 1/2 | M2 (ii) | row 1359 | L |
| N3 | Explicit finite-aspect theorem: (N-phys) gives S_kappa(n/2; n^3) < 2^(-18) in either flux alternative | `gap-solve9-astra62.md` L146-148, L213-227 (row 1161) | check 1162 | L, 64 twists |
| N4 | (TM-tw): twisted transfer operators, sector sums | `gap-transfer-twisted.md` Theorem TW-T (row 1004) | check 1008 | L |
| N5 | (S): Lemmas K, X, E, E', Theorem S; Lemma W, Theorem S-w, Corollary EV: a seed S_w(N; (2N)^3) <= s < 1/5041 gives m_ev(L^3) >= log(1/(5041 s))/N for every L >= 2N | `gap-crux-restate.md` 3.x (row 697), `gap-flux-exercise.md` 8.4 (row 731) | rows 698, 699, 732 | L, doubling induction |
| N6 | Lemma FE, Lemma RPc, Theorem L3 (a), (c); Lemma CB, MX, L1-ev, Theorem EV-L (c), (d): limit states of periodic tori cluster on A at rate m_0 | `gap-seed-limit.md` 4.2-4.3 (row 700), `gap-flux-exercise.md` 8.2 | rows 703, 723, 732 | L + limit |
| N7 | Lemma A-cl, Theorem L3-ev: D_nu is a reflection datum, unique vacuum, transfer gap on H_A(nu) | `gap-mini-branch-fable.md` 5.1 (row 1179) | (row 1179's check) | F + L |
| N8 | Proposition P-ev, Theorem BP (i)-(ii): at each cutoff, rate M_* in physical units | same file 5.2, 6 | same | L |
| N9 | Statements (1), (3), (5a)-(5c), Lemma E of `gap-os-equiv.md`: Hilbert space of a reflection datum; decay on a total class gives the gap; the gap passes to limits | `gap-os-equiv.md` (row 668) | on file as checked | F |
| N10 | Lemma DT (dense times suffice) and literal (H2) by a diagonal argument | row 1449 L97-99; check 1450 L48-50 | check 1450 | F |
| N11 | Continuum datum from S: (P1)-(P4), class C, maps iota_j into V_A, (TOT), Borel admission by Lemma FE | row 1449 Step 2 table; check 1450 L27-36 | check 1450 | R |
| N12 | Proposition P'-ev: unique vacuum and spec(H_S) in {0} union [M_*, infinity), M_* = (2/l) log(2^18/5041) | `gap-mini-branch-fable.md` 5.3; check 1450 L56-62 | check 1450 | F + R |
| N0 | BND, BND-1, BND-2: beta_K exists and is bracketed at every late K (only needed to state the target and to read it as the right one) | check 1453 L24-55 | check 1453 | R |

Reading of the table for the design (my own, **sketched**): the chain splits at one interface.

- **Interface (CL-nu), "uniform lattice clustering on the tr F^2 class".** For the release's states nu_j and the
  maps iota_j: there is M_* > 0 with u_j(iota_j F, iota_j F; t) <= C_F(j) e^(-M_* t) for every F in C, every
  late j and every lattice time t >= t_F (the constant may depend on j and F; only the rate is uniform). This is
  hypothesis (H1) of Statement (5) in the weak diagonal form that Statement (3) consumes at each j.
- **Upper half (U): (CL-nu) gives the gap of S.** Nodes N9-N12. Soft. It reads the release (the limit S, its
  axioms, nu_j, moment convergence). No transfer operator on a finite slice is needed here.
- **Lower half (W): (M-neutral-all) gives (CL-nu).** Nodes N1-N8. Lattice only. It needs the finite-slice Wilson
  transfer operator, the 64 twists, the doubling induction, and the passage from periodic tori to nu_j. It reads
  the release only through the definition of the finite Wilson law and of `IsInfiniteVolumeLimit`.

The size and the hardest step are decided by (W). Sections 2-3 inventory what exists for each half.

## 2. Inventory of the release (read from the source; nothing built or run)

Paths are relative to the release root `YM4 Lean/` at 3932084a9b82. `Y/C/` abbreviates `YangMills/Construction/`.
All declarations below are marked **read**: I opened the file and the lines quoted. I did not check their proofs.
The release separates statements from proofs: a file `X.lean` defines a `Prop` named `...Statement`, and a file
`XProof.lean` proves it. I cite the statement files. Toolchain `leanprover/lean4:v4.33.1`; Mathlib at
0df444a360ea (confirmed in `.lake/packages/mathlib`); four libraries `YangMills`, `Formulation`, `Challenge`,
`Reconstruction` (`lakefile.toml`).

### 2.1 The Wilson transfer operator on a spatial slice: EXISTS

File `Y/C/TransferOperators/` (147 files, 19,568 lines). Namespace `YangMills.Construction.TransferOperators`.

| Object of the chain | Declaration | File, line | What it is |
|---|---|---|---|
| The periodic box | `structure CubicPeriodSublattice` (fields `side : ℕ`, `one_le_side`, `lattice : InfiniteLattice.PeriodSublattice 1`, `periods_eq`) | `CubicToriAndProductsOfOperatorsOnPowersOfG.lean` 8-12 | The cubic torus of integer side at spacing 1. It exists iff side >= 3 (`GibbsHaarKernels.CubicPeriodSublatticeIffThreeLe`, `PeriodicStatesHaarMeasureCubicLatticesAndIntegralOperators.lean` 31-33). |
| Slice links, sites, faces | `Γ.LinkOrbits μ`, `Γ.VertexOrbits μ`, `Γ.FaceOrbits μ` (finite types) | `TransferOperatorOfACubicTorus.lean` 30-32 | Orbits of slice links under the periods inside the slice normal to the axis μ. So every axis can be time. |
| L^2 of the slice | `abbrev Γ.SliceL2 μ := HaarL2 (Γ.LinkOrbits μ)`; `abbrev HaarL2 ι := Lp ℂ 2 (haarPi ι)` | same file 208; `Y/C/Matrices/FunctionsAndOperatorsOfSeveralVariablesOnG.lean` 17 | A Mathlib `Lp` space over product Haar on SU(2)^links. It carries Mathlib's inner product. All link functions, not only gauge-invariant ones. |
| Gauge action and projection | `Γ.gaugeRep g`, `Γ.gaugeProjection μ` | same file 213-225 | Defined by `Classical.epsilon` of a predicate; the properties are `GaugeRepProperties` (`FactsOfTheOperatorsOfACubicTorus.lean` 20-44): unitary representation, the projection is symmetric, idempotent, with range the invariant vectors. |
| Slice energy factor | `Γ.sliceEnergy β u`, `Γ.boltzmannMultiplier μ β` | same file 204-207, 226-232 | Multiplication by exp(-β Σ_faces (1 - ½ tr U_p)) on the slice. |
| Time-link factor | `linkProductKernel β u u'`, `linkProductOperator β B`, `sqrtLinkOperator β B` | `BondKernelAndLayerEnergy.lean` 9-11; `SquareRootOfTheBondKernel.lean` 25 | The one-bond heat-type kernel between two slices and its positive square root. |
| **T** | `def Γ.transfer μ β : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ := (halfTransfer ∘ boltzmannMultiplier ∘ halfTransfer)`, `halfTransfer := sqrtLinkOperator ∘ gaugeProjection` | `TransferOperatorOfACubicTorus.lean` 233-239 | T = P_G K^(1/2) e^(-V) K^(1/2) P_G. This is the lane's T = M C M up to which factor is in the middle (see the note below). |
| T is positive, symmetric, trace class | `structure Γ.TransferProperties μ β` (`transfer_nonneg`, `transfer_symm`, `transfer_traceClass`, `half_hilbertSchmidt`, `transfer_eq_sandwich`, `entry_summable`) inside `CubicTorusOperators.Statement` (for every β > 0, Γ, μ) | `FactsOfTheOperatorsOfACubicTorus.lean` 78-98, 131-136 | The spectral input of Lemma M1: T >= 0, self-adjoint, trace class. |
| Hilbert–Schmidt, trace | `IsHilbertSchmidtPW T := Summable (k ↦ ‖T (peterWeylVec k)‖^2)`, `IsTraceClassPW`, `TraceSummablePW`, `tracePW T := ∑' k, peterWeylEntry T k k` | `Y/C/Matrices/HilbertSchmidtOperatorsTraceClassAndTraceOnG.lean` 8-16 | Predicates and a trace in the Peter–Weyl basis `peterWeylVec`. **No Hilbert–Schmidt norm as a number is defined.** |
| Z = Tr T^n | `Γ.PartitionFunctionEqTrace μ β := TraceSummablePW (T ^ Γ.side) ∧ partitionFunction β = tracePW (T ^ Γ.side)`; `CubicPartitionFunctionTraceStatement` | `ObjectsOfAnInsertionOfContractionsBetweenLayers.lean` 53-55; `NormaliserOfACubicTorusIsATrace.lean` 6-7 | The trace formula, **only for time length equal to the side** (the 4D torus is cubic). |
| Product over layers | `Γ.BoltzmannWeightEqProdSlices μ β` | same Objects file 44-52 | The Wilson weight of the torus as a product over time layers in a temporal transport. |
| Operator insertions | `Γ.ExpShiftIntegralEqTrace`, `interleavedProd`, `ContractionInsertionStatement` | Objects file 100-107; `InsertionOfContractionsBetweenLayers.lean` 9-27 | Tr of T interleaved with block operators equals a torus integral. This is the pattern of the lane's (TM-tw) proofs, for contractions on blocks. |
| Kernel operators on SU(2)^J | `Schatten.kernelOp`, `HasKernel`, `GibbsHaarKernels.ContinuousKernelCompAndUniqueness` | `Y/C/HilbertSpace/SchattenTraceKernels.lean` 10-14; `PeriodicStates...IntegralOperators.lean` 46-58 | Composition of continuous kernels, uniqueness of the kernel. |

Notes (**read**, with my reading marked).

- "Twisted" in this folder (`TwistedActionOnAPowerOfG.lean`) means a gauge action with separate source and target
  maps. It is not a centre twist. I found no centre twist, flux sector or Z_2 object in the file names of this
  folder (search of the names for `centre`, `center`, `flux`, `sector`: see 2.2).
- The lane's T acts on gauge-invariant functions and is written M C M (`gap-mini-mneutral-fable.md` L420). The
  release's T acts on all of L^2 and carries P_G on both sides, so it is zero off the invariant subspace. The two
  agree on the invariant subspace up to the placement of the square roots: release K^(1/2) e^(-V) K^(1/2), lane
  e^(-V/2) K e^(-V/2). The non-zero spectra agree (AB and BA). **sketched**: the eigenvalues x_a and the sums
  s(u) of the chain are the same for both forms; the unit vector φ of the rank-one test differs by a fixed map.
  The Lean statement of (M-neutral-all) in Section 4 uses the release's form.
- The trace formula is only at time length = side. The chain needs Tr(P T^t) for other t (t = n/2 in N3, 2w in
  M2 (iv)) and for twisted boundary conditions. As statements about T alone these need no torus: s(u) is a sum
  over the spectrum of T. The torus enters only in the lane's proofs of N3-N6.

### 2.2 The electric-neutral projection P_0, twists, flux sectors: ABSENT

- I listed the file names of `Y/C/TransferOperators`, `InfiniteLattice`, `ReflectionPositivity` and
  `ChessboardTori` for `centre`, `center`, `flux`, `sector`, `twist`, `parity`, `sign`. The hits are about
  centred moments, signs of states, and the gauge "twisted action" of 2.1. None is a centre translation, a
  twisted boundary condition or a flux sector. **read** (names only; a declaration inside a file with another
  name is not excluded).
- So P_0 (the mean of the eight centre translations of the slice, `gap-mini-mneutral-fable.md` L79), the 64 twists
  and the sector sums S_w, S_kappa, S_ev of `gap-flux-exercise.md` 8.3 have to be defined new. The building
  blocks exist: `Γ.coordResidues`, `Γ.linkClass`, `linkRep`, the `axis` of a slice link
  (`TransferOperatorOfACubicTorus.lean` 68, 37, 41, 117-118), `HaarPiInvariance` (multiplication by fixed group
  elements preserves product Haar), and `linkRelabelOp`, `tensorOne` for operators on sub-families of links.

### 2.3 Hilbert–Schmidt norm: predicate exists, the number does not; Mathlib has neither

- Release: `IsHilbertSchmidtPW` and `tracePW` of 2.1. No `hsNorm`.
- Mathlib at 0df444a360ea: `find` over `Mathlib/` for file names with `schmidt`, `schatten`, `TraceClass` gives
  only `GramSchmidtOrtho.lean`. `Mathlib/Analysis/InnerProductSpace/Trace.lean` and `SingularValues.lean` are
  finite-dimensional. `Rayleigh.lean` has the eigenvector at a maximum of the Rayleigh quotient and the
  finite-dimensional existence statement only. `Mathlib/Analysis/Normed/Operator/Compact.lean` exists. **read**.
- Consequence: the statement of (M-neutral-all) needs one new definition, the squared Hilbert–Schmidt norm in
  the Peter–Weyl basis, `hsSqPW A := ∑' k, ‖A (peterWeylVec k)‖ ^ 2`. Whether `peterWeylVec` is proved to be a
  Hilbert basis of `HaarL2` in the release I did not find by name; it is needed for basis independence only, and
  the statement below does not need basis independence. **sketched**.

### 2.4 Infinite-volume lattice states nu_j and their moments: EXIST

Namespace `YangMills.Construction.InfiniteLattice`, folder `Y/C/InfiniteLattice/` (693 files).

| Object | Declaration | File, line |
|---|---|---|
| Fields on a Z^4 of spacing a | `def GaugeField (a : ℝ) := {U : Link a → SU(2) // ∀ b, U b.opposite = (U b)⁻¹}` | `GaugeFieldsAndStates.lean` 71-72 |
| Plaquette energy, smeared energy | `faceEnergy U p = 1 - ½ Re tr`, `smearedEnergy f U = ∑ᶠ p, faceEnergy U p • f p.center` | same 69-70, 90-92 |
| Local observables | `IsLocalObservable`, `linkSigma`, `regionSigma`, `continuousLocalFunctions` | same 77-87 |
| Gibbs property | `IsGibbs β ν` (DLR with `wilsonSpecification`), `IsPeriodicGibbs`, `periodicGibbsSet L K β` | same 276-285 |
| nu_j | `IsInfiniteVolumeLimit L K β ν := IsWeakSubsequentialLimit (fun m => liftedWilsonMeasure L m K β) ν` (weak limit on bounded continuous tests along a subsequence of sides 2 L^(m+K)) | same 341-347 |
| Centred moments | `centeredMoment ν h := E_ν ∏ (smearedEnergy (h l) - E_ν smearedEnergy (h l))`, for any tuple h (no separation needed) | `ConnectedCorrelations.lean` 14-17 |
| Cumulants | `ursellFunction ν n f`, `smearedEnergyCumulant` | same 12-13 |
| Lattice reflection form and transfer | `reflectionPairing μ t B A`, `upperAlgebra t`, `reflectionPairingRoot`, `insertedTransfer`, `PeriodicGibbsReflectionTransfer` (positive Hermitian pairing at every half-spacing time for every state in `periodicGibbsSet`) | `ReflectionFormAndTransferOperatorOfAPeriodicGibbsState.lean` 11-70 |
| Symmetry, link-mirror positivity | `IsSymmetricReflPosGibbs`, `TorusStateLimitPoints` (check 1450 L23: symmetry at axial site and link mirrors, positivity at the half-odd link mirrors) | `InfiniteVolumeLimitPointsOfTheTorusStates.lean` 27-52, 78-84 (lines from check 1450; file opened by name only) |
| Finite torus measure | `PeriodicLattice.wilsonGibbsMeasure L m K β`, `liftField`, `Γ.lattice.partitionFunction β`, `quotientHaar`, `boltzmannWeight` | `GaugeFieldsAndStates.lean` 323-340; `Y/C/TransferOperators/ObjectsOf...Layers.lean` 44-55 |

Two torus models coexist: the tori of side 2 L^(m+K) at spacing L^(-K) (`PeriodicLattice`, used for nu_j), and
`PeriodSublattice 1` quotients at spacing 1 with any side >= 3 (`CubicPeriodSublattice`, used for T). The seed
cube n_K = l b^K is of the second kind. A dilation bridge exists by name (`DilationCarriesStatesToSpacingOne.lean`,
`CopyOfAStateOnADilatedLattice.lean`); not opened. **read** for the names.

### 2.5 The OS Hilbert space, the time semigroup, H, the vacuum, clustering: EXIST (two interfaces)

Interface B is the one the release's main theorem uses for the mixture; the design uses it.

| Object | Declaration (interface B) | File, line |
|---|---|---|
| Functional on separated tuples | `structure SeparatedTuples.TupleFunctional`; the mixture is `centredOf S` for `S : CumulantFamily` | `Y/C/ReflectionPositivity/SeparatedTuplesOfFourSpaceAndTheirFunctionals.lean` 144 |
| Positive-time span, form | `PositiveSpan := spanIn TimeAxis.upperHalfSpace`, `reflectionForm σ F F'` | `Y/C/ReflectionPositivity/FormOfAFunctionalOnSeparatedTuples.lean` 11-15 |
| OS Hilbert space | `PhysicalSpace σ hσ := FormCompletion (reflectionForm σ) hσ` for `hσ : IsPosSemidef (reflectionForm σ)`; `posClass σ hσ : PositiveSpan →ₗ[ℂ] PhysicalSpace σ hσ` | `Y/C/ReflectionPositivity/ReconstructionOfAFunctional.lean` 29-30 |
| Vacuum | `vacuum σ hσ := posClass σ hσ (the empty tuple)` | same 36-37 |
| Time semigroup | `timeShift σ hσ : ℝ≥0 → PhysicalSpace σ hσ →L[ℂ] PhysicalSpace σ hσ` (by `Classical.epsilon` of `IsTimeShiftFamily`) | same 38-43 |
| Hamiltonian | `hamiltonian σ hσ` with `timeShift t = expNeg A t`; and `PairMeasureOperators.pairHamiltonian σ hσ`, `pairMomentum`, `groundStateProjection`, `pairJointSpectrum` | same 44-46; `Y/C/ReflectionPositivity/HamiltonianAndMomentaFromThePairMeasures.lean` 11-35 |
| Dense times suffice (contraction) | `structure ContractionHypotheses σ S` (S dense in (0, ∞), `reflectedCorrelation σ F ((2t) • timeBasisVec) ≤ reflectionForm σ F F` on S) | `ReconstructionOfAFunctional.lean` 19-26 |
| Package | `HasReconstruction σ h := VacuumProperties ∧ TimeSemigroupProperties ∧ SpaceShiftProperties ∧ MatrixElementFormula` | `Y/C/LimitTheorem/FunctionalDefs.lean` 78-82 |
| For the mixture | `LimitConditions.reconstruction : ReconstructionConditions (centredOf S)` (form positive, `HasReconstruction`, separable, joint spectrum in {y_0 >= 0}) inside `LimitProperties` | `Y/C/SystemsWithFiveBounds/TheoremOverASystemWithFiveBounds.lean` 93-99, 154-176 |
| Unique vacuum, per component | `ComponentReconstruction.kernel_eq : opKernel (pairHamiltonian σ h) = ℂ ∙ vacuum σ h` | same 214-222 |
| Zero-energy space of the mixture | `ZeroEnergyIsL2 σ A`: `hamiltonianKernel σ h ≃ₗᵢ Lp ℂ 2 A.law`, and `ENat.card A.space = rank (hamiltonianKernel σ h)` | same 184-195 |
| Clustering, per component | `InverseSquareClustering K σ` (rate \|v\|^(-2)) | same 100-104 |
| The states behind S | `PairSequence` (`cutoff`, `coupling`, `state`, `isLimit`), `Q.Defines S`, `Q.PeriodicInvariantStates` | same 109-136 |

Interface A (`Y/C/ReflectionPositiveLimits/`, on `σ : Tuple → ℝ`): `ReconstructionSpace σ h`, `toReconstruction`,
`transferSemigroup σ h`, `hamiltonian σ h`, `jointSpectralMeasure`, `ContractsOnDenseTimes σ`,
`ReconstructionData σ` (`ReconstructionFromAContractionAtADenseSetOfTimes.lean` 43-190,
`ReconstructionOfAFunctional.lean` 26-80); and the qualitative theorem
`TimeClustering.VacuumClusteringHolds`: `KernelIsVacuumRay σ hσ ↔ ClustersInTime σ`
(`VacuumErgodicityAndClusteringInTime.lean` 34-78). This is the release's own "clustering in time gives a
unique vacuum". It has no rate. A quantitative version is what the chain adds.

Not found in the release: any statement with an exponential rate in the separation, a spectral gap of a
Hamiltonian, or a positivity-improving (Perron–Frobenius) statement for T (file-name search for `gap`,
`exponential`, `decay`, `Perron`, `GroundState`; the `gap` hits are geometric gaps between patches). **read**
(names only). Row 1449 1c and check 1453 reached the same verdict from the statements.

### 2.6 The theorem to extend, and where S and nu_j are exposed together

- Public: `YangMills.wilson_subsequence : Wilson.ContinuumLimitFor Wilson.selectedGauge` (`Challenge.lean`
  234-262). S is under an existential; nu_j does not appear.
- Internal: `YangMills.su2_fixed_observable_continuum_limit : FixedObservableLimit FixedObservableContinuum`
  (`Formulation/FixedObservableContinuum.lean` 169-171). `FixedObservableContinuumWith P L M g₀` (same file 20-55)
  is `∃ K m ν S X₂ X₄, ...` with these clauses for the same witnesses: `IsLeast ... (g j)` at every K_j with
  `g j = renormalizedBareCoupling L M (K j) g₀`, `β j = (g j ^ 2)⁻¹`; `IsInfiniteVolumeLimit L (K j) (β j) (ν j)`;
  the β slope; `Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.1) atTop (𝓝 (centredOfCumulants S ⟨n,X⟩))`
  for every separated tuple X; and for the mixture a `FlatSequence T` with
  `HasSchwingerSequence (centredOf S) T`, growth, `IsEuclidInvariant T`, `IsOSPositive T`.
- The least-root coupling is defined at **every** cutoff k, not only on K_j: `Wilson.bareCoupling G L M k g₀ :=
  sInf (couplingsAt G L M k g₀)` (`Challenge.lean` 122-123), internally `renormalizedBareCoupling L M k g₀`.
  So (M-neutral-all) can be stated with no reference to the proof's subsequence, and BND (check 1453) is not
  needed to state it.
- Inside the proof the stronger mixture facts are available but not exported: `hAss := hsh.ergodic Q' S hS`
  with `hAss.limit : LimitProperties ...` (`Formulation/ContinuumLimit.lean`, in
  `su2_continuum_limit_of_frequent_passage`, lines about 180-200). The step
  `BranchHot.fixed_observable_continuum_of_no_escape` is `private`. **read**.

Design consequence (**sketched**): state the conditional theorem for **every** tuple of witnesses of
`FixedObservableContinuumWith P L M g₀`, not for "the" constructed ones. Then nothing of their proof has to be
re-opened or copied, and the final packaged statement follows from `su2_fixed_observable_continuum_limit` by one
`obtain`. The mixture facts the proof needs (the form of `centredOf S` is positive; `HasReconstruction`; the
ν_j are periodic Gibbs states with link-mirror positivity) have to be derived from the exported clauses by the
release's general theorems. Which named theorem gives each is the first thing a build row must settle (Section 6).

## 3. The named chain items against the release (item (1) of the row)

"Lane" columns cite the hand statement. "Lean" says what exists. EXISTS = a declaration of the release or Mathlib
states the object; PART = a building block exists, the object does not; ABSENT = nothing found.

| Chain item | Lane | Lean status | Declaration or what is missing |
|---|---|---|---|
| Wilson transfer operator on a spatial slice | T = M C M, `gap-transfer.md` (TR) | EXISTS | `CubicPeriodSublattice.transfer μ β` (2.1). Cubic slices only: side^3. That is the shape (M-neutral-all) needs. |
| Its spectrum (eigenvalues λ_a, top λ_0, sums s(u)) | row 1356 Section 2 | PART | Positivity, symmetry, trace class: `TransferProperties`. No eigenvalue sequence, no top eigenvector, no simplicity of λ_0. The release has the spectral theorem for bounded self-adjoint operators (`Y/C/SpectralTheory/EverySelfAdjointOperatorIsResolved.lean`, by name) but no compact-operator form; Mathlib has none (2.3). |
| Electric-neutral projection P_0 | mean of the eight centre translations | ABSENT | To define (2.2). |
| Hilbert–Schmidt norm | row 1356 | PART | `IsHilbertSchmidtPW`; the number is one new definition (2.3). |
| Z = Tr T^t, also with operators between layers | (TM), (TM-tw) | PART | `PartitionFunctionEqTrace` (t = side only); `KernelCycleTrace.Statement`: ∫ kernelCycle β X = tracePW (interleavedProd X T) for any contractions X_k between the layers of a cubic torus (`CycleOfKernelsIsATrace.lean` 11-28). With X = a centre translation at one layer this is an electric twist. Rectangular tori, magnetic twists and the exchange of axes for twisted tori: ABSENT. |
| OS Hilbert space, time semigroup, H (continuum) | `gap-os-equiv.md` Statement (1) | EXISTS | `PhysicalSpace`, `posClass`, `vacuum`, `timeShift`, `hamiltonian`, `pairHamiltonian`, `HasReconstruction` (2.5). |
| OS form and transfer of a lattice state | L3-ev (e-ev), Lemma RPc | EXISTS, with link mirrors | `reflectionPairing μ t`, `upperAlgebra t`, `PeriodicGibbsReflectionTransfer`, with the log-convexity `ReflectionMomentsLogConvex` (2.4). The lane's site-mirror datum on the centre-blind class A is ABSENT and, in the design below, not needed. |
| Infinite-volume states ν_j | P-ev (b) | EXISTS | `IsInfiniteVolumeLimit L (K j) (β j) (ν j)` in `FixedObservableContinuumWith` (2.4, 2.6). |
| Statement (5) (the gap passes to limits) | `gap-os-equiv.md` L216-234 | ABSENT | No statement with a rate. The release has the limit of forms (`ContractionHypotheses`, dense times) for contraction only. |
| Statement (3) (decay on a total class gives the gap) | `gap-os-equiv.md` L165-195 | ABSENT; the qualitative analogue EXISTS | `TimeClustering.VacuumClusteringHolds` (clustering in time iff ker H is the vacuum ray), no rate. |
| Lemma DT (dense times) | row 1449 L97 | PART | The same device for contraction: `ContractionHypotheses.dense`, `ContractsOnDenseTimes`. Not for a rate. |
| Lemma FE (finite energy) | `gap-seed-limit.md` L120-126 | ABSENT, **not needed** | See the reduction below: the design tests ν_j on bounded continuous functions only. |
| Lemma M1, Corollary M2 | row 1356 2.1-2.2 | ABSENT | Elementary; needs the Hilbert–Schmidt inner product. |
| Theorem S, Lemmas K, X, E, E', S3' | row 697, 699 | ABSENT | Abstract statements on a symmetric function W(a, b) with trace-type inequalities. No gauge theory inside. |
| Lemma W, Theorem S-w, Corollary EV, Proposition CL | row 731 8.3-8.4 | ABSENT | Finite algebra on Z_2^6 plus (TM-tw). |
| Explicit finite-aspect theorem (K = 512) | row 1161 L213-227 | ABSENT | Needs all 64 twists, both frames, Taylor bounds on sums of x^s. |
| Lemma CB, MX, L1-ev, Theorem EV-L | row 731 8.2 | ABSENT | Needs torus expectations of slab functions as traces with an inserted operator. The release's insertion formulas are for block contractions built from kernel ratios (`ExpShiftIntegralEqTrace`), a different shape. |
| Proposition P-ev (b) | row 1179 5.2 | ABSENT | Follows from the two rows above. |
| Theorem BP | row 1179 Section 6 | ABSENT | A composition. |
| Proposition P'-ev | row 1179 5.3 | ABSENT | A composition of Statement (5) with the release's limit. |
| BND, BND-1, BND-2 | check 1453 | ABSENT, **not needed for the theorem** | The hypothesis is stated at `bareCoupling ... k g₀` for every k (2.6). BND explains why the hypothesis is reasonable. It is not a step of the implication. |

### 3.1 A shorter chain for Lean (**sketched**; this is a design proposal, not a checked proof)

The hand chain builds a lattice reflection datum on the centre-blind class A with the site mirror (Theorem L3-ev),
proves its transfer gap from clustering by Statement (3), and passes the gap to the limit by Statement (5). The
release already has reflection positivity of every periodic Gibbs state at link mirrors on **all** local
functions, with the log-convexity of the reflected moments. That allows a shorter route with one scalar interface.

**Interface (EC-ν): exponential time clustering of the ν_j at one physical rate.** There is M > 0 such that for
every finite complex combination Z of positive-time separated smooth tuples and every late j there is C < ∞ with

    u_j(Z; t) <= C exp(- M t)   for every t in 2 a_j N,

where u_j(Z; t) := sum over k, l of conj(c_k) c_l cm_j(θX_k ++ τ_t X_l) - |sum over k of c_k cm_j(X_k)|^2, and
cm_j is `InfiniteLattice.centeredMoment (ν j)`. C may depend on Z and j. Only M is uniform.

Step U1 (lattice, **sketched**). Fix j and Z. Put A := the lattice function sum_k c_k prod_i (smearedEnergy(f_i) -
mean) minus its ν_j-mean; it is bounded, continuous, local, at positive times. Then u_j(Z; 2 n a_j) is the
reflected moment m_n of A at the link mirror between times -a_j/2... (the mirror position needs care: see U1'
below). By `ReflectionMomentsLogConvex` (with the trivial insertion D = 1) the sequence m_n is non-negative and
log-convex. A non-negative log-convex sequence with m_n <= C q^n satisfies m_(n+1) <= q m_n for every n
(if m_(N+1) > q m_N > 0 then the ratios, which do not decrease, give m_n >= m_N (m_(N+1)/m_N)^(n-N), and this
beats C q^n; if m_N = 0 then log-convexity gives m_n = 0 for n > N... see the remark). So

    u_j(Z; t) <= exp(- M (t - s)) u_j(Z; s)   for s <= t in 2 a_j N.          (R_j)

This is (5.1) of Statement (5) without a lattice Hilbert space, and it replaces Statement (3) on the lattice.

Remark on m_N = 0. Log-convexity m_n^2 <= m_(n-1) m_(n+1) alone allows m = (1, 0, 1). The release's second
inequality m_1^n <= m_0^(n-1) m_n, applied to the shifted function, gives m_(N+1)^2 <= m_N m_(N+2) and
m_(N+1) <= m_N^(1/2) m_(N+2)^(1/2); with m_N = 0 this forces m_(N+1) = 0. So zeros propagate forward. **sketched**.

U1' (mirror kind; an open point of the design, **guessed**). The release's lattice positivity is at link mirrors
(half-odd times); its continuum form uses the mirror x_4 = 0 on tuples at positive times. A tuple X at positive
continuum times has its plaquettes at lattice times >= 0, and a temporal plaquette based at time 0 is cut by
the link mirror at time a_j/2 only if the mirror is put there. Put the link mirror at time -a_j/2 (it is a
link mirror: half-odd), so that all of A lies strictly above it, and use the reflection about -a_j/2, which is
the site reflection θ composed with the shift by -a_j. Then m_n = cm_j(θ' A, τ_(2n a_j) A) with θ' = τ_(-a_j) θ,
which equals u_j(Z; 2 n a_j + a_j) by shift invariance. So (R_j) holds on the odd grid a_j (2N + 1) rather than
on 2 a_j N. Both grids are dense in the limit, and Step U2 uses only a dense set. To be settled in the first
build row against `AxisMirrorData` and `halfSpacingTimes`.

Step U2 (limit, **sketched**). For t in the dense set of times that are on the grid for all late j, the clause
`Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.1) atTop (𝓝 (centredOfCumulants S ⟨n, X⟩))` of
`FixedObservableContinuumWith`, applied to the separated tuples θX_k ++ τ_t X_l and X_k, gives
u_j(Z; t) -> u_∞(Z; t) := reflectedCorrelation σ Z (t • timeBasisVec) - |<Ω, Z>|^2 with σ = centredOf S. So (R_j)
passes to u_∞ on the dense set, and to all 0 <= s <= t by the strong continuity of `timeShift` (Lemma DT;
the two approximating times are chosen with s' <= t').

Step U3 (Hilbert space, **sketched**). For ψ = posClass σ hσ Z - <Ω, Z> Ω: ‖timeShift (t/2) ψ‖^2 = u_∞(Z; t)
(matrix element formula of `HasReconstruction`), so ‖timeShift r ψ‖ <= exp(- M r) ‖ψ‖ for every r >= 0. Such ψ
are dense in the orthogonal complement of the vacuum (`posClass` has dense range; project). `timeShift r` is
bounded. So the bound holds on the whole complement. This is the mass gap in semigroup form. Unique vacuum
and the spectral form follow from it by the functional calculus the release already has.

What this removes from the Lean chain: Lemma FE (all tests are continuous), Lemma RPc and Theorem L3-ev (the
site-mirror datum), Statement (3) (replaced by the sequence lemma in U1), Statement (1) and (5) as general
theorems (replaced by U2, U3 on the release's `PhysicalSpace`), and the totality argument (TOT) (the class is
the whole dense subspace, because Z ranges over combinations, not single tuples).

What it does not remove: everything from (M-neutral-all) to clustering of ν_j, that is N1-N6 and P-ev (b).
P-ev (b) gives, for bounded continuous centre-blind local F, H separated by d lattice steps in the time
direction: |ν_j(F H) - ν_j(F) ν_j(H)| <= ‖F‖ ‖H‖ exp(- M_* d a_j). With F = conj(θ' A), H = τ_t A this is (EC-ν)
with C = sup|A|^2 (after the bounded shift of the separation by the time extent of A).

I have not found this shorter route on file. Search: `grep -l -i -E "log-convex|logconvex|log convex"` over
`library/gap-os-equiv.md`, `gap-mini-branch-fable.md`, `gap-seed-limit.md`, `prior/sa-ym4-lean-inputs-opus.md`
and `open-core.md` (run in the next step; result recorded there). The device itself is classical (it is the
proof of Lemma A2 of `gap-os-equiv.md`, row 668), so the claim is only about its use against the release.
