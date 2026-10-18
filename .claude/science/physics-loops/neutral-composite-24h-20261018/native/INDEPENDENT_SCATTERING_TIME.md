# Independent check: closed-ray moments and finite-time transfer

Scope: focused mathematical check of `/tmp/neutral_scattering_time_root.md`. No repository edits, formal audit, or claim of a microscopic infinite-time scattering matrix.

## 1. Uniform ray moments: valid operator proof

Write the coefficient operator on host plus two rays as K=[[Hh,V†],[V,Hr]], and let P=1_I(K), A=K restricted to Ran P. Assume sup I <= -4-g for a fixed g>0. Each ray is a nearest-neighbor halfline with hopping magnitude 2, so Hr+4 >=0. With X=pi_r P and Y=pi_h P, the exact intertwining equation is

    (Hr+4)X-X(A+4)=-VY.

Its bounded solution is

    X=- integral_0^infinity exp[-s(Hr+4)] VY exp[s(A+4)] ds.

The sign is correct: differentiation of the integrand gives minus the Sylvester operator, and the endpoint at infinity vanishes. No generalized-eigenvector integration or absolutely continuous spectrum hypothesis is required. This proof includes discrete eigenvectors in I.

For rigor with unbounded exponential weights, first use W_R=exp(mu min(ell,R)) on each ray. The conjugation difference W_R Hr W_R^-1-Hr has norm at most C(e^mu-1), uniformly R and uniformly in a clamped ray's length. Bounded perturbation of the contraction semigroup gives

    ||W_R exp[-s(Hr+4)] W_R^-1|| <= exp[C(e^mu-1)s].

V is supported at a fixed finite set of root sites, so ||W_R V|| is uniformly bounded. Choose mu>0 with C(e^mu-1)<g. The integral then bounds ||W_R X|| by a constant independent of R, delta, time, and host volume. Monotone convergence of the squared weighted norm gives ||exp(mu ell) pi_r P||<=C. The host can be assigned ell=1. Consequently, for every fixed p,

    sup_t ||ell^p exp(-itK)P|| <= C_p.

The constants require a uniform gap g below the ray band, not a gap below the host spectrum. This is exactly the useful circumstance near the stated transverse threshold. The same argument applies to finite clamped rays because their spectra remain in [-4,4].

## 2. Finite physical embedding: necessary scope

The bound above is for the host-plus-clamped-ray coefficient graph. It is NOT a bound on the complete physical finite-torus N4 spectral projector measured by interval length relative to one all-up background. Complement intervals and background-related configurations prevent that inference.

The draft now avoids this mistake. A periodic transverse host with normalized physical pair-orbit conventions and rays clamped at ell<L/16 embeds into the compact physical N4 sector. The embedding is an exact isometry when defined directly on this normalized finite graph. Comparing it with an infinite-ray graph introduces exponentially small truncation errors on Ran P. Special self-inverse relative positions on an even torus must retain their actual orbit normalization; they cannot simply be counted twice. Even COM mesh indices remove the half-COM relative-coordinate twist. These are representation requirements for the finite graph, not new physical assumptions.

At the terminal ray boundary the omitted native K1 link acts only on exponentially small terminal amplitudes. Thus its defect on Ran P is O(exp(-cL)), uniformly during coefficient evolution. No truncation of arbitrary transverse wavefunctions is required when the host is periodic from the start. A separate infinite-host packet limit remains separate work.

## 3. Duhamel estimate: valid conditional on the previously established local bounds

Use the established fixed-order bound

    ||(Dj-Evac,j) phi|| <= Cj ||(ell+1)phi||

on the compact sector, including output leakage from the length cutoff. The exponential ray estimate supplies its right side uniformly for phi=exp(-itK)P psi. The finite sum of j>=2 terms therefore has generator defect O(J lambda^2), not a volume-sized defect. This conclusion depends on the previously proved fixed-order local counting bound; the ray argument alone does not prove it.

With the order-40 global normal-form remainder O(J lambda^29), the ground-energy shift of the same order, and the exponentially small K1 embedding defect, variation of constants yields, for |t|<=S/(J lambda delta),

    error <= C_S lambda/delta
             + C_S lambda^28/delta
             + C_S exp(-cL)/delta,

up to equally small initial truncation/isometry errors. The factor J cancels as stated. On the finite box all operators are bounded; the uniform estimates also justify the corresponding domain-controlled infinite coefficient evolution.

This uses a single fixed embedding T and unitary dressing U. It does not require an evolving choice of background or multiply errors by the ground-space dimension. Extending T simultaneously over the ground orbit requires the earlier disjoint-orbit/isometry argument; it is not supplied merely by the ground projector's proximity. For an excitation prepared as U†T psi, no identification with a measured source-created state follows automatically.

For delta=lambda^alpha the transfer error tends to zero for alpha<1; the existing stricter alpha<2/3 is therefore sufficient. The time estimate establishes actual finite-time norm approximation for specified coefficient packets. It does not establish that those packets have completed their asymptotic collision at that time, does not transfer the infinite-time coefficient S matrix, and does not select a preparation or physical detector coupling.

## Conclusion

The closed-ray moment lemma and the stated clamped-periodic finite-time Duhamel transfer are mathematically sound with the explicit finite-graph normalization and previously established fixed-order coefficient bounds. The revised draft correctly avoids the full finite-physical-projector mistake. No additional claim about an actual infinite-time scattering matrix follows.
