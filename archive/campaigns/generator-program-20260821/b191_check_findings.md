# Block 191 adversarial check — boundary modes and lapse/volume physicality

Date: 2026-08-25

Status: **COMPLETE — exact reconstruction and adversarial probes finished.**

## Scope and authority

This is a dry adversarial computation. No repository file, audit surface, commit, or branch is modified.

Construction authority:

- Block-190 note at commit `e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd`, also the tip of `origin/physics-loop/toe-axiom-closure-block190-width-family-transfer-monodromy-20260825`.
- The named note is tracked in that commit (SHA-256 `f9392f362084d2e8a407d8bde1b7ac555eda9884504efe501630bd011f3702e4`). It is not present in freshly fetched `origin/main` at `b11811704efa98a12272d572f666e530a807f6c1`; here “landed” therefore means landed on the block-190 feature lane, not merged to current `main`.
- Block-105 primary note and runner provide the exact volume law

  `B(c,v) = diag(v, v*g(c)^(-1), 1/v)`, with `g(c)=[[1,c],[c,1]]`.

  Thus, in corner order `(1, dx, dt, dx^dt)`,

  `B(c,v) = [[v,0,0,0],[0,v/(1-c^2),-vc/(1-c^2),0],[0,-vc/(1-c^2),v/(1-c^2),0],[0,0,0,1/v]]`.

At `c=5/13`, this gives exactly

- `B(5/13,1) = diag(1,169/144,169/144,1)` with entries `(1,2)=(2,1)=-65/144`;
- `B(5/13,4/5) = diag(4/5,169/180,169/180,5/4)` with entries `(1,2)=(2,1)=-13/36`.

All construction arithmetic below uses SymPy 1.14.0 over exact `Integer`/`Rational` entries and exact `QQ` matrix algebra. `nsimplify` is never used. Decimal root data, when reported, are evaluations of already exact characteristic polynomials and are not fed back into the construction.

## Rebuild contract

For even width `T`, the rebuild follows block 190 literally:

1. Sites are `(t,x)` in `Z_T x Z_4`, ordered by `idx(t,x)=4t+x`.
2. The staggered antisymmetric kernel has `eta_t=1`, `eta_x=(-1)^t`, and the temporal `-1` sign on the wrap edge `t=T-1`.
3. `d_K=P1*K*P0+P2*K*P1`, with degree `deg(t,x)=t mod 2 + x mod 2`.
4. `theta_s(t)=-t mod T`; `Ps` is its site permutation.
5. The site Hodge is the quarter-weighted sum of four-corner embeddings. Uniform profiles put `B(c,v)` on `t<T/2` and `P4 B(c,v) P4^T` on `t>=T/2`. A localized positive-half profile is extended to the image half by the `P4` image of its `thA_s(t)=-1-t` partner.
6. `A_s` retains raising entries whose endpoint times lie in `{0,...,T/2}`, excluding spatial edges inside the fixed slices `{0,T/2}`; `D_s=A_s-Ps*A_s*Ps`.
7. `Q=mH+HD_s-D_s^T H`, `G=Q^(-1)`, at `m=9/20`, `c=5/13`.
8. On the two-slice core `{t0,t0+1} x Z_4`,
   `K_c[a,b]=G[(t_b,x_b),(theta_s(t_a),x_a)]` and
   `L_k[a,b]=G[(t_b+k,x_b),(theta_s(t_a),x_a)]`.
9. `W=K_c^(-1)L_2`.

The implementation is an independent compact rebuild rather than an invocation of the block-190 runner. Exact source coefficients from the claims are used only after the computed polynomials have been produced.

## Findings log

### P3 and C1 — baseline/deep controls and T=20 boundary monodromy

**P3: CONFIRMED exactly.** This control was run before constructing either localized bump. At uniform `v=1`, the independent rebuild gives, at each of `T=20, t0=3,4,5`,

`charpoly(W) = (22569375 z^2 - 233631106 z + 22569375)^2`

`               * (39529825 z^2 - 109432706 z + 39529825)^2`.

The same deep polynomial is obtained at `T=16, t0=3`.

**C1: CONFIRMED exactly, coefficient for coefficient.** The complete T=20 scan is:

- `t0=2,3,4,5`: heavy squared times light squared, exactly as above.
- `t0=1`: light squared, one heavy copy, and

  `43033320714375 z^2 - 445467467014578 z + 48554286398375`.

- `t0=6`: light squared, one heavy copy, and the exact coefficient reversal

  `48554286398375 z^2 - 445467467014578 z + 43033320714375`.

- `t0=7`: light squared, one heavy copy, and

  `48554286398375 z^2 - 376762652339458 z + 35686537764375`.

