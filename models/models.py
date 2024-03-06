# -*- coding: utf-8 -*-

import logging

from odoo import fields, models, api


_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None

class AccountPayment(models.Model):
    _inherit = 'account.payment'


    def _num2words(self, number, lang):
        if num2words is None:
            _logger.warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        return num2words(number, lang=lang).title()