## **Searches run.**

- Initial terms: `trace obstruction`, `character obstruction`, `quantum.link`, `D-theory`, `growing register`, `cube.face`, `odd coarse`.
- Follow-ups: `register`, `Clifford`, `Kogut`, `Spin(10)`, `Peter.Weyl`, `strong.coupling`, `electric.dominated`, `K-INV`, `end.pure`, `no Clifford node`, `odd.*flat`, `site.bilinear Spin`.
- Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`. Reads included consolidated notes, ledger rows, frozen parts, prior digests, referee reports, and `LIT_QLM.md`.
- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and says each consolidation PR “has a *CONSOLIDATED* note” (`ref/README.md:2–3`).

Path abbreviations below:

- `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`
- `D` = `ref/main/docs`
- `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030`
- `C` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`

LW2 covers feature mapping and growing registers. The magnetic-layer construction is assigned separately to LW2M: “LW2 (items 1 and 2) and LW2M (item 3)” (`T/TOE_ASSEMBLY.md:323`).

## **Already in the repo.**

- **Register size does not select the gauge group.** Consolidated #9882 states “per-site register size selects no gauge group.” Its Fock-register result assumes the split, chirality reading, and normal ordering (`C:55`). Consolidated #10027 excludes a finite-site composite 16 under site-bilinear Spin(10): “every parity-odd excitation is vector class, never the 16” (`C:23`). Status: “author statements for review” (`C:11`).

- **The trace obstruction depends on exact Gauss identification.** ZM1I1A Theorem 3 forces `L=1` under locality, singleton representatives, and `(G1)` (`T/ZM1I1A.md:44`, “no specified map for `L≥2`”). The file identifies the load-bearing requirement as “the exact generator identity (G1), together with locality and the fixed-form coarse algebra” (`:50`). Status: frozen author-side arguments, “not independent audit findings” (`:3`).

- **The current invariant-only zoom already changes that interface.** The owner’s replacement says “Impose no map on charged fields or Gauss generators” (`T/TOE_ASSEMBLY.md:252`). ZM1INV records why full-matrix trace transfer cannot simply be reused: the invariant algebra “has at least two tracial states,” and the old argument “cannot be applied directly” (`T/ZM1INV.md:84,92`). Its target remains open (`:5`, “neither construct the requested zoom nor prove it impossible”).

- **Characters obstruct the specified global readouts.** Every named `L5-U[m]`, `1≤m≤9`, and `L5-O[S_+]` invariant algebra has a character (`T/GB1Z2L5.md:7`, “full invariant algebra … has a character”). Theorem 4 excludes a unital map from a characterless source into either target (`:59`, “no unital *-homomorphism”). This includes the stated Z₂ source and specified finite abelian analogues. Status: frozen; “no retained or audit status” (`:5`).

- **The character result has explicit qualifications.** Spin-S U(1) quantum-link invariant algebras also have characters, so “the character obstruction alone does not decide its readout” (`T/GB1Z2L5.md:85`). U-law invariant algebras contain nonzero matrix corners (`:89`, “a non-unital embedding of M₂”). Changing to a sector quotient remains open except under the stated character-survival condition (`:117–121`, “GB1-Z2[L5,SEC] remains open”).

- **K-INV excludes odd coarse occupancy under specified lifts.** For odd `m₁`, even-`m` U or O fine laws admit no unital invariant map intertwining the end-exchanging rotation (`T/KINV.md:37`, “Injectivity and locality are not assumed”). Even coarse occupancy remains a separate question: the constant character map is “not injective” (`:53`). A local injective map cannot complete a good sector by a character filler (`:59–63`, “no character `χ` satisfies”). Status: frozen (`:5`, “FINISH: FROZEN”).

- **Exact continuous-group Wilson links already fail at finite dimension.** GA2 Corollary 2.2 states that a finite register with nontrivial infinitesimal covariance has “no invertible covariant link” (`T/GA2_Y2.md:43`). The finite-image exception is explicit: `L²(K)` carries an “entrywise-commuting unitary link” when `K=ρ(G)` is finite (`:49`). These statements distinguish exact link identities from approximate correlator comparisons.

