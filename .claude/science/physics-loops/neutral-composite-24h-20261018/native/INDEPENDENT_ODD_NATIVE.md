# Odd-height hierarchy, native nematic source and scalar darkness

Disposition: PASS at fixed even M>=4 and fixed odd open height L>=5, with the exact analytic hierarchy and native coefficients from the preceding check. No growing-size statement is obtained. Read /private/tmp/neutral_odd_root.md; no repository edits or numerical diagonalization performed.

## Odd-height representation and leading spectrum

The even-height multiplicity-one argument cannot be reused. On the column-sign quotient (a,b)~(-a,-b), A=product a and B=product b are well-defined for even M. The stated Gx=R_x and Gy=epsilon A C_y anticommute across families and commute within each family, with the single product relation. Their algebra has a two-dimensional irreducible factor and multiplicity two in each allowed central character on the P+ space. The relative R and relative C characters determine the center, subject to their one relation.

The native odd-height Y-pair process retains the column Y phases. A perfect row matching contributes epsilon B R_x, whereas the X-pair column matching contributes C_y. Thus U=epsilon B sum R_x and V=sum C_y anticommute, while each commutes with the physical plane algebra. Their squares are central. The previous valuation proof requires L>4, not even L, and applies unchanged to magnitudes and competing-event orders; the phases must be retained as here.

In the central sector with all relative R and C characters positive, U^2=V^2=M^2. It is the unique center with both maximal absolute sums. Its four-dimensional space is physical doublet times neutral multiplicity qubit. The two leading energies are +/-sqrt(2) M tau, each physically doubled. Every other center has at least one strictly smaller absolute sum, so its lowest leading energy is strictly higher at fixed M. The lowest actual states therefore belong to this center for sufficiently small lambda. Do not call the neutral gap the unrestricted first excitation gap: other centers can lie between the two neutral levels.

## Parameter derivative and connection

Use Jx=lambda Jz exp(delta), Jy=lambda Jz exp(-delta), so partial_delta H at delta=0 is exactly Hx-Hy. Perform the two exact analytic, symmetry-equivariant block reductions uniformly for delta in a fixed neighborhood of zero. At lambda=0 the first Kato projector is constant in delta. After dividing the aligned block by lambda^4, the leading plaquette operator is delta-independent because Jx^2 Jy^2 is unchanged. Its P+ projector is therefore also constant in delta at leading order. Both reductions can be chosen to tend to fixed identity identifications, with their parameter connections o(1).

More explicitly the first transformation is I+O(lambda), with delta derivative O(lambda). For the second reduction, only offdiagonal terms move P+; their size in rescaled units is O(lambda^(L-4)), and their delta derivatives have the same order at fixed L. Diagonal corrections preserve P+ and do not force an O(1) projector rotation. Thus the second connection tends to zero as well. These are analytic-parameter estimates; smallness of a transformation at a single delta would not by itself bound its derivative.

If K=W H W† and D=(partial_delta W)W†, then partial_delta K=W(partial_delta H)W†+[D,K]. The projected observable is partial_delta K-[D,K]. Every effective P+ coefficient before the hierarchical splitting is scalar by symmetry and the event valuation. Those terms commute with the connection; the first nonscalar piece is O(tau). Therefore the connection correction is o(tau), including after the exact reductions. No illicit derivative of an approximate eigenvalue is used as an exact observable identity.

Since t_x carries exp(L delta), t_y exp(-L delta), and the leading K is delta-independent, the n-event column and row amplitudes carry exp(+Ln delta) and exp(-Ln delta). Consequently

    (Hx-Hy)_eff = Ln tau (U-V)+o(tau)

for the relevant offdiagonal elements, with the stated sign convention. In the maximal center, U-V anticommutes with U+V and (U-V)^2=2M^2. The transition weight per normalized ground state is therefore 2M^2(Ln tau)^2+o(tau^2); physical-doublet averaging does not multiply it by two. This observable is plane-neutral but odd under xy exchange: a nematic diagnostic, not the scalar original readout.

## Exact darkness of the xy-even original C

Let the spatial xy swap be accompanied by the spin rotation sending X to Y and Y to -X. At isotropy it is an exact Hamiltonian symmetry, preserves the maximal central sector, and swaps the two leading neutral operators U and V. The original uniform longitudinal C is even under it and commutes with all plane generators.

Within the symmetry-resolved isolated four-state low band, the physical plane algebra is M2 acting on its irreducible doublet, tensored with identity on the multiplicity qubit. The exchange normalizes that algebra. Factoring an intertwiner implementing its automorphism on the physical doublet leaves a unitary acting on the multiplicity qubit. That multiplicity unitary is not scalar: its conjugation swaps U and V, which are independent anticommuting matrices. A nonscalar two-dimensional unitary has two distinct eigenvalues, so its commutant is abelian. Every operator commuting with both the plane algebra and exchange has its band compression in that abelian algebra. Hence the compressed exact H and original xy-even C commute exactly.

This representation statement persists under the exact symmetry-equivariant band continuation. It is a statement inside the maximal-center four-state band, not that C commutes with H on the full Hilbert space or has no transitions out of the band. The four states are best described as a symmetry-resolved low band; other central sectors have levels between its two doublets. The leading swap calculation establishes the nontrivial multiplicity action, and exact symmetry intertwining preserves it. No claim that mere plane neutrality forces darkness at odd height is valid.

## Explicit example and limitations

For M=4,L=5, K=19Jz lambda^4/128, t=Jz lambda^5/16, tau=Jz lambda^6/76. Thus the first neutral transition within the selected center is

    2sqrt(2) M tau = (2sqrt(2)/19) Jz lambda^6+o(lambda^6),

and its Hx-Hy weight is 3200 tau^2+o(tau^2). These are fixed-size native asymptotics, not an 80-qubit ED result. The physical plane doublet is protected; the multiplicity qubit is the neutral transition. No isotropic three-dimensional mediator, empirical detector coupling, cosmological scalar or uniform-size limit follows.
