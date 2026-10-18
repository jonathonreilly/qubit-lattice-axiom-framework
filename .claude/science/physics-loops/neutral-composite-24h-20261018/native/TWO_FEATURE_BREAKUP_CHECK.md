# Native four-singleton breakup channel at total momentum 2Q

Read `native/FINITE_FEATURE_COLLISION_PROOF.md` and `native/LARGE_BOUND_FEATURE_PROOF.md`. A valid native on-shell four-singleton channel exists at the total momentum of two near-threshold features. It uses transverse motion in one common longitudinal layer, not independent three-dimensional single-particle motion.

## Native hopping and wall sector

Place four down spins in distinct, widely separated transverse columns, all at one z layer. Each isolated spin creates two longitudinal walls, so N=8. The common layer contains four flips and every other layer zero, hence all longitudinal Z-plane parities are even, as for the two-feature sector.

A transverse bond swapping a down spin with an up neighbor preserves its two walls. The original XX Hamiltonian contributes -1 in K1. The mixed-spin YY product is +1, so -YY also contributes -1. Thus each isolated singleton moves by the original square-lattice hopping operator with dispersion -2(cos kx+cos ky). No longitudinal hopping is asserted: K1 contains transverse edges only, and a separated singleton remains in its layer. Pair interval growth requires transverse adjacency and is absent while the packets are separated.

For four separated singleton packets, K1 therefore acts as the sum of four such two-dimensional hopping operators, up to contact terms excluded by support separation. Hard-core coincidence constraints do not change this asymptotic channel.

## Explicit on-shell momenta

Let Qy=2acos(b), and let P be the principal representative of 2Qy modulo2pi, near -0.94787389 at the critical point. Set q=P/4. Write the one-feature bound energy as

E_b=-4(1+b)-delta.

Choose four transverse carrier momenta

(theta,q), (-theta,q), (theta,q), (-theta,q),

where

cos theta=1+b+delta/4-cos q.

Their total momentum is (0,P), exactly 2Q modulo reciprocal lattice vectors, and their native K1 energy is

-8cos theta-8cos q=-8(1+b)-2delta=2E_b.

At the certified critical b with delta=0, cos theta is approximately0.26270278851, strictly inside(-1,1). It therefore remains admissible for all sufficiently near-threshold bound states with small positive delta. This is not a generic continuum assertion: the displayed momenta explicitly realize the correct native energy and total momentum.

Numerical values at the critical endpoint are Qy approximately2.66765570852, P approximately-0.94787389014, q approximately-0.23696847253, theta approximately1.30497401287, and energy approximately-9.87805520742. The same subchannel, varying theta, has bottom -8[1+cos(P/4)] approximately-15.77643289934. Thus the two-feature energy is well inside this breakup channel, not at its threshold.

## Weyl sequence and exact momentum

Take smooth transverse packets of width M around the four carrier momenta and put their centers at separations much larger than M. Symmetrize over identical spin flips; disjoint supports make the resulting computational configurations distinct and avoid hard-core collisions. The free packet residual is O(1/M), while all native contact or interval-growth terms vanish on supports kept separated beyond their interaction range. Send M and separations to infinity.

For an exact total-momentum fiber, construct the packets in three relative transverse coordinates and impose the fourth carrier momentum by total momentum P, rather than treating localized absolute packets as exact momentum eigenstates. The relative packets can escape contact while retaining the same residual estimate. Longitudinal total momentum zero is obtained by the uniform common-layer fiber; this does not grant independent z motion to the four spins.

On finite periodic boxes, individual carriers can be approximated on compatible meshes with their sum fixed to the allowed P; the rounding energy error tends to zero. It is unnecessary to assume P/4 itself is exactly a one-spin mesh point. Packet widths and separations must remain much smaller than the box before the limiting argument.

## Symmetry qualifications

Layer-even parity is exact in the single-reference compact representation. Infinite physical X/Y plane flips change the ordered background and are not operators within that one reference finite-excitation Hilbert space. Therefore the infinite-volume Weyl statement should be named layer-neutral, not silently identified with every possible plane-character representation.

On large even finite tori, use the same plane-character orbit construction as for the candidate features. The four-singleton configurations have the same diagonal stabilizer characters as the reference: longitudinal plane parity and global spin-flip parity are even. Background-changing plane images have disjoint support. Thus orbit averaging in a selected compatible character sector is nonzero and preserves normalization and residual estimates. The all-plus plane sector is translation invariant; other chosen characters need the appropriate translation-compatible orbit construction. This shows there is no extra fixed-x or fixed-y parity obstruction requiring independent singleton motions to be forbidden.

At the non-special total P, transverse y reflection changes the momentum and is not a little-group restriction. If x-reflection evenness is required, reflect and symmetrize the separated packet arrangement; the carrier list and energy are invariant under x momentum reversal, and separated reflected supports give a nonzero even packet. Identical-spin exchange symmetry is already built into the computational-state construction.

## What this does not prove

The result supplies an on-shell native K1 breakup channel with the same total momentum and compatible finite-volume neutral characters. It does not compute a transition amplitude from the particular two-feature quasimode into that channel. Configuration connectivity, energy overlap, and the existence of a Weyl sequence do not exclude destructive interference, an embedded eigenstate, or further selection rules for a specific matrix element. No decay rate, scattering cross section, lifetime, or loss of the previously established finite-window ladder follows without that dynamical calculation. Nor does this coefficient channel alone prove an on-shell continuum of the full microscopic Hamiltonian at the same corrected energy.
