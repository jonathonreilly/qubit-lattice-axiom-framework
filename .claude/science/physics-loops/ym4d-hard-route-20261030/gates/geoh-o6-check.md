# Check: library/geoh-o6.md

Checked line by line by Claude (Opus 5.5), 2026-11-08. One check, not an audit.
Note: `library/geoh-o6.md` (490 lines, Codex gpt-6-astra). Contract: `library/cls.md`, `library/drlocp-draft.md` (DRL), `library/geoh.md` 261-280, N = YM4_1400.tex.

## Verdict: FIX (minor)

The mathematics is right. (A) the member bootstrap, (B) the winding carrier, (C) the three routes and (D) the periodic replacement all hold.
Four small repairs are needed, because some written claims say more than the proof gives. None of them changes the outcome (c) or the proposed contract.

## Findings

### (B) Winding indexed carrier, §5

1. **Allowed index.** Note 221-226; CLS 229-233; DRL 272. CLS sums over every `V ⊂ C_i \ N_f`. DRL takes any finite `V` with `V ∩ N = ∅`. Neither puts a size, length or span cutoff on `V`. So `V = C_p \ N_f` is an allowed index. (7) follows from `Y = N_1(N_f ∪ V)` and CLS 276. **CONFIRMED.**

2. **Component support rule.** Note 232-233; DRL 352, 362. `x` is a read cube, so `x` lies in some stencil `B_b ⊂ X_f ⊂ N_f`. The cycle `C_p` is connected and lies in `N_f ∪ V`. So every `v ∈ V` joins `B_b` inside `N_f ∪ V`. **CONFIRMED** for the `V` part of the rule.
   **MISMATCH (minor).** The rule also kills the piece unless `W ⊂ N_f ∪ V`, and `W` must be gas. Line 233 says without condition that the rule "does not remove this index". Line 324 adds the right condition: "whenever its selected gas cubes exist". The contract failure in §5 does not need a `W`, because CLS 462 asks Lift for every indexed carrier. **Repair:** at line 233 add "for every gas `W ⊂ N_f ∪ V`, when such `W` exists". Or note that the line through `x` can be chosen to meet distant gas on a large torus.

3. **Span obstruction for even `p`.** Note 239-244. Representatives of `0` and `(p/2)e_1` differ by an odd multiple of `p/2`. So no box of side `< p/2` holds both. More margin and more filling only make the set larger. **CONFIRMED.**

4. **Parity scope.** Note 218 vs status row 484; N 61913; geoh.md 271. §5 fixes an even period. The status table says "for every nonempty filing input". The level-`j` period is `ell L^(K-j)` with `L` odd, so the period can be odd. Then the antipodal pair does not exist. **MISMATCH (fixable).** **Repair:** use a residue count. A box that holds the image of `C_p` must hold all `p` residues of the `e_1` coordinate, so its `e_1` side is at least `p` cubes. This works for every `p`, with any side convention. For routes 2-3 with odd `p`, use three cubes spaced about `p/3` apart, with `W` of size 3 and `D_W` of `zeta_a zeta_b zeta_c`. Any arc that holds all three has length at least about `2p/3 > p/2`.

5. **Scope of (B).** Note 9, 246-280, 484. The note says this is a failure of the contract as written, not a physical-history counterexample. It claims no nonzero coefficient. The isolated-cell pattern (8) is called a pattern, not a certified fibre. **CONFIRMED.** The word "genealogy" at line 235 is loose: `V` is a summation index, not a process. This is harmless.

### (A) Member bootstrap, §4

6. **Recursion (2).** Note 119-141; CLS 96-98. The parent core sits in `N_e(N_c U)`, so its span is at most `a+2e` and `rho <= eta(a+2e)+1`. The member lies in `N_(e+rho+c+5)H`. With `L>=27` and `c>=0`, `ceil((e+rho+c+5)/L) - c <= (e+rho)/L + 32/27`. Then `(1+2eta) <= 3/2` and `1/L+32/27 < 2` give (2). The periodic coarsening step works: lift a shortest displacement, then use CLS Lemma 2's integer inequality. This needs aligned periods `p_(j-1) = L p_j`. **CONFIRMED.**

