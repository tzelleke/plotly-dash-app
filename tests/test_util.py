from app.util import aio_id_resolver, classes, toggle_classes


def test_aio_id_resolver():
    id_resolver = aio_id_resolver("TestComponent", ["subcomponent1", "subcomponent2"])

    assert id_resolver.subcomponent_1("id1") == {
        "component": "TestComponent",
        "subcomponent": "subcomponent1",
        "id": "id1",
    }
    assert id_resolver.subcomponent_2("id2") == {
        "component": "TestComponent",
        "subcomponent": "subcomponent2",
        "id": "id2",
    }


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
