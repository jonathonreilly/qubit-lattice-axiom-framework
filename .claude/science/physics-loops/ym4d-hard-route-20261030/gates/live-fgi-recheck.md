# Recheck of library/live-fgi.md (repaired)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading. Not an audit.
Note last changed at `ba87a59fc` (clone head `79192bd78`). Source: CA-I raw (I), local copy.
Earlier check: `live-fgi-check.md` (verdict FIX).

## Verdict: FIX (one line; the counterexample stands after it)

Every repair asked for is applied. Both core forms give two 3a-cubes with the midpoint missing.
Omega^c_{h+1} has two components. Z_{h+1} is one box. Section 4 holds at 20a.
One new defect: the note lets N < R. The account's waiting depth is R exactly.
With N < R the operation at h is barred, so the prehistory fails.
Fix: set N = R in (7) (allowed by (7) itself), or put the creations at b = h - R.
Nothing else changes.

## Findings

1. **Repairs applied (note 49, 88-100, 177, 267-271, 279-299, 407-432).** CONFIRMED.
   - Core by I 78969 and I 93532, and by I 63870: note 88, 93-99, 279-289.
   - Y_1 = 20a e_1 + Y_0: note 177.
   - I 118402: note 49, 270-271. I 55350-55418: note 267-269.
   - Later no-joining assumptions I 115866, 125168, 143731: note 407-412.
   - Box sentence of (g) at I 85629: note 299. Line 85629 is "The set C_C is a box, ...".
   - I 63872 false in the example: note 419-424. Span (20L+21)a_h > 100a_h. Correct.
   - The s = 6 failure of the I 78969 identity: note 428-431. I recomputed it.
     At s = 6, N_8 cubes overlap, so Omega^c is one box; E_5 then E_2 gives [-3/2,15/2]x[-3/2,3/2]^{d-1} (units a).
     N_1(Q_0 u Q_6) is two cubes with gap 3a. The forms differ. Correct.

