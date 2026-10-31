# h4 criteria (written before h4_threshold.py): threshold arithmetic — HIST.md §3, §7.4 (informational)

Informational table, [inference] wherever a one-loop rate is used. For N ∈ {2, 3}, ε_1 ∈ {0.25, 0.5, 1}, κ = 1, L = 3,
d = 4: η_1 (RLARGE RS) and η_q (RS-lin); a_η := η²/(2N) at each (the bare Wilson value, as RLARGE §7.1); the kernel exponents
κε_1²/(256N), κε_1²/(1024N); a_RS (RLARGE, c_RS = 625) and a'_RS (this file, c_RS = 81); with a one-loop β_- := 11N/(24π²)·2N
(Balaban normalisation as RLARGE §9 C) [inference]: n_♯ := ⌊4/(aβ_-)⌋ and n_H := ⌊(4 + 38416B_0/log L)/(aβ_-)⌋ for
B_0 ∈ {0, 0.1, 1}, with a := min{a'', a_RS} (a'' := 0.9ε_1²/(4N)).
- **I1 (consistency, the only criterion).** n_H(B_0 = 0) = n_♯ and n_H is nondecreasing in B_0 in every row. PASS iff so.
- Everything else printed, not judged.