- **A growing SU(2) family and quantitative comparison already exist.** GB1QL defines `R_s=⊕_{k≤s}H_k` with finite dimension `(s+1)(s+2)(2s+3)/6` (`T/GB1QL.md:53`). Proposition 4.11 supplies gauge invariance, cell covariance, and “Finite depth under NN-a” for `L5[SU(2),s]` (`:299`). Empty-matter correlators approach the cube-face Trotterized Kogut–Susskind model at `O((log s)⁴/s²)` for bounded flux and `O(s^{-2/3})` for bounded local electric energy (`:303`). The comparison is uniform in ambient volume and `n≤T`, with fixed support and stated state bounds. Status: frozen, proposed test laws; “not either named working-set law” (`:5–7`).

- **GB1E already supplies the finite-box Euclidean limit.** Its target lifts are gauge-invariant Haar-density probabilities with coordinate link-reflection positivity (`T/GB1E.md:9`, “Both have coordinate link-reflection positivity”). Theorem 8.3 gives trace-norm convergence of embedded finite-register Gibbs operators (`:198–202`, “longrightarrow0”). The limit is “fixed-box, fixed `a₀,N_t`, then `s→∞`”; it supplies no volume-uniform Euclidean estimate (`:206`). Status: frozen (`:5`).

- **The finite-register positivity negative is representation-specific.** The embedded group-variable kernel has negative real part for sufficiently small Euclidean steps (`T/GB1E.md:186`, “negative on a nonempty open set”). The file expressly says this “does not prove that every gauge-invariant measure requires an infinite register” (`:196`). This qualification belongs in LW2-MAP.

- **One-tiling factorization and the FP proposal are already frozen inputs.** GB1ISO records that the cube-face tick and both transfers “factor over disjoint link cubes” (`T/GB1ISO.md:7`). Under its shrinking-support, state, convergence, and invariance hypotheses, the reconstructed Hilbert space is `CΩ`, so NT1 fails (`:148`, “Then the reconstructed Hilbert space is …”). FP counts every spatial plaquette twice and gives the full sum on the infinite-register target (`:161`, “all `B_C` commute”). At finite register, covariance and the exact full-sum identity remain unproved; “Neither pass made an NN-a check of FP” (`:165`). Status: frozen conditional results (`:5`).

- **Odd-band and Clifford exclusions use additional structure.** LZ1’s finite-pattern odd bands are flat near nodes (`T/LZ1.md:64`, “every odd light species … is flat”). RCSPC excludes Clifford nodes for its rigid-label representations (`T/RCSPC.md:67`, “every orbit … stabilizer … rank at most 2”). RCSPO’s finite-range-background theorem requires positive empty-level weight in every transverse residue class and factor ray sectors (`T/RCSPO.md:87`, “then no representation built from these factor ray sectors has a Clifford node”). Their open classes remain explicit (`T/RCSPC.md:276`, “not claimed to be true or false”; `T/RCSPO.md:13`, “outside the proved classes”).

- **The four 16 routes already separate different law changes.** Non-Bogoliubov embeddings still have the specified physical-sector exclusion (`T/CG16B.md:84–92`, “target (T) has no instance”). Link-pure spinor sectors are node-flat (`T/CG16D.md:59–65`, “every `N_j=0`”). End-mixed point registers permit a local transfer, while the fully covariant moving law remains open (`T/CG16S.md:46,58`, “Whether a finite-depth NN-a law … moves sites is open”). K-27 supplies exact block-scale frame actions, while “The 16 question is unchanged by (K)” (`T/LW1_5.md:11`). These are frozen conditional routes, not a universal exclusion of revised laws (`T/CG16S.md:11`, “Neither a chiral 16 nor a universal exclusion … is established”).

- **A moving string band already prevents equating all motion with a Clifford cone.** RCSP16 constructs `V(K)=e^{iK₁}` on the U(16)-rishon witness (`T/RCSP16.md:80`, “node set is `K₁=0`”). It is longitudinal propagation; “No one-dimensional band has a three-dimensional Clifford cone with positive speed” (`:86`). Status: frozen, with no adopted law or vacuum (`:5`).

