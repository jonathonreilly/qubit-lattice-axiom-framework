# TOR-1 pre-registration: the chiral-measure RP test on a periodic torus

Written 2026-10-15, started 15:25Z (`date -u`), before any run. Worker: Claude Opus 5.5 (xhigh), same family as NT-1′, NT-1″,
K2c and the supervisor; not independent. Cap 0.5 GB per run via `scripts/capped.sh`; one process at a time; OMP 2 threads.
Deadline 21:00Z.

FIXED readings and gate (TESTS.md, "Campaign wave 2e", TOR-1; copied, not changed):
- G-LEG-T: (a) Lx ≥ 4. (b) Gauge invariance exact to roundoff; exponential locality of the measure current in the bulk, with no
  edges. (b″) Transport around at least one non-contractible Wilson-line loop returns a trivial phase for 11112, and the anomalous
  L1 control fails. (c) The anomalous control visibly fails locality or integrability. (d) The reflection condition holds.
- CHI-RP-FAIL: G-LEG-T passes, and the kernel has a quadrature-converged negative eigenvalue below −10E.
- CHI-RP-PASS-at-power: G-LEG-T passes, and the kernel is PSD within error, with the vector-like reference negative on the same
  geometry.
- OPEN: otherwise, naming the item.

Prior art (step 0). `git grep` on origin/main for Lüscher/toron/Kadoh/Kikukawa/"measure term"/"Weyl determinant"/"fermion
integration measure": no torus Lüscher-measure or chiral-RP construction on main (hits are RP/OS-transfer notes and a compact-U(1)
toron note in other contexts). All prior work on this object is on the exercise branch: NT-1′ (open-time measure, refereed
OPEN at (b)), NT-1″ (open-time edge obstruction; descriptive torus Chern numbers C(11112) = 0, C(L1) = −1), K2c (torus RP at
Lx = 2, vector-like). Reused code: NT-1′ `nt1p_lib.py` (`dq_dA`, `q_of`, transport scheme), K2/K2c `lat2d.py` (Duffy cells for
one Lx = 4 crossing plane), `k2c_lib.py` conventions, NT-1″ `nt1pp_b2c.py` (toron Chern method, as a cross-check).

## 1. Geometry and conventions

- 2D compact U(1) on an Lx × Lt torus; gauge links periodic. Sites (x, t), x ∈ Z_Lx, t ∈ Z_Lt. γ_x = σ1, γ_t = σ2, γ5 = σ3.
  Massless Wilson r = 1, M = 1, H_W = γ5(D_W − M), overlap D = 1 + γ5 sign(H_W) (NT-1′ conventions).
