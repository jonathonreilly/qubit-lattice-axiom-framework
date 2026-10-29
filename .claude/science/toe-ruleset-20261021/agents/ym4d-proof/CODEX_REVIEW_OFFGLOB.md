# PRE-STATED

UTC: 2026-10-29T04:28:37.022203+00:00

Independent hostile review of `OFFGLOB55.md`, specifically BFT-0/1/2 outside the global small-potential class, with the owner's seven targets and errata E1–E6 taking precedence over unrepaired text. This section is written before independent derivations. Prior exposure: headings, all six errata, the final status line, and §§0–1.7. The first creation command failed because `python` is absent; this successful creation uses `python3`. No prior mathematical verdict is adopted.

Refutation tests, fixed in advance:

1. Reconstruct the data/background classes, axial estimate, strict-subclass witness, and torus holonomy construction. A failed quantifier, norm conversion, integer/ceiling bound, or false linear-versus-square-root comparison refutes the attached claim.
2. Reconstruct the fine axial Hölder estimates and derivative-loss witness. Separate a counterexample to an axial gauge from a counterexample to existence of a better gauge. Test the flat-reference obstruction without assuming it.
3. Derive covariant charge routing including adjoints, tree orientations, support, scale factors and cut-off charges. Inspect the cited executable for independent positive and negative controls. Finite toy identities cannot prove uniform analytic bounds.
4. Rebuild GP's domain/codomain, source compatibility, local operator comparison, transition costs and Neumann correction. A non-cc residual, unavailable linear inverse, or unsupported uniform norm conversion defeats the asserted implication unless it is explicitly a matching premise.
5. Check OFF's inductive start, Newton radii, a priori estimate, nonlinear gauge matching, uniqueness, complex domain, and k/T quantifiers. Track constants by definition and detect stale smallness minima after constants change.
6. Derive L1/L2 and determine whether the no-alignment conclusion reaches ALIGN55's actual Hessian pair rather than a different weighted pair or slice formulation.
7. Adjudicate P5/P12/P13/P14/P19 and the named residual hypotheses. State exactly what can be banked, separating a proof of an implication from unproved inputs.

Evidence contract: only the permitted source files and at most two additional scientific files; bounded string searches and ranges for large files; no git, audit ledgers, snapshots, or background jobs. All writes are to this file. Arithmetic checks, if used, are exact plain-Python integer/rational/symbolic calculations only. File line numbers below come from current string matches, not copied source citations. Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN.

## Findings (appended incrementally)

### F1 — Data frames and the square-root obstruction survive; the flat-torus proof has its gauge factors reversed

Verdicts: **CONFIRMED** for Lemma C2, Proposition C4 with E1/E2, and Proposition C6's existence/bound; **REFUTED** for C6's displayed path-independent gauge formula. Claim status: **PROVEN**, with the formula corrected below.

Anchors: `OFFGLOB55.md:97–107`, locating “factor 12(R′ − 1)”; `:121–147`, locating “R_ε :=”; `:178–182` (E1); `:150–160`, locating “g(x) := T_V(γ_x)T_W(γ_x)^{−1}”; `REVIEW_S22.md:389–411`; `PROOF.md:5526`, “Lemma AX”.

Independent reconstruction: the tree loop for a μ-link sweeps at most sum_{ν>μ}(x_ν−o_ν) ≤ 3(ℓ−1) elementary squares. Multiplication by their conjugated holonomies and the bi-invariant triangle inequality gives 3(ℓ−1)ε. Conversely four α-small links bound a plaquette by 4α. Thus B(ε) ⊂ N(R,3(R′−1)ε) ⊂ B(12(R′−1)ε), with the small-log and non-wrapping restrictions retained. This is an equivalence up to constants, not equality at the same numerical parameter.

For C4 put a=√2π, q=ceil(sqrt(a/ε)). Prescribe +π/q² and −π/q² on two disjoint q-squares of the two-dimensional torus. A zero-total real two-cochain is exact: writing m_Φ(y)=T^{-1}sum_x Φ(x,y), take φ_2(x,y)=sum_{r<x}(Φ(r,y)−m_Φ(y)) and φ_1(x,y)=−sum_{s<y}m_Φ(s). Both are periodic, and Δ_1φ_2−Δ_2φ_1=Φ. Exponentiating its primitive in one abelian SU(2) subgroup gives plaquettes of distance a/q² ≤ ε. The positive square's boundary has holonomy diag(−1,−1,1,…,1), distance a. In every gauge its 4q links therefore have maximum distance at least a/(4q). Since q≤sqrt(a/ε)+1, the lower bound is sqrt(a) sqrt(ε)/(4(1+sqrt(ε/a))). For ε≤1/(6C²), C≥1, this exceeds (441/1000)sqrt(ε)>Cε. This refutes any inference of an ε-linear bound solely from a theorem giving a bound linear in the necessary global potential s. It does not refute every possible use of such a theorem with additional curvature estimates. A fixed ε_g exclusion additionally requires the stated relation between ε and ε_g; do not drop that quantifier.

For flat fields, commuting cycle holonomies admit commuting traceless logarithms X_μ with |X_μ|≤3π√N by shifting at most N/2 principal eigenangles by 2π. W_μ=exp(X_μ/T) has the same holonomies. With the file's transport convention T(gU)=g(o)T(U)g(x)^{-1}, the gauge mapping V to W is

    g(x)=T_W(γ_x)^{-1} T_V(γ_x),

not T_V T_W^{-1}. A changed path left-multiplies both transports by the same loop holonomy h; the corrected product cancels h, while the printed product is conjugated by h and need not be unchanged. This is an order error in a nonabelian proof, not a failure of the flat-torus statement. The lower bound s≥max_μ d(h_μ,1)/T follows from a cycle of T links and matches the commuting principal-log construction in the stated regime.

E1 also contains a minor exact-arithmetic typo: **0.441²=0.194481**, not 0.195. The needed strict comparison with 1/6 is unaffected.

### F2 — Covariant routing is real algebra; the script checks that algebra, not the analytic extension

Verdict: **CONFIRMED** for HR_U(i),(ii),(v) on real SU(N) configurations and LOC-cc_U's exact decomposition; **NOT-VERIFIED** for any analytic/norm claim inferred from `og55_1`. Claim status: **PROVEN** for the algebra only.

