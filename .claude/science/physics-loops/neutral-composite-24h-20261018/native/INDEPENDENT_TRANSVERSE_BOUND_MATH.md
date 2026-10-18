# Transverse high-momentum bound branch: independent analytic check

Disposition: PASS for the supplied infinite graph and stated source vector. Its identification with the full compact layer-even native N4 K1 is a separate native-reduction premise; the finite cutoff code alone does not establish that identification. Inspected /tmp/neutral_transverse_bound.py and JSON. No canonical edits.

At a=c=1,b=0 the y=1 host row is a full hopping-2 chain whose origin has one additional semi-infinite y arm. Gauge the positive y-arm hopping to negative. This is a three-lead junction with all hopping -2. The y=0 half-chain joined to the x arm is a full chain; each y>=2 row is a full chain. There is no further sub--4 component. Any zero isolated pieces in an enlarged representation likewise do not affect the lower bound.

For the junction write root amplitude v and each lead amplitude v r^n. The equations E=-2(r+r^-1) and E=-6r give r=1/sqrt(2), E0=-3sqrt(2). Normalization is v^2[1+3r^2/(1-r^2)]=4v^2, hence v=1/2 and root WEIGHT 1/4. The number 1/2 is the root amplitude, not its probability. The lower eigenvalue is simple; the symmetric upper partner is above the band, and the remaining junction channels have no eigenvalue below -4. The gap is d=3sqrt(2)-4.

The host perturbation in b has norm at most 4|b|, as can be seen before the relative-coordinate inversion quotient from -2b(S_y+S_y*); the normalized even quotient preserves the norm bound. Hence the isolated eigenvalue persists, simple and real analytic, for 8|b|<d. Its separation from all other spectrum is at least d-8|b|. This is a sufficient local condition, not the largest possible existence interval. Nearby a,c are also bounded perturbations, so the local multivariable branch and its Hessian are legitimate.

## Second-order coefficient

Let V=partial_b H. V psi0 is supported only on the complementary full chains: on the combined y=0/x-arm chain it is f_n=-4v r^n for n>=1 and zero on the other half; on the y=2 chain it is f_n=-2v r^|n| for n in Z. Both are orthogonal to the unperturbed junction eigenvector. At E0 the full-chain Green kernel is

 (E0-H_chain)^-1(n,m)=-r^|n-m|/sqrt(2).

The required sums are exactly

 S++=sum_(n,m>=1) r^(n+m+|n-m|)=sum_(j>=1)(2j-1)2^-j=3,
 Sabs=sum_(n,m in Z) r^(|n|+|m|+|n-m|)=13.

For the latter, split into two same-sign nonzero quadrants (2*3), two opposite-sign quadrants (2*1), one-zero pairs (4*1), and the origin (1). Therefore

 E2=<Vpsi0,(E0-H_chain)^-1 Vpsi0>
   =-[16v^2*3+4v^2*13]/sqrt(2)=-25/sqrt(2).

This is the coefficient of b^2, not E''(0); the latter is twice it. A host gauge (-1)^y, extended constantly along each attached arm, changes b to -b and preserves a,c, so the eigenvalue is even and E(b)=E0-25b^2/sqrt(2)+O(b^4).

## Source and other curvatures

The first-order correction at the x root is

 psi'_x(0)=(4v/sqrt(2))sum_(m>=1) r^(|1-m|+m)=4v=2.

Choose analytic real phase with the y-root amplitude positive. Then psi_y=v+O(b^2), psi_x=2b+O(b^3); the source defined in the code is -psi_x+b psi_y=-3b/2+O(b^3). Multiplying by the separately stipulated native factor lambda gives -3lambda b/2+O(lambda b^3). This coefficient would change if the native source has an additional normalization; none is checked by the graph code itself. In particular the source vanishes exactly at b=0.

Each lead has sum_(n>=0)psi_n psi_(n+1)=v^2 r/(1-r^2)=r/2. Hellmann-Feynman gives partial_a E=-4r=-2sqrt(2) for the two horizontal leads, and partial_c E=-2r=-sqrt(2) for the single gauged y arm. With a=cos(Qx/2), c=cos(Qz/2), b=cos(Qy/2) and delta=Qy-pi, the quadratic expansion is

 E=-3sqrt(2)+sqrt(2)Qx^2/4+sqrt(2)Qz^2/8-25delta^2/(4sqrt(2))+O(|(Qx,delta,Qz)|^4).

These are the quadratic coefficients; the respective second derivatives are twice them. The exact gauge evenness in b and the cosines in Qx,Qz exclude mixed quadratic terms. The branch is a saddle, with positive x,z and negative y curvature. This supplies no Lorentz-scalar or isotropic mass interpretation. All energies here are K1 coefficients; the physical native leading energy correction carries its separate Jz lambda prefactor, and higher-order native stability/source corrections require their own bounds.
