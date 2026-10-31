# NQ_DEF.md — what Setting SC's Q actually is, and what 𝔮₀ therefore is (target T55-P)

Owner: the T55-P worker, session 25. Append-only. Anyone may read it; nobody else writes it.
I write only this file and `checks/nd1_*`. I ran no git command, made no commit, no push, no PR.

**Line-number convention, stated once (REVIEW_NQ_S1 F6 asked for this and it is adopted here).** Every PROOF.md,
NORMS.md, LINEAR_PACKAGE.md, NQ_CHECK.md, REVIEW_NQ_S1.md and SESSION25_RESULTS.md line number in this file resolves
in the **live** file as of 2026-10-28 21:48 UTC, not in any snapshot. PROOF.md's numbering has drifted twice this
session, so every PROOF.md citation below is also given as a quoted string, which is the stable locator.

---

## §D0 PRE-STATED (first edit of this file, 2026-10-28 21:48:57 UTC; statements only; cites nothing produced in this session)

This section was written before any derivation, any script, any computation and any conclusion of mine. Nothing below
§D0 existed when §D0 was written. It names its inputs; it quotes no result produced in session 25.

**The question (T55-P).** NORMS.md §N4's named input **(N-Q)**: *‖Q^{j}‖_{∞→∞} ≤ 𝔮₀L^{j} for a constant
𝔮₀ = 𝔮₀(L, d), uniformly in j*, with ‖·‖_{∞→∞} = max_c Σ_b |·(c, b)| (the induced sup→sup operator norm = max row ℓ¹
sum). NORMS.md §N4 calls this *"a question about a DEFINITION, not a theorem"* and says it is *"immediate with
𝔮₀ = 1 for the straight average"*. SESSION25_RESULTS.md's T55-F entry names (N-Q) as **Theorem N1-15's only remaining
input** and asks whether Theorem N1-15 is therefore unconditional. NQ_CHECK.md (session 24) claims (N-Q) PROVEN as
Theorem NQ-1 with **𝔮₀ = 1 + d(L+1)/(2L) = 11/3** at d = 4, L = 3 — not 1 — and REVIEW_NQ_S1.md reviewed that claim.

**Named inputs I will read (naming them is not citing a session-25 result).** PROOF.md (Setting SC; L3g-ob;
L3g(a)-glob; L3g(a)-slice; J-str; IT-str), LINEAR_PACKAGE.md §0–§3, NORMS.md §N1/§N3/§N4/§N6/§N8/§N9/§N10,
NQ_CHECK.md, REVIEW_NQ_S1.md, SQ.md §0.4/§11.0, SESSION25_RESULTS.md's T55-F entry, TUNIF.md.

**Targets.**

- **TD1 (the definition, from the definition).** Locate Setting SC's definition of Q **by string** in the live
  PROOF.md and quote the defining sentence with its live line number. Do not accept any file's description of it.
  Then locate, in LINEAR_PACKAGE.md, the definitions of the three objects that sentence points at (the root map, the
  straight average, the slice functional) and quote them with line numbers. Report which of the three operators is
  Setting SC's Q.
- **TD2 (𝔮₀ from the definition).** Compute ‖Q^j‖_{∞→∞} from that definition. If Q is the straight average, report
  𝔮₀ = 1 and say so. If it is not, give the actual 𝔮₀ and say whether (N-Q) holds with it.
- **TD3 (re-derive, do not cite).** Re-derive Theorem NQ-1's statement from its two claimed inputs (the slice
  identity and root covariance) by my own induction and my own norm computations, and either confirm 𝔮₀ or refute
  it. A banked PROVEN and a banked review are evidence, not certificates.
- **TD4 (reconcile 1 against 11/3).** Decide which of three things the pair (1, 11/3) is: the same operator with two
  bounds, two different operators, or one bound that is not tight. Verify **by file:line** which operator each number
  is about. Report it as an instance of, or a counter-instance to, systemic defect 1.
- **TD5 (does the difference matter).** Determine whether any named consumer needs 𝔮₀ = 1 rather than 𝔮₀ = 11/3 —
  specifically whether 𝔮₀ enters any exponent, any level-ratio that must be < 1 (A_soft), or any smallness threshold.
  If 11/3 suffices everywhere, say the distinction is academic, plainly, rather than manufacture a problem. If some
  consumer needs 1, name it.
- **TD6 (the quantity that is actually load-bearing).** State which property of 𝔮₀ Theorem N1-15 consumes — its
  value, or its independence of j — and what the theorem's conclusion becomes if that property fails.
- **TD7 (consequence for Theorem N1-15).** State exactly what becomes unconditional, in exactly which regime, and
  what does not. The regime caveats (d = 4, trivial background, abelian/linearised) are load-bearing and must travel
  with any claim. Name what is still open.

**Pre-registered failure modes (things that would make my answer wrong, written before I look).**

- **Q-F1.** Setting SC has more than one definition of Q in the live PROOF.md, or the definition points at an object
  that is itself undefined. Then the finding is "a load-bearing operator left undefined" and TD2–TD5 change character.
- **Q-F2.** The operator in (N-Q) is not the operator in Setting SC — e.g. NORMS' Q is a third object, or the Q in
  Lemma N1-11's step (4) is not Setting SC's. (Systemic defect 1, applied to the symbol Q itself.)
- **Q-F3.** 𝔮₀ enters an exponent or a level-ratio and not only a prefactor, so that 11/3 vs 1 is decisive at d = 4.
- **Q-F4.** Theorem NQ-1's bound is stated for composites anchored at level 0 while its consumer needs composites
  anchored at an arbitrary level, and the proof does not deliver that.
- **Q-F5.** My own check is unable to fail (systemic defect 3). Every gate below carries a designed-FAIL control, and
  a control that passes when it should fail voids the gate.
- **Q-F6.** (N-Q) is discharged but Theorem N1-15 has an input I have not enumerated, so "unconditional" is wrong.

**Pre-registered criteria for the one computation I expect to run (check nd1).** Criteria go in
`checks/nd1_criteria.md`, written before the script exists; the constants in them (L = 3, d = 4, L^j = 3, 9) are
Setting SC's own hypotheses, not session-25 outputs. Exact `Fraction`/integer arithmetic, plain python, one process,
no numpy, no BLAS, no numeric lock (brief rule 6).

**Not success.** Declaring (N-Q) settled by citing NQ_CHECK or REVIEW_NQ_S1 rather than re-deriving it; reporting
𝔮₀ = 1 because it is the convenient answer; calling Theorem N1-15 "unconditional" without carrying the regime
caveats; asserting that 11/3 breaks something without naming the consumer and the threshold; running a gate with no
designed-FAIL control.

---

## §D1 What Setting SC's Q is (TD1): SETTLED FROM THE DEFINITION — it is **not** the straight average

**Warning, and the reason this section quotes strings.** `PROOF.md` was modified at **21:51:15 UTC**, i.e. between my
first and second read of it this session. Every line number in this section was re-resolved **after** that write, at
22:05 UTC, and the region containing Setting SC moved by **+25** during my own session (l.2200 → l.2225). The quoted
strings are the stable locators; the numbers are a convenience with a timestamp.

### D1.1 The defining sentence

> **PROOF.md l.2225-2226** (the definition of Setting SC, inside "*Setting SC (linearised soft chain)*"):
> "*Q is the linearised S4' map from level i to level i + 1 (**Q_root of L3g(a)-slice, with the S4' order average**).*"

