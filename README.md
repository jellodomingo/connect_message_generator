# LinkedIn Connect Message Generator

A really quick Python script to create connect messages used on the job hunt. 

There are three folders you need to have.
- connection_messages
- connection_value_json
- output

### Connection Messages folder

This folder should contain text files that will have the connect message that you want to use as a template. Create placeholders using the format of brackets and the value inside them. The script will replace the placeholder with the json values found in the json files within the connection_values_json folder.

Example:

> Hi there, I am very interested in your company, [company]. I would love the chance for a 10 minute chat to see if I am a great fit; if not now then maybe in the future. I am looking for a role as a [position] in your company. Please let me know if there is someone else on your team that I should reach out to instead. 

### Connection Values Json folder

This folder should contain json files that will fill in the placeholders
in the specified message text file. Label the keys to match the placeholders and the values should be the text you want to replace the placeholders with.

```json
{
    "company": "XYZ Company",
    "position": "Software Engineer"
}
```

### Output Folder

You will find the final message here as output.txt.

## How to Run
Clone the repo and run this command inside the same directory.

```shell
python connection_message_generator.py <json file> <text file>
```
Example
```shell
python connection_message_generator.py connection_message_1.json connection_message_1.txt
```

