lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-10T09:32Z

# Check of `library/rim-scale.md` (row 613)

Provenance: Claude Opus 5.5, max effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at 64bf74e70. One line-by-line reading of a proof written by Claude Fable 5.2 (row 609). Not an audit. Status: in progress; sections are written as they finish.

Credit. The object is the retained operation of Ethan Sussman and Levent Alpoge's `YM4_1400.tex` (their text names Claude and Codex as authors), commit `2bc0658f91d2`, fetched by URL into a scratch folder (136,637 lines). "Y n" is line n of that file. The method under check (test on the localized background; contrapositive payment) is Tadeusz Bałaban's, CMP 119 (1988) and CMP 122 (1989). I did not reopen Bałaban's pages; every verdict below rests on lines of Y that I read. No numeric job was run.

Order note. The row asks for item (4) before section 4 is read. I read the whole of `rim-scale.md` once at the start, before the search. So item (4) is not blind to section 4's table. To limit this, my search in item (4) uses different keys (the guard's labels and the read sets of each consumer, not section 4's word list), and I record every difference.

## 1. Item (1): Claim 5.1, Field 5.2, facts of section 3

**Verdict: holds as written, with two precision repairs that change no conclusion.**

Facts of section 3, against the cited lines:

| Fact | Lines read | Verdict |
|---|---|---|
| (R1) rim identity | Y 72327-72338; Y 35185-35188 (one-step face lift: a fine plaquette is `I` unless both directions cross block faces, else the coarse plaquette up to conjugation); Y 72277-72281; Y 64102-64105; Y 71379-71381; Y 134210-134214; also Y 98126-98135 (the same for every layer, "including those made using averages across the interfaces") | holds |
| (R2) one-step local flux | Y 71619-71634 (statement), proof Y 71636-71690; row sum `L^2` at Y 4756-4759; norm `<X,Y> = (1/2)Tr XY`, so `norm(1 - e^{iF}) = 2 sin(abs F / 2)`, at Y 4700-4702 | holds. `D(C)` is a `2L x 2L x L x L` site box, `4L^4` sites, at most `24 L^4` plaquettes internal to it, so `abs R_C <= 24 L^4 C_L kappa^2` |
| (G1) | Y 64229-64231 gives "two level-m cells inside X" | holds as stated. Theorem 6.2's proof needs more: `X cap Omega_m` EQUALS the outer two cell layers. That is Y 63760-63765 (`O_i = Omega_i^c cap X = H_i^{[8 a_i]}`, `G_k = X = H_k^{[10 a_k]}`), restated at Y 71429-71431. Repair: cite (63760) for the equality |
| (G3) | Y 72318-72319, 72327-72329, 135196-135209, 35166-35183, 77946-77949, 65054-65056 | holds for the datum (face lift) and for the weighted distance `>= c M R_m` from interior reads. "The tower lies in the outer cell layer" is not displayed in the cited lines. It follows from Y 132186-132212: the recursive tower removes a bounded number of grid layers per level (`1 + floor((R_1 + k)/L)`, fixed point after `a = log_L R_1` erosions), so its width is at most `C(L, R_1) frakM xi_m`, against a cell side `M R_m xi_m`. So it holds once `M R_m >= C(L, R_1) frakM`, a coupling condition. Section 9 item 5 already flags this |
| (G4) | Y 14936-14943 (`R_1 >= L >= 13`, `R_1 frakM >= L^2 rho`, gap of (mb:separation) `> R_1 frakM xi_j`); Y 10510-10511 (`xi_j = L^j eta`); Y 35693-35696 | holds. Whether the joined set at `dX` meets these floors is H-GEO (row 614); not checked here |

Claim 5.1, line by line.

- The 2-plane `{x_mu = c_mu, x_nu = c_nu}` of the two crossed block faces contains the normal direction, since `mu, nu` are tangent to the face. Correct.
- Layer 1 has normal width `> R_1 frakM xi_1 >= L^2 rho xi_1` (G4). Correct.
- The four bonds of `C` are rows: by (mb:determining-rows), Y 10555-10566, `Gamma_1` is the level-1 bonds touching `Omega_1` with no endpoint in `Omega_2`. Correct. `M_B U = V` (Y 35641-35643) gives `M U_X = V` on them. Correct.
- `D(C) subset Omega_1`, since `Omega_1` is a union of level-1 blocks (Y 10527-10529). No bare bond of `D(C)` is in `Gamma_0` (no endpoint may lie in `Omega_1`). So no plaquette of `D(C)` is in `P_rim`. Correct.
- `abs F_p = 2 arcsin(n/2) <= (pi/3) n` for `n <= 1`, by convexity of arcsin on `[0, 1]`. Correct; `pi/3 < 1.05`.
- `2.1 L^2 tau_m < 6.3 eps_m L^{-2(m-1)}` since `tau_m < 3 eps_m L^{-2m}`. Correct.
- `norm(V_m(dP) - 1) = 2 sin(abs F_C / 2) <= abs F_C`. Correct with Y's norm.
- Undefined orbit counts as failure: Y 64484-64486 states it for the inset guard `G = chi_in kappa_x`. Acceptable.

