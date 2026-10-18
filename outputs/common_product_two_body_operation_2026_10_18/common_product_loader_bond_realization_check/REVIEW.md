# Distinct check of the isolated positive square component

Disposition: SUPPORT for the isolated eight-qubit component, supplied cat+ initialization, stated scalar phase, full-vector approximation, incident cap and finite simulation horizon. No required mathematical correction found. This does not realize the full conditional entrance bond, its simultaneous six terms, their actual geometry or the coupled router runtime. It does not remove the complete-loader premise or establish native block/state supply.

Reviewed complete source: `common_product_loader_bond_realization/PROPOSAL.md`, SHA256 `7e6769927d3138b2812e0b4a0db62df1ef4d1d7096b10acfa2269a5ca8a98d39`. All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. I fully read the changed argument and the complete conditional entrance source c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e and its distinct review7a98f648e21cf63b70d481b2cbaba8fac86376763cec0f50678f0ed49e9bd68f. Earlier full reads of preparation9979/162edd and the router/packet/positive-block ancestry retain their unchanged scopes; no fresh blanket audit of that ancestry is claimed.

ROOT exposed the proposed gadget and requested a distinct check. I authored/reviewed several finite/preparation components but did not author this square gadget or its Feshbach argument. This is source-exposed same-model checking, not blind replication. In addition to analytical reconstruction I performed the expressly authorized bounded exact characteristic-polynomial calculation described below, using a different method from fourth-order path enumeration. That evidence corroborates the low-energy coefficients; it is not evidence for the missing background/geometry/initializer interfaces.

## 1. Target algebra, positivity, geometry and sector gap

The full-space identities hopping=(XiXj+YiYj)/2 and SWAP=(I+XQXP+YQYP+ZQZP)/2 give precisely the source's two-body/occupation terms and six four-Pauli terms, each with coefficient -j0/4. Vacuum and double occupation are retained. A single -g Omega is therefore one actual summand, not the entire conditional bond.

Every penalty Delta(I-ZZ)/2 has eigenvalues0,Delta; every nu(I+O_r X_b_r) has eigenvalues0,2nu since O_r and X_b_r are Hermitian unitaries on different qubits. These are full-support statements. The square and vertical edges at the displayed coordinates are nearest-neighbor and mutually distinct. Ancillary incident load is exactly2Delta+2nu and each isolated data terminal load is2nu. There are four new ancillas, eight total qubits and eight positive blocks. Geometric adjacency of the upper data square does not install additional couplings.

X_all commutes with H0 and V. The zero-energy space of H0 on all four ancillas is span{|0000>,|1111>}; its plus-sector intersection is exactly cat+. All other Ising configurations have at least two domain walls, so within the plus sector the complementary energy is at least2Delta. This uniqueness is ancillary: arbitrary data and references retain their degeneracy. Cat- in the other reducing sector is real and unpenalized by H0. The restriction cannot be inferred from low energy alone or from a product |0000> initialization.

## 2. Fourth order reconstructed and checked by exact polynomial

Within a joint data-Pauli eigenvector, the ancillary perturbation is nu sum o_r X_r. A single flip has energy2Delta, giving E2=-4nu^2/(2Delta)=-2nu^2/Delta and PV R^2 VP=nu^2/Delta^2. In the Feshbach inverse, inserting E2 into the energy-dependent denominator gives the POSITIVE product correction in equation(5). Its size is2nu^4/Delta^3; omitting it would give an incorrect scalar.

For four distinct flips there are24 orders. After two flips,16 have an adjacent pair with energy2Delta and8 have opposite sites with energy4Delta. The first and third intermediate energies are2Delta. Their weighted sum is(5/2)nu^4/Delta^3, multiplying Omega in the cat+ sector. For two distinct flips each repeated twice, the two orders beginning with a repeated site return to P at step two and are excluded. The four allowed orders per unordered pair give16 adjacent and8 opposite contributions, with the same denominator sum and identity data factor. Thus E4=-(1/2)nu^4/Delta^3 I-(5/2)nu^4/Delta^3 Omega, as claimed.

An independent exact-matrix route avoids this path count. Gauge each negative o_r by Z_r. It converts V to a uniform transverse field and sends the ancillary X_all sector from plus to omega=product o_r. In units Delta=1, x=nu/Delta, form the exact8-by-8 matrix in the complement basis (|n>+omega|15-n>)/sqrt(2), 0<=n<8. Its diagonal is the exact domain-wall count; a flipped bit contributes x, with an extra omega when its representative is the complement. Symbolic determinants yield:

    omega=+1:
    -(E-2)^4[-E^4+8E^3+16E^2 x^2-20E^2-64E x^2+16E+32x^2],

    omega=-1:
    (-E+2x+2)^2(E+2x-2)^2
                  (-E^2+2E+4x^2)(-E^2+6E+4x^2-8).

At x=E=0 both polynomials have E derivative -256, so the low root is simple. Implicit exact series solution gives

    omega=+1: E=-2x^2-3x^4+3x^6+O(x^8),
    omega=-1: E=-2x^2+2x^4-4x^6+O(x^8).

The fourth coefficients agree with -1/2-(5/2)omega. This checks both scalar and Omega signs and shows that the uncomputed higher terms cannot simply be set to zero. No floating-point eigensolver, numerical fitting or repeated parameter sweep was used.

Reproducible files retained in this review folder:

- `exact_square.py`, SHA256109b3f33919446f0c7cb7fa5cbcec5209df4f381bdbd145f5ab3661fb46f9ee3.
- `exact_square.txt`, SHA2564023c5f3fbd8eeabfe7feaa2d3cea77f694da7e1cece3ea5897dbf28e8247758.

