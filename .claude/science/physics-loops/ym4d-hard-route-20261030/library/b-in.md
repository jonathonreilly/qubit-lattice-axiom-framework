lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T02:47Z

# (B-in): the sealing construction on D_2 beside S

Queue row 389 (`b-in`). Started 2026-11-06T14:47Z at commit cf6677779. Proved by Claude, not yet checked by the other model. Work in progress; sections are added as they are written.

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

- **(B-in-w), base bound.** For every cell x of K with o(x) >= 1: Q_a(x) <= (phi_flat/64) theta^{B^t}_a(x) for a in {1,3,5,6,7} at the pair (U_2, J(U_2)); at every triple of the readings (Sigma^flat), (Sigma^*) at x, entries 2 and 4 at most phi_flat/64 of their thresholds; and on every cube of Q_{B^t} that lies in K, and on every frozen-family cube of a dissolving piece, a gauge u with U_2^u = e^{i eta A} and L^lambda eta |A|, (L^lambda eta)^2 |nabla A| <= (phi_flat/64) w_cube B C M alpha_{0,lambda}.
- **Why it suffices for R(b).** The clause of tau at x has threshold at least F_tau theta^{B^t}_a(x) >= phi_flat theta^{B^t}_a(x): for a stage-domain clause the structure read at x is the frozen one of B^t (precedence rule, I:132982-132986); for an earlier-born term, heredity (e2) of `4.27:lem-weights-heredity` (I:133096-133098; that lemma is marked incomplete at other steps) gives theta^{B}_a >= theta^{B^t}_a for B before B^t, as used at I:136670-136673; a finer birth index n < o(x) only enlarges r_a by (eq-factors-radii-coupling-2), I:131441-131446; and F_tau >= phi_flat is clause (a). "For all w >= 1" in the printed (b) is stronger than any consumer reads. See section 7 for why the stronger form is not claimed.
- **(Sh-w), shares.** At every cell x of K with o(x) >= 1, every entry of the presented pair at b_3, b_4 and on every segment differs from its value at b_2 by at most (3/64) phi_flat theta^{B^t}_a(x), the cube gauges being those of U_2.
- **(Pl), placement.** For every piece c dissolving at the step, W_c is contained in K, and so is every frozen-family cube of c.
- **(S-B).** The cells of level >= 1 meeting the one-bond neighbourhood of Col(C), and the index-zero cubes meeting Col(C), lie in K.