Precision repair P1 (unproved by the author, now supplied). The datum of `C` is `V_m(dP)` only if `C` lies in the same slab of level-m blocks as the rim plaquette. Layers 0 and 1 have total normal width at most `C(L, R_1) frakM L eta`, which is below `xi_m = L^m eta` once `m >= m_1(L, R_1, frakM)`. For smaller `m`, read `P` as the top plaquette at the position of `C`; the conclusion is unchanged. Field 5.2 is not affected: there every top 12-plaquette of the fixed box has the same defect.

Field 5.2, line by line.

- `2 sin(a/2) >= a - a^3/24 >= 7 eps_m L^{-2(m-1)}` when `a^2 <= 3`. Correct.
- Earlier stages (Y 72406-72419). Y's argument compares `C abs(a)` times fixed powers of `L` (the bare curvature at joined layers `>= h` is `<= C abs(a) L^{-2h}`, and `m - h = N_m` is fixed on the plateau) with thresholds of order `eps_j L^{-2j}`, `j <= m`. With `a = 8 eps_m L^{-2(m-1)}` the needed inequality is `8 C L^2 L^{-2m} < c L^{-2 N_m}`, true for large `m`. The radius `C abs(a)` and the fluctuation size `O(g_j^{-1} abs(a))` also tend to zero. So the factor `L^2` changes nothing in Y's verification. Correct.
- Top plaquettes `<= C abs(a)` (Y 72406-72408 at `j = m`); Wilson exponent `C theta_m a^2` (Y 72350-72352); fresh payments `O(a^2)` (Y 72420-72422). Correct. Here `theta_m = x_m` in the run with its own choices (Y 63855), and Y's drop-out witness uses `x_m` (Y 72146).
- Notation: the file uses `a_m` both for the cell side (section 3) and for the amplitude (Field 5.2). Wording only.

So A2 as worded in row 609 is false, as the file says. The failure is not stop (ii) literally (that stop names a plaquette with one to three lifted bonds); it is a plaquette with no lifted bond. The file says "wider form". Correct.

The closing remark of section 5 (failure in layer `j` once the rim defect exceeds `C eps_m L^{-2(m-j)}`) needs the local cone form of the averaging bound, `prop:small-energy-all-depth` or the local estimate of Y 134113-134120, not the global `cor:iterated-average-energy` as cited. It is a remark; nothing depends on it.

## 2. Item (2): Theorem 6.2, Corollary 6.3, inputs (I1)-(I5)

**Verdict: holds as an implication from H-GEO, (I1)-(I4) and (I3)'s support condition, after four small repairs (R-a to R-d). None changes a constant order or a conclusion.**

Inputs, each against Y:

| Input | Y as written | Same statement, all hypotheses? |
|---|---|---|
| (I1) | `bgc:proper-background`, Y 35632-35646: for the geometry of Y 35268-35275 there are `a_0, a_1, C_B` with `C_B a_1 < a_0`; a real mixed datum with all ordinary and mixed test holonomies within `eps <= a_1` of one has a constrained-critical `U(V)`, `M_B U(V) = V`, `R_mat <= C_B eps`; two critical configurations with `R <= a_0` are in one residual orbit | Yes. The hypotheses are the no-inward geometry with the floors of Y 14936-14943 and the patch floors `rho >= L^2 sigma` of Y 35549-35551. These are H-GEO (row 614), not checked here |
| (I2) | Proof of `bgc:reset`, Y 35610-35627: `r_U(x) <= K v_R(x) + r_R(x)/2` for real constrained-critical `U` with `R(U) <= a_c`; `P(x) = sup_tau e^{-delta d_B(x,tau)} abs(dV(tau) - 1)` with `e^{delta R} = sqrt 2`; the maximum argument gives `r_U <= 5K P`; "The bounded displacement from a corner to the base of a readout changes this constant by a fixed factor" | Yes, with R-b. It is a step inside a proof, not the lemma's statement; its own hypotheses are only `R(U) <= a_c`, criticality and the patch floors |
| (I3) | Y 65409-65410 (`e_l = R_l^2 eps_l`); Y 78328-78337 ("On its admitted incoming fibre the old lower holonomy bounds and the exact top averaging relation give the prepared datum bounds `C e_q` ... Carry these bounds as a support condition"); Y 134200-134216; Y 71385-71391 (`eps_* e^{-c delta_c M R_m} = o(eps_m)`) | Yes. It is a carried support condition on the prepared datum, as the file says; not rebuilt |
| (I4) | Y 135180-135190, and more exactly Y 134113-134120: the full bare averaging blocks of a level-k plaquette with a corner in a positive density cube lie in its one-layer enlargement; there the test gives bare curvature `< eps_k eta_k^2`; the local average estimate gives `abs(dV_k - 1) <= 2 eps_k`, "since the localized orbit has the prescribed `V_k` there" (also Y 98120-98140) | Yes, as Y states it. The global `cor:iterated-average-energy` (Y 4905-4920) gives `2 alpha` with `alpha = (pi/3) eps_m`, i.e. `2.1 eps_m`, through its local cone form. Harmless: every margin below has room for 2.1 |
| (I5) | `prop:small-energy-all-depth`, Y 71744-71760, with `N_0(S) = P_0(S)` of Y 71716-71726: "a bare plaquette is included exactly when all its corners lie in the four blocks `B^t(y)` belonging to one member `C` of `S`" | Yes, exactly; no hypothesis on `U` |

The three questions of the row.

1. *Profile over tested datum plaquettes only?* Yes. Y 12455-12460: "the distance to a tested plaquette is the minimum over its corners. When an inward row is kept one also counts the pinch tests ... On a determining set in force all inward rows have been removed, so only tested plaquettes remain." The tested plaquettes include the mixed (interface) holonomies (Y 35537-35538). On the joined set every tested holonomy is of one of the three kinds of Y 134210-134214, and on the tower the mixed ones are face-lift holonomies too (Y 98133-98135). So the file's three-kind split covers the whole supremum.
2. *Is `L(p) = eta L^{lambda(p)}` Y's assigned scale on the tower?* Yes, with R-a. Y 10541-10542: "For a bare bond or plaquette `e`, let `L(e)` be the largest top scale attached to its corners." A top of level `j` has a pillar of side `xi_j = L^j eta` (Y 10510-10511, 10528-10531). So `L(p) = eta L^{lambda(p)}` holds with `lambda(p)` = the largest pillar level among the corners of `p`. Inside one layer this is the layer index. At a seam it is the upper one.
3. *Is (I5) used with the right `N_0(S)`?* Yes. Corollary 6.3 takes `S = {P}`, `t = m`, and sums over the bare plaquettes with all corners in the four level-m blocks of `P`. `(1/4)(4 eps_m)^2 = 4 eps_m^2 <= e_*/2` when `eps_m^2 <= e_*/8`. Correct.

Theorem 6.2, line by line. The three-kind split (Y 134210-134214), the bound `2 eps_m` on top plaquettes, `eps_int`-regularity, existence and uniqueness from (I1) with `C_B eps_int <= min(a_0, a_c)`, and the profile bound are correct. The interior distance is right: by (63760) the second cell layer is in `Omega_m`, every prepared shell is in `Omega_m^c` (Y 64226-64227), so the band between `E` and `X cap Omega_m^c` is one cell of side `M R_m xi_m` at top scale, weighted length `>= M R_m`. Y states the same order (`c M R_m`, Y 65054-65056, 77946-77949). The conclusion is Y's own local-unit estimate (Y 72293-72306, `C L^{-2 lambda(p)}(...)`) with the carried density bound in place of the paying-energy bound `varsigma_*`. That is a consistency check, not a second proof.

Corollary 6.3, line by line. The contrapositive is correct: if all top plaquettes in the outer two layers are `<= 4 eps_m`, the same proof gives `r_U <= 4 K_w eps_m < 5 K_w eps_m = c_0 eps_m` on `E`, and `U_X` exists. The energy line is (I5) as written. The Wilson weight is `x''_m = x_m` outside the box (Y 71413-71415), and `theta_m = x_m` (Y 63855).

Repairs (wording or citation; none breaks a consumer):

