from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        info = toml.loads(content)
        poetry_info = info['tool']['poetry']
        return Project(poetry_info['name'], 
                       poetry_info['description'],
                       poetry_info['license'],
                       poetry_info['authors'],
                       list(poetry_info['dependencies'].keys()), 
                       list(poetry_info['group']['dev']['dependencies'].keys()))
