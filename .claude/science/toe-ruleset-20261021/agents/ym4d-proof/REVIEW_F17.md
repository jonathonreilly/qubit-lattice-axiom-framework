**Independent hostile review of F17.md**

Reviewer: Codex, fresh context, 2026-10-29. This is a same-family review
of Codex-authored work. I did not write F17.md. The earlier review
disclosed in F17_LOG.md was not used as mathematical evidence; only its
hash and terminal verdict were checked after the independent derivations.

**Disposition: LAND at the stated conditional scope.** No binding
mathematical defect was found. The actual Yang–Mills upper bound remains
UNDECIDED, and H_int remains OPEN. This review does not certify a
Yang–Mills estimate, a completed soft-RG construction, or retained-grade
audit status.

Line numbers below refer to the 397-line F17.md with SHA-256
b2a4f0f8650ff2db736acfaa1b0f30be1d30d449ceb827e32f55186b81e82440.
The supplied folder has no Git repository; no commit identity is inferred.
The reviewer brief, author brief and PROCESS_LIGHT were read.

**1. Exact law, observable and decomposition — CONFIRMED.**
Locations: F17.md:25–104, :314.
Fix: none.

Decision 4 at PROOF.md:2340–2344 and RLARGE.md:49–57 defines positive
normalized kernels. Integrating U_K, then U_(K−1), down to U_1 gives

    ∫ B(U_0) exp(−S_0(U_0)) ∏ K_i dU
      = ∫ B(U_0) exp(−S_0(U_0)) dU_0.

The same calculation without B identifies the partition functions.
Thus (1) preserves the bare-observable expectation. It does not identify
an auxiliary coarse link with deterministic blocking or with Wilson flow.

For any fixed finite history partition (2), multiplying by B≥0 and
integrating proves (3). The x-sum is inside the expectation bound;
there is no missing volume factor in this identity. An ordering of cuts
does give a measurable partition, but gives no localization or insertion
estimate. F17 expressly retains those obligations, including returned
and failed-return contributions. F17-SF-B is an additional bare-observable
estimate, not a consequence of kernel normalization.

**2. F17-2S and the weaker sufficient input — CONFIRMED conditionally.**
Locations: F17.md:47–64, :106–174.
Fix: none for the implication; the terminology clarification in item 9
would make its scope easier to preserve.

Summing (4), using F17-SF-B, u_k≥U_−(m), and monotonicity of H gives

    f_(K,R)(t_m) ≤ C_sf/u_k + W H(u_k)
                 ≤ C_sf/U_−(m) + W H(U_−(m)).

Since β_−>0, U_−(m)→∞. The right side tends to zero without any prescribed
power rate. A fixed integer m_1>m_0 can therefore be chosen with upper
mean at most A/2. TS-low and u_(K−m_0)≤U_+(m_0) give lower mean at least
A=c_−/U_+(m_0)>0. Both choices precede the cutoff and volume limits.

For the same joint subsequence, MOM2-B supplies
E[X_n 1_(X_n>M)]≤sup_n E[X_n²]/M. Truncating X_n at M, passing to the
joint-law limit, then taking M→∞ proves convergence of each first
moment. ALG-B and SHARP-B are explicitly retained to identify these
means with the same reconstructed vacuum pairings; first moments alone
would not establish that identification.

The comparator direction also checks. W_T0.md:220–285 defines its
calibrated magnetic class by a positive spectral measure and obtains

    f_mu(t) = (1/(4π²)) ∫ρ_M(ds)
                ∫_0^∞ v⁴ exp(−2v²)/sqrt(v²+ts) dv.

The ordered spatial tensor contraction is 4|p|²; radial integration and
v=sqrt(t)|p| give this formula. Its integrand increases when t decreases.
Hence t_1<t_0 implies z_0≤z_1, also for the allowed mixtures and constant
sectors. For y_0−y_1≥A/2,

    A/2 ≤ (y_0−z_0)−(y_1−z_1)
         ≤ |y_0−z_0|+|y_1−z_1|,

which proves the A/4 maximum-coordinate separation in (8).
This matches W_T0.md:458–525 and REVIEW_W_T0.md:24–71. It separates the
marked class; it does not identify that class with every free theory or
with the original e-only cyclic theory.

