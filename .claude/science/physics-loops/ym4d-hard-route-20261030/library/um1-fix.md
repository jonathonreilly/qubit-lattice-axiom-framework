lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T09:08Z

# um1-fix: Lemma S repaired for the actual M_s; Corollary R and Theorem U re-derived (queue row 189)

Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Commit read: c9ec3475a. SA means `YM4_sketch_500.tex` at `31a47c543775`, fetched once to a scratch folder; its SHA-256 is d7f77d4d...4b6f, the file of `nl-r9.md` Section 8.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for R9 and its splitting clause (SA L10360-10402), mechanism (j) (SA L10562-10578) and the UM chapter. SA L10578 already says, for System (II), that "the member -a is diagonal and is carried by no proper set, the splitting is built around this member". This note writes that out for R9's reduced W_s. Codex found the defect and named the repair route (`b4-step.md` Section 7). Tadeusz Balaban for localisation domains joined through common walls, with local operators carried beside the decoupled propagators (CMP 109, Section 1 and (3.10)-(3.11)).

## 1. The defect, and what survives

Codex's (10)-(11) in `b4-step.md` Section 7 are correct. I confirm them. The specified raw precision is

  M_s = M_s^w - a_0 I,   M_s^w := m^3 [W_0^{-1}]_s m^{-1}   (`nl-r9.md` (4.1) and line 189),

with a_0 = 1 (`a2-layers.md` line 61). M_s^w is a walk sum, and every walk has a nonempty tag. At s = 0 every walk vanishes, so M_0 = -a_0 I. So the last two sentences of `um1.md` Step 0 are false for M_s.

What survives:

- **Statement (i)** of Lemma S needs vanishing rows only for H_1(s), G(s) and H(s). These are fully tagged. So (i) holds with no row of M_s (Section 4).
- **Statement (ii).** The diagonal -a_0 I is a local map of read radius 0, so it never joins two wall-components. But it joins the local map before it to the local map after it. This gives three joined runs: K^T (-a_0 I) C, C'^T (-a_0 I) K and C'^T (-a_0 I) C. Each joined run reads up to 2 r_loc from its output, where `um1.md` assumed r_loc. The collars of the neighbouring tags, those of G(s) and of H(s)^T inside the Neumann series, must hold 2 r_loc. Definition D's collar is (8L^2 - 9) M_1 / 2. So the repair costs one floor on M_1 after L (Section 2, (F)).
- No tag is added to the diagonal. The assigned R9 system is unchanged, as Codex requires.

## 2. Setting, positions and inputs

The setting is that of `um1.md` Section 2: a single-scale step region in level-k units, the fine grid P_f of closed cubes of side M, parameters s in D_R = {|s_Delta| < e^{kappa-bar}}, and wall-components for the relation "share a three-dimensional face" (Lemma WC of `o1-decoupled.md`).

**Positions.** Every index carries a point pi(.) of the torus. A bare bond and a force component use the base point of their bond. A raw row uses the base point of its level-k bond. A level-k fluctuation bond uses its base point. Distances are sup-norm distances between points. "P at positions in a set S" means P on the bonds whose base point lies in S; likewise for u and a.

**Depth sets.** Let W be a wall-component of P_f \ N. For rho >= 0, let D_rho(W) be the set of points q such that every cube of P_f that meets the closed ball B(q, rho) lies in W. These sets decrease in rho. Every point lies in some cube, so D_0(W) is contained in the union of W.

**Lemma 0.** Let I_W be as in `um1.md` Lemma S: the bare bonds whose base point lies in a cube of W and in no closed cube of N. Then I_W = {b : pi(b) in D_0(W)}. Hence I_W is the same set for s and for s 1_W.

*Proof.* If pi(b) is in D_0(W), the cubes that contain pi(b) lie in W, and none lies in N. Conversely, let pi(b) lie in a cube of W and in no closed cube of N. Its star St(pi(b)), the set of cubes that contain it, then avoids N. The star is face-connected (proof of Lemma WC). So it lies in one wall-component. That component contains a cube of W, so it is W. At s 1_W the zero set is P_f \ W, W is its only wall-component, and the same two arguments apply. QED

**[D+] Tagged families.** This is `um1.md` [D], with the collar written out. The tagged families are

  T = {H(s), H(s)^T, H_1(s), G(s), M_s^w}.

Each is an entrywise absolutely convergent sum T(s) = sum_omega s^{P(omega)} T_omega on D_R. Each term omega has these properties.

