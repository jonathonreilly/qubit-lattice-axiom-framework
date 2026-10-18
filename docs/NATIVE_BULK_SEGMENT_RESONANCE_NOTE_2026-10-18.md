# Native bulk segments and a conditional large-feature resonance

Status: conditional-support. The supplied one-qubit Hamiltonian produces an extensive positive segment tension and endpoint motion without cutting column ends or adding an interaction. Their leading source-connected coefficient model has outgoing resonances whose characteristic length grows as inverse anisotropy. Native higher-order control at that growing length remains open. This is not an established native scalar, observed particle, or cosmological field.

Use H=-sum_(x,a) J_a sigma_x^a sigma_(x+e_a)^a with Jx=Jy=lambda Jz>0. A uniformly polarized Z background is prepared; strong Jz alone does not select it from all aligned-column backgrounds. Finite excitations and relative even parity in every transverse plane are considered, or finite periodic boxes before a limit. No literal undefined infinite product of plane operators is needed. All numerical cases are exposed model development; there are no empirical inputs.

## Four walls and the source-connected channel

Four longitudinal broken bonds cost8Jz. In the relative even-plane sector, any compact configuration at that energy consists of two distinct columns reversed over the same finite longitudinal interval. Each nonempty finite column costs at least two walls; a single column with two intervals violates plane parity. The two columns can be arbitrarily separated.

For interval length one, native transverse bonds exchange either flipped spin with an unoccupied neighbor. XX and YY both give hopping -Jperp on the uniform background. At zero total transverse momentum, the relative coordinate has hopping -2 in Jperp units on Z² excluding the origin. For interval length at least two, only adjacent columns can extend or contract at first order. X-oriented pairs have endpoint amplitude -Jperp, Y-oriented pairs +Jperp. At zero longitudinal momentum the two endpoints add.

The physical square rotation includes a spin rotation. Its scalar interval state is E_l=(|x,l>+(-1)^l|y,l>)/sqrt(2). At l=1 it maps to the normalized even relative vector

d=(|ex>+|-ex>-|ey>-|-ey>)/2.

The source-connected K1 is therefore a two-dimensional hopping-2 host, coupled with amplitude -2 from d to a half-line E2,E3,... whose hopping is also -2. The d-wave reflection sector vanishes at the relative origin, so hard-core deletion has no extra effect there. Long intervals on nonadjacent columns are frozen at K1 and remain additional states in the energy8 band. This channel is not the complete band and need not close at higher orders.

Direct physical-bit projection on a5x5x9 periodic grid checks the normalized matrix elements and a frozen-channel control. The225 physical spins are represented by bitstrings in the specified projected configurations, not by diagonalizing their full2^225-dimensional Hilbert space. Uniformity is important: arbitrary aligned-column signs can give nonzero transverse hopping flux. Gauge equivalence must be established before using the same host in another background.

## Coupling to the original observable

Keep C=sum_(x,y,z) Z_(x,y,z)Z_(x,y,z+2). A transverse pair flip from the prepared vacuum changes C by -8 and costs8Jz. First-order ground dressing is -V|0>/(8Jz), so the connected transition source is V|0>/Jz. For C/sqrt(Nphysical), the two orientations each have Nphysical translates. Consequently

C_connected|0> = -sqrt(2)lambda d + higher orders.

The leading total source norm squared is2lambda². This fixes a microscopic readout; it does not identify C with an experimental detector or a gravitational scalar. No independent source coefficient is fitted.

## A tension is generated inside the uncut bulk

The [checked fourth-order local plaquette term](NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md), reproduced by [the native plaquette runner](../scripts/native_column_plaquette_selection.py), per height is -k4 P, k4=Jperp^4/(128Jz^3). A long reversed adjacent-column interval changes four plaquette signs per interior slice. Its vacuum-subtracted diagonal energy density is therefore

sigma=8k4=Jz lambda^4/16.

Two columns sharing no plaquette instead have tension Jz lambda^4/8; diagonal neighbors share one and have3Jz lambda^4/32. In a local motif far from either endpoint, the preexisting walls cancel from every intermediate energy denominator. The same signed plaquette coefficient applies to the excited band. Second-order interior returns are spin-independent, and no odd three-step loop exists. Endpoint terms occupy bounded neighborhoods at fixed order; they do not contribute an extensive interior coefficient. This proves a local finite-order tension, not an isolated string eigenvalue or a uniform growing-length expansion.

A separate exact second-order projection supplies a missing mass correction. For an adjacent pair of length l>=3, the vacuum-subtracted diagonal is -5/2 in Jperp²/Jz units. Four endpoint changes by two layers each have coefficient -1/8; there are no other entries in that row. Four endpoint-adjacent layers each contribute(1-6)/8 to the diagonal: the shared bond has zero intermediate cost and is excluded, while six exterior incident bonds have cost4. Remote repeated-edge shifts cancel the vacuum. An endpoint change by two has exactly one permitted cost8 intermediate.

At zero longitudinal center-of-mass momentum, the long-arm K2 symbol in relative momentum k is -5/2-(1/2)cos(2k), with edge -3. Thus a native arm edge already includes -3Jz lambda², larger than the Airy level spacing below. Short length-one/two boundary rows and K3 corrections are not supplied by this long-arm statement.

