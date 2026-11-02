lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T21:54Z

# rel-phi-c: deciding (REL-Phi) of `library/seam-nonlinear-c.md` Section 4

Queue row 63, mapped side. Statement pinned at commit `bef9ac33c`. Author:
Anthropic claude-opus-5-5, effort max, Mac mini worker, 2026-11-02.
Same-model work: not independent in model, not a gate, not an audit, no
status.

Status: in progress (sections are added as they are written; the verdict
line below is final only when Section 7 exists).

**Firewall.** Mapped side. Read only FINISH.md, GOAL.md, mapped-side
`library/` notes, `parts/hard-core--mapped.md` and `parts/hard-core--excess.md`
excerpts, and mapped-side check code, as listed in Section 8. No file
excluded for the mapped side, no gate file, no Sussman-Alpoge text, no
literature, no file of the independent side's library.

## 1. The statement tested, units, and criteria fixed before any run

**Setting** (as in `seam-quadratic-c` 2 and `seam-nonlinear-c` 1, 4). Fine
lattice Z^4 (or a torus), unit spacing; L odd, L >= 3, m := (L - 1)/2; depth
n; B := L^n. Level-j sites are L^j Z^4; they nest because L is odd, so a top
centre (level n) is a level-j site for every j. B_s(x) := x + {-(s-1)/2, ...,
(s-1)/2}^4. For a fine 1-form theta (link logarithms; su(2)-valued, |.| the
norm |Z|_F) its top normalization is H := B theta. For a set S of fine bonds,

    ||H||_(L^p(S)) := (B^-4 sum_(b in S) |H_b|^p)^(1/p),   so   ||H||_(L^4(S)) = (sum_(b in S) |theta_b|^4)^(1/4).

Level-j path average of a fine 1-form, for a level-j bond c = [x, x + s e_mu],
s = L^j: Q_path^(s) theta(c) := s^-4 sum_(z in B_s(x)) theta([z, z + s e_mu]),
with Q_path^(1) = identity. One-step contour average at level k (1 <= k <= n),
on level-(k-1) 1-forms A, at a level-k site y:

    Phi^(k) A(y) := L^-4 sum_(x in B^(k)(y)) A(Gamma^(k)_(y,x)),   B^(k)(y) := y + L^(k-1) {-m, ..., m}^4,

Gamma^(k)_(y,x) the axial staircase from y to x in the level-(k-1) lattice
(axes in the fixed order 1, 2, 3, 4, as in `checks/seamqc/seamqc.py`), A(Gamma)
the oriented sum over its bonds. One step is Q^(k) = Q_path^(k) - d' Phi^(k)
(mapped Lemma 3.1); the composite is Q_n = Q^(n) ... Q^(1) = Q_path^(B) - d' Phi_n
with Phi_1 = Phi^(1), Phi_(k+1) = Av^(k+1) Phi_k + Phi^(k+1) Q_k
(`seam-quadratic-c` Lemma 2.2(d)). At the background T, Phi_n^(T) is the same
expression with the transports of T (Section 2.4).

**The statement** (`seam-nonlinear-c` 4.1). (REL) asks for a fine gauge g with
g = 1 at every top centre and H with U^g_b = exp(H_b/B) T_b, and

    (REL-2)   ||H||_(L^2(Q)) <= C_2 (K_delta * E)(Q)^(1/2),   C_2, delta absolute,
    (REL-4)   ||H||_(L^4(Q)) <= C_4(L) (K_delta * E)(Q)^(1/2),
    (REL-Phi) |Phi_n^(T) H(y)| <= C_Phi(L) (K_delta * E)(Q_y)^(1/2)  at every top centre y,
    (REL-E)   E(Q) <= C_E f^2,

uniformly in depth and volume. Write Psi := Phi_n^(T) H.

**What "decide" has to mean.** (REL) is existential in the gauge. Under a fine
gauge change e^lambda with lambda = 0 at every top centre ("admissible"), Psi
moves by Av_B lambda (Lemma 2 below). So a field H whose Psi grows with depth
refutes (REL-Phi) only if no admissible gauge with the other clauses has
bounded Psi; and a proof must exhibit or construct the gauge. Both readings
are tested below.

**Registered criteria for the runs (written before any run).** A run can
refute a hand identity or show a constant growing; it cannot prove a bound.
1. Identities (Lemmas 1 to 3 below) on the actual nested map of
   `seamqc.py` (`balaban_Q`, axial staircases), d = 4, L = 3, n = 2, random
   fields on the torus of side 18: the formula of Lemma 1 against the
   recursion of `seam-quadratic-c` 2.2(d) and against Q_2 = Q_path^(9) - d' Phi_2;
   the gauge law; constants. PASS if every relative error is below 1e-10. A
   value above 1e-8 means a hand step is wrong and stops the item there.
