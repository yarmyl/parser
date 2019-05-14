# parser

Умеет выдавать конфигу в формате yaml, json, conf (default), dict

# Usage

```
usage: parser.py [-h] [--url [URL]] [--format [FORMAT]] [--local [LOCAL]]

optional arguments:
  -h, --help         show this help message and exit
  --url [URL]
  --format [FORMAT]
  --local [LOCAL]
```

# Example

```
gitlab-runner@gitlab-runner:~/playbooks/lk-bc$ ../scripts/parser.py --url http://172.26.133.229:8761/config/lk-bc-front/broker/ --format json
{"baseUrl": "/", "name": "Project-template", "port": 443, "host": "app-broker.rusoft.pro", "appTitle": "Project-template", "api": "https://api-app-broker.rusoft.pro", "dist": "build", "source": "src"}
 
gitlab-runner@gitlab-runner:~/playbooks/lk-bc$ /home/gitlab-runner/playbooks/scripts/parser.py --url http://172.26.133.229:8761/config/lk-bc-front/broker/ --format dict
{'source': 'src', 'dist': 'build', 'host': 'app-broker.rusoft.pro', 'port': 443, 'appTitle': 'Project-template', 'name': 'Project-template', 'api': 'https://api-app-broker.rusoft.pro', 'baseUrl': '/'}
 
gitlab-runner@gitlab-runner:~/playbooks/lk-bc$ /home/gitlab-runner/playbooks/scripts/parser.py --url http://172.26.133.229:8761/config/lk-bc-front/broker/ --format сщта
Wrong format!
 
gitlab-runner@gitlab-runner:~/playbooks/lk-bc$ /home/gitlab-runner/playbooks/scripts/parser.py --url http://172.26.133.229:8761/config/lk-bc-front/broker/ --format conf
name=Project-template
dist=build
api=https://api-app-broker.rusoft.pro
port=443
host=app-broker.rusoft.pro
appTitle=Project-template
source=src
baseUrl=/
```
