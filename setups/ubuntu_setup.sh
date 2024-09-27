echo -E "Setting up all requirements"
echo -E "Installing all required packages"
apt-get install python3
if [ $? -eq 0 ]; then
    python3 -m pip install -r requirements.txt
    echo -E "All requirements installed successfully"
else
    echo -E "Failed to install requirements. You must be on python3, and use ubuntu. For windows users, please use setup.sh"
    exit 1
fi