param(
  [string]$Artifact,
  [string]$User,
  [string]$Password,
  [string]$Host
)

$secure = ConvertTo-SecureString $Password -AsPlainText -Force
$cred = New-Object PSCredential ($User, $secure)

$session = New-PSSession -ComputerName $Host -Credential $cred
Copy-Item -Path $Artifact -Destination "C:\temp\conf_bundle.zip" -ToSession $session -Force

Invoke-Command -Session $session -ScriptBlock {
  Expand-Archive -Path "C:\temp\conf_bundle.zip" -DestinationPath "C:\Program Files\Splunk\etc\apps\automation_app" -Force
  & "C:\Program Files\Splunk\bin\splunk.exe" restart
}

Remove-PSSession $session
