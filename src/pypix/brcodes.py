from binascii import crc_hqx
from decimal import Decimal
from typing import Optional


def get_payload_format_indicator() -> str:
    return "000201"


def get_merchant_account_information(key: str) -> str:
    GUI = "0014BR.GOV.BCB.PIX"
    string = "01{l:02d}{k}".format(l=len(key), k=key)
    result = GUI + string

    if len(result) > 99:
        raise ValueError("PIX key is too long.")

    return "26{l:02d}{r}".format(l=len(result), r=result)


def get_merchant_category_code() -> str:
    return '52040000'


def get_transaction_currency() -> str:
    return '5303986'


def get_transaction_value(value: Decimal) -> str:
    if value <= Decimal('0.00'):
        raise ValueError("Only positive decimals allowed.")

    string = str(value)
    return f"54{'{:02d}'.format(len(string))}{string}"


def get_country_code() -> str:
    return '5802BR'


def get_merchant_name(name: str) -> str:
    if len(name) > 25:
        raise ValueError(
            "Recipient name must be less than 25 characters long.")
    return f"59{'{:02d}'.format(len(name))}{name}"


def get_merchant_city(city: str) -> str:
    if len(city) > 15:
        raise ValueError("Max of 15 characters for city name.")
    return f"60{'{:02d}'.format(len(city))}{city}"


def get_additional_data_field_template(identifier: Optional[str] = None):
    if not identifier:
        identifier = '***'

    if len(identifier) > 25:
        raise ValueError("Only indentifiers with length less than 25 "
                         "characters are allowed.")

    txid = f"05{'{:02d}'.format(len(identifier))}{identifier}"
    return f"62{'{:02d}'.format(len(txid))}{txid}"


def get_crc16(payload: str) -> str:
    checksum = crc_hqx(bytes(payload + '6304', 'ascii'), 0xFFFF)
    return hex(checksum)[2:].upper()
