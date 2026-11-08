# Check: library/out-live.md (1252 lines) and library/out-live-issue.md (19 lines), combined version

Claude (Opus 5.5), 2026-11-08. One faithfulness check of the outward text. Codex gpt-6-astra wrote both files. This is a second Claude reading, not an independent model, and not an audit.
Clone head `b7000edcd`. Sources: CA-I and SA at 31a47c543775, N (YM4_1400.tex) at 2bc0658f91d2d03ba44e20bf695067e0a56a2ed9. All three local copies are byte-identical to the raw GitHub files at those commits (cmp). Line anchors in the links therefore resolve to the cited lines.

## Verdict: FIX

The mathematics is the checked mathematics. The counterexample is the repaired one (20a, N = R, both core forms). The proof under the outlines' rule contains the I 78969 paragraph. The repair claims and "endpoint only does not suffice" are true. YM4_1400 already has the rule.
Before posting: one wrong line citation (finding 3), one imprecise citation (finding 4), the issue text (findings 6-9), and math delimiters that GitHub does not render (finding 10). No finding changes a bound or the counterexample.

## Findings

1. **Mathematics matches the checked notes. CONFIRMED.**
   I diffed each section after normalising Ř to R, removing links, and mapping "CA-I" to "I".
   - Note §§2-6 (88-503) against geoh-live-ab.md §§2-6: only wording ("your", "Bałaban's T rule in your eight-layer form", "port" removed). No equation changed.
   - Note §7 (504-815) against live-fgi.md §§3-5: tags renamed (C7)-(C17); one paragraph of options removed; no equation changed. (C7) has N = R (live-fgi-recheck finding 2). (C8) has Y_1 = 20a e_1 + Y_0. (C12) computes both forms. Note 805-809 keeps the 6a comparison.
   - Note §8 (816-1209) against live-nj.md §§1-7 (after the live-nj-fix commit): tags renamed (J1)-(J17); only wording changed.
   - The repairs of live-nj-check are present: finding 6 (the I 78969 form) at note 1038-1049; finding 5 (other components of Z_h) at note 1033-1035; the SA 17433 citation at note 881.
   - I checked the 1038-1049 paragraph by hand. D_{h+1} = H^{[3a]} lies at distance at least 7a from C^c. So inside C, two layers added to Ω'' = (Z''_{h+1})^c remove two layers from the grid box H^{[3a]}. The result is H^{[a]}, the same box as (J10). Correct.
   - New sentences outside the checked text: note 539 "Set k_0 = k − N_0" matches I 53766 ("with k_0:=k-N_0"). Note 519 (hull = meeting cubes) matches I 50046-50054. Note 516 cites I 63883 for Ω''_{h+1} = (Z''_{h+1})^c; correct.
   - I also checked the closed-endpoint variant (note 769-776) by hand. It is not explicitly confirmed in either live-fgi check. With births at m = h − 1: for m < t < k, t ≤ k − 1 = m + N, so the mark lies in [t − N, t) and bars every intervening operation. At k the window [h, k) = [m+1, k) does not contain m. The step h−1 → h gives the two 21a_h boxes of (C8), so (C9)-(C16) are unchanged. Correct.

2. **Claims about their text. CONFIRMED, except findings 3-4.**
   - I 85575: "Geometry and counting of live large-field regions. Proof outstanding". I 85598: "The following statements are used in this chapter as hypotheses." I 85600: "\emph{Geometric hypotheses.}". I 85629: "The set C_C is a box, …". I 85644: contour hypothesis. I 85650: cell hypothesis.
   - I 78969: "C_C:=(Ω''^{~2}_{h+1})^c ∩ C = Z'^{~}_h ∩ C". I 93532 gives the first form only. I 63870-63871: "C_C=(Z'_h)^~∩C. This is a rectangular parallelepiped contained in Z''_{h+1}=(Z'_h)^{~3}". I 63871-63872: "By Bałaban's condition (ii), Z_h∩C lies in a cube of side 100Ř_h".
   - I 45985-46001: the class, with (ii-b) window (k−N_k, k). I 46024-46026: the window comparison. I 49762-49765: N_k := Ř_k. I 53766: k_0 := k − N_0. I 53783: Z''_i = (Ω_i^{~5})^c ∩ Z for h < i ≤ k_0.
   - I 115866 ("We assume moreover the following nesting condition: … no components are joined inside Z"), I 118394, I 118402 ("… forbids the creation of new large-field regions but not the joining of components"), I 125168, I 143731 (hypothesis (a)), I 85716-85718 and I 91947: all quoted accurately.
   - SA 17433 ("Islands and drop-outs are the marked components"), SA 17440 ("Marks wait … s<t_♭"), SA 17575 and N 63684 (identical text: "single component", "does not absorb a second component", "the lower end point included", "a joining does not count as a creation"), SA 17583 (nonwrapping), N 73101-73110 ("quarantine … including its lower endpoint", "single-box traces"): all accurate.
   - Bałaban: I 50227-50229 says the eight-layer display "is Bałaban's definition [(3.5)]{B-CMP119}, rewritten". The bibliography (CA-III 111546-111553) gives CMP 119 (1988) 243-285 and CMP 122 (1989) 175-202. In cmp122a.txt, §1 "The Basic Step of the Operation R" starts at line 96 and holds the prepared sequence ("separated by one layer", lines 190-197). So "CMP 122 (1989), pp. 175-202, §1, for preparation" (note 13) is right.

