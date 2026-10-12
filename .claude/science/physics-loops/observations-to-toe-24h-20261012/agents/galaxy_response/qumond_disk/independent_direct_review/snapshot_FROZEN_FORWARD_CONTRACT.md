# Actual isolated QUMOND disk field: forward comparison contract

This block resolves the specific gap between the preceding algebraic galaxy rotation rule and the newly supplied QUMOND PDE. It is a forward calculation at the already frozen galaxy parameters, not a refit. The earlier galaxy targets and Solar comparison are exposed; any comparison here is model development, not blind validation. No galaxy PDE output has been evaluated before this contract.

Source pin: origin/main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`; prior galaxy source/calibration artifacts are unchanged. New paths are confined to `agents/galaxy_response/qumond_disk/` and runtime `galaxy_response/qumond_disk/`. Deadline and stop markers remain binding. Computations use one CPU and less than2GB memory, in tracked foreground commands.

## Inputs and subset, fixed before PDE discrepancies

Use the existing 64-term positive Gaussian-ring mass reconstructions, gas sheet and exponential-height stellar disk, with **one global stellar M/L=0.5605122519882025**, **a0=7.658058668049826e-11 m/s^2**. Use the previous numerical G=4.30091e-6 kpc (km/s)^2 per Solar mass. Do not fit distances, inclinations, a0, M/L, external fields, or per-galaxy gravity parameters.

Initial subset uses source/geometry criteria only: accepted in both64 and96 reconstructions; stellar surface-brightness fractional L1 diagnostic<=0.10; minimum scored radius/sigma>=2; stellar height/sigma>=0.3. Partition by reconstructed gas mass fraction including the fixed stellar M/L into `[0,.25)`, `[.25,.75)`, `[.75,1]`. In each bin choose the greatest h/Rmax, breaking ties lexicographically. This gives **NGC2976**, **UGC07577**, **KK98-251**. All three happen to belong to the already exposed training sample; no held-out claim will be attached to them. Record the full eligible ordering before the first forward output.

First compare the field at the original scored radii R>=0.5 Rd. Evaluate the original algebraic radial rule, the local norm-based disk approximation, and the full PDE prediction on the identical fixed source. Only after numerical checks pass inspect their rotation-velocity residuals against the existing processed Vobs. No raw likelihood is constructed from SPARC mass-model tables.

If all three pass the declared numerical gates, expand to the next two source-ranked objects in each bin using the same criteria and parameters. Stop expansion on numerical failure and report the unresolved calculation instead of selecting galaxies by model agreement. A future fit or broader dataset pass requires a separately frozen contract.

## Field equation, boundary and gas-sheet treatment

Use the same supplied `laplacian Phi=div[nu(|grad Phi_N|/a0) grad Phi_N]`, `nu(y)=1/[1-exp(-sqrt(y))]`, `laplacian Phi_N=4 pi G rho_b`. Galaxies are axisymmetric, reflection symmetric and isolated, with zero imposed external field. These are additional physical modeling assumptions. They match the earlier no-EFE algebraic comparison but do not describe every actual galaxy environment.

The asymptotic isolated acceleration is `sqrt(G M a0)/r`; the potential is logarithmic and cannot be set to zero at infinity. Treat its monopole exactly. Higher angular modes have the regular interior/decaying exterior solution; no arbitrary homogeneous tidal term is supplied. Test truncation of the exterior anisotropic contribution explicitly.

For a ring of mass M, radius A and Gaussian smoothing sigma,

`Sigma_tilde(k)=M/(2 pi) J0(kA) exp(-sigma^2 k^2/2)`.

At z>=0, the finite-height exponential convolution of exp(-k|z|) is

`Z_h(k,z)=[exp(-kz)-kh exp(-z/h)]/[1-(kh)^2]`,

`V_h(k,z)=[exp(-kz)-exp(-z/h)]/[1-(kh)^2]`.

Here `-partial_z Z_h=k V_h`. At kh=1, the continuous limits are `Z_h=(1+z/h)exp(-z/h)/2`, `V_h=(z/h)exp(-z/h)/2`. For a thin sheet both equal exp(-kz). Thus the Newtonian potential gradients are

`U_R=G sum M integral dk k J1(kR) J0(kA) exp(-sigma^2 k^2/2) Z_h`,

`U_z=G sum M integral dk k J0(kR) J0(kA) exp(-sigma^2 k^2/2) V_h`.

At the gas sheet use the upper trace: `U_z(R,0+)=2 pi G Sigma_gas(R)`. The stellar U_z vanishes by symmetry. The QUMOND radial field is continuous across the sheet. Its tangential algebraic input is therefore `A_R(R,0+)=nu(sqrt(U_R^2+U_z^2)/a0) U_R`, not nu(U_R/a0)U_R. No finite thickness is silently assigned to the gas. The full field additionally requires the nonlocal Poisson projection below.

## Derived Poisson projection without source differentiation

Let `A=nu(|U|/a0)U`; use spherical coordinates r,c=cos(theta), with

`A_r=sum a_l(r) P_l(c)`, `A_theta=sum b_l(r) partial_theta P_l(c)`.

Only even l occur. On the upper hemisphere,

`a_l=(2l+1) integral_0^1 dc A_r P_l`,

`b_l=(2l+1)/[l(l+1)] integral_0^1 dc A_theta partial_theta P_l`, l>0.

The radial Poisson equation is

`(r^2 phi_l')'-l(l+1)phi_l=(r^2 a_l)'-l(l+1)r b_l`.

The regular/decaying Green solution, integrated by parts, gives for l>=2

`phi_l'=a_l-l(l+1)/(2l+1) [S_l+T_l]`,

`S_l=r^(-l-2) integral_0^r dt t^(l+1)[a_l+(l+1)b_l]`,

`T_l=r^(l-1) integral_r^infinity dt t^(-l)[a_l-l b_l]`.

The monopole satisfies phi_0'=a_0. At the midplane the full radial field is therefore

`g_Q(R)=A_R(R,0+)-sum_even_l>=2 l(l+1)/(2l+1) P_l(0)[S_l(R)+T_l(R)]`.

Keeping the exact local A_R and expanding only the solenoidal correction avoids slowly reconstructing the gas-sheet source as scalar multipoles. The angular derivative formula includes the sheet distribution through the vector-field upper/lower traces; there is no omitted delta-source differentiation. In log radius u=ln r, S and T are exponential one-sided convolutions with rates l+2 and l-1. Integrate piecewise-linear coefficient functions analytically within each radial cell, avoiding overflow from large powers of r.

An exact gradient A=grad f has `a_l=f_l'`, `b_l=f_l/r`; its two terms reduce to S=f_l/r and T=-f_l/r. The correction vanishes. This supplies checks independent of the implementation.

## Controls and bounded accuracy plan

1. Analytic Newtonian Gaussian sheet: exact midplane radial field and axial field. Also directly integrate the finite-height vertical convolution to check Z_h,V_h and their kh=1 limits.
2. Any spherical test field (choose a Plummer sphere) under this nu: the exact QUMOND field is the algebraic radial response and all angular corrections vanish.
3. Kuzmin disk: `Phi_N=-GM/sqrt(R^2+(|z|+b)^2)`. In each half-space U is radial about a displaced point; nu(|U|)U is curl-free, and its tangential trace is continuous. Hence its exact QUMOND radial field is `nu(GM/[a0(R^2+b^2)]) GM R/(R^2+b^2)^(3/2)`. Use this exact result, not a tuned expected constant.
4. Set nu=1 in each real-source calculation. The Poisson projection must recover the already checked Newtonian field, including the finite-height stars and gas sheet.

Initial discretizations: radial log grids384 and768 points; angular hemisphere Gauss-Legendre64 and128 points; even modes through32 and64; Hankel orders1024 and2048; inner cutoff sigma/16 and outer cutoff8 Rmax. Include all scored radii as exact radial grid points. Refine separately as needed to radial1536, angular256, modes128, Hankel4096, inner sigma/32 and outer16 Rmax, retaining failed checks. Cached coefficient arrays may be reused, but only matching source/parameter/grid hashes count. No solver target will be used to choose a galaxy.

Acceptance gates at scored radii: direct Newtonian midplane Hankel reconstruction relative error<=2e-6 against the frozen component forward model; independent Gaussian/vertical controls<=5e-7; spherical projection error<=1e-9; Kuzmin and real-source nu=1 projection errors<=0.003; full QUMOND force resolution change<=0.005 and boundary change<=0.003. A conservative working numerical budget of1% in radial force applies only after these checks. Refinement differences are numerical evidence, not interval-certified bounds. Nonpositive radial force is a model/rotation-support result, not changed to an absolute value.

Report the fixed-parameter change from the original algebraic rule, its decomposition into the local full-norm effect and nonlocal correction, and the resulting conditional residuals. Do not infer a new galaxy-calibrated a0 or claim the Solar comparison has survived a PDE refit: no such fit occurs here.
