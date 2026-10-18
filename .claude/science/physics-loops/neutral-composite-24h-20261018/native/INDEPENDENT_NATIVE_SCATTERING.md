# Native N4 constituent scattering: independent check

Disposition: PASS for the stated coefficient scattering problem and retarded normalization. This is scattering of the two constituent flips in the N4 graph, not scattering of two composite features or a full-microscopic scattering theorem. Read /tmp/neutral_native_scattering_root.md and reused the checked threshold cavity identities.

## Exact finite-rank formula and sheet

Use the full oriented relative lattice as the reference normalization, with Fourier measure d^2k/(2pi)^2. Removing the origin is the infinite on-site-potential limit and contributes T0=-|0><0|/g. The punctured incident root amplitudes are therefore exactly

 h_i(k,z)=sqrt(2)[cos(k_i)-g_i(z)/g(z)].

The two normalized even roots are (|+e_i>+|-e_i>)/sqrt(2). Eliminating the closed native rays gives a diagonal root self-energy sigma(z). The additional distorted-wave finite-rank T matrix is (sigma^-1 I-G)^-1. Thus the full plane-wave kernel is exactly

 t(k',k;z)=-1/g+h(k',z)^T(sigma^-1 I-G)^-1 h(k,z).

The left distorted wave is the retarded analytic factor too. There is no complex conjugation of g or G in this analytic formula; taking an advanced conjugate there would change the T matrix. Real cosine external form factors and the transpose give reciprocity.

The branch sigma(z)=(z-sqrt(z^2-16))/2 with sqrt(z^2-16)~z at infinity is correct. For real z<-4 the square root on this branch is negative, giving sigma=(z+sqrt_positive(z^2-16))/2. Near the host threshold b_c>0 the rays remain closed, so there is no extra open-ray flux in the optical identity below.

## Reduction to the logarithmic denominator

Write D=(gx-g,gy-g), and define M=G+2DD^T/g exactly. The entries of M are the finite linear combinations of free potential differences obtained by expanding the exact cavity formula. Consequently M-M_edge=O(w log w), with parameter-uniform differentiated expansions near b_c. A=sigma^-1 I-M and q=2D^T A^-1D give

 sigma^-1 I-G=A+2DD^T/g.

For h0=-sqrt(2)D/g, the rank-one inverse identity yields exactly

 -1/g+h0^T(A+2DD^T/g)^-1 h0=-1/(g+q).

Near but below the critical b, A_edge has one simple eigenvalue of size b_c-b and its other eigenvalue stays separated from zero. Hence ||A^-1||=O(log(1/delta)) on the considered energy scale. The exact shallow bound condition is g(Eh-delta)+q(Eh-delta)=0, since A is invertible there. This eliminates the nonuniversal constant in g without fitting an additional interaction.

For w=s delta+i0, with s in any fixed compact subset of (0,infinity), the Green expansions and inverse identity give q(Eh+sdelta+i0)-q(Eh-delta)=O(delta log^p(1/delta)) for some fixed finite p. This tends to zero. The dressed root inverse is at most O(log^2(1/delta)): its extra denominator 1+q/g is O(1/log), while g+q has a nonzero limiting imaginary part. The external correction h-h0=O(|k|^2)=O(delta) therefore produces only vanishing cross and quadratic errors. All these estimates are uniform in the incoming and outgoing directions on the shrinking elliptical energy shell.

For the dispersion excess 2kx^2+2b ky^2, the edge density of states in this Fourier normalization is c(b)=1/(8pi sqrt(b)). The retarded Green difference is

 g(Eh+sdelta+i0)-g(Eh-delta)=c(b)[log s-i pi]+o(1).

The sign of the imaginary part is negative, consistent with (E+i0-H)^-1. Therefore

 t(k',k;Eh+sdelta+i0)=-1/{c(b)[log s-i pi]}+o(1).

Equivalently the strict limit uses c(b_c), since b tends to b_c. At s=1 this is -i/[pi c(b)], as proposed.

## Optical identity and physical even convention

In the oriented plane-wave normalization, the limiting direction-independent amplitude obeys

 Im t=-pi c(b)|t|^2.

Indeed integrating the on-shell intermediate oriented momenta gives precisely DOS c(b). This identity has the correct sign and normalization and reflects elastic flux in the only open host channel.

If instead momentum representatives are restricted to one half of the shell and normalized inversion-even states |k>_+=(|k>+|-k>)/sqrt(2) are used, their kernel is t_even=2t (away from the measure-zero fixed points). The half-shell density is c(b)/2. The same optical identity becomes Im t_even=-pi[c(b)/2]|t_even|^2. Thus one must change BOTH the amplitude and the state measure; keeping t_even with the full-shell DOS would introduce a factor-two error. The supplied oriented convention is internally consistent, and no physical cross section should be quoted without the associated flux and state normalization.

This derives a native coefficient-level logarithmic constituent collision amplitude from the puncture and attached rays. It does not establish two-composite scattering, a composite lifetime, an isolated full-H particle, or a weak-coupling scattering limit for the microscopic Hamiltonian. The selected COM momentum, binding regime, and the established native graph identification remain explicit premises.