2. **Waiting depth (note 159-163, 188-201; I 49762-49765, 49785-49800, 51178-51189, 51389).** MISMATCH.
   I 49762: "The waiting depth at level k is N = N_k := Ř_k" (sans-serif N).
   I 49793 (ii'): "C ∩ W^_t = ∅ for every integer t with k - N_k < t ≤ k", with N_k = Ř_k.
   I 51178-51189 (waiting rule): a creation in W^_s inside C needs k - s ≥ N_k = Ř_k.
   I 51389 identifies h := k - N_k with Balaban's h = k - N. I 125168 runs "the R_k steps of the run".
   Note (7) takes "the fixed waiting depth N with N_0 = p+1 < N ≤ R".
   Note 200: "At h, h - b = N." The rule needs h - b ≥ R. This fails if N < R.
   Then the creation at b lies in (h - R, h], and R cannot act at h. Y_0, Y_1 are never made.
   Fix: N = R. Then N_0 = p+1 < L^p = R, h > R+1 ≥ R, k > N > N_0 (I 45848), and N ≤ R_k (I 53763).
   With N = R every later use of N in the note is unchanged and correct.
   Alternative fix: keep N and put the creations at b = h - R.

3. **Class tests at 20a (note 255-265; I 45984-46000).** CONFIRMED, given finding 2's fix.
   - (i) "X is contained in a cube of size 100MR_k": C = Z_k has side 21a_k. Passes.
   - (ii-a) first clause "no new large-field region created by one of the operations T_{j→j+1}, h≤j≤k-1": all seed and test sets empty. Passes.
     I 55350-55354: an R-operation at s ≤ h inside Z "is admitted ... this includes the case s=h". So the second-class Y_r at h are allowed.
   - (ii-a) second clause "every previous region contained in X satisfies (i) on its own scale": Y_0, Y_1 side 21a_h; Z_{h+1}∩C sides 41a, 21a; Z_i∩C side 21a_i for i ≥ h+2. Passes per region.
     I 118402: "bounds each previous component but not their number, and ... forbids the creation ... but not the joining of components". Supports this reading.
     I 55398-55400 reads (ii) as a bound on Z_j∩Z for "the levels h+1,…,k only". Passes too: Z_{h+1}∩C is one small box.
     Only the reading "Z_h∩C lies in one 100a_h cube" fails. That reading is I 63872, the sentence under attack.
   - (ii-b), window (k-N_k,k) = (h,k): the marks are at h, outside. Passes. I 46021-46025 states the open window is the account's choice.
   - Intervening steps h<t<k: h ∈ (t-N,t), so (ii-b) bars any operation. Note 252-253 correct.
   - Waiting rule at h and below: correct only with N = R (finding 2).
   - Box fact I 63547-63551: "each component is a box with sides a_μ Ř_k, a_μ ∈ {1,…,100}" and distinct components at distance ≥ Ř_k.
     Level h: two 21-cell boxes, gap (20L-21)a_h. Level h+1: one 41x21 box. Later: 21-cell cubes. Passes.
   - Second-class rule I 64479-64495: "takes its class as a whole". Y_r are whole components with flat level-h labels. Passes.

4. **Step h→h+1 at 20a (note 204-238; I 50046-50054, 50196-50229, 50342-50372).** CONFIRMED.
   With empty P', Q': Omega^c = Ŷ^{~8} (I 50225). With empty R': Z = M(Ŷ^{~10}) (I 50343, 50354, 50365-50367).
   Units a = a_{h+1}. Hull of Y_0 u Y_1 is Q_0 u Q_20: both boxes have half-side 21a/(2L) < a/2, strictly inside.
   N_8: [-17/2,17/2] and [20-17/2, 20+17/2] = [23/2,57/2]. Gap 23/2 - 17/2 = 3 cells. Not touching. Two components.
   N_10: [-21/2,21/2] and [19/2,61/2]. Overlap [19/2,21/2], width 1. Transverse intervals equal, [-21/2,21/2].
   Union = [-21/2,61/2]x[-21/2,21/2]^{d-1}, a box, sides 41a, 21a, small, fixed by M. One component. Joined.

5. **Both core forms at 20a (note 278-299; I 53783, 63870-63871, 63887, 78969, 93532).** CONFIRMED.
   I 53783: Z''_i = (Omega_i^{~5})^c ∩ Z for h<i≤k_0. Omega contains the 3-cell gap, so E_5 acts on each 17-cube separately.
   Z''_{h+1} = [-7/2,7/2]^d u [33/2,47/2]x[-7/2,7/2]^{d-1} = N_3(Q_0 u Q_20). This also matches I 63871, Z''_{h+1} = (Z'_h)^{~3}.
   I 63887: Omega''_{h+1} = (Z''_{h+1})^c. So (Omega''^{~2})^c = E_2(Z'') = [-3/2,3/2]^d u [37/2,43/2]x[-3/2,3/2]^{d-1}.
   Form I 63870: (Z'_h)^~ = N_1(Q_0) u N_1(Q_20). The same two sets. Both lie inside C (side 21a_k ≫ 43a).
   Point 0: in the first cube. Point 20a e_1: first coordinate 20 ∈ [37/2,43/2]. Midpoint 10a e_1: 10 ∉ [-3/2,3/2] u [37/2,43/2].
   A box containing two points contains their midpoint. So C_C is not a box. Gap 37/2 - 3/2 = 17 cells.
   This is robust: if the two layers in I 78969 were native cubes instead of boxing cells, the 7a-cubes still erode to two separated cubes.

6. **Later steps (note 240-250).** CONFIRMED.
   61/2 < L/2 since L ≥ 103. So the joined box is strictly inside the central level-(h+2) cell. (11) follows by induction (21 < L).

7. **Section 4, preparation (note 304-385).** CONFIRMED.
   - Z''_{h+1} ⊃ Z_h: each Y_r has half-side 21a/(2L) < 7a/2. Margin (7-21/L)a/2 > a/R. Correct.
   - Lower nesting: Z''_{h+2} = [-7La/2,7La/2]^d ⊃ [-7a/2,47a/2]. Gap (7L-47)a/2 > La ⟺ 5L > 47. Correct.
   - Later lower gaps 7(1-1/L)a_i/2 > a_i. Correct.
   - Upper (14): Z''_k = Q_*^{[3u_k]}, side 7u_k; Λ_C side 9u_k; Λ̃_C side 11u_k. dist = (21R-11)/2 ≥ 9R ⟺ 3R ≥ 11. Correct. 11 ≤ 112.
   - Upper gaps: (L-2)u_k/(L-1) > u_k/L; (3-7/L)u_k/2 > u_k ⟺ L > 7. Correct.
   - With N = R, k_0 - h = R - p - 1 ≥ 101, so the case k_0 = h+1 (note 344-345) does not occur. Harmless.
   - Strips: half-side 21a_h/2 + q_h u_h = (22R-1)u_h/2 < 11a_h. Distance to the core exterior ≥ 3a/2 - 11a/L > a ≥ (R+1)u_h/2 (L > 22). Correct.
   - Moat N_1(Q)\Q lies outside Z_h and inside Z''_{h+1}. Zone h by I 63879-63892. Correct.
   - Y^♯ ⊂ Z''_{h+1} ⊂ Z''_k (47a/2 < 7u_k/2). Touching cubes lie in Λ_C. Correct.
   - Side bound: span 23a = 23LR level-h units ≤ 104LŘ_{h+1}. Correct.

8. **Later no-joining conditions (note 407-415; I 115866, 118394, 125168, 143731, 85716-85718, 91947).** CONFIRMED.
   I 115866: "We assume moreover the following nesting condition: during the N steps ... no components are joined inside Z". Section 4.26.
   I 125168: "we assume throughout the nesting condition". I 143731: hypothesis "(a) The component C satisfies the nesting condition".
   None is in Def 4.14 (I 45984-46031), Def 4.22 (I 85575-85716) or the proof I 63772-63935. I searched these ranges for "join" and "nest".
   I 85716-85718 is a route remark: hypotheses "are to be derived from the property (ii) ... together with the nesting of the large-field regions".
   I 91947 uses "nesting" for inclusion Z_{j'+1} ⊂ Z_{k-1}. The note's reading is fair. It is still a reading; a reader could take 85717 to mean the no-joining condition. Then the remark's route would need that added premise. The counterexample is unaffected.
   Side note, not a defect: I 96299 lists "The nesting condition" as a hypothesis of the oscillation theorem (4.23). It is also a later section.

## Change before outward use

- Note (7): replace "N_0 = p+1 < N ≤ R" by "N = R" (the waiting depth N_k = Ř_k, I 49762), and cite I 49785-49800.
  Or keep N and move the creations to b = h - R.
