import Init

structure MomentPoly where
  a : Nat
  b : Nat
  c : Nat
  d : Nat

def sew (p q : MomentPoly) : MomentPoly :=
  ⟨24*p.a*q.a + 6*(p.a*q.c + p.c*q.a) + p.c*q.c,
   6*p.b*q.b, 2*p.c*q.c, 24*p.d*q.d⟩

def equivalent (p q : MomentPoly) : Bool :=
  (p.d != 0) && (q.d != 0) && (p.a*q.d == q.a*p.d) &&
  (p.b*q.d == q.b*p.d) && (p.c*q.d == q.c*p.d)

def plaquette : MomentPoly := ⟨15, 8, 4, 16⟩
def pairOfPlaquettes := sew plaquette plaquette
def square := sew pairOfPlaquettes pairOfPlaquettes
def known : MomentPoly := ⟨1769471, 1728, 4, 1769472⟩

theorem square_ok : equivalent square known = true := by decide
theorem square_assoc_ok : equivalent (sew (sew pairOfPlaquettes plaquette) plaquette) known = true := by decide
theorem reject_b : equivalent square { known with b := 6912 } = false := by decide
theorem reject_d : equivalent square { known with d := 0 } = false := by decide

#print axioms square_ok
#print axioms square_assoc_ok
#print axioms reject_b
#print axioms reject_d