2. The kernel w_n of Phi_n at one top centre, built from Lemma 1, for
   (L, n) = (3, 1), (3, 2), (3, 3), (5, 1), (5, 2): record N_tot := the
   l^(4/3) norm of w_n over all fine bonds (the exact L^4 to angle constant)
   and N_ann := max over the annuli A_j of Section 3 of the l^(4/3) norm of w_n
   on A_j. Lemma A (hand) predicts N_ann <= C_A(L) = 3.4 L + 1 for every n, and
   Example E (hand) predicts N_tot growing at least like n^(3/4). REFUTES
   Lemma A if some N_ann exceeds C_A(L). Also check sum over direction-mu
   bonds of w_n = 0 (Lemma 3) to 1e-12.
3. Example E: its two exact sums (Section 3.3) for L = 3, n = 1 to 12, to
   display the growth of Psi / ||dlambda||_(L^4) against (log B)^(3/4).
   Illustration only; the bound is proved by hand.

## 2. The composite contour average at a top centre (discharged, hand proofs)

**Lemma 1 (contours from the top centre at every level).** For every fine
1-form theta and every top centre y,

    Phi_n theta(y) = sum_(k=1)^n ( Phi^(k) Q_path^(L^(k-1)) theta )(y).

*Proof.* Two facts. (a) For a level-k 0-form mu, the oriented sum of d mu over
a path from y to x is mu(x) - mu(y), so Phi^(k+1)(d mu)(y) = (Av^(k+1) mu -
r^(k+1) mu)(y), where Av^(k+1) averages over the L^4 level-k sites of the block
B^(k+1)(y) and r^(k+1) restricts to level-(k+1) sites. (b) Q_k = Q_path^(L^k)
- d Phi_k, d the level-k gradient (`seam-quadratic-c` 2.2(d)). Hence
Phi^(k+1) Q_k = Phi^(k+1) Q_path^(L^k) - Av^(k+1) Phi_k + r^(k+1) Phi_k, and the
recursion Phi_(k+1) = Av^(k+1) Phi_k + Phi^(k+1) Q_k becomes
Phi_(k+1) = r^(k+1) Phi_k + Phi^(k+1) Q_path^(L^k). Start from
Phi_1 = Phi^(1) = Phi^(1) Q_path^(1) and iterate; a top centre is a level-k site
for every k, so the restrictions are evaluations at y. QED

*Reading.* At every level the staircases start at the top centre y itself,
and what they integrate is the path average one level below, which averages
over transverse boxes of side L^(k-1). The contour parts of the intermediate
maps have dropped out exactly. This is the open-path cancellation of
`lc-u` 5 ("all inserted interior contours cancel") at the linear level.

**Lemma 2 (gauge law).** For every fine 0-form lambda and top centre y,
Phi_n(d lambda)(y) = Av_B lambda(y) - lambda(y). So an admissible gauge change
(lambda = 0 at every top centre) moves Psi(y) by exactly Av_B lambda(y).

*Proof.* Q_path^(s) d = d Av_s at level j, s = L^j (`seam-quadratic-c` 2.2(c)).
So the k-th term of Lemma 1 is Phi^(k) d (Av_(L^(k-1)) lambda)(y) =
Av^(k) Av_(L^(k-1)) lambda(y) - Av_(L^(k-1)) lambda(y) by (a), and
Av^(k) Av_(L^(k-1)) = Av_(L^k) at a level-k site, since the blocks
B_(L^(k-1))(x), x in B^(k)(y), tile B_(L^k)(y) (`seam-quadratic-c` Lemma 2.1).
The sum over k telescopes to Av_B lambda(y) - lambda(y). QED

**Lemma 3 (affine gauges, constant fields).** If lambda is affine, then
Av_B lambda(y) = lambda(y), since the block is symmetric about y. Hence a
field equal to a constant a_mu on every direction-mu bond of the read set
R_n(y) below has Phi_n theta(y) = 0 (it agrees there with d of an affine
function, and Phi_n(y) reads only R_n(y)). Equivalently, the kernel w_n of
theta -> Phi_n theta(y) has zero sum over the positively oriented
direction-mu bonds, for each mu.

