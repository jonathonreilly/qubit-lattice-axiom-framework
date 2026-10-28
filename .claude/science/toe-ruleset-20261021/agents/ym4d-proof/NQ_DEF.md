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
