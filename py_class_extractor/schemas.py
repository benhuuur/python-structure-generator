from typing import Any, Tuple
from dataclasses import dataclass
from py_class_extractor.file_management import SerializableToDict


@dataclass
class AttributeInformation:
    """
    Data class to store information about a attribute.
    """

    name: str
    data_type: str
    encapsulation: str


@dataclass
class FunctionInformation:
    """
    Data class to store information about a function.
    """

    name: str
    args: Tuple[str]
    return_value: Any
    encapsulation: str


@dataclass
class RelationshipInformation:
    """
    Data class to store information about a UML relationship.
    """
    type: str
    related: str


@dataclass
class ClassInformation(SerializableToDict):
    """
    Data class to store information about a class.

    Attributes:
    - modules (Tuple[str]): Tuple of module names where the class is defined.
    - name (str): The name of the class.
    - relationships (Tuple[RelationshipInformation]): Tuple of RelationshipInformation objects representing relationships with other classes.
    - attributes (Tuple[AttributeInformation]): Tuple of AttributeInformation objects representing attributes of the class.
    - methods (Tuple[FunctionInformation]): Tuple of FunctionInformation objects representing methods of the class.
    """

    modules: Tuple[str]
    name: str
    relationships: Tuple[RelationshipInformation]
    attributes: Tuple[AttributeInformation]
    methods: Tuple[FunctionInformation]

    def to_dictionary(self) -> dict:
        """
        Converts the ClassInformation object into a dictionary representation suitable for JSON serialization.

        Returns:
        - dict: A dictionary containing the class information.
            {
                "modules": Tuple[str],                      # Tuple of module names where the class is defined.
                "class_name": str,                         # The name of the class.
                "relationships": Tuple[dict],              # Tuple of dictionaries representing relationships (RelationshipInformation objects).
                "attributes": Tuple[dict],                 # Tuple of dictionaries representing attributes (AttributeInformation objects).
                "methods": Tuple[dict]                     # Tuple of dictionaries representing methods (FunctionInformation objects).
            }
        """
        return {
            "name": self.name,
            "modules": tuple(self.modules),
            "relationships": tuple(relationship.__dict__ for relationship in self.relationships),
            "attributes": tuple(attribute.__dict__ for attribute in self.attributes),
            "methods": tuple(method.__dict__ for method in self.methods),
        }
