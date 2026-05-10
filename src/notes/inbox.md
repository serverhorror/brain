---
type: inbox
---

# Inbox

## Interesting Texts

This first one is a set of rules that have served me well.
They came to live in various discussions with colleagues.
Not much has changed, but they served well for ~15 years.

--

- [ ] [zk is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki](https://github.com/zk-org/zk)
- [ ] Link Coding tools / frameworks
  - [ ] [</>htmx](https://htmx.org/attributes/hx-trigger/)
  - [x] [[kb/go/note.foam.md]] with [[kb/go/managing-go-installations.foam.md]]
  - [ ] gRPC
    - [ ] [gRPC](https://grpc.io/)
    - [ ] [connectRPC](https://connectrpc.com/)

## Reading / Articles

- [ ] [[misc/secure-systems.foam.md]]
- [ ] [[article.software-development-continuous-production.rst]]
- [x] [[misc/if-wasm-existed.foam.md]]
- [ ] Cloud: [[kb/gcp/note.foam.md]]
- [[misc/rules.foam.md]]
- [x] [[misc/as-a-software-developer.foam.md]]
- [x] [[misc/secrets-in-system-engineering.foam.md]]
- [x] [[misc/is-a-software-engineer-an-engineer.foam.md]]
- [x] [Programming Sucks (stilldrinking.org)](https://www.stilldrinking.org/programming-sucks)
- [x] [Minimize Code, Maximize Data (database-programmer.blogspot.com](https://database-programmer.blogspot.com/2008/05/minimize-code-maximize-data.html)

This is a collection of interesting texts that I have come across.
They are mostly copy/pasted from the original source.

- [ ] #TODO: [GitHub - gamontal/awesome-katas: A curated list of code katas](https://github.com/gamontal/awesome-katas)
- [ ] [lsp-pyright (github.com)](https://github.com/emacs-lsp/lsp-pyright)
- [ ] [Pyright (microsoft.github.io)](https://microsoft.github.io/pyright)

<!-- markdownlint-disable MD033-->
<details>
<summary>TODOs, FIXMEs, and BUGs</summary>

## TODOs

```foam-query
filter:
  or:
   - tag: "#todo"
   - tag: "#TODO"
   - tag: "#fixme"
   - tag: "#FIXME"
   - tag: "#bug"
   - tag: "#BUG"
format: table
select:
  - title
  - tags
  - backlink-count
  - outlink-count
sort: title ASC
```

</details>
<!-- markdownlint-enable MD033-->
