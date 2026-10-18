# Distinct check of the weak-background addendum

**Disposition: SUPPORT at the stated conditional scope; no required correction found.** The explicit orthogonal dressing, its distance from identity, and the arbitrary bounded selfadjoint-background comparison are correct. The resulting O(λ) bound on the mediated timescale requires a uniform bound on B/λ². Mathematical selfadjointness does not by itself supply positive local hardware or waive incident loads.

## Sources and exposure

The complete new source is N/real_two_body_gap_mediation_probe/ADDENDUM.md, SHA256 `eb61571fc02140def4058ddc71cf55e3b9329dde25452fb4fadc07b6bef4d651`, 5645 bytes. Here N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. It was read in full and hashed. The unchanged source PROPOSAL.md has SHA `d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258`. Its full-sector algebra, complete propagator comparison and physical inventory were just checked in REVIEW.md, SHA `38ecd127adacb06f65ca6f827821f472969b677a737007173bb383c207b30947`; that report is preserved unchanged and is reused at its exact scope, not counted as fresh evidence.

ROOT proposed the weak-background conjugation route. I did not author the addendum, but have shared design and campaign exposure and read its formulas before reconstructing them. This is distinct same-model, source-exposed mathematical checking, not blind, model-diverse, retained-audit or publication certification. The task retains 0<λ<1 and the literal fixed old energy unit. All additional finite spectator factors are included explicitly in the operator domain, with D tensored by identity there.

## 1. Exact complete-space dressing

Reuse Z=Z₁Z₂, Q=X₁X₂Y_aY_b, R=ZQ, P_±=(I±R)/2, V=λ(Y₁Y_a+Y₂Y_b). Let

    F=ZV/(2λ),  α=arctan λ.

The previously checked commutators imply that F commutes with P_±, vanishes on P_+, satisfies F†=−F and F²=−P_-. All these are full-space identities: V²=4λ²P_- and {Z,V}=0. Since Z,V are real, F is real antisymmetric. Consequently

    D=P_+ + cos α P_- − sin α F,
    D†=P_+ + cos α P_- + sin α F

give DD†=D†D=P_+ +(cos²α+sin²α)P_-=I. The definition is real orthogonal on the entire gadget, not merely after preparing a sector. On P_- it is exp(−αF); on P_+ it is identity.

Writing X'=V/(2λ) on P_-, direct multiplication gives

    DZD†=cos(2α)Z+sin(2α)X'.

For example the cross term has the positive sign because ZF=X' and FZ=−X'. With cos(2α)=(1−λ²)/(1+λ²), sin(2α)=2λ/(1+λ²), and H_eff=K−λ²Q, this proves on P_-

    D H_eff D†=2I+(1−λ²)Z+V.

On P_+, V=0, Q=Z and D=I, giving the same identity there. Thus on the full space

    H=cI+D H_eff D†,  c=2λ+λ².                     (R1)

Both the physical identity shift and K's scalar 2I occur exactly once.

The nontrivial eigenvalues of D are e^{±iα}. They occur because F²=−I on the nonempty P_- space (real antisymmetry also pairs the signs). Hence

    d=‖D−I‖=2 sin(α/2)≤α≤λ.                       (R2)

There is no factor-of-two confusion between this one-endpoint norm and the two dressing endpoints in a propagator comparison.

## 2. Arbitrary bounded background, signs and time dependence

Let B be bounded and selfadjoint on the full gadget plus any declared finite spectator. It may couple the two, fail to commute with all the sector labels, and change ancillary occupation. With B'=D†BD, equation (R1) gives exactly

    H+B=cI+D(H_eff+B')D†.

The expansion in the source is algebraically correct:

    B'−B=D†B(D−I)+(D†−I)B,

so ‖B'−B‖≤2d‖B‖. B' remains selfadjoint. For any real t, finite-dimensional Duhamel (or the bounded-perturbation formula) therefore gives

    ‖e^(−it(H_eff+B'))−e^(−it(H_eff+B))‖
       ≤2d |t| ‖B‖.                                (R3)

Set U'=e^(−it(H_eff+B')) and U₀=e^(−it(H_eff+B)). Factoring the scalar from the actual evolution, subtract as

    D U'D†−U₀=D(U'−U₀)D†+(D−I)U₀D†+U₀(D†−I).

