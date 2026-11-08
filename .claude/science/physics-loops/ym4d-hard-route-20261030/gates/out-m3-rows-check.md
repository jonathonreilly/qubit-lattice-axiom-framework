1 MISMATCH / 0 UNCLEAR (plus two short-range citations, both cosmetic)

# Reading check: out-m3.md §6.3, the remaining rows

Checker: Claude (Opus 5.5), one line-by-line reading of the authors' text.
Source: CA-I, CA-II at `31a47c543775`, local copies in `/Users/jonreilly/ym4d-lead/sa/`.
Note: `library/out-m3.md`, §6.3 table, lines 1179–1198.
This is one reading check. It does not judge the layer premises or re-review the main proof.

I read every cited range in full. I also read enough nearby text to see the definitions.
Extra lines read for context: CA-I 112040–112071, 112110–112180, 112560–112586, 112626–112707,
115370–115388, 19758–19772, 72700–72753; CA-II 585–609, 629–640, 20760–20793,
21110–21124, 21940–21949, 22081–22082, 23145–23159, 23980–23992, 14106–14110.

## Row: CA-I 112072–112104; 112181–112194 — MATCH

At (T) the cut acts on the datum: "A'↦A'+t_□δA', X↦X+t_□δX" (112076).
Lemma current-partner applies to these layers. That is (18) on a datum-affine family, as in §5.1.
At (L)-far the layer is the field cut χH_s, χ = t + 𝗍χ̂_□, with partner 𝒥^♯[χ] (112084–112090). That is (19).
The proof splits the four entries (112181–112189).
For entry 3 it says "The third identity holds because P_1(σ) is linear" (112190).
That is the split (38).
For entry 4 it says "χ multiplies from outside m_H(σ)" (112190–112191).
(19) keeps χ outside m_H(s). The row is correct.
Range: correct. 112072–112104 runs from the layer list to `eq-increment-bound-3`.
112181–112194 is the decomposition paragraph.

## Row: CA-I 112708–112738; 115389–115407 — MATCH

At 112708–112718 the P_1-tail works "on the disc |𝗍| ≤ ρ_A = 𝗐_L/η_p^{1/2}".
It multiplies the product bound `eq-depth-hypothesis-3` by |𝗍|.
That is "the same product bound on the enlarged amplitude disc". This is the retained (L) profile premise of the previous row.
Entries 1, 2 and 4 "are taken from assumption (F), not derived from (e2)" (112733–112734).
So the local cut entries are supplied stencil bounds, as the row says.
At 115395–115403 the five entries include the P_1 tail in product form.
They "are read after the bound (e3)^+" (115403).
Wording remark, not a defect: in the remark (112560–112740), (e3)^+ is *established* in (i) from (A)–(E).
It is not assumed there. In the theorem list (115387–115388) it is an assumption of the increment lemma.
"Assumed" is right for the second range only. A possible wording: "after (e3)^+, supplied by (A)–(E)".
Range: 112738 ends in mid-sentence. The paragraph ends at 112740. Correct range: 112708–112740. Cosmetic.

## Row: CA-II 610–628 — MISMATCH (table only)

