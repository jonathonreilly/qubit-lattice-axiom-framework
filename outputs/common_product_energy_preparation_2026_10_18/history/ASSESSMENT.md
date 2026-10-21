# Blank-head supply: bounded next-opportunity assessment

Status: opportunity assessment with provisional analytical calculations, requiring a distinct check before theorem use. No preparation mechanism or publication is asserted. The useful next target is an energy-to-blankness interface for this finite apparatus, not a claim that its autonomous evolution initializes itself.

## Recommendation and decisive distinction

The proposed uniform positive head penalty is a viable, narrowly scoped next calculation. The actual positive-block inventory gives a linear all-head lower bound directly, without a many-body diagonalization. The current incident-cap reserve can accommodate a constant penalty without rescaling the router. This offers an explicit energy or conditional Gibbs-state criterion for approximately blank heads, with a logarithmic volume cost in inverse temperature. It does not remove the physical supply premise by itself: obtaining such a state, preparing blank R, and coherently loading the ordinary program/path input remain separate operations or assumptions.

The highest-leverage next calculation is therefore one checked finite-volume **energy-certified blank-head interface**, including an explicit input-loading channel premise and its error budget. The thermal specialization should be subordinate to that interface. A proof of a gap alone should not be described as initialization.

## Actual all-head accounting

Write the nominal finite Hamiltonian H=cI+K as in the checked matrix-robustness inventory. The only negative remainders after subtracting the vacuum scalar are vacancy terms:

    K = sum_(nonvacancy l) h_l - sum_v d_v n_v,
    c = 8b+8(sqrt(2)-1)j.

All h_l in the first sum are positive on their complete supports, including double-head occupation, arbitrary P, and arbitrary R. They include signed positive writer bonds, controlled mediator occupations, positive terminal-record blocks, source blocks and caps. They need not commute. Thus their sum can be discarded in a lower operator bound on the full finite Hilbert space.

There are two b vacancies at each of the four core endpoints, so d_v=2b there. Each writer has four distinct junction vertices, each with one (sqrt(2)-1)j vacancy; the two writers' junctions are distinct and do not coincide with core endpoints. All other d_v vanish. Since j<=b/8, max_v d_v=2b. With N_head=sum_v n_v,

    K >= -2b N_head.                                      (A)

This is an operator inequality in all head-number sectors, not the one-head norm estimate from robustness. No free-fermion spectrum, dilute approximation, P-sector selection or chosen record eigenvalue is involved. A weaker bound using the total vacancy scalar would also exist, but the actual occupancy accounting supplies the stronger constant 2b. Positivity of H alone would only give K>=-cI and would not by itself supply the advertised linear bound.

Every listed block conserves total head number. Add positive onsite blocks mu n_v at EVERY head, including emitters, mediators, all internal heads and output caps, with a common mu>2b. Then

    H_mu=H+mu N_head,
    [H,N_head]=0,
    H_mu-cI >= g N_head,  g=mu-2b>0.                     (B)

The all-head vacuum has energy exactly c on every P/R fiber state. It is therefore the complete ground sector, separated from its complement by at least g. It is not a unique ground vector: P and R give a four-dimensional ground space. The occupation basis, coefficients and absence of extra interactions remain supplied. Omitting the penalty from selected head sites would lose both the simple uniform phase and this global bound; excluding the emitters to favor a loaded source is a different problem.

The one-head evolution satisfies the exact identity

    exp(-it H_mu)|_(N_head=1)=exp(-i mu t)exp(-itH)|_(N_head=1).

Hence the normalized complete-output target and the SAME entire-horizon unnormalized flag target must both acquire exp(-i mu t). Relative program/path phases, the -i scattering phase, radial shift 57, window, packet and all reference contracts are otherwise unchanged. Vacuum-versus-one-head coherences would acquire a relative phase; the existing logical input has exactly one head, so no such sector coherence is imported. This is an explicit phase adjustment, not the original fixed-phase target unchanged.

## Cap, inventory and resource implications

