from django.forms import ModelForm
from .models import Endpoint as Endpoint
from django import forms

class EndpointForm(ModelForm):
    class Meta:
        """form for adding an endpoint device, used for configuring new nodes"""
        model = Endpoint
        fields = ['node_name','ip_address','protocol','username','password','SSH_rsa_pub','operating_system','location',
        'metric_arp','metric_bcache','metric_bonding','metric_boottime','metric_conntrack','metric_cpu',
        'metric_cpufreq','metric_diskstats','metric_edac','metric_entropy','metric_exec','metric_filefd',
        'metric_filesystem','metric_hwmon','metric_infiniband','metric_ipvs','metric_loadavg','metric_mdadm',
        'metric_meminfo','metric_netclass','metric_netdev','metric_netstat','metric_nfs','metric_nfsd',
        'metric_pressure','metric_rapl','metric_schedstat','metric_sockstat','metric_softnet','metric_stat',
        'metric_textfile','metric_thermal_zone','metric_time','metric_timex','metric_udp_queues','metric_uname',
        'metric_vmstat','metric_xfs','metric_zfs']
        widgets = {
        'password': forms.PasswordInput(),
    }

class UpdateEndpointForm(ModelForm):
    class Meta:
        """form for adding an endpoint device, used for configuring new nodes"""
        model = Endpoint
        fields = ['node_name','ip_address','protocol','username','password','SSH_rsa_pub','operating_system','location',
        'metric_arp','metric_bcache','metric_bonding','metric_boottime','metric_conntrack','metric_cpu',
        'metric_cpufreq','metric_diskstats','metric_edac','metric_entropy','metric_exec','metric_filefd',
        'metric_filesystem','metric_hwmon','metric_infiniband','metric_ipvs','metric_loadavg','metric_mdadm',
        'metric_meminfo','metric_netclass','metric_netdev','metric_netstat','metric_nfs','metric_nfsd',
        'metric_pressure','metric_rapl','metric_schedstat','metric_sockstat','metric_softnet','metric_stat',
        'metric_textfile','metric_thermal_zone','metric_time','metric_timex','metric_udp_queues','metric_uname',
        'metric_vmstat','metric_xfs','metric_zfs']
        widgets = {
        'password': forms.PasswordInput(),
    }