3. **Wrong line for the cutoff 100. FIX.**
   Note 1216: "with the explicit cutoff 100 from [N 63763–63764](…#L63763-L63764)". N 63763-63764 is "G_i=H_i^{[10a_i]}, \qquad G_k=X." The cutoff is N 63769-63770: "With the small-box cutoff of \(100\) cells per side, it has at most \(100\)." (also N 63828). live-nj-check finding 1 carried the same wrong line.
   Replace the link text and anchor with: `[N 63769–63770](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63769-L63770)`.

4. **Source of the Λ̃_C side. FIX (minor).**
   Note 724: "the definitions at [CA-I 53783–53804] give the centred boxes" for Z''_k, Λ_C and Λ̃_C. I 53782-53803 define Z''_k and Λ only. Λ̃_C, the one-layer enlargement of Λ_C, is defined at I 63799-63800. live-fgi.md (3) cited "I 53776–53804 and 63788–63835".
   Replace with: "In particular, the definitions at [CA-I 53776–53804](…#L53776-L53804) and [CA-I 63788–63800](…#L63788-L63800) give the centred boxes".

5. **Repair and "endpoint only". CONFIRMED, with one caveat for the issue (finding 8).**
   - Class placement at I 45984-46000: the example has C ∩ Z_h equal to two components. This fails rule 1 (one component at every h ≤ i ≤ k). It also fails rule 2 at h+1 (a second component is absorbed). In the open-endpoint example it also fails rule 3 (operations at h ∈ [h, k)). The variant with births at h−1 fails rules 1 and 2. So the rule excludes both histories, and §8 proves all clauses for every history the rule admits.
   - Hypothesis placement at I 85598-85600: the block then makes no claim for the example. But the account's operation still treats that component, so every later use of (a)-(i2) must supply the rule. Note 1241 says this. The issue does not (finding 8).
   - "Changing only the endpoint does not suffice": true (finding 1, last item).

6. **Counterexample sentence in the issue. FIX (clarity).**
   Issue 9: "Two old components, with centres \(20a\) apart, join without a creation; the waiting depth is \(N=R\). Both forms of your core give two \(3a\)-cubes containing \(0\) and \(20ae_1\), but missing \(10ae_1\)."
   Problems: a is undefined; "old components" does not say they are live second-class regions; "without a creation" needs its object; the class test is not stated; "two cubes containing 0 and 20ae_1" can be read as each cube containing both points.
   Replace issue 9 with:
   > The example has two live second-class regions, born at level $h$, with centres $20a$ apart. Here $a$ is the side of a level-$(h+1)$ boxing cell. The radii are constant, $\check R=L^p$, and the waiting depth is your $\mathsf N=\check R$. At step $h+1$ their components join into one small box, and no large-field region is created. At step $k=h+\mathsf N$ the joined component passes your conditions (i), (ii-a) and (ii-b). Both forms of your core, at CA-I 78969 and 63870, are then two cubes of side $3a$: one around $0$ and one around $20ae_1$. The midpoint $10ae_1$ is not in the core, so the core is not a box.

7. **Undefined labels in the issue. FIX.**
   The issue uses "CA-I", "SA" and "N" without defining them (issue 5, 11, 13). The note defines them (note 22-24); the issue does not.
   Replace the start of issue 5 with:
   > Your [live-region block in Part I of your complete account (CA-I below), lines 85575–85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85575-L85644) is headed "Proof outstanding".

   Finding 8 removes "SA" and "N" from issue 11.

8. **Repair paragraph and the outlines. FIX (precision; the issue must not suggest the outlines are wrong).**
   YM4_1400 already has the rule. N 63684 is N's only class definition ("Where it acts"), and SA 17575 is the same text. Both name the joining case: "Two small quiet boxes that join within the window form a small component without creation, yet its trace one scale lower has two components". N 73101-73110 repeats the single-box and closed-endpoint requirements for the dynamic class. So the counterexample concerns only CA-I Definition 4.14 (I 45985-46001). It is not a defect of either outline. N does not itself write out the proof of all clauses (out-live-check finding 2); §8 supplies that proof under N's rule.
   The present issue 11 does not say this, and its order and wording leave the hypothesis caveat out.
   Replace issue 11 with:
   > Your outlines already exclude this example. Their class rule, at [YM4_sketch_500.tex line 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) and [YM4_1400.tex line 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684), requires one small component at each level of the window, no joining, and quarantine including the lower endpoint. Both lines name the joining case. So the example concerns only the class of your complete account, at CA-I 45985–46001.
   >
   > The suggested repair is to add your outlines' rule to that class definition. This changes eligibility, and so the dynamic histories. Alternatively, state the rule as a hypothesis just before your geometric block, at CA-I 85598–85600. Then each later use of the block must supply the rule. Changing only the window $(h,k)$ to $[h,k)$ does not suffice: the same joining occurs with births at level $h-1$.

   Title: replace with "Your complete account's live-region geometry: a joining counterexample, and a proof under your outlines' rule".
   Optional, for the note: note 1213-1215 calls the hypothesis "the smallest textual repair" and lists it first. That is true, and 1239-1241 gives both caveats. No change needed. If changed, put the class option first to match the issue.