For the nominal accepted single-control family, D1=Lambda/8, b<Lambda/128, j<Lambda/1024. Choose the simple constant mu=Lambda/4. The largest nominal head load is D1+2b<9Lambda/64. Adding one norm-mu onsite term gives every head a load below 25Lambda/64. The program load remains below Lambda/2, and the record load remains 8j. Thus the full physical incident cap stays below Lambda without rescaling H or changing the existing operation duration. The lower gap is

    g=Lambda/4-2b > 15Lambda/64.

If a different starting apparatus used the cap tightly, a uniform rescaling H->sH would instead require accounting for s times every original coefficient and operation time t->t/s, and the lower gap would become mu-2sb. That fallback is unnecessary for this nominal recipe. It is NOT automatic that the same mu can be added at the extreme of the already perturbed robustness cap: that combination would require fresh cap and all-head lower-bound accounting. The pending vacuum-only robustness extension is not used here.

There are m=124+4ell head qubits, excluding the one P and one R. Keeping new onsite terms separately listed adds m positive blocks, no qubits or interaction edges. The resulting counts would be 126+4ell qubits and 288+8ell blocks. They retain the existing asymptotic size order. Uniform mu is a new supplied coefficient/occupation coupling; its exact uniformity is what gives the common-phase identity. Spatial errors in that coefficient require their own budget rather than being silently calibrated away.

In the nominal logarithmic family ell=Theta(epsilon^(-11/2)) and the operation duration is Theta(Lambda^-1 epsilon^(-15/2)). Adding this exact penalty changes neither order. It is not an efficiency claim: the independent cost of obtaining the initial low-energy state is still unquantified.

## What low energy or an assumed thermal state would certify

For any state omega on all heads and fibers, including reference entanglement, define the supplied energy excess E_ex=Tr[(H_mu-cI)omega]. Inequality (B) implies

    Pr_omega(N_head>=1) <= Tr(N_head omega) <= E_ex/g.     (C)

Thus low energy relative to c certifies approximate blank HEADS. It does not certify a chosen state of P or R, nor their independence from an external reference. If q is the nonvacuum probability, projection onto vacuum followed by normalization gives a nearby vacuum/fiber/reference state with unhalved trace distance at most 2sqrt(q), by purification and contractivity. This is a mathematical comparison; it is not permission to postselect or a supplied measurement. A physical loading operation would have to preserve the desired input and map the chosen ideal blank state to the exact seed. Applying the same channel to actual and ideal states would then contract their distance. That channel and its locality/time/cost must be explicit before composing a new preparation theorem.

For a separate, explicitly assumed full finite Gibbs state exp(-beta H_mu)/Z, the number of n-head basis states is 4 binomial(m,n). The factor four is the unrestricted P/R fiber. Head-number conservation and (B) bound every n-head energy above c by gn, so

    Z_exc / exp(-beta c) <= 4[(1+exp(-beta g))^m-1],
    Z_vac / exp(-beta c) = 4,
    q_Gibbs <= 1-(1+exp(-beta g))^(-m)
             <= m exp(-beta g).                         (D)

This uses eigenvalue bounds and sector dimensions; no noncommutative operator-monotonicity claim for exponentials is needed. A sufficient condition for q_Gibbs<=q_target is beta g>=log(m/q_target). At this constant lower gap and with q_target polynomially small in epsilon, the sufficient inverse-temperature order is Lambda^-1 log(1/epsilon), not a cooling-time bound. At fixed beta and increasing apparatus volume, this estimate does not maintain a fixed small global error. The volume factor is physically relevant to this sufficient contract.

The Gibbs vacuum block is exactly |vac><vac| tensor I_(P,R)/4. Its normalized P/R state does not prepare either an arbitrary coherent program or blank R; in particular recordblank probability there is 1/2. A bath or reset operation that selects R=0 would be another premise. Keeping unknown input coherence while thermalizing the apparatus is also not justified by the unrestricted Gibbs calculation. One can instead hold the logical input externally and specify a later loading interface, but that changes the preparation specification and must be paid for.

