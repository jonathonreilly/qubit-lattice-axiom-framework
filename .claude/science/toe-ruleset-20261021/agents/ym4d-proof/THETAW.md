# THETAW.md — the exponents of 𝔐 and BFT, decoupled (target T55-J)

*Owner: the T55-J worker, session 25. Writes only this file and `checks/tw1_*`. Every change this file
wants in another lane file is in `## FOR OTHER FILES (not edited)` at the end, for the lead to land.*

---

## §T0 PRE-STATED (first edit of this file, 2026-10-28T21:39:13Z; STATEMENTS ONLY)

**This is the first edit of THETAW.md.** It contains statements only: no derivation, no grep, no
classification, no arithmetic and no check of mine precedes it. It cites nothing produced in session 25.

### §T0.1 The object

`REVIEW_S22.md` l.389-432 states the background-field theorem (BFT), clauses 0-5, with the norm 𝔐
defined at l.392-397. The norm's scale weights, and BFT-1's decay rate, are written with the single
letter **θ_w**, quantified once at l.399 as *"there exist … θ_w ∈ (0, 2]"*. `NORMS.md` §N7 (session 24)
records that the composite contraction needs **three** exponents — θ_w^c (curvature), θ_w^r (residual),
θ_A (potential) — with θ_A = min(1, θ_w^c − 1) and A = L^{d − θ_w^r − 2θ_A}; and `PROOF.md` l.30-34
([S24-fix 3]) records that a single common θ_w has no solution in (0, 2]. Separately,
`RTARGET.md` §33 l.587-588, `SF.md` l.680 and `BFT_A.md` l.36 all use the letter **θ** for the *source*
weight ω_l = L^{θ(k−l)}, with their own stated windows.

### §T0.2 Pre-registered targets

- **TW-1 (inventory).** Enumerate every distinct job an exponent does in 𝔐 and in BFT-0…BFT-5, one
  symbol per job, preferring symbols already in use in the lane. State for each clause which jobs it
  inherits.
- **TW-2 (consumed windows).** For each job, derive the window its consumer's **proof** requires, not
  the window its **statement** announces, and record for each whether consumed ⊊ stated, consumed ⊋
  stated, or equal. A window read off a statement is to be recorded as unverified.
- **TW-3 (satisfiability).** Decide whether the decoupled system is satisfiable. If yes, exhibit the
  feasible region explicitly. If no, prove it empty and identify the minimal set of clauses whose
  windows must move, and by how much.
- **TW-4 (restatement).** Write append-ready replacement text for REVIEW_S22 l.389-432's clause
  statement with every exponent decoupled and quantified over its own window, saying what BFT-1's
  existential must become.
- **TW-5 (d = 4).** Determine whether the feasible region is empty only at d = 4 or at every d, and
  say which of the two it is.

### §T0.3 Named failure modes (pre-stated, so a failure is recorded as a failure)

- **TW-F1** The decoupling is vacuous — i.e. the four windows were always windows on the same job, so
  separating the letters changes nothing and the system stays empty. Then TW-3's answer is EMPTY and
  the repair is an estimate, not a restatement.
- **TW-F2** The decoupling *is* real but introduces a coupling I did not find, so a region I report as
  feasible is not. Guard: for every pair of jobs I must state explicitly which lemma couples them, or
  state that I searched and found none.
- **TW-F3** I report a window from a clause's **statement** rather than from its proof, and so inherit
  the very defect the target has. Guard: every window row carries the file:line of the step that
  consumes it.
- **TW-F4** A job exists that I do not enumerate (in particular: a clause of 𝔐 or of BFT-0/2/3/4 that
  carries a scale exponent I have not named), so a "feasible" verdict is feasibility of a sub-system.
  Guard: enumerate from the text of l.392-423 line by line, and from the consumers listed at l.425-431.
- **TW-F5** The symbol θ, or θ_w, means something different in one of the files I combine, and I combine
  two different objects. Guard: quote file:line at every comparison (session-25 brief, defect 1).

### §T0.4 What would count as a FAIL of my own gate

Any numeric gate I run is exact rational arithmetic over the exponent inequalities. It must come with a
designed-FAIL control — an input for which the gate must return INFEASIBLE — and I must report that the
control fired. A gate that returns FEASIBLE for every input it is given is not evidence. Two controls
are pre-registered here, before any script: **(i)** the single-common-θ_w system of PROOF l.30-34 must
come back EMPTY (if it does not, my encoding of NORMS §N7 is wrong and nothing else in this file counts);
**(ii)** the decoupled system must come back EMPTY in some dimension d, since if it is feasible in every
d the exponent count has lost the dimensional content it is supposed to carry.

### §T0.5 Scope limits stated in advance

- I decide **windows and satisfiability**, not the open estimates themselves. Nothing here proves
  (G♯_0-field), (GAP-Z), (CO-fun), (G♯-rough) or (SPD).
- A feasible region is a statement about *parameters*, not about *status*: a clause can have an
  admissible exponent and still be OPEN. I will not let a feasibility verdict read as progress on a
  proof.
- I do not edit `SYMBOLS.md`; where a rename is implied I list it for that file's owner.

---

## §T1 TW-1 — the job inventory. Status: PROVEN as a statement about the text of REVIEW_S22 l.389-432

Read line by line from `REVIEW_S22.md` l.392-423, plus the consumer list at l.425-431. **Six** distinct
jobs carry an exponent. The target writes three of them with **one** letter, writes two of them with
their own letters already, and does not write the sixth at all.

| # | job | symbol (existing lane name) | where the job is done | written in the target? |
|---|---|---|---|---|
| J1 | 𝔐's **curvature displacement** weight, = BFT-1's curvature decay rate | **θ_w^c** (`NORMS.md` l.644; `BFT_B.md` l.4364) | REVIEW_S22 l.393 (weight), l.410 (bound) | as θ_w |
| J2 | 𝔐's **soft-fluctuation (residual)** displacement weight, = BFT-1's residual decay rate | **θ_w^r** (`NORMS.md` l.644) | REVIEW_S22 l.393 (weight), l.410 (bound) | as θ_w |
| J3 | the **source** weight ω_l = L^{θ(k−l)} of the Y leg | **θ** (`RTARGET.md` l.587; `SF.md` l.680; `BFT_A.md` l.36) | REVIEW_S22 l.394 | as θ_w |
| J4 | the **Hölder/Campanato** exponent of the X_c-type curvature leg and of Y's Hölder leg | **α** (`RTARGET.md` l.591; `BFT_A.md` l.36) | REVIEW_S22 l.394 | yes, as α (implicitly, via "Hölder") |
| J5 | the **exponential-weight rate** e^{±m d} | **m** / **m_0** (`RTARGET.md` l.585; REVIEW_S22 l.396) | REVIEW_S22 l.396, l.412, l.415 | yes, as m_0 — but **quantified once for three jobs** |
| J6 | the **potential (gauge-representative) decay** | **θ_A** (`NORMS.md` l.645; Lemma N1-11, `NORMS.md` l.382) | consumed by the composite contraction (`NORMS.md` l.650-651); carried silently by 𝔐^∇'s units (`BFT_A.md` l.378) | **NO — missing clause** |

**J1 and J2 are the same letter twice over.** REVIEW_S22 l.393 puts "level-j curvature **and**
soft-fluctuation components" under one weight L^{θ_w(k−j)}, and l.410 states the BFT-1 bound for the
plaquette logs **and** ρ(U_j, U_{j+1}) with one rate. `NORMS.md` §N7 l.644-646 is the record that these
are two exponents with different required values.

