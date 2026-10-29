# Independent hostile review of W_T0

Reviewer: Codex, fresh context, 2026-10-29. This is a same-family review of
Codex-authored work. I did not author the note. The earlier reports in
W_T0_LOG.md were read as required, but their verdicts were not used as
mathematical evidence.

No binding correctness defect was found in the **scoped conditional
reduction**. This does not establish T_OS, construct the common Yang–Mills
OS system, or discharge ASSEMBLY55 F1 for the original e-only theory.

Source identity: checkout HEAD
`fcdd32c83bc5aed08ef4f3aa5da512e668d8b216`; fetched `origin/main`
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
The reviewed W_T0.md has 784 lines and SHA-256
`eaf064445948aed7096e7d4e53c20ed4407d1c87458943feb52f3d7638f2e804`.
W_T0_LOG.md has SHA-256
`0d6cac09733448908c4be4fae5d80e137387fcc4ed97154a873df8fe5eb4b324`.
All thirteen dependency hashes listed at W_T0_LOG.md:100–112 match the
files inspected. Line references below bind to these bytes. Current
repository reviewer guidance was used; its relevant methodology files
match the fetched main revision. Planning supplies no scientific status.

1. **Theorem T0-OS — CONFIRMED as the stated conditional implication.**
   References: W_T0.md:458–525, supported by :124–214 and :220–308.
   **Fix: none at this scope.** The original requested one-point inequality
   and an unmarked non-freeness conclusion must not replace the theorem
   actually proved here.

   The line-by-line dependency check is:

   | Lines | Check and verdict |
   |---|---|
   | 458–462 | ALG-B, SEQ and F-B are explicit additional premises. The four named YM inputs alone are not claimed to construct a common OS theory. Correct. |
   | 464–477 | U_+(m_0) is finite and positive; hence A>0. U_-(m) grows without bound and ϑ−1<0, so a finite m_1>m_0 satisfies (25). Both physical flow times are fixed before either limit. Correct. |
   | 479–491 | The conclusion is separation from the marked class 𝔉_B. It expressly does not identify that class with OWN-free. Correctly narrowed statement. |
   | 495–501 | The lower bound uses u_(K−m_0)≤U_+(m_0); the upper bound uses u_(K−m_1)≥U_-(m_1) and the negative exponent. Thus y_0≥A and y_1≤A/2 on every sufficiently fine admissible cutoff, uniformly in R. No inequality is reversed. |
   | 502–505 | MOM2-B gives uniform integrability of the first moments on the same jointly extracted sequence. For every fixed grid index the upper bound passes; taking that index to infinity gives the UV limit. This is not an interchange of a moving flow time with the cutoff limit. |
   | 507–513 | B-boundary supplies a vector with the limiting-law second moment as its squared norm. ALG-B and SHARP-B supply its identification with the common reconstructed system. This identification is assumed explicitly, not inferred from tightness. |
   | 515–517 | Every allowed comparator has z_0≤z_1. Therefore its positive-part witness is zero, while the YM witness is at least A/2. Correct, including the specified mixtures. |
   | 518–522 | Independently, the max-norm distance of (y_0,y_1), with y_0>y_1, from the cone z_0≤z_1 is exactly (y_0−y_1)/2, attained at equal midpoint coordinates. This verifies the A/4 constant in (28). |
   | 523–525 | A vacuum-preserving equivalence preserving the marked vectors preserves their vacuum pairings, so it cannot identify the two systems. Correct only with that marking. |

   In particular, the Hilbert-vector step survives scrutiny. At each
   cutoff let I_j(u) be the positive half-integral of exp(−S_+) at fixed
   boundary links u. The boundary marginal is proportional to I_j(u)^2,
   and let C_jF be the corresponding normalized conditional half-integral
   of F. Then

       q_j(bF,bF) = E_boundary[|b|² |C_jF|²]
                  ≤ ||b||_∞² q_j(F,F).

   This also holds when F is a finite sum of boundary-multiplied tests.
   Hence bounded boundary multiplication respects null vectors. Bounded
   mixed Gram entries can be extracted simultaneously with the original
   e-form. On boundary-only vectors the limiting form is L²(ν), so
   χ_M(X) converges in that form to X whenever ∫X²dν<∞. This verifies
   :169–170 without treating ordinary coincident e-moments as finite.

   The tail estimate E[X_j 1_(X_j>M)]≤C/M gives convergence of the means,
   and truncation of x² gives ∫X²dν≤C. Neither argument gives convergence
   of E X_j². The rare-spike example at :147–150 correctly exposes that
   distinction. Thus MOM2-B yields the boundary vector under the stated
   joint-limit/RP premises; **its identification with the reconstructed
   positive-time observable still uses ALG-B and SHARP-B**. Its vacuum
   pairing is then exactly the number used in the separation theorem.

   The answer to “is this the free class T_OS names?” is **not established**:
   ASSEMBLY55:128–135 leaves OWN-free open. W_T0.md:488–491 and :779–782
   state that limitation. There is no inference to non-freeness under an
   arbitrary observable identification, or to the original e-cyclic theory.

