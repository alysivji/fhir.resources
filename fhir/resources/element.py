# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import fhirabstractmodel, fhirtypes


class Element(fhirabstractmodel.FHIRAbstractModel):
    """ Base for all elements.
    Base definition for all elements in a resource.
    """

    resource_type = Field("Element", const=True)

    extension: ListType[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
    )

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String` (represented as `dict` in JSON)",
        description="Unique id for inter-element referencing",
    )
