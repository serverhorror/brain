---
id: nxlvjm6hui0yaltptr19hok
title: Windows Alt Tab
desc: ''
updated: 1703770452905
created: 1703770067787
---

## Get the old Alt-Tab dialog back

1. Open Registry Editor.
2. Go to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer`.
3. Create a DWORD value named `AltTabSettings`.
4. Set its value data to `1`.
5. Restart Windows Explorer or sign out and sign in again to apply the change.

   ```batch
   taskkill /f /im explorer.exe
   start explorer.exe
   ```

### Alternative via registry file

1. Save the following as a `.reg` file.

   ```reg
   Windows Registry Editor Version 5.00
  
   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer]
   "AltTabSettings"=dword:00000001
   ```

2. Double-click the file to apply the change.

3. Restart Windows Explorer or sign out and sign in again to apply the change.

   ```batch
   taskkill /f /im explorer.exe
   start explorer.exe
   ```