2. **ALG extension — CONFIRMED as an obstruction analysis and conditional
   compatibility result; the actual extension remains OPEN.**
   References: W_T0.md:565–745; OSLEAF55:148–209, :292–337, :484–517.
   **Fix: none for the stated result.** Before treating this as an actual
   common YM algebra, supply the four interface obligations at :660–702,
   the sharp-time identification, and any stricter locality demanded by
   the consumer.

   The e-test domain is a partial algebra of flat-on-collision Schwartz
   tests. Neither a time delta nor e(f)² belongs to it merely by notation.
   The boundary module avoids this error: it defines new bounded boundary
   multipliers and their joint moments, while leaving the e-domain intact.
   The constant Cartan-curvature example at :578–588 distinguishes B from
   the scalar e-data on the stated smooth configuration domain; it is
   correctly not promoted to a theorem about a state-specific Hilbert
   closure.

   A distant compact perturbation of a smooth abelian connection can change
   its spatial heat-smoothed curvature at the center. This verifies the
   failure of strict compact spatial support. A tilted full hyperplane has
   times of both signs, so a positive center time does not make its full
   observable an element of the original positive-half cone. These are
   real support restrictions, not rotation bookkeeping.

   Equation (31) is a consistent E(4) action on the enlarged labels.
   Its classical realization at :618–624 is correctly conditional on
   existing unique flows. The parallel-slice subgroup, spatial unitary
   action, positive-time semigroup, and need for rotated copies are
   distinguished correctly at :626–645. Exact finite-lattice rotations do
   not supply a dense continuum rotation action or invariance of mixed
   tests.

   Given the specified continuous common maps and bounds, the closure
   proof at :704–719 is valid: bounded-coordinate extraction and density
   preserve OS0; the assumed mixed symmetry defects and continuous action
   give OS1; finite positive Gram limits give OS2; compatible permutation
   and reality identities give OS3. The proof assumes the interface
   estimates. It does not produce them from the magnetic second moments.
   A completion containing full-slice B is also not a strictly local
   witness in a fixed compact region. The warning at :732–737 correctly
   retains the need for comparator-uniform localization if that stronger
   consumer is to be met.

3. **Provable-now items and normalization — CONFIRMED.**
   References: W_T0.md:90–214, :251–334, :527–559.
   **Fix: none.**

   Compactness of the finite link manifold and smoothness of the flow give
   global finite-time cutoff existence. Three spatial plaquettes, each
   with 0≤Re tr(1−V)≤2N, give precisely 12Nτ². The site-reflection
   factorization works because no plaquette crosses a fixed site plane;
   the boundary density is reflection-fixed. Its squared Hilbert norm and
   vacuum pairing are therefore ω(B²) and ω(B). The growing cutoff bound is not mistaken
   for a continuum estimate.

   An independent comparator contraction uses the magnetic vector
   H_i=(1/2)ε_ijk F_jk. At mass s its covariance is
   (|p|²δ_ij−p_i p_j)/(2√(|p|²+s)), whose spatial trace is
   2|p|²/(2√(|p|²+s)). The energy in (12) is
   (t²/2)Σ_i (K³_t*H_i)^T M(K³_t*H_i). The heat factors, radial measure
   and v=√t|p| substitution consequently give

       f_B(t) = (1/(4π²)) ∫ρ_M(ds)
                    ∫₀∞ v⁴ exp(−2v²)/√(v²+ts) dv.

   The zero-mass radial integral is 1/8. The kernel is comparable to
   min(1,σ^(−1/2)), decreases with σ, and increases to 1/8 as t↓0
   at each fixed s. These facts verify the exact integrability condition,
   monotonicity and possibly infinite UV limit, including the restriction
   to observed colors. Diagonalizing a finite Gaussian quadratic form as
   Σ_i λ_i Z_i², with independent standard normal Z_i, gives its second moment
   (Σ_iλ_i)²+2Σ_iλ_i²≤3(Σ_iλ_i)², verifying the vacuum-domain claim
   independently of a formal expectation alone.

   Direct plaquette expansion gives
   2 Re tr(1−V_ij)=a⁴Σ_a(F_ij^a)²/2+o(a⁴).
   Matching the Wilson action coefficient gives g_std²=2N g_FLOW².
   Hence the tree coefficient is
   N(N²−1)g_FLOW²/(16π²), as at :315–316. This agrees with the actual
   convention in FLOW:24–26 and corrects HINT2_55:302 and the separate
   trajectory dictionary defect identified in CODEX_REVIEW_OSLEAF:47–59.

   The Maxwell covariance at :544 exactly matches any prescribed
   positive single-scale value. Thus the universal one-point gap fails
   for the class allowing arbitrary normalization; the displayed two-scale
   replacement supplies a valid separation instead. Ordinary
   ordered positive-time tests also have reconstructed vacuum pairings,
   so the correction of the word “only” is justified. The optional L⁴
   inter-scale bound follows from monotonicity of the total spatial flow
   action and translation invariance, with the displayed factor retained.

