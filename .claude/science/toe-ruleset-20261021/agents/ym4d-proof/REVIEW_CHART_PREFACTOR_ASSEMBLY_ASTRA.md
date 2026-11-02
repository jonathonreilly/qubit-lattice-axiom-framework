# Independent review of the assembled auxiliary-chart prefactor

The four source arguments establish one compatible finite-chart theorem on a
common construction and domain. I found no blocking mathematical error in this
assembly. The conclusion includes the full critical action and determinant,
the original-coordinate side/corner return, and the shrinking-chart regime.
It does **not** establish full SU(N), d=4 continuum existence or a positive
physical continuum mass gap; both targets remain **OPEN**.

This is one fresh, source-first mathematical review, with same-family review
disclosed. Astra/max was requested; the reviewer has no separate backend
attestation. The coordinator supplied published head
`a8c9365e5418845c2e2812ec321f4b52263717a6`. I performed no Git operation and bind
the actual source bytes below, rather than claiming independent verification
of that head. No source fix was requested or made.

| Source | Complete primary read | SHA256 |
|---|---:|---|
| [Shifted nonlinear return](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md) (SN) | 1–711 | `47423d924c938f627550ae592d4ef2d5ef3255d6f2e60b2ab0887b9a46425d1b` |
| [Critical determinant](CRITICAL_DETERMINANT_READER_ASTRA.md) (CD) | 1–397 | `bd33e000b839fe79e9a9bceda43d9b28b370e69717f0cedb8d1c14336642b755` |
| [Shrinking chart](SHRINKING_CHART_RETURN_ASTRA.md) (SH) | 1–247 | `9ae446ca746639ff77295f9da712f47e4be9d315d7c26e975535f1602321abfc` |
| [Critical action](CRITICAL_ACTION_READER_ASTRA.md) (CA) | 1–238 | `a466d55444d17c0d54fe9efecabc956ac5e3fcf9c61fdc0780d9248dabaf62fd` |

My [independent findings](checks/review_chart_prefactor_assembly_source_first_findings.json)
were frozen, SHA256
`5504527f6e2c3d99cf1c06bc240a51adbbaee8737d27cd41df1b3c8be9819f96`, before
opening any author receipt or read manifest. No earlier review file or root
integration evidence was opened. Historical review-status assertions embedded
in the mathematical sources were ignored as proof evidence. The subsequent
packet inspection confirmed the four source identities and did not change the
frozen mathematical findings.

The [bounded read manifest](checks/review_chart_prefactor_assembly_read_manifest.json)
records the actual source ranges, including the consumed CB, FU, PC, SA, NC,
NRR, SC and STEP55 arguments. PROCESS_LIGHT was read at **1–11**. Its length is
eleven lines. Search hits outside the recorded ranges are not claimed as full
reads. This review does not certify all older units, their reviews, the whole
PR delta, or every consumer discussed in SH section 4.

The precise assembled statement is as follows. Fix N≥2, odd L≥3 and the
admitted positive compact interval of κ. There exist one geometry-only R, one
patch/reader rule, fixed positive source radius ρ, and the positive constants
chosen below, independent of finite T≥2 and u. Write D=N²−1,
σ²=N/u, n=(3L⁴+1)T⁴ and d=Dn. The phase is the actual Wilson/normalized
paired-S4-prime phase in the fixed pinned-tree left chart, including its
finite-t denominator and Haar logarithm. No colour, root, crossing or harmonic
integration coordinate is deleted.

For the fixed-chart result, one can choose positive r_a, τ, δ_* and η once,
and then take u sufficiently large. For the shrinking result, fix any
prescribed real p(u)≥1 with p(u)→∞ and σp(u)→0. Set

```text
r_a(u)=σp(u),       τ(u)=cσp(u),
δ_*(u)=η(u)=κ_c cσp(u),
V_c=exp(v_c)Vbar_c, max_c ||v_c||HS<η(u),
δ_(Vbar)≤δ_*(u),   |ε_p|<ρ.
```

Then for sufficiently large u, uniformly in T and admitted real centers
(including their arbitrary compatible holonomies), the same actual FU solution
b=b_*(V,ε) and K_*=F_ε''(b) give the exact identity

```text
Z_a = h_N^n (2πσ²)^(d/2) z_(κu)^(-4T⁴)
      exp{ -σ^-2 Σ_(coarse P) Σ_(p∈D(P)) (1+ε_p) W(V_P)
            -Σ_S a_S -½Σ_S ℓ_S +Σ_Y H_Y } ≠ 0.
```

