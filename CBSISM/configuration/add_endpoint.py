from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .scripts import hello
class EndpointForm(forms.Form):
    """form for adding an endpoint device, used for configuring new nodes"""

    node_name = forms.CharField(max_length=200, label='Node name')
    ip_address = forms.GenericIPAddressField(label='IP Address')
    username = forms.CharField(max_length=200, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    UBUNTU = 'UB'
    CENTOS = 'CE'
    FEDORAIOT = 'FE'
    OS_CHOICES = (
        (UBUNTU, 'Ubuntu'),
        (CENTOS, 'CentOS'),
        (FEDORAIOT, 'Fedora IOT'),
    )
    operating_system = forms.CharField(label="IIOT Device Operating System", widget=forms.Select(choices=OS_CHOICES))
    #these are metrics to monitor, this will have to be in a user friendly display
    #as there are a lot of choices... - taken list from nodeexpoter supported metrics list
    #Exposes ARP statistics from /proc/net/arp - Linux
    metric_arp = forms.BooleanField(label="ARP statistics",required=False)
    #Exposes bcache statistics from /sys/fs/bcache/. - Linux
    metric_bcache = forms.BooleanField(label="bcache statistics",required=False)
    #Exposes the number of configured and active slaves of Linux bonding interfaces.	Linux
    metric_bonding = forms.BooleanField(label="Linux bonding interfaces statistics",required=False)
    #Exposes system boot time derived from the kern.boottime sysctl
    # Darwin, Dragonfly, FreeBSD, NetBSD, OpenBSD, Solaris
    metric_boottime	= forms.BooleanField(label="System boot time",required=False)
    #Shows conntrack statistics (does nothing if no /proc/sys/net/netfilter/ present).	Linux
    metric_conntrack = forms.BooleanField(label="conntrack statistics",required=False)
    #Exposes CPU statistics	Darwin, Dragonfly, FreeBSD, Linux, Solaris
    metric_cpu = forms.BooleanField(label="CPU statistics",required=False)
    #Exposes CPU frequency statistics	Linux, Solaris
    metric_cpufreq = forms.BooleanField(label="CPU frequency statistics",required=False)
    #Exposes disk I/O statistics.	Darwin, Linux, OpenBSD
    metric_diskstats = forms.BooleanField(label="Disk I/O statistics",required=False)
    #Exposes error detection and correction statistics.	Linux
    metric_edac	= forms.BooleanField(label="Error detection and correction statistics",required=False)
    #Exposes available entropy.	Linux
    metric_entropy = forms.BooleanField(label="Available entropy",required=False)
    #Exposes execution statistics.	Dragonfly, FreeBSD
    metric_exec	= forms.BooleanField(label="Execution statistics",required=False)
    #Exposes file descriptor statistics from /proc/sys/fs/file-nr.	Linux
    metric_filefd = forms.BooleanField(label="file descriptor statistics",required=False)
    #Exposes filesystem statistics, such as disk space used.
    # Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_filesystem = forms.BooleanField(label="filesystem statistics",required=False)
    #Expose hardware monitoring and sensor data from /sys/class/hwmon/.	Linux
    metric_hwmon = forms.BooleanField(label="hardware monitoring and sensor data",required=False)
    #Exposes network statistics specific to InfiniBand and Intel OmniPath configurations.	Linux
    metric_infiniband = forms.BooleanField(label="network statistics specific to InfiniBand"
    +" and Intel OmniPath configurations",required=False)
    #Exposes IPVS status from /proc/net/ip_vs and stats from /proc/net/ip_vs_stats.	Linux
    metric_ipvs = forms.BooleanField(label="IPVS status",required=False)
    #Exposes load average.	Darwin, Dragonfly, FreeBSD, Linux, NetBSD, OpenBSD, Solaris
    metric_loadavg = forms.BooleanField(label="load average",required=False)
    #Exposes statistics about devices in /proc/mdstat
    # (does nothing if no /proc/mdstat present).	Linux
    metric_mdadm = forms.BooleanField(label="statistics about devices in /proc/mdstat",required=False)
    #Exposes memory statistics.	Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_meminfo = forms.BooleanField(label="memory statistics",required=False)
    #Exposes network interface info from /sys/class/net/	Linux
    metric_netclass	= forms.BooleanField(label="network interface info",required=False)
    #Exposes network interface statistics such as bytes transferred.
    # Darwin, Dragonfly, FreeBSD, Linux, OpenBSD
    metric_netdev = forms.BooleanField(label="network interface statistics",required=False)
    #Exposes network statistics from /proc/net/netstat.
    # This is the same information as netstat -s.	Linux
    metric_netstat = forms.BooleanField(label="network statistics statistics",required=False)
    #Exposes NFS client statistics from /proc/net/rpc/nfs.
    # This is the same information as nfsstat -c.	Linux
    metric_nfs = forms.BooleanField(label="NFS client statistics",required=False)
    #Exposes NFS kernel server statistics from /proc/net/rpc/nfsd.
    # This is the same information as nfsstat -s.	Linux
    metric_nfsd	= forms.BooleanField(label=" NFS kernel server statistics",required=False)
    #Exposes pressure stall statistics from /proc/pressure/.
    # Linux (kernel 4.20+ and/or CONFIG_PSI)
    metric_pressure	= forms.BooleanField(label="pressure stall statistics from /proc/pressure/",required=False)
    #Exposes various statistics from /sys/class/powercap.	Linux
    metric_rapl	= forms.BooleanField(label="/sys/class/powercap statistics",required=False)
    #Exposes task scheduler statistics from /proc/schedstat.	Linux
    metric_schedstat = forms.BooleanField(label="task scheduler statistics",required=False)
    #Exposes various statistics from /proc/net/sockstat.	linux
    metric_sockstat	= forms.BooleanField(label="/proc/net/sockstat statistics",required=False)
    #Exposes statistics from /proc/net/softnet_stat.	Linux
    metric_softnet = forms.BooleanField(label="/proc/net/softnet_stat statistics",required=False)
    #Exposes various statistics from /proc/stat.
    # This includes boot time, forks and interrupts.	Linux
    metric_stat	= forms.BooleanField(label="/proc/stat statistics",required=False)
    #Exposes statistics read from local disk.
    # The --collector.textfile.directory flag must be set.	any
    metric_textfile	= forms.BooleanField(label="statistics read from local disk",required=False)
    #Exposes thermal zone & cooling device statistics from /sys/class/thermal.	Linux
    metric_thermal_zone	= forms.BooleanField(label="thermal zone & cooling device statistics",required=False)
    #Exposes the current system time.	any
    metric_time	= forms.BooleanField(label="current system time",required=False)
    #Exposes selected adjtimex(2) system call stats.	Linux
    metric_timex = forms.BooleanField(label="adjtimex(2) system call stats statistics",required=False)
    #Exposes UDP total lengths of the rx_queue and tx_queue from
    # /proc/net/udp and /proc/net/udp6.	Linux
    metric_udp_queues = forms.BooleanField(label="UDP total lengths of the rx_queue and tx_queue",required=False)
    #Exposes system information as provided by the uname system call.
    #Darwin, FreeBSD, Linux, OpenBSD
    metric_uname = forms.BooleanField(label="system information as provided by the uname system call",required=False)
    #Exposes statistics from /proc/vmstat.	Linux
    metric_vmstat = forms.BooleanField(label="/proc/vmstat statistics",required=False)
    #Exposes XFS runtime statistics.	Linux (kernel 4.4+)
    metric_xfs = forms.BooleanField(label="XFS runtime statistics statistics",required=False)
    #Exposes ZFS performance statistics.	Linux, Solaris
    metric_zfs = forms.BooleanField(label="ZFS performance statistics",required=False)

def add_endpoint(request):
    submitted = False
    if request.method == 'POST':
        form = EndpointForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd.get('username'))
            # assert False
            hi = hello.hello(cd.get('username'),cd.get('password'),cd.get('ip_address'))
            hi.show()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = EndpointForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 
        'add_endpoint/add_endpoint.html',
        {'form': form, 'submitted': submitted}
        )