---
created: 2026-05-08
type: index
tags:
  - kb
  - windows
---

# Windows

## Windows Notes

<!-- markdownlint-disable MD033 -->
<details>
<summary>Windows Notes</summary>
```foam-query
filter: "#windows"
format: count
```
</details>
<!-- markdownlint-enable MD033 -->

```foam-query
filter: "#windows"
format: table
select:
  - x
  - title
  - type
  - tags
  - properties
  - properties.type
  - properties.created
  - backlink-count
  - outlink-count
sort: title ASC
```
