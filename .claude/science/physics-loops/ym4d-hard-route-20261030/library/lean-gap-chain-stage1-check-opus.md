lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T09:11Z

# Check of row 1459 (Lean Stage 1 of the gap chain): faithfulness and non-vacuity

Row 1503. Started 2026-11-24T21:11Z (date -u), Mac mini worker 2, at commit 7844497b7. Cross-provider check: the Lean files were written by gpt-6.2-astra (row 1459); this check is by Claude Opus 5.5 high. Release credit: the YM4 Lean library and complete account are Sussman-Alpoge (with Claude and Codex); the hand proofs are the lane's rows 668, 697-699, 1356, 1359 and the U4 row of library/gap-os-equiv.md.

## Plan

1. Read lean/gapchain/GapChain/{SequenceLemma,LemmaM1,TheoremS}.lean and RECEIPT.md in full.
2. Read the hand sources: U4 in library/gap-os-equiv.md; Lemma M1 in library/gap-mini-mneutral-fable.md (row 1356) and check 1359; Theorem S in library/gap-crux-restate.md section 3.4 with checks 698-699 and the S3' correction; Lemma A2 of row 668.
3. Faithfulness: statement by statement, and field by field for PairWeight, BoxSpectrum, TorusData.
4. Non-vacuity: build a consumer file in /tmp scratch that constructs an explicit TorusData and applies theoremS; print axioms.
5. Verdict.

## Step 1. Inventory of the Lean statements (read in full)

Files at 7844497b7: `lean/gapchain/GapChain/SequenceLemma.lean` (80 lines), `LemmaM1.lean` (110), `TheoremS.lean` (729), `RECEIPT.md` (190). Read in full.

Exported statements checked here:

- **U4** `sequenceLemma`: `q ≥ 0`, `m n ≥ 0` for all n, `m(n+1)^2 ≤ m n · m(n+2)` for all n, and `∃ᶠ j, m j ≤ C q^j` give `m(n+1) ≤ q m(n)` for all n. `sequenceLemma_of_bound`: same with the envelope at all j.
- **W1** `lemmaM1`: H a complex inner product space (completeness not assumed; a `HilbertBasis` is assumed to exist), B continuous, `B.IsPositive`, `∑ ‖B b_i‖^2` summable, `‖φ‖ = 1`, `c > 0`, and the finite-family test `HSNormLE (c⁻¹ B − |φ⟩⟨φ|) δ` (every finite orthonormal family v has `∑‖A v_i‖^2 ≤ δ^2`) give `(1 − δ^2) Σ_i Re⟨b_i, B² b_i⟩ ≤ ‖B‖^2`. `lemmaM1_hsSq` is the same without positivity, with `Σ‖B b_i‖^2`.
- **W5** structures: `PairWeight` (W : ℕ → ℕ → ℝ, all fields only at periods ≥ 3: pos, swap, submul in the first period, logConvex in the first period, lower `∃ d, d a b ≤ log W(a,b)`); `BoxSpectrum` (top > 0, ratio : ℕ → ℝ with 0 ≤ ratio ≤ 1, Σ ratio^3 summable; thermal a = Σ ratio^a; weight a = top^a (1 + thermal a); gap = inf over i with ratio_i > 0 of log(1/ratio_i) in EReal, ⊤ if none); `Box` (three spatial periods), `TorusData` (spectrum : Box → BoxSpectrum; cross: weight of box R[i:=b] at time a = weight of R[i:=a] at time b, for a, b ≥ 3 and R valid; logConvex in time for valid R; lower: for each valid R and axis i, ∃ d, ∀ a b ≥ 3, d a b ≤ log weight_{R[i:=b]}(a)). Note `T.seed n = thermal of cube(2n) at time n`; `seedRate N = log(1/(5041 s))/N` (⊤ at s = 0).
- **Theorem S** `theoremS`: N ≥ 3, seed N < 1/5041 give, for every k, `seed(2^k N) ≤ (5041 seed N)^(2^k)/5041` and `seedRate N ≤ gap(cube(2^(k+1) N))`. `corollaryS3'`: same seed hypothesis gives `seedRate N ≤ gap(cube L)` for every integer L ≥ 2N. `seed_of_phi`: Φ(n) = 16 log W_{cube n}(n) − log W_{cube 2n}(2n) ≤ 19/100000 gives seed n < 1/5041.

Axioms: per RECEIPT and row 1459 lead replay, all standard; I re-print axioms in my own consumer build (Step 5).