**J6 is a missing clause, not merely an unnamed one.** BFT-1 (l.409-410) states a curvature bound and a
soft-fluctuation bound and no potential bound. The composite contraction consumes a potential bound:
Theorem N1-15's steps (1)-(4) use |ζ^c_jY|_∞ ≤ 𝔠_PL^{−(k−j)} twice in every cubic vertex
(`NORMS.md` l.530, l.536, l.544-545, l.550), supplied by Lemma N1-11 (`NORMS.md` l.382-399), which is
**CONDITIONAL on (N-Q)** (`NORMS.md` l.401-420) and uses **(N-loc)** (l.422-432). 𝔐^∇ does carry it —
`BFT_A.md` l.378 records "|x̄| ≤ L^{−(k−l)}‖·‖_𝔐 (own units)" — but by its coarse-unit convention, with
no symbol and no clause. A consumer reading BFT-1 and nothing else does not get θ_A.

### §T1.1 Which clause inherits which job

| clause | jobs inherited | by what route |
|---|---|---|
| BFT-0 | J1, J2, J4, J5, J6 | the uniqueness ball ‖X‖_𝔐 ≤ C_0ε (l.405) is a ball in 𝔐 |
| BFT-1 | J1, J2, **J6 (should)** | it *is* the displacement-weight statement, read as a bound |
| BFT-2 | J1, J2, J6 | "BFT-1 holds there" (l.411); r_ℂ is a radius, not an exponent |
| BFT-3 | J5 | the tree rate m_0 (l.412) |
| BFT-4 | J5, **J1** | e^{m_0\|X\|} (l.415); and the polydisc is "the BFT-2 one in curvature-adapted coordinates" (l.416), so its level-j radius must contain BFT-1's ball, i.e. must be ≥ C_0L^{−θ_w^c(k−j)}ε. A consumption site of J1 the target does not name |
| BFT-5 | J1, J2, J3, J4, J5 | stated "in the 𝔐-pair" (l.419); the pair is (𝔐, Y), so it takes the source weight too |

### §T1.2 Are α and θ themselves doing double duty? Yes — θ three times, α twice

**θ is three objects in this lane**, and two of them meet inside the BFT clause-set:
1. the **source-weight exponent** — `RTARGET.md` l.587, `SF.md` l.680, `BFT_A.md` l.36 and l.880
   ("α := ¼, θ := ½"). This is J3.
2. a **field size** θ := sup|d_kB_k| — `NORMS.md` l.269 (Lemma N1-4) and l.384 (Lemma N1-11), and
   `NLOC.md` l.311. It is a *number of order ε*, inside the very file that supplies θ_w^c and θ_w^r.
3. a **Hessian-deviation threshold** θ := (1 − K̄)/2 — `PROOF.md` l.6326 — with the derived family
   C_θ, C_θ^ρ, ε_θ at `PROOF.md` l.6237-6239.

**REVIEW_S22 contains objects (1) and (3) in one clause-set**: l.394's ω_l exponent is object (1), and
BFT-4's "the C_θ, C_θ^ρ, ε_θ constants are level-uniform" (l.417) is indexed by object (3). Nothing is
mis-derived here that I found, but the two are three lines apart.

**α is two objects**: the Campanato exponent (`RTARGET.md` l.591) — this is J4, and the F3 slot weight
L^{(2+α)(k−l)} (`BFT_A.md` l.399-400) is the *same* α, derived, not a second object — and a **field
size** α := 3ℓ_θε_V at `PROOF.md` l.6236, with α′ at `PROOF.md`'s NAH1 (b) being "the AX-gauge field
size" (`NORMS.md` l.690). So bare α is an exponent in the §33 pair and a size in PROOF's NAH chain.

*Defect-1 note, for `SYMBOLS.md`'s owner, not for me to land:* `SYMBOLS.md` §6.3 records θ_w as "one
glyph that must become two". It is **three**: θ_w^c, θ_w^r and the source weight, which the lane
already calls θ elsewhere but which REVIEW_S22 l.394 writes as θ_w. And θ itself is a three-object
family that §6.3 does not cover.

---

## §T2 TW-2 — the consumed window of each job, derived from the consumer's proof

Every row names the file:line of the **step that consumes** the constraint, not of a statement that
announces it (failure mode TW-F3).

### J1 — θ_w^c (curvature)

| | window | from | status |
|---|---|---|---|
| **stated** | θ_w ∈ (0, 2] | REVIEW_S22 l.399 | — |
| **consumed, floor** | θ_w^c ≥ d − 2 = **2** | `NORMS.md` l.650 with l.656-657. Both branches force it: for θ_w^c ≥ 2, θ_A = 1 and the clause reads θ_w^c ≥ 2; for θ_w^c < 2, θ_A = θ_w^c − 1 and it reads 3θ_w^c − 2 ≥ 4, i.e. θ_w^c ≥ 2, a contradiction. Re-derived exactly in **tw1-F** | PROVEN, given the θ_A cap |
| **consumed, ceiling** | θ_w^c ≤ **2** | `NORMS.md` l.660, from K_p^♯ ≥ 1/L² (REVIEW_S21 P, recorded at `NORMS.md` l.139, l.478) | **ARGUED** — `NORMS.md` l.479 labels it so itself: "K_p^♯ on Z⁴ is not certified" |
| **delivered** | exactly **2** | Lemma N1-4, `NORMS.md` l.267-287, PROVEN-HERE (linear chain, trivial background, torus) | PROVEN-HERE |
| other consumers | RLARGE one-step C_IL^{−2} ⟹ 2 (REVIEW_S22 l.382); SQ (REG-min) decay L^{−2(k−i)} ⟹ 2 (REVIEW_S22 l.385, `NORMS.md` l.700); PROOF/N5 "θ_w = 0 suffices" ⟹ floor 0 (REVIEW_S22 l.426) | | |

**Consumed window = the single point {2}, against a stated interval (0, 2].** Strictly narrower, and
narrower in the strongest possible way: it is not an interval. *This is the finding that decides the
logical form of the restatement* — an existential "∃θ_w ∈ (0,2]" cannot be matched to a consumer that
needs θ_w^c = 2 without a separate argument that the witness equals 2, and no such argument exists in
the target.

### J2 — θ_w^r (residual)

| | window | from | status |
|---|---|---|---|
| **stated** | θ_w ∈ (0, 2] | REVIEW_S22 l.399 | — |
| **consumed, floor** | θ_w^r > d − 2θ_A = **2**, strictly | `NORMS.md` l.651, l.654 | PROVEN as a condition |
| **delivered, level-k data only** | **3** = d − 1 | Lemma N1-4's proof, `NORMS.md` l.278-279 (sup\|r_i\| ≤ κ̂C_RL^{−(d−1)(k−1−i)}θ, J-str (c)); independently `BFT_A.md` l.1549, "Data: L^{k−1−i}‖r^c_i‖ ≤ κ̂L^{−(k−1−i)}R̄" — **one spare power over 𝔐^∇'s leg** | PROVEN |
| **delivered, residual-type nonlinear sources** | **2 + θ** | `BFT_A.md` l.1551: Σ_iL^{k−1−i}‖σ^c_i‖ ≤ Σ_iL^{−θ(k−i)}‖s‖_R/κ_-, i.e. one extra L^{−θ(k−i)} over the exponent-2 leg | PROVEN on the linear side (Corollary HX, m = 0) |
| **what 𝔐 as built records** | **2** | 𝔐^∇'s residual leg is L^{k−1−j}‖r^c_j‖ (`BFT_A.md` l.38) with r^c := L^{k−1−i}r (`RTARGET.md` l.581, confirmed in use at `BFT_A.md` l.159: "ω_lL^{k−1−l}\|s^c_l\| = ω_lL^{2(k−1−l)}\|s_l\|"), i.e. L^{2(k−1−j)}\|r_j\|_own. §33's X_s (`RTARGET.md` l.596) is the same object | — |

