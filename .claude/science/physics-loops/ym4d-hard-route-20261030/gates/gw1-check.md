# Check of library/gw1.md

- File checked: library/gw1.md (1031 lines; research text by Codex, gpt-6-astra; repo revision
  0ec6a547f9 in its header; FINISH row 464).
- Task: one line-by-line check of the written port of CA-I (J7), 13944–13955.
- Date: 2026-11-08.
- Status: complete.

Sources read for this check: library/prior/gw1.md in full (brief; §6 (b)–(d) is the target);
library/gw1.md in full (by ranges); walks-gw.md 36–150 (theorem, (P1)–(P2)), 493–800 (§5 tags and
(P14)–(P15), §6 first-order branches, start of §7 averaging vertex); print-inverse-r2.md 322–366
(Theorem PI (a)–(e)); gates/layer-part-ref.md 187–274 (M3); b99.md 1594–1640 (B15 statement);
CA-I 13402–13452 (kernel classes), 13681–13980 (lemma 4.5:lem-free-current-operators, J1–J8 and
proof), 15262–15465 (K10 statement and proof), 14512 (c_K). Imports PI, GW and the frozen layer
part are used as given and not re-checked.

## Verdict summary

| Section | Verdict | One line |
|---|---|---|
| 1. Theorem and assignment (24–123) | REVISE (wording) | Matches brief (b) and the J2–J4 transfer; claims nothing more. The identity convention (14) for Π is a port choice and must be named (R1). |
| 2. Imports and norms (125–203) | ADVANCE | The restricted PI/GW imports exist at the cited places; norms are scale-consistent. |
| 3.1 Absolute algebra (216–275) | ADVANCE | (8) follows from (P14); doubling the reserve doubles the junction charge; finite reweighting before κ_1. |
| 3.2 Current vertex (277–331) | ADVANCE | (10)–(13) are scale-correct; only sup of w; J is not differentiated. |
| 3.3 Scalar branches (333–418) | ADVANCE | (15)–(16) is the exact Π expansion; the derivative and exponent allocation is right in every row. |
| 3.4 Nine terms, columns (420–520) | ADVANCE | (18)–(22) correct; the typed transpose and the Schur column are kept apart. |
| 4. Unswitched inverse, J2 (522–608) | ADVANCE | Series, ∇^* members with one source exponent, termwise transposes, inverse identity at one. |
| 5. Coarse inverse (610–742) | ADVANCE | Normalizations (28)–(31), (33)–(34) and the endpoint-only scale ratio (35)–(37) are correct. |
| 6. Lift and transpose (744–816) | REVISE (wording) | (39)–(42) correct; the B99 identification at 810–816 is cited, not proved, and must be labelled (R2). |
| 7. Words, switches, restriction (818–951) | ADVANCE | Union tags, e^{16κ_1}e^{μt} with a spare e^{μt}, product lift e^{32κ_1}, no switched inversion, separation including the untagged Q^*. |
| 8. Constant order (953–998) | ADVANCE | Non-circular; j_* precedes κ_1. |
| 9. Scope and account lines (1000–1031) | REVISE (citations) | Every cited range is supplied; three ranges are off by a few lines and the J2 proof range is missing (R3). |

## 1. The theorem and its assignment (lines 24–123) — REVISE (wording)

