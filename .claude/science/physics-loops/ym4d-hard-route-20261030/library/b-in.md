lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T02:47Z

# (B-in): the sealing construction on D_2 beside S

Queue row 389 (`b-in`). Started 2026-11-06T14:47Z at commit cf6677779. Proved by Claude, not yet checked by the other model. Complete: the Result is at the end.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number; Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier lanes here: `library/ca-claude.md` (Lemmas A, B), `gates/ca-gate.md` sections 4-5, `library/prior/b-in.md`.

## 1. Scope, duplicate check, sources

- **Item.** FINISH row 389. Moves: (B-in), named input 1 of CA (`library/ca-claude.md` Result), the first place CA can fail. CA is open-core item CA (`library/open-core.md`, owner `ca-claude`); (B-in) is its input, not CA itself.
- **Duplicate check (rule 0a).** `grep` of `library/open-core.md`, `library/l17c.md` and `library/open-registry.md` for "B-in", "sealing", "own-level": no row attacks (B-in) or the sealing construction. FINISH rows naming it: 382 (check, found no supplier), 383 and 387 (digests), 386 (ca-f, lists it as open), 389 (this row). No other lane attacks it.
- **Account label and status.** (B-in) is clause (b) of `4.27:prf-room-dissolving` (CA-I 138348, index PROVED), whose proof (I:138438-138450) cites "the own-level bound for the configuration U_2 of the sealing construction". The account states no such construction. The second consumer is the core step of `4.27:prf-ambient-inclusion` (I:136490, index INCOMPLETE), I:136718-136760.
- **Sources.** CA-I, CA-II, CA-III fetched by URL into a scratch folder of this lane; SHA-256 agree with `library/arr.md` section 1. Line numbers are of those raw files. CMP 122a/b are not in `~/ym4d-papers`; they are used only as the account quotes them. CMP 98, 99b, 102, 109, 119 are local.
- **Rules.** No numerical run. No computer-assisted step.

## 2. Consumers first: what each one reads

Notation of the completion site (CA-I 92401-92420, 138357-138366): step k, h := k - N_k, determining set B''_k with levels o(x) := l_{B''_k}(x), cut Omega''~_{h+1}, B_2 := B''_k u B_h((Omega''~_{h+1})^c) (CMP 122b (1.52)), U_2 := U_{B_2}(V_2) (CMP 122b (1.53)), base pair (U_2, J(U_2)), presentation chain b_2 -> b_3 -> b_4 with layers H_3, H_4. Source set S of current localisation: the (2M_1+3 blocks)-neighbourhood of Omega''^{~2}_{h+1} in Lambda (I:92468-92469). Threshold of B^t := B''_k at y: theta^{B^t}_a(y) = w_{B^t}(y) r_a(o(y)), with w_{B^t} the actual weight (I:132999).

**R. Room at dissolving pieces, `4.27:prf-room-dissolving` (I:138348-138483).** It fixes x in W_c for a dissolving piece c, and a term tau read at x with threshold theta = F_tau w r_a(n), n <= o(x) <= h. Clause (b) is used only at x in W_c ("Place", I:138400-138403). Clause (c) asks the increments of the chain at x to total at most 3 theta/64. Clause (d) adds them.

**A. Ambient inclusion, core step (I:136718-136756).** It needs the presented pair within 1/16 of phi_flat w_{B^t}(x) r_e(o(x)) at every point x of the core of level o(x) >= 1, cube clause included, with one gauge for the G-part. It takes F = phi_flat, w = w_{B^t}(x), c = 1 (I:136733-136742). Whole frozen-family cubes of a dissolved piece (side CML^{l_c} eta, l_c <= h) must lie in the core (I:136752-136756).

**C. Our CA, `library/ca-claude.md` Lemma B and `library/ca-f.md`.** Level-one plaquettes with a vertex on Col(C), and every plaquette of every index-zero cube meeting Col(C): |dU_2(p) - 1| <= 0.04 alpha_{0,0} suffices (Lemma B(ii), (iii) and Proposition C use no more). The layers at the collar are ca-f's (CL), already proved there as an implication.

**Weakest statements that serve R, A and C.** Let K be a set of cells of D_2 (the core) and B_S := D_2 \ K.

- **(B-in-w), base bound.** For every cell x of K with o(x) >= 1: Q_a(x) <= (phi_flat/64) theta^{B^t}_a(x) for a in {1,3,5,6,7} at the pair (U_2, J(U_2)); at every triple of the readings (Sigma^flat), (Sigma^*) at x, entries 2 and 4 at most phi_flat/64 of their thresholds; and on every cube of side at most CML^lambda eta that meets K (this covers the cubes of Q_{B^t} at core points and the frozen-family cubes of dissolving pieces), a gauge u with U_2^u = e^{i eta A} and L^lambda eta |A|, (L^lambda eta)^2 |nabla A| <= (phi_flat/64) w_cube B C M alpha_{0,lambda}.
- **Why it suffices for R(b).** The clause of tau at x has threshold at least F_tau theta^{B^t}_a(x) >= phi_flat theta^{B^t}_a(x): for a stage-domain clause the structure read at x is the frozen one of B^t (precedence rule, I:132982-132986); for an earlier-born term, heredity (e2) of `4.27:lem-weights-heredity` (I:133096-133098; that lemma is marked incomplete at other steps) gives theta^{B}_a >= theta^{B^t}_a for B before B^t, as used at I:136670-136673; a finer birth index n < o(x) only enlarges r_a by (eq-factors-radii-coupling-2), I:131441-131446; and F_tau >= phi_flat is clause (a). "For all w >= 1" in the printed (b) is stronger than any consumer reads; Corollary B2 below proves it anyway, under the condition (Q) on q, and Corollary B1 proves the part CA reads without (Q).
- **(Sh-w), shares.** At every cell x of K with o(x) >= 1, every entry of the presented pair at b_3, b_4 and on every segment differs from its value at b_2 by at most (3/64) phi_flat theta^{B^t}_a(x), the cube gauges being those of U_2.
- **(Pl), placement.** For every piece c dissolving at the step, the blocks of W_c of level >= 1 lie in K, and every frozen-family cube of c meets K.
- **(S-B).** The cells of level >= 1 meeting the one-bond neighbourhood of Col(C) lie in K, and every level-one plaquette of an index-zero cube meeting Col(C) is attached to a block of K.

