The first forest checker was interrupted with SIGINT, exit 130, while
enumerating candidate three-edge graphs. The traceback ended at tree_paths,
the stack.extend line. A triangle plus an isolated vertex was not excluded
before path search; the search tracked only the preceding vertex and could
loop around the triangle forever. The frozen source and hash preserve this
attempt. Adding a visited set permits disconnected candidates to terminate
and be excluded. No scientific assertion had run and no tolerance changed.
