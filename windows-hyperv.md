# Windows - Hyper-V

A _Hyper_-what-now?

Big words!
It's a piece like VMWare, VirtualBox, Hyper-V — which is built into Windows.

- [hyper-v-on-windows](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)

## Install

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

Output:

```text
Path          :
Online        : True
RestartNeeded : False
```

## Change the display resolution for a Hyper-V VM

```powershell
set-vmvideo -vmname <your_vm_name> `
  -horizontalresolution:1920  `
  -verticalresolution:1080 `
  -resolutiontype single
```

- This _should_ enhance the graphics performance

  ```powershell
  Set-VM -VMName <your_vm_name>  -EnhancedSessionTransportType HvSocket
  ```
