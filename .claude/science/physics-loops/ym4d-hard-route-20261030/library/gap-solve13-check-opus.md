# Check of gap-solve13-astra62.md (FINISH row 1170)

Status: DONE. Written step by step as the check went; RESULT at the end.
Checker: Claude Opus 5.5 (subagent of the lead).
File under check: library/gap-solve13-astra62.md.

Started 2026-11-19 (date -u at launch of row 1170: 16:15Z).
The first tool call created this file with a header only; this plan was
appended by the second call.

## Plan (at most eight steps)

1. Read the file under check in full (426 lines, in ranges) and the
   council brief for the setting.
2. Read the parts of rows 1157-1167 (gap-solve8 ... gap-solve12 and their
   checks) that the file cites.
3. Check the winding-majority large-deviation rate
   exp(-(1+o(1)) beta n^2) and the doubled reversal cost.
4. Check the two-collar case.
5. Check (12), (26), (19)-(20), (22), (15).
6. Check everything else, statement by statement.
7. Numeric guide where useful (guide only, under 2 GB).
8. Verdict table, summary and RESULT line.

## Step results

### Step 1. Reading (done)

- Read `library/gap-solve13-astra62.md` in full, L1-L426, in four ranges.
- Read `library/gap-council-brief.md` in full (122 lines). The wall (W), the
  strict seed limsup [X(n/2) - 1] < 1/1650 and z^- in the file's L9 match the
  brief's Section 2 and row 1167 L9.
- Notation used below. m = n^2 transverse lines y = (x_2, x_3). sigma is the
  relative sign cochain of the two completions on links with shared adjoints.
  B = d sigma is the relative curvature. The ribbons R_+(y), R_-(y) are the
  14 faces at y on the two time arcs between the endpoint lines. b(y,t) is
  sum over x_1 of c_1(x_1, y, t) for a compact primitive c. h = e^{-beta}/z_beta.

### Step 2. Cited earlier rows (done)

- Row 1167 (`library/gap-solve12-astra62.md`): read in full (306 lines). Its
  check, row 1168 (`library/gap-solve12-check-opus.md`, table L597-L664):
  HOLDS AFTER CORRECTION, hypothesis only, at its L252 (two spatial wells),
  which this file does not use. Its (1), (2), (3), (5), (6)-(7), (9), (10),
  (11), (12), (14), (17), (20), (21) HOLD there.
- Row 1157 (`library/gap-solve8-astra62.md`) L138-L165: the one-link error
  q(s) and its bounds c sqrt(1+s) e^{-s} <= q(s) <= C sqrt(1+s) e^{-s}, (8).
- Row 1155 (`library/gap-solve7-astra62.md`) L130-L134, (9):
  E exp{c beta sum_S (1-w_p)} <= C^{|S|} with absolute c = 1/8, C. Its check
  (row 1156) HOLDS. The absolute C matters for (16)-(17) below.
- Row 1153 (`library/gap-solve6-astra62.md`) L35 and L177: the strip bound
  E q(U_{1 x h})^2 <= C h/beta by Jensen on the h-th moment of a nonnegative
  eigenvalue ratio. Its check (row 1154) HOLDS. This is the file's (1).
- Row 1161 (`library/gap-solve9-astra62.md`) L215: the one-cube test
  s(u) <= 1/2 for 3 <= u <= n/512 (range 4 | n, n >= 2^70 per check 1162);
  L174 is its (13); L367 is its (25).
- The exercise items cited at L15 exist: `library/gap-invent-selective-max.md`
  C8 (L128) and `library/gap-wall-max.md` B2 (L199).

### Step 3. The full-adjoint majority rate (12) and the doubled cost (26)-(27) (done)

**S20. (11), L130-L136. HOLDS.** Given all adjoints, U_e = sigma_e U~_e on
every link, so w~_p = -w_p exactly on faces of B. For the maximizing
directional subset D of S, Pr(S in B) <= Pr(sum_D (a_p + a~_p) = 2|D|)
<= e^{-beta|D|} (E e^{beta sum_D a})^{1/2} (E e^{beta sum_D a~})^{1/2}
<= h^{|D|}, by exponential Markov, Cauchy-Schwarz and row 1167 (1) on each
Wilson marginal. max_i d_i >= k/2 since the four d_i sum to 2k. The Haar ball
of radius (1+beta)^{-1/2} has mass c(1+beta)^{-3/2} and Boltzmann weight at
least e^{-1/2}, so log h = -beta + O(log(2+beta)). The direct re-derivation
of row 1167 (1) (positive multipliers, 0 <= F_s <= F, Schatten and trace
Hoelder) is the same as the checked one.

**S21. Kept components, six faces, L138. HOLDS.** Faces of B in one
three-cube lie in one component, and each cube has an even number of B
faces, so each component is closed. A component of fewer than K faces lies
in a box of width O(K) < n, u, and compactly supported 2-cocycles in four
dimensions are coboundaries of compactly supported 1-cochains. The identity
b(y) + b(y + e_i) = sum_{x_1} (dc)_{1i}(x_1, y) holds because the
c_i-terms cancel in the full x_1 sum. So the pairing with a ribbon is
b(y, t_1) + b(y, t_2). If it is odd, b = 1 at some endpoint line, and the
support of b(., .) has an entry and an exit edge on each of the three
transverse lines through that point. That gives two faces each of types
12, 13, 14, so six direction-1 faces. Checked.

**S22. d_1 >= m on the kept union, L140. HOLDS.** If B = -1 then
N_- >= m/2 (also at a tie, by the tie rule). For an exact (closed, filled)
component the pairing with R_+(y) equals the pairing with R_-(y), since
both ribbons have the same boundary. Discarded components pair to zero. So
kept components meet each of the 2 N_- disjoint ribbons in an odd set:
d_14(kept) >= 2 N_- >= m, hence d_1 >= m.

