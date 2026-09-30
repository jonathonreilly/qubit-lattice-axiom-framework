# Exact shared outgoing row for opposite protected polarities

A separate analytical discriminator after the one-polarity proof. The target is only to determine whether opposite protected inputs can cancel at a common outgoing row of the ACTUAL H2 with consistent Gauss fields. It is not an invariant-module construction. No computation or hypothetical independent edge weights are used.

Take L>=12 divisible by four and n=L^3/2. Put

    a=(0,0,0), h_+=(2,0,0), h_-=(-2,0,0),
    b_+=(1,0,0), b_-=(-1,0,0), v=(1,L/2,0).              (1)

The A radius-two neighborhoods of h_+ and h_- intersect only at a. There is no periodic short-path alias at these distances. Their immediate B stars are disjoint. Construct an output word beta with hole a and unique B vacancy v. Set all eighteen occupied A sites in the first radius-two neighborhood to plus, all eighteen in the second to minus. Set the six immediate B neighbors of h_+ to plus and those of h_- to minus. Fill every other B site except v, and every A except a.

Complete the remaining signs so that exactly r=(n-2)/2 occupied sites are minus. This is possible: twenty-four minuses and twenty-four pluses have been prescribed among 2n-2 occupied sites, and r>=24 while there are more than r-24 unassigned occupied sites. Then beta has NB=n-1, total charge n, and a physical integer Gauss flow E_beta. A spanning tree supplies one. The vacancy v is at graph distance at least L/2+1>=7 from h_+, and at least L/2+3 from h_-, so both distance-three B neighborhoods are full.

Define alpha_+ by moving the hole from a to h_+, filling a with plus and retaining the whole B pattern. Define alpha_- by moving the hole from a to h_-, filling a with minus and retaining that B pattern. Assign their fields by reversing the following actual axial two-hop paths:

    Delta_+ = +e_(h_+,b_+) - e_(a,b_+),
    Delta_- = -e_(h_-,b_-) + e_(a,b_-),
    E_+ = E_beta-Delta_+,  E_- = E_beta-Delta_-.           (2)

Here e denotes a unit field on the corresponding A-to-B edge. For alpha_+, F_(h_+)* transfers the B+ at b_+ into h_+, then F_a moves the A+ into b_+. For alpha_-, the two transferred charges are minus, giving the signs in Delta_-. Both inverse paths preserve every actual Gauss equation. The source inputs have the same total charge n; each has merely exchanged its hole with an A site of the appropriate sign.

The word alpha_+ obeys all local support conditions of P_+, and alpha_- obeys those of P_-. In each, all A within distance two of its hole have the chosen sign, all B within distance three are occupied, and its six neighbors carry that sign. Their distinct hole positions make them orthogonal.

For the COMPLETE canceled block P_a H P_(h_sigma)=[F_a,F_(h_sigma)*], the axial stars share only b_sigma. The selected order is legal, the reverse first hop from a is blocked, and all different-intermediate paths have canceled in the exact original formula. Therefore

    <beta,H alpha_+>=<beta,H alpha_->=1.                  (3)

In fact these are the only outgoing words at hole a from these two inputs. With w=(alpha_+-alpha_-)/sqrt(2),

    P_a H w=0.                                           (4)

The electric outputs in (3) are the SAME E_beta, not merely the same occupation pattern. After physical Fourier transformation the corresponding input monomials in the actual cycle variables retain this cancellation. Thus no independent-phase assignment can justify treating these two outgoing sectors as orthogonal.

This is not a dark eigenvector. For example c=(4,0,0) is an allowed axial output from h_+ through (3,0,0), with coefficient one and its genuine two-link field shift. The input at h_- cannot reach hole c in one H step, because their periodic distance is six. Hence H w has a nonzero component at c while w has none. The remaining rows are not canceled.

The construction proves exactly why separate one-polarity eigenvector exclusions cannot simply be added: their actual mixed-star boundary rows can interfere. It does not exhibit a positive-measure dark module, prove generic-phase failure, or place positive Omega weight on w. The formal source-image condition and the full coherent dark-module problem remain unresolved.
