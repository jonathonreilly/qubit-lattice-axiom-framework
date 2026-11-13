# The general surface tail by a Kraft-weighted exploration code (FINISH row 833), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`. `git pull --ff-only` at the start: "Already up to date" at
  `83f6ffafe92a18e8d6d415b47453e830424e4160`. During the run the clone advanced to
  `7f5a581faaf2a0607c6f315da65fd326a677e0b7` (rows 831-839, other lanes). `git diff --stat` between the two
  commits is empty for every source read here.
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
- Read in full: `D/library/gap-flat-astra.md` (691 lines), `D/library/gap-rtail-astra.md` (805),
  `D/library/gap-sos-astra.md` (655), all by Codex gpt-6-astra; their checks `D/library/gap-flat-check-opus.md` (151),
  `D/library/gap-rtail-check-opus.md` (162), `D/library/gap-sos-check-opus.md` (208), all by Claude Opus 5.5, all HOLD.
  Read in part: `D/library/gap-joint-astra.md` lines 40-510 ((J1)-(J17)); `D/library/gap-expose-astra.md` lines 573-658
  ((E16)-(E18)); `D/library/gap-vmf-lip.md` lines 419-608 (Theorem DOB); `D/library/gap-fusion-astra.md` lines 85-135
  (the witness (2)); `D/library/gap-ext-astra.md` lines 60-180 ((E1)-(E5), (FQ)); `D/library/gap-novelty-opus.md` lines 1-80;
  `D/library/gap-arealaw-opus.md` lines 1-380.
- No repository file was edited. Only this output file was written.
- Marks. PROVED: proved here by me, by hand. READ: read in the named source (path and line). ARGUED: an argument
  short of proof standard. GUIDE: a numeric run that guided a choice and decided nothing. OPEN: not settled.
- GUIDE runs: small Python scripts (well under 1 MB, seconds each) in
  `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane833/guide/`.
  They optimised the free parameters of the Kraft weights and searched for simple fractions. Every inequality
  used below is then checked by hand with exact fractions.
- Credits. Codex gpt-6-astra: (F1)-(F28) of gap-flat-astra, (R1)-(R28) and the exploration code (R4) of
  gap-rtail-astra, (S1)-(S25) of gap-sos-astra, (J1)-(J17) of gap-joint-astra, (E16)-(E17) of gap-expose-astra,
  Theorem DOB of gap-vmf-lip, the witness (2) of gap-fusion-astra. Claude Opus 5.5: the line-by-line checks of
  gap-flat, gap-rtail and gap-sos. Claude Fable 5.2: Proposition SC and the area lemma (gap-kappa-order.md:31-74,
  as cited in gap-flat-astra.md:30-33). Kraft's inequality is classical (L. G. Kraft, 1949); Finner's inequality is
  H. Finner (1992), as identified in gap-flat-check-opus.md section 3.

## 0. Answer in brief

1. **PROVED (counting).** A breadth-first exploration code for link-connected closed plaquette sets in which a
   link carries a label only for the plaquettes it reveals. With Kraft weights, "closing" links, where every surface
   plaquette is already known, cost nothing. Consequence: at most `5^(n-1)` surfaces of area n with all links of
   degree two pass through a given plaquette (Corollary C5), against `400^(n-1)` in (B30) and sixteen labels per
   exceptional link in (R4).
2. **PROVED (Haar weights; Lemma P).** Integrate the link variables in the code's own order. Then each plaquette is
   integrated out at the link where it is discovered, against only the plaquettes discovered with it:
   `int prod_(p in S) |sinh(beta x_p)| <= sinh(beta) prod_e (sinh beta)^|sigma_e| E|x|^|sigma_e|` for **every**
   surface, branched or not. Closing links, branching ones included, cost nothing, and no Finner penalty appears.
3. **PROVED (main result; Theorems T4 and T6).** With `q = (sinh(beta)/2) cosh(beta)^8`: whenever
   `(20/3) q(beta) <= rho < 1`, the (F8) majorants of **all** odd surfaces sum to at most `(8/15) N_perp rho^A` (T4;
   this covers `0 < beta <= 7/30` with `rho = 0.9760`). Keeping the neighbourhood per link (T6) gives
   `B_O <= (51/100) N_perp (0.9697)^A` on `0 < beta <= 6/25`. With (F26) this proves (J12), (E17), RTAIL, (RTAIL*)
   and **(RTAIL-SOS) on the whole interval `(0, 6/25]`**, two-sided, with all decorations and the original `Z_m`.
   Since `6/25 > 2/9`, this passes the endpoint of the checked full seed (Theorem DOB). The earlier full-tail range
   was `beta <= 1/500` (F26).
4. **PROVED (Theorem T5).** Every odd surface whose links all have degree two (overhangs, folds, handles,
   simultaneous motion in both transverse directions, any excess) is controlled on `(0, 3/10]`:
   `sum u(S) <= (3 pi/20) N_perp (40 q/(3 pi))^A` with `40q/(3pi) < 0.9267`.
5. **What remains (OPEN).** On `(6/25, 3/10]`, (RTAIL-SOS) is equivalent to (RTAIL-BR), the signed remainder of the
   families containing a branched odd surface outside `G_**`. On `(3/10, 5/11]` unbranched surfaces outside `G_**` are
   open too. This encoding stops near `beta = 0.2497` for all surfaces and `0.314` for unbranched ones (GUIDE). Reaching
   `1/3` needs a degree-two discovery entropy below `4.51` (it is 5 here) and branching at closing links far cheaper
   than here. These are limits of the encoding, not lower bounds on surfaces or Wilson weights.
6. **Seed (READ, not re-checked).** (E17) is the consumer's input. If the lane's recorded continuation from (FQ) to a
   full seed holds as stated, the seed and lattice gap extend to `beta <= 6/25`. This does not reach the unrefereed
   `1/3` and `0.348` claims recorded in gap-novelty-opus.md.
7. **Group dependence.** All steps are group-blind between SU(2) and the binary icosahedral group (section 11), as
   expected for a strong-coupling-type bound. Nothing is said at weak coupling.
8. **Record of the first route.** Sections 4 to 8 bound the Haar integral with Finner's inequality. They prove the
   full tail on `(0, 1/6]` (T1), unbranched surfaces on `(0, 7/25]` (T2), a sharper branching lemma (Lemma B) and
   isolated-branching surfaces on `(0, 2/9]` (T3). All remain correct; section 9 supersedes them as bounds.

## 1. Inputs, all READ

**R1 (exact representation; READ gap-joint-astra.md:97-156).** `Z_m = int C(U) Xi(w_m; U) dU`, with the
connected closed parity surfaces as polymers and link sharing as incompatibility (J2). For any ordering of the odd
surfaces, `p_m(v) = sum_(S in O) D_m(S)` (J4). Here O is the set of link-connected closed mod-two plaquette sets
with odd pairing with the twist.

**R2 (majorant; READ gap-flat-astra.md:142-205, checked gap-flat-check-opus.md section 2).** For compatible marked
families H, `|W_m(H)| <= prod_(S in H) u(S)` with

    u(S) = (cosh beta)^|N(S) \ S| * int dU_E(S) prod_(p in S) |sinh(beta x_p)|.          (F8)

For any class F ordered first and any majorants `b(S) >= u(S)` with `B_F = sum_(S in F) b(S)`:
`sum_(S in F) |D_m(S)| <= B_F e^(2 B_F)` and `|T_m(F)| <= (e^(2 B_F) - 1)/2` (F9). With `F = O` this holds for any
ordering (F26, `L = 0`; gap-flat-astra.md:503-511, checked gap-flat-check-opus.md section 6). All decorations stay
inside, and the denominator is the original `Z_m`.

