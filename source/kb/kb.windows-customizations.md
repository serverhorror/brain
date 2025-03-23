# Windows Customizations

## Disable `Win+L`

Source:

- [How can I disable the function (window key + L )
  used to lock the window
  (answers.microsoft.com)](https://answers.microsoft.com/en-us/windows/forum/all/how-i-can-disable-the-function-window-key-l-used/fdb6696e-eb2f-4115-a79d-771b7e0bb496)

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System`

- create a new DWORD 32-bit value
  named `DisableLockWorkstation`
- give it one of these values:
  - `1` Disable Lock Workstation
  - `0` Enable Lock Workstation

## Windows Alt-Tab

### Get the old Alt-Tab dialog back

1. Open Registry Editor.
1. Go to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer`.
1. Create a DWORD value named `AltTabSettings`.
1. Set its value data to `1`.
1. Restart Windows Explorer or sign out and sign in again to apply the change.

   ```batch
   taskkill /f /im explorer.exe
   start explorer.exe
   ```

### Alternative via registry file

1. Save the following as a `.reg` file.

   .. todo:: FIXME find a pygments lexer for `reg` files

   ```text
   Windows Registry Editor Version 5.00

   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer]
   "AltTabSettings"=dword:00000001
   ```

1. Double-click the file to apply the change.

1. Restart Windows Explorer or sign out and sign in again to apply the change.

   ```batch
   taskkill /f /im explorer.exe
   start explorer.exe
   ```