The split into three shares (bend, source, map H') of the printed (c) is not read by any consumer; only the total 3/64 is. The account also asserts its base bound "for all F >= phi_flat, w >= 1, c >= 1" (I:138438-138444); taking F = phi_flat, w = w_{B^t}(x), c = 1 is the case every consumer reads.

## 3. The sealing construction, defined from the account's objects

The account names the construction (I:138361-138366) but states none of its theorems. Every object below is the account's or Balaban's; only K and B_S are chosen here.

- **The configuration.** U_2 := U_{B_2}(V_2), the minimal configuration of CMP 122b (1.53) for B_2 = B''_k u B_h((Omega''~_{h+1})^c) (CMP 122b (1.52), quoted at I:92417-92421). By CMP 119 (2.14) (local, p. 257), B u B_j(Omega) = (B n Omega^{~-2}) u (B_j(Omega) n (Omega \ Omega^{~-2})): the support of B_2 is Omega := (Omega''~_{h+1})^c; there B_2 has the blocks of B''_k except in the graded layer of width 2M_1 blocks at the cut (I:92515-92532). U_2 reads V'' only off Omega''^{~2}_{h+1} (I:138407-138411); it is real (current localisation, hypothesis (c), I:92446-92448).
- **The chain.** b_2: the pair (U_2, J(U_2)), A' = 0. b_3, b_4: the left factors e^{i eta t_3 H_3}, e^{i eta t_4 H_4} with the layers H_3, H_4 of `4.22:lem-current-localisation`, and the partner currents of ca-f Lemma S as source increments; t_3, t_4 in [0,1] give the segments.
- **Graded region and cut region.** G := (support of B_2) \ S. On G, B_2 = B''_k and V_2 = V''. The cut region is the rest of the support: the graded layer and S.
- **Core and B_S.** K := the blocks of B''_k of level >= 1 that lie in G at d_sc-distance at least Rc_k/2 from S; B_S := the cells of D_2 at d_sc-distance less than Rc_k/2 from S. So B_S is the half of the separating layer nearest S, and K contains Z_h^{(2)}, the points within 4CML^h eta of Z_h (C <= 2 the cube constant of CMP 122a (1.65)), because d_sc(Z_h, S) >= Rc_k - 1 (I-G)(b) and Rc_k - 9 >= Rc_k/2 once Rc_k >= 18. The objects Gamma_flat, "bend floor" and "ownership floor" of I:138455-138462 are not needed: their only role there is to make the shares and the cube clause hold, and sections 5-7 prove these directly under named ceilings.

## 4. The reset at one block (input) and its iteration (proved)

**Input (LR), the local reset.** This is the one place where this note reads a checked text in a new way; the checker should confirm it. There are constants B_3 >= 1, R_1M_1 >= 1, a_5 > 0, fixed in b102's order from d, L and the group, with this property. Let (B, V) be an admissible instance of b102 Theorem 1 (`library/b102.md` section 1, (T1)-(T4)), and U a critical configuration of it in the regular class (T1). For a block Delta = B^j(y) of level j, let box(y) be the cube of side 2R_1M_1 L^j eta through Delta and box~(y) its concentric enlargement with dist(box, box~^c) = 2R_1M_1 L^j eta (CMP 102 (144)). Let

  r(y) := the least r such that U obeys (T1) at radius r on every plaquette and bond of box~(y);
  e(y) := the least e such that the data tests of CMP 102 (7) hold at radius e on the two central layers inside box~(y).

If r(y) <= a_5, then U obeys (T1) on Delta at radius max{ B_3 e(y), r(y)/2 }.

*Source and reading.* Balaban, CMP 102 section F, pp. 300-304, (144)-(168), read on the printed pages (rendered from `~/ym4d-papers`): the gauge (145)-(146) uses the space (2) on box~ only; the local problem (147)-(151) lives on C_k inside box~, with artificial data equal to the averages of U itself; (160) uses the data assumption (7) only on the central layers; (161) splits the sum into the central part and C_k \ box_k, the latter carrying e^{-delta_0 R_1M_1/2} epsilon_0; (163)-(168) give the radius max{B_3 epsilon_1, epsilon_0/2} on Delta_0 = B^j(y). Balaban says the inequalities are local (p. 302: "They are local, and for a plaquette p, or a bond b, we take a unit cube Delta_0 in B^j(Lambda_j) containing p or b"); the local datum B of (155)-(156) is bounded through epsilon_0 on box~ only, and all operators of the local problem are the flat ones of CMP 95, 96 (p. 302). He states the result with global epsilon_0, epsilon_1 and iterates (Proposition 8); the argument at one block reads only r(y) and e(y). b102 rebuilds it as H21, "Reset for any already constructed critical field" (`library/b102.md` 2944-3021: "Freeze the actual averages of U on the artificial outer boundary ... The local field is therefore critical for that local problem"), checked line by line by Claude, first failing step none (`gates/b102-gate-b.md`). b102 proves SU(2), d = 4, uniformly in depth, spacing, volume and admissible nest.

**Lemma I (iteration).** Let Y be a set of blocks, N(y) := {z in Y : z meets box~(y)}, N^0(y) := {y}, N^{i+1}(y) := union of N(z) over z in N^i(y). Let rho, e : Y -> [0, infinity) with rho bounded, and suppose rho(y) <= max{ B_3 e(y), (1/2) sup_{N(y)} rho } for every y. Then for every y

  rho(y) <= B_3 sup_{i >= 0} 2^{-i} sup_{z in N^i(y)} e(z) = B_3 sup_z e(z) 2^{-d_N(y,z)},     (I.1)

where d_N(y,z) := min{i : z in N^i(y)} (infinity if none).

*Proof.* Claim: for every m >= 1 and every y, rho(y) <= max{ B_3 max_{0<=i<m} 2^{-i} sup_{N^i(y)} e, 2^{-m} sup rho }. For m = 1 this is the hypothesis, since sup_{N(y)} rho <= sup rho. If it holds for m at every block, insert it at each z in N(y):

  rho(y) <= max{ B_3 e(y), (1/2) sup_{z in N(y)} max{ B_3 max_{i<m} 2^{-i} sup_{N^i(z)} e, 2^{-m} sup rho } }
         =  max{ B_3 max_{i<m+1} 2^{-i} sup_{N^i(y)} e, 2^{-m-1} sup rho },

because the union of N^i(z) over z in N(y) is N^{i+1}(y). Let m tend to infinity; rho is bounded. QED.

**Theorem G (graded reset).** Let (B, V) be an admissible instance of b102 Theorem 1 with all data tests at most a_1, let U be its minimal configuration, and let rho(y) be the least radius at which U obeys (T1) on the plaquettes and bonds attached to the block y (a plaquette is attached to the block of its base point, a bond to the block of b_-; each test is read at the largest level j with p, b in Omega_j, as in (T1)). Assume (LR). Let t(z) be the largest data test of CMP 102 (7) attached to the block z. Then for every block y,

  rho(y) <= B_3 sup_z e(z) 2^{-d_N(y,z)} <= 2 B_3 sup_z t(z) 2^{-d_N(y,z)}.     (G.1)

*Proof.* b102 Theorem 1 puts U in the regular class at radius B_3 a_1 <= a_5 (b102 chooses a_0, a_1 last, "so that B_3 a_1 < a_0 and every preliminary radius above fits those fixed radii", lines 3066-3069). So rho is bounded by B_3 a_1 (Balaban fixes a_1 so that this radius is at most a_5, CMP 102 p. 304), and r(y) <= sup_{N(y)} rho <= a_5 for every y, since every plaquette and bond of box~(y) is attached to a block that meets box~(y). The conclusion of (LR) on Delta = y covers the tests attached to y. (LR) gives the hypothesis of Lemma I, hence the first inequality. For the second, every data plaquette in box~(z) is attached to a block z' of N(z), so e(z) <= sup_{z' in N(z)} t(z'), and d_N(y,z') <= d_N(y,z) + 1. QED.

