# gap-boundary-q (queue row 1036): route (ii) at the pinned boundary, (Q-INV) and (O2)
Worker: Claude Fable 5.2, medium effort, background agent on the lead's MacBook. Start: 2026-11-16T04:39:23Z (from `date -u`). Checked by: nobody.

## Plan (at most eight steps; each result is written here before the next step starts)
1. Read FINISH.md rules and row 1036, GOAL.md.
2. Read parts/gap.md, library/gap-sym-reg.md, library/gap-sym-reg-check-opus.md, gap-short-step-max.md 4.1-4.2, gap-aligned-frame.md. Fix the definitions of Q, Psi, H_c, pin, frame.
3. Grep the lane for earlier work on Q-INV, boundary gradients, curl inequality.
4. Hand test: one cube, lower face pinned. Compute Q(d lambda) for a boundary gradient.
5. Decide (Q-INV): proof, or a pin and lambda with Q(d lambda) > 0 and its value.
6. Decide (O2): curl inequality with C written, or a counterexample.
7. Compact U(1) control (zero gain) and the meaning for route (ii).
8. RESULT line.

## Step log

### Step 1 (done 2026-11-16T04:49:55Z): the brief

Read: FINISH.md sections "Joining", "Working efficiently", "Rules", and row 1036; GOAL.md (no computer-assisted step; marks).
Two statements to decide, in this order.
- **(Q-INV).** Pinned cell, order-one coupling, a site frame whose boundary values are functions of the pin, finite range.
  Is Q(theta n) the same after theta -> theta + d lambda, with lambda supported on pinned sites?
- **(O2).** Q(theta) <= C sum_p (d theta)_p^2 for boundary gradients. For theta = d lambda the right side is 0, so (O2) on
  gradients says Q(d lambda) <= 0.

### Step 2 (done 2026-11-16T04:49:55Z): sources read; definitions fixed

Read: `parts/gap.md` L1-100; `library/gap-sym-reg.md` (row 1034) L18-400; `library/gap-sym-reg-check-opus.md` (row 1035)
Step 5 and Step 8; `library/gap-short-step-max.md` 4.1-4.5; `library/gap-aligned-frame.md` Steps 2-4, 7;
`library/gap-pinned-cell-gauge-max.md` (row 1011) 3.1, 3.2, 4.2, 4.4.

Conventions (row 1011 3.1-3.2). SU(2) = unit quaternions; su(2) = Im H = R^3; t(g) = Re g, s(g) = Im g. For imaginary u, v:
u v = - u . v + u x v. A link l = (x -> y) has tail x and head y. Gauge: U_l -> g_x U_l g_y^(-1). Plaquette (x; mu, nu):
U_p = U_1 U_2 U_3^(-1) U_4^(-1), and [p : l] = +1 on l_1, l_2 and -1 on l_3, l_4.
Cell: a box with sides S_mu. A link is pinned if it lies in a boundary face. The action counts ALL plaquettes of the cell,
the boundary plaquettes included (row 1011 3.1):  A(U, omega) = sum_p beta_p w_p t_p,  Z_c(omega) = int e^A dU_int,
F_c = - log Z_c. Weights: w_p = 1 inside, 1/2 on a boundary plaquette of one face. Z_c(omega^g) = Z_c(omega) for every g on the sites.
R_(l,a) f = (d/d eps) f(U_l -> e^(eps e_a) U_l). With A = Re(U_l S_l) + A' (S_l the staple sum, A' free of U_l): N_l = Im(U_l S_l),
and R_(l,a) A = - N_l^a. For a pinned link l, E[N_l] is the gradient of F_c in the pin: (d/d eps) F_c(e^(eps a) omega_l) = a . E[N_l].
Frame: unit vectors n_x. On pinned sites n_x = n_x(omega). D_l n = n_tail - Ad(U_l) n_head.
Move: V = theta n, the rotation theta_l n_tail(l) on every link; on pinned links it moves the pin (omega_s = exp(s B) omega).
Psi_V = V A + div V (Lemma FLOW, row 1018 4.1).  **Q(theta) := - E_omega[V Psi_V]**, and
H_c(omega; B) = Q(theta) - Var_omega(Psi_V) <= Q(theta) (FLOW; row 1026 7.1).
For interior theta with (REG): Q(theta) = E[Psi^2] and Q(theta, d lambda) = Cov(Psi_theta, Psi_(d lambda)) (check 1035, Step 5).
So Q(theta + d lambda) = Q(theta) for all theta needs Q(d lambda) = 0 at least.

### Step 3 (done 2026-11-16T04:49:55Z): search of the lane (rule "Repo first")

Grep of `library/`, `parts/`, `gates/` in this checkout. Other branches and origin/main were NOT searched by this row.
- "Q-INV", "lower face pinned", "gauge return": no earlier hit in this sense.
- "boundary gradient", "Q(d lambda)": rows 1026, 1027, 1034, 1035 only. Row 1034 6.6 gives the formula
  Q(d lambda) = E[direct(b)] - 2 sum (n_tail x Ad(U_l) n_z) . E[N_l]; check 1035 re-derived it. Neither evaluates it.
