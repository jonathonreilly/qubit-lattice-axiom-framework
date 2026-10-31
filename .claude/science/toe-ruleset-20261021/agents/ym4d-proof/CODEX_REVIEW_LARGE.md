# PRE-STATED

UTC start: 2026-10-29 04:48:15 UTC.

Independent hostile review of `LARGE55.md`, with the owner’s requested cross-family role. Before derivation I have read the task, the science workflow, and a string-index of LARGE55’s headings/claims/errata. I have not yet read the proofs. No version-control operation will be used. This is the sole writable deliverable.

Targets and pre-stated refutations:

1. Rebuild TL, PP, LF-UV and LF-diff. A missing domain, normalization, source-uniformity hypothesis, or a purported removal of a requirement that merely moves it upstream refutes the stronger interpretation.
2. Rebuild DENSE and NOFREEZE from a conditional finite-energy argument, lattice packing and exact constants. Test the distinction between many defects and positive density; between lower and upper bounds; and between a fixed-size frozen cluster and every possible freezing policy. Check the reading of the cited three-dimensional construction.
3. Rebuild MIS, COL and PRICE, tracking conditioning, future kernel dependence, constraints and effective-density normalization. A legal future factor preventing the asserted integration, or a missing chart/coercivity implication, refutes an unconditional replacement.
4. Rebuild KA with a correctly normalized holomorphic kernel, its complex modulus, the number of coarse links and the relevant activity norm. An analytic function without the asserted uniform bound does not discharge RLF-5.
5. Check each of the eight inherited REFUTED items against its actual statement, including the overriding errata. Check TS-up’s quantifiers and what a divergent upper bound can establish.
6. Inspect the two cited checks for independently discriminating criteria, exact arithmetic, exhaustive domains and wrong/stale constants. Verify locating strings rather than relying on inherited line numbers.
7. Assess I1-I11 and the recommendation on substantive missing theorems, not row counts. A dropped wall that reappears inside an unproved representation is not a discharged obligation.

Verdicts will be CONFIRMED / NOT-VERIFIED / REFUTED; claim statuses PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. A CONFIRMED conditional lemma will state its hypotheses. Numerical corrections will include exact derivations. Findings will be appended during the review, followed by a summary table, bankable results and an explicit route verdict.

Read budget: named scientific sources only, targeted ranges for large files; the two discretionary scientific reads are reserved for the implementations `checks/lg55_1_dense.py` and `checks/lg55_2_s4p.py`. Entry-point methodology/procedure instructions are read only to honor the supplied operating contract. No snapshots or audit ledgers.

## Finding F1 — omitted normalizer in the claimed soft action

**Verdict: REFUTED** for the identity called the “total soft action”; the proposed background/Hessian replacement is **GAP** until corrected.

Attaches to `LARGE55.md:272`, locating string “total soft action S + Σκu φ”, and §5.4’s one-step positivity argument. `PROOF.md`, “Decision 4: the RG kernel” (observed lines 1851–1855), defines a NORMALIZED kernel. Its exact negative log at fixed V is

    S_eff(U; V) = S(U) + Σ_c [t φ_{M_c(U)}(V_c) + log N_t(M_c(U))].

The last term depends on U. Stationarity of S + Σtφ does not imply stationarity of this action, and its Hessian is not the conditional Hessian. This is an algebraic defect, not a request to assume more convexity. The source itself explicitly differentiates log N in “D4-norm (3) Derivatives” (observed lines 1874–1877).

A direct witness: take SU(2), M=rI, V=I, and q(V)=Re tr(V)/2. Write H(x)=∫exp(xq(V))dV. Then N_t(rI)=exp(−t)H(tr), and the exact kernel contribution is −tr+log H(tr). Its derivative in r is −t+t⟨q⟩_{tr}, whereas the displayed unnormalized contribution has derivative −t. For r,t>0, ⟨q⟩_{tr}>0: pair q with −q under V↦−V to obtain a strictly positive integral of q sinh(trq). The missing derivative is therefore genuinely nonzero. M=rI is an admissible average of SU(2) matrices (average exp(±iθσ_3), r=cos θ). No numerical integration is used.

The elementary Taylor identity at a critical point survives for the CORRECT action. A proof of chart-uniform positivity and BFT-coer for that action remains necessary; the unnormalized identity cannot supply it.

## Finding F2 — valid MIS and COL do not supply their advertised unconditional interfaces

**Verdict: CONFIRMED** for MIS’s centered-exponent tail and COL’s stated integration identity; **NOT-VERIFIED** for the geometric/pointwise replacements in §6.3. Claim status: **PROVEN** for the identities, **GAP** for those interfaces.

Attaches to `LARGE55.md:285–312`, strings “Lemma MIS”, “Lemma COL”; §6.3 steps 2–5 and E13–E15. Re-derivation: the Haar ball of radius 1/t about a maximizer gives N_t≥e^(−tφ_min−1)c_N t^(−D). Therefore k≤e c_N^(−1)t^D e^(−tψ). Conditional link independence gives MIS, and iterated conditional expectation gives its multistage version under the PLAIN chain. For COL, integrate the terminal outputs first; each kernel has integral one, and forward closure prevents a surviving non-cone kernel from reading an integrated variable. These are valid for every fixed N.

MIS bounds ψ≥δ, not automatically “non-chart curvature”. At M=0, ψ is identically zero and every positive-δ event in MIS is empty, while the coarse link is Haar. A check of the kernel’s own exponent cannot certify a geometric mismatch without a separate implication. The chart case needs quantitative nondegeneracy of M, a strict chart margin, and an explicit implication from a bad coarse plaquette to a link with ψ≥δ. E15 only supplies a non-strict radius inequality and cites the deterministic S4′ map; `PROOF.md`, “S4′ [S3] Order-averaged averaging” (observed lines 807–812), defines that map by averaged LOGS, whereas Decision 4’s M is the ARITHMETIC contour mean. Transferring a curvature bound between them is another needed derivation.

