
class GenericPage:
    pass


class TermPage(GenericPage):
    pass


class ColumnPage(GenericPage):
    pass


class LoadType:

    def __init__(self, page_formatter, stage_type, category,
                 children=None, cobol_category=None,
                 cobol_children=None):
        self.page_formatter = page_formatter
        self.stage_type = stage_type
        self.category = category
        self.children = self._convert_to_list(children)
        self.cobol_category = cobol_category
        self.cobol_children = self._convert_to_list(cobol_children)

    def _convert_to_list(string_or_list):
        if isinstance(string_or_list, str):
            string_or_list = [string_or_list]
        return string_or_list

    def __str__(self):
        return ('A page for the asset type {self.stage_type} '
                'formatted by {self.page_formatter}. '
                'The page belongs to the category {self.category} '
                'and contains {self.children} asset types'
                .format(self=self))


type_format_map = {
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
    print('Writing the page',pk,'for the load type',load_type)


def write_all_pages(page_type):
    """ Writes every uncomitted page for the specific type
    """
    load_type = type_format_map[page_type]
    modified_pages = get_all_modified_pages(page_type)
    for modified_page in modified_pages:
        write_page(modified_page, load_type)


def get_all_modified_pages(page_type):
    """ Gets all pages that need to be rewritten for the given type
    """
    return []