Thus the asserted survival multiplicities, near/far reversal, and distinct `t0=7` boundary factor are all correct.

### C2 — validity boundary at the fixed slice

**Geometric rule CONFIRMED; factorization wording requires narrowing.**

- At `T=20, t0=7`, `L2` reaches times `{9,10}` and merely touches the fixed slice `t=10`. Its characteristic polynomial still splits completely over `Q` into the three C1 quadratics with multiplicities `(1,2,1)`.
- At `T=16, t0=5`, `L2` reaches `{7,8}` and likewise merely touches the fixed slice. It has the identical clean quadratic factorization.
- At `T=20, t0=8`, `L2` reaches `{10,11}` and crosses into the image half. Exact factorization over `Q` has degree pattern `(2,2,4)`, with the quartic irreducible over `Q`.
- At `T=16, t0=6`, `L2` reaches `{8,9}` and crosses into the image half. It again has exact degree pattern `(2,2,4)`, with the quartic irreducible over `Q`.

Therefore the crossing/touching distinction is real at both widths, and crossing destroys the clean all-quadratic bulk/boundary decomposition. The literal phrase “non-factoring over Q” is false if it means that the whole degree-eight polynomial is irreducible: it retains two rational quadratic factors. The exact observed signature is **failure to factor completely into rational quadratics**, through one irreducible rational quartic.

The quartic irreducibility has compact independent certificates: the primitive `T=16` crossing quartic remains irreducible modulo 11 and the primitive `T=20` crossing quartic remains irreducible modulo 67. Hence each is irreducible over `Q` by Gauss's lemma.

For reproducibility, the crossing factors are:

`T=16, t0=6`

```text
(4915198633954034404379551871841039937705816650390625 z^2
 -112874852084585346450639041406575208118805763962566850 z
 +231203888637988118031497061583958449578306131447267233)

(7150826592411983212052541532481884182259054931640625 z^2
 +79471775010869592479812354304373018145022057048504350 z
 -219137863411622100415064968179635525458341259865235983)

(1451330584858535643005188771481391428040252776744991791233804809247800449156784452497959136962890625 z^4
 +1288362643740249021246792777897236469051343690715527431556644530438133092398031085884571075439453125000 z^3
 +367744739008634135861980302745959130582707069108288316392808934961505664080126684688183144214012848081718750 z^2
 -6543219044150315494594445731618258274650161485170602047943143518217778784559566021548975077548439344191917000 z
 +28425669623405706497734352834869055147131933377921408600803451684132045060714676461925519047602401896296761969)
```

`T=20, t0=8`

```text
(7680524108987851686724379797917131403760880868734357944488525390625 z^2
 -849873564393807449298963160088865682185144860530896719173447961752850 z
 +1938079434072524341765647427343362583894959352970952675570632056657713)

(11173932150536421126001319929704957525901062508356888757476806640625 z^2
 +797677680181358255643822906952476939332234428244038036254673547690350 z
 -1919224977813000068952921727615740494965297409593861428868666724626463)

(376568924422926926557182889058677744549017257878250683095282754741572918724020031156483369338960898176082991994917392730712890625 z^4
 +35351560870414136726689605611279124684886301422387370449684879298235343437277819245758052646352770200895303641445934772491455078125000 z^3
 +1055143869757295369010940947744656861653991306929445753159225321835671081741578776036161423287009915249407778686700271616542636528633606718750 z^2
 -18771868931824492509018180878675105309928748781341397687269048752693571042178837080045574390351807252009551620341143431538208276209498904357000 z
 +81543623187369354144273415030736691027531181733639601521138833510329417322585496275269350577002934208506849125085845461889794698963131996160049)
```

### C3 — uniform volume dial at T=16, t0=3

**Exact polynomial and opposite motions CONFIRMED; quoted decimal ratio REFUTED.** The independent rebuild at uniform `v=4/5` gives exactly

`charpoly(W) = (31260675 z^2 - 302948719 z + 31260675)^2`

`               * (50327125 z^2 - 139773119 z + 50327125)^2`.

Both factors remain palindromic squared. Their exact `2 cosh(theta)` traces move in opposite directions:

```text
302948719/31260675 - 233631106/22569375
  = -2071568131893/3135706208125 < 0,

139773119/50327125 - 109432706/39529825
  = 710938392957/79576897760125 > 0.
```

Since `acosh(x/2)` is strictly increasing for these `x>2`, `theta_heavy` decreases and `theta_light` increases exactly. Numerical evaluation of the exact expressions gives

```text
v=1:   theta_heavy = 2.3276840295798963
       theta_light = 0.85067750602759454
       ratio       = 2.7362708113083575

v=4/5: theta_heavy = 2.2603806616534694
       theta_light = 0.85532928100072796
       ratio       = 2.6427023040867293
```

