# ol55_1 — criteria (written before the script; OSLEAF55, Opus 5.5 worker)

Purpose (scope stated honestly): three exact-arithmetic sanity checks of CONVENTIONS and ELEMENTARY CONSTANTS used in
OSLEAF55. None of them checks a Yang–Mills estimate. Plain python, fractions.Fraction only (complex numbers as pairs of
Fractions). No floats in any verdict.

## G1 — clover bound |ê_a| ≤ 24 a^{-4}
ROTDEF §2.2: e_a(x) := (4a⁴)⁻¹ Σ_{μ≠ν} Σ_{p ∈ clover_{μν}(x)} s(U_p), s ∈ [0, 2].
Enumerate unit plaquettes of Z⁴ having the origin as a corner.
PASS iff: (i) exactly 24 distinct unordered plaquettes have the origin as a corner; (ii) the ordered-pair clover sum has
exactly 48 terms (12 ordered pairs × 4); (iii) the maximum of a⁴e_a, (48·2)/4, equals 24 exactly.
Control X1 (must fire): the same enumeration in Z³ must NOT give 24 (it gives 12); FAIL of the gate if it gives 24.

## G2 — Taylor constant used in Proposition GROW
Claim: (2n)^{5n} ≤ ((5n)!)² for every integer n ≥ 1 (equivalently (2n)^{5n/2}/(5n)! ≤ 1).
PASS iff it holds (exact integers) for every n = 1, …, 100. (The all-n proof is analytic, in OSLEAF55 §3.)
Control X2 (must fire): the false variant (2n)^{5n} ≤ ((2n)!)² must fail for at least one n in 1..100.

## G3 — the OS reflection form equals ⟨Θ(A)^*A⟩ (conventions Θ, *, order reversal), and RP can fail
Toy model (NOT Yang–Mills): times t ∈ {−3,…,3}, a stationary 3-state Markov chain, real field φ = v(state) with
v = (1, 0, −1). Schwinger "functions" S_n(t_1..t_n) := E[Π φ(t_i)]. Test sequences F = (F_0, F_1, F_2, F_3), F_n complex
rational, supported on strictly ordered positive times 0 < t_1 < … < t_n ≤ 3.
Q_OS(F) := Σ_{n,m} Σ_{x,y} (ΘF_n^*)(x) F_m(y) S_{n+m}(x, y), with (ΘF^*)(x_1..x_n) := conj F(−x_n, …, −x_1).
Q_dir(F) := E[ conj(A(θφ)) A(φ) ], A(φ) := Σ_m Σ_y F_m(y) Π_k φ(y_k), (θφ)(t) := φ(−t).
Reversible chain P = [[1/2,1/4,1/4],[1/4,1/2,1/4],[1/4,1/4,1/2]], π uniform.
PASS iff for 200 pseudo-random F (fixed seed, rational entries): Q_OS(F) = Q_dir(F) exactly, Im Q = 0, and Q ≥ 0.
Control X3a (must fire): dropping the complex conjugation in ΘF^* gives a value ≠ Q_dir for at least one of the 200 F.
Control X3b (must fire): for the deterministic cyclic chain 0→1→2→0 (stationary, uniform π; not reversible), the form at
F = (0, F_1 = indicator of t = 1, 0, 0) is negative (expected −1/3): shows the ≥ 0 gate can fail.

Overall verdict: PASS iff G1, G2, G3 all PASS and X1, X2, X3a, X3b all fire. Any exception or stderr output = FAIL.