Definitions (2) match CA-I 13727–13739 term by term: Λ = G'RD^*, Π = I − DΛ,
K_J = Θ'_J + Π^TΘ_JΠ, Θ_J built from H^J (not H_1^J), G_1^J = Σ(G_0K_J)^nG_0
(equal to the account's ΣG_0(K_JG_0)^n), q_{1,J} = (QG_1^JQ^*)^{-1}, H_1^J = G_1^JQ^*q_{1,J}ℓ^{-1}.
The gap (1) is the account's ε = (1−β_0)/2 with β+ε ≤ (1+β_0)/2 < 1 (CA-I 13858–13861).

Items 1–4 against the brief's minimal statement (b) (prior/gw1.md 345–359):
- item 1: J2 sup-data members F_3 → E_1^β, the ∇^* members on C_2^ε (and on C_2^{α_β}),
  the gap retained, no Laplacian member. Matches (b) bullet 1 and CA-I 13759–13764.
- item 2: (3) is the (b) density bound; K_{-2} follows by CA-I 13443–13449 (iv). Row and column
  majorants are claimed. Matches (b) bullet 2.
- item 3: K_{-1}, the J4 readouts, transpose F_3 → coarse weight −4, and the two identities at
  one. These are the J4 assertions of CA-I 13766–13774 transferred by (J7). Matches (b).
  The account writes N_β(H^JB) ≤ B_0|B| with H_0's constant; its own J4 proof gives B_0 + O(j).
  The port's C|B| is the correct reading; not a defect.
- item 4 and the switch paragraph: analytic words, absolute majorants with spare tree decay,
  restriction compatibility, zero-switch separation, expansion at one, union tags,
  Ce^{16κ_1} on |s| ≤ e^{κ_1} above the cube floor (4), j_* independent of κ_1. Matches (b).
- the lift paragraph (111–123): CA-I 15306–15308 lists H_1^J among the composites formed "by the
  formulas" from primitives at s, and CA-I 15279–15280 lists (QG_1^JQ^*)^{-1} as a primitive. So (5)
  is the account's assignment, with two tag products. The union-tag alternative is correctly
  stated as a different switched lift, equal at one only.

The theorem claims nothing beyond (b) and the J2–J4 statements that (J7) transfers. The extra
items, (G_1^J)^{-1} = Δ_a − K_J and ℓQH_1^J = I at one, are J2/J4 members.

One wording gap. Line 45 says "use precisely the account's definitions", and the switch paragraph
tags "complete footprints". The footprints use PI words and the identity convention (14),
I_f = Σ_τ h_{τ,f}^2 I_f, for the identity part of Π. The account does not fix that convention:
CA-I 15283–15302 gives Π's identity no localisation domain of its own, and its J8 parenthetical
(13797–13801) lists only H^{J,T}J as the side branch of Π^TΘ_JΠ (the port correctly also
includes the Λ words of Π). GW fixed the same convention for R only (walks-gw.md 101–105;
walks-gw-check.md "a choice. The account does not fix it"). The choice is harmless: at s ≡ 1
Σh^2 = 1, and every bound in §§3–7 also holds if the identity carries no domain. But the
identification sentence must name it.

**Repair R1.** After line 98 ("... met by its complete footprint."), insert:
"The words are PI/GW words, chosen by the rule of §7.1. The identity part of Π is assigned by (14),
I_f = Σ_τ h_{τ,f}^2 I_f with PI's cutoffs and full footprints. This extends GW's convention for R
to Π. The account does not fix it; at s ≡ 1 it gives the account's operator. The switched
primitives identified here are those of this assignment."

## 2. Named imports and local norms (lines 125–203) — ADVANCE

The imports are the restricted ones of the brief: PI Theorem (print-inverse-r2.md 322–365; I read
(a)–(e), including q_0 = −m^{-3}[M_5^{-1}]_{νν}m at 328 and the endpoint margin (2L+1)M_tℓ at
362–363); GW (P5), (P7), (P11)–(P15), §§5–8. The GW §6 word bounds used later are present at
walks-gw.md 635–700: scalar G'D^* bounded → C^α (0<α<1); G_0D on C^ε-data with gradient C^β,
β below the data exponent; P bounded → bounded first derivative; reversed words for transposes;
"the column estimate is the ordinary-source first-derivative estimate on the reversed scalar
word". The scalar output power a means m^a|u|, m^{a+1}|∇u|, source m^{a+2}|f| (walks-gw.md
129–132), so the a = 0 row of the table in §3.3 is supported. B99 is cited for reuse only.

Norms (6) are the normalized cell norms; (7) is GW's vector differentiated source with
V_3 + D C_2^α (walks-gw.md 642–646). Weights p are never differentiated. The smooth-partition
and zero-extension Hölder conventions are GW's. No defect.

## 3. The first hard step: G_0Π^TΘ_JΠ, all branches (lines 205–520) — ADVANCE

### 3.1 Absolute algebra with the extra tree reserve (216–275)

