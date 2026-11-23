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
- Registry search for 3.1 (run after writing it): `log-convex` occurs in `gap-os-equiv.md` only (Lemma A2, L73,
  used at 3.3 L178). It does not occur in `gap-mini-branch-fable.md`, `gap-seed-limit.md`, rows 1449/1450's
  files or `open-core.md`. `open-core.md` has no line on (M-neutral), (EC-ν) or link mirrors. So the device is
  the lane's Lemma A2; its use with the release's `ReflectionMomentsLogConvex` in place of a site-mirror datum
  is not on file.

## 4. The Lean statements (item (2) of the row)

Status of this section: **design text, not compiled**. Identifiers of the release are the ones read in Section 2
(file and line given there). Identifiers marked NEW are to be defined in the new library. A build row must
expect small type errors (coercions, implicit arguments, `NeZero` instances). Proposed library name:
`GapChain`, one `lean_lib` in a separate lake project that `require`s the release at 3932084a9b82 by path and
Mathlib at the same pin. No file of the release is edited or copied.

### 4.1 New definitions for the hypothesis

```lean
import YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus
import Formulation.FixedObservableContinuum
open YangMills YangMills.Construction YangMills.Construction.TransferOperators
open YangMills.Construction.SpinHarmonics YangMills.Construction.Matrices
open scoped InnerProductSpace NNReal

namespace GapChain

/-- NEW. Hilbert–Schmidt bound without a basis: the sum of ‖A e_i‖² over every finite
orthonormal family is at most δ². Equivalent to ‖A‖_HS ≤ δ, and to nothing weaker. -/
def HSNormLE {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (A : H →L[ℂ] H) (δ : ℝ) : Prop :=
  ∀ (n : ℕ) (e : Fin n → H), Orthonormal ℂ e → ∑ i, ‖A (e i)‖ ^ 2 ≤ δ ^ 2

/-- NEW. The rank-one projector |φ⟩⟨φ|. -/
def ketBra {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] (φ : H) : H →L[ℂ] H :=
  (innerSL ℂ φ).smulRight φ

/-- NEW. The centre element −1 of SU(2). -/
def centreElt : ComplexMatrix2.specialUnitary := ⟨-1, by sorry⟩   -- membership: 2 lines

namespace CubicPeriodSublattice
variable (Γ : CubicPeriodSublattice) (μ : Fin 4)

/-- NEW. The sign field of the centre translation in the spatial direction ν: −1 on the slice
links of axis ν whose source has ν-coordinate ≡ 0 mod side, +1 elsewhere. -/
def centreSign (ν : Fin 4) (e : Γ.LinkOrbits μ) : ComplexMatrix2.specialUnitary :=
  open Classical in
  if (linkRep e).axis = ν ∧ Γ.coordResidues ((linkRep e).source : InfiniteLattice.LatticePoint 1) ν = 0
  then centreElt else 1

/-- NEW. The predicate of the centre translation C_ν, in the release's own style
(compare `IsGaugeRep`, `TransferOperatorOfACubicTorus.lean` 209-212). -/
def IsCentreTranslation (ν : Fin 4) (T : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ) : Prop :=
  ∀ φ : Γ.SliceL2 μ, (T φ : (Γ.LinkOrbits μ → ComplexMatrix2.specialUnitary) → ℂ)
    =ᵐ[ComplexMatrix2.haarPi (Γ.LinkOrbits μ)]
    fun u => (φ : (Γ.LinkOrbits μ → ComplexMatrix2.specialUnitary) → ℂ)
      (fun e => Γ.centreSign μ ν e * u e)

def centreTranslation (ν : Fin 4) : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ :=
  Classical.epsilon (Γ.IsCentreTranslation μ ν)

/-- NEW. The electric-neutral projection P₀: the mean over the eight centre translations
of the slice normal to μ, written as a product of three commuting projections. -/
def neutralProj : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ :=
  ((Finset.univ.erase μ).toList.map fun ν => (1 / 2 : ℂ) • (1 + Γ.centreTranslation μ ν)).prod

/-- NEW. The rank-one test of (M-neutral) on one cube at one coupling:
there are 1 ≤ w ≤ side/1024, a unit vector φ and c > 0 with
‖c⁻¹ P₀ T^w − |φ⟩⟨φ|‖_HS ≤ 2/5. -/
def NeutralRankOneTest (β : ℝ) : Prop :=
  ∃ (w : ℕ) (φ : Γ.SliceL2 μ) (c : ℝ), 1 ≤ w ∧ 1024 * w ≤ Γ.side ∧ ‖φ‖ = 1 ∧ 0 < c ∧
    HSNormLE (((c⁻¹ : ℝ) : ℂ) • (Γ.neutralProj μ * Γ.transfer μ β ^ w) - ketBra φ) (2 / 5)

end CubicPeriodSublattice
```