COL requires F to read no cone variable. Fixed top fields, source insertions there, cone-reading indicators, and normalized activities need separate treatment. MIS under the plain law also does not give a density bound conditional on an arbitrary future V: conditioning can force a rare mismatch. This does not restore KS-N as mathematically mandatory, but its replacement is not just the displayed tail lemma.

E13 correctly retracts zero shadow cost. Even its constant boundary-cost assertion is unproved. Exact integration of unobserved raw kernels does not compare a history with the small-field reference or control polymers crossing its boundary. I5 remains substantive.

## Finding F3 — KA is correct for raw integrals; the returned-activity conclusion is not established

**Verdict: CONFIRMED** for KA and KA-1 as raw-integral statements; **REFUTED** for the claimed general implication to normalized/signed returned activities and the exact square-root sufficient window. Claim statuses: **PROVEN** for KA/KA-1; **GAP** for RLF-5 and IV6’s claimed reversal.

Attaches to `LARGE55.md:318–354`, “KA-1”, “KA-2”, “the same holds per link for every returned polymer”; §5.2 row 16; §6.3 step 3; IV6–IV7. The actual antecedent is narrower than the conclusion:

    |R(We^X)| ≤ exp(t(cosh r−1)|C|) ∫|F(U)| K(W,U)dU.

Re-derivation: with A=W* M, the real exponent change is t Re tr((cosh X−I)A)/N. Since cosh X−I is positive semidefinite and ||A||≤1, it is at most t(cosh||X||−1). Integration proves the displayed total-variation bound. For t=κ/g² and r=ρg/√κ, t(cosh r−1)≤(ρ²/2)cosh r. This is a useful, uniform envelope for arbitrary fine fields.

But replacing ∫|F|K by R(W) requires F≥0. Sign-changing connected activities and Taylor-subtracted remainders do not inherit that positivity. More decisively, `PLD.md:497–502`, “The frozen activity r_Y = Num_Y/Den_Y”, explicitly identifies denominator zeros as the obstruction. LARGE55 IV7 admits it did not read this paragraph. KA proves analyticity and an upper modulus bound for Num and Den separately; neither provides a nonvanishing bound for Den, a logarithm, or their ratio. V-dependent cut indicators and background-dependent domains also need justification before KA-1 applies.

A discriminating exact model for the missing zero-free implication is SU(2): put H=diag(i,−i) and take the positive mixture D(V)=[k_t(V;H)+k_t(V;−H)]/2. With q_H(V)=tr(V^(-1)H)/2, D(V) is a positive constant times cosh(t q_H(V)). On SU(2) it is strictly positive. At W=I, X=diag(r,−r), q_H(We^X)=−i sinh r, and D vanishes at

    r = asinh(π/(2t)).

The numerator k_t(V;H) does not vanish there. Thus a positive sum of normalized kernels can have quotient poles at scale 1/t, smaller than 1/√t, even in a tube based at the identity. This is a counterexample to deriving a zero-free tube from KA alone, not a claim that this exact mixture is the lane’s cut-good denominator. The latter remains NOT-VERIFIED and needs its own estimate. The simple zero is stable under replacing the two point masses by narrow positive densities; the issue is not atomic integration.

There is also an exact constant error. For a positive raw activity with c_ell n output links, the sufficient bound is

    α < acosh(1 + a/(c_ell κ)),

not merely α < sqrt(2a/(c_ell κ)). The latter is only its small-a asymptotic and is strictly larger. Exact witness: a/(c_ell κ)=1 and α=7/5 satisfy α²/2=49/50<1, while cosh α−1 ≥ α²/2+α⁴/24 = 17101/15000>1. The remaining price is at most −2101/15000 in these units. Even the exact acosh condition is a sufficient envelope criterion, not a necessary analyticity condition: take a constant activity, or M=0, for which no coarse-field growth occurs. Accordingly KA-2’s “iff” and “canonical units are forced” are not general theorems about all such activities.

## Finding F4 — DENSE’s bare-measure obstruction survives; its scope and cube count need correction

**Verdict: CONFIRMED** for DENSE (i), (ii), (iv) and the weak-coupling version of (v), with their slope/domain hypotheses; **REFUTED** for the uniform cube-stack prefactor after E3 and the unrestricted “every N” report. Claim status: **PROVEN** for the scoped bare result.

Attaches to `LARGE55.md:175–218`, “Theorem DENSE”; E2–E4; §7 “Report: ... every N”. This is independent finite-energy reasoning, not reliance on the prior LF-count claim.

For a link b, write its conditional density as exp(u f(U))/Z, f(U)=Re tr(UA)/N, ||A||≤6. At a maximizer U*, first variation in su(N) gives anti-Hermitian part of U*A equal to iλI. A rank-two rotation with opposite eigenangles cancels λ. A displacement of operator distance 2(ε+ε³) therefore costs at most (24/N)(ε+ε³)². The radius-ε³ Haar ball costs at most another 6ε³. It lies outside the target ε-ball, whether the maximizer starts near or far from that ball. Its conditional probability is at least

    π₀ = c_N ε^(3D) exp(−u₀ B_N(ε)),
    B_N(ε) = (24/N) ε²(1+ε²)² + 6ε³.

