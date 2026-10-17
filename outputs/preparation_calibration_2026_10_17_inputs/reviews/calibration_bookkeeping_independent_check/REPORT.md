# Selective independent check of calibration publication bookkeeping

## Finding and source boundary

The newly explicit full-space identity, channelwise scalar error, occupied-state energy witness and resource formulas are consistent with the exact PR9667 two-rail apparatus and preparation. No mathematical correction is required for the bookkeeping reviewed here. Both original calibration corrections—non-strict <=10eta at eta=0 and actual-deficiency d followed by monotonicity of the complete g—are preserved correctly.

This check is deliberately narrower than re-reviewing the calibrated theorem. It does not qualify any PR9668 endpoint apparatus, recertify the parent scattering/preparation theorem, rerun a publication program, or assign retained/audit status. Original qualification remains conditional and source-exposed.

The complete draft reviewed is `sources/THEOREM_NOTE.md`, 23314 bytes, SHA256 `2ab90129937c61c3255db5c93dc9af838a6249d11a16628c674b919ab54d85f2`. Its complete `SOURCE_IDENTITY_AND_DEPENDENCIES.json` was read. The exact PR9667 canonical parent was obtained by git show at commit `cbd23228ffb0b70f6b86f7d9ea03261fa6fb51f7`, path `docs/REAL_CONTROL_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`, SHA256 `0266602321da0c7a9a723b4f1bed38ef49b87a25f2213141217da2df124499ca`.

The canonical parent preserves the realifier body `c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018` exactly, and the preparation body `57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c` exactly after reversing its three declared Markdown link destinations. I independently verified both full-body comparisons, with wrapper-only whitespace outside them. Relevant full-qubit definitions, coefficients, geometry, schedule, counts, loads, identity and work sections were read from those original exact bodies. Their unchanged scattering proof was not re-reviewed.

The complete calibration REPORT, SHA256 `a495c6b5c7bb4fd2094bc122afdab811e85de9ef92a88ea9dc2ae918364982d4`, and complete CORRECTIONS.json, SHA256 `c119f7160b3bbd1d4005d04f2eebe0145608c9123c1ebc319f4f4668ecfd79a8`, were read to determine prior coverage and preserve the repairs. Exact source paths, sizes, hashes, read scopes and canonical comparisons are in SOURCE_PINS.json. The corrected candidate and root acceptance identities are carried by the draft/correction provenance; their full unchanged theorem/qualification is not represented as freshly re-reviewed here.

This is a same-model analytical check with the draft, parent definitions and previous calibration report exposed. This reviewer previously worked on the distinct PR9668 structural route, which supplies no mathematical premise for this check. No author checker, execution output or scientific program was used. Existing governing reviewer/workflow instructions were reused from the previous verified identical reads; this task does not modify them.

## 1. Full-space identity coefficient alpha_R

The coefficient of the global Pauli identity is the normalized full-qubit trace. It is not the energy of the delivered seed or the scalar in the one-head reduction. Identity extension to untouched qubits leaves each local normalized trace unchanged.

For Q_uv(h), the one-excitation block is [[|h|,h],[h,|h|]], with eigenvalues 0 and 2|h|; the |00> and |11> eigenvalues are 0 and 2|h|. Thus its full spectrum is {0,0,2|h|,2|h|}, its norm is 2|h| and its identity coefficient is |h|. Its full complement 2|h|I_uv-Q_uv(h) has the same norm and identity coefficient |h|. The constant 2|h|I_uv has not been discarded. An occupation or vacancy has identity coefficient one half.

Applying those facts to the parent preparation equations (1), (4), (5), (6) gives the following identity contributions:

| Runtime group | Identity coefficient |
|---|---:|
| K=2I+Z1Z2 | 2 |
| DeltaA nA+DeltaB nB | (DeltaA+DeltaB)/2 |
| hAB(nA+nB-hopAB) | hAB |
| u_AB nA nB | u_AB/4 |
| gA nA(I+X1)+gB nB(I+X2) | (gA+gB)/2 |
| Two rails' 2(M-1) Q(-J) bonds plus four endpoint Jn terms | 2J(M-1)+2J=2JM |
| Two contacts of each source type | lambdaA+lambdaB |
| Two mu0 occupations and two nu vacancies | mu0+nu |
| Six emitter cells, two emitter occupations and four clock vacancies | E0+2kappa d_c |

