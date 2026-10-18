# Distinct check of the finite-network vacancy interface

**Disposition: SUPPORT at the stated conditional single-link scope; no required correction found.** The spectator extension, global one-head restriction, positive compensation and finite-network error/cap allocations are valid. The actual dynamics need not conserve head number; its extra-head leakage is included in the complete-output bound. No released logical gate, common outgoing profile, return suppression or halt has been constructed.

## 1. Sources and exposure

The complete new source is N/counterterm_free_gap_mediation/NETWORK_VACANCY_INTERFACE.md, SHA256 `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e`, where N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. It was read fully and hashed.

The unchanged local source `7ce327a279b7c89e6ee48dd94555a78bdb357dd183b4333618f958e4d387da00` and exact mediator source `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34` were fully read in the preceding checks. Their reports are respectively `f1e754ed52ccb2ea27c3831659467a3f94f51d8ce75b26c8b7ce882a4b7e9df3` and `80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70`. Their exact local rotation and physical weak-background interface are reused at the checked scopes, not counted as newly proved. The source's historical pending-review wording is preserved; the local check now exists.

ROOT proposed the global-one-head and positive-compensation route and disclosed this design. I did not author the new source but have shared campaign and prior-review exposure. This is distinct same-model source-exposed reconstruction, not blind, retained-audit or native-realization certification. The finite network, listed geometry and positive block inventory are supplied hypotheses; no unspecified infinite or growing-network limit is used.

## 2. Full-space extension and the correct invariant sector

Let L≥2 be the number of clock qubits, N=Σ_jn_j, and P₁ its one-head projector. The checked pair rotation D, extended by identity on all other clocks and passive systems, remains real orthogonal with ‖D−I‖≤1/U and

    H_pair=D H_diag D†,
    H_diag=−XJ_ab−rP00+(U+r)P11,
    r=(sqrt(U²+4)−U)/2≤1/U.

For any bounded selfadjoint network B, the full-space subtraction gives ‖D†BD−B‖≤2‖D−I‖‖B‖. Duhamel and both outside dressing factors therefore give

    ‖e^(−is(H_pair+B))−e^(−is(H_diag+B))‖
       ≤min{2,(2/U)(1+|s|‖B‖)}.                   (R1)

This step uses the full network operator norm, not ‖P₁BP₁‖ or a local one-head proxy. It does not require local no-double invariance or global number conservation of the actual generator. Pair creation from a local vacancy can take an initial global one-head state to three heads; that actual leakage is precisely among the outputs controlled by (R1).

For the stated clock-only B with [B,N]=0, H_diag+B commutes with N: J_ab exchanges a local head and the two local projectors are occupation diagonal. Thus its comparison dynamics preserves P₁. On P₁, P11=0 and P00=I−n_a−n_b, giving the exact restriction

    H_one=−XJ_ab+B|_(P₁)−rI+r(n_a+n_b).            (R2)

B may move a head outside or into the pair. That does not invalidate (R2), because the invariant space is the global one-head sector, not the pair's local one-head subspace. Restricting the already full-space (R1) to initial P₁ states yields a complete-output isometry estimate without a final projection.

## 3. Positive compensation, full norm and phase

The proposed compensation B_comp=rΣ_(j outside a,b)n_j is a sum of positive real onsite blocks. On P₁ it equals r(I−n_a−n_b) and therefore cancels the entire last two terms in (R2). The compensated restriction is exactly

    H_one,comp=−XJ_ab+B|_(P₁).                      (R3)

No common scalar remains from that cancellation on P₁; introducing another e^(irs) factor there would double count. Without compensation, the −rI+r(n_a+n_b) operator must remain as in (R2), including its relative vacancy phase.

On the full network Hilbert space the commuting occupations can all equal one. Hence

    ‖B_comp‖=r(L−2),
    ‖B+B_comp‖≤‖B‖+r(L−2).                         (R4)

This is the appropriate norm in (R1). It is not the smaller one-head norm r. For L=2 the sum is empty, its norm is zero, and P00 vanishes on P₁; the formulas reduce correctly. Positivity does not authorize ignoring the extensive compensation cost for larger L.

## 4. Physical composition, outputs and inventory

