import xml.etree.ElementTree as ET

input = '''

<people>
    <users>
        <user x="2">
            <id>001</id>
            <name>Jonathan</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Hannah</name>
        </user>
    </users>
</people>'''

people = ET.fromstring(input)
lst = people.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get("x"))