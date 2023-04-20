def display_cell_clicked_on(cell):
    if cell is None:
        return "Click on a cell"
    return f"clicked on cell value:   {cell['value']}, column:   {cell['colId']}, row index:   {cell['rowIndex']}"  # noqa: E501