There is exactly **one** defining sentence for Setting SC's Q in the live file (`grep -c` on the string returns 1), so
pre-registered failure mode **Q-F1 does not occur**: the operator is not left undefined. It is defined by reference, and
the three objects it refers to are themselves defined:

> **PROOF.md l.760-762** (S4′, the contour family): "*For each of the d! coordinate orders σ, let P^σ be the
> complete-axial transporter moving in the coordinates in the order σ, and
> **T^σ_y = P^σ(c_X → y) · S_y · P^σ(c_Y → y + L e_μ)^dag**, with S_y the straight leg of L steps.*"
>
> **LINEAR_PACKAGE.md l.70**: "*For small abelian fields the averaged link is
> **Q_rootA(X, μ) := avg_{σ,y}∫_{T^σ_y}A** (the "root map").*"
>
> **LINEAR_PACKAGE.md l.71**: "*The **straight average** is **(Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)**.*"
>
> **LINEAR_PACKAGE.md l.72-73**: "*With the **slice functional** h(A)(X) := avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}A, the exact
> identity **Q_root = Q_str - d∘h** holds … Root covariance: **Q∘d = d∘ev**, ev the restriction to roots.*"
>
> **PROOF.md l.1292-1293** (L3g(a)-slice, the same identity at its source): "*with h(X) := avg_σ avg_{y∈B(X)}
> ∫_{P^σ(c_X → y)} A, the linearised average is **Q_root A = Q_str A - d h**.*"

**Answer to TD1: Setting SC's Q is Q_root, the S4′ order-averaged root map. It is NOT the straight average.** The
straight average is a *named different object in the same sentence that defines the root map*, and the two differ by
the exact coarse 1-form d∘h, which is nonzero.

### D1.2 The consumer forces the same answer, so this does not rest on which file one reads first

NORMS Lemma N1-11 step (4) transports with **B_j = Q^{j}B_0 − Σ_{i<j}Q^{\,j−1−i}r_i**. That is an *identity* only for
Setting SC's Q, because the residual is *defined* as r_i := QB_i − B_{i+1} (PROOF.md l.2228-2230, LINEAR_PACKAGE l.88).
NORMS' own Lemma N1-4 writes the Q_str version and qualifies it — the Q_str chain relation holds only "**modulo a
level-j pure gauge**". A *potential* bound cannot use that version, because the discarded pure gauge is the very thing
being bounded. So (N-Q) is a question about Q_root or it is not the input Lemma N1-11 needs. **Q-F2 does not occur.**

### D1.3 Where the lane's "Q is the straight average" belief is TRUE, and this is the key to §D4

It is true of the **transpose on co-closed forms**, and that is a genuinely used statement:

