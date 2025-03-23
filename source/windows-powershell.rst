.. _windows-powershell:

Windows PowerShell
==================

.. code-block:: powershell
   :linenos:

   # set an environment variable
   [Environment]::SetEnvironmentVariable('KEY', 'VALUE', [EnvironmentVariableTarget]::User)

.. code-block:: powershell
   :linenos:

   # get an environment variable
   [Environment]::GetEnvironmentVariable('KEY', [EnvironmentVariableTarget]::User)

.. code-block:: powershell
   :linenos:

   # delete an environment variable
   [Environment]::SetEnvironmentVariable('KEY', $null, [EnvironmentVariableTarget]::User)

.. code-block:: powershell
   :linenos:

   $newpwd = Read-Host "Enter the new password" -AsSecureString
   Set-ADAccountPassword jfrost -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True

.. code-block:: powershell
   :linenos:

   # Filter users by a certain field
   get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'"

.. code-block:: powershell
   :linenos:

   # Reset password for users in a certain field and force password reset
   get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADAccountPassword -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True

.. code-block:: powershell
   :linenos:

   # Force password reset for users in a certain field
   get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADuser -ChangePasswordAtLogon $True

Source:

- `Reset a user password with PowerShell (4sysops.com) <https://4sysops.com/archives/powershell-password-resets/>`_
- `What is PowerShell? (docs.microsoft.com) <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1>`_
