from flask import make_response


def to_title_case(word):
    return word[:1].upper() + word[1:]


def title_cased_list(field):
    return [to_title_case(word) if idx == 0 else word for idx, word in enumerate(field.split('_'))]


def title_case(field):
    """
    Takes a field from snake case to titlecase so it can be shown on the frontend to the end user

    Examples: 
    'phone_number' => 'Phone number'
    'verified' => 'Verified'


    :param field - all fields from the passed in dict
    :return titlecased string
    """
    return ' '.join(title_cased_list(field))


def add_to_parser(parser, field, type, required=False, error_message=None):
    if error_message is None:
        title_cased_field = title_case(field)
        error_message = f'{title_cased_field} is required.'
    parser.add_argument(field, type=type, required=required, help=error_message, location='json')
