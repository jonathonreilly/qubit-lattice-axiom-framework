The first local-law checker stopped during initial frame decoding with a SymPy
TypeError: its interval helper recognized p_plus and p_minus, but attempted a
Python Boolean conversion for the cross-tag expression 100 + p_minus. The
original checker and its actual stderr are preserved beside this note.

The corrected helper encloses every affine expression on the explicitly assumed
rectangle p_plus,p_minus in [1/5,4/5] using exact rational corners. It accepts
contained intervals, rejects disjoint intervals, and raises on unresolved
straddling intervals or unsupported expressions. This is a checker correction;
no probability, protocol, physical hypothesis, or tolerance was changed.

The second revision reached the rational endpoint fixtures, then failed at
p_plus=p_minus=0. The fixture's Python integer u=0 underwent Python division,
producing floating matrices; the deliberately exact trace-one recognizer
rejected trace 1.0. The second source and an actual minimal reproduction are
preserved here. Sympifying the fixture inputs before arithmetic restores exact
rational data. The recognizer and theorem are unchanged; no floating tolerance
is introduced.
