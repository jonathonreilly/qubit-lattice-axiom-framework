# Solar external-field quadrupole: initial independent derivation

Recorded before numerical quadrupole evaluation or reading the parent's derivation/code. The primary-paper PDFs have been downloaded and their abstracts/metadata seen, including the known Cassini summaries. Their detailed quadrupole formulae have not yet been inspected in this block. This is an original derivation of a known calculation, not a novelty claim.

Additional supplied field premise: `laplacian Phi = div[nu(|grad Phi_N|/a0) grad Phi_N]`, `laplacian Phi_N=4pi G rho`, with `nu(y)=1/[1-exp(-sqrt(y))]`. The galaxy packet calibrated an algebraic circular rule, not this nonspherical PDE. Its a0 is therefore a provisional input for this completion, not an already completed joint fit.

Let the physical Newtonian potential be negative for an attractive source: `Phi_N=-GM/r-g_Ne z`. The uniform Newtonian external acceleration points along +z. Set `rM=sqrt(GM/a0)`, `x=r/rM`, `c=cos(theta)` and `eta=g_Ne/a0`. Then the dimensionless Newtonian potential gradient is

`u=n/x²-eta e_z`, `v=|u|=sqrt(x^-4+eta²-2eta c/x²)`.

The extra Poisson source is

`rho_p = a0/(4pi G rM) D`, `D=div_x[(nu(v)-1)u]`.

Away from the origin, div u=0 and the Jacobian is `(I-3nn)/x³`. Thus

`D = nu'(v) [v²-3(x^-2-eta c)²] / (v x³)`.

Since nu approaches 1 exponentially at large argument, no extra delta mass sits at the origin. The zero of u at x=eta^-1/2,c=1 is an integrable saddle singularity and must be resolved numerically, not clipped away. At infinity the external constant field has zero divergence and D decreases as x^-3.

The Green solution has `delta Phi(r)=-G integral rho_p(r')/|r-r'| d³r'`, up to constant and uniform-acceleration terms. Its Hessian at the origin is

`H_ij=-G integral rho_p(r') [3n_i'n_j'-delta_ij]/r'^3 d³r'`.

Define the Cassini-type positive quadrupole convention explicitly by

`delta Phi_quad = -Q2/2 * [z²-r²/3]`.

Therefore `Hzz=-2Q2/3`, `Hxx=Hyy=Q2/3`. With `P2(c)=(3c²-1)/2`, direct substitution gives the dimensionless response

`F(eta)=Q2*rM/a0=(3/2) integral_0^infinity dx integral_-1^1 dc P2(c) D(x,c)/x`.

An integration by parts moves div off the source. The boundary terms vanish: the near-origin factor nu-1 is exponentially small, and at infinity the quadrupole test function falls as x^-3. With w=1/x,

`F(eta)=(9/4) integral_0^infinity dw integral_-1^1 dc [nu(sqrt(w^4+eta²-2eta w²c))-1] * [w²(3c²-1)+eta(3c-5c³)]`.

The first form uses nu' and the actual phantom density. The second uses nu-1 and independent angular/radial differentiation algebra. They must agree numerically. Under c -> -c the latter gains an overall minus sign relative to the common polynomial `w²(1-3c²)+eta(3c-5c³)`, with the plus cross-term under the square root. This records the convention before checking published q definitions.

Q2 scales as `a0^(3/2)/sqrt(GM)` times F(eta); it is a nonlocal field response. The fact that nu differs negligibly from 1 at a planet does not bound F. For eta=0 exact spherical symmetry forces F=0. For nu=1 it vanishes identically. The physical-to-Newtonian background conversion is a separate premise: the frequently used equation `g_e/a0=eta nu(eta)` is exact for a spherical algebraic parent solution, but a uniform local QUMOND boundary alone does not impose it. A flattened Galactic field or a nonzero harmonic/curl contribution can change the inferred eta.

Next: inspect primary equations/measurement conventions, freeze numerical ranges and source roles, then evaluate both integral forms. No a0 or nu parameter is to be fit to Solar data.
