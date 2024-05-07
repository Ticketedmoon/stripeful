# stripeful
A repository to manage test interactions with the Stripe Api

## Virtual Environment

#### Create

```
python3 -m venv env
```

#### Activate

```
source env/bin/activate
```

#### Deactivate

```
 ~ deactivate
```

### Dependencies

```
pip list
```

Create requirements.txt with currently installed Dependencies:
```
pip freeze > requirements.txt
```

## Git

If we want to remove a file (`constants.py` in this case) from our git repository, we can use the following:

```
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch stripeful/src/constants.py" --prune-empty --tag-name-filter cat -- --all
```

In some scenarios, we want to keep a file on git, but no longer want to track changes for a file.  
This is very useful when we want to have a template environment variable file where all of the keys are visible in VCS, but not the values:
```
git update-index --assume-unchanged stripeful/src/constants.py
```

To reverse this operation:
```
git update-index --no-assume-unchanged stripeful/src/constants.py
```
