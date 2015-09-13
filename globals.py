def enum(**named_values):
    return type('Enum', (), named_values)

Alert = enum(TEMP_LOW='temperature low', TEMP_HIGH='temperature high', ACTIVE='active', BARKING='barking')


