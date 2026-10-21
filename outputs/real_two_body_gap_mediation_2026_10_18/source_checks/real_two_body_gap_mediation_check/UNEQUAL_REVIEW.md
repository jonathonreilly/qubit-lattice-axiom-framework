> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Distinct check of unequal-coupling gap mediation

**Disposition: SUPPORT the frozen unequal-coupling extension; no required correction found.** Its exact full-space error, positive counterterm, phase and finite-time mistuning bounds survive reconstruction. Removing equality of the two couplings does not remove the supplied nonlinear counterterm calibration. Section 6 below additionally derives an unequal-coupling weak-background interface; that section is reviewer mathematics, not a claim that the frozen author source already contains it.

## 1. Identity, scope and exposure

The complete checked source is N/real_two_body_gap_mediation_probe/UNEQUAL_COUPLINGS.md, 6121 bytes, SHA256 `84ddf7968a0f75de54b36d8ac48a2c0917ba7fa49933191c74a92298ebd9c7f5`. Here N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The unchanged equal-coupling source `d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258` and weak-background addendum `eb61571fc02140def4058ddc71cf55e3b9329dde25452fb4fadc07b6bef4d651` were fully read in the preceding checks. Their corresponding reviews `38ecd127adacb06f65ca6f827821f472969b677a737007173bb383c207b30947` and `7819401a01a914a1e59775e30d596f311e0796456914fa03654a0ba6394edf40` are preserved and reused at their exact scopes, not counted as fresh checks. The unequal formulas and all changes are reconstructed here.

ROOT proposed the unequal square identity and mistuning comparison. I did not author this source, but have shared design and campaign exposure, including the preceding two reviews. This is distinct same-model, source-exposed checking, not blind, model-diverse, retained-audit or publication certification. The domain is exactly 0<u,v<1, the literal fixed old K=2I+Z₁Z₂, four qubits, all outputs and arbitrary passive references. An effective joint interaction is the comparison target; no old-only common-output gate is presumed.

## 2. Positive inventory and exact calibrated algebra

Write T₁=Y₁Y_a, T₂=Y₂Y_b, Z=Z₁Z₂, Q=X₁X₂Y_aY_b. The prior elementary identity R=ZQ=−T₁T₂ still holds. T₁,T₂ commute and square to I; Z anticommutes with each. Thus R commutes with both couplings and with Z. On R=r, T₂=−rT₁, so

    V=uT₁+vT₂=(u−rv)T₁,
    V²=(u²+v²)I−2uvR.                              (R1)

For 0<u,v<1 the supplied number a=sqrt[(1−u²)(1−v²)] lies strictly between zero and one. Hence all four actual blocks

    K, (1−a)(I−Z), u(I+T₁), v(I+T₂)

are positive and real on their complete two-qubit supports. Their norms are 3, 2(1−a), 2u and 2v. The same nearest-neighbor square geometry has four blocks on three distinct edges. Old-site loads are respectively 3+2(1−a)+2u and 3+2(1−a)+2v; clock-site loads are 2u and 2v. Taking the maximum gives exactly the claimed sufficient cap. K is counted once.

Summing the block identity coefficients gives 2+c with c=u+v+1−a. The nonscalar part is A=aZ+V. Since {Z,V}=0 and a²=1−u²−v²+u²v²,

    A²=a²I+V²=(1+u²v²)I−2uvR
       =(Z−uvQ)².                                  (R2)

The calibration uses the actual supplied u,v. It is a positive but specifically tuned counterterm, not an identity satisfied by independently unspecified coefficients.

## 3. Spectral signs and exact propagator norm

Set κ=uv, Ω_r=1−rκ and ν_r=|u−rv|. Both Ω_r are positive because κ<1, and

    a²+ν_r²=(1−rκ)²=Ω_r².                          (R3)

Each R sector has dimension eight, since R is a nonidentity Pauli string. On a sector with ν_r>0, X'_r=V/ν_r is a selfadjoint real involution anticommuting with Z. Since Q=rZ there,

    A_r=aZ+ν_rX'_r,
    (Z−κQ)_r=Ω_r Z.

When ν_r=0, (R3) and a>0 imply a=Ω_r, and the generators agree. This case includes r=+1 and u=v. The positive signs are essential: equality of squares alone would not determine the comparison generator.

