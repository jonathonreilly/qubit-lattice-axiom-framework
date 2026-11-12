# Check of library/gap-joint-astra.md (FINISH row 816), by Claude Opus 5.5, line by line

Clone: `/Users/jonreilly/ym4d-lead/clone` at commit `e3e52f6bbcd39ff776c99a15f6b2daff38338f7b`.
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target: `D/library/gap-joint-astra.md`, 723 lines, author Codex gpt-6-astra max (FINISH row 811).
The note says its own checkout was `9bb28a2f`. I read every source at the clone commit above.

Sources read: the target in full; `gap-kappa-order.md` lines 1-120 (Proposition SC, Lemmas M, F, T, Theorem SB);
`gap-expose-astra.md` lines 100-300 and 480-620 ((E1)-(E7), (E14)-(E18));
`gap-vmf-lip.md` lines 40-200 (Theorem V) and the verdict lines of `gap-vmf-lip-check-opus.md`;
`gap-tree-astra.md` lines 355-450 ((G14)-(G17a)) and `gap-tree-check-opus.md` lines 125-155 and its table;
`gap-ext-astra.md` lines 100-128 and 474-573 ((FQ), (LC), (E18)-(E20)) and the verdict lines of `gap-ext-check-opus.md`.
The SA outline `YM4_sketch_500.tex` at `31a47c543775` was downloaded once into
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/sa-dl3/wrOM0F/`.
I read its lines 1255-1360 only (the KP criterion and the rooted-tree theorem). It is not copied into any checkout.

Method: every step was re-derived by hand. One small run (under 1 MB) is reported as GUIDE. No verdict rests on it.
No repository file was edited.

## A. (J4): the telescoping sign-flip identity (lines 137-156)

**Polynomial form.** Write `e^{beta eta x} = cosh(beta x)(1 + eta tanh(beta x))`. The product over P gives
`C(U) sum_{S subset P} prod_{p in S} eta_p t_p`. Proposition SC kills every nonclosed S after integration.
For closed S, `prod_{p in S} eta_{m,p} = (-1)^{<m,S>}`. A change of representative `eta -> eta (-1)^{db}`
multiplies this by `(-1)^{<b, partial S>} = 1`. So (J2) holds.

**Unique decomposition (lines 97-103).** Link-connected components of a closed set are closed: all faces of S
at a link lie in one component. Distinct components share no link. Conversely a compatible family has a closed
union whose components are exactly its members. So closed sets and compatible families of members of cal S are
in bijection, and the weights multiply. HOLDS.

**Affine structure.** Each member appears at most once in a compatible family (self-incompatibility). So
`Xi(w) = Xi_{without S}(w) + w(S) Xi_comp(S)(w)`. The coefficient `Xi_comp(S)` does not contain w(S).
Its derivative in w(S) is exactly `Xi_comp(S)`.

**Telescoping.** Order the odd surfaces `S_1, ..., S_N`. Let `w^(k)` be `w_m` with the signs of `S_1..S_k` flipped.
Then `w^(0) = w_m` and `w^(N) = w_{m+v}`, since `(-1)^{<m+v,S>} = (-1)^{<m,S>}(-1)^{v(S)}`.
Step k gives `Xi(w^(k-1)) - Xi(w^(k)) = 2 w_m(S_k) Xi_comp(S_k)(w^(k-1))`.
In `w^(k-1)`, earlier odd surfaces carry `-w_m`, later odd and all even surfaces carry `w_m`.
That is exactly `w^[S_k]` of line 139. The value on S_k is absent from `Xi_comp(S_k)`.
C does not depend on m. Integrate and divide by `2 Z_m`. With (J1) this gives `p_m(v) = sum D_m(S)`.

**No positivity.** Each step is a finite polynomial identity. No logarithm, no convergence and no sign of
any D is used. HOLDS.

**(J3) (lines 123-135).** Expand each exponential. The average over b of `(-1)^{<db,S>} = (-1)^{<b,partial S>}`
is the indicator of `partial S = 0`. The average reproduces `C Xi(w_m)`. Each summand is a positive exponential.
HOLDS. It holds for every twist, not only the two endpoints.

**Lines 158-177.** `C w_m(S) prod t` is sinh on the selected faces and cosh elsewhere. The character series of
sinh and cosh are the half-integer and integer parts. HOLDS. The remark that (J4) "lies outside the obstruction
class of row 809" is not load-bearing. It is plausible, since D_m(S) is formed before any absolute value, but it is
an ARGUED remark, not a proved one.

**Verdict A: HOLDS.**

## B. (J15): the positive-transfer lower bound for (J14) (lines 386-445)

**(J14).** S is first, so `w^[S] = w_0` on every other surface. A surface T is compatible with S if and only if
`T subset P_far`: a shared link forces a face of T in N(S), and a face of `N(S)\S` carries a plane link.
Expand `prod_far e^{beta x} = prod_far cosh * sum_{R subset P_far} prod_R t`. If R is not closed then
`partial(S u R) = partial R != 0`, since S and R are disjoint and S is closed. SC kills that term.
The closed R are exactly the compatible families. So `Z_0 D_0(S) = Z_S^dec`. HOLDS.

**Time independence.** With r as time, S is the (r,i) plane at transverse position b.
N(S)\S consists of (r,j), (r,k) faces at b, b-e_j, b-e_k (temporal) and (i,j), (i,k) faces there (spatial).
These sets are invariant under r-translation. Each temporal face (r,s) at spatial base y corresponds to the
spatial link (y,s). The i-links at b get the sinh kernel. The j-links at b, b-e_j and the k-links at b, b-e_k
get cosh. All other spatial links get the full exponential. No spatial link receives two kernel types. HOLDS.

**Positivity of the kernels.** For a class function f, convolution acts on the spin-j block as `f^(j)/d_j`.
I checked `int e^{beta x} chi_j = d_j (2/beta) I_{2j+1}(beta)` from the Weyl density
(`(2/pi) sin^2 theta`, recurrence `I_{n-1} - I_{n+1} = 2n I_n / x`). So the eigenvalue is `z r_j > 0`.
sinh keeps the half-integer j and cosh the integer j. Both are positive semidefinite. On spin 0 cosh gives
`z >= 1`, and the constant kernel gives the rank-one projection. So `C_cosh >= C_1`. HOLDS.

**The transfer identity with signed kernels.** Integrating the temporal links gives the gauge projection.
That step uses only that the kernels are class functions. It is algebraic in them. HOLDS.

**The two-cut comparison.** Write `Z_S^dec = Tr_H (B^{1/2} K B^{1/2})^{n_r}`, with K a tensor product of
positive semidefinite convolutions and B a positive gauge-invariant multiplier.
(1) `K >= K_0 >= 0`, since `(C_cosh - C_1) (x) D >= 0` for `D >= 0`, applied factor by factor.
So `B^{1/2} K B^{1/2} >= B^{1/2} K_0 B^{1/2}`. Min-max for compact positive operators orders every eigenvalue.
(2) `B^{1/2} K_0 B^{1/2}` and `K_0^{1/2} B K_0^{1/2}` have the same nonzero eigenvalues (`X X*` and `X* X`).
(3) `B >= B_0 > 0` pointwise, since the spatial cosh factors are at least one. So
`K_0^{1/2} B K_0^{1/2} >= K_0^{1/2} B_0 K_0^{1/2}`. Min-max again.
All operators are positive, so `Tr X^{n_r} = sum lambda_k^{n_r}` is monotone in each eigenvalue.
Gauge projection commutes with K, K_0, B, B_0, so the comparison holds on H. No operator monotonicity of
powers is used. HOLDS.

**Factorization.** After the replacement, the plane faces use only plane links. The far faces use no plane link.
Every non-plane link lies only in far faces or in replaced faces. So the integral is `Z_plane * Z_far`. HOLDS.

**Torus Schur computation.** On the n_r x n_i torus, each edge lies in two faces, used as U and U^{-1}.
Orthogonality forces equal spins and gives `1/d_j` per edge. Each vertex closes an index loop, `d_j`.
Each face carries the coefficient `z d_j r_j`. With `V - E + F = A - 2A + A = 0` the result is `(z r_j)^A`.
Sum over half-integer j: `Z_plane = z^A sum_j r_j^A`. At small beta this is `(beta/4)^A`, matching Lemma T(d).
All terms are positive and `z >= 1`, so `Z_plane >= r_{1/2}^A`. HOLDS.

**Verdict B: HOLDS.**

## C. (J16): the local normalization bound (lines 447-473)

**The count |N(S)| = 9A.** The plane has A r-links and A i-links. Each link lies in 6 plaquettes in four
dimensions. Incidences: 12A. The A plane faces use 4A of them. Each other face at a plane link is an (r,j), (r,k),
(i,j) or (i,k) face at b or b - e_j, b - e_k. Its second link of that direction sits at a different transverse
position, and it has no link of the other plane direction. So it has exactly one plane link. Hence 8A such faces
and `|N(S)| = 9A`. Periods at least three exclude identifications. HOLDS.

**Assignment.** Each face of N(S) has at least one plane link; give it to the first one in the order. Then `k_e` is
at most the 6 faces at e, and `sum_e k_e = |N(S)| = 9A`. HOLDS.

**One step.** For SU(2), `(1/2) tr(M U)` and `(1/2) tr(M U^{-1})` are linear in the quaternion coordinates of U,
with a unit coefficient vector. So the exponent is `F_e . h_e` with `|F_e| <= beta k_e`. The Haar integral is
`z(|F_e|)`. z is increasing on `[0, infinity)` (average of `cosh(s h_1)`). So it is at most `z(beta k_e)`. HOLDS.

**`log z(u) <= u^2/8`.** `(log z)''(u) = Var_u(h_1)`. Theorem V with `e = e_1` and `phi = h_1`
(chord-Lipschitz) gives `Var <= a(|u|) <= 1/4`. Theorem V is checked HOLDS in `gap-vmf-lip-check-opus.md`.
`log z(0) = 0` and `(log z)'(0) = E_0 h_1 = 0`. Two integrations give the bound. HOLDS.