## Step 2. Faithfulness of W5 (Theorem S) against row 697 section 3.4, checks 698-699, S3' correction

Hand source read: `library/gap-crux-restate.md` lines 22-87 (Section 1: torus, (TM), (TM-c), Lemma A, definitions of S(k;B), m(B)) and 88-221 (Theorem D, Section 3.4: setting, Lemmas K, X, E, Theorem S, Corollaries S2, S3, the row-699 correction, Lemma E', Corollary S3').

**Dictionary.** Box R = (x, y, z) = the three spatial sides (n_2, n_3, n_4); time = direction 1. `(spectrum R).top` = lambda_0 of T_R; `ratio i` = r_i = lambda_i/lambda_0 for the excited eigenvalues listed with multiplicity, zeros padding; `weight a` = top^a (1 + sum_i r_i^a) = Tr T_R^a = Z(a, x, y, z); `thermal a` = S(a; R); `gap` = inf over i with r_i > 0 of log(1/r_i) in EReal = log(1/max r_i) = m(R) (= +infinity when every r_i = 0). `seed n` = thermal of cube(2n) at time n = S(n; (2n)^3) = the hand s. `seedRate N` = log(1/(5041 s))/N (+infinity at s = 0). `phi n` = 16 log Z(n^4) - log Z((2n)^4) = the hand Phi(n). All match.

**Field by field (TorusData, BoxSpectrum).**

| Field | Lean | Hand assumption it encodes | Verdict |
|---|---|---|---|
| `BoxSpectrum.top_pos` | 0 < top | lambda_0 > 0 ((TM): positive operator, Z > 0) | exact |
| `nonneg`, `le_one` | 0 <= r_i <= 1 | T >= 0; lambda_0 is the largest eigenvalue | weaker than hand: hand has lambda_0 simple (r_i < 1); Lean never needs simplicity, since the top is counted once by the `1 +` in `weight` and a degenerate top would appear as some r_i = 1 |
| `atThree` | sum r_i^3 < infinity | T trace class | weaker than hand (Tr T^3 finite); only periods >= 3 enter |
| `spectrum : Box -> BoxSpectrum` | a spectrum for every triple, including sides < 3 | (TM) for every box with sides >= 3 (Lemma 1.1 of `gap-seed-check.md`) | no constraint is ever placed on a box with a side < 3 (every field quantifies over valid R and replaced sides >= 3), so a junk value there costs nothing |
| `cross` | for valid R, axis i, a, b >= 3: Z(a; R[i:=b]) = Z(b; R[i:=a]) | symmetry W(a,b) = W(b,a) "because Z is invariant under the lattice symmetry that exchanges two axes" | exact; it is only the time-space exchange, the only symmetry the proof uses; true for Wilson (axis permutation maps the plaquette set to itself and preserves the product Haar measure) |
| `logConvex` | for valid R, a >= 3: W(a+1)^2 <= W(a) W(a+2) | Lemma A / Lemma K(c): log Tr T^a is convex in a | **redundant**: it follows from the BoxSpectrum fields alone (Cauchy-Schwarz on sum_i lambda_i^a with the top term included). Not stronger than the hand proof, and true for Wilson. See Step 5 for a Lean proof of the redundancy. |
| `lower` | for valid R, axis i: exists d, for a, b >= 3, d a b <= log Z(a; R[i:=b]) | "ell := inf over a, b of log W(a,b)/(ab) is finite" with the two other sides fixed | exact (same quantifier order: d may depend on the spectator sides). True for Wilson: Jensen on Haar measure gives log Z(n) >= -beta sum_p E_Haar(1 - tr U_p/2) = -6 beta |n|, so d = -6 beta (product of the two spectator sides) works; even the cruder bound 1 - tr U/2 <= 2 gives d = -12 beta (product). |

**Statements.**