**2.3 Read sets, weights, path averages (discharged).**
- *Read set.* The level-(k-1) bonds of the staircases from y have endpoints in
  y + L^(k-1)[-m, m]^4. For a level-(k-1) bond c = [x, x + s e_mu], s = L^(k-1),
  the path average reads the fine bonds S(c) := {[w, w + e_mu] : w in B_s(x) +
  {0, ..., s-1} e_mu}, whose sites lie within sup-distance (s - 1)/2 + s of x.
  So the k-th term reads only bonds with both endpoints within sup-distance
  rho_k := (L^k + 2 L^(k-1))/2 of y; call this set R_k(y). rho_n <= 5B/6, so
  Phi_n(y) reads inside Q_y^(+1), the 3^4 top cubes around Q_y.
- *Weights.* w^(k)(c) := L^-4 #{x : Gamma^(k)_(y,x) traverses c} lies in
  [0, m/L]. Staircases are monotone in each axis, so each traverses a bond at
  most once and never returns to y; hence sum_c w^(k)(c) = L^-4 sum_x
  |x - y|_1 / L^(k-1) = 4m(m + 1)/L < L, and the bonds at y carry total
  weight 1 - L^-4 < 1.
- **Lemma 4 (path averages).** |S(c)| = s^3 (2s - 1) <= 2 s^4, each fine bond
  of S(c) lies in at most s of the segments [z, z + s e_mu], z in B_s(x), so

      |Q_path^(s) theta(c)| <= s^-3 sum_(b in S(c)) |theta_b| <= 2^(3/4) ||theta||_(l^4(S(c))),

  and at s = B, |Q_path^(B) theta(c)| <= 2^(1/2) ||H||_(L^2(S(c))) in top units.
  *Proof.* Count, then Hoelder, |S|^(3/4) <= 2^(3/4) s^3; Cauchy-Schwarz for
  the second. QED

**2.4 The background T.** I read Phi_n^(T) as the formula of Lemma 1 with
the parallel transports of T along the staircases and segments into the frame
at y. Ad is orthogonal on su(2), so every absolute bound of Sections 3 and 4
holds verbatim for Phi_n^(T); Lemmas 2 and 3 hold with errors of relative size
C f (transports of T within Q_y^(+1) differ from the identity by C f in a local
gauge of T, (TOP-tr)). If the Phi_n^(T) of (CMP) is defined by the recursion
2.2(d) with transports instead, the two differ by curvature terms at each level
times the level-k contour averages; I did not bound that difference (defect 3
of Section 7).

## 3. Hardest first: contour averages that grow with depth

**3.1 Lemma A (the exact L^4 count at a top centre; discharged).** Put
R_0 := empty, R_j(y) as in 2.3 with rho_j = (L^j + 2L^(j-1))/2 for j >= 1, and
the annuli A_j(y) := R_j(y) \ R_(j-1)(y), j = 1, ..., n. For every fine 1-form
theta and top centre y,

    |Phi_n theta(y)| <= C_A(L) sum_(j=1)^n ||H||_(L^4(A_j(y))),     C_A(L) := 3.4 L + 1.

*Proof.* Write tau_k for the k-th term of Lemma 1, s = L^(k-1); it reads only
R_k, and |tau_k| <= sum_c w^(k)(c) |Q_path^(s) theta(c)|. Split theta on R_k
into its parts on R_(k-2) and on A_(k-1) u A_k.
(i) *Same scale.* By Lemma 4 and sum_c w^(k)(c) < L, the part on A_(k-1) u A_k
contributes at most 2^(3/4) L (||theta||_(l^4(A_(k-1))) + ||theta||_(l^4(A_k))).
(ii) *Finer scales, k >= 3.* R_(k-2) lies within sup-distance
rho_(k-2) <= L^(k-2) <= s/3 of y. If S(c) meets it, then for nu != mu,
|x_nu - y_nu| <= (s - 1)/2 + s/3 < s, so x_nu = y_nu, and
x_mu - y_mu lies in [-(3s - 1)/2 - s/3, (s - 1)/2 + s/3] intersected with sZ,
which is {-s, 0}: c is one of the 8 bonds at y, of total weight below 1. By the
first bound of Lemma 4 and Hoelder on each annulus,
|tau_k(theta 1_(R_(k-2)))| <= s^-3 sum_(j <= k-2) |A_j|^(3/4) ||theta||_(l^4(A_j)),
and |A_j| <= |R_j| <= 4 (2 rho_j + 1)^4 <= 64 L^(4j) (as 2 rho_j + 1 <= 2 L^j for
L >= 3). So the part is at most 22.7 sum_(j <= k-2) L^(-3(k-1-j)) ||theta||_(l^4(A_j)).
Summing over k, each A_j receives at most 2 x 2^(3/4) L from (i) and
22.7 sum_(i >= 1) L^(-3i) <= 0.88 from (ii). Finally ||theta||_(l^4(A)) =
||H||_(L^4(A)). QED

