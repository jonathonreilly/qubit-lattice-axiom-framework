lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T02:37Z

# gap-k2-end-class-fable (row 1471): the end class (END-K2) with numbers

Started 2026-11-24T14:37Z (date -u), Mac mini worker 1, Claude Fable 5.2 medium, pinned at bf0e5e0ec.
Status of this file: IN PROGRESS. Nothing below is checked by a second party.

## 0. Plan (written first, per the save protocol)

Item: component C2 of the K-II tool of row 1468 (`library/gap-k2-tool-design-fable.md` sections 3-4, 7).
To prove, with numbers: explicit eps_E > 0 and v_E(m) = O(log m) such that every family realizing a local
rule of norm at most eps_E (weighted norm of 4.2 at x of order one, or a justified variant) on the sixteen
twisted tori of spatial side m and time sides v, 2v, v >= v_E(m), wrap error <= 1/100, has purity >= 457/625.
Also the entry: largest beta_E such that Wilson at beta_E after one Q2 step of stated strength is in the class.

Steps (each appended here before the next starts):
1. Read row 1468 sections 3-4, 7 (statement, norm 4.2, Fact PUR, map Q2). Record exact statements used.
2. Read Theorem E (row 1354), Theorem END-D (row 1353), Theorem BS (row 1340): what they prove, with which
   norm (supremum bounds), and what ports.
3. Compare the weighted norm of 4.2 with the supremum bounds those theorems use; find the first failure or
   show the port goes through.
4. Prove (END-K2) with explicit constants, or repair the norm and prove the repaired statement.
5. Entry: beta_E and the Q2 strength.
6. Count of certified entry steps from beta about 2.3 to beta_E; next two rows with decisive outcomes.

Marks used below: [PROVED] = full argument written here or cited to a row with its location;
[SKETCHED] = argument outlined, a named step not written; [GUESSED] = no argument.

## 1. Step 1: what row 1468 fixes (read: sections 3, 4, 5, 7, 8 of `gap-k2-tool-design-fable.md`)

Read in full: 3.1 (Fact PUR, twisted field spaces F^z), 3.2 (map Q2, Lemma TW), 3.3 (Theorem K2), 4.1-4.5, 5, 7, 8.
Facts used below, with their standing there:

- Purity of a family: P = Z_+(2v)/Z_+(v)^2, Z_+(tau) = (1/8) sum over z in Z_2^3 of the mass Z^z(tau) of the
  density on the torus m^3 x tau with temporal twist z. (3.1, 3.3.)
- Weighted norm (4.2): norm(Phi)_(x,r) = sup_c sum_{X contains c} e^(r size X) sup_V |Phi_X(V)|/(1 + theta x E_X(V)),
  E_X = sum over plaquettes inside X of (1 - Re V_p), theta in (0,1]. Label there: GUESSED adequate.
- "Realizes Phi with site constant e and wrap error eta": on each torus T of shortest side s,
  |log D(V) + e size(T) + sum over X of diameter below s/2 of Phi_X(V)| <= eta for every V. (4.2.)
- In Theorem K2 the end level has m = 512 v (l_N = 512 v_E, v_N = v_E). So the consumer has v = m/512.
- (END-K2) is SKETCHED there, with "Not checked: that the weighted norm at x of order one gives the supremum
  bounds those theorems use". That is the question of Step 3.
- Lemma TW (Q2 is well defined on the twisted tori and keeps each mass) is PROVED BY HAND, UNCHECKED there
  (check row 1469 is queued). I use it in Section 6 only.

Plan of the proof, decided in this step (one approach): a polymer expansion of the sixteen masses in the
supremum norm, with the Kotecky-Preiss criterion in its two-function form (a, d). The weighted norm is first
reduced to a supremum norm at a smaller rate (Step 3). This is the strong-coupling expansion of Osterwalder
and Seiler in abstract form. Twists are invisible to every cluster that does not wrap the time direction.

## 2. Step 2: the three relatives, read (what each proves, in which norm, what ports)

Read at this pin: Theorem E (`gap-mini-nphys-fable.md` L185-240), Theorem END-D (`gap-mini-neutral-step-fable.md`
L268-345), Theorem BS (`gap-blockstep-fable.md` L264-270) and the RESULT text of rows 1340, 1353, 1354.