Unitary norms and (R2)–(R3) yield

    ‖e^(−it(H+B))−e^(−ict)e^(−it(H_eff+B))‖
       ≤2d(1+|t|‖B‖)≤2λ(1+|t|‖B‖).              (R4)

The common scalar does not require commutation with B beyond being an identity. The comparator retains B itself, including its scalar or old-energy components. There is no assumed factorization e^(−itH_eff)e^(−itB), no assumed invariance of an R sector after adding B, and no omission of a large accumulated c t phase. This estimate is less sharp than the exact base bound at B=0 and at t=0, but is valid; no claim of exactness or optimality is made for (R4).

The operator bound may be replaced by its minimum with two. For arbitrary pure joint inputs it bounds the complete vector error with the displayed phase. For arbitrary mixed inputs and passive extensions, the trace norm of the difference of the two output states is bounded by twice that capped norm, further capped at two. This also gives the asserted unhalved complete channel upper bound. No ancilla output is discarded, projected or normalized conditionally.

## 3. Weak-background policy and physical scope

For B=λ²B₀ and |t|≤a/λ² with a≥0,

    |t|‖B‖≤a‖B₀‖,

so (R4) is at most 2λ(1+a‖B₀‖). Thus λ≤ε/[2(1+a‖B₀‖)] is sufficient for the stated vector tolerance, subject also to λ<1 and the complete physical cap. This is a uniform family only if a stated λ-independent bound on ‖B₀‖ is available. Local boundedness alone is not an extensive operator-norm bound. For fixed nonzero ‖B‖ and t of order λ⁻², this estimate need not tend to zero; its uncapped expression can grow as λ⁻¹. That fact is not a dynamical lower bound or an obstruction theorem.

The base Hamiltonian still consists of four positive real nearest-neighbor blocks, with old loads 3+2λ+2λ² and ancillary loads 2λ. An arbitrary selfadjoint B does not ensure H+B is positive or local. To retain the same hardware class, the additional physical blocks must themselves be supplied as positive real at-most-two-body blocks on allowed nearest-neighbor supports, if those are the claimed requirements. This is the meaning of retaining the original physical inventory class; merely proving (R4) for arbitrary complex or nonlocal B does not establish that class.

For B=λ²Σ_l b_l with such supplied positive blocks, each site receives the added load λ²Σ_(l incident v)‖b_l‖, and ‖B₀‖≤Σ_l‖b_l‖ is sufficient. These counts and norms must be included for any new sites too. Conjugated B' is only a proof operator; it is not installed, and no physical implementation of D is assumed. Small λ can satisfy both a fixed finite extra inventory's load budget and (R4), but arbitrary growing inventories require their explicit norm bounds.

This establishes one weak-background interface for one exact gadget. It does not justify adding gadgets that share the old pair, duplicating K, separately canceling counterterms, compiling the earlier spectral clock matrices, preparing an ancillary eigenstate, or obtaining common clock outputs from a real product seed. Such an assembly must supply its own combined algebra and target. Interval W operation, release, capture and permanent halt remain outside this addendum.

## 4. Actual verification and disposition

The new load-bearing identities (R1)–(R4), endpoint cost, domains, scalar and weak-timescale substitution were reconstructed analytically. The unchanged base proof was reused from the exact frozen source/check above. No scientific program, numerical matrix calculation, sweep, external search, delegation or model override was used. Source hashes and file sizes were checked deterministically; this report was read back completely. Only this ADDENDUM_REVIEW.md was written. The completed REVIEW.md, source files, Git, canonical/checkpoint files and editable prompts remain unchanged.
