# Check of gap-kernel-solve-astra62.md (FINISH row 1673)

Reader: Claude Opus 5.5, high effort, laptop subagent, FINISH row 1677, commit bced04268. Started 2026-11-28T09:47Z (`date -u`). Cross-provider reader: the row is by gpt-6.2-astra max. Hand arguments only. No numeric job, no Lean run.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, wrote the YM4 release. Tadeusz Bałaban developed the method. gpt-6.2-astra max wrote the checked row.

Read: the row in full; `Stage0.lean` L90-L110, L200-L245, L296-L312; RESULT texts of FINISH rows 677, 685, 691, 693, 820, 1386, 1502, 1672; parts of `library/gap-ds-gauge.md`, `library/gap-direction9-fable.md` §3 and `library/gap-mech-direction2-fable.md` 4.1. Not read: the release definitions of `IsInfiniteVolumeLimit` and `timeReflection`. They are not in this checkout.

## 1. The consumer: (2), (1), (3)

**(2) HOLDS.** I checked each count.
- A link with source x lies in a translate exactly when x is in its source cube. There are R^d such cubes. In each, the two exterior data agree, so one draw erases the difference.
- The two exterior data of a translate D differ only when x is outside the cube C but inside C enlarged by one in sup norm. Every source in a plaquette through the link is within sup distance 1 of x. The number of such cubes is (R+2)^d - R^d = s_R. The torus side above 2R+2 prevents wrap.
- The factor 2: a link source y in C and x in the enlarged cube have sup distance at most R, so u_y ≤ 2u_x.
- The difference at x persists in the V - R^d translates that do not contain x. Hence q = 1 - (R^d - 2 s_R Q_R)/V. The bound s_R Q_R ≤ R^d/4 gives q ≤ 1 - R^d/(2V).

A coupling within η of the infimum, η → 0, is enough. The row does not state measurability of the coupling family in the exterior data. Lemma 2 of `library/gap-ds-gauge.md` (row 691) supplies it.

**(1) HOLDS.** Lip_u(F) ≤ 2||F||: changes at sources outside A do not change F, and u = 1 on A. Each P_D preserves μ. On a finite torus, (2) gives uniform convergence, and the telescoping sum converges. A term μ((I - P_D)H · G) is zero when D contains no link of G. At most |Y| R^d translates remain. In each, the oscillation of H is at most Lip_u(H) times the sum of weights in D, which is at most 2dR^d 2^(-dist/R): the cube has diameter R - 1 and meets Y. Then Σ_h q^h / V ≤ 2/R^d. The product is 8dR^d|Y| ||F|| ||G|| 2^(-dist/R). The constant agrees.

**(3) and the Stage 0 quantifiers: HOLDS, with two inputs not read.** `ExpClusters` (Stage0 L230-L234) asks: for every Z, frequently in j, some C, for every n. (E) holds frequently with one b. So the good set is infinite and serves every Z. C_{Z,j} may depend on j, so the support allowance h_{Z,j} (of order 1/a_j) and |Y| (of order a_j^-4) are allowed. With a_j R_j = b, 2^(-(t/a_j)/R_j) = exp(-(log 2) t/b). This is correct.

`latticeU` is Re(pair) - |mean|^2 (L214-L221). The tests are real-valued. So pair = ν(Θ F̄ · τ_t F), and latticeU is the real part of a covariance exactly when ν_j(ΘF) = ν_j(F). Two facts carry this step: ν_j is invariant under the reflection that `timeReflection` induces, and `isLimit` gives convergence of cylinder integrals from tori. I did not read either definition. The row asserts both. A reflection through the plane t = -a/2 maps lattice sites to lattice sites. So it is a symmetry of each torus law, and it passes to weak limits. The row's remark that the odd-time shift makes the mirror integral does not carry any load. Translation by any integer multiple of a is a lattice symmetry.

**Relation to row 691 (PROVED here).** (E) implies hypothesis (W) of `library/gap-ds-gauge.md` with δ = 1/4: take k_z = Q_R. At most s_R boundary links of one direction touch the box, and N_R ≥ R^d, so Σ k_z ≤ s_R Q_R ≤ N_R/4. (W) allows unequal k_z, so (E) is the uniform special case of (W). The box conventions differ by a collar, which changes only constants.

## 2. The finite-coupling items