For disjoint test plaquettes, condition successively on their dedicated links; independence of the plaquettes is NOT assumed. This gives P(all good)≤(1−π₀)^M≤exp(−Mπ₀), and P(n specified tests bad)≥π₀^n. An even-coordinate packing has M≥|Λ₀|/9. With u₀≤u_*+β_* K log L, log(Z/Z_sf) has the claimed lower bound proportional to L^((4−B_Nβ_*)K). For ε=g₀(log(1/g₀))^p, g₀→0 and u₀=O(K), log π₀=−O((log K)^(2p)+log K)=−o(K); every fixed n still gives exponentially many expected bad test patterns. These conclusions require no upper-tail estimate.

“Dense” here means an increasing absolute count and a vanishing all-good probability, not a positive limiting fraction of bad plaquettes: π₀ itself tends to zero. No general conclusion for fixed cuts ABOVE B_Nβ_*<4 is established.

E3 changes the object in (iii) to n distinct adjacent level-1 CUBES, each with an interior test plaquette. The old fine-plaquette packing count cannot then be reused without multiplicity. A safe corrected disjoint-cube count is

    E[number of prescribed bad n-cube rods] ≥ |Λ₀|/(2 n L⁴) · π₀^n,

when the side in CUBES, side(Λ₀)/L, is at least n. Derivation: there are s_c³ floor(s_c/n) disjoint rods, and floor(s_c/n)≥s_c/(2n). Choose one interior test plaquette per cube. For L=3, the prefactor is |Λ₀|/(162n), not |Λ₀|/(18n). The latter is not a uniform theorem for distinct cube clusters: already n=1 gives a purported lower bound larger than the total |Λ₀|/L⁴ cubes when L⁴π₀>18, possible at fixed u₀,ε and sufficiently large L. This correction changes no divergence exponent at fixed L. These bad patterns are also not necessarily maximal components of exactly n cubes.

The exact threshold checks independently reproduce all seven rows in §7. I expanded the polynomial as

    B_N(ε) β_N = [22N ε²(1+ε²)² + (11/2)N² ε³]/π²

and compared rational upper/lower π bounds (333/106<π<355/113). At N=2, ε=629/1000 gives upper value 20202034664558963491/5062500000000000000<4; ε=630/1000 gives lower value 126343744465253931/31506250000000000>4. At N=3, ε=538/1000 gives upper value 288731506252727491019/72193359375000000000<4; ε=539/1000 gives lower value 253369650644656323597897/63012500000000000000000>4. Thus 0.629/0.538 are CONFIRMED sufficient grid thresholds at the stated one-loop slope, not universal thresholds for an arbitrary F_R upper slope. At 1.1 times that slope the checked conservative grid thresholds are 0.610/0.520, as §7 itself records. The actual flow must be compared with β_*, not silently with β_0^std.

The sentence that ε₁=6.7×10^(−40) works “for every N” is false. The script only tests N∈{2,3,4,5,6,8,10}. At N=10^60 the N² term alone exceeds (11/20)N²ε₁³=3308393/20000>4, using π²<10. Correct statement: for the seven tested ranks; for each arbitrary fixed N one can choose a sufficiently small N-dependent cut.

## Finding F5 — NOFREEZE forbids the displayed fixed-cutoff bound, not every freezing policy

**Verdict: CONFIRMED** for the fixed-n arithmetic with its assumed weights; **REFUTED** for “every cut failure ... never frozen” and “an unreturned category needs a fixed threshold”. Claim status: **PROVEN** for the scoped obstruction; **OPEN** for a successful alternative scheme.

Attaches to `LARGE55.md:232–260`, especially “Consequence”, E11–E12, and §11 item 2. At fixed n, volume exp(4r log L) beats exp(−O(n(log r)^(2p))) and also any omitted polynomial factor. That arithmetic is sound. But the theorem’s hypotheses FIX n. They cannot imply a theorem excluding cutoffs depending on level/coupling. Indeed the same formal Peierls arithmetic admits

    q_j = p(g_j)²,   n_j = ceil(C u_j/q_j).

If an upper price exp(−c q_j) per cube is available, and shape entropy is exp(b n), then for sufficiently small g, cq_j−b≥cq_j/2. Hence the large-component tail is bounded by a constant times exp(−cC u_j/2). Under the lower flow bracket, choose (cC/2)β_- > 4 (or exceed the additional constant shadow rate). The resulting volume sum converges. This is a conditional arithmetic possibility, not a construction of the Yang–Mills route, but it directly disproves the claimed arithmetic exclusion of every variable-cutoff policy. LARGE55 itself uses a variable cutoff fallback in §6.3 step 5.

There is even a concrete bare-measure exception to the literal “no failure may be frozen”. Set p=1, x=log(1/g), ε=gx, V=|Λ₀| and M=V/L⁴ cubes, and freeze only the event that EVERY cube is bad. This is one connected full-torus component, with a size criterion depending on the volume. On that event the Wilson action is at least x²M/(2N), since each cube supplies a distinct interior plaquette. Restricting every bare link to its radius-g Haar ball gives plaquette norm ≤4g, Wilson plaquette action ≤8g² and

    Z ≥ (c_N g^D)^(4V) exp(−48V),
    P(all cubes bad) ≤ exp{V[48−4 log c_N+4Dx−x²/(2NL⁴)]}
                     ≤ exp(−V x²/(4NL⁴))

for sufficiently small g. The event has positive probability, and all future raw kernels integrate to one. Thus this particular failure category is genuinely rare enough to freeze under a variable rule, even with a coupling-scaled cut. This is not a proof that the complement’s returns or the full reference comparison close; it suffices to reject the literal universal prohibition while preserving the fixed-n obstruction.

Additional scope defects: DENSE counts occupied n-test patterns, not maximal components of exactly n cubes. It gives no lower bound for a specified isolated-component event. NOFREEZE’s statement mentions components of size ≤n, whereas its displayed history tail w^(n+1) is the tail for sizes >n; those are different policies. At j>0 the one-link Wilson conditional law used in DENSE is no longer the effective density’s conditional law. The claimed analogous bound there is an assumption, as §10 partly admits.

