import requests
from fabric.api import local

def update():
    local('rm -rf fonts/')
    local('rm katex.min.css')
    local('rm katex.min.js')
    local('rm -rf contrib/')
    latest_version = requests.get('https://api.github.com/repos/Khan/KaTex/releases/latest').json()['tag_name']
    local('wget https://github.com/Khan/KaTeX/releases/download/{0}/katex.zip'.format(latest_version))
    local('unzip katex.zip && rm katex.zip')
    local('rm katex/README.md')
    local('mv katex/* .')
    local('rmdir katex')
    print 'latest version: {0}'.format(latest_version)
