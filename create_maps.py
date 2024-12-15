import os

def create_maps(base_name, count, start_number=1, base_path="."):
    for i in range(start_number, start_number + count):
        map_name = f"{base_name}_{i}"
        map_path = os.path.join(base_path, map_name)
        os.makedirs(map_path, exist_ok=True)
        fxmanifest_path = os.path.join(map_path, "fxmanifest.lua")
        with open(fxmanifest_path, "w") as fx_file:
            fx_file.write("""
fx_version 'cerulean'
game 'gta5'


files {
}
""".strip())
        stream_path = os.path.join(map_path, "stream")
        os.makedirs(stream_path, exist_ok=True)
    print(f"Done: Created {count} maps with the name '{base_name}_<number>'.")
    
base_name = "Your map name"
number_of_maps = 10  # Number of folders to create
start_number = 1    # Start numbering from 1
create_maps(base_name, number_of_maps, start_number)