(8) follows from (P14) exactly: k ≤ Cθ_Z^{n/2}e^{−μd−2μt} gives
k e^{2μt+λd} ≤ Cθ_Z^{n/2}e^{−(μ−λ)d}. GW spent e^{μt} of the 2μ budget on its weights
(walks-gw.md 606–613); the port keeps all of it, which is what later leaves a spare e^{μt}.
D_*θ_Z^{1/4} ≤ 1/4 (walks-gw.md 532) sums D_*^n θ_Z^{n/2} from either end, so row and column
sums converge. (9) is GW's t_ϖ ≤ Σt_ω + 17c_ι n_ι (walks-gw.md 590) per junction; doubling the
reserve doubles the junction charge to e^{34μc_ι}. Submultiplicativity of the weighted Schur
norms then holds with a fixed per-junction constant. Lines 272–273 state that every later norm
includes these costs. So in (23)–(24) the junction to the next factor is inside C_K; I read it so.
The reweighting of GW §6's H^J, q_J, G_π^J families is a finite change of constants of the same
proof; the preliminary ceiling is re-chosen once, before κ_1. Correct.

### 3.2 The current vertex (277–331)

(10): w(c) = Σ_b η^4 H^J(b,c)J(b) and |J(b)| ≤ m_u^{-3}j give m_c^4|w_{c,γ,u}| ≤ h_γ(c,u)j.
The sum over γ,u with tree weight is GW's physical transpose majorant H_T^*.
(11) is GW §7's one-leg density Cℓ_c^{1−4} (walks-gw.md 790–791). Scale check: for B of weight −1,
(ΘB)(x) ≈ Σ_c m_c^4 w(c)·density ≤ Σ_c h j·C m_c^{-3}‖B‖_{V_1}; bounded carrier multiplicity
gives V_1 → V_3, as J5 (CA-I 13775–13781) requires. Leg interchange is the polarization of
⟨A,Θ_JA⟩ = 2⟨C^{(2)}(ℓA),H^{J,T}J⟩, so Θ_γ^T is the same vertex with legs swapped and the same
branch. Only sup|w| enters; J is not differentiated. (13) follows.

### 3.3 Scalar branches and identities (333–418)

Π = I − DG'RD^* with R = I_s − P gives Π = I_f − DG'I_sD^* + DG'PD^*, i.e. (15) with
σ = (1,−1,1). Then G_0Π^T = Σσ_a G_0B_a^T and B_1^T = D I_s^T G'^T D^*, B_2^T = D P^T G'^T D^*,
which is (16). At one R and G' are symmetric, so L_1 − L_2 = G_0DRG'D^*, the account's
Λ^T D^* term (CA-I 13944–13950: φ' = RG'D^*f'). The order R after G' agrees.

The allocation table is correct row by row:
- B_b: E → V_1 uses only ∇A (D^*A ∈ V_2), a V_2 multiplier or P, then DG' with the a = 0 scalar
  bounds (value power 0, gradient power 1). Constants r_a are products of these.
- L_a: V_3 → E_1^β. G'^T D^* sends a bounded force to scalar C_2^{α_β} (GW scalar divergence
  source, a = 2: source m^3|g|, output m^2|u| + m^{2+α}[u]_α). I_s^T and P^T keep C_2^{α_β}
  (P^T maps bounded data to Lipschitz, which dominates C^α locally). G_0D sends C_2^{α_β} to
  E_1^β with gap α_β − β = ε. L_0 = G_0I_f uses the ordinary vector source.