No thermal bath, Gibbs equilibration, detailed-balance dynamics, relaxation rate, heat-removal resource, measurement or entropy sink has been constructed. The closed Hamiltonian itself cannot cool an initially occupied head sector into vacuum: it exactly conserves N_head. This is a limitation of this particular proposed evolution, not a no-go for supplied open-system preparation or additional apparatus. The operating one-head seed is an excitation above the blank ground sector and still has to be injected coherently.

## Novelty at the pinned scope and comparison of next routes

The accepted note explicitly leaves blank heads, blank R and input supply open. The single-control source's all-head intertwining and the robustness source's full-support positivity supply useful premises, but neither presents the uniform head-penalty/Gibbs-volume contract above. Within the pinned current scope I found no equivalent established result. This is not an exhaustive claim over historical work, literature or uninspected files. A bounded top-level filename inventory and targeted local reads were used; a first broad inventory included irrelevant copied validation trees and was truncated, so it is not evidence of completeness. No remote search was needed for this finite-matrix assessment.

Compared with finite capture/reuse, this route has a short decisive algebraic step and preserves exact operational dynamics. Capture/reuse still requires handling returning heads, record restoration, correlations and repeated operation, none of which a vacuum penalty accomplishes. In fact N_head conservation prevents the penalty from removing a returned head. Compared with native coefficient supply, this route adds another supplied onsite term and thus does not reduce the Hamiltonian-installation gap. Native supply is more foundational but much less constrained by the current finite device's checked mathematics.

Recommend the energy-certified blank-head interface as the next bounded calculation because it can replace an exact vacancy-state premise with a quantitative energy premise without pretending to supply a bath. Its deliverable should independently check (A)--(D), exact counts/cap/common phase, and a precisely stated assumed loading-channel transfer for arbitrary logical/reference inputs. It should distinguish the general O(sqrt(q)) trace error from the improved O(q) available for a specified block-diagonal thermal mixture, and reserve an explicit preparation allowance alongside the current dynamical error. The key remaining decision is what physical preparation/energy-certification and input-loading operation is allowed. Until specified, the result is an energetic certificate conditional on state supply, not autonomous initialization.

## Exact sources and exposure

N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- Accepted nominal integration: `common_product_single_control_publication/NOTE.md`, `02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde`, fully read in the immediately preceding coherent task and refreshed unchanged here. Parent identifies its accepted publication as 9712; no remote publication/Git check was performed.
- Single-control source: `common_product_single_control_router/PROPOSAL.md`, `76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01`, fully reread here; earlier distinct check `549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0` is reused at its scope.
- Logarithmic policy `7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8`, earlier check `d1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3`, unchanged evidence reused for nominal resource orders only.
- Matrix robustness `common_product_local_matrix_robustness/PROPOSAL.md`, `f9e427ccd5ec0a25f0c28639f9707728489a7a7dcca139e6f9fe03289d9b8a20`, and my preceding full review `3d7be49f11dadbae49ed7c84a29e2a32ae8d38a83c1552a630716cc54c554b39`. Scalar precursor `3218676f11bbc39ecfcf3c84a568a2ffc8107a7b303f349195394a338b2b0623` has supplied check `0995e9e58fc7aa93fe27a3892e9615be7f3fd72fb6c989709dcb0a84105549e1`. Their all-support inventories are reused; no pending extension is presumed.
- Staged record core `c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729`, refreshed unchanged; vacancy geometry/scalar paragraphs were specifically reinspected. Earlier complete read and my review `61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1` remain the component evidence.
- Earlier opportunity assessment `next_physical_supply_opportunities/ASSESSMENT.md`, `d1c58b809dd37ff1e784f271eb2ded3df3644209879a0beca36a8c167d62ac59`, was consulted selectively for prior supply scope, not treated as a complete historical search.

ROOT proposed the chemical-potential route and requested this assessment. I have authored earlier components and checked several reused sources. This is exposed continuation at the same model/effort, not an independent review of the new provisional calculations. The physics-claim-reviewer discipline was used to separate energetic conclusions from state preparation. Only this assessment was created. No W, Git, checkpoint, source, editable prompt, axiom or model setting was changed; there was no delegation, publication, remote search or scientific executable.