Faithfulness points of 4.1 (each one is a place where a wrong definition would make the theorem empty or false).

1. `HSNormLE` is basis-free on purpose. A definition by `∑'` over `peterWeylVec` returns 0 for a
   non-summable family in Lean, which would make the test true for a non-Hilbert–Schmidt operator; and it
   would be the Hilbert–Schmidt norm only if `peterWeylVec` is complete, which I did not find stated (2.3).
2. `centreTranslation` is an `epsilon` of a predicate. It means C_ν only if an operator with the predicate
   exists. Existence is the first lemma to prove (measure preservation: `HaarPiInvariance`, 2.2). The release
   has the same pattern and proves existence in `GaugeRepProperties.rep_formula`.
3. `centreSign` reads a representative `linkRep e`. The axis and the residue of the source do not depend on the
   representative (`coordResidues` is constant on orbits; `linkOrbit` keeps the axis). Two lemmas.
4. Different planes x_ν = r give centre translations that differ by a gauge transformation with values ±1. On
   gauge-invariant vectors they agree. T carries P_G on both sides (2.1), so P₀ T^w does not depend on r. Lemma.
5. The release's T is K^(1/2) e^(-V) K^(1/2) between gauge projections, the lane's is e^(-V/2) K e^(-V/2). The
   spectra agree off zero. The lane's test and this test are equivalent by Corollary M2 (i): both say
   s(2w) ≤ 4/21, and s reads only the non-zero neutral spectrum. **sketched**; this equivalence needs M2 in both
   forms and is a lemma of the list (L1.4 below), not an assumption.
6. Time axis. The hypothesis is stated with one axis μ. All four give the same statement by the hypercubic
   symmetry of the cube. The theorem below uses `TimeAxis.timeIdx`, the axis of the release's continuum form.

### 4.2 The hypothesis (M-neutral-all) and its form along the extracted cutoffs

```lean
open Formulation in
/-- NEW. β_K at the least-root coupling of the release, at every cutoff K
(`renormalizedBareCoupling`, `Formulation/ReferenceCoupling.lean` 162). -/
def betaAt (L M K : ℕ) (g₀ : ℝ) : ℝ := (renormalizedBareCoupling L M K g₀ ^ 2)⁻¹

/-- NEW. (M-neutral-all), check 1453 L101-105, word for word: one physical side ℓ ∈ 4ℕ, and for
every late cutoff K the rank-one test on the cube of ℓ·L^K sites at the coupling β_K. -/
def MNeutralAll (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Prop :=
  0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ K₀ : ℕ, ∀ K : ℕ, K₀ ≤ K →
    ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ K →
      Γ.NeutralRankOneTest ReflectionPositivity.TimeAxis.timeIdx (betaAt L M K g₀)

/-- NEW. (M-neutral-Lean): the same on infinitely many cutoffs of a given sequence K. This is all
the theorem uses (check 1450 L62; row 1449 L124). -/
def MNeutralAlong (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) (K : ℕ → ℕ+) : Prop :=
  0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ᶠ j in Filter.atTop,
    ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
      Γ.NeutralRankOneTest ReflectionPositivity.TimeAxis.timeIdx (betaAt L M (K j) g₀)

theorem MNeutralAll.along {L M : ℕ} {g₀ : ℝ} {ℓ : ℕ} (h : MNeutralAll L M g₀ ℓ)
    {K : ℕ → ℕ+} (hK : StrictMono K) : MNeutralAlong L M g₀ ℓ K := by
  sorry   -- StrictMono K gives K j ≥ K₀ eventually; 10 lines
```

Notes. (a) `∀ Γ` with a given side: any two such Γ have the same period group, so this is one cube. (b) The
hypothesis does not mention the proof's subsequence, the flow, or BND. (c) The side ℓ·L^K is at least 3, so Γ
exists (`CubicPeriodSublatticeIffThreeLe`). (d) The lane's range condition n ≥ 2^70 of the explicit
finite-aspect theorem holds for late K; the theorem's proof takes it from `∃ᶠ` and K → ∞.