- u_a: B_a^T: V_3 → D_{α_β} is the representation D(I_s^TG'^TD^*f) in (7), not a pointwise
  derivative. Correct.
Exponent margins: ε ≤ α_β ≤ β_0 + ε = 1 − ε. Fixed positive margin; no limit exponent. Correct.

### 3.4 The nine terms and physical columns (420–520)

(18) is the exact expansion; the term count (1 + 4 + 4) is right. (19) is a nonnegative
convolution; norm ≤ l_a ϑ^* r_b. (20): (L_aΘB_b)^T = B_b^TΘ^TB_aG_0^T, read right to left
V_3 → E → V_1 → V_3 → D_{α_β}; correct, with constant u_b ϑ^* r_a g_0 and the same branch.
(21) scale neutrality m^4·m^{-1}·m^{-3} = 1 and m^4·m^{-2}·m^{-2} = 1 is correct.
(22) and the two forward Schur sums are distinct from the typed transpose readout; the text keeps
them apart. In a reversed chain the insertion G_0^TB_b^TΘ^TB_a is E → E_1^β through the reversed
vector Hölder-source word on D_{α_β}; correct. Each insertion regains C^{α_β} from a bounded
force, so the gap is not spent along a chain (the same mechanism as CA-I 13863–13870).
No ∇J and no Hölder norm of J enter. The brief's first hard step (d) is done.

## 4. The unswitched inverse and the J2 readouts (lines 522–608) — ADVANCE

(23): A_J = G_0Θ'_J + T_J; GW §6 gives the first summand (walks-gw.md 724–731), (22) the second.
(24): G_1^J = ΣA_J^nG_0 with a ≤ 1/4 converges in the algebra of §3.1; bounds g_0/(1−a) and
ag_0/(1−a) are right once C_K carries the right-hand junction cost (lines 272–273).
A term is a product of nonnegative majorants with every branch kept; no switched sum is resummed.
(25)–(26): the ∇^* members need the source exponent only at the first bare word; later
insertions use (23). For g ∈ C_2^ε the n = 0 term lies in E only and the rest in E_1^β, so
G_1^J∇^*g ∈ E; for g ∈ C_2^{α_β} all lie in E_1^β. This is the account's J2 mechanism
(CA-I 13885–13889). (26) at equal scales gives m^2, m, m^{1−β}; the long-range scale ratio is
paid by (35). Transposes: the reversed chain with literal transposes; termwise, as stated.
(27): Δ_a − K_J = Δ_a(I − G_0K_J); on a finite lattice ‖A_J‖ ≤ 1/4 in E makes I − A_J invertible,
and (Δ_a − K_J)(I − A_J)^{-1}G_0 = Δ_aG_0 = I. Correct, at one only, with no Laplacian member
extracted. This supplies the J2 identity (G_1^J)^{-1} = Δ_a − K_J.

## 5. The coarse inverse with physical scale factors (lines 610–742) — ADVANCE

(28): the normalized B_1 → B_3 matrix is m_c^3·m_{c'}^4 q·m_{c'}^{-1} = m_c^3m_{c'}^3q. Correct.
(29): from PI (a) q_0 = −m^{-3}[M_5^{-1}]_{νν}m as a counting operator, the density is
−m_c^{-3}m_{c'}^{-3}M, so q̂_0 = −[M_5^{-1}]_{νν}. Correct; (8) gives both Schur sums.
(30)–(31): Q^*: B_3 → F_3, G_1^J − G_0: F_3 → E, Q: E → B_1, q_0: B_1 → B_3, so E_J: B_3 → B_3 and
Ê_J = m^3E_J^{count}m^{-3}. Correct. (32) follows from (24).
Column claim: the physical transpose of E_J on B_1 has normalized matrix
m_c·m_{c'}^4E_J(c',c)·m_{c'}^{-1} = m_c m_{c'}^3 E_J(c',c) = Ê_J(c',c). Correct.
(33): QG_1^JQ^* = QG_0Q^* + Q(G_1^J − G_0)Q^* = q_0^{-1}(I + E_J), at one. (34): q_{1,J} =
(I + E_J)^{-1}q_0 = Σ(−E_J)^rq_0, and the normalized identity Σ(−Ê_J)^r q̂_0 is the conjugated
form. This is the J3 route (CA-I 13899–13911) with G_1^J for G_π^J. Each word starts and ends
with a q_0 word; the r = 0 term is a q_0 word, so no empty-footprint identity term. Correct.
(35)–(36): q = m_c^{-3}m_{c'}^{-3}q̂ = m_c^{-2}m_{c'}^{-4}(m_{c'}/m_c)q̂; with b = 1 in (35) and
8 log L/ρ ≤ λ/4 the ratio costs at most Le^{λd/32}, so δ ≤ λ/4 is enough. (37): the two
endpoint ratios (m_{c'}/m_c and m_c/m_{c'}) appear once each; no ratio per correction. The first
line with CA-I 13443–13449 (iv) gives K_{-2}; the second is the column bound. Correct.

## 6. The lift and its physical transpose (lines 744–816) — REVISE (wording)

(39): B_0 → B_1 → B_3 → F_3 → E_1^β is scale-consistent (m_c·m_c^{-1}|B| = |B| at the first
step). (40)–(41): the single-source column gives |H_1^J(b,c)| ≤ Cm_y^{-1}m_c^{-4}e^{-δd}, which
is the kernel form of K_{-1} in CA-I 13443–13447 with output power −1 and source density
ℓ^{-4}; no long-range ratio arises because both endpoints are normalized in their own scales.
(42): Σ_{b∈y}η^4 ≤ Cm_y^4 and m_y^{-1}·m_y^{-3}·m_y^4 = 1 give H_1^{J,T}: F_3 → B_4 by the column
majorant. This is the weight-−4 transpose J5 needs for H^J, now for H_1^J. Correct.
The item-3 identities follow from (27), (33), (38) at one: QH_1^J = QG_1^JQ^*q_{1,J}ℓ^{-1} = ℓ^{-1},
and (Δ_a − K_J)G_1^J = I. Correct.

Lines 810–816 are not part of Theorem GW1 and are not proved here. They identify the totals
with Balaban's corrected operators on B99's true-current class, and say that B99's unscaled lift
is H_1^Jℓ. The weight shift −4 → −3 is dimensionally consistent with that, but the identification
rests on CA-I 13755–13758 (Θ'_J = Δ'_π at J = J(U)), on Π^TΘ_JΠ matching Balaban's (3.135) at
own current, and on B99 B15. None of these is re-derived in gw1.

**Repair R2.** Replace lines 810–816 ("On the intersection ... is not replaced by this port.") by:
"Remark (cited, not part of Theorem GW1). At switches one and own current J = J(U), on B99's
admitted true-current class with the same rows and Hessian, the account identifies these totals
with Balaban's corrected operators (CA-I 13755–13758 and (J7)); B99 B15 constructs those real
operators. With the account's normalization, Balaban's lift is H_1^Jℓ, so B99's induced-current
weight −3 corresponds to weight −4 in (42). This port does not re-prove that identification and
does not replace B99's true-current proof."

## 7. Words, switches and exact restriction (lines 818–951) — ADVANCE

### 7.1 Words before switching
The word rule (number of insertions, branch choice per insertion, every bare, projection,
identity and current-leaf word; for q_{1,J} every factor and compression row) is a complete
assignment. Words are polynomial in finitely many current leaves, since GW builds H^J by current
Neumann words. Two-stage truncation with positive majorants justifies the regrouping and gives
analyticity by uniform convergence on compact sets. Correct.

### 7.2 Union tags (43)–(46)
(43) is the account rule of CA-I 15284–15302: one factor per cube met by any localisation
domain, side branches included. (44) is GW's Euler count (walks-gw.md 561–573), applied to the
tree through every carrier and branch. With M_dec ≥ 64κ_1/μ, #cubes ≤ 16 + 64t/M_dec gives
|s_w| ≤ e^{16κ_1}e^{μt_w}, which is (45); the 16 = 2^4 is the account's case split at
CA-I 15380–15384. The algebra carries e^{2μt}, so (46) holds with a spare e^{μt}: this is the
"spare tree decay" of (b). Primitives get Ce^{16κ_1}, as CA-I 15322–15323 requires.
The lift (5) is a product of two primitive majorants: Ce^{32κ_1}. CA-I 15324 and 15424–15427 bound
composites by B_0e^{c_Kκ_1} with "the absolute integer c_K" (CA-I 14512: "independent of all
parameters", otherwise free). So the lift needs c_K ≥ 32, a fixed integer. GW T3 uses the same
product rule (walks-gw.md 86–90). Consistent.
Lines 908–912: neither QG_1^J(s)Q^* nor I − G_0(s)K_J(s) is inverted; the series at one only
generate words. This is the K10 statement "not re-summed at s" (CA-I 15285–15286). Correct.

### 7.3 Common footprints and zero components
Restriction: as PI (e), with current and carriers added. Correct.
Separation: a surviving word meets only retained cubes and has a connected footprint, so it lies
in one component of Y(σ). For (5), the untagged Q^* sits between G_1^J and the leftmost q_0 word
of q_{1,J}. PI (e) puts the q_0 support at distance ≥ (2L+1)M_tℓ from the boundary of |ω|
(print-inverse-r2.md 362–363); with M_t ≥ 4L this contains the double-block carrier of c.
So the Q^* fine point lies in a retained cube of the same component, and the G_1^J word from that
point stays in it. Correct. At s ≡ 0 every primitive and the lift vanish; no untagged identity
summand exists in these composites, so the M3 mechanism (an untagged a or I surviving at s ≡ 0,
layer-part-ref.md 226–244) does not arise here. The text correctly limits the claim to primitive
and lift locality and leaves P_1(s), m_H(s) to LAYER-THM.

## 8. Constant order (lines 953–998) — ADVANCE

| Order | Constant | Depends on |
|---|---|---|
| 1 | N, L, β_0, ε; GW source spaces; flat tile, gap, torus room | — |
| 2 | M_t, r_N, r̂, D_X, θ_Z, μ = log(1/θ_Z)/(140D_X), D_*; background and averaging radii | 1 |
| 3 | c_ι (carriers, N,L only); identity, partition, carrier constants; junction cost e^{34μc_ι}; reweighted GW majorants; preliminary H^J ceiling | 1, 2 |
| 4 | H_T^*, C_av, the (17) constants, g_0, C_Π, C_K, q_*, C_comp (uniform for 0<λ≤μ/4, above the floors); j_* with C_Kj ≤ 1/4, C_comp·C_Kj/(1−C_Kj) ≤ 1/4 on j ≤ 2j_* | 1–3 |
| 5 | λ ≤ μ/4 and below GW endpoint rates; δ ≤ λ/4; floors (P5), 8 log L/ρ ≤ λ/4, PI separation, divisibility, torus | 2, 4 (uniformity only) |
| 6 | κ_1; M_dec ≥ max{4r̂+8L, c_ι, 64κ_1/μ} | 2, 3, κ_1 |

Non-circular. μ and c_ι precede j_*; j_* precedes κ_1; M_dec is chosen last. The floors in
step 5 come after the step-4 constants, but those constants are uniform above the floors, which
is GW's accepted order (walks-gw-check.md, constant-order checks). The extra reserve is paid by
the junction cost in step 3, not by a κ_1-dependent current reduction. The account requires this:
its insertion conditions "do not involve κ_1" (CA-I 15409–15412).
One wording point, no repair needed: step 6 says c_ι "includes the carriers used in this port".
c_ι is fixed in step 3 (it sets the junction cost); step 6 only restates its content.

## 9. Scope and account lines supplied (lines 1000–1031) — REVISE (citations)

The scope paragraphs are correct and match prior/gw1.md §6: no Laplacian member, no general
layer HΔ, no positivity at arbitrary current, no precision/root family, no domain admission,
no M3 repair, no identity carried through switching.

Each cited range, read in the account:

| CA-I lines | Content on the page | Supplied by gw1? |
|---|---|---|
| 13758–13771 (via 13783–13784) | 13758 is the last line of J1; J2–J4 run 13759–13774 | Yes: §§4–6 give the J2 members, J3 K_{-2}, J4 K_{-1}, readouts and identities. Range is off by one/three lines. |
| 13850–13874 | J1 proof: G_0θ split, (3.44)/(3.45) with gap ε, "no Hölder norm of J", weighted norms (the paragraph starts 13847) | Yes: §3.3–3.4 table, (22), lines 514–520. |
| 13944–13955 | J7 proof: Π^T = I − DRG'D^*, f', φ', "apply verbatim" | Yes: (15)–(22) write the termwise version. |
| 13896–13920 | 13896–13897 end the J2 proof; J3 is 13899–13911, J4 13912–13920 | Yes: §5 (J3 route) and §6 (J4 decomposition replaced by the direct product (39)). The J2 proof itself (13876–13897: series, ∇^* first iterate, telescoped inverse) is supplied by §4 but not listed. |
| 13957–13977 | J8 proof: local propagators, walk expansions, polynomial current, concatenated q-walks | Yes, on the PI/GW class: §7.1 (PI words replace the CMP 99b Cor. 3.5 local construction). |
| 15278–15314 | primitive list, expansion at one, tag rule with the CMP 116 quotation, composites by formula, A_0^J(s) form | Yes for G_1^J, q_{1,J}, H_1^J: (43), (5). |
| 15322–15324 | K10 item 1: primitives B_0e^{16κ_1}, composites B_0e^{c_Kκ_1} | Yes: (46) and Ce^{32κ_1} with c_K ≥ 32. |
| 15333–15337 | K10 items 3–4: separation, equality at s ≡ 1 | Yes: §7.3 and §7.1 regrouping at one. |

**Repair R3.** In the table at lines 1021–1029: change "13758--13771" to "13759--13774";
change "13850--13874" to "13847--13874"; change "13896--13920" to "13899--13920"; and add the row
"| 13876--13897 | The J2 series, the ∇^* first iterate and the inverse identity for G_1^J (§4). |".
Line 1031 should also be updated to name this check once R1–R3 are applied.

## The six questions

1. **Theorem vs digest (b).** Yes. Items 1–4 and the switch and lift paragraphs are exactly the
   (b) bullets plus the J2/J4 members that (J7) transfers (inverse identity, ℓQH_1^J = I at one).
   Nothing beyond (b) is claimed in the theorem. The only extra text, the B99 identification at
   810–816, is outside the theorem and needs the label of R2.
2. **Switched inversion or representation identity after switching.** None. QG_1^J(s)Q^* and
   I − G_0(s)K_J(s) are never inverted (908–912); (27), (33) and the item-3 identities are used
   at one only; identities in (14) are not substituted after tagging; §7.3 uses footprints only
   and leaves P_1(s), m_H(s) to LAYER-THM. The composites here have no untagged identity or mass
   summand, so the M3 zero-switch mechanism does not arise.
3. **Tag constants.** Consistent. Primitives Ce^{16κ_1} match CA-I 15322–15323 and the 2^4 case split
   (15380–15384), via GW's count with M_dec ≥ 64κ_1/μ. The lift is a composite by CA-I 15306–15308,
   so its two primitive tags multiply to Ce^{32κ_1}; this fits B_0e^{c_Kκ_1} once the free absolute
   integer c_K (CA-I 14512) is at least 32, and GW T3 and layer-thm-part.md 832–833 use the same
   product rule. The ceiling j_* is fixed in step 4, before κ_1 in step 6; non-circular.
4. **Hölder gap; J not differentiated.** Kept: ε = (1−β_0)/2 fixed, ε ≤ α_β ≤ 1−ε, vector loss ε,
   regained at each insertion from a bounded force. Only sup|w| = sup|H^{J,T}J| and |J|_{(-3)}
   enter (lines 331, 519–520); J is never differentiated.
5. **Account lines supplied.** All eight ranges read. Each is supplied on the PI/GW class.
   Three range boundaries are off by one to three lines and the J2 proof (13876–13897) is
   supplied but not listed; repair R3.
6. **Constant order.** See the §8 table. Order: (N,L,β_0,ε) → (M_t, D_X, θ_Z, μ, D_*) →
   (c_ι, e^{34μc_ι}, reweighted GW constants, preliminary ceiling) → (H_T^*, C_av, (17), g_0, C_Π,
   C_K, q_*, C_comp; j_*) → (λ, δ; floors) → (κ_1; M_dec). Each depends only on earlier ones
   (step 5 floors use only the uniformity of step 4). Non-circular.

First failing step: none. (R1–R3 are wording and citation repairs; no mathematical step fails.)

## Overall verdict

**REVISE (wording and citations only). No BLOCK.** With R1–R3 applied, Theorem GW1 holds as stated,
as a corollary of the PI/GW word algebra, and it supplies the (J7) port asked for in prior/gw1.md §6.

1. R1 (§1, after line 98): name the assignment, including the identity convention (14) for Π, as a
   port choice extending GW's R convention; equal to the account at s ≡ 1.
2. R2 (§6, lines 810–816): relabel the B99 identification as a cited remark outside Theorem GW1.
3. R3 (§9 table): correct the CA-I ranges to 13759–13774, 13847–13874, 13899–13920; add 13876–13897.

Observation, no repair: in (23)–(24), C_K (and C_comp in (32)) carry the junction constant to the
next factor; lines 272–273 say so, and the bounds are read that way.

Checked line by line by Claude (Opus 5.5).