Run `python3 exact_square.py` with SymPy to reproduce the exact symbolic result. The script constructs the reduced matrices and solves determinant coefficients; it does not import the author's Feshbach coefficients except as explicit assertions to be tested. The numerical contour and dynamical bounds below remain analytical obligations, not outputs of that script.

## 3. Complex Riesz construction and analytic remainder

On |z|=Delta/2 the unperturbed resolvent is bounded by2/Delta: zero is inside and all complementary energies are at least2Delta. With v=||V||<=4nu and |lambda|<=Delta/(8v), the Neumann ratio is at most1/4 and the perturbed resolvent is at most8/(3Delta). Integrating the resolvent identity over the contour gives ||Pi-P||<=1/3. This holds for complex lambda; Pi need not be orthogonal there, but it is an analytic idempotent and no spectrum crosses the contour.

On range P, P Pi P is within1/3 of identity. Its inverse square root is defined by the analytic binomial series, and ||C||^2<=3/2 follows from absolute coefficients. The definition E=C P H Pi P C uses no complex conjugation of lambda. For real lambda, Pi is orthogonal, W=Pi P C is an isometry, and Pi H Pi=H Pi gives E=W^*H W. Thus this analytic continuation is the correct normalized effective operator on the real axis.

The contour formula for H Pi gives norm at most (Delta/2)^2*8/(3Delta)=2Delta/3. Multiplying by C on both sides yields ||E(lambda)||<=Delta. The parity unitary Z1Z2Z3Z4 commutes with H0, anticommutes with V, preserves the plus sector and acts identically on P. Consequently P Pi(-lambda)P=P Pi(lambda)P and the same identity holds for P H Pi P. Hence E is even as an analytic operator, not merely a collection of symmetric eigenvalue sets.

The permitted analytic radius is at least Delta/(32nu)=1/(32alpha). Since alpha<=1/64, it is at least2. Cauchy coefficient bounds and summation of the even powers starting at six therefore give exactly

    ||E(1)-E_lead||<=Delta(32alpha)^6/[1-(32alpha)^2].

The data Pauli operators commute on their distinct supports, so their simultaneous columns reduce to individual isolated eigenvalues; this justifies identifying the second/fourth Taylor coefficients of this normalized E with the earlier column calculation. References tensor by identity and do not increase any bound.

## 4. Literal injection, phases and finite horizon

At lambda=1 the same resolvent-identity estimate gives deltaPi<=8alpha/(1-8alpha)<=1/7 and deltaPi<10alpha. For the positive real inverse square root, ||C||<1.081 and ||C-I||<=.64deltaPi follow from scalar spectral calculus on [1-deltaPi,1+deltaPi]. Thus ||W-J||<2deltaPi<20alpha. The source's notation identifies the data space with range P in this calculation; J is its actual literal cat+ injection.

Comparing literal J to W on the input, intertwining the exact low evolution through W, applying the real self-adjoint Duhamel bound to E(1)-E_lead, and comparing W to J on the output costs two copies of20alpha plus |t|R6. Restoring the identity shift4nu gives exactly exp[-it(4nu+s)]J exp(+itg Omega), with s negative as specified. The full actual ancilla output is retained in the discrepancy. This is not merely an eigenvalue estimate, projection onto a dressed low sector or renormalized successful outcome. It applies for every real t, although its usefulness is limited by the growing remainder term.

For Delta=Lambda/4 and the specified minimum choice of alpha, (32alpha)^2<=1/4 and

    R6/g <= (8/15)32^6 alpha^2<=epsilon/2,
    40alpha<=epsilon/2.

This proves the stated error <=epsilon for |t|<=1/g. The incident cap inequalities follow directly from alpha<=1/64. Eventually epsilon/80 is the smallest entry of the minimum, so the explicit isolated family has g=Theta(Lambda epsilon^4) and1/g=Theta(Lambda^-1 epsilon^-4). This asymptotic statement is not a claim that the same formula controls every finite epsilon by that branch of the minimum. Matching g=j0/4 requires adjusting or verifying j0; an independently fixed bond strength is not simulated to arbitrarily small error at the same cap by this prescription.

## 5. Scope and remaining physical interfaces

The source correctly distinguishes positive arbitrary Pauli-product couplers from the previously displayed exchange/diagonal-control/record primitives. Choosing real O=(X,X,Z,Z) gives real symmetric blocks, but positivity and reality do not derive their supply. Terms containing a single data Y yield genuinely complex Hermitian blocks in this construction; no real replacement is established.

The supplied cat+ is an entangled resource in a chosen reducing sector. An initialization error must be controlled jointly with every retained reference; a correct marginal alone does not ensure the full-output premise. The unused cat- ground sector prevents reading the gap as a unique initializer.

The explicit terminal square is not the actual entrance support geometry in c97b. Six copies per entrance share data terminals, and the physical P already has four mediator neighbors. Their naïve juxtaposition does not fit cubic degree or preserve this isolated spectral problem. Data terms in the router background generally fail to commute with the chosen O_r, so the scalar-column proof, low contour and effective terms require a new background-stable argument. The review supplies no claim that a globally small background norm is necessary for all possible constructions, only that the present proof does not handle that background.

Accordingly the accepted component neither realizes the complete SWAP-conditioned hopping bond nor transfers c97b's exact runtime gauge theorem through a gadget approximation. It supplies no endpoint injection, full autonomous loader, guaranteed old-P/environment release, native coefficient/state supplier, capture/reset or permanent halt. These restrictions are material, not caveats to be dropped when combining components.

Only this review and its expressly authorized exact-matrix script/output were created, all under N. No source, W, Git, checkpoint, axiom, editable prompt, model setting or publication was changed, and no delegation occurred. Support is for the isolated component and stated full-vector interface only.