- **GA1-5 already has a neutral propagating band.** Theorem 6.3 constructs `V(K)=e^{-iK·(1,1,1)}` for even `m` under NN-a (`T/GA1_5.md:166–170`, “generated by neutral link operators”). Proposition S-odd extends the construction to every `1≤m≤9` using an oriented sector and rotation averaging (`:180`, “same band”). Its limitation is explicit: “The one-way band is not a Clifford cone” (`:182`). Status: frozen, with identified unrefereed closures (`:5,11`).

- **SGAP0 supplies a zero-hop charged gap, not a growing gauge-register theorem.** In the finite-ring model, at `t=0`, Theorem 9 gives `E_σ≥E₀+7τ` for `|ε|≤2·10^{-10}τ` (`T/SGAP0.md:150–152`). Its scope is conditional on the frozen atom and Gauss reduction (`:3`). “Infinite-volume, GNS and tick statements are not established” (`:165`).

- **Main already contains a volume-uniform cutoff template.** The supplied SU(3) local-observable theorem combines spatial locality and complete Peter–Weyl truncation, “independent of total lattice size” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). It prices local energy and preparation probability (`:73`, “explicit resource premise”). Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

- **Main also contains cutoff-uniform strong-coupling gap support.** The supplied compact SU(3) theorem gives gap at least `2/a`, uniform in volume and every full Peter–Weyl cutoff `R≥1`, in its small-`av` regime (`D/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:26`, “uniform in volume and, separately, … cutoff”). Its constants are unspecified and its lattice is fixed. Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07.json:31`).

- **Fixed finite internal structure has native examples.** The U(1) matter–magnetic join uses four spin-one links and a charged hop on one face (`D/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md:38–39`, “`3^4 x 2 = 162` dimensional block”). Its palindromic tick has `O(h³)` one-step error (`:63`). Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/u1/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_bounded_theorem_note_2026-09-03.json:34`). The nearby MDTN truncation is “proposed (unaudited)” and leaves the BHM gap step an “open obligation” (`ref/pr10135/docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:14,31–32`).

## **Failed attempts on file.**

- **Growing the existing `L5-U[m]` register internally.** GB1QL’s step U2 fails because the law has one fixed register; the SU(2) block dimension is at most six (`T/GB1QL.md:310`, “A family of block registers whose size grows, inside the law. … Fails”).

- **Removing the flux restriction.** The top-flux state gives an operator-norm discrepancy at least one (`T/GA2_Y2.md:47`, “no rescaling … converges in operator norm”). GB1QL therefore fixes support, time, and flux before growing `s` (`T/GB1QL.md:259`, “the flux bound cannot be dropped”).

- **Repairing a global character obstruction by selecting states.** This leaves the target algebra unchanged (`T/GB1Z2L5.md:63`, “Restricting the class of states does not change the target algebra”). Completing the good-path sector by a character fails separately at the local filler condition (`T/KINV.md:77`, “fails at Theorem 5”).

- **Treating the finite-register embedded Gibbs kernel as a probability.** The small-step kernel has negative real part (`T/GB1E.md:186`, “negative on a nonempty open set”). Wrapping the infinite electric generator instead produces a bounded generator with a partition obstruction (`:103,107`, “infinite partition integral”; “Theorem 5.1 applies”).

- **Transferring FP counting directly to finite registers.** The failing step is commutation: “shared-link plaquette operators need not commute” (`T/GB1ISO.md:165`). The infinite-register exponential identity does not finish finite-register scheduling or covariance.

- **Obtaining ISO-FP from existing restoration arguments.** Axis reflection positivity does not supply RO1’s diagonal mirrors; tree-level matching gives no nonperturbative rate; the Ward route lacks anisotropy decay (`T/GB1ISO.md:167`, “These failures do not prove impossibility”).

- **Extending the no-Clifford result to arbitrary backgrounds.** RCSPC records three failed steps: general-state decoupling lacks the required factorization (`T/RCSPC.md:214`, “no clustering statement separates `X` from `Z_s`”); asymptotic flux lacks control of the weighted background (`:216`, “`ν_x` itself is not controlled”); stacking lacks composable sectors (`:218`, “straight-string limit sectors carry no composition law”).

- **Using D-theory reduction directly in the present dimension.** The repository literature record says reduction of three spatial directions plus time “would leave three Euclidean dimensions” (`T/LIT_QLM.md:15`). The many-flavour parameter also differs from occupancy and blocking: “neither the repo’s occupancy m nor a ZM1 block size” (`:45`).

