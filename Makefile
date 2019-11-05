#### Main

install: 
	cd server/ && npm install
	pip3 install RPI.GPIO && pip3 install adafruit-blinka
	pip3 install adafruit-circuitpython-framebuf && pip3 install adafruit-circuitpython-rfm9x
	cp service/lora.service /etc/systemd/system/lora.service && systemctl daemon-reload && systemctl enable lora && systemctl start lora && systemctl status lora

update:
	systemctl stop lora && cp service/lora.service /etc/systemd/system/lora.service && systemctl daemon-reload && systemctl enable lora && systemctl start lora && systemctl status lora

uninstall: 
	systemctl stop lora && systemctl disable lora && rm -rf /etc/systemd/system/lora.service && systemctl daemon-reload

install.rec:
	pip3 install RPI.GPIO && pip3 install adafruit-blinka
	pip3 install adafruit-circuitpython-framebuf && pip3 install adafruit-circuitpython-rfm9x
	cp service/lora-rec.service /etc/systemd/system/lora-rec.service && systemctl daemon-reload && systemctl enable lora-rec && systemctl start lora-rec && systemctl status lora-rec

update.rec;
	systemctl stop lora-rec & cp service/lora-rec.service /etc/systemd/system/lora-rec.service && systemctl daemon-reload && systemctl enable lora-rec && systemctl start lora-rec && systemctl status lora-re

uninstall.rec:
	systemctl stop lora-rec && systemctl disable lora-rec && rm -rf /etc/systemd/system/lora-rec.service && systemctl daemon-reload