- **R-a.** Define `lambda(p)` as the largest pillar level among the corners of `p` (Y 10541-10542). With any smaller choice at seams the threshold is still implied, but the consumer then reads a bound weaker by `L^2` at seam plaquettes.
- **R-b.** `K_w` is `5K` times the fixed corner-to-readout factor of Y 35626-35627, not `5K`. Only the name changes; `c_0 = 5 K_w` keeps its role.
- **R-c.** In the proof of Theorem 6.2, "the top plaquettes ... lie in the outer two cell layers (G1)" needs the equality `X cap Omega_m = H^{[10 a_m]} \ H^{[8 a_m]}` from (63760), not (G1).
- **R-d.** Corollary 6.3 says the blocks of `P` lie "at least one cell from `X cap Omega_m^c`". The proof does not give this: `P` may sit in the second layer next to `Omega_m^c`. Repair: from the weighted profile, a failing `p in E` with corner `x` forces `P(x) >= 5 eps_m`, so some top-type `tau` has `abs(dV(tau) - 1) >= 5 eps_m e^{delta d_B(x, tau)}`, hence `d_B(x, tau) <= delta^{-1} log(2/(5 eps_m))`, far less than `M R_m`. Take `P = tau`. The witness then lies in `Omega_m`, which is all that "no corner in the floor" needs (the floor is inside `X cap Omega_m^c`, Y 72146 item (4)).

What item (2) does not show. The theorem is an implication. Its geometry input is H-GEO and its interior input is (I3), both open and owned elsewhere. Whether the stage guard is evaluated only on the support of the carried density test is a property of Y's operation. Y 71427-71436 (the carried `chi_k(Omega_k^{~4})` covers the outer six cells, `X^{~-6}` the rest) and Y 72146 ("each test carried by X takes its recorded value") support it. I did not check every fibre on which the guard is evaluated.

## 3. Item (3): section 7.2

**Verdict: the computation holds after repair R-e. Point (ii), the current, is decided by Y and holds. Point (i), the cube fit, is not stated in Y. Y's geometry decides it: it fails under Y's stated floor `R_1 >= L` and holds after repair R-f.**

Clause read (Y 1260-1274). Good real gauges are required on "all its gauge cubes of side at most `12 frakM xi_n` at index `n`, including cubes contained in layer `n+1`". In bare units: `L^n abs(v) <= a_flat`, `L^{2n} abs(delta v) <= a_flat`. Y 62962-62966 defines the family: all such cubes that are unions of `frakM`-cubes and lie in `L_q cup L_{q+1}`; "Such a cube need not meet `L_q`". Nothing keeps a gauge cube off the outer face of `Omega_n`.

Index 0 (Lemma A of `g0-cover.md`, (A2): half-width `q`, plaquettes `< eps`, one gauge with `eta abs(A) <= 16 q eps`, `eta^2 abs(grad A) <= 32 q eps` when `8 q eps < 1/4`). Applied with `eps = c_0 eps_m`, `q <= 6 frakM + 1`: correct. The side condition `8 q eps < 1/4` follows from `32 q eps <= a_flat <= 1`.

Index `n >= 1` through Lemma A: `q = 6 frakM L^n`, `eps = c_0 eps_m L^{-2n}`, giving `abs(v) <= 96 frakM c_0 eps_m L^{-n}` and `abs(delta v) <= 192 frakM c_0 eps_m L^{-n}`. The second misses `a_flat L^{-2n}` by `L^n`. Correct. As the file says, this is a fact about Lemma A's bound, not a proof that no gauge exists.

Index `n >= 1` through `prop:bg-local-gauge` (Y 25030-25066).