**Induction.** Integrate the plane links in the chosen order, with all non-plane links fixed. At link e the
factors still depending on e are exactly the faces assigned to e; faces assigned earlier were already replaced by
constants. Far faces contain no plane link and factor out. So `Z_0 <= Z_far prod_e z(beta k_e)`. HOLDS.

**Final constant.** `sum k_e^2 <= 6 sum k_e = 54A`. So the exponent is `(beta^2/8) 54 A = 27 beta^2 A / 4`. HOLDS.

**(J17).** `D_0(S) = Z_S^dec / Z_0 >= Z_far r_{1/2}^A / (Z_far e^{27 beta^2 A/4})`. `Z_far > 0`. HOLDS.

**Verdict C: HOLDS.**

## D. (J17) arithmetic at beta = 1/2 and the refutation of (J11) (lines 479-489)

(E15) gives `r_{1/2}(beta) >= beta/(4 e^beta)`. I re-derived it: the numerator `int x e^{beta x}` has nonnegative
odd-order coefficients starting at `beta/4`, and `z <= e^beta`.
At beta = 1/2: `r_{1/2} >= 1/(8 e^{1/2})`. The bracket is at least `e^{-1/2 - 27/16}/8 = e^{-35/16}/8`.
Since `35/16 < 3` and `e^3 < 27`, it exceeds `1/(8 e^3) > 1/216`. So `D_0(S) > 216^{-A}` strictly. HOLDS.
GUIDE (series of I_1, I_2 at 1/2): `r_{1/2}(1/2) = 0.12372`, bracket `0.02289`, proved lower bound `0.01402`,
`1/216 = 0.00463`.

