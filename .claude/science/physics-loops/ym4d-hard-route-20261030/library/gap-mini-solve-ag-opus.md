lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:22Z

# gap-mini-solve-ag-opus (queue row 1258): plain brief, the 4D SU(2) mass gap

Provenance: Claude Opus 5.5 (max reasoning), Mac mini Claude worker 1, branch claude/ym4d-hard-route pinned at
df7bac204. Started 2026-11-20T10:22Z (date -u). No subagents. Labels: PROVED, ARGUED, GUIDE, OPEN.


## 1. How to attack it (judgement; written 2026-11-20T10:55Z by date -u)

**Read for this choice.** GOAL.md; FINISH.md L1-84 and L299-349; queue row 1258 in full; the RESULT lines of rows
1215-1256; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; `parts/gap.md` L1-104; the plans of the running
siblings (rows 1249, 1255: reading only at this pin); `library/gap-mini-solve-w-opus.md` L25-90 (row 1237: the crux in
two parts); `library/gap-mini-solve-t-opus.md` L40-70 (row 1229); `library/gap-seed-limit.md` L220-240 ((NS-gap), row 700);
`library/gap-ds-gauge.md` L28-201 (row 691: (W), Theorem W and its proof; check row 693); `library/gap-crux-restate.md`
L66-84 (the five one-scale or all-scale forms C1-C5); `library/gap-vmf-lip.md` L419-560 (row R-b: the seed from Dobrushin
by integration in beta); `library/gap-ymcons-opus.md` L134, L300-326 (row 975: Lemmas META, SVD, VOL).

**What the record fixes (cited, not re-derived).**
- The gap clause reads one open lattice input, (N-phys) (rows 1161, 1179, 1225; check 1232). Modulo the ultraviolet carry
  (UNIV-K) it is a seed of Wilson SU(2) at ONE fixed coupling beta_0 with an explicit side (rows 916-917 (ONE-K), 1180,
  1225, 1229 Step 1.1). Rows 1229 and 1237 ARGUE that this is the 4D analogue of the step that crosses the band in OpenAI's
  2D O(3) paper: a pin-uniform mixing bound at one bare coupling (their Proposition 2.1) turned into a periodic doubling
  criterion at one cutoff (their Proposition 8.1 (a)), then carried by the renormalisation group (rows 1009-1010, reading).
- The lane's only one-scale form that is uniform over boundary values is C3, the Dobrushin-Shlosman block hypothesis (W)
  of row 691 (`gap-crux-restate.md` L72). Theorem W (row 691, check 693: no statement fails) turns (W) at one coupling into
  uniqueness and covariance decay AT THAT COUPLING. It does not give the seed: the file says "The gap does not follow from
  anything in this file" (L170) and its decay is weak mixing only (L141). The lane's one derivation of the seed from a
  mixing condition, row R-b (`gap-vmf-lip.md` Section 4), integrates d F / d beta from beta = 0 and so needs the mixing
  condition at EVERY coupling s <= beta (it is the Dobrushin regime beta < 2/9). Row 975 Lemma VOL: a gap alone misses the
  seed by a volume factor; Lemma META: each metastable set adds about 1 to S.
- No engine for the band is on file. About 45 route families have a named failing step (rows 1189, 1194, 1199 tables;
  `parts/gap.md` methods 19-36). Rows 1237-1251 (seven Opus runs of this brief) found none; this worker's own lesson
  (rows 1188-1251) is that a further blind screen is waste.

**Decision.** I do not offer a band engine. I attack the missing link between the two one-scale forms C3 and C1:

> (WS) At one fixed coupling beta, (W) at (R, delta) implies the periodic doubling defect
> Phi_B(a) = 2 F(a, B) - F(2a, B) is at most C beta R M^6 exp(-eps a/2), hence the seed (SEED) at an explicit side
> of order R log R, with no use of any other coupling.