Anchors: `OFFGLOB55.md:275–294`, “Lemma HR_U”; `:318–334`, “Proposition LOC-cc_U”; `:421–431`, “Check og55_1”; `checks/og55_1_route.py:85–132,146–245`.

On an oriented path b_1,…,b_m terminating at z, put I_i=Ad(U_i…U_m)u(z). At each interior vertex the incoming Ad(U_i)^{-1}I_i equals the outgoing I_{i+1}; the endpoint contributes u(z), the start contributes −Ad(T_γ)u(z). Reverse-edge coordinates must be −Ad(U_b)I_rev. Summing paths and then nested levels cancels all intermediate transported charges. Thus D_U^⊥P_U^T=1; P_cc^U=1−P_U^TD_U^⊥ is a projection; its partition pieces are individually cc_U and sum to any cc_U source. Nested paths remain in their coarse cell. These statements require neither criticality nor flatness. The bare-charge count is unchanged for SU(N), because each Ad is an isometry: a level-i block contains ≤L^{d(i−j)} charges, at most M_γ paths cross a link, and sum_{i=j}^{k−1}L^{−(k−i)}≤1/(L−1).

I inspected the entire route script and reran it once with `nice -n 10 python3 -I -B`, stdout only, no saved output files. Actual result: **24/24 A-items and 20/20 controls**; exit 0, elapsed tool wall time 4.983113125 seconds. No memory claim is made. A0 pairs independently evaluated incidence and gauge-generator formulas; A1 tests vertex divergences; A2 tests conjugation covariance. Wrong routing/sign/transport controls genuinely break tested identities. A3's sum property is largely a consequence of linearity and a source manufactured by the same projector, but A4 checks the resulting divergence independently; together with A1 this is a useful implementation consistency check. It is not a second proof of the analytic theorem. The three partition functions in lines 138–144 are nonzero throughout the model, so **no support-localisation gate is present**. There is also no G/s-slot, cutoff Hölder, Hessian, transition, d=4, or uniform-in-k/T gate. The file discloses most of these exclusions. The pre-registration timestamps/log provenance were not independently checked; the criteria/log files were not read.

Read-budget record: the two additional scientific files selected are `KFACTOR_OFF55.md` and `checks/og55_1_route.py`; other scientific files consulted so far were explicitly named by the user. The mandatory methodology/skill text was read only for review procedure, with the user's narrower no-git/one-file constraints controlling.

### F3 — Lemma U1(b)'s 1.1 is false in the lane's actual Hölder metric

Verdict: **REFUTED** for the displayed coefficient; **CONFIRMED** for the uniform sup/C^α conclusion after correction, and for U2's axial derivative-loss exponent. Claim status: **PROVEN** in the explicitly specified axial-frame pointwise norm, with corrected constants; the conversion from an arbitrary covariant curvature seminorm remains **NOT-VERIFIED** here.

Anchors: `OFFGLOB55.md:201–219`, “(b) [A^c]^∞_α ≤”; `:221–229`, “Proposition U2”; `BFT_A.md:459–462`, defining the pointwise seminorm using **|z−z′|_∞**.

The proof tests only c′=c+r e_λ. That does not establish its coefficient for diagonal separations in the stated norm. Take a fixed unit-norm abelian generator X∈su(2), n=3, ℓ=2, ε_0=1/24, and on the box put

    A_1(x)=−(ε_0/n²)(x_2+x_3+x_4)X,    A_2=A_3=A_4=0,    U=exp A.

This is already the prescribed complete axial gauge: direction-1 tree links have x_2=x_3=x_4=0, and the other tree links are 1. The three (1,ν) plaquette logs are constant ±ε_0 X/n²; the other components vanish. Thus max|F^c|=ε_0 and [F^c]^∞_α=0. Both parallel 1-links based at (0,0,0,0) and (0,n,n,n) lie in the box and have coarse ℓ∞ separation 1. Their coarse potentials differ by **3ε_0=1/8**, whereas U1(b) claims at most **1.1ε_0=11/240**. The exact positive discrepancy is **19/240**. The assumed smallness is 3ℓε_0=1/4≤1/2, so this is inside the claimed domain, for every 0<α<1.

Correct the display to

    [A^c]^∞_α ≤ 3.3ℓ [F^c]^∞_α + 3.3 ε_0.

For a general displacement r, pair the common ordered plaquette factors ribbon by ribbon. Their projected displacement has ℓ∞ size at most |r|_∞; there are at most 3ℓn common factors. The unmatched factors number at most sum_{ν>μ}|r_ν|≤3|r|_∞. The same 1.1 log-Lipschitz factor used in E2 then gives the corrected estimate. The coefficient multiplying ε_0 cannot be below 3 for this metric. The uniform-in-k conclusion survives; the printed number does not. E2 repairs a different issue and does not repair this one.

For U2, normalize the fixed generator to length one and take F(a,h)=K n^{−2−α}(−1)^a X. Then A_1=−hF, so n²Δ_1A_1=±2hK n^{−α}X. At h=ℓn the size is exactly 2ℓK n^{1−α}; [F^c]_α≤2K. The alternative A_2=−(K/2)n^{−2−α}(−1)^a X, A_1=0, has Δ_1A_2=F and d*A=0; its scaled derivative and Hölder derivative remain bounded. This proves a failure of this axial gauge's derivative estimate, not a failure of Coulomb-gauge existence. U3's nonlinear C^α-to-C^{1,α} bootstrap is still only ARGUED.

### F4 — CCL_U has an actual-generator sign error, and LOC-cc_U silently drops curvature from its constant

Verdicts: **REFUTED** for CCL_U's printed exact G-slot identity and the advertised arbitrary-configuration specialization of its constant; **CONFIRMED** for the corresponding magnitudes with the corrections below. Claim status: **PROVEN** for the corrected real, differentiable-log identities; **CONDITIONAL** for the small-frame norm estimate.

Anchors: `OFFGLOB55.md:269–273`, “(Ξ_Uλ)_l(b) :=”; `:299–316`, especially “(d_UΞ_Uλ)(P) = [λ(base P), log U_P]”; `:323–324`, “C_loc :=”; `:334`, “216 → 221”.