Thus the stated qualitative change and its exact coefficient data are correct, but `2.7361 -> 2.6449` is not the ratio implied by the displayed exact factors. Correct rounding is `2.7363 -> 2.6427` (four decimals).

### C4 and probes

#### C4 — localized bump on positive anchors `{3,4}`

**Core algebra CONFIRMED exactly; the complex-root gloss needs qualification.** The profile used is `v=4/5` at positive anchors `3,4`, `v=1` at the other positive anchors, and on the image half the `P4` image of the `thA_s(t)=-1-t` partner.

Exact covariance residuals are

```text
nnz(Ps H Ps - H)   = 0
nnz(Ps Q Ps - Q^T) = 0.
```

The irreducible factorization over `Q` is:

`t0=1`

```text
(1345846680 z^2 - 3973376087 z + 1478415455)
(24349745880 z^2 - 72455211787 z + 27315109075)
(65582920234848542400 z^4
 -1482708604980552127920 z^3
 +8535510836512821008759 z^2
 -1754062292362811443250 z
 +91505439094037734375)
```

`t0=3`

```text
(573370050 z^2 - 1494466969 z + 531948700)
(706236550 z^2 - 1827879139 z + 617587500)
(114565459508949172500 z^4
 -2050729233157099637100 z^3
 +9367229822132458083989 z^2
 -1702027048070120587200 z
 +78988021416996930000)
```

`t0=5`

```text
(988245625 z^2 - 2738989093 z + 1007414244)
(12768133475 z^2 - 35396157503 z + 12528288900)
(28294075662319609375 z^4
 -513108970448968703250 z^3
 +2332339383938836349679 z^2
 -471493433933816742000 z
 +24391099255638855600)
```

Every displayed irreducible factor has `leading coefficient != constant coefficient`, exactly. This proves the requested loss of palindromic form. The quartic irreducibility also has short finite-field certificates: the `t0=1` quartic remains irreducible modulo 61, and the `t0=3,5` quartics remain irreducible modulo 11. By Gauss's lemma, each is irreducible over `Q`.

Exact reality results are obtained by positive quadratic discriminants plus Sturm counts for the quartics:

| core | quadratic discriminants | quartic real-root count | total spectrum |
| ---: | --- | ---: | --- |
| 1 | `7828835401653673969`, `2589293856456096289369` | 2 | 6 real roots, 1 nonreal conjugate pair |
| 3 | `1013417710566306961`, `1596490685498881321` | 0 | 4 real roots, 2 nonreal conjugate pairs |
| 5 | `3519770374790232649`, `613036506422939485009` | 2 | 6 real roots, 1 nonreal conjugate pair |

For the decimal shift comparison, roots of the exact factored polynomials were paired with the `v=1` roots by the minimum-total-distance perfect matching. The resulting largest displacements are:

| core | max `|Delta lambda|` | load-bearing signed displacement |
| ---: | ---: | --- |
| 1 | `0.9570159788` | `10.2415182723 -> 11.1984320472 + 0.0139861010 i`, so `Delta=+0.9569137749+0.0139861010 i` |
| 3 | `1.3978902241` | `10.2541656672 -> 8.8563197380 + 0.0111282045 i`, so `Delta=-1.3978459292+0.0111282045 i` |
| 5 | `0.0144654296` | `2.3412325139 -> 2.3556979435`, so `Delta=+0.0144654296` |

This confirms the quoted `~0.96`, `~1.40`, and `~0.0145` magnitudes and supplies their signs for representative maximally shifted roots.

The nonreal roots themselves are:

```text
t0=1: 11.1984320472 +/- 0.0139861010 i
t0=3:  0.0937130291 +/- 0.0028458544 i
        8.8563197380 +/- 0.0111282045 i
t0=5:  0.1046641456 +/- 0.0018623814 i
```

Hence “small complex pairs with `|Im| ~ 0.002-0.003`” is true for the small pair at `t0=3` and approximately for `t0=5`, but it is not a complete description: `t0=1` has `|Im|~0.0140`, and `t0=3` has a second pair with `|Im|~0.0111`.

As an independent ordering/inversion check, for all three bump cores (and representative C1, C2, and C3 cores) the directly computed generalized polynomial

`det(z K_c - L2) / det(K_c)`

agrees coefficientwise with `charpoly(K_c^(-1)L2)` at exact zero residual.

#### P1 — is the `t0=1` response boundary-mode dominated?

**REFUTED as a one-mode claim; NARROWED to a boundary/heavy-sector response.** The exact two-site shift `U` remains both a Gram isometry and a commutant at the bumped core:

```text
nnz(U^T K_c U - K_c) = 0,
nnz([W,U])            = 0.
```

