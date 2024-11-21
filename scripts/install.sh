#!/bin/bash

# ----------- Création du Wrapper ------------ #
cd ..
echo "#!/bin/bash" >> scripts/wrapper.sh
echo "$(pwd)/main.py \"\$@\"" >> scripts/wrapper.sh
chmod a+wxr scripts/wrapper.sh
# -------------------------------------------- #

# ------ Copie du Wrapper dans /usr/bin ------ #
sudo cp scripts/wrapper.sh /usr/bin/fratb
sudo chmod a+wxr main.py