Even at level zero, DENSE supplies c_N ε^(3D)exp(−A p(g)²), not c exp(−A p(g)²) with the same constants. Absorbing the g^(3D) prefactor into a changed constant exponent of p(g)² is not justified for all p>0 (it fails by that argument when p<1/2). The correct logarithmic loss is O(log u+(log u)^(2p))=o(u), which suffices for the fixed-n divergence. None of this forces the particular in-step R-operation architecture: DENSE forces correction of the divergent free-energy difference from the all-small sector, not a unique counterterm organization or a nonzero coupling shift.

## Finding F6 — TL and PP are sound, but PP-2 does not propagate SRC’s spatial content

**Verdict: CONFIRMED** for TL, TL-1/2, PP and their stated scalar bounds; **REFUTED** for the assertion that PP-2 alone supplies SRC-κ-LF; **NOT-VERIFIED** for LF-UV/LF-diff as the claimed complete source interface. Claim statuses: **PROVEN** for the scalar lemmas; **GAP** for the stronger interface.

Attaches to `LARGE55.md:100–164`, “PP-2”, “Sufficiency”, E9/E17; `UNIV55.md:333–345`, (N1)/(N3); `SRCCD55.md:354–368`, SRC-κ/SRC-κ-LF, and :716–719, (M2).

TL follows from e^(−2t)≤k≤e c_N^(−1)t^D, then integration against the positive incoming density. At the last level |E_K|=4|T| and bounded t_(K−1) makes its logarithmic loss O(|T|). This is only a positive-real density comparison; applying it directly to a complex source weight would lose the sign argument. The factors are independent of cutoff K at fixed endpoint coupling, not independent of the endpoint coupling or volume.

PP follows by integrating a pointwise inequality against a common positive kernel. In particular real global log-ratio bounds propagate, and a complex relative-error disc with δ<1 remains a zero-free disc. E9 correctly removes the false converse. Also, a per-block error η_m first becomes a GLOBAL error N_mη_m: PP preserves the latter, not the polymer norm, spatial localization, or a per-block error unchanged after volume shrinks. The common-kernel hypothesis includes the kernel coupling values, not just equal lattice geometry.

This is enough to avoid a separate last-level calculation for UNIV’s U-dens, GIVEN a sufficiently small global all-configuration comparison at an earlier common level. UNIV (N1) already asks for large-field uniformity. That requirement remains open, and no convergence rate or marginal/irrelevant recursion is generated by PP.

SRC (M2) is stronger: it includes spatially weighted joint cumulants, coarse-image quasi-locality and a path sum. Nonvanishing of the source generating function is not that statement. A direct failure of the claimed implication: let a hidden sign U=±1 have equal weights, let both distant source insertions equal εU, and propagate with a common kernel independent of U. At every finer fixed U the log generating function is εU(z₁+z₂), so its mixed second derivative vanishes. At the coarser level it is log cosh(ε(z₁+z₂)), with mixed derivative ε² at zero, independent of the distance between the sources. For a sufficiently small fixed polydisc the relative-error hypothesis of PP-2 holds with δ<1. Thus even exact absence of finer conditional mixed cumulants need not survive arbitrary positive propagation as a spatial decay estimate. The example challenges the PP-only inference; it is not a counterexample to a properly localized Yang–Mills source induction.

To obtain M2, I10 must include the source polymer norm and its localized propagation through the last levels, or an equivalent conditional-mixing theorem. Merely relabelling it LF-diff does not remove it.

LF-UV also orders complex quantities with ≤ in its source clause; that is not a defined mathematical inequality. It needs an explicitly nonvanishing ratio, a specified analytic logarithm (with its local source counterterms), and a bound on its real part/modulus. Even after that repair it is a sufficient template conditional on node A, not a proved minimal characterization. DENSE does not prove the g_j^6 coupling-shift cap necessary, and E16’s quasi-local-in-scale replacement needs an actual summable rate, not only the word “decaying”.

## Finding F7 — lg55_2’s six tables are correct evidence; they do not test a general tower contraction

**Verdict: CONFIRMED** for the six finite linear calculations; **NOT-VERIFIED** for I4 and any generic “decays per level” inference. Claim status: **PROVEN** for the stated finite linear cases; **OPEN** for nonlinear tower control.

Attaches to `LARGE55.md:496–500`, §7 lg55_2, E1/E7; `checks/lg55_2_s4p.py:21–42,107–141,155–163`; `PROOF.md`, “S4′ [S3] Order-averaged averaging” and “Decision 4”.

Independent derivation: linearize the transporter with a fine one-form A. The first and last axial legs average to a vertex function h_X, giving

    Q A(X,mu) = h_X − h_(X+e_mu) + T_mu(X),
    T_mu(X) = L^(−d) Σ_(y in B(X)) Σ_(r=0)^(L−1) A_mu(y+r e_mu).

Thus the coarse curl of QA is exactly the coarse curl of T; the axial-order dependence cancels. This is the independent calculation missing from a mere re-run of the script. For one fine link inside B(0), its straight-leg multiplicity ranges from 1 to L−1, so R1=(L−1)/L^d. At b₀=(0,e₀), the two nonzero straight-leg responses are (m+1)/L^d and m/L^d, m=(L−1)/2. Therefore

    R1(b₀)=R1c=(m+1)/L^d,
    R2=((m+1)²+m²)/L^(2d).

The center’s averaged first-leg coefficient is q=(L^d−1)/(2dL^d): all nonempty axial paths distribute their first step equally among the 2d signed directions. The full star response, after including the straight leg, has gauge projection omega=−q−1/(2dL^d)=−1/(2d), not just the first-leg coefficient. Its remainder is [2d(m+1)−1]/(2dL^d). This reconstructs the center numbers independently.