For the last line, the six cell magnitudes sum to 2kappa d_c, the two emitter occupations contribute E0-kappa d_c, and the four vacancy identity coefficients sum to kappa d_c. Therefore the complete sum is exactly

    alpha_R=2+(DeltaA+DeltaB+gA+gB)/2+hAB+u_AB/4
            +2JM+lambdaA+lambdaB+mu0+nu+E0+2kappa d_c.

This matches the draft and parent preparation equation (26). In particular the full normalized-trace contribution of two nu vacancies is nu, whereas their scalar in the one-head expansion is 2nu. Confusing those would be an error; the draft does not.

## 2. Every calibration-channel identity contribution

The isolation consists of eight edge complements: six emitter edges and two clock edges incident to m. The sum of their |h| is 2kappa d_c+2J. The pin contributes identity coefficient (E0-kappa)/2. Hence

    sum_(a=1)^9 alpha_a=2J+2kappa d_c+(E0-kappa)/2=Aiso/2.

The isolation profile has area four. In the stated ordering of channels 10–14, their operators, areas and identity coefficients are respectively:

| Channel | Operator | Area | Identity coefficient | Integrated error |
|---|---|---:|---:|---:|
| 10 | Q_e0,m(+1) | pi/4 | 1 | (pi/4)xi_10 |
| 11 | n_e1 | pi/4 | 1/2 | (pi/8)xi_11 |
| 12 | Q_m,e1(-1) | pi/2 | 1 | (pi/2)xi_12 |
| 13 | n_e0 | pi/2 | 1/2 | (pi/4)xi_13 |
| 14 | n_e1 | pi/2 | 1/2 | (pi/4)xi_14 |

Together they reproduce exactly

    delta_theta=4 sum_(a=1)^9 xi_a alpha_a
                +(pi/4)xi_10+(pi/8)xi_11+(pi/2)xi_12
                +(pi/4)xi_13+(pi/4)xi_14,
    |delta_theta|<=eta[2Aiso+11pi/8].

The nominal integrated identity coefficient is 5alpha_R+2Aiso+11pi/8 and the actual coefficient adds delta_theta. This full-space quantity is not Phi. The old 2I is already included in the literal exp(-5iK), and nonidentity terms have additional action in the supported core. Duhamel uses the full perturbed positive blocks, so it already pays delta_theta; a second scalar-error charge would double count it.

The repeated n_e1 operator is two independently calibrated time channels. Combining them would alter the allowed calibration family; the draft keeps them separate. All relative errors scale whole complements/Q/occupation blocks, so they cannot be interpreted as independent density, hopping and identity errors.

## 3. All-occupied energy witness and variance

Take old |00>, so K has expectation 3 and each old X has expectation zero. The good auxiliary state has only e0 occupied; all clock/source sites and e1 are blank. Its clock/contact occupations vanish, the two nu vacancies give 2nu, and its emitter block sum gives E0+2kappa d_c. Therefore

    E_good=3+E0+2nu+2kappa d_c.

For the bad auxiliary state every auxiliary qubit, including both sources, is occupied. On each clock bond Q(-J), the expectation is 2J. The two rails contain 2(M-1) such bonds and four endpoint occupations Jn, giving exactly 4J(M-1)+4J=4JM.

Its source diagonal terms give DeltaA+DeltaB+2hAB+u_AB+gA+gB. Each source X expectation is zero, so the four clock/source contacts give 2(lambdaA+lambdaB), the two mu0 occupations give 2mu0, and both nu vacancies vanish. The six emitter cells give 4kappa d_c, the two emitter occupations give 2E0-2kappa d_c, and the four emitter-associated clock vacancies vanish. Their total is 2E0+2kappa d_c. Hence

    E_bad=4JM+3+DeltaA+DeltaB+2hAB+u_AB+gA+gB
           +2(lambdaA+lambdaB+mu0)+2E0+2kappa d_c.

All hopping expectations vanish in these computational basis vectors. Neither component needs to be an eigenstate: source/old X terms and outgoing hopping can create nonzero within-component variance. Their means are nevertheless exactly the displayed expectations.

