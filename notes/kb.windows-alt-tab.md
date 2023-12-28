---
id: nxlvjm6hui0yaltptr19hok
title: Windows Alt Tab
desc: ''
updated: 1703770088671
created: 1703770067787
---

## Get the old Alt-Tab dialog back

1. Open Registry Editor.
2. Go to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer`.
3. Create a DWORD value named `AltTabSettings`.
4. Set its value data to `1`.
5. Restart Windows Explorer or sign out and sign in again to apply the change.