**Corollary A1 (what (REL-4) alone gives).** By Hoelder over the n disjoint
annuli, |Psi(y)| <= C_A(L) n^(3/4) ||H||_(L^4(Q_y^(+1))). So (REL-4) gives
(REL-Phi) with a constant growing like n^(3/4) = (log B / log L)^(3/4), and no
better: Example E below attains this growth.

**Corollary A2 (one notch above criticality is enough).** For p > 4, Hoelder
in top units gives ||H||_(L^4(A_j)) <= (64 L^(-4(n-j)))^(1/4 - 1/p) ||H||_(L^p(A_j)),
so

    |Psi(y)| <= C_A(L) 2^(3/2) (1 - L^-(1 - 4/p))^-1 ||H||_(L^p(Q_y^(+1))),

uniformly in depth. Each level gains (L^-(n-j))^(1-4/p): this is the
counterpart, one derivative up, of the gain s_j^(1/4) per level in `lc-u` (5.6)
and (5.7). There the summand is a curvature angle, which is s_j times a
critical norm; here it is a potential angle, which is a critical norm with no
factor, so at p = 4 there is no gain at all.

**Corollary A3 (point defects at the centres are free).** If
||H_2||_(L^4(A_j(y))) <= M L^(-alpha j) for some alpha > 0, then H_2 adds at most
C_A(L) M / (1 - L^-alpha) to Psi(y). So a fine-scale defect at each top centre,
whose critical mass sits at the finest scales, is harmless; what is fatal is
critical mass spread evenly over the n scales.

**3.2 Run (registered criterion 2; guidance).** The kernel w_n of
theta -> Phi_n theta(0), built from Lemma 1, reproduces the actual nested map
(criterion 1 below), and its exact l^(4/3) norms are:

| (L, n) | N_tot (all bonds) | N_tot / n^(3/4) | per level, k = 1 ... n | N_ann on A_1 ... A_n | C_A(L) |
|---|---|---|---|---|---|
| (3, 1) | 1.117 | 1.117 | 1.117 | 1.117 | 11.2 |
| (3, 2) | 1.660 | 0.987 | 1.117, 0.838 | 1.340, 0.584 | 11.2 |
| (3, 3) | 2.127 | 0.933 | 1.117, 0.838, 0.806 | 1.345, 0.870, 0.523 | 11.2 |
| (5, 1) | 1.522 | 1.522 | 1.522 | 1.522 | 18.0 |
| (5, 2) | 2.346 | 1.395 | 1.522, 1.258 | 1.674, 1.096 | 18.0 |

N_tot is the exact constant of |Psi(0)| <= N_tot ||H||_(L^4) (duality); it
grows, each level adding a scale-invariant amount (0.84, 0.81 at L = 3), as
Lemma A's proof says. Every annular norm is far below C_A(L) (criterion 2:
PASS, Lemma A not refuted; the hand constant is crude). Mass of w_n outside
R_n(0): 0; sum of w_n over direction-mu bonds: at most 4.4e-16 (Lemma 3).
Identities (criterion 1): Lemma 1 against the recursion 2.2(d), 3.7e-16;
Q_2 = Q_path^(9) - d' Phi_2 on `balaban_Q`, 1.3e-15; gauge law, 2.1e-16;
constants, 4.1e-17; kernel against the torus value, 4.8e-16. PASS.
(`checks/relphi/relphi.py`, log `relphi_run.log`, data `relphi_results.json`;
under the numeric lock, 65 percent memory free, 3.5 s, 0.8 GB.)

**3.3 Example E (a relative field with bounded local energy whose contour
averages grow at every top centre; discharged).** Let R := floor((B - 1)/4) >= 2,
phi(r) := log(1 + r)/log(1 + R) for 0 <= r <= R and phi(r) := 1 for r >= R,
e a fixed unit vector of su(2), a > 0, and

    lambda(z) := a e phi( min over top centres y' of |z - y'|_inf ).