The frame convention is U^g_b=g(tail)U_bg(head)^{-1}. Its actual left-trivialized gauge generator is λ(tail)−Ad_Uλ(head)=−Ξ_Uλ, whereas the routing convention in §3.1 uses +Ξ_U. Therefore, for w_P=log U_P,

    d_U Ξ_U λ = −[λ(base P),w_P] = [w_P,λ(base P)],
    D_U d_U^T G(z) = sum_{base(P)=z} [G(P),w_P],

not sum[w_P,G(P)]. The residual-slot analogue likewise acquires the opposite sign with this Ξ convention. The sign does not affect charge-size estimates or the projection/routing algebra, but the stated exact identity is false for noncommuting w_P,G(P). This is precisely a collision between an actual gauge generator and its negative, not an uncertainty about conventions.

Independently, CCL_U's own correctly scaled G-slot magnitude is

    (6√2 M_γ / ((L−1)n ℓ_χ)) η_F ||G_0^c||∞,
    η_F = n² sup_P |log U_P|.

At ℓ_χ=1/4,d=4,L=3,M_γ=27, a safe summed localization coefficient from the displayed estimates is

    C_loc ≤ 221 + (324√2/n) η_F + 2592 η_ρ.

The file instead prints 221+(648√2/n)+2592η_ρ: it has silently replaced **η_F by 2**. That replacement is available on a sufficiently small regular frame ball (BA-3 gives η_F≤2η+9η²), but not at EVERY configuration without smallness. At arbitrary U it can be O(n²), and the stated derivation then has an O(n) term, not O(n^{−1}). The omitted-factor inference is REFUTED; the unrestricted numerical norm inequality itself is NOT-VERIFIED, rather than refuted by a lower-bound witness. This is a correction of the estimate and its domain; I do not claim an independent lower-bound theorem that every alternative routing must incur O(n). The exact decomposition is still valid wherever the slots/log derivatives exist, but the headline “≈221” is a small-curvature/small-residual specialization. No uniform log-based slot assertion is defined at a principal-log branch cut. The executable tests none of this.

### F5 — L1/L2 provide a genuine local bypass, but only in their specified pair

Verdict: **CONFIRMED** as the following matched-input implication; **REFUTED** for L2's auxiliary displayed sign ΓK=−1+ΓK′. Claim status: **CONDITIONAL** on the full-ball K^(σ) estimates and the flat cc inverse/GV input, and on Faddeev–Popov transversality for the kernel equality.

Anchors: `OFFGLOB55.md:364–407`, “Lemma L1”, “Proposition L2”; E4 `:581–586`; `KFACTOR_OFF55.md:173–206,280–298` (ROW, CCP), `:391–407` (K^(σ)).

Write G=G_♯ and let K be the corrected full-ball Lipschitz constant in E4, not K_rows or K_C separately. Differentiating the source map gives

    ||D S̃(y)u||_N ≤ K(2||y||+s)||u||_(σ),
    𝒦_y=H−P_cc(H−H_y^log)+Γ^TΓ=P_cc H_y^log+Γ^TΓ.

Every differentiated source is flat-cc. Thus T_y=𝓛_Γ^{-1}D S̃(y) obeys ||T_y||≤GK(2r+s)≤1/2 for r≤1/(4GK)−s/2, with the additional chart/ROW smallness minima retained. Neumann inversion gives a unique response to every flat-cc source with bound 2G. Applying D^⊥ to 𝒦_yu=f gives −Γu=0. The full-ball argument genuinely does not use Γy=0 or Γu=0 in ROW/CB; homogeneous-data tangent norms are essential. I have not independently reproved the imported all-orders corrected K theorem or GV-E; this finding is an implication from those estimates, not a new unconditional verification of them.

At a critical y and for K_y^Tf=0, solve 𝒦_yu=P_ccf. Then Γu=0 and g=H_y^log u−f satisfies g=P^TD^⊥g. Differentiated gauge invariance gives H_y^log K_y=0, hence K_y^Tg=0. Since K_y=−Ξ+K′_y, D^⊥g=(K′_y{}^Tg)^⊥. CCP therefore gives J(g)≤cη′J(g), c=2d c_Bern L^{d−1}, so g=0 when cη′<1. This closes the compatibility step without alignment and without a Λ_E^T source completion. The residual g is a finite plain chain; no false conversion of a general divergence-form source to a uniformly bounded J norm is used.

If ΓK_y is invertible, subtract K_y(ΓK_y)^{-1}Γw from any Hessian-kernel vector w. The result lies in Ker Γ and is killed by 𝒦_y, hence vanishes. This proves Ker H_y^log=K_yΛ_*. With ΓΞ=−1 and K_y=−Ξ+K′_y, however, the correct formula is **ΓK_y=+1+ΓK′_y**, not the printed **−1+ΓK′_y** at :390. The small perturbation-of-identity criterion survives.

The exact certified CCP coefficient at d=4,L=3,c_Bern≤59/100 is 3186/25=127.44, and the corresponding sufficient threshold is η′<25/3186. No identification with another file's C_1 or c_1 is used.

### F6 — GP has not defined its advertised operator on source vectors: slot-wise cutoffs depend on the representation

Verdict: **REFUTED** for treating slot-wise M_χ and S_□ as intrinsic operators on source vectors; **NOT-VERIFIED** for the advertised 𝒫_U/E_U endomorphism and uniform GP theorem until this interface is supplied. Claim status: **GAP** in the written operator construction, not a counterexample to existence of a repaired parametrix.

Anchors: `OFFGLOB55.md:299–302`, “acting slot-wise”; `:328`, “on representations”; `:440–456`, “N_𝔇” and “E_U :=”; `KFACTOR_OFF55.md:90–96`, “Source functional on explicit representations”.

The σ source functional is defined on explicit (G,s,j) representations. M_χ multiplies those slots before applying d_U^T or r_U^T. It is therefore not an operator on the underlying source vector S. Already at U=1, choose a spatially constant nonzero 12-plaquette field G on a periodic lattice. Its physical source S=d^TG is **zero**, but

    M_χ S := d^T(χG) ≠ 0

