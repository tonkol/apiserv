function Get-Task {
    param(
        [string]$apiUrl,
        [string]$Id        
    )

    $url = "{0}/task/{1}" -f $apiUrl, $Id
    $response = Invoke-RestMethod -Method Get -Uri $url
    $response
}

function Add-Task {
    param(
        [string]$apiUrl,
        [string]$Id,        
        [string]$Text,
        [DateTime]$Created,
        [DateTime]$Completed,
        [bool]$IsCompleted
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
    $url = "{0}/task" -f $apiUrl
    $response = Invoke-RestMethod -Method Post -Uri $url -Body $json -ContentType "application/json"
    $response
}

function Remove-Task {
    param(
        [string]$apiUrl,
        [string]$Id
    )
        $url = "{0}/task/{1}" -f $apiUrl, $Id
        $response = Invoke-RestMethod -Method Delete -Uri $url
        $response    
}

function test-api {
    $api = "http://192.168.1.86:5000/api"

    $id = '4d3b70d5-5666-4ea8-9ac0-63ccea70fe0c'
    $add_r = `
        Add-Task -ApiUrl $api `
            -Id $id `
            -Text 'Do do do' `
            -Created (Get-Date) `
            -Completed (Get-Date)
    
    $id2 = '4d3b70d5-5666-4ea8-9ac0-63ccea70fe0d'    
    $add_r2 = `
        Add-Task -ApiUrl $api `
            -Id $id2 `
            -Text 'Do do do'
    
    $remove_r = Remove-Task -ApiUrl $api -Id $id

    $get_r = Get-Task -ApiUrl $api -Id $id
    
    $add_r
    $add_r2
    $get_r
    $remove_r
}




