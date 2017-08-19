function Get-TTTask {
    param(
        [Parameter(Mandatory=$True)]
        [string]$Api,
        [Parameter(Mandatory=$True)]
        [string]$Id        
    )

    $url = "{0}/task/{1}" -f $Api, $Id
    $response = Invoke-RestMethod -Method Get -Uri $url
    $response
}

function Add-TTTask {
    param(
        [Parameter(Mandatory=$True)]
        [string]$Api,
        [Parameter(Mandatory=$True)]
        [string]$Id,
        [Parameter(Mandatory=$True)]        
        [string]$Text,
        [DateTime]$Created,
        [DateTime]$Completed        
    )    

    $p = @{
        "id" = $Id;
        "text" = $Text;
    }

    # Date conversions
    $ref = Get-Date -Date "01/01/1970"    
    if ($Created) {
        $unix_Created = (New-TimeSpan -Start $ref -End $Created).TotalSeconds
        $p["createdAt"] = $unix_Created
    }
    if ($Completed) {
        $unix_Completed = (New-TimeSpan -Start $ref -End $Completed).TotalSeconds
        $p['completedAt'] = $unix_Completed
    }
    $p["completed"] = $Completed -ne $null
    
    # Convert to json and make request
    $json = ConvertTo-Json $p
    $url = "{0}/task" -f $Api
    $response = Invoke-RestMethod -Method Post -Uri $url -Body $json -ContentType "application/json"
    $response
}

function Remove-TTTask {
    param(
        [Parameter(Mandatory=$True)]
        [string]$Api,
        [Parameter(Mandatory=$True)]
        [string]$Id
    )
        $url = "{0}/task/{1}" -f $Api, $Id
        $response = Invoke-RestMethod -Method Delete -Uri $url
        $response    
}

function Test-Api-Methods {
    # API URL
    $api = "http://192.168.1.86:5000/api"

    $id = '4d3b70d5-5666-4ea8-9ac0-63ccea70fe0c'    
    # Test adding with dates
    $add_r = `
        Add-TTTask -Api $api `
            -Id $id `
            -Text 'Do do do' `
            -Created (Get-Date) `
            -Completed (Get-Date)
    
    $id2 = '4d3b70d5-5666-4ea8-9ac0-63ccea70fe0d'    
    # Test adding without dates
    $add_r2 = `
        Add-TTTask -Api $api `
            -Id $id2 `
            -Text 'Do do do'
    
    # Test removal
    $remove_r = Remove-TTTask -Api $api -Id $id
    $get_r = Get-TTTask -Api $api -Id $id
    
    $add_r
    $add_r2
    $get_r
    $remove_r
}