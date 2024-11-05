import psutil
import time

class RPiMonitor:
    def get_cpu_metrics(self):
        return {
            'usage': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count(logical=True),
            'frequency': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            'load_avg': psutil.getloadavg()
        }

    def get_memory_metrics(self):
        virtual_mem = psutil.virtual_memory()._asdict()
        swap_mem = psutil.swap_memory()._asdict()
        return {
            'virtual_memory': virtual_mem,
            'swap_memory': swap_mem
        }

    def get_disk_metrics(self):
        disk_usage = psutil.disk_usage('/')._asdict()
        disk_io = psutil.disk_io_counters()._asdict()
        return {
            'disk_usage': disk_usage,
            'disk_io': disk_io
        }

    def get_network_metrics(self):
        net_io = psutil.net_io_counters()._asdict()
        return net_io

    def get_temperature_metrics(self):
        temps = psutil.sensors_temperatures() if hasattr(psutil, 'sensors_temperatures') else None
        return temps

    def get_uptime(self):
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        uptime_days, remainder = divmod(uptime_seconds, 86400)
        uptime_hours, remainder = divmod(remainder, 3600)
        uptime_minutes, uptime_seconds = divmod(remainder, 60)
        return {
            'days': uptime_days,
            'hours': uptime_hours,
            'minutes': uptime_minutes,
            'seconds': uptime_seconds
        }
    
monitor = RPiMonitor()

print(monitor.get_temperature_metrics())
