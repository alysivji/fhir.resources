# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    resource_type = Field("Ratio", const=True)

    denominator: fhirtypes.QuantityType = Field(
        None,
        alias="denominator",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Denominator value",
    )

    numerator: fhirtypes.QuantityType = Field(
        None,
        alias="numerator",
        title="Type `Quantity` (represented as `dict` in JSON)",
        description="Numerator value",
    )