At `v=1, t0=1`, the exact sector factorization is

```text
U=+1: light^2
U=-1: heavy * boundary.
```

After the `{3,4}` bump it is

```text
U=+1: the two nonpalindromic quadratics shown above,
U=-1: the irreducible nonpalindromic quartic shown above.
```

Thus the bump destroys the separate heavy/boundary factor labels: they hybridize inside one irreducible `U=-1` quartic. Continuity-based minimum-distance matching gives

```text
baseline boundary large root: 10.2415182723 -> 11.1984320472 +/- 0.0139861010 i,
                               |Delta| = 0.9570159788;

baseline heavy large root:    10.2541656672 -> conjugate member of the same pair,
                               |Delta| = 0.9443699527.
```

The two baseline large roots were already separated by only about `0.01265`; after the bump they become one conjugate pair with the same real part. Assigning one post-bump member as uniquely “boundary” is therefore not invariant. The light-sector large-root shifts are smaller but non-negligible, `0.174426` and `0.191449`.

Conclusion: the large response is concentrated in the `U=-1` sector that contains the boundary mode, but the bulk-heavy root moves almost equally and the exact factors merge. “Boundary-mode dominated” overstates what the data identify.

#### P2 — second bump position `{2,3}`

The `{2,3}` profile also obeys exact covariance:

```text
nnz(Ps H Ps - H)   = 0,
nnz(Ps Q Ps - Q^T) = 0.
```

Its response is:

| core | `nnz(W_bump-W_v1)` | max matched root shift | exact factor behavior |
| ---: | ---: | ---: | --- |
| 1 | 64 | `0.6880075885` | two nonpalindromic quadratics plus an irreducible nonpalindromic quartic |
| 3 | 64 | `0.0737486236` | two nonpalindromic quadratics plus an irreducible nonpalindromic quartic |
| 5 | 0 | `0` exactly | the complete `v=1` factorization survives exactly |

The `t0=1` large `U=-1` pair is `9.5662376816 +/- 0.0104655833 i`; relative to the two nearby baseline heavy/boundary large roots, the real shifts are about `-0.688` and `-0.675`. The response therefore persists for a different bump location, but its sign reverses and its size falls from `~0.957` to `~0.688`. At `t0=3`, the maximum response falls from `~1.398` for `{3,4}` to `~0.07375` for `{2,3}`; at `t0=5` the operator itself, not merely its spectrum, is unchanged exactly.

Conclusion: near-edge coupling is **generic across these two bump locations**, not unique to `{3,4}`, but magnitude, sign, and spatial reach are strongly bump-position dependent.

### Physicality fence — what the volume calculation does not establish

The exact spectral sensitivity does **not** establish lapse physicality. `v` is the imposed Block-105 Hodge-volume parameter. The calculation supplies no lapse variable in an ADM phase space, no Hamiltonian constraint, no gauge orbit/quotient, no Dirac observable, and no OS reconstruction making `W` a physical transfer operator. Exact `Ps` covariance only proves compatibility with this reflection; it does not prove that two `v(t)` profiles are physically inequivalent.

What is established is narrower: within the imposed finite matrix construction, uniform and localized changes of the Hodge volume alter the exact monodromy spectrum, while the specified reflection covariance survives. Calling that parameter a physical lapse, or these eigenvalue shifts physical lapse excitations, remains unsupported and would contradict block 190's own interpretation fence.

## Verdict summary

| item | verdict |
| --- | --- |
| P3 | **CONFIRMED exactly** |
| C1 | **CONFIRMED exactly** |
| C2 | **CONFIRMED geometrically, narrowed algebraically**: crossing gives `(2,2,4)`, not an irreducible degree-eight polynomial |
| C3 | **Exact formula/direction CONFIRMED; quoted decimals REFUTED**: ratio is `2.7362708113 -> 2.6427023041` |
| C4 | **Core exact claims CONFIRMED; complex-pair gloss qualified** by the larger imaginary parts listed above |
| P1 | **REFUTED as boundary-mode dominance**; exact result is heavy/boundary-sector hybridization |
| P2 | **Generic near-edge coupling supported**, with strong position dependence and an exact zero beyond range for `{2,3}` at `t0=5` |
| lapse physicality | **NOT ESTABLISHED**; only finite constructed-matrix sensitivity to an imposed Hodge-volume profile is shown |

Overall: **CONFIRMED WITH MATERIAL NARROWINGS AND TWO NUMERICAL CORRECTIONS.** No headline exact polynomial in C1, C3, or C4 failed. The main refutations are the literal C2 nonfactorization wording, C3's ratio decimals, a blanket `0.002-0.003` description of all complex imaginary parts, and P1's one-mode boundary-dominance interpretation.
