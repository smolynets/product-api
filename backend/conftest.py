# import pytest
# from django.core.management import call_command

# @pytest.fixture
# def reset_db(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         call_command('flush', interactive=False)