The states are orthogonal, so the auxiliary mixture with weights 1-epsilon and epsilon has exact seed probability 1-epsilon. The mean shift is epsilon(E_bad-E_good). More explicitly,

    E_bad-E_good=4JM+C,
    C=DeltaA+DeltaB+2hAB+u_AB+gA+gB
       +2(lambdaA+lambdaB+mu0)+E0-2nu.

The kappa d_c terms cancel. C is independent of M and kappa for this fixed coefficient family. Thus the displayed 4J epsilon M+O(epsilon) statement has an explicit fixed remainder.

For any two component density matrices and any finite Hermitian H, direct expansion of Tr(rho H^2)-Tr(rho H)^2 gives

    Var_mix(H)=(1-epsilon)Var_good(H)+epsilon Var_bad(H)
              +epsilon(1-epsilon)(E_bad-E_good)^2.

Nonnegative component variances give the draft's lower bound. No one-head theorem is being applied to the many-head branch. This witness does not prove an impossibility of preparation or cooling: it shows why small trace deficiency alone cannot retain the pure-seed energy-moment formula with a small clock-length-independent bound. The stated coupling interval has finite maximum M; the draft correctly preserves that qualification. The setup-work bound limits the change of delivered mean energy, not its initial value.

## 4. Physical counts, supports and loads

There are two rails of M qubits, two emitters, two sources and two old qubits, giving 2M+6 qubits. To reconstruct the parent count of runtime positive blocks excluding K:

| Group | Two-body blocks | Onsite blocks |
|---|---:|---:|
| Source/old terms: exchange hAB, density u_AB, two g terms, two Delta occupations | 4 | 2 |
| Rail bonds and endpoint occupations | 2M-2 | 4 |
| Four source/clock contacts, two mu0 occupations, two nu vacancies | 4 | 4 |
| Six emitter cells, two emitter occupations, four emitter-clock vacancies | 6 | 6 |
| Total | 2M+12 | 16 |

Thus there are 2M+28 runtime blocks excluding K. The hAB and u_AB terms count separately even though they use the same pair. These are prescribed positive-block/channel counts, not counts of distinct graph edges.

Preparation adds eight complements, one pin, two pair pulses, two spectator pulses and one phase pulse: 8+1+2+2+1=14 channels. These use eight existing sites and eight existing edges. The pair pulses use two of the already listed emitter edges; no extra qubit is introduced. Total runtime-plus-preparation channels are 2M+42 excluding K.

The source incident norm sums reconstruct as

    load_A=DeltaA+2hAB+u_AB+2gA+4lambdaA
           =27.936224853155858,
    load_B=DeltaB+2hAB+u_AB+2gB+4lambdaB
           =22.228906875353305.

The added old loads are 2gA=1.993757127633340 and 2gB=1.198638631120596. The unchanged K edge has separate norm 3. Controls touch none of these sites, so these loads remain unchanged. Full complement norms are counted on their prescribed support; their scalar identities are not discarded to reduce an incident load.

For a touched site, the safe total bound is unchanged runtime load plus (1+eta) times nominal added-control peak load. Rescaling the runtime or source loads would describe the wrong calibration model. The draft uses the correct addition. The eight coordinates and six signed emitter edges match the exact parent's definitions. At kappa=10^-8, T=10^16, M=5e17, so 2M+6=10^18+6 and the total elapsed window is [5+T,5+2T]. These counts concern PR9667 exclusively.

## 5. Strength, slew and all-state work bookkeeping

The nine isolation norms sum to Aiso=4J+4kappa d_c+E0-kappa. Because pulse windows are disjoint, the largest pair-plus-spectator control sum is 3 max(w2)=45pi/16, not the sum of all pulse peaks. Therefore the added peak norm sum is bounded by

    (1+eta)[Aiso+45pi/16]<9(1+eta)<9.001

for eta<=10^-5. During ramps, derivative incidence is bounded by (1+eta)(3/2)Aiso. During the second pulse, a pair site has derivative norm at most (1+eta)*2*(pi/2)*(10sqrt(3)/3), below 20(1+eta)<20.001. Its spectator occupies a separate site and has a smaller bound. Isolation is constant during pulses, so no ramp derivative is added to that peak.

