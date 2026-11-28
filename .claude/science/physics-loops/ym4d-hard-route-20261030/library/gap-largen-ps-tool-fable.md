lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 17:55:37 UTC 2026. Author only, checked by no one.

# Planar stability (PS) certificate tool (FINISH row 1716)

## 0. Plan (written first; sections are filled in as the work proceeds)

1. Read row 1708 sections 6 and 7. Fix the planar equation, the norm and the statement (PS).
2. Specify the certificate: loop set, truncation rule, arithmetic, approximate inverse, inequalities.
3. Tail lemma: prove it or reduce it to one precise lemma.
4. First exact instance at small beta; compare with the strong-coupling expansion.
5. Cost at order-one beta; what Lean must check.
6. The U(N) twin.
7. RESULT line.

Sources read: the brief (items/gap-largen-ps-tool-fable.item); row 1708, library/gap-largen-build-fable.md, sections 1 to 10 in full; GOAL.md, "Computation only as a formal proof". No web. No other lane file was read. Scripts are in /private/tmp/claude-501/largen-ps-tool/ (twin.py, twin_odd.py, series4d.py, count.py), outside the repository. All runs are python3 -I with fractions; every number below that is called exact is a rational.

## 1. Verdict first

The tool is built as a specification and as one proved theorem (Theorem C). It does not prove (PS) at an order-one beta in 4D. It cannot do so in its present form, for a reason that is now exact:

1. Theorem C (PROVED). A finite head computation, an enclosure of the master field on finitely many loops (EN), and one tail statement (TL) together prove (PS) with an explicit kappa. This is the certificate.
2. The tail statement (TL) in its row-sum form holds only for 6 beta a^4 < 1 (PROVED lower bound on the tail row sum, section 4.1). So the simplest tail closes only inside the contraction window.
3. The one-plaquette twin of (PS) is solved exactly (section 4.2, PROVED, with exact checks). In its strong phase (beta < 1) (PS) holds exactly when a^4 < 1/beta + sqrt(1/beta^2 - 1); the row-sum certificate proves all of that range, and it passed at beta = 9/10. In its weak phase (beta > 1) (PS) is FALSE for every a > 1: the linearised planar equation has a nonzero solution delta_k = sum_{n<k} (-1)^(k-1-n) P_n(1 - 2/beta) with |delta_k| <= k. It is the direction "move a small fraction of the eigenvalues to the top of the potential, theta = pi". The loop equation is a first-variation equation. It does not see that this direction is unstable.
4. Consequence (ARGUED). A tail lemma that proves (PS) in 4D on the weak side must use a structure that the twin does not have, or (PS) must be restated on a smaller class of perturbations. I GUESS that (PS) as stated is also false in 4D on the weak side (section 4.3). Reflection positivity in the tail alone does not repair this: the twin's bad direction is a real, bounded, exact solution of the linear equation, so it is a defect of the statement and not of the truncation.
5. First 4D instance (exact): the planar equation, solved as a power series in u = beta/2 by its own recursion, gives W(plaquette) = u + 4 u^5 + O(u^6) in d = 4, u + 2 u^5 in d = 3, and u in d = 2 through u^7, with three different link-selection rules giving the same series in d = 4. This checks the row generator of the certificate (signs, splits, staples) against the strong-coupling expansion. It certifies no stability statement.

Open inputs by name: (TL) in 4D at any beta; (EN) at any order-one beta; a correct replacement of (PS) on the weak side.

## 2. The object, in the form the certificate uses

Notation of row 1708. u = beta/2. A loop is a closed word; delta is a bounded function on loops with delta(empty) = 0. For a loop l and a link e of l, the linearised planar operator at a field W with W(p) = W(p^-1) is

  (DF^e(W) delta)(l) = (1/n_e) [ - sum_{x != y} eps_x eps_y ( W(l_1) delta(l_2) + delta(l_1) W(l_2) )
                                 + u sum_x eps_x sum_p ( delta(l (-)_x p) - delta(l (+)_x p) )
                                 + u t_e W(l) sum_p ( delta(p) - delta(p^-1) ) ].

(PS)(beta; m, a, kappa): ||delta||_{m,a} <= kappa sup_{l,e} |delta(l) - DF^e(W_beta) delta (l)| e^(-m r(l)) a^(-|l|), with ||delta||_{m,a} = sup_l |delta(l)| e^(-m r(l)) a^(-|l|), m >= 0, a >= 1.