- Fermions antiperiodic in x (sign on every x-link x = Lx−1 → 0) and antiperiodic in t, the t-sign placed on the plane-B crossing
  links (x, T) → (x, T+1), T = Lt/2, so that the sign pattern is invariant under the link reflection (K2c's torus convention).
- Link reflection θ: t → 1 − t (mod Lt); x-links map to x-links, t-links to minus the mirrored t-links. Two reflection planes:
  A between slices 0|1, B between slices T|T+1. Λ+ = slices 1..T.
- Charge sets: 11112 = four left-handed charge 1, one right-handed charge 2 (L Weyl ↔ positive subspace of H_W(U^e), rows γ5 = +1;
  R ↔ negative subspace, rows γ5 = −1, as NT-1′). Anomalous control L1 = one left-handed charge 1.
- Sizes: Lx = 4 primary. Lt = 8 primary for gates; the kernel Lt is chosen by the cost rule in §5.

## 2. The measure (Lüscher hep-lat/9811032, Theorem 5.4 as constructed in its §§7–11)

Vacuum sector Q = 0 only (all kernel nodes are in it; checked per node).
1. **Canonical decomposition (Lemma 7.4).** F_p = plaquette angles reduced to (−π, π]. A^T = pinv(P) F (the unique transverse,
   zero-mean potential with plaquettes F, eq. 7.15). Toron w_μ = W_μ[θ] − W_μ[A^T] on a reference line (real lift).
   Canonical potential A_c = A_w + A^T with A_w = w_μ/L_μ on every μ-link (gauge-equivalent to Lüscher's U[w]).
   This map is a function of gauge-invariant data, so ρ is gauge-invariant by construction; it is θ-covariant (checked in T0).
2. **Toron-torus part ρ_tor(w) (§§9, 11.2).** On zero-field toron fields everything is momentum-diagonal. The Weyl basis is
   parallel-transported per momentum along the path 0 → (w_x, 0) → (w_x, w_t), and multiplied by exp(−i ∫ S), where S is
   Lüscher's Lemma 9.2 connection on the toron torus built from the multiplet's Berry curvature: S_x(w_x, 0) = 0 on leg 1 and
   S_t(w_x) = (Γ_t(w_x) − Γ_t(0))/2π on leg 2, Γ_t(r) = continuous lift of the phase of the multiplet's Berry holonomy around the
   w_t-cycle at w_x = r (K = 0 on the toron torus because j⋆ vanishes at zero field). Sign conventions are fixed by the
   single-valuedness algebra written in the code header, not tuned on results.
3. **Transverse part (eq. 11.15–11.16).** Basis transported along the straight curve U[w] e^{isA^T}, s ∈ [0, 1], by polar/SVD steps,
   Ns = 8 with Richardson against Ns = 4 (NT-1′ scheme).
4. **Measure-term phase (eq. 5.8).** i s_k Φ with Φ = Σ_l A^T_l ∫_0^1 ds (1 − s)-weighted local cohomology current, built exactly as
   NT-1′ but on the torus: the multiplet anomaly's gauge-invariant plaquette derivative g(x, p) = Σ_l ∂q(x)/∂θ_l · a_p,l with
   a_p = pinv(P) e_p (unit flux at p, uniformly compensated, fixed toron); monopole Σ_x g(x, p) removed at the plaquette corners
   (expected 0 on the torus, logged); local Poincaré current along symmetric shortest torus paths; any residual divergence mismatch
   sent through the torus Laplacian right inverse (logged; expected roundoff). s_k fixed by the un-fixed Ward test (T0), expected −1.
   So log ρ = log ρ_tor(w) + log T(w; A^T) + i s_k Φ, evaluated on A_c.

## 3. Gate G-LEG-T operationalised

- (a) Lx = 4.
- (b1) Gauge invariance: |Δ log ρ| under ≥ 5 random gauge transformations ≤ 1e-10 on ≥ 5 random admissible fields (complex log,
  mod 2πi). Un-fixed Ward identity (no canonicalisation: ray from U[w] to A_w + A^T + ∂ω): residual must fall with Ns at
  ≥ second order with the registered s_k and stall with the opposite sign (supporting that canonicalisation evaluates the
  gauge-invariant limit, not a hidden anomaly).
- (b2) Bulk locality: response χ(d) = max over link pairs at torus taxicab distance d of |∂ kbb_l / ∂θ_l'| (central finite
  differences, ε = 1e-4) on ≥ 3 random admissible fields at Lx = Lt = 8 (also 4×8). PASS: fitted exponential rate ν > 0 at ≥ 3σ
  over d ≥ 1 for 11112. Also the plaquette-derivative profile max |g(x, p)| vs distance.
- (b3) Finite-volume part: the toron connection magnitude max_wx |Γ_t(w_x) − Γ_t(0)| (11112) at L = 4, 6, 8, 10 (square tori,
  zero field) decays exponentially (fit rate > 0 at ≥ 3σ, ≥ 3 sizes); L1 contrast reported.
- (b″) Non-contractible loops. (i) On the toron torus (momentum space, fine grids): base-cycle Berry holonomies h_x(0), h_t(0) and
  the winding of Γ_t over the w_x-circle. (ii) Full construction: ρ continued around the loop w_ν → w_ν + 2π (ν = x and t) at
  ≥ 3 base fields with A^T ≠ 0; closure Q_loop = ρ(end)/ρ(start). (iii) Independent route: Lüscher Lemma 8.1 holonomy
  det(1 − P_0 + P_n…P_0) of the multiplet computed in position space with projectors only, along the same loop at one base field
  with A^T ≠ 0, n → ∞ by Richardson, compared with Π_k det(v_{k+1}† v_k) from the construction's bases.
  PASS (11112): |Q_loop − 1| ≤ 1e-8 on every tested loop and (iii) agreement ≤ 1e-5. L1 FAILS if, for some loop, no constant
  phase redefinition can close it (winding ≠ 0), or |Q_loop − 1| ≥ 0.1.
- (c) PASS if L1 shows winding ≠ 0 (integrability) or a plateau in g(x, p)/kbb response with Lx·plateau roughly constant
  (locality), at the same settings.
- (d) ρ(θU) = c·conj ρ(U): c from ≥ 10 random admissible fields; PASS if the spread of c ≤ 1e-8.

## 4. RP kernel (only if G-LEG-T passes; otherwise the kernel may still be run as descriptive)

- W-matched gauge-invariant point-orbit witnesses as in K2c V2: each Λ+ configuration holonomy-shifted so the x-Wilson lines of
  slices 1 and T are 0 (plaquettes unchanged), bulk plaquettes ≤ 0.55 (margin), random generator rand_half (σ 0.3), seeds fixed
  per pool. Hard crossing weight δ = 0.6, β_g = 0. Pools: P1 random W-matched k = 8 (seed 3101); P2 if time.
- Crossing integration (Lx = 4 torus: 7 dims): plane A by lat2d Duffy cells (φ_0 = 0 gauge-fixed by the global negative-half
  shift), plane B by the same cells, the Polyakov variable χ_0 by the trapezoid rule on the full circle.
  Levels: LOW (n, nw) = (2, 4), HIGH (3, 6); third level (4, 8) on a random subset of 6 off-diagonal entries plus the diagonal.
- Kernels on the same nodes: chiral 11112 (full measure, every upper-triangle entry; Hermiticity checked on the subset by
  computing (b, a) directly), modulus |det D(1)|²|det D(2)|^½, vector-like overlap O (m = 0.05; power reference), massless vector
  overlap, Wilson (m = 0.05), pure gauge. Error estimate E = k·max(q, q3, h) + 1e-13 (K2c/NT-1′ estimator; q = max entry change
  LOW→HIGH, q3 = HIGH→third on the subset, h = Hermiticity defect). Quadrature-converged negative: λ_min < −10E.
- Phase question: report max phase spread of ρ over nodes, ‖Z_chi − Z_mod‖, and λ_min shift chiral vs modulus.

## 5. Cost rule (registered; decided by a timed probe before the kernel)

Time one chiral measure evaluation batch and one modulus batch at Lt ∈ {8, 4}. Run the kernel at Lt = 8 if the projected total
(LOW + HIGH + third, all kernels) is ≤ 80 min; else Lt = 6 if ≤ 80 min; else Lt = 4. If even Lt = 4 exceeds 80 min, reduce to
LOW = (2, 4), HIGH = (3, 4) and k = 6, and say so. Kernel results are reported only with their E; no reading from an
unconverged kernel (that is OPEN, naming "kernel convergence").

## 6. Outputs

`scripts/*.py`, `*.out` (each ending with the watchdog peak RSS), pools `pool_TOR1_*.npz`, kernels `*_Z*.npy`/`*_logK.npz`,
toron data `toron_*.npz`, locality arrays `loc_*.npy`. Final report = final message.

## Follow-ups (dated, appended only)

**F1 (2026-10-15, 15:49Z, before running it).** (b″)(iii) as registered (comparing Lemma 8.1 position-space projector products
with Π_k det(v_{k+1}† v_k) from the construction) is algebraically equivalent to the Q_loop closure already measured (worked
out in the code notes: for any basis, Π det(v_{k+1}† v_k) → W̃ · Q_loop^{-1}), so it adds no independent content. Replaced by
an independent-code check of the only global input, the toron-torus topology: NT-1″'s position-space `nt1pp_b2c.py` (Lüscher
wrap-link toron placement, Fukui–Hatsugai–Suzuki Chern numbers; copied unchanged) at 4×8 and 4×4, to agree with my
momentum-space winding (11112: 0; L1: ±1). Also: kernel-time settings of the measure fixed now, before any kernel run:
ntor = 192 (Richardson 192/96), Γ_t from its 512-point grid by periodic cubic spline (nloop 1024/512), Ns = 8 (Richardson 8/4).
These were chosen from T0's convergence data (closure 7.7e-7 → 4.8e-8 when doubling at 4×4), not from kernel results.