*Remark (edges of the problem).* Lemma I needs its inequality at every block, not (LR) itself. At a level-zero block all of whose attached plaquettes are pinned (for instance near the outer boundary of Omega_0, where every bond is prescribed, M^0 being the identity), U equals the datum there, so rho(y) = t(y) <= B_3 t(y) and the inequality holds with e(y) := t(y). At any block where (LR) is not read (for U_2, only at blocks of the cut region, at the boundary of the support), put e(y) := a_1; since rho <= B_3 a_1 the inequality holds there too, and such blocks enter (G.1) only through a_1 2^{-d_N}, which is how sections 5.3-5.4 treat the cut region.

Theorem G is linear in the data: each data test enters with the factor 2^{-d_N}, whatever its level. The rest of the note estimates sup_z t(z) 2^{-d_N(y,z)} at the blocks the consumers read.

## 5. The base bound

### 5.1 Named inputs (account statements and readings)

- **(I-A) U_2 is an instance of b102 Theorem 1.** The nest of B_2 is admissible in the sense of CMP 102 (1), the data V_2 pass every data test of CMP 102 (7) at radius at most a_1, and U_2 is the minimal configuration. Sources: U_2 is "the minimiser of the problem [CMP 122b (1.53)]" (I:92419-92420); CMP 119 (2.12)-(2.15) builds U_{B u B_j(Omega)} as a minimal configuration and says "we will use all the results of [15]" (= CMP 102). Not proved here.
- **(I-G) Geometry of B''_k on G.** (a) Levels are consecutive across strata, and each zone Omega_l \ Omega_{l+1} has dist_inf(Omega_l^c, Omega_{l+1}) >= M L^l eta (the weaker of the two forms in the account: (G) of `4.27:lem-live-piece-increments`, I:137093-137097; (c7)(d) at I:63571-63586 gives M L^{l+1} eta). (b) d_sc(Z_h, S) >= Rc_k - 1, with d_sc the path metric counting cells of the local scale (law-site lemma (ii)(beta), I:92095-92097, index PROVED; I:91723-91728). (c) S does not meet Z_h, so S lies in Lambda_h, inside Omega_h (as in `ca-claude.md` Lemma E).
- **(I-D) Data.** On G, every data test of V'' (CMP 102 (7), mixed-level plaquettes included) attached to a block z of level o(z) is at most 6 K_d L_0^{2 nu(z)} eps_{o(z)}, with an integer 0 <= nu(z) <= min{o(z), N_0}, nu = 0 off blocks raised by an operation R. Here eps_j = A_0 g_j (log g_j^{-2})^{p_0} (CMP 119 (2.4)). Sources: the account's data clause (gamma) at I:137012-137036: strata made by T, "of size O(L^2) eps_n" (CMP 119 p. 256); rebuilt strata, K_J eps_{k''}; raised blocks, "|dV - 1| <= 6 L_0^{2 nu} eps_m" from CMP 122a (1.24) and CMP 98 (54), local by CMP 98 Proposition 2; unprocessed shells, CMP 122a (1.3), (1.4). The mixed-level tests are Balaban's regularity of the datum ("A regular configuration V on B", CMP 119 (2.12)). Raises are at most N_0 (I:68331-68334).
- **(I-N0) Weights are polynomial.** L_0^{6 N_0} <= L^{4 N_0} <= l_j^2, with l := (L^2 Rbar)^2 and Rbar(x) = L (2 log x)^r (I:68334, I:131459-131463). Hence L_0^{2 nu} <= l_j and every data test on G is at most eps^D_{o(z)} := 6 K_d l(x_{o(z)}) eps_{o(z)}.
- **(I-R) Ratios across levels.** For n > m: g_n <= (1+beta_0)(n-m)^{1/2} g_m, g_m <= (1+beta_0) g_n, (log g_n^{-2})^p <= (1+beta_0)(log g_m^{-2})^p, (log g_m^{-2})^p <= (1+beta_0)(n-m)^{beta_0}(log g_n^{-2})^p (CMP 119 (2.6)-(2.7), read on p. 255). Every function f_j = c g_j (log g_j^{-2})^P of the level (eps_j, eps^D_j, alpha_{i,j}) therefore obeys f_n <= (1+beta_0)^2 (n-m)^{1/2} f_m and f_m <= (1+beta_0)^2 (n-m)^{beta_0} f_n. With beta_0 <= 1/7 (Ce4), both are at most c_R (n-m)^{1/2} f, c_R := (8/7)^2.
- **(I-T) Thresholds.** r_1(n) = r_5(n) = alpha_{0,n} L^{-2n}, eta^3 r_3(n) = alpha_{0,n} L^{-3n}, alpha_{i,n} = C^rad_i e^{-t_n/2} t_n^q, and eps_n / alpha_{0,n} = (A_0/C_0^rad) t_n^{p_0-q} with q > p_0 (I:131413-131420, I:131427-131433; CMP 119 (2.34)-(2.39) read on p. 261; (Fl8)). t_n >= t_gamma for every level (flow bounds).
- **(I-K) Scales.** Rc_k >= (log(x_k - c_5))^r with r >= 2, k = h + Rc_k (I:77938-77954, with r >= 2 there).

**Floor (M).** M >= max{16 L s_0, 8 L^2} R_1M_1 with s_0 := 2 + ceil(2 log_2 L_0), so that 2^{s_0} >= 4 L_0^2; and M >= 4 W_aux, W_aux the auxiliary width of b102 H14. M is chosen after L, L_0 and b102's R_1M_1, as the account's M >= 2LR_1M_1 of `4.9:prop-real-backgrounds` already is.

### 5.2 Lemma C: chains in the graded region (proved)

A chain of length i from y is a sequence y = z_0, ..., z_i of blocks with z_{t+1} in N(z_t). d_N^G(y,z) is the least length of a chain from y to z through blocks of G; i_S(y) is the least length of a chain from y that reaches a block of the cut region.

**Lemma C.** Assume (I-G) and the floor (M). Let y be a block of G of level j.
- (C0) box~(y) meets at most two zones, and they are consecutive among j-1, j, j+1.
- (C1) If z is in G and |o(z) - j| = m >= 1, then d_N^G(y,z) >= (m - 1) s_0.
- (C2) i_S(y) >= (1/2) [ (h - j - 2)^+ s_0 + (d_sc(y, S) - 1)/8 ]. In particular i_S(y) >= (1/2)[(h - j - 2)^+ s_0 + (Rc_k - 4)/32] if d_sc(y, S) >= Rc_k/4.

*Proof.* A block of level m has side L^m eta, and box~ of it lies within sup-distance 4R_1M_1 L^m eta of it. If z_{t+1} is in N(z_t), points of z_t and of z_{t+1} are within (4R_1M_1 + 1) L^{o(z_t)} eta + L^{o(z_{t+1})} eta of each other; call this the step bound.