For (6), limsup S_n≤C_sf/U_−(m_1) and the displayed LF budget suffice
by addition. They give the same two-scale conclusion. They give no
all-grid ultraviolet conclusion. With (4) at every fixed label, the
bound first passes at that label; only afterward is m sent to infinity.
No moving flow time is interchanged with the continuum limit.

The rates at :166–174 are correct: at p=1/2, (5) is C v^(−c/2);
for p>1/2 it decays faster than every inverse power; for 0<p<1/2
it decays more slowly than every positive inverse power. The regular
C_sf/v term limits the asserted full TS-up exponent to α≤1.
The threshold c>2 is exactly the extra condition for H=o(v^−1)
at p=1/2, not for decay to zero.

**3. Countermodels to strict probability-rate necessity — CONFIRMED
as logical countermodels.**
Locations: F17.md:176–203.
Fix: none; retain the explicit exclusion of a Yang–Mills counterexample.

For each finite truncation, Σ_r 2^(−r−1)≤1, so the constructed B is
pointwise at most v^−α. It has the required mean bound and all positive
moments bounded. Nevertheless, with u=v+br,

    exp(−(log u)²) / [C exp(−a u)]
      = C^−1 exp(a u−(log u)²) → ∞

for every fixed a>0 and C<∞. The contributions are nonzero on their
events and still satisfy the asserted amplification upper bound.
Thus an amplitude upper bound cannot reverse the expectation inequality
to force these event probabilities. The lower-amplitude premise at
:200–201 would give the stated individual probability bound, but is
an additional premise and does not establish the strict exponent.

This directly answers the inference criticized at
CODEX_REVIEW_ASSEMBLY.md:51–57. It does not decide whether additional
geometry of actual surviving Yang–Mills concentrations forces a stronger
tail. F17.md:196–199 correctly leaves that issue open.

**4. F17-CRIT and the strict-exponent alternative — CONFIRMED.**
Locations: F17.md:205–257.
Fix: none.

Let r=k−j and b=β_− log L. From u_(k−r)≥v+br−R_F,

    L^(4r) exp(−a u_(k−r))
      ≤ exp(aR_F) exp(−av) L^((4−aβ_−)r).

This proves (10), including its additive-error factor, when aβ_−>4.
At aβ_−=4 the geometric decay disappears, but for
r≥r_0=ceil(2R_F/b), u_(k−r)≥v+br/2. Therefore

    Σ_r (1+u_(k−r))^(−s)
      ≤ r_0 + (1+v)^(−s)
           + ∫_0^∞ (1+v+bx/2)^(−s) dx
      = r_0 + (1+v)^(−s)
           + 2(1+v)^(1−s)/(b(s−1)).

This proves (12) for s>1, uniformly in depth. Multiplication by
exp(aR_F−av) proves the claimed LF bound. Its combination with C_sf/v
gives full TS-up for 0<α≤1, conditional on (9).

