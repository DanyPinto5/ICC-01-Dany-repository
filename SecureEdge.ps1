Import-Module ActiveDirectory

$users = Import-Csv -Path "C:\Users\Dany~\Desktop\users.csv"
$users | ForEach-Object {

    $FirstName = $_.FirstName
    $LastName = $_.LastName
    $Username = $_.Username
    $Password = $_.Password
    $Department = $_.Department
    $Jobrole = $_.Jobrole

    $OU = "OU=$Department,DC=SecureEdgeInc,DC=local"

    If ($Department -eq $true){
    else New-ADOrganizationalUnit -Name $Department -Path "DC=SecureEdgeInc.DC=local"
    }
    
    New-ADOrganizationalUnit -Name $Department -Path "DC=SecureEdgeInc.Dc=Local"
        
    New-ADUser -SamAccountName $Username -UserPrincipalName "$Username@SecureEdgeInc.local" -Name "$FirstName $LastName" -GivenName "$FirstName" -Surname "$LastName" -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) -Department "$Department" -Title "$Jobrole" -Path "$OU" -Enabled $true -ChangePasswordLogon $true

    Write-Host "Created user: $FirstName $LastName $Username in OU: $Department $Jobrole"

    }

###########################################
#|      Script created by Dcman          |#
###########################################