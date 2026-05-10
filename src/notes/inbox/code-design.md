---
created: 2026-05-07
id: 3e35833a-d153-4e12-857e-8d96ed7fa79c
tags:
  - bug
  - kb
  - misc
---

# Code Design

- [Functional Core, Imperative Shell (destroyallsoftware.com)](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
- [Robert C Martin - Functional Programming; What? Why? When? (youtube.com)](https://www.youtube.com/watch?v=7Zlp9rKHGD4)
- [Moving IO to the edges of your app: Functional Core, Imperative Shell - Scott Wlaschin (youtube.com)](https://www.youtube.com/watch?v=P1vES9AgfC4)

- [ ] #BUG: enable mermaid

```mermaid
journey
    title Functional Core, Imperative Shell
    section Side Effects (Imperative Shell)
    I/O: 3: Developer
    Validation: 3: Developer
    section Pure (Functional Core)
    Business Logic: 4: Developer
    section Side Effects (Imperative Shell)
    Validation: 3: Developer
    I/O: 3: Developer
```
