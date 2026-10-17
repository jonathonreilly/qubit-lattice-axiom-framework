# C14: the order-4 BKSF codes (open)

- The pair-test data under the bare action are -1 for all three C2 of D2. A one-state fermion cannot carry
  this: the quaternion class has no 1-dim representation with -1 -> -1. The group theory was checked
  independently (`../c8_rotation_action/independent_check/grouptheory/`, 22/22).
- `dressing.py`: for a class-representative ordering of an order-4 code, P_R(A^o_e) A^o_{Re} is not in the
  stabilizer group for any of its three C2. The bare rotation turns a bare hop into a hop times a
  flux-creating factor, so there is no fermion map of the form c -> a c in this convention.
- `d2conv.py`: none of the 12 orderings x 4096 corner-dressed flux conventions of this code is D2-invariant
  (D3 codes have 8 D3-invariant ones, 2 with clean hops).
- Reading: consistent with a symmetry-localization obstruction of the bare D2 action, but not decided. The
  alternative is a failure of lambda = theta*eta for these C2.
- Decisive next step (from the group-theory check): compute eta(R,S) for R != S directly, from an explicit
  fermion-operator map in a D2-symmetric convention if any exists in a larger class, or prove that none
  exists.