## Solving the explicitly conditional confined-channel model

Now retain K1 and the linear tension in the source-connected channel. This is a specified partial coefficient model, not a claim that omitted native terms vanish. In units Jperp, let f=lambda³/16 and n=l-1>=1. The arm has hopping -2 and diagonal f(n+1). Its endpoint couples to d with amplitude -2.

The retarded host matrix element is

G(E)=average_(kx,ky) [(cos kx-cos ky)^2/(E+4cos kx+4cos ky+i0)].

At E=-4, G=-.2817722049865-.0870681002914i. The self-energy is Sigma=4G. The zero-energy extrapolated boundary location is a=Sigma/(2+Sigma)=-.976549771107-.788599975044i. This follows from the ghost value psi0=-Sigma psi1/2 and the zero-energy linear solution psi_n proportional to n-a.

The unconfined coupled model does not acquire a state below its host band: for E<-8, the rank-one bound-state condition is4G(E)g_arm(E)=1. Its largest limiting product at -8 is(2/pi-1/2)(4-2sqrt(3))=.07321431535<1; positivity and monotonicity of the two negative resolvents bound it below that value for lower E. Bipartite symmetry gives the corresponding upper-band result. The small-f low levels discussed next lie inside the host continuum, not below it.

For fixed Airy index j and f tending to zero, the outgoing-sheet asymptotic in this coefficient model is

E_j=-4+2^(1/3)f^(2/3)|a_Airy,j|+f(1+a)+o(f).

The size scale is L=(2/f)^(1/3)=32^(1/3)/lambda. Physical spacings scale as Jz lambda³. With Ephysical=Ereal-i Gamma/2, the full width is

Gamma=.09857499688 Jz lambda^4+o(lambda^4).

A frozen-boundary complex tridiagonal calculation and a frequency-dependent outgoing continuation/continued-fraction calculation independently approach this coefficient. At lambda=.2,.1,.05,.025 the latter gives Gamma/(Jz lambda^4)=.09838151,.09852041,.09856057,.09857129. These are convergence controls for the stated coefficient model, not finite native spectra. Simply evaluating the physical-sheet resolvent below the real axis would give the wrong prescription; the code continues the upper boundary value through a local analytic integral representation.

The original normalized C source has complex resonance residue

Res_C ~ (G²(1-a)²/4) lambda^5
       =(.02073497093+.09626339064i)lambda^5.

It is a complex pole residue, not a positive spectral weight or probability. A measured line area would require the full real-frequency background and interference. The growing size accompanies a diminishing microscopic response.

## The conditional branch is not an isotropic scalar

Longitudinal total momentum p changes the endpoint hop to -2cos(p/2). The arm edge -4cos(p/2) has quadratic coefficient +Jz lambda/2 in physical units. Transverse center-of-mass momentum Q instead changes the host dispersion to -4[cos(Qx/2)cos kx+cos(Qy/2)cos ky]. For the continued d-channel Green function, at Q=0,

dG/d(Qx²)=(G+E G')/16,
da/d(Qx²)=(G+E G')/[2(2+4G)²].

At E=-4 this last coefficient is -.08901367093+.01449119580i. The real transverse quadratic coefficient in the conditional boundary energy is therefore -.00556335443 Jz lambda^4, with the same result for Qy. Hard-core subtraction starts at Q^4 because Gd0 vanishes at Q=0. The other orientation channel has a distinct boundary scattering eigenvalue, so its off-diagonal Q² mixing also affects this branch only at Q^4. This branch has a negative transverse coefficient, not a positive isotropic effective mass. Native higher-order control is still absent; the calculation cannot be promoted to a microscopic dispersion. Even the partial model does not supply the desired relativistic scalar near zero momentum.

## What has and has not been derived

The local tension, first-order channel/source normalization and all-length long-arm K2 row come from the original Hamiltonian. They remove the need to append an interaction or cut column ends to motivate a large finite segment. The Airy resonances solve an explicit partial coefficient model assembled from those terms. Their promotion to native resonances requires the remaining short-channel and higher-order operators, a uniform expansion at length1/lambda, control of coupling to all other four-wall states, and a prepared-state/native spectral connection. The lambda² mass correction above illustrates why absolute native energies cannot be read from K1 plus tension alone.

The model Hamiltonian, anisotropy, uniform background, state/sector, and measurement identification remain premises. The characteristic size is in lattice units; the physical lattice spacing and Jz have not been derived. No physical scalar, fermion, universal force, cosmological connection or TOE closure is claimed.

Weak-confinement spectra of spin-chain kinks have established prior art, for example [Rutkevich's solution of a two-kink model](https://arxiv.org/abs/1003.5654). Airy scaling is not a novelty claim. The question here is which tension, kinetic channel and readout follow from this supplied directional Hamiltonian without an added confining field.

## Reproduction

Run `python scripts/native_bulk_segment_resonance.py`. It repeats physical-bit source/channel projection, exact local second-order rows, frozen-boundary and outgoing frequency-dependent resonance controls, and the independent dispersion quadrature. The result separates native local calculations from partial-model spectra. Local tension reuses the linked plaquette calculation cited above; independent checks and exact input identities are preserved in the campaign pack. The scratch output locations in the individual reproducers are explicit and do not imply independent observational data.
