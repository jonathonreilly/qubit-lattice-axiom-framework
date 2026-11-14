# Repo search

Research note for FINISH row 865, `gap-sdcyl-ca-astra`; repairs the complete-account port requested after row 848. No scientific or audit status is granted.

- READ: target prior-work file `library/prior/gap-sdcyl-ca-astra.md` is absent in this checkout (checked before any other source).
- Final disposition: the conditional lattice-kernel port and corrected witness implication are written below. The flux estimate and imported analytic suppliers remain OPEN.

Source credit: Ethan Sussman and Levent Alpoge; Claude and Codex are credited as authors of their supplied outline/account text. Exact source revisions and line ranges are recorded below.

Search-hit path prefix: `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. The hit files are `PROOF.md:7453`, `PROOF_session21_snapshot.md:5928`, `PROOF_session22_snapshot.md:5961`, and `PROOF_session23_snapshot.md:6058`, on pr/10114 and pr/10133. The primary statement is compared in Step 1; snapshot matches are retrieval hits, not independent evidence. The direct local predecessors are `library/gap-e17phys-opus.md`, `library/gap-e17phys-check-astra.md`, `library/port/p3-free.md`, and `library/port/p9-witness.md`.

## Step 1 — source and prior-work boundary

READ: this checkout is `379e03fb58e78e198b007b6e4752d2e379b3e153`. GOAL.md and FINISH.md 52–74, 320–351 were read. The workflow is absent in this sparse checkout; its current map and RULES/SETTINGS/PROCEDURES were read through `origin/main` in the explicitly requested full repository. The supplied `/Users/jonreilly/ym4d-lead/sa` directory has no Git metadata; the requested revision `31a47c543775` is supplied provenance, to be checked against the existing source hashes.

Searches on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`, over `*.md` and `*.tex`, include `SD-cyl|E17-phys|sdcyl|Proposition W-phys|background.curvature kernel`. They returned no exact SD-cyl/E17-phys port. The background-kernel hits are the older soft-route `PROOF.md:7453` and its session21/22/23 snapshots on pr/10114 and pr/10133. READ: pr/10114 `PROOF.md:7444–7485` defines the linear response `K=(1-d C^0 d*) iota`, proves its algebraic response and operator upper bounds, and explicitly describes measured row norms. This is a one-level soft-constraint response operator, not the squared retained covariance kernel or a cylinder witness lower bound. No result from it is imported. An initial unqualified `W-phys` query and a broad kernel/normalizer query hit their output caps with unrelated results; neither supports an absence claim. More precise method searches are recorded below when complete.

READ: `gap-e17phys-opus.md:1–257`, especially 123–141 and 147–199; `gap-e17phys-check-astra.md:99–148`. Reuse row 844's tent, Lemma W, rectangular floor argument and trace-limit passage. Row 848 already checks these implications and supplies the complex rectangular chessboard dictionary. They are not new work here. The port still to match is the complete-account reference kernel, transfer, depth floor and error budget. An exact-label search of `open-registry.md`, `open-core.md`, `l17c.md`, and `port-map.md` returned no SD-cyl/E17-phys/sdcyl owner; nearby ownership will be compared by statement, not just label.

READ: CA-I 2715–2826 states `S_2=Z b_0 K_s^star(1+R)`, `Z=zeta'_(K-s)^2 g_(K-s)^4`, `|R|<=1/2`, and `c_K ||f||inf ||h||inf <= K_s^star <= C_K ||f||inf ||h||inf`. It requires all three depth floors and `K-s>=k_W`, and provides only `zeta' in [2/3,4/3]`. The lattice kernel is retained in this port. No continuum replacement or claim `zeta' -> 1` is made.

OPEN at this checkpoint: match the complete account's rectangular transfer and remaining half-error reserve. The detailed kernel lemma is in CA-II, not CA-I: `8.1:lem-kernel-bounds`, CA-II 69925–70152, found through `sa-index/ca-full/index.tsv`. Its explicit hypotheses (h1)–(h3), including the free comparison, stay premises; the index label PROVED is not an unconditional certification. Its raw constants and the theorem's absorbed shape constants must not be silently identified.

## Step 2 — additional prior work and the account's reserve