Refutation. (J11) for this S gives `D_0(S) <= C_0 q^A`. With `q < 1/400`, `1/(216 q) > 400/216 > 1`.
So `(1/(216q))^A < C_0`, or a polynomial in the periods. `A = n_r n_i >= a^2` is unbounded. Contradiction. HOLDS.
The pair m = 0 is a frame-1 crossed pair (`m_2 = 0`), so it lies in the uniformity class of (J11).

**Verdict D: HOLDS.**

## E. (J2)-(J3)

Checked inside section A. (J2): HOLDS. (J3): HOLDS. The cocycle pairing is representative-independent. HOLDS.

## F. (J5)-(J10): the strong-coupling domain (lines 179-297)

**(J5) against the source.** SA outline lines 1271-1340 state the criterion
`sum_{Y not~ X} |z_Y| e^{a_Y} <= a_X` (their eq. kp-explicit, credited to KP86). Their theorem gives absolute
convergence, `e^L = Z != 0`, and the rooted bound: the sum over lists rooted at X, with `1/(n-1)!` and the
non-root activities, is at most `e^{a_X}`. The note's use matches: the root's own `|w(S)|` times `e^{|S|}`.
The theorem also gives the branch of log that is zero at zero. For real activities the series is real, so
`Xi = e^L > 0`. HOLDS. The criterion survives deleting polymers and flipping signs (same magnitudes). HOLDS.