- (D1) A connected full read hull [[omega]]^+, with P(omega) = {Delta in P_f : Delta meets [[omega]]^+} and s^{P(omega)} = prod over Delta in P(omega) of s_Delta.
- (D2) A core hull [[omega]] that contains pi(x) and pi(y) whenever T_omega(x, y) != 0, with B([[omega]], R_coll) contained in [[omega]]^+. Here R_coll := (8L^2 - 9) M_1 / 2.
- (D3) T_omega reads P only at positions in [[omega]]^+, and it does not depend on s.

Sources, each with its check:

- H(s): `o1-decoupled.md` Definition D and Theorem B(a), (d) (checked by Codex, row 129). There [[omega]] is the union of the cubes kappa_i^(4), of side 9 M_1, and [[omega]]^+ is the union of the concentric cubes kappa_i^#, of side 8 L^2 M_1, at xi = 1. A sup-norm ball of radius R about a point of a cube of side q lies in the concentric cube of side q + 2R. So (D2) holds with R_coll = (8 L^2 M_1 - 9 M_1)/2. The transpose H(s)^T has the same terms with x and y exchanged.
- H_1(s): its own walk and tree expansion with the same full-hull convention (`o1-decoupled.md` 2.1; `pw-bridge.md` [Parameter geometry], line 319).
- G(s): `pw-bridge.md` (7.4), line 436. Each composite is tagged once on the cubes that meet the union of its factors' full read hulls and connecting derivative stencils. That union is connected. The output lies in the first factor's core hull and the input in the last factor's core hull, so (D2) holds through those factors.
- M_s^w: `nl-r9.md` line 189, its own -nu nu block walk expansion with the same full-hull convention. The diagonal factors m^3 and m^{-1} do not change supports.
- Every term, including a term of length zero, has P(omega) nonempty (Codex, `b4-step.md` (10)).

