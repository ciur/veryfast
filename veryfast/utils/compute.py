import logging

logger = logging.getLogger(__name__)

logger.info(f"My name was set to '{__name__}'")


def xvf_info():
    logger.debug("doing some extra XFV computations")
    return 100

