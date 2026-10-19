# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# All-length leading tunneling source derivative

The identity can be proved for every fixed open length L>=3 by the exactly free Ising chain at s=0 and a Wick/Hellmann-Feynman calculation. No free-fermion assumption at nonzero s is needed. For L2 the source sum is empty and the result is zero. This proves the leading tunneling coefficient's derivative, not an exact finite-g formula or a uniform-in-L expansion.

Set K=2Jz>0, h=g>0, r=h/K, and

H(s)=-K sum_(j=1..L-1) Z_j Z_(j+1)-h sum_j X_j+2s sum_(j=1..L-2) Z_j Z_(j+2).

The two lowest states at s=0 differ by occupation of the exponentially small Majorana mode. Their splitting is Delta E=2K r^L[1+O(r²)] for each fixed L. Let t=Delta E/2, consistent with the off-diagonal Hamiltonian term -t between aligned configurations.

## Majorana signs and soft-mode matrix elements

Define a_j=(prod_(l<j)X_l)Z_j, b_j=(prod_(l<j)X_l)Y_j. Then i a_j b_j=X_j and i b_j a_(j+1)=Z_j Z_(j+1). Thus H(0)=-i sum_(jk) b_j B_jk a_k, with B_jk=K delta_(k,j+1)-h delta_(jk).

Let C_jk=<i b_j a_k>. The ground-state C is the polar matrix of B. Choosing the soft singular vectors with a-side components v_k=r^(k-1)[1+O(r²)] and b-side components u_j=-r^(L-j)[1+O(r²)], occupation of this mode changes the covariance by -2u_j v_k. Hence, with Delta meaning first excited minus ground,

Delta C_jk=2 r^(L-j+k-1)[1+O(r²)].

These asymptotics follow directly from the bidiagonal singular-vector recurrences Bv=sigma u and B^T u=sigma v. The first nonzero coefficients of both edge-localized vectors have magnitude one; normalization and opposite-edge corrections enter at relative order r² or higher. The minus sign of u gives the positive Delta C above, consistent with positive splitting2sigma and B's negative end-to-end effective coupling.

## Background contractions

Write Cbar=(C_excited+C_ground)/2, which removes the soft-mode contribution. For every j=1,...,L-2,

Cbar_(j,j+1)=1+O(r²),
Cbar_(j+1,j+2)=1+O(r²),
Cbar_(j,j+2)=r/2+O(r³),
Cbar_(j+1,j+1)=O(r).

The r/2 coefficient is local and the same at every such j, including the near-end cases. At h=0 the two neighboring strong bonds are independent Majorana dimers. The transverse field on their shared spin creates two dimer excitations costing4K; first-order perturbation gives the next-dimer contraction +h/(2K). Fields at either distant end do not change that first-order local contraction. Equivalently it follows by expanding the polar matrix on these adjacent dimers. The on-site contraction is -r/2 to first order at this shared interior spin, but only its O(r) bound is needed below.

## Wick difference for each original distance-two term

At s=0 the real bipartite quadratic Hamiltonian has no off-diagonal same-species a-a or b-b covariance. The Gaussian Wick identity therefore gives

<W_j>=<Z_j Z_(j+2)>
=C_(j,j+1) C_(j+1,j+2)-C_(j,j+2) C_(j+1,j+1).

Use the average/difference identity for each product, which is exact and avoids a discarded quadratic Delta term. The two nearest-bond changes each contribute2r^L to Delta<W_j>. In the crossed product, Delta C_(j+1,j+1)=2r^(L-1) multiplies Cbar_(j,j+2)=r/2, contributing r^L with the MINUS Wick sign. The other crossed contribution is O(r^(L+2)). Therefore

Delta<W_j>=4r^L-r^L+O(r^(L+2))
           =3r^L+O(r^(L+2)),

independently of j. Missing the crossed Wick term would incorrectly give4 instead of3.

## Hellmann-Feynman derivative

For h>0 and fixed finite L the two levels are distinct, so ordinary Hellmann-Feynman differentiation applies at s=0. The perturbation is PLUS2s sum W_j, hence

partial_s Delta E=2 sum_j Delta<W_j>
                 =6(L-2)r^L+O(r^(L+2)).

Dividing by Delta E=2K r^L[1+O(r²)] yields

(t'/t)_(s=0)=3(L-2)/K+O(r²)
            =3(L-2)/(2Jz)+O(g²/Jz³).

In particular the EXACT derivative ratio of the LEADING h^L tunneling coefficient is3(L-2)/(2Jz), as in the subset recurrence. Equivalently each local source term2s W_j contributes3/(2Jz) to that leading coefficient's logarithmic derivative. The finite-g full splitting has higher corrections; do not write the leading identity as an exact formula for that full splitting.

The sign is positive: positive s lowers the virtual defect costs, increasing the tunneling magnitude t. The corresponding coefficient in the effective Hamiltonian -t(s) times the aligned-column flip operator differentiates to -t'(0), so the original observable's off-diagonal coefficient carries the negative sign. This agrees with the previous denominator convention.

## Scope

Only the derivative at s=0 uses free-fermion solvability. The s-dependent distance-two Ising chain need not remain quadratic; Hellmann-Feynman makes that irrelevant to this first derivative. The source is a differentiation device for an existing readout, not a new physical interaction. All asymptotics are at fixed finite L with open boundaries and small g/Jz. Uniformity in growing L, additional native transverse edges and the complete original-source dressing remain separate questions.
