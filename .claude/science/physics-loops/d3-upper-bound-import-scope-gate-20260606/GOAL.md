# Goal

Package a narrow D3 upper-bound import-scope gate.

The target is not a framework-internal dimension-selection theorem. The target
is to make the current composition rule inspectable:

- lower runner support gives `{3,4,5}`;
- Bertrand upper-bound import gives `d <= 3`, hence intersection `{3}`;
- weaker atomic stability gives `d <= 4`, hence intersection `{3,4}`.

The deliverable is an exact-support branch-local gate that prevents later
review from silently treating atomic stability alone as a unique selector or
treating named imports as framework derivations.
