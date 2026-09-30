# Derivation checkpoint 1 — exact removal and capacity

Author derivation, not independent review. No computation has run yet.

Let B be the physical graph-edge set (9V edges), H_N the fixed-N physical
Hamiltonian, K its actual N=2 restriction to graph edges, and η an (N−2)
occupation set. Define (T_N ψ)_η(e)=ψ(η union e) if e is disjoint fromη,
zero otherwise. The map has no chosen matching. It repeats an occupation
amplitude once for every occupied graph edge. Thus T†T=P_edges exactly.
Every S/W annihilation square acts by an actual linear combination of B_e;
resolving its output η proves exactly

 H_N = μ D_N + T_N† (direct_sum_η K) T_N.

The K here includes all 9 physical bond types/shared plane centers, not only
five projected modes. In Fourier form its axial block has two τℓ bands
and one2μ band. Each plane has one2μ band and one
 μ(1−coski coskj)+τℓ(1+coski coskj) band. Its kernel consists of the five
normalized uniform pair waves.

The diagonal graph identity is D=N−2P_edges+V3/μ. Together with checked
V3<=24μ Egrad and H>=a Egrad this gives the operator bounds

 N/2−H/(2μ) <= T†T <= N/2+12H/a.

On the H_N spectral subspace H<=εN, ε<μ, A=sqrt(2/N)T is within O(ε/a)
of an actual isometry by its polar normalization. Explicitly
(1−ε/μ)I <= A†A <= (1+24ε/a)I and
||A−U||<=max(1−sqrt(1−ε/μ),sqrt(1+24ε/a)−1)<=12ε/a.
The residual occupation space stays present. Iterating O(N) such estimates
is NOT a proved many-boson embedding and can accumulate an extensive error.

For each background η, E_η restricts to edges intersectingη, so E_η f_η=0.
Let P commute with K, let Q=1−P have a positive spectral gap, p=P f,q=Q f.
Define G=Q(QKQ)^{-1}Q and M_η=E_η G E_η†. For λ>0, completion of squares
in q proves the exact lower bound

 <f,Kf> >= <p,Kp> + (E_η p)† (λ^{-1}I+M_η)^{-1}(E_η p).

Indeed the RHS second term is the minimum of <q,Kq>+
λ||E_η p+E_η q||² over q inQ; the actual q has zero penalty.
Retain any fraction θ of qKq by multiplying that capacity term by1−θ.
This has no global Q_iso(H−E_N) denominator and no background-energy shift.
For P=kerK the p kinetic term vanishes and G=K^+; the finiteλ formula
avoids any pin-rank/domain issue. The λ→infinity pseudoinverse limit may be
used only on its feasible range, which the actual f satisfies.

If η has disconnected occupied-graph componentsη_i, their forbidden-edge
sets are disjoint: a common forbidden edge would connect the components.
Write D_block=diag_i(λ^{-1}I+M_ii), E_off=M−diag_i M_ii and
κ=||D_block^{-1/2} E_off D_block^{-1/2}||. Positivity gives
(λ^{-1}I+M)<= (1+κ) D_block, hence inverse>=D_block^{-1}/(1+κ).
Therefore the exact capacity is at least (1+κ)^{-1} times the sum of its
component capacities. This is an actual controlled background-relative
comparison, valid at every finiteN,V, with its explicit κ. It is useful
only where κ is small; no ground-state estimate ofκ is yet proved.
For isolated dimer backgrounds each block has35 incident physical edges.
No identification of these fixed-background capacities with full T0 is made.

A distinct exact matching representation maps |S> to the normalized sum
of all perfect matchings of its induced graph, with normalization sqrt(m(S)).
For a graph edge e, ordinary dimer annihilation on that vector has coefficient
sqrt(m(S minus e)/m(S)); physical b_e has coefficient1 when its residual
configuration has a matching. A long even induced axial rectangle cycle has
m=2 and removal of an edge leaves m=1. Cutting two distant vertices and
adding a remote isolated pair restoresN but makes m=1 with a chosen local
matched edge. Thus no bounded-neighborhood normalization rule for that
specific canonical matching representation is exact on all configurations.
This does not exclude another representation or a dilute ground-state theorem.

Next: literal K/whole-H identity, finiteλ pin capacity and block comparison
controls; precise low-energy reset construction testing what defect estimates
alone allow; attempt to bound off-block κ or identify its real missing input.
