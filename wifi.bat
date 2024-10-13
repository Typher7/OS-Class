for /f "tokens=2 delims=:" %%a in ('netsh wlan show interfaces ^| findstr "Profile"') do set ProfileName=%%a
netsh wlan show profile %ProfileName% key=clear
