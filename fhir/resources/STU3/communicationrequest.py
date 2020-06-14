# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """

    resource_type = Field("CommunicationRequest", const=True)

    authoredOn: fhirtypes.DateTime = Field(
        None,
        alias="authoredOn",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When request transitioned to being actionable",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Fulfills plan or proposal",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Message category",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Type `Reference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON)",
        description="Encounter or episode leading to message",
    )

    groupIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="groupIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Composite request this is part of",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Unique identifier",
    )

    medium: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="A channel of communication",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="List of `Annotation` items (represented as `dict` in JSON)",
        description="Comments made about communication request",
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="Type `DateTime` (represented as `dict` in JSON)",
        description="When scheduled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="When scheduled",
        one_of_many="occurrence",  # Choice of Data Types. i.e value[x]
        one_of_many_required=False,
    )

    payload: ListType[fhirtypes.CommunicationRequestPayloadType] = Field(
        None,
        alias="payload",
        title="List of `CommunicationRequestPayload` items (represented as `dict` in JSON)",
        description="Message payload",
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="Type `Code` (represented as `dict` in JSON)",
        description="Message urgency",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Why is communication needed?",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="List of `Reference` items referencing `Condition, Observation` (represented as `dict` in JSON)",
        description="Why is communication needed?",
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="List of `Reference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson, Group, CareTeam` (represented as `dict` in JSON)",
        description="Message recipient",
    )

    replaces: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="replaces",
        title="List of `Reference` items referencing `CommunicationRequest` (represented as `dict` in JSON)",
        description="Request(s) replaced by this request",
    )

    requester: fhirtypes.CommunicationRequestRequesterType = Field(
        None,
        alias="requester",
        title="Type `CommunicationRequestRequester` (represented as `dict` in JSON)",
        description="Who/what is requesting service",
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Type `Reference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON)",
        description="Message sender",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="draft | active | suspended | cancelled | completed | entered-in-error | unknown",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Type `Reference` referencing `Patient, Group` (represented as `dict` in JSON)",
        description="Focus of message",
    )

    topic: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="topic",
        title="List of `Reference` items referencing `Resource` (represented as `dict` in JSON)",
        description="Focal resources",
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "occurrence": ["occurrenceDateTime", "occurrencePeriod",],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """

    resource_type = Field("CommunicationRequestPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Type `Attachment` (represented as `dict` in JSON)",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Type `Reference` referencing `Resource` (represented as `dict` in JSON)",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Type `String` (represented as `dict` in JSON)",
        description="Message part content",
        one_of_many="content",  # Choice of Data Types. i.e value[x]
        one_of_many_required=True,
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "content": ["contentAttachment", "contentReference", "contentString",],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class CommunicationRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting service.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    resource_type = Field("CommunicationRequestRequester", const=True)

    agent: fhirtypes.ReferenceType = Field(
        ...,
        alias="agent",
        title="Type `Reference` referencing `Practitioner, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON)",
        description="Individual making the request",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Type `Reference` referencing `Organization` (represented as `dict` in JSON)",
        description="Organization agent is acting for",
    )