- `PairWeight.lemmaK` (deficit antitone at b >= 3), `deficit_nonneg`, `ground_convex`, `ground_multiple`, `ground_limit`, `bulk_eq`: Lemma K (a)-(d) with the corrected domain (rows 698/699: sizes >= 3). Faithful. The Lean route to K(a) differs (doubling plus discrete convexity gives monotonicity of F(a,b)/a at every a, instead of Lemma A(a)); this is a different proof of the same statement, not a change of statement.
- `crossing`, `lemmaX`: Lemma X verbatim (identity and (b - a) kappa(b) <= g(a,b) for 3 <= a < b).
- `lemmaE'`: Lemma E' of row 699 (h >= b > a >= 3), exact. `lemmaE`: Lemma E (h = 2b).
- `enlarge_side`, `cube_enlarge`: the three enlargements of the proof of Theorem S / S3' with exponent L/(2a - a) <= 4 for 2a <= L <= 4a. The spectator sides are carried as in the hand text ((2a,2a) -> (L,2a) -> (L,L)). Faithful.
- `theoremS_step`: S(2n; (4n)^3) <= ((1+s)^64 - 1)^2. Exact, including the time doubling S(2n) <= S(n)^2 from multiplicity (`thermal_add`).
- `seed_polynomial`: (1+x)^64 - 1 <= 71 x on [0, 1/640]. The hand proof goes through e^(64x) and e^0.1; Lean proves 64 (641/640)^63 <= 71 by `norm_num` (exact rational arithmetic in the kernel). Same statement, independent proof. Check by hand: (641/640)^63 = exp(63 log(1.0015625)) ~ exp(0.0983) ~ 1.1033, times 64 = 70.6 <= 71. Correct.
- `dyadic_thermal`, `theoremS`: the dyadic claims of Theorem S. The second conjunct gives m((2 n_k)^3) >= log(1/(5041 s))/N, the hand claim. Faithful.
- `intermediate_thermal`, `corollaryS3'`: Corollary S3' of row 699 (every integer L >= 2N from one seed), with the bracketing 2a <= L <= 4a (hand: D <= L < 2D with D = 2a; Lean also admits L = 4a, harmless). Lean's bound for the gap is log(1/q)/N, the weaker of the two in the hand proof (the hand also has the extra log 71/(2^k N)), so not stronger than proved. Faithful.
- `seed_of_phi`: Phi(n) <= 19/100000 gives s < 1/5041, the last sentence of Theorem S via Theorem D(b). Lean's route to D(b) (`log_seed_le_phi`) uses three side doublings (Lemma A(a) through `cross` and `weight_add`) and then log(1+S(n)) <= 2 log W(n) - log W(2n) on the cube (2n)^3, which uses S(2n) <= S(n) in place of the hand's Lemma A(b) (lambda_0^n >= Tr T^(2n)/Tr T^n). Equivalent content; statement exact.

**What Lean does not carry, and is not claimed to.** (i) Theorem S is about any TorusData; nothing ties `spectrum` to the Wilson transfer operator. The instantiation obligation is exactly: for SU(2) Wilson at fixed beta, (TM) on every box with sides >= 3 with the excited eigenvalues listed with multiplicity, plus the axis-exchange identity and the Jensen lower bound. All three are true statements with hand proofs on file ((TM): `library/gap-transfer.md` row 667, check 671, extended to rectangular boxes by Lemma 1.1 of `gap-seed-check.md`; the other two are one line each), but none is in Lean. (ii) The hand's Theorem D (a), (c)-(f), Corollaries D2, S2, S3 (the superseded block version) and Proposition R are not formalized; Stage 1 did not ask for them. (iii) The seed (SEED) itself is open, as row 1459 says.

**Verdict for W5: FAITHFUL.** No field is stronger than the hand proof uses; one field (`logConvex`) is redundant; two fields (`le_one`, `atThree`) are weaker than the hand setting. No field is false for the Wilson data at any beta > 0 under the dictionary above.

## Step 3. Faithfulness of U4 and W1

### U4 (`sequenceLemma`) against Lemma A2 of row 668 (`library/gap-os-equiv.md` lines 73-77) and design row U4 (`lean-gap-chain-design-fable.md` L637)

Hand: g_k = ||T_{kh} psi||^2 for a self-adjoint semigroup; A2.1 gives g_k^2 <= g_{k-1} g_{k+1} (k >= 1); ||T_{kh} psi|| <= C rho^k for infinitely many k gives g_1 <= rho^2 g_0. Scalar form: m = g, q = rho^2, envelope constant C^2. Lean hypotheses: `0 <= q`, `0 <= m n`, `m(n+1)^2 <= m n * m(n+2)` for all n (= A2.1 re-indexed), `∃ᶠ j in atTop, m j <= C q^j` (= "for infinitely many k"). Conclusion `m(n+1) <= q m(n)` for every n: the hand states n = 0; every n follows by applying the hand lemma to the shifted semigroup vector T_{nh} psi, and Lean proves it directly. The zero case A2.2 ("forward zeros" in the design) is derived inside the proof, not assumed. Nothing in the hypotheses is stronger than A2's; the semigroup itself is not formalized (the instantiation m_k = ||T_{kh} psi||^2 and the Cauchy-Schwarz step A2.1 are left to the consumer U5, as the design says). **Verdict U4: FAITHFUL.**

