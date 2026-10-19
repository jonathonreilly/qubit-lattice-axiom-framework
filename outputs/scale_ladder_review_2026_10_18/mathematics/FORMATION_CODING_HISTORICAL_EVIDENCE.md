# Historical submitted evidence and bibliographic assertions

Preserved for retrieval only; no fresh execution or independent theorem validation is implied. The corrected live argument is in the sibling mathematical file.

## 8. Runner evidence (finite Monte Carlo, not proof)

`python3 runner_formation_coding_radius.py` (full run, seed 20261018). The log is `runner_full.log`.

Result: **TOTAL PASS=22 FAIL=0** in 74 s.

The checks fall into five groups.

- **A. Path counts.** The enumerated self-avoiding-walk counts c₀…c₉ on Z³ equal OEIS A001412, an expected constant that is independent of this code. They also satisfy c_n ≤ 6·5^(n−1).
- **B. Decreasing paths, infinite volume.** 120 000 lazily sampled infinite-volume fields:
  - The mean number of decreasing paths of length n matches c_n/(n+1)! for n = 1…9, with |z| ≤ 0.91. This is an exact identity.
  - P(L ≥ n) is 0.0403, 0.0078 and 3.0·10⁻⁴ at n = 10, 12 and 15. The bound c_n/(n+1)! gives 0.232, 0.037 and 1.4·10⁻³.
  - The lower bound 1/(n+1)! holds.
  - The radius of K is at most L + 1 in every sample.
- **C. Two-copy intersection probability.** It is 0.137, 4.9·10⁻³ and 7.8·10⁻⁵ at d = 6, 9 and 12. The analytic Γ(d) is valid but vacuous below d = 22. The ball form drops below 1/4 from d = 21.
- **D. 32³ torus, three rules** (native (3,1,2), ferro (20,1,1), copy-unanimous):
  - X_x is unchanged after resampling all noise outside K_x, and after resampling outside B(x, L_x + 1). Each test recomputes the whole field: 10 trials per test, two rules. The control, which resamples inside K_x, changes X_x in 3/10 and 2/10 trials.
  - The tail of L(x) is rule-independent and below the bound.
  - The empirical C(d), for example ferro: C(1) = 0.138, C(3) = 0.009, C(5) = 4·10⁻⁴, satisfies |C(d)| ≤ 2·P_bad(d). Where resolved, the ratio is at most 0.07.
- **E. Fixed +x slab, ferro rule.** ⟨v_x⟩ = 0.886, 0.264, 0.048 and 0.002 at h = 1, 2, 3 and 4. This is within 2·P(K meets slab) + 4 SE. Beyond h ≈ 6 the check is noise-limited (SE ≈ 0.007, largest excursion 2.2 SE at h = 10).

The runner checks lemmas and finite instances. It does not prove the infinite-volume theorems.

## 9. Prior art and actual contribution

- **Known.** Lemma 1 is Harris (1972) and Liggett (1985, graphical construction), Penrose–Sudbury (2005, deposition), and the random-ranking local algorithms of Nguyen–Onak (2008). The ffiid language and coding radius come from Holroyd–Schramm–Wilson (Ann. Probab. 2017). The independent-copy / stopping-set coupling is standard: van den Berg–Steif (Ann. Probab. 27, 1999), Spinka (Ann. Probab. 2020), Harel–Spinka (2022). These citations are recalled. The HSW and van den Berg–Steif abstracts were checked by web search in this session; the other bibliographic details were not.
- **New here (packaging, not new probability).**
  - The exact formation class of the repo is placed under the theorem with rule-independence made explicit: order-sensitive, clock-reading, zeros, holes.
  - Explicit Z³ constants are given for the coding tail, for both covariance forms and for start-slice forgetting.
  - The pinch-point, symmetry-breaking and 3-colouring exclusions are stated as quantified corollaries.
  - The evasion routes are separated precisely.

## 10. No-Go Discipline Gate (brief)

- **N1.** The routes to evade are listed in §7 (seven items). Each is a scope boundary, not a closed physical family.
- **N2.** The exclusion is proved only for Definition 1. Nothing is claimed about the framework as a whole.
- **N3.** The supplied premises are iid atomless clocks, independent marks, a deterministic start slice and finite degree. No physical selection of these is made.
- **N4.** The 3-colouring corollary rests on a cited external theorem. The ice exclusion is limited to pinch points.
- **N5–N8.** The infinite-volume statements are analytic. The runner checks finite instances only. The bound constants are not tuned to data.
