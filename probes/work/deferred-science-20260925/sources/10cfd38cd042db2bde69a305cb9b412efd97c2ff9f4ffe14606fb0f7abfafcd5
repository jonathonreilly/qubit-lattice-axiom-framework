# Released comparison of the optical reference-energy and response candidates

This is a bounded POST comparison, not an audit verdict or a new blind derivation. The independent PRE remains unchanged: `PRE.md` SHA-256 `24e103cc969b14d80f7e4e897d1a94c885914306b6feecdacf9656663e168bc6`, sealed by `PRE_SEAL.json` SHA-256 `0931fe9b88d147fcb9994ea87a0cb48b47cf0215055a8fe9a4780f51ef38666c` at 2026-09-24 23:17:14.539761 UTC. All 23 PRE members and its four current parent origins were verified again. The three author packets below were first opened for this released POST. Root28's experimental-comparison argument is separately checked released material; it was not derived in this PRE.

The root26 finite-volume reference-gap argument and root27 hard-band and mean-energy response bounds are supported under their stated conditional premises. Their larger constants than the PRE's constants are valid. I found no material proof or SI-arithmetic error. Three small reporting repairs are specified below. The root28 comparison correctly stops short of an empirical identification, exclusion or confirmation.

## Exact released scope and origins

All paths below are relative to `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth`. Complete source snapshots, author controls, result/stdout/stderr files, execution receipts, source declarations and preserved hard-band history are retained under this directory's `post_sources/`. `POST_SOURCE_PINS_INITIAL.json` records all 33 original-file and snapshot identities; the final manifest refreshes them.

| Released argument | Argument SHA-256 | AUTHOR_SEAL SHA-256 |
| --- | --- | --- |
| `finite-volume-observation-personal/FINITE_VOLUME_OPTICAL_SCALE_DIAGNOSTIC_ROOT.md` | `f28a1e685cf74050230f123a074c34ea87ddf7f088ad663b7755fd43756b3e1c` | `4bfc4024aba417878501140db6a2fda47d4251cc0f922a55002939a799848c6e` |
| `optical-band-response-personal/OPTICAL_BAND_ORIGINAL_PROBE_RESPONSE_ROOT.md` | `892598ff8c260bad16fe1fe36d6a3b5e4ba5dcb0b247f394853360f44d4b901b` | `0207294ccd5079745d0d6915a5060fb74b482eeedabf944a0180174631adba80` |
| `optical-experiment-scope-personal/OPTICAL_EXPERIMENT_COMPARISON_SCOPE_ROOT.md` | `2f34fa36a2d7da31be5cf78beaf4c1800ed91051dfdc9a542f1bacd09251def0` | `7a809dd2ca14265b8659fbd5eea19e6377cb4864ab04a35645c9489854a92e01` |

The three seals respectively bind 7, 15 and 7 members. Their recorded times precede the PRE seal. This verifies the stored identities/timing records, not private author activity. Root26/27 were compared against my preserved derivation. Root28 and its primary comparison were assessed after release.

The four named PRE parents are reused conditionally with unchanged hashes and scopes in `SOURCE_PINS.json`: weak-field `651fa7cf…`, photon/SI `acf74cfc…`, physical prepared probe `14ed0194…`, and physical-limits Part C `2dd49ffa…`. No transitive theorem or archival timing analysis is recertified. Root28's additional clock-note origin `91fd6c3d…` is an unchanged previously reviewed source; its hash was checked. Whole-file hashing of the physical-limits parent does not add Part A/B science coverage. In particular, the root26 sentence about the broad ordinary charged-probe energy is a cited external premise, not a new full-Hamiltonian result checked here.

## Reference spectrum and local spectral weights

