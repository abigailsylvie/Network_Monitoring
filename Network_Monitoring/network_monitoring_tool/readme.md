Sure! Here is the revised documentation without mentioning Git and including the instructions for installing and setting up nmap:

---

## Network Monitoring Tool Setup and Installation Guide

### Prerequisites
- Python 3.x installed on your system.
- Virtual environment tool (`venv`).
- nmap installed and set to the system path.

### Step 1: Extract the Project Files
Extract the project files from the provided ZIP file to your desired directory.

### Step 2: Set Up Virtual Environment
Create and activate a virtual environment to manage your dependencies.

1. Open Command Prompt and navigate to the project directory.
   
   ```sh
   cd path\to\network_monitoring_tool
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

### Step 3: Install Required Packages
Install the necessary Python packages listed in `requirements.txt`. Create this file if it does not exist and add the following dependencies:

```txt
Django==4.1
scapy
python-nmap
```

Then install the packages:

```sh
pip install -r requirements.txt
```

### Step 4: Install and Configure nmap
1. **Download nmap**: Download nmap from the official website: [nmap.org/download](https://nmap.org/download.html)

2. **Install nmap**: Follow the installation instructions for your operating system.

3. **Set nmap Path**:
   - Add the nmap installation directory to your system's PATH environment variable.
   - For Windows 10:
     1. Open **Control Panel** > **System and Security** > **System**.
     2. Click **Advanced system settings**.
     3. Click **Environment Variables**.
     4. Under **System variables**, find the `Path` variable, and click **Edit**.
     5. Click **New** and add the path to the nmap installation directory (e.g., `C:\Program Files (x86)\Nmap`).
     6. Click **OK** to close all dialog boxes.

### Step 5: Django Project Configuration
Ensure your Django project is correctly configured:

1. **Project Structure**:
   Make sure your project structure resembles the following:

   ```plaintext
   network_monitoring_tool/
   ├── manage.py
   ├── network_monitoring_tool/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── monitor/
       ├── __init__.py
       ├── admin.py
       ├── apps.py
       ├── models.py
       ├── tests.py
       └── views.py
   ```

2. **settings.py**:
   Ensure `INSTALLED_APPS` includes `'monitor'`:

   ```python
   INSTALLED_APPS = [
       ...
       'monitor',
       ...
   ]

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

### Step 6: Database Setup
Migrate the database to create necessary tables.

```sh
python manage.py migrate
```

### Step 7: Running the Network Monitoring Script
Create a script `integrate.py` in the root directory with the following content:

```python
import os#noqa
import django#noqa
from scapy.all import sniff, IP
import nmap

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_monitoring_tool.settings')
django.setup()#noqa

from monitor.models import Vulnerability

def packet_callback(packet):
    ip_layer = packet.getlayer(IP)
    if ip_layer:
        print(f'IP Packet: {ip_layer.src} -> {ip_layer.dst}')
        nmap_scan(ip_layer.src)

def nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024', '-sV')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                new_vuln = Vulnerability(
                    host=host,
                    port=port,
                    service=nm[host][proto][port]['name'],
                    state=nm[host][proto][port]['state']
                )
                new_vuln.save()

if __name__ == '__main__':
    sniff(iface='Wi-Fi', prn=packet_callback, count=10)
```

### Step 8: Running the Script
Ensure your virtual environment is activated and run the script.

```sh
python integrate.py
```

### Additional Configuration and Notes

1. **Logging**:
   Consider adding logging for better monitoring and debugging.

   ```python
   import logging

   logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
   ```

2. **Error Handling**:
   Add robust error handling to manage unexpected issues gracefully.

   ```python
   def nmap_scan(target):
       try:
           nm = nmap.PortScanner()
           nm.scan(target, '1-1024', '-sV')
           for host in nm.all_hosts():
               for proto in nm[host].all_protocols():
                   lport = nm[host][proto].keys()
                   for port in lport:
                       new_vuln = Vulnerability(
                           host=host,
                           port=port,
                           service=nm[host][proto][port]['name'],
                           state=nm[host][proto][port]['state']
                       )
                       new_vuln.save()
                       logging.info(f'Saved vulnerability: {new_vuln}')
       except Exception as e:
           logging.error(f'Error scanning {target}: {e}')
   ```

### Conclusion
You have successfully set up and run the network monitoring tool. For any issues or further customization, refer to the Django and Scapy documentation.

---

This documentation should guide your team through setting up and running the network monitoring tool on Windows OS, with all necessary details included.