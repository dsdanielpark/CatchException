from ExceptNotifier.base.notifier import BaseSuccessHandler, BaseSendHandler, BaseExceptionIpython
from ExceptNotifier.apps.discord.sender import send_discord_msg
from ExceptNotifier.base.stacker.success_stacker import stack_success_msg
from ExceptNotifier.base.stacker.send_stacker import stack_send_msg
from ExceptNotifier.base.stacker.error_stacker import stack_error_msg
from ExceptNotifier.decorators.bard_ai_decorator import handle_bard_if_available
from ExceptNotifier.decorators.open_ai_decorator import handle_openai_if_available

from os import environ


class SuccessDiscord(BaseSuccessHandler):
    """
    Sends success message to Discord.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends success message to Discord.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_discord_msg(environ["_DISCORD_WEBHOOK_URL"], stack_success_msg("discord")["text"])
        return super().__call__(*args, **kwargs)


class SendDiscord(BaseSendHandler):
    """
   Sends specific line arrival message to Discord.
    """

    def __call__(self, *args, **kwargs):
        """
       Sends specific line arrival message to Discord.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_discord_msg(environ["_DISCORD_WEBHOOK_URL"], stack_send_msg("discord")["text"])
        return super().__call__(*args, **kwargs)


class ExceptDiscord(BaseException):
    """
    Custom exception that sends error message to Discord.
    """

    @handle_openai_if_available
    @handle_bard_if_available
    def __call__(etype: object, value: object, tb: object):
        """
        Sends error message to Discord.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_discord_msg(
            environ["_DISCORD_WEBHOOK_URL"],
            stack_error_msg(etype, value, tb, "discord")["text"],
        )


class ExceptDiscordIpython(BaseExceptionIpython):
    def __init__(self):
        super().__init__()
        pass

    @handle_openai_if_available
    @handle_bard_if_available
    def custom_exc(
        self, shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in IPython for sending Discord.

        :param shell: Executed shell, ZMQInteractiveShell object.
        :type shell: object
        :param etype: Error type
        :type etype: object
        :param evalue: Error value
        :type evalue: object
        :param tb: TraceBack object of IPython
        :type tb: object
        :param tb_offset: Offset of traceback, defaults to 1
        :type tb_offset: int, optional
        """
        shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
        data = stack_error_msg(etype, evalue, tb, "discord")
        send_discord_msg(environ["_DISCORD_WEBHOOK_URL"], data["text"])

        return None