**Lemma S (selection). PROVED.** Let e(l) be any rule that picks one link of each loop. Put A(l, l') for the matrix of delta -> DF^{e(l)}(W_beta) delta, and L = 1 - A. If ||delta||_{m,a} <= kappa ||L delta||_{m,a} for all bounded delta, then (PS)(beta; m, a, kappa) holds.
Proof. The right side of (PS) is a supremum over all pairs (l, e). It is at least the supremum over the pairs (l, e(l)). QED.
So the system is over-determined and the certificate may choose the rows. Each row of A has at most 12 n_e + 2 n_e (n_e - 1) + 12 nonzero entries. The entries of the deformation term are +-u/n_e and do not contain W. The entries of the split term are values W_beta(l_1). The entries of the last term are +-u t_e W_beta(l)/n_e in the 12 columns p, p^-1.

**Lemma K (weighted row sums). PROVED.** Let omega be a positive weight on loops and ||delta||_omega = sup |delta(l)|/omega(l). For a matrix K with finite rows put |K|_omega = sup_l sum_{l'} |K(l,l')| omega(l')/omega(l). Then ||K delta||_omega <= |K|_omega ||delta||_omega. For omega(l) = e^(m r(l)) a^|l|: omega(l')/omega(l) <= nu(l,l') := e^(m D(l';l)) a^(|l'|-|l|), where D(l';l) is the largest distance from a site of l' to the site set of l (because r(l') <= r(l) + D(l';l)). nu does not change when l and l' are translated together. So if K commutes with translations, |K|_omega <= sup over translation classes of l of sum_{l'} |K(l,l')| nu(l,l').
Proof. Direct. QED.
Lemma K is how the weight e^(m r) is handled: the certificate never uses the position of a loop, only rows modulo translation, with the factor e^(m D) on each entry. The rows also commute with the 384 lattice symmetries when the rule e(l) does, so one row per symmetry class is checked.

## 3. The certificate. Theorem C

**Theorem C. PROVED.** Let the loops be split into a head H and a tail T. Let M be a matrix on H and N a matrix on T, both with finite rows (N = 1 is allowed). Put, with the weighted absolute row sums of Lemma K,

  eps_H = sup_{l in H} [ sum_{l' in H} |(1 - M L_HH)(l,l')| omega(l')/omega(l) + sum_{l' in T} |(M L_HT)(l,l')| omega(l')/omega(l) ],
  eps_T = sup_{l in T} [ sum_{l' in T} |(1 - N L_TT)(l,l')| omega(l')/omega(l) + sum_{l' in H} |(N L_TH)(l,l')| omega(l')/omega(l) ],
  theta = max(eps_H, eps_T),   mu = max(|M|_omega, |N|_omega).

If theta < 1 and mu is finite, then every delta with ||delta||_omega finite has ||delta||_omega <= (mu/(1 - theta)) ||L delta||_omega. With omega = e^(m r) a^|l| and Lemma S this is (PS)(beta; m, a, mu/(1-theta)).
Proof. Let Ahat = M (+) N. Then 1 - Ahat L has the block rows (1 - M L_HH, - M L_HT) and (- N L_TH, 1 - N L_TT), so |1 - Ahat L|_omega = theta. Write delta = (1 - Ahat L) delta + Ahat (L delta) and use Lemma K twice: ||delta|| <= theta ||delta|| + mu ||L delta||. ||delta|| is finite, so it can be moved to the left. QED.

A variant for a tail lemma that gives only a norm (PROVED the same way): if ||delta_T|| <= kappa_T ||(L delta_T)_T|| for every delta_T supported in T, and theta' = |1 - M L_HH| + |M L_HT| kappa_T |L_TH| < 1, then (PS) holds with kappa_H = (|M| + |M L_HT| kappa_T)/(1 - theta') and kappa = max(kappa_H, kappa_T (1 + |L_TH| kappa_H)). This form is weaker, because it multiplies the two couplings. In the twin at beta = 9/10 it fails (theta' about 3.6) where Theorem C passes.

### 3.1 The certificate, item by item

A certificate for (PS)(beta; m, a, kappa) is the following finite data, all rational.

1. beta, e^m (a rational upper bound E >= e^m is enough; only E enters), a >= 1.
2. The head: H = all loops of length at most Lambda. The truncation rule is by length only. The rows are listed modulo translation and lattice symmetry. The selection rule e(l) is a fixed computable function that commutes with the symmetries (for example: the first link, in a canonical form of the word, among the links of least n_e).
3. The enclosure table (EN): for each loop l' in a finite list, rationals lo(l') <= W_beta(l') <= hi(l'). The list holds every split piece of every head row and every head loop that has t_e != 0 at its selected link. For every other loop only |W_beta| <= 1 is used.
4. The approximate inverse M: a translation-covariant matrix on H with finite rows and rational entries. In practice M = q(A~_HH) for a polynomial q with rational coefficients, where A~ uses the midpoints of the enclosures. M is found by floats; this does not matter, because only the check below is trusted.
5. The checks. (a) eps_H < 1, where each entry of 1 - M L_HH and of M L_HT is bounded above in absolute value by interval arithmetic over the table (the entries are polynomials in the table values; with rational endpoints no rounding occurs), and each entry carries the factor E^(D(l';l)) a^(|l'|-|l|). (b) |M|_omega <= mu. Both are finitely many rational inequalities, one per row class.
6. The tail input (TL): a matrix N on T with eps_T < 1 and |N|_omega <= mu. This is not a finite computation. It is the tail lemma.

What a passing certificate proves: (EN) and (TL) and checks 5(a), 5(b) imply (PS)(beta; m, a, mu/(1 - theta)), by Theorem C, Lemma S and Lemma K. PROVED as an implication.

### 3.2 Where Newton-Kantorovich is, and where it is not

(PS) is a linear statement at W_beta. For a linear statement the Newton-Kantorovich inequality is the Neumann condition theta < 1 of Theorem C. The nonlinear part of a Newton-Kantorovich proof would give the existence of W_beta near an approximate W~ and hence the table (EN). In the norm of (PS) this part is not available (PROVED in one line): the split term is the bilinear form B(W,W')(l) = -(1/n_e) sum eps eps W(l_1) W'(l_2), and on the loops p^n (n_e = n, all splits inside the family) its weighted norm is at least n - 1, because |W(l_1) W'(l_2)| is only bounded by a^(|l_1|+|l_2|) = a^|l|. So DF is not Lipschitz on any ball of the space, and no radius inequality can be checked. This is Proposition N of row 1708 again. Also, a solution of the planar equation found by a fixed-point argument is not known to be the limit of Wilson states.
So the table (EN) must come from another proof. Two sources: at small beta, the convergent expansion with a remainder bound (CITED in kind: Chatterjee, Jafarov; from memory, UNVERIFIED); at order-one beta, two-sided bounds from positivity of the loop matrix together with the loop equations, a semidefinite programme whose dual solution is an exact rational certificate (the loop-equation bootstrap of Anderson-Kruczenski and Kazakov-Zheng; from memory, UNVERIFIED; such bounds hold for every positive solution of the equations, so they enclose every master field). (EN) is the place where reflection positivity can enter as a finite, Lean-checkable computation. I did not build that part.

## 4. The tail

**(TL)(beta; m, a, Lambda; theta_T, mu).** There is a matrix N on T = {|l| > Lambda}, with finite rows, with |N|_omega <= mu and eps_T <= theta_T < 1 (eps_T as in Theorem C).
The simplest case is N = 1: then eps_T is the largest weighted absolute row sum of A over the tail rows.

### 4.1 The row-sum tail closes only in the contraction window. PROVED

Let l be a loop whose selected link e has n_e = 1. The deformation part of the row (l, e) has 12 entries +-u, at the words p^-1 e R and p e R (l = e R, p one of the 6 plaquettes at e). These 12 words are different from each other (p^-1 e R has one letter e, p e R has two; different p give different words), and the row has no split entries because n_e = 1. Each has length |l| + 4 as a word, and r(l') >= r(l). So the weighted absolute row sum is at least 12 u a^4 = 6 beta a^4. With N = 1, (TL) therefore needs 6 beta a^4 < 1, so beta < 1/6. In this window the whole operator is a contraction and the head adds nothing but a better constant.
With N different from 1 this bound does not apply. A general N is as hard as the problem. Section 4.2 proves that no N exists in the twin's weak phase.

### 4.2 The one-plaquette twin, solved. PROVED

The twin (row 1708, section 6): loops are p^k; W_k = lim E tr V^k for one plaquette variable; planar equation W_k = - sum_{j=1}^{k-1} W_j W_{k-j} + u (W_{k-1} - W_{k+1}), W_0 = 1. On even perturbations (delta_{-k} = delta_k) the operator is (L delta)_k = delta_k + 2 sum_{j=1}^{k-1} W_j delta_{k-j} - u (delta_{k-1} - delta_{k+1}), delta_0 = 0. The weight is q^k with q = a^4 >= 1. The master field is W_1 = beta/2, W_k = 0 (k >= 2) for beta <= 1, and W_1 = 1 - 1/(2 beta) for beta >= 1 (Gross-Witten, Wadia; CITED from memory, UNVERIFIED; the planar equation itself is checked exactly in twin.py for the strong phase).

Generating identity (PROVED, formal power series). Put G = sum_{k>=1} W_k z^k, dhat = sum_{k>=1} delta_k z^k, b = 1 + u (1/z - z), S = b + 2G. Then sum_k (L delta)_k z^k = S dhat - u delta_1. The planar equation is G^2 + b G - u (z + W_1) = 0, so S^2 = b^2 + 2 beta (z + W_1), and z^2 S^2 = (beta^2/4) z^4 + beta z^3 + (1 - beta^2/2 + 2 beta W_1) z^2 + beta z + beta^2/4.

Strong phase. (L delta)_k = delta_k + u (delta_{k-1} + delta_{k+1}). The weighted row sum is u (q + 1/q). It is below 1 exactly when 1/g < q < g, g = 1/beta + sqrt(1/beta^2 - 1). So (PS) holds for 1 <= q < g with kappa = 1/(1 - u(q + 1/q)). For q > g it is false: the solution of L delta = 0 from delta_1 = 1 is (lambda_1^k - lambda_2^k)/(lambda_1 - lambda_2) with |lambda_1| = g; cut it at k = K; the residual is in rows K, K+1 and has weighted size at most C (g/q)^K, and ||delta|| >= 1/q. So the row-sum certificate is sharp in the twin's strong phase, up to q = g.

Weak phase. With W_1 = 1 - 1/(2 beta): z^2 S^2 = (beta^2/4) (1 + z)^2 (1 + c z + z^2), c = 4/beta - 2, |c| < 2. So the solution of L delta = 0 is

  dhat = delta_1 z / ( (1 + z) sqrt(1 + c z + z^2) ),   delta_k = delta_1 sum_{n=0}^{k-1} (-1)^(k-1-n) P_n(x),   x = 1 - 2/beta in (-1, 1),

with P_n the Legendre polynomials (1/sqrt(1 - 2xz + z^2) = sum P_n z^n). Because |P_n(x)| <= 1 on [-1,1] (classical), |delta_k| <= k |delta_1|. Cut at k = K: the residual is in rows K and K+1, of weighted size at most u (K+1) q^-K, and ||delta|| >= 1/q. So for every q > 1 no kappa exists: **(PS) is false in the weak phase of the twin for every a > 1 and every m.** (TL) is false there too, for every Lambda, every N and every q > 1 (PROVED): (TL) gives ||delta|| <= (mu/(1 - eps_T)) ||(L delta)_T|| for delta supported in T (write delta = (1 - N L_TT) delta + N (L delta)_T). The shifted sequence delta_k = d_{k-Lambda} (d the solution above, zero for k <= Lambda) has S dhat = u z^Lambda, so its residual is zero in every tail row; cut it at K as before.
The pole at z = -1 is a unit mass at theta = pi: delta_k tends to (-1)^(k-1)/sqrt(2 - c) plus a decaying oscillation (ARGUED from the pole; seen in the exact values below). The effective potential of the weak-phase density has its maximum at theta = pi and zero slope there. So the direction is an unstable stationary direction. For q = 1 the statement "delta is bounded" is seen exactly for k <= 240 and is ARGUED (Abel summation), not proved here.

Odd sector and the last term (PROVED, formal series; checked exactly for k <= 240). On odd perturbations (delta_{-k} = -delta_k) the last term of (SD) adds the column - beta W_k delta_1 for SU(N); for U(N) it is absent and the odd operator is the even one. For SU: S dhat - u delta_1 - beta delta_1 G = 0, so dhat = delta_1 u (1 + 2G)/S = delta_1 u [ 1 - (1 - z)/sqrt(1 + c z + z^2) ], delta_k = - u delta_1 (P_k(x) - P_{k-1}(x)), |delta_k| <= beta |delta_1|. The last term removes the pole at z = -1 but leaves a bounded nonzero solution. So in the twin's weak phase the odd sector fails for SU(N) as well, also at q = 1.

Exact runs (twin.py, twin_odd.py). Core of the weak-phase check:

```
W = [Fr(1), 1 - 1/(2*beta)]
for k in range(1, Kmax): W.append(W[k-1] - (2/beta)*(W[k] + sum(W[j]*W[k-j] for j in range(1, k))))
d = [Fr(0), Fr(1)]
for k in range(1, Kmax): d.append(d[k-1] - (2/beta)*(d[k] + 2*sum(W[j]*d[k-j] for j in range(1, k))))
# then every row k < Kmax is re-evaluated and asserted to be exactly 0
```

Output (floats only print exact rationals):

```
STRONG beta=9/10 q=5/4 K=8
 ||M|| = 20245053937/2388008704 ~ 8.477797
 ||M L_HT|| = 2330603100/2975682721 ~ 0.783216
 theta_T = 369/400  theta = 369/400  pass: True
 kappa <= max(||M||,1)/(1-theta) = 506126348425/4626766864 ~ 109.3909
 q < g(beta): True
WEAK beta=2: max|W_k| (k<=240) = 0.750000 ; max|delta_k| = 1.000000
  predicted |limit| 1/sqrt(2-c) = 0.707107 ; delta_k for k=235..240: 0.68111 -0.68111 0.73299 -0.73299 0.68133 -0.68133
  min |delta_k| over k in [200,240] = 0.678862
WEAK beta=3/2: max|W_k| (k<=240) = 0.666667 ; max|delta_k| = 1.333333
  predicted |limit| 1/sqrt(2-c) = 0.866025 ; delta_k for k=235..240: 0.84223 -0.89561 0.90940 -0.86542 0.82243 -0.83763
  min |delta_k| over k in [200,240] = 0.818559
SU odd, beta=2: delta_k == -(beta/2)(P_k(x)-P_{k-1}(x)), x=1-2/beta, for k<=240: True
   |delta_k| at k=10,40,160,240: 0.24609 0.12537 0.06298 0.05145 ; max over [200,240] = 0.05635
U  odd (= even sector), beta=2: delta_k == sum_{n<k} (-1)^(k-1-n) P_n(x): True
SU odd, beta=3/2: delta_k == -(beta/2)(P_k(x)-P_{k-1}(x)), x=1-2/beta, for k<=240: True
   |delta_k| at k=10,40,160,240: 0.15445 0.03894 0.01446 0.05109 ; max over [200,240] = 0.06907
U  odd (= even sector), beta=3/2: delta_k == sum_{n<k} (-1)^(k-1-n) P_n(x): True
```

The STRONG block is the first complete instance of the certificate: head k <= 8, M the exact rational inverse of L_HH (so the first sum of eps_H is 0), N = 1, eps_H = 0.783..., eps_T = 369/400. It proves the twin's (PS) at beta = 9/10, a^4 = 5/4, with kappa <= 109.4. The direct contraction bound gives kappa = 400/31 = 12.9; the certificate constant is worse because mu uses the full norm of M. The head buys nothing in the twin, because the row-sum bound is already sharp there.

### 4.3 What this says about 4D

(a) PROVED: no argument that is blind to the dimension can prove (TL) or (PS) at a beta where the twin is in its weak phase. In particular "perimeter decay of W_beta plus row sums" cannot, and neither can any argument that uses only the algebraic form of the linearised equation.
(b) GUESSED: (PS) as stated is false in 4D on the weak side. Candidate direction: a small block of the colour space is put in a stationary but unstable configuration of the action (for example all plaquettes equal to -1 in the block, which is a critical point of Re Tr U_p; or a thin Z_2 vortex in the block). To first order in the size of the block this should give a bounded delta with zero residual, as the mass at theta = pi does in the twin. The plaquette spectrum of the 4D master field is expected to have a gap at theta = pi on the weak side (lore, UNVERIFIED), which is the twin's situation. I did not construct this delta in 4D.
(c) ARGUED: the repair is in the statement. The loop equation is the first variation of a free energy, weighted by the state itself, so it is blind where the state has no spectral weight. In the twin the bad delta is a functional that is not continuous on the C*-algebra generated by the master field (it gives weight to the spectral point -1, where the master field has none). A candidate replacement, (PS*): the same inequality, for delta that extend to bounded functionals on that C*-algebra, in the dual norm. In the twin the even kernel is then excluded (ARGUED: it contains the functional f -> f(-1), which is not continuous on the continuous functions on the arc); whether the inequality then holds in the twin with a constant is NOT checked, and the odd SU solution -u(P_k - P_{k-1}) is the moment sequence of an integrable function on the arc, so (PS*) may still fail in the odd sector. Perturbations that leave the spectrum must then be paid for by (LD), at a cost exp(-c N^2 times the fraction moved). This moves work from (PS) to (LD) and to step 2 of Theorem T. It is a proposal, not a result.
(d) The guess of row 1708, "the tail needs reflection positivity", is sharpened: positivity is needed in three places, and the tail is the least of them. It is needed for the table (EN) (section 3.2), for the identification of a computed solution with the limit of Wilson states, and for the class of delta in the statement itself. A sup-norm tail with signs discarded stops at the absolute convergence of the planar expansion in any case.

**The one precise lemma.** With Theorem C the tail is reduced to (TL)(beta; m, a, Lambda; theta_T, mu) of section 4. Status: PROVED false for the twin at every beta > 1 (every Lambda, every N, every a > 1); PROVED true for the twin at beta < 1, a^4 < g, with N = 1; in 4D with N = 1 it needs 6 beta a^4 < 1 (PROVED necessary) and I did not prove it there even in that window (the split rows of non-reduced words need a bound on W_beta on all loops, which is (EN) on an infinite list). In 4D at order-one beta: OPEN, and expected false on the weak side together with (PS).

## 5. First 4D instance: the row generator against the strong-coupling series (exact)

What is computed. The planar equation, with a selection rule, is a recursion for W as a power series in u: the deformation terms carry a factor u, the split pieces are shorter loops at the same order, and W = O(u) on every nonempty reduced loop. So W(l) mod u^(n+1) is computed exactly by memoised recursion. Reduced representatives are used; this is allowed for W itself, which does not change under backtracks. The last term is dropped because the series has W(p) = W(p^-1).

Core of series4d.py (w is a canonical cyclically reduced word in steps +-1..+-d; occ lists the positions and signs of the selected link; padd, pmul are exact polynomial operations):

```
for (x, ex) in occ:
    for (y, ey) in occ:
        if x == y: continue
        a, b = min(x, y), max(x, y)
        if ex == ey: l1 = w[a:b];   l2 = w[b:] + w[:a]        # e A e B -> (eA),(eB)
        else:        l1 = w[a+1:b]; l2 = w[b+1:] + w[:a]      # e A e^-1 B -> (A),(B)
        acc = padd(acc, pmul(W(canon(l1), n), W(canon(l2), n), n), -ex*ey)
for (x, ex) in occ:
    s = w[x]
    for nu in range(1, D+1):
        if nu == abs(s): continue
        for v in (nu, -nu):
            st = canon(w[:x] + (v, s, -v) + w[x+1:])           # staple: the (-) insertion for e, the (+) insertion for e^-1
            lg = canon(w[:x] + (s, v, -s, -v, s) + w[x+1:])    # the other insertion
            acc = padd(acc, [Fr(0)] + padd(list(W(st, n-1)), list(W(lg, n-1)), -1))
return tuple(c/ne for c in acc[:n+1])
```

Output:

```
d=4 rule=first order=5  W(p) coefficients u^0..: ['0', '1', '0', '0', '0', '4']   states=29151 cache=388207
   W(p^2) = ['0', '0', '0', '0', '0', '0']
   W(1x2) = ['0', '0', '1', '0', '0', '0']
   W(bent) = ['0', '0', '1', '0', '1', '0']
   W(figure8 p.q) = ['0', '0', '1', '0', '0', '0']
d=4 rule=minmult order=5  W(p) coefficients u^0..: ['0', '1', '0', '0', '0', '4']   states=17997 cache=199966
   (the four other loops: the same values)
d=4 rule=hash order=5  W(p) coefficients u^0..: ['0', '1', '0', '0', '0', '4']   states=40075 cache=631524
   (the four other loops: the same values)
d=2 rule=minmult order=7  W(p) coefficients u^0..: ['0', '1', '0', '0', '0', '0', '0', '0']   states=1991 cache=6558
d=3 rule=minmult order=5  W(p) coefficients u^0..: ['0', '1', '0', '0', '0', '2']   states=3345 cache=23792
```

Time and memory in d = 4: 19 s and 0.30 GB (minmult), 31 s and 0.50 GB (first), 78 s and 1.11 GB (hash; this run went above the 1 GB limit of the brief and was not repeated).

What it certifies.
- PROVED by exact computation (not Lean-checked, so by the lane rule a "gap: computation specified, not formally checked"): the formal power series solution of the planar equation in d = 4 has W(p) = u + 4 u^5 + O(u^6), W(1x2 rectangle) = u^2 + O(u^6), W(bent pair of plaquettes) = u^2 + u^4 + O(u^6), W(p^2) = O(u^6).
- The coefficient 4 = 2(d - 2) is the number of 3-cubes on a plaquette, and 2 in d = 3, and the 2D value W = u is exact; this agrees with the strong-coupling expansion as I remember it (UNVERIFIED citation). The bent loop's u^4 is the four other faces of its cube.
- Three selection rules give the same series. The system is over-determined, so this is a real test that the generator implements a consistent set of equations (it would fail for a sign error in the staple or split rules).
- It certifies nothing about (PS). A 4D certificate was not run, because (TL) and (EN) are not available in 4D at any beta in this file.

## 6. Cost of a first certificate at an order-one beta, and the Lean part

Loop counts (count.py, exact dynamic programme; cyclically reduced closed words in Z^4, rooted):

```
4 48 rooted words; about 12 classes mod translation and rotation
6 912 ; about 152
8 28944 ; about 3618 ; about 4 mod lattice symmetry and inversion
10 976800 ; about 97680 ; about 127
12 34953120 ; about 2912760 ; about 3792
14 1302548688 ; about 93039192 ; about 121144
16 50125332432 ; about 3132833277 ; about 4079209
```

("about": the rooted count divided by n, and by 768; exact orbit counts were not computed.) The growth is a factor of about 38 per two links. Non-reduced words, which (PS) as stated quantifies over, are more numerous (8^n rooted before closing).

Estimate (GUESSED sizes; the counts are exact):
- Row classes to check: about 3.8e3 at Lambda = 12, 1.2e5 at 14, 4.1e6 at 16, 1.5e8 at 18.
- Entries per row of L: 13 for n_e = 1, more with splits. M cannot be an exact inverse: the inverse of a translation-covariant operator has infinite range. With M = q(A~_HH), q of degree J, a row of 1 - M L has up to 13^(J+1) entries. Lambda = 12, J = 4: about 1.4e9 rational operations. Lambda = 16, J = 6: about 2.5e14.
- Arithmetic size: beta, a, E rational with small denominators; table endpoints with a fixed dyadic denominator 2^-40; entries of q(A~) then have denominators up to 2^(40 J) times powers of the denominators of beta, a, E, so numbers of a few hundred bits. Fixed-denominator interval arithmetic with outward rounding keeps them at 64 to 128 bits at the cost of a bounded loss in theta.
- Which Lambda is needed is not known, because (TL) is not known. If the tail were a row-sum tail, Lambda would not matter (section 4.1). For a real gain the head must reach several correlation lengths; at order-one beta that is Lambda >= 16 at least (GUESSED).
- In the twin, the only passing instance: 8 x 8 rationals, numerators of 11 digits.

What must be Lean-checked for a 4D certificate to count as a proof step:
1. Lemma S, Lemma K, Theorem C: hand proofs, short, formalisable as stated.
2. The row generator: a Lean function from a canonical word to its row, with a proof that it is the definition of DF^e(l). The exact run of section 5 is a test of the Python generator, not this proof.
3. Checks 5(a), 5(b) of section 3.1: rational or interval inequalities, one per row class. At Lambda = 12, J = 4 this is in reach of a compiled evaluator (`native_decide`, trusted base: the Lean compiler and GMP), not of kernel reduction. At Lambda = 16 it is out of reach today.
4. (EN): a separate certificate (dual semidefinite solution, exact LDL^T with rationals), plus the hand proof that the master field is of positive type and solves the loop equations.
5. (TL): a hand proof. Not available.

## 7. The U(N) twin

Structure (PROVED). Let iota be inversion of loops, and let the rule satisfy e(l^-1) = e(l)^-1. W_beta(l^-1) = W_beta(l), so L commutes with iota and splits into an even block and an odd block. On even delta the last term is zero, so the even blocks of SU(N) and U(N) are the same matrix. On odd delta the SU(N) row has the extra entries - 2 u (t_e/n_e) W_beta(l) in the six columns p containing e(l); the U(N) row does not. So the two certificates differ only in the odd block, by a matrix B with (B delta)(l) = beta (t_e/n_e) W_beta(l) sum_{p contains e} delta(p). B is zero on every row whose selected link has zero net current.

How the U(N) certificate would fail where U(N) is Coulomb (ARGUED). The response of the planar state to an odd local source j (a term N^2 sum_p j_p Im tr U_p in the action) solves L delta = (local right side). For U(N) the response contains the exchange of the U(1) photon, of order one after the factor N^2, with a power-law kernel. So the inverse of the odd U(N) block cannot be bounded with a weight e^(m r), m > 0, and in d = 4 not at m = 0 either (the kernel 1/|x|^3 is not summable). In the certificate this shows as follows: the head check 5(a) of the odd block with factor E^D > 1 cannot reach eps_H < 1 for any polynomial M when Lambda is large, and a tail matrix N cannot exist. A finite head does not see a massless pole exactly; it sees eps_H grow toward 1 as Lambda grows at fixed E > 1. For SU(N) the matrix B is the only term that can change this. It has the form "W(l) times the current of l at e times the lattice divergence of the plaquette field delta(p) at e", which is the form of the photon source. I did not compute this in 4D.

What the 0-dimensional twin shows, and its limit (PROVED there, section 4.2). In the one-plaquette model the last term changes the odd kernel from sum (-1)^(k-1-n) P_n (not decaying) to -u (P_k - P_{k-1}) (decaying like k^(-1/2), seen in the exact values). It does not restore (PS) in the weak phase. The one-plaquette model has no photon, so it does not test the Coulomb mechanism; it only shows that the last term is a rank-one change of the odd block and that it acts on the pole at z = -1.

At small beta both groups pass (row 1708, Nissim as reported there): in the contraction window |B|_omega <= 6 beta |W(l)| is a small bounded change. The selective line matters only where (PS) itself is in doubt.

## 8. Open items by name

- (TL) in 4D at any beta; in the window 6 beta a^4 < 1 it needs a bound on W_beta on all (non-reduced) loops.
- (EN): the bootstrap enclosure certificate; not built.
- Whether (PS) is false in 4D on the weak side (the block direction of section 4.3 (b)); a construction or a refutation.
- A correct weak-side statement, for example (PS*), and its use in Theorem T, step 2 and (LD).
- Boundedness of the even twin kernel for q = 1 (Abel summation, not written).
- All citations are from memory; none was read in this row.

RESULT: Certificate (Theorem C, PROVED): head inverse on loops up to length Lambda, an enclosure table of W_beta, and weighted row sums with theta < 1 prove (PS) with kappa = mu/(1-theta). Tail lemma (TL): reduced to one statement; OPEN in 4D; its row-sum form needs 6 beta a^4 < 1 (PROVED); PROVED false in the one-plaquette twin's weak phase, where (PS) itself is false (bounded kernel sum (-1)^(k-1-n) P_n(1-2/beta), exact to k = 240), so (PS) is GUESSED false on the 4D weak side and needs restating. First instance: twin certificate passes at beta = 9/10 (kappa <= 109.4); 4D planar series from the row generator gives W(p) = u + 4u^5, three selection rules agree. Cost at order-one beta: 4e6 row classes at Lambda = 16, about 1e14 rational operations, beyond Lean. U(N) twin: differs only in the odd block; fails by the photon's power law (ARGUED).
