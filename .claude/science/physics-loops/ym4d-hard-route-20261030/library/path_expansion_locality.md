# Path expansion of an inverse, and Mobius locality in local parameters

Credit: the parametrix and random-walk expansion is the method of T. Balaban (CMP 89, 95, 96, 99; titles and reviews only here, bodies unread) as exposed in J. Dimock, arXiv:1108.1335, section 2.4, which I read. The statement below is written here for arbitrary local parameters. Status: proved here. Consumers: `parts/hard-core--independent.md`, Text 4.4, 4.5.

## Setting

Let H be a bounded invertible operator on a Hilbert space E = direct sum over sites of E_x, and let {c} be a finite family of patches, with functions h_c, 0 <= h_c <= 1, supp h_c in c, sum_c h_c^2 = 1, and local inverses: operators S_c supported in the enlarged patch c^+ with H S_c = 1 on functions supported on supp h_c. Assume that patches meet a bounded number nu of others, and that

    eps := sup_c || [H, h_c] S_c h_c || * nu < 1.                                                                                      (1)

## Lemma 1 (path expansion)

With K := sum_c h_c S_c h_c and E_c := [H, h_c] S_c h_c, we have H K = 1 + sum_c E_c, and

    H^{-1} = K sum_{n >= 0} (- sum_c E_c)^n = sum over paths w = (c_0, c_1, ..., c_n) of (-1)^n h_{c_0} S_{c_0} h_{c_0} E_{c_1} ... E_{c_n},

where only paths with consecutive patches at distance bounded by the range of E contribute. The series converges in operator norm, with sum over paths of length n at most ||K|| eps^n.

*Proof.* H h_c S_c h_c = h_c H S_c h_c + [H, h_c] S_c h_c = h_c^2 + E_c, using H S_c = 1 on supp h_c. Sum over c, using sum h_c^2 = 1. Then ||sum_c E_c|| <= eps by the almost-orthogonality count in (1), and the Neumann series gives a right inverse. Since H is invertible it is the inverse.  []

## Lemma 2 (Mobius locality)

Let the operators depend on parameters t = (t_c), with H(t) and S_c(t) depending only on the t at patches within a bounded distance of c, and (1) holding uniformly in t in a set T containing a base point 0. For G(t) := <f, H(t)^{-1} g> and a set A of patches, put

    M_A(t) := sum_{B subset A} (-1)^{|A \ B|} G(t 1_B).

Then |M_A(t)| <= C ||f|| ||g|| eps^{tau(A) / r}, where tau(A) is the length of the shortest tree joining the patches of A, and r the bounded range.

*Proof.* Expand G by Lemma 1. A term for the path w depends only on t near w. If w misses a patch c of A, then the alternating sum over the inclusion of c vanishes for that term. So only paths visiting a neighbourhood of every patch of A survive. Such a path has length at least tau(A) / r. There are at most 2^{|A|} terms in B, but the alternating sum is applied term by term, so each surviving path term enters with a factor at most 2^{|A|}, and |A| <= C tau(A) / r + 1. Summing eps^n over n >= tau(A) / r and adjusting eps by that factor gives the bound.  []

## Remarks

- Decay in the distances between sources f, g follows in the same way, since a path must connect them.
- log det: d/ds log det H_s = Tr(H_s^{-1} dH_s/ds) for a linear path H_s from a local reference; the trace is a sum over sites of matrix elements, and Lemma 2 applies to each.
- Fractional powers: C^{1/2} = (1 / 2 pi i) contour integral of z^{1/2} (z - C)^{-1}, on a contour at positive distance from the spectrum; Lemma 1 applies to each resolvent, with eps uniform along the contour when the local inverses are.

## Hostile check

(a) H S_c = 1 on supp h_c is a real requirement: for a saddle operator with a constraint, the local inverse must solve the local saddle problem, with free or Dirichlet boundary outside c^+, and then H S_c differs from 1 by a boundary term supported outside supp h_c if supp h_c is well inside c^+. Correct. (b) The eps in (1) must be small, not merely below 1, for useful decay. In the application, the commutator of h_c gains 1 / R. (c) No lower bound on the spectrum of H beyond invertibility is used in Lemma 1; invertibility itself also follows when H is self-adjoint and K is an approximate right inverse with eps < 1.