**Connected-set count.** A plaquette has 4 links, each in 5 other plaquettes: 20 neighbours, 21 with itself.
The depth-first encoding of a spanning tree gives at most `C(2k-2, k-1) 20^{k-1} <= 80^{k-1} <= 400^{k-1}`
connected k-sets through a face. HOLDS (with room).

**(J6).** `|t_p| <= tanh(beta) = t`. An incompatible T contains a face of N(S), at most `21|S|` faces.
So the sum is at most `21|S| sum_k 400^{k-1} (et)^k = 21|S| et/(1 - 400 et)`. With `rho <= 1/2`,
`et <= 1/800`, so this is at most `21|S|/400`. `beta <= 1/2400` gives `400 e beta < 1/2`. HOLDS.

**(J7): vacuum cancellation and delta_Lambda.** A list without an odd member has the same weight. A list with
an odd member changes by at most `2 |phi| prod |w|`. By symmetry of the ordered sum,
`(1/n!) sum_{some X_i odd} <= (1/(n-1)!) sum_{X_1 odd}`. So the difference is at most
`2 sum_{S odd} |w(S)| e^{|S|} <= 2 sum_{S odd} (et)^{|S|}`. Lemma M gives `|S| >= A_0 = n_r n_i` for `v(S) = 1`.
Counting odd S of size k by a root face: at most `N_p 400^{k-1}`. So the bound is
`(2 N_p/400) sum_{k >= A_0} rho^k = (N_p/200) rho^{A_0}/(1 - rho)`. HOLDS.
With `N_p <= 24 a^4`, `A_0 >= a^2` and `rho <= 1/2`, `delta_Lambda <= (6/25) a^4 2^{-a^2}`, uniform and tending to zero. HOLDS.

**(J8).** The clusters of the full gas that meet a polymer incompatible with S have total at most
`sum_{T not~ S} |w(T)| e^{|T|} <= |S|`. So `Xi_comp(S)(w^[S]) <= e^{|S|} Xi(w^[S])`, both positive.
`w^[S]` is a sign flip of odd surfaces (give S either sign), so `Xi(w^[S]) <= e^{delta} Xi(w_m)` by (J7).
With `|w_m(S)| <= t^{|S|}`, integrate against `C Xi(w_m) dU / Z_m`. This gives `|D_m(S)| <= e^delta (et)^{|S|}`. HOLDS.

**(J9).** Flip all odd signs: `Xi_{m+v} >= e^{-delta} Xi_m` pointwise. Integrate against C. So `F <= delta`.
`F >= 0` uses the inherited `Z_{m+v} <= Z_m`. `p = (1 - e^{-F})/2 <= F/2`. HOLDS.
The implication to (E17): `a^4 rho^{a^2}` beats `eta_*^{a/2}` for any fixed `rho <= 1/2` and `eta_* < 1`. HOLDS.

**(J10).** At `|S| = A_0`, Lemma M forces one (r,i) face per stack and no other orientation. The Lemma F argument
(each r-link and i-link of S lies in exactly two (r,i) faces) forces invariance under `e_r` and `e_i` shifts. So S
is one plane, and there are `N_perp` of them. Lemma T gives `4^{-A_0}`. A spatial m pairs to zero with an
(r,i) plane. `Z_m = 1 + O(beta^2)`. So `p_m(v) = N_perp (beta/4)^{A_0} (1 + O(beta))` and `F = 2p + O(p^2)`.
HOLDS at fixed volume. Precision, not a correction: the remainder is in fact `O(beta^2)`, since no odd surface has
`A_0 + 1` faces (an extra face would make a stack of another orientation odd, which then needs a full area).
`r_{1/2} = beta/4 + O(beta^3)`: HOLDS.

