# Define the input file path
$SubdomainsFile = "M:\misc\subdomains.txt"

# Read the file line by line and resolve each subdomain
Get-Content $SubdomainsFile | ForEach-Object {
    $Subdomain = $_.Trim() # Trim any extra spaces or newlines
    try {
        $IP = [System.Net.Dns]::GetHostAddresses($Subdomain).IPAddressToString | Select-Object -First 1
        if ($IP) {
            Write-Output "$Subdomain - $IP"
        } else {
            #Write-Output "$Subdomain - No IP Found"
        }
    } catch {
        #Write-Output "$Subdomain - Error Resolving"
    }
}
