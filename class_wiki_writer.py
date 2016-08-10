def get_asset(rid):
    """ Get the asset from the staging table
    """
    pass


class BasicType:

    def __init__(self, rid):
        self.rid = rid

    @property
    def staging_types(self):
        """ TODO: Is the asset type really required??? IDT so....
        """
        try:
            # Combine extra staging types and the main asset type
            return self._extra_staging_types + [self.asset_type]
        except NameError:
            # _extra_staging_types is not set, so return only
            # the asset type
            return [self.asset_type]
        except TypeError:
            # _extra_staging_types was not a list, so return a
            # two element list
            return [self._extra_staging_types, self.asset_type]

    @property
    def children(self):
        """ This is made generic for 3 types. Can it be defined
        once per type??? DRY VIOLATION???
        """
        try:
            return [self.child]
        except NameError:
            return self._children

    def get_page_text(self, asset):
        text = self.get_prefix(asset['_name'])
        raise Exception('This method should be defined by a subclass')

    def get_prefix(self, asset_name):
        """ TODO: test self vs cls
        """
        prefix = '{{DISPLAYTITLE:%s}}\n' % asset_name
        prefix += '[[Category:{}|{}]]'.format(self.category, self.asset_name)
        return prefix

    def write_page_to_wiki(self):
        pass

    def write_page(self):
        asset = get_asset(self.rid)
        text = self.get_page_text(asset)
        self.write_page_to_wiki(text)


class Term(BasicType):
    asset_type = 'term'
    category = 'Terms'


class Host(BasicType):
    asset_type = 'host'
    category = 'Host'
    child = 'Databases'
    cobol_child = 'Subject Areas'


class Schema(BasicType):
    asset_type = 'database_schema'
    category = 'Schemas'
    _children = ['Tables', 'Views']
    cobol_category = 'Copybooks'
    cobol_child = '01 Level/Areas'


class Table(BasicType):
    asset_type = 'database_table'
    category = 'Tables'
    _extra_staging_types = 'design_table'
    cobol_category = '01 Level/Areas'  # DRY VOILATION!!!!