(E1) lambda = 0 at every top centre: the gauge e^lambda is admissible. The
sup-balls of radius R about distinct centres are disjoint and inside their
blocks, and lambda = a e off them.
(E2) d lambda is a pure gauge in a fixed direction: zero curvature, and Q_n d lambda
= d' r_n lambda = 0, so the parent is untouched.
(E3) ||B d lambda||_(L^4(Q)) <= 4.25 a / log^(3/4)(1 + R) on every top cube.
*Proof.* Only bonds from sup-sphere r to r + 1 (r < R) carry d lambda, at most
4(64 r^3 + 16 r) of them for r >= 1 and 8 for r = 0, each with
|d lambda| <= a/((1 + r) log(1 + R)). So sum |d lambda|^4 <= a^4 (1.85 +
320 sum_(r=1)^(R-1) 1/(1 + r)) / log^4(1 + R) <= 322 a^4 / log^3(1 + R). QED
(E4) ||B d lambda||_(L^2(Q))^2 = B^-2 sum |d lambda|^2 <= B^-2 a^2 (3.9 + 160 R^2)
/ log^2(1 + R) <= 11 a^2 / log^2(1 + R).
(E5) By Lemma 2, Psi(y) = Av_B lambda(y) = a e (1 - c_R) with
0 <= c_R <= ((2R + 1)/B)^4 <= 0.2, so |Psi(y)| >= 0.8 a at every top centre.

With a := t log^(3/4)(1 + R)/4.25: ||B d lambda||_(L^4(Q)) <= t,
||B d lambda||_(L^2(Q)) <= 0.8 t / log^(1/4)(1 + R), and
|Psi(y)| >= 0.18 t log^(3/4)(1 + R) >= 0.1 t (log B)^(3/4) for B >= 81.
*Run (criterion 3, illustration):* the exact sums at L = 3 give
Psi / ||B d lambda||_(L^4) = 0.66, 0.80, 0.99, 1.17, 1.35, 1.53, 1.70, 1.87,
2.03, 2.19, 2.34 for n = 2, ..., 12, that is 0.33 to 0.34 times (log B)^(3/4)
throughout.

**3.4 What Example E refutes, and what it does not.**
- **(C1) "(REL-g), (REL-2), (REL-4) imply (REL-Phi) in the same gauge" is
  REFUTED** (linear level, hand construction). Take an admissible relative
  field H_0 with those clauses on a torus on which (K_delta * E)(Q) >= e_0 >=
  eps_0 max_Q (K_delta * E)(Q) (a parent of roughly uniform flux), and
  t := C_4 e_0^(1/2). Then H_0 + B d lambda is admissible, satisfies (REL-4) with
  2 C_4 and (REL-2) with C_2 + 1 once log(1 + R) >= (0.8 C_4)^4, and has
  |Psi(y)| / (K_delta * E)(Q_y)^(1/2) >= 0.1 C_4 eps_0^(1/2) (log B)^(3/4) - C, so
  no C_Phi(L) works at large depth. Nonlinearly the same holds while the twist
  of the rotation e^lambda against T stays below the absolute constant, i.e.
  for a below c/f, which still gives a ratio of order min((log B)^(3/4), 1/f).
- **(C2) No gauge-invariant bound can give (REL-Phi).** Example E adds zero
  curvature. So the curvature-L^4 count of `lc-u` 5, which bounds holonomy
  defects, cannot by itself bound Psi; Corollary A2 is the form that applies.
- **(C3) (R3)'s H^2 bound does not transfer to the global gauge by itself.**
  In a local Landau gauge with an H^2 bound, Psi is bounded (Corollary A2 and
  the lattice Sobolev inequality of mapped Text 5.3, not rebuilt here). The
  global admissible gauge differs by a gauge omega with B d omega only in L^4
  (both fields are), and by Lemma 2 Psi changes by Av_B omega(y) - omega(y): a
  point value at the centre against a block average, which L^4 data do not
  control. Example E is exactly such an omega.
- **(C4) Example E does not refute (REL-Phi).** It is removable: undo the
  gauge. A counterexample must show that *every* admissible gauge with (REL-2)
  and (REL-4) has large Psi. Section 4 shows there is none at the linear level.

## 4. No counterexample at the linear level; why the nonlinear level is different

**4.1 Lemma CAP (linear level: (REL-Phi) is implied by the other clauses;
discharged).** Linear flat setting: theta = H/B admissible, i.e. Q_n theta = 0,
with (REL-2) (C_2, delta absolute) and (REL-4). Then there is a fine 0-form
lambda, zero at every top centre, such that H' := H + B d lambda has
Phi_n theta'(y) = 0 at every top centre, and (REL-2), (REL-4) with
C_2' = C (C_2 + 1), C absolute, and C_4' = C(L)(C_4 + 1), uniformly in depth and
volume, for n >= n_0(L). For n < n_0(L), (REL-Phi) holds in the original gauge
with C_Phi = 3 C_A(L) n_0(L)^(3/4) e^(C delta) C_4 (Corollary A1). Either way
(REL) holds at the linear level with (REL-Phi).