The split into three shares (bend, source, map H') of the printed (c) is not read by any consumer; only the total 3/64 is. The account also asserts its base bound "for all F >= phi_flat, w >= 1, c >= 1" (I:138438-138444); taking F = phi_flat, w = w_{B^t}(x), c = 1 is the case every consumer reads.

## 3. The sealing construction, defined from the account's objects

The account names the construction (I:138361-138366) but states none of its theorems. Every object below is the account's or Balaban's; only K and B_S are chosen here.

- **The configuration.** U_2 := U_{B_2}(V_2), the minimal configuration of CMP 122b (1.53) for B_2 = B''_k u B_h((Omega''~_{h+1})^c) (CMP 122b (1.52), quoted at I:92417-92421). By CMP 119 (2.14) (local, p. 257), B u B_j(Omega) = (B n Omega^{~-2}) u (B_j(Omega) n (Omega \ Omega^{~-2})): the support of B_2 is Omega := (Omega''~_{h+1})^c; there B_2 has the blocks of B''_k except in the graded layer of width 2M_1 blocks at the cut (I:92515-92532). U_2 reads V'' only off Omega''^{~2}_{h+1} (I:138407-138411); it is real (current localisation, hypothesis (c), I:92446-92448).
- **The chain.** b_2: the pair (U_2, J(U_2)), A' = 0. b_3, b_4: the left factors e^{i eta t_3 H_3}, e^{i eta t_4 H_4} with the layers H_3, H_4 of `4.22:lem-current-localisation`, and the partner currents of ca-f Lemma S as source increments; t_3, t_4 in [0,1] give the segments.
- **Graded region and cut region.** G := (support of B_2) \ S. On G, B_2 = B''_k and V_2 = V''. The cut region is the rest of the support: the graded layer and S.
- **Core and B_S.** Z_h^{(1)} := the points within sup-distance 2CML^h eta of Z_h (C <= 2 the cube constant of CMP 122a (1.65)). K := the blocks of B''_k contained in Z_h^{(1)} n Lambda; B_S := D_2 \ K. The objects Gamma_flat, "bend floor" and "ownership floor" of I:138455-138462 are not needed: their only role there is to make the shares and the cube clause hold, and sections 5-7 prove these directly under named ceilings.

## 4. The reset at one block (input) and its iteration (proved)

**Input (LR), the local reset.** This is the one place where this note reads a checked text in a new way; the checker should confirm it. There are constants B_3 >= 1, R_1M_1 >= 1, a_5 > 0, fixed in b102's order from d, L and the group, with this property. Let (B, V) be an admissible instance of b102 Theorem 1 (`library/b102.md` section 1, (T1)-(T4)), and U a critical configuration of it in the regular class (T1). For a block Delta = B^j(y) of level j, let box(y) be the cube of side 2R_1M_1 L^j eta through Delta and box~(y) its concentric enlargement with dist(box, box~^c) = 2R_1M_1 L^j eta (CMP 102 (144)). Let

  r(y) := the least r such that U obeys (T1) at radius r on every plaquette and bond of box~(y);
  e(y) := the least e such that the data tests of CMP 102 (7) hold at radius e on the two central layers inside box~(y).

If r(y) <= a_5, then U obeys (T1) on Delta at radius max{ B_3 e(y), r(y)/2 }.

*Source and reading.* Balaban, CMP 102 section F, pp. 300-304, (144)-(168), read on the printed pages (rendered from `~/ym4d-papers`): the gauge (145)-(146) uses the space (2) on box~ only; the local problem (147)-(151) lives on C_k inside box~, with artificial data equal to the averages of U itself; (160) uses the data assumption (7) only on the central layers; (161) splits the sum into the central part and C_k \ box_k, the latter carrying e^{-delta_0 R_1M_1/2} epsilon_0; (163)-(168) give the radius max{B_3 epsilon_1, epsilon_0/2} on Delta_0 = B^j(y). Balaban states it with global epsilon_0, epsilon_1 and iterates (Proposition 8); the argument at one block reads only r(y) and e(y). b102 rebuilds it as H21, "Reset for any already constructed critical field" (`library/b102.md` 2944-3021: "Freeze the actual averages of U on the artificial outer boundary ... The local field is therefore critical for that local problem"), checked line by line by Claude, first failing step none (`gates/b102-gate-b.md`). b102 proves SU(2), d = 4, uniformly in depth, spacing, volume and admissible nest.

**Lemma I (iteration).** Let Y be a set of blocks, N(y) := {z in Y : z meets box~(y)}, N^0(y) := {y}, N^{i+1}(y) := union of N(z) over z in N^i(y). Let rho, e : Y -> [0, infinity) with rho bounded, and suppose rho(y) <= max{ B_3 e(y), (1/2) sup_{N(y)} rho } for every y. Then for every y

  rho(y) <= B_3 sup_{i >= 0} 2^{-i} sup_{z in N^i(y)} e(z) = B_3 sup_z e(z) 2^{-d_N(y,z)},     (I.1)

where d_N(y,z) := min{i : z in N^i(y)} (infinity if none).

*Proof.* Claim: for every m >= 1 and every y, rho(y) <= max{ B_3 max_{0<=i<m} 2^{-i} sup_{N^i(y)} e, 2^{-m} sup rho }. For m = 1 this is the hypothesis, since sup_{N(y)} rho <= sup rho. If it holds for m at every block, insert it at each z in N(y):

  rho(y) <= max{ B_3 e(y), (1/2) sup_{z in N(y)} max{ B_3 max_{i<m} 2^{-i} sup_{N^i(z)} e, 2^{-m} sup rho } }
         =  max{ B_3 max_{i<m+1} 2^{-i} sup_{N^i(y)} e, 2^{-m-1} sup rho },

because the union of N^i(z) over z in N(y) is N^{i+1}(y). Let m tend to infinity; rho is bounded. QED.

**Theorem G (graded reset).** Let (B, V) be an admissible instance of b102 Theorem 1 with all data tests at most a_1, let U be its minimal configuration, and let rho(y) be the least radius at which U obeys (T1) on the plaquettes and bonds attached to the block y (a plaquette is attached to the block of its base point, a bond to the block of b_-; each test is read at the largest level j with p, b in Omega_j, as in (T1)). Assume (LR). Then for every block y, rho(y) <= B_3 sup_z e(z) 2^{-d_N(y,z)}.

*Proof.* b102 Theorem 1 puts U in the regular class at radius B_3 a_1 <= a_5 (b102 chooses a_0, a_1 last, "so that B_3 a_1 < a_0 and every preliminary radius above fits those fixed radii", lines 3066-3069). So rho is bounded by B_3 a_1 (Balaban fixes a_1 so that this radius is at most a_5, CMP 102 p. 304), and r(y) <= sup_{N(y)} rho <= a_5 for every y, since every plaquette and bond of box~(y) is attached to a block that meets box~(y). The conclusion of (LR) on Delta = y covers the tests attached to y. (LR) gives the hypothesis of Lemma I. QED.

Theorem G is linear in the data: each data test enters with the factor 2^{-d_N}, whatever its level. The rest of the note estimates sup_z e(z) 2^{-d_N(y,z)} at the blocks the consumers read.