The checked exact mediator interface extends by identity to the other clocks and compares a physical background b_eff(UP11+B_tot), with B_tot=B or B+B_comp, to its effective joint generator. Its norm is bounded by b_eff(U+M_B), where M_B=‖B‖ or ‖B‖+r(L−2). With s=b_eff t, the first error is

    164λ[1+|s|(U+M_B)].

The comparator factors as e^(−it c_eff)e^(−itK), pair/network evolution, and effective mediator aging e^(−it2a_eff n_m). This factorization uses clock-only B and [K,X]=0. Applying (R1) to the pair/network factor and then restricting initial clocks to P₁ gives total error

    E(s)=164λ[1+|s|(U+M_B)]
                     +(2/U)(1+|s|M_B).             (R5)

The target is exactly the source's evolution by (R2) or (R3), embedded back into the full output. All actual extra clock heads and mediator errors remain in the difference norm. Arbitrary old/clock/mediator correlations with initial clock support in P₁ and passive extensions are covered. The mediator need not be prepared, but its comparison evolution remains effective aging rather than bare gap four or reset.

The proposed physical layout has L clock qubits plus two old qubits and one mediator, totaling L+3. The base five blocks involve the old pair, the selected clock pair and the mediator. Adding the repulsion and q listed B blocks gives 6+q blocks without compensation. With L−2 additional onsite compensation blocks this becomes L+4+q. These counts agree at L=2. A physically supplied embedding must keep all clocks distinct from old/mediator sites and realize each declared edge; no existence of an arbitrary requested embedding is inferred.

The base old and mediator loads are unchanged. Each endpoint a or b receives 2λ+b_eff U plus b_eff times the sum of norms of B blocks incident on that endpoint. Each outside clock receives only its B-block incident sum, and additionally b_eff r if compensated. Repeated supports count as separate listed blocks. This agrees with the source and does not merge loads or use restricted norms. A positive real local decomposition of B is required for the physical statement; abstract selfadjoint number conservation alone supplies no such hardware.

## 5. Explicit simultaneous error and cap budget

Let b_norm=‖B‖ and d=L−2 with compensation, zero otherwise. Since r≤1/U, M_B≤b_norm+d/U. For |s|≤S, the second term of (R5) is bounded by

    2(1+S b_norm)/U+2S d/U².

The first U lower bound 16(1+S b_norm)/ε makes its first summand at most ε/8. The second U lower bound sqrt(16Sd/ε) makes the second at most ε/8 (when Sd=0 that summand is zero). Thus the clock contribution is ≤ε/4. The additional U≥1 is compatible with both.

Choosing

    λ≤min{10⁻³, ε/[656(1+S(U+b_norm+d/U))]}

makes the first contribution at most ε/4. Consequently E(s)≤ε/2 uniformly on the stated scaled horizon. Twice this is a valid unhalved complete channel upper bound ≤ε, without postselection.

For cap feasibility set C_load=U+Σ_l‖B_l‖+d/U. Because g<3λ and b_eff≤λ², the crude sitewise upper bound 4+8λ+λ²C_load covers old, mediator, pair endpoints and all outside clocks. For a compensated outside clock, r≤d/U when d≥1; when d=0 there is no outside compensation term. Thus no endpoint is missed. The further choices

    λ≤(Λ−4)/16,
    λ≤sqrt[(Λ−4)/(2C_load)]

make 8λ and λ²C_load at most (Λ−4)/2 each. All budgets are simultaneous for a fixed finite specified network, finite S and Λ>4. This includes S=0 and L=2 without singular cases. It is a sufficient feasibility construction, not a uniform cost claim for networks whose size or block norms grow without bound.

## 6. Scope and actual verification

The source extends one controlled hopping link to a supplied finite number-conserving target network and compensates its vacancy energy with positive outside onsite terms. It permits target transport away from the pair, but does not choose a graph realizing literal W, prove a common outgoing profile, bound returns or certify released-gate retention. Combining several mediated links sharing the old K also remains unproved. No native initialization, capture, reset or permanent halt follows.

I fully read the new source and reconstructed the spectator norm, target invariance, compensation identity/full norm, physical two-stage comparison, counts, site loads and each allocation analytically. No scientific executable, numerical solver, scan, external search, delegation or model override was used. Hashing and complete report readback were performed. Only NETWORK_VACANCY_REVIEW.md was written; predecessor reports, sources, Git, canonical/checkpoint files and editable prompts remain unchanged. This is scoped mathematical decision evidence, not retained certification or publication approval.
