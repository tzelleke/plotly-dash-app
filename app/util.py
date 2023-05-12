from functools import cache


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
