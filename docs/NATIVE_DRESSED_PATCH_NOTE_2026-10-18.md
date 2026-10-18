# A large dressed feature from the native one-qubit Hamiltonian

Status: bounded-support. The native moving defect can alter its environment
without an added interaction. A controlled weak-coupling construction on a
four-layer slab gives an extended trial feature and the actual two-wall
band-bottom gap

    E2-Eg = 4J-4Jlambda+O(Jlambda^(5/2)).

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DRESSED_PATCH_PROOF.md)
derives the second-order term from physical spin-flip paths. It is
-(Tx-Ty)^2/8, and an operator inequality controls it without an order-lambda²
loss. A patch of altered background with side proportional to lambda^-3/4
then yields the upper energy bound on growing transverse boxes. This
constructs a large dressing family; it does not select an exact radius.

The same estimate forces low-energy defects to encounter nearly flat local
plaquettes: the dressed particle-conditioned bad-flux weight is
O(lambda^(3/2)). This is a derived environment response, rather than an
assigned profile or assumed equality with the vacuum background.

[Replay](../scripts/native_dressed_patch.py) checks exact native second-order
paths, the noncommuting matrix inequality, the flux bound and asymptotic
scaling controls. The proof supplies the uniform estimates; finite numerical
controls are exposed model development and do not certify a laboratory
coupling range. The supplied Hamiltonian and slab geometry remain premises.
Fermionic statistics, three-dimensional motion, the relaxed feature's scalar
response and universal gravitational coupling remain open.