for a nonconstant cutoff χ. This output is already co-closed (d*d^T=0), so P_cc does not remove it. The zero-slot representation of the very same S=0 instead gives zero. An exact rational 3×3 periodic two-dimensional check, embedded unchanged in four dimensions, gave this effect with G=1 and χ(x)=1_{x_1=0}: the physical source is zero, the cutoff current is nonzero, and its divergence is zero at every vertex. No unboundedness claim or approximate arithmetic is involved.

Thus S_□, and hence the inputs used to define 𝒫_U, require a representation as extra input. Calling E_U=P_cc^U DG(U)𝒫_U−1 an endomorphism of cc_U, then taking its Neumann series, silently assumes either a fixed linear bounded selection of representations or a fully specified operator on a Banach space of compatible representations. Neither is stated in the GP inputs. The latter repair is possible in principle, but it must give a linear representation of each error, preserve compatibility, and prove its norm bound for every iterate; merely identifying the physical source does not do that. If instead one uses physical link multiplication χS to make the operator intrinsic, the displayed G/s-slot charge formulas change and require fresh estimates. The plain-current-only script cannot detect this interface defect.

### F7 — The complex a priori estimate is false under E5's explicit real-gauge reading

Verdict: **REFUTED** for AP on the stated complex domain with real frames, and for uniqueness modulo real root-trivial gauges on that domain; **NOT-VERIFIED** for a repaired complex-frame/complex-gauge version. Claim status: the counterexample is **PROVEN**; the complex assembly is **GAP**.

Anchors: `OFFGLOB55.md:163–175` (frame class and complex target), `:486–494` (OFF), `:537–555` (AP/UQ), E5 `:685–693`, especially “my uses of NSL … are real-gauge … uses on frame coordinates”, and E6 `:791–795` (infimum over admissible frames). This distinction is substantive: complex data and configurations require an explicit choice between SU(N) and SL(N,C) gauges/frames.

Exact counterexample already at k=1, L=3, N=2, any sufficiently large T. Put V=1, choose one level-0 site z_0 which is not a level-1 root, H=diag(1,−1), and

    h(z_0)=exp(tH),   h(x)=1 otherwise,   t>0,
    U_b=h(tail b) h(head b)^{-1}.

All plaquette holonomies are exactly 1. Every S4′ path between level-1 roots has transport 1, so every soft residual is exactly zero. The Wilson gradient vanishes at identity plaquettes; the soft gradient vanishes at its exact matching datum. Hence **U is a complex critical configuration with trivial real data**, for every sufficiently small t. Its logs are ±tH on incident links and zero elsewhere; Q log U=0 because the generator vanishes at the coarse roots. This uses a one-level abelian subgroup and exact identities, not asymptotics or numerical evidence.

Identity frames show U∈𝔇_1(R,r_u) for small t. Explicitly, the coarse potential/gradient/Hölder-gradient norm is at most

    √2 t (L + 2L² + 4L^{2+α}) ≤ 258t   (L=3, 0<α<1),

and the linear residual is zero. Choose t=r_u/516. But **no real SU(2) frame can reduce the local potential below 3t**: on an incident link the singular values are e^{±t}, unchanged by unitary gauges at the two endpoints. If exp Y is any gauged link, e^{||Y||op}≥||exp Y||op=e^t, so ||Y||HS≥t; the level-0 coarse potential norm is at least L t=3t. Consequently the infimum r_* over real frame systems in E6 is positive independently of ε.

V=1 belongs to 𝔅^ℂ_1(ε,r_ℂ) for arbitrarily small positive ε. Taking C_0ε<3t contradicts AP's conclusion U∈𝔇_1(R,C_0ε). U is also not SU(2)-gauge equivalent to the identity configuration, again by its nonunit singular values. Thus a uniqueness assertion over complex critical configurations modulo **real** gauges fails on this example. It does not contradict uniqueness modulo the complexified gauge group, since h itself is root-trivial in SL(2,C).

There are two possible repairs, neither made by E5/E6: restrict AP/UQ to real configurations and separately establish a uniform complex induction, or explicitly allow controlled complex frames and complex root-trivial gauges, invoke the **complex** NSL statement, and reprove the transition/routing norm estimates with nonunitary conjugation costs. Ad is then not an exact norm isometry. Holomorphic NK iteration alone does not repair AP's false real-frame assertion. This is the most serious concrete failure found so far: the estimate used to reset constants at every depth has the wrong complex gauge class.

### F8 — OFF's uniqueness proof uses a relative patching lemma that is not one of its premises

Verdict: **NOT-VERIFIED** for UQ even after restricting to real configurations; **REFUTED** for treating the displayed q≤q/2 step as already supplied by the stated single-field FP. Claim status: **GAP** in the implication proof, not a counterexample to real uniqueness.

Anchors: `OFFGLOB55.md:502–507`, “Lemma FP”; `:548–555`, “with Lemma FP, q :=”; E6 `:795–798`, “frames with the same AX root values”.

The local differential estimate bounds w_□ on a smaller core by a constant times its size on Ω_□. To conclude q≤q/2, one needs the **relative** estimate

    max_□ ||y′_□−y_□||_(σ),Ω ≤ C_rel max_□ ||y′_□−y_□||_(σ),core

for consistently matched, root-fixed slice frames, or an infimum version that compares two gauge orbits. FP only says that ONE configuration with small frames on a cover has a small frame on the enlarged box. Applying it separately to Z and Z′ bounds their sizes; it does not bound their difference, and its new frames need not agree with either previously selected family. The transition gauges for Z and Z′ differ, so their differences do not transform simply by one Ad rotation. A relative Lipschitz patching theorem, including the gauge-alignment cost proportional to **||Z′−Z||**, is missing. A cost merely O(η) yields an additive term and cannot force q=0.

E6 addresses root matching at O(η), not this relative estimate. NSL's small-gauge uniqueness applies to two points already known to lie on the same local orbit; using it to establish that they are on the same orbit would assume what UQ is proving. Once local equality and root-trivial overlap gauges have actually been established, the final gluing argument is valid: a stabilizing gauge equal to 1 at one vertex propagates to 1 along every link in a connected overlap. The gap is before that gluing step.

### F9 — What survives of GP: exact compatibility and a conditional parametrix, not the advertised completed estimate

