from decimal import Decimal
from typing import Optional

from .brcodes import (get_additional_data_field_template, get_country_code,
                      get_crc16, get_merchant_account_information,
                      get_merchant_category_code, get_merchant_city,
                      get_merchant_name, get_payload_format_indicator,
                      get_transaction_currency, get_transaction_value)
from .utils import round_decimal


def create_pix_string_code(key: str, name: str, city: str,
                           value: Optional[Decimal] = None,
                           identifier: Optional[str] = None) -> str:
    """Generate a static PIX code following the instructions given by the
    `Manual de Padrões para Iniciação do Pix` v2.3.0 section 1.5.    

    :param key: Recipient's PIX key. Follow the key formatting from section 
        1.4 in the PIX manual.
    :type key: str
    :param name: Recipient's name. Maximum of 25 characters. Does not need 
        to be the exact name os the one used by the receiver's payments 
        service provider (PSP), and will be ignored by the payer's PSP as 
        stated in the manual.
    :type name: str
    :param city: Recipient's city. Must be an uppercase ASCII string (i.e no 
        accented characters, backtics, etc. only A-Z and whitespaces). 
        15 characters max.
    :type city: str
    :param value: Value to be transferred, defaults to None. If the value is to 
        be specified by the payer, set it to None.
    :type value: Optional[Decimal], optional
    :param identifier: Transaction identifier `txid` (section 1.5.2), defaults 
        to None.
    :type identifier: Optional[str], optional
    :return: The PIX code, ready to be used as is or generated as QR Code.
    :rtype: str

    .. _Manual de Padrões para Iniciação do Pix:
        https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix
    """

    transaction_value: str
    if value is not None:
        transaction_value = get_transaction_value(round_decimal(value))
    else:
        transaction_value = ''

    payload = "{pfi}{mai}{mcc}{tc}{tv}{cc}{mn}{mc}{adft}".format(
        pfi=get_payload_format_indicator(),
        mai=get_merchant_account_information(key),
        mcc=get_merchant_category_code(),
        tc=get_transaction_currency(),
        tv=transaction_value,
        cc=get_country_code(),
        mn=get_merchant_name(name),
        mc=get_merchant_city(city),
        adft=get_additional_data_field_template(identifier),
    )
    crc = get_crc16(payload)
    return payload + f"6304{crc}"