For a nontrivial sector, the exact exponential has cosine cos(Ω_rt) and sine coefficient (aZ+ν_rX'_r)/Ω_r. Subtracting the comparator cancels the cosines. Squaring the remaining real Pauli combination gives

    [(a/Ω_r−1)Z+(ν_r/Ω_r)X'_r]²
       =[2−2a/Ω_r]I.

Therefore, with d_r=sqrt(2−2a/Ω_r),

    ‖e^(−itH)−e^(−ict)e^(−it(K−κQ))‖
       =max_(r=±1) d_r |sin(Ω_rt)|                  (R4)

for every real t, including negative times and the zero-coupling-difference sector. This is an exact full-space norm. The common scalar 2+c was handled identically on both sides. Tensoring any passive identity leaves the norm unchanged. Twice (R4), capped at two, is a valid unhalved complete channel upper bound; it is not asserted to be the exact channel distance.

Since Ω_−≥Ω_+ and a>0, d_−≥d_+. The uniform upper bound d_− is valid without simultaneous sine maxima. In fact the r=−1 sine alone attains one at appropriate times, but that strengthening is unnecessary. At u=v=λ, a=1−λ², d_+=0 and d_−=2λ/sqrt(1+λ²), reproducing the accepted source including its phase and frequency.

For u,v≤1/2, a≥3/4. Rationalizing the difference gives

    d_r²=2ν_r²/[Ω_r(Ω_r+a)]≤ν_r²/a²,

because Ω_r≥a>0. Thus d_−≤(u+v)/a≤4(u+v)/3. The endpoint u=v=1/2 is included in this estimate; the broader exact formula still requires only u,v<1. At a fixed positive mediated angle b and T=b/(uv), [K,Q]=0 yields the comparator e^(−icT)e^(−iTK)e^(ibQ). The literal scalar and the whole elapsed K are retained; unequal small couplings do not by themselves prevent T from becoming large.

## 4. Mistuning, scalar and tolerance allocation

For real δ with 1−a+δ≥0, replacing the counterterm changes H by δ(I−Z). Consequently

    H_δ=(2+c+δ)I+A−δZ.

The displayed actual-scalar comparator is e^(−it(c+δ))e^(−it(K−κQ)). After removing the same scalar on both sides, the difference from the nominal generator is only −δZ, of norm |δ|. Duhamel therefore adds at most |δ||t| to (R4). The source does not claim an unchanged exact square identity or exact frequency matching for δ≠0.

If the comparator instead keeps nominal c, the extra common phase has norm error |e^(−itδ)−1|≤|δ||t|. Adding this second charge is safe. Unknown δ still cannot be silently used as a known calibrated phase, much less an input-dependent fitted phase. The actual-scalar theorem is a conditional statement about that actual parameter.

For |t|≤T_max, u,v≤1/2 and u+v≤3ε/8 give nominal error ≤ε/2. Requiring |δ|≤ε/(2T_max) gives the other ε/2. Hence the advertised total ≤ε is correct, provided positivity and the actual cap are also checked. At T_max=b/(uv) this becomes |δ|≤εuv/(2b), with b>0. The source's earlier example assumes T_max>0; no division-by-zero policy at b=0 is needed. The mistuned old-site counterterm load is 2(1−a+δ), not its nominal value. This is a sufficient precision condition, not a lower bound on required precision or a derivation of fabrication control.

## 5. Product seed and physical limitations remain unchanged

The effective interaction is still Q=X₁X₂Y_aY_b with the entire Y-pair operator. For |00>_ab the effective output at angle b is

    cos b ξ⊗|00>−i sin b X₁X₂ξ⊗|11>.

For general old ξ this is entangled, including the nonzero two-Schmidt-coefficient example at b=θ. Unequal couplings do not supply a +1 Y_aY_b eigenstate, return a common clock output, or conserve a one-head clock sector. Thus the claimed relaxation removes only exact equality u=v, while retaining the nonlinear counterterm, declared matrix suppliers and joint-output interpretation. No assembly, native dynamics, preparation, interval W theorem or permanent halt follows.

## 6. Additional reviewer derivation: unequal dressing with a weak background

This section answers the separately requested possible extension; it is not attributed to the frozen author text. Set β_r∈[0,π/2) by cos β_r=a/Ω_r and sin β_r=ν_r/Ω_r. When ν_r=0 put D_r=I; otherwise put

    D_r=exp[−(β_r/2)ZX'_r]

on the r sector. Define D by the direct sum of these two sector operators. Each is real orthogonal and sends Z to cos β_r Z+sin β_r X'_r. Therefore the exact full-space identity is

    H=cI+D(K−κQ)D†.                                 (R5)

Moreover

    d_D:=‖D−I‖=max_r 2sin(β_r/4)=2sin(β_−/4).

The last equality follows from cos β_r=a/Ω_r and Ω_−≥Ω_+, which order β_−≥β_+. Since β_−=arctan[(u+v)/a],

    d_D≤β_−/2≤(u+v)/(2a).                           (R6)

All these are complete-space statements and tensor with spectator identity. Let B be any bounded selfadjoint background on that joint space. Then

    H+B=cI+D[H_eff+D†BD]D†,  H_eff=K−κQ,
    ‖D†BD−B‖≤2d_D‖B‖.

Paying the two outside dressing factors and applying Duhamel gives

    ‖e^(−it(H+B))−e^(−ict)e^(−it(H_eff+B))‖
       ≤2d_D(1+|t|‖B‖)
       ≤(u+v)/a · (1+|t|‖B‖),                     (R7)

again capped at two if desired. With B=κB₀ and |t|≤b/κ, the bound is ≤(u+v)/a·(1+b‖B₀‖), at most 4(u+v)(1+b‖B₀‖)/3 when u,v≤1/2. A uniform weak-background claim requires a uniform bound on ‖B₀‖; an extensive sum is not automatically bounded by its local strength. For physical positivity/reality/locality, B must separately be supplied in that block class and its incident norms counted. No installation of D or D†BD is assumed: they are proof transformations only.

This added derivation is conditional on the same exact calibration as (R5). It does not validate simultaneous isolated gadgets sharing K. Its status is explicitly reviewer-derived mathematics, not another independent check of itself or an author-source claim.

## 7. Actual verification record

The complete new source was read; its source identity and the unchanged earlier review identities were checked. The changed sector algebra, spectral signs, error coefficients, scalar, cap and mistuning policy were reconstructed analytically. The additional dressing extension above uses the already checked general conjugation argument with the explicitly derived unequal angles. No numerical solver, scientific executable, scan, external search, delegation or model/effort override was used. This report was read back completely. Only UNEQUAL_REVIEW.md was written; prior sources and reviews, Git, canonical/checkpoint files and editable prompts remain unchanged. This is scoped research-decision evidence, not retained certification or a publication instruction.
