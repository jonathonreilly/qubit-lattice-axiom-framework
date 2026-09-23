# Post-PRE clarification: finite-spin instrument losses

2026-09-23. This clarification corrects the comment at line 116 of the frozen
independent decisive_controls.py, which says: "Two instruments can have
different finite-spin losses; check their shared rotor limit directly."
For the stipulated resolved/coherent edge instruments, that possibility is
false. The PRE file is preserved unchanged for provenance; this clarification
supersedes only that comment. No computed result, generator, coefficient,
theorem, acceptance tolerance or PRE report conclusion changes.

For any fixed edge e and any integer spin S, the two creation operators
j_(e,+),S and j_(e,-),S have orthogonal output ranges: their newborn charges
at the two endpoints are the distinct patterns (+,-) and (-,+). Multiplying
by physical spin projectors or link weights does not change that matter
orthogonality. Therefore

    j_(e,+),S^dagger j_(e,-),S=0,
    B_(e,+),S^dagger B_(e,-),S=0,

where B_(e,sigma),S=-P j_(e,sigma),S Pi1 T_S P. It follows exactly that

    (B_(e,+),S+B_(e,-),S)^dagger(B_(e,+),S+B_(e,-),S)
       =B_(e,+),S^dagger B_(e,+),S+B_(e,-),S^dagger B_(e,-),S.

Summing edges proves equality of resolved and coherent total losses at every
finite S, as well as in the rotor limit. Their no-event generators therefore
also agree exactly. Their recycling maps and operational mark outputs still
can differ: the coherent recycling term retains the off-diagonal output
operators B_+ rho B_-^dagger and its adjoint. Orthogonality makes their trace
zero, not the operators themselves.

The post-PRE independent comparison verifies every cross-Gram matrix has
zero structural nonzero entries on the complete finite-spin P spaces for
S=1,2,4,8. Total-loss differences are at most 3.6e-15 from floating summation
order. The proof above is general and does not extrapolate from those spins.
The exact rotor identity R=4 Q_adj was also reconstructed on all 36 P charge
words for both instruments, without opening the excluded second-event packet.
Evidence is in comparison_check.py, COMPARISON_RESULTS.json and the actual
comparison run streams/receipt.

The parent coordinator raised this comment as a post-PRE concern; the general
orthogonality argument and new checks were completed after candidate access.
They are not relabelled as part of the frozen PRE reconstruction.