7. **Sum (3).** Note 143-158. Drop gives `a_(j-k) <= L^ceil(k/2) a_j`. The term is `eta a_j (3/2)^(k-1) L^(-floor(k/2))`. Paired terms give `1 + (5/3) sum (1/12)^m = 38/33`. The second sum is `2/(1-1/18) = 36/17`. Both bounds are below `2 eta a_j + 3`. **CONFIRMED.**

8. **Chart and (4).** Note 160-178. The hub box, enlarged by `c+e_j`, has side `a_j+2e_j < 2a_j+16 < p_j/2` by (1). So it projects one-to-one, and the torus set `N_(e_j)(N_c U_j)` is its image. Then `rho_j <= eta a_j(1+4eta) + 6eta + 1 <= 2eta a_j + 2`, since `eta <= 1/8`. The side is `a_j + 8 eta a_j + 16 + 2b <= 2a_j + 16 + 2b`. **CONFIRMED.** The sentence on Mon at line 163 is not needed for the span bound. It does no harm.

9. **(5) and "no CLS output-side estimate".** Note 180-186. `2a_j+16+2b = 2CL r_j + 28 + 4c + 2b <= (2CL+28+4c+2b) r_j`. The proof uses hub charts, G, Drop, Mon and (1). It does not use CLS Lemmas 3-4. The hub charts are a stated input. **CONFIRMED.**

10. **Tree span paragraph.** Note 188-203. A tree with `n` edges, lifted from a root, has span `<= n`. It gives no bound on `d_f`, `|V|` or the MST. **CONFIRMED.**

### (D) Replacement and consumers, §7

11. **D3, Lemmas 3-4.** CLS 85-141. The §4 chart exists before `rho_j` is used. Lemma 3-4's sharper bounds then run inside that chart. Separation and gas gaps are torus triangle inequalities. **CONFIRMED.**

12. **Lemma 2.** CLS 73-83. The distance and neighbourhood inequalities hold on the torus. A cycle in the image graph is removed as before. The bound `s(πA) <= ceil(s(A)/L)+1` needs a chart, but it is used only on members, which have charts. **CONFIRMED.**

13. **Lemma 5.** CLS 143-145. Containment comes from (1) on the torus. Lemma 2 bounds the edge count. **CONFIRMED.**

14. **Lemma 6.** CLS 151-173. The depth-first code count needs only degree `<= 80`. The island count uses member disjointness. `V_* = (D*_j)^4` uses a member chart. **CONFIRMED.**

15. **Lemma 7.** CLS 177-214; AG1 14-32. Geodesics, connector cost and gap are periodic. Crossing a core uses its chart. AG1 does start on a periodic lattice with sup-distance. **CONFIRMED, with one gap.** The proof also uses TD Lemma 1's lattice sum `sum_z e^(-6 d(z,z_0)) <= 2` (CLS 204). The table row does not name it. **Repair:** add one sentence. The shortest-representative injection at note 427-431 bounds the torus sum by the lattice sum.

16. **Lemma 8 shell count.** CLS 249-256; note 427-431. Take the representative with coordinates in a fixed half-open window of length `p`. Its sup norm is the torus distance. Distinct torus cubes give distinct representatives. Norm `n` puts the representative on a face of `[-n,n]^4`, so there are at most `8(2n+1)^3` of them. `|R| <= s^4` uses the core chart. **CONFIRMED.**
    **Gap (minor).** Lemma 8 also calls DRL Lemma 5.1 (CLS 270; DRL 405-412). Each non-root vertex there uses `sum_v e^(-s d(v,v_p)) <= 2` (TD (9)), which is a lattice sum. **Repair:** state that the same injection gives the torus version.