What their text says. Reading (q) states that the profile quantities majorise the four entries.
These are N^Δ_y(A'), N_y(ℍ), ℓ³|P_1(σ)A'| and ℓ³|𝔪_H(σ)X| (611–613).
At (L) the 𝐉-entries use `5.2:eq-three-sites-c` (624–627).
The sentence then continues past 628. The t-member of the third entry must be
"at most 20K_χ|𝗍|q_□(y)" (628–629), with
q_□(y) := sup_{y'⊂□^ζ} p_s(y') e^{−2δ_P d_{𝔅_s}(y,y')} (633).

What the table claims. "Equations (7), (32) and (37) give the required operator contributions."

The defect. (37) as stated in §6.1 is read at the source profile p = p_s. There it gives
C·B·p_s(y)e^{−δ_P d(y,□^ζ)}. That is the *middle* member of `eq-three-sites-c`.
By that display q_□(y) ≤ p_s(y)e^{−δ_P d(y,□^ζ)}. So (37) at p_s is weaker than the q_□ form this consumer states.
(7) and (32) do not close the gap. (7) is a weight-to-weight bound. (32) is the use of the four entries, not a bound on them.
The cited range also stops in mid-sentence at 628. So it leaves out the clause that fails.

Smallest fix.
1. Change the range to CA-II 610–633. This takes in the t-member clause and the definitions of p_s and q_□.
2. Replace "(37)" in the row by a sentence like this: "(37) read at the weight q_□ itself gives the 𝗍-member ≤ C|𝗍|q_□(y). The weight has rate 2δ_P ≤ λ, the extra decay rate is zero, and the proof uses only the cut clause of (36). Read at p_s, (37) gives only the middle member of `eq-three-sites-c`."
The proof of (37) uses only the second clause of (36) and the weight ratio. The weight q_□ satisfies p(z) ≥ p_s(z) on S and has rate 2δ_P. So (37) gives this form with no new estimate.
The metric comparison d vs d_{𝔅_s} stays a named profile premise, as §6.1 already says.
Effect: the table and §6.1 wording only. The theorem, bounds (7) and (27) do not change.

## Row: CA-II 20794–20828; 21125–21144 — MATCH

(c2) writes the cut current as (19), with D^*D = D_1^TD_1 and 𝖪 = K_W (20798–20800).
It says the current "has exactly one member non-local in χ, namely −P_1(σ_s)(χA'_s)" (20806).
It also says this member is linear in χ. That is §6.1 and (38).
The tail bound (20823–20825) and its repeat at 21135–21138 is
20K_P B_♯ p_s(y')e^{−δ_P d(y',□^ζ)} ≤ … 𝖺_s e^{−δ_P d^∧(y',𝔉)} e^{−δ_P d(y',□^ζ)}.
The text adds "not a minimum" (20827–20828). This is exactly (37) at p = p_s, S = □^ζ.
§6.1 also keeps both factors and does not take a minimum.
The condition η_p ≥ e^{−2δ_P d(□^ζ,S_v)} (21128) belongs to their receding-block lemma. It stays a retained input.
Range: correct.

## Row: CA-II 21950–22080 — MATCH

Hypothesis (b) asks that the kernels of P_1(σ_s), H(σ_s), 𝔪_H(σ_s) "vanish unless both arguments lie in one component" (21970–21971).
It asks this for every subfamily σ_0 (21954, 21958–21959). §4.3 gives it for P_1 and 𝔪_H.
Their Y(σ_s) is the never-cut set ∪ Λ^∼ ∪ ⋃𝗒 (21960–21962). This set keeps the hubs and the never-cut cells.
The note's Y(s) keeps only cubes with s_Δ ≠ 0. That set is a subset of theirs. So locality in the note's Y(s) gives locality in theirs.
Hypothesis (d) and the split at 22061–22066 give "both summands ... restricted to S_v ... vanish".
That is the §6.2 sentence on (38).
Remark: the kernel locality of H(σ_s) and hypothesis (a) come from the layer input (input 5), not from §4.3.
The row does not say this, but the table preamble keeps the layer inputs.
Range: the proof ends at 22082. Correct range: 21950–22082. Cosmetic.

## Row: CA-II 23160–23169; 23993–24005 — MATCH

The boundary-term pieces use Φ_s^χ = (e^{iηχℍ_s}W_s, J_s + 𝒥^♯_s[χ]) (23167).
Here 𝒥^♯_s[χ] is "the current of the dilated layer χℍ_s" (23169). That is (19).
The core carrier pair is (∏_s e^{iηℍ_s}𝕌, 𝐉 + Σ𝔰^♯) (23995). It sums the partner currents (18) of the brackets.
This matches §6.2: "your sums of the individual furnished riders".
Range: correct. The sentence at 24005 ends at 24006, which is harmless.

## Row: Outside multiple, CA-II 13888–14105 — MATCH

The map is Φ_t = (e^{iηχ_tℍ}𝕌, 𝕁 + χ_t 𝒥^♯[1]) (13986). That is the outside multiple, not (19).
Entry three uses hypothesis (c) only at χ ≡ 1: "We apply hypothesis (c) at χ≡1" (14076).
It then multiplies by |χ_t| ≤ a(y) (14082–14090). That is "uncut bounds times multiplier bounds".
Holomorphy uses (a) at χ ≡ 1 for the current (14100). Locality uses "the product χ_t·𝒥^♯[1]" (14102). The row matches both.
Remark: hypotheses (a) and (c) (13950, 13956–13959) are stated for general χ, that is, for the cut current (19).
The proof uses them only at χ ≡ 1, where (19) equals (18). The note proves (32)–(33) only for χ = t + 𝗍χ̂_□.
So a reader who takes (a) and (c) literally, for general χ, does not find them in the note.
A possible clarification for the row: "(a) and (c) are consumed only at χ ≡ 1, where (19) = (18)."
Conclusion (iv) at b = 0 uses the zero-datum property (input 5) and F(W,0) = 0, as in §5.2.
Range: correct for the object. The radius step runs on to about 14112 and does not bear on the current.

## Row: Older chart formulations, CA-I 19637–19685; 29381–29412 — MATCH

Both ranges define Φ^𝕂 with the native chart current 𝔍(B(t),t_□) (19643–19648, 29386–29387).
(F5) says "The same statements hold for the functions localised in the decoupling parameters" (19684).
That is their own K10 assertion away from one. The row leaves it as defined. That is correct.
At 29389–29390, P_1 is "the operator as they occur in [CMP109 (3.13)–(3.14)]". This is the native operator, not the note's P_1(s).
Wording remark: 19771–19772 shows that 𝔍(B,t_□) − 𝔍(B) − t_□δ𝔍[v] is a second-order Taylor remainder.
So 𝔍(B(t),t_□) is the chart current along an affine *datum* path. It is not a field-affine family as in §5.1.
The identification this row needs is §5.3's first paragraph: pointwise in the datum at one, for each admitted datum on the path.
§5.3's explicit affine statement is on K6's domain only. A clearer row would say "§5.3 identifies the current at each admitted datum, hence along B(t) + t_□v and in its first variation".
This is a precision fix. It is not a change of argument.
Range: correct.

## Partly read rows: the new parts

### CA-I 72754–72783 (row "72754–72783; 72823–72860") — MATCH

Readers at amplitude one read the triple 𝒜(𝗌) = (𝒴, 𝒥[𝒴], 𝗎) (72757–72758).
On a component C it is a function of the restrictions. It also satisfies "𝒜(𝗌)↾C=(0,0,1) if b↾C=0" (72766).
§5.2 proves both, with the gauge-map input.
The holomorphy property (72769–72783) asks for holomorphy and the bound 𝔑(F) on a product polydisc.
§6.2 gives holomorphy by substitution. It keeps the reader bounds and the admission of intermediate images as inputs. The row matches.
Range: correct.

### CA-I 111410–111486 (row "111391–111486") — MATCH

The proof says "Both data are taken at the same kernel (𝒲,σ)" (111421).
It subtracts and bounds five terms. The constant is K_𝗃 = 3+18d+9K_J (111415, 111477–111478).
This is (31) then (32). The P_1 and 𝔪_H terms are entries of 𝖭_y(δ) (111442–111443). (7) feeds those entries from the layer response bounds.
The 𝖪 line writes N_y(δℍ) (111438). §5.2 already notes this and uses N_y(δA'). The constant does not change.
Range: correct.

### CA-I 111512–111530 and 111550–111580 (row "111512–111580") — MATCH

The cut current `eq-cut-layer-partner-1` (111542–111543) is (19) word for word.
χ stays outside 𝔪_H(σ). The lift H(σ)X is unchanged in the commutator.
c_ζ := 2c_d with c_d := (2+4τ)(d−1) (111557). This equals (33)'s c_ζ = 2(2+4ϑ)(d−1).
The bound (111548–111552) uses K_𝗃 and c_ζ as the row says.
Their cutoff asks |ζ''| ≤ 5 (111527). Input 6 replaces this by |ζ''| ≤ 42 and keeps c_ζ. The row's "cutoff of input 6" is consistent with this.
Range: correct.

### CA-I 112587–112608 (row "112587–112625") — MATCH

(F) at (T) uses the layer Lipschitz bound for five weighted norms. These include
"‖P_1(σ)(A'_1−A'_2)‖_p, ‖𝔪_H(σ)(X_1−X_2)‖_p" (112596).
The weights are e^{−δd^∧(·,Ω)} and e^{−δ dist(·,□)} (112610–112613).
(7) at these weights, with the layer's ‖δA'‖_p and |δX|_p, gives the two operator norms. This holds if the weights are admitted in the note's sense (rate ≤ λ, with metric comparison). The row says "admitted weighted differences", so this is retained.
At (L) the product form `eq-depth-hypothesis-3` (112622–112625) is a distinct premise, as the row says.
Range: correct. 112587 is the start of (F). 112625 is the end of the product display.

## Summary

- One MISMATCH: CA-II 610–628. The consumer asks for the 𝗍-member of entry 3 to be ≤ 20K_χ|𝗍|q_□(y). (37) read at p_s gives only the weaker middle member of `eq-three-sites-c`. The range also stops before that clause.
  Fix: cite 610–633, and read (37) at the weight q_□ (rate 2δ_P ≤ λ, extra decay zero, only the cut clause of (36)). Table and §6.1 wording only; the theorem is unaffected.
- Range nits: 112708–112738 should be 112708–112740. 21950–22080 should be 21950–22082.
- Wording remarks with no change of argument: "assumed (e3)^+" (row 112708); χ ≡ 1 use of (a) and (c) (outside-multiple row); "datum-affine continuation" means an affine datum path (older-chart row).
