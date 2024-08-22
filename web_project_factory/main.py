import gitlab
import yaml
from collections import defaultdict
TOKEN = 'YOUR_GitLAB_Token_HERE'
gl = gitlab.Gitlab('https://gitlab.de/', private_token=TOKEN)

project = gl.projects.get(YOUR_PROJECT_NUMBER_HERE)

documents = None
with open(r'project_dummy.yaml') as file:
    documents = yaml.full_load(file)
   # print(documents)
    print(documents["billing_account_id"])
    print(documents["billing_alert"]["amount"])
    print(documents["billing_alert"]["thresholds"]["current"])
    documents["billing_alert"]["thresholds"]["current"] = [0.2,0.5,0.8]
    documents["labels"] = { 'env' : 'dev', 'name':'pancho'}
    for item, doc in documents.items():
       # print(item, ":", doc)
        documents["billing_account_id"] = "modified"

with open(r'/tmp/newfile.yaml', 'w') as file:
    documents = yaml.dump(documents, file)

data = {
    'branch': 'main',
    'commit_message': 'commited from python',
    'actions': [
        {
            'action': 'create',
            'file_path': 'data/projects/project_dummy.yaml',
            'content': open('project_dummy.yaml').read(),
        }
    ]
}
try:
    commit = project.commits.create(data)
    print(commit)
except Exception as exc:
    # This will be raised if the token is expired or any other
    # verification checks fail.
    print(exc)