**[S-loc'] Local maps.** This replaces `um1.md` [S-loc]. The untagged maps of R9 are

  L = {C, C'(z), C'(z)^T, (C''(0)[., .])^T, K, K^T, N_0, B', the identity, -a_0 I, P -> J}.

Each ell in L has read radius at most r_loc. That is, its value at an index x depends on its arguments, and on P, u and the region geometry, only at positions within r_loc of pi(x). No ell depends on s. The identity, -a_0 I and P -> J have radius 0. r_loc depends only on L. Evidence:

- [Rows] in `nl-r9.md` Section 3: each row carrier has bounded determining diameter, and scales on it are comparable.
- N_0 has a fixed plaquette stencil (`nl-r9.md` 3.2).
- B' goes through SA's fibre chart (QC24). By SA L8283-8287, each pivot equation uses only its own pivot value and the nonpivot data of its double block, so the chart is exactly finite range.
- A transpose at most doubles a radius, through the coefficient reads at the far end.

I read these sources. I did not compute r_loc.

**(F) The floor.**

  2 r_loc <= R_coll = (8 L^2 - 9) M_1 / 2.

For L >= 3, R_coll >= 31.5 M_1, so 31 M_1 >= 2 r_loc suffices. r_loc depends only on L, so (F) is a floor on M_1 after L. SA's order (L10582) puts such floors in the L-group, before M_1. (F) replaces the floor 31 M_1 >= C_L of `um1.md`.

**[R9]** is as in `um1.md` Section 3: `dec-field.md` Proposition 5.1 from [PW] and [NL]. It solves a = Phi_s(a) := H_1(s) B'(u) - G(s) W_s(a), then h = a - H(s) C(h), and H := h, by Picard iteration from zero. W_s is (4.4) of `nl-r9.md`. Its inner map d_s(a) is the limit of d_{m+1} = C(a - H(s) d_m), d_0 = 0, and z = a - H(s) d_s(a) (`nl-r9.md` Section 5). By (5.3) there, d_s'(a)^T = A^T N^T with A = C'(z) and N^T = sum_{n >= 0} (-H(s)^T A^T)^n. The Neumann series converges in every admitted weight, since ||H(s)^T A^T|| <= 1/2 (`nl-r9.md` Section 5). All three iterations converge in norm, hence entry by entry, at every s in D_R.

## 3. Matching through the chains

Fix s in D_R, its zero set N = {Delta : s_Delta = 0}, a wall-component W of P_f \ N, and s' := s 1_W. Take two data sets, (P, u, a) and (P', u', a'). Both lie in the domains where R9's maps are defined. Assume P = P' and u = u' at positions in the union of W, and a = a' on I_W. A quantity Q is computed by one formula from (s, P, u, a) and from (s', P', u', a'); call the two results Q and Q'. Say that Q *matches at depth rho* if Q(x) = Q'(x) for every index x with pi(x) in D_rho(W).

**Lemma M.**

- (M1) a, J and u match at depth 0.
- (M2) If Q_1, ..., Q_j match at depth rho and ell in L has radius r, then ell(Q_1, ..., Q_j) matches at depth rho + r.
- (M3) If Q matches at depth rho <= R_coll and T is in the tagged class, then T(s) Q and T(s') Q' match at depth 0.
- (M4) Matching at depth rho implies matching at every larger depth. A finite sum of quantities that match at depths rho_i matches at depth max rho_i.
- (M5) If Q_n matches at depth rho for every n, and Q_n -> Q, Q'_n -> Q' entry by entry, then Q matches at depth rho.

*Proof.* (M1): for a this is Lemma 0. For J and u, use D_0(W) inside the union of W. (M4) and (M5) are immediate.

(M2): Let pi(x) lie in D_{rho + r}(W). The map reads at positions q with |q - pi(x)| <= r. The ball B(q, rho) lies in B(pi(x), rho + r), so q lies in D_rho(W), and hence in the union of W. There Q_i = Q'_i, P = P' and u = u'. The map does not depend on s. So the two values agree.

(M3): Let pi(x) lie in D_0(W), and let omega be a term with T_omega(x, .) != 0. By (D2), pi(x) lies in [[omega]]. Each closed cube that contains pi(x) lies in W, and it meets [[omega]]^+, so it is in P(omega).

- If s^{P(omega)} != 0, then P(omega) avoids N. By (D1), [[omega]]^+ is connected, and every cube that meets it is in P(omega). Lemma WC then puts P(omega) in one wall-component. That component contains a cube of W, so P(omega) lies in W, and s'^{P(omega)} = s^{P(omega)}.
- If s^{P(omega)} = 0, some Delta in P(omega) has s_Delta = 0. Then s'_Delta = 0, and s'^{P(omega)} = 0.

So the two sums at x run over the same terms with the same coefficients, and P(omega) lies in W for each of them. Such a term reads P only in [[omega]]^+, by (D3). That set lies in the union of P(omega), hence in the union of W, where P = P'. It reads Q at indices y with pi(y) in [[omega]]. By (D2), every cube that meets B(pi(y), R_coll) meets [[omega]]^+, so it lies in P(omega), hence in W. So pi(y) lies in D_{R_coll}(W), which is inside D_rho(W), and Q(y) = Q'(y). The two sums agree term by term, and both converge absolutely. QED

(M3) is the only rule that uses a tag. A local map never reads s. So -a_0 I enters only through (M2), with r = 0. Its cost is the depth that it passes on from the map before it to the map after it.

## 4. Lemma S': the repaired splitting

**Lemma S'.** Assume [R9], [D+], [S-loc'] and (F). Let s be in D_R, N = {Delta : s_Delta = 0}, W a wall-component of P_f \ N, and I_W as in Lemma 0. Then:

- (i) H(P; s, u)(b) = 0 for every bond b based in a closed cube of N;
- (ii) for b in I_W, H(P; s, u)(b) = H(P'; s 1_W, u')(b) whenever P = P' and u = u' at positions in the union of W. In particular H(P; s, u)(b) = H(P; s 1_W, u)(b), and this value depends on (P, u) only through their values at positions in the union of W.

This is the statement of `um1.md` Lemma S. Only the inputs change: [S-loc'] and (F) replace [S-loc].

*Proof of (i).* Let b be based in a closed cube Delta of N, and let omega be a term of H_1(s) or G(s) with a nonzero entry in row b. By (D2), pi(b) lies in [[omega]], so Delta meets [[omega]]^+ and lies in P(omega). Hence s^{P(omega)} = 0. So the rows H_1(s)(b, .) and G(s)(b, .) vanish, and Phi_s(a)(b) = 0 for every a. The solution therefore has a(b) = 0. The row H(s)(b, .) vanishes for the same reason, so h(b) = a(b) - (H(s) C(h))(b) = 0. No row of M_s is used. QED

*Proof of (ii).* Write r = r_loc. Each line uses only Lemma M and earlier lines. The last column names the rule and every use of (F).

| quantity | formula | depth | rule; condition |
|---|---|---|---|
| d_m, inner iterates | d_0 = 0, d_{m+1} = C(a - H(s) d_m) | r | M3 (r <= R_coll), M1, M2, induction on m |
| d = d_s(a) | lim d_m | r | M5 |
| z | a - H(s) d | 0 | M3, M1 |
| A^T v = C'(z)^T v | v at depth rho | rho + r | M2 (a local map of (z, v)) |
| N^T v | sum_n (-H(s)^T A^T)^n v, v at depth rho | rho | the n = 0 term is v; for n >= 1, M2 then M3, which needs rho + r <= R_coll; M5 |
| p_s | H(s)^T J | 0 | M1, M3 |
| T1 = -d_{3,s}'(a)^T p_s | -A^T N^T p_s + (C''(0)[a, .])^T p_s | r | N^T p_s at depth 0; M2 |
| T2 = -K^T M_s d | -K^T (M_s^w d) + a_0 K^T d | **2r** | M_s^w d at depth 0 by M3; a_0 d at depth r; **joined run K^T (-a_0 I) C** |
| T3 = -d_s'^T M_s K a | -A^T N^T (M_s^w K a - a_0 K a) | **2r** | inner vector at depth r; N^T needs **2r <= R_coll**; **joined run C'^T (-a_0 I) K** |
| T4 = d_s'^T M_s d | A^T N^T (M_s^w d - a_0 d) | **2r** | as T3; **joined run C'^T (-a_0 I) C** |
| T5 = Z^T N_0(z) | N_0(z) - A^T N^T H(s)^T N_0(z) | r | M2, M3 |
| W_s(a) | T1 + T2 + T3 + T4 + T5 (`nl-r9.md` (4.4)) | 2r | M4 |
| Phi_s(a) | H_1(s) B'(u) - G(s) W_s(a) | 0 | B'(u) at depth r; M3 for G(s) needs **2r <= R_coll** |

The formulas for T1-T5 use d_s' = N A, Z = 1 - H(s) d_s' and d_{3,s} = d_s - C_2 with C_2(a) = (1/2) C''(0)[a, a] (`nl-r9.md` (4.3), (5.3) and line 49).

*Outer iterates.* Put a_0 = a'_0 = 0. Suppose a_n = a'_n on I_W. Apply the table with (a, a') = (a_n, a'_n). Its last line gives a_{n+1} = Phi_s(a_n) = Phi_{s'}(a'_n) = a'_{n+1} on I_W. The iterates converge to the solutions of Proposition 5.1 at s and at s', both in D_R. So the two solutions agree on I_W, by (M5).

*Second contraction.* Put h_0 = h'_0 = 0 and h_{m+1} = a - H(s) C(h_m). If h_m matches at depth 0, then C(h_m) matches at depth r, H(s) C(h_m) at depth 0 by M3, and so does h_{m+1}. By (M5), H = h matches at depth 0, that is, on I_W. This is the first claim of (ii).

*The two consequences.* Take P' = P and u' = u for the first. For the second, let (P, u) and (P', u') agree at positions in the union of W. The first claim gives H(P; s, u)(b) = H(P'; s 1_W, u')(b). Applied to (P', u') alone, it gives H(P'; s, u')(b) = H(P'; s 1_W, u')(b). So H(P; s, u)(b) = H(P'; s, u')(b). QED

**Where `um1.md`'s proof broke, and why this proof does not.** `um1.md` Step 1 assumed that every run of local maps between two tags is one map of radius r_loc, and that M_s is tagged. With the untagged diagonal, the runs in T2, T3 and T4 are two maps long. The table shows where they end: in the input collar of G(s), and, inside N^T, in the input collar of H(s)^T. (F) says that these collars hold the joined stencils. Without the diagonal, depth r would suffice on every line, which is `um1.md`'s floor.

*Kill attempt.* Could the diagonal carry s-dependence across a wall? Only through a read at a point outside D_0(W), since local maps do not read s. In the table every read lies in D_0(W) once (F) holds. If (F) failed, the joined run in T2 could reach a bond of another wall-component W'. There the iterates differ in general: a'_n vanishes on W' by (i) at s', and a_n need not. G(s) would pass that difference to b, and this proof would stop. This does not refute (ii) without (F); it shows that (F) is where the proof uses the size of the collar. (F) holds above a floor on M_1, because r_loc does not depend on M_1.
