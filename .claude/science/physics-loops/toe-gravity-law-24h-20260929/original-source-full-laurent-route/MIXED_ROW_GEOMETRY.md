# Complete reverse-row geometry for protected opposite polarities

Separate exact necessary-condition result on the original H2, after the literal shared-row example. Work at L>=12 so radius-four geometry has no periodic alias. Keep the protected P_+ and P_- classes from PROTECTED_POLARITY_PROOF.md. This does not assert either class is invariant or replace the actual configuration graph.

Fix a physical output word beta with hole a. Suppose its H row has a nonzero entry from a protected plus input and from a protected minus input. Then each contributing input has a different hole from a. A same-hole protected column has only the six diagonal returns: its negative terms are blocked and all immediate B sites were occupied. Such an output retains its uniform star sign, whereas an opposite-sign hole-moving input would leave at least its shared B with the opposite sign. They therefore could not give the same beta.

Write h_+,h_- for the two input holes. Each is at graph distance two from a. The complete protected-column calculation shows that beta has charge sigma at EVERY A site in the radius-two A neighborhood of h_sigma other than a. At h_sigma this is the restored charge; at every other such A the charge is unchanged. Hence the two radius-two A neighborhoods can intersect only at a, since an occupied output A cannot be both signs.

On the cubic even-parity A sublattice this forces

    h_+=a+2e_i,    h_-=a-2e_i                            (1)

for one signed coordinate axis. Here is the full geometric reason. Their distance is even and at most four. If it is zero or two, their neighborhoods contain a second common A site (in particular their centers when distance two). If it is four, the common A sites include all length-two midpoints of a shortest nearest-neighbor path between them. A displacement of l1 length four that uses more than one coordinate has at least two distinct such midpoints. Only a displacement of four along one axis has a unique midpoint. That midpoint must be a. No wrap changes these counts at L>=12.

The axial pair in (1) has a unique shared B site with a on each side. Thus for this fixed beta there is at most ONE protected predecessor of each sign: reverse that actual axial charge/field word. If there were an additional predecessor of either sign, pairing it with the known opposite predecessor would force the same axial center and the same inverse fields. The coefficients are +1 in the physical field basis, or their genuine unit Laurent monomials in a chosen Gauss phase section.

Moreover beta has a full B star. Every B neighbor of a lies at distance at most three from either contributing h, where all B sites were occupied; protected hole moves preserve the entire B pattern. Its B at a+e_i is plus and at a-e_i is minus. Therefore beta is G-dark but has a MIXED full star and lies outside P_+ union P_-.

Consequently any actual eigenvector confined to P_+ union P_- must obey on every such row the exact two-term relation

    t_+(theta) psi_(alpha_+)(theta)
      +t_-(theta) psi_(alpha_-)(theta)=0,                 (2)

with the two actual axial inverse configurations and physical phases. In the glued field words of MIXED_POLARITY_ROW.md both coefficients are one. No spectral term occurs on this row, because the eigenvector's output component there is zero. This is a necessary relation, not an existence theorem for a consistent solution over all rows.

Rows receiving only one polarity can still contain several same-polarity predecessors. Their remaining constraints and the compatibility of (2) across different charge/mask configurations are unresolved. In particular, replacing these relations by an independently weighted graph, or by an edge-orientation process that forgets shared A charges, would lose actual coefficients. A midpoint A charge can participate in more than one axial constraint, and the completed background changes across a polarity switch. No global acyclicity or unique-continuation claim is made.

The literal two-input construction already shows that (2) can cancel one complete mixed row while another actual row remains nonzero. No full dark Laurent module, positive-Haar failure or actual source weight has been produced.