(C0) Meeting zones j-1 and j+1 together needs a set of diameter at least the width of zone j, which is at least M L^j eta > 9 R_1M_1 L^j eta. Meeting zone j-2 needs to cross zone j-1, of width at least M L^{j-1} eta > 5 R_1M_1 L^j eta. Meeting zone j+2 needs to cross zone j+1, wider still. All by (M).

(C1) Let m >= 2, say o(z) = j + m. Levels change by at most one per step, by (C0). For each l with j < l < j + m, let tau_l be the first index with z_t in Omega_{l+1}, and sigma_l the last index before tau_l with z_t in Omega_l^c. The blocks strictly between lie in zone l, hence have level l; the block at sigma_l has level l - 1 and the block at tau_l level l + 1. Points of the blocks at sigma_l and tau_l are at least M L^l eta apart. By the step bound, each of the tau_l - sigma_l steps moves at most (4R_1M_1 + 1 + L) L^l eta <= 6 L R_1M_1 L^l eta. So tau_l - sigma_l >= M/(6 L R_1M_1) >= s_0 + 1 by (M). If o(z) = j - m, the roles of Omega_l^c and Omega_{l+1} are exchanged; the first step of each crossing starts at a block of level l + 1 and moves at most (4R_1M_1 + 1) L^{l+1} eta + L^l eta <= 6 L R_1M_1 L^l eta, and the others start at blocks of level l, so tau_l - sigma_l >= s_0 + 1 again. The open index intervals (sigma_l, tau_l) for distinct l are disjoint, since their blocks lie in distinct zones, and consecutive closed intervals share at most one index. Summing over the m - 1 zones, i >= (m-1) s_0.

(C2) A chain that reaches the cut region reaches S, and S lies in Omega_h (I-G)(c). Its last block in G is within one step of Omega_h, so by (C0) it has level at least h - 1. Before that the chain stays in G and climbs from level j to level h - 1, crossing the zones j+1, ..., h-2; by the argument of (C1) its length is at least (h - j - 2)^+ s_0. Separately, by the step bound and (M), a step from a block of level l <= h moves less than the side M L^{l-1} eta of a cell of level l - 1, the finest cells its box~ meets (C0). So it crosses at most one cell boundary in each of the d = 4 directions on each side and changes d_sc to a fixed set by at most 2d = 8 (reading of d_sc as the path metric that counts cells, I:91723). So the chain has length at least (d_sc(y, S) - 1)/8. The larger of two numbers is at least their mean. QED.

### 5.3 Corollary B1: the base bound that CA reads (proved, as an implication)

**Corollary B1.** Assume (LR), (I-A), (I-G), (I-D), (I-R), (I-T), (I-K), the floor (M), and the two ceilings (Gamma_1), (Gamma_2) below, each a one-sided cap of degree minus infinity fixed last. Let C be a completing component at a completion date and y a block of B''_k of level at most 1 within sup-distance 20 M eta of Col(C). Then U_2 obeys (T1) on y at radius

  rho(y) <= 2 B_3 C_1 eps_1,   C_1 := 6 K_d c_R L_0^4,

and every plaquette p of level one attached to such a block satisfies |dU_2(p) - 1| <= (phi_flat/64) r_1(1).

*Proof.* The block y lies in Z_1 (the boundaries of Omega_1 and Lambda_1 are at least 2MR_1 cells of level one apart, I:63572-63574, so blocks within 20 M eta of Col(C), which lies outside Omega_1, avoid Lambda_1), hence in Z_h, at d_sc-distance at least Rc_k - 2 from S (I-G)(b); so y is in G, where B_2 = B''_k and V_2 = V''. Theorem G applies by (I-A) and (LR). Split the supremum in Theorem G by whether the chain stays in G:

  rho(y) <= 2 B_3 max{ sup_{z in G} t(z) 2^{-d_N^G(y,z)}, a_1 2^{-i_S(y)} }.

*Chains in G.* Let z be in G, of level lambda. By (I-D), t(z) <= 6 K_d L_0^{2 lambda} eps_lambda, since nu(z) <= lambda. By (I-R), eps_lambda <= c_R max{1, lambda - 1}^{1/2} eps_1 for every lambda >= 0. By (C1) with j <= 1, d_N^G(y,z) >= (lambda - 2)^+ s_0. Hence t(z) 2^{-d} <= 6 K_d c_R eps_1 L_0^4 (L_0^2 2^{-s_0})^{(lambda-2)^+} max{1, lambda-1}^{1/2} <= C_1 eps_1, because L_0^2 2^{-s_0} <= 1/4 and 4^{-n}(n+1)^{1/2} <= 1 for n >= 0.

*Chains to the cut region.* By (C2) with j <= 1 and d_sc(y, S) >= Rc_k/4, 2^{-i_S(y)} <= 2^{-(h-3)^+ s_0/2} 2^{-(Rc_k - 4)/64}. By (I-R) with n = k > m = 1, g_k <= (1+beta_0)(k-1)^{1/2} g_1, so e^{-t_1/2} >= e^{-t_k/2} (1+beta_0)^{-1} (k-1)^{-1/2}; and k - 1 = h - 1 + Rc_k <= (1+h) Rc_k. Since eps_1 = A_0 e^{-t_1/2} t_1^{p_0} >= A_0 e^{-t_1/2},

  C_1 eps_1 >= C_1 A_0 e^{-t_k/2} (1+beta_0)^{-1} (1+h)^{-1/2} Rc_k^{-1/2}.

Now 2^{-(h-3)^+ s_0/2} (1+h)^{1/2} <= 2 for all h >= 0, as s_0 >= 2. So a_1 2^{-i_S(y)} <= C_1 eps_1 follows from the ceiling

  (Gamma_2)  2 (1+beta_0) a_1 R^{1/2} 2^{-(R-4)/64} e^{t/2} <= 6 K_d c_R A_0   for all t >= t_gamma and all R >= (log(e^t - c_5))^r,

applied at t = t_k >= t_gamma, R = Rc_k (I-K). The left side is largest at the least R once R >= 100, and with r >= 2 it tends to 0 as t tends to infinity; so (Gamma_2) is a one-sided cap of degree minus infinity, and every constant in it is fixed before gamma. So rho(y) <= 2 B_3 C_1 eps_1.

*The plaquettes.* A plaquette p of level one attached to y has |dU_2(p) - 1| <= rho(y) L^{-2} (T1). By (I-T), eps_1 = (A_0/C_0^rad) t_1^{p_0-q} alpha_{0,1}, and the ceiling

  (Gamma_1)  128 B_3 C_1 (A_0/C_0^rad) t_gamma^{p_0 - q} <= phi_flat

gives |dU_2(p) - 1| <= (phi_flat/64) alpha_{0,1} L^{-2} = (phi_flat/64) r_1(1). QED.