**Two separate defects, pointing opposite ways.** (i) The stated interval (0, 2] **excludes** every
admissible value, since the floor is strict at 2. (ii) The norm **as instantiated** records exactly 2 —
precisely the boundary at which A = L^{4−2−2} = L^0 = 1 and the contraction is lost (check **tw1-G**,
row "boundary tr = 2: A = 3^0 = 1, NOT a contraction"). So the repair is not a wider existential: it is
to put the delivered exponent **into the norm**, which currently throws away the one power that the
whole composite route runs on.

### J3 — θ (the source weight). **This is the row on which the "no admissible exponent" verdict rested**

| | window | from | status |
|---|---|---|---|
| **stated** | θ ∈ (0, 1] | `SF.md` l.680; `RTARGET.md` l.588 | — |
| **stated** | θ ∈ [0, 1) | `BFT_A.md` l.36 | — |
| **stated** | α ≤ θ ≤ 1 − α ≤ ¾ | `BFT_A.md` l.396-397 ([RBA1-fix]) | — |
| **consumed, floor** | θ > 0, strictly; cost 1/(L^θ − 1) | `RTARGET.md` l.588 (Ω ≤ 1 + 1/(L^θ − 1)); `BFT_A.md` l.534 (level-0 current ≤ ‖j^c_0‖ + ‖j‖_{Pc}/(L^θ − 1)); `BFT_A.md` l.1551 (≤ ‖s‖_R/(κ_-(L^θ − 1))) | PROVEN (`BFT_A.md` l.834, Theorem 6.8) |
| **consumed, ceiling** | θ < 1, strictly; cost 1/(1 − θ) | `BFT_A.md` l.534 (C_P := L/(e(1 − θ)ln L)); `BFT_A.md` l.159 (BA-6's L^{−(1−θ)(k−l)}, summable in l only for θ < 1) | PROVEN (`BFT_A.md` l.834, BL-6 (a), BA-6) |
| **consumed, coupling** | α ≤ θ, and α < θ strictly | `BFT_A.md` l.524-528 (BL-5 (c)): a **counterexample family** — for α > θ, sup_{‖s‖_R≤1}‖x(s)‖_inv → ∞. Sufficiency at α ≤ θ: BL-5 (a), l.518, "**no upper restriction on θ**". Strictness: Corollary G♯R is PROVEN at 0 < α < θ, with α = θ "OPEN and possibly false" (`BFT_A.md` l.2359, l.2878, via `NBG_B.md` §9.2 S4) | PROVEN |
| **θ ≤ 1 − α** | **NOT a proven constraint** | `BFT_A.md` l.560-561 (BL-7 (f)): *"θ ≤ 1 − α enters **only** through the repaired plain slot (BL-6 (c)), ARGUED"*. l.834's list of constraints actually proven is **θ > 0, θ < 1, α ≤ θ** — 1 − α is **not on it**. l.833: *"the F3 slot as a slot for all currents is dead for every (α, θ); **the window is not**"* | the ceiling is conditional on an abandoned slot |

**Consumed window = (0, 1) with α < θ.** Against the three stated versions:

- **narrower than `SF.md` l.680's (0, 1] at the top endpoint**, and that endpoint is not cosmetic:
  C_P = L/(e(1 − θ)ln L) **diverges at θ = 1**. SF states a window containing a value its own pair's
  constant cannot be evaluated at. Over-statement, endpoint-only, real.
- **narrower than `RTARGET.md` l.588's (0, 1] at the same endpoint**, for the same reason.
- **WIDER than `BFT_A.md` l.396-397's α ≤ θ ≤ 1 − α.** The ¾ ceiling is lane A's own earlier text,
  superseded by its own [RBA2-fix] B4 at l.826-834.

**Consequence, and it is the pivot of this file.** The "four incompatible windows" that leave the target
with no admissible exponent are three windows on **J3** (lane A's, SF's, RTARGET's) and one requirement
on **J2** (θ_w^r = 3). Once the letters are separated they are **constraints on different variables and
cannot clash**. The clash was produced by the single-symbol defect it was diagnosing — failure mode
TW-F1 **does not occur**, and the quoted ceiling that made the system look empty is in addition not a
proven constraint. See §T4 for what is genuinely empty.

### J4 — α (Hölder)

| | window | from | status |
|---|---|---|---|
| **stated** | 0 < α < 1 | `RTARGET.md` l.591; `BFT_A.md` l.36 | — |
| **stated** | α ≤ ½ | `BFT_A.md` l.396 | a *consequence* of α ≤ θ ≤ 1 − α; it falls with that ceiling |
| **consumed, floor** | α > 0, strictly, no positive floor | the Campanato step exists because of failure mode G0-F2, `RTARGET.md` l.611: *"no bound in sup norm alone for f_0"*. Any α > 0 serves | PROVEN as a requirement |
| **consumed, ceiling** | α < θ | as J3's coupling row | PROVEN |

**Consumed window = (0, θ).** Equal to stated except for the coupling. **Nothing consumes a positive
floor on α** — and that is what makes the repair in §T4.3 cheap, because the system's whole margin can
be pushed into θ and α taken as small as we like.

### J5 — m (the exponential rate). Reported, not resolved: the same defect, a different letter

The target quantifies **m_0 > 0 once** (l.399) and uses it for three jobs: 𝔐's weights (l.396),
BFT-3's tree rate (l.412), BFT-4's polymer weight e^{m_0|X|} (l.415).

- **consumed by BFT-3, BFT-4:** m_0 > 0 strictly.
- **where the pair's proofs actually live:** **m = 0**. BL-5 (a) is "PROVEN-HERE, 0 < α ≤ θ, **m = 0**"
  (`BFT_A.md` l.767); Corollary HX is "(H-lin^∇) for the X_s outputs, **m = 0**" (l.1548); Corollary
  G♯R is PROVEN at **m = 0** (`NBG_B.md` §9.2 S4). m > 0 for the data part is **ARGUED**
  (`BFT_A.md` l.789).
- **ceiling:** m < m_*′ (`RTARGET.md` l.601); Theorem RH_m is PROVEN for 0 ≤ m < m′ < m_*′
  (`BFT_B.md` l.2816-2819, via `NBG_B.md` §9.2 S5).

So m_0 is **a second instance of the target's defect**: one letter, three jobs, one quantifier, and the
consumed windows differ as *statuses* — {0} is where the pair is proven, (0, m_*′) is what BFT-3/4 need.
This is outside T55-J's named scope and I do not resolve it. It is listed in §T8 as a second
decoupling the lead should make in the same edit, because the restatement touches the same lines.

### J6 — θ_A (potential)

| | window | from | status |
|---|---|---|---|
| **stated** | — (no clause) | | |
| **consumed** | θ_A = **1** | `NORMS.md` l.651, l.662 (the soft condition at θ_A = 1); used twice per cubic vertex at `NORMS.md` l.530, l.536, l.544-545, l.550 | required |
| **ceiling** | θ_A ≤ **1**, PROVEN | Lemma N1-6, `NORMS.md` l.301-312: the level-j difference of the nested interpolant is the level-k difference divided by L^{k−j}. No interpolant agreeing with λ at level-k sites does better: a path of L^{k−j} level-j steps joins two level-k sites across which λ changes by d_kλ, so the mean level-j difference is ≥ L^{−(k−j)}\|d_kλ\|. **This is a hard cap, not a measured one** | PROVEN |
| **floor** | θ_A ≥ θ_w^c − 1 | Lemma N1-5 (axial), `NORMS.md` l.289-299, applied at Lemma N1-11 step (3), l.392-394 | PROVEN (abelian/linearised; imported nonabelian) |
| **delivered** | 1, **CONDITIONAL on (N-Q)**, using **(N-loc)** | Lemma N1-11, `NORMS.md` l.382-399; (N-Q) at l.401-420 is ARGUED and *"a question about a DEFINITION"*; (N-loc) at l.422-432 is ARGUED | CONDITIONAL |

**Consumed window = {1}**, and it is simultaneously the proven ceiling. A second pinned exponent.

---

## §T3 The couplings, named one by one (guard against failure mode TW-F2)

Decoupling the letters is only legitimate if every genuine coupling is carried over as an explicit
inequality. Here is every one I found, with the lemma that imposes it; and, at the end, the pairs I
searched and found uncoupled.

- **(C1) θ_A = min(1, θ_w^c − 1).** `NORMS.md` l.656-657; Lemma N1-5 supplies the floor θ_w^c − 1
  (axial integration over a box of side L^{k−j} converts curvature decay θ_w^c into potential decay
  θ_w^c − 1), Lemma N1-6 the cap 1 (the pure-gauge part cannot be spread below L^{−(k−j)}).
  **The potential exponent is not free and never was.**
- **(C2) θ_w^r ≤ 2 + θ, when the source class contains the residual-type nonlinear rows.**
  `BFT_A.md` l.1551. The residual response to a residual-type source of ‖·‖_R-size 1 is
  L^{−θ(k−i)} in 𝔐's exponent-2 leg; the leg may therefore be strengthened by θ and no further.
  **This is the one coupling between the source weight and a displacement weight, and it is the reason
  the system is interesting rather than trivially feasible.**
  For **level-k data alone** the response carries a full spare power (`BFT_A.md` l.1549), giving
  θ_w^r = 3 with no reference to θ — which is why Theorem N1-15, a data-only statement, quotes
  A_soft = 1/L.
- **(C3) α < θ.** `BFT_A.md` l.524-528 (necessity, by counterexample), l.518 (sufficiency),
  Corollary G♯R for strictness.
- **(C4) the F3 plain-current rows: linear side needs θ > 1 − α, remainder side needs θ ≤ 1 − α.**
  `BFT_A.md` l.538-543 (BL-6 (b)), restated at l.815-816 ([RBA2-fix] B1) as *"PROVEN: the F3 slot gives
  no k-uniform linear bound for θ ≤ 1 − α. ARGUED (power count only): for θ > 1 − α the remainder rows
  are not bounded in it."* **Empty for every (α, θ)** — l.542-543 says exactly that: *"no θ makes the
  F3 slot serve both the linear and the remainder side."*
- **(C5) BFT-4's polydisc radius ≥ C_0L^{−θ_w^c(k−j)}ε at level j.** REVIEW_S22 l.416 with l.405:
  the polydisc is "the BFT-2 one in curvature-adapted coordinates", and the Cauchy estimates of l.417
  are taken on it, so it must contain BFT-1's ball. No new exponent; a consumption site of J1.

**Pairs searched, no coupling found:** (θ_A, θ) — θ_A is fixed by (C1) from θ_w^c and never reads the
source weight; (α, θ_w^c) — the Campanato leg of 𝔐 is a seminorm at fixed level with the coarse-unit
convention already applied, so α does not enter the level weight; (m, the scale exponents) beyond the
e^{O(m)} change of weight recorded at `BFT_A.md` l.789. I state this rather than leaving it implied,
because a coupling I missed is exactly how a FEASIBLE verdict here would be wrong.

---

## §T4 TW-3 — is the decoupled system satisfiable? **YES, with one slot empty.** Status: see per-row labels

### §T4.1 The verdict in one line

**The decoupled system is SATISFIABLE.** The emptiness recorded against the target is the emptiness of
**one slot** — the F3 plain-current slot, (C4) — and not of the system; and the "four incompatible
windows" that produced it are three windows on J3 and one requirement on J2, which after decoupling
constrain different variables and cannot clash (§T2, J3's consequence paragraph).

### §T4.2 The feasible region, explicitly

Two nested regions, because the source class matters.

**R_lin — level-k data, divergence-form sources, residual-type sources.** (What lane A proves, and
what Theorem N1-15 consumes.)

> θ_w^c = 2, θ_A = 1, θ_w^r = 3, 0 < α < θ < 1, m = 0.
> **A = L^{d − θ_w^r − 2θ_A} = L^{4−3−2} = L^{−1} = 1/3 = A_soft.**

| defining relation | status | where |
|---|---|---|
| θ_w^c ≥ 2 | PROVEN, given θ_A ≤ 1 | `NORMS.md` l.650 + l.657; tw1-F |
| θ_w^c ≤ 2 | **ARGUED** | `NORMS.md` l.660, l.478-479 |
| θ_A ≤ 1 | **PROVEN** | Lemma N1-6, `NORMS.md` l.301-312 |
| θ_A = 1 delivered | **CONDITIONAL on (N-Q), (N-loc)** | Lemma N1-11, `NORMS.md` l.382-432 |
| θ_w^r = 3 delivered | PROVEN at the trivial background | `NORMS.md` l.278-279 (J-str (c)); `BFT_A.md` l.1549 |
| 0 < θ < 1 | PROVEN | `BFT_A.md` l.834 |
| α < θ | PROVEN | `BFT_A.md` l.524-528 + Cor. G♯R |
| m = 0 | this is where the proofs are; m > 0 ARGUED | `BFT_A.md` l.767, l.1548, l.789 |

**R_full — R_lin plus the nonlinear remainder rows that are residual-type or divergence-form.**
By (C2) the residual leg is capped at 2 + θ:

> θ_w^c = 2, θ_A = 1, **θ_w^r = 2 + θ**, 0 < α < θ < 1, m = 0.
> **A = L^{4 − (2+θ) − 2} = L^{−θ}.**

Non-empty for every θ ∈ (0, 1), hence a contraction for every admissible θ; check **tw1-B** returns 440
exact grid points with θ_w^c and θ_A pinned at 2 and 1 and the contraction exponent ranging over
[−11/12, −1/12] on a 1/12 grid, the extreme attained at θ = 11/12 — i.e. the exponent **is** −θ.

**A result worth separating out (ARGUED, mine, from (C2)).** The lane quotes **A_soft = 1/3** as the
composite contraction rate (`NORMS.md` l.517, l.581; `PROOF.md` l.30-34). That is the **data-only**
rate. With the nonlinear residual-type sources in the same norm, (C2) caps the residual leg at 2 + θ
and the rate becomes **A = L^{−θ} with θ < 1 strictly**, so **1/3 is an infimum that is not attained**,
approached only as θ → 1 where the constant C_P = L/(e(1 − θ)ln L) diverges. The honest statement of
the composite contraction is therefore *"A = L^{−θ} for any θ ∈ (0,1), with constants degrading like
1/(1 − θ) and 1/(L^θ − 1)"*, not *"A = 1/3"*. I label this **ARGUED**: it composes `BFT_A.md` l.1549
and l.1551 with `NORMS.md` l.651, and I have not rebuilt lane A's Corollary HX to check that the
strengthened leg survives every row of it.

### §T4.3 What is genuinely empty, and the minimal set of clauses that must move

**The empty slot.** The two rows named in GAP 1 (F3) — the soft (∂ρ^{(2)})^Tr_l row (`BFT_A.md` l.229)
and the (COMM) [A^T, χ]A row (l.244) — are **plain level-l currents**, "neither divergence form nor
residual type" (l.387-388), and carry **no level decay** (l.388-389; l.819-820). For them (C4) applies
and the slot is empty for every (α, θ). This is the only genuine emptiness in the system, and it is
also where the lane's level-count factor lives: with an unweighted plain-current family the level-0
images sum to (k − 1)η² and *"the entire level-count loss sits in the level-0 image"*
(`BFT_A.md` l.822-824) — the same ≈ 25(k − 1) that `HANDOFF.md` critical-path item 5 puts first.
**The θ question and the k-factor question are one question:** a positive source weight is exactly what
turns the (k − 1) sum into a geometric one, and the plain rows have no decay to pay for the weight.

**The minimal set of clauses whose windows must move: ONE, plus a named partner.**

**(W2) (SPD), `BFT_A.md` l.830-831.** As stated: *"the Ran Q^T component of a remainder row at level l,
carried up to level m, has plain coarse size ≲ L^{−(m−l)}η²"* — i.e. per-level decay exponent **σ = 1**.

> **How much it must move: σ > 0 suffices. Any positive power.**
>
> *Derivation.* Let (SPD) supply decay σ relative to the top, so a row born at level l has plain
> coarse size ≲ L^{−σ(k−l)}η². Its Y-weight is ω_l = L^{θ(k−l)} (`RTARGET.md` l.587), so its
> contribution to ‖·‖_Y is ≲ L^{(θ−σ)(k−l)}η², bounded uniformly in k **iff θ ≤ σ**. Combine with the
> proven floor α < θ (C3) and with §T2's finding that **α has no positive floor**: for any σ > 0 take
> α := σ/2 and θ := σ (admissible, since σ ≤ 2/3 gives θ ≤ 1 − α automatically and σ > 2/3 only
> widens the room, with θ < 1 the binding ceiling). The region is non-empty and the contraction rate
> is A = L^{−min(σ, θ)} = L^{−θ}. ∎

That is the highest-value number in this file: **the open estimate the lane must go and prove is not
"decay L^{−(m−l)}"; it is "decay L^{−σ(m−l)} for some σ > 0"**, which is a strictly and substantially
weaker target than the one currently written, and it buys the whole region. The price of a small σ is
paid in constants only: 1/(L^θ − 1) from Ω (`RTARGET.md` l.588) and 1/(1 − θ) from C_P
(`BFT_A.md` l.534), both finite for every σ > 0.

**The named partner: (W1) (G♯-rough), `BFT_A.md` l.828-829** — needed for the complementary rough part
of BL-6 (c)'s split. **This one does NOT soften to "any positive power", and I record the reason.**
`BFT_A.md` l.996-999 reduces (G♯-rough) to ‖x(J)‖_inv ≤ CL^{−α(k−l)}N for the level-0 images of rough
currents, *"a special case of the OPEN (G♯_0-lev0) whose sup size is too large by L^{(k−l)/4}"*
(BR-2 (iii)). The deficit is therefore **(¼ + α) powers per level**, and lowering α buys back only the
α of it: **an irreducible ¼-per-level deficit remains at α = 0⁺.** Route (A) (RP) removes the loss for
the **X_s** half with no L^{(k−l)/4} penalty (l.1000-1002); the **curvature** half still needs (G♯-up),
OPEN. So the honest split is: *(W1)'s X_s half is reducible given (RP); its curvature half carries a
fixed ¼-per-level deficit that no choice of exponent removes.*

### §T4.4 Does feasibility mean progress? No, and I say so explicitly

Every statement in §T4.2 is about **parameters**. (G♯_0-field), (GAP-Z), (CO-fun), (G♯-rough) and
(SPD) are exactly as open as they were. What changes is that a clause with no admissible parameter
cannot be proven *or refuted*, whereas these can: the defect §T4 removes is an obstruction to **working
on** BFT-1 and BFT-5, not to BFT-1 and BFT-5 being true.

---

## §T5 TW-5 — the d = 4 question. **Not a bookkeeping failure: it is the marginality, again**

Evaluate the two conditions of `NORMS.md` l.650-651 at the maximal supplies θ_w^c = 2 (ARGUED ceiling)
and θ_A = 1 (PROVEN ceiling):

| condition | general d | reading |
|---|---|---|
| Wilson (level 0, incurred once), θ_w^c + 2θ_A ≥ d | 2 + 2 ≥ d ⟺ **d ≤ 4** | slack exactly **4 − d** |
| soft (level j), θ_w^r + 2θ_A > d, with θ_w^r ≤ 2 + θ | (2 + θ) + 2 > d ⟺ **θ > d − 4** | at d = 4 this is **θ > 0**, which is *the same inequality the linear estimate already imposes* (`RTARGET.md` l.588) |

Check **tw1-E** (exact): feasible at d = 2, 3, 4; **EMPTY at d = 5 and d = 6**, in both the
nonlinear-source and the data-only readings. Wilson slack at (θ_w^c, θ_A) = (2, 1): +2, +1, **0**, −1, −2.

**So the region is non-empty at d = 4 and empty at every d ≥ 5 — the opposite of "empty only at d = 4".**
But at d = 4, and only at d = 4:

1. **the Wilson clause holds with exactly zero slack**, so θ_w^c is pinned at the single point 2 by a
   floor and a ceiling that meet (tw1-F);
2. **the soft clause's entire margin collapses onto one free parameter, θ**, whose two endpoints are
   both excluded by proven consumers (θ > 0 by Ω and C_P; θ < 1 by C_P and BA-6) — an open interval
   with no interior slack in any other coordinate;
3. **the two conditions coincide**: both read "d ≤ 4".

This is not an accounting artefact. `NORMS.md` l.571-575 states the same fact from the other side —
*"d − 2 − 1 − 1 = d − 4 = 0 for the Wilson vertex (**marginal**) … The result is true for every d ≥ 2
and has no margin to spare in the exponent"* — and `NORMS.md` l.86 names *"the d = 4 cubic vertex is
marginal"* as the reason A ≥ 1 in the per-level route. **The exponent system of 𝔐 is the marginality
of the four-dimensional cubic vertex, written in weights.** The condition θ_w^c + 2θ_A ≥ d, with the
maximal proven supplies, *is* the power counting that makes Yang-Mills renormalisable at d ≤ 4: one
differentiated leg of dimension 2, two potential legs of dimension 1 each, against the volume d.

**Name it as such, and do not "repair" it.** A restatement that gave the Wilson clause slack at d = 4
would be giving the cubic vertex a dimension it does not have, and would be feasible at d = 5 as well
— which is why tw1-D is a designed-FAIL control and not a bonus check. The three lanes that reported a
d = 4 marginality independently are reporting one phenomenon, and the lane already has the right words
for it.

**One honesty note that limits this.** The zero-slack claim rests on the **ARGUED** ceiling
θ_w^c ≤ 2 (`NORMS.md` l.660, l.478-479, from the uncertified K_p^♯ ≥ 1/L²). If θ_w^c could exceed 2 —
i.e. if the chain minimiser smoothed the curvature strictly faster than the classical scaling — the
Wilson clause would have slack and d = 4 would not be saturated. **Proving that ceiling would turn
"marginal" into "provably marginal", and it is the cheapest named upgrade to the statement of §T5**:
one lower bound on the one-level curvature response on ℤ⁴, against a quantity the lane has already
measured twice (`NORMS.md` l.138-139, REVIEW_S21 P/T).

---

## §T6 Checks record — `checks/tw1_*`. One ABORT, reported; both designed-FAIL controls FIRED

Criteria pre-registered in `checks/tw1_criteria.md` **before** `checks/tw1_feas.py` existed, containing
no constant derived in session 25. Exact `fractions.Fraction` arithmetic, no floating point, no BLAS,
no numerics lock (session-25 brief rule 6). Scripts and outputs kept unaltered.

| id | pre-registered verdict | result | status |
|---|---|---|---|
| **tw1-A** | PASS iff the single-common-θ_w system is EMPTY | **EMPTY** | **PASS** — reproduces `PROOF.md` l.30-34 [S24-fix 3] independently of it |
| **tw1-B** | report either way | **FEASIBLE**, 440 exact points; θ_w^c ≡ 2, θ_A ≡ 1, contraction exponent = −θ | reported |
| **tw1-B′** | report either way | **FEASIBLE**, 660 points, best exponent −1 (A = 1/3) at the data-only cap | reported |
| **tw1-C** | control FIRES iff EMPTY at θ = 0 | **EMPTY** | **CONTROL FIRED** — the θ > 0 floor is live, the gate is not blind to it |
| **tw1-D** | control FIRES iff EMPTY at d = 5 | **EMPTY** | **CONTROL FIRED** — the count carries the dimension |
| **tw1-D′** | — | EMPTY at d = 5 with the data-only cap too | reported |
| **tw1-E** | reporting only | feasible d = 2, 3, 4; empty d = 5, 6; Wilson slack 2, 1, **0**, −1, −2 | reported |
| **tw1-F** | reporting only | θ_w^c ≥ 2 forced in both branches of the θ_A cap | reported |
| **tw1-G** | reporting only | **ABORTED** — see below | **FAIL (abort), reported** |

**The abort, reported as a fail.** `tw1_feas.py` raised `TypeError` at line 202 building
`Fraction(1, 3**(-e))` for a non-integer exponent e, and exited 1. Gates tw1-A, B, B′, C, D, D′, E and
F had all completed and printed before it (`checks/tw1_out.txt`, kept unaltered;
`checks/tw1_err.txt` holds the traceback). The defect is in a **display line of the last block only**
and touches no verdict. Re-run under a new id with the criteria untouched:
`checks/tw1b_display.py` → `checks/tw1b_out.txt`, exit 0.

**A second, cosmetic defect, disclosed.** `tw1b_display.py`'s bracketing line prints
"3^-1 > A > 3^-3/2" for the exponent −1/2, which is false as an inequality (3^{−1/2} > 3^{−1}). It is a
print-formatting error in a line that carries no verdict; **the exponent column is the result**, and
the exponents are exact. I am not re-running a third time for a cosmetic line; I am recording it so
that nobody quotes that bracket.

**Were these gates able to fail?** tw1-A could have: had my encoding of `NORMS.md` §N7 been wrong it
would have returned FEASIBLE and voided the file. tw1-C and tw1-D did fail, by construction, on inputs
chosen before the run — a source weight of 0 and a fifth dimension — and both returned EMPTY as
required. The one gate that cannot fail is tw1-E, which is why it is labelled reporting-only.

---

## §T7 Honest statuses

**PROVEN here** (as statements about the text and about the exponent arithmetic, which is all they
claim to be):
- §T1, §T1.1, §T1.2 — the job inventory, the inheritance map, and the θ/α multiplicities, each by
  file:line.
- §T2 — every "consumed" row whose status column says PROVEN, in particular: θ_w^c's floor of 2;
  θ_A ≤ 1 (Lemma N1-6 plus the pigeonhole step I supply at §T2 J6); θ ∈ (0,1) strictly, with the
  divergences that make both endpoints inadmissible named; α < θ.
- §T2 J3's finding that **θ ≤ 1 − α is not a proven constraint** (`BFT_A.md` l.560-561, l.833-834).
- §T4.1/§T4.2 — the decoupled system is satisfiable, with R_lin and R_full as given.
- §T4.3's derivation that **σ > 0 suffices** for (SPD).
- §T5 — the d-dependence, and that the region is empty at d ≥ 5 and non-empty with zero Wilson slack
  at d = 4, *given* the ARGUED ceiling θ_w^c ≤ 2.

**ARGUED** (convincing, with the hole named):
- **A = L^{−θ}, not 1/3, once the nonlinear residual-type rows are in the norm** (§T4.2). The hole: it
  composes `BFT_A.md` l.1549 + l.1551 with `NORMS.md` l.651 and does not rebuild Corollary HX row by
  row against the strengthened residual leg.
- The ceiling θ_w^c ≤ 2 itself is ARGUED upstream (`NORMS.md` l.479), so every "pinned" and
  "zero slack" statement is ARGUED to that extent and is labelled so where it occurs.

**CONDITIONAL:**
- θ_A = 1 is delivered **CONDITIONAL on (N-Q)** and uses **(N-loc)** (`NORMS.md` l.401-432). Since θ_A
  is pinned and appears doubled in both contraction conditions, **(N-Q) is load-bearing for the whole
  feasible region**, not for a convenience. If θ_A < 1 the Wilson clause fails at d = 4 outright.

**OPEN, untouched, and not advanced by anything here:** (G♯_0-field), (GAP-Z), (CO-fun), (G♯-rough)
= (W1), (SPD) = (W2), (N-bg), and every status in BFT-0…BFT-5.

**What I did NOT do.** I did not re-derive lane A's Theorem 6.8, BL-1, BL-5 or Corollary HX from their
own primitives; I read their statements and the lines that consume the exponents, which is what TW-2
asks for but is weaker than rebuilding them. The session-25 brief's fourth point applies to me: the
rows above marked PROVEN rest on lane A's and NORMS's proofs being what they say, and §T4.2's
contraction rate is the place where that reliance is load-bearing.

### §T7.1 Where I departed from the framing I was given (D6)

Two places, both reported loudly as the brief requires.

1. **The scope prompt (and the finding it relays) says the four windows are incompatible and the
   system has no admissible exponent. After decoupling, they are not incompatible.** Three of the four
   are windows on the **source weight** J3 and one is a requirement on the **residual decay** J2;
   separated, they constrain different variables. The clash was an artefact of the single-symbol
   defect being diagnosed — which is exactly the trap the brief's defect 1 warns about, operating one
   level up. **Failure mode TW-F1 does not occur.** The honest verdict is SATISFIABLE with one empty
   slot, not EMPTY.
2. **The ceiling "α ≤ θ ≤ 1 − α ≤ ¾", on which the emptiness turned, is not a proven constraint.**
   Lane A's own [RBA2-fix] B4 supersedes [RBA1-fix]: `BFT_A.md` l.834 lists the proven constraints as
   θ > 0, θ < 1, α ≤ θ, and l.833 says the F3 slot that carries the 1 − α ceiling *"is dead for every
   (α, θ); the window is not"*. The quoted ¾ is `BFT_A.md` l.396-397, the **superseded** text. This is
   the brief's defect 2 in its purest form: a ceiling fixed once, superseded in the same file 430
   lines later, and still being quoted.

Neither departure makes the lane's position better. It relocates the obstruction from "the target has
no admissible parameter" (a statement defect, cheap) to "one source slot is provably empty and one
open estimate, (SPD), must deliver some positive power" (a mathematics defect, and the same one that
`HANDOFF.md` already puts first as the level-count factor k).

---

## FOR OTHER FILES (not edited)

### F1. `REVIEW_S22.md` l.389-432 — append-ready replacement for the BFT statement

*Replace l.389-423 (Data, the norm 𝔐, Claim, BFT-0…BFT-5, Anti-circularity) with the text between the
rules below. l.425-431 ("Who needs which part") needs the three amendments in **F2**. The table at
l.376-385 and the "Smallest measurable piece" at l.433-435 are untouched.*

---

**Statement (BFT).**

*Data:* N ≥ 2; L ≥ 3 odd; soft couplings κ_j ∈ [κ_-, κ_+]; F_j = E_j^br + κ_jΣ_cφ̂_c and 𝔉_k as in
PROOF [S20]-[S22] (TOWER-VAR); S_k a composite slice at the composite lift Z^lift(V_k).

*Exponents — fixed, not existentially quantified.* The weights of 𝔐 and the decay rates of BFT-1 are
**four** distinct exponents, not one. Three are **pinned numerals**; one is a free parameter of the
theorem, quantified universally with the constants allowed to depend on it.

- **θ_w^c := 2** — the curvature weight / curvature decay rate. Required to be ≥ d − 2 = 2 by the
  composite contraction (NORMS §N7 l.650 with l.656-657) and available only up to 2
  (NORMS l.660, ARGUED). **A single point: there is no interval here.**
- **θ_A := 1** — the potential (gauge-representative) decay rate. Capped at 1 by Lemma N1-6
  (NORMS l.301-312, PROVEN) and required to be 1 by the same contraction. **Delivered CONDITIONAL on
  (N-Q), using (N-loc)** (NORMS l.401-432).
- **θ_w^r** — the soft-fluctuation (residual) weight / decay rate. Required **> d − 2θ_A = 2,
  strictly** (NORMS l.651). Supplied at **θ_w^r = d − 1 = 3** for the response to level-k data alone
  (J-str (c); NORMS l.278-279; BFT_A l.1549), and at **θ_w^r = 2 + θ** once the nonlinear
  residual-type sources are in the norm (BFT_A l.1551).
- **θ ∈ (0, 1), α ∈ (0, θ)** — the source weight ω_l = L^{θ(k−l)} (l ≥ 1; ω_0 = 1) and the
  Campanato/Hölder exponent. **Both endpoints of θ are excluded and neither exclusion is cosmetic:**
  Ω ≤ 1 + 1/(L^θ − 1) diverges as θ ↓ 0 (RTARGET §33 l.588) and C_P = L/(e(1 − θ)ln L) diverges as
  θ ↑ 1 (BFT_A l.534). α < θ is necessary (BFT_A l.524-528, by counterexample) and α = θ is OPEN and
  possibly false (BFT_A l.2359). *There is no ceiling θ ≤ 1 − α: that constraint belongs to the F3
  plain-current slot, which is dead (BFT_A l.833-834).*

*The norm 𝔐 = 𝔐(α, θ) (on composite displacements X, Z = e^XZ^lift):*
- level-j **curvature** components are weighted by L^{θ_w^c(k−j)} = L^{2(k−j)}, in a Hölder (X_c-type)
  norm with exponent α;
- level-j **soft-fluctuation (residual)** components are weighted by L^{θ_w^r(k−j)} — **a different
  exponent, and strictly larger than 2.** *(Note: 𝔐^∇ as instantiated at BFT_A l.38 and §33's X_s at
  RTARGET l.596 weight the residual by L^{2(k−1−j)}, i.e. θ_w^r = 2 exactly, at which A = L^0 = 1 and
  the contraction is lost. The leg must be strengthened to the delivered exponent; BFT_A l.1549
  provides the spare power for the data part and l.1551 the amount 2 + θ for residual-type sources.)*
- level-j **potential** components are weighted by L^{θ_A(k−j)} = L^{(k−j)}. *(Carried implicitly today
  by 𝔐^∇'s coarse-unit convention, BFT_A l.378; it must be named, because the contraction consumes it
  twice per cubic vertex.)*
- nonlinear sources are in a divergence-form norm Y (SF / RTARGET §33's pair) with **ω_l = L^{θ(k−l)}**
  — **the source weight, which is not any of the three above**;
- exponential weights e^{±m d} are in level-k ancestor distance. *(See F3: m likewise does three jobs
  and should be decoupled in the same edit.)*
- The plain sup-curvature norm is excluded (COMP-F1; SF S4-1).

*Claim:* **for every α, θ with 0 < α < θ < 1**, there exist ε_0 > 0, r_ℂ ∈ (0, 1], m_0 > 0, C_0 < ∞ and
T_0, **depending only on (N, L, κ_±, α, θ)**, such that for **every** k ≥ 1, **every** torus whose
level-k side is ≥ T_0 (and every non-wrapping box with the boundary convention of N5-sf0), and
**every** level-k field V_k = e^zV_k^r with V_k^r real, max_P|log V^r_{k,P}| ≤ ε ≤ ε_0 and
|z|_∞ ≤ r_ℂε:

- **BFT-0 (existence, uniqueness, identification).** As before, with the ball
  {e^XZ^lift : X ∈ S_k, ||X||_{𝔐(α,θ)} ≤ C_0ε}.
- **BFT-1 (scale-weighted regularity).** For every j < k, in Hölder form within each level-k block:
  - **(1a) curvature.** The own-units plaquette logs of U_j are ≤ C_0L^{−2(k−j)}ε. *(θ_w^c = 2, the
    maximum available; a weaker clause is not a safer one.)*
  - **(1b) soft fluctuations.** ρ(U_j, U_{j+1}) ≤ C_0L^{−θ_w^r(k−j)}ε with **θ_w^r > 2 strictly**;
    θ_w^r = 3 for the response to level-k data, θ_w^r = 2 + θ in the presence of residual-type
    nonlinear sources.
  - **(1c) potential (NEW CLAUSE; CONDITIONAL on (N-Q), (N-loc)).** There is an admissible gauge
    representative with own-units potentials ≤ C_0L^{−(k−j)}ε, i.e. θ_A = 1. *Without (1c) the
    composite contraction has no input for two of the three legs of every cubic vertex
    (NORMS l.530, l.536, l.544-545, l.550), and BFT-1 as previously written did not state it.*
- **BFT-2 (analyticity).** As before; "BFT-1 holds there" means (1a), (1b) and (1c).
- **BFT-3 (locality).** As before.
- **BFT-4 (branch-action class).** As before, with the polydisc required to contain BFT-1's ball, i.e.
  of level-j curvature radius ≥ C_0L^{−2(k−j)}ε.
- **BFT-5 (linear stability at the background).** The composite slice Hessian at Z(V_k) satisfies (G♯)
  **in the (𝔐(α, θ), Y_{α,θ})-pair** with constants ≤ C_0, for the same (α, θ). As before, this
  follows from BFT-1/2 plus (G♯_0-field) + (R♯_ω) by SF's Lemma G-pert on X_c-small patches, and
  (G♯-patch) globally.
- **BFT-6 (BB-mix).** [Promoted per HANDOFF; not restated here.]
- **Anti-circularity:** unchanged.

**Why the old existential cannot stand, and what replaces it.** The previous text read *"there exist
… θ_w ∈ (0, 2]"*, with one letter serving 𝔐's curvature weight, 𝔐's residual weight, 𝔐's source
weight ω_l and BFT-1's decay rate. **An existential over an interval is the wrong logical form here,
for two independent reasons, and widening the interval repairs neither.**
1. **Every consumer needs a specific value, and the suppliers deliver specific values.** RLARGE's
   one-step C_IL^{−2} (REVIEW_S22 l.382) and SQ's (REG-min) decay L^{−2(k−i)} (l.385) both need
   exactly 2; the composite contraction needs exactly θ_A = 1 and θ_w^r > 2; Lemma N1-4 delivers
   exactly 2 and J-str (c) exactly d − 1. A clause of the form "∃θ_w ∈ (0,2]" cannot be handed to a
   consumer that needs θ_w = 2 without a separate argument that the witness is 2 — and no such
   argument exists in the statement or in its consumers.
2. **The required values are not a sub-interval of (0, 2]**: θ_w^r must exceed 2 strictly, and the
   contraction's own canonical triple is (θ_w^c, θ_w^r, θ_A) = (2, 3, 1), verified as
   A = L^{4−3−2} = L^{−1}.
So: **the exponents move out of the existential and into the data of the theorem**, as the pinned
numerals θ_w^c = 2 and θ_A = 1 plus the parameter θ_w^r with its stated floor; **only the constants
stay existential**; and **(α, θ) are universally quantified over 0 < α < θ < 1 with the constants
depending on them**. That is the smallest change that makes BFT-1 matchable to its consumers.

---

### F2. `REVIEW_S22.md` l.425-431 — three amendments to "Who needs which part"

- l.426, **PROOF/N5: "BFT-1 (θ_w = 0 suffices)"** — correct, and should read "(θ_w^c = θ_w^r = 0
  suffices; no (1c) needed)", so that it is visibly a *floor* and not a different value of the same
  parameter.
- l.427, **SF: "BFT-1 (θ_w > 0)"** — should read "BFT-1 (1a)/(1b) with θ_w^c = 2, θ_w^r > 2, and the
  source weight θ ∈ (0,1); SF's own (a5-G♯) at SF.md l.680 states θ ∈ (0, **1**], and the endpoint
  θ = 1 is inadmissible because C_P = L/(e(1 − θ)ln L) diverges there (BFT_A l.534). SF.md l.680 and
  RTARGET §33 l.588 should both read **(0, 1)**."
- l.429, **RLARGE: "BFT-1 one-step (C_I; not load-bearing)"** — this is a consumer of θ_w^c = **2**
  specifically (REVIEW_S22 l.382's C_IL^{−2}); worth saying, since it is one of the three independent
  witnesses that the curvature exponent is a point and not an interval.

### F3. `REVIEW_S22.md` l.396, l.399, l.412, l.415 — m_0 does three jobs too

Same defect, different letter, and the same edit touches the same lines. m_0 is quantified once at
l.399 and used for 𝔐's weights (l.396), BFT-3's tree rate (l.412) and BFT-4's polymer weight (l.415).
The consumed windows differ **as statuses**: the pair's estimates are PROVEN at **m = 0**
(BFT_A l.767 BL-5 (a); l.1548 Corollary HX; Corollary G♯R per NBG_B §9.2 S4), m > 0 for the data part
is ARGUED (BFT_A l.789), the ceiling is m < m_*′ (RTARGET l.601), and BFT-3/BFT-4 need m_0 > 0
strictly. Recommend three symbols — m_𝔐, m_tree, m_𝒜 — with m_𝔐 = 0 admitted, since that is where the
lane's proofs are. **I have not analysed this family's feasibility; it is flagged, not decided.**

### F4. `SYMBOLS.md` — three additions for that file's owner (I did not edit it)

1. **§6.3 says θ_w is "one glyph that must become two". It is three.** The third is the **source
   weight**, which REVIEW_S22 l.394 writes as θ_w and which RTARGET §33 l.587, SF l.680 and BFT_A l.36
   all write as plain **θ**. Recommended canonical names: θ_w^c, θ_w^r (already in use) for the
   displacement weights, and **θ** (already in use in three files) for the source weight — no new
   glyph needed.
2. **θ is itself a three-object family** not listed in §6.3: the source-weight exponent
   (RTARGET l.587, SF l.680, BFT_A l.36, l.880); a **field size** θ := sup|d_kB_k| (NORMS l.269,
   l.384; NLOC l.311), inside the very file that supplies θ_w^c and θ_w^r; and a **Hessian-deviation
   threshold** θ := (1 − K̄)/2 (PROOF l.6326) with its derived C_θ, C_θ^ρ, ε_θ (PROOF l.6237-6239).
   **Objects 1 and 3 appear three lines apart inside REVIEW_S22's BFT clause-set** (l.394 and l.417).
3. **α is a two-object family**: the Campanato exponent (RTARGET l.591, BFT_A l.36 — the F3 slot's
   L^{(2+α)(k−l)} at BFT_A l.399 is the *same* α, derived) and a **field size** α := 3ℓ_θε_V
   (PROOF l.6236), with α′ "the AX-gauge field size" (NORMS l.690).

### F5. `BFT_A.md` — one superseded line still being quoted elsewhere

l.396-397 ([RBA1-fix]) states the window as **α ≤ θ ≤ 1 − α**, and is superseded 430 lines later by
l.826-834 ([RBA2-fix] B4), whose list of constraints **actually proven** is θ > 0, θ < 1, α ≤ θ, with
l.833 recording that the slot carrying the 1 − α ceiling *"is dead for every (α, θ); the window is
not"*. l.396-397 is still being quoted as lane A's proven window in downstream files. Recommend a
one-line pointer at l.396 to l.826-834. *(Lane A's file; I am not editing it.)*

### F6. `NORMS.md` §N7 and `PROOF.md` l.30-34 — two additions, both to statements the lane already owns

1. **(N-Q) is load-bearing for the feasible region, not for a convenience.** θ_A appears **doubled**
   in both contraction conditions (NORMS l.650-651) and is pinned at its proven ceiling 1, so if (N-Q)
   fails and θ_A < 1 the Wilson clause fails at d = 4 outright. NORMS l.418-419 calls (N-Q) *"a
   question about a DEFINITION, not a theorem"* and the first item of its own FOR OTHER FILES list;
   that item is the gate on the whole exponent system, and is worth saying where θ_A is introduced.
2. **The composite contraction rate, with nonlinear sources, is A = L^{−θ} and not 1/3.** NORMS l.517
   and l.581 quote A_soft = 1/L = 1/3; that is the **data-only** rate (NORMS l.278-279, BFT_A l.1549).
   With residual-type nonlinear sources BFT_A l.1551 caps the residual leg at 2 + θ, giving
   **A = L^{4−(2+θ)−2} = L^{−θ}** with θ < 1 strictly, so **1/3 is an unattained infimum**. Status of
   this item: **ARGUED** (mine, THETAW §T4.2); it composes two of lane A's lines with NORMS's
   condition and does not rebuild Corollary HX against the strengthened leg. **It does not change any
   verdict** — A < 1 either way — but it changes the margin from "one power of L" to "θ powers of L",
   and the margin is what the constants are spent against.

### F7. `BFT_A.md` (W2)/(SPD), l.830-831 — the open estimate can be weakened substantially

(SPD) is stated with per-level decay exponent **1**. The decoupled system needs only **σ > 0**: a row
born at level l with plain coarse size ≲ L^{−σ(k−l)}η² is absorbed by the weight ω_l = L^{θ(k−l)} iff
θ ≤ σ, and θ may be taken as small as desired above α, which has no positive floor (THETAW §T2 J4,
§T4.3). The price of a small σ is 1/(L^θ − 1) in Ω and 1/(1 − θ) in C_P, both finite. **Recommend
restating (W2) with a free exponent σ > 0 rather than the exponent 1**, since the weaker statement
buys the entire feasible region and is a materially easier target.
*Its partner (W1)/(G♯-rough) does **not** soften the same way:* BFT_A l.996-999 reduces it to a bound
the available (G♯_0-lev0) overshoots by L^{(k−l)/4}, so the deficit is (¼ + α) powers per level and
lowering α buys back only α — **an irreducible ¼-per-level deficit remains at α = 0⁺**. Route (A) (RP)
removes the loss for the X_s half (l.1000-1002); the curvature half still needs (G♯-up), OPEN.