*Proof.* Since Q_n theta = 0, Q_path^(B) theta = d' Psi (`seam-quadratic-c` 2.2(d)).
Let T_0, T_1 be the tensor right inverse of `seam-quadratic-c` 3 at side B
(Av_B T_0 = I, d T_0 = T_1 d', sum_(y') |zeta_(y')(z)| < 2^4, range below 2 top
units, and Lemma PG (iv) of `seam-nonlinear-c`). Let phi_y be the log profile of
Example E about y with R := floor(B^(1/2)) (R <= (B - 1)/4 once B >= 25), and
c_R := Av_B(1 - phi_y)(y) <= ((2R + 1)/B)^4 <= 81 B^-2. Let K := r_n T_0 on top
0-forms (sup-norm at most 16, range 1) and, once 16 c_R <= 1/2,

    mu := (I - c_R K)^-1 Psi,    lambda := -T_0 mu + sum_y (T_0 mu)(y) (1 - phi_y).

Then lambda(y) = 0 (the bumps are disjoint, 1 - phi_y(y) = 1), and
Av_B lambda(y) = -mu(y) + c_R (K mu)(y) = -Psi(y). By Lemma 2,
Phi_n(theta + d lambda)(y) = Psi(y) + Av_B lambda(y) = 0 exactly. Costs, on a top
cube Q containing the centre y:
- *Smooth part.* -B d T_0 mu = -B T_1 d' mu, and d' mu = Q_path^(B) theta + c_R d' K mu.
  The first gives at most 12.8 ||H||_(L^2(Q^(+3))) and 58 ||H||_(L^4(Q^(+3)))
  (Lemma PG (iv)); the second is pointwise at most 24 x 32 x 16 c_R max_near |Psi|,
  negligible. These are absolute constants: this is where admissibility is used,
  since only differences of Psi enter.
- *Bumps.* By (E3), (E4) with a = |(T_0 mu)(y)| <= 32 max_near |Psi|:
  L^4 cost at most 4.25 x 32 max_near |Psi| / log^(3/4)(1 + R), L^2 cost at most
  3.4 x 32 max_near |Psi| / log(1 + R) x (R/B) x 4.
- *Depth count.* By Corollary A1, max_near |Psi| <= 3 C_A(L) n^(3/4) e^(C delta)
  C_4 (K_delta * E)(Q)^(1/2), and log(1 + R) >= (n/2) log L. So the L^4 cost is at
  most C(L) C_4 (K_delta * E)(Q)^(1/2) with C(L) free of n, since
  n^(3/4) / (n log L / 2)^(3/4) = (2/log L)^(3/4); and the L^2 cost carries the
  extra factor R/B <= L^(-n/2), so it is below (K_delta * E)(Q)^(1/2) for
  n >= n_0(L). The Neumann series and T_0 have bounded range, so the kernel
  K_delta absorbs the enlargements at a factor e^(C delta). QED

*Reading.* The worst growth allowed by (REL-4), n^(3/4) (Lemma A, sharp by
Example E), is exactly absorbed by the 4-capacity of a point at depth n in
d = 4, (log B)^(-3) in ||.||_4^4. So at the linear level, contour averages
are a gauge artifact of size and cost both critical, and they can be removed;
no linear counterexample to (REL) can come from them. This sharpens the
statement of `seam-nonlinear-c` that "at the linear level that size is
irrelevant": no root gauge is needed, the gauge stays admissible, and C_2
stays absolute.

**4.2 Why Lemma CAP does not carry to the nonlinear level (diagnostic, not a
theorem).** The gauge of 4.1 has |lambda| up to |mu|, of order
C(L) n^(3/4) (K_delta * E)^(1/2), on the bulk of each block. As a rotation
e^lambda acting on U alone:
- (N-a) *Twist.* The relative field becomes
  B log(e^(lambda(x)) e^(H_b/B) T_b e^(-lambda(x+b)) T_b^-1). Interpolated with the
  transports of T, lambda is consistent only up to the holonomy of T around
  loops of top size, so a term of size C f |lambda| appears in top units
  (`seam-nonlinear-c` 3.4). Relative to (K_delta * E)^(1/2) it is C(L) f n^(3/4):
  not depth-uniform, and it would enter the absolute constant of (REL-2).
