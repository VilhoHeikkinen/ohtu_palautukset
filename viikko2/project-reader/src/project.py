class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _make_bulletpoint(self, items):
        return "\n- " + "\n- ".join(items) if len(items) > 0 else "\n-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors: {self._make_bulletpoint(self.authors)}"
            f"\n\nDependencies: {self._make_bulletpoint(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._make_bulletpoint(self.dev_dependencies)}"
        )
