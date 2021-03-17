#!/bin/bash
#below only works for pi4
sudo curl -SL https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-armv7.tar.gz > node_exporter.tar.gz && sudo tar -xvf node_exporter.tar.gz -C /usr/local/bin/ --strip-components=1
node_exporter &
echo "[Unit]" >>/etc/systemd/system/nodeexporter.service
echo "Description=NodeExporter" >>/etc/systemd/system/nodeexporter.service
echo "[Service]" >>/etc/systemd/system/nodeexporter.service
echo "TimeoutStartSec=0" >>/etc/systemd/system/nodeexporter.service
echo "ExecStart=/usr/local/bin/node_exporter" >>/etc/systemd/system/nodeexporter.service
echo "[Install]" >>/etc/systemd/system/nodeexporter.service
echo "WantedBy=multi-user.target" >>/etc/systemd/system/nodeexporter.service
sudo systemctl daemon-reload
sudo systemctl enable nodeexporter 
sudo systemctl start nodeexporter 
echo "install-done"
exit 1