Verdicts: **CONFIRMED** for the source-compatibility algebra, the Neumann conclusion once its endomorphism and bound exist, and GP-R2's finite-dimensional kernel inference; **NOT-VERIFIED** for the uniform GP bound as presently formulated. Claim status: **CONDITIONAL**, with F6/F7 unresolved. A second sign in the displayed local Ward identity is **REFUTED**.

Anchors: `OFFGLOB55.md:445–480`, especially “D^⊥(H^log_ỹu) =”, “Apply P_cc^U”, and “Corollary GP-R2”; `BGT55.md:422–434`; `BFT34_55.md:308–325,329–375`.

The original non-cc cutoff objection is handled at the FIRST inverse call: for any chosen representation, f_□=P_cc^U M_χ f is physically cc_U. Pullback to a frame gives f̂=J_y^T M_g f_□ with K_y^Tf̂=0, and P_cc f̂ is flat-cc. This is precisely the source class L1 can invert. A root-preserving embedding and sufficient support margin preserve the annihilator identity. E3 correctly refuses to assume that a transplanted local configuration is critical.

However, the subsequent recovery of an unprojected local Hessian equation needs a more careful calculation than the printed J-bound on H_yu. Let H=H_y^log, a=∇F(y), u=𝒦_y^{-1}P_cc f̂, and g=Hu−f̂. Then

    P_cc g=0,
    K_y^Tg=−(DK_y[u])^T a,
    D^⊥g=(K′_y{}^Tg + (DK_y[u])^T a)^⊥,
    (1−P^T K′_y{}^T)g=P^T((DK_y[u])^T a)^⊥.

The **plus** sign in the third line follows from K_y=−Ξ+K′_y; the minus sign at OFFGLOB55:462 is incorrect. If the last right side has the asserted uniform chart-coordinate ND bound, CCP(c) gives

    J(g) ≤ (1−cη′)^{-1} J(P^T((DK_y[u])^T a)^⊥).

This uses cancellation of the f̂ terms BEFORE estimating. A general divergence-form source may have an enormous plain-current J norm; one cannot instead price P^TK′^T(Hu) solely by N(Hu) using CCP(c), which is a **J→J** estimate. The chart-coordinate ND estimate (including derivatives of dexp), its transplantation boundary term, and the conversion back to frame source norms must be supplied explicitly. The file's ND is stated in left-trivialized coordinates; NE/CONV alone are not a written proof of all these differentiated chart-product estimates.

Likewise, LOC-cc_U is a localization bound for a **cc input**, not a general bound for P_cc^U on arbitrary commutator sources. The final projection can instead be priced by the aggregate Ward identity

    D_U^⊥DG(U)w = −((DΞ_U[w])^T G(U))^⊥,

with w=𝒫_Uf, using ND directly. At a critical U the entire error is already cc. This repair avoids reintroducing the original non-cc source gap; it must be implemented in the representation-space endomorphism of F6.

Once a genuine E:cc_U→cc_U has norm ≤1/2, R=𝒫(1+E)^{-1} and the factor 2 are exact. At a real critical Z, symmetry and gauge invariance give Ran H_Z⊂cc_Z. A right inverse on cc_Z then gives equality and Ker H_Z=Ran Ξ_Z by finite-dimensional annihilators. No alignment is needed for that deduction. None of these algebraic steps proves the missing uniform error estimate.

The transition assertion also needs its stated qualifications: constant **real unitary** rotations are isometries, but C3 only controls the first linkwise variation. Passing to C^{1,α} field norms, residual weights and differentiated chart terms requires NE/RG-type regularity. Nonunitary complex transitions are not isometries. The weighted m>0 version and BGT55's full covariant source pair are not established here.

### F10 — The one-level lift is sound; the uniform induction still depends on the failed/reset and relative estimates

Verdicts: **CONFIRMED** for the exact lift and the abstract NK residual recurrence; **NOT-VERIFIED** for Theorem OFF as a complete implication from its stated input list. Claim status: lift/abstract recurrence **PROVEN**; the off-global nonlinear theorem **GAP**.

Anchors: `OFFGLOB55.md:509–579` and E4–E6; `PROOF.md:5884`, “Lemma U0 (the exact lift)”; `REVIEW_S22.md:404–411`.

For U^(0)(V), an S4′ path has interior identity links and crosses exactly one relevant block boundary, so every path product is V_c and the soft residual is zero. Plaquettes with fewer than two crossing directions cancel; a corner plaquette equals the coarse V_P. Block-constant extensions give the asserted covariance. One such rough level therefore costs fixed powers of L, not powers of L^k. If the previous-depth field already has a matching regular frame norm, rescaling its potentials/derivatives/residual weights costs at most L^{2+σ}; patching costs the named C_FP(L+2). The resulting C_1 depends on C_0, but not on k. This by itself does not close the induction: without AP the new constant can be a fixed multiple of the old one at every depth.

For NK, with v=R_U G(U), the identity P_cc^UDG(U)v=G(U) gives DG(U)v=G(U)+P_U^TD_U^⊥DG(U)v. ND and a **uniform quadratic remainder in the same fixed norm** give

    N(G(U_next)) ≤ (K_2β²+K_3β) N(G(U))².

If aN(G(U_0))≤1/2, then N(G(U_n))≤N(G(U_0)) 2^{1−2^n}. For n≥1, 2^{1−2^n}≤2^{−n}; including n=0, the sum is ≤2. The claimed displacement bound 2βN(G(U_0)) follows in a common Banach chart. These inequalities could fail; they are not automatic gates. They require the uniform K_2 bound, compatible source representations, fixed or uniformly compared charts, and a controlled domain for R_U. Those are not produced merely by labeling NK “standard”.

For real AP, E6's infimum repair is logically usable only if the map producing improved frames stays in the same **admissible** frame class, including the specified AX root values, and all NSL/FP constants are included. It does not repair the complex counterexample F7. UQ still lacks the relative estimate F8.

A noncircular smallness choice would have to fix R and all norm/patching constants first; then set C_0 from the actual AP estimate, C_1 from the lift, r_u inside every chart/NSL/FP/linearization radius, and finally impose at least

    s_R ≤ s_0,
    ε ≤ min(η_GP,r_u)/(C_1+2β C_G C_0),
    ε ≤ 1/[2(K_2β²+K_3β) C_G C_0],

