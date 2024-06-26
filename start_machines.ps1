$machinename1 = 'Box1'
$machinename2 = 'Box2'
$machinename3 = 'Box3'
$machinename4 = 'Box4'

Start-Process "$env:windir\system32\mstsc.exe" -ArgumentList "/v:$machinename1"
Start-Process "$env:windir\system32\mstsc.exe" -ArgumentList "/v:$machinename2"
Start-Process "$env:windir\system32\mstsc.exe" -ArgumentList "/v:$machinename3"
Start-Process "$env:windir\system32\mstsc.exe" -ArgumentList "/v:$machinename4"