**Note (15:50Z).** F1's header time '15:49Z' was typed one minute ahead of the clock (`date -u` read 15:48Z just after it was written). The text is unchanged; this note corrects the stamp to 15:48Z.

**F2 (2026-10-15, 15:52Z, before any kernel run). Cost rule outcome and kernel plan.**
- Timed probe (`PROF_4_8_32.out`, `PROF_4_4_32.out`, plus a batch-64 probe): chiral measure ≈ 37 ms/node at Lt = 8 and 8 ms/node
  at Lt = 4 (with the kernel settings below); modulus 3.5 / 0.5 ms/node. The Lx = 4 torus crossing integral is 7-dimensional; the
  W-matched plane polytope has 4 Duffy tetrahedra, so a level (n, nw) has (4n³)²·nw nodes per entry: (2,4) 4096, (2,6) 6144,
  (3,4) 46 656, (3,6) 69 984, (4,4) 262 144. With k = 6 (21 upper-triangle entries) the registered HIGH (3,6) chiral kernel
  projects to ~15 h at Lt = 8 and ~3.3 h at Lt = 4; even the registered fallback HIGH (3,4) projects to ~2.2 h at Lt = 4.
  So the rule gives Lt = 4, k = 6, LOW (2,4), HIGH (3,4) — and it still exceeds 80 min. I run it anyway because it fits before the
  deadline, and say so; the third level (4, ·) is infeasible for the chiral kernel and is replaced as below.
