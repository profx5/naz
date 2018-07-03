import typing
import logging


class BaseHook:
    """
    Interface that must be implemented to satisfy naz's hooks.
    User implementations should subclassing this class and
    implement the request and response methods with the type signatures shown.
    """

    async def request(self, event: str, correlation_id: typing.Optional[str] = None) -> None:
        raise NotImplementedError("request method must be implemented.")

    async def response(self, event: str, correlation_id: typing.Optional[str] = None) -> None:
        raise NotImplementedError("response method must be implemented.")


class SimpleHook(BaseHook):
    """
    class with hook methods that are called before a request is sent to SMSC and
    after a response is received from SMSC.

    User's can provide their own hook classes
    """

    def __init__(self, logger) -> None:
        self.logger: logging.Logger = logger

    async def request(self, event: str, correlation_id: typing.Optional[str] = None) -> None:
        """
        hook method that is called just before a request is sent to SMSC.
        """
        self.logger.debug(
            "request_hook_called. event={0}. correlation_id={1}".format(event, correlation_id)
        )

    async def response(self, event, correlation_id: typing.Optional[str] = None) -> None:
        """
        hook method that is called just after a response is gotten from SMSC.
        """
        self.logger.debug(
            "response_hook_called. event={0}. correlation_id={1}".format(event, correlation_id)
        )
