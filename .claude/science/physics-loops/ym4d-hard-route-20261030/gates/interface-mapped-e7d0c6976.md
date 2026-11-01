lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T19:06Z

# Gate: interface-mapped, at e7d0c6976

**Provenance.** Model claude-opus-5-5, effort high, fresh session on the Mac mini, side mapped, commit `e7d0c6976`. A same-model check is not independent in model and is not an audit. Verdicts steer research and grant no status. This is a reading of statements only: no proof was checked, and "repair" always means unproved.

**Overall.** The interface does not close as written. No clause is shown false. One claim the attempt relies on is false: that no consumer reads an isolated deep mark. Defect D1 breaks the producer of the upper chain's class on this map, and so everything down to (SM). D2 to D5 are independent of D1 and each stops a named consumer step. D6 to D10 are wording or constants, each with a cheap repair.

## Verdict table

The mapped attempt's deliverable, set beside what the upper chain consumes. "Fits" means fits as a statement, and it stays conditional on (Z) and its gaps.

| Upper chain consumes | Mapped delivers | Verdict |
|---|---|---|
| Prop 8.1 hypothesis at w = 0 | "Deliverable: UV-LOC-R", with no source carried | Not delivered as a statement. D7 |
| (RAR^1_j) at depth one, top regular | (Z) with marks, Lemma OW | Fits, apart from parents (D2) and separation (D6) |
| (RAR^1_j), (20.2) below a top at any depth, all of LL_j | (Z), leaf sets only | **WRONG: the claim that this is not read.** Not delivered. D1 |
| (RAR^1_j) under mu, "free given (FF_l)" | Quiet in l^2 on bricks | **WRONG as written on this map.** Conclusion not refuted. D2 |
| (RAR^ch_j) at a regular top and under mu | Class-top corollary of (Z), (A1') | Not delivered: not a leaf set. D3, and D1 for depth |
| (MD*_j) | Prop MD* | Fits. Closure of the second tier unstated (D5). Layer constants (D6) |
| (SCR_j), (DEC_j) | Nothing direct; Prop 20.4 from (MD*_j), (20.2) | Inherits D1 and D2 |
| Lemmas 22.1, 22.2 | Own mirrored exploration, own constants | Hypotheses not met at mapped's numbers. D6 |
| (GS_j)(a), (c), (d) | Text 5.8, counts | Constants (D4), tier (D5), test class (D8) |
| (GS_j)(b), a > 0 | a = 4 at flat, counts | Fits |
| (C2_j) | Text 5.8 | Tails stated at a rate the class cannot take. D5 |
| (CF_j), (LE_j), (REG_j), (R3) with kappa = 1 | Text 5.8 | Fits. (R3) is local with tails, so (LE_j)'s Ebar is met |
| (Q_j) | R_k in derivative form | Fits the use, agreed in Requests. Clause text stale, D10 |
| (FF_j) truncated | Text 5.8, `library/quiet-boundary-rarity.md` | Fits at eps_1 <= T only. Proof text retired. D9 |
| Lemma 10.6 covariance, even torus | Planes through level-j sites, L odd | Fits for the planes it reads. Range, D10 |
| (LOC), Lemma 20.3 | R_loc, labels as variables | Fits. Clearance and range wording, D10 |
| (FLOW) | Theorem P1 | No mismatch. (T3) is not stated on this map, and follows from the flow at x >= x_* |

## Defects, ranked by what each breaks

**D1. (RAR^1_j) and (20.2) below a deep regular top are read, and (Z) does not give them. Breaks the producer of Lemma 20.5 on this map, so Theorem 14.13, Theorem 14.1c and (SM).**

The attempt says "An isolated deep mark does lose per level; no consumer reads one" (`parts/hard-core--mapped.md:26`, `library/quiet-boundary-rarity.md:87`). The gate at 60036ba4d, D4, says the same: "or to depth one, which is what the consumers read". The upper chain reads one.

- LL_j holds the law of V_j below a regular W_0 at any level i > j (`parts/upper-chain.md:799`).
- (RAR^1_j) and (20.2) are asked below such a top (`parts/upper-chain.md:823`, `:1215`).
- The depth is forced. (K3) at level j + 1 at a point mass reads (K3) at level j under its image at depth one, and so on down, so level 0 is read at depth j + 1. Lemma 20.5 uses pi_j(A) and (RAR_(j+1)) for every nu' in LL_(j+1) (`parts/upper-chain.md:1256`, `:1258`).

*Failure.* Take S one brick at level m, and a top regular everywhere at level l = m + n. Then col_k(S) >= C(t_0) d_x^4 at each k between m and l, so the loss in (Z) is about n C log x_m, and the gain is (1/4) x_m c_S eps_q^2 T^2. The bound is empty once n >= c x_m eps_q^2 T^2 / (C log x_m), and the slope of the flow does not pay, as the gate's D4 says. The event H^c at level j has the same defect. It is a chain of h = 3 D / (28 w_0) separated cells with one ball per level above level j, so it fails at depth about h times that number. Depth reaches K - j, of order x_j / b', so this needs h >= C log x_j / (c eps_q^2 T^2 b'), while D = m / 2 with m near r_(j+1) gives only h of order log x_j / (kappa w_0). The rarity itself is not refuted, and it is expected to hold up to the bounded shift below, since a rough parent forces rough children only over a number of levels depending on L and a_*.

*Repair (unproved).* A same-top ratio at a class top, with no ball entropy:

    (DM)  for V class on the region inside a stop, F_l^{S, 𝔡}(V) - F_l^𝔡(V) >= (1/4) sum_k x_k Delta_k(S), with no column loss on class fields.

Route: in Step 4 split W_B. Where W_B is class on B, both integrals carry the same exp(-F_{l-1}) dW, so the ratio recurses with no n log x. Where W_B is rough on B, a rough cell's own x T^2 pays n log x, and the mark keeps its gain from (Z). The obstacle recorded at `parts/hard-core--mapped.md:43`, a certificate reaching a rough parent with different parents above and below, does not arise, because LL_j tops are regular everywhere and the recursion stays inside a stop with quiet data. A mark forced by a non-regular parent moves its cost up by a bounded number of levels, which replaces lambda_l by lambda_(l+h). Under mu no repair of this kind is needed, since the chessboard has no top.

**D2. (RAR^1) under mu is not "free given (FF_l)" on this map. Breaks the Corollary of 22.3 as written, and with it (20.2) under mu.**

The upper chain reads quiet as a flux threshold eps_1 := eps_0 / C_2 and prices it by Lemma 10.6 (`parts/upper-chain.md:1474`, `:1211`). Here quiet is Dev_b <= eps_q^2 T^2 with regular parents on the patch (`library/quiet-boundary-rarity.md:19`), and `parts/hard-core--mapped.md:240` says so, but the Corollary was not redone.

*Failure.* Take parents of flux near T_2 and V_l the lift, flux up to T/4, plus a relative field in the fibre with angle eps_q T / t_0^2 per cell. Then Dev_b is above threshold and no plaquette exceeds any flux that separates this brick from a quiet one, so X-tilde prices nothing. The same event also has the case of a non-regular parent, which is non-quiet by definition, and (O2') is stated only with regular parents (`library/quiet-boundary-rarity.md:157`).

*Repair (unproved).* A deterministic lemma: if parents and level-l plaquettes on b^++ have flux at most tau := c(t_0, L) eps_q T, then Dev_b <= eps_q^2 T^2. Then apply Lemma 10.6 at levels l and l + 1 with the union over plaquettes of a patch, and Cauchy-Schwarz between the two levels. This gives a positive rate, near t_0(L) x tau^2 / C with this t_0 the moment parameter of (U^r). It lowers l_0, l_1. Both still come before gamma, so the order of constants survives, as (TT) needs only l_0 large.

**D3. (RAR^ch_j) is not a corollary of (Z). Stops the (K2) recursion of Lemma 20.5.**

(Z) marks are leaves of a witness forest, and a tree stops at a non-quiet parent (`library/quiet-boundary-rarity.md:61`, `:231`). The nested event Ch_(j,s)(c) has a rough cell at each consecutive level, so it is not a leaf set. R_k pays inside the infimum over chains, in a bound on the unrestricted F_l, so no mass with prescribed rough cells is bounded. (A1') expands one level at a time (`library/quiet-boundary-rarity.md:137`). The upper chain's 23.4 item (3), "Theorem Z with marks gives the marked (U)", holds only for leaf sets. The older route by (RP'^S_k), `parts/hard-core--mapped.md:964`, is listed as not consumed.

*Repair (unproved).* State (Z) for F_l restricted to chains with prescribed cells in R_k, and assign each column ball to a cell at its own level. The count then holds for a stack at consecutive levels, with marks at most R_j apart costing about log_L x_j extra levels each. Arbitrary sparse S_l, as (RAR^ch_j) is worded, are not consumed, so that clause can shrink to the stacks of Ch_(j,s)(c). At a rough top, adding back F(V^fl) leaves x-tilde_{l-1} A(c) plus the summed Delta_k, and Lemma TE then gives a factor per level, so no positivity at a rough top is needed. Depth above the stack is D1.

**D4. (GS_j) constants: the consumer needs them free of L, and the attempt states them free of x. Would break Lemma 14.15(a), (b), so Theorem 14.13.**

The clauses ask C_n polynomial in n and free of L up to powers of log L (`parts/upper-chain.md:816`), and theta_r <= L/2, theta_rho <= 1/4 read that (`:940`). The attempt defines "constant" as free of x (`parts/hard-core--mapped.md:266`), and its route says derivatives are "bounded free of the volume and of x" (`:903`), through a chart whose gap is gamma(L). A factor L^p, p >= 1, in C_n breaks theta_r <= L/2. Only the leading covariance is argued free of L (`:912`). Nothing shows that C_n does grow.

*Repair (unproved).* State (GS_j)(a), (c), (d) with the leading part as the Landau Gaussian of the curvature, free of L, and put every C(L) g into omega_L(g) t_n^2, which the clause allows. The coefficient of t_n^3 has to be checked free of L.

**D5. The second tier is missing from (GS_j)(d), (C2_j)(c), and the attempt's own tails are stale. Stops Lemma 14.15 Step 3 and the (K1) line of Lemma 14.16 as written.**

(GS_j)(d) and (C2_j)(c) carry one exponential, exp(-c_F m) (`parts/upper-chain.md:821`, `:824`). Lemma HS-T has a second term, poly(x) z^{1/2} exp(-rho_s' tau) (`library/preconditioned-covariance.md:108`). At large m this is above exp(-c_F m) L^4 omega_j. Text 21.7 puts the second tier in (MD*_j) and the profile, not in these clauses. Separately, `parts/hard-core--mapped.md:918`, `:984` state tails at the rate of (J), delta_0(L) per box, with coefficient C(L) g^2, and say no place was found where this hurts. It would hurt: (K1) has kappa absolute, and 21.7 says kappa must not come down to a tail's rate, while the second tier of Phi_j is of size zeta_j, far below g^2. Also Prop MD* still closes with "a much larger exponent" (`library/quiet-boundary-rarity.md:181`), which 23.4 showed is not true of the second tier at small D.

*Repair (unproved).* Restate both clauses with the HS-T second tier, which fits under Phi_j by z^{1/8} <= zeta_j and kappa_s <= c_s/16. Replace the (J) sentences by HS-T. State the (TT)-type condition log(1/z_j) against (c_t / c_s) log L / L in Prop MD*.

**D6. Lemmas 22.1, 22.2 do not apply at mapped's layer numbers.** "Text 22 is uniform" (`parts/upper-chain.md:1507`, `:141`) needs w_0 >= 3 b. Mapped's brick has side t_0 and its layer has thickness t_0, so b = w_0. "w + 2 b L <= 2 w" then fails (`:1448`). (RAR^1) is asked at separation 7 w / 3, and mapped's marks are 12 t_0 apart (`library/quiet-boundary-rarity.md:61`).

*Repair (unproved).* Take w := 6 t_0 in the consumer's parameters, so w_0 = 6 b and 7 w / 3 = 14 t_0. This needs t_0 >= r_S L / 3, which t_0 >= C L log(1/T) allows for C large. No count above changes.

**D7. UV-LOC-R is named the deliverable and is not delivered.** `parts/hard-core--mapped.md:14` says deliverable UV-LOC-R. `:865` and `:1046` say no source is carried and that plan is superseded. So Prop 8.1's hypothesis is reached only as an output of Theorems 14.1b, 14.1c, and is not an input from this attempt. Its wording is also too strong for that route: "supports of measure at most v" in `:262` and in `parts/upper-chain.md:429`, against the delta-neighbourhood in (SM) (`:418`), since Theorem 14.1c's bound carries N_k(f), and N small bumps have small support and large count (the gate's D11, cited there).

*Repair.* Name the Text 14 clauses as the deliverable, and use the neighbourhood in Prop 8.1 and in UV-LOC-R.

**D8. (GS_j) test class.** The clause has |e| <= 1 + tau_n^2 + tau_n^3 (`parts/upper-chain.md:821`). The route is written for bounded e, with sup |e| in every bound (`parts/hard-core--mapped.md:903`, `:907`). *Repair (unproved):* Gaussian moments in the chart, with rare sites at weight z.

**D9. (FF_j).** The clause allows eps_1 <= eps_0 = T_2; the attempt has eps_1 <= T (`parts/hard-core--mapped.md:889`). *Repair:* t_1 reduced by (T_2/T)^2, still absolute. The derivation at `:887` to `:889` reads (RP_j[0]) and 𝔹, which are retired (`library/quiet-boundary-rarity.md:51`, `:199`), and Obligation `:203` still lists them. The live form is `library/quiet-boundary-rarity.md:139`, so (FF_j) now rests on (Z) and its gaps, and it is not a separate implication.

**D10. Wording and small constants.** (a) Lemma 20.3 needs r_S L above the family's diameter, here R_loc of order (2 J + 2) L. The definition of r_S (`library/quiet-boundary-rarity.md:35`) does not state r_S >= 2 J + 3, and r_* has no definition in the text I read. (b) Lemma 10.6 has p at least 2 cells from a face and b >= 6, and on this kernel V_j reads about 2 J + 3 level-j cells. Take b_0 >= 4 J + 8, still absolute. (c) Stale in the upper chain, since parked: the range 2 L + S_* + d_1 at `:69`, the flux definition of quiet at `:1211`, (LOC) in two blocks at `:822`, the additive form in (Q_j) at `:825` against its own `:140` item (1), and `:146`, which `parts/hard-core--mapped.md:281` answers.

## Read and not read

Read: `FINISH.md`, `GOAL.md`. Mapped file: State of attack, Obligations, Requests, Text 5.8, 5.10, 5.6, 4. `library/quiet-boundary-rarity.md`: setting, Theorem Z and its proof as statements, consequences, Lemma OW, Prop MD*, the restated induction, hostile (12) to (19). `library/preconditioned-covariance.md`: statement of Lemma HS-T. Upper chain: State of attack, Obligations, Requests, Text 7, 8, Lemma 10.6, (FF_j), (OS_j) statements, the Text 14 clauses, Lemma 14.10, 14.16, Text 16 audit table, the L-adic paragraph of Text 15, Text 20 and 21 statements, 21.7, Text 22, 23.1 to 23.4. Gate at 60036ba4d: D4 only. Gate at bad958abb: one search of its lines.

Not read: any proof for its truth; Text 5.9 and the bulk of `library/`; (OS_j) as a consumer, which belongs to the milestone and not to this item's list; the upper chain's Theorem 10.7; the Sussman-Alpoge repository, not needed for statements.

Firewall kept: I opened neither `parts/hard-core--independent.md` nor any gate on that attempt, and I ignored the upper chain's rows about it. The upper chain's clauses cite that attempt's labels, and those were seen only as they stand in the upper chain.

No numeric job was run, since nothing here was decidable by one. No `checks/` folder and no library file were written. Evidence for the upper chain's owner is D1, D2, D3, D5, D6, D7, D10(c), for the lead to forward under the firewall.
