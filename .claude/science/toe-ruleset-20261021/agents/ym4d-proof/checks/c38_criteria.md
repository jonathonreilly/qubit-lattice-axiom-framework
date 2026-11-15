# c38 criteria (written before any c38 script; session 22, 2026-10-28 UTC; targets RTARGET.md §48 A)

Run discipline: machine-wide numeric lock (`until mkdir …/locks/numeric; do sleep 20; done`, run, `rmdir` exactly once, no
trap), nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, load (1-min) < 8 and memory ≥ 25% free before each job, peak memory
< 1 GB, each job < 20 min, no `timeout`, python without -I. A FAIL is recorded as a FAIL; no criterion is edited after a
run. Parts are independent: `python3 c38_cubic.py A|B|C`.

Objects (trivial background, d = 4, L = 3, κ ≡ 1, SU(2) with su(2) structure constants ε_{abc}; unit cell = one block:
324 fine links, 486 fine plaquettes, 4 coarse links; Bloch fibres as in c37 (Fib)).
- Level-0 action in link logs u (U_b = e^{u_b}) and coarse logs B (V_c = e^{B_c}): G(u, B) := Σ_p φ(log U_p) +
  κΣ_c √det(M̄_c)·φ(log(V_c^†W_0(M̄_c))) with φ(X) := Re tr(1 - e^X) (the c36 B soft density), M̄_c the S4' contour average
  (c36 `Mbar`: 81 starting sites × 24 axial orders, c_X → y → y + Le_μ → c_{X+μ}).
- Quadratic part (normalisation ½|X|² for φ): G_2 = ½|du|² + ½κ|Qu - B|² (c35/c37's O_0 without the fixing).
- Linear critical branch (all fine directions): **Û(K) := κM(K)^+Q(K)^†, M := d^†d + κQ^†Q** (pseudo-inverse, eigenvalue
  cut 1e-9 relative). Gauge-mode ambiguity is irrelevant at cubic order when ∇_uG_2(ÛB, B) = 0 (A1 checks it).
- Cubic part, in the bracket ⟨X, [Y, Z]⟩ ↦ ε_{abc}X^aY^bZ^c (the true SU(2) cubic is a fixed constant times this, common to
  every object below):
  **E_3(B) := Σ_p Σ_{i<j}½σ_iσ_j ε(dÛB)_p(ÛB)_{b_i}(ÛB)_{b_j} + κΣ_c avg_{contours j of c}Σ_{k<l}½σ_kσ_l ε((QÛ - 1)B)_c
  (ÛB)_{b_k}(ÛB)_{b_l}** (plaquette links in path order (x,μ)+, (x+μ,ν)+, (x+ν,μ)-, (x,ν)-; contour links in path order).
  By Lemma E3 at the trivial background (tree level), E_3 is the cubic Taylor coefficient of E_1^br(e^B).
  **W_3(B) :=** the same Wilson expression on the coarse lattice with u = B (the cubic vertex of S_W, i.e. D³S_W(1) = the
  level-0 object in own units).
- Kernels: E_3(B) = Σ_{x,y,z}T(x,y,z)ε_{abc}B^a_xB^b_yB^c_z with T totally antisymmetric (computed from the Bloch vertex,
  antisymmetrised, 8-dim inverse FFT on the side-T coarse torus). **N3(T) := max_x Σ_{y,z}|T(x, y, z)|** (the signed
  N_0-type norm: one slot fixed, ℓ¹ over the other two; scalar kernel). **R_3(T) := N3(T_E)/N3(T_W).**

## A. Validation
- A1 (12 random K on the (2π/5)Z⁴ grid): max ||M(K)Û(K) - κQ(K)^†|| ≤ 1e-9; dÛ(K) = 𝒦(K)d_1(K) and QÛ(K) - 1 = 𝒦_ρ(K)d_1(K)
  (c37's fibres F1h, rh) to ≤ 1e-9; the Hessian Û^†d^†dÛ + κ(QÛ - 1)^†(QÛ - 1) equals c37 E's Ĥ_1 formula
  κ - κ²(QÕ^{-1}Q^† - Q(1 - Π)Q^†) and equals -κ𝒦_ρ(K)d_1(K) (the factorisation through the coarse curl) to ≤ 1e-9.
- A2 (coarse torus T = 3, SU(2)): W_3 by the formula against the exact Wilson action, (S(tB) - S(-tB))/(2t³) Richardson-
  extrapolated from t = 0.01, 0.02, times the bracket constant: relative error ≤ 1e-5; W_3 by the antisymmetrised kernel
  against the formula: relative ≤ 1e-10.
- A3 (coarse torus T = 2, fine side 6, SU(2), random B): the odd part of G(tÛB, tB)/t³ (exact actions, Richardson as in A2)
  against E_3(B) by the formula times the bracket constant: relative ≤ 1e-5; E_3 by the Bloch vertex sum and by the
  antisymmetrised kernel against the real-space formula: relative ≤ 1e-8.
PASS iff A1-A3.

## B. Main: the signed cubic norm, level 1 against level 0 ((H-C) artefact test)
N3(T_E), N3(T_W), R_3 at T ∈ {4, 5}; also N3 of the Wilson and soft parts of T_E separately, the max imaginary part of the
kernels, and (informational) the absolute-leg bound N3^abs (absolute values on every fine leg before summing; the analogue
of Lemma E3's Z_colZ_row² counting) for T_E.
**PASS iff R_3(5) ∈ [0.1, 10] and |R_3(5) - R_3(4)| ≤ 0.1·R_3(5).** (Prediction: R_3 of order 1, far below c37 D2's
Z_colZ_row² = 1266.8.)

## C. Informational: smooth limit (continuous momenta, no torus)
For s ∈ {0.1, 0.03, 0.01, 0.003}: K_1 = sk_1, K_2 = sk_2, K_3 = -K_1 - K_2 (k_1, k_2 fixed generic unit vectors), fixed generic
polarisations e_1, e_2, e_3: c_3(s) := V_A^E(K_1, K_2, K_3)[e_1, e_2, e_3]/V_A^W(…)[…] (antisymmetrised vertices) and c_2(s) :=
⟨e, H_E(sk)e⟩/|d_1(sk)e|² (generic e, H_E the Hessian of A1). Prediction (not a criterion): c_2 and c_3 within 0.05 of 1
at s = 0.003 and |c_3 - c_2| ≤ 0.01 (gauge invariance ties the cubic to the quadratic coefficient).

Not attempted in c38: a closed-input (LP) trilinear norm; level 2.
