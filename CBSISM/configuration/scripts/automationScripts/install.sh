#!/bin/bash
sudo curl -SL https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-armv7.tar.gz > node_exporter.tar.gz && sudo tar -xvf node_exporter.tar.gz -C /usr/local/bin/ --strip-components=1
node_exporter &
echo "[Unit] \n Description=NodeExporter \n[Service]\nTimeoutStartSec=0\nExecStart=/usr/local/bin/node_exporter\n[Install]\nWantedBy=multi-user.target" >>/etc/systemd/system/nodeexporter.service
sudo systemctl daemon-reload
&& sudo systemctl enable nodeexporter 
&& sudo systemctl start node-exporter 
curl localhost:9100/metrics | less