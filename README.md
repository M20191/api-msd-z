<h1 align=center>MSD-Z API</h1>

<p align=center>
 <a href="#"><img title="build" src="https://img.shields.io/badge/status-stable-green?style=for-the-badge&logo=github"><a>
</p>
   
<p align=center>
  <a href="#"><img title="build" src="https://img.shields.io/badge/OS-WINDOWS-blue?style=for-the-badge&logo=windows"><a>
  <a href="#"><img title="build" src="https://img.shields.io/badge/OS-LINUX-yellow?style=for-the-badge&logo=linux"><a>
</p>
    
    
<p align="center">
  <a href="#"><img src="https://img.shields.io/github/license/M20191/MSD-X?style=flat-square&logo=sublime-text"></a>
</p>
   
---
    
## 🌿 Jar's Versions
* Purpur
* Paper
* Spigot
    
## ☀ Features

* Easy to use
* Easy to implement
* Support for all operating systems
* Modularization
* Light (-5MB)
* Global compatibility
    
## 🛠 Downloading repo, installing requirements and cd path:
```console 
git clone https://github.com/M20191/api-msd-z && pip install -r requirements.txt && cd api-msd-z/
```
## 🖥 How to use:
py (in windows)
python3 (in linux)
    
```console
py .\wsgi.py
```

## 🚀 Implementation
```python
import requests

print("Active development for Minecraft 1.18.2")
spigot_select = int(input("[1]1.18.2\n[2]1.18.1\n[3]1.17.1\n..."))

resp = requests.get(f'http://localhost:80/spigot/{spigot_select}')
print(resp.json()["link"])
```
    
### ⚙ Future To-do List:
- [ ] Deploy API
- [ ] Apply API to MDS-X
- [x] document better
    