*What B1 gives CA.* Lemma B(i) of `ca-claude.md` is its second conclusion, now without (B-in): the plaquettes there have a vertex on Col(C) and a corner in Omega''_1, so they are attached to blocks of level at most 1 within one lattice step of Col(C). Lemma B(iii) reads the level-one plaquettes of index-zero cubes meeting Col(C); such a cube has at most 10M sites per side (I:142775-142777), so its plaquettes are attached to blocks within 20 M eta of Col(C), and B1 bounds them; the pinned ones are Lemma A. So (S-B) is not needed by CA either: B1 is proved at the blocks themselves, which lie in Z_1. Constants: K_d, L_0, beta_0, B_3, a_1, R_1M_1 are fixed before M; M before gamma; (Gamma_1), (Gamma_2) last. Nothing depends on h, k, the age, or the numbers of exclusions, blocks or strata.

### 5.4 Corollary B2: the base bound at every core block (proved, as an implication)

Corollary B1 uses the weighted data bound and needs nothing about q beyond (Fl8). At blocks of higher level the weights L_0^{2 nu} of nearby raised blocks are not dominated by a power of L_0 per level, so B2 uses the account's absorption of the weights into eps^l = l eps (I-N0), which is the form of its own floor K^own eps^l <= m phi_flat alpha_0 (I:131713-131716, I:136827-136832).

**Condition (Q).** q > p_0 + 2r. Then delta_D(t) := sup_{t' >= t} eps^D(t')/alpha_0(t') = 6 K_d L^6 4^r (A_0/C_0^rad) sup_{t' >= t} t'^{p_0 + 2r - q} tends to 0. (With l = (L^2 Rbar)^2 = L^6 (2t)^{2r}.) The account's floor (Fl11), imposed at every margin m it uses, needs the same ratio to be small; I did not find (Q) stated in this form.

**Lemma J (current from the regularity tests).** Let U be real, b a bond, and suppose the six plaquettes p containing b obey |dU(p) - 1| <= theta <= 1/10. Then eta^3 |J(U)(b)| <= c_pi ( eta |D^{eta*}_U dU(b)| + 3.4 theta^2 ), with c_pi <= 2 (I:142727-142728).

*Proof.* By input (e) of `4.27:lem-real-point-collar` (CMP 109 (1.8)), eta^3 J(U)(b) = sum_{p ni b} (+-) Ad_{tau_p} pi Im W_p, W_p := dU(p). Put X_p := W_p - 1. Then W_p^* - 1 = W_p^{-1} - 1 = -X_p W_p^{-1}, so W_p - W_p^* = 2X_p - X_p^2 W_p^{-1} and Im W_p = -i X_p + (i/2) X_p^2 W_p^{-1}; the Neumann series gives |W_p^{-1}| <= 10/9, so |Im W_p + i X_p| <= 0.56 theta^2. pi commutes with Ad (the trace is invariant), and the signed sum of the identity over the six plaquettes vanishes (the two plaquettes in each transverse direction have opposite orientation), so sum (+-) Ad_{tau_p} X_p = eta (D^{eta*}_U dU)(b), the covariant divergence of (T1) (CMP 102 (2); b102 records the same conversion at H14: "The anti-Hermitian part is the current"). Hence eta^3 |J(b)| <= c_pi (eta |D^{eta*}_U dU(b)| + 6 (0.56) theta^2). QED.

**Corollary B2.** Assume (LR), (I-A), (I-G), (I-D), (I-N0), (I-R), (I-T), (I-K), (Q), the floor (M), (Gamma_2), and the ceiling (Gamma_3) below. Then:

- (a) rho(y) <= 2 B_3 c_R eps^D_n for every block y of G of level n := o(y) with d_sc(y, S) >= Rc_k/4;

and for every block y of the core K, of level n >= 1:

- (b) entries 1 and 5 of (U_2, J(U_2)) at y are at most (phi_flat/64) r_1(n), entry 3 at most (phi_flat/64) r_3(n), and entries 6, 7 vanish;
- (c) on every cube of side at most CML^lambda eta, of level lambda, meeting K, there is a gauge u with U_2^u = e^{i eta A} and L^lambda eta |A|, (L^lambda eta)^2 |nabla A| <= (phi_flat/64) B C M alpha_{0,lambda};
- (d) under the refinement input (Ref) below, entries 2 and 4 at every triple of (Sigma^flat), (Sigma^*) at y are at most phi_flat/64 of their thresholds.

These are thresholds at weight w = 1, factor phi_flat and multiplier c = 1, the smallest the account's clause allows; so (b)-(d) hold for every w >= 1, c >= 1, F >= phi_flat, as the account's own-level bound is stated (I:138438-138444).

*Proof of (a).* As in B1, rho(y) <= 2 B_3 max{ sup_{z in G} t(z) 2^{-d_N^G(y,z)}, a_1 2^{-i_S(y)} }. For z in G of level lambda, (I-D) and (I-N0) give t(z) <= eps^D_lambda, and (I-R) and (C1) give t(z) 2^{-d} <= c_R max{1, m}^{1/2} 2^{-(m-1)^+ s_0} eps^D_n <= c_R eps^D_n, m := |lambda - n|, since m^{1/2} 2^{-(m-1) s_0} <= 1 for m >= 1. For the cut region, d_sc(y, S) >= Rc_k/4 and (C2) give the same bound on i_S(y) as in B1, with h - 3 replaced by h - n - 2, and 2^{-(h-n-2)^+ s_0/2}(1 + h - n)^{1/2} <= 2. Then, exactly as in B1 with level 1 replaced by n and k - n <= (1 + h - n) Rc_k, (Gamma_2) gives a_1 2^{-i_S(y)} <= 6 K_d c_R A_0 e^{-t_n/2} <= c_R eps^D_n, since eps^D_n >= 6 K_d A_0 e^{-t_n/2}.