### W1 (`lemmaM1`) against Lemma M1 of row 1356 (`library/gap-mini-mneutral-fable.md` lines 86-99) and check row 1359 (`gap-mini-mneutral-check-astra.md` L15: M1 HOLDS)

Hand: B >= 0 Hilbert-Schmidt, sigma = sum_{i>=1} (mu_i/mu_0)^2; min over c > 0 and unit rank-one Q of ||B/c - Q||_HS^2 = sigma/(1+sigma). The direction used (Corollary M2 (i), "only if"): if ||B/c - |phi><phi| ||_HS <= delta for some c > 0, unit phi, then sigma/(1+sigma) <= delta^2, i.e. (1 - delta^2) Tr B^2 <= mu_0^2.

Lean: `HSNormLE A δ` := every finite orthonormal family v has sum ||A v_i||^2 <= δ^2. For a bounded A on a Hilbert space this is equivalent to ||A||_HS <= |δ| (every finite orthonormal family extends to a Hilbert basis, and the HS norm is the supremum over finite subsets of a basis; the Lean file proves the needed direction as `HSNormLE.sum_le`). `ketBra φ = rankOne ℂ φ φ`, x ↦ <φ, x> φ, the projection on φ. `((c⁻¹ : ℝ) : ℂ) • B` = B/c. Conclusion `(1 - δ^2) * Σ' Re<b_i, B(B b_i)> <= ‖B‖^2`: the sum is Tr B^2 in any Hilbert basis (summability of Σ||B b_i||^2 is the HS hypothesis), and ‖B‖ is the operator norm, which equals mu_0 for B >= 0 compact. So the Lean conclusion is exactly (1 - delta^2) Tr B^2 <= mu_0^2. Lean does not assume delta < 1 (for delta >= 1 the conclusion is trivial) or B ≠ 0 (hand's Lemma M1 assumes B ≠ 0 for sigma to be defined; the Lean form needs no sigma). `lemmaM1_hsSq` drops positivity too (true: the proof only uses Re<φ, Bφ> <= ‖B‖).

Gap between W1 and its consumer (not a faithfulness defect; it is design row W8): to read the conclusion as s(2w) <= delta^2/(1 - delta^2) for B = P_0 T^w one needs ‖B‖_op = lambda_0^w and Tr B^2 = lambda_0^(2w)(1 + s(2w)), i.e. the spectral theorem for the compact positive B. Not in Stage 1.

**Verdict W1: FAITHFUL** (the one direction the design asked for).

## Step 4. Non-vacuity: consumer file (written; build pending at 21:17Z)

Scratch project `/tmp/opus-1503-check.K2ISLt/proj` (Lean 4.33.1, the committed lakefile and toolchain, the replay's `lake-manifest.json` renamed to gapchain, `.lake/packages` symlinked read-only to the replay's packages, as in the RECEIPT). The copied GapChain sources have the SHA-256 values listed in RECEIPT.md (checked: identical). Consumer: `Check/Consumer.lean`. Contents:

- **A. `weight_logConvex`**: for every BoxSpectrum B and a >= 3, weight(a+1)^2 <= weight(a) weight(a+2) (Cauchy-Schwarz on partial sums with sqrt(r_i)^a, sqrt(r_i)^(a+2), passed to the limit, plus pointwise 2 r^(a+1) <= r^a + r^(a+2)). Hence `TorusData.mk'` builds a TorusData from `spectrum`, `cross`, `lower` alone.
- **B. An explicit TorusData** (`tunnelTorus`): every box R has top 1 and one excited ratio 2^(-xyz); weight_R(a) = 1 + 2^(-a x y z), i.e. Z(n) = 1 + 2^(-n1 n2 n3 n4), symmetric in all four sides (a two-level tunnelling model, T_R = diag(1, 2^(-xyz))). cross: exponent identity a (R[i:=b] volume) = b (R[i:=a] volume); logConvex: u^a (1-u)^2 >= 0; lower: d = 0 (log of a number >= 1). Seed: s = seed 3 = 2^(-648) > 0, < 1/5041. Applied: `theoremS` for every k, `corollaryS3'` at the non-dyadic side L = 13, and `seedRate 3` = log(2^648/5041)/3 > 0 finite (so the conclusion is a genuine finite positive bound, not the ⊤ case). Also `phi 3 <= 19/100000`, so the pressure alternative is non-vacuous too. Cross-check by hand: the true gap of cube L is L^3 log 2 >= 216 log 2 ~ 149.7, above seedRate = (648 log 2 - log 5041)/3 ~ 146.9. Consistent.
- **C.** U4 at m_n = 2^(-n), q = 1/2, C = 1; W1 on H = ℂ with B = 1, phi = 1, c = 1, delta = 0 (the test holds since c^-1 B - |phi><phi| = 0).

Memory: `memory_pressure` reported 39 then 36 percent free (five lean processes of another build running), below the 50 percent floor of the row; the build waits for the floor.

Note on W1 notation (added while waiting). Row 1356 section 2 says "Norms of operators are Hilbert-Schmidt norms", and the design row W1 writes the conclusion as "(1 - δ²) Tr B² <= ‖B‖²". Read with ‖B‖ as the Hilbert-Schmidt norm that conclusion would be trivial ((1 - δ²) Tr B² <= Tr B²). The Lean `‖B‖` is the operator norm of `H →L[ℂ] H`, which is mu_0 for B >= 0, so the Lean statement is the meaningful one that Lemma M1 gives. The design text should say "operator norm" there; the Lean file is right.

## Step 6. What instantiating TorusData on the Wilson data needs (for the next rows; not a faithfulness defect)

Under the dictionary of Step 2, a Wilson TorusData at fixed beta needs, for every box R = (x, y, z) with sides >= 3 (not only cubes):

1. **Rectangular transfer operators.** `cube_enlarge` passes through the non-cubic boxes (L, 2a, 2a) and (L, L, 2a), and `log_seed_le_phi` through (2n, n, n) and (2n, 2n, n), so `spectrum` must be the spectrum of T on rectangular slices. The release's transfer operator is `CubicPeriodSublattice.transfer` (cubic slices only), and Z = Tr T^t is in the release only at t = side (design file L246, L250: "Rectangular tori ... ABSENT"). Hand source: Lemma 1.1 of `library/gap-seed-check.md` (row 698). This is design rows W3/W10 and risk R4, already on file; Stage 1 does not change it.
2. **An eigenvalue sequence with multiplicity** (`ratio`, top counted once) for each such T: needs the spectral theorem for compact positive operators, absent from the release and Mathlib (design L247). Equivalently one may build `BoxSpectrum` from any enumeration of the nonzero spectrum; zeros pad.
3. **cross**: Z(a; R[i:=b]) = Z(b; R[i:=a]), the exchange of the time axis with axis i on a rectangular torus. Hand: one line (axis permutation preserves the plaquette set and the product Haar measure); not in the release for rectangular tori.
4. **lower**: Jensen, d = -6 beta (product of the spectator sides). One line by hand; needs log Z >= E_Haar(-beta A).
5. **logConvex**: no work, by `weight_logConvex` (Step 5).
6. **The gap** of the Lean `BoxSpectrum` is the gap on the whole gauge-invariant space, flux sectors included (as in the hand Theorem S). Any consumer that wants the neutral-sector gap only (row 1356's P_0) uses the same spectrum with fewer entries; Theorem S applies to it only if the restricted spectra still satisfy `cross`; that is not shown anywhere I read (a sector projection in the time direction is not obviously the image of one in a space direction under the axis exchange), so as it stands the TorusData route gives the full gap, not a sector gap. No Stage 1 statement claims otherwise.

## Step 5. Builds

**Independent rebuild of Stage 1** (22:39:37Z start, after memory_pressure read 52 percent free; numeric lock held by opus-1503-worker2): `lake build` in the scratch project, LEAN_NUM_THREADS=2, nice 10: rc 0, "Build completed successfully (3258 jobs)", wall 730.6 s (the machine was shared with another Lean build), maximum RSS 1,839,742,976 bytes. Every `#print axioms` line of the three modules reads `[propext, Classical.choice, Quot.sound]` (the same 49 lines as RECEIPT.md). Lake printed "manifest out of date: git url of dependency 'mathlib' changed" (the replay's manifest records a different URL form for the same rev 0df444a360ea); no update was run, and nothing was rebuilt in the packages. Log: `/tmp/opus-1503-check.K2ISLt/logs/build.log`.

**Consumer, run 1** (22:51:47Z): elaboration errors in my own file only (a `HasSum.mul` overload, `_` placeholders in two `positivity` terms, `norm_num` not closing (1/2)^648 < 1/5041, a parenthesis in the W1 statement). `u4_instance` compiled with the three standard axioms. Fixed; run 2 below.