- **Seven-link transport: HOLDS.** If a cube vertex has exactly one coordinate zero, the incoming link on that axis is its only exterior link. With U_xy ↦ h_x U_xy h_y^(-1) and h = (u')^(-1)u at v, the incoming link goes to u h^(-1) = u'. Plaquette traces and Haar measure are invariant, so the push-forward is exactly γ^(ξ'). The change touches 2d - 1 interior links.
- **(4): HOLDS.** For SU(2), |½ Tr(A(f - f')B)| ≤ ||f - f'||_op. At most 2(d-1) plaquettes enter. The common mass is at least e^(-4(d-1)βδ).
- **Strong coupling: HOLDS.** D = 6(d-1). Two links share at most one plaquette. The mismatch probability is p_β = 1 - e^(-4β). The path-coupling recursion gives Q_R ≤ Dp_β/(1 - Dp_β), and the limit coupling exists by compactness. The regime is β below about 0.014 in 4D. The witnesses never enter it.
- **(5): HOLDS as stated.** Two internally disjoint d-move paths need d - 1 ≥ 2. 2c^d = √2. The count of endpoints is C(k+d-2, d-2). The paths stay in the box for 2k ≤ R - 2. The sum grows as R^(d-1). The maximizer argument gives c_eg → 1 (the phases of (p-1)I + V have product 1, so the maximizer is in SU(q)). The Villain and heat-kernel versions are as stated. I did not read Nowak-Sjögren-Szarek.
- **β = 1 row sum: HOLDS.** The staple sum is zero. The two densities are e^(±h) with equal normalizers, because U ↦ -U preserves Haar. The total variation is ∫|sinh h| / ∫cosh h > (1/4)/2, since E h^2 = 1/4 for a uniform unit quaternion.

**(iii) Ising-line example: HOLDS** for local models. Two spins have covariance e^(-a^2 n), and (1) at R = b/a would force the faster rate a log 2 / b for a < log 2 / b. So (E) ⇒ action clustering has no converse in general. It says nothing about Wilson SU(2).

## 3. The decisive item: is (E) false for a near-free field?

**PROVED (elementary).** Line (5) does not show that (E) is false. A certificate gives an upper bound on Q_R, and (5) is a lower bound on the certificate. A large upper bound says nothing about Q_R. The row says this itself ("The optimal transport for that tangential link stays open"). So (5) is a negative for the one-link method only.

**PROVED (elementary): the lower-bound tools.** Let S be the disagreement set of any coupling. Let O_k be functions of link sets S_k, with each link in at most m of the S_k. Then E|S| ≥ m^(-1) Σ_k TV(law_ξ O_k, law_ξ' O_k). By Kantorovich duality, W_H = sup(E_ξ' f - E_ξ f) over the f whose one-link oscillation is at most 1. Interior links have Haar marginals under both laws. So a useful O_k or f must be invariant under the interior gauge group: loop variables, or lines between frozen boundary vertices (the box vertices that touch exterior links).

**ARGUED: the naive obstruction fails.** "The classical response is nonzero on every link, so exact agreement fails on most links" is wrong. Couplings are random. Exact agreement is possible wherever the two local laws overlap. The response at distance n from the changed link is small against fluctuations of size β^(-1/2). Linearized at weak coupling, the response has potential a ~ δ n^(1-d) and curvature F ~ δ n^(-d).

**ARGUED: what the gauge-invariant lower bounds give.**
- Plaquettes. In U(1), the per-plaquette TV is about √β δ n^(-d). The sum over the box is O(√β δ log R). In SU(2), closed-loop variables in a region are invariant under a constant rotation of that region. The first-order term of the likelihood ratio, β⟨F_resp, F⟩, averages to zero over that rotation. So the loop TV is second order, O(βδ^2 n^(-2d)), and the sum is O(βδ^2).
- Lines between frozen vertices. These see the potential at first order. Their mean is suppressed by perimeter fluctuations, roughly exp(-c ℓ/β). Lines of length ℓ ~ n contribute about δ n e^(-cn/β) per dyadic scale. The total is O(δβ). Along the witnesses β_j ≈ 0.37 log R_j, so this is O(δ log R).

Every lower bound I can derive is polylogarithmic in R. This is far below the threshold R/32.

**Contrast (ARGUED): a scalar field fails.** For a 4D Gaussian free field with one changed Dirichlet value, the site marginals shift by δ H(x,y) ~ δ n^(1-d). The per-site TV sums to about c √β δ R, since Σ_x H(x,y) ~ R. So a scalar near-free field violates the analogue of (E) once √β δ exceeds a fixed constant. The gauge field differs in exactly one way: its potential is not a local observable. The scalar argument does not carry over.

**ARGUED: the upper bound side.** The only coupling I can build shifts link by link by a gauge representative of the response, with a conditional maximal coupling at each link. It costs about √β Σ_e |a_e|. By Stokes, a loop of length n must carry the flux n^2 · δ n^(-d), so every gauge representative has Σ_e |a_e| ≳ δR. This coupling therefore costs order √β δ R. That is above R/32 at large β. A nested maximal coupling over shells (Goldstein type) costs order √β δ R^(d/2), which is worse. Gauge freedom can beat both. On a chain of m links between two frozen vertices, the optimal cost is the TV of the holonomy, about √β h / √m, and not √β h. The shear along the gauge fibre moves the whole difference onto one link. Whether the same gain works in a 4D box is the open point.

**ARGUED: a second route to failure.** Q_R is a supremum over all exterior data, rough data included. Data at a degeneracy between two interior states would let one link flip a large region. I found no such data and no argument that excludes them. Row 691 names the same obstruction (`library/gap-ac-lat.md` 3.2).

**Verdict on item 2: OPEN.** The near-free field does not show that (E) is false. All the obstructions that do not depend on the gap are polylogarithmic. The scalar mechanism that would give order R is absent for a gauge field. But (E) is not shown plausible either. Weakest step: no coupling is known for a near-free 4D gauge field in a box with W_H = o(R) under a one-link boundary change. The only coupling I can build costs order √β δ R. A proof that the optimal W_H grows linearly would make the row a negative for its consumer. A coupling of cost O(polylog R) would push the decision to the physical scale b, where it depends on the gap.

## 4. Novelty

grep counts: 80 FINISH lines name Dobrushin, Shlosman, complete analyticity, Martinelli, Stroock or Zegarlinski.
- **Row 691 (`gap-ds-gauge`, Claude Fable 5.2 medium), checked in row 693 (Claude Opus 5.5 high, same provider; no statement fails).** It states hypothesis (W): per direction, Σ_z k_z ≤ δ N_R, where k_z is the expected number of disagreeing links in the cube for one changed boundary link z. Theorem W proves weak mixing, uniqueness, and the covariance bound for all bounded local F, G on Z^4 and on tori, at rate ln(1/δ)/(2(R+2)), with no use of the group. **Section 1 shows (E) is the uniform case of (W). So (E) and its consumer (1) have been on file since 2026-11-11.** Row 691 also found: plain (D) is not enough (Proposition H); (W) forces R ≥ ½ ln(1/δ) times the correlation length (Proposition B); strong mixing for cubes gives (W) (Proposition S); "(W) is the gap in finite form", and whether it holds for Wilson SU(2) beyond the one-link regime is untouched. Row 1673 ran closed-folder, so it could not see row 691.
- **Rows 677/685** (one-link complex Dobrushin bound, threshold about 0.102) and the repo note on main named in row 691 (one-link bound for β below 1/18).
- **Row 820 (numeric guide).** The typical one-link row sum is 2 to 4 at order-one β, and "most of the apparent single-link sensitivity is gauge direction". This anticipates the seven-link transport and the β = 1 check.
- **Row 1502 (literature).** The Dobrushin-Shlosman, Stroock-Zegarlinski and Martinelli-Olivieri criteria all need uniform boundary-conditioned influence.
- **Candidate d of row 1672 and (STEP) of row 1386 4.1.** Both are finite-size criteria whose threshold sits in a small box. Both rows call them "the seed in steps, no mechanism". (STEP) above first passage is equivalent to the target. (E) is the same kind of object: a finite-box input of gap strength with no method that reaches the witnesses.

What is new in row 1673: the bookkeeping to the exact Stage 0 quantifiers; the seven-link gauge transport; and the R^(d-1) lower bound for clipped positive path certificates at weak coupling, in Wilson SU(q), Villain U(1) and heat-kernel SU(2). My grep found no earlier row with that bound. The search was bounded and does not prove absence.

## 5. The six tests

- **(g1): HOLDS AFTER CORRECTION.** The failure line is the clustering consequence (1), not a U(1)-specific line. At fixed weak β, (1) for every R would give a transfer gap of at least (log 2)/R on local vectors. The Villain lift turns the Fröhlich-Spencer massless correlations into bounded local functions. The argument is sound. Correction: Fröhlich-Spencer covers Villain U(1). For Wilson U(1) the row needs Guth's massless phase (1980), or the claim should say Villain only. The test is cheap: any input that implies clustering passes it. It gives no evidence for (E) in SU(2).
- **(g3): HOLDS as the row admits.** Line (5) fires on weak 3D Villain U(1), which has a gap (Göpfert-Mack). So the path test does not separate gapped from gapless models, and (g3) rejects it. For (E) itself, (g3) is not run, because (E) on the 3D twin is open.
- (g2), (g4), (g5), (g6) are as the row labels them. (g5) is correct: R_j = exp((3π^2/11 + o(1)) β_j) from Stage0 L303-L309.

**The rule "equivalent to the seed is not progress".** A strictly stronger input with no method is not progress. It replaces the target with a harder target. Here the only methods are one-link certificates. They work only at β below about 0.014, where a gap is already known by strong-coupling expansion. They fail at weak coupling by (5). Row 691 recorded the same verdict for (W). The new pieces are reusable tools (the seven-link transport, the certificate bound (5)), but they do not move the crux.

## 6. Verdicts

| Item | Verdict |
|---|---|
| (2), (1) | HOLDS |
| (3) and `ExpClusters` | HOLDS, given reflection invariance of ν_j and the `isLimit` mode (not read) |
| Seven-link, (4), strong coupling | HOLDS |
| (5), β = 1 check | HOLDS, for certificates only |
| (iii) | HOLDS for local models |
| (E) false near-free? | OPEN |
| Novelty | (E) is the uniform case of (W), row 691 |
| (g1) | HOLDS AFTER CORRECTION |
| (g3) | rejects the path test only |
| Progress (seed rule) | none on the crux |

Ended 2026-11-28T10:00Z (`date -u`).

RESULT: Items (i)-(iii) HOLD; (E) is the uniform special case of (W) of row 691, so the consumer is on file; (5) refutes only the one-link certificate method, not (E); for a near-free 4D gauge field every lower bound I can derive is polylogarithmic in R while my best coupling costs order √β δ R, so whether (E) is false is OPEN (weakest step: no o(R) coupling); no progress on the crux.
