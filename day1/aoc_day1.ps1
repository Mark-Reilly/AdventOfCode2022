$InputFile = Get-Content C:\Users\markreil\Desktop\aoc\day1\aoc_day1.txt

$Scoreboard = @()
[int]$ThisElfsTotal = 0

foreach ($Row in $InputFile)
{
    [int]$Row = $Row
    if ($Row -ne 0)
    {
        [int]$ThisElfsTotal += $Row
    }
    else
    {
        $Scoreboard += $ThisElfsTotal
        $ThisElfsTotal = 0
    }
}

$Scoreboard = $Scoreboard | Sort-Object -Descending

Write-Output "`n`nTop: $($Scoreboard[0])"
Write-Output "Top 3 Total: $($Scoreboard[0] + $Scoreboard[1] + $Scoreboard[3])"