from fabric.api import local

def update():
    local('rm -rf fonts/')
    local('rm katex.min.css')
    local('rm katex.min.js')
    local('wget https://github.com/Khan/KaTeX/releases/download/v0.2.0/katex.zip')
    local('unzip katex.zip')
    local('rm katex.zip')
    local('rm katex/README.md')
    local('mv katex/* .')
    local('rmdir katex')