**S26. Improved probability upper bound, L167-L171. HOLDS.** At the
endpoint t_i where b(y_0, t_i) = 1, the two transverse spatial lines
(directions 2, 3) through y_0 on that slice each have an entry and an exit,
and each change edge needs a face of type 12 or 13 at time t_i in its own
strip. These four spatial faces are distinct from all 14 faces. The pairing
is odd on both arcs (same boundary), so d_14 >= 2. Hence for a kept small
component, with 0 < s < 1 - eps:
(1-eps) d_1 + eps k/2 - s d_14 >= (1-eps)(4 + d_14) - s d_14
>= 4(1-eps) + 2(1-eps-s) = 6(1-eps) - 2s.
For a large component the same remainder is at least eps k/2, using
d_1 >= d_14. Since max_i d_i >= (1-eps) d_1 + eps k/2, (11) on the union
gives Pr <= h^{s m} prod_S h^{e(S)}. The sum over families is at most
prod (1 + h^{e(S)}). Its log is at most
C_K n^3 h^{6(1-eps)-2s} + C n^4 sum_{k >= K} (C_0 h^{eps/2})^k. The first
term is n^{3 - kappa[6(1-eps)-2s] + o(1)} = o(n^2) exactly when
kappa[6(1-eps) - 2s] > 1, that is s < 3 - 1/(2 kappa) for small eps. The
second tends to zero for K > 8/(kappa eps). So the lower limit of the rate
is at least min(1, 3 - 1/(2 kappa)) when this is positive.

**S27. (13), L173-L184. HOLDS.** No plaquette contains two selected links
(collinear links never share a square; black checkerboard lines are not
adjacent). Given the first exterior, each selected link has density
proportional to exp(k_e . u), |k_e| <= 6 beta (six plaquettes). The error of
the more likely lift, averaged over the adjoint, is the stated q(s), since
Haar on S^3 projects to the density proportional to sqrt(1-t^2). Numerator
>= e^{-1/2} (3/4)^{1/2} /(2s) on [-1/(2s), 0]; denominator
<= e^s sqrt2 Gamma(3/2) s^{-3/2}; so q(s) >= c sqrt(s) e^{-s} for s >= 1,
and q is nonincreasing by tilting. U and U~ are independent given V, and
(V, first exterior) is generated by (first exterior, selected adjoints), so
revealing U~ leaves the selected sign posteriors unchanged. theta_y equals a
known sign times the product of the n lift signs on line_1(y), so its
smaller conditional probability is (1 - prod a_e)/2. Different lines use
disjoint, conditionally independent links, and E[a_e | ext] = 1 - 2q(|k_e|)
<= 1 - 2q(6 beta). This gives (13). The extra white line costs at most
1 + e^{12 beta}: the central flip of one of its links is an involution that
fixes V and the selected event and changes six deficits by at most 2 each.
With nq(6 beta) = n^{1 - 6 kappa + o(1)}, the rate upper limit is
(1/2)(6 - 1/kappa) = 3 - 1/(2 kappa) when kappa > 1/6, and 0 otherwise.

**S28. N_-/m -> 0 for kappa > 1/6, L186. HOLDS.** A component of size >= K
meeting a ribbon (O(n^2) faces) costs C n^2 (C_0 sqrt h)^K =
n^{2 - kappa K/2 + o(1)} -> 0 for K > 4/kappa. A smaller component changing
theta_y has b = 1 on one of the two endpoint lines at y, so it lies within
O(K) of one of 2n links, and costs C_K n h^6 -> 0. Translation invariance and
Markov give the claim.

**S29-S32. The strip transformation and the upper rate one, L188-L205.
HOLDS.**
- Both J and C_D J are conditional Haar translations of the selected links
  given the transverse links and the Gaussians. They induce the same map j on
  V, because Ad(v U) = Ad(-v U) and v depends only on transverse adjoints.
