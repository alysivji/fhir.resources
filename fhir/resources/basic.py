# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Basic
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Basic(domainresource.DomainResource):
    """ Resource for non-supported content.
    Basic is used for handling concepts not yet defined in FHIR, narrative-only
    resources that don't map to an existing resource, and custom resources not
    appropriate for inclusion in the FHIR specification.
    """

    resource_type = Field("Basic", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Type `Reference` referencing `Practitioner, PractitionerRole, Patient, RelatedPerson, Organization` (represented as `dict` in JSON)",
        description="Who created",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Kind of Resource",
    )

    created: fhirtypes.Date = Field(
        None,
        alias="created",
        title="Type `Date` (represented as `dict` in JSON)",
        description="When created",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Identifies the focus of this resource",
    )