- **R-e (radius and a missing hypothesis).** Y's cube is `Q_R = {x : abs(x)_inf <= R}`, a radius (Y 24976). The least `r` with `Q_r` covering a gauge cube is `r = 6 frakM xi_n`, and then `Q_{8r}` has side `96 frakM xi_n`. The file writes `r = 12 frakM xi_n` and "side `96 frakM xi_n`"; these two do not agree. With `r = 6 frakM xi_n` the bounds are `xi_n abs(A) <= 6 C frakM rho` and `xi_n^2 abs(DA) <= C(1 + 6 frakM) rho`. The proposition also needs `r^2 kappa <= eps_*`, here `36 frakM^2 rho <= eps_*`. The file does not list it. Add it to section 8, item 5. It holds at weak coupling.
- **Point (ii), the current: decided by Y; holds.** The proposition reads "the actual current in (bg:current-normalization)". That is the physical gradient of the Wilson action at bonds whose full plaquette stencil is present (Y 25004-25011). Y's own corollary `cor:bg-physical-local-scale` (Y 25690-25722, with the remark at Y 25725-25729) says it "applies to the physical Wilson current. A separately prescribed auxiliary current satisfying a numerical bound cannot replace `J_A(U)`". The radius `R` bounds exactly this current at full bonds (Y 35277-35283; Y 10544-10547). For a constrained-critical field the exact equation `F'(A) = q'(A)^# omega` identifies it with the multiplier term (Y 35599-35602). So the multipliers are already inside `R(U_X) <= rho`; nothing is added to `J`. "Proved for one spacing" is no obstruction: `U_X` is a bare connection on one lattice of spacing `eta`. The layers enter only through the bounds `kappa`, `j` on `Q_{8r}` and `Q_{7r}`, and through the condition that these cubes lie "inside the action region, including every plaquette used by the current" (Y 25691-25692). That condition is point (i).
- **Point (i), the fit: not stated in Y; fails under Y's stated floors.** Y never applies the proposition to the gauge family. Y supplies index-`q` gauges by restriction from an enlarged original class (Y 62955-63039). Y's only use of the proposition is the corollary above. So the fit must be read off Y's tower geometry:
  - The erosion rule (Y 651-664) builds `Omega_{q+1}` from cubes of side `frakM L^{q+1}` at distance `> R_1 frakM L^q` from `Omega_q^c`. The minimal recursive tower (Y 132186-132212) meets this floor with one grid cell of rounding. So layer `q` has width at most `(R_1 + L) frakM L^q`, and `dist(Omega_n, X^c) < (R_1 + L) frakM xi_n / (L - 1)`.
  - The proposition needs the curvature bound on `Q_{8r}`, a margin `7r = 42 frakM xi_n` beyond the gauge cube.
  - Y allows `R_1 = L` (Y 14941, 16102-16103, 35850: only "`R_1 >= L`", a power of `L`). Then `dist(Omega_n, X^c) < 2L/(L-1) frakM xi_n < 2.2 frakM xi_n`. For a gauge cube on the outer face of `Omega_n`, `Q_{8r}` leaves `X`. The hypothesis "inside the action region" fails. Inside `X` it fails too: `Q_{8r}` meets layer 0, where a face-lift plaquette carries a whole top plaquette, so the physical curvature there is of order `eps_m eta^{-2}`, not `O(rho xi_n^{-2})`. Then `r^2 kappa` is about `36 frakM^2 L^{2n} eps_m`, which is not small for large `n`. The same happens for `R_1 = L^2` when `L < 41`, since then `(R_1 + L)/(L-1) < 42`.
  - This is a failure of the proof route at the line "use `R(U_X) <= rho` on the cube in layers `n, n+1`". It is not a counterexample to the clause.
- **R-f (repair of the fit, proposed and checked here).** Add the floor `R_1 >= 42 L`, for example `R_1 = L^3` (with `L >= 13`, `R_1/L = L^2 >= 169`). Then layer `n-1` alone has width `> R_1 frakM xi_{n-1} >= 42 frakM xi_n`. So `Q_{8r} subset Omega_{n-1} subset X`, at least `R_1 frakM eta` from `X^c`, and the current is read only at full bonds. The bounds there are `kappa = rho L^2 xi_n^{-2}` and `j = rho L^3 xi_n^{-3}`. With `rho := C_B eps_int`, the global radius from (I1), the conclusions are `xi_n abs(A) <= 6 C frakM L^2 rho` and `xi_n^2 abs(DA) <= C(L^2 + 6 frakM L^3) rho`, under `36 frakM^2 L^2 rho <= eps_*`. The clause holds once `a_flat >= 7 C frakM L^3 rho`. That is a coupling condition, since `a_flat` is fixed first (Y 1268-1270). The global `rho` is used because `Q_{8r}` may leave `E` inward; on `E` Theorem 6.2 gives the smaller `2 K_w eps_m`. Not checked: whether another part of Y fixes `R_1` below `42L`. All the floors I found are lower bounds (Y 651-652, 14941, 16102-16103, 35850). The tower must still fit in the outer cell layer, which needs `M R_m >= C(L, R_1) frakM` (section 1, (G3)). That holds at weak coupling.

What item (3) does not show. It does not decide the clause at `R_1 in {L, L^2}` by another route (for example, patching smaller Coulomb gauges). It does not check the collar radii of the pointwise clause (the file's other flag in 7.2), which the row did not ask for.