**Mack-Meyer convention (lines 299-313).** I did not read the paper. Internally the claim is consistent:
if their free energy is `-(1/2) log(Z_tw/Z) = F/2`, then `F/2 = N_perp (beta/4)^{A_0}(1 + ...)`.
`A_0 = n_r n_i` is the area transverse to the vortex sheet and `N_perp` its longitudinal area. The reading of
the paper itself is NOT CHECKED here.

**Comparison with gap-vmf-lip (lines 315-325).** The ranges `beta < 2/3` (layer) and `beta < 2/9` (seed) match
the RESULT line of `gap-vmf-lip-check-opus.md`. HOLDS.

**Verdict F: HOLDS** (the Mack-Meyer reading not checked).

## G. (J11)-(J12) and the implication to Q_F (lines 327-365)

**(J11) implication.** `p_m(v) = sum_{S odd} D_m(S) <= C_0 sum_{S odd} q^{|S|}`. Root counting gives at most
`N_p 400^{k-1}` odd S of size k, all with `k >= A_0`. So `p <= C_0 N_p (400q)^{A_0} / [400 (1 - 400 q)]`. HOLDS.

**(J12) implication.** `p_m(v) <= sum_p sum_{root(S) = p} |D_m(S)| <= N_p C_1 a^b e^{-kappa a}`.
`N_p <= 24 a^4` and `e^{-kappa a} <= eta_*^{a/2}` when `kappa >= (1/2) log(1/eta_*)`.
So `Q_F <= 24 C_1 a^{b+4} eta_*^{a/2}`, which is (E17). HOLDS.
Precision: (J12) still depends on the ordering through `w^[S]`. Read it as "for some fixed ordering".

**Verdict G: HOLDS** (one precision).

## H. The identity-configuration violation of (J5) at beta = 1/2 (lines 491-502)

At `U = 1`, `x_p = 1`, so `|t_p| = tanh(1/2) = t` and a cube boundary T has `|w(T)| = t^6`.
`t = (e - 1)/(e + 1)` is increasing in e. With `e > 8/3`, `t > 5/11`. So `et > 40/33 > 6/5`
(`200 > 198`). Then `(et)^6 > (6/5)^4 = 1296/625 > 2`. The cube itself and two cubes sharing a face with it
are incompatible with it. So the incompatibility sum exceeds `3 * 2 = 6 = |S|`. Continuity gives an open set.
HOLDS. GUIDE: `et = 1.2562`, `(et)^6 = 3.929`.
Scope wording: "three ... exist" means "at least three"; many more cubes share a link. The conclusion is unaffected.
The counterexample is to (J5) with `b(S) = |S|` and pointwise activities only, as the note states. HOLDS.

**Verdict H: HOLDS.**

## I. (J18)-(J20): the fixed-face scalar tail (lines 506-560)

**(J18)-(J19).** `e^{beta x(g)} = z sum_j d_j r_j chi_j(g)`, so `H_J` is its spin tail. `e^{beta eta x(U)} = e^{beta x(eta U)}`
since `-I` is central. `|H_J(g)| <= z sum_{j>J} d_j^2 r_j` and the replaced factor is at least `e^{-beta}`.
So the ratio is at most `eps_J` pointwise. Multiply over H and integrate against the original positive measure.
HOLDS.

**(J20).** I did not rely on (GL4). Independent derivation: `z r_j = (2/beta) I_{2j+1}(beta)`. The integral
representation `I_nu(x) = (x/2)^nu / (sqrt(pi) Gamma(nu + 1/2)) int_{-1}^{1} (1 - s^2)^{nu - 1/2} e^{xs} ds`
gives `I_nu(x) <= (x/2)^nu e^x / Gamma(nu + 1)` for all `x > 0`. So `z r_j <= e^beta (beta/2)^{2j} / (2j+1)!`.
Then `eps_J <= e^{2 beta_+} sum_{j>J} (2j+1)^2 (beta_+/2)^{2j} / (2j+1)!`, monotone in beta. HOLDS for every beta_+.
The successive-term ratio is `((2j+2)/(2j+1))^2 (beta_+/2)/(2j+2) -> 0`, so `eps_J -> 0`. HOLDS.

