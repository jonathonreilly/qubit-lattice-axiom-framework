# Native compass energy–composite bridge: exact tracial obstruction

Reviewed the current `native/compass_energy_bridge.py`. The proposed all-orders reason is valid, with boundary/state qualifications below. It strengthens the finite hierarchy check; it does not exclude finite-temperature or nonlinear coupling.

## Onsite automorphism

At site x=(x,y,z), take mod2 signs

    f_X=x+z, f_Y=y, f_Z=x+y+z=f_X+f_Y.

The relation f_X+f_Y+f_Z=0 ensures that these are Pauli-conjugation signs: choose I when (f_X,f_Y)=(0,0), X for(0,1), Y for(1,0), and Z for(1,1). Thus an onsite conjugation gamma sends sigma_x^a to (−1)^(f_a(x))sigma_x^a.

Along its own axis a, f_a(x+e_a)−f_a(x)=1 mod2. Every nearest compass bond consequently changes sign, while the distance-two neighbor pair has sign

    f_a(x−e_a)+f_a(x+e_a)=0 mod2.

Therefore, exactly,

    gamma(H)=−H, gamma(e_r)=−e_r, gamma(E_r)=−E_r,
    gamma(C_r)=C_r, E_r=2e_r/K.

The E normalization assumes K!=0; the underlying sign statements remain trivial at K=0. On the infinite lattice this is a well-defined automorphism of the quasi-local spin algebra; a single infinite-product Hilbert-space unitary need not be asserted. It preserves the tracial state. On periodic finite tori the period-two pattern is compatible when each side length is even. An odd-length periodic seam invalidates the all-bonds-flip identity. Open finite boxes with the corresponding available bonds do not have that periodic obstruction.

## Derivative hierarchy

For D=i[H,.], gamma D=−D gamma, so

    gamma(D^m C0)=(−1)^m D^m C0,
    gamma(D^n Er)=(−1)^(n+1) D^n Er.

Tracial invariance forces the mixed overlap to vanish whenever m+n is even. In particular <D^n C0,D^n Er>_HS=0 for every n and r.

For odd total derivative order, Pauli-weight parity supplies the complementary statement. A nonzero commutator with a two-site Pauli bond changes Pauli-word weight parity. Both C and E start with even weight, so the two differentiated operators have opposite weight parity when m+n is odd and are orthogonal. Hence **all** mixed derivative overlaps vanish, not merely the equal-order ones.

The script currently asserts only that the sum over displacements vanishes. For derivative order n>=1 that summed condition is also implied by total-energy conservation and is weaker than pointwise vanishing. Its empty recorded displacement lists establish the stronger computed check; the automorphism proves pointwise vanishing at all orders independently of that assertion.

## Entire unequal-time HS correlation

One can avoid inferring global time behavior from a Taylor series. Let

    F_r(t)=tr[C0(t) Er],

with the normalized tracial state. The automorphism intertwines dynamics t<->−t and changes Er's sign, giving F_r(t)=−F_r(−t).

Under the declared usual spin time reversal Theta, H,C,E are even, Theta C(t) Theta^−1=C(−t), and the trace is invariant with complex conjugation. Since the trace of a product of two Hermitian operators is real, F_r(t)=F_r(−t). Combining the two identities gives

    F_r(t)=0 for every real t and every r.

This uses existence of the standard finite-range spin dynamics, not an unproved infinite radius of Taylor convergence. It applies to the infinite-lattice tracial state and compatible finite tori. It is not a statement about an arbitrary ground state or a thermal state at beta!=0.

## The nonlinear connection remains exact

The previously checked identity is

    e_r²=(3K²/2)I+(K²/2)C_r,
    C_r=2e_r²/K²−3I.

Thus C is exactly present in local energy squared within this candidate. The linear tracial energy–composite channel vanishes because energy is odd under the spectral-reflection automorphism while its square is even. This is not statistical independence, and it is not absence of nonlinear energy content. No new microscopic interaction has been added to establish the identity or the obstruction.

## Finite-temperature exception is concrete

At beta!=0, gamma maps the Gibbs state of H at beta to the state at −beta; it does not preserve the same state. Therefore the tracial zero cannot be promoted to a finite-temperature zero.

A short local count gives an explicit allowed static channel on the nonaliasing lattice. For each axis, multiply C0's length-two pair by either of E0's two adjacent same-axis bonds. The result is the other nearest bond, which appears in H with coefficient K. These are six contributions; the cross-axis products are not nearest bonds. Hence

    tr(H C0 E0)=6K,
    <C0 E0>_beta=−6 beta K+O(beta²),
    <C0 e0>_beta=−3 beta K²+O(beta²).

The zero-temperature notation is not intended here: tr is the beta=0 normalized trace and the displayed formulas are high-temperature expansions. At this order subtracting the product of one-point means does not alter the result: <C0> starts at order beta² while <E0> starts at order beta. This is a thermal covariance under a supplied equilibrium preparation, not a calibrated source/detector or cosmological bridge.

Do not confuse that static linear-beta covariance with retarded response. For the convention chi=i theta(t)<[C0(t),Er]>_beta, the first beta coefficient equals minus the derivative of the tracial mixed correlation, which is identically zero. Thus any nonzero retarded channel begins at order beta² or higher in this expansion. The reflection/time-reversal relations further make this cross retarded response even in beta where the Gibbs expansion is analytic. These facts leave finite-temperature response open; they do not derive its magnitude or a physical state temperature.

## Scope conclusion

There is an exact absence of the **linear mixed tracial HS energy–composite correlation** for this supplied compass candidate, alongside an exact quadratic local-energy identity and an explicit permitted thermal static covariance. No conclusion about electromagnetic neutrality, universal scalar coupling, a ground-state pole or the cosmological scalar field follows without additional observations and dynamics.
