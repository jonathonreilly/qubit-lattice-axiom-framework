# FINISH row 872, gap-filter-ls-opus, Claude Opus 5.5 max

(file seeded by the lead; the author writes below)

Author: Claude Opus 5.5 (max effort). FINISH row 872. 4D SU(2) lattice Yang-Mills.
Clone: /Users/jonreilly/ym4d-lead/clone at commit 6ed5bb723e1efd0d44ef0ce331b03d39a019ae1f (pull --ff-only: already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
SA sources: /Users/jonreilly/ym4d-lead/sa at commit 31a47c543775 (Ethan Sussman and Levent Alpoge; Claude and Codex authors of their text).
Status labels: PROVED (mine), READ (path:line), ARGUED, GUIDE, OPEN.

## Target

Make the corrected spin-5/2 filter (row 843 Theorem 3.4, Corollary 3.7, as repaired by
D/library/gap-q8test-check-astra.md) carry (LS) = (E17) of row 860, or show it cannot.
Sub-questions:
(a) What exactly does the corrected filter control, and where does it sit in the transfer L_m?
(b) How can a wrong-class half-integer Z_2 cycle of a time slice avoid the filter at order one
    (the cycle is dense, about 1/3 of edges at beta 2.3, GUIDE)?
(c) What does avoidance cost in the one-slice law? Either prove avoidance is exponentially
    costly in the cycle's wrapping size (crux lemma, stated exactly, attempted as a real proof),
    or construct avoiding configurations and show the filter cannot carry (E17), naming what else
    is needed.
Every step tested against U(1) Coulomb, Q_8 and 2T.

## Plan (at most eight steps; one step per response)

1. READ the exact statements: row 860 (LS), (E17), (HS), odd-sector event; check 864 verdict V1;
   row 843 Theorem 3.4 and Corollary 3.7 with the astra repairs; row 867 Lemma QS and Prop TL;
   SEED-FP (gap-finishline-opus.md lines 110-160).
2. State the corrected filter exactly: operator, space, norm bound, and its slot in L_m.
3. Map the odd-class event onto the filter: which representation content a wrong-class
   half-integer Z_2 cycle forces in the one-slice law, and where the filter acts on it.
4. Avoidance: construct candidate configurations by which a dense wrong-class cycle avoids
   spin-5/2 content (or the filter's slot) at order one.
5. Cost: state the crux lemma (avoidance costs e^{-c |wrap|}) exactly in the one-slice law.
6. Attempt the crux lemma as a proof, or build the counterexample family; name what else is needed.
7. Fact tests: run each step against U(1) Coulomb, Q_8, 2T; record pass/fail.
8. Optional GUIDE numeric (under 300 MB, minutes); then the RESULT line.

## Work log

### Step 1 (READ). The inputs, quoted or paraphrased with locations.

Abbreviations (all under D/library/): Q = gap-q8test-opus.md (row 843); QC = gap-q8test-check-astra.md;
H = gap-hs-max.md (row 860); HC = gap-hs-check-astra.md (row 864); EX = gap-expose-astra.md;
S = gap-sep-opus.md (row 867); SC = gap-sep-check-astra.md; FLN = gap-finishline-opus.md.

- READ EX:94-103, (E1). H = L^2(SU(2)^E)^(SU(2)^V); K = (x)_e C_beta, C_beta = Sum_j r_j Pi_j, r_j = I_(2j+1)/I_1;
  B_m(U) = exp(beta Sum_(p in P) eta_(m,p) x(U_p)) (spatial plaquettes, signs eta = the spatial twist);
  L_m = z^|E| K^(1/2) B_m K^(1/2). Z^m = Tr L_m^t. L_m positive, injective, trace class.
- READ EX:111-152, (E2)-(E3). J_e = sign flip of edge e; E_b (b in F_2^E) selects the parity of 2j on each edge;
  E_b = 0 unless partial b = 0. Theta_omega = Prod J_e^(omega_e), omega the cut cochain; P_- = (1 - Theta)/2;
  Z^m - Z^(m+v) = 2 Tr(P_- L_m^t).
- READ EX:575-599, (E16)-(E17). p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr L_m^a = (1 - R_m(v_(1i)))/2 (time period t = a);
  Q_F = max over m_2 = 0, i = 3, 4. (E17): Q_F <= C a^p eta_*^(a/2), 0 < eta_* < 1 (from S_ev >= eta_*^a).
  "Neither (E17) nor (FQ) is proved here."
- READ H:102-111, Lemma OS. One-slice law P_m(j_e = j_e, e in S) = E_mu[Prod_(e in S) d_j r_j(beta) chi_j(U_p(e)) / k_beta(U_p(e))],
  p(e) the timelike plaquette over e between times 0 and 1, k_beta = Sum_j d_j r_j chi_j (normalized e^(beta x)).
- READ H:168-172, Proposition P1 (checked HOLDS, HC:232). Theta_omega = (-1)^(N_h(cut)); p_m(t) = P_m(N_h(cut) odd)
  = (1/2)(1 - E_mu[exp(-2 beta Sum_(e in cut) x(U_p(e)))]). The half-integer edges of a slice form a Z_2-cycle C;
  (E17) says the omega-class of C vanishes except with probability C a^p eta_*^(a/2).
- READ H:174-179, Proposition P2 (checked HOLDS). 0 <= Tr(P_- L^t) - Tr(P_- Pi_low L^t) <= e^(-c|E|) Tr(P_+ L^t).
  So (LS) = (E17) up to e^(-c|E|).
- READ H:115-119, Lemma DS (checked HOLDS AFTER CORRECTION). On plaquette-separated S:
  P(j_S) <= P(0_S) Prod d_j^2 r_j(beta) r_j(5 beta).
- READ S:458-480, Lemma QS (checked HOLDS, SC:41). |E_(nu_p)[chi_j(U_p)]| <= d_j E_(nu_p)[Prod_(i=1..4) r_j(beta rho_i)]
  <= d_j r_j(5 beta)^4; rho_i = |A_i| <= 5 the staple-sum norms of the four links of p.
- READ S:534-541, Proposition TL, with SC:129-139 correction. For any set R of time-0 edges,
  E_m[(-1)^(N_h(R))] = Z_m(flip R)/Z_m: the insertion is the disorder surface Sigma_R (dual plaquettes of p(e), e in R)
  with boundary partial Sigma_R; a wrapping closed component records the global twist (= P1).
- READ Q:191-211, Theorem 3.4 (checked: (i)-(iv),(vi) HOLDS QC:264; (v) HOLDS AFTER CORRECTION of arithmetic QC:66).
  H = V_(5/2) = Sym^5 V. (i) SU(2): C_(beta,H) = r_(5/2) I_H; on H' = V (x) Sym^6 V, norm r_(5/2) <= M(beta).
  (ii) Q_8: C^(Q_8) = r^(Q_8)_V I_H. (iii) 2T: H = V + V' + V''; C^(2T) = r^(2T)_V on the V copy.
  (iv) U(1): weight vectors x^3y^2, x^2y^3 of H have eigenvalue I_1/I_0. (v) r_(5/2) <= M < r^(2T)_V <= r^(Q_8)_V
  and M < I_1/I_0, every beta > 0. Here "C_(beta,W)" is convolution by the normalized class kernel k_beta acting on a
  G-module W (Q:28): the one-plaquette kinetic operator restricted to a charged space.
- READ Q:219, Corollary 3.7. On H_2 = V (x) Sym^4 V = V_(3/2) + V_(5/2), SU(2) norm r_(3/2) < r^(2T)_V <= r^(Q_8)_V,
  and r_(3/2) < I_1/I_0, every beta > 0.
- READ Q:249-251, 4.1 (a) (checked HOLDS, QC:412). On an edge in a centre-odd block of spin j >= 5/2, C_beta acts as
  the scalar r_j <= r_(5/2) <= M: the filter is an exact factor of L_m in every kinetic step, at original
  normalization. QC:431: "This does not give an upper bound for the full L_m by M: B_m mixes edge spins."
- READ QC:449-470, 4.1 (b) FAILS as an L^2 restriction map; only the algebraic identity on finite sums of matrix
  coefficients holds. It "does not compare the two full L2 transfers or their normalized Gibbs laws."
- READ QC:472-486. "largest defect at (5/2, V)" FAILS: spin 7/2 also contains V for Q_8, 2T, with larger defect.
- READ Q:279 with QC:512-526, 4.3 (HOLDS AFTER CORRECTION). TR's (G20)-(G21): the flat wrapping plane of spin-1/2
  plaquettes contributes 2 z^(N_p) r_(1/2)^A to Z^m - Z^(m+v) with no edge above spin 1/2. Exposure is not mandatory.
- READ HC:199-212, verdict V1 FAILS. The filter's hypothesis is a bound on the charged space Sym^5 V; U(1) restricted
  there contains charges +-1, +-3, +-5 and has norm >= I_1/I_0 > M. So U(1) does not satisfy that bound. "This note
  does not prove that the actual filter together with those estimates cannot imply (LS). It also does not prove that
  they can." Also: masslessness of a matching model does not by itself negate (E17); a bridge is needed (HC:207).
- READ HC:214-221, V2 HOLDS only in limited form: high-spin exposure is not mandatory for every odd configuration.
  "A small one-slice marginal density does not bound the probability of visiting that set over an arbitrarily long
  history, its contribution conditional on winding, or its effect on spectral splitting." GUIDE numbers stay GUIDE.
- READ H:189 (GUIDE, single seed, 8^4 heat bath; not a theorem): one-slice densities at beta = 2.3: spin 1/2 0.327,
  spin 3/2 1.3e-3, odd spin >= 5/2 below 6e-7.
- READ FLN:118-120 (SEED-FP): the real object is the bare Wilson transfer along first passage; FLN:149: (E17) is a
  fixed-coupling statement (the order-one window is bare beta_W about 2.3-2.6).
- Do not use: S's test T3 (SC:199, FAILS); relative (HA) (row 871).

Geometry fixed by these definitions (PROVED from EX (E3) and P1). The time period is t = a; the cut is a spatial
coordinate plane transverse to direction i in {3, 4}; P_- is the event that the half-integer cycle C of the time-0
slice crosses that plane an odd number of times, i.e. C has odd winding in direction i. "Wrapping size" below means
L_i in {c, d}, and also the transverse area of the cut.

### Step 2 (PROVED, from the READ definitions). What the corrected filter controls, and where it sits in L_m.

Notation. On one edge, L^2(SU(2)) = (+)_j V_j (x) V_j*. Call a block "high" if j is a half-integer >= 5/2
(centre-odd, j in {5/2, 7/2, ...}), "low" otherwise. Pi_hi,e is the projection of edge e on its high blocks.
C_beta = C_lo + C_hi with C_hi = Sum_(j high) r_j Pi_j. N_hi = Sum_e Pi_hi,e counts the high edges of one slice.

**Statement F (the corrected filter, as an input to the SU(2) transfer).**
(F1) SU(2) side. On every edge and in every kinetic step, C_beta acts on the spin-j block by the scalar r_j(beta).
     For high j: r_j <= r_(5/2) <= M(beta). As an operator inequality on L^2(SU(2)): C_hi <= M(beta) Pi_hi.
     (Q Theorem 3.4 (i), Lemma 3.1 (a); QC:264.)
(F2) Comparison side. The same 6-dimensional space H = Sym^5 V carries a G-copy of V on which the G-kernel acts by
     r^G_V(beta) > M(beta) (G = Q_8, 2T), and U(1) weight vectors of charge +-1 on which the U(1) kernel acts by
     I_1/I_0 > M(beta). (Q Theorem 3.4 (ii)-(v); arithmetic repaired QC:66-131.) These clauses are about other groups'
     kernels on the same vector space. Inside the SU(2) transfer they enter only through the numbers r_j(beta), j high.
(F3) Location. The filter is the high part of each kinetic factor: K = (x)_e (C_lo,e + C_hi,e), diagonal in the spin
     basis, present at every time step, at the original normalization (Q 4.1 (a), QC:412-431). In the one-slice
     (Lagrangian) form it is the coefficient d_j r_j(beta) of chi_j on the temporal plaquette p(e) (Lemma OS, H:102).
     The same numbers d_j r_j(beta) are also the character coefficients of B_m on spatial plaquettes; there they are
     not eigenvalues, and B_m mixes edge spins (QC:431).
(F4) Not controlled. The filter says nothing about low blocks (spins 0 to 2, including the flux carrier 1/2 and 3/2);
     nothing about how often B_m populates high blocks; and it gives no L^2 comparison of the SU(2) and G transfers
     (QC:449-470). For 2T the first V-channel is spin 5/2 (spin 3/2 restricts to V' + V''); for Q_8 it is spin 3/2.

**Proposition EXP (the exact way the filter enters the odd fraction; PROVED here).** For s >= 0 put
K(s) = (x)_e (C_lo,e + s C_hi,e), L(s) = z^|E| K(s)^(1/2) B_m K(s)^(1/2), p(s) = Tr(P_- L(s)^t)/Tr L(s)^t.
s = 1 is SU(2); s = 0 removes every high block at every time step; s = s_G := r^G_V/r_(5/2) raises the spin-5/2
kinetic factor to the comparison eigenvalue of (F2). Then:
(a) L(s) >= 0, trace class, and commutes with Theta_omega; Tr(P_sigma L(s)^t) >= 0 for sigma = +, -.
(b) For s > 0 and sigma in {+, -, all}:  d/ds log Tr(P_sigma L(s)^t) = (t/s) <N_hi>_(sigma,s),
    where <X>_(sigma,s) = Tr(P_sigma X L(s)^t)/Tr(P_sigma L(s)^t) is the one-slice expectation in sector sigma.
(c) Hence, with Delta(s) := <N_hi>_(-,s) - <N_hi>_(all,s) (the excess high-edge count of the odd sector per slice),
        log p(s_1) - log p(s_0) = t Int_(s_0)^(s_1) Delta(s) ds/s,   0 <= s_0 < s_1.
(d) Tr(P_sigma L(s)^t) is nondecreasing in s (each sector separately).

*Proof.* (a) K(s) has eigenvalues r_j or s r_j >= 0 with finite multiplicity d_j^2 per edge and Sum d_j^2 r_j < inf,
so it is positive and trace class; B_m is bounded, positive, and commutes with Theta (EX:131-140); K(s) commutes
with Theta because J_e acts on the spin-j block by (-1)^(2j). Then L(s) is positive, and
Tr(P L^t) = ||L^(t/2) P||_HS^2 >= 0 (QC:441). (b) Tr(P L(s)^t) = z^(t|E|) Tr(P (K(s)B)^t) by cyclicity, since P
commutes with K and B. K(s) is a polynomial in s of degree |E| with trace-class coefficients, so the trace is a
polynomial in s. The product rule and cyclicity give d/ds Tr(P (KB)^t) = t Tr(P K'(s) B (K B)^(t-1)), and
K'(s) = Sum_e C_hi,e (x) (others) = (1/s) Sum_e Pi_hi,e K(s), because (C_lo,e + s C_hi,e) Pi_hi,e = s C_hi,e.
Finally Tr(P Pi_e (KB)^t) = Tr(P Pi_e M^t) with M = K^(1/2) B K^(1/2): write (KB)^t = K^(1/2) M^(t-1) K^(1/2) B,
move K^(1/2) B to the front, and use that Pi_e and P commute with K^(1/2) and with each other. Each term
Tr(P Pi_e L^t) is >= 0 by (a) applied to the projection P Pi_e. (c) Subtract (b) for sigma = - and sigma = all and
integrate; near s = 0 the integrand is bounded because both traces are polynomials with positive constant terms
(the s = 0 odd sector contains the spin-1/2 flat plane of Q 4.3, so its trace is > 0). (d) (b) with <N_hi> >= 0. QED

Reading. The filter changes the odd fraction only through Delta, the excess number of high edges that the odd
sector carries in one slice over the full ensemble. The value r_(5/2) itself does not bound Delta from below. The
identity holds verbatim for U(1), Q_8, 2T with any subset of their own blocks in place of "high" (group-blind; it is
an identity, not a confining input). The "full history" worry of HC:216 is inside the identity: the factor t
collects every time step.

### Step 3 (PROVED). The odd-class event meets the filter only through a covariance; the crux lemma stated exactly.

**Lemma 3.1 (the excess is a one-slice covariance on the cycle; PROVED).** High blocks are half-integer, so every
high edge lies on the cycle C of half-integer edges, and N_hi = #{e in C : j_e >= 5/2}. P_- = Pi_{N_h(cut) odd}
(P1) and N_hi are both diagonal in the edge spins, so with P_(m,s) the one-slice law of L(s),
    Delta(s) = E_(m,s)[N_hi | C has odd winding in direction i] - E_(m,s)[N_hi]
             = Cov_(m,s)(N_hi, 1_odd) / p(s) = Sum_e Cov_(m,s)(1{j_e >= 5/2}, 1_odd) / p(s).
*Proof.* <X>_(-,s) = Tr(P_- X L^t)/Tr(P_- L^t) is the conditional expectation in the positive one-slice law
(Q 4.1 (c), QC:441) when X is a spin function; expand. QED
So "the wrong-class cycle avoids the filter" has an exact meaning: its high-spin edges are not more frequent than
in the full ensemble, Cov(N_hi, 1_odd) <= 0 or small.

**Crux Lemma EXC (the filter carries (E17); OPEN).** There are an order-one interval I in the window 2.3-2.6,
a number s_* > 1 (the natural choice is s_* = s_G = r^(2T)_V/r_(5/2), the comparison eigenvalue of (F2)) and c_0 > 0
such that for all beta in I, all admissible tori (a, a, c, d), twists m with m_2 = 0 and i in {3, 4}, at t = a,
        Int_1^(s_*) Delta(s) ds/s >= c_0.
Area form EXC-W: Delta(s) >= delta L_i on [1, s_*], with delta > 0 (avoidance costs at rate delta per unit wrapping
length).

**Proposition 3.2 (EXC carries (E17), and that is all it carries; PROVED).**
(a) EXC implies (E17) with C = 1, p = 0, eta_* = e^(-2 c_0); EXC-W implies p(1) <= exp(-delta log(s_*) a L_i),
    an area law in the (time, i) plane with tension delta log s_*.
(b) For each fixed s_* > 1: EXC with constant c_0 holds iff p(1) <= e^(-c_0 a) p(s_*). So the filter carries (E17)
    exactly when true SU(2) is exponentially more confining, in the period a, than SU(2) with its high kinetic
    factors raised by s_*.
(c) If p(1) >= p_min > 0 on a family of tori, then Int_1^(s_*) Delta ds/s <= log(1/p_min)/a on that family.
*Proof.* Proposition EXP (c) with s_0 = 1, s_1 = s_*: p(1) = p(s_*) exp(-a Int_1^(s_*) Delta ds/s), and
0 <= p(s_*) <= 1 because 0 <= Tr(P_- L^t) <= Tr L^t (Prop EXP (a)). All three parts are rearrangements. QED

Reading of (b). EXC is strictly stronger than (E17): besides (E17) it asks that the boosted model be exponentially
less confining. The filter's eigenvalue r_(5/2) never appears in the bound; only the response of the odd sector to
raising it does. Any proof of EXC must therefore show that the wrong-class cycle uses high spins more than the vacuum
does, when they are made cheaper.

Fact tests of Proposition EXP and Lemma 3.1 (PROVED as identities; no confining claim). Both hold verbatim for
U(1) (high := odd charges |n| >= 3, or any set of odd charges), Q_8 and 2T (high := any set of centre-odd blocks).
Part (c) shows that the EXC analogue fails in every theory whose odd fraction stays of order one: this is the U(1)
Coulomb and frozen Q_8, 2T expectation (phase inputs recalled, not proved: HC:205-210). That is a tautology, not
evidence. A proof of EXC must use something those theories lack; Step 6 asks what.

### Step 4. Avoidance: the configurations by which a wrong-class cycle avoids the filter.

**Construction A (the wrapping Wilson line; PROVED).** Let gamma be a closed edge path wrapping direction i once
(it crosses the cut once), and w_gamma = (1/2) tr Prod_(e in gamma) U_e, a bounded gauge-invariant multiplication
operator. Then Theta w_gamma = - w_gamma Theta, so w_gamma maps P_+ H onto a subspace of P_- H. In the spin basis,
multiplication by U_e in the defining representation maps the spin-j block of e into blocks j +- 1/2
(V_j (x) V_(1/2) = V_(j-1/2) + V_(j+1/2)) and leaves every other edge alone. Hence for any state psi with all its
spin components in a set A of configurations, w_gamma psi has components only in configurations that differ from
some sigma in A by +-1/2 on the edges of gamma, and
    N_hi(w-image) <= N_hi(sigma) + #{e in gamma : j_e(sigma) is an integer >= 2}.
In particular from the all-zero configuration w_gamma produces the straight spin-1/2 line: N_hi = 0. Raising N_hi
needs integer spins >= 2 on gamma. Their one-slice density is at most 0.275 (Corollary DS-1, H:121, beta <= 2.5;
checked HOLDS AFTER CORRECTION) and measured about 2e-5 at beta = 2.3 (H:189, GUIDE).
*Proof.* Clebsch-Gordan and Theta_omega = Prod_(e in cut) J_e with |gamma cap cut| = 1. QED

**Construction B (the flat wrapping plane; READ Q:279, QC:512-526).** The flat (time, i) plane of spin-1/2
plaquettes contributes 2 z^(N_p) r_(1/2)^A, A = a L_i, to Z^m - Z^(m+v), with no edge above spin 1/2 at any time.

**Construction C (full-history avoidance; PROVED by Proposition EXP (a), (d)).** L(0) has no high block at any time
step. Tr(P_- L(0)^t) > 0 (it contains Construction B) and Tr(P_- L(0)^t) <= Tr(P_- L(1)^t). The cost of
avoidance, in the one-slice law and for the whole history at once, is the exact number
    log p(1) - log p(0) = t Int_0^1 Delta(s) ds/s.

**The order-one avoidance mechanism at the crossover (ARGUED; numbers GUIDE).** Compare the two ways a wrapping odd
line can live in the boosted model L(s_*), where the spin-5/2 kinetic factor equals r^(2T)_V (about 0.49 at beta
2.3, GUIDE) and the spin-1/2 factor is r_(1/2) (0.479, GUIDE):
- A spin-1/2 line moves by one spatial spin-1/2 plaquette of B_m, coefficient d_(1/2) r_(1/2)(beta) = 0.96: it is
  soft, and its free energy per unit area is the true string tension, recalled near 0.14 at beta = 2.3 (GUIDE,
  literature value, not re-read), far below its bare cost log(1/r_(1/2)) = 0.74.
- A spin-5/2 line moves only by a spin-5/2 plaquette of B_m, coefficient d_(5/2) r_(5/2)(beta) = 6 x 0.0018 = 0.011
  (B_m is not boosted: Statement F3), or through fragments 2 + 1/2, 3/2 + 1, whose integer and spin-3/2 parts keep the
  unboosted factors r_2 = 0.0099, r_(3/2) = 0.045 (GUIDE decimals). It is rigid: its cost per unit area stays near
  log(1/r^(2T)_V) = 0.72.
So raising the filter channel to the comparison value opens a wrapping channel of weight about e^(-0.72 A) next to an
existing one of weight about e^(-0.14 A). The relative change of the odd weight is about e^(-0.58 A). By Proposition
3.2 (b) this means Int_1^(s_*) Delta ds/s is exponentially small in A, not >= c_0. In words: the cycle avoids the
filter by entropy. Its cheap moves are spin-1/2 moves, and the filter does not act on them.

Second effect, same size class (ARGUED, GUIDE). Even a localized spin-1/2 line changes the high count only where it
crosses vacuum edges of integer spin >= 2 (Construction A) or high spin. Its excess per unit length is then of order
rho_2 q - rho_(5/2)(s), with rho_2 about 2e-5, rho_(5/2)(1) below 6e-7 (H:189, GUIDE) and q a Clebsch-Gordan and
kinetic branching fraction. Along [1, s_*] rho_(5/2)(s) grows with s, so the sign of Delta(s) is not fixed. Either way
the filter's share of the exponent is of order 1e-4 x log(s_*) per unit area, against about 0.14.

Contrast with strong coupling (ARGUED; leading-order surface counting, not a cluster-expansion proof). For small beta
the odd sector is dominated by flat planes, a flat spin-j torus plane has weight r_j^A exactly (d_j^(Euler char 0)),
and r^(2T)_V - r_(1/2) = beta^5/7680 + O(beta^7) (Q:279). The boosted spin-5/2 plane then competes on equal terms and
p(1)/p(s_G) is about (r_(1/2)/r^(2T)_V)^A = exp(-A beta^4/1920 (1 + O(beta^2))). There EXC-W holds with
delta log s_G about beta^4/1920: the filter carries a real but tiny area-law factor, because planes are rigid anyway.
At the crossover the flux carrier is soft, the filter channel is rigid, and this factor disappears.

### Step 5. Attempted proof of EXC, where it breaks, and a correction to Step 4.

Decimals used (GUIDE, by hand from the series; no proof rests on them): at beta = 2.3, I_1 = 2.0978,
r_(1/2) = 0.4793, r_(3/2) = 0.0450, r_2 = 0.00993, r_(5/2) = 0.001846; r^(2T)_V = (4 sinh b + 16 sinh(b/2)) /
(2(2 cosh b + 6 + 16 cosh(b/2))) = 0.4841 (Lemma 1.2, Q:37-53); s_G = 0.4841/0.001846 = 262, log s_G = 5.57.
Correction to Step 4: there "about 0.49" should read 0.484; log(1/0.484) = 0.726.

**5.1 Exact rescaling (PROVED).** C_lo + s C_hi = s^(Pi_hi) C_beta on each edge, so K(s) = s^(N_hi) K(1) with commuting
factors, and L(s) = z^|E| K(1)^(1/2) s^(N_hi/2) B_m s^(N_hi/2) K(1)^(1/2). The boost is a one-slice "fugacity" s per
high edge, inserted at every time step.

**5.2 Large-t reading (PROVED for a fixed spatial torus with simple top eigenvalues).** Let lambda_sigma(s) be the
top eigenvalue of L(s) on P_sigma H and psi_sigma its unit eigenvector. lambda_sigma is also the top eigenvalue of
B^(1/2) K(s) B^(1/2) (same nonzero spectrum). With K'(s) = (1/s) K^(1/2) N_hi K^(1/2) and psi = K^(1/2) B^(1/2) phi /
lambda^(1/2), first-order perturbation gives d log lambda_sigma/ds = <psi_sigma, N_hi psi_sigma>/s. So as t -> infinity
on a fixed torus, Delta(s) -> <N_hi>_(psi_-) - <N_hi>_(psi_+): the high-spin content of the lowest odd-flux state minus
that of the vacuum. EXC says that the flux energy log(lambda_+/lambda_-) drops by at least c_0 when the high factors
are raised by s_*.

**5.3 The variational attempt (fails; PROVED that this route gives only volume-order bounds).** A lower bound on
lambda_-(s_*) by the trial vector psi_-(1) needs a lower bound on the high-spin weight of psi_-(1). An upper bound on
lambda_+(s_*) needs the vacuum's response. By 5.1 the only response bound free of state information is
L(s) <= s^|E| L(1) on each sector (N_hi <= |E|), so the best such bound is lambda_+(s_*) <= s_*^|E| lambda_+(1).
This is the extensive cost of EX (E18) again: Delta is a difference of two extensive one-slice expectations, and any
argument that bounds the two sectors separately loses a factor e^(O(|E|)). To prove EXC one must control the
difference itself, which is a statement about where the odd sector differs from the vacuum.

**5.4 The localization dichotomy (ARGUED).** Two ways an odd sector can differ from the vacuum:
- Localized flux (a tube of bounded width, the confining picture). Then the tube changes the high count only along
  its length, at first order: Delta about delta(s) L_i, with |delta| of order rho_2 q + rho_(5/2)(s) (Step 4, second
  effect). If delta(s) > 0 on [1, s_*], EXC-W holds and Int Delta ds/s grows like L_i >= a (admissible tori have
  c, d in {a, 2a}, READ gap-ext-astra.md:81). Then EXC holds for all large a, with an area-law share of order
  1e-4 log s_* per unit area (GUIDE estimate).
- Spread flux (the U(1) Coulomb picture). The odd state shifts the field on all A_perp L_i edges by about 1/A_perp.
  By the centre symmetry j -> j, m -> -m of the vacuum spin law (charge symmetry n -> -n for U(1)), the first-order
  change of a high count cancels, and Delta is of order L_i/A_perp = O(1/a). Then Int Delta ds/s = O(1/a) and EXC
  fails (consistent with Proposition 3.2 (c)).
So a proof of EXC must first prove that the wrong-class cycle is localized. Localization is the content of (E17)
itself. The filter adds nothing before that step, and after it adds a sign-indefinite share of order 1e-4.

**Correction to Step 4.** Step 4 said that Int_1^(s_*) Delta ds/s is exponentially small in A. That holds only for
the new rigid spin-5/2 wrapping channel (relative weight about e^(-0.58 A)). The dressing of a localized spin-1/2
tube (Step 4, second effect) gives a term of order L_i x 1e-4 x log s_*, which is not small for L_i of order 1e4 and
larger. So EXC is not refuted. Its truth depends on the sign of delta(s) on [1, s_*], and it presupposes localization.

### Step 6. Verdict on the filter route, and what else is needed.

Wording fix to 5.4 (ARGUED). For SU(2) the "shift" of the spread case is not a spin shift. Gauge invariance gives
<E^a_e> = 0 in every physical state, so a spread odd state changes each edge's gauge-invariant data (for example
the Casimir j(j+1)) only at second order in the local flux 1/A_perp. The total change of a high count is then of
order A_perp L_i / A_perp^2 = L_i / A_perp, as for U(1). The conclusion of 5.4 is unchanged.

**Verdict (ARGUED, with PROVED structure).**
(V-a) PROVED: the corrected filter enters the odd fraction only through the response Delta (Proposition EXP), and it
      carries (E17) exactly when EXC holds (Proposition 3.2). EXC implies (E17); EXC is strictly stronger.
(V-b) PROVED: a wrong-class cycle can avoid the filter at every time step (Constructions A-C); the cost of avoidance
      in the one-slice law, for the whole history, is exactly t Int_0^1 Delta ds/s.
(V-c) ARGUED: avoidance at order one is by entropy. At the crossover the flux carrier (spin 1/2) is soft, with
      spatial move coefficient 0.96, while the filter channel is rigid (0.011), even when its kinetic factor is
      raised to the 2T value. The new wrapping channel this opens has relative weight about e^(-0.58 A).
(V-d) ARGUED, GUIDE size: what is left of the filter's effect is the dressing of a localized tube by vacuum spins
      >= 2, of order 1e-4 x log s_G per unit wrapping area, with undetermined sign along the boost path, against a
      recalled string tension near 0.14. So even granting localization, the filter supplies well under 1% of the
      area-law exponent, and possibly a negative share.
(V-e) ARGUED: any proof of EXC must first prove that the wrong-class cycle is localized (5.4). Localization is what
      (E17) needs, so the filter cannot carry (E17) as an independent input. It is a spectator channel of the odd
      sector at the crossover. This does not discard the filter: HC:212 stands (it is a real SU(2)-versus-G
      separation), and at strong coupling it does carry a factor about exp(-A beta^4/1920) (Step 4, ARGUED).

**What else would be needed (OPEN; candidate inputs, not consequences).**
(N1) Localization of the wrong-class cycle: in the odd sector the excess over the vacuum sits in a tube of bounded
     width, uniformly in the admissible tori. It must fail for U(1) Coulomb, where the flux spreads (5.4), and for
     frozen Q_8, 2T, where p tends to 1/2 (recalled phases, HC:205-210).
(N2) An input on the flux carrier's own channel, not on spin 5/2. At beta = 2.3 the kinetic factors of the carrier
     are nearly equal, r_(1/2) = 0.479 against r^(2T)_V = 0.484 (GUIDE), so a kinetic filter on the carrier separates
     nothing. The candidate SU(2)-versus-2T difference for the carrier is its environment: the typical value of the
     Lemma QS coefficient E[Prod_i r_(1/2)(beta rho_i)] (READ S:458-480; worst case r_(1/2)(5 beta)^4 = 0.580, typical
     value about 0.27 by row 860's GUIDE) against a frozen 2T value near 1. A typical-value bound of that kind is
     OPEN (H:250).
(N3) An input against integer flux, so that the spread state of U(1) is not available. In SU(2) two spin-1/2 lines
     fuse to 0 or 1 and the conserved charge is the Z_2 class only (EX:131-152). How to turn this into an estimate is
     OPEN; HC:220 records that this is a proposed strategy, not a consequence of the checked identities.
(N4) If (N1) is proved, the filter can still be used: Proposition EXP for the spin-1/2 channel and for the high
     channel then measure the tube's spin content, and the filter bounds the high part. That is bookkeeping after
     localization, not a source of it.

### Step 7. Fact tests of every step, and small repairs.

Repairs (PROVED unless marked).
- Proposition EXP (c), positivity at s = 0: take psi the gauge-invariant state with spin 1/2 on a simple wrapping line
  gamma and spin 0 elsewhere (it lies in the low blocks and in P_- H). Then <psi, L(0) psi> =
  z^|E| <K0^(1/2) psi, B_m K0^(1/2) psi> > 0 since B_m >= e^(-beta|P|), and <psi, L(0)^t psi> >= <psi, L(0) psi>^t
  (spectral Jensen for A >= 0, t >= 1). So Tr(P_- L(0)^t) > 0. This replaces "contains the flat plane".
- Construction A: take gamma a simple closed path, so each edge of gamma changes once.
- Step 6 (N2): the "typical value about 0.27" of row 860 is the one-link (Lemma DS) environment coefficient against its
  worst case r_(1/2)(5 beta) = 0.87 (H:198, H:250, GUIDE); the four-link Lemma QS worst case is 0.580 (S:336). The
  typical value of the four-link QS coefficient is not quoted here.

| Step | U(1) Coulomb | Q_8 | 2T | Use made of it |
|---|---|---|---|---|
| Statement F (filter) | (F2): charge +-1 vectors of Sym^5 V have I_1/I_0 > M (HC:203). U(1) has no separate spin-5/2 channel of its own. | Sym^5 V is V-isotypic: r^(Q_8)_V on all of it. | V-copy inside Sym^5 V with r^(2T)_V. | Inputs only; READ, checked. |
| Prop EXP, Lemma 3.1 | Hold verbatim (high := odd charges >= 3). | Hold (any centre-odd blocks). | Hold. | Identities. No confining claim, so no test to pass. |
| Prop 3.2 | The EXC analogue fails whenever p stays of order one (part (c)); the U(1) Coulomb odd fraction on (a, a, c, d) is expected of order one (recalled; the bridge from the Villain theorem to this fraction is missing, HC:205-207). | Frozen: p -> 1/2 expected (recalled), so the analogue fails. | Same. | Shows EXC is a confinement statement, not a reduction. |
| Construction A | Charge-1 line raises the |n| >= 3 count only at |n| >= 2 edges: same. | V-line; Q_8 has one centre-odd irreducible, so no "high" channel distinct from the carrier. | V-line; V', V'' sit in spin 3/2. | Group-blind. Avoidance is available in every group. |
| Construction B | Flat charge-1 plane, (I_1/I_0)^A. | (r_V)^A. | (r_V)^A. | Group-blind (READ Q:279). |
| (V-c) rigidity | Charge-3 line also rigid (coefficient I_3/I_0 small): same mechanism. | Not applicable: the alias is the carrier. | Same. | Explains why the filter is a spectator in SU(2); it is not a confining input and is not used as one. |
| (V-d), 5.4 dichotomy | Spread flux gives Delta = O(L_i/A_perp): EXC fails, as it must. | Frozen: no localized tube, Delta -> 0 expected. | Same. | Reduces EXC to localization (N1). |
| Strong coupling factor | U(1) has no second odd channel with the carrier's weight; analogue absent. | No distinct channel. | No distinct channel. | ARGUED only; outside the window. |

Other fact tests from the brief. No step uses a Dobrushin bound (single-site cap 2/3, vertex-block cap 0.775), a
background-uniform layer twist bound (cap 4 G_3 = 1.0109) or (AN1). No step uses S's test T3. Nothing here touches
relative (HA) (row 871). The order-one window enters only through the GUIDE decimals at beta = 2.3; Propositions
EXP and 3.2 hold at every beta > 0 and every twist with positive temporal weights.

GUIDE run: SKIPPED. The quantity that would test (V-d) is Delta(1) = E[N_hi | odd] - E[N_hi] in the one-slice law
on a small twisted torus. It needs the odd-sector estimator E_m[X 1_odd] = (E_m[X] - (Z^(m+v)/Z^m) E^(m+v)[X'])/2
with the Lemma OS factors and a measured twist ratio, and the high counts are of order 1e-4 per slice. A run of a few
minutes would not resolve a difference of that size, and an unchecked sampler would add nothing (compare SC:199).

### Step 8a. Re-read corrections, and the spin-3/2 side of Corollary 3.7.

READ H:149-155 (GUIDE, 8^4, 200 configurations, unverified): at beta = 2.3, rho_0 = 0.6373, rho_(1/2) = 0.3267,
rho_1 = 0.0347, rho_(3/2) = 1.26e-3, rho_2 = 2.1e-5, rho_(5/2) below 6e-7; environment coefficients
e_j = E_nu[chi_j(U_p)]/d_j: e_(1/2) = 0.267, e_1 = 0.036, e_(3/2) = 0.0028, e_2 = 1.3e-4.

Correction to the Step 7 repair of (N2). e_(1/2) = 0.267 is the full environment coefficient of a spin-1/2
plaquette. Lemma DS bounds the same object by r_(1/2)(5 beta) = 0.87 (one link integrated), Lemma QS by
r_(1/2)(5 beta)^4 = 0.580 (four links). So the typical-value gap for the carrier is 0.267 against worst cases 0.87
and 0.58 (GUIDE value; the bounds are PROVED).

Correction to 5.4, SU(2) form of the spread case (ARGUED). The one-slice law is diagonal in the spins, so "spread"
means: conditioning a dense, weakly correlated half-integer cycle on odd crossing parity of the cut. The parity of
many weakly dependent bits is close to uniform, so conditioning on it moves each local marginal by an amount that
decays with A_perp. Then Delta is small and EXC fails. This is the deconfined picture (p near 1/2). Only a confined
odd sector, where odd parity forces a localized excess, gives Delta of order L_i. The dichotomy of 5.4 stands.

**The spin-3/2 side (Corollary 3.7; same structure, larger size).** Corollary 3.7's SU(2) side is r_(3/2) on
H_2 = V_(3/2) + V_(5/2). Its Q_8 and U(1) comparisons sit in spin 3/2 (Q Corollary 3.5); its 2T comparison sits in
spin 5/2. Proposition EXP and 3.2 hold with high' = {3/2, 5/2, ...} (PROVED: the proof never used which blocks are
high). The boost factors are s' = r^(Q_8)_V/r_(3/2) = 0.614/0.045 = 13.6 and I_1/I_0 / r_(3/2) = 0.741/0.045 = 16.5
(GUIDE decimals; r^(Q_8)_V = sinh b/(cosh b + 3), Lemma 1.2).
Size of the dressing term for a localized line (ARGUED; GUIDE inputs). Two crude accountings bracket it:
- Trial state w_gamma psi_0 (Construction A applied to the vacuum, no kinetic reweighting). Multiplying a spin-j
  matrix coefficient by a spin-1/2 one sends the fraction d_(j+1/2)/(2 d_j) of the norm to j + 1/2: spin 1 -> 3/2 with
  2/3, spin 3/2 -> 1 or 2 always. Excess per unit length: rho_1 (2/3) - rho_(3/2) = 0.0231 - 0.0013 = +0.022.
- Vacuum ratios (the line takes the vacuum's relative weight of 3/2 to 1/2, about 1.26e-3/0.327): excess about
  0.0347 x 0.008 - 0.00126, about -1e-3.
So for Corollary 3.7's channel |delta| is at most about 0.02 per unit length, and the share of the exponent is at most
about 0.022 x log 13.6 = 0.06 per unit area, sign undetermined, against a recalled string tension near 0.14.
For Theorem 3.4's channel the same trial accounting gives rho_2 (6/10) - rho_(5/2), about 1.3e-5 per unit length,
share about 7e-5 per unit area.

Revised (V-d). Spin-5/2 filter (Theorem 3.4): share of order 1e-4 per unit area; a spectator. Spin-3/2 side of
Corollary 3.7: share up to a few hundredths per unit area, possibly a sizable fraction of the exponent, sign
undetermined. In both cases the share is the dressing of a tube that must already be localized, so (V-e) is
unchanged: the filter does not supply localization, and without localization its share vanishes.

### Step 8b. Status lists.

**PROVED (here; not checked by another model).**
1. Statement F: inside the SU(2) transfer the corrected filter is the kinetic factor r_j <= r_(5/2) <= M(beta) on the
   high blocks, diagonal in K at every time step; its comparison clauses (Q_8, 2T, U(1) on Sym^5 V) enter only through
   these numbers. It controls nothing about the low blocks or about how B_m populates high blocks.
2. Proposition EXP: d log Tr(P_sigma L(s)^t)/d log s = t <N_hi>_(sigma,s) in each sector; log p(s_1) - log p(s_0) =
   t Int Delta ds/s; each sector's trace is nondecreasing in s. Valid for any set of blocks and any group (identity).
3. Lemma 3.1: Delta = Cov(N_hi, 1_odd)/p, a one-slice covariance of the high count on the cycle with odd winding.
4. Proposition 3.2: EXC implies (E17) with C = 1, p = 0, eta_* = e^(-2 c_0); EXC-W implies an area law with tension
   delta log s_*; EXC holds iff p(1) <= e^(-c_0 a) p(s_*); EXC fails on any family with p >= p_min > 0.
5. Construction A (the wrapping Wilson line maps P_+ into P_- and raises N_hi only at integer spins >= 2 on gamma) and
   Construction C (the truncated transfer L(0): 0 < Tr(P_- L(0)^t) <= Tr(P_- L(1)^t)).
6. 5.1 K(s) = s^(N_hi) K(1); 5.2 the large-t reading of Delta as the high content of the odd ground state minus the
   vacuum's; 5.3 the only state-free response bound is L(s) <= s^|E| L(1), a volume-order loss.

**ARGUED.** Avoidance at the crossover is by entropy (soft spin-1/2 carrier, rigid filter channel; new-channel weight
about e^(-0.58 A)). The localization dichotomy: Delta is of order L_i only for a localized odd excess; a spread or
dense-random odd sector gives small Delta and EXC fails. Hence a proof of EXC needs localization first, and the filter
cannot carry (E17) as an independent input. Dressing shares: about 1e-4 per unit area at spin 5/2 (Theorem 3.4), up to
a few hundredths at spin 3/2 (Corollary 3.7), sign undetermined. At strong coupling the filter carries a factor about
exp(-A beta^4/1920) (leading-order surface count).

**GUIDE.** The decimals at beta = 2.3 (r_j, r^(2T)_V = 0.484, r^(Q_8)_V = 0.614, I_1/I_0 = 0.741, s_G = 262); row 860's
measured one-slice densities and environment coefficients (single 8^4 runs, unverified, H:149-155); the recalled string
tension near 0.14. No GUIDE run was made in this row.

**READ.** EX (E1)-(E3), (E16)-(E18); Q Theorem 3.4, Corollaries 3.5, 3.7, Sections 4.1-4.4 with QC's repairs; H Lemma
OS, DS, P1, P2, V1, V2 and the GUIDE tables; HC's verdicts V1, V2; S Lemma QS and Proposition TL with SC's corrections;
FLN (SEED-FP); gap-ext-astra.md:81 (c, d in {a, 2a}).

**OPEN.** EXC and EXC-W; the sign of delta(s) on the boost path; (E17) itself; (N1) localization of the wrong-class
cycle, uniform in the admissible tori; (N2) a typical-value environment bound for the carrier (e_(1/2) = 0.267 measured
against the proved worst cases 0.87 and 0.58); (N3) an estimate that uses the absence of an integer-valued flux.

No mass gap is proved here. No repository file was edited. No subagent was used. Credits: Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text, for the account and the Bessel convolution facts used through
Q; Codex gpt-6-astra for the checks QC, HC, SC; Claude Fable 5.2 for row 860; Claude Opus 5.5 for rows 843 and 867.

RESULT: NEGATIVE for the filter as a carrier of (LS) = (E17) (ARGUED), with PROVED structure, by Claude Opus 5.5 (max), not checked — Proposition EXP (PROVED): the corrected spin-5/2 filter is the high-spin part of the kinetic factor K at every time step, and it enters the odd fraction only through the exact identity log p(s_1) - log p(s_0) = t Int Delta(s) ds/s, where s scales the high-spin kinetic factors and Delta = E[N_hi | odd winding] - E[N_hi] is the odd sector's one-slice excess of high edges; so the filter carries (E17) exactly when Crux Lemma EXC (Int_1^(s_*) Delta ds/s >= c_0) holds, which implies (E17) with eta_* = e^(-2 c_0) and is equivalent to true SU(2) being e^(-c_0 a) more confining than SU(2) with boosted high-spin factors (PROVED); wrong-class cycles avoid the filter at every time step (wrapping Wilson-line map, truncated transfer; PROVED), at the crossover they avoid it by entropy because the spin-1/2 carrier is soft and the filter channel stays rigid when boosted (ARGUED), a proof of EXC needs localization of the wrong-class cycle first, which is what (E17) needs (ARGUED), and the filter's share of the area-law exponent is about 1e-4 at spin 5/2 and at most a few hundredths at Corollary 3.7's spin 3/2, sign undetermined (GUIDE inputs); OPEN: EXC, (E17), localization (N1), a typical-value environment bound for the carrier (N2), an input against integer flux (N3).
