#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

# ----------- Création du Wrapper ------------ #
cd ..
WRAPPER_PATH="$(pwd)/scripts/wrapper.sh"
BIN_PATH="/usr/bin"

echo "#!/bin/bash" > "$WRAPPER_PATH"
echo "$(pwd)/main.py \"\$@\"" >> "$WRAPPER_PATH"
chmod +x "$WRAPPER_PATH"
echo -e "${RED}[*] Wrapper créé !${NC}"
# -------------------------------------------- #

# ------ Copie du Wrapper dans /usr/bin ------ #
sudo cp $WRAPPER_PATH $BIN_PATH/fratb
sudo chmod a+wxr main.py
echo -e "${RED}[*] Wrapper copié dans $BIN_PATH !${NC}"
# -------------------------------------------- #

# ---- Installation des librairies Python ---- #
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
echo -e "${RED}[*] Python configuré avec succès !${NC}"
# -------------------------------------------- #

echo -e "${RED}[*] Installation terminée avec succès !${NC}"