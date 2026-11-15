# Frozen affected review, revision 1

VERDICT: HOLD

Scope: reconstruction-consumer corrections in OSLEAF55 and ASSEMBLY55, including their directly consumed growth alternatives. This is a source verdict, not a whole-PR, audit or whole-theory verdict. The original full existence AND physical continuum mass-gap target remains OPEN. Recorded before reading the author packaging or old review reports.

Bound corrected OSLEAF55 SHA256: 4e778a30fdc9dd7734499c52a141bef753e10c9c77b298eea76a6858a54a96e8.
Bound corrected ASSEMBLY55 SHA256: c15524d7a1c3c04ce9c32567f6f61ec5113ebe24be9eba8de87f97e3109d326d.
Original pushed HEAD: 3bba91875672becadc0ab120204905d9f1f405a8; baseline 814364fcc7dbcf0ff4146f6766e98890124ac905 has the same original consumer bytes. Full v1 corrected source snapshots and the independent diff are retained beside this record.

## F-SP-SINGLETON — inherited direct-dependency inference remains false as stated

Location: OSLEAF55.md lines 919–926, (SP_lambda), immediately upstream of the changed BRIDGE(v) reconstruction consumer and the alternative smeared route mentioned in GROW, ASSEMBLY N9, ML9 and item 18.

Exact source quote:

> **(SP_λ) — the separated-product input with its separation quantified (the form the RG must deliver).** There are A, b, p, r ≥ 0
> and c_SP ≥ 1 such that for all a ∈ (0, 1], R ≥ 32, n ≥ 2, λ ∈ [c_SPa, 1] and all f_1, …, f_n ∈ C_c^∞(R^4; C), each supported in
> a cube of side 2 inside B_{R/4}, pairwise at distance ≥ λ:
>   |S^{a,R}_n(f_1 ⊗ ⋯ ⊗ f_n)| ≤ A^n(n!)^b λ^{−pn} Π_i ‖f_i‖_{λ,r},  ‖f‖_{λ,r} := max_{|γ|≤r} λ^{|γ|}‖∂^γf‖_∞,
> and the same with λ = 1 for separations ≥ 1. Equivalent and natural RG forms: (a) the same bound for conditional CUMULANTS
> (moments then follow by the partition sum, b → b + 1, since every sub-block of a separated family is separated); (b) the
> coarse-image form sup_V|E_{a,R}[Π_iÕ_a(f_i) | V]| ≤ (same right side) for every coarse field V — the shape of SEAM55's

The displayed quantifier starts at n=2. The conditional first cumulant is a conditional mean, which does not vanish merely because the field is centered under the unconditional law. The partition into n singleton blocks contributes their product. A bound on higher conditional cumulants alone does not control it. Also a uniform conditional-moment bound is sufficient for an unconditional bound by averaging, but is not equivalent to it; unconditional bounds can average rare large conditional values.

Exact analytic counterexample to the claimed combinatorial inference: let V take values +/-1 with probability 1/2, and on each finite lattice set e_a(x)=a^(-4)(1+V), so the centered field is X_a(x)=a^(-4)V. The same deterministic crude envelope 0<=e_a<=2a^(-4)<=24a^(-4) holds. Condition on V. For O_a(f)=a^4 sum_x f(x)X_a(x), every conditional joint cumulant of order at least 2 is zero, hence satisfies any of the claimed higher-cumulant bounds uniformly with fixed A,b,p,r. The first conditional cumulant is a^(-4)V c_a(f), where c_a(f)=a^4 sum_x f(x).

Choose two fixed nonnegative compact smooth tests of positive integral, with separated supports in unit cubes and fixed lambda>0, at a fixed sufficiently large admissible R. Along a->0, c_a(f_i)->integral f_i>0, whereas

    E[O_a(f_1)O_a(f_2)] = a^(-8)c_a(f_1)c_a(f_2) -> infinity.

The right side of SP_lambda at n=2 and fixed lambda is a cutoff-independent constant. Thus it fails. Unconditional centering holds exactly. No numerical calculation is involved. This is a counterexample to the algebraic implication from the stated n>=2 conditional-cumulant premise; it is not a counterexample to actual Wilson Yang–Mills, to SP_lambda stated as unconditional moments, or to reconstruction, and it is not a no-go claim.

The GROW total-cumulance branch now correctly requires singleton-inclusive G-outer. The nearby smeared alternative must be just as explicit, with an actually sufficient statement and a proof of its factorial and separation costs. One possible correction is a genuinely uniform-in-V conditional cumulant bound for EVERY nonempty block, INCLUDING order 1, with one consistent separation convention and common constants. Conditional moments then follow by their partition identity, and averaging can be justified. Another route would need quantitative all-order outer-product bounds. Neither route follows from higher conditional cumulants alone. Merely renaming the input or repeating that actual estimates are OPEN does not repair the false implication.

## Other affected conclusions at this revision

The independent producer reconstruction is preserved separately in initial_findings.md. The full current consumer sources have now been read, as have their actual REC_LIB/REC_CONT producers. REC(e)'s E0′ requirement, the insertion-count translation estimate, the explicit finite Cartesian tensor dictionary and sum norm, and the corrected pointwise GROW q_X order agree with that derivation. ASSEMBLY N9/ML2/ML9/item18 use the right implication direction and preserve the missing actual hierarchy/physical estimates. The no-E0′ alternative and unspecified O(4) representation route are explicitly unproved. No new blocker has been identified in these particular corrections.

The exact 2591-byte geometric RP block, including the statement, paired-half proof, extent-two counterexample, and reflection identity, is present byte-for-byte with SHA256 086bef4ca78481cf27a81c4f70b47254d65e47eb3a8ea8d41e563ea71eea545c. Producer bytes REC_LIB, REC_CONT and HRP match both original HEAD and baseline. Remaining history/read-manifest verification continues; no certification is inferred from those hashes.

The HOLD is narrow: the direct SP_lambda alternative remains unsound as written. It does not retract the conditional E0′ reconstruction or the corrected pointwise GROW route. A same-session affected confirmation is required after a frozen minimal correction. No source file was edited by this reviewer.
