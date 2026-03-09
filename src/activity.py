import logging
logger = logging.getLogger(__name__)

def process_user(user):
    logger.info(f"Processing user: {user.email}")
    logger.debug(f"User phone: {user.phone}")
    logger.info(f"Full user payload: {user.__dict__}")

def track_payment(payment):
    logger.info(f"Payment from {payment.email}: ${payment.amount}")
    logger.debug(f"Card: {payment.card_number}")
    