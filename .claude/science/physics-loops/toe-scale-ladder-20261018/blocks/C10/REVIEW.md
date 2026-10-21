# C10 review: burn-and-turn source tensor on the C7 walk vs the C8 couplings

**Reviewer provenance.** A Claude subagent, same model as the author. Separate context and own code,
but not an independent-family review. Single reviewer. No commits.
**Scope read.** C10 `NOTE.md`, `WORKLOG.md` (pre-registration and log), `scripts/` and `logs/` (in full).
The burn-and-turn (BT) note on `origin/claude/gravity-burn-turn-source-tensor-20261021` (read as data).
C7 `NOTE.md` §0–§3, C8 `NOTE.md` §0–§1, and the parent walk note (Theorems 1–4, for G(b)).
**Evidence.** `review_scripts/r10_walk.py` rebuilds the walk from the parent's G(b). It computes u\* by its
own root of det G, the f row as Gφ₀, and the h rows by eigen-factorising G − (Gφ₀)(Gφ₀)ᵀ. It does not
reuse the author's code. `review_scripts/r10_review.py` writes `review_scripts/logs/r10_review.log`, which ends
**TOTAL: PASS=21 FAIL=0** (9 s, one core, nice 10). One debug run, kept in the scratchpad and not logged, gave 20/1. The one
failure was my own overlap check: I used the spectral norm, while the author's 0.16–0.23 is a
basis-dependent max-element measure. The check was reworded to state this (see 1c). After that the
reviewer's spectral-norm value and the author's element value were both reproduced.

## Verdict table

| # | claim | verdict | severity |
|---|---|---|---|
| 1a | BT as defined needs shift-coin form; C7 walk is not of that form | **correct with fix** | minor |
| 1b | 27 nonzero hops, rank sum 92 | **correct** | — |
| 1c | overlaps max \|A_nA_m†\| ≈ 0.16–0.23 | **correct with fix** (basis-dependent measure) | minor |
| 2a | E-K, E-W are declared extensions, reduce to Born odds on shift-coin walks | **correct, honestly labelled** | — |
| 2b | E-K mean step ≈ 15% of v, rel. dev ≥ 0.63 | **correct** | — |
| 2c | E-W mean = v exactly; weights complex, \|Im w\| up to 0.62, Re w down to −0.68 | **correct** | — |
| 3a | ⟨α_i⟩ = g_i/sin ω for every band vector | **correct** | — |
| 3b | T^{BT,W} = ωDD/sin²ω, T^{M1} = ωgg/sin²ω (and M2–M4 forms) | **correct** | — |
| 3c | D − λsg = sin k_a[E₁(x_b+x_c)+E₂x_bx_c], E₁(θ=0) = −3β, β = C7's k⁴ coefficient; C(b_iso) | **correct** | — |
| 4a | continuum order: all four agree up to s²; as given T^BT = s²T^X | **correct** | — |
| 4b | O(a²): only M1, only at massless b_iso; massive fails at registered constant | **correct** | — |
| 4c | "selects M1 at b_iso" as a BT result | **correct with fix** (wording) | moderate |
| 5 | clock fails at rest: E-K action/θ = 0.54/0.52/0.64 | **correct with fix** (small formula slip) | minor |
| — | c_G, a/l_P quoted from C8 | not rechecked here (C8 review) | — |

## Details

**1a. Domain.** The BT note's supplied model is: "components labelled by step directions d … each component
moves one link along its d", with U(k) = diag(e^{−ik·d})C. So the requirement is shift-coin form, where each
component label carries one hop vector. The C10 note and its runner message ("≤ 4 unit-length hops") also ask
for **unit length**. That is stricter than BT. The BT note's own eight-direction walk uses body diagonals,
which have Euclidean length √3 in Z³ and are one link of the D4 carrier. *Fix:* state the condition as
"A_n = Π_nC with orthogonal Π_n (rank sum 4, A_nA_m† = 0)" and drop "unit-length". The conclusion does not change.

I also added a basis-free certificate. For a shift-coin walk, U(k)U(0)† = diag(phases) for all k, so these
operators commute pairwise. For the C7 walk, max ‖[U(k)U(0)†, U(k′)U(0)†]‖ ≈ 1.9 at all three points, massless
and massive. So no constant internal basis gives the shift-coin form (R1). *Caveat (unverified, low severity):*
neither party tested whether U factors into shift-coin **sub-steps**. Such a factorisation would be a
different tick, so it is outside "BT as defined". The note's claim is restricted to one tick, and this caveat
should be stated.

**1b/1c.** I reproduce 27 nonzero hops and rank sum 92 at every point and mass setting (rec 1e-15).
The basis-invariant overlap ‖A_nA_m†‖₂ is 0.232 (b\*), 0.254 (b_iso) and 0.234 (b_gold). It is exactly
θ-independent, because A_n(θ) = M A_n(0) M with M unitary. The author's 0.159/0.173 are the max element in the
author's basis: I get 0.159 at b\*, θ = 0. That number is basis-dependent, which is why it "varies with θ".
*Fix:* quote the invariant norm, or label the measure.

