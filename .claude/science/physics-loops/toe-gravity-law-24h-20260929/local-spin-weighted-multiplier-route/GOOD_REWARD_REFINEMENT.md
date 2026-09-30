# Candidate refinement: the field cost is supported in Pi

This is an analytic strengthening of REPORT2f757a42, not an independent check. It was derived after its first frozen proof, while its finite control was running. The weaker report remains unchanged.

On the physical spin box set V_S=P_S V P_S, so O_S=i(V_S*-V_S). Write D for the dark occupancy projection, B=I-D and P for the geometric sparse-dark projection, now restricted to that box. Spin losses have exactly the same kernel D: a vacant edge always retains at least its inward sign weight. The actual dark-compressed spin Hamiltonian preserves P. Indeed its allowed word geometries are a subset of the rotor geometries, the local B count is still preserved by every same-hole dark word, and no dark hole move can start in P. Delta_S is diagonal. No field-cut subprojection of P is asserted invariant.

The original selected bright output still has only one occupied B neighbor. Therefore its inverse row from ANY dark spin word has the same unique predecessor as for rotors; only its two-hop weight changes. Consequently

 V_S* H_S D = w_S P,

where w_S is the diagonal nonnegative selected-path weight, set to zero when the selected rotor output is outside the spin box. There is no other dark predecessor. In particular the dark-dark block of i[H_S,O_S] is2w_S P, supported in P. Its dark-bright block -D H_S D V_S*+V_S*B H_S B has range in P because P reduces D H_S D. Its bright-bright block is already supported in B. The G_S anticommutator with O_S only connects P and B, and G_S itself is supported in B. It follows exactly that

 L_S(T_S)=Pi_S L_S(T_S) Pi_S.

Apply the already proposed weighted inequality to Pi_S psi. Since Q_loc and Pi_S commute, its improved form is

 L_S(T_S)<=-Pi_S+(K_loc/C)Pi_S Q_loc^2 Pi_S.           (R1)

Thus equations7 and8 of REPORT remain valid with Q_loc Z_S and Q_loc y replaced respectively by Q_loc Pi_S Z_S and Q_loc Pi_S y. There is no dense-dark field residence term. This still does not bound the good-sector moving-hole field weight on the actual microscopic source. In particular a field-cut sparse projector need not reduce the full dynamics, and exact boundary-blocked selected paths are retained through w_S=0. The entire refinement needs focused independent checking with the base report before reuse.
