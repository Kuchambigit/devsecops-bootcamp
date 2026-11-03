
# Import the os module to interact with the operating system
import os

# Import the platform module to retrieve server information
import platform

# Display the server's hostname
print("Server Name:", platform.node())

# Display the operating system
print("Operating System:", platform.system())

# Retrieve the number of logical CPU cores
cpu_count = os.cpu_count()

# Display the CPU count
print("CPU Cores:", cpu_count)

# Import the psutil library for system monitoring
import psutil

# Measure CPU utilization over a one-second interval
cpu_usage = psutil.cpu_percent(interval=1)

# Retrieve memory utilization as a percentage
memory_usage = psutil.virtual_memory().percent

# Retrieve disk utilization for the root filesystem
disk_usage = psutil.disk_usage("/").percent

# Display the monitoring results
print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory_usage, "%")
print("Disk Usage:", disk_usage, "%")

# Import datetime to work with dates and time
from datetime import datetime

# Retrieve the server's last boot time
boot_time = datetime.fromtimestamp(psutil.boot_time())

# Calculate how long the server has been running
uptime = datetime.now() - boot_time

# Display the server uptime
print("Server Uptime:", uptime)

# Define resource utilization thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 85

# Check whether CPU utilization exceeds its threshold
if cpu_usage > CPU_THRESHOLD:
    print("WARNING: High CPU usage!")
else:
    print("CPU Status: Healthy")

# Check whether memory utilization exceeds its threshold
if memory_usage > MEMORY_THRESHOLD:
    print("WARNING: High memory usage!")
else:
    print("Memory Status: Healthy")

# Check whether disk utilization exceeds its threshold
if disk_usage > DISK_THRESHOLD:
    print("WARNING: High disk usage!")
else:
    print("Disk Status: Healthy")
