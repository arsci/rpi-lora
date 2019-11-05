#### Main

install: 
	cp lora.service /etc/systemd/system/lora.service && systemctl daemon-reload && systemctl enable lora && systemctl start lora && systemctl status lora

uninstall: 
	systemctl stop lora && systemctl disable lora && rm -rf /etc/systemd/system/lora.service && systemctl daemon-reload

install.receiver:
	cp lora-rec.service /etc/systemd/system/lora-rec.service && systemctl daemon-reload && systemctl enable lora-rec && systemctl start lora-rec && systemctl status lora-rec

uninstall.receiver:
	systemctl stop lora-rec && systemctl disable lora-rec && rm -rf /etc/systemd/system/lora-rec.service && systemctl daemon-reload