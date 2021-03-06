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

   <p aling=center>
<a href="https://api-msd-z.matiasing.repl.co/"><img src="https://img.shields.io/badge/API LINK-blue?style=for-the-badge&logo=web"></a>
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
py .\main.py
```

## 🚀 Implementation
```python
# EXAMPLE
import requests
print("Active development for Minecraft 1.18.2")
# purpur_select = int(input("[1]1.18.2\n[2]1.18.1\n[3]1.16.5\n..."))    
spigot_select = int(input("[1]1.18.2\n[2]1.18.1\n[3]1.17.1\n..."))
   
   
# spigot/paper/purpur   
# resp = requests.get(f'http://localhost:80/purpur/{purpur_select}')
resp = requests.get(f'http://localhost:80/spigot/{spigot_select}')
print(resp.json()["link"])
```
    
### ⚙ Future To-do List:
- [x] Deploy API
- [x] Apply API to MDS-X
- [x] document better
