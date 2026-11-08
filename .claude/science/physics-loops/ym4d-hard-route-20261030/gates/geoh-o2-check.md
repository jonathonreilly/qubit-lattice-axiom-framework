Verdict: FIX

# Line-by-line check of library/geoh-o2.md (440 lines)

Checked line by line by Claude (Opus 5.5, fresh session), once. Branch `claude/ym4d-hard-route` at 2bed22991.
I read the note in full, its task file, `prior/geoh.md` (GEOH-O2 row, verdict item 2), `geoh.md` 8-18 and 142-169, `gates/geoh-gate.md`, `in1.md` 60-90 and 145-190, and `sa-2.13.md` 104-118 and 220-232.
Source lines read: N 4150-4182, 73086-73100, 73145-73196, 74248-74322, 74613-74672, 75913-75966, 77136-77157, 78488-78527, 78846-78940, 61926, 96520; SA 17274, 17552-17568, 18082-18115, 18673-18717; CA-I 85575, 166650-166668.
No computation is used.

Summary. Every proved step checks. Every ported citation reads as stated. The defect is in the target. UO2 is stronger than IN1 H-G and N 78917 need. Its item 3 includes the analytic per-site charge density. That density is a hypothesis of other rows. So two of the three route failures are not failures of a geometric supplier. A narrower geometric supplier is stated in Finding 9. Route two nearly proves it.

## Findings

**1. L79-91, (2). CONFIRMED.** Source: geoh.md L11, |x_j - θ_j| ≤ θ_j/4, θ_j ≥ X_0 > e. ℓ ≥ 1 + λ - log(4/3) ≥ λ. ℓ ≤ 1 + λ + log(5/4) ≤ 3λ, since λ > 1. log x ≥ log(3e/4) > 0.

**2. L99-107, (3). CONFIRMED.** Source: geoh.md L11 with i = j-1 gives θ_{j-1} ≤ θ_j + B̄. Then x_{j-1} ≤ (5/2)θ_j and log x_{j-1} < λ_j + 1 ≤ 2ℓ_j. The four series terms give 8/3 > 5/2. Small point: the extra floor X_0 ≥ B̄ is already implied by geoh Lemma 1 (X_0 ≥ 4B̄, geoh L68). No new floor is needed.

**3. L109-133, (4). CONFIRMED, with one wording repair.** The collar bound (1 + 2c_0/R_n)^4 ≤ 2 checks against N 74274-74290. The product 2(MR_n)^4 · μL^4 · 2ℓ_n gives 4μL^4. The source v is SA 17274 (also N 61926): it counts log x_j per stored site. CONFIRMED. Repair: L114 should say "per owner occurrence and per level-n site". The sum in (4) uses that reading. Note also that (4) lets an owner sit one level above the site. geoh (7) asks for an owner at the site's own level (geoh L150). Say that (4) replaces geoh (7) for IN1's reserve clause, with C_v = 4μL^4.

**4. L50-60, ported table. CONFIRMED.** N 74615-74647 (D ≤ L^4+3^4+2, D^{2(N-1)}), N 74649-74669 (exp(bV°) under fixed tests per site), N 74250-74271 ("No third tree meets it"), N 74274-74300 (read-site budget), N 74302-74320 (restored versus retained load), N 78917-78923 (C_d assertion), N 4163-4171 ("finite read ownership" in H_step), CA-I 85575 ("Proof outstanding") and CA-I 166652-166659 all read as stated. SA 18673-18690 proves the rooted count; SA 18692-18701 sketches the code.

**5. L183-202, L296-345, other ports. CONFIRMED.** N 73088-73099 (no level-zero region), N 73147-73158 (five read uses), N 73181-73194 (seam tags), N 75915-75965 (I_W(s), row assignment, stopped sharp-test branch), SA 17558-17564 (background differences), N 78490-78525 ("There is no new factor for the number of later levels"), N 78848-78861 (kernel composition) and N 77136-77157 (carrier criterion) read as stated. sa-2.13.md 220-232 gives (7) as (6.1).

**6. L249-255, collar overlap 2·3^4. CONFIRMED.** With c_0 < R_j, a point lies in at most three intervals per coordinate. Same-level nodes are disjoint (geoh L161). A clearing node occurs twice (N 74266-74268).

**7. L296-339, (9) and (12). CONFIRMED.** (9) telescopes. In (12), the mean of K is 1 and the mean of sup_p K is 2. This is the same phenomenon as IN1's own example at in1.md L188.

**8. L384-399, (13). CONFIRMED.** The per-address log-count is at most log2 + 2JμL^4 v_n log K + log(3K_f) + p log(R_n+1). Since ℓ_n, v_n ≥ 1 and log(R_n+1) ≤ c_Rℓ_n (geoh L163), (13) follows. Remark: the code needs only discrete test slots per site (N 74655-74659: "a fixed finite number of such tests is attached to each site or bond"; sa-2.13.md 104: "at most J s(v) addresses"). Tying J to the charge count μ is sufficient but not needed.