Let `V=L^3`, `s(k)=sqrt(4 sum_mu sin^2(k_mu/2))`, and `E_*=hbar c/a`. After removing gauge and harmonic zero directions, the reference contains `2(V-1)` real oscillators. For even `L>=6`, the lowest shell has six nonzero momenta and two polarizations, hence twelve real oscillator directions. Counting both momenta in a complex Fourier sum already reproduces the real sine/cosine quadratic form; a further factor of two would be wrong. The root normalization agrees with the PRE's direct real-curl reconstruction.

For every normalized reference one-excitation packet,

    E_ref >= 2 E_* sin(pi/L).

Root26's proof identifies the minimum exactly and its inequality direction is correct. The standalone harmonic identity also holds on the stated `L>=4` graph; when attached to the original prepared probe, retain that probe's even `L>=6` hypothesis. No global zero mode or vacuum component can be used to evade this minimum while remaining in the stipulated normalized nonzero one-excitation sector. It is neither a lower bound on the full charged Hamiltonian's spectral gap nor a statement about arbitrary sectors.

Under the *same additional* photon, proper-spacing and clock identification and the inherited orientation-necessary bound `a<6 hbar c/E_QG,min`,

    E_ref,min > E_QG,min sin(pi/L)/3,
    L > pi/arcsin(3 E_lab/E_QG,min),  0<3 E_lab/E_QG,min<1,

is necessary for a normalized packet with hard ceiling or mean ceiling `E_lab`. The argument does not select `a` or `L`, does not add statistical coverage to the archival bound and does not obtain a volume-uniform approximation to the full dynamics. The PRE's physical-side-length expression `L a` and static cell enclosures are independent PRE additions; root26 did not derive them.

For an xy plaquette, the sum over its two transverse polarizations is `D_xy(k)/V`. Gauge-gradient and harmonic directions have zero curl. Thus the root's real mode vector `d`, its total norm `v`, and its band norm are exactly

    v = sum d_r^2 = (1/(2V)) sum_{k!=0} D_xy(k)/s(k),
    v_band = (1/(2V)) sum_{0<s(k)<=epsilon} D_xy(k)/s(k).

In particular `v=(1/(3V)) sum_{k!=0}s(k)` by coordinate permutation. For a nonempty band, `max |d^T alpha|^2/v=v_band/v`, attained by the normalized projected vector if nonzero. An empty band has no normalized state. A nonempty subspace with vanishing projected vector instead has an attained zero response. These cases are correctly separated in root27's prose.

The root's coarse uniform estimate is valid: `||c_p||^2=4`, `s<=sqrt(12)` give `v>=1/sqrt(3)`. For centered momenta, `s>=2|k|/pi`; a band momentum therefore satisfies `|n|<=L epsilon/4`. A nonempty band implies `L epsilon>=4`, so its enclosing cube has at most `27 L^3 epsilon^3/64` points. Each plaquette-weight summand is at most `epsilon/(2V)`. Consequently, for the specified `0<epsilon<=2`,

    v_band <= 27 epsilon^4/128,
    eta <= 27 sqrt(3) epsilon^4/128.

The empty-band case satisfies the projected-weight inequality without supplying an optimizer. An upper bound greater than one at large epsilon is merely non-sharp. The stronger small-band constants, explicit static large-volume remainder, exact mean optimizer and tail attainability in my PRE remain separately attributed PRE results, not claims of root27-before-disclosure derivation.

## Mean energy, mixed states and transfer to counts

The weighted bound does not discard high-energy tails. On the finite positive one-particle mode space let `Omega=diag(s_r)` and `w_p=d^T Omega^-1 d`. Permutation symmetry gives exactly

    w_p=(1/(2V)) sum_{k!=0} D_xy(k)/D(k)=(V-1)/(3V).

Weighted Cauchy-Schwarz gives the operator inequality `|d><d| <= w_p Omega`. Hence a density matrix supported in this reference one-particle space satisfies

    eta(rho)=Tr(rho |d><d|)/v
            <= w_p Tr(rho Omega)/v <= epsilon/sqrt(3).

