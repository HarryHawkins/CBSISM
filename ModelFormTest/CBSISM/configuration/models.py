from django.db import models


# Create your models here.
class Endpoint(models.Model): 
    """An endpoint device, used for configuring new nodes"""
    node_name = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    port_number = models.CharField(max_length=200)
    HTTPS = 'S'
    HTTP = 'P'
    protocol_choices = (
        (HTTPS,'HTTPS'),
        (HTTP,'HTTP'),
    )
    protocol = models.CharField(max_length=2,
                                      choices=protocol_choices,
                                      default=HTTPS)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200) # this must be pw type in form/view
    UBUNTU = 'UB'
    CENTOS = 'CE'
    FEDORAIOT = 'FE'
    OS_CHOICES = (
        (UBUNTU, 'Ubuntu'),
        (CENTOS, 'CentOS'),
        (FEDORAIOT, 'Fedora IOT'),
    )
    operating_system = models.CharField(max_length=2,
                                      choices=OS_CHOICES,
                                      default=UBUNTU)
    location = models.CharField(max_length=200, default="NA")

    #these are metrics to monitor, this will have to be in a user friendly display
    #as there are a lot of choices... - taken list from nodeexpoter supported metrics list
    #Exposes ARP statistics from /proc/net/arp - Linux
    metric_arp = models.BooleanField(default=True)
    #Exposes bcache statistics from /sys/fs/bcache/. - Linux
    metric_bcache = models.BooleanField(default=True)
    #Exposes the number of configured and active slaves of Linux bonding interfaces.	Linux
    metric_bonding = models.BooleanField(default=True)
    #Exposes system boot time derived from the kern.boottime sysctl
    # Darwin, Dragonfly, FreeBSD, NetBSD, OpenBSD, Solaris
    metric_boottime	= models.BooleanField(default=True)
    #Shows conntrack statistics (does nothing if no /proc/sys/net/netfilter/ present).	Linux
    metric_conntrack = models.BooleanField(default=True)
    #Exposes CPU statistics	Darwin, Dragonfly, FreeBSD, Linux, Solaris
    metric_cpu = models.BooleanField(default=True)
    #Exposes CPU frequency statistics	Linux, Solaris
    metric_cpufreq = models.BooleanField(default=True)
    #Exposes disk I/O statistics.	Darwin, Linux, OpenBSD
    metric_diskstats = models.BooleanField(default=True)
    #Exposes error detection and correction statistics.	Linux
    metric_edac	= models.BooleanField(default=True)
    #Exposes available entropy.	Linux
    metric_entropy = models.BooleanField(default=True)
    #Exposes execution statistics.	Dragonfly, FreeBSD
    metric_exec	= models.BooleanField(default=True)
    #Exposes file descriptor statistics from /proc/sys/fs/file-nr.	Linux
    metric_filefd = models.BooleanField(default=True)
    #Exposes filesystem statistics, such as disk space used.
    # Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_filesystem = models.BooleanField(default=True)
    #Expose hardware monitoring and sensor data from /sys/class/hwmon/.	Linux
    metric_hwmon = models.BooleanField(default=True)
    #Exposes network statistics specific to InfiniBand and Intel OmniPath configurations.	Linux
    metric_infiniband = models.BooleanField(default=True)
    #Exposes IPVS status from /proc/net/ip_vs and stats from /proc/net/ip_vs_stats.	Linux
    metric_ipvs = models.BooleanField(default=True)
    #Exposes load average.	Darwin, Dragonfly, FreeBSD, Linux, NetBSD, OpenBSD, Solaris
    metric_loadavg = models.BooleanField(default=True)
    #Exposes statistics about devices in /proc/mdstat
    # (does nothing if no /proc/mdstat present).	Linux
    metric_mdadm = models.BooleanField(default=True)
    #Exposes memory statistics.	Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_meminfo = models.BooleanField(default=True)
    #Exposes network interface info from /sys/class/net/	Linux
    metric_netclass	= models.BooleanField(default=True)
    #Exposes network interface statistics such as bytes transferred.
    # Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_netdev = models.BooleanField(default=True)
    #Exposes network statistics from /proc/net/netstat.
    # This is the same information as netstat -s.	Linux
    metric_netstat = models.BooleanField(default=True)
    #Exposes NFS client statistics from /proc/net/rpc/nfs. 
    # This is the same information as nfsstat -c.	Linux
    metric_nfs = models.BooleanField(default=True)
    #Exposes NFS kernel server statistics from /proc/net/rpc/nfsd.
    # This is the same information as nfsstat -s.	Linux
    metric_nfsd	= models.BooleanField(default=True)
    #Exposes pressure stall statistics from /proc/pressure/.
    # Linux (kernel 4.20+ and/or CONFIG_PSI)
    metric_pressure	= models.BooleanField(default=True)
    #Exposes various statistics from /sys/class/powercap.	Linux
    metric_rapl	= models.BooleanField(default=True)
    #Exposes task scheduler statistics from /proc/schedstat.	Linux
    metric_schedstat = models.BooleanField(default=True)
    #Exposes various statistics from /proc/net/sockstat.	linux
    metric_sockstat	= models.BooleanField(default=True)
    #Exposes statistics from /proc/net/softnet_stat.	Linux
    metric_softnet = models.BooleanField(default=True)
    #Exposes various statistics from /proc/stat.
    # This includes boot time, forks and interrupts.	Linux
    metric_stat	= models.BooleanField(default=True)
    #Exposes statistics read from local disk.
    # The --collector.textfile.directory flag must be set.	any
    metric_textfile	= models.BooleanField(default=True)
    #Exposes thermal zone & cooling device statistics from /sys/class/thermal.	Linux
    metric_thermal_zone	= models.BooleanField(default=True)
    #Exposes the current system time.	any
    metric_time	= models.BooleanField(default=True)
    #Exposes selected adjtimex(2) system call stats.	Linux
    metric_timex = models.BooleanField(default=True)
    #Exposes UDP total lengths of the rx_queue and tx_queue from
    # /proc/net/udp and /proc/net/udp6.	Linux
    metric_udp_queues = models.BooleanField(default=True)
    #Exposes system information as provided by the uname system call.
    #Darwin, FreeBSD, Linux, OpenBSD
    metric_uname = models.BooleanField(default=True)
    #Exposes statistics from /proc/vmstat.	Linux
    metric_vmstat = models.BooleanField(default=True)
    #Exposes XFS runtime statistics.	Linux (kernel 4.4+)
    metric_xfs = models.BooleanField(default=True)
    #Exposes ZFS performance statistics.	Linux, Solaris
    metric_zfs = models.BooleanField(default=True)
