# checks/bb11_criteria.md — pre-registered criteria for check bb11 (BFT_B session 11)

Written **after** BFT_B.md §38 (the session-11 PRE-STATED section, stat 13:58:33 UTC) and **before** any bb11 script
exists. **No constant derived in session 11 appears below.** The only numerical constants used are:

- `2`, as the elementary bound `||Ad_g - 1||_op <= ||Ad_g||_op + ||1||_op = 2` for `Ad_g` orthogonal (elementary, not
  derived here);
- `L = 3`, `d = 2`, `k = 2`, the lattice parameters of the model, chosen to match `checks/bb9b_rtcc.py` and
  `checks/bb10_cof.py` so that the only change is the gauge group;
- the rational rotation entries `3/5, 4/5` (a 3-4-5 Pythagorean triple), chosen so that every adjoint matrix is exactly
  representable in `Fraction`.

No criterion below quotes a bound proven in session 11. Every test is either an **exact identity** (PASS iff the computed
object is exactly zero / exactly equal), an **exact non-vacuity** statement (PASS iff a named object is exactly nonzero,
so that the identity it accompanies is not vacuous), or an inequality against a quantity **computed from the background in
the same run** (never against a session-11 constant).

## Environment (binding)

Exact rational arithmetic in plain python: `fractions.Fraction` and Python `int` only. **No numpy, no BLAS, no scipy.**
`python3 -I`, `PYTHONDONTWRITEBYTECODE=1`, `nice -n 10`, `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=
VECLIB_MAXIMUM_THREADS=1`. DRIVE_BRIEF rule 6 exempts exact rational/symbolic arithmetic in plain python from the numeric
lock, so **no numeric lock is taken**. Target: under 2 minutes, under 200 MB.

## Model (fixed here, before the script)