### 4.3 The conclusion: unique vacuum and mass gap of the constructed mixture

```lean
open SeparatedTuples ReflectionPositivity.TupleForm HilbertSpaceBasics
open ReflectionPositivity.Reconstruction LimitTheorem

/-- NEW. Mass gap m of the functional σ on separated tuples, in semigroup form on the release's
reconstructed Hilbert space: the form is positive, the reconstruction exists, and the time
semigroup contracts at rate m on the orthogonal complement of the vacuum. -/
def HasMassGap (σ : TupleFunctional) (m : ℝ) : Prop :=
  ∃ hσ : IsPosSemidef (reflectionForm σ), HasReconstruction σ hσ ∧
    ∀ ψ : PhysicalSpace σ hσ, ⟪vacuum σ hσ, ψ⟫_ℂ = 0 →
      ∀ t : ℝ≥0, ‖timeShift σ hσ t ψ‖ ≤ Real.exp (-m * t) * ‖ψ‖

/-- NEW. Unique vacuum: every vector fixed by the time semigroup is a multiple of the vacuum. -/
def HasUniqueVacuum (σ : TupleFunctional) : Prop :=
  ∃ hσ : IsPosSemidef (reflectionForm σ), HasReconstruction σ hσ ∧
    ∀ ψ : PhysicalSpace σ hσ, (∀ t : ℝ≥0, timeShift σ hσ t ψ = ψ) → ∃ c : ℂ, ψ = c • vacuum σ hσ

theorem HasMassGap.uniqueVacuum {σ : TupleFunctional} {m : ℝ} (hm : 0 < m)
    (h : HasMassGap σ m) : HasUniqueVacuum σ := by
  sorry   -- ψ − ⟪Ω,ψ⟫Ω is fixed and orthogonal to Ω, so its norm is ≤ e^(−mt) times itself; 25 lines
```

Faithfulness points of 4.3.

1. `HasReconstruction σ hσ` is inside the conclusion because `timeShift` is an `epsilon`
   (`ReconstructionOfAFunctional.lean` 42-43). Without it the bound would be about an arbitrary operator family.
2. The semigroup form with rate m is the statement spec(H) ⊂ {0} ∪ [m, ∞) with ker H = ℂΩ (Lemma E of
   `gap-os-equiv.md`, (E1) and (E3)). The spectral form in the release's words is a corollary to add later:
   `opKernel (pairHamiltonian σ hσ) = ℂ ∙ vacuum σ hσ` (the shape of `ComponentReconstruction.kernel_eq`), and
   the support of the energy spectral measure outside (0, m). With `ZeroEnergyIsL2` it gives that the canonical
   decomposition has one point: `ENat.card A.space = 1` (2.5). **sketched**.