with s_0 chosen so that r_lin(s_0)>0 and the cutoff configuration fits that radius. A separate bound must keep C_E(1/R+η+N(G))≤1/2 throughout the NK neighborhood. This is a feasible order only after the missing uniform constants and the correct real/complex frame domain exist; the printed ε_*(C_0,C_1) is not an independently verified numerical threshold. There is no justified assertion that these repaired constants are already available.

Finally, this file explicitly omits the tower identification clause and the box-boundary problem. REVIEW_S22's original BFT-2 includes E_k^br, whereas OFF asserts holomorphy of 𝔉_k(Z(V);V) and has not identified it with E_k^br off the global class. Even a repaired OFF result must be banked by its actual clauses, not as the entirety of REVIEW_S22 BFT-0/1/2.

### F11 — This does not retire ALIGN55: the source pairs and response norms are different

Verdict: **CONFIRMED** that alignment is unnecessary for the narrow L1/L2 implication; **NOT-VERIFIED** that this makes the ALIGN55/CODEX_REVIEW_ALIGN programme unnecessary for its actual target. Claim status: the narrow bypass is **CONDITIONAL**; replacement of the full (R2) estimate is **OPEN**.

Anchors: `OFFGLOB55.md:398–419,471–480`; `KFACTOR_OFF55.md:85–97`; `ALIGN55.md:65–80,101–120`; `BGT55.md:86–103,326–336`; the checked review's exact-obstruction discussion is `CODEX_REVIEW_ALIGN.md`, locating “NEC-E's witness and exponent” (no status there is adopted as proof).

The σ source pair permits G at level 0 only, uses J=sum_l π_l for plain currents, and weighs residual slots by L^{(2+σ)m}, m=k−1−l. ALIGN's N pair allows positive-level divergence slots G_l, a weighted max for positive-level plain currents, and residual weight L^θ L^{(2+θ)m}; its response norm additionally includes N_res. NE/CONV in OFF are comparisons between flat and covariant versions of the **σ pair**, not conversions from ALIGN's full N pair.

For σ>θ a residual slot normalized in the latter has σ-size proportional to L^{(σ−θ)m}; no k-uniform inclusion follows from the definitions. Choosing σ=θ removes this particular mismatch. For plain currents the weighted max does control J:

    sum_{l=1}^{k−1}π_l ≤ ||j||_Pc sum_{q=1}^{k−1}L^{−θq}
                         ≤ ||j||_Pc/(L^θ−1).

But positive-level G_l slots still need conversion to the permitted σ representation, and N_res still needs its stated estimate. Neither is supplied by L2(c), whose hypothesis is a plain-current representation. Taking an infimum over all source representations cannot be justified by checking just one restricted representation class.

Accordingly: L2 genuinely bypasses alignment for qualitative nondegeneracy and the specified slice-response estimate on a small global σ-ball. A corrected GP could do the same in a frame-local σ norm at m=0. This does not invalidate a dual obstruction to a particular alignment map, supply ALIGN's full source norm, establish m>0 locality, or prove the off-global nonlinear theorem. Do not retire that programme on this file's present evidence.

### F12 — The argued analytic leftovers, priced individually

Verdicts: **CONFIRMED** for the following elementary cutoff power counts; **NOT-VERIFIED** for the complete remaining analytic package. Claim status: the counts are **PROVEN** in their stated linear frame-coordinate scope; the remaining lemmas are **ARGUED/GAP** as detailed below.

Anchors: `OFFGLOB55.md:409–419,445–451,497–507,557–579`; `BFT34_55.md:360–369`; `BFT_A.md:238–247` (CEN1).

A useful piece CAN be isolated. For a smooth scalar cutoff φ of coarse scale a≥1 with bounded coarse C^{2,α} derivatives, multiplication is uniformly bounded in the **flat homogeneous-data 𝔐^(σ) norm**, 0<σ≤1. The potential/gradient/Hölder components follow by the discrete product rule. For the residual leg,

    r_l(φu)=φ_(l+1)r_l(u)+[Q_l,φ]u_l.

The S4′ average annihilates the commutator for a direction-constant u and affine φ: the straight leg has midpoint average at the coarse-link midpoint; the go/return-leg area term is linear in the centered block offset and averages to zero. Taylor-expand φ to first order and u to a constant on the contour. With h_l=L^{−(k−l)}, own |u_l|=O(h_l||u||), its variation over the fixed L-sized contour is O_L(h_l²||u||); the cutoff-gradient and cutoff-Hessian terms therefore both give

    |[Q_l,φ]u_l| ≤ C(L) h_l³ ||u||/a.

Multiplication by the residual weight yields C(L)L^{(σ−1)m−3}||u||/a, bounded uniformly in k for σ≤1. The same proof applies to an affine configuration norm when its top datum is cut off simultaneously. This banks a precise **frame-log-coordinate W-mult** statement for smooth cutoffs; it does not bank multiplication by an arbitrary merely Lipschitz cutoff, nor comparison across different nonlinear frames.

For the flat physical Hessian commutator, the problematic soft plain row has own size bounded by L² h_l |r_l(u)|/R. Multiplying by L^{3(k−l)} and using |r_l(u)|≤L^{−(2+σ)(k−1−l)}||u|| gives exactly

    π_l ≤ C L^{4+σ} L^{−σ(k−l)} ||u||/R.

Thus the exponent correction already adopted in OFF is right, and sum_{q≥1}L^{−σq}=1/(L^σ−1) is finite. The residual-type commutator has the same favorable σ≤1 bound as above. This is a power-count check, not verification of every Hölder leg, the Γ/♮ commutator, the nonlinear background derivative, or the common error representation needed by GP.

The remaining obligations must stay separate:

| Input | What is supported here | What remains |
|---|---|---|
| NE | Near-identity dexp and fixed real constant rotations suggest the local comparison | Full covariant C^{1,α}/residual/source equivalence, complex norm costs, and uniform constants |
| CONV | Plain-current CCP estimate; exact annihilator identity K_y^T J_y^TM_g S=0 | G- and s-slot representations, cancellations, Hölder estimates, and every-representation bound |
| ND | Exact differentiated Ward identity; aggregate projection strategy in F9 | J bound for G/s sources, the differentiated chart version, and transplant boundary terms |
| W-comm^σ | Flat physical-Hessian scale counts above are summable | Γ commutator, Hölder parts, nonlinear frame-background version and representation lift |
| W-mult^σ | Uniform flat/frame-log multiplication for smooth cutoffs as proved above | Any stronger covariant or nonsmooth-cutoff reading |
| RG | C3 proves linkwise variation, and real constants cost no norm | Full scaled gauge regularity, root constraints, complex extension |
| FP | Plausible single-field patching mechanism | Quantified constants and admissibility; especially a relative, Lipschitz, root-preserving version for UQ |
| UHL-fine | Corrected axial C^α and explicit axial derivative-loss witness | Nonlinear Coulomb bootstrap; the loss does not refute that theorem |

Calling these “all local” does not establish them. In particular a family of fixed-coarse-size boxes has arbitrarily many fine sites as k grows; finite coarse range alone gives no uniform Hölder or routing norm.

### F13 — Disposition of the five advertised REFUTED items

The verdict here concerns OFF's stated refutation, not a claim that the quoted source theorem was proved. NSL55/GV55/HANDOFF were not separately read; their claims are evaluated only as quoted at the OFF anchors below.

| Item and current anchor | Review verdict | Derivation / limit |
|---|---|---|
| P5, `OFFGLOB55.md:606–611`; `HESSREL.md:502–505,515–520` | **CONFIRMED**, conditional on the stated BFT-1 regularity/soft matching | A field within s′ of any flat field on every link has contractible-loop holonomy distance ≤length×s′, by telescoping the product against the flat product. The C4 square has distance √2π. At level k−1, two S4′ paths of one coarse link differ by finitely many L-dependent plaquettes; BFT-1 makes their products O(ε)-close. The polar root map is locally Lipschitz near a common unitary (expand its inverse square root near 1), and the soft residual is O(ε), so a chosen root-to-root path is O(ε)-close to V_c. Around 4R_ε coarse links the error is O(R_ε ε)→0. FLAT-REF with s′=O(ε/L) instead makes the lifted contractible loop O(R_ε ε)-close to 1: contradiction. For N>2 the loop is diag(−1,−1,1,…,1), not −I_N. This is a global obstruction, not a refutation of a local Uhlenbeck theorem. |
| P12, `OFFGLOB55.md:636–640`; `BGT55.md:446–449` | **CONFIRMED** only for a new σ-pair mechanism; **NOT-VERIFIED** as replacement of full (R2) | F5 supplies a different, cc-projected derivative and exact compatibility argument. This defeats a universal “no new mechanism” assertion. It does not alter the limitation of the particular Feynman map analyzed in An-3, nor provide the missing norm conversions in F11. |
| P13, `OFFGLOB55.md:641–644` | **NOT-VERIFIED** as a completed necessity refutation | Flat NSL can be used on an already regular, small REAL frame configuration. That conditional observation does not supply the frames, relative patching, or complex extension used by OFF. F7 directly defeats the claim that real-gauge NSL suffices throughout the complex proof. |
| P14, `OFFGLOB55.md:645–647` | **NOT-VERIFIED** as a completed replacement reduction | A valid alternative could replace the old route's inputs. This file has not yet proved that alternative with its stated domains and interfaces. The old route's status list is not itself a necessity theorem. |
| P19, `OFFGLOB55.md:656–658` | **CONFIRMED** for the terminology only | The displayed class assumes small plaquette curvature and allows arbitrary holonomy. Calling this the large-curvature regime is incorrect. The claimed supersession of the old input list remains NOT-VERIFIED for the reasons above. |

### F14 — Citation drift, provenance, and what the gates did not decide

Verdict: **CONFIRMED** that cited line ranges have drifted; **NOT-VERIFIED** for imported status/provenance beyond the specific reads and independent derivations recorded here.

`OFFGLOB55.md:42` gives PROOF's AX range as 5521–5540. The first string search in this review located the heading at **5526**. A later search located it at **5528**, with its last coarse-link sentence at **5547**; line 5521 then lay in the preceding N5-cov proof. Thus the quoted range is not a current full-lemma range. The file changed during this review; the locating strings, not a uniform offset, control.

A more decisive stale pointer occurs in the selected input `KFACTOR_OFF55.md:109`: “PROOF l.6667–6693 (CL-0)–(CL-4)”. Reading that range begins in the previous vertex discussion; the actual “Proposition COMP (the composite contraction)” was found at **6699**, with the CL-4 correction at **6719** and its scope through **6724**. The cited range does not reach the proposition. No numerical source line was accepted without a string search. Earlier PROOF numbers in this report record the reads at that time; the strings disambiguate the moving file.

Scientific files actually read: OFFGLOB55, REVIEW_S22, bounded PROOF ranges, bounded BFT_A ranges, BFT34_55, HESSREL, BGT55, ALIGN55, and bounded CODEX_REVIEW_ALIGN ranges; the two selected additional scientific files were KFACTOR_OFF55 and og55_1_route.py. Procedure reads were SCIENCE_WORKFLOW and the packaged review-loop SKILL.md selected from the session catalogue. This is the complete access account; no claim is made to have read NSL55, GV55, CODEX_REVIEW_NSL, CODEX_REVIEW_KOFF, the original criteria/log files, any snapshot, audit ledger, or full PROOF/BFT_A/BFT_B. CODEX_REVIEW_ALIGN was visibly still receiving incremental additions; its statements were not used as authority for the mathematical findings here.

Every mutation in this review was to CODEX_REVIEW_OFFGLOB.md. No git command, source edit, external search, floating arithmetic, numpy/BLAS operation, long numerical job, or background worker was run. The failed initial `python` command was immediately replaced by `python3`, and the pre-stated record discloses the source exposure before successful creation. The report uses the actual 24/20 rerun result; it does not validate the script's preregistration timestamps or original resource-use claims.

