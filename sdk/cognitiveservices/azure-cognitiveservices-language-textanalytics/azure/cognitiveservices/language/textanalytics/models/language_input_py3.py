# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LanguageInput(Model):
    """LanguageInput.

    :param country_hint:
    :type country_hint: str
    :param id: Unique, non-empty document identifier.
    :type id: str
    :param text:
    :type text: str
    """

    _attribute_map = {
        'country_hint': {'key': 'countryHint', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
    }

    def __init__(self, *, country_hint: str=None, id: str=None, text: str=None, **kwargs) -> None:
        super(LanguageInput, self).__init__(**kwargs)
        self.country_hint = country_hint
        self.id = id
        self.text = text
