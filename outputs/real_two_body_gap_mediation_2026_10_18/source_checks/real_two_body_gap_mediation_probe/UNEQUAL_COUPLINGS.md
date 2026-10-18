# Unequal real couplings with an exactly calibrated positive counterterm

**Status: proposed extension, pending distinct check.** Exact equality of the two weak couplings is unnecessary for the full-output mediated-interaction estimate. A nonlinear counterterm calibration remains supplied. This is not generic coefficient robustness or a clock assembly.

The frozen equal-coupling source is PROPOSAL.md SHA256 `d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258`. Its weak-background addendum is `eb61571fc02140def4058ddc71cf55e3b9329dde25452fb4fadc07b6bef4d651`. Neither file changes. ROOT proposed the unequal-coupling square identity and mistuning comparison; the derivation below is shared-design author work requiring distinct review.

## Actual four-block model

Retain the same four physical sites and nearest-neighbor geometry as the source. Let Z=Z1Z2, K=2I+Z, Q=X1X2Y_aY_b and R=ZQ. Choose0<u,v<1 and define

    a=sqrt[(1−u²)(1−v²)],  κ=uv,
    V=uY1Y_a+vY2Y_b,
    c=u+v+1−a.

Install exactly the positive real two-qubit blocks

    K, (1−a)(I−Z), u(I+Y1Y_a), v(I+Y2Y_b).         (U1)

Their full-support norms are3,2(1−a),2u,2v. Old-site loads are3+2(1−a)+2u and3+2(1−a)+2v; ancillary loads are2u and2v. A sufficient cap is3+2(1−a)+2max(u,v)≤Λ. Counts remain four qubits and four positive blocks, with K counted once. The counterterm coefficient is determined from the actual supplied u,v; treating independently unknown coefficients as though this identity were automatic would be incorrect.

Write H=(2+c)I+A, A=aZ+V. The signs inherited from Pauli algebra are {Z,V}=0, {Q,V}=0, [R,V]=0, and

    V²=(u²+v²)I−2uvR,
    A²=(1+κ²)I−2κR=(Z−κQ)².                       (U2)

The equality follows from a²+u²+v²=1+u²v². It includes the full sixteen-dimensional space, not just an ancillary excitation sector.

## Exact sectors and complete propagator error

On the R=r sector, r=±1, set

    Ω_r=1−rκ>0,  ν_r=|u−rv|.

Then Q=rZ, V²=ν_r²I and a²+ν_r²=Ω_r². For ν_r>0, X'_r=V/ν_r is a real symmetric involution anticommuting with Z. The actual and comparator non-scalar sector generators are

    A_r=aZ+ν_r X'_r,
    (Z−κQ)_r=Ω_r Z.                                (U3)

For ν_r=0 they agree exactly since a=Ω_r>0. Positivity of a and Ω_r checks the spectral sign that a squared-operator identity alone would not fix. Each nontrivial sector is an exact real rotation with cosβ_r=a/Ω_r and sinβ_r=ν_r/Ω_r.

The cosine parts of their propagators cancel. Consequently the exact full operator norm, for every real t, is

    ||exp(−itH)−exp(−ict)exp[−it(K−κQ)]||
      =max_(r=±1) d_r |sin(Ω_r t)|,
    d_r=sqrt(2−2a/Ω_r).                             (U4)

Both sectors are nonempty. Since Ω_-≥Ω_+ and a>0, d_-≥d_+. Thus the uniform error is at most d_-; the two sine factors need not reach their maxima simultaneously, and no such assertion is used. This is a full-output estimate for arbitrary old/ancillary states and correlations, tensoring with identity on arbitrary passive references. The unhalved channel distance is at most twice this operator bound, capped at2.

For u=v=λ, a=1−λ², κ=λ², d_+=0 and d_-=2λ/sqrt(1+λ²), recovering the frozen source exactly.

For0<u,v≤1/2, a≥3/4. The identity

    d_r²=2ν_r²/[Ω_r(Ω_r+a)]≤ν_r²/a²

gives the simple uniform sufficient bound

    d_-≤(u+v)/a≤4(u+v)/3.                          (U5)

This is not an optimal constant. At T=b/κ for fixed mediated angle b, [K,Q]=0 makes the comparator exp(−icT)exp(−iTK)exp(ibQ), with no time-growing truncation remainder. If one coupling tends to zero much faster, the mediated time grows as1/(uv); small error alone is not a bounded-runtime assertion.

## Counterterm mistuning with its actual scalar retained

Replace the counterterm in(U1) by (1−a+δ)(I−Z), where δ is real and1−a+δ≥0. The actual Hamiltonian is

    H_δ=(2+c+δ)I+A−δZ.

The appropriate comparator retains the known actual scalar:

    exp[−it(c+δ)]exp[−it(K−κQ)].                    (U6)

After removing that scalar, the only additional perturbation is−δZ of norm|δ|. Duhamel and(U4) therefore imply

    ||exp(−itH_δ)−(U6)||
       ≤max_r d_r|sin(Ω_rt)|+|δ||t|.               (U7)

No sector-preserving simplification or new exact square identity for δ≠0 is claimed. If comparison instead insists on nominal scalar c, the extra phase mismatch must also be paid; a safe bound adds another|δ||t|. Unknown δ does not authorize silently fitting the output phase to each input.

For example, for a prescribed horizon T_max>0 and desired complete vector tolerance ε, the conditions u,v≤1/2, u+v≤3ε/8 and |δ|≤ε/(2T_max), together with positivity and the actual cap, suffice for error≤ε over |t|≤T_max. At T_max=b/(uv) this requires |δ|≤εuv/(2b). This is a supplied finite-time accuracy condition, not a manufacturing or necessary precision claim. With mistuning, replace2(1−a) in the old loads by2(1−a+δ), and verify the cap rather than reusing nominal slack.

## Scope and unresolved assembly

The full effective clock operator remains Y_aY_b, including pair creation and annihilation. A real product ancillary seed generally gives old/clock entanglement, not the literal fixed W with a common clock output. No preparation stage, two-sample clock, dwell, capture, reset or permanent halt is supplied by this extension. Simultaneously composing gadgets or adding substantial backgrounds needs its own control; equality of the isolated squares does not establish such a result.

The given K, positive matrix inventory, exact functional counterterm relation and initial-state interpretation remain explicit suppliers. No native coefficient mechanism is inferred. All computations here were analytical Pauli algebra, exact sector exponentials and Duhamel. No scientific executable, Git, source overwrite, canonical/checkpoint/axiom/prompt/model change, publication or delegation occurred. Only this separate extension was written; prior sources remain frozen.
