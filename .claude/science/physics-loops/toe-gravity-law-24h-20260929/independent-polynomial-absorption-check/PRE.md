# Independent polynomial-weight check: pre-comparison plan

2026-09-30. Focused independent check, not formal review or audit. Writes only this directory. No root polynomial-extension proof or code has been read; the extension was described as still being written. The existing FAST_ONE_HOLE_ABSORPTION.md proof has not yet been opened by this checker. The check starts from the explicitly supplied candidate hypotheses below, then will read that frozen proof at its declared sector before issuing a final scope judgment.

## Exposure, stated exactly

The root brief disclosed the following candidate formulas, which are claims to check, not expected truths:

- Rotor sector W=1 and global N_B<=9, actual H=H2 and original loss G; ||H||<=M=1092, 0<=G<=12, S(t)=exp[t(-i delta H-kappa G/2)] with ||S(t)||<=C0 exp(-gamma t).
- Q=1+sum_e |E_e|, bandwidth2 for H and diagonal G; h_r=5 delta M 2^r for nested Q commutators of the generator.
- P0=1, Pp(0)=0 for p>0, Pp'=C0 sum_(r=1)^p binom(p,r)h_r P_(p-r), and proposed closed form Pp=2^p Touchard_p(5C0 delta M t).
- R_p=sum_(r=0)^p binom(p,r)P_r and proposed weighted propagation C0 exp(-gamma t)R_p(t)||Q^p psi||.
- Actual stacked original jump J has bandwidth1 and norm<=sqrt(12); proposed weighted transfer norm3 sqrt(12)2^p.
- Proposed integrated output constant108 kappa 4^p C0² integral_0^infinity exp(-2gamma t)R_p(t)² dt.

The root also disclosed that its own earlier independent read/check covers FAST_ONE_HOLE_ABSORPTION.md SHA3950bd73aea13b20fac74585c639fb5903bde25cac1a7d2f9308ab771ce6371c and the dark-word argument. This is provenance, not a substitute for the actual proof. No author code is being imported. The checker's separate large-background fast-sector report is frozen and is not a premise of this check.

## Independent reconstruction and failure tests

1. Decompose the bounded actual operator by integer spectral differences of Q. Prove each diagonal-band operator has norm bounded by the original operator, then bound nested commutators without assuming absolute matrix row summability.
2. Work directly with Q^p S(t) and the graph norm ||Q^p psi||. Derive its Duhamel recursion, independently solve the formal generating function, and compare it with the disclosed recurrence/Touchard expression. Explicitly check p=0,1,2,3.
3. Prove D(Q^p) invariance by closing identities on the finite-field core and exponentiating the same bounded generator on the graph-norm space. Never replace the generator by one with deleted boundary transitions. Check the necessary dense core and graph-norm equivalence.
4. Treat actual marks as a direct-sum output map. Preserve coherent sign addition inside an edge and resolved marks where selected. Derive input/output spectral-band transfer and the integrated norm-squared estimate, including the meaning of the field moment and time convention.
5. Read the frozen low-global-excitation proof and the future root extension only after freezing the independent reconstruction. Check that no domain, normalization, volume, field-support or instrument hypothesis changed. A finite-global-sector result does not close the full microscopic source process.

Any small exact control will test rational polynomial coefficient identities rather than numerically pretending to prove an unbounded-domain statement. Initial budget<=30 CPU seconds and150 MB, one thread; no heavy job is planned. Deadline/STOP checked before work: original deadline2026-09-30T22:41:00.557005Z, no STOP present at06:08UTC. Cached scientific main remains30a9461ee19a49b99fa6628fe942f08e504e8903 and selected procedure7146fe17a76de41badcaca3c3c7cac6d11eb2a00. Primitive/source reads from the preceding tasks are reusable only at matching bytes and scope.
