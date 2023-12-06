#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json

class Converter:
    def __init__(self):
        # Define the initial announcements
        self.jsonfile = {'annoucment1': 'help my patient is gone', 'annoucment2': 'help my patient is gone'}
        self.announcement = self.jsonfile

    # Parse announcements into a JSON file
    def parse_announcements(self):
        with open("announcements.json", "w") as file:
            json.dump(self.announcement, file, indent=4)
        print('Executed parsing')

    # Open the JSON file
    def open_json_file(self):
        with open("announcements.json", "r") as file:
            data = json.load(file)
            print(data)
        print('Executed open JSON file')

    # Edit an announcement
    def edit_announcement(self, announcement_key, new_text):
        with open("announcements.json", "r") as file:
            data = json.load(file)

        if announcement_key in data:
            data[announcement_key] = new_text
            with open("announcements.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Executed edit announcement: {announcement_key}")
        else:
            print(f"Announcement '{announcement_key}' not found.")

    # Delete an announcement
    def delete_announcement(self, announcement_key):
        with open("announcements.json", "r") as file:
            data = json.load(file)

        if announcement_key in data:
            del data[announcement_key]
            with open("announcements.json", "w") as file:
                json.dump(data, file, indent=4)
                print(data)
            print(f"Executed delete announcement: {announcement_key}")
        else:
            print(f"Announcement '{announcement_key}' not found.")

# Example usage
converter_instance = Converter()
converter_instance.parse_announcements()
converter_instance.open_json_file()
converter_instance.edit_announcement('annoucment1', 'nvm found him')
converter_instance.delete_announcement('annoucment2')

