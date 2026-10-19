> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Exact gap-mediated four-body rotation from real positive two-body blocks

**Status: new analytical candidate, pending distinct check.** Four real positive nearest-neighbor two-qubit blocks simulate the complete evolution of K−λ²X1X2Y_aY_b, up to one known scalar and a uniformly O(λ) full-space operator error for ALL times. A positive old-pair counterterm is explicitly supplied; it cancels the diagonal self-energy exactly in this special algebra. This is not yet a realization of the earlier three-clock matrices or a product-seed implementation of the literal W with common ancillary output.

ROOT suggested using the old gap and subsequently the exact square identity. I reconstructed the invariant sectors and obtain an exact propagator-error expression below. Shared design exposure is explicit; this is not independent validation. The original K is retained once. No microscopic-native selection of any displayed block or coefficient is asserted.

## Literal gap, actual blocks and geometry

Let Z=Z1Z2, K=2I+Z, and0<λ<1. Put old sites1=(0,0,0),2=(1,0,0), ancillary clock sites a=(0,1,0),b=(1,1,0). Install exactly

    h0=K,
    hc=λ²(I−Z1Z2),
    h1=λ(I+Y1Y_a),
    h2=λ(I+Y2Y_b).                                  (1)

Each matrix is real on its two-qubit support: Y⊗Y is real. They are positive, with full-support norms3,2λ²,2λ,2λ respectively. No interaction is installed on a–b or other unlisted pairs. All four listed blocks are nearest-neighbor; hc and K share the old edge. There are four qubits and four positive blocks. Old-site incident loads are3+2λ+2λ², and each ancillary load is2λ. Thus anyΛ>3 permits a sufficiently small λ with3+2λ+2λ²≤Λ.

The coefficients use the fixed unit coefficient of ZZ in K. λ is measured relative to that old energy scale; λ² is not a dimensionally arbitrary square after changing units. More generally a gap coefficient D would replace this counterterm scale by coupling²/D. Only the stated literal normalization is proved here.

Define

    V=λ(Y1Y_a+Y2Y_b),
    Q=X1X2Y_aY_b,
    R=ZQ,
    A=(1−λ²)Z+V,
    c=2λ+λ².

The actual Hamiltonian is H=h0+hc+h1+h2=(2+c)I+A. The comparator is

    H_eff=K−λ²Q,
    U_cmp(t)=exp(−ict)exp(−itH_eff).                 (2)

Both the scalar2I in K and c are retained exactly. The counterterm is a new declared positive supplier, not a change to K or an assumed native cancellation.

## Algebra and sign

The two summands of V commute. Each anticommutes with Z. Q commutes with Z but ANTICOMMUTES with each summand of V. Thus R=ZQ commutes with Z,V and A. These signs matter: Q itself is not a conserved label of the actual Hamiltonian.

Using Z1Y1=−iX1 and Z2Y2=−iX2,

    Z(Y1Y2)=−X1X2,
    V²=2λ²[I+Y1Y2Y_aY_b]=2λ²(I−R).                 (3)

It follows exactly that

    A²=(1−λ²)²I+V²
       =(1+λ⁴)I−2λ²R
       =(Z−λ²Q)².                                  (4)

Equation(4) is not alone an equivalence proof; the spectral signs and rotation must still be checked. We do so in the two conserved R sectors.

Let P_r=(I+rR)/2. On r=+1, V²=0; since V is selfadjoint, V=0 on that sector. Also Q=Z, so

    A=(1−λ²)Z=Z−λ²Q.

On r=−1, Q=−Z and V²=4λ²I. Define X'=V/(2λ) on this sector. It is a selfadjoint involution anticommuting with Z. There

    A=(1−λ²)Z+2λX',
    Z−λ²Q=(1+λ²)Z.                                 (5)

