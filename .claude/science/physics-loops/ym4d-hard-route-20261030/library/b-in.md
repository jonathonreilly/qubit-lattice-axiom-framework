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