- Measure settings in the kernel (from the T0 convergence data, max |Δ log ρ| ≤ 1.4e-7 against ntor 384 / Ns 8): toron legs
  n2 = 96, n1 = 24 (Richardson with half), Γ_t by periodic spline, transverse Ns = 4 (Richardson 4/2), kbb Simpson on the same
  4 intervals.
- Pool: P1 = `pool_TOR1_Lt4_k6_s3101.npz` (W-matched random, k = 6, no search). Only upper-triangle entries are computed; the
  lower triangle is the complex conjugate, which is exact given the measured reflection condition (c = 0, spread 5e-14) and
  a θ-symmetric crossing rule; Hermiticity is checked directly on 2 off-diagonal pairs computed both ways at LOW.
- Error estimate for each op: E = k·max(q_plane, q_poly, h) + 1e-13, with q_plane = max entry change (2,4) → (3,4),
  q_poly = max entry change (2,4) → (2,6), h = Hermiticity defect. This replaces the registered third-level q3 by a second,
  independent refinement direction (the Polyakov circle); it is still an a-posteriori estimate, not a bound. For the cheap ops
  (modulus, O, massless vector, Wilson, PG) a (4,4) third level on 2 off-diagonal entries + diagonal is added if time allows.
- Reading rule unchanged: CHI-RP-FAIL needs G-LEG-T and the chiral λ_min(3,4) < −10 E_chi; CHI-RP-PASS-at-power needs the chiral
  kernel PSD within error and the vector-like O reference converged-negative on the same pool; otherwise OPEN naming the item.
- Chain order: cheap ops (2,4),(2,6) → chiral (2,4),(2,6) → cheap ops (3,4) → chiral (3,4) → modulus third level (4,4) subset.

**F3 (2026-10-15, 16:01Z; after the cheap kernels on P1 and a Polyakov probe, before any further kernel run).**
- What was seen (descriptive; `POST_partial1.out`, `tor1_poly_probe.py` output in the report): on P1 (random W-matched, k = 6)
  the cheap kernels at (2,4) and (2,6) are all PSD (O λ_min +4.9e-6). The integrand's Fourier modes in the Polyakov variable χ_0
  decay fast for O (|c_4/c_0| ≈ 3e-7, |c_6| ≈ 6e-10) but slowly for the chiral modulus |det D(1)|²|det D(2)|^½
  (|c_4| ≈ 1.6e-3, |c_6| ≈ 4e-5, |c_8| ≈ 1e-6, |c_12| ≈ 1e-9): the charge-2 factor doubles the frequency. So nw = 4 or 6 is
  not converged for the chiral kernel; the F2 chain was stopped after one chiral entry (no chiral kernel result exists from it).