> **PROOF.md l.2258** (Lemma J-str's proof): "*L3g(a)-slice: Q = Q_str - d∘h exactly, so Q^T = Q_str^T - h^Td*.
> **On co-closed r the funnel term h^Td*r vanishes.***"
> **PROOF.md l.2261**: "*So **||Q_str^T||_{∞→∞} = L^{1-d} = L^{-3}**.*"

So the lane holds two statements, both correct, about the same operator:

| direction | the object | what is true | where used |
|---|---|---|---|
| **forward, on potentials** | Q = Q_root | Q ≠ Q_str; the difference d∘h is nonzero | **(N-Q)**, Lemma N1-11 step (4), TUNIF Cor. TU-5 |
| **transpose, on co-closed residuals** | Q^T = Q_str^T **exactly** | ‖Q_str^T‖_{∞→∞} = L^{1−d}, exact | J-str (b)(c); the residual decay L^{−(d−1)(n−1)} of Thm N1-15 steps (3)(4) |

The extra power of decay that makes Theorem N1-15's series converge (Remark N6-1: "*the residual's extra power of
decay — L^{−(d−1)} per level, from J-str (c)*") comes from the **transpose** statement, where the straight average is
exactly right. The funnel survives only in the forward direction, on the potentials — which is precisely the slot
(N-Q) is about. **That is how the lane came to believe both "Q is the straight average" and "Q is not", without
either belief being an error.**

---

## §D2 𝔮₀ from the definition (TD2), and check nd1

Since Q ≠ Q_str, NORMS §N4's one-line route is unavailable. I computed ‖Q^j‖_{∞→∞} directly from the definitions of
§D1.1, in exact rational arithmetic, in code that imports nothing from `nq1_qnorm.py` (session 24) or from
REVIEW_NQ_S1's `revnq1/`. Criteria: `checks/nd1_criteria.md`, written 21:56 UTC, **before** `checks/nd1_qrow.py`
existed. Script `checks/nd1_qrow.py`, output `checks/nd1_out.txt`, resources `checks/nd1_time.txt`
(**3.10 s wall, 175 MB peak RSS**, single thread, `python3 -I`, `nice -n 10`, load average 1.93 at launch, **no
numeric lock taken** — brief rule 6's exemption for exact rational arithmetic in plain python).

### D2.1 The numbers

| object | support (one row) | row ℓ¹ = ‖·‖_{∞→∞} | exact |
|---|---|---|---|
| h | 216 | **8/3** = 2.666667 | = d(L²−1)/(4L) |
| Q_str (LINEAR_PACKAGE l.71) | 135 | **3** = L | exact |
| Q_str (NORMS §N1 l.103-104) | 81 | 3 = L | exact |
| **Q_root = Setting SC's Q**, j = 1 | 459 | **205/27** = 7.592593 | R₁ = 205/81 = **2.530864** |
| **Q_root^{(2)}**, j = 2 | 47 385 | **2021/81** = 24.950617 | R₂ = 2021/729 = **2.772291** |

All four link directions agree at both j. **‖Q‖_{∞→∞} = 205/27 > 3 = L.**

### D2.2 The answer to TD2, and it is a refutation

**𝔮₀ = 1 is FALSE for Setting SC's Q.** Any valid 𝔮₀ obeys 𝔮₀ ≥ sup_j ‖Q^j‖/L^j ≥ **205/81 = 2.5309**. So the
"straight average ⟹ 𝔮₀ = 1" route is not merely unproven — it is **excluded by a factor 2.53 at j = 1 alone**, by an
exact computation whose only inputs are Setting SC's own contour definition.

**(N-Q) holds, with 𝔮₀ = 1 + d(L+1)/(2L) = 11/3 at d = 4, L = 3** (proof re-derived in §D3), and the true constant
lies in the interval **[205/81, 11/3] = [2.531, 3.667]**.

### D2.3 Gates and their designed-FAIL controls — all five gates PASS, all five controls FIRED

| gate | result | its designed-FAIL control | control result |
|---|---|---|---|
| **A** slice identity Q_root = Q_str^LP − d∘h, entrywise | **PASS**, 0 differing entries × 4 directions | **A′** the same with NORMS §N1's Q_str | **FAILED AS DESIGNED**, 108 differing entries × 4 |
| **B** ‖Q_root‖ > L | **PASS**, 205/27 > 3 × 4 | **B′** the same code path on Q_str^LP | **FAILED AS DESIGNED**, returns exactly 3 |
| **C** values and session-24 bounds | **PASS**, 205/27 ≤ 25/3 ≤ 11; 2021/81 ≤ 91/3 ≤ 33 | **C′** value strictly between L^j and p_L^j | **holds at both j** (neither frame is right) |
| **D** telescoping at j = 2 (§D3 Step 1) | **PASS**, 0 differing of 47 385 × 4 | **D′** far-end shift Le_μ instead of L²e_μ | **FAILED AS DESIGNED**, 33 534 differing × 4 |
| **E** root covariance Q^{(j)}(d₀λ) = λ(L^je_μ) − λ(0), j = 1, 2 | **PASS** × 8 | **E′** Q_str^LP in place of Q_root | **FAILED AS DESIGNED**, fired in **2 of 8** cases |

**The honest qualification on E′, which I report because it is the "could this check have failed?" lens applied to my
own control.** E′ fired only for μ = 0 (at both j). It *could not* fire for μ = 1, 2, 3 with my pre-registered λ, and
the reason is structural, not accidental: for a 0-form that is **quadratic** in the direction tested, the block mean
and the root value differ by the *same* constant at both ends of the coarse link, so the difference d∘M − d∘ev
vanishes identically. My λ was cubic only in x₀. **A quadratic test function cannot distinguish Q_str from Q_root at
all** — the same defect the hostile reviewer found in session 24's gate G2. POST-HOC probe P1 (labelled post-hoc in
the output; run after seeing E′) confirms this is a property of λ and not of the operator: with λ₂ = x₂³ + x₃³ the
control fires in directions 2 and 3 and not in 0 and 1. Taking E′ and P1 together, the control fires in every
direction, but **only P1's half of that is post-hoc**, and I do not claim pre-registered status for it.

### D2.4 What I did not run, declared in advance

`j = 3` (‖Q³‖ = 6115/81, two independent session-24 computations). Declared not-attempted in
`checks/nd1_criteria.md` before the run: ~4.1·10⁶ entries and ≥ 480 MB on a machine shared with seven agents, for a
third data point on a question settled analytically in §D3.

---

## §D3 Theorem NQ-1 re-derived, not cited (TD3)

Session 24's `NQ_CHECK.md` §Q3 and `REVIEW_NQ_S1.md` Part C both assert this. **Neither is used below.** The proof
here is written from the two identities quoted in §D1.1 and from four elementary norm facts, three of which I also
measured (§D2.1) and the fourth of which is one line.

**Setting.** Own units at every level (PROOF.md l.2222-2223: "*the level-i lattice is a torus in its own units
(spacing 1)*"), so **Q_i is the same operator at every level i**, with block side L. Write, for the step i → i+1,
S_i := Q_str, H_i := h (level-i 1-forms → level-(i+1) 0-forms), D_{i+1} := the level-(i+1) coboundary on 0-forms,
E_i := ev_i (level-i 0-forms → level-(i+1) 0-forms, λ ↦ λ∘c). All norms are ‖·‖_{∞→∞} = max row ℓ¹, the induced
sup→sup operator norm, which is **submultiplicative**.

**Theorem NQ-1′ (re-derivation; PROVEN-HERE).** *Let d ≥ 2, L ≥ 3 odd, and let Q be Setting SC's averaging operator.
For **any composite of m consecutive levels**, on Z^d and on every torus,*

  **‖Q^{(m)}‖_{∞→∞} ≤ L^m + (d(L²−1)/(2L))·(L^m−1)/(L−1) ≤ 𝔮₀·L^m,  𝔮₀ := 1 + d(L+1)/(2L),**

*uniformly in m and in the starting level. At d = 4, L = 3: 𝔮₀ = 11/3.*

**Step 1 (an exact operator identity).** For a ≤ b put Π(b,a) := Q_{b−1}∘⋯∘Q_a. Then

  **Π(b,a) = S_{b−1}⋯S_a − D_b·Σ_{i=a}^{b−1} (E_{b−1}⋯E_{i+1})·H_i·(S_{i−1}⋯S_a),**

empty products read as the identity.
*Proof, by induction on b − a.* For b − a = 1 this is the slice identity Q_a = S_a − D_{a+1}H_a itself. For the step,
Π(b,a) = Π(b,a+1)∘Q_a = Π(b,a+1)S_a − Π(b,a+1)D_{a+1}H_a. Root covariance Q_i∘d_i = d_{i+1}∘ev_i applied b − a − 1
times gives Π(b,a+1)D_{a+1} = D_b·E_{b−1}⋯E_{a+1}. Substituting the inductive form of Π(b,a+1) into the first term
just appends S_a to every straight product. Collecting, the i = a term appears with an empty S-product. ∎

Three things to note, because each is a place this could have gone wrong.
- **The identity is on ALL level-a 1-forms, with no co-closedness restriction.** The forward slice identity
  Q_root A = Q_str A − dh(A) is stated for every A (PROOF.md l.1292-1293); co-closedness enters only in J-str's
  *transpose* statement (§D1.3), where what must vanish is d*r.
- **The single D sits at the top level, outside the sum.** That is what makes the whole correction *one* coarse exact
  form, and it is what control **D′** tests: moving its shift from L²e_μ to Le_μ breaks the identity in 33 534 entries.
- **The expansion uses ev, not the block mean M.** This is the whole content of the theorem (see §D4.3).

**Step 2 (four norms).**
1. **‖S_{b−1}⋯S_a‖ = L^{b−a}, exactly.** A single Q_str row is **non-negative** with row ℓ¹ sum
   L^{−d}·L^d·L = L (L^d block sites y, L links each, weight L^{−d}; coincident links merge, which cannot change a sum
   of positives). A product of non-negative matrices with constant row sum L has constant row sum L^{b−a}. *Measured:
   3 at one level (gate B′); the non-negativity is in the definition.*
2. **‖E_{b−1}⋯E_{i+1}‖ = 1.** ev has exactly one entry 1 per row; a composite of restrictions is a restriction.
3. **‖H_i‖ = ‖h‖ ≤ d(L²−1)/(4L).** P^σ(c_X→y) is a monotone axial path of exactly |y − c_X|₁ distinct links, each with
   coefficient ±1, so the row ℓ¹ mass is at most
   avg_{σ,y}|y − c_X|₁ = L^{−d}Σ_{y∈B(X)}|y − c_X|₁ = d·(2/L)Σ_{t=1}^{(L−1)/2}t = **d(L²−1)/(4L)**, using **L odd**
   (Setting SC hypothesises it) so that c_X is a lattice site and the block is centred. *Measured: exactly 8/3 at
   (L,d) = (3,4), so the inequality is an equality there.*
4. **‖D_b∘G‖ ≤ 2‖G‖** for any G into level-b **0-forms**: (D_bG)(X,μ;·) = G(X+e_μ;·) − G(X;·), two terms, so
   ‖D_b‖_{∞→∞} = 2 exactly, in every d. *This is a coboundary on 0-forms, not on 1-forms; the d-dependent term count
   of a coboundary on p-forms does not arise, and that is exactly what the slice identity buys by putting the funnel
   into a coarse **exact** 1-form.*

**Step 3 (assembly).** Submultiplicativity and the triangle inequality give

  ‖Π(b,a)‖ ≤ L^{m} + Σ_{i=0}^{m−1} 2·1·(d(L²−1)/(4L))·L^{i}
          = L^m + (d(L²−1)/(2L))·(L^m−1)/(L−1) = L^m + (d(L+1)/(2L))(L^m−1) ≤ 𝔮₀L^m,  m := b−a. ∎

**Torus.** Every input of Step 2 holds verbatim on a torus: Q_str is still non-negative with row sum L when block
legs wrap, ‖ev‖ = 1 and ‖D‖ = 2 are counts, and ‖h‖ is still bounded by the average path length. No periodisation
argument is needed.

**Numerical consistency with §D2.** The theorem's sharp form gives 25/3 = 8.3333 and 91/3 = 30.3333 at j = 1, 2,
against the computed 205/27 = 7.5926 and 2021/81 = 24.9506: the bound dominates by **+9.8 %** and **+21.6 %**, and
𝔮₀ = 3.6667 dominates max_j R_j = 2.7723. The only lossy step is ‖H_iS^{(i)}‖ ≤ ‖h‖L^i; POST-HOC probe P2 measures
the true values ‖hQ_str^{(i)}‖ = 8/3 and 56/9 at i = 0, 1, i.e. 2.667 and 2.074 after dividing by L^i, so the slack
is **stable, not growing** — the signature a false bound would not have.

**Generality of the constant — a defect-2 check (is L = 3 still an input?).** POST-HOC probe nd1b
(`checks/nd1b_hnorm.py`, `nd1b_out.txt`, 1.09 s, 19 MB) verifies ‖h‖ = d(L²−1)/(4L) and ‖Q_str‖ = L **exactly at nine
(L,d) pairs** with L ∈ {3,5,7,9} and d ∈ {2,3,4}, with a designed-FAIL control (the formula d(L+1)/(4L)) that fired
in 3 of 3 cases. So the constant is not an L = 3 artefact. Moreover 𝔮₀ = 1 + d(L+1)/(2L) is **strictly decreasing in
L** (11/3, 17/5, 23/7 at L = 3, 5, 7, d = 4; → 1 + d/2 = 3), so **L = 3 is the worst admissible case** and
𝔮₀ ≤ 11/3 holds for every odd L ≥ 3 at d = 4.

**Quantifier (pre-registered failure mode Q-F4).** The statement above is for **any** composite of m consecutive
levels, not only for composites anchored at level 0, because nothing in Steps 1–3 uses the starting level and Q_i is
the same operator at every level in own units. That is what Lemma N1-11 step (4) actually consumes: it needs
‖Q^{\,j−1−i}‖ for the residual transport starting at level i+1, and m = 0 gives the identity, of norm 1 ≤ 𝔮₀.
**Q-F4 does not occur** (it was a real gap between the session-24 statement and its consumer; REVIEW_NQ_S1 F3 asked
for the same one-line repair, and this re-derivation supplies it rather than citing it).

**Scope, which must travel with the statement.** **Abelian / linearised only.** Input 1 of Step 1 (the slice
identity) has no nonabelian analogue — PROOF.md records this in terms at L3g(a)-slice's [R3-fix]: "*the identity is
linearised and abelian only: the nonabelian straight average is not even covariant, so there is no nonlinear SU(N)
analogue*". **Theorem NQ-1 therefore does nothing for (N-bg)** and nothing for (N-loc).

---

## §D4 How NORMS' "1" and NQ_CHECK's "11/3" reconcile (TD4): **two different operators, and a third one nobody noticed**

Answering the brief's three-way question directly: they are **not** the same operator with two bounds, and **not** one
loose bound. They are about **different operators**, and the conditional that joins them has a **false antecedent**.

### D4.1 The two numbers, each pinned by file:line

- **"𝔮₀ = 1"** — NORMS.md **l.403**: "*It is **immediate with 𝔮_0 = 1 for the straight average**: ‖Q_str^{j}‖_{∞→∞}
  = L^{j} exactly …*", and NORMS.md tally item 15 at **l.809-810**: "*immediate with 𝔮_0 = 1 **if Setting SC's Q is
  the straight average***". This is a statement about **Q_str**, inside a conditional. It is **true of Q_str** (§D2.1
  measures ‖Q_str‖ = L exactly and §D3 Step 2.1 proves ‖Q_str^{(m)}‖ = L^m), and its **antecedent is FALSE** (§D1.1).
- **"𝔮₀ = 11/3"** — NQ_CHECK.md §Q3 / §Q5 item 1, re-derived here as §D3. This is a statement about **Q_root**, and
  §D2.2 shows no smaller-than-2.53 constant is available for that operator.

So the reconciliation is: **one true statement about Q_str, one true statement about Q_root, and a conditional whose
"if" does not hold.** Nothing in the lane is wrong *as written*; what is wrong is the expectation that the conditional
would discharge. **This is systemic defect 1 in its mildest form** — not a wrong number asserted of the wrong object,
but a **live hope** resting on a false antecedent, which has now been quoted forward three times (NORMS l.403, NORMS
l.809, and TUNIF.md **l.678**, written this session).

### D4.2 The live instance: TUNIF.md carries both numbers, four pages apart

`TUNIF.md` (target T55-F, this session) **l.120** imports (N-Q) as a numbered input:
> "*(I-C) **Theorem NQ-1** (NQ_CHECK.md): ‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j uniformly in j, **𝔮_0 = 1 + d(L+1)/(2L)**.*"

and the same file at **l.678** says:
> "*if Setting SC's Q is the straight average, **𝔮_0 = 1** and Theorem N1-15 is **unconditional** …*"

Both sentences are defensible in isolation (l.678 is quoting NORMS' conditional), but read together they invite the
reading that 𝔮₀ is an open number between 1 and 11/3 that someone should go and determine. **It is not open**: l.120
is correct and l.678's antecedent is false. The forward pointer should be repaired (FOR OTHER FILES item 2).

### D4.3 Why NORMS also *derived* a different (polynomial) constant, and who is right

NORMS §N4's own estimate (l.409-417) reaches "*𝔮_0 ≤ 1 + 2d‖h‖·j/L — only **POLYNOMIAL** in j*", with a named hole
("*h applied to a pure gauge*"). That is a **third** number for the same quantity. I adjudicate it from my own Step 1
rather than from either session-24 file:

- Expanding Q^{(m)} with the **block mean M** (using Q_str∘d = d∘M) gives the composite slice functional
  h^{(m+1)} = M h^{(m)} + h Q^{(m)}. The second term feeds h the output of the **root** map, and
  Q^{(m)} = Q_str^{(m)} − d h^{(m)} contains the object being bounded. **Self-referential**: the circle has to be
  broken by charging the upward transport a generic L^{j−1−i}, and that is where the factor j comes from.
- Expanding with the **root restriction ev** (using Q∘d = d∘ev) gives h^{(m+1)} = ev h^{(m)} + h Q_str^{(m)}, i.e.
  my Step 1. Every h now acts on **Q_str^{(i)}B₀**, a straight composite of the input, **never on a pure gauge**. The
  hole does not arise, and ‖ev‖ = 1 costs nothing.
- The two expansions describe the **same operator**: they agree iff h∘d = M − ev on 0-forms, which is PROOF.md's
  "*h(A + dλ) = h(A) + Q_0λ − λ(c)*". My gate **D** verifies the ev form entrywise at the first non-trivial composite
  (0 differing of 47 385, four directions), with control **D′** firing.

**So NORMS' polynomial estimate is a valid but loose upper bound on the same quantity, not a competing claim.**
[N1-corr 1]'s **case 1** is the case that holds; its cases 2 and 3 are moot for this route. One wording consequence:
NORMS l.414-415 writes the transport law as "*Q_str d_iμ = d_{i+1}(μ|centres)*", which conflates M with ev —
Q_str∘d = d∘**M** and Q_root∘d = d∘**ev**. Both have ℓ^∞ norm 1, so nothing numerical turns on it, but it is the
textual trace of exactly the confusion that produced the j-dependence.

### D4.4 **A NEW collision, for the SYMBOLS.md catalogue: Q_str is two operators**

`SYMBOLS.md` (T55-C, this session) swept eleven glyph families; **Q and Q_str are not among them**, and §6.7's
"honest zeros" list does not contain either. It should. Verified by file:line **and** by computation:

| | NORMS.md **l.103-104** | LINEAR_PACKAGE.md **l.71** |
|---|---|---|
| definition | "*Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the **L^{d−1} straight paths of L links***" | "*(Q_strA)(X, μ) := **L^{-4}Σ_{y∈B(X)}Σ_{j<L}**A_μ(y + je_μ)*" |
| paths averaged | L^{d−1} (transverse offsets only) | L^d (every block site) |
| row support at L = 3, d = 4 | **81** | **135** (longitudinal profile 1,2,3,2,1) |
| row ℓ¹ | L = 3 | L = 3 |
| satisfies Q_root = Q_str − d∘h | **NO — 108 differing entries** (gate A′) | **YES — 0 differing entries** (gate A) |

Both have norm L, so every *use* NORMS makes of Q_str (‖Q_str‖ = L, ‖Q_str^T‖ = L^{−(d−1)}, Q_str∘d = d∘avg) is
**safe with either**, and (I4) imports the identity from LINEAR_PACKAGE rather than from this definition. **Impact:
benign today.** But NORMS l.403's parenthetical justification of 𝔮₀ = 1 — "*a straight composite contour is L^j fine
links; the **transverse** averaging weights sum to 1*" — is reasoning about the §N1 object, which is **not** the
operator in the slice identity. A future consumer that needs the identity and reads §N1's definition gets a wrong
operator. This is the third distinct meaning in play for "the straight average" and it is the one that is actually
wrong where it matters.

Separately, the **bare glyph Q** means Q_root in PROOF.md, NORMS.md, NLOC.md and TUNIF.md, and **Q_str** in SQ.md
§11.0 (**SQ.md l.655**: "*Q := Q_str (§0.4; …)*"), by SQ's own declared local convention. SQ §0.4's substitution is
correct — I re-derived it: with λ₀ := 0, λ_{i+1} := avg λ_i + h(B_i), B′_i := B_i + dλ_i, the identities
Q_str∘d = d∘avg and Q_root = Q_str − d∘h give Q_strB′_i − B′_{i+1} = Q_rootB_i − B_{i+1}, so residuals and curvatures
are literally equal and B′₀ = B₀ — but it is a **gauge shift**, so it is unavailable to a consumer that bounds a
potential in a stated gauge. Lemma N1-11 is such a consumer. **That is why (N-Q) had to be proved rather than
substituted away**, and it is why 𝔮₀ − 1 is precisely a norm of the accumulated funnel gauge: SQ's recursion
λ_{i+1} = avg λ_i + h(B_i) *is* the M-form of the composite slice functional of §D4.3.

---

## §D5 Does the difference matter (TD5), and what is actually load-bearing (TD6)

**Short answer: no. 11/3 suffices for every named consumer, by margins of between one and thirty decades, and no
consumer needs 1.** The distinction between 1 and 11/3 is academic. What is **not** academic — and what the whole
theorem turns on — is that 𝔮₀ does not depend on j.

### D5.1 Where 𝔮₀ enters, exhaustively

Two places, both **prefactors**, both **linear** in 𝔮₀:

1. **NORMS Lemma N1-11**: 𝔠_P := 2[c_AX R_eff C_f·**𝔮₀** + **𝔮₀**·4κ̂C_R L²/(L²−1)] + 2. With X := c_AX R_eff C_f +
   4κ̂C_R L²/(L²−1) > 0 the ratio 𝔠_P(11/3)/𝔠_P(1) = (𝔮₀X + 1)/(X + 1) is **strictly below 11/3** and tends to it.
2. **TUNIF Corollary TU-5** (this session): 𝔠_L := d·c_{η′}·(**𝔮₀**𝔠₀ + **𝔮₀**·8dκ̂C_RL²/(L²−1) + 1 + c_{η′}).
   Same shape, same factor ≤ 11/3.

𝔠_P enters Theorem N1-15 only through 𝔚 and 𝔖, as 𝔠_P². So **the entire cost of 𝔮₀ = 11/3 rather than 1 is a factor
≤ (11/3)² = 121/9 = 13.444 in 𝔚 and 𝔖, i.e. 1.13 decades**, once, in a prefactor.

### D5.2 Where 𝔮₀ does **not** enter: no exponent, and not A_soft

Theorem N1-15's four exponent counts (NORMS §N6 steps (1)–(4), Remark N6-1's table) are pure powers of L:
(d−2)k, n+(d−1), (d−1)n, −2n, −n. 𝔮₀ sits inside 𝔠_P, which is **j-independent**, so it is absorbed into 𝔖 and the
level ratio is pure L: **A_soft = 1/L = 1/3, free of 𝔮₀**, in every d ≥ 2. Likewise the Wilson exponent
L^{(d−4)k} = 1 at d = 4 is a power count with no constant in it. **Pre-registered failure mode Q-F3 does not occur.**

**Against the brief's steer (D6).** The brief suggested the d = 4 marginality lens — "*a constant that is harmless at
d < 4 can be decisive at d = 4*". **That lens does not bite on 𝔮₀, and I think the framing is the wrong one here.**
The d = 4 marginality is the Wilson vertex's own exponent L^{(d−4)k}, which 𝔮₀ cannot reach; and the thing that
*would* be decisive — a **j-dependent** 𝔮₀ — is decisive in **every** d ≥ 2, not specially at d = 4. I checked the
counterfactual rather than assume it (next subsection), and it breaks at d = 3 as well.

### D5.3 What IS load-bearing (TD6): j-uniformity, and the price of losing it, re-derived

Suppose 𝔮₀ were only the crude compounding bound ‖Q^{m}‖ ≤ (𝔮₀L)^m. Then Lemma N1-11 step (4) gives
|B_j|_∞ ≤ 𝔠·𝔮₀^{\,j}L^{−(k−j)}θ = 𝔠·𝔮₀^{\,k−n}L^{−n}θ with n := k − j. Two potential legs per soft vertex, and the
residual ℓ¹ mass L^{\,n+(d−1)}, give a level-n contribution ≤ 𝔖·𝔮₀^{2(k−n)}L^{(d−1)−n}, so

  Σ_{n≥1} 𝔖·𝔮₀^{2k}·(𝔮₀²L)^{−n}·L^{d−1} ≍ **𝔖·𝔮₀^{2k}** = 𝔖·(121/9)^k = 𝔖·**13.44^k**.

The series in n still converges, but the whole bound grows like **13.44 per level in k** — exactly NORMS
[N1-corr 1]'s case 3 ("*compounding by (p_L/L)² = (11/3)² ≈ 13.4 per level*"), which my own derivation reproduces
independently. **k-uniformity dies, and with it the entire deliverable**; at d = 3 it also dies (13.44/L = 4.48 > 1).
A polynomial 𝔮₀(j) = 1 + cj gives Σ_n(k−n)²L^{(d−1)−n} ≲ k², [N1-corr 1]'s case 2.

**So the property Theorem N1-15 consumes is "𝔮₀ is a constant", not "𝔮₀ is small". Theorem NQ-1 delivers exactly
that property, and its numerical value is free.**

### D5.4 The named consumers below C_♭, checked rather than asserted

NQ_CHECK §Q4(e) says "*no value of ε_1, g_K² or any smallness condition changes*", citing NORMS §N9. That conclusion
is right, but §N9's argument covers only one of the two places C_♭ appears, so I checked both — and the decisive
reason is a third one that neither file gives.

1. **The decisive reason: the C_♭ that Theorem N1-15 bounds is not yet the C_♭ that the thresholds consume.**
   Theorem N1-15 bounds **N3(D³E_k^br(1))** — the third derivative **at the trivial point**. What Lemma BR1 and
   δ_Sch consume is **C_♭ := 4S_♭n_1/r_♭** (PROOF.md **l.5885**), the N₀-**Lipschitz constant of Hess f on the
   small-field class**. These are different statements (NORMS Remark N6-5; TUNIF §U5 item 1), and the bridge between
   them is **(N-bg), which is OPEN**. **So today no factor from Theorem N1-15 — 𝔮₀ included — reaches any smallness
   threshold at all.** That is a stronger and more robust statement than a margin computation, and it does not depend
   on any evaluated constant.
2. **If (N-bg) closed, place one: CURV1's C_θ** (PROOF.md **l.6262**), term 288𝔠_∞³C_♭ ≈ 9.0·10⁹·C_♭ against the
   binding term 288A_in coth⁴(m₁/2)ℓ_θ, which NORMS §N9(2) prices as **≈ 10³² larger** (coth⁴(m₁/2) ≈ 5.9·10²⁰ at the
   session-23 m₁, ≈ 2.9·10⁴² at N5-w0's). A factor 13.44 costs **1.13 decades out of ≈ 32**: it would take a
   31-decade error in §N9 for 𝔮₀ to matter here.
3. **If (N-bg) closed, place two: Lemma BR1's ε_br** (PROOF.md **l.5896**), where C_♭ appears directly as the clause
   **4.19·10⁻⁷/C_♭** in a five-way minimum whose first clause is 1.98·10⁻¹⁸/C_Δ. Since PROOF.md l.5890 fixes
   **C_Δ ≤ C_♭**, the ratio (C_♭-clause)/(C_Δ-clause) = 2.12·10¹¹·(C_Δ/C_♭), so the C_♭ clause is above the C_Δ clause
   by up to **11.3 decades** and a 1.13-decade tightening cannot make it bind — unless C_♭/C_Δ > 2.1·10¹¹, which
   nothing records. **Honest limit on this item: both (C_♭-eval) and the C_Δ evaluation are *named OPEN inputs* at
   PROOF.md l.5898-5899, so this is a margin statement about a ratio, not about two numbers. Item 1 is the reason the
   question does not arise today; item 3 is only a forecast.** NORMS §N9 does not examine ε_br at all; that gap is
   reported, with the conclusion unchanged.

**Verdict on TD5: no named consumer needs 𝔮₀ = 1. The difference between 1 and 11/3 is academic, and saying so
plainly is the honest answer rather than manufacturing a marginality.**

### D5.5 Is 𝔮₀ = 1 reachable at all, if anyone ever wanted it? [SKETCH — NOT CLAIMED]

Recorded because it is the only route and because someone will ask. Q = Q_str **exactly** on the slice
H₀ = {A : h(A) = 0} (PROOF.md L3g(a)-slice). If one could choose the admissible representative with **h_j(B_j) = 0 at
every level simultaneously**, then B_{j} = Q_str^{(j)}B₀ − Σ_i Q_str^{(j−1−i)}r_i exactly and 𝔮₀ = 1. The admissible
freedom (Lemma N1-2) is one fine gauge λ, trivial at the level-k centres, inducing δB_j = d_j(ev^jλ); the conditions
read (M − ev)(ev^jλ) = −h_j(B_j), one equation per level-(j+1) site against L^d values of λ per block, and the
level-(j+1) centres stay free after the level-j equation is solved, so **a solution exists by a nested count**. The
catch is the **size**: λ must be of order ‖h‖·|B₀|, so |B₀ + d₀λ| is of order |B₀| again and Lemma N1-11 step (3)'s
box-axial bound on |B₀| (constant c_AX) is lost and must be re-proved in the new gauge. **So the route moves the
constant from the transport into c_AX; it does not remove it.** This is the same object NORMS [N1-corr 1] already
names as the bypass ("*a **multi-scale axial gauge** … PROOF.md already records that object as needed and OPEN under
(CL-1)*"), in slice form rather than axial form. **Status: SKETCH, not proven, and — given §D5.1-§D5.4 — not worth
doing.** It is recorded so that nobody spends a session on it believing 𝔮₀ = 1 is needed.

---

## §D6 What is now unconditional, and in exactly which regime (TD7)

### D6.1 The claim

With **(N-Q) PROVEN** (§D3) and **(N-loc) discharged** by T55-F's Corollary TU-5 / Theorem TU-6, **Theorem N1-15 has
no remaining named conditional input**:

> **N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + 𝔖·L^{d−1}/(L−1); at d = 4, ≤ 𝔚 + 13.5·𝔖, for every k ≥ 1 and every T ≥ T₀,
> with the soft level-ratio A_soft = 1/L = 1/3 < 1.**

### D6.2 The regime, which is load-bearing and must travel with the claim

Every one of these is a hypothesis, not a decoration:

1. **d = 4** (the general-d form is displayed, but the lane's claim is d = 4, where the Wilson exponent
   L^{(d−4)k} = 1 is **marginal** and the term survives undamped — it is finite only because it is incurred **once**).
2. **Trivial background.** The object bounded is D³E_k^br(**1**) — one Taylor coefficient **at the trivial point**.
3. **Abelian / linearised.** One real colour component around the trivial SU(N) background. Theorem NQ-1's input
   (the slice identity) has **no nonabelian analogue**, by PROOF.md's own [R3-fix].
4. **Setting SC's standing hypotheses**: L ≥ 3 **odd** (used in ‖h‖'s centred-block count), κ_j ∈ [κ_−, κ_+], levels
   0..k, torus side T_j = TL^{k−j}, T ≥ T₀.
5. **Uniformly in k and in T** — that is the content of T55-F, and (N-Q) supplies the j-uniformity it needs.

### D6.3 What it still rests on — "unconditional" means "no named OPEN/ARGUED input", not "assumption-free"

(I-A) LINEAR_PACKAGE v1.1's analyticity and exponential-locality package (the **frozen** package, Lemma 4.4 /
Thm 3.8); (I-B) f₀ = L^{2k}d₀B₀ with C_f; (I-D) NORMS Lemmas N1-2 and N1-6; (I-E) NORMS Lemma N1-7; and inside
NORMS, Lemmas N1-1, N1-3, N1-4, N1-5, N1-11 and TOWER-VAR (d). All are PROVEN or PROVEN-HERE. **And it rests on
`TUNIF.md` itself, which is a session-25 file and is UNREVIEWED** — my scope was (N-Q), and I did not audit §U4's
twisted division theorem. If TU-5 falls, Theorem N1-15 reverts to CONDITIONAL on (N-loc) and the (N-Q) half of this
report is unaffected. **Pre-registered failure mode Q-F6 is addressed, not waved away.**

**Unconditional ≠ explicit.** 𝔠_P still carries **C_f, C_R and R_eff** unevaluated (REVIEW_NQ_S1 F9), and TUNIF's
𝔠_L carries 𝔠₀ and c_{η′} (the T-free price is 2(1+κ)c_{η′} = 7.9·10⁹). 𝔮₀ = 11/3 turns **one** named unknown into a
number. **Against lead decision D3 ("the constants are the enemy"), this is not a constants win: it removes a
depth-dependence, not a factor.**

### D6.4 What does NOT become unconditional — the list, because this is where over-claims live

- **(H-C)'s C_♭ clause as Lemma BR1 and δ_Sch consume it.** They need the **Lipschitz constant of Hess E_k^br on the
  small-field class**; Theorem N1-15 bounds **one Taylor coefficient at the trivial point**. The bridge is **(N-bg),
  which is OPEN**, and Theorem NQ-1 **provably cannot cross it** (input abelian-only). (NORMS Remark N6-5, TUNIF §U5
  item 1.)
- **(N-bg)** itself, and anything at a nontrivial background; anything nonabelian.
- **The other (H-C) clauses**: 𝔠_∞^{(i)}, A_in, A_out, c_K, 1/m₁, the Z-tails.
- **(N-loc-b) as literally stated.** T55-F proves **(N-loc-b′)** = exponential decay **plus** an explicit constant
  mode, because no gauge changes a torus mean; its failure mode U-F7 occurred and is reported there.
- **ε₁, g_K², the HW ceiling.** Unchanged (NORMS §N9; §D5.4 above re-checks the two places C_♭ could have reached).
- **NORMS §N5's per-level no-go** (Theorem N1-13): untouched; Theorem NQ-1 is about the composite transport and says
  nothing about A_per.

### D6.5 Ledger rows that this moves (for the owners; I edit nothing)

| row | was | becomes |
|---|---|---|
| NORMS tally item 15, **(N-Q)** | ARGUED, hole "h applied to a pure gauge" | **PROVEN**, 𝔮₀ = 1 + d(L+1)/(2L) = 11/3, uniformly in j and in the starting level; the hole is an artefact of the M-form expansion |
| NORMS tally item 12, **Lemma N1-11** | CONDITIONAL on (N-Q) | **its last named condition is discharged** (I did not review the rest of its proof — REVIEW_NQ_S1 F4's wording, which I adopt) |
| NORMS tally item 13, **Theorem N1-15** | CONDITIONAL on (N-Q) + (N-loc) | **unconditional at the §D6.2 regime, uniformly in k and T** (via T55-F for the (N-loc) half) |
| NORMS §N8 table, **Prop. NAH-unif / (H-C)** | CONDITIONAL on (N-Q), (N-loc); (N-bg) for the class | **CONDITIONAL on (N-bg) for the class only**; the trivial-background clause is discharged |
| TUNIF **(I-C)** | "*Status as recorded there: PROVEN; the file is session-24*" | re-derived independently here (§D3); the import stands, with the quantifier repaired to "any m consecutive levels" |

---

## §D7 The "could this have failed?" lens, applied to my own work

- **Gate A is nearly self-referential and I say so.** I built Q_root's far funnel by walking the axial path from c_Y
  independently rather than by translating the near one, so gate A does test the Le_μ offset and translation
  covariance of the walker — but both sides are still assembled from the same two primitives by the same code, so A
  could only have failed on a bug in the path walker. **Its real content is control A′**, which decides a live
  question (which Q_str the identity is about) and which fired in all four directions.
- **Gate C cannot fail at j = 1 in one of its clauses.** R₁ ≤ 11/3 is forced a priori by the contour-length bound
  𝔫₁ ≤ p_L = 11, with no computation. I disclose it; the j = 2 clause has real content (a priori bound 121/9 = 13.4).
- **Control E′ was under-powered and I report the directions in which it could not fire** (§D2.3), with the
  structural reason (a quadratic test 0-form cannot distinguish d∘M from d∘ev) and a post-hoc probe that closes it.
- **No gate here compares Q_root against an independent *geometric* construction of the S4′ transporter and its
  linearisation.** Mine is an independent re-implementation of the *linear contour average*, which is what
  LINEAR_PACKAGE l.70 defines; the step from the nonlinear S4′ map to that average is check c8(f)'s content and I did
  not re-run it. REVIEW_NQ_S1 F1 makes the same point about session 24's gate G1 and it applies to me verbatim: **I
  do not claim to have strengthened c8(f).**
- **What would overturn §D3.** Only one of: the forward slice identity failing for some A (it is an identity with a
  three-line proof, and gate A exercises it); root covariance failing (gate E, which fired its control); or ‖h‖
  exceeding d(L²−1)/(4L) (measured as an equality at nine (L,d) pairs). I could not construct a route past any of
  them.
- **What I did not check at all**: (N-loc), (N-bg), any clause of (H-C) other than C_♭'s, TUNIF §U4's twisted
  division theorem, check c8(f), and Lemma N1-11's proof apart from its use of (N-Q).

### Disposition of the pre-registered failure modes

| mode | disposition |
|---|---|
| **Q-F1** Q undefined or multiply defined | **does not occur** — one defining sentence, pointing at three defined objects |
| **Q-F2** (N-Q)'s Q ≠ Setting SC's Q | **does not occur** — and the consumer (Lemma N1-11 step 4) forces the same operator |
| **Q-F3** 𝔮₀ in an exponent or in A_soft | **does not occur** — prefactor only; A_soft = 1/L is 𝔮₀-free (§D5.2) |
| **Q-F4** quantifier gap, level-0-anchored vs arbitrary start | **occurred in the session-24 statement; repaired here** (§D3), as REVIEW_NQ_S1 F3 also asked |
| **Q-F5** my own check unable to fail | **partially occurred**: gate A is near-tautological and control E′ fired in 2 of 8 cases. Both reported (§D2.3, §D7); neither voids a gate, since every gate's control did fire at least once |
| **Q-F6** an unenumerated input of Theorem N1-15 | **does not occur in the named list**, but §D6.3 records that the claim rests on the unreviewed `TUNIF.md` |

---

## §D8 Tally for this file

**PROVEN-HERE (complete proof written out above, from stated hypotheses)**
1. **Theorem NQ-1′** (§D3): ‖Q^{(m)}‖_{∞→∞} ≤ L^m + (d(L²−1)/(2L))(L^m−1)/(L−1) ≤ (1 + d(L+1)/(2L))L^m, for **any
   composite of m consecutive levels**, on Z^d and on every torus, for Setting SC's Q = Q_root, d ≥ 2, L ≥ 3 odd,
   abelian/linearised. At d = 4, L = 3: **𝔮₀ = 11/3**. **This is (N-Q).** Re-derived, not cited.
2. The exact operator identity Π(b,a) = S_{b−1}⋯S_a − D_b Σ_{i=a}^{b−1} (E_{b−1}⋯E_{i+1}) H_i (S_{i−1}⋯S_a), on all
   level-a 1-forms, with no co-closedness restriction.
3. ‖h‖ ≤ d(L²−1)/(4L) (an equality at the nine (L,d) pairs measured); ‖ev^m‖ = 1; ‖Q_str^{(m)}‖ = L^m exactly with
   non-negative entries; ‖D‖_{∞→∞} = 2 exactly on 0-forms, in every d.
4. **𝔮₀ is strictly decreasing in L**, so L = 3 is the worst admissible case at d = 4.

**REFUTED (exactly, with a witness)**
5. **𝔮₀ = 1 is FALSE for Setting SC's Q**: ‖Q‖_{∞→∞} = 205/27 > 3 = L, so any valid 𝔮₀ is ≥ 205/81 = 2.5309. NORMS
   §N4 l.403 / tally item 15 l.809 and TUNIF l.678 state it as a **conditional whose antecedent is false**; the
   conditional itself is true and is a statement about **Q_str**, not about Setting SC's Q.

**COMPUTED (exact, independent implementation)**
6. ‖Q^j‖ = 205/27 and 2021/81 at j = 1, 2 (L = 3, d = 4), supports 459 and 47 385, all four directions; ‖h‖ = 8/3;
   ‖Q_str^LP‖ = 3 with support 135; ‖Q_str^NORMS‖ = 3 with support 81. Check nd1, gates A–E PASS, controls A′–E′ all
   fired. (These reproduce NQ_CHECK §Q2's and REVIEW_NQ_S1 NQ-18's values; I built them from the definitions, not
   from their code.)
7. POST-HOC: ‖hQ_str^{(i)}‖ = 8/3, 56/9 at i = 0, 1; ‖h‖ = d(L²−1)/(4L) and ‖Q_str‖ = L at nine (L,d) pairs with a
   control that fired 3/3.

**SETTLED FROM THE DEFINITION (a reading of the files, not a theorem)**
8. Setting SC's Q is **Q_root**, the S4′ order-averaged root map (PROOF.md l.2225-2226), **not** the straight
   average; the two differ by the nonzero exact form d∘h. The lane's "Q is the straight average" is true of the
   **transpose on co-closed forms** (PROOF.md l.2258, l.2261) — which is where it is used — and false in the forward
   direction on potentials, which is what (N-Q) asks about.

**NEW DEFECT FOUND (systemic defect 1)**
9. **Q_str denotes two different operators** in the lane: NORMS.md l.103-104 (L^{d−1} transverse paths, support 81)
   and LINEAR_PACKAGE.md l.71 (L^d block legs, support 135). The slice identity holds for the latter and **fails for
   the former by 108 entries** (gate A′). Benign for every current use (both have norm L), but NORMS l.403's
   justification of 𝔮₀ = 1 is written against the wrong object. Neither Q nor Q_str is in SYMBOLS.md's families or
   in its "honest zeros" list.

**ARGUED / SKETCH, not claimed**
10. A multi-level slice gauge (h_j(B_j) = 0 at every level) would give 𝔮₀ = 1 but moves the constant into c_AX; it is
    the slice form of NORMS [N1-corr 1]'s multi-scale-axial bypass, recorded OPEN under (CL-1). **Not worth doing**
    (§D5.5).

**NOT ESTABLISHED, said plainly**
11. (N-loc) — not touched here; discharged by T55-F, whose file is unreviewed. (N-bg) — untouched, and Theorem NQ-1
    provably does not transfer. Every other clause of (H-C). Check c8(f). Lemma N1-11's proof apart from its use of
    (N-Q). TUNIF §U4.

**Counted here: nothing.** This file is not a ledger; no item above is to be added to PROOF.md's tally by me.

---

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file.

**1. NORMS.md owner — three text repairs; the status moves are as in §D6.5.**
(a) **l.403** and **tally item 15, l.809-810**: the conditional "*immediate with 𝔮_0 = 1 if Setting SC's Q is the
straight average*" has a **false antecedent** (PROOF.md l.2225-2226), and the conclusion is false for Setting SC's Q
(‖Q‖ = 205/27 > L). Replace with the proven statement. (b) **l.103-104** misdefines **Q_str** (L^{d−1} transverse
paths; the operator in the slice identity averages the L^d block legs — supports 81 vs 135, verified in check nd1).
Every current NORMS use is safe with either, but l.403's parenthetical reasoning is about the wrong object. (c)
**l.414-415** writes "*Q_str d_iμ = d_{i+1}(μ|centres)*", conflating the block mean M with the root restriction ev:
Q_str∘d = d∘**M**, Q_root∘d = d∘**ev**. That conflation is the textual trace of the j-dependence [N1-corr 1] prices.
(Items (b) and (c) were also raised as F5 by REVIEW_NQ_S1 and are repeated here because I verified them myself.)

**2. TUNIF.md owner (T55-F) — one internal inconsistency, created this session.** Your **l.120** imports (I-C) with
𝔮₀ = 1 + d(L+1)/(2L), which is correct. Your **l.678** then says "*if Setting SC's Q is the straight average,
𝔮_0 = 1 and Theorem N1-15 is unconditional*". The antecedent is false; the two lines invite the reading that 𝔮₀ is
an open number. Suggested repair at l.678: "*(N-Q) is Theorem NQ-1, re-derived in NQ_DEF.md §D3: Setting SC's Q is
Q_root, not the straight average, and 𝔮₀ = 11/3 — which is all Theorem N1-15 consumes, since 𝔮₀ enters only 𝔠_P and
𝔠_L as a prefactor and A_soft = 1/L is 𝔮₀-free.*" Second, smaller: §U5 item 2 can be closed, and Corollary TU-5's
use of ‖Q^j‖ is now covered for composites starting at any level, not only at level 0.

**3. NQ_CHECK.md owner (session 24) — your Theorem NQ-1 stands, re-derived independently.** I rebuilt Steps 1–3 and
the four norm inputs without using your file or REVIEW_NQ_S1, and reproduced 205/27 and 2021/81 from the definitions.
Two of REVIEW_NQ_S1's binding fixes are confirmed by my own work and should be applied: **F1** (gate G1 does not
strengthen c8(f) — my gate A has the same limitation and I say so) and **F3** (state the theorem for any m
consecutive levels; §D3 does). One addition to your FOR-OTHER-FILES item 1: NORMS l.403's *justification* of
𝔮₀ = 1 is written against NORMS §N1's Q_str, which is not the operator in the slice identity (§D4.4).

**4. SYMBOLS.md owner (T55-C) — two glyphs for the catalogue, with the evidence already gathered.**
**Q_str**: a FAMILY of **two** objects (NORMS l.103-104 vs LINEAR_PACKAGE l.71), distinguishable by support (81 vs
135) and by whether the slice identity holds (it fails by 108 entries for the first). **Q** (bare): Q_root in
PROOF.md / NORMS.md / NLOC.md / TUNIF.md, Q_str in SQ.md §11.0 by SQ's declared local convention (SQ.md l.655).
Neither is in §6.7's "honest zeros". Classification: **one live text defect (NORMS l.403's justification), no live
numerical defect** — every current use of Q_str goes through ‖Q_str‖ = L, ‖Q_str^T‖ = L^{1−d} or Q_str∘d = d∘avg,
all of which hold for both objects.

**5. SQ.md owner — one clause, as REVIEW_NQ_S1 and NQ_CHECK both asked, and I confirm the reason.** §0.4's
substitution is correct (I re-derived it, §D4.4) but is a **gauge shift**, so it is unavailable to any consumer that
bounds a **potential** in a stated gauge. Its accumulated λ_{i+1} = avg λ_i + h(B_i) **is** the M-form of the
composite slice functional, i.e. exactly the object whose norm 𝔮₀ − 1 measures. Suggested sentence in §0.4:
"*curvatures and residuals only; the potentials move by the accumulated funnel gauge*".

**6. PROOF.md / lead — the ledger row, and one warning.** Theorem N1-15's row can read **"unconditional at d = 4,
trivial background, abelian/linearised, L ≥ 3 odd, uniformly in k and T"**, provided TUNIF's Corollary TU-5 is
accepted (it is unreviewed). **Do not let this be read as (H-C)'s C_♭ clause**: N1-15 bounds D³E_k^br(**1**), (H-C)
names the Lipschitz constant on the class, and **(N-bg) is the bridge and is OPEN**. Also: PROOF.md moved by **+25
lines** in the Setting SC region during this session (21:51 UTC), so every line number above carries a 22:05 UTC
timestamp and a quoted string.
