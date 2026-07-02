import types

from celery import Task
from celery.signals import task_prerun, task_postrun
from django.core.management import ManagementUtility
from django.db.backends.signals import connection_created
from django.dispatch import receiver
from django_querytagger.wrapper import wrapper
from .tagging import current_tag


@receiver(connection_created)
def on_connection_created(sender, connection, **kwargs):
    connection.execute_wrappers.append(wrapper)


@receiver(task_prerun)
def on_task_prerun(task_id, task: Task, args, kwargs, **other):
    current_tag.set(f"task={task.name} taskid={task_id}")


@receiver(task_postrun)
def on_task_postrun(task_id, task: Task, args, kwargs, retval, state, **other):
    current_tag.set(None)


_old_fetch_command = ManagementUtility.fetch_command


def fetch_command(self, subcommand):
    current_tag.set(f"command={subcommand}")
    return types.MethodType(_old_fetch_command, self)(subcommand)


ManagementUtility.fetch_command = fetch_command
