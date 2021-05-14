import sys, json

def connection_message_generator(message_json, message_text):
    message_json = 'connection_value_json/{message_json}'.format(message_json = message_json)

    message_text = 'connection_messages/{message_text}'.format(message_text = message_text)

    message_values = {}
    message = ''

    try:
        with open(message_json) as message_values_data:
            message_values = json.load(message_values_data)
            
        with open(message_text) as reader:
            message = reader.readline()
            for value in message_values:
                target = '[{value}]'.format(value = value)
                message = message.replace(target, message_values[value])
        
        with open('output/output.txt', 'w') as writer:
            writer.writelines(message)

        print("Successfully created message! Check output folder for the message.")
    except:
        print('Unexpected error:', sys.exc_info()[0])

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print('Unexpected error: Invalid args')
    else: 
        connection_message_generator(sys.argv[1], sys.argv[2])
    
    