**2. Extensions.** Both are declared in the WORKLOG pre-registration as the author's choices. Both reduce
to |u_d|² on shift-coin walks: analytically, Π_dCu = e^{−iω}e^{ik·d}Π_du; numerically, R2e. Over the declared
momentum set with random band vectors:
- E-K: |m|/|v| is 0.127–0.174 (mean 0.157) for massless members, and the min relative deviation is 0.638. This
  confirms "≈15%" and "≥ 0.63".
- E-W: mean − v ≤ 8e-9 (finite-difference limited), max |Im w| = 0.623 and min Re w = −0.679. This confirms the claims.

E-W is honestly called a continuation rather than the rule. I agree it does not count as "applying BT": its
"flows" 2εww′/ρ are complex.

**3. Identities (eigen-route, 50 digits).** v is the numerical derivative of the eigenphase of the explicit
4×4 matrix (mpmath eig), and ⟨α⟩ comes from random band eigenvectors. Results:
- ⟨α_i⟩ − g_i/sin ω ≤ 1.5e-50.
- v sin ω − [λsg + sin k(E₁(x+x)+E₂xx)] ≤ 4e-51, at 3 points × 4 mass settings (including a generic
  χ = 0.7) × random k, with c_i taken from my own h rows.
- Independently, the Σk⁴ coefficient of ω² from my own series is −s(b₀−b₁−2b₂)/3 exactly. This is β, C7's
  anisotropy coefficient (C7 §4, parent Theorem 7).
- E3 holds as a polynomial identity in (c, b).
- C(b_iso) = (10√10 − 32)/27.

The tensor forms follow from C8's definitions: T^X = ⟨V^X⟩, ρ = ω/sin ω, and Hellmann–Feynman on the degenerate
band, since H_a² = ω². I checked these by hand, and R4 uses the eigen-route quantities.

**4a/4b.** Reproduced:
- The as-given deviation is 1 − s² (0.1638, 0.3333, 0).
- The κ⁴ xx coefficient of g g − DD/s² along (123) is 0.0080184 vs 3βn₁²(n₂²+n₃²) = 0.0080187 (b\*), and
  0.0096766 vs 0.0096769 (b_gold). It is 9e-9 at b_iso, i.e. O(κ⁶).
- Slopes: M1 2.00 (b\*, b_gold), 4.00 (b_iso); M2–M4 2.00 along (123) at all points.
- Axis: exact agreement (1e-49).
- b_iso along (111): M3 and M4 have slope 4.
- Massive b_iso, M1 at constant s²: slope 1.00 when Wilson-aligned, 2.00 at maximal twist.

**4c. Is "selects M1 at b_iso" honest?** The arithmetic is right. The attribution needs care:
- By E1, BT's plane-wave tensor is εmm for **any** odds. Under E-W, m = v by construction, so
  T^{BT,W} = ωvv is the plane-wave dust tensor. Every rule whose mean step equals v gives the same tensor.
  The turn mechanics contribute nothing beyond this.
- The comparison with M1 is then exactly v vs s⟨α⟩, because T^{M1} = ω⟨α⟩⟨α⟩. So the O(a²) selection is a
  kinematic property of the walk, "v = s⟨α⟩ + O(k⁵) iff β = 0". It is not a property of burn-and-turn.
- It also depends on: the extension choice (E-K selects nothing, failing at continuum order); the shape
  relaxation by 1/s² (as given, nothing is selected unless s = 1); the candidate set M1–M4; q = 0 plane waves
  only; and fixing the constant at continuum order (an energy-dependent constant would tie M2, since
  T^{M2} = (sin ω/ω)T^{M1}).

The note does say "everything below concerns … the dust tensor εvv", and its §6 flags E-W. But Result 5 and the
Outcome present it as "the selection" and quote c_G and a/l_P next to it. *Fix:* reword Result 5 as "the
plane-wave dust tensor (equal to the E-W continuation of BT) agrees with M1 through O(a²) iff β = 0, i.e. at
massless b_iso. This does not depend on the turn rule. BT as defined selects nothing (outside its domain)." Quote
c_G only as "the M1 value, if M1 is adopted".

**5. Clock.** At rest ω = θ to 1e-6, and ⟨|n|²⟩_K = 0.5389/0.5195/0.6401, band- and θ-independent to 1e-10. The
action/θ is 0.537/0.518–0.520/0.638–0.640, far from 1, so the failure is confirmed. *Slip:* the E-K mean step
at rest is not zero (|m_K| up to 0.048, a spurious rest drift of E-K). So the action is θ(⟨|n|²⟩_K − |m_K|²),
not θ⟨|n|²⟩_K. The difference is ≤ 0.3%, and the runner's printed range [0.5184, 0.6401] already contains it.
*Fix:* correct the formula and mention the drift.

## Overall

The load-bearing identities and numbers reproduce by an independent construction. The domain verdict holds; the
fix is to drop "unit-length". The open issue is one of attribution: the M1-at-b_iso result belongs to the dust
tensor, i.e. to the walk's kinematics, not to burn-and-turn. **Ready after the minor fixes and the 4c rewording.**
