from django_viewcomponent import component
from django_viewcomponent.fields import RendersOneField, RendersManyField

        
@component.register("table")
class TableComponent(component.Component):

    class RowComponent(component.Component):
        template_name = "table/table_row.html"
        items = RendersManyField()

        def __init__(self, **kwargs):
            pass

    class ColumnComponent(component.Component):
        template_name = "table/table_column.html"

        def __init__(self, **kwargs):
            pass

    template_name = "table/table.html"
    columns = RendersManyField(required=True, component=ColumnComponent)
    rows = RendersManyField()

    def __init__(self, title, **kwargs):
        self.title = title