| Theorem | Class | Norm | Conclusion | Use here |
|---|---|---|---|---|
| E (row 1354) | plaquette weights a_p(alpha_p + beta_p (-1)^(z_p)) with a centre bit split off | L^6 norms under a product reference: norm(alpha_p - 1)_6 <= 1/4096, norm(beta_p)_6 <= 1/40 | eight twisted masses within e^(2 tau); two-period bound | NOT a port. A local rule in SU(2) block links has no split centre bit and no product reference. Its content that I keep: the end class must be of the small-coupling kind (C3), so the twisted masses come out equal. |
| END-D (row 1353) | functions f_W on windows W = link sets of boxes, centre invariance (G), Haar links | supremum norm N_kappa(f) = sup_l sum_{W contains l} e^(kappa size W) sup abs(f_W), size = sites of the box | N_kappa <= kappa/32 gives every Z^e > 0 and abs(2 log Z_+(T) - log Z_+(2T)) <= 4 v e^(-kappa j_0/4), j_0 = min(T, m) - 1 | The nearest relative. Same method (polymers, rooted sums, two-period bookkeeping). It is a supremum-norm theorem. See the two differences below. |
| BS (row 1340) | Wilson datum at one coupling, block Dobrushin condition (B-pin) | chord coupling numbers of a block law | the seed, given (B-pin) | NOT a port for the end. It proves a seed from a mixing hypothesis. It gives no local form of an image density. |

Two places where END-D does not give (END-K2) as stated. Both are bookkeeping, not analysis.

- (D1) Windows against connected sets. END-D indexes by boxes, with size = number of sites of the box. A rule
  of 4.2 is indexed by connected bond sets X. The bounding box of a connected set of n bonds can have of
  order (n/4)^4 sites. So a rule that is small in e^(r size X), size X = number of bonds, is not small in
  e^(kappa size W). If "size(X)" in 4.2 is read as the number of bonds (4.2 does not say), END-D cannot be
  quoted. Theorem END-K2 below is proved for connected sets with size = number of bonds. If size is read as
  the sites of the bounding box, both theorems apply (bonds of X <= 4 sites of the box).
- (D2) The remainder. END-D's remainder is 4 v e^(-kappa j_0/4) with j_0 = min(T, m) - 1. At the consumer's
  shape (time side v = m/512) this is the same kind of bound as below. END-D states the two-period bound for
  Z_+ only; the purity needs exactly that, so END-D's conclusion is already the purity bound
  P >= exp(-4 v e^(-kappa j_0/4)) for its class. [PROVED there, unchecked at this pin.]

So I do not redo END-D. I prove the statement for the class of 4.2 by the Kotecky-Preiss theorem, which gives
the constants in a few lines, and I record END-D as the window form.

Search (rule 0a). `grep END-K2` in FINISH.md: one hit, my own queue row 1471. In `library/open-core.md`: no hit.
In `library/` and `parts/`: only row 1468's file and this file. Strong-coupling relatives on file: Theorem 1 and
Theorem 3 of `gap-seed-sc.md` (row 701: the seed for the Wilson weight at beta below 1/12800), Theorem DOB (row
785), Lemma END-RAY (row 1340), END-D, Theorem E. None is stated for a local rule in a weighted norm. So the
statement below is new on file as a statement; its method is standard and is not new.

## 3. Step 3: the weighted norm gives the supremum bounds, with an explicit loss [PROVED]

Convention. size(X) = abs(X) = the number of bonds of X. The diameter of X is its largest coordinate extent,
so diam(X) <= abs(X) for a connected X. w_X = sup over V of abs(Phi_X(V))/(1 + theta x E_X(V)).

**Lemma W.** For every X and V: abs(Phi_X(V)) <= w_X (1 + 3 theta x abs(X)). Hence for 0 < q < r,

    sup_c sum_{X contains c} e^(q abs(X)) sup_V abs(Phi_X(V)) <= M norm(Phi)_(x,r),
    M = M(theta x, r - q) = sup over n >= 1 of (1 + 3 theta x n) e^(-(r - q) n) <= 1 + 3 theta x/(e (r - q)).

Proof. 1 - Re V_p lies in [0, 2]. A plaquette inside X has its four bonds in X, and a bond lies in six
plaquettes. So X holds at most 6 abs(X)/4 plaquettes and E_X <= 3 abs(X). The second line follows term by
term. For the last bound, n e^(-s n) <= 1/(e s). QED

