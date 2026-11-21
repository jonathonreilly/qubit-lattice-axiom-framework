# C4: simultaneous order of constants
Provenance: Codex (GPT-6; exact runtime model ID unavailable), xhigh queue assignment; checkout `75752c07e1f2864b606056195041681352549c11`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; grants no status.

## Scope and notation

This checks node C4 of `t0-skeleton.md`, Section 5, item 4. It does not prove any estimate.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and its constant scheme.
`SA` means their `YM4_sketch_500.tex` at the commit above, fetched once. Local paths below are relative to this research folder.
An arrow means “choose before.” Constants returned by a stated estimate remain conditional on that estimate.
Different occurrences of an unnamed `C` need not denote the same constant. Scale-indexed thresholds are functions, not new choices.
In the table, `p₀,p₁` denote the exponents `𝔭₀,𝔭₁`, not the functions `p₀(g),p₁(g)`.

## One order

Read downward; read arrows within a row from left to right. Each dependency includes its own earlier inputs.
Row 8 flags an early input not supplied with the required uniformity; the rows after it are conditional on that input.
Use different names for the local walk size `m_w` (called `M` in `p82-curved.md`) and the construction size `M`.
Write `γ_H` for a response rate, `γ₀` for a current ceiling, and `γ` for the coupling ceiling.
Freeze estimates on a larger admissible class first. Later field strengths lie below its ceilings; they do not redefine its rates.

