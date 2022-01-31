def field_mapping(some_class):
    """ returns a dictionary mapping model field names to lookukp values
        :param some_class: Any django model class with extra field properties
        :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[(x.extra['data_lookup']).strip()] = x.name
        except:  # noqa: E722
            pass
    return field_mapping_dict