READ: the completed precise method search `8\.1:lem-kernel-bounds|signed translation averages|scalar transfer estimate|finite-reference-normalizer|curvature two-point witness|background.curvature kernel`, on all five refs above, returned only the same soft-route curvature-operator hits. A local label search found **existing, directly relevant ports**:

- `library/port/p9-witness.md:1013–1091`: the signed-translate bound with the exact `C_T`, the reference-torus quarter-error, and the transfer quarter-error. It also records H-depth and the strict coupling-ceiling endpoint qualification. These are prior results, not new derivations here.
- `library/port/p3-free.md:166–184` and its kernel-bounds section: the background Gaussian identification and kernel estimates are conditional on their named free-minimiser/comparison premises. Attachment-point kernels there are not silently substituted for barycentre observables here.
- `library/open-registry.md:32–34` separates the all-state/component vanishing bound, a reflected witness on a chosen component, and blocked-observable NT2. None is the requested finite spatial-cylinder even-sector ratio. The exact CA kernel/volume-transfer labels have no separately owned registry row. Upstream witness suppliers remain with their existing owners; this note only ports their consequences.

READ: CA-II `8.22:cor-transfer-depth-floor`, 142316–142515, uses a **reference error at most 1/4**, then the same reference kernel throughout. Its main term is

```math
\mathfrak M^\star=\zeta_{K-s}'^{\,2}b_0g_{K-s}^4\mathcal K_s^\star,
\qquad
\mathfrak M^\star\ge\frac49 b_0c_{\mathcal K}\bar x_s^{-2}
\|f_1\|_\infty\|f_2\|_\infty,
\quad \bar x_s=g^{-2}+B^\sharp(s+1).
```

The tail floor `s_T(g)` requires, for every depth `v>=s_T(g)`,

```math
LC_W(v)L^{-v}\le\frac1{40},\qquad
C_T(g)L^2C_W(v)^2L^{-2v}
\le\frac19b_0c_{\mathcal K}\bar x_v^{-2}.
```

With `s=s(d)>=s_T`, minimality gives `d<LC_W(s)L^{-s}`. Therefore the transfer cost `C_T(g)d^2||f_1||inf||f_2||inf` is at most `M^star/4`. This is an additive reserve: `R=R_ref+(S_target-S_ref)/M^star`, so `|R|<=1/4+1/4=1/2`. It does not multiply two relative errors. READ: CA-II 142516–142546 explicitly leaves the optional replacement of the reference kernel by the target-torus kernel unproved. That replacement is not needed.

The source constants to be ported are (CA-II 141540–141583, 141994–142100):

```math
Q_\star=\exp\{(E_+^\sharp+C_{\rm low}+\bar\delta_{\rm vac})\ell_c^4
                    +4C_{\rm face}(1)\},
\quad
C_{\rm VT}=2\log2\,(2Q_\star+2)^2(2\mathfrak r/\varrho)^2,
\quad
C_T=5^4c_\Gamma^{-1}(40M/\vartheta)^2C_{\rm VT},\quad c_\Gamma=32^{-4}.
```

Here `ell_c` is the least power of `L` at least 32 and `mathfrak r` is the source-radius convention (1 or 2), fixed once. None depends on the cutoff or the target periods. PROVED below will mean a written implication from these named account inputs and the previously proved transfer-operator lemma, not that the account's unresolved suppliers have been settled.

## Step 3 — rectangular transfer with the complete-account constants

**PROVED, conditional port.** Retain hypotheses (a)–(f) of CA-II `8.22:thm-volume-transfer` (141540–141583), including the reference sourced energy, face estimate, zero-source stability and cubic vacuum-density comparison. Retain the transfer-operator input of row 844 Lemma W. Let

```math
m_\star=m_{\mathbb T}(g_-(g)),\qquad
\ell_\star^{\rm CA}=2L^{m_\star},\qquad
\mathcal T=\prod_{\mu=0}^3\mathbb R/(q_\mu\ell_\star^{\rm CA})\mathbb Z,
\quad q_\mu\in\mathbb N.
```

All periods are at least the reference period and are even multiples of `ell_c`. For real Lipschitz tests in one radius-one ball, the conclusion of that theorem holds between `T` and the reference torus, with its **same** `C_VT`.