Moves: (i) C3 at one window coupling becomes a PROVED sufficient input of the chain (modulo (ONE-K)/(UNIV-K) and the
account), so the 4D analogue of OpenAI's Proposition 2.1 needs only to be proved at one coupling, in (W) form; this turns
the ARGUED structural claim of rows 1229/1237 into a proved implication for that form; (ii) it replaces R-b's integration
over all s <= beta by a fixed-coupling argument, so a mixing proof at the window alone would suffice. If (WS) failed, C3
would be useless to the chain and should be dropped from the crux list. It is not an engine: it holds for every compact
fibre, so the selective content stays in proving (W) at the window.

**Rule 0a.** `library/open-core.md`: no gap-lane entry (grep gap, seed, Dobrushin, (W): no hit on this lane). FINISH rows
and library: no statement "(W) gives the seed" (greps: `Theorem W` in 20 files, none derives the seed; `weak mixing.*seed`:
only row 975's Lemma META; `effective rank`, `swap path`, `boundary swap`: 0 files; the "(W) gives (PHYS-SEED)" hits of
rows 1032, 1049 and 1019 concern the WALL (W) of row 998, a different statement). Sibling rows 1249, 1252, 1254-1256 at this
pin are on other items or have not chosen.

**Plan.** Section 2: Lemma WS and its proof. Section 3: the explicit seed side; the fixed-coupling (N-phys) instance; what
WS does not give (the volume factor, physical units). Section 4: what the chain now reads, and the next open step.

## 2. Lemma WS: (W) at one coupling bounds the periodic doubling defect (written 2026-11-20T10:56Z by date -u)