## **Overlap with this lane's results.**

not run

LW2 is recorded as “Open,” with its pass-1 work following the prior-work digest (`T/TOE_ASSEMBLY.md:323`).

## **Missed inputs.**

- **Start LW2-G from the existing `L5[SU(2),s]` test family.** It already supplies finite-register NN-a compilation and finite-time regulator rates (`T/GB1QL.md:299,303`, “Finite depth under NN-a”; “uniformly in the volume”). This changes the task from inventing the SU(2) family to checking which other frozen statements transfer to it.

- **Use the tensor-copy alternative as a separate family.** GA2 computes coherence `k/(k+5)` and a defect floor `2/(5k+1)²` for `(Λ⁵C¹⁰)^{⊗k}` (`T/GA2_Y2.md:105`). It labels this “not an adopted change of law” and withholds a phase or continuum conclusion (`:105–107`, “not a proof of a classical phase”). This supplies quantitative kinematics for a candidate family, with dynamics still to check.

- **Keep algebra changes distinct from state changes.** Matrix corners and sector quotients provide different escape questions from a full-unit readout (`T/GB1Z2L5.md:89,121`, “non-unital embedding”; “remains open”). They change which map LW2 must construct; excluding a vacuum witness alone does not change the global algebra (`:63`).

- **Use the existing uniform-gap theorem as a comparison template.** Its imported constants depend on interaction range, “not on local dimension or an onsite upper spectral bound” (`D/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:135`). This identifies a route for proving register-uniform stability under checked hypotheses. It does not transfer SGAP0’s finite-ring gap automatically.

- **Preserve the finite-register and D-theory qualifications.** GB1E excludes only particular kernels (`T/GB1E.md:196`, “nor exclude other representations”). The literature record supplies no uniform large-representation remainder (`T/LIT_QLM.md:33`, “does not provide uniform remainder bounds”). These inputs prevent replacing a scoped negative or semiclassical proposal with a general law classification.

## **Consumers.**

- **LW2M / GB1-CF / ISO-FP.** Need an admissible finite-register cube-coupling update, its NN-a certification, and the actual finite-register comparison. Infinite-register FP counting is already available; “Neither pass made an NN-a check of FP” (`T/GB1ISO.md:165`). ISO-FP then needs a nontrivial rescaled-isotropic correlation limit with a rate (`:167`, “at rate `O((a/r)^p)`”).

- **W1 / GB1 / GA2.** Need a named regulator family and controlled gauge-invariant observable comparison. The assembly names LW2’s service as “the register limit and isotropy” (`T/TOE_ASSEMBLY.md:759`). Finite-time empty-matter convergence supplies the regulator component; the missing measure and RG admission remain separate (`T/GB1QL.md:17`, “(H-4D) first”).

- **W3 / CN1 / ZM1-INV.** Need an injective, cell-covariant, exponentially local invariant-algebra map and its stated `p=2` comparison, without a charged-field map (`T/TOE_ASSEMBLY.md:252`, “Impose no map on charged fields or Gauss generators”). Odd-coarse K-INV exclusions and even-coarse obligations must remain separate (`T/KINV.md:41`, “some even `m₁∈{2,4,6,8}`”).

- **MT1 / CG1 / W2.** Need an identified propagating spinor sector and, eventually, chiral light content. The current moving string witness is insufficient for the cone target (`T/RCSP16.md:86`, “not a Clifford cone”). The W2 target requires “one Weyl 16 … with every mirror and doubler gapped” (`T/TOE_ASSEMBLY.md:749`).

- **YM T0-start / T0-rate.** Need gauge-invariant reflection-positive starts in a pinned RG class, plus scale-uniform source and volume estimates (`T/GA2_Y2.md:178`, “class and topology must be pinned”). The YM interface requires CT1–CT4 with “All constants … independent of a and L” (`Y/GOAL.md:70–73`). A fixed-box lift or finite-time real-time comparison supplies only part of that interface.

- **Assembly coherence AS0.** Ultimately needs the transferred positives and escaped negatives on one law and one vacuum. The assembly explicitly requires “one law `L` … one zoom … and one vacuum” (`T/TOE_ASSEMBLY.md:718`). Results on separate supplied models remain inputs to that obligation.