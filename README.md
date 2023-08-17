Steps to compile sphinx documentation on Local:
1. Go to 'edit_documentation_here'.
2. Install required packages from requirements.txt.
3. Use MakeFile to run ´make html´.
4. Find 'documentation_preview' in root folder.

Workflow for github hosting:
(.github/worflows/jekyll.yml)
1. Push changes to repository.
2. Github Action runs jekyll.yml
3. Sphinx documentation is built on the server.
4. Changes are pushed automatically to the repository.
5. Jekyll is compiled.
6. Website is deployed to invesalius.github.io