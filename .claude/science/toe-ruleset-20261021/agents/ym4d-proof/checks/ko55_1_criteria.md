# ko55_1 — pre-registered criteria (written before checks/ko55_1.py exists)

Owner: KFACTOR_OFF55.md (Opus 5.5 worker, model claude-opus-5-5). Exact integer / Fraction arithmetic only; no floats
in any verdict; no BLAS. Pure python, single thread.

## Objects (definitions the script must implement literally)
Lattice: dimension d, odd L = 3, depth k, coarse torus side T. Level-j sites: Z in (Z/(T L^{k-j}))^d. The level-j block of
a level-j site Z (as level-0 sites): {L^j Z + t : t in {0..L^j-1}^d}. The ROOT of a level-(j+1) block of the level-(j+1)
site Y, as a level-j site: L Y + ((L-1)/2) 1 (block centre). ev^{(j)}: level-0 function -> level-j function,
(ev^{(j)} f)(Z) = f(L^j Z + ((L^j-1)/2) 1). ev^{(j)T} places a level-j function at those level-0 sites.
Level-j 1-forms live on links (Z, mu) from Z to Z + e_mu. d*: (d* v)(Z) = sum_mu [v(Z - e_mu, mu) - v(Z, mu)].
Composite divergence of a chain S = (S_0..S_{k-1}): D(S) := sum_j ev^{(j)T} d*_j S_j (a level-0 function).
Hierarchical routing P^T u (u a level-0 function): for each level j = 0..k-1 and each level-j site Z with parent
Y = floor(Z/L) (componentwise) and root R = L Y + ((L-1)/2) 1: V_j(Z) := sum of u over the level-j block of Z;
gamma(Z) := the level-j axial path from R to Z moving coordinate 1 first, then 2, ..., then d (each step one level-j
link, signed +1 for a step in +mu, -1 for a step in -mu, recorded on the link (min endpoint, mu)); (P^T u)_j := sum_Z
V_j(Z) gamma(Z). Path multiplicity M_gamma := max over level-j links of the number of Z in one level-(j+1) block whose
path uses that link. Plain coarse size in d dimensions: pi_j(v) := L^{(d-1)(k-j)} * max|v| (own units).

## Part A — the routing identity and its sizes (the load-bearing new lemma, Lemma HR of KFACTOR_OFF55)
Cases (d,k,T): (2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),(2,4,1),(4,1,1),(4,2,1). Seeded integer data in [-5,5].
- **A1 (identity).** For random u: D(P^T u)(z) = u(z) at every level-0 site z that is not a level-k root, and
  D(P^T u)(r_X) = u(r_X) - sum_{z in cell X} u(z) at every level-k root r_X. PASS iff exact equality at every site in
  every case.
- **A1-ctl (controls; each must FIRE, i.e. the identity must FAIL):** (i) route to the block CORNER L Y instead of the
  centre while ev keeps centres; (ii) omit the level-1 routing (j = 1) when k >= 2. PASS iff both controls produce at
  least one site with D(P^T u) != the A1 right side, in every case with k >= 2 (control (i) in every case with k >= 1).
- **A2 (vanishing below l and the sup route).** For u = ev^{(l)T} d*_l w, w a random level-l 1-form, every l <= k-1:
  (P^T u)_i == 0 for i < l; and for i >= l: |V_i(Z)| <= 2 d L^{(d-1)(i-l)} max|w| for every Z, and
  max|(P^T u)_i| <= M_gamma * 2 d L^{(d-1)(i-l)} max|w|. Also M_gamma == L^{d-1}(L-1)/2 exactly. PASS iff all hold.
- **A3 (boundary-flux identity, Hoelder route).** For a random level-0 current w and every level-i block (1 <= i <= k-1):
  V_i(Z) for u = d*_0 w equals sum_mu sum_{lines} [w(entry link) - w(exit link)] exactly (entry = the link entering the
  block from the -mu side along the line, exit = the link leaving through the +mu side). PASS iff exact in every case.