This explicitly verifies the root's convexity extension without replacing mixed-state response by a coherent amplitude. For an individual pure packet it reduces to the PRE formula. For varying density matrices the inequality still holds pointwise; a displayed limiting equality requires a fixed state or a convergent response parameter, otherwise state it as a limsup bound when the parent's finite-dimensional uniformity is used.

The root's approximate-band bound also follows from the orthogonal low/high decomposition and Cauchy-Schwarz. If the high-band probability is `w_tail`,

    eta <= [sqrt((1-w_tail) v_band/v)
             +sqrt(w_tail (1-v_band/v))]^2.

There is no justification for applying the hard-band fourth-power bound using only a mean-energy ceiling. My PRE supplies explicit normalized one-particle high-tail examples and a sharper constrained optimizer; root27 does not claim those constructions. Its weaker linear bound is independently valid and adequate for its conditional SI conclusion. None of these one-particle inequalities is automatically an arbitrary-multiparticle statement or a bound on ordinary energy of the full charged preparation.

For the uncut harmonic reference the root uses the exact initial ratio `1+2 eta x/(exp(x)-1)`, with `x=g^2 v/2`. For the actual normalized compact preparation and full original process the applicable conclusion is instead the parent's shrinking-window limit: at each fixed finite graph, for `b=o(tau g^3)`, the at-least-one selected-mark probability ratio tends to `1+2 eta`. This imports the full-generator and factorial-moment estimates, retaining every channel and the physical Gauss-consistent preparation. It does not evolve the charged state solely with the reference harmonic Hamiltonian or assert band conservation under the full generator.

The microscopic comparison first fixes graph, `g` and a positive window, takes the prescribed spin/register comparison and grid refinement, and only then chooses errors small enough before the weak-field/window limit. The microscopic initial derivative is not substituted for the effective initial rate. Finite-dimensional uniformity at one fixed graph does not control changing `L`. To resolve the tiny optical contrast one would need errors below that contrast, not only an unquantified `o(1)`. No finite `g`, changing-volume or fixed laboratory-duration accuracy follows here.

## Released primary comparison and SI arithmetic

