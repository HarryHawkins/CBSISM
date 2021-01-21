CREATE TABLE "users" (
  "user_id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "username" varchar,
  "privilege" varchar
);

CREATE TABLE "node" (
  "node_id" SERIAL PRIMARY KEY,
  "device_name" varchar,
  "ip_address" varchar,
  "port_number" int,
  "protocol" varchar,
  "username" varchar,
  "password" varchar, 
  "location" varchar,
  "operating_system" varchar,
  "enabled_metrics_id" int UNIQUE
);

CREATE TABLE "users_nodes" (
  "user_nodes_id" SERIAL PRIMARY KEY,
  "user_id" int UNIQUE,
  "node_id" int UNIQUE
);

CREATE TABLE "enabled_metrics" (
  "enabled_metrics_id" SERIAL PRIMARY KEY,
  "arp" int,
  "bcache" int,
  "bonding" int,
  "boottime" int,
  "conntrack" int,
  "cpu" int,
  "cpufreq" int,
  "diskstats" int,
  "edac" int,
  "entropy" int,
  "exec" int,
  "filefd" int,
  "filesystem" int,
  "hwmon" int,
  "infiniband" int,
  "ipvs" int,
  "loadavg" int,
  "mdadm" int,
  "meminfo" int,
  "netclass" int,
  "netdev" int,
  "netstat" int,
  "nfs" int,
  "nfsd" int,
  "pressure" int,
  "rapl" int,
  "schedstat" int,
  "sockstat" int,
  "softnet" int,
  "stat" int,
  "textfile" int,
  "thermal_zone" int,
  "time" int,
  "timex" int,
  "udp_queues" int,
  "uname" int,
  "vmstat" int,
  "xfs" int,
  "zfs" int
);

CREATE TABLE "node_metrics_data" (
  "node_id" int PRIMARY KEY,
  "timestamp" timestamp,
  "arp" varchar,
  "bcache" varchar,
  "bonding" varchar,
  "boottime" varchar,
  "conntrack" varchar,
  "cpu" varchar,
  "cpufreq" varchar,
  "diskstats" varchar,
  "edac" varchar,
  "entropy" varchar,
  "exec" varchar,
  "filefd" varchar,
  "filesystem" varchar,
  "hwmon" varchar,
  "infiniband" varchar,
  "ipvs" varchar,
  "loadavg" varchar,
  "mdadm" varchar,
  "meminfo" varchar,
  "netclass" varchar,
  "netdev" varchar,
  "netstat" varchar,
  "nfs" varchar,
  "nfsd" varchar,
  "pressure" varchar,
  "rapl" varchar,
  "schedstat" varchar,
  "sockstat" varchar,
  "softnet" varchar,
  "stat" varchar,
  "textfile" varchar,
  "thermal_zone" varchar,
  "time" varchar,
  "timex" varchar,
  "udp_queues" varchar,
  "uname" varchar,
  "vmstat" varchar,
  "xfs" varchar,
  "zfs" varchar
);

ALTER TABLE "enabled_metrics" ADD FOREIGN KEY ("enabled_metrics_id") REFERENCES "node" ("enabled_metrics_id");

ALTER TABLE "node_metrics_data" ADD FOREIGN KEY ("node_id") REFERENCES "node" ("node_id");

ALTER TABLE "users_nodes" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "node" ADD FOREIGN KEY ("node_id") REFERENCES "users_nodes" ("node_id");
