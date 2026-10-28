# Check x3: criteria (written 2026-10-27, before checks/x3_soft_rp.py exists)

Purpose: test two session-4 claims on explicit finite models. (1) Theorem X-RP^S: soft (normalised-kernel) blocking
keeps reflection positivity across a block-boundary plane, and for site planes the normalisation 𝒩 is what blocks the
proof. (2) Lemma KN's algebraic core: for M̄ a mean of unitaries T_i = S e^{X_i} with ||X_i||_op ≤ δ ≤ 1/4,
W' := S e^{X̄} (X̄ = mean X_i), R := W'^{-1}M̄ - 1 obeys ||R||_op ≤ 3δ², and for every V in SU(N),
Re tr((W'^{-1} - V^{-1})M̄) ≥ ½x² - 3√N δ² x with x = ||V - W'||_HS.

Toy model for A and B (a spin toy; it tests the RP mechanism of the proof, not gauge structure): fine Z_q clock spins
on a ring of 6 sites, weight exp(β Σ_x cos(σ_x - σ_{x+1})); blocks of 3 sites; coarse Z_Q spins φ_b drawn from the
normalised kernel k(φ | M̄_b) = exp(κ Re(e^{-iφ}M̄_b)) / 𝒩(M̄_b), M̄_b the mean of e^{iσ_x} over the block,
𝒩 = Σ_φ exp(κ Re(e^{-iφ}M̄_b)). All sums exact (no sampling).

**A (must hold; PASS criterion).** Block-boundary plane between sites 2|3 (antipode 5|0), θx = 5 - x, blocks {0,1,2},
{3,4,5}. Gram matrix G[(s', φ'), (s, φ)] = P((σ_5, σ_4, σ_3, φ_2) = (s', φ'), (σ_0, σ_1, σ_2, φ_1) = (s, φ)) over the
indicator basis of positive-side variables. PASS iff min eigenvalue ≥ -1e-12 (relative to max eigenvalue) for every
(q, Q, β, κ) in the grid q ∈ {3, 5}, Q = 4, β ∈ {0.3, 1.0, 2.5}, κ ∈ {0.5, 2.0, 6.0}. Also report G - G^T (must be
≤ 1e-12: θ-invariance of the joint law).

**B (informational; interpretation pre-stated).** Site plane through sites 0 and 3, θx = -x mod 6; blocks {5,0,1} and
{2,3,4} are centred on the plane, so both coarse spins are θ-fixed. Positive algebra: functions of (σ_0, σ_1, σ_2, σ_3,
φ_A, φ_B). Gram matrix as in A (q = 3, Q = 4, same β, κ grid). Two versions: B1 normalised kernel; B2 unnormalised kernel
exp(κ Re(e^{-iφ}M̄)) (this changes the fine marginal). Interpretation fixed now: B2 is expected PSD (the unnormalised
weight factorises as G·θ(G) over a θ-fixed variable). If B1 has a min eigenvalue < -1e-10 (relative) in some case,
"site-plane RP FAILS for the normalised soft kernel" may be stated; if B1 is PSD in all cases, only "the proof of
X-RP^S does not apply to site planes" may be stated.

**C (must hold; PASS criterion).** 2000 random instances each for SU(2) and SU(3): S Haar-random, 4 to 12 unitaries
T_i = S e^{X_i} with X_i random in su(N), ||X_i||_op = δ·u (u uniform in (0,1]), δ uniform in (0, 1/4]; random V
(both Haar and near W'). PASS iff ||R||_op ≤ 3δ² in every instance and the inequality
Re tr((W'^{-1} - V^{-1})M̄) ≥ ½x² - 3√Nδ²x holds in every instance (tolerance 1e-12). Report max ||R||_op/δ².
Discrimination: C is discriminating for the constant 3 only if the max ratio is ≥ 0.1 (reported either way).

Run discipline: one process, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8 and memory ≥ 25% free checked before the
run, no `timeout`. Time and peak memory recorded in checks/x3_time.txt.