Here is the dictionary and the only geometry extension. Write `V_star=(ell_star^CA)^4`, `V_T=prod_mu(q_mu ell_star^CA)`, and `E_star` for the account's zero-source vacuum constant.

1. **Floor (reuse row 844 Lemma F, with CA notation).** For any cubic account torus of side `H` larger than all four periods, positivity of each directional transfer operator gives
   `log Z_T(0)/V_T >= log Z_H(0)/H^4`. The inequality uses monotonicity of `(Tr T^n)^(1/n)` for all positive integer exponents; no divisibility of `H` by the rectangle's periods is required. CA's lower stability and cubic density comparison then give

```math
\log Z_{\mathcal T}(0)\ge V_{\mathcal T}
\left(E_\star/V_\star-C_{\rm low}-\bar\delta_{\rm vac}\right).
```

2. **Complex chessboard and pressure (reuse row 848 §§9–10).** The complex cell lemma CA-II `6.2:lem-chessboard-estimate` uses even cell counts one coordinate at a time. Replace the equal counts by `n_mu=q_mu ell_star^CA/ell_c` and the cell number by `J_T=V_T/ell_c^4`. Reflections conjugate the source in odd cells. The placement margin is unchanged. Thus for the account's mirror-periodic `W_z`,

```math
|M_{\mathcal T}(z)|\le
\left[Z_{\mathcal T}(W_z)/Z_{\mathcal T}(0)\right]^{1/J_{\mathcal T}},
\qquad
0\le Z_{\mathcal T}(W_z)\le Z_\star(W_z)^{V_{\mathcal T}/V_\star}.
```

The second inequality is already **explicitly rectangular** in CA-II `8.22:lem-trace-subadditivity`, 140995–141056, proof through 141255. Apply its one-coordinate inequality with the separate factors `q_mu`. Their parity does not matter: every intermediate partition function is nonnegative, and each integer power is increasing on `[0,infinity)`. This matters for the consumer's doubled sides.

3. **Common counterterm.** The reference upper stability bound is
`log Z_star(W_z) <= E_star+Re E_source,star(W_z)+E_+^sharp V_star`.
Combine it with steps 1–2. The two `E_star` terms cancel exactly, giving

```math
\log|M_{\mathcal T}(z)|\le
J_\star^{-1}\operatorname{Re}\mathcal E_\star(W_z)
 +(E_+^\sharp+C_{\rm low}+\bar\delta_{\rm vac})\ell_c^4.
```

The counterterm `E''` is formed **only on the reference torus**, as in CA-II 141721–141783. Its holomorphy, source radius and face comparison therefore do not change. That comparison costs at most `4 C_face(1)`. Consequently `h_T=e^{-E''}M_T` and `h_star=e^{-E''}M_star` both equal one at zero and obey `|h|<=Q_star` on the same domain `sum |z_i| ||F_i||sharp < varrho/mathfrak r`. No sourced RG on a rectangle is assumed. The account's Schwarz–Cauchy argument now gives the same `C_VT`; the mixed derivative of `E''` cancels.

4. **Signed translates (reuse P9, 1013–1049).** The bare rectangular Wilson measure is invariant under simultaneous `a_K Z^4` translations. The reference measure is too. All packed tests fit in a radius-one ball on both tori. The bilinear difference therefore satisfies the exact hypotheses of CA-II `8.22:lem-signed-translates`. With the same packing and norm bounds, its two-source corollary gives

```math
|S_2^{\mathcal T}(f,h)-S_2^\star(f,h)|
\le C_T(g)\mathsf d^2\|f\|_\infty\|h\|_\infty
\quad (a_K\le\mathsf d\le1/40).
```

This proves the rectangle-to-reference estimate without any period-dependent loss. It ports the already existing CA/P9 argument, with the already existing rectangular floor/chessboard dictionary from rows 844/848. Its analytic antecedents remain named inputs.

## Step 4 — (SD-cyl-CA), depth admission, and the half-error

**Fixed choices.** Set `vartheta=1/300`, as in row 844. Fix the complete-account auxiliary parameters, including `q>=21 p_0+1`, its source radius, and a positive coupling **strictly below** `gamma_W^VT`. This uses P9's endpoint qualification; alternatively require the reference-horizon inequality explicitly at the endpoint. Fix a positive separation `d` with `s=s(d)` satisfying