Answer to the question of row 1468 4.3 ("Not checked: that the weighted norm at x of order one gives the
supremum bounds"): it does. The weight costs a factor 1 + 3 theta x abs(X), which a part r - q of the decay
rate pays. There is no failure and no repair of the norm is needed for the end. The loss is the factor M, of
order theta x / (r - q). So eps_E is of order 1/(theta x): the end class shrinks as x grows, as it must,
because a rule of weighted norm eps may equal eps theta x times the Wilson action.

Remark (the weighted class is not a small-coupling class at large x). Phi = -c sum_p (Re V_p - 1) has
w_p = sup of c (1 - Re V_p)/(1 + theta x (1 - Re V_p)) = 2c/(1 + 2 theta x), so its weighted norm is about
6 e^(4r) c/(theta x). A Wilson rule of coupling c of order eps theta x is inside the ball of radius eps. So
(END-K2) can hold only with eps_E theta x below the hand range of the Wilson weight. This is why the
statement says "x of order one".

## 4. Step 4: the expansion lemma, and Theorem END-K2 with numbers

### 4.1 Lemma KP-F (polymer expansion for function-valued elements) [PROVED given the Kotecky-Preiss theorem]

Setting. A finite set L of links, each with a variable in SU(2) and Haar measure (product measure). A finite
set of elements E. Each E has a support supp(E), a nonempty subset of L, and a bounded measurable function f_E
of the variables on supp(E), with sup abs(f_E) <= phi_E. Two elements touch if their supports meet. Put

    Xi = integral of prod over E of (1 + f_E).

A polymer is a set S of elements that is connected under touching; supp(S) is the union of the supports;
rho(S) = integral of prod_{E in S} f_E. Two polymers are compatible if their supports are disjoint. A cluster
C is a finite family of polymers, with multiplicities, whose incompatibility graph is connected; Phi(C) is
its Ursell coefficient times the product of the activities.

**Lemma KP-F.** Let a(E) > 0 and d(E) >= 0 be numbers such that for every element E

    (CR)   sum over E' that touch E (E' = E included) of phi_E' e^(2 a(E') + d(E')) <= a(E).

Then Xi > 0, log Xi = sum over clusters of Phi(C) with absolute convergence, and for every element E_0

    sum over clusters C that hold an element touching E_0 of abs(Phi(C)) e^(d(C)) <= a(E_0),

where d(C) is the sum of d(E) over the elements of the polymers of C, with multiplicity. If moreover
sum over E' with l in supp(E') of phi_E' e^(2 a(E') + d(E')) <= a_0 for a link l, then the sum of
abs(Phi(C)) e^(d(C)) over the clusters whose support contains l is at most a_0.

Proof. (i) Expand the product over subsets of elements and split each subset into its connected components.
Components have disjoint supports and the measure is a product, so the integral factors:
Xi = sum over families of pairwise compatible polymers of prod rho(S). Also abs(rho(S)) <= prod_{E in S} phi_E.

(ii) Rooted sums. Put psi_E = phi_E e^(a(E) + d(E)) and, for an element E_0,
T(E_0) = sum over polymers S containing E_0 of prod over E in S, E not E_0, of psi_E. Claim: T(E_0) <= e^(a(E_0)).
Induction on the largest number N of elements allowed in S. For N = 1 the sum is 1. Remove E_0 from S. The
rest splits into components S_1, ..., S_k, each a polymer with at most N - 1 elements, each holding an element
E_i that touches E_0. So T_N(E_0) <= sum_k (1/k!) (sum over E' touching E_0 of psi_E' T_(N-1)(E'))^k
<= exp(sum over E' touching E_0 of psi_E' e^(a(E'))) <= e^(a(E_0)) by (CR).

(iii) The criterion. Put a(S) = sum of a(E) and d(S) = sum of d(E) over E in S. A polymer S' incompatible
with S holds an element E' that touches (or equals) an element E of S. So

    sum over S' incompatible with S of abs(rho(S')) e^(a(S') + d(S'))
      <= sum_{E in S} sum over E' touching E of psi_E' T(E') <= sum_{E in S} sum_{E'} phi_E' e^(2a(E') + d(E')) <= a(S).

This is the hypothesis of the theorem of Kotecky and Preiss (Comm. Math. Phys. 103 (1986) 491: abstract
polymers, a reflexive symmetric incompatibility relation, two functions a and d; cited, a published theorem,
not re-derived here; the deletion induction of END-D Steps 2-3 on file is a proof of the same kind). Its
conclusion is: log Xi = sum of Phi(C), and for every polymer S the sum of abs(Phi(C)) e^(d(C)) over the clusters
incompatible with S is at most a(S). Take S = {E_0}. For a link l, add to the polymer set a ghost polymer
with support {l}, activity 0 and a = a_0. The hypothesis for the ghost is the last displayed condition; the
hypotheses of the true polymers do not change. QED

### 4.2 Twisted tori and local rules [PROVED]

Hypotheses on a rule in this section. Phi = (Phi_X), X the finite connected sets of bonds of Z^4. Each Phi_X
is a bounded measurable function of the field on X, with
(T) covariance under the translations of Z^4, and
(G) invariance under centre gauge maps: Phi_X does not change when each V(b), b in X, is multiplied by
sigma at its two ends, for a function sigma from the sites of X to {1, -1}.
A rule of 4.2 of row 1468 (continuous, gauge invariant, covariant under the hypercubic group) satisfies both.
Reflections and rotations are not used. This matters in Section 6: the image of a Q2 step with corner bases
is covariant under translations and axis permutations, not under reflections.

Let T be the torus (Z/m)^3 x (Z/tau) with twist z, m >= 4, tau >= 4, s = min(m, tau). Fields are the elements
of F^z(m, tau) (row 1468 3.1): W on the cylinder (Z/m)^3 x Z with W(x + tau e_0, mu) = (C_z W)(x, mu).

(a) A connected X of Z^4 of diameter below s/2 projects injectively to the cylinder. Phi_X is evaluated on
the cylinder through this projection. The value is the same for X and for X + tau e_0: by (T) it is
Phi_X evaluated at C_z W, and on a set of spatial extent below m/2 the map C_z is a centre gauge map (for
each i with z_i = 1 put sigma = -1 on the sites of X on one side of the cut between x_i = 0 and x_i = 1,
which the extent of X crosses at most once). By (G) the value is unchanged. So sum_X Phi_X is a function on
F^z(m, tau), and the definition "realizes" of row 1468 4.2 has a meaning on the twisted tori.

(b) Under Haar measure on one period, the variables on any set of cylinder bonds that are distinct modulo
tau e_0 are independent Haar variables: each is a fixed sign times a variable of the period, and Haar
measure is invariant under V -> -V.

(c) Elements on T: the projections of the X of diameter below s/2, with f_X = e^(-Phi_X) - 1. By (b), Lemma
KP-F applies on T with L the bonds of T. If supp(S) of a polymer S does not wrap the time circle, then
rho(S) is the integral of prod f_X over independent Haar variables on a lift of supp(S) to the cylinder. It
does not depend on z, and it is the same on the tori of time sides v and 2v.

### 4.3 Theorem END-K2 [PROVED given Lemma KP-F; by hand, unchecked]

**Theorem END-K2.** Let x > 0, theta in (0, 1], r > 0. Choose alpha > 0 and t > 0 with q = r - 2 alpha - t > 0. Put

    M = sup over n >= 1 of (1 + 3 theta x n) e^(-q n)   (M <= 1 + 3 theta x/(e q)),
    eps_E = alpha e^(-alpha) / M.

Let m >= 4 and v >= 4. Let a family of sixteen positive densities, on the tori (Z/m)^3 x (Z/v) and
(Z/m)^3 x (Z/2v) with the eight twists, realize a rule Phi with (T), (G), with one site constant e, with
norm(Phi)_(x,r) <= eps_E and with wrap error eta. Then, with |T_v| = m^3 v:

- (a) for each of the two time sides tau, the eight twisted masses lie within the factor
  exp(2 eta + 8 alpha m^3 tau e^(-t v/2)) of each other;
- (b) log P >= -3 eta - 16 alpha m^3 v e^(-t v/2), P the purity Z_+(2v)/Z_+(v)^2;
- (c) so P >= 457/625 as soon as eta <= 1/100 and

      (E-v)   16 alpha m^3 v e^(-t v/2) <= 0.283     (log(625/457) = 0.31306, minus 3/100).

  (E-v) holds for v >= v_E(m) = (4/t) (3 log m + log(64 alpha/(0.283 e t))), which is O(log m).

With the default alpha = r/8, t = r/2, q = r/4:

    eps_E = (r/8) e^(-r/8) / M(theta x, r/4),   (E-v): 2 r m^3 v e^(-r v/4) <= 0.283,   v_E(m) = (8/r)(3 log m + 3.04).

Proof. Step 1 (supremum bounds). By Lemma W with rate 2 alpha + t: sup abs(Phi_X) <= eps_E M for every X, and
sup_c sum_{X contains c} e^((2 alpha + t) abs(X)) sup abs(Phi_X) <= eps_E M. With phi_X = e^(sup abs Phi_X) - 1
<= sup abs(Phi_X) e^(eps_E M) and eps_E M = alpha e^(-alpha):

    sup_c sum_{X contains c} phi_X e^((2 alpha + t) abs(X)) <= alpha e^(-alpha) e^(alpha e^(-alpha)) <= alpha.

On a torus the X through a bond are a subset of the X of Z^4 through a lift of it. So (CR) holds on each of
the sixteen tori with a(X) = alpha abs(X), d(X) = t abs(X), and a_0 = alpha: an element has abs(X) bonds, and (CR) is the bond-wise bound summed over them.

Step 2 (masses). Xi^z(tau) = integral of exp(-sum_X Phi_X) over one period. By "realizes",
Z^z(tau) = e^(-e m^3 tau) Xi^z(tau) e^(+-eta). By Lemma KP-F, log Xi^z(tau) = sum of Phi^z(C) over the clusters on
the torus. Write norm(C) for the sum of abs(X) over the elements of C with multiplicity; d(C) = t norm(C),
and the support of C is connected with at most norm(C) bonds.

Step 3 (short clusters). Let norm(C) < v/2. Then every element of C has abs(X) < v/2, hence diameter below
v/2. The support of C has time extent below v/2, so no polymer of C wraps the time circle, and by 4.2 (c)
Phi^z(C) does not depend on z. The elements with abs(X) < v/2 are the same on both tori: on each, they are
the X with abs(X) < v/2 and diameter below min(m, v)/2 (if v <= m the second condition follows from the
first; if v > m both tori have s = m). The covering map from the torus of time side 2v to that of time side
v maps the clusters with norm(C) < v/2 two to one, with equal values. So, for all z, z', z'',

    S^z(2v) = 2 S^z'(v),   S^z(tau) = sum over the clusters on the torus of time side tau with norm(C) < v/2 of Phi(C).

Step 4 (long clusters). A cluster contains a bond. By Lemma KP-F with a_0 = alpha, on a torus with 4 m^3 tau bonds,

    sum over C with norm(C) >= v/2 of abs(Phi(C)) <= e^(-t v/2) 4 m^3 tau alpha.

Step 5. For any three twists, abs(log Xi^z(2v) - log Xi^z'(v) - log Xi^z''(v)) <= 4 alpha e^(-t v/2) (2 m^3 v + 2 m^3 v)
= 16 alpha m^3 v e^(-t v/2). Z_+(2v) >= e^(-2 e m^3 v - eta) min_z Xi^z(2v) and Z_+(v)^2 <= e^(-2 e m^3 v + 2 eta) max_z Xi^z(v)^2.
The site constant cancels. This is (b). For (a) use Steps 3 and 4 for two twists at one tau. (c): 3 eta <= 0.03
and 0.31306 - 0.03 > 0.283. For v_E: v e^(-t v/4) <= 4/(e t), so the left side of (E-v) is at most
(64 alpha/(e t)) m^3 e^(-t v/4). With the default, 64 alpha/(0.283 e t) = 16/(0.283 e) = 20.8 and log 20.8 = 3.04. QED

### 4.4 Numbers [hand arithmetic; each line is a product of four-digit values; unchecked]

Default choice alpha = r/8, t = r/2. Worst weight theta = 1. Column "v at m = 512 v" is the least v with (E-v)
at the consumer's shape of Theorem K2 (row 1468 3.3), solved from log(2 r 512^3) + 4 log v - r v/4 <= -1.262.

| r | theta x | M | eps_E | v_E(m), explicit | least v at m = 512 v |
|---|---|---|---|---|---|
| 0.3 | 2.3 | 34.22 (n = 13) | 0.00105 | 26.7 (3 log m + 3.04) | not computed |
| 0.7 | 2.3 | 14.84 (n = 6) | 0.0054 | 11.5 (3 log m + 3.04) | 242 |
| 1 | 2.3 | 10.53 (n = 4) | 0.0104 | 8 (3 log m + 3.04) | 165 |
| 1 | 1 | 4.79 (n = 4) | 0.0230 | 8 (3 log m + 3.04) | 165 |
| 2 | 2.3 | 5.45 (n = 2) | 0.0357 | 4 (3 log m + 3.04) | 78 |
| 4 | 2.3 | 2.91 (n = 1) | 0.104 | 2 (3 log m + 3.04) | 37 |

Worked line (r = 1, theta x = 2.3): (1 + 6.9 n) e^(-n/4) is 10.25, 10.52, 10.17 at n = 3, 4, 5, so M <= 10.53;
alpha e^(-alpha) = 0.125 x 0.8825 = 0.11031; eps_E = 0.11031/10.53 = 0.01047. (E-v) at m = 512 v:
log(2 x 512^3) = 19.408; at v = 165, 4 log v = 20.424 and v/4 = 41.25, total -1.418 <= -1.262; at v = 164 the
total is -1.193, which fails. So with r = 1 the end level of Theorem K2 may take v_E = 165 (166 if an even
side is wanted), spatial side 84,480.

**The statement of the row, in one line.** For the norm of row 1468 4.2 with r = 1, theta x <= 2.3:
eps_E = 0.0104 and v_E(m) = 24 log m + 25. Every family that realizes a rule (with (T) and (G)) of norm at
most 0.0104 on the sixteen twisted tori of spatial side m and time sides v, 2v, v >= v_E(m), with wrap error
at most 1/100, has purity at least 457/625. [PROVED given Lemma KP-F and the Kotecky-Preiss theorem.]

What is not claimed. The constants are not optimal (the criterion (CR) loses a factor e^(2a), and Lemma W
is a worst case). eps_E is of order r^2/(35 theta x) at small r and at most 1/e at large r. The theorem says
nothing at theta x large against r^2. It is a statement about families, not about Wilson.

## 5. Step 5: the entry. One Q2 step maps the Wilson weight at small beta into the end class

### 5.1 Setting and counts [PROVED: counts by hand from the definition of Q2 in row 1468 3.2]

Fine torus with sides 2m, 2m, 2m, 2 tau and twist z; coarse torus with sides m, m, m, tau; m, tau >= 4. Wilson
density D_beta(W) = exp(beta sum_p Re W_p), Re the real part of the unit quaternion. Image
(Q2_kappa D_beta)(V) = integral of prod_p (1 + f_p(W)) prod_c (1 + g_c(W, V)) dW, with

    f_p = e^(beta Re W_p) - 1,                      abs(f_p) <= e^beta - 1,
    g_c = e^(kappa Re(M_c V(c)^(-1)))/Zc(kappa norm(M_c)) - 1,   abs(g_c) <= e^kappa - 1.

For g_c: Zc(t) = 2 I_1(t)/t = sum_k (t/2)^(2k)/(k! (k+1)!) lies in [1, e^(t^2/8)], and norm(M_c) <= 1. So the
kernel factor is at most e^kappa and at least e^(-kappa - kappa^2/8) >= 1 - (e^kappa - 1).

Elements: the fine plaquettes p (support: 4 links) and the coarse bonds c (support B_c: the fine links on
the 384 contours of c).

- B_c has 72 links, for c = (y, mu): the 32 links of the cube 2y + {0,1}^4 (every cube link lies on an axis
  path from the corner 2y), the 32 links of the cube at y + e_mu, and the 8 links of direction mu between
  the two cubes. The straight parts use these 8 links and 16 cube links.
- A link inside a cube lies in B_c for the 8 coarse bonds at that coarse site. A link between two cubes
  lies in B_c for one c.
- A plaquette touches at most 21 plaquettes (itself included) and at most 15 coarse bonds (one cube: 8; two
  cubes: 8 + 8 - 1; four cubes: 4).
- A coarse bond touches at most 72 x 6 = 432 plaquettes and at most 15 coarse bonds (itself included).
- A link lies in 6 plaquettes and in at most 8 sets B_c.

The coarse set of a cluster. Give each element a connected graph on the coarse lattice: c gives the bond c;
p gives the coarse sites of the cubes of its corners and the coarse bonds between them (a site, a bond, or
the four bonds of a coarse square). If two elements share a fine link, their graphs share a coarse site
(the ends of a link of B_c lie in the cubes of the two ends of c). So for a cluster C with at least one
coarse-bond element, the union X(C) of the bonds is a connected set of coarse bonds that contains every
coarse bond of C, and abs(X(C)) <= (number of c-elements) + 4 (number of p-elements).

### 5.2 Theorem EN (entry) [PROVED given Lemma KP-F and Lemma TW of row 1468; by hand, unchecked]

**Theorem EN.** Let beta, kappa > 0, r > 0, lambda >= 1, a_p > 0, a_c > 0. Put
A = (e^beta - 1) e^(2 a_p + 4 r), B = lambda (e^kappa - 1) e^(2 a_c + r), a_0 = 6A + 8B. Assume

    (CR-EN)    21 A + 15 B <= a_p,      432 A + 15 B <= a_c.

Then there are a rule Phi on the coarse lattice with (T) and (G), invariant under all gauge maps and
continuous, and a constant e, both independent of m, tau and z, such that

    sup_c sum_{X contains c} e^(r abs(X)) sup_V abs(Phi_X(V)) <= a_c/lambda,

and for all m, tau >= 4 and every twist z the density Q2_kappa D_beta on F^z(m, tau) satisfies, with s = min(m, tau),

    abs( log(Q2_kappa D_beta)(V) + e m^3 tau + sum over X of diameter below s/2 of Phi_X(V) )
        <= eta(m, tau) = 8 m^3 tau (a_c/lambda) e^(-r s/2) + 128 m^3 tau a_0 e^(-8 r s).

So the family of the sixteen images realizes Phi with site constant e and wrap error max eta. Since the
weighted norm is at most the supremum norm, norm(Phi)_(x,r) <= a_c/lambda for every x and theta.

Proof. Fix V. Use Lemma KP-F with a(p) = a_p, a(c) = a_c, d(p) = 4r, d(c) = r + log lambda. By the counts of 5.1,
(CR) for a plaquette is the first inequality of (CR-EN) and (CR) for a coarse bond is the second; the link
bound is a_0. By Lemma TW the kernel is a function on the twisted tori, and 4.2 (b) gives the product measure.
So log(Q2 D)(V) is the sum of Phi(C; V) over the clusters on the fine torus, and

    (i)  for each coarse bond c_0: sum over clusters that touch c_0 of abs(Phi(C; V)) e^(d(C)) <= a_c;
    (ii) for each fine link l: sum over clusters through l of abs(Phi(C; V)) e^(d(C)) <= a_0.

For a cluster with at least one c-element, e^(d(C)) >= lambda e^(r abs(X(C))). For a cluster of n plaquettes
only, d(C) = 4 r n, and Phi(C) does not depend on V.

The rule. On Z^4 (the bounds hold in every finite box with the same constants, and a cluster has the same
value in every box that holds it) put Phi_X(V) = - sum over the clusters C with at least one c-element and
X(C) = X of Phi(C; V). A cluster with c_0 in X(C) holds c_0 or a plaquette with a link between the two
cubes of c_0, which is a link of B_(c_0); so it touches c_0. By (i) the norm bound holds. Phi_X depends on
V on X only, is continuous (uniform limit), and is covariant under coarse translations. It is gauge
invariant: for a coarse gauge map h take the fine gauge map g with g(2y) = h(y) and g = 1 elsewhere. Then
M_c(W^g) V^h(c)^(-1) is conjugate to M_c(W) V(c)^(-1), the plaquette functions are invariant, and W -> W^g
keeps the Haar measure on the support of each polymer. The constant: e = - 16 k, k the sum of Phi(C) over
the plaquette-only clusters of Z^4 whose first site (in a fixed order) is the origin.

The torus. (1) Clusters with a c-element and abs(X(C)) < s/2 do not wrap (the support lies over the sites
of X(C)). They are the projections of the clusters of Z^4 with the same coarse set, with equal values (on a
twisted torus by the joint centre gauge invariance of the plaquette functions and of Re(M_c V(c)^(-1)), as
in 4.2 (a)). Their sum is - sum over X with abs(X) < s/2 of Phi_X(V). (2) The X of diameter below s/2 with
abs(X) >= s/2 contribute at most 4 m^3 tau (a_c/lambda) e^(-r s/2) to the rule's sum. (3) Clusters with a
c-element and abs(X(C)) >= s/2: at most 4 m^3 tau (a_c/lambda) e^(-r s/2), by (i) summed over the coarse bonds.
(4) Plaquette-only clusters with n < 2s plaquettes do not wrap the fine torus of shortest side 2s; they sum
to 16 m^3 tau k_(<2s), and abs(k - k_(<2s)) 16 m^3 tau <= 64 m^3 tau a_0 e^(-8 r s) by (ii) (the fine torus has
64 m^3 tau links). (5) Plaquette-only clusters with n >= 2s: at most 64 m^3 tau a_0 e^(-8 r s). QED

**Corollary EN-K2 (the entry into the end class).** Fix theta x and r, and let eps_E, alpha, t be as in Theorem
END-K2. If (CR-EN) holds with a_c/lambda <= eps_E, then for all m >= v >= 4 with (E-v) and eta(m, v), eta(m, 2v) <= 1/100,
the Q2_kappa images of the Wilson weights at beta on the sixteen fine tori (sides 2m, time sides 2v and 4v)
have purity at least 457/625. By Lemma TW the fine Wilson masses equal the image masses. So the Wilson
transfer operator at beta on the spatial torus of side 2m has s(2v) <= 4/21 in the sense of Fact PUR, with
u = 2v. With the default (alpha, t) and (E-v): eta <= (2.27/r) e^(-r v/4) (a_c/lambda + 16 a_0), far below 1/100.

Proof. Theorems EN and END-K2. For eta: 16 m^3 v e^(-r v/2) = (8/r) e^(-r v/4) (2 r m^3 v e^(-r v/4)) <= (2.27/r) e^(-r v/4). QED

Remark (what the corollary is). It is a strong-coupling theorem for Wilson, reached through one block step.
It is weaker in range than the hand results on file for the seed (Dobrushin-type, beta below 2/9) and of
the kind of Theorem 3 of `gap-seed-sc.md` (beta below 1/12800). Its use is the form: the image is in a
class that names no torus, and the end theorem is read on the class.

### 5.3 The numbers: beta_E for three strengths [hand arithmetic, unchecked]

Worst weight theta x = 2.3 (theta = 1, x = 2.3). eps_E from the table of 4.4. In each row a_c/lambda = eps_E.

| Entry | r | eps_E | beta_E | kappa | a_p, a_c, lambda | 21A + 15B <= a_p | 432A + 15B <= a_c |
|---|---|---|---|---|---|---|---|
| E1, strength ratio 1 | 0.7 | 0.0054 | 1/40000 = 2.5e-5 | beta | 0.2622, 0.5, 92.59 | 0.01459 + 0.19006 = 0.2047 | 0.30005 + 0.19006 = 0.4901 |
| E3, ratio 0.09 | 0.3 | 0.00105 | 1e-4 | 9e-6 | 0.2622, 0.5, 476.2 | 0.01178 + 0.23589 = 0.2477 | 0.24233 + 0.23589 = 0.4782 |
| E2, ratio 1.5e-12 | 0.3 | 0.00105 | 0.002 | 3e-15 | 0.5, 9.5, 9047.6 | 0.37943 + 0.09809 = 0.4775 | 7.8054 + 0.09809 = 7.9035 |

Worked line E1: e^beta - 1 <= 2.50003e-5; e^(2 a_p + 4r) = e^3.3244 = 27.782, A = 6.9456e-4; e^(2 a_c + r) = e^1.7 =
5.47395, B = 92.59 x 2.50003e-5 x 5.47395 = 0.012671; a_0 = 6A + 8B = 0.1055. At the consumer's shape m = 512 v the
least v with (E-v) at r = 0.7 is 242 (4.4), and there eta is below e^(-40).

**beta_E.** With the strength of the design (kappa = beta, ratio a = 1): beta_E = 1/40000, with r = 0.7 and
eps_E = 0.0054. With a free strength: (CR-EN) needs 21 (e^beta - 1) e^(2 a_p + 4r) < a_p, so the method stops at
e^beta - 1 < e^(-4r)/(42 e), beta_E < 0.0087 for every strength and every r. E2 reaches 0.002 with a strength of
3e-15. A strength far below beta is allowed by the chain (Lemma TW keeps the masses at every strength), and at
the last step the returned coupling is tiny, so the requirement "kappa at least of order x'" of row 1468
3.2 does not forbid it. But it shows what the entry is: at strength 0 the image is a constant, and "the
constant is the same per site on all sixteen tori" is the purity statement itself. The step moves no
difficulty; it only changes the form.

Where the constants are lost (the first three places to improve, in order of size): the count 432 with
d(p) = 4r for every plaquette (a typed count by the number of cubes of a plaquette would give 0, r or 4r);
the 72-link support of a coarse bond, which costs e^(2 a_c); the factor e^(2a) of (CR). A character
expansion of the plaquette factor (Osterwalder and Seiler) would replace e^beta - 1 by about beta/4 on closed
surfaces. None of these moves beta_E to order one. GUIDE: I expect at most a factor 100.

Tube version [SKETCHED]. The same proof handles a fine rule Psi in place of the Wilson weight, with elements
the sets of Psi and the coarse bonds: the image of a connected fine bond set under the cube map is a
connected coarse graph with no more bonds, so d(X) = r abs(X) serves. With a(E) = alpha_f abs(supp E) the
criterion is sup_l [sum_{X contains l} (e^(sup abs Psi_X) - 1) e^((2 alpha_f + r) abs(X)) + 8 lambda (e^kappa - 1) e^(144 alpha_f + r)] <= alpha_f
and the image norm is at most 72 alpha_f/lambda. Not written out; the constants are about 40 times worse than
the typed count of Theorem EN. This is the form a chain needs, since after a certified step the density is
not a Wilson weight.
