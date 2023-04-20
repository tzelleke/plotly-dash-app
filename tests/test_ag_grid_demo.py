from app.ag_grid_demo.callbacks import display_cell_clicked_on


def test_callback_display_clicked_on():
    assert display_cell_clicked_on(None) == "Click on a cell"