- (N-b) *Scrambling.* H is rotated by Ad e^(lambda(z)), which runs from 1 at
  the centre to about e^(-mu) in the bulk, along the very staircases of
  Lemma 1. The new contour average differs from Psi + Av_B lambda by up to
  min(2, sup |lambda|) sum_b |w_n(b)| |theta_b|, which is Lemma A's annular sum
  again, not small under (REL-4) alone.
So at the nonlinear level a contour average that has grown like n^(3/4)
cannot be removed after the fact at controlled cost. The gauge has to be
chosen with the annular sum bounded from the start. That is (REL-D) below.

## 5. The reduction: (REL-Phi) from an L^4 condition on L-adic annuli

**5.1 The smaller inequality.** In the admissible gauge of (REL), at every
top centre y,

    (REL-D)   sum_(j=1)^n ||H||_(L^4(A_j(y))) <= C_D(L) (K_delta * E)(Q_y^(+1))^(1/2),

uniformly in depth and volume, with A_j(y) the annuli of Lemma A (sup-distance
from y between rho_(j-1) and rho_j, rho_j = (L^j + 2L^(j-1))/2). (REL-4) says the
same with an l^4 sum over the n annuli in place of the l^1 sum; nothing else
changes.

**Theorem R (implication; discharged as an implication).** (REL-D) implies
(REL-Phi) with C_Phi = C_A(L) C_D(L) (1 + C f) e^(C delta), C_A(L) = 3.4 L + 1.
*Proof.* Lemma A, with the transports of T as in 2.4, and
(K_delta * E)(Q_y^(+1)) <= 3^4 e^(2 delta) (K_delta * E)(Q_y). QED

*Why it is strictly smaller.* (REL-D) has no contour, no nested map, no
transport and no line integral: it is a Lebesgue bound on H in L-adic shells
about the top centres, one notch above (REL-4). It is the sharp
gauge-by-gauge form: Lemma A gives the sufficiency, Example E shows that the
l^4 sum of (REL-4) loses exactly the factor n^(3/4) that separates it from
(REL-D). It is not necessary for (REL-Phi) (Psi can be small by cancellation),
and it is not needed at all at the linear level (Lemma CAP).

**5.2 What supplies (REL-D), in decreasing strength.**
- A pointwise bound sup over Q_y^(+1) of |H| <= C(L) (K_delta * E)^(1/2) in top
  units (Corollary A2 with p = infinity: |Psi(y)| <= 2^(3/2) C_A(L)
  (1 - 1/L)^-1 sup |H|).
- (REL-p) for one p > 4 (Corollary A2).
- An H^2 bound on H at the top scale in the admissible gauge, through the
  lattice Sobolev inequality quoted in mapped Text 5.3
  (||grad f||_(L^4) <= C (||grad^2 f||_(L^2) + ||grad f||_(L^2)), then L^4 into
  L^p on a box; not rebuilt here, label: implication from that inequality).
- Any of these for a regular part H_1, plus a defect H_2 at the centres whose
  annular L^4 norms decay geometrically (Corollary A3). The point multipliers
  of the L^2-minimal admissible gauge are of this kind if the lattice Green's
  function gradient obeys |grad G(x)| <= C |x|^-3 (not rebuilt), giving
  ||mu grad G||_(L^4(A_j)) <= C |mu| L^(-2j). Note that (REL-p) itself fails for
  that defect, by B^(1 - 4/p) |mu|, so (REL-D), not (REL-p), is the right form.

*Consistency with the only known concentration mechanism.* At a curved
background the composite adjoint has residual contour sums concentrated at
nested block centres (mapped Text 5.3, (R3) and the composite-adjoint
paragraph); the scaling count of `relative-density-bound` item 2 gives
|grad H| of order lambda a L^2 log_L(1/r) at distance r from a nested centre,
hence H bounded there. Bounded H gives (REL-D) with geometric shells
(first item above). So that mechanism produces no growth of Psi with depth.
This is a scaling count, not a proof.

**5.3 Answers to the queue row's sub-questions.**
- *Does the path coarsening and fourth-norm count of `lc-u` 5 apply to the
  composite contour average?* The coarsening applies exactly: Lemma 1 is the
  open-path cancellation, with contours from the top centre at every level.
  The fourth-norm count applies with no gain at the critical norm: a potential
  angle at level j is a critical norm with no factor s_j (Lemma 4), whereas a
  curvature angle is s_j times one. So with (REL-4) alone the count gives
  n^(3/4), and that is sharp (Corollary A1, Example E). One notch up it gives
  the gain (L^-(n-j))^(1 - 4/p) per level, the analogue of s_j^(1/4)
  (Corollary A2). A curvature-only version cannot exist (3.4 (C2)).
