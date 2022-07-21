import platform,psutil

print("OS : eNix* (Version 0.1 alpha)")
print("Host OS : " + platform.system())
print("RAM : " + str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
print("CPU : " + str(platform.processor()))
print("CPU Cores : " + str(psutil.cpu_count()))
print("Storage spcace: " + str(round(psutil.disk_usage('/').total / (1024.0 **3)))+" GB")