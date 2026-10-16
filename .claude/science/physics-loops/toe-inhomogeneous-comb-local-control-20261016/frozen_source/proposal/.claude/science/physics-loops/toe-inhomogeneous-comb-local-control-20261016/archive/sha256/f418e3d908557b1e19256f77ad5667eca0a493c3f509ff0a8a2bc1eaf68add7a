# Current analytic checkpoint

Proposed count, not yet frozen or checked: A=L+q+1 complete sectors, each d=2^q dimensional, giving exactly A*d selected computational basis states (not the minimal V-dependent support). A determinant-one Givens elimination can use d(d-1)/2 two-level gates and one residual phase per block. Every within-sector prefix-code pair has Hamming distance at most 2q.

The primary proof provides a controlled-SU(2) recursion without extra ancillas. Independently counting its elementary forward sqrt(iSWAP)/Z base gives 152 gates; the recursion leaf count T(k)=2T(floor(k/2))+2T(ceil(k/2)) has T(1)=1. A phase on a nonvacuum computational basis state is lifted to a determinant-one diagonal pair with one initially zero ancilla; the selected sectors all have positive weight. Candidate routed count is (2n-1)*A*[d(d-1)/2*(152T(n-2)+68(q-1))+152T(n-1)], n=L+3q, hence O(L^4) for fixed q if the base and phase signs verify.

Named finite risk for a single exact check: paper exchange conjugation/control-bit orientation and the six-letter variable-XY reduction; these determine the 152/34 constants and global phase. Additional small exact checks may exercise the same sparse decomposition and clean-ancilla interfaces. No numerical evidence exists yet. Root proposal/reviews remain unread.