- `d = 2`, `L = 3`, `k = 2`, coarse top side `T` as stated per part; level sides `T*L^k, T*L^{k-1}, ..., T`.
- Roots: block centres, as in `checks/bb9b_rtcc.py` (§15.0's convention).
- Gauge group **SU(2)**, represented **in the adjoint**: a group element acts on `su(2) ≅ Q^3` by a 3x3 rational
  orthogonal matrix. The generators used are `Rz(c,s)` and `Rx(c,s)` with `(c,s) = (3/5, 4/5)` and their transposes and
  powers; all entries stay in `Q`.
- A **background chain** is an assignment of such a matrix `A(b) := Ad_{Z_j(b)}` to every level-`j` link `b`, `0 <= j < k`,
  together with the level-`k` links.
- Three background families, all built before any test is run:
  - **FLAT-NA**: `A(b) := G(y) G(y')^{-1}` for a link `b = (y, y')`, with `G` a site-wise assignment of rational rotations
    (a pure gauge; every plaquette holonomy is exactly the identity).
  - **CURVED-NA**: a background whose level-0 plaquette holonomies are **not** all the identity (at least one plaquette
    holonomy differs from `1`), with the level-`(j+1)` links defined as the straight row products of the level-`j` links
    (the "straight-row tower" property of §38.1).
  - **CURVED-NA-OFF**: CURVED-NA with the level-1 links perturbed by one extra rational rotation on one link, so that the
    straight-row tower property fails on exactly that link.
  - **ABELIAN**: every `A(b) = 1` (the identity matrix). This is the control family: for it `Ad ≡ 1`, so it is the
    abelian/trivial-background case.
- `log` of a rational rotation is **not** computed; wherever §38 writes `|log W_p|`, the script uses the exactly
  computable surrogate `defect(W) := ||W - 1||_op` (the operator norm of the matrix difference, evaluated as the maximum
  absolute row sum, which is exact in `Q`), and every criterion below is written in terms of `defect`. (This is a choice
  of surrogate made in the criteria, not a result: `defect(W) = 0` iff `W = 1` iff `log W = 0`, which is all the
  exactness tests need, and the size test A3 is written as a ratio against `defect`.)

## Part A — no solve, background family as named, `T = 2`

| id | statement tested | PASS iff | FAIL iff |
|---|---|---|---|
| **A1** | §38.3 Theorem BGD (a) identity: `(d_Z d_Z lam)(p) = (Ad_{W_p} - 1) lam(z_p)` for every plaquette `p`, every level `j < k`, on 8 pseudo-random `su(2)`-valued level-`j` functions `lam` with rational entries | the two sides agree **exactly** (difference identically `0` in `Q`) on every `(p, j, lam)`, for **both** CURVED-NA and FLAT-NA | any entry differs |
| **A1n** | A1 non-vacuity | on CURVED-NA there is at least one `(p, j, lam)` with `(d_Z d_Z lam)(p)` **exactly nonzero** | `d_Z d_Z lam ≡ 0` for every tested `(p, j, lam)` on CURVED-NA |
| **A2** | Tier-A adjointness: `<j, d_Z lam> = <d_Z^* j, lam>` in the `Ad`-invariant (Euclidean on `Q^3`) pairing, for 8 pseudo-random level-`j` 1-forms `j` and functions `lam`, every `j < k`, on CURVED-NA | exact equality in `Q` on every instance | any instance differs |
| **A3** | §38.3 Theorem BGD (a) size: for every level-`j` 2-form `G` tested (8 pseudo-random), `max_z |(d_Z^* d_Z^* G)(z)|_inf <= 2 * max_p defect(W_p) * max_q |G(q)|_inf` on CURVED-NA | the inequality holds on every instance | any instance violates it |
| **A3n** | A3 non-vacuity | `d_Z^* d_Z^* G` is **exactly nonzero** for at least one tested `G` on CURVED-NA | it is zero on every tested `G` |
| **A4a** | §38.3 Theorem BGD (b), tower case: `Q_str^Z d_Z ev^{(l)} lam = d_Z ev^{(l+1)} lam` for `l = 0, 1` on **CURVED-NA** (a straight-row tower), 8 pseudo-random level-0 functions `lam` | exact equality in `Q` on every instance | any instance differs |
| **A4b** | §38.3 Theorem BGD (b), defect case: on **CURVED-NA-OFF** the same difference equals the stated `E_l lam = (Ad_{Z_{l+1}(Y,mu)} - Ad_{Z_l(row)}) lam(c_{Y+e_mu})` **exactly**, and is **nonzero** on at least one `(Y, mu, lam)` | both the exact identity and the non-vacuity hold | either fails |
| **A5** | §38.2 Theorem N1-alg, gauge-shift clause (the covariant form of §16.1 (a)): the covariant box-Coulomb minimiser obeys `lam_X^{E,Z}(x + d_Z mu) = lam_X^{E,Z}(x) - mu + mu(c_X)` exactly, for 4 pseudo-random `x` and 4 pseudo-random `mu`, on CURVED-NA | exact equality in `Q` on every instance | any instance differs |
| **A6** | §38.2 Theorem N1-alg, uniqueness clause (the linearised Lemma CL-uniq): the `Q`-linear system `d_Z lam = 0`, `lam(c_X) = 0` on the box `Ñ_X` has **only** the zero solution on CURVED-NA; and on ABELIAN the same system has solution space of dimension exactly `3` before the pin and `0` after it (so the pin, not the curvature, is what kills the constants there) | the CURVED-NA nullity after the pin is exactly `0` **and** the ABELIAN nullity before the pin is exactly `3` | either number differs |

## Part B — exact solve, `T = 1` for the solve, `T = 2` where Part A's boxes are needed

| id | statement tested | PASS iff | FAIL iff |
|---|---|---|---|
| **B1** | §38.2 (N1-a) idempotence at a curved background: the covariant box-Coulomb problems on all boxes have unique solutions with the pin, `Lambda_Z(Pi_E^Z x) = 0`, and `Pi_E^Z (Pi_E^Z x) = Pi_E^Z x` exactly, for 4 pseudo-random `x` on CURVED-NA | all three hold exactly in `Q` | any fails |
| **B2** | §38.3 Lemma CONJ at a **flat** nonabelian background: with `G` the gauge of FLAT-NA, `Ad_G^{-1} d_Z Ad_G = d`, `Ad_G^{-1} Q_str^Z Ad_G = Q_str`, and `lam_X^{E,Z}(Ad_G x) = Ad_{G(c_X)} lam_X^E(x)` — all exactly, on 4 pseudo-random `x` | all three hold exactly in `Q` | any fails |

## Controls

| id | statement tested | PASS iff |
|---|---|---|
| **C1** | the nonabelian model is load-bearing: on **ABELIAN**, `d_Z d_Z = 0`, `d_Z^* d_Z^* = 0` and A4b's defect `E_l = 0`, all exactly | all exactly zero |
| **C2** | Lemma CONJ's hypothesis is load-bearing: on **CURVED-NA** the intertwining of B2 **fails** for at least one instance, and the failure of `Ad_G^{-1} d_Z Ad_G - d` is nonzero | the failure is exactly nonzero |

## Verdict rule (pre-registered)

- **ALL PASS** iff every one of A1, A1n, A2, A3, A3n, A4a, A4b, A5, A6, B1, B2, C1, C2 passes.
- Any failure is reported as a **FAIL**, the output and the script are kept unaltered, and any rerun is made under a new
  id with this criteria file untouched. Any probe designed after seeing an outcome is labelled **post-hoc** and carries no
  pre-registration weight.
- **Expected vacuity, pre-registered:** at `k = 2` and `T = 1` the level-2 lattice has a single site, so, exactly as in
  bb9b's B4 and bb10's limitation 4, any test that needs two distinct level-2 roots is run at `T = 2` instead; A4a/A4b are
  therefore run at `T = 2` (Part A), not inside the Part-B solve.
- **Pre-registered scope limitation, to be reported whatever the outcome:** `d = 2`, `k = 2`, SU(2) in the adjoint, and a
  thin family of rational-rotation backgrounds. The check tests the **algebra and the exactness defects** of §38.2-§38.3.
  It tests **nothing** in Tier C (no `M`, no `M_f`, no `C_alpha`, no `C_K`, no `Lemma LE`), **nothing** in §38.4 (no
  `(C_g-theta)`, no `(N2-lip)`, no weight), and no `d = 4` arithmetic and no `k`-uniformity.

---

## AMENDMENT (appended 2026-10-28 14:02:18 UTC, before any bb11 script existed; disclosed in full)

Five changes. Each is a correction of *this criteria file*, made before the script was written, so that no test would fail
for an error in the criteria rather than for a fact about the statement. Nothing below is retuned after an outcome: no
bb11 script existed when this amendment was appended. **The original text above stands as the record.**

1. **A1's exact form (a convention error in this file).** Computing `d_Z d_Z` from §38.1's conventions gives, for a
   plaquette `p` based at `z` with directions `mu < nu` and far corner `c := z + e_mu + e_nu`,
   `(d_Z d_Z lam)(p) = (U1 - U2) lam(c)`, with `U1 := A(z,mu) A(z+e_mu,nu)` and `U2 := A(z,nu) A(z+e_nu,mu)` the two
   corner transports from `z` to `c`. The holonomy form of §38.2 is recovered as `U1 - U2 = U1 (1 - U1^T U2)` with
   `Ad_{W_p} := U1^T U2`. **A1 therefore tests `(d_Z d_Z lam)(p) = (U1 - U2) lam(c)` exactly**, and separately the
   identity `||U1 - U2||_F = ||Ad_{W_p} - 1||_F` (both exactly, as squares in `Q`). §38.2's display, which put the
   argument at `z_p` and omitted the transport prefactor, is corrected in the session's proof section.
2. **A3's norm and constant.** `||M v||_2 <= ||M||_F ||v||_2` and `||U1 - U2||_F^2 = 6 - 2 tr(U1^T U2) =
   ||Ad_{W_p} - 1||_F^2` are both exact in `Q`, whereas an `l^inf` operator norm of a rational rotation is not comparable
   to `2`. **A3 therefore tests, as squares in `Q`:**
   `max_z |(d_Z^* d_Z^* G)(z)|_2^2 <= (max_p ||Ad_{W_p} - 1||_F^2) * (max_q |G(q)|_2^2)`,
   with constant `1` (Frobenius dominates the operator norm — elementary, not derived here), which is **stronger** than
   the `2` of the original A3.
3. **A4b's sign.** The computed defect is `(Q_str^Z d_Z ev^{(l)} - d_Z ev^{(l+1)}) lam = (Row_l(Y,mu) - A_{l+1}(Y,mu))
   lam_{l+1}(Y + e_mu)`, with `Row_l(Y,mu)` the straight level-`l` row product from `c_Y` to `c_{Y+e_mu}`. §38.2's display
   had the two terms in the other order and did not name the argument. **A4b tests this identity exactly**, together with
   non-vacuity.
4. **The box size for A5, A6, B1, B2.** `Ñ_X` has coarse half-width 2, i.e. own side `4n + 1 = 37` in this model
   (`n = L^k = 9`), so an exact rational solve on it is `3 * 37^2 = 4107` unknowns and is not affordable. The clauses
   tested — the gauge shift, the uniqueness/nullity, idempotence and the flat-background intertwining — use **only** that
   the box is connected, that the problem is linear, and that `lam(c_X) = 0`; none uses the box size. **A5, A6, B1 and B2
   are therefore run on a connected box of own half-width 2 (a `5 x 5` box, 25 sites, 75 unknowns) on a side-6 level-0
   torus**, and that substitution is reported as a scope limitation whatever the outcome.
5. **B1's partition of unity, and B2's intertwining form.** (i) §16.1 (d)'s idempotence proof uses exactly two properties
   of the tents, `Sum_X chi_X = 1` and `chi_X(c_Y) = delta_{XY}`; **B1 is run with the quintic tents of §15.0 restricted to
   this model** (roots on a spacing-3 sublattice of the side-6 torus, `chi_X(z) = prod_nu sigma_5(|z_nu - c_{X,nu}|/3)`,
   exactly rational), and the two properties are themselves tested as **B1a**. (ii) The intertwining of a gauge is
   **pointwise**, not by the root value: for `x(b) = G(base b) xt(b)` the minimiser is `lam_X^{E,Z}(M_G xt) = M_G
   lam_X^E(xt)` (`G` applied at each site), and likewise `Q_str^Z M_G = M_G^{root} Q_str` and `d_Z M_G = M_G^{base} d`.
   **B2 tests those three pointwise forms exactly.** §38.3's display `lam^{E,Z}(Ad_G x) = Ad_{G(c_X)} lam^E(x)` is wrong
   as written (it holds pointwise, not with the constant `G(c_X)`) and is corrected in the session's proof section.
6. **C2's construction.** CURVED-NA carries no gauge `G`, so the original C2 is not well posed. **C2 is run as:** let
   `A' := A_flat` except on one link `b_0`, where `A'(b_0) := A_flat(b_0) P` with `P` a rational rotation `!= 1` (so some
   plaquette holonomies of `A'` differ from `1`). Then the intertwining defect `d_{Z'}(M_G lamt) - M_G^{base}(d lamt)` is
   **exactly nonzero** and **supported exactly on `b_0`**. PASS iff both hold.
