# Complete fixed-order compact-sector pole: root derivation

Status: bounded-support. Fix an integer m>=4. Use the actual order-m zero-block local normal form of the supplied XX/YY/ZZ one-qubit Hamiltonian, the all-up bulk reference, even longitudinal plane parities, all three center-of-mass momenta zero, and the physical square scalar with even coordinate reflections. Subtract the vacuum coefficientwise. All constants and small-lambda thresholds may depend on m. This theorem concerns the complete compact E8 coefficient operator; it is not a resonance theorem for the untruncated microscopic Hamiltonian.

## 1. Actual coefficient structure and gauge

Four longitudinal walls and even parity in every longitudinal plane require two flipped columns with a common finite interval. Thus the compact sector is indexed by interval length ell and unordered transverse separation. At fixed order, connected coefficient clusters have bounded diameter and cardinality. Away from a finite region in these relative coordinates, short-length hosts have finite-range translation-invariant hopping, and long arms have a real finite-range Toeplitz kinetic term plus affine diagonal tension. Crosscomponent vertices have finite support after COM reduction. These are consequences of local nested commutators, not a selection of higher interactions.

The canonical E8 rotation and local N rotation agree on their first P-Q generator. Their difference at first order is entirely QQ; their second PP relative-unitary coefficient vanishes. Explicitly, with L1=A+B, B=QBQ, and both second generators PP-zero,

    P[(A+B)^2/2+A^2/2-(A+B)A]P=0.

Formal spectral-projector uniqueness makes the relative transformation block diagonal. Consequently D4-K4=[G3,K1]. Both external long slow states lie in ker K1, so their K4 matrix and vacuum subtraction agree. The previously computed coefficients ell/8+29/192, 19/32 and -13/128 in COM0 are therefore coefficients of this actual local normal form. Their bulk symbol at k=0 is c=109/96. This does not assert arbitrary off-block source or boundary gauge equality.

Split the compact graph into S (ell=2 host and axial-distance-two long arms), F (ell=1 host and adjacent long arms), and C (other ell>=3 arms). The closed-arm proof gives an analytic finite-rank correction O(Jz lambda^4) from C in the slow energy region. In slow units this is O(lambda^2); it does not alter either long-arm tension or bulk host dispersion.

## 2. Fast host with its native higher coefficients

In units Jz lambda the fast bulk symbol is

    e_lambda(k)=-4(cx+cy)-lambda(cx-cy)^2+O_m(lambda^2).

The remainder is a finite trigonometric polynomial with fixed Fourier support. Thus its fixed C^k norms are O_m(lambda^2), not merely its operator norm. Native reflections and xy exchange pin the two nondegenerate saddle points to (0,pi),(pi,0), with common energy -4lambda+O_m(lambda^2). The slow pole is tested at fast energy

    z=-6lambda+O(lambda^(7/3))-i Theta(lambda^3).

Its distance from the saddle energy is comparable to 2lambda. Analytic Morse coordinates and outgoing continuation through the regular negative-detuning interval give, uniformly on depth-lambda^3 disks,

    G_dd^out=-i/pi log(1/lambda)+O_m(1),
    G_ij^out=O_m(log(1/lambda))

for fixed local form factors, d=cx-cy. The positive leading coefficient follows from d^2=4 at both saddles and |det Hess|^(1/2)=4+O(lambda). This continuation is on the outgoing sheet; the ordinary lower-half-plane physical resolvent has the opposite sign and cannot replace it.

The ell=1 scalar is orbital B1 because the physical quarter-turn supplies phase (-1)^ell. Even reflections are imposed to distinguish B1 from B2. The origin hole is irrelevant in B1. The single adjacent scalar arm has kinetic -2T+O_m(lambda), positive slope lambda^3/16+O_m(lambda^4), and fixed endpoint corrections O_m(lambda). The general finite-range arm-strip theorem gives bounded endpoint Green entries and Im g11>=c>0. The leading host/arm coupling is -2, so

    |1-4G_dd g11| >= 4|G_dd||g11|-1 >= c log(1/lambda).

The coupled local Green matrix is O_m(log); higher finite contacts are O_m(lambda), restored by a finite-matrix Neumann series with parameter lambda log(1/lambda). The closed-arm correction is smaller in these units. S-F vertices start at Jz lambda^2 and have finite support. Eliminating the complete F block therefore produces a holomorphic slow-unit finite-support correction

    Delta_S=O_m(lambda log(1/lambda)).

No special cancellation to 1/log is required. Finite Fourier support and scalar graph identification are essential; a norm-only perturbation estimate would not prove this continuation.

## 3. Slow host: strict radiation channel without a fitted width