Final-read OFFGLOB55 content fingerprint (SHA-256, 2026-10-29T04:59:35.059419+00:00): `c55f87098d048ca96949fbb2143e3d5a8062f6149a39a541e2ea4e8f67fed17b`. This identifies the source at completion without using git; moving PROOF line numbers remain governed by their locating strings.

## Summary table

| Finding / target | Verdict | What may be used |
|---|---|---|
| F1: data frames, C4, C6 | **CONFIRMED**, with a **REFUTED** gauge formula / minor arithmetic equality | Quantified local equivalence, √ε obstruction, corrected flat-torus construction |
| F2: HR_U / LOC algebra and og55_1 | **CONFIRMED** | Exact real covariant charge routing and decomposition for a supplied representation; 24 identities / 20 controls reproduced |
| F3: axial regularity | Printed coefficient **REFUTED**; corrected bound and U2 **CONFIRMED** | Replace 1.1ε_0 by 3.3ε_0 in U1(b); retain the axial derivative-loss witness |
| F4: CCL / localization norm | Signs and omitted-factor inference **REFUTED**; unrestricted norm inequality **NOT-VERIFIED** | Corrected charge identities; explicit η_F,η_ρ-dependent estimate in its domain |
| F5: L1/L2 | **CONFIRMED** as a matched-input implication | Small-global-σ-ball slice inverse and conditional nondegeneracy, with ΓK sign corrected |
| F6: GP source-space endomorphism | Intrinsic slot cutoff **REFUTED**; GP interface **NOT-VERIFIED** | Representation-aware algebra only; define and bound the lifted error operator before Neumann iteration |
| F7: AP/UQ on complex fields with real frames/gauges | **REFUTED** | Exact complex pure-gauge counterexample; corrected complex formulation still needed |
| F8: real UQ relative patching | **NOT-VERIFIED** | Final overlap gluing only after a relative estimate establishes local equality |
| F9: GP / GP-R2 | Formal compatibility/kernel deductions **CONFIRMED**; uniform theorem **NOT-VERIFIED** | Conditional Neumann and annihilator implications, corrected Ward sign |
| F10: depth induction / OFF | Lift and abstract NK **CONFIRMED**; OFF **NOT-VERIFIED** | One-level starting mechanism; no completed uniform real/complex induction or original BFT-0/1/2 |
| F11: alignment retirement | **NOT-VERIFIED** for ALIGN's full target | Narrow no-alignment σ-pair route only |
| F12: leftovers | Cutoff/counting sublemmas **CONFIRMED**; remaining package **NOT-VERIFIED** | Smooth frame-log W-mult; summable corrected flat commutator powers |
| F13: P5/P12/P13/P14/P19 | Scoped P5/P12/P19 **CONFIRMED**; P13/P14 necessity refutations **NOT-VERIFIED** | The precise restrictions in F13, not the blanket five-item refutation tally |
| F14: line pointers / provenance | Drift **CONFIRMED**; uninspected provenance **NOT-VERIFIED** | Locating strings and actual command output only |

Numerical and sign corrections not already made by E1–E6:

- U1(b): **1.1ε_0 → 3.3ε_0** for the lane's ℓ∞ pointwise Hölder norm. Exact violating example: actual **1/8**, printed bound **11/240**.
- E1's exact square: **0.195 → 0.194481** for 0.441²; its comparison with 1/6 survives.
- LOC's unrestricted G correction: **648√2/n → (324√2/n)η_F**; a safe general coefficient is **221+(324√2/n)η_F+2592η_ρ**. The printed coefficient presupposes η_F≤2.
- L2's ΓK leading sign: **−1 → +1**. CCL's G charge is **[G,w]**, not [w,G]. GP's log-coordinate Ward defect has **+DK^T∇F**, not minus.
- C6's gauge product: **T_V T_W^{-1} → T_W^{-1} T_V** in the stated convention.

**Single most dangerous unverified obligation:** a uniform, Lipschitz, root-preserving **relative** frame-patching estimate in the full σ norm, strong enough to compare two local slice representatives and justify UQ's q≤q/2 step. Single-field FP does not state it; O(η) transition costs alone do not imply it.

## Exactly what may be banked

1. **PROVEN:** the bounded-box axial data estimate and its two class inclusions; C4's quantified √ε lower-bound witness; the flat-torus 3π√N/T construction with the corrected gauge order; and the conditional incompatibility of O(ε) FLAT-REF with the stated BFT-1 matching on that witness.
2. **PROVEN:** U1's uniform sup and axial-frame pointwise C^α bounds with the corrected 3.3ε_0 term; U2's exact n^{1−α} axial gradient growth and uniformly regular abelian Coulomb alternative. No nonlinear UHL-fine theorem is banked.
3. **PROVEN:** real SU(N) hierarchical covariant routing, gauge covariance, the bare-charge bound, and exact cc localization for an explicitly supplied slot representation, with corrected generator signs and the stated curvature/residual-dependent coefficient. The 24/20 script result supports only its finite algebraic scope.
4. **CONDITIONAL:** L1 and L2's small-global-σ-ball slice inverse and nondegeneracy implication from the corrected full-ball K/GV estimates, CCP and Faddeev–Popov transversality. This is a genuine limited no-alignment mechanism. It does not supply the missing covariant/full-source comparisons or the off-global theorem.
5. **PROVEN:** the one-level exact lift; the abstract NK recurrence under its matched uniform hypotheses; smooth scalar multiplication in the flat/frame-log σ norm; and the corrected, summable flat commutator power counts. **CONDITIONAL:** the formal GP Neumann/kernel consequences once a genuine bounded compatible error operator has been constructed.
6. **PROVEN counterexamples / corrections:** U1(b)'s printed numerical bound, real-frame AP on complex pure gauges, the non-intrinsic nature of slot cutoffs, the nonabelian gauge-product order error, and the generator/sign and curvature-factor corrections above. These refute precise printed assertions, not the possibility of a repaired off-global construction.

**Not banked:** Theorem OFF as a completed implication in its present real/complex frame conventions; uniform GP as a defined source-space inverse; real UQ; full BGT55 (R2); the original BFT-0 identification or E_k^br analyticity off 𝒞_glob; BFT-3/4; the non-wrapping-box boundary theorem; or retirement of ALIGN55. The main off-global construction remains **GAP**, with viable local components and explicit repair obligations.
