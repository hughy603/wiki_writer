
class GenericPage:
    pass


class TermPage(GenericPage):
    pass


class ColumnPage(GenericPage):
    pass


class LoadType:

    def __init__(self, page_formatter, stage_types, category,
                 children=None, cobol_category=None,
                 cobol_children=None):
        self.page_formatter = page_formatter
        self.stage_types = self._convert_to_list(stage_types)
        self.category = category
        self.children = self._convert_to_list(children)
        self.cobol_category = cobol_category
        self.cobol_children = self._convert_to_list(cobol_children)

    def _convert_to_list(string_or_list):
        if isinstance(string_or_list, str):
            string_or_list = [string_or_list]
        return string_or_list


page_type_to_format = {
    'host': LoadType(GenericPage, 'host', 'Hosts', 'database'),
    'database': LoadType(GenericPage, 'database', 'Databases',
                         'schema', 'Subject Matter', 'Copybooks'),
    'schema': LoadType(GenericPage, 'schema', 'Schemas',
                       ['table', 'view'], 'Copybooks',
                       '01 Level/Areas'),
    'term': LoadType(TermPage, 'term', 'Terms'),
    'column': LoadType(ColumnPage, 'column', 'Columns',
                       cobol_category='COBOL Fields')
}


def write_page(pk, load_type):
    """ Writes the page for a specific primary key using
    the provided page formatting class
    """
    pass


def write_all_pages(page_type):
    """ Writes every uncomitted page for the specific type
    """
    load_type = page_type_to_format[page_type]
    modified_pages = get_all_modified_pages(page_type)
    for modified_page in modified_pages:
        write_page(modified_page, load_type)


def get_all_modified_pages(page_type):
    """ Gets all pages that need to be rewritten for the given type
    """
    return []
