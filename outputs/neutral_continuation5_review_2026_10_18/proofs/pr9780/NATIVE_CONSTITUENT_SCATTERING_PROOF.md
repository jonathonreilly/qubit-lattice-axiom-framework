<!-- Original PR9780 source SHA256 671acf17ba5d58bf3f3963ef3b631efebf0ec263020acb41996600813cb59142. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Root native two-flip scattering from same N4 Hamiltonian

Conditional coefficient theorem, not full-H scattering or two-composite scattering. Complete N4 host is inversion-even punctured square lattice with hops -2,-2b and two native attached rays. Q=(0,2acos b,0), c=1; b approaches bc from below, bound gap delta→0.

Use oriented full relative host for scattering amplitude normalization; physical space is inversion-even. Free dispersion e(k)=-4cos kx-4b cos ky, edge Eh=-4(1+b). Free retarded g_r(z)=integral exp(ikr)/(z-e(k)) d²k/(2pi)². Let g=g0, D=(gx-g,gy-g). Root states |x>=(|ex>+|-ex>)/sqrt2, similarlyy. Punctured cavity G=Gedge-2DD^T/g+o(1) near edge. More exactly its finite part M(z)=G(z)+2D(z)D(z)^T/g(z), with M→Gedge and M-Medge=O(w log w), w=z-Eh. Rays selfenergy sigma(z)=(z-sqrt(z²-16))/2, sqrt chosen ~z at infinity; for z<-4 this equals (z+sqrt(z²-16))/2.

Set A(z)=sigma(z)^-1 I-M(z). Cavity dressed T=(sigma^-1 I-G)^-1=(A+2DD^T/g)^-1. The hard-core missing-origin scattering contribution relative to full free lattice is -1/g. Incoming punctured root amplitude h(k,z)=sqrt2(cos kx-gx/g,cos ky-gy/g). Total oriented plane-wave amplitude
 t(k',k;z)=-1/g+h(k',z)^T T(z) h(k,z).
No conjugation of analytic Greenfunctions in this retarded formula; real k cos, reciprocity. On-shell h=-sqrt2D/g+O(|k|²).

Define q(z)=2D^T A^-1 D. Then exact algebra for the leading h term gives -1/g+q/[g²(1+q/g)]=-1/(g+q). For b<bc sufficientlynearbc A(edge) invertible with ||A^-1||=O(log1/delta), since its simple small eigenvalue is O(bc-b). The pole condition for exact bound gap is g(Eh-delta)+q(Eh-delta)=0. On w=s delta+i0 with fixed s>0, q(z)-q(Eh-delta)=O(delta log^p(1/delta))→0 for a fixed finite p; follows parameter expansions of M,D,sigma and inverse identity. The root h remainder gives o(1) after multiplication by T and 1/g, using T=O(log²) in this scaling. Free Green difference is c(b)[log(s)-i pi]+o(1), c(b)=1/(8pi sqrt b).

Hence t(k',k;Eh+sdelta+i0)→ -1/{c(b)[log s-i pi]} uniformly for incoming/outgoing directions on their shrinking elliptical shells (k=O(sqrt(delta))). At s=1 amplitude -i/[pi c(b)]. Im t=-pi c(b)|t|² in the limit. This is oriented plane-wave T normalization with DOS c(b). Even-parity normalized-channel factors must be stated consistently; do not silently compare to physical crosssection without convention. It derives a logarithmic native two-flip collision amplitude, not postulates an attractive delta potential. Binding gap/momentum selection stillconditional. No empirical claim or two-composite lifetime.

For normalized inversion-even half-shell states the amplitude is t_even=2t and the density is c/2. Thus Im(t_even)=-pi(c/2)|t_even|². Both factors change together. The strict limiting coefficient is c(bc); the displayed c(b) form has the same o(1) accuracy.