```math
s\ge\max\{s_W(g),s_{\rm vol}^{\star}(g),s_T(g)\},\qquad
s-r(s)\ge s_*,\quad s\ge m_{\mathbb T}(g),\quad
2B^\sharp(r(s)+1)\le\underline x_s.
```

The last three inequalities are P9's **H-depth**, already identified there. Do not infer their upward closure from the printed first-admissible minimum defining `s_W`. One may choose `d` using a tail where they all hold; CA-II 69049–69069 proves eventual satisfaction, and `s(d)->infinity`. The quarter-error reference theorem and all its analytic hypotheses are retained. Below the reference horizon its volume floor is zero; keeping `s_vol^star` in this displayed admission also respects CA-I's wording.

Choose `K_0` before any cutoff so that, for all `K>=K_0`,

```math
K-s\ge k_W,\qquad a_K=L^{-K}\le\min\{\mathsf d/8,\ \vartheta^2\mathsf d/32\}.
```

The second bound also pays the continuum-to-discrete test admission of CA-II 68788–68795: a continuous class member at shape `vartheta` becomes a discrete member at shape `vartheta/2`. It implies `eta/rho=a_K/d<=1/6`, the mass-upper-bound qualification already repaired in P3. All kernel, extraction and transfer constants must be chosen for this admitted shape. In the formulas below `c_K` and `C_K` mean **the constants in CA-I's displayed sup-norm sandwich**, with these fixed shape choices, not the unspecialized raw constants of CA-II Lemma 8.1.

**(SD-cyl-CA), PROVED as an implication.** For every first-passage datum `0<g_0<=g_-(g)`, `K=K(g_0,g)>=K_0`, and every spatial cylinder with physical periods that are integer multiples of `ell_star^CA`, for every pair in CA-I's class `T(d;vartheta)` supported together in one ball of radius `5d`,

```math
S_2^{\rm cyl}(f,h)=Z_{K,s}\,b_0\,\mathcal K_s^\star(f,h)(1+R_{\rm cyl}),
\quad Z_{K,s}=\zeta_{K-s}'^{\,2}g_{K-s}^{4}>0,
\quad |R_{\rm cyl}|\le\frac12,
```

```math
c_{\mathcal K}\|f\|_\infty\|h\|_\infty
\le\mathcal K_s^\star(f,h)
\le C_{\mathcal K}\|f\|_\infty\|h\|_\infty.
```

The kernel and `Z` are read on the same reference run. They may depend on `K`, but their comparison constants do not. No cylinder free kernel is introduced.

**Proof.** For the finite cylinder with temporal period `q ell_star^CA`, Step 3 gives the source's `C_T` bound. The reference witness has error at most `1/4` (CA-II 142328–142346, with its explicit antecedents). Step 2's depth inequalities make the transfer error at most `M^star/4`. Thus the finite cylinder has the displayed reference-kernel law with error at most `1/2`, uniformly in `q`.

Now hold `K,g_0`, the spatial box and the tests fixed and let `q` tend to infinity. The local observables and their product are bounded at this cutoff. Row 844 Lemma W(i), including its trace-norm ground-state limit, passes each of their three moments to the cylinder; hence their covariance converges. The reference main term is positive and independent of `q`. Its closed relative interval `[1/2,3/2]` is preserved. This proves the cylinder formula. It uses no convergence rate uniform in `K` and exchanges no two limits.

**Kernel comparison used, and its scope (READ).** CA-II 69925–70152 proves the kernel sandwich conditional on (h1)–(h3). It sums squared curvature entries, whose signs before squaring are irrelevant. Its raw mass constants are `c_0=2*10^(-8)/pi^4` and `C_0=36 C_u^2`; its sup-norm version includes the factors `vartheta_discrete^2` and `100`. Thus those raw symbols are not numerically interchangeable with the absorbed `c_K,C_K` above. The lower comparison (h3) is exactly

```math
\eta^{-8}k(x,y)\ge\frac13\sum_{\mu<\nu,\rho<\sigma}
\langle F_{\mu\nu}(x-y)F_{\rho\sigma}(0)\rangle^2
=\frac{2}{\pi^4|x-y|^8}
```