- *Given the H^2 bound of (R3)?* Only in the gauge where that bound holds. In
  (R3)'s local Landau gauges Psi is bounded (Corollary A2 plus lattice
  Sobolev). Passing to the global admissible gauge moves Psi by
  Av_B omega(y) - omega(y) for the gauge difference omega (Lemma 2), a point
  value at the centre that L^4 data do not control (3.4 (C3)). So (R3) gives
  (REL-Phi) if its H^2 bound holds in the admissible gauge itself, or if the
  gauge difference is bounded at the top centres (for instance by a discrete
  maximum principle when the global gauge has pointwise bounded divergence, as
  the gauge of (R2), D^* H = r^* c constant on blocks, would if c is pointwise
  bounded; not checked).
- *A relative field with bounded local energy whose contour averages at nested
  centres grow with depth:* Example E, Psi of order (log B)^(3/4) times the
  local energy at every top centre, with (REL-2) and (REL-4). It refutes the
  implication from (REL-4) in a given gauge, not (REL-Phi): it is a removable
  gauge (3.4 (C4)), and at the linear level every such growth is removable
  (Lemma CAP).

## 6. The other clauses of (REL) at the iterated trial, in one global gauge

**6.1 The constraint g = 1 at the top centres is harmless for (REL-2) and
(REL-4) (discharged at the linear level).** Let theta_L be the relative field
in any global gauge, not necessarily admissible, with centre values kappa(y)
of the gauge (so that Q_n theta_L = d' kappa at the linear level). The point
bumps lambda_b := -sum_y kappa(y) (1 - phi_y), R = floor(B^(1/2)), make it
admissible (Q_n(theta_L + d lambda_b) = 0) at cost, by (E3) and (E4),

    ||B d lambda_b||_(L^2(Q)) <= 13 B^(-1/2) |kappa(y_Q)| / log(1 + R),   ||B d lambda_b||_(L^4(Q)) <= 4.25 |kappa(y_Q)| / log^(3/4)(1 + R),

and they move the contour average by kappa(y)(1 - c_R). So the absolute L^2
constant of a supplier that works in its own (Landau-type) gauge survives the
constraint at no cost, and (REL-4) survives if |kappa| <= C(L) (log B)^(3/4)
(K_delta * E)^(1/2). What the constraint moves is the contour average: in the
unconstrained gauge the quantity to bound is Psi_L + kappa, whose differences
between neighbouring centres are Q_path^(B) theta_L (absolute) at the linear
level, so Lemma CAP applies to it unchanged. Nonlinearly the bumps live within
B^(-1/2) top units of the centres, so their twist against T is negligible in
L^2 and L^4; their effect on the contour average is bounded by
min(2, |kappa|) times Lemma A's annular sum, hence controlled under (REL-D).

**6.2 Linear level.** (REL-g) is empty. (REL-2) and (REL-4) for the pair
(A_*, A_t) at the flat background are the bounds on the fibre response
A_* - A_t (minimizer minus trial, an element of ker Q_n) with exponential decay
and an absolute L^2 constant, which is Theorem F's content at the flat
background (`library/fibre-propagator.md`, not read here), together with a
critical representative (Lemma PG of `seam-nonlinear-c`). Given those, Lemma
CAP supplies (REL-Phi), and 6.1 lets the supplier work in its own gauge.

**6.3 Nonlinear level at T: first step not carried.** All clauses together
need one admissible gauge in which the class minimizer is exp(H/B) T with
(REL-2) absolute, (REL-4) and (REL-D). The natural construction is the fixed
point of mapped (R2) run around the iterated trial T at depth n instead of
the one-shot trial U^tr at one level, in the admissible class, which needs
Sad#(T) invertible with exponential decay (Theorem F at T), the identification
of the fixed point with the class minimizer (item (o) of
`relative-density-bound`, a sketch), and the regularity step of (R3) carried
out in the admissible gauge itself, so that its H^2 bound gives (REL-D)
directly (5.2) rather than through a local-to-global gauge comparison
(5.3). None of these is written for T, and I did not attempt them here. By
4.2, a gauge chosen first and corrected afterwards does not do: a contour
average that has grown like n^(3/4) cannot be removed nonlinearly at
controlled cost. The first step not carried is Theorem F at T, as
`seam-nonlinear-c` found; for (REL-Phi) specifically it is (REL-D) in that
gauge.