Each isolation profile has variation two; each nonnegative one-hump pulse profile has variation twice its peak. Using full norms 2 for Q and 1 for each spectator/phase occupation gives

    integral ||dot A_xi|| <=(1+eta)[2Aiso+6 max(w1)+6 max(w2)+2 max(w3)]
                          =(1+eta)[2Aiso+165pi/16]
                          <33(1+eta)<33.001.

The equality for modeled work follows by differentiating the actual state's expectation of HR+A_xi; its commutator contribution has zero trace. The endpoint controls vanish, giving Wsetup=Tr(HR rho5)-Tr(HR rho0). This holds for leaked, correlated and many-head inputs on the finite space. It does not use ideal-core cancellation, nor assert zero pulse work. Whole-block constant scaling preserves the finite variation/C1 properties. A mere amplitude bound on rapidly time-varying errors would not justify these slew/work ceilings.

## 6. Prior review coverage versus newly displayed formulas

No newly introduced scientific formula in the requested bookkeeping lacks a source derivation. The distinctions are:

| Draft elaboration | Prior coverage |
|---|---|
| Explicit expanded alpha_R | Not printed as an expanded formula in calibration REPORT; exactly parent preparation equation (26), which REPORT identifies as its read/inherited identity-coefficient source. Reconstructed independently in section 1 above. |
| Full complement identity coefficients, alpha_iso, all fourteen delta_theta terms, integrated scalar and Phi distinction | Explicitly present in calibration REPORT section 4, lines 178–201. |
| E_good, E_bad, all-occupied clock term, mixture variance inequality and finite-maximum-M qualification | Explicitly present in REPORT section 8, lines 458–501. |
| 2M+6 qubits | Explicitly stated in REPORT section 2; also parent section 7. |
| Explicit 2M+28 runtime blocks | Parent preparation section 7 gives this exact number and its 2M+12 plus 16 decomposition. REPORT section 7 refers to the unchanged runtime count without printing 2M+28; its explicit 2M+42 total and fourteen added channels are consistent. Reconstructed independently in section 4 above. |
| Fourteen channels, eight sites/edges, 2M+42 total, source/old loads, correct scaling of control-only loads, strength/slew | Explicit REPORT section 7. |
| Full-state work identity and 165pi/16 variation coefficient | Explicit REPORT section 8. |
| Exact coordinate list and concrete polynomial schedules | Exact parent definitions; REPORT references those supports/profiles and states their extrema. The draft expands their display, not the calibration domain. |

Thus the main added printed expression not already expanded in REPORT is alpha_R, and the explicit runtime-only count is inherited rather than printed there. Neither is a new theorem beyond the pinned parent; both have now received this selective independent algebra/count reconstruction. The expanded draft should not be described as though every displayed equation originated in REPORT alone.

## 7. Preserved corrections and verification limits

At eta=0 the draft says <=10eta, correctly allowing equality zero. Its subsequent strict output ceilings retain separate nominal slack. For the imperfect seed it uses actual deficiency d<=epsilon, derives the projection disturbance at d, adds d and only then uses monotonicity of g(d)=d+sqrt[d(4-3d)]. It retains the d=2/3, epsilon=1 counterexample to monotonicity of the isolated projection term. Neither repair was undone by the bookkeeping expansion. This check does not rerun the unchanged channel-composition proof.

The broad rg inventory output was truncated, so it was used only to locate sections; the complete draft, manifest and calibration REPORT and the specific full parent premise sections were read separately. No truncated inventory was treated as mathematical evidence.

One metadata-only capture attempt failed an assertion that assumed a separator after each canonical preserved source. Inspection showed three trailing newlines instead. Both source bodies were already exact matches after the declared link reversals. The wrapper check was corrected to require whitespace-only suffix and a single wrapper heading; the final source manifest verifies both bodies. This was not a scientific failure or changed acceptance threshold. It is recorded in SOURCE_PINS.json. No scientific program, matrix computation, numerical parameter test or inherited checker ran.

Only calibration_bookkeeping_independent_check was written. No proposal, previous review, canonical source, W, Git state, prompt, axiom, audit verdict, root checkpoint or other chat was edited. This report supports only the requested explicit bookkeeping on the pinned PR9667 family. It neither extends the preparation-calibration model to PR9668 nor changes any source qualification or publication decision.