| Order | Constants, including returned constants | Inputs and source of dependence |
|---|---|---|
| 1 | Fixed margins `β_s, θ_s, θ_c`, mark fraction `w<1`, Hölder exponent `0<α_H<1`, window enlargement factors, tolerance `ε`; finitely many requested age exponents `b` | Free data. SA 19444, 19461–19464, 19481; `gates/sa-2.8-terms-gate.md:172`. Fix the inner envelope factor `λ_a` here, as required by `gates/o1-decoupled-gate.md:205–210`. |
| 2 | `r≥2 → p₀ → p₁ → q`; `κ₀>max(8,C)` | Require `p₀>3Cr`, `(p₀+Cr)/2<p₁<p₀−Cr`, `q−p₀>Cr`, `q>Cp₀`. SA 19487–19493, 20745–20748. The `C` here denotes the fixed power-count constants of those assertions. |
| 2a | Geometric counts `C_D^dom,κ_D,κ_f,c_f,c_b,c_m,C_v,c_adj`; fixed hull/base constants `C_h^WF,C_win,C_h^UM,c_ℓ,C_geo,C_base`; `λ₀,σ₀>κ_f`, entropy reserve `ε_rate>0`, logarithm gap `g_*` and its sum `B_*^UM` | Fixed cubical/window rules. SA 14416–14477, 14661–14699, 15229–15235, 15848–15855, 16137–16175, 16248–16279. Choose `g_*>κ_D+C_v` with `c_adj B_*^UM≤1`. The fixed-ratio geometric interpretation, needed to put the hull constants here, is stated below. |
| 3 | Odd `L≥27`; one-step averaging/chart constants and flat constants `B_L,C_L,c_L,N_L,D_L,a_L`, flat decay and Hölder bounds | Rows 1–2a; require `L>4C_h^WF C_h^UM c_ℓ(1+4β_s)` for the rate window below, and `L²≥6√2 λ_a` for inner substitution. `p82-curved.md:44`; `gates/o1-decoupled-gate.md:210`; `geo-5.md:45`. |
| 3a | One-loop constants `c₀,c₂ → C_β=c₀+2c₂+2 → λ̲=c₀/4,c₅=2c₂,B̄=C_β+1`; increment envelope `B_*=B̄` | `c₀,c₂` are fixed with `L` (SA 19475). The slack choices are allowed by SA 20736–20746. The later smallness ceiling makes the error fit this envelope. These weak bounds do not use `E₀,N_★` or `γ`; see the hand check. |
| 4 | Local inverse/gauge constants `B₀,B₁,B₃`, collar/reset widths `W`; `m_w, c_reg, α_*^loc → δ_w,θ₀`; initial regularity/current ceilings | `L` and flat inputs. `a1-balaban.md:1341–1348`; `p82-curved.md:44`; `gates/a1-balaban-gate.md:134`. Fix local sizes at their admissible `L`-dependent values, before the actual layer gap. |
| 5 | Propagator rates `δ₀,δ_*,δ′`; profile length `σ → δ,ε_*`; walk constants `M′,ρ′,r₀,τ₀,τ_L,B_L,C_K,C_W,C_T,C_h^walk,δ_h` and ceilings `a_*,γ_j,a_T,a_B,a_h` | Row 4 and fixed reference ceilings. SA 9916, 10582; `a3-profile.md:618–633`; `h-walk.md:391`. Any common rate is below **both** the profile and propagator rates (`a3-profile.md:679–684`). |
| 6 | Walk/cell size `M₁=𝔐 → R₁ → ρ=R₁M₁`; summation constants `K_a` | Earlier rates, reset widths and walk counts. Include `ν₁C_W/M₁≤1/2`, the tree-count floor on `C_TM₁^(−1/3)`, `R₁≥8L³`, and all rate-times-gap floors. `gates/a1-balaban-gate.md:37` and D2; `a3-close.md:44`; `o1-decoupled.md:105,135`; `pw-bridge.md:379`. |
| 7 | Actual A1/seam constants `C↓,B →` uniqueness/reset radii `a₅,a₀,a₁,ε̄,r_B`; A2 gap and complex radius `c_L,C_A,ρ_L`; A3 `C_lin,C_N,r_*,r_A3 → C₄,C_R,C_μ,C_P,C′_c,C_mult`; tower `r_D,r_Q,C_D,C_Q,K_L,C_b,K♯,θ_b → a_T,d_*` | Rows 3–6. A1: `a1-balaban.md:1345–1348,2440–2447`; A2: `a2-curved.md:770`, `a2-full.md:206`; A3: `a3-derivative.md:351` and Section 7 (`r_A3` is its radius, not row 2's exponent); tower: `wf-room-2.md:252`, SA 9753. `C_mult` denotes the multiplier constant `C_M` of `ref-chart.md` Lemma M. These are package ceilings and bounds, distinct from the final running radii. |
| 8 | **Flagged input:** a fixed finite Gaussian cost envelope `C̄₀^UM`; history entropy rate; `κ → κ_sum=κ/4,κ_far=κ/4,κ_ret=κ/2`; `μ_out=(1+4β_s)κ → Λ=μ_out+g_* → K_*^UM=2+c_ℓΛ → Θ=C_h^UM(C̄₀^UM+K_*^UM) → λ=λ_V` | Earlier geometry and exponents **only if** the cost envelope can be fixed before `κ̄,M`. Otherwise its inputs are in row 14: see the cycle below. Choose `κ` large for history entropy, `κ/4>κ_D`, and `λ₀+σ₀+Θ/L≤λ<κ/(2C_h^WF)−ε_rate`. SA 14565–14583, 16265–16279, 19444. SA 14779–14791 does not state the required uniformity in these later constants. |
| 9 | `κ̄,κ₁`; parameter radius `R_s=e^κ̄`, bracket rate `β_br=κ̄−1` | `L,κ,Θ,λ`: `κ̄≫Lκ`, `β_br>C_h^WF(λ+ε_rate)`, `log(R_s−1)≥Θ`, `β_br>C_geo λ+2`; `κ₁` exceeds history entropy. SA 19475–19477, 17820, 14583, 15233–15235, 16273–16279. |
| 10 | Definition D: read radii `r₁,R_*=C_LM₁`; parameter length `ℓ_P`; `C_H, b̂=C e^(16κ̄)`, A2 comparison prefactor `C_VI`; response-ball radius `r_dec`, datum radius `b_dec`, second current ceiling `γ₀^II` | `L,M₁,R₁,τ_L,κ̄`. Take `ℓ_P>8 max(r₁,R_*)+1`, `ℓ_P≥2048κ̄/τ_L`; retain hypothesis (P). Then `r_dec<c/b̂`, `b_dec≤c b̂^(−4)`, `b̂²γ₀^II≪1`. `o1-decoupled.md:105–142`; `pw-bridge.md:367–385`; SA 10383–10404, 10580–10582; `a2-full.md`, Section 8. |
| 11 | `μ=M₁′ → M₂`; collar counts `n_c^col,n_s^col`; preparation face factor `K_face=L+1`, profile width `C_p=3/4`, eligibility bound `b_box`; WF7 `b,b_*,C_*^buf,S_γH` | `μ≥ρ`, `M₂≥Lμ`; `(n_s^col−n_c^col)μ>max(ρ,3μ)`. Definition A: `assign-adopt.md:21–35`; corrected admission: `geo-prop23.md:28`; face/profile rules: `gates/geo-gate.md`, Sections 1–3. Fix `b_box` in the eligibility rule (`geo-5.md`, Section 2). WF7: `C_*^buf=b_*+(ρ+L𝔐)/(L−1)`; take `γ_H` between the counting rate and half the response rate (`wf7-bf.md:66–81`). |
| 12 | `Θ₁,varpi_T`; A2 collar width `w_col`; construction cube size `M` | `θ_c`, response rates, `μ,M₂,ℓ_P,κ̄,c_L,C_VI`. Require `Θ₁≥C/θ_c`, `varpi_T≥C`, `M≥max(varpi_T,L²M₂,80μ,ℓ_P)`, `bM≥2C_*^buf`, and the A2 exponential-collar floor. SA 17363–17367, 19479–19480; `a2-full.md:206`; `geo-5.md:45`. WF tower room requires `min(γ_H,θ_b)cML≥log4` (`wf-room-2.md:266`). Use the `M`-grid for Definition D's parameters; it satisfies (P) with the earlier lower length `ℓ_P` (`o1-decoupled.md:116`). |
| 13 | WF tail coefficient `c_WF`; base-count factor `C_M^WF`; comparison threshold `a(L,ρ,μ)` and constants `C_E,C_BC,C_BC′,C_φ` | Earlier geometry and analytic packages. After `M`, set `c_WF≤min(c_response,b₁κ_far/M)`: SA 15868–15875; `wf7-bf.md:101–108`. Thus `c_WF M` for long members need not grow with `M`. `C_M^WF` counts old bases, SA 15848. For 2.8 retain the actual collar factor in `C_E` (`gates/sa-2.8-terms-gate.md:60,172–173`); 6(c)'s threshold comes after `μ` (SA 9916). |
| 14 | Gaussian reference bound `K_G → A_K,ε₀(K_G),ρ₀(K_G)`; density constant `C_p^UM`; tilt budgets `W₀,γ_tilt`, perturbation allowance `ε_G`; `σ_★≤1/2`; box constants `C_Λ,n_b,A_M,C_P(M),C_c(M),ℓ_N,C₅(M) → c_*(M),α_*(M) → a_Λ,C_m,C_2.4,ε_*(M)` | `M`, A1–A3 and fixed geometry. Require UM14 and UM15's `C₀^UM≤C̄₀^UM`, with `ε_G≤ε₀(K_G)` (SA 14380–14399, 14513–14528). SA 14779–14791 explicitly requires control of the actual matrix package on the enlarged discs; the budget does not establish it. `σ_★≤c(LM)^(−4)` (SA 14175–14199). Box order: `ref-chart.md:254–280`; corrected `α_*≤ε̄/(2max(1,B))` in `gates/ref-chart-regate.md:42–44`. In particular `a_Λ=α_*/(64A_M)`. |
| 15 | Joint-chart constants `C_ω → C_G → ρ_H,ρ_v,C_v,ρ_β,K_F`; tail constants `C_TL,T_C,T,K′`; reference cutoff `M₀` | A3, `r_B,c_*,n_b,a_Λ,ε_*`, and `C_φ,C_BC′`. `ref-chart.md:322–358,373–398,508`; `gates/ref-chart-regate.md`, Section 5. First restrict `r_B≤1/2` (that check, line 58). Choose `M₀` only after these constants. |
| 16 | Test amplitudes `A₁ → A₀` with `A₀≫A₁`; radius coefficients `C₀ → C₁`; absolute radii `α₁ → α₀`; inner radii `α′₀,α′₁,α′`; independent-current radii; joint-pair bound `β_A` | All preceding chart/response ceilings and `M,M₀,a_Λ`. SA 19470, 19480, 5999–6010, 9911; `ref-chart.md:508`. Take `C₁≫MC₀`. Keep `CMα₀<α₁`, `α₁²≤Cα₀`, `K♯(α′₀+α′₁²)≤α₀`, and the reduced-current ceilings. These are a radius window; see the hand check below. |
| 16a | WF normalized-response constant `C_R^WF`, fixed core-room fraction, `C_age → c_ν`; inner datum allowance `c_B′`, chart radius `r_I` | `R_s,b̂`, final radius ratios, tower margins and the **earlier** weak frame constants. Choose `C_R^WF c_ν C_age` below half every room (SA 15792–15818). Inner admission: `gates/o1-decoupled-gate.md:161,205–213`. Include the final formation-bound constant here, before the small-field map constant `K_M`. |
| 17 | Normalizer bound `E_N`, small-field constants `K_M → E₀`; boundary bound `𝔅 → C_vol`; reserve `c_r` and fixed rarity loss `c′`; deposit coefficient `c_dep` | Fixed geometry and radii. `E₀` comes from the Gaussian normalizer, not from `N_★`; boundary-origin bounds do not depend on `𝔅`. SA 19506–19522, 22308–22310. Choose the volume-payment constant after `𝔅`, and `c_r` before its coupling ceiling (SA 19482). Choose `c_dep≤c′_dep min(Θ₁^(−2),θ_c²)` after `A₁/A₀` (SA 17492). |
| 19 | GEO5(c) `C₁^GC=L2^(r−1)(1+r^rB̄) → C₄^GC=12C₁^GC(1+C₁^GC) → d₀=5+log_L C₄^GC`; `D_R=L2^r` | `L,r,B̄`, not `M`. `geo5c-count.md:11`; `gates/geo5c-gate.md:154,182`; rounded-radius repair in `geo-5.md`, Section 4.3. This corrects the printed 2.8 order. |
| 20 | Remaining 2.8 constants `C(M),c(M),C_n,n_X,C_F,C_*^2.8,C′_*^2.8`, power `K_*=9r+2p₀+3p₁+4`; profile envelope `C_x`; A2 perturbation bounds `C_IV,C_ct` | Earlier analytic, box, cutoff, profile and weak frame constants. `sa-2.8-terms.md:349–366`, with `gates/sa-2.8-terms-gate.md:166–176`; `a2-full.md:170,180–206`. The requested remainder tolerance was fixed in row 1. |
| 21 | Age weights `ω_n`, input majorant `N_★`; UM `S_σ₀,A_a,a_*^UM,w_*`, failed-test ceiling `p_*`, activity allowance `τ`; remaining marked-load constants and `s` ceiling; flow-error constants `C_v^flow,C′`; tube parameters `q₀,varpi₀,q_t,varpi` | `ω_n` uses `L,α_H`; `N_★` uses `E₀` and the early weak frame envelope (SA 16298–16303, 19501–19512). UM thresholds use `L,M,Θ,W₀,σ₀,γ_tilt`: SA 14622–14638, 14795–14806. The physical norm `a` and failed-test cutoff `𝔟` must meet these thresholds by the final ceiling; `γ_tilt` is not `γ`. Other load bounds: SA 22311–22314. Flow/tube: SA 20685–20704, 20280; require `varpi₀≤σ_★/2`, `q_t≥max(q,q₀)`, `2q_t>q+p₀`, `2varpi≤min(varpi₀,σ_★)`. |
| 22 | One common floor `X₀`, then `γ=X₀^(−1/2)` | **All previous constants**, including `c_r`, `d₀`, `c_ν`, A2 perturbation tolerances and 2.8's tolerance. Require `X₀≥e^(2q)`, `s_k<c_ν/2`, absolute/running radius ceilings, `C(M)ε_k≤a_Λ`, `M₀ε_k≤r_B/64`, tube smallness and repaired rounded-depth margins. SA 15819, 17656, 19439, 19485; `gates/sa-2.8-terms-gate.md:174`; `ref-chart.md:508`. |
| 23 | Returned flow errors `barς=C′γ^(κ₀−8) → λ_♯=c₀/2−barς,B_♯=C_β+barς` | Earlier constants and `γ`; require `barς≤min(c₀/4,1)` at row 22. SA 20740–20746. They do not select the frame constants. |
| 24 | Source radius `varrho`, age constant `c_a`; then any stronger source/mark coupling ceilings `γ_J,γ_U,γ_W,γ_★` | Earlier package, the finite age exponents and `γ`. SA 19461–19470, 19481, 6911, 17477. In particular `c_a≥C(b)log L` only for the finitely fixed `b`. Later ceilings on the actual coupling may depend on `c_a,w,varrho`; do not redefine the earlier `γ`. |
| 25 | Run data `g,ℓ,β,K`; frame values `θ_j`, actual weights `x_j`; all derived thresholds and radii | Choose within the ceilings and torus/grid floors, after every fixed constant. SA 19470, 10244, 6020–6048, 17585. `R_j=ceil_{L-powers}(log min θ_i)^r`, `N_j=R_j`, `ε_j=θ_j^(−1/2)A₀(log θ_j)^p₀`, `δ_j=(A₁/A₀)ε_j`, `δ′_j=A₁θ_j^(−1/2)(log θ_j)^p₁`, `α_{ι,j}=C_ιθ_j^(−1/2)(log θ_j)^q`. WF then defines `σ_j,ρ_j,s_k,R_ν=c_ν/s_k,varrho_F` (SA 15725–15742, 15978–15987). Compute the next coefficient before choosing `θ_{k+1}` (SA 19440, 20720–20726). |

## Hand check

**The genuine flow cycle is already cut in SA.** It would be
`γ → (λ_♯,B_♯) → γ`: SA 20740 makes the remainder depend on `γ`; SA 19485 states the reverse dependence through flow bounds.
Use the weak triple instead. Row 3a fixes its slack from the one-loop bounds; the eventual ceiling pays the errors.
This also puts the weak triple before `C_age,c_ν,K_M,N_★`, rather than following the compressed list at SA 22311–22313 literally.
No bound returned after `γ` feeds its choice.

**The literal 2.8 list has a removable order cycle.** `r → d₀` is explicit at `geo5c-count.md:11`.
The reverse precedence occurs at `sa-2.8-terms.md:365`: `r` is step 4, after step 2's `d₀` (line 363).
Rows 2, 3a and 19 apply the exact repair in `gates/geo5c-gate.md:182`. No estimate or geometry changes.

**The apparent radius cycle is a nonempty window.** Put `α₁=t`, `α₀=t/(2D)`, with fixed `D>CM`.
Then `CMα₀<α₁`; `α₁²≤Cα₀` holds for sufficiently small positive `t`.
Choose `α′₀≤α₀/(2K♯)` and `α′₁=α₁/2`; decrease `t` until `K♯α′₁²≤α₀/2`.
All fixed absolute ceilings can hold together. Running radii then fit by increasing `X₀`, without changing their prescribed ratios.

**WF's output rate must also feed UM.** WF13d (SA 16277) gives an upper bound on `λ`; UM19 (SA 14582) gives a lower bound through the target `(1+4β_s)κ`.
With row 8's definitions, the lower endpoint has slope `C_h^UM c_ℓ(1+4β_s)/L` in `κ`, while the upper has slope `1/(2C_h^WF)`.
Row 3 leaves a strict slope gap; increasing `κ` then makes the window nonempty. Choosing `λ` independently before `κ` would hide this check.

**The remaining budget cycle is `κ̄ → M → C₀^UM → Θ → κ̄`.** The opposing requirements are SA **19477**, `δ₀M≫κ̄`, and **14583**, `log(e^κ̄−1)≥Θ`; the intermediate dependencies are explicit at **14526–14528** and **14576**.
SA 14779–14785 suggests controlling the matrix contribution and then shrinking the tilt budgets, but states independence of exterior volume, not an envelope fixed before `κ̄,M`.
A visible candidate repair is to supply that envelope first and require the actual matrix/radius choices to meet it. Row 8 records exactly this change of selection rule.
Merely moving `M` or `κ̄` does not break the displayed cycle. The cited dependencies alone do not establish that the candidate repair is available; no new matrix estimate is asserted here.

**WF6 and Definition D add no reverse arrow.** The retained factor `e^(16κ̄)` enters `C_R^WF`, then `c_ν`.
Finally `s_k=(A₁/C₀)(log θ_k)^(p₀−q)` tends to zero, so row 22 enforces `s_k<c_ν/2`.
For row 2a, fix window enlargement ratios first and use the `M`-cube parameter grid in row 12.
Rescaling lengths by `M` leaves cubical counts unchanged; old-to-current rescaling contracts lengths. Thus the fixed-ratio rule gives hull/base envelopes before `L` and the rates. This is the geometric inference used here; UM explicitly fixes its collar widths independently of `L` (SA 14418).
The parameter-count lower length `ℓ_P` need not equal the actual cube side `M`.
This makes explicit the supplied partition choice; identifying parameter cubes with the smaller walk cells would not justify this order.
WF7's long-member coefficient is `b₁κ_far/M`; it supplies no new floor on `M`.

Apart from the flagged budget, dependencies are earlier or resolved by the displayed windows and within-row orders.
Smallness estimates and the geometry/response premises remain separate obligations.

## Result

A consistent order is displayed **conditionally on an early uniform UM cost envelope**; the supplied dependencies do not yet give a complete acyclic order.
The remaining cycle is `κ̄ → M → C₀^UM → Θ → κ̄`. The budget-first rule above would break it, if supplied with that uniformity.
The literal `2.8-T` conflict `r → d₀ → r` is removed by moving `d₀`; the flow cycle `γ → (λ_♯,B_♯) → γ` is already cut by SA's weak frame constants.
This is not nonexistence of suitable constants, a proof of the estimates, WF7(C), or C4 invariance.