**R3 (Finner's inequality and moments; READ gap-flat-astra.md:209-238, checked gap-flat-check-opus.md section 3).**
If nonnegative `f_p` depend on independent link variables and `sum_(p ni e) 1/h_p <= 1` at every link e, then
`int prod f_p <= prod ||f_p||_(h_p)` (F10). For Haar SU(2) and `x = tr(U)/2`: `E x^2 = 1/4`, `E x^4 = 1/8`,
`E x^6 = 5/64` (F11, from the recursion for the even moments at gap-flat-astra.md:226-236), and
`|sinh(beta x)| <= |x| sinh beta`.

**R4 (area lemma and rooting; READ gap-rtail-astra.md:81-88, 135-139).** Every `S in O` has an odd number, hence
at least one, of horizontal `(r,i)` plaquettes over each of the A base faces. So `|S| >= A`. The first such
plaquette over a fixed base face `f_0`, in a fixed order of its stack, is a root with at most `N_perp` choices.

**R5 (consumer; READ gap-expose-astra.md:575-599, gap-fusion-astra.md:95-133).** (E17) is
`Q_F <= C a^p eta_*^(a/2)` with `Q_F = max_(m_2 = 0, i = 3,4) p_(m,i)(a)` (E16). The witness
`S_ev(t; B) >= eta(beta)^t` with `eta(beta) = e^(-80 beta) r(beta)^4/(4 + 16 r(beta)^4) > 0` holds for every
`beta > 0` (gap-fusion-astra.md (2)). Any area decay therefore beats `eta_*^(a/2)` for every fixed `eta_*`.

**R6 (the classes already proved; READ gap-sos-astra.md:513-575, checked gap-sos-check-opus.md section 7).**
`G_** = A_* union H union P_* union F_SOS` has `B_(G_**) <= 8 N_perp e^(-tau A)` on `0 < beta <= 5/11` (S23), and
(RTAIL-SOS) is the signed remainder `R_m^**` after ordering `G_**` first (S25).

**Notation.** `c = cosh beta`, `s = (sinh beta)/2`, `q = s c^8`. A *surface* is a nonempty link-connected closed
mod-two set of plaquettes in the four-torus with all periods at least three. For a surface S and a link e,
`d_e = d_e(S)` is the number of plaquettes of S containing e: 0, 2, 4 or 6. `E(S)` is the set of links with
`d_e > 0`. A link is *branching* if `d_e >= 4`. Six distinct plaquettes contain each link, since all periods are at
least three. Two distinct plaquettes share at most one link.

## 2. A code that charges only discoveries (PROVED)

This section is pure combinatorics. It refines the exploration code (R4) of gap-rtail-astra.md:122-176.
There every exceptional link carries one of sixteen labels. Here a link carries a label only for the plaquettes it
reveals, and Kraft weights replace counting.

**Definitions.** Fix a plaquette `p_0`, a total order on links, and an order of the six plaquettes `P(e)` at each
link e. A *decoder state* is a pair (Disc, Proc): a finite set of discovered plaquettes containing `p_0`, and a set
of processed links. A link is *pending* if it lies in some discovered plaquette and is not processed. The decoder
starts at `({p_0}, empty)`. While some link is pending, it takes the least pending link e and puts
`D_e = Disc ∩ P(e)`, `D = |D_e| >= 1`. It reads one *label* `sigma`, a subset of `P(e) \ Disc` such that
(i) `D + |sigma|` is even and (ii) no plaquette in `sigma` contains a processed link. It then sets
`Disc := Disc ∪ sigma` and `Proc := Proc ∪ {e}`. It halts when no link is pending and outputs Disc.

**Lemma K1 (encoding; PROVED).** Let S be a surface containing `p_0`. Run the decoder with the labels
`sigma_e = (S ∩ P(e)) \ Disc`. Then every label is allowed, the run halts with `Disc = S`, the processed links are
exactly `E(S)`, and at each processed link `d_e(S) = |D_e| + |sigma_e|`. Distinct surfaces give distinct label
sequences.

*Proof.* By induction `Disc ⊂ S`, so `D_e ⊂ S ∩ P(e)` and `S ∩ P(e) = D_e ∪ sigma_e`. Its size `d_e` is even by
closure, which is (i). Suppose `q in sigma_e` contained a processed link e'. At e' all of `S ∩ P(e')` was added
to Disc, and q lies there; so q was already discovered. This contradicts `q notin Disc`, which proves (ii). At
halting, every link of every discovered plaquette is processed, and at a processed link all plaquettes of S there
are discovered. If some `q in S` were undiscovered, take a chain `p_0 = f_0, f_1, ..., f_k = q` in S with
consecutive plaquettes sharing a link (S is link-connected), and the first undiscovered `f_j`. The link shared by
`f_(j-1)` and `f_j` is a link of a discovered plaquette, hence processed, hence `f_j` is discovered. This
contradiction gives `Disc = S`. A processed link lies in a plaquette of S, so it is in `E(S)`; conversely every link
of S lies in a discovered plaquette and gets processed. The decoder's choices depend only on its state and the
labels already read, so the label sequence determines the run and its output S. QED

**Lemma K2 (Kraft inequality for this code; PROVED).** Let `w(sigma | state) >= 0` be weights such that, at every
decoder state with a pending link, the weights of the allowed labels sum to at most one. Then

    sum over surfaces S containing p_0 of  prod_(e in E(S)) w(sigma_e | state at e)  <=  1.            (K2)

*Proof.* Each step processes a new link, and the torus has finitely many links, so every run halts after a bounded
number of steps. For a state s let `T(s)` be the sum, over all halting continuations from s, of the product of the
weights read. A halting state has `T = 1`. Otherwise `T(s) = sum_sigma w(sigma | s) T(s.sigma)`, an empty sum being
zero when no label is allowed. By induction on
the largest number of remaining steps, `T(s) <= sum_sigma w(sigma | s) <= 1`. By Lemma K1 the encoder maps distinct
surfaces through `p_0` to distinct halting runs, so the left side of (K2) is at most `T(initial) <= 1`. QED

**Corollary C5 (degree-two surfaces; PROVED).** Let `N_2(n)` be the number of surfaces of area n through `p_0`
with `d_e = 2` at every used link. Then `sum_n N_2(n) 5^(1-n) <= 1`; in particular `N_2(n) <= 5^(n-1)`.

*Proof.* Use the weights `1/5` on one-plaquette labels at states with `D = 1`, weight 1 on the empty label at states
with `D = 2`, and weight 0 otherwise. Each state's allowed labels have total weight at most one, since at `D = 1`
there are at most five one-plaquette labels. For a surface with all degrees two, each processed link has either
`(D, |sigma|) = (1, 1)` or `(2, 0)`, since `D + |sigma| = 2` and parity excludes `(1, 0)`. Every plaquette other than
`p_0` is discovered exactly once, so exactly `n - 1` links have `D = 1`. The product in (K2) is `5^(1-n)`. QED

**Remark (comparison; PROVED).** For the same class the uniform link code would charge five per link, `25^n`
in total, since such a surface has `2n` links. Kraft weighting charges only the `n - 1` discoveries. The `n + 1`
closing links are free. The connected-set count (B30) used in (F25) charges 400 per plaquette.

## 3. The majorant as a product over links (PROVED)

**Lemma U.** For every surface S,

    u(S) <= prod_(e in E(S)) phi(d_e),   phi(2) = c^4 s^(1/2),   phi(4) = 2 c^2 s,   phi(6) = 5 s^(3/2).     (U)

In particular `u(S) <= q^|S|` when every used link has degree two.

*Proof.* (a) Neighbourhood. Each plaquette of `N(S) \ S` contains a link of `E(S)`. At such a link e it is one of the
`6 - d_e` plaquettes of `P(e)` outside S. Counting each one at every such link overcounts, so
`|N(S) \ S| <= sum_(e in E(S)) (6 - d_e)`. This is the inequality (S7) of gap-sos-astra.md:231-241, now for every
surface. (b) Haar. In (F10) take `h_p = max_(e in p) d_e` for `p in S`. At a link e, the `d_e` plaquettes of S
containing e have `h_p >= d_e`, so `sum_(p ni e) 1/h_p <= 1`. Each `U_p` is Haar distributed, so
`|| sinh(beta x_p) ||_h <= sinh(beta) (E|x|^h)^(1/h) = F(h)`, with `F(2) = s`, `F(4) = 2 s 8^(-1/4) = 2^(1/4) s` and
`F(6) = 2 s (5/64)^(1/6) = 5^(1/6) s`. (c) Distribution over links. Put `g(2) = 1`, `g(4) = 2^(1/4)`,
`g(6) = 5^(1/6)`. All three are at least one, so `F(h_p) = s g(max_(e in p) d_e) <= s prod_(e in p) g(d_e)`. Hence

    prod_(p in S) F(h_p) <= prod_(p in S) prod_(e in p) s^(1/4) g(d_e) = prod_(e in E(S)) (s^(1/4) g(d_e))^(d_e).

Multiply by (a): `u(S) <= prod_e c^(6 - d_e) s^(d_e/4) g(d_e)^(d_e)`, which is (U), since `2^(4/4) = 2` and
`5^(6/6) = 5`. If all degrees are two, `|E(S)| = 2|S|` and the product is `(c^4 s^(1/2))^(2|S|) = q^|S|`. QED

The ratios that measure branching are `kappa := phi(4)/phi(2)^2 = 2 c^(-6)` and
`lambda := phi(6)/phi(2)^3 = 5 c^(-12)`. Both are at most their values 2 and 5 at `c = 1`.

## 4. Theorem T1: the whole odd-surface tail for 0 < beta <= 1/6 (PROVED)

**Theorem T1.** Let `P, y > 0` satisfy, with `kappa = 2`, `lambda = 5`,

    K1 = 5Py + 10 kappa P^2 y^3 + lambda P^3 y^5 <= 1,     K2 = P + 6 kappa P^2 y^2 + lambda P^3 y^4 <= 1,
    K3 = 3 kappa P^2 y + lambda P^3 y^3 <= 1,              K4 = kappa P^2 + lambda P^3 y^2 <= 1,
    K5 = lambda P^3 y <= 1,                                K6 = lambda P^3 <= 1.                       (K)

Then, at every `beta > 0` and for every plaquette `p_0`,

    sum over surfaces S containing p_0 of  u(S) (P^2 y/q)^|S|  <=  y.                                  (T1a)

Consequently, if `q(beta) <= rho P^2 y` with `rho <= 1`,

    B_O := sum_(S in O) u(S) <= N_perp y rho^A.                                                         (T1b)

*Proof.* Put `X = P/phi(2)`. For an allowed label at a state with `|D_e| = D`, put
`w(sigma | state) = phi(D + |sigma|) X^((D + |sigma|)/2) y^|sigma|`. Allowed labels have `D + |sigma|` even, between 2
and 6. Dropping condition (ii) only adds terms, so the weight of the allowed labels at such a state is at most
`sum_j binom(6 - D, j) phi(D + j) X^((D + j)/2) y^j`, over `j` with `D + j` even. Since `phi(2) X = P`,
`phi(4) X^2 = kappa_c P^2` and `phi(6) X^3 = lambda_c P^3`, with `kappa_c = 2c^(-6) <= 2` and
`lambda_c = 5 c^(-12) <= 5`, these sums are the six expressions (K) at `(kappa_c, lambda_c)`. Each is increasing in
kappa and lambda, so each is at most one. The binomial coefficients are `5, 10, 1` for `D = 1`; `1, 6, 1` for
`D = 2`; `3, 1` for `D = 3`; `1, 1` for `D = 4`; `1` for `D = 5, 6`. Lemma K2 applies. By Lemma K1, along the encoder
of S the exponents add to `sum_e d_e = 4|S|` and `sum_e |sigma_e| = |S| - 1`. So the product of weights is
`prod_(e in E(S)) phi(d_e) (X^2 y)^|S| / y`, and `X^2 y = P^2 y/phi(2)^2 = P^2 y/q`. Lemma U gives (T1a).
For (T1b), every `S in O` has `|S| >= A` and contains its root over `f_0`, one of `N_perp` plaquettes (R4). If
`q <= rho P^2 y`, then `(P^2 y/q)^|S| >= rho^(-|S|) >= rho^(-A)`, since `rho <= 1`. So (T1a) gives
`sum u(S) <= y rho^A` over the odd surfaces with a given root. Sum over the `N_perp` roots. QED

**The choice `P = 7/12`, `y = 2/7` (PROVED by exact arithmetic).** Here `P^2 y = 7/72`, and

    K1 = 5/6 + 10/63 + 5/2646 = 2630/2646,     K2 = 7/12 + 1/3 + 5/756 = 698/756,
    K3 = 7/12 + 5/216 = 131/216,               K4 = 49/72 + 140/1728 = 1316/1728,
    K5 = 490/1728,                             K6 = 1715/1728.

For instance `10 kappa P^2 y^3 = 20 (49/144)(8/343) = 7840/49392 = 10/63` and
`lambda P^3 y^5 = 5 (343/1728)(32/16807) = 160/84672 = 5/2646`, using `16807 = 49 * 343`. All six are below one.
So T1 holds whenever `(72/7) q(beta) <= rho < 1`.

**The interval (PROVED).** For `0 <= x < sqrt(6)` the successive terms of the sinh series have ratios at most
`x^2/6`, so `sinh x <= x/(1 - x^2/6)`. Also `log cosh t <= t^2/2` (its derivative is `tanh t <= t`), and
`e^u <= 1/(1 - u)` for `0 <= u < 1`. At `beta = 1/6`: `s <= (1/12)(216/215) = 18/215` and
`c^8 <= e^(1/9) <= 9/8`. Hence `q <= 81/860` and `(72/7) q <= 5832/6020 = 1458/1505 < 1`. Since q increases with
beta, on the whole interval `0 < beta <= 1/6`,

    B_O <= (2/7) N_perp (1458/1505)^A <= (8/7) a^2 (1458/1505)^(a^2).                                  (T1c)

**Consequences on `(0, 1/6]` (PROVED from T1 and R2, R5).** Put `tau_1 = log(1505/1458)`. Since
`log(1 + u) >= u/(1 + u)`, `tau_1 >= 47/1505 > 1/33`. Since `x e^(-tau x) <= 1/(e tau)`, `B_O < (8/7)(33/e) < 14`.
By (F26) with `F = O`,

    sum_(S in O) |D_m(S)| <= B_O e^(2 B_O) <= (8/7) e^28 a^2 (1458/1505)^(a^2),                         (T1d)

uniformly in the box, the crossed pair, the twist and `0 < beta <= 1/6`. Therefore:
- (J12) holds, since a rooted sum is at most the whole sum.
- `0 <= p_m(v) <= (8/7) e^28 a^2 e^(-tau_1 a^2)`. With `kappa_* = (1/2) log(1/eta_*)` and
  `-tau_1 a^2 + kappa_* a <= kappa_*^2/(4 tau_1)`, this gives (E17):
  `Q_F <= C a^2 eta_*^(a/2)`, `C = (8/7) e^(28 + 33 kappa_*^2/4)`, for every fixed `0 < eta_* < 1`.
- RTAIL, (RTAIL*) and (RTAIL-SOS) hold on `(0, 1/6]`, even two-sided. For example
  `R_m^** = p_m(v) - T_m(G_**)`, `|T_m(G_**)| <= (e^(2 B_(G_**)) - 1)/2 <= B_O e^(2 B_O)`, so
  `|R_m^**| <= 2 B_O e^(2 B_O)`.

The constant `e^28` is explicit and enormous; it is not optimised. A GUIDE run with coupling-dependent parameters
(using `c > 1` at the endpoint) finds feasible weights with rate below one up to about `beta = 0.185`; this note
claims only `1/6`.

## 5. Theorem T2: every unbranched odd surface, up to beta = 7/25 (PROVED)

**Theorem T2.** Let `O_2` be the odd surfaces with `d_e = 2` at every used link. If `5 q(beta) <= 1`, then

    sum_(S in O_2) u(S) <= (N_perp/5) (5q)^A.                                                         (T2)

*Proof.* Lemma U gives `u(S) <= q^|S| = (5q)^|S| 5^(-|S|)`. For a fixed root, `|S| >= A` and `5q <= 1` give
`sum u(S) <= (5q)^A (1/5) sum_S 5^(1 - |S|) <= (5q)^A/5` by Corollary C5. Sum over the `N_perp` roots (R4). QED

**Intervals (PROVED).** At `beta = 1/4`: `s <= (1/8)(96/95) = 12/95` and `c^8 <= e^(1/4) <= 4/3`, so
`5q <= 16/19`. At `beta = 7/25`: `s <= (7/50)(3750/3701) = 525/3701 < 0.14186`. With `u = 4 beta^2 = 196/625`,
`c^8 <= e^u <= 1 + u + u^2/(2(1 - u/3)) = 1 + 196/625 + 57624/1049375 < 1.3686`; the series bound uses
`n! >= 2 * 3^(n-2)` for `n >= 2`, as in (F22). So `5q < 5 * 0.14186 * 1.3686 < 0.9708`. Hence (T2) is area-small,
uniformly, on `0 < beta <= 7/25`. (GUIDE: `5q = 1` near `beta = 0.2855`.)

**Scope (PROVED).** `O_2` has no excess cutoff and no graph condition. It contains every flat plane; every
admissible SOS graph without four-way contacts; every one-step terrace without checkerboard vertices; every
separated pillar; every fold or overhang whose links have degree two; every handle or tube whose junctions have
degree two; every surface moving in both transverse directions whose links have degree two; and surfaces with
singular vertices, since only link degrees matter. So, on `(0, 7/25]`, three of the four obstacles named in
gap-sos-astra.md:576-599 (overhangs, general handles, simultaneous transverse motion) are removed, together with
the winding and full-period walls of its fourth bullet, *except where some link branches*. What `O_2` misses is
exactly the surfaces with a link of degree four or six.

**Remark (PROVED).** (T2) is an absolute bound on the class, as (S18) is for `F_SOS`. On the common range
`beta <= 5/11` the two overlap: an SOS graph without four-way contacts lies in both. Neither contains the other.

## 6. Branching links: a sharper Haar bound when no plaquette carries two of them (PROVED)

Lemma U charges a link of degree four the Finner factor `2 = (2^(1/4))^4` and a link of degree six the factor
`5 = (5^(1/6))^6`. These factors are attained only when the four (six) plaquette holonomies are aligned. Integrating
the branching link first sees the misalignment.

**Lemma B.** Let S be a surface in which no plaquette contains two branching links. Let `b_4, b_6` count its links of
degree four and six. Then

    int prod_(p in S) |sinh(beta x_p)| dU_E(S)  <=  s^|S| g4^(b_4) g6^(b_6),
    g4 = (2/3)(1 + 2^(-1/2)) < 239/210,   g6 = 1 + 2^(-1/2) < 239/140.                               (B)

*Proof.* *Step 0.* `|sinh(beta x)| <= 2s|x|`, so it suffices to prove
`J(S) := int prod_(p in S) |x_p| <= 2^(-|S|) g4^(b_4) g6^(b_6)`. Write unit quaternions for SU(2), so
`x(U) = Re U = <U, 1>` and `Re(ab) = <a, conj(b)>` in R^4.

*Step 1 (one link).* Let `p` contain the link e. A cyclic rotation of the holonomy and, if needed, an inversion
leave `x_p` unchanged and put it in the form `U_e V_p`, where `V_p` is the product of the other three link
variables of p. So `x_p = <U_e, W_p>` with `W_p = conj(V_p)`, a unit vector depending only on the other three links
of p.

*Step 2 (moments).* Haar measure on SU(2) is the uniform measure on `S^3`. Its moment tensors are invariant under
O(4), so `E[U^(tensor 2k)]` is a multiple of the sum of the `(2k - 1)!!` pairings of Kronecker deltas. Contracting
with `a^(tensor 2k)` and using (F11) fixes the multiple: `(1/8)/3 = 1/24` for `k = 2`, `(5/64)/15 = 1/192` for
`k = 3`. Hence, for unit vectors a, b, c,

    E <U,a>^2 <U,b>^2 = (1 + 2<a,b>^2)/24,
    E <U,a>^2 <U,b>^2 <U,c>^2 = (1 + 2(<a,b>^2 + <a,c>^2 + <b,c>^2) + 8<a,b><b,c><c,a>)/192.

The second line lists the 15 pairings of `{a,a,b,b,c,c}`: one pairs equal letters, six pair one equal couple, and
eight pair no equal letters.

*Step 3 (one branching link).* Let `a_i = <U_e, W_i>` for the plaquettes `p_i` at e. For degree four,
`prod_1^4 |a_i| <= (a_1^2 a_2^2 + a_3^2 a_4^2)/2`, so with `c_ij = <W_i, W_j>`,

    E_(U_e) prod_1^4 |a_i| <= (1 + c_12^2 + c_34^2)/24.

For degree six, `|a_1 ... a_6| <= (A^2 + B^2)/2` with `A = a_1 a_2 a_3`, `B = a_4 a_5 a_6`. Step 2 and
`|c_31|, |c_64| <= 1` give

    E_(U_e) prod_1^6 |a_i| <= (1/192)(1 + sum_(ij in 123) c_ij^2 + sum_(ij in 456) c_ij^2 + 4|c_12||c_23| + 4|c_45||c_56|).

*Step 4 (all branching links at once).* Let B be the set of branching links and `F_e = S ∩ P(e)`. By hypothesis no
plaquette contains two links of B. So the sets `F_e`, `e in B`, are disjoint, and every `W_p` with `p in F_e`
depends on no link of B. Fix all links outside B. The integrand is
`prod_(e in B) prod_(p in F_e) |<U_e, W_p>| * prod_(p notin union F_e) |x_p|`, and the `U_e`, `e in B`, are
independent Haar variables. Fubini and Step 3 bound the B-integral by `prod_(e in B) M_e`, where each `M_e` is the
displayed finite sum of nonnegative terms, each a constant times a function `Phi` equal to `1`, `c_ij^2` or
`|c_ij||c_jk|` of the non-B links.

*Step 5 (Finner on each term).* Expand the product into terms. Each term is a product of the untouched plaquette
functions `|x_p|` and one function `Phi` for each `e in B`. A non-B link `ell` of S has degree two; its two plaquettes
are each either untouched, or in some `F_e`. Each plaquette lies in at most one `F_e`, and the term contains exactly
one function `Phi` from each `M_e`. Two plaquettes of one `F_e` share only e, so they cannot both contain `ell`.
So at most two functions of the term depend on `ell`: one for each of its two plaquettes. Give every function the
exponent two; Finner's condition `sum 1/h <= 1` holds at every link. The norms are: `||x_p||_2 = 1/2`;
`||c_ij^2||_2 = (E x^4)^(1/2) = 2^(-3/2)`, since `W_i` and `W_j` are products over disjoint links, so `W_i conj(W_j)`
is Haar; and `|| |c_12||c_23| ||_2 = (E_(W_2)[E_(W_1)<W_1,W_2>^2 E_(W_3)<W_2,W_3>^2])^(1/2) = (1/16)^(1/2) = 1/4`,
since `E<W, a>^2 = |a|^2/4` and `W_1, W_2, W_3` are independent Haar. Summing the terms,

    J(S) <= 2^(-(|S| - sum_(e in B) d_e)) prod_(e in B) T_e,
    T_e = (1 + 2 * 2^(-3/2))/24 = (1 + 2^(-1/2))/24                      (d_e = 4),
    T_e = (1 + 6 * 2^(-3/2) + 8 * (1/4))/192 = (1 + 2^(-1/2))/64          (d_e = 6).

Finally `2^4 T_e = g4` and `2^6 T_e = g6`. The rational bounds use `2^(-1/2) < 99/140`, since
`99^2 * 2 = 19602 > 19600 = 140^2`. QED

The gain is a factor `g4/2 < 0.57` per degree-four link and `g6/5 < 0.35` per degree-six link.

**Corollary B1 (PROVED).** If no plaquette of S contains two branching links, then `u(S) <= prod_e phi_iso(d_e)`
with `phi_iso(2) = phi(2)`, `phi_iso(4) = g4 c^2 s`, `phi_iso(6) = g6 s^(3/2)`. Indeed combine (B) with
`|N(S) \ S| <= sum_e (6 - d_e)` from Lemma U (a). The branching ratios become `kappa = g4 c^(-6) < 239/210` and
`lambda = g6 c^(-12) < 239/140`.

**Theorem T3 (isolated branching, PROVED).** Let `O_iso` be the odd surfaces in which no plaquette contains two
branching links. Let `P, y > 0` satisfy (K) with `kappa = 239/210` and `lambda = 239/140`. If `q <= rho P^2 y` with
`rho <= 1`, then `sum_(S in O_iso) u(S) <= N_perp y rho^A`.

*Proof.* Use the weights of Theorem T1 with `phi_iso` in place of `phi`. Their state sums are the expressions (K) at
`(g4 c^(-6), g6 c^(-12))`, at most one. Lemma K2 sums over **all** surfaces through `p_0`, so no restriction of the
decoder is needed; on `O_iso` Corollary B1 bounds u by the product. The rest is the proof of T1. QED

**The choice `P = 11/14`, `y = 2/9` (PROVED by exact arithmetic).** Here `P^2 y = 121/882`. With
`kappa = 239/210`, `lambda = 239/140`:

    K1 = 55/63 + 2313520/30005640 + 10179488/22684263840 < 0.873016 + 0.077103 + 0.000449 < 0.9506,
    K2 = 11/14 + 28919/138915 + 1272436/630118440       < 0.785715 + 0.208178 + 0.002020 < 0.9960,
    K3 = 173514/370440 + 2544872/280052640               < 0.4775,
    K4 = 28919/41160 + 1272436/31116960                   < 0.7435,
    K5 = 636218/3457440 < 0.1841,    K6 = 318109/384160 < 0.8281.

For instance the middle term of K2 is `6 (239/210)(121/196)(4/81) = 694056/3333960 = 28919/138915`, with
`138915 = 15 * 21^3` and `28919 = 239 * 121`.

**The interval (PROVED).** At `beta = 2/9`: `s <= (1/9)(243/241) = 27/241`, and with `u = 16/81`,
`c^8 <= 1 + u + u^2/(2(1 - u/3)) = 1 + 16/81 + 62208/2978694 < 1.218416`. So `q <= 0.1365033`, and
`q/(P^2 y) <= 0.1365033 * 882/121 < 0.99502`. Hence on `0 < beta <= 2/9`,

    sum_(S in O_iso) u(S) <= (2/9) N_perp (0.99502)^A.                                               (T3)

The margin is small and the implied constants are very large; the statement is still a uniform area bound.
`O_iso` contains `O_2`. A GUIDE run with coupling-dependent weights finds rate below one for `O_iso` up to about
`beta = 0.235`.

## 7. How far this method reaches, and where it stops

*(Finner route of sections 4-6. Section 10 gives the reach of the peeling route of section 9.)*

**Proposition L (the rate is at least 5q; PROVED).** In Theorems T1 and T3, every admissible `(P, y)` has
`P^2 y <= 1/5`, so the certified rate `q/(P^2 y)` is at least `5q`. More generally, no Kraft certificate whose
weights depend only on `(|D_e|, |sigma_e|)` proves `N_2(n) < 5^(n-1)`.

*Proof.* `K1 >= 5Py` and `K2 >= P`, so `5 P^2 y <= K1 K2 <= 1`. For the second claim, let `w_1` and `w_2` be the
weights of a one-plaquette label at `D = 1` and of the empty label at `D = 2`. The first processed link of the root
is a state with `D = 1` and five allowed one-plaquette labels, so `5 w_1 <= 1`; also `w_2 <= 1`. For a degree-two
surface of area n the product of weights is `w_1^(n-1) w_2^(n+1) <= 5^(1-n)` (Corollary C5's count of states), so
(K2) can certify at best `N_2(n) <= 5^(n-1)`. QED

So the code cannot give area decay for degree-two surfaces once `q >= 1/5`, that is from about `beta = 0.2855`
(GUIDE). At `beta = 1/3`, `sinh(1/3) >= 55/162` and the first four binomial terms of `(1 + 1/18)^8` give
`q(1/3) > 0.2614` (GUIDE value 0.2627), so `1/q < 3.83`: one would need a count of the
relevant surfaces with growth below 3.83 per plaquette, with the same weights, against 5 here. This is a limit of
the encoding, not a lower bound on the true number of surfaces or on any Wilson weight. The true growth constant of
closed plaquette surfaces in four dimensions is not known to me; explicit families (tubes, trees of cube
boundaries) give lower bounds near 1.5 to 2.4 per plaquette (ARGUED, rough counts), far below 5.

**Where the full tail stops at 1/6 (GUIDE).** With Finner's constants (`kappa = 2`,
`lambda = 5` at `c = 1`), the GUIDE optimum of (K) is `P^2 y = 0.0979`, so the rate is near `10.2 q`; the binding
constraints are K1 and **K6**. K6 is the state of a degree-six link all of whose six plaquettes were found before the
link is processed: its only label is empty, so no entropy can absorb its Finner factor 5. K4 (degree four, all four
found) and the branching option at `D = 2` (six ways to add two plaquettes, weight `6 kappa P^2 y^2`) are the next
constraints. With the isolated constants of Lemma B the optimum rises to `P^2 y = 0.1404` (rate near `7.1 q`); with
no branching at all, to `1/5` (rate `5q`).

**Adjacent branching links (ARGUED).** Take two degree-four links e, e' sharing one plaquette p, with all other
plaquettes at e and e' distinct, all their other links of degree two, and no further shared links among the
plaquettes involved. Integrate `U_e` by Step 3 of Lemma B (pairing p with one other plaquette), then `U_(e')` with the
weighted splits `|a_1 a_2 a_3| <= (t a_1^2 a_2^2 + a_3^2/t)/2` and `|a_1 a_2 a_3| z^2 <= (t a_1^2 a_2^2 + a_3^2 z^4/t)/2`,
using `E<U,a>^2<U,z>^4 = (3 + 12<a,z>^2)/192`, and finish with Finner at exponent two. The seven plaquettes then cost
`(1/24)(0.13335 + 0.05180 + 2^(-3/2) * 0.13335) = 0.009679 = 1.239 * 2^(-7)`, below `g4^2 = 1.295` and far below
Finner's 3.36. So adjacency is not worse in this example. A general sequential version of Lemma B is not proved.

**The missing lemma, stated (OPEN).**

    (BR-SEQ)   int prod_(p in S) |x_p| dU  <=  2^(-|S|) g4^(b_4) g6^(b_6)   for every surface S.

(BR-SEQ) is Lemma B without the isolation hypothesis. If it holds, the proof of T3 applies to all of O with the same
weights, and gives the full tail, (E17) and (RTAIL-SOS) on `(0, 2/9]` (PROVED implication). Any weaker bound with
constants `(Gamma_4, Gamma_6)` in place of `(g4, g6)` suffices on the interval where (K) at
`(kappa, lambda) = (Gamma_4, Gamma_6)` admits `P^2 y > q(beta)`. Past `2/9` it gives at most about `0.235` (GUIDE,
coupling-dependent weights): this route alone cannot reach the unrefereed `1/3` and `0.348` claims recorded in
gap-novelty-opus.md:15-33.

## 8. Consequences for (RTAIL-SOS) and the exact remaining statements

*(Finner route. Superseded by section 10: Theorem T6 proves (RTAIL-SOS) on all of `(0, 6/25]`, so (RTAIL-ADJ)
below is no longer open there.)*

**On `(0, 1/6]` (PROVED).** Theorem T1 proves (RTAIL-SOS), (RTAIL*), RTAIL, (J12) and (E17), two-sided, with
the constants of (T1d). The "stronger target" `B_out` of gap-rtail-astra.md:704-713 is also proved there, since
`B_out <= B_O`.

**On `(1/6, 2/9]` (PROVED reduction; OPEN estimate).** Order `G_**` first, then `O_iso \ G_**`, then the rest, and put
`G_iso = G_** ∪ O_iso`. By (S23) and (T3), `B_(G_iso) <= 8 N_perp e^(-tau A) + (2/9) N_perp (0.99502)^A`. Define

    R_m^iso = (1/(2 Z_m)) int C(U) [ Xi(w_m^(G_iso); U) - Xi(w_m^O; U) ] dU,   p_m(v) = T_m(G_iso) + R_m^iso.

Exactly as in (S25), `R_m^** - R_m^iso = T_m(G_iso) - T_m(G_**)` is the sum of `D_m(S)` over `G_iso \ G_**` for this
ordering, and (F9) makes it area-small. So on any `I ⊂ (1/6, 2/9]`, (RTAIL-SOS) is equivalent, up to constants and
powers, to

    (RTAIL-ADJ)   R_m^iso <= C a^p eta_*^(a/2),

whose marked families each contain an odd surface in which some plaquette contains two branching links, outside
`G_**`. (BR-SEQ) would prove it.

**On `(2/9, 7/25]` (PROVED reduction; OPEN estimate).** The same construction with `G_2 = G_** ∪ O_2` and (T2)
reduces (RTAIL-SOS) to (RTAIL-BR): the signed remainder of the marked families containing an odd surface with a
link of degree four or six, outside `G_**`.

**On `(7/25, 5/11]` (OPEN).** Only the classes of `G_**` are controlled there; (T2) extends somewhat beyond 7/25 with
sharper arithmetic, but not past `q = 1/5`.

## 9. Peeling in exploration order: no branching penalty at all (PROVED; supersedes T1, T2, T3 as bounds)

Sections 4 to 6 integrate with Finner's inequality, which charges every plaquette at every link. A better order is
the decoder's own order. Then each plaquette is integrated out at the link where it is discovered, against only the
other plaquettes discovered there. Closing links, branching or not, then cost nothing.

**Lemma P (peeling; PROVED).** Let S be a surface through `p_0`, and let `e_1, ..., e_L` be the links of `E(S)` in the
order in which the encoder of Lemma K1 processes them. Put `N_k = E_Haar |sinh(beta x)|^k` (`N_0 = 1`) and
`M_k = E_Haar |x|^k`. Then

    int prod_(p in S) |sinh(beta x_p)| dU_E(S)  <=  N_(1 + |sigma_(e_1)|) prod_(i >= 2) N_(|sigma_(e_i)|)
                                                <=  sinh(beta) prod_(e in E(S)) (sinh beta)^|sigma_e| M_(|sigma_e|).      (P)

*Proof.* Integrate `U_(e_1)`, then `U_(e_2)`, and so on (Fubini; the integrand is bounded and nonnegative). Let
`S_i` be the plaquettes of S containing none of `e_1, ..., e_i`. Claim: after i steps the integral is at most
`prod_(j <= i) N_(k_j)` times the integral of `prod_(p in S_i) |sinh(beta x_p)|`, where `k_j` is the number of plaquettes
of `S_(j-1)` containing `e_j`. At step i, only those `k_i` plaquettes depend on `U_(e_i)`. For each of them,
`x_p = <U_(e_i), W_p>` with `W_p` a unit vector depending on the other three links of p (Step 1 of Lemma B), none of
which has been integrated, since `p in S_(i-1)`. Hölder's inequality with `k_i` equal exponents and Haar invariance
give `E_U prod |sinh(beta <U, W_p>)| <= prod (E |sinh(beta x)|^(k_i))^(1/k_i) = N_(k_i)`, a constant. This proves the
claim; `S_L` is empty.
Now identify `k_i`. For `i >= 2`, a plaquette of `S_(i-1)` at `e_i` was not discovered before step i: a discovered
plaquette other than `p_0` contains the link where it was discovered, which precedes `e_i`, and `p_0` contains `e_1`.
Conversely an undiscovered plaquette contains no processed link (Lemma K1). So the plaquettes of `S_(i-1)` at `e_i` are
exactly `sigma_(e_i)`, and `k_i = |sigma_(e_i)|`. At `i = 1` they are `p_0` and `sigma_(e_1)`. Finally
`N_(1+j) <= sinh(beta) N_j` and `N_j <= (sinh beta)^j M_j`, since `|sinh(beta x)| <= |x| sinh beta <= sinh beta`. QED

The moments are, by hand: `M_2 = 1/4`, `M_4 = 1/8`, `M_6 = 5/64` (F11), and for odd orders
`M_(2l+1) = (4/pi) I_(2l+1)` with `I_m = int_0^1 x^m sqrt(1 - x^2) dx`, `I_1 = 1/3` and
`I_(2l+1) = (2l/(2l + 3)) I_(2l-1)` (integrate the derivative of `x^(2l) (1 - x^2)^(3/2)`). So
`M_1 = 4/(3 pi)`, `M_3 = 8/(15 pi)`, `M_5 = 32/(105 pi)`.

**Corollary P1 (PROVED).** With `t = 2q = sinh(beta) c^8`, every surface satisfies

    u(S) <= t^|S| prod_(e in E(S)) M_(|sigma_e|),                                                       (P1)

the product being taken along the encoder of S. Indeed `c^(|N(S) \ S|) <= c^(8|S|)` (Lemma U (a) and
`|E(S)| <= 2|S|`), and `|S| = 1 + sum_e |sigma_e|`. No Finner exponent, and no isolation hypothesis, enters.

**Theorem T4 (the whole odd-surface tail, PROVED).** Let `a, Z > 0` satisfy

    J1 = 5 M_1 a Z + 10 M_3 a^2 Z^3 + M_5 a^3 Z^5 <= 1,     J2 = a + 6 M_2 a^2 Z^2 + M_4 a^3 Z^4 <= 1,
    J3 = 3 M_1 a^2 Z + M_3 a^3 Z^3 <= 1,                    J4 = a^2 + M_2 a^3 Z^2 <= 1,
    J5 = M_1 a^3 Z <= 1,                                    J6 = a^3 <= 1.                              (J)

Then for every `beta > 0` and every plaquette `p_0`, `sum_(S ni p_0) u(S) (a^2 Z/(2q))^|S| <= Z`. Hence, if
`2q <= rho a^2 Z` with `rho <= 1`, then `B_O <= N_perp Z rho^A`.

*Proof.* Use Lemma K2 with `w(sigma | state) = M_(|sigma|) a^((D + |sigma|)/2) Z^|sigma|`, where `D = |D_e|`. The
state sums are at most the expressions (J) (binomial coefficients as in T1). Along the encoder of S the product of
weights is `prod_e M_(|sigma_e|) a^(2|S|) Z^(|S| - 1)`, since `sum_e d_e = 4|S|` and `sum_e |sigma_e| = |S| - 1`. By
(P1) this is at least `u(S) (a^2 Z/t)^|S| / Z`. Then argue as in T1. QED

**The choice `a = 3/4`, `Z = 8/15` (PROVED by exact arithmetic).** Here `a Z = 2/5` and `a^2 Z = 3/10`:

    J1 = (1/pi)(8/3 + 512/1125 + 884736/159468750) < 3.1274/pi < 1,
    J2 = 3/4 + 6/25 + 8/1875 = 7457/7500,           J3 = (6/5 + 0.0342)/pi < 0.40,
    J4 = 9/16 + 27/900 < 0.60,   J5 = (3/10)/pi < 0.1,   J6 = 27/64.

For example `10 M_3 a^2 Z^3 = (16/(3 pi)) (32/375) = 512/(1125 pi)` and `6 M_2 a^2 Z^2 = (3/2)(9/16)(64/225) = 6/25`.
`J1 < 1` needs only `pi > 3.1274`. So T4 holds whenever `(20/3) q(beta) <= rho < 1`.

**The interval (PROVED).** At `beta = 7/30`: `sinh(7/30) <= (7/30)(5400/5351) = 1260/5351`, so `s <= 630/5351`;
with `u = 4 beta^2 = 49/225`, `c^8 <= 1 + u + u^2/(2(1 - u/3)) = 1 + 49/225 + 1620675/63382500 < 1.24335`. So
`q < 0.146386` and `(20/3) q < 0.9760`. Since q increases with beta, on the whole interval `0 < beta <= 7/30`,

    B_O <= (8/15) N_perp (0.9760)^A <= (32/15) a^2 (0.9760)^(a^2).                                       (T4)

Note `7/30 > 2/9`. (GUIDE: the bound `(20/3) q < 1` holds up to about `beta = 0.2375`; the best weights of this form
give rate `6.607 q`, up to about `0.2385`.)

**Consequences on `(0, 7/30]` (PROVED from T4, R2, R5).** With `tau_4 = log(1/0.9760) >= 0.024 > 1/42` and
`x e^(-tau x) <= 1/(e tau)`, `B_O < (32/15)(42/e) < 33`. By (F26),
`sum_(S in O) |D_m(S)| <= B_O e^(2 B_O) <= (32/15) e^66 a^2 (0.9760)^(a^2)`, uniformly in the box, crossed pair, twist
and coupling. Hence (J12), (E17) with `Q_F <= (32/15) e^(66 + 11 kappa_*^2) a^2 eta_*^(a/2)`
(using `-tau_4 a^2 + kappa_* a <= kappa_*^2/(4 tau_4) < 21 kappa_*^2/2 < 11 kappa_*^2`), RTAIL,
(RTAIL*) and (RTAIL-SOS), two-sided, on the whole interval `0 < beta <= 7/30`. This **extends the full-tail range
past the checked seed endpoint 2/9 of Theorem DOB**.

**Theorem T5 (unbranched odd surfaces, PROVED).** If `40 q/(3 pi) <= 1`,
`sum_(S in O_2) u(S) <= (3 pi/20) N_perp (40 q/(3 pi))^A`. Indeed (P1) gives `u(S) <= (2q)^|S| M_1^(|S| - 1)` for
degree-two surfaces, and Corollary C5 gives `sum_S 5^(1 - |S|) <= 1` per root, so the sum per root is at most
`(1/M_1)(10 M_1 q)^A/5`. At `beta = 3/10`: `s <= 0.15/(1 - 0.015) < 0.152285`, `c^8 <= e^(0.36) < 1.43364`, so
`q < 0.218321` and `40q/(3 pi) < 0.9267`. So `O_2` is area-small on `(0, 3/10]`. (GUIDE: up to about `0.314`.)

**Theorem T6 (per-link neighbourhood; PROVED; the main result of this note).** Keep the neighbourhood per link,
as in Lemma U (a), instead of `c^8` per plaquette. With `sh = sinh(beta)`, Lemma U (a) and Lemma P give
`u(S) <= sh^|S| prod_(e in E(S)) c^(6 - d_e) M_(|sigma_e|)` along the encoder of S. Let `a, V > 0` satisfy

    L1 = 5 c^4 M_1 a V + 10 c^2 M_3 a^2 V^3 + M_5 a^3 V^5 <= 1,   L2 = c^4 a + 6 c^2 M_2 a^2 V^2 + M_4 a^3 V^4 <= 1,
    L3 = 3 c^2 M_1 a^2 V + M_3 a^3 V^3 <= 1,                        L4 = c^2 a^2 + M_2 a^3 V^2 <= 1,
    L5 = M_1 a^3 V <= 1,                                            L6 = a^3 <= 1.                       (L)

Then `sum_(S ni p_0) u(S) (a^2 V/sh)^|S| <= V`, so `B_O <= N_perp V rho^A` whenever `sh/(a^2 V) <= rho <= 1`.

*Proof.* Use Lemma K2 with `w(sigma | state) = c^(6 - D - j) M_j a^((D + j)/2) V^j`, `j = |sigma|`, `D = |D_e|`. The
state sums are at most (L). Along the encoder of S the product is
`prod_e c^(6 - d_e) M_(|sigma_e|) a^(2|S|) V^(|S| - 1) >= u(S) (a^2 V/sh)^|S| / V`. QED

Every term of (L) increases with beta, so (L) at one coupling gives (L) below it; the rate `sh/(a^2 V)` increases
too.

**The choice `a = 7/10`, `V = 51/100` at `beta = 6/25` (PROVED by hand).** Bounds: `sh <= (6/25)(625/619) = 150/619
< 0.2423264`; `c^2 <= e^(beta^2)`, `c^4 <= e^(2 beta^2)` (from `log cosh t <= t^2/2`), and the series bound give
`c^2 < 1.059292`, `c^4 < 1.122101`; `pi > 3.14159` gives `M_1 < 0.424414`, `M_3 < 0.169766`, `M_5 < 0.097010`.
With `aV = 0.357`, `a^2 = 0.49`, `a^3 = 0.343`, `V^2 = 0.2601`, `V^3 = 0.132651`, `V^4 < 0.067653`, `V^5 < 0.034503`:

    L1 < 0.85009 + 0.11689 + 0.00115 < 0.9682,     L2 < 0.785471 + 0.202510 + 0.002901 < 0.9909,
    L3 < 0.33705 + 0.00773 < 0.345,                L4 < 0.519054 + 0.022305 < 0.542,
    L5 < 0.0743,                                    L6 = 0.343.

For instance the middle term of L2 is `6 c^2 (1/4)(0.49)(0.2601) < 6 * 1.059292 * 0.25 * 0.49 * 0.2601 < 0.202510`.
The rate is `sh/(a^2 V) < 0.2423264/0.2499 < 0.9697`. Hence, on the whole interval `0 < beta <= 6/25`,

    B_O <= (51/100) N_perp (0.9697)^A <= (51/25) a^2 (0.9697)^(a^2).                                    (T6)

**Consequences on `(0, 6/25]` (PROVED from T6, R2, R5).** `tau_6 = log(1/0.9697) >= 0.0303 > 1/34`, so
`B_O < (51/25)(34/e) < 26` and `sum_(S in O) |D_m(S)| <= B_O e^(2 B_O) <= (51/25) e^52 a^2 (0.9697)^(a^2)`. Hence
(J12); (E17) with `Q_F <= (51/25) e^(52 + 9 kappa_*^2) a^2 eta_*^(a/2)` (since `kappa_*^2/(4 tau_6) < 34 kappa_*^2/4
< 9 kappa_*^2`); RTAIL, (RTAIL*) and (RTAIL-SOS), two-sided, on the whole interval `0 < beta <= 6/25`, with every
decoration and the original `Z_m`. Note `6/25 > 7/30 > 2/9`. (GUIDE: with coupling-dependent `(a, V)` this scheme
keeps the rate below one up to about `beta = 0.2497`; at `1/4` the best rate found is 1.0018.)

**What T4 and T6 supersede.** T6 contains T4 (`7/30 < 6/25`), T1 (`1/6 < 6/25`) and T3 (`O_iso ⊂ O`, `2/9 < 6/25`);
T5 contains T2 (`7/25 < 3/10`). Lemma B and Proposition L stay correct as statements about the Finner route. The "missing lemma"
(BR-SEQ) of section 7 is no longer needed below `6/25`: peeling removes the branching penalty without it.

## 10. Updated consequences, the reach of the method, and what is open

This section replaces the conclusions of sections 7 and 8 wherever they differ; those sections remain as the record
of the Finner route.

**(RTAIL-SOS) on `(0, 6/25]` (PROVED).** Theorem T6 bounds the majorants of **all** odd surfaces, so it proves
(RTAIL-SOS), (RTAIL*), RTAIL, (J12) and (E17) on the whole interval `0 < beta <= 6/25`, two-sided, with every
decoration and the original `Z_m`. Explicitly, `|R_m^**| <= |p_m(v)| + |T_m(G_**)| <= 2 B_O e^(2 B_O)` with (T6).
The "stronger target" `B_out` of gap-rtail-astra.md:704-713 is proved on the same interval.

**Relation to the seed (READ, not re-checked).** (E17) is the input of the consumer: with the witness
`S_ev >= eta(beta)^a`, valid at every `beta > 0` (gap-fusion-astra.md:95-133), (E17) gives (FQ) with `K(a) = 8 C a^2`
(gap-expose-astra.md:586-598; gap-ext-astra.md:115-127). gap-rtail-astra.md:752-762 records that (FQ) on an interval
is "the precise input that could be combined with the checked seed and the lane's continuation argument". On
`(0, 2/9)` the checked seed already exists (Theorem DOB, gap-vmf-lip.md:438-466). T6 supplies (E17) on
`[2/9, 6/25]` as well. **If** the recorded continuation from (FQ) to a full seed holds as stated, the seed and the
lattice gap extend to `beta <= 6/25`. I have not checked that continuation. On `(0, 2/9)` T6 is a second derivation
of the consumer input, by a different method (surface expansion, peeling and counting, against Dobrushin
contraction). It does not reach the unrefereed claims `1/3` (forest gauge) and `0.348` (plaquette blocks) recorded in
gap-novelty-opus.md:15-33.

**The remaining tail, exactly (PROVED reductions; OPEN estimates).**
- On `(6/25, 3/10]`: order `G_** ∪ O_2` first. By (S23) and (T5) this class is area-small, and, as in (S25),
  (RTAIL-SOS) is equivalent there, up to constants and powers, to **(RTAIL-BR)**: the signed remainder of the marked
  families containing an odd surface that has a link of degree four or six and lies outside `G_**`.
- On `(3/10, 5/11]`: only `G_**` is controlled; the unbranched surfaces outside `G_**` are open as well
  (T5 reaches about `0.314` with sharper arithmetic, not more).

**The reach of the method (PROVED where stated).**
- *Degree-two surfaces.* By Corollary C5 and (P1), the certified rate is `10 M_1 q = 40q/(3 pi) = 4.244 q`. As in
  Proposition L, no Kraft certificate with weights depending only on `(|D_e|, |sigma_e|)` does better against the
  majorant (P1): it cannot prove `N_2(n) < 5^(n-1)`. So this route stops at `q = 3 pi/40`, about `beta = 0.314`
  (GUIDE).
- *All surfaces.* With (P1) the binding Kraft constraints are J1 and J2. J2 contains the branching option at a
  closing link: six ways to add two plaquettes, weight `6 M_2 a^2 Z^2`. It forces `a < 1` and costs the factor
  `6.607/4.244 = 1.56` in the rate (GUIDE optimum, neighbourhood `c^8` per plaquette). The full tail stops near
  `beta = 0.2385` with that accounting, and near `0.2497` with the per-link accounting of T6 (GUIDE).
- *At `beta = 1/3`.* `q(1/3) > 0.2614`, so even the degree-two rate exceeds `1.10`. Reaching `1/3` would need
  both (a) a degree-two discovery entropy below `5 * (3 pi/40)/q(1/3) < 4.51` instead of 5, and (b) branching options
  at closing links costing far less than the 56 percent they cost here. These are limits of the encoding, not lower
  bounds on surface numbers or on Wilson weights.

**Concrete next steps (ARGUED, ranked by what they move).**
1. Branching at closings (lever (b)). Charging the neighbourhood per link (T6) already saves `c^6` per branching
   link and moves the endpoint from about 0.2385 to about 0.2497 (GUIDE). Larger gains need a code in which branching
   at a closing link is far rarer (a potential on pending links, or a separate flag paid by the smaller weight of the
   new sheets).
2. Discovery entropy (lever (a)). Exclude candidates having a processed link (Lemma K1 (ii)) through a vertex-state
   potential; at bends, count the doubly counted outside plaquettes of Lemma U (a). Both are local and hand-checkable.
3. Sharper one-link constants: `N_1 = E|sinh(beta x)|` is about 1 percent below `sinh(beta) M_1` at `beta = 1/3`.
These are refinements of one encoding. Other routes are not excluded by anything here.

## 11. Group dependence (PROVED / READ)

The code (sections 2, 9) uses no group. Lemma U and (F8) use the central sign, Haar invariance, zero mean and
`|x| <= 1` (gap-flat-check-opus.md section 7). Lemma P uses only that `<U, W>` has the law of x for every unit W
(Haar invariance) and the absolute moments `M_1, ..., M_6`. Lemma B uses the Haar moment tensors of U of degrees
two, four and six.

*Binary icosahedral group 2I.* Its Haar tensors agree with those of SU(2) through degree eleven (READ:
gap-flat-astra.md:571-579, crediting Lemma 2, (G12)-(G13), of gap-tree-astra.md:288-346; moments re-derived in
gap-flat-check-opus.md section 7 and gap-rtail-check-opus.md section 6). So Lemma U, Lemma B and the even moments in
(J) transfer unchanged. The odd absolute moments are not polynomial and differ. From the class values
(x = ±1 once each, 0 thirty times, ±1/2 twenty times each, ±(1+√5)/4 and ±(1−√5)/4 twelve times each), by hand:
`M_1(2I) = (22 + 24 * sqrt(5)/2)/120 < 0.4070 < M_1`, and `M_3(2I) = (7 + 24 (|c_+|^3 + |c_-|^3))/120 < 0.1702`,
where `|c_+|^3 + |c_-|^3 = sqrt(5)/4` since `|c_+| + |c_-| = sqrt(5)/2` and `|c_+||c_-| = 1/4`.
`M_5(2I) = (3.25 + 3.75 sqrt(5))/120 < 0.0970` likewise. With these values `J1(2I) < 0.97`, `J3(2I) < 0.38`,
`J5(2I) < 0.1`, and, at `beta = 6/25`, `L1(2I) < 0.934`, `L3(2I) < 0.331`, `L5(2I) < 0.072`. So T4, T5 and T6
hold for 2I on the same intervals. The result is group-blind between SU(2) and 2I, as expected for a strong-coupling-type
bound.

*U(1).* `x = cos(theta)` has `M_1 = 2/pi`, `M_2 = 1/2`: the constants change and the intervals shrink. No U(1)
conclusion is drawn.

*Weak coupling.* `q >= sinh(beta)/2 > 1` for `beta >= 2`, so these estimates say nothing at weak coupling, for any
of the groups.

## 12. Verification boundary and source record

- **What was done by hand.** Every PROVED statement above is my hand argument: Lemmas K1, K2, U, B, P; Corollaries
  C5, B1, P1; Theorems T1-T6; Proposition L; all interval endpoints, with every fraction displayed. The rational
  comparisons are written so that a reader can redo them; the largest is the check of K1 and K2 for T3.
- **What the GUIDE runs did.** They located optimal weight parameters (`P^2 y`, `a^2 Z`), the coupling at which each
  certified rate reaches one (0.1725, 0.185, 0.227, 0.235, 0.2375, 0.2385, 0.2497, 0.2855, 0.314), and simple
  fractions; they also evaluated `q` at sample couplings. No conclusion rests on them. Scripts: `kraft1.py` to
  `kraft6.py`, `peel1.py` to `peel3.py`, `ratsearch.py`, `ratsearch2.py` in the `guide/` directory named in the header.
- **A Monte Carlo sanity check of Lemma P (GUIDE, `peelmc.py`, 4 x 10^5 Haar samples).** For the boundary of a unit
  cube, `E prod |x_p| = 0.00582 +- 0.00002`, below the Lemma P bound `M_2 M_1^4 = 0.00811` and Finner's `2^(-6)`.
  For two cube boundaries glued along one link (one degree-four link, 12 plaquettes),
  `E prod |x_p| = 3.41e-5 +- 0.04e-5`, below every Lemma P bound for that surface (at least `M_2 M_1^10 = 4.74e-5`)
  and far below Finner's `4.9e-4`. This tests the lemma; it proves nothing.
- **What was not checked.** The consumer chain from (E17) through (FQ) to a full seed past 2/9 is READ and not
  re-checked. The inputs (F8)-(F11), (F26), (S23), (S25) are READ with their Claude Opus 5.5 checks (all HOLD).
  This note has had no independent check; the self-read below is not one.
- **Self-read.** I re-derived the parity and discovery bookkeeping of Lemma K1, the identification of the
  plaquettes integrated at each step of Lemma P, the moment tensors and the 15 pairings of Lemma B, and each exact
  fraction. Points a checker should test first: the identification `k_i = |sigma_(e_i)|` in Lemma P (including the
  root), the use of Lemma K2 over all surfaces while (P1) is applied surface by surface, and the 2I odd moments.
- **Files.** Only this output file was written. No repository file, registry, queue, audit or public post was
  touched. No download was made.

RESULT: PROVED BY HAND, NOT INDEPENDENTLY CHECKED — a Kraft-weighted exploration code in which closing links are free, and peeling in the code's own order (each plaquette integrated at its discovery link, with no branching penalty), bound the (F8) majorants of all odd surfaces by (51/100) N_perp (0.9697)^A on 0 < beta <= 6/25, so (RTAIL-SOS), RTAIL, (RTAIL*), (J12) and (E17) hold on (0, 6/25], past the 2/9 seed endpoint, with all decorations and the original Z_m, group-blind between SU(2) and the binary icosahedral group; unbranched odd surfaces (overhangs, handles, two transverse directions, any excess) are area-small on (0, 3/10]; OPEN: (RTAIL-BR) on (6/25, 3/10] and all surfaces outside G_** above 3/10; this encoding stops near beta = 0.2497 (0.314 unbranched) and 1/3 needs a smaller surface entropy; a seed past 2/9 follows only through the READ, unchecked continuation.
