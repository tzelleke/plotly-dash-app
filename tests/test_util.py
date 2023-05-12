from app.util import classes, toggle_classes


def _has_only_classes(class_name: str, expected_classes_: str) -> bool:
    return set(class_name.split()) == set(expected_classes_.split())


def test_toggle_classes():
    assert toggle_classes("") == ""
    assert toggle_classes("   ") == ""
    assert _has_only_classes(
        toggle_classes("a b c", "d", "e"),
        "a b c d e",
    )
    assert _has_only_classes(
        toggle_classes("a b c", "b", "e"),
        "a c e",
    )
    assert _has_only_classes(
        toggle_classes("a b c"),
        "a b c",
    )


def test_classes_():
    assert classes() == ""
    assert classes("a", "b", "c") == "a b c"