at `K-s>=k_W` and `|x-y|>=C_0^ker` in witness-cell units. P3 already ports this implication. The finite-cutoff diagonal positivity bound with a factor `eta^8` is insufficient for the present purpose; the two separated-support constants are essential. **ARGUED/OPEN upstream:** the quantitative comparison is a named hypothesis here, not a newly supplied proof. CA-II 145220–145222 leaves the statement and proof of its continuum-kernel lemma unwritten. This port does not repair that upstream supplier or identify attachment-point and barycentre kernels on its own; it consumes CA-I's stated witness formula for its stated observable.

## Step 5 — the tent ratio, W-phys-CA, and corrected E17-phys

**PROVED given (SD-cyl-CA).** Keep row 844's tent

```math
f(x)=(r-|x-x_0|)_+,\qquad r=\mathsf d/4,
\qquad t_1=\left\lceil\frac{3\mathsf d}{2a_K}\right\rceil,
\quad t_2=2t_1,\quad h_i=\tau_{t_i a_K}f.
```

Choose `x_0` on a lattice time-reflection plane. Row 844 already proves its mass, Lipschitz, centre-flip and slab-reflection properties. CA-I 2756–2763 uses the same continuous test class. In particular `||f||inf=||h_i||inf=r`, `Lip f=1` and `int f=pi^2 r^5/10`; the latter exceeds `(1/300) r d^4`. If `sigma=t_1 a_K`, then

```math
\frac32\mathsf d\le\sigma<\frac32\mathsf d+a_K,\qquad
\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}h_1)
=\sigma-\mathsf d/2\in[\mathsf d,\mathsf d+a_K),
```

```math
\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}h_2)
=2\sigma-\mathsf d/2\in[5\mathsf d/2,5\mathsf d/2+2a_K).
```

Both are in `[d,6d]`. Both pairs fit in a radius-`2d` ball. Therefore the **actual reference kernels at these two separations** obey

```math
\mathcal K_s^\star(f,h_2)\ge c_{\mathcal K}r^2,
\qquad
\mathcal K_s^\star(f,h_1)\le C_{\mathcal K}r^2,
\qquad
\frac{\mathcal K_s^\star(f,h_2)}{\mathcal K_s^\star(f,h_1)}
\ge\frac{c_{\mathcal K}}{C_{\mathcal K}}>0.
```

This uses the class-wide lower bound, not a new inverse-eighth-power assertion. In particular no extra `(2/7)^8` is multiplied into it.

Let `w` be the tent's slab width, `u_i=t_i-w`, and `G` be row 844 Lemma W's connected cylinder function. The existing slab calculation gives `w<=d/(2a_K)+3`, so `u_1>=0` at `a_K<=d/8`. By (SD-cyl-CA), with **one common** `Z_{K,s}`,

```math
\frac{G(u_2)}{G(u_1)}
=\frac{\mathcal K_s^\star(f,h_2)}{\mathcal K_s^\star(f,h_1)}
  \frac{1+R_2}{1+R_1}
\ge \rho_{\rm CA}:=\frac{c_{\mathcal K}}{3C_{\mathcal K}}>0.
```

The factor `1/3` is exactly `(1-1/2)/(1+1/2)`. The same `zeta'`, running coupling and `b_0` cancel; using the separate extremal bounds for `zeta'` would lose an unnecessary factor four. A nonempty witness class implies `c_K<=C_K`, so `0<rho_CA<=1/3<1`. Lemma W also gives `G(u_2)/G(u_1)<=1`.

**Proposition W-phys-CA.** Let the physical sides of the spatial box be multiples of `ell_star^CA`, and let `A=n_A a_K>=2d`, with integer `n_A`. At the admitted first-passage cutoffs,

```math
S_{\rm ev}(n_A;B)\ge\rho_{\rm CA}^{\,2A/(3\mathsf d)}.
```

**Proof.** The two gaps differ by `u_2-u_1=t_1`. Since `t_1 a_K<3d/2+a_K<=2d`, one has `n_A>=t_1`. The already proved Lemma W(iii) applies, since `G(u_2)>0`, and gives

```math
S_{\rm ev}(n_A;B)
\ge\left(\frac{G(u_2)}{G(u_1)}\right)^{n_A/t_1}
\ge\rho_{\rm CA}^{\,n_A/t_1}
\ge\rho_{\rm CA}^{\,2A/(3\mathsf d)}.
```

