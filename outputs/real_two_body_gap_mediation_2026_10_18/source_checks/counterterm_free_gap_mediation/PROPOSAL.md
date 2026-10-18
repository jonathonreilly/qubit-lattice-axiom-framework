# Product-mediator cancellation without an old-only counterterm

Status: new conditional analytical construction, pending distinct check. Five supplied positive real nearest-neighbor blocks, with a mediator initially in |0>, approximate the complete evolution of K−lambda²Q on the old pair and two clock qubits. The bound includes the final mediator and arbitrary passive references. No old-only counterterm is installed. Constants below are deliberately conservative; no clock common-output construction or native realization follows.

ROOT proposed the auxiliary cancellation and subsequently suggested a two-conjugation remainder proof. The signs and estimates below were reconstructed independently as author work, with that design exposure declared. This is not an independent check.

## Actual device and target

Use Z=Z1Z2, K=2I+Z, Q=X1X2Y_aY_b and 0<lambda<=1/1000. Put old1=(0,0,0), old2=(1,0,0), a=(0,1,0), b=(1,1,0), and mediator m=(0,0,1). Set g=sqrt(6)lambda. Install precisely

    K,
    lambda(I+Y1Y_a),
    lambda(I+Y2Y_b),
    4 n_m,
    g(I+X1X_m).                                      (1)

Each is real positive on its full support. Norms are respectively 3,2lambda,2lambda,4,2g. There are five qubits and five positive blocks. The incident loads are

    old1: 3+2lambda+2g;  old2: 3+2lambda;
    a,b: 2lambda;       m: 4+2g.

All listed pairs are nearest neighbors. For any supplied cap Lambda>4, reducing lambda additionally until these loads are <=Lambda suffices. The fixed gap 4 is measured relative to the coefficient 1 of Z in the literal K; time is not silently rescaled. K occurs once and no other old-only block is supplied. The positive scalar shifts of both exchanges are retained.

Let J0 map xi on old+clock+passive space to xi tensor |0>_m. The conclusion proved below, for every real t, is

    || e^{-itH} J0
       − exp[-it(2lambda+g−2lambda²)]
           J0 e^{-it(K−lambda²Q)} ||
       <= min{2, 62lambda+10^6 |t|lambda³}.           (2)

Tensor identities and the position of the mediator factor are implicit only in this displayed notation. All clock states and correlations with the old system are permitted; only the mediator is selected initially. No mediator projection is performed at the end. At |t|<=a/lambda² the bound is (62+10^6 a)lambda. Thus choosing lambda<=epsilon/(62+10^6 a), together with the fixed smallness and cap conditions, gives vector error epsilon on that entire interval. The unhalved complete channel distance is <=min(2,2epsilon). This is a sufficient slow family, not an optimized estimate.

## Spectral decomposition and first conjugation

Strip only the exact scalar c=2lambda+g. Write

    H−cI=H0+lambda V,
    H0=K+4n_m,
    V=Y1Y_a+Y2Y_b+sqrt(6)X1X_m.

The four H0 eigenvalues are 1,3,5,7, each with a degenerate old/clock fiber. Denote their orthogonal projectors P_j and energies E_j. One has ||H0||=7 and ||V||<5. Every summand of V changes old Z; the last also flips m. Hence P_j V P_j=0 for all j, including the degeneracies.

Define

    S = sum_{j!=k} P_j V P_k/(E_j−E_k).

Then S is anti-Hermitian, real antisymmetric, and [S,H0]=−V. There are twelve ordered off-diagonal blocks, each denominator has magnitude >=2, so ||S||<=6||V||<30. This deliberately crude bound avoids using a sharper block-matrix norm without proof. Conjugation gives

    e^{lambda S}(H0+lambda V)e^{-lambda S}
       = H0+lambda² W2+R3,
    W2=[S,V]/2,       ||W2||<=150.                   (3)

The linear term cancels. The sign of W2 is fixed by this convention. For a bounded generator S, ||ad_S^k A||<= (2||S||)^k||A||. Expanding H0 from order three and lambda V from order two, using sum_{k>=r} x^k/k!<=x^r e^x/r!, gives

    ||R3|| <= e^{60lambda}
       [7(60lambda)^3/6 +5lambda(60lambda)^2/2]
       <600000 lambda³                              (4)

for lambda<=1/1000. The number in brackets is 261000lambda³ and e^{0.06}<2, so the displayed ceiling is safe. No unbounded operator or infinite-volume expansion is involved.

## Removing second-order off-diagonal terms