- New plan (replaces F2's levels; same estimator form):
  - Pool P2 = greedy W-matched search on the VECTOR-LIKE O kernel (power reference, as NT-1′'s P-A; never on the chiral answer):
    `tor1_search.py 4 6 3201` (start 3 random; each step best of 4 random + 4 perturbed candidates by λ_min(O) at (2,6)).
  - Levels: A = (2, 8) and B = (2, 12) on all 21 upper-triangle entries; C = (3, 8) on the 6 diagonal + 2 off-diagonal entries
    (subset seed 12). Ops: chi, mod, O, vec0, W, PG. Hermiticity of chi checked on 2 reversed pairs at A.
  - Reported kernel = B. E = k·max(q_poly, q_plane, h) + 1e-13 with q_poly = max|Z_B − Z_A| (all entries), q_plane =
    max|Z_C − Z_A| over the subset, h = Hermiticity defect. Same reading rule as before.
  - Order: search → cheap A, B → chi A, B → cheap C → chi C. If the deadline cuts chi C, the chiral kernel has no plane-refinement
    estimate and the reading is OPEN (kernel convergence).
- P1 cheap results are kept as descriptive (a random pool without search).

**F4 (2026-10-15, 16:12Z; registered before running, to run after the kernel chain if time allows).** Descriptive add-ons for
G-LEG-T (b): (i) `tor1_hess.py 4 8 11112 2 7301` — response of the FULL measure current j_l = ∂ log ρ/∂θ_l (complex) to one
source link, d²log ρ/∂θ_l0∂θ_l by mixed central differences (ε = 2e-3), vs torus distance; same for L1 (one field) as contrast.
This answers the NT-1′ referee's remark that the kbb response is not the full measure current. (ii) `tor1_ward.py 4 8` (the Ward
test at the primary size). Neither changes a registered gate decision; they are reported as descriptive.

**F5 (2026-10-15, 16:18Z; before running it).** The cheap kernels on P2 (`POST2_partial.out`) show the Wilson + hard kernel at
λ_min −3.65e-6 (q_poly 3.6e-15; plane refinement pending), i.e. the K2c Lx = 2 positivity argument for Wilson + hard does not
obviously carry to Lx = 4. Before interpreting that, a geometry control is added: Wilson (m = 0.05) with β_g = 0 and NO
admissibility cut (Haar crossing links; 4-point trapezoid per crossing link, exact for the degree-≤1 Wilson determinant, checked
against 6 points on one entry) on the same pool and joined geometry. Expected: PSD to roundoff (Osterwalder–Seiler positivity of
Wilson fermions under link reflection at β = 0). If it is not PSD, the kernel geometry is wrong and no kernel reading is made.
The chain was paused after the running chiral (2,8) job for this control and then resumed unchanged.

**F6 (2026-10-15, 16:43Z).** Geometry control F5 passed (`HAAR_control.out`: Wilson + Haar λ_min +4.5e-9, 4- vs 6-point exact to
3.6e-15). Chiral kernel at A = (2,8) on P2: λ_min −6.446e-7, modulus −6.461e-7, and the modulus Polyakov change A→B is
q_poly(mod) = 1.34e-7, so E_chi ≥ 6 × 1.3e-7 ≈ 8e-7 on the registered estimator, i.e. |λ_chi| < 10 E whatever the plane level adds
(E only grows with more terms). The chiral plane refinement C (107 min) therefore cannot change the chiral reading and is dropped;
chi B (2,12) still runs (it is the reported kernel and gives the chiral q_poly), and cheap C still runs (it decides whether the
vector-like O reference is converged-negative). The freed time goes to F4 (full-current response, Ward at 4×8).

**Note (16:42Z).** F6's header stamp '16:43Z' was typed ahead of the clock (`date -u` read 16:41Z when it was written); text unchanged.

**F7 (2026-10-15, 16:42Z; before any of the runs it names).** Refinement of the chiral kernel's error estimate, added because the
F3 estimator's q_poly = |Z(2,12) − Z(2,8)| measures the Polyakov error of the LOWER level (dominated by the charge-2 factor's
|c_8| ≈ 1e-6 Fourier tail), not of the reported level. Added level B′ = (2, 16) for chi on all 21 entries, and chi at C = (3, 8)
on a reduced subset (diagonal entries 0 and 5 plus off-diagonal (0, 5); subset fixed now, not from results). Second estimate:
E′ = k·max(|Z_B′ − Z_B|, q_plane, h) + 1e-13 with q_plane = max|Z_C − Z_A| on that subset; reported kernel B′. Both E (F3, as
registered) and E′ (F7) are reported with the reading each gives; the F3 reading stays the registered one, F7 is labelled a
follow-up. Same treatment for the cheap ops where available. Run order: chi B (2,12) → cheap C → full-current response 11112
(F4 i) → Ward 4×8 (F4 ii) → chi B′ (2,16) → chi C subset → L1 full-current response.