The last direction follows from `t_1 a_K>=3d/2` and `rho_CA<1`. This proves the proposition by applying the existing spectral lemma; it does not reprove that lemma. Its even-gap consequence in physical units is

```math
m_{\rm ev}^{\rm physical}(B)
\le\frac{2}{3\mathsf d}\log\frac{3C_{\mathcal K}}{c_{\mathcal K}}.
```

It is an upper bound on the even gap, not a positive lower gap.

**Corrected (E17-phys-CA), a hypothesis still OPEN.** Fix the parameters above, one physical size `A=2L^m>=max(ell_star^CA,2d)`, and `K_F>=1`. For every admitted first-passage datum with `K>=K_0`, at all three consumer shapes

```math
(n_A,n_A,n_C,n_D),\qquad
(n_C,n_D)\in\{(n_A,n_A),(2n_A,n_A),(2n_A,2n_A)\},
\qquad n_A=A/a_K,
```

require

```math
\boxed{\quad Q_F\le\frac{K_F}{8}\rho_{\rm CA}^{\,A/(3\mathsf d)}
       =\frac{K_F}{8}e^{-\Lambda_{\rm CA}A},\qquad Q_F<\frac1{192},\quad}
\qquad
\Lambda_{\rm CA}:=\frac{1}{3\mathsf d}
                     \log\frac{3C_{\mathcal K}}{c_{\mathcal K}}.
```

This is an explicit rate in terms of the account's two fixed kernel constants. It is independent of `K,g_0` and the spatial/time lattice sizes. No numerical values for those analytic constants are supplied or inferred.

**Corollary, PROVED given (SD-cyl-CA) and (E17-phys-CA).** Each consumer spatial period is `A` or `2A`, hence a multiple of `ell_star^CA`. The proposition gives `sqrt(S_ev)>=rho_CA^(A/(3d))`. Consequently

```math
8Q_F\le K_F\rho_{\rm CA}^{\,A/(3\mathsf d)}
       \le K_F\sqrt{S_{\rm ev}(n_A;B)},\qquad Q_F<1/192.
```

This is row 844's consumer (FQ) with `K(n_A)=K_F`, equivalently `p_1=0`, `C_1=K_F`. The exponent `A/(3d)` survives the port. Its base and rate change from `(2/7)^8/3` to `c_K/(3C_K)` and `Lambda_CA`. The flux estimate (E17-phys-CA), the glue estimates and a mass gap are not proved.

## Step 6 — disposition and precise remaining scope

**Answer to the port question.** The complete account's **lattice-kernel version** supplies the consumer-strength cylinder witness, conditionally on its named reference-witness and source-transfer premises. The corrected base is `rho_CA=c_K/(3C_K)`, and the corrected (E17-phys) rate is `Lambda_CA=log(3C_K/c_K)/(3d)`. No extra rectangle or cylinder estimate is left over from this port. The complete-account implication includes P9's existing admission qualifications; it is not a proof that all the account's premises hold.

The literal row-844 continuum-normalized (SD-cyl), with `K_free` and error at most `1/2`, is a stronger identification. It has **not** been obtained from the two comparison constants. A precise sufficient missing statement for that identification is the following uniform relative comparison, for the actual reference kernel and the same admitted tests and cutoffs:

```math
\left|\frac{\mathcal K_s^\star(f,h)}{6\pi^{-4}\mathcal K_{\rm free}(f,h)}-1\right|
\le\frac1{16}.
```

It must include the observable's evaluation convention. With that statement and the source's stronger transfer floor (replace `9` by `18`, CA-II 142516–142605), the lattice-kernel error is at most `1/4+1/8=3/8`. Multiplying by the comparison gives total continuum error at most `3/8+(11/8)(1/16)=59/128<1/2`. Thus the missing comparison is explicit; a loose two-sided sandwich alone does not prove it. This optional supplier belongs to the existing kernel work. It is not needed for W-phys-CA or the corrected (FQ) implication, and is not attacked here.