9. **Credit sentence in the issue. FIX (minor).**
   Issue 13: "Your account identifies the T rule at CA-I 50226; it cites CMP 119, §3, and CMP 122, §1." Line 50226 is `\end{equation}`; the sentence is 50227-50229. Volume 122 holds two Bałaban papers (175-202 and 355-392), so "CMP 122, §1" is ambiguous. Replace the last sentence of issue 13 with:
   > Your account says at CA-I 50227–50229 that the T rule is his definition, rewritten. It cites CMP 119 (1988), §3, for T, and CMP 122 (1989), pp. 175–202, §1, for the preparation.

   Credit otherwise: "your" throughout. Bałaban is credited for the method, the T rule and the preparation geometry (note 10-13; table 68-72; issue 13). No third-person credit to the readers. CONFIRMED.

10. **Math does not render on GitHub. FIX (mechanical).**
    I tested GitHub's renderer (`gh api markdown`, gfm). `\(m\le h\)` renders as plain "(m\le h)". `\[ … \]` renders as "[ … ]". `$m\le h$` and a ```` ```math ```` block render as math. The issue has `\(…\)` at lines 7 and 9. The note has 369 lines with `\(` and 57 display blocks `\[ … \]`. Earlier issues (for example #21) have the same defect.
    Convert inline `\(…\)` to `$…$`, and each display `\[ … \]` to a ```` ```math ```` fenced block (the `\tag{}` inside is fine). Do this in both files. The replacement texts in findings 6 and 8 already use `$…$`.

11. **Small wording. FIX (optional).**
    Note 15: "Your observation that no creation does not exclude joining" → "Your observation that the no-creation condition does not exclude joining".

12. **Earlier faithfulness fixes (gates/out-live-check.md). CONFIRMED, still hold.**
    Finding 4 credit: note 10-11 and issue 13 carry the replacement. Finding 5: no "separate question" or "revised operation" sentence remains. Finding 6: the old §8 process text is gone. Finding 7: "Bałaban's T rule in your eight-layer form" at note 68, 164, 1105; "Bałaban's" five-layer preparation, upper gap and nested members at note 70-72. Finding 8: no "port", "CA's" or "grants no status" remains. Finding 9: "your Lemma 4.21" at note 54 and 82. Finding 10: `@NOTE_LINK@` (issue 7) must still be filled.

13. **Scope, not-covered and internal text. CONFIRMED.**
    The table (note 36-52) and issue 7 match the three checks' tables: on the account's class, (a) for i ≥ m, (b)-(e), (h) and m ≤ h are proved; (g) box is false; (f), the rest of (g), (i1) and (i2) are not established in general. Under the rule, all are proved. Issue 15 and note 1239-1248 state what is not covered: contour, cell and summation hypotheses; positive field support; a Yang-Mills theorem; downstream waiting and rarity for the restricted class. Neither file has internal paths, row numbers, "lane", "gate", "port", "registry" or file names. The note link will be a repository URL, which is fine.
    Issue 17 ("Claude (Opus 5.5) checked each proof line by line, and its repairs are applied") is accurate: the repairs of geoh-live-ab-check, live-fgi-check, live-fgi-recheck and live-nj-check are in the note. The I 78969 paragraph had no separate recheck; this check verified it (finding 1).

## Who checked what

Claude (Opus 5.5) checked both files line by line against: CA-I 45984-46032, 49760-49766, 49785-49800, 50046-50056, 50224-50230, 51178-51189, 53755-53819, 63683-63693, 63786-63800, 63866-63892, 78966-78971, 85575-85650, 85716-85718, 91947, 93530-93534, 115866, 118394, 118402, 125168, 143731; CA-III 111546-111553; SA 17433, 17440, 17575, 17583; N 63684, 63744-63775, 73101-73110; cmp122a.txt lines 1-30, 96, 190-197. Section diffs were done against geoh-live-ab.md, live-fgi.md and live-nj.md at `b7000edcd`. GitHub rendering was tested with `gh api markdown`. Codex wrote the note and the issue.
Incidental, not part of this check: issue #21 on their repository is open with no comments or labels as of this reading. The owner's engagement check still applies before posting.