4. **Open YM inputs and producer matches — CONFIRMED as open obligations.**
   References: W_T0.md:343–452; ASSEMBLY55:294–298, :494–497.
   **Fix: none.** Retain the distinction between a proposed sufficient
   producer and an already proved input.

   MOM2-B quantifies second moments on the same trajectory and common
   hierarchy; (TS-up)^B and (TS-low)^B have the needed depth and
   volume-uniform quantifiers. SHARP-B explicitly requires a Hilbert-norm
   boundary limit identified with the same truncation law. It is stronger
   than a finite one-point value. The all-grid formulation, rather than
   merely the two selected scales, is used for the full UV assertion.

   The source distinctions are accurate:

   - SRCCD55:339 and :354–368 concern local e-sources and separated
     conditional cumulants, not the coincident magnetic square.
   - EXISTENCE:617–633 leaves H-src-flow open for spacetime-smeared
     four-dimensional flowed fields. It supplies no sharp-time B theorem.
   - EXISTENCE:235–247 gives the stated H-Bal-1 provenance and unresolved
     volume/SU(N) extensions. The corrected section locator is right.
   - EXISTENCE:1137–1155 and :1205–1229 put H-loc-LF and LF-P on the
     deterministic S4c block law. They do not transport that bound to
     fine concentrations surviving the magnetic flow.
   - HINT2_55:391–419 proposes SRC/FLOW-BLK, anti-concentration and
     LF-inst routes; CODEX_REVIEW_HINT2:58–77 explicitly limits the
     alleged necessity of LF-inst. W_T0 preserves that correction.

   The geometric-series thresholds c_LFβ_->4 and, for the stated L²
   triangle method, >8 follow from their respective assumed amplification
   bounds. They are sufficient within those assumed decompositions;
   no necessity for the actual YM estimates is established. The instanton
   convention conversion is correct and used only conditionally.

   The easier/harder discussion is appropriately limited: the moment
   exponent comparison depends on δ; temporal support helps RP; removing
   time smoothing leaves a separate UV/domain problem. No inequality
   comparing the two different random fields, or ordering of the full
   proof difficulties, is asserted.

5. **Hidden imports — no unlabelled load-bearing physics or reconstruction
   theorem found.** References: W_T0.md:220–245, :401–452, :739–745.
   **Fix: none.**

   The positive spectral class is defined, not deduced by importing an
   interacting tensor Källén–Lehmann theorem. The probability-law limit,
   boundary quotient, comparator integral, moment estimate and separation
   were checked directly. HINT2's remembered flow-survival claims are
   explicitly unused. Balaban/Dimock estimates and full multi-field
   OS-to-Wightman reconstruction remain outside the proved block.
   The abstract of [Kravchuk–Qiao–Rychkov](https://arxiv.org/abs/2104.02090v2)
   was inspected for orientation only; no theorem from it is used to
   discharge an obligation in this review.

6. **Consumer match — quotations CONFIRMED; fulfillment is explicitly
   partial and conditional.** References: W_T0.md:747–764.
   **Fix: none at the declared scope.** Do not report the downstream
   requirements as discharged merely because this review returns LAND.

   All six quoted excerpts match their sources after only whitespace,
   Markdown emphasis and table-pipe escaping are normalized:

   | Note line | Source | Actual handoff |
   |---|---|---|
   | 755 | ASSEMBLY55:199–202 | Finite-moment continuous separation with a uniform margin, conditionally. Strict locality and the original e-only identification remain open. |
   | 756 | ASSEMBLY55:390–400 | A boundary-vector mechanism and enlarged-system reduction. The quoted e-only implication remains unproved. |
   | 757 | PANEL_P1:63 | Zero on 𝔉_B, positive on the hypothesized YM limit, with no auxiliary soft noise. This does not settle OWN-free or the common local-system requirement. |
   | 758 | CODEX_REVIEW_P4:286–296 | Two fixed physical scales and a conditional uniform margin. The sphere construction, mixed covariance, matched trajectory and radius-uniform estimates remain prerequisites. |

   ASSEMBLY55 N15's open status and F17's heading are quoted accurately.
   The theorem's narrower class is not silently substituted for the
   unresolved owner choice; the nonlocal full-slice observable is not
   certified as PANEL_P1's strictly local witness.

**Binding fixes: none.** LAND means the reduction and the provable-now
items are correct as scoped, with the YM inputs and the additional common
algebra/identification obligations still open. It grants neither retained
science status nor closure of the original T_OS objective.

Verification limits and recovery: the complete W_T0 argument and its log
were read, along with the named consumer passages and necessary source
premises identified above. Truncated broad source output was not used as
complete verification; required passages were retrieved in bounded ranges.
No numerical experiment, inherited runner, formal proof checker, audit or
commit was performed. The quoted proofs were checked mathematically;
hashes and quotation checks establish provenance only. Only
REVIEW_W_T0.md is written by this review; no editable prompt, source note,
log, skill or ledger is changed. Resume from the source hashes above and
reopen affected findings if those bytes change.

VERDICT: LAND
