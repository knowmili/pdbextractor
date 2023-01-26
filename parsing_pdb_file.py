#seen = {}
for line in open("C:\\Users\\91898\\Dropbox\\My PC (LAPTOP-9P9FFH1A)\\Documents\\Milind\\M.Sc\\Project\\l\\1AKI_clean.pdb"):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        atom_type = list[1]
        type = list[2]
        residue = list[3]
        type_of_chain = list[4]
        atom_count = int(list[5])
        position = list[6:9]
        occupancy = float(list[7])
        b_factor = float(list[8])
        if atom_count >= 0:
            print(atom_type,type,residue,type_of_chain,atom_count,' '.join(position))
        print(f"X-Coordinate = {list[6]}, Y-Coordinate = {list[7]}, Z-Coordinate = {list[8]}")
                    
