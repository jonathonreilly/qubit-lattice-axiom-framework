# Referee: library/layer-thm-part.md (LAYER-THM conditional part)

File: `library/layer-thm-part.md`, 1608 lines (Codex distil of layer-pkg,
walks-gw, layer-r3, adm-pl). Date: 2026-11-07. FINISH row 452.
Account: Sussman–Alpöge at 31a47c543775; SHA-256 of part I checked
(`4cb5cb5e0af8…`, matches the part's table).

One referee pass. Imports PI, GW (repaired walks-gw.md), B98-P5 port and
the b98p5-r3 gate are used as given.

(Sections below are saved one at a time.)

## Verdict table

| Section | Verdict | One line |
|---|---|---|
| §1.1 norms, equation, tags | REVISE | Say which identity factors carry tags (R1). Tie the weight rate to GW's final rate (R2). |
| §1.2 imports and premises | ADVANCE | Every name used later is listed; each has an Outstanding paragraph. |
| §2 statement | ADVANCE | The clauses follow from the premises listed; (e) is honestly parametric. |
| §3.1 admission, order, non-circularity | REVISE | (22)–(30) check. (26) must use GW's radii (R3). (31) lacks GW's tower floor (R4). (32) lacks c_ι (R5). |
| §3.2 walks to primitive estimates | REVISE | Matches repaired walks-gw except the insertion-carrier tree and its floor (R5, R6). |
| §3.3 contractions | ADVANCE | All numerical steps recomputed. |
| §3.4 four entries, linearization | ADVANCE | K_A, K_X, K_Δ, B_H and (45) recomputed. |
| §3.5 structure | ADVANCE | Covariance by uniqueness; (f) proviso correct. |
| §3.6 rider, cutoff, (M1)–(M3) | REVISE (wording) | (20), (46), (48), (21) recomputed. (M3) holds; state m_H = m_c (R7). |
| §3.7 field data | ADVANCE | (49)–(51) recomputed. |
| §3.8 RC bridge | ADVANCE | (54), (56), (57) recomputed; citations spot-checked. |
| §4 Outstanding paragraphs | REVISE | GW, R, S and M paragraphs need the additions R8–R11. |
| §5 and U01–U34 table | ADVANCE | Each row follows from the theorem and the premises it names. |

## Detailed checks

### §1.1

- (1)–(4), (S5): (4) is the seven-term formula at I 14177–14182, term by
  term. ADVANCE.
- Lines 105–109, tags. The text says "Identity pieces are expanded as
  I = Σ_τ h_τ² I" with tags. The same part treats the identity in
  T_σ = I + Γ as untagged (§3.5: off the retained region the equation "can
  still read −j"), and the zero-switch test in §4 M needs P_0 = I − … and
  k = (q_J − a)ℓ^{-1} with untagged I and a. The account's K10 convention
  (I 15306–15316) tags only the listed primitives. **R1 (REVISE).** Replace
  "Identity pieces are expanded as I=Σ_τh_τ²I, with the PI cutoffs and full
  footprints." by: "Inside the walk expansions of R and of the PI parametrix,
  the identity is expanded as I=Σ_τh_τ²I with the PI cutoffs and full
  footprints, and each such piece is a walk term with its tag. All other
  factors that are not listed primitives (Q, Q', a, ℓ, the identity in
  T_σ=I+Γ, in P_0=I−G_0Q^Tq_0Q and in (I−·)^{-1} expansions) carry no tag,
  as in I 15306–15316."
- Line 84, weights. 𝔐_δ is not tied to the rate at which GW's weighted
  majorants are finite. (40) needs Σ_z k e^{δd^∧} ≤ K. **R2 (REVISE).**
  After "p(z)≤e^{δd^∧(y,z)}p(y)." insert: "Here δ≤δ_*, where δ_*≤μ is
  GW's common final rate (walks-gw constant step 11), below every composite
  rate used."

### §1.2

All later inputs appear: PI, GW, AV, UA (R, A0, L0, S, T, P2), ID (EQ, LC,
PH), M with RJ, FM/FD, E(e), RC. The scope sentences match the sources I
read (I 72392–72399; II 55882ff, 58620ff; I 15669–15701 for K6). (12) is
correctly called an added clause. ADVANCE.

### §2

Each clause is proved in §3 from the listed premises: (a) §3.3, (b) §3.4,
(c)/(d)/(f) §3.5, rider §3.6, corollary §3.5, U33 bridge §3.8. (e) is
retained only through E(e); the "specialization property" is proved and not
substituted. No hidden premise found apart from the rate in R2. ADVANCE.

### §3.1

Recomputed:
- (22): replacing the shifted potentials costs η·η r/ℓ² each in operator
  norm (Duhamel, unitary outer factors), so 2√N rη²/ℓ² in Frobenius; the
  commutator costs at most 2η²|a|‖b‖_F ≤ 2√N r²η²/ℓ², below the stated
  2N r². With √N r ≤ 1 the sum is ≤ 4√N r(η/ℓ)². Correct.
- Level conversion L^{2(q−m)_+}: correct.
- Post-step crossing (23)–(24): the cube of side s_n through the four
  corners has every site at sup-distance < s_n from each corner; the two gaps
  put it in Ω_n and outside Ω_{n+2}. Coefficient 4BCMα_{0,n}; (24) gives
  ≤ a and √N r ≤ 1. Correct as an implication.
- Thick cover: an aligned start at the grid point below e_0 gives a
  12g_q interval that contains any run of length ≤ 11g_q. PL needs r ≤ 2a,
  S1′ needs 4r ≤ a; the stated r ≤ a and r ≤ a/4 are sufficient. Correct.
- (25): PL at grade j−1 gives 8√N a L²(η/ℓ_j)². Slides: 2(d−1)ℓ_j/η
  slides times (25) give 16(d−1)√N L² aη/ℓ_j ≤ 16d√N L² aη/ℓ_j. Correct.
- (26)–(27): the exponential/logarithm steps check: total exponent
  ≤ h_*(3ρ/16), e^{3ρ/16} < 4/3, log series ≤ 2× for norm ≤ 1/2;
  ℓ_{j−1}‖v‖ < ρ/(16L) gives ℓ_j‖v‖ < ρ/16. Correct.
- (30): log t ≤ 2√t and t ≥ 64p² give p log t ≤ t/4. Correct.
- (12) heredity: see the S1′ verdict below. Correct in its stated scope.
- Order of constants and non-circularity. The order PI/GW flat and
  comparison constants → M_t → floors and rates → κ_1, switch geometry →
  real/twist/current ceilings and datum radii → coupling ceiling is
  consistent with walks-gw steps 0–14. T keeps intermediate admission
  separate; "A layer estimate cannot admit its own input" is enforced in
  §1.2 T and in the closing paragraph of §3.1. No circular use found.

Repairs:
- **R3 (REVISE), (26).** GW constant step 9 requires radii a_0^*,a_1^* that
  also satisfy e ≤ c/(M_tC_Zc_Z), B_ZC_Ze ≤ 1/8 and a_* ≤ ρ/(16C_{N,L}).
  Replace "a_0^{PI},a_1^{PI}" in (26) by "a_0^*,a_1^*" and add after (26):
  "Here a_0^*,a_1^* are the radii of walks-gw constant step 9 (PI item 7
  with enlarged constants, and B_ZC_Ze≤1/8); they are at most PI's radii."
- **R4 (REVISE), (31).** walks-gw step 12 needs
  R_1M_b ≥ 2(8+b_0)log L/δ′ at every rate δ′ used. Replace
  "3\log L/\delta_q" by "3\log L/\delta_q,\ 2(8+b_0)\log L/\delta'
  \ (\text{every rate }\delta'\text{ used, }b_0=8)".
- **R5 (REVISE), (32).** walks-gw (P15) and step 13 need the floor c_ι.
  Replace "M_{\rm dec}\ge\max\{4\widehat r+8L,64\kappa_1/\mu\}" by
  "M_{\rm dec}\ge\max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1/\mu\}",
  with c_ι=c_ι(N,L) the layer diameter of a local insertion's complete
  carrier.

### §3.2

Checked against the repaired walks-gw.md (P12)–(P15), constant table and §7.
(33)–(36), θ_Z, D_*, μ = log(1/θ_Z)/(140D_X), t_ω ≤ 17D_X(n+1) and the
Euler count 16+64t/M_dec match. (38)–(39), the Wilson first-variation step
and the scalar majorant match the repaired §7. (41) is correct:
X = C(SA − SHX) gives (I + DC·SH)D_AX = DC·S, and the inverse is ≤ 2 when
c_w r h_1 ≤ 1/2.

- **R6 (REVISE), lines 804–817.** The tree must also pass through the cubes
  met by each insertion's complete carrier (walks-gw lines 575–598). After
  "including the complete-footprint representatives." insert: "For a
  primitive concatenation, join each insertion point to the adjacent anchors
  and to one representative of every cube met by its complete carrier (the
  double blocks of its averaging rows, its plaquette reads, the reads of
  j_J,k_J and its endpoint stencils). This adds at most 17c_ι per insertion,
  so t_ϖ ≤ Σ_i t_{ω_i} + 17c_ι n_ι, and needs M_dec ≥ c_ι. Each insertion is
  weighted by e^{17μc_ι} in θ^*, C_1, C_2, C_3."

### §3.3

Recomputed: |SA′−SHX| ≤ 2r + 8chr² ≤ 17r/8; image 9cr²/2 < 8cr²;
factor 3chr ≤ 3/64; auxiliary ball 9r/2, 81cr²/8 ≤ 32cr², 9/128;
9r/2 < s_C. Datum ceiling: h_0ε ≤ r/8 and (t+k)ε ≤ r/8 since a_* ≥ t+k.
Outer image ≤ r/8 + 4qr² ≤ 3r/16. Cauchy: 16qr²/(2r) = 8qr ≤ 1/8; the
4r ball lies in s_V since s_V ≥ 8r. ADVANCE.

### §3.4

Recomputed K_A, (42), (43), the three remaining entries, (44), (45) and
the unswitched U07 bound (G = B_0 + B_0Θ_JG gives ‖G‖ ≤ 2b_0 and the graph
bound b_Δ(1+2b_0θ)). "Only the last two constants use M" is correct.
ADVANCE.

### §3.5

EQ plus uniqueness gives covariance; the bounded complex-gauge overlap uses
K(K_A+h_0)s and KK_Xs. LC: restriction commutes with full-footprint words;
the −j proviso off the retained region is correct and needed. ADVANCE.

### §3.6

- (20): disc radius 1/(40D) keeps N ≤ 1/20; RJ gives 0.11K_J and 0.22K_J;
  Schwarz gives 0.22K_J·40D = 8.8K_JD; the small-radius case gives
  0.105K_J ≤ 8.8K_JD. K_j = 3+18d+9K_J matches I 111409–111415.
- (46): I derived it from ∇(χB) = χ∇B + f T B and
  ∇^T(gY) = g∇^TY − (∂^-g)T^{-1}Y. Correct. Both translation identities
  check.
- (48): integral 1; ‖v‖∞ = 150/99 = 50/33; ‖v′‖∞ = 4.5/0.9801;
  |ζ′| ≤ 50/11; |ζ″| ≤ 405000/9801 < 42; v ∈ C² since v_e″ is a sum of
  point masses convolved with a continuous triangle. At L = 3,
  5/(2L) + 42/(4L²) = 2 exactly, so "≤ 2|τ|" holds with equality at L = 3.
- (M1)–(M3): see the (M3) verdict. The subtraction giving (M3) assumes
  m_H = m_c. **R7 (REVISE).** Before (M3) write "If L_σ=Δ_W+K_W−P_1(σ) and
  m_H=m_c, its difference from the rider is exactly".

### §3.7

(49): T_1 = (I−B_0Θ_J)^{-1} since (I−B_0Θ)Γ = B_0Θ; the multiplication
step checks. (51): ‖Γ‖_{E^Δ→E^Δ} ≤ C_κ|J|_{-3} follows from (6) and
‖u‖ ≤ ‖u‖^Δ. The warnings that (51) does not rename U02/U26 data are
correct. ADVANCE.

### §3.8

(54): p(y) ≤ e^{5δ_1d/2}p(x) gives e^{−3δ_1d/2}; the second line follows
by the triangle inequality and summability at δ_1/2. (56) is the derivative
of ⟨L_gX,K_PC⟩ + ½⟨K_PC,K_PC⟩. (57) is an exact rearrangement. Spot
checks: II 55882 is the two-cutoff comparison theorem; II 58624ff is the
remark on two off-shell extensions. ADVANCE.


## (M3) verdict

**Verdict: HOLDS, as stated in the part (a test of two proposed switched
extensions, not a refutation of the layer theorem). It is a gap in the
account's assumed layer package (an undefined object), plus one
over-wide sentence; it is not a false proved step of the account.**

Source facts (read in the account).

1. I 14404–14409 defines the chart current by formula:
   Λ^J(B) = P_0^T Ξ + Q^*(q_0 − a)B̃ − Q^* k X_G − Λ^T j_J(H^J X_G),
   𝔍 = Λ^J − Δ'𝓗^J + F. Expanding 𝓗^J = A_G − H^J X_G gives exactly the
   part's (M2) with m_c of (M1). I checked this term by term.
2. I 14439–14493 proves the representation identity
   Δ_a A_G = P_0^T Ξ + Q^* q_0 B̃ and the reduced form
   𝔍 = (Δ_a − Q^*aQ − Δ')A_G − 𝒦_1 X_G + F. The proof uses the P_0G_0
   fixed-point form, Δ_a P_0 G_0 = P_0^T, Δ_a H_0 = Q^* q_0 and
   QA_G = B̃ (from QP_0 = 0, QH_0 = ℓ^{-1}). All are inverse identities.
   𝒦_1 = m_c exactly. With Δ_a = 𝒟(W) + D_0 R D_0^T + Q^T a Q and
   P = I − R (I 25322), Δ_a − Q^*aQ − Δ' = D_1^TD_1 + D_0RD_0^T
   = Δ_W + K_W − P_1 with P_1 = D_U P D_U^* (I 14727). So (18) at σ = 1
   is the account's reduced form. (M1) is correct.
3. I 15266–15339 (K10): G_0, q_0, q_J, G̃^J and the others are primitive
   and walk-tagged; composites (H_0, P_0^T, H^J, Λ, D^J, V', 𝒜, 𝓗, Λ^J, 𝔍)
   are formed "by the formulas" from the primitives at s. Q, a and the
   identity are not primitives, so they carry no tag. The fixed point at s is
   taken in the G̃^J form (I 15310–15313), not in the P_0G_0 form.
4. I 15338–15339 and 15448–15451: the explicit formulas enter only
   chart-structure-a, response-chart-a and diagonal-exactness-a, "This is
   why the first and the last of these are asserted at s≡1 only". The
   representation identity (the middle one) is not restricted there. It is
   stated "At every (U,J)∈𝔖" (I 14439).
5. I 72720–72728 and 72831–72851: the link current is
   𝔰^♯_s, "a local function of (A',X,𝒴), up to the action of the decoupled
   operators P_1(s) and m_H(s)", whose kernels "vanish unless both arguments
   lie in one component of Y(σ)". I 111394–111399 writes the rider in the
   reduced form (18) with P_1(σ), m_H(σ). The account never defines
   P_1(σ), m_H(σ) at σ ≠ 1; the layer package is assumed (I 72392–72399).

My own argument for the zero-switch test. Take site (T), so 𝖪 = ∅ and
σ_0 = π (I 72704). Put s ≡ 0. Every walk term of every primitive meets a
cube, so every primitive is zero: G_0 = q_0 = q_J = G_π^J = G̃^J = 0.
Then H_0 = H^J = B_0 = Γ = 0, and the composites P_0 = I and
k = (q_J − a)ℓ^{-1} = −aℓ^{-1}, because I and a are untagged (fact 3).
At j = 0, (S5) gives A' = 0, X = C(0) = 0, h = 0, and Ξ = 0 since V'(0) = 0.
So the rider (18) is F(W,0) = 0. The definitional current (M2), which is
the account's own 𝔍(s) of fact 3, is −Q^T a ℓ^{-1} b. Choose b on one block
bond; Q^T b is the transpose of one nonzero averaging row times b, so it is
nonzero. Also QA_G = 0 ≠ B̃, so the reduced form of fact 2 fails at s ≡ 0.
And m_c(0) = −Q^T a ℓ^{-1} ≠ 0, while Y(0) = ∅, so the locality clause of
fact 5 requires a zero kernel. The flat torus and J = 0 are not needed for
the vanishing of the primitives; they only keep the point in the admitted
class. The argument holds.

Where the identity is used. Inside the account's proved text, the
representation identity is not load-bearing at s ≠ 1:
- K3 at s (via K10 "verbatim", I 15429–15438) only reads the term list of
  I 14759–14765, which is the definitional list. The bound on 𝔍(s) is
  therefore valid without the identity.
- K6 (I 15676–15860) uses it only at s ≡ 1.
So the identity is not used beyond its hypotheses in a proved step.
The sentence at I 15450–15451 is over-wide: it leaves the identity
unrestricted although its proof is valid only at s ≡ 1.

Account or route? The account consumes the rider at arbitrary s in the
reduced form (fact 5) with P_1(s), m_H(s) that it never defines. The only
switched current the account does construct (K10's 𝔍(s), = (M2)) is not
of that form and violates the locality clause at s ≡ 0. Thus:
- It is a defect of the account's assumed package (missing definition and
  proof of P_1(s), m_H(s)), not only of the (S5) route.
- It is not a contradiction in the account: a rider defined directly by
  (18) with every local diagonal term tagged (reduce before switching) may
  satisfy everything that is consumed (holomorphy, (7), locality, value at
  s = 1 by K6). That assignment and its checks are absent. This is exactly
  premise M.

Repair to the part (REVISE, wording only). In the Outstanding M paragraph,
after "all primitive sums vanish;" insert: "here 𝖪 = ∅ (site (T), I 72704),
and, as in I 15266–15339, Q, a and the identities in P_0 = I − G_0Q^Tq_0Q
and k = (q_J − a)ℓ^{-1} are untagged composite factors;". After "…requires
a zero kernel for the empty retained region." insert: "The account's own
switched current at I 15306–15313 is (M2). Its proved bounds at s read only
the definitional term list (I 14759–14765), so no proved account step uses
the representation identity at s ≠ 1; I 15450–15451 leaves that identity
unrestricted, which is too wide. The defect is the absence of a definition
of P_1(σ), m_H(σ) at σ ≠ 1 in the assumed package." In (M3) state the
assumption m_H = m_c used in the subtraction.
This repair is **R11** below.

## S1′ / relaxed-K109 verdict

**(i) S1′ hereditary claim (adm-pl Lemma 5, part (12) and §3.1 lines
634–645): HOLDS in its stated scope. It is not a defect of the account; it
is an added clause.**

My argument. (12) is a set of inequalities on one fixed real reference U_r,
indexed by (frame F, complete read p in F). A defined layer W → e^{iηH}W
that keeps U_r does not change any left side. Restriction of reads and
discarding frames remove inequalities. A unitary gauge conjugates
U_r(∂p) − 1 and keeps its norm. A joint unit change keeps η/ℓ. So each
needed inequality is an old one. I checked that one listed site really
keeps the reference: I 10130–10133 sets U^♭ := U. The limits stated in the
part are correct and necessary: a new frame, a new real reference, or a
raised grade needs a fresh entry (cost L^{2g}). The claim is close to a
tautology; its value is only that it can be carried, not that it is supplied.

**(ii) Relaxed-K109 finding: HOLDS as a reading of the account. Whether it
is a defect of the account or only of the PL/B98-P5 route: CANNOT DECIDE.
Missing: the printed definition of CMP 109's 𝔎(𝔅;γ_0), which is not in
the paper set (`papers/` has CMP 95, 96, 98, 99a, 99b, 102 only).**

What I verified in the source:
1. I 110264–110284 defines 𝔎_109(𝔅;γ_0) by CMP 99b (3.35) on U, (3.37)
   on A′ and sup ℓ³|J| ≤ γ_0. I 110313–110317 defines 𝔎_P from it.
   No all-plaquette clause (CMP 109 (1.11)) is included.
2. CMP 99b p. 396 (papers/cmp99b.txt 425–470): (3.35) is a cube-gauge
   test "for an arbitrary cube of the described above class", and Bałaban
   notes these conditions "do not impose any constraints on U outside the
   domain Ω_0". A cube test gives PL only on plaquettes that lie in one
   class cube with their stencils (part (22)). The checked b98p5-r3 gate
   records that the fixed-side cube test alone does not give carrier PL
   (island example); that is not a counterexample to the actual induction.
3. I 116570–116572 applies the stage-layer theorem on 𝔎_P and calls it
   "the kernel-regularity space ... of CMP 109". I 119615–119650: beyond
   Y⁺ only global 𝔎_P membership is given, and at unlocalised σ the stage
   layer reads the pair there.
4. I 10637 opens the proof of conclusion (1); the chart citations at
   I 10681 ((K1),(K3),(K8)) and I 10701 ((K2),(K3),(K8)) are inside that
   proof. (2^int) at I 10608–10631 is the separate one-power branch. The
   attribution in the part and in adm-pl is correct.
5. I 10178: "the regularity class of that determining set" is not defined
   there. Elsewhere the account uses "regularity class" for CMP 99b
   (3.35)–(3.38) (I 25219, 25290) and, from §4.7, for U^{Σ¹}
   (I 30188–30196), whose representatives do carry (1.11) (I 33138–33141).
   Neither use is attached to I 10178.

Consequence. On U19, U27 and U34 the account's own class definitions do
not print S1′/PL on all complete reads beyond Y⁺. So PL must come from R,
S, or the imposed clause (12). If CMP 109's own space contains (1.11), the
account's definition at I 110264 is weaker than the space it names at
I 116570, and the gap is in the account. If it does not, the gap belongs to
any route that needs carrier PL (the B98-P5 port is one). In both cases it
is a missing admission proof, not a refutation of an account statement.

## Outstanding-paragraph audit

| Premise | Exact and complete? | Fix |
|---|---|---|
| PI | Yes | — |
| GW | No | **R8:** add "Include the insertion-carrier tree and the floors M_dec ≥ c_ι, R_1M_b ≥ 2(8+b_0)log L/δ′ and δ ≤ δ_* ≤ μ of walks-gw constant steps 11–13." |
| AV | Yes | — |
| R | No (incomplete) | **R9:** after "by its wording." add "The account uses 'regularity class' for CMP 99b (3.35)–(3.38) at I 25219, 25290 and for U^{Σ¹} from I 30188; neither is attached to I 10178, and only U^{Σ¹} prints (1.11)." |
| A0 | Yes | — |
| L0 | Yes | — |
| S | No (one wrong label, one omission) | **R10:** replace "it does not include full CMP 109 (i)–(iii)" by "it uses only CMP 99b (3.35), (3.37) and a current ceiling; it does not include CMP 109 (1.11)–(1.16), in particular the all-plaquette clause (1.11). I 116570 nevertheless names 𝔎_P the space of CMP 109; whether that printed space contains (1.11) is not checked here (CMP 109 is not in the paper set)." |
| T | Yes | — |
| P2 | Yes | — |
| ID/EQ/PH/LC | Yes | — |
| M (M3) | Exact in content; missing two load-bearing conventions | **R11:** the two insertions written under "(M3) verdict" above (site (T) with 𝖪=∅; Q, a and the identities untagged; K10 bounds read only the definitional term list; I 15450–15451 too wide; the defect is the undefined P_1(σ), m_H(σ)). |
| RJ | Yes | — |
| FD | Yes | — |
| FM | Yes | — |
| E(e) | Yes | — |
| RC | Yes | — |

The use lists inside the paragraphs (PH, LC, FD, S, T, P2, RC, E(e))
agree with the table rows. I checked each cross-reference.

## U01–U34 table check

Each row follows from Theorem LAYER and the premises it names, with
D[U] = PI, GW, AV, ID and R, A0, L0, T. Rows that read the last two N1
entries or the rider (U01, U14, U19, U27, U29, U30, and others through N)
carry M. Rows that read only response size use V (U20, U31). U14 and U15
are correctly "Covered" relative to furnished data. U21's normalization
matches the account's own remark (I 131624, 131668–131672). U33 correctly
needs RC plus residual (56). No row claims more than the theorem gives.
The redundant "L0 and R/A0" in U07 (already in D) is harmless.
**ADVANCE.**

First failing step: §3.1 (32), feeding §3.2 (37): the cube floor omits
c_ι, so the insertion-carrier count in the decoupling bound is not proved
as written (repairs R5, R6). No step is false after the repairs.

## Overall verdict

**FREEZE WITH REPAIRS: R1–R11.**

- R1 §1.1: say which identity factors carry tags.
- R2 §1.1: δ ≤ δ_* ≤ μ for admitted weights.
- R3 §3.1 (26): use GW's radii a_0^*, a_1^*.
- R4 §3.1 (31): add R_1M_b ≥ 2(8+b_0)log L/δ′.
- R5 §3.1 (32): add c_ι to the M_dec floor.
- R6 §3.2: tree through insertion carriers; weights e^{17μc_ι}.
- R7 §3.6: state m_H = m_c before (M3).
- R8 §4 GW: name the floors of R4–R6 and R2.
- R9 §4 R: name the two account uses of "regularity class".
- R10 §4 S: correct the CMP 109 label; note I 116570.
- R11 §4 M: state site (T), the untagged factors, and where the identity is
  and is not used.

No BLOCK. The conditional theorem is proved from exactly its named imports
and premises once R1–R6 are applied.

Checked line by line by Claude (Opus 5.5).