**"Not SU(2)-selective".** `|chi_j| <= d_j` and `x >= -1` hold on any subgroup. HOLDS.

**(J21) (READ).** It matches the checked (G15)-(G17a): on `V (x) Sym^{12k} V` the eigenvalues are
`r_{6k-1/2} <= (beta/2)^{12k-1}/(12k)!` and `r_{6k+1/2} <= (beta/2)^{12k+1}/(12k+2)!`. The note's sum of the two
bounds dominates their maximum. The Gamma and U(1) lower bounds `beta_-/(4 e^{beta_+})` and `beta_-/(2 e^{beta_+})`
are those of `gap-tree-check-opus.md` line 150. HOLDS.

The ARGUED paragraphs (lines 546-560, 582-599) are scope statements. They claim no proof. I found nothing false in them.

**Verdict I: HOLDS.**

## J. (J22)-(J23): low-spin averaging of (LC) (lines 612-651)

`C_N = exp(i pi sigma_3 / N)` acts on spin j with eigenvalues `e^{2 pi i m / N}`, `m = -j..j` in steps of one.
Haar conjugation averages `D^j(g C g^{-1})` to `(chi_j(C_N)/d_j) I`. Independence multiplies the means.
So the eigenvalue is `c_{j,N}^N`. HOLDS.
`cos u >= 1 - u^2/2` and `sum m^2 = (2j+1) j (j+1)/3` (checked at j = 1/2: 1/2; j = 3/2: 5) give (J22). HOLDS.
If `x_j = 2 pi^2 j(j+1)/(3N^2) <= 1`, then `c >= 1 - x_j >= 0` and Bernoulli gives `c^N >= 1 - N x_j`.
Monotone in j up to J. (J23) HOLDS. At j = 1/2, `c = cos(pi/N)`, which is (E18) of `gap-ext-astra.md`. HOLDS.
`-I` acts as `(-1)^{2j}`, of norm one. HOLDS.

**Verdict J: HOLDS.**

## K. The control table (lines 655-671)

Row 1, (J2)-(J4) for U(1) and Gamma: both contain `-I`, and `U_l -> -U_l` preserves their Haar measure. SC and
the telescoping are group-free. HOLDS.
Row 2, small beta: (J6)-(J8) use only `|x| <= 1`, the `-I` symmetry and the combinatorics. HOLDS.
Precision: the lower bound `F >= 0` in (J9) uses `Z_{m+v} <= Z_m`, inherited for SU(2). For the controls it needs
the same inherited inequality (reflection positivity holds for any compact group); the note does not state it.
The upper bounds hold without it. (J10)'s coefficient `1/4` is SU(2)-specific and is not claimed for the controls.
Row 3, (J19): HOLDS (section I). Row 4, (J21): HOLDS (section I). Row 5, (LC): matches the checked
`gap-ext-check-opus.md` line 98. Row 6: OPEN, correctly. The closing sentence claims no falsity of (E17) for the
controls. HOLDS.

**Verdict K: HOLDS** (one precision).

## L. Scope of (J13) and the RESULT line

**Does (J13) refute (J11) only for the stated ordering?** Yes. D_0(S) equals `Z_S^dec / Z_0` only when no odd
surface precedes S. In another ordering, earlier odd surfaces carry flipped signs inside `Xi_comp(S)`, and (J14)-(J15)
no longer apply. The refutation covers every ordering that puts some flat (r,i) plane first, on infinitely many tori.
The note's "for this ordering" and "a natural ordering" (line 344) are accurate.

**Does it leave (J12) open?** Yes. (J12) asks for `C_1 a^b e^{-kappa a}` per root face. The lower bound
`216^{-A}` with `A >= a^2` decays faster than any `e^{-kappa a}`. Even the `N_perp` planes give at most a polynomial
times `216^{-a^2}` from below. No contradiction arises. The note says so (lines 380-383).