3. The Hilbert space is the completion of the positive-time span of separated **tensors** (C^1 tuples in the
   release's `SepTuple`). For the larger space of all flat positive-time Schwartz sequences of `Challenge.lean`
   the gap needs the density of the tensors (check 1450 L35; the release's optional
   `Reconstruction/MinkowskiSpace/VectorsOfSmoothSequencesAreTotalInTheClosedSubspace.lean`, by name). That is a
   second theorem (4.6), not part of the first one.
4. "In the tr F² sector" is built into σ = `centredOf S`: S is the limit of centred smeared plaquette
   energies only.

### 4.4 The interface (EC-ν) and the two halves

```lean
open InfiniteLattice

/-- NEW. The reflected, time-shifted, truncated two-point function of a positive-time
combination Z in the lattice state ν, at the time shift t (continuum units). `refl` is the
time reflection of tests and `shiftT t` the time translation; `Z.terms` lists (coefficient,
tuple). The mirror convention is the open point U1' of 3.1. -/
def latticeU {a : ℝ} (ν : MeasureTheory.Measure (GaugeField a)) (Z : PositiveSpan) (t : ℝ) : ℝ :=
  sorry   -- finite double sum of `centeredMoment ν (refl X ++ shiftT t Y)` minus |Σ c_k centeredMoment ν X_k|²

/-- NEW. (EC-ν): exponential time clustering of the lattice states at one physical rate. -/
def ExpClusters (L : ℕ) (K : ℕ → ℕ+)
    (ν : ∀ j, MeasureTheory.Measure (GaugeField (PeriodicLattice.meshSize L (K j : ℤ))))
    (m : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∃ᶠ j in Filter.atTop, ∃ C : ℝ, ∀ n : ℕ,
    latticeU (ν j) Z ((2 * n + 1) * PeriodicLattice.meshSize L (K j : ℤ)) ≤
      C * Real.exp (-m * ((2 * n + 1) * PeriodicLattice.meshSize L (K j : ℤ)))

/-- NEW. The clauses of `FixedObservableContinuumWith` that the chain reads, for named witnesses. -/
structure Inputs (L M : ℕ) (g₀ : ℝ) (K : ℕ → ℕ+)
    (ν : ∀ j, MeasureTheory.Measure (GaugeField (PeriodicLattice.meshSize L (K j : ℤ))))
    (S : CumulantFamily) : Prop where
  strictMono : StrictMono K
  beta_pos : ∀ j, 0 < betaAt L M (K j) g₀
  isLimit : ∀ j, IsInfiniteVolumeLimit L (K j) (betaAt L M (K j) g₀) (ν j)
  moments : ∀ n (X : TestSpaces.SepTupleOfCard n),
    Filter.Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.1) Filter.atTop
      (nhds (TestSpaces.centredOfCumulants S ⟨n, X⟩ : ℂ))
  mixture : ∃ (D : SystemsWithFiveBounds.LimitConstants) (T : ConfigSpace.FlatSequence),
    D.Valid ∧ SystemsWithFiveBounds.HasSchwingerSequence (centredOf S) T ∧
    SystemsWithFiveBounds.SatisfiesGrowth T D.schwartzOrder D.schwartzPrefactor D.schwartzBase D.schwartzExp ∧
    ConfigSpace.IsEuclidInvariant T ∧ ConfigSpace.IsOSPositive T ∧
    ConfigSpace.IsPermSymmetric T ∧ ConfigSpace.IsReflectionReal T

/-- Upper half (U). Soft. Reads the release's limit and reconstruction. -/
theorem massGap_of_expClusters {L M : ℕ} {g₀ : ℝ} {K ν S} (hL : 3 ≤ L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasMassGap (centredOf S) m := by
  sorry

/-- Lower half (W). Lattice only. Reads the release through `transfer`, `IsInfiniteVolumeLimit`
and the finite Wilson measure. -/
theorem expClusters_of_mNeutral {L M : ℕ} {g₀ : ℝ} {K ν S} (hL : Odd L) (hL3 : 3 ≤ L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    ExpClusters L K ν ((2 / ℓ) * Real.log (2 ^ 18 / 5041)) := by
  sorry
```

### 4.5 The conditional theorem

```lean
/-- The conditional gap theorem for named witnesses. -/
theorem massGap_of_mNeutral {L M : ℕ} {g₀ : ℝ} {K ν S} (hL : Odd L) (hL3 : 3 ≤ L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    HasMassGap (centredOf S) ((2 / ℓ) * Real.log (2 ^ 18 / 5041)) ∧ HasUniqueVacuum (centredOf S) := by
  sorry   -- the two halves of 4.4, and HasMassGap.uniqueVacuum; rate positive since 2^18 > 5041

/-- The packaged statement: the release's fixed-observable continuum limit, with one more clause
for the same witnesses. For every admissible L, M, g₀ there are witnesses of
`FixedObservableContinuum L M g₀` such that (M-neutral-all) at any side ℓ gives a unique vacuum
and the mass gap (2/ℓ) log(2^18/5041) of the constructed mixture. -/
def FixedObservableContinuumWithGap (L M : ℕ) (g₀ : ℝ) : Prop :=
  ∃ (K : ℕ → ℕ+) (ν : ∀ j, MeasureTheory.Measure (GaugeField (PeriodicLattice.meshSize L (K j : ℤ))))
    (S : CumulantFamily),
    Inputs L M g₀ K ν S ∧
    -- (here: the remaining clauses of `FixedObservableContinuum L M g₀` for the same K, ν, S, quoted
    --  from `Formulation/FixedObservableContinuum.lean` 26-55, so that S is identified as their limit)
    ∀ ℓ : ℕ, MNeutralAll L M g₀ ℓ →
      HasMassGap (centredOf S) ((2 / ℓ) * Real.log (2 ^ 18 / 5041)) ∧ HasUniqueVacuum (centredOf S)

theorem su2_fixed_observable_gap_of_mNeutral :
    FixedObservableLimit FixedObservableContinuumWithGap := by
  sorry   -- obtain the witnesses from `su2_fixed_observable_continuum_limit`; apply `massGap_of_mNeutral`
```

Reading of the packaged statement, in words. Sussman and Alpoge's theorem gives, for every large odd L, some M
and δ, and for every g₀ in (0, δ), a cutoff sequence K_j, infinite-volume lattice states ν_j and a continuum
limit S. The new clause says: for these same K_j, ν_j, S, if for some ℓ ∈ 4ℕ the rank-one test holds on the cube
of ℓ L^K sites at the least-root coupling for every late K, then the Hilbert space reconstructed from S has a
unique vacuum and its Hamiltonian has no spectrum in (0, (2/ℓ) log(2^18/5041)).

Points a reader of the statement must check (they decide whether the theorem says what the lane means).

1. `FixedObservableLimit` puts `∀ g₀ ∈ Ioo 0 δ` outside the witnesses, so ℓ may depend on g₀. That is the
   lane's statement (check 1453 L101: "a fixed 0 < g₀ < δ").
2. The witnesses are existential. The clause is proved for **every** tuple of witnesses (4.5, first theorem),
   so nothing depends on which S the release's proof picked.
3. Vacuity. The implication is true and empty if (M-neutral-all) is false. The Lean theorem does not say the
   hypothesis is consistent. That is the open seed (rows 1353-1367), and no formalization of this chain touches it.
4. The trusted base is the release's: `propext`, `Classical.choice`, `Quot.sound` (row 1455 replays it). The
   new library adds no axiom and no `native_decide`: the numerical steps are the inequalities 2^18 > 5041,
   (3/4)^3 < 1/2 and a few like them, all by `norm_num`.

### 4.6 The same conclusion on the public statement's Hilbert space (second theorem, **sketched**)

For `S : WilsonOS.Family` of `Challenge.lean`, with `Admissible`, `pairing`, `translate` as there (L150-166):

```lean
/-- NEW. Mass gap of a Schwinger family in the vocabulary of `Challenge.lean` alone. -/
def WilsonOS.HasMassGap (S : WilsonOS.Family) (m : ℝ) : Prop :=
  ∀ Φ, WilsonOS.Admissible Φ → ∀ t : ℝ, 0 ≤ t →
    (WilsonOS.pairing S Φ (fun n => WilsonOS.translate (t • Pi.single 3 1) (Φ n))).re
        - ‖∑ᶠ n, S n (Φ n)‖ ^ 2
      ≤ Real.exp (-m * t) * ((WilsonOS.pairing S Φ Φ).re - ‖∑ᶠ n, S n (Φ n)‖ ^ 2)
```

This is <ψ, e^(-tH) ψ> ≤ e^(-mt) ‖ψ‖² for ψ = Φ − <Ω, Φ>Ω, on all admissible flat sequences. It can be read by
a person who knows only `Challenge.lean`. It needs: (a) the identification of the public S with the internal
`centredOf S` on tensors (the release proves it inside `WilsonSubsequence.lean` 14-67); (b) density of tensors
in the flat positive-time tests for the form (check 1450 L35). Proposed as the last stage, because it adds no
mathematics of the gap.

## 5. Lemmas to formalize, in dependency order (item (3) of the row)

Sizes are lines of Lean including proofs. Every size is **guessed**. Calibration, counted from the release:
its `TransferOperators` folder (cubic trace formula, insertions, Peter–Weyl) is 19,568 lines; its
`ReflectionPositiveLimits` (reconstruction of a functional, clustering in time) is 7,535; `HilbertSpaces` 10,362;
`SpectralTheory` 17,051; `InfiniteLattice` 94,933. The hand notes behind the lower half are short: `gap-transfer.md`
279 lines, `gap-transfer-twisted.md` 140 lines. The column "math" says where the hand proof is and who checked it.

### 5.1 Upper half (U): (EC-ν) gives the gap. Soft.

| # | Lemma | Depends on | Size | Math |
|---|---|---|---|---|
| U0 | `Inputs` from any witnesses of `FixedObservableContinuumWith P L M g₀` (β_j > 0 from `IsLeast`; the rest is projection) | release | 60 | none |
| U1 | The form of `centredOf S` is positive and `HasReconstruction` holds, from the `mixture` clause (find the release's theorem from `IsOSPositive T` and `HasSchwingerSequence` to `IsPosSemidef (reflectionForm σ)`, and from `ContractionHypotheses` to `HasReconstruction`) | U0 | 100-400 | release's; **risk R1** below |
| U2 | ν_j is a shift-invariant periodic Gibbs state with link-mirror positivity (`IsInfiniteVolumeLimit` to `periodicGibbsSet`, then `PeriodicGibbsReflectionTransfer`) | U0 | 150 | release's |
| U3 | `latticeU (ν j) Z t` at t = (2n+1) a_j is the n-th reflected moment of one function of `upperAlgebra` (products of centred `smearedEnergy`; reflection of tests against reflection of fields; the mirror at a_j/2 with A shifted up by a_j) | U2 | 400-700 | 3.1 U1, U1'; **sketched** |
| U4 | Sequence lemma: non-negative, log-convex with forward zeros, m_n ≤ C q^n gives m_(n+1) ≤ q m_n | Mathlib | 80 | Lemma A2 of row 668 in scalar form |
| U5 | (R_j) passes to the limit on the dense set {(2r+1) L^(-k)} (L odd), then to all 0 ≤ s ≤ t by continuity of t ↦ ‖timeShift t ψ‖ | U1, U3, U4 | 300 | Lemma DT (row 1449, check 1450) |
| U6 | Density: the bound on ψ = posClass Z − <Ω, Z>Ω extends to the complement of the vacuum; `massGap_of_expClusters` | U5 | 150 | 3.1 U3 |
| U7 | `HasMassGap.uniqueVacuum`; later the spectral forms and `ENat.card A.space = 1` | U6 | 25, later 300 | Lemma E of row 668 |

Total (U): about 1,300 to 2,200 lines.

### 5.2 Lower half (W): (M-neutral-all) gives (EC-ν). Lattice only.

| # | Lemma | Depends on | Size | Math |
|---|---|---|---|---|
| W1 | Lemma M1 in the direction used: `HSNormLE (c⁻¹ • B − ketBra φ) δ`, B ≥ 0 Hilbert–Schmidt, δ < 1 gives (1 − δ²) Tr B² ≤ ‖B‖² | Mathlib | 200 | row 1356 2.1, check 1359. No eigenvector needed for this direction. |
| W2 | Spectral toolkit for a positive trace-class operator on `HaarL2`: eigenvalue family with multiplicity, Tr T^a = Σ λ_i^a, top eigenvalue = ‖T‖, joint eigenvectors with commuting unitary involutions; Lemma A (Tr T^(jb) ≤ (Tr T^b)^j, convexity of a ↦ log Tr T^a); sums of real powers Σ x_i^s | Mathlib; release `tracePW`, `TransferProperties` | 1,200-2,000 | standard; not in Mathlib at this pin (2.3) |
| W3 | Rectangular tori with twists on a direct finite model (sites ZMod N_0 × ... × ZMod N_3, sides ≥ 3): sign fields s^(e,m), Z^(e,m); independence of the place of the stacks; Z^(σk)(σn) = Z^k(n) for the 24 permutations | Mathlib; release Haar on SU(2) | 1,500-2,500 | `gap-transfer-twisted.md` 1.4, 3.5 (row 1004, check 1008) |
| W4 | (TM-tw): T_(B,m) = P M_m C_E M_m P on the box B, positive, trace class, strictly positive kernel; C^e commute with it; Z^(e+m)(a, B) = Tr(T_(B,m)^a C^e) for every a ≥ 3 and every one of the four directions as time; (F1), (S1)-(S3) | W2, W3; release `sqrtLinkOperator`, `linkProductKernel`, `kernelOp`, `TwistedActionOperators` (all generic in the finite link set) | 5,000-9,000 | Theorem TW-T (row 1004, check 1008); `gap-flux-exercise.md` 3.1 C2 |
| W5 | Abstract Theorem S: for a symmetric positive W(a, b) = Tr T_b^a, Lemmas K, X, E, E', Theorem S, Corollary S3' | W2 (Lemma A only) | 600-1,000 | `gap-crux-restate.md` 3.4 (row 697; checks 698, 699). No gauge theory. |
| W6 | Finite algebra on Z_2^6: the three sector sets (Proposition CL (b)), the Pfaffian weight, Lemma W, Theorem S-w, Corollary EV | W4, W5 | 500-900 | `gap-flux-exercise.md` 8.3-8.4 (row 731, check 732). Facts on 64 elements by kernel `decide`. |
| W7 | Explicit finite-aspect theorem, K = 512: on a cube with 4 ∣ n, n ≥ 2^70, s(u) ≤ 1/2 for some 3 ≤ u ≤ n/512 gives S_κ(n/2; n³) < 2^(-18) | W2, W4, W6 | 1,500-3,000 | `gap-solve9-astra62.md` L213-227 with its (3), (4), (5), (8), (9) (row 1161, check 1162) |
| W8 | Corollary M2 and Theorem BP (i): the rank-one test gives s(2w) ≤ 4/21, then s(u) ≤ 1/2 at u = max(3, 2w) ≤ n/512, then the κ-seed with N = n/2; the release's T against the lane's T (4.1 point 5); independence of the plane (4.1 point 4) | W1, W2, W7 | 400 | row 1356 2.2; row 1179 Section 6; check 1450 L56 |
| W9 | Torus expectations of slab functions as traces with an inserted operator k_F; the cylinder state; Lemma T and Theorem L1 of (L); Lemma CB, MX, L1-ev; Theorem EV-L (c), (d) for bounded continuous centre-blind local functions; axis exchange of the periodic state | W2, W4 | 3,000-5,000 | `gap-transfer.md` Section 8, `gap-seed-limit.md` (row 700; checks 703, 723), `gap-flux-exercise.md` 8.2 (check 732) |
| W10 | Bridge to the release: its tori of side 2 L^(m+K) at spacing L^(-K) (`PeriodicLattice.wilsonGibbsMeasure`, `liftedWilsonMeasure`) against the finite model at spacing 1; centred smeared energies are bounded continuous centre-blind local functions; weak limits keep the clustering bound; lattice steps to physical time | W9; release | 1,000-2,000 | check 1450 L27-36 (with the Borel step dropped: 3.1) |
| W11 | Proposition P-ev (a), (b) with the constants (5041, 71, 2^(-18), M_* = (2/ℓ) log(2^18/5041)); `expClusters_of_mNeutral` | W6, W8, W9, W10 | 300 | row 1179 5.2; check 1450 L56-62 |

Total (W): about 15,000 to 26,000 lines. Whole chain: about 16,000 to 28,000 lines, of the order of 5 to 8
percent of the release's `YangMills/Construction` tree as sampled above. **guessed**.

### 5.3 The hardest step

**W7, the explicit finite-aspect theorem, is the hardest step.** Reasons.

1. It is the only node whose hand proof is a long chain of numerical inequalities (2^(-169), 160 h, 2^(-59),
   2^(-47), 2^(-19)) inside one file of the solve chain, with one check (1162). Every other node of (W) is a
   structural statement checked twice or more.
2. It reads all 64 twists in more than one time frame at once (misaligned coefficients "in that frame"), so it
   needs W3 and W4 complete in all four directions, with the crossing of twisted traces.
3. It differentiates spectral sums in a real exponent (sums of x^s for s in [1/2, 3/2], bounds on −x log x). So it
   needs eigenvalue families with multiplicity (W2 in full), not only traces of integer powers.
4. If a formalization finds a real gap anywhere in the chain, this is the most likely place. A found gap would be
   a result about the lane's chain, not only about its Lean form.

**W4 is the largest step**, and the place where the release helps most. Its Haar, Peter–Weyl, kernel-operator
and trace machinery is generic in the finite set of links (2.1). Its layer decomposition and trace formula are
stated for cubic tori of the infinite-lattice quotient formalism and cannot be reused as statements. The proofs
(`CycleOfKernelsIsATraceProof.lean` 391 lines, `ExactEliminationOfAnOutermostLayerProof.lean` 544 lines,
`ConfigurationsOfACubicTorusByLayersProof.lean` 269 lines) are the template.

Risks of the design itself (each one is **guessed** until a build row tests it).

- **R1.** The exported `mixture` clause may not give `HasReconstruction (centredOf S)` by a theorem of the release
  that is public. Inside their proof it is available (`hAss.limit.conditions.reconstruction`, 2.6), but the step
  before it is `private`. Fallback: put `ReconstructionConditions (centredOf S)` into `Inputs` as a field, and
  supply it by re-proving the last two theorems of the release with one more conjunct in a new file (about 200
  lines that follow their proof text line by line; a question of credit and licence for the lead; the release's
  README shows no licence line in a grep for `licen`).
- **R2.** The mirror bookkeeping of U3 (U1' of 3.1): site reflection of tests, link-mirror positivity of states.
- **R3.** `Inputs.moments` is stated for `SepTupleOfCard n`, which are C¹ compactly supported separated tuples.
  The tuples θX_k ++ τ_t X_l must be shown to be of this type, uniformly in the bookkeeping of `PositiveSpan`.
- **R4.** The two torus formalisms (2.4). W10 may cost more than estimated.
- **R5.** `HSNormLE` against `IsHilbertSchmidtPW`: W1 needs the trace of B² in the Peter–Weyl basis, hence
  completeness of `peterWeylVec`. If the release does not state it, it is Peter–Weyl for SU(2)^J (about 500
  lines more, or a route through `Schatten.kernelOp` kernels: ‖B‖²_HS = ∫∫ |kernel|²).

## 6. What can be stated and checked first (item (4) of the row)

Order chosen so that each stage ends in a kernel-checked artefact that stands alone, and so that the cheap
stages test the risky interfaces before the expensive ones start.

**Stage 0. The statement file, with `sorry` in the proofs only.** Sections 4.1-4.5 in one file `GapChain/Statement.lean`
(about 150 lines), compiled against the release. Definitions carry no `sorry` except `latticeU` (which must be
written out in this stage) and the two-line membership proof of `centreElt`. Decisive content: the statement
type-checks against their declarations, and `#print axioms` on `su2_fixed_observable_gap_of_mNeutral` shows
`sorryAx` plus the release's three axioms and nothing else. This stage settles R3 and half of R1 (whether the
needed names are public). It needs the replay build of row 1455 to be finished, because Lean must load the
release's `.olean` files. It is the place for the faithfulness reading: the points of 4.1, 4.3 and 4.5 are a
checklist for the cross-provider reader.

**Stage 1. Three small closed pieces, independent of each other.**
- U4 (sequence lemma), Mathlib only, about 80 lines.
- W1 (Lemma M1, one direction), Mathlib only, about 200 lines.
- W5 (abstract Theorem S with Lemmas K, X, E, E', S3'), Mathlib only once Lemma A is taken as a hypothesis on
  W (submultiplicative and log-convex in each argument), about 600-1,000 lines. This is the lane's main
  theorem of row 697 in kernel-checked form, with the constant 5041. It is also the piece of the chain that a
  reader outside the lane can check most easily.

**Stage 2. The upper half (U) complete: `massGap_of_expClusters` with no `sorry`.** About 1,300-2,200 lines.
Result: a kernel-checked theorem on the release's own objects, "if the infinite-volume lattice states of the
construction cluster exponentially in time at one physical rate on the tr F² observables, the continuum limit
has a unique vacuum and a mass gap at that rate". It is the standard criterion, and to my reading of rows 1449
and 1453 the release does not contain it (no statement with a rate, 2.5). It settles R1 and R2. After it, the
gap of the Lean continuum theory is reduced in Lean, not only by hand, to one lattice statement (EC-ν).

**Stage 3. The lower half in the order W2, W3, W4, W6, W9, W10, W11 with the κ-seed as hypothesis.**
Intermediate theorem: `expClusters_of_kappaSeed` (hypothesis S_κ(n/2; n³) < 2^(-18) on the cubes n = ℓ L^K_j). It
leaves out W1, W7, W8.

**Stage 4. W7 and W8.** The theorem of 4.5 with no `sorry`.

**Stage 5.** The spectral corollaries of U7 and the `Challenge.lean` form of 4.6.

What not to do first: W7. It is the hardest and needs nearly all of the rest.

## 7. Open points, and what this note does not show

- Nothing here was compiled. Every Lean block is a design. Names of the release are quoted from files I
  opened; types of composite expressions (coercions `ℕ+ → ℕ → ℤ`, `PositiveSpan` internals, the exact form of
  `TimeAxis.timeIdx`) are not verified.
- The shorter route of 3.1 (link mirrors and log-convexity instead of the site-mirror datum, Statement (3) and
  Lemma FE) is my proposal. It is **sketched**, by me only, and checked by no one. If it fails at U3, the fallback
  is the chain as on file (add Lemma FE, Lemma RPc, Theorem L3-ev and Statements (1), (3), (5): about 3,000 to
  4,000 lines more, **guessed**).
- The sizes are guesses with the stated calibration. I did not measure how long any piece takes to write or build.
- I read the lane's lattice statements (Theorem S, S-w, EV-L, TW-T 1.1-1.4, the explicit finite-aspect theorem) for
  their structure. I did not re-check their proofs.
- The seed (M-neutral-all) stays open. A complete formalization of this chain proves an implication only.
- Row 1455 (replay) was running while I read. I read source files only. I did not touch the build.