| Mark | Exact content |
|---|---|
| READ | CA-I's lattice reference-kernel witness clause and class, 2715–2826. |
| READ | CA-II's conditional kernel bounds, 69925–70152; volume-transfer statement and argument, 141540–141852; short-distance corollary, 141994–142100; reserve and reference transfer, 142164–142515. |
| PROVED, conditional | Rectangle-to-reference transfer with the same `C_T`; (SD-cyl-CA) after the quarter-plus-quarter reserve and fixed-cutoff cylinder limit. |
| PROVED, conditional | Tent kernel ratio `>=c_K/C_K`; covariance ratio `>=rho_CA`; W-phys-CA and corrected (E17-phys-CA) imply (FQ) with `K=K_F`. |
| ARGUED | Availability of the imported analytic reference-witness and transfer premises, with exactly their existing upstream qualifications. This note is an unchecked research port. |
| OPEN | The kernel-comparison/extraction/source suppliers retained in P3/P9; the literal continuum replacement above; (E17-phys-CA) as a flux estimate; the glue estimates and the mass-gap problem. No status is granted. |

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account and its kernel, transfer and reserve arguments. Tadeusz Balaban is credited for the minimiser/RG inputs as quoted in CA-II 69927–69929 and 70004–70016; `library/lit-balaban.md:1–43` is a secondary search record, not a firsthand reading of his papers. Reused local work is `port/p3-free.md:330–575`, `port/p9-witness.md:1013–1091` (Codex), row 844 (Claude Opus, tent and Lemma W), and row 848 (Codex, the rectangular dictionary). No independent check of this new note has run.

## Source and recovery record

Author: Codex, this session. Task: FINISH row 865, requested as an Astra/xhigh port. Only this output file was written. No ledger, registry, FINISH row, branch, commit or remote was changed. No computation discharged any mathematical step. The source/hash and text checks below are bookkeeping only.

The supplied source bytes match the hashes recorded in row 848 for revision `31a47c543775`:

| Source under `/Users/jonreilly/ym4d-lead/sa/` | SHA-256 |
|---|---|
| `YM4_sketch_500.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `theorem_0_complete_account_raw_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `theorem_0_complete_account_raw_II.tex` | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

Search refs resolved to `origin/main=f07a5b9fc623c34517f8915bb2d3ab9cfe57ce78`, `pr/10114=f76f6c649cff7dffbab664d8976e680e8f287fe9`, `pr/10133=89faef229ff6e6bde42baad15ed8270c2f4087d8`, `pr/10134=1e70c7211a2cdbc39001e619f1dd89db45e25851`, and `pr/10141=c73ad7b177d94f89ff37b77386936e3d52b48b05` at verification. Capped/noisy exploratory searches were not used as evidence of absence. The precise completed searches and exact relevant statements are recorded in Steps 1–2. `library/prior/repo-search-2026-11-08.md` is a retrieval record for older, different targets; its TPI/free-background distinction and soft-route lineage agree with the bounded source hit read here.

Index consultation: `sa-index/README.md`, chunk-24's kernel and transfer rows and neighbours, `obligations.md:1314–1325,1590–1598`, and `ca-full/README.md` plus the surrounding index rows for Chapters 6.2, 8.1 and 8.22. The outline was used only to confirm the different comparison/reserve route at SA 26054–26066, after the index lookup. The proof above uses complete-account locators. Additional bounded primary reads are CA-II 68722–68795 (discrete witness admission), 68978–69069 (actual depth conditions), 61205–61415 and 108696–108756 (chessboard), 140995–141275 (rectangular pressure), 141276–141347 (vacuum-density premises), 144388–144445 and 144797–144835 (reference witness antecedents), and 145218–145228 (unwritten continuum-kernel lemma).

Recovery: the mathematical port is complete at the stated conditional scope. The next useful action is the lead's check of the new rectangular application and ratio, retaining P3/P9's supplier boundaries. There is no reason to rederive Lemma W, the complex chessboard, the signed-translate estimate or the quarter-error arithmetic. The unproved flux and upstream kernel tasks keep their existing owners.

RESULT: PROVED as a conditional complete-account port: (SD-cyl-CA) with the reference lattice kernel and half-error yields rho_CA=c_K/(3C_K), S_ev>=rho_CA^(2A/(3d)), and corrected (E17-phys-CA) at rate log(3C_K/c_K)/(3d) implies (FQ) with cutoff-independent K_F; the literal continuum-kernel identification and the account's unresolved analytic suppliers remain OPEN, as do the flux estimate and glue estimates; no mass gap or scientific status is granted.