17. **Lemma 8 filling, cluster joins.** CLS 276, 278. `Y*` and its spanning tree are torus graph objects. Incompatibility edges and Gaussian stars are periodic. G-P on a winding support stays an input, and the note says so at 425. **CONFIRMED.**

18. **Table coverage.** CLS 312-322. Lemma 9 uses member diameters and `d(p,q)`. It goes through with periodic distance. The table leaves it out. **Repair:** add a Lemma 9 row. Lemmas 10-11 are explicit models in a large torus, not consumers, so they need no row.

19. **`A_loc` at CLS 462.** Note 438-448; geoh.md 268-280. GEOH Theorem 4 needs supplied boxes of side `<= A_rd M R_j`. The floor with `A_rd >= 2CL+28+4c+2b` implies (1) at every level, so the §4 boxes exist. The order has no cycle. **CONFIRMED.** **Repair (wording):** GEOH (13) already uses the name `A_loc` for `2CL+8+2c+2c_rd`. That value rests on Lemma 4's side bound, which depends on Lift. Say that the note's larger constant replaces GEOH (13) for the bootstrap, or rename it.

20. **Scope of the replacement.** Note 409-412, 433-436, 450-454. It drops only the demand that every carrier fit in one chart. It keeps D4, the companions and the Match conditions as inputs. It says that local gauge suppliers do not apply to winding carriers. This follows N's C2 (N 2329-2330, "with their winding retained"). **CONFIRMED.**

### (C) LIFT-ONE, §6

21. **Statement.** Note 288-299. Full Lift at CLS 462 implies LIFT-ONE. So calling it a "necessary sublemma" is right. **CONFIRMED.**

22. **Route 1.** Note 301-317. Union with `V` happens at the same scale, with no factor `1/L`. It fails at the step it names. **CONFIRMED.** It restates §5 at the level of the recursion. It is still a distinct mechanism: contraction.

23. **Route 2.** Note 326-357. At `s = 1_(N_f ∪ A)`, the product over `C_p` is 1 only when `A = V`. `D_W` of `zeta_a zeta_b` is `zeta_a zeta_b`. So (10) holds exactly. `F` meets both support rules and is holomorphic, and a small `epsilon` meets any amplitude bound. The note calls it a test of the mechanism, not a response. **CONFIRMED** (for `4 | p`; see finding 4).

24. **Route 3.** Note 359-386. A lift that keeps every edge of the cycle shifts the coordinate by `p`. Deleting one edge leaves span `p-1`. Any function that reads only a half-period chart misses `a` or `b`, so `D_a D_b` of it is 0. This stays true under finite or absolutely convergent sums. **CONFIRMED.** Routes 2 and 3 share the witness (9), but they test different mechanisms: decay and cancellation, then cutting and refiling. They count as distinct.

25. **Stopping outcome.** Note 7, 284-286, 388-390. Outcome (b) needs an actual history and a nonzero coefficient. Neither is shown. So (c) is the correct label. **CONFIRMED.**

### Honesty of scope

26. Note 456-471 and the status table. Each port is marked as input, sketched, or "proof outstanding" in its source. N 2320-2332, 61908-61914, 63684-63692, 70104-70112 and 82915-82923 say what the note says they say. The note's claim that §7 is "proved here" needs findings 15, 16 and 18 to be complete. **CONFIRMED, apart from findings 2, 4, 15, 16, 18, 19.**

## Repairs, in one list

1. Line 233: make the support-rule sentence depend on a gas `W ⊂ N_f ∪ V`.
2. §5 and row 484: use the residue count so the result holds for any period, or limit row 484 to even `p`. For routes 2-3 with odd `p`, use three cubes about `p/3` apart.
3. §7 table: add the torus version of TD Lemma 1's sum (Lemma 7) and of DRL Lemma 5.1's non-root sum (Lemma 8), using the same injection.
4. §7 table: add a Lemma 9 row.
5. Line 441: separate the new constant from GEOH (13)'s `A_loc`.