For d=4: L=3 gives R1=2/81, R2=5/6561, R2/R1(b₀)=5/162, omega=−1/8, remainder=5/216. L=5 gives R1=4/625, R2=13/390625, ratio=13/1875, omega=−1/8, remainder=23/5000. All six source table rows agree with the symbolic formulas and an exact replay of the supplied incidence code. Replay was in memory: only imports/function definitions were executed, and the display-only report.append containing float conversions was removed. No script or output file was written; every executed calculation used integers/Fraction. It took the tool-reported 2.701 seconds.

These are matrix-entry bounds, not an operator-norm contraction. For a coherent weak Abelian curvature in a sufficiently large patch, take a linear potential A_mu(x)=Σ_nu F_(nu,mu)x_nu. Its straight block average has coarse curvature L²F, so coarse-link-unit curvature grows by L² per level. There is no contradiction with the single-link result: many inputs add coherently. Tower estimates must track support size, shape, collars and the price of coherent fields. Also the conditional soft kernel adds fluctuations; the deterministic mean alone is not a tower probability estimate. The author’s explicit finite-case/nonlinear-OPEN qualification is essential.

### Gate audit for both scripts

- `lg55_1_dense.py:38–67`: feasibility and P1/P2/C1/C2 are exact comparisons which can distinguish a wrong constant at the tested points. P3/P4 validate monotonicity of the supplied polynomial/grid, not the Wilson-measure derivation or all ranks. Analytically, B_N is strictly increasing in ε>0; B_Nβ_N is strictly increasing in N>0. All numerical boundary results were independently reproduced in F4. The all-N extrapolation at LARGE55 §7 is not a tested gate.
- `lg55_2_s4p.py:58–103`: G0 checks actual contour support; G1’s gauge half is a telescoping identity, with a non-gauge control preventing the zero-functional implementation from passing both halves. G2 checks the first-step symmetry count. These are structural correctness controls, not large-field tests.
- H3/H4/H5 test finite responses and can fail. Replacing the average by a single central straight transporter would give a unit single-link curvature response and a unit two-step response, violating the d=4 H4/H5 bounds. Their limited tested domain does not decide I4; no large nonlinear input is present.
- **REFUTED as a success certificate:** “exit 0, empty stderr” in LARGE55 §7. Neither script exits nonzero when a logical gate is false (`lg55_1_dense.py:78–80`; `lg55_2_s4p.py:161–163` only print PASS/FAIL). A false gate still reaches normal exit. This does not reverse the actual checked rational results, but exit status cannot certify them.
- The separately claimed criteria-file timestamps and pre-registration hashes were not independently verified: those files were outside the two discretionary implementation reads. Status **NOT-VERIFIED**, not fabricated PASS.

## Finding F8 — the displayed union bound fails, but the universal TS-up no-go is too strong

**Verdict: CONFIRMED** for divergence of the displayed counting bound under aβ_+<4 and fixed endpoint coupling; **REFUTED** for promoting that to every cut-based counting scheme and for the unqualified small-tail comparison. Claim status: **PROVEN** for the arithmetic; **NOT-VERIFIED** for necessity of LF-inst or any universal impossibility.

Attaches to `LARGE55.md:437–452`, E6/E20, and §10 lg-18. With u_j≤u_k+R+β_+(k−j)log L,

    Σ L^(4(k−j)) exp(−a u_j)
      ≥ exp(−a(u_k+R)) Σ L^((4−aβ_+)(k−j)).

This diverges over an increasing depth range at fixed u_k when aβ_+<4. It invalidates that raw union bound. It does not show all cut schemes fail: a scheme can count only larger clusters, use a level-dependent cutoff, or use an amplitude/flow-survival weight. Whether any of those proves TS-up is OPEN; they are not excluded by this calculation. E20 itself admits the bare cheapest-cost argument has not been proved for level-j effective actions, so the application to every intermediate level is conditional as written.

For clarity, a genuine effective-level lower tail can instead be obtained from the output kernel, but with different constants. Conditional on all other level-j links, the remaining link has a mixture of k_(j−1)(·;M), ||M||≤1. Repeating F4 with staple norm 6 replaced by 1 yields a bound

    c_N ε^(3D) exp{−κu_(j−1)[(4/N)(ε+ε³)²+ε³]}.

This is not the bare coefficient B_N times u_j; κ and the level index must be carried. It still does not classify flow-surviving defects.

Line 444 says “cost_k ... is ≪g_k²”. The COST tends to infinity; the intended quantity is the PRICE exp(−cost_k). Even for the price, with x=log(1/g),

    exp(−c p(g)²)/g² = exp(2x−c x^(2p)).

It tends to zero for p>1/2, or for p=1/2 with c>2; it does not for 0<p<1/2, and equals 1 at p=1/2,c=2. LARGE55 quantified p>0. Fixed-cut exp(−a/g²)=o(g²) for any a>0 is sound. Branch D therefore needs the stated tail assumptions plus an observable comparison; its closure is not established by this paragraph.

## Finding F9 — PRICE and HIST-sum need explicit local and post-normalization prices

**Verdict: NOT-VERIFIED** for PRICE from BFT-coer exactly as written and for the per-history application; **REFUTED** for retaining the same exponent after absorbing an unbounded polynomial prefactor. Claim status: **CONDITIONAL** for the corrected local-price implication; **OPEN** for I2/I5/I6.

Attaches to `LARGE55.md:475–486` (“BFT-coer”, “Lemma PRICE”), :458–461 (parameter order), and :501–513 (freezing/normalization/history sum).