- **A4 (mechanism; the hierarchy is load-bearing).** d = 2, T = 1, k = 1..5. Fixed coarse profile: the level-0 current
  w_mu(z) = n^{-(d-1)} W_mu(z) * (scale), realised exactly as integers by taking w_mu(z) := tri(z_{mu'}) with tri a triangle
  wave of period n = L^k and integer slope 1 per own step in coordinate mu' != mu (so the coarse current j^c = n^{d-1} w
  has coarse Lipschitz constant Lip_c = n^{d-1} * n * (own slope 1) / n^{d-1}... the script computes the exact coarse
  Lipschitz constant Lip_c := n^{d-1} * max over adjacent own steps |w(z+e)-w(z)| * n). With u := d*_0 w:
  J_hier(k) := sum_i pi_i((P^T u)_i); J_single(k) := pi_0 of the single-level routing current (every level-0 charge of u
  routed directly to its level-k root along a level-0 axial path, same coordinate order).
  PASS iff (a) J_hier(k) <= d * M_gamma * Lip_c / (L - 1) for every k = 1..5 (the Lemma HR Hoelder-route bound at
  alpha = 1), AND (b) the control fires: J_single(5) >= 10 * J_single(2) and J_single is nondecreasing in k.
  (a) is a rigorous instance of the lemma; (b) shows that routing the same charges in one level-0 step (the shape of
  Gamma_E^T / the (NEUT-box) term) grows with k, so the bound in (a) is not automatic.

## Part B — the constant in the K'_x bound (Bernoulli series)
Exact Bernoulli numbers B_0..B_60 by the standard recurrence (Fractions, B_1 = -1/2). PASS iff
S_60 := sum_{n=1}^{60} |B_n|/n! satisfies S_60 + (4/6^61)/(1 - 1/6) <= 59/100, and |B_n|/n! <= 4/6^n for 2 <= n <= 60.
(The tail bound |B_{2n}|/(2n)! = 2 zeta(2n)/(2 pi)^{2n} <= 4/6^{2n} is a theorem used for n > 60, not checked.)

## Part C — series constants used in the text
L = 3: sum_{m=0}^{M} (m+1) L^{-m} < (L/(L-1))^2 = 9/4 for M = 1..400 and the limit identity holds exactly
(closed form of the partial sum checked exactly); (1316/1000)^4 < 3 (so 1/(3^{1/4} - 1) < 1/(316/1000) < 3165/1000);
sum_{m=0}^{M} L^{-m} < L/(L-1) for M = 1..400. PASS iff all hold.

## Overall
OVERALL PASS iff A1, A1-ctl, A2, A3, A4, B, C all PASS. Any FAIL is reported as FAIL with the failing case; nothing is
re-run with changed criteria. Discriminating power (stated before running): A1 and A3 are exact identities that fail if
the routing, the nesting of roots or the block bookkeeping is wrong (A1-ctl demonstrates two such failures); A2 can fail
if the path multiplicity or the flux count is wrong; A4 (a) can fail if the Hoelder-route bound is wrong, A4 (b) is a
control. No part of ko55_1 tests a nonlinear Yang-Mills estimate, the linear response theory (TW, C2-COF, TOP#), or the
local analytic inputs (LA); those rest on the cited lemmas and on the proofs in KFACTOR_OFF55.

## AMENDMENT 1 (appended 2026-10-29 ~00:24Z UTC, BEFORE checks/ko55_1.py exists; nothing above is edited)
Defect found in A4 as registered above, by re-reading it before writing the script: (1) a current w_mu that depends
only on a coordinate mu' != mu is divergence-free (d*w = 0), so u = 0 and A4 would be vacuous (both sides 0);
(2) control (b) compares RAW growth of J_single, which also holds for J_hier because the test current's amplitude grows
with n, so (b) as written cannot discriminate. A4 is therefore REPLACED by A4' below; the original A4 is not run.
- **A4' (mechanism; replaces A4).** d = 2, T = 1, k = 1..5, n = L^k. w_mu(z) := tri(z_mu) with tri(t) := min(t mod n,
  n - (t mod n)) (integer, period n in the link's OWN coordinate, |slope| <= 1 per own step). u := d*_0 w (not zero).
  s_max := max over all mu, nu, z of |w_mu(z + e_nu) - w_mu(z)| (computed; expected 1). Coarse Lipschitz normaliser
  Lip_c(k) := n^{d-1} * n * s_max (the coarse current j^c = n^{d-1} w moves by <= n^{d-1} s_max per own step, i.e. per
  coarse distance 1/n). J_hier(k) and J_single(k) as defined in A4. rho_hier := J_hier/Lip_c, rho_single := J_single/Lip_c.
  PASS iff (a) rho_hier(k) <= d * M_gamma / (L - 1) for every k = 1..5 (rigorous instance of Lemma HR's Hoelder route at
  alpha = 1), AND (b) control fires: rho_single(5) >= 10 * rho_single(2) (single-level routing of the same charges grows
  relative to the same normaliser, the hierarchical routing does not).
OVERALL now reads: A1, A1-ctl, A2, A3, A4', B, C all PASS.
