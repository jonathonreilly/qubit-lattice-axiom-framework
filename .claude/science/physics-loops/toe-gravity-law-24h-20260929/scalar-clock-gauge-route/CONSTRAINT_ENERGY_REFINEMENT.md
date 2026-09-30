# A positive continuum constraint energy in the same clock gauge

Root candidate refinement of WORKING_PROOF.md bff81bc6; unchecked. The
Hamiltonian, carrier, diagnostic and all finite control inputs are unchanged.
This supplies a distinct direct uniqueness proof for the constraint system,
and removes the additional constraint-only analytic time shortening. It does
not improve the metric evolution's analytic-time or smooth-data status.

Use q=sqrt(det g), fixed positive w=w0, N=q/w, s=aK and the exact
continuum C,J in(C2). Set

 E=q C,       u=E/w^2,
 A^ij=(det g/w^2)g^ij=N^2 g^ij.                           (E1)

These symbols are constraint fields, not physical energy density or
the trace-free initial tensor A(x) used in(C11). To avoid that latter
notational collision, call the matrix here A_clock when used in prose.

The actual metric velocity from H_clock has

 qdot/q=-a tr(g pi)/(2w)=-zeta.

Thus(C5) gives

 Edot=s q[g^ij J_i partial_j N+partial_j(N g^ij J_i)]
      =s w partial_j[(q^2/w^2)g^ij J_i].                  (E2)

The last equality follows by expanding both products: qN=q^2/w and
2partial_j log N=partial_j log(q^2/w^2). It is a continuum product
identity, not a discrete rewrite. Equation(C6) is Jdot_i=w partial_i u.
Since w is fixed in time, the complete constraint system is consequently

 udot=(s/w)partial_j(A_clock^ij J_i),
 Jdot_i=w partial_i u.                                  (E3)

Its positive quadratic functional on the real periodic continuum torus is

 F(t)=1/2 mean[w u^2+(s/w)J_i A_clock^ij J_j].             (E4)

The weights are positive for the supplied a,K,w and positive metric.
Differentiate and integrate the u term by parts:

 Fdot=mean[s u partial_j(A_clock^ij J_i)
            +s J_i A_clock^ij partial_j u
            +(s/(2w))J_i (A_clock^ij)dot J_j]
      =mean[(s/(2w))J_i (A_clock^ij)dot J_j].              (E5)

No spatial derivative of w is dropped: its factor cancels BEFORE the
integration by parts because the first equation in(E3) has coefficient
s/w and the u-energy weight is w. This is why the chosen weights matter.

On any compact time interval of a smooth positive-metric solution with
w bounded away from zero, the number

 k(t)=sup_x ||A_clock^(-1/2) (A_clock)dot A_clock^(-1/2)||

is finite and locally bounded. Hence |Fdot|<=k(t)F. Zero initial(C,J)
implies F(0)=0; Gronwall gives F=0 and therefore C=J=0 throughout that
interval. In particular the analytic solution constructed in proof(C8)-(C9)
has this property on all of its T1. No separate T_cons shortening is needed.
The former homogeneous-analytic uniqueness argument remains a valid weaker
proof; this refinement supplies a direct positive energy instead.

The integral of E/w is also constant by(E2), since its derivative is a
periodic divergence. It is exactly H_clock. This is a consistency check
of the canonical signs, not a positivity assertion for H_clock; its
constraint value is zero and its off-constraint density is indefinite.

The finite spectral/centered Hamiltonian retains the literal derivatives
and does not obey(E2)-(E5) exactly. The finite diagnostic bound(C10) still
comes from analytic sampling consistency and the ACTUAL finite canonical
gradient, now on T1. This positive continuum constraint energy supplies
neither exact finite closure nor a physical scalar or record-clock choice.