Let D2=sum_j P_j W2 P_j. This pinching is norm-contracting: for a vector split into the four orthogonal blocks, each diagonal block has norm <=||W2||, so ||D2||<=150. Define

    S2=sum_{j!=k} P_j W2 P_k/(E_j−E_k).

Then ||S2||<=900, S2 is anti-Hermitian, and [S2,H0]=−(W2−D2). A second conjugation yields

    e^{lambda² S2} e^{lambda S}(H−cI)
          e^{-lambda S} e^{-lambda² S2}
       = H0+lambda² D2+R.                            (5)

Conjugation preserves the norm of R3 exactly. The additional remainder, bounding the H0 series from order two and the lambda² W2 series from order one, is at most

    e^{1800lambda²}
       [7(1800lambda²)^2/2
                   +150lambda²(1800lambda²)]
       <23220000lambda^4.

At lambda<=1/1000 this is <=23220lambda³. Combining with (4) proves ||R||<=10^6lambda³. In particular the neglected error is explicitly paid on times lambda^{-2}; it is not presumed to vanish because the formal second-order generator looks correct.

For F=e^{lambda² S2}e^{lambda S}, anti-Hermiticity gives

    ||F−I||<=lambda||S||+lambda²||S2||
              <=30lambda+900lambda².

Duhamel applied to (5), with the two outside F factors, therefore bounds the complete propagator error against exp[-it(cI+H0+lambda²D2)] by

    2(30lambda+900lambda²)+|t|10^6lambda³
       <=62lambda+|t|10^6lambda³.                   (6)

This comparison is first proved on the entire five-qubit space, with the entire D2 retained. It can subsequently be restricted to J0 without discarding any actual high-band leakage.

## Selected-band second-order generator and cancellation

For a particular energy block j, direct multiplication in (3) gives

    P_j W2 P_j = sum_{k!=j}
                    P_j V P_k V P_j/(E_j−E_k).      (7)

Let z=+1 or −1 be old Z and select m=0. The two YY terms together, denoted VY, have intermediate energy denominator 2z and

    VY²=2(I−ZQ).

Consequently their contribution is z−Q on that selected block. The XX-mediator term has squared matrix element 6 and denominator 2z−4. Its contribution is

    6/(2z−4)=−2−z.

Mixed YY/XX terms flip m exactly once and cannot return to the same H0 eigenspace: m=0 has energies 1,3 and m=1 has energies 5,7. Their diagonal contribution is zero. Thus, on the whole selected m=0 space including both old parities,

    D2 = −2I−Q.                                     (8)

Q commutes with Z, so this is genuinely block diagonal in H0. Equations (6)-(8) prove (2), with the scalar −2lambda² combined with the positive shifts c. The self-energy +lambda²Z from the YY interactions is canceled by −lambda²Z from virtual mediator excitation. This cancellation is an effective statement with the stated remainder, not exact equality of the actual Hamiltonian to its comparator.

The proposed general denominator calculation is also consistent: with gap Delta>2, choosing g²=lambda²(Delta²−4)/2 gives mediator shift −lambda²(Delta/2+z), canceling z−Q to −Delta/2−Q. However, this note proves explicit uniform constants and resource prescriptions only for Delta=4. General Delta requires its own spectral separation bounds, particularly near cross-band degeneracies.

## What this removes and what it leaves supplied

No old-only counterterm is present in (1); the literal K remains installed once. The new costs are a fifth qubit in a supplied real |0> state, a supplied positive gap 4n_m, and the calibrated positive coupling g=sqrt(6)lambda. All are ordinary real one- or two-qubit terms, but their native origin and calibration are not derived. A mediator in an arbitrary unknown state is not covered by the selected-input conclusion (2). Its output vacancy is approximate and paid in the complete norm, not assumed.

The effective interaction remains −lambda² X1X2Y_aY_b. A real clock product input does not automatically produce a common clock output implementing literal W. No multiple-gadget sum, additional clock background, receiving-device attachment, selected-time dwell, capture, reset or permanent halt theorem is imported. Adding another background to this new construction requires extending (3)-(8) with that actual background; the prior exact-rotation addendum cannot simply be reused because the actual mediator Hamiltonian is different.

Source context: real_two_body_gap_mediation_probe/PROPOSAL.md SHA d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258 was read fully and supplies notation for the previous counterterm construction only. Its algebra is rederived here where used. The new proof is the explicit five-qubit spectral elimination and selected-band cancellation, not a quotation of an external perturbative theorem. No scientific executable, literature search, Git, canonical/checkpoint/editable-prompt/model changes, publication, or delegation was used. Only this source was written. Distinct checking remains required.