The leading S host is nearest-neighbor hopping -1 on Z^2 with the cross of five sites removed. Its symbol is h=-2(cx+cy); E=-2 is a regular energy. In the scalar hole basis c=delta0 and s=sum(nearest neighbors)/2,

    g_cs=(1-Eg_cc)/2,
    g_ss=(E^2g_cc-E)/4,
    det G_hh=(E g_cc-1)/4 !=0.

The inequality follows from Im g_cc<0 at a regular interior energy. For A=sum(axial distance-two sites)/2, the punctured self-energy is

    Sigma0=G_AA-G_Ah G_hh^-1 G_hA, evaluated at E=-2+i0.

Let b=G_hh^-1 G_hA and w=A-sum_h b_h delta_h. The exact Schur spectral-density identity gives

    -Im Sigma0=pi integral |Ahat-bhat|^2 delta(-2-h(k)) dk/(2pi)^2.

On this Fermi curve u+v=1, with u=cx,v=cy, every scalar hole correction is constant. But Ahat=cos2kx+cos2ky=-4uv varies from 0 to -1 along regular arcs. Hence the integral is strictly positive: Im Sigma0<0 and 1+Sigma0!=0. This establishes the open radiation channel analytically, without using a numerical width as an input.

Small native finite-range bulk corrections preserve regularity and local outgoing continuation. Finite contacts preserve the nonzero hole determinant. Restoring Delta_S then gives a finite-endpoint analytic self-energy change O_m(lambda log(1/lambda)), uniformly on the smaller depth-lambda^2 slow-energy disk.

## 4. Slow arm and pole stability

Checkerboard grading sends lambda to -lambda. Every S state has grading +1; hence its odd coefficients vanish. Its long arm in slow units is

    -T+f_lambda(n+2)+lambda^2 V+O_m(lambda^4) bounded terms,
    f_lambda=lambda^2/8+O_m(lambda^4),
    V=d I+a T+b(S^2+S*^2)+fixed endpoint matrix,
    d=29/192, a=19/32, b=-13/128.

Any difference caused by using f_lambda(n+2) rather than f_lambda n is a bounded O(lambda^4) term at higher orders. The leading scalar boundary is Sigma(E), with Sigma(-2)=Sigma0 from the punctured host. The checked range-two Airy theorem supplies a simple pole and fixed-endpoint Riesz residues O(f), f=lambda^2/8. Higher slope changes shift the Airy term by O(lambda^(10/3)) in slow units; higher bounded bulk terms are O(lambda^4). Both are smaller than the allowed O(lambda^(8/3)) error.

For clarity, the endpoint stability argument uses more than a global norm. For the baseline slow problem BEFORE adding the fast correction, on a contour of radius proportional to f^(2/3), the pole is unique and all fixed-endpoint Green entries are bounded. Subtract its O(f) endpoint residue divided by E-E_p. The remaining matrix is holomorphic and bounded throughout the interior by the maximum principle. The fast correction is added only on its proved lower-half-plane depth-f disk; no continuation of that correction across the large Airy contour is assumed. On that depth-f disk around E_p, an analytic finite-endpoint perturbation of size delta then moves this pole by O(f delta). This follows from the finite determinant lemma: the regular part is invertible by a Neumann series, and the remaining rank-one scalar equation has coefficient O(f delta). Cauchy bounds on a slightly larger depth-f disk control energy dependence; the derivative correction is O(delta), not delta/f, after multiplication by the endpoint residue.

Here delta=O_m(lambda log(1/lambda)), which tends to zero. Its physical pole shift is O_m(Jz lambda^5 log(1/lambda)), smaller than Jz lambda^(14/3). Small closed-arm contacts and finite slow-host corrections are covered simultaneously. Thus the complete fixed-order compact coefficient operator has the outgoing pole

    E_p/Jz = 8-6lambda^2
      +alpha1 lambda^2 (lambda^2/8)^(2/3)
      +lambda^4[109/96+(2+a0)/8]+O_m(lambda^(14/3)),
    a0=Sigma0/(1+Sigma0),
    Gamma=-2 Im E_p=(-Im a0)/4 Jz lambda^4+O_m(Jz lambda^(14/3)).

The sign is positive because Im a0=Im Sigma0/|1+Sigma0|^2<0. The derived feature extent is O(lambda^(-2/3)); the gap remains O(Jz), not a cosmological light mass.

## 5. Boundaries of the result

No higher coefficient has been chosen to enforce the pole: the fixed-order locality, parity, symmetry and leading coefficients determine this asymptotic result. Constants are not uniform as m tends to infinity. The actual local remainder theorem controls finite-time observables, but does not transfer outgoing poles through the many-body continuum. Original-source residue control, a selected state, scale setting, isotropic low-energy limit, physical detector coupling and cosmological identification remain open. No empirical fit or independent observation test occurs here. The use of the supplied Hamiltonian and ordered reference is conditional throughout.