**F8 (2026-10-17, 11:02Z). Gap.** The worker session was stopped by the account usage limit at about 17:05Z on 2026-10-15 (last
action: waiting on the chiral (2,12) job). The background chain `chainO.sh` kept running and finished at about 18:54Z on
2026-10-15 (`chainO.done`); every registered F7 job completed (chi (2,12), cheap (3,8) subset, F4 (i) and (ii), chi (2,16),
chi (3,8) fixed subset, L1 response). Nothing of mine was running at resume (`ps` checked). No result was looked at between the
stop and this note; no reading or registration was changed. New deadline 16:00Z on 2026-10-17. Finished runs are not repeated.

**F9 (2026-10-17, 11:03Z; before running it).** Descriptive phase probe `tor1_phase_probe.py` (written 2026-10-15, not yet run):
the chiral measure's phase over the nodes of entries (0,0), (0,3), (2,5) at level (2,8), split into S-phase and kbb phase,
and |Σ w ρ| / Σ w |ρ|. Motivation: the chiral kernel came out real to 3e-14 and equal to the modulus kernel to 4e-7 (POST3.out).

**F10 (2026-10-17, 11:07Z; correction of F4 (i), registered before the new run).** F4 (i) called ∂ log ρ/∂θ_l "the full measure
current". That identification is wrong (my error): ∂ log ρ/∂θ_l is the expectation of the fermion gauge current, which contains
the massless-fermion propagator term Tr[(ūDv)⁻¹ ū(δD v + D δP̂ v)] — physical vacuum polarisation, nonlocal for massless fermions
(its real part is exactly the vector-like |det D(1)|²|det D(2)|^½ response) — in addition to Lüscher's measure current.
`HESS_*.out` is therefore reported only as that descriptive quantity, not as a locality test of the measure. The object Lüscher's
conditions constrain is the measure term L_η = i Σ_j (v_j, δ_η v_j) of the construction's basis (Theorem 5.1). New descriptive
test `tor1_jcur.py`: j_l = −Σ_f m_f Im ln det(V_f(U−εe_l)† V_f(U+εe_l))/(2ε) − ∂_l α (α = S-phase + s_k Φ; V_f the transported
bases at the actual, non-canonicalised fields, via the un-fixed ray), ε = 1e-4, Ns = 8. Checks: (i) anomalous Ward identity
Σ_l (∂ω)_l j_l = ± Σ_x ω(x) A_L(x) for random ω (|ratio| = 1 identifies j as Lüscher's measure current); (ii) the response
∂j_l/∂θ_l0 (δ = 1e-3) vs torus distance for 2 fields × 2 source links (11112, 4×8 and one field at 8×8) and 1 field for L1.
Locality reading (descriptive, does not change the registered (b2) decision): exponential decay of max response with distance,
and L1 contrast.

**F11 (2026-10-17, 11:24Z; before running).** Ward-identity convergence of the F10 current: `tor1_jcur.py 4 8 11112 2 7402 Ns ward` with
Ns = 4 and 16 (same fields as the Ns = 8 run), to show the 0.1–3 % mismatch is transport discretisation.

**F12 (2026-10-17, 11:25Z; before running).** The 8×8 11112 measure-current response (`JCUR_Lx8_8_11112_1_7403.out`, Ns = 8) flattens at
about 2e-5 for d = 6–8, the same size as that run's Ward mismatch (≈1e-5). To separate a discretisation floor from a real tail,
rerun the same field at Ns = 16 (`tor1_jcur.py 8 8 11112 1 7403 16`). Descriptive.

**Closing log (2026-10-17, 11:43Z).** `tor1_poly_probe.py` (F3's Polyakov probe, first run 2026-10-15 without the watchdog and without
saving its output) rerun under `capped.sh` only to archive its output (`POLY_probe.out`); same numbers. F12 outcome: the Ns = 16
profile equals the Ns = 8 one to 3 digits, so the 8×8 tail is not a transport-discretisation floor. All runs finished; nothing of
mine is running.

**Correction (2026-10-17, 11:43Z).** The closing log above said the archival rerun of `tor1_poly_probe.py` gave the same numbers; it had
in fact crashed (the script exec'd the pre-refactor `tor1_kernel.py`). The script was adapted to import `tor1_geom` (no change to
what it computes) and rerun; its output is now in `POLY_probe.out`.