The rotation angle β=2arctanλ satisfies cosβ=(1−λ²)/(1+λ²), sinβ=2λ/(1+λ²). Thus (5) is an exact rotation of a Pauli axis, not a Taylor expansion or a perturbative spectral guess. One may take the real orthogonal rotation exp[−(β/2)ZX'] in that sector and identity in r=+1; ZX' is real antisymmetric. Its conjugation sends Z to cosβ Z+sinβ X'. This supplies an exact dressed equivalence on the entire sixteen-dimensional Hilbert space.

## Exact complete propagator error: no secular remainder

In r=+1 the two propagators agree. In r=−1, writing Ω=1+λ², the cosine terms agree and subtraction gives

    exp(−itA)−exp[−itΩZ]
     =−i sin(Ωt){[(1−λ²)/Ω−1]Z+(2λ/Ω)X'}.

The anticommuting-involution norm is therefore exactly

    ||exp(−itH)−U_cmp(t)||
      = [2λ/sqrt(1+λ²)] |sin[(1+λ²)t]|
      ≤2λ/sqrt(1+λ²)<2λ,                            (6)

for every real t. Both R sectors are nonempty, so the displayed full-space norm is indeed attained as an operator norm; no state restriction is used. Tensoring any passive identity preserves it. For arbitrary mixed old/ancillary/passive inputs, the unhalved channel distance is at most twice (6), capped at2.

In particular no O(λ⁴t) remainder has been dropped at t~λ^−2. For a target mediated angle a at T=a/λ², [K,Q]=0 gives

    U_cmp(T)=exp(−icT)exp(−iTK)exp(iaQ).             (7)

All outputs are present; any initial ancillary state or old/ancillary correlation is allowed under the full-space comparison. Choosing λ≤ε/2 suffices for vector error≤ε for every t, subject to the cap and λ<1. The phase cT can be large and is known explicitly; it is not omitted because the interaction is weak. The time scale is real relative to the fixed old gap.

## What happens without the supplied counterterm

If hc is omitted, the non-scalar Hamiltonian is Z+V. In each R sector its exact rotated eigenvalue is Z sqrt[I+2λ²(I−R)]. Expanding only to identify the second-order term gives

    Z+λ²Z−λ²Q+O(λ⁴).

The +λ²Z self-energy changes literal old aging by O(1) at times O(λ^−2). It cannot be called a harmless common phase, since Z has both signs on arbitrary old inputs. Adding hc introduces −λ²Z together with the paid scalarλ². Equation(4) then proves exact cancellation to all orders in this special spectrum. This explanation does not license generic counterterm cancellation in another gadget.

## Clock-pair terms and the product-state limitation

The effective operator is the whole Y_aY_b, not only its excitation-conserving part:

    Y_aY_b=−σ_a^+σ_b^+−σ_a^-σ_b^-
            +σ_a^+σ_b^-+σ_a^-σ_b^+.

Pair creation/annihilation is essential. For the real product clock seed|00>_ab, since Y_aY_b|00>=−|11>, (7) gives, after removing the known scalar and old aging,

    exp(iaQ)(ξ⊗|00>)
      =cos a ξ⊗|00>−i sin a (X1X2ξ)⊗|11>.          (8)

For a=θ, both coefficients are nonzero. For an old vector with ξ orthogonal to X1X2ξ, this has two nonzero Schmidt coefficients3/5 and4/5. It is not the fixed W applied to ξ with an input-independent clock output. Thus the proved full-space simulation of a useful conditioned interaction is not itself the desired common-output gate.

An ancillary eigenstate of Y_aY_b with eigenvalue+1 would reduce exp(iθQ) to exp(iθX1X2), and the literal W would then be obtained with an extra known scalar exp(−iθ) in the comparator. A real such state is (|00>−|11>)/sqrt2, but it is entangled. Product eigenstates require Y-eigenstate coherences and are not real computational-basis product inputs. Neither supplier is silently installed here. Equation(8) is the explicit product-input output that must be retained.

The Hamiltonian is real and positive two-body, but does not conserve an ancillary head-number sector: the actual Y couplings and effective pair terms permit its change. A later use cannot import one-head support/counting lemmas without checking their hypotheses.

## Concrete next interface and unresolved obligations

This exact gadget is a positive building block for the previous sampled-clock problem: it realizes one XX-conditioned real pair operation with ordinary two-body blocks and no prepared auxiliary state requirement for the simulation estimate. It does NOT realize arbitrary parity-dependent clock matrices A_±. A sum of such gadgets sharing old qubits need not preserve (3)–(5); cross terms and simultaneous background interactions must be derived, not added by analogy. The old K and the tuned counterterm must not be duplicated across an assembly.

The next bounded calculation should test whether a finite clock network built from this exact interaction and permitted ordinary clock terms can enact the two sampled common-output maps from a real product clock. Its decisive obligations are the actual noncommuting combined spectrum, common clock outputs, full phase, background stability, positivity and incident cap. Alternatively a real product-to-eigenstate preparation stage would need an autonomous attachment/release proof. No such assembly or preparation is claimed here.

The earlier enlarged-block source is `selected_seed_real_clock_probe/PROPOSAL.md`, SHA `668725c1c8d02a777b2751fb392ba78ab108824ed6a3d3cb670695b5a2f5056b`; it motivates the interface but no logarithm/locality result from it is needed for(3)–(8). Literal K/W identities remain those of direct source `c0cc65e615bb6bdb7466c01c68ce53d6647c75e73a322bd88fff97580428f7d6`. All old sources remain frozen. No scientific executable, external search, Git, publication, canonical/checkpoint/axiom/prompt/model change or new agent was used. Only this proposal was written. Exact finite algebra is author evidence, pending distinct review; it is not native physical realization or mission closure.