Here Z_a is exactly the integral over the product of original-coordinate HS
balls of radius r_a, z_t is CA10's probability-Haar normalizer, a_S is CA9's
critical-action correction, ℓ_S is CD19's full critical log-determinant, and
H_Y is SN29's returned nonlinear logarithm. The coefficients use connected
**original coarse-block** labels with all original data/source readers.
For μ=β/2 and β=(16R)^−4, their proven budgets are

```text
||a||_β ≤ C_H t_b²/(2σ²),       t_b ≤ τ/2,
||ℓ||_β ≤ C_lift+C_crit,
||H||_μ ≤ ε ≤ C_1 σ²+C_3 exp[-a p²/128]    (shrinking chart).
```

The letter a in the last exponent is SN2's positive precision bound, distinct
from both the fine field and CA9's scalar coefficients. All fixed constants
may be very large. The threshold u_0 depends on the prescribed p and its
eventual inequalities; there is no common numerical threshold for every
function satisfying those two limits.

I checked the joint construction, rather than intersecting unrelated theorem
domains. SN2–SN4 first fix the R-independent inverse-core bounds. SN3 chooses R
large enough for the lift tail and then recomputes the FU marked constants at
that R. FU18 also pays the stronger critical-tail cap. Positive preliminary
ceilings bar_τ, bar_ρ exist because N′(0)=D_H(0,0)=0. The local Cauchy constants
are fixed at those ceilings before r_a or r_max is chosen. The later choices
of τ, ρ, δ_* and η are restrictions of this construction; FU's contraction
from zero and uniqueness identify b on all overlaps.

CD needs no larger R than SN. Its determinant homotopy K_θ is an auxiliary
representation of the *lift determinant*, not a replacement physical
covariance. Its critical correction uses FU's actual G and Δ. CA builds H_s
from the same actual b atoms and original phase vertices. SN and SH use
precisely C=K_*^−1=P+E_lift+T_crit with the same lift core and both tails.
Thus the distinct homotopy representation in CD creates no inconsistency in
the covariance atoms used for the nonlinear return.

For SH, ρ can be fixed at bar_τ because the contraction and Hessian majorants
are monotone. SH1 chooses c>0 before u and pays both the chart/shift ratio and
the translation exponential. Choosing κ_c>0 with
`9 A_G g_*(1+ρ) κ_c≤1/4` gives the actual joint force estimate with
`δ_hat=δ_*+8η=9κ_cτ`; it implies t_b≤τ/2. It does not replace δ_hat by a real
δ_V. The remaining fixed CB/FU ceilings hold eventually as σp→0. Meanwhile
SH3 makes h_s and h_tr polynomials in p times exp(−ap²/64), with no residual
inverse power of σ. Thus p→∞ and σ→0 pay h_0, h_s and ε; σp→0 pays the chart
conditions. This establishes the moving-radius claim from the displayed
finite-parameter estimates, without assuming uniformity of an unspecified
fixed-radius threshold. No condition σp³→0 is needed for this theorem.

The complex normalizations were separately challenged. CB9 uses the doubled
holomorphic means, not complex conjugates of complex fields. STEP55 PR/NZ
(320–377, with corrections 673–678) recenters in SL(N,C) and obtains a
relative expectation `|Z−1|≤K_N ε_E<1` at fixed real t. Its centered logarithm
has a uniform bound; the uncentered vacuum remains explicit. This supplies
the fixed fine analytic domain for F. Haar's logarithm is zero-free on the
same sufficiently small chart. These arguments do not infer complex
nonvanishing from real positivity.

For the Gaussian, FU controls the Hermitian part under complex perturbations;
SN's pair masks satisfy Re C_I(s)≥3c0/4 and
Re C_I(s)^−1≥12a/25 on the analytic pair polydisc. Gaussian marginalization
uses the principal **covariance** and the holomorphic normalized density.
CD13 and CD18 fix TrLog through accretive homotopies. Since the reciprocal of
a right-half-plane eigenvalue stays in that half-plane,
TrLog(K_*^−1)=−TrLog K_* on these branches. Hence CD's inverse square root
is SN's Gaussian determinant branch, without a volume-dependent scalar
principal-log choice. Finally, SN's absolutely convergent gas identity itself
proves the returned chart integral nonzero on the joint complex domain.

The exact side and reader accounting survives the assembly. Direct
differentiation of the translated ball integral gives the minus outward flux;
tensoring gives every corner, one full D-colour sphere and one t_e integral
per selected side. Each flux contains b_e/σ. The top-form σ powers cancel
exactly. Before extending unused coordinates to the Gaussian marginal, SN
retains balls on every selected nonlinear field slot. It never evaluates a
local Taylor expansion on a bad-ball exterior.

