# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """

    resource_type = Field("ObservationDefinition", const=True)

    abnormalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="abnormalCodedValueSet",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Value set of abnormal coded values for the observations conforming to this ObservationDefinition",
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Category of observation",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Type of observation (code / type)",
    )

    criticalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="criticalCodedValueSet",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Value set of critical coded values for the observations conforming to this ObservationDefinition",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Business identifier for this ObservationDefinition instance",
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Method used to produce the observation",
    )

    multipleResultsAllowed: bool = Field(
        None,
        alias="multipleResultsAllowed",
        title="Type `bool`",
        description="Multiple results allowed",
    )

    normalCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="normalCodedValueSet",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Value set of normal coded values for the observations conforming to this ObservationDefinition",
    )

    permittedDataType: ListType[fhirtypes.Code] = Field(
        None,
        alias="permittedDataType",
        title="List of `Code` items (represented as `dict` in JSON)",
        description="Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period",
    )

    preferredReportName: fhirtypes.String = Field(
        None,
        alias="preferredReportName",
        title="Type `String` (represented as `dict` in JSON)",
        description="Preferred report name",
    )

    qualifiedInterval: ListType[
        fhirtypes.ObservationDefinitionQualifiedIntervalType
    ] = Field(
        None,
        alias="qualifiedInterval",
        title="List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON)",
        description="Qualified range for continuous and ordinal observation results",
    )

    quantitativeDetails: fhirtypes.ObservationDefinitionQuantitativeDetailsType = Field(
        None,
        alias="quantitativeDetails",
        title="Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON)",
        description="Characteristics of quantitative results",
    )

    validCodedValueSet: fhirtypes.ReferenceType = Field(
        None,
        alias="validCodedValueSet",
        title="Type `Reference` referencing `ValueSet` (represented as `dict` in JSON)",
        description="Value set of valid coded values for the observations conforming to this ObservationDefinition",
    )


class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """

    resource_type = Field("ObservationDefinitionQualifiedInterval", const=True)

    age: fhirtypes.RangeType = Field(
        None,
        alias="age",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Applicable age range, if relevant",
    )

    appliesTo: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="appliesTo",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Targetted population of the range",
    )

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Type `Code` (represented as `dict` in JSON)",
        description="reference | critical | absolute",
    )

    condition: fhirtypes.String = Field(
        None,
        alias="condition",
        title="Type `String` (represented as `dict` in JSON)",
        description="Condition associated with the reference range",
    )

    context: fhirtypes.CodeableConceptType = Field(
        None,
        alias="context",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Range context qualifier",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="Type `Code` (represented as `dict` in JSON)",
        description="male | female | other | unknown",
    )

    gestationalAge: fhirtypes.RangeType = Field(
        None,
        alias="gestationalAge",
        title="Type `Range` (represented as `dict` in JSON)",
        description="Applicable gestational age range, if relevant",
    )

    range: fhirtypes.RangeType = Field(
        None,
        alias="range",
        title="Type `Range` (represented as `dict` in JSON)",
        description="The interval itself, for continuous or ordinal observations",
    )


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    Characteristics for quantitative results of this observation.
    """

    resource_type = Field("ObservationDefinitionQuantitativeDetails", const=True)

    conversionFactor: fhirtypes.Decimal = Field(
        None,
        alias="conversionFactor",
        title="Type `Decimal` (represented as `dict` in JSON)",
        description="SI to Customary unit conversion factor",
    )

    customaryUnit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="customaryUnit",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Customary unit for quantitative results",
    )

    decimalPrecision: fhirtypes.Integer = Field(
        None,
        alias="decimalPrecision",
        title="Type `Integer` (represented as `dict` in JSON)",
        description="Decimal precision of observation quantitative results",
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="SI unit for quantitative results",
    )
