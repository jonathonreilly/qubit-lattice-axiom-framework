> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# A pole-free ladder band and normalized scattering-packet interface

Status: new bounded author derivation, pending distinct check. The exact center solution is LADDER_SCATTERING_REDUCTION.md SHA `4f22fdb84d7636a6caad536323e5f02f971fba04a22ae9e8292e3c4e234929cc`, currently undergoing distinct check. This note is conditional on that source's explicit finite matrices; their norms are bounded independently below. No endpoint-seed, finite-cut or release-time theorem is imported.

ROOT requested an explicit band and derivative interface. The constants here are deliberately coarse and obtained analytically, with no scan or scientific executable. Frozen predecessors remain unchanged.

## Finite matching matrix and normalization convention

Use exactly the six-vertex core, positive coefficients and unit leads of the center source. Write k0=pi/2, E(k)=2−2cos k, z(k)=exp(ik). The core matrix H_core includes the unit lead bond's +1 diagonal at each port but not the external lead vertices. Let P:C²->C⁶ insert the left/right port amplitudes. Conditional on old X1X2=p, define

    F_p(k)=H_core,p−E(k)I−z(k)PP†.                (1)

For incoming channel amplitude a in C², the complete six-core stationary field and outgoing channel amplitudes are

    T_p(k)a=−2i sin(k) F_p(k)^{-1}P a,
    S_p(k)a=P†T_p(k)a−a.                          (2)

Indeed on either lead the amplitude is a_j e^{-ikn}+(S_pa)_j e^{ikn}, n>=0, with n=0 the port. At n=1 it equals z times the port amplitude plus (z^{-1}−z)a_j. Substitution gives (1)-(2). The four internal-head map is T_int,p=P_int T_p. Port vertices are counted once, as n=0 on their leads.

These are amplitudes with equal lead flux because both leads have the same dispersion and velocity 2sin k. The old sectors share this same channel measure and velocity. No momentum or flux Jacobian is missing between sectors.

## Explicit center inverse bound

Let f=1/sqrt(8). At k0 the four-internal-vertex matrix K_p has outer diagonal d=f/4 at v,w. Eliminating them leaves the two-by-two matrix [[0,−p],[−p,0]] on A,B, whose inverse norm is 1. Each outer-to-inner elimination coefficient is c/d=2. The resulting K_p^{-1} has outer diagonal block bounded by d^{-1}+4, off-diagonal block norm <=2, and inner block norm <=1. Its norm is bounded by the norm of the real symmetric two-by-two comparison matrix

    [d^{-1}+4  2; 2  1],

which is at most its maximum row sum d^{-1}+6=8sqrt(2)+6<18. The block comparison follows by applying the triangle inequality to the norms of the outer and inner vector components; it does not depend on signs of p.

The port/internal coupling matrix C has orthogonal columns of squared norm (f/2)²+(3f)²=37/32, so ||C||<2. At k0 the port Schur matrix after outgoing lead elimination is

    [3p/4−i   5p/4; 5p/4   3p/4−i].

Its eigenvalues are 2p−i and −p/2−i, giving inverse norm 2/sqrt(5)<1. The full block inverse of F_p is the sum of the internal inverse block and a lifted Schur inverse. Consequently

    ||F_p(k0)^{-1}||
       <=18+(1+18*2)²<1400.                       (3)

For example the lifted part is [I;−K_p^{-1}C] times the Schur inverse times [I,−C†K_p^{-1}], whose two outside norms are each <=1+||K_p^{-1}C||. Thus (3) is a full six-dimensional norm bound, not just a port estimate.

## Pole-free interval and first derivatives

For real k, ||F_p(k)−F_p(k0)||<=3|k−k0|, since |E'|<=2 and |z'|=1. On the closed interval

    I={k: |k−pi/2|<=10^{-4}},

the Neumann product in (3) is <=0.42<1/2. Therefore uniformly for p=±1,

    ||F_p(k)^{-1}||<=2800.                         (4)

The internal K_p(k) separately remains invertible there: ||K_p(k)−K_p(k0)||<=2|k−k0| and ||K_p(k0)^{-1}||<18. Thus this interval is free both of the internal elimination poles and of full outgoing matching poles. No determinant sign is inferred only from numerical proximity.

With R_p=F_p^{-1}, one has R_p'=−R_p F_p'R_p and ||F_p'||<=3. It follows that

    ||R_p'||<=23,520,000,
    ||T_p||,||T_int,p||<=5600,
    ||T_p'||,||T_int,p'||,||S_p'||<=48,000,000.      (5)

