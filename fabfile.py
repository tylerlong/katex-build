import requests
from fabric.api import local

def update():
    latest_version = requests.get('https://api.github.com/repos/Khan/KaTex/releases/latest').json()['tag_name']
    local('rm -rf fonts/')
    local('rm katex.min.css')
    local('rm katex.min.js')
    local('wget https://github.com/Khan/KaTeX/releases/download/{0}/katex.zip'.format(latest_version))
    local('unzip katex.zip')
    local('rm katex.zip')
    local('rm katex/README.md')
    local('mv katex/* .')
    local('rmdir katex')