Side flags, shared t_e and the presence/absence pattern of each vertex belong
to primitive components before taking the Gaussian forest. The core collars
make P[I] block diagonal at that stage. Both covariance tails appear in the
normalized-density loops/chains and the forest edges. Their complete labels
include remote diagonal readers. Expanding the Gaussian translation adds
its own b readers; SN24 pays their mark by rooting at an **actual side**,
with the flux budget and the second critical-field budget. The resulting
K_tr Q_s Dτ² has precisely the two powers of τ needed for SH3. Using a
generic weak vertex at that step would not establish the shrinking theorem.

The density-jet factorial remains a product over scalar coordinates. Its
child-leg recursion has an exponential cost linear in the component size.
Centered parity is used only for no-side nonlinear singletons. The positive
side-activity rescaling pays the whole side-containing family; it never
assigns it the singleton parity improvement. The four separate β/8 losses
pay primitive components, Gaussian attachments, full-reader regrouping and
the connected logarithm. CD and CA can be restricted from β to μ without
consuming a further margin. None of this imports the larger rates used by
older R-box or history consumers.

The assembled logarithm is not wholly small. On the shrinking domain,

```text
||a||_β ≤ (C_H c²/8) p²,
lift field-action budget ≤ C_W(1+ρ)(9κ_c c)² p²,
compact vacuum budget = 4 exp(β)|log z_(κu)|,
determinant budget = (C_lift+C_crit)/2.
```

CA7's minus sign follows from stationarity of the total action and the
weight s in `−∫_0^1 s b^T H_s b ds`; it does not assign stationarity to each
local vertex. CA11 retains every individual original fine Wilson source at
the lift. The remaining source plaquettes still enter b and H_s. The compact
vacuum has its exact real-u value and only the stated crude O(u) upper bound.
The determinant has an O(1) **per-block** bound; neither it nor the p² action
correction is an O(1/u) irrelevant remainder. The explicit h_N and σ powers
remain. The displayed combined identity uses no action/determinant/source
cancellation.

For derivatives, SH7 is valid on the half-size joint domain: coarse scalar
jets cost `(2D/η(u))^|α|`, original-source jets cost `(2/ρ)^|ζ|`, and the
factorials and complete marked norm remain. Consequently unscaled coarse
derivatives may grow as powers of (σp)^−1. Only after writing
`v=(σp)v_hat` do those powers cancel, leaving fixed v_hat radius κ_c c.
The small bound applies to H and its corresponding Cauchy estimates; applying
Cauchy to the full action or determinant uses their own larger budgets.
No differentiability or analyticity in u of an arbitrary p(u) is asserted.

After the source-first freeze I ran the independent
[exact symbolic checker](checks/review_chart_prefactor_assembly_identity_check.py).
Its [result](checks/review_chart_prefactor_assembly_identity_check.json) reports
19 exact identities passed and 13 sign/factor/order/power mutations rejected,
with all thirteen bound source/procedure files unchanged. It checks generic
noncommuting 2×2 inverse identities, the normalized Gaussian heat identity,
the action coefficient identity for a symbolic degree, the side σ powers,
the shrinking substitutions, the support loss, the full prefactor and the
scaled coarse radius. These are exact algebraic checks, not scientific
numerical experiments or a substitute for the analytic proof. No author
physics script was executed. The [criteria](checks/review_chart_prefactor_assembly_criteria.json)
were written before the checker.

One review pass was performed: zero blocking findings, zero source fixes and
zero unresolved findings within the assembled theorem above. Its proof
obligations are closed within the supplied finite one-step model and its
explicit admissible domain. There is no empirical fit or new physical
identification in this conclusion. Bałaban and Dimock retain the constructive
architectural credit stated by the sources.

The review does not establish equality with the original hard-cut transform,
G/Omega sectors, white cubes, history-dependent references or their
complementary integrals. It does not establish an effective RG step, repeated
RG contraction, non-freeness of a continuum limit, four-dimensional continuum
existence or a physical mass gap. These are remaining proof obligations,
not an impossibility result. No Nature-grade or retained status is awarded.

PR preservation, exact Git-head verification, publication bindings, combined
repository validation and audit compatibility remain with the coordinator.
They were outside this reviewer allocation; this report supplies a bounded
scientific source verdict, not those integration gates. No commits, pushes,
front edits, PR edits, audit/ledger writes, or additional workers occurred.

Recommendation: PASS WITH BOUNDED CLAIMS for the assembled auxiliary-chart
theorem stated here.

VERDICT: LAND