**Setting (the lane's, cited).** Wilson SU(2) at beta > 0: density proportional to the product over plaquettes of
exp(beta x_p), x_p = (1/2) tr U_p in [-1, 1], against product Haar measure (`gap-ds-gauge.md` L28: phi_p =
beta (1 - x_p)). Direction 0 is time. B = (Z/M)^3, |B| = M^3. A slice is the set of the 3 M^3 spatial links with lower end
at one time. F(t, B) = log Z(t x B) on the periodic torus (Z/t) x B; S(t; B) = sum over j >= 1 of (lambda_j/lambda_0)^t for
the transfer operator of B (the lane's (TM); `gap-vmf-lip.md` L426-433). The periodic doubling defect is
Phi_B(a) = 2 F(a, B) - F(2a, B). Distances, cubes V_R = L({0,...,R}^4), Lambda°, B_Lambda, (W) at (R, delta) and
eps = ln(1/delta)/(2(R+2)) are those of row 691 (`gap-ds-gauge.md` L28, L85-91).

**Slab and kernel (definitions).** For a >= 2 let Lambda_a be the set of the spatial links with lower-end time in
{1, ..., a-1} and the temporal links with lower-end time in {0, ..., a-1}. Its boundary is the two slices at times 0
and a (every plaquette that meets Lambda_a has its other links in Lambda_a or in those two slices). For slice values D
(time 0) and E (time a) put Z_a(D, E) = integral over G^(Lambda_a) of the product over the plaquettes p that meet Lambda_a
of exp(beta x_p), and gamma_a(. | D, E) the Wilson conditional law on Lambda_a (row 691's gamma_Lambda with Lambda =
Lambda_a). With s(C) = sum of x_p over the spatial plaquettes of a slice C, put
K_a(D, E) = exp(beta s(D)/2) Z_a(D, E) exp(beta s(E)/2), a continuous positive function. Cutting the periodic tori at
slices gives the exact formulas
    Z(a x B) = integral K_a(C, C) dC,        Z(2a x B) = double integral K_a(C, C') K_a(C', C) dC dC'.     (2.1)
(K_a is the kernel of the a-th power of the transfer operator; nothing below uses its spectrum except the D-shape step.)

**Lemma WS (PROVED GIVEN Theorem W (A) of row 691, checked by row 693; by Claude Opus 5.5 here, checked by no one).**
Let Wilson's SU(2) specification at beta satisfy (W) at (R, delta) with R >= 1 and delta < 1. Let M >= R + 4 and let a be
even with a >= 2R + 2. Then, uniformly in the slice values C, C',
    abs( log [ K_a(C,C) K_a(C',C') / (K_a(C,C') K_a(C',C)) ] ) <= 6 pi beta (8R+6) M^6 (sqrt(delta)/(1 - sqrt(delta))) e^(-eps (a/2 - R)),   (2.2)
and therefore
    0 <= log(1 + S(a; B)) <= Phi_B(a) <= 6 pi beta (8R+6) M^6 e^(-eps a/2) / (1 - sqrt(delta)).                  (2.3)

**Proof.**

*Step 1 (exact identity).* By (2.1), Z(a x B)^2 / Z(2a x B) = E[Q(C_0, C_a)], where (C_0, C_a) are the slices at times
0 and a under the Wilson measure of the torus (Z/2a) x B, whose joint density is K_a(C_0, C_a) K_a(C_a, C_0)/Z(2a x B), and
Q(C, C') = K_a(C,C) K_a(C',C') / (K_a(C,C') K_a(C',C)). So Phi_B(a) = log E[Q] <= sup log Q.

*Step 2 (swap the top slice one link at a time).* List the spatial links of the top slice as y_1, ..., y_N, N = 3M^3.
Given C, C', let C^(k) equal C' on y_1, ..., y_k and C on the other links (C^(0) = C, C^(N) = C'). For a bottom value D put
l_k(D) = log K_a(D, C^(k)) - log K_a(D, C^(k-1)). Then log K_a(C, C') - log K_a(C, C) = sum_k l_k(C) and
log K_a(C', C') - log K_a(C', C) = sum_k l_k(C'), so
    log Q(C, C') = sum over k = 1..N of [ l_k(C') - l_k(C) ].                                                  (2.4)
(K_a is used only with the bottom in the first slot and the top in the second; no symmetry of K_a is needed.)

*Step 3 (one swap is a bounded local derivative).* Fix k, write E = C^(k-1), E' = C^(k), g = E(y_k), g' = E'(y_k).
Exactly one plaquette meets both y_k and Lambda_a: the temporal plaquette p_k with top edge y_k; its other three links
(the parallel spatial link at time a-1 and the two temporal links with lower end a-1) lie in Lambda_a. The spatial
plaquettes through y_k meet no link of Lambda_a, and the temporal plaquette above y_k is outside the slab. So
    l_k(D) = (beta/2)(s(E') - s(E)) + log Z_a(D, E') - log Z_a(D, E),
and the first term does not depend on D. Take a minimizing geodesic g(theta) = g exp(theta X), theta in [0, 1], from g to
g' in SU(2) = S^3 (unit quaternions, bi-invariant metric of the unit sphere; length d = abs(X) <= pi), and let E(theta)
be E with value g(theta) at y_k. Only x_(p_k) depends on theta, so
    log Z_a(D, E') - log Z_a(D, E) = beta * integral over theta in [0,1] of E_(gamma_a(. | D, E(theta)))[h_theta] dtheta,
h_theta = d x_(p_k)/d theta. Bound on h_theta: after a cyclic permutation, x_(p_k) = Re(q(theta) w) or Re(q(theta)^(-1) w)
with q(theta) = g (cos(theta d) + u sin(theta d)), u a unit pure quaternion, w a unit quaternion. The derivative of
cos(theta d) + u sin(theta d) is d u (cos(theta d) + u sin(theta d)), so h_theta = +- d Re(r) for a unit quaternion r, and
abs(h_theta) <= d <= pi. Hence for two bottoms D, D' (same top path),
    abs(l_k(D) - l_k(D')) <= beta * sup over theta of abs(E_(D,E(theta))[h_theta] - E_(D',E(theta))[h_theta])
                           <= 2 pi beta * sup over tops E~ of TV( law of the three Lambda_a-links of p_k under gamma_a(.|D,E~),
                                                                 the same under gamma_a(.|D',E~) ).               (2.5)

*Step 4 (the middle slice shields the top).* Let L be the slice at time t_L = a/2. Call a link of Lambda_a upper if it is
a spatial link with time > t_L or a temporal link with lower-end time >= t_L, lower otherwise. A temporal plaquette between
times t and t+1 contains the spatial links at t and t+1 and the temporal links with lower end t; so every plaquette that
meets an upper link has its other links upper, in L, or in the top slice, and every plaquette that meets a lower link has
its other links lower, in L, or in the bottom slice. The density of gamma_a(. | D, E) is therefore a product
f_low(lower, L; D) f_up(upper, L; E): given L, the upper links are independent of the lower ones and of D. The three
Lambda_a-links of p_k are upper (a - 1 > t_L because a >= 4). So for every bounded function h of upper links,
abs(E_(D,E) h - E_(D',E) h) <= osc(h) TV(law of L under gamma_a(.|D,E), law of L under gamma_a(.|D',E)), and the TV in
(2.5) is at most the TV of the laws of L.

*Step 5 (Theorem W (A) on the slice L).* Work on the torus (Z/2a) x B; all its sides are at least R + 4 (2a >= 4R + 4,
M >= R + 4), as Theorem W (A) on a torus requires (`gap-ds-gauge.md` L147, proof of (C): "it uses only that each cube with its
boundary is embedded"). A cube V_R + b lies in Lambda_a iff its time range [b_0, b_0 + R] satisfies 1 <= b_0 and
b_0 + R <= a - 1. Hence a spatial link at time t is in Lambda_a° iff R + 1 <= t <= a - 1 - R, and a temporal link with lower
end t is in Lambda_a° iff R <= t <= a - 1 - R. Since a >= 2R + 2, L is in Lambda_a°. The links of B_Lambda_a have
lower-end times in [0, R] or [a - R, a], so d(L, B_Lambda_a) >= a/2 - R (the time coordinate alone gives this, also around
the torus), and abs(B_Lambda_a) = 2R(3M^3) + 2R M^3 + 2(3M^3) = (8R + 6) M^3. Theorem W (A), for all boundary values,
    TV(laws of L) <= (sqrt(delta)/(1 - sqrt(delta))) (8R + 6) M^3 exp(-eps (a/2 - R)) =: tau_a.

*Step 6 (sum).* By (2.4), (2.5) and Steps 4-5, abs(log Q(C, C')) <= N * 2 pi beta * tau_a = 6 pi beta M^3 tau_a for all
C, C'. That is (2.2). Step 1 gives Phi_B(a) <= 6 pi beta M^3 tau_a. Since eps (R + 2) = (1/2) ln(1/delta),
sqrt(delta) e^(eps R) <= 1, which gives the right side of (2.3). For the left side (the lane's D-shape, row 705, checked
by row 707, `gap-seed-shape.md` L165-181): F(t, B) = t log lambda_0 + g(t) with g(t) = log(1 + S(t; B)), so
Phi_B(a) = 2 g(a) - g(2a) >= g(a) >= 0 because S(2a; B) <= S(a; B). QED

**What the proof uses, and what it does not.**
- Only the weak mixing that Theorem W proves (decay from the collar B_Lambda, `gap-ds-gauge.md` L141). The collar of the
  top slice is not controlled by Theorem W, and the proof never asks it to be: the bottom's influence on the top collar
  passes through the middle slice L, which lies in Lambda_a°, and Theorem W bounds the law of the WHOLE slice L at once (its
  bound does not grow with abs(S)).
- No other coupling (contrast row R-b, which integrates in beta from 0); no group structure beyond the bound on h_theta
  (the same proof works for any compact fibre with a Lipschitz plaquette term, with 2 pi beta replaced by the Lipschitz
  constant times the diameter); no reflection positivity (only (2.1) and, for the left side of (2.3), the trace formula).
- The bound is uniform over (C, C'), so it bounds every average of Q, not only the periodic one. This is how it avoids
  row 975's Lemma META: a metastable set would make Q large on a set of slices, and (W) forbids that for every boundary.
