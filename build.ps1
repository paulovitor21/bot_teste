$exclude = @("venv", "bot_teste.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_teste.zip" -Force