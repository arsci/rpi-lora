install: 
        cp lora.service /etc/systemd/system/lora.service && systemctl daemon-reload && systemctl enable lora && systemctl start lora && systemctl status lora