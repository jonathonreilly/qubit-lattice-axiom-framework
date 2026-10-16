# Sampled coupling milestone

The standalone source derives a six-sample clamped-pulse inverse, relative coupling shapes and the common-potential shape/sign condition. The sampled recurrence is calibrated on separate histories; it leaves continuous frequencies and hidden initial states unselected. No empirical dataset was used.

Primary scripts/sampled_coupling_inverse.py imports scripts/sampled_coupling_math.py. The cache is logs/runner-cache/sampled_coupling_inverse.txt. Scratch mutation controls and focused source checks live under outputs/sampled_coupling/. A real sensitivity-term failure was corrected before integration; integration failures are preserved in AUTHOR_CORRECTIONS.md.

Final canonical source review is complete:44primary controls,135independent assertions and21detected scratch mutations. Citation discovery adds exactly one node with the intended primary/helper, with zero rewiring. Final historical-cache packaging is lossless; see HISTORICAL_CACHE_STORAGE.json and the independent storage addendum. Next: commit/push this standalone branch and attach its milestone PR. Full integrated landing validation remains pending. Do not merge, apply audit verdicts or push main. Then continue personally on the actual source/coordinate/actuator bridge in the existing campaign; its22:36:59Zdeadline is unchanged.
