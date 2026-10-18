# Neutral domain composites from the native one-qubit Hamiltonian

Status: conditional-support. Finite canonical coefficients and exact rational
matrix elements support an expanded effective-model resonance. An infinite native
Hamiltonian pole, physical scalar identification and cosmological coupling remain
open. No interaction or degree of freedom is added to obtain these coefficients.

## Premises and reach

Start with the same directional bond Hamiltonian and its exact positive-parity
2×2×L rung representation from
[NATIVE_DERIVED_COLLECTIVE_INTERACTION_NOTE_2026-10-18.md](NATIVE_DERIVED_COLLECTIVE_INTERACTION_NOTE_2026-10-18.md).
Here the longitudinal coupling is dominant: λ=Jperp/Jz, both positive. This λ is
the inverse anisotropy convention of the weak-longitudinal block. The microscopic
Hamiltonian, thin periodic geometry, selected rung parity, aligned-vacuum sector
and anisotropic expansion are premises. Neither a three-dimensional continuum
nor a physical detector follows from this calculation. The color-symmetric vacuum
combination used for the source is specified, not a cosmological state derivation.

There are no observational datasets in this block. All finite sizes and momenta
are exposed model-development calculations. Independent algebraic checks test
calculations, not empirical predictions. No mass, lattice spacing, J scale,
Newton coupling, fermion identity or equivalence principle is fitted or derived.

## Complete first excited band

At Jperp=0 the eight uniform even-parity rung colors have E0=−4LJz. A pair of
colors differing in two physical bits, with one contiguous segment of either
color, gives two domain walls at energy E0+8Jz. All 24L(L−1) such states form the
complete first excited band. Let P project onto it, V be the original sum of
transverse rung bonds, Q=1−P and R=Q/(8−H0), using energies relative to E0 in Jz.
The canonical Hermitian band coefficients are

K1=PVP,
K2=PVRVP,
K3=PVRVRVP−{PVR²VP,K1}/2.

The reported excitation K2 adds L/2 to subtract the ground energy correction.
The enumeration includes every one-hop Q state, with its actual classical energy.
For K4 paths, second-hop states outside this first-hop set are also included.
Full 512-state L3 comparisons after polar identification show errors O(λ³) for
K1+λK2 and O(λ⁴) after K3; these are convergence checks, not uniform error bounds.

The original normalized transverse source V|vac>/sqrt(L) has norm squared4.
At q=0 its K1 Krylov chain has hopping2 (a finite folded terminal has 2sqrt2),
energies4cos((2m+1)π/L), weights16 sin²((2m+1)π/L)/L. Its continuum is broad,
not an isolated scalar mode.

## A derived internal state and bright continuum

K2 connects the source chain to a normalized state d2: a diagonal-column color
pair (physical xor6 or9) occupies a segment of length2, summed with translation
phase and color symmetry. It is constructed inside the same band. K1 d2=0.
No oscillator was appended to the Hamiltonian.

For principal momentum −π<q<π define u=cos q, c=cos(q/2), t=2c. Let A be a
half-line chain with nearest-neighbor hopping t and sites n=0,1,... . The local
coefficients extracted from the full finite native band are

B=−u A²/(4t²)+(u−1)I/2+(3/4−u/2)|0><0|,

C=(2u−1)A³/(32t²)−(7+6u)A/32
  +t(−21+10u)(|0><1|+|1><0|)/64.

In units Jperp, relative to8Jz, the bright Hamiltonian is A+λB+λ²C. Its coupling
to d2 is the derived vector

w=−sqrt2 λ|1>+λ²[−sqrt2 c|0>+c|2>/sqrt2],

and d2 has energy−2λ through this order. Finite L12,16 local entries at 12 momenta q<=3π/4 and complete
third-order invariant-subspace residuals are checked in the runner. Folded
terminals are not substituted for infinite-chain coefficients.

At energy−2λ the bright boundary wave satisfies φ1=−9λφ0/(4t)+O(λ²),
φ2=−φ0+O(λ). Thus the on-shell vertex is
3sqrt2(1−2u)λ²φ0/(8c), and the boundary density of states is1/(πt).
Direct resolvent expansion, including B, gives

Re Σbright = λ³ f(q)+..., f(q)=(1−9u)/(4(1+u)),

Γbright/Jperp = λ⁴ W(q)+..., W(q)=9(1−2u)²/(32c³).

The vanishing coefficient at q=±π/3 is not a protected stable state. This
expansion is nonuniform near q=±π and must not be used there. The later bound-state
expansion also requires fixed q away from |v|=|T| binding thresholds.

## Necessary correction: longer dark domains

Stopping at one internal state would miss a degenerate coupling. The full K4d2
has a component along d4. For L12 and q=0,π/6,π/3 its coefficient is exactly
reproduced numerically by−3cos(q)/32. The remainder is exhausted by d4, to roundoff,
after removing the bright chain and d2. L8 has a folded enhancement at q0.

