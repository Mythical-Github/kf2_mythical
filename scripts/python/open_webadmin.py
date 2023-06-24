import os
import json
import webbrowser

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'other', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_server_ip"]
part_b =data["webadmin_port"]
url = f"{part_a}:{part_b}"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

#using edge because wedadmin doesn't like firefox for me for whatever reason
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)