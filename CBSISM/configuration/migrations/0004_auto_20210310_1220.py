# Generated by Django 3.1.5 on 2021-03-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_endpoint_ssh_rsa_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoint',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_arp',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_bcache',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_bonding',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_boottime',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_conntrack',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_cpu',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_cpufreq',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_diskstats',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_edac',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_entropy',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_exec',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_filefd',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_filesystem',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_hwmon',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_infiniband',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_ipvs',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_loadavg',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_mdadm',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_meminfo',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_netclass',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_netdev',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_netstat',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_nfs',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_nfsd',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_pressure',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_rapl',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_schedstat',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_sockstat',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_softnet',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_stat',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_textfile',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_thermal_zone',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_time',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_timex',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_udp_queues',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_uname',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_vmstat',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_xfs',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='metric_zfs',
        ),
        migrations.AddField(
            model_name='endpoint',
            name='IP_address',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='node_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