Here dℓ is the analogous diagonal-column segment of lengthℓ. On checked L12,16,
even ℓ>=4 have K1dℓ=0, K2dℓ=−2dℓ and K3dℓ=0. Odd ℓ3 can have nonzero K3 and
must not be silently included in the even family. Full K4 actions at L12,q0 on
d4 and folded d6 close on their adjacent even-length states, after the bright
source subspace is included. This is a finite closure check, not an all-L proof.

Fraction-arithmetic translation kernels give:

- d2 diagonal, ground subtracted: −73/192, all other translations zero, L8,10.
- d4 diagonal: −13/96, all other translations zero, L14,16.
- d2↔d4 and d4↔d6: −3/64 at starts separated by0 and2, zero otherwise,
  L14,16. With segment-center phases this is−3cos(q)/32.

These certify exact finite entries at every allowed momentum on those sizes.
Locality and absence of additional relevant channels in the infinite expansion
remain to be proved. In particular, the first isolated-side-state pole is retained
only as a historical truncated-model calculation, not the native leading result.

## Expanded effective-model bound composite

Conditional on the preceding coefficient pattern and closure extending to the
infinite even-domain family, subtract8Jz−2Jperp²/Jz and divide byJperp⁴/Jz³.
The even-domain chain has bulk diagonal b=−13/96, hopping T=−3u/32, and boundary
defect

v=−47/192+f(q)=(1−479u)/(192(1+u)).

For |v|>|T| its normalized bound state has amplitudes sqrt(Z)(T/v)^n,
Z=1−(T/v)², and energy coefficient E4(q)=b+v+T²/v. The binding is generated by
native virtual processes and bright-continuum self-energy; it is not a supplied
potential. This state is bound relative to the slow dark-domain continuum but
still embedded in the bright continuum, so it is a resonance, not a stable
particle of the full model.

At q0:

E4=−63659/45888, Z=56797/57121,
E4(q)=E4(0)+(145219/456968)q²+O(q⁴),
Γ/Jperp=(511173/1827872)λ⁴+... .

The positive curvature gives motion in the conditional effective theory. Its gap
starts at8Jz; it is not a light cosmological scalar. The expanded resolvent pole
numerically approaches these coefficients. The width requires that the leading
bright loss remains localized at d2; tested even deeper domains have zero K3.
A uniform infinite-volume expansion and a native resonance continuation are not
yet established. A finite collection of exact entries cannot replace those steps.

## Coupling to the original composite observable

For the uniform O=Σj,a Zj,a Zj+2,a, canonical ground-to-band dressing gives
s1=V|vac> and s2=−K1V|vac>/4. This uniform observable accesses q0 only. This follows from the actual O differences: −8 on V|vac>, −16 on
K1V|vac>. For general momentum define the actual centered Fourier observable
O_q=Σj,a exp[iq(j+1)] Zj,a Zj+2,a. Its diagonal difference on a single flipped
rung is −8cos(q)exp(iqj). All aligned vacua have the same O_q eigenvalue (zero
for nonzero allowed momentum). Canonical second-order dressing is
( O_q−O_q,vac ) K1 V|vac>/64, not an assumed Fourier transform of the q0 result.
Direct diagonal-entry checks at18 momenta on L8,12,16 yield the bright source
cos(q)[2λ|0>−tλ²|1>/2]+O(λ³), with sqrt(L) normalization.
No independent detector coefficient is selected.

The leading pole residue in the expanded model is

Res O_q = [2Z(q)cos²(q)/c²] λ⁴+...,

hence at q0 coefficient113594/57121. At q=π/2 the leading physical source
vanishes; the earlier generic-source residue without cos²(q) is not a result
for this observable. This is a dimensionless matrix element of a
specified microscopic observable. It is not a matter coupling, measurement
identification, gravitational charge or environment-to-cosmology bridge.

## Verification and next hard residual

Run `python scripts/native_neutral_domain_resonance.py`. The runner binds input
hashes, reproduces finite canonical/source coefficients, rational translation
kernels and conditional pole mathematics. More expensive full K4 action results
are frozen auxiliary evidence with their scripts and hashes, explicitly labeled.
Independent reviews are in the campaign native directory. No audit verdict is
applied and no current authority surface is promoted.

Next: prove connected-support/all-length closure or find the omitted channel;
then test the native finite-H spectrum and response at growing length with the
correct degenerate dark basis. Equal coupling, broader cross section, state
selection and empirical identification remain separate tests.

Configuration-interaction resonances are established prior art, e.g.
[Fano, Physical Review124,1866(1961)](https://doi.org/10.1103/PhysRev.124.1866).
The proposed contribution here is the native coefficient/source reconstruction
and its exposed limits, not invention of resonance theory. The citation is
context only; its values are not inputs.