**RESULT line (line 723).** Each clause matches a proved item: the exact representation (A), the strong-coupling area
bound and leading coefficient (F, at `beta <= 1/2400` and at fixed volume respectively), the refutation of the uniform
`q^A` budget for the stated ordering (B-D), the fixed-face tail with the same denominator (I), and (J12), (E17), (FQ),
(V) left open. "Not independently checked" was true when written. The line is FAIR.

## Verdict table

| Item | Lines | Verdict |
|---|---|---|
| A. (J4) telescoping identity, no positivity | 137-156 | HOLDS |
| (J2), unique decomposition, cocycle pairing | 97-121 | HOLDS |
| (J3) pointwise positivity | 123-135 | HOLDS |
| "outside row 809's class" remark | 174-177 | not load-bearing; ARGUED-level |
| B. (J14) exact first activity | 386-402 | HOLDS |
| B. kernel positivity, `C_cosh >= C_1` | 404-416 | HOLDS |
| B. two-cut min-max comparison | 418-427 | HOLDS |
| B. factorization and torus Schur sum (J15) | 429-445 | HOLDS |
| C. `|N(S)| = 9A`, `k_e <= 6`, `sum k_e = 9A` | 447-460 | HOLDS |
| C. `log z(u) <= u^2/8` via Theorem V | 462-465 | HOLDS |
| C. induction and (J16) | 466-473 | HOLDS |
| D. (J17), bracket `> 1/216` at beta = 1/2, (J13) | 476-489 | HOLDS |
| (J5) against SA's rooted theorem | 181-198 | HOLDS |
| (J6), count `400^{k-1}`, arithmetic | 200-220 | HOLDS |
| (J7), vacuum cancellation, delta_Lambda | 222-243 | HOLDS |
| (J8) | 245-260 | HOLDS |
| (J9) and (E17) at small beta | 262-275 | HOLDS |
| (J10) leading planes | 277-297 | HOLDS (remainder is in fact O(beta^2)) |
| Mack-Meyer convention | 299-313 | internally consistent; paper NOT CHECKED |
| (J11) implication | 329-345 | HOLDS |
| (J12) implication to Q_F | 347-365 | HOLDS (read "for some fixed ordering") |
| (J5) violation at U = 1, beta = 1/2 | 491-502 | HOLDS |
| (J18)-(J20) | 508-544 | HOLDS (J20 re-derived without GL4) |
| (J21) reuse | 562-580 | HOLDS |
| (J22)-(J23) | 612-642 | HOLDS |
| Control table | 655-671 | HOLDS (state `Z_{m+v} <= Z_m` for controls) |
| Scope of (J13); (J12) left open | 369-384 | HOLDS |
| RESULT line | 723 | FAIR |

Nothing FAILS. Precisions, none changing a conclusion:
1. (J10): the remainder is `O(beta^2)`; `O(beta)` is true but weak.
2. (J12): the activities depend on the ordering; read the criterion for some fixed ordering.
3. Control table, row 2: `F >= 0` for U(1) and Gamma needs the inherited `Z_{m+v} <= Z_m`, not stated there.
4. Line 494: "three ... exist" means "at least three".
5. Lines 174-177: the row-809 class remark is argued, not proved; nothing depends on it.
The Mack-Meyer reading (lines 299-313) was not checked against the paper.

Checked line by line by Claude Opus 5.5. Credit Codex gpt-6-astra max for (J4), (J13)-(J17) and (J22)-(J23).

RESULT: Every PROVED step of gap-joint-astra.md HOLDS on a hand re-derivation by Claude Opus 5.5 — the telescoping identity (J4), the positive-transfer bound (J15), the local normalization bound (J16) and hence (J13) at beta = 1/2, the strong-coupling chain (J5)-(J10), the (J5) violation, (J18)-(J20) and (J22)-(J23) — nothing FAILS, five wording precisions change no conclusion, (J13) refutes (J11) only for orderings that put a flat plane first and leaves (J12) open, and the RESULT line is fair.
