---
id: nxlvjm6hui0yaltptr19hok
title: Windows Customizations
desc: ''
updated: 1705271872054
created: 1703770067787
tags:
  - windows
  - registry
  - tweak
  - keyboard
  - kb
  - shortcut
  - hotkey
---

## Disable `Win+L`

Source:

* [How can I disable  the function (window key + L ) used to lock the window (answers.microsoft.com)](https://answers.microsoft.com/en-us/windows/forum/all/how-i-can-disable-the-function-window-key-l-used/fdb6696e-eb2f-4115-a79d-771b7e0bb496)

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System`

* create a new DWORD 32-bit value named `DisableLockWorkstation` and
* give it one of these values:
  * `1` Disable Lock Workstation
  * `0` Enable Lock Workstation

## Chane the display resolution for a Hyper-V VM

```powershell
set-vmvideo -vmname <your_vm_name> -horizontalresolution:1920  -verticalresolution:1080 -resolutiontype single
```

* This _should_ enhance the graphics performance

  ```powershell
  Set-VM -VMName <your_vm_name>  -EnhancedSessionTransportType HvSocket
  ```


## Windows Alt-Tab

### Get the old Alt-Tab dialog back

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