I read the complete primary [Brouri et al., quant-ph/0007032v1](https://arxiv.org/pdf/quant-ph/0007032v1), including all methods, normalization, results and captions, and visually inspected all eight locally rendered pages. Exact local PDF SHA-256 is `a5759a2a381b2039448484e321b740f2bf2b73d3c8265e58f1e76d8b08a3cb6a`. `POST_PRIMARY_WEB_RETRIEVAL.json` records the URL, full parsed retrieval and time; the remote PDF byte hash was not measured. The local exact-byte copy is the rendered primary.

The paper uses continuously excited NV fluorescence and two APDs in an HBT geometry. Its quoted detector factor is an estimate, `eta_det=0.7`; the overall per-detector collection/detection estimate is `0.0014`. The coincidence correction uses `rho=S/(S+B)=0.34`, not `S/B`. Its formulas and Figure 3 inputs give

    C_N(t)=c(t)/(N1 N2 w T),
    g_signal^(2)(t)=[C_N(t)-(1-rho^2)]/rho^2,
    N1 N2 w T=5780*5990*(1 ns)*11450 s=396.42419.

Thus a hypothetical exact corrected zero corresponds to `C_N=0.8844` and raw count `350.597553636`, not zero raw coincidences. This is formula arithmetic, not digitization or a fit. Background independence is an explicit source assumption; that background is not a prepared quantum vacuum. The delay-bin width is not by itself a fresh-preparation event window or a detector-response-time measurement. The quoted fluorescence interval is not certified hard support; the paper also discusses stray shorter-wavelength fluorescence.

Independent Decimal arithmetic, using exact SI `h`, `c` and elementary-charge definitions and a separately written Machin-series pi calculation, agrees with all twenty stored root26/27/28 unit quantities. The largest relative discrepancy is below `2.34e-65`; these are rounded consistency checks, not interval certificates. Important illustrative values are:

| Conditional quantity | Independently checked value |
| --- | --- |
| `hc/(637 nm)` and `hc/(800 nm)` | `1.94637674149 eV`, `1.54980248042 eV` |
| Root27 mean-bound limiting excess for a **supplied** 2 eV reference mean ceiling | `<2.00817484936e-20` |
| Same-clock bound from `E_QG,min=6.9e20 eV` | `tau<5.72358223436e-36 s` |
| A 1 ns interval divided by that upper clock scale | `b/tau>1.74715756506e26` |

The 2 eV mean ceiling is an illustrative model premise, not an experimental state estimate inferred from endpoints. The ratio `p_1/p_0-1` is neither quantum efficiency per incident photon nor the normalized two-detector correlation above. Comparing it numerically with 0.7 has no calibrated meaning. The preparations, observed count functional, physical probe, source history, background and time regime have not been matched.

The existing sufficient regime `b/(tau g^3)->0` provides no controlled error for the cited 1 ns histogram at a chosen finite `g`; its failure to cover that scale does not prove necessary detector bandwidth or rule out a longer-time law. The timing input also retains all inherited photon/source/cosmological/orientation assumptions. The root28 non-exclusion and non-confirmation conclusions are therefore justified. A physical comparison requires a derived and calibrated source/detector/count mapping with errors on the actual scales. This review establishes no unique required detector design, source-to-detector theorem or framework-wide impossibility.

## Exact repairs, evidence and remaining scope

1. **Root27 data label:** eleven rows have `normalized_band_packet_available=false` but `max_eta=0`. Zero is the correct projected weight, while a normalized-state maximum on the empty band is undefined. Before presenting this field as an optimum, use `max_eta=null` for unavailable bands, or rename the field to `projected_weight_fraction`. Preserve the feasibility flag and existing runs. The root prose already states the correct case distinction; no spectral inequality changes.
2. **Root28 normalization wording:** replace the ambiguous phrase “signal/background parameter0.34” with `rho=S/(S+B)=0.34`. This prevents reading the number as `S/B` and binds the normalization to the actual primary method.
3. **Root28 closing efficiency wording:** replace “measured efficiency” with “quoted detector-efficiency estimate”. The primary's 0.7 detector factor and 0.0014 overall estimate are distinct. The scope conclusion is unchanged.

The current root26 and root28 complete controls/results, the current root27 six volume records and all 42 band/three SI rows, its complete code/review, and the preserved earlier generation were inspected. `POST_HISTORY_DIFF.txt` contains the full earlier/current argument and source differences. The earlier scientific payload equals the current payload exactly after removing the explicit mean-energy additions, renaming the expanded hard-band field, and excluding runtime/source identity. All five volumes shared with my sealed PRE agree in `v` and `w_p` within `2.23e-16`. Floating cutoff membership is not a certified integer-shell enumeration; the analytic bound supplies the theorem.

No author or inherited runner was imported or executed. `post_verify_and_arithmetic.py` is new independent bookkeeping/Decimal code. Its first execution stopped on a source-manifest schema mismatch before arithmetic; exact first code/logs/receipt are preserved under `post_attempt01_schema_key_failure/`. The corrected verifier completed in approximately 0.071 seconds with exit zero and empty stderr. The PDF renderer completed with a retained Fontconfig warning; all eight pages were readable and inspected. A mistyped nonexistent result filename caused one read-only `cat` error; the correct named file was then read. These events are recorded, not erased or treated as scientific failures.

`POST_VERIFICATION_REPORT.json`, full stdout/stderr and execution receipts bind these checks. All source/evidence identities and the unchanged PRE anchor are sealed separately by `POST_SEAL.json`. No author/publication file, prior seal, audit state or retained status was changed. No other active checker packet, new energy candidate, checkpoint or outcome file was opened. Work stops at this POST.
