sentiment_analysis_schema = {
    'type': 'object',
    'properties': {
        'comments': {
            'type': 'array',
            'items': {
                'anyOf': [
                    {
                        'type': 'string',
                        'minLength': 1
                    }
                ]
            }
        }
    },
    'required': [
        'comments'
    ]
}