Indeed differentiating (2) costs at most 2||R_p||+2||R_p'||<=47,045,600. The larger stated integer constant covers all three maps. All six core fields, including both ports, are included in T_p; no hidden internal mode is dropped. These constants are uniform on I and may be very far from sharp.

At any real k in I the stationary solution conserves probability current. Summing the finite-core stationary continuity equations leaves only the two lead currents, each 2sin k times incoming norm squared minus outgoing norm squared. Thus ||S_pa||=||a|| for all a, and the square two-by-two S_p is unitary. This can also be verified directly from F_p−F_p†=−2i sin k PP† and (2). Its norm is exactly 1, despite the coarse inverse bound.

The center source gives S_p(k0)=t_p X_ports, with t_p=−exp(−i theta)w_p. Therefore, on any narrower support |k−k0|<=h<=10^{-4},

    ||S_p(k)−t_p X_ports||<=48,000,000 h.          (6)

This is a full two-port column/operator bound, including reflection. It does not only compare transmission phases or probabilities. In particular sector-dependent delay is paid by (6) on a narrow band, rather than presumed equal.

## Exact packet normalization without a completeness assumption

For completeness, (1)-(5) support a normalized stationary-superposition interface. Let g be a C² compactly supported incoming two-port amplitude in the interior of I with integral ||g(k)||² dk=1. Form the lead fields

    psi_j(n,t)=1/sqrt(2pi) integral
        [e^{-ikn}g_j(k)+e^{ikn}(S_p(k)g(k))_j]
                         e^{-itE(k)} dk,

for n>=0, and use T_int,p(k)g(k) in the same integral for the four internal vertices. At n=0 formula (2) makes the port values exactly T_p g, so they are not independently added again. This superposition solves the bounded one-head Schrodinger equation of the infinite two-lead graph exactly. Smooth compact support and the analytic inverse on I justify differentiation; all fields are square summable for each finite t.

Here is a direct norm argument, rather than an assumption of scattering completeness. Extend g by zero to the full circle. Parseval makes the complete integer-lattice incoming Fourier sequence have norm 1. As t tends to minus infinity, its mass lies on n>=0: on the excluded negative indices the phase derivative has fixed sign and magnitude at least |n|+v_min|t|, where v_min=min_I 2sin k>0. One integration by parts with the compactly supported smooth amplitude bounds the corresponding squared tail by a constant times sum_{n>=0}(n+v_min|t|)^{-2}, which tends to zero. The outgoing sequence on n>=0 has the same nonstationary bound at negative times, with amplitude S_p g; (5) supplies its first derivative. Each of the four internal integrals tends to zero by one integration by parts in E(k), again because E'(k)>=v_min. Cross terms vanish by Cauchy-Schwarz.

Thus the full packet norm tends to 1 in the remote past. Its exact bounded selfadjoint evolution conserves norm, so it is exactly 1 at every finite time. At positive infinite time the same argument removes the incoming and internal pieces; the outgoing spectral amplitude is exactly S_p g. This constructs the needed packet and its asymptotic channel normalization without asserting that these packets span all states or that a local product seed has no bound-state component.

The argument extends to finite-dimensional coherent old-sector and passive-reference amplitudes using the same operator bounds. Infinite passive extensions follow by the norm bounds and finite-rank approximation. For arbitrary such normalized incoming amplitudes supported within h, (6) and Parseval give outgoing spectral L² error <=48,000,000 h against the common ideal amplitude

    −exp(−i theta) W X_ports g(k).

The comparator has norm 1 because W and X_ports are unitary. This is an asymptotic scattering-packet error statement, not a finite-time full-output bound against an already departed packet. No fixed-time internal tail constant or physical endpoint-source normalization has been imported.

## What remains before finite release

The explicit pole-free band and full internal first-derivative bounds now provide a conservative scattering interface. A finite product-seed theorem still needs a launcher with sufficient spectral weight in that band, an explicit vector comparison to the packet above, cut/return estimates, quantitative internal and source vacancy bounds at the chosen output interval, and the separately charged mediator/vacancy physical errors. A microscopic product input need not lie in this constructed continuum subspace. These obligations cannot be waived by perfect center transmission or by unitarity of S_p.

Only this note was written. The matrix bounds and packet norm argument were derived analytically with no scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication or delegation. Predecessor sources remain frozen. Distinct checking is required before promotion.
