get = {
    'parameters': [{
        'name': 'id',
        'in': 'formData',
        'type': 'integer',
        'required': False,
        'description': 'id'
    }],
     "responses": {
        "200": {
          "description": "A list of gas station",
          "schema": {
            'id': 'gas_station',
              'properties':{
                'name':{
                  'type': 'string',
                  'description': 'Gas station name',
                  'default': ''
                },
                'place_id':{
                  'type': 'integer',
                  'description': 'Gas station place_id',
                  'default': ''
                },
                'latitude':{
                  'type': 'float',
                  'description': 'Gas station latitude',
                  'default': ''
                },
                'longitude':{
                  'type': 'float',
                  'description': 'Gas station longitude',
                  'default': ''
                },
                'rating':{
                  'type': 'float',
                  'description': 'Gas station rating',
                  'default': ''
                },
                'vicinity':{
                  'type': 'string',
                  'description': 'Gas station vicinity',
                  'default': ''
                }
              }
          },
          "examples": {
            "rgb": [
              "red",
              "green",
              "blue"
            ]
          }
        }
    }
}

post = {
    'parameters': [
        {
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Gas station name'
        },
        {
            'name': 'place_id',
            'in': 'formData',
            'type': 'integer',
            'required': False,
            'description': 'Gas station place_id'
        },
        {
            'name': 'latitude',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': True,
            'description': 'Gas station latitude'
        },
        {
            'name': 'longitude',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': True,
            'description': 'Gas station longitude'
        },
        {
            'name': 'rating',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': False,
            'description': 'Gas station longitude'
        },
        {
            'name': 'vicinity',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Gas station vicinity'
        },
    ],
     "responses": {
        "200": {
          "description": "A gas station created.",

        }
    }
}

