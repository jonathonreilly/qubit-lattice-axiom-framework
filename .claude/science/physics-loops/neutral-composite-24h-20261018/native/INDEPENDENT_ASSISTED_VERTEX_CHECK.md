# Assisted hopping vertex: focused weight check

PASS, conditional on the separately checked canonical third-order nearest-neighbor block. This report checks its spectral-weight consequence, not the physical three-word/fold coefficient again.

Let Q_g=I-|g><g| in the vacuum background block. For the stated nearest x-hop,

    Q_g H_ji g = -(J lambda^3/4) Q_g E_edge g + O_R(J lambda^4).

Both the leading -Jlambda identity and the third-order identity are exactly removed by Q_g. Therefore the squared norm is

    J^2 lambda^6 Var_g(E_edge)/16 + O_R(J^2 lambda^7).

The factor 1/16 and power six are correct. The error should carry J^2, not J, when writing the squared vertex with dimensional J explicit. For a lower bound it is clearest to write “>= J^2 lambda^6 m^2/16 - C_R J^2 lambda^7”; a signed O term in an inequality is conventional but less explicit.

## Uniform positive coefficient

In the original logical-X configuration basis, E is diagonal and each P_p flips four variables. In the unique positive all-row/column-X-plus ground, the established amplitude-ratio inequality gives a(ps)/a(s)>=m pointwise. Summing a(s)a(ps) proves <P_p>>=m, with

    m=8/(sqrt(80^2+64)+80)=(sqrt(404)-20)/2
      approximately 0.04987562112.

Choose a plaquette having exactly one endpoint of the edge, so {P_p,E_edge}=0. Both are self-adjoint involutions. The two-component Pauli inequality gives <P_p>^2+<E_edge>^2<=1, hence Var(E_edge)>=m^2. Thus the coefficient lower bound m^2/16 is approximately 0.0001554736, independent of R within the geometry where the ratio estimate holds. This is a lower bound on the coefficient, not a uniform finite-lambda bound on the asymptotic remainder.

E_edge commutes with the row/column-X symmetry operators, so E_edge g remains in the all-plus block. Since that block has a unique ground, its centered part lies wholly in positive coefficient-energy spectral subspaces. This is the necessary qualification preventing a merely elastic ground-space rotation from being counted as excitation. A plaquette must actually anticommute with the edge; using a plaquette containing both endpoints would fail this step.

## Actual vacuum and gauge

At each fixed admissible even R, the native vacuum coefficient ground is isolated and unique in the relevant symmetry block. In the same symmetry-equivariant canonical reduction, the actual vacuum-block ground g_lambda converges to g with O_R(lambda) error, since its first nonconstant operator is lambda^4 K/128 and the next coefficient is higher order. Consequently Var_(g_lambda)(E_edge)=Var_g(E_edge)+O_R(lambda), which preserves the displayed lambda^6 leading weight and O_R(lambda^7) error.

The positive-energy assertion can equally be made relative to the unique actual vacuum-block ground, with its corresponding centered projector. It does not assert that the resulting particle-at-j/background-excited vector is an eigenstate, or an outgoing excitation, of the full heavy Hamiltonian.

The block H_ji is gauge dependent. The result has an operationally definite meaning only when the preparation of particle position i, the position-j projection and background-orthogonality readout are all transported by the same canonical SW/Kato identification used to obtain H_ji. An arbitrary intra-N2 unitary can redistribute this vertex among operators and states. Under simultaneous transport of preparation and readout the matrix element is unchanged, so there is no gauge-transfer obstruction to the stated matched-dressing claim. The formula does not establish the same leading coefficient for bare microscopic preparation/readout; their dressing corrections cannot simply be ignored when extracting a lambda^3 amplitude.

The controlled limit is fixed R followed by lambda tending to zero. The matching actual vacuum and heavy embeddings must use the same declared canonical convention through the relevant orders. No finite-time emission rate, decay width, on-shell transition probability, relaxed-heavy coupling, or universal matter coupling follows from this nonzero infinitesimal prepared-state vertex.
