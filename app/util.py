from functools import cache

import pydash as py_


def aio_id_resolver(component_name: str, subcomponent_labels: list[str]) -> type:
    """Create a resolver class for subcomponent IDs in AIO components.

    Args:
        component_name (str): Fills 'component' key in ID dict.
        subcomponent_labels ([str]): Define names of resolver methods
            Fill 'subcomponent' keys in ID dicts.

    Returns:
        type: ID resolution class for AIO component.
    """
    class_properties = {
        py_.snake_case(label): staticmethod(
            py_.partial(
                lambda component, subcomponent, aio_id: dict(
                    component=component,
                    subcomponent=subcomponent,
                    id=aio_id,
                ),
                component_name,
                label,
            )
        )
        for label in subcomponent_labels
    }

    return type(f"IdResolver{component_name}", (), class_properties)


@cache
def toggle_classes(class_name: str, *classes_: str) -> str:
    """Toggle classes in a string of classes.

    Args:
        class_name (str): String of classes separated by spaces.
        *classes_ (str): Classes to toggle.

    Returns:
        str: String of classes separated by spaces.
    """
    return " ".join(set(class_name.split()).symmetric_difference(classes_))


@cache
def classes(*classes_: str) -> str:
    """Return a string of classes separated by spaces.

    Args:
        *classes_ (str): Classes to join.

    Returns:
        str: String of classes separated by spaces.
    """
    return " ".join(classes_)
