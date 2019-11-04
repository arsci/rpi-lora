install: 
    cp lora.service /etc/systemd/system/lora.service && systemctl daemon-reload && systemctl enable lora && systemctl start lora && systemctl status lora

uninstall: 
	systemctl stop lora && systemctl disable lora && rm -rf /etc/systemd/system/lora.service && systemctl daemon-reload