PRICE is immediate if one has a consistent decomposition E=E_S+E_rest with E_S≥c_co ε_cl²|S|, a bounded overlap of charged plaquettes, and a quantified norm for polymers touching S. The displayed aggregate coercivity with “exponentially decaying ... tails” has not specified such a decomposition or a bound on its boundary/tail debit. Applying a separate region’s BFT inequality is insufficient unless its main term agrees with the restriction of the original region’s main term, including its boundary conditions. If BFT-coer is intended to include this local consistency, state it, and PRICE is a valid conditional lemma. The present one-line proof does not settle the boundary problem on holes.

The exponent called a changes role without being recomputed. In §6 it is c_co ε_cl², the raw main-term price. Step 4 introduces a factor (e c_N^(−1)t_j^D) per frozen link and then absorbs it. For any q>0 and t=κu,

    t^q exp(−a u) / exp(−a u) = t^q → infinity.

It cannot be absorbed into a u-independent prefactor with the SAME a. A correct bound uses a_eff<a:

    (κu)^q exp(−a u) ≤ C_(a−a_eff,q,κ) exp(−a_eff u).

One must also take the minimum with the geometric mismatch price and account for links per cube. For example reserving half the action gives a_eff=a/2 and the sufficient history cutoff floor(2(4+c_B)/(aβ_-)); more economically choose any a_eff satisfying (n_sharp+1)a_effβ_->4+c_B and then choose the weak-coupling ceiling. The original floor((4+c_B)/(aβ_-)) is valid ONLY for the actual final exponent a and the rule that frozen sizes exceed that floor. This is precisely a stale-parameter risk: the exponent used to choose the cutoff cannot then be spent unchanged.

There is a separate missing branch in the induction: §6.3 freezes components of size >n_sharp “or failed returns”. A failed return of small size has no >n_sharp guarantee. Giving it only exp(−a_eff u) per cube reintroduces the divergent small-cluster history sum. I4/I6 must prove that every such failure acquires sufficient additional price, grows into a sufficiently large paid component, or is eventually returned. The present list does not state this discharge.

Finally (R_m)(b) concerns a fixed-U density while COL concerns integrated unobserved outputs. A construction must explain how the fixed cone variables are represented before they may be integrated and how the small-field reference is compared. Calling I6 “proof = I1–I5” is not itself that induction.

## Finding F10 — the literature comparison is fair in its narrow scope; the claimed wall reduction is not a proof

**Verdict: CONFIRMED** for the narrow dimensional comparison and the table’s 38/15 label counts; **REFUTED** for the quoted scalar-kernel coefficient and for treating three route entries as three independent required walls. Claim status: **ARGUED** for the alternative research architecture, not established replacement.

Attaches to `LARGE55.md:167–173,266–277,376–419`, especially “three P-scale walls”; `RLARGE.md:490–491,494` (rows 9,9p,10b).