The weakness is strict in the stated estimate class. Every stronger
exponential exp(−a'u), a'>a, satisfies (11) after changing C because
(1+u)^s exp(−(a'−a)u) is bounded. Conversely the probabilities in
:245–249 satisfy (11) and violate every such stronger exponential.
Independent Bernoulli events realize equality in (9).

The moment qualification at :251 is essential and correct. In that
critical model,

    E[Y_r²] = exp(−av) L^(4r) (1+v+br)^(−s)

on the exact linear trajectory. These terms grow with r, so the example
does not supply a cutoff-uniform second moment. It proves strict-exponent
nonnecessity for the first-moment amplification estimate, not closure of
all W_T0 inputs. The coefficient 4 remains conditional on the unproved
observable amplification, not on spatial dimension alone.

**5. F17-COUNT — CONFIRMED obstruction to the specified estimate class.**
Locations: F17.md:259–305.
Fix: none; do not promote it to an obstruction to decision 4.

At fixed m, write C_m=U_+(m)+R_F. For r=floor(k/2), monotonicity of q
and the upper trajectory bracket give

    log(term) ≥ 4r log L − q(C_m+β_+r log L).

Since q(x)=o(x), the second term is o(r), proving divergence.
A fixed multiplicity of paid defects still gives a sublinear exponent;
fixed polynomial factors change its logarithm by only O(log r).
This polynomial observation applies to the sublinear-price case.
It must not be extended to the critical linear case, where item 4
shows exactly how a polynomial factor can restore summability.

For q(u)=a_eff u the lower bound (15) follows term by term. It diverges
for a_eff β_+<4 and grows linearly at equality. The use of β_+ here,
versus β_− in the sufficient upper estimates, is correct.
Fixing one physical time does not bound the number of finer RG levels.

The Bernoulli construction gives more than a divergent upper estimate:
choose any exact linear trajectory with β between the two brackets and
P(I_r=1)=exp(−q(v+βr log L)). Then

    E[Σ_r L^(4r) I_r] = Σ_r L^(4r) exp(−q(v+βr log L)),
    P(I_r=1 for all r in T) = ∏_(r in T) P(I_r=1).

Thus even product Peierls bounds and the stipulated amplification upper
control do not imply the desired uniform mean in this class. This is
an actual counterexample to that inference, not a lower bound on the
Yang–Mills observable. Larger paid clusters, variable cutoffs and better
observable response are explicitly left available at :298–305.

**6. Producer/review locators and missing interfaces — CONFIRMED at the
declared scope.**
Locations: F17.md:307–344, :379–384.
Fix: none. These are scoped source assessments, not a re-certification
of every upstream theorem or a claim about every file on disk.

| F17 location | Sources checked against the current bytes | Finding |
|---|---|---|
| :314 | PROOF.md:2340–2376; RLARGE.md:45–57 | Normalization and positivity are exact. D4-obs explicitly leaves observable comparison or sources open. |
| :315 | RLARGE.md:186–220, :385–415, :579–592; REVIEW_RLARGE_V3.md:27–69, :75–142 | RLF is an open target. The conditional forward-price result is bad-only/SU(2), with the future-tilt bridge, returned price and shadow costs still required. |
| :316 | LARGE55.md:232–260, :437–452, :475–529; CODEX_REVIEW_LARGE.md:100–120, :170–211 | Fixed-size counting failure does not exclude variable cluster rules. The final price must retain normalization, boundary and failed-return costs. |
| :317 | LARGE55.md:100–138, :285–312; CODEX_REVIEW_LARGE.md:21–69, :122–138, :193–213 | TL/PP and centered MIS/raw COL have conditional scopes. Scalar propagation, raw analyticity and unobserved-cone integration do not establish the needed localized, normalized insertion estimate. |
| :318 | LCONV55.md:373–430; CODEX_REVIEW_LCONV.md:23–33, :174–199 | Restricted negative-curvature calculations do not exclude every usable chart. Exact lowered-coupling identification and a completed one-step/tilted theorem are not available. |
| :319 | W_T0.md:392–452; REVIEW_W_T0.md:164–201 | Magnetic transport, moments and sharp-time identification remain separate. Neither the 4D flow nor a deterministic block witness supplies them automatically. |
| :379–384 | PROOF.md:1991–2007; HINT2_55.md:391–419; CODEX_REVIEW_HINT2.md:58–77 | The sources distinguish fixed chart cuts from logarithmic fluctuation cuts. The remembered instanton-shrinking premise is not a proved flow-survival input and is not used in F17's proofs. |

The normalization warning was also checked directly. Taking the
negative logarithm of a normalized kernel contributes
aφ_M(V)+log N_a(M), so the U-dependent normalizer cannot be discarded.
Moreover,

    exp(λaφ_M(V)) exp(−aφ_M(V))/N_a(M)
      = [N_((1−λ)a)(M)/N_a(M)] k_((1−λ)a)(V|M).

For Decision 4's uncentered SU(2) example M=rI,
N_a(rI)=exp(−a)H(ar), H(x)=E_Haar exp(x Re tr(V)/2).
H has a nonzero quadratic Taylor coefficient, so the normalizer ratio
is generally r-dependent. This verifies the warning without borrowing
a convexity theorem or confusing a minimized column action with φ.
Finally, sup_(u≥0) u^q exp(−(a−a_eff)u)<∞ for a_eff<a,
whereas u^q is unbounded for q>0. The exponent-loss statement is correct.

**7. Instanton normalization — CONFIRMED; probability interpretation
remains unproved.**
Locations: F17.md:346–378.
Fix: none.

In Euclidean four dimensions, the Hodge star preserves the two-form
norm. Expanding the square gives, for either sign,

    S = (1/(8g_std²)) ∫(F∓tilde F)²
          ± (1/(4g_std²)) ∫F·tilde F
      ≥ 8π²|Q|/g_std²

after choosing the sign of Q. Equality holds for the corresponding
self-duality condition. At |Q|=1 and u=2N/g_std² this gives
S_inst=(4π²/N)u. FLOW.md:24–40 and RLARGE.md:45–47 confirm the lane's
coupling dictionary and the stated one-loop slope convention.
Consequently (4π²/N)[11N²/(12π²)]=11N/3, while the actual lower-bracket
criterion is β_−>N/π². Positivity of β_− alone is insufficient.

The attribution was checked against Vandoren and van Nieuwenhuizen,
[Lectures on instantons, §2, equation (2.9)](https://arxiv.org/html/0802.1862v1).
It agrees with the action-square convention. The calculation above is
independent of that citation. No topological quantization theorem for
rough lattice fields, instanton measure, determinant bound or flow
survival assertion follows from it. F17 explicitly retains these limits.

**8. Achievability, outcome table and status discipline — CONFIRMED.**
Locations: F17.md:3–21, :334–344, :386–397.
Fix: none at this scope.

The deliverable meets both author tasks. It rejects a logical necessity
claim and gives explicit weaker sufficient estimates. It also proves
an obstruction to one available estimate class without treating that
obstruction as a no-go for the actual RG route.

The precise missing first-moment result is F17-SF-B together with
F17-WINS-B(2), for a specified actual-history partition under the same
normalized law and trajectory. Equation (4) is a stronger target, not an
already available Peierls estimate. An explicit event/amplification
decomposition plus the strict or critical exponential bound is another
sufficient route. The named producer reviews establish neither route
for the spatially flowed B observable.

Therefore UNDECIDED is the supported achievability verdict. A future
proof would discharge only the upper-bound part of the marked two-scale
reduction; the lower bound, moments, common algebra and sharp-time
identification would still be required. H_int for the original target
and a mass gap do not follow. The recommendation to investigate weighted
insertions is a research preference, correctly labeled ARGUED.
No audit or ledger status is upgraded by the note or by this review.

**9. Two wording clarifications — nonbinding.**

At F17.md:127–138, “minimal” and “irreducible” should be read relative
to the chosen regular-sector upper envelope, not as a theorem that (6)
is necessary. The actual S can be strictly smaller than
C_sf/U_−(m_1), leaving a larger permissible LF contribution. For example,
S=0 and LF=A/2 already meet the desired upper mean while violating (6)
whenever that envelope is positive. Suggested fix: “two-scale sufficient
version” and “sufficient LF budget using this regular-sector envelope.”
The surrounding sufficiency statements and F17_LOG.md already exclude
the stronger interpretation; no proved implication depends on it.

At F17.md:27 and :154–163, the grid notation t_m and the selected-time
notation t_0,t_1 overlap. The intended selected labels are clear from
the explicit adoption of W_T0's convention and the m_0,m_1 argument.
Suggested fix: use t^(m) for the grid and explicitly declare
t_0=t^(m_0), t_1=t^(m_1) before (8). In particular, the selected t_1
does not mean the grid point with index 1.

**Binding fixes: none.** LAND applies to the conditional reduction,
logical countermodels, critical summation, restricted counting
obstruction and normalization, with the open physical inputs preserved.

The prior-review hash and terminal verdict match F17_LOG.md; this is
provenance only. The author-source manifest contains 17 source pins.
Mechanical hashing and file-scope checks carry no physics evidence.
No numerical experiment, worker, audit action, source correction or
commit was performed. This review writes only REVIEW_F17.md.

VERDICT: LAND
