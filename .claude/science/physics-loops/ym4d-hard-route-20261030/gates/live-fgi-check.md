# Check of library/live-fgi.md

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading. Not an audit.
Note at clone `aa33ce362`. Sources: CA-I raw (I), YM4_sketch_500 (SA), YM4_1400 (N), local copies.

## Verdict: FIX

The mechanism is right. The class admits a joining. The box claim for the core is false on the account's class.
But the written example (centre separation 6a) is not a counterexample under the account's own definition of the core.
That definition is I 78969 (the `:=` form, also I 93532): C_C := (Ω''^{~2}_{h+1})^c ∩ C.
In the note's example this set is the box [-3a/2,15a/2]×[-3a/2,3a/2]^{d-1}. It contains the midpoint 3a e_1.
The note uses only the second form, (Z'_h)^~ ∩ C, which is what I 63870 says.
A one-number repair works: put Y_1 at centre separation s·a with 18 ≤ s ≤ 21, for example 20a.
Then both forms give two 3a-cubes, and every class test still passes (finding 3).
The same example also shows that the identity printed at I 78969 fails under joining (s = 6).

## Findings

1. **Class rules (note 47-51, 236-245; I 45984-46000).** CONFIRMED.
   Rules quoted and tested on the example (both s = 6 and s = 20):
   - (i) "X is contained in a cube of size 100MR_k". C = Z_k has side 21 a_k. Passes.
   - (ii-a), first clause: "no new large-field region created by one of the operations T_{j→j+1}, h≤j≤k-1". All these creation sets are empty. Passes.
   - (ii-a), second clause: "every previous region contained in X satisfies (i) on its own scale". Y_0, Y_1 have side 21 a_h; Z_{h+1}∩C has sides ≤ 41a; later Z_j∩C have side 21 a_j. Passes per region.
   - (ii-b): excludes components of the class of an operation at level k' ∈ (k-N, k) that introduced a large field. The only such operation is at k' = h, outside the open window. Passes.
   - Waiting rule (I 51178-51189): a creation in W^_s inside C needs k - s ≥ N. Creation at s = b = h-N; operation at h. Passes at h, blocks b ≤ t < h. Matches note 187-189.
   - Admissible geometry fact (1) (I 63547-63551): components of Λ^c are boxes of 1..100 cells, at distance ≥ Ř. All components in the history are such boxes. Passes.
   - Second-class rule (I 64479-64495): the whole component takes the class and keeps the flat level-t label. Matches note 174.
   The account itself supports the per-component reading: I 118402, "bounds each previous component but not their number, and the first clause forbids the creation ... but not the joining of components".
   It also reads (ii) at levels h+1..k as a bound on Z_j∩Z (I 55350, 55400). The example passes that reading too: Z_{h+1}∩C is one small box.
   I 55350-55354 and 55418 also admit retained regions of an operation at s = h inside Z. Note 174-189 matches.
   The example fails only the reading "Z_h∩C lies in one 100 a_h cube". That reading appears only in the sentence under attack (I 63871-63872).

2. **Configuration (9)-(12) (note 192-265).** CONFIRMED arithmetic; MISMATCH on "as the account defines it".
   Step rules: with empty P', Q', R', I 50214-50229 give Ω^c = Ŷ^{~8}; I 50346-50372 give Z = M(Ŷ^{~10}). Here Y = Z_h (I 50163). Ŷ is the P_{h+1}-hull (I 50046-50054); Z'_{t-1} is the same hull (I 59496-59499). (9), (10) and (11) are correct.
   (12) equals N_1(Q_0∪Q_6): two cubes with a gap of 3a; the midpoint argument is correct.
   But the core's definition in this chapter is I 78969: "C_C := (Ω''^{~2}_{h+1})^c ∩ C = Z'^~_h ∩ C". I 93532 gives the first form only.
   Z''_{h+1} = (Ω^{~5}_{h+1})^c ∩ Z (I 53783) is the box (13), and Ω''_{h+1} = (Z''_{h+1})^c (I 63887). So the `:=` form is (13) eroded by two layers: [-3a/2,15a/2]×[-3a/2,3a/2]^{d-1}. That is a box.
   The note never mentions I 78969 or I 93532. Its line 89-92 cites I 63868-63892 only.
   Repair, checked by hand with s = 20 (units of a = a_{h+1}):
   - Hull Q_0 ∪ Q_20. Ω^c_{h+1} = N_8: [-17/2,17/2]^d and [23/2,57/2]×[-17/2,17/2]^{d-1}, gap 3a, two components.
   - N_10: [-21/2,21/2] and [19/2,61/2] overlap. Z_{h+1} = [-21/2,61/2]×[-21/2,21/2]^{d-1}, sides 41a and 21a, small, fixed by boxing. The components have joined.
   - Z''_{h+1} = two 7a-cubes = N_3(hull). C_C by either form = [-3/2,3/2]^d ∪ [37/2,43/2]×[-3/2,3/2]^{d-1}.
   - 0 and 20a e_1 lie in C_C; 10a e_1 does not. Not a box.
   - Step h+2: largest coordinate 61a/2 < La/2 since L ≥ 103. Then (11) holds as written.
   - The side bound still holds: extent 23a ≤ 104 L Ř_{h+1} level-h units.
   Any 18 ≤ s ≤ 21 works: s ≥ 18 keeps Ω^c_{h+1} split; s ≤ 21 makes Z_{h+1} touch-connected.
   Section 4's remark (13), "a single box", becomes two 7a-cubes. The author should recheck 266-307 for the new s; (15)-(16) are unchanged because the region is one centred cube from h+2 on.

3. **I 63870-63872 (note 360-362).** CONFIRMED with a small citation fix.
   I 63870: "C_C=(Z'_h)^~ ∩ C. This is a rectangular parallelepiped contained in" I 63871: "Z''_{h+1}=(Z'_h)^{~3}."
   I 63871-63872: "By Ba{\l}aban's condition (ii), Z_h∩C lies in a cube of side 100Ř_h."
   With s = 20 the box sentence is false under both core forms. The 63872 sentence is false in the example, not only unsupported: Z_h∩C spans (20L+21) a_h > 100 a_h.
   The note should add that I 78969 asserts an identity that fails for s = 6. Note 265 cites "I 85628"; the box sentence of (g) is I 85629.

4. **Outline rules (note 50, 355-358).** CONFIRMED.
   SA 17575 and N 63684 are the same text: "for k_♭≤i≤k the set X∩Z_i is a single component of Z_i and is small", "it does not absorb a second component, X∩Z_i=Φ_i(X∩Z_{i-1})". They add: "a joining does not count as a creation".
   Z_h∩C has two components, so both examples are excluded.
   Under that rule the box claim holds. Each Z_i∩C is one box H_i^{[10]} (N 63749-63834). The hull of a box is a box. So (Z'_h)^~∩C = H_{h+1}^{[1]} is a box. The erosion form gives the same box.

5. **Joining restrictions elsewhere in the account (note 47-51, 367-373).** CONFIRMED that none applies here; FIX for completeness.
   The account has its own no-joining "nesting condition": I 115866 ("during the N steps of this application no components are joined inside Z"), I 125168, I 143731, used at I 118394 and 143964.
   Each is an added assumption ("We assume moreover", "we assume throughout") in later sections. None is in Def 4.14 (the class), Def 4.22 (the hypotheses), or the proof at I 63772-63935.
   The route remark at I 85716-85718 says "the nesting of the large-field regions"; in this chapter that phrase means inclusion (I 91947).
   That condition would exclude both examples. The note should cite it beside SA/N. It should also cite I 118402, which states the joining gap in the account's own words.

6. **Clause table rows (f), (i1), (i2) (note 390, 394, 395).** CONFIRMED honest.
   (f): the account's proof uses Z_{k0+1}∩C and Z_{k0}∩C as one small set (I 63817-63833). So it has the same single-predecessor dependence. The row says conditional; that is accurate. Whether a later joining breaks (f) was not checked by the note or by me.
   (i1): I 63920 cites "clause (c′)", which is not stated in Def 4.22. Clause (c) gives 5/2 Ř_m in level-m units only. The row is accurate. Not checked: (d) rescaled gives dist_n ≥ 7Ř_{n-1}/L, a possible supplier.
   (i2): the vertex argument at note 127-130 is correct for closed axis-parallel boxes. Strips are closed boxes (I 63528). Sides ≥ Ř_m ≥ 38 follow from I 63549-63551 and 63621-63622, not from clause (a) as I 63930 says. The row is accurate.

## What to change before any outward use

- Replace 6a by 20a (or any s in 18..21) in (8), (9)-(13), and recheck section 4.
- State the core by I 78969 and show both forms agree in the new example.
- Cite I 118402, I 55350-55418, and the account's nesting condition (I 115866, 125168, 143731).
- Fix I 85628 → I 85629.