- Affected faces: 2 q_D temporal 14 faces, each with one changed link, whose
  new |Re| is at most |Im U_p| since v_x is pure imaginary; interior 12, 13
  faces with two changed links, where the transformed holonomy is
  v_x U_p v'^{-1} with v' = Ad_{T^{-1}} v_{x'}, so the excess chord is
  |v_x - Ad v_{x'}|, of mean square O(beta^{-2/3}) by the 2D form of (2);
  O(n) boundary faces of cost at most 2. With the exact identity
  D(Phi_* mu || mu) = beta E_mu[S(Phi U) - S(U)] for a Haar-preserving
  bijection, each one-path entropy is at most beta M (1 + C beta^{-1/2})
  + C beta^{1/3} q_D + O(beta n) = (1 + o(1)) beta M. Same for C_D J (the
  two central signs cancel on interior spatial faces).
- (14): Donsker-Varadhan with the adjoint function
  F = beta sum (1 - |w_p|) over the M faces. Under j_* mu_V the faces have
  |w_p| <= |Im U_p|, so E F >= beta M (1 - C beta^{-1/2}). The M faces all
  contain direction 1, so the full deletion of row 1167 (1) bounds the log
  moment by M log(1/z_beta) = O(M log beta). Hence (1 - o(1)) beta M.
  Uniform in the auxiliary choice.
- Chain rule: P = mu_V(dV) mu(dU|V) mu(dU~|V); Q has V-marginal j_* mu_V and,
  since j is a bijection, conditionally independent paths with conditionals
  (Phi_* mu)(.|V') and (Phi'_* mu)(.|V'). So
  D(Q||P) = D(Phi_*mu||mu) + D(Phi'_*mu||mu) - D(j_*mu_V||mu_V)
  <= (1 + o(1)) beta M. Checked term by term.
- Common J keeps sigma on the endpoint lines (U~_e = sigma_e U_e and both get
  the same v_x). C_D flips sigma on one link of each line y in D. So
  N_-^Q >= q_D - N_-^P > m/2 with Q-probability -> 1 for d > 1/2.
- D(Q||P) >= Q(E) log(1/P(E)) - log 2 gives -log P(N_- > m/2)
  <= (1 + o(1)) 2 d beta m. Sending d to 1/2 gives the upper rate 1.

**S25. (12), L158-L165. HOLDS.** S26 gives liminf >= min(1, 3 - 1/(2kappa))
when positive; S27 gives limsup <= max(0, 3 - 1/(2 kappa)); S32 gives
limsup <= 1 for kappa > 1/6. For kappa <= 1/6 both sides are 0. The bounds
meet at min{1, max(0, 3 - 1/(2 kappa))}, also for the strict majority.
11/(3 pi^2) = 0.3715 > 1/4, so the rate is 1 on the conditional slope.

**S70. (26), L383-L388. HOLDS.** Lower rate: N_- >= d m forces
d_14(kept) >= 2 d m, so the same allocation gives h^{2 s d m} e^{o(beta m)}.
Upper rate: (25) with ceil(dm) prescribed negatives gives
-log Pr <= ceil(dm)(-log v_*). The stated upper bound
q(s) <= C sqrt(1+s) e^{-s} holds (numerator <= 1/s; denominator
>= (2s)^{-1} e^{s-1} (2s)^{-1/2} on 1 - t in [1/(2s), 1/s]). So
-log v_*/beta -> max(0, 6 - 1/kappa) = 2 max(0, 3 - 1/(2 kappa)). The strip
at any d' in (d, 1) gives the competing rate 2d' (no need for d' > 1/2 here).
Both together give 2 d I_kappa for d < 1.

**S71. (27) and the endpoint d = 1, L390-L396. HOLDS.** Partition
{N_+ <= k} by the exceptional set E, |E| <= k. Flipping one first-path
endpoint link on each line of E is an involution that fixes every adjoint
observation and maps the event theta_+ = E onto a subset of {N_- = m}, with
density ratio at least e^{-12 beta k}. Summing over E gives (27) with
sum_{j <= k} C(m, j). Overlaps only cancel plaquette changes. With
k = floor(eps m): -log Pr(N_- = m) <= 2(1-eps) I_kappa beta m + 12 beta eps m
+ m log 2 + o(beta m), then eps -> 0. The lower rate at d = 1 is the case
d = 1 of S70. The conditional excess rate 2 eps I_kappa follows by dividing
(26) at d = 1/2 + eps by (12), for I_kappa > 0. "Exact unanimous reversal
costs twice the majority rate" is (26) at d = 1 against (12).

### Step 4. The two-collar case (done)

**S6. (1), L17-L21. HOLDS (imported).** The bound is row 1153 L35 and L177
(checked by row 1154). The step shown is Jensen: E w_{1 x h} >= (E w_p)^h
>= 1 - Ch/beta, then |1 - U|^2 = 2(1 - w_U). The one-plaquette bound and the
transfer representation are imports, not re-derived here.

**S7. (2), L23-L34. HOLDS.** Given the links, G_x is Gaussian with
covariance sum_z w_x(z)^2 P_xz P_xz^T = I_3. The tent has unnormalized
squared norm of order b^3 and neighbour differences at most 1/b at O(b^3)
sites, so the normalized squared difference is O(b^{-2}). Coordinate-ordered
paths to neighbours x, y differ by at most two width-one strips of length at
most b (none when the bond is along the last coordinate). With
||Ad_g - I||_F <= C|1 - g| and |1 - g_1 g_2| <= |1 - g_1| + |1 - g_2|, (1)
gives C b/beta for the transport part. Normalization: |u/|u| - v/|v|| <=
2|u - v|/|u|; writing G_x - Ad G_y = M G_x + E with E independent of G_x,
E|M G_x|^2/|G_x|^2 = ||M||_F^2/3 and E|G_x|^{-2} = 1 in R^3, so the ratio is
at most the unnormalized mean square. Factor 4. Gauge covariance in law holds
because each eta_z is isotropic.

**S9-S11. The first map, (3) and (4), L40-L62. HOLDS.** H_x is a Haar
translation given tangential links and eta; alpha = pi gives H = -1, a flat
flip on the second collar, so A is fixed and s_2(y) flips on every line.
For an affected face the transformed holonomy is G U_p up to conjugation, and
|1 - G| <= |alpha_x - alpha_y| + |v_x - Ad v_y| (since |e^{av} - e^{bv'}| <=
|a - b| + |v - v'|). The new deficit is |1 - G U_p|^2/2 <= |1-G|^2 + |1-U_p|^2,
a pointwise bound, so no independence is needed. O(mw) ramp faces give
C m (beta/w + beta w b^{-2} + w b + w), which is (3). The joint law with only
the first path moved has relative entropy D(Phi_* mu || mu) because
A(Phi U) = A(U). Since B(Phi U, U~) = -B(U, U~) and the tie rule is odd,
data processing gives d(1-p||p) <= D, and (1-2q) log((1-q)/q) >=
(1/2) log(1/(2q)) for q <= 1/4. Checked.

**S13. The profile (7), L78-L85. HOLDS.** The walk on shells: position i on
shell k+1 receives (1/(k+1))[i/(k+2) + (k+1-i)/(k+2)] = 1/(k+2), so each
shell is uniform. With an independent uniform stopping shell in [R, 2R-1],
rho(z) = 1/(R(k+1)) <= R^{-2}, sum rho = 1. Mean flow: outflow minus inflow
is 1 at o and -Pr(stop at z) elsewhere, by independence of the stop.
Rotation gives a primal a with da = pi(1_o - rho). Edge values on shell k are
at most pi/(k+1) on at most 2(k+1) edges, so sum a^2 <= 2 pi^2 sum 1/(k+1)
<= C log(2R) and sum (1 + dist) a^2 <= C R. Numerics in Step 7 agree.

**S14. Which links move, L87. HOLDS.** sigma = -1 on the cut 1-links over
the interval I that contains the second collar has 14-curvature exactly at
the two time ends of I, on every transverse translate, and none elsewhere
(12, 13 faces contain two flipped links). At the defect face
-e^{i pi(1 - rho_o)} has angle pi rho_o = 0 mod 2 pi; elsewhere the angle is
pi rho_p. a = 0 in directions 2, 3 and constant there, so all non-14 curls
vanish. Either global sign works because e^{i pi} = e^{-i pi}.

**S15. Axes and (8), L89-L94. HOLDS.** The 2D tent and path comparison work
with one strip. Comb paths from the root (adjacent to o) to a vertex at
normal distance s have length O(s+1). A normal non-tree bond closes a
width-one strip of length O(s+1) with the comb; a transverse bond closes two
such strips plus the transverse root bond, whose error is (2). Squared
triangle inequality and (1) give (8).

**S16. The Jacobian, L96-L100. HOLDS.** For a tree edge from parent x to
child y with v_x = Ad_{U_e} v_y: Ad_{e^{eps a v_x} U_e} v_y =
e^{eps a v_x} v_x e^{-eps a v_x} = v_x, so the reconstructed axes are
unchanged. For an edge from child y to parent x, e^{eps a v_y} U_e =
U_e e^{eps a v_x} with v_x known. Exposing the tree from the root makes each
step a translation by a known quaternion; non-tree edges are left
translations by known quaternions; central factors have trivial adjoint
action. Triangular change of variables, so product Haar is preserved and the
map is bijective.

**S17. (9), L102-L112. HOLDS.** Pulled to the base, the transported axes
differ from the base axis by at most d_p, and |e^{a u} - e^{a u'}| <=
|a||u - u'| telescopes over four factors. The common-axis product is
exp(v(pi k + eps (da)_p)) with angle at most pi rho_p. So
1 - Re B_eps <= C[rho_p^2 + d_p^2 sum a_e^2] (Cauchy-Schwarz over four
edges). Averaging over eps keeps only even sine subsets; with a common axis
these products are real; replacing axes costs at most 4 d_p; each surviving
coefficient is at most |a_i||a_j| <= (1/2) sum a^2. Then
Re U_p - Re(Bbar U_p) = Re U_p (1 - Re Bbar) + Im Bbar . Im U_p, with
|Im U_p|^2 <= 2(1 - w_p) and AM-GM, gives (9). The file correctly says this
bounds only the mean over the two signs. Since D(Phi_* mu || mu) is an exact
identity for each sign, averaging the entropies is legitimate.

**S18 and S12. Summation, (5), (6), L66-L76, L114-L118. HOLDS.** Per
transverse site: beta sum rho^2 <= beta/R^2; the rest is
C sum_e a_e^2 [beta/b^2 + b + dist(e) + 1] <= C(beta/b^2 + b + 1) log(2R)
+ C R by (7)-(8) and E(1 - w_p) <= C/beta. With b = R of order beta^{1/3}
this is C beta^{1/3} log(2 + beta) per site. Each map reverses all lines in
exactly one collar (profile boxes avoid the collars; the collar links get
only central factors), so (4) gives (5). For (6), Z_tw = Z_0 E_mu
e^{-beta(S_tau(Phi U) - S(U))} and Jensen give -log(Z_tw/Z_0) <= beta E[...];
averaging valid bounds over (eps, eta) gives (6). Hypotheses (room of order
C beta^{1/3}, and (1) at beta >= 1 with the chord bound below) are stated.

**S19. (10) and the collar comparison, L122-L128. HOLDS.** (10) follows from
S20-S24; (5) gives -log p = o(beta m); so p/p_all grows exponentially on the
scale beta m once kappa > 1/6.

**S64-S66. (23), L348-L362. HOLDS.** In the original pair: E D_n <=
C n^3 h^6 = o(m) (row 1167 (17) upper bound), each path's realized lift
passes all tests along a specified ribbon except with probability
C n^2 h^6 = o(1) at slope > 1/3, and Pr(B = +1) >= 1/2 - o(1) because the
two readings on one line are conditionally i.i.d. given the collars. For the
transform of (5), outside a fixed neighbourhood of the ribbon's
intersection with the two boxes the change is central with zero curvature.
Inside, the expected original deficit is O(R^2/beta) and the expected sum of
|1 - B_eps|^2 is C{R^{-2} + (b^{-2} + (b+1)/beta) log(2R) + R/beta} = o(1)
for b = R of order beta^{1/3}; Markov then keeps every tested face trace
positive near the change. So the transformed lift is admitted and the
explicit rule reads the flipped winding, for all but o(m) ribbons in
probability. Q(event) >= 1/2 - o(1), and the binary event inequality with
the entropy bound of (5) gives (23).

**S74. (29), L407-L413. HOLDS.** In the collar experiment Pr(N_- <= k)
>= 1/3 for k = ceil(C(1 + n^3 h^6)) (S72). Each map of (5) sends this event
onto {N_- >= m - k}, so P(N_- >= m - k) >= exp(-3[C m beta^{1/3}
log(2+beta) + log 2]). Then (27) with i = m costs
k(12 beta + log(m+1)) = n^{3 - 6 kappa + o(1)} log n = o(m) for kappa > 1/6.
The second part of (29) is (26) at d = 1. The lower bound
-log Pr_collars(N_- = m) >= m v_* = n^{3 - 6 kappa + o(1)} follows from (25)
(collar adjoints are first-path adjoints), for kappa < 1/2.

### Step 5. (19)-(20), (22), (15) (done)

**S43-S45. Stability of (12) under r = o(n^2) holes, L269-L277. HOLDS.**
Setting the relative sign to +1 on unobserved links gives an exact cochain
whose endpoint windings are the true relative windings (endpoint slices are
observed) and whose curvature agrees with B on every face with four
observed links. At most 6r faces touch a hole, and removing them lowers each
d_i by at most 6r, so (11) loses at most h^{-6r} = e^{o(beta m)} once on the
union. Upper rate: J reads only the observed endpoint-slice adjoints, so j
is a bijection of the observed field; at least M - 6r of the M temporal
faces have observable |w_p|; the chain-rule subtraction holds with the
observed marginal because both maps induce the same j on it; common J keeps
sigma on the endpoint lines. N_-/m -> 0 with holes follows from the same
bound at threshold eps m, since 2 s eps m > 6r + o(m). (13) needs only the
selected adjoints and conditional independence given the observation.

**S46. (19), L279. HOLDS.** At the jump e^{pi v} = -1 for every unit
imaginary v, so the jump face carries an exact central factor that cancels
the slab's 14-curvature there, and the 24, 34 faces at x_1 = 1 see two
factors -1. The ramp back to 0 over w steps costs beta/w per transverse
site, and axis mismatches cost beta w (b^{-2} + b/beta). The temporal links
are translated by quaternions that depend only on spatial adjoints (central
slab factors do not move axes) and on eta. Only temporal links at
x_1 in [2, w] at the two time ends change adjoint: at most 2 n^2 (w + 2).
The map fixes the reduced observation and reverses every theta_y. Cost
C m (beta/w + beta^{2/3} + w) = o(beta m) for w -> infinity, w <= beta^{1/3}.
(4) gives (19) for both signs of the odd bit.

**S47-S51. (20), L281-L293. HOLDS.** Checked step by step.
- At most C_1 m/(K+1) < m/8 tori carry more than K missing normal edges.
- Each missing normal edge lies in exactly one 14 torus, inside one arc
  (endpoint 1-links are observed; a temporal edge's two 14 faces are at the
  same time step). After merging touching rectangles, final boxes are
  pairwise non-touching, of side at most 2K + 2 (subadditive widths), and no
  missing edge lies on a box boundary.
- Cheap box: in a comb gauge each link angle is at most a sum of at most
  2K + 2 plaquette angles, bounded by C sqrt((K+1) S_B) via
  theta^2 <= (pi^2/2)(1 - cos theta). A cycle of known edges has at most
  C(K+1)^2 edges, so the two holonomy angles sum to at most
  C(K+1)^{5/2} sqrt(S_B) < pi under the threshold c/(K+1)^6. A relative sign
  -1 on such a cycle would force phi_1 + phi_2 = pi. So sigma is a gradient
  on each component of the known graph, and the gradient fill makes the 14
  curvature vanish in the box. Faces outside boxes on good tori touch no
  missing edge.
- Expensive boxes on at least m/8 good tori force deficit c_K m on a
  deterministic set of C_K m faces; row 1155 (9) and Cauchy-Schwarz give
  exp(-c'_K beta m + C'_K m).
- Otherwise at least m/2 - m/8 - m/8 = m/4 negative good cheap tori give at
  least m/2 clean kept 14 faces. (11) on the clean part, with fractions
  s, gamma, eps (gamma > 1/(6 kappa), gamma + s + eps <= 1, 3 eps C_1 < s/4),
  gives the factor h^{sm/2 - 3 eps r} <= h^{sm/4}; small dirty supports
  number C_{K'} r = O(m) = o(beta m); small clean and large supports are as
  in (10). So p <= e^{-c beta m}. The consequence r/m -> infinity, and its
  attainment by (19), are correct.

**S56-S62. (22), L323-L339. HOLDS.**
- J_R^0 = W prod_{p in R} xi_p g_p by the Stokes identity of row 1167 (9).
- A temporal link e in the ribbon interior lies on exactly two ribbon faces
  (its left and right 14 faces); every g_q that reads u_e is centred within a
  fixed distance of e.
- The frustrated cube: four links e^{i pi/4} around one square give
  holonomy -1 there, +1 on the opposite square, and e^{+-i pi/4} (trace
  1/sqrt2) on each side face. Each cube edge lies on two cube faces, so the
  product of the six signs (-1) is lift-invariant and stable on an open set.
  Even-based cubes on one slice are vertex-disjoint.
- Distances: q to a 12 face at its spatial base in a common 124 cube (1
  step); in-plane unit translation of a 12 face (2 steps via a 23 or 13 face),
  perpendicular translation (1 step); at most 2 + 2 + 1 units per coordinate
  pattern gives at most 10; one more step to any face of the 123 cube. Total
  12. A BFS on a 4D lattice in Step 7 confirms this for all base parities.
  Sixteen disjoint cubes give at least sixteen negative faces in any lift;
  over three spatial directions their counts sum to at least 32, so at least
  six negatives share a direction. No lift passes (7): g_q = +1 for every
  affected q, independent of u_e.
- With staples 1 and i (set by the temporal neighbours), caps about
  (1+i)/sqrt2 and (-1+i)/sqrt2 give face-sign products -1 and +1. So the block
  factor takes opposite values on the two caps for every exterior.
- Conditional density of M_0 block links is at least e^{-12 M_0 beta}
  (oscillation of at most 6 M_0 plaquettes), the caps have conditional
  probability at least c_1 e^{-12 beta}, so each block bias is at most
  1 - c_2 e^{-C_2 beta}. Blocks at large fixed spacing are conditionally
  independent given the exterior, which contains the collars and W. So
  |E[J | A]| <= (1 - c_2 e^{-C_2 beta})^N with N >= c n^2, and
  p_R = (1 - E b^2)/2 >= c min{1, n^2 e^{-C beta}}. Same for Pr(J != W).

**S33-S42. (15), L209-L265. HOLDS.**
- Kernels (L220): p_{+,s} = P^s E_+ is symmetric and nonnegative and
  ||p_{+,s}||_HS^2 = X_+(2s); X(u) <= 8 X_+(u) because Tr(E_+ P^u) is the mean
  of eight nonnegative twisted traces, one of them X(u).
- Shorter period (L222): the endpoint ratio bound (row 1167, L160 there)
  survives the flip average; C >= e^{-8k beta} B on fibres; testing on the
  lifted product of marginal square roots gives
  log X_sec(t) <= 16 k beta - 2 log H_sec(t). With 16 k beta = O(log^2 n) the
  first hypothesis gives log X(t) = o(sqrt n).
- Local laws (L224-L229): no face contains two missing links (spatial faces
  by hypothesis; a temporal face has one spatial link per slice), so q_B is a
  product; s_e is built from retained links.
- Good event (L231-L235): |u_ej - s_e|^2 <= 4(1 - w_{p_j}) + 4(1 - w_{p_s}),
  so the sum is at most 28 times the incident deficits; row 1155 (9) with
  absolute C gives C^k e^{-cM}. (With z_beta^{-1} constants instead, the
  bound would fail at k of order log n; the file uses the right input.)
- (16): h_e . s_e = 6 - (1/2) sum_j |u_ej - s_e|^2 >= 6 - eta/(2 kappa_0);
  Phi(beta h) <= C e^{beta|h|} beta^{-3/2} for |h| >= 5; cap volume
  c beta^{-3/2}; on the cap |h| - h.v <= 6/beta + sum_j |u_ej - s_e|^2. So
  q_B >= c^k e^{-M} l_R.
- (17): E||f(X_0)||^2 = 1, E||f(X_0) - f(X_1)||^2 = 2(1 - X(2t+1)/X(2t));
  e_t <= t^{-1} log(X(t)/X(2t)) by 1 - r <= -log r and Jensen on r^{-t}.
  The replacement costs at most 2 sqrt(2 e_t) by Cauchy-Schwarz, and
  reweighting the stationary three-slice law by p_{2t}(X_1, X_{-1})/X(2t)
  is (X(2t+2)/X(2t)) times the period-(2t+2) cylinder law with the two
  retained transporter layers.
- (18): l_R <= delta^{-1} q_B gives the Jensen step; conditional variance
  given (B, R) is at most E||f(X_0) - f(X_{-1})||^2 = 2 e_t;
  (1 - sqrt chi)^2 <= 1 - chi; sqrt(chi) a_R lies in ran(D) tensor L^2.
- Constants (L263): delta^{-1} <= n^{C(c_* + eta)} <= n^{1/4} and
  C^k e^{-cM} <= n^{-c eta/2}, so (18) is o(1). K_+ = sqrt(X/X_+) K E_+
  gives the factor sqrt 8.
- Conclusion (L265): 0 <= DKD <= B_0 pointwise, ||B_0||_HS = 1,
  ||B_0 - DKD||^2 <= 1 - ||DKD||^2 = o(1), and testing on the unit lifted
  product gives X_sec(2t)^{-1/2} >= H_sec(2t) - o(1). With
  liminf H_+(2t) > sqrt(2/3) this gives limsup X_+(2t) < 3/2. Since
  2t = 4 floor(n/4096) lies in [3, n/512], row 1161's test applies (its
  4 | n, n >= 2^70 range is the same asymptotic setting). The necessity
  remark uses ||K - 1||_HS^2 = 2 - 2/sqrt(X(v)) and Hellinger contraction;
  t >= n/8192 = b/2 for the row 1167 enlargement with D = 4096. HOLDS.

### Step 6. Everything else (done)

**S1. Repo search, L1-L5. GUIDE.** Not re-run here; the pins and PR line
ranges are not re-verified.

**S2. Account readings, L7 and L11 (external part). GUIDE.** Readings of the
Sussman-Alpoge text at revision 31a47c543775; not re-verified here.

**S3. Setting, L9. HOLDS.** Matches the council brief Section 2 and row
1167 L9. "Row 1167, whose independent check is pending at the pin" is a
statement about the pin; row 1168 has since checked it (S41 correction
only, unused here).

**S4-S5. Overview and motivation, L11, L15. HOLD** as summaries; the cited
items exist (Step 2).

**S8. Setup and the odd tie rule, L38. HOLDS.**

**S23. Entropy bound and the lower limit in (10), L142-L152. HOLDS.**
max_i d_i >= (s + gamma) d_1 + eps k/2 with s + gamma + eps = 1; the gamma
part pays 6 per small kept component; n^3 h^{6 gamma} = o(n^2) iff
6 gamma kappa > 1. Superseded by S26 but correct.

**S24. Upper bound 4 in (10), L154. HOLDS.** The unsmoothed slab flip fixes
all adjoints, reverses every theta_y and changes 2m plaquette signs, so the
density ratio lies in [e^{-4 beta m}, e^{4 beta m}].

**S52. Cost of the positive profile estimate, L297-L301. HOLDS.**
E(1 - w_p | rest) >= 1 - m(6 beta) with m(s) = (log Phi)'(s) increasing,
and 1 - m(s) >= c/s from angles in [s^{-1/2}, 2 s^{-1/2}]. If
beta sum f_p^2 < log beta, Cauchy-Schwarz gives sum_{Q_j} |f_p| =
O(j sqrt(log beta/beta)) = o(1) for j <= beta^{1/4}; the odd flux gives
|sum_{dQ_j} a_e| >= pi/2 on disjoint boundaries of length O(j); so
sum a^2 >= c log beta and beta E(1-w_p) sum a^2 >= c log beta per plane.
Precision (no change needed): for a general profile the rho_p^2 term of (9)
is read as the squared common-axis chord, which is how (9) is derived and is
comparable to f_p^2.

**S53. (21), L303-L309. HOLDS.** Same good-event variance proof with g;
the bad part is at most 4 ||g||_inf^2 Pr(G^c) in the stationary vacuum;
E(g(X_0) - g(X_{-1}))^2 = 2 <g, (I - P) g>.

**S54. Limitation of the common minorant, L311-L317. HOLDS.** With retained
links and temporal links equal to one, the spatial staples are 1 and both
temporal staples equal the neighbour link e^{+- i theta}; h_+- =
(4 + 2 cos theta, +- 2 sin theta). The affinity is
Phi(beta u)/Phi(beta sqrt(u^2 + 4 sin^2 theta)); the argument gap tends to
4/(2 * 6) = 1/3 and (log Phi)' -> 1, so the limit is e^{-1/3} (numerics in
Step 7). The local deviation beta sum |u - s|^2 is about 2 per link, so these
histories lie in G when 2 c_* < eta. A common minorant has mass at most the
product affinity e^{-ck}.

**S55. Retained neutral level, L319. HOLDS.** For 1 + lambda h(x) h(y) the
kernel at time s is 1 + lambda^s h h, its trace at period 2t is
1 + lambda^{2t}, the R-marginals are pi_R, and the affinity is
(1 + lambda^{2t})^{-1/2}: limit 1/sqrt2 for lambda = e^{-1/n^2}, 1 for fixed
lambda; the first hypothesis of (15) holds in both. These kernels are not the
Wilson transfer, as stated.

**S63. Obstruction to local-error amplification, L341-L346. HOLDS.**
E|E(J | E)| >= E[W E(J | E)] = E(WJ) = 1 - 2 Pr(J != W) for E containing W.

**S67. (24), L364-L370. HOLDS.** P(Y = y | A) = (1 + y lambda b)/2,
posterior mean (b + y lambda)/(1 + y lambda b), and
1 - m_y^2 = (1 - b^2)(1 - lambda^2)/(1 + y b lambda)^2; averaging over y
gives (24) and both bounds. |b| < 1 a.s. by the block bound of (22), so
p_lambda/(1 - lambda^2) -> 1/2 by bounded convergence. Exact check of the
algebra in Step 7.

**S68. (25), L374-L379. HOLDS.** Black lines at endpoint 1 and white lines
at endpoint 2 share no plaquette (different times are far apart). The
observation is a function of the first path's adjoints, so revealing the
second path does not change the posteriors. Each line probability lies in
[(1 - prod a_e)/2, (1 + prod a_e)/2]; averaging the independent factors
gives both bounds.

**S69. Coupling to fair signs, L381. HOLDS.** Coordinate coupling gives
mismatch prod a_e/2 per line; convexity removes the extra exterior. For
kappa < 1/6, n^2 exp(-2 n q(6 beta)) -> 0.

**S72. Correction cost, L398. HOLDS.** Pr(theta_y = -1) <= 1/2 for two
conditionally i.i.d. products; |1_{B=-1} - N_-/m| <= D_n/m; E D_n <=
C_r n^3 h^6 with r chosen so the large-component term is at most n h^6.
Pr(N_- <= k) >= Pr(B = +1) - E D_n/k >= 1/3 for large C.

**S73. (28), L400-L405. HOLDS.** -log Pr(N_- = 0) <= log 3 +
k(12 beta + log(m+1)) = n^{3 - 6 kappa + o(1)}, and >= m v_* =
n^{3 - 6 kappa + o(1)} by (25), for 1/6 < kappa < 1/2. At the conditional
slope 3 - 6 kappa = 0.771.

**S75. O(n^2) holes and the explicit reading, L417. HOLDS.** Pr(theta_y != B)
<= C n h^6 + Pr(majority != b_1 b_2) = o(1) using only the collars (no
translation invariance needed), Pr(B = -1) <= e^{-c beta m} by (20), and
each reading differs from its true product with probability O(n^2 h^6).

**S76. OPEN, L419-L424. HOLDS** as a statement of what remains: the two
strict inequalities of row 1167 (10) at one permitted side.

**S77. RESULT, L426. HOLDS** as a summary of what the file proves; the
"(1+o(1))" rate and the doubled exponent are (12) and (26) at the
conditional slope, the collar statements are (29) and (28).

### Step 7. Numeric guides (done; GUIDE only, they prove nothing)

One scratch script (`check1170_guides.py`, kept in the session scratchpad,
not committed), pure Python plus numpy and scipy, run with -E -P. Peak
resident memory at most 143 MB per part; total run time under one minute.

- A. q(s) by quadrature: nonincreasing on the grid; q(s)/(sqrt(s) e^{-s})
  = 0.814, 0.828, 0.822, 0.811, 0.804, 0.801, 0.799 at s = 1, 5, 10, 20, 50,
  100, 200, tending to sqrt(2/pi) = 0.798. Consistent with both bounds used.
  kappa = 11/(3 pi^2) = 0.37151: 3 - 1/(2 kappa) = 1.654 > 1,
  6 kappa = 2.229, 3 - 6 kappa = 0.771.
- B. The profile (7), built exactly from the walk for R = 2, 4, ..., 128:
  max |da - pi(1_o - rho)| = 2.2e-16; R^2 max rho in [0.67, 0.99];
  sum rho = 1; sum a^2 / log(2R) in [5.8, 6.2]; sum (1 + dist) a^2 / R in
  [8.9, 10.0]; box side about 2R.
- C. Affinity of L313: 0.72714, 0.71759, 0.71664, 0.71654 at beta = 10,
  10^2, 10^3, 10^4, tending to e^{-1/3} = 0.71653; the argument gap tends to
  1/3; beta sum |u - s|^2 tends to 2 per link.
- D. BFS in the 4D face graph (adjacent = common 3-cube; graph restricted to
  a box, which can only increase distances): for every parity of the base of
  the 14 face q, all six faces of every 123 cube at even spatial bases within
  2, at times t and t+1, are within face distance 8 (the file's path bound
  is 12). The number of such cubes is 16 to 54 by parity, so at least 16.
- E. Frustrated cube: traces (-1, 1, 0.707, 0.707, 0.707, 0.707), sign
  product -1; in 20000 random lifts with perturbation 0.15 the product was
  always -1.
- F. (24): exact two-point computation against the formula, maximum error
  2.2e-16 over 20000 random (b, lambda).
- G. Random compactly supported Z_2 cochains c (box at most 3^4, torus
  8^3 x 10): in 2243 endpoint lines with b = 1, the strip faces of types 12
  and 13 at that time, the odd pairing on both arcs, d_14 >= 2 when the
  pairing is odd, and d_1 >= 6 held every time. No failures.

### Step 8. Verdict table and result (done)

| Statement | Lines | Verdict |
|---|---|---|
| S1 repo search | L1-L5 | GUIDE (not re-run) |
| S2 account readings | L7, L11 (external part) | GUIDE (not re-verified) |
| S3 setting | L9 | HOLDS |
| S4 overview | L11 | HOLDS as a summary |
| S5 motivation, citations | L15 | HOLDS as a reading |
| S6 (1) strip bound | L17-L21 | HOLDS (imported from row 1153, checked by row 1154) |
| S7 (2) transported axes | L23-L34 | HOLDS |
| S8 two-completion setup, odd tie rule | L38 | HOLDS |
| S9 first map | L40-L44 | HOLDS |
| S10 (3) | L46-L56 | HOLDS |
| S11 (4) | L58-L62 | HOLDS |
| S12 statements (5), (6) | L66-L76 | HOLDS |
| S13 profile (7) | L78-L85 | HOLDS |
| S14 which links move | L87 | HOLDS |
| S15 comb axes, (8) | L89-L94 | HOLDS |
| S16 Haar preservation | L96-L100 | HOLDS |
| S17 (9) | L102-L112 | HOLDS |
| S18 summation, proof of (5), (6) | L114-L118 | HOLDS |
| S19 (10) statement | L122-L128 | HOLDS |
| S20 (11) | L130-L136 | HOLDS |
| S21 kept components, six faces | L138 | HOLDS |
| S22 d_1 >= m | L140 | HOLDS |
| S23 entropy, lower limit of (10) | L142-L152 | HOLDS |
| S24 upper bound 4 | L154 | HOLDS |
| S25 (12) | L158-L165 | HOLDS |
| S26 improved probability bound | L167-L171 | HOLDS |
| S27 (13) | L173-L184 | HOLDS |
| S28 N_-/m -> 0 | L186 | HOLDS |
| S29 strip maps J, C_D J | L188 | HOLDS |
| S30 one-path entropies | L190 | HOLDS |
| S31 (14) | L192-L199 | HOLDS |
| S32 chain-rule subtraction, upper rate 1 | L201-L205 | HOLDS |
| S33 (15) statement | L209-L218 | HOLDS |
| S34 kernels, X <= 8 X_+ | L220 | HOLDS |
| S35 shorter period | L222 | HOLDS |
| S36 local conditional laws | L224-L229 | HOLDS |
| S37 good event | L231-L235 | HOLDS (uses row 1155 (9), absolute C) |
| S38 (16) | L237-L242 | HOLDS |
| S39 (17) | L244-L254 | HOLDS |
| S40 (18) | L256-L261 | HOLDS |
| S41 constants | L263 | HOLDS |
| S42 conclusion of (15), necessity | L265 | HOLDS |
| S43 (19) statement, stability | L269-L273 | HOLDS |
| S44 holes, lower rate | L275 | HOLDS |
| S45 holes, upper rate | L277 | HOLDS |
| S46 (19) construction | L279 | HOLDS |
| S47 (20) statement | L281-L285 | HOLDS |
| S48 repair boxes | L287 | HOLDS |
| S49 cheap boxes | L289 | HOLDS |
| S50 expensive boxes, clean witnesses | L291 | HOLDS |
| S51 count despite holes | L293 | HOLDS |
| S52 cost of the positive profile estimate | L297-L301 | HOLDS (reading precision, no change) |
| S53 (21) | L303-L309 | HOLDS |
| S54 limitation of the minorant | L311-L317 | HOLDS |
| S55 retained neutral level | L319 | HOLDS |
| S56 (22) statement | L323-L327 | HOLDS |
| S57 local sign change | L329 | HOLDS |
| S58 frustrated cubes | L331 | HOLDS |
| S59 sixteen cubes within distance 12, g_q = +1 | L333 | HOLDS |
| S60 two caps | L335 | HOLDS |
| S61 block bias | L337 | HOLDS |
| S62 many blocks, proof of (22) | L339 | HOLDS |
| S63 obstruction to amplification | L341-L346 | HOLDS |
| S64 (23) statement | L348-L354 | HOLDS |
| S65 original pair | L356 | HOLDS |
| S66 transform, proof of (23) | L358-L362 | HOLDS |
| S67 (24) | L364-L370 | HOLDS |
| S68 (25) | L374-L379 | HOLDS |
| S69 coupling to fair signs | L381 | HOLDS |
| S70 (26) | L383-L388 | HOLDS |
| S71 (27), endpoint d = 1 | L390-L396 | HOLDS |
| S72 correction cost | L398 | HOLDS |
| S73 (28) | L400-L405 | HOLDS |
| S74 (29) | L407-L413 | HOLDS |
| S75 O(n^2) holes, explicit reading | L417 | HOLDS |
| S76 OPEN | L419-L424 | HOLDS as a statement of scope |
| S77 RESULT | L426 | HOLDS as a summary |

Counts: 77 statements. 75 HOLD (one of them, S6, as an import from a
checked row), 2 GUIDE (S1 not re-run; S2 a reading of external text). None
HOLDS AFTER CORRECTION. None FAILS.

Needed corrections: none.

Precisions (no change needed):
- L297-L301 (S52): for a general real profile, the rho_p^2 term of (9) is
  to be read as the squared common-axis chord, comparable to f_p^2; this is
  how (9) is derived, and the proof uses it that way.
- L333 (S59): the text says "at least twelve" and then constructs sixteen
  cubes; sixteen is the count, and twelve already suffices. The BFS guide
  finds all their faces within distance 8 of q.
- L9 (S3): the "pending" check of row 1167 has since been done by row 1168
  (one hypothesis correction at its L252, not used in this file).

Not verified here: the account's flow inputs behind the slope 11/(3 pi^2)
(conditional, as the file says); the external pins and line ranges of L5,
L7, L11; the transfer representation behind (1) (row 1153) and the
absolute-constant marked-face bound row 1155 (9), taken from their checks.
The row-1167 inputs used here ((1)-(2), (9), (17) upper bound, (21)) were
re-derived where used.

Provenance: checked by hand by Claude Opus 5.5 (laptop subagent) as FINISH
row 1170; the file under check is by Codex (astra62), so this is a
cross-provider check. Guide runs are in Step 7 and prove nothing.

RESULT: HOLDS - check of row 1169 (`library/gap-solve13-astra62.md`), checked line by line by hand by Claude Opus 5.5 as FINISH row 1170, positive claims first: 77 statements, 75 HOLD (S6 as an import from checked row 1153), 2 GUIDE, none HOLDS AFTER CORRECTION, none FAILS; with all spacetime adjoints shared the negative winding majority has exact rate (12), lim -log p_all/(beta n^2) = min{1, max(0, 3 - 1/(2 kappa))}, from the component bound with four spatial plus two temporal direction-1 faces per kept small component, the single-link fluctuation (13) and the connected strip with the shared adjoint cost (14) paid once, so at the conditional slope 11/(3 pi^2) = 0.3715 the probability is exp[-(1+o(1)) beta n^2]; (26)-(27) give the tail rate 2 d I_kappa and exactly twice the majority rate for unanimous reversal; with only the two collars shared (5) gives d(1-p||p) <= C m beta^{1/3} log(2+beta), (23) a coherent explicit-rule reversal, and (29) -log Pr(N_- = m) <= C m beta^{1/3} log(2+beta) while (25) and (28) force exact unanimity of either sign to vanish at 1/6 < kappa < 1/2; (19)-(20) give the deletion scale r/m -> infinity; (22) gives p_R >= c min{1, n^2 e^{-C beta}}; (15) holds for k <= c_* log n omissions under its two affinity hypotheses; guide runs (under 150 MB) agree and prove nothing; the order-one charged probability, the neutral upper bound, (W) and the four-dimensional SU(2) mass gap remain OPEN.