- "trivial pin": row 1011 4.2 (Proposition B'): with strength b on boundary plaquettes and 0 inside,
  H_c(1; B) = b sum w_p |B_1 + B_2 - B_3 - B_4|^2, positive on a closed theta; for homogeneous strength "ARGUED only".
  Row 1016 Theorem BH: for homogeneous strength, a lower bound on the supremum over pins (and on the free-pin mean) of
  H_c(omega; a theta) for a FIXED colour a. It "says nothing about the trivial pin" (row 1016 L790). Row 1011 4.4: the
  bound H_c(1; a theta) <= b times the classical action is OPEN. Check 1014 names the unproved route "omega = 1 minimises F_int".
- No row gives the value of Q(d lambda), or of H_c, for a pin-measurable frame at homogeneous strength at a named pin.
  The statements below (GR, TP, CUBE, SIGN, MASS) are new in this lane in that sense. The character expansion they use
  is standard and is used elsewhere in the lane (row 1016 L865).

### Step 4 (done 2026-11-16T04:51:51Z): one exact identity, then the cube by hand

All of Step 4 is PROVED by hand here unless marked. Nobody checked it.

**4.1 Theorem GR (gauge return: a boundary gradient is a move of the pin alone).**
Setting. Any finite set of plaquettes with a set of pinned links (a box cell, or the cube of 4.2). A site is pinned if it
has a pinned link. Let L be the set of pinned sites z such that every free link at z has tail z. (Box with all S_mu >= 2:
L is the boundary without the relative interiors of the upper faces {x_mu = S_mu}; the head of a free link out of L is a
free site.) Let n be unit vectors on the pinned sites (functions of the pin; nothing else is assumed), lambda a real
function supported on L, and V = (d lambda) n: (lambda_tail - lambda_head) n_tail on pinned links, lambda_z n_z on the free links out
of z in L. V is a fixed field, so div V = 0 and Psi_V = V A. For a pinned link l = (x -> y) put tau_l = lambda_y and

  W_l(eps) = exp(- eps tau_l n_x) exp(eps tau_l Ad(omega_l) n_y),     omega_eps := (W_l(eps) omega_l)_l   (a curve of pins).

Then, for every U and eps:
 (a) A(e^(eps V)(U, omega)) = A(U, omega_eps). The free links do not move on the right side.
 (b) W_l(eps) = exp(eps b_l + eps^2 c_l + O(eps^3)) with  b_l = - tau_l D_l n  and  c_l = tau_l^2 n_x x D_l n.
 (c) Psi_(d lambda) = sum over pinned l of tau_l (D_l n) . N_l.
 (d) Q(d lambda) = - E[(d/d eps)^2 A(U, omega_eps)] at eps = 0
       = sum over pinned l of tau_l^2 ( |D_l n|^2 E[Re(omega_l S_l)] + 2 (n_x x D_l n) . E[N_l] ) - E[M(b)],
     where M(b) = sum over ordered pairs l != l' of b_l^a b_l'^a' R_(l,a) R_(l',a') A (pairs of pinned links in one plaquette).
 (e) H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(omega_eps) at eps = 0 = Q(d lambda) - Var(Psi_(d lambda)).
Proof. (a) Let g_x = exp(eps lambda_x n_x) on pinned sites and 1 on free sites. A is invariant under g^(-1). On a pinned link
(x -> y): g_x^(-1) exp(eps (lambda_x - lambda_y) n_x) omega_l g_y = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y) = W_l omega_l. On a free link
out of z in L: g_z^(-1) exp(eps lambda_z n_z) U_l = U_l (its head is free, g = 1 there). No free link has its head in the support
of lambda. (b) With n = n_x, m = Ad(omega_l) n_y, tau = tau_l: W = (1 - eps tau n - eps^2 tau^2/2)(1 + eps tau m - eps^2 tau^2/2) + O(eps^3)
= 1 + eps tau (m - n) + eps^2 tau^2 (- 1 + n . m - n x m) + O(eps^3). So W'(0) = - tau D n and
W''(0) = - tau^2 |D n|^2 - 2 tau^2 n x m. exp(eps b + eps^2 c) has second derivative b^2 + 2 c = - |b|^2 + 2 c, so c = - tau^2 n x m
= tau^2 n x D n (n x n = 0). (c) (d/d eps) A(U, omega_eps) = sum_l R_(l, b_l) A = - sum_l b_l . N_l. (d) Q = - E[V V A] and V V A is
the second derivative of A along the flow of the fixed field V; use (a). A is affine in each link, with
A = Re(omega_l S_l) + A'. Re(W_l''(0) omega_l S_l) = - tau^2 |D n|^2 Re(omega_l S_l) + 2 tau^2 (n x m) . N_l (Re(v q) = - v . Im q for imaginary v),
and n x m = - n x D n. The mixed second derivatives are M(b). (e) Z_c(e^(eps B) omega) = Z_c(omega_eps) by the gauge covariance of Z_c
(row 1011 3.1) with the same g, and F_c'' = - E[A''] - Var(A') along a curve of pins. QED
Reading. The move (d lambda) n is the gauge transformation exp(eps lambda n) followed by a pin move with velocity - lambda_head D n.
It is a pure gauge move exactly when D n = 0 on the pinned links into the support of lambda. Row 1034 6.6 has the formula of (d)
for one site; (a), (b), (e) put the whole statement in the pin.
U(1): D n = 0, W = 1, omega_eps = omega. So Psi = 0, Q(d lambda) = 0 and H_c = 0 for every boundary lambda. Passes, zero gain.

**4.2 The cube with its lower face pinned: partition function.**
Sites {0,1}^3. Pinned: the four links of the face {x_3 = 0}; they form one plaquette p_0, with weight b_0 := beta_(p_0) w_(p_0) >= 0
and holonomy h. The other five plaquettes have strength beta > 0 and weight 1. Free: four vertical links, four top links.
L is the four lower sites. Facts used (f(g) := e^(beta t(g)), chi_d the character of dimension d, chi_d = U_(d-1)(t), the
Chebyshev polynomial of the second kind):
 (C1) f = sum over d >= 1 of d u_d(beta) chi_d with u_d > 0 and u_d' > 0 for beta > 0, the series converging absolutely with
      all beta-derivatives. Proof of the signs: t = chi_2/2, and chi_2^k is a sum of characters with non-negative integer
      multiplicities (Clebsch-Gordan), chi_d occurring in chi_2^(d-1); so d u_d = int f chi_d is a power series in beta with
      non-negative coefficients, not identically zero, without constant term for d >= 2 and with a positive beta^2 term
      for d = 1. RECALLED, used only for the GUIDE numbers: u_d = 2 I_d(beta)/beta, u_d'/u_d = I_(d+1)/I_d + (d - 1)/beta.
 (C2) For a class function f: int f(Y) D^d(Y) dY = (int f chi_d / d) 1 = u_d 1 (Schur), and f(Y^(-1)) = f(Y).
Lemma CUBE-Z.  Z_c(omega) = e^(b_0 t(h)) G(t(h)),   G(t) := sum_d d u_d^5 U_(d-1)(t).  With strengths beta_1, ..., beta_5 on the five free
plaquettes and the trivial pin: Z = e^(b_0) sum_d d^2 u_d(beta_1) ... u_d(beta_5).
Proof. For fixed vertical links V_x substitute T' = V_a T V_b^(-1) in each top link T (over the lower link a -> b). The side
plaquette over omega_k becomes Re(omega_k T_k'^(-1)) and the top plaquette is conjugated. So the vertical links drop out. Put
Y_k = omega_k T_k'^(-1). The top holonomy is Y_1^(-1) omega_1 Y_2^(-1) omega_2 omega_3^(-1) Y_3 omega_4^(-1) Y_4. Expand f of it by (C1) and integrate each Y_k
by (C2): the result is sum_d d u_d u_d^4 chi_d(omega_1 omega_2 omega_3^(-1) omega_4^(-1)). QED
Consequences at the trivial pin (homogeneous beta). For each of the five free plaquettes
  xbar := E_1[t_p] = sum_d d^2 u_d^4 u_d' / sum_d d^2 u_d^5,   0 < xbar < 1     (differentiate log Z in beta_p; (C1) gives the sign),
and with U_(d-1)(1) = d, U_(d-1)'(1) = d (d^2 - 1)/3 (from sin(d phi)/sin(phi) = d - d (d^2 - 1) phi^2/6 + ..., t = cos phi):
  kappa := (d/dt) log G at t = 1 = sum_d d^2 (d^2 - 1) u_d^5 / (3 sum_d d^2 u_d^5) > 0,    (d/dt) F_c = - (b_0 + kappa) at t(h) = 1.
So F_c is a function of t(h) alone, and the trivial pin (t = 1) is its minimum: |chi_d| <= d gives G(t) <= G(1).

**4.3 Lemma CUBE (the values, trivial pin, any unit vectors n_000, n_100, n_010, n_110).**
Let lambda be the indicator of 110, l_1 = (100 -> 110), l_2 = (010 -> 110), delta_1 = n_110 - n_100, delta_2 = n_110 - n_010. Then
 (i)   Psi_(d lambda) = - delta_1 . N_(l_1) - delta_2 . N_(l_2);
 (ii)  **Q(d lambda) = beta xbar (|delta_1|^2 + |delta_2|^2) + b_0 |delta_1 - delta_2|^2;**
 (iii) H_c(1; (d lambda) n) = (b_0 + kappa) |delta_1 - delta_2|^2 = (b_0 + kappa) |n_100 - n_010|^2;
 (iv)  Var(Psi_(d lambda)) = beta xbar (|delta_1|^2 + |delta_2|^2) - kappa |delta_1 - delta_2|^2.
Proof. (i) GR (c) with omega = 1, D_l n = n_tail - n_110. (ii) GR (a): the pinned links l_1, l_2 become W_1, W_2 with
b_i = delta_i. The side plaquette over l_i has holonomy W_i R_i up to conjugation, R_i a product of three free links.
The constant gauge transformation g at all eight sites fixes the trivial pin and the law, and sends Im R_i to
Ad(g) Im R_i; so E[Im R_i] = 0 and E[t(W_i R_i)] = t(W_i) xbar. By GR (b), t(W_i) = 1 - eps^2 |delta_i|^2/2 + O(eps^3). The lower
plaquette has holonomy W_1 W_2^(-1) = exp(- eps n_100) exp(eps n_010), with real part 1 - sin^2(eps) |n_100 - n_010|^2/2. The
top plaquette does not move. (iii) GR (e) and 4.2: F_c(omega_eps) is a function of t(h(eps)) = 1 - sin^2(eps) |n_100 - n_010|^2/2,
with derivative - (b_0 + kappa) at t = 1. (iv) = (ii) - (iii). QED
The same proof gives, for every lambda on the four lower sites, with b_l = lambda_head(l) (n_head - n_tail):
  Q(d lambda) = beta xbar sum over the four pinned l of |b_l|^2 + b_0 |sum_l [p_0 : l] b_l|^2,     H_c = (b_0 + kappa) |sum_l [p_0 : l] b_l|^2.
(At 000 there is no incoming link, b = 0: the gradient is a pure gauge move, as in STAR of row 1034.)

**4.4 What the cube shows.**
- Example A: n_100 = n_010 = i, n_110 = j. Q(d lambda) = 4 beta xbar > 0, H_c = 0, Var(Psi) = 4 beta xbar. Here the pin move is the
  gauge transformation at 110, and the fixed vector n_110 on the free link (110 -> 111) is the wrong extension: FLOW's
  bound is strict by the whole of Q. (The vector n_100 on that link gives the exact gauge move and cost 0. This is the
  freedom that check 1035 names: the pin vector on the link out of a boundary site is not forced.)
- Example B: n_100 = i, n_010 = n_110 = j. Q(d lambda) = 2 beta xbar + 2 b_0 and H_c = 2 (b_0 + kappa) > 0. Here the RESPONSE itself is
  positive on a boundary gradient. No interior extension, with any frame, can give a bound <= 0, since every FLOW
  bound is >= H_c.
- GUIDE values (4.5): at beta = 2.4, xbar = 0.5240 and kappa = 0.1085. Example A: Q = 5.03. Example B with b_0 = 0: Q = 2.52,
  H_c = 0.217; with b_0 = beta: Q = 7.32, H_c = 5.02.
- The covariant case on the cube is empty. A gauge-covariant unit vector at a lower site that is a function of the pin
  alone is fixed by the stabiliser of the pin, which is the circle about the axis of h (for s(h) != 0). So n = s(h_z)/|s(h_z)|,
  with h_z the holonomy based at z, D n = 0 on the four pinned links, and Q(d lambda) = H_c = Psi = 0 by GR. One pinned plaquette
  is a reducible pin. The test needs a face with two plaquettes at a site; that is Step 5.
- U(1) on the cube: n is constant, delta = 0, every value above is 0. Passes with zero gain.

**4.5 GUIDE run (it evaluates the series of 4.2; it proves nothing).** One job under the numeric lock. The checkout is
sparse and has no `scripts/`, so the lock command was run from a copy of `scripts/lab_ops.py` and `scripts/automation_lock.py`
taken with `git show HEAD:` into the session scratch folder (same lock directory /tmp/physics-lab; acquire reported
"acquired", release "released"; 2026-11-16T04:50:31Z by `date -u`; under one second; python3 -I, thread variables 1;
peak memory under 20 MB). Script and output: scratch folder `r1036/cube_guide.py`, `r1036/cube_guide.out` (not committed).
| beta | xbar | kappa | beta xbar - kappa | I_2/I_1 (one free plaquette) |
|---|---|---|---|---|
| 1.0 | 0.243138 | 0.003190 | 0.239948 | 0.240194 |
| 2.3 | 0.507763 | 0.094566 | 1.073288 | 0.479279 |
| 2.4 | 0.523996 | 0.108475 | 1.149115 | 0.493513 |
| 2.6 | 0.554404 | 0.138670 | 1.302781 | 0.520342 |
| 4.0 | 0.701490 | 0.397610 | 2.408348 | 0.658047 |
A finite difference of log Z in beta agrees with xbar to six digits (a check of the algebra of u_d'/u_d only).

### Step 5 (done 2026-11-16T04:53:38Z): (Q-INV) decided. It FAILS, with values

All PROVED by hand here unless marked. Nobody checked it.

**5.1 Theorem TP (the value at the trivial pin, any box).** Box cell in any dimension with all S_mu >= 2, every boundary
link pinned to 1, any strengths beta_p >= 0 and weights w_p. Unit vectors n on the boundary sites, lambda supported on L (4.1),
b_l = lambda_head(l) (n_head(l) - n_tail(l)) on the pinned links. Then

  **Q(d lambda) = sum_p beta_p w_p xbar_p | sum over pinned l in p of [p : l] b_l |^2,     xbar_p := E_1[t_p]**   (xbar_p = 1 on boundary plaquettes).

Proof. Step 1, geometry. In the plaquette (x; mu, nu), if x_kappa is 0 or S_kappa for some kappa outside {mu, nu}, all four links are
pinned. If not, (x, mu) is pinned iff x_nu = 0, and (x + e_nu, mu) is pinned iff x_nu + 1 = S_nu; both would need S_nu = 1. The same
holds for the two nu-links. So the pinned links of a plaquette are none, all four, one, or one mu-link and one nu-link,
and these two share a site. In each case the holonomy along the curve of GR (a) is, up to conjugation,
What_p(eps) R_p, where What_p is the ordered product of the W_l^([p : l]) of its pinned links and R_p is the product of its free
links (R_p = 1 if there is none). Step 2, symmetry. The constant gauge transformation g on all sites fixes the pin 1
and the law, and sends Im R_p to Ad(g) Im R_p. So E[Im R_p] = 0, E[t(What_p R_p)] = t(What_p) xbar_p. Step 3. By GR (b),
What_p = product of exp(+-(eps b_l + eps^2 c_l + ...)), and for imaginary b_k, c_k:
Re product_k (1 + eps b_k + eps^2 (b_k^2/2 + c_k)) = 1 - eps^2 |sum_k b_k|^2/2 + O(eps^3). Step 4. The law does not depend on eps, so
Q(d lambda) = - (d/d eps)^2 sum_p beta_p w_p xbar_p t(What_p(eps)) at 0 (GR (d)). QED
Remark. For a pure-gauge pin omega = 1^h the same value holds with n_x replaced by Ad(h_x)^(-1) n_x (covariance of Z_c and of GR).
Control against row 1011 4.2: with beta = 0 inside, the sum runs over boundary plaquettes only, Var(Psi) = 0, and the
value is Proposition B' at B = (d lambda) n.

**5.2 Corollary TP4 (the lane's cell).** Four dimensions, S_1, S_2, S_3 >= 3, S_4 >= 2, homogeneous beta > 0, w = 1 inside and 1/2
on boundary plaquettes, trivial pin. Let z be in the relative interior of the face {x_4 = 0}, lambda the indicator of z,
delta_i = n_z - n_(z - e_i) and xbar_i = E_1[t_p] for p = (z - e_i; i, 4), i = 1, 2, 3. Then

  Q(d lambda) = beta [ sum_i (1 + xbar_i) |delta_i|^2 + (1/2) sum over i < j of |delta_i - delta_j|^2 ]  >=  beta sum_i (1 + xbar_i) |delta_i|^2,

and 1 + xbar_i > 0. So Q(d lambda) > 0 unless n_(z - e_1) = n_(z - e_2) = n_(z - e_3) = n_z.
Proof. b is delta_i on the incoming link (z - e_i, i) and 0 on every other pinned link (lambda_head = 0 there). The plaquettes
through (z - e_i, i): the interior one (z - e_i; i, 4), with that one moving link (if z_i = 1 its link (z - e_i, 4) is pinned
too, with b = 0); the boundary ones (z - e_i; i, j), j != i in {1, 2, 3}, with that one moving link, two per i; and
(z - e_i - e_j; i, j), which contains (z - e_j, j) as l_2 and (z - e_i, i) as l_3, one per pair. (z - e_i - e_4; i, 4) is not in
the cell. t_p > - 1 almost surely gives xbar_i > - 1. QED
Not proved: xbar_i > 0 for this cell (expected; proved on the cube, 4.2). Without the boundary plaquettes in the action
the value would be beta sum_i xbar_i |delta_i|^2, whose sign then rests on xbar_i > 0. The lane's F_c contains them (row 1011 3.1).
Not proved: H_c(1; (d lambda) n) > 0 for this cell. By GR (e) it is the Hessian of F_c at the trivial pin along a direction
that is not a gauge direction when some delta_i != 0 (the face stays connected without the three links). Its sign is the
open item "omega = 1 minimises F_int" of check 1014. On the cube it is PROVED positive (4.3 (iii)).
(Added in Step 6: Theorem H4 proves it for this cell when beta <= 3 and only one delta_i is not zero, by a direct bound on
Var(Psi); the general sign stays open.)

**5.3 Corollary OPEN-SET (a gauge-covariant frame of range 1, a set of pins of positive measure).** Cell of 5.2.
Frame on the face {x_4 = 0}: n_y(omega) = s(h_y)/|s(h_y)|, h_y the holonomy of the face plaquette (y; 1, 2) based at y. It is
gauge covariant, reads four pinned links at y, uses the same rule at every site, and is defined where s(h_y) != 0.
Then there is an open, non-empty set O of pins on which the frame is defined at z, z - e_1, z - e_2, z - e_3 and

  Q(d lambda) >= beta (1 + xbar_1)/2 > 0      for lambda the indicator of z.

Proof. Let Phi(omega, nu) be the right side of GR (d) for the pin omega and frame values nu in (S^2)^4 at the four sites.
Phi is the mean, in the law of the pin omega, of a polynomial in the entries of U, omega, nu; the density e^A/Z_c is continuous
in omega. So Phi is continuous, and (S^2)^4 is compact: for eta = beta (1 + xbar_1)/2 there is a neighbourhood N of the trivial pin
with |Phi(omega, nu) - Phi(1, nu)| <= eta for all nu and all omega in N. By 5.2, Phi(1, nu) >= beta (1 + xbar_1) |nu_z - nu_(z - e_1)|^2. Take the pin
omega^phi: U_(z - e_1 + e_2, 1) = exp(- phi i), U_(z + e_2, 1) = exp(- phi j), all other links 1 (the witness of row 1034 6.5). Then
h_(z - e_1) = exp(phi i), h_z = exp(phi j), so n_(z - e_1) = i, n_z = j, |n_z - n_(z - e_1)|^2 = 2, and omega^phi is in N for small phi > 0.
n_z and n_(z - e_1) are continuous near omega^phi. The pins where also s(h) != 0 at z - e_2 and z - e_3 are open and dense. So
O = {omega in N: the four vectors are defined, |n_z - n_(z - e_1)|^2 > 3/2} is open and not empty, and on it
Q(d lambda) = Phi(omega, n(omega)) >= (3/2) beta (1 + xbar_1) - eta. QED
A non-empty open set of pins has positive Haar measure, and positive measure in the law of the surrounding model.

**5.4 Proposition SIGN (at a pin where F_c is not stationary, Q(d lambda) takes both signs).** Cell and z as in 4.1, lambda the
indicator of z, l one pinned link into z, e_l := E[Re(omega_l S_l)], f_l := E[N_l] (the gradient of F_c in the pin link l).
Take pin-measurable vectors with D n = 0 on the other pinned links into z, m := Ad(omega_l) n_z, nu a unit vector orthogonal
to m, and n_tail(l) = cos(alpha) m + sin(alpha) (nu x m). Then, exactly,

  Q(d lambda) = 2 e_l (1 - cos alpha) + 2 sin(alpha) (nu . f_l).

Proof. GR (d) with one non-zero b, so M(b) = 0. |D_l n|^2 = 2 - 2 cos alpha. n_tail x D_l n = - n_tail x m = - sin(alpha) (nu x m) x m
= sin(alpha) nu. QED
So if f_l is not parallel to m, Q(d lambda) is negative for small alpha of one sign and positive for the other; it vanishes at
alpha = 0 and (e_l > 0) at tan(alpha/2) = - (nu . f_l)/e_l. Reading: Q(d lambda) is minus the mean second derivative of the action
along a curve of pins with acceleration c (GR (b)), so it contains the first-order term 2 c . grad F_c. Its sign is not
a stiffness. At a stationary pin (the trivial pin: f = 0 by the symmetry of 5.1) only the direct term is left, and it
is positive (5.1, 5.2). On the cube f_l = - (b_0 + kappa(t)) grad t(h) != 0 for t(h) near 1, h != 1.

**5.5 Verdict on (Q-INV): FAILS.**
- Q(theta + d lambda) = Q(theta) for all theta gives Q(d lambda) = 0 at theta = 0. GR (d) gives Q(d lambda) in closed form.
- A pin and a lambda with Q(d lambda) > 0 and its value: the cube, trivial pin, n_100 = n_010 = i, n_110 = j, lambda = indicator of 110:
  Q(d lambda) = 4 beta xbar(beta), xbar = sum d^2 u_d^4 u_d'/sum d^2 u_d^5 in (0, 1); GUIDE value 5.03 at beta = 2.4 (4.3, 4.5).
  The lane's cell, trivial pin: the value of 5.2, at least beta sum_i (1 + xbar_i) |delta_i|^2 > 0.
- It is not an effect of a null set of pins or of frames without covariance: 5.3.
- When it does hold: if D n = 0 on the pinned links into the support of lambda, the move is a pure gauge move and Psi = 0,
  Q(d lambda) = 0, H_c = 0 (GR). That needs a reducible pin near those sites (Lemma FR), or the cube's one-plaquette face.
  For compact U(1) it always holds.
- Not decided (OPEN, and not needed for the verdict): whether some special covariant frame rule has Q(d lambda) = 0 for
  every boundary lambda on a set of pins of positive measure. By 5.4 one scalar condition per site does not exclude it;
  by 5.3 it is false for the plaquette-axis rule. By 4.4 Example B and GR (e), where H_c > 0 no frame at all helps.
- Correction to check 1035's sentence "Q(d lambda) = H_c + Var(Psi) can vanish": true as arithmetic (5.4 gives pins and
  frames where it does), false at and near the trivial pin for every frame with D n != 0 there.

### Step 6 (done 2026-11-16T04:55:27Z): (O2) decided. It FAILS on gradients; the response itself is positive; the true bound is a mass term

All PROVED by hand here unless marked. Nobody checked it.

(O2) on a boundary gradient says Q(d lambda) <= C * 0 = 0 (row 1034 7.4: H_c + Var(Psi) <= 0). By 5.2 and 5.3 it fails at the
trivial pin and on an open set of pins, for every C. The next theorem shows more: there the quantity that Q bounds is
itself positive, so no better interior field can repair it.

**6.1 Theorem H4 (the response to a boundary gradient is positive; the lane's cell, 0 < beta <= 3).** Cell and z as in 5.2.
(i) Trivial pin, unit vectors with n_(z - e_2) = n_(z - e_3) = n_z, delta_1 = n_z - n_(z - e_1), lambda the indicator of z, p_1 = (z - e_1; 1, 4):

  H_c(1; (d lambda) n) = |delta_1|^2 [ beta (2 + xbar_1) - (beta^2/3) E_1[1 - t_(p_1)^2] ]  >=  beta |delta_1|^2 ( (1 + xbar_1) + (1 - beta/3) )  >  0   for delta_1 != 0.

(ii) For the plaquette-axis frame of 5.3 there is an open, non-empty set O' of pins on which
H_c(omega; (d lambda) n(omega)) > 0. On O', every bound of Lemma FLOW for the boundary rotation (d lambda) n, with any interior field
(any interior frame, a field-dependent vector on the link (z, 4), any range), is positive.
Proof. (i) By 5.2 with delta_2 = delta_3 = 0: Q(d lambda) = beta |delta_1|^2 ((1 + xbar_1) + (1/2)(1 + 1)) = beta (2 + xbar_1) |delta_1|^2. By GR (c),
Psi = - delta_1 . N_l with l = (z - e_1, 1), and at the trivial pin N_l = Im S_l. The four boundary staples are 1. So
N_l = beta Im R_1, with R_1 the staple of p_1 and t(R_1) = t_(p_1). The constant gauge transformation sends Im R_1 to
Ad(g) Im R_1 and fixes the law, so E[(Im R_1)^a (Im R_1)^b] = (1/3) E|Im R_1|^2 times the identity, and E|Im R_1|^2 = E[1 - t^2] <= 1.
So Var(Psi) = (beta^2/3) E[1 - t_(p_1)^2] |delta_1|^2 <= (beta^2/3) |delta_1|^2. H_c = Q - Var (GR (e)). xbar_1 > - 1 and beta <= 3 give the sign.
(ii) Theta(omega, nu) := H_c(omega; (d lambda) nu) = Phi(omega, nu) - Var_omega(Psi) is continuous in the pin and in nu in (S^2)^4 (as Phi in 5.3). At
nu* = (n_z; n_(z - e_1), n_(z - e_2), n_(z - e_3)) = (j; i, j, j), (i) gives Theta(1, nu*) = 2 h, h := beta (2 + xbar_1) - (beta^2/3) E[1 - t_(p_1)^2] > 0.
So Theta > h on a product neighbourhood N x N' of (1, nu*). Pin omega': U_(z + e_2, 1) = exp(- phi j), U_(z - e_3 + e_2, 1) = exp(- phi j),
U_(z - e_1 + e_2, 1) = exp(- phi i), U_(z - e_2, 1) = exp(phi j), all other links 1. Its plaquettes (y; 1, 2) have holonomy exp(phi j) at
y = z, z - e_2, z - e_3 and exp(phi i) at y = z - e_1 (each of the four set links lies in exactly one of these four
plaquettes: as l_3, l_3, l_3, l_1). So n(omega') = nu*, omega' is in N for small phi > 0, and n is continuous near omega'.
O' = {omega in N: n defined at the four sites, n(omega) in N'} is open and contains omega'. The last sentence is Lemma FLOW:
H_c <= - E[V Psi_V] for every extension V. QED
What (ii) does not cover: larger beta (the bound on Var is crude; with xbar_1 > 0 the same line gives beta <= 6); frames
with several non-zero delta_i (the covariances E[N_i N_j] are not computed); typical pins far from pure gauge.
Check against the cube: 4.3 (iv) is the same computation with the exact covariance, and there H_c >= 0 for every
frame and every beta.

**6.2 Lemma MASS (the bound that is true, with its constant).** Setting of 4.1, any pin, strengths with beta_p w_p <= b.
For every lambda supported on L, with tau_l = lambda_head(l):

  |Q(d lambda)| <= sum_p beta_p w_p [ ( sum over pinned l in p of |tau_l| |D_l n| )^2 + 2 sum over pinned l in p of tau_l^2 |D_l n| ],

and in four dimensions  |Q(d lambda)| <= b sum over pinned l of tau_l^2 (24 |D_l n|^2 + 12 |D_l n|) <= 60 b sum over pinned l of lambda_head(l)^2 |D_l n|.
Proof. By GR (a), (d): Q(d lambda) = - sum_p beta_p w_p E[(d/d eps)^2 t_p] along the curve, where the holonomy of p has the factors
W_l^(+-1) inserted. Its second derivative at 0 is a sum of terms Re(... W_k'' ...) and 2 Re(... W_k' ... W_j' ...), k < j, over the pinned
links of p, with unit quaternions in between. |W_k'(0)| = |b_k|, |W_k''(0)| = |b_k^2 + 2 c_k| <= |b_k|^2 + 2 |c_k|, and
|c_k| = tau^2 |n x D n| <= tau^2 |D n| (GR (b)). So |(d/d eps)^2 t_p| <= (sum_k |b_k|)^2 + 2 sum_k |c_k|. A plaquette has at most four
links and a link lies in at most six plaquettes: (sum of four)^2 <= 4 sum of squares. |D n| <= 2. QED
Sharpness. At the trivial pin the lower bound of 5.2 has the same form, beta (1 + xbar) tau^2 |D n|^2 per link. The term linear
in |D n| is real: it is 2 c . E[N_l], the first-order term of 5.4, and it vanishes at stationary pins.
U(1): D n = 0, the bound is 0. Passes, zero gain: the curl bound Q(theta) <= beta sum_p w_p (d theta)_p^2 of row 1034 4.1 stands,
with all plaquettes of the cell in the sum.

**6.3 Verdict on (O2).**
- (O2) as a curl inequality for boundary gradients, with any constant C: FAILS. Witness with value: 4.3 (ii) on the cube;
  5.2 in the lane's cell; an open set of pins with a covariant frame: 5.3.
- The stronger reading "some interior field gives a FLOW bound <= C sum (d theta)^2": FAILS as well, on the cube for every
  beta (4.3 (iii)) and in the lane's cell for beta <= 3 on an open set of pins (6.1).
- What holds, with the constant written: Lemma MASS, a term per pinned link in lambda^2 |D n|. It is a mass term for the part
  of theta that is a gradient along the boundary. It is zero exactly when the move is a pure gauge move.
- Where (O2) can hold pointwise: at pins where F_c is not stationary, for frames tuned to the pin gradient (5.4). There
  Q(d lambda) < 0 comes from the first-order term. No gain follows from it (ARGUED): the same term appears with the
  opposite sign for the mirror frame (alpha -> - alpha), and the sum of the two values is 4 e_l (1 - cos alpha).
- OPEN: (O2) for typical pins of the model (far from pure gauge) and frames with small |D n| on the boundary. By MASS
  this is a statement about the size of sum lambda^2 |D n|, which is (N1) of row 1011 7.4.

### Step 7 (done 2026-11-16T04:55:52Z): the U(1) control, and what the result means for route (ii)

**7.1 Compact U(1): zero gain (PROVED; it is row 1034 4.1 with GR).** One axis, Ad trivial, n constant, D n = 0. GR: W_l = 1,
the boundary gradient is a pure gauge move, Psi_(d lambda) = 0, Q(d lambda) = 0, H_c = 0, for every pin and every boundary lambda.
So (Q-INV) holds, (O2) holds with C = beta (Q(theta) = sum_p beta w_p E[cos F_p] (d theta)_p^2 over all plaquettes of the cell), TP gives 0,
MASS gives 0, and H4 has delta = 0. Every statement of this row passes for U(1), and none gives U(1) a gain. The row's
positive values come only from D n != 0, that is from Ad != 1.

**7.2 What it means for route (ii) (one paragraph; the facts cited are PROVED above, the reading is ARGUED).**
Route (ii) wanted the cost of a covariant frame move to be a curl form at order-one response, as it is for U(1). At the
pinned boundary this is now refuted with values, not only at the level of Psi: a boundary gradient (d lambda) n is a gauge move
followed by a real move of the pin with velocity - lambda D n (GR), and its cost at and near a pure-gauge pin is the positive
mass term beta sum (1 + xbar) lambda^2 |D n|^2 per pinned link (TP, TP4, OPEN-SET), with zero curl. The failure is not in the choice
of the interior field: on the cube for every beta, and in the lane's cell for beta <= 3, the response H_c itself is positive
on such a gradient (CUBE (iii), H4), and every FLOW bound lies above H_c. So no interior frame, no solution of Lemma O1
and no field-dependent vector on the links out of the boundary (the escape named by check 1035) can return the
scale-invariant blind bound for a pin-measurable boundary frame: the obstruction is the shape of F_c on the space of
pins, which is not flat along the non-gauge directions lambda D n. The only cases left are D n = 0 on the boundary
(reducible pins: a null set, and the U(1) case) and D n small on the boundary, where MASS bounds the extra cost by
60 b sum lambda^2 |D n|. The second is a statement about typical pins being smooth in some frame. It is (N1) of row 1011 7.4,
of the (K-flow) kind, and not a symmetry. Route (ii) at the pinned boundary is closed as an exact mechanism; with
row 1034 6.2 (interior conservation gives nothing by itself) it has no exact part left on record, and Lemma O1 has no consumer on record.

**7.3 Limits of this row.**
- H4 needs beta <= 3 and a frame with one non-zero delta_i; TP4's positivity uses the boundary plaquettes that the lane's
  F_c contains. xbar_i > 0 and "omega = 1 minimises F_int" in the 4D cell are not proved.
- The pins are the trivial pin and open sets near it. Nothing is proved for typical pins of the model at order-one
  coupling, where no symmetry gives E[N_l] = 0 and Q(d lambda) has no sign (SIGN).
- Upper faces {x_mu = S_mu} (relative interior) are outside L: there a free link has its head on the boundary and its
  tail frame may depend on the field. Not treated.
- A general theta (boundary part not a gradient) is not treated; only the gradient part, which is what (Q-INV) and (O2) ask.
- The Bessel form of u_d is recalled, and used for the GUIDE numbers only. The signs use (C1), (C2) alone.

### Step 8 (done 2026-11-16T04:56:21Z): verdicts

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit bed8e5de3, one session, no
subagents. One GUIDE job under the numeric lock (4.5; it evaluates two series and proves nothing). Checked by: nobody.
A same-provider check and a cross-provider check are both open. Only this file was written.

| Item | Statement | Mark |
|---|---|---|
| GR (4.1) | a boundary gradient (d lambda) n is a gauge move plus the pin move W_l = exp(- eps lambda n_tail) exp(eps lambda Ad(omega_l) n_head); formulas for Psi, Q(d lambda), H_c | PROVED |
| CUBE-Z (4.2) | cube with lower face pinned: Z_c = e^(b_0 t(h)) sum_d d u_d^5 chi_d(h); xbar, kappa > 0 | PROVED (Bessel form of u_d RECALLED, GUIDE only) |
| CUBE (4.3) | trivial pin: Q(d lambda) = beta xbar (delta_1^2 + delta_2^2) + b_0 (delta_1 - delta_2)^2; H_c = (b_0 + kappa)(delta_1 - delta_2)^2; Var = difference | PROVED |
| Cube, covariant frame (4.4) | the only covariant pin frame is the plaquette axis, D n = 0, all values 0 | PROVED |
| TP (5.1) | box, trivial pin: Q(d lambda) = sum_p beta_p w_p xbar_p (sum [p : l] b_l)^2 | PROVED |
| TP4 (5.2) | lane's cell: Q(d lambda) = beta [sum (1 + xbar_i) delta_i^2 + (1/2) sum (delta_i - delta_j)^2] > 0 | PROVED |
| OPEN-SET (5.3) | covariant plaquette-axis frame: Q(d lambda) > 0 on an open set of pins | PROVED |
| SIGN (5.4) | one link: Q(d lambda) = 2 e_l (1 - cos alpha) + 2 sin(alpha) nu . E[N_l]; both signs where E[N_l] != 0 | PROVED |
| (Q-INV) (5.5) | Q invariant under boundary gradients | FAILS (true iff the move is pure gauge in the cases computed; always true for U(1)) |
| H4 (6.1) | lane's cell, beta <= 3: H_c(omega; (d lambda) n) > 0 at the trivial pin (one delta_i) and on an open set of pins (axis frame) | PROVED |
| MASS (6.2) | abs Q(d lambda) <= 60 b sum lambda_head^2 abs(D_l n) in 4D (finer form in the text) | PROVED |
| (O2) (6.3) | curl inequality on boundary gradients | FAILS for every C; no interior field repairs it where H_c > 0 |
| U(1) (7.1) | every statement passes; zero gain | PROVED |
| Route (ii) at the pinned boundary (7.2) | closed as an exact mechanism; what is left is (N1) of row 1011 | ARGUED from the proved items |
| xbar_i > 0 and Hess F_c(1) >= 0 off gauge directions, 4D cell, all beta | | OPEN |
| A special frame with Q(d lambda) = 0 for all boundary lambda on a positive-measure set of pins | | OPEN (not needed) |
| Typical pins at order-one coupling; upper faces; non-gradient boundary theta | | OPEN (not treated) |

Corrected texts for the lead (no other file was edited).
- `parts/gap.md` L141 and row 1035's corrected text: replace "Whether Q itself is invariant there is open" by "Q is not
  invariant under boundary gradients: Q(d lambda) is the cost of the pin move - lambda D n, a mass term, positive at and near
  pure-gauge pins (row 1036 GR, TP4, OPEN-SET; unchecked), and there H_c itself is positive for beta <= 3 (H4)."
- Row 1034's O2: "FAILS on gradients (row 1036 6.3); the true bound is Lemma MASS".
- Row 1011 4.2 "ARGUED only" for homogeneous strength: row 1036 TP4 and H4 prove the trivial-pin case for a
  site-dependent colour (d lambda) n, beta <= 3. Row 1011 4.4's fixed-colour bound H_c(1; a theta) is a different statement and stays OPEN.

RESULT: Row 1036 (Claude Fable 5.2 medium, laptop background agent; written by hand, checked by nobody; one GUIDE run under the numeric lock that proves nothing). (Q-INV) FAILS and (O2) FAILS. PROVED: Theorem GR, a boundary gradient (d lambda) n of a pin-measurable site frame is a gauge move followed by the pin move W_l = exp(- eps lambda n_tail) exp(eps lambda Ad(omega_l) n_head), so Psi = sum lambda (D_l n) . N_l, Q(d lambda) = - E[second derivative of the action along that pin curve] and H_c = second derivative of F_c along it; it is pure gauge exactly when D n = 0 (always for compact U(1): zero gain, the classical constant beta). Values: on the cube with its lower face pinned, trivial pin, Q(d lambda) = beta xbar (|delta_1|^2 + |delta_2|^2) + b_0 |delta_1 - delta_2|^2 and H_c = (b_0 + kappa) |delta_1 - delta_2|^2 with xbar = sum d^2 u_d^4 u_d'/sum d^2 u_d^5 and kappa = sum d^2 (d^2 - 1) u_d^5/(3 sum d^2 u_d^5) from the character expansion (for n_100 = n_010 = i, n_110 = j: Q = 4 beta xbar, GUIDE 5.03 at beta = 2.4; a covariant pin frame on the cube has D n = 0 and all values 0); in the lane's 4D cell at the trivial pin Q(d lambda) = beta [sum_i (1 + xbar_i) |delta_i|^2 + (1/2) sum_(i<j) |delta_i - delta_j|^2] > 0 (Theorem TP for every box), and Q(d lambda) > 0 on an open set of pins for the gauge-covariant plaquette-axis frame of range 1; Theorem H4, for beta <= 3 the response H_c(omega; (d lambda) n) is itself positive there, so no interior field, no solution of Lemma O1 and no field-dependent vector on the links out of the boundary gives a curl bound; Lemma MASS, the true bound |Q(d lambda)| <= 60 b sum over pinned links of lambda_head^2 |D_l n|; Proposition SIGN, at pins where F_c is not stationary Q(d lambda) = 2 e_l (1 - cos alpha) + 2 sin(alpha) nu . E[N_l] takes both signs, so its sign is not a stiffness. Meaning (ARGUED): route (ii) at the pinned boundary is closed as an exact mechanism; the cost of a boundary rotation has a mass term in lambda |D n| that vanishes only on reducible pins, and what is left is the typical-pin smoothness statement (N1) of row 1011. OPEN: xbar_i > 0 and positivity of the Hessian of F_c at the trivial pin in the 4D cell for all beta, typical pins at order-one coupling, upper faces, non-gradient boundary fields, and any check of this file.