Dimock’s d=3 QED exposition does use a hard gauge-field average, the constrained-minimizer quadratic split, and a large-field factor beating the ultraviolet volume. Its coupling scales exponentially with cutoff depth; for the positive-integer p used there, the log-power cut produces exp(−C K^(2p)), which beats exp(3K log L). That is a fair comparison with the much slower d=4 running. It does not refute Dimock’s theorem in its own setting, nor every architecture involving suppression and entropy. [Dimock, 2204.07201, §§2–5, equations (7), (17)–(19), (56)](https://arxiv.org/html/2204.07201).

The scalar example really is already soft and uses localized averaging, so it supports that organizational idea rather than supplying a nonabelian normalized-kernel theorem. There is a coefficient error in LARGE55: its quoted equation (5) has aL² in the Gaussian, while the paper has a/L² multiplying the coarse-lattice squared norm. The equivalent counting-norm coefficient is aL, from its volume factor L³. Correct aL²→a/L², a factor L⁴. [Dimock, 1212.5562, equations (5), (13)–(15)](https://arxiv.org/html/1212.5562).

The h1–h5 replacements therefore have the following status: h1 needs the normalized action (F1); h2 needs its gauge-fixed chart Hessian and hole-uniform covariance bounds (OPEN); h3 has a valid MIS tail but an unproved geometric interface (F2); h4 has valid raw COL but an unproved reference-density comparison (F2/F9); h5 needs local normalized BFT-coer (F9). The compactness observation in h6 is useful but does not preserve the same price after normalization (F9).

There are indeed 38 labeled rows and 15 labels designated V3-specific: 7,9,9p,10,10a–10f,12,17–20. This is a count of table entries. Rows 9 and 9p are ALTERNATIVE ways to obtain the SAME CLS-min bound; row 9p is explicitly marked parallel. With row 10b, the cited three entries represent TWO distinct endpoint obligations, not three simultaneous independent walls. Other selected rows include a clause already off the HW path (7), consequences, and repeated dependencies. “15 dropped” does not measure 15 independently discharged theorems.

More importantly, the proposal replaces the hard interfaces with I1–I6 and I10. It has not proved those interfaces weaker or cheaper. BFT-coer is not the only new nonlinear input: I4 is expressly a nonlinear tower theorem, and I5 includes nonlinear reference normalization. The savings may be real, but calling these s-scale is an estimate, not mathematical evidence. The failure of one moment formulation is a reason to investigate another, not proof that the alternative closes.

## Finding F11 — symbol, quantifier and source-control ledger

**Verdict: CONFIRMED** for the distinctions below; **NOT-VERIFIED** for any comparison that suppresses them.

| Object | Exact source/locating string | Required distinction |
|---|---|---|
| Kernel stiffness | LARGE55 §0 “t_j := κu_j”; PROOF “Decision 4” | κ is the kernel coefficient; it is not UNIV’s irrelevant-contraction exponent κ in (N1). |
| Haar constant | LARGE55 §0 “c_N := inf” | This is a Haar-ball-volume constant, not a norm-conversion c_N elsewhere in PROOF. No numerical value was assumed. |
| Flow slope | RLARGE:45–47 “Action normalisation”; :98–103 “(F_R)” | β_0^std=11N²/(12π²) is not the proven upper slope β_+. DENSE must use the latter or its actual stated β_*. |
| Prices | RLARGE:87–94 “The defect exponent”; LARGE55:458–459 | v3’s a=min(theta a_bad,a_A), the raw BFT price c_co ε_cl², the mismatch price, and the post-normalization price are different quantities. F9 forbids silently reusing one cutoff. |
| Small threshold | RLARGE:70–81 “Current ε_1 ceiling” | 6.7×10^(−40) is an approximate CEILING conditional on other minima, not a fixed guaranteed admissible value for all N or all future outputs. The report-only script does not test those other minima. |
| g_0 | LARGE55 §2.1 vs §6 “Parameters, fixed in this order” | The bare coupling depends on K; the final parameter-order g_0 appears to be a global weak-coupling ceiling. Rename the latter gamma_0 to prevent an input/output collision. |
| Coarse maps | PROOF “S4′ [S3]” vs “Decision 4”; LARGE55 §6.3 step 2 | Averaged logarithms and the arithmetic transporter mean are different nonlinear maps. The cited L1d(i) passage also states L≥9, not the L=3,5 examples in lg55_2. |
| LF-UV locality | LARGE55 E16 | The original two-coupling input became scale-quasi-local dependence on a whole past. Its decay constant/rate must be an explicit output, not assumed from the former finite-dependence statement. |

PROOF line numbers changed during this review: the Decision 4 locating string was initially reported at 1850 and later at 1851, and LF-count at 4411 then 4413. All substantive citations above therefore include locating strings. I found no specific numbered PROOF citation in LARGE55 that could itself be certified stale; I do not invent such a finding. The actual stale-interface issues are F1/F3/F9, not a guessed line-number error.

Clarification to F4: retaining many test-plaquette labels inside the same cube may retain a fine-plaquette prefactor, but then the counted objects are decorated test patterns. They cannot be silently counted as distinct RLARGE cube components. The corrected one-test-per-cube bound has an unambiguous cube interpretation.

Procedural disclosure: a row-count helper loaded RLARGE.md into memory before selecting §4.2 and printed only the counts. That departed from the literal grep/sed-only rule for large files, although no full-file text entered the review context. The scientific findings must not be represented as a strictly protocol-compliant certificate under the owner’s binding rule. All other displayed large-source content was located by string and read in bounded ranges. No version-control command, snapshot, audit ledger, source edit, separate output artifact, floating-point numerical evaluation, or long job was used.

## Disposition of the eight inherited REFUTED items

The verdict here assesses LARGE55’s claimed reversal, not the truth of an unread or unproved upstream theorem.

| Item | Review verdict | What survives / what does not |
|---|---|---|
| IV1 | CONFIRMED, scoped | DENSE refutes Z≤exp(E|T|)Z_sf for its permitted bare cuts/slopes. It does not exclude all renormalized or weighted counting architectures. |
| IV2 | CONFIRMED, scoped | The d=3 volume-beating argument cannot be transplanted with the stated d=4 cuts and no extra free-energy correction. Dimock’s own theorem is unaffected. |
| IV6 | NOT-VERIFIED | KA does not settle the normalized returned-polymer width. Its exact raw-positive-integral sufficient window is acosh, and the node-A lower width requirement and denominator zeros remain. |
| IV8 | CONFIRMED for the narrow replacement | A centered mismatch tail for every fixed SU(N) needs no KS-N moment estimate. The complete geometric/history/pointwise use of it is still GAP; the truth of KS-N is not reviewed. |
| IV10 | CONFIRMED as a conditional redundancy | A sufficiently small global density comparison propagates through genuinely common kernels. N1’s full large-field uniformity remains required; this is not proof of N1 or its local norm recursion. |
| IV11 | REFUTED for the stated PP-only reduction | PP-2 gives a zero-free scalar source ratio, not SRC-κ-LF’s spatial cumulants and quasi-locality. Those must remain explicit in I10. |
| IV15 | NOT-VERIFIED as a substantive reversal | The supplied quote is a conditional HW-route implication. Avoiding that named obligation in a different design is plausible, but its replacement induction is not proved; the original LCONV55 file was not read under the read budget. |
| IV17 | NOT-VERIFIED as a reversal of RLARGE | COL eliminates raw unobserved kernels. RLARGE:213–219 states a conditional representation-dependent upper bound, not a theorem that its B_0 is universally intrinsic. E13 leaves a boundary cost; normalized-history savings remain I5. |

## Remaining inputs I1–I11 after this review

| Input | Status | Minimum exact obligation still needed |
|---|---|---|
| I1 | OPEN | Gauge-fixed one-step positivity and the cluster expansion for the correctly normalized action, uniformly on charts with holes and allowed boundary data. |
| I2 | OPEN | Quantified local/coherent BFT coercivity, compatible with restriction to regions, collars, tails and normalization; geometric mismatch detection with an actual delta. |
| I3 | OPEN | Returned/tower R-operation in the actual normalized activity class, including zero-free denominators, cuts, source dependence, locality and the required complex norm. |
| I4 | OPEN | Nonlinear, support-dependent tower bound including random kernel fluctuations and failed returns; finite single-link dilution is evidence only. |
| I5 | OPEN | Relative normalization versus the small-field reference with a proved constant boundary cost, or a fully re-derived variable-cutoff summation. c_B=0 is withdrawn by E13. |
| I6 | OPEN | Exact history induction with compatible pointwise/integrated interfaces, charge allocation and a summable treatment of small failed returns. It is not automatic from the names I1–I5. |
| I7 | CONDITIONAL | F_R for the actual chain, FI-1 and RLF-delta with correct coupling indices; use the final price exponent and actual slopes in the cutoff. No new verification of those upstream theorems is claimed. |
| I8 | OPEN | The matching BFT-0…5 package on the needed domains; a banked clause on another domain does not close this package. |
| I9 | OPEN | Wrap/final-level polymer and source assembly. TL supplies only the positive raw-density bound at the final level. |
| I10 | OPEN | Difference-form/source induction in a spatial polymer norm at every relevant configuration, with a common-kernel specification, nonvanishing and quasi-locality. PP supplies scalar propagation only. |
| I11 | OPEN | An estimate sufficient for the chosen flowed witness; LF-inst is one proposed form, not proved necessary by the failed union bound. Branch D’s full observable bridge is not reviewed here. |

The extra “node-A norm decision” is a mathematical compatibility obligation: nonempty exact width window, zero-free normalized activities, and Cauchy/cluster estimates in that same norm. It cannot be checked off as a choice of notation.

## Summary table

| Finding | CONFIRMED | REFUTED / NOT-VERIFIED |
|---|---|---|
| F1 | Correct normalized action formula | REFUTED: omission of log N from the claimed total action. |
| F2 | MIS and raw COL | NOT-VERIFIED: geometric mismatch, history conditioning and normalized comparison. |
| F3 | KA/KA-1 raw holomorphic envelope | REFUTED: unrestricted returned-activity inference, square-root sufficient bound/necessity claims. RLF-5 remains unverified. |
| F4 | Bare finite-energy obstruction and seven threshold rows | REFUTED: distinct-cube prefactor after changing the counted object; all-N extrapolation. Actual-slope qualification required. |
| F5 | Fixed-n divergence | REFUTED: every freezing policy needs a fixed threshold. |
| F6 | TL, PP, global U-dens propagation | REFUTED: PP-only spatial SRC implication. Source interface remains incomplete. |
| F7 | Six exact linear tables | NOT-VERIFIED: general nonlinear towers and pre-registration; exit-zero is not a logical success gate. |
| F8 | Displayed union-bound arithmetic | REFUTED: universal counting no-go and unqualified p>0 tail comparison. |
| F9 | Local pricing under explicit stronger hypotheses | NOT-VERIFIED: stated normalized history induction; REFUTED: same-a polynomial absorption. |
| F10 | Narrow d=3 comparison; 38/15 label count | REFUTED: aL² coefficient and three independent-wall interpretation. |
| F11 | Source/symbol distinctions located | Open comparisons cannot suppress the distinctions; procedural exception disclosed. |

## Exactly what may be banked

Source receipt: LARGE55 SHA-256 `79bc36d60687376716aa425ad3c271b681ca9549f5d217693e2736b805cdf0e7`, unchanged between the recorded mid-review hash and the final source check at 2026-10-29 05:12:23 UTC. The procedural exception above remains part of this receipt; it is not cured by a later range-only recount.

1. **PROVEN:** TL for the positive normalized chain and its last-level O(|T|) corollaries, with fixed endpoint coupling; PP for genuinely common positive kernels and global scalar relative/log bounds. These do not bank spatial SRC.
2. **PROVEN:** DENSE’s one-link lower bound, disjoint-test all-small bound and exponential lower bound on log(Z/Z_sf), under B_N(ε)β_*<4; coupling-scaled fixed-pattern divergence at weak coupling. For cube rods use the corrected prefactor and cube-side condition. The 0.629/0.538 numbers are bankable at the stated one-loop slope, not at an unspecified β_+.
3. **PROVEN:** MIS as a centered-exponent tail under the plain chain, for each fixed N, and COL when every other factor avoids the forward cone. Neither banks its stronger architecture interface.
4. **PROVEN:** KA and KA-1 for raw kernel superpositions; for positive raw activities with the required real price and link count, the exact acosh window gives a sufficient complex envelope. Normalized returned activities, their logarithms and their source norms remain unverified.
5. **PROVEN:** the six finite lg55_2 tables, independently reconstructed at linear order. No nonlinear or general operator contraction is banked.
6. **CONDITIONAL:** the fixed-n entropy arithmetic and the generic history condition (n_sharp+1)a_eff β_->4+c_B, provided the actual final activity bounds, geometry and size rule hold. The particular constants 38416/6400 and the full HIST theorem were not independently re-derived here; keeping that existing arithmetic means keeping its hypotheses, not newly certifying its source.
7. **CONDITIONAL:** PRICE after explicitly providing local charge allocation, boundary/tail control and the correct normalized main term. No claim that I1–I11 are closed is bankable.

## Route verdict

**I do not agree with the recommendation to replace/drop the v3 pricing obligations as a verified simplification on the evidence in LARGE55.** I do agree that action pricing at each level is a worthwhile candidate research route, while retaining the returned-cluster R-operation and correctly scoped history arithmetic. It should be tested as a new induction, not announced as fifteen discharged rows or three removed independent walls.

A concrete next milestone is one normalized, history-compatible step on a chart with a hole: prove its main-term price, geometric mismatch implication, normalized returned-activity analytic norm and reference comparison, and account for failed returns. That would make a route comparison substantive. Until then the defects above prevent a favorable two-family check of the recommendation as stated.

The **single most dangerous unverified claim** is a cutoff-uniform zero-free complex domain for the normalized returned activities. KA provides only numerator/denominator upper envelopes; it does not prevent nearby denominator zeros, yet RLF-5 and the source induction need precisely that missing control.