**9. L153-165, UO2 itself. MISMATCH: stronger than the consumers need.**
- IN1 H-G (in1.md L156) needs only two things: the code count, and v ≤ C_v v♮ for SA's v. SA's v counts stored sites (SA 17274; SA 18087-18091 counts them "at their own levels, including the assigned collars and the operation's fixed coordinate multiplicities"). The note says this itself at L76: a repeated read creates no stored site.
- N 78917-78923 asks that "each such read belongs to its owning cell collar, with a bounded covering multiplicity C_d". N 78923-78926 adds: "No factor counts the number of later reads of a mark." Its load (N 78872-78878) counts sites #_j per level, not factor incidences.
- The per-site count of analytic charges is a separate hypothesis. In N it is the carrier density f̄ of N 77136-77157 (sup over owned sites of Σ_f b_f/|R_f|). In SA it is "the rooted sum is a constant per stored site" (SA 18092-18094). In IN1 it sits in H-E (16) as C_env V°. UO2 item 3 restates that hypothesis as a slot count. L344-345 says the carrier criterion does not bound "multiplicity in the actual history". But its sum over f already runs over every carrier at the site, with multiplicity. So it is that bound, as an analytic input.
- Repair. Split UO2. **UO2-geo**: (a) every stored site of s_j, with SA's assigned collars and coordinate multiplicities, has one creating occurrence (n,Q), n ∈ {j, j+1}; (b) every read used by the code or by N's load (five uses, N 73147-73158) lies in its owner's c_0-collar at its own level or one level up; (c) per owner and per site the multiplicity is at most a template constant μ_0. **UO2-an**: the per-site analytic density. Leave UO2-an to the analytic rows (N 77136-77157; IN1 H-E). GEOH-O2's consumers then need UO2-geo only.

**10. L171-230, route one. UNCLEAR as a GEOH failure.** The failed step (6) is the count of new charged uses e_s from the differences d_s. SA 17564 bounds each localized piece of d_s at the stage that forms it: modulus ≤ C(log x_i)^{-(q-3p_0-Cr)} e^{-c d(Y)}. So the piece is a level-i analytic term on level-i domains. It is not a new geometric incidence at A's old site. Later reads of a kept island are paid once by N 78490-78525. So (6) fails only for UO2-an. For UO2-geo, rows 1-2 of the ledger at L196-197 and H-LF ("each variable retained or integrated exactly once", in1.md L145) already give (a), as L228 says.

**11. L290-354, route three. MISMATCH in placement.** The failure at (11)-(12) is sup_p∫ versus ∫sup_p. That is IN1's "Outstanding — common domination" (in1.md L188), an H-E row. L350 says no analytic estimate of another row is attempted. It should also say that the failure point is that row's open item. Route three is then not a distinct failure of a GEOH supplier.

**12. L257-277, route two. CONFIRMED for UO2 as stated; it nearly proves UO2-geo.** (8) is right: a union forgets repeated incidences. But under UO2-geo each (level, use, site) is counted once per owner. The uses per owner and site are then at most 5 uses × 2 levels × μ_0, a template constant. The covering bound 2·3^4 of Finding 6 then gives N's C_d. L272-277 is right that a k-j > 1 conversion fails. That is why UO2-geo (b) needs the remade-layer owner at the layer's own level (Finding 13).

**13. Route not in the note (concrete).** Take N's four owner rules (N 78906-78916). An unaltered layer site goes to its action cell (one step, L^4). A remade determining site goes to the mark that remade it, at its original level. A prepared mean goes to its owned level cell. With nested marks, use the latest owner. Realize the remade-layer rule at the level-j node of the standing mark's chain in the genealogy. That node exists if the chain carries a node at every window level (geoh waiting chain; IN1 H-G "chain ... at most T_t light nodes"). The disjoint windows of nested standing marks (geoh mark rule; sa-2.13.md 6.1 text) make that owner unique. Then (a) is H-LF, (c) is the template, and the covering count is Finding 6. The one open input is (b): for every revised-operation read, its finite stencil lies within c_0 M-layers of that owner's cells, with c_0 early. This is exactly N 78917-78919. I have not proved (b). I also have not checked that the mark chain has a node at every remade level.

**14. L404-415 and L440, scope. MISMATCH, fixable.** The stop is (c), one supplier failing three routes. Findings 9-11 show the supplier mixes geometry with analytic inputs of other rows. Two route failures are those analytic inputs. Repair: restate the stop as "UO2-geo open at (b); UO2-an belongs to N 77136-77157 / IN1 H-E". The rest of the scope is honest. No status is claimed. (4) and (13) are correctly marked conditional. L269 and L338-339 correctly say the counterexamples refute only inferences.

## Repairs, in order

1. Split UO2 into UO2-geo and UO2-an (Finding 9).
2. Restate the route outcomes: route one closes UO2-geo (a); route three's failure is IN1's common-domination row; route two gives the covering count (Findings 10-12).
3. State the next task as UO2-geo (b) along Finding 13.
4. Wording: L114 per owner (Finding 3); (4) replaces geoh (7)'s same-level owner; drop the redundant floor at L99 (Finding 2).