*Proof of (b).* A plaquette attached to y has |dU_2(p) - 1| <= rho(y) L^{-2n} <= 2 B_3 c_R delta_D(t_gamma) alpha_{0,n} L^{-2n}. For entry 3, Lemma J with theta <= rho' L^{-2n}, rho' the largest rho over the blocks attached to the six plaquettes (all in G at d_sc-distance at least Rc_k/2 - 2 >= Rc_k/4 from S, of level >= n - 1, so rho' <= 2 B_3 c_R^2 eps^D_n by (a) and (I-R)), gives eta^3 |J(U_2)(b)| <= 2.2 rho' L^{-3n} once rho' <= 1/34. The ceiling

  (Gamma_3)  128 (2.2) B_3 c_R^2 delta_D(t_gamma) <= phi_flat,   with   2 B_3 c_R^2 delta_D(t_gamma) <= 1/34,

gives both bounds; it is a one-sided cap of degree minus infinity under (Q). U_2 is real, so A' = 0 and entries 6, 7 vanish; entry 5 equals entry 1.

*Proof of (c).* b102 H14.1 (`library/b102.md` 1858-1886, checked in `gates/b102-gate-a.md`): around a cube of side n s, s = L^lambda eta, n <= CM, an enclosing cube of side M'' s with M'' <= CM + 2 W_aux carries a gauge with s|A| + s^2 |nabla A| <= C_L M'' eps', where eps' is the regularity radius on the enclosing region, read at the finer scale of a two-layer cube at the cost of L^2, L^3. The enclosing region is within 2 cells of level lambda of the cube (M >= 4 W_aux), so its blocks are at d_sc-distance at least Rc_k/2 - 4 >= Rc_k/4 from S, and eps' <= 2 L^3 B_3 c_R^2 eps^D_lambda by (a) and (I-R). The ceiling

  (Gamma_4)  128 C_L (CM + 2 W_aux) L^3 B_3 c_R^2 delta_D(t_gamma) <= phi_flat B C M

gives (c). C_L, W_aux, L, B, C, M are fixed before gamma. The account's `4.9:prop-real-backgrounds` (b) (index PROVED, I:36501) gives the same conclusion from its regularity hypothesis and may replace H14.1 here.

*Proof of (d).* **Input (Ref).** For every triple (p, X', s) of the readings at y, the restriction of U_2 to X' is critical for the refined problem on X' at its own averages M^s U_2, and that problem has one critical orbit in the regular class. This is the account's "statement on refinement of the determining set" (I:136835-136839), the hypothesis under which it derives the same clause for the real minimiser (I:137049-137070). Criticality is the elementary inclusion of constraint classes used at I:131690; uniqueness is the uniqueness clause of b102 Theorem 1 when the refined problem is an admissible instance. Given (Ref), U_{p,X'}(M^s U_2) is a gauge copy of U_2 on X' and J_{p,X'} a gauge copy of J(U_2), and the identities L^{-2p}(L^n L^{-p})^{-2} = L^{-2n}, L^{n - min{p,n}} >= 1 turn the bounds of (b) for entries 1 and 3 into those for entries 2 and 4 (I:137062-137068). QED.

## 6. Placement (Pl) and (S-B) (proved)

**Lemma P.** (i) For every piece c that dissolves at the completion step, every block of W_c of level >= 1 is a block of K, and every cube of side at most CML^h eta that meets W_c meets K. (ii) Every block of level >= 1 within 20 M eta of Col(C) is a block of K, and every index-zero cube meeting Col(C) consists of blocks of level <= 1 bounded by Corollary B1.

*Proof.* (i) Clauses (T2) and (T4) of `4.27:lem-arrest-timing` give X_c in Z_{k_c} in Z_h (as the account uses them at I:138393-138398), so W_c lies in Z_h. Z_h lies in D_2 (law-site proof, I:91991-92024), hence outside Omega''~_{h+1}, and d_sc(Z_h, S) >= Rc_k - 1 >= Rc_k/2 (I-G)(b). So the blocks of W_c lie in G at d_sc-distance at least Rc_k/2 from S. A cube of side at most CML^h eta meeting W_c meets a block of W_c. (ii) As in the proof of B1, these blocks lie in Z_1, inside Z_h. The cube statement is the size bound of I:142775-142777 with B1. QED.

So the account's placement sentence ("W_c lies two layers of cubes of side LMR_{h+1} inside S, and it lies off B_S", I:138400-138403) holds for our B_S, and so does its claim that frozen cubes lie "whole in D_2 \ B_S" (I:136752-136756) in the form B2(c) needs: a cube meeting K.

## 7. Shares (Sh-w): the increments at core blocks (proved, as an implication)

The increments are the left factors e^{i eta t_s H_s}, s = 3, 4, with their partner currents. `library/ca-f.md` bounds them on the collar. Its Proposition R bounds the layer tuple E_{y'}(H_s) at every block y' (its Step 3), in the units of y'. Here that bound is used at core blocks of level n >= 1, with two lemmas for the change of units.

**Lemma BCH (quadratic remainder).** For matrices with |X| <= 1/40 and |Y| <= 1/80, |log(e^X e^Y) - X - Y| <= 1.1 |X| |Y|.

*Proof.* Let F(t) := log(e^{tX} e^Y) and G := F - tX - Y. By the proof of (ii) of `4.27:lem-left-factor-algebra` (I:141336-141380), F is defined on [0,1] with |F| < 0.04, and F' = psi(ad_F) X. Write psi(z) - 1 = z phi~(z); from the coefficients listed there, ||phi~(ad_F)|| <= 1/2 + (zeta/12)/(1 - zeta^2) <= 0.511 for zeta = ||ad_F|| <= 0.08. Since [tX, X] = 0, ad_F X = [G + Y, X]. So |G'| <= 0.511 * 2 |G + Y| |X| <= 1.022 (|G| + |Y|) |X|, and G(0) = 0. Gronwall's inequality gives |G(1)| <= |Y| (e^{1.022 |X|} - 1) <= 1.05 |X| |Y|. QED.

**Lemma A_n (left-factor algebra at level n).** Write Ub for the full configuration, Ub = e^{i eta A'} U with U G-valued (the account's bold U). Let y be a point, n >= 0 and l := L^n eta, and let h be a g^c-valued 1-form, all on the bonds read by `4.27:lem-left-factor-algebra` at y. Put N := sup max{ l|h|, l^2 |nabla_{Ub} h| }, a := sup l|A'|, theta := max |dUb(p) - 1| over plaquettes based at y. Assume N <= 1/40, a <= 1/80, theta <= 1/10. Then, with Ub^+ := e^{i eta h} Ub = e^{i eta A'^+} U:
- (i_n) |dUb^+(p) - dUb(p)| <= L^{-2n} (2.9 + 5.6 theta L^n) N;
- (ii_n) l |A'^+ - A'| <= 1.06 N;
- (iii_n) l^2 |nabla_U (A'^+ - A')| <= (1 + 4.3 a) N <= 1.06 N.

*Proof.* Since l >= eta, the hypotheses of the unit-spacing lemma hold for eta h and eta A', so every identity of its proof holds; only the bookkeeping of sizes changes. (i_n): in its display (4.27:eq-left-factor-algebra-5), |S| <= 2 eta^2 sup|nabla_{Ub} h| + (2 theta/(1 - theta))(2.03) eta sup|h| <= 2 L^{-2n} N + 4.6 theta L^{-n} N, using eta^2 = L^{-2n} l^2 and eta = L^{-n} l. Each |A_j| <= 1.26 eta |h| =: alpha' <= 1.26 L^{-n} N, so |Xi - S| <= 8.6 alpha'^2 <= 13.7 L^{-2n} N^2 <= 0.35 L^{-2n} N. Then |Xi| <= 0.071 and |dUb^+(p) - dUb(p)| <= |e^Xi - 1| |W| <= 1.21 |Xi|, which gives (i_n). (ii_n): multiply (4.27:eq-left-factor-algebra-3) by L^n. (iii_n): A'^+ - A' = h + E with E the BCH remainder at each bond; by Lemma BCH, l|E| <= 1.1 L^{-n} (l|h|)(l|A'|), so l^2 |nabla_U E| <= 2 L^n l |E| <= 2.2 N a. Replacing nabla_{Ub} h by nabla_U h costs (e^{2 eta|A'|} - 1) eta |h| <= 2.1 L^{-2n} N a in eta^2-units, that is 2.1 N a in l^2-units (as in the account's proof of (iii)). Sum. QED.

**Lemma E' (distance of core blocks from S).** Assume (c7)(d) of `4.21:def-strips-geometry` (zones at least L cells of their level thick, I:63571-63586, as `ca-claude.md` Lemma E does). For every block y of K of level n, d_sc(y, S) >= (1/2) [ Rc_k/2 + (L - 2)(h - n - 1)^+ ].

*Proof.* d_sc(y, S) >= Rc_k/2 by the definition of K. S lies in Omega_h (I-G)(c), and y lies outside Omega_{n+1}; the argument of `ca-claude.md` Lemma E, applied to the zones of levels n+1, ..., h-1, gives d_sc(y, S) >= (L - 2)(h - n - 1)^+. The larger of two numbers is at least their mean. QED.

**Proposition Sh.** Assume the named inputs of `library/ca-f.md` (N1)-(N8), with (N7) read at the kernels of H_3, H_4 at core blocks and (G-sep) read for every block of K (for blocks of Z_h this is ca-f's (G-sep)); the base bound B2; Lemma E'; the rescaling bound 1(e) of the arrest theorem's inputs for entries 2 and 4 (I:131580-131586), with its radius alpha~_{0,m} at least a fixed multiple c~ of alpha_{0,m} (reading); and the ceiling (Gamma_Sh) below. Then at every block y of K of level n >= 1, for s in {3,4}, t_s in [0,1], every entry of the presented pair at b_3, b_4 and on the segments differs from its value at b_2 by at most (3/64) phi_flat theta^{B^t}_a(y), and the G-part, hence every cube gauge, is that of U_2.

*Proof.* *Layer sizes.* Proposition R of ca-f, Step 3, gives E_{y'}(H_s) <= (C_D/K_u) eps_Q(k) p_T(y'), p_T := e^{-delta_R d_sc(., T)}, at every block y', in the units l_{y'} of y' (the account's local norms use l = l_y, I:111408-111410). We take delta_R <= w delta/2 (shrink it if needed), so that p_T lies in the class M^wedge_{delta/2} that 1(e) reads (the argument of ca-f Step 1 with delta/2). For y' within two cells of y, (G-sep) and Lemma E' give d_sc(y', T) >= d_sc(y, S) - 3 >= (1/2)[Rc_k/2 + (L-2)(h-n-1)^+] - 3. By (N8), eps_Q(k) <= K_Q A^+ rho_C max_i alpha_{i,k}, and by (I-R), alpha_{i,k} <= c_R (k - n)^{1/2} alpha_{i,n}, with k - n = Rc_k + h - n. The blocks y' read at y have levels n - 1, n, n + 1 (C0), so converting their units to l = L^n eta costs at most L for |h| and L^2 for |nabla h|; this is the factor L^2 below. Hence, with alpha_{*,n} := min_i alpha_{i,n},

  F(y) := L^2 sup_{y'} E_{y'}(H_s) <= C_S ( Rc_k^{1/2} + S_2 ) e^{-delta_R Rc_k/4} alpha_{*,n},
  C_S := L^2 (C_D/K_u) K_Q A^+ rho_C^2 c_R e^{3 delta_R},   S_2 := sup_{m >= 0} m^{1/2} e^{-delta_R (L-2)(m-1)^+/2} < infinity.

*Entries 6 and 7.* At b_3 the base has A' = 0, so A'_3 = t_3 H_3 exactly; at b_4, Lemma A_n (ii_n), (iii_n) apply. Each layer moves entries 6, 7, in the units l = L^n eta of y, by at most 1.06 F(y); entries 6, 7 have thresholds alpha_{1,n} (L^n eta)^{-1}, alpha_{1,n} (L^n eta)^{-2} times w >= 1.
*Entries 1 and 5.* Entry 5 does not move. By B2(b), theta <= (phi_flat/64) alpha_{0,n} L^{-2n}, so 5.6 theta L^n <= 0.1 and Lemma A_n (i_n) moves entry 1 by at most 3 L^{-2n} F(y) per layer.
*Entry 3.* Lemma S of ca-f holds at y with l_y = L^n eta in place of eta: its three steps use only (N6), (N7) read at y, which are stated in local units (I:94996-95001, I:111580-111586). It gives l^3 |s^#_{sigma_s}[t_s H_s](b)| <= Kcur F(y), so eta^3 |J| moves by at most Kcur L^{-3n} F(y) per layer, against eta^3 r_3(n) = alpha_{0,n} L^{-3n}.
*Entries 2 and 4.* Input 1(e) with the majorant mu := (C_D/K_u) eps_Q(k) p_T gives Q_e^+ <= Q_e (1 + pi_x) + pi r_e with pi_x <= pi := K^b_S mu(x)/alpha~_{0,n} <= K^b_S F(y)/(c~ alpha_{0,n}); with Q_e <= r_e (B2(d)) the move is at most 2 pi r_e.
*Ceiling.* With c_sh := max{1.06, 3, Kcur, 2 K^b_S/c~},

  (Gamma_Sh)  sup_{R >= R_gamma} 2 c_sh C_S (R^{1/2} + S_2) e^{-delta_R R/4} <= (3/64) phi_flat,

a one-sided cap of degree minus infinity (R_gamma := inf_k Rc_k tends to infinity as gamma tends to 0, as in ca-f (N9)), makes the two layers together move every entry by at most (3/64) phi_flat times its threshold at weight one, hence at most (3/64) phi_flat theta^{B^t}_a(y). The left factor leaves U_2 and its gauges unchanged (`4.27:lem-left-factor-algebra`). QED.

The account's three shares (bend, source, map H') are this total split by kind; no consumer reads the split.

## 8. What is not shown, and where it can fail

- **(LR) is a reading.** Balaban proves the reset with global epsilon_0, epsilon_1 and iterates it (CMP 102 Proposition 8); b102 H21 states it the same way. This note uses the argument at one block, where only the regularity on box~ and the data on its two central layers enter (section 4). Every displayed step of CMP 102 (145)-(168) reads only those; the checker should confirm this once. If it fails, Theorem G fails, and with it B1 and B2.
- **(I-A) is not proved here.** That B_2 is an admissible nest of CMP 102, and V_2 passes the data tests at radius a_1, is Balaban's (CMP 122b (1.52)-(1.53), CMP 119 (2.14)) and is used as stated. CMP 122a/b are not in `~/ym4d-papers`; the data of B_h on the graded layer are not identified. Theorem G needs only that they pass the tests at radius a_1: the cut region enters every bound through 2^{-i_S} a_1.
- **(I-D) is the account's data clause.** Its raised-block bound rests on CMP 122a (1.24) and CMP 98 (54) as the account quotes them; its mixed-level tests are Balaban's regularity of the datum. The account's own summary of the data (I:137037-137038) rests on `4.27:lem-weights-heredity` (b), marked incomplete at one step; this note uses the pointwise bounds of (gamma) and (I-N0) instead.
- **(Q) is needed for B2 and not for B1.** If q <= p_0 + 2r, then eps^l/alpha_0 does not tend to 0, the account's own floor (Fl11) cannot hold at small margins either, and B2 is not proved by this route at raised blocks. B1, which is what CA reads, uses only q > p_0 (Fl8).
- **SU(2) only.** b102 is proved for SU(2) (`gates/uses-b102.md`, G1). For N >= 3, (LR) is Balaban's text unchecked here.
- **(Ref) and 1(e) are the account's.** Entries 2 and 4 (B2(d), and their shares) rest on the account's statement on refinement and on its rescaling bound 1(e), both used as stated. The consumers of A read no entry 2 or 4.
- **Coverage in consumer A.** Our B_S is the band of d_sc-width Rc_k/2 at S. That the keystone region covers B_S is part of A's own argument and is not checked here.
- **Not reconstructed.** The account's Gamma_flat, bend floor and ownership floor, and the split of the 3/64 into three shares. No consumer reads them separately.
- **Tries to kill the statement.** (1) A weighted form fails in general: at blocks raised by nu levels the data may be as large as 6 L_0^{2 nu} eps_m, and with weights varying across original shells thinner than one reset step, a weighted bound w_{B^t}(y) eps at an inner shell cannot be read off from Theorem G (section 5.4). This kills the route "weighted data, weighted thresholds", not (B-in): the account's absorption L_0^{2 nu} <= l (I-N0) gives the unweighted form. (2) A uniform-epsilon bound from b102 Theorem 1 alone fails: it gives rho <= B_3 eps_{max}, and eps_h/eps_n can be as large as c_R (h-n)^{1/2}, so the 1/64 is not uniform in the age. Theorem G repairs this by the factor 2^{-d_N}. No numerical run was used.

## Result

**Proof, as an implication.** The sealing construction is supplied, for SU(2), as follows. Proved by Claude, not yet checked by the other model.

1. **CA's input (B-in) is discharged (Corollary B1).** At every completion date, for every completing component C, U_2 obeys Balaban's regularity tests at radius 2 B_3 C_1 eps_1 on every block of level at most 1 within 20 M eta of Col(C). Hence every level-one plaquette there has |dU_2(p) - 1| <= (phi_flat/64) r_1(1) < 2.6 x 10^-4 alpha_{0,0} (the last step by `4.27:lem-level-zero-ratios` (a), as in `ca-claude.md` Lemma B(i)). This is Lemma B(i) of `library/ca-claude.md` and the level-one part of Lemma B(iii), without (B-in) and without (S-B). The bound is uniform in the cutoff, the density, h - n, the history, and the numbers of exclusions, blocks and strata.
2. **The account's own-level bound holds on the core (Corollary B2).** On K (blocks of level >= 1 at d_sc-distance at least Rc_k/2 from S), the base pair (U_2, J(U_2)) obeys every direct entry at 1/64 of phi_flat r_a(o(x)), entries 6 and 7 vanish, and every cube of side at most CML^lambda eta meeting K carries a gauge at 1/64 of phi_flat BCM alpha_{0,lambda}. Entries 2 and 4 hold under the account's refinement statement (Ref). This is the printed form, for every w >= 1, c >= 1, F >= phi_flat (I:138438-138444).
3. **Placement and (S-B) (Lemma P).** W_c of every dissolving piece lies in K, its frozen cubes meet K, and B_S is the band of width Rc_k/2 at S.
4. **Shares (Proposition Sh).** At every block of K, the layers b_3, b_4 and their segments move every entry by at most 3/64 of phi_flat times its threshold and keep the cube gauges of U_2, as an implication from the inputs of `library/ca-f.md`.

So clauses (b) and (c) of `4.27:prf-room-dissolving` and the core step of `4.27:prf-ambient-inclusion` get their inputs as implications. Neither those lemmas nor the arrest theorem is used to supply any of them.

**New mathematics here.** Theorem G (section 4): Balaban's reset of CMP 102 section F, read at one block and iterated (Lemma I), bounds the minimiser by the data with weight 2^{-chain distance}. Lemma C (chain geometry), Lemma J (current from the tests), Lemma A_n (left-factor algebra at level n), Lemma BCH, Lemma E', Lemma P. Theorem G is what makes the 1/64 independent of the age: a uniform-epsilon use of b102 Theorem 1 loses a factor up to (h - n)^{1/2}.

**Named inputs** (each cited where used).
- (LR): CMP 102 (144)-(168) and its rebuild b102 H21 (checked by Claude, first failing step none), read at one block. This reading is new and is **the first place the proof can fail**.
- (I-A): U_2 is an admissible instance of b102 Theorem 1 (CMP 122b (1.52)-(1.53), CMP 119 (2.12)-(2.15)).
- (I-D), (I-N0): the account's data clause (gamma) and its bound L_0^{6N_0} <= l^2 (I:137012-137036, I:68331-68334), from CMP 122a (1.24), CMP 98 (54) and Proposition 2, CMP 119 p. 256.
- (I-G): admissible geometry ((G) of `4.27:lem-live-piece-increments`, (c7)(d) for Lemma E'), and the law-site separation d_sc(Z_h, S) >= Rc_k - 1 (index PROVED).
- (I-R), (I-T), (I-K): CMP 119 (2.4)-(2.8) read on the printed pages; the account's radii and scales.
- For B2 only: condition (Q), q > p_0 + 2r; (Ref) for entries 2, 4.
- For Sh only: (N1)-(N8) and (G-sep) of `library/ca-f.md` (with (N1) the layer theorem (L) owned by `stage-claude`), and the rescaling bound 1(e).
- Floor (M) on M; ceilings (Gamma_1), (Gamma_2) for B1, and (Gamma_3), (Gamma_4), (Gamma_Sh) for B2 and Sh, all one-sided caps of degree minus infinity fixed last.

**Kind (How we work, item 9).** Proof of a step the account assumes: it cites "the own-level bound", "the share statement" and "the placement statement" of its sealing construction (I:138361-138483, I:136724-136756) and states none of them (`gates/ca-gate.md` section 4).

**What changes for consumers.** In `library/ca-claude.md`, named input 1 ((B-in) with (S-B)) is replaced by the inputs of Corollary B1. CA's first open inputs are then (LR) as read here, (I-A), and the layer inputs of `library/ca-f.md` ((N1)-(N3)). No consumer statement changes.

**Not shown.** See section 8: (LR) as a reading, (I-A), SU(N) for N >= 3, (Q) for B2, the coverage of B_S by the keystone region in consumer A, and the account's three-way split of the shares.

**Suggested next steps, for the lead.** (a) One line-by-line check by Codex, with attention to (LR) (does CMP 102 (145)-(168) read only box~ and the central layers?), Lemma C and Theorem G. (b) If it passes, update the CA node in `library/t0-tree.md` and its registry row. (c) Corollary B2 proves a statement the account uses and does not supply (`gates/ca-gate.md` section 4: "no noncircular supplier"). After a check, it may be a candidate under How we work item 6; nothing is posted.

**Provenance.** Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, 2026-11-06, pinned at cf6677779. Account files fetched by URL (SHA-256 as in `library/arr.md`). Balaban's CMP 102 pp. 300-305 and CMP 119 pp. 255-256, 261 were read on printed pages rendered locally from `~/ym4d-papers`; nothing was copied into the repository. No computer-assisted step; no numerical run.
