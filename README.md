# Django boilerplate

## How to use this template
- Click on "Use this template" above, this will create a new repository based on this template
- clone your new repository to local
- setup your environment using venv or pipenv, and activate
- run `pip install -r installer/requirements.txt`, or if you plan on testing it, use `installer/test_requirements.txt`. If the installation throws an error like this: `ERROR: No matching distribution found for psycopg2==2.9.2`, edit `installer/basic_requirements.txt` on line 7 to `psycopg2-binary==2.9.2` and re-run that command. Don't forget to undo the change after `pip install` is done
- setup your environment variable, consult `ex.env` file as a guide. Copy that file, make modifications, and rename it to `.env`

## Notes on testing
- make sure you install the requirements from `installer/test_requirements.txt` file
- we are using `pytest` as the test framework, so you can put fixtures in the `conftest.py` file and your tests in `tests` folder.
- make sure to prefix the names of your test files (and test functions inside of them) with `test_`. For example:
  ```
  # file name: tests/test_user.py

  def test_user(user) -> None:
    assert user is not None
  ```
- run the tests with this command: `pytest -s`. This will run all tests in `tests` folder, the `-s` flag is used to show all `print()` functions that will otherwise be hidden. You can also run the test files individually like so: `pytest -s tests/test_user.py`
- consult [Pytest documentation](https://pytest.org/) or [pytest-django documentation](https://pytest-django.readthedocs.io/) for more information

## Notes on localisation
- install `gettext` from your OS's package manager (`sudo apt install gettext` in Ubuntu)
- import `gettext` on the file you want to have your translations in like so:
  ```
  from django.utils.translation import gettext as _
  ```
- mark the texts you want to be translated like this:

  ```
  print(_("key"))
  message: str = _("another key")
  ```
- run `./manage makemessages -a` **every time** you add new keys or edit existing ones to save the changes and register your keys.
- edit `locale/en_US/LC_MESSAGES/django.po` (or `locale/zh_Hant/LC_MESSAGES/django.po`) and add your translations in `msgstr` fields
- when finished, run `./manage.py compilemessages` to compile your changes, this will create `*.mo` files alongside the `.po` files
- consult [Django documentation](https://docs.djangoproject.com/en/3.2/topics/i18n/translation) for more information

## Notes on deployment
- There is a descriptive [README](deployment/README.md) file in the `deployment/` directory.
- skaffold.yaml is used by the skaffold dev/deployment tool. It needs to be in the root directory so that it can access all the code for building images.